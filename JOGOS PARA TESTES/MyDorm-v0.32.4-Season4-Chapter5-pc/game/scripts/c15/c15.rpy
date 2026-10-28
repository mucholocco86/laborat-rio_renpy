label c15:
    python:
        _skipping = True
        for characterProfile in [ bet, dap, deb, eil, emm, eri, kat, kia, kim, lis, mar, mee, nor, sai, sam, sca, sim, oma, eva, ama, mad, meg ]:
            characterProfile._var("is known", True)
            characterProfile.initProfileImages ()
            while len (characterProfile.profileImages) > 0:
                characterProfile.profileImages.pop (0) # first remove
        oma.addProfileImage ("alexia_0")
        oma.addProfileImage ("notAvailable")
        oma.addProfileImage ("alexia_2")
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
        bet.addProfileImage ("betty_2")
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
        eil.addProfileImage ("eileen_2")
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
        emm.addProfileImage ("emma_7", "route")
        emm.addProfileImage ("emma_8", ["route", "itchio"])
        eri.addProfileImage ("erika_0")
        eri.addProfileImage ("erika_1")
        eri.addProfileImage ("erika_2")
        eri.addProfileImage ("erika_3")
        eri.addProfileImage ("erika_4")
        eri.addProfileImage ("erika_5")
        eri.addProfileImage ("notAvailable")
        eri.addProfileImage ("notAvailable")
        eri.addProfileImage ("erika_8", ["route", "itchio"])
        eva.addProfileImage ("eva_0")
        eva.addProfileImage ("eva_1")
        kat.addProfileImage ("kate_0")
        kat.addProfileImage ("notAvailable")
        kat.addProfileImage ("kate_2")
        kia.addProfileImage ("kiara_0")
        kia.addProfileImage ("notAvailable")
        kia.addProfileImage ("kiara_2")
        kia.addProfileImage ("notAvailable")
        kia.addProfileImage ("kiara_4")
        kim.addProfileImage ("kim_0")
        kim.addProfileImage ("notAvailable")
        kim.addProfileImage ("kim_2")
        kim.addProfileImage ("kim_3")
        lis.addProfileImage ("lisa_0")
        lis.addProfileImage ("notAvailable")
        lis.addProfileImage ("lisa_2")
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
        meg.addProfileImage ("megan_2")
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
        mee.addProfileImage ("olivia_2")
        sai.addProfileImage ("saira_0")
        sai.addProfileImage ("saira_1")
        sai.addProfileImage ("saira_2")
        sai.addProfileImage ("notAvailable")
        sai.addProfileImage ("notAvailable")
        sai.addProfileImage ("notAvailable")
        sai.addProfileImage ("notAvailable")
        sai.addProfileImage ("notAvailable")
        sai.addProfileImage ("saira_8")
        sam.addProfileImage ("samantha_0")
        sam.addProfileImage ("samantha_1")
        sam.addProfileImage ("samantha_2")
        sam.addProfileImage ("notAvailable")
        sam.addProfileImage ("samantha_4")
        sam.addProfileImage ("notAvailable")
        sam.addProfileImage ("notAvailable")
        sam.addProfileImage ("samantha_7", "route")
        sam.addProfileImage ("samantha_8", ["route", "itchio"])
        sca.addProfileImage ("scarlett_0")
        sca.addProfileImage ("scarlett_1")
        sca.addProfileImage ("scarlett_2")
        sca.addProfileImage ("notAvailable")
        sca.addProfileImage ("notAvailable")
        sca.addProfileImage ("scarlett_5")
        sca.addProfileImage ("notAvailable")
        sca.addProfileImage ("scarlett_7", "route")
        sca.addProfileImage ("scarlett_8", ["route", "itchio"])
        sim.addProfileImage ("simone_0")
        sim.addProfileImage ("simone_1")
        sim.addProfileImage ("simone_2")
        sim.addProfileImage ("notAvailable")
        sim.addProfileImage ("notAvailable")
        sim.addProfileImage ("notAvailable")
        sim.addProfileImage ("notAvailable")
        sim.addProfileImage ("notAvailable")
        sim.addProfileImage ("simone_8", ["route", "itchio"])
    if dap._var("route"):
        call c15s001_DapDate from _call_c15s001_DapDate
        call c15s002_DapLewd from _call_c15s002_DapLewd
    else:
        call c15s001_WakeUp from _call_c15s001_WakeUp
    #next day
    call c15s003_PickUpEileen from _call_c15s003_PickUpEileen
    call c15s003_LunchEileen from _call_c15s003_LunchEileen
    if eil._var("route"):
        call c15s004_LewdEileen from _call_c15s004_LewdEileen
    call c15s005_LisaDate from _call_c15s005_LisaDate
    call c15s005_BeforeAaronVisit from _call_c15s005_BeforeAaronVisit
    call c15s005_MeemawDiscussion from _call_c15s005_MeemawDiscussion
    call c15s006_AaronVisit from _call_c15s006_AaronVisit
    call c15s007_KiaraHouse from _call_c15s007_KiaraHouse
    call c15s007_Night from _call_c15s007_Night
    return
label c15s001_DapDate:
    if _in_replay:
        $ dap._var("route" , True)
        $ AuxReplay = True
        call mrS3_sam_route from _call_mrS3_sam_route_12
        if not sam._var("route"):
            call mrS3_sim_route from _call_mrS3_sim_route_14
            if not sim._var("route"):
                call mrS3_oma_route from _call_mrS3_oma_route_11
                if not oma._var("route"):
                    call mrS3_eri_route from _call_mrS3_eri_route_20
        call mrS3_wantsChildren from _call_mrS3_wantsChildren_1
    scene black with dissolve
    "[dap] introduce en el GPS la dirección del restaurante y conduces hasta allí. Está a poco menos de 20 minutos de la tienda de Maddie."
    call BlinkXP ("c15s001_005" , "d") from _call_BlinkXP_1002
    play music ("music/AmbientPianoStrings.ogg")
    dap "Ya hemos llegado. No te sorprendas por lo que veas ahí dentro..."
    dap "O mejor aún, sorpréndete."
    mc "Ya estoy sorprendido. Esto antes era un gimnasio, ¿no? ¿Ahora es un restaurante?"
    call BlinkXP ("c15s001_010" , "d") from _call_BlinkXP_1003
    dap "Son unos cuantos restaurantes... y algo más. Lo abrieron hace unos meses. Tenía ganas de venir, pero no tenía nadie con quién venir hasta que... tú y yo... ya sabes..."
    mc "[dap], puedes decir hasta que empezamos a salir."
    dap "Lo sé, pero se me hace raro decirlo."
    call BlinkXP ("c15s001_015" , "d") from _call_BlinkXP_1004
    dap "Pues ya estamos aquí."
    mc "¿Black Crow? Suena bien, debería haber mirado la página web. Pero es un poco pronto para ir a cenar, ¿no?"
    dap "No creas. Tenemos que ducharnos y pasar por la peluquería. Al menos yo. Contigo no van a poder hacer gran cosa."
    mc "¿Peluquería? *Risa* ¿Dónde me has traído?"
    dap "Entremos y lo verás."
    scene c15s001_020b with fade
    _("Recepcionista") "Buenas tardes, ¿tienen reserva?"
    mc "Sí, a nombre de Marks."
    scene c15s001_020c with hpunch
    dap "¡[mc] Marks!"
    scene c15s001_020An with dissolve
    _("Recepcionista") "Ah, vale, perfecto. Tienen reserva en el restaurante Black Crow."
    mc "Exacto."
    _("Recepcionista") "Entonces, subiendo por estas escaleras encontrarán el vestuario donde les atenderán mis compañeros."
    mc "Gracias."
    call BlinkXP ("c15s001_025" , "d") from _call_BlinkXP_1005
    mc "¿Vestuario? Ahí es donde nos podremos duchar, supongo."
    dap "Y cambiarnos. Vas a poder elegir a tu gusto. Tan solo recuerda esto. 14. Para ir a juego."
    mc "Estás siendo muy misteriosa."
    call BlinkXP ("c15s001_030" , "d") from _call_BlinkXP_1006
    dap "¿Quieres que te lo cuente todo y estropee la sorpresa?"
    mc "No, prefiero que me sorprendas, pero sigo pensando que es un poco pronto para cenar."
    dap "No te preocupes, entre ducha, cambiarme, y peluquería yo voy a tardar cerca de una hora."
    mc "¿Qué? ¿Una hora?"
    call KissXP ("c15s001_035" , "d") from _call_KissXP_27
    dap "Querrás que tu novia esté guapa en nuestra primera cita, ¿verdad?"
    mc "[dap], tú estás guapa siempre, pero esperaré. Cada vez siento más curiosidad."
    dap "Bueno, la curiosidad se acabará en cuanto entres por esa puerta. Nos vemos en una hora."
    scene c15s001_040a with dissolve
    "Es el momento de saber a qué viene tanto secretismo."
    scene c15s001_040b with fade
    "Entras en el vestuario y te está esperando alguien de la plantilla vestido como la recepcionista."
    "Elliot" "Buenas tardes, Sr. Marks. Soy Elliot y seré su Ayudante de Vestuario."
    "Elliot" "Tiene las duchas al fondo. Recomendamos su uso antes de cambiarse."
    mc "Perfecto. Venimos de la playa y necesito una ducha. Pero no he traído ropa."
    "Elliot" "Veo que es su primera vez en nuestras instalaciones. ¿Quiere que le explique cómo funciona?"
    mc "Por supuesto."
    scene c15s001_040c with dissolve
    "Elliot" "Lo primero que me tiene que decir es de qué siglo se quiere vestir. Puede ser XIV, XVI, o XVIII. Eso nos ayuda a que las salas sean más homogéneas y a la inmersión de los clientes."
    mc "Mi novia me ha dicho que recuerde el número 14. Supongo que se refería a esto. No sabía que era un restaurante temático."
    "Elliot" "Perfecto. Siendo el Siglo XIV puede escoger entre vestirse de caballero, cortesano, o pícaro. Teníamos un disfraz de campesino, pero no triunfó demasiado."
    mc "¿Caballero con armadura, espada y esas cosas?"
    scene c15s001_040d with dissolve
    "Elliot" "Sí a la armadura, no a la espada. No proporcionamos armas, lo siento. Pese a que es uno de los más populares, le tengo que avisar que no es el más cómodo."
    "Elliot" "Estar cenando con armadura, aunque sea falsa, puede resultar un poco incómodo si no está acostumbrado."
    mc "¿Podría probarme los tres y decidir?"
    "Elliot" "No lo podemos permitir por un tema de higiene. Todos nuestros disfraces se envían a la lavandería después de cada uso."
    mc "Entonces me disfrazaré de..."
    menu:
        "Pícaro":
            $ Aux = 2
        "Cortesano":
            $ Aux = 1
        "Caballero":
            $ Aux = 0
    scene c15s001_040e with dissolve
    "Elliot" "Perfecto. Pues si quiere pasar a la ducha y le preparo su ropa. Se la dejaré en la taquilla. Aquí tiene la llave. Número 93. La combinación es 23129. Supongo que no quiere servicio de peluquería."
    mc "No, no es necesario. ¿Por qué lo dice?"
    "Elliot" "Normalmente los clientes masculinos suelen rechazarlo a menos que lleven el pelo largo."
    mc "Entonces seré como el resto. *Risa* Rechazaré el servicio de peluquería."
    "Elliot" "Perfecto. Cuando esté listo, o si necesita ayuda para vestirse, llame a aquel timbre y volveré para acompañarle a la sala de espera."
    scene black with dissolve
    "Después de darle tu talla, pasas a la ducha. Está claro que han mantenido las instalaciones del antiguo gimnasio."
    "Al volver tienes tu disfraz en la taquilla. Tienes curiosidad por saber cómo te va a quedar. Y especialmente tienes curiosidad sobre cómo se va a vestir [dap]. Esperas haber acertado."
    if Aux == 0:
        scene c15s001_045a with dissolve
        mc "No quedo mal de caballero. Aunque el escudero tenía razón. No es muy cómodo. *Risa* Escudero... ya me estoy metiendo en el papel."
    elif Aux == 1:
        scene c15s001_045b with dissolve
        mc "El disfraz de cortesano es chulo. El tacto es suave. Me alegra haber hecho caso al sirviente y no haber cogido el de caballero. *Risa* Sirviente... ya me estoy metiendo en el papel."
    else:
        scene c15s001_045c with dissolve
        mc "Creo que Vilfredo vestirá así en la partida de DnD. Me alegra haber hecho caso al tabernero y no haber cogido el de caballero. *Risa* Tabernero... ya me estoy metiendo en el papel."
    scene c15s001_050a with dissolve
    "Justo cuando vas a pulsar el timbre para llamar a Elliot, te das cuenta de que no estás solo en el vestuario."
    _("Hombre") "Buenas tardes. ¿Siglo XIV?"
    mc "Hola, buenas tardes. Sí."
    _("Hombre") "Nosotros estuvimos la semana pasada. Hoy toca cenar en el Siglo XXXII. Lo han abierto esta semana. Supongo que mi mujer se disfrazará de Princesa Laia. ¿De qué se disfrazará su esposa?"
    mc "Mi novia. No lo sé, es la primera vez que venimos y yo ni siquiera sabía qué tipo de restaurante era."
    scene c15s001_050b with dissolve
    _("Hombre") "Si es la primera vez, prepárate para esperar. A nosotros nos dan tres o cuatro opciones, dependiendo del restaurante. A ellas les dan seis o siete."
    mc "Pero no pudiéndoselos probar, no tardarán tanto, ¿no?"
    scene c15s001_050c with dissolve
    _("Hombre") "No se los pueden probar, pero pueden verlos en la percha. Mi mujer se pasó 20 minutos intentando decidir entre siete vestidos la semana pasada."
    _("Hombre") "Y obviamente, una vez deciden el vestido, tienen que decidir qué peinado le pega mejor a ese estilo. Media hora más. Espero que tengas batería en el móvil. *Risa*"
    mc "*Risa* Sí, por suerte voy servido de batería."
    scene c15s001_050d with dissolve
    _("Hombre") "Bueno, te dejo con tu espera. Ahí viene mi copiloto."
    mc "Que pase una buena noche."
    _("Hombre") "Igualmente, hijo."
    scene black with dissolve
    "Elliot os lleva a diferentes salas de espera y te sientas a hacer tiempo hasta que [dap] esté preparada. Por lo que ha dicho el hombre en el vestuario, te tocará esperar un rato."
    stop music fadeout (1.5)
    "Cuando ya has leído todas las noticias locales, internacionales, sobre videojuegos, e incluso sobre la vida de los famosos..."
    play sound ("music/RingtoneMC.ogg")
    "*Ring-Ring*"
    mcp "(¿Número oculto?)"
    if Aux == 0:
        scene c15s001_055a with dissolve
    elif Aux == 1:
        scene c15s001_055b with dissolve
    else:
        scene c15s001_055c with dissolve
    call c15s001_AmandaCall from _call_c15s001_AmandaCall
    if Aux == 0:
        scene c15s001_055e with dissolve
    elif Aux == 1:
        scene c15s001_055f with dissolve
    else:
        scene c15s001_055g with dissolve
    "Justo al colgar, oyes pasos en las escaleras por las que has bajado."
    play music ("music/TheBritons.ogg")
    dap "¿Llevas mucho tiempo esperándome?"
    scene c15s001_095d with dissolve:
        yalign 1.0
        linear 5.0 yalign 0.0
    pause (5.0)
    call BlinkXP ("c15s001_095" , "d") from _call_BlinkXP_1007
    $ renpy.notify ("Profile Image unlocked for Daphne: 12 - Special (I)")
    $ dap.addProfileImage ("notAvailable")
    $ dap.addProfileImage ("notAvailable")
    $ dap.addProfileImage ("daphne_11", "route")
    mc "¡Wow, [dap]! ¡Pareces salida de un cuento de hadas! Estás preciosa."
    dap "¡Gracias, [mc]! Me preocupaba quedar ridícula."
    if Aux == 0:
        dap "Tú también estás muy guapo, pero no sé si va a ser cómodo cenar con la armadura."
        mc "Me lo ha comentado el ayudante del vestuario, pero no podía dejarlo pasar."
        scene c15s001_100AnBlink
        dap "Lástima que no hayas hecho a Vilfredo un guerrero o un paladín. Me hubiera gustado imaginarte así en la partida."
    elif Aux == 1:
        dap "Tú también estás muy guapo, te queda genial el look de... ¿príncipe?"
        mc "Oficialmente cortesano, pero si quieres que sea tu príncipe solo tienes que pedirlo."
        scene c15s001_100AnBlink
        dap "Lástima que no hayas hecho a Vilfredo noble. Me hubiera gustado imaginarte así en la partida."
    else:
        dap "Tú también estás muy guapo, te queda genial el look de... ¿espadachín?"
        mc "Me lo han ofrecido como pícaro y, después de generar el personaje de Vilfredo, no podía dejarlo pasar. Quiero que vista parecido a esto, si es posible."
        scene c15s001_100AnBlink
        dap "Ningún problema. No me perdería un pícaro tan guapo por nada del mundo."
    mc "Vas a hacer que este pobre pícaro se ruborice. *Risa*"
    call BlinkXP ("c15s001_105" , "d") from _call_BlinkXP_1008
    dap "¿Pasamos a cenar? Tengo ganas de ver el restaurante."
    mc "Cuando quieras. A mí me ha entrado hambre mientras esperaba. Pero la espera ha valido la pena."
    if Aux == 0:
        call KissXP ("c15s001_110a" , "d") from _call_KissXP_28
        dap "Gracias, mi amable caballero."
    elif Aux == 1:
        call KissXP ("c15s001_110b" , "d") from _call_KissXP_29
        dap "Gracias, mi apuesto príncipe."
    else:
        call KissXP ("c15s001_110c" , "d") from _call_KissXP_30
        dap "Gracias, mi pícaro seductor."
    call BlinkXP ("c15s001_115" , "d") from _call_BlinkXP_1009
    "Llamáis al timbre y aparece alguien nuevo del personal."
    "Mathilda" "Buenas tardes les de Dios a vuesas mercedes. Mi nombre es Mathilda. Si tienen el placer de acompañarme, les guiaré a su mesa para que puedan disfrutar del yantar."
    call BlinkXP ("c15s001_120" , "d") from _call_BlinkXP_1010
    dap "Cuando quiera. Estamos listos."
    mc "*Susurrando* Ahora pillo lo del acento raro del tipo que me cogió el teléfono. Era este falso acento medieval."
    call BlinkXP ("c15s001_125" , "d") from _call_BlinkXP_1011
    dap "De momento me está gustando, y eso que aún no hemos visto el restaurante."
    mc "El vestido te queda increíble, y el peinado te hace preciosa... más preciosa de lo habitual."
    call BlinkXP ("c15s001_130" , "d") from _call_BlinkXP_1012
    dap "Gracias, pero debería haberme quedado con mi trenza. También pega con el vestido y hubiera estado más cómoda. No me siento demasiado confortable con esto."
    mc "Bueno, cuando volvamos al vestuario tendrás que devolver todo, incluidos los anillos del pelo. Solo será una hora o dos, ¿no?"
    scene c15s001_135An with fade
    "Atravesáis todo el restaurante y Mathilda os lleva a una zona que parece tranquila. El restaurante parece salido de una película. Al menos es una de aquellas películas donde todo está limpio."
    call BlinkXP ("c15s001_135" , "d") from _call_BlinkXP_1013
    "Mathilda" "Hoy está bastante vacío, y esta es la zona más resguardada de miradas ajenas. ¿Les va bien sentarse aquí?"
    mc "Gracias, Mathilda, es perfecto."
    "Mathilda" "¿Saben cómo funciona el menú? Si quieren se lo explico."
    mc "Sí, por favor."
    "Mathilda" "Nuestros platos son típicos de la Europa medieval, pero con un toque moderno, con lo que pueden encontrar ingredientes como patata o maíz, que no estaban disponibles en la época."
    "Mathilda" "Nosotros recomendamos el menú degustación mixto, de carne, o de pescado, donde podrán disfrutar de algunas de nuestras especialidades. También pueden pedir platos individuales."
    call BlinkXP ("c15s001_140" , "d") from _call_BlinkXP_1014
    dap "Yo querré el menú degustación mixto. Y cerveza tostada para beber."
    mc "¿Qué platos individuales tienen? Cosas con carne, por favor."
    call BlinkXP ("c15s001_145" , "d") from _call_BlinkXP_1015
    "Mathilda" "Tenemos asado del pastor, que lleva patata sustituyendo al nabo, cazuela del granjero, que lleva maíz para sustituir a la avena, chuletas con salsa de calabaza, o albóndigas de ternera."
    "Mathilda" "El menú degustación de carne consiste en asado del pastor, cazuela del granjero y las albóndigas de ternera. Normalmente lo recomendamos para compartir entre dos personas."
    "Mathilda" "Con una ensalada o unas verduras para compartir como complemento."
    mc "¿Ensalada? ¿Verduras? *Risa* Esa es la comida de mi comida... Siempre he querido decir esa frase."
    menu:
        "Tomaré el menú degustación":
            $ Aux2 = 4
        "Tomaré asado del pastor":
            $ Aux2 = 0
        "Tomaré la cazuela del granjero":
            $ Aux2 = 1
        "Tomaré las chuletas con salsa de calabaza":
            $ Aux2 = 2
        "Tomaré las albóndigas de ternera":
            $ Aux2 = 3
    mc "Pero si algún plato lleva brócoli, no lo ponga, por favor. Soy alérgico."
    "Mathilda" "Como vuesa merced desee. ¿Para beber, señor?"
    mc "Agua. Tengo que conducir luego."
    call BlinkXP ("c15s001_150" , "d") from _call_BlinkXP_1016
    dap "Tráigale una cerveza tostada también a él. Vamos a tardar mucho en coger el coche."
    call BlinkXP ("c15s001_145b" , "d") from _call_BlinkXP_1017
    "Mathilda" "Perfecto. Voy a cursar su pedido y ahora mismo les traigo la bebida."
    call BlinkXP ("c15s001_155" , "d") from _call_BlinkXP_1018
    dap "¿Desde cuándo eres alérgico al brócoli? No lo sabía."
    mc "*Risa* No soy alérgico, pero para mí estropea cualquier comida. Siempre digo \"si lleva brócoli no lo pongan\" y la mitad de las veces se olvidan."
    mc "Diciendo que soy alérgico, van con cuidado de no ponerlo. No se han olvidado ni una sola vez."
    dap "Es una buena idea. Poco honesta, pero buena idea. Aunque si pidiéndolo correctamente no te hacen caso, es la única forma que te queda de hacerlo."
    call BlinkXP ("c15s001_160" , "d") from _call_BlinkXP_1019
    dap "Cambiando de tema, ¿qué te parece el sitio? Es original, ¿verdad?"
    mc "Es muy original, e ir así vestidos le da un giro interesante, es como si tuvieras una inmersión total."
    dap "Yo siempre he querido probar algo así, sentirte dentro de una partida de DnD, aunque solo sea durante la cena."
    mc "Si en la partida visitamos una taberna o una posada, será difícil imaginársela diferente a esto."
    call BlinkXP ("c15s001_165" , "d") from _call_BlinkXP_1020
    dap "Esa era una de las razones para traerte aquí. *Risa* Quiero que sepas qué cosas me gustan. No hemos tenido mucho tiempo de hablar de hobbies y nimiedades."
    mc "Bueno, sé que te gusta estudiar, leer y aprender, los videojuegos, los juegos de rol... ¿la música pop?"
    dap "*Risa* Sí, la música pop. Si llegas a fallar en eso... Te hubiera torturado con los peores discos de Taylor Shift. *Risa*"
    call BlinkXP ("c15s001_170" , "d") from _call_BlinkXP_1021
    dap "Pero a lo que me refiero es a que me encanta este ambiente. Hacer cosas diferentes. No soy tan aventurera como [emm], pero en un sitio así me siento... especial."
    mc "[dap], tú eres especial. Nunca se me hubiera ocurrido venir a un restaurante así, con lo que la noche ya es diferente."
    mc "Pasarla contigo, vestida así, la hace verdaderamente especial."
    call BlinkXP ("c15s001_175" , "d") from _call_BlinkXP_1022
    dap "No creía que vestirme de molinera para una cita fuera lo mejor, lo mismo que de tabernera. Imagínate que las otras mesas empiezan a pedirme cosas. *Risa*"
    mc "Vestida de tabernera seguro que estabas monísima, pero no puedo imaginarme a una molinera sexy. *Risa* Ni siquiera a ti."
    dap "Había un disfraz de guerrera, pero seguía la norma de Hollywood para las armaduras femeninas de que cuanto menos cubra más protege. *Risa*"
    mc "Interesante. No me hubiera importado verte así. *Risa*"
    dap "No seas impaciente. *Risa* Me verás con menos cobertura hoy... si quieres..."
    mc "Por supuesto que quiero, si es lo que quieres tú."
    call BlinkXP ("c15s001_180" , "d") from _call_BlinkXP_1023
    dap "Llevo deseándolo desde nuestra segunda lección. Con lo que sí. Es lo que quiero."
    mc "Yo también llevo tiempo deseándolo."
    "Justo en ese momento, Mathilda trae las cervezas."
    call BlinkXP ("c15s001_185" , "d") from _call_BlinkXP_1024
    dap "Por una noche especial con mi novio. Mi primer novio."
    mc "Por la chica más especial de la noche."
    scene c15s001_190AnBlink
    dap "¡Está buenísima!"
    mc "*Risa*"
    call BlinkXP ("c15s001_195" , "d") from _call_BlinkXP_1025
    dap "¿Qué pasa?"
    mc "Que estás super graciosa con el bigote de espuma, aunque no te pega con el vestido. *Risa* Te pegaría más con un uniforme de fontanero y una gorra roja."
    call BlinkXP ("c15s001_200" , "d") from _call_BlinkXP_1026
    dap "¡Oops, perdón! *Risa* Tendré que beber como una princesita."
    mc "*Risa*. Ya te he dicho que estabas muy graciosa."
    call BlinkXP ("c15s001_205" , "d") from _call_BlinkXP_1027
    dap "Pero no quiero estar graciosa. Quiero estar guapa y sexy para ti en nuestra primera cita."
    mc "[dap], ya te he dicho que estabas preciosa. Y lo de estar sexy lo llevas dentro, no tienes que hacer nada especial para estarlo."
    call BlinkXP ("c15s001_210" , "d") from _call_BlinkXP_1028
    dap "Entonces, ¿me harías el amor esta noche, aunque no llevase este vestido?"
    mc "Espero que cuando hagamos el amor no lo lleves. *Risa* Pero sí, te haría el amor aunque fueras con un saco de patatas en vez de con ese vestido."
    call BlinkXP ("c15s001_215" , "d") from _call_BlinkXP_1029
    dap "Perfecto, porque no pienso dejarte escapar esta noche."
    mc "No tengo intención de escaparme. Esta noche soy todo para ti."
    call BlinkXP ("c15s001_220" , "d") from _call_BlinkXP_1030
    dap "Sabes que, si seguimos hablando de esto, voy a estar pensando en lo que pasará después toda la cena, ¿verdad?"
    mc "¿Quieres cambiar de tema?"
    call BlinkXP ("c15s001_225" , "d") from _call_BlinkXP_1031
    dap "El problema es que ahora mismo solo me apetece hablar sobre nosotros y de nuestra relación."
    dap "Sobre qué piensas que va a pasar con nosotros... somos primos..."
    mc "Me da lo mismo que lo seamos, [dap]."
    if not persistent.family:
        mc "Y más teniendo en cuenta que los dos sabemos que no lo somos."
        call BlinkXP ("c15s001_230" , "d") from _call_BlinkXP_1032
        dap "Lo sé, pero todo el mundo piensa que sí. Bueno, todo el mundo no. Mi madre lo sabe y lógicamente la tuya también... y la abuela... y Tía Betty, supongo... Y a [sca] se lo dije yo."
    else:
        call BlinkXP ("c15s001_230" , "d") from _call_BlinkXP_1033
    dap "Pero ¿qué pensará la gente si lo hacemos público? ¿Mi hermana o la tuya? ¿[eil] o Jamaal? Ya viste las caras de las estudiantes cuando me besaste durante el juego."
    mc "¿Te soy sincero? No me importa lo que piensen. Lo único que deben pensar es que estoy con una chica maravillosa que me hace feliz."
    mc "Quiero pasar el resto de mi vida contigo, [dap]. Quiero que envejezcamos juntos. Quiero que sepas lo importante que eres para mí. Y quiero que todo el mundo lo sepa también."
    mc "¿Y a ti? ¿Te importa lo que piensen los demás?"
    call BlinkXP ("c15s001_235" , "d") from _call_BlinkXP_1034
    dap "Después de lo que acabas de decir... no debería decir que me importe... pero me importa. No sé cómo decírselo a mi hermana. O al resto de la familia."
    dap "Quiero hacerlo, pero no sé cómo... cualquier escenario que en el que puedo pensar acaba en discusión... con mi madre, con la tuya, con la abuela..."
    mc "Se lo puedes decir con un beso..."
    call BlinkXP ("c15s001_240" , "d") from _call_BlinkXP_1035
    dap "¡[mc]! ¡Ya te dije que no beso a chicas! ¡Lo de [sca] fue solo para aprender!"
    mc "*Risa* No me refería a que las besaras a ellas, sino a que me besaras a mí delante de ellas."
    call BlinkXP ("c15s001_245" , "d") from _call_BlinkXP_1036
    "La conversación es interrumpida por Mathilda, que llega con la comida."
    "Mathilda" "Aquí traigo su yantar. Disfruten de nuestros manjares. ¿Puedo ofrecerles algo más a vuesas mercedes?"
    scene c15s001_250AnBlink with dissolve
    dap "Por mí no, gracias. Esto tiene una pinta deliciosa."
    mc "Por mí tampoco, gracias."
    scene c15s001_255a with dissolve
    dap "Esto tiene una pinta excelente. ¿Qué tal lo tuyo?"
    if Aux2==0:
        scene c15s001_255b with dissolve
    elif Aux2==1:
        scene c15s001_255c with dissolve
    elif Aux2==2:
        scene c15s001_255d with dissolve
    elif Aux2==3:
        scene c15s001_255e with dissolve
    else:
        scene c15s001_255f with dissolve
    mc "Tiene muy buena pinta. Cuidan hasta el mínimo detalle, fíjate en los platos."
    call BlinkXP ("c15s001_260" , "d") from _call_BlinkXP_1037
    dap "Ya te he dicho que tenía ganas de venir. Los comentarios en ThreeSquare eran muy buenos para un sitio que lleva tan poco tiempo abierto. ¿Empezamos?"
    mc "Sí, pero estábamos hablando de hacer público lo nuestro."
    call BlinkXP ("c15s001_265" , "d") from _call_BlinkXP_1038
    dap "Sí, y tú has dicho que te bese delante de mi madre o de [eri]. *Risa* Estás loco. ¿O crees que soy tonta?"
    if sam._var("route") or sim._var("route") or oma._var("route") or eri._var("route"):
        mc "No es tan mala idea. Ha funcionado con anterioridad."
        call BlinkXP ("c15s001_270" , "h") from _call_BlinkXP_1039
        dap "{b}¿Qué? ¿Quién? ¿Cuándo?{/b} ¿Cómo se lo tomaron?"
        mc "Sigo vivo, con lo que la cosa no acabó mal. *Risa*"
    else:
        mc "No me parece una mala idea. Eres tú quien tiene que decidir si quieres que lo sepan y cuando quieres que lo sepan."
    call BlinkXP ("c15s001_275" , "d") from _call_BlinkXP_1040
    dap "Yo no podría hacerlo. Sabes que soy más de hablar que de actuar."
    mc "Entonces tendremos que buscar el momento correcto para explicarlo. O puedo besarte yo."
    dap "Prefiero hablarlo, a ser posible de una en una. Primero [eri], después mi madre. Con un poco de suerte cuando le toque a la abuela ya estará de nuevo en Florida."
    mc "¡Cuánto miedo le tenéis todas a Meemaw!"
    call BlinkXP ("c15s001_280" , "d") from _call_BlinkXP_1041
    dap "¿Le tenemos? ¿Todas? ¿Quién más?"
    mc "Ermmm... tu madre, por ejemplo. Desde que sabemos que venía, ha estado preocupada sobre lo que diría sobre la casa... y esas cosas..."
    call BlinkXP ("c15s001_285" , "d") from _call_BlinkXP_1042
    dap "Ah, vale, te refieres a eso. ¡Qué susto! Creía que te referías a que estabas con alguien más de la familia... y no estoy preguntando porque sé que no vas a contestar."
    call BlinkXP ("c15s001_290" , "d") from _call_BlinkXP_1043
    dap "Pero volviendo al tema encima de la mesa. Tú querrías hacerlo público y yo no estoy preparada. ¿Te importa que nos lo tomemos con calma?"
    mc "Mientras me sigas dejando disfrutar de tu compañía, mientras me dejes seguir besándote y acariciándote, no me importa quién lo sepa."
    mc "¿Preferiría poder llegar a casa y decírselo a todo el mundo? Por supuesto, pero no te voy a forzar a ello."
    call BlinkXP ("c15s001_295" , "d") from _call_BlinkXP_1044
    dap "Gracias, [mc]."
    dap "Cambiando de tema, ¿cómo nos ves en cinco años?"
    mc "Eso es más una pregunta para una entrevista de trabajo que para una cita. *Risa* Pero es fácil de contestar."
    scene c15s001_300d with dissolve
    if persistent.pregnancy or mc._var("wantsChildren"):
        mc "Me gustaría tener, como mínimo, una pequeña [dap] correteando por casa."
    mc "Me gustaría que hubieras acabado tus estudios y encontrases algún trabajo que te llenara en un sitio donde pudiéramos estar juntos."
    scene c15s001_300e with dissolve
    mc "Me gustaría que mirásemos hacia atrás, a esta noche, y pensáramos \"¿Ya han pasado cinco años?\" y nos sorprendiéramos."
    scene c15s001_300a with dissolve
    mc "Me gustaría que de lo único que nos arrepintiéramos fuera de no haber empezado antes, de haber desperdiciado unos preciosos días juntos."
    call BlinkXP ("c15s001_300" , "d") from _call_BlinkXP_1045
    dap "¡Joder, [mc]! ¡No podías haber dicho algo más bonito!"
    mc "No se lo podía haber dicho a alguien más bonita."
    scene c15s001_305AnBlink
    dap "¡Un brindis porque todo lo que has dicho se cumpla!"
    mc "¡Brindo por ello!"
    scene c15s001_310AnBlink
    dap "Veo que lo de beber como una princesa no se me da bien. A lo mejor puedo trabajar aquí de tabernera. *Risa*"
    mc "Es posible. *Risa* Pero siempre serás mi princesa. Tengo una duda."
    dap "Dime."
    if persistent.pregnancy or mc._var("wantsChildren"):
        mc "Has brindado por que se cumpla todo. ¿Todo? ¿Incluida la pequeña [dap]?"
        call BlinkXP ("c15s001_315" , "d") from _call_BlinkXP_1046
        dap "*Susurrando* ¿Tú has traído condones? Porque yo no estoy con la pastilla, nunca la he necesitado, y no voy a empezar ahora."
        mc "No, no he traído."
        call BlinkXP ("c15s001_320" , "d") from _call_BlinkXP_1047
        dap "Entonces podemos ir a comprarlos cuando acabemos de cenar, o podemos hacer el primer intento de hacer a la pequeña [dap]."
        dap "Hoy quiero hacer el amor contigo, si quieres con condón, si quieres sin. No me da miedo quedarme embarazada. Sé que voy a pasar el resto de mi vida contigo."
        dap "Y no quiero que, dentro de cinco años, cuando miremos hacia atrás, a esta noche, nos arrepintamos de no haberlo hecho."
        dap "La pequeña [dap] va a tener una gran familia. Quiero que la disfrute el máximo de tiempo posible."
        mc "Sabes que ahora mismo me podría levantar y besarte, ¿verdad?"
        call BlinkXP ("c15s001_325" , "d") from _call_BlinkXP_1048
        dap "Después del discurso que acabo de soltar, me están temblando las piernas. Pero si te levantas y me besas, nos vamos a tener que ir sin acabar de cenar. Dudo que pudiera parar."
        dap "Mejor guarda esos besos para cuando estemos solos. Los vas a necesitar."
        mc "No te preocupes, no se agotan."
        mc "¿Tienes pensado algún nombre para la pequeña [dap]?"
        call BlinkXP ("c15s001_330" , "d") from _call_BlinkXP_1049
        dap "Sí. Me gustan Maeve y Claire. También me gusta Hope, pero es un nombre que [eri] siempre ha querido ponerle a nuestra hermana, si mi madre encontraba a alguien."
        dap "Supongo que con la edad que tiene mi madre, ese nombre pasará a la hija de [eri] cuando ella encuentre un chico que valga la mitad de lo que vales tú."
        mc "Me gustan los dos nombres. *Risa* Podemos seguir tu tradición familiar y tener gemelas."
        call BlinkXP ("c15s001_335" , "d") from _call_BlinkXP_1050
        dap "Si pudiera elegirlo, las tendría. *Risa* Pero no es algo que se elija."
        mc "Lo sé, pero sería bonito tener dos pequeñas [dap] correteando por casa en vez de solo una."
        dap "Sí, sería bonito... pero todo se andará."
    mc "Sobre lo del trabajo, sé que vas a estudiar Química. ¿De qué quieres trabajar? ¿Qué posibilidades laborales tienes en Newport?"
    call BlinkXP ("c15s001_340" , "d") from _call_BlinkXP_1051
    dap "Enseñar en la NWU o en algún instituto. O investigación, que es lo que me gustaría, en la NWU o en la Cal Poly."
    dap "En San Luís, en Paso Robles, o en Atascadero hay algunas empresas donde también podría trabajar. Pero vete a saber cómo estará el tema laboral en cuatro años."
    mc "Con lo que podrías seguir viviendo en Newport, ¿no?"
    call BlinkXP ("c15s001_345" , "d") from _call_BlinkXP_1052
    dap "No lo sé. Me tendrían que contratar en alguno de esos sitios. Pero nunca había pensado en mudarme. Me gustaría vivir en Newport siempre. ¿Qué opinas?"
    mc "Que me da lo mismo donde vivamos. Pero a mí también me gustaría quedarme en Newport."
    dap "¿Y tú? ¿Qué planes tienes para el futuro? Una vez el Dormitorio esté totalmente en marcha, vas a tener muy poco trabajo."
    mc "He estado haciendo números, y no pintan bien. Con lo que pagan 12 chicas, y una vez se acabe la subvención extra que nos da la NWU, los números salen muy justos."
    call BlinkXP ("c15s001_350" , "d") from _call_BlinkXP_1053
    dap "¿Tan mal estamos?"
    mc "Entre impuestos y los costes operativos estimados, quedarán un par de sueldos medianos. Somos tres personas trabajando, con lo que seguramente tendré que buscar algo. En Newport o alrededores."
    mc "La NWU nos subvenciona este año y el que viene, con lo que tengo tiempo para buscar algo."
    call BlinkXP ("c15s001_355" , "d") from _call_BlinkXP_1054
    dap "Mierda. Si fueran cuatro años, yo podría aportar mis ingresos en vez de generar gastos, pero en dos años..."
    mc "No es una noche para que te preocupes, cielo. Los dos primeros años estaremos bien, y después ya se verá. Pero no tendré problemas en encontrar trabajo en Newport o los alrededores."
    call BlinkXP ("c15s001_360" , "d") from _call_BlinkXP_1055
    "En ese momento llega Mathilda..."
    "Mathilda" "¿Han disfrutado de la comida? ¿Puedo ofrecerles algún dulce?"
    mc "Estaba todo muy bueno, pero yo voy a tener que renunciar al postre."
    call BlinkXP ("c15s001_365b" , "d") from _call_BlinkXP_1056
    dap "Todo estaba exquisito, pero yo también voy a pasar. ¿Nos puede cargar la cuenta a la habitación?"
    mc "¿Qué habitación?"
    scene c15s001_365AnBlink with dissolve
    dap "¡Hush, [mc]!"
    dap "La habitación está a nombre de Marks, [dap] Marks."
    call BlinkXP ("c15s001_360b" , "d") from _call_BlinkXP_1057
    "Mathilda" "Sin ningún problema. No olviden recoger sus cosas de los vestuarios, por la mañana estarán cerrados. Los disfraces los pueden dejar en la habitación."
    "Mathilda" "Esperamos verles de nuevo en nuestras instalaciones."
    mc "Gracias, Mathilda. Creo que volveremos."
    call BlinkXP ("c15s001_365b" , "d") from _call_BlinkXP_1058
    dap "Es probable que volvamos. Ha sido una experiencia muy buena. Gracias, Mathilda."
    call BlinkXP ("c15s001_370" , "d") from _call_BlinkXP_1059
    dap "¿Vamos?"
    mc "¿Qué es eso de la habitación?"
    dap "Ya te he dicho que había varios restaurantes. El Black Crow es éste, el Pitch Raven es el de ciencia ficción, y el Nigrum Corvus es el de la era clásica, romanos, griegos, y esas cosas."
    dap "Y después tienen la Red Crow Inn, con habitaciones temáticas. Tenemos una habitación medieval, aunque seguramente no se parezca en nada a como dormían entonces."
    mc "Así que la otra reserva a nombre de \"otros\" Marks era tuya, ¿no?"
    call BlinkXP ("c15s001_375" , "d") from _call_BlinkXP_1060
    dap "Sí. Te hice reservar el restaurante por si querías meterte en la web y cambiar la época. La habitación la tenía elegida yo. Me parece más romántica la medieval que la de ciencia ficción."
    mc "Me ha encantado el Black Crow, con lo que me alegro de no haberlo hecho. La próxima vez, podemos probar uno de los otros."
    call BlinkXP ("c15s001_380" , "d") from _call_BlinkXP_1061
    dap "Mejor no..."
    mc "¿Pasa algo, [dap]?"
    dap "Si estamos mal de dinero, me conformo con que la próxima vez sea en un Burger Prince y durmamos en un motel. Si es contigo, me da lo mismo el sitio."
    mc "Es caro, ¿verdad?"
    dap "Un poco, pero no te preocupes. La habitación ya está pagada. Solo me falta pagar la cena."
    mc "¿De dónde has sacado el dinero, [dap]?"
    call BlinkXP ("c15s001_385" , "d") from _call_BlinkXP_1062
    dap "Había estado ahorrando la paga para comprarme un nuevo portátil gaming. He invertido parte de ese dinero en la habitación y en la cena."
    mc "De eso nada, cielo. No puedo hacer nada con la habitación, pero no voy a permitirte pagar la cena. Igual que tú no vas a permitirme devolverte el dinero de la habitación, ¿verdad?"
    call BlinkXP ("c15s001_390" , "d") from _call_BlinkXP_1063
    dap "¡Ni de coña! Ha sido elección mía y lo pago yo todo."
    mc "Eso no va a pasar. La cena corre de mi cuenta. Tú has ahorrado para ese portátil y te lo mereces."
    call BlinkXP ("c15s001_395" , "d") from _call_BlinkXP_1064
    dap "Bueno, ya lo hablaremos mañana. Es el momento de ver la habitación."
    mc "¡Vamos!"
    return
label c15s001_AmandaCall:
    if _in_replay and not AuxReplay:
        call mrS3_dap_route from _call_mrS3_dap_route_21
        if not dap._var("route"):
            call mrS3_emm_route from _call_mrS3_emm_route_27
            if not eri._var("route"):
                call mrS3_eri_route from _call_mrS3_eri_route_21
    mc "¿Hola? ¿Quién es?"
    stop sound
    play music ("music/ForWhenItRains.ogg")
    call BlinkXP ("c15s001_060" , "d") from _call_BlinkXP_1065
    ama "Hola, [mc]. No quiero molestarte demasiado."
    mc "No molestas, Amanda. ¿Puedo ayudarte en algo?"
    call BlinkXP ("c15s001_065" , "d") from _call_BlinkXP_1066
    if dap._var("route"):
        ama "Me iba a acostar cuando he recibido una llamada y te tenía que avisar."
        ama "Aaron, nuestro supervisor, llega mañana por la mañana y él querría reunirse con vosotros por la tarde para explicaros la situación."
    else:
        ama "Me acaban de despertar con una llamada y te tenía que avisar."
        ama "Aaron, nuestro supervisor, acaba de aterrizar y él querría reunirse con vosotros esta tarde para explicaros la situación."
    mc "¿Nosotros? ¿[mar], [nor], [emm], [eri], [dap] y yo?"
    call BlinkXP ("c15s001_070" , "d") from _call_BlinkXP_1067
    ama "De momento solo con [mar], [nor] y contigo. Eva y yo también vamos a estar ahí, y las chicas podrían flipar un poco."
    ama "Además, no es cosa nuestra decirles la verdad, sino de sus madres."
    if emm._var("route") or eri._var("route") or dap._var("route"):
        ama "Y tuya."
    mc "Lo entiendo. No me gusta ocultarles la verdad, pero hablaré con [mar] y con [nor]. ¿A qué hora os esperamos?"
    call BlinkXP ("c15s001_075" , "d") from _call_BlinkXP_1068
    ama "A las 1700. Aaron volará fuera del país por la noche."
    mc "Intentaré que las chicas no estén en casa a esa hora. ¿Cuánto tiempo necesitáis que estén fuera?"
    scene c15s001_080 with dissolve
    ama "No más de una hora, supongo. Depende de las preguntas que tengáis. Por eso es mejor que sólo estéis [nor], [mar], y tú. Nada de Olivia o Betty."
    mc "Van a querer estar. También sufrieron el... *Susurro* secuestro."
    call BlinkXP ("c15s001_080b" , "d") from _call_BlinkXP_1069
    ama "Es posible que sea la última vez que nos veamos. Nuestra misión con vosotros ya está acabando."
    mc "¿Aaron se os va a llevar? ¿A alguna base de NTR?"
    call BlinkXP ("c15s001_085" , "d") from _call_BlinkXP_1070
    ama "Aaron solo quiere hablar con vosotros de momento. El resto ya se verá."
    ama "Por cierto, deberíais informar a [mar] de lo que pasó el lunes con Eric y los demás. Nos ahorraremos preguntas incómodas."
    mc "No te preocupes, hablaré con ella antes de que lleguéis."
    call BlinkXP ("c15s001_090" , "d") from _call_BlinkXP_1071
    if dap._var("route"):
        ama "Perfecto. Entonces nos vemos mañana por la tarde. Feliz Navidad de nuevo, [mc]."
        mc "Hasta mañana. No sé si es un poco tarde para seguir celebrando la Navidad, pero Feliz Navidad de nuevo, Amanda."
    else:
        ama "Perfecto. Entonces nos vemos esta tarde. A las 1700."
        mc "Hasta luego, Amanda."
    stop music fadeout (1.5)
    return
label c15s001_WakeUp:
    centered "{size=+20}{b}DÍA 17 – JUEVES{/b}{/size}"
    play sound ("music/RingtoneMC.ogg")
    "*Ring-Ring*"
    "Suena el teléfono y te saca de tus sueños, si es que los has tenido. Despertarse tan de golpe ha hecho que olvides lo que estabas soñando."
    mcp "(¿Número oculto?)"
    stop sound
    scene c15s001_055d with dissolve
    call c15s001_AmandaCall from _call_c15s001_AmandaCall_1
    "Cuando cuelgas te das cuenta de que has dormido hasta tarde. Casi no vale la pena bajar a desayunar."
    scene c15s001_400 with dissolve
    "Decides jugar un rato a My Residence, El MC por fin lleva a Laura a una cita, aunque es ella la que elige restaurante."
    "Como ella es fan de las novelas de fantasía, elige un restaurante temático medieval en el que pueden disfrazarse. Laura cada vez te recuerda más a [dap]."
    scene black with dissolve
    return
label c15s002_DapLewd:
    if _in_replay:
        call mrS3_sca_route from _call_mrS3_sca_route_17
        if not sca._var("route"):
            call mrS3_emm_route from _call_mrS3_emm_route_28
        menu:
            "¿De qué te disfrazaste?"
            "Pícaro":
                $ Aux = 2
            "Cortesano":
                $ Aux = 1
            "Caballero":
                $ Aux = 0
    scene c15s002_001pv with dissolve
    show c15s002_001v
    pause (18.66)
    call BlinkXP ("c15s002_005" , "d") from _call_BlinkXP_1072
    dap "¡Es fantástica! ¡Está muy bien hecha! Quizás algún detalle aquí y allí está fuera de lugar, pero por el resto está muy bien."
    dap "Después de encontrar patatas, maíz, y pimiento en el menú, no me voy a quejar. Esperaba algo más... turístico."
    mc "A mí me parece muy lograda. Parece sacada de una película."
    call BlinkXP ("c15s002_010" , "d") from _call_BlinkXP_1073
    dap "A eso me refiero. Está muy bien para una película, pero no para una recreación histórica. Las camas eran mucho más cortas, dormían semisentados, especialmente los nobles."
    mc "[dap], es un hotel..."
    call BlinkXP ("c15s002_015" , "d") from _call_BlinkXP_1074
    dap "Técnicamente una posada."
    mc "Vale. Es una posada. No es la habitación de un castillo. Aquí la gente viene a pasárselo bien por una noche, no a hacer un análisis historiográfico de la habitación."
    mc "Los castillos no tenían jacuzzi. Y además han tenido el detalle de llenárnoslo cuando han encendido las velas."
    call BlinkXP ("c15s002_020" , "d") from _call_BlinkXP_1075
    dap "Son velas de gas. Se encienden con el interruptor. Sería prohibitivamente caro tener velas de verdad, y un peligro de incendio para el hotel."
    mc "Posada. *Risa*"
    call BlinkXP ("c15s002_025" , "d") from _call_BlinkXP_1076
    dap "Vale, un peligro para la posada. *Risa* ¿Vamos a los vestuarios a por nuestras cosas?"
    mc "No. Todavía no."
    call BlinkXP ("c15s002_030" , "d") from _call_BlinkXP_1077
    dap "¿Por qué? Recuerda que nos han dicho que cierran los vestuarios por la noche."
    mc "Lo sé, pero quiero besar a mi princesa antes de cambiarnos de ropa."
    if Aux == 0:
        scene c15s002_035aa with dissolve
    elif Aux == 1:
        scene c15s002_035ba with dissolve
    else:
        scene c15s002_035ca with dissolve
    dap "*Risita nerviosa* Si es por eso... "
    if Aux == 0:
        scene c15s002_035ab with dissolve
    elif Aux == 1:
        scene c15s002_035bb with dissolve
    else:
        scene c15s002_035cb with dissolve
    "Vuestros labios se juntan en un largo beso. Vuestras lenguas se buscan en un juego que ambos conocéis bien."
    "Pero hay algo que no funciona en ese beso. Algo que está fuera de lugar."
    call BlinkXP ("c15s002_040" , "d") from _call_BlinkXP_1078
    mc "[dap], ¿pasa algo?"
    dap "Lo has notado, ¿verdad?"
    mc "Sí, es la primera vez que no pones el alma en un beso. ¿Estás nerviosa?"
    call BlinkXP ("c15s002_045" , "d") from _call_BlinkXP_1079
    dap "Un poco... Estamos aquí... en la habitación de un hotel... posada... y sé que va a pasar. Sé que tiene que pasar.... pero parece demasiado real ahora mismo."
    mc "[dap], no hace falta que hagamos nada si no quieres. O que vayamos más allá de donde hemos ido hasta ahora. Si crees que no estás preparada..."
    call BlinkXP ("c15s002_050" , "d") from _call_BlinkXP_1080
    dap "¿Qué? ¡No! Sí que estoy preparada, pero sé que no voy a estar a la altura de lo que esperas... tú has estado con otras chicas antes y para mí va a ser la primera vez..."
    if sca._var("route"):
        dap "[eil], [sai], [sca]... y vete a saber cuántas más..."
    else:
        dap "[eil], [sai]... y vete a saber cuántas más..."
    mc "¿Eso es importante para ti? ¿Que yo tenga más experiencia que tú?"
    call BlinkXP ("c15s002_055" , "d") from _call_BlinkXP_1081
    dap "Un poco... Sé que es bueno, que no hay nadie en el mundo con el que quiera aprender más que contigo, pero sabes que odio no hacer las cosas bien..."
    mc "Te acuerdas de la primera lección de besos, ¿verdad?"
    dap "Sí..."
    mc "El primer beso, el que me diste tú, ¿cómo fue?"
    dap "Patético... es a lo que me refiero..."
    mc "Y el segundo beso, un minuto después, ¿cómo fue?"
    dap "Alucinante... pero me gustaría que nuestra primera vez fuera igual de alucinante que nuestro segundo beso."
    scene c15s002_060An with dissolve
    mc "[dap], mírame."
    call BlinkXP ("c15s002_060" , "d") from _call_BlinkXP_1082
    mc "Lo va a ser. Voy a ir con todo el cuidado posible. Y estoy con la chica más lista del mundo, con lo que vas a aprender muy rápido."
    dap "¿Estás seguro?"
    mc "Lo estoy."
    call BlinkXP ("c15s002_065" , "d") from _call_BlinkXP_1083
    dap "¡Entonces vamos a por nuestras cosas!"
    mc "No, todavía no. Quiero un beso de verdad y antes de irnos."
    if Aux == 0:
        scene c15s002_035aa with dissolve
        dap "Ven aquí, mi caballero. Ojalá fuera tan valiente como tú."
    elif Aux == 1:
        scene c15s002_035ba with dissolve
        dap "Ven aquí, mi príncipe. El rey de mis sueños."
    else:
        scene c15s002_035ca with dissolve
        dap "Ven aquí, mi pícaro. El que ha robado mi corazón."
    if Aux == 0:
        scene c15s002_035ab with dissolve
    elif Aux == 1:
        scene c15s002_035bb with dissolve
    else:
        scene c15s002_035cb with dissolve
    "Vuestros labios se vuelven a juntar otra vez. Esta vez con menos dudas, con más pasión. Con más alma."
    call BlinkXP ("c15s002_070" , "d") from _call_BlinkXP_1084
    mc "Ahora sí. Ahora podemos ir a por nuestras cosas."
    dap "Te libras por eso. En mitad del beso he tenido unas ganas enormes de tirarte en la cama y empezar a desnudarte..."
    mc "*Risa* Habrá tiempo para eso, no te preocupes."
    call BlinkXP ("c15s002_075" , "d") from _call_BlinkXP_1085
    dap "Vamos. Espérame en el jacuzzi cuando vengas. Yo voy a tardar un poco más que tú."
    mc "¿Alguna sorpresa más para mí?"
    dap "No, no es ninguna sorpresa. Tan solo algo que quiero hacer. Tendrás que verlo cuando vuelva."
    mc "Entonces vamos."
    call BlinkXP ("c15s002_075b" , "d") from _call_BlinkXP_1086
    dap "Déjame las llaves del coche. Tengo que coger una cosa que me he dejado."
    mc "¿El qué?"
    dap "Esta vez sí. Sorpresa..."
    mc "De momento me están encantando todas las sorpresas de la noche. Ahora te las doy en el vestuario."
    scene black with dissolve
    "Vas a buscar tus cosas al vestuario y vuelves a la habitación. La idea de [dap] de empezar en el jacuzzi parece prometedora."
    scene c15s002_080a with dissolve
    mcp "(Esto es fantástico... Hay que usar más el jacuzzi de casa de [nor].)"
    "Pasa un rato antes de que [dap] vuelva de los vestuarios."
    call BlinkXP ("c15s002_085" , "d") from _call_BlinkXP_1087
    dap "Hola, cielo, ya estoy aquí. ¿Qué tal el jacuzzi? Pareces salido de \"The Warlock\" ahora mismo."
    mc "¡El jacuzzi está genial! ¿Qué le ha pasado a tu pelo? ¿Qué le ha pasado a tu peinado medieval?"
    call BlinkXP ("c15s002_090" , "d") from _call_BlinkXP_1088
    dap "¿No te gusta mi trenza?"
    mc "Me encanta, eres más tú."
    call BlinkXP ("c15s002_095" , "d") from _call_BlinkXP_1089
    dap "Esa es una de las razones por las que me lo he cambiado... quiero recordar mi primera vez siendo yo misma, no una [dap] disfrazada."
    mc "Me parece una razón increíblemente buena. De todas formas, me gustas más así. Así eres tú."
    mc "¿Y las otras razones?"
    call BlinkXP ("c15s002_100" , "d") from _call_BlinkXP_1090
    dap "No quería sacarte un ojo con los anillos de la trenza. *Risa*"
    mc "Esa es una razón aún mejor. *Risa*"
    mc "¿Vienes?"
    call BlinkXP ("c15s002_105" , "d") from _call_BlinkXP_1091
    dap "Dame un segundo que me quite el vestido y voy... ahora es cuando viene la sorpresa..."
    mc "¿Necesitas ayuda para quitártelo?"
    dap "No, tranquilo. Además, si vinieras... no ibas a volver al jacuzzi una vez me desnudara."
    stop music fadeout (1.5)
    mc "Entonces te espero aquí."
    scene c15s002_080b with dissolve
    play music ("music/SensualJazzMedium2.ogg")
    mc "¿Te vas a dejar puesta la joyería?"
    dap "Pensaba quitármela. No sé si le va a ir bien mojarse en el jacuzzi."
    mc "Yo creo que no le va a pasar nada. Seguramente sea bisutería de todas formas. No te van a dejar piedras preciosas para un disfraz."
    dap "Entonces sí que me la dejaré, si te gustan."
    mc "Se está muy solo aquí. ¿Te falta mucho o tengo que ir a buscarte? *Risa*"
    dap "Ya estoy acabando, pero no me voy a meter en el jacuzzi... aún. Quiero que veas algo antes... a ver si te gusta..."
    mc "Seguro que me va a encantar."
    dap "Ya puedes mirar."
    if itchio:
        scene itchio with dissolve
        "Cuando [dap] se acaba de cambiar, pasáis una agradable noche jugando al ajedrez."
        "Os acostáis a dormir y, a la mañana siguiente, os despertáis muy temprano."
        call c15s002_ReturnHome from _call_c15s002_ReturnHome
        return
    scene c15s002_110d with dissolve:
        yalign 1.0
        linear 5.0 yalign 0.0
    pause (5.0)
    call BlinkXP ("c15s002_110" , "d") from _call_BlinkXP_1092
    mc "¡Wow, [dap]! ¡Estás preciosa!"
    if not _in_replay:
        $ renpy.notify ("Profile Image unlocked for Daphne: 8 - Lingerie")
        $ dap.profileImages.pop (7) # first remove
        $ dap.profileImages.insert (7, ("daphne_7", "route")) # then add new
    dap "¿Te gusta?"
    mc "¿Gustarme? ¡Me encanta! Espera que a que salga de aquí."
    call BlinkXP ("c15s002_115" , "d") from _call_BlinkXP_1093
    dap "Mejor entro yo. Eso tiene pinta de ser muy cómodo."
    mc "Pero no vas a entrar con eso puesto, ¿verdad?"
    dap "No, tonto. Me lo voy a quitar. Has dicho que querías que entrara con la joyería... solo con la joyería..."
    mc "¡Striptease! *Risa*"
    scene c15s002_120a with dissolve
    dap "¡No seas pervertido, [mc]! Soy [dap], tu inocente primita. Tan solo pensaba quitarme esto y entrar..."
    scene c15s002_120b with dissolve
    dap "Tan solo tu primita desnudándose..."
    scene c15s002_120c with dissolve
    dap "Nada sexy..."
    scene c15s002_120d with dissolve
    dap "Tan inocentemente como sea capaz..."
    scene c15s002_120e with dissolve
    dap "Hasta quedarse desnuda..."
    scene c15s002_120f with dissolve
    dap "Para poderse meter en el jacuzzi contigo..."
    scene c15s002_120g with dissolve
    dap "Y, obviamente, descalza..."
    call BlinkXP ("c15s002_125" , "d") from _call_BlinkXP_1094
    dap "¿Me haces un hueco?"
    mc "¡Wow! Espera un momento... tengo que recoger mi mandíbula del agua."
    call BlinkXP ("c15s002_130" , "d") from _call_BlinkXP_1095
    dap "*Risa* Deja de hacer el payaso y déjame entrar antes de que me vuelva a vestir."
    mc "¿Vestirte? Ni se te ocurra pensar que te dejaría volver a vestirte. *Risa*"
    stop music fadeout (1.5)
    dap "Es lo que esperaba oír."
    call BlinkXP ("c15s002_135" , "d") from _call_BlinkXP_1096
    play music ("music/SexyLoungeMusic.ogg")
    dap "Se está bien aquí."
    mc "Se está bien en cualquier sitio donde te pueda tener entre mis brazos."
    call BlinkXP ("c15s002_140" , "d") from _call_BlinkXP_1097
    dap "¿Cómo funciona esto?"
    mc "¿A qué te refieres?"
    call BlinkXP ("c15s002_140" , "h") from _call_BlinkXP_1098
    dap "A cuándo empezamos a follar. No sé cómo hacer la transición de una conversación normal a que me desvirgues."
    mc "*Risa* ¡[dap]! Me hubiera imaginado esa pregunta de cualquier otra menos de ti. *Risa* Al menos formulada así."
    call BlinkXP ("c15s002_145" , "d") from _call_BlinkXP_1099
    dap "¡No te rías! Una vez perdida la excusa de las lecciones... no sé... se me hace violento... es mi primera vez..."
    mc "No te preocupes, por norma son cosas que no se hablan. Suceden."
    call KissXP ("c15s002_150" , "d") from _call_KissXP_31
    mc "Se puede empezar con unos besos..."
    dap "Eso es terreno conocido, y me gusta..."
    scene c15s002_155a with dissolve
    mc "Después se puede seguir por besos en otros sitios..."
    dap "*Gemido* Aún me acuerdo de la primera lección cuando dijiste que si confiaba en ti y que me ibas a besar en otros sitios aparte de los labios..."
    call BlinkXP ("c15s002_160" , "d") from _call_BlinkXP_1100
    mc "Y míranos ahora, desnudos en un jacuzzi..."
    dap "Parece ser que confiar en ti salió bien. *Risita*"
    dap "Pero hay algo que quiero hacer..."
    mc "Puedes hacer lo que quieras, mi amor."
    scene c15s002_165a with dissolve
    dap "Bueno, parece que hay un submarino sacando el periscopio aquí que puede impedirlo..."
    scene c15s002_165An with dissolve
    dap "Arreglado..."
    mc "*Risa* Por un momento he pensado que..."
    call BlinkXP ("c15s002_170" , "d") from _call_BlinkXP_1101
    dap "Todavía no, primero quiero hacer esto..."
    scene c15s002_175pv with dissolve
    show c15s002_175v with dissolve
    mc "*BRL* ... *BRL* ... *BRL*..."
    dap "¡Hey! *Risa* ¡Esto es muy divertido! Haces unos sonidos muy graciosos."
    mc "*BRL afirmativo*"
    scene c15s002_180pv with dissolve
    show c15s002_180v with dissolve
    dap "*Risa* ¿Te gusta?"
    mc "*BRL* Sí, tienes *BRL* unas tetas *BRL* fantásticas..."
    call BlinkXP ("c15s002_185" , "d") from _call_BlinkXP_1102
    hide c15s002_180v
    hide c15s002_175v
    dap "Ha sido muy divertido. Vi a una chica haciéndoselo a su novio y a él parecía gustarle."
    mc "A mí me ha gustado, puedes estar segura de ello."
    call BlinkXP ("c15s002_190" , "d") from _call_BlinkXP_1103
    dap "Y ahora ha llegado el momento, ¿verdad? Puedo notar como presionas contra mi almeja..."
    mc "¿Cómo quieres que esté? Tengo a una mujer preciosa sentada encima de mi amigo mientras me abofetea la cara con sus tetas. *Risa*"
    mc "Deliciosas bofetadas, por cierto..."
    call BlinkXP ("c15s002_195" , "d") from _call_BlinkXP_1104
    if sca._var("route"):
        dap "[sca] me dijo que me olvidase de la teoría de la tirita, que no es cierta..."
    elif emm._var("route"):
        dap "[emm] estuvo comentando que había leído que la teoría de la tirita no es cierta..."
    else:
        dap "He leído que la teoría de la tirita no es cierta..."
    mc "No sé de dónde habéis sacado esa teoría, pero ciertamente no es como funciona."
    dap "¿Cómo lo tengo que hacer entonces?"
    mc "¿Quieres tener tú el control? ¿Estar arriba?"
    call BlinkXP ("c15s002_200" , "d") from _call_BlinkXP_1105
    dap "He leído que, de esta forma, al tener la mujer más control de la penetración, puede evitar que duela tanto... pero también he leído la teoría de la tirita... ya no sé qué creer."
    mc "A mí me parece bien que vayas haciéndolo a tu ritmo. Puedes parar si te duele... mucho."
    dap "Entonces, vamos allá..."
    scene c15s002_205a with dissolve
    "[dap] coge tu enhiesta polla y la apoya firmemente entre sus labios. Puedes notar el calor que emana de su entrepierna."
    call BlinkXP ("c15s002_210" , "d") from _call_BlinkXP_1106
    dap "¿Estás seguro de que va a entrar? Ya sé cómo funciona la dilatación, pero... se nota enorme..."
    mc "No te preocupes, si sabes cómo funciona la dilatación, ya sabes que acabará entrando."
    scene c15s002_205Anb with dissolve
    "Tu capullo desaparece en el interior de su coño en un movimiento lento. Su vagina se siente muy estrecha."
    call BlinkXP ("c15s002_215" , "d") from _call_BlinkXP_1107
    dap "¿Ya está? ¿Ya no soy virgen? Esperaba que fuera más... doloroso."
    mc "La punta está dentro, pero no he notado ninguna resistencia..."
    call BlinkXP ("c15s002_220" , "d") from _call_BlinkXP_1108
    dap "{b}¿Qué? ¿Sólo la punta?{/b} La sensación es de tener un mástil dentro..."
    mc "¿Duele?"
    call BlinkXP ("c15s002_225" , "d") from _call_BlinkXP_1109
    dap "No, no duele. Es incómodo, pero no hay dolor. Voy a bajar un poco más."
    mc "Adelante, hazlo a tu ritmo."
    scene c15s002_205Anc with dissolve
    "[dap] baja poco a poco, empalándose en tu astil hasta que notas la conocida resistencia del himen."
    mc "[dap], para."
    call BlinkXP ("c15s002_230" , "d") from _call_BlinkXP_1110
    dap "Lo estoy notando. Ahora es cuando va a doler de verdad, ¿cierto?"
    mc "Depende de la chica, pero es uno de los momentos más delicados."
    dap "Bueno... allá vamos..."
    scene c15s002_205And with dissolve
    "Ella vuelve a reanudar su descenso a lo largo de tu polla. Puedes notar como el himen se va estirando alrededor de tu capullo, hasta que la tensión desaparece con un *pop*."
    dap "¡Aaaargh!"
    call BlinkXP ("c15s002_235" , "d") from _call_BlinkXP_1111
    mc "¿Ha dolido mucho?"
    dap "Ha dolido. Pero no tanto como esperaba. Pero notar como se iba estirando ha sido casi peor hasta que se ha roto... es como quitarte una tirita poco a poco..."
    if emm._var("route") or sca._var("route"):
        mc "Hazme caso, la alternativa es peor."
        if sca._var("route"):
            dap "Lo sé. [sca] ya me lo contó..."
    mc "Ya ha pasado lo peor."
    dap "¿Puedes esperar un momento a que me acostumbre a tenerte entero dentro de mí?"
    mc "Puedo esperar a que te acostumbres ahora, si quieres, y después cuando esté entero dentro de ti."
    call BlinkXP ("c15s002_240" , "d") from _call_BlinkXP_1112
    dap "Bueno... eso... ¿Queda mucho fuera?"
    mc "Algo más de la mitad..."
    dap "Entonces..."
    scene c15s002_245An with dissolve
    "[dap] baja su cabeza hasta que sus labios rozan los tuyos."
    "Las lecciones de besos han valido la pena y [dap] es una experta besadora."
    scene c15s002_205Ane with dissolve
    "Las piernas de tu novia empiezan a temblar, como siempre que os besáis, y su cuerpo se va deslizando por tu polla, abrazándola con sus paredes vaginales."
    scene c15s002_245An2 with dissolve
    "Parece que los besos han hecho que se relaje, y que la incomodidad de notarte dentro por primera vez haya desaparecido."
    call BlinkXP ("c15s002_250" , "d") from _call_BlinkXP_1113
    dap "¿Seguimos? Me parece que he bajado un poco mientras te besaba."
    mc "Un poco no, [dap], ahora estoy dentro de ti por completo."
    call BlinkXP ("c15s002_255" , "h") from _call_BlinkXP_1114
    dap "¿Qué? ¿Ya está hecho? No me ha molestado en absoluto... bueno... aún tengo un poco de dolor de antes, pero es muy soportable..."
    mc "Si necesitas un ratito más..."
    call BlinkXP ("c15s002_260" , "d") from _call_BlinkXP_1115
    dap "¿Para qué? ¿Voy a sentirme menos rellena?"
    mc "No... *Risa*"
    dap "Entonces voy a empezar a moverme si no te importa..."
    mc "Adelante, marca tú el ritmo..."
    scene c15s002_265pv with dissolve
    show c15s002_265v with dissolve
    "[dap] comienza una salvaje cabalgata encima de tu polla."
    "En vez del habitual recorrido arriba y abajo, decide realizar un movimiento hacia adelante y atrás."
    dap "*Gemido* Esto es increíble..."
    dap "*Jadeo* ¿Te gusta así?... Las piernas no me sostienen para hacer otra cosa ahora mismo..."
    mc "Es fantástico, [dap]."
    scene c15s002_275pv with dissolve
    show c15s002_275v with dissolve
    "La sensación de estar dentro del agua mientras [dap] te cabalga con furia es totalmente diferente."
    "La ligereza que proporciona el agua hace que los movimientos fluyan de una forma inesperada."
    dap "*Jadeo* Si sigo así... me voy a correr enseguida. *Gemido* Y no quiero que acabe tan pronto..."
    mc "Correrte no significa que acabe, [dap]. esto puede durar tanto como quieras."
    dap "*Gemido* Pues quiero que dure para siempre."
    scene c15s002_270pv with dissolve
    show c15s002_270v with dissolve
    "Los movimientos de [dap] se hacen cada vez más espasmódicos mientras notas como sus piernas presionan contra las tuyas cada vez con más fuerza."
    "Es un signo inequívoco de que su orgasmo está a punto de llegar."
    dap "Estoy a punto... *Gemido* quiero que nos corramos juntos, mi amor."
    mc "No te preocupes por mí. Córrete y disfruta"
    dap "*Jadeo* Pero yo quería..."
    call OrgasmX ("c15s002_280") from _call_OrgasmX_21
    "No puede acabar la frase antes de que el orgasmo le golpee como una bola de demolición. O como el martillo de Thor."
    dap "*GEMIDO* ¡Me corro! ¡No pares!"
    "¿Parar? Ella ha hecho todo el trabajo y te tiene aprisionado. No hay mucho que puedas hacer más allá de movimientos cortos."
    call BlinkXP ("c15s002_285" , "d") from _call_BlinkXP_1116
    hide c15s002_265v
    hide c15s002_270v
    hide c15s002_275v
    "Cuando sus orgasmos por fin finalizan, se derrumba encima de tu hombro, exhausta."
    dap "¡Ha sido increíble! Pero esperaba que se notara tu descarga cuando te corrieras..."
    mc "[dap], yo no me he corrido aún. *Risa*"
    call BlinkXP ("c15s002_290" , "d") from _call_BlinkXP_1117
    dap "¿Tan mal lo he hecho?"
    mc "No, [dap]. Lo has hecho genial, pero a mí aún me quedaba un poco."
    call BlinkXP ("c15s002_295" , "d") from _call_BlinkXP_1118
    dap "Pues eso hay que solucionarlo. No puede ser que solo me corra yo en nuestra primera vez."
    dap "Las piernas no me van a aguantar para seguir llevando yo el ritmo, pero... podemos probar otra cosa..."
    mc "¡Sorpréndeme!"
    scene c15s002_300pv with dissolve
    show c15s002_300v with dissolve
    dap "¿Qué te parece si seguimos aquí?"
    mc "¿Por detrás? ¿Estás segura?"
    dap "*Risa* Me has malinterpretado. Quiero poder volver a casa sentada en el asiento del coche, no de pie en la cama de la camioneta. *Risa*"
    mc "Ya me parecía muy bonito para ser verdad. *Risa*"
    dap "*Risa* Quizás algún día si no tengo que sentarme o caminar después. *Risa*"
    scene c15s002_305An
    hide c15s002_300v
    "Te colocas detrás de [dap] y penetras su estrecho coño en un solo movimiento."
    dap "¡Ufff! Así parece más grande todavía. Me gusta esta posición."
    mc "Tenemos miles de posiciones que probar para que decidas cual es la que más te gusta, mi amor."
    dap "Esta postura es una seria candidata..."
    scene c15s002_310pv with dissolve
    show c15s002_310v with dissolve
    "Empiezas a bombear en el coño de [dap]. La postura anterior te ha dejado cerca de tu límite, pero la pequeña conversación te ha ayudado a alejarte de él."
    "Pese a todo, tus caderas tienen urgencia por llevarte al orgasmo y martillean el culo de [dap] a cada embestida."
    dap "*Gemido* ¡Oh, sí! ¡Joder! Esto es totalmente diferente..."
    dap "*Jadeo* Menos mal que me puedo apoyar en el jacuzzi... *Gemido* si no acabaría con la cara en el suelo..."
    scene c15s002_315pv with dissolve
    show c15s002_315v with dissolve
    dap "*Gemido* Me encanta notar como saltan mis tetas en cada embestida... *Jadeo* Me encanta notar como golpeas mi cérvix cada vez que llegas al fondo."
    dap "¡Sigue follándome así! *Gemido* ¡Más profundo! ¡Más duro si puedes!"
    "En el calor del momento [dap] ha olvidado que no quería ser follada, sino que quería hacer el amor. Esta chica puede ser muy sorprendente."
    scene c15s002_320pv with dissolve
    show c15s002_320v with dissolve
    dap "*Gruñido* ¡Me estás destrozando por dentro! ¡Pero qué bien sienta! *Jadeo* ¡Voy a correrme otra vez!"
    dap "*Gemido* ¡No pares! ¡Aquí llega!"
    "Tus caderas han adquirido vida propia y, aunque quisieras parar, no podrías. Pero no quieres. Tú también estás demasiado cerca de tu orgasmo."
    mc "Córrete para mí, mi amor."
    call OrgasmX ("c15s002_325") from _call_OrgasmX_22
    "El orgasmo de [dap] llega como una explosión, mucho más potente que el clímax anterior."
    dap "*GEMIDO* ¡Joder! ¡SÍ! ¡Fóllame más duro! ¡Córrete dentro, por favor!"
    scene c15s002_310pv with dissolve
    show c15s002_310v with dissolve
    "[dap] apoya todo su peso en el borde del jacuzzi mientras sus paredes vaginales exprimen tu astil con cada nueva oleada de orgasmos."
    dap "*JADEO* ¡No puedo parar de correrme!"
    "Notas los espasmos de su vagina en toda la longitud de tu polla, en una rápida sucesión de pequeñas contracciones seguidas de otras enormes."
    dap "*Gemido* ¡Lléname entera con tu leche!"
    "Oleada tras oleada, el coño de [dap] te acerca más a tu propio clímax hasta que ya no puedes retrasarlo más."
    if persistent.walkthrough:
        $ wt1 = _("[dap] embarazada.")
        $ wt2 = _("Sin consecuencias.")
    else:
        $ wt1 = ""
        $ wt2 = ""
    menu:
        "Correrte dentro." (wt = wt2):
            pass
        "Correrte dentro. Ir a por el bebé." (wt = wt1) if persistent.pregnancy:
            play sound ("music/OldMusicBox5.ogg")
            $ dap._var("pregnant", True) #RIAM track this one, please
    $ resetWalkthrough ()
    call OrgasmX ("c15s002_330") from _call_OrgasmX_23
    hide c15s002_310v
    hide c15s002_315v
    hide c15s002_320v
    "Explotas en el interior de [dap] tal como te ha pedido. La descarga es enorme, después de todo el rato en el jacuzzi."
    mc "¡Mpffft!"
    dap "¡Puedo notar tu leche en mi interior! ¡Está muy caliente!"
    "Te tiemblan las piernas al mismo ritmo que lo hacen las de [dap], convirtiéndoos en dos montañas de gelatina sincronizadas."
    scene c15s002_335An
    "Al salir del interior de [dap], parte de tu semilla se escapa de su coño antes de que éste recupere su forma original."
    stop music fadeout (1.5)
    call BlinkXP ("c15s002_340" , "d") from _call_BlinkXP_1119
    dap "¿Siempre es tan intenso? No me extraña que el sexo sea lo que mueve el mundo..."
    play music ("music/CinematicFairyTaleStory.ogg")
    mc "Siempre había oído que era el dinero. *Risa* Pero sí, cuando el sexo es bueno es así de intenso."
    call BlinkXP ("c15s002_345" , "d") from _call_BlinkXP_1120
    dap "Hay una teoría que dice que la gente quiere dinero para tener más sexo. *Risa* Algo como selección económica en vez de selección natural."
    mc "*Risa* No lo había oído nunca, pero tiene cierta lógica."
    mc "¿Qué te ha parecido tu primera vez?"
    call BlinkXP ("c15s002_350" , "d") from _call_BlinkXP_1121
    dap "Mucho más bestial que mis expectativas más salvajes... ahora mismo mis piernas parecen gelatina..."
    dap "¿Nos secamos y vamos a descansar un ratito a la cama antes del segundo asalto?"
    mc "Si tu primera vez quieres un segundo asalto... es que te ha gustado. Vamos a secarnos."
    dap "¿Me ha gustado? No, en absoluto. ¿Me ha encantado? Tampoco, se queda corto... Tengo que buscar un superlativo de \"encantado\"."
    call BlinkXP ("c15s002_355" , "d") from _call_BlinkXP_1122
    dap "No te he preguntado qué te ha parecido a ti... ¿Qué tal lo he hecho para ser novata?"
    mc "[dap], olvídate de la experiencia o la diferencia de experiencia que tengamos. Me ha encantado. Yo tampoco sé el superlativo."
    scene c15s002_360An with dissolve
    dap "Bueno, la diferencia en número no se reducirá, pero en porcentaje sí. Hasta hoy, tú eras infinitamente más experto que yo. Si tu experiencia era 1,000 la mía era cero."
    dap "Ahora a lo mejor estamos 1,001 a 1. Después del segundo asalto, 1,002 a 2... Dentro de 998 veces solo me doblarás en experiencia. *Risa*"
    mc "Espero que no me pongas un calendario muy exigente para llegar a ese 2,000 a 1,000 lo antes posible. *Risa*"
    call BlinkXP ("c15s002_365" , "d") from _call_BlinkXP_1123
    dap "¿Quién sabe? *Risa* Pero ahora lo que quiero es que mi novio venga aquí y me abrace."
    mc "Hazme un hueco. Acabo de secarme y estoy ahí en un momento."
    call BlinkXP ("c15s002_370" , "f") from _call_BlinkXP_1124
    dap "¿Sabes que me gusta mucho estar así? Con mi cabeza apoyada en tu pecho, escuchando tu corazón latir..."
    mc "Creía que te gustaría más ser la cuchara pequeña."
    call BlinkXP ("c15s002_375" , "d") from _call_BlinkXP_1125
    dap "He visto muchos memes en internet sobre cómo os hace sentir ser la cuchara grande, y duermo con el pelo suelto casi siempre. Te levantarías con pelos rojos entre los dientes. *Risa*"
    dap "Por no hablar del brazo derecho dormido y la erección incómoda..."
    mc "*Risa* Sí, veo que has visto los memes. No es tan malo como lo pintan. Lo de comer pelo sí, lo del brazo un poco, lo de la erección no es tan incómodo."
    call BlinkXP ("c15s002_380" , "d") from _call_BlinkXP_1126
    dap "Bueno, yo no te haré pasar por eso. Ya te digo que prefiero dormir así."
    scene c15s002_380An with dissolve
    dap "*Bostezo* Pero antes de dormir hay que hacer el segundo asalto."
    mc "Creo que te está entrando sueño. Podemos dejar el segundo asalto para cuando nos despertemos, si quieres."
    call BlinkXP ("c15s002_385" , "d") from _call_BlinkXP_1127
    dap "Sobre eso... he puesto el despertador a las 5:00."
    mc "¿Por qué tan pronto?"
    dap "No me gustaría llegar a casa cuando todo el mundo estuviera despierto. Si llegamos entonces... todo el mundo descubriría lo nuestro y ya te dije que prefiero hablarlo antes."
    dap "¿No te importa que no te deje dormir mucho?"
    mc "Ningún problema, [dap]. Si llegamos a casa antes de que se despierte todo el mundo, podremos dormir un rato más, aunque sea cada uno en su cama."
    scene c15s002_375c with dissolve
    "*Silencio*"
    mc "¿[dap]?"
    dap "*Ronquidito*"
    mcp "(Y hasta aquí hemos llegado con la posibilidad del segundo asalto. *Risa mental*)"
    mcp "(Se ha quedado dormida con la tiara y los pendientes. Se puede hacer daño durante la noche.)"
    scene c15s002_390An
    "Intentas quitarle la tiara y te llevas una palmada en el antebrazo."
    dap "*En sueños* ¡Suéltame, idiota! ¡Tengo novio y le soy fiel! Como venga te va a dar una paliza..."
    mcp "(Vale. *Risa mental* Tienes novio y mañana tendrás la tiara marcada en la frente. Pero mejor no despertarte.)"
    stop music fadeout (1.5)
    scene black with dissolve
    "Apagas las velas de gas con un interruptor ingeniosamente escondido en el armazón de la cama y te dispones a dormir. Al fin y al cabo, ha sido un día de playa y siempre te han parecido muy cansados."
    centered "{size=+20}{b}DÍA 17 – JUEVES{/b}{/size}"
    play music ("music/CinematicFairyTaleStory.ogg")
    "Te despiertas en medio de la noche con una sensación extraña. Todavía es de noche."
    scene c15s002_395a with dissolve
    mcp "(Parece ser que ser la cuchara pequeña no le desagrada, al fin y al cabo.)"
    scene c15s002_395b with dissolve
    "Te das cuenta de que tu erección matutina está aprisionada entre las piernas de [dap]. Esa es la sensación que te ha despertado."
    mcp "(*Risa mental* Y también parece que ha encontrado la forma de acomodar mi erección.)"
    dap "*Susurrando* ¿Estás despierto?"
    mc "Me acabo de despertar. ¿Llevas despierta mucho rato?"
    dap "Unos minutos. Estabas presionando contra mi culo..."
    mc "Lo siento... no es algo que pueda controlar, pero veo que has encontrado una solución. *Risa*"
    dap "Espera que encienda las luces. Está muy oscuro aún..."
    call BlinkXP ("c15s002_400" , "d") from _call_BlinkXP_1128
    dap "Una solución para mi culo, pero... no había contado con que, al dejar de presionar contra mi culo, estarías presionando contra mi entrepierna."
    mc "El martillo del amor tiene la mala costumbre de presionar donde le da la gana. *Risa*"
    call BlinkXP ("c15s002_405" , "d") from _call_BlinkXP_1129
    dap "*Risa* ¡El martillo del amor! ¡Me gusta! Si fueras rubio podría ser el Martillo de Thor. Chris Hemsworthy fue uno de mis primeros crush."
    mc "*Risa* Pues que sea el Martillo de Thor."
    scene c15s002_395c with dissolve
    dap "*Risa* ¡Con mis fluidos vaginales te bautizo como Mjolnir!"
    mc "¿Fluidos vaginales? ¿Te has despertado cachonda?"
    call BlinkXP ("c15s002_410" , "d") from _call_BlinkXP_1130
    dap "Un poco. Despertarme notando a Mjolnir en el culo me ha puesto un poco cachonda. Cuando lo he acomodado entre las piernas..."
    dap "Has empezado a moverte un poco... rozándome... presionando... he estado tentada de despertarte para ese segundo asalto que no pudimos hacer anoche."
    mc "Pues ya estoy despierto... y si mi novia se ha despertado cachonda, una de mis funciones es..."
    stop music fadeout (1.5)
    call BlinkXP ("c15s002_415" , "d") from _call_BlinkXP_1131
    dap "¿Hacerle el amor?"
    play music ("music/SexyLoungeMusic.ogg")
    mc "No, ponerla más cachonda antes de hacerle el amor. *Risa*"
    scene c15s002_420pv with fade
    show c15s002_420v
    "Os sentáis en la cama mientras empieza la sesión de besos matutina."
    "Esta vez las dudas que [dap] mostró después de la cena no hacen su aparición. Su primera vez le ha dado una confianza que no estaba ahí ayer."
    "No sabes como lo hace, pero incluso los besos matutinos saben dulces en su boca. No hay rastro de mal aliento."
    scene c15s002_425pv with fade
    hide c15s002_420v
    show c15s002_425v
    "Vuestras bocas siguen recorriéndose, vuestras lenguas buscándose y encontrándose, y poco a poco acabáis tumbados en la cama de nuevo."
    "La conversación es difícil, ya que a vuestros labios no les gusta separarse, pero, entre gemidos y besos, [dap] consigue decir algunas palabras."
    dap "*Gemido* Si no usas a Mjolnir, me voy a correr solo con estos besos. Si querías ponerme más cachonda aún, lo has conseguido."
    mc "¿Quieres que pare de besarte?"
    dap "*Jadeo* Quiero que me hagas el amor. ¡Ya!"
    scene c15s002_430pv with fade
    "Te sitúas entre sus piernas, con Mjolnir firmemente plantado en la entrada de su vagina y, con un movimiento de caderas, introduces la punta."
    hide c15s002_425v
    show c15s002_430v
    "Tus caderas empiezan a marcar un ritmo al que [dap] se adapta perfectamente."
    dap "*Gemido* ¿Alguna vez me acostumbraré a esto? *Jadeo* ... Espero que no... Me encanta sentirme llena de ti."
    "Pese a la pérdida de virginidad de anoche, no parece que [dap] sienta ninguna molestia."
    scene c15s002_435pv with dissolve
    hide c15s002_430v
    show c15s002_435v
    dap "*Jadeo* ¡Quiero que se llame Maeve! *Gemido* Nuestra primera hija..."
    "La revelación casi te desconcierta por un momento."
    dap "¡Embarázame! *Gemido* ¡Pon a una pequeña Maeve en mi útero!"
    "Mal momento para pensar en correrte en cualquier sitio que no sea en su interior. No puedes negarle nada mientras te mira con esos hermosos ojos."
    scene c15s002_440pv with dissolve
    hide c15s002_435v
    show c15s002_440v
    dap "Estoy notando *Gemido* como llega... *Jadeo* No pares, por favor..."
    "El cuerpo de [dap] se tensa visiblemente bajo tus manos, a cada movimiento de tus caderas."
    "La presión dentro de ella es cada vez mayor cada vez que se tensa, haciendo que cada vez lo sientas más estrecho."
    mc "No tengo intención de parar, cielo..."
    call OrgasmX ("c15s002_445") from _call_OrgasmX_24
    dap "*GEMIDO* ¡sí! ¡JODER! *JADEO* ¡Este es mejor que el de ayer!"
    "Los músculos de [dap] se tensan hasta que parecen a punto de romperse, entre gemidos y jadeos."
    "Su coño aprieta alrededor de tu polla en una sucesión de oleadas, intentando ordeñar una corrida que todavía no ha llegado. Intentando sacar cada gota de semen de tu pene."
    scene c15s002_430pv with dissolve
    hide c15s002_440v
    show c15s002_430v
    "Continúas embistiendo el coño de [dap] mientras a ella le llegan multitud de orgasmos que hacen que sus movimientos sean cada vez más espasmódicos."
    dap "*JADEO* ¡Por el amor de Dios! ¡No puedo parar de correrme!"
    "Mientras tanto, puedes notar como el espacio entre sus piernas cada vez se estrecha más, haciéndote más difícil controlar tu clímax."
    "Es una batalla perdida y acabas explotando dentro de ella."
    if persistent.walkthrough:
        $ wt1 = _("[dap] embarazada.")
        $ wt2 = _("Sin consecuencias.")
    else:
        $ wt1 = ""
        $ wt2 = ""
    menu:
        "Correrte dentro." (wt = wt2):
            pass
        "Correrte dentro. Ir a por el bebé." (wt = wt1) if persistent.pregnancy and not dap._var("pregnant"):
            play sound ("music/OldMusicBox5.ogg")
            $ dap._var("pregnant", True)
    $ resetWalkthrough ()
    call OrgasmX ("c15s002_450") from _call_OrgasmX_25
    mc "¡Mpfft!"
    "Descargas toda tu semilla en el interior de [dap]. Tienes la sensación de que no va a caber tanto semen dentro de ella."
    "[dap] no ha parado de correrse en los últimos minutos."
    dap "¡SÍ! *Gemido* ¡Lléname!"
    scene c15s002_425pv with dissolve
    "Cuando finalmente termina la descarga de semen, doblas tu cuerpo para besar a [dap]. Ha sido totalmente diferente de lo de ayer en el jacuzzi, pero no por ello menos impresionante."
    stop music fadeout (1.5)
    call BlinkXP ("c15s002_455" , "d") from _call_BlinkXP_1132
    dap "¡Ha sido increíble! Esperaba que la incomodidad que sentía por lo de anoche no me dejase disfrutar tanto..."
    play music ("music/CinematicFairyTaleStory.ogg")
    dap "Pero he tenido ocho orgasmos más que ayer..."
    mc "¿Los cuentas?"
    call BlinkXP ("c15s002_460" , "d") from _call_BlinkXP_1133
    dap "¡Claro! ¿Cómo, si no, voy a saber cuántos he tenido? ¿Cómo saber qué día ha sido mejor?"
    mc "*Risa* No me lo había planteado nunca... al menos no de forma numérica... No piensas hacer una tabla, ¿verdad? Con fecha y numero de orgasmos, me refiero."
    call BlinkXP ("c15s002_465" , "d") from _call_BlinkXP_1134
    dap "Supongo que... ¿no? Si lo hiciera... y no digo que vaya a hacerlo... sería por la ciencia..."
    mc "*Risa* No me molestaría que lo hicieras si es por lo que dices. Solo me sorprendería. Puedes apuntar un \"1\" en mi columna para ayer y para hoy. *Risa*"
    call BlinkXP ("c15s002_470" , "d") from _call_BlinkXP_1135
    dap "En tu caso esperaba que pudieras dar una puntuación del 0 al 10... Ya sé que los hombres solo soléis tener un orgasmo... pobres seres desgraciados..."
    mc "*Risa* No pienso puntuar cada vez que hagamos el amor. Cada vez es distinta e incomparable..."
    scene c15s002_470d with dissolve
    "*Alarma*"
    call BlinkXP ("c15s002_475" , "d") from _call_BlinkXP_1136
    dap "Son las 5:00. Deberíamos pensar en irnos si no queremos que nos pillen al llegar a casa..."
    mc "Cuando quieras. Voy a darme una ducha."
    call BlinkXP ("c15s002_480" , "d") from _call_BlinkXP_1137
    dap "Te acompaño, pero no tengas ideas extrañas. Nos tenemos que ir."
    scene c15s002_480d with fade
    "Os dais una ducha rápida llena de abrazos y besos en el moderno baño que hay hábilmente disimulado tras una pared falsa, pero no hay tiempo para mucho más."
    "Como se podía esperar, las ideas extrañas hacen su aparición, pero quedan en poco más que un magreo."
    "Si por ti fuera, os pasaríais en la habitación todo el tiempo posible antes de volver a casa, pero comprendes perfectamente a [dap] y su necesidad de guardar el secreto por el momento."
    call c15s002_ReturnHome from _call_c15s002_ReturnHome_1
    return
label c15s002_ReturnHome:
    if _in_replay and not AuxReplay:
        call mrS3_sca_route from _call_mrS3_sca_route_18
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
            "¿Besaste a Lisa en el Verdad o Reto?"
            "Sí":
                $ lis._var("kissedBeach" , True)
            "No":
                $ lis._var("kissedBeach" , False)
        menu:
            "¿Cuántos Puntos de Relación tienes con Debbie?"
            "Mas de 0":
                $ deb._var("relationshipPoints", 5, intention = "set")
            "Menos de 0":
                $ deb._var("relationshipPoints", -5, intention = "set")
                menu:
                    "¿Debbie te rechazó el beso en el Verdad o Reto?"
                    "Sí":
                        $ deb._var("kissRejected" , True)
                    "No":
                        $ deb._var("kissRejected" , False)
    scene black with dissolve
    stop music fadeout (1.5)
    "Después de abonar la cuenta de la cena, que consigues pagar tú, abandonáis el hotel y volvéis a casa."
    call BlinkXP ("c15s002_485" , "d") from _call_BlinkXP_1138
    play music ("music/Separation.ogg")
    mc "Bueno, hasta aquí ha llegado nuestra primera cita... espero que la hayas disfrutado."
    dap "Ha sido alucinante. Gracias, mi amor."
    dap "Ahora hay que planificar la siguiente. En un Burger Prince."
    mc "Vamos, te acompaño a casa."
    dap "No hace falta. Vivo aquí al lado. *Risita*"
    scene c15s002_490d with dissolve
    "Vuestros labios se juntan en un beso de despedida. No es muy diferente de los besos que os dabais para saludaros hace tan solo unos días, pero está mucho más cargado de sentimientos."
    call BlinkXP ("c15s002_490" , "h") from _call_BlinkXP_1139
    deb "*Suspiro de sorpresa*"
    mc "Buenos días, Debbie."
    scene c15s002_495AnBlink with hpunch
    dap "*Suspiro de sorpresa* Buenos días, Debbie. *Susurrando* Y aquí se acabó el secreto."
    call BlinkXP ("c15s002_500" , "d") from _call_BlinkXP_1140
    deb "Buenos días... No os preocupéis... Vuestro secreto está a salvo conmigo, no os preocupéis... Hacéis una pareja muy bonita..."
    deb "Yo os dejo... me he levantado pronto para ir a correr... hasta luego. No he visto nada y vosotros no me habéis visto a mí."
    mc "Nos vemos luego, Debbie..."
    scene c15s002_505AnBlink with dissolve
    dap "Hasta luego, Debbie..."
    dap "No sé quién está más sorprendida, si ella o yo..."
    if deb.rps > 0:
        dap "Después de vuestro beso en la playa... quizás se había hecho ilusiones..."
    elif deb._var("kissRejected"):
        dap "Después de que intentaras besarla en la playa, quizás se había hecho ilusiones..."
    else:
        dap "Espero que no le haya molestado... vi cómo te miraba en la playa cuando le tocó besar a alguien, como si dudara..."
    call BlinkXP ("c15s002_510" , "d") from _call_BlinkXP_1141
    dap "Sería bueno que hablaras con ella..."
    if deb.rps > 0 or deb._var("kissRejected"):
        mc "Lo haré... "
        if not lis._var("kissedBeach") and not kat._var("kissedBeach") and not kim._var("kissedBeach"):
            if sca._var("route"):
                if not deb._var("kissRejected") or deb.rps > 0:
                    dap "Aparte de a [sca] y a mí es a la única a la que besaste. Ahora sabe que tú y yo estamos juntos y no le costará atar cabos sobre [sca]..."
                elif deb._var("kissRejected"):
                    dap "Aparte de a [sca] y a mí es a la única a la que intentaste besar. Ahora sabe que tú y yo estamos juntos y no le costará atar cabos sobre [sca]..."
            else:
                if not deb._var("kissRejected") or deb.rps > 0:
                    dap "Aparte de a [sca] y a mí es a la única a la que besaste. Ahora sabe que tú y yo estamos juntos y no le costará atar cabos sobre [sca]..."
                elif deb._var("kissRejected"):
                    dap "Aparte de a mí es a la única a la que intentaste besar. Ahora sabe que tú y yo estamos juntos..."
            dap "No me gustaría que se hiciera ilusiones si no quieres nada con ella... y si quieres algo con ella... me cae bien..."
        else:
            if lis._var("kissedBeach") and kat._var("kissedBeach") and kim._var("kissedBeach"):
                dap "Y también con Lisa, Kate y Kim."
            elif lis._var("kissedBeach") and kat._var("kissedBeach"):
                dap "Y también con Lisa, Kate."
            elif lis._var("kissedBeach") and kim._var("kissedBeach"):
                dap "Y también con Lisa, y Kim."
            elif kat._var("kissedBeach") and kim._var("kissedBeach"):
                dap "Y también con Kate y Kim."
            elif lis._var("kissedBeach"):
                dap "Y también con Lisa."
            elif kat._var("kissedBeach"):
                dap "Y también con Kate."
            elif kim._var("kissedBeach"):
                dap "Y también con Kim."
            dap "No me gustaría que se hicieran ilusiones si no quieres nada con ellas... y si quieres algo con ellas... me caen bien..."
    else:
        mc "Lo haré... pero me parece que lo malinterpretaste, no creo que le caiga muy bien..."
    mc "¿Sabes que eres increíble?"
    call BlinkXP ("c15s002_515" , "d") from _call_BlinkXP_1142
    dap "Sí, lo sé. *Risa* Pero ahora mismo no sé por qué lo dices. *Risita*"
    mc "Al final de nuestra cita en lo único que estás pensando es en que otra chica no salga herida."
    dap "Entre las chicas nos tenemos que ayudar... y sé el efecto que puedes provocar. Yo caí víctima de él."
    dap "Si se puede llamar víctima a la persona más feliz del mundo. *Risita*"
    call BlinkXP ("c15s002_520" , "d") from _call_BlinkXP_1143
    dap "Y ahora me voy a mi habitación a dormir un rato más antes de que a nadie más se le ocurra salir a correr. En un par de horas tenemos la sesión de yoga."
    dap "Deberías volver a apuntarte..."
    mc "Quizás otro día, yo también voy a dormir un poco más. Nos vemos luego."
    call KissXP ("c15s002_525" , "d") from _call_KissXP_32
    mc "Te quiero."
    dap "Yo también te quiero."
    stop music fadeout (1.5)
    scene black with dissolve
    "Caes en la cama y tus ojos se cierran casi antes de que toques el colchón. Cuando te despiertas te das cuenta de que has dormido hasta tarde. Casi no vale la pena bajar a desayunar."
    return
label c15s003_PickUpEileen:
    if _in_replay:
        call mrS3_emm_route from _call_mrS3_emm_route_29
        if emm._var("route"):
            call mrS3_oma_route from _call_mrS3_oma_route_12
        call mrS3_eri_route from _call_mrS3_eri_route_22
        call mrS3_eil_route from _call_mrS3_eil_route_15
    "Después de comer y de informar a [mar] y [nor] de la visita de Aaron, llevas a [eri] al trabajo."
    call BlinkXP ("c15s003_005" , "d") from _call_BlinkXP_1144
    play music ("music/motor.ogg")
    eri "¿Sabes que le pasó a [dap] ayer?"
    mc "¿A qué te refieres?"
    call BlinkXP ("c15s003_010" , "d") from _call_BlinkXP_1145
    eri "Cuando volvimos de la playa, [sca] nos dijo que estaba durmiendo. Ni siquiera se levantó para cenar."
    mc "A lo mejor la playa le cansó mucho más de lo que ella esperaba. Yo también me quedé dormido en cuanto llegué."
    mc "¿Cuántos años llevabais sin ir?"
    call BlinkXP ("c15s003_015" , "d") from _call_BlinkXP_1146
    eri "Todas preferimos la piscina, con lo que... es posible que hace dos veranos fuera la última vez que fuimos. Y tienes razón. Yo estaba agotada ayer, y estoy acostumbrada a estar de pie todo el día."
    mc "¿Ves? Nada de lo que preocuparse con [dap]."
    if emm._var("route"):
        if eri._var("route"):
            call BlinkXP ("c15s003_020" , "d") from _call_BlinkXP_1147
            eri "¿Tengo que esperar alguna sorpresa más hoy?"
            if oma._var("route") and eil._var("route"):
                eri "El otro día, Alexia y [eil]. Ayer [emm]. ¿Algo para hoy?"
            elif oma._var("route"):
                eri "El otro día, Alexia. Ayer [emm]. ¿Algo para hoy?"
            elif eil._var("route"):
                eri "El otro día, [eil]. Ayer [emm]. ¿Algo para hoy?"
            mc "Depende, ¿a qué hora sales hoy de trabajar?"
            call BlinkXP ("c15s003_025" , "d") from _call_BlinkXP_1148
            eri "A las 8 PM. ¿Qué tiene que ver eso?"
            mc "Entonces no tengo ninguna sorpresa planeada para hoy. *Risa*"
    else:
        call BlinkXP ("c15s003_025" , "d") from _call_BlinkXP_1149
        mc "¿A qué hora sales hoy?"
        eri "A las 8 PM. ¿Por qué?"
    mc "Es posible que pase a buscarte cuando salgas. A esa hora deberíamos estar volviendo de casa de [eil]. Hoy Solomon sale a cenar con amigos. O de copas. O algo."
    call BlinkXP ("c15s003_030" , "d") from _call_BlinkXP_1150
    eri "Id con cuidado."
    mc "Ayer hablé con Alexia y nos acompañará. Uniformada. Por lo que pueda ser. Pero Kiara dice que Solomon estará fuera hasta medianoche, con lo que, en principio, no hay peligro."
    call BlinkXP ("c15s003_035" , "d") from _call_BlinkXP_1151
    eri "Hablando de [eil] y Alexia. ¿Puedes llevar a [eil] de vuelta a casa? Acaba su turno ya y ella no te lo va a pedir..."
    mc "¿Por qué no me lo iba a pedir?"
    call BlinkXP ("c15s003_040" , "d") from _call_BlinkXP_1152
    eri "Porque no quiere molestar. Ayer estaba diciendo que éramos mucha gente en casa y que daban más trabajo del necesario."
    eri "Ella no está segura del todo de que volver a casa, aunque sea esperando una semana, vaya a funcionar."
    eri "Ayer por la noche estuvimos hablando en la piscina. Me dijo que, si tenían que volver a irse, le pediría una habitación a Alexia. O incluso irse antes."
    mc "Aprovecharé el viaje de vuelta a casa para quitarle esas tonterías de la cabeza."
    stop music fadeout (1.5)
    "Pasáis el resto del trayecto hablando del día anterior en la playa. No vale la pena seguir hablando del tema hasta no hablar con [eil]."
    call BlinkXP ("c15s003_045" , "f") from _call_BlinkXP_1153
    play music ("music/SadSummer.ogg")
    mc "Buenas tardes, [eil]. ¿Acabas ya tu turno?"
    eil "Hola, [eri] y [mc]. Sí, en dos minutos. Por fin. Ha sido un día de locos."
    mc "Genial, entonces te llevo a casa, si quieres."
    call BlinkXP ("c15s003_050" , "d") from _call_BlinkXP_1154
    eil "No hace falta que te molestes. No he tenido tiempo de comer nada y pensaba ir al Burger Prince a comer algo antes de volver. ¡Me muero de hambre!"
    mc "Pues si no te importa que te acompañe, al menos no comes sola. Yo ya he comido, pero sabes que los helados del Burger Prince siempre me han gustado."
    call BlinkXP ("c15s003_055" , "d") from _call_BlinkXP_1155
    eil "¡Perfecto!"
    if eil._var("route"):
        call KissXP ("c15s003_060" , "d") from _call_KissXP_33
        eil "Antes de ir a cambiarme quiero un beso."
    eil "¡Ahora vuelvo! ¡Me muero de hambre! *Risa*"
    call BlinkXP ("c15s003_060b" , "d") from _call_BlinkXP_1156
    eri "Bien jugado, [mc]. Mientras tiene la boca llena no puede discutir. *Risa*"
    mc "Tampoco es que quiera discutir. Quiero hacerle saber que ni ella ni Kiara molestan en casa."
    eri "¿Quieres tomar algo mientras la esperas?"
    mc "No gracias, tengo que mantener la línea. *Risa*"
    scene c15s003_065d with fade:
        yalign 1.0
        linear 5.0 yalign 0.0
    pause (5.0)
    call BlinkXP ("c15s003_065" , "d") from _call_BlinkXP_1157
    "Unos minutos después..."
    if not _in_replay:
        $ renpy.notify ("Profile Image unlocked for Eileen. 1 - Casual")
        $ eil.profileImages.pop (0) # first remove
        $ eil.profileImages.insert (0, ("eileen_0", "route")) # then add new
    eil "Ya estoy lista. ¿Nos vamos?"
    mc "Cuando quieras."
    if eri._var("route"):
        call KissXP ("c15s003_070" , "d") from _call_KissXP_34
        mc "Te quiero."
        eri "Yo también te quiero."
    else:
        scene c15s003_070a with dissolve
    mc "Te recogemos cuando volvamos de casa de [eil]. Hasta luego."
    eri "Hasta luego."
    if eri._var("route"):
        call BlinkXP ("c15s003_075" , "f") from _call_BlinkXP_1158
        eil "Se me hace extraño verte besar a [eri] delante mío."
        if eil._var("route"):
            mc "¿Te molesta? También te beso a ti delante de ella..."
            call BlinkXP ("c15s003_080" , "d") from _call_BlinkXP_1159
            eil "No, me refiero a todo lo contrario. Cuando nos lo contamos, creía que iba a haber rivalidad entre nosotras compitiendo por ti."
            eil "Pero ha sido justo lo contrario. Nos ha hecho más amigas todavía. Casi todos los días que nos coinciden turnos nos lo pasamos hablando de ti."
            mc "*Risa* No sé si sentirme halagado o preocuparme."
            call BlinkXP ("c15s003_085" , "d") from _call_BlinkXP_1160
            eil "Nada de lo que preocuparte. Pero no sabía que me sentiría así con ella. Veo el bien que nos haces a las dos y no puedo evitar quererte más todavía."
            mc "Si sigues así me voy a ruborizar. *Risa*"
        else:
            mc "¿Te molesta? No quisiera que te sintieras incómoda..."
            call BlinkXP ("c15s003_080" , "d") from _call_BlinkXP_1161
            eil "No, me refiero a que cuando descubrí lo vuestro, creía que me iba a importar más. Después acepté que mi momento había pasado y era el suyo."
            eil "Lo que se me hace raro es precisamente que no me moleste... Ahora hablamos de ti un montón."
            mc "*Risa* No sé si sentirme halagado o preocuparme."
            call BlinkXP ("c15s003_085" , "d") from _call_BlinkXP_1162
            eil "Nada de lo que preocuparte. Me pregunta sobre qué hacíamos cuando estábamos juntos y esas cosas."
            eil "Si puedo ayudar a que la relación entre mi ex-novio y una de mis mejores amigas prospere, no tenéis más que pedirlo. Aún te quiero, aunque sea solo como amigo."
            mc "Si sigues así me voy a ruborizar. *Risa*"
    call BlinkXP ("c15s003_090" , "f") from _call_BlinkXP_1163
    "Unos minutos después, ya en el Burger Prince..."
    eil "Si quieres puedes robarme UNA O DOS patatas. *Risa*"
    mc "*Risa* No te preocupes. He comido mucho en casa y con el helado tengo de sobras. Además, la que me robaba patatas siempre eras tú."
    eil "*Risa* Pero eso es porque estabas gordo y no quería que te engordaras más."
    return
label c15s003_LunchEileen:
    if _in_replay:
        call mrS3_eil_route from _call_mrS3_eil_route_16
        call mrS3_sam_route from _call_mrS3_sam_route_13
        call mrS3_sim_route from _call_mrS3_sim_route_15
        call mrS3_mar_route from _call_mrS3_mar_route_27
        call mrS3_nor_route from _call_mrS3_nor_route_19
    call BlinkXP ("c15s003_095" , "d") from _call_BlinkXP_1164
    mc "¿Tienes ganas de volver a casa a por vuestras cosas?"
    eil "Sobre todo, tengo ganas de coger mi bici. No me gusta coger el bus o depender de vosotros para que me traigáis al trabajo o me llevéis a casa."
    mc "Sabes que no es ninguna molestia, ¿verdad?"
    call BlinkXP ("c15s003_100" , "d") from _call_BlinkXP_1165
    eil "No, no lo sé. Sé que lo decís y que os ofrecéis a hacer de taxista para todas nosotras, pero sé que es una molestia."
    eil "Vosotros tenéis cosas que hacer, una empresa que administrar. No podéis estar dejando de hacer vuestras cosas para llevarnos arriba o abajo."
    mc "[eil.nick], el dormitorio lo llevan entre [mar] y [nor]. Yo apenas hago nada. Si puedo ayudar haciendo que os sintáis más cómodas y llevándoos a los sitios, no es algo que me moleste hacer."
    call BlinkXP ("c15s003_105" , "d") from _call_BlinkXP_1166
    eil "Pero es a eso a lo que me refiero. Que tengas que llevar a Kate o Lisa tiene cierta lógica. Son vuestras clientas, al fin y al cabo."
    eil "Mi madre y yo somos poco más que una imposición. Nos hemos colado en vuestras vidas cuando más ocupados estáis."
    mc "Y nosotros estamos contentos de que lo hayáis hecho."
    call BlinkXP ("c15s003_110" , "d") from _call_BlinkXP_1167
    eil "Al menos solo serán unos días antes de que os dejemos tranquilos."
    eil "O volvemos a casa o buscamos otra solución la semana que viene."
    mc "O os quedáis en casa."
    call BlinkXP ("c15s003_115" , "d") from _call_BlinkXP_1168
    eil "Mejor no, he hablado con Alexia y, ahora que su abuelo se ha ido, podríamos usar su habitación."
    mc "Y en su casa no seríais una imposición por alguna razón que desconozco, ¿verdad?"
    call BlinkXP ("c15s003_120" , "d") from _call_BlinkXP_1169
    eil "¡Claro que lo seríamos! Pero vive en la ciudad, seríamos más independientes para movernos."
    eil "Y ella no tiene que atender a una familia, invitadas y clientas. Además, nos dejaría ayudarle en casa, cosa que ni [mar] ni [nor] hacen."
    mc "Si es por eso, ya hablaré con ellas para que os dejen colaborar. Si os vais a sentir más a gusto..."
    call BlinkXP ("c15s003_125" , "d") from _call_BlinkXP_1170
    eil "No es solo eso, [mc]. Son muchas cosas. Ayer, en la comida... "
    mc "¿Qué pasó? ¿Alguien os hizo sentir mal?"
    eil "No, todo lo contrario... Hemos comido dos veces con tu familia... el día que llegamos y ayer..."
    mc "Con nuestra familia..."
    call BlinkXP ("c15s003_130" , "d") from _call_BlinkXP_1171
    eil "¿Ves? Es a lo que me refiero... "
    eil "Yo sé cómo funciona tu... la familia... pero mi madre no. Anoche estaba excitada con el día de playa... tenías que haberla oído hablar..."
    mc "Pero eso es bueno, ¿no?"
    call BlinkXP ("c15s003_135" , "d") from _call_BlinkXP_1172
    eil "No, no lo es. Después de descubrir cómo es una familia de verdad... vamos a tener que volver a casa... a nuestra familia... si es que se le puede llamar así."
    eil "En casa mi madre tiene a su marido y yo a mi padre, pero mi madre está descubriendo que eso no nos convierte en familia."
    eil "Y solo llevamos dos días en casa de [nor]. Cuando haya pasado la semana, volver a casa va a ser deprimente para mi madre, una vez se acostumbre a los Marks."
    mc "Y crees que, si os vais a casa de Alexia, la cosa va a ser diferente, ¿verdad?"
    call BlinkXP ("c15s003_140" , "d") from _call_BlinkXP_1173
    eil "En cierto modo, sí. Los Marks sois fantásticos, pero podéis ser un poco abrumadores. Y con toda la familia volcada en nosotras por el momento que estamos atravesando..."
    mc "[eil.nick], en la comida de ayer en el merendero, ¿quién estaba?"
    call BlinkXP ("c15s003_145" , "d") from _call_BlinkXP_1174
    eil "La familia..."
    mc "Exacto. La familia. Nuestra familia. No solo los Marks. También estabais vosotras, las Lamb. Y las Washington, [sam] y [sim]. Y las estudiantes. Y Alexia."
    mc "Y técnicamente mi Meemaw y Tía Betty no son Marks. *Risa*"
    mc "¿Estás diciendo que Alexia es menos familia que [sam]? ¿O que Debbie? ¿O que tú? Iros a casa de Alexia no os va a librar de la familia."
    call BlinkXP ("c15s003_150" , "d") from _call_BlinkXP_1175
    eil "Pero no es lo mismo... veros todos los días hace que nos demos cuenta de lo que no tenemos en nuestras vidas."
    mc "Podéis tenerlo si queréis, pero no si huis de nosotros."
    mc "[nor] ya os lo dijo. Podéis quedaros tanto tiempo como sea necesario."
    call BlinkXP ("c15s003_155" , "d") from _call_BlinkXP_1176
    eil "Ya... mi madre está encantada... "
    eil "Ya te digo que estaba muy excitada con la comida de ayer..."
    if sam._var("route") or sim._var("route"):
        if mar._var("route") or nor._var("route") or sam._var("route") or sim._var("route"):
            eil "Y con algo que pasó antes y que no me ha querido contar..."
            mc "Bueno, pasó algo que la sorprendió, pero no es el momento de hablar de ello."
    mc "Lo importante para mí es que estuvo totalmente integrada con el resto de la familia. Y, como tú dices, solo lleváis dos días en casa."
    call BlinkXP ("c15s003_160" , "d") from _call_BlinkXP_1177
    eil "Y, como también he dicho, cuando pase la semana y tengamos que volver a casa, puede ser deprimente para ella. Parece que solo escuchas lo que quieres escuchar. *Risa*"
    mc "Siempre buscando el lado bueno de la vida, ¿no? *Risa*"
    mc "Pero no hacemos más que hablar de Kiara. ¿Cómo estás tú en casa?"
    call BlinkXP ("c15s003_165" , "d") from _call_BlinkXP_1178
    eil "¿Cómo quieres que esté? Genial, tu familia... la familia... siempre me ha gustado. Vivirlo desde dentro es alucinante."
    if eil._var("route"):
        eil "Y saber que estamos juntos y que puede que un día también sea mi familia... mi familia de verdad... es increíble."
    else:
        eil "Aunque saber que ya no estamos juntos y que nunca va a ser mi familia... mi familia de verdad... es un poco raro, pero no deja de ser increíble."
    mc "Ya es tu familia de verdad. Pregúntale a cualquiera de las chicas y verás que te ven como a una hermana o prima más."
    call BlinkXP ("c15s003_170" , "d") from _call_BlinkXP_1179
    eil "Lo sé... especialmente [emm] y [eri]..."
    mc "Hablando de [emm]... tengo que pedirte un favor..."
    eil "Dime..."
    mc "¿Se te ocurre cómo puedo sacar de casa a [emm], [dap], Meemaw y Betty esta tarde? Necesitaría que estuvieran fuera de 5 a 6 de la tarde."
    call BlinkXP ("c15s003_175" , "d") from _call_BlinkXP_1180
    eil "¿Puedo saber por qué o es otro de tus secretos?"
    mc "Vamos a recibir unas visitas por un tema de negocios. Y nos han pedido que estemos solo mi madre, [nor], y yo."
    call BlinkXP ("c15s003_180" , "d") from _call_BlinkXP_1181
    eil "¿No sería más lógico pedirles que no entren dónde sea que vayáis a tener la reunión?"
    mc "Es más complicado que todo eso, [eil.nick]."
    call BlinkXP ("c15s003_185" , "d") from _call_BlinkXP_1182
    eil "No te preocupes. Ayer, hablando con Betty, me dijo que tenía que comprarse ropa. Olivia seguramente la querrá acompañar, y no será difícil convencer a [emm] y a [dap] para que vengan también."
    eil "Si me dejas el coche, les puedo llevar a un par de tiendas de ropa y después ir a tomar algo para daros tiempo de que acabéis la reunión."
    mc "Gracias, [eil.nick]."
    call BlinkXP ("c15s003_190" , "d") from _call_BlinkXP_1183
    eil "No hay de qué. Para eso está la familia. *Risa*"
    eil "¿Voy al lavabo y nos vamos? Tengo que convencerlas de ir a comprar ropa... *Risa* ¿Qué tipo de ropa usa una monja en su tiempo libre?"
    mc "No tengo ni idea, pero Betty parece vestir bastante normal. *Risa* Te espero aquí."
    scene c15s003_190An with dissolve
    "Te dispones a esperar a [eil] cuando oyes una conversación en una mesa a tu espalda."
    "No puedes evitar escucharla. No habla alto, pero el local está prácticamente vacío."
    "Hombre al teléfono" "... lo sé, hermanita, lo sé. Lo último que desearía sería hacerle daño..."
    "Hombre al teléfono" "No, no creo que sienta nada por mí ahora mismo, apenas nos conocemos. Yo nos definiría con amigos con posibilidades de llegar a algo más."
    "Hombre al teléfono" "Pero no consigo sentir nada por ella. Es una chica fantástica... deberías haberla visto el otro día..."
    "Hombre al teléfono" "Y sé que ahora me deberían gustar las chicas... pero no lo consigo..."
    "Hombre al teléfono" "Sí, también lo sé... ¿Soy raro, Olga?"
    "Hombre al teléfono" "¡Qué fácil es para ti decirlo! Para hacerlo más complicado todavía, hace unos días conocí a un chico..."
    "Hombre al teléfono" "No, no ha pasado nada... solo hemos hablado un par de veces... pero me atrae..."
    "La conversación se va alejando de ti, como si el hombre se estuviera marchando del Burger Prince."
    "Hombre al teléfono" "Ser alguien como yo en una ciudad como esta... es complicado... Si estuviera en San Francisco contigo... sería diferente..."
    "Empiezas a sentir curiosidad por saber quién está hablando. La voz te resulta familiar, pero no la ubicas."
    menu:
        "Te giras a mirar quién es":
            $ mc._var("knowsAnthony", True)
            scene c15s003_195An with dissolve
            "Te giras justo a tiempo de ver como sale del restaurante mientras habla."
            mcp "(¿Ese es Anthony? No le he podido ver la cara, pero la voz...)"
        "No es asunto tuyo":
            mcp "(No debería meterme en los asuntos de los demás. Suficiente tengo con todo lo que tengo entre manos.)"
    scene c15s003_200AnBlink with dissolve
    "Tras unos minutos más, [eil] vuelve del lavabo."
    eil "¿Nos vamos? Quiero enseñarte algo que encontré en el bosque antes de irnos a casa y tener que llevar a las chicas de compras."
    mc "¿Qué encontraste?"
    eil "Me tendrás que llevar allí para enseñártelo. Ya te indicaré dónde tienes que parar."
    mc "Entonces vamos."
    stop music fadeout (1.5)
    scene black with dissolve
    return
label c15s004_LewdEileen:
    if _in_replay:
        call mrS3_eil_route from _call_mrS3_eil_route_17
        if eil._var("route"):
            call mrS3_eil_pregnant from _call_mrS3_eil_pregnant_4
        call mrS3_emm_route from _call_mrS3_emm_route_30
        call mrS3_eri_route from _call_mrS3_eri_route_23
        call mrS3_dap_route from _call_mrS3_dap_route_22
        call mrS3_sca_route from _call_mrS3_sca_route_19
        call mrS3_sam_route from _call_mrS3_sam_route_14
    "Cuando estáis a unos minutos de casa, [eil] te indica que pares en el arcén de la carretera y que la sigas al interior del bosque."
    call BlinkXP ("c15s004_005" , "d") from _call_BlinkXP_1184
    play music ("music/MorningFunnyBeat.ogg")
    eil "Aquí está."
    mc "¿Un columpio?"
    call BlinkXP ("c15s004_010" , "d") from _call_BlinkXP_1185
    eil "Sí, es un columpio, no una nave espacial. *Risa* Lo vi hace unos días cuando salí a correr y me acordé de aquel que había detrás de tu casa."
    mc "Pero aquel tenía un neumático en vez de una tabla. Lo hizo el Tío Mike poco antes de morir. Tía [nor] cambió la cuerda varias veces mientras las chicas crecían."
    mc "Debería montar uno igual que aquel, creo que a las chicas les gustaría."
    mc "¿Sabes a quién pertenece este?"
    call BlinkXP ("c15s004_015" , "d") from _call_BlinkXP_1186
    eil "No tengo ni idea. Creo que esto es terreno municipal, con lo que no será de nadie. Lo habrán construido unos críos."
    mc "Seguro que sí."
    if eil._var("pregnant"):
        call BlinkXP ("c15s004_020" , "d") from _call_BlinkXP_1187
        eil "Hablando de críos... tengo unas ganas enormes de que llegue la semana que viene..."
        mc "¿Por qué? No lo entiendo..."
        call BlinkXP ("c15s004_025" , "d") from _call_BlinkXP_1188
        eil "El tiempo de espera para la prueba de embarazo..."
        mc "¿Todavía tienes molestias?"
        call BlinkXP ("c15s004_030" , "d") from _call_BlinkXP_1189
        eil "Sí, y cada vez van a más. No solo son los pezones sensibles... llevo una semana sin poderme poner un sujetador si no es deportivo...."
        eil "Esta mañana he vomitado... pero podría ser porque ayer comí demasiado también... Me estoy volviendo paranoica y a todo le veo un significado."
        mc "¿Pero tú te encuentras bien? ¿Puedes seguir trabajando? ¿Cuándo te dijeron que te podías hacer la prueba?"
        call BlinkXP ("c15s004_035" , "d") from _call_BlinkXP_1190
        eil "Sí, me encuentro bien exceptuando los pezones y los vómitos. La prueba la haré semana que viene. El martes, aunque para más exactitud me recomendaron el jueves."
        mc "Es decir, en un máximo de una semana... y no la harás. La haremos."
        call BlinkXP ("c15s004_040" , "d") from _call_BlinkXP_1191
        eil "Sí. Me muero de ganas por saberlo. Y porque salga positivo..."
        if oma._var("pregnant"):
            eil "Alexia está igual, pero sin vómitos... aún."
            $ Aux = True
        if emm._var("route") and eri._var("route"):
            call BlinkXP ("c15s004_045" , "d") from _call_BlinkXP_1192
            $ Aux = True
            eil "¿Con [emm] y [eri] ya has...? Olvídalo, no es asunto mío..."
        elif emm._var("route"):
            call BlinkXP ("c15s004_045" , "d") from _call_BlinkXP_1193
            $ Aux = True
            eil "¿Con [emm] ya has...? Olvídalo, no es asunto mío..."
        elif eri._var("route"):
            call BlinkXP ("c15s004_045" , "d") from _call_BlinkXP_1194
            $ Aux = True
            eil "¿Con [eri] ya has...? Olvídalo, no es asunto mío..."
        if Aux:
            call BlinkXP ("c15s004_045b" , "d") from _call_BlinkXP_1195
            eil "Lo digo porque a este paso, más que un columpio vas a tener que construir una guardería para nuestros niños. *Risa*"
            mc "No me asustes... no quedan habitaciones libres. *Risa*"
    call BlinkXP ("c15s004_050" , "d") from _call_BlinkXP_1196
    eil "Es resistente, al menos. *Risa* Aún me acuerdo cuando pasábamos horas en aquel neumático hablando de nuestros planes de futuro. *Risa*"
    mc "Sí, y haciendo otras cosas. Si aquella rueda pudiera hablar..."
    if not eil._var("route"):
        call BlinkXP ("c15s004_055" , "d") from _call_BlinkXP_1197
        eil "Sí, qué tiempos aquellos..."
        eil "Deberíamos irnos si tengo que convencer a Betty para ir de compras antes de vuestra reunión."
        mc "Vamos. Este columpio me ha traído un montón de recuerdos, pero se nos va a echar el tiempo encima."
        scene black with dissolve
        "Volvéis al coche en silencio, recordando aquellos tiempos en los que pensabais que estaríais juntos para siempre."
        return
    if eil._var("route") and itchio:
        scene itchio with dissolve
        "Jugáis un rato en el columpio recordando viejos tiempos."
        scene black with dissolve
        return
    call BlinkXP ("c15s004_060" , "h") from _call_BlinkXP_1198
    stop music fadeout (1.5)
    eil "¿Te apetecería recordar aquellas \"otras cosas\"?"
    play music ("music/NightJazzBeats.ogg")
    mc "¡[eil]! ¿Has estado sin bragas todo este tiempo?"
    mc "Lo sé, lo sé, es una pregunta estúpida. No has tenido tiempo de quitártelas ahora."
    call BlinkXP ("c15s004_065" , "d") from _call_BlinkXP_1199
    eil "Por un momento he creído que se te había fundido la última neurona. *Risa*"
    mc "Mi neurona sigue funcionando perfectamente."
    mc "Me está diciendo que, si sigues metiéndote conmigo, me vaya corriendo al coche y te deje aquí tirada. *Risa*"
    call BlinkXP ("c15s004_070" , "d") from _call_BlinkXP_1200
    eil "¿Ves como no funciona demasiado bien? Si funcionase, en vez de huir, te hubiera indicado que me tapases la boca para que dejase de hablar. *Risa*"
    mc "Supongo que no creerás que iba a contarte mis planes como un villano cutre de película de serie B, ¿no?"
    scene c15s004_195pv with dissolve
    show c15s004_195v with dissolve
    "Cada vez que os besáis el tiempo vuelve a vuestra adolescencia, cuando os podíais pasar horas besándoos sin prácticamente hablar."
    "El mismo sabor de pintalabios, moras, con un ligero toque al batido de fresa que ha bebido en la comida, hace que los besos de [eil] no sean dulces sólo en sentido figurado."
    "El beso va ganando en intensidad con el paso de los segundos y [eil] empieza a gemir en tu boca."
    call BlinkXP ("c15s004_075" , "d") from _call_BlinkXP_1201
    eil "*Gemido* Todavía sabes al helado de chocolate."
    mc "Y tú al batido de fresa..."
    eil "Si quieres quitarte el sabor..."
    mc "No te voy a dejar que me lo repitas dos veces..."
    call BlinkXP ("c15s004_085" , "d") from _call_BlinkXP_1202
    eil "Veo que tu neurona vuelve a funcionar correctamente. *Risa*"
    mc "Si hay un sabor mejor que el del helado de chocolate, es el tuyo."
    eil "*Risa* ¡Glotón!"
    scene c15s004_190pv with dissolve
    show c15s004_190v with dissolve
    hide c15s004_195v
    "Te agachas entre las piernas de [eil] y sumerges tu cara en su entrepierna."
    "El conocido olor terroso que emana te pone cachondo inmediatamente... más incluso de lo que lo ha hecho el largo beso."
    eil "*Gemido* Adoro esa lengua tuya... siempre has sabido tocar todos mis puntos correctos..."
    "No hay nada como sentirse en casa... no hay nada como estar donde perteneces."
    eil "*Jadeo* No sabía si te apetecería... pero llevo esperando esto desde que hemos salido del Burger..."
    call BlinkXP ("c15s004_090" , "d") from _call_BlinkXP_1203
    mc "Si alguna vez no me apetece esto, llévame al médico. Significará que la neurona se ha fundido definitivamente."
    eil "*Risa* ¡Calla y sigue, payaso! Me estaba acercando mucho..."
    mc "A tus órdenes, mi amor."
    scene c15s004_185pv with dissolve
    show c15s004_185v with dissolve
    hide c15s004_190v
    "Continúas lamiendo la húmeda raja de [eil] mientras sus jugos van impregnando tu lengua."
    eil "*Gemido* Sigue así, mi amor. Está siendo fantástico..."
    "Las piernas de [eil] hacen presión sobre tus orejas y puedes notar sus latidos en tu cráneo... ¿O son los tuyos?"
    eil "*Jadeo* ¡Cada vez eres mejor haciendo esto! *Gemido* ¡Y ya me parecías buenísimo antes!"
    scene c15s004_190pv with dissolve
    show c15s004_190v with dissolve
    hide c15s004_185v
    "No eres de las personas a las que le suba el ego ese tipo de afirmación, pero es agradable saber que tu lengua está complaciendo a [eil]."
    eil "¡Estoy a punto de llegar, [mc]! *Gemido* Quiero correrme contigo dentro..."
    mcp "(Lo harás, pero todavía no... O no como esperas...)"
    "Introduces toda tu lengua en el interior de su vagina, provocando un sonido de sorpresa en [eil]."
    eil "*Respiración entrecortada* No... me... refería... a... eso..."
    "La sorpresa junto a la presión simultánea de tu lengua en su clítoris y en su interior, hace que explote."
    call OrgasmX ("c15s004_095") from _call_OrgasmX_26
    eil "¡Oh, SÍ! *Gemido* ¡No saques la lengua ahora!"
    "El sonido llega amortiguado a tus oídos. Las piernas de [eil] presionan con fuerza contra ellos mientras sus jugos inundan tu boca."
    if emm._var("route") or eri._var("route") or dap._var("route") or sam._var("route") or sca._var("route"):
        "Cada vez disfrutas más de estos orgasmos explosivos. Te provocan un sentimiento de trabajo bien hecho difícil de igualar."
    scene c15s004_190pv with dissolve
    show c15s004_190v with dissolve
    "Continúas introduciendo y sacando tu lengua de la vagina de [eil] durante un tiempo que no puedes medir hasta que te interrumpe."
    eil "*Gemido* Para o me voy a caer del columpio."
    call BlinkXP ("c15s004_080" , "d") from _call_BlinkXP_1204
    eil "Te necesito dentro de mí. Ahora."
    scene c15s004_200pv with dissolve
    "Te levantas y te bajas los pantalones. El columpio tiene la altura perfecta para que apoyes tu glande en la entrada de su cueva."
    show c15s004_200v with dissolve
    hide c15s004_190v
    "Empiezas a bombear con toda tu energía. El bamboleo del columpio adelante y atrás ayuda a [eil] a marcarte el ritmo con sus piernas entrelazadas detrás de tu culo."
    eil "¡Por el amor de Dios! *Gemido* ¡Te puedo notar muy profundo dentro de mí!"
    "[eil] tiene razón, la posición permite que en cada embestida llegues a su cérvix. Sabes que después de esto estará dolorida, pero también sabes que le encanta que golpees la puerta de su útero."
    eil "*Jadeo* ¡No se te ocurra dejar de hacerlo! *Gemido* Da lo mismo si duele un poco..."
    scene c15s004_205pv with dissolve
    show c15s004_205v with dissolve
    hide c15s004_200v
    "Parece que tu pensamiento sobre su cérvix se ha dejado notar en tus movimientos y lleváis mucho tiempo juntos. Sabéis lo que piensa el otro con sólo una mirada o un cambio de ritmo."
    "Vuelves a acelerar. Intentando llegar más profundo cada vez y topando cada vez en el cuello del útero."
    eil "¡Oh, sí! *Gemido* ¡Cómo echaba de menos esta sensación!"
    mc "Después no me eches la culpa..."
    eil "¡Te la echaré! *Jadeo* ¡No es culpa mía que tu polla sea enorme!"
    scene c15s004_210pv with dissolve
    show c15s004_210v with dissolve
    hide c15s004_205v
    eil "¿Te queda mucho? *Gemido* Yo estoy a punto de llegar otra vez..."
    mc "Solo un poco más... Comerte me ha puesto muy cachondo."
    "El dolor y el placer se entremezclan en la cara de [eil] a cada embestida. Es un dolor placentero, un placer doloroso."
    eil "¡Córrete dentro de mí! *Gemido* Quiero notar tu caliente descarga bien dentro de mí."
    "Puedes notar tu orgasmo acercándose a pasos agigantados, mientras percibes los síntomas del de [eil] llegando como una avalancha."
    "Con sus piernas aprisionándote como un abrazo de oso, te sería difícil dar marcha atrás aunque quisieras."
    if persistent.walkthrough:
        $ wt1 = _("[eil] embarazada")
        $ wt2 = _("Sin consecuencias")
    else:
        $ wt1 = ""
        $ wt2 = ""
    menu:
        "Correrte dentro." (wt = wt2):
            pass
        "Correrte dentro. Ir a por el bebé." (wt = wt1) if persistent.pregnancy and not eil._var("pregnant"):
            $ eil._var("pregnant", True)
            play sound ("music/OldMusicBox5.ogg")
    call OrgasmX ("c15s004_095b") from _call_OrgasmX_27
    "Vuestros orgasmos llegan simultáneamente en una explosión compartida de fuertes espasmos."
    mc "¡Mpfft!"
    eil "*Gemido* ¡Sí! ¡Sí! *Jadeo* ¡Joder!"
    scene c15s004_205pv with dissolve
    show c15s004_205v with dissolve
    hide c15s004_210v
    "Continúas bombeando unos momentos más para alargar al máximo el placer de [eil], pese a que tus piernas amenazan con no seguir aguantándote."
    eil "*Gemido* ¡Continúa todo lo que puedas! *Jadeo* ¡Te quiero! *Gemido* ¡Es enorme!"
    "No sabes si se refiere al orgasmo o a tu martillo del amor, pero continúas embistiendo entre espasmos de placer hasta que su cuerpo te indica que puedes parar."
    "Tus piernas han estado a punto de sucumbir."
    call BlinkXP ("c15s004_100" , "d") from _call_BlinkXP_1205
    "[eil] se derrumba encima de tu hombro, exhausta. Toda la energía que tenía tan solo hace unos segundos ha desaparecido tras el clímax."
    eil "Ha sido fantástico... notarte tan dentro de mí... ¡Ufff!"
    eil "Ha sido mucho mejor que en el viejo columpio de tu casa con el neumático..."
    mc "Me alegra que prefieras este... entonces... ¿neumático o tabla?"
    call BlinkXP ("c15s004_105" , "d") from _call_BlinkXP_1206
    eil "¡Tabla, por supuesto! *Risa* Habrá que ponerlo en un sitio que no se vea desde la casa..."
    mc "Ya buscaremos algún sitio, aunque será difícil justificar que es para los niños si no los podemos vigilar desde la piscina. *Risa*"
    call BlinkXP ("c15s004_110" , "d") from _call_BlinkXP_1207
    eil "Se está muy bien aquí, en tus brazos, pero deberíamos irnos si tengo que llevar a las abuelas de compras."
    mc "Cuando quieras."
    eil "En un minuto..."
    scene black with dissolve
    "Pasa un minuto y pasan dos. Pasan cinco e incluso diez. El hogar está donde están las personas a las que amas. En ese momento el hogar de ambos está en el columpio."
    "Volvéis al coche en silencio. No puedes saber en qué está pensando [eil], pero en tu mente se está formando la idea de un columpio que construir."
    return
label c15s005_LisaDate:
    if _in_replay:
        call mrS3_dap_route from _call_mrS3_dap_route_23
        call mrS3_sca_route from _call_mrS3_sca_route_20
        menu:
            "¿Intentaste besar a Kate en el Verdad o Reto en la playa?"
            "Sí":
                $ kat._var("kissedBeach" , True)
                menu:
                    "¿Te rechazó?"
                    "Sí":
                        $ kat._var("kissRejected" , True)
                    "No":
                        $ kat._var("kissRejected" , False)
            "No":
                $ kat._var("kissedBeach" , False)
                $ kat._var("kissRejected" , False)
        menu:
            "¿Tienes Puntos de Relación positivos con Kim?"
            "Si":
                $ kim._var("relationshipPoints", 5, intention = "set")
            "No":
                $ kim._var("relationshipPoints", -5, intention = "set")
                menu:
                    "¿Intentaste besar a Kim en el Verdad o Reto en la playa?"
                    "Sí":
                        $ kim._var("kissedBeach" , True)
                    "No":
                        $ kim._var("kissedBeach" , False)
        menu:
            "¿Intentaste besar a Debbie en el Verdad o Reto en la playa?"
            "Sí":
                $ deb._var("kissedBeach" , True)
            "No":
                $ deb._var("kissedBeach" , False)
        menu:
            "¿Tienes Puntos de Relación positivos con Debbie?"
            "Si":
                $ deb._var("relationshipPoints", 5, intention = "set")
            "No":
                $ deb._var("relationshipPoints", -5, intention = "set")
        menu:
            "¿Intentaste besar a Lisa en el Verdad o Reto en la playa?"
            "Sí":
                $ lis._var("kissedBeach" , True)
                menu:
                    "¿Te rechazó?"
                    "Sí":
                        $ lis._var("kissRejected" , True)
                    "No":
                        $ lis._var("kissRejected" , False)
            "No":
                $ lis._var("kissedBeach" , False)
                $ lis._var("kissRejected" , False)
        menu:
            "¿Descubriste que la persona que hablaba por teléfono durante tu comida con [eil] era Anthony?"
            "Sí":
                $ mc._var("knowsAnthony" , True)
            "No":
                $ mc._var("knowsAnthony" , False)
    stop music fadeout (1.5)
    "Llegáis a casa y dejas el coche en la calle. No tiene sentido meterlo dentro del garaje si [eil] va a llevar a Betty y a las chicas a la ciudad."
    "Justo cuando vas a entrar en casa te encuentras con Lisa saliendo."
    call BlinkXP ("c15s005_005", "d") from _call_BlinkXP_1208
    play music ("music/Swing.ogg")
    mc "Buenas tardes, Lisa."
    lis "Hola, [mc]."
    mc "¿Vas a salir?"
    call BlinkXP ("c15s005_010", "d") from _call_BlinkXP_1209
    lis "Sí, voy al cine... con Anthony..."
    mc "¿Pasa algo? Imaginaba que estarías más contenta con la segunda cita..."
    call BlinkXP ("c15s005_015", "d") from _call_BlinkXP_1210
    lis "{b}¡No es una cita!{/b} Tan solo vamos a ver una película juntos. Y es la tercera vez que... salimos... ayer fuimos a cenar... cuando tú estabas desaparecido."
    mc "Vale, vale... no quería suponer nada. Con lo ilusionada que parecías la primera vez, creía que..."
    call BlinkXP ("c15s005_020", "d") from _call_BlinkXP_1211
    lis "¡Pues no tienes que creer nada! Solo somos amigos..."
    mc "Vale, vale... ¿Quieres que me quede contigo hasta que llegue?"
    call BlinkXP ("c15s005_025", "d") from _call_BlinkXP_1212
    lis "Si no te importa..."
    if mc._var("knowsAnthony"):
        mcp "(Si lo que he oído en el Burger Prince es cierto y {b}si era Anthony{/b} debería decirle algo...)"
        mcp "(Pero si no era él, sería meterme donde no me llaman y podría crear un problema donde no lo hay. Mejor me quedo callado...)"
    mc "No me importa, Lisa. Estoy aquí para lo que necesites."
    scene c15s005_030AnBlink with fade
    "Lisa está visiblemente incómoda por alguna razón y de vez en cuando te mira de reojo, como si quisiera decir algo, pero no se atreviera."
    "El silencio se va haciendo más incómodo tal como va pasando el rato."
    mc "Lisa, ¿he hecho algo malo?"
    call BlinkXP ("c15s005_035", "d") from _call_BlinkXP_1213
    if lis._var("kissedBeach") and not lis._var("kissRejected"):
        mc "¿Es por el beso de ayer?"
        $ Aux = 1
    elif lis._var("kissRejected"):
        mc "¿Es porque intenté besarte ayer?"
        $ Aux = 2
    elif deb.rps > 0:
        mc "¿Es porque Debbie y yo nos besamos ayer?"
        $ Aux = 3
    elif dap._var("route") or sca._var("route") or kim.rps > 0 or kim._var("kissedBeach") or kat._var("kissedBeach"):
        $ Aux = 0
        if dap._var("route"):
            $ Aux = Aux + 1
        if sca._var("route"):
            $ Aux = Aux + 1
        if kim.rps > 0 or kim._var("kissedBeach"):
            $ Aux = Aux + 1
        if kat._var("kissedBeach") and not kat._var("kissRejected"):
            $ Aux = Aux + 1
        if Aux > 1:
            mc "¿Es porque no te besé ayer habiendo besado a otras chicas?"
        else:
            mc "¿Es porque no te besé ayer habiendo besado a otra chica?"
        $ Aux = 4
    else:
        mc "¿Es por algo que hice o no hice ayer?"
        $ Aux = 5
    if Aux == 1 or Aux == 2:
        lis "¡No!... Sí... No lo sé... No estoy acostumbrada a que la gente quiera besarme, y menos aún... diciendo que se siente atraída por mí..."
        mc "Siento si te incomodé."
        call BlinkXP ("c15s005_040", "d") from _call_BlinkXP_1214
        lis "No es que me incomodaras... es que... tú viniste a mí... a besarme... mientras Anthony... ni siquiera lo ha intentado..."
        call c15s005_Anthony from _call_c15s005_Anthony
    elif Aux == 3:
        call BlinkXP ("c15s005_055", "d") from _call_BlinkXP_1215
        lis "No, no tiene nada que ver con eso..."
        if deb._var("kissedBeach"):
            lis "Ni con que la quisieras besar a ella y no a mí... no es que yo quisiera que me besaras, claro..."
        call BlinkXP ("c15s005_060", "d") from _call_BlinkXP_1216
        lis "Estoy acostumbrada a que no quieran besarme... mira Anthony, por ejemplo..."
        call c15s005_Anthony from _call_c15s005_Anthony_1
    elif Aux == 4 or Aux == 5:
        call BlinkXP ("c15s005_055", "d") from _call_BlinkXP_1217
        lis "No, yo no soy nadie para decirte a quien debes querer besar o a quien no. Ni tú... ni Anthony..."
        lis "No quiero decir que ayer me hubiera hecho ilusión que me besaras, por supuesto..."
        call c15s005_Anthony from _call_c15s005_Anthony_2
    if deb.rps > 0:
        stop music fadeout (1.5)
        call BlinkXP ("c15s005_065", "d") from _call_BlinkXP_1218
        lis "Pero como se te ocurra hacerle daño a Debbie... te vas a enterar de quién soy yo."
        play music ("music/SeeingHeaven.ogg")
        "El cambio de tema te pilla totalmente desprevenido."
        mc "Lisa, solo era un juego. No creo que..."
        call BlinkXP ("c15s005_070", "d") from _call_BlinkXP_1219
        lis "¿Qué? ¿Que la chica que siempre se ha sentido el patito feo pueda creer que le puede gustar a alguien?"
        lis "¿Que mi hermana se pueda hacer ilusiones con el chico que le ha dado su primer beso?"
        mc "No sabía que era su primer beso, Lisa. Si lo hubiera sabido..."
        call BlinkXP ("c15s005_075", "d") from _call_BlinkXP_1220
        lis "Si lo hubieras sabido, ¿qué hubieras hecho?"
        if deb._var("kissedBeach"):
            lis "¿Mentir y no querer besarla?"
        else:
            lis "¿Rechazarla y hacerla sentir mal?"
        mc "No sé lo que hubiera hecho, Lisa. Seguramente hablar con ella antes del beso."
        call BlinkXP ("c15s005_080", "d") from _call_BlinkXP_1221
        lis "Sí, claro... \"Chicas, esperad un momento porque tengo que hablar con Debbie sobre si le doy su primer beso o no\". ¿Te das cuenta de que con eso la avergonzarías aún más?"
        mc "Por supuesto. Pero al no tener la información... cuando la tuve... no sé... me pareció lo mejor continuar."
        call BlinkXP ("c15s005_085", "d") from _call_BlinkXP_1222
        lis "¡Obviamente! Una vez estabas en esa situación solo podías continuar..."
        call BlinkXP ("c15s005_090", "d") from _call_BlinkXP_1223
        lis "Pero ve con cuidado con ella, por favor. Es muy sensible..."
        mc "Hablaré con ella si es lo que quieres, o si crees que es lo mejor."
        call BlinkXP ("c15s005_095", "d") from _call_BlinkXP_1224
        lis "Todo depende de lo que vayas a decirle..."
        mc "No sé lo que voy a decirle, pero con lo que me acabas de decir, creo que sería bueno que habláramos."
        lis "Yo también lo creo."
    "Justo en ese momento se oye el motor de un coche en la lejanía."
    call BlinkXP ("c15s005_100", "d") from _call_BlinkXP_1225
    lis "Ahí llega Anthony con su contaminante coche."
    mc "Pasáoslo bien en el cine. ¿Cenarás en casa o cenarás con él?"
    call BlinkXP ("c15s005_105", "d") from _call_BlinkXP_1226
    lis "*Risa* ¿Celoso?"
    mc "Nope. *Risa* Es para decirle a mi madre para cuantas personas tiene que preparar cena."
    call BlinkXP ("c15s005_110", "d") from _call_BlinkXP_1227
    lis "¡Oops! *Risa* Eso me pasa por intentar hacerme la graciosa. Cenaré en casa seguramente. Si al final decidimos quedarnos a cenar fuera, ya avisaré a [mar]."
    mc "Perfecto entonces. Nos vemos, Lisa."
    lis "Hasta luego, [mc]."
    scene black with dissolve
    "Anthony recoge a Lisa y tú te diriges a casa de [nor] para hablar con ella y [mar] sobre la reunión con Aaron."
    stop music fadeout (1.5)
    if deb.rps > 0:
        "Tendrás que hablar con Debbie, y no es una conversación que estés ansioso por tener. No tienes ni idea de hacia dónde puede evolucionar esa conversación."
        if dap._var("route"):
            "Especialmente después de que te pillara con [dap] esta mañana."
    return
label c15s005_Anthony:
    call BlinkXP ("c15s005_045", "d") from _call_BlinkXP_1228
    lis "Y antes de que preguntes, eso no significa que a Anthony le dejase hacerlo, claro... cada vez estoy más segura de que... solo vamos a ser amigos..."
    lis "No siento lo mismo por él que por... no siento por Anthony lo que debería sentir para empezar una relación con él."
    mc "Parece buen chico... quizás aclararlo sea lo mejor, si no te sientes atraída por él."
    if mc._var("knowsAnthony"):
        mcp "(Y si el del restaurante era él, parece que es mutuo.)"
    call BlinkXP ("c15s005_050", "d") from _call_BlinkXP_1229
    lis "No piensas que haya coqueteado con él o que le haya dado falsas esperanzas, ¿verdad?"
    mc "No, Lisa. Os conocisteis por internet. Te mudaste aquí y cuando os habéis conocido la chispa no ha saltado. Nadie te puede acusar de nada."
    return
label c15s005_BeforeAaronVisit:
    if _in_replay:
        call mrS3_dap_route from _call_mrS3_dap_route_24
        call mrS3_mar_route from _call_mrS3_mar_route_28
        call mrS3_nor_route from _call_mrS3_nor_route_20
        call mrS3_emm_route from _call_mrS3_emm_route_31
        call mrS3_eri_route from _call_mrS3_eri_route_24
        call mrS3_sam_route from _call_mrS3_sam_route_15
        call mrS3_sim_route from _call_mrS3_sim_route_16
    if not sam._var("route") and not sim._var("route"):
        if nor._var("route"):
            $ Caught = 1 #RIAM, don't track this one
        elif mar._var("route"):
            $ Caught = 2
        else:
            $ Caught = 5
    else:
        if nor._var("route"):
            $ Caught = 3
        elif mar._var("route"):
            $ Caught = 4
        else:
            $ Caught = 5
    play music ("music/Embrace.ogg")
    "En la cocina de [nor]..."
    if Caught == 1 or Caught == 3:
        scene c15s005_130d with fade:
            yalign 1.0
            linear 5.0 yalign 0.0
        pause (5.0)
        call BlinkXP ("c15s005_130" , "d") from _call_BlinkXP_1230
        mc "Hola, Tía [nor]. ¡Qué elegante!"
        if not _in_replay:
            $ renpy.notify ("Profile Image unlocked for Norah. 5 - Professional")
            $ nor.profileImages.pop (4) # first remove
            $ nor.profileImages.insert (4, ("norah_4", None)) # then add new
        nor "El tal Aaron va a llegar en un rato. No quieres que me pasee en ropa interior delante de él, ¿verdad?"
        mc "Por mí no habría ningún problema, pero supongo que el pobre chico no podría concentrarse. *Risa*"
    else:
        call BlinkXP ("c15s005_130b" , "d") from _call_BlinkXP_1231
        if persistent.family:
            mc "Hola, Mamá. ¡Qué elegante!"
        else:
            mc "Hola, [mar!t]. ¡Qué elegante!"
        mom "El tal Aaron va a llegar en un rato. Hay que ser mínimamente profesional, ¿verdad? No sabemos de lo que quiere hablarnos."
        mc "Espero que Tía [nor] también se vista profesional, o el pobre chico no va a poder concentrarse si ella baja en ropa interior."
    if Caught == 1 or Caught == 3:
        call BlinkXP ("c15s005_135" , "d") from _call_BlinkXP_1232
        nor "¿Chico? ¿Qué edad tiene?"
    else:
        call BlinkXP ("c15s005_135b" , "d") from _call_BlinkXP_1233
        mom "¿Chico? ¿Qué edad tiene?"
    mc "Si lo que he deducido de la información que me envió Jamaal es cierto, debe ser algo más joven que yo."
    if Caught == 1 or Caught == 3:
        call BlinkXP ("c15s005_140" , "d") from _call_BlinkXP_1234
        nor "No encaja. Erik le llamó \"el viejo\" cuando habló de que habían intentado matarlo..."
    else:
        call BlinkXP ("c15s005_140b" , "d") from _call_BlinkXP_1235
        mom "Por lo que había dicho [nor], creía que sería más mayor."
    mc "También podría ser que la información de Jamaal, o lo que yo saqué de ella, no sea del todo correcta."
    if Caught < 5:
        mc "Pero lo descubriremos en breve. Ahora quiero un beso..."
        if Caught == 1:
            call BlinkXP ("c15s005_145" , "d") from _call_BlinkXP_1236
            nor "¿Aquí? ¿Ahora? ¡La casa está llena de gente! ¿Tú quieres que le dé un infarto a mi madre?"
        elif Caught == 3:
            call BlinkXP ("c15s005_145" , "d") from _call_BlinkXP_1237
            nor "¿Aquí? ¿Ahora? ¡La casa está llena de gente! ¿Tú quieres que le dé un infarto a mi madre? ¿O que continúe la discusión de ayer?"
        elif Caught == 2:
            call BlinkXP ("c15s005_145b" , "d") from _call_BlinkXP_1238
            if persistent.family:
                mom "¿Aquí? ¿Ahora? ¡La casa está llena de gente! ¿Tú quieres que le dé un infarto a mi madre?"
            else:
                mom "¿Aquí? ¿Ahora? ¡La casa está llena de gente! ¿Tú quieres que le dé un infarto a Olivia?"
        else:
            call BlinkXP ("c15s005_145b" , "d") from _call_BlinkXP_1239
            if persistent.family:
                mom "¿Aquí? ¿Ahora? ¿Tú quieres que nos pille mi madre y que continúe la bronca de ayer en la playa?"
            else:
                mom "¿Aquí? ¿Ahora? ¿Tú quieres que nos pille Olivia y que continúe la bronca de ayer en la playa?"
        mc "Me da lo mismo lo que piense Meemaw. Estoy harto de esconderme."
        if Caught == 1 or Caught == 3:
            call BlinkXP ("c15s005_150" , "d") from _call_BlinkXP_1240
            nor "Yo también. Lo de la piscina de anteayer es una demostración de que tenemos que hacerlo público cuanto antes."
            if eri._var("route"):
                mc "¿Quieres incluir a alguien más en lo que pasó con [eri]?"
                call BlinkXP ("c15s005_155a" , "d") from _call_BlinkXP_1241
                nor "¿Qué? ¡No!... o sí... no sé... pero me refiero a que... sentí una conexión preciosa con una de mis hijas que no había sentido nunca."
                call BlinkXP ("c15s005_155b" , "d") from _call_BlinkXP_1242
                if dap._var("route"):
                    nor "Si [dap] no saliera con nadie... casi te pediría que empezaras a salir con ella para poder compartir lo mismo que hice con [eri]."
                    nor "A menos que..."
                else:
                    nor "Estoy casi tentada de pedirte que empieces a salir con [dap] para poder compartir lo mismo que hice con [eri]. *Risa*"
            else:
                mc "¿A qué te refieres?"
                call BlinkXP ("c15s005_155b" , "d") from _call_BlinkXP_1243
                nor "A que [eri] nos dejó solos porque sabe lo nuestro... si ella no lo hubiera sabido..."
        else:
            call BlinkXP ("c15s005_150b" , "d") from _call_BlinkXP_1244
            if Caught == 2:
                mom "Yo también. Tengo muchas ganas de contárselo a [emm] y..."
            elif Caught == 4:
                mom "Lo de ayer fue un paso... pero hay que dar más. Tengo ganas de contárselo a [emm] y..."
        mc "Ven aquí..."
        if Caught == 1 or Caught == 3:
            scene c15s005_160a with dissolve
        else:
            scene c15s005_160b with dissolve
        stop music fadeout (1.5)
        "Vuestros labios se juntan en un beso más tierno que sensual, un beso que confirma que ambos estáis en la misma página."
        if Caught == 1 or Caught == 3:
            scene c15s005_160c with dissolve
        else:
            scene c15s005_160d with dissolve
        play music ("music/WarIsComing.ogg")
        "Como no podía ser de otra forma, justo en ese momento tenía que aparecer alguien."
        call BlinkXP ("c15s005_165" , "h") from _call_BlinkXP_1245
        mee "¿Qué está pasando aquí?"
        if Caught == 1 or Caught == 2:
            call BlinkXP ("c15s005_170" , "d") from _call_BlinkXP_1246
            bet "Ermmm... Ya sabes que se saludan así en casa..."
            if nor._var("route"):
                call BlinkXP ("c15s005_175" , "d") from _call_BlinkXP_1247
                nor "No, Tía Betty. [mc] y yo estamos juntos."
                call BlinkXP ("c15s005_180" , "d") from _call_BlinkXP_1248
                nor "Ya está, ya lo he dicho... se acabó el secreto..."
                scene c15s005_160c with dissolve
                bet "¡Lo sabía!" (multiple = 2)
                mom "¿Qué? ¿Desde cuándo?" (multiple = 2)
            else:
                call BlinkXP ("c15s005_175b" , "d") from _call_BlinkXP_1249
                mom "No, Tía Betty. [mc] y yo estamos juntos."
                call BlinkXP ("c15s005_180b" , "d") from _call_BlinkXP_1250
                mom "Ya está, ya lo he dicho... se acabó el secreto..."
                scene c15s005_160d with dissolve
                bet "¡Lo sabía!" (multiple = 2)
                nor "¿Qué? ¿Desde cuándo?" (multiple = 2)
            mee "¿Estáis locos?"
            call BlinkXP ("c15s005_185" , "d") from _call_BlinkXP_1251
            if nor._var("route"):
                if persistent.family:
                    mee "¡Es tu sobrino, por el amor de Dios!"
                else:
                    mee "¡Es prácticamente tu sobrino, por el amor de Dios!"
            else:
                if persistent.family:
                    mee "¡Es tu hijo, por el amor de Dios!"
                else:
                    mee "¡Lo has criado como a tu propio hijo, por el amor de Dios!"
            mee "¡Y le doblas la edad!"
            if nor._var("route"):
                if mar._var("route"):
                    call BlinkXP ("c15s005_190" , "d") from _call_BlinkXP_1252
                    if persistent.family:
                        mom "También es mi hijo, Mamá, y también le doblo la edad... casi..."
                    else:
                        mom "También es prácticamente mi hijo, Olivia, y también le doblo la edad... casi..."
                    call BlinkXP ("c15s005_195" , "d") from _call_BlinkXP_1253
                    mee "¿Qué?"
                    call BlinkXP ("c15s005_200" , "d") from _call_BlinkXP_1254
                    mom "¿Preparado?"
                    mc "Nunca lo he estado más."
                    scene c15s005_205a with dissolve
                    "Los labios de [mar] rozan los tuyos de una forma diferente de la habitual. Están haciendo una declaración delante del resto de mujeres."
                    call BlinkXP ("c15s005_210" , "d") from _call_BlinkXP_1255
                    bet "¡Esto también lo sabía!"
            if nor._var("route") and mar._var("route"):
                scene c15s005_205b with dissolve
                nor "Estamos juntos y ya está." (multiple=2)
                if persistent.family:
                    mom "Aunque mi hermana y yo vamos a tener que hablar." (multiple=2)
                else:
                    mom "Aunque [nor] y yo vamos a tener que hablar." (multiple=2)
            elif nor._var("route"):
                scene c15s005_205c with dissolve
                nor "Estamos juntos y ya está."
            else:
                scene c15s005_205d with dissolve
                mom "Estamos juntos y ya está."
        else:
            call BlinkXP ("c15s005_170" , "d") from _call_BlinkXP_1256
            bet "La continuación de lo de ayer en la playa, por lo que parece..."
            call BlinkXP ("c15s005_215" , "d") from _call_BlinkXP_1257
            mee "¿Pero aquí? ¿En casa? ¿Donde las niñas pueden verles?"
            if nor._var("route"):
                if mar._var("route"):
                    scene c15s005_205a with dissolve
                    "[mar] se dirige a ti y sus labios rozan los tuyos de una forma diferente de la habitual. Están haciendo una declaración delante del resto de mujeres."
                    call BlinkXP ("c15s005_140b" , "d") from _call_BlinkXP_1258
                    if persistent.family:
                        mom "Tenemos intención de decírselo a nuestras hijas en cuanto podamos. Con lo que no hay razón para esconderse."
                    else:
                        mom "Tenemos intención de decírselo a las niñas en cuanto podamos. Con lo que no hay razón para esconderse."
                    call BlinkXP ("c15s005_215" , "d") from _call_BlinkXP_1259
                    mee "¿Qué?"
                    scene c15s005_205b with dissolve
                    nor "Estamos juntos y ya está." (multiple=2)
                    if persistent.family:
                        mom "Aunque mi hermana y yo aún tenemos que pulir cosas." (multiple=2)
                    else:
                        mom "Aunque [nor] y yo aún tenemos que pulir cosas." (multiple=2)
                else:
                    call BlinkXP ("c15s005_220" , "d") from _call_BlinkXP_1260
                    nor "Tengo intención de decírselo a [dap] en cuanto tenga la ocasión. [eri] ya lo sabe y lo acepta."
                    if eri._var("route"):
                        mcp "(Al menos no mataremos a Meemaw de un infarto diciéndole que también estoy con [eri].)"
                    call BlinkXP ("c15s005_195" , "d") from _call_BlinkXP_1261
                    mee "¿Qué?"
                    scene c15s005_205c with dissolve
                    nor "Estamos juntos y ya está."
            else:
                call BlinkXP ("c15s005_225" , "d") from _call_BlinkXP_1262
                mom "Tengo intención de decírselo a [emm] en cuanto tenga la ocasión."
                if emm._var("route"):
                    mcp "(No te puedo decir que [emm] ya lo sabe. Sería liarla demasiado ahora mismo, y prefiero que te lo diga ella.)"
                call BlinkXP ("c15s005_215" , "d") from _call_BlinkXP_1263
                mee "¿Qué?"
                scene c15s005_205d with dissolve
                mom "Estamos juntos y ya está."
        mc "Y te puedes enfadar si quieres, pero no va a cambiar nada."
        mc "Lo máximo que vas a conseguir es alienarnos a nosotros y que te dejemos fuera de esto."
    else:
        mc "Le he pedido a [eil] que lleve a Tía Betty, a Meemaw, a [dap] y a [emm] de compras, pero no sé qué vamos a hacer con Kiara y las estudiantes."
        call BlinkXP ("c15s005_230" , "d") from _call_BlinkXP_1264
        mom "Si están en la otra casa no creo que haya problemas, ¿no? [sai] y Debbie están en la universidad y Lisa ha salido. Sólo habría que preocuparse de Kate, Kim, y Kiara."
        mc "Nuestro propio KKK. *Risa* Por suerte sólo en cuanto a iniciales."
        call BlinkXP ("c15s005_235" , "d") from _call_BlinkXP_1265
        mom "*Risa* ¡Qué payaso eres!"
        mc "Si te hago reír, bienvenido sea."
        mc "Hablando de Kiara, por ahí viene."
    return
label c15s005_MeemawDiscussion:
    if _in_replay:
        call mrS3_dap_route from _call_mrS3_dap_route_25
        call mrS3_mar_route from _call_mrS3_mar_route_29
        call mrS3_nor_route from _call_mrS3_nor_route_21
        call mrS3_emm_route from _call_mrS3_emm_route_32
        call mrS3_eri_route from _call_mrS3_eri_route_25
        call mrS3_sam_route from _call_mrS3_sam_route_16
        call mrS3_sim_route from _call_mrS3_sim_route_17
        call mrS3_eil_route from _call_mrS3_eil_route_18
        if not sam._var("route") and not sim._var("route"):
            if nor._var("route"):
                $ Caught = 1 #RIAM, don't track this one
            elif mar._var("route"):
                $ Caught = 2
            else:
                $ Caught = 5
        else:
            if nor._var("route"):
                $ Caught = 3
            elif mar._var("route"):
                $ Caught = 4
            else:
                $ Caught = 5
    if Caught == 5:
        scene c15s005_250a with dissolve
        mc "¡Qué guapas estáis todas!"
        kia "Gracias, [mc]."
        bet "Hay que dar buena impresión, ¿no? No puedo ir a comprar ropa vestida con harapos o con el hábito. *Risa*"
        mee "Y yo tenía ganas de ponerme un vestido... Ahora solo falta que [eil] acabe su llamada de teléfono."
        nor "¿Tú no te vas a cambiar para la reunión de... negocios?"
        mc "Sí, ahora iré. Me quiero dar una ducha."
        call BlinkXP ("c15s005_255" , "d") from _call_BlinkXP_1266
        kia "¿Puedo hablar contigo un momento?"
        mc "Sí, claro."
        call BlinkXP ("c15s005_260" , "f") from _call_BlinkXP_1267
        kia "Me ha dicho [eil] que necesitabais la casa vacía, y me he ofrecido a enseñarles a Kate y Kim a la biblioteca municipal, pero necesitaré un coche."
        mc "Gracias, Kiara. Puedes coger el de mi madre. El de [nor] no es muy fiable. Acompáñame a casa y te doy las llaves, y así me cambio de ropa."
        kia "Perfecto, gracias."
        call BlinkXP ("c15s005_355" , "f") from _call_BlinkXP_1268
        stop music fadeout (1.5)
        bet "¿Puedo preguntarte algo? Hace días que no te veo saludar a nadie con un beso ¿Me puedo unir a esos los saludos? Me parece una costumbre genial."
        play music ("music/LifeOfAWanderingWizard.ogg")
        call c15s005_kisses from _call_c15s005_kisses
        call c15s005_kisses2 from _call_c15s005_kisses2
        mc "*Risa* ¿Vamos a por las llaves?"
        call c15s005_kisses3 from _call_c15s005_kisses3
    else:
        call BlinkXP ("c15s005_265" , "d") from _call_BlinkXP_1269
        mee "Es decir, me estás diciendo que no me meta donde no me llaman, aunque vea claramente que estáis cometiendo un error, ¿no?"
        call BlinkXP ("c15s005_270" , "d") from _call_BlinkXP_1270
        bet "No creo que sea lo que te están diciendo exactamente... aunque estaría bien que alguien alguna vez te pusiera en tu sitio."
        mc "Cierto, no exactamente. Lo que te estoy diciendo es que, si nos quieres apoyar en nuestra relación, eres bienvenida."
        mc "Pero que si lo único que vas a aportar son quejas y argumentos que no compartimos, te agradecería si te los guardaras. Ya hemos pensado en todos ellos y no han evitado esta relación."
        call BlinkXP ("c15s005_275" , "d") from _call_BlinkXP_1271
        if sam._var("route") or sim._var("route"):
            kia "Sé que, como hice ayer, me voy a volver a meter en un tema familiar que posiblemente no me corresponde..."
        else:
            kia "Sé que me voy a meter en un tema familiar que posiblemente no me corresponde..."
        mc "Kiara, si estuviste en la comida de ayer, es que perteneces a la familia. Todas las opiniones son bienvenidas."
        call BlinkXP ("c15s005_280" , "d") from _call_BlinkXP_1272
        mee "Todas menos la mía, ¿no?"
        mc "La tuya también. Lo que no es bienvenido es la estrechez de mente y las teorías caducas sobre relaciones familiares."
        call BlinkXP ("c15s005_285" , "d") from _call_BlinkXP_1273
        mee "*Grrrr*"
        mc "Mientras la abuela gruñe, ¿qué querías decir, Kiara?"
        call BlinkXP ("c15s005_290" , "d") from _call_BlinkXP_1274
        kia "Primero, darte las gracias por decir que pertenezco a la familia... se siente raro... y más en una familia tan diferente como esta... pero se siente bien."
        mc "No he dicho nada que no crea que pensamos todos..."
        todas "Totalmente de acuerdo."
        if eil._var("route"):
            kia "Lo siguiente es que... cuando [eil] me dijo que podrías estar con más chicas aparte de ella..."
            if nor._var("route") and nor._var("route"):
                scene c15s005_295a with hpunch
                nor "¿QUÉ?" (multiple = 2)
                mom "¿También está con [eil]?" (multiple = 2)
                call BlinkXP ("c15s005_300" , "d") from _call_BlinkXP_1275
                kia "Espera... ¿No lo sabíais? Me parece que he metido la pata..."
            elif nor._var("route"):
                scene c15s005_295b with hpunch
                nor "¿Qué? ¿También está con [eil]?"
                call BlinkXP ("c15s005_300" , "d") from _call_BlinkXP_1276
                kia "Espera... ¿No lo sabías? Me parece que he metido la pata..."
            else:
                scene c15s005_295c with hpunch
                mom "¿Qué? ¿También está con [eil]?"
                call BlinkXP ("c15s005_300" , "d") from _call_BlinkXP_1277
                kia "Espera... ¿No lo sabías? Me parece que he metido la pata..."
            mc "No pasa nada, Kiara. [eil] me autorizó a hacerlo público si lo consideraba necesario, y estaba esperando el momento adecuado... continúa, Kiara, por favor."
            if nor._var("route") and nor._var("route"):
                scene c15s005_305a with dissolve
                nor "No pasa nada, pero..." (multiple=2)
                mom "Vamos a tener que hablar de esto." (multiple=2)
            elif nor._var("route"):
                scene c15s005_305b with dissolve
                nor "No pasa nada, pero tú y yo vamos a tener que hablar de esto."
            else:
                scene c15s005_305c with dissolve
                mom "No pasa nada, pero tú y yo vamos a tener que hablar de esto."
            call BlinkXP ("c15s005_310" , "d") from _call_BlinkXP_1278
            kia "Lo que quería decir es que no me podía imaginar que estabas con miembros de tu familia también..."
        else:
            call BlinkXP ("c15s005_310" , "d") from _call_BlinkXP_1279
            kia "Lo siguiente es que, nunca me hubiera podido imaginar que salieras con miembros de tu propia familia..."
        kia "¿Sorprendente e inesperado? Sí. Pero si estamos en una sociedad donde la gente se casa con sus almohadas o se enamora de personajes de dibujos animados, ya nada me parece raro..."
        mc "Kiara, no es lo mismo..."
        call BlinkXP ("c15s005_315" , "d") from _call_BlinkXP_1280
        kia "Lo sé... a lo que me refiero es a que si eso se empieza a ver normal... ¿por qué no vuestra relación?"
        mc "Ah, OK. No te había entendido."
        call BlinkXP ("c15s005_320" , "d") from _call_BlinkXP_1281
        kia "En esta familia se respira amor... un amor diferente del que he conocido en cualquier otra familia."
        kia "No sé... no me extraña que el siguiente paso sea que se creen parejas... lo veo casi normal."
        call BlinkXP ("c15s005_325" , "d") from _call_BlinkXP_1282
        mee "¿Pero tú estás loca? ¿Estás diciendo que verías normal que [mc] saliera con su hermana? ¿O con mi hermana para el caso?"
        mee "¡Que nos queramos no significa que tengamos que montar una orgía de todos revueltos, joder!"
        mc "Meemaw, creo que no se refiere a eso..."
        call BlinkXP ("c15s005_330" , "d") from _call_BlinkXP_1283
        kia "No me refiero a eso, pero no ando muy lejos... Leí sobre una tribu donde la gente se casa con familiares directos. Obviamente, sin nuestra medicina, tienen todos los problemas de la endogamia..."
        kia "Pero si ellos lo pueden hacer, ¿por qué no vosotros? Aquí tienen acceso a medicina moderna..."
        mc "¿Ves, Meemaw? Y te lo está diciendo, posiblemente, la persona de la casa que más ha leído, con permiso de [dap] y [sca]."
        call BlinkXP ("c15s005_335" , "d") from _call_BlinkXP_1284
        mee "¿Estáis todos locos? ¿Qué será lo siguiente? ¿Vas a empezar a tirarle los trastos a tu hermana? ¿A tus primas? ¿A Betty?"
        stop music fadeout (1.5)
        mc "No es eso y lo sabes, Meemaw."
        call BlinkXP ("c15s005_340" , "d") from _call_BlinkXP_1285
        play music ("music/LifeOfAWanderingWizard.ogg")
        bet "Olivia Lena Pitt. ¿Tú sabes cuál es mi mayor hobby?"
        call BlinkXP ("c15s005_345" , "d") from _call_BlinkXP_1286
        mee "¡Zampar! Pero no veo qué tiene que ver eso con todo esto."
        call BlinkXP ("c15s005_350" , "d") from _call_BlinkXP_1287
        bet "No, ese es el segundo mayor. Mi mayor hobby es y siempre ha sido tocarte los huevos."
        call BlinkXP ("c15s005_355" , "d") from _call_BlinkXP_1288
        bet "¿Me puedo unir a los saludos con besos, [mc]?"
        call c15s005_kisses from _call_c15s005_kisses_1
        if eil._var("route"):
            call BlinkXP ("c15s005_425" , "d") from _call_BlinkXP_1289
            bet "Bueno, contigo no tiene mucho mérito sabiendo que salís juntos..."
            call BlinkXP ("c15s005_430" , "d") from _call_BlinkXP_1290
            eil "¿Qué?"
            mc "A tu madre se le ha escapado..."
            call BlinkXP ("c15s005_435" , "d") from _call_BlinkXP_1291
            eil "¡Mamaaaa!"
            call BlinkXP ("c15s005_440" , "d") from _call_BlinkXP_1292
            kia "Perdón... creía que..."
            mc "Ya te he dicho que no pasa nada..."
        call c15s005_kisses2 from _call_c15s005_kisses2_1
        call BlinkXP ("c15s005_465" , "d") from _call_BlinkXP_1293
        kia "¿Puedo hablar contigo un momento?"
        mc "Sí, claro."
        call BlinkXP ("c15s005_260" , "d") from _call_BlinkXP_1294
        kia "*Susurrando* Me ha dicho [eil] que necesitabais la casa vacía, y me he ofrecido a enseñarles a Kate y Kim a la biblioteca municipal, pero necesitaré un coche."
        mc "Gracias, Kiara. Puedes coger el de mi madre. El de [nor] no es muy fiable. Acompáñame a casa y te doy las llaves, y así me cambio de ropa."
        call BlinkXP ("c15s005_485" , "d") from _call_BlinkXP_1295
        nor "¡Hey, os estoy oyendo! Mi coche es muy fiable. Te puedes fiar de que se va a estropear en el momento menos adecuado. *Risa*"
        mc "Por eso es mejor que se lleve el coche de Mamá. *Risa*"
        mc "Voy a darle las llaves a Kiara y a cambiarme. Ahora vuelvo."
        call c15s005_kisses3 from _call_c15s005_kisses3_1
    scene black with dissolve
    "Acompañas a Kiara a casa y le entregas las llaves."
    stop music fadeout (1.5)
    "Decidís, tácitamente, no comentar nada sobre lo que acaba de pasar en la cocina."
    "Se despide de ti con otro beso, esta vez sin agresividad, tan solo un beso de despedida. Ya no tiene que demostrar nada a nadie."
    "Después pasas por tu habitación a darte una ducha y ponerte un traje."
    return
label c15s005_kisses:
    mc "¿Qué? Sí... bueno... pero... eso ya había acabado... era por un reto en un juego y duró solo una semana."
    call BlinkXP ("c15s005_360" , "d") from _call_BlinkXP_1296
    bet "Pues te reto a que lo reanudes. Y ya sé que el juego no funciona así. Pero te reto."
    bet "Si besas a toda la familia como saludo, mi retrógrada hermana no podrá escandalizarse... demasiado... si te ve besar a [eri], a [dap] o a [emm]... o a cualquier otra chica de la familia."
    bet "¿Aceptas el reto?"
    mc "¡Por supuesto!"
    call BlinkXP ("c15s005_365" , "d") from _call_BlinkXP_1297
    mee "¿Habéis perdido la cordura?"
    call BlinkXP ("c15s005_370" , "d") from _call_BlinkXP_1298
    bet "No le hagas caso. Tiene la tensión baja, con lo que no le va a dar un jamacuco."
    bet "Pues puedes empezar conmigo... si quieres..."
    call KissXP ("c15s005_375" , "d") from _call_KissXP_35
    "Vuestros labios se juntan en un breve beso que tiene mucho de cariño, un poco de pillería, y nada de pasión."
    bet "Gracias, [mc]. Creo que le podría pillar el gusto a esto..."
    call BlinkXP ("c15s005_380" , "d") from _call_BlinkXP_1299
    mee "¡Eres una jodida monja! ¡No deberías poder hacer eso!"
    call KissXP ("c15s005_385" , "d") from _call_KissXP_36
    nor "No le hagas ni caso. Yo también me apunto."
    mee "Pero... pero..."
    call KissXP ("c15s005_390" , "d") from _call_KissXP_37
    mom "Y yo."
    mee "¿Vais a parar de una vez con las tonterías?"
    call BlinkXP ("c15s005_395" , "d") from _call_BlinkXP_1300
    bet "¿Ya estás contenta? ¿No eres capaz de ver que cada vez que te pones cabezona acabas perdiendo? Acuérdate de la conversación de la desnudez."
    bet "Cuando esta familia se une no hay nada que no podamos conseguir, y sacarte de quicio es una de las cosas que a mí, personalmente, me encanta hacer."
    call BlinkXP ("c15s005_400" , "d") from _call_BlinkXP_1301
    "En ese momento aparece [eil] en la cocina."
    eil "Ya he hablado con Alexia para esta tarde. Nos podemos ir cuando queráis..."
    call BlinkXP ("c15s005_405" , "d") from _call_BlinkXP_1302
    eil "¿Pasa algo, Olivia? Pareces enfadada... ¿No te apetece venir de compras?"
    call BlinkXP ("c15s005_410" , "d") from _call_BlinkXP_1303
    bet "Lo que le pasa es que tiene mal perder. *Risa*"
    mc "No hurgues en la herida, Tía Betty..."
    call BlinkXP ("c15s005_415" , "d") from _call_BlinkXP_1304
    mee "Lo que me pasa es que mi familia se ha vuelto loca... han decidido saludar a [mc] con un beso en la boca."
    call KissXP ("c15s005_420" , "d") from _call_KissXP_38
    eil "Genial, me apunto... pero es nuestra familia."
    return
label c15s005_kisses2:
    call BlinkXP ("c15s005_445" , "d") from _call_BlinkXP_1305
    bet "Ahora solo faltan Kiara y mi hermana..."
    call BlinkXP ("c15s005_450" , "d") from _call_BlinkXP_1306
    eil "¿Mi madre? Realmente habéis perdido el juicio... *Risa*"
    call BlinkXP ("c15s005_455" , "d") from _call_BlinkXP_1307
    bet "Pertenece a la familia, igual que tu o yo. Si quiere hacerlo puede, pero nadie la va a obligar."
    call BlinkXP ("c15s005_460" , "d") from _call_BlinkXP_1308
    eil "Os conocéis poco todavía, Betty. *Risa* Mi madre nunca se atrevería a..."
    call BlinkXP ("c15s005_465" , "d") from _call_BlinkXP_1309
    kia "¿Puedo?"
    mc "Sólo si quieres. Como ha dicho Betty, no tienes ninguna obligación."
    scene c15s005_470An with dissolve
    "El beso dura más que un simple saludo. Donde tú esperabas un beso tímido, por compromiso, te encuentras con un beso agresivo. Sin pasión, pero agresivo. Tan solo labios presionados con fuerza."
    "Kiara tan solo le está demostrando a su hija que está equivocada."
    call BlinkXP ("c15s005_470" , "d") from _call_BlinkXP_1310
    kia "¡Nadie llama cobarde ni loca a Kiara Lamb!"
    call BlinkXP ("c15s005_475" , "d") from _call_BlinkXP_1311
    eil "¡Mamá! No me refería a eso."
    call BlinkXP ("c15s005_480" , "d") from _call_BlinkXP_1312
    kia "Lo sé, pero has dicho que no me atrevería... Y sabes que la mejor forma de meter 300 irlandeses en un coche es decirles que no caben."
    return
label c15s005_kisses3:
    call BlinkXP ("c15s005_490" , "d") from _call_BlinkXP_1313
    bet "Olivia, tu nieto se va. ¿No vas a despedirte? Nosotras nos vamos con [eil] y no lo vas a ver hasta la noche..."
    call BlinkXP ("c15s005_495" , "d") from _call_BlinkXP_1314
    mee "Me puede dar un beso en la mejilla como ha hecho siempre..."
    mc "O puedo decirte un simple \"Hasta luego\", Meemaw."
    mee "*Grrrr* Adiós, [mc]."
    call BlinkXP ("c15s005_500" , "d") from _call_BlinkXP_1315
    bet "*Risa* ¿Sabes que estás monísima cuando te enfadas? Eres como un Minioff al que le han quitado su banana. *Risa*"
    bet "¿Vas a ser la única que no lo despida con un beso en toda la familia? Después dices que es tu favorito..."
    call KissXP ("c15s005_505" , "h") from _call_KissXP_39
    "Olivia se levanta y te da un beso rápido. Sabe que ha perdido la batalla, pero se niega a creer que haya perdido la guerra."
    mee "Ya está. ¿Estás contenta?"
    mc "No sé ella, pero yo sí."
    call BlinkXP ("c15s005_510" , "d") from _call_BlinkXP_1316
    bet "Sí, estoy contenta. Bienvenida de nuevo a la familia, hermanita."
    call BlinkXP ("c15s005_515" , "d") from _call_BlinkXP_1317
    mee "¿Hermanita? ¡Soy la mayor!"
    call BlinkXP ("c15s005_520" , "d") from _call_BlinkXP_1318
    bet "Pues empieza a comportarte como tal."
    return
label c15s006_AaronVisit:
    if _in_replay:
        call mrS3_dap_route from _call_mrS3_dap_route_26
        call mrS3_sca_route from _call_mrS3_sca_route_21
        call mrS3_oma_route from _call_mrS3_oma_route_13
        call mrS3_mar_route from _call_mrS3_mar_route_30
        call mrS3_nor_route from _call_mrS3_nor_route_22
        call mrS3_emm_route from _call_mrS3_emm_route_33
        call mrS3_eri_route from _call_mrS3_eri_route_26
        call mrS3_eil_route from _call_mrS3_eil_route_19
        call mrS3_sam_route from _call_mrS3_sam_route_17
        call mrS3_sim_route from _call_mrS3_sim_route_18
        call mrS3_sai_route from _call_mrS3_sai_route_15
        call mrS3_edmund_story from _call_mrS3_edmund_story_8
    scene c15s006_005 with dissolve
    play music ("music/EpicFemaleSolo.ogg")
    "Cuando estás volviendo a casa de [nor], unos minutos antes de las 5:00 PM, un elegante coche para delante de la puerta."
    call BlinkXP ("c15s006_010" , "d") from _call_BlinkXP_1319
    ama "Buenas tardes, [mc]. ¿Podemos meter el coche en el garaje de tu casa? Está vacío..."
    mc "Sí, os abro la cancela y el garaje."
    mcp "(No me acostumbro a que sepan todo lo que pasa en la casa)"
    if mar._var("route") or nor._var("route") or emm._var("route") or eri._var("route") or dap._var("route") or sca._var("route") or oma._var("route") or sai._var("route"):
        mcp "(Todo...)"
    scene c15s006_015a with fade
    mc "Buenas tardes, Amanda, Eva."
    mc "Aaron, supongo."
    mcp "(Esperaba que fuera mucho más joven. Supongo que hay dos Aaron en NTR-GILF. Diferentes personas con el mismo nombre.)"
    eva "Buenas tardes, [mc]."
    ama "Aaron, [mc]. [mc], Aaron."
    python:
        if "aar" not in globals () or not isinstance (aar, TGCharacter):
            aar = TGCharacter ("Aaron", color = "#62b587", lname = "Gilford")
    aar "Encantado de conocerte, [mc]. Tenía muchas ganas de conocerte por fin."
    mc "Igualmente. Yo tenía ganas de que nos expliquéis que está pasando. Mi madre y mi tía nos están esperando."
    if not persistent.family:
        call BlinkXP ("c15s006_020" , "d") from _call_BlinkXP_1320
        aar "¿Su madre? ¿No lo sabe? Eso va a complicar mucho las explicaciones..."
        mc "¿Saber qué?"
        scene c15s006_025AnBlink with dissolve
        ama "Sí que lo sabe. Se comportan como si [mar] fuera su madre y [nor] su tía para guardar las apariencias de cara a las chicas y proteger sus identidades."
        mc "¡Ah! ¿Eso? Sí, soy consciente de que mi madre murió."
        call BlinkXP ("c15s006_030" , "d") from _call_BlinkXP_1321
        aar "Mis condolencias, aunque lleguen 16 años tarde. Era una gran mujer."
        mc "¿La conociste?"
        aar "Sí, la conocí brevemente."
    scene c15s006_015b with dissolve
    ama "¿Pasamos a la casa? [nor] y [mar] nos deben estar esperando..."
    mc "Nos están esperando en el salón de [nor]... pero supongo que ya lo sabéis..."
    scene c15s006_035a with fade
    if persistent.family:
        mc "[mar], [nor], estos son Amanda, Eva, y Aaron. [mar], mi madre, y [nor], mi tía."
    else:
        mc "[mar], [nor], estos son Amanda, Eva, y Aaron. [mar] y [nor]."
    mom "¡Oh, Dios mío!" (multiple=2)
    nor "Son casi iguales..." (multiple=2)
    scene c15s006_035b
    mom "¿Sí?" (multiple=2)
    nor "¡Sí!" (multiple=2)
    scene c15s006_035c with hpunch
    mom "¡Bienvenidas!" (multiple=2)
    nor "¡Sentíos como en casa!" (multiple=2)
    ama "*Suspiro* Gracias, [mar]." (multiple=2)
    eva "*Jadeo* Gracias... supongo..." (multiple=2)
    scene c15s006_035d with dissolve
    mom "Te queda genial el rubio, Amanda... aunque no le digas a [emm] que te lo he dicho..."
    ama "Gracias, [mar]. Es un cambio que he hecho hace poco tiempo. Y no te preocupes, no creo que tenga oportunidad de decírselo."
    scene c15s006_035e with dissolve
    nor "Te miro a los ojos y no puedo dejar de ver a mis niñas, pero está claro que nadie os podría confundir."
    scene c15s006_035An2 with dissolve
    eva "No, seguramente solo un tonto nos confundiría..."
    mcp "(Mierda, la [eri] de los tatuajes que se corrían... ¡El tonto soy yo!)"
    call BlinkXP ("c15s006_040" , "d") from _call_BlinkXP_1322
    mc "Aaron, ¿quieres sentarte? Dejemos un poco de tiempo para que se acostumbren. Mi madre y mi tía, me refiero."
    aar "Sí, será mejor que nos sentemos y les demos un poco de espacio, aunque tenemos un tiempo limitado y os tengo que explicar muchas cosas."
    mc "¿Quieres beber algo? ¿Café, una copa de algo?"
    aar "Un vaso de agua, por favor. Voy a tener que hablar mucho."
    mc "Ahora vuelvo."
    call BlinkXP ("c15s006_045" , "f") from _call_BlinkXP_1323
    mc "Una pregunta, Aaron. ¿Nos hemos visto? Tu cara me resulta familiar. ¿Viniste a casa alguna vez antes del accidente, cuando yo era niño?"
    aar "No, tú y yo no nos hemos visto nunca en persona, pero mejor os explico todo cuando las chicas hayan acabado con las presentaciones."
    mc "¿Qué me puedes contar de ellas? ¿De Amanda y Eva?"
    call BlinkXP ("c15s006_050" , "d") from _call_BlinkXP_1324
    aar "Aparte de que son unas de las mejores agentes con las que he trabajado nunca, no creo que pueda contarte demasiado. O al menos no demasiado que te interese."
    mc "Eso ya lo veremos..."
    scene c15s006_035g with dissolve
    eva "Creo que la reunión debe empezar ya... *Mascullando* Yo puedo aguantar un número de abrazos limitado."
    ama "Sí, empecemos ya o no va a dar tiempo de explicároslo todo."
    mc "¿Os sentáis?"
    eva "Yo prefiero continuar de pie... para... para poder contrarrestar cualquier amenaza..."
    scene c15s006_035h with dissolve
    nor "Siéntate al lado de Amanda, Eva, por favor. Yo me sentaré a tu lado."
    eva "Mmmm... OK."
    call BlinkXP ("c15s006_055" , "f") from _call_BlinkXP_1325
    mc "Explícanos, Aaron. ¿Qué es tan importante?"
    aar "¿Qué sabéis de NTR y de GILF?"
    if persistent.family:
        mc "Que fue fundada por mis tíos y que ahora, debido a un extraño testamento, somos prácticamente los dueños."
    else:
        mc "Que fue fundada por mi madre, mi tío y por Dominic Andersen. Y que ahora, debido a un extraño testamento, somos prácticamente los dueños."
    aar "Exacto. Prácticamente. Vuestra familia tiene el 75\% del accionariado. La mía el 25\% restante."
    call BlinkXP ("c15s006_060" , "d") from _call_BlinkXP_1326
    nor "¿La tuya?"
    mc "¿Nos puedes explicar eso? Por lo que sé el 25\% restante lo heredaban la Serie XY-A y la Serie XX a partes iguales."
    mc "Hemos descubierto que Eva y Amanda son XX. Pero tú no puedes ser Serie A."
    call BlinkXP ("c15s006_065" , "d") from _call_BlinkXP_1327
    ama "Quizás sería bueno que empezases por el principio, Aaron."
    menu:
        "Escuchar la historia.":
            call c15s006_Story from _call_c15s006_Story
        "No me interesa la historia. ([mc] sabrá la historia igualmente)":
            pass
    call BlinkXP ("c15s006_240" , "d") from _call_BlinkXP_1328
    mc "Es decir, somos los dueños de una empresa millonaria que se dedica a trabajar como mercenarios."
    aar "Sí, esa es la actividad económica principal. La secundaria es la investigación y diseño de dispositivos de medicina avanzada."
    mc "Vale, ¿y ahora qué?"
    call BlinkXP ("c15s006_245" , "d") from _call_BlinkXP_1329
    aar "Ahora tenéis que tomar una decisión sobre qué queréis hacer con la empresa. Podéis venderla, mantenerla o cambiarla."
    aar "No hace falta que toméis la decisión ahora. Antes deberíais decirle la verdad a [emm], [dap] y [eri]. Ellas también tienen voto. Igual que nosotros."
    if mc._var("edmundsStory"):
        mc "¿Y mi padre?"
        call BlinkXP ("c15s006_250" , "d") from _call_BlinkXP_1330
        aar "¿Tu padre? ¿Qué tiene que ver Edmund en todo esto?"
        mc "Le perseguíais... o le perseguían... aquí en Newport. Cuando se fugó también le persiguieron..."
        call BlinkXP ("c15s006_255" , "d") from _call_BlinkXP_1331
        mom "¿Qué? ¿Has estado en contacto con tu padre? ¿Has hablado con él?"
        mc "Sí, Mamá. Te lo explico luego."
        call BlinkXP ("c15s006_260" , "d") from _call_BlinkXP_1332
        aar "Tu padre no ha sido un objetivo nunca. No soy consciente de que nadie le haya seguido a ningún sitio o de que le estén vigilando."
        mc "Vuestros Serie G le siguieron hasta Aruba..."
        call BlinkXP ("c15s006_265" , "d") from _call_BlinkXP_1333
        aar "¿Aruba? *Risa* ¿Tu padre se fugó a Aruba?"
        mc "Sí... no entiendo qué tiene de gracioso..."
        call BlinkXP ("c15s006_265b" , "d") from _call_BlinkXP_1334
        aar "¿Te acuerdas que te he dicho que NTR compró laboratorios en el extranjero? El laboratorio principal está en Aruba."
        aar "Nadie le vigilaba y nadie le siguió... *Risa* Fue él quien se metió en la boca del lobo..."
    aar "Si decidís mantener la empresa, uno de vosotros debería venir a Aruba con nosotros en unas semanas, una vez se calmen las aguas."
    mc "¿Para qué?"
    call BlinkXP ("c15s006_270" , "d") from _call_BlinkXP_1335
    aar "Ahora mismo la empresa está sin liderazgo. Con Xabier apartado de su puesto, GILF desaparecerá y todo el personal será absorbido por NTR."
    aar "Alguien debe dirigir ese cambio y decidir el rumbo que queréis... queremos darle a la empresa, sea para mantenerlo o cambiarlo."
    mc "Ninguno de nosotros sabe nada de operaciones encubiertas, clonación, o medicina..."
    call BlinkXP ("c15s006_275" , "d") from _call_BlinkXP_1336
    nor "Pero tú sabes cómo dirigir una empresa. Es lo que has estudiado."
    mc "Tú también... y yo solo he estudiado. No tendría ni idea de por dónde empezar..."
    nor "Yo sufro para administrar el Dormitorio... estoy demasiado oxidada..."
    call BlinkXP ("c15s006_280" , "d") from _call_BlinkXP_1337
    aar "Yo podría ayudarte en eso... si quieres."
    mc "¿Y por qué no la diriges tú? También eres accionista..."
    aar "Hay demasiada mala sangre ahora mismo como para que yo tome el poder. Además, tu familia tiene la mayoría de las acciones..."
    aar "Puedo dirigir el proceso de transición, pero no puedo hacerme cargo de la empresa."
    mc "¿Y Amanda y Eva?"
    call BlinkXP ("c15s006_285" , "d") from _call_BlinkXP_1338
    ama "Si tú no sabes por dónde empezar, imagínate nosotras... y estamos en la misma posición que Aaron. Hay gente que no lo aceptaría. Volveremos a la base hoy con Aaron para allanarte el camino."
    ama "Además, sólo serían unos meses. Una vez toméis la decisión sobre qué hacer con la empresa, una vez aprendas en quién puedes delegar, podrás dirigirlo todo desde aquí."
    mc "¿Meses? ¡No puedo irme meses!"
    call BlinkXP ("c15s006_290" , "d") from _call_BlinkXP_1339
    eva "¿No te puedes separar de tu familia? Si decidís mantener la empresa y no venderla, sabes que es lo mejor."
    eva "Ayer se te llenaba la boca con la palabra familia. Hoy parece que no estás dispuesto a sacrificar unos meses por su bien."
    mc "Espera... ¿tenemos la oportunidad de venderla? ¿Hay compradores? ¿Qué valor tiene?"
    call BlinkXP ("c15s006_295" , "d") from _call_BlinkXP_1340
    aar "No hemos calculado el valor todavía. Pero bastante. Seguramente diez u once cifras. No creíamos que quisierais poner en venta la empresa familiar."
    mc "¡Wow! Es para pensarlo..."
    call BlinkXP ("c15s006_295b" , "d") from _call_BlinkXP_1341
    aar "Es posible que en las próximas semanas os hagan alguna oferta. Va a ser difícil que vuestra identidad no se filtre en algunos círculos."
    aar "Si decidís venderla, nos gustaría pediros un favor. Dadnos la oportunidad de comprar vuestra parte."
    aar "O al menos lo suficiente para tener el control de la empresa. No queremos que caiga en manos equivocadas."
    call BlinkXP ("c15s006_300" , "d") from _call_BlinkXP_1342
    nor "De momento me parecería buena idea no venderla hasta no saber más, y si decidimos hacerlo, creo que os debemos el derecho de tanteo."
    "En ese momento te das cuenta de que [nor] y [mar] han estado usando sus teléfonos los últimos minutos. Estabas demasiado concentrado en la conversación para notarlo."
    nor "Pero nosotras también queremos algo a cambio. Al menos hasta que [mc] decida si va a Aruba en unas semanas."
    call BlinkXP ("c15s006_305" , "d") from _call_BlinkXP_1343
    mom "Queremos que Amanda y Eva se queden en Newport durante ese tiempo."
    "Y ahora entiendes qué hacían con los teléfonos. Estaban creando su propia estrategia de negociación."
    scene c15s006_310d with dissolve
    ama "¡Sí!... Digo... ¿Qué?" (multiple=2)
    eva "¿Por qué nosotras?" (multiple=2)
    call BlinkXP ("c15s006_310" , "d") from _call_BlinkXP_1344
    aar "Eso no va a ser posible..."
    call BlinkXP ("c15s006_315" , "d") from _call_BlinkXP_1345
    mom "Aaron, déjame hablar."
    mom "Queremos que se queden por varias razones. La primera es que queremos conocerlas mejor."
    scene c15s006_315An with dissolve
    mom "También queremos que conozcan a las chicas. Creemos que las cinco tienen el derecho a conocerse."
    call BlinkXP ("c15s006_320" , "d") from _call_BlinkXP_1346
    nor "Habrá que dar muchas explicaciones... pero..."
    nor "Queremos que pasen tiempo en casa una vez se lo hayamos contado a las chicas. Una comida o una cena cada día. Se pueden turnar."
    nor "Obviamente, solo si ellas quieren. Así podrán conocer a toda la familia."
    scene c15s006_320AnBlink with dissolve
    nor "Nos habéis dicho que hay agentes a los que todavía no les habéis cancelado las órdenes, y no creemos que haya nadie mejor para protegernos."
    call BlinkXP ("c15s006_310" , "d") from _call_BlinkXP_1347
    aar "Eso va a ser muy complicado, no podemos..."
    mc "Creo que tienes la batalla perdida, Aaron."
    mc "Yo también tengo un par de condiciones si queréis el derecho a tanteo. Serían tres, pero con una se me han adelantado."
    call BlinkXP ("c15s006_325" , "d") from _call_BlinkXP_1348
    ama "¿Qué condiciones, [mc]?"
    mc "Quiero que me enseñéis a disparar. No quiero volver a sentirme tan indefenso como me sentí con Eric el otro día."
    mc "Y quiero que me enseñen Eva y Amanda, con lo que la condición de que se queden es indispensable."
    call BlinkXP ("c15s006_330" , "d") from _call_BlinkXP_1349
    eva "¡De eso me ocupo yo!... Si no le importa a Amanda..."
    mc "Y quiero que retiréis las cámaras de los espacios privados de la casa. Habitaciones, baños..."
    scene c15s006_195a with hpunch
    mom "¿De qué estás hablando?" (multiple=2)
    nor "¿Nos han grabado en las habitaciones?" (multiple=2)
    mc "Sí, y eso se acaba hoy."
    call BlinkXP ("c15s006_335" , "d") from _call_BlinkXP_1350
    ama "Eso va a hacer más complicado protegeros. Si se infiltra alguien y no sabemos dónde está..."
    mc "Podéis revisar los pasillos y las zonas comunes. Pero se acabó grabarnos... durmiendo o duchándonos."
    call BlinkXP ("c15s006_340" , "d") from _call_BlinkXP_1351
    eva "Vale... no me gusta la idea, pero lo entiendo..."
    mc "Perfecto. ¿Mañana empezamos las lecciones sobre armas de fuego?"
    scene c15s006_345a with vpunch
    eva "¡Sí!"
    call BlinkXP ("c15s006_350" , "d") from _call_BlinkXP_1352
    eva "Digo... sí. Ya que es tu condición, podemos hacerlo a mediodía si te va bien. En el lago."
    mc "Genial. Entonces todo está aclarado."
    call BlinkXP ("c15s006_355" , "d") from _call_BlinkXP_1353
    aar "Nosotros nos vamos a tener que ir ya. Nuestro... mi vuelo sale en menos de dos horas."
    $ KnownToAmandaEva = 0 #RIAM, don't track this one
    if mar._var("route"):
        $ KnownToAmandaEva = KnownToAmandaEva + 1
    if nor._var("route"):
        $ KnownToAmandaEva = KnownToAmandaEva + 1
    if emm._var("route"):
        $ KnownToAmandaEva = KnownToAmandaEva + 1
    if dap._var("route"):
        $ KnownToAmandaEva = KnownToAmandaEva + 1
    if eri._var("route"):
        $ KnownToAmandaEva = KnownToAmandaEva + 1
    if sca._var("route"):
        $ KnownToAmandaEva = KnownToAmandaEva + 1
    if sam._var("route"):
        $ KnownToAmandaEva = KnownToAmandaEva + 1
    if sim._var("route"):
        $ KnownToAmandaEva = KnownToAmandaEva + 1
    if eil._var("route"):
        $ KnownToAmandaEva = KnownToAmandaEva + 1
    if oma._var("route"):
        $ KnownToAmandaEva = KnownToAmandaEva + 1
    if sai._var("route"):
        $ KnownToAmandaEva = KnownToAmandaEva + 1
    if KnownToAmandaEva > 0:
        call BlinkXP ("c15s006_360" , "h") from _call_BlinkXP_1354
        eva "¡Mierda! ¡Me he dejado la caja en el coche!"
        mc "¿Qué caja?"
        eva "Dame las llaves del garaje y ahora la traigo... que te lo vaya explicando Aaron..."
        mc "Tranquila, cuando os acompañe al coche la cogeré yo. ¿Qué es?"
        call BlinkXP ("c15s006_365" , "d") from _call_BlinkXP_1355
        aar "Es uno de los últimos productos de NTR. Un test de embarazo rápido. Todavía no está aprobado por la FDA, pero las chicas me pidieron que trajera una caja."
        mc "¿Rápido? ¿15 segundos? Los normales tardan cinco minutos..."
        aar "No me refiero a eso. Es un test que se puede hacer 48 horas después de tener relaciones. Solo necesita una gota de sangre y en 24 horas el resultado es 99.9\% preciso."
        if mar._var("route") and nor._var("route"):
            scene c15s006_370a with dissolve
            pause (1.5)
        elif mar._var("route"):
            scene c15s006_370b with dissolve
            pause (1.5)
        elif nor._var("route"):
            scene c15s006_370c with dissolve
            pause (1.5)
        call BlinkXP ("c15s006_365" , "d") from _call_BlinkXP_1356
        aar "Las chicas me dijeron que tú sabrías qué hacer con los tests... hay 50. Espero que sean suficientes."
    call BlinkXP ("c15s006_375" , "d") from _call_BlinkXP_1357
    aar "Bueno, creo que con esto acaba esta reunión. Nos veremos en unas semanas, espero, si no tengo que volver antes."
    mc "Encantado de haberte conocido, Aaron."
    scene c15s006_380a with dissolve
    nor "Me ha gustado mucho conocerte, Eva. ¿Por qué no vienes a comer mañana después de las lecciones con [mc]?"
    nor "Mientras estáis fuera, les contaremos la verdad a las chicas y al resto de la familia."
    eva "Si no hay más remedio... es una de las condiciones que habéis puesto."
    scene c15s006_380b with dissolve
    nor "Sólo si quieres. No quiero que te sientas obligada."
    eva "No, no... lo habéis pedido y vendré, no es justo que os echéis atrás ahora. Cuenta conmigo para comer. Por la tarde retiraré las cámaras de las habitaciones."
    scene c15s006_380c with dissolve
    mom "Eso te deja a ti para cenar, Amanda. ¿Te apetece?"
    ama "Me muero de ganas."
    scene c15s006_380d with dissolve
    mom "[emm] te va a caer muy bien, estoy segura."
    ama "Lo sé. Tengo experiencia tratando con... alguien parecido. *Risita*"
    call BlinkXP ("c15s006_385" , "d") from _call_BlinkXP_1358
    aar "*Susurrando* Me gustaría tener una conversación privada contigo en unos días. ¿Puedo llamarte?"
    mc "Por supuesto. ¿Sobre qué?"
    aar "*Susurrando* Entre otras cosas, sobre dónde me has visto con anterioridad. Recuerda que éramos tres. Pero ahora no es el momento."
    scene c15s006_380e with dissolve
    mom "Eva, estoy deseando que vengas a comer mañana y tener más tiempo para conocernos, si las chicas te dejan un minuto."
    eva "Seguro que sí... no suelo ser muy sociable... y se van a aburrir de mí enseguida."
    mom "*Risa* Lo dudo, pero ya lo veremos mañana."
    scene c15s006_380f with dissolve
    nor "Gracias por lo del otro día, Amanda. Tengo muchas ganas de conocerte mejor."
    ama "Yo también... a todas. Observándoos a distancia parecéis una familia... muy interesante."
    nor "No sé lo que habrás visto... quizás sí que somos un poco diferentes de lo normal..."
    mc "¡Ejem! Creo que es momento de acabar con los abrazos. El vuelo de Aaron no va a esperar."
    scene c15s006_380g with dissolve
    mc "¡Vale, vale! No hace falta que me miréis como si yo fuera el enemigo. Os vais a ver mañana..."
    mc "Os acompaño al coche."
    scene c15s006_380h with fade
    "Después de despedirte de Aaron..."
    mc "Bueno, chicas, nos veremos mañana. Eva, a mediodía en el lago, ¿OK?"
    call BlinkXP ("c15s006_390" , "h") from _call_BlinkXP_1359
    eva "Sí, a mediodía... y gracias..."
    mc "No sé por qué, pero no hay de qué..."
    eva "Por convencer a [mar] y [nor] de que nos aceptaran... ha sido intenso..."
    mc "Yo no..."
    call BlinkXP ("c15s006_395" , "d") from _call_BlinkXP_1360
    ama "No lo niegues, [mc]... ha quedado muy claro que lo de pedir que nos quedáramos lo teníais pactado."
    mc "Ha sido cosa de ellas, te aseguro que no he tenido nada que ver. No quiero un mérito que no es mío. Aunque yo también lo iba a pedir."
    mc "Pero me alegra que os hayáis sentido así."
    ama "A ver si Eva me deja despedirme."
    call BlinkXP ("c15s006_390b" , "d") from _call_BlinkXP_1361
    eva "Solo un minuto más..."
    aar "Chicas, el plan de vuelo..."
    eva "Vaaale..."
    call BlinkXP ("c15s006_400" , "d") from _call_BlinkXP_1362
    ama "Gracias, [mc]. Ha sido casi como sentirse parte de la familia por un momento."
    ama "Me costaba creerte ayer, cuando hablabas de la familia... pero después de esto... tengo muchas ganas de cenar mañana."
    mc "Me temo que se te pasarán en cuanto llegues. Ser el centro de atención puede ser complicado en esta familia. Ármate de paciencia."
    stop music fadeout (1.5)
    scene black with dissolve
    if KnownToAmandaEva > 0:
        "Tras la segunda queja de Aaron sobre el plan de vuelo, te entregan la caja y se marchan a regañadientes."
    else:
        "Tras la segunda queja de Aaron sobre el plan de vuelo, se marchan a regañadientes."
    scene c15s006_405a with dissolve
    play music ("music/UnforeseenMotive.ogg")
    mc "Ya se han ido. ¿Qué os ha parecido la reunión?"
    mom "Extraño... tener a una [emm] que no es nuestra [emm] delante, ha sido extraño... Si no fuera por el pelo..."
    nor "Eva me ha parecido... encantadora de una forma rara... al principio estaba distante, pero después... no sé... creo que al final no quería irse."
    mc "Ninguna de las dos quería irse. Ayer estuve hablando con las dos, en la playa..."
    scene c15s006_405b with dissolve
    mom "¿Estaban en la playa?" (multiple=2)
    nor "¿Por qué no les dijiste que se unieran?" (multiple=2)
    mc "Sólo Eva estaba en la playa, vigilándonos. Amanda estaba en su base."
    mc "Y decirles que se unieran podría haber sido complicado sin que nuestras chicas supieran de su existencia. Ni nuestras chicas ni el resto, claro."
    call BlinkXP ("c15s006_410" , "d") from _call_BlinkXP_1363
    nor "Tienes razón. Solo nosotros, Betty y tu abuela saben de su existencia. Demasiadas explicaciones."
    nor "Y esas explicaciones habrá que darlas mañana. Realmente me da miedo la reacción de las chicas..."
    mc "Aprovechad mientras Eva me enseña a disparar. Creo que es una cosa que cada una de vosotras tiene que hacer con sus hijas. Y no es que me esté escaqueando."
    call BlinkXP ("c15s006_415" , "d") from _call_BlinkXP_1364
    mom "Yo también lo creo. Prefiero explicárselo a [emm] a solas."
    mom "Pero ¿qué hacemos con el resto? Si [sca] o las estudiantes... o Kiara y [eil]... ven a Eva con [dap] y [eri], o a Amanda con [emm]..."
    mc "¡Uff! No había pensado en eso. Yo confío en que [eil] y [sai] podrán guardar el secreto..."
    call BlinkXP ("c15s006_420" , "d") from _call_BlinkXP_1365
    nor "Yo pondría la mano en el fuego por Kiara... Supongo que es mejor explicarles algo al resto de las estudiantes antes de que lo descubran ellas."
    nor "Podemos decir que son... unas primas que viven lejos..."
    mc "¿Más mentiras, [nor]? Creo que nadie de los que estuvieron ayer en la playa va a hacer nada que pueda perjudicar a las chicas... a ninguna de las cinco."
    call BlinkXP ("c15s006_425" , "d") from _call_BlinkXP_1366
    mom "Estoy de acuerdo contigo. Y eso incluye a [sam], [sim], Alexia... y también a Jamaal. Creo que no nos dejamos a nadie."
    if mar._var("route"):
        mc "Tan solo a [meg]... la invitaste a dormir en casa el fin de semana... va a ver a las chicas juntas."
    else:
        mc "Tan solo a [meg], una amiga... la invité a dormir en casa el fin de semana... va a ver a las chicas juntas."
    mom "¿Confías en ella?"
    mc "Sí. Además, también es amiga de [sai], con lo que es mejor que se lo cuente yo antes de que se entere por otros medios."
    mc "¡Joder! Tantos años guardando el secreto y ahora lo destapamos a lo grande..."
    mc "Un tema aclarado. ¿Qué opináis del tema de la empresa? ¿Qué hacemos?"
    call BlinkXP ("c15s006_430" , "d") from _call_BlinkXP_1367
    nor "Mientras despedías a Eva y a Amanda, hemos decidido que primero hay que explicárselo a nuestras chicas. Ellas también tienen que decidir."
    nor "La empresa es tan suya como nuestra, o de Aaron, Eva y Amanda, y a lo mejor tienen ideas diferentes sobre qué hacer a las que podamos tener nosotras."
    mc "Me parece lo más correcto."
    if mar._var("route"):
        call BlinkXP ("c15s006_435" , "d") from _call_BlinkXP_1368
        mom "Cambiando de tema... ¿Qué has hecho con la caja? ¿La de los tests?"
    elif nor._var("route"):
        call BlinkXP ("c15s006_440" , "d") from _call_BlinkXP_1369
        nor "Cambiando de tema... ¿Qué has hecho con la caja? ¿La de los tests?"
    if mar._var("route") or nor._var("route"):
        mc "La he dejado en el recibidor."
    if mar._var("route") and nor._var("route"):
        scene c15s006_445An
    elif mar._var("route"):
        scene c15s006_445An2
    elif nor._var("route"):
        scene c15s006_445An3
    if mar._var("route") or nor._var("route"):
        mcp "(No creo que venga de un minuto. Hay que esperar 24 horas para saber los resultados. *Risa mental*)"
    scene black with dissolve
    if mar._var("route") and nor._var("route"):
        "Hacéis las pruebas de embarazo. Son tan sencillas como poner una gota de sangre en una tira de plástico y ponerla dentro de una pequeña máquina."
        "Etiquetáis las pruebas con el nombre de [nor] y [mar] y las guardáis en lugar seguro, en la habitación de [nor]."
    elif mar._var("route") or nor._var("route"):
        "Hacéis la prueba de embarazo. Es tan sencilla como poner una gota de sangre en una tira de plástico y ponerla dentro de una pequeña máquina. La guardáis en lugar seguro."
    stop music fadeout (1.5)
    "Continuáis hablando sobre la reunión un rato, antes de que empiecen a volver las chicas que han ido a la ciudad."
    if KnownToAmandaEva > 0:
        if mar._var("route") or nor._var("route"):
            "Te llevas la caja con las otras 48 pruebas a tu habitación. Esperas tener suficientes para el resto de tu vida."
        else:
            "Te llevas la caja con las 50 pruebas de embarazo a tu habitación. Esperas tener suficientes para el resto de tu vida."
    return
label c15s006_Story:
    if persistent.family:
        scene c15s006_070a with dissolve
        aar "OK. Ya sabéis quién fundó NTR. Tenéis que entender que eran unos genios."
    else:
        scene c15s006_070b with dissolve
        aar "OK. Ya sabéis quién fundó NTR. Tienes que saber que tu madre era un genio, [mc]. Todos lo eran."
    aar "Empezaron estudiando árboles genealógicos basándose en el ADN. Pero hicieron un descubrimiento rompedor."
    aar "Ya se habían hecho clonaciones anteriormente de animales. Todos recordamos a Dolly."
    aar "Pero ellos descubrieron como hacer clonaciones aceleradas. De embrión a individuo viable en un tercio del tiempo de gestación."
    if persistent.family:
        aar "Daniel era la gran mente detrás de ello."
    else:
        aar "Anna era la gran mente detrás de ello."
    scene c15s006_070c with dissolve
    aar "Empezaron clonando animales... ovejas, cerdos..."
    aar "Pero Dominic convenció al resto para que probasen la clonación humana. Ahí es donde estaría el dinero de verdad. Imaginaros tener un clon humano en solo tres meses."
    aar "Obviamente en los Estados Unidos era ilegal, con lo que compraron laboratorios en un par de países donde la legislación era poco clara al respecto."
    aar "Después de varios experimentos en el extranjero consiguen la primera clonación más o menos correcta. La Serie A. Yo y mis dos hermanos. Alfred y Arnau."
    call BlinkXP ("c15s006_075" , "d") from _call_BlinkXP_1370
    mc "Espera... has dicho que eso pasó hace 20 o 21 años. ¿Cómo puedes ser tú?"
    aar "Porque yo tengo 21 años. No solo se triplicaba la velocidad de gestación. El envejecimiento no se paraba al \"nacer\"."
    aar "Además, el material genético inicial... Bueno, eso es para otro día... hoy no hay tiempo."
    mc "¡Joder! Entonces..."
    call BlinkXP ("c15s006_075b" , "d") from _call_BlinkXP_1371
    aar "Sí, mi cuerpo tiene más de 60. Pero no estamos aquí para hablar de mí."
    aar "Después llegó la Serie B. Brandon, Bryce, Brady, Benito, y Bart. Los chicos no salieron bien."
    aar "Intentaron controlar el envejecimiento una vez fuera de los tubos, pero no funcionó. El resultado fue inverso. A los 10 años estaban peor que yo ahora."
    call BlinkXP ("c15s006_080" , "d") from _call_BlinkXP_1372
    if persistent.family:
        aar "Para la tercera serie, Daniel decidió probar otra cosa. Clonar chicas introduciendo algunos cambios."
        mc "Y aparecen Amanda y Eva, ¿no?"
        aar "Exacto."
        call BlinkXP ("c15s006_085" , "d") from _call_BlinkXP_1373
        eva "También Beatrice, Claire, y Diana... y Fiona..."
        scene c15s006_090a with dissolve
        nor "Pero ¿De dónde sacaron el material?"
        mom "Nunca perdí a [emm] de vista. Nunca se quedó sola cuando íbamos al médico."
        call BlinkXP ("c15s006_095" , "d") from _call_BlinkXP_1374
        aar "Estabais embarazadas a la vez. A Daniel se le ocurrió la idea de extraer células de los fetos."
        aar "En algún momento os debieron llevar engañadas a las instalaciones de NTR a haceros algunas pruebas y aprovecharon para extraer el material genético."
        call BlinkXP ("c15s006_100" , "d") from _call_BlinkXP_1375
        mom "¿Sin nuestro consentimiento? ¿Cómo pudieron hacernos eso?"
        call BlinkXP ("c15s006_105" , "d") from _call_BlinkXP_1376
        nor "¡Qué hijos de puta! ¿Cómo pudo Mike aceptar hacer eso con sus propias hijas?"
        scene c15s006_110a with dissolve
        mom "No te lo tomes mal, cielo... esto es nuevo para nosotras... me alegra que estéis aquí ahora."
        ama "Gracias, [mar]..."
        scene c15s006_110b with dissolve
        nor "Sí, vosotras no tenéis la culpa... pero si Mike no estuviera muerto... lo volvería a matar yo ahora mismo."
        eva "Me gusta como piensas. Yo seguramente haría lo mismo."
        call BlinkXP ("c15s006_115" , "d") from _call_BlinkXP_1377
        aar "El experimento XX fue todo un éxito como podéis ver. Solucionaron el problema de los telómeros cortos y..."
        mc "¿Telo-qué?"
        aar "Telómeros. Es lo que produce el envejecimiento acelerado. Como podéis ver, Eva y Amanda no parecen mayores que [emm], [eri], o [dap]."
        mc "Ah, OK."
        mcp "(Necesitaríamos que [dap] estuviera aquí para que nos tradujese la jerga científica.)"
        mc "Pero habéis nombrado a seis chicas, y solo había dos embarazos... o tres si contáis que [nor] tenía gemelas... ¿Quiénes eran las otras...? ¿Donantes?"
        call BlinkXP ("c15s006_120" , "d") from _call_BlinkXP_1378
        ama "No había más donantes. Los sujetos A, B, y C, Beatrice, Claire y yo, nacimos de material genético de [emm]. D, E, y F, Diana, Eva, y Fiona, del de [dap] o [eri]."
        mc "Ah, vale... tres clones por cada chica."
        call BlinkXP ("c15s006_125" , "d") from _call_BlinkXP_1379
        eva "Sí. La idea era que sirviéramos como \"material de repuesto\" por si alguna vez necesitaban un trasplante."
        mc "¡Pero eso es inhumano! ¡Sois personas! No podían pensar en sacrificaros si [dap] hubiera necesitado... yo que sé... un pulmón..."
        eva "Sí, lo es. Y sí, lo pensaban hacer. A ellos les daba lo mismo en ese momento. Solo éramos experimentos."
        call BlinkXP ("c15s006_130" , "d") from _call_BlinkXP_1380
        aar "Y ahí es cuando empezó a torcerse la cosa. Si puedes crear clones y usarlos como repositorio de órganos de cara al futuro..."
        mc "Los billonarios se volverían locos por tener eso para sus hijos."
        aar "Exacto. Mis chicas nacieron antes que las vuestras. Y se comprobó que el envejecimiento no continuaba una vez fuera del tanque."
    else:
        aar "Para la tercera serie, Anna decidió probar otra cosa. Clonar chicas introduciendo algunos cambios."
        mc "Y aparecen [emm], [eri] y [dap], ¿no?"
        aar "Exacto."
        scene c15s006_090a with dissolve
        nor "Pero ¿De dónde sacaron el material genético?"
        mom "Mike y Dominic nunca nos lo contaron."
        call BlinkXP ("c15s006_095" , "d") from _call_BlinkXP_1381
        aar "Se pagó a mujeres embarazadas que querían dar sus bebés en adopción. NTR los adoptaría a cambio de hacer unas pruebas con los fetos."
        aar "En total había seis chicas."
        mc "Amanda, Eva, y ¿quién más?"
        call BlinkXP ("c15s006_085" , "d") from _call_BlinkXP_1382
        eva "También Beatrice, Claire, y Diana... y Fiona... Ninguna de ellas está entre nosotras a día de hoy."
        mc "Lo siento..."
        call BlinkXP ("c15s006_115" , "d") from _call_BlinkXP_1383
        aar "El experimento XX fue todo un éxito como podéis ver. Solucionaron el problema de los telómeros cortos y..."
        mc "¿Telo-qué?"
        aar "Telómeros. Es lo que produce el envejecimiento acelerado. Como podéis ver, [emm], [eri], o [dap] no parecen mayores que Eva y Amanda."
        mc "Ah, OK."
        mcp "(Necesitaríamos que [dap] estuviera aquí para que nos tradujese la jerga científica.)"
        mc "Pero habéis nombrado a seis chicas, y solo acaba por haber tres clones... o dos si contamos a [eri] y [dap] como uno."
        scene c15s006_110c with dissolve
        ama "Los clones de Beatrice, Claire, Diana, y Fiona no fueron viables. Dos no llegaron a nacer y otros dos murieron a los pocos días."
        mom "Eso es muy triste..."
        call BlinkXP ("c15s006_105" , "d") from _call_BlinkXP_1384
        nor "¡Qué hijos de puta! ¿Cómo pudo Mike experimentar así con niñas pequeñas?"
        scene c15s006_110a with dissolve
        mom "No te lo tomes mal, cielo... esto es nuevo para nosotras... me alegra que estés aquí ahora."
        ama "Gracias, [mar]..."
        scene c15s006_110b with dissolve
        nor "Sí, vosotras no tenéis la culpa... pero si Mike no estuviera muerto... lo volvería a matar yo ahora mismo."
        eva "Me gusta como piensas. Yo seguramente haría lo mismo."
        call BlinkXP ("c15s006_130" , "d") from _call_BlinkXP_1385
        aar "Y ahí es cuando empezó a torcerse la cosa. Si puedes crear clones que envejezcan a la vez que sus donantes y usarlos como repositorio de órganos de cara al futuro..."
        mc "Los billonarios se volverían locos por tener eso para sus hijos."
        aar "Exacto. Cuando vuestras chicas nacieron, se comprobó que el envejecimiento no continuaba una vez fuera del tanque."
    aar "Dominic hizo contactos con un tipo muy rico. Había mucho dinero en juego."
    call BlinkXP ("c15s006_135" , "d") from _call_BlinkXP_1386
    aar "Y entoces, llegó el accidente de avión. Se sospechó de un sabotaje, pero no se pudo probar nada."
    aar "Después de la reestructuración de NTR y GILF, se intentó llevar a cabo la primera clonación del hijo de un millonario."
    call BlinkXP ("c15s006_140" , "d") from _call_BlinkXP_1387
    aar "No funcionó. Creemos que una parte fundamental del trabajo en parar el envejecimiento estaba en alguno de los portátiles que se destruyeron en el accidente."
    aar "Faltaban datos en los servidores de NTR. Se redujo el ratio de envejecimiento. Primero a 2.8, 2.5, 2... pero nunca han conseguido que sea inferior a 1.7."
    mc "¿Qué pasó con esos clones fallidos?"
    call BlinkXP ("c15s006_145" , "d") from _call_BlinkXP_1388
    aar "Si no puedes utilizarlos como repositorio de órganos para sus donantes millonarios, ¿qué puedes hacer con unos clones que a los 6 años tienen el cuerpo de alguien de 18?"
    aar "Con la capacidad de aprendizaje de un niño pequeño, pero con la fuerza y la agilidad de un adulto."
    mc "Un ejército de clones."
    call BlinkXP ("c15s006_150" , "d") from _call_BlinkXP_1389
    aar "Exacto. Los entrenas para realizar operaciones encubiertas y los alquilas al mejor postor."
    mc "No es justo. Seguían... seguíais siendo niños..."
    call BlinkXP ("c15s006_155" , "d") from _call_BlinkXP_1390
    ama "Si y no. Eric solo tiene 15 años aunque su cuerpo ronde los 30. Pero ya has visto como puede ser..."
    mc "Lo había leído, pero las edades reales y aparentes no encajaban."
    call BlinkXP ("c15s006_160" , "d") from _call_BlinkXP_1391
    eva "Y no le hubiera importado mataros si hubiera sido necesario, si no hubierais querido firmar... al menos a uno de vosotros, para forzar a los demás."
    mc "¿Iba en serio lo de matarnos?"
    call BlinkXP ("c15s006_165" , "d") from _call_BlinkXP_1392
    aar "Ya llegaremos al tema de los asesinatos más tarde..."
    mc "Pero..."
    aar "Mas tarde, [mc]."
    call BlinkXP ("c15s006_165b" , "d") from _call_BlinkXP_1393
    aar "En definitiva, en pocos años NTR y GILF tuvieron un pequeño ejército de clones entrenados. Cuando los A teníamos 8 años empezamos a hacer misiones."
    aar "Después se unieron los C, los D... Había gobiernos, como el vuestro, que pagaban muy bien por un equipo de mercenarios que no se pudiera relacionar con ellos."
    aar "Las chicas empezaron con sus misiones hace cuatro años, cuando cumplieron 14. Menos Fiona, que había muerto en un accidente durante el entrenamiento."
    scene c15s006_170a with dissolve
    mom "Lo siento mucho, Amanda... supongo que... debía ser como una hermana para vosotras."
    ama "No como una hermana... era una hermana de verdad..."
    scene c15s006_170b with dissolve
    nor "Debió de ser duro para vosotras."
    eva "Fue la primera en morir. Es un golpe duro cuando ves morir a tu hermana a los 12 años en una explosión."
    mc "¿12 años? ¡Joder! ¿Cuándo empezasteis a entrenar?"
    call BlinkXP ("c15s006_175" , "d") from _call_BlinkXP_1394
    aar "Las chicas empezaron a entrenar a los 6 años. Tenían el cuerpo de una niña de 6 años, pero cuando todo lo que haces es entrenar... te conviertes en bueno. Y ellas son muy buenas."
    mcp "(No puedo evitar imaginarme a [emm] o [dap] con una metralleta con 6 años. Es una imagen ridícula. No puedo imaginar por lo que han pasado Eva y Amanda.)"
    call BlinkXP ("c15s006_180" , "d") from _call_BlinkXP_1395
    aar "Con un suministro cada vez mayor de agentes, NTR creció mucho."
    aar "El director de GILF, Richard, sabía que eso podría funcionar por un tiempo limitado, conocía el testamento de los fundadores y sabía que heredaríais... heredaríamos la empresa."
    mc "Y no podía saber qué haríamos con ella o si estaríamos de acuerdo con la forma de operarla."
    call BlinkXP ("c15s006_185" , "d") from _call_BlinkXP_1396
    aar "Exacto. Pero Richard había sido amigo y compañero de los Fundadores desde el principio y estaba dispuesto a cumplir su última voluntad."
    aar "Pero Richard murió hace unos meses. Causas naturales. Su segundo, Xabier, tomó el mando y descubrió el testamento."
    mc "Y él no estaba dispuesto a cumplir con las condiciones."
    call BlinkXP ("c15s006_190" , "d") from _call_BlinkXP_1397
    aar "Exacto. Si moríais antes de que la última cláusula del testamento entrara en vigor, la propiedad de NTR pasaba definitivamente a GILF."
    aar "Se ordenó a la serie XX asesinaros. A todos."
    mc "{b}¿Qué?{/b} ¡Nos han estado defendiendo!"
    scene c15s006_195An
    mom "¿Nos iban a matar por una empresa?" (multiple=2)
    nor "¿Tan importante es?" (multiple=2)
    call BlinkXP ("c15s006_200" , "d") from _call_BlinkXP_1398
    eva "No seáis inocentes. La mayoría de los asesinatos tienen que ver con dinero o con poder. Y NTR vale MUCHO dinero, y los propietarios de NTR pueden tener MUCHO poder."
    eva "La orden de asesinato tenía una parte oculta. La que nos llegó a nosotras decía que cuando acabáramos con vosotros teníamos que matar también a los A."
    call BlinkXP ("c15s006_205" , "d") from _call_BlinkXP_1399
    ama "Erais unos civiles, con lo que no se dedicaron muchos recursos. Cinco agentes a la caza de seis civiles. Una misión fácil."
    call BlinkXP ("c15s006_210" , "d") from _call_BlinkXP_1400
    aar "Cuando las chicas recibieron las órdenes, vinieron a vernos a Arnau y a mí a explicarnos las órdenes que habían recibido respecto a nosotros."
    aar "Debía tratarse de un error. Arnau fue a hablar con Xabier para aclararlo y nunca volvió. Nosotros nos fuimos de la base. Pudimos huir por los pelos."
    mc "Y fue cuando decidisteis protegernos, ¿no?"
    call BlinkXP ("c15s006_215" , "d") from _call_BlinkXP_1401
    eva "Ya sabes... el enemigo de mi enemigo... Si os querían muertos sería por algo y nosotros aún no sabíamos por qué."
    call BlinkXP ("c15s006_220" , "d") from _call_BlinkXP_1402
    ama "Aaron y Claire investigaron y descubrieron la cláusula del testamento mientras Eva y yo protegíamos a la familia en Newport, y Beatrice y Diana te protegían a ti en Portland."
    ama "Como es normal en estos casos, la información fluía entre nosotros, con lo que, cuando llegaste a Newport, sabíamos mucho de ti."
    call BlinkXP ("c15s006_225" , "d") from _call_BlinkXP_1403
    aar "Decidimos que, si queríamos sobrevivir, erais nuestra mejor opción. Además, lo que hacía Xabier iba en contra de la voluntad de los Fundadores."
    aar "Pero la mayoría de los agentes, menos los G, son buenos. Nos acabaron encontrando."
    aar "Primero murió Claire, después Beatrice y Diana. Ahora solo quedamos nosotros tres."
    mc "¿Y qué va a pasar ahora? ¿Van a seguir intentando asesinarnos?"
    call BlinkXP ("c15s006_230" , "d") from _call_BlinkXP_1404
    ama "No. Una vez entró en vigor la cláusula, mataros no tiene sentido. Por eso Eric quería que firmarais el traspaso de acciones."
    ama "Tampoco tiene sentido que nos den caza a nosotros. Ya tenemos el control de NTR y Aaron ha cancelado las órdenes."
    call BlinkXP ("c15s006_235" , "d") from _call_BlinkXP_1405
    eva "Hemos tenido que falsificar alguna de vuestras firmas... *Risita*"
    call BlinkXP ("c15s006_240b" , "d") from _call_BlinkXP_1406
    aar "Xabier ha sido apartado de su puesto y ahora está todo bajo control... más o menos."
    mc "¿Más o menos?"
    aar "Hay todavía algún agente con el que no hemos logrado contactar para anular sus órdenes, pero estará resuelto en los próximos días."
    return
label c15s007_KiaraHouse:
    if _in_replay:
        call mrS3_eil_route from _call_mrS3_eil_route_20
        call mrS3_oma_route from _call_mrS3_oma_route_14
        call mrS3_mar_route from _call_mrS3_mar_route_31
        call mrS3_nor_route from _call_mrS3_nor_route_23
        call mrS3_sam_route from _call_mrS3_sam_route_18
        menu:
            "¿Amanda y Eva te dieron los test de embarazo?"
            "Sí":
                $ KnownToAmandaEva = 1
            "No":
                $ KnownToAmandaEva = 0
    "Por fin llega la hora de ir a casa de [eil] y Kiara a buscar sus cosas. Esperas que Solomon no esté allí."
    "Llamas a Alexia y quedáis en la puerta. Está a punto de terminar su turno y os acompañará antes de volver a la comisaría."
    if KnownToAmandaEva > 0:
        if eil._var("route"):
            "Antes de salir le das a [eil] una de las pruebas de embarazo de Aaron, ponéis la gota de sangre y la guarda en su habitación."
            "Explicarle de dónde ha salido ha sido difícil. Contarle la verdad sobre [eri], [emm] y [dap] ha sido una odisea."
            if oma._var("route"):
                "Coges otra prueba para Alexia."
        elif oma._var("route"):
            "Antes de salir coges una de las pruebas de embarazo de Aaron para dársela a Alexia. Tendrás que explicarle de dónde ha salido."
    if eil._var("route"):
        "Aprovechas el viaje para explicarle también a Kiara la situación de [eri], [emm], [dap], Amanda y Eva."
    else:
        "Aprovechas el viaje para explicarles a [eil] y a Kiara la situación de [eri], [emm], [dap], Amanda y Eva."
    "Lo vas a llamar La Conversación de los Clones. O simplemente \"La Conversación\". La vas a tener mucho en los próximos días."
    "Flipan. Hablan entre ellas. Prometen guardar el secreto. Caen en un silencio pensativo hasta estar cerca de su casa."
    play music ("music/motor.ogg")
    call BlinkXP ("c15s007_005" , "d") from _call_BlinkXP_1407
    mc "¿Nerviosas?"
    eil "No deberíamos estarlo. Tan solo volvemos a casa a por unas cosas, pero..."
    call BlinkXP ("c15s007_010" , "d") from _call_BlinkXP_1408
    kia "Pero parece que volvamos como unas ladronas... es una sensación rara..."
    kia "He llamado a mi vecina y me ha dicho que Solomon no está en casa, con lo que no debería haber problemas."
    mc "Bueno, cojamos las cosas antes de que vuelva y no tendremos ningún problema. Alexia ya debe estar allí."
    stop music fadeout (1.5)
    call BlinkXP ("c15s007_015" , "f") from _call_BlinkXP_1409
    mc "Gracias por venir, Alexia."
    play music ("music/CumbiaColombiana.ogg")
    oma "Es lo menos que podía hacer, ¿no? Para eso estamos las amigas"
    mc "Tengo que hablar contigo un momento."
    call BlinkXP ("c15s007_020" , "d") from _call_BlinkXP_1410
    kia "Os dejamos que habléis mientras vamos trayendo cosas. Supongo que vas a tener \"La Conversación\"."
    mc "Sí, es algo que quiero que sepa toda la familia lo antes posible."
    call BlinkXP ("c15s007_025" , "d") from _call_BlinkXP_1411
    oma "¿Que es eso de La Conversación? Casi se podían escuchar las mayúsculas."
    mc "Te acuerdas de que te llamé el lunes mientras llevabas a tu abuelo a San Diego, ¿verdad?"
    scene c15s007_030An
    "Le explicas el secuestro, por qué la llamaste ese día mientras conducía a San Diego, y todo lo que ha pasado desde entonces."
    "También todo lo que va a pasar a partir de ahora y el secreto familiar."
    call BlinkXP ("c15s007_035" , "d") from _call_BlinkXP_1412
    oma "Es alucinante... parece sacado de una novela mala de ciencia ficción y espionaje escrita por un escritor tarado..."
    mc "Yo he pensado lo mismo cuando nos han dicho que sobre el accidente hubo sospechas de sabotaje."
    call BlinkXP ("c15s007_040" , "h") from _call_BlinkXP_1413
    oma "Gracias por confiar en mí, [mc]... supongo que también tendré que agradecérselo a [mar] y [nor]."
    if oma._var("route"):
        mc "¿Cómo querías que no confiara en mi novia? Te confiaría mi vida."
    else:
        mc "¿Cómo querías que no confiara en ti? Te confiaría mi vida."
    oma "Pero... no sé... después de lo de ayer... ahora esto... ¿me podéis adoptar?"
    mc "Yo creía que ya lo habíamos hecho. *Risa*"
    if oma._var("route") and KnownToAmandaEva > 0:
        call BlinkXP ("c15s007_045" , "d") from _call_BlinkXP_1414
        oma "Genial, pero... ¿cuánto vas a tardar en darme el test? Me muero de ganas por saberlo."
        mc "Alexia, el test tarda 24 horas en dar el resultado. ¿No querrías hacerlo en casa, más tranquila?"
        call BlinkXP ("c15s007_050" , "d") from _call_BlinkXP_1415
        oma "Soy la primera latina en tu vida, ¿verdad?"
        oma "¡Lo quiero ahora! *Risa* No me hagas cometer un delito y robártelo."
        mc "Vale, vale. Ahora te lo doy."
        scene c15s007_055An with fade
        "Coges el test de la guantera y lo abres. Buscas un sitio donde hacerlo y no encuentras ninguno mejor que el asiento del copiloto."
        "Sacáis una gota de sangre del dedo de Alexia, la ponéis en la tira de plástico, y la introducís en la máquina. Se enciende una luz roja."
        scene c15s007_055c with dissolve
        oma "¿Qué es esa luz roja? ¿Significa que no estoy embarazada? ¿O que lo estoy?"
        mc "Significa que ha reconocido la tira de plástico y que hay sangre dentro. Se pondrá verde cuando tenga el resultado mañana a esta hora."
        mc "La otra luz se pondrá verde si el resultado es positivo y roja si es negativo."
        call BlinkXP ("c15s007_060" , "d") from _call_BlinkXP_1416
        oma "¿Y si se queda sin batería?"
        mc "Alexia, es una empresa de tecnología punta que hace clones. Creo que habrán pensado en ponerle la batería suficiente para que pueda funcionar durante 24 horas."
        oma "Tienes razón... es que estoy muy nerviosa... es la primera vez que quiero estar embarazada en mi vida..."
        mc "Mañana sabremos si lo estás. ¿Te lo quieres llevar?"
        call BlinkXP ("c15s007_065" , "d") from _call_BlinkXP_1417
        oma "No, mejor llévatelo tú. Imagínate que me lo dejo en el coche patrulla y lo coge otro compañero sin saber qué es."
        mc "Vale, lo meteré en la guantera y al llegar a casa..."
    call BlinkXP ("c15s007_070" , "d") from _call_BlinkXP_1418
    eil "Aquí está la bici. Mi madre está llenando sus maletas. Ahora voy a llenar yo las mías."
    mc "¿Necesitáis ayuda?"
    call BlinkXP ("c15s007_075" , "d") from _call_BlinkXP_1419
    eil "Gracias, pero no. No te quiero ver revolviendo entre mi ropa. *Risa*"
    mc "Yo tenía pensado robarte el uniforme de animadora. *Risa*"
    eil "Voy a empezar a recoger la ropa. Os dejo con La Conversación."
    call BlinkXP ("c15s007_080" , "d") from _call_BlinkXP_1420
    oma "Ya la hemos tenido. Es totalmente increíble."
    if oma._var("route"):
        oma "Y ya hemos hecho el test también."
        mc "Ahora solo falta esperar las 24 horas para saber el resultado."
        if eil._var("route"):
            call BlinkXP ("c15s007_085" , "d") from _call_BlinkXP_1421
            eil "El tuyo y el mío darán el resultado con una hora de diferencia..."
            eil "¿Quieres que los miremos juntas? Yo estaré en el trabajo cuando pasen las 24 horas del mío."
            call BlinkXP ("c15s007_090" , "d") from _call_BlinkXP_1422
            oma "Te paso a buscar mañana por el trabajo y vamos a casa de [mc]. Así los podremos mirar juntas, no te preocupes."
            oma "Ahora hay que convencer a éste de que no los mire sin nosotras allí."
            mc "¡Hey! ¡Estoy aquí! Tranquilas, no lo voy a mirar sin vosotras delante."
    mc "[eil], hay unas maletas esperándote. ¿Podemos hablar luego del tema? No me gustaría que tu padre llegara y nos pillara aquí."
    call BlinkXP ("c15s007_095" , "d") from _call_BlinkXP_1423
    eil "Tranquilo, no volverá hasta medianoche, pero tienes razón, voy a llenar las maletas. Hasta ahora."
    mc "Te esperamos aquí."
    call BlinkXP ("c15s007_100" , "d") from _call_BlinkXP_1424
    mc "La situación de [eil] y Kiara es muy jodida."
    oma "Sí que lo es. Si Kiara no quiere denunciar, no podemos hacer nada si no lo pillamos in fraganti."
    mc "¿Ni siquiera con el testimonio de [eil]?"
    call BlinkXP ("c15s007_105" , "d") from _call_BlinkXP_1425
    oma "Es complicado. Cuando se produjo la agresión, [eil] no estaba. Cuando llegó no hubo más violencia, y la violencia de hace años no nos sirve de nada ahora."
    mc "Por suerte ahora están a salvo en casa de [nor]."
    oma "Sí, pero ¿qué pasará cuando vuelvan aquí la semana que viene?"
    mc "Si Solomon es inteligente, las tratará como reinas porque debe estar acojonado ahora mismo."
    call BlinkXP ("c15s007_110" , "d") from _call_BlinkXP_1426
    oma "¡Venga ya! Si fuera inteligente no habría hecho lo que ha hecho. Además, ese tipo de personas difícilmente cambian."
    mc "Es lo que le dije a Kiara..."
    oma "El mayor problema es que no tienen donde ir... o no quieren tener donde ir. Yo les he ofrecido mi casa..."
    mc "Y en mi casa se pueden quedar tanto tiempo como quieran, pero Kiara tiene prisa en volver a la suya."
    call BlinkXP ("c15s007_115" , "d") from _call_BlinkXP_1427
    oma "¿No la tendrías tú? En tu casa son invitadas, pero su casa es esta. No es un hogar, pero es su casa."
    mc "Lo entiendo, pero ¿y si la próxima vez Solomon no se contenta con hacerle unos hematomas?"
    oma "Entonces tendrá que denunciar, o irse, o..."
    scene c15s007_120d with dissolve
    "Radio" "Martínez, ¿estás operativa todavía? Todavía veo la chatarra de tu coche en el aparcamiento."
    call BlinkXP ("c15s007_120" , "d") from _call_BlinkXP_1428
    oma "Sí, Schrute. He acabado mi turno, pero estoy haciendo un último servicio. Dime."
    python:
        if "sch" not in globals () or not isinstance (aar, TGCharacter):
            sch = TGCharacter ("Schrute", color = "#060f6c")
    sch "Ha habido un accidente en Mill Road. ¿Te puedes acercar?"
    oma "¿No pueden ir Jones o Garcia? Hace una hora que han empezado su turno."
    sch "Ahí está el problema. El accidente lo ha tenido Jones contra un civil. Él está bien, pero su coche no. El civil necesitará atención. Ya he enviado la grúa y la ambulancia."
    sch "Y antes de que preguntes, Garcia está en un servicio, esta vez no se está escaqueando."
    oma "Lo entiendo. Voy para allá."
    sch "Gracias, preciosa. Trae a Jones aquí. Le tendrás que dejar tu coche patrulla para esta noche."
    oma "Corto y cierro."
    call BlinkXP ("c15s007_125" , "d") from _call_BlinkXP_1429
    oma "Ya lo has oído, me tengo que ir."
    mc "Ya, el deber es lo primero. No te preocupes, ya me quedo yo con Kiara y [eil]."
    oma "Llámame si hay algún problema. En cuanto acabe vendré, no me debería llevar más de 30 o 40 minutos..."
    mc "En 30 minutos ya no deberíamos estar aquí, no te preocupes. Y ya has oído a [eil], su padre no volverá hasta medianoche."
    oma "De todas formas, llámame o escríbeme cuando estéis en casa. Me quedaré más tranquila. Yo te llamaré cuando acabe, por si aún estáis aquí."
    if oma._var("route"):
        call KissXP ("c15s007_130" , "d") from _call_KissXP_40
        oma "Te quiero."
        mc "Yo también te quiero."
    else:
        scene c15s007_130a with dissolve
        mc "Perfecto, te llamo luego."
        oma "Hasta luego."
    stop music fadeout (1.5)
    call BlinkXP ("c15s007_135" , "f") from _call_BlinkXP_1430
    "Unos minutos después..."
    play music ("music/CelticFlute.ogg")
    eil "¿Dónde está Alexia?"
    mc "La han llamado para un servicio de urgencia. Si no habéis terminado cuando lo acabe, volverá."
    call BlinkXP ("c15s007_140" , "d") from _call_BlinkXP_1431
    mc "Una maleta hecha. ¿Os queda mucho?"
    eil "Yo casi he acabado, mi otra maleta ya está hecha y solo me falta cerrarla. Voy a ayudar a mi madre con las suyas."
    mc "¿Queréis ayuda?"
    call BlinkXP ("c15s007_140b" , "d") from _call_BlinkXP_1432
    eil "No te preocupes, entre las dos acabaremos rápido. No creo que a mi madre le gustara que hurgaras entre su ropa interior."
    mc "Ermmm..."
    call BlinkXP ("c15s007_145" , "d") from _call_BlinkXP_1433
    eil "*Risa* ¡Y no hagas ninguna broma sobre meterte en sus bragas, que te conozco!"
    mc "Maleta cargada. Solo quedan tres más."
    mc "No iba a hacer ninguna broma... Y no me des ideas. *Risa*"
    call BlinkXP ("c15s007_150" , "d") from _call_BlinkXP_1434
    eil "¿Lo estás diciendo en serio?"
    mc "Por supuesto, que sí."
    mc "No iba a hacer ninguna broma. *Risa*"
    call BlinkXP ("c15s007_155" , "d") from _call_BlinkXP_1435
    eil "No, idiota. Estoy hablando en serio. Lo de tener ideas con mi madre."
    mc "¿Qué? ¡No! No se me ha ocurrido nunca. Tan solo te seguía la broma."
    call BlinkXP ("c15s007_160" , "d") from _call_BlinkXP_1436
    eil "Casi me habías asustado... después del beso de antes..."
    mc "Me ha besado porque la has puesto entre la espada y la pared, no porque quisiera."
    mc "Y ha sido el beso menos sensual que me han dado nunca... hasta el de Tía Betty ha sido mejor. *Risa*"
    call BlinkXP ("c15s007_165" , "d") from _call_BlinkXP_1437
    kia "¿Hasta una monja besa mejor que yo? Tendré que mejorar eso. *Risa* ¿Y por qué te has asustado, [eil.nick]? Solo ha sido un beso."
    call BlinkXP ("c15s007_170" , "d") from _call_BlinkXP_1438
    eil "Por nada... [mc] ha hecho una broma sobre tu ropa interior y..."
    mc "¡Pero si yo no he llegado a decir nada!"
    call BlinkXP ("c15s007_175" , "d") from _call_BlinkXP_1439
    eil "¡Vale, tú no has dicho nada! Me he montado yo sola la película en la cabeza... Pero imaginaros juntos..."
    scene c15s007_180 with dissolve
    kia "*Risa* ¿Qué? ¿[mc] y yo juntos? ¡Después la loca soy yo! *Risa* Espero que no me estés retando como con el beso."
    mc "*Risa* No sé si sentirme ofendido ahora mismo."
    call BlinkXP ("c15s007_185" , "d") from _call_BlinkXP_1440
    kia "No me refiero a eso, cielo. ¿Qué ibas a hacer tú con una mujer como yo, con todos los problemas que hay en mi vida ahora mismo? *Risa*"
    mc "Ayudarte a resolverlos, por supuesto. *Risa*"
    call BlinkXP ("c15s007_190" , "d") from _call_BlinkXP_1441
    if eil._var("route"):
        kia "No me extraña que le echaras el lazo en cuanto volvió, [eil.nick]. Siempre tiene la respuesta adecuada para todo."
    else:
        kia "Es una lástima que no le echaras el lazo en cuanto volvió, [eil.nick]. Siempre tiene la respuesta adecuada para todo."
    mc "Eso no es verdad, pero sabes que estoy para ayudarte en cualquier cosa que necesites. Que necesitéis las dos."
    call BlinkXP ("c15s007_195" , "d") from _call_BlinkXP_1442
    if eil._var("route"):
        kia "[eil.nick], si alguna vez te cansas de él, me lo pido para mí. *Risa*"
    else:
        kia "Estoy por pedírmelo para mí ahora que no lo tendría que compartir contigo, [eil.nick]. *Risa*"
    mc "Yo estoy abierto a ser compartido. *Risa*"
    kia "Si tuviera 25 años menos y estuviera soltera... *Risa*"
    call BlinkXP ("c15s007_200" , "d") from _call_BlinkXP_1443
    eil "¿Ves? ¡A eso me refiero! Empezáis con las bromas, los abrazos y los besos y acabáis..."
    stop music fadeout (1.5)
    mc "[eil.nick], ¿en serio te preocupa que tu madre y yo acabemos juntos?"
    python:
        if "sol" not in globals () or not isinstance (aar, TGCharacter):
            sol = TGCharacter ("Solomon", color = "#6c0615")
    scene c15s007_205a with dissolve
    play music ("music/AnxiousMarch.ogg")
    sol "*Voz de borracho* A ella quizás no, pero a mí sí. *Hic* ¡Quítale las manos de encima a mi mujer!"
    call BlinkXP ("c15s007_210" , "d") from _call_BlinkXP_1444
    kia "¡Solomon! ¡No es lo que pueda parecerte! ¿Qué haces aquí?"
    scene c15s007_205b with dissolve
    sol "*Voz de borracho* ¿Qué hago aquí? ¡Es mi puta casa! *Hic* Un amigo me ha llamado para decirme que la policía estaba en la puerta de casa."
    sol "*Voz de borracho* Y llego para ver que mi propia mujer me está robando y está *Hic* en los brazos de otro hombre! ¡De un niñato!"
    call BlinkXP ("c15s007_215" , "d") from _call_BlinkXP_1445
    kia "No estamos robando, hemos venido a por algo de ropa. Nuestra ropa. Y..."
    scene c15s007_205c with dissolve
    sol "*Voz de borracho* Y a avergonzarme delante de todo el barrio *Hic* abrazando a otro delante de casa. ¡Además, al ex-novio de tu hija!"
    mc "Solomon, no te acerques más. Solo era un abrazo."
    scene c15s007_220 with dissolve
    mc "[eil], ve a buscar las maletas. Kiara, detrás de mí."
    eil "Voy."
    scene c15s007_205d with dissolve
    sol "*Voz de borracho* ¿Ahora me das ordenes? *Hic* ¿Y también a tus putitas?"
    mc "No les faltes al respeto, Solomon. Estás borracho."
    call BlinkXP ("c15s007_225" , "d") from _call_BlinkXP_1446
    kia "[mc] solo ha venido a ayudarnos y se lo estaba agradeciendo con un simple abrazo."
    mc "Déjanos acabar de recoger lo que hemos venido a llevarnos y no habrá problemas, Solomon."
    scene c15s007_205e with dissolve
    sol "*Voz de borracho* ¡Tú quieres robarme mi familia! *Hic* ¡Pero esta se queda aquí!"
    scene c15s007_205An with dissolve
    mc "¡Te he dicho que no te acerques! ¿No tuviste suficiente con lo que le hiciste el otro día?"
    scene c15s007_205i with dissolve
    sol "*Voz de borracho* ¡No te entrometas en los asuntos de mi familia!"
    scene c15s007_205An2 with dissolve
    sol "¡Aaargh!"
    play sound ("music/MurderByShovel.ogg")
    call BlinkXP ("c15s007_230" , "d") from _call_BlinkXP_1447
    kia "¡Solomon! ¡Para ahora mismo! ¡Déjanos irnos con nuestras cosas!"
    mc "Haz caso a tu mujer y vete, Solomon. No quiero hacerte daño."
    scene c15s007_205m with dissolve
    sol "*Voz de borracho* ¡Pelea como un hombre!"
    mc "No quiero pelear contigo, Solomon."
    scene c15s007_205An3 with dissolve
    sol "*Voz de borracho* ¡Hijo de puta!"
    play sound ("music/MurderByShovel.ogg")
    sol "¡Aaargh!"
    mc "Quédate ahí, Solomon. No quiero pegarte delante de tu mujer, pero no dudaré en hacerlo si vuelves a intentar pegarme a mí."
    call BlinkXP ("c15s007_235" , "d") from _call_BlinkXP_1448
    kia "No te levantes, por favor, Sol. No quiero que te hagan daño."
    mc "Haz caso a Kiara. Kiara, sube al coche, por favor."
    call BlinkXP ("c15s007_235b" , "d") from _call_BlinkXP_1449
    mc "*Susurrando* Mira, puto desperdicio humano, no quiero que te vuelvas a acercar a Kiara o [eil] si no se acercan ellas primero."
    mc "*Susurrando* Sólo he necesitado un pequeño empujón para que acabes en el suelo. Si se te ocurre tocarlas, a cualquiera de las dos, entonces vendré a por ti y no seré comprensivo. ¿Entendido?"
    sol "¡Son mi mujer y mi hija! ¡Tú no eres nadie...!"
    scene c15s007_205q with vpunch
    sol "¡Aaargh!"
    mc "¡Oops, qué asco! Me parece que he pisado una mierda de perro. Pero al menos así las dos manos te dolerán igual."
    mc "Te he preguntado si me has entendido."
    sol "¡Sí, sí!"
    call BlinkXP ("c15s007_240" , "f") from _call_BlinkXP_1450
    eil "Ya está, esto es lo último."
    call BlinkXP ("c15s007_245" , "d") from _call_BlinkXP_1451
    eil "¿Qué ha pasado? ¿Lo has tumbado?"
    mc "No, [eil.nick], Se ha tumbado solo. Ha intentado pegarme y ha acabado con la cabeza en la camioneta. Está muy borracho."
    scene c15s007_205r with dissolve
    sol "*Voz de borracho* Tu exnovio no pelea limpio. *Hic* Pero iré a buscaros cuando él no esté."
    scene c15s007_205s with dissolve
    sol "¡Aaargh! ¡Hija de puta!"
    call BlinkXP ("c15s007_250" , "d") from _call_BlinkXP_1452
    eil "*Susurrando* Escuchame bien, saco de mierda. No te vas a volver a acercar a Mamá, ¿vale?"
    eil "*Susurrando* Voy a hacer todo lo posible para que no vuelva con una basura como tú."
    eil "*Susurrando* Si se te ocurre tocarla o, aunque sea, amenazarla, todo el mundo se va a enterar de que ya no eres un hombre. ¿Vale?"
    eil "*Susurrando* A ver qué mote te sacan tus amigos cuando se enteren ¿Fideo? ¿Picha blanda?"
    mc "[eil], déjalo. Está tan borracho que mañana no se va a acordar de lo que le has dicho."
    call BlinkXP ("c15s007_255" , "d") from _call_BlinkXP_1453
    eil "No, esto no se le va a olvidar. Cuando se pregunte por qué le duele la mano, lo recordará."
    mc "No te conviertas en lo que es él. No vale la pena."
    call BlinkXP ("c15s007_260" , "d") from _call_BlinkXP_1454
    eil "Tienes razón, no merece la pena... pero sienta tan bien... Es tan fácil convertirse en una mala persona..."
    mc "Vámonos, [eil.nick]."
    stop music fadeout (1.5)
    scene black with dissolve
    "Conduces en silencio durante unos minutos hasta que salís del barrio donde está la casa que tan malos recuerdos les trae ahora mismo."
    call BlinkXP ("c15s007_265" , "d") from _call_BlinkXP_1455
    play music ("music/CelticFlute.ogg")
    eil "¿Puedes parar un momento? Necesito estirar las piernas... me tiembla todo."
    mc "Eso es la adrenalina. Te has enfrentado a él por primera vez."
    eil "También voy a necesitar un abrazo..."
    call BlinkXP ("c15s007_270" , "f") from _call_BlinkXP_1456
    eil "Gracias, [mc]."
    mc "No hace falta que las des. Me encanta abrazar."
    eil "¡Idiota! No me refería a eso y lo sabes."
    call BlinkXP ("c15s007_275" , "d") from _call_BlinkXP_1457
    kia "Gracias por como lo has tratado, [mc]... Cualquier otro le hubiera pegado... sé que se lo hubiera merecido... pero no deja de ser mi marido..."
    mc "Ver en la piltrafa de hombre que se ha convertido me ha revuelto el estómago."
    mc "Pegarle no hubiera mejorado nada, tan solo lo hubiera empeorado."
    call BlinkXP ("c15s007_270b" , "d") from _call_BlinkXP_1458
    eil "Mamá, hay espacio aquí para ti también. Sé que te encantan los abrazos de [mc]."
    if eil._var("route"):
        eil "Pero no tengas ideas raras con mi novio."
    else:
        eil "Pero no tengas ideas raras con mi ex-novio."
    mc "Será mejor que no vuelvas a retar a tu madre, [eil]... ya has visto como ha ido con los besos. *Risa*"
    call BlinkXP ("c15s007_275b" , "d") from _call_BlinkXP_1459
    eil "¿Qué? ¡No! ¡No te estoy retando, Mamá!"
    eil "Si te lo tomas como un reto... No creo que sea capaz de mantener sus manos alejadas de ti."
    scene c15s007_275d with dissolve
    kia "*Risa* No funciona así, cielo. No te preocupes, [mc] es un buen amigo, pero soy demasiado vieja para él."
    if mar._var("route") or nor._var("route") or sam._var("route"):
        kia "{i}(Aunque parece que a él la edad no le importa demasiado.){/i}"
    scene c15s007_275e with hpunch
    kia "{i}(¡No! ¡[eil.nick] tiene razón! Estos pensamientos son peligrosos y no debo tenerlos... y soy una mujer casada.){/i}"
    scene c15s007_275f with dissolve
    kia "{i}(Pero se está tan bien aquí... estos abrazos y los besos...){/i}"
    scene c15s007_275g with hpunch
    kia "{i}(¡Los besos! ¿Por qué he aceptado? ¿Cómo puedo ser tan fácil de manipular? ¿Me está manipulando [eil]?){/i}"
    scene black with dissolve
    "Cuando las chicas se calman del todo, pasáis a recoger a [eri] y volvéis a casa. Entre los cuatro subís sus maletas a su habitación."
    stop music fadeout (1.5)
    return
label c15s007_Night:
    if _in_replay:
        call mrS3_dap_route from _call_mrS3_dap_route_27
        call mrS3_sca_route from _call_mrS3_sca_route_22
        call mrS3_mar_route from _call_mrS3_mar_route_32
        call mrS3_emm_route from _call_mrS3_emm_route_34
        call mrS3_sai_route from _call_mrS3_sai_route_16
        menu:
            "¿Intentaste besar a Kate en el Verdad o Reto en la playa?"
            "Sí":
                $ kat._var("kissedBeach" , True)
            "No":
                $ kat._var("kissedBeach" , False)
        menu:
            "¿Tienes Puntos de Relación positivos con Kate?"
            "Si":
                $ kat._var("relationshipPoints", 5, intention = "set")
            "No":
                $ kat._var("relationshipPoints", -1, intention = "set")
        menu:
            "¿Tienes Puntos de Relación positivos con Kim?"
            "Si":
                $ kim._var("relationshipPoints", 5, intention = "set")
            "No":
                $ kim._var("relationshipPoints", -1, intention = "set")
        menu:
            "¿Tienes Puntos de Relación positivos con Debbie?"
            "Si":
                $ deb._var("relationshipPoints", 5, intention = "set")
            "No":
                $ deb._var("relationshipPoints", -1, intention = "set")
        menu:
            "¿Tienes Puntos de Relación positivos con Lisa?"
            "Si":
                $ lis._var("relationshipPoints", 5, intention = "set")
            "No":
                $ lis._var("relationshipPoints", -1, intention = "set")
    "La noticia de que los saludos con besos se han reanudado ha corrido como la pólvora. [emm], [dap], [eri], y [sca] se unen a la nueva costumbre sin hacer preguntas."
    "[mar], [nor] y Betty continúan con ella. Incluso Olivia te saluda con un beso en los labios al llegar. Reluctantemente, pero menos que por la tarde."
    "Después de cenar, Kiara se despide de ti con un beso, casi tan reluctante como el de Meemaw, lo cual te sorprende después del último beso de la tarde. El de [eil] es normal."
    "Vuelves a casa después de un día lleno de emociones, pero escuchas risas en la sala nada más entrar."
    scene c15s007_280a with dissolve
    play music ("music/PositiveWoman.ogg")
    mc "Buenas noches, chicas. ¿Parece que tenéis una fiesta hoy? Veo mucho vino ahí, y algunas botellas vacías."
    kat "Es noche de chicas. Muchas confidencias que hacernos. *Risa*"
    kim "No sabíamos que saliste con [sai] en Portland."
    sai "No salíamos... al menos no oficialmente."
    deb "Bueno, pero erais pareja, ¿no?"
    lis "No, Deb, tenían una relación abierta, podrían haber salido con otras personas si hubieran querido. Lo ha explicado [sai] cuando has ido al lavabo."
    mc "Supongo que no soy bienvenido a quedarme, ¿no?"
    scene c15s007_280b with dissolve
    todas "¡No!"
    kim "Hemos dicho noche de chicas, y si estás delante, [sai] no nos va a poder contar cosas sobre ti. *Risa*"
    if deb.rps > 0 or kim.rps > 0 or lis.rps > 0 or kat.rps > 0 or dap._var("route") or sca._var("route"):
        deb "Después de los besos de ayer en la playa, ya has aparecido en la conversación."
        kat "Y queremos saber más *Risa*"
    lis "Aunque no solo hemos hablado de ti, ¿eh?"
    mc "*Sniff* Pues me voy desconsolado a mi habitación sintiéndome rechazado. *Risa*"
    sai "¿Puedo hablar contigo un momento antes de que te vayas?"
    mc "Por supuesto."
    call BlinkXP ("c15s007_285" , "d") from _call_BlinkXP_1460
    sai "[emm] nos ha contado lo de la nueva costumbre de saludos con besos. ¿Eso también nos incluye a nosotras? *Susurrando* ¿A mí?"
    sai "Algunas queremos participar."
    kim "¡Di que sí, [mc]! Al menos con [sai]..."
    if sai._var("route"):
        sai "*Susurrando* Así podría robarte algunos besos sin que fuera sospechoso para estas chicas."
    else:
        sai "*Susurrando* Así podría robarte algunos besos sin que fuera sospechoso para estas chicas, al menos hasta que decidamos que hacer con lo nuestro."
    sai "*Susurrando* Y si las incluyes a ellas... mejor todavía."
    kat "¡Hey! ¡Nada de secretitos!"
    call BlinkXP ("c15s007_290" , "d") from _call_BlinkXP_1461
    sai "¡Calla, Kate! *Risa* ¡Estoy intentando negociar!"
    call BlinkXP ("c15s007_285" , "d") from _call_BlinkXP_1462
    sai "Si lo vas a hacer con toda la familia... queremos formar parte de la familia... Todas nos sentimos muy a gusto ayer."
    deb "Sí, fue fantástico."
    if kat.rps > 0:
        kat "¡Queremos besos para todas!"
    kim "¡Besos! ¡Besos! ¡Besos!"
    if kim.rps > 0:
        kim "¡Las chicas queremos besos!"
    mc "Chicas, ¿cuánto habéis bebido?"
    lis "Solo un par de botellas... por ahora..."
    sai "Bueno, ¿qué dices? ¿podemos unirnos a la nueva costumbre?"
    mc "Por supuesto, chicas. Pero recordad que es voluntario, no tenéis obligación de hacerlo."
    call KissXP ("c15s007_295" , "d") from _call_KissXP_41
    sai "Pues buenas noches, [mc]."
    mc "Buenas noches, [sai]."
    "El beso de [sai] es mucho más sensual de lo que deberían ser este tipo de saludos, pero no tienes ninguna queja sobre ello."
    sai "Siguiente..."
    "[sai] vuelve a su sitio, dejándole espacio a Kate."
    call KissXP ("c15s007_300" , "d") from _call_KissXP_42
    kat "Buenas noches, besucón."
    mc "Buenas noches, guapísima."
    if kat._var("kissedBeach"):
        "El beso de Kate es mucho más inseguro de lo que sus palabras risueñas dejan entrever. Sus labios saben a vino tinto."
    else:
        "El beso de Kate es un beso de una amiga, en consonancia con sus palabras risueñas. Sus labios saben a vino tinto."
    if kim.rps > 0:
        call KissXP ("c15s007_305" , "d") from _call_KissXP_43
        kim "Buenas noches, guapo."
        mc "Buenas noches, preciosa."
        "Kim te besa con seguridad, e incluso un poco de sensualidad. Puedes notar el sabor a alcohol mezclado con el de su pintalabios."
    if lis.rps > 0:
        call KissXP ("c15s007_310" , "d") from _call_KissXP_44
        lis "Descansa, [mc]."
        mc "Tú también, Lisa."
        "Los labios de Lisa también saben a alcohol, pero su beso es inseguro, como si estuviera dudando sobre si debería hacerlo o no."
    if deb.rps > 0:
        stop music fadeout (1.5)
        call BlinkXP ("c15s007_315" , "d") from _call_BlinkXP_1463
        "Debbie se ha levantado, dudando sobre si acercarse o no."
        play music ("music/SadSoul.ogg")
        call BlinkXP ("c15s007_320" , "d") from _call_BlinkXP_1464
        lis "Debbie, solo es un beso, no implica nada. Y sólo tienes que hacerlo si quieres."
        mc "No es una proposición de matrimonio, Debbie."
        call BlinkXP ("c15s007_325" , "d") from _call_BlinkXP_1465
        deb "¿Puedo darte un beso de buenas noches?"
        mc "Claro que sí, cielo."
        call KissXP ("c15s007_330" , "d") from _call_KissXP_45
        deb "Buenas noches... [mc]."
        mc "Buenas noches, Debbie."
        "El beso de Debbie es increíblemente tímido, tierno y dulce. Es de esos besos que podrían matar a un diabético, pero en ningún momento hace contacto visual contigo"
        mc "*Susurrando* Si tienes algo de lo que quieras hablar, podemos hacerlo mañana... hablar."
        call BlinkXP ("c15s007_335" , "d") from _call_BlinkXP_1466
        deb "*Susurrando* No sé..."
        mc "*Susurrando* Si no hay nada de lo que hablar, no te preocupes, ha sido solo un beso."
        call BlinkXP ("c15s007_340" , "d") from _call_BlinkXP_1467
        deb "*Susurrando* ¿Te gustaría que salieramos a correr mañana y hablamos?"
        mc "*Susurrando* Genial. A mediodía tengo que estar en el lago, si no te importa tener que volver sola, podemos ir juntos y hablar por el camino."
        call KissXP ("c15s007_330b" , "d") from _call_KissXP_46
        deb "*Susurrando* Perfecto. Hasta mañana, [mc]."
        "Debbie te pilla por sorpresa con un segundo beso. Sigue siendo tan tierno y dulce como el anterior, pero mucho más seguro."
        mc "Hasta mañana, Debbie."
        kim "¡Hey! Era un solo beso por chica. *Risa*"
        kat "¡Si empezamos una segunda ronda de besos no vamos a continuar la noche de chicas! *Risa*"
        sai "A mi no me importaría una segunda ronda. *Risa*"
        lis "¡Callaos, perras envidiosas! *Risa*"
    scene c15s007_280a with dissolve
    mc "Bueno, chicas, ahora sí que os dejo. Pasadlo bien."
    todas "Buenas noches, [mc]."
    stop music fadeout (1.5)
    scene black with dissolve
    "Subes a tu habitación sin más encuentros."
    if mar._var("route") and emm._var("route"):
        scene c15s007_400d with dissolve
        play music ("music/ABCSong.ogg")
        mc "¿Volvéis a dormir en mi habitación las dos? No es que no seáis bienvenidas... pero hacía varios días."
        mom "Te acuerdas de la idea que tuve sobre [emm] y su novio, ¿no?"
        mom "Hoy parece un buen día para llevarla a cabo."
        emm "Me parece que Mamá se ha vuelto un poco loca. *Risa*"
        mc "Mamá, te quedaste dor... al final no me dijiste la idea que habías tenido."
        call BlinkXP ("c15s007_405" , "d") from _call_BlinkXP_1468
        mom "¡Creía que te la había contado y que estabas de acuerdo!"
        mc "Pues no... ni me lo contaste ni tengo ni idea de con lo que tengo que estar de acuerdo."
        call BlinkXP ("c15s007_410" , "d") from _call_BlinkXP_1469
        emm "Pues lo dejamos para otro día... no sé si va a aceptar. Es... raro."
        mc "Explicadme la idea y decidimos."
        call BlinkXP ("c15s007_415" , "d") from _call_BlinkXP_1470
        mom "Aún recuerdo mi primer beso con un chico. Hice el ridículo más espantoso porque no tenía ni idea de besar."
        mom "No quiero que a [emm] le pase lo mismo."
        mom "Quiero que le enseñes a besar."
        stop music fadeout (1.5)
    else:
        "Llegas y te desplomas como un tronco en la cama. Te quedas dormido casi antes de tocar las sábanas."
    return

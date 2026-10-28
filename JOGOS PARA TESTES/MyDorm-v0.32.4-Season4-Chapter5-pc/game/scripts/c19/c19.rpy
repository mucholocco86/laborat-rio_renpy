label c19:
    call c19s001_JamaalSamantha from _call_c19s001_JamaalSamantha
    if sam._var("route"):
        call c19s001_Samantha from _call_c19s001_Samantha
    call c19s001_MarthaKim from _call_c19s001_MarthaKim
    call c19s002_Simone from _call_c19s002_Simone
    call c19s003_Gifts from _call_c19s003_Gifts
    call c19s004_PhoneMessage from _call_c19s004_PhoneMessage
    call c19s004_Betty from _call_c19s004_Betty
    call c19s004_AmandaEva from _call_c19s004_AmandaEva
    call c19s004_MaddieDebbie from _call_c19s004_MaddieDebbie
    call c19s005_Meemaw from _call_c19s005_Meemaw
    call c19s005_Kiara from _call_c19s005_Kiara
    call c19s005_KateNorah from _call_c19s005_KateNorah
    call c19s007_EileenLisa from _call_c19s007_EileenLisa
    call c19s007_KateWithNor from _call_c19s007_KateWithNor
    call c19s007_MeganJamaal from _call_c19s007_MeganJamaal
    call c19s006_Alexia from _call_c19s006_Alexia
    call c19s008_LeeroyJenkins from _call_c19s008_LeeroyJenkins
    call c19s009_Teaser from _call_c19s009_Teaser
    return
label c19s001_JamaalSamantha:
    if _in_replay:
        menu:
            "¿Está [nor] embarazada?"
            "Sí":
                $ nor._var("pregnant" , True)
            "No":
                $ nor._var("pregnant" , False)
        menu:
            "¿Estás en una relación con Samantha?"
            "Sí":
                $ sam._var("route" , True)
            "No":
                $ sam._var("route" , False)
    call BlinkXP ("c18s005_080" , "d") from _call_BlinkXP_3388
    play music ("music/Sunny-Skies.ogg")
    nor "Pasa a la piscina antes de ir a ponerte el bañador, si tienes curiosidad. Descubrirás que hay alguien con bañador de cuerpo entero."
    mc "*Risa* Ya lo supongo. No esperaba que la mayoría fuera como vais tú y [eri]."
    call BlinkXP ("c19s001_005" , "d") from _call_BlinkXP_2812
    nor "Yo voy a la cocina a por más cosas."
    if nor._var("pregnancyDiscovered"):
        "Levantas una ceja mientras la miras inquisitivamente."
        call BlinkXP ("c19s001_010" , "d") from _call_BlinkXP_2813
        nor "Vaaale, no voy a coger peso."
    mc "Voy a saludar y a ponerme el bañador. En unos minutos iré a ayudarte."
    nor "OK. Te espero allí."
    scene c19s001_015a with fade
    mc "¡Samantha y Jamaal! ¡Ya habéis llegado! ¿Dónde está Simone?"
    mcp "(Samantha haciendo topless. La primera sorpresa del día.)"
    scene c19s001_015b with dissolve
    if not _in_replay:
        $ sam.profileImages.pop (13) # first remove
        $ sam.profileImages.insert (13, ("samantha_13", None)) # then add new
        $ renpy.notify ("Profile Image unlocked for Samantha: 14 - Topless party")
    sam "Ha ido a cambiarse a la habitación de [emm]."
    jam "El más rápido cambiándome he sido yo. *Risa* No tenía que subir a ninguna habitación y he escondido la ropa detrás de un seto."
    mc "*Risa* ¿Qué llevas puesto?"
    call BlinkXP ("c19s001_020a" , "d") from _call_BlinkXP_2814
    jam "Me escribiste que viniera en bikini. *Risa* Me probé uno de mi madre, pero no lo llenaba, con lo que me puse este que compré para una fiesta hace un par de años."
    mc "*Risa* ¡Estás ridículo! Más incluso de lo habitual."
    call BlinkXP ("c19s001_020b" , "d") from _call_BlinkXP_2815
    jam "Al menos yo no llevo una camiseta con un puerco dibujado. *Risa*"
    mc "¡Me la regalaste tú antes de ir a la universidad! *Risa*"
    call BlinkXP ("c19s001_020c" , "d") from _call_BlinkXP_2816
    jam "Que yo tenga un gusto pésimo para regalar ropa no significa que te la tengas que poner. *Risa* Además, te la regalé porque entonces estabas hecho un cerdo. Gordo."
    mc "Volviendo a tu monokini... No sé si atreverme a preguntar que has hecho con tus herramientas para que te quepan ahí. *Risa*"
    call BlinkXP ("c19s001_025" , "d") from _call_BlinkXP_2817
    jam "He tomado malas decisiones en mi vida, como regalarte esa camiseta. *Risa* Pero estar sentado encima de mis pelotas todo el día va a ser una de las peores."
    mc "También has tomado alguna buena. *Risa* Te hiciste amigo mío."
    jam "Dabas pena, siempre sentado solo, tú, tu panza, y tu caja de donuts. *Risa* Lo mejor de nuestra amistad fueron los donuts."
    call BlinkXP ("c19s001_030" , "d") from _call_BlinkXP_2818
    sam "No vais a cambiar nunca, ¿verdad?"
    mc "Yo he cambiado. Ya no llevo la panza ni la caja de donuts."
    call BlinkXP ("c19s001_035" , "d") from _call_BlinkXP_2819
    jam "Y yo también. *Risa* Sigo siendo su amigo aunque ya no tenga donuts."
    mc "Porque soy tu único amigo y no puedes vivir sin mí. *Risa*"
    call BlinkXP ("c19s001_040" , "d") from _call_BlinkXP_2820
    sam "Me han dicho que se ha instaurado una nueva costumbre en esta casa. Algo sobre besos. ¿No me incluye a mí?"
    mc "Por supuesto, a toda la familia. Ven aquí."
    call KissXP ("c19s001_045" , "d") from _call_KissXP_85
    mc "Buenos días, Sam."
    sam "Buenos días, [mc]."
    call BlinkXP ("c19s001_050" , "d") from _call_BlinkXP_2821
    jam "¡Yo también quiero! *Risa*"
    mc "*Risa* Para ti no hay."
    call BlinkXP ("c19s001_055" , "d") from _call_BlinkXP_2822
    jam "¿Yo no soy de la familia? *Sniff*"
    mc "Claro que lo eres, pero no quiero que tus herramientas sufran más si te tengo que besar. *Risa*"
    call BlinkXP ("c19s001_060" , "d") from _call_BlinkXP_2823
    sam "¡[mc]!"
    mc "¿Qué? Mis besos son irresistibles. *Risa* Pueden levantar a un muerto, pero no a Jamaal."
    sam "¡[mc]!"
    mc "Va a tener que seguir sentado encima de su tesoro más preciado. Y no queremos que se le salga de ese bañador ridículo."
    call BlinkXP ("c19s001_065" , "d") from _call_BlinkXP_2824
    jam "¡Hey! Esa es nueva. *Risa* Estaba un poco harto de las bromas sobre morir de pie o vivir de rodillas."
    mc "A tu servicio. Siempre pensando en nuevas formas de meterme contigo. *Risa*"
    if sam._var("route"):
        mc "Voy a tener que llevarme a tu madre un rato."
        call BlinkXP ("c19s001_070" , "d") from _call_BlinkXP_2825
        sam "¿A dónde? [nor] y [mar] me han dicho que no me acercara a las cocinas. Han dicho que hoy soy una invitada."
        mc "No tiene que ver con la comida, no te preocupes. Quiero enseñarte una cosa que tengo en mi habitación."
        sam "Ah, OK. Vamos entonces."
    else:
        mc "Voy a subir a ponerme el bañador a mi habitación. Bajo en un momento."
    call BlinkXP ("c19s001_075" , "d") from _call_BlinkXP_2826
    mc "Tú puedes venir también si quieres, Jam."
    jam "Creo que voy a pasar. Ya te he visto desnudo antes y no vale la pena arrastrarme por esas escaleras para volver a hacerlo."
    jam "Seguro que cuando bajase tu madre había tirado la silla porque molestaba o estaba fuera de su sitio. *Risa*"
    mc "Entonces te veo luego. Bajo en un momento."
    call BlinkXP ("c19s001_080" , "d") from _call_BlinkXP_2827
    jam "Hasta ahora. Yo esperaré aquí, al lado de los entremeses que va a bajar [mar]. No sé si quedarán cuando bajes."
    mc "Ahora mando a Betty para que los proteja. *Risa* Le diré que quiero bendecir la mesa y no dejará que nadie coma hasta que vuelva."
    jam "Eres un mal amigo... *Risa*"
    if not sam._var("route"):
        call BlinkXP ("c19s001_085" , "d") from _call_BlinkXP_2828
        sam "Antes de que te vayas... ¿puedo hablar un momento contigo?"
        mc "Por supuesto. Hoy va a estar toda la familia y va a ser complicado estar a solas."
        call BlinkXP ("c19s001_090" , "f") from _call_BlinkXP_2829
        mc "¿De qué quieres hablar?"
        if not persistent.family:
            call c19s001_SamConvSecret from _call_c19s001_SamConvSecret
        call c19s001_SamConvAmEv from _call_c19s001_SamConvAmEv
        call BlinkXP ("c19s001_095c" , "d") from _call_BlinkXP_2830
        sam "Entonces no te entretengo más."
        mc "Nos vemos en un rato."
        stop music fadeout (1.5)
    return
label c19s001_Samantha:
    if _in_replay:
        $ sam._var("route" , True)
        menu:
            "¿Estás en una relación con [mar!t]?"
            "Sí":
                $ mar._var("route" , True)
                menu:
                    "¿Está embarazada?"
                    "Sí":
                        $ mar._var("pregnancyDiscovered" , True)
                    "No":
                        $ mar._var("pregnancyDiscovered" , False)
            "No":
                $ mar._var("route" , False)
                $ mar._var("pregnancyDiscovered" , False)
        menu:
            "¿Estás en una relación con Simone?"
            "Sí":
                $ sim._var("route" , True)
            "No":
                $ sim._var("route" , False)
    stop music fadeout (1.5)
    call BlinkXP ("c19s001_105" , "f") from _call_BlinkXP_2831
    "Al llegar a tu habitación..."
    play music ("music/Bolero.ogg")
    sam "¡Qué difícil se hace mantener el secreto delante de Jamaal y darte solamente un besito!"
    sam "¡Ven aquí!"
    mc "A tus órdenes."
    scene c19s001_105d with dissolve
    "Los jugosos labios de Samantha aprisionan los tuyos."
    "Sus tetas presionan contra tu pecho."
    "Vuestras manos recorren la piel del otro."
    "Hasta que Sam se separa de ti."
    call BlinkXP ("c19s001_110" , "d") from _call_BlinkXP_2832
    sam "Si quieres llegar a tiempo para la comida, mejor parar, ¿no?"
    mc "Es difícil parar. Te veo tan poco que cuando te tengo entre mis brazos se me hace casi imposible."
    call BlinkXP ("c19s001_115" , "d") from _call_BlinkXP_2833
    sam "Lo sé... pero con el trabajo tengo muy poco tiempo libre..."
    sam "Y cuando tengo tiempo libre, Jamaal está en casa."
    mc "No te preocupes, encontraremos tiempo para nosotros."
    call BlinkXP ("c19s001_120" , "d") from _call_BlinkXP_2834
    sam "¿Qué querías enseñarme?"
    mc "¿Cuánto te han contado de Amanda y Eva?"
    "Te pone al día sobre cuánto sabe. Tú la pones al día sobre las pruebas de embarazo."
    call BlinkXP ("c19s001_125" , "d") from _call_BlinkXP_2835
    sam "¿Eso existe? Tiene que ser tecnología muy avanzada... no he oído nunca hablar de algo así."
    mc "Por lo que me comentó Amanda, mide no-se-qué hormonas de una forma que no se había podido medir hasta ahora, al menos de forma doméstica."
    mc "NTR no solo se dedica a lo que todos sabemos, sino que parece ser que tiene una división muy importante de medicina aplicada."
    call BlinkXP ("c19s001_130" , "d") from _call_BlinkXP_2836
    sam "Y quieres que me haga la prueba, ¿no?"
    mc "Sólo si tú quieres. O si has notado algún síntoma. Tenemos los tests, con lo que creo que sería una buena idea saberlo."
    call BlinkXP ("c19s001_135" , "d") from _call_BlinkXP_2837
    sam "¿Y qué querrías que saliera en el test?"
    menu:
        "Me gustaría que saliera positivo":
            mc "No me malinterpretes, no voy a sentirme mal si sale negativo, pero me haría ilusión tener un hijo contigo."
        "Preferiría que saliera negativo":
            mc "No me malinterpretes, pero hasta que se lo digamos a Jamaal preferiría no enredarlo más."
        "No tengo preferencias":
            mc "Te voy a querer igual salga una cosa o la otra."
    mc "¿Y tú? ¿Qué te gustaría a ti que saliera en el test?"
    call BlinkXP ("c19s001_140" , "d") from _call_BlinkXP_2838
    sam "No lo he pensado aún. Si sale positivo me alegraré, aunque tiene riesgos a mi edad. Ya he pasado de los 40..."
    sam "Pero si sale negativo no me voy a sentir decepcionada. A mi edad la fertilidad cae considerablemente, con lo que no espero que me dejes embarazada en dos intentos."
    mc "Lo entiendo. Tomemos la muestra de sangre y lo sabremos mañana a esta hora."
    call BlinkXP ("c19s001_145" , "d") from _call_BlinkXP_2839
    sam "No. Mañana a esta hora estaré trabajando, y quiero mirarlo contigo. Me lo llevaré a casa y lo miraremos cuando vengas."
    mc "Pero pueden pasar días hasta que pueda ir y coincidamos los dos solos en tu casa..."
    call BlinkXP ("c19s001_150" , "d") from _call_BlinkXP_2840
    sam "Bueno, no hay prisa. Si sale positivo tenemos tiempo antes de que empiece a engordar, y no tengo ningún síntoma."
    mc "Cómo quieras. Trae ese dedo aquí y extraigamos la sangre."
    call BlinkXP ("c19s001_155" , "d") from _call_BlinkXP_2841
    "Después de tomar la muestra..."
    sam "Luego pasaré para coger el test. Cuando tenga el bolso para guardarlo."
    mc "Perfecto, lo dejaré en el cajón debajo de la TV."
    if sim._var("route"):
        call BlinkXP ("c19s001_160" , "d") from _call_BlinkXP_2842
        sam "¿Ya has hecho la prueba con Simone?"
        mc "No, aún no. No la he visto desde que tenemos los tests. No habéis venido a ninguna de las comidas o cenas familiares estos días."
        mc "Luego le diré que suba para hacer la prueba."
    call c19s001_SamConvAmEv from _call_c19s001_SamConvAmEv_1
    if not persistent.family:
        call c19s001_SamConvSecret from _call_c19s001_SamConvSecret_1
    call BlinkXP ("c19s001_190" , "d") from _call_BlinkXP_2843
    sam "Entonces voy a bajar. Al final Jamaal va a sospechar."
    mc "No sin antes dejarme hacer esto."
    scene c19s001_195d with hpunch
    sam "¡[mc]!"
    call BlinkXP ("c19s001_195" , "d") from _call_BlinkXP_2844
    mc "No puedes esperar venir a mi habitación con estas maravillas al aire y que no tome medidas, ¿verdad?"
    sam "Pero tenemos que bajar... o van a sospechar..."
    mc "No te importó hacerlo público en la playa. Quien tenga que sospechar, que sospeche."
    scene c19s001_200pv with dissolve
    show c19s001_200v with dissolve
    "El pezón de Samantha responde a las caricias de tu lengua poniéndose durísimo."
    sam "[mc], si sigues así, la prueba de embarazo que acabamos de hacer no va a servir de mucho y habrá que hacer otra en un par de días..."
    "No te importaría que eso pasara, pero sabes que no es el momento."
    "También sabes que si no paras ahora, va a ser casi imposible hacerlo."
    "Pero, por alguna razón, te es muy difícil mantener tu lengua y tus manos quietas."
    play sound ("music/knock.ogg")
    stop music fadeout (1.5)
    "*Knock-Knock*"
    mcp "(Salvados por la campana... o por unos golpes en la puerta.)"
    play music ("music/Wonder.ogg")
    call BlinkXP ("c19s001_205" , "f") from _call_BlinkXP_2845
    hide c19s001_200v
    "Te separas a regañadientes del pezón de Sam."
    mom "*A través de la puerta* Soy yo. ¿Puedo pasar?"
    mc "Sí, pasa."
    call BlinkXP ("c19s001_210" , "d") from _call_BlinkXP_2846
    if not _in_replay:
        $ mar.profileImages.pop (13) # first remove
        $ mar.profileImages.insert (13, ("martha_13", None)) # then add new
        $ texto = str(mar.name)
        $ renpy.notify ("Profile Image unlocked for "+str(texto)+": 14 - Topless party")
    mom "¡Oops! Lo siento. No sabía que estabas ocupado."
    mc "No te preocupes. ¿Necesitabas alguna cosa?"
    mom "Saber si ya te habías cambiado y si podías ayudarnos a bajar cosas a la piscina. Pero tranquilos, acabad lo que estuvierais haciendo."
    call BlinkXP ("c19s001_215" , "d") from _call_BlinkXP_2847
    sam "No te preocupes, [mar]. Ya habíamos acabado."
    scene c19s001_215d with dissolve
    sam "Ahora toca esperar..."
    mom "¿Prueba de embarazo?"
    sam "Sí..."
    call BlinkXP ("c19s001_220" , "d") from _call_BlinkXP_2848
    if mar._var("pregnancyDiscovered"):
        mom "Espero que la tuya TAMBIÉN salga positiva."
    elif mar._var("route"):
        mom "Espero que la tuya salga positiva."
    else:
        mom "Espero que tengáis mucha suerte."
    call BlinkXP ("c19s001_225" , "d") from _call_BlinkXP_2849
    if mar._var("pregnancyDiscovered"):
        sam "¿También? ¿Estás embarazada, [mar]?"
        call BlinkXP ("c19s001_230" , "d") from _call_BlinkXP_2850
        mom "Sí... Aparte de [nor] eres la primera en saberlo."
    elif mar._var("route"):
        sam "Lo estábamos hablando y aún no sé lo que quiero que salga."
        sam "¿Aún no tenéis tus resultados o es que aún no la necesitas?... ¿O ha salido negativa?"
        call BlinkXP ("c19s001_230" , "d") from _call_BlinkXP_2851
        mom "Negativo, pero eso sólo significa que lo deberemos intentar más."
    else:
        sam "Se me hace tan raro esto de que sepas lo nuestro después de que tú y yo bromeáramos sobre compartir a [mc]..."
        call BlinkXP ("c19s001_230" , "d") from _call_BlinkXP_2852
        mom "Bueno, ahora soy tu suegra, pero no voy a ser una mala suegra. Sé que mi hijo no podría estar con nadie mejor."
    call BlinkXP ("c19s001_235" , "h") from _call_BlinkXP_2853
    if mar._var("route"):
        "Samantha se lanza a los brazos de [mar]. Se encuentran a medio camino."
        sam "Se me hace tan raro estar hablando de embarazos a nuestra edad..."
        mom "Embarazos posiblemente provocados por el mismo hombre..."
        sam "Que además es tu hijo..."
        mom "Nuestros hijos siempre han sido amigos y se han tratado como hermanos... si tenemos más, serán hermanos de verdad..."
        mc "¡Hey! ¡Jam es mi hermano de verdad!"
        scene c19s001_235d with dissolve
        sam "Nadie lo pone en duda, pero estos serán hermanos del mismo padre..."
        mom "Con lo que serán medio-hermanos..."
        mc "Sí, Mamá, y tú serás la abuela del hijo de Sam, además de su suegra."
        mc "Y Sam será la cuñada de tu hijo... que también será tu nieto."
        scene c19s001_235e with dissolve
        sam "¡Por el amor de Dios! Eso es demasiado lioso para mí."
        mom "¿Nos vamos antes de que nos explote la cabeza y dejamos que [mc] se cambie de ropa?"
        sam "Mejor... me estoy mareando solo de pensar en las implicaciones de lo que acaba de decir."
        if sim._var("route"):
            mom "Y eso sin pensar en si Simone también está embarazada..."
            mc "Haremos la prueba más tarde. Aún no la he visto."
        scene c19s001_235f with dissolve
        mom "Hasta luego, mi amor."
        sam "Te vemos luego, [mc]."
        mc "¿No hay besos de despedida?"
        scene c19s001_235g with dissolve
        mom "¿Qué opinas?"
        sam "Después de la playa... no me voy a avergonzar por besarlo ahora. ¿Tú?"
        mom "Creo que nos vamos a tener que acostumbrar a que las dos lo besemos delante de la otra."
        call KissXP ("c19s001_240" , "d") from _call_KissXP_86
        mom "Hasta luego, mi amor."
        mc "Hasta luego, mi vida."
        "Pese a lo que acaban de decir, Samantha se gira para daros privacidad, mientras finge mirar algo en el mueble de la TV."
        call KissXP ("c19s001_245" , "d") from _call_KissXP_87
        sam "Te vemos abajo, mi vida."
        mc "En un momento bajo y paso por la cocina a recoger cosas."
        "[mar] hace algo parecido, mirando a ninguna parte para daros un poco de espacio."
        scene c19s001_235h with dissolve
        mc "Por cierto... no solo tenéis unas tetas preciosas ambas sino que también tenéis unos culos increíbles."
        mom "*Risita* Creo que nuestro hombre quiere más besos."
        sam "*Risa* Si por él fuera, tendría mucho más que besos. Pero tenemos unos cumpleaños que organizar."
        scene c19s001_235i with dissolve
        mcp "(Y se fueron. La dinámica entre ellas es perfecta. ¿Quién sabe si algún día...?)"
        stop music fadeout (1.5)
        mcp "(Mejor no pensar en eso ahora. Hora de ponerme el bañador.)"
    else:
        "Las dos avanzan hacia la otra y se funden en un abrazo a medio camino."
        sam "Lo sé. Y yo voy a ser una nuera que no te dará problemas. *Risa*"
        mom "Debería bajar a seguir preparando cosas. Cuando puedas, [mc], ve a la cocina a recoger cosas y bajarlas a la piscina."
        sam "Voy a ayudarte mientras tanto. Y no me digas que soy una invitada. Soy tu nuera, al fin y al cabo."
        mc "Dadme dos minutos y bajo. También le he dicho a [nor] que la ayudaría."
        scene c19s001_235f with dissolve
        sam "Vale, te esperamos en la cocina."
        mom "Si no, no vas a saber lo que tienes que bajar."
        mc "Sam, ¿y mi beso?"
        scene c19s001_235g with dissolve
        sam "¿Te importa?"
        mom "Para nada. Ya te he dicho que no sería una mala suegra. *Risa*"
        call KissXP ("c19s001_245" , "d") from _call_KissXP_88
        sam "Te vemos abajo, mi vida."
        mc "En un momento bajo y paso por la cocina a recoger cosas."
        "[mar] fija su vista en la pared para daros un poco de privacidad. Es una buena suegra, pero aún se tiene que acostumbrar a esto."
        scene c19s001_235h with dissolve
        mcp "(Podría hacer algún comentario sobre que no solo tienen unas tetas increíbles sino unos culos preciosos, pero podría incomodarlas.)"
        scene c19s001_235i with dissolve
        stop music fadeout (1.5)
        mcp "(Y se fueron. Hora de ponerme el bañador.)"
    return
label c19s001_SamConvSecret:
    if sam._var("route"):
        call BlinkXP ("c19s001_175" , "d") from _call_BlinkXP_2854
        sam "Sobre eso... sobre la familia... ¿Cómo te sientes sabiendo que [mar] no es tu madre y que las chicas no son tu hermana y tus primas?"
    else:
        sam "Precisamente sobre eso... sobre la familia... ¿Cómo te sientes sabiendo que [mar] no es tu madre y que las chicas no son tu hermana y tus primas?"
    sam "Cuando [mar] me lo contó... por un momento me enfadé. No había confiado en mí para algo así."
    sam "Por otro lado lo entendí. Es algo demasiado grande para contarlo por ahí."
    mc "Sam, yo siempre lo he sabido. La noticia ha sido una sorpresa para las chicas, pero no para mí."
    if sam._var("route"):
        call BlinkXP ("c19s001_180" , "d") from _call_BlinkXP_2855
    else:
        call BlinkXP ("c19s001_095a" , "d") from _call_BlinkXP_2856
    sam "¿Y siempre guardaste el secreto? ¡Lo debes saber desde muy niño!"
    mc "Me inculcaron que era algo de lo que no debía hablar ni fuera ni dentro de casa si un adulto no sacaba el tema. No ha sido difícil no hablar de ello."
    mc "No es un tema de conversación que salga habitualmente con otros niños. \"Tengo una hermana pero es un clon de alguien\". Nunca me he sentido tentado de hacerlo."
    mc "Además, no es que lo supiera todo con cinco años. Quizás tuve toda la información a los once. O al menos toda la que tenía hasta hace unos días."
    if sam._var("route"):
        call BlinkXP ("c19s001_185" , "d") from _call_BlinkXP_2857
    else:
        call BlinkXP ("c19s001_095b" , "d") from _call_BlinkXP_2858
    sam "Ha tenido que ser muy duro para todos vosotros. Tanto guardar el secreto, como para las chicas descubrirlo ahora."
    mc "Hubo de todo un poco, pero se lo tomaron mejor de lo que esperaba. Quizás excepto [emm], que estuvo enfadada unas horas. Aunque también menos de las que esperaba."
    mc "No te preocupes por nosotros. Todos estamos bien."
    return
label c19s001_SamConvAmEv:
    if sam._var("route"):
        call BlinkXP ("c19s001_165" , "d") from _call_BlinkXP_2859
    else:
        call BlinkXP ("c19s001_100a" , "d") from _call_BlinkXP_2860
    sam "¿Qué me puedes contar de Amanda y Eva? Me han dicho que son... especiales."
    mc "Lo son. Os habéis perdido algunas cosas muy emotivas estos últimos días. Te van a encantar."
    mc "Pero prefiero no explicarte muchas cosas. Quiero que te formes tu propia opinión cuando las conozcas."
    if sam._var("route"):
        call BlinkXP ("c19s001_170" , "d") from _call_BlinkXP_2861
    else:
        call BlinkXP ("c19s001_100b" , "d") from _call_BlinkXP_2862
    sam "No puedo ser imparcial. He estado hablando con [mar] antes. Se le iluminaban los ojos hablando de ellas."
    sam "Especialmente de Amanda. Es la que es igual que [emm], ¿no?"
    mc "Sí. Pero son muy diferentes. Y también Amanda y Eva son diferentes entre ellas."
    sam "No podía parar de sonreír. Si alguien es capaz de poner así de contenta a tu madre... ya se ha ganado mi cariño."
    mc "Ya te digo que son especiales. Todo el mundo en la familia las adora."
    return
label c19s001_MarthaKim:
    scene c19s001_300a with fade
    play music ("music/AmbientPianoStrings.ogg")
    "Después de cambiarte pasas por la cocina..."
    kim "No estaba segura de qué hacer. Es... raro..."
    kim "No creía que tú lo fueras a hacer. Ha sido una sorpresa."
    mom "Lo autoricé porque lo pidió [eri]. Sabía que [nor] también lo iba a hacer, con lo que no me parecía bien dejarlas solas."
    mc "¿Estáis hablando del topless?"
    scene c19s001_300b with dissolve
    mom "Sí. De momento me ha sorprendido un poco quién se ha apuntado."
    kim "Y quién no se ha apuntado..."
    scene c19s001_300c with dissolve
    mom "No, cariño. Cada una de vosotras sois libres para decidir por vosotras mismas. Era una posibilidad y no una obligación."
    mom "Igual que nadie te va a obligar a desnudarte en el jacuzzi o la sauna de [nor]."
    mc "En eso tiene razón, Kim. Tienes permiso para hacerlo, pero no tienes por qué hacerlo si no quieres."
    kim "Pero si soy la única..."
    call BlinkXP ("c19s001_305" , "d") from _call_BlinkXP_2863
    mom "No eres la única. Las hay que llevan un bañador de cuerpo entero. Y hay más chicas que se han decidido por un bikini igual que tú."
    if persistent.family:
        mom "Mi madre y mi tía también llevan bikinis. Al resto aún no las he visto, pero seguro que hay más."
    else:
        mom "Olivia y Betty también llevan bikinis. Al resto aún no las he visto, pero seguro que hay más."
    mc "¡Ohhh! ¿Tía Betty no va a hacer topless? *Risa* ¡Qué decepción! Nunca me lo hubiera imaginado."
    call BlinkXP ("c19s001_310" , "d") from _call_BlinkXP_2864
    mom "[mc], esto es serio. Kim se siente insegura y cohibida con Jamaal y contigo aquí. Estoy segura de que si no estuvierais no tendría dudas."
    mc "¿Habéis visto a Jamaal?"
    scene c19s001_300d with dissolve
    mom "No. Aún no he bajado a la piscina desde que han llegado."
    mc "¿Y él no ha subido a saludarte a la cocina? *Risa* ¡Qué maleducado!"
    kim "¡[mc]! ¡Eso es cruel y no es digno de ti!"
    call BlinkXP ("c19s001_315" , "d") from _call_BlinkXP_2865
    mom "No te preocupes. No lo dice con maldad y siempre están buscando excusas para meterse el uno con el otro."
    mom "Y, aunque deberían, no ponen ningún límite a lo que es correcto y lo que no."
    mc "Si lo pusiéramos dejaría de ser divertido. O tan divertido al menos."
    call BlinkXP ("c19s001_320" , "d") from _call_BlinkXP_2866
    kim "Ah, OK. Nunca he entendido ese tipo de humor..."
    mc "Es fácil de entender. En el instituto éramos los perdedores. La gente se metía conmigo por gordo y con Jamaal por su velocidad y su movilidad."
    mc "Si nosotros nos decíamos en broma lo que otras personas podían decirnos en serio, no tenía sentido que nos lo dijeran porque sabían que no nos iban a hacer daño."
    mc "Es el tipo de humor que utiliza Kate también."
    kim "Pese a todo sigo sin entenderlo. Yo no podría bromear con mis defectos..."
    call BlinkXP ("c19s001_325" , "d") from _call_BlinkXP_2867
    kim "Pero volviendo a Jamaal, nos han presentado antes. Iba con camiseta y bermudas. ¿Por qué preguntas si lo hemos visto?"
    mc "Cuando puedas, baja a la piscina y mira cómo va ahora. Se te quitará cualquier tipo de complejo sobre cómo debes vestirte o qué debes ponerte."
    call BlinkXP ("c19s001_330" , "d") from _call_BlinkXP_2868
    mom "Y sobre [mc], creo que no debería importarte que esté aquí. No lo eduqué para que se quede mirando a una mujer mientras babea porque haga topless."
    mom "Ni siquiera a una tan bonita como tú."
    mc "Pero una mirada de reojo sí que puedo echar de vez en cuando. *Risa*"
    scene c19s001_300e with dissolve
    mom "¡[mc]!" (multiple=2)
    kim "¿Ves?" (multiple=2)
    mc "Sólo estaba bromeando. Si te sirve de algo, prometo no mirar ni una sola vez en tu dirección."
    mc "Independientemente de lo que hagas con el top de tu bikini."
    call BlinkXP ("c19s001_335" , "d") from _call_BlinkXP_2869
    kim "Cambiando de tema... ¿Cuándo vais a dar los regalos a las chicas?"
    mc "Después de comer. ¿Por qué?"
    kim "En mi familia de Cleveland lo hacemos como en Navidad, nada más levantarnos."
    kim "Pero tiene lógica hacerlo así, viniendo gente de fuera de la casa."
    call BlinkXP ("c19s001_340" , "d") from _call_BlinkXP_2870
    mom "Hasta este año sólo habían venido Samantha, Simone, y Jamaal."
    mc "Y Eileen cuando salíamos juntos en el instituto."
    mom "Y Scarlett los últimos seis o siete años. Lo máximo que estuvimos fue... el año antes de que [mc] se marchara. Fuimos catorce."
    call BlinkXP ("c19s001_345" , "d") from _call_BlinkXP_2871
    kim "Este año somos 24. Lo he contado..."
    mc "Va a ser la celebración más grande en la historia de esta casa. No creo que lo superemos."
    call BlinkXP ("c19s001_350" , "d") from _call_BlinkXP_2872
    kim "Mmmm... ¿Cuándo es el próximo cumpleaños?"
    mc "Scarlett, Simone, y Debbie en octubre. Después de ellas vas tú, en noviembre."
    call BlinkXP ("c19s001_355" , "h") from _call_BlinkXP_2873
    kim "¿Te sabes el cumpleaños de todo el mundo?"
    mc "Sí... Es lógico, ¿no? Pero ¿por qué lo preguntabas?"
    call BlinkXP ("c19s001_360" , "d") from _call_BlinkXP_2874
    kim "Para los próximos cumpleaños ya estarán aquí las seis chicas que van a vivir en casa de [nor]."
    kim "Si se quieren integrar en la familia... ¡Podríamos llegar a ser 30!"
    mc "Pero no estarán Meemaw y Betty; están ocupando sus habitaciones y tenían planes para volver a Florida. Tampoco vivirán con nosotros Kiara y Eileen, están ocupando otra."
    mc "Y yo seguramente estaré en Aruba todavía, con Eva o Amanda, o las dos."
    call BlinkXP ("c19s001_365" , "d") from _call_BlinkXP_2875
    kim "No me había dado cuenta... La familia se separará tarde o temprano... pero es demasiado pronto."
    mc "Y eso no es lo peor. Lisa y Kate acaban sus carreras en un par de años..."
    call BlinkXP ("c19s001_370" , "d") from _call_BlinkXP_2876
    mom "No adelantemos acontecimientos aún. Queda muchísimo para eso."
    mc "Sí, sólo hace una semana que han llegado y ya estamos pensando lo que las echaremos de menos dentro de uno o dos años."
    scene c19s001_300f with dissolve
    kim "Dame algo para bajar antes de que me pongáis triste solo de pensarlo. *Risa*"
    mom "Coge ese pastel de ahí si quieres. [mc] bajará el resto mientras yo acabo de preparar unas cosas."
    mc "Y después tengo que ir a la cocina de [nor]. Le he prometido que la ayudaría."
    scene c19s001_375d with dissolve
    "Kim se dirige a la puerta y se para justo antes de abrirla."
    kim "Pero..."
    mc "¿Qué pasa, Kim?"
    call BlinkXP ("c19s001_375" , "d") from _call_BlinkXP_2877
    kim "Aunque hayamos acabado nuestras carreras... ¿podremos venir a visitaros?"
    call BlinkXP ("c19s001_380" , "d") from _call_BlinkXP_2878
    mom "Claro que sí, cielo. Siempre seréis bienvenidas en casa."
    mc "Y si tenemos las habitaciones ocupadas, ya apañaremos algo. Yo ya sé lo que es dormir en el sofá."
    mom "Y Newport ha crecido mucho en los últimos años. ¿Quién sabe si alguna de vosotras encuentra un trabajo aquí y decide quedarse?"
    scene c19s001_385An with dissolve
    pause (2.4)
    "Kim planta un sorprendente beso en tus labios tras entregarte la tarta."
    scene c19s001_385An2 with dissolve
    "Y rodea la península de la cocina hasta abrazar a [mar]."
    kim "¡Gracias, [mar]!"
    mom "No pasa nada, cielo."
    kim "*Susurrando* No se lo digas a nadie, pero... ¡Qué vergüenza! He estado a punto de decir \"Gracias, Mamá\". *Risita* Creo que paso demasiado tiempo con [emm] y [mc]."
    mom "*Susurrando* Tampoco pasa nada por eso, cielo."
    mc "¿Qué estáis susurrando? Me gustaría recordaros que estoy aquí. *Risa*"
    scene c19s001_385f with dissolve
    kim "Cosas nuestras..."
    mom "Nada que sea de tu interés ahora mismo, cielo."
    mom "¿Por qué no bajas la tarta? Voy a quedarme hablando con Kim un rato."
    mc "Ningún problema. Os dejo solas."
    stop music fadeout (1.5)
    scene black with dissolve
    "Bajas las bandejas que te ha indicado [mar] y vas a por más a la cocina de [nor]."
    return
label c19s002_Simone:
    if _in_replay:
        $ sim._var("pregnant" , False)
        menu:
            "¿Estás en una relación con [emm]?"
            "Sí":
                $ emm._var("route" , True)
            "No":
                $ emm._var("route" , False)
        menu:
            "¿Estás en una relación con Simone?"
            "Sí":
                $ sim._var("route" , True)
            "No":
                $ sim._var("route" , False)
    play music ("music/Sunny-Skies.ogg")
    scene c19s002_005a with dissolve
    "Cuando acabas de llevar todo lo que está preparado a la piscina, oyes las voces de Simone y [emm] en la sala y decides pasar a saludar."
    if not _in_replay:
        $ emm.profileImages.pop (13) # first remove
        $ emm.profileImages.insert (13, ("emma_13", None)) # then add new
        $ texto = str(emm.name)
        $ renpy.notify ("Profile Image unlocked for "+str(texto)+": 14 - Topless party")
    call KissXP ("c19s002_010" , "d") from _call_KissXP_89
    mc "Felicidades, [emm]."
    emm "Gracias, [mc]. Creo que va a ser el mejor cumpleaños de la historia."
    call KissXP ("c19s002_015" , "d") from _call_KissXP_90
    mc "Buenos días, Simone."
    sim "Buenos días... "
    scene c19s002_005b with dissolve
    sim "..."
    mc "¿Qué pasa, Simone?"
    emm "Oh... ¿nadie le ha explicado que ahora todas saludamos a [mc] así?"
    call BlinkXP ("c19s002_020" , "d") from _call_BlinkXP_2879
    sim "¿Qué? ¿Por qué?"
    mc "Un invento de Tía Betty para sacar a Meemaw de sus casillas."
    call BlinkXP ("c19s002_025" , "d") from _call_BlinkXP_2880
    emm "Yo no estaba, pero por lo que me ha contado mi madre, a mi abuela casi le explota la cabeza. *Risa*"
    mc "Yo sí que estaba. Le faltó muy poco para esa explosión."
    call BlinkXP ("c19s002_030" , "d") from _call_BlinkXP_2881
    sim "¡Qué susto! Por un momento he pensado que vosotros..."
    mc "Lo hace toda la familia, por eso te he besado también a ti. Ya lo he tomado yo también como costumbre y no se me ha ocurrido preguntar."
    if emm._var("route") and sim._var("route"):
        scene c19s002_005c with dissolve
        emm "Pero si nosotros... supongo que te refieres a estar juntos... ¿Sería un problema para ti? Sé que siempre te ha gustado mi hermano."
        sim "No, para nada. Ya me dijo que era posible que saliera con otras chicas... aunque me sorprendería un poco siendo tú..."
        if persistent.family:
            sim "Eres su hermana..."
        else:
            sim "Os habéis criado como hermanos..."
        scene c19s002_005d with dissolve
        emm "Me alegro mucho por vosotros."
        sim "¿Qué? ¿Por qué?"
        emm "No te hubiera dicho eso si no saliera también contigo."
        call BlinkXP ("c19s002_035" , "d") from _call_BlinkXP_2882
        sim "¡Oh, mielda! ¡Lo siento!"
        mc "*Risa* Nunca os metáis a espías. Sois horribles guardando secretos."
        call BlinkXP ("c19s002_040" , "d") from _call_BlinkXP_2883
        emm "¿Yo? ¡Esta vez no he dicho nada!"
        mc "Acabas de decir \"si no saliera también contigo\". *Risa*"
        call BlinkXP ("c19s002_045" , "d") from _call_BlinkXP_2884
        emm "¡Oh, mierda! *Risa* ¡Tienes razón!"
        mc "..."
        emm "*Risa* Sí, lo sé. Siempre tienes razón."
        scene c19s002_005e with dissolve
        emm "¿Ya te has hecho la prueba de embarazo? ¿O vosotros todavía no...?"
        sim "¿Qué prueba de embarazo?"
        mc "Te lo iba a comentar..."
        scene c19s002_005f with dissolve
        "Tras ponerla al día..."
        emm "Yo me la he hecho esta mañana y tendré los resultados mañana."
        mc "Las tengo en mi habitación. Cuando quieras podemos ir y hacerla."
        sim "Estaría bien... no tengo ninguna molestia, pero... siempre es bueno saber algo así, ¿no?"
        call BlinkXP ("c19s002_050" , "d") from _call_BlinkXP_2885
        emm "Pues subid y hacerla. Y si os queréis tomar vuestro tiempo, hacedlo. Yo os cubro."
        mc "Me parece alucinante lo que has cambiado en un par de semanas, [emm]."
        call BlinkXP ("c19s002_055" , "d") from _call_BlinkXP_2886
        emm "Ya tengo 19. Es hora de que me empiece a comportar como la adulta de la casa, ¿no?"
        mc "*Risa* No sé qué diría Mamá si te oyera decir eso."
        call BlinkXP ("c19s002_060" , "d") from _call_BlinkXP_2887
        sim "O Tía Betty y Olivia. *Risa*"
    play sound ("music/doorbell1.ogg")
    "*Ding-Dong*"
    call BlinkXP ("c19s002_065" , "d") from _call_BlinkXP_2888
    emm "Voy a abrir. Seguro que son chicas que vienen a felicitarme el cumpleaños. *Risita*"
    if emm._var("route") and sim._var("route"):
        mc "Muy adulta... *Risa*"
    else:
        mc "Te esperamos aquí."
    scene c19s002_070d with fade
    "Unos segundos después..."
    emm "Mirad quién ha venido."
    ama "Buenos días, [mc]. Encantada de conocerte por fin, Simone."
    eva "Buenos días a los dos. Ya era hora de que nos conociéramos. Creo que tu madre y tu hermano son los últimos que me quedan por conocer."
    mc "Están en la piscina. Podréis conocerlos cuando os cambiéis de ropa."
    call BlinkXP ("c19s002_070" , "d") from _call_BlinkXP_2889
    sim "Si no os tuviera delante no podría creerlo... es increíble."
    mc "Te acostumbrarás muy pronto. *Risa*"
    scene c19s002_070e with dissolve
    emm "Las llevo a mi habitación a que se cambien."
    ama "Un segundo, [emm]."
    call KissXP ("c19s002_075" , "d") from _call_KissXP_91
    ama "Buenos días, [mc]."
    mc "Buenos días, Amanda."
    call KissXP ("c19s002_080" , "d") from _call_KissXP_92
    eva "Buenos días, [mc]."
    mc "Buenos días, Eva."
    eva "Ya nos podemos ir."
    mcp "(Sin un cronómetro en la mano no podría asegurarlo, pero juraría que sus besos no se han desviado más de una décima de segundo.)"
    scene c19s002_070f with dissolve
    eva "Hablamos luego, Simone. Tengo ganas de conocerte mejor."
    ama "Yo también, además... bueno ya lo hablaremos otro día."
    emm "Vámonos o no podremos cotillear mientras os cambiáis."
    call BlinkXP ("c19s002_085" , "d") from _call_BlinkXP_2890
    "Una vez se han ido..."
    sim "Voy a volver a repetirlo... Increíble..."
    mc "*Risa* Tranquila. La sorpresa se pasa en cuanto empieces a hablar con ellas."
    mc "Son buenas chicas, aunque prefiero que te formes una opinión tú, una vez hayas tenido la oportunidad de conocerlas."
    call BlinkXP ("c19s002_090" , "d") from _call_BlinkXP_2891
    sim "Sabes que hace unos diez años que vengo para el cumpleaños de las chicas, ¿verdad?"
    mc "Sí..."
    sim "¿Sabes de lo que hablaba [emm] en cada uno de ellos?"
    mc "¿De sus regalos? ¿De la comida? No sé..."
    call BlinkXP ("c19s002_095" , "d") from _call_BlinkXP_2892
    sim "Más o menos. Hablaba de qué le iban a regalar a ella, de si [mar] habría hecho su plato favorito..."
    sim "Básicamente era [emm] hablando de [emm]."
    mc "Muy típico de [emm]."
    call BlinkXP ("c19s002_100" , "d") from _call_BlinkXP_2893
    sim "¿Sabes de que ha hablado hoy mientras nos cambiábamos?"
    mc "De Amanda y de Eva. *Risa*"
    call BlinkXP ("c19s002_105" , "d") from _call_BlinkXP_2894
    sim "Después de intentar convencerme para que hiciera topless, sí. Ha sido su tema de conversación."
    mc "Han sido un cambio muy importante en casa..."
    call BlinkXP ("c19s002_110" , "d") from _call_BlinkXP_2895
    sim "Si han conseguido que [emm] deje de pensar sólo en [emm] es un cambio a mejor. *Risa*"
    sim "Con lo que ya me he formado una opinión de ellas. [emm] no me ha dejado otra opción. *Risa* Ahora estoy deseando que bajen para poder hablar con ellas."
    mc "Habrá tiempo de sobras después de comer, tranquila."
    call BlinkXP ("c19s002_115" , "d") from _call_BlinkXP_2896
    if not sim._var("route"):
        sim "Voy a la habitación de [emm]. Es un buen momento para empezar."
        mc "*Risa* Te puede el ansia. Yo voy a ver si hay algo más para bajar de la cocina. Te veo luego."
        sim "Hasta luego, [mc]."
        scene black with dissolve
        "Después de varios viajes a las cocinas, todo está preparado para empezar la fiesta."
        return
    sim "Creo que sería un buen momento para ir a hacer esa prueba, ¿no?"
    mc "Sí, la tengo en mi habitación."
    sim "Pues vamos. Cuanto antes la hagamos, antes lo sabremos."
    call BlinkXP ("c19s002_120" , "d") from _call_BlinkXP_2897
    stop music fadeout (1.5)
    "Una vez en tu habitación, con la sangre en el test, y éste guardado a buen recaudo..."
    play music ("music/Salsa.ogg")
    sim "Ahora toca esperar. Ya te dije que quería tener un par de hijos. No me importaría empezar joven."
    mc "Tendremos que esperar 24 horas para saberlo. Pero de momento, quiero un beso, y uno de verdad, no uno como en el saludo de antes."
    scene c19s002_120d with dissolve
    "No hace falta que lo repitas dos veces."
    "Desde aquel día en la sala de mantenimiento no habéis tenido tiempo para estar a solas."
    if sam._var("route"):
        "El tiempo en su casa, el día que te pilló con Samantha, no cuenta. No era el mejor día para poneros cariñosos."
    else:
        "El tiempo en el pasillo de su casa, el día que os pilló Samantha, no cuenta. Apenas tuvisteis dos minutos antes de que Samantha saliera."
        "Y después ya no hubo tiempo para poneros cariñosos."
    "Su lengua recorre tu boca con ansia. Parece mentira que sólo haga poco más de una semana desde vuestro último encuentro."
    call BlinkXP ("c19s002_125" , "d") from _call_BlinkXP_2898
    sim "Me encanta que cada beso siga siendo alucinante."
    mc "Espero que lo sigan siendo por mucho tiempo."
    call BlinkXP ("c19s002_130" , "d") from _call_BlinkXP_2899
    sim "Solo hay un problema con que seas tan bueno besando."
    mc "¿Y cuál es?"
    scene c19s002_135d with dissolve
    sim "Que me has dejado empapada."
    call BlinkXP ("c19s002_135" , "d") from _call_BlinkXP_2900
    sim "Voy a tener que dejar esto en algún sitio para que se seque."
    mc "¡Simone! Nos están esperando en la piscina..."
    call BlinkXP ("c19s002_140" , "d") from _call_BlinkXP_2901
    sim "Y quieres que baje a una piscina llena de mujeres que van a reconocer la humedad en esa zona, ¿verdad?"
    mc "No lo había pensado..."
    if sim._var("route") and emm._var("route"):
        sim "Ya nos ha pillado [emm], no quiero que [dap] y [eri] se enteren hoy también."
        sim "Además, [emm] nos ha dicho que nos cubriría."
    else:
        sim "No me importa quién lo sepa, pero prefiero que no sea mi regalo de cumpleaños para las chicas."
    call BlinkXP ("c19s002_145" , "d") from _call_BlinkXP_2902
    sim "Y parece que tú y yo estamos destinados a tener sexo rápido con el peligro de que nos pillen."
    mc "Un día tenemos que tener una cita normal..."
    call BlinkXP ("c19s002_150" , "d") from _call_BlinkXP_2903
    sim "Sí, tenemos que tenerla. De momento vamos a quitar ese bañador."
    mc "Yo aún no lo he mojado. *Risa*"
    scene c19s002_155d with dissolve
    sim "Y mejor que no lo hagas."
    scene c19s002_155e with dissolve
    sim "Hola, pequeñín."
    mc "¿Pequeñín? *Risa*"
    call BlinkXP ("c19s002_155" , "d") from _call_BlinkXP_2904
    sim "Mejor que llamarle Cockzilla, ¿no? *Risa*"
    mc "Yo prefiero Mjolnir. Y eres digna para levantarlo. *Risa*"
    call BlinkXP ("c19s002_160" , "d") from _call_BlinkXP_2905
    sim "Siéntate en la cama. Quiero hacer algo."
    mc "Lo que tú quieras... te veo muy decidida hoy."
    call BlinkXP ("c19s002_165" , "d") from _call_BlinkXP_2906
    sim "Después de lo difícil que fue besarte en la playa delante de Olivia y Betty... me atrevo con casi todo."
    mc "¿Vas a dejarte el top puesto?"
    sim "De momento, sí."
    call BlinkXP ("c19s002_170" , "d") from _call_BlinkXP_2907
    "Sigues sus instrucciones y te sientas en el borde de la cama. Crees que sabes lo que viene ahora."
    mc "Cuando quieras..."
    sim "Te va a parecer una tontería, pero vi esto en internet... al chico parecía gustarle..."
    mc "Probemos; no creo que sea el momento de que te entren dudas ahora."
    scene c19s002_175An with dissolve
    "Para tu sorpresa, en vez de arrodillarse entre tus piernas, Simone se gira y se sienta en tu regazo, empujando tu polla con sus glúteos."
    mc "Me gusta a dónde parece que va esto."
    sim "Ya te dije que es algo que vi en internet. No sé cómo saldrá o si lo haré bien."
    mc "De momento las vistas son inmejorables. *Risa*"
    scene c19s002_205pv with dissolve
    sim "A ver si te gustan en movimiento..."
    show c19s002_205v
    "Simone empieza un movimiento arriba y abajo, ajustando su posición para que sus cachetes abracen tu astil en vez de sólo empujarlo."
    mc "Me encanta, y no solo las vistas... Es una sensación diferente..."
    "Las vistas de su culo subiendo y bajando son hipnóticas. Podrías pasar horas mirándolo."
    sim "A mí también me está gustando... pero estoy acojonada."
    "Simone siempre ha tenido un culo increíble. Años de natación han forjado sus músculos a fuego."
    mc "¿Por qué?"
    scene c19s002_200pv with dissolve
    hide c19s002_205v
    show c19s002_200v
    "Te vas excitando cada vez más. Las sensaciones a lo largo de tu polla son alucinantes."
    sim "*Gemido* Cada vez que rozas mi agujero pequeño tengo miedo de equivocarme en el siguiente movimiento y que acabes dentro."
    "Una idea interesante, aunque desde tu perspectiva puedes asegurar que eso no puede pasar."
    sim "*Jadeo* Acabar con Cockzilla dentro no es mi objetivo para hoy..."
    "Te sorprendes. Mucho. Creías que era precisamente a dónde iba esto."
    scene c19s002_210pv with dissolve
    hide c19s002_200v
    show c19s002_210v
    sim "*Gemido* Al menos en ese agujero..."
    "Eso es otra cosa. Más lógico conociendo a Simone y su frase sobre tener sexo rápido."
    sim "*Jadeo* Me gusta esto, pero esperaba que fuera mejor..."
    "Está siendo muy bueno, al menos para ti, pero puedes entender que para ella no sea igual de bueno. Sus zonas erógenas están muy lejos de la zona de contacto."
    mc "Si quieres cambiamos de posición."
    sim "*Gemido* Me parece una buena idea... *Jadeo* Pese al miedo, hacer esto me ha puesto muy cachonda."
    scene c19s002_205dv with dissolve
    hide c19s002_200v
    "Simone se para al final de uno de sus movimientos."
    sim "Hoy quiero probar la postura de a cuatro..."
    mc "Lo que tú quieras, cielo. Tenemos toda la vida para probar todas las posturas que se te puedan ocurrir."
    scene c19s002_180d with fade
    "Ella se prepara en la cama, haciéndote levantar y retirando la colcha."
    sim "¿Te va bien que me ponga así? ¿Levanto más el culo?"
    "Es un culo precioso..."
    mc "No te preocupes. Nos adaptaremos en cuanto empecemos a movernos. Pero... ¿a qué ha venido lo de la colcha?"
    call BlinkXP ("c19s002_180" , "d") from _call_BlinkXP_2908
    sim "¿Para tener más tracción? *Risa* No sé... Mi única experiencia es en habitaciones de mantenimiento."
    sim "Ahí soy una maestra. *Risa* Las camas todavía no las domino."
    mc "*Risa* Pues vamos a empezar para que le cojas el tranquillo."
    scene c19s002_220pv with dissolve
    "Te arrodillas detrás de ella y apuntas tu glande a su entrada."
    show c19s002_220va
    pause (0.23)
    scene c19s002_220dv
    "En un movimiento rápido la penetras. Está empapada y te recibe con facilidad. Te viene a la mente la frase sobre un guante hecho a medida."
    sim "*Jadeo* ¡Ooof! Me acabas de romper. *Risa*"
    "Su risa reverbera en su túnel del amor. Puedes notar cada nota musical de su carcajada en tu astil."
    sim "Puedes empezar cuando quieras."
    scene c19s002_220pv with dissolve
    show c19s002_220v
    "Empiezas a bombear con tus caderas, tal como ella te ha pedido."
    sim "*Gemido* ¡Sí! Justo así..."
    "Su cuerpo se estremece con cada embestida, recibiendo tu astil con avidez."
    mc "¿Te gusta así?"
    "Aunque quisiera, no podría negarlo. Su cuerpo habla por ella con cada fibra de sus músculos."
    sim "*Gemido* Me gusta... me gusta más que la última vez."
    mcp "(A lo mejor te gusta más porque no es tu primera vez.)"
    scene c19s002_215pv with dissolve
    hide c19s002_220v
    show c19s002_215v
    "Como si te leyera el pensamiento, te saca de tu error."
    sim "*Jadeo* Y no tiene nada que ver con que fuera virgen. Me sigo notando tan rellena como el otro día."
    "Al menos esta vez es en una cama. La habitación de mantenimiento no era el mejor sitio para su primera vez."
    sim "*Gemido* ¡Justo ahí! *Jadeo* Así puedo notarte en todos mis puntos sensibles..."
    "El volumen y tono de sus gemidos te indica que ritmo llevar, con qué movimiento disfruta más."
    scene c19s002_230pv with dissolve
    hide c19s002_215v
    show c19s002_230v
    sim "*Jadeo* No pares... estoy a punto de llegar."
    "Eso significa que realmente le gusta más así. Crees recordar que la última vez tardó bastante más."
    sim "*Gemido* ¡Me encanta! *JADEO* ¡Quiero esto todos los días de mi vida!"
    "Será difícil lograrlo, apenas os veis, pero sabiendo que a Simone le encanta el sexo rápido y a escondidas... ¿quién sabe?"
    call OrgasmX ("c19s002_185") from _call_OrgasmX_63
    sim "*GEMIDO* ¡Me corroooo! *JADEO* ¡No pares!"
    "Todos los músculos de Simone, tensos hasta entonces, se ponen más rígidos todavía. Especialmente sus músculos vaginales, que aprisionan tu polla en su interior."
    sim "*JADEO* ¡Más duro! *GEMIDO* ¡Más rápido!"
    "Con sus paredes estrujando tu polla, las sensaciones se multiplican. Su coño es estrecho, pero mientras sus orgasmos recorren su cuerpo, se estrecha todavía más."
    scene c19s002_225pv with dissolve
    hide c19s002_230v
    show c19s002_225v
    "Continúas embistiendo su coño con tu polla como si de un ariete se tratara. Tus caderas impactando con su perfecto culo a cada embestida."
    sim "*JADEO* ¡Más profundo!"
    "Lo pide como si pudieras profundizar más todavía. Tus rodillas resbalan en las sábanas cuando llegas al final de tu embestida."
    sim "*GEMIDO* ¡Fóllame más duro!"
    mcp "(¿Fóllame? Definitivamente necesitamos una cita...)"
    "Se te ocurre una idea..."
    scene c19s002_190a with dissolve
    hide c19s002_225v
    sim "*Gemido* ¿Por qué te paras?"
    mc "Dame las manos."
    sim "*Jadeo* Me voy a comer el colchón si te las doy..."
    mc "¿No confías en mí?"
    scene c19s002_190An with dissolve
    "Simone confía en ti."
    "Te da las manos y su cabeza queda suspendida en el aire, a unos centímetros del colchón."
    sim "*Gemido* Oh... ahora veo lo que quieres hacer... Me gusta a dónde va esto..."
    scene c19s002_235pv with dissolve
    show c19s002_235v
    "Se acabaron los problemas de tracción. Ahora puedes llegar todo lo profundo que te permite Mjolnir utilizando sus brazos como punto de apoyo. ¡Bendito Arquímedes!"
    sim "*JADEO* ¡Jodel! *GEMIDO* ¡Así me gusta aún más!"
    "Parece que a Simone le gusta el sexo más duro, menos romántico, de lo que parecía. ¡Las sorpresas que puede dar una chica en su segunda vez!"
    sim "*GEMIDO* ¡Están volviendo! *JADEO* ¡No quiero que esto acabe!"
    "Por suerte para ambos, aún te queda un poco de gasolina en el depósito. No va a acabar todavía."
    scene c19s002_240pv with dissolve
    hide c19s002_235v
    show c19s002_240v
    "Hacerlo así es una sensación fantástica. Tienes el control absoluto sobre la velocidad y el ritmo."
    sim "*JADEO* ¡Ya están llegando! *GEMIDO* ¡No voy a poder bajar las escaleras!"
    "Notas en tu ástil, en tus manos y en tus caderas, cómo el cuerpo de Simone pasa por ciclos en los que se tensa y otros en los que se desmadeja."
    sim "*GEMIDO* ¡No puedo parar de correrme!"
    "Si no la tuvieras cogida por las manos, es posible que ya se hubiera derrumbado sobre la cama."
    scene c19s002_245pv with dissolve
    hide c19s002_240v
    show c19s002_245v
    "Con su coño exprimiendo tu polla, queriendo ordeñar la leche que está por llegar, tu límite se va acercando."
    sim "*JADEO* No voy a aguantar mucho más... *GEMIDO* Las piernas empiezan a fallarme."
    "Por suerte está ensartada en tu polla y la aguantas por los brazos. No tiene que hacer mucha fuerza con las piernas."
    "Pero tú tampoco vas a poder aguantar mucho más."
    sim "*GEMIDO* ¡Córrete dentro, por favor!"
    "Es una elección muy difícil: hacerle caso o pintar blanco sobre negro su espalda."
    if sim._var("pregnant"):
        $ sim._var("pregnancyDiscovered", True)
    if persistent.walkthrough:
        $ wt1 = _("Simone embarazada.")
        $ wt2 = _("Sin consecuencias.")
    else:
        $ wt1 = ""
        $ wt2 = ""
    menu:
        "Correrte dentro." (wt = wt2):
            $ Aux = True
        "Correrte dentro. Ir a por el bebé." (wt = wt1) if persistent.pregnancy and not sim._var("pregnant"):
            play sound ("music/OldMusicBox5.ogg")
            $ sim._var("pregnant", True)
            $ Aux = True
        "Correrte en su espalda" (wt = wt2):
            $ Aux = False
    $ resetWalkthrough ()
    if Aux:
        call OrgasmX ("c19s002_250") from _call_OrgasmX_64
        mc "¡Mpfft!"
        "Explotas en el interior de Simone mientras notas como tu descarga provoca una última oleada de orgasmos en su cuerpo, que intenta ordeñar hasta la última gota de tu semilla."
        call OrgasmX ("c19s002_255") from _call_OrgasmX_65
        sim "*GEMIDO* ¡Oh, Dios! ¡Este es enorme!"
    else:
        call OrgasmX ("c19s002_260") from _call_OrgasmX_66
        mc "¡Mpfft!"
        "Sales justo a tiempo antes de correrte, pintando de blanco la espalda y el culo de Simone."
    "Sus muñecas quedan flácidas en tus manos, mientras la aguantas para que no caiga en el colchón."
    stop music fadeout (1.5)
    call BlinkXP ("c19s002_265" , "d") from _call_BlinkXP_2909
    "La dejas caer suavemente, su cuerpo, roto y con toda la tensión perdida, se apoya dulcemente en el colchón."
    play music ("music/SensualJazzMedium2.ogg")
    if emm._var("route"):
        sim "Espero que [emm] haya inventado una buena excusa..."
    sim "Llevamos mucho tiempo aquí y deberíamos bajar. Esto ha sido alucinante. Dame un momento para que pueda levantarme y bajemos."
    mc "Estoy deseando que llegue el día en que nos podamos quedar abrazados después del sexo."
    sim "Yo también. Pero llegará."
    call BlinkXP ("c19s002_270" , "f") from _call_BlinkXP_2910
    "Después de limpiaros..."
    sim "¿Me ayudas a bajar las escaleras?"
    mc "¿Tan mal estás?"
    call BlinkXP ("c19s002_275" , "d") from _call_BlinkXP_2911
    sim "Me tiemblan las piernas y tu habitación está en el cuarto piso. *Risa* ¿Crees que voy a ser capaz de bajar sin ayuda?"
    mc "Si quieres te bajo en brazos. *Risa*"
    sim "No es necesario. *Risa* Con que te asegures de que no bajo rodando tengo suficiente."
    mc "¿Mejor tu segunda vez?"
    call BlinkXP ("c19s002_280" , "d") from _call_BlinkXP_2912
    sim "¡Muchísimo mejor! No tenía miedo y... cuando me has cogido de las muñecas... alucinante..."
    sim "De momento es mi postura favorita."
    mc "¿Sabes cuál es la mía?"
    call BlinkXP ("c19s002_285" , "d") from _call_BlinkXP_2913
    sim "¿Misionero? ¿Cowgirl?... No tengo ni idea..."
    mc "Los abrazos de después. Me gustaría que la próxima vez te quedaras a pasar la noche."
    call BlinkXP ("c19s002_290" , "d") from _call_BlinkXP_2914
    sim "Pero [mar]..."
    mc "Ya sabe que estamos juntos."
    sim "Las chicas..."
    if emm._var("route"):
        mc "[emm] ya lo sabe. Habría que pensar en decírselo al resto."
    else:
        mc "Habría que pensar en cuándo quieres decírselo al resto."
    mc "En la playa no te importó quién hubiera. No sé por qué te tiene que importar contárselo una vez pase este fin de semana."
    call BlinkXP ("c19s002_295" , "d") from _call_BlinkXP_2915
    sim "Me parece una buena idea. A ver si podemos decírselo un día de la semana que viene."
    sim "¿Bajamos?"
    mc "Vamos."
    stop music fadeout (1.5)
    scene black with dissolve
    if emm._var("route"):
        "[mar] te llama cuando pasas por delante de la cocina. Simone continúa bajando."
        play music ("music/MorningFunnyBeat.ogg")
        "Sigilosamente."
        "Sus piernas aguantan mejor de lo que ella pensaba."
        call BlinkXP ("c19s002_300" , "d") from _call_BlinkXP_2916
        mom "¿Puedes bajar esas cosas mientras acabo esto? Es lo último que queda por bajar."
        mc "¿Aún estás cocinando?"
        call BlinkXP ("c19s002_305" , "d") from _call_BlinkXP_2917
        mom "Sí, un imprevisto. Samantha estaba buscando a Simone hace un rato."
        mom "[emm] le ha dicho que estaba en el lavabo desde que se han cambiado... por lo visto la pobre chica tiene diarrea."
        mom "Le estoy haciendo un poco de arroz hervido. No va a poder comer la mayoría de las cosas que hemos preparado si está mal del estómago."
        mc "Pobre Simone, con lo que le gustan tus pasteles."
        mcp "(¿Algún tipo de broma por parte de [emm]? ¿O no se le ha ocurrido una excusa mejor para cubrirnos?)"
        mc "Vale, bajo esto. No tardes demasiado, o Tía Betty y Jamaal van a matar a alguien si no pueden empezar a comer."
        stop music fadeout (1.5)
        mom "Vale. Te veo abajo."
    scene black with dissolve
    "Cuando toda la comida está en la piscina, empieza la fiesta."
    return
label c19s003_Gifts:
    if _in_replay:
        menu:
            "¿Estás en una relación con Maddie?"
            "Sí":
                $ mad._var("route" , True)
                menu:
                    "¿Estás en alguna las rutas de dominación con Maddie?"
                    "Sí":
                        $ mad._var("dom" , True)
                        $ mad._var("romance" , False)
                    "No":
                        $ mad._var("romance" , True)
                        $ mad._var("dom" , False)
                        $ mad._var("sub" , False)
            "No":
                $ mad._var("route" , False)
                $ mad._var("dom" , False)
                $ mad._var("sub" , False)
                $ mad._var("romance" , False)
        menu:
            "¿Estás en una relación con [emm]?"
            "Sí":
                $ emm._var("route" , True)
            "No":
                $ emm._var("route" , False)
        menu:
            "¿Estás en una relación con Simone?"
            "Sí":
                $ sim._var("route" , True)
            "No":
                $ sim._var("route" , False)
    scene c19s003_005aa with fade
    play music ("music/Acoustic-Inspirational.ogg")
    if not _in_replay:
        $ oma.profileImages.pop (13) # first remove
        $ oma.profileImages.insert (13, ("alexia_13", None)) # then add new
        $ renpy.notify ("Profile Image unlocked for Alexia: 14 - Topless party")
    "En seguida se forman grupos de chicas para comer juntas. Esta vez, a diferencia de la comida de Navidad, no hace falta organizarlo como hizo Scarlett."
    "Todas quieren hablar con todas, especialmente con las que menos contacto tienen. [emm] está en su salsa."
    scene c19s003_005ba with fade #Mar*, Kim+, Megan
    "O con las que son más afines con ellas. Kim no es capaz de separarse de [mar] más de unos pocos minutos."
    scene c19s003_005ca with fade #Eri*, Lisa, Sam*
    if not _in_replay:
        $ eri.profileImages.pop (13) # first remove
        $ eri.profileImages.insert (13, ("erika_13", None)) # then add new
        $ texto = str(eri.name)
        $ renpy.notify ("Profile Image unlocked for "+str(texto)+": 14 - Topless party")
    "También hay grupos en los que no se puede intuir afinidad ninguna a simple vista, pero todo se desarrolla de buen rollo."
    scene c19s003_005da with fade #Betty+, Kate, Jamaal
    "O grupos realmente peligrosos a los que acercarse. Si te unes a ese trío sabes que vas a salir escaldado."
    scene c19s003_005fa with fade # Nor*, Eva+, Eileen*
    if not _in_replay:
        $ eil.profileImages.pop (13) # first remove
        $ eil.profileImages.insert (13, ("eileen_13", None)) # then add new
        $ renpy.notify ("Profile Image unlocked for Eileen: 14 - Topless party")
    "Eileen se ha perdido muchos de los últimos eventos debido a su trabajo, y no pierde oportunidad en asaltar a las chicas nuevas."
    scene c19s003_005ga with fade #Maddie*, Kiara+, Scarlett*,
    if not _in_replay:
        $ mad.profileImages.pop (13) # first remove
        $ mad.profileImages.insert (13, ("maddie_13", None)) # then add new
        $ renpy.notify ("Profile Image unlocked for Maddie: 14 - Topless party")
    "Maddie se ha convertido en la novedad y siempre está escoltada por una o dos chicas como mínimo para hacerla sentir a gusto."
    if mad._var("sub") or mad._var("dom"):
        "Pero hay algo en su actitud que dice que no se siente parte de todo esto."
    else:
        "Poco a poco se va integrando, pero está claro que esto es nuevo para ella."
    if not _in_replay:
        $ sca.profileImages.pop (13) # first remove
        $ sca.profileImages.insert (13, ("scarlett_13", None)) # then add new
        $ renpy.notify ("Profile Image unlocked for Scarlett: 14 - Topless party")
    "Es su primera visita a casa, al fin y al cabo."
    scene c19s003_005ea with fade #Dap*, Saira*, Debbie
    if not _in_replay:
        $ dap.profileImages.pop (13) # first remove
        $ dap.profileImages.insert (13, ("daphne_13", None)) # then add new
        $ texto = str(dap.name)
        $ renpy.notify ("Profile Image unlocked for "+str(texto)+": 14 - Topless party")
    "Lo mismo pasa con las chicas del cumpleaños. Es imposible pillarlas a solas en ningún momento."
    if not _in_replay:
        $ sai.profileImages.pop (13) # first remove
        $ sai.profileImages.insert (13, ("saira_13", None)) # then add new
        $ renpy.notify ("Profile Image unlocked for Saira: 14 - Topless party")
    scene c19s003_005ha with fade #Amanda*, Olivia+, Alexia*
    "Y Olivia no puede dejar pasar la oportunidad de pasar más tiempo con sus nuevas nietas. No te has dado cuenta de cuándo Amanda y Alexia se han hecho amigas."
    if not _in_replay:
        $ ama.profileImages.pop (13) # first remove
        $ ama.profileImages.insert (13, ("amanda_13", None)) # then add new
        $ renpy.notify ("Profile Image unlocked for Amanda: 14 - Topless party")
    if emm._var("route") and sim._var("route"):
        scene c19s003_005ia with fade #Emm*, Simone+
        "Puedes ver como [emm] le pasa comida a Simone a escondidas para paliar un poco su mierda de excusa."
    else:
        scene c19s003_005ab with fade
        "[emm] y Simone están conversando animadamente."
    "Decides acercarte a ellas."
    scene c19s003_010a with dissolve
    mc "¿Qué tal os lo estáis pasando, chicas?"
    emm "¡Genial! ¡Tener tanta gente en casa es alucinante!"
    sim "Está muy bien. Además, si miras a todo el mundo, te das cuenta de que no hay ningún mal rollo pendiente. Eso es rarísimo con tanta gente."
    if emm._var("route") and sim._var("route"):
        mc "¿Ningún mal rollo? ¿Ni siquiera por inventar excusas de mierda? *Risa*"
        scene c19s003_010b with dissolve
        sim "Se está portando bien para compensarme. *Risa* Me está trayendo comida de verdad que meto en el bol de arroz."
        emm "¡No es culpa mía! Si no os hubierais puesto a follar como conejos no hubiera tenido que inventar esa excusa de mierda."
        mc "Excusa de mierda... sobre diarrea. *Risa* ¿En qué estás pensando hoy, [emm]?"
        scene c19s003_010c with dissolve
        emm "*Risa* ¡No lo había pensado!" (multiple=2)
        sim "*Risa* ¡Es verdad!" (multiple=2)
        scene c19s003_010d with dissolve
        emm "Y no me digas que no pienso nunca. *Gruñido*"
        mc "No pensaba decirlo, no te preocupes. *Risa* Pero ¿puedo pensarlo aunque sea tu cumpleaños?"
    else:
        mc "Todos vamos con pies de plomo para no fastidiar el cumpleaños. *Risa* Imagínate a [emm] enfadada un día como hoy."
    call BlinkXP ("c19s003_015" , "d") from _call_BlinkXP_2918
    emm "Por mucho que lo intentéis, hoy no voy a enfadarme por nada. Toda la familia está aquí y eso es suficiente para pasárselo bien."
    emm "A menos que mi hermano me haga un regalo... de mierda. *Risa*"
    mc "Estoy seguro de que te va a gustar, no te preocupes. Aunque no lo puedas disfrutar hoy."
    call BlinkXP ("c19s003_020" , "d") from _call_BlinkXP_2919
    sim "¡Eso es cruel por tu parte, [mc]! *Risa*"
    if emm._var("route") and sim._var("route"):
        sim "Aunque se lo merezca por sus excusas de mierda."
    mc "También estoy seguro de que no le va a importar esperar para disfrutarlo."
    scene c19s003_010e with dissolve
    emm "Me voy a tener que fiar de ti, pero ahora estoy ansiosa. ¿Por qué todo el mundo come tan lento? *Risa* ¿No se dan cuenta de que cuanto más tarden en comer más tardaremos en recibir los regalos?"
    sim "Para tu próximo cumpleaños compra unos embudos y nos cebas a todos como a pollos. *Risa*"
    emm "Ve a meterles prisa, [mc]. *Risa* Diles que estoy a punto de sufrir un infarto por la ansiedad de saber qué me habéis regalado."
    if emm._var("route") and sim._var("route"):
        mc "Rara forma de comportarse para la adulta de la casa. *Risa*"
    mc "Vale, voy a ello. Os veo luego."
    scene c19s003_005db with fade #Betty+, Kate, Jamaal
    "Te acercas al grupo de los bromistas. Al menos bromistas cuando tú estás cerca y puedes ser el centro de sus bromas."
    "Quizás te salve que Kate y Jamaal aún no se conocen lo suficiente."
    mc "¿Qué tal lo estáis pasando por aquí?"
    jam "Bien hasta que has llegado. *Risa* Tengo a estas chicas tan guapas trayéndome comida y ahora la tendré que compartir contigo."
    bet "No te pases con [mc], Jamaal. *Risa* El pobre chico lleva un día de locos."
    kat "¿Un día? *Risa* Creo que cuando acabe la fiesta vendrán a buscarlo del manicomio más cercano."
    "De acuerdo. Nada te va a salvar de ser el centro de las bromas."
    mc "No te preocupes por la comida, Jamaal. Ya no como tanto como comía antes."
    call BlinkXP ("c19s003_025" , "d") from _call_BlinkXP_2920
    jam "Es una suerte para todos. Tienes que llevar una vida sana y dejarnos la comida a Betty, Kate, y a mí."
    mc "Estoy seguro de que comes más de lo que te toca y dejas a estas señoritas sin su parte."
    call BlinkXP ("c19s003_030" , "d") from _call_BlinkXP_2921
    kat "Yo no puedo comer mucho por tu culpa, [mc]. Me duelen tanto los brazos de tanto nadar que casi no puedo aguantar el plato. Y Jamaal es un devorador de rollitos."
    mc "Puedes usar a Jamaal de carrito de la comida. No se va a ir corriendo a ningún sitio y es bastante estable. Pero marca cuál es tu plato."
    call BlinkXP ("c19s003_035" , "d") from _call_BlinkXP_2922
    bet "No es mala idea. *Risa* Lo podemos llevar arriba y abajo en vez de dar tantos viajes nosotras. Le podemos poner una bandeja encima de las piernas y quitarle el pollo frito."
    mc "Sólo si lo queréis ver llorar. *Risa* Ese pollo lo hace [mar] casi exclusivamente para él."
    mc "Pero podéis aparcarlo al lado de la mesa de la comida. Así está a la sombra y no se le cuece el cerebro."
    scene c19s003_005dc with dissolve
    jam "Chicas, el trato consistía en meterse con [mc], no conmigo. ¡Y con mi pollo no se juega!"
    kat "Si no te hubieras comido el último rollito de calabacín, a lo mejor hubiera respetado el trato. *Risa*"
    bet "Pero es que serías un carrito de la comida fantástico. *Risa* Especialmente si te atamos las manos para que no comas. Nos ahorrarías muchos paseos."
    mc "Bueno, yo os dejo discutiendo la logística. Voy a saludar por allí."
    mcp "(Si no puedes con ellos, desvía la atención hacia uno de ellos.)"
    call BlinkXP ("c19s003_040" , "d") from _call_BlinkXP_2923
    bet "Luego tengo que hablar contigo, [mc]."
    mc "Cuando quieras, dime que necesitas."
    bet "Luego. En privado."
    mc "Perfecto. ¿Después de los regalos?"
    bet "Vale."
    scene c19s003_005bb with fade #Mar*, Kim+, Sam*
    mc "¿Cómo lo estáis pasando?"
    kim "¡Es impresionante! Nunca había estado en una fiesta familiar tan grande."
    mom "Todo está saliendo bien, la comida no está demasiado fría, ni la bebida demasiado caliente, con lo que no me puedo quejar. Cocinar para 24 personas es complicado."
    mom "No había cocinado para tanta gente desde que dejé de trabajar."
    sam "Y además teniendo que hacer opciones veganas para Lisa. [nor] y tu madre se han lucido."
    if emm._var("route") and sim._var("route"):
        sam "Por no hablar del arroz hervido para Simone a última hora. ¡Pobre hija mía! Se está perdiendo esta comida deliciosa."
    mc "Está todo genial, Mamá. ¿Cuántos sois en vuestras reuniones familiares, Kim?"
    call BlinkXP ("c19s003_045" , "d") from _call_BlinkXP_2924
    kim "Mi padre, mi madrastra, mi abuelo, mi hermano y yo."
    mcp "(No hay madre en esa frase...)"
    "Kim parece leerte el pensamiento sin que tengas que pronunciar una palabra."
    kim "Mi madre no está entre nosotros desde que nació mi hermano, cuando yo tenía dos años."
    call BlinkXP ("c19s003_050" , "d") from _call_BlinkXP_2925
    mom "¡Oh, mi niña! ¡No lo sabía! ¡Lo siento mucho!"
    kim "No pasa nada, [mar]. No la recuerdo. Solo he visto fotos y videos suyos. Era guapísima."
    mom "Como tú, mi niña. Como tú."
    call BlinkXP ("c19s003_055" , "d") from _call_BlinkXP_2926
    sam "Si algún día quieres hablar de ello, sabes que nos tienes aquí para lo que necesites."
    kim "Gracias, Samantha, pero ya os digo que no os tenéis que preocupar. Hace mucho..."
    mc "Puede que haga mucho, pero..."
    scene c19s003_005bc with dissolve
    kim "*Risa* Sí, [mc]. Hay que hablarlo todo. Lo sé."
    sam "Tu manía de hablarlo todo le ha devuelto la sonrisa. *Risa* Tenía que servir de algo."
    mom "¿Por qué no vas a ver cómo les va a Eva y Amanda? Creo que esta comida también puede ser un poco abrumadora para ellas siendo su primera fiesta... normal."
    mcp "(Eso es lo más parecido a ordenarme que las deje solas que voy a oír. No quiere que Kim se sienta mal, pero quiere hablar con ella sin que yo esté delante.)"
    mc "Voy a ver cómo se lo están pasando. Hablamos luego."
    scene c19s003_005fb with fade #Eva, Sca, Eil
    mc "Están dos pelirrojas y una rubia en la puerta de un garaje... casi podría parecer el inicio de un chiste."
    eva "Y una de las pelirrojas mata al humorista y se acaba el chiste. *Risa*"
    sca "No me acaba de gustar ese final, Eva. Yo estaba pensando en tirar al humorista a la piscina. *Risa*"
    eil "Esperad un momento... ¿Vosotras le habéis dado el beso de buenos días?"
    scene c19s003_005fc with dissolve
    eva "Cuando hemos llegado. Después de que [emm] nos presentara a Simone."
    sca "Yo esta mañana... cuando me lo he cruzado en la cocina."
    eil "Pues no os dejo que lo matéis ni que lo tiréis a la piscina antes de mi beso. *Risa*"
    call KissXP ("c19s003_060a" , "d") from _call_KissXP_93
    eil "Buenos días, [mc]."
    mc "Buenos días, Eileen."
    call BlinkXP ("c19s003_060b" , "d") from _call_BlinkXP_2927
    eil "Vale, todo vuestro. Merece una muerte horrible por empezar ese chiste. No puede definirnos por nuestro color de pelo. Yo soy algo más que una maravillosa pelirroja. *Risa*"
    call BlinkXP ("c19s003_065" , "d") from _call_BlinkXP_2928
    eva "Creo que su sangre podría estropear el cumpleaños un poquito. Ya sabes, Alexia tendría que investigar en vez de seguir disfrutando de la comida. *Risa*"
    eva "[mar] y [nor] se pondrían a limpiar. Es posible que alguna chica se pusiera triste... Mejor dejamos el asesinato para otro día. *Risa*"
    mc "Muy graciosa..."
    call BlinkXP ("c19s003_070" , "d") from _call_BlinkXP_2929
    sca "Y si lo tiramos a la piscina... ¿cuánto pesa? Seguro que salpica mucho y le moja la comida a alguien. *Risa*"
    mc "¡Por Dios! Creía que el grupo peligroso era el de Jamaal y Kate."
    scene c19s003_005fd with dissolve
    eil "Pobrecitos, suficiente tienen con aguantar el monokini de Jam. *Risa* Pero te lo tienes merecido por todos los años en los que te has metido con Jamaal."
    sca "Y Kate es un amor. Nunca se mete con nadie que no sea ella misma. *Risa*"
    eva "Bueno, yo tengo algunas grabaciones de Kate metiéndose con [mc]. *Risa* Son relevantes para vuestra protección. O, al menos, la de [mc]."
    eva "Esa chica puede ser una fiera. *Risa*"
    mc "*Risa* Me parece que voy a seguir mi ronda con el resto de las chicas. Algún sitio donde me dejen respirar."
    mc "Os veo luego. Y... Eva, luego quiero hablar en privado con Amanda y contigo. Después de los regalos."
    call BlinkXP ("c19s003_075" , "d") from _call_BlinkXP_2930
    eva "¿Sobre qué? Amanda y yo aún no hemos acabado de aclarar lo que hablamos anoche..."
    mc "¿Sabes lo malo de amenazar con asesinarme? Que ahora puedo tenerte intrigada hasta que tengamos esa conversación. *Risa*"
    mc "Y con ganas de más..."
    mc "Hasta luego chicas."
    scene c19s003_005cb with fade #Eri*, Megan, Lisa
    "Te giras sin darle tiempo a contestar (o a asesinarte) y te diriges al siguiente grupo."
    mc "Hola, chicas. Felicidades, [eri]. Antes te has llevado a Maddie tan rápido que no me ha dado tiempo de felicitarte."
    meg "¡Qué maleducado por tu parte, [mc]! *Risa* Y además llegas aquí y no nos das los buenos días a ninguna."
    lis "Dice que es el hombre de la casa y esas cosas. *Risa* Y tiene aquí a tres damiselas desatendidas."
    eri "Como es mi cumpleaños, reclamo el primer beso. *Risa* Después os lo presto un rato."
    call KissXP ("c19s003_080" , "d") from _call_KissXP_94
    mc "Felicidades, [eri]."
    eri "Gracias, [mc]. Más vale que las beses también a ellas si no quieres que no llegue a mañana a cumplir los 19."
    call KissXP ("c19s003_085" , "d") from _call_KissXP_95
    mc "Buenos días, Lisa. ¿Cuánto habéis bebido?"
    lis "Buenos días. Megan y [eri] no quieren beber, con lo que yo tengo que beber por las tres, ¿no?"
    mc "Sabes que no es necesario, ¿verdad?"
    lis "No te preocupes, tan solo he bebido tres copas de vino."
    call KissXP ("c19s003_090" , "d") from _call_KissXP_96
    mc "Buenos días, Megan. Gracias por lo de anoche en el Jazz Corner."
    meg "Buenos días, [mc]. Era el cumpleaños de tres de mis chicas favoritas, es lo menos que podía hacer."
    scene c19s003_005cc with dissolve #Eri*, Megan, Lisa
    mc "¿Estabais hablando de algo en lo que pueda participar? ¿O me vais a echar como han hecho el resto?"
    eri "Estábamos hablando del topless."
    meg "Se han apuntado muchas más chicas de lo que cualquiera de nosotras había pensado."
    lis "Y alguna que las tres pensábamos que lo haría, como Eva, no lo ha hecho."
    mc "¿Quién os ha sorprendido más de las que se han apuntado?"
    call BlinkXP ("c19s003_095" , "d") from _call_BlinkXP_2931
    eri "Yo no pensaba que [dap] fuera a hacerlo. Demasiada atención sobre ella el día que tiene que abrir los regalos."
    mc "Creo que era muy consciente de por qué lo pediste, con lo que creo que también quería apoyar a tu madre."
    eri "Es posible..."
    call BlinkXP ("c19s003_105a" , "d") from _call_BlinkXP_2932
    lis "A mí me ha sorprendido mucho Alexia. Cuando la conocí parecía tan seria y profesional, que no me la imaginaba así."
    lis "Después hemos hablado mucho y sé que es muy abierta y simpática, pero esa primera impresión sigue contando para mí."
    mc "Alexia puede ser una caja de sorpresas. Después iré a hablar con ella."
    call BlinkXP ("c19s003_100" , "d") from _call_BlinkXP_2933
    meg "A mí me ha sorprendido Kim. Si yo tuviera un cuerpo tan perfecto como el suyo, no dudaría en enseñarlo."
    mc "Estaba preocupada por ser la única en no hacerlo, y pese a todo no lo ha hecho, con lo que debe ser importante para ella."
    meg "Tienes razón, no lo había pensado así. ¿Y a ti? ¿Quién te ha sorprendido más?"
    mc "Samantha y Simone. Si me hubieran preguntado ayer, hubiera dicho que las dos habrían hecho justo lo contrario de lo que han hecho."
    scene c19s003_005cd with dissolve #Eri*, Megan, Lisa
    lis "Ahora sólo falta que se acabe la comida y empezar a abrir regalos. Tengo ganas de saber si hemos acertado con lo que les hemos regalado a las chicas."
    eri "Los regalos son lo de menos. Yo cambiaría todos los regalos por poder repetir esto más a menudo."
    meg "Tú quieres que no entre en ninguno de mis vestidos del trabajo. *Risa* [nor] y [mar] cocinan demasiado bien para mí."
    mc "Con los que somos aquí, habrá celebraciones de sobras solamente con los cumpleaños. Suma el 4 de julio, Acción de gracias, Navidad, Nochevieja..."
    mc "No vamos a ir cortos de celebraciones los próximos meses."
    scene c19s003_005ce with dissolve #Eri*, Megan, Lisa
    meg "Es fantástico, aunque tenga que comprar vestuario nuevo. *Risa*"
    lis "Tengo ganas de pasar Nochevieja con vosotros. Me gustan más las fiestas con vestido formal que en bikini, aunque me podría acostumbrar."
    eri "Pues te llevarás una sorpresa. Lo solemos celebrar en pijama. *Risa*"
    mc "¿No vais a volver a Aurora para Navidad?"
    call BlinkXP ("c19s003_105b" , "d") from _call_BlinkXP_2934
    lis "Debbie y yo hemos estado hablando sobre eso. Seguramente pasemos Acción de Gracias y Navidad con mis padres, pero querríamos estar aquí para Nochevieja."
    lis "Si no os importa, claro... no sé si el Dormitorio seguirá abierto durante las fiestas."
    mc "Creo que no habrá ningún problema con eso, Lisa."
    scene c19s003_005cf with dissolve #Eri*, Megan, Lisa
    meg "¿Os está apeteciendo tanto como a mí empezar a planear todas esas fiestas? *Risa*"
    eri "Es un poco pronto... pero ¡sí! *Risa*"
    lis "Aún no ha acabado tu cumpleaños y ya estamos hablando de las siguientes fiestas. *Risa* El cumpleaños de Debbie es en octubre..."
    mc "Antes van los de Simone y Scarlett. Ya os pasaré una lista, pero si os vais a poner a organizar más fiestas, os voy a dejar y seguir disfrutando de esta."
    mc "Os veo luego chicas."
    scene c19s003_005cg with dissolve #Eri*, Megan, Lisa
    todas "Hasta luego, [mc]."
    scene c19s003_005gb with fade #Maddie*, Kiara+, Nor*
    if not _in_replay:
        $ nor.profileImages.pop (13) # first remove
        $ nor.profileImages.insert (13, ("norah_13", None)) # then add new
        $ texto = str(nor.name)
        $ renpy.notify ("Profile Image unlocked for "+str(texto)+": 14 - Topless party")
    "Pasas a recargar el plato por la mesa de la comida y te acercas al siguiente grupo."
    mcp "(Me sorprende que Maddie se haya apuntado al topless siendo su primera vez en casa.)"
    mc "¿Qué tal lo estáis pasando?"
    nor "Genial, hay comida de sobras y todo el mundo está divirtiéndose. No se puede pedir más."
    kia "Me encantan estas celebraciones familiares. Eileen me había hablado de ellas hace años, pero no me las imaginaba así."
    mad "Es una inmersión forzada en vuestra familia. *Risa* Aunque conocía a la mayoría de la tienda, no habíamos tenido la oportunidad de hablar mucho."
    mc "Espero que no te parezcamos demasiado raros. *Risa*"
    scene c19s003_110d with dissolve
    mc "Veo que el hematoma de tu brazo ha mejorado mucho."
    call BlinkXP ("c19s003_110" , "d") from _call_BlinkXP_2935
    kia "Sí, el ungüento de Samantha ha obrado maravillas. Me ha dicho que amarilleará durante unos días y desaparecerá antes del próximo fin de semana."
    mc "Eso es fantástico. En una semana ya no nos acordaremos del hematoma."
    scene c19s003_005gc with dissolve #Maddie*, Kiara+, Nor*
    mad "¿Qué te pasó? ¿Te caíste? Tuvo que ser una caída muy fuerte..."
    "Le haces señas de que no continúe por ahí, pero llegas tarde."
    kia "No... es un tema... de mi pasado..."
    mc "Lo tienes que ver así. Algo que pasó y no volverá a pasar. Me ocupare... nos ocuparemos... de que no pase de nuevo."
    nor "Aquí estás segura y nadie te volverá a hacer daño. Todos te vamos a proteger"
    call BlinkXP ("c19s003_115" , "d") from _call_BlinkXP_2936
    mad "¡Oops! Lo siento, Kiara... no lo sabía..."
    mc "Mejor hablar de cosas más alegres, ¿no? Luego traeré tus regalos. Supongo que son los más voluminosos."
    scene c19s003_005gd with dissolve #Maddie*, Kiara+, Nor*
    nor "Creo que casi todo el mundo ha comido lo que podía comer ya, con lo que en veinte o treinta minutos haremos la entrega de regalos. Si quieres llevarlos a la pérgola, puedes hacerlo."
    kia "Yo tengo los míos en mi habitación. También tendré que ir a buscarlos."
    mad "Si quieres te ayudo a traerlos. No pesan, pero son incómodos de llevar para una sola persona."
    mc "Perfecto. ¿Vamos?"
    scene black with dissolve
    "Llevas los regalos de Maddie a la pérgola del fondo del jardín y vas a buscar los tuyos a tu habitación."
    scene c19s003_005hb with fade #Amanda*, Olivia+, Saira*
    "Después te acercas a algunas de las últimas chicas con las que no has hablado aún."
    mc "¿Qué tal chicas? ¿Ya no coméis?"
    sai "Estoy a punto de reventar. Y aún queda el pastel."
    ama "Con lo que había aquí se podría alimentar a un país pequeño. *Risa*"
    mee "Estas chicas están descubriendo cómo nos organizamos cuando hay comida por en medio. *Risa*"
    call BlinkXP ("c19s003_120" , "d") from _call_BlinkXP_2937
    sai "Pero es que es imposible no querer probarlo todo. Cada plato es más delicioso que el anterior."
    mc "Hay que hacer sacrificios y renunciar a cosas. Yo era una bola hasta que no lo aprendí. *Risa*"
    mc "Por ejemplo, va a haber tres pasteles. Solo hay que comer de uno de ellos. O una porción minúscula de cada una."
    call BlinkXP ("c19s003_125" , "d") from _call_BlinkXP_2938
    ama "Es lo que estaba diciéndole a Olivia. No sé cómo puede mantener una figura así, a su edad, si las comidas familiares son así."
    ama "Creo que me he engordado un par de kilos desde que os conozco."
    mc "Bueno, Meemaw tiene un truco, cuando no está con nosotros adelgaza rápidamente. *Pretendiendo susurrar* Cocina fatal cualquier cosa más allá de una ensalada. *Risa*"
    call BlinkXP ("c19s003_130" , "d") from _call_BlinkXP_2939
    mee "No es cierto del todo. No sabéis apreciar las cualidades del arroz duro o del filete carbonizado. *Risa*"
    mc "Si que sabemos. Como materiales de construcción son geniales. Como alimento... no tanto. *Risa*"
    scene c19s003_005hc with dissolve #Amanda*, Olivia+, Saira*
    sai "¿Y tú? ¿Cómo lo estás pasando? Te hemos visto ir como un pollo sin cabeza entre todas nosotras."
    ama "Parece que quieras hablar con todas nosotras, pero no te quedas más de cinco o diez minutos con cada grupo."
    mee "Es que [mc] sería el perfecto anfitrión en cualquier fiesta. Quiere que todo el mundo se sienta a gusto y se lo pase bien."
    mc "¿Acaso me perdonaríais si me quedara todo el día charlando con el mismo grupo?"
    scene c19s003_005hd with dissolve #Amanda*, Olivia+, Saira*
    ama "*Risa* No, tendríamos que secuestrarte."
    sai "Sólo te perdonaríamos si ese grupo fuese el nuestro. *Risa*"
    mee "Y entonces el resto de las mujeres de la familia vendrían a este grupo a secuestrarte y sería lo mismo. *Risa*"
    mee "Por alguna razón, todas queremos nuestra ración de [mc]."
    mc "Lo acabas de decir como si fuera el cuarto pastel de cumpleaños. *Risa*"
    scene c19s003_135a with fade
    "*Ding-Ding-Ding*"
    mar "¿Podéis prestarnos un momento de atención?"
    nor "Nos hemos dado cuenta de que nadie está comiendo ya."
    mar "Suponemos que os estáis reservando para los pasteles."
    nor "Con lo que sería el momento para que las chicas soplaran las velas."
    mar "Y nos comamos el pastel antes de que este calor lo derrita."
    mom "No os preocupéis. Hay más pasteles, no sólo estos tres."
    nor "Después, cuando todos vosotros estéis hartos de pastel, haremos la entrega de regalos y no os molestaremos más."
    todas "¡Sí!"
    scene c19s003_135b with fade
    "Las chicas soplan las velas rodeadas por los regalos mientras todo el mundo aplaude."
    "Se reparten las porciones de pastel y todo el mundo vuelve a sus conversaciones. Todas las chicas menos Betty piden una ración pequeña. Jamaal pide una ración grande de cada pastel."
    "Pruebas un pedacito MUY pequeño de cada uno. Como siempre, están deliciosos, pero la experiencia te ha enseñado que tres trozos normales son demasiados."
    "El niño gordo de tu pasado grita angustiado en tu mente."
    "Todo el mundo se vuelve a dividir en grupos para comer el pastel antes de abrir los regalos."
    scene c19s003_005eb with fade #Dap*, Alexia*, Debbie
    "Te diriges al grupo de [dap]. Aún no has tenido oportunidad de charlar con ellas."
    mc "¿Qué tal, chicas? ¿Ya os habéis comido el pastel?"
    deb "[dap] tiene prisa por que todo el mundo se lo acabe. Tiene ganas de abrir los regalos. *Risa* No nos ha prestado atención hasta que no nos hemos acabado el pastel."
    dap "Es lógico. Solo se cumplen 19 una vez. Bueno, en mi caso dos. Hoy y mañana. *Risa*"
    oma "Ahora solo falta que Jamaal y Betty se acaben los suyos. *Risa* Creo que la impaciencia está matando a [dap]."
    mc "Bueno, no hemos tenido tanta gente en una fiesta nunca. La comida está siendo mucho más larga."
    call BlinkXP ("c19s003_140" , "d") from _call_BlinkXP_2940
    dap "Y más gente son más regalos para abrir. *Risa* Va a llevar un rato..."
    mc "Y todavía quedará mucha tarde para seguir charlando."
    call BlinkXP ("c19s003_145" , "d") from _call_BlinkXP_2941
    deb "Y podríamos jugar a algo en la piscina. Estar tan cerca del agua y no meterme dentro me está matando."
    mc "Habló la sirenita. *Risa* Supongo que después de abrir los regalos habrá pasado el tiempo prudencial para bañarse después de comer."
    call BlinkXP ("c19s003_150" , "d") from _call_BlinkXP_2942
    oma "Las madres latinas siempre dicen que son dos horas desde que acabas de comer hasta que te puedes bañar. Espero que [mar] y [nor] no tengan genes latinos o sean más razonables."
    mc "Y que la apertura de regalos no dure tanto. *Risa*"
    scene c19s003_005ec with fade #Dap*, Alexia*, Debbie
    dap "Creo que todo el mundo ha acabado de comerse el pastel ya. Voy a preguntarle a mi madre si podemos abrir los regalos."
    mc "No te preocupes, ya voy yo a hacerlo."
    oma "¿Ya nos abandonas? Sólo has estado un par de minutos con nosotras."
    mc "Tu no quieres que a [dap] le entre un ataque de ansiedad, ¿verdad? *Risa* Pero no te preocupes, después de los regalos tendré tiempo para todas vosotras también."
    deb "Mejor que no. *Risa* Ve a preguntarle a [nor]."
    mc "Ahora vuelvo."
    scene black with dissolve
    "Preguntas a [mar] y [nor] sobre la apertura de regalos."
    "Como cada año se sorprenden de lo mucho que han aguantado las chicas antes de pedir permiso para abrirlos."
    "Todo el mundo se reúne alrededor de la pérgola para ver cómo reaccionan las chicas a cada uno de los regalos."
    scene c19s003_155a with dissolve
    "Todas las chicas reciben ropa. Mucha ropa. En la mayoría de los casos aciertan con sus gustos."
    "También reciben vales para ir a un spa, colonias, complementos..."
    "Todos los regalos son recibidos con sonrisas y abrazos de agradecimiento."
    scene c19s003_155b with dissolve
    if mad._var("route"):
        "Los cuadros de Maddie son una sensación. Las chicas están contentísimas con ellos y todo el mundo se ríe con lo adorable que está Zeus."
        "El cuadro de [dap] es diferente del que estaba pintando Maddie cuando estuviste en su casa. Le tienes que preguntar por qué."
    else:
        "Las cajas que ha traído Maddie son cuadros personalizados para las chicas. Les encantan y todo el mundo se ríe con lo adorable que está Zeus, el gato de Maddie."
    stop music fadeout (1.5)
    "Las chicas dicen que los colgarán en sus habitaciones antes de acabar el día."
    call BlinkXP ("c19s003_160a" , "d") from _call_BlinkXP_2945
    play music ("music/SaveMe.ogg")
    "[emm] es la primera en llegar a tu regalo para ella."
    emm "¿Un sobre, [mc]? No has sido tan cutre como para regalarme dinero, ¿verdad?"
    mc "*Risa* Ábrelo y lo sabrás. Pero no, no es dinero."
    call BlinkXP ("c19s003_160b" , "d") from _call_BlinkXP_2946
    emm "¿QUÉ? ¿Un vale de alquiler por un Ferrarini rosa? ¿Dónde has encontrado esto?"
    mc "En Monterey. Es el único en todo el estado fuera de LA."
    call BlinkXP ("c19s003_160c" , "d") from _call_BlinkXP_2947
    emm "¡Me encanta! Cuando el otro día dije que quería uno no creía que existieran de alquiler."
    mc "*Risa* Hace una semana que lo reservé. Tienes que usar el vale durante los próximos siete días."
    emm "¡Pues hay que organizar un viaje a Monterey! ¡Estoy impaciente!"
    call BlinkXP ("c19s003_165a" , "f") from _call_BlinkXP_2943
    "La siguiente en llegar a tu regalo es [dap]."
    dap "¡Hey! Esto pesa... ¿Qué es?"
    mc "Lo tendrás que abrir para saberlo. *Risa*"
    call BlinkXP ("c19s003_165b" , "h") from _call_BlinkXP_2944
    dap "¡Es el Super Gamertron 4090! ¡Es mejor que el portátil que quería comprarme!"
    mc "Pues ya no necesitas comprártelo. Ya puedes jubilar tu viejo portátil."
    dap "Pero te has pasado mucho. ¡Es carísimo!"
    call BlinkXP ("c19s003_165c" , "d") from _call_BlinkXP_2948
    dap "¡Gracias, [mc]! Es una auténtica pasada de portátil."
    mc "Disfrútalo, pero no te pases la vida encerrada en tu habitación jugando. *Risa*"
    dap "Tranquilo, no lo haré. Hay cosas demasiado buenas aquí fuera."
    call BlinkXP ("c19s003_170a" , "f") from _call_BlinkXP_2949
    "La última en llegar a tu regalo es [eri]."
    eri "¡Qué cajita más mona! ¿Un anillo?"
    mc "Tú también vas a tener que abrirlo para descubrirlo."
    scene c19s003_170d with dissolve
    eri "¡Oh! ¡Son preciosos!"
    scene c19s003_170e with dissolve
    eri "¡Me encanta el triskelion!"
    mc "Al representar la evolución de una persona, pasado, presente, y futuro, creo que te pegan. Los diseñé y los hice fabricar para ti."
    todas "¡Qué bonitos!"
    call BlinkXP ("c19s003_170b" , "d") from _call_BlinkXP_2950
    eri "Déjame ponérmelos un momento."
    call BlinkXP ("c19s003_170c" , "d") from _call_BlinkXP_2951
    eri "¡Muchas gracias, [mc]! ¡Se acaban de convertir en mis pendientes favoritos!"
    mc "Te quedan muy bien. Obsidiana sobre plata. Son tus colores."
    scene c19s003_155c with fade
    "Después de eso siguen abriendo más regalos y dando más abrazos hasta que se acaban las cajas."
    stop music fadeout (1.5)
    scene c19s003_175a with fade
    "Mientras unos cuantos ayudáis a las chicas a subir sus regalos a sus habitaciones, otros recogéis toda la comida y los platos sucios."
    play music ("music/ChillUkelele.ogg")
    "Vais a comer sobras durante unos días. [nor] y [mar] siempre cocinan demasiado."
    dap "Propongo una lucha de caballos en la piscina. Podemos hacer equipos..."
    mc "Mucho ejercicio después de comer, ¿no? Aunque yo me apunto."
    mcp "(Tan solo espero que no pase lo mismo que la última vez.)"
    emm "Yo montaré a [mc] como la última vez. ¡Somos invencibles! Lo siento, [eri]."
    eri "Podemos hacer equipos topless contra top. No sé si cuadran los números."
    scene c19s003_175b with dissolve
    nor "Conmigo no contéis. Yo necesito reposar la comida un rato."
    mee "Yo también... Como dice [mc], demasiado ejercicio después de comer. Necesito un poco de descanso a la sombra."
    kat "Yo me apunto, no he comido tanto como para perderme la diversión. Aunque es difícil decidir..."
    jam "Conmigo tampoco contéis. *Risa*"
    "Al final, tan solo doce decidís lanzaros a la piscina. Podréis hacer dos equipos de seis."
    return
label c19s004_PhoneMessage:
    if _in_replay:
        $ mc._var("relationships", 0, intention = "set")
        menu:
            "¿Estás en una relación con [dap]?"
            "Sí":
                $ dap._var("route" , True)
                $ mc._var("relationships", 1)
                menu:
                    "¿Está embarazada?"
                    "Si":
                        $ dap._var("pregnant" , True)
                    "No":
                        $ dap._var("pregnant" , False)
            "No":
                $ dap._var("route" , False)
        menu:
            "¿Estás en una relación con Scarlett?"
            "Sí":
                $ sca._var("route" , True)
                $ mc._var("relationships", 1)
                menu:
                    "¿Está embarazada?"
                    "Si":
                        $ sca._var("pregnancyDiscovered" , True)
                    "No":
                        $ sca._var("pregnancyDiscovered" , False)
            "No":
                $ sca._var("route" , False)
        menu:
            "¿Estás en una relación con Alexia?"
            "Sí":
                $ oma._var("route" , True)
                $ mc._var("relationships", 1)
                menu:
                    "¿Está embarazada?"
                    "Si":
                        $ oma._var("pregnancyDiscovered" , True)
                    "No":
                        $ oma._var("pregnancyDiscovered" , False)
            "No":
                $ oma._var("route" , False)
        menu:
            "¿Estás en una relación con Megan?"
            "Sí":
                $ meg._var("route" , True)
                $ mc._var("relationships", 1)
                menu:
                    "¿Está embarazada?"
                    "Si":
                        $ meg._var("pregnancyDiscovered" , True)
                    "No":
                        $ meg._var("pregnancyDiscovered" , False)
            "No":
                $ meg._var("route" , False)
        menu:
            "¿Estás en una relación con [mar!t]?"
            "Sí":
                $ mar._var("route" , True)
                $ mc._var("relationships", 1)
                menu:
                    "¿Está embarazada?"
                    "Si":
                        $ mar._var("pregnancyDiscovered" , True)
                    "No":
                        $ mar._var("pregnancyDiscovered" , False)
            "No":
                $ mar._var("route" , False)
        menu:
            "¿Estás en una relación con [nor]?"
            "Sí":
                $ nor._var("route" , True)
                $ mc._var("relationships", 1)
                menu:
                    "¿Está embarazada?"
                    "Si":
                        $ nor._var("pregnancyDiscovered" , True)
                    "No":
                        $ nor._var("pregnancyDiscovered" , False)
            "No":
                $ nor._var("route" , False)
        menu:
            "¿Estás en una relación con [emm]?"
            "Sí":
                $ emm._var("route" , True)
                $ mc._var("relationships", 1)
            "No":
                $ emm._var("route" , False)
        menu:
            "¿Estás en una relación con [eri]?"
            "Sí":
                $ eri._var("route" , True)
                $ mc._var("relationships", 1)
            "No":
                $ eri._var("route" , False)
        menu:
            "¿Estás en una relación con Eileen?"
            "Sí":
                $ eil._var("route" , True)
                $ mc._var("relationships", 1)
                menu:
                    "¿Está embarazada?"
                    "Si":
                        $ eil._var("pregnancyDiscovered" , True)
                    "No":
                        $ eil._var("pregnancyDiscovered" , False)
            "No":
                $ eil._var("route" , False)
        menu:
            "¿Estás en una relación con Samantha?"
            "Sí":
                $ sam._var("route" , True)
                $ mc._var("relationships", 1)
            "No":
                $ sam._var("route" , False)
        menu:
            "¿Estás en una relación con Simone?"
            "Sí":
                $ sim._var("route" , True)
                $ mc._var("relationships", 1)
            "No":
                $ sim._var("route" , False)
        menu:
            "¿Estás en una relación con Saira?"
            "Sí":
                $ sai._var("route" , True)
                $ mc._var("relationships", 1)
            "No":
                $ sai._var("route" , False)
        menu:
            "¿Estás en una relación con Debbie?"
            "Sí":
                $ deb._var("route" , True)
                $ mc._var("relationships", 1)
            "No":
                $ deb._var("route" , False)
        menu:
            "¿Estás en una relación con Maddie?"
            "Sí":
                $ mad._var("route" , True)
                $ mc._var("relationships", 1)
                menu:
                    "¿Estás en alguna las rutas de dominación con Maddie?"
                    "Sí":
                        $ mad._var("dom" , True)
                        $ mad._var("romance" , False)
                    "No":
                        $ mad._var("dom" , False)
                        $ mad._var("sub" , False)
                        $ mad._var("romance" , True)
            "No":
                $ mad._var("route" , False)
                $ mad._var("dom" , False)
                $ mad._var("sub" , False)
                $ mad._var("romance" , False)
        menu:
            "¿Has pre-abierto la relación con Meemaw?"
            "Sí":
                $ mee._var("route" , True)
            "No":
                $ mee._var("route" , False)
    scene c19s004_005a with dissolve
    play sound ("music/notification.ogg")
    "Mientras estáis discutiendo cómo distribuís los grupos, suena tu móvil"
    call BlinkXP ("c19s004_005a" , "d") from _call_BlinkXP_2952
    sam "Te acaba de sonar el móvil, [mc]. Un mensaje de texto."
    mc "Léemelo. La clave para desbloquearlo es el cumpleaños de Jamaal."
    call BlinkXP ("c19s004_005b" , "d") from _call_BlinkXP_2953
    sam "¿Estás seguro?"
    mc "No tengo ningún secreto que esconder. Puedes leerlo."
    call BlinkXP ("c19s004_010" , "d") from _call_BlinkXP_2954
    sam "Un pedido de Amazonian, una mesa. Llega mañana."
    mc "¿Ves como no era ningún secreto? *Risa*"
    mc "Lo que es raro es que solo llegue la mesa."
    play sound ("music/notification.ogg")
    "Suena el móvil de nuevo."
    stop music fadeout (1.5)
    mc "Si antes lo digo... Ese debe ser el otro pedido. ¿Puedes mirar cuando llega?"
    play music ("music/OneLastChance.ogg")
    call BlinkXP ("c19s004_015" , "d") from _call_BlinkXP_2955
    sam "No es de Amazonian... y no creo que quieras que lea este mensaje."
    mc "Puedes leerlo. Ya te he dicho que no tengo ningún secreto."
    sam "Es... privado..."
    mc "Léelo, Sam. Tengo las manos mojadas y no hay ningún secreto mío que no quiera que la familia conozca."
    call BlinkXP ("c19s004_020" , "d") from _call_BlinkXP_2956
    sam "A ver si hay suerte y hoy también te puedes librar de la zorra de tu novia y podemos volver a estar juntos. Lo de anoche fue alucinante."
    scene c19s004_025aAn with dissolve
    "Todo el mundo te mira sorprendido."
    call BlinkXP ("c19s004_020" , "d") from _call_BlinkXP_2957
    mc "¿Qué? ¿Quién lo manda?"
    if sai._var("route"):
        scene c19s004_030An with dissolve
        "Miras a Saira, quien niega con la cabeza, sorprendida."
    call BlinkXP ("c19s004_035" , "d") from _call_BlinkXP_2958
    sam "No la tienes entre los contactos. Sólo sale el número de teléfono."
    mc "No tengo ni idea de quién puede ser..."
    scene c19s004_040a with dissolve
    jam "He sido yo, Mamá. Era una broma privada." (multiple=2)
    bet "He sido yo, Samantha. Lo de anoche..." (multiple=2)
    mcp "(¿Qué?)"
    scene c19s004_025bAn with dissolve
    "Ahora es el momento en que todo el mundo mira a Betty y Jamaal con sorpresa e incredulidad en sus caras."
    mee "¡Betty!"
    scene c19s004_040b with dissolve
    jam "¡Tía Betty! No sabía que tú y [mc]..."
    bet "Lo llevamos en secreto... No tienes que mentir por mí, Jamaal..."
    play sound ("music/notification.ogg")
    "Suena el móvil una vez más."
    call BlinkXP ("c19s004_045" , "d") from _call_BlinkXP_2959
    sam "Otro mensaje del mismo número. Y ni Jamaal ni Betty tienen sus móviles en la mano."
    mc "Léelo, Sam."
    call BlinkXP ("c19s004_050" , "d") from _call_BlinkXP_2960
    sam "*Risa* No os lo vais a creer."
    mc "¿Qué pasa? ¿Qué dice el mensaje?"
    sam "Lo siento. Número equivocado."
    call BlinkXP ("c19s004_055" , "d") from _call_BlinkXP_2961
    mee "Betty, ¿nos explicas a todas por qué nos has mentido?"
    mee "¿O realmente estás haciendo... cosas... con [mc]?"
    call BlinkXP ("c19s004_060" , "d") from _call_BlinkXP_2962
    bet "No. No estamos haciendo \"cosas\"."
    bet "Pero he pensado que si alguna de estas chicas las está haciendo y había mandado ese mensaje por error sin saber que lo leería Samantha..."
    stop music fadeout (1.5)
    bet "Era una forma de cubrirla. Si no quieren que lo sepamos, un mensaje que lee la persona equivocada no debería destapar sus secretos."
    play music ("music/On-The-Rise.ogg")
    $ Aux = 0
    $ Aux2 = 0
    if eri._var("route"):
        $ Aux = 1
        call BlinkXP ("c19s004_065" , "d") from _call_BlinkXP_2963
        "[eri] te mira sonriendo un segundo antes de hablar. Asientes con la cabeza."
        eri "Lo siento, [dap]... [mc] y yo sí que estamos haciendo... cosas. Estamos saliendo."
        eri "Si Tía Betty es lo suficientemente valiente como para cargar con la culpa de un mensaje que no es suyo, yo debo ser lo suficientemente valiente como para hacerlo público."
        eri "No es como hubiera querido hacerlo público, pero creo que es el momento."
    elif emm._var("route"):
        $ Aux = 2
        call BlinkXP ("c19s004_070" , "d") from _call_BlinkXP_2964
        "[emm] te mira sonriendo un segundo antes de hablar. Asientes con la cabeza."
        emm "Lo siento, [dap]... [mc] y yo sí que estamos haciendo... cosas. Estamos saliendo."
        emm "Si Tía Betty tiene huevos para cargar con la culpa de un mensaje que no es suyo, yo debo tenerlos para hacerlo público."
        emm "No es como hubiera querido hacerlo público, pero creo que es el momento."
    elif dap._var("route"):
        $ Aux = 3
        call BlinkXP ("c19s004_075a" , "d") from _call_BlinkXP_2965
        "[dap] te mira sonriendo un segundo antes de hablar. Asientes con la cabeza."
        dap "Lo siento, chicas... [mc] y yo sí que estamos haciendo... cosas. Estamos saliendo."
        if dap._var("pregnant"):
            call BlinkXP ("c19s004_075b" , "d") from _call_BlinkXP_2966
            dap "Y una de las cosas que hemos hecho es un hijo."
            $ Aux2 = Aux2+1
        dap "Si Tía Betty es lo suficientemente valiente como para cargar con la culpa de un mensaje que no es suyo, yo debo ser lo suficientemente valiente como para hacerlo público."
        dap "No es como hubiera querido hacerlo público, pero creo que es el momento."
    elif mar._var("route"):
        $ Aux = 4
        call BlinkXP ("c19s004_080a" , "d") from _call_BlinkXP_2967
        "[mar] te mira sonriendo un segundo antes de hablar. Asientes con la cabeza."
        mom "Lo siento, chicas... [mc] y yo sí que estamos saliendo... me niego a decir \"haciendo cosas\"..."
        if mar._var("pregnancyDiscovered"):
            call BlinkXP ("c19s004_080b" , "d") from _call_BlinkXP_2968
            mom "Y estamos esperando un hijo."
            $ Aux2 = Aux2+1
        mom "Gracias por intentar cubrirnos, Tía Betty, pero ya es hora de que lo sepa toda la familia, aunque me hubiera gustado que fuera de otra forma."
    elif nor._var("route"):
        $ Aux = 5
        call BlinkXP ("c19s004_085a" , "d") from _call_BlinkXP_2969
        "[nor] te mira sonriendo un segundo antes de hablar. Asientes con la cabeza."
        nor "Lo siento, chicas... [mc] y yo sí que estamos saliendo... me niego a decir \"haciendo cosas\"..."
        if nor._var("pregnancyDiscovered"):
            call BlinkXP ("c19s004_085b" , "d") from _call_BlinkXP_2970
            nor "Y estamos esperando un hijo."
            $ Aux2 = Aux2+1
        nor "Gracias por intentar cubrirnos, Tía Betty, pero ya es hora de que lo sepa toda la familia, aunque me hubiera gustado que fuera de otra forma."
    elif sca._var("route"):
        $ Aux = 6
        call BlinkXP ("c19s004_090a" , "d") from _call_BlinkXP_2971
        "Scarlett te mira sonriendo un segundo antes de hablar. Asientes con la cabeza."
        sca "Lo siento, chicas... [mc] y yo sí que estamos haciendo... cosas. Estamos saliendo."
        if sca._var("pregnancyDiscovered"):
            call BlinkXP ("c19s004_090b" , "d") from _call_BlinkXP_2972
            sca "Y una de las cosas que hemos hecho es un hijo."
            $ Aux2 = Aux2+1
        sca "Si Tía Betty es lo suficientemente valiente como para cargar con la culpa de un mensaje que no es suyo, yo debo ser lo suficientemente valiente como para hacerlo público."
        sca "No es como hubiera querido hacerlo público, pero creo que es el momento."
    elif eil._var("route"):
        $ Aux = 7
        call BlinkXP ("c19s004_095a" , "d") from _call_BlinkXP_2973
        "Eileen te mira sonriendo un segundo antes de hablar. Asientes con la cabeza."
        eil "Lo siento, chicas... [mc] y yo sí que estamos saliendo... me niego a decir \"haciendo cosas\"..."
        if eil._var("pregnancyDiscovered"):
            call BlinkXP ("c19s004_095b" , "d") from _call_BlinkXP_2974
            eil "Y estamos esperando un hijo."
            $ Aux2 = Aux2+1
        eil "Gracias por intentar cubrirnos, Tía Betty, pero ya es hora de que lo sepa toda la familia, aunque no es la forma en que hubiera planeado hacerlo."
    elif sam._var("route"):
        $ Aux = 8
        call BlinkXP ("c19s004_100" , "d") from _call_BlinkXP_2975
        "Samantha te mira sonriendo un segundo antes de hablar. Asientes con la cabeza."
        sam "Lo siento, chicas... [mc] y yo sí que estamos saliendo... me niego a decir \"haciendo cosas\"..."
        sam "Gracias por intentar cubrirnos, Betty, pero ya es hora de que lo sepa toda la familia, aunque seguramente lo hubiera hecho de otra forma."
    elif sim._var("route"):
        $ Aux = 9
        call BlinkXP ("c19s004_105" , "d") from _call_BlinkXP_2976
        "Simone te mira sonriendo un segundo antes de hablar. Asientes con la cabeza."
        sim "Lo siento, chicas... [mc] y yo sí que estamos saliendo..."
        sim "Gracias por intentar cubrirnos, Tía Betty, pero ya es hora de que lo sepa toda la familia, aunque seguramente lo hubiera hecho de otra forma."
    elif oma._var("route"):
        $ Aux = 10
        call BlinkXP ("c19s004_110a" , "d") from _call_BlinkXP_2977
        "Alexia te mira sonriendo un segundo antes de hablar. Asientes con la cabeza."
        oma "Lo siento, chicas... [mc] y yo sí que estamos saliendo... me niego a decir \"haciendo cosas\"..."
        if oma._var("pregnancyDiscovered"):
            call BlinkXP ("c19s004_110b" , "d") from _call_BlinkXP_2978
            oma "Y estamos esperando un hijo."
            $ Aux2 = Aux2+1
        oma "Gracias por intentar cubrirnos, Tía Betty, pero ya es hora de que lo sepa toda la familia. Lo hubiera hecho de otra forma, pero sienta bien hacerlo sea como sea."
    elif meg._var("route"):
        $ Aux = 11
        call BlinkXP ("c19s004_115a" , "d") from _call_BlinkXP_2979
        "Megan te mira sonriendo un segundo antes de hablar. Asientes con la cabeza."
        meg "Lo siento, chicas... [mc] y yo sí que estamos saliendo... me niego a decir \"haciendo cosas\"..."
        if meg._var("pregnancyDiscovered"):
            call BlinkXP ("c19s004_115b" , "d") from _call_BlinkXP_2980
            meg "Y estamos esperando un hijo."
            $ Aux2 = Aux2+1
        meg "Gracias por intentar cubrirnos, Tía Betty, aunque no supieras quién era, pero ya es hora de que lo sepa toda la familia."
        meg "[mar] ya lo sabía, pero ahora lo sabéis todas."
    elif deb._var("route"):
        $ Aux = 12
        call BlinkXP ("c19s004_120" , "d") from _call_BlinkXP_2981
        "Debbie te mira tímidamente una décima de segundo antes de hablar. Asientes con la cabeza. Baja la mirada."
        deb "Lo siento, chicas... [mc] y yo sí que estamos haciendo... cosas. Estamos saliendo."
        deb "Si Tía Betty es lo suficientemente valiente como para cargar con la culpa de un mensaje que no es suyo, yo debo ser lo suficientemente valiente como para hacerlo público."
    elif sai._var("route"):
        $ Aux = 13
        call BlinkXP ("c19s004_125" , "d") from _call_BlinkXP_2982
        "Saira te mira sonriendo un segundo antes de hablar. Asientes con la cabeza."
        sai "Lo siento, chicas... [mc] y yo sí que hemos vuelto a estar juntos."
        sai "Si Tía Betty es lo suficientemente valiente como para cargar con la culpa de un mensaje que no es suyo, yo debo ser lo suficientemente valiente como para hacerlo público."
    elif mad._var("route"):
        $ Aux = 14
        call BlinkXP ("c19s004_130" , "d") from _call_BlinkXP_2983
        "Maddie te mira sonriendo un segundo antes de hablar. Asientes con la cabeza."
        if mad._var("romance"):
            mad "Lo siento, chicas... [mc] y yo sí que estamos saliendo."
        else:
            mad "Lo siento, chicas... [mc] y yo sí que estamos... teniendo algo."
    if mc._var("relationships")>1:
        "Sin dar tiempo a reaccionar a nadie, siguen las revelaciones. Una vez abiertas las puertas de los secretos va a ser difícil cerrarlas."
    if emm._var("route") and Aux < 2:
        call BlinkXP ("c19s004_070" , "d") from _call_BlinkXP_2984
        emm "También está saliendo conmigo."
    if dap._var("route") and Aux < 3:
        call BlinkXP ("c19s004_075a" , "d") from _call_BlinkXP_2985
        dap "Yo también estoy saliendo con [mc]."
        if dap._var("pregnant"):
            call BlinkXP ("c19s004_075b" , "d") from _call_BlinkXP_2986
            dap "Y estamos esperando un hijo."
            $ Aux2 = Aux2+1
    if mar._var("route") and Aux < 4:
        call BlinkXP ("c19s004_080a" , "d") from _call_BlinkXP_2987
        mom "[mc] y yo también estamos saliendo."
        if mar._var("pregnancyDiscovered"):
            call BlinkXP ("c19s004_080b" , "d") from _call_BlinkXP_2988
            mom "Y tenemos un hijo en camino."
            $ Aux2 = Aux2+1
    if nor._var("route") and Aux < 5:
        call BlinkXP ("c19s004_085a" , "d") from _call_BlinkXP_2989
        nor "Apuntadme al club de las chicas de la familia que salen con [mc]."
        if nor._var("pregnancyDiscovered"):
            call BlinkXP ("c19s004_085b" , "d") from _call_BlinkXP_2990
            nor "Llevo un hijo suyo dentro de mí."
            $ Aux2 = Aux2+1
    if sca._var("route") and Aux < 6:
        call BlinkXP ("c19s004_090a" , "d") from _call_BlinkXP_2991
        sca "Otra más que sale con [mc]."
        if sca._var("pregnancyDiscovered"):
            call BlinkXP ("c19s004_090b" , "d") from _call_BlinkXP_2992
            sca "Y vamos a traer a un hijo al mundo como nuevo miembro de la familia."
            $ Aux2 = Aux2+1
    if eil._var("route") and Aux < 7:
        call BlinkXP ("c19s004_095a" , "d") from _call_BlinkXP_2993
        eil "También nosotros estamos juntos. Otra vez."
        if eil._var("pregnancyDiscovered"):
            call BlinkXP ("c19s004_095b" , "d") from _call_BlinkXP_2994
            eil "Y añado otra pelirroja a la familia. Espero que sea niña y pelirroja, pero aún no lo sabemos."
            eil "Faltan pelirrojas en esta familia. Somos pocas."
            $ Aux2 = Aux2+1
    if sam._var("route") and Aux < 8:
        call BlinkXP ("c19s004_100" , "d") from _call_BlinkXP_2995
        sam "Nosotros también estamos saliendo."
    if sim._var("route") and Aux < 9:
        call BlinkXP ("c19s004_105" , "d") from _call_BlinkXP_2996
        sim "Yo también estoy saliendo con [mc]."
    if oma._var("route") and Aux < 10:
        call BlinkXP ("c19s004_110a" , "d") from _call_BlinkXP_2997
        oma "Otra más para el harén."
        if oma._var("pregnancyDiscovered"):
            call BlinkXP ("c19s004_110b" , "d") from _call_BlinkXP_2998
            oma "Y vais a ser tías también por mi parte."
            $ Aux2 = Aux2+1
    if meg._var("route") and Aux < 11:
        call BlinkXP ("c19s004_115a" , "d") from _call_BlinkXP_2999
        meg "Sumad otra."
        if meg._var("pregnancyDiscovered"):
            call BlinkXP ("c19s004_115b" , "d") from _call_BlinkXP_3000
            meg "Y espero que el hijo que llevo dentro cante mejor que [mc]."
            $ Aux2 = Aux2+1
    if deb._var("route") and Aux < 12:
        call BlinkXP ("c19s004_120" , "d") from _call_BlinkXP_3001
        if Aux2 > 0:
            deb "Una más aquí... pero no estoy embarazada."
            deb "Todavía no hemos hablado de hijos, pero viendo las caras que ponéis... espero daros una buena noticia algún día."
        else:
            deb "Una más aquí..."
    if sai._var("route") and Aux < 13:
        call BlinkXP ("c19s004_125" , "d") from _call_BlinkXP_3002
        sai "[mc] y yo hemos vuelto a estar juntos, pero de forma diferente a como estábamos en Portland."
    if mad._var("route") and Aux < 14:
        call BlinkXP ("c19s004_130" , "d") from _call_BlinkXP_3003
        if mad._var("romance"):
            mad "[mc] y yo también estamos saliendo."
        else:
            mad "[mc] y yo también estamos... teniendo algo."
    if Aux == 0:
        mc "No hacía falta que lo hicieras, Tía Betty. No estoy con nadie ahora mismo."
        call BlinkXP ("c19s004_135" , "d") from _call_BlinkXP_3004
        mee "Aparte de Betty mintiendo para proteger secretos ajenos..."
        call c19s004_Meemaw from _call_c19s004_Meemaw
    else:
        call BlinkXP ("c19s004_135" , "d") from _call_BlinkXP_3005
        call c19s004_Meemaw from _call_c19s004_Meemaw_1
    return
label c19s004_Meemaw:
    stop music fadeout (1.5)
    mee "¿Alguna sorpresa más?"
    play music ("music/pianomatic.ogg")
    mcp "(Está extrañamente tranquila. ¿La calma que precede a la tormenta?)"
    if mee._var("route"):
        mcp "(¿Va a confesar el millón de orgasmos de esta mañana? O mejor aún... ¿va a confesar que me ha dado la razón dos veces?)"
    todas "No..."
    mee "A mí ya no me sorprende nada de esta familia... Pero ahora dejadme hablar, por favor. SIN INTERRUPCIONES."
    call BlinkXP ("c19s004_140a" , "f") from _call_BlinkXP_3006
    mee "Yo también tengo algo que deciros."
    call BlinkXP ("c19s004_140b" , "d") from _call_BlinkXP_3007
    mee "Sé que algunas os vais a enfadar porque no os lo he dicho antes, pero no podía."
    call BlinkXP ("c19s004_140c" , "d") from _call_BlinkXP_3008
    mee "He tenido cáncer. Ya estoy limpia. Una semana antes de venir aquí acabé la quimio. Si salen los secretos a la luz, no soy quién para mantener ocultos los míos."
    mcp "(Alguno sí que te estás guardando... aunque no esperaba que te sincerases con todo el mundo hoy.)"
    call BlinkXP ("c19s004_140d" , "d") from _call_BlinkXP_3009
    mee "Como efecto secundario... tengo galactorrea. Para quién no sepa qué es, mi pecho produce leche aunque no esté embarazada."
    if mee._var("route"):
        mcp "(Un secreto menos... queda lo de los masajes y el millón de orgasmos.)"
    stop music fadeout (1.5)
    mcp "(Tiene que ser muy difícil confesar que ha estado guardando secretos todo este tiempo. No está diciendo durante cuánto tiempo los ha guardado, pero se lo preguntarán en breve.)"
    call BlinkXP ("c19s004_145a" , "d") from _call_BlinkXP_3010
    play music ("music/Rise-Up.ogg")
    emm "Estoy enfadada porque no nos lo has contado antes, pero la alegría porque estás limpia es mayor que el enfado."
    emm "Se ha convertido en el mejor regalo que hemos podido recibir cualquiera de nosotras hoy. Y no me refiero sólo a las que celebramos el cumpleaños."
    mcp "([emm], por extraño que parezca, resume el sentimiento general en la piscina.)"
    if Aux > 0:
        call BlinkXP ("c19s004_145b" , "d") from _call_BlinkXP_3011
        emm "Creía que nos ibas a decir que tú también salías con [mc]. *Risa*"
    call BlinkXP ("c19s004_145c" , "d") from _call_BlinkXP_3012
    emm "Ven aquí, dale un abrazo a tu nieta favorita. Pero no nos vuelvas a ocultar algo así."
    call BlinkXP ("c19s004_150" , "d") from _call_BlinkXP_3013
    mee "Ven tú. Yo estoy vieja y no me voy a meter en la piscina tan pronto después de comer. *Risa* Y ¿de dónde has sacado que seas la favorita?"
    scene c19s004_155aAn with dissolve
    emm "¿A quién puedes querer más que a mí?"
    scene c19s004_155An with dissolve
    "Todas las chicas se unen al abrazo que ha iniciado [emm]."
    "Algunas con los ojos húmedos."
    "Otras con enormes sonrisas."
    "Maddie da su apoyo mientras mantiene las distancias."
    "Tú eres el último en unirte. 22 personas sustituyéndose unas a otras para abrazar a Olivia es todo un reto logístico de brazos, tetas y cuerpos."
    call BlinkXP ("c19s004_160" , "d") from _call_BlinkXP_3014
    mc "¿No te unes, Jamaal?"
    jam "El único hueco que queda para llegar a Olivia y unirme comportaría pasar mi cara peligrosamente cerca de tu culo. No, no es una propuesta. *Risa*"
    if mc._var("relationships") > 1:
        jam "No quiero entrar en tu harén."
    jam "Pero tampoco quiero oler tus pedos. *Risa* Cuando dejéis a Olivia tranquila, ya vendrá a darle un abrazo a su nieto favorito."
    call BlinkXP ("c19s004_155b" , "d") from _call_BlinkXP_3015
    mee "Iré en cuanto me dejen respirar un poco, Jamaal."
    call BlinkXP ("c19s004_155c" , "d") from _call_BlinkXP_3016
    emm "¿A él no le preguntas de dónde ha sacado que sea tu nieto favorito?"
    call BlinkXP ("c19s004_155d" , "d") from _call_BlinkXP_3017
    mee "No hace falta. Él ya lo sabe. *Risa*"
    call BlinkXP ("c19s004_165" , "d") from _call_BlinkXP_3018
    jam "Por supuesto que lo sé. Y tú eres mi abuela favorita. Y más ahora que puedes darme leche para mis pastitas. *Risa* ¿En este cumpleaños no hay merienda?"
    if sam._var("route"):
        mc "¡Jam! Soy prácticamente tu padrastro. No sigas por ahí o te tendré que castigar sin pastitas. *Risa*"
    elif sim._var("route"):
        mc "¡Jam! Soy prácticamente tu cuñado. No sigas por ahí o tendré que hablar con mi suegra para que te castigue sin pastitas. *Risa*"
    else:
        mc "¡Jam! No sigas por ahí o tendré que hablar con [sam] para que te castigue sin pastitas. *Risa*"
    call BlinkXP ("c19s004_170" , "d") from _call_BlinkXP_3019
    jam "¡Hey! No es culpa mía. Es de [eri]."
    jam "Después de todo el día viendo tetas, mi cerebro gay está confuso."
    if mc._var("relationships") > 1:
        jam "No me extraña que no puedas elegir sólo a una. *Risa*"
    elif mc._var("relationships") == 1:
        jam "Casi podría envidiarte. *Risa*"
    else:
        jam "Y tú sin poder probar ninguna. *Risa*"
    call BlinkXP ("c19s004_175" , "d") from _call_BlinkXP_3020
    mee "No te preocupes, Jamaal, no me ofendo por tu broma de la leche. Cuando me la extraiga te la dejaré en el estante de arriba de la nevera."
    todas "*Risa*"
    mee "Tan solo espero que para mi cumpleaños no vengas con esa cosa verde que llevas puesta."
    mc "Meemaw, pero tu cumpleaños es en octubre... ¿Volverás de Florida para el cumpleaños?"
    call BlinkXP ("c19s004_180" , "d") from _call_BlinkXP_3021
    mee "Es otra cosa que quería deciros... Todavía estoy atando cabos y por eso no había dicho nada..."
    mee "Voy a vender la casa de Florida y me voy a mudar a Newport. Entre lo que saque por ella, mi pensión, y el sueldo de Betty, podremos comprar algo confortable."
    mee "Betty, aún no te había comentado nada... espero que no te importe mudarte aquí."
    call BlinkXP ("c19s004_190b" , "d") from _call_BlinkXP_3022
    bet "Ningún problema..."
    mcp "(¡Qué poca efusividad! Parece que le ha molestado...)"
    call BlinkXP ("c19s004_180" , "d") from _call_BlinkXP_3023
    mee "No voy a poder estar lejos de todas estas chicas maravillosas... ni de Jamaal."
    mc "*Risa* Eso me deja fuera a mí. Si lo sé no te defiendo. *Risa*"
    call BlinkXP ("c19s004_185" , "d") from _call_BlinkXP_3024
    mee "Tu estarás en Aruba en mi cumpleaños, cariño."
    mee "Solo espero que te puedas escapar y venir."
    call BlinkXP ("c19s004_190a" , "d") from _call_BlinkXP_3025
    "Se vuelve a repetir la escena de los abrazos a Meemaw, pero alguien se queda apartado."
    if mc._var("relationships")==1:
        "Parece que nadie recuerda la revelación previa. La noticia del cáncer de Meemaw y de su mudanza ha dejado tu relación como una anécdota."
    elif mc._var("relationships")>1:
        "Parece que nadie recuerda las revelaciones previas. La noticia del cáncer de Meemaw y de su mudanza ha dejado a tus relaciones como una anécdota."
    if Aux2 > 0:
        "Incluso que pueda haber nuevas incorporaciones a la familia parece que no va a recibir mucha atención."
    if mc._var("relationships")>0:
        "Es mejor así."
    stop music fadeout (1.5)
    "Todo el mundo está contento de que Meemaw y Betty no vuelvan a Florida."
    play music ("music/SadSoul.ogg")
    "Bueno... parece que todo el mundo no..."
    "Decides acercarte a Betty. Quería hablar contigo. ¿Será de esto? Pero Meemaw no se lo había comentado aún..."
    return
label c19s004_Betty:
    if _in_replay:
        menu:
            "¿En cuántas relaciones estás?"
            "Más de una":
                $ mc._var("relationships", 2, intention = "set")
            "Una":
                $ mc._var("relationships", 1, intention = "set")
            "Ninguna":
                $ mc._var("relationships", 0, intention = "set")
        if mc._var("relationships") > 0:
            menu:
                "¿Alguien reveló que estaba esperando un hijo tuyo?"
                "Sí, una chica":
                    $ Aux2 = 1
                "Sí, más de una chica" if mc._var("relationships") > 1:
                    $ Aux2 = 2
                "No":
                    $ Aux2 = 0
    call BlinkXP ("c19s004_200a" , "d") from _call_BlinkXP_3026
    mc "Gracias por lo de antes, Tía Betty."
    bet "No sé a lo que te refieres... yo no he hecho nada."
    mc "Bueno, pues gracias por NO intentar cubrirme cuando ha pasado lo del mensaje."
    call BlinkXP ("c19s004_200b" , "d") from _call_BlinkXP_3027
    bet "Ya te digo que no he hecho nada que no hubiera hecho cualquier tía abuela por su sobrino nieto favorito."
    mc "¿Ha pasado algo, Tía Betty? Te veo... ¿triste?"
    call BlinkXP ("c19s004_200c" , "d") from _call_BlinkXP_3028
    if mc._var("relationships") > 1:
        bet "Felicidades por haber salido a la luz con tus chicas, aunque no hayas tenido mucho que ver."
    elif mc._var("relationships") == 1:
        bet "Felicidades por haber salido a la luz, aunque no hayas tenido mucho que ver."
    if mc._var("relationships") > 0:
        bet "Excepto tu pequeño asentimiento antes de la revelación. Creo que le ha pasado desapercibido a la mayoría."
    if Aux2 > 0:
        bet "Y felicidades por tu futura paternidad."
        mc "Gracias, pero..."
    mc "No parece que te alegres demasiado. Y no has respondido a mi pregunta."
    call BlinkXP ("c19s004_205a" , "d") from _call_BlinkXP_3029
    bet "No es eso... es que la sobredosis de noticias me ha dejado un poco anonadada."
    if mc._var("relationships") > 0:
        call BlinkXP ("c19s004_205b" , "d") from _call_BlinkXP_3030
        bet "Has tenido suerte que la revelación de Olivia haya desviado la atención sobre la tuya."
        if mc._var("relationships") > 1:
            bet "Podrías haberte encontrado con un problema con las noticias simultáneas y con las chicas a las que les gustaría poder dar una noticia similar y a las que no has hecho mucho caso."
            mc "Si te refieres a Kiara, aún no hemos tenido la oportunidad de hablar..."
            call BlinkXP ("c19s004_210" , "d") from _call_BlinkXP_3031
            bet "No solo a Kiara, cielo... Ver a toda la familia aquí, y ver cómo te miraban las que no tenían noticias que dar sobre ti..."
            bet "Alguna parecía querer estar en posición de poder darla."
            mc "Tú tampoco tenías ninguna noticia que dar sobre mí. *Risa* ¿También te hubiera gustado?"
            call BlinkXP ("c19s004_215" , "d") from _call_BlinkXP_3032
            bet "No apliques mi psicología contra mí. *Risa triste*"
        bet "Hoy han salido a la luz noticias importantes que una vieja monja nunca podrá igualar."
        mc "No es una competición para ver quién da la noticia más grande."
        mc "Por raro que parezca, me parece más importante la noticia de Meemaw. Que quiera confiar en todos nosotros y la mudanza. Creo que la mudanza te ha sorprendido incluso a ti."
    else:
        mc "La mudanza y el cáncer. Creo que la mudanza te ha sorprendido incluso a ti."
    call BlinkXP ("c19s004_220" , "d") from _call_BlinkXP_3033
    bet "Un poco..."
    mcp "(Obviamente le pasa algo de lo que no quiere hablar tan cerca del resto.)"
    mc "Antes has dicho que querías hablar conmigo. ¿Te parece un buen momento?"
    bet "Sí, pero... ¿podemos ir a sentarnos?"
    mc "Por supuesto."
    call BlinkXP ("c19s004_225" , "f") from _call_BlinkXP_3034
    mc "Dime, ¿de qué querías hablar?"
    bet "Desde que te lo he dicho han cambiado tanto las cosas..."
    bet "Esta mañana he ido a misa... con el coche de [nor]."
    mc "Muy valiente por tu parte. *Risa*"
    call BlinkXP ("c19s004_230" , "d") from _call_BlinkXP_3035
    bet "*Risa triste* Sí... es más viejo aún que yo... o al menos tiene más achaques..."
    mc "No eres vieja, Tía Betty... digamos que eres vintage. *Risa* Pero aún estás muy bien... de salud, me refiero."
    call BlinkXP ("c19s004_235" , "d") from _call_BlinkXP_3036
    bet "Bueno... hoy me he saltado un Stop al volver de misa. No ha pasado nada grave, excepto que me ha parado la policía."
    mc "¿Estás así por una multa? No pasa nada. A Mamá le ponen como mínimo una al mes."
    call BlinkXP ("c19s004_240" , "d") from _call_BlinkXP_3037
    bet "No es por la multa... cuando el agente me ha pedido la documentación... mi permiso de conducir está caducado desde hace más de un año."
    bet "Ni me había dado cuenta de cuándo caducaba."
    bet "El agente ha sido muy amable y me ha dejado volver a casa conduciendo, pero voy a tener que hacer unas gestiones en la DMV para renovar la licencia."
    mc "Y quieres que te lleve a renovarla, no hay ningún problema."
    call BlinkXP ("c19s004_245" , "d") from _call_BlinkXP_3038
    bet "No hace falta. Me ha dicho que lo puedo hacer online, pero no voy a poder conducir hasta que llegue el nuevo permiso."
    bet "Y aquí es donde se pone raro. Te iba a pedir que me llevases a Monterey antes de saber lo que le habías regalado a [emm]."
    mc "¿A Monterey? ¿Qué tienes que hacer allí? No hay ningún problema en llevarte. No lo habría aunque no le hubiera regalado el alquiler a [emm]."
    call BlinkXP ("c19s004_250" , "d") from _call_BlinkXP_3039
    bet "¿Qué te han contado de por qué dejé África?"
    mc "Nada. Creía que volviste para unas vacaciones o algo así y te quedaste por lo de Meemaw."
    call BlinkXP ("c19s004_255" , "d") from _call_BlinkXP_3040
    bet "Volví porque me expulsaron de Tanzania..."
    bet "No del país, sino de la Iglesia de allí. Me abrieron expediente... por enfrentarme a un Obispo local."
    mc "¿Qué hiciste, Tía Betty?"
    call BlinkXP ("c19s004_260" , "d") from _call_BlinkXP_3041
    bet "Negarme a operar el cerebro de alguien para curarle la homosexualidad. O lobotomizarlo si no era posible hacerlo."
    mc "¿Qué? ¿Eso aún pasa?"
    call BlinkXP ("c19s004_265" , "d") from _call_BlinkXP_3042
    bet "No, no pasa. Pero el Obispo quería demostrar al jefe de uno de los kraal, aldeas Masái, que aún sigue religiones tradicionales, el poder de Cristo..."
    bet "Aunque fuera de una forma rastrera y mintiéndole. Si el jefe se convertía, parte del kraal también lo haría... y el hijo gay de un jefe era una oportunidad."
    bet "Mucha gente en Tanzania piensa que la homosexualidad no está bien y que los homosexuales no tienen lugar en la sociedad."
    bet "Un jefe con un hijo gay, por muy integrado que esté en la sociedad tanzana, tiene un problema grave."
    mc "¡Eso es terrible! ¿Qué pasó?"
    call BlinkXP ("c19s004_270" , "d") from _call_BlinkXP_3043
    bet "Que me negué a operar un cerebro completamente sano para buscar algo que no se puede extirpar."
    bet "Se lo dije al jefe y al chico, y eso llevó a problemas con el Obispo."
    bet "Él sabe que estaba mintiendo, pero en vez de reconocerlo, me echó las culpas a mí y consiguió que la Iglesia me echara de allí. Había socavado su imagen."
    mc "Pero podrías haberte quedado aunque no fuera trabajando para la Iglesia, ¿no?"
    call BlinkXP ("c19s004_275" , "d") from _call_BlinkXP_3044
    bet "No, [mc]. El permiso de residencia y trabajo lo tenía gracias a la Iglesia. Puedo visitar el país a nivel particular, pero no trabajar allí."
    bet "Y adoro ese país."
    mc "Lo que no entiendo es qué tiene esto que ver con la visita a Monterey."
    call BlinkXP ("c19s004_280" , "d") from _call_BlinkXP_3045
    bet "Hoy he estado hablando con el Padre Matthews en la iglesia. Me ha dicho que mis papeles han llegado ya desde Florida y que debería ir al Obispado de Monterey."
    bet "Como visita de cortesía y para informarme sobre cómo está mi expediente."
    mc "¿Tus papeles? No lo entiendo. ¿Tienes que informar a la Iglesia de dónde vives?"
    call BlinkXP ("c19s004_285" , "d") from _call_BlinkXP_3046
    bet "Normalmente no. Pero con un expediente sancionador en curso... Es lo mejor. No quiero parecer una monja rebelde más de lo que ya lo parezco."
    mc "Lo entiendo. No hay ningún problema. Puedo llevarte cuando vaya con [emm]. *Risa* Aunque no iremos al Obispado con el Ferrarini."
    call BlinkXP ("c19s004_290" , "d") from _call_BlinkXP_3047
    bet "*Risa* No, no quedaría muy profesional."
    mc "¿Y por eso estás tan... triste? ¿Una multa y una visita al Obispado?"
    call BlinkXP ("c19s004_295a" , "d") from _call_BlinkXP_3048
    bet "No es eso. Me siento inútil. Hace un año que no piso un quirófano. Lo intenté en Florida. Hay buenos hospitales católicos allí."
    bet "Y me dijeron que no podían darme ningún puesto hasta que no se resolviera mi expediente."
    call BlinkXP ("c19s004_295b" , "d") from _call_BlinkXP_3049
    bet "Llevo un tiempo pensando que quizás acabe relegada en un convento. E ir a Monterey me tiene asustada."
    mc "¿Van a perder una cirujana porque te negaste a operar lo inoperable?"
    call BlinkXP ("c19s004_300a" , "d") from _call_BlinkXP_3050
    bet "No, es posible que releguen a una monja rebelde que desobedeció una orden de un Obispo. Y, además, lo dejó en mal lugar."
    bet "Para ellos, puedo seguir sirviendo a Dios en un convento igual que lo hago en un quirófano."
    mc "¿Incluso si había razones médicas para hacerlo?"
    call BlinkXP ("c19s004_300b" , "d") from _call_BlinkXP_3051
    bet "A los Obispos eso les da lo mismo. Piensa en ellos como políticos más que como sacerdotes."
    mc "Y que Meemaw diga que cuenta con tu sueldo para la mudanza es la gota que ha colmado el vaso, ¿no?"
    call BlinkXP ("c19s004_305" , "d") from _call_BlinkXP_3052
    bet "Más o menos. Desde que llegué a Florida estoy cobrando un sueldo reducido, hasta que se resuelva el expediente. Es suficiente para colaborar, pero no para lo que quiere Olivia."
    bet "Si acabo en un convento será aún menos. Si depende de mi sueldo..."
    mc "Si depende de tu sueldo y éste desaparece o se reduce, el resto de la familia colaboraremos."
    mc "Tenemos una empresa millonaria. Supongo que como CEO tendré un sueldo... algo más alto que el de una monja."
    call BlinkXP ("c19s004_310" , "d") from _call_BlinkXP_3053
    bet "Es tan fácil olvidarse de eso..."
    mc "Vale. Un problema resuelto. El permiso de conducir lo renovaremos mañana online. El transporte a Monterey también está resuelto. Hay que llevar a [emm] de todos modos."
    bet "Las casualidades que pasan en esta familia..."
    mc "¿Algún problema más del que quieras hablar?"
    call BlinkXP ("c19s004_315" , "d") from _call_BlinkXP_3054
    bet "No, pero un abrazo sí que aceptaría..."
    mc "De esos tengo muchos y no se van a agotar."
    call BlinkXP ("c19s004_320" , "f") from _call_BlinkXP_3055
    bet "Gracias por ayudar a esta vieja, [mc]. Te has convertido en el hombre de la casa sin que nadie se diera cuenta. Sin que nadie te lo pidiera."
    bet "Cada día que pasa te pareces más a John..."
    if Aux2 > 0:
        bet "Y ahora además también vas a ser padre. No sé cuándo vas a tener tiempo para ti."
    bet "Tienes que guardar tiempo para hacer las cosas que te gustan o al final explotarás."
    mc "Ya lo hago, Tía Betty. Dar abrazos es uno de mis mayores hobbies."
    call BlinkXP ("c19s004_325" , "d") from _call_BlinkXP_3056
    bet "*Risa* Te conformas con poco."
    mc "Si el dormitorio no me da más trabajo que hacer la contabilidad y la compra, me tengo que buscar entretenimientos, ¿no? *Risa*"
    mc "Y estar con mis chicas es una de las mejores cosas que hay. Sois 22 aquí. No puedo pedir estar mejor acompañado."
    mc "Incluso Jamaal está bien para pasar un rato. *Risa* Pero a él no voy a darle abrazos."
    call BlinkXP ("c19s004_330" , "d") from _call_BlinkXP_3057
    bet "Debería dejarte ir o el resto de las chicas me van a odiar por acapararte."
    mc "Deberías disfrutar el abrazo y callar. Después puedes hablar con Scarlett sobre la app que usó anoche. Se acabarían los problemas de acaparamiento."
    bet "¿Qué app?"
    "Le explicas la app de los turnos de baile. Alargas la explicación innecesariamente para estar más rato abrazado a ella."
    "La mujer que siempre da apoyo a los demás necesita apoyo hoy."
    call BlinkXP ("c19s004_335" , "f") from _call_BlinkXP_3058
    "Al cabo de un largo rato, se separa de ti reluctantemente."
    bet "Creo que ahora sí que debería dejarte... pero antes..."
    call KissXP ("c19s004_340" , "d") from _call_KissXP_97
    bet "Gracias por todo, [mc]. Deberías cobrar por esos abrazos."
    mc "Ese beso me parece un buen pago. *Risa*"
    scene c19s004_340c with dissolve
    bet "De esos tengo muchos y no se van a agotar."
    stop music fadeout (1.5)
    mcp "(Espero que Eva y tú no habléis demasiado. Me acabas de recordar a lo que hizo anoche.)"
    play music ("music/Sad-Piano.ogg")
    mcp "(¡Oh, mierda! Me había olvidado de que le había dicho que tenía que hablar con ella y con Amanda! Hora de hacerlo)"
    return
label c19s004_AmandaEva:
    if _in_replay:
        menu:
            "¿En cuántas relaciones estás?"
            "Más de una":
                $ mc._var("relationships", 2, intention = "set")
            "Una":
                $ mc._var("relationships", 1, intention = "set")
            "Ninguna":
                $ mc._var("relationships", 0, intention = "set")
        if mc._var("relationships") > 0:
            menu:
                "¿Alguien reveló que estaba esperando un hijo tuyo?"
                "Sí":
                    $ Aux2 = 1
                "No":
                    $ Aux2 = 0
    call BlinkXP ("c19s004_400" , "f") from _call_BlinkXP_3059
    "Pillas a Amanda a solas, volviendo de la casa. El resto de las chicas siguen alrededor de Meemaw."
    if mc._var("relationships")>0:
        "Se han formado grupos, supones que comentando todas las revelaciones del día."
    "Nadie se acuerda ya de la lucha de caballos a la que ibais a jugar."
    mc "Amanda, ¿puedo veros a ti y a Eva en mi habitación en cinco minutos?"
    ama "¿Para qué? Aún no hemos acabado de concretar lo que hablamos anoche..."
    mc "No tiene que ver con lo de anoche, no te preocupes."
    mc "¿Vas a buscarla y os veo arriba?"
    call BlinkXP ("c19s004_405" , "d") from _call_BlinkXP_3060
    ama "De acuerdo, voy a avisarla."
    scene c19s004_410a with fade
    "Unos minutos después..."
    ama "¿Qué necesitas, [mc]?"
    eva "¿Es urgente? Las chicas... la fiesta..."
    mc "Van a ser dos minutos. Tengo algo para vosotras."
    scene c19s004_410b with dissolve
    eva "¿Para nosotras?" (multiple=2)
    ama "¿Qué es? ¿Algo sobre NTR?" (multiple=2)
    mc "No os conocía en vuestro cumpleaños, con lo que he pensado que sería una buena idea dároslo hoy."
    mc "No es nada... importante... Tan solo algo que se me ocurrió."
    scene c19s004_410c with dissolve
    mc "Son esas dos cajas que hay encima de la mesa."
    mc "La caja púrpura es para Eva y la azul para Amanda."
    scene c19s004_410d with dissolve
    "Las chicas casi corren hacia las cajas. Las sopesan y escuchan en su interior."
    scene c19s004_415An with dissolve
    "Las caras de sorpresa cuando las abren valen la pena. No sabes lo que esperaban, pero desde luego no lo que hay en las cajas."
    ama "¿Le has dicho algo?"
    eva "Salió la conversación el otro día..."
    call BlinkXP ("c19s004_420" , "f") from _call_BlinkXP_3061
    eva "Tengo que sentarme..."
    "No es el efecto que esperabas... A lo mejor la cara de sorpresa no era por una \"buena sorpresa\"."
    mc "¿No os gustan? Creía que..."
    scene c19s004_425d with dissolve
    eva "¿Una muñeca, [mc]? ¿Crees que somos niñas pequeñas?"
    mc "No. No es lo que quería decir con ese regalo... dijiste que nunca habíais tenido una. Encontré esas que eran personalizables y... No son pistolas... creía que os gustarían..."
    mc "No sé... quería regalaros vuestra primera muñeca... no quería ofenderos."
    call BlinkXP ("c19s004_425" , "d") from _call_BlinkXP_3062
    eva "No creía que te acordaras... o que hubieras prestado atención..."
    mc "Siempre presto atención a lo que decís, Eva."
    scene c19s004_430a with dissolve
    mc "¿A ti tampoco te gusta la tuya, Amanda?"
    ama "¿Gustarme? ¿Tampoco?"
    ama "[mc], a veces pareces tan listo y a veces parece que no sabes de qué estás hablando... eres desconcertante."
    scene c19s004_430b with dissolve
    ama "Me encanta... La has vestido como el día que nos conocimos, durante el secuestro, pero sin el pasamontañas..."
    call BlinkXP ("c19s004_435" , "d") from _call_BlinkXP_3063
    ama "Gracias, [mc]. Es increíble que te hayas tomado tantas molestias por nosotras."
    ama "Y a Eva también le gusta la suya. Pero no sabe expresar agradecimiento."
    mc "No..."
    scene c19s004_430c with dissolve
    mc "... pasa..."
    scene c19s004_430d with hpunch
    mc "... nada..."
    eva "¡Gracias, [mc]!"
    call KissXP ("c19s004_440" , "d") from _call_KissXP_98
    eva "¡Gracias, gracias, gracias!"
    mc "Me alegra que os gusten..."
    scene c19s004_440c with dissolve
    eva "Tu turno, Amanda."
    scene c19s004_440d with dissolve
    ama "Gracias, [mc]."
    call KissXP ("c19s004_445" , "d") from _call_KissXP_99
    ama "No sabes lo que significa esto para nosotras."
    mc "No lo puedo imaginar, pero me encantan vuestras reacciones. Aunque me habéis acojonado al principio."
    call BlinkXP ("c19s004_450" , "d") from _call_BlinkXP_3064
    ama "La próxima vez, añade un set de maquillaje. Últimamente, por tu culpa, parezco un mapache demasiado a menudo."
    mc "*Risa* Y yo que creía que erais mercenarias duras..."
    call BlinkXP ("c19s004_455" , "d") from _call_BlinkXP_3065
    eva "Ponme a luchar con guerrillas africanas y te demostraré lo dura que soy..."
    mc "Pero una muñeca te hace llorar..."
    call BlinkXP ("c19s004_460" , "d") from _call_BlinkXP_3066
    ama "No es la muñeca en sí, [mc]. Es que hayas pensado que podrían gustarnos a nosotras."
    call BlinkXP ("c19s004_465" , "d") from _call_BlinkXP_3067
    eva "Y que hayas pensado que nosotras también debíamos recibir regalos. El día del cumpleaños de las chicas."
    mc "Sois tan parte de esta familia como cualquiera de nosotros. Os debemos 18 regalos de cumpleaños."
    stop music fadeout (1.5)
    mc "¿Por qué no dejas la muñeca y vuelves aquí? Creo que un abrazo triple estaría bien, ¿no?"
    scene c19s004_465d with fade
    play music ("music/SadSoul.ogg")
    eva "Sí. Se está bien aquí..."
    ama "Rechazo tu idea, Eva."
    eva "Creo que yo también la rechazo."
    mc "¿De qué habláis?"
    eva "Te hemos dicho que no habíamos acabado de concretar lo que hablamos ayer..."
    ama "Mi hermana tuvo la \"genial\" idea de decirte que, o nos elegías a las dos, o a ninguna."
    eva "No contestes qué elegirías... Ese plan se acaba de ir a la mierda. De todas formas, Amanda no estaba convencida."
    eva "Es lo que se me ocurrió para que no discutiéramos."
    mc "Y ¿por qué la rechazáis ahora?"
    call BlinkXP ("c19s004_470" , "d") from _call_BlinkXP_3068
    ama "No podría aceptar que rechazaras a Eva por ese ultimátum si no quieres estar conmigo pero sí con ella."
    mcp "(Cada día te pareces más a [eri].)"
    mc "¿Y tú, Eva? Si la idea fue tuya..."
    call BlinkXP ("c19s004_475a" , "d") from _call_BlinkXP_3069
    eva "Me he imaginado cómo reaccionaría yo si me pusieran entre la espada y la pared como pensaba hacerte."
    eva "Mi reacción no hubiera sido... agradable. Ha hecho falta que me hagas llorar para que lo entienda."
    mcp "(Y tú cada día te pareces más a [emm].)"
    call BlinkXP ("c19s004_475b" , "d") from _call_BlinkXP_3070
    eva "No quiero que pases por eso porque nosotras nos estemos comportando como niñas pequeñas."
    mc "Gracias, Eva..."
    call BlinkXP ("c19s004_480" , "d") from _call_BlinkXP_3071
    ama "Al menos ahora seremos niñas pequeñas con muñecas. *Risa* Poco a poco iremos aprendiendo."
    mc "*Risa* Poco a poco. Os iremos dando un curso acelerado de \"normalidad\". O tanta \"normalidad\" como esta familia sea capaz."
    scene c19s004_465d with dissolve
    "El abrazo dura un rato, con conversaciones intrascendentes y risas."
    if mc._var("relationships")>0:
        "La revelación de secretos se intercala entre las conversaciones."
        "Coinciden con lo que ha dicho Betty sobre el secreto de Meemaw dejando los tuyos en segundo plano."
    if Aux2 > 0:
        "También te felicitan por tu futura paternidad. Has dado un buen uso a los tests."
    call BlinkXP ("c19s004_485" , "d") from _call_BlinkXP_3072
    ama "Creo que deberíamos ir bajando. Las chicas se van a preguntar dónde estamos."
    if mc._var("relationships")>0:
        ama "O si va a haber más secretos que revelar cuando bajemos. *Risa*"
    mc "Sería buena idea bajar. No os olvidéis las muñecas."
    ama "De camino a la piscina, las dejaremos en la habitación de [emm], con nuestra ropa."
    call BlinkXP ("c19s004_490" , "d") from _call_BlinkXP_3073
    eva "Dadme un segundo..."
    call BlinkXP ("c19s004_495" , "d") from _call_BlinkXP_3074
    if not _in_replay:
        $ eva.profileImages.pop (13) # first remove
        $ eva.profileImages.insert (13, ("eva_13", None)) # then add new
        $ renpy.notify ("Profile Image unlocked for Eva: 14 - Topless party")
    eva "Ya. Podemos bajar. También dejaré esto en la habitación de [emm]."
    mc "¿Por qué has cambiado de opinión?"
    scene c19s004_495d with dissolve
    eva "Alguien me dijo que tenía que dejar con ganas de más a los chicos que me interesaran y que contara las veces que lo hacía."
    eva "Van dos."
    scene c19s004_495e with dissolve
    play sound ("music/DoorSlam.ogg")
    "*Blam*"
    call BlinkXP ("c19s004_500" , "d") from _call_BlinkXP_3075
    mc "Creo que he creado un monstruo. *Risa*"
    ama "Es culpa tuya. *Risa*"
    scene c19s004_495e with dissolve
    play sound ("music/knock.ogg")
    "*Knock-Knock*"
    eva "*A través de la puerta* Soy yo..."
    mc "Adelante..."
    call BlinkXP ("c19s004_505" , "d") from _call_BlinkXP_3076
    eva "He querido hacer una salida tan dramática que me he olvidado a Fee."
    mc "*Risa* Cógela y nos vemos abajo."
    mcp "(¿Fee? ¿Ya le ha puesto nombre? ¿Es posible que sea por Fiona, la primera de las chicas que murió?)"
    if persistent.family:
        mcp "(La he diseñado para que se parezca a Eva, lo cual significa que también se parece a Fiona.)"
    scene c19s004_495f with fade
    eva "Hasta luego, [mc]." (multiple=2)
    ama "Te vemos en la piscina." (multiple=2)
    mc "Hasta ahora, chicas. No os quedéis jugando con las muñecas en la habitación de [emm]. O al menos no os quedéis demasiado rato."
    stop music fadeout (1.5)
    return
label c19s004_MaddieDebbie:
    if _in_replay:
        $ mc._var("relationships", 0, intention = "set")
        menu:
            "¿Estás en una relación con Maddie?"
            "Sí":
                $ mad._var("route" , True)
                $ mc._var("relationships", 1)
                menu:
                    "¿Estás en alguna las rutas de dominación con Maddie?"
                    "Sí":
                        $ mad._var("dom" , True)
                        $ mad._var("romance" , False)
                    "No":
                        $ mad._var("romance" , True)
                        $ mad._var("dom" , False)
                        $ mad._var("sub" , False)
            "No":
                $ mad._var("route" , False)
                $ mad._var("romance" , False)
                $ mad._var("dom" , False)
                $ mad._var("sub" , False)
        menu:
            "¿Estás en una relación con Alexia?"
            "Sí":
                $ oma._var("route" , True)
                $ mc._var("relationships", 1)
            "No":
                $ oma._var("route" , False)
                menu:
                    "¿Estás en una relación con [mar!t]?"
                    "Sí":
                        $ mar._var("route" , True)
                        $ mc._var("relationships", 1)
                    "No":
                        $ mar._var("route" , False)
                        menu:
                            "¿Estás en una relación con [nor]?"
                            "Sí":
                                $ nor._var("route" , True)
                                $ mc._var("relationships", 1)
                            "No":
                                $ nor._var("route" , False)
                                menu:
                                    "¿Estás en una relación con Eileen?"
                                    "Sí":
                                        $ eil._var("route" , True)
                                        $ mc._var("relationships", 1)
                                    "No":
                                        $ eil._var("route" , False)
                                        menu:
                                            "¿Estás en una relación con Samantha?"
                                            "Sí":
                                                $ sam._var("route" , True)
                                                $ mc._var("relationships", 1)
                                            "No":
                                                $ sam._var("route" , False)
                                                menu:
                                                    "¿Estás en una relación con Simone?"
                                                    "Sí":
                                                        $ sim._var("route" , True)
                                                        $ mc._var("relationships", 1)
                                                    "No":
                                                        $ sim._var("route" , False)
        if mc._var("relationships") < 2:
            menu:
                "¿En cuántas relaciones estás?"
                "Más de una":
                    $ mc._var("relationships", 2, intention = "set")
                "Una" if mc._var("relationships") < 2:
                    $ mc._var("relationships", 1, intention = "set")
                "Ninguna" if mc._var("relationships") < 1:
                    $ mc._var("relationships", 0, intention = "set")
    call BlinkXP ("c19s004_600" , "f") from _call_BlinkXP_3077
    "Al llegar a la piscina, te acercas a Maddie, que parece que se acaba de quedar sola."
    play music ("music/Inspiring-Upbeat-Ambient.ogg")
    mc "¿Qué tal te lo estás pasando, Maddie?"
    mad "Muy bien, había algunas chicas a las que solo conocía de pasada. Hacía mucho tiempo que no estaba en una fiesta con tanta gente y con tan buen rollo."
    mad "Incluso lo del mensaje se ha solucionado de una forma... diferente a como me imaginaba."
    mc "Bueno... creo que somos diferentes a lo habitual."
    mad "Siéntate conmigo un rato. Apenas hemos tenido tiempo de hablar."
    $ Aux = mc._var("relationships")
    call BlinkXP ("c19s004_605a" , "d") from _call_BlinkXP_3078
    if mad._var("route") and mc._var("relationships") > 1:
        mad "No todas las chicas descubren todos los días que el chico con el que pensabas que tenías algo especial lo tiene también con más chicas."
        mc "Nunca me he escondido sobre eso."
        if mad._var("romance"):
            mc "Te dije que estaba con alguien más. No me puedes acusar de no ser sincero."
        else:
            mc "Tu relación y la mía es diferente a cualquier otra que tenga."
        call BlinkXP ("c19s004_605b" , "d") from _call_BlinkXP_3079
        mad "Pero que Betty haya querido cubrirte... ha sido alucinante."
    elif mad._var("route") and mc._var("relationships") == 1:
        mad "Ha sido alucinante que Betty haya intentado cubrirnos sin ni siquiera saber a quién cubría."
    elif mc._var("relationships") == 1:
        mad "Ha sido alucinante que Betty haya intentado cubriros sin ni siquiera saber a quién cubría."
        if mar._var("route") or nor._var("route") or sim._var("route") or sam._var("route") or oma._var("route") or eil._var("route"):
            mc "Lo sabía, pero eso no le quita mérito a que haya querido cubrirnos."
        else:
            mc "No me extrañaría que lo hubiera sospechado en todo momento, conociendo a Tía Betty."
    elif mc._var("relationships") == 0:
        mad "Has tenido que alucinar mucho cuando has recibido ese mensaje, no saliendo con nadie, y con Betty confesando algo que no es cierto para cubrirte."
    mc "Betty es así. La razón que ha dado es tan propia de ella... Ha preferido cargar con la culpa antes de que se descubriera el posible culpable."
    call BlinkXP ("c19s004_605c" , "d") from _call_BlinkXP_3080
    mad "Es bueno tener a alguien así cerca. Todos sois alucinantes... Betty, Olivia, [mar], [nor], las chicas... Obviamente Amanda y Eva..."
    mc "¿Y el resto? Creo que no conocías a Kim, Lisa, o Kate. Te he visto hablando con ellas antes."
    call BlinkXP ("c19s004_610" , "d") from _call_BlinkXP_3081
    mad "A Kate y a Lisa sí que las había visto. Vinieron con Debbie hace unos días a la tienda."
    mad "A Kim no la había visto. Es espectacular. No me extraña que sea modelo."
    mc "Es una chica muy especial."
    call BlinkXP ("c19s004_615" , "d") from _call_BlinkXP_3082
    mad "Y muy amable. Después de los regalos, hablando con Lisa y Kim, hemos estado hablando de pintura."
    mc "Lisa estudia arte, es lógico."
    call BlinkXP ("c19s004_620a" , "d") from _call_BlinkXP_3083
    if mad._var("route"):
        mad "Les ha hablado de los cuadros de Zeus, y de los diseños de vestidos."
    else:
        mad "Les he hablado de unos cuadros de Zeus que tengo en mi habitación y... no sé si sabes que diseño ropa."
        mc "No, no lo sabía..."
    call BlinkXP ("c19s004_620b" , "d") from _call_BlinkXP_3084
    mad "¡Pues Kim se ha ofrecido a servirme como maniquí para probar cómo quedan los vestidos en una persona real!"
    mc "¡Eso es fantástico!"
    mc "No tengo ni idea de si eso puede ayudarte, pero supongo que es mejor que verlos en papel o en un ordenador."
    call BlinkXP ("c19s004_625" , "d") from _call_BlinkXP_3085
    mad "¡Es increíble! Muchas veces, cuando tengo el vestido cortado y pre-cosido, me lo pruebo y no se parece en nada a lo que tenía en mente."
    mad "Hacer modificaciones sobre mí misma es muy complicado, pero tener a Kim para ayudarme en eso... sería de una ayuda que no te puedes imaginar."
    mc "*Risa* Se te ve muy emocionada, con lo que empiezo a imaginármelo."
    mc "Y voy más allá. Ya me estoy imaginando a Kim desfilando en una pasarela con tus vestidos. *Risa*"
    call BlinkXP ("c19s004_630" , "d") from _call_BlinkXP_3086
    mad "Mmmm... creo que me acabas de dar una idea muy interesante. Si encontráramos un fotógrafo... las dos podríamos sacar algo de esto..."
    mc "Habla con [emm]. No es profesional ni nada por el estilo, pero es buena con la cámara."
    call BlinkXP ("c19s004_635" , "d") from _call_BlinkXP_3087
    mad "¿Qué? ¡No lo sabía!"
    mc "La fotografía es una de sus pasiones. Creo que las tres podríais sacar algo de esto."
    mc "[emm] aumentar su portfolio, Kim su book, y tú poder promocionar tus vestidos."
    mad "¡Tengo que hablar con ella!"
    mc "*Risa* La he visto entrar en casa hace un momento. Supongo que no tardará."
    call BlinkXP ("c19s004_640a" , "d") from _call_BlinkXP_3088
    mad "Bueno, tampoco es el momento de hablar de negocios. Además es su cumpleaños."
    mc "Le harás un regalo increíble... otro regalo increíble, si le ofreces hacer fotos profesionales el día de su cumpleaños, o casi."
    if mad._var("route"):
        call BlinkXP ("c19s004_640b" , "d") from _call_BlinkXP_3089
        mc "Tengo una pregunta, hablando de regalos. ¿Qué ha sido del cuadro de Zeus disfrazado de superhéroe?"
        mad "No me gustaba. No estaba tan personalizado como me hubiera gustado. Sabiendo que [dap] quiere dedicarse a la química me pareció una mejor opción."
        mc "Es una buena razón. Me ha gustado más el de químico que el de superhéroe."
        mad "*Risa* El de superhéroe se quedará en mi pared cuando lo acabe. Lo dejé apartado mientras pintaba el de químico."
    call BlinkXP ("c19s004_645" , "d") from _call_BlinkXP_3090
    stop music fadeout (1.5)
    deb "¿Interrumpo algo?"
    play music ("music/SneakySnitch.ogg")
    mc "No, Debbie, estábamos hablando de las fotos de [emm]."
    call BlinkXP ("c19s004_650" , "d") from _call_BlinkXP_3091
    deb "¡Oh! ¡Son fantásticas! Tiene muy buen ojo para la composición y la luz... al menos eso dice Lisa. Yo no entiendo de fotografía."
    deb "Yo sólo sé si una foto me gusta o no. Y las de [emm] me gustan. Igual que tus cuadros, Maddie. Son super bonitos y muy graciosos."
    call BlinkXP ("c19s004_655a" , "d") from _call_BlinkXP_3092
    mad "Gracias. Fue muy divertido pintarlos y disfrazar a Zeus."
    call BlinkXP ("c19s004_655b" , "d") from _call_BlinkXP_3093
    deb "¿Lo has traído también?"
    call BlinkXP ("c19s004_655c" , "d") from _call_BlinkXP_3094
    mad "¿A qué te refieres?"
    call BlinkXP ("c19s004_655d" , "d") from _call_BlinkXP_3095
    deb "Has traído al otro gato, ¿no? Por eso preguntaba si habías traído a Zeus."
    call BlinkXP ("c19s004_655e" , "d") from _call_BlinkXP_3096
    mad "No... solo tengo a Zeus... bueno \"tengo\"... Él seguramente pensaría diferente. ¿Por qué?"
    call BlinkXP ("c19s004_655f" , "d") from _call_BlinkXP_3097
    deb "Cuando he subido a mi habitación, por la ventana se ve el jacuzzi de [nor]. Me ha parecido que Alexia tenía un gato en el regazo."
    mc "¿El jacuzzi nudista? ¿Un gato negro?"
    call BlinkXP ("c19s004_660a" , "d") from _call_BlinkXP_3098
    deb "Sí, pero... ¿cómo... lo... sabes?"
    call BlinkXP ("c19s004_660b" , "d") from _call_BlinkXP_3099
    deb "¡Oh! ¡No! ¡Era otro tipo de animal peludo!"
    call BlinkXP ("c19s004_660c" , "d") from _call_BlinkXP_3100
    mad "*Risa* ¡Un conejo!"
    mc "*Risa* Puedes preguntarle a Alexia cómo se llama su mascota."
    call BlinkXP ("c19s004_665" , "d") from _call_BlinkXP_3101
    deb "¡Por el amor de Dios! A veces soy tan pardilla..."
    mc "No pasa nada, supongo que a esa distancia no podías tener una buena vista."
    call BlinkXP ("c19s004_670" , "d") from _call_BlinkXP_3102
    mad "Creo que yo pasaré del jacuzzi nudista. A [eri] le ha costado convencerme para hacer topless..."
    mad "Creía que iba a ser la única que no lo hiciera. Si llego a saber que habría más mujeres tapadas... Aunque te acabas acostumbrando."
    call BlinkXP ("c19s004_675" , "d") from _call_BlinkXP_3103
    deb "Dejaron claro que era opcional. A lo mejor no te lo han transmitido bien."
    mc "Debbie tiene razón. Ni en el jacuzzi ni en la piscina hay nada obligatorio. Todo es opcional."
    scene c19s004_680a with dissolve
    mad "Entonces creo que sí que voy a ir. Me apetece un rato relajante. ¿Os apuntáis?"
    deb "Si a [mc] no le importa que le dejemos solo... si no se quiere apuntar, claro."
    stop music fadeout (1.5)
    mc "No os preocupéis. Acabo de ver que Meemaw se ha quedado sola y quiero hablar con ella. Id y disfrutad."
    return
label c19s005_Meemaw:
    if _in_replay:
        $ eri._var("route" , False)
        $ mar._var("route" , False)
        $ nor._var("route" , False)
        $ mc._var("relationships", 0, intention = "set")
        menu:
            "¿[dap] está embarazada?"
            "Sí":
                $ dap._var("pregnancyDiscovered" , True)
                $ mc._var("relationships", 1)
                $ Aux2 = 1
            "No":
                $ dap._var("pregnancyDiscovered" , False)
                $ Aux2 = 0
        menu:
            "¿Estás en una relación con [emm]?"
            "Sí":
                $ emm._var("route" , True)
                $ mc._var("relationships", 1)
            "No":
                $ emm._var("route" , False)
                menu:
                    "¿Estás en una relación con [eri]?"
                    "Sí":
                        $ eri._var("route" , True)
                        $ mc._var("relationships", 1)
                    "No":
                        $ eri._var("route" , False)
                        menu:
                            "¿Estás en una relación con [mar!t]?"
                            "Sí":
                                $ mar._var("route" , True)
                                $ mc._var("relationships", 1)
                            "No":
                                $ mar._var("route" , False)
                                menu:
                                    "¿Estás en una relación con [nor]?"
                                    "Sí":
                                        $ nor._var("route" , True)
                                        $ mc._var("relationships", 1)
                                    "No":
                                        $ nor._var("route" , False)
        if not dap._var("pregnancyDiscovered"):
            menu:
                "¿Alguien reveló que estaba esperando un hijo tuyo?"
                "Sí":
                    $ Aux2 = 1
                "No":
                    $ Aux2 = 0
        if mc._var("relationships")<2:
            menu:
                "¿En cuántas relaciones estás?"
                "Más de una":
                    $ mc._var("relationships", 2, intention = "set")
                "Una":
                    $ mc._var("relationships", 1, intention = "set")
                "Ninguna" if mc._var("relationships")==0:
                    $ mc._var("relationships", 0, intention = "set")
        menu:
            "¿Has pre-abierto la relación con Meemaw?"
            "Sí":
                $ mee._var("route" , True)
            "No":
                $ mee._var("route" , False)
    call BlinkXP ("c19s005_005" , "f") from _call_BlinkXP_3104
    play music ("music/From-Above.ogg")
    mc "¿Qué tal, Meemaw? ¿Ya te has cansado de los abrazos? *Risa* Te veo muy apartada."
    mee "No. *Risa* De eso nunca me canso. Pero necesitaba un momento a solas."
    call BlinkXP ("c19s005_010" , "d") from _call_BlinkXP_3105
    mee "He entendido cómo se tuvieron que sentir Amanda y Eva."
    mee "Estoy... abrumada..."
    mc "Con la bomba que has dejado caer... las bombas, si incluimos la mudanza... ¿Esperabas otra reacción?"
    call BlinkXP ("c19s005_015" , "d") from _call_BlinkXP_3106
    mee "No de las chicas..."
    if persistent.family:
        mee "Y cuando hablo de las chicas incluyo a mis hijas."
    else:
        mee "Y cuando hablo de las chicas incluyo a [nor] y [mar]."
    call BlinkXP ("c19s005_020" , "d") from _call_BlinkXP_3107
    mee "Pero me ha sorprendido mucho cómo se han comportado el resto de las chicas..."
    mc "Te has ganado su cariño en los últimos días, Meemaw. Casi todas se sienten parte de la familia, y os ven a Tía Betty y a ti de una forma especial."
    mc "No te digo que alguien como Maddie, que es la primera vez que viene, sienta eso, ¿pero el resto? Seguro que sí."
    call BlinkXP ("c19s005_025" , "d") from _call_BlinkXP_3108
    mee "El cariño es mutuo, [mc]. Pero... no sé... ha habido casi demasiados abrazos y ha sido muy emocionante."
    mc "Entonces no te ofreceré el abrazo que venía a darte."
    mc "Me voy a abrazar a otras chicas por ahí... seguro que ellas sí que lo necesitan. *Risa*"
    call BlinkXP ("c19s005_030" , "h") from _call_BlinkXP_3109
    mee "¡Ni se te ocurra! Nunca le niegues un abrazo a una anciana. *Risa*"
    mc "*Risa* Sabía que ibas de farol..."
    call BlinkXP ("c19s005_035" , "d") from _call_BlinkXP_3110
    mee "Cuando te suelte... dentro de un par de horas... ¿quieres sentarte un rato conmigo?"
    mc "Por supuesto. Pero solo queda un sillón. ¿Quién se ha llevado el otro?"
    call BlinkXP ("c19s005_040" , "d") from _call_BlinkXP_3111
    mee "No lo sé... el único de quien no sospecho es de Jamaal... *Risa* Viene con asiento incorporado."
    mc "*Risa* Me encanta que te unas al grupo de Whack a Jamaal. Lo del estante de arriba de antes ha sido ingenioso."
    mee "Si no me hubiera pedido leche para sus pastitas no lo habría hecho. *Risa*"
    mc "Pues te tendrás que sentar en mis rodillas. No creo que yo pueda sentarme en las tuyas después de tantos años. *Risa*"
    call BlinkXP ("c19s005_045" , "f") from _call_BlinkXP_3112
    if Aux2 > 0:
        mee "Por cierto, felicidades por la paternidad. Me vas a hacer bisabuela... Cuando te pedí bisnietos en el aeropuerto no me imaginaba que sería tan pronto."
        if dap._var("pregnancyDiscovered"):
            mc "Por partida doble en el caso de [dap]."
            if emm._var("route") or eri._var("route"):
                mee "Y aún podrían llegar más que me hicieran doblemente bisabuela."
        mc "No estaba planeado, pero han llegado y estoy contento."
        mee "Yo también. Esta familia cada vez es más rara, pero cada vez me gusta más."
    if mc._var("relationships")>1:
        call BlinkXP ("c19s005_050" , "d") from _call_BlinkXP_3113
        mc "Al menos con la revelación de tu secreto, nadie ha prestado demasiada atención a mis relaciones."
        mee "En parte lo he hecho por eso. Era un buen momento antes de que nadie se escandalizara o se sorprendiera demasiado de que salieras con más de una mujer."
        mee "Hay gente muy retrógrada en esta familia... y yo soy una de ellas. Quizás la que más."
        mee "Si yo lo tengo que aceptar... el resto también. Que se jodan."
        mc "*Risa* A veces eres maravillosa, Meemaw."
        call BlinkXP ("c19s005_055" , "d") from _call_BlinkXP_3114
        mee "*Risa* ¿Sólo a veces?"
        mc "Sí, [emm]... digo... Meemaw. *Risa*"
    call BlinkXP ("c19s005_060" , "d") from _call_BlinkXP_3115
    mc "¿Cómo sienta salir a la luz con tus secretos?"
    mee "Cuando he empezado a hablar estaba asustada. No sabía cómo se lo iban a tomar. Lo he ocultado durante demasiado tiempo y temía la reacción de [nor]."
    mee "Y la de [emm]. Nunca sabes por dónde puede explotar esa chica."
    call BlinkXP ("c19s005_065" , "d") from _call_BlinkXP_3116
    mee "Y entonces [emm] ha hablado, sin dejar reaccionar a nadie."
    mee "Cuando ha venido a abrazarme, casi se me saltan las lágrimas. Después han venido el resto... ha sido increíble."
    mc "No era el momento de echarte en cara que hubieras guardado el secreto. Todas estaban muy contentas con que lo hubieras superado."
    call BlinkXP ("c19s005_070" , "d") from _call_BlinkXP_3117
    mee "Cuando han pasado los abrazos, [nor] me lo ha echado en cara. Pero de una forma diferente a como esperaba..."
    mee "Creo que... nos estamos haciendo amigas... nos ha costado 45 años, pero lo estamos logrando..."
    mc "Ayuda mucho que haya aprendido a plantarte cara. Cuando nos dijo que venías estaba tan asustada como tú antes de contar lo del cáncer."
    call BlinkXP ("c19s005_075" , "d") from _call_BlinkXP_3118
    mee "¿De mí? Pero... pero..."
    call BlinkXP ("c19s005_080" , "d") from _call_BlinkXP_3119
    mee "La critico mucho, ¿verdad?"
    mc "Lo hacías. ¿Te imaginas qué hubiera pasado hace unos años si hubiera decidido ir en ropa interior por casa?"
    call BlinkXP ("c19s005_085" , "d") from _call_BlinkXP_3120
    mee "Me hubiera puesto hecha una fiera. Bueno... prácticamente lo hice después del secuestro."
    mc "Pero te plantó cara y te puso en tu sitio. Es su casa y son sus normas."
    call BlinkXP ("c19s005_090" , "d") from _call_BlinkXP_3121
    mee "Y tú te desnudaste. *Risa*"
    mc "Bueno, la primera en desnudarse fuiste tú... *Risa*"
    mc "Pero sí. [nor] ha aprendido a tratarte y tú estás aprendiendo a respetarla."
    mc "Ahora tenéis una buena base para haceros amigas. Las dos lo necesitabais."
    call BlinkXP ("c19s005_095" , "d") from _call_BlinkXP_3122
    mee "Y la fiesta en topless ha sido una gran idea. Estoy segura de que [eri] lo pidió para que [nor] pudiese estar cómoda y yo no pudiera protestar."
    mc "Conoces muy bien a tu nieta. *Risa*"
    mee "Pero se han apuntado más chicas de lo que esperaba. Y creo que les ha ido bien. Eva ha cambiado de opinión hace un rato..."
    scene c19s005_095d with dissolve
    mc "Y tú también deberías cambiar de opinión. Estás empezando a mojar tu top..."
    call BlinkXP ("c19s005_100" , "d") from _call_BlinkXP_3123
    if not mee._var("route"):
        mee "¡Oh, mierda! No mires..."
        mc "Meemaw, te vi el otro día en la consulta del médico y te he dado un par de masajes desde entonces. No me voy a asustar por un poco de leche."
        call BlinkXP ("c19s005_105" , "d") from _call_BlinkXP_3124
        mee "Tienes razón..."
        scene c19s005_110AnBlink with dissolve
        mee "Ya está... ya no mancho más. Creo que al final voy a disfrutar yo también la fiesta topless."
        mc "Bien dicho, Meemaw."
        call BlinkXP ("c19s005_115" , "d") from _call_BlinkXP_3125
        mee "Ahora me voy a ir a lavar. Están... pegajosas"
        mc "Tranquila, ve a lavarte y después olvídate del problema y disfruta la tarde."
        call KissXP ("c19s005_120a" , "d") from _call_KissXP_100
        mee "Hasta luego, cariño."
        mc "Te veo luego, Meemaw."
        return
    mee "¡Oh, mierda! Estar sentada encima tuyo me ha recordado a esta mañana..."
    mc "¿Te has puesto cachonda, Meemaw?"
    call BlinkXP ("c19s005_105" , "d") from _call_BlinkXP_3126
    mee "Un poco, pero puedo controlarlo..."
    mc "Tu top dice lo contrario..."
    scene c19s005_110AnBlink with dissolve
    mee "Ya está... ya no mancho más."
    if not _in_replay:
        $ mee.profileImages.pop (13) # first remove
        $ mee.profileImages.insert (13, ("olivia_13", None)) # then add new
        $ renpy.notify ("Profile Image unlocked for Olivia: 14 - Topless party")
    mc "Creo que es una buena idea, pero eso nos lleva a la pregunta del millón de dólares."
    mc "No has dicho nada de lo que hemos estado haciendo. Ya que estabas confesando secretos..."
    call BlinkXP ("c19s005_120b" , "d") from _call_BlinkXP_3127
    mee "No sé qué podría haber dicho. No puedo decir que mi nieto me produce orgasmos cada vez que me masajea las tetas..."
    if mar._var("route"):
        mee "No es que estemos saliendo como estás haciendo con [mar]... ¿no?"
    elif nor._var("route"):
        mee "No es que estemos saliendo como estás haciendo con [nor]... ¿no?"
    elif emm._var("route"):
        mee "No es que estemos saliendo como estás haciendo con tu hermana... ¿no?"
    elif eri._var("route"):
        mee "No es que estemos saliendo como estás haciendo con [eri]... ¿no?"
    elif dap._var("route"):
        mee "No es que estemos saliendo como estás haciendo con [dap]... ¿no?"
    else:
        mee "No es que estemos saliendo... ¿no?"
    call BlinkXP ("c19s005_125" , "d") from _call_BlinkXP_3128
    mee "Me sentiría ridícula si dijera que estoy saliendo con cualquiera... y más aún contigo."
    mc "Entonces ¿qué estamos haciendo?"
    mee "No lo sé... No lo he pensado. Lo que ha pasado esta mañana ha sido increíble..."
    call BlinkXP ("c19s005_130" , "d") from _call_BlinkXP_3129
    mee "¿Pero realmente quieres tener una relación romántica conmigo? Salir sigue significando eso para los jóvenes, ¿no?"
    mc "Sí, sigue significando eso..."
    mc "No sé si quiero salir contigo ahora o más adelante, pero quiero hacerlo."
    call BlinkXP ("c19s005_135" , "d") from _call_BlinkXP_3130
    mee "¿Por qué? ¿Qué puedo aportarte yo?"
    if mc._var("relationships")>1:
        mee "Sales con chicas mucho más jóvenes que yo..."
    elif mc._var("relationships")==1:
        mee "Sales con una chica mucho más joven que yo..."
    mee "Yo tan solo soy una vieja que ha disfrutado mucho de lo que ha hecho con su nieto esta mañana..."
    mc "No hace falta que contestes. Ni siquiera te lo estoy pidiendo. Sólo quiero que sepas que un día vamos a salir a cenar. Vamos a tener una cita."
    call BlinkXP ("c19s005_140" , "d") from _call_BlinkXP_3131
    mee "Y eso lo has decidido tú sin consultármelo a mí, sin tener en cuenta mi opinión, ¿no?"
    mc "Sí. Vamos a salir como un nieto que lleva a su abuela a cenar... A eso no te puedes negar, a una cena inocente."
    call BlinkXP ("c19s005_145" , "d") from _call_BlinkXP_3132
    mee "Pero eso no es una cita..."
    mc "Déjame hablar. Vamos a salir como un nieto que lleva a su abuela a cenar."
    mc "Antes de volver a casa decidiremos si volvemos como hemos salido o como algo más. Y ahí tendré en cuenta tu opinión y tú tendrás en cuenta la mía."
    mc "¿Te parece bien? Solo pido ir a cenar un día. No es un chantaje ni nada por el estilo. Tan solo quiero cenar con mi Meemaw y tener una conversación adulta después."
    call BlinkXP ("c19s005_150" , "d") from _call_BlinkXP_3133
    mee "Son unas condiciones que puedo aceptar..."
    mee "¿Pero qué pasará si volvemos como hemos salido?"
    mc "No pasará nada. Seguiremos como hasta ahora y habremos disfrutado de la compañía del otro durante una cena."
    call BlinkXP ("c19s005_155" , "d") from _call_BlinkXP_3134
    mee "¿Y si volvemos siendo algo más?"
    if persistent.family:
        mc "Te tocará explicárselo a tus hijas, a tu hermana, y a tus nietas. Yo me ocuparé de explicárselo al resto de las chicas"
    else:
        mc "Te tocará explicárselo a tu hija, a tu hermana, y a tus nietas. Yo me ocuparé de explicárselo a [mar] y al resto de las chicas."
    call BlinkXP ("c19s005_160" , "d") from _call_BlinkXP_3135
    mee "Sabes que lo estás poniendo muy difícil, ¿verdad?"
    mc "¿Tanto te asusta decírselo?"
    call BlinkXP ("c19s005_165" , "d") from _call_BlinkXP_3136
    mee "No lo entiendes, cariño... pones difícil decirte que no a esa cena."
    if persistent.family:
        mee "Yo sólo voy a tener que explicárselo a ocho personas y tú al resto. *Risita*"
        mcp "(Ya está contando a Amanda y a Eva en el número de nietas.)"
    else:
        mee "Yo sólo voy a tener que explicárselo a siete personas y tú al resto. *Risita*"
        mcp "(Está contando a [emm] y ya ha incluido a Amanda y a Eva en el número de nietas.)"
    call BlinkXP ("c19s005_170" , "d") from _call_BlinkXP_3137
    mee "*Susurrando* Soy de otra época... a mí no me parecen bien esas cosas modernas de que no hay que tratar a una mujer como se nos debe tratar."
    mee "*Susurrando* No sabes lo cachonda que me pone que un hombre tome las riendas como estás haciendo tú."
    mc "¡Ese lenguaje, Señorita!"
    call BlinkXP ("c19s005_175" , "d") from _call_BlinkXP_3138
    mee "*Risa* ¿Te importa mi lenguaje después de haberme hecho correr esta mañana como si fuera una cascada?"
    mc "*Risa* Para nada, pero siempre ha sido una frase que he querido decirte. Es mi pequeña venganza por las veces que me la dijiste tú."
    mee "¡Es verdad, tienes razón! *Risa* Eras muy malhablado de pequeño."
    call KissXP ("c19s005_120a" , "d") from _call_KissXP_101
    mee "Voy a ir a lavarme... la leche se está poniendo pegajosa... y está a punto de empezar a salir más."
    mc "Vale. Te veo luego."
    scene c19s005_180d with dissolve
    mc "Una cosa más, Meemaw."
    call BlinkXP ("c19s005_180" , "d") from _call_BlinkXP_3139
    mee "Dime."
    mc "Cuando confieses que estamos saliendo..."
    mee "Si. No cuando..."
    mc "Cuando confieses que estamos saliendo, también tendrás que confesar que me has dado la razón TRES veces el mismo día. Lo acabas de volver a hacer."
    call BlinkXP ("c19s005_185" , "d") from _call_BlinkXP_3140
    mee "*Risa* Confesar que salgo contigo, si al final lo hago... vale."
    mee "Confesar que te he dado la razón... NUNCA. *Risa*"
    mee "Te veo luego, cariño. Si no me voy ya, voy a tener que besarte, y no como un saludo."
    mc "Hasta luego, Meemaw."
    scene c19s005_185d with dissolve
    mcp "(Ha ido mejor de lo que esperaba cuando ha salido la conversación. Por un momento he pensado que se iba a negar en redondo.)"
    return
label c19s005_Kiara:
    if _in_replay:
        $ mar._var("route" , False)
        $ nor._var("route" , False)
        $ mc._var("relationships", 0, intention = "set")
        menu:
            "¿Estás en una relación con Eileen?"
            "Sí":
                $ eil._var("route" , True)
                $ mc._var("relationships", 1)
            "No":
                $ eil._var("route" , False)
        menu:
            "¿Estás en una relación con Samantha?"
            "Sí":
                $ sam._var("route" , True)
                $ mc._var("relationships", 1)
            "No":
                $ sam._var("route" , False)
                menu:
                    "¿Estás en una relación con [mar!t]?"
                    "Sí":
                        $ mar._var("route" , True)
                        $ mc._var("relationships", 1)
                    "No":
                        $ mar._var("route" , False)
                        menu:
                            "¿Estás en una relación con [nor]?"
                            "Sí":
                                $ nor._var("route" , True)
                                $ mc._var("relationships", 1)
                            "No":
                                $ nor._var("route" , False)
        if mc._var("relationships") < 2:
            menu:
                "¿En cuántas relaciones estás?"
                "Más de una":
                    $ mc._var("relationships", 2, intention = "set")
                "Una":
                    $ mc._var("relationships", 1, intention = "set")
                "Ninguna" if mc._var("relationships")==0:
                    $ mc._var("relationships", 0, intention = "set")
    stop music fadeout (1.5)
    scene c19s005_200a with dissolve
    "Ves que Kiara se ha quedado sola. Es tu momento de hablar con ella otra vez sobre sus razones para evitarte."
    scene c19s005_200b with dissolve
    "Te lanzas a la piscina y buceas hasta donde está Kiara. Si no te ve llegar no podrá huir."
    scene c19s005_200c with dissolve
    play sound ("music/Splash.ogg")
    kia "¡[mc]!"
    "Tu objetivo era que no tuviera la oportunidad de huir, pero consigues sobresaltarla sin pretenderlo."
    play music ("music/What-Ive-Found.ogg")
    call BlinkXP ("c19s005_205" , "d") from _call_BlinkXP_3141
    kia "Me has asustado. Estaba... ausente."
    mc "Lo siento, Kiara. No era mi intención."
    mc "¿Qué tal lo estás pasando?"
    call BlinkXP ("c19s005_210" , "d") from _call_BlinkXP_3142
    kia "Ya te lo he dicho antes. Eileen me había hablado de vuestras fiestas, pero esto es más grande de lo que me imaginaba."
    "Su tono intenta ser cortante pero educado. Tan solo consigue sonar triste."
    mc "Bueno, este año somos más gente de lo que hemos sido nunca. Para nosotros también es más grande."
    mc "Vosotras, las chicas nuevas, hacéis que este año sea diferente. Mejor. Mucho mejor."
    call BlinkXP ("c19s005_215" , "d") from _call_BlinkXP_3143
    kia "*Risa triste* Creo que hace 20 años que nadie me llamaba \"chica\"."
    mc "*Risa* Es difícil hablar de un grupo tan grande sin generalizar. Para Meemaw todas sois \"las chicas\". A veces incluso Tía Betty."
    mc "Para mí también."
    call BlinkXP ("c19s005_220" , "d") from _call_BlinkXP_3144
    kia "Te debes sentir como el gallo en un gallinero."
    if mc._var("relationships")>1:
        kia "Con varias gallinas para ti..."
    mc "Para nada, Kiara. Me siento afortunado de estar aquí, de teneros a todas cerca."
    call BlinkXP ("c19s005_225" , "d") from _call_BlinkXP_3145
    kia "Creo que te voy a dejar, si no te importa. Están jugando a algo en el jacuzzi y quiero ir a ver a qué."
    mc "Y sigues evitándome."
    call BlinkXP ("c19s005_230" , "d") from _call_BlinkXP_3146
    kia "¿Qué? No..."
    mc "Kiara, engáñate a ti misma si quieres, pero no niegues lo evidente."
    mc "Desde que estuvimos en tu casa, cada vez que he intentado hablar contigo a solas hemos intercambiado cinco o seis frases y has salido corriendo."
    call BlinkXP ("c19s005_235" , "d") from _call_BlinkXP_3147
    kia "Nunca he salido corriendo..."
    mc "Lo hiciste en la cena de anteayer y lo estás volviendo a hacer ahora."
    call BlinkXP ("c19s005_240" , "d") from _call_BlinkXP_3148
    kia "Es que... lo pones muy difícil..."
    mc "No entiendo qué es lo que pongo difícil, Kiara."
    call BlinkXP ("c19s005_245" , "d") from _call_BlinkXP_3149
    if eil._var("route"):
        kia "Sales con mi hija..."
        if mc._var("relationships") > 1:
            kia "Y no sólo con ella..."
            if mar._var("route") or nor._var("route") or sam._var("route"):
                kia "Alguna cercana a mi edad..."
    elif mc._var("relationships") > 1:
        kia "Sales con más de una mujer..."
        if mar._var("route") or nor._var("route") or sam._var("route"):
            kia "Alguna cercana a mi edad..."
    elif mar._var("route") or nor._var("route") or sam._var("route"):
        kia "Sales con una mujer cercana a mi edad..."
    elif mc._var("relationships")==1:
        kia "Estás saliendo con alguien..."
    else:
        kia "Eres como el soltero de oro..."
    mc "No entiendo qué tiene que ver eso con que me rehúyas."
    mc "Me parece que, de alguna forma, te sientes atraída por mí. Pero, por alguna razón que no entiendo, no quieres hablarlo..."
    call BlinkXP ("c19s005_250" , "d") from _call_BlinkXP_3150
    kia "[mc], mi familia es como un castillo en ruinas."
    mcp "(No ha negado que se sienta atraída por mí. Tía Betty tenía razón.)"
    kia "Mi marido se ha pasado años socavando los cimientos. Mi hija tan solo quiere demolerlo."
    kia "Soy la única que aún... hasta el otro día, cuando te enfrentaste a Solomon... estaba empeñada en hacer obras para evitar que se derrumbara del todo."
    mc "¿Ya no?"
    call BlinkXP ("c19s005_255" , "d") from _call_BlinkXP_3151
    kia "Reparar ese castillo... que ha dejado de servir para protegernos..."
    kia "Un castillo que se ha convertido tan solo en una prisión..."
    call BlinkXP ("c19s005_260" , "d") from _call_BlinkXP_3152
    kia "No, ya no."
    kia "Que Solomon quisiera pegarte, cuando lo único que hacías era ayudarme, fue la gota que colmó el vaso."
    mc "Y me culpas por ello. Lo entiendo."
    call BlinkXP ("c19s005_265" , "d") from _call_BlinkXP_3153
    kia "No, no te culpo por ello."
    kia "Tú tan solo me has enseñado que un castillo no tiene por qué ser opresivo. Que puede guardar cosas hermosas en su interior."
    mc "¿Por eso me evitas? Ahora es cuando no entiendo nada."
    call BlinkXP ("c19s005_270" , "d") from _call_BlinkXP_3154
    kia "Aquí tenéis un castillo precioso. Pero también es un palacio. Nadie es prisionero en su propia casa."
    mc "Sigo sin entender qué tiene que ver eso con que me evites."
    call BlinkXP ("c19s005_275" , "d") from _call_BlinkXP_3155
    kia "No sé si es agradecimiento o algo más, pero cada vez que hablo contigo pienso que la vida puede ser diferente de lo que he vivido con Solomon."
    if mc._var("relationships")==1:
        if eil._var("route"):
            kia "Pero ya estás con mi hija... "
        else:
            kia "Pero ya estás con alguien. Una mujer a la que aprecio... Además saliste con mi hija y al volver de la universidad no habéis vuelto juntos."
    elif mc._var("relationships")>1:
        if eil._var("route"):
            kia "Pero estás con más de una mujer. Una de ellas mi hija..."
        else:
            kia "Pero estás con más de una mujer. Y pese a todo no has vuelto con mi hija después de volver de la universidad."
    else:
        kia "Pero saliste con mi hija. Y cuando has vuelto de la universidad no has querido volver con ella."
    kia "No puedo ni siquiera pensar en cómo se sentiría si tú y yo... No. No puedo hacerle eso. Ni siquiera planteármelo."
    mc "Si tú y yo... ¿Qué, Kiara?"
    mcp "(Dilo, Kiara. Aclara las cosas y borra esta barrera que nos está separando.)"
    call BlinkXP ("c19s005_280" , "d") from _call_BlinkXP_3156
    kia "Nada... no es posible, con lo que no vale la pena ni siquiera hablarlo."
    kia "Mañana es el cumpleaños... el de verdad... de [eri] y [dap]. No quiero fastidiárselo. Pero mañana mismo empezaré a buscar algún sitio a donde mudarme."
    mc "¿Por qué? ¿Qué es tan importante como para querer irte de un sitio en el que estás a gusto y donde todo el mundo te quiere?"
    call BlinkXP ("c19s005_285" , "d") from _call_BlinkXP_3157
    kia "No sé si es que no lo estás entendiendo, si tienes un ego tan enorme que me lo quieres oír decir, o si quieres que lo diga para evitar malentendidos."
    mc "Puede haber más razones para querer oírtelo decir."
    mc "Quizás para poder rebatir tu idea de marcharte."
    call BlinkXP ("c19s005_290" , "d") from _call_BlinkXP_3158
    kia "No vas a lograr convencerme..."
    mc "Dime tus razones para irte y yo te expondré mis argumentos para que te quedes."
    mc "Si no te puedo hacer cambiar de opinión, no volveré a insistir."
    call BlinkXP ("c19s005_295" , "h") from _call_BlinkXP_3159
    kia "¡Vale! Vas a conseguir que me avergüence a mí misma como una colegiala, pero si es lo que quieres..."
    call BlinkXP ("c19s005_300" , "d") from _call_BlinkXP_3160
    kia "¿Sabes lo que sentí el otro día? ¿Cuándo me defendiste delante de Solomon?"
    mc "Me lo puedo imaginar. Te sentiste protegida."
    call BlinkXP ("c19s005_305" , "d") from _call_BlinkXP_3161
    kia "Como no me había sentido nunca..."
    scene c19s005_305d with fade
    kia "Esto no lo sabe nadie, pero hace unos años, fuimos a San Francisco para nuestro aniversario a pasar un fin de semana."
    kia "Nos perdimos y acabamos en un sitio sospechoso. Un tipo nos intentó atracar."
    kia "¿Sabes lo que hizo Solomon?"
    mc "Supongo que nada. Darle el dinero. Y entonces llegó la policía."
    call BlinkXP ("c19s005_310" , "f") from _call_BlinkXP_3162
    kia "¿Qué? ¿Cómo sabes lo de la policía? Nunca se lo contamos a Eileen..."
    mc "Has dicho que el tipo intentó atracaros, no que os atracara. He supuesto que, después de que Solomon le diera el dinero, llegó la policía."
    scene c19s005_315d with fade
    kia "Casi has acertado. No le dio el dinero. Me dijo \"corre\" y empezó a correr él también."
    kia "Sin mirar atrás. Sin comprobar si le seguía."
    call BlinkXP ("c19s005_315" , "f") from _call_BlinkXP_3163
    mc "¡Qué hijo de puta!"
    kia "Corrimos durante dos manzanas. Solomon cada vez más lejos. El atracador cada vez más cerca. Yo gritando, pidiendo ayuda."
    scene c19s005_320d with fade
    kia "Y me topé de bruces con dos policías. Solomon había pasado corriendo por su lado sin pararse."
    call BlinkXP ("c19s005_320" , "f") from _call_BlinkXP_3164
    mc "Y el atracador desapareció. Y el hijo de puta de tu marido también."
    call BlinkXP ("c19s005_325" , "d") from _call_BlinkXP_3165
    kia "Exacto. Llegó corriendo al hotel. Estaba a cinco o seis manzanas de donde encontré a los policías."
    kia "Sólo entonces se le ocurrió mirar atrás y descubrió que no estaba. Me llamó al móvil... para ver si estaba bien."
    mc "No sé cómo no le pediste el divorcio en ese mismo momento."
    call BlinkXP ("c19s005_330" , "d") from _call_BlinkXP_3166
    kia "Eileen tenía siete años, [mc]. Yo no tenía trabajo y Solomon aún no bebía como hizo tiempo después."
    kia "Le hubieran concedido la custodia a él. Hubiera perdido a mi hija. Ya me había amenazado con eso..."
    mc "¿Qué? ¿Cuándo?"
    call BlinkXP ("c19s005_335" , "d") from _call_BlinkXP_3167
    kia "Unos meses después de que naciera Eileen. Cuando empecé a ver a mis amigas de nuevo. Me dijo que ya era una mujer con una hija."
    scene c19s005_335d with fade
    kia "Que mi lugar estaba en casa con mi hija, no paseando a la niña y quedando con mis amigas. Si le tenía que dar el sol, teníamos un jardín."
    kia "Que si no quería comportarme como una mujer casada, pediría el divorcio y se quedaría con la niña porque yo no la podía mantener."
    call BlinkXP ("c19s005_335" , "f") from _call_BlinkXP_3168
    mc "Me estoy arrepintiendo de no haberle pegado el jueves."
    call BlinkXP ("c19s005_340" , "d") from _call_BlinkXP_3169
    kia "No tienes que rebajarte a su altura..."
    kia "Pero volviendo a San Francisco... Volví al hotel con los policías. No había denuncia que presentar. Por mi vida no podría recordar el aspecto del atracador."
    kia "Y cuando llegué, ¿sabes qué pasó?"
    mc "Me puedo llegar a imaginar cualquier cosa. Espero que no te pegara encima de haberte dejado sola."
    call BlinkXP ("c19s005_345" , "d") from _call_BlinkXP_3170
    kia "No, por entonces aún no se emborrachaba y no era violento. Pero estaba enfadado."
    kia "Se había puesto nervioso al ver que yo no llegaba al hotel. Estaba enfadado porque yo lo había dejado solo. Porque no había corrido lo suficiente."
    scene c19s005_345d with fade
    kia "Empezó a gritarme... y se fue sin decirme a dónde."
    kia "En nuestro aniversario cenó él solo en el restaurante que había reservado para nosotros y después fue de bar en bar hasta que volvió al hotel."
    scene c19s005_345e with fade
    kia "Mientras tanto, yo estaba en la habitación sin saber si volvería o cuándo lo haría."
    call BlinkXP ("c19s005_350" , "d") from _call_BlinkXP_3171
    mc "¡Es increíble!"
    call BlinkXP ("c19s005_355" , "d") from _call_BlinkXP_3172
    kia "Y catorce años después, por fin tuvo el valor de encararse con un hombre. Y fue el hombre equivocado."
    kia "No estabas haciendo nada malo. Nos estabas ayudando a recoger nuestras cosas. Y quiso pegarte."
    mc "Estaba muy borracho."
    call BlinkXP ("c19s005_360" , "d") from _call_BlinkXP_3173
    kia "Podrías haberte apartado. Decir que no era tu problema. Salir corriendo..."
    kia "Pero no lo hiciste. Me defendiste como no lo hizo mi marido cuando tuvo la oportunidad."
    call BlinkXP ("c19s005_365" , "d") from _call_BlinkXP_3174
    kia "Nos diste un techo cuando más lo necesitábamos. Cuando no teníamos a donde ir."
    kia "Incluso nos dejaste tu cama el día que llegamos y fuiste a dormir a un sofá."
    mc "Es lo menos que podía hacer, ¿no?"
    call BlinkXP ("c19s005_370" , "d") from _call_BlinkXP_3175
    kia "No tenías que hacer nada. No tenías que cedernos tu cama. Ni pelearte con mi marido."
    kia "No tenías ninguna obligación."
    mc "Sí que la tenía, aunque sólo fuera por decencia humana."
    mc "Aunque hubiera hecho lo mismo sin esa obligación. Necesitabais mi ayuda y yo estaba ahí para prestárosla."
    call BlinkXP ("c19s005_375" , "d") from _call_BlinkXP_3176
    kia "A eso me refiero, [mc]. Mi marido salió corriendo en nuestro aniversario. Y un chico sin ninguna obligación lo dejó todo y se enfrentó a él por nosotras."
    kia "Por mí."
    mc "No sé cómo lo estás viendo tú, pero yo cada vez lo veo peor como razón para querer irte."
    call BlinkXP ("c19s005_380" , "d") from _call_BlinkXP_3177
    kia "*Risa triste* No, esa es la razón que ha creado la razón para querer irme."
    kia "Después de sentirme tratada como un pedazo de mierda por mi marido durante años... llegas tú y me tratas como a una persona."
    kia "Me enseñas cómo funciona una familia. Me lo enseñáis entre todos."
    mc "Bueno, no se puede decir que seamos una familia ejemplar..."
    call BlinkXP ("c19s005_385" , "d") from _call_BlinkXP_3178
    kia "No, pero todos os queréis y os protegéis. Todos os ayudáis. Y tú estás en todos sitios. Sólo había que verte durante la comida."
    kia "¿Ha habido alguna chica con quién no hayas hablado hoy? ¿A alguien a quién hayas dejado de lado?"
    mc "Creo que no... y si lo ha habido debería compensarla."
    call BlinkXP ("c19s005_390" , "d") from _call_BlinkXP_3179
    kia "Pues todas esas cosas hacen que esté empezando a albergar sentimientos por ti que no deberían estar ahí."
    kia "Ya está. Ya lo he dicho."
    call BlinkXP ("c19s005_395" , "d") from _call_BlinkXP_3180
    kia "Por eso te he estado evitando. No quiero que esos sentimientos crezcan."
    if eil._var("route"):
        kia "Con la relación que tienes con mi hija, no puedo permitirme enamorarme de ti y... Sencillamente, no puedo."
    else:
        kia "Después de la relación que tuviste con mi hija... no puedo permitirme enamorarme de ti. ¿Cómo se sentiría después de que no hayas vuelto con ella?"
    mc "Y ¿cómo llevas lo de que los sentimientos no crezcan? Ya llevas tres días evitándome."
    call BlinkXP ("c19s005_400" , "d") from _call_BlinkXP_3181
    kia "Fatal... Sólo espero que cuando me mude podamos seguir siendo amigos."
    if persistent.walkthrough:
        $ wt1 = _("Ruta con Kiara pre-abierta.")
        $ wt2 = _("Ruta con Kiara cerrada. \n{b}Advertencia:{/b} No habrá más posibilidades de abrir la ruta.")
    else:
        $ wt1 = ""
        $ wt2 = ""
    menu:
        "No me parece bien." (wt = wt1):
            $ kia._var("route" , True)
        "Me parece bien." (wt = wt2):
            pass
    $ resetWalkthrough ()
    if kia._var("route"):
        mc "Yo también estoy empezando a albergar sentimientos por ti. Pero en mi caso, no me avergüenzo de ellos."
        call BlinkXP ("c19s005_405" , "d") from _call_BlinkXP_3182
        kia "¿Qué? ¿Desde cuándo?"
        mc "Desde que he tenido la oportunidad de conocerte mejor. Conocerte como mujer, no como la madre de mi novia del instituto."
        mc "Desde que sé por lo que has pasado. Desde que pude ver a Solomon en el momento en que más asco daba."
        mc "Llámalo complejo del caballero de brillante armadura o como quieras. Pero aquel día algo hizo clic en mí."
        call BlinkXP ("c19s005_410" , "d") from _call_BlinkXP_3183
        kia "Pero... ¿qué pasa con Eileen?"
        if eil._var("route"):
            mc "Podemos hablar con ella. Si a ninguna de las dos os importa que la otra esté conmigo, no veo dónde puede estar el problema."
        else:
            mc "Ella y yo tuvimos nuestro momento. Fuimos felices. ¿Crees que, si quieres estar conmigo, te va a negar la oportunidad de tener la felicidad que ella tuvo?"
            mc "Creo que es algo que podemos hablar los tres, si quieres."
        mcp "(Sabiendo que Eileen quiere que estés lo más lejos posible de Solomon, va a superar cualquier reparo que tenga.)"
        call BlinkXP ("c19s005_415" , "d") from _call_BlinkXP_3184
        if mc._var("relationships") == 1 and not eil._var("route"):
            kia "¿Y con tu novia? No podría aceptar ser \"la otra\", ni hacerle daño o engañarla a sus espaldas."
            mc "Podemos hablar con ella también. Si a ella no le importa, y a ti tampoco, no veo dónde puede estar el problema."
        elif mc._var("relationships") > 1:
            kia "¿Y con tu harén?"
            mc "¿Crees que no te van a aceptar en el harén? ¿Has visto algún problema con las revelaciones de hoy?"
        call BlinkXP ("c19s005_420" , "d") from _call_BlinkXP_3185
        kia "Haces que todo parezca tan fácil... pero no lo es."
        mc "Hagamos una cosa... empecemos hablando con Eileen. Después puedes tomar una decisión. Pero que esa decisión no incluya mudarte, por favor."
    else:
        mc "Siempre vamos a ser amigos, Kiara. A mí siempre me has caído bien, pero no creo que debamos ir más allá de ser amigos."
        call BlinkXP ("c19s005_410" , "d") from _call_BlinkXP_3186
        kia "Eso ayuda..."
        if mc._var("relationships") > 1:
            kia "Después de ver que sales con más de una mujer... casi había empezado a albergar esperanzas. Aunque me negara a aceptarlas."
        mc "Te quiero, pero no así. Te quiero porque eres una mujer maravillosa y siempre me vas a tener a tu lado para lo que necesites."
        mc "Pero no puedo tener una relación contigo. Comparto varios de tus reparos."
        call BlinkXP ("c19s005_420" , "d") from _call_BlinkXP_3187
        kia "Y hasta aquí ha llegado esta conversación, ¿no?"
        mc "Aún queda lo de irte de la casa. Yo me voy a ir a Aruba en unas semanas, con lo que no creo que debas hacerlo. Vas a estar mejor aquí que en cualquier otro sitio."
    call BlinkXP ("c19s005_425" , "d") from _call_BlinkXP_3188
    kia "Creo que debería irme igualmente. De todas formas, en septiembre deberemos dejar la habitación libre para las estudiantes nuevas..."
    mc "Pero yo no estaré. Podéis usar mi habitación mientras esté en Aruba. No hay ninguna prisa en que os vayáis."
    call BlinkXP ("c19s005_430" , "d") from _call_BlinkXP_3189
    kia "Pero volverás. No podemos pedirte que duermas en el sofá eternamente. Igualmente tendremos que irnos a algún sitio."
    stop music fadeout (1.5)
    mc "Lo entiendo, pero no tomes ninguna decisión precipitada. Creo que se me está ocurriendo una idea."
    play music ("music/Sunny-Skies.ogg")
    call BlinkXP ("c19s005_435" , "d") from _call_BlinkXP_3190
    mad "Hola, ¿interrumpo algo?"
    mc "Hola de nuevo, Maddie. No, no te preocupes. ¿Necesitas algo?"
    call BlinkXP ("c19s005_440" , "d") from _call_BlinkXP_3191
    mad "Estamos haciendo un juego en el Jacuzzi y venía a preguntarle a Kiara si se quería apuntar."
    mc "¿Sólo Kiara?"
    mad "Es un juego solo de chicas, [mc]. Lo siento. Algo para crear más vínculos entre nosotras."
    call BlinkXP ("c19s005_445" , "d") from _call_BlinkXP_3192
    kia "¡Me apunto! ¿De qué va el juego?"
    call BlinkXP ("c19s005_455" , "d") from _call_BlinkXP_3193
    mad "Mejor te lo explico por el camino. Ya estamos unas cuantas allí."
    call BlinkXP ("c19s005_450" , "d") from _call_BlinkXP_3194
    kia "Te veo luego, [mc]. Me tienes que explicar esa idea que has tenido."
    mc "Perfecto."
    scene c19s005_460An with dissolve
    "Kiara cruza la piscina a nado y se va junto a Maddie hacia el Jacuzzi."
    mcp "(Al menos ha quedado aclarado el tema de Kiara. A ver cómo evoluciona.)"
    return
label c19s005_KateNorah:
    if _in_replay:
        $ mc._var("relationships", 0, intention = "set")
        menu:
            "¿Estás en una relación con [nor]?"
            "Sí, la dejé entrar en la ducha.":
                $ nor._var("route", True)
                $ nor._var("routeSecondChance", False)
                $ mc._var("relationships", 1)
            "Sí, pero no la dejé entrar en la ducha.":
                $ nor._var("route", True)
                $ nor._var("routeSecondChance", True)
                $ mc._var("relationships", 1)
            "No":
                $ nor._var("route", False)
        menu:
            "¿Estás en una relación con Samantha?"
            "Sí":
                $ mad._var("route" , True)
                $ mc._var("relationships", 1)
            "No":
                $ mad._var("route" , False)
        if mc._var("relationships") < 2:
            menu:
                "¿En cuántas relaciones estás?"
                "Más de una":
                    $ mc._var("relationships", 2, intention = "set")
                "Una":
                    $ mc._var("relationships", 1, intention = "set")
                "Ninguna" if mc._var("relationships")==0:
                    $ mc._var("relationships", 0, intention = "set")
    scene c19s005_600a with fade
    "Buscas a Eileen con la mirada, pero no la ves por ningún lado. Supones que estará en el juego del jacuzzi."
    "Cada vez quedan menos chicas en la piscina. Te acercas a Kate y a [nor]."
    scene c19s005_600b with dissolve
    if mc._var("relationships")>1:
        kat "Aquí llega mi héroe. *Risa* Salir con una de las preciosidades de esta familia ya es un triunfo. Tú lo haces con más de una."
        mc "No es heroísmo. *Risa* Es suerte."
        if nor._var("route"):
            mc "Y me refiero a suerte por mi parte. Estar con alguien como [nor] es increíble."
            nor "Gracias, mi amor."
        else:
            mc "Y me refiero a suerte por mi parte."
            nor "Por tu parte y por la de ellas."
    elif mc._var("relationships")==1:
        kat "Aquí llega el hombre del día. *Risa* Que hayas conseguido una relación en esta familia es para felicitarte."
        if nor._var("route"):
            mc "Gracias. No podría estar con nadie mejor. *Risa* Y no lo digo porque esté delante."
            nor "Gracias, mi amor."
        else:
            mc "Gracias, Kate. Soy un hombre con suerte."
            nor "Y ella también, [mc]. No lo olvides."
    else:
        kat "Aquí llega el hombre más desafortunado del mundo. *Risa* La única mujer que le escribe y es un número equivocado."
        mc "No sabemos si escribía una mujer o un hombre. *Risa*"
        nor "En eso tienes razón, pero todas hemos pensado que era una chica."
    call BlinkXP ("c19s005_605" , "d") from _call_BlinkXP_3195
    kat "Desde La Revelación te he visto hablar con Tía Betty, Amanda, Olivia, y Kiara."
    if mc._var("relationships") > 1:
        kat "Ninguna está en tu harén..."
    if mc._var("relationships") > 0:
        kat "Supongo que te han ametrallado a preguntas, con lo que no lo voy a hacer yo."
    else:
        kat "Supongo que lo de Meemaw se ha convertido en la comidilla del día."
    mc "El tema de conversación ha salido, pero hemos hablado de otros temas que teníamos pendientes. No todo gira alrededor de La Revelación."
    call BlinkXP ("c19s005_610" , "d") from _call_BlinkXP_3196
    nor "Son estas cosas por las que no se deberían soltar noticias bomba en una fiesta familiar. Absorben las conversaciones."
    mc "Por otro lado, es el mejor momento. Ahora ya lo sabe todo el mundo."
    call BlinkXP ("c19s005_615" , "d") from _call_BlinkXP_3197
    mc "Pero cambiemos de tema y volvamos a la fiesta. ¿Qué tal tu primera experiencia con una fiesta con toda la familia?"
    kat "Te recuerdo que estuve en la playa en Navidad. *Risa*"
    mc "*Risa* Lo sé, pero ahora la familia ha crecido. Al menos hasta que lleguen las chichas nuevas, creo que no van a aparecer nuevos miembros."
    call BlinkXP ("c19s005_620" , "d") from _call_BlinkXP_3198
    kat "En eso tienes razón. Megan, Amanda, Eva... No estuvieron en la playa, pero son parte de esto."
    if mad._var("route"):
        kat "Y Maddie supongo que también, saliendo contigo... pero se la ve cohibida aún."
    else:
        kat "Y creo que Maddie también podría unirse si le damos la oportunidad. Es muy buena chica."
    call BlinkXP ("c19s005_625" , "d") from _call_BlinkXP_3199
    nor "No la conocía mucho, más allá de comprarle ropa, pero es una chica muy agradable."
    mc "Lo es. Y creo que se está integrando bien hoy. Al menos para ser su primera vez."
    call BlinkXP ("c19s005_680" , "d") from _call_BlinkXP_3200
    kat "Cambiando de tema, cuando te vayas a Aruba, ¿quién se ocupará de lo que haces tú en el Dormitorio?"
    kat "Creo que entre todas podríamos ayudar para que [mar] y [nor] no tengan demasiado trabajo."
    mc "No te preocupes. Vosotras tenéis vuestros estudios. Y la contabilidad la puedo seguir haciendo desde allí. No lleva mucho tiempo."
    if nor._var("route"):
        mc "Ahora mismo es mi trabajo principal. Bueno, y hacer de taxista. *Risa*"
        call BlinkXP ("c19s005_630" , "d") from _call_BlinkXP_3201
        kat "¿Puedo preguntar cómo empezasteis a salir juntos vosotros dos? ¿Y cómo habéis conseguido ocultarlo?"
        kat "Si me hubieran dicho que salías con una de las chicas Marks, seguramente [nor] hubiera sido mi última elección."
        kat "Bueno, no la última... nunca hubiese pensado en Olivia o Betty tampoco."
        mc "Bueno, todo empezó mientras pintábamos la habitación de Saira."
        call BlinkXP ("c19s005_635" , "d") from _call_BlinkXP_3202
        nor "Después yo me metí en el baño dónde se estaba duchando después de pintar."
        if not nor._var("routeSecondChance"):
            nor "Y me metí en la ducha con él."
        else:
            nor "No pasó nada, pero nos dio pie a hablar."
        call BlinkXP ("c19s005_640" , "d") from _call_BlinkXP_3203
        kat "¿Qué? ¡No puede ser! ¡Yo nunca me atrevería a algo así!"
        call BlinkXP ("c19s005_645" , "d") from _call_BlinkXP_3204
        kat "¿Y tú no sabes que existen los pestillos?"
        mc "*Risa* El de ese baño estaba roto. Me alegra que lo estuviera."
    else:
        mc "Y para las pequeñas reparaciones pueden llamar a alguien para que las haga."
        call BlinkXP ("c19s005_685" , "d") from _call_BlinkXP_3205
        nor "Los pestillos de los baños están aguantando bien. Y eso que ahora hay mucho más tráfico en esos baños que antes."
        call BlinkXP ("c19s005_690" , "d") from _call_BlinkXP_3206
        kat "¿Teníais roto algún pestillo antes de que nosotras llegáramos?"
        call BlinkXP ("c19s005_635" , "d") from _call_BlinkXP_3207
        nor "Sí, yo una vez pillé a [mc] duchándose. El día que pintamos la habitación de Saira."
        mc "¡Es verdad! ¡Casi ni me acordaba!"
    call BlinkXP ("c19s005_650" , "d") from _call_BlinkXP_3208
    kat "Mmmm... ¿Qué baño es el que tiene el pestillo roto?"
    mc "*Risa* Ahora ninguno. Arreglé el de la planta baja pocos días antes de que llegarais, y puse uno en vuestra planta."
    mc "Los únicos que no tienen son los de las habitaciones de [mar] y Saira, y el del gimnasio."
    mc "No estás pensando en meterte en algún baño mientras alguna de las chicas se ducha, ¿verdad?"
    call BlinkXP ("c19s005_655" , "d") from _call_BlinkXP_3209
    kat "¿Qué? ¿Alguna de las chicas? ¡No!"
    kat "Sólo lo decía en caso de... en caso de... en caso de tener que atrancar la puerta o algo."
    mc "*Risa* Yo siempre llamo antes de entrar en un baño, no te preocupes. Crecí rodeado de chicas."
    call BlinkXP ("c19s005_660" , "d") from _call_BlinkXP_3210
    nor "Y si quieres pillar a [mc] duchándose, tu mejor opción es el baño del gimnasio."
    if nor._var("route"):
        nor "Es el primero que probé yo, pero por entonces había menos gente en la casa. Se estaba duchando en otro."
        mc "No creo que Kate tenga ningún interés en pillarme en la ducha, mi vida."
    else:
        mc "No creo que Kate tenga ningún interés en pillarme en la ducha, [nor]."
    call BlinkXP ("c19s005_665" , "h") from _call_BlinkXP_3211
    if nor._var("route"):
        kat "¡Por supuesto que no! ¡Además, ya estás con [nor]!"
    elif mc._var("relationships")==1:
        kat "¡Por supuesto que no! ¡Además, ya estás con alguien!"
    elif mc._var("relationships")>1:
        kat "¡Por supuesto que no! ¡Además, tú ya tienes tu harén!"
    else:
        kat "¡Por supuesto que no! ¡Además, saliste con Eileen y Saira!"
    call BlinkXP ("c19s005_670" , "d") from _call_BlinkXP_3212
    nor "*Risa*"
    mc "¿Qué pasa, [nor]?"
    call BlinkXP ("c19s005_675" , "d") from _call_BlinkXP_3213
    if nor._var("route"):
        nor "Nada, mi amor. Pero creo que deberías ir a hablar con otras chicas antes de que piensen que te monopolizamos."
    else:
        nor "Nada, cielo. Pero creo que deberías ir a hablar con otras chicas antes de que piensen que te monopolizamos."
    mcp "(No soy tan obtuso como para no darme cuenta de cuando quieren hablar a solas.)"
    stop music fadeout (1.5)
    mc "De acuerdo. Además, tenía que hablar con Eileen, y veo que está ahí, hablando con Lisa."
    mc "Os veo luego, chicas."
    return
label c19s007_KateWithNor:
    if _in_replay:
        $ mc._var("relationships", 0, intention = "set")
        menu:
            "¿Estás en una relación con [nor]?"
            "Sí":
                $ nor._var("route", True)
                $ mc._var("relationships", 1)
            "No":
                $ nor._var("route", False)
        if mc._var("relationships") > 0:
            menu:
                "¿Alguien reveló que estaba esperando un hijo tuyo?"
                "Sí, una chica":
                    $ Aux2 = 1
                "Sí, más de una chica":
                    $ Aux2 = 2
                "No":
                    $ Aux2 = 0
        menu:
            "¿Tienes Puntos de Relación positivos con Kate?"
            "Sí":
                $ kat._var("relationshipPoints", 5, intention = "set")
            "No, un poco negativos":
                $ kat._var("relationshipPoints", -4, intention = "set")
        if mc._var("relationships") < 2:
            menu:
                "¿En cuántas relaciones estás?"
                "Más de una":
                    $ mc._var("relationships", 2, intention = "set")
                "Una":
                    $ mc._var("relationships", 1, intention = "set")
                "Ninguna" if mc._var("relationships")==0:
                    $ mc._var("relationships", 0, intention = "set")
    scene black with fade
    stop music fadeout (1.5)
    "Mientras tú hablabas con Eileen..."
    play music ("music/Separation.ogg")
    call BlinkXP ("c19s007_005" , "d") from _call_BlinkXP_3214
    nor "Te gusta, ¿verdad?"
    call BlinkXP ("c19s007_010" , "d") from _call_BlinkXP_3215
    kat "¿Qué? ¡No! No sé si lo sabes, pero a mí me gustan las mujeres, no los hombres."
    call BlinkXP ("c19s007_015" , "d") from _call_BlinkXP_3216
    nor "Sabes que te pueden gustar las mujeres... y [mc], ¿verdad?"
    nor "No es necesario que te gusten el resto de los hombres."
    call BlinkXP ("c19s007_020" , "d") from _call_BlinkXP_3217
    kat "No sé de dónde has sacado la ridícula idea de que me puede gustar [mc]."
    call BlinkXP ("c19s007_025" , "d") from _call_BlinkXP_3218
    nor "De hace un momento. Cuando has dicho ese vehemente \"por supuesto que no\"."
    if nor._var("route"):
        nor "Tu razón para ese \"por supuesto que no\" es que está conmigo."
    elif mc._var("relationships")==1:
        nor "Tu razón para ese \"por supuesto que no\" es con quién sale."
    elif mc._var("relationships")>1:
        nor "Tu razón para ese \"por supuesto que no\" es que tiene un harén."
    else:
        nor "Tu razón para ese \"por supuesto que no\" es con quién salió en el pasado."
    nor "Sólo estábamos hablando de pillarlo desnudo, no de salir con él. No debería importar... a menos que te guste."
    call BlinkXP ("c19s007_030" , "d") from _call_BlinkXP_3219
    kat "Supongo que lo consideraba algún tipo de traición... pillarlo desnudo a propósito, me refiero."
    call BlinkXP ("c19s007_035" , "d") from _call_BlinkXP_3220
    nor "¿Sabes lo que realmente sería una traición? Que no aceptaras lo que sientes."
    nor "Sería una traición a ti misma."
    call BlinkXP ("c19s007_040" , "d") from _call_BlinkXP_3221
    kat "Pero..."
    call BlinkXP ("c19s007_045" , "d") from _call_BlinkXP_3222
    nor "No hay peros, Kate. Si, sé que te gustan las mujeres. Todas lo sabemos."
    nor "Cuando [eri] pidió la fiesta topless, se te caía la baba mientras [mar] la autorizaba."
    nor "Te pasaste el resto de la cena imaginándonos a todas en topless."
    call BlinkXP ("c19s007_050" , "d") from _call_BlinkXP_3223
    kat "Lo siento... creía que había sido más discreta."
    call BlinkXP ("c19s007_055" , "d") from _call_BlinkXP_3224
    nor "No pasa nada, cielo. La discreción no es lo tuyo, pero no pasa nada."
    nor "Lo estoy diciendo porque hoy, con doce o trece chicas en topless, nos has dedicado menos miradas de las que todas esperábamos."
    nor "Has pasado más tiempo mirando a [mc] que a nosotras."
    call BlinkXP ("c19s007_060" , "d") from _call_BlinkXP_3225
    kat "*Risa* Eso es porque hoy he sido más discreta mirando."
    call BlinkXP ("c19s007_065" , "d") from _call_BlinkXP_3226
    nor "*Risa* No, Kate, no lo has sido."
    nor "Creo que te he pillado mirándome los pechos unas seis veces. Y mis ojos están aquí arriba. *Risa* Siete."
    call BlinkXP ("c19s007_070a" , "d") from _call_BlinkXP_3227
    kat "Lo siento..."
    kat "Como Jamaal ha dicho, mi cerebro lésbico está confundido."
    call BlinkXP ("c19s007_070b" , "d") from _call_BlinkXP_3228
    kat "No por un exceso de tetas. De esas nunca hay suficientes. Pero es que [mc] me confunde."
    if kat.rps > 0:
        kat "Me cae muy bien, se porta genial conmigo... no es el concepto de hombre que siempre he tenido."
    else:
        kat "Aún no lo tengo calado. La mayoría de las veces no me cae bien, pero tengo que reconocer que no es el concepto de hombre que siempre he tenido."
    call BlinkXP ("c19s007_075" , "d") from _call_BlinkXP_3229
    nor "[mc] es cualquier cosa menos el hombre estándar. Creo que deberías hablar con él."
    call BlinkXP ("c19s007_080" , "d") from _call_BlinkXP_3230
    if nor._var("route") and mc._var("relationships")==1:
        kat "¿Para qué? Ya está contigo..."
        if nor._var("pregnancyDiscovered"):
            kat "Y estáis esperando un hijo..."
        call BlinkXP ("c19s007_085" , "d") from _call_BlinkXP_3231
        nor "Como mínimo para aclarar las cosas que tienes en la cabeza."
        nor "No tienes que preocuparte por mí. No soy la dueña de [mc]."
        nor "Lo amo con locura, pero cuando empezamos a salir no me prometió exclusividad. Ni yo se la exigí."
    elif mc._var("relationships")==1:
        kat "¿Para qué? Ya está con alguien..."
        if Aux2 > 0:
            kat "Y están esperando un hijo..."
        call BlinkXP ("c19s007_085" , "d") from _call_BlinkXP_3232
        nor "Como mínimo para aclarar las cosas que tienes en la cabeza."
        nor "Si ves que puede haber alguna posibilidad para vosotros, deberías hablar con ella. Pero primero debes hablar con [mc]."
    elif mc._var("relationships")>1:
        kat "¿Para qué? Ya tiene su harén... yo no pinto nada ahí."
        if Aux2 == 1:
            kat "Y tiene un hijo en camino..."
        elif Aux2 > 1:
            kat "Y tiene varios hijos en camino..."
        call BlinkXP ("c19s007_085" , "d") from _call_BlinkXP_3233
        nor "Como mínimo para aclarar las cosas que tienes en la cabeza."
        nor "Si ves que puede haber alguna posibilidad para vosotros, quizás deberías hablar con el resto de las chicas."
        if nor._var("route"):
            nor "Yo no tendría ningún problema en que tú también estuvieras en el harén."
    else:
        kat "¿Para qué? Si no está con nadie... debe ser porque no quiere, ¿no?"
        call BlinkXP ("c19s007_085" , "d") from _call_BlinkXP_3234
        nor "Como mínimo para aclarar las cosas que tienes en la cabeza."
        nor "No puedes saber si no está con nadie porque está esperando que alguien se decida a hablar."
    call BlinkXP ("c19s007_090" , "d") from _call_BlinkXP_3235
    kat "Haces que todo suene tan lógico... pero es que, además, hay también una chica..."
    scene c19s007_090d with dissolve
    "Kate y [nor] hablan largo y tendido sobre las dudas que acucian a Kate y cómo encararlas."
    stop music fadeout (1.5)
    "Se pasan el resto de la tarde hablando. Al menos hasta que un evento externo corte su conversación."
    return
label c19s007_EileenLisa:
    if _in_replay:
        $ nor._var("route" , False)
        $ mc._var("relationships", 0, intention = "set")
        menu:
            "¿Estás en una relación con [dap]?"
            "Sí":
                $ dap._var("route" , True)
                $ mc._var("relationships", 1)
                menu:
                    "¿Estás en una relación con [nor]?"
                    "Sí":
                        $ nor._var("route" , True)
                        $ mc._var("relationships", 1)
                    "No":
                        $ nor._var("route" , False)
            "No":
                $ dap._var("route" , False)
        menu:
            "¿Estás en una relación con [mar!t]?"
            "Sí":
                $ mar._var("route" , True)
                $ mc._var("relationships", 1)
                menu:
                    "¿Estás en una relación con [emm]?"
                    "Sí":
                        $ emm._var("route" , True)
                        $ mc._var("relationships", 1)
                    "No":
                        $ emm._var("route" , False)
            "No":
                $ mar._var("route" , False)
        menu:
            "¿Estás en una relación con [eri]?"
            "Sí":
                $ eri._var("route" , True)
                $ mc._var("relationships", 1)
                if not nor._var("route"):
                    menu:
                        "¿Estás en una relación con [nor]?"
                        "Sí":
                            $ nor._var("route" , True)
                            $ mc._var("relationships", 1)
                        "No":
                            $ nor._var("route" , False)
            "No":
                $ eri._var("route" , False)
        menu:
            "¿Estás en una relación con Eileen?"
            "Sí":
                $ eil._var("route" , True)
                $ mc._var("relationships", 1)
            "No":
                $ eil._var("route" , False)
        menu:
            "¿Estás en una relación con Samantha?"
            "Sí":
                $ sam._var("route" , True)
                $ mc._var("relationships", 1)
                menu:
                    "¿Estás en una relación con Simone?"
                    "Sí":
                        $ sim._var("route" , True)
                        $ mc._var("relationships", 1)
                    "No":
                        $ sim._var("route" , False)
            "No":
                $ sam._var("route" , False)
        menu:
            "¿Has pre-abierto la relación con Kiara?"
            "Sí":
                $ kia._var("route" , True)
            "No":
                $ kia._var("route" , False)
        if mc._var("relationships") < 2:
            menu:
                "¿En cuántas relaciones estás (sin contar a Kiara)?"
                "Más de una":
                    $ mc._var("relationships", 2, intention = "set")
                "Una":
                    $ mc._var("relationships", 1, intention = "set")
                "Ninguna" if mc._var("relationships")==0:
                    $ mc._var("relationships", 0, intention = "set")
    scene c19s007_100a with dissolve
    play music ("music/Sunny-Skies.ogg")
    mc "Hola, chicas. ¿Interrumpo algo?"
    eil "No, que va. Lisa me estaba pidiendo que me uniera al juego en el jacuzzi."
    lis "Está siendo muy divertido."
    mc "¿A qué estáis jugando?"
    call BlinkXP ("c19s007_105" , "d") from _call_BlinkXP_3236
    lis "Es una cosa que se le ha ocurrido a Simone. Como hoy la cosa parece que iba de secretos..."
    lis "Todas tenemos que contar un secreto y votamos por el más jugoso."
    lis "La que ha contado el menos jugoso tiene que pagar prenda o se le encarga una tarea... y se pierde los secretos que se cuenten. Mi tarea es conseguir que Eileen se una a nosotras."
    mc "Ahora entiendo por qué yo no estaba invitado. *Risa* ¿No os vais a quedar sin secretos?"
    call BlinkXP ("c19s007_110" , "d") from _call_BlinkXP_3237
    lis "Ahí está lo divertido del juego. En saber cuándo contar los secretos más jugosos y cuándo los menos."
    lis "Si has perdido tu top, puedes recuperarlo si tu secreto es el mejor."
    call BlinkXP ("c19s007_115" , "d") from _call_BlinkXP_3238
    eil "Si hubiera sabido antes a qué estaban jugando, me hubiera apuntado sin que me vinieran a buscar. *Risa*"
    eil "Es una forma genial de conocernos más entre nosotras."
    mc "Antes de que os vayáis, ¿puedo hablar un momento contigo, Eile?"
    call BlinkXP ("c19s007_120" , "d") from _call_BlinkXP_3239
    lis "Os espero aquí sentada. No puedo volver con las manos vacías o volveré a perder mi top."
    stop music fadeout (1.5)
    mc "Solo serán dos minutos, no te preocupes."
    call BlinkXP ("c19s007_125" , "f") from _call_BlinkXP_3240
    play music ("music/Retrospection.ogg")
    eil "Dime, supongo que es sobre mi madre."
    eil "Os he visto antes, hablando."
    mc "Sí, sigue empeñada en mudarse. Al menos ya no quiere volver a vuestra casa."
    mc "He conseguido que retrase la decisión. Al menos por unos días."
    call BlinkXP ("c19s007_130" , "d") from _call_BlinkXP_3241
    eil "Gracias, [mc]. No sé cómo lo has conseguido, pero gracias."
    eil "Estar aquí le está haciendo mucho bien, e irnos ahora sería un error."
    mc "Tengo una idea que podría resolverlo todo, pero tengo que atar unos cabos sueltos antes."
    call BlinkXP ("c19s007_185" , "d") from _call_BlinkXP_3242
    eil "¿Que nos mudemos con Tía Betty y Yaya Olivia?"
    mc "¿Yaya Olivia? ¡Eso es nuevo!"
    call BlinkXP ("c19s007_190" , "d") from _call_BlinkXP_3243
    eil "*Risa* Sí. Lexi ha empezado a llamarla así. Yaya es abuela en español, creo. Pienso que se le va a quedar el nombre."
    mc "¡Es genial! Eso muestra que el cariño en esta familia va en todos los sentidos."
    mc "Meemaw se ha emocionado mucho con todos los abrazos."
    call BlinkXP ("c19s007_195" , "d") from _call_BlinkXP_3244
    eil "Claro que va en todos los sentidos. Todas nos hemos sentido aliviadas cuando ha unido las palabras cáncer y limpia."
    eil "Pero a lo que íbamos. ¿Esa ha sido tu idea? ¿Que nos mudemos con ellas?"
    mc "Sí, sería bueno que hablarais sobre ello."
    call BlinkXP ("c19s007_200" , "d") from _call_BlinkXP_3245
    eil "A mí también se me había ocurrido y quería hablar con ellas un día de estos. Pagarles un alquiler o algo por una habitación."
    eil "Por alguna razón mi madre no quiere seguir viviendo aquí. Posiblemente con Olivia y Tía Betty le parezca mejor."
    mc "Las grandes mentes piensan igual. *Risa* Y te has olvidado lo de Yaya..."
    if kia._var("route"):
        mc "Pero hay otra cosa..."
        call BlinkXP ("c19s007_135" , "d") from _call_BlinkXP_3246
        eil "Me das miedo cuando lo dices así. ¿Qué ha pasado?"
        if eil._var("route"):
            if mc._var("relationships")==1:
                mc "Ya has visto que sólo estoy contigo..."
                call BlinkXP ("c19s007_140" , "d") from _call_BlinkXP_3247
                eil "Sí..."
                mc "Pero aquel día, en el bosque, hablaste de un harén, y de ser la Primera Concubina..."
                eil "Sí..."
            else:
                mc "Ahora ya sabes quién forma parte del harén..."
                call BlinkXP ("c19s007_140" , "d") from _call_BlinkXP_3248
                eil "Sí..."
                mc "Recuerdo aquel día, en el bosque, cuando hablaste de ser la Primera Concubina..."
                eil "Sí..."
        else:
            mc "Tú y yo fuimos felices en el instituto..."
            call BlinkXP ("c19s007_140" , "d") from _call_BlinkXP_3249
            eil "Sí..."
            mc "Y, cuando rompimos, prometimos no inmiscuirnos en las futuras relaciones del otro..."
            eil "Sí..."
        mc "Creo que deberías hablar con Kiara sobre ello."
        call BlinkXP ("c19s007_145" , "h") from _call_BlinkXP_3250
        eil "¿Qué? ¿Tú y mi madre?"
        mc "No, no estamos juntos, no te preocupes."
        call BlinkXP ("c19s007_150" , "d") from _call_BlinkXP_3251
        eil "No entiendo de qué quieres que hable con ella, entonces."
        mc "De cual sería tu posición si lo estuviéramos."
        call BlinkXP ("c19s007_155" , "d") from _call_BlinkXP_3252
        eil "¿Me estás pidiendo permiso para salir con mi madre? *Risa* ¿No solía ser al revés?"
        mc "En cierto modo, sí. También te estoy pidiendo que hables con ella para despejar sus dudas sobre cómo te sentirías si lo hiciéramos."
        call BlinkXP ("c19s007_160" , "d") from _call_BlinkXP_3253
        eil "Sabes que va a ser rarísimo tener esa conversación, ¿verdad?"
        mc "Me lo imagino, pero a ella le preocupa."
        if not eil._var("route"):
            mc "Le preocupa como te sentirías si ella y yo empezáramos algo teniendo en cuenta que tú y yo no hemos vuelto."
        elif mc._var("relationships")==1:
            mc "Le preocupa que la percibas como \"la otra\". Cómo te sentirías si saliera con las dos."
        else:
            mc "Le preocupa tener que compartir harén contigo."
        call BlinkXP ("c19s007_165" , "d") from _call_BlinkXP_3254
        if eil._var("route"):
            eil "¡Joder! ¡A mí también me preocuparía! ¡Compartir hombre con mi madre no es normal!"
        else:
            eil "¡Joder! ¡A mí también me preocuparía! ¡Primero sales con la hija y después con la madre!"
        $ Aux = False
        $ Aux3 = True
        if mar._var("route") and emm._var("route"):
            $ Aux = True
        else:
            $ Aux3 = False
        if nor._var("route") and eri._var("route"):
            $ Aux = True
        else:
            $ Aux3 = False
        if nor._var("route") and dap._var("route"):
            $ Aux = True
        else:
            $ Aux3 = False
        if sam._var("route") and sim._var("route"):
            $ Aux = True
        else:
            $ Aux3 = False
        if Aux:
            eil "Aunque no seamos la primera pareja madre e hija con la que estás."
            call BlinkXP ("c19s007_170" , "d") from _call_BlinkXP_3255
            if Aux3:
                if persistent.family:
                    eil "Sólo te quedarían Olivia y [nor], y Olivia y [mar]."
                    if nor._var("route") and mar._var("route"):
                        eil "Y con las hijas ya estás... te faltaría añadir a Olivia al harén."
                else:
                    eil "Sólo te quedarían Olivia y [nor]."
                    if nor._var("route"):
                        eil "Y con [nor] ya estás... te faltaría añadir a Olivia al harén."
        else:
            call BlinkXP ("c19s007_170" , "d") from _call_BlinkXP_3256
        eil "Esto es muy raro, [mc]."
        mc "Lo es. Pero hablarás con ella, ¿verdad?"
        call BlinkXP ("c19s007_175a" , "d") from _call_BlinkXP_3257
        eil "¡Claro que hablaré con ella! Es raro, pero también creo que puedes ser muy bueno para ella."
        eil "Y ella para ti. Por raro que parezca. Aunque no va a ser una conversación fácil. Me pones en una situación complicada."
        mc "Gracias, Eileen. ¿Realmente no te importa? Lo último que querría es que te sientas incómoda."
        call BlinkXP ("c19s007_175b" , "d") from _call_BlinkXP_3258
        eil "Después de todo lo que hemos pasado juntos, ¿aún dudas de si te voy a ayudar a salir con mi madre?"
        eil "Hace unos días me hubiera hecho sentir incómoda, como bien dices, pero ya no. Ahora entiendo muchas cosas sobre cómo se siente mi madre."
        call BlinkXP ("c19s007_175c" , "d") from _call_BlinkXP_3259
        eil "No sé si se dice así o no, pero tenéis mi bendición. *Risa*"
        mc "*Risa* Creo que ya no se usa esa frase, pero gracias."
        call BlinkXP ("c19s007_180" , "d") from _call_BlinkXP_3260
        eil "¿Sabes dónde está?"
        mc "En el jacuzzi. Maddie la ha venido a buscar para que se uniera al juego hace un rato."
        call BlinkXP ("c19s007_185b" , "d") from _call_BlinkXP_3261
        eil "Entonces voy a ir al jacuzzi antes de que Lisa empiece a morderse las uñas."
        eil "A ver si tengo oportunidad de hablar con ella antes de que acabe la fiesta. Si no, hablaré con ella esta noche."
    else:
        call BlinkXP ("c19s007_185b" , "d") from _call_BlinkXP_3262
        eil "Si no hay nada más, voy a ir al jacuzzi antes de que Lisa empiece a morderse las uñas."
    mc "De acuerdo, Eileen. Hablamos luego."
    scene c19s007_100b with dissolve
    "Las dos chicas se dirigen al jacuzzi, Lisa visiblemente con prisa."
    mcp "(¿Tiene la tarea un tiempo establecido para cumplirla?)"
    "Ves que Megan se acerca a ti. ¿Es un plato de galletas y un vaso de leche lo que lleva en las manos?"
    return
label c19s007_MeganJamaal:
    if _in_replay:
        $ meg._var("pregnancyDiscovered" , False)
        $ mc._var("relationships", 0, intention = "set")
        menu:
            "¿Estás en una relación con Megan?"
            "Sí":
                $ meg._var("route" , True)
                $ mc._var("relationships", 1)
                menu:
                    "¿Está embarazada?"
                    "Sí":
                        $ meg._var("pregnancyDiscovered" , True)
                    "No":
                        $ meg._var("pregnancyDiscovered" , False)
            "No":
                $ meg._var("route" , False)
        menu:
            "¿Estás en una relación con Samantha?"
            "Sí":
                $ sam._var("route" , True)
                $ mc._var("relationships", 1)
            "No":
                $ sam._var("route" , False)
        menu:
            "¿Estás en una relación con Simone?"
            "Sí":
                $ sim._var("route" , True)
                $ mc._var("relationships", 1)
            "No":
                $ sim._var("route" , False)
        if mc._var("relationships") < 2:
            menu:
                "¿En cuántas relaciones estás (sin contar a Kiara)?"
                "Más de una":
                    $ mc._var("relationships", 2, intention = "set")
                "Una":
                    $ mc._var("relationships", 1, intention = "set")
                "Ninguna" if mc._var("relationships")==0:
                    $ mc._var("relationships", 0, intention = "set")
    call BlinkXP ("c19s007_205a" , "f") from _call_BlinkXP_3263
    "Mientras tanto, al otro lado de la casa..."
    play music ("music/LifeOfAWanderingWizard.ogg")
    mc "¿Te has quedado con hambre, Megan? No podrás quejarte si no entras en el vestido esta noche."
    meg "*Risa* No es para mí, es para Jamaal. Me ha pedido que le trajera algo para merendar."
    mc "¡Maldito tragón! *Risa* ¿Dónde está? Déjame ayudarte."
    call BlinkXP ("c19s007_205b" , "d") from _call_BlinkXP_3264
    meg "Ha aparcado detrás de casa. *Risa* Toma la leche, mi pulso no es el mejor"
    meg "No sé cómo he llegado hasta aquí sin derramar nada."
    mc "Vamos."
    call BlinkXP ("c19s007_210" , "f") from _call_BlinkXP_3265
    "Por fin descubres dónde está la silla que faltaba. Jamaal es más culpable de lo que Olivia pensaba."
    mc "He oído que alguien insaciable había pedido comida por aquí. Tragón."
    jam "¡Hey! No he comido demasiado durante la comida. ¡No he repetido de ninguno de los tres pasteles!"
    mc "Creo que voy a dejar de meterme contigo por hoy. Aunque sólo sea para agradecerte lo que has intentado hacer con el mensaje."
    call BlinkXP ("c19s007_215" , "d") from _call_BlinkXP_3266
    jam "No lo he hecho por ti. *Risa* Creía que era de alguna de las chicas."
    jam "No de mi madre o de mi hermana, las dos estuvieron en casa ayer."
    call BlinkXP ("c19s007_220" , "d") from _call_BlinkXP_3267
    if sam._var("route"):
        jam "Aunque sospechara que tenías algo con mi madre, ha sido una grata sorpresa confirmarlo, padrastro."
    else:
        jam "Además nunca sospeché que estuvieras con mi madre."
    call BlinkXP ("c19s007_225" , "d") from _call_BlinkXP_3268
    if sim._var("route"):
        jam "Y lo de Simone no ha llegado ni a sorpresa. Desde aquel día en el café me olía algo."
    else:
        jam "Y Simone me ha dado un poquito de pena. Siempre le has gustado..."
    call BlinkXP ("c19s007_230" , "d") from _call_BlinkXP_3269
    jam "Y si estabas con alguna de las otras chicas, había que protegerlas, ¿no?"
    call BlinkXP ("c19s007_235" , "d") from _call_BlinkXP_3270
    if meg._var("route"):
        meg "Yo te lo agradezco. Si el mensaje lo hubiera enviado yo, me hubiera muerto de vergüenza mientras lo leía Samantha."
        meg "Aunque nunca hubiera mandado un mensaje como ese. Has actuado como un buen amigo."
    else:
        meg "Dudo que ninguna de las chicas de la familia enviara un mensaje como ese, pero has actuado como un buen amigo."
    call BlinkXP ("c19s007_240" , "d") from _call_BlinkXP_3271
    meg "Hubieras quedado mejor si Tía Betty no hubiera intentado lo mismo que tú, claro. *Risa*"
    mc "Lo de Betty ha sido alucinante. Si no hubieran hablado a la vez, todo hubiera sido distinto."
    call BlinkXP ("c19s007_245" , "d") from _call_BlinkXP_3272
    jam "Especialmente creo que Olivia no hubiera confesado sin lo de Tía Betty."
    if mc._var("relationships")>1:
        mc "Ni el resto de las chicas, obviamente. Yo hacía tiempo que quería hacer algo así, aunque no de esta forma."
        call BlinkXP ("c19s007_250" , "d") from _call_BlinkXP_3273
        if meg._var("route"):
            meg "Yo, desde luego, no lo habría hecho sin una razón así. Y menos aún hoy."
        else:
            meg "Yo también dudo que ninguna de ellas lo hubiera hecho sin la intervención de Betty."
        meg "Y Olivia tampoco lo hubiera hecho. Me alegro de que haya confesado. Es una mujer adorable."
    elif meg._var("route"):
        mc "No creo que Megan lo hubiera hecho sin el intento de Betty por cubrirnos."
        call BlinkXP ("c19s007_250" , "d") from _call_BlinkXP_3274
        mc "¿Verdad, cielo?"
        meg "Por supuesto que no. Tenía la intención de hacerlo más adelante, pero no hoy."
        meg "Y Olivia tampoco lo hubiera hecho. Me alegro de que haya confesado. Es una mujer adorable."
    elif mc._var("relationships")==1:
        mc "No creo que hubiera habido ninguna confesión sin el intento de Betty por cubrirme."
        call BlinkXP ("c19s007_250" , "d") from _call_BlinkXP_3275
        meg "Antes he estado hablando con ella, y no, no lo hubiera hecho. Y sin su revelación, Olivia tampoco hubiera confesado."
    else:
        mc "Creo que Meemaw ha visto la valentía de Betty y se ha sentido mal por ocultar su enfermedad a la familia."
        call BlinkXP ("c19s007_250" , "d") from _call_BlinkXP_3276
        meg "Ha sido emocionante. Solo la conozco desde hace un par de días, pero es una mujer adorable."
    call BlinkXP ("c19s007_255" , "d") from _call_BlinkXP_3277
    jam "Olivia antes era adorable. *Risa* Como un sargento de instrucción."
    jam "¿Pero ahora? Ahora se está volviendo tan mala como su nieto."
    jam "Fíjate lo que ha dicho de la leche y el estante de arriba. *Risa* Esta leche podía ser de abuela."
    mc "Si no puedes cogerla, podemos usarla para hacer helado. *Risa*"
    call BlinkXP ("c19s007_260" , "d") from _call_BlinkXP_3278
    meg "¿En serio beberíais leche humana? ¿O haríais helado?"
    if persistent.lactation:
        mc "Por supuesto. Es un fetiche muy común. Y dicen que es muy nutritiva."
    else:
        mc "Dicen que es muy nutritiva. Es un fetiche muy común, pero no es uno de los míos."
    call BlinkXP ("c19s007_265" , "d") from _call_BlinkXP_3279
    jam "Yo soy un tipo abierto a nuevas experiencias. Y no recuerdo el sabor de la leche materna."
    jam "Aunque el envase no me ponga, estaría dispuesto a probarla si fuera embotellada."
    jam "O en forma de helado, o de queso. No sé si se puede hacer queso con leche materna. Tengo que investigar."
    mc "Sí, se puede. Lo leí hace unos años. Aunque no sé si probaría el queso hecho con la leche de una desconocida."
    call BlinkXP ("c19s007_270" , "d") from _call_BlinkXP_3280
    mc "¿Tú no tendrías curiosidad por probar tu propia leche, Meg?"
    meg "La mía sí. La de otra mujer... nunca lo he pensado. Supongo que me daría reparo."
    meg "Y no, no probaría helado o queso hecho con la leche de Olivia."
    if meg._var("route"):
        if meg._var("pregnancyDiscovered"):
            mc "Habrá que esperar unas 22 semanas para que puedas probar la tuya, entonces. *Risa*"
        else:
            mc "Habrá que hacer algo para que empieces a producir leche, entonces. *Risa*"
    else:
        mc "Algún día encontrarás a alguien con quien tener críos y podrás probar la tuya."
    call BlinkXP ("c19s007_275" , "d") from _call_BlinkXP_3281
    jam "Y cuando eso pase, quiero ser el sumiller de la leche. *Risa*"
    jam "Eso sí, no quiero probarla del envase original. *Risa* Eso se lo dejo al padre de la criatura."
    if meg._var("route"):
        mc "No creo que la quiera compartir contigo. *Risa*"
        call BlinkXP ("c19s007_280" , "d") from _call_BlinkXP_3282
        jam "¡Mal amigo! *Risa*"
    else:
        mc "No sé si el padre estará muy contento de compartir la leche de la criatura contigo."
        call BlinkXP ("c19s007_280" , "d") from _call_BlinkXP_3283
    jam "Tendré que investigar con qué hay que alimentar a Megan para que produzca mucha leche y haya para todos."
    call BlinkXP ("c19s007_285" , "d") from _call_BlinkXP_3284
    meg "Chicos, estáis hablando de mí como si fuera una vaca. *Risa* Estoy de acuerdo que no estoy tan delgada como Scarlett, pero eso es pasarse, ¿no?"
    mc "No era a lo que nos referíamos, Meg."
    call BlinkXP ("c19s007_290" , "d") from _call_BlinkXP_3285
    meg "Lo sé, [mc]. No te preocupes. *Risa* Pero ver tu cara preocupándote por si me habías ofendido ha valido la pena."
    mc "*Risa* Creo que pasas demasiado tiempo con Jamaal."
    call BlinkXP ("c19s007_295" , "d") from _call_BlinkXP_3286
    jam "¡Hey! Mi alianza con Kate y con Tía Betty ha sido un fracaso. Tengo que buscar nuevos socios. *Risa*"
    mc "¿Desde cuándo necesitas aliados contra mí? ¿Ya no eres capaz de defenderte por ti mismo?"
    call BlinkXP ("c19s007_300" , "d") from _call_BlinkXP_3287
    jam "Tú has conseguido que Olivia se meta conmigo, yo tengo que conseguir que el resto de las chicas se metan contigo."
    mc "No, Jam. *Risa* Que Meemaw se meta contigo ha sido totalmente obra tuya."
    call BlinkXP ("c19s007_305" , "d") from _call_BlinkXP_3288
    meg "Habláis de vosotros como si fuera una guerra. *Risa* Lo siento, Jamaal, pero los objetivos con poca movilidad suelen ser los primeros en caer."
    mc "*Risa* Esa ha sido muy ingeniosa, Meg."
    call BlinkXP ("c19s007_310" , "d") from _call_BlinkXP_3289
    jam "¿Ves? Incluso la adorable Megan se mete conmigo ya. Y yo creía que era una buena chica."
    call BlinkXP ("c19s007_315" , "d") from _call_BlinkXP_3290
    meg "Si no hubieras hablado de alimentarme para que produjera leche, quizás podría haber habido una alianza. *Risa* Tratarme como a una vaca no es una buena opción diplomática, Jam."
    mc "No digas palabras complicadas como diplomacia. Jam no las va a entender."
    call BlinkXP ("c19s007_320" , "d") from _call_BlinkXP_3291
    jam "¡Hey! Tengo las piernas inútiles, no el cerebro."
    mc "¿Estás seguro de eso? *Risa*"
    scene c19s007_325a with dissolve
    "Pasáis un rato riéndoos los unos de los otros. Megan uniéndose a vuestro deporte favorito es una grata sorpresa."
    "Después de, como dice ella, tratarla como una vaca, está más o menos a salvo de vuestras pullas. Al menos por hoy. Ha sido una buena estrategia por su parte."
    scene c19s007_325b with fade
    mc "Os voy a abandonar un rato. Voy a comprobar si alguien necesita algo por ahí."
    meg "Pásalo bien, y acuérdate de guardar un poco de tiempo para ti."
    jam "Si pasas por la cocina de [nor], tráeme un trozo de pastel. Del de [eri]."
    mc "¡Tragón!"
    stop music fadeout (1.5)
    return
label c19s006_Alexia:
    if _in_replay:
        $ oma._var("pregnancyDiscovered" , False)
        $ oma._var("pregnant" , False)
        $ mc._var("relationships", 0, intention = "set")
        menu:
            "¿Estás en una relación con Alexia?"
            "Sí":
                $ oma._var("route" , True)
                $ mc._var("relationships", 1)
                menu:
                    "¿Está embarazada?"
                    "Sí":
                        $ oma._var("pregnancyDiscovered" , True)
                        $ oma._var("pregnant" , True)
                    "No":
                        $ oma._var("pregnancyDiscovered" , False)
                        $ oma._var("pregnant" , False)
                menu:
                    "¿Estás en una relación con Eileen?"
                    "Sí":
                        $ eil._var("route" , True)
                        $ mc._var("relationships", 1)
                    "No":
                        $ eil._var("route" , False)
                menu:
                    "¿Estás en una relación con Debbie?"
                    "Sí":
                        $ deb._var("route" , True)
                        $ mc._var("relationships", 1)
                    "No":
                        $ deb._var("route" , False)
                        menu:
                            "¿Estás en una relación con Maddie?"
                            "Sí":
                                $ mad._var("route" , True)
                                $ mc._var("relationships", 1)
                            "No":
                                $ mad._var("route" , False)
            "No":
                $ oma._var("route" , False)
                $ oma._var("pregnancyDiscovered" , False)
        if mc._var("relationships") < 2:
            menu:
                "¿En cuántas relaciones estás (sin contar a Kiara)?"
                "Más de una":
                    $ mc._var("relationships", 2, intention = "set")
                "Una":
                    $ mc._var("relationships", 1, intention = "set")
                "Ninguna" if mc._var("relationships")==0:
                    $ mc._var("relationships", 0, intention = "set")
    scene black with dissolve
    "Casi todo el mundo ha desaparecido de la piscina. Supones que deben estar en el jacuzzi de [nor]. Te diriges a la cocina a por el pastel de Jamaal."
    "A medio camino te encuentras con una visión sorprendente."
    play music ("music/Inspire.ogg")
    scene c19s006_005a with dissolve #bet no bra, kim no bra, mar no bra - al fondo kia no bra, Sim no bra, eil
    if not _in_replay:
        $ bet.profileImages.pop (13) # first remove
        $ bet.profileImages.insert (13, ("betty_13", None)) # then add new
        $ renpy.notify ("Profile Image unlocked for Betty: 14 - Topless party")
    mc "¿Ya os habéis cansado del juego?"
    bet "Ha sido muy divertido e instructivo. *Risa* Pero con Alexia, Amanda, y Eva ganando casi cada ronda, se estaba volviendo peligroso."
    if not _in_replay:
        $ kim.profileImages.pop (13) # first remove
        $ kim.profileImages.insert (13, ("kim_13", None)) # then add new
        $ renpy.notify ("Profile Image unlocked for Kim: 14 - Topless party")
    kim "Van a poder hacer una colección de tops de bikinis. *Risa* Pero ha estado bien."
    mom "Pero cuando casi no quedaban tops, hemos considerado que era mejor dejarlo."
    mc "Entonces, ¿ya puedo visitar el jacuzzi?"
    call BlinkXP("c19s006_010" , "d") from _call_BlinkXP_3292
    kim "Yo no te lo recomendaría. Han decidido que sea zona exclusivamente nudista por el resto de la fiesta. *Risa*"
    mc "¿Quienes? ¿Lo ha aprobado [nor]?"
    call BlinkXP("c19s006_015" , "d") from _call_BlinkXP_3293
    mom "Amanda, Alexia, y Eva. Era eso o que Betty perdiera sus braguitas. Todas lo hemos aceptado, con lo que [nor] estará de acuerdo."
    mc "*Risa* Veo que el juego se ha puesto serio."
    call BlinkXP("c19s006_020" , "d") from _call_BlinkXP_3294
    bet "Y además yo voy sin recortar. *Risa* Demasiado pelo para los filtros del jacuzzi."
    mc "¿Tú también vas en modo Yeti?"
    call BlinkXP("c19s006_025" , "d") from _call_BlinkXP_3295
    bet "*Risa* No creo que lo vayas a saber nunca."
    bet "Hemos decidido volver a la piscina para tomar el sol un rato. ¿Te apuntas?"
    mc "Iba a llevarle un trozo de pastel a Jamaal."
    call BlinkXP("c19s006_030" , "d") from _call_BlinkXP_3296
    mom "No te preocupes, ya se lo llevo yo. ¿Dónde está?"
    mc "Con Megan, detrás de casa. Quiere un trozo del pastel de [eri]."
    mom "Ok. Te vemos luego en la piscina."
    mc "Primero voy a hablar un momento con esas chicas y a pasar por el jacuzzi."
    mom "Por cierto, los pasteles están en nuestra cocina. En la nevera de [nor] no cabía nada más."
    scene c19s006_005b with fade
    mc "Hola, chicas. ¿Vosotras tampoco teníais secretos jugosos que contar?"
    if not _in_replay:
        $ kia.profileImages.pop (13) # first remove
        $ kia.profileImages.insert (13, ("kiara_13", None)) # then add new
        $ renpy.notify ("Profile Image unlocked for Kiara: 14 - Topless party")
    eil "Yo no he perdido ninguna ronda. *Risa* Si lo hubiera hecho estaría arriba con las nudistas."
    kia "Estas chicas tienen cosas muy interesantes que contar. Yo he perdido una. Y no quería perderme nada, con lo que he rechazado la tarea."
    kia "No pasaba nada por liberar a las gemelas. Éramos solo chicas. Lo que no sabía es que la ropa se la quedaban las vencedoras."
    if not _in_replay:
        $ sim.profileImages.pop (13) # first remove
        $ sim.profileImages.insert (13, ("simone_13", None)) # then add new
        $ renpy.notify ("Profile Image unlocked for Simone: 14 - Topless party")
    sim "Yo he perdido dos, pero he ganado una y he recuperado una pieza."
    call BlinkXP("c19s006_035" , "d") from _call_BlinkXP_3297
    sim "¿Vas a venir a la piscina?"
    mc "Dentro de un rato. Ahora que habéis dejado de tener el jacuzzi solo para chicas, voy a relajarme un rato allí."
    call BlinkXP("c19s006_040" , "d") from _call_BlinkXP_3298
    kia "No sé si te lo han dicho, pero ahora es zona nudista."
    mc "Supongo que eso sólo se aplica a las que jugabais, ¿no?"
    call BlinkXP("c19s006_045" , "d") from _call_BlinkXP_3299
    kia "Pues la verdad es que no lo sé... han dicho lo de la zona nudista y todas hemos estado de acuerdo para evitarle a Betty el tener que desnudarse."
    kia "Conociendo a esas chicas, es posible que lo quieran aplicar a todo el mundo, pero no tendría mucha lógica que el resto os vierais obligados si no jugabais."
    mc "Iré a preguntar y a aclararlo."
    call BlinkXP("c19s006_050" , "d") from _call_BlinkXP_3300
    eil "Mientras tú vas, {b}mi madre y yo vamos a tener una conversación que tenemos pendiente{/b}. Y no es una propuesta, Mamá."
    call BlinkXP("c19s006_055" , "d") from _call_BlinkXP_3301
    kia "Pero... la piscina..."
    call BlinkXP("c19s006_060" , "d") from _call_BlinkXP_3302
    eil "Va a seguir ahí cuando acabemos de hablar. Tengo sed, con lo que puedes... {b}vas a{/b} acompañarme a la cocina de [nor] a beber un poco de agua."
    call BlinkXP("c19s006_065" , "d") from _call_BlinkXP_3303
    kia "Vaaale..."
    call BlinkXP("c19s006_070" , "d") from _call_BlinkXP_3304
    sim "Yo os espero a todos en la piscina. Tengo ganas de tomar el sol con las chicas libres."
    mc "Os veo luego allí."
    scene c19s006_115d with dissolve
    mcp "(No quisiera estar en la piel de Kiara. Eileen puede ser muy asertiva cuando quiere.)"
    scene c19s006_115a with dissolve
    mc "Hola, chicas. Veo que os habéis quedado el jacuzzi para vosotras solas."
    oma "No para nosotras solas, sino para cualquiera que quiera estar en la nueva zona nudista."
    mc "No sé si eso le va a gustar mucho a [nor]."
    ama "No creo que le importe mucho. Solo va a ser por un rato."
    eva "Esperábamos que se uniera, pero Betty ha perdido demasiado rápido como para a mandar a alguien a buscarla."
    mc "¿Todos esos viajes de Lisa y Maddie eran porque habían perdido una de las rondas?"
    call BlinkXP("c19s006_075" , "d") from _call_BlinkXP_3305
    ama "Sí, algunas chicas han sido poco imaginativas con las tareas cuando alguien perdía. Querían que se uniera todo el mundo."
    mc "Posiblemente no querían avergonzarlas, obligándolas a quitarse ropa."
    call BlinkXP("c19s006_080" , "d") from _call_BlinkXP_3306
    eva "No lo entiendes... ¿Has visto a Kiara, Simone, Betty, o Kim avergonzadas?"
    mc "No..."
    eva "Sólo necesitaban un empujón para unirse al topless. Simone incluso ha llegado a estar totalmente desnuda un rato, hasta que ha ganado una ronda."
    mc "Pero..."
    call BlinkXP("c19s006_085" , "d") from _call_BlinkXP_3307
    oma "Por eso hemos empezado el juego. Ninguna de ellas ha reclamado sus tops cuando ha acabado. Tampoco se los hubiéramos dado. Son nuestro botín. *Risa*"
    oma "Hemos conseguido que se sientan a gusto aquí, entre chicas. Ahora también lo estarán cuando tú estés alrededor."
    mc "Pero podría haberos explotado en la cara..."
    call BlinkXP("c19s006_090" , "d") from _call_BlinkXP_3308
    ama "Podría, pero yo he perdido una de las primeras rondas... casi a propósito. Cuando he ganado varias rondas después no he reclamado mis braguitas."
    ama "Eso, y que Alexia estuviera desnuda desde el principio, les ha demostrado que no pasaba nada. Que todo era muy natural."
    mc "¿Me estás diciendo que teníais una estrategia antes de empezar?"
    call BlinkXP("c19s006_095" , "d") from _call_BlinkXP_3309
    eva "*Risa* Casi. La única que ha pedido una prenda cuando hemos terminado de jugar ha sido Kim. Y solo ha pedido las braguitas para no pasearse desnuda por la piscina."
    eva "Podía haber pedido también el top, pero no lo ha hecho. Quizás, junto con Betty, era quien más necesitaba un juego así."
    mc "Sois unos genios. Habéis conseguido que todas las chicas se sientan a gusto, incluso las que no han querido hacer topless al principio."
    call BlinkXP("c19s006_100" , "d") from _call_BlinkXP_3310
    ama "No todas. Debbie no ha perdido ni una ronda, y Lisa tenía suerte. Cuando ha perdido y no ha aceptado la tarea, ha ganado en seguida para recuperar el top."
    ama "Pero creo que para la siguiente fiesta topless se unirán. Han visto que no pasa nada, que todo el mundo está cómodo y que nadie juzga a nadie."
    call BlinkXP("c19s006_105" , "d") from _call_BlinkXP_3311
    oma "Y algunas no han venido. Habrá que trabajar con Kate, Megan, y Olivia."
    mc "De Meemaw no os tenéis que preocupar. Si vais a la piscina, veréis que se ha unido. Ha tenido... un pequeño accidente con su leche."
    call BlinkXP("c19s006_110" , "d") from _call_BlinkXP_3312
    eva "¡Oh! ¡Eso es genial! Bueno... no lo del accidente, sino que haya decidido unirse a la fiesta topless."
    eva "¿Y tú? ¿Vas a entrar en el jacuzzi nudista?"
    mc "¿Para mí también es nudista?"
    scene c19s006_115b with dissolve
    todas "¡Por supuesto! *Risa*"
    if oma._var("route"):
        eva "Todas te hemos visto desnudo, con lo que no deberías avergonzarte de nada."
    else:
        eva "Amada y yo te hemos visto desnudo. Alexia está en desventaja."
    ama "Y recuerda, nadie juzga."
    oma "Si quieres mojarte y mantener el bañador, te toca ir a la piscina. *Risa*"
    mc "Entonces no me va a quedar otra opción."
    scene c19s006_115c with fade
    "Tras desnudarte, te sientas al lado de Alexia. Si lo hiciste por Meemaw no pasa nada por hacerlo ahora."
    mc "Me parece que habéis hecho un buen trabajo con este juego. Si hace que todo el mundo cree vínculos y se sienta más a gusto, no creo que nadie ponga pegas."
    ama "Es lo que llevas haciendo tú desde que llegaste de la universidad. Era el momento de que alguien más cogiera el testigo. ¿no?"
    eva "Esto era algo que tú no podías hacer, con lo que nos ha tocado hacerlo a nosotras. Y estamos orgullosas de haberlo podido hacer."
    oma "Lo siguiente que tenemos que hacer es convencer a [mar] para que la piscina también sea nudista opcionalmente. *Risa*"
    mc "Eso lo veo más difícil. Un camionero pasando por la carretera podría veros en la piscina."
    call BlinkXP("c19s006_120" , "d") from _call_BlinkXP_3313
    ama "Por eso debería ser opcional. No es que pasen muchos camiones por aquí, de todas formas."
    mc "Quizás uno cada dos o tres días..."
    call BlinkXP("c19s006_125" , "d") from _call_BlinkXP_3314
    oma "A [mar] se la ha visto muy cómoda aquí, incluso cuando hemos llegado a estar desnudas Amanda, Eva, Kim, Simone, y yo a la vez."
    oma "Sólo se ha puesto un poco nerviosa cuando Betty estaba a punto de perder sus braguitas, y creo que es porque todas sabemos que no está preparada."
    mc "Es una monja, al fin y al cabo."
    call BlinkXP("c19s006_130" , "d") from _call_BlinkXP_3315
    eva "Creo que si se lo proponemos hoy, [mar] no aceptaría, pero quizás un poco más adelante... posiblemente como un hecho consumado..."
    mc "No creo que eso funcione con ella. Pero podéis probarlo. Especialmente si sois más de tres."
    call BlinkXP("c19s006_135" , "d") from _call_BlinkXP_3316
    ama "¿Con quién crees que podríamos contar?"
    mc "No tengo ni idea. Si me hubieran preguntado quién iba a hacer topless hoy, hubiera fallado en más de la mitad de vosotras."
    mc "Supongo que las que os habéis quedado desnudas en el jacuzzi. [eri] y [dap] quizás se apuntarían si lo hace [nor]. [emm] también podría hacerlo, para no ser menos."
    mc "Lisa, Debbie, Megan, y Maddie lo dudo. [mar], Tía Betty y Meemaw descartadas. Kim y Kate es posible, si no estoy yo. Sam no tengo ni idea."
    call BlinkXP("c19s006_140" , "d") from _call_BlinkXP_3317
    eva "¡Vale! Es una buena cifra con la que empezar. Tenemos que hablar con las mejores candidatas y montar una fiesta sin [mc] en la piscina. ¿Vamos?"
    mc "Yo me voy a quedar un rato más en el jacuzzi. No quiero estar implicado en esto para no asustar o cohibir a nadie."
    call BlinkXP("c19s006_145" , "d") from _call_BlinkXP_3318
    oma "Yo también me voy a quedar un rato aquí contigo. La idea del Strip Secret ha sido mía, aunque el juego lo haya propuesto Simone, y no quiero que parezca que tengo ningún interés en esto."
    scene c19s006_145d with dissolve
    "Amanda y Eva se ponen sus bikinis dentro del agua."
    mcp "(Para querer avanzar hacia una piscina nudista, se han comportado más tímidamente de lo que habría esperado.)"
    scene c19s006_145e with dissolve
    eva "Bueno, vamos a ver si encontramos aliadas para la piscina nudista. *Risita*"
    ama "Os vemos luego. No te dejes a Fee, Eva."
    call BlinkXP("c19s006_150" , "d") from _call_BlinkXP_3319
    eva "Me la voy a tener que atar con una cadena a la muñeca. *Risita* Va a ser la única forma de no perderla."
    eva "Alexia, ¿tienes unas esposas de sobras? *Risa*"
    call BlinkXP("c19s006_155" , "d") from _call_BlinkXP_3320
    oma "Sí, pero no tamaño muñeca. *Risa*"
    stop music fadeout (1.5)
    call BlinkXP("c19s006_160" , "f") from _call_BlinkXP_3321
    "Una vez Amanda y Eva se han ido..."
    play music ("music/ForWhenItRains.ogg")
    oma "Lo que has hecho por esas chicas regalándoles las muñecas ha sido increíble."
    oma "Eva no se separa de ella. Aunque se ve rara una chica de su edad paseando una muñeca."
    mc "Ha sido muy emotivo. Nunca han tenido ningún juguete. Ninguna muñeca."
    call BlinkXP("c19s006_165" , "d") from _call_BlinkXP_3322
    oma "Eso lo explica. Sigue siendo raro, pero es más comprensible."
    mc "Yo no lo considero raro. Es su primera muñeca. Y la diseñé para que se pareciera a ella lo máximo posible."
    if persistent.family:
        mc "Con lo que no conté es que también se parecería a Fiona y a Diana."
    else:
        mc "No sé qué aspecto tenían las hermanas que perdieron por el camino, pero creo que..."
    call BlinkXP("c19s006_170" , "d") from _call_BlinkXP_3323
    oma "¡Oh! No lo había pensado... La muñeca se llama Fee. De Fiona."
    mc "Exacto. Creo que por eso le ha afectado más todavía. Le ha puesto el nombre dos minutos después de recibirla."
    call BlinkXP("c19s006_175" , "d") from _call_BlinkXP_3324
    oma "No me imagino por lo que han tenido que pasar esas chicas."
    oma "Aún se me hace raro que estés hablando con ellas y parezcan super adultas y un minuto después se rían como niñas por una broma que lleva rondando diez años."
    mc "Esa broma seguramente sea nueva para ellas. Creo que en su vida han faltado muchas risas."
    mc "Pero están cambiando muy rápido. Creo que las hemos pillado justo a tiempo para... ¿salvarlas? No se me ocurre ninguna palabra mejor."
    oma "Creo que es la palabra adecuada. Esta familia les puede hacer mucho bien, pero si las hubiéramos conocido dentro de unos años quizás hubiera sido tarde para ellas."
    if not oma._var("route"):
        call BlinkXP("c19s006_335" , "d") from _call_BlinkXP_3325
        stop music fadeout (1.5)
        "Pasáis un rato charlando de Amanda y Eva, de la fiesta, de las revelaciones."
        return
    call BlinkXP("c19s006_180" , "d") from _call_BlinkXP_3326
    stop music fadeout (1.5)
    oma "Nuestros hijos no tendrán que pasar por eso, espero. Van a tener una familia enorme."
    play music ("music/Embrace.ogg")
    if not oma._var("pregnancyDiscovered"):
        oma "Si alguna vez los tenemos claro..."
    mc "Creo que van a tener tías y abuelas suficientes como para que nunca les falte cariño, cielo."
    mc "También creo que vamos a tener que batallar para poder darles cariño nosotros. *Risa* Todo el mundo va a querer achucharlos."
    if mc._var("relationships")>1:
        call BlinkXP("c19s006_185" , "d") from _call_BlinkXP_3327
        oma "Eso dependerá de cuántas chicas más añadas al harén, y de cuántos hijos tengas con ellas."
        mc "Siempre se los tendremos que quitar a Meemaw. *Risa* No creo que suelte a sus bisnietos fácilmente."
    call BlinkXP("c19s006_190" , "d") from _call_BlinkXP_3328
    oma "Hablando de niños... y de cómo se hacen..."
    oma "Después de las revelaciones, he hablado con [nor] y [mar]..."
    stop music fadeout (1.5)
    mc "Me dais miedo. *Risa*"
    scene c19s006_190d with dissolve
    play music ("music/CCFunk.ogg")
    oma "Ahora que todo el mundo sabe que estamos juntos... ya no hace falta que nos escondamos para tener sexo."
    mc "¡Alexia! ¿Aquí? ¿Ahora?"
    call BlinkXP("c19s006_195" , "d") from _call_BlinkXP_3329
    oma "Uno de los secretos con los que he ganado una ronda, creo que he ganado el top de Kiara, ha sido cuando he dicho que me muero por hacer el amor contigo en el jacuzzi."
    mc "Me hubiera gustado ver sus caras. *Risa* ¿Cómo se lo han tomado?"
    call BlinkXP("c19s006_200" , "d") from _call_BlinkXP_3330
    oma "Estamos solos, ¿no?"
    oma "¿Crees que Amanda y Eva tenían prisa por montar una fiesta nudista en la piscina para convencer a [mar]?"
    mc "Es decir, nos han dejado solos a propósito."
    call BlinkXP("c19s006_205" , "d") from _call_BlinkXP_3331
    oma "Igual que Maddie, Debbie, y Lisa. Se han ido cuando te han visto dirigirte aquí, mientras hablabas con Betty, Kim, y [mar]."
    if mc._var("relationships")>1:
        oma "Hemos decidido, sin tener que hablarlo, darnos privacidad las unas a las otras, ahora que todo el mundo sabe con quién sales."
        if deb._var("route") or mad._var("route"):
            oma "Como puedes ver, incluso entre las chicas de tu harén."
    else:
        oma "Ahora que todo el mundo sabe que estamos juntos, nos van a dar privacidad. No ha hecho falta ni siquiera hablarlo."
    mc "¿Me estás diciendo que nadie se va a asomar desde una ventana de mi casa? Antes Debbie te ha visto desnuda aquí desde su habitación."
    call BlinkXP ("c19s006_210" , "d") from _call_BlinkXP_3332
    oma "Sí, lo del gato negro. *Risa* Me lo ha contado. Estaba sentada ahí arriba."
    call BlinkXP ("c19s006_215" , "d") from _call_BlinkXP_3333
    oma "Y no, nadie lo va a hacer, a menos que tengan un fetiche voyeur. Y la primera vez que tuvimos sexo fue en el prado, donde nos podía ver cualquiera."
    oma "No me importa si alguien quiere mirarnos, si a ti no te importa. Incluso la posibilidad de que Yaya Olivia nos vea desde la escalera me está poniendo más cachonda aún."
    mc "*Risa* La pobre mujer se ha librado del cáncer y quieres matarla de un infarto..."
    call BlinkXP ("c19s006_220" , "d") from _call_BlinkXP_3334
    oma "*Risa* No, pero no me importaría que se le alegrara la vista."
    scene c19s006_225pv with dissolve
    oma "Y a ti también te está poniendo cachondo que nos vea Olivia por lo que veo. Mjolnir acaba de saltar en mi mano."
    mc "No, no es por Meemaw. Es que llevas un par de minutos con Mjolnir en la mano. Creo que está pidiendo que la muevas."
    show c19s006_225v
    oma "Eso tiene fácil solución. Tengo muchas ganas de hacer esto."
    "Alexia empieza a subir y bajar su mano a lo largo de tu astil, ya duro del todo."
    oma "Desde que has llegado no podía esperar a que las chicas se marcharan para quedarnos solos."
    mc "Si lo hubieras dicho, hubiéramos podido subir a mi habitación."
    "Su mano aprieta más por un segundo, casi un gesto involuntario de rechazo."
    oma "Hoy quería que fuera aquí."
    if eil._var("route"):
        oma "Nuestras dos veces juntos han sido al aire libre, en el prado y en el lago."
    else:
        oma "Nuestra primera vez fue al aire libre, en el prado."
    call BlinkXP ("c19s006_275" , "d") from _call_BlinkXP_3335
    hide c19s006_225v
    oma "Hoy, el día de la revelación secretos, tenía que ser también en un sitio al aire libre. Y siempre he querido hacer el amor en un jacuzzi."
    oma "Lo que no me esperaba es tener que hacer todo el trabajo yo. *Risa*"
    mc "Eso es fácil de arreglar..."
    scene c19s006_230pv with dissolve
    show c19s006_230v
    "Introduces una mano entre las piernas de Alexia. El tacto del Yeti, empapado, es muy diferente de cómo lo recordabas."
    oma "*Gemido* ¡Eso es!"
    "Ella se estremece con tu primer contacto. Hace mucho de la última vez que estuvisteis a solas. La has echado de menos."
    oma "*Jadeo* Te he echado de menos. Mucho. Y no solo por el sexo."
    "Parece que vuestras mentes entran en la misma comunión que lo están haciendo vuestros cuerpos, comunicándose sin necesidad de palabras."
    scene c19s006_270b with fade
    hide c19s006_230v
    mc "Yo a ti también, mi amor."
    oma "*Gemido* Me está poniendo muy cachonda que nos puedan ver. ¿A ti no?"
    call BlinkXP ("c19s006_280" , "f") from _call_BlinkXP_3336
    mc "*Risa* No sabía que tenías una vena exhibicionista..."
    oma "*Jadeo* He sido la primera en desnudarse en el jacuzzi... *Gemido* Antes de conocerte no lo hubiera hecho... *Jadeo* Me hubiera avergonzado de que vieran al Yeti..."
    mc "El Yeti es maravilloso. Nunca deberías avergonzarte de él."
    call BlinkXP ("c19s006_285" , "d") from _call_BlinkXP_3337
    oma "Pues ahora el Yeti tiene hambre. *Gemido* Va a devorarte por completo."
    mc "*Risa* Estoy dispuesto a ser su víctima."
    scene c19s006_270a with fade
    oma "Déjame que me siente encima tuyo..."
    mc "Como quieras, no me atrevería a llevare la contraria ahora mismo."
    oma "Así..."
    oma "¡Oof! ¡Por Dios! *Gemido* Creía que, en mi imaginación, te recordaba más grande de lo que eras... era al revés."
    scene c19s006_240pv with fade
    show c19s006_240v
    "Alexia empieza a cabalgarte ayudada por tus manos en su cintura. El agua hace que sea mucho más liviana."
    oma "*Gemido* ¡Así! *Jadeo* ¡Justo ahí!"
    "Hacer el amor dentro del agua es increíble. las sensaciones, los pesos, son totalmente diferentes. Es tu primera vez. No será la última."
    oma "*Jadeo* ¡Me encanta! *Gemido* ¡Más rápido!"
    "Más rápido. Mas profundo. Mas placer para ambos."
    scene c19s006_235pv with dissolve
    hide c19s006_240v
    show c19s006_235v
    "El coño de Alexia abraza a tu polla en cada recorrido, sumando su propia humedad a la del agua."
    oma "*Gemido* Sigue así y me correré muy pronto..."
    "Quieres que dure. A ti te queda mucho aún. No te importa que se corra antes que tú. Es lo que deseas."
    oma "*Jadeo* ¿A ti te queda mucho?"
    mc "Mucho, mi amor, pero no te preocupes por mí."
    "Alexia adora que lleguéis juntos al orgasmo, pero puedes intentar lograrlo durante su segundo, tercer, o cuarto orgasmo."
    scene c19s006_250pv with fade
    hide c19s006_235v
    show c19s006_250v
    "Ella ha dicho que el resto de las chicas os van a dar intimidad pero, por alguna razón, te sientes observado. Deben ser imaginaciones tuyas."
    oma "*Gemido* Casi me gustaría que Olivia nos estuviera mirando..."
    "Otra vez parece que te ha leído el pensamiento. Vas a tener que vigilar lo que piensas cerca de Alexia. Por suerte, solo puedes pensar en ella en este momento."
    oma "*Jadeo* Se sentiría orgullosa de su nieto. *Gemido* Me va a hacer correr como una perra..."
    "Puedes notar en tu polla como su vagina aprieta cada vez más en cada recorrido. Su orgasmo se está acercando."
    scene c19s006_245pv with fade
    hide c19s006_250v
    show c19s006_245v
    "Con tus manos en su cintura, corriges sus movimientos, cada vez más erráticos. Le cuesta coordinarlos cuando se está acercando su orgasmo."
    oma "*Jadeo* Estoy a punto de llegar..."
    "Lo puedes notar. Sus paredes vaginales abrazan tu polla cada vez con más fuerza, intentando llevarte a un orgasmo que todavía está lejos para ti."
    oma "*Gemido* ¡No voy a poder contenerlo!"
    mc "No lo hagas. Córrete para mí."
    call OrgasmX ("c19s006_295") from _call_OrgasmX_67
    "Dicho y hecho. El cuerpo de Alexia se tensa durante una fracción de segundo para después liberar toda esa tensión en una maravillosa explosión."
    oma "*GEMIDO* ¡SÍ!"
    oma "*JADEO* ¡NO PARES!"
    "No piensas hacerlo, pero sabes que Alexia está más desmadejada que nunca y va a necesitar un pequeño respiro."
    call OrgasmX ("c19s006_290") from _call_OrgasmX_68
    "Continúas moviendo su cuerpo arriba y abajo durante unos segundos. Ella ha dejado de colaborar y se centra en las oleadas de placer que recorren su cuerpo."
    oma "*Gemido* Cambiemos de posición. *Jadeo* No voy a poder continuar así."
    "Cambiáis a una posición donde Alexia tenga que hacer menos movimientos coordinados."
    scene c19s006_300pv with fade
    hide c19s006_245v
    show c19s006_300v
    "Apoya sus manos en la pared del jacuzzi mientras penetras su coño desde atrás. Mucho más fácil para ella. Inmejorables vistas para ti."
    oma "*Gemido* ¡Oh, sí!"
    "El impacto de tus caderas en su hermoso culo cada vez que tu polla penetra en su coño produce un sonido húmedo."
    oma "*Jadeo* ¡No pares!"
    "No piensas hacerlo. Acabas de empezar tus embestidas en el caliente agujero."
    scene c19s006_255pv with fade
    hide c19s006_300v
    show c19s006_255v
    "Te das cuenta de que nunca has hecho el amor con Alexia mientras le mirabas a esos profundos ojos oscuros."
    oma "*JADEO* ¡Sí, sigue así!"
    "En el prado te cabalgó como acaba de hacer."
    if eil._var("route"):
        "En el trío con Eileen, en el bosque, tenías a la propia Eileen sentada en tu cara, tapándote el rostro de Alexia. No te vas a quejar de estar con ambas."
    oma "*GEMIDO* ¡Te amo!"
    "La próxima vez tienes que cambiar la posición. Quieres verle la cara mientras se corre."
    mc "Yo también, mi amor."
    scene c19s006_265pv with fade
    hide c19s006_255v
    show c19s006_265v
    oma "*JADEO* ¡Estoy a punto de correrme otra vez!"
    "Tú te estás acercando rápidamente a tu clímax, pero aún te queda un poco de gasolina en el depósito."
    oma "*GEMIDO* ¡Quiero que te corras dentro!"
    "Correrte fuera y dejar tu semen flotando en el jacuzzi no se te había pasado por la cabeza en ningún momento."
    mc "Córrete para mí, mi vida. A mí me queda un poco aún."
    call OrgasmX ("c19s006_305") from _call_OrgasmX_69
    oma "*JADEO* ¡Este es más grande!"
    "Estando ahora su coño fuera del agua, puedes notar a lo largo de tu astil sus contracciones mucho más fuertes. O es posible que el orgasmo sea más intenso."
    "Con cada contracción, su coño intenta ordeñarte, retenerte, no dejarte ir."
    scene c19s006_260pv with fade
    hide c19s006_265v
    show c19s006_260v
    oma "*GEMIDO* ¡No van a parar!"
    "Lo puedes notar. Ya no son contracciones en oleadas como antes. Ahora su coño no llega a relajarse por completo. Una oleada de contracciones se entrelaza con la siguiente."
    "Su coño es cada vez más estrecho, ya no abraza a tu polla, ahora la estruja. Con la fuerza de los músculos de alguien como Alexia, es una sensación alucinante."
    "Es tan alucinante que te lleva más allá de tu límite."
    if persistent.walkthrough:
        $ wt1 = _("Alexia embarazada.")
        $ wt2 = _("Sin consecuencias.")
    else:
        $ wt1 = ""
        $ wt2 = ""
    menu:
        "Correrte dentro." (wt = wt2):
            pass
        "Correrte dentro. Ir a por el bebé." (wt = wt1) if persistent.pregnancy and not oma._var("pregnant"):
            play sound ("music/OldMusicBox5.ogg")
            $ oma._var("pregnant", True)
    $ resetWalkthrough ()
    call OrgasmX ("c19s006_310") from _call_OrgasmX_70
    hide c19s006_260v
    mc "¡Mpfft!"
    "Explotas en el interior de Alexia. Mientras ella sigue encadenando un orgasmo tras otro. Al final os habéis corrido a la vez."
    "Entre lo excitante que ha sido hacer el amor donde alguien os pueda ver y el placer de volverla a tener entre tus brazos, descargas una enorme cantidad de semen."
    if oma._var("pregnancyDiscovered"):
        "No puedes volver a dejarla embarazada, obviamente, pero siempre es increíble descargar tu semilla dentro de ella."
    scene c19s006_270d with fade
    stop music fadeout (1.5)
    "Al cabo de unos segundos os sentáis de nuevo en el jacuzzi. Las piernas de Alexia temblando. Las tuyas a punto de pedir una tregua."
    play music ("music/Stardust.ogg")
    oma "Ha sido increíble... me encanta follar en el agua. La próxima vez en el lago."
    mc "*Risa* La próxima vez en una cama. Mirándonos a los ojos."
    call BlinkXP ("c19s006_315" , "f") from _call_BlinkXP_3338
    oma "*Risa* ¿Esposado?"
    mc "No me quejaría si lo estuviera. *Risa* Además, me lo prometiste."
    call BlinkXP ("c19s006_320" , "d") from _call_BlinkXP_3339
    oma "En tu cama no hay dónde esposarte, con lo que debería ser en mi casa."
    mc "Me parece una buena idea. Nunca he estado en tu casa."
    call BlinkXP ("c19s006_325" , "d") from _call_BlinkXP_3340
    oma "Ni hemos salido a cenar, ni al cine... No hemos empezado como empiezan las parejas normales."
    oma "Me alegra no ser una pareja normal."
    mc "A mí también, mi amor. No lo cambiaría por nada del mundo."
    call BlinkXP ("c19s006_330" , "d") from _call_BlinkXP_3341
    oma "Pero lo de salir a cenar un día, o que vengas a casa a cenar y te quedes a dormir, sí que me apetece."
    mc "Es una buena idea. Ni siquiera sé cuáles son tus platos favoritos."
    call BlinkXP ("c19s006_335" , "d") from _call_BlinkXP_3342
    oma "Yo tampoco sé los tuyos... no sabría qué cocinarte."
    mc "*Risa* Mientras no lleve brócoli, todo está bien."
    oma "Entonces no hay ningún problema. Odio el brócoli."
    mc "¿Ves como eres la mujer perfecta? *Risa*"
    "Empezáis a charlar y a planear vuestra primera cita."
    return
label c19s008_LeeroyJenkins:
    if _in_replay:
        $ mc._var("relationships", 0, intention = "set")
        menu:
            "¿Has pre-abierto la relación con Kiara?"
            "Sí":
                $ kia._var("route" , True)
                menu:
                    "¿Estás en una relación con [mar!t]?"
                    "Sí":
                        $ mar._var("route" , True)
                        $ mc._var("relationships", 1)
                    "No":
                        $ mar._var("route" , False)
                        menu:
                            "¿Estás en una relación con Saira?"
                            "Sí":
                                $ sai._var("route" , True)
                                $ mc._var("relationships", 1)
                            "No":
                                $ sai._var("route" , False)
                                menu:
                                    "¿Estás en una relación con [nor]?"
                                    "Sí":
                                        $ nor._var("route" , True)
                                        $ mc._var("relationships", 1)
                                    "No":
                                        $ nor._var("route" , False)
                                        menu:
                                            "¿Estás en una relación con [emm]?"
                                            "Sí":
                                                $ emm._var("route" , True)
                                                $ mc._var("relationships", 1)
                                            "No":
                                                $ emm._var("route" , False)
                                                menu:
                                                    "¿Estás en una relación con [eri]?"
                                                    "Sí":
                                                        $ eri._var("route" , True)
                                                        $ mc._var("relationships", 1)
                                                    "No":
                                                        $ eri._var("route" , False)
                                                        menu:
                                                            "¿Estás en una relación con [dap]?"
                                                            "Sí":
                                                                $ dap._var("route" , True)
                                                                $ mc._var("relationships", 1)
                                                            "No":
                                                                $ dap._var("route" , False)
                                                                menu:
                                                                    "¿Estás en una relación con Scarlett?"
                                                                    "Sí":
                                                                        $ sca._var("route" , True)
                                                                        $ mc._var("relationships", 1)
                                                                    "No":
                                                                        $ sca._var("route" , False)
                                                                        menu:
                                                                            "¿Estás en una relación con Samantha?"
                                                                            "Sí":
                                                                                $ sam._var("route" , True)
                                                                                $ mc._var("relationships", 1)
                                                                            "No":
                                                                                $ sam._var("route" , False)
                                                                                menu:
                                                                                    "¿Estás en una relación con Simone?"
                                                                                    "Sí":
                                                                                        $ sim._var("route" , True)
                                                                                        $ mc._var("relationships", 1)
                                                                                    "No":
                                                                                        $ sim._var("route" , False)
                                                                                        menu:
                                                                                            "¿Estás en una relación con Alexia?"
                                                                                            "Sí":
                                                                                                $ oma._var("route" , True)
                                                                                                $ mc._var("relationships", 1)
                                                                                            "No":
                                                                                                $ oma._var("route" , False)
                                                                                                menu:
                                                                                                    "¿Estás en una relación con Maddie?"
                                                                                                    "Sí":
                                                                                                        $ mad._var("route" , True)
                                                                                                        $ mc._var("relationships", 1)
                                                                                                    "No":
                                                                                                        $ mad._var("route" , False)
                                                                                                        menu:
                                                                                                            "¿Estás en una relación con Debbie?"
                                                                                                            "Sí":
                                                                                                                $ deb._var("route" , True)
                                                                                                                $ mc._var("relationships", 1)
                                                                                                            "No":
                                                                                                                $ deb._var("route" , False)
                                                                                                                menu:
                                                                                                                    "¿Estás en una relación con Megan?"
                                                                                                                    "Sí":
                                                                                                                        $ meg._var("route" , True)
                                                                                                                        $ mc._var("relationships", 1)
                                                                                                                    "No":
                                                                                                                        $ meg._var("route" , False)
            "No":
                $ kia._var("route" , False)
        if mc._var("relationships") > 0:
            menu:
                "¿En cuántas relaciones estás (sin contar a Kiara)?"
                "Más de una":
                    $ mc._var("relationships", 2, intention = "set")
                "Una":
                    $ mc._var("relationships", 1, intention = "set")
    stop music fadeout (1.5)
    "De pronto..."
    play music ("music/Epic-Adventure-Action.ogg")
    sol "¡KIARA!"
    call BlinkXP ("c19s008_005" , "d") from _call_BlinkXP_3343
    oma "¿Qué? ¿Ese es el marido de Kiara?"
    mc "Creo que sí. Voy a ver."
    scene c19s008_005d with fade #fuera de casa. Coche aparcado.
    "Ciertamente es Solomon. Esta vez no parece borracho."
    call BlinkXP ("c19s008_010" , "d") from _call_BlinkXP_3344
    mc "Voy a bajar a echarlo."
    oma "Ponte el bañador. Yo voy a ponerme algo y bajo contigo."
    mc "Mejor que no te metas, al menos de momento. Voy a intentar solucionarlo por las buenas."
    mc "Mantén a las chicas alejadas. Ese tío puede ser imprevisible."
    scene c19s008_015a with fade
    sol "¡Eres una puta zorra! Paseándote con las tetas al aire en casa de ese... perdedor."
    mcp "(El top de Kiara se ha quedado en el jacuzzi...)"
    kia "Solomon, por favor, vete a casa. Estamos celebrando un cumpleaños."
    mc "Haz caso a Kiara, Solomon. No eres bienvenido en esta casa."
    scene c19s008_015b with dissolve
    sol "¡Tú cállate! He venido a llevarme a mi mujer a casa, donde debe estar."
    kia "No me voy a ir, Solomon."
    mc "Ya la has oído. Ella no va a salir, y tú no vas a entrar en mi casa."
    mc "Kiara, no salgas de la propiedad. Ponte detrás mío."
    scene c19s008_015c with dissolve #aparecen varias chicas
    mc "Id a la piscina, por favor. Alexia, ¿puedes ocuparte?"
    oma "No te preocupes. Chicas, acompañadme, por favor."
    eil "Yo me quedo. Quiero ver qué hace la piltrafa humana."
    call BlinkXP ("c19s008_020" , "d") from _call_BlinkXP_3345
    "Alexia te mira interrogativamente."
    "Asientes."
    "Eileen tiene todo el derecho a estar aquí."
    scene c19s008_025a with dissolve
    sol "¿Llamas piltrafa a tu exnovio? *Risa* Eso no le deja en muy buen lugar."
    mc "Y esa frase no te deja a ti en muy buen lugar. Se refiere a ti, no a mí."
    scene c19s008_025b with dissolve
    sol "¡Puta zorra! ¡De tal palo tal astilla!"
    mc "No vuelvas a insultar a ninguna de las dos, Solomon. Ni a nadie que esté en esta casa."
    "La sangre empieza a calentársete."
    call BlinkXP ("c19s008_030" , "d") from _call_BlinkXP_3346
    kia "Por favor, Solomon. Vete. No voy a volver a casa contigo."
    scene c19s008_025c with dissolve
    sol "¿Por qué? ¿Te estás follando a este perdedor?"
    sol "¿No te das cuenta de lo patética que eres a tu edad persiguiendo a críos?"
    "La sangre empieza a hervir. Mantienes la calma."
    scene c19s008_025d with dissolve
    "Sales de casa."
    mc "Te he dicho que no vuelvas a insultarla."
    sol "Cuidadito con lo que haces con ese dedo, gilipollas."
    scene c19s008_035a with dissolve
    mc "Mira, capullo. Estoy usando el dedo por no usar el puño."
    scene c19s008_035b with dissolve
    mc "La última vez no lo necesité para tumbarte. No quise humillarte delante de Kiara y Eileen en frente de tu casa."
    scene c19s008_035c with dissolve
    mc "Esta vez has venido a mi casa. No voy a tener tantos miramientos. Te he dicho que no volvieras a insultar a nadie de esta casa y acabas de insultarme a mí."
    mc "No voy a permitirte que insultes a Kiara."
    scene c19s008_040a with dissolve
    eil "Vete, Solomon. No tienes nada que hacer aquí."
    mcp "(Solomon, no Papá.)"
    scene c19s008_025e with dissolve
    sol "Déjame llevarme a mi mujer y no te molestaré más."
    sol "Puedes quedarte con la zorra de mi hija."
    "Tienes la sangre a punto de explotar."
    menu:
        "Abofetearlo como a un llorón.":
            pass
        "Abofetearlo como a un mal marido.":
            pass
        "¿Qué coño? Abofetearlo.":
            pass
    scene c19s008_045An with dissolve
    pause (1.3)
    play sound ("music/Slap.ogg")
    scene c19s008_045bAn with hpunch
    "Nunca habías abofeteado a nadie. Sienta bien en este caso. Sabes que una bofetada así es humillante."
    mc "Te he dicho que no insultes a nadie."
    scene c19s008_025f with dissolve
    sol "¡Me has abofeteado!"
    mc "Los puños los guardo para los hombres de verdad."
    mc "Tú estás lejos de serlo."
    scene c19s008_025g with dissolve
    sol "¡Pelea como un hombre, capullo!"
    mc "Hoy no tienes la excusa de estar borracho, gilipollas."
    mc "Si tú empiezas una pelea, la voy a acabar yo."
    call BlinkXP ("c19s008_050" , "d") from _call_BlinkXP_3347
    kia "No hace falta que le pegues, [mc]."
    kia "No me voy a ir con él. Ni ahora ni nunca."
    scene c19s008_055a with dissolve
    "Detectas movimiento en la periferia de tu visión."
    "Te giras justo a tiempo."
    scene c19s008_055b with dissolve
    "La piltrafa humana, como lo ha llamado Eileen, ha intentado un puñetazo a traición."
    "Esos reflejos que no habías usado desde la segunda pelea con Jack entran en funcionamiento."
    scene c19s008_055c with hpunch
    play sound ("music/Slap.ogg")
    "Paras su puño con tu mano izquierda. Te queda la derecha libre."
    "Tu sangre entra en erupción."
    menu:
        "Darle un puñetazo por cobarde.":
            pass
        "Darle un puñetazo porque se lo merece.":
            pass
        "¿Qué coño? Darle un puñetazo.":
            pass
    scene c19s008_025h with hpunch
    play sound ("music/punch.ogg")
    "Tu puño derecho pasa de estar al lado de tu cintura a estar en la nariz de Solomon. Casi parece que se ha movido solo."
    mcp "(¡Joder! El capullo tiene la cabeza más dura que Jack.)"
    scene c19s008_025i with dissolve
    "Solomon sale volando, dejando un rastro de sangre saliendo a reacción por su nariz."
    "Acabas de hacer un favor a todos los hombres que recibieron como respuesta \"cuando los cerdos vuelen\" al pedirle sexo anal a su mujer."
    "Vuela como un cerdo. Sangra como un cerdo."
    scene c19s008_025j with hpunch
    play sound ("music/MurderByShovel.ogg")
    "*Dong*"
    "Su cabeza al impactar contra la furgoneta suena como un gong."
    scene c19s008_025k with dissolve
    mc "No te levantes, Solomon. O mejor aún, levántate para irte."
    sol "¡Me has pegado!"
    mc "¿Vas a dejar de decir obviedades? Levántate, sube al coche, y vete."
    mc "O ven a por más."
    call BlinkXP ("c19s008_060" , "d") from _call_BlinkXP_3348
    kia "Solomon, vete a tu casa. No voy a irme contigo."
    call BlinkXP ("c19s008_065" , "d") from _call_BlinkXP_3349
    eil "No hagas caso a Mama, Solomon. Levántate e intenta pegarle de nuevo."
    eil "[mc] es mucho más hombre de lo que tú nunca has sido. No es una mujer, que es a lo que estás acostumbrado a pegarle."
    scene c19s008_025l with dissolve
    mc "No tengo ganas de darte una paliza, pero lo haré si es necesario."
    mc "¡Qué coño! Tengo ganas de dártela, pero no quiero fastidiar la fiesta."
    sol "No te vas a quedar con mi mujer, hijo de puta."
    menu:
        "Darle una patada porque se lo merece.":
            pass
        "Darle una patada por insultar a tu madre.":
            pass
        "¿Qué coño? Darle una patada.":
            pass
    scene c19s008_070An with dissolve
    pause (1.0)
    play sound ("music/punch.ogg")
    scene c19s008_070bAn with hpunch
    mc "Me vas a poner muy difícil lo de no darte una paliza si no dejas de insultar a mi familia."
    scene c19s008_025m with dissolve
    sol "¿Tu familia? ¡Esa es mi familia! Solo quiero recuperarla."
    call BlinkXP ("c19s008_075" , "d") from _call_BlinkXP_3350
    eil "¿Recuperarla? ¿Así?"
    eil "Vienes aquí tratando a Mamá como mierda. Como has hecho siempre. Exigiéndole que vuelva a casa..."
    call BlinkXP ("c19s008_080" , "d") from _call_BlinkXP_3351
    kia "Llevo casi una semana aquí, Solomon. En una semana me han mostrado más respeto y cariño que tú en 22 años."
    kia "Esto es una familia. Lo que nosotros teníamos era una mala imitación de lo que debe ser una familia."
    call BlinkXP ("c19s008_085" , "d") from _call_BlinkXP_3352
    eil "Mamá es feliz aquí. Nunca volverá contigo."
    scene c19s008_025n with dissolve
    sol "¡Estamos casados! ¡Nunca te daré el divorcio!"
    sol "¡Estarás viviendo en pecado con este niñato!"
    mc "A mí puedes insultarme. Esta vez."
    call BlinkXP ("c19s008_090" , "d") from _call_BlinkXP_3353
    kia "[mc] y yo no estamos juntos, Solomon. Tan solo lo estamos en tu imaginación."
    kia "Vete a tu casa y déjanos en paz. Esta es una fiesta a la que no estás invitado."
    call BlinkXP ("c19s008_095" , "d") from _call_BlinkXP_3354
    eil "No están juntos..."
    if kia._var("route"):
        eil "Pero, si de mí depende, lo van a estar. Yo me ocuparé de ello."
    else:
        eil "Pero podrían estarlo. [mc] es más y mejor hombre de lo que tú serás nunca."
    call BlinkXP ("c19s008_100" , "h") from _call_BlinkXP_3355
    kia "¡Calla, Eileen!"
    mc "Puede opinar, Kiara. También es... era su familia."
    call BlinkXP ("c19s008_105" , "d") from _call_BlinkXP_3356
    kia "Puede opinar sobre su padre. No sobre lo que yo haga con mi vida o con quién esté. Es mi vida, no la suya."
    if kia._var("route"):
        mcp "(Parece que la conversación entre ellas no ha ido como Eileen esperaba.)"
    mc "Tienes razón. Es algo que solo tú puedes decidir."
    scene c19s008_025o with dissolve
    sol "¿Con quién estés? ¡Tienes que estar conmigo, maldita zorra! ¡Soy tu marido a los ojos de Dios!"
    mc "Te lo he advertido..."
    scene c19s008_025p with dissolve
    sol "¡Oh, no!"
    menu:
        "Darle una patada por capullo.":
            pass
        "Darle una patada por insultar a Kiara.":
            pass
        "¿Qué coño? Darle una patada.":
            pass
    scene c19s008_025q with hpunch
    play sound ("music/punch.ogg")
    "La sensación de tu pie desnudo impactando en sus testículos es desagradable."
    "La sensación de darle su merecido es increíble."
    scene c19s008_025r with dissolve
    sol "*Voz aguda* ¡Cabrón!"
    mc "No te vuelvas a levantar si no es para subirte al coche e irte."
    mc "No vuelvas a abrir la boca. Ni siquiera para despedirte."
    mc "Esto ya está dejando de ser divertido."
    mcp "(Nunca he sido un tipo violento, y estoy disfrutando esto demasiado.)"
    scene c19s008_025s with dissolve
    "Solomon te hace caso. Se levanta y se dirige al coche, con la cabeza baja, sin decir una palabra."
    stop music fadeout (1.5)
    scene c19s008_025t with dissolve
    "Se sienta en el coche, en silencio, durante unos segundos, antes de encender el motor."
    play music ("music/motor.ogg")
    call BlinkXP ("c19s008_110" , "d") from _call_BlinkXP_3357
    "Kiara te coge de los hombros y te gira hacia ella."
    kia "Gracias, [mc]. Tenías razón. No voy a estar mejor que en esta familia en ningún sitio."
    "Las piernas empiezan a temblarte. La adrenalina empieza a mostrar sus desagradables efectos secundarios."
    mc "Siempre tendrás tu lugar aquí, Kiara."
    call BlinkXP ("c19s008_115" , "h") from _call_BlinkXP_3358
    kia "¡Gracias, [mc]! ¡Gracias a todos vosotros!"
    "Tus piernas están temblando. Todo el cuerpo de Kiara tiembla como una hoja en un otoño ventoso."
    "La abrazas fuertemente. Te abraza como si su vida dependiera de ello."
    "Escuchas un sonido detrás tuyo. La puerta del coche de Solomon abriéndose."
    ama "¡Cuidado!"
    eil "¡[mc]!"
    oma "¡Detrás tuyo!"
    todas "*Cacofonía de advertencias*"
    scene c19s008_025u with fade
    "Giras la cabeza en el último segundo. Tus brazos aún alrededor de Kiara."
    sol "¡Hijo de la gran puta!"
    "Si esquivas el golpe se lo puede llevar Kiara. Te preparas para detener el golpe. Estás en situación de desventaja"
    scene c19s008_025v with dissolve
    play sound ("music/Desert-Eagle-Gunshot.ogg")
    "*Bang*"
    sol "¿Qué?"
    scene c19s008_120An with dissolve
    pause (2.1)
    play sound ("music/punch.ogg")
    scene c19s008_120bAn with hpunch
    "Amanda aparece de la nada, saltando la valla, y pegándole una patada a Solomon que parece salida de una película."
    stop music
    play music ("music/Dark-Score.ogg")
    "¿De dónde ha salido el disparo?"
    scene c19s008_125AnBlink with dissolve #AN d-blink
    "Eva te mira, con una mezcla de alivio, sonrisa, y disculpa en su cara."
    "Sabe que [mar] no quiere armas en casa. ¿La tenía escondida entre las plantas?"
    "Por una vez, te alegra que su respeto por las normas sea más bien laxo."
    call BlinkXP ("c19s008_130" , "d") from _call_BlinkXP_3359
    ama "Sube al coche y vete, pedazo de mierda. A menos que quieras probar a hacer un Leroy Jenkins."
    ama "Mi hermana nunca falla. Si vuelves a intentar algo así..."
    ama "Piensa que en este bosque hay mucho terreno donde enterrar un cadáver y que no lo encuentren nunca."
    "Habla tan calmadamente que da miedo."
    scene c19s008_025w with dissolve
    "Solomon se levanta, cada vez más magullado. Mantiene la puerta de la camioneta entre él y Amanda. Como si le fuese a servir de defensa."
    sol "¡Os voy a denunciar! ¡Me habéis disparado!"
    mc "Demuéstralo, gilipollas."
    call BlinkXP ("c19s008_135" , "d") from _call_BlinkXP_3360
    ama "Hazlo si quieres. O mejor. Inténtalo."
    ama "Vuelve a amenazar a alguien más de mi familia, vuelve a intentar tocarlos, y no podrás contarlo."
    "Ahora sí que da miedo."
    mc "Creo que lo ha entendido, Amanda."
    scene c19s008_025x with dissolve
    mc "No te quiero volver a ver en mi casa."
    mc "No quiero volver a escuchar tu voz."
    mc "No te quiero volver a ver cerca de Kiara ni de Eileen."
    sol "Me las pagarás..."
    mc "Te he dicho que no quiero volver a escuchar tu voz."
    scene c19s008_025y with dissolve
    "Solomon parece entrar en razón. O quizás su cerebro ha entendido que no le queda ninguna ventaja."
    stop music fadeout (1.5)
    "Entra en el coche sin decir una palabra. Se sienta en silencio, bajo la atenta mirada de Amanda."
    play music ("music/Fragile-Beauty.ogg")
    if kia._var("route"):
        call BlinkXP ("c19s008_140" , "d") from _call_BlinkXP_3361
        eil "Hazlo, Mamá."
        call BlinkXP ("c19s008_145" , "d") from _call_BlinkXP_3362
        kia "Pero..."
        call BlinkXP ("c19s008_140" , "d") from _call_BlinkXP_3363
        eil "Hazlo, Mamá. Es el momento."
        call BlinkXP ("c19s008_150" , "d") from _call_BlinkXP_3364
        kia "Chicas... siento todo esto..."
        kia "Siento que esta situación haya fastidiado la fiesta."
        kia "Pero tengo una cosa que decir..."
        call BlinkXP ("c19s008_155" , "d") from _call_BlinkXP_3365
        kia "[mc] y yo hemos estado hablando... y después he hablado con mi hija..."
        if mc._var("relationships")==1:
            if mar._var("route"):
                kia "También he hablado con [mar] y está de acuerdo."
            elif sai._var("route"):
                kia "También he hablado con Saira y está de acuerdo."
            elif nor._var("route"):
                kia "También he hablado con [nor] y está de acuerdo."
            elif emm._var("route"):
                kia "También he hablado con [emm] y está de acuerdo."
            elif eri._var("route"):
                kia "También he hablado con [eri] y está de acuerdo."
            elif dap._var("route"):
                kia "También he hablado con [dap] y está de acuerdo."
            elif sca._var("route"):
                kia "También he hablado con Scarlett y está de acuerdo."
            elif sam._var("route"):
                kia "También he hablado con Sam y está de acuerdo."
            elif sim._var("route"):
                kia "También he hablado con Simone y está de acuerdo."
            elif oma._var("route"):
                kia "No he tenido la oportunidad de hablar con Alexia, y no sé si estará de acuerdo..."
                call BlinkXP ("c19s008_160" , "d") from _call_BlinkXP_3366
                oma "Si vas a decir lo que me imagino, por mí adelante."
            elif mad._var("route"):
                kia "También he hablado con Maddie y está de acuerdo."
            elif deb._var("route"):
                kia "También he hablado con Debbie y está de acuerdo."
            elif meg._var("route"):
                kia "También he hablado con Megan y está de acuerdo."
        elif mc._var("relationships")>1:
            kia "No sé si las chicas del harén vais a odiarme o a aceptarme... Espero que sea lo último. Al menos con las que he tenido la oportunidad de hablar así ha sido."
        call BlinkXP ("c19s008_165" , "d") from _call_BlinkXP_3367
        kia "Es el momento de que deje de engañarme. De que afronte mis sentimientos..."
        kia "Si me aceptas, me gustaría explorar los sentimientos de los que hemos hablado antes. No voy a conseguir que dejen de crecer."
        mc "Kiara, ¿aceptarte? Estaría loco si no lo hiciera. Y ya has hecho tú todo el trabajo..."
        scene c19s008_165d with hpunch
        "Kiara se lanza a tus brazos otra vez. Esta vez no busca un abrazo, busca tus labios."
        "Tímidamente al principio. Con más énfasis mientras pasan los segundos..."
        "Los dos sabéis que es el primer beso de muchos, que va a hacer de tus labios su hogar."
        "Un hogar que, obviamente, nunca compartirá con Solomon."
        scene c19s008_025z with dissolve
        "Tan solo Amanda presta atención a la cara de sorpresa de Solomon."
        scene c19s008_025za with dissolve
        "Solo ella se da cuenta de que arranca el coche y se va."
        call BlinkXP ("c19s008_170" , "d") from _call_BlinkXP_3368
        kia "*Susurrando* Creo que es lo más difícil que he hecho nunca. Pero sienta tan bien..."
        mc "Me alegra que hayas dado este paso, Kiara."
        call BlinkXP ("c19s008_175" , "d") from _call_BlinkXP_3369
        emm "¡Ha sido tan romántico! ¡Parece el guion de una película romántica mala! Pero ha quedado tan bonito..."
    else:
        call BlinkXP ("c19s008_115" , "h") from _call_BlinkXP_3370
        "Kiara se vuelve a lanzar a tus brazos en un abrazo lleno de agradecimiento."
        call BlinkXP ("c19s008_175" , "d") from _call_BlinkXP_3371
        emm "¡Ha sido alucinante! ¡Parece el guion de una película romántica mala! Sólo ha faltado que os besarais..."
        scene c19s008_025za with dissolve
        "Solo Amanda se da cuenta de que Solomon arranca el coche y se va."
    scene c19s008_180a with dissolve
    stop music fadeout (1.5)
    "Las chicas arrancan a Kiara de tus brazos y se la llevan hacia la piscina. Ellas también quieren consolarla."
    play music ("music/LostVoices.ogg")
    if kia._var("route"):
        "O felicitarla por su decisión de dejar completamente atrás su pasado."
    call BlinkXP ("c19s008_185" , "d") from _call_BlinkXP_3372
    ama "Nunca más vuelvas a hacerme esto, [mc]."
    ama "Nunca des la espalda a un enemigo, aunque parezca derrotado."
    mc "Lo siento... y gracias."
    call BlinkXP ("c19s008_190a" , "d") from _call_BlinkXP_3373
    eva "Y pídele disculpas a [mar] de mi parte por haber escondido algunas armas en su casa..."
    eva "A mí me da vergüenza... nos habéis tratado tan bien que... siento que os he traicionado... un poco."
    mc "No creo que le importe en este caso."
    mc "Y gracias a ti también."
    mc "¿Cuántas armas tienes repartidas por la casa?"
    call BlinkXP ("c19s008_190b" , "d") from _call_BlinkXP_3374
    eva "Siete... no, ocho... Pero nadie las ha encontrado nunca."
    mc "Creo que sería bueno que las retiraras, o las pusieras en una caja fuerte o algo..."
    call BlinkXP ("c19s008_195" , "d") from _call_BlinkXP_3375
    eva "Pero hoy han servido de algo... Si hubiera estado en una caja fuerte, dentro de casa..."
    mc "Por eso no le va a importar. Pero no va a querer armas por casa al alcance de cualquiera."
    call BlinkXP ("c19s008_200" , "d") from _call_BlinkXP_3376
    ama "No, no le va a hacer ilusión, pero tenemos que tener medios para proteger a la familia."
    ama "Aunque hoy lo has hecho muy bien excepto por lo de darle la espalda. La violencia justa y, especialmente, necesaria. No te has excedido."
    call BlinkXP ("c19s008_205" , "d") from _call_BlinkXP_3377
    eva "Yo seguramente hubiese dejado su cara hecha pulpa al segundo insulto. Me habría costado contenerme."
    eva "Y me ha costado no fallar cuando he disparado a la llave. Esa cabeza era un blanco tentador."
    mc "*Risa* Ya has dicho antes que un asesinato podía fastidiar la fiesta. Limpiar sangre y esas cosas..."
    if kia._var("route"):
        call BlinkXP ("c19s008_210" , "d") from _call_BlinkXP_3378
        ama "Solo tengo una pregunta, [mc]."
        mc "Dime."
        call BlinkXP ("c19s008_215" , "d") from _call_BlinkXP_3379
        ama "¿Vamos a tener que ponernos en plan damisela en apuros nosotras también para conseguir un beso como ese?"
    else:
        call BlinkXP ("c19s008_210" , "d") from _call_BlinkXP_3380
        ama "¿Sabes que por un momento he pensado que Kiara iba besarte?"
        ama "He pensado que el modo damisela en apuros iba a forzarte a aceptarla."
        call BlinkXP ("c19s008_215" , "d") from _call_BlinkXP_3381
        ama "Y después he pensado en qué pasaría si nosotras también estuviéramos en esa situación."
    mc "*Risa* No os pegaría el papel de damisela en apuros, Amanda. O al menos no como lo estaba Kiara."
    mc "Aún no sé si quiero tener una relación con vosotras y no lo voy a saber hasta que no resolváis lo que hablamos anoche."
    call BlinkXP ("c19s008_220" , "d") from _call_BlinkXP_3382
    eva "¿Qué? ¿Aún no lo sabes?"
    mc "No, Eva. Hasta que no me digáis qué condiciones va a tener esa relación... o esas relaciones."
    call BlinkXP ("c19s008_225" , "d") from _call_BlinkXP_3383
    eva "¡Entonces no hay tiempo que perder, Amanda!"
    call BlinkXP ("c19s008_230" , "d") from _call_BlinkXP_3384
    eva "Nos vamos a algún lugar donde podamos hablar en privado."
    scene c19s008_235a with dissolve
    "Eva y Amanda se van, dejándote solo."
    "El resto de las chicas están con Kiara."
    scene c19s008_180a with dissolve
    "Solomon no ha conseguido su objetivo de que Kiara se fuera con él."
    "Pero su aparición ha matado el ambiente de la fiesta de cumpleaños."
    "El resto de la tarde gira alrededor de su visita. Todo el mundo quiere apoyar a Kiara."
    scene c19s008_235d with dissolve
    if kia._var("route"):
        $ mc._var("relationships", 1, "add")
        "Que Kiara se haya unido a las revelaciones del día tan solo ayuda a ello."
        if mc._var("relationships")>2:
            "Es la primera vez que alguien pide permiso para entrar en el harén, lo cual lo hace especial en cierto modo."
        elif mc._var("relationships")==2:
            "Que haya mostrado el respeto suficiente hacia tu relación previa para pedir permiso, lo hace especial en cierto modo."
    else:
        "Amanda no es la única que ha pensado que Kiara iba a besarte."
    scene c19s008_235h with dissolve
    "Todas las chicas se acercan a ti en algún momento de la tarde, preocupadas por cómo te sientes tras lo que ha pasado."
    "Todas ellas saben que la violencia no va contigo y que has actuado movido por la necesidad."
    "Ninguna sabe que has disfrutado cada bofetón, puñetazo, y patada."
    "Lo ocultas haciendo bromas sobre la fiesta y los regalos. Evitas hablar de la visita de Solomon."
    scene c19s008_235e with dissolve
    "Amanda y Eva se pasan el resto de la tarde charlando, intentando resolver sus diferencias."
    stop music fadeout (1.5)
    "Prefieres no acercarte demasiado. Aún no estás preparado para tomar una decisión."
    scene c19s008_235f with dissolve
    play music ("music/Looking-Forward.ogg")
    "Cuando el sol deja de calentar, las chicas que viven en la ciudad empiezan a irse."
    "Excepto Maddie, que se queda para la partida de DnD."
    "Todas rechazan la invitación a quedarse a cenar, para tristeza de Jamaal."
    "Jamaal se lleva sobras para cenar. Sobras con las que cenarían cuatro o cinco personas."
    scene c19s008_235g with dissolve
    "Las que viven en casa pasan por la ducha haciendo turnos o duchándose en grupo."
    "Tú te duchas en el gimnasio. Nadie intenta pillarte desnudo mientras lo haces."
    scene black with dissolve
    "Una vez rechazadas las invitaciones a cenar, descubrís que nadie tiene hambre. Todos habéis comido demasiado."
    "Un día entero en la piscina os ha dejado a todos agotados. La mayoría de las chicas se retiran pronto a sus habitaciones."
    "[emm] se queja de que una partida de DnD sin pizza va a ser rara. Alguien comenta que le apetecía pizza con kiwi."
    "Es un alivio que todos hayáis comido demasiado y no tengáis que pedir ese crimen contra la humanidad. Si la piña tiene mala fama en la pizza, el kiwi tiene que ser el peor invento de la historia."
    return
label c19s009_Teaser:
    stop music fadeout (1.5)
    "Te preparas para tu primera partida de DnD. No tienes ni idea de lo que esperar pese a que [dap] y Scarlett te lo han explicado cien veces los últimos días."
    call BlinkXP ("c19s009_005" , "d") from _call_BlinkXP_3385
    play music ("music/Throne-King.ogg")
    "Cuando llegas a la cocina, solo están [dap] y Scarlett. [dap] tiene un montón de cosas extrañas encima de la mesa."
    "Deben ser los famosos dados para jugar a rol."
    dap "¡Qué puntual! Siéntate a ese lado, en la segunda silla. La primera es de Scarlett."
    call BlinkXP ("c19s009_010" , "d") from _call_BlinkXP_3386
    sca "Necesito estar al lado de [dap] para mover las figuras. Ella no llega."
    mc "Ningún problema. Así también me ayudas a mí. Soy el único novato."
    scene c19s009_010d with dissolve
    dap "¿Preparado para la mayor aventura de tu vida?"
    sca "No te asustes, es posible que no sea tanto como esperas."
    dap "Tendrás que esperar un poco. Tienen que llegar el resto de las chicas."
    sca "Suelen ser más puntuales, pero [eri] se está cambiando con Maddie. Empezaremos en poco tiempo."
    stop music fadeout (1.5)
    return

label c23:
    call c23s000_DiscoveredPregnancies from _call_c23s000_DiscoveredPregnancies
    if sca._var("route"):
        call c23s001_ScaSex from _call_c23s001_ScaSex
    else:
        call c23s001_NoScaSex from _call_c23s001_NoScaSex
    call c23s002_SaiPregnancy from _call_c23s002_SaiPregnancy
    call c23s002_Lugagge from _call_c23s002_Lugagge
    call c23s002_NoPatty from _call_c23s002_NoPatty
    call c23s003_Eil from _call_c23s003_Eil
    call c23s004_Kia from _call_c23s004_Kia
    call c23s004_Oma from _call_c23s004_Oma
    call c23s004_Kim from _call_c23s004_Kim
    call c23s005_MarVisit from _call_c23s005_MarVisit
    call c23s006_TripToMonterrey from _call_c23s006_TripToMonterrey
    call c23s006_FerrariniGirl from _call_c23s006_FerrariniGirl
    call c23s006_AfterTheMeeting from _call_c23s006_AfterTheMeeting
    call c23s007_AmaCalls from _call_c23s007_AmaCalls
    call c23s007_SleepingArrangements from _call_c23s007_SleepingArrangements
    return
label c23s001_DayChange:
    scene black with dissolve
    centered "{size=+20}{b}DÍA 23 – MIÉRCOLES{/b}{/size}"
    if mc._var("edmundsStory") and not sca._var("route"):
        "Cuando te despiertas, [sca] ya no está en tu cama."
    return
label c23s001_ScaSex:
    if _in_replay:
        call mrS3_sca_pregnant from _call_mrS3_sca_pregnant_1
        call mrS3_sca_anal from _call_mrS3_sca_anal
        call mrS3_edmund_story from _call_mrS3_edmund_story_2
        call mrS3_rels from _call_mrS3_rels_4
    call c23s001_DayChange from _call_c23s001_DayChange
    call c00Renames from _call_c00Renames_1
    play music ("music/m0450.ogg")
    "Te despiertas abrazado a [sca]. Es una gran sensación."
    scene c23s001_005a with fade
    "Una de tus manos ha buscado un lugar cómodo para descansar durante la noche, un precioso lugar."
    "Decides retirarla lentamente para no despertar a [sca]."
    call BlinkXPS3 ("c23s001_010" , "d") from _call_BlinkXPS3_1017
    sca "No hace falta que la quites si no quieres."
    mc "¿Estás despierta?"
    call BlinkXPS3 ("c23s001_015" , "d") from _call_BlinkXPS3_1018
    "Devuelves la mano a su cómoda posición. Y empiezas a besar su espalda."
    sca "No, hablo en sueños sobre mi novio tocándome una teta. *Risa*"
    mc "*Risa* Creo que todas pasáis demasiado tiempo con Jamaal."
    mc "*Smooch* No me imagino a la [sca] de hace tres semanas contestándome así. *Risa*"
    call BlinkXPS3 ("c23s001_020" , "d") from _call_BlinkXPS3_1019
    sca "Y aquella [sca] no se podía imaginar que, tres semanas después, estaría durmiendo contigo."
    sca "Aunque solo haya sido dormir."
    mc "*Smooch* Han pasado muchas cosas en tres semanas, ¿verdad?"
    call BlinkXPS3 ("c23s001_025" , "d") from _call_BlinkXPS3_1020
    sca "Muchísimas. Mi vida ha cambiado totalmente, y no solo por despertarme con una mano en mi teta."
    sca "Salgo con el único chico con quien he querido salir en toda mi vida."
    if sca._var("pregnant"):
        sca "Me he quedado embarazada."
    if persistent.family and mc._var("edmundsStory"):
        sca "He descubierto quién es mi padre."
    sca "He encontrado a una familia de verdad..."
    sca "Muchísimas cosas, pero no demasiadas. Si son tan buenas como las que han pasado, espero que pasen más cosas todavía."
    mc "*Smooch* Yo también, cielo."
    mc "Y no es por despreciar a tu maravillosa teta, pero... ¿no hay beso de buenos días?"
    call BlinkXPS3 ("c23s001_030" , "v") from _call_BlinkXPS3_1021
    sca "¿Qué? ¿Sin lavarme los dientes? Seguro que el aliento me huele mal después de dormir."
    mc "Mírame, [sca]."
    call BlinkXPS3 ("c23s001_035" , "f") from _call_BlinkXPS3_1022
    sca "Seguro que me huele la boca..."
    mc "A esta distancia no puedo oler nada, y voy a besarte."
    call BlinkXPS3 ("c23s001_040" , "d") from _call_BlinkXPS3_1023
    sca "Pero..."
    scene c23s001_040d with hpunch
    "Sin dejarle contestar aprisionas sus labios entre los tuyos."
    "No emite ningún olor desagradable."
    "Aunque lo hiciera, no te perderías la primera vez que puedes besarla tras dormir juntos."
    call BlinkXPS3 ("c23s001_045" , "d") from _call_BlinkXPS3_1024
    mc "Ningún mal olor o sabor. ¿Qué tal mi aliento?"
    sca "Tampoco tienes mal sabor. ¿Será un mito?"
    mc "No, no lo es. A alguna gente le huele el aliento por la mañana, una vez leí el por qué pero me he olvidado."
    call BlinkXPS3 ("c23s001_050" , "d") from _call_BlinkXPS3_1025
    sca "Leí que tiene que ver con la producción de saliva y..."
    scene c23s001_040d with hpunch
    "No tienes el menor interés en entrar en una discusión sobre por qué le huele el aliento a la gente."
    scene c23s001_040e with dissolve
    "Lo único que quieres es seguir disfrutando de esos labios."
    if persistent.family and mc._var("edmundsStory"):
        "Los labios de tu hermana recién recuperada."
        $ sca._var("halfSister", True)
    else:
        $ sca._var("halfSister", False)
    call BlinkXPS3 ("c23s001_055" , "d") from _call_BlinkXPS3_1026
    sca "¡[mc]! ¡Me has interrumpido!"
    mc "Había unos preciosos labios que requerían mi atención."
    call BlinkXPS3 ("c23s001_060" , "d") from _call_BlinkXPS3_1027
    sca "Si es por eso, puedes interrumpirme tantas veces como quieras. *Risa*"
    call BlinkXPS3 ("c23s001_065" , "d") from _call_BlinkXPS3_1028
    sca "Aunque ahora te voy a interrumpir yo. Me he dado cuenta de que Mjolnir se ha despertado. Está presionando contra mi ombligo."
    mc "Es su forma de darte los buenos días."
    call BlinkXPS3 ("c23s001_070" , "d") from _call_BlinkXPS3_1029
    sca "Yo tengo mi propia forma de saludarlo."
    scene c23s001_075AnBlink with dissolve
    mc "¿Vas a algún sitio?"
    sca "A quitarme la ropa. *Risa* Mjolnir y yo tenemos confianza y le gusta verme desnuda, ¿no?"
    stop music fadeout (1.5)
    mc "Por supuesto. *Risa* A mí también me encanta."
    play music ("music/CCFunk.ogg")
    scene c23s001_080AnBlink with dissolve
    sca "Pues ya está... no queda ropa."
    mc "Me encanta esta nueva [sca] que toma la iniciativa."
    call BlinkXPS3 ("c23s001_085" , "d") from _call_BlinkXPS3_1030
    sca "Va a ser nuestra segunda vez. La primera estaba nerviosísima y te dejé marcar el ritmo."
    sca "No tenía ni idea de cómo debía actuar."
    sca "Ahora quiero probar a hacerlo a mi paso, si no te importa."
    if sca._var("halfSister"):
        mc "Para nada, hermanita. Sorpréndeme."
    else:
        mc "Para nada, cielo. Sorpréndeme."
    call BlinkXPS3 ("c23s001_090" , "f") from _call_BlinkXPS3_1031
    "Para tu sorpresa, [sca] tira el edredón al suelo, te tumba de espaldas, se sube a horcajadas encima tuyo y apunta a Mjolnir hacia su coño."
    sca "¿Preparado?"
    mc "Sorprendido pero preparado. *Risa*"
    call BlinkXPS3 ("c23s001_095" , "d") from _call_BlinkXPS3_1032
    sca "¿Sorprendido? ¿Por qué? ¿Qué tenía que hacer?"
    mc "No tenías que hacer nada, cielo. Pero creía que querrías unos preliminares antes."
    call BlinkXPS3 ("c23s001_100" , "d") from _call_BlinkXPS3_1033
    sca "¡Vaya! Sabía que se me olvidaba algo..."
    sca "¿Quieres que baje y juguemos un poco?"
    mc "Quiero que hagas lo que quieras hacer. Habrá tiempo para preliminares otro día si no te apetecen."
    scene c23s001_105An with dissolve
    "Antes de responder, [sca] se empala en tu polla en un rápido movimiento."
    sca "¡Ufff! Demasiado tentador."
    call BlinkXPS3 ("c23s001_110" , "d") from _call_BlinkXPS3_1034
    sca "Me encantaron los preliminares, pero esto me gustó más aún."
    mc "No me voy a quejar. *Risa*"
    sca "¿Puedo empezar a moverme ya?"
    mc "Cuando tú quieras. Tú tienes el control."
    scene c23s001_910pv with dissolve
    show c23s001_910v
    "[sca] empieza a moverse arriba y abajo a lo largo de tu astil, en una posición que considerarías incomodísima."
    if mc._var("edmundsStory"):
            sca "*Gemido* Te echaba de menos, [mc]. *Jadeo* Me he tenido que retener de visitarte todos estos días. *Gemido*"
    else:
        sca "*Gemido* Te echaba de menos [mc]. *Jadeo*"
    "La luz del amanecer baña vuestros cuerpos y proyecta sombras que hace que parezca que hay otra pareja haciendo el amor en la misma habitación."
    if mc._var("edmundsStory"):
        sca "*Jadeo* Me daba miedo que no quisieras acostarte conmigo hasta que lo descubriéramos. *Gemido*"
        if sca._var("halfSister"):
            mc "Nunca rechazaría esto contigo, hermanita. El resultado no iba a afectarme en eso."
        else:
            mc "Nunca rechazaría esto contigo, cielo. El resultado no iba a afectarme en eso."
    else:
        sca "*Jadeo* No sé por qué no te he visitado desde que llegué a casa. *Gemido*"
    mc "Los dos nos lo hemos perdido. *Risa* Tenemos que recuperar el tiempo perdido."
    if sca._var("halfSister"):
        "Al escuchar tu frase, las paredes vaginales de tu hermana se cierran con fuerza sobre tu astil. Las sombras siguen follando como si no les importara."
    else:
        "Al escuchar tu frase, las paredes vaginales de [sca] se cierran con fuerza sobre tu astil. Las sombras siguen follando como si no les importara."
    scene c23s001_900pv with dissolve
    hide c23s001_910v
    show c23s001_900v
    "Apoyándose en tu hombro para mantener el equilibrio, no deja de subir y bajar a lo largo de tu polla mientras la dorada luz del amanecer se derrama sobre su cuerpo."
    if sca._var("halfSister"):
        sca "*Gemido* Tengo toda una vida que recuperar contigo. *Jadeo* Pensar que siempre he estado enamorada de mi hermano... *Gemido*"
    else:
        sca "*Gemido* Tenemos mucho que recuperar. *Jadeo* Toda una vida enamorada de ti... *Gemido*"
    "Su húmeda raja abraza tu enhiesta polla con fuerza. Ella sabe que ahora eres suyo. Que ella es tuya. Que su infantil sueño se ha cumplido."
    sca "*Jadeo* Nunca hubiera soñado poder hacer esto contigo. *Gemido* Es un sueño hecho realidad. *Jadeo*"
    "Es la primera vez que os despertáis juntos, pero el sueño continúa. Vendrán más veces. Continuaréis soñando."
    scene c23s001_905pv with dissolve
    hide c23s001_900v
    show c23s001_905v
    if sca._var("halfSister"):
        $ YourSister = __("tu hermana")
    else:
        $ YourSister = sca.name
    "Mjolnir se desliza en el interior de [YourSister] como si se tratara de su hogar. [sca] baja profundamente, impactando con su cérvix en tu glande cada vez."
    sca "*Gemido* Me estás destrozando. *Jadeo* ¡Me encanta! *Gemido*"
    "Puedes notar cómo se va humedeciendo cada vez más, cómo su coño está cada vez más caliente."
    sca "*Jadeo* Podría estar haciendo esto horas. *Gemido* La segunda vez es mejor que la primera. *Jadeo*"
    "Dudas que en esa posición pueda durar mucho tiempo más. Sigues pensando que tiene que ser muy incómodo para ella estar con las piernas tan abiertas."
    scene c23s001_915pv with dissolve
    hide c23s001_905v
    show c23s001_915v
    "Pero, si es necesario, estás preparado para tomar el control. No quieres que esto acabe con un calambre en una de sus piernas."
    sca "*Gemido* ¡Quiero despertarme así todos los días! *Jadeo* ¡Esto es lo mejor del mundo! *Gemido*"
    "Las sensaciones a lo largo de tu polla corroboran sus palabras. El ritmo que marca [YourSister] está siendo increíble."
    sca "*Jadeo* ¡Fóllame más duro! *Gemido* ¡Más rápido! *Jadeo* ¡Más profundo! *Gemido*"
    "En esta posición ella es la que marca el ritmo. No puedes hacer mucho más que sincronizar tus caderas con sus movimientos."
    scene c23s001_920pv with hpunch
    hide c23s001_915v
    "La cambias de posición sin salir de su coño."
    sca "*Jadeo* ¿Qué haces? *Gemido* ¡Estaba a punto de llegar! *Jadeo*"
    mc "Follarte más duro."
    show c23s001_920v
    "En esta nueva posición tienes el control del que carecías antes. Puedes marcar el ritmo que quieres. El que [YourSister] necesita."
    sca "*GEMIDO* ¿QUÉ? *JADEO* ¿Por qué me has dejado a mí encima? *GEMIDO* ¡Esto es mucho mejor! *JADEO*"
    "Bombeas más duro, más rápido, más profundo de lo que ella podía hacer estando encima. Ella te lo ha pedido. Te alegra cumplir su petición."
    sca "*JADEO* ¡Nunca más me dejes ponerme encima! *GEMIDO* Nunca dejes de follarme así. *JADEO*"
    "No piensas hacerlo. Te gusta probar nuevas posiciones. Pero las que funcionan a la perfección siempre estarán en tu repertorio."
    scene c23s001_925pv with dissolve
    hide c23s001_920v
    show c23s001_925v
    "Con Mjolnir disfrutando de total libertad para marcar el ritmo, embistes el coño de [YourSister] como si te fuera la vida en ello."
    sca "*GEMIDO* ¡JODER, JODER, JODER! *JADEO* ¡ME ENCANTA! *GEMIDO*"
    "Tu velocidad se incrementa, llegando a lo más profundo de [sca] con cada embestida. Su cuerpo se tensa, anunciando un inminente orgasmo."
    sca "*JADEO* ¡Me voy a correr! *GEMIDO* ¡Quiero que nos corramos juntos! *JADEO*"
    "Será en otra ocasión. Aún te queda gasolina en el depósito para un rato. Quizás en su siguiente orgasmo..."
    scene c23s001_930pv with dissolve
    hide c23s001_925v
    show c23s001_930v
    "Su preciosa cara refleja todas las sensaciones que está experimentando en su coño. El placer, la resistencia a correrse, o la sorpresa cuando tocas un punto nuevo."
    sca "*GEMIDO* ¡Córrete conmigo! *JADEO* ¡TE QUIERO! *GEMIDO*"
    "Esta vez el 'Te quiero' llega antes del orgasmo. Suena incluso mejor que otras veces."
    mc "Y yo a ti, mi vida."
    mc "A mí me queda un poco, pero córrete para mí, mi amor."
    "No puede resistirse más a las sensaciones que recorren su cuerpo. Su orgasmo llega como una explosión."
    call OrgasmXS3 ("c23s001_115") from _call_OrgasmXS3_30
    sca "*GEMIDO* ¡SÍ! *JADEO* ¡ME CORRO! *GEMIDO*"
    scene c23s001_935pv with vpunch
    "Da un salto abrazándose a ti, intentando empalarse más profundamente con Mjolnir."
    "La sujetas como puedes mientras mantienes el equilibrio con una sola mano."
    sca "*JADEO* ¡NO PARES! *JADEO* ¡ES ENORME! *GEMIDO*"
    "Hablando de posiciones incómodas, es tu turno de practicar una nueva posición aguantando todo el peso de [sca]."
    hide c23s001_930v
    show c23s001_935v
    "Afortunadamente [YourSister] es ligera y se agarra a ti como un koala a su eucalipto. Apenas tienes que hacer fuerza con la mano que tienes en su espalda."
    sca "*GEMIDO* ¡OH, SÍ! *JADEO* ¡ES INCREÍBLE! *GEMIDO*"
    "La postura limita el recorrido de tus caderas. El cuerpo de [sca] se mueve junto al tuyo, con lo que Mjolnir entra y sale tan solo unos centímetros en cada embestida."
    sca "*JADEO* ¡ARF! *GEMIDO* ¡Me encanta hacer el perezoso! *JADEO*"
    "Casi se te escapa una carcajada. Entre koala y perezoso, te quedas con koala."
    scene c23s001_940pv with dissolve
    hide c23s001_935v
    show c23s001_940v
    "No tardas en encontrar un ritmo que vuelve a ser maravillosamente placentero. Orgasmo tras orgasmo recorren el cuerpo del koala."
    sca "*GEMIDO* ¡Así estás tocando puntos que ni sabía que tenía! *GEMIDO*"
    "Pese a la extraña posición, te vas acercando a tu clímax ayudado por las oleadas que recorren el coño de [YourSister], aprisionando tu polla."
    sca "*JADEO* ¡No puedo parar de correrme! *JADEO*"
    "Sus piernas se cierran con fuerza sobre tu espalda a cada embestida. Creías que no aguantaría en esta posición, pero es imposible que se suelte."
    scene c23s001_945pv with dissolve
    hide c23s001_940v
    show c23s001_945v
    "Mientras ella sigue abrazada a su eucalipto, tú la embistes con tu tronco. La combinación perfecta."
    mc "Me estoy acercando, [sca]."
    "Su cuerpo responde a la perspectiva de recibir tu leche con otro orgasmo. Sus piernas y brazos se cierran aún con más fuerza a tu alrededor."
    sca "*GEMIDO* ¡LLÉNAME! *JADEO*"
    if sca._var("halfSister"):
        sca "*JADEO* ¡Llena a tu hermana con tu semen! *GEMIDO*"
    "Con sus piernas alrededor de tu cuerpo, va a ser imposible no hacerlo."
    if persistent.pregnancy and not sca._var("pregnant"):
        if persistent.walkthrough:
            $ wt1 = _("[sca] embarazada.")
            $ wt2 = _("Sin consecuencias.")
        else:
            $ wt1 = ""
            $ wt2 = ""
        menu:
            "Correrte dentro" (wt = wt2):
                pass
            "Correrte dentro. Ir a por el bebé." (wt = wt1):
                $ sca._var("pregnant", True)
                $ sca._var("undiscoveredPregnancy", True)
                play sound ("music/OldMusicBox5.ogg")
    $ resetWalkthrough ()
    call OrgasmXS3 ("c23s001_120") from _call_OrgasmXS3_31
    mc "¡Mpfft!"
    if sca._var("halfSister"):
        "Explotas en el interior de tu dulce y sexy hermana, al mismo tiempo que un nuevo orgasmo la recorre."
    else:
        "Explotas en el interior de la dulce y sexy [sca], al mismo tiempo que un nuevo orgasmo la recorre."
    sca "*JADEO* ¡SÍ! *GEMIDO* ¡LLÉNAME!"
    "Vuestros fluidos se entremezclan en un momento de placer compartido."
    if sca._var("halfSister"):
        "Tan solo un par de hermanos corriéndose simultáneamente."
    scene c23s001_940pv with dissolve
    hide c23s001_945v
    show c23s001_940v
    "Continúas embistiendo a [sca] durante unos momentos más, hasta que empiezas a notar que sus piernas y brazos están ejerciendo menos presión a tu alrededor."
    stop music fadeout (1.5)
    "Decides dejarla suavemente encima de la cama."
    play music ("music/ChillUkelele.ogg")
    call BlinkXPS3 ("c23s001_125" , "f") from _call_BlinkXPS3_1035
    hide c23s001_940v
    mc "¿Te ha gustado, mi precioso koala?"
    sca "*Risa* ¿Qué? ¿Koala? ¿A qué viene eso?"
    mc "Abrazada así a mí, es lo que me ha venido a la cabeza. Tú has dicho perezoso, pero me gustan más los koalas."
    mc "Creía que ibas a estar incómoda o que te ibas a soltar en cualquier momento."
    call BlinkXPS3 ("c23s001_130" , "d") from _call_BlinkXPS3_1036
    sca "Me gusta lo de koala. *Risa* No me hubiera podido soltar aunque hubiera querido."
    sca "Con cada orgasmo las piernas se cerraban solas a tu alrededor. Ha sido increíble."
    mc "Me gusta que hayas disfrutado nuestro primer despertar juntos. Habrá más."
    call BlinkXPS3 ("c23s001_135" , "d") from _call_BlinkXPS3_1037
    sca "Me podría despertar así todos los días..."
    call BlinkXPS3 ("c23s001_140" , "d") from _call_BlinkXPS3_1038
    sca "No, mejor no... *Risa* Si repitiéramos esto todas las mañanas no podría juntar las piernas el resto del día."
    mc "Bueno, tampoco hay que ser avaricioso. *Risa* Tenemos toda una vida para repetir esto cuando quieras."
    mc "Pero ahora quiero mi ración de abrazos. En eso sí que soy avaricioso."
    if sca._var("anal"):
        call BlinkXPS3 ("c23s001_145" , "d") from _call_BlinkXPS3_1039
        sca "No solo repetir, hacer variaciones."
        mc "¿A qué te refieres?"
        call BlinkXPS3 ("c23s001_150" , "d") from _call_BlinkXPS3_1040
        sca "A que me encantó lo que hicimos la última vez... ya sabes... por detrás."
        sca "Podríamos repetir algún día..."
        mc "¿Algún día? ¿Por qué no hoy?"
        call BlinkXPS3 ("c23s001_155" , "v") from _call_BlinkXPS3_1041
        sca "¿Qué? ¿Estás listo tan rápido? ¿No necesitas descansar?"
        stop music fadeout (1.5)
        if sca._var("halfSister"):
            mc "No, hermanita, no necesito descansar si quieres esto. U otra cosa."
        else:
            mc "No, cielo, no necesito descansar si quieres esto. U otra cosa."
        play music ("music/LePrunierenFleur.ogg")
        call BlinkXPS3 ("c23s001_160" , "d") from _call_BlinkXPS3_1042
        sca "No, no. *Risa* ¡Has dicho hoy, y va a ser hoy!"
        sca "Déjame limpiarte un momento y me dices cómo debo ponerme."
        scene c23s001_165a with fade
        "[sca] se mete tu polla en la boca y empieza a lamer los restos entremezclados de semen y de sus propios orgasmos."
        "Si Mjolnir no estuviera duro como una piedra, sólo con esta visión recuperaría cualquier erección perdida."
        scene c23s001_965pv with fade
        "Tras unos lametones, con [YourSister] ansiosa por recibir a Mjolnir por detrás, os ponéis en posición."
        mc "¿Lista?"
        "Apoyas tu glande firmemente contra el estrecho agujero de [sca], esperando su luz verde."
        sca "Adelante. No hace falta que vayas con cuidado."
        show c23s001_965v
        pause (0.43)
        scene c23s001_965dv
        "El estrecho agujero de [sca] opone una resistencia mucho mayor que la última vez."
        scene c23s001_165b with hpunch
        sca "¡Ufff!"
        "Supones que no ha usado el plug en los últimos días. La sensación a lo largo de tu astil es maravillosa."
        mc "¿Estás bien?"
        call BlinkXPS3 ("c23s001_170" , "d") from _call_BlinkXPS3_1043
        sca "Sí, no te preocupes. Me he sentido ensartada en un espeto por un momento. Pero ya estoy bien."
        sca "Puedes empezar a moverte cuando quieras."
        scene c23s001_955pv with dissolve
        hide c23s001_965v
        show c23s001_955v
        "Los primeros movimientos te indican que va a ser una experiencia increíble. El apretado culo de [YourSister] exprime tu polla a cada embestida."
        sca "*Gemido* Es mejor de lo que recordaba. *Jadeo* Mucho mejor. *Gemido*"
        "Los músculos se distienden tal como el placer de [sca] va aumentando. Su agujero sigue igual de estrecho, pero ya no es una batalla."
        sca "*Jadeo* Me podría convertir en una adicta a esto. *Gemido* No podría decidirme entre anal y vaginal... *Jadeo*"
        "Adoras las dos cosas, con lo que no te importa demasiado lo que decida. Cualquier cosas que le guste es buena para ti."
        mc "No hace falta que decidas. Me encantan ambas."
        scene c23s001_960pv with dissolve
        hide c23s001_955v
        show c23s001_960v
        "El culo de [sca] se contrae por un momento, pensando en lo mucho que vais a disfrutar de vuestros gustos compartidos."
        sca "*JADEO* Me encanta sentirme llena de ti. *GEMIDO* Me da lo mismo qué parte de mí. *JADEO*"
        "Compartes el sentimiento con ella. Mientras los dos disfrutéis de la experiencia, da lo mismo la postura o lo que hagáis."
        sca "*GEMIDO* ¿Cómo es posible que vaya a tener un orgasmo más rápido por detrás? *GEMIDO*"
        "Los orgasmos previos han preparado su cuerpo para seguir experimentando placer, dejándola sensible a tus embestidas."
        mc "A mí me pasa lo mismo. No voy a poder aguantar mucho. Eres muy estrecha aquí detrás."
        scene c23s001_950pv with dissolve
        hide c23s001_960v
        show c23s001_950v
        "Tú también estás sensible. Tu capullo aún está sensible de la corrida anterior y de la limpieza que te ha hecho [sca]."
        sca "*JADEO* ¡NO TE CONTENGAS! *GEMIDO* ¡LLÉNAME LOS INTESTINOS! *JADEO*"
        "[sca] tensa sus músculos, sabiendo que así va a llevarte antes al orgasmo. Pero su cuerpo te indica que ella también está muy cerca."
        sca "*GEMIDO* ¡QUIERO QUE ESTA VEZ NOS CORRAMOS A LA VEZ! *GEMIDO*"
        "Va a ser imposible no hacerlo. Vuestros cuerpos quieren tener un orgasmo compartido, y no puedes hacer nada para evitarlo."
        call OrgasmXS3 ("c23s001_170b") from _call_OrgasmXS3_32
        mc "¡Mpfft!"
        "Explotas en el interior del culo de [sca], llenando sus intestinos tal como te ha pedido."
        sca "*JADEO* ¡SÍ! *GEMIDO* ¡ME CORRO! *JADEO* ¡ESTÁ SUPER CALIENTE! *GEMIDO*"
        "Nada más recibir tu leche, el koala experimenta un intenso orgasmo, tensando aún más todos sus músculos para ordeñar hasta la última gota de tu semen."
        scene c23s001_960pv with dissolve
        hide c23s001_950v
        show c23s001_960v
        "Sigues bombeando un rato más, sintiéndote exprimido, ordeñado, atrapado en el culo de [YourSister]. Bendita prisión."
        sca "*GEMIDO* ¡ME ESTÁS CONVIRTIENDO EN UNA PUTILLA ANAL! *GEMIDO*"
        "Te sorprende la expresión saliendo de la boca de la dulce [sca]. Esa frase en sus labios parece fuera de lugar."
        sca "*JADEO* ¡SIGUE! *GEMIDO* ¡NO PUEDO PARAR DE CORRERME! *JADEO*"
        "A veces en los momentos de máximo placer es cuando los filtros desaparecen y salen de nosotros cosas que no nos creemos capaces de decir."
        sca "*GEMIDO* ¡TE QUIERO! *GEMIDO*"
        mc "Yo también te quiero."
        "[sca] tiene un historial de decir cosas que no quería decir en medio de una catarata de orgasmos."
        call BlinkXPS3 ("c23s001_175" , "f") from _call_BlinkXPS3_1044
        "Cuando vuestra resistencia llega a su fin, os tumbáis de nuevo, con [YourSister] reposando sobre tu pecho."
        sca "Ha sido increíble. Me encanta..."
        stop music fadeout (1.5)
        mc "*Risa* Me he dado cuenta, mi pequeña putilla anal. *Risa*"
        play music ("music/ChillUkelele.ogg")
        call BlinkXPS3 ("c23s001_180" , "d") from _call_BlinkXPS3_1045
        sca "¡Oops! Se me ha escapado. No quería sonar soez."
        mc "No pasa nada, cielo, pero no me pidas que te llame eso. *Risa* Como mucho te llamaré Mi Koala Anal."
        mc "*Risa* Aunque tendríamos que dar muchas explicaciones si alguien me oye llamarte así."
        call BlinkXPS3 ("c23s001_190" , "d") from _call_BlinkXPS3_1046
        sca "Me gusta lo de Koala, pero podemos dejar lo de anal aparcado. *Risita* Los koalas son dulces y monos."
    else:
        call BlinkXPS3 ("c23s001_185" , "d") from _call_BlinkXPS3_1047
        sca "Por cierto, ¿vas a seguir llamándome Koala?"
        mc "No me digas que te gusta. *Risa* Vamos a tener que dar explicaciones sobre el mote."
        call BlinkXPS3 ("c23s001_190" , "d") from _call_BlinkXPS3_1048
        sca "Me gusta lo de Koala. *Risita* Los koalas son dulces y monos."
    sca "Siempre y cuando no los veas mojados, claro. *Risa* Entonces dan miedo."
    mc "*Risa* Entonces no te mojaré, pero tampoco te daré de comer después de medianoche."
    call BlinkXPS3 ("c23s001_195" , "d") from _call_BlinkXPS3_1049
    sca "¡Hey! *Risa* ¡He pillado esa referencia! *Risa* Vi esa vieja película cuando era una niña..."
    mc "Yo la vi hace unos meses otra vez. Hicieron un ciclo de películas clásicas en la universidad."
    call BlinkXPS3 ("c23s001_200" , "d") from _call_BlinkXPS3_1050
    sca "Y sobre lo de Koala, no tenemos que dar ninguna explicación. Los motes que nos pongamos son nuestros y ya está."
    if mc._var("relationships")>1:
        sca "Está muy bien que en el harén haya comunicación, pero no tenemos por qué explicarlo todo."
    if sca._var("halfSister"):
        mc "Me parece una idea genial, hermanita. *Risa* Vas a ser mi koala a partir de ahora."
    else:
        mc "Me parece una idea genial, cielo. *Risa* Vas a ser mi koala a partir de ahora."
    call BlinkXPS3 ("c23s001_205" , "d") from _call_BlinkXPS3_1051
    sca "¿Te importa que nos quedemos abrazados un rato antes de ir a la ducha?"
    mc "Por supuesto que no. Adoro abrazarte."
    call BlinkXPS3 ("c23s001_210" , "d") from _call_BlinkXPS3_1052
    sca "Y a mí me encanta que me abraces. Creía que lo mejor de tener novio sería el sexo."
    sca "Pero son los abrazos, los besos, el saber que siempre voy a poder contar contigo..."
    mc "No voy a decir que el sexo esté sobrevalorado, pero no es lo más importante en una relación."
    call BlinkXPS3 ("c23s001_215" , "d") from _call_BlinkXPS3_1053
    sca "Por eso las parejas de viejecitos siguen juntos aunque ya no tengan sexo."
    mc "*Risa* Te sorprendería el sexo que tienen los viejecitos. Leí que las residencias de ancianos son una fuente de ETS. *Risa*"
    call BlinkXPS3 ("c23s001_220" , "d") from _call_BlinkXPS3_1054
    sca "¡No es posible!"
    mc "Sí, lo es. Por lo visto se aburren y follan más de lo que follaban antes de entrar."
    mc "*Risa* Las pastillas azules han hecho maravillas con la vida de los ancianos."
    call BlinkXPS3 ("c23s001_225" , "d") from _call_BlinkXPS3_1055
    sca "Mmmmm... Eso quiere decir que dentro de medio siglo seguiremos haciendo esto, ¿no?"
    mc "*Risa* Sí, pero lo haremos más lento y con menos flexibilidad."
    call BlinkXPS3 ("c23s001_230" , "d") from _call_BlinkXPS3_1056
    sca "Ya sé que he sido yo quién te ha pedido que nos quedemos abrazados, pero me voy a tener que ir a la ducha."
    mc "¿Ya? Ha sido un abrazo muy corto."
    call BlinkXPS3 ("c23s001_235" , "d") from _call_BlinkXPS3_1057
    if sca._var("anal"):
        sca "Me tengo que ir antes de empezar a gotear tu semen por mis dos agujeros."
    else:
        sca "Me tengo que ir antes de empezar a gotear tu semen."
    sca "Voy a poner la cama perdida si me río."
    mc "Da lo mismo. Puedo poner las sábanas a lavar, pero no voy a poder recuperar los abrazos que no te de ahora."
    call BlinkXPS3 ("c23s001_240" , "d") from _call_BlinkXPS3_1058
    sca "Pero me podrás dar más abrazos luego."
    mc "¿Quieres coger mi albornoz?"
    call BlinkXPS3 ("c23s001_245" , "d") from _call_BlinkXPS3_1059
    sca "Sí, gracias. No quiero volver a ponerme el pijama para ir a mi habitación a coger el mío."
    mc "Te espero aquí. Luego me ducharé yo."
    call BlinkXPS3 ("c23s001_250" , "f") from _call_BlinkXPS3_1060
    sca "Te propondría que nos ducháramos juntos, pero..."
    mc "*Risa* Lo sé, consiste en quitarte mi corrida de dentro, no acumular más."
    call BlinkXPS3 ("c23s001_255" , "d") from _call_BlinkXPS3_1061
    sca "*Risa* Exacto."
    call BlinkXPS3 ("c23s001_260" , "h") from _call_BlinkXPS3_1062
    sca "¡Mierda! ¡No me hagas reír o se va a salir todo el semen!"
    scene c23s001_260d with hpunch
    play sound ("music/DoorSlam.ogg")
    "*Blam*"
    "Compruebas el móvil mientras [sca] se ducha y esperas tu turno."
    call BlinkXPS3 ("c23s001_265" , "f") from _call_BlinkXPS3_1063
    "Al cabo de un rato..."
    sca "Ya estoy. Tienes la ducha para ti cuando quieras."
    if sca._var("halfSister"):
        mc "Gracias, hermanita. ¿Necesitas algo más?"
    else:
        mc "Gracias, cielo. ¿Necesitas algo más?"
    call BlinkXPS3 ("c23s001_270" , "d") from _call_BlinkXPS3_1064
    sca "¿Puedes dejarme algo de ropa? No quiero ponerme el pijama usado justo después de salir de la ducha."
    sca "Y volver desnuda a la habitación de [dap.nick] no es una opción. *Risa*"
    mc "*Risa* No lo creo. Puedes coger lo que quieras."
    call BlinkXPS3 ("c23s001_275" , "d") from _call_BlinkXPS3_1065
    sca "¿No te ibas a duchar?"
    mc "¿Y perderme el espectáculo de verte cambiarte? *Risa* ¡Nunca!"
    scene c23s001_280a with dissolve
    sca "No entiendo a qué espectáculo te refieres."
    sca "Tan solo soy una chica quitándose un albornoz."
    mc "Una chica, no. Mi maravilloso koala."
    call BlinkXPS3 ("c23s001_285" , "d") from _call_BlinkXPS3_1066
    sca "Y ahora voy a ver qué ropa le puedo robar a mi novio."
    mc "Es un préstamo, no un robo."
    call BlinkXPS3 ("c23s001_290" , "d") from _call_BlinkXPS3_1067
    sca "Parece mentira que hayas tenido novias antes. *Risa* Si tomamos algo prestado, se convierte en nuestro."
    sca "Voy a tener que hablar con [eil.nick] y con [sai] para echarles la bronca por no haberte educado bien."
    mc "*Risa* A veces las mujeres dais mucho miedo."
    scene c23s001_295a with dissolve
    sca "No entiendo por qué. *Risa* Tenemos que alimentar a nuestros armarios."
    sca "Ya sabes que nunca tenemos suficiente ropa."
    mc "*Risa* Te estás convirtiendo en un cliché."
    scene c23s001_295b with fade
    sca "Creo que esto me queda bien."
    sca "Supongo que te queda mejor a ti, pero no está mal."
    mcp "(Por suerte ha elegido unos boxers que me regaló Jamaal y no me he puesto nunca.)"
    mc "Sabes que una mujer con boxers y camisa de hombre es super sexy, ¿verdad?"
    mc "{b}Solo{/b} con boxers y la camisa."
    call BlinkXPS3 ("c23s001_300" , "d") from _call_BlinkXPS3_1068
    sca "Te oí decírselo a [eil] hace años. Por eso he elegido los boxers."
    sca "Ahora a buscar una camisa que me pueda quedar bien."
    mc "Lástima que no haya ninguna de franela. Suele ser lo que completa el conjunto."
    scene c23s001_295c with dissolve
    sca "Bueno, creo que esta me quedará igual de bien que la de franela."
    sca "Además, no quiero llegar a la habitación de [dap] empapada en sudor. El verano y la franela no se llevan bien."
    mc "Tienes razón. Pero estoy seguro de que cualquier camisa te queda perfecta."
    call BlinkXPS3 ("c23s001_305" , "d") from _call_BlinkXPS3_1069
    sca "¿Qué tal esta?"
    mc "Increíblemente preciosa. Me están entrando ganas de levantarme y quitártela."
    call BlinkXPS3 ("c23s001_310" , "d") from _call_BlinkXPS3_1070
    sca "Por muy tentador que sea, me voy a tener que ir. Tú tienes que ducharte y no quiero entretenerte más."
    mc "Lo entiendo. *Risa* Además, te acabas de duchar y no querrás que te vuelva a hacer sudar, ¿verdad?"
    call BlinkXPS3 ("c23s001_315" , "d") from _call_BlinkXPS3_1071
    sca "*Risa* Por mucho que me mires con ojos de cachorrito, no me vas a convencer para quitarme mi recién adquirida camisa."
    mc "*Risa* Tenía que intentarlo. Un beso al menos sí que tendré, ¿no?"
    sca "Eso sí. Ven aquí, cielo."
    scene c23s001_320a with dissolve
    "Vuestros labios se juntan en una alegre despedida hasta la próxima vez."
    "Sabéis que volveréis a besaros en breve, pero no cuándo podréis volver a dormir juntos."
    call BlinkXPS3 ("c23s001_325" , "d") from _call_BlinkXPS3_1072
    sca "Bueno, me voy ya, o me acusarás de dejarte cachondo cuando me vaya."
    mc "Nunca te acusaré de eso. *Risa* Aunque me dejes cachondo cuando te vayas."
    mc "Puedes decirle a [nor] que me devuelva la camisa y los boxers cuando los laves."
    call BlinkXPS3 ("c23s001_330" , "d") from _call_BlinkXPS3_1073
    sca "¿Qué camisa y qué boxers? ¿Lo que llevo puesto? Esto va directamente a mi armario cuando [nor] lo lave."
    sca "Ella lo entenderá y me apoyará en esto. *Risa* Te puedes despedir de ellos."
    if mc._var("relationships")>1:
        mc "Si algún día tengo un harén de 20 chicas, no voy a ganar para ropa."
        call BlinkXPS3 ("c23s001_335" , "d") from _call_BlinkXPS3_1074
        sca "Y no sólo en ropa que te robemos. *Risa* Vestir a 20 chicas te va a salir caro."
    else:
        mc "Espero que no me robes ropa cada vez que vengas. *Risa* No voy a ganar para ropa si es así."
        call BlinkXPS3 ("c23s001_335" , "d") from _call_BlinkXPS3_1075
    sca "Como soy buena chica y no voy a pedirte que me compres ropa, ese dinero lo puedes usar en ropa para ti que después te robaré. *Risa*"
    mc "*Risa* Eres malvada, pero me gusta la idea. La única condición es que tienes que pasar la noche aquí para robarme ropa."
    scene c23s001_320b with dissolve
    sca "No me tientes. *Risa* No puedo pasar todas las noches aquí, y no hay demasiado espacio en el armario que comparto con [dap]."
    scene c23s001_320c with dissolve
    play sound ("music/DoorSlam.ogg")
    "*Blam*"
    mc "[sca], ¿no te olvidas algo?"
    call KissXPS3 ("c23s001_340" , "d") from _call_KissXPS3_18
    sca "Tienes razón. Hasta luego, cielo."
    if sca._var("halfSister"):
        mc "Hasta luego, hermanita, pero no me refería a eso."
    else:
        mc "Hasta luego, cielo, pero no me refería a eso."
    scene c23s001_340c with dissolve
    sca "¡Ooops!"
    call BlinkXPS3 ("c23s001_345" , "d") from _call_BlinkXPS3_1076
    sca "Menos mal que me lo has dicho. Intentando hacer una salida dramática me he olvidado."
    sca "Lo peor de venir a verte es que duermas aquí arriba."
    call KissXPS3 ("c23s001_350" , "d") from _call_KissXPS3_19
    sca "Ahora sí. Hasta luego, cielo."
    mc "Hasta luego, mi lindo koala."
    scene c23s001_320c with dissolve
    sca "*A través de la puerta* Cada vez me gusta más que me llames así."
    sca "*A través de la puerta* Dile a [mar] que me devuelva el pijama cuando lo eches a lavar."
    mc "¿No me lo puedo quedar?"
    sca "*A través de la puerta* Puedes. *Risa* Pero no te quedaría tan bien como me queda a mí la camisa y los boxers."
    stop music fadeout (1.5)
    "Se oyen sus pasos bajando las escaleras. Ha sido una mañana fantástica."
    return
label c23s001_NoScaSex:
    call c23s001_DayChange from _call_c23s001_DayChange_1
    return
label c23s000_DiscoveredPregnancies:
    $ mc._var("discoveredPregnancies", 0, "set")
    if sai._var("pregnancyDiscovered"):
        $ mc._var("discoveredPregnancies", 1, "add")
    if mar._var("pregnancyDiscovered"):
        $ mc._var("discoveredPregnancies", 1, "add")
    if eri._var("pregnancyDiscovered"):
        $ mc._var("discoveredPregnancies", 1, "add")
    if dap._var("pregnancyDiscovered"):
        $ mc._var("discoveredPregnancies", 1, "add")
    if sca._var("pregnancyDiscovered"):
        $ mc._var("discoveredPregnancies", 1, "add")
    if nor._var("pregnancyDiscovered"):
        $ mc._var("discoveredPregnancies", 1, "add")
    if eil._var("pregnancyDiscovered"):
        $ mc._var("discoveredPregnancies", 1, "add")
    if sam._var("pregnancyDiscovered"):
        $ mc._var("discoveredPregnancies", 1, "add")
    if sim._var("pregnancyDiscovered"):
        $ mc._var("discoveredPregnancies", 1, "add")
    if oma._var("pregnancyDiscovered"):
        $ mc._var("discoveredPregnancies", 1, "add")
    if meg._var("pregnancyDiscovered"):
        $ mc._var("discoveredPregnancies", 1, "add")
    return
label c23s002_SaiPregnancy:
    if _in_replay:
        call mrS3_sai_route from _call_mrS3_sai_route_4
        if sai._var("route"):
            call mrS3_sai_pregnant from _call_mrS3_sai_pregnant
        call mrS3_sca_route from _call_mrS3_sca_route_3
    scene c23s002_005a with fade
    play music ("music/Embrace.ogg")
    "Bajas a desayunar y, por una vez, no hay nadie en la cocina."
    "Preparas un café y coges un trozo pequeño de pastel."
    call BlinkXPS3 ("c23s002_010" , "d") from _call_BlinkXPS3_1077
    "A los pocos minutos aparece [sai]."
    sai "Hola, [mc]. Qué raro ver la cocina tan vacía."
    if sai._var("route"):
        call KissXPS3 ("c23s002_015" , "d") from _call_KissXPS3_20
        mc "Hola, cielo."
    mc "Creo que todo el mundo está haciendo yoga ahora mismo o preparándose para ir a clase."
    call BlinkXPS3 ("c23s002_020" , "d") from _call_BlinkXPS3_1078
    sai "Tienes razón. Hoy es más tarde que ayer. No tengo clase esta mañana."
    sai "Tan solo tengo que acabar un estudio sobre Maria Montessori."
    mc "No tengo ni idea de quién es."
    if not sai._var("route"):
        call c23s002_Montessori from _call_c23s002_Montessori
        "Para cuando acaba, tú has terminado tu trozo de pastel, quizás demasiado pequeño, y subes a tu habitación."
        call c23s002_ScaYoga from _call_c23s002_ScaYoga
    else:
        call BlinkXPS3 ("c23s002_025" , "d") from _call_BlinkXPS3_1079
        sai "Era una profesora italiana que..."
        call c23s002_Montessori from _call_c23s002_Montessori_1
        call BlinkXPS3 ("c23s002_030" , "d") from _call_BlinkXPS3_1080
        mc "Parece interesante."
        sai "Lo es. Pero ¿sabes qué sería interesante también?"
        mc "*Risa* Muchas cosas. Es una pregunta imposible de acertar."
        call BlinkXPS3 ("c23s002_035" , "d") from _call_BlinkXPS3_1081
        sai "Tienes razón. *Risa* Sin saber en lo que estoy pensando es imposible que lo aciertes."
        mc "Dame alguna pista..."
        call BlinkXPS3 ("c23s002_040" , "d") from _call_BlinkXPS3_1082
        sai "Hablando de Montessori he empezado a pensar en niños..."
        mc "Y quieres saber el resultado de la prueba de embarazo."
        call BlinkXPS3 ("c23s002_045" , "d") from _call_BlinkXPS3_1083
        sai "Me conoces demasiado. ¿Te importa si subimos ya? Puedo desayunar más tarde."
        mc "Si, por mí perfecto. Cuanto antes lo sepamos, mejor. Vamos."
        call c23s002_ScaYoga from _call_c23s002_ScaYoga_1
        call BlinkXPS3 ("c23s002_070" , "d") from _call_BlinkXPS3_1084
        sai "*Risa* Pobre [sca]. Con lo poco que le gusta el deporte, y ha tenido que subir hasta la azotea para nada."
        mc "*Risa* Y ahora bajar corriendo a la piscina. Va a llegar agotada."
        call BlinkXPS3 ("c23s002_075" , "d") from _call_BlinkXPS3_1085
        sai "¿Continuamos a tu habitación?"
        mc "Vamos."
        call BlinkXPS3 ("c23s002_080" , "f") from _call_BlinkXPS3_1086
        mc "Lo puedes coger tú misma si quieres. Está en el armario."
        sai "Mejor míralo tú primero. Estoy un poco nerviosa."
        mc "¿Te da miedo estar embarazada?"
        call BlinkXPS3 ("c23s002_085" , "d") from _call_BlinkXPS3_1087
        sai "Por un lado no. Quiero tener un par de críos correteando por casa lo antes posible. Me da lo mismo si son niños o niñas."
        sai "Por otro lado... creo que es demasiado pronto... aún no he acabado la carrera y nunca me había planteado tener hijos tan joven..."
        mc "Bueno, si estás embarazada, no hay mucho que podamos hacer, pero si no lo estás, si quieres puedes volver a tomar anticonceptivos."
        mc "Tenemos mucho tiempo para tener ese par de niños."
        call BlinkXPS3 ("c23s002_090" , "d") from _call_BlinkXPS3_1088
        sai "No pienso tomar anticonceptivos. Cuando el destino decida que tienen que llegar, llegarán."
        sai "Y míralo ya antes de que me ponga más nerviosa."
        if sai._var("pregnant"):
            $ sai._var("pregnancyDiscovered" , True)
            call c23s000_DiscoveredPregnancies from _call_c23s000_DiscoveredPregnancies_1
            call c23s002_SaiPregnant from _call_c23s002_SaiPregnant
        else:
            call c23s000_DiscoveredPregnancies from _call_c23s000_DiscoveredPregnancies_2
            call c23s002_SaiNotPregnant from _call_c23s002_SaiNotPregnant
    return
label c23s002_ScaYoga:
    scene c23s002_050d with fade:
        yalign 1.0
        linear 5.0 yalign 0.0
    pause (5.0)
    call BlinkXPS3 ("c23s002_050" , "d") from _call_BlinkXPS3_1089
    call addProfileImageS3 (3, "scarlett_3", sca, _(": 15 - Especial"), "") from _call_addProfileImageS3_2
    "Al salir al comedor te encuentras con [sca] con pinta de estar perdida."
    mc "¿Buscas algo, [sca]?"
    sca "Creo que he llegado tarde a la sesión de yoga."
    call BlinkXPS3 ("c23s002_055" , "d") from _call_BlinkXPS3_1090
    mc "¿Has decidido apuntarte? Eso es nuevo."
    sca "Bueno, después de lo de ayer, quiero hacer aún más cosas con las chicas."
    sca "Pero acabo de ir a la terraza y parece que ya han acabado."
    mc "Oh, ¿nadie te ha dicho que han movido las sesiones de yoga a la piscina?"
    call BlinkXPS3 ("c23s002_060" , "d") from _call_BlinkXPS3_1091
    sca "¿Qué? ¡No! Nadie me lo había dicho."
    sca "¡Me voy antes de que acaben!"
    scene c23s002_065aAn
    mc "Hasta luego, [sca]."
    if sai._var("route"):
        sai "Adiós, [sca]."
    sca "Hasta luego..."
    if sca._var("route"):
        scene c23s002_065bAn
        sca "Ahora sí. Hasta luego."
    return
label c23s002_Montessori:
    scene c23s002_025An
    "[sai] pasa los siguientes minutos explicándote la biografía de la pedagoga. Por lo visto hizo cosas revolucionarias para su época."
    "Pero es una historia en la que se entrevén muchos grises."
    return
label c23s002_SaiPregnant:
    call BlinkXPS3 ("c23s002_095" , "f") from _call_BlinkXPS3_1092
    mc "¡Verde. Vamos a tener un bebé!"
    call BlinkXPS3 ("c23s002_100" , "v") from _call_BlinkXPS3_1093
    sai "Felicidades, cielo. Sé que te hacía ilusión."
    mc "No suenas muy contenta."
    call BlinkXPS3 ("c23s002_105" , "d") from _call_BlinkXPS3_1094
    sai "Estoy contenta, pero preocupada."
    mc "¿Por la carrera? Te ayudaremos en todo lo que podamos."
    call BlinkXPS3 ("c23s002_110" , "d") from _call_BlinkXPS3_1095
    sai "No, la carrera no me preocupa demasiado. Me parece raro tener un bebé antes de acabarla, pero ya está."
    sai "Me preocupa decírselo a mis padres."
    mc "¿Cómo se lo van a tomar?"
    call c23s002_parents from _call_c23s002_parents
    mc "Bueno, si quieres que esté ahí para decírselo, cuenta conmigo..."
    call BlinkXPS3 ("c23s002_125" , "d") from _call_BlinkXPS3_1096
    sai "No te preocupes. No se lo voy a decir todavía."
    mc "¿Por qué? ¿Cuánto quieres esperar?"
    call BlinkXPS3 ("c23s002_130" , "d") from _call_BlinkXPS3_1097
    sai "Como mínimo, hasta que Kaly esté aquí. Si les digo que me he quedado embarazada del dueño de la residencia, no le van a dejar venir."
    sai "Van a pensar que la vas a dejar embarazada en cuanto llegue..."
    if mc._var("discoveredPregnancies")>1:
        sai "Y eso que tu fama de embarazador no ha llegado aún hasta India."
    mc "No tengo intención de tener nada con Kalyani, [sai]."
    call BlinkXPS3 ("c23s002_135" , "d") from _call_BlinkXPS3_1098
    sai "*Risa* En cuanto veas esos grandes ojos parpadeando en tu cara, me lo confirmas."
    mc "Bueno, pero aparte de lo de tus padres, ¿cómo estás tú?"
    call BlinkXPS3 ("c23s002_140" , "d") from _call_BlinkXPS3_1099
    sai "Ya te digo que estoy contenta, aunque..."
    mc "¿Qué pasa?"
    call BlinkXPS3 ("c23s002_145" , "d") from _call_BlinkXPS3_1100
    sai "No voy a poder volverme a poner este top en cuanto éstas empiecen a crecer. Voy a tener que cambiar el vestuario."
    mc "*Risa* Vas a estar guapísima lleves lo que lleves."
    call BlinkXPS3 ("c23s002_155" , "d") from _call_BlinkXPS3_1101
    sai "No es cómo esperaba que pasara, pero estoy más contenta de lo que parezco. Tan solo me siento rara de tener que ocultárselo a mis padres."
    mc "No se lo ocultas, retrasas la noticia tan solo."
    call BlinkXPS3 ("c23s002_150" , "d") from _call_BlinkXPS3_1102
    sai "¡Vamos a la piscina! Quiero darles la noticia al resto de las chicas. Después lo publicaré en el grupo de WhatsUp."
    mc "¿En el que estoy yo o en el que no estoy?"
    call BlinkXPS3 ("c23s002_160" , "d") from _call_BlinkXPS3_1103
    sai "En los dos. En el tuyo no contestará casi nadie, pero lo publicaré por si alguien quiere felicitarte a ti."
    mc "*Risa* A veces os odio. Vamos."
    return
label c23s002_parents:
    call BlinkXPS3 ("c23s002_115" , "d") from _call_BlinkXPS3_1104
    sai "Imagínate enviar a tu hija al extranjero a estudiar y que antes de que acabe la carrera se quede embarazada."
    sai "Y del dueño de la residencia de estudiantes nada menos... Y sin estar casados..."
    mc "Me lo puedo imaginar. Ya me dijiste que eran muy tradicionales."
    call BlinkXPS3 ("c23s002_120" , "d") from _call_BlinkXPS3_1105
    sai "*Risa triste* ¿Tradicionales? Une a eso retrógrados y te acercarás a una versión modernizada de mis padres."
    sai "A veces parece que vivan en el Siglo XIX o el XX."
    return
label c23s002_SaiNotPregnant:
    call BlinkXPS3 ("c23s002_095" , "f") from _call_BlinkXPS3_1106
    mc "Rojo. No vamos a tener un bebé aún."
    call BlinkXPS3 ("c23s002_100" , "v") from _call_BlinkXPS3_1107
    sai "Bueno, otra vez será. No tenemos prisa."
    mc "No suenas muy decepcionada. Eso es bueno."
    call BlinkXPS3 ("c23s002_105" , "d") from _call_BlinkXPS3_1108
    sai "Estoy decepcionada, pero, por otro lado, estoy aliviada."
    mc "¿Por la carrera? Te ayudaremos en todo lo que podamos."
    call BlinkXPS3 ("c23s002_110" , "d") from _call_BlinkXPS3_1109
    sai "No, la carrera no me preocupa demasiado. Me hubiera parecido raro tener un bebé antes de acabarla, pero ya está."
    sai "Me preocupaba decírselo a mis padres."
    mc "¿Cómo se lo iban a tomar?"
    call c23s002_parents from _call_c23s002_parents_1
    mc "Bueno, si, cuando te quedes embarazada, quieres que esté ahí para decírselo, cuenta conmigo..."
    call BlinkXPS3 ("c23s002_125" , "d") from _call_BlinkXPS3_1110
    sai "No te preocupes. No se lo pensaba decir aunque me hubiera quedado embarazada ahora."
    mc "¿Por qué? ¿Cuánto hubieras querido esperar?"
    call BlinkXPS3 ("c23s002_130" , "d") from _call_BlinkXPS3_1111
    sai "Como mínimo, hasta que Kaly esté aquí. Si les hubiera dicho que me he quedado embarazada del dueño de la residencia, no le iban a dejar venir."
    sai "Iban a pensar que la ibas a dejar embarazada en cuanto llegara..."
    if mc._var("discoveredPregnancies")>1:
        sai "Y eso que tu fama de embarazador no ha llegado aún hasta India."
    mc "No tengo intención de tener nada con Kalyani, [sai]."
    call BlinkXPS3 ("c23s002_135" , "d") from _call_BlinkXPS3_1112
    sai "*Risa* En cuanto veas esos grandes ojos parpadeando en tu cara, me lo confirmas."
    mc "*Risa* No me tientes, sabes que unos ojos bonitos son mi perdición."
    mc "Pero volviendo a tus padres, la parte buena es que no tienes que ocultarles nada."
    call BlinkXPS3 ("c23s002_140" , "d") from _call_BlinkXPS3_1113
    sai "Sí, y al menos no tendré que cambiar de vestuario."
    mc "¿Por qué?"
    call BlinkXPS3 ("c23s002_145" , "d") from _call_BlinkXPS3_1114
    sai "Si me hubiera quedado embarazada no hubiera podido volver a ponerme este top en cuanto éstas empezaran a crecer."
    mc "*Risa* Ibas a estar guapísima llevaras lo que llevaras."
    call BlinkXPS3 ("c23s002_150" , "d") from _call_BlinkXPS3_1115
    sai "Voy a ir a la piscina a decirle a [mar] y a [emm] que el test ha salido negativo."
    mc "¿Quieres que te acompañe?"
    call BlinkXPS3 ("c23s002_160" , "d") from _call_BlinkXPS3_1116
    sai "No hace falta. Me van a querer dar abrazos para consolarme, aunque no sean necesarios. *Risa* Quiero esos abrazos solo para mí."
    mc "*Risa* A veces os odio. Te veo luego."
    return
label c23s002_Lugagge:
    if _in_replay:
        call mrS3_mar_route from _call_mrS3_mar_route_3
        call mrS3_emm_route from _call_mrS3_emm_route_4

    scene black with dissolve
    stop music fadeout (1.5)
    if sai._var("route") and not sai._var("pregnant"):
        "Vas al lavabo y vuelves a tu habitación a meter una muda de ropa en una mochila para el viaje de mañana."
    elif sai._var("pregnant"):
        "Después de pasar por la piscina, vuelves a tu habitación a meter una muda de ropa en una mochila para el viaje de mañana."
    else:
        "Vuelves a tu habitación a meter una muda de ropa en una mochila para el viaje de mañana."
    "Cuando casi has acabado..."
    scene c21s001_020b with dissolve
    play sound ("music/knock.ogg")
    "*Knock-Knock*"
    play music ("music/Emotional-Piano-Sad.ogg")
    mom "*A través de la puerta* Soy yo. ¿Puedo pasar?"
    mc "Sí, pasa."
    if mar._var("route"):
        call KissXPS3 ("c23s002_165a" , "d") from _call_KissXPS3_21
    else:
        call BlinkXPS3 ("c23s002_165b" , "d") from _call_BlinkXPS3_1117
    mom "Venía a ver si querías que te ayudara a hacer la maleta para mañana."
    mc "*Risa* ¿Maleta? Con una mochila tengo suficiente. Una muda de ropa y artículos de higiene."
    call BlinkXPS3 ("c23s002_170" , "d") from _call_BlinkXPS3_1118
    mom "¿Sólo eso?"
    mc "No necesito más. Es solo una noche."
    mom "¿Y si llueve? ¿O si hace frío? Deberías coger una chaqueta."
    if persistent.family:
        $ Mom = __("Mamá")
    else:
        $ Mom = mar.name
    mc "[Mom], he mirado las temperaturas en el móvil, y se espera que haga buen día."
    call BlinkXPS3 ("c23s002_175" , "d") from _call_BlinkXPS3_1119
    mom "Nunca te puedes fiar de esas aplicaciones, cielo. Acuérdate de cuando fuimos a Fresno. La app decía que iba a hacer sol y llovió."
    mc "De eso hace casi diez años, [Mom]. Las aplicaciones son mucho más fiables ahora."
    call BlinkXPS3 ("c23s002_180" , "d") from _call_BlinkXPS3_1120
    mom "Bueno, pero llévate una chaqueta por lo que pueda ser. ¿Qué camisas te vas a llevar?"
    mc "Una camiseta. Nada de camisas. Van a llegar arrugadas."
    call BlinkXPS3 ("c23s002_185" , "d") from _call_BlinkXPS3_1121
    mom "Deberías llevarte la camisa azul. Tienes que ir bien vestido si vas a reunirte con el obispo, y esa camisa te queda muy bien."
    mc "*Risa* No soy yo quien se reúne con el obispo, es Tía [bet]. Por una vez sólo hago de chófer, no tengo que resolver nada."
    mc "Y la reunión ni siquiera es con el obispo, es con un secretario."
    call BlinkXPS3 ("c23s002_190" , "d") from _call_BlinkXPS3_1122
    mom "Pero la acompañarás, ¿verdad? Está muy nerviosa."
    mc "No creo que quiera que la acompañe a la reunión. La llevaré a las oficinas de la diócesis, pero no creo que entrar con ella sea lo mejor."
    mc "De todas formas, le preguntaré, pero dudo que quiera que esté en esa reunión."
    call BlinkXPS3 ("c23s002_195" , "d") from _call_BlinkXPS3_1123
    mom "Bueno, pues mete la camisa azul por si acaso la tienes que acompañar."
    mom "Siempre tienes que llevar algo de ropa correcta por si surge un imprevisto."
    mc "La eché a lavar ayer o anteayer. No la he visto en el armario."
    call BlinkXPS3 ("c23s002_200" , "d") from _call_BlinkXPS3_1124
    mom "Tienes razón, creo que la lavé ayer. Tengo que plancharla."
    mc "No te molestes, [Mom], con una camiseta también voy bien. Además, se va a arrugar en la mochila."
    call BlinkXPS3 ("c23s002_215" , "d") from _call_BlinkXPS3_1125
    mom "No te preocupes. La meteré en una de las maletas de [emm]. Luego le tengo que ayudar a hacerlas."
    mc "Espera. ¿Has dicho una de las maletas? ¿Cuántas lleva?"
    call BlinkXPS3 ("c23s002_210" , "d") from _call_BlinkXPS3_1126
    mom "La he visto subir con dos maletas del sótano."
    mc "¿Para una noche?"
    call BlinkXPS3 ("c23s002_205" , "d") from _call_BlinkXPS3_1127
    mom "Es [emm]..."
    stop music fadeout (1.5)
    scene c21s001_020b with dissolve
    play sound ("music/knock.ogg")
    "*Knock-Knock*"
    emm "*A través de la puerta* Soy yo. ¿Puedo pasar?"
    play music ("music/MorningFunnyBeat.ogg")
    mc "Sí, pasa."
    call BlinkXPS3 ("c23s002_220" , "d") from _call_BlinkXPS3_1128
    emm "Mamá, ¿crees que esto será suficiente para mañana?"
    mc "¿Dónde crees que vas con eso, [emm]?"
    call BlinkXPS3 ("c23s002_225" , "d") from _call_BlinkXPS3_1129
    emm "Vamos al norte. Hará más frío que aquí, y ya sabes que yo tengo frío en seguida..."
    mc "Vamos 200 Km al norte. No nos vamos a Alaska..."
    call BlinkXPS3 ("c23s002_230" , "d") from _call_BlinkXPS3_1130
    mom "Te he dicho una chaqueta, [emm], no que te vistas de invierno."
    call BlinkXPS3 ("c23s002_235" , "d") from _call_BlinkXPS3_1131
    emm "Pero el Ferrarini será descapotable y hará frío..."
    mc "No, [emm], el coche no es descapotable. Además, ¿crees que vas a poder conducir con eso puesto?"
    call BlinkXPS3 ("c23s002_240" , "d") from _call_BlinkXPS3_1132
    emm "Tienes razón. Sería muy incómodo."
    emm "Mamá, ¿me ayudas a escoger una chaqueta adecuada?"
    call BlinkXPS3 ("c23s002_245" , "d") from _call_BlinkXPS3_1133
    mom "Sí, te acompaño. Después tengo que ir a planchar. Deja un hueco en una de tus maletas para una camisa de [mc]."
    if mar._var("route"):
        call KissXPS3 ("c23s002_255a" , "d") from _call_KissXPS3_22
    else:
        call BlinkXPS3 ("c23s002_255b" , "d") from _call_BlinkXPS3_1134
    mom "Hasta luego, [mc]."
    if emm._var("route"):
        call KissXPS3 ("c23s002_250a" , "d") from _call_KissXPS3_23
    else:
        call BlinkXPS3 ("c23s002_250b" , "d") from _call_BlinkXPS3_1135
    emm "Te vemos luego. Voy a tener que añadir otra maleta por lo de tu camisa."
    scene c21s001_020b with fade
    mcp "(¿Otra maleta por una camisa? Creo que es una excusa para poder llevarse más ropa.)"
    stop music fadeout (1.5)
    mcp "(No me extrañaría que se llevara un traje de buzo por si hay una inundación. Mujeres...)"
    return
label c23s002_NoPatty:
    if _in_replay:
        call mrS3_nor_route from _call_mrS3_nor_route_2
        call mrS3_rels from _call_mrS3_rels_5
        call mrS3_sai_route from _call_mrS3_sai_route_5
        call mrS3_deb_route from _call_mrS3_deb_route_4
        call mrS3_lis_route from _call_mrS3_lis_route_1
    scene black with dissolve
    "Cuando acabas de preparar la mochila, trabajas un rato en la contabilidad del dormitorio y después bajas a la cocina a comer algo."
    play music ("music/Majestica.ogg")
    "El trozo de pastel era demasiado pequeño."
    call BlinkXPS3 ("c23s002_300" , "d") from _call_BlinkXPS3_1136
    "[nor] aparece al cabo de unos minutos."
    nor "Hola, [mc]. ¿No está [mar]?"
    if persistent.family:
        $ Aunt = __("Tía ")
    else:
        $ Aunt = ""
    if nor._var("route"):
        call KissXPS3 ("c23s002_305" , "d") from _call_KissXPS3_24
        mc "Hola, cielo."
    else:
        mc "Hola, [Aunt!t][nor]."
    mc "Si no está en la habitación de [emm], está en el sótano, planchando. Se ha empeñado en que me lleve la camisa azul mañana a Monterey."
    mc "Ni que me fuera una semana. Si por ella fuera, me tendría que llevar tres maletas para pasar una noche fuera."
    call BlinkXPS3 ("c23s002_310" , "d") from _call_BlinkXPS3_1137
    nor "Es que esa camisa te queda muy bien. Y nunca lo entenderás."
    nor "Las mujeres nos solemos llevar mucha ropa a cualquier sitio. *Risa* Casi puedo apostar a que [emm] va a llevar tres maletas."
    mc "*Risa* ¿Sólo tres? Ha dicho que iba a añadir otra maleta porque tenía que meter mi camisa."
    mc "No me extrañaría que cogiera una cuarta maleta para meter el secador y los artículos de higiene."
    mc "Pero, ¿necesitabas algo? ¿Te puedo ayudar yo?"
    call BlinkXPS3 ("c23s002_315" , "d") from _call_BlinkXPS3_1138
    nor "No, no es nada importante. Me han escrito de la universidad diciendo que hay un cambio en las chicas que tenían que alojarse en mi casa."
    nor "Por lo visto, una de las chicas ha sido aceptada en otra universidad y no vendrá. Me han mandado la información de la chica que la sustituye."
    call BlinkXPS3 ("c23s002_320" , "d") from _call_BlinkXPS3_1139
    nor "[mar] se ocupa de enviarles la documentación a las chicas nuevas. Era sólo para darle los datos."
    mc "Dámelos y se lo dejo en su habitación, si quieres."
    call BlinkXPS3 ("c23s002_325" , "d") from _call_BlinkXPS3_1140
    nor "*Risa* ¿Quieres cotillear el expediente de la chica nueva? En la foto parece muy mona."
    if mc._var("relationships")>1:
        nor "*Risa* Podrías meterla en el harén."
        if sai._var("route") and deb._var("route") and lis._var("route"):
            nor "Después de meter a [sai], [deb.nick], y [lis]..."
        elif sai._var("route") and deb._var("route"):
            nor "Después de meter a [sai] y a [deb.nick]..."
        elif sai._var("route") and lis._var("route"):
            nor "Después de meter a [sai] y a [lis]..."
        elif deb._var("route") and lis._var("route"):
            nor "Después de meter a [deb.nick], y a [lis]..."
        elif sai._var("route"):
            nor "Después de meter a [sai]..."
        elif deb._var("route"):
            nor "Después de meter a [deb.nick]..."
        elif lis._var("route"):
            nor "Después de meter a [lis]..."
        mc "*Risa* Aún no ha llegado y ya estás pensando que quiero que entre en el harén."
    elif mc._var("relationships")==1:
        if nor._var("route"):
            nor "*Risa* ¿Me tengo que preocupar? Aunque ya sabes que nuestra relación empezó como no exclusiva..."
            mc "No, cielo. No te tienes que preocupar por nada. ¿Aún no ha llegado y ya le tienes miedo? ¿Qué hablamos ayer?"
            mc "Si estoy contigo es porque quiero estar contigo. No importaría que Charlotte Theron apareciera en la puerta de casa."
            call BlinkXPS3 ("c23s002_330" , "d") from _call_BlinkXPS3_1141
            nor "Lo estaba diciendo en broma, [mc]. Confío en ti."
            if nor._var("discoveredPregnancy"):
                nor "Y nuestro bebé también."
        else:
            nor "*Risa* ¿[gf] tiene que preocuparse?"
            mc "No, que va."
    mc "Por cierto, ¿lo llevas en papel? ¿No sería más cómodo enviárselo por email?"
    call BlinkXPS3 ("c23s002_335" , "d") from _call_BlinkXPS3_1142
    if persistent.family:
        $ YourMom = __("tu madre")
    else:
        $ YourMom = mar.name
    nor "*Risa* Parece que no conozcas a [YourMom]. Ella lo quiere todo en papel para poder archivarlo."
    nor "O esa es su excusa. *Risa* Creo que se hace un lío cambiando de ventanas para coger los datos."
    mc "*Risa* No me sorprendería. Nunca se le han dado demasiado bien los ordenadores."
    call BlinkXPS3 ("c23s002_340" , "d") from _call_BlinkXPS3_1143
    nor "*Risa* Bueno, tú tampoco eres [jam]."
    mc "*Risa* No, pero soy más guapo."
    nor "*Risa* En eso tengo que darte la razón."
    call BlinkXPS3 ("c23s002_345" , "d") from _call_BlinkXPS3_1144
    nor "Bueno, te dejo el expediente aquí y me vuelvo a casa. Tengo que hacer un pedido de papel higiénico."
    nor "Nunca pensé que ser 15 mujeres en casa y recibir visitas de varias más pudiera agotar el papel tan rápido."
    mc "*Risa* ¡Sois todas una panda de meonas!"
    call BlinkXPS3 ("c23s002_350" , "d") from _call_BlinkXPS3_1145
    nor "Un poco..."
    call c23s000_DiscoveredPregnancies from _call_c23s000_DiscoveredPregnancies_3
    if mc._var("discoveredPregnancies")>1:
        nor "Y espera que se empiecen a desarrollar los embarazos."
    elif mc._var("discoveredPregnancies")==1:
        nor "Y espera que se empiecen a desarrollar el embarazo."
    if nor._var("route"):
        call KissXPS3 ("c23s002_305" , "d") from _call_KissXPS3_25
    nor "Bueno, hasta luego, que si no, no voy a hacer ese pedido."
    mc "Hasta luego, [nor]."
    scene c23s002_350d with dissolve
    mcp "(Ahora tengo curiosidad por saber cómo es, después de que [nor] dijera que era mona.)"
    mcp "(¿Qué hago?)"
    if persistent.walkthrough:
        $ wt1 = _("Posibilidad de renombrar a una de las chicas del segundo lote.")
        $ wt2 = _("Se quedará el nombre por defecto (Charlotte).")
    else:
        $ wt1 = ""
        $ wt2 = ""
    menu:
        "Mirar la foto del expediente." (wt=wt1):
            scene c23s002_350e with dissolve
            mcp "(Sí, es mona. Un poco aniñada, pero mona.)"
            mcp "(¿Qué pone aquí? [nor] seguro que no ha esperado a que la tinta se secara. Hace años que le dije que comprara una impresora láser.)"
            if not _in_replay:
                $ pat.name.first_name = renpy.input (_("¿Qué nombre pone en el borrón de tinta?"), default = "Charlotte")
                $ pat.nick = renpy.input (_("El apodo también está emborronado ¿Qué crees que pone?"), default = "Charlie")
            call BlinkXPS3 ("c23s002_355" , "h") from _call_BlinkXPS3_1146
            "La puerta se abre de golpe a tu espalda."
            nor "*Risa* Sabía que no podrías resistirte a mirarlo en el momento en que te he dicho que era mona."
            nor "Me voy a hacer ese pedido y a acabar de secarme el pelo. Recuerda dejárselo a [mar] en su habitación."
            scene c23s002_355d with dissolve
            mcp "(Me conoce demasiado. *Risa mental*)"
            $ mc._var("lookedCharlotte", True)
        "No mirar la foto del expediente." (wt=wt2):
            mcp "(No tengo interés de momento. Si no he mirado los expedientes de las otras chicas...)"
            $ mc._var("lookedCharlotte", False)
    scene black with dissolve
    stop music fadeout (1.5)
    if mc._var("lookedCharlotte"):
        "Dejas el expediente de [pat] en la habitación de [mar] y vuelves a tu habitación."
    else:
        "Dejas el expediente de la chica nueva en la habitación de [mar] y vuelves a tu habitación."
    return
label c23s003_Eil:
    if _in_replay:
        call mrS3_eil_route from _call_mrS3_eil_route_1
        if eil._var("route"):
            call mrS3_eil_pregnant from _call_mrS3_eil_pregnant
            call mrS3_oma_route from _call_mrS3_oma_route_1
            if not oma._var("route"):
                $ sam._var("naturalPubicHair", False)
                call mrS3_sam_route from _call_mrS3_sam_route_3
                if sam._var("route"):
                    call mrS3_sam_blackPanther from _call_mrS3_sam_blackPanther_1
                else:
                    call mrS3_deb_route from _call_mrS3_deb_route_5
                    if not deb._var("route"):
                        call mrS3_mad_route from _call_mrS3_mad_route_1
        call mrS3_kia_route from _call_mrS3_kia_route_1
        call mrS3_rels from _call_mrS3_rels_6
    scene c21s001_020b with dissolve
    "Alguien llama a tu puerta a los pocos minutos."
    play sound ("music/knock.ogg")
    "*Knock-Knock*"
    play music ("music/Memories-Instrumental.ogg")
    eil "*A través de la puerta* ¿Estás ahí? ¿Puedo pasar?"
    mc "Sí, [eil], pasa."
    scene c23s003_005d with fade:
        yalign 1.0
        linear 5.0 yalign 0.0
    pause (5.0)
    call BlinkXPS3("c23s003_005" , "d") from _call_BlinkXPS3_1147
    eil "¡Mira lo que he encontrado!"
    call addProfileImageS3 (5, "eileen_5", eil, _(": 15 - Especial"), "") from _call_addProfileImageS3_3
    mc "¡Ostias! ¡Tu uniforme de animadora!"
    if eil._var("route"):
        call KissXPS3("c23s003_010" , "d") from _call_KissXPS3_26
    eil "Creía que se había quedado en casa. Pero lo había cogido mi madre."
    mc "Cada vez adoro más a [kia]. *Risa* Te sigue quedando muy bien."
    call BlinkXPS3("c23s003_015" , "d") from _call_BlinkXPS3_1148
    eil "*Risa* ¿Estás insinuando que me he engordado en estos años?"
    eil "Por eso creías que me quedaría mal, ¿no?"
    mc "[eil], sabes que eso no funciona conmigo. *Risa* No me quieras hacer sentir culpable por algo que no he dicho."
    call BlinkXPS3("c23s003_020" , "d") from _call_BlinkXPS3_1149
    eil "*Risa* Ayer le funcionó a [kat] con lo de las belugas."
    mc "Eso es diferente. A veces no sé cómo tratarla. No sé si se va a ofender por algo."
    call BlinkXPS3("c23s003_025" , "d") from _call_BlinkXPS3_1150
    eil "Trátala como nos tratas a cualquiera de nosotras."
    if mc._var("relationships") > 1:
        call BlinkXPS3("c23s003_030" , "d") from _call_BlinkXPS3_1151
        eil "Y no me refiero a que te acuestes con ella. *Risa*"
    mc "Es difícil. Es totalmente diferente al resto. Se parece más a Jamaal que a vosotras."
    call BlinkXPS3("c23s003_035" , "d") from _call_BlinkXPS3_1152
    eil "Pues trátala cómo tratarías a Jamaal. Ríete de ella por cosas por las que no se va a ofender."
    eil "Por lo que he visto, vas con pies de plomo alrededor de ella. Id a tomaros una cerveza o invítala a comer."
    mc "Es buena idea. Un día, cuando vuelva de Monterey, lo haré."
    if kia._var("route"):
        call BlinkXPS3("c23s003_040" , "d") from _call_BlinkXPS3_1153
        eil "Hablando de invitar a comer..."
        mc "¿Me vas a preguntar por la comida con tu madre?"
        mc "Sabes que no voy a explicarte nada. Lo que pase entre nosotros se queda entre nosotros."
        mc "Al menos por mi parte."
        call BlinkXPS3("c23s003_045" , "d") from _call_BlinkXPS3_1154
        eil "*Risa* No, no te iba a preguntar por la comida. Ya me lo ha explicado ella."
        mc "Por eso decía lo de que al menos por mi parte se quedaría entre nosotros."
        mc "*Risa* Sabía que le ibas a preguntar."
        call BlinkXPS3("c23s003_050" , "d") from _call_BlinkXPS3_1155
        eil "¿Tú no lo hubieras hecho en mi lugar?"
        mc "Por supuesto. Tú quizás seas la persona que mejor me conoces en una relación y sabes que no te iba a explicar nada, con lo que tenías que preguntarle a ella."
        mc "Entre vosotras es diferente. Sois amigas aparte de madre e hija y tiene lógica que te lo explique."
        call BlinkXPS3("c23s003_055" , "d") from _call_BlinkXPS3_1156
        eil "Fue muy bonito lo que hiciste con el bolso. Mi madre se emocionó mientras me lo explicaba."
        eil "Si le quedaba alguna duda de lo diferente que eres de mi padre, en ese momento se disipó."
        mc "Si le quedaba alguna duda de que fuera diferente que tu padre, significa que estoy haciendo algo mal."
        call BlinkXPS3("c23s003_060" , "d") from _call_BlinkXPS3_1157
        eil "¡No! No me refiero a que la tuviera. Era una forma de hablar."
        eil "Si hubiera pensado que te pareces lo más mínimo a él, no hubiera aceptado tu invitación a comer."
        eil "Ni te hubiera besado el domingo."
        mc "Me tranquiliza escuchar eso. Por un momento había creído que [kia] pensaba que todos los hombres nos parecemos y la vamos a tratar como tu padre."
        call BlinkXPS3("c23s003_065" , "d") from _call_BlinkXPS3_1158
        eil "No le preocupa como sean el resto de los hombres. Sabe que tú eres tan diferente a mi padre como pueden serlo la noche y el día."
        eil "Y, con la ilusión que habla desde vuestra comida, no creo que vaya a tener la intención de probar nada con ningún hombre que no seas tú."
        mc "Yo también estoy ilusionado, [eil]. Tu madre me parece una mujer maravillosa."
        call BlinkXPS3("c23s003_070" , "d") from _call_BlinkXPS3_1159
        eil "Ahora ya solo falta que os acostéis juntos. *Risa* ¿Ya has planeado cuándo?"
        mc "*Risa* Veo que no te lo ha explicado todo."
        call BlinkXPS3("c23s003_075" , "d") from _call_BlinkXPS3_1160
        eil "¿QUÉ? ¿Ya te has acostado con ella? ¿Cuándo? ¿Dónde? ¿Cuándo lo planeaste?"
        mc "*Risa* No voy a confirmar ni a desmentir nada. Sólo te digo que [kia] no te lo ha explicado todo."
        call BlinkXPS3("c23s003_080" , "d") from _call_BlinkXPS3_1161
        eil "¡Joder, [mc]! *Risa* ¡Ahora no voy a poder pensar en otra cosa!"
    else:
        call BlinkXPS3("c23s003_070" , "d") from _call_BlinkXPS3_1162
        eil "*Risa* Al menos ella está protegida contra tus encantos."
        mc "¡Hey! ¡No tengo intención de salir con cada chica que viva en casa!"
        call BlinkXPS3("c23s003_080" , "d") from _call_BlinkXPS3_1163
        eil "¡Joder, [mc]! *Risa* ¡Ahora no voy a poder pensar en otra cosa que en [kat], [kim] y tú en la misma cama!"
    if not eil._var("route"):
        scene c23s003_080An with dissolve
        stop music fadeout (1.5)
        "Pasáis un rato charlando y riéndoos de los viejos tiempos y de las nuevas situaciones."
        return
    mc "Bueno, yo puedo darte otras cosas en las que pensar. Ese uniforme me trae recuerdos..."
    call BlinkXPS3("c23s003_085" , "d") from _call_BlinkXPS3_1164
    eil "¿Me vas a levantar la falda como hacías debajo de las gradas?"
    mc "Creo que ya somos mayorcitos para eso, [eil.nick]."
    mc "Ahora quiero el plato completo."
    call BlinkXPS3("c23s003_090" , "d") from _call_BlinkXPS3_1165
    eil "El plato completo lo has tenido siempre. *Risa* No sé a lo que te refieres."
    mc "*Risa* El papel de animadora tonta no te pega, [eil]."
    call BlinkXPS3("c23s003_095" , "d") from _call_BlinkXPS3_1166
    eil "No sé... dijiste que era una animadora cliché."
    mc "Pero no en ese sentido. Eras un poco abusona con el resto de las chicas, y un poco mandona conmigo, pero nunca has sido tonta."
    mc "Te importaban las apariencias, pero no igual que a otras de las chicas del equipo."
    call BlinkXPS3("c23s003_100" , "d") from _call_BlinkXPS3_1167
    eil "Si me hubieran importado las apariencias no hubiera salido contigo. *Risa*"
    mc "*Risa* Si hubieras sido la animadora cliché, hubiera sido yo quien no hubiera salido contigo."
    call BlinkXPS3("c23s003_105" , "d") from _call_BlinkXPS3_1168
    eil "..."
    mc "*Risa* Vale, sí. Hubiera salido contigo si se hubiera dado la oportunidad."
    mc "Pero hubiera salido contigo a desgana. *Risa*"
    scene c23s003_110AnBlink with dissolve
    eil "Seguramente hasta que vieras a estas dos..."
    call BlinkXPS3("c23s003_115" , "d") from _call_BlinkXPS3_1169
    eil "*Risa* Y pusieras esa cara, como si los ojos se te fueran a salir de las órbitas."
    mc "*Risa* Creo que, en el momento en que las viera por primera vez, me daría lo mismo si eras superficial o una animadora cliché."
    call BlinkXPS3("c23s003_120" , "d") from _call_BlinkXPS3_1170
    eil "*Risa* ¿Sabes una cosa que me encanta y nunca te he dicho?"
    mc "*Risa* No sé, ¿la pizza con piña?"
    call BlinkXPS3("c23s003_125" , "d") from _call_BlinkXPS3_1171
    eil "*Risa* No, idiota."
    eil "Me encanta que todavía las miras con la misma cara que las miraste la primera vez."
    mc "¿Qué cara puse?"
    call BlinkXPS3("c23s003_130" , "d") from _call_BlinkXPS3_1172
    eil "La misma que pones ahora. No sé, como preguntándote si son de verdad y si voy a dejarte tocarlas."
    eil "Como si todavía fuera la primera vez que las vieras."
    mc "Es que siguen tan perfectas como la primera vez que las vi."
    mc "Pero no sabía que recordaras la cara que puse aquel día."
    call BlinkXPS3("c23s003_135" , "d") from _call_BlinkXPS3_1173
    eil "Estaba tan nerviosa como tú. Eras el primer chico que las veía."
    eil "Siempre me han parecido pequeñas y no sabía si te iban a gustar."
    mc "Tienen el tamaño perfecto, [eil.nick]. Y lo siguen teniendo aunque hayan crecido un poco. Siempre te lo he dicho."
    call BlinkXPS3("c23s003_140" , "d") from _call_BlinkXPS3_1174
    eil "Ahora lo sé. *Risa* Lo supe desde que las viste por primera vez y empezaste a babear."
    call BlinkXPS3("c23s003_145" , "d") from _call_BlinkXPS3_1175
    eil "Pero aquel día estaba más nerviosa de lo que había estado nunca."
    eil "Estaba más nerviosa incluso de lo que estuve cuando, meses después, perdimos la virginidad juntos."
    mc "Yo estaba histérico la primera vez que nos acostamos juntos."
    call BlinkXPS3("c23s003_150" , "d") from _call_BlinkXPS3_1176
    eil "Yo también, pero estaba mucho más segura de nuestra relación. Era una evolución natural..."
    mc "Ven aquí, cielo."
    call BlinkXPS3("c23s003_155" , "d") from _call_BlinkXPS3_1177
    eil "Lo siento..."
    mc "¿El qué? ¿Qué ha pasado?"
    call BlinkXPS3("c23s003_160" , "d") from _call_BlinkXPS3_1178
    eil "A veces me pongo demasiado sentimental recordando aquellos tiempos. Cuando todo empezaba y teníamos todo por descubrir todavía."
    eil "Cuando te tenía para mí todo el día..."
    if mc._var("relationships")>1:
        mc "[eil.nick], mírame."
        call BlinkXPS3("c23s003_165" , "d") from _call_BlinkXPS3_1179
        eil "Lo sé, soy una tonta..."
        mc "¿Te molesta que salga con alguien más aparte de ti?"
        call BlinkXPS3("c23s003_170" , "d") from _call_BlinkXPS3_1180
        eil "¿Qué? ¡No! ¡No lo decía por eso!"
        mc "Entonces me he perdido algo. No te entiendo."
        call BlinkXPS3("c23s003_175" , "d") from _call_BlinkXPS3_1181
        eil "La idea de que tuvieras un harén fue mía. Tú no lo hubieras hecho nunca."
        eil "Es imposible que me moleste que me hayas hecho caso, idiota."
        mc "Entonces, ¿a qué te referías?"
    call BlinkXPS3("c23s003_180" , "d") from _call_BlinkXPS3_1182
    eil "Entonces pasábamos todo el día juntos. En el instituto y al acabar las clases. Íbamos a la biblioteca juntos..."
    mc "Aunque a veces se apuntara Jam. *Risa*"
    call BlinkXPS3("c23s003_185" , "d") from _call_BlinkXPS3_1183
    eil "*Risa* Sí, le costó entender que ya no le pertenecías sólo a él y que tenía que compartirte conmigo."
    mc "*Risa* Creo que eso ha sonado mejor en tu cabeza..."
    call BlinkXPS3("c23s003_190" , "d") from _call_BlinkXPS3_1184
    eil "Es posible, pero a lo que me refiero es que, por entonces, nos veíamos todos los días, a todas horas."
    eil "Ahora hay días en los que apenas te veo si no es en la comida o en la cena. Echo de menos cosas de aquellos días."
    mc "Lo entiendo, a mí me pasa lo mismo. Pero también hay cosas que no echo de menos."
    call BlinkXPS3("c23s003_195" , "d") from _call_BlinkXPS3_1185
    eil "¡Por supuesto! *Risa* No echo de menos mi acné ni tu barriga."
    eil "Ni los exámenes. Ni siquiera echo de menos al equipo de animadoras."
    call BlinkXPS3("c23s003_200" , "d") from _call_BlinkXPS3_1186
    eil "Pero, sobre todo, no echo de menos tener que ver a mi padre al llegar a casa."
    eil "No echo de menos vivir en un ambiente tóxico."
    call BlinkXPS3("c23s003_205" , "d") from _call_BlinkXPS3_1187
    eil "Sabía que vivir con vosotros iba a ser increíble. Os había visto como la familia que hubiera querido tener."
    eil "Estaba equivocada."
    mc "¿Tan malos somos?"
    call BlinkXPS3("c23s003_210" , "d") from _call_BlinkXPS3_1188
    eil "Lo que se ve desde fuera es increíble. Vivirlo desde dentro es indescriptible."
    eil "Y las cosas han cambiado mucho desde que tú y yo íbamos al instituto. Ahora son incluso mejores."
    mc "Es lo que tiene tener un padre de mierda y que haya desaparecido."
    mc "Nunca creí que mi padre fuera tan malo como el tuyo, pero su marcha ha hecho que todo el mundo se sienta liberado hasta cierto punto."
    call BlinkXPS3("c23s003_215" , "d") from _call_BlinkXPS3_1189
    eil "Bueno, los dos nos hemos librado de nuestra mierda de padres."
    if eil._var("pregnant"):
        eil "Y ahora vamos a ser padres nosotros..."
        mc "Espero ser mejor que ellos."
        eil "Lo serás."
    stop music fadeout (1.5)
    eil "Pero volviendo al tema inicial..."
    call BlinkXPS3("c23s003_220" , "d") from _call_BlinkXPS3_1190
    play music ("music/SensualJazzMedium2.ogg")
    eil "¿Me vas a levantar la falda o no? *Risa* ¿O me voy a tener que ir al trabajo sin que la levantes?"
    mc "Tus cambios de tema a veces me desconciertan. *Risa*"
    call BlinkXPS3("c23s003_225" , "d") from _call_BlinkXPS3_1191
    eil "*Risa* Hemos empezado hablando de mis tetas y hemos acabado hablando de nuestros padres."
    eil "Creo que es mejor volver a las tetas. *Risa*"
    mc "Estoy totalmente de acuerdo. *Risa* Llevan mucho rato al descubierto sin que nadie les preste atención."
    call BlinkXPS3("c23s003_230" , "d") from _call_BlinkXPS3_1192
    eil "Aún no has hablado de la falda. *Risita* Creía que ibas a tener más interés en ella."
    mc "Ya te he dicho que el único interés que tengo en esa falda es arrancártela. *Risa*"
    call BlinkXPS3("c23s003_235" , "d") from _call_BlinkXPS3_1193
    eil "¡No, no! Eres capaz de romperla y entonces no me podré volver a vestir de animadora para ti."
    mc "O te la quitas tú o te la quito yo. *Risa* Puedes elegir."
    mc "Prefiero una animadora desnuda a una vestida."
    scene c23s003_240AnBlink with dissolve
    eil "Pues va a ser una desnuda. Le tengo cariño al uniforme."
    mc "Tanto como desnuda... aún veo ropa ahí."
    call BlinkXPS3("c23s003_245" , "d") from _call_BlinkXPS3_1194
    eil "*Risa* Eso sí que dejo que me lo quites tú. No quiero que las rompas, pero no me llevaría un disgusto enorme si lo hicieras."
    mc "Entonces creo que las quitaré todo lo delicadamente que mi ansia permita."
    scene c23s003_250An with dissolve
    mc "Tan precioso como siempre."
    eil "¿Sabes una de las cosas que siempre me han gustado de ti y nunca te he dicho?"
    call BlinkXPS3("c23s003_255" , "d") from _call_BlinkXPS3_1195
    mc "Otra pregunta imposible de responder. ¿Que no odio a la gente a quien le gusta la pizza con piña?"
    eil "*Risa* ¿Qué te pasa hoy con la pizza con piña?"
    mc "Nada. *Risa* He estado leyendo una discusión en un foro sobre eso."
    mc "Pero dime qué es eso tan importante que siempre te ha gustado de mí. Me encanta que me regalen los oídos."
    call BlinkXPS3("c23s003_260" , "d") from _call_BlinkXPS3_1196
    eil "Que nunca te has puesto quisquilloso con cómo llevo el pelo ahí abajo."
    mc "Bueno, si me gustas tal como eres, eso incluye tu pelo. Arriba y abajo."
    mc "No soy de los tipos que piensan que el pelo equivale a suciedad ni voy a rechazar a nadie por cómo lo lleve."
    if oma._var("route"):
        call BlinkXPS3("c23s003_265" , "d") from _call_BlinkXPS3_1197
        eil "Si no, no saldrías con [oma]. *Risa* Me encanta que sea tan segura como para llevarlo así."
        mc "¿Salir con [oma]? No sé quién es [oma]. Solo existes tú, cielo."
    elif sam._var("route") and sam._var("naturalPubicHair"):
        call BlinkXPS3("c23s003_265" , "d") from _call_BlinkXPS3_1198
        eil "Si no, no saldrías con [sam]. *Risa* Me encanta que sea tan segura como para llevarlo así."
        mc "¿Salir con [sam]? No sé quién es [sam]. Solo existes tú, cielo."
    elif deb._var("route") or mad._var("route") or (sam._var("route") and not sam._var("naturalPubicHair")):
        call BlinkXPS3("c23s003_265" , "d") from _call_BlinkXPS3_1199
        eil "Lo sé. Si no, no saldrías con chicas con el pelo tan variado. *Risa* Abajo."
        mc "No sé a qué chicas te refieres. Solo existes tú, cielo."
    call BlinkXPS3("c23s003_270" , "d") from _call_BlinkXPS3_1200
    eil "Sube aquí y bésame. Eres el hombre de las respuestas correctas."
    mc "¿Alguna vez te dije que eras una novia un poco mandona? Cuando me mandas cosas así casi no me importa."
    scene c23s003_895pv with fade
    show c23s003_895v
    "La lengua de la animadora pelirroja sale a saludar a la tuya en un beso largamente esperado."
    "Los días de instituto, de besos en cada descanso, han quedado en el pasado."
    "Viviendo casi en la misma casa os veis mucho menos que antes, entre su trabajo y tus obligaciones."
    "Vuestras lenguas y vuestras bocas quieren recuperar el tiempo perdido cuanto antes."
    call BlinkXPS3("c23s003_275" , "d") from _call_BlinkXPS3_1201
    hide c23s003_895v
    eil "Me parece que estoy en inferioridad de condiciones."
    eil "Te sobra mucha ropa ahora mismo y le voy a poner solución."
    mc "Me parece una buena idea. *Risa* Me siento un poco apretado dentro de los pantalones ahora mismo."
    scene c23s003_280An with dissolve
    eil "¿Sabes que a veces echo de menos que estés un poco gordito?"
    mc "¿Qué? ¿Por qué?"
    scene c23s003_285An with dissolve
    eil "No lo sé, era diferente que ahora. Parecías... más real."
    mc "Sigo siendo el mismo, [eil.nick]. Tan solo hay menos grasa."
    scene c23s003_290AnBlink with dissolve
    eil "Lo sé, pero... no sé... ponerme el uniforme ha hecho que me entre añoranza del instituto..."
    mc "Eras lo único bueno del instituto, cielo. Yo no lo recordaría como una época feliz si no fuera por ti."
    mc "*Risa* Bueno, y Jamaal no molestaba demasiado."
    call BlinkXPS3("c23s003_295" , "d") from _call_BlinkXPS3_1202
    eil "Tienes razón. Tenemos perspectivas diferentes."
    eil "Pero si hay algo que no cambia es esta preciosidad que tengo en las manos. Duro como siempre."
    mc "Es el efecto que provocas. *Risa* No es culpa mía."
    eil "Yo no buscaría culpables en esto. *Risa* Y es una forma de hacer que una chica se sienta halagada."
    scene c23s003_305An with dissolve
    "Sin decir una palabra más, [eil] se sienta entre tus piernas y se introduce en la boca a su viejo amigo."
    "La boca de la camarera conoce a la perfección cada uno de tus puntos sensibles."
    scene c23s003_945pv with dissolve
    show c23s003_945v
    "Reconoces de inmediato lo que está haciendo [eil]. Parece que encontrar el uniforme le ha afectado más de lo que pensabas."
    mc "¿El partido del último año contra Cabrillo High School?"
    "Fue la primera vez que te hizo una mamada sentada así, entre tus piernas, después del partido, debajo de las gradas."
    eil "*Slurp afirmativo*"
    "[eil] era la única razón por la que asistías a los partidos de los equipos del instituto."
    scene c23s003_950pv with dissolve
    hide c23s003_945v
    show c23s003_950v
    "Ella es igual de exquisita con tu polla en la boca como lo ha sido siempre. Conoce cada uno de tus puntos sensibles y los visita todos con su lengua."
    eil "*Slurp*"
    "Sus mamadas sin manos son de las mejores que has recibido nunca. Siempre te has preguntado donde esconde los dientes cuando tiene tu polla en la boca."
    eil "*Slurp inquisitivo*"
    "Sabe que te encanta lo que te está haciendo, pero siempre pregunta si te está gustando. Una chica considerada."
    mc "Sí, [eil.nick]. Está siendo alucinante."
    scene c23s003_955pv with dissolve
    hide c23s003_950v
    show c23s003_955v
    "Con [eil] el sexo siempre ha consistido más en darle placer al otro que en recibirlo uno mismo."
    eil "*Slurp feliz*"
    "Es una suerte que descubrieras el sexo con ella. Una de las personas más generosas que has conocido cuando se trata de sexo."
    eil "*Slurp*"
    "Eso hizo que tú también te volvieras generoso, priorizando su placer por encima del tuyo. Es el momento de hacerlo."
    mc "[eil], vamos a la cama, yo también quiero probarte."
    call BlinkXPS3("c23s003_310" , "d") from _call_BlinkXPS3_1203
    eil "*Jadeo* No, cielo, no va a ser hoy. Quiero que me hagas el amor aquí, de pie."
    "Su voz y su mirada te indican que se ha puesto tan cachonda comiéndote la polla como te ha puesto a ti."
    mc "Como desees. Ven aquí."
    scene c23s003_900pv with fade
    hide c23s003_955v
    show c23s003_900v
    "En el momento en que la penetras y empiezas a bombear recuerdas en qué partido follasteis por primera vez así. Contra Atascadero HS. Vuestro equipo perdió. Tú ganaste."
    eil "*Gemido* Hoy no me daré con la cabeza contra las vigas de las gradas. *Jadeo*"
    "Tuvisteis que cambiar de postura varias veces, hasta encontrar una posición cómoda en la que la animadora pudiera sacar todo el partido a su flexibilidad."
    eil "*Jadeo* Sigue siendo tan bueno como lo fue entonces. *Gemido*"
    "En esta posición la penetras profundamente, impactando en su cérvix a cada embestida. Era increíble entonces y lo sigue siendo."
    scene c23s003_905pv with dissolve
    hide c23s003_900v
    show c23s003_905v
    "Puedes notar cada una de las rugosidades del interior de su coño con cada movimiento, mientras ella estruja tu astil sincronizándose contigo."
    eil "*GEMIDO* ¿Te está gustando, mi amor? *JADEO* A mí me está encantando. *GEMIDO*"
    mc "Sí, cielo. No te preocupes y disfruta."
    "Sus movimientos se adaptan tan bien a los tuyos que parecéis una máquina bien engrasada de crear placer. Para ella y para ti."
    eil "*JADEO* Me encanta esta postura. *GEMIDO* Llegas a todos mis puntos sensibles. *JADEO*"
    "Y cada uno de sus puntos sensibles rozan en los tuyos de una forma increíble, convirtiéndose en la funda perfecta para tu polla."
    scene c23s003_910pv with dissolve
    hide c23s003_905v
    show c23s003_910v
    "Sus movimientos se van haciendo más espasmódicos tal como tu bombeo gana en velocidad, indicando que la incómoda posición la está cansando."
    eil "*GEMIDO* Es uno de los mejores polvos que hemos echado nunca. *JADEO*"
    "O a lo mejor es que se está acercando al orgasmo. A veces no estás seguro con [eil]."
    eil "*JADEO* Déjame cambiar de posición. *GEMIDO* La pierna se me está cansando mucho. *JADEO*"
    "¡Lo sabías! No siempre estás seguro, pero conoces su cuerpo tan bien como ella conoce el tuyo."
    scene c23s003_930pv with fade
    hide c23s003_910v
    show c23s003_930v
    "[eil] cambia a una posición que te parece igual de incómoda para ella. E igual de increíble para ti."
    eil "*GEMIDO* ¡Mucho mejor así! *JADEO*"
    "El cambio de su pierna de apoyo le vuelve a dar estabilidad y te permite cambiar el ángulo en el que la embistes."
    eil "*JADEO* ¡No pares! *GEMIDO* ¡Estoy muy cerca! *JADEO*"
    "Este ángulo hace que roces en sitios en los que no lo hacías antes, provocando y recibiendo nuevas dosis de placer."
    scene c23s003_940pv with dissolve
    hide c23s003_930v
    show c23s003_940v
    "Su cara refleja las sensaciones que su cuerpo recibe. Placer en dosis inconmensurables."
    eil "*GEMIDO* ¡Estoy a punto! *JADEO* ¡Pero a ti te falta mucho aún! *GEMIDO*"
    "No hay demasiado espacio para las sorpresas entre vosotros cuando sois capaces de leer los movimientos del otro como si de un libro abierto se tratara."
    eil "*JADEO* ¡NO VOY A PODER CONTENERLO MÁS! *GEMIDO* ¡Aunque me corra, no pares! *JADEO*"
    "Nunca lo has hecho, y no es el mejor momento para empezar. Sabes que seguir bombeando mientras [eil] se corre es una de las mejores sensaciones."
    call OrgasmXS3("c23s003_315") from _call_OrgasmXS3_33
    eil "*GEMIDO* ¡ME CORROOOO! *JADEO* ¡MAS PROFUNDO! *GEMIDO*"
    "El coño de [eil] se cierra sobre tu astil como una trampa para osos sin querer soltar su presa."
    "Su estrecho agujero se estrecha más todavía, con oleadas de espasmos musculares que recorren toda su vagina y que amasan tu polla en toda su longitud."
    scene c23s003_935pv with dissolve
    hide c23s003_940v
    show c23s003_935v
    "Y, obviamente, no dejas de embestir. La estrechez que produce su clímax es contrarrestada por la nueva humedad lubricando todo el recorrido."
    eil "*JADEO* ¡SIGUE ASÍ! *GEMIDO* ¡AL MENOS MIENTRAS ME AGUANTE LA PIERNA! *JADEO*"
    "Se acerca el siguiente paso. Esa frase tan solo significa que su pierna se está convirtiendo en gelatina. Te preparas para llevarla a la cama cuando la pierna empiece a fallar."
    eil "*GEMIDO* ¡NO PUEDO PARAR DE CORRERME! *JADEO* ¡NO VOY A AGUANTAR MUCHO MÁS! *GEMIDO*"
    "A veces te odias por conocerla tan bien. Ella adora que puedas anticipar cada uno de sus movimientos."
    scene c23s003_940pv with dissolve
    hide c23s003_935v
    show c23s003_940v
    "Cuando la pierna le empieza a fallar, la gravedad hace su trabajo y se empala todavía más en Mjolnir, aunque sea casi imperceptible."
    eil "*GEMIDO* ¡LLÉVAME A LA CAMA! *JADEO* ¡O VOY A CAERME!"
    "Es una lástima tener que perder de vista su hermoso rostro mientras las oleadas de orgasmos recorren su cuerpo uno tras otro."
    scene c23s003_915pv with fade
    "La levantas en vilo y te sientas en la cama sin salir de su coño en ningún momento, dejando que ella se siente encima de tu polla."
    hide c23s003_940v
    show c23s003_915v
    "Es el momento de dejarle marcar el ritmo. La pelirroja sigue controlando el ritmo de sus movimientos a pesar de las oleadas de orgasmos que la recorren."
    eil "*GEMIDO* ¡TE QUIERO! *JADEO* ¡Eres el mejor amante que nadie podría imaginar! *GEMIDO*"
    "Esas palabras llenarían el ego de cualquiera. No el tuyo. Tu ego es alimentado por los gemidos y los espasmos que sufre el cuerpo de [eil]."
    eil "*JADEO* ¡ME ENCANTA! *GEMIDO* ¡NO QUIERO QUE ESTO ACABE! *JADEO*"
    "Tu tampoco, pero tu resistencia también tiene un límite, y ser exprimido por el coño de la preciosa mujer te está acercando a tu límite."
    scene c23s003_920pv with dissolve
    hide c23s003_915v
    show c23s003_920v
    eil "*GEMIDO* ¡Córrete para mí, mi amor! *JADEO* ¡LLÉNAME CON TU SEMILLA! *GEMIDO*"
    if eil._var("pregnant"):
        "Aunque no puedas dejarla embarazada otra vez, su avaricia por tu semen no ha disminuido un ápice sorprendentemente."
    else:
        "No has conseguido dejarla embarazada hasta ahora y aparece una avaricia por tu semen que te sorprende."
    "Con las inmejorables vistas y los movimientos rítmicos de la asombrosa mujer no tienes tiempo de disfrutar de la sorpresa."
    eil "*JADEO* ¡HE PERDIDO LA CUENTA DE CUANTAS VECES ME HE CORRIDO! *GEMIDO* ¡AHORA QUIERO QUE TE CORRAS TÚ! *JADEO*"
    "Aunque intentes contenerlo, tu orgasmo llega como una explosión bajo las órdenes de [eil]."
    if persistent.pregnancy and not eil._var("pregnant"):
        if persistent.walkthrough:
            $ wt1 = _("[eil] embarazada.")
            $ wt2 = _("Sin consecuencias.")
        else:
            $ wt1 = ""
            $ wt2 = ""
        menu:
            "Correrte dentro" (wt = wt2):
                pass
            "Correrte dentro. Ir a por el bebé." (wt = wt1):
                $ eil._var("pregnant", True)
                $ eil._var("undiscoveredPregnancy", True)
                play sound ("music/OldMusicBox5.ogg")
    $ resetWalkthrough ()
    call OrgasmXS3("c23s003_320") from _call_OrgasmXS3_34
    mc "¡Mpfft!"
    "Un géiser de semen brota de la punta de tu polla y llena el interior de la chica."
    eil "*GEMIDO* ¡SÍ! *JADEO* ¡ME ENCANTA SENTIRME LLENA DE TI! *GEMIDO*"
    "Pese a que tensa su coño con todas sus fuerzas, algunas gotas se escapan irremisiblemente."
    "Y ahora viene lo mejor."
    scene c23s003_925pv with dissolve
    hide c23s003_920v
    show c23s003_925v
    "Ella te conoce tan bien que sabe que los segundos después de correrte son los que más disfrutas, cuando más sensible estás."
    eil "*JADEO* ¡ESTO VA POR TI, MI AMOR! *GEMIDO*"
    "Sacando fuerzas de flaqueza, en medio de una oleada de orgasmos, [eil] redobla sus esfuerzos por mantener un ritmo que ordeñe cada gota de tu corrida."
    eil "*GEMIDO* ¡DÁMELA TODA! *JADEO*"
    "Sabes que no va a durar mucho más después de las decenas de orgasmos que ha experimentado, pero la sensación en tu polla es increíble."
    call BlinkXPS3("c23s003_325" , "f") from _call_BlinkXPS3_1204
    "Al cabo de un par de impresionantes minutos, [eil] para su proceso de empalamiento."
    stop music fadeout (1.5)
    eil "*Gemido* No puedo más... *Jadeo* Lo siento... *Gemido*"
    play music ("music/Separation.ogg")
    mc "¿Sentir? ¡Ha sido increíble, [eil.nick]!"
    mc "Ven aquí, túmbate conmigo."
    call BlinkXPS3("c23s003_330" , "f") from _call_BlinkXPS3_1205
    mc "¿Qué es lo que tienes que sentir, cielo?"
    eil "Antes duraba más. Era capaz de seguir más tiempo después de que te corrieras..."
    mc "*Risa* Nos hacemos viejos, [eil]."
    call BlinkXPS3("c23s003_335" , "d") from _call_BlinkXPS3_1206
    eil "*Risa* Si me llegas a llamar vieja antes de empezar, te quedas sin follar."
    mc "Por eso te lo he dicho ahora. *Risa* No te preocupes, ha sido buenísimo."
    mc "Y creo que tienes una percepción equivocada sobre lo que durábamos antes. Siempre íbamos con prisas y con miedo de que alguien nos pillara."
    call BlinkXPS3("c23s003_340" , "d") from _call_BlinkXPS3_1207
    eil "*Risa* Tienes razón. Siempre teníamos que hacerlo en algún sitio medio a escondidas."
    mc "Creo que debemos ser una de las parejas que menos sexo ha tenido en una cama, al menos porcentualmente."
    call BlinkXPS3("c23s003_345" , "d") from _call_BlinkXPS3_1208
    eil "Es posible. Esta es nuestra primera vez en una cama desde que volviste."
    mc "Siempre hemos sido más de exteriores. Pero ahora que nos hacemos viejos..."
    call BlinkXPS3("c23s003_350" , "d") from _call_BlinkXPS3_1209
    eil "Ni se te ocurra acabar esa frase. Te haces viejo tú. Yo me convertiré en una madura interesante. Dentro de 20 o 30 años."
    mc "Serás una MILF increíble. *Risa* La mejor amante que se puede tener."
    call BlinkXPS3("c23s003_355" , "d") from _call_BlinkXPS3_1210
    eil "Sobre eso..."
    mc "¿Qué pasa? ¿He dicho algo malo?"
    call BlinkXPS3("c23s003_360" , "d") from _call_BlinkXPS3_1211
    eil "No. Es por lo que he dicho yo antes sobre que eres el mejor amante que nadie podría imaginar..."
    mc "¿Qué pasa con eso?"
    call BlinkXPS3("c23s003_365" , "d") from _call_BlinkXPS3_1212
    eil "Sabes que soy una bocazas y sé que nunca me lo vas a preguntar por no ponerme en una situación incómoda..."
    mc "¿Preguntarte qué? No te entiendo."
    call BlinkXPS3("c23s003_370" , "d") from _call_BlinkXPS3_1213
    eil "El día que volviste... bueno, el primer día que nos vimos en el café... te dije que..."
    mc "Que habías tenido algunas citas una vez rompimos, lo sé. Y sabes que no me importa. Yo también tuve algunas citas."
    call BlinkXPS3("c23s003_375" , "d") from _call_BlinkXPS3_1214
    eil "Lo que quiero decir es que no tengo con quién compararte como amante. Ninguna de esas citas pasó de una cena o de ir al cine."
    eil "No me acosté con ninguno de esos chicos."
    call BlinkXPS3("c23s003_380" , "d") from _call_BlinkXPS3_1215
    eil "Ninguno de aquellos chicos eras tú."
    mc "Me lo imagino. Si hubiera yo hubiera sido uno de ellos, lo recordaría."
    call BlinkXPS3("c23s003_385" , "d") from _call_BlinkXPS3_1216
    eil "¡Idiota! ¡Estoy hablando en serio!"
    mc "Y yo también. ¿Crees que me importaría si te hubieras acostado con alguno de ellos?"
    mc "¿Te importa a ti que saliera y me acostara con [sai] mientras tú y yo no estábamos juntos?"
    call BlinkXPS3("c23s003_390" , "d") from _call_BlinkXPS3_1217
    eil "No. Y no. Pero con las mujeres es diferente..."
    eil "Si un hombre se acuesta con diez mujeres diferentes es un macho."
    eil "Si una mujer se acuesta con tres hombres, es una puta para muchos hombres."
    mc "Son esos hombres los que tienen un problema, no la mujer. Sabes que yo no pienso así."
    mc "Además, no lo hiciste, con lo que no hay más de que hablar."
    call BlinkXPS3("c23s003_395" , "d") from _call_BlinkXPS3_1218
    eil "Son por estas cosas por las que te quiero. Lo sabes, ¿verdad?"
    mc "Yo creía que sólo me querías porque soy el mejor amante que nadie pueda imaginar. *Risa*"
    call BlinkXPS3("c23s003_400" , "d") from _call_BlinkXPS3_1219
    eil "A veces eres idiota. Estoy hablando en serio, [mc]."
    eil "Si fueras diferente no me atrevería a hablarte de todo."
    mc "Lo sé. Yo también te quiero, [eil.nick]. Eres una mujer maravillosa."
    call BlinkXPS3("c23s003_405" , "d") from _call_BlinkXPS3_1220
    eil "Pues ahora esta mujer maravillosa se va a tener que ir. Me quiero dar una ducha rápida antes de ir a trabajar."
    mc "Puedes coger mi albornoz si quieres y ducharte aquí."
    call BlinkXPS3("c23s003_410" , "d") from _call_BlinkXPS3_1221
    eil "No hace falta. Me vuelvo a poner el uniforme y voy a casa. Tengo tiempo."
    mc "Como desees."
    call BlinkXPS3("c23s003_415" , "f") from _call_BlinkXPS3_1222
    "Una vez los dos os habéis vestido..."
    eil "Me voy a ir ya. Gracias por ser como eres."
    mc "Gracias a ti por hacerme como soy."
    call BlinkXPS3("c23s003_420" , "d") from _call_BlinkXPS3_1223
    eil "¡Oh! ¡Eso es muy bonito! No me lo habías dicho nunca."
    stop music fadeout (1.5)
    mc "Pero te lo he demostrado muchas veces."
    return
label c23s004_Kia:
    if _in_replay:
        call mrS3_kia_route from _call_mrS3_kia_route_2
        call mrS3_eil_route from _call_mrS3_eil_route_2
    scene c23s004_005a with dissolve
    play sound ("music/knock.ogg")
    "*Knock-Knock*"
    kia "*A través de la puerta* [mc], ¿estás ahí? ¿Puedo pasar?"
    mc "Sí, pasa."
    play music ("music/Rise-Up.ogg")
    call BlinkXPS3 ("c23s004_010" , "d") from _call_BlinkXPS3_1224
    kia "¡Oh! No sabía que estabas aquí, [eil.nick]. Precisamente venía a preguntarle a [mc] si te había visto."
    call BlinkXPS3 ("c23s004_015" , "d") from _call_BlinkXPS3_1225
    eil "Llevo un rato aquí, hemos estado... charlando."
    mc "¿No estabas trabajando?"
    call BlinkXPS3 ("c23s004_020" , "d") from _call_BlinkXPS3_1226
    kia "Hoy empiezo a mediodía. Por eso estaba buscando a [eil]."
    kia "Me ha llamado [oma]. Va a venir a recogerme para llevarme al trabajo, por si querías venir tú también y te dejamos en el café."
    call BlinkXPS3 ("c23s004_025" , "d") from _call_BlinkXPS3_1227
    eil "¡Oh, eso sería fantástico! ¡Voy a cambiarme!"
    if kia._var("route"):
        call BlinkXPS3 ("c23s004_030" , "d") from _call_BlinkXPS3_1228
        eil "Por cierto, Mamá, sabes que puedes besar a [mc] aunque yo esté delante, ¿verdad?"
        mc "[eil], no tienes que presionarla."
        call BlinkXPS3 ("c23s004_035" , "d") from _call_BlinkXPS3_1229
        kia "*Risa* No me siento presionada, pero prefiero hacerlo cuando te hayas ido."
        call BlinkXPS3 ("c23s004_040a" , "d") from _call_BlinkXPS3_1230
        eil "Pues me voy y os dejo que os beséis con tranquilidad."
        call c23s004_EilKiss from _call_c23s004_EilKiss
        call BlinkXPS3 ("c23s004_045" , "d") from _call_BlinkXPS3_1231
        kia "Esta chica..."
        mc "Creo que tenías un beso para mí..."
        scene c23s004_050a with dissolve
        "Sin decir una palabra, sus dulces labios buscan los tuyos."
        "Hoy no saben a aguacate, pero no por ello son menos deliciosos."
        "Como siempre, os separáis para recuperar el aliento. Demasiado pronto."
        call BlinkXPS3 ("c23s004_055" , "d") from _call_BlinkXPS3_1232
        hide c23s004_050v
        kia "*Respiración entrecortada* ¡Phew! Y por esto prefiero besarte en privado. *Risa*"
        mc "Llamaremos a estos besos Darth Bader. *Risa* Cada vez que nos separamos respiramos como él."
        call BlinkXPS3 ("c23s004_060" , "d") from _call_BlinkXPS3_1233
        kia "*Risa* A veces me extraña que algo tan de mi época lo hayáis adoptado los jóvenes."
        mc "*Risa* Con la cantidad de spin offs que han hecho, creo que es de todas las épocas."
        call BlinkXPS3 ("c23s004_065" , "d") from _call_BlinkXPS3_1234
        kia "*Risa* Tienes razón, han encontrado la gallina de los huevos de oro y no pararán hasta que la maten."
        mc "Cambiando de tema, ¿hoy no hay vestido morado?"
        call BlinkXPS3 ("c23s004_070" , "d") from _call_BlinkXPS3_1235
        kia "Hoy no he quedado para comer con ningún chico guapo, con lo que no hay nadie a quien impresionar."
        mc "Tú impresionarías a ese chico afortunado llevaras lo que llevaras, o aunque no llevaras nada..."
        mc "Eso ha sonado mejor en mi cabeza..."
        call BlinkXPS3 ("c23s004_075" , "d") from _call_BlinkXPS3_1236
        kia "Bueno, espero, si no impresionarte, al menos no decepcionarte cuando no lleve nada."
        mc "No me podrías decepcionar nunca, [kia]. Estoy deseando poder demostrártelo."
        call BlinkXPS3 ("c23s004_080" , "d") from _call_BlinkXPS3_1237
        kia "Si no fuera porque mañana tienes que levantarte temprano... Tenemos una cena pendiente."
        kia "¿Cuándo vuelves? ¿El viernes?"
        mc "Sí, el viernes por la tarde espero estar de vuelta."
        call BlinkXPS3 ("c23s004_085" , "d") from _call_BlinkXPS3_1238
        kia "¿Te apetece que vayamos a cenar? Si no estás muy cansado cuando vuelvas, claro."
        mc "Apúntalo en la agenda. *Risa* Son poco más de dos horas conduciendo, no voy a estar cansado."
        call BlinkXPS3 ("c23s004_090" , "d") from _call_BlinkXPS3_1239
        kia "Entonces el viernes. Me apetece mucho tener nuestra tercera cita."
        mc "A mí también. Me encanta pasar tiempo contigo."
        call KissXPS3 ("c23s004_095" , "d") from _call_KissXPS3_27
        kia "Eres tan dulce... Pero debería bajar antes de que llegue [oma]."
    else:
        call c23s004_EilKiss from _call_c23s004_EilKiss_1
        call BlinkXPS3 ("c23s004_085" , "d") from _call_BlinkXPS3_1240
        kia "Debería bajar por si [oma] llega pronto."
    mc "Vamos. Te acompaño. No he visto a [oma] desde la fiesta de la piscina."
    if kia._var("route"):
        mc "Por cierto, sólo te había visto con las gafas en el restaurante."
    else:
        mc "Por cierto, hacía mucho tiempo que no te veía con gafas."
    call BlinkXPS3 ("c23s004_100" , "d") from _call_BlinkXPS3_1241
    kia "Me las pongo para leer y trabajar. Estas son las de reserva y no tienen funda, con lo que no las quiero llevar sueltas en el bolso para evitar rayarlas."
    kia "No sé dónde he dejado las otras gafas. A lo mejor las dejé en la biblioteca."
    mc "Si quieres le puedo pedir una funda a [mar] o a [kim]. Seguro que tienen de sobras."
    call BlinkXPS3 ("c23s004_105" , "d") from _call_BlinkXPS3_1242
    kia "No hace falta, son progresivas, puedo ver bien con ellas en cualquier circunstancia. Ya encontraré la funda."
    mc "Como quieras. Vamos entonces."
    stop music fadeout (1.5)
    if kia._var("route"):
        mc "De todas formas, estás guapísima con ellas."
        call BlinkXPS3 ("c23s004_110" , "d") from _call_BlinkXPS3_1243
        kia "Vamos antes de que te tenga que besar otra vez. *Risa*"
    return
label c23s004_EilKiss:
    if eil._var("route"):
        call KissXPS3 ("c23s004_040b" , "d") from _call_KissXPS3_28
        eil "Hasta luego, cielo."
    scene c23s004_005b with dissolve
    play sound ("music/DoorSlam.ogg")
    "*Blam*"
    eil "*A través de la puerta* Date prisa, Mamá. En menos de diez minutos estaré lista."
    return
label c23s004_Oma:
    if _in_replay:
        call mrS3_kia_route from _call_mrS3_kia_route_3
        call mrS3_oma_route from _call_mrS3_oma_route_2
        call mrS3_eil_route from _call_mrS3_eil_route_3
        if not eil._var("route"):
            call mrS3_deb_route from _call_mrS3_deb_route_6
    if kia._var("route"):
        call BlinkXPS3 ("c23s004_150a" , "f") from _call_BlinkXPS3_1244
    else:
        call BlinkXPS3 ("c23s004_150b" , "f") from _call_BlinkXPS3_1245
    play music ("music/CumbiaColombiana.ogg")
    "Cuando llegáis abajo, [oma] ya está esperando a [kia]."
    if oma._var("route"):
        call KissXPS3 ("c23s004_155" , "d") from _call_KissXPS3_29
        oma "Hola, cielo."
        mc "Hola, preciosa. ¿No trabajas hoy?"
    else:
        call BlinkXPS3 ("c23s004_160" , "d") from _call_BlinkXPS3_1246
        oma "Hola, [kia] y [mc]."
        mc "Hola, [oma]. ¿No trabajas hoy?"
    call BlinkXPS3 ("c23s004_165" , "d") from _call_BlinkXPS3_1247
    oma "Acabo de salir. Llevo toda la semana cubriendo el primer turno. Schrute está enfermo y estoy en el mostrador de la comisaría."
    mc "Ufff. Yo odiaría tener que madrugar tanto."
    call BlinkXPS3 ("c23s004_170" , "d") from _call_BlinkXPS3_1248
    kia "*Risa* Todo el mundo sabe que te gusta dormir hasta tarde."
    mc "¡Hey! ¡A primera hora de la mañana no tengo nada que hacer!"
    call BlinkXPS3 ("c23s004_175" , "d") from _call_BlinkXPS3_1249
    oma "Podrías venir a correr conmigo, al menos cuando tengo turno normal."
    call BlinkXPS3 ("c23s004_180" , "d") from _call_BlinkXPS3_1250
    kia "O hacer yoga con las chicas. Me han dicho que lo probaste una vez y no has vuelto."
    mc "*Risa* ¿Os dais cuenta de que lo único que proponéis es que haga más ejercicio?"
    mc "*Risa* ¿Me estáis soltando indirectas de que me estoy engordando?"
    call BlinkXPS3 ("c23s004_185" , "d") from _call_BlinkXPS3_1251
    if eil._var("route") or deb._var("route"):
        oma "No, sabemos que vas a correr al lago a menudo. *Risita* No necesitas más ejercicio."
    else:
        oma "No, sabemos que vas a correr al lago a menudo. No necesitas más ejercicio."
    oma "Pero has dicho que no tienes nada que hacer por las mañanas. *Risa* Sólo te estamos dando opciones."
    mc "Ya, pero lo del yoga... Ufff..."
    call BlinkXPS3 ("c23s004_190" , "d") from _call_BlinkXPS3_1252
    kia "Yo quiero apuntarme algún día. Quizás el domingo. ¿Por qué no vienes, [oma]?"
    call BlinkXPS3 ("c23s004_195" , "d") from _call_BlinkXPS3_1253
    oma "El domingo lo tengo libre. A lo mejor me apunto también. Solo lo he probado una vez, hace años, pero me gustó."
    call BlinkXPS3 ("c23s004_200" , "d") from _call_BlinkXPS3_1254
    eil "¿Qué pasa el domingo?"
    call BlinkXPS3 ("c23s004_205" , "d") from _call_BlinkXPS3_1255
    kia "Estábamos diciendo de apuntarnos a una sesión de yoga con las chicas."
    kia "A ver si así convencemos a [mc] de que se apunte también."
    call BlinkXPS3 ("c23s004_210" , "d") from _call_BlinkXPS3_1256
    eil "¡Contad conmigo! Creo que estoy perdiendo algo de flexibilidad."
    mc "Sabéis que no me vais a convencer, ¿verdad?"
    call BlinkXPS3 ("c23s004_215" , "d") from _call_BlinkXPS3_1257
    oma "No estés tan seguro. Con todas las chicas haciéndote bullying para que te apuntes, dudo que puedas resistirte."
    mc "Ya veremos, pero no estéis tan seguras."
    if oma._var("route"):
        call KissXPS3 ("c23s004_155" , "d") from _call_KissXPS3_30
    else:
        call BlinkXPS3 ("c23s004_220" , "d") from _call_BlinkXPS3_1258
    oma "Bueno, ya veremos. Me llevo a estas dos chicas antes de que se haga más tarde. Espero verte el domingo con mallas."
    mc "No me vuelvo a poner las mallas de Tío Mike en mi vida. *Risa*"
    if kia._var("route"):
        call KissXPS3 ("c23s004_225a" , "d") from _call_KissXPS3_31
    else:
        call BlinkXPS3 ("c23s004_225b" , "d") from _call_BlinkXPS3_1259
    kia "*Risa* Nos hablaron de lo anticuadas que se veían."
    mc "*Risa* Deben tener 20 años por lo menos."
    if eil._var("route"):
        call KissXPS3 ("c23s004_230a" , "d") from _call_KissXPS3_32
    else:
        call BlinkXPS3 ("c23s004_230b" , "d") from _call_BlinkXPS3_1260
    eil "Le preguntaremos a [mad.nick] si tiene unas más modernas para regalártelas. Así no podrás negarte. *Risa* No vas a despreciar nuestro regalo."
    mc "*Risa* Sois malvadas..."
    mc "Iros antes de que me convenzáis de irme a Aruba antes de que llegue el domingo."
    scene c23s004_235a with dissolve
    todas "Hasta luego, [mc]."
    scene c23s004_235b with dissolve
    oma "Por cierto, os tengo que contar algo que pasó el lunes."
    stop music fadeout (1.5)
    oma "Ahora os lo explico en el coche."
    return
label c23s004_Kim:
    scene black with dissolve
    "Pasas un rato después de comer leyendo los expedientes que [ama] y [jam] te han enviado sobre Iron Fist."
    play music ("music/thinking-of-you.ogg")
    "Bajas a media tarde a la cocina a por un vaso de agua. Tienes que comprarte una nevera para tu habitación."
    "[oma] y [kia] no contaban con la cantidad de escaleras que subes y bajas al cabo del día cuando hablaban del ejercicio que haces."
    scene c23s004_250d with fade:
        yalign 1.0
        linear 5.0 yalign 0.0
    pause (5.0)
    call BlinkXPS3 ("c23s004_250" , "d") from _call_BlinkXPS3_1261
    "Al pasar por la planta de las estudiantes te encuentras con [kim], que baja de tu planta."
    call addProfileImageS3 (4, "kim_4", kim, _(": 15 - Especial"), "") from _call_addProfileImageS3_4
    kim "Hola, [mc]. He pasado a verte por tu habitación."
    mc "¡Wow! ¿Dónde vas así vestida? Pareces una cazavampiros."
    call BlinkXPS3 ("c23s004_255" , "d") from _call_BlinkXPS3_1262
    kim "¿Te has olvidado?"
    if persistent.walkthrough:
        $ wt1 = "[gr][kim] +5"
        $ wt2 = "[red][kim] -5"
    else:
        $ wt1 = ""
        $ wt2 = ""
    menu:
        "¿De llevarte al puerto? No, no me he olvidado" (wt=wt1):
            $ kim.rp(+5)
            mc "Pero no sabía que tenías que ir vestida así. Me dijiste que era un trabajo de azafata y podrías pasar por una espía como [eva] y [ama]."
            call BlinkXPS3 ("c23s004_260" , "d") from _call_BlinkXPS3_1263
            kim "¡Sabía que no te olvidarías!"
        "¿Olvidarme de qué?" (wt=wt2):
            $ kim.rp(-5)
            mc "¿Tenía que hacer algo? No soy capaz de acordarme."
            call BlinkXPS3 ("c23s004_265" , "d") from _call_BlinkXPS3_1264
            kim "Te pedí que me llevaras al puerto para el trabajo que tengo esta tarde..."
            mc "¡Es verdad! ¡No me acordaba!"
            mc "Pero no sabía que tenías que ir vestida así. Me dijiste que era un trabajo de azafata y podrías pasar por una espía como [eva] y [ama]."
    $ resetWalkthrough()
    call BlinkXPS3 ("c23s004_270" , "d") from _call_BlinkXPS3_1265
    kim "Me han enviado el uniforme con una nota de que tengo que llegar vestida."
    kim "Por lo visto no hay espacio suficiente para cambiarse en el evento."
    mc "Ah, OK. ¿Cuándo quieres que vayamos?"
    call BlinkXPS3 ("c23s004_275" , "d") from _call_BlinkXPS3_1266
    kim "Debería estar allí en una hora, pero, si te va bien, me gustaría salir antes. No me gusta llegar con el tiempo justo a los sitios."
    mc "*Risa* Ningún problema. Pero deberías dar clases de puntualidad al resto de las chicas. Lo de llegar con tiempo no se les suele dar bien."
    mc "Déjame coger las llaves y la cartera, y nos podemos ir."
    call BlinkXPS3 ("c23s004_280" , "f") from _call_BlinkXPS3_1267
    "Unos minutos después, en el coche..."
    mc "Ese evento, ¿es algo de ciencia ficción o de espías? Podrías salir en una peli de ciencia ficción con ese atuendo."
    kim "No tengo ni idea. No me ha contratado el cliente final, sino la agencia de la que te hablé."
    mc "Pero ¿no deberías saber qué tienes que hacer?"
    call BlinkXPS3 ("c23s004_285" , "d") from _call_BlinkXPS3_1268
    kim "Bueno, es un trabajo de azafata. Recibir a los asistentes al evento, estar por allí en caso de que alguien necesite ayuda."
    kim "En algunos de esos eventos, incluso nos toca pasear con bandejas de comida. Odio esa parte."
    mc "¿Por qué? Tiene que ser más divertido que quedarse en la puerta esperando que lleguen asistentes con retraso."
    call BlinkXPS3 ("c23s004_290" , "d") from _call_BlinkXPS3_1269
    kim "*Risa* ¿No me conoces aún? Aeropuerto, bosque... Tengo cierta tendencia a tropezar."
    kim "Imagina esos tropiezos con una bandeja llena de canapés. *Risa* Canapés voladores..."
    mc "Y el CEO de una compañía acaba con caviar en la corbata."
    call BlinkXPS3 ("c23s004_295" , "d") from _call_BlinkXPS3_1270
    kim "Más o menos. *Risa* O Dwayne Johnston con un canapé de salmón y dos de queso en la calva."
    mc "*Risa* ¿Te pasó eso?"
    call BlinkXPS3 ("c23s004_300" , "d") from _call_BlinkXPS3_1271
    kim "*Risa* Sí. No sabía dónde meterme. Era el primer evento que hacía con gente famosa."
    mc "¿Qué pasó?"
    call BlinkXPS3 ("c23s004_305" , "d") from _call_BlinkXPS3_1272
    kim "El Sr. Johnston fue muy amable... después de lanzarme una mirada asesina. Me ayudó a levantarme y me preguntó si me había hecho daño."
    kim "Después se rio mucho cuando me ruboricé mientras le pedía disculpas. Por suerte solo le manché la cabeza y no el traje."
    mc "Con un tipo tan enorme mirándome con ganas de asesinarme, seguramente me hubiera escondido debajo de una mesa. *Risa*"
    call BlinkXPS3 ("c23s004_310" , "d") from _call_BlinkXPS3_1273
    kim "*Risa* Te aseguro que es lo primero que se me pasó por la cabeza. Hacer como el actor ese pequeñito que hace pelis con él y salir de allí gateando."
    mc "¿Kevin Heart?"
    kim "Sí, ese. ¡Me encanta ese tío! ¡Es super gracioso!"
    mc "Y sobre el evento, ¿conoces a alguna de las otra chicas? Si os ha contratado la misma agencia..."
    call BlinkXPS3 ("c23s004_315" , "d") from _call_BlinkXPS3_1274
    kim "A una de ellas, Adeline. Hemos coincidido en la agencia, pero no he trabajado nunca con ella. Va a ser la jefa esta noche."
    mc "Bueno, al menos tendrás una cara conocida. Supongo que siempre es bueno."
    call BlinkXPS3 ("c23s004_320" , "d") from _call_BlinkXPS3_1275
    kim "Depende a quién pertenezca esa cara. *Risa* En este mundillo hay muchas perras."
    kim "Y en el mundo de las modelos es peor todavía."
    mc "Me tienes que contar cómo empezaste en lo de trabajar de modelo."
    call BlinkXPS3 ("c23s004_325" , "d") from _call_BlinkXPS3_1276
    kim "Todo empezó cuando Winnie Carlow saltó a la fama. Los cazatalentos empezaron a visitar escuelas y..."
    scene black with dissolve
    "[kim] te explica todo lo que tuvo que aprender en las escuelas de modelos, sus primeros trabajos, sus primeros éxitos y fracasos..."
    "Se nota que adora su trabajo por la ilusión con la que habla de ello."
    "La conversación es tan amena que casi no te das cuenta de que ya habéis llegado al puerto, donde hay otras chicas vestidas como [kim]."
    call BlinkXPS3 ("c23s004_330" , "f") from _call_BlinkXPS3_1277
    mc "Pues ya hemos llegado. ¿Quieres que te acompañe?"
    kim "Gracias, pero no hace falta."
    scene c23s004_330d with dissolve
    kim "Aquella rubia es Adeline. De la que te he hablado antes. Mi jefa por esta noche."
    kim "Iré a presentarme al resto de chicas, y si me acompañas sería como mostrar inseguridad."
    mc "Como desees. ¿Los dos tipos que parecen guardaespaldas también pertenecen al evento?"
    scene c23s004_335AnBlink with dissolve
    kim "No lo sé. Por lo que sé, somos cinco azafatas y otras dos chicas para otros servicios. No me han dicho nada de chicos."
    kim "A lo mejor son los porteros y los han contratado en otra agencia. No tengo ni idea."
    mc "Pues eres la cuarta en llegar. Falta una cazavampiros y las dos chicas de los otros... servicios."
    call BlinkXPS3 ("c23s004_340" , "d") from _call_BlinkXPS3_1278
    kim "*Risa* Has dicho lo de servicios como si te sonara sospechoso."
    kim "Se suele llamar así a la gente del cátering, de la limpieza, etc."
    mc "Ah, OK. Al decirlo así ha sonado... *Risa* sospechoso."
    mc "¿Quieres que te venga a buscar cuando acabes?"
    call BlinkXPS3 ("c23s004_345" , "d") from _call_BlinkXPS3_1279
    kim "No hace falta. Acabará tarde y no quiero molestarte."
    mc "No es molestia. ¿Cómo volverás a casa si nadie viene a buscarte?"
    call BlinkXPS3 ("c23s004_350" , "d") from _call_BlinkXPS3_1280
    kim "Pediré un Under o a lo mejor alguna de las chicas puede llevarme."
    mc "Si tienes algún problema, no dudes en llamarme. Sea la hora que sea."
    call BlinkXPS3 ("c23s004_355" , "d") from _call_BlinkXPS3_1281
    kim "Gracias de nuevo, [mc]. Pero no te preocupes. Si tengo algún problema, te llamaré."
    call BlinkXPS3 ("c23s004_360" , "d") from _call_BlinkXPS3_1282
    kim "Ahora tengo que irme, antes de que llegue la última cazavampiros."
    mc "Suerte con el trabajo y, si te hacen pasear bandejas, que sean de canapés y no de copas de champán. *Risa*"
    call BlinkXPS3 ("c23s004_365" , "d") from _call_BlinkXPS3_1283
    kim "Muy gracioso... *Risa*"
    kim "Te veo mañana en casa."
    mc "Hasta mañana, [kim]."
    scene c23s004_370pv
    show c23s004_370v
    pause (6.0)
    scene c23s004_370dv
    "[kim] se aleja del coche con paso seguro, pasando de largo de los porteros y dirigiéndose a las cazavampiros."
    "Por primera vez, te la puedes imaginar caminando por una pasarela. Los porteros parecen tener otros pensamientos."
    stop music fadeout (1.5)
    scene black with dissolve
    hide c23s004_370v
    "Vuelves a casa y cenas con las chicas. El tema de conversación se centra en el viaje de [bet] a Monterey."
    "Que seas tú quien conduce o que [emm] vaya a cumplir su sueño de conducir un Ferrarini rosa casi no se comenta."
    "Todo el mundo está preocupado con lo que pueda pasar en la reunión de [bet]."
    return
label c23s005_MarVisit:
    if _in_replay:
        call mrS3_sca_route from _call_mrS3_sca_route_4
        call mrS3_mar_route from _call_mrS3_mar_route_4
        if mar._var("route"):
            call mrS3_mar_pregnant from _call_mrS3_mar_pregnant
            call mrS3_emm_route from _call_mrS3_emm_route_5
            if emm._var("route"):
                call mrS3_emm_hadAnal from _call_mrS3_emm_hadAnal_2
            if not sca._var("route"):
                call mrS3_edmund_story from _call_mrS3_edmund_story_3
            call mrS3_mar_lewdname from _call_mrS3_mar_lewdname
    "Después de cenar te das una ducha y bajas a la habitación de [mar]."
    play music ("music/Stardust.ogg")
    scene c23s005_005a with dissolve
    play sound ("music/knock.ogg")
    "*Knock-Knock*"
    mc "Soy yo, ¿puedo entrar?"
    mar "*A través de la puerta* Sí, entra."
    call BlinkXPS3 ("c23s005_010" , "d") from _call_BlinkXPS3_1284
    mc "Quería preguntarte por la camisa azul. ¿La has encontrado?"
    mom "Sí, la he metido en la maleta de [emm]. En una de las maletas."
    mc "*Risa* ¿Cuántas se lleva al final?"
    mc "¿Te importa si me siento?"
    call BlinkXPS3 ("c23s005_015" , "d") from _call_BlinkXPS3_1285
    mom "*Risa* Eso es algo que tendrás que descubrir mañana."
    mc "Dame sólo una pista. Si fuéramos en tu coche en vez de con la pick up, ¿cabrían?"
    call BlinkXPS3 ("c23s005_020" , "d") from _call_BlinkXPS3_1286
    mom "No. *Risa* Seguramente deberíais dejar a Tía [bet] aquí."
    mc "Vale, me hago una idea."
    mc "Por cierto, ¿qué estás leyendo? No sabía que te gustaban los cómics."
    call BlinkXPS3 ("c23s005_025" , "d") from _call_BlinkXPS3_1287
    mom "Creía que era una revista. Se llama Días de Dormitorio."
    mom "Pero creo que es de [kat]."
    call BlinkXPS3 ("c23s005_030" , "d") from _call_BlinkXPS3_1288
    mom "Un grupo de chicas en un dormitorio femenino. Ellas no tienen la suerte de tenerte a ti para ayudarlas, aunque tampoco parecen necesitarlo."
    mom "Y... ya sabes..."
    mc "Vale, un cómic lésbico."
    if persistent.lesbian:
        mc "Quizás se lo pida para echarle un vistazo."
    call BlinkXPS3 ("c23s005_035" , "d") from _call_BlinkXPS3_1289
    mom "Aparte de hablar de mis gustos literarios... *Risa* ¿Querías algo más?"
    mc "No, sólo venía por lo de la camisa. No es que tenga intención de ponérmela, pero..."
    if sca._var("route"):
        call BlinkXPS3 ("c23s005_040" , "d") from _call_BlinkXPS3_1290
        mom "Pero hoy ya has perdido una camisa y no quieres perder más. *Risa*"
        mc "*Risa* Exacto."
    mom "No te preocupes, está en la maleta de [emm]. En una de sus maletas."
    if mar._var("route"):
        call c23s005_Mar from _call_c23s005_Mar
    else:
        call c23s005_NoMar from _call_c23s005_NoMar
    return
label c23s005_NoMar:
    mc "Bueno, entonces me voy a dormir ya. Mañana nos levantamos temprano."
    mc "Te veo el viernes."
    call BlinkXPS3 ("c23s005_045" , "d") from _call_BlinkXPS3_1291
    mom "No, me levantaré para haceros el desayuno antes de que salgáis."
    mc "No te tienes que preocupar por eso."
    call BlinkXPS3 ("c23s005_050" , "d") from _call_BlinkXPS3_1292
    mom "He dicho que me levantaré y lo pienso hacer. No voy a dejar que conduzcas tres horas con el estómago vacío."
    mc "Sabes que soy capaz de prepararme un café y cortarme un trozo de tarta, ¿verdad?"
    mc "Pero bueno, no te voy a convencer de que no lo hagas. Te veo mañana."
    mom "Hasta mañana."
    stop music fadeout (1.5)
    scene black with dissolve
    "Subes a tu habitación y duermes toda la noche sin soñar..."
    centered "{size=+20}{b}DÍA 24 – JUEVES{/b}{/size}"
    call BlinkXPS3 ("c23s005_055" , "d") from _call_BlinkXPS3_1293
    play music ("music/WarIsComing.ogg")
    "... Hasta que la puerta se abre de golpe y alguien enciende la luz."
    emm "¡Despierta! ¡Nos tenemos que ir!"
    "OK. Ya estás despierto. Y sobresaltado."
    mc "¿Qué hora es, [emm]? No he oído el despertador."
    call BlinkXPS3 ("c23s005_060" , "d") from _call_BlinkXPS3_1294
    emm "Las 6:00 AM. Llevo más de una hora despierta conteniéndome para no subir a buscarte."
    emm "Pero si no te levantas ya, se va a hacer tarde."
    mc "[emm], dijimos que saldríamos de aquí a las 8:00. Había puesto el despertador a las 7:15."
    call BlinkXPS3 ("c23s005_065" , "d") from _call_BlinkXPS3_1295
    emm "Y en 45 minutos ibas a ducharte..."
    mc "Me duché anoche..."
    emm "A vestirte..."
    mc "Soy un hombre. Necesito menos de cinco minutos. Cinco minutos reales..."
    emm "Y a desayunar..."
    mc "Para eso eran 30 de los 45 minutos. *Risa*"
    mc "Puedes ir preparando el café, si quieres ir avanzando. Mamá dijo que se levantaría para hacer el desayuno."
    call BlinkXPS3 ("c23s005_070" , "d") from _call_BlinkXPS3_1296
    emm "Mamá ya está en la cocina horneando algo. El olor es lo que me ha convencido de que ya era hora de despertarte."
    mc "Vale... ¿Tía [bet] ya está despierta?"
    call BlinkXPS3 ("c23s005_075" , "d") from _call_BlinkXPS3_1297
    emm "¡No lo sé! ¡Aún no he ido a verla!"
    mc "¿A qué esperas? Es una mujer y va a tardar más en vestirse que yo."
    emm "¡Tienes razón! ¡Me voy!"
    scene c23s005_075d with dissolve
    play sound ("music/DoorSlam.ogg")
    "*Blam*"
    emm "*A través de la puerta* Todo lo tengo que hacer yo en esta casa..."
    stop music fadeout (1.5)
    mcp "(Y se fue. Bajaré a la cocina a ayudar a [mar] a preparar el desayuno.)"
    return
label c23s005_Mar:
    call BlinkXPS3 ("c23s005_080" , "d") from _call_BlinkXPS3_1298
    mom "¿Quieres quedarte a dormir?"
    mc "*Risa* Creía que no me lo ibas a pedir."
    call BlinkXPS3 ("c23s005_085" , "d") from _call_BlinkXPS3_1299
    mom "¿De verdad lo creías? Venir a preguntar por la camisa, cuando no tienes interés en ella, es la peor excusa que se te podía haber ocurrido."
    mom "Y saber que vas a estar dos días fuera cuando apenas acabas de volver de la universidad..."
    mc "Hace más de tres semanas que volví. Y no son dos días. Sólo es una noche."
    call BlinkXPS3 ("c23s005_090" , "d") from _call_BlinkXPS3_1300
    mom "Bueno, lo que sea. A una madre no le gusta perder de vista a sus polluelos aunque sea sólo por una noche."
    mc "*Risa* Y estoy seguro de que me dirás que conduzca con cuidado y que no corra por la autopista."
    call BlinkXPS3 ("c23s005_095" , "d") from _call_BlinkXPS3_1301
    mom "¡Por supuesto! *Risa* ¡Y me levantaré temprano para prepararos el desayuno!"
    mc "No hace falta, sé preparar café y coger un trozo de tarta."
    call BlinkXPS3 ("c23s005_100" , "d") from _call_BlinkXPS3_1302
    mom "Me da lo mismo. Mis dos niños se van a pasar la noche fuera y no pienso dejar que os vayáis con el estómago vacío."
    mc "Lo haces para sentirte mejor, ¿no?"
    call BlinkXPS3 ("c23s005_105" , "d") from _call_BlinkXPS3_1303
    mom "Entre otras cosas..."
    mc "Entonces estaré encantado de que nos prepares el desayuno."
    call BlinkXPS3 ("c23s005_110" , "d") from _call_BlinkXPS3_1304
    mom "¿Por qué no te pones cómodo mientras yo guardo el cómic?"
    mc "¿Guardarlo? ¿Por qué no lo dejas en la mesilla de noche?"
    call BlinkXPS3 ("c23s005_115" , "d") from _call_BlinkXPS3_1305
    mom "Estoy casi segura de que [emm] vendrá aquí si se despierta antes que yo, y no quiero que tenga ninguna idea rara."
    if persistent.lesbian and emm._var("route"):
        mom "Últimamente la he visto queriendo probar cosas nuevas..."
    mc "Si me encuentra durmiendo aquí, en lo que menos se va a fijar será en un cómic lésbico encima de tu mesilla."
    mc "Además, con lo excitada que estará, no creo que se fije ni siquiera en si estoy yo. *Risa*"
    call BlinkXPS3 ("c23s005_120" , "d") from _call_BlinkXPS3_1306
    mom "Bueno, de todas formas voy a guardarlo. No voy a leer nada más esta noche..."
    mom "Hay cosas que me apetecen más hacer que leer."
    mc "Me parece una idea prometedora... Voy a hacerte caso y a ponerme cómodo."
    call BlinkXPS3 ("c23s005_125" , "d") from _call_BlinkXPS3_1307
    mom "Yo también voy a ponerme cómoda."
    mc "Déjate puesto el collar, si no te importa. Me encanta cómo te queda."
    call BlinkXPS3 ("c23s005_130" , "d") from _call_BlinkXPS3_1308
    mom "¿Sólo el collar?"
    stop music fadeout (1.5)
    mc "Solo el collar."
    play music ("music/SexyLoungeMusic.ogg")
    call BlinkXPS3 ("c23s005_135" , "f") from _call_BlinkXPS3_1309
    "Un par de minutos después..."
    mom "Aquí estamos... Solo con el collar..."
    mc "Es un collar precioso, pero me gusta mucho más el resto de ti."
    call BlinkXPS3 ("c23s005_140" , "d") from _call_BlinkXPS3_1310
    mom "Te va a parecer una tontería..."
    mc "¿El qué?"
    call BlinkXPS3 ("c23s005_145" , "d") from _call_BlinkXPS3_1311
    mom "Quiero hacer el amor contigo esta noche..."
    mc "*Risa* No, no me parece una tontería."
    call BlinkXPS3 ("c23s005_150" , "d") from _call_BlinkXPS3_1312
    mom "*Risa* Calla y escucha..."
    call BlinkXPS3 ("c23s005_155" , "d") from _call_BlinkXPS3_1313
    mom "Cuando lo hicimos la primera vez, era como la culminación de una noche perfecta y fue mágico..."
    mom "Hoy somos como una pareja normal... no sé cómo hacerlo sin que se pierda la magia."
    mom "Sin que parezca algo programado..."
    mc "Bueno, creo que lo de pareja normal no se nos aplica demasiado."
    call BlinkXPS3 ("c23s005_160" , "d") from _call_BlinkXPS3_1314
    if persistent.family:
        mom "*Risa* Tienes razón. Nadie vería bien que me acostara con mi hijo, pero me da lo mismo."
    else:
        mom "*Risa* Tienes razón. Nadie vería bien que me acostara con el chico a quién he criado, pero me da lo mismo."
    mc "No me refiero sólo a eso. ¿Crees que las parejas normales se plantean estas cosas tan pronto?"
    mc "¿Que hablan en su segunda vez sobre no perder la magia?"
    call BlinkXPS3 ("c23s005_165" , "d") from _call_BlinkXPS3_1315
    mom "Me preocupo demasiado, ¿verdad?"
    mc "Un poco..."
    mom "Es que no quiero que se convierta en algo rutinario, en plan \"Es sábado y toca sexo\"."
    mc "Si no lleváramos una vida tan ajetreada, seguramente sería \"Es una noche cualquiera y toca sexo\"."
    mc "Llevo días queriendo bajar a dormir contigo, pero cuando no pasa una cosa, pasa otra."
    call BlinkXPS3 ("c23s005_170" , "d") from _call_BlinkXPS3_1316
    mc "O te veo cansada durante el día y quiero que tengas una buena noche de descanso."
    mom "Lo sé. Yo también he estado a punto de pedirte varias veces que vengas."
    mom "Ayer iba a subir a tu habitación pero..."
    if sca._var("route") or mc._var("edmundsStory"):
        mom "Me crucé con [sca] que iba a tu habitación en pijama."
    else:
        mom "No podía hacer el esfuerzo de subir las escaleras."
    mc "Bueno, hoy estamos aquí y nadie nos va a molestar."
    scene c23s005_895pv with dissolve
    show c23s005_895v
    mc "Y hay mucha piel pidiendo ser acariciada..."
    "En cuanto empiezas a recorrer su costado, apenas rozándola, puedes notar en la yema de tus dedos cómo a [mar] se le pone la piel de gallina."
    mom "Me encanta eso..."
    if persistent.family:
        "Tu madre se estremece cada vez que pasas tus dedos por la curva de su cadera o cuando recorres su estómago en el camino de subida a su espalda."
    else:
        "[mar] se estremece cada vez que pasas tus dedos por la curva de su cadera o cuando recorres su estómago en el camino de subida a su espalda."
    mc "Lo estoy notando. Aquella noche no tuve mucho tiempo para explorar, quiero conocer cada rincón de tu piel."
    "Un estremecimiento vuelve a recorrer el cuerpo de la hermosa mujer, esta vez provocado por tus palabras en vez de por tus dedos."
    scene c23s005_890pv with dissolve
    show c23s005_890v
    hide c23s005_895v
    mom "Me encanta que seas tan delicado siempre... Bueno, siempre que tienes que serlo."
    "Su mirada se vuelve felina por momentos, empiezas a sentirte como se debe sentir la presa de un puma. Una presa voluntaria."
    mc "Tan solo soy tan delicado como mereces en cada momento. Ni un poco más ni un poco menos."
    "Otro estremecimiento recorre su cuerpo, deseoso de caricias. Deseoso de delicadeza."
    mom "*Gemido* Pero todavía tienes mucha piel que conocer, no solo ese costado."
    mc "¿Ya te has cansado de mis caricias?"
    call BlinkXPS3 ("c23s005_175" , "d") from _call_BlinkXPS3_1317
    if persistent.family:
        mom "No, hijo mío, pero yo también quiero que acaricies toda mi piel."
    else:
        mom "No, mi amor, pero yo también quiero que acaricies toda mi piel."
    mom "*Gemido* Si no lo haces tú, tendré que empezar yo a descubrir cada rincón de la tuya."
    mc "*Risa* Hoy estás teniendo unas ideas excelentes, pero me parece que voy a seguir yo con mi exploración."
    "Otro estremecimiento más. Esta vez producido por la anticipación."
    scene c23s005_180An with fade
    "Tumbándola de espaldas, empiezas a recorrer su cuerpo con tu boca, tal como has prometido que harías."
    mom "*Gemido* Me encanta sentir tus labios sobre mi piel. *Jadeo*"
    "Y tú disfrutas explorando cada rincón de su cuerpo. Cada lugar es un nuevo descubrimiento que atesoras para más tarde."
    mc "*Smooch* Una piel fantástica que no me voy a cansar de recorrer."
    "Tomas notas mentales sobre qué zonas son más sensitivas para ella, es un conocimiento al que sacarás partido durante años."
    scene c23s005_185An with fade
    "No sólo tus labios recorren su cuerpo, sino que tus manos también lo hacen al mismo tiempo."
    mom "*Jadeo* Me estás volviendo loca... *Gemido* Y aún no has tocado lo más sensible. *Jadeo*"
    "Miente. Cada trozo de su piel es más sensible que el anterior. Cada estremecimiento es mayor que el que la ha recorrido un segundo antes."
    mom "*Gemido* Voy a necesitarte dentro... *Jadeo* No puedo aguantar más. *Gemido*"
    "Todo lo bueno se acaba. Lo mejor está por llegar."
    scene c23s005_190a with hpunch
    "[mar] te da la vuelta sin saber muy bien cómo lo ha hecho. Te tumba de espaldas y se sienta encima tuyo."
    mom "*Risita* Estar cachonda me da fuerzas. No creía que pudiera tumbarte así."
    "No tienes por qué decirle que no has opuesto ninguna resistencia. Escuchar su risa es suficiente premio por dejarte vencer."
    mc "Ahora me tienes a tu merced. ¿Qué piensas hacer con este pobre muchacho?"
    scene c23s005_190b with dissolve
    if persistent.family:
        "Mjolnir ha encontrado la perfecta posición entre los cachetes de tu madre, pareciendo indicar dónde quiere entrar hoy."
    else:
        "Mjolnir ha encontrado la perfecta posición entre los cachetes de [mar], pareciendo indicar dónde quiere entrar hoy."
    mom "Por muy tentador que sea donde estás apuntando, te quiero en el otro agujero."
    $ mar._var("analChance", True)
    if persistent.walkthrough:
        $ wt1 = _("[gr]Anal activado con [mar].")
        $ wt2 = _("[red]Anal desactivado con [mar].")
    else:
        $ wt1 = ""
        $ wt2 = ""
    menu:
        "Quizás otro día, entonces." (wt=wt1):
            $ mar._var("anal", True)
        "No es algo que me guste, no te preocupes." (wt=wt2):
            $ mar._var("anal", False)
    $ resetWalkthrough()
    call notificationS3 (0, mar) from _call_notificationS3
    if mar.name.lewd == "Mamá":
        $ mar.name.lewd = __("Mamá")
    elif mar.name.lewd != "Mom":
        $ mar.name.lewd = mar.name.firstname
    mc "Con lo que puedes hacer lo que quieras."
    scene c23s005_190An with vpunch
    mom "*GEMIDO* ¡Ooof! *JADEO*"
    call BlinkXPS3 ("c23s005_195" , "d") from _call_BlinkXPS3_1318
    if persistent.family:
        mom "*Gemido* Pues si es lo que quiera, quiero volver a tener a mi hijo dentro de mí. *Jadeo*"
    else:
        mom "*Gemido* Pues volver a tener a Mjolnir dentro de mí me parece la mejor idea."
    mc "*Risa* Una de las mejores ideas que has tenido."
    call BlinkXPS3 ("c23s005_200" , "d") from _call_BlinkXPS3_1319
    mom "¿Quieres que empiece a moverme?"
    mc "Cuando estés lista. ¿Necesitas un poco de tiempo para acostumbrarte?"
    call BlinkXPS3 ("c23s005_205" , "d") from _call_BlinkXPS3_1320
    if persistent.family:
        mom "No, te llevé dentro nueve meses. No necesito volver a acostumbrarme."
    else:
        mom "No hace falta. Quiero notarte antes de que me abras de par en par."
    mom "Casi me corro cuando has entrado..."
    mc "¿Tan rápido?"
    mom "Tus caricias y tus besos me han dejado muy cerca..."
    scene c23s005_915pv with dissolve
    show c23s005_915v
    hide c23s005_890v
    "[mar] empieza un movimiento rítmico, dejando que Mjolnir solo entre y salga unos centímetros, concentrando sus músculos en aprisionar tu glande."
    if persistent.family:
        mom "*Gemido* ¿Te gusta así, hijo mío? *Jadeo* ¿Te gusta volver al lugar de dónde saliste? *Gemido*"
    else:
        mom "*Gemido* ¿Te gusta así, mi amor? *Jadeo* ¿Te gusta estar dentro de mí? *Gemido*"
    "Te cuestionas si es una pregunta trampa por un momento. ¿Cómo puede dudar de si te gusta?"
    mc "Me encanta, [mar.name.lewd]. Ese ritmo es perfecto."
    if persistent.family:
        "Todo en ella es perfecto, no sólo el ritmo. Y el fetiche que ha desarrollado con el incesto sólo lo hace mejor."
    else:
        "Todo en ella es perfecto, no sólo el ritmo. Y el fetiche que ha desarrollado con el pseudo incesto sólo lo hace mejor."
    scene c23s005_925pv with dissolve
    show c23s005_925v
    hide c23s005_915v
    if persistent.family:
        "Tu polla entra y sale del coño de tu madre siguiendo su ritmo mientras tu acompasas tus caderas a las suyas."
        mom "*Jadeo* No sé por qué hemos dejado pasar tantos días desde la última vez. *Gemido* Me estoy volviendo adicta a la polla de mi hijo. *Jadeo*"
    else:
        "Tu polla entra y sale del coño de [mar] siguiendo su ritmo mientras tu acompasas tus caderas a las suyas."
        mom "*Jadeo* No sé por qué hemos dejado pasar tantos días desde la última vez. *Gemido* Me estoy volviendo adicta a tu polla. *Jadeo*"
    "La adicción es mutua. No crees que haya grupos de apoyo para [mar]-colicos Anónimos. Tampoco los necesitas. Es una adicción que no quieres dejar."
    mom "*Gemido* Parece que hayan pasado meses y fue tan solo hace unos días. *Jadeo* Ese es el efecto que provocas en mí. *Gemido*"
    "Atrás queda el tiempo en que [mar] tenía dudas sobre vosotros. La intimidad ya no es un problema para ella."
    scene c23s005_920pv with dissolve
    show c23s005_920v
    hide c23s005_925v
    "Ahora es todo más íntimo. Ya no es la salvaje y ansiosa cabalgata del primer día intentando llegar al orgasmo lo antes posible."
    mom "*Jadeo* Eres lo mejor que me ha pasado nunca. *Jadeo* Te quiero. *Jadeo*"
    "Hoy hay más tranquilidad en vuestros movimientos. Ambos queréis hacer que el primer asalto se prolongue. No es una carrera."
    mc "Yo también te quiero, [mar.name.lewd]. Y tú eres lo mejor."
    "Parece que habéis llegado a un acuerdo tácito sin tener que hablarlo. No necesitáis impresionaros el uno al otro. Ya no."
    scene c23s005_930pv with dissolve
    show c23s005_930v
    hide c23s005_920v
    if persistent.family:
        "Ya no es necesario que tu madre te diga lo que le gusta. Aquella primera noche aprendiste a leer sus movimientos y sus expresiones."
    else:
        "Ya no es necesario que [mar] te diga lo que le gusta. Aquella primera noche aprendiste a leer sus movimientos y sus expresiones."
    mom "*Gemido* Me estoy acercando... *Jadeo*"
    "Y su expresión corrobora sus palabras. Sabes que ella está a punto, y estás preparado para tomar el control en cuanto ella lo pierda."
    mc "Córrete para mí, [mar.name.lewd]. Déjate ir."
    "También sabes que no es necesario que se lo pidas. Aunque quisiera no va a poder contener el clímax que está llamando a las puertas. A punto de derribarlas."
    call OrgasmXS3 ("c23s005_210") from _call_OrgasmXS3_35
    mom "*GEMIDO* ¡SÍ! *JADEO* ¡Por el amor de Dios! *GEMIDO*"
    "El coño de [mar] estruja toda la longitud de tu polla que tiene dentro antes de relajarse por un segundo."
    "Un momento después vuelve a exprimirte."
    "No quiere dejarte ir. Tu no quieres salir."
    scene c23s005_905pv with fade
    show c23s005_905v
    hide c23s005_930v
    "Aprovechas que sus movimientos pierden fluidez para tumbarla en la cama y seguir bombeando."
    mom "*GEMIDO* ¡ASÍ SÍ! *JADEO* ¡NO IBA A AGUANTAR MUCHO MÁS ARRIBA! *GEMIDO*"
    "Lo sabes."
    mom "*JADEO* ¡ME ENCANTA! *GEMIDO*"
    "Vuestros movimientos se vuelven a sincronizar en el momento en que [mar] ya no tiene que aguantar su propio peso."
    scene c23s005_900pv with dissolve
    show c23s005_900v
    hide c23s005_905v
    "Tu polla entra y sale de su húmedo coño, que sigue presentando batalla oleada tras oleada, como si fuera tu hogar."
    mom "*GEMIDO* Así tocas puntos que no tocabas antes. *Respiración entrecortada* ¡ES INCREÍBLE! *GEMIDO*"
    "Tu glande golpea en sus paredes antes de deslizarse por ellas hasta su cérvix. La sensación es totalmente diferente a la postura anterior."
    mom "*GEMIDO* ¡ME ENCANTA TENERTE DENTRO DE NUEVO! *GEMIDO*"
    mc "Estoy a punto de llegar, [mar.name.lewd]."
    scene c23s005_910pv with dissolve
    show c23s005_910v
    hide c23s005_900v
    "Su coño se aprieta más aún al escuchar tus palabras. Sabes lo que va a decir antes de que su boca empiece a moverse."
    if persistent.pregnancy and not mar._var("pregnant"):
        mom "*GEMIDO* ¡CÓRRETE DENTRO! *JADEO* ¡DÉJAME EMBARAZADA ESTA VEZ! *GEMIDO*"
        "Tras la decepción de su prueba de embarazo negativa, sabías lo que te iba a pedir. También se está volviendo adicta a tus corridas."
    else:
        mom "*GEMIDO* ¡CÓRRETE DENTRO! *JADEO*"
        "Conociendo su adicción por tus corridas, sus palabras eran fácilmente previsibles."
    mom "*GEMIDO* ¡No quiero desperdiciar ni una gota! *GEMIDO*"
    "Tampoco quieres que ni una gota caiga fuera de su destino. Tu corrida es inminente."
    if persistent.pregnancy and not mar._var("pregnant"):
        if persistent.walkthrough:
            $ wt1 = _("[mar] embarazada.")
            $ wt2 = _("Sin consecuencias.")
        else:
            $ wt1 = ""
            $ wt2 = ""
        menu:
            "Correrte dentro" (wt = wt2):
                pass
            "Correrte dentro. Ir a por el bebé." (wt = wt1):
                $ mar._var("pregnant", True)
                $ mar._var("undiscoveredPregnancy", True)
                play sound ("music/OldMusicBox5.ogg")
    $ resetWalkthrough()
    call OrgasmXS3 ("c23s005_215") from _call_OrgasmXS3_36
    hide c23s005_910v
    mc "¡Mpfft!"
    if persistent.family:
        "Descargas el contenido de tus pelotas en el interior de tu madre, coincidiendo... o provocando... un nuevo orgasmo en la hermosa mujer."
    else:
        "Descargas el contenido de tus pelotas en el interior de [mar], coincidiendo... o provocando... un nuevo orgasmo en la hermosa mujer."
    mom "*GEMIDO* ¡ESTÁ SUPER CALIENTE! *JADEO* ¡ESTO ES LO MEJOR! *GEMIDO*"
    "Su coño estruja tu polla otra vez. Ahora más intensamente, intentando sin éxito que toda tu semilla se quede en su interior."
    mc "Te quiero, [mar]."
    stop music fadeout (1.5)
    if mar.name.firstname == "Martha":
        scene c23s005_215An
        pause (4.1)
    call BlinkXPS3 ("c23s005_220" , "f") from _call_BlinkXPS3_1321
    play music ("music/Fragile-Beauty.ogg")
    mom "Y yo a ti también, mi amor."
    "Caéis rendidos sobre el colchón, con tu polla aún en su interior, taponando la salida de tu semen."
    mom "¿Siempre va a ser así?"
    mc "¿A qué te refieres?"
    call BlinkXPS3 ("c23s005_225" , "d") from _call_BlinkXPS3_1322
    mom "No sé... *Risa* ¿Maravilloso? ¿Increíble? ¿A que me dejes destrozada pero a la vez con ganas de repetir?"
    mc "Espero que sí. *Risa* Y será aún mejor tal como nos vayamos adaptando el uno al otro y descubriendo que posturas nos gustan."
    call BlinkXPS3 ("c23s005_230" , "d") from _call_BlinkXPS3_1323
    mom "¡Todas! *Risa* ¡Contigo me gustan todas las posturas!"
    mc "Pero... ¿todas por igual?"
    call BlinkXPS3 ("c23s005_235" , "f") from _call_BlinkXPS3_1324
    "[mar] se desempala de Mjolnir y se da la vuelta para mirarte."
    mom "No, tienes razón. Lo que me hiciste la última vez, con la pierna levantada, sigue siendo mi favorita."
    mom "Pero eso no significa que tengamos que descartar el resto. Ya te digo que me gustan todas."
    mc "Ni probar nuevas. Puede que la siguiente que probemos se convierta en tu favorita."
    call BlinkXPS3 ("c23s005_240" , "d") from _call_BlinkXPS3_1325
    mom "Me gusta cómo piensas. *Risa* Además así seguro que no caemos en la rutina y nos convertimos en una pareja que siempre lo hace igual."
    mc "Bueno, creo que lo de caer en la rutina no va con nosotros. Hay tantas cosas que quiero probar contigo..."
    call BlinkXPS3 ("c23s005_245" , "d") from _call_BlinkXPS3_1326
    mom "¿Como qué?"
    call BlinkXPS3 ("c23s005_250" , "d") from _call_BlinkXPS3_1327
    mom "..."
    call BlinkXPS3 ("c23s005_255" , "d") from _call_BlinkXPS3_1328
    mom "*Risa* ¡Parezco una virgen ansiosa! Acabamos de terminar y ya quiero saber qué vamos a hacer la próxima vez."
    mc "O en el segundo asalto. *Risa*"
    call BlinkXPS3 ("c23s005_260" , "d") from _call_BlinkXPS3_1329
    mom "No va a haber segundo asalto, mi amor. Tienes que levantarte pronto y..."
    call BlinkXPS3 ("c23s005_265" , "d") from _call_BlinkXPS3_1330
    mom "*Susurrando* Ahora mismo estoy demasiado sensible... me has destrozado un poco."
    mc "Bueno, lo de levantarme pronto no es excusa. Son menos de tres horas de coche."
    mc "Puedo dormir en el coche mientras Tía [bet] tiene la reunión."
    call BlinkXPS3 ("c23s005_270" , "d") from _call_BlinkXPS3_1331
    mom "¿Qué va a hacer [emm] mientras tanto? No le dejarás que se suba al coche y empiece a conducir como una loca por Monterey, ¿verdad?"
    mc "*Risa* No te preocupes. Es una sorpresa para ella, pero le he contratado un curso de conducción segura."
    mc "Se pasará las primeras tres horas con un instructor en un circuito cerrado. Así podrá exprimir el coche."
    mc "Tiempo suficiente para la reunión de Tía [bet] y para que vaya al motel a dejar las maletas."
    call BlinkXPS3 ("c23s005_275" , "d") from _call_BlinkXPS3_1332
    mom "Bien pensado. Nunca le he visto el interés a los deportivos si no puedes correr en una carretera."
    mc "Yo tampoco. Seguramente me arruinaría en multas de exceso de velocidad si tuviera uno. Supongo que pisas el acelerador y ni te das cuenta..."
    if not mar._var("anal"):
        call c23s005_sleep from _call_c23s005_sleep
        call c23s005_Emm from _call_c23s005_Emm
        return
    play music ("music/Sexy-Background-Music.ogg")
    call BlinkXPS3 ("c23s005_280" , "d") from _call_BlinkXPS3_1333
    mom "¿Tienes sueño?"
    mc "No, ¿y tú?"
    call BlinkXPS3 ("c23s005_285" , "d") from _call_BlinkXPS3_1334
    mom "No..."
    mc "*Risa* Conozco esa mirada. ¿En qué estás pensando?"
    call BlinkXPS3 ("c23s005_290" , "d") from _call_BlinkXPS3_1335
    mom "En el segundo round..."
    mc "¿Estás segura? ¿No has dicho que te había destrozado?"
    call BlinkXPS3 ("c23s005_295" , "d") from _call_BlinkXPS3_1336
    mom "Bueno... has dicho que quizás querrías probar por detrás algún día..."
    mom "¿Te apetecería hoy?"
    mc "¡Sí!... Digo... Sí, si tú quieres."
    call BlinkXPS3 ("c23s005_300" , "d") from _call_BlinkXPS3_1337
    mom "*Risa* ¡Qué mal se te da disimular el entusiasmo!"
    mc "¿Entusiasmo? ¿Yo? *Risa*"
    call BlinkXPS3 ("c23s005_305" , "d") from _call_BlinkXPS3_1338
    mom "¿Va a dolerme?"
    mc "¿No lo has probado nunca?"
    call BlinkXPS3 ("c23s005_310" , "d") from _call_BlinkXPS3_1339
    mom "No. Con tu padre nunca me apeteció por mucho que insistiera."
    if emm._var("hadAnal"):
        mom "Pero desde que [emm] comentó lo del plug ayer, me lo he estado pensando."
        mc "Es verdad, dijiste que no tenías experiencia."
    call BlinkXPS3 ("c23s005_315" , "d") from _call_BlinkXPS3_1340
    mom "Cuando Mjolnir se ha puesto ahí... he pensado que estaría bien probarlo algún día."
    mc "Intentaré ser todo lo cuidadoso que pueda para que te duela lo menos posible."
    call BlinkXPS3 ("c23s005_320" , "d") from _call_BlinkXPS3_1341
    mom "Vale, dime cómo me tengo que poner. Me está apeteciendo mucho hacer esto contigo."
    if persistent.walkthrough:
        $ wt1 = _("Beso negro.")
        $ wt2 = _("Sin consecuencias.")
    else:
        $ wt1 = ""
        $ wt2 = ""
    menu:
        "Vamos a lubricarte." (wt=wt1):
            $ mar._var("rimjob", True)
        "Voy a meterte un dedo." (wt=wt2):
            $ mar._var("rimjob", False)
    $ resetWalkthrough()
    mc "Ponte ahí, con las manos apoyadas en la pared."
    scene c23s005_320d with dissolve
    mom "¿Así?"
    mc "Así estás perfecta."
    if mar._var("rimjob"):
        scene c23s005_325An with hpunch
        mom "¿QUÉ?"
        mc "¿Sorprendida? ¿Qué creías que iba a hacer?"
        call BlinkXPS3 ("c23s005_330" , "d") from _call_BlinkXPS3_1342
        mom "No sé... meter un dedo o algo, no tu lengua..."
        mc "¿Te parece desagradable? Puedo parar si quieres..."
        mc "Lo del dedo iba a venir después."
        call BlinkXPS3 ("c23s005_335" , "d") from _call_BlinkXPS3_1343
        mom "No, desagradable no... creo que ha sido la sorpresa de no saber qué esperar. Puedes seguir si quieres."
        mc "Si no te gusta, dímelo y pararé."
        scene c23s005_885pv with dissolve
        show c23s005_885v
        "Empiezas a pasar tu lengua por su estrecho agujero. Es en estos momentos en los que adoras la costumbre familiar de ducharos antes de dormir."
        mom "*Jadeo* Se nota totalmente diferente que cuando me comes el coño. *Jadeo*"
        mc "*Slurp* {i}(Es que es totalmente diferente, mi amor.){/i}"
        "El olor a jabón de su limpísimo ano se mezcla con los efluvios que brotan de su coño por los orgasmos anteriores. Es una combinación perfecta."
        mom "*Gemido* Me está empezando a gustar... *Jadeo*"
        mc "*Slurp* {i}(Hagamos que tu pérdida de virginidad anal sea lo más placentera posible.){/i}"
        "Los movimientos de [mar], buscando tu lengua con su culo son cada vez más ansiosos."
        scene c23s005_880pv with dissolve
        show c23s005_880v
        hide c23s005_885v
        "Abandonas los alrededores de su ano para introducir tu lengua dentro."
        mom "*GEMIDO* ¡Ooof! *JADEO* ¡Eso no me lo esperaba! *GEMIDO* Me gusta... *Jadeo*"
        "Penetras su ano con tu lengua, dando vueltas y expandiéndolo poco a poco. Preparándolo para lo que vendrá después."
        mom "*JADEO* Sé que tu lengua es mucho más pequeña que tu polla. *GEMIDO* Pero creo que me va a gustar. *JADEO* Ya estoy lista. *GEMIDO*"
        "Sabes que no está lista, pero ahora viene la siguiente fase."
        scene c23s005_320e with dissolve
        hide c23s005_880v
        mom "*JADEO* ¿Qué? ¿Por qué paras?"
        mc "Ahora viene lo del dedo."
        call BlinkXPS3 ("c23s005_340" , "d") from _call_BlinkXPS3_1344
        mom "¿Crees que es necesario? Me parecía que ya me habías abierto suficiente con la lengua."
        mc "Es necesario. Confía en mí."
        mom "Confío en ti, mi amor."
    scene c23s005_345a with dissolve
    "Apoyas un dedo contra su ano después de chupártelo para humedecerlo. Nunca hay suficiente humedad la primera vez."
    mc "¿Preparada?"
    mom "Sí, hazlo ya."
    scene c23s005_345An1 with dissolve
    "Introduces tu dedo un poco, esperando no hacerle mucho daño."
    mom "*Gemido* ¡Ooof! *Gemido*"
    mc "¿Bien por ahora?"
    mom "Sí, no te preocupes. Tenías razón, era necesario."
    mc "Voy a seguir."
    scene c23s005_345An2 with dissolve
    "Acabas de meter el dedo dentro del culo de [mar] hasta donde te atreves. Ella aprieta su esfínter con fuerza a tu alrededor."
    mom "*JADEO* ¿Ya está todo dentro?"
    mc "Sí, [mar.name.lewd]. Ahora voy a empezar a moverlo. ¿Preparada?"
    mom "Sí, cuando quieras."
    scene c23s005_345An3 with dissolve
    "Empiezas a introducir y a sacar tu dedo suavemente, intentando dar de sí su virgen ano sin hacerle sentir dolor."
    mc "¿Va bien así, [mar.name.lewd]?"
    mom "*Gemido* Sí, noto cómo me amoldo a tu dedo cada vez más. *Jadeo*"
    mc "Déjame hacerlo un poco más y ya estarás lista. Sobre todo recuerda que tienes que relajar los músculos."
    call BlinkXPS3 ("c23s005_350" , "d") from _call_BlinkXPS3_1345
    "Al cabo de unos segundos..."
    mom "*GEMIDO* O paras ya o me voy a correr con mi primera paja anal. *JADEO*"
    mom "*JADEO* Quiero probar lo que se siente al tenerte dentro. *GEMIDO*"
    mc "Como quieras. Creo que ya estás lista. Ponte de rodillas en la cama."
    call BlinkXPS3 ("c23s005_355" , "f") from _call_BlinkXPS3_1346
    "Tras unas instrucciones y cambios de posición, apoyas tu glande contra su ano."
    mc "Cuando estés lista."
    mom "*Gemido* Me has puesto tan cachonda que lo quiero todo y lo quiero ya. *Jadeo*"
    mc "Pero..."
    mom "*Jadeo* Sin peros. No aguanto más. *Gemido*"
    scene c23s005_970An with hpunch
    "Cuando empiezas a penetrarla con cuidado, ella empuja su culo hacia ti, empalándose en Mjolnir."
    mom "*JADEO* ¡OOOF! *GEMIDO* ¡Se nota más grande de lo que esperaba! *JADEO* ¡Me acabas de romper el culo!"
    if persistent.family and emm._var("route"):
        "Por fin has descubierto de dónde ha heredado [emm] sus métodos."
    elif emm._var("route"):
        "Por fin has descubierto dónde ha aprendido [emm] sus métodos."
    mc "Puedo esperar tanto tiempo como quieras. No hay ninguna prisa. Relaja los músculos y mejorará."
    mom "No, no. Empieza a moverte. No ha sido {b}excesivamente{/b} malo. Me olvidé de relajarme."
    "Su culo empieza a relajarse pero, pese a todo, posiblemente sea el sitio más estrecho donde has estado nunca."
    scene c23s005_965pv with dissolve
    show c23s005_965v
    "Empiezas a mover tus caderas, con la intención de hacerlo lentamente."
    mom "*GEMIDO* ¿Así? *JADEO* ¡OOOF! *GEMIDO*"
    if persistent.family:
        "El culo de tu madre no te permite ninguna lentitud. Cobra vida propia y se mueve para empalarse profundamente en tu polla a cada embestida."
    else:
        "El culo de [mar] no te permite ninguna lentitud. Cobra vida propia y se mueve para empalarse profundamente en tu polla a cada embestida."
    mc "Vas un poco rápido para ser tu primera vez..."
    "Su esfínter, cada vez más relajado, sigue igual de estrecho y masajea toda la longitud de tu polla hasta la base."
    mom "*JADEO* Le estoy pillando el ritmo. *GEMIDO* ¡Y me encanta! *JADEO*"
    scene c23s005_970pv with dissolve
    show c23s005_970v
    hide c23s005_965v
    "Su culo impacta contra tu pelvis mientras aprieta toda la longitud de tu polla en una maravillosa danza de placer."
    if emm._var("hadAnal"):
        mom "*GEMIDO* Ahora entiendo por qué a [emm] le gustó tanto. *GEMIDO*"
    mom "*JADEO* Entiendo por qué a tantas mujeres les encanta esto. *GEMIDO*"
    "Sus gemidos suben de volumen tal como su cuerpo se va amoldando al tuyo, encajando perfectamente el uno con el otro."
    mom "*GEMIDO* No voy a esperarte para correrme. *JADEO* No voy a poder contenerlo. *GEMIDO*"
    "Lo que menos te importa ahora mismo es que te espere o no. Lo que más te satisface es que habéis encontrado una nueva forma de placer compartido."
    scene c23s005_960pv with dissolve
    show c23s005_960v
    hide c23s005_970v
    "Sus movimientos continúan siguiendo los tuyos a la perfección, pese a que puedes notar cómo sus músculos empiezan a tensarse."
    mom "*JADEO* ¡Sigue así! *GEMIDO* ¡Va a ser un orgasmo increíble! *GEMIDO* ¡NO ME LO PUEDO CREER! *JADEO*"
    if persistent.family:
        "El culo de tu madre se tensa a la par que el resto de ella, haciendo que entrar y salir de su estrecho agujero sea más placentero todavía."
    else:
        "El culo [mar] se tensa a la par que el resto de ella, haciendo que entrar y salir de su estrecho agujero sea más placentero todavía."
    mom "*GEMIDO* ¡ME VOY A CORRER! *JADEO* ¡PASE LO QUE PASE, NO PARES! *GEMIDO*"
    mc "Córrete para mí, [mar.name.lewd]."
    call OrgasmXS3 ("c23s005_360") from _call_OrgasmXS3_37
    mom "*JADEO* ¡SÍ! *GEMIDO* ¡ME CORROOOO! *JADEO* ¡SIGUE! *GEMIDO* ¡MÁS! *JADEO*"
    "La hermosa mujer se derrumba sobre el colchón cuando un intenso orgasmo recorre su cuerpo, arrastrándote con ella."
    mom "*GEMIDO* ¡NO PARES! *JADEO*"
    mc "¿Estás bien?"
    call BlinkXPS3 ("c23s005_365" , "d") from _call_BlinkXPS3_1347
    mom "*GEMIDO* ¡No es el momento de comportarte como un caballero! *JADEO* ¡TE HE DICHO QUE NO PARES!"
    scene c23s005_975pv with dissolve
    show c23s005_975v
    hide c23s005_960v
    "Retomas el control y las embestidas. En esta posición entras mucho más profundamente en los intestinos de [mar]."
    mom "*JADEO* ¡ESTA POSICIÓN ME GUSTA MUCHO MÁS! *GEMIDO*"
    "Su cuerpo no tarda en acompasarse con el tuyo, produciéndoos a ambos un increíble placer. Tu polla parece hecha para su culo."
    mom "*GEMIDO* ¡SIGUE ASÍ! *JADEO*"
    "Notas cómo sus orgasmos reverberan por todo su cuerpo, produciendo que su esfínter se tense y se distienda cada pocos segundos."
    scene c23s005_985pv with dissolve
    show c23s005_985v
    hide c23s005_975v
    "Esos ciclos en los que aprieta tu polla como si su vida dependiera de ello para después soltarla, aunque sólo sea un poco, son maravillosos."
    mom "*JADEO* ME PONE CACHONDÍSIMA VERNOS EN EL ESPEJO. *GEMIDO*"
    mc "A mí también, [mar.name.lewd]. Estoy a punto de correrme."
    "Has estado observándoos desde el principio, disfrutando de unas vistas privilegiadas en las que podías disfrutar de cada cambio en su lenguaje corporal."
    mom "*GEMIDO* ¡SIGUE DESTROZÁNDOME EL CULO! *JADEO* ¡CÓRRETE DENTRO! *GEMIDO*"
    "Tu capullo, sensible de la corrida anterior, puede contar cada uno de los pliegues de su intestino mientras su ano sigue intentando aprisionarte."
    call OrgasmXS3 ("c23s005_370") from _call_OrgasmXS3_38
    mc "¡Mpfft!"
    if persistent.family:
        "Tu clímax llega de golpe. Has notado cómo se iba generando poco a poco, pero llega como una explosión que llena los intestinos de tu madre."
    else:
        "Tu clímax llega de golpe. Has notado cómo se iba generando poco a poco, pero llega como una explosión que llena los intestinos [mar]."
    call OrgasmXS3 ("c23s005_375") from _call_OrgasmXS3_39
    if persistent.family:
        mom "*JADEO* ¡SÍ! *GEMIDO* ¡LLÉNAME! *JADEO* ¡LLENA EL CULO DE TU MADRE CON TU SEMEN! *GEMIDO*"
    else:
        mom "*JADEO* ¡SÍ! *GEMIDO* ¡LLÉNAME! *JADEO* ¡LLÉNAME EL CULO CON TU SEMEN! *GEMIDO*"
    "Al recibir tu descarga, otro enorme orgasmo recorre el cuerpo de la mujer que yace debajo tuyo."
    scene c23s005_980pv with dissolve
    show c23s005_980v
    hide c23s005_985v
    "Tras descargar en su culo, reemprendes las embestidas. Los espasmos de [mar] te intentan ordeñar hasta la última gota de leche."
    mom "*GEMIDO* ¡NO VOY A PODER SENTARME EN DÍAS! *JADEO* ¡VALE LA PENA! *GEMIDO*"
    "Su cuerpo, pese a todos sus orgasmos, sigue acoplándose con el tuyo a la perfección, pero cada vez os cuesta más aguantar el ritmo."
    mom "*JADEO* ¡ME ENCANTA! *GEMIDO*"
    "Vuestra resistencia está llegando a su fin, hasta que te quedas inmóvil en su interior."
    call BlinkXPS3 ("c23s005_375b" , "d") from _call_BlinkXPS3_1348
    hide c23s005_980v
    stop music fadeout (1.5)
    mom "*GEMIDO* ¡Por el amor de Dios! *Jadeo* ¡Ha sido increíble!"
    play music ("music/SaveMe.ogg")
    mc "¿Qué tal tu primera experiencia?"
    mom "*Gemido* No quería que acabara... pero por otro lado... casi demasiado intensa."
    call BlinkXPS3 ("c23s005_380" , "d") from _call_BlinkXPS3_1349
    mom "¿Nos podemos tumbar? Me encanta tenerte dentro, pero... pesas un poco..."
    mc "*Risa* ¿Ya me estás llamando gordo otra vez?"
    "La risotada hace que expulses las últimas gotas de leche dentro del culo de [mar]."
    call BlinkXPS3 ("c23s005_385" , "d") from _call_BlinkXPS3_1350
    mom "*Risa* No es eso. El músculo pesa más que la grasa, y tienes un montón de músculos."
    mom "Sal de encima mío y túmbate a mi lado."
    call BlinkXPS3 ("c23s005_390" , "f") from _call_BlinkXPS3_1351
    mom "¿Te ha gustado? Para mí ha sido una pasada..."
    mc "¿Gustado? Me ha encantado. Es como crear una nueva intimidad entre nosotros."
    call BlinkXPS3 ("c23s005_395" , "d") from _call_BlinkXPS3_1352
    mom "Siempre había creído que el sexo anal era sucio... pero contigo nada lo es."
    mom "Creo que me podría atrever a cosas contigo que no se me hubieran pasado por la cabeza nunca."
    mc "Casi nada es sucio en el sexo si es consensuado y compartido."
    scene c23s005_400An with dissolve
    mom "*Bostezo* Lo estoy descubriendo. Gracias por eso..."
    mc "¿Tienes sueño?"
    call c23s005_sleep from _call_c23s005_sleep_1
    call c23s005_Emm from _call_c23s005_Emm_1
    return
label c23s005_sleep:
    call BlinkXPS3 ("c23s005_600" , "d") from _call_BlinkXPS3_1353
    mom "Se hace tarde y estoy un poco cansada. ¿Me abrazas un rato y dormimos? Aunque digas que no es necesario, tú tienes que dormir."
    mc "Sí, no tengo sueño, pero estoy seguro de que yo también me dormiré en cuanto te duermas tú."
    mc "Después de mirarte un rato, claro. Estás preciosa mientras duermes."
    call BlinkXPS3 ("c23s005_605" , "h") from _call_BlinkXPS3_1354
    mom "{b}¿Me miras mientras duermo? ¡Qué vergüenza!{/b}"
    mom "Seguro que pongo caras raras y se me cae la baba."
    mc "No te preocupes. Te acabo de decir que estás preciosa mientras duermes. Y no se te cae la baba. *Risa*"
    call BlinkXPS3 ("c23s005_610" , "d") from _call_BlinkXPS3_1355
    mom "Vale, te creo. ¿Puedo quitarme el collar ya?"
    mc "Sí, no se vaya a romper, o a clavártelo mientras duermes."
    call BlinkXPS3 ("c23s005_615" , "f") from _call_BlinkXPS3_1356
    "Unos minutos después, tras pasar por el baño..."
    mom "Buenas noches, mi amor."
    if persistent.family:
        mc "Buenas noches, Mamá."
    else:
        mc "Buenas noches, [mar.name.lewd]."
    scene c23s005_615d with dissolve
    "Vuestros labios se unen en un dulce beso de buenas noches que cierra con un broche dorado una noche perfecta."
    "Ahora te toca una de las mejores partes. Dormir abrazado a la mujer más maravillosa del mundo. Porque no hay otra mujer en el mundo."
    scene c23s005_615e with dissolve
    "Apagáis la luz y os tumbáis a dormir. Tal como has dicho, [mar] está preciosa mientras duerme."
    mom "*Voz adormilada* No me mires..."
    "No le piensas hacer caso. Es una visión que quieres grabar en tus retinas."
    scene black with fade
    "La miras hasta que, sin darte cuenta, se te cierran los ojos."
    stop music fadeout (1.5)
    "Duermes plácidamente toda la noche sin recordar tus sueños..."
    return
label c23s005_Emm:
    centered "{size=+20}{b}DÍA 24 – JUEVES{/b}{/size}"
    call BlinkXPS3 ("c23s005_655a" , "d") from _call_BlinkXPS3_1357
    "... Hasta que la puerta se abre de golpe y alguien enciende la luz."
    play music ("music/WarIsComing.ogg")
    emm "¡Despertad! ¡Nos tenemos que ir!"
    "OK. Ya estás despierto. Y sobresaltado."
    call BlinkXPS3 ("c23s005_655b" , "d") from _call_BlinkXPS3_1358
    mom "¿Qué hora es, [emm]? No he oído el despertador."
    "En algún momento, durante la noche, [mar] se ha tapado con el edredón."
    call BlinkXPS3 ("c23s005_660a" , "d") from _call_BlinkXPS3_1359
    emm "Las 6:00 AM. Llevo más de una hora despierta conteniéndome para no subir a la habitación de [mc]. Y resulta que estaba aquí."
    if emm._var("route"):
        call BlinkXPS3 ("c23s005_660b" , "d") from _call_BlinkXPS3_1360
        emm "¡Y no me habéis invitado! Pero os lo perdono porque hoy estoy emocionada con el viaje."
    emm "Pero si no os levantáis ya, se va a hacer tarde."
    mc "[emm], dijimos que saldríamos de aquí a las 8:00. Había puesto el despertador a las 7:15."
    call BlinkXPS3 ("c23s005_665a" , "d") from _call_BlinkXPS3_1361
    emm "Y en 45 minutos ibas a ducharte..."
    mc "Me duché anoche..."
    emm "A vestirte..."
    mc "Soy un hombre. Necesito menos de cinco minutos. Cinco minutos reales..."
    emm "Y a desayunar..."
    mc "Para eso eran 30 de los 45 minutos. *Risa*"
    mc "Puedes ir preparando el café, si quieres ir avanzando."
    call BlinkXPS3 ("c23s005_665b" , "d") from _call_BlinkXPS3_1362
    mom "No os preocupéis por el desayuno. Ya lo preparo yo mientras te vistes."
    mom "De todas formas mi despertador iba a sonar en 15 minutos para prepararlo."
    call BlinkXPS3 ("c23s005_670" , "d") from _call_BlinkXPS3_1363
    emm "Mamá, eres la mejor. Sabía que no ibas a dejar que nos fuéramos con sólo un trozo de tarta de ayer en el estómago."
    mc "Vale, [emm]... ¿Tía [bet] ya está despierta?"
    call BlinkXPS3 ("c23s005_675" , "d") from _call_BlinkXPS3_1364
    emm "¡No lo sé! ¡Aún no he ido a verla!"
    mc "¿A qué esperas? Es una mujer y va a tardar más en vestirse que yo."
    emm "¡Tienes razón! ¡Me voy!"
    scene c23s005_675d with dissolve
    play sound ("music/DoorSlam.ogg")
    "*Blam*"
    stop music fadeout (1.5)
    emm "*A través de la puerta* ¡Lo tengo que hacer todo yo!"
    play music ("music/What-Ive-Found.ogg")
    mc "Y se fue. Voy a vestirme y a ayudarte a preparar el desayuno."
    call BlinkXPS3 ("c23s005_680" , "d") from _call_BlinkXPS3_1365
    mom "No es necesario, puedes dormir un rato más, si quieres. ¿Te levanto dentro de 30 minutos?"
    mc "No voy a poder dormirme otra vez si no estás aquí."
    mc "Me va a faltar tu peso sobre mi pecho."
    scene c23s005_615f with dissolve
    "[mar] te besa apasionadamente por sorpresa. Te podrías acostumbrar a despertarte así todos los días."
    call BlinkXPS3 ("c23s005_685" , "d") from _call_BlinkXPS3_1366
    mom "Entonces sube a vestirte y ven a la cocina."
    scene black with dissolve
    return
label c23s006_TripToMonterrey:
    call c23s006_AfterBreakfastBetConfession from _call_c23s006_AfterBreakfastBetConfession
    call c23s006_Rent from _call_c23s006_Rent
    call c23s006_RideBetChurch from _call_c23s006_RideBetChurch
    return
label c23s006_AfterBreakfastBetConfession:
    if _in_replay:
        call mrS3_mar_route from _call_mrS3_mar_route_5
        call mrS3_emm_route from _call_mrS3_emm_route_6
        call mrS3_mee_route from _call_mrS3_mee_route_2
    scene black with dissolve
    stop music fadeout (1.5)
    scene c23s006_005a with dissolve
    "Después de desayunar bajas las {b}tres{/b} maletas de [emm] a la camioneta."
    "[bet] solo lleva una maleta pequeña, donde lleva el hábito y otras cosas más normales."
    "Tú sólo llevas tu mochila."
    play music ("music/Separation.ogg")
    call BlinkXPS3 ("c23s006_010" , "f") from _call_BlinkXPS3_1367
    mom "No corras. Conduce con cuidado. Haz un par de paradas a medio camino para descansar..."
    mc "No te preocupes, en cuanto lleguemos te llamo para decirte que hemos llegado bien. Espera la llamada alrededor de la hora de comer."
    call BlinkXPS3 ("c23s006_015" , "d") from _call_BlinkXPS3_1368
    mom "¿Tan tarde?"
    mc "Cuando lleguemos tenemos que ir a alquilar el coche y después tengo que llevar a Tía [bet]."
    mc "Mejor que la esperes tarde y te llame antes, a que la esperes pronto y me retrase."
    if mar._var("route"):
        call KissXPS3 ("c23s006_020" , "d") from _call_KissXPS3_33
        mom "Hasta mañana, mi amor."
    else:
        call BlinkXPS3 ("c23s006_010" , "d") from _call_BlinkXPS3_1369
        mom "Hasta mañana, [mc]."
    mc "No te preocupes por nada. Vamos dos adultos... y [emm]. Hasta mañana."
    call BlinkXPS3 ("c23s006_025a" , "f") from _call_BlinkXPS3_1370
    stop music fadeout (1.5)
    "Al cabo de unos minutos, sospechosamente cuando todas las maletas ya están cargadas, aparece [emm]."
    play music ("music/LifeOfAWanderingWizard.ogg")
    emm "¡Me pido el asiento de atrás! Así podré echar una cabezada por el camino."
    mc "No esperarás ir tumbada, ¿verdad?"
    call BlinkXPS3 ("c23s006_025b" , "d") from _call_BlinkXPS3_1371
    emm "Claro que sí. He dormido muy poco..."
    mcp "(Y has dejado dormir poco a los demás.)"
    emm "Y no me vengas con que si frenas de golpe me voy a caer del asiento. Conduces como una abuelita."
    mc "Era precisamente lo que te iba a decir. *Risa* Bueno, excepto lo de la abuelita."
    call BlinkXPS3 ("c23s006_030" , "d") from _call_BlinkXPS3_1372
    emm "¡Pero no puedo dormir sentada! ¡Siempre acabo con dolor de cuello y de mal humor!"
    emm "Y eso me va a estropear el día."
    mc "Lo que me extraña es que no estés de mal humor por haber tenido que levantarte temprano. *Risa*"
    call BlinkXPS3 ("c23s006_035" , "d") from _call_BlinkXPS3_1373
    emm "¡Hoy había una buena razón para hacerlo!"
    mc "Bueno, por ahí viene Tía [bet]. Ya nos podemos ir."
    scene black with dissolve
    "Tras unas cuantas despedidas más, por fin os ponéis en camino."
    "Por suerte habéis salido con tiempo. Había unas obras en la carretera antes de llegar a Atascadero que os han retrasado un poco."
    stop music fadeout (1.5)
    "Aún vais bien de tiempo."
    $renpy.sound.play("music/motor.ogg", loop=True)
    call BlinkXPS3 ("c23s006_040" , "f") from _call_BlinkXPS3_1374
    emm "¿Cómo estás, Tía [bet]? ¿Nerviosa?"
    play music ("music/i-feel-alive.ogg")
    mcp "(Extrañamente [emm] se preocupa por otras personas en un día importante para ella. ¿Habrá entendido lo que significa la empatía?)"
    call BlinkXPS3 ("c23s006_045" , "d") from _call_BlinkXPS3_1375
    bet "Sí, estoy nerviosa. No tengo ni idea de qué va a pasar en esa reunión, pero no soy capaz de encontrar ningún escenario bueno para mí."
    mc "El mejor escenario para ti sería que te destinasen a otro hospital en África, en otro país, ¿no?"
    call BlinkXPS3 ("c23s006_050" , "d") from _call_BlinkXPS3_1376
    emm "Eso no, Tía. Nadie quiere que te vayas ahora que te conocemos mejor y que la abuela se va a mudar aquí."
    mc "Pero no tenemos que ser egoístas, [emm]. Yo tampoco quiero que se vaya, pero si es lo que quiere ella..."
    call BlinkXPS3 ("c23s006_055" , "d") from _call_BlinkXPS3_1377
    bet "Gracias, chicos. Realmente aún no sé lo que quiero. Me gustaría volver a África."
    bet "Pero también me gustaría quedarme por aquí y trabajar en algún hospital que me permita veros más a menudo."
    bet "Incluso hay un par de hospitales católicos cerca de casa donde podría trabajar sin mudarme de Newport."
    mc "Eso sería fantástico. Nadie quiere que te vayas de casa, pero todos lo entenderíamos si decidieras volver a África."
    mc "Bueno, quizás todos menos [emm]. *Risa*"
    call BlinkXPS3 ("c23s006_060" , "d") from _call_BlinkXPS3_1378
    emm "*Risa* Ni siquiera que gastes bromas sobre mí va a poder estropearme el día."
    mc "Nunca querría estropearte el día, hermanita. Además, tengo una sorpresa para ti, para cuando lleguemos a Monterey."
    call BlinkXPS3 ("c23s006_065" , "d") from _call_BlinkXPS3_1379
    emm "¿Qué es?"
    mc "No te lo voy a decir. Si te lo dijera, ya no sería una sorpresa."
    call BlinkXPS3 ("c23s006_070" , "d") from _call_BlinkXPS3_1380
    emm "Decirme que tienes una sorpresa para mí y no decirme qué es... Eso sí que podría estropearme el día..."
    mc "Los chantajes emocionales no sirven conmigo, [emm]."
    call BlinkXPS3 ("c23s006_075" , "d") from _call_BlinkXPS3_1381
    bet "Pero la chica lo tenía que intentar. *Risa*"
    if emm._var("route"):
        call BlinkXPS3 ("c23s006_080" , "d") from _call_BlinkXPS3_1382
        bet "Si eso no funciona, siempre puedes amenazarle con castigarle sin sexo. *Risa* A otras mujeres les funciona."
        call BlinkXPS3 ("c23s006_085" , "d") from _call_BlinkXPS3_1383
        emm "¡Eso no! ¡Eso sería más castigo para mí que para él!"
        mc "*Risa* Además, tampoco funcionaría."
    call BlinkXPS3 ("c23s006_090" , "d") from _call_BlinkXPS3_1384
    bet "¿Y tú que quieres hacer con el coche? ¿Quieres ir a algún sitio en particular o sólo conducir donde la carretera te lleve?"
    call BlinkXPS3 ("c23s006_095" , "d") from _call_BlinkXPS3_1385
    emm "Había pensado en ir a ver Carmel, he leído que es bonito, y me gustaría hacer unas fotos."
    mc "Creo que hoy no tendremos mucho tiempo para hacer turismo."
    call BlinkXPS3 ("c23s006_100" , "d") from _call_BlinkXPS3_1386
    emm "Lo sé. Y mañana tampoco si tenemos que devolver el coche a mediodía."
    mc "Bueno, si no podemos ir a Carmel, te prometo que te llevaré un día cuando vuelva de Aruba."
    emm "Me parece bien. Y ahora voy a dormir un poco."
    mc "Pero..."
    call BlinkXPS3 ("c23s006_105" , "d") from _call_BlinkXPS3_1387
    bet "No la pongas de mal humor discutiendo con ella por una causa perdida, [mc]."
    mc "Tienes razón. Va a hacer lo que quiera..."
    call BlinkXPS3 ("c23s006_110" , "d") from _call_BlinkXPS3_1388
    emm "Exacto. *Risita* Pero te haré caso y no me tumbaré. Si das un frenazo, voy a acabar con mi cara en el culo de Tía [bet]."
    emm "Despertadme antes de llegar, o si paramos para tomar un café."
    mc "¿No vas a tener que parar para hacer pis? Siempre teníamos que parar por ti cada pocos kilómetros."
    call BlinkXPS3 ("c23s006_115" , "d") from _call_BlinkXPS3_1389
    emm "Si estoy durmiendo, no sabré si me estoy meando. *Risa* Con lo que os hago un favor echándome una siesta."
    mc "Estás aprendiendo a tener respuestas para todo."
    call BlinkXPS3 ("c23s006_120" , "d") from _call_BlinkXPS3_1390
    "[bet] y tú charláis durante unos minutos hasta que os dais cuenta de que [emm] ya no hace ningún comentario."
    mc "Ya se ha dormido, ¿no? ¡[emm.nick] mira, un tractor rosa!"
    bet "No reacciona. Está durmiendo como un tronco."
    mc "Entonces ahora podemos hablar tú y yo. No puedes huir de mí como has hecho los últimos dos días"
    call BlinkXPS3 ("c23s006_125" , "d") from _call_BlinkXPS3_1391
    bet "No he huido de ti. Tenía muchas cosas que hacer..."
    mc "Y una de ellas era esquivarme. Es culpa tuya que me haya dado cuenta."
    call BlinkXPS3 ("c23s006_130" , "d") from _call_BlinkXPS3_1392
    bet "¿Mía? ¿Por qué? ¿Qué he hecho yo?"
    mc "Me enseñaste a reconocer los síntomas cuando alguien me esquiva. Como pasó con [kia]. Como está pasando contigo."
    mc "Desde el incidente con Meemaw me estás evitando."
    if not mee._var("route"):
        call BlinkXPS3 ("c23s006_135" , "d") from _call_BlinkXPS3_1393
        bet "Bueno... fue un malentendido... "
    else:
        call BlinkXPS3 ("c23s006_135" , "d") from _call_BlinkXPS3_1394
    bet "Veros como os vi... me sorprendió mucho..."
    mc "Me di cuenta."
    call BlinkXPS3 ("c23s006_140" , "d") from _call_BlinkXPS3_1395
    bet "Pero no creo que sea el mejor momento para hablar de esto, con [emm] ahí atrás."
    mc "Está dormida como un tronco. Lo acabas de decir."
    mc "Y si me sigues evitando, nunca podemos hablarlo. Creo que en estos dos días nuestra relación ha dado un paso atrás, como si hubieras perdido confianza en mí."
    call BlinkXPS3 ("c23s006_145a" , "d") from _call_BlinkXPS3_1396
    bet "No es eso, cariño. No puedo perder la confianza en ti, no has hecho nada merecedor de ello."
    mc "Entonces explícamelo. No entiendo tu actitud de los últimos días, ni qué fue aquello de \"otra vez\" que dijiste en el baño."
    if persistent.family:
        bet "¿Qué sabes de tu abuelo?"
    else:
        bet "¿Qué sabes de John, el marido de [mee]?"
    mc "¿Qué tiene que ver él en esto? Ahora estoy confundido."
    bet "¿Qué sabes de él?"
    if persistent.family:
        mc "Lo que me han explicado Meemaw, mi madre, y [nor]. Se conocieron en la universidad, amor a primera vista, y un matrimonio feliz que acabó demasiado pronto."
    else:
        mc "Lo que me han explicado Meemaw y [nor]. Se conocieron en la universidad, amor a primera vista, y un matrimonio feliz que acabó demasiado pronto."
    mc "Y que parece que todo lo hacía bien y nunca se equivocaba en nada. Pero eso supongo que se debe a que ya no está entre nosotros."
    call BlinkXPS3 ("c23s006_145b" , "d") from _call_BlinkXPS3_1397
    bet "Sí y no. Hacía muchas cosas bien, pero también se equivocaba en muchas otras."
    bet "No, no era perfecto."
    mc "Bueno, nadie lo es. Pero una vez alguien se muere, normalmente se olvidan las cosas malas que hizo. A menos que fuera un hijo de puta."
    mc "Entonces se olvidan las buenas, si es que hizo alguna."
    call BlinkXPS3 ("c23s006_145c" , "d") from _call_BlinkXPS3_1398
    bet "No, con John no era así. De sus equivocaciones te olvidabas a los cinco minutos."
    bet "Tenía un don para que sus aciertos y éxitos pesaran mucho más que sus fallos y sus fracasos."
    call BlinkXPS3 ("c23s006_145d" , "d") from _call_BlinkXPS3_1399
    bet "Tenía un carisma especial para hacer que ni te fijaras en sus carencias o en lo que hacía mal."
    bet "Como siempre estaba haciendo cosas por los demás, todo el mundo pensaba que él no tenía problemas propios."
    bet "Tú te pareces mucho a él. Más de lo que incluso [mee] ha descubierto."
    mc "Gracias, supongo. A veces lo describís como si meara whisky y sus pedos fueran arcoíris."
    call BlinkXPS3 ("c23s006_145e" , "d") from _call_BlinkXPS3_1400
    bet "*Risa* Te puedo asegurar que sus pedos NO eran arcoíris. Sabías que había estado en una habitación horas después de que se fuera."
    bet "Bromeábamos con que no fue a Vietnam porque se le consideraba un arma química con piernas. *Risa*"
    mc "*Risa* Bueno, al menos en eso no me parezco a él... creo."
    call BlinkXPS3 ("c23s006_150" , "d") from _call_BlinkXPS3_1401
    bet "Sobre el resto, como resumen está bien. Se conocieron cuando [mee] iba a la universidad. John ya había acabado."
    bet "[mee] estaba en su tercer año en San Luis Obispo y yo acababa de empezar en Stanford."
    bet "John estaba trabajando en un pequeño estudio de arquitectura en San Francisco."
    if persistent.family:
        mc "Sigo sin entender qué tiene que ver el abuelo en todo esto."
    else:
        mc "Sigo sin entender qué tiene que ver John en todo esto."
    call BlinkXPS3 ("c23s006_155" , "f") from _call_BlinkXPS3_1402 #past
    bet "Déjame continuar y lo entenderás."
    bet "Yo conocí a John antes que [mee]. Me lo presentó un amigo común."
    mc "¿Os llevabais bien?"
    call BlinkXPS3 ("c23s006_160" , "d") from _call_BlinkXPS3_1403 #past
    bet "Nos hicimos amigos en seguida."
    bet "Teníamos un sentido del humor muy parecido, a los dos nos gustaba pasear, y salía con mi grupo de amigos los fines de semana."
    bet "Era el mayor de todos nosotros, pero eso era bueno. Arnold no había sido gobernador y la edad para beber eran 21 todavía."
    mc "¿Lo llevabais para que os comprara alcohol? *Risa*"
    call BlinkXPS3 ("c23s006_165" , "f") from _call_BlinkXPS3_1404
    bet "Eran los setenta... conseguir alcohol... y otras cosas... era fácil. *Risa* Pero sí, él nos compraba las bebidas."
    mc "*Risa* Tía [bet] en plan malota, bebiendo... y haciendo otras cosas... ilegalmente. Me hubiera gustado conocerte en aquella época."
    call BlinkXPS3 ("c23s006_170" , "f") from _call_BlinkXPS3_1405 #past
    bet "*Risa* Yo era una chiquilla divertida en aquella época. Creo que nos hubiéramos llevado bien."
    mc "Sigues siendo divertida y nos llevamos bien. No ha cambiado nada."
    call BlinkXPS3 ("c23s006_175" , "f") from _call_BlinkXPS3_1406
    bet "Excepto que tengo 46 años más que entonces..."
    mc "Bueno, la edad sólo es un número. Si te sientes joven eres joven."
    call BlinkXPS3 ("c23s006_180" , "f") from _call_BlinkXPS3_1407 #past
    bet "¡Qué fácil parece todo a tu edad!"
    bet "Pero volviendo a John..."
    bet "Nos llevábamos tan bien que empecé a ver cosas dónde no las había."
    bet "Me hacía la encontradiza con él para verlo, paseaba cerca de su trabajo, de su casa..."
    mc "Vaya, que te enamoraste como una adolescente."
    call BlinkXPS3 ("c23s006_185" , "f") from _call_BlinkXPS3_1408
    bet "*Risa triste* ¡Era una adolescente!"
    bet "Pero sí, enamorada hasta las trancas. Y un poco acosadora."
    mc "Esas cosas pasan cuando eres joven."
    call BlinkXPS3 ("c23s006_190" , "f") from _call_BlinkXPS3_1409 #past
    bet "Ya te dije que yo vivía en una caravana cerca del campus, ¿no?"
    mc "Sí, la caravana rosa de la que [emm] estaría orgullosa."
    call BlinkXPS3 ("c23s006_195" , "d") from _call_BlinkXPS3_1410 #past
    bet "Pues [mee] vino a visitarme un fin de semana, se iba a quedar a dormir en la caravana el viernes y el sábado."
    if persistent.family:
        mc "Y conoció al abuelo."
    else:
        mc "Y conoció a John."
    scene c23s006_200 with dissolve #past
    bet "Exacto. La llevé a una bar, donde había quedado con mi grupo de amigos y se la presenté a todo el mundo."
    bet "Y ahí entra lo que tú conoces. Amor a primera vista."
    bet "Él arquitecto. Ella estudiando arquitectura. Empezaron a charlar y encajaron."
    call BlinkXPS3 ("c23s006_205" , "d") from _call_BlinkXPS3_1411 #past
    bet "Parecía que el resto del mundo no existía para ellos, como si fuéramos estatuas decorativas del bar."
    bet "Se pasaron toda la noche juntos, charlando y riendo. Conociéndose."
    mc "Y tú te sentiste fatal."
    call BlinkXPS3 ("c23s006_210" , "d") from _call_BlinkXPS3_1412 #past
    bet "Sí. No quiero endulzarlo. *Risa* Me comporté como una niña celosa de mi propia hermana."
    bet "*Risa* Me pasé toda la noche pensando en mil formas de asesinar a [mee] cuando fuéramos a la caravana a dormir."
    mc "Pero no lo hiciste. *Risa* Si todos los asesinatos mentales sucedieran, no quedaría nadie en el mundo."
    call BlinkXPS3 ("c23s006_215" , "f") from _call_BlinkXPS3_1413
    bet "No lo hice porque [mee] no vino a dormir a la caravana ninguna de las dos noches."
    mc "Eso es sorprendente, viniendo de Meemaw."
    call BlinkXPS3 ("c23s006_220" , "d") from _call_BlinkXPS3_1414
    bet "Ella también era joven entonces. *Risa* Y recuerda lo del amor a primera vista."
    mc "Amor a primera vista y sexo a primer parpadeo. *Risa* Pero sigo sin entender qué tiene que ver eso con lo que pasó el otro día."
    call BlinkXPS3 ("c23s006_225" , "d") from _call_BlinkXPS3_1415
    bet "Ni [mee] ni John sabían lo que yo sentía por él. Con lo que di un paso a un lado y empecé mi descenso a los infiernos."
    mc "Así que John es quien, sin saberlo, te empujó a frecuentar esas compañías inadecuadas de las que hablaste."
    mc "Y finalmente hacerte monja..."
    call BlinkXPS3 ("c23s006_230" , "d") from _call_BlinkXPS3_1416
    bet "No, no me empujó él. Me empujó el no saber gestionar mis emociones."
    bet "Era una niña imbécil que no podía soportar ver al hombre del que me había enamorado con otra."
    bet "Y menos aún con mi hermana."
    call BlinkXPS3 ("c23s006_235" , "d") from _call_BlinkXPS3_1417
    bet "Sentía como si [mee] me lo hubiera robado. *Risa triste* No me podía robar algo que nunca fue mío, pero era como me sentía."
    mc "Te entiendo. Las comidas familiares tuvieron que ser una pesadilla para ti."
    call BlinkXPS3 ("c23s006_240" , "d") from _call_BlinkXPS3_1418
    bet "Lo fueron durante un tiempo, la boda de [mee] incluida. Después ya no."
    bet "Me alegré mucho por ellos, pero dejé de ir a esas comidas. Siempre buscaba una excusa para quedarme en Stanford."
    if persistent.family:
        bet "Eso me distanció de [mee] y de tus bisabuelos. Me sentí muy sola durante años."
    else:
        bet "Eso me distanció de [mee] y de mis padres. Me sentí muy sola durante años"
    mc "Y encontraste a la iglesia que llenó ese vacío."
    call BlinkXPS3 ("c23s006_245" , "f") from _call_BlinkXPS3_1419 #past
    bet "Sí, pero fue mucho más tarde. Me volqué en estudiar primero y en trabajar después."
    bet "Cuando acabé la carrera, mientras hacía la residencia en San José descubrí que la religión ayudaba a muchas personas a superar sus pérdidas."
    call BlinkXPS3 ("c23s006_250" , "d") from _call_BlinkXPS3_1420 #past
    bet "Empecé a ir a la iglesia y poco tiempo después lo dejé todo atrás y me hice monja. El resto ya lo sabes."
    if persistent.family:
        mc "Y todo ese tiempo estuviste enamorada del abuelo, ¿no? ¿Hasta que murió?"
    else:
        mc "Y todo ese tiempo estuviste enamorada de John, ¿no? ¿Hasta que murió?"
    call BlinkXPS3 ("c23s006_255" , "f") from _call_BlinkXPS3_1421
    bet "No tanto, pero lo estuve durante mucho tiempo."
    bet "Hasta que, a principios de los 90, me fui a África y descubrí que mis problemas eran nimiedades comparados con los del resto del mundo."
    bet "Una historia de amor no correspondido que duró más de 10 años, y en la que no hay culpables aparte de mí."
    mc "No creo que haya culpables, ni siquiera tú. Te enamoraste y lo guardaste en silencio. Otra mujer se llevó al chico."
    call BlinkXPS3 ("c23s006_260" , "d") from _call_BlinkXPS3_1422
    bet "Por eso es por lo que más culpable me sentí todos esos años. Mi cabeza estaba llena de escenarios que no pasaron."
    bet "¿Qué hubiera pasado si le hubiera dicho a John lo que sentía por él antes de presentarle a [mee]?"
    bet "¿Hubiera sido correspondida? ¿Hubiéramos durado? ¿Hubiera sido un matrimonio tan bonito como el que tuvo [mee]?"
    mc "Son cosas que no puedes saber, con lo que no tienes que pensar en eso. Solo te harás daño."
    call BlinkXPS3 ("c23s006_265" , "d") from _call_BlinkXPS3_1423
    bet "Hacía años que no pensaba en eso. Hasta que pasó lo del otro día."
    mc "Y ahí vino el \"Otra vez\". Estabas viviendo otra vez lo mismo, con la misma persona."
    if persistent.family:
        mc "Pero esta vez era yo en vez del abuelo."
    else:
        mc "Pero esta vez era yo en vez de John."
    call BlinkXPS3 ("c23s006_270" , "d") from _call_BlinkXPS3_1424
    bet "No pareces sorprendido."
    mc "No lo estoy. Empecé a sospecharlo aquel día en el que hablamos de por qué [kia] me estaba evitando."
    mc "Después de lo que pasó en el baño, has sido tú la que me evitabas."
    mc "Y tu historia me ha dado el contexto para entender el \"Otra vez\", que era la única pieza que me faltaba."
    call BlinkXPS3 ("c23s006_275" , "d") from _call_BlinkXPS3_1425
    bet "Pues ahora lo entiendes todo. Me siento estúpida."
    mc "¿Por qué?"
    call BlinkXPS3 ("c23s006_280" , "d") from _call_BlinkXPS3_1426
    bet "Por mil razones. Porque me he vuelto a enamorar de una persona que no debo."
    if persistent.family:
        bet "Porque esa persona es mi sobrino nieto."
    bet "Porque soy 1,000 años mayor que él."
    bet "Porque, aunque existiera la remota posibilidad de que quisieras estar conmigo, yo no podría porque soy monja."
    bet "Porque soy una vieja estúpida..."
    mc "Te voy a hacer dos preguntas, que es lo único que no he entendido."
    bet "Dime..."
    if persistent.family:
        mc "¿Te has enamorado de mí o del reflejo que ves del abuelo en mí?"
    else:
        mc "¿Te has enamorado de mí o del reflejo que ves de John en mí?"
    call BlinkXPS3 ("c23s006_285" , "d") from _call_BlinkXPS3_1427
    bet "¿Cuándo te has vuelto así?"
    mc "¿A qué te refieres?"
    bet "Hace dos semanas no hubieras preguntado eso. No te hubieras ni siquiera dado cuenta. Ni te lo hubieras planteado."
    mc "He tenido una buena maestra a la hora de observar cosas. No he pasado tanto tiempo contigo como me gustaría, pero el suficiente para aprender algunos trucos."
    call BlinkXPS3 ("c23s006_290" , "d") from _call_BlinkXPS3_1428
    bet "Empecé en pensar en ti de una forma inapropiada porque me recordabas a John."
    bet "Pero me he dado cuenta de que lo que me gusta de ti son las cosas que te hacen diferente a él."
    mc "Lo que significa que no era tan perfecto... pedos aparte."
    call BlinkXPS3 ("c23s006_295" , "d") from _call_BlinkXPS3_1429
    bet "*Risa* No era perfecto. Y tú tampoco lo eres, no empieces a buscar un pedestal al que subirte."
    bet "Pero tú tienes virtudes que él no tenía, y algunas que él tenía son más grandes en ti. Pero lo mismo pasa con los defectos."
    call BlinkXPS3 ("c23s006_300" , "d") from _call_BlinkXPS3_1430
    bet "Tan solo es que... tu combinación de virtudes y defectos es diferente..."
    bet "Me recuerdas mucho a él. También a [mee] se lo recuerdas. Pero no sois la misma persona."
    bet "Pero hay una segunda pregunta..."
    mc "Y esa va a ser la más complicada."
    mc "¿Cómo querrías que acabara esto? Como has dicho, eres monja."
    call BlinkXPS3 ("c23s006_305" , "d") from _call_BlinkXPS3_1431
    bet "No tengo una respuesta para esa pregunta. Y no es la pregunta que me esperaba."
    mc "¿Qué pregunta esperabas?"
    call BlinkXPS3 ("c23s006_310" , "d") from _call_BlinkXPS3_1432
    bet "No sé, algo en plan \"¿Te has vuelto loca, Tía [bet]?\" *Risa*"
    mc "¿Por qué iba a preguntarte algo así?"
    call BlinkXPS3 ("c23s006_315" , "d") from _call_BlinkXPS3_1433
    $ bet._var("chanceRoute", True)
    bet "Porque es una locura."
    bet "Que yo sienta esto y que tengamos esta conversación precisamente hoy."
    if persistent.walkthrough:
        $ wt1 = _("[gr]Ruta con [bet] pre-abierta.")
        $ wt2 = _("[red]Ruta con [bet] cerrada.\n [red]ADVERTENCIA: No habrá más oportunidades de abrir la ruta con [bet].")
    else:
        $ wt1 = ""
        $ wt2 = ""
    menu:
        "No creo que sea una locura, si dejas de ser monja." (wt=wt1):
            $ bet._var("route", True)
        "Solo es un poco locura." (wt=wt2):
            $ bet._var("route", False)
    $ resetWalkthrough()
    call notificationS3 (2, bet) from _call_notificationS3_1
    if not bet._var("route"):
        call BlinkXPS3 ("c23s006_320" , "d") from _call_BlinkXPS3_1434
        bet "Lo sé. Entre la edad, ser monja, y ni siquiera saber lo que quiero..."
        mc "Principalmente la última razón. Creo que tienes la cabeza hecha un lío ahora mismo."
        mc "Estás muy presionada con esta visita y me parece que estás buscando experiencias que viviste antes de ser monja por si tienes que dejar de serlo."
        call BlinkXPS3 ("c23s006_325" , "d") from _call_BlinkXPS3_1435
        bet "Empecé a sentir algo por ti antes de saber nada de esta visita..."
        mc "Pero esos sentimientos han crecido desde que lo sabes, ¿verdad?"
        bet "Sí..."
        mc "Hagamos un trato. Resolvamos lo de la visita al obispado y después volvemos a hablar sobre cómo te sientes. ¿Te parece bien?"
        mc "De esa forma sabrás hacia dónde va tu vida y qué quieres hacer con ella."
        call BlinkXPS3 ("c23s006_330" , "d") from _call_BlinkXPS3_1436
        bet "Me parece un buen plan. Creo que tienes razón y que la incertidumbre de este viaje me está afectando más de lo que debería."
    else:
        call BlinkXPS3 ("c23s006_340" , "d") from _call_BlinkXPS3_1437
        bet "¿Qué? Ahora el que estás loco eres tú."
        mc "No quiero influir en tu decisión sobre qué hacer hoy pero, de todos los impedimentos que has puesto, es el único que veo insalvable."
        mc "Quiero que la decisión que tomes, la tomes por ti, no por mí. No tengo ningún derecho a pedirte que dejes de ser monja y no lo voy a hacer."
        call BlinkXPS3 ("c23s006_345" , "d") from _call_BlinkXPS3_1438
        bet "¿Me estás diciendo que, si no fuera monja, estarías conmigo?"
        mc "Te estoy diciendo que, si no fueras monja, tendríamos una posibilidad de estar juntos."
        mc "Sé que no estarías a gusto si pasara mientras aún lo eres. Y no quiero que esto pese en tu decisión de qué hacer hoy."
        call BlinkXPS3 ("c23s006_350" , "d") from _call_BlinkXPS3_1439
        bet "Pero no me puedes pedir eso..."
        mc "Exacto. NO te lo estoy pidiendo."
        mc "Cuando ese secretario te diga qué opciones tienes, deberás decidir qué quieres hacer con tu vida."
        mc "Decidas lo que decidas, yo voy a apoyarte."
        mc "Y no quiero que esa decisión tenga nada que ver con esta conversación. Lo tienes que decidir por lo que quieres tú."
        call BlinkXPS3 ("c23s006_355" , "d") from _call_BlinkXPS3_1440
        bet "Estás pidiendo un imposible. ¿Cómo no voy a tener en cuenta lo que has dicho?"
        mc "Porque primero tienes que saber lo que te dicen. Después tienes que decidir qué quieres."
        mc "Si te dicen que puedes volver a África, ¿lo dejarías correr y dejarías de ser monja?"
        call BlinkXPS3 ("c23s006_360" , "d") from _call_BlinkXPS3_1441
        bet "Seguramente me arrepentiría si lo hiciera..."
        mc "Por eso tienes que decidir una vez sepas que opciones tienes. No en base a esta conversación, sino en base a lo que tú quieres hacer."
        mc "Pero si decides dejar de ser monja, porque tú quieres dejar de serlo, me gustaría que tuviéramos una oportunidad."
        scene c23s006_365An with dissolve
    mc "¿Y sabes una cosa, Tía [bet]? Pase lo que pase hoy, decidas lo que decidas, te voy a seguir queriendo. Todos lo vamos a hacer."
    call BlinkXPS3 ("c23s006_335" , "d") from _call_BlinkXPS3_1442
    bet "Gracias, [mc]. Nadie podría pedir una familia mejor."
    bet "Y sobre la familia..."
    scene c23s006_335An with dissolve
    "Pasáis los siguientes 40 minutos charlando de cómo ha cambiado la familia en los días que hace que llegaron las estudiantes, [bet] y [mee]."
    "Ninguno de vosotros podría imaginar cómo iba a evolucionar. Los dos estáis contentos de cómo lo ha hecho."
    stop music fadeout (1.5)
    "Dejáis la conversación aparcada para más adelante."
    scene c23s006_370AnBlink with dissolve
    "Cuando estáis a mitad de la ruta..."
    play music ("music/Happy-Sun.ogg")
    emm "*Bostezo* ¿Falta mucho? ¡Me estoy meando!"
    mc "*Risa* La Bella Durmiente se ha despertado y se ha convertido en La Bella Meona."
    mc "Queda poco más de una hora."
    call BlinkXPS3 ("c23s006_375" , "d") from _call_BlinkXPS3_1443
    emm "¿Podemos parar en algún bar de carretera? Os invito a desayunar de nuevo y así voy al lavabo."
    mc "*Risa* ¿Segundo desayuno? ¿Has comprobado si tienes los pies peludos?"
    call BlinkXPS3 ("c23s006_380" , "d") from _call_BlinkXPS3_1444
    bet "Creo que [emm] no va a pillar la referencia."
    mc "Yo creo que sí. Le gustan las películas de fantasía."
    call BlinkXPS3 ("c23s006_385" , "d") from _call_BlinkXPS3_1445
    emm "¡Claro que lo he pillado! Es de El Señor de los Pendientes. No es tan buena como La Novia Princesa, pero no está mal."
    emm "Y me estoy meando."
    mc "*Risa* En cinco minutos pasaremos por King City. Hay varios sitios para comer allí."
    scene black with dissolve
    stop sound
    "Paráis a desayunar de nuevo en King City. [emm] apenas llega al lavabo."
    "La única que pide un desayuno completo es [bet]. Ni siquiera la preocupación por la reunión le quita el hambre."
    stop music fadeout (1.5)
    return
label c23s006_Rent:
    if _in_replay:
        call mrS3_emm_route from _call_mrS3_emm_route_7
    call BlinkXPS3 ("c23s006_400" , "f") from _call_BlinkXPS3_1446
    "Finalmente llegáis a la agencia de alquiler de coches..."
    play music ("music/Looking-Forward.ogg")
    emm "¡Es precioso! ¡Pink Dreams! ¡Es un sueño hecho realidad!"
    mc "Vamos antes de que me empiecen a sangrar los ojos con tanto rosa."
    emm "¡Qué poco gusto!"
    scene c23s006_405a with fade
    "Amber" "Hola, buenos días, soy Amber. ¿En qué puedo ayudarles?"
    mc "Teníamos una reserva para un Ferrarini rosa. A nombre de [mc] Marks."
    mcp "(¡Qué forma de destrozar esos coches pintándolos de rosa!)"
    scene c23s006_410a with dissolve
    "Amber mira directamente a [bet]."
    "Amber" "He mirado el expediente y he visto que también ha contratado las clases de conducción segura para deportivos con nuestro instructor Chad."
    "Amber" "En breve estará aquí. Justo a tiempo para que, cuando acabemos el papeleo, la pueda llevar a comer. La comida está incluida en el curso."
    call BlinkXPS3 ("c23s006_415" , "d") from _call_BlinkXPS3_1447
    emm "¿Unas clases de conducción de deportivos? ¿Esa era la sorpresa? ¡Eres el mejor hermano del mundo!"
    mc "Conducción {b}segura{/b} de deportivos."
    scene c23s006_405An with dissolve
    "Amber mira alternativamente a [emm] y a [bet] como si no entendiera nada."
    "Amber" "Perdón por la confusión. Esas clases las suelen contratar señoras... más maduras. Muchas de ellas repiten el curso."
    mc "En este caso, las lecciones son un regalo para mi hermana."
    call BlinkXPS3 ("c23s006_420" , "d") from _call_BlinkXPS3_1448
    emm "No veo el Ferrarini aquí. ¿Dónde está? ¿Qué modelo es? ¿Podemos ir a verlo?"
    mc "Veo que estás impaciente."
    scene c23s006_405c with fade
    "Amber" "Sí, podemos ir a verlo antes de hacer el papeleo. Sígame por aquí."
    "Amber" "Es nuestro modelo más valioso y lo tenemos apartado del resto."
    scene c23s006_405An2 with dissolve
    "Amber abre una puerta con un mando a distancia y allí está el peor atentado contra el buen gusto de la historia de la automoción."
    call BlinkXPS3 ("c23s006_425" , "d") from _call_BlinkXPS3_1449
    emm "¡Oh! ¡Es el Ferrarini F69 de 2018! ¡Tiene 660 CV y puede llegar a 355 Km/h! ¡Me encanta este coche!"
    call BlinkXPS3 ("c23s006_430" , "d") from _call_BlinkXPS3_1450
    emm "Pero este no se comercializó en ese color... Solo en rojo o en negro."
    scene c23s006_405d with dissolve
    "Amber" "Todos nuestros coches son pintados localmente para que proporcionen una experiencia más exclusiva."
    "Amber" "Tenemos tres tonos de rosa dependiendo del tipo de coche."
    call BlinkXPS3 ("c23s006_435" , "d") from _call_BlinkXPS3_1451
    emm "¡Han hecho un trabajo exquisito! ¡Sácame una foto con el logo, [mc]!"
    call BlinkXPS3 ("c23s006_440" , "f") from _call_BlinkXPS3_1452
    emm "Que salga bien el Jaballino. Da lo mismo que no me encuadres bien a mí." #pigletino
    emm "Sí, ya sé que es Cinghialetto. Pero me gusta más como lo digo yo. Más fotos."
    mc "Creo que sería mejor fuera que en un garaje."
    emm "¡Ya habrá tiempo para eso! ¡Hazme un par de fotos ahora!"
    scene c23s006_440An with dissolve
    "Tomas varias fotos de [emm] posando con el coche. Apenas se atreve a tocarlo."
    scene c23s006_405e with dissolve
    "Amber" "Miren, por allí llega nuestro instructor Chad. Se ha adelantado."
    "Amber" "Buenos días, Chad."
    scene c23s006_445An with dissolve
    "Puedes entender por qué las señoras maduras contratan el curso de conducción."
    "Chad se dirige directamente a [bet]."
    "Chad" "Buenos días, señora. ¿Preparada para la mejor experiencia automovilística de su vida con Chad?"
    scene c23s006_450a with dissolve
    bet "*Risa* Creo que te equivocas, Chad."
    call BlinkXPS3 ("c23s006_455" , "d") from _call_BlinkXPS3_1453
    bet "Amber, ¿me puedes decir dónde está el lavabo? Voy a ir a cambiarme mientras le presenta a Chad a su clienta."
    call BlinkXPS3 ("c23s006_460" , "f") from _call_BlinkXPS3_1454
    "Unos minutos después, una vez acabadas las presentaciones y el papeleo..."
    emm "Entonces nos vemos aquí en tres horas, ¿no?"
    mc "Bueno, la reunión es en una hora y media. No sé cuánto durará."
    mc "El curso de conducción segura acaba en tres horas, con lo que seguramente nosotros acabaremos antes."
    call BlinkXPS3 ("c23s006_465" , "d") from _call_BlinkXPS3_1455
    emm "Conducción segura {b}de deportivos{/b}. *Risa*"
    mc "Sí, vale. Te he mandado la dirección del motel en el que nos alojaremos, por si nos retrasamos y quieres ir a descansar."
    mc "En cuanto acabemos te llamo y quedamos en algún sitio."
    emm "Perfecto."
    call BlinkXPS3 ("c23s006_470" , "d") from _call_BlinkXPS3_1456
    if emm._var("route"):
        emm "*Susurrando* Te daría un beso, pero seguro que Amber se escandaliza después de decirle que eras mi hermano."
        mc "*Susurrando* No creo que se escandalice demasiado, teniendo en cuenta las señoras maduras que contratan a Chad. *Risa*"
    else:
        emm "*Susurrando* Creo que el curso para señoras maduras con Chad debe incluir alguna cosa más que conducir, viendo su aspecto."
        mc "*Susurrando* Estoy seguro de ello."
    call BlinkXPS3 ("c23s006_475" , "d") from _call_BlinkXPS3_1457
    emm "*Susurrando* Pues que no espere nada conmigo. No es para nada mi tipo."
    if emm._var("route"):
        emm "*Susurrando* Me gustan más como tú."
    mc "*Risa* Te veo luego. [bet] ya está saliendo del lavabo."
    call BlinkXPS3 ("c23s006_480" , "d") from _call_BlinkXPS3_1458
    bet "Disfruta del coche y no dejes que Chad haga nada que no debe, [emm]."
    mc "*Risa* Precisamente estábamos hablando de eso."
    call BlinkXPS3 ("c23s006_485" , "d") from _call_BlinkXPS3_1459
    bet "¿Nos vamos, entonces?"
    mcp "(Claramente no tiene ganas de ir a esa reunión. Yo tampoco las tendría.)"
    mc "Sí, vámonos."
    scene c23s006_490a with dissolve
    emm "Suerte, Tía [bet]."
    mcp "(A veces [emm] es sorprendentemente maravillosa.)"
    stop music fadeout (1.5)
    bet "Gracias, cielo."
    return
label c23s006_RideBetChurch:
    call BlinkXPS3 ("c23s006_500" , "f") from _call_BlinkXPS3_1460
    play music ("music/Sad-Piano.ogg")
    "Después de una comida en la que intentas levantarle los ánimos sin éxito, llevas a [bet] a la catedral de Monterey."
    "La reunión tendrá lugar en un edificio cercano a la catedral."
    bet "Aquí estamos..."
    mc "No tienes ganas de entrar, ¿verdad?"
    call BlinkXPS3 ("c23s006_505" , "d") from _call_BlinkXPS3_1461
    bet "Ahora mismo me apetecería más pegarme un martillazo en el pie que entrar ahí."
    mc "Te entiendo. Pero ¿sabes qué me decía [nor] cuando no quería hacer algo de niño?"
    call BlinkXPS3 ("c23s006_510" , "d") from _call_BlinkXPS3_1462
    bet "Que cuanto antes lo hicieras, antes podrías dedicarte a otras cosas que te gustan más."
    mc "Veo que la frase tiene raíces profundas en la familia. Son exactamente las mismas palabras."
    call BlinkXPS3 ("c23s006_515" , "d") from _call_BlinkXPS3_1463
    bet "*Risa triste* Es una frase que nos decía mi abuela cuando íbamos a visitarla a Missouri."
    if persistent.family:
        bet "Tu bisabuela se la decía a [nor] y a [mar]. Es una frase que suelen decir las abuelas de la familia."
    else:
        bet "Mi madre se la decía a [nor]. Es una frase que suelen decir las abuelas de la familia."
    mc "Y ahora invertimos el proceso y te la digo yo, igual que [nor] me la dijo a mí."
    mc "¿Quieres que te acompañe?"
    call BlinkXPS3 ("c23s006_520" , "d") from _call_BlinkXPS3_1464
    bet "Gracias, pero será mejor que entre sola. De todas formas, a la reunión no puedes asistir."
    mc "Entonces iré al motel a dejar las maletas y vuelvo a buscarte. He visto un café en el que puedo esperarte."
    mc "Llámame cuando salgas y vengo en dos minutos."
    call BlinkXPS3 ("c23s006_525" , "d") from _call_BlinkXPS3_1465
    bet "Me parece perfecto. No sé cuánto voy a tardar y no quiero que te quedes en el coche todo este rato."
    mc "¿Quieres un abrazo antes de ir?"
    call BlinkXPS3 ("c23s006_530" , "d") from _call_BlinkXPS3_1466
    bet "Me encantaría, pero mejor no. *Risa triste* Si me abrazas ahora no voy a querer ir."
    mc "Entonces sin abrazos."
    mc "Suerte, Tía [bet]."
    call BlinkXPS3 ("c23s006_535" , "d") from _call_BlinkXPS3_1467
    bet "Gracias, cielo."
    scene c23s006_540a with dissolve
    "Puedes ver como Tía [bet] se dirige al edificio de oficinas de la diócesis con los hombros hundidos, como un fantasma azul."
    "La batalla que tenga que librar ahí dentro está perdida antes de empezar."
    scene black with dissolve
    "Vas al motel a dejar las maletas de [bet] y [emm] en una habitación y tu mochila en otra."
    "[bet] ha dejado la ropa que llevaba puesta para el viaje en la camioneta. La dejas allí por si se quiere cambiar después."
    "Vuelves al barrio de la catedral y te tomas un café en una heladería a tres minutos del edificio donde [bet] está teniendo la reunión."
    "No disfrutas del café. Estás casi tan nervioso por el resultado como lo estaba [bet] al entrar."
    stop music fadeout (1.5)
    return
label c23s006_FerrariniGirl:
    if _in_replay:
        call mrS3_emm_route from _call_mrS3_emm_route_8
    "La reunión se alarga tanto que [emm] te llama para decirte que ya ha acabado el curso."
    call BlinkXPS3 ("c23s006_600" , "d") from _call_BlinkXPS3_1468 #207
    emm "Hey, [mc]. ¿Aún no habéis acabado la reunión?"
    play music ("music/Ferrari.ogg")
    mc "No, estoy esperando a que Tía [bet] me llame para recogerla e ir a buscarte."
    call BlinkXPS3 ("c23s006_605" , "d") from _call_BlinkXPS3_1469 #197
    emm "No te preocupes por mí. Ya he acabado el curso y voy a conducir un rato. ¡Este coche es increíble!"
    mc "¿Qué tal el curso?"
    call BlinkXPS3 ("c23s006_610" , "d") from _call_BlinkXPS3_1470 #187
    emm "¡Genial! Aunque estoy casi segura de que Chad se saca un extra como gigoló con las maduras, realmente es un profesional."
    emm "Fue piloto de pruebas en un equipo de la WEC durante varios años."
    mc "¿WEC?"
    call BlinkXPS3 ("c23s006_615" , "d") from _call_BlinkXPS3_1471 #177
    emm "El World Endurance Championship, el mundial de resistencia... 24 horas de Le Mans y ese tipo de carreras."
    if emm._var("route"):
        emm "A veces parece que el hombre en esta relación sea yo. No sabes nada de coches."
    else:
        emm "A veces parece que yo sea el hermano y tú la hermana. No sabes nada de coches."
    call BlinkXPS3 ("c23s006_620" , "d") from _call_BlinkXPS3_1472 #167
    emm "¡Pero alquilas unos coches de puta madre!"
    mc "Me alegra que lo estés disfrutando. Me hubiera gustado estar contigo y que lo disfrutáramos juntos."
    call BlinkXPS3 ("c23s006_625" , "d") from _call_BlinkXPS3_1473 #157
    emm "A mí también me hubiera gustado, pero entiendo que no podemos dejar a Tía [bet] sola."
    mc "*Risa* Tu concepto de \"podemos\" es un poco especial. Yo estoy aquí y tú estás conduciendo un coche hortera."
    call BlinkXPS3 ("c23s006_630" , "d") from _call_BlinkXPS3_1474 #147
    emm "*Risa* ¡Qué poco gusto tienes para los coches!"
    mc "Eso es discutible. *Risa* Si no se comercializaba en rosa, por algo será..."
    mc "Por cierto, sabes que si te ponen una multa de velocidad me tocará pagarla a mí, ¿verdad?"
    stop music fadeout (1.5)
    mc "Aunque sea un coche de alquiler, las multas llegan igualmente. Y te las pienso pasar a ti para que las pagues."
    play music ("music/Inspiring-Upbeat-Ambient.ogg")
    call BlinkXPS3 ("c23s006_635" , "d") from _call_BlinkXPS3_1475
    emm "¡Oops! No lo sabía. Pero no te preocupes... no estoy corriendo... {b}demasiado{/b}."
    mc "*Risa* Ese \"demasiado\" me da mucho miedo."
    call BlinkXPS3 ("c23s006_640" , "d") from _call_BlinkXPS3_1476
    emm "Una pregunta, ¿mi nombre está en algún sitio en el motel? Es decir... ¿puedo ir y pedir una llave de la habitación?"
    mc "Sí, ya he avisado en la recepción que era posible que fueras y les pidieras una llave. Estás en la habitación número 6."
    mc "¿Por qué? ¿Estás cansada?"
    call BlinkXPS3 ("c23s006_645" , "d") from _call_BlinkXPS3_1477
    emm "No, es que es posible que compre algunas cosas para las chicas y me gustaría dejarlas en la habitación en vez de llevarlas en el coche todo el día."
    mc "¿Has visto algún souvenir? *Risa* Solo espero que no necesites comprar una cuarta maleta para llevar los regalos."
    call BlinkXPS3 ("c23s006_650" , "d") from _call_BlinkXPS3_1478
    emm "Más o menos. *Risita* Te veo luego. Avísame cuando Tía [bet] acabe, a ver dónde estoy."
    mc "Si conduces demasiado, es posible que acabes en San Francisco... *Risa* con un montón de multas de velocidad."
    emm "No te preocupes. *Risa* No voy a llegar tan lejos. Hasta luego."
    stop music fadeout (1.5)
    return
label c23s006_AfterTheMeeting:
    scene black with dissolve
    "Media hora y dos cafés después, [bet] te avisa de que ya ha salido. Le propones ir a buscarla, pero cuando le dices dónde estás, decide unirse a ti en el café."
    "Avisas a [emm] de que [bet] ya está llegando y le mandas tu ubicación. Está en el motel y llegará en 15 minutos."
    "La monja llega cinco minutos después y se va inmediatamente a poner la ropa que llevaba durante el viaje mientras llega la chica del Ferrarini."
    "[bet] no quiere empezar a explicarte cómo ha ido la reunión para tener que volver a hacerlo cuando llegue [emm]."
    call BlinkXPS3 ("c23s006_655" , "d") from _call_BlinkXPS3_1479
    "Cuando estáis los tres por fin sentados a la mesa..."
    play music ("music/LostVoices.ogg")
    emm "Me muero de impaciencia, Tía [bet]. ¿Qué te han dicho?"
    call BlinkXPS3 ("c23s006_660" , "d") from _call_BlinkXPS3_1480
    bet "El secretario me ha dicho que hice bien en negarme a operar a aquel muchacho."
    mc "Eso es bueno, ¿no?"
    bet "Pero que hice mal en informar a su padre, el jefe tribal, de que el obispo Bakari le había engañado diciéndole que la homosexualidad se podía curar."
    bet "El obispo es una figura muy importante en la iglesia de Tanzania y... ha pedido mi cabeza."
    call BlinkXPS3 ("c23s006_665" , "d") from _call_BlinkXPS3_1481
    emm "¡Que hijo de puta! Supongo que se refiere a que no vuelvas a Tanzania, ¿no?"
    call BlinkXPS3 ("c23s006_670" , "d") from _call_BlinkXPS3_1482
    bet "Ni a Tanzania ni a ningún otro lugar de África."
    mc "Entonces solo te queda lo de trabajar en hospitales en California..."
    call BlinkXPS3 ("c23s006_675" , "d") from _call_BlinkXPS3_1483
    bet "Eso tampoco."
    bet "La iglesia me da dos opciones. Entrar en un convento de clausura en los Estados Unidos o jubilación en otro convento de mi elección en Latinoamérica."
    call BlinkXPS3 ("c23s006_680" , "d") from _call_BlinkXPS3_1484
    emm "¿Por qué? No lo entiendo. ¿Tú lo entiendes?"
    mc "Si está aquí en un convento en el que pueda hablar con la prensa, podría liarla parda. Por eso aquí el convento es de clausura."
    mc "Si está jubilada en un convento en... yo qué sé... Nicaragua o Bolivia... La prensa de allí no le prestará atención."
    mc "Y si habla con la prensa, la iglesia puede decir que la jubilaron con antelación porque ya no pensaba con claridad."
    call BlinkXPS3 ("c23s006_685" , "d") from _call_BlinkXPS3_1485
    mc "¿Me equivoco?"
    bet "No lo ha dicho así, pero tienes razón sobre sus motivos."
    bet "Sea como sea no volveré a ejercer en ningún hospital."
    call BlinkXPS3 ("c23s006_690" , "d") from _call_BlinkXPS3_1486
    emm "No volverás a ejercer si sigues siendo monja, ¿no?"
    emm "Podrías dejar la iglesia y seguir trabajando. Problema resuelto."
    call BlinkXPS3 ("c23s006_695" , "d") from _call_BlinkXPS3_1487
    bet "Me tendría que volver a certificar para poder ejercer de cirujana en los Estados Unidos."
    bet "Y eso vale dinero, no tengo ni idea de cuánto. En mi plan de trabajar en hospitales católicos, esa certificación la pagaba la iglesia..."
    mc "Por el dinero no te preocupes."
    call BlinkXPS3 ("c23s006_700" , "d") from _call_BlinkXPS3_1488
    emm "Tenemos una empresa millonaria. Podemos pagar tu certificación sin problemas."
    mc "Bueno, no con dinero de NTR. Sería un gasto injustificable."
    mc "Pero yo puedo pedir un adelanto de mi sueldo para pagar por tu certificación. Y dudo que el CEO de NTR lo rechace."
    call BlinkXPS3 ("c23s006_705" , "d") from _call_BlinkXPS3_1489
    bet "No os puedo pedir eso..."
    mc "No lo estás pidiendo. Lo estamos ofreciendo nosotros."
    mc "El sábado voy a actuar como CEO por primera vez, y pienso cobrar por ello. Ese dinero es tuyo para la certificación."
    scene c23s006_705d with dissolve
    bet "..."
    mc "Tía [bet]... ¿Estás bien?"
    call BlinkXPS3 ("c23s006_710" , "d") from _call_BlinkXPS3_1490
    emm "¿Qué pasa, Tía?"
    call BlinkXPS3 ("c23s006_715" , "d") from _call_BlinkXPS3_1491
    bet "No me merezco esta familia..."
    mc "Te mereces esto y más."
    call BlinkXPS3 ("c23s006_720" , "d") from _call_BlinkXPS3_1492
    emm "Estoy de acuerdo con [mc]. Todos querríamos ayudarte, y todo el mundo estaba muy preocupado por tu situación."
    emm "Si [mc] se negara a sí mismo el adelanto de sueldo, estoy segura de que entre todas conseguiríamos el dinero para tu certificación."
    call BlinkXPS3 ("c23s006_725" , "d") from _call_BlinkXPS3_1493
    emm "Seguro que para alguien como [lis] y [deb.nick], lo que cuesta la certificación es calderilla, y dijeron que podíamos contar con ellas para lo que necesitáramos."
    emm "Aunque no hablamos de dinero, claro, porque no sabíamos que eso podría ser el problema."
    call BlinkXPS3 ("c23s006_730" , "d") from _call_BlinkXPS3_1494
    mc "Todo el mundo va a querer ayudarte. No te preocupes por eso."
    bet "Pero..."
    call BlinkXPS3 ("c23s006_735" , "d") from _call_BlinkXPS3_1495
    emm "Y [dap] y [sca] te ayudarán a estudiar si es necesario... Hay que estudiar para la certificación, ¿no?"
    emm "Yo también te ayudaría, pero no tengo ni idea de medicina."
    call BlinkXPS3 ("c23s006_740" , "d") from _call_BlinkXPS3_1496
    bet "Chicos... me estáis emocionando..."
    mc "La familia está para eso, Tía [bet]. No sólo para cuando todo va bien, sino para apoyarnos cuando hay algún problema."
    mc "¿Cuándo les tienes que dar una respuesta?"
    call BlinkXPS3 ("c23s006_745" , "d") from _call_BlinkXPS3_1497
    bet "Me han dado dos meses para pensármelo. Mañana tengo que pasar a recoger una documentación sobre los diferentes conventos que proponen."
    bet "Todo eso, obviamente, bajo la condición de que no hable con la prensa nunca."
    mc "¿Qué te pueden hacer si hablas con la prensa?"
    call BlinkXPS3 ("c23s006_750" , "d") from _call_BlinkXPS3_1498
    bet "Podrían eliminar la opción del convento en Latinoamérica, que era la menos mala."
    bet "De todas formas, no pensaba hablar con la prensa. No serviría de nada. El obispo Bakari no se vería afectado."
    call BlinkXPS3 ("c23s006_755" , "d") from _call_BlinkXPS3_1499
    emm "Bueno, como no vas a hablar con la prensa ni vas a coger esa opción, no tenemos que hablar de eso ahora."
    mc "Tienes razón, [emm]. Ahora hay dos meses para sopesar opciones y pensar en qué podemos hacer y cómo hacerlo."
    call BlinkXPS3 ("c23s006_760" , "d") from _call_BlinkXPS3_1500
    bet "No hay mucho que pensar. Si me prestáis el dinero..."
    mc "No es un préstamo, es un regalo."
    call BlinkXPS3 ("c23s006_765" , "d") from _call_BlinkXPS3_1501
    bet "{b}Si me prestáis el dinero{/b} para certificarme, creo que mi mejor opción sería abandonar la iglesia..."
    bet "Y empezar a buscar trabajo como cirujana... a mi edad... Ufff..."
    mc "Bueno, si piensas que es la mejor opción no vamos a intentar convencerte de lo contrario. Tienes dos meses para pensártelo."
    call BlinkXPS3 ("c23s006_770" , "d") from _call_BlinkXPS3_1502
    emm "Y para alegrarte un poco el día, hoy invito yo a pizza."
    emm "Por si estabas triste había buscado pizzerías con buenas reseñas."
    mc "A veces eres sorprendente, [emm]. Cada vez más."
    call BlinkXPS3 ("c23s006_775" , "d") from _call_BlinkXPS3_1503
    bet "¿Crees que me puedes comprar con comida, [emm]?"
    call BlinkXPS3 ("c23s006_780" , "d") from _call_BlinkXPS3_1504
    emm "No quería que sonara así, Tía... perdona..."
    call BlinkXPS3 ("c23s006_785" , "d") from _call_BlinkXPS3_1505
    bet "Porque si lo crees, tienes toda la razón. *Risa*"
    mc "*Risa* Vamos al motel a ducharnos y vamos a ver qué pizzería ha encontrado [emm]."
    stop music fadeout (1.5)
    scene black with dissolve
    "Ver que se han abierto más opciones de las que había planteado la iglesia ayuda a mejorar los ánimos."
    "Vais al motel a ducharos y cambiaros de ropa. Te pones la camisa azul."
    return
label c23s007_AmaCalls:
    if _in_replay:
        call mrS3_eva_route from _call_mrS3_eva_route_3
        call mrS3_ama_route from _call_mrS3_ama_route_5
        call mrS3_deb_laptop from _call_mrS3_deb_laptop
    scene c23s007_005a with fade
    play sound ("music/RingtoneMC.ogg")
    "*Ring-Ring*"
    "Suena tu teléfono, es [ama]."
    stop sound
    scene c23s007_005b with dissolve
    play music ("music/UnforeseenMotive.ogg")
    mc "Hola, [ama]. ¿Puedo ayudarte en algo?"
    scene c23s007_010a with fade
    ama "Sólo llamábamos para saber cómo había ido la reunión de Tía [bet]. No queremos molestarla a ella."
    eva "Hubiéramos llamado antes, pero no sabíamos a qué hora iba a terminar la reunión."
    mc "Bueno, ha ido como uno de los peores escenarios que habíamos pensado."
    mc "La propuesta de la iglesia es que se retire a un convento."
    call BlinkXPS3 ("c23s007_015" , "d") from _call_BlinkXPS3_1506
    eva "¡Putos cabrones! ¿Necesitas que hagamos una visita a ese obispo para convencerle... sutilmente?"
    mc "No, [eva]. Tía [bet] tiene que darles una respuesta en dos meses, con lo que hay tiempo para pensar qué quiere hacer."
    call BlinkXPS3 ("c23s007_020" , "d") from _call_BlinkXPS3_1507
    ama "Si quieres... podemos buscar cosas sobre ese obispo, o sobre el de Tanzania, para poder hacer más presión y que cambien de opinión."
    mc "Creo que Tía [bet] no querría eso. Ahora mismo se siente como que no pertenece a la Iglesia. Se siente traicionada."
    mc "Por eso se tomará estos meses para sopesar dejar de ser monja. Casi lo ha decidido ya."
    call BlinkXPS3 ("c23s007_025" , "d") from _call_BlinkXPS3_1508
    ama "Es lógico. La quieren esconder después de lo de Tanzania, y eso es cruel."
    mc "Por lo que me ha explicado, esa es exactamente su intención, que acabe sus días en un sitio donde no moleste."
    mc "Y donde no pueda hablar con la prensa."
    call BlinkXPS3 ("c23s007_030" , "d") from _call_BlinkXPS3_1509
    eva "¡Putos cabrones! Necesito dispararle a algo. Dale un abrazo de mi parte a Tía [bet]."
    mc "¡[eva]!"
    call BlinkXPS3 ("c23s007_035" , "d") from _call_BlinkXPS3_1510
    ama "Ya se ha ido. Cuando se le desatan sentimientos que no puede controlar hace prácticas de tiro. Ya lo viste ayer."
    mc "Espero no enfadarla nunca..."
    call BlinkXPS3 ("c23s007_040" , "d") from _call_BlinkXPS3_1511
    if eva._var("route"):
        ama "Hasta vuestra primera cita, como mínimo, estás seguro. *Risa*"
        mc "Entonces tendremos la primera cita dentro de muchos años. *Risa*"
        ama "Si la retrasas mucho dejarás de estar seguro también. *Risa*"
    else:
        ama "Si no te disparó ayer después de rechazarla, supongo que puedes considerarte seguro."
    mc "¿Necesitas algo más? Iba a llevar a las chicas a cenar..."
    call BlinkXPS3 ("c23s007_045" , "d") from _call_BlinkXPS3_1512
    ama "Solo una cosa más. Es una idea que se les ha ocurrido a Jamaal y a [nor], pero puede esperar si tienes prisa."
    mc "No, tranquila, [emm] aún se está acabando de vestir. Dime."
    call BlinkXPS3 ("c23s007_050" , "d") from _call_BlinkXPS3_1513
    ama "Jamaal y yo estábamos hablando de lo de los asistentes a la fiesta del barco de Iron Fist cuando ha aparecido [nor]."
    ama "[nor] es muy inteligente y ha estado pensando en que, si reconvertimos NTR en una empresa médica, el nombre puede ser un lastre."
    mc "*Risa* Ese nombre sería un lastre fuera como fuera."
    call BlinkXPS3 ("c23s007_055" , "d") from _call_BlinkXPS3_1514
    ama "Algo parecido ha dicho Jamaal, pero no entiendo por qué."
    ama "[nor] lo decía porque NTR tiene un pasado militar y, en este país, puede ser un problema."
    mc "Tiene razón, pero no por el pasado militar, sino por las operaciones encubiertas. La gente desconfía de lo que se le oculta."
    mc "¿Ha propuesto cambiarle el nombre a la empresa?"
    call BlinkXPS3 ("c23s007_060" , "d") from _call_BlinkXPS3_1515
    ama "Más que cambiarle el nombre, crear una empresa filial y traspasar toda la actividad médica allí. Al menos a nivel comercial."
    mc "Me parece bien. Así NTR quedará para soporte a otras empresas de operaciones encubiertas y la nueva empresa se ocupará de todo el tema médico."
    call BlinkXPS3 ("c23s007_065" , "d") from _call_BlinkXPS3_1516
    ama "A Jamaal también le ha parecido una buena idea. Incluso se le ha ocurrido un nombre. Harnessing Advanced Research for Enhancing Medicine."
    ama "Aprovechar la investigación avanzada para mejorar la medicina. Aunque me parece un poco largo" #Me parece un poco largo
    mc "A mí me parece un buen nombre, podemos usar siglas como NTR..."
    mc "Espera..."
    mc "*Risa* Jamaal es un capullo."
    call BlinkXPS3 ("c23s007_070" , "d") from _call_BlinkXPS3_1517
    ama "¿Qué pasa?"
    mc "¿No te has dado cuenta de cuáles serían las siglas? H.A.R.E.M."
    call BlinkXPS3 ("c23s007_075" , "d") from _call_BlinkXPS3_1518
    ama "¡Me ha tomado el pelo! *Risa* Voy a decirle a [eva] que practique tiro contra sus ruedas."
    mc "*Risa* Si Jamaal empieza a gastarte bromas, significa que está dejando de teneros miedo. Es su forma de daros la bienvenida a la familia."
    mc "*Risa* Pero sigue pareciéndome un buen nombre. Sigue la línea de NTR y GILF."
    call BlinkXPS3 ("c23s007_080" , "d") from _call_BlinkXPS3_1519
    ama "Continúo sin entender qué tiene de malo NTR."
    mc "Mucho, [ama]. Mucho."
    if deb._var("laptop"):
        mc "Puedes preguntárselo a [deb.nick] cuando la veas. *Risa*"
    scene c23s007_005c with dissolve
    play sound ("music/knock.ogg")
    "*Knock-Knock*"
    emm "*A través de la puerta* [mc], ya estamos listas. Te esperamos en el coche."
    mc "Ahora voy. Un segundo."
    call BlinkXPS3 ("c23s007_085" , "d") from _call_BlinkXPS3_1520
    ama "Ve antes de que [emm] se impaciente. *Risa* No sé si ese hotel tiene tienda de regalos, pero podría empezar a comprar cosas rosas."
    mc "*Risa* No te preocupes, no hay tienda de regalos."
    mc "Os mantengo informadas de cómo va lo de Tía [bet] mañana."
    if eva._var("route") and ama._var("route"):
        mc "Y has dicho que estaré seguro hasta la primera cita con [eva]. Tú y yo tenemos que planificar la nuestra también."
    elif ama._var("route"):
        mc "Y tú y yo tenemos una cita que planificar."
    if ama._var("route"):
        call BlinkXPS3 ("c23s007_090" , "d") from _call_BlinkXPS3_1521
        ama "No te preocupes por eso. El otro día en el café cuenta como nuestra primera cita. Hubo besos. Suficiente para mí, al menos por ahora."
    ama "Y vete antes de que Tía [bet] empiece a tener hambre. *Risa* Hasta mañana, [mc]."
    mc "Hablamos mañana, [ama]."
    stop music fadeout (1.5)
    return
label c23s007_SleepingArrangements:
    if _in_replay:
        call mrS3_bet_route1 from _call_mrS3_bet_route1
        call mrS3_emm_route from _call_mrS3_emm_route_9
    scene black with dissolve
    "Pasáis una noche agradable, cenando y riendo, sin nombrar ni una sola vez el dilema de [bet]."
    "[emm] os explica emocionada todo lo que ha aprendido en el curso de conducción y por dónde ha conducido mientras os esperaba."
    "Cuando le preguntas, se niega a decir qué ha comprado para las chicas en casa."
    if not bet._var("route"):
        "Al llegar al hotel os dirigís a vuestras respectivas habitaciones."
        "Pasas una buena noche de descanso."
        return
    call BlinkXPS3 ("c23s007_100" , "d") from _call_BlinkXPS3_1522
    play music ("music/SneakySnitch.ogg")
    "Al llegar al hotel..."
    emm "¡Ay! ¡Uff!"
    mc "¿Qué te pasa, [emm]?"
    call BlinkXPS3 ("c23s007_105" , "d") from _call_BlinkXPS3_1523
    emm "Te he dicho antes de salir que si tenía que dormir sentada me acabaría doliendo el cuello."
    emm "Entre eso y después el curso de conducción, lo tengo hecho polvo. Ahora entiendo por qué los pilotos tienen cuellos como troncos."
    call BlinkXPS3 ("c23s007_110" , "d") from _call_BlinkXPS3_1524
    bet "¿Quieres que te dé un masaje o algo?"
    mc "O tomarte un analgésico."
    call BlinkXPS3 ("c23s007_115" , "d") from _call_BlinkXPS3_1525
    emm "No hace falta. Con una buena noche de descanso..."
    call BlinkXPS3 ("c23s007_120" , "d") from _call_BlinkXPS3_1526
    emm "¡Oh!"
    mc "¿Qué pasa?"
    call BlinkXPS3 ("c23s007_125" , "d") from _call_BlinkXPS3_1527
    emm "No has cogido camas individuales, y cuando tengo este dolor de cuello me muevo mucho durmiendo."
    emm "Voy a molestar a Tía [bet] y no le voy a dejar dormir."
    call BlinkXPS3 ("c23s007_130" , "d") from _call_BlinkXPS3_1528
    bet "No te preocupes, yo duermo como un tronco..."
    call BlinkXPS3 ("c23s007_125" , "d") from _call_BlinkXPS3_1529
    mc "Puedes dormir en mi cama y yo duermo en el sofá. No parece incómodo."
    call BlinkXPS3 ("c23s007_135" , "d") from _call_BlinkXPS3_1530
    emm "No podría hacerte eso. Es tu cama..."
    emm "Pero has tenido una buena idea. ¿Por qué no nos cambiamos de habitación? Yo duermo en la tuya y tú en la mía."
    mc "Porque acabas de decir que es una cama doble. No sé si Tía [bet] querrá compartirla conmigo."
    call BlinkXPS3 ("c23s007_140" , "d") from _call_BlinkXPS3_1531
    bet "No voy a permitir que duermas en un sofá."
    call BlinkXPS3 ("c23s007_145" , "d") from _call_BlinkXPS3_1532
    emm "¿Ves? Además, Tía [bet] seguro que ha traído un pijama nada sexy de esos de franela."
    call BlinkXPS3 ("c23s007_150" , "d") from _call_BlinkXPS3_1533
    bet "*Risa* ¿Has estado revolviendo en mi maleta? No es de franela, pero no creo que nadie pueda considerarlo sexy."
    mc "¿Estás segura, Tía [bet]?"
    call BlinkXPS3 ("c23s007_155" , "d") from _call_BlinkXPS3_1534
    bet "¿De que el pijama no es sexy o de que no voy a dejarte dormir en el sofá?"
    bet "Porque estoy muy segura de las dos cosas."
    call BlinkXPS3 ("c23s007_160" , "d") from _call_BlinkXPS3_1535
    emm "Entonces todo arreglado. Ayúdame a mover mis tres maletas a tu habitación, [mc]."
    mc "Vamos, se está haciendo tarde y tú has dormido poco esta noche."
    call BlinkXPS3 ("c23s007_165" , "d") from _call_BlinkXPS3_1536
    "Una vez movidas las maletas..."
    emm "Descansa, que mañana quiero hacer turismo. Podemos dejar el Ferrarini aquí e ir con tu coche. O incluso devolverlo antes."
    mcp "(¿No era el otro lado del cuello el que le dolía? Es posible que le duelan los dos, ¿no?)"
    emm "Tengo ganas de pasar tiempo con Tía [bet]."
    mc "Ahora necesita nuestro apoyo más que nunca."
    if emm._var("route"):
        call KissXPS3 ("c23s007_170" , "d") from _call_KissXPS3_34
    else:
        call BlinkXPS3 ("c23s007_175" , "d") from _call_BlinkXPS3_1537
    emm "Espero que la apoyes mucho esta noche. Hasta mañana, [mc]."
    mc "Hasta mañana, [emm]."
    scene c23s007_180An with dissolve
    emm "Cuídala."
    stop music fadeout (1.5)
    scene c23s007_185a with fade
    "Al llegar a la habitación que compartes con [bet] con tu mochila..."
    play music ("music/Tribal.ogg")
    bet "*Desde el lavabo* ¡Voy a matarla!"
    mc "¿Qué pasa Tía [bet]? ¿A quién quieres matar?"
    scene c23s007_185b with fade
    bet "*A través de la puerta* ¡A [emm]!"
    mc "¿Qué ha hecho ahora?"
    bet "*A través de la puerta* ¡Se ha llevado toda mi ropa!"
    mc "¿Se ha llevado tu maleta?"
    bet "*A través de la puerta* ¡No! ¡Ha vaciado mi maleta! ¡No ha dejado ni la ropa que llevaba en el viaje!"
    stop music fadeout (1.5)
    mc "Voy a decirle que te la devuelva. Seguramente te quería gastar una broma."
    play sound ("music/Wheels.ogg")
    scene c23s007_185c with fade
    pause (0.3)
    scene c23s007_185d with dissolve
    pause (0.3)
    scene c23s007_185e with dissolve
    "Cuando sales de la habitación, ves el Ferrarini rosa saliendo a toda velocidad del aparcamiento."
    stop sound
    mcp "(¿Qué trama esta chica?)"
    call c23s007_End from _call_c23s007_End
    return
label c23s007_End:
    scene c23s007_185b with fade
    "Tras un paso infructuoso por recepción, vuelves a la habitación de [bet]..."
    play music ("music/TheMatador.ogg")
    bet "*A través de la puerta* ¿Has conseguido que te devuelva mi ropa?"
    mc "No, cuando he salido se iba en su coche."
    bet "*A través de la puerta* ¿Has ido a recepción para que te den la llave? Esa habitación está a tu nombre."
    mc "He ido, y [emm] les ha dicho que hemos cambiado de habitaciones y que no le den su llave a nadie bajo ninguna circunstancia."
    bet "*A través de la puerta* ¡La mato!"
    bet "*A través de la puerta* ¿Tú estás seguro de que estaba durmiendo en el coche?"
    mc "No lo sé, has sido tú quien ha dicho que estaba durmiendo. ¿Por qué?"
    bet "*A través de la puerta* Porque creo que lo ha oído todo."
    mc "¿Por qué crees eso?"
    scene c23s007_190d with fade:
        yalign 1.0
        linear 5.0 yalign 0.0
    pause (5.0)
    call BlinkXPS3 ("c23s007_190" , "d") from _call_BlinkXPS3_1538
    bet "Porque lo único que ha dejado en mi maleta ha sido esto, que ni siquiera es mío y todavía tiene la etiqueta."
    call addProfileImageS3 (7, "betty_7", bet, _(": 15 - Especial"), "") from _call_addProfileImageS3_5
    bet "Y una nota que decía \"Disfrútalo\"."
    stop music fadeout (1.5)
    return

label c30:
    #call eoc from _call_eoc_1
    if dap._var("route") and sca._var("route"):
        call c30s001_DapScaLewd from _call_c30s001_DapScaLewd
    else:
        call c30s001_noDapScaLewd from _call_c30s001_noDapScaLewd
    call checkPregnancies from _call_checkPregnancies
    call c30s002_pregnancyTests from _call_c30s002_pregnancyTests
    if kat._var("route"):
        call c30s002_KatKiss from _call_c30s002_KatKiss
    call c30s002_getEriEilSca from _call_c30s002_getEriEilSca
    call c30s002_AfterDinner from _call_c30s002_AfterDinner
    if lis._var("route"):
        call c30s002_LisSlap from _call_c30s002_LisSlap
    #Change Day Monday
    call c30s002_SolomonDream from _call_c30s002_SolomonDream
    if kat._var("route"):
        call c30s003_KatWakeUp from _call_c30s003_KatWakeUp
    call c30s003_MarShopping from _call_c30s003_MarShopping
    if emm._var("route"):
        call c30s005_EmmLewd from _call_c30s005_EmmLewd
    call c30s004_Eva from _call_c30s004_Eva
    #Change Day Tuesday
    call c30s004_EmmMarEri from _call_c30s004_EmmMarEri #Se quejan de lo difícil que es no tener sexo
    call c30s004_NorGetsBetMee from _call_c30s004_NorGetsBetMee #MC se ofrece pero no le dejan
    call c30s004_getJam from _call_c30s004_getJam #Sam Manda a MC a por Jam
    call c30s006_atHome from _call_c30s006_atHome
    if mc._var("relationships")>0:
        call c30s006_wedding from _call_c30s006_wedding
    call c30s007_MeeBetAtHome from _call_c30s007_MeeBetAtHome
    if kat._var("route"):
        call c30s007_KatLewd from _call_c30s007_KatLewd
    else:
        call c30s007_noKatLewd from _call_c30s007_noKatLewd
    return
label c30s001_DapScaLewd:
    if _in_replay:
        call mrS3_dap_pregnant from _call_mrS3_dap_pregnant_2
        call mrS3_sca_pregnant from _call_mrS3_sca_pregnant_4
        call mrS3_sca_anal from _call_mrS3_sca_anal_1
        call mrS3_edmund_story from _call_mrS3_edmund_story_12
        call mrS3_kat_route from _call_mrS3_kat_route_3
        call c29s009_ScaDapTeaser from _call_c29s009_ScaDapTeaser_1
    scene c29s009_005a
    play music ("music/Sexy-Background-Music.ogg")
    mc "No me voy a quejar, pero ¿qué hacéis aquí?"
    call BlinkXS4("c30s001_005") from _call_BlinkXS4_812
    dap "*Risa* Creo que es la pregunta más idiota que podrías haber hecho."
    dap "¿Tienes dos mujeres desnudas en tu cama y preguntas qué hacemos aquí?"
    mc "No me refería a..."
    call BlinkXS4("c30s001_010") from _call_BlinkXS4_813
    sca "*Risa* Hemos venido a limpiar tu habitación y, por alguna razón desconocida, hemos perdido la ropa."
    mc "*Risa* Vale, tenéis razón. La pregunta era idiota."
    mc "Tan solo estaba sorprendido de veros aquí."
    call BlinkXS4("c30s001_015") from _call_BlinkXS4_814
    dap "Venimos a por nuestra última lección."
    mc "Ninguna de las dos necesitáis lecciones desde hace mucho."
    call BlinkXS4("c30s001_020") from _call_BlinkXS4_815
    sca "*Risa* Lo sabemos, pero pese a todo queremos tener nuestra última lección."
    sca "Sabes que somos unas nerds y nos encanta estudiar."
    call BlinkXS4("c30s001_025") from _call_BlinkXS4_816
    sca "Además, yo he querido hacer esto con [dap] desde el día que llegaron las chicas nuevas... O incluso desde antes."
    sca "Nada lésbico, antes de que preguntes. Me refiero a la última lección."
    sca "Creo que hoy es un día estupendo para hacerlo. Pasado mañana empiezo a trabajar y..."
    call BlinkXS4("c30s001_030") from _call_BlinkXS4_817
    dap "Y estará demasiado cansada para esto. Además, hoy parece que estás libre."
    mc "Lo estaba hasta ahora. Creo que voy a estar ocupado el resto de la noche."
    scene c30s001_030d with dissolve
    sca "Entonces, ven aquí."
    dap "Te estamos esperando. *Risa* A menos que quieras que nos vayamos."
    scene c30s001_035An with dissolve
    "No vas a esperar a que te lo repitan. Ni a darles a las dos mujeres la oportunidad de que se vayan."
    "No podrías sentirte más orgulloso como profesor cuando tus labios van pasando de una de sus bocas a la siguiente."
    mcp "(Ha pasado casi un mes de aquella noche en que me besaron en el Twins.)"
    "Sus besos no tienen nada que ver con los de aquella noche. Si es que podían considerarse besos."
    "Ahora vuestras manos recorren vuestros cuerpos a la vez que vuestras lenguas recorren vuestras bocas."
    call BlinkXS4("c30s001_040") from _call_BlinkXS4_818
    mc "¡Wow! Eres una gran besadora."
    dap "*Risa* ¡Wow! Tuve un gran maestro."
    call BlinkXS4("c30s001_045") from _call_BlinkXS4_819
    sca "¿Sabéis de qué me estaba acordando? De la noche del Twins."
    sca "Solo de pensar en cómo ha cambiado todo en un mes..."
    mc "Yo estaba pensando lo mismo. Os habéis graduado Cum Laude en lo que a besos se refiere."
    call BlinkXS4("c30s001_050") from _call_BlinkXS4_820
    dap "..."
    mc "¿Qué pasa, [dap]?"
    call BlinkXS4("c30s001_055") from _call_BlinkXS4_821
    dap "*Risa* Quería hacer una broma sobre las diferencias entre el significado de 'Cum' en latín y en inglés..."
    dap "Pero no he sido capaz de construirla en mi mente sin que me hiciera sonar como una nerd."
    mc "*Risa* Adoro a mis nerds."
    call BlinkXS4("c30s001_060") from _call_BlinkXS4_822
    sca "¿Cuál es la siguiente lección? ¿Cómo quieres hacerlo?"
    mc "La siguiente lección es que no hay normas. Esta vez tenéis que tomar la iniciativa vosotras."
    call BlinkXS4("c30s001_065") from _call_BlinkXS4_823
    dap "¿Te parece poca iniciativa la que hemos tomado hasta ahora?"
    dap "Hace un mes vinimos a ese sofá a que nos enseñaras a besar. Sin eso no estaríamos aquí hoy."
    mc "No lo podemos saber. *Risa* Creo que a [sca] se le hubiera ocurrido algo más."
    call BlinkXS4("c30s001_070") from _call_BlinkXS4_824
    sca "*Risa* Tenía muchos planes, pero ninguna esperanza de que alguno de ellos funcionara."
    sca "Ni siquiera el que al final funcionó. Y ha funcionado mucho mejor de lo que podía haber esperado."
    call BlinkXS4("c30s001_075") from _call_BlinkXS4_825
    sca "No sólo tengo el mejor novio del mundo, sino que, además, he encontrado una familia."
    mc "La familia la hubieras encontrado aunque tus planes hubieran fracasado, [sca]."
    call BlinkXS4("c30s001_080") from _call_BlinkXS4_826
    dap "[mc] tiene razón. Todos te queremos, y hubieras acabado aquí, aunque no hubieras tenido ningún plan y no estuvieras con [mc]..."
    call BlinkXS4("c30s001_085") from _call_BlinkXS4_827
    dap "Bueno, no exactamente aquí, en la cama de [mc] y desnuda, pero sabes a lo que me refiero..."
    mc "*Risa* Hubiera sido raro encontraros a las dos desnudas en mi cama si no estuviéramos juntos."
    call BlinkXS4("c30s001_090") from _call_BlinkXS4_828
    sca "[dap], [mc] ha dicho que no hay normas hoy. Voy a poner una. Tenemos que mantener la norma de decir si algo nos molesta."
    sca "Voy a empezar yo. Creo que hablamos demasiado y tenemos un hombre al que desnudar."
    mc "*Risa* Me gusta que se mantenga esa norma."
    scene c30s001_095An with dissolve
    "Las dos chicas no tardan nada en desnudarte."
    "Mjolnir ya está preparado para ellas."
    "Sus ansiosas miradas te dicen que ellas también están preparadas para ti."
    call BlinkXS4("c30s001_100") from _call_BlinkXS4_829
    dap "Túmbate. Vamos a preparar a Mjolnir..."
    mc "Ya está más que preparado. *Risa* Llevo 15 minutos aquí con vosotras desnudas y creo que estaba preparado desde el minuto uno."
    call BlinkXS4("c30s001_105") from _call_BlinkXS4_830
    sca "Nos has dicho que tomemos la iniciativa. Túmbate."
    mc "Mis chicas se han puesto en plan mandonas. Dejadme un hueco."
    scene c30s001_110a with fade
    mc "¿Qué es lo que estáis pensando en hacer?"
    dap "Lo tendrás que descubrir tú solo. Ten un poco de paciencia."
    sca "Vamos a poner tus lecciones a prueba. Si hay algo que no te guste, nos lo dices."
    mc "No creo que haya nada que podáis hacer ahora mismo que no me vaya a gustar."
    scene c30s001_110b with dissolve
    sca "*Risa* Es lo que pensábamos, [dap]. Ya puedes sacar el strap-on. Hoy [mc] va a perder la última virginidad que le queda."
    mc "*Risa* Vale. Hay cosas que podríais hacer y que no me gustarían."
    dap "*Risa* No te preocupes. Si alguien va a bombear con las caderas, vas a ser tú."
    dap "Pero hay que lubricar un poco a Mjolnir."
    scene c30s001_110c with fade
    mc "No me convence esta postura demasiado... No os puedo ver."
    dap "Así no podrás anticipar nuestros movimientos."
    sca "¡Lengüetazos sorpresa!"
    scene c30s001_900pv with fade
    show c30s001_900v
    "Las dos chicas ponen sus manos y sus lenguas a trabajar, sin que sepas en ningún momento cuál de las dos va a lamer tu glande a continuación."
    sca "*Slurp*"
    "Los movimientos de la mano de [dap] son rápidos, buscando que produzcas líquido preseminal en seguida para incrementar la lubricación."
    dap "*Slurp*"
    "Los de [sca] son más pausados y suaves, tan solo dirigiendo tu polla de una lengua a la siguiente."
    scene c30s001_905pv with fade
    show c30s001_905v
    hide c30s001_900v
    dap "*Slurp* Cada vez está más duro."
    "[dap] tan solo constata un hecho. Como un experimento científico que confirma sus hipótesis. Pero su voz suena excitada."
    sca "*Slurp* ¿Esperabas otra cosa?"
    "Casi dejas escapar una carcajada. No crees que nadie pueda ser tan sexy discutiendo sobre un experimento."
    scene c30s001_115a with fade
    hide c30s001_905v
    "Por un momento te las imaginas en uno de los laboratorios de NTR, como científicas ultra sexys."
    mcp "(Creo que no sería capaz de escuchar sus explicaciones sobre experimentos.)"
    "La visión dura un segundo, pero es suficiente para que Mjolnir se ponga aún más duro."
    scene c30s001_115b with fade
    dap "Creo que no puede crecer más."
    sca "No sé en lo que estará pensando, pero casi me rompe la muñeca hace un segundo."
    mc "Chicas, estoy aquí..."
    scene c30s001_115c with dissolve
    dap "¡Hush! Tenemos que decidir con quién empiezas."
    sca "Va a ser nuestro primer trío de verdad y queremos hacerlo bien."
    mc "Me extraña que no lo tuvierais decidido antes de llegar a la habitación."
    scene c30s001_115d with dissolve
    sca "Creo que deberías empezar tú..."
    dap "No, creo que deberías ser tú..."
    mc "No creo que debáis discutir por eso."
    scene c30s001_115e with dissolve
    sca "Tienes razón. Deberías elegir tú."
    dap "Las dos queremos que la otra sea la primera, pero no queremos quedarnos mirando..."
    sca "¿Con quién quieres empezar?"
    mc "Con las dos. Poneos en la otomana."
    scene c30s001_115f with dissolve
    dap "¿Qué?" (multiple=2)
    sca "¿Cómo?" (multiple=2)
    mc "Una encima de la otra."
    scene c30s001_115g with fade
    dap "Eso no me lo esperaba. Puede ser interesante..."
    sca "Y excitante. ¿Te quieres poner arriba o abajo?"
    mc "¿Vais a tener que llegar a un acuerdo para todo?"
    mc "[dap] abajo y [sca] arriba. Por un tema de alturas."
    scene c30s001_115h with fade
    sca "¿Así?"
    dap "Es un poco... raro. Puedo notar las tetas de [sca] en mi espalda..."
    mc "Así estáis perfectas."
    scene c30s001_120An with dissolve
    $renpy.sound.play("music/DaphneMoan.ogg", loop=True)
    "Te arrodillas detrás de las dos mujeres y empiezas a usar tu boca alternativamente en una y en otra."
    "La humedad de tu lengua se suma a la de sus excitados coños."
    $renpy.sound.play("music/ScarlettMoan.ogg", loop=True, relative_volume=15.0)
    dap "*Gemido* Se me acaba de poner piel de gallina... *Jadeo*"
    sca "*Jadeo* Me encanta cuando hace eso... *Gemido*"
    $renpy.sound.play("music/DaphneMoan.ogg", loop=True)
    "Por tu mente pasa la idea de continuar comiéndote sus coños hasta llevarlas al orgasmo."
    "Pero después de las atenciones que le han prestado a Mjolnir, no puedes esperar más para penetrarlas."
    scene c30s001_125a with fade
    "Apoyas la punta de tu polla contra la entrada del coño de [dap]."
    mc "Voy a empezar contigo, cielo."
    sca "Supongo que te refieres a [dap.nick]..."
    dap "*Jadeo* Te hemos dicho que ninguna quería ser la primera..."
    scene c30s001_125b with hpunch
    $renpy.sound.play("music/DaphneMoan.ogg", loop=True)
    "No tienes ninguna intención de discutir. Con un movimiento de tus caderas embistes a [dap] hasta el fondo."
    dap "*JADEO* Aunque bien pensado... *Gemido* No me importa ser la primera... *Jadeo*"
    sca "*Risita* Pues sí. Te referías a [dap.nick]. Me tocará esperar mi turno."
    scene c30s001_980pv with dissolve
    show c30s001_980v
    $renpy.sound.play("music/ScarlettMoan.ogg", loop=True, relative_volume=15.0)
    "No la haces esperar demasiado. Vas cambiando de una a otra chica tras un par de embestidas."
    sca "*Gemido* Mi turno sabe a poco. *Jadeo*"
    $renpy.sound.play("music/DaphneMoan.ogg", loop=True)
    "Un húmedo coño te abraza antes que los fluidos del anterior se sequen sobre tu polla."
    dap "*Jadeo* Cállate, perra avariciosa. *Gemido risueño*"
    "La relación entre las dos chicas es increíblemente bonita."
    scene c30s001_985pv with dissolve
    show c30s001_985v
    hide c30s001_980v
    $renpy.sound.play("music/ScarlettMoan.ogg", loop=True, relative_volume=15.0)
    "Que se puedan insultar y reírse al mismo tiempo es una demostración de lo buenas amigas que son."
    sca "*Jadeo* Cállate tú. *Gemido* Y dame las gracias. *Jadeo risueño*"
    $renpy.sound.play("music/DaphneMoan.ogg", loop=True)
    "Todos sabéis que sin los planes de [sca] no estaríais aquí ahora mismo."
    dap "*Gemido risueño* Gracias por ser una tan perra tan lista, [sca]. *Jadeo*"
    $renpy.sound.play("music/ScarlettMoan.ogg", loop=True, relative_volume=15.0)
    "Solamente [dap] podría mostrarse agradecida e insultante a la vez."
    scene c30s001_990pv with dissolve
    show c30s001_990v
    hide c30s001_985v
    $renpy.sound.play("music/DaphneMoan.ogg", loop=True)
    "Pero el que debería sentirse agradecido eres tú."
    dap "*Jadeo* ¿Podrías hacer las embestidas más largas? *Gemido* [sca] tiene razón... *Jadeo*"
    $renpy.sound.play("music/ScarlettMoan.ogg", loop=True, relative_volume=15.0)
    "Dudas que muchos hombres tengan la oportunidad de estar con dos mujeres tan increíbles como [dap] y [sca] alguna vez en sus vidas."
    sca "*Gemido* ¿Y dejarme más rato vacía de Mjolnir? *Jadeo risueño* ¡Nunca! *Gemido*"
    $renpy.sound.play("music/DaphneMoan.ogg", loop=True)
    "¿Tenerlas juntas a la vez, perforando sus coños alternativamente mientras se ríen la una de la otra? Seguramente seas el único afortunado en la historia."
    scene c30s001_995pv with dissolve
    show c30s001_995v
    hide c30s001_990v
    dap "*Jadeo* Empiezo a necesitar a Mjolnir sólo para mí... *Gemido*"
    $renpy.sound.play("music/ScarlettMoan.ogg", loop=True, relative_volume=15.0)
    "Sabes que los movimientos de un túnel húmedo al otro tan solo ayudan a excitaros, pero que no os van a llevar al orgasmo."
    sca "*Gemido* Yo creo que te puedo ceder el primer turno. *Jadeo*"
    $renpy.sound.play("music/DaphneMoan.ogg", loop=True)
    "En la partida que ninguno de vosotros jugaba para decidir quién sería la primera, [dap] ha perdido."
    "Aunque perder de esa forma debe ser la forma más agradable de perder."
    scene c30s001_115h with fade
    hide c30s001_995v
    stop sound fadeout (1.5)
    "Te separas de las dos chicas y vuelves a mirar sus impresionantes cuerpos uno encima del otro."
    "Quieres grabar esa imagen en tu retina. Sabes que pasarás mucho tiempo sin volver a verlas así."
    mc "Seguidme a la cama."
    scene c30s001_130a with dissolve
    dap "*Gemido* Me gusta cuando nuestro hombre se pone dominante..."
    sca "*Jadeo* Tiene un algo animal cuando se pone así... Me pone cachonda..."
    mc "¿Vais a venir o vais a quedaros ahí comentando cada una de mis palabras?"
    scene c30s001_130b with dissolve
    sca "¡Ve a la cama ahora mismo!"
    dap "A mí me gusta comentarlo cuando te portas como un semental."
    dap "Pero te puedes ir tumbando."
    scene c30s001_130c with fade #tumbado las dos chicas de pie
    dap "Así estás perfecto. Se me ocurre una idea..."
    dap "[sca], siéntate en su cara."
    sca "Me gusta la idea."
    mc "A veces [dap] también tiene buenas ideas."
    scene c30s001_130d with dissolve
    sca "¿Qué vas a hacer tú?"
    dap "Seguir excitando a nuestro semental."
    mc "*Risa* Te aseguro que no hace falta que me sigas excitando. Dudo que lo pueda estar más."
    scene c30s001_130e with fade #dap sentada de espaldas, sca a cuatro patas en la cama
    dap "Eso lo veremos."
    mc "Eso tiene muy buena pinta."
    if sca._var("anal"):
        sca "A lo mejor [dap] quiere unirse al club de las putillas anales."
        dap "*Risa* Quizás algún día, pero no ahora."
    sca "La segunda clase fue sobre cómo hacerte una paja. Déjala que aproveche aquella clase."
    scene c30s001_950pv with fade
    show c30s001_950v
    $renpy.sound.play("music/ScarlettMoan.ogg", loop=True, relative_volume=15.0)
    "Una vez [sca] se sienta sobre tu cara, todo empieza a moverse a la vez."
    "Mientras [dap] te pajea y frota tu astil contra sus glúteos, tu lengua recorre cada pliegue del coño de [sca]."
    $renpy.sound.play("music/DaphneMoan.ogg", loop=True)
    sca "*Gemido* Nunca me cansaré de esto... *Jadeo*"
    dap "¿Te gusta esto, [mc]?"
    $renpy.sound.play("music/ScarlettMoan.ogg", loop=True, relative_volume=15.0)
    mc "*Slurp afirmativo*"
    "No vas a dejar de lamer para responder. Tan solo esperas que [dap] entienda lo que quieres decir."
    scene c30s001_945pv with fade
    show c30s001_945v
    hide c30s001_950v
    $renpy.sound.play("music/DaphneMoan.ogg", loop=True)
    "No tienes dudas de que te haya entendido, ya que continúa con el mismo ritmo maravilloso."
    dap "Ya estás muy duro. Creo que voy a empezar a cabalgarte. Quiero a Mjolnir dentro de mí."
    $renpy.sound.play("music/ScarlettMoan.ogg", loop=True, relative_volume=15.0)
    "La inteligente pelirroja te provoca sin casi tocar tu glande, sabiendo que así retrasa tu orgasmo mientras te mantiene excitado."
    sca "*Jadeo* Yo ya lo tendría dentro. *Gemido* No sé cómo puedes retenerte. *Jadeo*"
    $renpy.sound.play("music/DaphneMoan.ogg", loop=True)
    "[sca] siempre ha sido más impaciente que [dap], con lo que te puedes imaginar que los preliminares no hubieran durado tanto con ella."
    scene c30s001_955pv with fade
    show c30s001_955v
    hide c30s001_945v
    "Por suerte, se han distribuido de la mejor forma posible para alargar el momento."
    $renpy.sound.play("music/ScarlettMoan.ogg", loop=True, relative_volume=15.0)
    sca "*Gemido* Empálate ya, [dap]. *Jadeo* O me voy a correr antes de que lo hagas. *Gemido*"
    "Tu lengua recorriendo todos los rincones de su coño están acercándola al punto de no retorno."
    $renpy.sound.play("music/DaphneMoan.ogg", loop=True)
    dap "Puedes hacerlo. *Risita* Y seguir corriéndote mientras cabalgo a [mc]."
    "Te gusta el plan."
    scene c30s001_135An with dissolve
    "Pero [dap] tampoco puede aguantar más. Tiene paciencia, pero su excitación es más grande que su paciencia."
    dap "*GEMIDO* ¡Ooof! *JADEO* ¡Por fin! *GEMIDO*"
    "Su coño te recibe con un fuerte abrazo, como dos amantes que han estado largamente separados. Exactamente lo que son."
    $renpy.sound.play("music/ScarlettMoan.ogg", loop=True, relative_volume=15.0)
    sca "*JADEO* ¡Fóllatelo! *GEMIDO* ¡Fóllatela! *JADEO*"
    "Por un momento parece un general dando órdenes desde su posición privilegiada, con las mejores vistas sobre la acción."
    scene c30s001_975pv with fade
    show c30s001_975v
    hide c30s001_955v
    "[sca] cambia de posición para buscar el apoyo de tus manos mientras empieza a mover sus caderas sobre tu cara."
    sca "*Gemido* Justo ahí, [mc]. *Jadeo*"
    "Sabes que se refiere tanto a tu lengua como a cómo tus caderas suben para embestir a [dap] cuando desliza su coño alrededor de tu polla."
    $renpy.sound.play("music/DaphneMoan.ogg", loop=True)
    dap "*Jadeo* Exactamente ahí. *Gemido*"
    "La pelirroja se mueve expertamente, haciendo que Mjolnir llegue al final de su túnel del amor."
    "Eres un maestro orgulloso de tus pupilas."
    scene c30s001_965pv with fade
    show c30s001_965v
    hide c30s001_975v
    dap "*Gemido* ¡Esto es increíble! *Jadeo* ¡Me encanta! *Gemido*"
    $renpy.sound.play("music/ScarlettMoan.ogg", loop=True, relative_volume=15.0)
    if persistent.family:
        "Si pudieras responder, dirías que para ti también es fantástico. El coño de tu prima abraza tu polla como si no hubiera un mañana."
    else:
        "Si pudieras responder, dirías que para ti también es fantástico. El coño de [dap] abraza tu polla como si no hubiera un mañana."
    mc "*Slurp afirmativo*"
    if persistent.family and mc._var("edmundsStory"):
        "Pero tienes la boca ocupada con el coño de tu medio-hermana. Tendrán que descubrir qué significaba el sonido que acabas de emitir."
        sca "*Jadeo* Ahora mismo no te cambiaría la posición. *Gemido* La lengua de mi hermano es alucinante. *Jadeo*"
    else:
        "Pero tienes la boca ocupada con el coño de [sca]. Tendrán que descubrir qué significaba el sonido que acabas de emitir."
        sca "*Jadeo* Ahora mismo no te cambiaría la posición. *Gemido* La lengua de [mc] es alucinante. *Jadeo*"
    scene c30s001_960pv with fade
    show c30s001_960v
    hide c30s001_965v
    $renpy.sound.play("music/DaphneMoan.ogg", loop=True)
    "Haces lo que puedes para llevar a la rubia a su primer orgasmo, mientras observas entre sus muslos como la pelirroja te cabalga."
    "Difícilmente podrías estar en un lugar mejor ahora mismo. Aunque lo hubiera, dudas que abandonaras la compañía de las dos mujeres."
    $renpy.sound.play("music/ScarlettMoan.ogg", loop=True, relative_volume=15.0)
    sca "*Gemido* Aunque se te ve espectacular desde aquí, [dap]. *Jadeo*"
    dap "*Jadeo* Eres afortunada... *Gemido* Es lo malo de esta posición. *Jadeo*"
    "No crees que haya nada malo en esta posición."
    scene c30s001_970pv with fade
    show c30s001_970v
    hide c30s001_960v
    $renpy.sound.play("music/DaphneMoan.ogg", loop=True)
    dap "*Gemido* Parezco la niña de La Exorcista para poder veros. *Jadeo*"
    "Casi se te escapa la risa mientras esperas que no entre un cura en este momento en la habitación."
    sca "*Jadeo risueño* ¿Has visto lo que ha hecho la cochina de tu prima? *Gemido*" #Do you know what she did, your cunting cousin?
    "La voz de [sca], forzada para parecer más demoniaca, hace que por fin se te escape la risa."
    mc "*Slurp risueño*"
    call OrgasmXS4("c30s001_140") from _call_OrgasmXS4_41
    $renpy.sound.play("music/ScarlettMoan.ogg", loop=True, relative_volume=15.0)
    sca "*GEMIDO* ¡JODER! *JADEO* ¡SÍ! *GEMIDO*"
    "Las vibraciones de tu risa en su coño hacen que la rubia sea la primera en llegar al orgasmo."
    dap "*Jadeo* ¡El mío también está llegando! *Gemido*"
    "Aceleras un poco el movimiento de tus caderas, sabiendo que también estás a punto de llegar al clímax."
    call OrgasmXS4("c30s001_145") from _call_OrgasmXS4_42
    $renpy.sound.play("music/DaphneMoan.ogg", loop=True)
    dap "*JADEO* ¡DIOS MÍO! *GEMIDO* ME ESTOY ROMPIENDO. *JADEO*"
    "Notas cómo el coño de [dap] se cierra con fuerza sobre Mjolnir, mientras oleadas de placer recorren sus paredes vaginales."
    "No vas a durar mucho más."
    sca "*GEMIDO* ¡CÓRRETE DENTRO DE ELLA! *JADEO* ¡LLÉNALA! *GEMIDO*"
    if persistent.pregnancy and not dap._var("pregnant"):
        if persistent.walkthrough:
            $ wt1 = _("[dap] embarazada.")
            $ wt2 = _("Sin consecuencias.")
        else:
            $ wt1 = ""
            $ wt2 = ""
        menu:
            "Correrte dentro. Ir a por el bebé." (wt = wt1):
                $ dap._var("pregnant", True)
                $ dap._var("undiscoveredPregnancy", True)
                play sound ("music/OldMusicBox5.ogg")
            "Correrte dentro." (wt = wt2):
                pass
    call OrgasmXS4("c30s001_150") from _call_OrgasmXS4_43
    mc "¡Mpfft!"
    "Tu orgasmo llega como una explosión que, siguiendo las órdenes de [sca], llena a [dap] hasta que una parte de tu semen empieza a caer por tu astil."
    dap "*JADEO* ¡SÍ! *GEMIDO* ¡ES LA MEJOR SENSACIÓN DEL MUNDO! *JADEO*"
    "Estás de acuerdo. Los tres corriéndoos casi simultáneamente es difícilmente mejorable."
    call BlinkXS4("c30s001_155a") from _call_BlinkXS4_831
    stop sound fadeout (1.5)
    "Cuando vuestros orgasmos finalizan, os tumbáis en la cama. Es el momento de los abrazos."
    dap "Ha sido increíble. Hacía mucho que tú y yo no..."
    call BlinkXS4("c30s001_155b") from _call_BlinkXS4_832
    sca "El truco está en colarte en su habitación y decirle que es solo para dormir. *Risa* Por la mañana puedes hacer el koala."
    mc "Sabéis que podéis venir cuando queráis."
    call BlinkXS4("c30s001_155c") from _call_BlinkXS4_833
    dap "A partir de la semana que viene será más difícil. Habría que coger un avión..."
    call BlinkXS4("c30s001_155d") from _call_BlinkXS4_834
    sca "*Risa* Y seguramente llegaría tarde al trabajo. A menos que NTR tenga aviones supersónicos."
    mc "*Risa* Aún no he tenido tiempo de mirar el inventario de armas, tampoco es que me importe demasiado."
    mc "Pero dudo que tengamos aviones de caza que puedan usarse para traerte al trabajo."
    call BlinkXS4("c30s001_155e") from _call_BlinkXS4_835
    dap "*Risa* Tu novio es muy desagradable, [sca]. Mira que no prestarte un caza para que vengas a servir cafés..."
    call BlinkXS4("c30s001_155f") from _call_BlinkXS4_836
    sca "*Risa* ¿Mi novio? ¡También es el tuyo!"
    call BlinkXS4("c30s001_155e") from _call_BlinkXS4_837
    dap "*Risa* Lo sé, pero por mí seguro que lo haría. Aunque solo fuera porque puedo votar por despedirlo en la junta de accionistas."
    dap "Además, si hace algo malo, es tu novio. Si hace algo bueno, es el mío. *Risa*"
    mc "*Risa* Un avión de caza no lo sé, pero tenemos el avión de la empresa si queréis hacer una visita."
    mc "Era el plan antes de que [sca] consiguiera el trabajo, ¿no?"
    call BlinkXS4("c30s001_155g") from _call_BlinkXS4_838
    dap "Bueno, entre el trabajo de [sca] y la llegada de las chicas nuevas no lo vamos a poder hacer ahora."
    dap "Después empiezan las clases y..."
    call BlinkXS4("c30s001_155h") from _call_BlinkXS4_839
    sca "Quizás en Navidad o en Acción de Gracias. Y las dos queremos ir a trabajar en NTR en verano."
    mc "¿En plan becarias?"
    call BlinkXS4("c30s001_155i") from _call_BlinkXS4_840
    dap "Sí. Quiero... queremos aprender qué podemos hacer en la empresa. Queremos ayudar en el cambio de orientación."
    call BlinkXS4("c30s001_155j") from _call_BlinkXS4_841
    sca "Pero primero tenemos que acabar el curso. Ahora mismo no nos enteraríamos de la mitad de lo que nos explicaran."
    sca "Con lo que, como máximo, te visitaremos unos días."
    mc "Va a ser duro no veros durante tanto tiempo."
    scene c30s001_155k with dissolve
    sca "¿Sabes lo que también está duro?"
    dap "Seguro que has estado pensando en repetir esto cuando vayamos a verte."
    mc "*Risa* No voy a negarlo..."
    call BlinkXS4("c30s001_155l") from _call_BlinkXS4_842
    dap "Pues creo que es el turno de [sca]..."
    call BlinkXS4("c30s001_155t") from _call_BlinkXS4_843
    sca "¿Cambiamos de posición?"
    call BlinkXS4("c30s001_155m") from _call_BlinkXS4_844
    dap "Yo me voy a quedar fuera de esta ronda. Me ha destrozado."
    mc "Lo siento..."
    call BlinkXS4("c30s001_155n") from _call_BlinkXS4_845
    sca "Creo que se refiere a destrozada en plan bien..."
    call BlinkXS4("c30s001_155o") from _call_BlinkXS4_846
    dap "Sí. Pero dudo que ahora mismo pueda seguir."
    mc "Dejadme un momento para limpiarme y vuelvo en seguida."
    scene c30s001_155p with fade
    sca "No hay nada que no pueda limpiar yo."
    dap "Pero... ha estado dentro de mí..."
    call BlinkXS4("c30s001_155r") from _call_BlinkXS4_847
    sca "A mí me da lo mismo. No es como si te estuviera comiendo el coño. Eso nunca lo haría."
    call BlinkXS4("c30s001_155s") from _call_BlinkXS4_848
    dap "Ni yo te dejaría hacerlo..."
    call BlinkXS4("c30s001_160") from _call_BlinkXS4_849
    sca "Precisamente por eso no lo haría nunca. Si [mc] y tú tuvierais ese fetiche..."
    sca "No me gustan las chicas, pero por cumplir los fetiches de mi novio y de mi mejor amiga, estaría dispuesta a hacerlo."
    sca "Pero serías la única con la que me atrevería."
    call BlinkXS4("c30s001_165") from _call_BlinkXS4_850
    dap "No contestes, [mc]. [sca] ha dicho si los dos tuviéramos ese fetiche, y yo no lo tengo."
    dap "Con lo que podemos dejar esta conversación y seguir con lo que ibais a hacer."
    mc "Me parece una buena idea. ¿Cómo queréis...?"
    scene c30s001_935pv with fade
    show c30s001_935v
    hide c30s001_970v
    "No te dejan acabar la frase. [sca] se mete a Mjolnir en la boca y [dap] se inclina buscando tus labios."
    "Tres bocas ocupadas que dicen todo lo necesario sin precisar de palabras."
    sca "*Slurp*"
    "Bueno, algún sonido sí que producen esas bocas, al menos una de ellas."
    "Sigues pensando que las dos chicas aprendieron demasiado rápido tus lecciones."
    scene c30s001_930pv with fade
    show c30s001_930v
    hide c30s001_935v
    "La limpieza que [sca] está haciendo de tu polla es espectacular."
    "Aunque no puedas verla, puedes notar cómo su lengua recorre tu glande."
    sca "*Slurp*"
    "A estas alturas, tu polla debe estar limpia como una patena."
    "La limpieza ha pasado a un segundo plano hace rato y la chica se dedica a prepararte para ella."
    scene c30s001_940pv with fade
    show c30s001_940v
    hide c30s001_930v
    "Mientras tanto, [dap] no deja a tu boca descansar."
    dap "*Gemido*"
    "Sus gemidos resuenan en el interior de tu boca, demostrando lo excitada que está."
    sca "*Slurp*"
    "Si [sca] sigue así mucho rato más, vas a descargar tu semen en su boca."
    call BlinkXS4("c30s001_170") from _call_BlinkXS4_851
    "Como si te leyera la mente, o como una buena alumna que sabe leer tu lenguaje corporal, [sca] para la maravillosa mamada."
    sca "Creo que esto ya está. No queremos que te corras ahora, ¿no?"
    mc "Prefiero hacerlo dentro tuyo."
    call BlinkXS4("c30s001_175") from _call_BlinkXS4_852
    dap "Túmbate. Se me ha ocurrido una posición."
    mc "Sorprendedme..."
    scene c30s001_180a with dissolve
    "Te tumbas esperando las instrucciones de la pelirroja."
    dap "[sca], súbete encima de [mc]..."
    sca "¿Qué vas a hacer tú?"
    dap "*Risita* Darte apoyo..."
    scene c30s001_180b with fade #Partir de 915
    "Lo de darle apoyo a [sca] es literal. [dap] se sitúa a su espalda y ambas entrelazan sus manos."
    dap "Ya podéis empezar a moveros. Quiero saber cómo es notaros follar si eliminamos el componente visual."
    mc "*Risa* Me encantan tus experimentos."
    sca "Pero tú..."
    dap "No os preocupéis por mí. Ya os he dicho que no puedo más hoy."
    scene c30s001_915pv with fade
    show c30s001_915v
    hide c30s001_940v
    $renpy.sound.play("music/ScarlettMoan.ogg", loop=True, relative_volume=15.0)
    "[sca] empieza a cabalgarte sin hacer más preguntas usando las manos de [dap] como apoyo."
    sca "*Gemido* Casi no podía aguantar a tenerte dentro. *Jadeo*"
    "No sabes cuánto hace que has entrado en la habitación, pero entiendes perfectamente a la chica."
    dap "Es... diferente..."
    "La voz de la pelirroja suena analítica a la vez que excitada. Sus caderas se mueven buscando una polla que no está ahí."
    scene c30s001_920v with fade
    show c30s001_920v
    hide c30s001_915v
    "[sca] te cabalga expertamente, como si hubierais hecho esto miles de veces."
    sca "*Jadeo* Es increíble... *Gemido* Estás llegando a todos los puntos correctos... *Jadeo*"
    "Sus orgasmos anteriores, la excitación de ver cómo te follabas a su amiga y de la mamada hacen que esté super excitada."
    $renpy.sound.play("music/DaphneMoan.ogg", loop=True)
    dap "*Gemido* Me gusta notar cómo os movéis..."
    "El primer gemido de [dap] hace su aparición. No te sorprende. Sin el elemento visual, es casi como si fuera porno táctil."
    scene c30s001_910v with fade
    show c30s001_910v
    hide c30s001_920v
    $renpy.sound.play("music/ScarlettMoan.ogg", loop=True, relative_volume=15.0)
    "Y la imaginación de [dap] es muy poderosa, acrecentada al notar los movimientos de su hermana de otra madre."
    "Estás seguro de que sus manos entrelazadas transmiten todo lo que la otra necesita saber."
    dap "*Jadeo* Me encanta... *Gemido* Me estoy poniendo muy caliente... *Jadeo*"
    sca "*Gemido risueño* ¿No decías que no podías más? *Jadeo* ¡Mentirosa! *Gemido risueño*"
    "Y, como hermanas que son, no dejan pasar la oportunidad de meterse la una con la otra."
    scene c30s001_925v with fade
    show c30s001_925v
    hide c30s001_910v
    $renpy.sound.play("music/DaphneMoan.ogg", loop=True)
    dap "*Gemido risueño* ¡Folla y calla! *Jadeo* Estás a punto de llegar al orgasmo. *Gemido*"
    "La pelirroja ha notado los cambios en los movimientos de la rubia a la vez que tú."
    "Son cambios sutiles que anuncian que su orgasmo está a punto de llegar."
    $renpy.sound.play("music/ScarlettMoan.ogg", loop=True, relative_volume=15.0)
    sca "*Jadeo* ¡Sí! *Gemido* ¡Está llegando! *Jadeo*"
    "Otra vez vuestros orgasmos van a ser casi simultáneos. El tuyo también está llamando a las puertas."
    "Te sientes un poco decepcionado porque [dap] no se una a esta ronda de orgasmos."
    call OrgasmXS4("c30s001_185") from _call_OrgasmXS4_44
    sca "*GEMIDO* ¡JODER! *JADEO* ¡YA ESTÁ AQUÍ! *GEMIDO*"
    "La camarera explota alrededor de tu polla... O implosiona, si hay que tener en cuenta cómo su coño se cierra sobre tu astil."
    "Sus paredes vaginales empiezan a masajear tu polla con una fuerza impresionante para un cuerpo tan delgado."
    if persistent.pregnancy and not sca._var("pregnant"):
        if persistent.walkthrough:
            $ wt1 = _("[sca] embarazada.")
            $ wt2 = _("Sin consecuencias.")
        else:
            $ wt1 = ""
            $ wt2 = ""
        menu:
            "Correrte dentro. Ir a por el bebé." (wt = wt1):
                $ sca._var("pregnant", True)
                $ sca._var("undiscoveredPregnancy", True)
                play sound ("music/OldMusicBox5.ogg")
            "Correrte dentro." (wt = wt2):
                pass
    call OrgasmXS4("c30s001_190") from _call_OrgasmXS4_45
    mc "¡Mpfft!"
    "No puedes evitar descargar una enorme cantidad de tu semilla dentro de la chica."
    "El orgasmo de [sca] te ha llevado al tuyo sin poder remediarlo."
    scene c30s001_195An with dissolve
    "Alzas tu muslo para presionar contra la entrepierna de [dap], intentando incluirla en el momento."
    "Puedes notar su humedad y su sorpresa al percibir tu pierna haciendo contacto con sus labios."
    $renpy.sound.play("music/DaphneMoan.ogg", loop=True)
    dap "*GEMIDO* ¡OH! *JADEO*"
    call OrgasmXS4("c30s001_200") from _call_OrgasmXS4_46
    dap "*JADEO* ¡SÍ! *GEMIDO*"
    "Para sorpresa de nadie, [dap] se une a los orgasmos compartidos entre los tres mientras [sca] aún se retuerce alrededor de Mjolnir."
    if persistent.family:
        "La pelirroja se ha puesto más cachonda de lo que estaba dispuesta a aceptar mientras percibía cómo su pseudo-hermana y su primo follaban."
    else:
        "La pelirroja se ha puesto más cachonda de lo que estaba dispuesta a aceptar mientras percibía cómo su pseudo-hermana y tú follabais."
    scene c30s001_205a with fade
    stop music fadeout (1.5)
    stop sound fadeout (1.0)
    "Al cabo de unos minutos, cuando todos os habéis recuperado de vuestros orgasmos..."
    play music ("music/Stardust.ogg")
    mc "Creo que habéis superado la última lección con una nota muy alta."
    dap "*Risa* Si fundaras una academia de sexo te pondría cinco estrellas en Foogle Maps."
    sca "Academia Sexual [mc]. Mande a su hija a estudiar aquí y volverá no siendo la misma. Eso es si vuelve, claro."
    sca "*Risa* Solo para chicas."
    mc "*Risa* Creo que podríamos llegar a un acuerdo con la universidad si el decano no fuera un gilipollas."
    mc "Servicios integrales para estudiantes femeninas. Allí se forman profesionalmente y aquí se divierten mientras aprenden."
    scene c30s001_205b with dissolve
    dap "¡Aprender para el futuro profesional es divertido!"
    sca "Por muy divertido que sea, prefiero esto."
    scene c30s001_205c with dissolve
    dap "Yo también, pero no me gusta que nadie diga que ir a clase es aburrido."
    sca "*Risa* Eres una nerd."
    sca "¿Vamos a lavarnos?"
    mc "¿Ya os vais? ¿No os vais a quedar a dormir?"
    scene c30s001_205d with fade
    sca "Ahora volvemos. Aún tengo el sabor de Mjolnir en la boca."
    sca "Una cosa es que te deje besarme recién despertada y otra que te deje besarme con sabor a semen en la boca. Tengo que enjuagarme."
    dap "Sería... raro..."
    mc "¿Nunca os habéis chupado los dedos después de masturbaros?"
    scene c30s001_205e with hpunch
    sca "¡Creía que los chicos no hacíais eso!" (multiple=2)
    dap "¿Qué? ¿Has probado tu semen?" (multiple=2)
    mc "*Risa* No, no lo he hecho nunca, pero no es lo mismo."
    scene c30s001_205e2 with dissolve
    dap "Sea como sea, conmigo no lo vas a probar."
    sca "Ni conmigo. Ahora que lo has dicho, puedo notar más todavía tu sabor mezclado con el de [dap]."
    scene c30s001_205f with dissolve
    sca "No te duermas." (multiple=2)
    dap "Volvemos en un momento." (multiple=2)
    mc "¿Vais a ir desnudas?"
    sca "Todo el mundo sabe que estamos aquí. Nadie va a subir a esta planta."
    scene c30s001_205g with dissolve
    "A veces te sigue sorprendiendo que las chicas se informen las unas a las otras sobre cuándo van a hacerte una visita."
    if kat._var("route"):
        "Es comprensible. Si no lo hicieran, [kat] podría venir a por otro beso de buenas noches y encontrarse en una situación incómoda."
    else:
        "Es comprensible. Si no lo hicieran, [kat] podría venir a por otro abrazo de buenas noches y encontrarse en una situación incómoda."
    "No eres capaz de descubrir si la situación sería incómoda para ella por las chicas o por ti."
    scene black with dissolve
    "Sigues pensando en eso cuando tus parpadeos pasan de durar una décima de segundo a varios segundos... o minutos."
    "Esperar que las dos chicas vuelvan mientras te entra la somnolencia post-orgasmo es demasiado para ti en un día largo."
    dap "*Susurrando* No hagas ruido. Se ha dormido."
    sca "*Susurrando* Le he dicho que no lo hiciera. *Risita*"
    dap "*Susurrando* Hemos tardado demasiado..."
    sca "*Susurrando* ¡No quedaba colutorio en este baño!"
    scene c30s001_205h with dissolve
    mc "Chicas, puedo escucharos."
    dap "¿Te hemos despertado?"
    mc "No me había dormido... o eso creo..."
    sca "Sigue durmiendo... O empieza a dormir."
    scene c30s001_205i with dissolve
    "La rubia te da un beso con sabor a enjuague bucal."
    sca "Buenas noches, mi amor."
    mc "Buenas noches, preciosa."
    scene c30s001_205j with dissolve
    "En cuanto tu boca queda libre, es ocupada por la de [dap], que tiene el mismo sabor que la de [sca]."
    dap "Buenas noches, [mc]."
    mc "Buenas noches, [dap]."
    scene c30s001_205k with dissolve
    "Las dos chicas se tumban a izquierda y derecha de ti, apoyando sus cabezas sobre tus hombros."
    stop music fadeout (1.5)
    "No hay nada mejor que dormir con dos mujeres a las que adoras."
    return
label c30s001_noDapScaLewd:
    scene c30s001_1000a with dissolve
    "Subes a tu habitación y juegas un rato a My Residence, en la que tienes una tórrida escena con Laura y Sky."
    "Las dos chicas cada vez se comportan más como si fueran hermanas de elección."
    "Ese comportamiento y su aspecto hacen que te recuerden a [dap] y a [sca]."
    "El desarrollador del juego incluso ha usado un sofá que se parece al tuyo."
    return
label checkPregnancies:
    $ pregnanciesNotDiscovered = 0
    $ textPregnanciesNotDiscovered = ""
    if eri._var("route") and not eri._var("pregnancyDiscovered"):
        $ pregnanciesNotDiscovered = pregnanciesNotDiscovered + 1
        $ textPregnanciesNotDiscovered = textPregnanciesNotDiscovered + eri.name.first_name
    if sam._var("route") and not sam._var("pregnancyDiscovered"):
        $ pregnanciesNotDiscovered = pregnanciesNotDiscovered + 1
        if textPregnanciesNotDiscovered != "":
            $ textPregnanciesNotDiscovered = textPregnanciesNotDiscovered + ", " + sam.nick
        else:
            $ textPregnanciesNotDiscovered = textPregnanciesNotDiscovered + sam.nick
    if emm._var("route") and not emm._var("pregnancyDiscovered"):
        $ pregnanciesNotDiscovered = pregnanciesNotDiscovered + 1
        if textPregnanciesNotDiscovered != "":
            $ textPregnanciesNotDiscovered = textPregnanciesNotDiscovered + ", " + emm.name.first_name
        else:
            $ textPregnanciesNotDiscovered = textPregnanciesNotDiscovered + emm.name.first_name
    if dap._var("route") and not dap._var("pregnancyDiscovered"):
        $ pregnanciesNotDiscovered = pregnanciesNotDiscovered + 1
        if textPregnanciesNotDiscovered != "":
            $ textPregnanciesNotDiscovered = textPregnanciesNotDiscovered + ", " + dap.name.first_name
        else:
            $ textPregnanciesNotDiscovered = textPregnanciesNotDiscovered + dap.name.first_name
    if sim._var("route") and not sim._var("pregnancyDiscovered"):
        $ pregnanciesNotDiscovered = pregnanciesNotDiscovered + 1
        if textPregnanciesNotDiscovered != "":
            $ textPregnanciesNotDiscovered = textPregnanciesNotDiscovered + ", " + sim.name.first_name
        else:
            $ textPregnanciesNotDiscovered = textPregnanciesNotDiscovered + sim.name.first_name
    if nor._var("route"):
        if nor._var("undiscoveredPregnancy") or not nor._var("pregnant"):
            $ pregnanciesNotDiscovered = pregnanciesNotDiscovered + 1
            if textPregnanciesNotDiscovered != "":
                $ textPregnanciesNotDiscovered = textPregnanciesNotDiscovered + ", " + nor.name.first_name
            else:
                $ textPregnanciesNotDiscovered = textPregnanciesNotDiscovered + nor.name.first_name
    if sca._var("route"):
        if sca._var("undiscoveredPregnancy") or not sca._var("pregnant"):
            $ pregnanciesNotDiscovered = pregnanciesNotDiscovered + 1
            if textPregnanciesNotDiscovered != "":
                $ textPregnanciesNotDiscovered = textPregnanciesNotDiscovered + ", " + sca.name.first_name
            else:
                $ textPregnanciesNotDiscovered = textPregnanciesNotDiscovered + sca.name.first_name
    if eil._var("route"):
        if eil._var("undiscoveredPregnancy") or not eil._var("pregnant"):
            $ pregnanciesNotDiscovered = pregnanciesNotDiscovered + 1
            if textPregnanciesNotDiscovered != "":
                $ textPregnanciesNotDiscovered = textPregnanciesNotDiscovered + ", " + eil.name.first_name
            else:
                $ textPregnanciesNotDiscovered = textPregnanciesNotDiscovered + eil.name.first_name
    if mar._var("route"):
        if mar._var("undiscoveredPregnancy") or not mar._var("pregnant"):
            $ pregnanciesNotDiscovered = pregnanciesNotDiscovered + 1
            if textPregnanciesNotDiscovered != "":
                $ textPregnanciesNotDiscovered = textPregnanciesNotDiscovered + ", " + mar.name.first_name
            else:
                $ textPregnanciesNotDiscovered = textPregnanciesNotDiscovered + mar.name.first_name
    if kia._var("route") and not kia._var("pregnancyDiscovered"):
        $ pregnanciesNotDiscovered = pregnanciesNotDiscovered + 1
        if textPregnanciesNotDiscovered != "":
            $ textPregnanciesNotDiscovered = textPregnanciesNotDiscovered + ", " + kia.name.first_name
        else:
            $ textPregnanciesNotDiscovered = textPregnanciesNotDiscovered + kia.name.first_name
    if bet._var("route") and not bet._var("pregnancyDiscovered"):
        $ pregnanciesNotDiscovered = pregnanciesNotDiscovered + 1
        if textPregnanciesNotDiscovered != "":
            $ textPregnanciesNotDiscovered = textPregnanciesNotDiscovered + ", " + bet.name.first_name
        else:
            $ textPregnanciesNotDiscovered = textPregnanciesNotDiscovered + bet.name.first_name
    if eva._var("route") and not eva._var("pregnancyDiscovered"):
        $ pregnanciesNotDiscovered = pregnanciesNotDiscovered + 1
        if textPregnanciesNotDiscovered != "":
            $ textPregnanciesNotDiscovered = textPregnanciesNotDiscovered + ", " + eva.name.first_name
        else:
            $ textPregnanciesNotDiscovered = textPregnanciesNotDiscovered + eva.name.first_name
    if meg._var("route"):
        if meg._var("undiscoveredPregnancy") or not meg._var("pregnant"):
            $ pregnanciesNotDiscovered = pregnanciesNotDiscovered + 1
            if textPregnanciesNotDiscovered != "":
                $ textPregnanciesNotDiscovered = textPregnanciesNotDiscovered + ", " + meg.name.first_name
            else:
                $ textPregnanciesNotDiscovered = textPregnanciesNotDiscovered + meg.name.first_name
    if sai._var("route") and not sai._var("pregnancyDiscovered"):
        $ pregnanciesNotDiscovered = pregnanciesNotDiscovered + 1
        if textPregnanciesNotDiscovered != "":
            $ textPregnanciesNotDiscovered = textPregnanciesNotDiscovered + ", " + sai.name.first_name
        else:
            $ textPregnanciesNotDiscovered = textPregnanciesNotDiscovered + sai.name.first_name
    if oma._var("route"):
        if oma._var("undiscoveredPregnancy") or not oma._var("pregnant"):
            $ pregnanciesNotDiscovered = pregnanciesNotDiscovered + 1
            if textPregnanciesNotDiscovered != "":
                $ textPregnanciesNotDiscovered = textPregnanciesNotDiscovered + ", " + oma.name.first_name
            else:
                $ textPregnanciesNotDiscovered = textPregnanciesNotDiscovered + oma.name.first_name
    if mad._var("route") and not mad._var("pregnancyDiscovered"):
        $ pregnanciesNotDiscovered = pregnanciesNotDiscovered + 1
        if textPregnanciesNotDiscovered != "":
            $ textPregnanciesNotDiscovered = textPregnanciesNotDiscovered + ", " + mad.nick
        else:
            $ textPregnanciesNotDiscovered = textPregnanciesNotDiscovered + mad.nick
    if deb._var("route") and not deb._var("pregnancyDiscovered"):
        $ pregnanciesNotDiscovered = pregnanciesNotDiscovered + 1
        if textPregnanciesNotDiscovered != "":
            $ textPregnanciesNotDiscovered = textPregnanciesNotDiscovered + ", " + deb.nick
        else:
            $ textPregnanciesNotDiscovered = textPregnanciesNotDiscovered + deb.nick
    if kim._var("route") and not kim._var("pregnancyDiscovered"):
        $ pregnanciesNotDiscovered = pregnanciesNotDiscovered + 1
        if textPregnanciesNotDiscovered != "":
            $ textPregnanciesNotDiscovered = textPregnanciesNotDiscovered + ", " + kim.name.first_name
        else:
            $ textPregnanciesNotDiscovered = textPregnanciesNotDiscovered + kim.name.first_name
    if lis._var("route") and not lis._var("pregnancyDiscovered"):
        $ pregnanciesNotDiscovered = pregnanciesNotDiscovered + 1
        if textPregnanciesNotDiscovered != "":
            $ textPregnanciesNotDiscovered = textPregnanciesNotDiscovered + ", " + lis.name.first_name
        else:
            $ textPregnanciesNotDiscovered = textPregnanciesNotDiscovered + lis.name.first_name
    return
label c30s002_pregnancyTests:
    if _in_replay:
        $ mc._var("relationships", 0, "set")
        call mrS3_ama_route from _call_mrS3_ama_route_15
        call mrS3_sai_route from _call_mrS3_sai_route_20
        if sai._var("route"):
            menu:
                "¿Ha descubierto que está embarazada?"
                "Sí.":
                    $ sai._var("discoveredPregnancy", True)
                    $ sai._var("undiscoveredPregnancy", false)
                "No.":
                    $ sai._var("discoveredPregnancy", False)
        call mrS3_mar_route from _call_mrS3_mar_route_41
        if mar._var("route"):
            menu:
                "¿Ha descubierto que está embarazada?"
                "Sí.":
                    $ mar._var("discoveredPregnancy", True)
                    $ mar._var("undiscoveredPregnancy", false)
                "No.":
                    $ mar._var("discoveredPregnancy", False)
        call mrS3_emm_route from _call_mrS3_emm_route_40
        call mrS3_eri_route from _call_mrS3_eri_route_31
        if eri._var("route"):
            menu:
                "¿Ha descubierto que está embarazada?"
                "Sí.":
                    $ eri._var("discoveredPregnancy", True)
                "No.":
                    $ eri._var("discoveredPregnancy", False)
        call mrS3_nor_route from _call_mrS3_nor_route_31
        if nor._var("route"):
            menu:
                "¿Ha descubierto que está embarazada?"
                "Sí.":
                    $ nor._var("discoveredPregnancy", True)
                "No.":
                    $ nor._var("discoveredPregnancy", False)
        call mrS3_dap_route from _call_mrS3_dap_route_32
        if dap._var("route"):
            menu:
                "¿Ha descubierto que está embarazada?"
                "Sí.":
                    $ dap._var("discoveredPregnancy", True)
                "No.":
                    $ dap._var("discoveredPregnancy", False)
        call mrS3_sca_route from _call_mrS3_sca_route_26
        if sca._var("route"):
            menu:
                "¿Ha descubierto que está embarazada?"
                "Sí.":
                    $ sca._var("discoveredPregnancy", True)
                "No.":
                    $ sca._var("discoveredPregnancy", False)
        call mrS3_eil_route from _call_mrS3_eil_route_24
        if eil._var("route"):
            menu:
                "¿Ha descubierto que está embarazada?"
                "Sí.":
                    $ eil._var("discoveredPregnancy", True)
                "No.":
                    $ eil._var("discoveredPregnancy", False)
        call mrS3_sam_route from _call_mrS3_sam_route_22
        if sam._var("route"):
            menu:
                "¿Ha descubierto que está embarazada?"
                "Sí.":
                    $ sam._var("discoveredPregnancy", True)
                "No.":
                    $ sam._var("discoveredPregnancy", False)
        call mrS3_sim_route from _call_mrS3_sim_route_22
        if sim._var("route"):
            menu:
                "¿Ha descubierto que está embarazada?"
                "Sí.":
                    $ sim._var("discoveredPregnancy", True)
                "No.":
                    $ sim._var("discoveredPregnancy", False)
        call mrS3_oma_route from _call_mrS3_oma_route_17
        if oma._var("route"):
            menu:
                "¿Ha descubierto que está embarazada?"
                "Sí.":
                    $ oma._var("discoveredPregnancy", True)
                "No.":
                    $ oma._var("discoveredPregnancy", False)
        call mrS3_eva_route from _call_mrS3_eva_route_17
        call mrS3_mad_route from _call_mrS3_mad_route_17
        call mrS3_meg_route from _call_mrS3_meg_route_8
        if meg._var("route"):
            menu:
                "¿Ha descubierto que está embarazada?"
                "Sí.":
                    $ meg._var("discoveredPregnancy", True)
                "No.":
                    $ meg._var("discoveredPregnancy", False)
        call mrS3_kim_route from _call_mrS3_kim_route_12
        call mrS3_kat_route from _call_mrS3_kat_route_4
        call mrS3_deb_route from _call_mrS3_deb_route_26
        call mrS3_lis_route from _call_mrS3_lis_route_24
        call mrS3_bet_route from _call_mrS3_bet_route_10
        call mrS3_kia_route from _call_mrS3_kia_route_17
    scene black with dissolve
    centered "{size=+20}{b}DÍA 34 – DOMINGO{/b}{/size}"
    scene c30s002_150e with fade
    "A la mañana siguiente, después de desayunar sin ver a nadie en la cocina, subes a tu habitación a ponerte el bañador."
    "Sabes que, si bajas a la piscina, seguro que encontrarás a alguna de las chicas."
    "Cuando aún no te ha dado tiempo de ponértelo..."
    play sound ("music/knock.ogg")
    "*Knock-Knock*"
    play music ("music/Looking-Forward.ogg")
    ama "*A través de la puerta* Soy yo, ¿puedo pasar?"
    mc "Pasa, [ama]."
    if ama._var("route"):
        call KissXS3 ("c30s002_150") from _call_KissXS3_17
    call BlinkXS3("c30s002_150") from _call_BlinkXS3_868
    mc "¿Qué tal, [ama]?"
    ama "Bien. Vengo en una visita semiprofesional."
    mc "¿Pasa algo en NTR? ¿A qué te refieres con 'semi'?"
    call BlinkXS3("c30s002_155") from _call_BlinkXS3_869
    ama "*Risita* No, nada de lo que preocuparte."
    ama "Vengo a llevarme los test de embarazo."
    mc "¿Por qué? Siempre los he tenido yo y no ha habido ningún problema."
    mc "Ni siquiera cuando había que mantener el secreto de con quién estaba saliendo."
    call BlinkXS3("c30s002_160") from _call_BlinkXS3_870
    ama "Es por una cuestión práctica. Nos vamos el jueves. También venía a decírtelo."
    mc "¿El jueves? ¿Tan pronto? Creía que sería hacia final de semana..."
    mc "Meemaw y Tía [bet] vuelven el martes..."
    call BlinkXS3("c30s002_165") from _call_BlinkXS3_871
    ama "Por eso nos vamos el jueves, para que [bet] pueda descansar un poco del viaje antes de subirla de nuevo a un avión."
    ama "Si dejáramos que Aaron decidiera, [bet] no saldría del aeropuerto. La montaría directamente en el avión de la compañía."
    mc "¿Alguien le ha dicho a Aaron la edad que tiene [bet]? Del Atlántico al Pacífico y vuelta al Caribe el mismo día..."
    call BlinkXS3("c30s002_170") from _call_BlinkXS3_872
    ama "Sí, ya se lo he dicho. Aunque no le he dicho que quiero pasar tiempo con Meemaw antes de irnos..."
    mc "*Risa* ¿Ahora también la llamas Meemaw?"
    call BlinkXS3("c30s002_175") from _call_BlinkXS3_873
    ama "*Risita* Es culpa tuya. Oyéndote hablar de ella... Has conseguido que piense en ella como Meemaw en vez de como Olivia..."
    mc "*Risa* Seguro que le hace ilusión. Hace tiempo que te cuenta entre sus nietas."
    if persistent.family:
        mc "Ahora sólo falta que llames 'Mamá' a mi madre."
    else:
        mc "Ahora sólo falta que llames 'Mamá' a [mar]."
    call BlinkXS3("c30s002_180") from _call_BlinkXS3_874
    ama "Sobre eso..."
    mc "*Risa* ¡Lo sabía! ¡Ya lo has hecho! Por alguna razón me hace muy feliz que lo hagas."
    scene c30s002_185abn with fade
    ama "A [mar] también pareció gustarle una vez pasó la sorpresa inicial..."
    ama "[kim] y yo estábamos ayer ayudándola a cocinar, y sabes que [kim] hace días que la llama así..."
    mc "Sí, creo que empezó en la fiesta de la piscina."
    call BlinkXS3("c30s002_190") from _call_BlinkXS3_875
    ama "Pues acabé diciéndole, 'Ya he acabado con esto, Mamá'."
    mc "Me imagino la cara de sorpresa..."
    scene c30s002_185bbn with fade
    ama "Duró un par de décimas de segundo. Después, me dio un abrazo de aquellos que casi te rompen un par de costillas."
    mc "*Risa* Y me imagino a la pobre [kim] con un cuchillo en la mano cortando zanahorias y sin saber qué hacer."
    call BlinkXS3("c30s002_195") from _call_BlinkXS3_876
    ama "*Risita* No te equivocas demasiado. Pero [mar] y yo nos dimos cuenta, y la incluimos en el abrazo en seguida."
    mc "Y os pusisteis a llorar durante media hora, ¿verdad?"
    scene c30s002_185cbn with fade
    ama "*Risa* No voy a contestar a esa pregunta."
    mc "No hace falta que lo hagas. Creo que os conozco lo suficiente para saber la respuesta."
    call BlinkXS3("c30s002_200") from _call_BlinkXS3_877
    ama "Pero volviendo a los tests de embarazo..."
    mc "Sí, ¿por qué quieres llevártelos? ¿Qué tiene que ver que nos vayamos el jueves a Aruba?"
    call BlinkXS3("c30s002_205") from _call_BlinkXS3_878
    if sai._var("route") and not sai._var("discoveredPregnancy") or mar._var("route") and not mar._var("discoveredPregnancy") or nor._var("route") and not nor._var("discoveredPregnancy") or sam._var("route") and not sam._var("discoveredPregnancy") or sim._var("route") and not sim._var("discoveredPregnancy") or eri._var("route") and not eri._var("discoveredPregnancy") or dap._var("route") and not dap._var("discoveredPregnancy") or sca._var("route") and not sca._var("discoveredPregnancy") or eil._var("route") and not eil._var("discoveredPregnancy") or oma._var("route") and not oma._var("discoveredPregnancy") or meg._var("route") and not meg._var("discoveredPregnancy") or emm._var("route") or eva._var("route") or mad._var("route") or kim._var("route") or deb._var("route") or lis._var("route") or bet._var("route") or kia._var("route") or kat._var("route"):
        ama "¿No piensas tener sexo de despedida entre hoy y el jueves con ninguna de las chicas que pueda necesitar el test una vez nos hayamos ido?"
    call checkPregnancies from _call_checkPregnancies_1
    if pregnanciesNotDiscovered == 1:
        "[textPregnanciesNotDiscovered] todavía no se lo ha hecho..."
    elif pregnanciesNotDiscovered > 1:
        "Todavía hay chicas que no se lo han hecho. [textPregnanciesNotDiscovered]..."
    ama "Y, si no se usa ningún test más, habrán caducado para cuando vuelvas y los puedas necesitar otra vez."
    ama "Es mejor que los tenga [eva] en la base para poder deshacerse de ellos."
    mc "Tienes razón, no lo había pensado."
    call BlinkXS3("c30s002_215") from _call_BlinkXS3_879
    ama "*Risa* Eso ha sonado como [emm]." (multiple=2)
    mc "*Risa* Eso lo podría haber dicho [emm]." (multiple=2)
    mc "A veces creo que nos reímos demasiado de ella."
    call BlinkXS3("c30s002_220") from _call_BlinkXS3_880
    ama "Deberías saber a estas alturas que a ella le encanta que hagamos bromas sobre que no piensa."
    ama "Incluso dijo que pensó en teñirse de rubia, para parecer más tonta, pero no lo hizo porque nadie nos distinguiría..."
    mc "*Risa* Aunque os cortarais el pelo igual, yo seguiría sabiendo quién es [ama] y quién es [emm]."
    call BlinkXS3("c30s002_225") from _call_BlinkXS3_881
    ama "Ya lo demostraste con [eva] y [dap]. [eva] aún habla de ello."
    mc "¿Probó ese truco con alguien más?"
    call BlinkXS3("c30s002_230") from _call_BlinkXS3_882
    ama "No, tú fuiste el primero y, como el resultado salió bien, no quiere arriesgarse a que el siguiente experimento salga mal. *Risita*"
    ama "Además, tú fallaste la primera vez, en el desayuno de disfraces."
    mc "¡No sabía que existíais! No podía pensar que había una persona idéntica a [eri] por ahí."
    call BlinkXS3("c30s002_235") from _call_BlinkXS3_883
    ama "Las dos lo sabemos, [mc]. Pero... después de conoceros... [eva] quiso hacer la prueba."
    ama "Y salió bien, no te engañó. Y después, en la cocina de [nor], nadie las confundió tampoco."
    call BlinkXS3("c30s002_240") from _call_BlinkXS3_884
    ama "Quizás algún día vuelva a probarlo, quizás con las chicas nuevas cuando lleguen y aún no la conozcan demasiado."
    ama "Pero no creo que lo vuelva a probar con nadie de la familia... Al menos por un tiempo."
    mc "*Risa* ¿Hasta que nos olvidemos de la última vez?"
    if ama._var("route"):
        call KissXS3 ("c30s002_150") from _call_KissXS3_18
    call BlinkXS3("c30s002_150") from _call_BlinkXS3_885
    ama "Exacto. Y ahora me voy a llevar esos tests de embarazo. Tengo un montón de cosas que hacer hoy."
    mc "Están en el armario. Espera que te los doy."
    scene black with dissolve
    stop music fadeout (1.5)
    "[ama] coge la caja con los tests y te deja sólo en tu habitación."
    return
label c30s002_KatKiss:
    if _in_replay:
        $ mc._var("relationships", 0, "set")
        call mrS3_rels from _call_mrS3_rels_37
    scene c30s002_285e with dissolve
    "Un par de minutos después..."
    play sound ("music/knock.ogg")
    "*Knock-Knock*"
    kat "*A través de la puerta* Soy yo."
    play music ("music/Morning-Sun.ogg")
    mc "*Risa* Me alegra escuchar que sabes quién eres."
    kat "*A través de la puerta* *Risa* ¡Idiota! ¿Puedo pasar?"
    mc "*Risa* Sí, claro, pasa."
    scene c30s002_245d with fade
    "El beso de cada mañana con [kat] se está convirtiendo en una costumbre bienvenida."
    "La chica gana confianza con cada uno de esos besos, confirmando que no se ha despertado soñando algo que no existe."
    call BlinkXS3("c30s002_245") from _call_BlinkXS3_886
    kat "Buenos días, [mc]. Estaba en la ducha cuando has bajado a desayunar y venía a por mi... segundo desayuno. *Risita*"
    mc "*Risa* Buenos días, [kat]. Pero no eres tan baja como para usar el segundo desayuno, ¿no?"
    call BlinkXS3("c30s002_250") from _call_BlinkXS3_887
    kat "*Risa* ¡Capullo! Tienes que decidirte sobre si soy una beluga o un halfling."
    mc "¿Por qué no ambos? Sí, ambos están bien. Dependiendo de la circunstancia."
    call BlinkXS3("c30s002_255") from _call_BlinkXS3_888
    kat "Es decir, te vas a reír de mi peso y de mi altura, ¿no?"
    kat "Creo que en esta familia es el único sitio donde alguien me consideraría un halfling."
    mc "No me voy a reír de tu peso ni de tu altura. Me voy a reír de ti en cuanto tenga ocasión. Da lo mismo la razón."
    mc "Pero, como me conozco y sé que se me puede ir de las manos, avísame si alguna vez quieres que pare de hacerlo."
    call BlinkXS3("c30s002_260") from _call_BlinkXS3_889
    kat "*Risa* Que yo no me haya reído de ti en los últimos días no significa que lo vaya a dejar de hacer."
    kat "Con lo que no voy a querer que pares nunca. En cuanto vuelva a tener la cabeza en su sitio, volveré a hacerlo."
    mc "*Risa* A mí me parece que está en su sitio. Sigue estando al final del cuello."
    scene c30s002_260d with dissolve
    "En un súbito arrebato, decides probar el sabor del cuello de [kat]. Hasta ahora tus labios solo han recorrido los suyos."
    "Pero están ansiosos por descubrir el resto de la piel de [kat]. Hay mucha piel por descubrir."
    "Y no. No es una broma sobre su peso."
    call BlinkXS3("c30s002_265") from _call_BlinkXS3_890
    "[kat] te deja besarle el cuello durante unos segundos, en los que notas cómo se eriza su piel, hasta que rompe bruscamente el contacto."
    kat "Para ya antes de que te tire encima de la cama."
    mc "*Risa* Esa amenaza es una buena razón para continuar."
    call BlinkXS3("c30s002_270") from _call_BlinkXS3_891
    kat "Cuando subía hacia aquí me he cruzado con [ama], que se llevaba los tests de embarazo."
    if mc._var("relationships")==1:
        kat "Por un momento me ha dado tristeza de no haber tenido la oportunidad de usarlos."
    else:
        kat "Por un momento me ha dado tristeza de ser la única de tus chicas que no ha tenido la oportunidad de usarlos."
        if ama._var("route"):
            kat "Aparte de [ama], claro."
    call BlinkXS3("c30s002_275") from _call_BlinkXS3_892
    kat "Pero eso no significa que tú y yo vayamos a tener sexo hoy."
    mc "No te preocupes. Mi intención no era tener sexo ahora. Supongo que necesitas algo de tiempo antes de eso."
    mc "Tan solo quería comprobar si podía ponerte la piel de gallina. *Risa* Objetivo conseguido."
    call BlinkXS3("c30s002_280") from _call_BlinkXS3_893
    kat "*Risa* Si sólo querías eso, puedes continuar. Me ha gustado mucho lo que has hecho."
    kat "Pero no esperes que me quite la ropa. Sólo tienes acceso de mi cuello hacia arriba."
    mc "*Risa* Puedo trabajar con eso."
    scene c30s002_260d with dissolve
    "Pasas los siguientes minutos descubriendo cómo tus besos afectan a cada centímetro cuadrado del cuello de [kat]."
    "Explorando dónde es más sensible y dónde lo es menos. Atesorando el conocimiento."
    "[kat] está extrañamente pasiva, disfrutando del contacto de tus labios."
    scene c30s002_285a with fade
    call BlinkXS3("c30s002_285") from _call_BlinkXS3_894
    "Al cabo de unos minutos que se te hacen demasiado cortos, [kat] vuelve a cortar el contacto, esta vez sin brusquedad."
    kat "*Respiración pesada* Ha sido fantástico, pero ahora me tengo que ir."
    mc "¿Tienes que estudiar? Es domingo..."
    scene c30s002_285d with dissolve
    kat "*Respiración pesada* No, pero tengo que... hacer algo en mi habitación. Hasta luego, [mc]."
    scene c30s002_285e with dissolve
    play sound ("music/DoorSlam.ogg")
    "La chica se va sin darte un beso de despedida."
    kat "*Hablando para sí misma* ¡Joder! Solo con unos besos en el cuello me ha puesto más cachonda de lo que he estado en toda mi puta vida."
    kat "*Hablando para sí misma* Voy a hacerme la que posiblemente sea la mejor paja de la historia. Espero que [kim] ya se haya ido."
    "No puedes evitar que se te escape una carcajada."
    kat "*Hablando para sí misma* ¡Joder! ¡Lo he dicho en voz alta!"
    stop music fadeout (1.5)
    scene black with dissolve
    return
label c30s002_getEriEilSca:
    scene c30s002_500d with dissolve
    play music ("music/ForWhenItRains.ogg")
    "Por fin consigues ponerte el bañador sin interrupciones y bajas a la piscina."
    "Te equivocabas y está totalmente vacía pese a que hace buen día y que es domingo."
    "Pasas un rato tumbado, esperando sin éxito que llegue alguna de las chicas."
    "Te aburres rápidamente y vuelves a tu habitación."
    scene black with dissolve
    "Por la tarde, te ofreces a ir a buscar a [eri], [eil], y [sca] al café."
    "La casa se está volviendo un poco opresiva. Cada vez estás más convencido de que te están evitando."
    "Te quedan pocos días para irte a Aruba y esperabas pasar tiempo con las chicas antes de hacerlo."
    "Al menos [sca], [eri], y [eil] no podrán evitarte en la camioneta."
    scene c30s002_500a with fade
    call BlinkXS3("c30s002_500") from _call_BlinkXS3_895
    stop music fadeout (1.5)
    "Tras recoger a las chicas..."
    play music ("music/Higher-Instrumental.ogg")
    sca "Y ahí acaba mi último día de turista en el Luca Café. Mañana empieza el trabajo."
    mc "¿Estás emocionada por empezar?"
    call BlinkXS3("c30s002_505a") from _call_BlinkXS3_896
    sca "Mucho. Al menos a partir de mañana ayudaré en vez de solo molestar con las preguntas."
    call BlinkXS3("c30s002_505b") from _call_BlinkXS3_897
    eri "No has molestado en ningún momento, [sca]. Si lo hubieras hecho..."
    mc "*Risa* [eri] no te lo diría, pero [eil] te hubiera mandado a callar."
    call BlinkXS3("c30s002_510") from _call_BlinkXS3_898
    eil "*Risa* A ver si [sai] tenía razón y es verdad que soy la bruja pelirroja."
    mc "*Risa* No lo decía por eso, pero eres una mujer que sabe priorizar las cosas y sabes que le puedes decir 'Hablamos después' a [sca]."
    call BlinkXS3("c30s002_515") from _call_BlinkXS3_899
    eri "*Risa* ¿Y yo no sé priorizar las cosas?"
    mc "No lo decía por eso, sino porque preferirías estar haciendo 10 cosas a la vez y respondiendo preguntas." id c30s002_getEriEilSca_678571e7
    mc "No querrías darle una mala contestación a [sca] que pudiera herirla."
    call BlinkXS3("c30s002_520") from _call_BlinkXS3_900
    sca "*Risa* Creo que te estás metiendo en un berenjenal."
    sca "Ahora podría preguntar yo si tan frágil me ves como para que me hiriese que me dijeran que esperara."
    mc "*Risa* ¿Vais a sacar de contexto todo lo que diga?"
    todas "*Risa* ¡Sí!"
    scene drive_afternoon
    "El viaje a casa continúa entre risas y comentarios."
    "Cada vez que dices algo, una de las tres tiene una respuesta ingeniosa que retuerce tus palabras y te hace parecer el malo."
    "Es como si el tiempo hubiera vuelto atrás y todo fuera como hace unos días."
    "Empiezas a pensar que te estabas volviendo paranoico con lo de que te estaban evitando."
    stop music fadeout (1.5)
    scene c30s002_520d with dissolve
    "Hasta que, al llegar a casa, las tres se despiden de ti y se van a casa de [nor], volviéndote a dejar solo."
    "En ese momento te preguntas por qué [eri] y [eil] han vuelto a casa con el uniforme en vez de cambiarse en el café."
    "Recuerdas que ahora comparten taquilla. ¿Lo han hecho para evitarte el tiempo de espera mientras se cambiaban?"
    return
label c30s002_AfterDinner:
    if _in_replay:
        $ mc._var("relationships", 0, "set")
        call mrS3_emm_route from _call_mrS3_emm_route_41
        call mrS3_deb_route from _call_mrS3_deb_route_27
        call mrS3_kat_route from _call_mrS3_kat_route_5
        call mrS3_kim_route from _call_mrS3_kim_route_13
        call mrS3_eri_route from _call_mrS3_eri_route_32
        if mc._var("relationships")==5:
            menu:
                "¿En cuántas relaciones estás?"
                "22":
                    $ mc._var("relationships", 22, "set")
                "Menos de 22":
                    pass
    scene c30s002_300d with dissolve
    "Después de cenar, subes a tu habitación. Ha sido un día raro."
    call BlinkXS3("c30s002_300") from _call_BlinkXS3_901
    play music ("music/SneakySnitch.ogg")
    "Al pasar por la segunda planta, ves a [emm] saliendo de su habitación."
    emm "¿Ya te vas a dormir, [mc]?"
    mc "No tengo sueño todavía, leeré o jugaré un rato antes de dormir."
    if emm._var("route"):
        mc "A menos que quieras subir a mi habitación... Parece que hoy todo el mundo me está evitando."
        emm "Me gustaría, pero no puedo. Voy a la habitación de [kat] y [kim] a ver una película. Me están esperando."
    else:
        mc "¿Qué vas a hacer tú? Parece que hoy todo el mundo me está evitando."
        emm "Voy a la habitación de [kat] y [kim] a ver una película. Me están esperando."
    call BlinkXS3("c30s002_305") from _call_BlinkXS3_902
    emm "[eri] y [deb.nick] ya deben estar allí."
    mc "Supongo que no me puedo unir, ¿verdad?"
    call BlinkXS3("c30s002_310") from _call_BlinkXS3_903
    emm "*Risa* ¿Quieres estar con cinco chicas viendo una comedia romántica?"
    mc "*Risa* Lo planteas como si fuera una tortura..."
    emm "*Risa* No quieres escuchar nuestros comentarios cuando el chico se quite la camisa."
    mc "Entonces te acompaño a la habitación de las chicas y me voy a la mía."
    if emm._var("route") and eri._var("route") and kim._var("route") and kat._var("route") and deb._var("route"):
        call BlinkXS3("c30s002_315") from _call_BlinkXS3_904
        emm "*Risa* Deberías verte la cara de decepción. Seguro que ya estabas pensando en tener sexo con las cinco a la vez."
        mc "*Risa* ¡Que salvaje eres! No estaría mal, pero creo que algunas de las chicas en esa habitación no están preparadas aún."
    call BlinkXS3("c30s002_325") from _call_BlinkXS3_905
    mc "¿Y el resto de la familia? ¿Sabes qué están haciendo?"
    emm "[dap], [sca], Tía [nor], [sai], y [kia] iban a ver un drama histórico en casa de Tía [nor]. Me ha sonado a algo aburrido."
    emm "[lis], [eva], y [ama] están en la piscina."
    emm "[meg] está en el Jazz Corner, [oma] ha llevado a [mad.nick] a casa, y no tengo ni idea del resto."
    emm "Creo que [eil] dormía con Mamá hoy."
    if eil._var("route") and mar._var("route"):
        call BlinkXS3("c30s002_320") from _call_BlinkXS3_906
        emm "*Risa* Y no creo que estés invitado tampoco."
    mc "Entonces definitivamente es el momento de subir a mi habitación."
    if emm._var("route"):
        call KissXS3 ("c30s002_330") from _call_KissXS3_19
    call BlinkXS3("c30s002_330") from _call_BlinkXS3_907
    mc "Te veo mañana, [emm]."
    emm "Hasta mañana, [mc]."
    scene c30s002_335a with fade
    call BlinkXS3("c30s002_335") from _call_BlinkXS3_908
    emm "Ya estoy aquí. Perdonad el retraso, me he topado con [mc] en la escalera."
    if emm._var("route"):
        emm "¡Joder! ¡Qué difícil es rechazarlo cuando te propone ir a su habitación!"
    emm "Por cierto, él se está empezando a dar cuenta de que le estamos evitando."
    scene c30s002_335d with dissolve
    eri "Os dije que no funcionaría. Es listo y ya no es tan naive como hace un mes."
    if kat._var("route"):
        kat "*Risa* Obviamente que es listo. Está saliendo conmigo después de estar evitándolo durante días."
    else:
        kat "*Risa* Obviamente que es listo. Me perdonó todas mis tonterías después de estar evitándolo durante días."
    deb "Quizás por eso se esté dando cuenta de que algo falla. Ya lo vivió contigo."
    if not emm._var("route") and not eri._var("route") and not kim._var("route") and not kat._var("route") and not deb._var("route"):
        kim "Entiendo por qué lo estamos evitando nosotras, pero no me gusta. No corremos ningún riesgo y me sabe mal por él."
    elif emm._var("route") and eri._var("route") and kim._var("route") and kat._var("route") and deb._var("route"):
        if mc._var("relationships")==22:
            kim "Creo que tenemos que convencer a [ama] de que pase más tiempo con él."
            kim "Ella no está en riesgo. No van a tener sexo, como mínimo, hasta Aruba."
        else:
            kim "Creo que tenemos que convencer a las que no tienen riesgo de que pasen más tiempo con él."
            if ama._var("route"):
                kim "Incluida [ama]. No van a tener sexo, como mínimo, hasta Aruba."
    else:
        if kim._var("route"):
            kim "Creo que las que no tenéis riesgo deberíais pasar más tiempo con él."
            if ama._var("route"):
                kim "Incluida [ama]. No van a tener sexo, como mínimo, hasta Aruba."
        else:
            kim "Creo que las que no tenemos riesgo deberíamos pasar más tiempo con él."
            if ama._var("route"):
                kim "Incluida [ama]. No van a tener sexo, como mínimo, hasta Aruba."
    call BlinkXS3("c30s002_340a") from _call_BlinkXS3_909
    emm "Bueno, lo que está claro es que hay que buscar una solución hasta el martes."
    emm "Sé que es necesario y que nuestras razones son buenas, pero... Me da un poco de pena por [mc]."
    call BlinkXS3("c30s002_340b") from _call_BlinkXS3_910
    emm "Pero creo que tenemos una película esperándonos. Ya lo hablaremos luego."
    emm "Podemos hacer apuestas sobre en qué minuto se quita la camisa Matthew McCon."
    emm "Y yo voy a empezar por quitarme los pantalones."
    stop music fadeout (1.5)
    return
label c30s002_LisSlap:
    if _in_replay:
        call mrS3_lis_anal from _call_mrS3_lis_anal
    scene c30s002_345a with fade
    "Mientras tanto, en la piscina..."
    play music ("music/thinking-of-you.ogg")
    ama "¿No te dolió nada?"
    lis "No... Es extraño, ¿no? Me dolían los pies, pero no me dolió cuando lo hicimos."
    if lis._var("anal"):
        lis "Ni por delante ni por detrás."
    eva "¿Estás segura de que no has usado un consolador tamaño poste de teléfono con anterioridad?"
    call BlinkXS3("c30s002_350") from _call_BlinkXS3_911
    lis "*Risa* Segurísima. Era tan virgen como una recién nacida."
    call BlinkXS3("c30s002_355") from _call_BlinkXS3_912
    eva "Y los pies... ¿Te dolían mientras bailabais?"
    eva "¿O sólo empezaron a dolerte cuando dejasteis de bailar?"
    call BlinkXS3("c30s002_360") from _call_BlinkXS3_913
    stop music fadeout (1.5)
    lis "Cuando dejamos de bailar. Hasta entonces es como si nada existiera..."
    scene c30s002_345An with dissolve
    pause (4.6)
    play sound ("music/Slap.ogg")
    scene c30s002_345An2 with dissolve
    "*Slap*"
    scene c30s002_345f with hpunch
    play music ("music/thinking-of-you.ogg")
    ama "¡[eva]! ¿Qué haces?"
    scene c30s002_345g with hpunch
    lis "¿Qué? ¿Por qué me has pegado una bofetada?"
    call BlinkXS3("c30s002_365") from _call_BlinkXS3_914
    eva "¿Te ha dolido?"
    call BlinkXS3("c30s002_370") from _call_BlinkXS3_915
    lis "¡Claro que me ha dolido!"
    lis "¡Me has pegado muy fuerte!"
    call BlinkXS3("c30s002_375") from _call_BlinkXS3_916
    eva "¿Te ha dolido o crees que te ha dolido?"
    call BlinkXS3("c30s002_380") from _call_BlinkXS3_917
    lis "¡Claro que me ha dolido! ¿Cómo voy a imaginar que me ha dolido? ¡Me has dado un bofetón!"
    call BlinkXS3("c30s002_385") from _call_BlinkXS3_918
    eva "Quítate la mano de la cara."
    call BlinkXS3("c30s002_390") from _call_BlinkXS3_919
    lis "¿Para qué? ¿Me vas a dar otro bofetón?"
    call BlinkXS3("c30s002_395") from _call_BlinkXS3_920
    ama "Haz caso a [eva], [lis]. Ahora entiendo lo que intenta hacer. Y no te va a volver a pegar."
    call BlinkXS3("c30s002_400") from _call_BlinkXS3_921
    lis "Estáis locas..."
    call BlinkXS3("c30s002_405") from _call_BlinkXS3_922
    ama "¿Aún te duele?"
    call BlinkXS3("c30s002_410") from _call_BlinkXS3_923
    lis "No, ya se ha pasado."
    call BlinkXS3("c30s002_415") from _call_BlinkXS3_924
    eva "Tienes que ir al médico, [lis]. Ni siquiera se te ha enrojecido la cara."
    call BlinkXS3("c30s002_420") from _call_BlinkXS3_925
    lis "¿Qué? ¿Por qué? Me has pegado fuerte, pero tampoco tan fuerte."
    call BlinkXS3("c30s002_425") from _call_BlinkXS3_926
    ama "Es posible que tengas una condición que se llama analgesia congénita."
    ama "No puedes sentir dolor, o no lo sientes como lo sentimos el resto de las personas. Puede ser... Es peligroso."
    call BlinkXS3("c30s002_440") from _call_BlinkXS3_927
    lis "Pero la bofetada me ha dolido."
    call BlinkXS3("c30s002_435") from _call_BlinkXS3_928
    eva "No te ha dolido. Crees que te ha dolido porque sabes que las bofetadas duelen. Pero no sabes durante cuánto tiempo duelen."
    eva "Por eso ya se te ha pasado el 'dolor', porque no había dolor real. A mí aún me duele la mano de la bofetada."
    eva "Si sintieras dolor, aún te dolería... durante bastante rato."
    call BlinkXS3("c30s002_430") from _call_BlinkXS3_929
    lis "¿Qué? ¿Eso es posible?"
    call BlinkXS3("c30s002_445") from _call_BlinkXS3_930
    ama "Sí. Por eso no te dolían los pies pese a que estuviste bailando durante mucho rato."
    ama "Cuando tu amiga te dijo el tiempo que llevabais bailando, tu cerebro te engañó y te dijo que te deberían doler, con lo que te convenció de que te dolían."
    ama "Como tu cerebro no sabe cómo o cuánto duele perder la virginidad, no supo cómo decirte que te tenía que doler."
    call BlinkXS3("c30s002_450") from _call_BlinkXS3_931
    lis "¿Me estáis diciendo que mi cerebro me ha estado mintiendo todo este tiempo? ¿Estoy loca?"
    call BlinkXS3("c30s002_455") from _call_BlinkXS3_932
    eva "No estás loca, [lis]. Tu cerebro no recibe señales de dolor a menos que sepa que le tiene que doler algo."
    eva "La serie B tenía el mismo problema. No es una buena situación para un soldado que no sabe cuándo está herido."
    eva "Por eso he reconocido los síntomas. Ellos nunca aprendieron cuándo tenían que sentir dolor. Tu cerebro te engaña para que 'lo sientas'."
    call BlinkXS3("c30s002_460") from _call_BlinkXS3_933
    lis "Pero esto tiene cura, ¿verdad?"
    call BlinkXS3("c30s002_465") from _call_BlinkXS3_934
    ama "No, [lis]. No tiene cura que yo sepa, si es lo mismo que tuvieron los B. Pero puedes vivir una vida normal, como has hecho hasta ahora."
    ama "Parece que tu cerebro ha aprendido a reconocer cuándo tiene que decirte que te duele algo."
    ama "Pero deberías ir al médico lo antes posible. A lo mejor estamos equivocadas..."
    scene c30s002_470a with hpunch
    eva "Lo siento mucho, [lis]."
    lis "[ama] ha dicho que puedo llevar una vida normal..."
    eva "Lo digo por la bofetada. Aún me duele la mano y, si me hubiera equivocado, me estarías odiando ahora mismo."
    ama "*Risa* A veces te pareces demasiado a [emm]."
    scene black with dissolve
    todas "*Risa*"
    "Las chicas se quedan en la piscina, charlando, riendo, y abrazándose durante un rato."
    "Cuando abandonan la piscina, la mano de [eva] ha dejado de doler, pero todavía le pica."
    eva "{i}(Menos mal que no me he equivocado. Creo que le he pegado demasiado fuerte){/i}"
    stop music fadeout (1.5)
    return
label c30s002_SolomonDream:
    scene black with dissolve
    "Duermes de forma agitada, sin saber por qué. Entre otras razones porque estás durmiendo."
    play music ("music/Dark-Score.ogg")
    scene c30s002_475a with dissolve
    "Te despiertas en medio de la noche, con la sensación de que algo va mal."
    "Supones que has tenido un sueño raro del que no recuerdas nada."
    scene c30s002_475b with fade
    "Decides bajar a beber agua a la cocina. Sigues sin acordarte de coger una botella cuando vas a dormir."
    "Cuando vas por la mitad del tramo de escaleras que lleva a la planta de las estudiantes, escuchas ruidos que vienen de abajo."
    "Como si alguien estuviera intentando moverse sin hacer ruido. Alguien pesado y torpe."
    "Te paras en medio de las escaleras y escuchas."
    scene c30s002_475c with fade
    kev "*Susurrando* ¿Cómo sabes que duerme en la última planta?"
    sol "*Susurrando* Mi hija no hacía más que hablar de él con su madre cuando salían juntos en el instituto."
    sol "*Susurrando* También cuando volvió de la universidad. No es que prestara atención, pero..."
    mcp "(No sabía que esos dos se conocían... ¿Dónde guarda [eva] las armas?)"
    scene c30s002_475d with dissolve
    kev "*Susurrando* Lo sé. Tu cerebro es capaz de registrar cosas de las que no te das cuenta."
    sol "*Susurrando* No me caía bien entonces, y ahora lo odio. Creo que has tenido una buena idea."
    scene c30s002_475e with dissolve #aparecen las pistolas
    kev "*Susurrando* Cuando me dijiste que la zorra rubia no era del FBI, supe que teníamos que hacer algo."
    sol "*Susurrando* *Risita* Al menos no lo podrán arrestar una vez acabemos con él esta noche. Y no me hagas pensar en la zorra rubia."
    stop music fadeout (1.5)
    sol "*Susurrando* Resbalé cuando estaba a punto de darle una paliza y se aprovechó de ello."
    scene c30s002_475f with hpunch #disparos
    play sound ("music/Desert-Eagle-Gunshot.ogg")
    pause 0.1
    play sound ("music/Desert-Eagle-Gunshot.ogg")
    "*Bang*" (multiple=2)
    "*Bang*" (multiple=2)
    scene c30s002_475g with fade
    "Bajas las escaleras corriendo al oír los disparos."
    play music ("music/Epic-Adventure-Action.ogg")
    "La imagen es estremecedora, con las dos mercenarias sobre los cuerpos inertes de sus víctimas."
    "Creías que un disparo a esa distancia produciría más sangre."
    "En el fondo de tu mente, sabes que es una solución definitiva a una situación que se iba seguir repitiendo."
    mc "¿Qué habéis hecho?"
    mcp "(Creo que hay una pala en el sótano, y conozco una parte del bosque que nunca visita nadie.)"
    scene c30s002_475h with dissolve
    "Bajas los últimos escalones. Es la primera vez que estas chicas matan por la familia y sabes que necesitan un abrazo."
    scene c30s002_475i with dissolve
    "Las dos mercenarias se arrancan los pasamontañas revelando una sorpresa inesperada."
    sca "Lo que era necesario." (multiple=2)
    kia "Acabar con dos problemas." (multiple=2)
    stop music fadeout (1.5)
    scene c30s002_475a with hpunch
    "Te despiertas con la respiración agitada."
    "Saber que era un sueño no lo hace menos inquietante."
    "Ver a las dulces [sca] y [kia] en el papel de frías asesinas ha sido lo más abrumador."
    "Tienes que hablar con [eva] por la mañana. No crees en los sueños premonitorios, pero quieres a Solomon y a Kevin vigilados mientras estés fuera."
    mcp "(Lo más ridículo del sueño es pensar que se conocen y que se van a poner de acuerdo para hacer algo contra mí o mi familia.)"
    scene black with dissolve
    "Te cuesta dormirte, das vueltas en la cama durante un rato largo."
    "Por un momento te sientes tentado de bajar a la planta de las estudiantes para comprobar si hay sangre en el suelo."
    "Ese sueño ha sido demasiado real."
    centered "{size=+20}{b}DÍA 35 – LUNES{/b}{/size}"
    return
label c30s003_KatWakeUp:
    scene c30s003_005d with dissolve
    play music ("music/Embrace.ogg")
    "Te vuelves a despertar sobresaltado. Esta vez estás seguro de que no es un sueño."
    kat "Buenos días, dormilón."
    call BlinkXS4("c30s003_005") from _call_BlinkXS4_853
    mc "¡Oh! Buenos días, [kat]. ¿Has estado mirando cómo dormía? ¿Cuánto rato llevas aquí?"
    kat "Solo unos minutos. He venido a buscar mi beso antes de irme a clase. Estás muy mono mientras duermes. Pero no quería despertarte."
    mc "*Risa* Esto empieza a hacer que parezcas una acosadora."
    call BlinkXS4("c30s003_010") from _call_BlinkXS4_854
    kat "¿Me estoy poniendo muy pesada viniendo a buscar mis besos?"
    kat "Si te molesta dejaré de hacerlo... Al menos lo de venir cuando estés durmiendo..."
    kat "Tienes razón. Empiezo a parecer una psicópata..."
    mc "Creo que tengo una respuesta para eso..."
    scene c30s003_015a with dissolve
    "Te incorporas y le das el beso de buenos días que la rubia merece."
    "Te ilusiona que esté tan ilusionada como para venir a espiarte mientras duermes."
    scene c30s003_015b with fade
    "La tumbas boca arriba en la cama sin interrumpir el beso. Es una besadora excelente."
    "Sabes que tarde o temprano se quedará a dormir contigo, cuando esté preparada."
    "Te preguntas si [kat] dormirá o se quedará mirando como lo haces tú."
    call BlinkXS4("c30s003_020") from _call_BlinkXS4_855
    kat "No sigas... He dicho que tengo que ir a la universidad."
    mc "Entonces no hay besos en el cuello hoy, ¿no?"
    scene c30s003_025d with dissolve
    pause (1.0)
    call BlinkXS4("c30s003_025") from _call_BlinkXS4_856
    kat "Pones muy difícil resistirse. Aún puedo quedarme unos minutos."
    mc "Es una lástima que sólo sean unos minutos..."
    scene c30s003_015c with dissolve
    "Tienes que aprovechar los minutos que tienes disponibles para degustar el cuello de la preciosa chica."
    "Te empleas con ansia, ya que no sabes cuántos minutos va a durar la sesión de besos en el cuello."
    "Y viendo el resultado que tuvieron ayer, te resulta gracioso excitarla justo antes de ir a clase."
    "Por desgracia, los minutos corren rápido y no son demasiados."
    call BlinkXS4("c30s003_030") from _call_BlinkXS4_857
    kat "Se acabó. Has conseguido que me tenga que ir a clase con las bragas chorreando."
    mc "¿No te da tiempo a cambiártelas?"
    call BlinkXS4("c30s003_035") from _call_BlinkXS4_858
    kat "*Risa* He alargado los besos todo lo posible. No puedo gastar ni un minuto en ello."
    kat "Meteré unas bragas limpias en el bolso y me cambiaré allí."
    scene c30s003_035d with dissolve
    "Te besa apasionadamente una última vez."
    call BlinkXS4("c30s003_040") from _call_BlinkXS4_859
    kat "Me voy o perderé el autobús."
    mc "Si quieres te puedo llevar yo..."
    call BlinkXS4("c30s003_045") from _call_BlinkXS4_860
    kat "Tendríamos que salir ahora mismo igualmente. Entre que sacas el coche del garaje y..."
    call BlinkXS4("c30s003_050") from _call_BlinkXS4_861
    kat "¡Que me tengo que ir! *Risa* No me tientes con un minuto más de besos en el cuello."
    mc "*Risa* Pues te veo luego. Que lo pases bien en la universidad."
    scene c30s003_050d with fade
    kat "Odio llevar las bragas mojadas. *Risa* ¡Te odio!"
    mc "*Risa* ¡Yo no he hecho nada!"
    scene c30s003_050e with hpunch
    play sound ("music/DoorSlam.ogg")
    "*Blam*"
    kat "*A través de la puerta* Estás desnudo. Desde el primer beso..."
    "Y te quedas solo una vez más en tu habitación."
    "Pillarte desnudo es uno de los riesgos de venir a verte mientras duermes."
    stop music fadeout (1.5)
    scene black with dissolve
    "Te quedas dormido sin darte cuenta."
    return
label c30s003_MarShopping:
    if _in_replay:
        call mrS3_mar_route from _call_mrS3_mar_route_42
        call mrS3_dap_route from _call_mrS3_dap_route_33
        call mrS3_sca_route from _call_mrS3_sca_route_27
    scene c30s003_050e with dissolve
    "Te despiertas tarde y decides saltarte el desayuno."
    scene black with dissolve
    "Continúas preparando cosas para el viaje hasta la hora de comer."
    "La cocina de [nor] está extrañamente vacía."
    "Las estudiantes están en la universidad. [eri], [eil], y [sca] están trabajando, mientras [dap] está en el café para dar apoyo moral a [sca]."
    "De las chicas que no viven en casa, sólo [ama] aparece. Ella también se va en unos días y la conversación gira a su alrededor."
    scene c30s002_150e with dissolve
    "Poco después de la comida..."
    play sound ("music/knock.ogg")
    "*Knock-Knock*"
    play music ("music/i-feel-alive.ogg")
    if persistent.family:
        mc "Pasa, Mamá."
    else:
        mc "Pasa, [mar]."
    if mar._var("route"):
        call KissXS4("c30s003_150") from _call_KissXS4_24
    call BlinkXS4("c30s003_150") from _call_BlinkXS4_862
    mom "¿Cómo sabías que era yo?"
    mc "Mi puerta ha sonado tantas veces en las últimas semanas, que empiezo a reconocer cómo cada una de vosotras usáis los nudillos."
    mc "¿Puedo ayudarte en algo?"
    call BlinkXS4("c30s003_155") from _call_BlinkXS4_863
    mom "Tengo que ir a comprar al supermercado, y me preguntaba si podrías venir con la camioneta y traer la compra."
    mc "*Risa* ¿Vas a comprar comida para un regimiento?"
    call BlinkXS4("c30s003_160") from _call_BlinkXS4_864
    if sca._var("route") or dap._var("route"):
        mom "*Risa* No, qué va. Pero voy a comprar algunos congelados y no vendré a casa directamente. Tengo que pasar por el café a recoger a [dap] y [sca]."
    else:
        mom "*Risa* No, qué va. Pero voy a comprar algunos congelados y no vendré a casa directamente. Tengo que pasar por el café a recoger a [eil], [dap] y [sca]."
    mc "Si quieres puedo ir a buscarlas yo. Quiero ver cómo le ha ido a [sca] su primer día de trabajo."
    call BlinkXS4("c30s003_165") from _call_BlinkXS4_865
    mom "Bueno, tengo que llevar a [dap] y [sca] de compras. Se lo prometí hace unos días. ¿Por qué no recoges a [eil] y traes la compra a casa?"
    mc "Me parece una buena idea. Así le puedo preguntar a [sca] antes de que os vayáis de compras."
    mc "Nos podemos ir cuando quieras."
    scene c30s003_170d with fade
    "Finalmente, no compráis nada congelado y [mar] y tú podéis ir a recoger a las chicas."
    "Los dos estáis ansiosos por ver cómo le ha ido a [sca] el primer día de trabajo."
    "Llegáis unos minutos antes de que [eil] y [sca] acaben su turno."
    "Encuentras el café más oscuro de lo normal, pero no parece haber ninguna luz fundida."
    call BlinkXS4("c30s003_175") from _call_BlinkXS4_866
    "Para no molestar a [sca], decidís ir a hacerle compañía a [dap]."
    mc "Hola, [dap]. ¿Qué tal le va a [sca]?"
    dap "Mejor de lo que todos esperábamos. No ha roto nada. *Risa*"
    call BlinkXS4("c30s003_180") from _call_BlinkXS4_867
    mom "Voy a pedir un café. Quiero probar el café que hace [sca] para poder compararlo con los que hacen [eil] y [eri]."
    mom "¿Quieres algo, [mc]?"
    mc "*Risa* Sabía que no podrías resistirte. Pide un espresso para mí, por favor."
    scene c30s003_185a with fade
    call BlinkXS4("c30s003_185") from _call_BlinkXS4_868
    mc "*Risa* Veo que tú has optado por lo seguro y has pedido un agua."
    dap "*Risa* Esto sólo ha sido después de los primeros cuatro cafés."
    dap "Tengo intención de poder dormir esta noche, o esta semana... No estoy acostumbrada a tomar tanto café."
    mc "Así que todo bien con el trabajo, ¿no?"
    call BlinkXS4("c30s003_190") from _call_BlinkXS4_869
    dap "Sí, parece muy ilusionada. Todos estos días que ha pasado aquí le han dado mucha seguridad."
    dap "¿Te acuerdas de lo tímida que era cuando llegaste de Portland?"
    mc "Creo que esa versión de [sca] ha quedado atrás. Mudarse a casa le ha hecho mucho bien."
    call BlinkXS4("c30s003_195") from _call_BlinkXS4_870
    if sca._var("route"):
        dap "Estar rodeada de chicas a las que no conocía bien ha sido bueno para ella. Y salir contigo también."
    else:
        dap "Estar rodeada de chicas a las que no conocía bien ha sido bueno para ella. Le ha obligado a abrirse."
    mc "¿Y sobre el cansancio? [eil] me dijo que los primeros días pueden ser agotadores."
    scene c30s003_200d with dissolve
    dap "Se lo puedes preguntar tú mismo. Viene por ahí con los cafés."
    mc "Justo a tiempo."
    call addProfileImageS3 (4, "sca_4", sca, __(": 15 - Especial"), "") from _call_addProfileImageS3_25
    call BlinkXS4("c30s003_200") from _call_BlinkXS4_871
    sca "Aquí está su café, Señor."
    if mar._var("route"):
        sca "Y el café de su esposa. *Risita*"
    else:
        sca "Y el café de la señora."
    mc "Gracias. ¡Qué formal!"
    call BlinkXS4("c30s003_205") from _call_BlinkXS4_872
    sca "[eil] me ha dicho que trate a todo el mundo con el máximo respeto, aunque los conozca."
    sca "A algunas personas no les gusta que los camareros los traten con familiaridad."
    mc "Bueno, a mí me puedes tratar como siempre."
    if sca._var("route"):
        mc "Aunque supongo que no me vas a dar un beso hoy. Al menos hasta que acabes el turno."
    call BlinkXS4("c30s003_210") from _call_BlinkXS4_873
    dap "*Risa* A mí casi no me ha dejado abrazarla cuando me ha traído el primer café."
    dap "Pero sabes que puedo ser muy insistente con los abrazos."
    mc "*Risa* Eso va en la familia."
    call BlinkXS4("c30s003_215") from _call_BlinkXS4_874
    mc "[dap] me ha dicho que el día va bien. ¿Estás muy cansada?"
    sca "Más de lo que creía, pero también muy contenta. Nadie se ha quejado de mis cafés."
    sca "Y no creo que tengan muchas oportunidades para quejarse. Sólo me quedan unos minutos para acabar mi turno."
    mc "Entonces no te entretenemos más. *Risa* Luego te diré si tengo alguna queja sobre el café."
    scene c30s003_220d with fade
    "Al cabo de unos segundos, [mar] vuelve de la barra, dónde se ha quedado hablando con [eil]."
    "Os miráis reluctantemente antes de probar el café que ha hecho [sca]."
    call BlinkXS4("c30s003_220") from _call_BlinkXS4_875
    mom "Está... sorprendentemente bueno. Me gusta más cómo lo hace [eri], pero no está nada mal para el primer día."
    mc "A mí me gusta más cómo hace los cafés [eil], pero está mejor de lo que esperaba."
    call BlinkXS4("c30s003_225") from _call_BlinkXS4_876
    dap "¡Vuestra carencia de fe resulta molesta! *Risa* Siempre he querido decir esa frase." #I find your lack of faith disturbing
    mc "*Risa* Mientras no me digas que tú eres mi padre..."
    mc "¿Por cierto, qué es lo que vais a ir a comprar?"
    call BlinkXS4("c30s003_230") from _call_BlinkXS4_877
    dap "Algo de ropa y algunas cosas más. Ya sabes, empezamos la universidad en unas semanas..."
    mc "¿Qué tiene de malo vuestra ropa? A mí me gusta."
    call BlinkXS4("c30s003_235") from _call_BlinkXS4_878
    mom "Una chica debe tener ropa para todas las ocasiones, [mc]. Deberías saberlo a estas alturas."
    mc "*Risa* Sí, para todas las ocasiones posibles y las imposibles también."
    mc "No olvidéis comprar la escafandra de buzo ni el traje de astronauta."
    scene c30s003_240a with dissolve
    eil "¿Otra vez se está quejando de que compramos mucha ropa?"
    mc "No me estoy quejando. Sólo preguntaba. ¿Ya has acabado tu turno?"
    call BlinkXS4("c30s003_245") from _call_BlinkXS4_879
    eil "Si. [sca] se está cambiando y nos podremos ir cuando queráis."
    mc "¿No te quitas el uniforme?"
    eil "Mi taquilla está a reventar con las cosas de [eri] y [sca], con lo que voy y vuelvo de casa con el uniforme."
    mc "Creía que lo de compartir tu taquilla era precisamente para no tener que hacer eso..."
    call BlinkXS4("c30s003_250") from _call_BlinkXS4_880
    mom "Estás muy quisquilloso con la ropa hoy. Si [eil] quiere volver a casa con el uniforme, está en su derecho de hacerlo."
    mc "Yo no estaba diciendo..."
    call BlinkXS4("c30s003_255") from _call_BlinkXS4_881
    dap "Por ahí viene [sca]. Ella sí que se ha cambiado. Estarás contento, [mc]."
    mc "Que no me importa, sólo es que me parece raro..."
    call BlinkXS4("c30s003_260") from _call_BlinkXS4_882
    sca "¿Nos vamos? Tengo ganas de ver esa... tienda... de la que nos has hablado."
    mc "No haré ningún comentario sobre que creía que comprabais la ropa en la tienda de [mad.nick]."
    mc "Seguro que os ponéis a la defensiva."
    scene drive_afternoon with fade
    "Tras las despedidas, [eil] y tú volvéis a casa mientras el resto de las mujeres se van de compras."
    "[eil] está contenta por cómo ha ido el primer día de trabajo de [sca]. La chica presta atención a los detalles."
    stop music fadeout (1.5)
    scene black with dissolve
    "Al volver a casa te ayuda a subir la compra a la cocina, pero te deja solo para que la guardes en la despensa."
    "No sabe dónde [mar] guarda cada cosa y sería más un estorbo que una ayuda."
    return
label c30s005_EmmLewd:
    if _in_replay:
        call mrS3_emm_pregnant from _call_mrS3_emm_pregnant_2
    scene c30s005_005a with fade
    "Cuando acabas de recoger la compra decides bajar a la piscina. El sol está bajo y seguramente puedas aguantar un rato sin sentirte un filete a la brasa."
    play sound ("music/notification.ogg")
    "Nada más acabar de cambiarte, recibes un WhatsUp de [emm]."
    emm "*Mensaje* ¿Puedes bajar un momento a la sala de la colada?"
    mc "*Mensaje* Ahora bajo. Acabo de llegar de recoger a [eil] y de recoger la compra."
    scene c30s005_005b with fade
    play music ("music/NightJazzBeats.ogg")
    "Al entrar en la sala de la colada..."
    mc "*Risa* ¿Qué haces ahí dentro?"
    emm "*Risa* Hermanastro, me he quedado atascada dentro de la lavadora..."
    mc "*Risa* ¿Qué es eso de 'hermanastro'?"
    emm "¿Tú no ves porno? ¡Es uno de los clásicos!"
    emm "La hermanastra idiota se queda atascada en la lavadora y el hermanastro cachondo se la folla."
    mc "*Risa* ¿Sigues queriendo tener sexo como en las pelis porno?"
    emm "*Risa* Si no quisiera, ¿qué estoy haciendo dentro de una lavadora mandándote mensajes llevando sólo unas bragas sexys y un top?"
    scene c30s005_005c with dissolve
    mc "*Risa* Ciertamente unas bragas muy sexys que te hacen un culo muy bonito."
    mc "Pero yo creía que la siguiente vez que quisieras follar a lo peli porno te volverías a poner el uniforme de criada francesa."
    scene c30s005_005d with vpunch
    play sound ("music/MurderByShovel.ogg")
    "*Dong*"
    emm "¡Ouch!"
    mc "¿Te has hecho daño? *Risa* Ha sonado a hueco y no sé si era la lavadora o tu cabeza..."
    emm "*Gruñido* Muy gracioso. No, no me he hecho daño, pero es que no me he acordado del uniforme de criada francesa."
    emm "Aunque hoy no es un buen día para ponérmelo. Un día te sorprenderé."
    mc "Pero no entiendo cómo te has quedado atascada dentro de la lavadora..."
    call BlinkXS4 ("c30s005_010") from _call_BlinkXS4_883
    emm "*Risa* No estoy atascada. ¿Para qué voy a meter medio cuerpo dentro de una lavadora vacía llevando el móvil?"
    emm "Voy a volver dentro..."
    mc "*Risa* Lo de que algún día me sorprenderás... ¿aún más que hoy?"
    scene c30s005_005b with dissolve
    emm "*Risa* Sí, aún más que hoy. Pero puedes empezar cuando quieras. Se me están quedando las rodillas congeladas."
    emm "Sabía que este plan tenía que tener algún fallo..."
    mc "*Risa* ¿Qué plan tuyo no lo tiene? ¿Quieres unas toallas para las rodillas?"
    emm "Lo que quiero es que me quites las bragas de una vez."
    scene c30s005_005e with fade
    mc "Hecho. Sigo pensando que es un culo precioso."
    emm "Gracias, pero supongo que aún estás vestido... No te veo desde aquí dentro."
    mc "Sólo llevo el bañador."
    emm "Eso es bueno. Así tardarás menos en desnudarte."
    mc "¿Lo dices en serio? ¿No prefieres que subamos a mi habitación? La cama es más cómoda que una lavadora."
    emm "Calla y fóllame... Hermanastro... *Risita*"
    scene c30s005_950pv with fade
    show c30s005_950v
    "Te quitas el bañador y perforas el coño de [emm] sin piedad. Si quiere follar como en una peli porno, no vas a negarle ese deseo en esta ocasión."
    $renpy.sound.play("music/EmmaMoan.ogg", loop=True, relative_volume=5.0)
    emm "*Gemido* ¡Oh, hermanastro! *Jadeo* ¿Qué estás haciendo? *Gemido*"
    "Su último intento de recrear una peli porno fue cuando se presentó en tu habitación con el uniforme de criada."
    "Por aquel entonces no estaba preparada, pero las cosas han cambiado mucho en las últimas semanas."
    emm "*Jadeo* La casera puede venir en cualquier momento. *Gemido* No deberíamos estar haciendo esto. *Jadeo*"
    "Se está metiendo en el papel, pero puedes notar cómo lo está disfrutando. Decides seguirle la corriente."
    scene c30s005_955pv with fade
    show c30s005_955v
    hide c30s005_950v
    mc "No te preocupes por la casera. Follas mejor que ella."
    "Su coño se tensa de placer al escuchar esa frase y ver que estás entrando en su juego."
    emm "*Gemido* Lo sé. *Jadeo* Me lo ha dicho... el casero... *Gemido risueño* Que eres tú..."
    "El sexo con [emm] puede ser muy divertido. Pese a sus alocados planes, tiene una frescura increíble."
    emm "*Jadeo risueño* Mi voz hace eco aquí dentro. *Gemido* Y los gemidos también. *Jadeo*"
    "La chica se lo está pasando muy bien, cumpliendo su objetivo de follar como en una peli porno."
    scene c30s005_960pv with fade
    show c30s005_960v
    hide c30s005_955v
    "Su coño se cierra con fuerza sobre tu astil, como muestra de lo mucho que está disfrutando."
    emm "*Gemido* ¡Oh, hermanastro! *Jadeo* Me estás follando tan bien que me voy a correr en seguida. *Gemido*"
    "Todo está pasando muy rápido. La fuerte presión de sus paredes vaginales hace que tú también estés a punto de llegar al orgasmo."
    mc "Yo no voy a poder aguantar mucho más."
    "[emm] tensa aún más sus músculos para reducir tu resistencia."
    emm "*Jadeo* Corrámonos juntos. *Gemido* Quiero notar tu leche dentro de mí. *Jadeo*"
    "No puedes hacer mucho por evitarlo."
    if persistent.pregnancy and not emm._var("pregnant"):
        if persistent.walkthrough:
            $ wt1 = _("[emm] embarazada.")
            $ wt2 = _("Sin consecuencias.")
        else:
            $ wt1 = ""
            $ wt2 = ""
        menu:
            "Correrte dentro. Ir a por el bebé." (wt = wt1):
                $ emm._var("pregnant", True)
                $ emm._var("undiscoveredPregnancy", True)
                play sound ("music/OldMusicBox5.ogg")
            "Correrte dentro." (wt = wt2):
                pass
    call OrgasmXS4 ("c30s005_015") from _call_OrgasmXS4_47
    hide c30s005_960v
    emm "*GEMIDO* ¡OH, SÍ! *JADEO* ¡CÓRRETE DENTRO DE MÍ, HERMANASTRO! *GEMIDO*"
    "Incluso mientras se corre se mantiene dentro del papel."
    "Y su orgasmo lleva al tuyo irremediablemente."
    mc "¡Mpfft!"
    stop music fadeout (1.5)
    "Para haber sido un polvo tan rápido sin preliminares, tu descarga de semen es enorme."
    stop sound fadeout (1.0)
    scene c30s005_020d with fade
    play music ("music/On-The-Rise.ogg")
    "Al cabo de unos segundos, te separas de [emm] para observar tu obra."
    mc "¿Te ha gustado?"
    emm "Me ha encantado. Pero prefiero cuando lo hacemos... como siempre."
    emm "Echo de menos los preliminares y los abrazos."
    mc "Siempre podemos tener los abrazos de después del polvo."
    scene c30s005_020e with fade
    if persistent.family:
        "Tu hermana sale de dentro de la lavadora y te recuestas sobre ella. El suelo está frío."
    else:
        "La chica sale de dentro de la lavadora y te recuestas sobre ella. El suelo está frío."
    mc "¿Quiere decir eso que se ha acabado lo de follar como en una peli porno?"
    call BlinkXS4("c30s005_020") from _call_BlinkXS4_884
    emm "¡Ni en broma! Me ha gustado mucho, y de vez en cuando me seguirá apeteciendo."
    mc "Me parece una buena idea. Siempre y cuando podamos tener nuestra ración de abrazos."
    call BlinkXS4 ("c30s005_025") from _call_BlinkXS4_885
    emm "Para hacer la peli porno completa, te hubieras corrido en mi espalda. Pero eso lo hacen para los espectadores, y no tenemos."
    mc "Sabes que esto es una zona común, ¿verdad?"
    call BlinkXS4 ("c30s005_030") from _call_BlinkXS4_886
    emm "Pero aquí no debería haber cámaras, ¿no?"
    mc "Le deberías preguntar a [ama] o [eva]. Creo que tienen cámaras en los sitios más insospechados."
    mc "Es su forma de ver a la familia mientras hacemos tareas cotidianas y sentirse parte de ello."
    call BlinkXS4 ("c30s005_035") from _call_BlinkXS4_887
    emm "Pues le diré a [eva] que quite las cámaras de aquí."
    emm "Creo que esto lo vamos a repetir y no quiero que, cuando haya clones masculinos mirando las cámaras, nos vean así."
    mc "¿No te importa que [ama] y [eva] te vean, pero te importa con los clones masculinos?"
    call BlinkXS4 ("c30s005_040") from _call_BlinkXS4_888
    emm "Es diferente. Ellas son mis hermanas de elección. A los clones masculinos no los conozco."
    emm "A mí realmente no me importa que alguna de las chicas de la familia nos mire si quiere."
    mc "Entiendo. No sabía que tuvieras esa vena exhibicionista."
    call BlinkXS4 ("c30s005_045") from _call_BlinkXS4_889
    emm "*Risa* [ama], [eva], si habéis mirado, espero que lo hayáis disfrutado."
    call BlinkXS4 ("c30s005_050") from _call_BlinkXS4_890
    emm "No creo que sea una vena exhibicionista... No me pone que me miren las chicas, pero tampoco es algo que me importe."
    emm "Creo que el sexo es tan natural como comer. Y no me importa que me vean comiendo."
    mc "*Risa* ¿Te importa que te vean comiendo los clones masculinos?"
    call BlinkXS4 ("c30s005_055a") from _call_BlinkXS4_891
    emm "*Risa* Vale, es más privado que comer."
    call BlinkXS4 ("c30s005_055b") from _call_BlinkXS4_892
    emm "Aunque no me gustaría que alguien a quien no conozco me vea con un trozo de lechuga en los dientes."
    emm "Sin embargo, no me importaría que me vieran [kim], [ama], [eri], o [eil] con la lechuga. No sé si me explico..."
    mc "¿Quieres una tarea importante?"
    call BlinkXS4 ("c30s005_060") from _call_BlinkXS4_893
    emm "¿Qué? ¿Vas a confiar en mí para algo importante? ¡Por supuesto que quiero esa tarea!"
    mc "Te confiaría mi vida, [emm]. Mi ropa no, ¿pero mi vida? Seguro."
    call BlinkXS4 ("c30s005_065") from _call_BlinkXS4_894
    emm "*Risa* Eso es porque tienes un gusto pésimo para elegir ropa. Especialmente el color."
    emm "Pero dime esa tarea importante. Me tienes en ascuas."
    mc "He estado pensando en los clones masculinos y en las cámaras después de la conversación con [ama] en tu habitación."
    mc "Quiero que te coordines con [eva] para ampliar el perímetro de las cámaras."
    call BlinkXS4 ("c30s005_070") from _call_BlinkXS4_895
    emm "¿En plan si vigilan fuera no hace falta que vigilen dentro?"
    mc "Mas o menos... Sabes dónde es necesario que vigilen dentro y..."
    call BlinkXS4 ("c30s005_075") from _call_BlinkXS4_896
    emm "*Risa* En la sala de la lavadora no... Aunque si [eva] las puso aquí, no quiero que se pierda a Mamá poniendo la lavadora, por aburrido que sea."
    mc "Creo que eso es más cosa de [ama]..."
    emm "Pero se me acaba de ocurrir una idea."
    mc "*Risa* Me das miedo."
    call BlinkXS4 ("c30s005_080") from _call_BlinkXS4_897
    emm "Una aplicación en los móviles que nos permita desactivar cámaras individuales si no queremos que alguien nos vea."
    emm "Y no solo cuando vayamos a hacer algo como esto..."
    mc "Eso puede ser peligroso, si nadie se acuerda de volverlas a activar."
    call BlinkXS4 ("c30s005_085") from _call_BlinkXS4_898
    emm "Sólo sería para las cámaras interiores. O las de la piscina y el jacuzzi, si a alguna de las chicas les molesta que las vean en topless o desnudas."
    emm "Incluso se podría poner un temporizador para que se reactiven si no se confirma la orden de mantenerlas desactivadas..."
    mc "Parece una idea interesante, pero deberías coordinarlo con [eva]."
    mc "No sé si va a querer que cualquiera pueda desactivar las cámaras."
    scene c30s005_085d with vpunch
    "[emm] se levanta de un salto. Tu cabeza, hasta ese momento apoyada cómodamente en su pierna, impacta contra el suelo."
    emm "¡Voy a decírselo!"
    mc "[emm]... te olvidas de las bragas... y de ponerte algo..."
    call BlinkXS4 ("c30s005_090") from _call_BlinkXS4_899
    emm "*Risa* Las bragas las puedes poner para lavar. Estaban empapadas cuando has llegado."
    stop music fadeout (1.5)
    emm "¡Hasta luego!"
    scene c30s005_090d with hpunch
    play sound ("music/DoorSlam.ogg")
    "*Blam*"
    mcp "(Y se ha vuelto a ir sin darme un beso.)"
    return
label c30s005_noEmmLewd:
    scene c30s005_1000a with fade
    "Cuando acabas de recoger la compra, decides bajar a la piscina. El sol está bajo y seguramente puedas aguantar un rato sin sentirte un filete a la brasa."
    "Antes de bajar a la piscina, compruebas si hay alguna actualización de My Residence."
    "Parece que va a haber una escena con Irma, la hermana del MC en la sala de lavandería."
    "Conociendo lo sorprendente que puede llegar a ser, seguro que es una escena divertida."
    scene black with dissolve
    "De camino a la piscina, te encuentras con [emm] y te comenta unas ideas que ha tenido para las cámaras."
    "No cree que algunas de las chicas estén cómodas en topless cuando las cámaras las vigilen los clones masculinos."
    "Le propones que lo comente con [eva]. [emm] a veces tiene buenas ideas. Pero la ejecución no suele ser tan buena."
    return
label c30s004_Eva:
    if _in_replay:
        call mrS3_emm_route from _call_mrS3_emm_route_42
        call mrS3_eva_route from _call_mrS3_eva_route_18
        call mrS3_mar_route from _call_mrS3_mar_route_43
        if mar._var("route"):
            call mrS3_mar_pregnant from _call_mrS3_mar_pregnant_5
        call mrS3_edmund_story from _call_mrS3_edmund_story_11
    scene c30s004_115a with fade
    "Al llegar a la planta baja..."
    play music ("music/Memories-Instrumental.ogg")
    mc "Hola, chicas. ¿Venís de correr?"
    deb "No, hace un rato que hemos vuelto. Ahora venimos de la piscina."
    mc "¿Hay alguien allí?"
    lis "[eva] estaba allí hace un momento, pero se ha ido y no sé si volverá."
    deb "El sol ya está demasiado bajo para mi gusto."
    mc "Para mí es el momento ideal para relajarme un rato sin tener que tostarme al sol."
    scene c30s004_115b with dissolve
    deb "Entonces no te entretenemos más, o vas a acabar bañándote de noche."
    lis "Un día tenemos que hacer algo de noche en la piscina. Un día que haga buena noche."
    mc "Cuando queráis. Aunque, si queréis contar conmigo, deberá ser pronto."
    scene c30s004_115c with dissolve
    lis "Ya lo hablaremos. Y no hay prisa."
    mc "[ama] y yo nos vamos el jueves."
    deb "Y nosotras seguiremos aquí cuando volváis."
    scene c30s004_005a with fade
    "Te despides de las dos chicas y, al llegar a la piscina, está más oscuro de lo que creías y está obviamente vacía."
    "El tema con [emm] te ha retrasado más de lo que creías. Parece que tus últimos días en casa los vas a pasar bastante solo."
    if emm._var("route"):
        "Si no fuera por ratos como el de [emm]..."
        "Anoche parecía que te evitaba y sin embargo hoy ha sido ella la que te ha buscado para una visita a la sala de la colada."
    else:
        "Y después hay cosas como lo de [emm]. Anoche parecía claro que te quería evitar y hoy ha estado hablando contigo de las cámaras como si no pasara nada."
    "No entiendes nada..."
    scene c30s004_005b with fade
    "Al cabo de un rato empieza a nublarse. Habían anunciado lluvias para toda la noche."
    "Parece que tu sesión en la piscina ha terminado. No ha durado ni siquiera 10 minutos."
    "No crees que ninguna de las chicas vaya a bajar a la piscina lloviendo. Decides recoger los colchones de las tumbonas."
    scene c30s004_005c with fade
    "Cuando acabas de recogerlos, escuchas sollozos detrás de casa."
    "No has visto llegar a nadie en los 15 minutos que has estado solo en la piscina."
    "*Sollozo*"
    stop music fadeout (1.5)
    "No reconoces a quién pertenecen. Te acercas por si alguien te necesita."
    scene c30s004_005d with fade
    play music ("music/Sad-Piano.ogg")
    "Al girar la esquina ves a [eva] en un rincón, sentada en el césped y sollozando."
    "Pocas veces la has visto con un aspecto tan frágil."
    mc "¿Quieres compañía?"
    call BlinkXS4("c30s004_010") from _call_BlinkXS4_900
    eva "*Voz llorosa* No te he oído llegar."
    eva "Supongo que, aunque te dijera que no quiero compañía no me dejarías sola, ¿no?"
    mc "Te dejaría sola, pero me quedaría cerca por si cambias de opinión."
    mc "Estás en mi rincón de las rabietas. Cuando era un niño venía aquí cuando quería estar solo."
    call BlinkXS4("c30s004_015") from _call_BlinkXS4_901
    eva "Es un buen rincón. Nadie pasa por aquí nunca."
    mc "Lo sé. Por eso venía cuando algo me enfadaba, o, especialmente, cuando me ponía triste."
    call BlinkXS4("c30s004_020") from _call_BlinkXS4_902
    eva "Por entonces no había un [mc] que viniera a interrumpir tu soledad..."
    mc "Bueno, yo tenía que convivir con el [mc] de 12 años 24 horas al día."
    mc "Entiendo que puede ser un poco molesto. Por eso te pregunto si quieres que me quede."
    call BlinkXS4("c30s004_025") from _call_BlinkXS4_903
    eva "Gracias, [mc], pero preferiría estar sola ahora mismo."
    mc "No hay ningún problema, [eva]. Estaré aquí mismo, doblando la esquina, por si necesitas un abrazo."
    scene c30s004_025d with fade
    "Te sientas fuera de la vista de [eva], al doblar la esquina."
    "Sabes que, a veces, lo mejor es permanecer callado, esperando a que te necesiten."
    "Te han acusado muchas veces de hablar demasiado, pero conoces tu rincón, ahora el rincón de [eva], demasiado bien."
    "Cuando alguien quiere estar solo en ese rincón, significa que está en un mal momento."
    scene c30s004_025e with fade
    "Te das cuenta de que habéis pasado bastante rato en silencio cuando las luces de la piscina se encienden."
    "El sol casi se ha puesto ya."
    "Empiezas a dudar sobre si deberías irte o no. Parece que [eva] no va a querer hablar contigo."
    "Estás seguro de que, sea lo que sea lo que le pasa, hablar de ello le iría bien."
    "Tú nunca solucionaste nada pasando horas en el rincón. De lo único que te sirvió fue para autocompadecerte."
    stop music fadeout (1.5)
    "O para sentirte un idiota."
    play music ("music/Sad-Cinematic.ogg")
    eva "¿Aún estás ahí?"
    mc "Claro. Te he dicho que estaría aquí por si querías hablar."
    mc "Y si no quieres hablar, estaré aquí hasta que quieras ir a cambiarte para la cena."
    call BlinkXS4("c30s004_030") from _call_BlinkXS4_904
    eva "Sabes que soy sigilosa y que me podría haber ido sin darte cuenta, ¿verdad?"
    "Se ha secado las lágrimas de sus mejillas, pero la expresión en su cara te indica que podría seguir llorando si no estuvieras ahí."
    mc "Lo sé. También sé que no lo harías."
    call BlinkXS4("c30s004_035") from _call_BlinkXS4_905
    eva "¿Alguna vez me vas a dejar estar triste sin meterte por en medio?"
    mc "No si estoy a menos de 50 kilómetros de distancia."
    if eva._var("route"):
        mc "Es una de mis prerrogativas como tu pareja."
    else:
        mc "Es lo que hacemos en esta familia."
    call BlinkXS4("c30s004_040") from _call_BlinkXS4_906
    eva "Eres el único que ha venido..."
    mc "Porque te he oído cuando recogía los colchones de las tumbonas."
    mc "Sé lo solo que se puede estar en ese rincón. A veces sirve de más hablar que estar solos aquí, mortificándonos."
    call BlinkXS4("c30s004_045") from _call_BlinkXS4_907
    eva "Es que... si te lo explico... voy a parecer idiota."
    mc "Nadie se pasa dos horas en ese rincón si no tiene una buena razón, [eva]."
    mc "Es posible que la razón sea que somos idiotas. Eso no lo voy a negar."
    call BlinkXS4("c30s004_050") from _call_BlinkXS4_908
    eva "*Risa triste* ¿Incluso hoy tienes que intentar hacerme reír?"
    mc "Especialmente hoy."
    mc "No me gusta verte triste, y menos aún llorando."
    call BlinkXS4("c30s004_055") from _call_BlinkXS4_909
    mc "Entiendo que dejarnos llevar por las emociones y llorar un rato a veces es balsámico."
    mc "Y también entiendo que, cuando estamos así, lo que menos queremos es un payaso intentando hacernos reír."
    mc "Pero si la tristeza es sustituida por ira hacia el payaso, es un paso en la buena dirección."
    call BlinkXS4("c30s004_060") from _call_BlinkXS4_910
    eva "No quieres ser el centro de mi ira..."
    mc "No, no quiero serlo. Le tengo mucho aprecio a mis huesos intactos."
    mc "Pero si la ira te saca de la tristeza, estoy dispuesto a que me rompas alguno."
    mc "Uno pequeñito, que duela poco, si es posible."
    call BlinkXS4("c30s004_065") from _call_BlinkXS4_911
    eva "*Risa triste* Ciertamente eres un payaso."
    eva "Pero no conozco ningún hueso que no duela. Estoy entrenada para infligir dolor."
    call BlinkXS4("c30s004_070") from _call_BlinkXS4_912
    eva "No sirve de nada romper un hueso si no duele, ¿no?"
    mc "Podría servir de algo. Especialmente cuando hay un payaso bienintencionado alrededor."
    call BlinkXS4("c30s004_075") from _call_BlinkXS4_913
    eva "Creo que debería ir a cambiarme para la cena."
    mc "Me parece bien. ¿Dónde tienes la ropa? ¿Quieres que te acompañe?"
    call BlinkXS4("c30s004_080") from _call_BlinkXS4_914
    eva "¿No vas a intentar sonsacarme qué es lo que me pasa?"
    mc "No. Si quieres contármelo algún día, lo harás."
    if eva._var("route"):
        mc "Te quiero, pero no tengo derecho a interrogarte si no me lo quieres contar."
    else:
        mc "Te quiero, te has convertido en una nueva hermana para mí, pero no tengo derecho a interrogarte si no me lo quieres contar."
    call BlinkXS4("c30s004_085") from _call_BlinkXS4_915
    "La tristeza vuelve a aparecer en sus ojos, pese a que nunca la ha abandonado del todo."
    eva "¿Puedes abrazarme?"
    mc "Por supuesto. Sabes que eso se me da muy bien."
    scene c30s004_085d with fade
    eva "Incluso mejor que hacer el payaso."
    mc "Y eso se me da cojonudamente bien."
    scene c30s004_090a with fade
    call BlinkXS4("c30s004_090") from _call_BlinkXS4_916
    "Os mantenéis abrazados, en silencio, durante mucho rato, hasta que os separáis cuando el sol termina de ponerse."
    eva "Nos van a echar de menos en la cena..."
    mc "¿Quieres ir a cambiarte?"
    call BlinkXS4("c30s004_095") from _call_BlinkXS4_917
    eva "No."
    eva "Cuando has dicho que me querías..."
    mc "Te quiero. No puedo evitarlo. No quiero evitarlo."
    call BlinkXS4("c30s004_100") from _call_BlinkXS4_918
    eva "[deb.nick] y [lis] me han dicho casi lo mismo..."
    mc "¿Y por eso te has puesto así? A mí me gusta que me digan que me quieren."
    mc "¿Quieres explicármelo?"
    call BlinkXS4("c30s004_105") from _call_BlinkXS4_919
    eva "Vas a pensar que soy una idiota..."
    mc "No lo creo."
    mc "Te he visto llorar varias veces y siempre ha sido de alegría."
    mc "La única vez que te vi realmente triste fue cuando pasó lo de Gavin... Y hoy supera con creces a aquel día."
    call BlinkXS4("c30s004_110") from _call_BlinkXS4_920
    eva "Es que creo que les he hecho daño... a [lis] y a [deb.nick]."
    mc "Las he visto cuando venía hacia aquí y no me han comentado nada."
    mc "Si quieres, sigo aquí para que me lo expliques."
    scene c30s004_120a with fade
    eva "Estábamos las tres en la piscina, sentadas en las tumbonas..."
    eva "Le he dado las gracias a [deb.nick] por lo que dijo sobre mí y sobre [ama] hace un par de días."
    scene c30s004_120b with dissolve
    deb "No hace falta que me des las gracias. Lo dije de corazón. Las dos te queremos."
    scene c30s004_120c with dissolve
    lis "Sé que suena raro, pero el sábado, cuando [deb.nick] me dijo lo que había pasado, estuvimos hablando."
    lis "No sé cómo explicarlo, pero con todo este sentimiento familiar que se ha creado..."
    scene c30s004_120d with dissolve
    deb "Me niego a llamarte prima o algo por el estilo. Una prima suena como algo lejano."
    scene c30s004_120e with dissolve
    lis "Lo que [deb.nick] quiere decir es que las dos te queremos... os queremos a [ama] y a ti... como si fuerais nuestras nuevas hermanas."
    scene c30s004_120f with dissolve
    deb "Sabemos que es raro, que hace menos de un mes que os conocemos..."
    scene c30s004_120g with dissolve
    lis "Pero si algo me enseñó la fiesta en la que estuve el viernes es que cuando pienso en alguna chica en quien confío ciegamente es en vosotras."
    call BlinkXS4("c30s004_125") from _call_BlinkXS4_921
    eva "Y ahí se ha venido todo abajo..."
    scene c30s004_130a with fade
    scene c30s004_130An with dissolve
    eva "Me he quedado con la boca abierta, como una tonta, mirándolas a una y a la otra."
    eva "No sabía qué decir."
    scene c30s004_130c with fade
    eva "Y he salido corriendo, sin poder decir nada, hasta este rincón."
    call BlinkXS4("c30s004_135") from _call_BlinkXS4_922
    eva "Ahora lo puedes decir. Soy idiota. Prometo no romperte nada si lo dices."
    mc "No eres idiota, [eva]. No estás acostumbrada a que la gente te diga cuánto te quiere."
    mc "No has sabido cómo reaccionar."
    call BlinkXS4("c30s004_140") from _call_BlinkXS4_923
    eva "No es porque me hayan dicho que me quieren. Es porque me han dicho que me quieren como a su hermana."
    eva "Las dos estaban allí. Las dos se quieren un montón. Y me estaban incluyendo..."
    eva "Nos estaban incluyendo a [ama] y a mí. Como sus hermanas."
    mc "Ahora entiendo lo que te ha pasado. Y me reafirmo en lo que he dicho. No eres idiota."
    call BlinkXS4("c30s004_145") from _call_BlinkXS4_924
    eva "¿De verdad lo entiendes?"
    mc "Por supuesto que sí. Ya habías aceptado a dos hermanas con las que compartes genes. Ellas también te han dicho que te consideran sus hermanas."
    call BlinkXS4("c30s004_150") from _call_BlinkXS4_925
    eva "Sí... pero eso es natural. Como dices, somos casi trillizas."
    mc "Eso es lo más importante. [lis] y [deb.nick] te han nombrado su hermana de elección."
    call BlinkXS4("c30s004_155") from _call_BlinkXS4_926
    eva "Y yo no les he podido decir lo mismo."
    mc "Lo entiendo."
    call BlinkXS4("c30s004_160") from _call_BlinkXS4_927
    eva "[dap] y [eri] no son mis hermanas de elección. Tenemos los mismos genes. Somos hermanas lo queramos o no, al menos hasta cierto punto."
    if persistent.family:
        eva "Con Diana y Fiona también compartía genes, y también eran mis hermanas."
        eva "[ama], Beatrice, y Clarice eran mis hermanas de elección."
    else:
        eva "[ama], Fiona, Clarice, Diana, y Beatrice eran mis hermanas de elección."
    eva "Con ellas no compartía genes, pero compartía... otras cosas. Mi vida."
    mc "Es normal."
    call BlinkXS4("c30s004_165") from _call_BlinkXS4_928
    eva "No puedo decirles a [lis] y a [deb.nick] que las considero mis hermanas..."
    mc "Tiene sentido."
    call BlinkXS4("c30s004_170") from _call_BlinkXS4_929
    eva "Mis hermanas mueren a mi alrededor. A veces por culpa mía."
    eva "Tenía cinco hermanas. Y ahora cuatro de ellas no están. Y a una la maté yo."
    mc "Me dijisteis que murió en una explosión en un entrenamiento..."
    eva "Aquel día yo preparé los explosivos..."
    scene c30s004_085e with hpunch
    mc "No lo sabía, [eva]..."
    "La abrazas fuertemente. Con uno de esos abrazos típicos de los Marks que podrían romper costillas."
    "Creías que la entendías."
    "Te equivocabas."
    "Nunca podrás entender qué se siente al pensar que eres el culpable de la muerte de un ser querido."
    "Aún tienes mucho que aprender de lo que pasó en NTR en aquella época."
    eva "Me estás... haciendo daño..."
    "Su voz suena extrañada. Casi sorprendida."
    call BlinkXS4("c30s004_175") from _call_BlinkXS4_930
    mc "Lo siento."
    "La frase sirve tanto para la fuerza del abrazo como para lo que tuvo que pasar siendo una niña en Aruba."
    eva "Aaron dice que no fue culpa mía. Aquel día él estaba supervisando la preparación de los explosivos y dice que lo hice bien."
    eva "Pero..."
    scene c30s004_175d with dissolve
    "La mano de la chica busca el collar que casi siempre lleva puesto. Hoy, el collar no está ahí."
    mc "Pero no te puedes quitar de la cabeza qué hubiera pasado si hubieras hecho algo diferente."
    call BlinkXS4("c30s004_180") from _call_BlinkXS4_931
    eva "Exacto. Siempre sabré que a Fiona la maté yo."
    mc "Y piensas que, si les dices a [lis] y a [deb.nick] que las quieres como hermanas la estarías traicionando."
    mc "Y a Beatrice, Clarice, y Diana."
    call BlinkXS4("c30s004_185") from _call_BlinkXS4_932
    eva "Sí... ¿Aún no piensas que soy idiota?"
    mc "No, [eva]. Ninguno de nosotros puede pensarlo, porque ninguno de nosotros puede imaginar lo que experimentasteis."
    mc "Las seis pasasteis 24 horas al día juntas durante 12 años. Y pasasteis por muchas cosas malas juntas."
    mc "Una relación de menos de un mes no se puede comparar a eso."
    call BlinkXS4("c30s004_190") from _call_BlinkXS4_933
    eva "Es... diferente..."
    mc "Es exactamente eso. Diferente. Tuviste cinco hermanas y ahora tienes dos más."
    mc "Y ahora empiezas a ver al resto de las chicas bajo otra luz. Si no lo hicieras, no te hubiera afectado lo que [deb.nick] y [lis] dijeron."
    call BlinkXS4("c30s004_195") from _call_BlinkXS4_934
    "Su mano vuelve a buscar el collar."
    eva "Sí..."
    mc "Aún no están a la altura de tus hermanas originales. Quizás no lo estén nunca."
    mc "Pero empiezas a sentir por ellas cosas que sólo habías sentido por tus hermanas."
    call BlinkXS4("c30s004_200") from _call_BlinkXS4_935
    eva "Eso es lo que me da miedo. No solo las estoy traicionando, sino que..."
    mc "No las vas a olvidar nunca. Ni las vas a sustituir."
    if persistent.family and mc._var("edmundsStory"):
        mc "Cuando descubrimos que [sca] era mi medio hermana, no sustituyó a [emm]."
    elif mar._var("pregnant") and persistent.family:
        mc "Cuando [mar] de a luz, tendré un hermano o una hermana nuevos. No va a sustituir a [emm]."
    elif mar._var("route") and persistent.family:
        mc "Si [mar] se queda embarazada, tendré un hermano o una hermana nuevos. No va a sustituir a [emm]."
    elif persistent.family:
        mc "Si [mar] tiene otro bebé algún día, tendré un hermano o una hermana nuevos. No sustituiría a [emm]."
    else:
        mc "Si mi padre tuviera un bebé, tendría un hermano o una hermana nuevos. No sustituiría a [emm]."
    call BlinkXS4("c30s004_205") from _call_BlinkXS4_936
    eva "Pero eso es porque hay genes en común... Esto es diferente. Es elegir hermanas nuevas."
    "Está empezando a estar molesta por no poder convencerte de verlo desde su punto de vista."
    "Es el momento de cambiar de táctica."
    mc "Jamaal nunca sustituyó a [emm]. Yo elegí que fuera mi hermano."
    stop music fadeout (1.5)
    mc "Lo sé. *Risa* Quizás fuera una elección rara."
    call BlinkXS4("c30s004_210") from _call_BlinkXS4_937
    play music ("music/SadSoul.ogg")
    eva "*Risa* Eres idiota."
    "Por primera vez, no hay una nota de tristeza en su risa."
    "Parece que tus palabras la están empezando a convencer de lo equivocada que está."
    mc "*Risa* También lo sé."
    mc "Pero lo que quiero decir es que puedes tener varias hermanas de elección y no se sustituirán entre ellas."
    mc "Pasa lo mismo con la familia. ¿Te acuerdas de la Navidad en la playa?"
    call BlinkXS4("c30s004_215") from _call_BlinkXS4_938
    eva "Sí. ¿A qué te refieres?"
    mc "Me dijiste algo como 'Esa no es mi familia. Mi familia es [ama]. Y ni siquiera es Navidad'."
    call BlinkXS4("c30s004_220") from _call_BlinkXS4_939
    eva "¡Es que no era Navidad!"
    mc "Sabes que no es eso a lo que me refiero."
    mc "Ahora consideras tu familia a las chicas y a mí. Quizás incluso a Jamaal."
    mc "*Risa* Tú también puedes hacer elecciones raras."
    call BlinkXS4("c30s004_225") from _call_BlinkXS4_940
    eva "*Risa* Sigues siendo idiota."
    mc "Pero, ¿consideras menos familia a [ama] ahora que también consideras familia a [nor]... o a [eil]?"
    "Evitas nombrar a [eri] o a [dap] a propósito. De esa forma cubres la familia más amplia."
    call BlinkXS4("c30s004_230") from _call_BlinkXS4_941
    eva "No... Pero..."
    mc "No hay 'peros'. No te estoy diciendo que tengas que ir a abrazar a [lis] y a [deb.nick] y decirles que las consideras tus hermanas."
    mc "Un día quizás lo hagas. O quizás ese día no llegue nunca y seáis tan solo buenas amigas."
    mc "Pero lo hagas o no lo hagas, ninguna de ellas va a sustituir a Fiona. O a Beatrice, Clarice, o Diana."
    call BlinkXS4("c30s004_235") from _call_BlinkXS4_942
    eva "Te quiero."
    if not eva._var("route"):
        eva "A ti te puedo decir que te quiero como a un hermano."
    mc "Yo también te quiero."
    "Reconoces esa chispa en sus ojos, acompañada por una sonrisa sincera."
    "La has visto mil veces en los ojos de [emm] cuando todo hace clic en su cabeza en un segundo."
    scene c30s004_085f with dissolve
    "Os volvéis a abrazar. Esta vez sin que ninguno haga daño al otro."
    eva "A veces me pregunto por qué. Y recuerdo que siempre estás aquí para mí."
    mc "Y siempre voy a estar para ti cuando me necesites. Incluso cuando no quieras que esté."
    eva "Lo sé."
    if eva._var("route"):
        mc "*Risa* Espero que no me quieras como a un hermano."
        if emm._var("route"):
            eva "*Risa* Teniendo en cuenta tu relación con [emm], no creo que haya mucha diferencia."
        else:
            eva "*Risa* Idiota."
    "Es un abrazo largo."
    "[eva] está mucho mejor que en los abrazos anteriores."
    "No sabes qué pasa por su cabeza, pero te alegras de lo que su cuerpo, mucho más relajado que antes, transmite."
    mc "Un día me tienes que explicar la historia de ese collar que siempre buscas cuando hablas de tus hermanas."
    "La pelirroja se tensa por un momento entre tus brazos."
    eva "Quizás otro día."
    mc "Entonces me tienes que explicar por qué llevas un traje de neopreno para venir a la piscina."
    eva "*Risa* Eso también tendrá que esperar."
    eva "Y ahora abrázame en silencio."
    "Es una forma educada de decirte que hablas demasiado. Esta vez te alegras de haber hablado mucho."
    "El lenguaje corporal de [eva] te indica que la conversación ha sido buena para ella."
    scene c30s004_240a with fade
    "Cuando decidís interrumpir el abrazo e ir a cenar, ya no queda nadie en la cocina de [nor]."
    "Hay una nota en la encimera indicándoos que os han dejado la cena en la nevera."
    stop music fadeout (1.5)
    "No te puedes imaginar cómo sabían que ibais a llegar a cenar tarde."
    if eva._var("route"):
        eva "Si empiezas a comportarte estúpidamente romántico después de esto, te enseñaré que yo también puedo dar abrazos que duelan."
    scene c30s004_240b with fade
    "Un par de horas antes..."
    play music ("music/SaveMe.ogg")
    ama "[nor], dudo que [eva] y [mc] vayan a llegar a la cena."
    nor "¿Pasa algo, cielo?"
    ama "Nada malo. Creo que [mc] está ayudando a [eva] ahora mismo más de lo que se puede imaginar."
    nor "(Y, sea lo que sea lo que está haciendo, por lo que dice tu sonrisa, también te está ayudando a ti.)"
    return
label c30s004_EmmMarEri:
    if _in_replay:
        $ mc._var("relationships", 0, "set")
        call mrS3_emm_route from _call_mrS3_emm_route_43
        call mrS3_eri_route from _call_mrS3_eri_route_33
        call mrS3_mar_route from _call_mrS3_mar_route_44
        call mrS3_mad_route from _call_mrS3_mad_route_18
        if mc._var("relationships")==0:
            call mrS3_rels from _call_mrS3_rels_38
    scene black with dissolve
    centered "{size=+20}{b}DÍA 36 – MARTES{/b}{/size}"
    play music ("music/RhythmPlay.ogg")
    scene c30s004_250a with fade
    "A la mañana siguiente, mientras aún duermes..."
    eri "Menos mal que Tía [bet] y la abuela vuelven hoy."
    mom "Se ha hecho largo que no estuvieran, y [bet] se vuelve a ir en un par de días."
    emm "Creo que va a estar muy ocupada esos días. Todas vamos a querer pasar tiempo con ella antes de que se vaya."
    call BlinkXS4("c30s004_255") from _call_BlinkXS4_943
    mom "No la agobiéis demasiado. Seguramente tendrá que preparar cosas antes de irse."
    call BlinkXS4("c30s004_260") from _call_BlinkXS4_944
    eri "Yo tenía la intención de ayudarle a preparar esas cosas."
    eri "Ayudarle a deshacer y volver a hacer las maletas es una forma de pasar tiempo con ella."
    call BlinkXS4("c30s004_265") from _call_BlinkXS4_945
    emm "*Risa* ¡La cucaracha es lista! No se me había ocurrido."
    emm "Creo que ayudarla a llevar la ropa a la sala de la colada y esas cosas puede ser divertido... Por una vez."
    if emm._var("route"):
        call BlinkXS4("c30s004_270") from _call_BlinkXS4_946
        mom "*Risa* Tú tienes experiencia en diversión en la sala de la colada."
        call BlinkXS4("c30s004_275") from _call_BlinkXS4_947
        eri "Lo que no entiendo es cómo pudiste evitar que... ya sabes..."
        call BlinkXS4("c30s004_280") from _call_BlinkXS4_948
        emm "*Risa* Porque mi plan funcionó genial. De cintura para arriba estaba dentro de la lavadora."
        emm "A veces os quejáis de que mis planes nunca funcionan. ¡Zas! En toda la boca."
        call BlinkXS4("c30s004_285") from _call_BlinkXS4_949
        emm "Estuvo a punto de irse a la mierda cuando me propuso subir a su habitación..."
        emm "Pero me resistí lo suficiente."
        call BlinkXS4("c30s004_290") from _call_BlinkXS4_950
        if persistent.family:
            mom "No podéis saber lo raro que es que mi hija me diga que se ha follado a mi hijo y que me parezca normal."
        else:
            mom "No podéis saber lo raro que es que [emm] me diga que se ha follado a [mc] y que me parezca normal."
        if mar._var("route"):
            mom "Y que haya sido con un plan que no se me haya ocurrido a mí."
            call BlinkXS4("c30s004_295") from _call_BlinkXS4_951
            emm "*Risa* ¡Eso es porque ves poco porno, Mamá!"
            if eri._var("route"):
                call BlinkXS4("c30s004_300") from _call_BlinkXS4_952
                eri "*Risa* Creo que últimamente todas vemos más porno de lo habitual."
                call BlinkXS4("c30s004_305") from _call_BlinkXS4_953
                mom "Vosotras habéis tenido tiempo a solas con él hace poco. Yo no he tenido sexo desde... antes de que se fuera a Monterrey."
            else:
                call BlinkXS4("c30s004_300") from _call_BlinkXS4_954
                eri "*Risa* Creo que últimamente Tía [mar] ve más porno de lo habitual."
                call BlinkXS4("c30s004_305") from _call_BlinkXS4_955
                mom "[emm] tuvo tiempo a solas con él ayer. Yo no he tenido sexo desde antes de que se fuera a Monterrey."
            call BlinkXS4("c30s004_355") from _call_BlinkXS4_956
            emm "Yo lo hubiera tenido allí, pero con lo de Tía [bet]..."
    if mc._var("relationships")>0:
        call BlinkXS4("c30s004_310") from _call_BlinkXS4_957
        eri "Menos mal que todo acaba hoy. Estoy un poco harta de pasar calor."
        call BlinkXS4("c30s004_315") from _call_BlinkXS4_958
        mom "Yo de lo que estoy cansada es de tener que evitar a [mc] cuando él también está a punto de irse."
        if mar._var("route"):
            mom "Pero sabemos lo que podría pasar y se fastidiaría la sorpresa."
        else:
            mom "Pero si no lo evitamos las que no estamos con él, sospecharía de las que lo evitan estando con él."
        call BlinkXS4("c30s004_320") from _call_BlinkXS4_959
        emm "No sé a quién se le ocurrió el plan, pero es peor que uno de mis planes."
        call BlinkXS4("c30s004_325") from _call_BlinkXS4_960
        if mad._var("route"):
            eri "Bueno, todo empezó cuando [mc] le pidió matrimonio a [mad.nick]..."
            eri "Y después a Jamaal se le ocurrió la idea en el grupo de WhatsUp."
        else:
            eri "Bueno, todo empezó con aquella conversación en el grupo de WhatsUp sobre anillos..."
            eri "Y después, cuando Jamaal vio los mensajes, se le ocurrió la idea."
        call BlinkXS4("c30s004_330") from _call_BlinkXS4_961
        emm "*Risa* Es verdad. Odio a Jamaal."
        call BlinkXS4("c30s004_335") from _call_BlinkXS4_962
        mom "*Risa* Todas odiamos a Jamaal."
        call BlinkXS4("c30s004_340") from _call_BlinkXS4_963
        if mad._var("route"):
            eri "No seáis así. A él se le ocurrió la idea después de lo que dijo [mad.nick]. Pero todas lo aceptamos."
        else:
            eri "No seáis así. A él se le ocurrió la idea. Pero todas lo aceptamos."
        call BlinkXS4("c30s004_345") from _call_BlinkXS4_964
        mom "Sobre el papel, la idea era muy buena. Pero llevarla a práctica..."
        mom "Ciertamente parece un plan de [emm]."
        call BlinkXS4("c30s004_350") from _call_BlinkXS4_965
        emm "*Risa* Mi venganza será histórica, Mamá."
        emm "Si al menos Jamaal estuviera disponible para entretener a [mc]..."
        emm "Por cierto, ¿sabéis cómo le va con Anthony?"
    else:
        call BlinkXS4("c30s004_310") from _call_BlinkXS4_966
        eri "Hablando de colada, tengo que poner los uniformes en la lavadora."
        eri "Os veo luego."
    scene black with dissolve
    stop music fadeout (1.5)
    return
label c30s004_NorGetsBetMee:
    if _in_replay:
        call mrS3_nor_route from _call_mrS3_nor_route_32
    call BlinkXS4("c30s004_400") from _call_BlinkXS4_967
    "Después de comer..."
    play music ("music/romantic-day.ogg")
    nor "¿Ya tienes preparado todo lo que te tienes que llevar a Aruba?"
    mc "Prácticamente. Estos últimos días han sido raros y he tenido un montón de tiempo libre."
    call BlinkXS4("c30s004_405") from _call_BlinkXS4_968
    nor "¿A qué te refieres con raros?"
    mc "No lo sé. El último mes siempre ha habido alguna de vosotras que necesitaba algo o que quería pasar tiempo conmigo."
    mc "Desde la semana pasada parece que sea justo lo contrario. Parece que me estáis evitando."
    call BlinkXS4("c30s004_410") from _call_BlinkXS4_969
    nor "*Risa* ¿No crees que te estás volviendo un poco paranoico?"
    nor "Es posible que no haya surgido nada en lo que pudieras ayudar a alguien. No somos damiselas indefensas."
    mc "No sé. A lo mejor tienes razón."
    if nor._var("route"):
        scene c30s004_410d with dissolve
        mcp "(Creo que nunca me cansaré de verlas... Y con ese vestido están espectaculares.)"
    call BlinkXS4("c30s004_415") from _call_BlinkXS4_970
    nor "Y, por lo que sé, ayudaste a [mar] a ir a hacer la compra, y fuiste a recoger a las chicas al café..."
    nor "Te seguimos necesitando, pero no todos los días hay un gran problema que resolver."
    mc "*Risa* Por suerte."
    call BlinkXS4("c30s004_420") from _call_BlinkXS4_971
    nor "Y otras veces no te pedimos cosas que por norma te pediríamos a ti."
    nor "Ahora voy a ir a buscar a tu abuela y a [bet] al aeropuerto, por ejemplo."
    mc "Eso por norma lo hacía yo..."
    call BlinkXS4("c30s004_425") from _call_BlinkXS4_972
    nor "Lo sé, pero era porque yo estaba ocupada. Ahora mismo no tengo nada que hacer, y me apetece ver a mi madre."
    nor "*Risa* Si hace un mes me hubieran dicho que podría decir esa frase..."
    mc "*Risa* No se lo hubiera creído nadie. Estabas super tensa cuando tenía que venir, y mírate ahora."
    call BlinkXS4("c30s004_430") from _call_BlinkXS4_973
    nor "Ha cambiado mucho desde que vino a casa. Nos hemos hecho amigas..."
    mc "Algo que hubiera sido imposible hace unos años."
    call BlinkXS4("c30s004_435") from _call_BlinkXS4_974
    nor "Lo importante es que ahora es posible que lo seamos."
    nor "En el momento en que descubrimos que teníamos más cosas en común de lo que pensábamos..."
    mc "Dejasteis aparcadas vuestras diferencias. Me alegro mucho por las dos."
    mc "También ayudó que dejara de querer dirigir la vida de todo el mundo."
    call BlinkXS4("c30s004_440") from _call_BlinkXS4_975
    nor "*Risa* ¡Oh! ¡Eso todavía quiere hacerlo! Pero nadie se lo permite."
    nor "También ayudó mucho que vuestro juego de verdad o reto la inmunizara sobre los besos en la familia."
    mc "*Risa* Tienes razón. Casi le da un infarto aquella primera noche."
    if nor._var("route"):
        call KissXS4("c30s004_445") from _call_KissXS4_25
    call BlinkXS4("c30s004_445") from _call_BlinkXS4_976
    nor "La tentación de quedarme aquí criticando a la antigua versión de mi madre es muy grande."
    nor "Pero si no llego a tiempo al aeropuerto se va a enfadar."
    mc "*Risa* No creo que nunca cambie en lo estricta que es con la puntualidad. Te veo luego."
    scene c30s004_445e with dissolve
    nor "Creo que [sam.nick] quería hablar contigo de algo. A lo mejor te pide algo que hace que se te pase un poco la paranoia."
    stop music fadeout (1.5)
    mc "*Risa* Mientras no me pida que vaya a buscar a Jamaal..."
    return
label c30s004_getJam:
    scene c30s004_500a with fade
    "Das una vuelta por la casa, buscando a [sam]. La encuentras hablando con [oma] y [meg]."
    play music ("music/These-Little-Moments.ogg")
    "Hoy ha venido casi todo el mundo a comer. Sólo han faltado las chicas que están trabajando en el café, [mad.nick], y Jamaal."
    "Incluso [meg] ha venido. Es la primera vez que viene fuera del fin de semana o el lunes, que es su día libre."
    mc "Hey, [sam.nick]. [nor] me ha dicho que me estabas buscando."
    scene c30s004_500b with dissolve
    meg "*Risa* ¿Solo 'Hey, [sam.nick]'? ¿[oma] y yo somos invisibles?"
    oma "*Risa* Este tío quiere que lo arreste. Seguro que hay alguna oscura normativa que me permite hacerlo."
    sam "*Risa* Chicas, dadle un respiro. Ha empezado por la más guapa. Estoy segura de que os iba a saludar a vosotras también."
    scene c30s004_500c with dissolve
    meg "*Risa* O a lo mejor ha empezado por la más vieja porque quiere saludarte antes de que te tengas que ir a cambiar los pañales de la incontinencia."
    oma "*Risa* [sam.nick], yo no me metería con [meg]. Esta chica tiene la lengua afilada."
    sam "*Risa* Vale, vale. Ha empezado por orden de edad y, coincidentemente, por la más guapa."
    sam "Jamaal ya me había avisado de las cosas que pueden salir de esa boca. Y no me refiero solo a cómo canta."
    mc "Hola, [oma] y [meg]. ¿Contentas?"
    scene c30s004_500d with dissolve
    todas "*Risa* Sí."
    mc "Bueno, ¿me necesitabas para algo, [sam.nick]?"
    call BlinkXS4("c30s004_505") from _call_BlinkXS4_977
    sam "Me ha escrito Jamaal y me ha dicho que ya ha acabado el trabajo. ¿Puedes ir a buscarlo?"
    mc "Ya se ha acabado la comida. *Risa* ¿Para qué quiere venir?"
    call BlinkXS4("c30s004_510") from _call_BlinkXS4_978
    sam "No seas idiota. Mi hijo piensa en más cosas aparte de la comida. Algunas veces, al menos."
    call BlinkXS4("c30s004_515") from _call_BlinkXS4_979
    meg "¿Desde cuándo?"
    call BlinkXS4("c30s004_520") from _call_BlinkXS4_980
    oma "Supongo que desde que está con Anthony, ¿no?"
    call BlinkXS4("c30s004_525") from _call_BlinkXS4_981
    sam "*Risa* Más o menos. Diría que Jamaal ha perdido cuatro o cinco libras desde empezaron a salir."
    mc "¿Jamaal está adelgazando? ¡Eso quiere decir que van en serio!"
    "No quieres que te cuenten cotilleos. Si vas a recoger a Jamaal, ya se lo preguntarás a él."
    mc "Pero ¿por qué no me ha escrito a mí para que vaya a buscarlo?"
    call BlinkXS4("c30s004_530") from _call_BlinkXS4_982
    oma "Mmmm... ¿Llevas el móvil encima?"
    "Te palpas los bolsillos buscando el móvil sin encontrarlo."
    mc "Ermmm... No. Lo he dejado cargando en mi habitación."
    call BlinkXS4("c30s004_535") from _call_BlinkXS4_983
    meg "Pues por eso. A lo mejor te ha escrito y, al no contestarle, ha escrito a [sam.nick]."
    mc "Tiene lógica... Bueno, voy a buscar a Jam. Os veo en un rato."
    call BlinkXS4("c30s004_540") from _call_BlinkXS4_984
    sam "Sube la maleta que hay en la camioneta a mi casa, por favor."
    sam "Supongo que [mar] ya la habrá dejado ahí. Si no hay maleta, pregúntale a ella."
    "No es la primera maleta con ropa que llevas a esa casa."
    "[emm] o [mar] les han regalado ropa a [sim] y a [sam] algunas veces, especialmente cuando van mal de dinero."
    "Lo del supermercado de hace unos días te enseñó que es uno de esos momentos para ellas."
    "Lástima que no quieran aceptar ayuda. Al menos esperas que los planes que has trazado con [nor] sean una forma de ayudarlas."
    "También esperas que no te maten cuando se enteren. Por suerte, estarás en Aruba por entonces."
    mc "OK. Nos vemos luego."
    stop music fadeout (1.5)
    scene drive_day with fade
    "Ciertamente hay un mensaje de Jamaal en tu móvil."
    "La maleta está en el asiento trasero, con lo que conduces hasta casa de Jamaal."
    scene c30s004_545d with fade
    play sound ("music/doorbell1.ogg")
    "*Ding-Dong*"
    jam "*A través de la puerta* ¡Voy!"
    play music ("music/Vacation-Vibe.ogg")
    call BlinkXS4("c30s004_545") from _call_BlinkXS4_985
    jam "¡Ya era hora de que vinieras!"
    mc "¿Qué haces vestido así? ¿Ahora te pones traje para hacer videoconferencias?"
    call BlinkXS4("c30s004_550") from _call_BlinkXS4_986
    jam "¿Tú eres tonto? Hoy es la fiesta. Llegan Tía [bet] y [mee]."
    mc "¿Qué fiesta? Nadie me ha dicho nada..."
    call BlinkXS4("c30s004_555") from _call_BlinkXS4_987
    jam "¿Nadie te ha dicho que íbamos a dar una fiesta porque vuelven [mee] y Tía [bet]?"
    jam "Creo que tendré que hablar con esas chicas. La comunicación no fluye fuera del grupo de WhatsUp."
    mc "Espera... creo que sí que me dijeron algo, pero no recuerdo cuando."
    mc "Y no voy vestido para una fiesta. Bueno, tengo mejor pinta que tú con ese traje, pero..."
    call BlinkXS4("c30s004_560") from _call_BlinkXS4_988
    jam "Me ha dicho mi madre que metían tu ropa en la maleta o no te iba a dar tiempo de cambiarte."
    jam "Pasa a la habitación de [sim] a cambiarte, si quieres, mientras yo recojo la mía. Deja el resto de la ropa en la maleta."
    mc "OK. Espérame ahí sentado. Pero me tendrás que dejar pasar, ¿no?"
    scene c30s004_560d with fade
    mc "Por cierto, ¿qué tal con Anthony?"
    mc "Desde que estás con él no te vemos apenas."
    mc "No es que tenga ganas de ver tu fea cara, pero..."
    jam "*A través de la puerta* ¿Mi fea cara? ¿Tú te has mirado a un espejo últimamente?"
    mc "Yo sí. ¿Y tú? Los espejos seguramente se descuelguen de la pared y salgan corriendo cuando te acercas."
    mc "Pero me doy cuenta de que, hablando contigo a través de una puerta, no me dan ganas de vomitar."
    jam "*A través de la puerta* *Risa* Eso es porque [sim] no tiene un espejo en el interior de la puerta para que te reflejes."
    mc "*Risa* Yo no soy feo. Tengo una belleza... Picassiana... Lo que me convierte en una obra de arte."
    jam "*A través de la puerta* *Risa* Más bien una belleza Daliniana. Parece que la cara se te ha derretido en algunas partes."
    mc "*Risa* Acabas de reconocer que soy una obra de arte. Punto para mí."
    jam "*A través de la puerta* *Risa* ¡Mielda!"
    mc "Pero no me has contestado a la pregunta sobre Anthony."
    jam "*A través de la puerta* Te lo explico cuando acabes de cambiarte. Me jode hablar con una puerta."
    jam "*A través de la puerta* Aunque la puerta tenga más cerebro que tú."
    mc "¿Es la puerta contra la que te diste el golpe cuando eras pequeño y dejaste tus sesos ahí?"
    jam "*A través de la puerta* ¡No tengo por qué aguantar esto! ¡Me voy a cagar mientras acabas de cambiarte!"
    mc "*Risa* Demasiada información."
    scene c30s004_565a with fade
    call BlinkXS4("c30s004_565") from _call_BlinkXS4_989
    "Menos de cinco minutos después..."
    "(Sí, tú puedes tardar menos de cinco minutos en vestirte.)"
    jam "¡Joder! Pues sí que te queda mejor el traje que a mí."
    mc "Para que me quedara peor debería ser un saco de patatas. Usado. Roto. Con 300 años de patatas en su historial."
    call BlinkXS4("c30s004_570") from _call_BlinkXS4_990
    jam "*Risa* Eres un capullo."
    mc "Lo sé. Pero me quieres por ello."
    mc "*Risa* Porque aún me quieres, ¿verdad?"
    call BlinkXS4("c30s004_575") from _call_BlinkXS4_991
    jam "¿Estás celoso de Anthony? Me sorprendes, [mc] Marks."
    mc "¿Celoso? No. Pero te echo de menos, colega. Ya no te veo casi nunca."
    call BlinkXS4("c30s004_580") from _call_BlinkXS4_992
    jam "Bueno... Intento pasar casi todo mi tiempo libre con él. Sé que he dejado de lado un poco a la familia estos días..."
    mc "Es normal. Los inicios de una relación son así."
    mc "Todo va bien con él, supongo."
    call BlinkXS4("c30s004_585") from _call_BlinkXS4_993
    jam "Sí. Todo va genial. Sé que es pronto para decirlo, pero creo que vamos en serio."
    mc "Eso suena muy bien. Podrías haberle dicho que viniera a la fiesta de hoy."
    mc "Así se lo podrías haber presentado al resto de la familia, a las que no lo conocen aún."
    call BlinkXS4("c30s004_590") from _call_BlinkXS4_994
    jam "*Risa* Tú no quieres eso. Si estuviera ahí... No sé... Creo que no le podría prestar la atención que se merece a la fiesta."
    mc "Estáis en ese momento en que no hay tiempo suficiente para todos los besos que os queréis dar, ¿verdad?"
    mc "Cuando vuestras manos tienen en que estar en contacto con las manos del otro..."
    mc "*Risa* Si es en contacto con otra parte de vuestro cuerpo, prefiero no saberlo."
    call BlinkXS4("c30s004_595") from _call_BlinkXS4_995
    jam "*Risa* Eres un capullo, pero tienes razón. Es ese momento en el que miras la agenda del día buscando un hueco para verle."
    mc "Me alegro mucho por ti, colega."
    mc "¿Has conocido a su hermana?"
    call BlinkXS4("c30s004_600") from _call_BlinkXS4_996
    jam "¿A cuál de ellas? A Harley sí, nos la encontramos en el centro comercial."
    jam "A Olga todavía no. No vive en Newport. Por lo que dice Anthony, es la 'hermana buena'."
    mc "Harley me pareció una tía muy maja."
    call BlinkXS4("c30s004_605") from _call_BlinkXS4_997
    jam "Es maja, pero es muy conservadora y todavía le cuesta un poco aceptar por lo que está pasando Anthony, aunque va dando pasos en la buena dirección."
    jam "Olga siempre lo ha apoyado en todas las decisiones que ha tomado..."
    mc "*Risa* Eso es porque todavía no sabe que ha decidido salir contigo."
    call BlinkXS4("c30s004_610") from _call_BlinkXS4_998
    jam "*Risa* ¡Eres un capullo!"
    mc "Te estás volviendo repetitivo con los insultos. Creo que Anthony te ha chupado el poco cerebro que te quedaba..."
    mc "*Risa* Si te ha chupado otra cosa, tampoco lo quiero saber."
    call BlinkXS4("c30s004_615") from _call_BlinkXS4_999
    jam "Va, vámonos o vamos a llegar tarde. Van a pensar que te has feminizado y has tardado una hora en cambiarte."
    jam "Además, puedo contarte mis aventuras sexuales con Anthony en la camioneta."
    mc "Si puedes contármelas en los diez minutos que tardamos en llegar a casa, es que no hay tanto que contar."
    scene c30s004_615d with dissolve
    jam "Te haré un resumen centrándome en las partes más picantes."
    stop music fadeout (1.5)
    mc "*Risa* Noooooo."
    return
label c30s006_atHome:
    if _in_replay:
        $ mc._var("relationships", 0, "set")
        call mrS3_sai_route from _call_mrS3_sai_route_21
        call mrS3_mar_route from _call_mrS3_mar_route_45
        call mrS3_emm_route from _call_mrS3_emm_route_44
        call mrS3_eri_route from _call_mrS3_eri_route_34
        call mrS3_nor_route from _call_mrS3_nor_route_33
        call mrS3_dap_route from _call_mrS3_dap_route_34
        call mrS3_sca_route from _call_mrS3_sca_route_28
        if sca._var("route"):
            call mrS3_edmund_story from _call_mrS3_edmund_story_13
        call mrS3_eil_route from _call_mrS3_eil_route_25
        call mrS3_sam_route from _call_mrS3_sam_route_23
        call mrS3_sim_route from _call_mrS3_sim_route_23
        call mrS3_oma_route from _call_mrS3_oma_route_18
        call mrS3_eva_route from _call_mrS3_eva_route_19
        call mrS3_mad_route from _call_mrS3_mad_route_19
        call mrS3_meg_route from _call_mrS3_meg_route_9
        call mrS3_ama_route from _call_mrS3_ama_route_16
        call mrS3_mee_route from _call_mrS3_mee_route_14
        call mrS3_kim_route from _call_mrS3_kim_route_14
        call mrS3_kat_route from _call_mrS3_kat_route_6
        call mrS3_deb_route from _call_mrS3_deb_route_28
        if deb._var("route"):
            call mrS3_deb_pregnant from _call_mrS3_deb_pregnant_2
        call mrS3_lis_route from _call_mrS3_lis_route_25
        if lis._var("route"):
            call mrS3_lis_pregnant from _call_mrS3_lis_pregnant_1
        call mrS3_bet_route from _call_mrS3_bet_route_11
        call mrS3_kia_route from _call_mrS3_kia_route_18
    scene c30s006_005a with fade
    call BlinkXS4("c30s006_005") from _call_BlinkXS4_1000
    "Al llegar a casa..."
    "No, Jamaal no te ha dado demasiada información sobre su relación con Anthony. Al menos sobre las partes que menos te importan."
    play music ("music/Wonder.ogg")
    "Crees que él ha aprendido de ti que, lo que pasa en una habitación con dos... o más... personas, solo les atañe a ellas."
    mc "¿En qué casa es la fiesta? Y no te lo he preguntado, pero ¿por qué vamos con traje?"
    jam "Bueno, esta fiesta no solo es para darles la bienvenida a [bet] y a [mee]."
    jam "También es para despediros a [bet], a [ama], y a ti."
    jam "Las chicas querían hacer algo elegante."
    call BlinkXS4("c30s006_010") from _call_BlinkXS4_1001
    jam "*Risa* Hoy no va a haber un montón de tetas al aire. O eso espero."
    mc "*Risa* Sabes que, si querían darme una sorpresa, la acabas de fastidiar, ¿verdad?"
    call BlinkXS4("c30s006_015") from _call_BlinkXS4_1002
    jam "Si te hubieran querido dar una sorpresa, no te hubieran dicho que había una fiesta, ¿no?"
    mc "Veo que tu cerebro aún funciona. Levemente, al menos."
    call BlinkXS4("c30s006_020") from _call_BlinkXS4_1003
    call check_relationships_c30 from _call_check_relationships_c30
    if mc._var("relationships")==0:
        jam "Vamos a la cocina de [nor]. Creo que alguna de las mujeres ya está allí."
        stop music fadeout (1.5)
        return
    elif mad._var("route") or kia._var("route") or mar._var("route") or sim._var("route"):
        jam "Además, todo esto es culpa tuya."
        if kia._var("route"):
            jam "Si no le hubieras pedido matrimonio a [kia], esta fiesta sería diferente."
        elif mad._var("route"):
            jam "Si no le hubieras pedido matrimonio a [mad.nick], esta fiesta sería diferente."
        elif mar._var("route"):
            jam "Si no le hubieras pedido matrimonio a [mar], esta fiesta sería diferente."
        else:
            jam "Si no hubieras aceptado cuando mi hermana te pidió matrimonio, esta fiesta sería diferente."
    else:
        jam "Además, todo esto es culpa tuya."
        jam "Si fueras capaz de mantener tu polla dentro de los pantalones, esta fiesta sería diferente."
        if mc._var("relationships")==1:
            if kat._var("route") or ama._var("route"):
                mc "No sé a qué te refieres. ¡No he follado desde que volví a Newport!"
        elif mc._var("relationships")==2:
            if kat._var("route") and ama._var("route"):
                mc "No sé a qué te refieres. ¡No he follado desde que volví a Newport!"
    return
label c30s006_wedding:
    if _in_replay:
        call c30s006_atHome from _call_c30s006_atHome_1
    mc "¿Qué tiene que ver eso con esta fiesta?"
    scene c30s006_025d with dissolve #mira el móvil
    jam "Déjame mirar una cosa un momento..."
    call BlinkXS4("c30s006_025") from _call_BlinkXS4_1004
    jam "¡Por Dios! Odio que las mujeres tarden mil horas en cambiarse."
    mc "*Risa* Bienvenido a mi mundo."
    mc "Pero aún no me has contestado."
    call BlinkXS4("c30s006_030") from _call_BlinkXS4_1005
    $ proposals = 0
    if mad._var("route"):
        $ proposals = proposals + 1
    if kia._var("route"):
        $ proposals = proposals + 1
    if mar._var("route"):
        $ proposals = proposals + 1
    if sim._var("route"):
        $ proposals = proposals + 1
    if proposals==1:
        if mc._var("relationships")>1:
            jam "No puedes proponerle matrimonio a una chica y esperar que el resto del harén no quiera lo mismo."
            if sim._var("route"):
                mc "Bueno, fue ella quien me lo pidió..."
                mc "Pero sí, lo entiendo."
            else:
                mc "Lo entiendo..."
        else:
            jam "No puedes proponerle matrimonio a una chica y no darle un anillo."
            if sim._var("route"):
                mc "Bueno, fue ella quien me lo pidió..."
                mc "Pero sí, lo entiendo."
            else:
                mc "Técnicamente se lo di..."
    elif proposals > 1:
        if mc._var("relationships")>proposals:
            jam "No puedes proponerles matrimonio a [proposals] chicas y esperar que el resto del harén no quiera lo mismo."
        else:
            jam "No puedes proponerles matrimonio a [proposals] chicas y esperar que no hablen entre ellas."
        mc "Sería un iluso si esperara eso..."
    else:
        if mc._var("relationships")==1:
            if ama._var("route") or bet._var("route"):
                jam "¿Crees que te puedes ir a Aruba sin que tu novia quiera hacer algo especial antes de que os vayáis?"
            else:
                jam "¿Crees que te puedes ir a Aruba dejando a tu novia aquí sin que ella quiera hacer algo especial?"
        elif mc._var("relationships")==2:
            if ama._var("route") and bet._var("route"):
                jam "¿Crees que te puedes ir a Aruba sin que tus novias quieran hacer algo especial antes de que os vayáis?"
            elif ama._var("route") or bet._var("route"):
                jam "¿Crees que te puedes ir a Aruba sin que la novia que dejas aquí quiera hacer algo especial antes de que os vayáis?"
            else:
                jam "¿Crees que te puedes ir a Aruba dejando a todas tus novias aquí sin que ellas quieran hacer algo especial?"
        elif mc._var("relationships")==3:
            if ama._var("route") and bet._var("route"):
                jam "¿Crees que te puedes ir a Aruba sin que la novia que dejas aquí quiera hacer algo especial antes de que os vayáis?"
            else:
                jam "¿Crees que te puedes ir a Aruba sin que las novias que dejas aquí quieran hacer algo especial antes de que te vayas?"
        else:
            jam "¿Crees que te puedes ir a Aruba sin que las novias que dejas aquí quieran hacer algo especial antes de que te vayas?"
        mc "Bueno..."
    call BlinkXS4("c30s006_035a") from _call_BlinkXS4_1006
    if mc._var("relationships")>1:
        jam "Además, tú sabes lo difícil que debe ser para varias chicas ponerse de acuerdo en algo, ¿no?"
        mc "*Risa* Claro que lo sé. En lo único que se ponen de acuerdo es en mandarme a hacer cosas."
        stop music fadeout (1.5)
        mc "No es que me queje, claro. Adoro hacer cosas por ellas."
    else:
        if proposals==1:
            jam "Además, tu chica quería algo tangible y..."
        else:
            jam "Tu chica quiere algo tangible antes de que te vayas y..."
        mc "¿Me estás diciendo que ha comprado un anillo?"
        stop music fadeout (1.5)
        jam "No quiero estropear la sorpresa."
    play sound ("music/notification.ogg")
    "*Ding-Ding*"
    scene c30s006_025d with dissolve #mira el móvil
    jam "Bueno, parece que ya podemos empezar. Sígueme."
    if mc._var("relationships")>1:
        jam "Vamos a por la primera de las chicas."
    else:
        jam "Vamos a ver a tu chica."
    $ weddings = 0
    $ tattoo = False
    $ frase = False
    $ orangutan = False
    $ ScaWed = False
    $ EriWed = False
    $ EvaWed = False
    $ EmmWed = False
    $ LisWed = False
    $ DapWed = False
    $ KimWed = False
    $ OmaWed = False
    $ MegWed = False
    $ DebWed = False
    $ KatWed = False
    $ pendingWeddings = 0
    $ menuWedding = False
    if sca._var("route") and not ScaWed:
        $ pendingWeddings = pendingWeddings + 1
    if eri._var("route") and not EriWed:
        $ pendingWeddings = pendingWeddings + 1
    if eva._var("route") and not EvaWed:
        $ pendingWeddings = pendingWeddings + 1
    if emm._var("route") and not EmmWed:
        $ pendingWeddings = pendingWeddings + 1
    if lis._var("route") and not LisWed:
        $ pendingWeddings = pendingWeddings + 1
    if dap._var("route") and not DapWed:
        $ pendingWeddings = pendingWeddings + 1
    if kim._var("route") and not KimWed:
        $ pendingWeddings = pendingWeddings + 1
    if oma._var("route") and not OmaWed:
        $ pendingWeddings = pendingWeddings + 1
    if meg._var("route") and not MegWed:
        $ pendingWeddings = pendingWeddings + 1
    if mad._var("route"):
        call c30s006_mad from _call_c30s006_mad
    call check_relationships_c30 from _call_check_relationships_c30_1
    if kia._var("route"):
        call c30s006_kia from _call_c30s006_kia
    if sim._var("route"):
        call c30s006_sim from _call_c30s006_sim
    if kat._var("route"):
        call c30s006_kat from _call_c30s006_kat
    if sam._var("route"):
        call c30s006_sam from _call_c30s006_sam
    if deb._var("route"):
        call c30s006_deb from _call_c30s006_deb
        $ DebWed = True
    while pendingWeddings > 0:
        call menuwed from _call_menuwed
    if sai._var("route"):
        call c30s006_sai from _call_c30s006_sai
    if eil._var("route"):
        call c30s006_eil from _call_c30s006_eil
    if bet._var("route"):
        call c30s006_bet from _call_c30s006_bet
    if mee._var("route"):
        call c30s006_mee from _call_c30s006_mee
    if nor._var("route"):
        call c30s006_nor from _call_c30s006_nor
    if mar._var("route"):
        call c30s006_mar from _call_c30s006_mar
    if ama._var("route"):
        call c30s006_ama from _call_c30s006_ama
    return
label check_relationships_c30:
    $ mc._var("relationships", 0, "set")
    if sai._var("route"):
        $ mc._var("relationships", 1, "add")
    if mar._var("route"):
        $ mc._var("relationships", 1, "add")
    if emm._var("route"):
        $ mc._var("relationships", 1, "add")
    if eri._var("route"):
        $ mc._var("relationships", 1, "add")
    if nor._var("route"):
        $ mc._var("relationships", 1, "add")
    if dap._var("route"):
        $ mc._var("relationships", 1, "add")
    if sca._var("route"):
        $ mc._var("relationships", 1, "add")
    if eil._var("route"):
        $ mc._var("relationships", 1, "add")
    if sam._var("route"):
        $ mc._var("relationships", 1, "add")
    if sim._var("route"):
        $ mc._var("relationships", 1, "add")
    if oma._var("route"):
        $ mc._var("relationships", 1, "add")
    if eva._var("route"):
        $ mc._var("relationships", 1, "add")
    if mad._var("route"):
        $ mc._var("relationships", 1, "add")
    if meg._var("route"):
        $ mc._var("relationships", 1, "add")
    if ama._var("route"):
        $ mc._var("relationships", 1, "add")
    if mee._var("route"):
        $ mc._var("relationships", 1, "add")
    if kim._var("route"):
        $ mc._var("relationships", 1, "add")
    if kat._var("route"):
        $ mc._var("relationships", 1, "add")
    if deb._var("route"):
        $ mc._var("relationships", 1, "add")
    if lis._var("route"):
        $ mc._var("relationships", 1, "add")
    if bet._var("route"):
        $ mc._var("relationships", 1, "add")
    if kia._var("route"):
        $ mc._var("relationships", 1, "add")
    return
label menuwed:
    call BlinkXS4("c30s006_035b") from _call_BlinkXS4_1007
    if weddings == 0 and pendingWeddings > 1:
        jam "¿Por quién quieres empezar?"
        mc "¿De qué va esto, Jam?"
        jam "Tú tan solo dime un nombre."
    elif weddings>0 and pendingWeddings > 1:
        if pendingWeddings>1 and sam._var("route") and weddings>1 and not menuWedding:
            jam "Como antes te has puesto quisquilloso con el orden y ahora hay varias chicas preparadas, te voy a dejar elegir."
            mc "¡No me he puesto quisquilloso! ¡Solo he preguntado!"
            jam "*Risa* Soy el maestro de ceremonias. Si digo que te has puesto quisquilloso, es que te has puesto quisquilloso."
            $ menuWedding = True
        jam "¿A quién quieres ir a ver ahora?"
    if pendingWeddings > 1:
        menu:
            "[sca]" if sca._var("route") and not ScaWed:
                call c30s006_sca from _call_c30s006_sca
                $ pendingWeddings = pendingWeddings - 1
                $ ScaWed = True
            "[eri]" if eri._var("route") and not EriWed:
                call c30s006_eri from _call_c30s006_eri
                $ pendingWeddings = pendingWeddings - 1
                $ EriWed = True
            "[eva]" if eva._var("route") and not EvaWed:
                call c30s006_eva from _call_c30s006_eva
                $ pendingWeddings = pendingWeddings - 1
                $ EvaWed = True
            "[emm]" if emm._var("route") and not EmmWed:
                call c30s006_emm from _call_c30s006_emm
                $ pendingWeddings = pendingWeddings - 1
                $ EmmWed = True
            "[lis]" if lis._var("route") and not LisWed:
                call c30s006_lis from _call_c30s006_lis
                $ pendingWeddings = pendingWeddings - 1
                $ LisWed = True
            "[dap]" if dap._var("route") and not DapWed:
                call c30s006_dap from _call_c30s006_dap
                $ pendingWeddings = pendingWeddings - 1
                $ DapWed = True
            "[kim]" if kim._var("route") and not KimWed:
                call c30s006_kim from _call_c30s006_kim
                $ pendingWeddings = pendingWeddings - 1
                $ KimWed = True
            "[oma]" if oma._var("route") and not OmaWed:
                call c30s006_oma from _call_c30s006_oma
                $ pendingWeddings = pendingWeddings - 1
                $ OmaWed = True
            "[meg]" if meg._var("route") and not MegWed:
                call c30s006_meg from _call_c30s006_meg
                $ pendingWeddings = pendingWeddings - 1
                $ MegWed = True
    else:
        if mc._var("relationships")>1:
            if mar._var("route") or eil._var("route") or nor._var("route") or bet._var("route") or mee._var("route"):
                jam "Vamos a ver a la siguiente de las chicas. Te está esperando."
            else:
                if weddings>0:
                    jam "Vamos a ver a la última de tus chicas. Te está esperando."
        else:
            jam "Vamos a ver a tu chica. Te está esperando."
        if sca._var("route") and not ScaWed:
            call c30s006_lastWedding (sca, False) from _call_c30s006_lastWedding
            call c30s006_sca from _call_c30s006_sca_1
            $ ScaWed = True
        if eri._var("route") and not EriWed:
            call c30s006_lastWedding (eri, False) from _call_c30s006_lastWedding_1
            call c30s006_eri from _call_c30s006_eri_1
            $ EriWed = True
        if eva._var("route") and not EvaWed:
            call c30s006_lastWedding (eva, False) from _call_c30s006_lastWedding_2
            call c30s006_eva from _call_c30s006_eva_1
            $ EvaWed = True
        if emm._var("route") and not EmmWed:
            call c30s006_lastWedding (emm, False) from _call_c30s006_lastWedding_3
            call c30s006_emm from _call_c30s006_emm_1
            $ EmmWed = True
        if lis._var("route") and not LisWed:
            call c30s006_lastWedding (lis, False) from _call_c30s006_lastWedding_4
            call c30s006_lis from _call_c30s006_lis_1
            $ LisWed = True
        if dap._var("route") and not DapWed:
            call c30s006_lastWedding (dap, False) from _call_c30s006_lastWedding_5
            call c30s006_dap from _call_c30s006_dap_1
            $ DapWed = True
        if kim._var("route") and not KimWed:
            call c30s006_lastWedding (kim, False) from _call_c30s006_lastWedding_6
            call c30s006_kim from _call_c30s006_kim_1
            $ KimWed = True
        if oma._var("route") and not OmaWed:
            call c30s006_lastWedding (oma, False) from _call_c30s006_lastWedding_7
            call c30s006_oma from _call_c30s006_oma_1
            $ OmaWed = True
        if meg._var("route") and not MegWed:
            call c30s006_lastWedding (meg, False) from _call_c30s006_lastWedding_8
            call c30s006_meg from _call_c30s006_meg_1
            $ MegWed = True
        $ pendingWeddings = pendingWeddings - 1
    return
label c30s006_lastWedding (personaje, nick):
    if nick:
        jam "Sígueme. Nos toca ir a ver a [personaje.nick]."
    else:
        jam "Sígueme. Nos toca ir a ver a [personaje]."
    return
label c30s006_firstWedding (personaje):
    jam "Ve a hablar con ella. Tiene algo que decirte. Yo te esperaré aquí."
    jam "Mi madre me ha dicho que no me cocinará postres durante un mes si me inmiscuyo."
    mc "*Risa* Tu madre te tiene pillado por los huevos con la comida."
    if personaje!=sim and personaje!=sam:
        mc "Te veo en un rato."
    return
label c30s006_approach (personaje, nick):
    if nick:
        $ nombre=personaje.nick
    else:
        $ nombre=personaje.name.first_name
    "Te acercas a [nombre] con un nudo en el estómago. No sabes qué esperar."
    if personaje != kim:
        mc "Hola, [nombre]. Estás preciosa. Alguien me ha dicho que quieres hablar conmigo."
    elif personaje = kim:
        mc "Hola, [nombre]. Alguien me ha dicho que quieres hablar conmigo."
    elif personaje = mee:
        mc "Hola, Meemaw. Estás preciosa. Alguien me ha dicho que quieres hablar conmigo."
    if personaje != ama:
        personaje "*Risa* ¿Te lo ha dicho un pajarito?"
        mc "*Risa* Un pájaro negro, grande y comilón. Un buitre carroñero."
    return
label c30s006_sentence (personaje):
    mc "¿Habéis ensayado esa frase? ¿La de 'con este tatuaje me declaro tu esposa'?"
    personaje "*Risa* Sí. No queríamos hacer unos votos eternos o que los votos de una chica eclipsaran a los de otra."
    personaje "Sabemos que se te hará repetitivo, pero... Tuvimos que llegar a un acuerdo."
    mc "Me parece una idea fantástica."
    $ frase = True
    return
label c30s006_tattoo (personaje):
    mc "No tengo ninguna queja sobre que te hayas hecho el tatuaje, pero... ¿qué hubiera pasado si no me gustaran?"
    if eri._var("route"):
        personaje "Sales con [eri], con lo que no hemos dudado ni por un momento que te desagradaran los tatuajes."
    else:
        personaje "Como tú has dicho varias veces, hay que aceptar a todo el mundo como es."
    personaje "Ahora te toca aceptarme a mí con un tatuaje."
    mc "Y los tatuajes son para siempre."
    return
label c30s006_BetMee (personaje):
    personaje "No se lo digas a ellas, pero creo que ahora mismo odio a Tía [bet] y a [mee]. *Risa*"
    mc "Me lo puedo imaginar. A mí también me gustaría pasar más tiempo aquí contigo, pero..."
    if weddings>0:
        personaje "Pero esto es una fiesta para ellas. Aunque nos hayamos inmiscuido un poco antes de que empiece."
        "Crees que recordarás este día por razones diferentes a la bienvenida de [mee] y [bet]."
    else:
        personaje "Pero esto es una fiesta para ellas. Aunque me haya inmiscuido un poco antes de que empiece."
        "Crees que recordarás este día por una razón diferente a la bienvenida de [mee] y [bet]."
    return
label c30s006_orangutan (personaje):
    mc "Pero no acabo de entender por qué un tatuaje."
    personaje "Hay varias respuestas. La primera es que un tatuaje no se puede perder. Se puede quitar, pero... me entiendes."
    if mc._var("relationships") > 1:
        personaje "Después, nunca nos podríamos poner de acuerdo en qué modelo de anillo queremos. Lo que significa que deberías llevar un anillo diferente por cada chica."
        personaje "Si sigues añadiendo chicas al harén, acabarías arrastrando los brazos como un orangután, debido al peso de los anillos."
        personaje "Y, además, cada una de nosotras podíamos personalizarlo para que significara algo único."
    else:
        personaje "Un anillo podría servir para una boda... oficial. Un tatuaje nos hace únicos hasta cierto punto."
        personaje "Además, no creo que pudiera encontrar un anillo que simbolizara lo que este tatuaje significa para nosotros."
    mc "Lo entiendo."
    $ orangutan = True
    return
label c30s006_mad:
    scene c30s006_040e with fade
    play music ("music/pianomatic.ogg")
    "Sigues a Jamaal hasta la piscina, donde [mad.nick] está esperándote."
    call BlinkXS4("c30s006_045") from _call_BlinkXS4_1008
    call c30s006_firstWedding (mad) from _call_c30s006_firstWedding
    scene c30s006_040d with fade:
        yalign 1.0
        linear 5.0 yalign 0.0
    pause (4.8)
    if not _in_replay:
        $ mad.profileImages.insert (15, ("mad_15", None))
    call addProfileImageS3 (15, "mad_15", mad, __(": 15 - Especial"), "a") from _call_addProfileImageS3_26
    call BlinkXS3("c30s006_040") from _call_BlinkXS3_935
    call c30s006_approach (mad, True) from _call_c30s006_approach
    call BlinkXS4("c30s006_050") from _call_BlinkXS4_1009
    if mc._var("relationships")>1:
        mad "Estoy nerviosa. Me ha tocado ser la primera..."
        mad "Dicen que fue idea mía..."
    else:
        mad "Estoy nerviosa..."
    mc "Aún no sé de qué va esto, con lo que no sé por qué lo estás. Pero yo empiezo a ponerme nervioso si nos vemos y no me das un beso."
    scene c30s006_050d with dissolve
    "La chica te besa apasionadamente durante unos segundos que se hacen cortos."
    "Su cuerpo se va relajando tal como pasa el tiempo."
    "En algún sitio leíste que un beso debe durar 20 segundos como mínimo para liberar toda la oxitocina. ¿O eso eran los abrazos?"
    call BlinkXS4("c30s006_055") from _call_BlinkXS4_1010
    mc "¿Menos nerviosa?"
    mad "Un poco..."
    mc "Bueno, querías hablar conmigo, ¿no?"
    call BlinkXS4("c30s006_060") from _call_BlinkXS4_1011
    if kia._var("route"):
        mad "Bueno, todo empezó cuando le pediste matrimonio a [kia] y después me lo pediste a mí con aquel post-it..."
    else:
        mad "Bueno, todo empezó cuando me pediste matrimonio con aquel post-it."
    mc "Y descubrimos que tienes un fetiche con el matrimonio. *Risa*"
    mad "Sí..."
    call BlinkXS4("c30s006_065") from _call_BlinkXS4_1012
    mad "No sé si te has fijado, pero casi nunca llevo anillos."
    mc "Me había fijado. Yo tampoco los llevo, pero por un anillo de boda sería capaz de cambiar la costumbre."
    if mc._var("relationships")>1:
        call BlinkXS4("c30s006_070") from _call_BlinkXS4_1013
        mad "¿Un anillo por cada chica? ¿El anillo de qué chica va en el dedo anular?"
        mad "Seríamos incapaces de ponernos de acuerdo en un modelo de anillo para que tú sólo llevaras uno."
        mc "Eso podría ser complicado. Cada una querría algo a su gusto."
    call BlinkXS4("c30s006_075") from _call_BlinkXS4_1014
    mad "Pero tu post-it resolvió ese problema. Me dio una idea."
    if mc._var("relationships")>1:
        mad "Cada una de nosotras podía tener su anillo personalizado a su gusto. Con algo que significara algo para ella."
    mad "No necesitamos un anillo físico para demostrar que estamos juntos."
    stop music fadeout (1.0)
    mc "No entiendo a qué te refieres."
    scene c30s006_075d with dissolve
    play sound ("music/wedding-march-music-box.ogg")
    mad "[mc] Marks, con este anillo me declaro tu esposa. Si quieres, claro."
    mc "¡Por supuesto que quiero!"
    scene c30s006_050d with dissolve
    "Tu nueva esposa se gira y te besa más apasionadamente todavía que antes."
    "Ya no hay nervios. Solo alegría. Ahora entiendes por qué nadie te ha dicho de qué iba esto."
    "El beso es aún más largo que el anterior. Pese a todo se te hace corto."
    scene c30s006_080a with fade
    call BlinkXS4("c30s006_080") from _call_BlinkXS4_1015
    stop sound
    play music ("music/Rise-Up.ogg")
    mc "¿Te has tatuado el dibujo que hice en el post-it?"
    if mc._var("relationships")>1:
        mad "Al hacer el dibujo del anillo resolviste el tema del anillo personalizado."
        mad "Significó tanto para mí que no quiero ningún otro anillo."
        mc "¿Cada una de vosotras se ha tatuado un anillo?"
        call BlinkXS4("c30s006_085") from _call_BlinkXS4_1016
        mad "Eso lo tendrás que descubrir tú solo. La parte mala del harén es que no podemos disfrutar de este momento mucho rato."
        if mc._var("relationships")==2:
            mad "Hay otra chica esperándote y Jamaal tiene que estar impacientándose."
        else:
            mad "Hay otras chicas esperándote y Jamaal tiene que estar impacientándose."
        mc "*Risa* Odio al buitre carroñero."
    else:
        mad "Al hacer el dibujo del anillo resolviste el tema de no llevar anillos que pueda perder."
        mad "Significó tanto para mí que no quiero ningún otro anillo."
        mc "Los anillos son incómodos y este seguro que no lo puedes perder. Esto es más... definitivo."
        call BlinkXS4("c30s006_085") from _call_BlinkXS4_1017
        mad "Pero ahora deberíamos ir a ver a [mee] y a Tía [bet]. Estoy segura de que quieren darnos la enhorabuena."
    mc "No vamos a poder tener un momento para nosotros, ¿verdad?"
    call BlinkXS4("c30s006_090a") from _call_BlinkXS4_1018
    mad "Por desgracia, no. Pero espero que lo tengamos antes de que te vayas a Aruba."
    mc "Por cierto, ¿me voy a tener que tatuar yo también el anillo?"
    call BlinkXS4("c30s006_090b") from _call_BlinkXS4_1019
    mad "*Risa* No, cielo. Me gusta tu cuerpo como está, sin tatuajes."
    call c30s006_tattoo (mad) from _call_c30s006_tattoo
    scene c30s006_050d with dissolve
    "Os volvéis a besar, igual de apasionadamente que las dos veces anteriores, pero a la vez más tranquilos."
    "Besar a tu nueva esposa produce un calor en tu interior que te recorre todo el cuerpo."
    scene black with dissolve
    "Os separáis reluctantemente."
    if mc._var("relationships")>1:
        "Hay un buitre carroñero que te está esperando."
    else:
        "[mee] y Tía [bet] os están esperando." id c30s006_mad_81b6f66c
    $ weddings = weddings + 1
    stop music fadeout (1.5)
    return
label c30s006_kia:
    scene c30s006_095e with fade
    if mad._var("route"):
        "La siguiente parada es [kia], después de que Jamaal te haga dar una vuelta a la casa."
        play music ("music/pianomatic.ogg")
    else:
        "Jamaal te acompaña hasta donde está [kia]."
        play music ("music/pianomatic.ogg")
        call c30s006_firstWedding (kia) from _call_c30s006_firstWedding_1
    scene c30s006_095d with fade:
        yalign 1.0
        linear 5.0 yalign 0.0
    pause (4.8)
    call BlinkXS3("c30s006_095") from _call_BlinkXS3_936
    if not _in_replay:
        $ kia.profileImages.insert (15, ("kia_15", None))
    call addProfileImageS3 (15, "kia_15", kia, __(": 15 - Especial"), "") from _call_addProfileImageS3_27
    if weddings > 0:
        $ relaciones = mc._var("relationships")
        "Te acercas a [kia] imaginando lo que te espera. ¿Se han tatuado todas un anillo?"
        mc "Hola, [kia]. Estás guapísima. Supongo que hay un tatuaje que debo ver."
        kia "*Risa* Supongo que ser la segunda tiene la desventaja de que ya no te sorprende."
        if mc._var("relationships")!=2:
            kia "Y supongo que cuando llegues a la número [relaciones] se te hará todo repetitivo."
        else:
            kia "Aunque ser la última tiene algunas ventajas."
        call BlinkXS4("c30s006_105") from _call_BlinkXS4_1020
        kia "Por raro que te parezca, no quiero llevar tu anillo en el dedo."
        kia "El que hiciste tiene la mala costumbre de desmontarse y no lo quiero perder."
        mc "Ya te dije que compraríamos un anillo nuevo, pero supongo que el tatuaje lo resuelve."
        call BlinkXS4("c30s006_110") from _call_BlinkXS4_1021
        kia "Lo sé, pero además... Tendría que llevarlo en el mismo dedo que he llevado el de Solomon todos estos años."
        kia "Y no quiero que lo nuestro tenga ninguna relación con él."
        mc "Y [mad.nick] resolvió el problema cuando se le ocurrió la idea, ¿no?"
        call BlinkXS4("c30s006_115") from _call_BlinkXS4_1022
        stop music fadeout (1.0)
        kia "Exacto..."
    else:
        call c30s006_approach (kia, False) from _call_c30s006_approach_1
        call BlinkXS4("c30s006_100") from _call_BlinkXS4_1023
        kia "Bueno, todo esto lo empezaste tú en aquel mirador, mientras mirábamos la puesta de sol."
        mc "¿Te refieres al anillo? No me digas que has comprado uno."
        call BlinkXS4("c30s006_105") from _call_BlinkXS4_1024
        kia "Por raro que te parezca, no quiero llevar tu anillo en el dedo."
        kia "El que hiciste tiene la mala costumbre de desmontarse y no lo quiero perder."
        mc "Ya te dije que compraríamos un anillo nuevo."
        call BlinkXS4("c30s006_110") from _call_BlinkXS4_1025
        kia "Lo sé, pero... Tendría que llevarlo en el mismo dedo que he llevado el de Solomon todos estos años."
        kia "Y no quiero que lo nuestro tenga ninguna relación con él."
        mc "Lo entiendo. ¿Qué propones, entonces?"
        call BlinkXS4("c30s006_115") from _call_BlinkXS4_1026
        stop music fadeout (1.0)
        kia "Algo más definitivo. Algo que nunca pueda perder."
    scene c30s006_115d with dissolve
    play sound ("music/wedding-march-music-box.ogg")
    kia "Con este anillo declaro que soy tu esposa. Ahora y para siempre."
    if weddings==0:
        mc "¿Qué? ¿Te has tatuado el anillo que te hice?"
    else:
        mc "Me encanta que te hayas tatuado el anillo que te hice."
    call BlinkXS4("c30s006_120") from _call_BlinkXS4_1027
    kia "*Risa* Era eso o tatuarme un corcho. Preferí el anillo."
    scene c30s006_120d with dissolve
    "Ninguno de los dos necesitáis decir nada más. Vuestros labios se juntan en un beso increíblemente tierno."
    "Durante la fiesta de cumpleaños te explicó su historia aquí mismo y te quedaste con ganas de besarla..."
    "Hoy os dais vuestro primer beso como marido y mujer."
    stop sound
    play music ("music/Rise-Up.ogg")
    if weddings==0:
        call BlinkXS4("c30s006_125") from _call_BlinkXS4_1028
        call c30s006_tattoo(kia) from _call_c30s006_tattoo_1
    $ weddings = weddings + 1
    call BlinkXS4("c30s006_130") from _call_BlinkXS4_1029
    kia "Quisiera que te quedaras conmigo toda la tarde y toda la noche, pero..."
    if mc._var("relationships")>weddings:
        mc "Lo sé, Jamaal me está esperando para llevarme al siguiente tatuaje, ¿verdad?"
    else:
        mc "Lo sé, a mí también me gustaría, pero esto era teóricamente una fiesta para Tía [bet] y Meemaw, ¿verdad?"
    kia "Sí. Tendremos tiempo para nosotros luego. Aunque te tenga que compartir con el resto de las chicas."
    kia "Resérvame un baile."
    stop music fadeout (1.0)
    if mc._var("relationships")>weddings:
        mc "Te veo luego, preciosa."
    else:
        mc "¿Vamos?"
    return
label c30s006_sim:
    scene c30s006_135e with fade
    play music ("music/pianomatic.ogg")
    if weddings > 0:
        "La siguiente parada es [sim], después de la vuelta obligada a la casa para que la siguiente chica se ponga en la posición que ha elegido."
        "Obviamente, está al lado de la piscina."
    else:
        "Jamaal te acompaña hasta donde está [sim]."
        call c30s006_firstWedding (sim) from _call_c30s006_firstWedding_2
    call BlinkXS4("c30s006_140") from _call_BlinkXS4_1030
    jam "Es mi hermana. Trátala bien, por favor."
    mc "¿Alguna vez la he tratado mal?... Bueno, mejor no contestes. Pero de eso hace muchos años."
    mc "Además, parece que estar con Anthony te está reblandeciendo. *Risa* ¿Ahora te preocupas por [sim]?"
    scene c30s006_135e with dissolve
    "Te giras hacia [sim] sin darle tiempo a responder."
    jam "*Risa* Aún no sé por qué soy tu amigo. ¡Capullo!"
    scene c30s006_135d with fade:
        yalign 1.0
        linear 5.0 yalign 0.0
    pause (4.8)
    call BlinkXS3("c30s006_135") from _call_BlinkXS3_937
    if not _in_replay:
        $ sim.profileImages.insert (15, ("sim_15", None))
    call addProfileImageS3 (15, "sim_15", sim, __(": 15 - Especial"), "") from _call_addProfileImageS3_28
    if weddings > 0:
        mc "Hola, [sim]. No sé cómo haces para estar cada día más guapa."
        sim "Gracias. Tú también estás muy guapo con ese traje."
        mc "Supongo que hay un tatuaje que debo ver, ¿no?"
        mc "Aunque en nuestro caso no hubo anillo, con lo que va a ser una sorpresa."
        call BlinkXS4("c30s006_145") from _call_BlinkXS4_1031
        sim "Cuando surgió la idea de los tatuajes quería algo que nos representara, que fuera solo nuestro."
        sim "Pero hemos pasado tantos años juntos que no hay una sola cosa que destaque por encima del resto, con lo que he ido a lo clásico."
        mc "Lo clásico siempre es una buena elección."
        call BlinkXS4("c30s006_150") from _call_BlinkXS4_1032
        sim "También quería algo que durase para siempre. *Risa* No te vas a escapar de mí tan fácilmente. Con lo que el tatuaje era una opción genial."
    else:
        call c30s006_approach (sim, False) from _call_c30s006_approach_2
        call BlinkXS4("c30s006_145") from _call_BlinkXS4_1033
        sim "El otro día, en tu habitación, te pedí matrimonio. Y dijiste que sí."
        mc "Nunca podría haber rechazado una propuesta como esa, [sim]."
        sim "Pero no tenía un anillo que darte."
        mc "No es necesario un anillo entre nosotros, [sim]."
        call BlinkXS4("c30s006_150") from _call_BlinkXS4_1034
        sim "Quería algo que durase para siempre. *Risa* No te vas a escapar de mí tan fácilmente."
    stop music fadeout (1.0)
    mc "*Risa* No tengo intención de escapar."
    scene c30s006_150d with dissolve
    play sound ("music/wedding-march-music-box.ogg")
    sim "[mc], con este anillo me declaro tu esposa."
    if weddings==0:
        mc "¿Qué? ¿Te has tatuado un anillo de boda?"
    mc "Es un tatuaje precioso. Muy clásico, como nosotros. El tipo que sale con la hermana de su mejor amigo y..."
    sim "Y ella se acaba tatuando un anillo. *Risa* En vez del clásico anillo he hecho una cadena; cada eslabón es un paso que nos ha traído hasta aquí."
    call BlinkXS4("c30s006_155") from _call_BlinkXS4_1035
    mc "Veo muchos eslabones... ¿Tantos pasos hemos dado?"
    sim "Así seguro que dura para siempre. Tenemos que darle un significado a cada eslabón."
    scene c30s006_155d with dissolve
    "Besas a tu nueva esposa por primera vez. En pocos días ha pasado de amiga a novia, a prometida, y a esposa."
    "Una evolución natural y clásica, aunque rápida."
    "Como rápido, demasiado rápido, acaba vuestro beso."
    stop sound
    play music ("music/Rise-Up.ogg")
    if weddings==0:
        call BlinkXS4("c30s006_160") from _call_BlinkXS4_1036
        call c30s006_tattoo(sim) from _call_c30s006_tattoo_2
    else:
        call BlinkXS4("c30s006_160") from _call_BlinkXS4_1037
        call c30s006_sentence(sim) from _call_c30s006_sentence
    $ weddings = weddings + 1
    call BlinkXS4("c30s006_165") from _call_BlinkXS4_1038
    if mc._var("relationships")>weddings:
        sim "Sabes que odio a mi hermano ahora mismo, ¿verdad?"
        mc "*Risa* ¿Ahora mismo? Creo que lo has odiado siempre."
        call BlinkXS4("c30s006_170") from _call_BlinkXS4_1039
        sim "*Risa* Bueno, sí. Pero ahora lo odio más. Está allí haciéndome señas para que te envíe con él."
        sim "Creo que te tiene que llevar a algún otro sitio ahora mismo."
        mc "*Risa* Todos odiamos a Jamaal."
    else:
        call c30s006_BetMee(sim) from _call_c30s006_BetMee
    scene c30s006_155d with dissolve
    if mc._var("relationships")>weddings:
        "Vuelves a besar a tu esposa esta vez como despedida por un breve tiempo antes de volver con Jamaal."
    else:
        "Vuelves a besar a tu esposa esta vez como despedida por un breve tiempo antes de dirigirte a la fiesta."
    stop music fadeout (1.0)
    return
label c30s006_kat:
    scene c30s006_175e with fade
    if weddings > 0:
        "La siguiente chica es [kat]. Te está esperando donde tuvisteis la no-cita."
        play music ("music/pianomatic.ogg")
    else:
        "Jamaal te guía hasta donde [kat] te está esperando, donde tuvisteis la no-cita."
        play music ("music/pianomatic.ogg")
        call c30s006_firstWedding (kat) from _call_c30s006_firstWedding_3
    scene c30s006_175d with fade:
        yalign 1.0
        linear 5.0 yalign 0.0
    pause (4.8)
    call BlinkXS3("c30s006_175") from _call_BlinkXS3_938
    if not _in_replay:
        $ kat.profileImages.insert (15, ("kat_15", None))
    call addProfileImageS3 (15, "kat_15", kat, __(": 15 - Especial"), "") from _call_addProfileImageS3_29
    if weddings > 0:
        mc "Estás guapísima, [kat]. Tengo ganas de ver qué te has tatuado."
        kat "¿Quién te ha dicho que me haya hecho un tatuaje?"
        mc "¿No te lo has hecho? Me sorprendes, pequeña beluga."
        call BlinkXS4("c30s006_180") from _call_BlinkXS4_1040
        kat "*Risa* Sí que me lo he hecho. Pero te aseguro que yo no quería. Me parece ridículo declararme tu esposa después de sólo unos cuantos besos."
        mc "No tienes por qué hacerlo si no quieres."
        call BlinkXS4("c30s006_185a") from _call_BlinkXS4_1041
        kat "He dicho que me parece ridículo, no que no quiera hacerlo. Lo que no quería era hacerme un tatuaje."
        kat "Tú mismo lo has dicho. No sabes qué me he tatuado. No tenemos nada que nos defina, que sea sólo nuestro. Es demasiado pronto."
        if kat._var("waffle"):
            mc "Si yo tuviera que elegir, me hubiera tatuado un gofre, te pusiste monísima cuando te di un trozo del mío."
        else:
            mc "Si yo tuviera que elegir, me hubiera tatuado un gofre, ya sabes, por la no-cita... Amenazaste con robarme un trozo."
        mc "Eso sería solo nuestro."
    else:
        call c30s006_approach (kat, False) from _call_c30s006_approach_3
        call BlinkXS4("c30s006_180") from _call_BlinkXS4_1042
        kat "Quiero empezar diciendo que yo no quería hacer esto. Me parece ridículo después de sólo unos cuantos besos."
        if mc._var("relationships")>0:
            kat "Pero me han obligado a hacerlo..."
        else:
            kat "Pero no quería que te fueras a Aruba sin hacerlo..."
        mc "Sea lo que sea lo que vayas a hacer, no tienes por qué hacerlo si no quieres."
        call BlinkXS4("c30s006_185a") from _call_BlinkXS4_1043
        kat "No me refiero al hecho de hacerlo, sino a que todavía no tenemos nada que nos defina... Nada que lo veas y pienses en nosotros como pareja."
        if kat._var("waffle"):
            mc "Si yo tuviera que elegir, pensaría en un gofre, te pusiste monísima cuando te di un trozo del mío. O en una beluga..."
        else:
            mc "Si yo tuviera que elegir, pensaría en un gofre, ya sabes, por la no-cita... Te pusiste monísima cuando amenazaste con robarme un trozo. O en una beluga..."
        mc "Eso sería solo nuestro."
    call BlinkXS4("c30s006_185b") from _call_BlinkXS4_1044
    kat "*Risa* ¡Eres un capullo! Pero me gusta que empieces a conocerme."
    stop music fadeout (1.0)
    kat "Y ahora eres mi capullo."
    scene c30s006_185d with dissolve
    play sound ("music/wedding-march-music-box.ogg")
    kat "Con este gofre me declaro tu esposa."
    $ kat._var("engaged", True)
    mc "*Risa* ¿Me estás proponiendo matrimonio con un gofre?"
    call BlinkXS4("c30s006_190") from _call_BlinkXS4_1045
    kat "No. Te estoy diciendo que, te guste o no, estás casado conmigo. En vez de tarta de bodas podemos tener gofre de bodas."
    kat "Puedes besar a la novia."
    call BlinkXS4("c30s006_195") from _call_BlinkXS4_1046
    kat "Si aceptas... claro..."
    scene c30s006_195d with dissolve
    "Nunca se te pasaría por la cabeza no aceptar una propuesta así de una mujer tan maravillosa como [kat]."
    "Selláis vuestro futuro con un beso tan tierno como apasionado."
    "Nunca podrías haber imaginado que esto acabaría así cuando aquella chica con el pelo teñido de púrpura apareció en el aeropuerto."
    call BlinkXS4("c30s006_200") from _call_BlinkXS4_1047
    stop sound
    play music ("music/Rise-Up.ogg")
    mc "Por supuesto que acepto. Pedirme matrimonio... o declararte mi esposa... con un gofre es... demasiado dulce."
    kat "*Risa* ¡Por Dios! Me está entrando hambre sólo de pensarlo. Recuerda que como cuando me pongo nerviosa..."
    mc "No tienes que ponerte nerviosa por nada, cielo. Ahora eres mi esposa y eso no va a cambiar nunca."
    call BlinkXS4("c30s006_205") from _call_BlinkXS4_1048
    kat "Supongo que sería un poco difícil encontrar un juez que nos divorciara tal y como ha sido la boda, ¿no?"
    mc "No tengo ningún interés en buscar ese juez, con lo que nunca lo sabremos."
    if weddings == 0:
        call BlinkXS4("c30s006_210") from _call_BlinkXS4_1049
        call c30s006_tattoo(kat) from _call_c30s006_tattoo_3
    elif not frase:
        call BlinkXS4("c30s006_210") from _call_BlinkXS4_1050
        call c30s006_sentence (kat) from _call_c30s006_sentence_1
    call BlinkXS4("c30s006_215") from _call_BlinkXS4_1051
    mc "Ahora solo nos falta tener nuestra noche de bodas, ¿no?"
    kat "Habrá tiempo para eso, aunque no te voy a negar que estoy nerviosa por ello."
    mc "*Risa* No te preocupes, me ocuparé de que haya gofres al lado de la cama."
    call BlinkXS4("c30s006_220") from _call_BlinkXS4_1052
    kat "*Risa* Eres un capullo."
    mc "*Risa* No sé si eso dice algo bueno sobre ti. Te acabas de casar conmigo."
    $ weddings = weddings + 1
    call BlinkXS4("c30s006_225") from _call_BlinkXS4_1053
    if mc._var("relationships")>weddings:
        kat "Pero no soy la última chica que tienes que visitar hoy, con lo que el gofre al lado de la cama tendrá que esperar."
        mc "Eso significa que me tengo que ir con Jamaal otra vez, ¿no?"
        kat "A menos que quieras que la siguiente chica venga a matarme, sí."
        scene c30s006_195d with dissolve
        "Vuelves a besar a [kat] antes de dirigirte hacia donde Jamaal te espera."
    else:
        kat "Pero tenemos que ir a ver a Tía [bet] y a [mee], con lo que el gofre al lado de la cama tendrá que esperar."
        mc "Eso significa que esto acaba aquí por ahora, ¿no?"
        kat "A menos que quieras que dos ancianas vengan a matarme, sí."
        call BlinkXS4("c30s006_230") from _call_BlinkXS4_1054
        call c30s006_BetMee(kat) from _call_c30s006_BetMee_1
        scene c30s006_195d with dissolve
        "Vuelves a besar a [kat] antes de dirigiros hacia donde está la fiesta."
    "Saber que [kat] ya está pensando en la noche de bodas es casi una sorpresa."
    stop music fadeout (1.5)
    "Aunque habiendo descubierto lo que tus besos en su cuello producen, la sorpresa es menor de lo que lo hubiera sido hace unos días."
    $ KatWed = True
    return
label c30s006_sam:
    scene c30s006_235e with dissolve
    "Jamaal te acompaña hasta donde está [sam]."
    play music ("music/pianomatic.ogg")
    call BlinkXS4("c30s006_240") from _call_BlinkXS4_1055
    jam "Es mi madre, con lo que te atropellaré si haces alguna tontería."
    if weddings > 0:
        mc "No te preocupes. No la voy a hacer."
        mc "Pero tengo una pregunta, ¿Hay algún orden en las chicas a las que me llevas?"
        call BlinkXS4("c30s006_245") from _call_BlinkXS4_1056
        jam "El orden lo decido yo en base a cuáles de ellas están listas cuando vuelves a mí."
        jam "Aunque hay alguna que ha pedido una posición concreta en la lista."
        call BlinkXS4("c30s006_250") from _call_BlinkXS4_1057
        if pendingWeddings > 1:
            jam "*Risa* Después de mi madre quizás te deje elegir la siguiente."
            jam "Te lo prometo. Si hay más de una chica preparada, claro."
        jam "*Risa* Te juro que a mi madre no la podía hacer esperar más."
        mc "Lo entiendo. Te castigaría sin pastelillos durante un par de semanas."
    else:
        mc "No te preocupes. No la voy a hacer, aunque no sepa de qué va esto."
        call BlinkXS4("c30s006_245") from _call_BlinkXS4_1058
        call c30s006_firstWedding (sam) from _call_c30s006_firstWedding_4
    scene c30s006_235d with fade:
        yalign 1.0
        linear 5.0 yalign 0.0
    pause (4.8)
    call BlinkXS3("c30s006_235") from _call_BlinkXS3_939
    if not _in_replay:
        $ sam.profileImages.insert (15, ("sam_15", None))
    call addProfileImageS3 (15, "sam_15", sam, __(": 15 - Especial"), "") from _call_addProfileImageS3_30
    mc "Estás guapísima, [sam.nick]."
    sam "Gracias, [mc]. La ocasión lo merecía."
    if weddings > 0:
        mc "Supongo que tengo que ver un tatuaje, ¿no?"
        call BlinkXS4("c30s006_255") from _call_BlinkXS4_1059
        sam "Supones bien. Aunque ha sido complicado elegir qué tatuarme. Te conozco de toda la vida."
        mc "Yo tampoco sabría qué elegir. Hemos pasado por tantas cosas juntos que..."
        call BlinkXS4("c30s006_260a") from _call_BlinkXS4_1060
        sam "Exacto. *Risa* Y tatuarme un bote de ungüento para tus moretones no me parecía bien."
        sam "Pese a que todo empezó entonces, tus moretones no son algo que quiera recordar."
        stop music fadeout (1.0)
        mc "*Risa* Totalmente comprensible. Sorpréndeme."
    else:
        call c30s006_approach (sam, True) from _call_c30s006_approach_4
        mc "¿De qué va esto [sam.nick]? ¿De qué quieres hablar conmigo?"
        call BlinkXS4("c30s006_255") from _call_BlinkXS4_1061
        sam "Sabes que te conozco de toda la vida..."
        mc "Lo sé..."
        call BlinkXS4("c30s006_260a") from _call_BlinkXS4_1062
        sam "*Risa* Vale, no era la forma correcta de empezar."
        sam "Me refiero a que hace muchos años que nos conocemos, pero que en las últimas semanas nuestra relación ha cambiado mucho."
        mc "Ha cambiado a mejor, diría yo."
        call BlinkXS4("c30s006_265a") from _call_BlinkXS4_1063
        sam "Sí. Es algo que no me podía haber imaginado, pero has traído una nueva... ilusión... a mi vida."
        if mc._var("relationships")==1:
            sam "Quería hacer algo antes de que te fueras a Aruba."
        else:
            sam "Las chicas del harén queríamos hacer algo antes de que te fueras a Aruba."
        mc "¿Te das cuenta de que estás dando rodeos sin decirme nada?"
        call BlinkXS4("c30s006_260b") from _call_BlinkXS4_1064
        sam "*Risa* ¡Eres muy impaciente!"
        stop music fadeout (1.0)
        mc "*Risa* No, soy curioso. Me tienes en ascuas con tanto rodeo."
    scene c30s006_260d with dissolve
    play sound ("music/wedding-march-music-box.ogg")
    sam "Con estos anillos me declaro tu prometida y tu esposa."
    $ sam._var("engaged", True)
    if weddings == 0:
        mc "¿Qué? ¡Me encanta! Aunque me hubiera gustado habértelo propuesto yo."
    else:
        mc "¿Dos anillos en vez de uno? ¡Me encanta! Aunque me hubiera gustado habértelo propuesto yo."
    call BlinkXS4("c30s006_265b") from _call_BlinkXS4_1065
    sam "Ya que no me pedías que fuera tu prometida, he tenido que dar el paso yo."
    if mar._var("route"):
        sam "Y una vez le dijiste a [mar] que era tu esposa, el siguiente paso estaba claro."
    mc "Me alegro de que hayas dado el paso. ¿Puedo besar a mi esposa?"
    scene c30s006_265d with dissolve
    "Los dos sabéis que es una pregunta retórica. Hace mucho que sellasteis vuestro destino."
    "El beso con [sam] sabe ligeramente diferente esta vez. Es la primera vez que la besas como esposa."
    "No solo sabe diferente. También sabe corto cuando vuestros labios empiezan a separarse. Pero eso es normal siempre que besas a [sam]."
    stop sound
    play music ("music/Rise-Up.ogg")
    if weddings==0:
        call BlinkXS4("c30s006_270") from _call_BlinkXS4_1066
        call c30s006_tattoo(sam) from _call_c30s006_tattoo_4
    elif not frase:
        call BlinkXS4("c30s006_270") from _call_BlinkXS4_1067
        call c30s006_sentence(sam) from _call_c30s006_sentence_2
    $ weddings = weddings + 1
    call BlinkXS4("c30s006_275") from _call_BlinkXS4_1068
    if mc._var("relationships")>weddings:
        sam "Sabes que nunca diré que odio a mi hijo, y por norma no lo hago, pero ahora mismo..."
        mc "*Risa* En este caso sólo es el mensajero."
        call BlinkXS4("c30s006_280") from _call_BlinkXS4_1069
        sam "*Risa* Lo sé. Y ni siquiera ha sido idea suya, con lo que no lo castigaré sin pastelillos."
        mc "Tu venganza puede ser muy dura cuando lleve a Anthony a casa y solo hagas pastelillos para él."
        sam "*Risa* ¡Eres cruel con mi hijo! Pero me gusta la idea..."
        mc "Bueno, por mucho que me cueste separarme de ti, creo que es el momento en que me tengo que ir."
    else:
        call c30s006_BetMee(sam) from _call_c30s006_BetMee_2
    scene c30s006_265d with dissolve
    "Os dais un último beso por el momento."
    stop music fadeout (1.5)
    if mc._var("relationships")>weddings:
        "Es más corto de lo que cualquiera de vosotros querríais. Ninguno de los dos queréis ver a Jamaal impaciente."
    else:
        "Es más corto de lo que cualquiera de vosotros querríais. Los dos sabéis que os están esperando para empezar la fiesta."
    return
label c30s006_eri:
    scene c30s006_285e with fade
    if weddings > 0:
        jam "Bueno, la siguiente chica es tu gótica favorita."
        play music ("music/pianomatic.ogg")
    else:
        "Jamaal te acompaña hasta donde está [eri]."
        play music ("music/pianomatic.ogg")
        call c30s006_firstWedding(eri) from _call_c30s006_first_wedding
    scene c30s006_285d with fade:
        yalign 1.0
        linear 5.0 yalign 0.0
    pause (4.8)
    call BlinkXS3("c30s006_285") from _call_BlinkXS3_940
    if not _in_replay:
        $ eri.profileImages.insert (15, ("eri_15", None))
    call addProfileImageS3 (15, "eri_15", eri, __(": 15 - Especial"), "") from _call_addProfileImageS3_31
    if weddings > 0:
        mc "Estás preciosa, [eri]. Y supongo que tengo un tatuaje que ver, ¿no?"
        eri "Me hubiera gustado ser la primera para ver tu cara de sorpresa. Así pierde un poco la gracia."
        mc "¿Puedo decir algo antes de que me enseñes el tatuaje?"
    else:
        call c30s006_approach(eri, False) from _call_c30s006_approach_5
        mc "¿Puedo decir algo antes de lo que me tengas que contar?"
    stop music fadeout (1.5)
    eri "Por supuesto."
    scene c30s006_290d with fade
    play sound ("music/wedding-march-music-box.ogg")
    mc "[eri] Marks, ¿quieres casarte conmigo?"
    $ eri._var("engaged", True)
    eri "¿Qué? ¿De dónde has sacado ese anillo?"
    mc "*Risa* Del bolsillo. Pero ¿vas a contestar?"
    eri "¡Por supuesto que sí!"
    scene c30s006_290e with fade
    "Te levantas y os fundís en un beso que transmite todo lo necesario en un momento como ese."
    "No es un beso de los que empiezan en los labios de la boca y acaban en otros labios. No es un beso sexual."
    stop sound fadeout (1.0)
    "Es un beso que transmite todo el amor que os tenéis."
    play music ("music/pianomatic.ogg")
    call BlinkXS4("c30s006_290") from _call_BlinkXS4_1070
    eri "¿Cuánto hace que tienes este anillo?"
    mc "Algo más de una semana. Pero no he encontrado la oportunidad de dártelo."
    mc "Te lo hubiera dado cuando fui a arreglar el enchufe, pero ese día no lo llevaba encima."
    mc "Desde entonces no ha salido de mi bolsillo, al menos cuando tengo bolsillos."
    scene c30s006_290f with dissolve
    eri "Es precioso. A juego con los pendientes y..."
    call BlinkXS4("c30s006_295") from _call_BlinkXS4_1071
    eri "*Risa*"
    stop music fadeout (1.0)
    mc "¿De qué te ríes?"
    if weddings > 0:
        mc "¿Te has tatuado los pendientes?"
    scene c30s006_295d with dissolve
    play sound ("music/wedding-march-music-box.ogg")
    eri "Con este trisquel me declaro tu esposa."
    eri "Iba a decir tu prometida y tu esposa, pero tú me has convertido en tu prometida con el anillo."
    if weddings > 0:
        mc "Creo que eres casi la única sobre la que podía adivinar qué te ibas a tatuar."
        mc "Aunque no sé cómo sabías que te iba a regalar ese anillo."
    else:
        mc "¿Qué? ¿Habías visto el anillo antes de hoy? ¡Me encanta!"
    call BlinkXS4("c30s006_300") from _call_BlinkXS4_1072
    stop sound
    play music ("music/Rise-Up.ogg")
    eri "No es exactamente igual. El trisquel es más pequeño en el tatuaje que en el anillo."
    eri "Pero cuando tuve que elegir un motivo para el tatuaje lo tuve claro. El trisquel representa la evolución y el cambio."
    eri "Tú me has cambiado. Y espero que de ahora en adelante evolucionemos juntos."
    mc "Es un tatuaje con mucho sentido. Algo con significado, como todos tus tatuajes."
    call BlinkXS4("c30s006_305") from _call_BlinkXS4_1073
    eri "Ese tatuaje es el único que sé que no me quitaré nunca. Quería que significara algo nuestro."
    eri "No solo es que sea igual que los pendientes. Es que nos representa a nosotros."
    mc "¿Puedo besar a mi esposa? He besado a mi prometida, pero no a mi esposa."
    scene c30s006_290e with fade
    "La chica se da cuenta de que está divagando sobre el tatuaje y decide acallar su boca presionando sus labios contra los tuyos."
    "Los dos sabíais que estabais destinados a esto desde aquel primer beso del que parece que hace tanto tiempo."
    "Este es vuestro primer beso como marido y mujer. Obviamente, no será el último."
    call BlinkXS4("c30s006_310") from _call_BlinkXS4_1074
    eri "No sé a ti, pero a mí este beso me ha sabido... diferente."
    mc "No he notado ninguna diferencia. Sabes que 'novia', 'prometida' o 'esposa' no dejan de ser etiquetas."
    mc "No ha cambiado en nada lo que siento por ti. Dudo que alguna vez cambie, excepto por quererte más cada día."
    if weddings==0 or not frase:
        mc "Por cierto..."
        call BlinkXS4("c30s006_315") from _call_BlinkXS4_1075
        if weddings==0:
            mc "No tengo ninguna queja sobre que te hayas hecho el tatuaje, pero... ¿qué hubiera pasado si no hubiera querido que te hicieras más?"
            eri "Mi piel, mi decisión. Me aceptaste con tatuajes y uno más no iba a cambiar nada."
            eri "Siempre y cuando no me tatuara el cuerpo entero, no creía que te importara."
            mc "No me importa. Al menos ese es nuestro. No tiene que ver con un pasado en que necesitabas que los tatuajes te apoyaran."
            mc "Ahora estoy yo aquí para apoyarte en lo que necesites."
        else:
            call c30s006_sentence (eri) from _call_c30s006_sentence_3
    $ weddings = weddings + 1
    call BlinkXS4("c30s006_320") from _call_BlinkXS4_1076
    if mc._var("relationships")>weddings:
        eri "Y ahora te vas a tener que ir. La siguiente chica te está esperando y no la quieres hacer esperar, ¿verdad?"
        mc "Por muy ansioso que esté por verla, me fastidia que nuestro tiempo acabe aquí."
        eri "Solo de momento, cielo. Venga, vete antes de que te tenga que volver a besar y tenga que venir Jamaal a buscarte."
    else:
        call c30s006_BetMee(eri) from _call_c30s006_BetMee_3
    stop music fadeout (1.0)
    return
label c30s006_emmText:
    call BlinkXS4("c30s006_345a") from _call_BlinkXS4_1077
    if persistent.family:
        emm "Sabemos que no nos podremos casar nunca oficialmente."
        if mc._var("relationships")>1:
            emm "Incluso aunque legalizaran la poligamia, no creo que nunca legalicen el incesto..."
        else:
            emm "No creo que legalicen nunca el incesto..."
    else:
        if mc._var("relationships")>1:
            emm "Sabemos que no nos podremos casar nunca oficialmente. Dudo que alguna vez legalicen la poligamia."
        else:
            emm "Quería hacer esto antes de que te fueras a Aruba..."
    return
label c30s006_emmMenu:
    menu:
        "Un anillo de boda de oro rosa.":
            mc "Supongo que sería adecuado para la situación..."
        "Una rosa rosa.":
            mc "Es la flor que te define, y como eres tan original, es posible que no te hayas tatuado un anillo."
        "Un jabalí rosa.":
            mc "Sería un recordatorio de nuestra noche en el bosque y del Ferrarini."
            mc "Como eres tan original, es posible que no te hayas tatuado un anillo."
    call BlinkXS4("c30s006_335") from _call_BlinkXS4_1078
    emm "¡Te odio!"
    mc "¿He acertado?"
    emm "No, pero ahora que lo has dicho, tu opción me gusta más que la que elegí yo."
    return
label c30s006_emm:
    scene c30s006_325e with fade
    "Jamaal te acompaña hasta donde está [emm]. Obviamente vestida de rosa."
    play music ("music/pianomatic.ogg")
    if weddings == 0:
        call c30s006_firstWedding(emm) from _call_c30s006_first_wedding_1
    scene c30s006_325d with fade:
        yalign 1.0
        linear 5.0 yalign 0.0
    pause (4.8)
    call BlinkXS3("c30s006_325") from _call_BlinkXS3_941
    if not _in_replay:
        $ emm.profileImages.insert (15, ("emm_15", None))
    call addProfileImageS3 (15, "emm_15", emm, __(": 15 - Especial"), "") from _call_addProfileImageS3_32
    if weddings > 0:
        mc "Me podía imaginar que tu vestido sería rosa."
        emm "¿Acaso hay otro color que valga la pena vestir?"
        mc "Estarías guapísima con cualquier otro color, [emm]."
        call BlinkXS4("c30s006_330") from _call_BlinkXS4_1079
        emm "Ahora te toca adivinar qué me he tatuado."
        mc "*Risa* ¡Eso es nuevo!"
        emm "Soy una chica original."
        call c30s006_emmMenu from _call_c30s006_emmMenu
        mc "*Risa* Bueno, estoy seguro de que tienes otro hombro en el que poder tatuártelo."
        call BlinkXS4("c30s006_340") from _call_BlinkXS4_1080
        emm "*Risa* ¿Y volver a pasar por el dolor del tatuaje? ¡Nunca!"
        emm "Además, cuando acabemos aquí ya estaremos casados, con lo que no necesitaré más tatuajes."
        mc "¿Dolió mucho?"
        call c30s006_emmText from _call_c30s006_emmText
        call BlinkXS4("c30s006_345b") from _call_BlinkXS4_1081
        emm "Con lo que sí. Dolió. Pero me parece un precio barato para sentirme casada contigo."
        stop music fadeout (1.0)
        mc "Eso es muy tierno, [emm]. Me encantaría ver ese tatuaje."
    else:
        call c30s006_approach (emm, False) from _call_c30s006_approach_6
        mc "¿Qué es lo que pasa?"
        call c30s006_emmText from _call_c30s006_emmText_1
        call BlinkXS4("c30s006_330") from _call_BlinkXS4_1082
        emm "Imagínate que me he hecho un tatuaje para demostrar que estamos casados, ¿qué crees que me tatuaría?"
        call c30s006_emmMenu from _call_c30s006_emmMenu_1
        stop music fadeout (1.0)
        mc "Pero si lo hicieras, me encantaría ver ese tatuaje."
    scene c30s006_345d with dissolve
    play sound ("music/wedding-march-music-box.ogg")
    emm "Con este tatuaje me declaro casada contigo."
    $ emm._var("engaged", True)
    mc "¿Qué? ¿Te has tatuado un corazón como si fuera el diamante de un anillo?"
    mc "¡Me encanta! Y, obviamente, el corazón es rosa."
    call BlinkXS4("c30s006_350") from _call_BlinkXS4_1083
    emm "Por eso te he dicho que tu opción me gustaba más que la mía. Ahora parece soso."
    stop sound
    mc "A mí me parece precioso, [emm]."
    call BlinkXS4("c30s006_355") from _call_BlinkXS4_1084
    play music ("music/Rise-Up.ogg")
    emm "Le pedí al tatuador si podía dibujar un grano de pimienta rosa en el medio del corazón..."
    emm "Ya sabes, para mostrar que en nuestra relación hay mucho amor, pero también una parte picante..."
    mc "*Risa* Sólo a ti se te podía haber ocurrido una idea como esa. Pero no hay ningún grano de pimienta."
    call BlinkXS4("c30s006_360") from _call_BlinkXS4_1085
    emm "*Risa* Le pedí que lo dibujara en papel primero y... parecía una mierda de oveja... Una mierda rosa."
    mc "*Risa* Entonces es mejor que no te lo hayas tatuado. En vez de 'amor y picante', se podría malinterpretar como 'el amor es una mierda'."
    emm "*Risa* Algo parecido pensé yo."
    mc "¿Puedo besar a mi esposa?"
    scene c30s006_360d with dissolve
    if persistent.family:
        "Besas a tu hermana, a tu prometida, a tu esposa."
    else:
        "Besas a tu prometida, a tu esposa, a la mujer a la que has considerado como una hermana durante años."
    if mc._var("relationships")>1:
        "No te sorprendería que el plan para hacer esto hubiera sido parcialmente suyo. Por una vez sus planes funcionan."
    else:
        "Te sorprende que el plan para hacer esto haya salido de su cabeza. Ha funcionado. No te sorprendería que el resto de las chicas le hayan ayudado."
    call BlinkXS4("c30s006_365") from _call_BlinkXS4_1086
    emm "¡Wow!"
    mc "¿Qué tal tu primer beso de casada?"
    emm "Me deja sin aliento igual que cualquier otro."
    emm "Creo que soy como tú y que las etiquetas no significan demasiado para mí. Aunque estoy contenta de ser tu esposa."
    mc "Yo también estoy contento de que lo seas, [emm]."
    mc "Pero tengo una pregunta. Lo de ayer con la lavadora... ¿tiene algo que ver con esto?"
    call BlinkXS4("c30s006_370") from _call_BlinkXS4_1087
    emm "*Risita* Quería mi último polvo de soltera. Y no podía quitarme la camiseta o verías el tatuaje, con lo que se me ocurrió lo de la lavadora."
    mc "*Risa* Por suerte ya tenías el tatuaje hecho, o corríamos el riesgo de que te tatuaras una lavadora."
    emm "*Risa* Sería complicado de explicarles a nuestros nietos por qué tengo una lavadora tatuada en el hombro."
    if weddings==0:
        call BlinkXS4("c30s006_375") from _call_BlinkXS4_1088
        call c30s006_tattoo (emm) from _call_c30s006_tattoo_5
    elif not frase:
        call BlinkXS4("c30s006_375") from _call_BlinkXS4_1089
        call c30s006_sentence (emm) from _call_c30s006_sentence_4
    $ weddings = weddings + 1
    call BlinkXS4("c30s006_380") from _call_BlinkXS4_1090
    if mc._var("relationships")>weddings:
        emm "Y, por mucho que me duela, te tengo que mandar con Jamaal otra vez."
        emm "Si te vuelvo a besar, creo que te llevaré a la sala de la colada."
        mc "Y no estaría bien hacer esperar a la siguiente chica, ¿no?"
        emm "No, no estaría bien hacer esperar a mi futura cuñada."
        if eva._var("route"):
            call BlinkXS4("c30s006_385") from _call_BlinkXS4_1091
            emm "*Risa* No me gustaría hacer esperar a [eva] y que después viniera a torturarme por la noche."
            if EvaWed:
                mc "*Risa* No te preocupes. Ya he hablado con ella."
                mc "Además, no te torturaría. Seguro que os poníais a contaros cómo ha ido vuestra 'boda'."
            else:
                mc "*Risa* Seguramente no te torturaría. Os pondríais a contaros cómo ha ido vuestra 'boda'."
            emm "*Risita* Lo sé."
        scene c30s006_360d with dissolve
        "Le das un beso a tu preciosa esposa antes de dirigirte a donde te espera Jamaal."
    else:
        call c30s006_BetMee (emm) from _call_c30s006_BetMee_4
        if weddings>1:
            call BlinkXS4("c30s006_385") from _call_BlinkXS4_1092
            emm "*Risa* Por cierto, te odio."
            mc "¿Qué? ¿Por qué? ¿Qué he hecho yo ahora?"
            emm "*Risa* Dejarme para la última."
            mc "Sabes que las comidas acaban con el postre, ¿no?"
            emm "*Risa* Vale. Ahora te odio un poco menos."
        scene c30s006_360d with dissolve
        "Le das un beso a tu preciosa esposa antes de dirigiros hacia la fiesta de bienvenida."
    stop music fadeout (1.0)
    return
label c30s006_debKiss:
    scene c30s006_395d with dissolve
    "La preciosa nadadora te da un tierno beso de agradecimiento."
    "Sabes que ya no necesita que la reafirmen en lo preciosa que es, pero sigue encantándole que lo hagas."
    "Y, con premios como este, dudas que alguna vez dejes de hacerlo."
    return
label c30s006_deb:
    scene c30s006_390e with fade
    "Jamaal te guía hacia dónde te está esperando la sirena residente."
    play music ("music/pianomatic.ogg")
    if weddings==0:
        call c30s006_firstWedding (deb) from _call_c30s006_first_wedding_2
    scene c30s006_390d with fade:
        yalign 1.0
        linear 5.0 yalign 0.0
    pause (4.8)
    call BlinkXS3("c30s006_390") from _call_BlinkXS3_942
    if not _in_replay:
        $ deb.profileImages.insert (15, ("deb_15", None))
    call addProfileImageS3 (15, "deb_15", deb, __(": 15 - Especial"), "a") from _call_addProfileImageS3_33
    if weddings > 0:
        mc "[deb.nick], creo que no podría estar con una mujer más preciosa ahora mismo."
        if weddings == 1:
            deb "*Risita* ¿Le has dicho lo mismo a la chica anterior?"
        else:
            deb "*Risita* ¿Les has dicho lo mismo a las chicas anteriores?"
        mc "No, eres la primera a quién se lo digo."
        call c30s006_debKiss from _call_c30s006_debKiss
        call BlinkXS4("c30s006_395") from _call_BlinkXS4_1093
        deb "Supongo que sabes lo que viene ahora, ¿no?"
        mc "Me vas a enseñar el tatuaje y vas a decir la frase que habéis pactado."
        deb "Y supongo que sabes lo que me he tatuado..."
        call BlinkXS4("c30s006_400") from _call_BlinkXS4_1094
        deb "*Risa* Si no lo sabes di que lo sabes. Me sentiría un poco tonta por ponerte en un apuro si no lo adivinas."
        mc "Podría dudar entre la piedra corazón y la flor del remolino. Pero me inclino por la piedra corazón."
        mc "Tiene un montón de simbolismo para nosotros y creo que refleja mejor el concepto de duradero."
        call BlinkXS4("c30s006_405") from _call_BlinkXS4_1095
        deb "Las flores se marchitan o se secan, quedando aplastadas entre las páginas de un libro."
        stop music fadeout (1.0)
        deb "No es eso lo que quiero para lo nuestro."
    else:
        call c30s006_approach (deb, True) from _call_c30s006_approach_7
        mc "No sé de qué va esto, pero estás preciosa."
        call c30s006_debKiss from _call_c30s006_debKiss_1
        call BlinkXS4("c30s006_395") from _call_BlinkXS4_1096
        if mc._var("relationships")>1:
            deb "Tus novias hemos decidido hacer esto antes de que te vayas a Aruba."
        else:
            deb "He querido hacer esto antes de que te vayas a Aruba."
        stop music fadeout (1.0)
        mc "¿Qué es 'esto', [deb.nick]? Me tienes en ascuas."
    scene c30s006_395e with dissolve
    play sound ("music/wedding-march-music-box.ogg")
    deb "Con esta piedra corazón, que tú encontraste para mí, me declaro tu esposa."
    $ deb._var("engaged", True)
    deb "Sé que no es un anillo o algo por el estilo, pero representa mucho más para mí."
    if weddings > 0:
        mc "Me encanta. Ciertamente es un 'para siempre', o al menos lo espero."
    else:
        mc "¿Qué? ¡Me encanta!"
        call BlinkXS4("c30s006_405") from _call_BlinkXS4_1097
        deb "Por un momento dudé entre la piedra corazón y la flor del remolino, pero la piedra me pareció más idónea."
        deb "Las flores se marchitan o se secan, quedando aplastadas entre las páginas de un libro."
        deb "No es eso lo que quiero para lo nuestro."
        mc "Creo que la piedra tiene mucho más simbolismo para nosotros y que refleja mejor el concepto de 'para siempre'."
    scene c30s006_395d with dissolve
    "Esta vez el beso es igual de tierno, pero refleja más seguridad."
    "Estás seguro de que [deb.nick] ha estado dudando sobre si la rechazarías en el último momento."
    "Su inseguridad, aunque innecesaria, forma parte de su encanto."
    stop sound
    play music ("music/Rise-Up.ogg")
    call BlinkXS4("c30s006_410") from _call_BlinkXS4_1098
    deb "Tengo que pedirte disculpas..."
    mc "¿Por qué? Ha sido muy bonito."
    deb "No por esto sino... ¿te acuerdas del otro día en la piscina?"
    mc "¿Cuando dijiste que no podías bañarte porque tenías un sangrado?"
    call BlinkXS4("c30s006_415") from _call_BlinkXS4_1099
    deb "Sí... Entre [dap] y [sca] te hicieron pensar que era... otro tipo de sangrado. Y yo no hice nada por evitarlo."
    mc "No hay como hablar del periodo para que los hombres nos callemos."
    mc "Era por el tatuaje, ¿no?"
    call BlinkXS4("c30s006_420") from _call_BlinkXS4_1100
    deb "Sí. Se me infectó un poco y saltó la costra. No mentimos, pero te hicimos pensar que..."
    mc "Lo entiendo. Si me hubierais dicho la verdad se habría fastidiado la sorpresa."
    mc "Pero no importa, yo he jugado a ese juego, a hacer creer algo sin decirlo, demasiadas veces como para ofenderme."
    if deb._var("pregnant"):
        scene c30s006_420d with dissolve
        $ deb._var("undiscoveredPregnancy", False)
        "[deb.nick] se inclina sobre ti, poniendo los labios a la altura de tu oído."
        deb "Además, durante nueve meses no voy a tener ese... otro tipo de sangrado."
        mc "¿Qué? ¿Estás embarazada? ¿Cómo? ¿Cuándo?"
        call BlinkXS4("c30s006_425") from _call_BlinkXS4_1101
        deb "¡Sí! El 'como' ya lo sabes. Pero si te refieres a cuándo lo he descubierto, fue cuando [ama] se llevó los tests."
        deb "No podíamos decirte que lo íbamos a hacer. ¿Estás decepcionado porque no lo hemos mirado juntos?"
        mc "¿Decepcionado? ¡Contentísimo con el resultado! ¿Y tú? ¿Estás contenta? Tu carrera como nadadora..."
        "Las palabras se atropellan al salir de tu boca. Quieres hacer demasiadas preguntas a la vez."
        call BlinkXS4("c30s006_430") from _call_BlinkXS4_1102
        deb "No te preocupes por mi carrera ahora. Sí. Estoy contenta. Mucho."
        deb "No sabía que sentiría si salía positivo o negativo. Mientras esperaba que el test pitara, descubrí que quería ver el positivo."
        mc "¿Puedo besar a mi esposa y a la madre de mis hijos?"
        scene c30s006_395d with dissolve
        "No hace falta que conteste. Al menos no con palabras."
        "El beso transmite felicidad, alivio, y una seguridad que [deb.nick] nunca antes había tenido."
        "Crees que va a ser una gran madre. Ya es una gran esposa."
    call BlinkXS4("c30s006_435") from _call_BlinkXS4_1103
    mc "No vamos a tener luna de miel..."
    if deb._var("pregnant"):
        mc "Ni vamos a poder celebrar lo del bebé como es debido..."
    deb "Habrá tiempo para eso y para todas las celebraciones que queramos. Recuerda, una piedra es para siempre."
    deb "Y espero ser una piedra para ti el resto de tu vida. Aunque eso suene fatal."
    mc "*Risa* Sabes que un diamante es un piedra, ¿verdad?"
    if weddings == 0 or not frase:
        call BlinkXS4("c30s006_440") from _call_BlinkXS4_1104
        mc "Por cierto..."
        if weddings == 0:
            call c30s006_tattoo(deb) from _call_c30s006_tattoo_6
        else:
            call c30s006_sentence(deb) from _call_c30s006_sentence_5
    $ weddings = weddings + 1
    call BlinkXS4("c30s006_445") from _call_BlinkXS4_1105
    if mc._var("relationships")>weddings:
        deb "Ahora deberías volver con Jam. Hay otra chica esperándote."
        mc "No me vais a dejar tiempo para disfrutar de esto, ¿verdad?"
        call BlinkXS4("c30s006_450") from _call_BlinkXS4_1106
        deb "*Risa* La culpa es tuya por tener un harén."
        mc "*Risa* Visto así..."
        deb "Y estoy muy feliz de pertenecer a ese harén. *Risita* Pese a que tenga algunas desventajas."
        mc "Te veo luego, preciosa."
        scene c30s006_395d with dissolve
        "Os dais un último beso de despedida momentánea. Como ha dicho [deb.nick], hay otra chica esperándote."
    else:
        call c30s006_BetMee(deb) from _call_c30s006_BetMee_5
        scene c30s006_395d with dissolve
        "Os dais un último beso de despedida momentánea. Tenéis que uniros a la fiesta de bienvenida."
    stop music fadeout (1.0)
    return
label c30s006_oma:
    scene c30s006_455e with fade
    "Jamaal te acompaña hasta las escaleras del jacuzzi de [nor]."
    "[oma] te está esperando arriba, haciéndote señas para que la sigas."
    play music ("music/pianomatic.ogg")
    if weddings==0:
        call c30s006_firstWedding (oma) from _call_c30s006_first_wedding_3
    scene c30s006_455d with fade:
        yalign 1.0
        linear 5.0 yalign 0.0
    pause (4.8)
    call BlinkXS3("c30s006_455") from _call_BlinkXS3_943
    if not _in_replay:
        $ oma.profileImages.insert (15, ("oma_15", None))
    call addProfileImageS3 (15, "oma_15", oma, __(": 15 - Especial"), "") from _call_addProfileImageS3_34
    if weddings == 0:
        call c30s006_approach (oma, False) from _call_c30s006_approach_8
    if weddings>0:
        mc "Hola, Agente. Vengo a poner una denuncia. Estar tan guapa debe ser un delito."
    else:
        mc "¿Puedo denunciarte? Estar tan guapa debe ser un delito."
    call BlinkXS4("c30s006_460") from _call_BlinkXS4_1107
    oma "*Risa* Eres idiota. Lo sabes, ¿verdad?"
    mc "*Risa* Lo que sé es que pasáis demasiado tiempo con [kia] y [eil]. Al final os olvidaréis de mi nombre y todas me llamaréis 'idiota'."
    call BlinkXS4("c30s006_465") from _call_BlinkXS4_1108
    oma "No estaría mal. Le podría preguntar a [emm], '¿has visto al idiota de mi marido?'"
    stop music fadeout (1.0)
    if weddings>0:
        mc "Lo cual nos lleva al tatuaje, ¿no? Tengo ganas de ver qué te has tatuado."
        scene c30s006_465d with dissolve
    else:
        mc "*Risa* ¿Tu marido? ¿Cuándo nos hemos casado?"
        scene c30s006_465d with dissolve
        oma "Ahora."
    play sound ("music/wedding-march-music-box.ogg")
    oma "Con este anillo me declaro tu esposa. Ahora y siempre."
    $ oma._var("engaged", True)
    oma "Además, en español la palabra 'esposa' es la misma para esposas con las que te casas y esposas con las que te arrestan."
    if weddings>0:
        mc "¡Me encanta! Pero... ¿un cangrejo?"
    else:
        mc "¿Qué? ¿Me estás pidiendo que me case contigo?"
        oma "No. Te estoy informando de que estás casado conmigo."
        mc "Pero ¿nos casamos con un cangrejo?"
    call BlinkXS4("c30s006_470") from _call_BlinkXS4_1109
    stop sound
    play music ("music/Rise-Up.ogg")
    oma "¿No te acuerdas?"
    mc "¿De que confundí Krav Maga con un cangrejo por como lo pronunciaste? Claro que sí."
    call BlinkXS4("c30s006_475") from _call_BlinkXS4_1110
    oma "Aquel día empezó todo entre nosotros. Es un día que no quiero olvidar nunca y creo que es una cosa única."
    if mc._var("relationships")>1:
        oma "Cuando empezamos a hablar del tatuaje, es en lo primero que pensé, con lo que seguí mi instinto. No se me ocurría nada mejor."
    else:
        oma "Cuando pensé en qué tatuaje quería hacerme, es lo primero que me vino a la cabeza, con lo que seguí mi instinto."
    mc "Me encanta el tatuaje y me encanta el simbolismo, pero ¿puedo besar a mi esposa ya?"
    scene c30s006_475d with dissolve
    "Os lanzáis el uno en los brazos del otro mientras vuestros labios se buscan y se encuentran."
    "Los dos queríais que este momento llegara algún día. Tú no podías imaginarte que llegaría así."
    "De alguna forma, los dos habíais elegido al otro para el resto de la vida, con lo que esto solo significa cambiar la etiqueta."
    "A veces no odias las etiquetas... demasiado."
    if weddings==0:
        call BlinkXS4("c30s006_480") from _call_BlinkXS4_1111
        call c30s006_tattoo(oma) from _call_c30s006_tattoo_7
    elif not frase:
        call BlinkXS4("c30s006_480") from _call_BlinkXS4_1112
        call c30s006_sentence(oma) from _call_c30s006_sentence_6
    $ weddings = weddings + 1
    call BlinkXS4("c30s006_485") from _call_BlinkXS4_1113
    mc "Sobre lo que has dicho del significado de 'esposa' en español..."
    oma "Sí..."
    mc "Creo que tiene mucho sentido. Voy a estar atado a ti de por vida..."
    call BlinkXS4("c30s006_490") from _call_BlinkXS4_1114
    oma "*Risa* Mas te vale. Soy católica y no nos divorciamos."
    oma "*Risa* Y si alguna vez intentas que rompamos, como haciendo comentarios tontos sobre estar atados, buscaré hasta la última multa de tráfico que tengas."
    mc "*Risa* No te preocupes. No lo intentaré."
    call BlinkXS4("c30s006_495") from _call_BlinkXS4_1115
    if mc._var("relationships")>weddings:
        oma "Pero ahora deberías irte. Hay otro tatuaje esperando a ser descubierto."
    else:
        call c30s006_BetMee(oma) from _call_c30s006_BetMee_6
    mc "¿Puedo tener un último beso para el camino?"
    scene c30s006_475d with dissolve
    "Os besáis de una forma que sabe a despedida."
    stop music fadeout (1.0)
    if mc._var("relationships")>weddings:
        "Ninguno de los dos queréis que la siguiente chica te espere demasiado."
    else:
        "Los dos sabéis que en cuanto os unáis a la fiesta, no vais a poder estar a solas."
    return
label c30s006_eva:
    scene c30s006_500e with fade
    "Jamaal te acompaña hasta el rincón de estar solo, donde [eva] te está esperando."
    play music ("music/EpicFemaleSolo.ogg")
    if weddings==0:
        call c30s006_firstWedding (eva) from _call_c30s006_first_wedding_4
    scene c30s006_500d with fade:
        yalign 1.0
        linear 5.0 yalign 0.0
    pause (4.8)
    call BlinkXS3("c30s006_500") from _call_BlinkXS3_944
    if not _in_replay:
        $ eva.profileImages.insert (15, ("eva_15", None))
    call addProfileImageS3 (15, "eva_15", eva, __(": 15 - Especial"), "") from _call_addProfileImageS3_35
    if weddings == 0:
        call c30s006_approach (eva , False) from _call_c30s006_approach_9
        call BlinkXS4("c30s006_505") from _call_BlinkXS4_1116
    mc "Ayer estábamos aquí mismo, pero las circunstancias parecen haber cambiado, ¿no?"
    eva "Un poco..."
    mc "¿Pasa algo, [eva]?"
    call BlinkXS4("c30s006_510") from _call_BlinkXS4_1117
    mc "Ayer estabas triste y hoy pareces enfadada."
    eva "Es lógico que esté enfadada."
    stop music fadeout (1.0)
    mc "Explícame por qué. No entiendo nada..."
    if weddings > 0:
        mc "¿No querías hacerte el tatuaje?"
    scene c30s006_510d with dissolve
    play sound ("music/wedding-march-music-box.ogg")
    eva "Mira. Con este estúpido tatuaje me declaro tu esposa."
    $ eva._var("engaged", True)
    if weddings == 0:
        mc "¿Qué? No lo entiendo. Ni por qué estás enfadada."
    else:
        mc "No entiendo por qué estás enfadada."
    mc "Y no entiendo por qué el tatuaje es estúpido. A mí me parece muy chulo."
    call BlinkXS4("c30s006_515") from _call_BlinkXS4_1118
    eva "Porque el tatuaje no tiene ningún sentido. Sólo lo tiene para mí."
    mc "Bueno... ¿tú eres la bala desgastada? Y... Yo soy el anillo que te... ¿abraza?... ¿No?"
    scene c30s006_515d with hpunch #abrazo
    eva "¡Lo has deducido! Más o menos... Y no es una bala. Es un cartucho. Voy a tener que seguir enseñándote."
    mc "Me da lo mismo como se llame... Bala o cartucho. Para mí se llama [eva] y no me voy a cansar de abrazarte."
    mc "¿Y estabas enfadada por eso? ¿Por si no pillaba el significado de un tatuaje?"
    stop sound
    play music ("music/Rise-Up.ogg")
    call BlinkXS4("c30s006_520") from _call_BlinkXS4_1119
    eva "No. Estoy enfadada porque me han dicho que solo tengo unos minutos para hacer esto contigo. Me hubiera gustado tener más tiempo, pero..."
    $ weddings = weddings + 1
    if mc._var("relationships") > weddings:
        eva "La siguiente chica ya está preparada y no la puedes hacer esperar."
    else:
        eva "Tía [bet] y [mee] ya nos estarán esperando." id c30s006_eva_97aa1882
        if weddings > 0:
            eva "Y me has dejado para la última. Aunque si hubiera sido la primera, sería otra chica la que estaría esperando en vez de ellas."
    mc "Pues saquemos el máximo provecho de esos minutos que tenemos."
    scene c30s006_520d with dissolve
    "Ya tienes a [eva] entre tus brazos, con lo que besas dulcemente a tu esposa."
    "Puedes notar con tus labios como una sonrisa va apareciendo en su boca, reemplazando definitivamente a la expresión enfadada."
    "Sí, [eva] es una mujer de muchos talentos y puede sonreír mientras besa."
    call BlinkXS4("c30s006_525") from _call_BlinkXS4_1120
    mc "¿Te parece una buena forma de aprovechar estos minutos?"
    eva "*Risita* La mejor. O casi..."
    mc "Supongo que ahora ya tengo la respuesta a por qué ibas con un traje de neopreno ayer."
    call BlinkXS4("c30s006_530") from _call_BlinkXS4_1121
    eva "Si hubiera llevado un bikini hubieras podido ver el tatuaje."
    if dap._var("route") and sca._var("route"):
        eva "Menos a [dap] y a [sca], creo que no nos has visto los hombros a ninguna de nosotras desde el sábado. Algunas desde antes."
    else:
        eva "Creo que no nos has visto los hombros a ninguna de nosotras desde el sábado. Algunas desde antes."
    if mc._var("relationships")<22:
        eva "Ni siquiera a las que no se han tatuado nada. Para que no sospecharas de las que lo hemos hecho."
    mc "¿Me vas a hacer daño si te digo que no me había dado cuenta? Bueno, excepto en tu caso, claro."
    call BlinkXS4("c30s006_535") from _call_BlinkXS4_1122
    eva "*Risa* No te voy a hacer daño porque te diste cuenta conmigo. Pero mejor no se lo digas al resto."
    mc "*Risa* Bueno, ahora tengo una esposa que me puede defender."
    scene c30s006_520d with dissolve
    "Os volvéis a besar. Esta vez no hay cambio de expresión en sus labios. La sonrisa va a estar permanentemente en su boca por mucho tiempo."
    "La alegría os recorre al mismo tiempo que vuestras lenguas recorren vuestras bocas."
    call BlinkXS4("c30s006_540") from _call_BlinkXS4_1123
    eva "Sigue siendo un buen modo de aprovechar los minutos que nos han dado."
    if mc._var("relationships")>weddings:
        eva "Pero deberías ir yéndote o no voy a poder defenderte de la siguiente chica."
    else:
        eva "Pero deberíamos ir a la fiesta antes de que Tía [bet] y [mee] se enfaden."
    mc "Antes de irnos quiero decirte una cosa."
    mc "Te prometo que tendremos más de cinco minutos para la renovación de votos."
    call BlinkXS4("c30s006_545") from _call_BlinkXS4_1124
    eva "¡Pero eso es dentro de 10 años!"
    mc "Podemos renovarlos cuando vengas a Aruba. Se me va a hacer muy largo no verte durante un mes. Casi como si pasaran 10 años."
    if weddings==1 or not frase:
        mc "Por cierto..."
        call BlinkXS4("c30s006_550") from _call_BlinkXS4_1125
        if weddings == 1:
            call c30s006_tattoo (eva) from _call_c30s006_tattoo_8
        else:
            call c30s006_sentence (eva) from _call_c30s006_sentence_7
    call BlinkXS4("c30s006_555") from _call_BlinkXS4_1126
    if mc._var("relationships")>weddings:
        eva "Deberías irte ya o te voy a besar hasta que Jamaal venga a buscarte."
    else:
        eva "Deberíamos irnos ya o te voy a besar hasta que vengan a buscarnos."
    eva "Y no sé si podría controlarme para que sólo fuera un beso..."
    mc "Entonces creo que será lo mejor."
    scene black with dissolve
    "En el momento en que te separas de [eva], tus brazos se sienten vacíos."
    stop music fadeout (1.0)
    "Has estado abrazándola desde que has deducido el significado del tatuaje y ahora te falta algo entre las manos."
    return
label c30s006_kim:
    scene c30s006_560e with fade
    "Jamaal te acompaña hasta la piscina, donde [kim] está radiante."
    play music ("music/pianomatic.ogg")
    if weddings==0:
        call c30s006_firstWedding (kim) from _call_c30s006_first_wedding_5
    scene c30s006_560d with fade:
        yalign 1.0
        linear 5.0 yalign 0.0
    pause (4.8)
    call BlinkXS3("c30s006_560") from _call_BlinkXS3_945
    if not _in_replay:
        $ kim.profileImages.insert (15, ("kim_15", None))
    call addProfileImageS3 (15, "kim_15", kim, __(": 15 - Especial"), "") from _call_addProfileImageS3_36
    if weddings == 0:
        call c30s006_approach (kim , False) from _call_c30s006_approach_10
        call BlinkXS4("c30s006_565") from _call_BlinkXS4_1127
        mc "¿Es importante? Jamaal ha sido muy misterioso."
        mc "Por cierto... Estás guapísima, [kim], pero supongo que no hace falta que te lo diga."
    else:
        mc "Estás guapísima, [kim], pero supongo que no hace falta que te lo diga."
    kim "Me gusta que me lo digas. Creo que no me cansaré nunca de oírtelo decir."
    if weddings == 0:
        kim "Y sí. Es importante, al menos para mí. Pero nada de lo que te tengas que preocupar demasiado..."
        mc "*Risa* Le estás poniendo aún más misterio."
        call BlinkXS4("c30s006_570") from _call_BlinkXS4_1128
        if mc._var("relationships")>1:
            kim "A ver cómo te lo explico... Las chicas hemos hablado y todas queremos que nuestras relaciones sigan adelante."
            kim "Tanto las individuales como el harén."
            kim "Y he decidido que no quiero seguir siendo tu novia."
            "No tiene demasiado sentido, pero la notas nerviosa por algo."
        else:
            kim "A ver cómo te lo explico... No quiero ser tu novia cuando te vayas a Aruba."
        mc "¿Estás rompiendo conmigo?"
        call BlinkXS4("c30s006_575") from _call_BlinkXS4_1129
        stop music fadeout (1.0)
        kim "*Risa* ¿Qué? ¡No! Sólo quiero decir que quiero ser algo más que tu novia."
    else:
        call BlinkXS4("c30s006_570") from _call_BlinkXS4_1130
        kim "Se pierde un poco la sorpresa no siendo la primera, ¿verdad?"
        mc "Bueno, depende de qué te hayas tatuado puede ser una sorpresa."
        call BlinkXS4("c30s006_575") from _call_BlinkXS4_1131
        kim "*Risa* ¡Tienes razón! ¿Qué crees que me he tatuado?"
        if not KatWed and not EmmWed and not DebWed:
            mc "La verdad es que no sé qué tipo de anillo podría reflejarnos a nosotros."
            mc "Si no fuera un anillo, supongo que algo referido a un mapa."
            if DebWed:
                mc "Si no fuera porque [deb.nick] ha roto la tendencia del anillo..."
            elif KatWed and EmmWed:
                mc "Si no fuera porque [emm] y [kat] han roto la tendencia del anillo..."
            elif KatWed:
                mc "Si no fuera porque [kat] ha roto la tendencia del anillo..."
            elif EmmWed:
                mc "Si no fuera porque [emm] ha roto la tendencia del anillo..."
            mc "No tendría ni idea de qué podrías haberte tatuado."
            mc "Una vez rota... supongo que algo referido a un mapa."
        stop music fadeout (1.0)
        mc "Un barco no. Eso seguro que nos traería recuerdos desagradables."
    scene c30s006_575d with dissolve
    play sound ("music/wedding-march-music-box.ogg")
    kim "Con esta brújula me declaro tu esposa. De esta forma no te perderás en el mapa de mi piel."
    $ kim._var("engaged", True)
    if weddings == 0:
        mc "¿Qué? ¿Mi esposa? ¡Me encanta! Y el tatuaje es... tan nuestro..."
    else:
        mc "¡Me encanta! Es... tan nuestro..."
    call BlinkXS4("c30s006_580") from _call_BlinkXS4_1132
    kim "*Hablando rápido* Querría haber dicho que, con la brújula, siempre encontrarías el camino de vuelta a mí, especialmente ahora que te vas..."
    kim "*Hablando rápido* Pero entonces la brújula la tendrías que tener tú y no tenerla yo tatuada en la piel, y..."
    mc "Siempre soy yo a quién acusáis de hablar demasiado, [kim]."
    scene c30s006_580d with dissolve
    "Besas a tu esposa por primera vez. O por primera vez desde que es tu esposa."
    "La chica torpe e insegura que bajó de aquel avión ha desaparecido, pero su encanto sigue intacto."
    "Y sus labios saben tan bien como siempre. A veces te preguntas por qué no la besaste antes."
    stop sound
    play music ("music/Rise-Up.ogg")
    call BlinkXS4("c30s006_585") from _call_BlinkXS4_1133
    kim "*Jadeo* Creo que voy a necesitar un momento para recuperar mi respiración..."
    mc "Todo el tiempo que necesites."
    kim "*Jadeo* Si pudiera tener todo el tiempo que necesito..."
    if weddings == 0 or not frase:
        call BlinkXS4("c30s006_590") from _call_BlinkXS4_1134
        if weddings == 0:
            call c30s006_tattoo (kim) from _call_c30s006_tattoo_9
        else:
            call c30s006_sentence (kim) from _call_c30s006_sentence_8
    if not orangutan:
        call BlinkXS4("c30s006_595") from _call_BlinkXS4_1135
        call c30s006_orangutan (kim) from _call_c30s006_orangutan
    call BlinkXS4("c30s006_600") from _call_BlinkXS4_1136
    $ weddings = weddings + 1
    if mc._var("relationships")>weddings:
        kim "Y ahora, aunque no quiera, deberías irte. Hay alguien más esperándote."
        mc "Lo sé. Yo tampoco quiero dejarte aquí sola. Me fastidia que algo tan importante como esto lo tengamos que hacer tan rápido."
        call BlinkXS4("c30s006_605") from _call_BlinkXS4_1137
        kim "*Risa* Si no fueras coleccionando novias..."
        mc "*Risa* Ahora parece que colecciono esposas."
    else:
        call c30s006_BetMee (kim) from _call_c30s006_BetMee_7
    scene c30s006_580d with dissolve
    "Vuelves a besar a la preciosa [kim]. Esta vez es un beso más calmado que el anterior, pero no menos tierno."
    if mc._var("relationships") > weddings:
        "Por un lado, no quieres volver con Jamaal. Por otro, quieres ver a la siguiente chica."
    else:
        "Por un lado, no quieres ir a la fiesta de bienvenida. Por otro, tienes ganas de ver a [mee] y a Tía [bet]."
    stop music fadeout (1.0)
    "El beso dura menos de lo que quisieras, antes de que os tengáis que separar."
    return
label c30s006_meg:
    scene c30s006_610e with fade
    if weddings==0:
        play music ("music/pianomatic.ogg")
        call c30s006_firstWedding (meg) from _call_c30s006_first_wedding_6
    else:
        play music ("music/pianomatic.ogg")
        "Jamaal te acompaña hasta la parte trasera de la casa de [nor], donde te está esperando [meg]."
    scene c30s006_610d with fade:
        yalign 1.0
        linear 5.0 yalign 0.0
    pause (4.8)
    call BlinkXS3("c30s006_610") from _call_BlinkXS3_946
    if not _in_replay:
        $ meg.profileImages.insert (15, ("meg_15", None))
    call addProfileImageS3 (15, "meg_15", meg, __(": 15 - Especial"), "") from _call_addProfileImageS3_37
    if weddings == 0:
        call c30s006_approach (meg , False) from _call_c30s006_approach_11
    else:
        mc "Estás guapísima, [meg]."
        meg "Tú también. Me encanta cómo te queda ese traje."
        mc "Y supongo que ahora me toca ver un tatuaje, ¿no?"
    call BlinkXS4("c30s006_615") from _call_BlinkXS4_1138
    meg "Esto se me hace muy raro. Nunca pensé que llegaríamos a esto."
    if weddings == 0:
        mc "Sigo sin saber qué es 'esto'."
    else:
        mc "A mí me parece de lo más natural. ¿O es que sólo querías algo casual conmigo?"
    call BlinkXS4("c30s006_620") from _call_BlinkXS4_1139
    meg "Cuando saliste de mi apartamento aquel día en Westport creí que esto sería algo casual. No pensé que estuvieras interesado en algo serio conmigo."
    mc "Pero..."
    call BlinkXS4("c30s006_625") from _call_BlinkXS4_1140
    meg "¡Hush! ¡Déjame hablar! He ensayado esto delante del espejo."
    mc "Vale. Mantendré la boca cerrada."
    call BlinkXS4("c30s006_630") from _call_BlinkXS4_1141
    meg "Nunca demostraste ningún interés por mí en Portland. Sí, ya sé que estabas con [sai]..."
    meg "Pero, pese a vuestra relación abierta, nunca te fijaste en mí..."
    call BlinkXS4("c30s006_635") from _call_BlinkXS4_1142
    meg "Pero aquel día me tiraste el café encima y... después mi mundo se hizo pedazos."
    meg "Nunca había sido tan feliz como desde que estoy contigo."
    meg "Me paso los días deseando que llegue el fin de semana para venir a Newport."
    call BlinkXS4("c30s006_640") from _call_BlinkXS4_1143
    meg "Y, por si fuera poco, me has dado una familia donde no esperaba encontrarla."
    stop music fadeout (1.0)
    meg "Por todo eso..."
    scene c30s006_640d with dissolve
    play sound ("music/wedding-march-music-box.ogg")
    meg "Con este anillo y esta taza, tan rota como mi mundo, me declaro tu esposa."
    $ meg._var("engaged", True)
    if weddings == 0:
        mc "¿Qué? ¡Estoy muy sorprendido! No sabía de qué iba esto..."
    mc "¡Me encanta! Estoy muy contento de ser tu marido."
    call BlinkXS4("c30s006_645") from _call_BlinkXS4_1144
    meg "¿No te parece una estupidez?"
    if weddings == 0:
        meg "¿O que me estoy imponiendo sin darte la oportunidad de rechazarme?"
    else:
        meg "¿O que nos estamos imponiendo sin darte la oportunidad de rechazarnos?"
    mc "[meg], me conoces bien. Sabes lo que haría si creyera que se me está imponiendo una decisión que no quiero tomar."
    mc "Y no sería esto."
    scene c30s006_645d with dissolve
    "La coges entre tus brazos y la besas con pasión, demostrándole que la decisión ya está tomada."
    "Y es la decisión correcta."
    "Le has demostrado cien veces que estás loco por ella y, pese a todo, su inseguridad muestra su fea cara de vez en cuando."
    "Tendrás que demostrárselo aún más veces. Mil veces. Un millón de veces. Mil besos o un millón. Nunca serán suficientes."
    stop sound
    play music ("music/Rise-Up.ogg")
    call BlinkXS4("c30s006_650") from _call_BlinkXS4_1145
    meg "Vale. Me ha quedado claro."
    meg "*Risa* Bueno. No. No lo tengo claro del todo. ¿Puedo tener otro beso para acabar de quitarme las dudas?"
    mc "*Risa* Puedes tener todos los besos que quieras, [meg]. Hay muchos esperando que vengas a buscarlos."
    scene c30s006_645d with dissolve
    "Ahora es ella la que busca tu boca con la suya."
    "Obviamente, las dudas ya no existen. Ahora tan solo sois dos adictos a la boca del otro disfrutando vuestra dosis."
    "Es una adicción tan grande, que el síndrome de abstinencia empezará en el momento en que separéis vuestros labios."
    if weddings == 0 or not frase:
        call BlinkXS4("c30s006_655") from _call_BlinkXS4_1146
        if weddings == 0:
            call c30s006_tattoo (meg) from _call_c30s006_tattoo_10
        else:
            call c30s006_sentence (meg) from _call_c30s006_sentence_9
    $ weddings = weddings + 1
    if not orangutan:
        call BlinkXS4("c30s006_660a") from _call_BlinkXS4_1147
        call c30s006_orangutan (meg) from _call_c30s006_orangutan_1
    call BlinkXS4("c30s006_660b") from _call_BlinkXS4_1148
    if mc._var("relationships")>weddings:
        meg "Me podría pasar horas besándote, pero entonces me convertiría en la chica más odiada de la casa."
        mc "Y no queremos eso, ¿verdad?"
        meg "Ni eso ni que Jamaal venga a decirnos que la cena se va a retrasar por nuestra culpa."
        mc "*Risa* ¡Puñetero comilón!"
        call BlinkXS4("c30s006_665") from _call_BlinkXS4_1149
        meg "Ve con él. Seguro que se está impacientando por llevarte con la siguiente chica."
        mc "Te veo en un rato, cielo."
    else:
        call c30s006_BetMee (meg) from _call_c30s006_BetMee_8
    stop music fadeout (1.0)
    return
label c30s006_lis:
    scene c30s006_670e with fade
    "Vas con Jamaal hasta un lateral de la casa de [nor], donde [lis] te está esperando."
    play music ("music/pianomatic.ogg")
    "Nunca habías visto a [lis] en esta zona del jardín. Tú tampoco vienes mucho."
    if weddings == 0:
        call c30s006_firstWedding (lis) from _call_c30s006_first_wedding_7
    scene c30s006_670d with fade:
        yalign 1.0
        linear 5.0 yalign 0.0
    pause (4.8)
    call BlinkXS3("c30s006_670") from _call_BlinkXS3_947
    if not _in_replay:
        $ lis.profileImages.insert (15, ("lis_15", None))
    call addProfileImageS3 (15, "lis_15", lis, __(": 15 - Especial"), "") from _call_addProfileImageS3_38
    if weddings > 0:
        mc "Estás preciosa, [lis]. Aunque eso no es ninguna novedad."
        lis "Gracias, [mc]. Eso le sube la autoestima a cualquier chica."
        mc "Tengo ganas de ver qué te has tatuado. No creía que fueras una chica dada a hacerte tatuajes."
        call BlinkXS4("c30s006_675") from _call_BlinkXS4_1150
        lis "No me han gustado nunca, pero, cuando hablamos de ello entre nosotras, creí que, si alguna vez me hacía un tatuaje, esta sería la mejor razón."
        lis "Hoy es un día para cosas nuevas. Por eso he elegido esta parte del jardín. Nunca había venido aquí."
    else:
        call c30s006_approach (lis, False) from _call_c30s006_approach_12
        call BlinkXS4("c30s006_675") from _call_BlinkXS4_1151
        if mc._var("relationships")>1:
            lis "Me ha tocado ser la primera, con lo que te lo voy a tener que explicar desde el principio."
            lis "Sabemos que no podremos casarnos contigo nunca, pero queremos hacerlo de alguna forma, aunque no sea oficial."
            if mar._var("route"):
                lis "Tal como hiciste con [mar]."
            lis "Mi vida cambió el día que me besaste en mi habitación, y quiero que continúe cambiando."
        else:
            lis "Sé que es muy pronto para hablar de casarnos, pero sé que quiero pasar el resto de mi vida contigo."
            lis "El resto de mi vida empezó el día que me besaste en mi habitación, y quiero que continúe así."
        mc "Me parece una idea estupenda. Y estabas monísima con aquel pijama de vaca."
        call BlinkXS4("c30s006_680a") from _call_BlinkXS4_1152
        lis "Hoy es un día para cosas nuevas. Por eso he elegido esta parte del jardín. Nunca había venido aquí."
        lis "Si vamos a crear recuerdos nuevos juntos, este es un lugar perfecto, donde no se entremezclarán con otros recuerdos."
    stop music fadeout (1.0)
    mc "Siempre me ha parecido la parte más anodina del jardín de [nor], pero creo que hoy cambiará eso."
    scene c30s006_675d with dissolve
    play sound ("music/wedding-march-music-box.ogg")
    lis "Con este anillo me declaro tu esposa. *Risa* Más te vale no rechazarme. Como te dije en la fiesta, tengo amigas que saben cómo enterrar un cadáver."
    $ lis._var("engaged", True)
    lis "*Risa* Y supongo que la amenaza de pasar la eternidad en una bolsa rosa con un lazo es suficiente para no hacerlo."
    if weddings==0:
        mc "¿Qué? ¿Me estás pidiendo que me case contigo?"
        lis "*Risa* No, te estoy informando de que estás casado."
    mc "No te rechazaría aunque no me hubieras amenazado. Puede que esté loco, pero eso sería demasiada locura incluso para mí."
    stop sound
    play music ("music/Rise-Up.ogg")
    call BlinkXS4("c30s006_680b") from _call_BlinkXS4_1153
    lis "Sabes que ahora tienes una cuñada y unos suegros, ¿no? Yo también vengo con una familia en la mochila."
    if deb._var("route"):
        mc "*Risa* Hasta hace un momento mi cuñada eras tú."
    else:
        mc "*Risa* Supongo que [deb.nick] estará esperando que vayas a decirle cómo ha ido esto."
    mc "Y sobre mis suegros... Me impone un poco conocerlos por lo que me habéis explicado."
    call BlinkXS4("c30s006_685") from _call_BlinkXS4_1154
    lis "No te preocupes por eso. Al menos hasta que vuelvas de Aruba. Habrá tiempo cuando vuelvas..."
    if lis._var("pregnant"):
        lis "Estaré embarazada de seis meses por entonces, con lo que se lo tendré que decir antes..."
        mc "¿Qué? ¿Estás embarazada?"
        $ lis._var("undiscoveredPregnancy", False)
    scene c30s006_675e with dissolve #beso
    "Rodeas a tu nueva esposa entre tus brazos y la besas con pasión."
    if lis._var("pregnant"):
        "No te importa demasiado cómo son sus padres ni cómo te recibirán. Lo importante es que vuestro bebé está creciendo dentro de ella."
    else:
        "No te importa demasiado cómo son sus padres ni cómo te recibirán. Lo importante es que [lis] sea feliz."
    "El beso dura demasiado poco, pero transmite lo que los dos sentís. Que este es un nuevo inicio para los dos."
    call BlinkXS4("c30s006_700") from _call_BlinkXS4_1155
    mc "Te quiero, por cierto."
    lis "*Risa* Yo también, pero ese 'por cierto' al final de la frase..."
    mc "*Risa* ¿No te ha gustado?"
    call BlinkXS4("c30s006_705") from _call_BlinkXS4_1156
    lis "Me ha encantado. Es tan... tú..."
    mc "Como supongo que el tatuaje es parte de ti. Sólo he visto un anillo, pero no sé si tiene algún significado extra."
    call BlinkXS4("c30s006_710") from _call_BlinkXS4_1157
    lis "Esperaba que no me lo preguntaras... Lo elegí en un impulso y..."
    mc "No tienes por qué explicármelo si no quieres."
    lis "No quiero tener secretos con mi marido, con lo que allá va. Espero que no pienses que soy demasiado... tonta."
    call BlinkXS4("c30s006_715") from _call_BlinkXS4_1158
    lis "Quería un anillo de boda, pero no el típico anillo de boda, liso."
    lis "Sabes que puedo ser... rugosa... a veces. Y sé que algún día me pondré borde y diré algo que no debo..."
    lis "Con el anillo, rugoso por fuera y liso por dentro, quería representar que nuestra relación va a tener baches, pero que por dentro va a ser maravillosa."
    mc "¿Y por eso tenía que pensar que eres tonta?"
    mc "Me parece que has pensado mucho el significado de ese tatuaje. Eso es lo contrario de ser tonta para mí."
    call BlinkXS4("c30s006_690") from _call_BlinkXS4_1159
    mc "Y hablando de joyería... Se me hace raro verte vestida así, pero sin pendientes o algún collar."
    lis "*Risa* La joya que quería llevar, la llevo tatuada en la espalda."
    lis "Y no quería que nada le quitara protagonismo ni al tatuaje ni a este maravilloso vestido."
    mc "Pero los brazaletes..."
    call BlinkXS4("c30s006_695") from _call_BlinkXS4_1160
    lis "Los brazaletes venían con el vestido... Si el diseñador los ha hecho para que vayan juntos..."
    mc "*Risa* Y no podías resistirte a usarlos, ¿verdad?"
    call BlinkXS4("c30s006_690") from _call_BlinkXS4_1161
    lis "*Risa* Por supuesto que no."
    if weddings == 0 or not frase:
        call BlinkXS4("c30s006_720") from _call_BlinkXS4_1162
        if weddings == 0:
            call c30s006_tattoo (lis) from _call_c30s006_tattoo_11
        else:
            call c30s006_sentence (lis) from _call_c30s006_sentence_10
    $ weddings = weddings + 1
    if not orangutan:
        call BlinkXS4("c30s006_725") from _call_BlinkXS4_1163
        call c30s006_orangutan (lis) from _call_c30s006_orangutan_2
    call BlinkXS4("c30s006_730") from _call_BlinkXS4_1164
    if mc._var("relationships")>weddings:
        lis "No se lo digas a Jamaal, pero ahora mismo lo odio un poquito."
        mc "*Risa* Bueno, estás en tu derecho a hacerlo. Ahora es realmente tu cuñado."
        mc "Pero sé a lo que te refieres. No queremos que se inmiscuya en nuestros nuevos recuerdos apareciendo para venir a buscarme."
    else:
        call c30s006_BetMee(lis) from _call_c30s006_BetMee_9
    scene c30s006_675e with dissolve #beso
    "Vuelves a rodear entre tus brazos a tu esposa y le das un tierno beso."
    stop music fadeout (1.0)
    if mc._var("relationships")>weddings:
        "Es una despedida momentánea, hasta que os podáis reunir de nuevo en la fiesta."
    else:
        "Es una despedida momentánea. No habrá más besos hasta que lleguéis a la fiesta. Si os paráis cada dos metros a besaros, no llegaréis nunca."
    return
label c30s006_scaSpa:
    mc "No sé por qué deberías sorprenderte. Sabes que es lo que pienso."
    call BlinkXS4("c30s006_740a") from _call_BlinkXS4_1165
    sca "Lo sé, pero después de tantos años esperando a que te fijaras en mí... Parece raro que ahora estemos aquí."
    mc "Bueno, muchas cosas han cambiado desde entonces. Ahora vives aquí y estamos juntos."
    mc "Aún me acuerdo del día que viniste a esta casa para quedarte definitivamente."
    call BlinkXS4("c30s006_745") from _call_BlinkXS4_1166
    sca "Por eso he elegido este lugar. Fue donde todas las chicas me dieron la bienvenida... Bueno, más bien delante del garaje..."
    sca "Es un lugar que evoca recuerdos felices, y quiero añadir uno más a la colección de recuerdos."
    return
label c30s006_sca:
    scene c30s006_735e with fade
    "Jamaal te acompaña hasta la valla de la casa de [nor], donde [sca] te está esperando."
    play music ("music/pianomatic.ogg")
    if weddings == 0:
        call c30s006_firstWedding (sca) from _call_c30s006_first_wedding_8
    scene c30s006_735d with fade:
        yalign 1.0
        linear 5.0 yalign 0.0
    pause (4.8)
    call BlinkXS3("c30s006_735") from _call_BlinkXS3_948
    if not _in_replay:
        $ sca.profileImages.insert (15, ("sca_15", None))
    call addProfileImageS3 (15, "sca_15", sca, __(": 15 - Especial"), "") from _call_addProfileImageS3_39
    if weddings > 0:
        mc "Estás guapísima, [sca]."
        call BlinkXS4("c30s006_740b") from _call_BlinkXS4_1167
        sca "¿Sabes que aún me sorprendo cuando me lo dices?"
        call c30s006_scaSpa from _call_c30s006_scaSpa
        mc "*Risa* Ahora solo falta que me digas que te has tatuado un plato de espaguetis."
        call BlinkXS4("c30s006_750") from _call_BlinkXS4_1168
        sca "Lo pensé, pero... sigo considerando aquellos espaguetis un fracaso."
        mc "*Risa* ¿Como comida o como material de construcción?"
        call BlinkXS4("c30s006_755") from _call_BlinkXS4_1169
        stop music fadeout (1.0)
        sca "Pero es el momento de crear más recuerdos felices."
    else:
        call c30s006_approach (sca, False) from _call_c30s006_approach_13
        call BlinkXS4("c30s006_740b") from _call_BlinkXS4_1170
        sca "¿Sabes que aún me sorprendo cuando me dices que estoy guapa?"
        call c30s006_scaSpa from _call_c30s006_scaSpa_1
        mc "*Risa* Y puedes usar el recuerdo de los espaguetis para cimentarlo todo."
        call BlinkXS4("c30s006_750") from _call_BlinkXS4_1171
        sca "Sigo considerando aquellos espaguetis un fracaso..."
        mc "*Risa* ¿Como comida o como material de construcción? Mejor no contestes."
        mc "Pero aún no me has dicho qué hacemos aquí."
        call BlinkXS4("c30s006_755") from _call_BlinkXS4_1172
        stop music fadeout (1.0)
        sca "Crear más recuerdos felices."
    scene c30s006_755d with dissolve
    play sound ("music/wedding-march-music-box.ogg")
    sca "Con este anillo me declaro tu esposa. Siempre lo he querido ser y..."
    $ sca._var("engaged", True)
    if persistent.family and mc._var("edmundsStory"):
        sca "Sabemos que no nos vamos a poder casar nunca por ser medio-hermanos..."
    elif mc._var("relationships")>1:
        sca "Sabemos que no nos vamos a poder casar nunca porque no quiero ser la única con la que te cases..."
    else:
        sca "Nunca te he preguntado si quieres casarte oficialmente en el futuro..."
    if weddings==0:
        mc "¿Qué? ¡Me parece una idea increíble!"
    scene c30s006_755e with dissolve #beso
    "No tienes nada que añadir. Sabes que, después de tanto tiempo enamorada de ti, dar este paso es muy importante para [sca]."
    "Vuestro primer beso como marido y mujer es espectacular. Atrás quedaron las lecciones sobre besos."
    "Hoy no eres un maestro orgulloso, sino un marido feliz."
    call BlinkXS4("c30s006_760") from _call_BlinkXS4_1173
    stop sound
    play music ("music/Rise-Up.ogg")
    sca "Espero que nunca pares de dejarme sin respiración con cada beso."
    mc "Yo también lo espero. Pero ahora eres una gran besadora. Tú también me dejas sin respiración a mí."
    mc "El anillo es precioso. ¿De dónde sacaste la idea?"
    call BlinkXS4("c30s006_765") from _call_BlinkXS4_1174
    sca "Es una mezcla de los dibujos de Escher, de mis múltiples planes para acabar aquí, y... de los espaguetis. *Risita*"
    mc "*Risa* Sabía que esos espaguetis estarían con nosotros para siempre."
    call BlinkXS4("c30s006_770") from _call_BlinkXS4_1175
    sca "Aquel día hablaste sobre nietos por primera vez."
    sca "No voy a llevar un plato de espaguetis tatuado en el hombro, pero esto me recordará las partes bonitas de aquella noche."
    scene c30s006_775An with dissolve
    "Dices 'Te quiero' en lengua de signos. Sabes perfectamente a qué se refiere con lo de las partes bonitas."
    "Has aprendido a decir más cosas en lengua de signos desde entonces, pero guardas la sorpresa para otro momento."
    call BlinkXS4("c30s006_780") from _call_BlinkXS4_1176
    sca "Yo también te quiero, [mc]."
    "No hay lágrimas como la primera vez. Tan solo una sonrisa radiante que adoras."
    scene c30s006_755e with dissolve #beso
    "Os volvéis a besar. Es un beso que se repetirá el resto de vuestras vidas."
    "Tierno y lleno de amor. No necesitáis nada más."
    if weddings == 0 or not frase:
        call BlinkXS4("c30s006_785") from _call_BlinkXS4_1177
        if weddings == 0:
            call c30s006_tattoo (sca) from _call_c30s006_tattoo_12
        else:
            call c30s006_sentence (sca) from _call_c30s006_sentence_11
    $ weddings = weddings + 1
    if not orangutan:
        call BlinkXS4("c30s006_790") from _call_BlinkXS4_1178
        call c30s006_orangutan (sca) from _call_c30s006_orangutan_3
    call BlinkXS4("c30s006_795") from _call_BlinkXS4_1179
    if mc._var("relationships")>weddings:
        mc "Creo que odio a Jamaal. Seguro que ha sido idea suya organizar esto y que sólo tengamos unos minutos juntos."
        sca "Bueno, más o menos. Nosotras propusimos más tiempo, pero Jamaal dijo que se haría muy tarde para la fiesta."
        sca "[meg] y [sam.nick] tienen que ir a trabajar y..."
        mc "Y será mejor que me empiece a ir, ¿no?"
        sca "*Risa* Y será mejor que yo no conteste a eso."
    else:
        call c30s006_BetMee(sca) from _call_c30s006_BetMee_10
    stop music fadeout (1.0)
    return
label c30s006_dap:
    scene black with dissolve
    "Acompañas a Jamaal por el jardín. Dais una vuelta a la casa de [nor], como si estuviera haciendo tiempo."
    play music ("music/pianomatic.ogg")
    "Una sonrisa pícara se dibuja en su cara durante todo el recorrido."
    scene c30s006_800e with fade
    "Finalmente te acompaña hasta donde está [dap]."
    if weddings == 0:
        call c30s006_firstWedding (dap) from _call_c30s006_first_wedding_9
    scene c30s006_800d with fade:
        yalign 1.0
        linear 5.0 yalign 0.0
    pause (4.8)
    call BlinkXS3("c30s006_800") from _call_BlinkXS3_949
    if not _in_replay:
        $ dap.profileImages.insert (15, ("dap_15", None))
    call addProfileImageS3 (15, "dap_15", dap, __(": 15 - Especial"), "") from _call_addProfileImageS3_40
    if weddings > 0:
        mc "No sé si es más espectacular el vestido o tu sonrisa, [dap]"
    else:
        call c30s006_approach (dap, False) from _call_c30s006_approach_14
        mc "Lo digo en serio. No sé si es más espectacular el vestido o tu sonrisa, [dap]"
    call BlinkXS4("c30s006_805") from _call_BlinkXS4_1180
    dap "Bueno, esto creo que se me va a dar muy mal..."
    mc "No sé de nada que se te dé especialmente mal, si exceptuamos las habilidades sociales, y has mejorado mucho en eso."
    dap "Esto forma parte de las habilidades sociales. Y esta en particular no la he entrenado."
    call BlinkXS4("c30s006_810") from _call_BlinkXS4_1181
    dap "Sabes que la noche en el hotel medieval fue la mejor noche de mi vida, ¿no?"
    mc "Fue una noche fantástica."
    dap "Y sé que no la podré olvidar nunca. Por eso he querido hacer esto de esta forma."
    stop music fadeout (1.0)
    mc "No lo entiendo. No veo nada de medieval en el vestido."
    scene c30s006_810d with dissolve
    play sound ("music/wedding-march-music-box.ogg")
    dap "No es el vestido sino el anillo. Con este anillo me declaro tu esposa. Si aceptas, claro."
    $ dap._var("engaged", True)
    if weddings==0:
        mc "¿Qué? ¿Mi esposa?"
    mc "Por supuesto que acepto. Tan solo espero que no haya un noble cerca que quiera tener su derecho a Prima Nocta."
    call BlinkXS4("c30s006_815") from _call_BlinkXS4_1182
    dap "Bueno, eso realmente no existía... o solo en raras ocasiones. Los historiadores todavía no se han encontrado pruebas sobre..."
    scene c30s006_815d with dissolve #beso
    "No quieres una clase de historia. Quieres besar a tu esposa."
    "Pobre del noble, real o ficticio, que quiera arrancártela de tus brazos."
    "El beso es tan alucinante como la mujer cuya boca recorre tu lengua."
    call BlinkXS4("c30s006_820") from _call_BlinkXS4_1183
    stop sound
    play music ("music/Rise-Up.ogg")
    dap "... si eso pasaba, o solo son leyendas o malas interpretaciones de documentos históricos."
    mc "*Risa* Tenías que acabar la frase, ¿verdad?"
    dap "Por supuesto. *Risa* Sabes que no me gusta que me interrumpan cuando estoy hablando de algo que me apasiona."
    mc "*Risa* ¿Ni siquiera con un beso?"
    call BlinkXS4("c30s006_825") from _call_BlinkXS4_1184
    dap "Bueno... siempre pueden haber excepciones."
    mc "Hablando de cosas que te apasionan. ¿Lo del anillo es un trenzado celta?"
    call BlinkXS4("c30s006_830") from _call_BlinkXS4_1185
    dap "No necesitas darme más razones para que me case contigo."
    dap "Que hayas reconocido el trenzado no me va a convertir más en tu esposa de lo que ya lo soy."
    mc "*Risa* Pues para vivir la experiencia medieval completa... Creo que te compraré un cinturón de castidad para cuando me vaya a Aruba."
    call BlinkXS4("c30s006_835") from _call_BlinkXS4_1186
    dap "*Risa* Eres un idiota."
    mc "*Risa* Más idiota eres tú, que te has casado conmigo."
    if weddings == 0 or not frase:
        call BlinkXS4("c30s006_840") from _call_BlinkXS4_1187
        if weddings == 0:
            call c30s006_tattoo (dap) from _call_c30s006_tattoo_13
        else:
            call c30s006_sentence (dap) from _call_c30s006_sentence_12
    $ weddings = weddings + 1
    if not orangutan:
        call BlinkXS4("c30s006_845") from _call_BlinkXS4_1188
        call c30s006_orangutan (dap) from _call_c30s006_orangutan_4
    call BlinkXS4("c30s006_850") from _call_BlinkXS4_1189
    if mc._var("relationships")>weddings:
        dap "Ve con Jamaal antes de que te secuestre."
        mc "*Risa* Jamaal o ser secuestrado por una preciosa pelirroja. Creo que lo has planteado mal."
    else:
        call c30s006_BetMee(lis) from _call_c30s006_BetMee_11
    scene c30s006_815d with dissolve #beso
    stop music fadeout (1.0)
    if mc._var("relationships")>weddings:
        "Le das un beso de despedida antes de volver con tu mejor amigo. Un amigo al que odias ahora mismo."
    else:
        "Os besáis antes de dirigiros hacia donde se va a desarrollar la fiesta de bienvenida."
    return
label c30s006_waiting(personaje):
    sai "Y ahora deberías irte. [personaje] te está esperando y se empieza a hacer tarde."
    if personaje == eil:
        sai "*Risa* Tengo ganas de saber qué tiene preparado la bruja pelirroja. Nos ha ocultado su tatuaje a todas."
    return
label c30s006_sai:
    scene c30s006_855e with fade
    "Jamaal te guía hacia la piscina. Por el camino más largo"
    play music ("music/RayOfHope.ogg")
    if weddings == 0:
        call c30s006_firstWedding (sai) from _call_c30s006_first_wedding_10
    scene c30s006_855d with fade:
        yalign 1.0
        linear 5.0 yalign 0.0
    pause (4.8)
    call BlinkXS3("c30s006_855") from _call_BlinkXS3_950
    if not _in_replay:
        $ sai.profileImages.insert (15, ("sai_15", None))
    call addProfileImageS3 (15, "sai_15", sai, __(": 15 - Especial"), "") from _call_addProfileImageS3_41
    if weddings > 0:
        mc "Estás preciosa, [sai]. Nunca te había visto con este vestido"
    else:
        call c30s006_approach (sai, False) from _call_c30s006_approach_15
        mc "Nunca te había visto con ese vestido."
    call BlinkXS4("c30s006_860") from _call_BlinkXS4_1190
    if mc._var("relationships")>1:
        sai "La mayoría de nosotras nos hemos comprado vestidos nuevos para lo de hoy."
    else:
        sai "Me lo he comprado para lo de hoy."
    sai "También he ido a la peluquería a cortarme un poco las puntas. Pero esperar que te des cuenta de eso es una utopía."
    if weddings == 0:
        mc "¿Para lo de hoy? ¿La fiesta de bienvenida?"
    else:
        mc "Supongo que necesitabas un vestido con los hombros al descubierto. No tienes demasiados así."
    mc "Puedes ver que he ignorado a propósito la falacia sobre que no me doy cuenta de tus cambios de peinado."
    call BlinkXS4("c30s006_865") from _call_BlinkXS4_1191
    sai "Antes de empezar, déjame explicarte algo."
    mc "Adelante..."
    if weddings==0:
        mc "Aunque no sé a qué te refieres con 'empezar'."
    call BlinkXS4("c30s006_870") from _call_BlinkXS4_1192
    sai "En Portland tú querías formalizar la relación y yo no estaba preparada."
    sai "Me comporté como una idiota, pero sé que, si no lo hubiera hecho, posiblemente no estaríamos aquí hoy, en estas circunstancias."
    stop music fadeout (1.0)
    mc "Lo más probable."
    scene c30s006_870d with dissolve
    play sound ("music/wedding-march-music-box.ogg")
    sai "Con este anillo me declaro tu esposa. Espero que no seas tú el que se comporte como un idiota ahora."
    $ sai._var("engaged", True)
    if weddings==0:
        mc "¿Qué? ¿Quieres casarte conmigo?"
    mc "*Risa* ¿Has pasado de no querer ser mi novia a querer ser mi esposa?"
    call BlinkXS4("c30s006_875") from _call_BlinkXS4_1193
    sai "No lo has entendido. No quiero ser tu esposa. {b}SOY{/b} tu esposa. Si no me rechazas..."
    scene c30s006_875d with dissolve #beso
    "Ni por todo el oro del mundo rechazarías una propuesta como esa."
    "Vuestros labios se juntan en un beso mil veces besado. Y cada una de esas veces ha sido diferente de la anterior."
    "Esta vez no es diferente. O sí. No se parece a ningún beso que os hayáis dado nunca, pero es igual que todos los anteriores."
    call BlinkXS4("c30s006_880") from _call_BlinkXS4_1194
    stop sound
    play music ("music/Rise-Up.ogg")
    sai "Me lo tomaré como que voy a seguir siendo la única idiota de esta relación."
    mc "*Risa* Bueno, el resto de la familia discreparía. Ya no sé si me llamo [mc] o me llamo 'Idiota'."
    call BlinkXS4("c30s006_885") from _call_BlinkXS4_1195
    sai "*Risa* Bueno, no se equivocan demasiado."
    mc "Por cierto, me encanta el anillo. Es muy original."
    call BlinkXS4("c30s006_890") from _call_BlinkXS4_1196
    sai "Busqué por internet modelos de anillos y cuando vi uno parecido a este, un círculo sin cerrar, me recordó a nuestra relación abierta."
    if mc._var("relationships")>1:
        sai "Añadí las barras como una representación del harén. Como si cada chica que añades ayudara a cerrar el círculo."
        sai "Y cada barra es diferente para reflejar que cada una de nosotras somos diferentes también."
    else:
        sai "El anillo era un poco soso, con lo que añadí las barras, como si cada paso que diéramos cerrara un poco el círculo."
        sai "Unos pasos son más grandes que otros, y por eso las barras son diferentes."
    mc "Es una explicación muy bonita, [sai]. Y un diseño muy original."
    mc "Pero ¿por qué ahora?"
    if weddings > 0:
        mc "Sé que el resto del harén te ha impulsado a ello, pero ¿por qué {b}tú{/b} quieres hacer esto ahora?"
    call BlinkXS4("c30s006_895") from _call_BlinkXS4_1197
    sai "Porque ahora te vuelves a ir."
    sai "La última vez que te fuiste, tuve que recorrer medio mundo... dos veces... para volver a encontrarte."
    sai "Cuando te fuiste de Portland, habíamos decidido dejarlo. Ésta es mi forma de decirte que seguiré aquí cuando vuelvas."
    scene c30s006_875d with dissolve #beso
    "No tienes palabras para expresar lo que sus palabras significan para ti, porque sabes lo mucho que significan para ella también."
    "Sí, incluso tú te quedas sin palabras... a veces."
    "Por suerte, tus labios hablan mejor que tú en esas ocasiones."
    if weddings == 0 or not frase:
        call BlinkXS4("c30s006_900") from _call_BlinkXS4_1198
        if weddings == 0:
            call c30s006_tattoo (sai) from _call_c30s006_tattoo_14
        else:
            call c30s006_sentence (sai) from _call_c30s006_sentence_13
    $ weddings = weddings + 1
    if not orangutan:
        call BlinkXS4("c30s006_905") from _call_BlinkXS4_1199
        call c30s006_orangutan (sai) from _call_c30s006_orangutan_5
    call BlinkXS4("c30s006_910") from _call_BlinkXS4_1200
    if mc._var("relationships")>weddings:
        if eil._var("route"):
            call c30s006_waiting (eil) from _call_c30s006_waiting
        elif bet._var("route"):
            call c30s006_waiting (bet) from _call_c30s006_waiting_1
        elif mee._var("route"):
            call c30s006_waiting (mee) from _call_c30s006_waiting_2
        elif nor._var("route"):
            call c30s006_waiting (nor) from _call_c30s006_waiting_3
        elif mar._var("route"):
            call c30s006_waiting (mar) from _call_c30s006_waiting_4
        elif ama._var("route"):
            call c30s006_waiting (ama) from _call_c30s006_waiting_5
    else:
        call c30s006_BetMee(lis) from _call_c30s006_BetMee_12
    scene c30s006_875d with dissolve #beso
    stop music fadeout (1.0)
    "Tras un rápido beso, te despides de [sai] y vuelves con Jamaal."
    return
label c30s006_eil:
    scene c30s006_915e with fade
    if weddings > 0:
        "Jamaal te hace dar una vuelta a la casa hasta que llegáis al lugar donde espera la siguiente chica."
        play music ("music/Separation.ogg")
        "Esta vez es [eil] quien te espera."
    else:
        "Jamaal te acompaña hasta donde [eil] te está esperando."
        play music ("music/Separation.ogg")
    if weddings == 0:
        call c30s006_firstWedding (eil) from _call_c30s006_first_wedding_11
    scene c30s006_915d with fade:
        yalign 1.0
        linear 5.0 yalign 0.0
    pause (4.8)
    call BlinkXS3("c30s006_915") from _call_BlinkXS3_951
    if not _in_replay:
        $ eil.profileImages.insert (15, ("eil_15", None))
    call addProfileImageS3 (15, "eil_15", eil, __(": 15 - Especial"), "") from _call_addProfileImageS3_42
    if weddings > 0:
        mc "Hola, cielo. Estás preciosa."
        eil "Gracias, cariño. A ti te queda genial ese traje."
    else:
        call c30s006_approach (eil, False) from _call_c30s006_approach_16
    call BlinkXS4("c30s006_920") from _call_BlinkXS4_1201
    eil "Aquí estamos para cerrar el círculo, ¿no?"
    mc "No sé a qué círculo te refieres, [eil.nick]."
    call BlinkXS4("c30s006_925") from _call_BlinkXS4_1202
    eil "Empezamos a salir en el instituto, intentamos tener una relación a distancia, rompimos, y hemos vuelto a estar juntos."
    eil "¿No te parece un círculo incompleto? El primer beso que nos dimos aquí, en tu casa, fue justo aquí. En las tumbonas que suele haber aquí."
    mc "Lo recuerdo. No querías subir a mi habitación por si quería ir demasiado deprisa."
    mc "No querías besarme con mi familia alrededor y estuvimos leyendo Romeo y Julieta justo aquí, bajo el sol."
    call BlinkXS4("c30s006_930") from _call_BlinkXS4_1203
    eil "Y yo no me estaba enterando de nada de lo que leíamos. Tan solo tenía ganas de besarte mientras recitabas a Shakespeare."
    mc "A mí me temblaban las piernas. Por suerte estábamos sentados y no se notaba..."
    call BlinkXS4("c30s006_935") from _call_BlinkXS4_1204
    eil "*Risa* Nunca lo hemos hablado, pero lo noté. No hacías más que mover la pierna, como cuando estás concentrado, pero más rápido."
    mc "Y, pese a todo, me besaste."
    call BlinkXS4("c30s006_940") from _call_BlinkXS4_1205
    eil "No pude aguantar más y me daba lo mismo que tu familia estuviera en casa."
    eil "Eras irresistible entonces y lo sigues siendo ahora, cielo."
    eil "*Risa* Te prohíbo que le leas Shakespeare a ninguna chica en Aruba. Bueno, se lo puedes leer a [ama], [eva], o Tía [bet]..."
    stop music fadeout (1.0)
    if weddings==0:
        mc "Pero no sé qué tiene que ver eso con cerrar el círculo."
    else:
        mc "Y ahora quieres cerrar el círculo aquí mismo."
    scene c30s006_940d with dissolve
    play sound ("music/wedding-march-music-box.ogg")
    eil "Con este anillo me declaro tu esposa. Quería que fuera a la vez un círculo y un anillo..."
    $ eil._var("engaged", True)
    if mc._var("relationships")>1:
        if not ama._var("route") or mc._var("relationships")>2:
            eil "Aunque después de ver los otros tatuajes... parece soso."
    else:
        eil "Sé que parece un poco soso..."
    mc "A mí me parece perfecto. Y no sólo como círculo que cerramos hoy, sino por todo lo que significa."
    mc "Un círculo es una línea. Una línea es un conjunto de puntos. Y los hemos recorrido todos tú y yo juntos."
    call BlinkXS4("c30s006_945") from _call_BlinkXS4_1206
    if weddings==0:
        eil "No pareces sorprendido de que me haya declarado tu esposa en vez de pedirte que te casaras conmigo."
    else:
        eil "Espero que no estés decepcionado porque te lo haya dicho así... En vez de pedirte que te casaras conmigo."
        eil "Sé que no soy la primera, pero..."
    mc "No lo estoy. En el momento en que has hablado de cerrar el círculo..."
    stop sound
    play music ("music/Rise-Up.ogg")
    mc "Pedirme que me casara contigo sería tan solo otro punto del círculo. Lo tendríamos que cerrar en la boda."
    call BlinkXS4("c30s006_950") from _call_BlinkXS4_1207
    eil "Siempre supe que algún día me lo pedirías. O al menos lo esperaba..."
    mc "Yo ya lo hice, [eil.nick]. Muchas veces. Y siempre dijiste que sí."
    scene c30s006_950d with hpunch
    eil "¿Qué? ¿Cuándo?"
    mc "Cada vez que te quedabas a dormir en mi habitación durante el último año de instituto."
    mc "¿Quién se dormía primero siempre?"
    call BlinkXS4("c30s006_955") from _call_BlinkXS4_1208
    eil "Yo. *Risa* Caía dormida en el momento en que mi cabeza tocaba tu pecho. Eras tan cómodo..."
    mc "Cuando llevabas unos minutos durmiendo y se me dormía el brazo, siempre decía lo mismo."
    mc "'Te quiero. Un día me casaré contigo. ¿Quieres casarte conmigo, [eil.nick]?'"
    call BlinkXS4("c30s006_960") from _call_BlinkXS4_1209
    eil "*Risa* ¿Y yo contestaba?"
    mc "Siempre decías lo mismo. 'Sí. Mañana.'"
    mc "Y 'mañana' es hoy."
    scene c30s006_960d with dissolve #beso
    "Coges a tu esposa entre tus brazos por primera vez como recién casados."
    "Os besáis como si llevarais 25 años casados. Como si vuestra relación acabara de empezar. Como si... Como si estuvierais hechos el uno para el otro."
    "Tu vida con ella pasa por delante de tus ojos cerrados mientras rememoras cada beso, cada abrazo, cada..."
    call BlinkXS4("c30s006_970") from _call_BlinkXS4_1210
    eil "Yo también te quiero."
    mc "*Risa* Hace un rato me he acordado de una cosa. No sé si puedo querer a una mentirosa."
    call BlinkXS4("c30s006_975") from _call_BlinkXS4_1211
    eil "¿Qué ha recordado esa mente retorcida tuya?"
    mc "¿Te acuerdas de la primera vez que hablamos de que un día nos casaríamos? Estando tú despierta, claro."
    call BlinkXS4("c30s006_980") from _call_BlinkXS4_1212
    eil "*Risa* Dije que le pagaríamos a Jamaal un título de esos que se pueden sacar online para que nos pudiera casar."
    mc "*Risa* Llevo un rato esperando que aparezca Jamaal con una túnica o que se ponga un alzacuellos."
    eil "*Risa* Aún está en la puerta del garaje. Y sigue vestido... normal."
    mc "*Risa* Me alegra que faltaras a tu palabra."
    call BlinkXS4("c30s006_985a") from _call_BlinkXS4_1213
    eil "Yo también. Esto es sólo nuestro. Es nuestro momento, aunque tenga que durar muy poco."
    if mc._var("relationships")==2:
        eil "Y aunque lo tengamos que compartir con otra de tus chicas."
    else:
        eil "Y aunque lo tengamos que compartir con tus otras chicas."
    if sai._var("route"):
        mc "Por cierto, ¿sabes que llevas el mismo vestido que [sai]?"
        call BlinkXS4("c30s006_985b") from _call_BlinkXS4_1214
        eil "*Risa* Lo hemos descubierto hace un rato. Por suerte el color es diferente."
        eil "Hasta cierto punto tiene lógica. Compartimos gustos por nuestro marido y por los vestidos... Bueno, compartimos marido."
    if weddings == 0 or not frase or not orangutan:
        mc "Lo sé. Pero..."
    else:
        mc "Lo sé."
    if weddings == 0 or not frase:
        call BlinkXS4("c30s006_990a") from _call_BlinkXS4_1215
        if weddings == 0:
            call c30s006_tattoo (eil) from _call_c30s006_tattoo_15
        else:
            call c30s006_sentence (eil) from _call_c30s006_sentence_14
    $ weddings = weddings + 1
    if not orangutan:
        call BlinkXS4("c30s006_990b") from _call_BlinkXS4_1216
        call c30s006_orangutan (eil) from _call_c30s006_orangutan_6
    call BlinkXS4("c30s006_995") from _call_BlinkXS4_1217
    if mc._var("relationships")>weddings:
        eil "Y ahora deberías irte con nuestro maestro de ceremonias."
        eil "Hay otra chica esperándote y, como Primera Concubina, tengo que cuidar de ella y no robarle más tiempo del necesario."
    else:
        call c30s006_BetMee(eil) from _call_c30s006_BetMee_13
        eil "No deberíamos robarles más tiempo."
    scene c30s006_960d with dissolve #beso
    "Robáis un poco de tiempo para alargar el beso lo máximo posible antes de tener que separaros."
    stop music fadeout (1.0)
    "Tu boda con [eil] se te ha hecho demasiado corta. Tan corta como parece cada uno de vuestros besos, independientemente de cuánto duren."
    return
label c30s006_bet:
    scene c30s007_005e with fade
    "Jamaal te acompaña hasta donde [bet] te está esperando."
    play music ("music/pianomatic.ogg")
    if weddings == 0:
        call c30s006_firstWedding (bet) from _call_c30s006_first_wedding_12
    scene c30s007_005d with fade:
        yalign 1.0
        linear 5.0 yalign 0.0
    pause (4.8)
    call BlinkXS3("c30s007_005") from _call_BlinkXS3_952
    if not _in_replay:
        $ bet.profileImages.insert (15, ("bet_15", None))
    call addProfileImageS3 (15, "bet_15", bet, __(": 15 - Especial"), "") from _call_addProfileImageS3_43
    if weddings > 0:
        mc "Estás guapísima, [bet]."
    else:
        call c30s006_approach (bet, False) from _call_c30s006_approach_17
    mc "Bienvenida de vuelta a casa."
    mc "Se me hace raro verte vestida así y... maquillada."
    scene c30s007_030d with dissolve #beso
    "Tras varios días de separación vuestros labios se buscan antes de que la exmonja conteste."
    "Es un beso breve, pero es suficiente para calmar el hambre del otro que habéis tenido estos últimos días. Al menos de momento."
    call BlinkXS4("c30s007_010") from _call_BlinkXS4_1218
    bet "Una mujer tiene que ponerse guapa para lo que vamos a hacer, ¿no?"
    mc "No hacía falta que lo hicieras. Sé que no te gusta llevar maquillaje. Y estás guapa sin maquillaje también."
    if weddings == 0:
        mc "Pero aún no sé qué vamos a hacer..."
        call BlinkXS4("c30s007_015") from _call_BlinkXS4_1219
        bet "Algunas chicas me comentaron una idea muy loca por videoconferencia hace unos días..."
        if mc._var("relationships")>1:
            bet "Y al harén le pareció bien... A mí al principio no me lo pareció, pero..."
    else:
        call BlinkXS4("c30s007_015") from _call_BlinkXS4_1220
        if mad._var("route"):
            bet "Cuando [mad.nick] propuso lo del tatuaje, el día que nos íbamos, justo después del post-it, me pareció una locura."
        else:
            bet "Cuando propusieron lo del tatuaje, en una videoconferencia, me pareció una locura."
    bet "Tal como le iba dando vueltas, cada vez me parecía mejor."
    mc "A veces dais miedo cuando os ponéis a planear cosas."
    call BlinkXS4("c30s007_020") from _call_BlinkXS4_1221
    bet "El maquillaje ha sido el toque final. Sin él me sentía un poco... sosa."
    stop music fadeout (1.0)
    mc "¿Sosa? ¿Con ese vestido? ¡Estás increíble!"
    scene c30s007_020d with dissolve
    play sound ("music/wedding-march-music-box.ogg")
    bet "No me refiero al vestido. Con este anillo me declaro tu esposa. Sé que es un anillo muy sencillo, pero..."
    $ bet._var("engaged", True)
    if weddings==0:
        mc "¿Qué? ¿Quieres casarte conmigo?"
        bet "No, tan solo te informo de que estamos casados."
    else:
        mc "¡Es super chulo!"
    call BlinkXS4("c30s007_025") from _call_BlinkXS4_1222
    bet "*Risa* Si cuando me casé con Dios no le pedí permiso, tampoco te lo pido a ti. Aunque espero que lo nuestro acabe mejor."
    mc "*Risa* Te dio su permiso implícito, si existe. Si no hubiera querido, te hubiera mandado un rayo vengador o algo así."
    bet "*Risa* Sí, sería muy de su estilo."
    call BlinkXS4("c30s007_030") from _call_BlinkXS4_1223
    bet "¿Y tú? ¿Me aceptas como tu esposa?"
    mc "*Risa* Bueno, yo no puedo lanzar rayos vengadores... Lo de Mjolnir solo es un apodo."
    mc "Pero puedo hacer esto."
    scene c30s007_030d with dissolve #beso
    "Coges a la exmonja entre tus brazos y le das un apasionado beso."
    "No necesita maquillarse o cambiar para ser una mujer maravillosa. Aunque tienes que reconocer que le sienta bien."
    "Una parte de tu cerebro espera la llegada de un rayo vengador durante todo el beso."
    "Esa parte de tu cerebro piensa que lo de robarle la mujer a Dios podría tener consecuencias inesperadas. ¿Le has hecho netori a Dios?"
    call BlinkXS4("c30s007_035") from _call_BlinkXS4_1224
    stop sound
    play music ("music/Rise-Up.ogg")
    "Para cuando el beso acaba, el resto de tu mente ha acallado a la que se preocupaba demasiado."
    bet "*Risa* No lanzas rayos, pero una corriente me ha recorrido de los pies a la cabeza con ese beso."
    mc "*Risa* Al final va a resultar que sí que soy un dios."
    call BlinkXS4("c30s007_040") from _call_BlinkXS4_1225
    bet "*Risa* Que no se te suba a la cabeza."
    if mc._var("relationships")>1:
        bet "*Risa* Al final he cambiado el harén de un dios por el de un marido divino."
    else:
        bet "*Risa* Al final he cambiado un marido divino por otro."
    mc "*Risa* Creo que, si sigues diciendo cosas así, se me va a acabar subiendo a la cabeza."
    call BlinkXS4("c30s007_045") from _call_BlinkXS4_1226
    bet "*Risita* Bueno, creo que las togas y las túnicas le quedan mejor a él, si eso ayuda a bajarte los humos."
    mc "*Risa* Ahí, dando donde más duele. Todas os ponéis de acuerdo en que la ropa me queda mal. Incluso Jamaal."
    bet "*Risa* Es que, excepto este traje, casi todo te queda mal."
    mc "*Risa* A veces os odio..."
    mc "Cambiando de tema, me gusta que hayas elegido un anillo sencillo a la par que bonito."
    call BlinkXS4("c30s007_050") from _call_BlinkXS4_1227
    bet "Creo que nos define bastante. Nuestra relación es... más bonita que pasional..."
    bet "No me entiendas mal. No me estoy quejando... Dudo que muchas mujeres tengan una noche como la que tuvimos en Monterey."
    mc "No hemos tenido demasiado tiempo para estar juntos desde que volvimos de Monterey... Al menos espero poder pasar tiempo contigo en Aruba."
    if weddings == 0 or not frase:
        mc "Pero tengo una duda..."
        call BlinkXS4("c30s007_055") from _call_BlinkXS4_1228
        if weddings == 0:
            call c30s006_tattoo (bet) from _call_c30s006_tattoo_16
        else:
            call c30s006_sentence (bet) from _call_c30s006_sentence_15
    $ weddings = weddings + 1
    if not orangutan:
        call BlinkXS4("c30s007_060") from _call_BlinkXS4_1229
        call c30s006_orangutan (bet) from _call_c30s006_orangutan_7
    call BlinkXS4("c30s007_065") from _call_BlinkXS4_1230
    if mc._var("relationships")>weddings:
        bet "Y ahora creo que deberías irte. Hay otra chica esperándote."
        mc "Y después está la fiesta para daros la bienvenida a ti y a Meemaw."
    else:
        bet "Y ahora creo que deberíamos irnos. [mee] se debe estar impacientando."
        mc "Vamos antes de que deje de impacientarse y empiece a enfadarse."
    call BlinkXS4("c30s007_055") from _call_BlinkXS4_1231
    bet "*Risa* Además, [nor] me ha prometido que pedirá pizza."
    scene c30s007_030d with dissolve #beso
    "Le das un rápido beso mientras piensas en si hay algo que [bet] prefiera a la pizza."
    "Aparte de besos, abrazos y sexo."
    stop music fadeout (1.0)
    "Tampoco llega el rayo vengador esta vez."
    return
label c30s006_mee:
    scene c30s007_070e with fade
    "Vas con Jamaal hasta la parte delantera de la casa de [nor], donde [mee] te está esperando."
    play music ("music/pianomatic.ogg")
    "Está en el mismo lugar donde se quedó esperándote, empapada, el día de vuestra cita."
    if weddings == 0:
        call c30s006_firstWedding (mee) from _call_c30s006_first_wedding_13
    scene c30s007_070d with fade:
        yalign 1.0
        linear 5.0 yalign 0.0
    pause (4.8)
    call BlinkXS3("c30s007_070") from _call_BlinkXS3_953
    if not _in_replay:
        $ mee.profileImages.insert (15, ("mee_15", None))
    call addProfileImageS3 (15, "mee_15", mee, __(": 15 - Especial"), "") from _call_addProfileImageS3_44
    if weddings > 0:
        mc "Estás guapísima, Meemaw."
    else:
        call c30s006_approach (mee, False) from _call_c30s006_approach_18
    scene c30s007_100d with dissolve #beso
    "Besas a la preciosa anciana dándole la bienvenida de vuelta a la casa de la locura."
    call BlinkXS4("c30s007_075") from _call_BlinkXS4_1232
    mc "Bienvenida de vuelta a casa, por cierto."
    mee "¿Alguna vez vas a dejar de llamarme Meemaw? Estamos juntos y..."
    mc "No lo creo, si a ti no te molesta. Para mí siempre serás Meemaw. No puedo pensar en ti como [mee]."
    mc "Sé que ahora salimos juntos, pero eso no evita que sigas siendo mi Meemaw."
    mc "Aunque, si te molesta, podría intentarlo."
    call BlinkXS4("c30s007_080") from _call_BlinkXS4_1233
    mee "No me molesta. Tan solo creía que, quizás, quisieras empezar a llamarme por mi nombre."
    if persistent.family:
        mee "Y dejar de pensar en mí como en tu abuela."
    else:
        mee "Y dejar de pensar en mí como en tu pseudo-abuela."
    mc "Nunca dejaré de pensar en ti de esa forma. Que estemos juntos no significa que dejemos de ser quienes somos."
    stop music fadeout (1.0)
    mc "Aunque no entiendo por qué quieres que deje de llamarte Meemaw de repente."
    scene c30s007_080d with dissolve
    play sound ("music/wedding-march-music-box.ogg")
    mee "No quiero, pero si tú quisieras, este tatuaje perdería un poco de sentido."
    mee "Con estos anillos me declaro tu esposa. Uno por abuela, otro por amante, y el tercero por esposa."
    $ mee._var("engaged", True)
    if weddings==0:
        mc "¿Qué? ¿Me estás pidiendo que me case contigo?"
        mee "*Risa* No, te estoy informando de que estamos casados."
    mc "Me encanta. Le has buscado un bonito significado al tatuaje."
    call BlinkXS4("c30s007_090") from _call_BlinkXS4_1234
    mee "No le busques mucho significado a los colores de los anillos..."
    mc "Antes de decir qué significaba cada anillo, he pensado en tu pelo. De negro a blanco pasando por plateado."
    mc "Resume toda nuestra historia, aunque no te recuerdo con el pelo negro aparte de en las fotos que he visto."
    stop sound
    play music ("music/Rise-Up.ogg")
    call BlinkXS4("c30s007_095") from _call_BlinkXS4_1235
    mee "*Risa* Creo que ya tenía algunas canas cuando naciste. Tenía la edad de [nor]."
    mc "Algún día nos tenemos que sentar a mirar fotos tuyas de joven para saber lo que me he perdido."
    mc "No me malinterpretes, no cambiaría esta versión de ti por ninguna otra, pero nunca he mirado tus fotos antiguas viéndote como mujer."
    mc "Siempre has sido Meemaw. Y lo seguirás siendo."
    call BlinkXS4("c30s007_100") from _call_BlinkXS4_1236
    mee "Te sorprenderás con algunas de esas fotos viejas... Hay algunas un poco atrevidas... Aunque esas no están en el álbum familiar." id c30s006_mee_71cd67eb
    mc "Estoy deseando verlas. Pero creo que, ahora, tengo que besar a mi esposa."
    scene c30s007_100d with dissolve #beso
    "Rodeas a la mujer entre tus brazos y la besas con pasión."
    "Recuerdas lo frágil que parecía cuando llego a casa, aún recuperándose de la quimioterapia."
    "Esa fragilidad ha desaparecido para ser sustituida por fuerza y alegría por vivir."
    call BlinkXS4("c30s007_105") from _call_BlinkXS4_1237
    mee "No sigas o voy a manchar el vestido con leche..."
    mc "¿Ya te has excitado?"
    call BlinkXS4("c30s007_110") from _call_BlinkXS4_1238
    mee "*Risa* Llevo excitada desde que te he visto aparecer con Jamaal."
    mc "*Risa* No dejas de sorprenderme."
    if weddings == 0 or not frase:
        call BlinkXS4("c30s007_115") from _call_BlinkXS4_1239
        if weddings == 0:
            call c30s006_tattoo (mee) from _call_c30s006_tattoo_17
        else:
            call c30s006_sentence (mee) from _call_c30s006_sentence_16
    $ weddings = weddings + 1
    if not orangutan:
        call BlinkXS4("c30s007_120") from _call_BlinkXS4_1240
        call c30s006_orangutan (mee) from _call_c30s006_orangutan_8
    call BlinkXS4("c30s007_125") from _call_BlinkXS4_1241
    if mc._var("relationships")>weddings:
        mee "Ahora deberías irte. No quiero entretenerte más tiempo del debido."
        if nor._var("route") or mar._var("route") and persistent.family:
            mee "Mi hija te está esperando. Es la siguiente."
        elif mar._var("route") and not persistent.family:
            mee "[mar] te está esperando. Es la siguiente."
        elif ama._var("route"):
            mee "[ama] te está esperando. Es la siguiente."
        mc "Odio tener que hacer esto de forma tan rápida, pero tengo ganas de verla y saber qué tiene preparado. O tatuado."
    else:
        mee "Ahora deberíamos ir a la fiesta de bienvenida. No van a empezar sin mí."
        mee "Y si se enfría la comida, [bet] va a enfadarse."
        mc "*Risa* No creo que se enfadara hoy aunque la dejáramos sin comer."
    scene c30s007_100d with dissolve #beso
    stop music fadeout (1.0)
    if mc._var("relationships")>weddings:
        "Le das un rápido beso a la preciosa mujer antes de volver con Jamaal."
    else:
        "Le das un rápido beso a la preciosa mujer antes de dirigiros a la fiesta de bienvenida de la que ella es protagonista."
    return
label c30s006_nor:
    scene c30s007_130e with fade
    "Jamaal te guía hasta el lugar donde comisteis el primer domingo después de tu retorno."
    play music ("music/pianomatic.ogg")
    "Lo de vestirse elegante para comer cayó en desuso una vez [mar] salió de la depresión."
    "[nor] te está esperando justo donde os besasteis aquel día."
    if weddings == 0:
        call c30s006_firstWedding (nor) from _call_c30s006_first_wedding_14
    scene c30s007_130d with fade:
        yalign 1.0
        linear 5.0 yalign 0.0
    pause (4.8)
    call BlinkXS3("c30s007_130") from _call_BlinkXS3_954
    if not _in_replay:
        $ nor.profileImages.insert (15, ("nor_15", None))
    call addProfileImageS3 (15, "nor_15", nor, __(": 15 - Especial"), "") from _call_addProfileImageS3_45
    if weddings == 0:
        call c30s006_approach (nor, False) from _call_c30s006_approach_19
    mc "Me encanta ese vestido, [nor]. Y aún más lo que hay dentro."
    call BlinkXS4("c30s007_135") from _call_BlinkXS4_1242
    nor "No recuerdo la última vez que me vestí de blanco. ¿Hace un mes quizás? Pero me parecía una buena idea hacerlo hoy."
    mc "Si cada vestido blanco te queda como ese, creo que deberías alternarlos con los vestidos rojos."
    call BlinkXS4("c30s007_140") from _call_BlinkXS4_1243
    nor "*Risa* ¿No te gustan mis vestidos rojos?"
    mc "Me encanta todo de ti. Tus vestidos y cuando te los quitas. Tus labios rojos que resaltan aún más vestida de blanco."
    mc "No hay nada que me gustaría cambiar de ti. Te lo he dicho muchas veces."
    call BlinkXS4("c30s007_145") from _call_BlinkXS4_1244
    nor "Y esa es una de las razones por las que estoy enamorada de ti."
    nor "Empezaste besando a una mujer insegura y ahora soy capaz de vestirme de blanco... *Risa* Y el blanco hace gorda."
    call BlinkXS4("c30s007_150") from _call_BlinkXS4_1245
    nor "Pero ¿de verdad no cambiarías nada de mí? ¿Ni siquiera mi espalda o mis hombros?"
    stop music fadeout (1.0)
    mc "Lo puedo jurar por lo más sagrado que haya."
    if weddings > 0:
        mc "Aunque tengo ganas de ver qué te has tatuado."
    scene c30s007_160d with dissolve
    play sound ("music/wedding-march-music-box.ogg")
    if weddings == 0:
        nor "Pues lo siento mucho, pero hay un cambio."
    nor "Con estos anillos me declaro tu esposa."
    $ nor._var("engaged", True)
    mc "¿Qué? ¡Me encantan!"
    call BlinkXS4("c30s007_155") from _call_BlinkXS4_1246
    nor "Quise representar muchas cosas con ellos, pero no estoy muy convencida de que puedas entenderlo..."
    mc "Puedes explicármelo si quieres, pero antes quiero besarte."
    scene c30s007_160e with dissolve #beso
    "¡Cómo ha cambiado todo en un mes! La mujer insegura a la que besaste en aquel café se ha hecho un tatuaje para declararse tu esposa."
    "Sus labios siguen siendo como un hogar al que volver siempre. Eso nunca cambiará."
    "Es imposible no pensar en todos los momentos que habéis pasado juntos en las últimas cinco semanas mientras recorres tu boca con su lengua."
    call BlinkXS4("c30s007_160") from _call_BlinkXS4_1247
    stop sound
    play music ("music/Rise-Up.ogg")
    mc "Ahora puedes explicármelo."
    nor "*Risa* Ahora no tengo aliento para hacerlo."
    mc "Entonces no tendrás aliento tampoco para resistirte si te quito el vestido, ¿no?"
    scene c30s007_160f with hpunch
    nor "¿Qué? ¿Quieres quitarme el vestido? ¿Ahora?"
    mc "*Risa* Siempre quiero quitarte lo que llevas puesto. Pero he pensado que si vas a la fiesta desnuda sería el último paso en tu exhibicionismo."
    call BlinkXS4("c30s007_165") from _call_BlinkXS4_1248
    nor "*Risa* Y el primer paso de mi madre hacia el ataúd. Si voy desnuda le dará un infarto."
    mc "Estaba bromeando, pero veo que ya has recuperado el aliento. ¿Me explicas el tatuaje?"
    call BlinkXS4("c30s007_170") from _call_BlinkXS4_1249
    nor "Son dos anillos entrelazados, representándonos a ti y a mí."
    nor "Pensé que todo esto no empezó cuando volviste de la universidad, sino que hemos estado caminando hacia este momento desde hace años."
    call BlinkXS4("c30s007_175") from _call_BlinkXS4_1250
    nor "Por eso los anillos no tienen los bordes lisos... Son como un zigzag en el que nos acercábamos y nos alejábamos."
    nor "Y tienen varios tonos para representar todas las fases por las que hemos pasado."
    call BlinkXS4("c30s007_180") from _call_BlinkXS4_1251
    nor "Ya lo sé... Muy abstracto y nadie va a pillar el significado si no se lo explico."
    mc "¿Necesitas explicárselo a alguien? Bueno, excepto a mí, pero ya sabes que a veces me cuesta pillar las cosas."
    mc "Una vez me lo has explicado me parece un tatuaje fantástico."
    call BlinkXS4("c30s007_200") from _call_BlinkXS4_1252
    nor "Tienes razón, no le debemos explicaciones a nadie, ¿verdad?"
    mc "Solo a quién queramos dárselas, cielo."
    if weddings == 0 or not frase:
        call BlinkXS4("c30s007_185") from _call_BlinkXS4_1253
        if weddings == 0:
            call c30s006_tattoo (nor) from _call_c30s006_tattoo_18
        else:
            call c30s006_sentence (nor) from _call_c30s006_sentence_17
    $ weddings = weddings + 1
    if not orangutan:
        call BlinkXS4("c30s007_190") from _call_BlinkXS4_1254
        call c30s006_orangutan (nor) from _call_c30s006_orangutan_9
    call BlinkXS4("c30s007_195") from _call_BlinkXS4_1255
    if mc._var("relationships")>weddings:
        nor "Bueno, basta ya de explicaciones. Tienes que irte."
        if mar._var("route"):
            nor "[mar] se debe de estar impacientando."
        elif ama._var("route"):
            nor "[ama] se debe de estar impacientando."
        mc "Sabes que me quedaría aquí contigo un rato más, ¿verdad?"
        nor "Lo sé, pero no puedes hacerla esperar."
    else:
        nor "Bueno, basta ya de explicaciones. Tenemos que irnos."
        nor "Mi madre y Tía [bet] se deben de estar impacientando."
        mc "Estoy seguro de que lo entenderán si tardamos un poco. Sabes que me quedaría aquí contigo un rato más, ¿verdad?"
        nor "Lo sé, pero no podemos hacerlas esperar. Y yo tengo que pasar por la cocina antes de unirme a la fiesta."
    scene c30s007_160e with dissolve #beso
    "Os dais un rápido beso de despedida. Tan solo vais a estar separados unos minutos, pero se os van a hacer muy largos."
    stop music fadeout (1.0)
    "Y en un par de días os separaréis por unos meses. Eso va a ser un infierno."
    return
label c30s006_mar:
    scene c30s007_205e with fade
    if weddings > 0 and not ama._var("route"):
        "Jamaal te acompaña hasta la última parada del alucinante recorrido."
    elif weddings > 0 and ama._var("route"):
        "Jamaal te acompaña hasta la penúltima parada del alucinante recorrido."
    else:
        "Jamaal te acompaña de vuelta a la puerta de tu casa."
    play music ("music/pianomatic.ogg")
    "[mar] está esperando allí, en el mismo sitio donde os visteis por primera vez al volver a casa."
    if weddings == 0:
        call c30s006_firstWedding (mar) from _call_c30s006_first_wedding_15
    scene c30s007_205d with fade:
        yalign 1.0
        linear 5.0 yalign 0.0
    pause (4.8)
    call BlinkXS3("c30s007_205") from _call_BlinkXS3_955
    if not _in_replay:
        $ mar.profileImages.insert (15, ("mar_15", None))
    call addProfileImageS3 (15, "mar_15", mar, __(": 15 - Especial"), "") from _call_addProfileImageS3_46
    if weddings > 0:
        mc "Hoy soy el tipo más afortunado del mundo. Varias veces, además."
        mom "*Risa* Espero que te sientas así. Yo me siento la mujer más afortunada del mundo."
    else:
        call c30s006_approach (mom, False) from _call_c30s006_approach_20
    call BlinkXS4("c30s007_210") from _call_BlinkXS4_1256
    mc "Supongo que hoy no colaría si te dijera que soy el repartidor de Amazonian."
    mom "Supones bien. A menos que traigas una caja de dónuts."
    mc "Bueno, ya te di el mejor dónut del mundo. El que te convertía en mi esposa."
    call BlinkXS4("c30s007_215") from _call_BlinkXS4_1257
    stop music fadeout (2.0)
    if weddings > 0:
        mom "Lo cual me ha dejado un poco al margen con lo de hoy. Soy la única que no se puede declarar tu esposa. Ya lo soy."
        mc "Pero aún y así quiero saber qué te has tatuado."
    else:
        mom "Lo cual ha hecho esto un poco innecesario. Pero las chicas han insistido y creo que es un gesto bonito antes de que te vayas."
        mc "No sé si te has dado cuenta, pero aún no sé de qué va esto."
    scene c30s007_215d with dissolve
    play sound ("music/wedding-march-music-box.ogg")
    mom "Con este dónut me declaro tu esposa. *Risa* Sé que ya lo soy, pero quería decir esa frase."
    mom "Tú me regalaste el mejor dónut del mundo, y quiero llevarlo siempre conmigo."
    mc "*Risa* ¡Te has tatuado el dónut!"
    call BlinkXS4("c30s007_220") from _call_BlinkXS4_1258
    if persistent.family:
        mom "Sé que nunca permitirán que una madre se case con su hijo."
        if mc._var("relationships")>1:
            mom "Además, no me gustaría que el resto del harén sienta que me has elegido a mí por encima de ellas."
    elif mc._var("relationships")>1:
        mom "Nunca podremos casarnos porque no quiero que el resto del harén sienta que me has elegido a mí por encima de ellas."
    else:
        mom "No vamos a poder casarnos antes de que te vayas a Aruba y quería mi anillo."
    if mc._var("relationships")>1 or persistent.family:
        mom "Y, aunque pudiéramos, no podríamos hacerlo antes de que te vayas a Aruba."
    call BlinkXS4("c30s007_225") from _call_BlinkXS4_1259
    mom "Pero como dijiste en la cocina, no necesitamos el permiso de nadie ni un anillo de boda para sentirnos marido y mujer."
    mom "Creo que este es el anillo más dulce que se puede tener."
    scene c30s007_225d with dissolve #beso
    "Si hay algo más dulce que el anillo, son los labios de tu esposa."
    "Y sus abrazos, y su sonrisa, y su mirada..."
    "Ciertamente eres el tipo más afortunado de la historia."
    call BlinkXS4("c30s007_230") from _call_BlinkXS4_1260
    stop sound
    play music ("music/Rise-Up.ogg")
    mom "Te quiero."
    mc "Yo también te quiero."
    scene c30s007_230d with dissolve #abrazo
    "No necesitáis decir nada más, al menos por un rato."
    "Sabéis que habéis recorrido un largo camino desde aquel día en que se tiró a tus brazos, el día que llegaste, y acabasteis los dos en el suelo."
    "La sigues teniendo entre tus brazos, de una forma diferente que no podíais imaginar entonces, y no piensas soltarla nunca. Al menos figuradamente."
    if weddings == 0 or not frase:
        call BlinkXS4("c30s007_240") from _call_BlinkXS4_1261
        if weddings == 0:
            call c30s006_tattoo (mar) from _call_c30s006_tattoo_19
        else:
            call c30s006_sentence (mar) from _call_c30s006_sentence_18
    $ weddings = weddings + 1
    if not orangutan:
        call BlinkXS4("c30s007_245") from _call_BlinkXS4_1262
        call c30s006_orangutan (mar) from _call_c30s006_orangutan_10
    call BlinkXS4("c30s007_235a") from _call_BlinkXS4_1263
    if ama._var("route"):
        mom "Deberías ir a ver a [ama] ahora. Estaba muy nerviosa por lo de hoy."
        mc "Me gustaría quedarme un rato más contigo, pero también tengo ganas de verla a ella."
        mom "Nosotros tuvimos nuestro momento cuando me diste el dónut. No necesito más."
        call BlinkXS4("c30s007_235b") from _call_BlinkXS4_1264
        mom "Sé que no es necesario que te lo diga, pero cuida de mi niña cuando estéis en Aruba, por favor."
        mc "No te preocupes. Creo que cuidará más ella de mí que yo de ella..."
    else:
        mom "Deberíamos ir hacia la fiesta de bienvenida o se van a impacientar."
        mc "Me gustaría quedarme un rato más contigo, pero creo que hemos retrasado la fiesta demasiado."
        mom "Nosotros tuvimos nuestro momento cuando me diste el dónut. No necesito más."
        mom "Tendremos tiempo para estar juntos antes de que te vayas. Pero tengo que subir a la cocina a coger unas cosas antes de unirme."
        mc "Eso espero..."
    scene c30s007_225d with dissolve #beso
    stop music fadeout (2.0)
    "Os dais un largo beso antes de separaros."
    "Se os hace corto."
    return
label c30s006_ama:
    scene c30s007_250e with fade
    "Jamaal te acompaña hasta la puerta de la cocina de [nor]. [ama] te está esperando un poco más allá."
    play music ("music/Retrospection.ogg")
    "Parece que se aleje conscientemente del lugar donde rompió a llorar durante su presentación a la familia."
    if weddings == 0:
        call c30s006_firstWedding (ama) from _call_c30s006_first_wedding_16
    scene c30s007_250d with fade:
        yalign 1.0
        linear 5.0 yalign 0.0
    pause (4.8)
    call BlinkXS3("c30s007_250") from _call_BlinkXS3_956
    if not _in_replay:
        $ ama.profileImages.insert (15, ("ama_15", None))
    call addProfileImageS3 (15, "ama_15", ama, __(": 15 - Especial"), "") from _call_addProfileImageS3_47
    if weddings > 0:
        mc "Estás guapísima, [ama]."
        ama "Gracias. ¿Podemos pasear?"
    else:
        call c30s006_approach (ama, False) from _call_c30s006_approach_21
        ama "¿Te apetece que demos un paseo?"
    mc "Por supuesto."
    scene c30s007_255d with fade
    "Empezáis a caminar mientras [ama] parece pensativa."
    scene c30s007_255e with fade
    "La coges de la mano, de una forma suave, diciéndole que estás ahí para lo que quiera."
    ama "Gracias..."
    mc "¿Pasa algo [ama]?"
    call BlinkXS4("c30s007_255") from _call_BlinkXS4_1265
    ama "Vas a pensar que soy tonta."
    mc "El día que lo piense, pégame un tiro..."
    mc "*Risa* No me hagas caso. Tú serías capaz de hacerlo. Era sarcasmo."
    mc "A lo que me refiero es que no creo que haya llegado el día en que pueda pensar que eres tonta."
    call BlinkXS4("c30s007_260") from _call_BlinkXS4_1266
    if weddings > 0:
        ama "Sabes lo de los tatuajes... Lo de declararnos tus esposas y todo eso..."
    else:
        ama "Las chicas me convencieron para que me hiciera un tatuaje para decirte que me consideraba tu esposa."
    mc "Es muy original, pero ¿dónde está el problema?"
    call BlinkXS4("c30s007_265") from _call_BlinkXS4_1267
    ama "En que no lo quiero hacer."
    mc "No tienes por qué hacerlo. Decir que te sientes como si estuviéramos casados a estas alturas puede sonar un poco raro."
    call BlinkXS4("c30s007_270") from _call_BlinkXS4_1268
    ama "¿Porque no he querido tener sexo contigo?"
    mc "No, no tiene nada que ver con el sexo."
    if kat._var("route"):
        mc "Tampoco he tenido sexo con [kat], y con ella no ha sonado raro."
    call BlinkXS4("c30s007_275") from _call_BlinkXS4_1269
    ama "Es que no me refiero a que me sienta como si estuviéramos casados. No sé lo que es estar casado más allá de las películas."
    ama "No he crecido en una familia... normal."
    mc "Lo sé. Yo tampoco." id c30s006_ama_50d8828a
    call BlinkXS4("c30s007_280") from _call_BlinkXS4_1270
    ama "Sé que quiero pasar cada momento libre contigo. Sé que me levanto y me acuesto pensando en ti."
    ama "Pensando en que tenemos un mes por delante en Aruba para nosotros solos. Cuando el trabajo nos deje tiempo libre."
    mc "Eso se parece bastante a un matrimonio. Al menos a unos recién casados. Y el viaje a Aruba parece una luna de miel. Mientras trabajamos."
    call BlinkXS4("c30s007_285") from _call_BlinkXS4_1271
    ama "Pero, por mucho que he pensado, no se me ha ocurrido un tatuaje que representara lo que siento."
    ama "Sólo se me ocurría un anillo... Pero me parecía... No sé... No me parecía correcto."
    if weddings > 0:
        ama "Y no quiero decir que no haya sido correcto si alguna chica se ha tatuado un anillo. Pero no lo era para mí."
        ama "No he querido que nadie me enseñara su tatuaje para que no me pidiera ver el mío."
    mc "Lo entiendo. Un anillo tiene que significar algo. Si no significa nada, sólo es un trozo de metal. O un círculo tatuado."
    call BlinkXS4("c30s007_290") from _call_BlinkXS4_1272
    ama "A eso me refiero. Un anillo no significaría nada entre nosotros. Tenemos que crear recuerdos para encontrar algo que sea significativo."
    mc "Yo tengo muchos recuerdos contigo, [ama]."
    call BlinkXS4("c30s007_295") from _call_BlinkXS4_1273
    ama "Lo sé. Podría enumerar cien, pero ninguno sería 100%% nuestro."
    ama "Ahí detrás, cuando me puse a llorar como una tonta, abrumada por las emociones, tú viniste a salvarme. Pero lloré por ellas, por todos vosotros."
    ama "En la puerta del garaje, cuando me diste el primer abrazo el día que vinimos con Aaron."
    ama "En el café, cuando me besaste por primera vez mientras hablábamos de la empresa, mientras mirábamos datos en el portátil."
    ama "En tu cama, el día que se rompió..."
    mc "El día que Zeus la rompió."
    call BlinkXS4("c30s007_300") from _call_BlinkXS4_1274
    ama "*Risa* El día que siete mujeres en tu cama la rompimos."
    "La primera vez que [ama] se ríe desde que os habéis visto suena mejor que cualquier sinfonía de la historia. ¡Chúpate esa, Beethoven!"
    mc "*Risa* Siete mujeres y un gato."
    ama "*Risa* OK. El día que siete mujeres y un gato rompimos tu cama."
    mc "*Risa* Eso me parece mejor."
    mc "Veo lo que quieres decir. En nuestros recuerdos siempre está la familia."
    call BlinkXS4("c30s007_305") from _call_BlinkXS4_1275
    ama "Y por eso no me he tatuado nada. No me voy a tatuar a Zeus ni a Aaron. No me voy a tatuar a las otras seis mujeres que rompimos tu cama o un portátil."
    ama "Quizás pueda hacerlo el día que tengamos un recuerdo solo nuestro. Pero no hoy."
    mc "Lo entiendo. Y no hace falta que digas que te sientes..."
    scene c30s007_305d with dissolve
    "Sin dejarte acabar la frase, la preciosa mercenaria te da un tierno beso."
    "Es solo el roce de sus labios sobre los tuyos, pero comunica más de lo que ningún tatuaje podría hacer en su caso."
    stop music fadeout (1.5)
    "El beso dura unos breves segundos. Se hace corto. Pero ninguno necesitáis más por el momento."
    stop music
    call BlinkXS4("c30s007_310") from _call_BlinkXS4_1276
    play sound ("music/wedding-march-music-box.ogg")
    ama "Con este beso me declaro tu esposa, [mc]."
    $ ama._var("engaged", True)
    ama "Algún día me haré un tatuaje para poder mostrarlo."
    mc "¿Ese beso no te parece suficiente forma de mostrarlo?"
    mc "Se puede mostrar amor de muchas formas diferentes. No es necesario un tatuaje, ni un anillo, ni firmar un papel."
    mc "Desde este momento me considero tu esposo, [ama]."
    scene c30s007_305d with dissolve
    "Os volvéis a besar. Como marido y mujer esta vez. La primera vez de muchas. Y cada vez os besaréis como si fuera la última."
    "Y un minuto, una hora, o un día después, os alegraréis de que aquella no fuera la última vez cuando os volváis a besar."
    stop sound fadeout (1.0)
    "Os esperan muchos besos en Aruba. Os esperan muchos besos el resto de vuestras vidas."
    call BlinkXS4("c30s007_315") from _call_BlinkXS4_1277
    play music ("music/Rise-Up.ogg")
    ama "*Risita* A veces odio a esta familia."
    mc "*Risa* ¿Qué ha pasado?"
    call BlinkXS4("c30s007_320a") from _call_BlinkXS4_1278
    ama "A una de nosotras se le ocurre una idea y parece que todas estamos obligadas a seguirla..."
    mc "Acabas de demostrar con la falta de tatuajes que no es necesario seguir una idea que no te guste o con la que no estés de acuerdo."
    call BlinkXS4("c30s007_320b") from _call_BlinkXS4_1279
    ama "A veces es complicado no seguir al grupo..."
    mc "¿Te acuerdas de cuando [eva] se disfrazó de [dap] para intentar engañarme?"
    call BlinkXS4("c30s007_320c") from _call_BlinkXS4_1280
    ama "Sí..."
    mc "¿Por qué lo hizo?"
    ama "Para reafirmar su individualidad."
    mc "También se puede reafirmar la individualidad rechazando seguir a la manada, [ama]."
    mc "Cada una de las mujeres de esta familia sois individuos y debéis tomar vuestras decisiones."
    mc "A veces, una de esas decisiones puede ser ir en una dirección diferente a la manada."
    call BlinkXS4("c30s007_320d") from _call_BlinkXS4_1281
    ama "*Risa* Dices 'manada' como si fuéramos unas lobas. La mayoría de gente diría rebaño en ese contexto."
    mc "*Risa* Sois mis lobas, [ama]. Aún me extraña que no haya habido ninguna lucha para saber quién es la alfa."
    ama "*Risa* No hacen falta luchas. Las alfas son [mar] y [nor]. Todas lo sabemos."
    if weddings == 0 or not frase:
        call BlinkXS4("c30s007_325") from _call_BlinkXS4_1282
        if weddings == 0:
            mc "Por cierto, no hubiera tenido ninguna queja si te hubieras hecho el tatuaje, pero... ¿qué hubiera pasado si no me hubiera gustado la idea?"
            ama "Como tú has dicho varias veces, hay que aceptar a todo el mundo como es."
            ama "Si hubiera encontrado algo que nos representara, te hubiera tocado aceptarme con un tatuaje."
            mc "*Risa* Me parece justo."
        else:
            call c30s006_sentence (ama) from _call_c30s006_sentence_19
    $ weddings = weddings + 1
    if not orangutan:
        call BlinkXS4("c30s007_330") from _call_BlinkXS4_1283
        mc "Pero no acabo de entender por qué un tatuaje."
        ama "Las chicas dijeron que no lo podríamos perder y que sería para siempre."
        if mc._var("relationships") > 1:
            ama "Además, nunca nos podríamos poner de acuerdo en qué modelo de anillo queremos. Lo que significa que deberías llevar un anillo diferente por cada chica."
            ama "Si sigues añadiendo chicas al harén, acabarías arrastrando los brazos como un orangután, debido al peso de los anillos."
            ama "Y, además, cada una de nosotras podíamos personalizarlo para que significara algo único."
        else:
            ama "Un anillo podría servir para una boda... oficial. Un tatuaje nos hace únicos hasta cierto punto."
            ama "Por eso no he podido hacerlo."
    call BlinkXS4("c30s007_335") from _call_BlinkXS4_1284
    ama "Ahora deberíamos ir a la fiesta. Nos deben estar esperando."
    mc "Y todas querrán saber qué te has tatuado."
    ama "Y, gracias a esta conversación, no me sentiré como una tonta diciéndoles que no me he tatuado nada."
    mc "Esa es la actitud, cielo."
    scene c30s007_305d with dissolve
    "Os volvéis a besar antes de dirigiros a la fiesta. Hace más de un minuto de vuestro último beso."
    "Alguna vez has intentado aguantar la respiración más de un minuto. Todos los niños lo han hecho alguna vez. La presión en los pulmones se hace dolorosa."
    "La falta de contacto con los labios de [ama] parece más dolorosa que la falta de oxígeno."
    scene c30s007_305e with dissolve
    "Desde que te ha besado por primera vez no ha soltado tus manos, como si fueran un ancla a un sueño del que no quiere despertar."
    scene c30s007_255e with dissolve
    "Cuando vuestros labios se sacian de los labios del otro os dirigís a la fiesta."
    "La saciedad durará un minuto. Por suerte, su mano sigue en la tuya."
    stop music fadeout (1.5)
    "Sigues siendo su ancla. Ella es la tuya."
    return
label c30s007_convJamaal1:
    jam "Está demasiado cansada después de lo de hoy. Me ha dicho que le encantaría, pero que la boda ya ha sido demasiado rápida."
    jam "Tener sexo de recién casados estando cansados no es una buena idea y estoy de acuerdo."
    return
label c30s007_convJamaal2:
    jam "¿A quién vas a elegir para pasar la noche y a quién vas a ofender sin elegirla?"
    jam "No creo que sea una buena forma de empezar vuestros matrimonios."
    return
label c30s007_MeeBetAtHome:
    if _in_replay:
        $ mc._var("relationships", 0, "set")
        call mrS3_sai_route from _call_mrS3_sai_route_22
        call mrS3_mar_route from _call_mrS3_mar_route_46
        call mrS3_emm_route from _call_mrS3_emm_route_45
        call mrS3_eri_route from _call_mrS3_eri_route_35
        call mrS3_nor_route from _call_mrS3_nor_route_34
        call mrS3_dap_route from _call_mrS3_dap_route_35
        call mrS3_sca_route from _call_mrS3_sca_route_29
        call mrS3_eil_route from _call_mrS3_eil_route_26
        call mrS3_sam_route from _call_mrS3_sam_route_24
        call mrS3_sim_route from _call_mrS3_sim_route_24
        call mrS3_oma_route from _call_mrS3_oma_route_19
        call mrS3_eva_route from _call_mrS3_eva_route_20
        call mrS3_mad_route from _call_mrS3_mad_route_20
        call mrS3_meg_route from _call_mrS3_meg_route_10
        call mrS3_ama_route from _call_mrS3_ama_route_17
        call mrS3_mee_route from _call_mrS3_mee_route_15
        call mrS3_kim_route from _call_mrS3_kim_route_15
        call mrS3_kat_route from _call_mrS3_kat_route_7
        call mrS3_deb_route from _call_mrS3_deb_route_29
        call mrS3_lis_route from _call_mrS3_lis_route_26
        call mrS3_bet_route from _call_mrS3_bet_route_12
        call mrS3_kia_route from _call_mrS3_kia_route_19
    scene c30s007_350a with fade
    "Al llegar a la cocina de [nor], te diriges a dar la bienvenida oficial a [mee] y a [bet]."
    play music ("music/PositiveWoman.ogg")
    $ actualizarPerfiles = False
    if not mee._var("route"):
        $ actualizarPerfiles = True
        if not _in_replay:
            $ mee.profileImages.insert (15, ("mad_15", None))
        call addProfileImageNoNotification (15, "mee_15", mee) from _call_addProfileImageNoNotification_171
    if not bet._var("route"):
        $ actualizarPerfiles = True
        if not _in_replay:
            $ bet.profileImages.insert (15, ("mad_15", None))
        call addProfileImageNoNotification (15, "bet_15", bet) from _call_addProfileImageNoNotification_172
    if not sai._var("route"):
        $ actualizarPerfiles = True
        if not _in_replay:
            $ sai.profileImages.insert (15, ("mad_15", None))
        call addProfileImageNoNotification (15, "sai_15", sai) from _call_addProfileImageNoNotification_173
    if not mar._var("route"):
        $ actualizarPerfiles = True
        if not _in_replay:
            $ mar.profileImages.insert (15, ("mad_15", None))
        call addProfileImageNoNotification (15, "mar_15", mar) from _call_addProfileImageNoNotification_174
    if not emm._var("route"):
        $ actualizarPerfiles = True
        if not _in_replay:
            $ emm.profileImages.insert (15, ("mad_15", None))
        call addProfileImageNoNotification (15, "emm_15", emm) from _call_addProfileImageNoNotification_175
    if not eri._var("route"):
        $ actualizarPerfiles = True
        if not _in_replay:
            $ eri.profileImages.insert (15, ("mad_15", None))
        call addProfileImageNoNotification (15, "eri_15", eri) from _call_addProfileImageNoNotification_176
    if not dap._var("route"):
        $ actualizarPerfiles = True
        if not _in_replay:
            $ dap.profileImages.insert (15, ("mad_15", None))
        call addProfileImageNoNotification (15, "dap_15", dap) from _call_addProfileImageNoNotification_177
    if not sca._var("route"):
        $ actualizarPerfiles = True
        if not _in_replay:
            $ sca.profileImages.insert (15, ("mad_15", None))
        call addProfileImageNoNotification (15, "sca_15", sca) from _call_addProfileImageNoNotification_178
    if not eil._var("route"):
        $ actualizarPerfiles = True
        if not _in_replay:
            $ eil.profileImages.insert (15, ("mad_15", None))
        call addProfileImageNoNotification (15, "eil_15", eil) from _call_addProfileImageNoNotification_179
    if not sam._var("route"):
        $ actualizarPerfiles = True
        if not _in_replay:
            $ sam.profileImages.insert (15, ("mad_15", None))
        call addProfileImageNoNotification (15, "sam_15", sam) from _call_addProfileImageNoNotification_180
    if not sim._var("route"):
        $ actualizarPerfiles = True
        if not _in_replay:
            $ sim.profileImages.insert (15, ("mad_15", None))
        call addProfileImageNoNotification (15, "sim_15", sim) from _call_addProfileImageNoNotification_181
    if not oma._var("route"):
        $ actualizarPerfiles = True
        if not _in_replay:
            $ oma.profileImages.insert (15, ("mad_15", None))
        call addProfileImageNoNotification (15, "oma_15", oma) from _call_addProfileImageNoNotification_182
    if not eva._var("route"):
        $ actualizarPerfiles = True
        if not _in_replay:
            $ eva.profileImages.insert (15, ("mad_15", None))
        call addProfileImageNoNotification (15, "eva_15", eva) from _call_addProfileImageNoNotification_183
    if not mad._var("route"):
        $ actualizarPerfiles = True
        if not _in_replay:
            $ mad.profileImages.insert (15, ("mad_15", None))
        call addProfileImageNoNotification (15, "mad_15", mad) from _call_addProfileImageNoNotification_184
    if not meg._var("route"):
        $ actualizarPerfiles = True
        if not _in_replay:
            $ meg.profileImages.insert (15, ("mad_15", None))
        call addProfileImageNoNotification (15, "meg_15", meg) from _call_addProfileImageNoNotification_185
    if not ama._var("route"):
        $ actualizarPerfiles = True
        if not _in_replay:
            $ ama.profileImages.insert (15, ("mad_15", None))
        call addProfileImageNoNotification (15, "ama_15", ama) from _call_addProfileImageNoNotification_186
    if not kim._var("route"):
        $ actualizarPerfiles = True
        if not _in_replay:
            $ kim.profileImages.insert (15, ("mad_15", None))
        call addProfileImageNoNotification (15, "kim_15", kim) from _call_addProfileImageNoNotification_187
    if not kat._var("route"):
        $ actualizarPerfiles = True
        if not _in_replay:
            $ kat.profileImages.insert (15, ("mad_15", None))
        call addProfileImageNoNotification (15, "kat_15", kat) from _call_addProfileImageNoNotification_188
    if not deb._var("route"):
        $ actualizarPerfiles = True
        if not _in_replay:
            $ deb.profileImages.insert (15, ("mad_15", None))
        call addProfileImageNoNotification (15, "deb_15", deb) from _call_addProfileImageNoNotification_189
    if not lis._var("route"):
        $ actualizarPerfiles = True
        if not _in_replay:
            $ lis.profileImages.insert (15, ("mad_15", None))
        call addProfileImageNoNotification (15, "lis_15", lis) from _call_addProfileImageNoNotification_190
    if not kia._var("route"):
        $ actualizarPerfiles = True
        if not _in_replay:
            $ kia.profileImages.insert (15, ("mad_15", None))
        call addProfileImageNoNotification (15, "kia_15", kia) from _call_addProfileImageNoNotification_191
    if mee._var("route") and bet._var("route"):
        "Ya las has saludado individualmente durante vuestras bodas, pero no habéis hablado de su viaje."
    elif mee._var("route"):
        "Ya has saludado a [mee] durante vuestra boda, pero no habéis hablado de su viaje y es el momento de saludar también a [bet]."
        mc "Bienvenida de vuelta a casa, Tía [bet]."
    elif bet._var("route"):
        "Ya has saludado a [bet] durante vuestra boda, pero no habéis hablado de su viaje y es el momento de saludar también a [mee]."
        mc "Bienvenida de vuelta a casa, Meemaw."
    else:
        "No las has visto aún desde que Jamaal y tú habéis llegado a casa."
        if mc._var("relationships")>0:
            "El buitre carroñero te ha mantenido ocupado."
        mc "Bienvenidas de vuelta a casa."
    mc "Me tenéis que explicar qué tal ha ido el viaje."
    bet "Todo ha ido bien, pero os echaba de menos a vosotros y la pizza de Gino's. La pizza que pedíamos en Florida no era tan buena."
    mee "Aparte de que [bet] acabara con las existencias de pizza del estado, todo ha ido bien."
    mee "La casa ya está en venta y nuestras cosas llegarán el viernes."
    mc "Pero [bet] no estará aquí..."
    scene c30s007_350b with dissolve
    bet "No te preocupes, no tenía gran cosa allí. Algunos hábitos y algo de ropa que... ya no es de mi estilo."
    mee "Creo que [bet] ha descubierto su gusto por vestidos... demasiado cortos para su edad."
    mc "No creo que la longitud del vestido tenga nada que ver con la edad, Meemaw."
    if bet._var("route"):
        mc "Y, aunque se puede defender ella sola si cree que la estás atacando, creo que no debería permitirte que criticaras a mi esposa por cómo se viste."
        if mee._var("route"):
            mc "Igual que no permitiría que nadie te criticara a ti por cómo vistes."
            mc "En los dos casos me encanta como vestís mis esposas. Cada una de vosotras está genial en vuestro estilo."
        else:
            mc "Además, me encanta el cambio de vestuario que ha hecho Tía [bet]."
    scene c30s007_350c with dissolve #llega al F
    bet "No le hagas caso. Ha pasado unos días alejada de la familia y ya cree que nos puede mangonear a todas otra vez."
    mee "¡Eso no es cierto!"
    mc "*Risa* Parece que sí que lo es. Que no te gusta cómo viste tu hermana pequeña ha sido casi lo primero que me has dicho."
    mc "*Risa* Mientras no empieces a meterte con el peso de [nor] o con cómo tiene organizada la casa..."
    call BlinkXS4("c30s007_355") from _call_BlinkXS4_1285
    mee "¿Estoy volviendo a ser esa [mee] otra vez?"
    mc "No lo creo, además no te van a permitir que vuelvas a ser esa versión de ti misma."
    mc "Y, si lo intentas, habrá 19 mujeres y un buitre negro para ponerte en tu sitio cuando yo no esté."
    call BlinkXS4("c30s007_360") from _call_BlinkXS4_1286
    bet "No critiques al buitre negro... ¡Mierda! *Risa* A Jamaal. Al final conseguirás que todas lo llamemos buitre."
    if mc._var("relationships")>0:
        bet "Ha hecho un buen trabajo como maestro de ceremonias."
    else:
        bet "La idea de esta fiesta fue parcialmente suya, por lo que me han dicho."
    mc "*Risa* Cuando empiece a robar comida entenderás por qué lo llamo buitre."
    scene c30s007_365d with dissolve #mano de eri coje MC
    eri "Os voy a robar a [mc]."
    scene c30s007_350d with dissolve
    stop music fadeout (1.5)
    mee "¡Acaba de llegar, jovencita!"
    bet "Creo que sé por qué se lo va a llevar."
    call BlinkXS4("c30s007_365") from _call_BlinkXS4_1287
    play music ("music/MorningFunnyBeat.ogg")
    eri "[meg] y [sam.nick] se van a tener que ir en breve y no se van a quedar a cenar. Las dos trabajan esta noche."
    eri "Ninguna de las dos quiere irse sin despedirse de [mc] por si no lo ven antes de que vuele a Aruba."
    mc "¿Y te han mandado a ti a buscarme?"
    call BlinkXS4("c30s007_370") from _call_BlinkXS4_1288
    eri "*Risa* No, me he prestado voluntaria. A [sam.nick] le da miedo la abuela y no se atrevía. Y [meg] está demasiado ocupada metiéndose con Jamaal."
    scene c30s007_350e with dissolve
    mee "*Risa* ¿Le doy miedo a [sam.nick]? ¡Tendré que pasar más tiempo con ella para que cambie de opinión!"
    bet "*Risa* Eso ha sonado a amenaza."
    mc "*Risa* Creo que acabo de oír el coche de [sam.nick] chirriando ruedas mientras se va a toda velocidad."
    mc "Bueno, señoras, os veo más tarde."
    scene c30s007_350f with dissolve
    mee "Hasta luego, [mc]."
    bet "Pásalo bien, [mc]."
    scene c30s007_375a with fade
    call BlinkXS4("c30s007_375") from _call_BlinkXS4_1289
    mc "¿De verdad [sam.nick] tiene miedo de Meemaw?"
    eri "Más que miedo, le infunde un tremendo desasosiego. Piensa que no han coincidido demasiado desde aquel día en la playa. Dos o tres veces."
    eri "[sam.nick] no ha experimentado de primera mano lo mucho que ha cambiado la abuela."
    mc "Tienes razón. Supongo que, a partir de ahora, será diferente, con todo el mundo definitivamente en Newport."
    call BlinkXS4("c30s007_380") from _call_BlinkXS4_1290
    eri "Bueno... No todo el mundo..."
    mc "Vale, sí. [ama], Tía [bet] y yo nos vamos un tiempo... y después [eva], pero ya habrá vuelto Tía [bet] seguramente..."
    mc "A lo que me refiero es a que casi todas vosotras vais a estar aquí y vais a tener más tiempo para conoceros."
    mc "Además, os vais a tener que ayudar entre vosotras cuando yo no esté."
    call BlinkXS4("c30s007_385") from _call_BlinkXS4_1291
    eri "Lo sé. Pero va a ser difícil no tenerte aquí. Ni a [ama], [eva], o Tía [bet]."
    mc "También va a ser difícil para nosotros. Pero yo me voy tranquilo. Sé que tú vas a ayudar a mantener la paz en casa y a que todo el mundo se comporte."
    call BlinkXS4("c30s007_390") from _call_BlinkXS4_1292
    eri "¡Estás poniendo mucha responsabilidad sobre mis hombros!"
    mc "*Risa* Y aún no te he dicho que vas a ser una de las principales encargadas de que las chicas nuevas se integren bien."
    call BlinkXS4("c30s007_395") from _call_BlinkXS4_1293
    eri "*Risa* No creo que haya demasiados problemas. Están hablando mucho en el grupo de WhatsUp que propusiste hacer con ellas."
    mc "¿Cómo lo sabes?"
    call BlinkXS4("c30s007_400") from _call_BlinkXS4_1294
    eri "¿Te acuerdas de lo que dije sobre que escribiría a [zoe] sobre su maquillaje? Hemos hablado mucho, y me ha metido en el grupo."
    eri "Ahora hablo con todas. Son buenas chicas y, como te he dicho, no creo que haya muchos problemas."
    mc "Ahora entiendes por qué te estoy dando la responsabilidad de mantener todo en su sitio, ¿verdad?"
    call BlinkXS4("c30s007_405") from _call_BlinkXS4_1295
    eri "Lo entiendo. Intentaré hacer un buen trabajo."
    eri "Y mi trabajo empieza por mandarte con [sam.nick]. Ahí está."
    stop music fadeout (1.5)
    mc "Te veo luego, [eri]."
    eri "Resérvame un baile."
    scene c30s007_410a with fade
    call BlinkXS4("c30s007_410") from _call_BlinkXS4_1296
    play music ("music/Bolero.ogg")
    mc "[eri] me ha dicho que te vas. ¿Tan pronto?"
    sam "Tengo que ir al hospital. Mi turno empieza en poco más de una hora."
    sam "Pero no quería irme sin tener un baile contigo."
    sam "Creo que esta fiesta es tanto una bienvenida para [mee] y [bet] como una despedida para [ama], [bet], y tú."
    if mc._var("relationships") == 1:
        if sam._var("route"):
            mc "Y una celebración de nuestra boda..."
        else:
            mc "Y una celebración de mi boda..."
    elif mc._var("relationships") > 1:
        mc "Y una celebración de mis bodas..."
    else:
        mc "Eso parece, aunque aún nos quedan un par de días para irnos."
    if mc._var("relationships") > 0:
        mc "Aunque a nosotros aún nos quedan un par de días para irnos."
    call BlinkXS4("c30s007_415") from _call_BlinkXS4_1297
    sam "Un par de días pasan demasiado rápido. No sé si todas os vamos a poder ver antes de que os vayáis."
    if sam._var("route"):
        mc "¿Eso quiere decir que no vamos a tener noche de bodas?"
        call BlinkXS4("c30s007_420") from _call_BlinkXS4_1298
        sam "*Risa* Tengo que mirar mi agenda. Es broma. No te preocupes, estoy segura de que buscaremos un momento antes de que te vayas."
        mc "*Risa* Eso espero. Tengo muchas ganas de pasar tiempo a solas con mi esposa."
        mc "*Risa* Aunque me tenga que romper un brazo e ir al hospital a recibir un tratamiento especial."
    else:
        mc "Estoy seguro de que nos volveremos a ver antes de que nos vayamos. Aunque me tenga que romper un brazo para ir al hospital."
    call BlinkXS4("c30s007_425") from _call_BlinkXS4_1299
    stop music fadeout (1.5)
    sam "*Risa* Mejor que no te rompas ningún brazo. Y ahora, vamos a bailar. Me encanta esta canción."
    scene c30s007_430An1
    play music ("music/RhythmPlay.ogg")
    "Bailas con [sam] y con [meg] antes de que se vayan."
    "Después pasas de una chica a otra sin tener un momento de pausa."
    "Todas quieren tener un último baile contigo y no dejan que bailes más de una canción seguida con otra chica."
    if mc._var("relationships") > 1:
        "Las conversaciones mientras bailáis tratan sobre las bodas y sobre lo mucho que os vais a echar de menos."
    elif mc._var("relationships") == 1:
        "Las conversaciones mientras bailáis tratan sobre la boda y sobre lo mucho que os vais a echar de menos."
    else:
        "Las conversaciones mientras bailáis tratan sobre lo mucho que os vais a echar de menos."
    "Es un contraste de felicidad y tristeza entremezclado."
    "Es una fiesta de bienvenida y de despedida."
    stop music fadeout (1.5)
    scene c30s007_435a with fade
    call BlinkXS4("c30s007_435") from _call_BlinkXS4_1300
    $ texto = __("Imágenes de perfil actualizadas")
    if actualizarPerfiles:
        $ renpy.notify (texto)
    "Para cuando te dejan descansar, estás hambriento. Te diriges a donde está Jamaal. Seguro que hay comida cerca. Si no se la ha acabado..."
    play music ("music/SneakySnitch.ogg")
    mc "¿Queda algo para comer? ¿O te lo has comido todo?"
    jam "Creo que no voy a contestar a esa acusación infundada."
    jam "Pero no queda nada, a menos que quieras comer helado del que hizo [mee] o algo de la nevera. El helado está sorprendentemente bueno."
    mc "*Risa* Come, come. No dejes nada para los demás."
    if mc._var("relationships") > 0:
        call BlinkXS4("c30s007_440") from _call_BlinkXS4_1301
        jam "¿Qué te ha parecido la sorpresa?"
        mc "Ha estado genial, pero me hubiera gustado que durase más."
        mc "Se ha hecho muy corto. Ha sido casi un 'llego, charlamos un poco, se declara mi esposa, y me voy'"
        if mc._var("relationships")>1:
            mc "Y vuelve a repetir. Los detalles se mezclan en mi cabeza."
        call BlinkXS4("c30s007_445") from _call_BlinkXS4_1302
        jam "No podíamos alargarlo más o la fiesta de bienvenida no hubiera empezado nunca."
        jam "Y mi madre y [meg] se tenían que ir a trabajar."
        mc "Entiendo por qué ha tenido que ser así y me encanta que haya pasado."
        mc "Pero quizás lo hubiera planeado de otra forma si lo hubiera sabido."
        call BlinkXS4("c30s007_450") from _call_BlinkXS4_1303
        jam "Sé cómo lo hubieras planeado tú, y era imposible."
        mc "*Risa* Ilústrame sobre lo que tu bola de cristal te ha dicho sobre mis planes."
        call BlinkXS4("c30s007_455") from _call_BlinkXS4_1304
        if mc._var("relationships")==1:
            jam "Hubieras querido dedicar un día entero a la boda."
        else:
            jam "Hubieras querido dedicar un día entero a cada una de las bodas."
        mc "Es lo lógico, y lo mínimo que deberíamos haber hecho."
        call BlinkXS4("c30s007_460") from _call_BlinkXS4_1305
        jam "Pero te vas dentro de dos días. No hubiera habido tiempo para organizarlo."
        $ bodas = mc._var("relationships")
        if mc._var("relationships")>1:
            jam "Ni tiempo para hacerlo. ¿[bodas] bodas en dos días y además preparar el viaje?"
            jam "Además, ¿con quién te casas primero? ¿Cuál de tus chicas tiene una muerte dolorosa porque la has elegido la primera?"
            jam "Y todas querrían estar en todas las bodas, y hoy era el único día en que todo el mundo tenía un rato libre."
        mc "Tienes razón... Y no te voy a comprar una camiseta que ponga que siempre tienes razón. Esa es para mí."
        call BlinkXS4("c30s007_465") from _call_BlinkXS4_1306
        jam "*Risa* No necesito una camiseta. Esta adorable cara dice todo lo que es necesario decir."
        mc "*Risa* Lo que dice esa cara es que eres un comilón que me ha dejado sin cenar."
        if not kat._var("route"):
            call BlinkXS4("c30s007_470") from _call_BlinkXS4_1307
            jam "*Risa* Al menos no vas a necesitar energía para la noche de bodas."
            mc "¿Qué? ¿Por qué?"
            call BlinkXS4("c30s007_475") from _call_BlinkXS4_1308
            if mc._var("relationships")==1:
                if sam._var("route") or meg._var("route"):
                    jam "*Risa* ¡Porque se ha ido a trabajar, idiota!"
                else:
                    call c30s007_convJamaal1 from _call_c30s007_convJamaal1
            elif mc._var("relationships")==2:
                if sam._var("route") and meg._var("route"):
                    jam "*Risa* ¡Porque se han ido a trabajar, idiota!"
                elif sam._var("route") or meg._var("route"):
                    jam "Una se ha ido a trabajar, y la otra..."
                    call c30s007_convJamaal1 from _call_c30s007_convJamaal1_1
                else:
                    call c30s007_convJamaal2 from _call_c30s007_convJamaal2
            elif mc._var("relationships")==3:
                if sam._var("route") and meg._var("route"):
                    jam "*Risa* ¡Porque se han ido a trabajar, idiota! Y la otra..."
                    call c30s007_convJamaal1 from _call_c30s007_convJamaal1_2
                else:
                    call c30s007_convJamaal2 from _call_c30s007_convJamaal2_1
            else:
                call c30s007_convJamaal2 from _call_c30s007_convJamaal2_2
        else:
            call BlinkXS4("c30s007_470") from _call_BlinkXS4_1309
            jam "*Risa* Pues vas a necesitar energía para la noche de bodas."
            mc "¿También habéis planeado mi noche de bodas?"
            if mc._var("relationships")>1:
                mc "No sabría a quién elegir. Quien no fuera elegida se podría sentir mal."
                call BlinkXS4("c30s007_475") from _call_BlinkXS4_1310
                jam "Solo había una buena opción para hoy, y no me hagas decir quién es si no eres capaz de deducirlo."
                jam "Todas tus esposas se han puesto de acuerdo, con lo que no tienes que preocuparte."
            else:
                call BlinkXS4("c30s007_475") from _call_BlinkXS4_1311
                jam "¿Acaso tienes algo mejor que hacer?"
        mc "Me voy a arrepentir de decir esto, pero tienes razón una vez más."
        if eil._var("route"):
            call BlinkXS4("c30s007_485b") from _call_BlinkXS4_1312
            jam "Por cierto, estoy muy decepcionado."
            mc "¿Por qué? ¿Qué he hecho ahora?"
            jam "No es contigo. [eil] me prometió que os podría casar yo cuando estábamos en el instituto."
            jam "Incluso me saqué un título de sacerdote por la Iglesia Unificada de la Lasaña."
            mc "*Risa* Lo hemos comentado durante nuestra boda. Los dos temíamos que aparecieras con una túnica."
            mc "*Risa* Y los dos nos hemos alegrado de que no lo hicieras."
            call BlinkXS4("c30s007_485c") from _call_BlinkXS4_1313
            jam "Los dos sois unos malos amigos. Me hacía ilusión hacerlo..."
            mc "*Risa* Tendrías que verte la cara de niño con una pataleta ahora mismo."
            mc "Te prometo que hablaré con [eil] para que oficies la renovación de votos. Pero ella tiene que aceptar."
            call BlinkXS4("c30s007_485d") from _call_BlinkXS4_1314
            jam "*Risa* Eso me sirve. Si la bruja pelirroja no acepta, sé secretos que les puedo contar a las otras chicas."
            mc "*Risa* Creo que pasas demasiado tiempo con [sai]."
            mc "Yo que tú empezaría a pasar más tiempo con [ama] y [eva], para tener a alguien que te defienda de la furia de [eil] si lo intentas."
    scene c30s007_470An
    "Pasas un rato charlando con Jamaal sobre la fiesta, sobre Anthony, sobre tu viaje a Aruba, y sobre mil otras cosas."
    if mc._var("relationships")>0:
        "Obviamente también sobre su papel como maestro de ceremonias."
        "Se sorprende por haberse convertido en el tipo más odiado de la familia."
    stop music fadeout (1.5)
    "Entre la conversación y que Jamaal ha dado buena cuenta de toda la comida que había alrededor, no comes nada."
    call BlinkXS4("c30s007_480") from _call_BlinkXS4_1315
    play music ("music/CumbiaColombiana.ogg")
    oma "*Risa* Vengo a arrestarte, [mc]."
    mc "*Risa* ¿Qué he hecho ahora? ¿De qué se me acusa, Agente?"
    oma "*Risa* De dejar a 20 mujeres desatendidas. Ya te hemos dado un rato para que comieras algo. Te toca volver a bailar."
    call BlinkXS4("c30s007_485a") from _call_BlinkXS4_1316
    jam "*Risa* Ya has oído. Te han dado un rato para que comas. *Risa*"
    mc "*Risa* Puto comilón."
    scene c30s007_490a with fade
    call BlinkXS4("c30s007_490") from _call_BlinkXS4_1317
    oma "¿De qué iba eso?"
    mc "¿Has visto comida alrededor? Has dicho que me habíais dado tiempo para comer algo, pero Jamaal ha acabado con todo."
    call BlinkXS4("c30s007_495") from _call_BlinkXS4_1318
    oma "No me había dado cuenta. Te hemos secuestrado para bailar contigo y no te hemos dado tiempo de comer hasta ahora."
    oma "Nosotras hemos ido comiendo algo entre baile y baile contigo."
    mc "*Risa* Deberíais sacar a Jamaal a bailar cuando hay comida cerca. Así dejaría algo para los demás."
    call BlinkXS4("c30s007_500") from _call_BlinkXS4_1319
    oma "*Risa* Sería capaz de mordernos una mano si le separamos de la comida."
    oma "Pero no te preocupes, cuando acabe este baile iré con alguna de las chicas a prepararte algo para comer."
    mc "*Risa* No hace falta, de verdad. Puedo comer algo de fruta o algo de la nevera."
    call BlinkXS4("c30s007_505") from _call_BlinkXS4_1320
    oma "Pues casi me estás haciendo un favor. No me atrevería a cocinar con este vestido. Me lo ha prestado [nor] y no querría mancharlo."
    mc "Estás guapísima con él."
    if oma._var("route"):
        oma "No tenía ningún vestido blanco y, aunque nuestra boda haya sido corta, quería vestirme de blanco para hoy."
        if mee._var("route") or bet._var("route") or mar._var("route") or eil._var("route") or sai._var("route") or sca._var("route") or deb._var("route") or emm._var("route") or eri._var("route") or kia._var("route") or mad._var("route"):
            mc "No todas habéis elegido ir de blanco hoy."
            call BlinkXS4("c30s007_510") from _call_BlinkXS4_1321
            oma "Bueno, las hay que somos más tradicionales que otras. Aunque la boda no haya sido demasiado tradicional."
            if lis._var("route") or eva._var("route") or sim._var("route"):
                if lis._var("route"):
                    $ personaje = lis
                elif eva._var("route"):
                    $ personaje = eva
                else:
                    $ personaje = sim
                oma "Y después tienes a [personaje], que se ha vestido literalmente de novia."
    stop music fadeout (1.5)
    oma "Y ahora es el momento de que bailes con otra. Creo que el resto de las chicas me están mirando como lobas esperando su ración de [mc]."
    scene c30s007_430An2 with dissolve
    play music ("music/RhythmPlay.ogg")
    "Vuelves a bailar con las mujeres que aún están en casa y pasas el resto de la velada yendo de los brazos de una a los brazos de otra."
    "El cansancio empieza a hacer mella en todos vosotros, y cada chica te dice que es la última vez que baila contigo y que te van a dejar descansar."
    "Ninguna cumple su palabra y vuelves a encontrarte con ellas entre tus brazos al cabo de una hora o así."
    "20 mujeres. 20 canciones. Y vuelta a empezar."
    scene c30s007_510d with fade
    "Cuando se hace tarde, empiezan las despedidas de las chicas que se van a ir."
    "[oma] lleva a Jamaal, [sim] y [mad.nick] a casa. Los cuatro tienen que trabajar mañana y el comilón tiene que levantarse temprano."
    "[ama] y [eva] no abandonan la casa. Van a dormir con [mee] y [bet] respectivamente."
    scene black with dissolve
    "Tras ayudar a recoger la cocina de [nor], subes a tu habitación."
    stop music fadeout (1.5)
    "Ha sido un día alucinante."
    return
label c30s007_KatConv (route):
    scene c30s007_550e with fade
    "Al cabo de un rato..."
    play sound ("music/knock.ogg")
    "*Knock-Knock*"
    kat "*A través de la puerta* ¿Puedo pasar? Traigo comida."
    mc "*Risa* Adelante, [kat]."
    if route:
        scene c30s007_550d with fade:
            yalign 1.0
            linear 5.0 yalign 0.0
        pause (4.8)
        call BlinkXS3("c30s007_550") from _call_BlinkXS3_957
        call addProfileImageS3 (7, "kat_7", kat, __(": 15 - Especial"), "") from _call_addProfileImageS3_48
    else:
        call BlinkXS4("c30s007_555") from _call_BlinkXS4_1322
    kat "Me han dicho que Jamaal te ha dejado sin cenar... O entre Jamaal y nosotras."
    kat "Te he hecho unos gofres. No sabía si te gustaban con nata o con chocolate, con lo que traigo de los dos."

    if route:
        kat "No puedo permitir que mi marido pase hambre, ¿no?"
        mc "Creo que, ahora mismo, del único gofre que tengo hambre es del que llevas tatuado en el hombro."
        kat "*Risita* El gofre está lo suficientemente cerca del cuello... Eso hace que esa propuesta resulte MUY tentadora."
    else:
        mc "Gracias, [kat]."
        kat "Te dejo que te los comas antes de que se enfríen, y me voy a la cama. Hasta mañana."
        mc "Hasta mañana, [kat]."
    return
label c30s007_KatLewd:
    if _in_replay:
        $ kat._var("route", True)
    call c30s007_KatConv (True) from _call_c30s007_KatConv
    return
label c30s007_noKatLewd:
    if _in_replay:
        $ kat._var("route", False)
    call c30s007_KatConv (False) from _call_c30s007_KatConv_1
    return

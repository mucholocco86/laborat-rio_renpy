label c22:
    default gr = "{color=#17ff00}"
    default red = "{color=#ff0000}"
    default ora = "{color=#ff9300}"
    if dap._var("route") and emm._var("route") and eri._var("route"):
        $ emm._var("foursome", True)
    if nor._var("route"):
        call c22s001_NorSex from _call_c22s001_NorSex
    else:
        call c22s001_NoNorSex from _call_c22s001_NoNorSex
    call c22s002_EmmMarChat from _call_c22s002_EmmMarChat
    if mc._var("edmundsStory"):
        call c22s002_MarAboutEdmund from _call_c22s002_MarAboutEdmund
    call c22s002_MeemawMassage from _call_c22s002_MeemawMassage
    call c22s003_AmaCalls from _call_c22s003_AmaCalls
    call c22s003_IronFistCalls from _call_c22s003_IronFistCalls
    call c22s004_EriPregnancyResult from _call_c22s004_EriPregnancyResult
    if eri._var("route") and persistent.pregnancy:
        call c22s004_EriPregnancy from _call_c22s004_EriPregnancy
    if mc._var("edmundsStory"):
        call c22s004_ScarlettDNA from _call_c22s004_ScarlettDNA
    else:
        call c22s004_ScarlettReveal from _call_c22s004_ScarlettReveal
    call c22s004_BetCallsBishop from _call_c22s004_BetCallsBishop
    if mc._var("edmundsStory"):
        call c22s004_MarChat from _call_c22s004_MarChat
    call c22s004_BookFerrarini from _call_c22s004_BookFerrarini
    call c22s005_SamCall from _call_c22s005_SamCall
    if sam._var("route"):
        call c22s005_SamSex from _call_c22s005_SamSex
    call c22s006_Simone from _call_c22s006_Simone
    call c22s007_LisChat from _call_c22s007_LisChat
    if mc._var("edmundsStory") or sca._var("route"):
        call c22s008_Sca from _call_c22s008_Sca
    else:
        call c22s008_NoSca from _call_c22s008_NoSca
    return
label c22s000_relationships:
    $ mc._var("relationships", 0, "set")
    if sai._var("route"):
        $ mc._var("relationships", 1, "add")
    if mar._var("route"):
        $ mc._var("relationships", 1, "add")
    if emm._var("route"):
        $ mc._var("relationships", 1, "add")
    if eri._var("route"):
        $ mc._var("relationships", 1, "add")
    if dap._var("route"):
        $ mc._var("relationships", 1, "add")
    if nor._var("route"):
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
    if mad._var("route"):
        $ mc._var("relationships", 1, "add")
    if meg._var("route"):
        $ mc._var("relationships", 1, "add")
    if deb._var("route"):
        $ mc._var("relationships", 1, "add")
    if kia._var("route"):
        $ mc._var("relationships", 1, "add")
    if ama._var("route"):
        $ mc._var("relationships", 1, "add")
    if eva._var("route"):
        $ mc._var("relationships", 1, "add")
    if lis._var("route"):
        $ mc._var("relationships", 1, "add")
    if mc._var("relationships")==1:
        call c22s000_gf from _call_c22s000_gf
    return
label c22s000_gf:
    if mar._var("route"):
        $ mc._var("girlfriend", mar.name.first_name)
    elif sai._var("route"):
        $ mc._var("girlfriend", sai.name.first_name)
    elif emm._var("route"):
        $ mc._var("girlfriend", emm.name.first_name)
    elif eri._var("route"):
        $ mc._var("girlfriend", eri.name.first_name)
    elif dap._var("route"):
        $ mc._var("girlfriend", dap.name.first_name)
    elif nor._var("route"):
        $ mc._var("girlfriend", nor.name.first_name)
    elif sca._var("route"):
        $ mc._var("girlfriend", sca.name.first_name)
    elif eil._var("route"):
        $ mc._var("girlfriend", eil.name.first_name)
    elif sam._var("route"):
        $ mc._var("girlfriend", sam.name.first_name)
    elif sim._var("route"):
        $ mc._var("girlfriend", sim.name.first_name)
    elif oma._var("route"):
        $ mc._var("girlfriend", oma.name.first_name)
    elif mad._var("route"):
        $ mc._var("girlfriend", mad.nick)
    elif meg._var("route"):
        $ mc._var("girlfriend", meg.name.first_name)
    elif deb._var("route"):
        $ mc._var("girlfriend", deb.nick)
    elif kia._var("route"):
        $ mc._var("girlfriend", kia.name.first_name)
    elif ama._var("route"):
        $ mc._var("girlfriend", ama.name.first_name)
    elif eva._var("route"):
        $ mc._var("girlfriend", eva.name.first_name)
    elif lis._var("route"):
        $ mc._var("girlfriend", lis.name.first_name)
    return
label c22s001_NorSex:
    call c22s000_relationships from _call_c22s000_relationships
    if _in_replay:
        call mrS3_rename from _call_mrS3_rename_10
        $ mc._var("relationships", 1, "set")
        call mrS3_nor_pregnant from _call_mrS3_nor_pregnant
        call mrS3_eri_route from _call_mrS3_eri_route_1
        call mrS3_meg_route from _call_mrS3_meg_route
        call mrS3_mee_route from _call_mrS3_mee_route
        if mc._var("relationships")<2:
            call mrs3_rels from _call_mrs3_rels
        call c21s006_Nor from _call_c21s006_Nor_1
    call BlinkXPS3 ("c21s006_020" , "d") from _call_BlinkXPS3_475
    play music ("music/Bolero.ogg")
    mc "Aunque creo que voy a quitártelo en breve."
    scene c22s001_005An with dissolve
    nor "No, [mc]. Hoy quiero ser yo la que te desnude a ti."
    mc "*Risa* Me da lo mismo el orden de los factores."
    call BlinkXPS3 ("c22s001_010" , "d") from _call_BlinkXPS3_476
    nor "Voy a empezar por la camisa. Creo que sobra."
    mc "*Risa* ¿Sin un beso o sin invitarme a cenar?"
    call BlinkXPS3 ("c22s001_015" , "d") from _call_BlinkXPS3_477
    nor "¿Tan ansioso estás por probar mi pintalabios?"
    mc "El pintalabios me da lo mismo. Te queda precioso, pero lo que me importa es lo que hay debajo."
    nor "Respuesta correcta."
    scene c22s001_155pv with dissolve
    show c22s001_155v
    "Una vez liberado de tu camisa, los labios de [nor] empiezan a recorrer los tuyos."
    "Su pintalabios sabe tan bien como siempre, pero no mentías cuando decías que lo que te importaba era lo que había debajo."
    "Sus labios carnosos, húmedos y calientes, aprietan apasionadamente los tuyos en un movimiento sin fin."
    "Esos labios que se separan para dejar salir a vuestras lenguas, que se encuentran a medio camino para un saludo largamente esperado."
    call BlinkXPS3 ("c22s001_020" , "d") from _call_BlinkXPS3_478
    hide c22s001_155v
    nor "¡Wow! Me encanta que dejes mis labios húmedos después de un beso como este."
    mc "Y a mí me encanta besar esos labios."
    call BlinkXPS3 ("c22s001_025" , "d") from _call_BlinkXPS3_479
    nor "*Risa* No me refería a ESTOS labios."
    mc "¡Oh! *Risa*"
    call BlinkXPS3 ("c22s001_030" , "d") from _call_BlinkXPS3_480
    nor "Ha llegado el momento de comprobar si a ti te ha producido el mismo efecto ese beso."
    mc "Si quieres te hago un spoiler... *Risa*"
    call BlinkXPS3 ("c22s001_035" , "d") from _call_BlinkXPS3_481
    nor "No hace falta. *Risa* Creo que lo puedo comprobar por mí misma."
    scene c22s001_035d with dissolve
    nor "Ayúdame con las deportivas."
    call BlinkXPS3 ("c22s001_040" , "d") from _call_BlinkXPS3_482
    nor "Y ahora los pantalones."
    mc "Ten cuidado. No quiero sacarte uno de esos preciosos ojos."
    call BlinkXPS3 ("c22s001_045" , "d") from _call_BlinkXPS3_483
    nor "*Risa* Te he dicho que nada de spoilers."
    mc "¡Oops! Lo siento."
    scene c22s001_050AnBlink with dissolve
    nor "No sé por qué me sorprendo cada vez que lo veo."
    nor "Siempre pienso que va a ser más pequeño que en mis recuerdos. Apóyate en el armario..."
    mc "No me pidas que la lije. *Risa* Es la única forma en que podría hacerlo más pequeño."
    call BlinkXPS3 ("c22s001_055" , "d") from _call_BlinkXPS3_484
    nor "*Risa* Por nada del mundo. He pasado años abriendo la boca para meterme comida."
    nor "Ahora la puedo abrir para esto."
    scene c22s001_100pv
    show c22s001_100va
    pause (0.66)
    scene c22s001_100dv
    hide c22s001_100va
    "[nor] se incorpora y engulle tu polla en un solo movimiento hasta que notas la entrada de su garganta en tu glande."
    mc "¡Ufff! Me encanta esa boca tuya, [nor]."
    "Sus labios se quedan unos segundos aprisionando la base de tu polla antes de empezar una profunda mamada."
    scene c22s001_110pv with dissolve
    show c22s001_110v
    if persistent.family:
        $ Nor = _("tu Tía")
        $ Aunt = _("Tía ")
    else:
        $ Nor = nor.name
        $ Aunt = ""
    "Nunca te puedes cansar de ver la cabeza de [Nor!t] subiendo y bajando, tragándose a Mjolnir como si fuera un helado."
    mc "Sigue así, [Aunt!t][nor]. Está siendo increíble."
    "Tampoco te cansarías nunca de ver su culo bamboleándose en cada recorrido. Un increíble culo."
    mc "Tienes un culo precioso, [Aunt!t][nor]. Todo en ti es precioso."
    nor "*Gemido agradecido*"
    scene c22s001_105pv with dissolve
    hide c22s001_110v
    show c22s001_105v
    "El culo de [Nor!t] es increíble. No tienes palabras para describirlo. Nunca hubieras pensado en ella así antes de irte a la universidad, pero ahora..."
    mc "Justo así, [Aunt!t][nor]. Lo estás haciendo perfecto."
    "Estabas tan acostumbrado a verla desnuda que nunca tuviste una erección con ella en la ducha."
    nor "*Jadeo*"
    "Y ahora jadea sobre tu polla como si fuera su plato favorito. Y tu polla reacciona poniéndose cada vez más dura."
    scene c22s001_100pv with dissolve
    hide c22s001_105v
    show c22s001_100v
    "Nunca hubieras imaginado por entonces que sus rojos labios aprisionarían a Mjolnir de esta forma."
    nor "*Gemido*"
    "Ella nunca se pintaba los labios por entonces. Ahora eres incapaz de imaginarte su hermoso rostro sin ese toque de carmín."
    nor "*Jadeo*"
    "Una historia de cariño entre tía y sobrino se ha convertido en una historia de amor."
    mc "[Aunt!t][nor], para o me voy a acabar corriendo..."
    call BlinkXPS3 ("c22s001_060" , "d") from _call_BlinkXPS3_485
    nor "Eso no lo podemos consentir, ¿verdad?"
    nor "Quiero que te corras dentro de mí."
    mc "Pues tendré que empezar a desnudarte, ¿no?"
    scene c22s001_065d with dissolve:
        yalign 1.0
        linear 5.0 yalign 0.0
    pause (5.0)
    call BlinkXPS3 ("c22s001_065" , "d") from _call_BlinkXPS3_486
    mc "No sé ni por donde empezar a desenvolver el regalo de navidad."
    mc "Me da miedo romperlo. *Risa*"
    nor "Lo he comprado para ti. *Risa* Si lo rompes no lo volverás a ver."
    nor "Se quita con el sujetador entero."
    scene c22s001_065An with dissolve
    mc "Asombroso."
    nor "¿El sistema para quitarlo o lo que escondía? *Risa*"
    mc "Ambos... *Risa* o los tres, teniendo en cuenta que escondían estas dos maravillas."
    call BlinkXPS3 ("c22s001_070" , "d") from _call_BlinkXPS3_487
    nor "Recuerdas cómo funciona esto, ¿no? *Risa* Hay otra pieza que quitar más abajo."
    mc "¿No me vas a dejar disfrutar de las vistas?"
    nor "Ya tendrás tiempo luego. Ahora quiero tenerte dentro de mí."
    mc "¿A qué viene tanta prisa? Tenemos toda la noche..."
    call BlinkXPS3 ("c22s001_075" , "d") from _call_BlinkXPS3_488
    nor "*Risa* A que no quiero que vengan unos secuestradores y nos interrumpan el segundo round como la última vez."
    mc "¿Lo dices en serio? ¿Te preocupa eso?"
    call BlinkXPS3 ("c22s001_080" , "d") from _call_BlinkXPS3_489
    nor "No, cielo. Era una broma."
    mc "Por un momento me habías asustado. Estrés postraumático y esas cosas."
    nor "No te preocupes, mi amor. Quizás no era el momento de hacer esa broma."
    call BlinkXPS3 ("c22s001_085" , "d") from _call_BlinkXPS3_490
    nor "Y, si no quieres que le pida el rodillo a [bet], hay unas bragas esperando a ser quitadas."
    mc "*Risa* ¡A sus órdenes, mi comandante! Ponte aquí."
    scene c22s001_090An with dissolve
    mc "Precioso..."
    nor "Y deseoso de tenerte dentro."
    mc "Eso tiene fácil arreglo..."
    scene c22s001_090c with hpunch
    "Hundes tu cara entre sus piernas, percibiendo su aroma terroso y áspero."
    nor "*Gemido* No es lo que quería decir."
    "Está completamente húmeda. La excitación y la anticipación mientras te chupaba la polla la ha puesto cachondísima."
    nor "*Jadeo* Por favor, no continúes con eso. *Gemido* Sube aquí y hazme el amor."
    call BlinkXPS3 ("c22s001_095" , "d") from _call_BlinkXPS3_491
    mc "¿Preparada?"
    nor "Preparada y ansiosa."
    scene c22s001_115An
    "Tus caderas empujan a Mjolnir hasta el fondo de la vagina de [nor]. Puedes notar tu glande en su cérvix."
    if nor._var("pregnant"):
        $ nor._var("pregnancyDiscovered", True)
    $ nor._var("undiscoveredPregnancy", False)
    nor "¡Ufff! *Gemido* Es increíble."
    "Para Mjolnir es como estar en su hogar. El húmedo, estrecho, y caliente coño de [nor] lo abraza en toda su longitud."
    mc "¿Estás bien?"
    nor "Mejor que bien. Y estaré mejor aún cuando empieces a moverte."
    scene c22s001_115pv with dissolve
    show c22s001_115v
    hide c22s001_115va
    "No quieres decepcionarla, con lo que empiezas a mover tus caderas a un ritmo confortable para ambos. Quieres hacer durar la experiencia."
    nor "*Jadeo* Nunca lo habíamos hecho así. *Gemido* Me gusta mucho..."
    "Su respuesta, entre besos y jadeos entremezclados de vuestras bocas te excita mucho."
    "La tensión en sus piernas hace que su coño se sienta muy apretado. Su altura, perfecta para ti, hace que cada una de sus embestidas sea más fácil que la anterior."
    nor "*Gemido* ¡Oh, sí! *Jadeo* Aplasta mi cérvix."
    "La posición es idónea para llegar al fondo de su coño, golpeando la entrada de su útero en cada estocada de tu sable."
    scene c22s001_120pv with dissolve
    show c22s001_120v
    hide c22s001_115v
    "Sable, martillo... ¿Qué más da mientras le de placer a la hermosa mujer que tienes entre tus brazos?"
    nor "*Jadeo* ¡Sigue así! *Jadeo* Estoy a punto de correrme..."
    "Te sorprende la velocidad a la que su orgasmo se está acercando. Otras veces ha tardado mucho más. A ti aún te queda mucha gasolina en el depósito."
    mc "¿Ya? Acabamos de empezar..."
    "Su pierna de apoyo empieza a temblar, anunciando que realmente se está acercando a su orgasmo a una velocidad inusitada."
    scene c22s001_125pv with dissolve
    show c22s001_125v
    hide c22s001_120v
    nor "*Gemido* Esa posición me está encantando. *Jadeo* Es increíble."
    "Entre el ruido que producen vuestros cuerpos al chocar y que sus palabras se pierden dentro de tu boca, casi cuesta entenderle."
    nor "*Gemido* Pero no pares... *Gemido* Va a ser el mejor orgasmo de mi vida... *Gemido*"
    "Su cuerpo tiembla bajo tanta tensión acumulándose en sus músculos. Puedes notarlo en su espalda, en su pierna, en sus manos en contacto con tu piel."
    nor "*Jadeo* Aquí llega... *Gemido* Es enorme... *Jadeo*"
    call OrgasmXS3 ("c22s001_200") from _call_OrgasmXS3_15
    nor "*GEMIDO* ¡SÍ! *JADEO* ¡TE QUIERO! *GEMIDO*"
    "Su cuerpo explota bajo tus dedos, se aprieta contra ti, intenta ordeñar tu polla, mientras orgasmo tras orgasmo recorren el sexy cuerpo de [Nor!t]."
    nor "*JADEO* ¡TE LO HE DICHO! *JADEO* ¡El mejor orgasmo de la historia! *JADEO*"
    scene c22s001_115pv with dissolve
    show c22s001_115v
    hide c22s001_125v
    "Continúas bombeando con tus caderas, mientras poco a poco ella va recuperando la tensión después de relajarse explosivamente durante su primer orgasmo."
    nor "*GEMIDO* No voy a poder continuar así... *JADEO* la pierna no me aguanta... *JADEO*"
    "Su pierna está en proceso de convertirse en un espagueti mojado después del primer clímax. Sabes que van a venir más, si consigues que no se caiga al suelo."
    nor "*JADEO* Vamos a la cama... *GEMIDO* antes de que tengamos un accidente... *GEMIDO*"
    "Casi pensáis lo mismo. Casi."
    scene c22s001_205An with dissolve
    "La levantas en brazos, para su sorpresa. La falta de apoyo de su pierna hace que se empale aún más en Mjolnir."
    nor "*GEMIDO* Aún puedo andar... *GEMIDO* No hace falta que me lleves a la cama."
    mc "¿Quién te ha dicho que te iba a llevar a la cama?"
    nor "*Jadeo* Te vas a joder la espalda, cielo."
    mc "Quizás con la antigua [nor], pero no con esta versión flacucha. *Risa*"
    scene c22s001_130pv with dissolve
    show c22s001_130v
    hide c22s001_115v
    "Aposentas bien los pies antes de empezar a bombear. Los travesaños del armario podrían destrozarle la espalda, con lo que la mantienes en vilo."
    nor "*JADEO* ¡[mc]! *GEMIDO* ¡Hablo en serio!"
    "Te cuesta un poco equilibrar los pesos, pero consigues estabilizar el ritmo después de un par de embestidas."
    mc "Cuando me digas que no te gusta, te llevo a la cama. Y no me sirve que me lo digas entre gemidos."
    "Permanece en silencio. O, al menos, no son palabras lo que sale de su boca."
    nor "*GEMIDO*"
    scene c22s001_135pv with dissolve
    show c22s001_135v
    hide c22s001_130v
    "En esta posición, puedes notar cada fibra de [Nor!t] tensándose. Ha dejado de resistirse y ha decidido dejarse llevar por el placer."
    nor "*GEMIDO* ¡No sé cuántas veces me he corrido ya! *JADEO*"
    mc "Yo aún ninguna, con lo que, si a la señora no le molesta, voy a seguir haciéndote el amor. *Risa*"
    "No hay nada más bonito que la cara de [nor] mientras recibe placer. No hay nada mejor que reírte mientras lo haces."
    nor "*Jadeo* Cuando llegues, córrete dentro de mí. *Gemido*"
    if not nor._var("pregnant") and persistent.pregnancy:
        nor "*Gemido* A ver si esta vez lo conseguimos..."
        "Las ganas de [nor] de llevar un hijo tuyo son conmovedoras. Le debes, como mínimo, intentarlo."
    elif nor._var("pregnant"):
        "Aunque ya esté embarazada, quiere seguir recibiendo tu semilla. No te vas a negar, por supuesto."
    elif not persistent.pregnancy:
        "Le está cogiendo el gusto a que llenes su útero. No te vas a negar, por supuesto."
    scene c22s001_140pv with dissolve
    show c22s001_140v
    hide c22s001_135v
    "Tus piernas empiezan a temblar con cada embestida, indicándote que tu orgasmo se acerca para mezclarse entre las oleadas que recorren el cuerpo de [Nor!t]."
    nor "*GEMIDO* ¡Es increíble cómo tocas todos mis puntos sensibles! *JADEO*"
    "Y es increíble cómo el coño de [nor], ávido por recibir tu leche, estruja tu astil intentando llevarte al clímax para poder ordeñarte."
    if persistent.family:
        nor "*JADEO* Córrete para tu tía. *GEMIDO* Córrete dentro de tu tía."
    else:
        nor "*JADEO* Córrete para mí. *GEMIDO* Córrete dentro de mí."
    "Tus piernas no aguantan más. Tus huevos no pueden retener tu leche mucho más. Tu polla explota en un géiser."
    if persistent.pregnancy and not nor._var("pregnant"):
        if persistent.walkthrough:
            $ wt1 = _("[nor] embarazada.")
            $ wt2 = _("Sin consecuencias.")
        else:
            $ wt1 = ""
            $ wt2 = ""
        menu:
            "Correrte dentro" (wt = wt2):
                pass
            "Correrte dentro. Ir a por el bebé." (wt = wt1):
                $ nor._var("pregnant", True)
                $ nor._var("undiscoveredPregnancy", True)
                play sound ("music/OldMusicBox5.ogg")
    $ resetWalkthrough ()
    call OrgasmXS3 ("c22s001_210") from _call_OrgasmXS3_16
    mc "¡Mpfft!"
    "Nunca deja de sorprenderte lo abundantes que son tus corridas cada vez que tienes sexo con [Nor!t]."
    nor "*GEMIDO* ¡Sí! *JADEO* ¡Dámela! *JADEO* ¡Lléname! *GEMIDO* ¡Hay muchísima!"
    "No es que haya pasado una semana desde que vaciaste tus huevos por última vez."
    "Vuestros orgasmos se funden en uno, que recorre el ser con dos espaldas en el que os habéis convertido."
    call BlinkXPS3 ("c22s001_215" , "f") from _call_BlinkXPS3_492
    "Bombeas un rato más hasta que [nor] te para."
    nor "*Gemido* No puedo más... *Jadeo* Bájame al suelo, por favor."
    mc "¿Ya quieres que pare?"
    call BlinkXPS3 ("c22s001_220" , "d") from _call_BlinkXPS3_493
    nor "*Risa* Quiero ir a la cama, a recibir mi ración de abrazos."
    stop music fadeout (1.5)
    mc "Eso puedo arreglarlo. *Risa*"
    call BlinkXPS3 ("c22s001_225" , "f") from _call_BlinkXPS3_494
    play music ("music/Fragile-Beauty.ogg")
    nor "Ha sido increíble. Me ha encantado la nueva postura. Y no es que no me haya gustado las otras veces."
    mc "A mí también me ha gustado mucho. {b}Tú{/b} eres increíble."
    call BlinkXPS3 ("c22s001_230" , "d") from _call_BlinkXPS3_495
    nor "..."
    mc "¿Pasa algo? ¿He dicho algo malo?"
    call BlinkXPS3 ("c22s001_235" , "d") from _call_BlinkXPS3_496
    nor "¿Has dicho en serio lo de antes?"
    mc "¿El qué? No recuerdo haber dicho nada en especial aparte de que eres increíble."
    call BlinkXPS3 ("c22s001_240" , "d") from _call_BlinkXPS3_497
    nor "No, me refiero a lo que has dicho de la antigua [nor]. De cuando estaba gorda... {b}más{/b} gorda."
    mc "Uno. No estás gorda."
    mc "Dos. ¿A qué te refieres? ¿A lo de que me fastidiaría la espalda?"
    call BlinkXPS3 ("c22s001_245" , "d") from _call_BlinkXPS3_498
    nor "Sí y no."
    nor "Me refiero... lo estuve pensando hace unos días... ¿Estarías conmigo si continuara estando tan gorda como estaba?"
    mc "No."
    call BlinkXPS3 ("c22s001_250" , "d") from _call_BlinkXPS3_499
    nor "Lo sabía... No te lo echo en cara. A veces yo me daba asco a mí misma al mirarme al espejo."
    mc "No lo has entendido."
    mc "No estaría contigo porque no habrías intentado pillarme en la ducha."
    call BlinkXPS3 ("c22s001_255" , "d") from _call_BlinkXPS3_500
    mc "No estaría contigo porque tendrías aún menos seguridad en ti misma y no hubieras intentado nada conmigo."
    call BlinkXPS3 ("c22s001_260" , "d") from _call_BlinkXPS3_501
    mc "No te quiero por cómo eres por fuera, mi amor. Te quiero por quién eres." id c22s001_NorSex_e6d63423
    mc "Te quiero por lo que me haces sentir cada vez que sonríes."
    call BlinkXPS3 ("c22s001_265a" , "d") from _call_BlinkXPS3_502
    mc "Si hubieras actuado exactamente igual que lo has hecho desde que he vuelto, daría lo mismo si pesaras 50 kilos más. Te querría igual."
    mc "Pero no lo hubieras hecho. Y por eso no estaríamos juntos."
    call BlinkXPS3 ("c22s001_265b" , "d") from _call_BlinkXPS3_503
    nor "Lo que acabas de decir es muy bonito, mi vida."
    mc "La verdad a veces es muy bonita, mi amor."
    mc "Y como vuelvas a decir que estás gorda, dejaré de llamarte \"Mi amor\" para llamarte \"Mi Gordita\"."
    call BlinkXPS3 ("c22s001_270" , "d") from _call_BlinkXPS3_504
    nor "¿Pero tú has visto qué culo más gordo tengo?"
    scene c22s001_270d with hpunch
    "Lanzas a [nor] sobre la cama"
    mc "*Ñam* ¿Este culo? No veo que le sobre ni un gramo."
    call BlinkXPS3 ("c22s001_275" , "d") from _call_BlinkXPS3_505
    nor "¡[mc]! ¡Estoy hablando en serio!"
    mc "Y yo también. *Risa* Me encanta tu culo."
    call BlinkXPS3 ("c22s001_280" , "d") from _call_BlinkXPS3_506
    nor "Sobre mis ubres no voy a decir nada. Seguro que también te gustan."
    mc "Me encantan."
    scene c22s001_280d with hpunch
    mc "*Ñam* Y no las vuelvas a llamar ubres. Son preciosas tetas."
    if persistent.lactation:
        mc "Y estoy deseando que empiecen a dar leche."
    call BlinkXPS3 ("c22s001_285" , "d") from _call_BlinkXPS3_507
    nor "Entonces... ¿no cambiarías nada de mí?"
    mc "¿Físicamente? Nada."
    mc "¿Mentalmente? Que dejes de verte como lo que no eres. Que te veas como te veo yo."
    mc "Como una mujer preciosa que no sabe lo bonita que es."
    call BlinkXPS3 ("c22s001_290" , "d") from _call_BlinkXPS3_508
    nor "Para ti es muy fácil decirlo..."
    mc "Cielo, yo he recorrido el mismo camino."
    call BlinkXPS3 ("c22s001_295" , "d") from _call_BlinkXPS3_509
    nor "Y ¿crees que serías como eres si no lo hubieras tenido que hacer?"
    mc "¿Si no hubiera estado gordo? Por supuesto que no sería el mismo que soy."
    mc "Forma parte de mi historia y moldeó mi personalidad. Conocí a [jam] porque estaba gordo y no tenía amigos."
    mc "Empecé a salir con [eil] porque estaba gordo y tenía que usar otros talentos para conquistarla, como hacerle reír."
    mc "Seguramente me hubiera convertido en un gilipollas pagado de sí mismo si hubiera tenido un cuerpo lleno de músculos."
    call BlinkXPS3 ("c22s001_300" , "d") from _call_BlinkXPS3_510
    nor "*Risa* Un poco gilipollas sigues siendo."
    mc "*Risa* Pero soy un gilipollas que te hace reír. Eso es lo importante para mí."
    call BlinkXPS3 ("c22s001_305" , "d") from _call_BlinkXPS3_511
    nor "Te quiero."
    mc "Y yo a ti, mi amor."
    call BlinkXPS3 ("c22s001_310" , "d") from _call_BlinkXPS3_512
    nor "¿No es \"Mi Gordita\"? He continuado diciendo que estaba gorda."
    mc "*Risa* ¿Quieres que te llame \"Mi Gordita\"?"
    if mc._var("relationsips")>1:
        nor "Me gusta. Y me diferenciaría dentro del harén... A menos que también metas en el harén a [kat] o a [bet]. *Risa*"
        if meg._var("route"):
            call BlinkXPS3 ("c22s001_315" , "d") from _call_BlinkXPS3_513
            nor "No creo que a [meg] te atrevas a decírselo nunca. Ella también lo piensa de sí misma, aunque está equivocada."
            mc "Tan equivocada como lo estás tú."
    else:
        nor "Me parece un mote muy cariñoso."
    menu:
        "Te llamaré \"Mi Gordita\".":
            $ nor._var("uNick", _("Mi Gordita"))
            $ uNick = _("Mi Gordita")
        "Te llamaré otra cosa.":
            $ texto = renpy.input (_("¿Cómo quieres llamar cariñosamente a [nor]? Recomiendo que tenga que ver con su peso."))
            $ nor._var("uNick", texto)
            $ uNick = texto
    call BlinkXPS3 ("c22s001_320" , "d") from _call_BlinkXPS3_514
    mc "[uNick!t] suena bien."
    nor "Me gusta. *Risa* Aunque sólo sea porque lo has inventado tú para mí."
    call BlinkXPS3 ("c22s001_325" , "d") from _call_BlinkXPS3_515
    nor "¿Te importaría demasiado que no hubiera segundo round? Estoy muy cansada y tan solo quiero que me abraces."
    mc "Tendremos muchos días para un segundo o un tercer round. Lo de los abrazos se me da muy bien."
    scene c22s001_330a with dissolve
    "Os quedáis abrazados durante un largo rato, hasta que os quedáis dormidos con la luz encendida."
    stop music fadeout (1.5)
    scene c22s001_330b with dissolve
    "Te despiertas a media noche, con [nor] aún en tus brazos. En algún momento se ha despertado y ha apagado las luces."
    scene black with dissolve
    "Sigues durmiendo."
    centered "{size=+20}{b}DÍA 22 – MARTES{/b}{/size}"
    play music ("music/KindofGirl.ogg")
    "Horas después te despiertas con una sensación extraña y húmeda."
    scene c22s001_145pv with dissolve
    show c22s001_145v
    hide c22s001_140v
    mc "Buenos días [uNick!t]."
    nor "*Ronroneo húmedo*"
    mcp "(¿Cómo consigue levantarse con el maquillaje perfecto? ¿Se ha remaquillado antes de empezar a chupar?)"
    mc "¿Sabes que no hacía falta una compensación por la falta de un segundo round ayer?"
    nor "*Ronroneo afirmativo*"
    mc "Aunque no me voy a quejar por despertarme así ningún día. *Risa*"
    scene c22s001_150pv with dissolve
    show c22s001_150v
    hide c22s001_145v
    mc "Hay que poner un espejo en el techo. Me puedo imaginar tu precioso, y nada gordo, culo ahora mismo, pero no puedo verlo."
    nor "*Ronroneo pensativo*"
    "Los ronroneos de [Nor!t] a lo largo de tu polla empiezan a ponerte cachondo, haciendo que tu glande salte de alegría en su boca."
    nor "*Ronroneo inquisitivo*"
    "Y ella lo sabe."
    call BlinkXPS3 ("c22s001_335" , "d") from _call_BlinkXPS3_516
    nor "Buenos días, mi amor. Veo que ya estás listo para el segundo round."
    mc "*Risa* Siempre estoy listo para ti."
    call BlinkXPS3 ("c22s001_340" , "d") from _call_BlinkXPS3_517
    nor "Pues siéntate en la silla. Te voy a cabalgar como si no hubiera un mañana."
    nor "O como si tuviera que ir a hacer yoga en menos de una hora."
    mc "Con lo que, supongo, tampoco habrá segundo round hoy. *Risa*"
    call BlinkXPS3 ("c22s001_345" , "d") from _call_BlinkXPS3_518
    nor "Mi niño se está volviendo avaricioso. *Risa*"
    mc "Por supuesto que sí, [uNick!t]."
    call BlinkXPS3 ("c22s001_350" , "f") from _call_BlinkXPS3_519
    mc "No sé si vas a poder cabalgarme con los brazos de la silla..."
    nor "Déjame probar..."
    scene c22s001_355a with fade
    nor "No... así se me clava en las pantorrillas..."
    scene c22s001_355b with fade
    nor "Así me da la sensación de que me voy a caer hacia atrás..."
    scene c22s001_355c with fade
    nor "Así es perfecto si me ayudas a aguantar el equilibrio."
    scene c22s001_355d with dissolve
    mc "Y las vistas no podrían ser mejores..."
    nor "¿Mi gordo culo? *Risa*"
    mc "Sí, [uNick!t]. *Risa*"
    scene c22s001_355An with dissolve
    nor "¡Ufff!"
    "[Nor!t] se empala en tu polla en un rápido movimiento que hace que notes su cérvix en la punta de tu glande."
    mc "¿Bien?"
    call BlinkXPS3("c22s001_360" , "d") from _call_BlinkXPS3_520
    nor "Aún estoy sensible de anoche, pero de momento... bien."
    nor "Casi me corro..."
    mc "*Risa* Eso lo consideraría mejor que bien."
    nor "Chuparte la polla siempre me pone muy cachonda."
    mc "Ya te he dicho que me podría despertar así todos los días. *Risa*"
    scene c22s001_160pv with dissolve
    show c22s001_160v
    hide c22s001_150v
    "Sin contestarte, [nor] empieza a cabalgarte tal como había prometido."
    nor "*Gemido* Otra postura más... *Jadeo* para la colección de posturas... *Gemido* que me encantan."
    "Estás totalmente de acuerdo. En esta postura tiene total libertad y marca un ritmo endiablado."
    nor "*Jadeo* ¿A quién quiero engañar? *Jadeo* Todas las posturas contigo me encantan. *Jadeo*"
    "También estás de acuerdo. [nor] es una amante maravillosa que te hace sentir cosas increíbles."
    scene c22s001_165pv with dissolve
    show c22s001_165v
    hide c22s001_160v
    if persistent.family:
        "Su coño, estrecho pese a haber dado a luz a las gemelas, abraza tu polla en cada recorrido, acercándote a un rápido clímax matutino después de la mamada."
    else:
        "Su coño, estrecho y elástico pese a su edad, abraza tu polla en cada recorrido, acercándote a un rápido clímax matutino después de la mamada."
    nor "*GEMIDO* ¡No voy a poder aguantar mucho más! *JADEO*"
    "La postura quizás es un poco forzada para ella, manteniendo el control para no chocar con los brazos de la silla. Pese a ser una maestra en yoga, no debe ser cómodo."
    mc "¿Cambiamos de postura? ¿Te es incómodo?"
    nor "*JADEO* ¡NO! *GEMIDO* ¡QUE ME CORROOO! *JADEO*"
    "Si ha estado a punto de correrse cuando se ha empalado, su salvaje cabalgata la lleva más allá de su límite."
    call OrgasmXS3 ("c22s001_365") from _call_OrgasmXS3_17
    nor "*GEMIDO* ¡SÍ! *JADEO* ¡SIGUE!"
    "Las paredes vaginales de [Nor!t] estrujan tu astil con fuerza con la llegada de un potente orgasmo."
    nor "*JADEO* ¡NO PARES! *JADEO*"
    scene c22s001_170pv with dissolve
    show c22s001_170v
    hide c22s001_165v
    "[nor] sigue cabalgándote, cada vez más desmadejada mientras oleada tras oleada de placer recorre su cuerpo."
    nor "*GEMIDO* ¡MÁS PROFUNDO! *JADEO* ¡FÓLLAME MÁS DURO! *GEMIDO*"
    "Si no fuera por tus manos guiando sus movimientos, hace rato que éstos hubieran empezado a ser erráticos."
    nor "*GEMIDO* *ARF* *JADEO* *UFFF*"
    "Conoces perfectamente a [nor] y sabes que no va a poder aguantar este ritmo por mucho más tiempo."
    if persistent.family:
        nor "*GEMIDO* ¡Córrete dentro de tu tía! *JADEO* ¡LLÉNAME!"
    else:
        nor "*GEMIDO* ¡Córrete dentro! *JADEO* ¡LLÉNAME!"
    scene c22s001_175pv with dissolve
    show c22s001_175v
    hide c22s001_170v
    "Tu gasolina se está agotando a pasos agigantados. Los movimientos espasmódicos de [nor] llevándote cada vez más cerca de tu límite."
    nor "*JADEO* ¡ME ENCANTA! *JADEO* ¡NO PUEDO MÁS!"
    "El culo de [Nor!t] rebotando en tu abdomen mientras su vagina intenta exprimir a Mjolnir es una vista increíble. Una sensación impresionante."
    nor "*GEMIDO* ¡CÓRRETE YA! *GEMIDO* ¡NO VOY A PODER ANDAR EN TRES DÍAS!"
    "No puedes negarle sus deseos a una mujer como esta."
    if persistent.pregnancy and not nor._var("pregnant"):
        if persistent.walkthrough:
            $ wt1 = _("[nor] embarazada.")
            $ wt2 = _("Sin consecuencias.")
        else:
            $ wt1 = ""
            $ wt2 = ""
        menu:
            "Correrte dentro" (wt = wt2):
                pass
            "Correrte dentro. Ir a por el bebé." (wt = wt1):
                $ nor._var("pregnant", True)
                $ nor._var("undiscoveredPregnancy", True)
                play sound ("music/OldMusicBox5.ogg")
    call OrgasmXS3 ("c22s001_370") from _call_OrgasmXS3_18
    mc "¡Mpfft!"
    "Vuelves a llenar su útero por segunda vez en pocas horas. No puede retener toda tu semilla en su interior y parte se escapa entre sus labios."
    nor "*GEMIDO* ¡SÍ! *JADEO* ¡POR FIN!"
    scene c22s001_175pv with dissolve
    show c22s001_175v
    hide c22s001_170v
    "[nor] continúa cabalgándote durante unos momentos más, extrayendo cada gota de leche de tu polla y de tus huevos."
    stop music fadeout (1.5)
    "Al poco tiempo su cuerpo se rinde y se queda inmóvil."
    call BlinkXPS3 ("c22s001_375" , "d") from _call_BlinkXPS3_521
    play music ("music/LostVoices.ogg")
    nor "*Gemido* Follar por la mañana después de lo de anoche me ha dejado agotada... *Jadeo* Has tardado mucho más en correrte."
    "Su vagina sigue contrayéndose en pequeños espasmos, como si se despidiera de Mjolnir hasta la próxima vez."
    mc "Anoche me dejaste a punto de correrte con la mamada. Hoy has parado antes."
    call BlinkXPS3 ("c22s001_380" , "d") from _call_BlinkXPS3_522
    nor "*Risa* Consistirá en dejarte a punto la próxima vez que tenga que cabalgarte."
    nor "Y de no tocarte cuando me toque estar pasiva. *Risa*"
    mc "Espero que nunca estés pasiva, [nor]. Me encanta que nos turnemos."
    nor "*Risa* No me refería al modo estrella de mar. Eso no va conmigo."
    mc "¿Modo estrella de mar?"
    call BlinkXPS3 ("c22s001_385" , "d") from _call_BlinkXPS3_523
    nor "Brazos y piernas abiertas y hazme lo que quieras. *Risa* Pero nunca diría que no a un buen misionero."
    mc "Sé que has dicho que tienes que ir a yoga, pero..."
    call BlinkXPS3 ("c22s001_390" , "d") from _call_BlinkXPS3_524
    nor "*Risa* No va a haber otro round, mi insaciable muchacho."
    nor "Voy a ducharme antes de yoga. No quiero bajar oliendo a sexo."
    mc "Supongo que no estoy invitado a la ducha."
    call BlinkXPS3 ("c22s001_395" , "d") from _call_BlinkXPS3_525
    nor "Supones correctamente. *Risa*"
    call BlinkXPS3 ("c22s001_400" , "f") from _call_BlinkXPS3_526
    nor "[mc]... sabes que me ha encantado que duermas aquí, ¿verdad?"
    mc "A mí también me ha gustado. ¿Por qué lo dices?"
    call BlinkXPS3 ("c22s001_405" , "d") from _call_BlinkXPS3_527
    nor "Cuando has dicho que te gustaría despertarte con tu polla en mi boca cada mañana..."
    mc "Es que me encantaría. Y si algún extraño día me despertara yo antes, te despertarías tú con tú clítoris en la mía."
    call BlinkXPS3 ("c22s001_410" , "d") from _call_BlinkXPS3_528
    nor "¿Te molestaría que cada uno siguiera durmiendo en su habitación?"
    if mc._var("relationships")==1 or (mc._var("relationships")==2 and mee._var("route")):
        nor "Me he pasado muchos años durmiendo sola y, pese a que me ha encantado, no creo que me acostumbrara a dormir todas las noches con alguien."
        mc "Ningún problema, lo entiendo. Hay personas que descansan mejor cuando duermen solas."
    else:
        nor "No me gustaría que hubiera celos entre tus chicas. Si te quedas todas las noches... parecería que hay favoritismos."
        mc "Eso es algo que deberíais hablar entre vosotras. Sabes que no voy a favorecer a ninguna por encima de otra. Pero no hay ningún problema."
    call BlinkXPS3 ("c22s001_415" , "d") from _call_BlinkXPS3_529
    nor "¿De verdad no te molesta?"
    mc "¿Me has oído decir algo que no sea verdad alguna vez? Y no me refiero a cuando escondía caramelos por toda la casa."
    mc "Desde que estamos juntos, ¿te he mentido alguna vez?"
    call BlinkXPS3 ("c22s001_420" , "d") from _call_BlinkXPS3_530
    nor "No. Nunca."
    mc "No te preocupes. Entiendo que no me quieras en tu cama todos los días. Incluso alguno puedes venir tú a la mía. Aún no la has probado."
    call BlinkXPS3 ("c22s001_425" , "d") from _call_BlinkXPS3_531
    nor "Mmmmm... es una buena idea... Esa cama la tienes que hacer tú después. *Risa*"
    stop music fadeout (1.5)
    mc "*Risa* Ve a ducharte mientras hago la cama."
    scene c22s001_425d with dissolve
    play sound ("music/knock.ogg")
    "*Knock-Knock*"
    play music ("music/LifeOfAWanderingWizard.ogg")
    eri "*A través de la puerta* Soy yo ¿Puedo entrar ahora que habéis acabado?"
    nor "Un momento..."
    scene c22s001_425d with fade
    nor "Pasa..."
    call BlinkXPS3 ("c22s001_430" , "d") from _call_BlinkXPS3_532
    eri "Buenos días a los dos."
    scene c22s001_430d with dissolve
    mc "Buenos días, [eri]."
    nor "Buenos días, cielo."
    call BlinkXPS3 ("c22s001_435" , "d") from _call_BlinkXPS3_533
    eri "Sólo quería deciros que he preparado el desayuno. Os he oído cuando me he levantado y he supuesto que no tendrías demasiado tiempo para hacerlo, Mamá."
    eri "No quería gritarlo a través de la puerta por si la abuela o Tía [bet] no os han oído. Aunque lo dudo."
    call BlinkXPS3 ("c22s001_440a" , "d") from _call_BlinkXPS3_534
    nor "Gracias, cielo. Ahora iba a ducharme y a bajar a hacerlo. Me acabas de dar unos minutos más en la ducha."
    if eri._var("route"):
        call BlinkXPS3 ("c22s001_440b" , "f") from _call_BlinkXPS3_535
        eri "¿Me dejas que bese a mi novio? *Risa*"
        call BlinkXPS3 ("c22s001_445" , "d") from _call_BlinkXPS3_536
        nor "¡Por supuesto! *Risa* Me voy a la ducha."
        scene c22s001_445d with dissolve
        "[eri] se inclina sobre ti, sin dejarte levantar de la silla, y te besa con dulzura. No hay rastro de celos."
        call BlinkXPS3 ("c22s001_450" , "d") from _call_BlinkXPS3_537
        eri "Buenos días, mi amor."
        mc "Buenos días, mi vida."
        eri "Te espero abajo."
    else:
        call BlinkXPS3 ("c22s001_440b" , "f") from _call_BlinkXPS3_538
    mc "¿Hemos hecho mucho ruido?"
    call BlinkXPS3 ("c22s001_455" , "d") from _call_BlinkXPS3_539
    eri "Han llamado de Protección Animal preguntando si teníamos una manada de rinocerontes en casa. *Risa*"
    mc "*Risa* Me lo tomaré como un sí."
    call BlinkXPS3 ("c22s001_460" , "d") from _call_BlinkXPS3_540
    eri "No sabía si ibas a desayunar aquí. ¿Quieres que te prepare algo?"
    mc "No hace falta, gracias. Tomaré un café tan solo. Yo también quiero ducharme antes de desayunar."
    eri "Entonces te dejo que te vistas y te espero abajo. No tardes, el café está recién hecho."
    scene black with dissolve
    "Bajas a la cocina a tomar un café y te encuentras con miradas que van desde la risueña de [eil] a la sorpresa de [mee]."
    "Parece que todo el mundo ha oído la manada de rinocerontes."
    stop music fadeout (1.5)
    "Te tomas el café rápidamente con unos cuantos ojos clavados en ti antes de despedirte y volver a casa con una sonrisa en tu cara."
    return
label c22s001_NoNorSex:
    call c22s000_relationships from _call_c22s000_relationships_1
    scene c22s001_1000 with dissolve
    "Vas a tu habitación a jugar un rato a My Residence. La Tía alienígena del MC, Nellie, le tiene preparada una sorpresa cuando él la visita en su habitación."
    "Después de la tórrida escena, te vas a dormir."
    scene black with dissolve
    centered "{size=+20}{b}DÍA 22 – MARTES{/b}{/size}"
    return
label c22s002_EmmMarChat:
    if _in_replay:
        call mrS3_rename from _call_mrS3_rename_11
        call mrS3_mar_route from _call_mrS3_mar_route
        call mrS3_emm_route from _call_mrS3_emm_route
        call mrS3_ama_route from _call_mrS3_ama_route
        call mrS3_deb_route from _call_mrS3_deb_route
        call mrS3_sai_route from _call_mrS3_sai_route
        if emm._var("route"):
            call mrS3_dap_route from _call_mrS3_dap_route
            if dap._var("route"):
                call mrS3_eri_route from _call_mrS3_eri_route
                if eri._var("route"):
                    call mrS3_emm_hadAnal from _call_mrS3_emm_hadAnal
        call mrS3_kat_slim from _call_mrS3_kat_slim
    scene black with dissolve
    call changenicks from _call_changenicks
    "Vas a la cocina a desayunar. Con todas las chicas preparándose para la sesión de yoga o ir a clase, debe ser el momento propicio."
    "Posiblemente tengas la cocina para ti."
    scene c22s002_005a with dissolve
    play music ("music/Morning-Sun.ogg")
    "Al llegar descubres que tu idea era equivocada."
    mc "Buenos días. Yo creía que el yoga lo hacíais antes de desayunar."
    if mar._var("route"):
        call KissXPS3("c22s002_010" , "d") from _call_KissXPS3_5
    mom "Buenos días, cielo."
    mom "Sólo nos estamos tomando un café mientras esperamos que el resto estén listas."
    if emm._var("route"):
        call KissXPS3("c22s002_015" , "d") from _call_KissXPS3_6
    emm "Buenos días, [mc]. Hoy están especialmente lentas."
    mc "Me dijo [deb.nick] que os habíais mudado a la piscina para hacer yoga."
    call BlinkXPS3("c22s002_020" , "d") from _call_BlinkXPS3_541
    mom "Sí, la terraza empezaba a estar atestada. Es mucho más cómodo hacerlo alrededor de la piscina."
    call BlinkXPS3("c22s002_025" , "d") from _call_BlinkXPS3_542
    emm "Aunque Mamá aún no nos deja hacer yoga en topless. *Risa*"
    call BlinkXPS3("c22s002_030" , "d") from _call_BlinkXPS3_543
    mom "Podéis hacer topless después del yoga si queréis, pero para hacer deporte os quiero con ropa de deporte."
    mc "Hay un montón de videos en MeTube de mujeres haciendo yoga desnudas, con lo que la ropa no debe ser necesaria. *Risa*"
    call BlinkXPS3("c22s002_035" , "d") from _call_BlinkXPS3_544
    emm "¿Ves? Y si nos dejaras hacerlo, a lo mejor [kat] se unía a las sesiones. *Risa*"
    call BlinkXPS3("c22s002_040" , "d") from _call_BlinkXPS3_545
    kat "Buenos días. ¿A qué sesiones me tengo que unir?"
    mc "A las de yoga."
    call BlinkXPS3("c22s002_045" , "d") from _call_BlinkXPS3_546
    kat "No lo penséis ni por un momento. *Risa* Ya hago demasiado deporte. Si fuera como esos videos de MeTube..."
    scene c22s002_005b with dissolve
    python:
        if "maremm" not in globals () or not isinstance (maremm, TGCharacter):
            maremm = TGCharacter (_("[mar] y [emm]"),   color = "#ff3c33")
    maremm "*Risa*"
    call BlinkXPS3("c22s002_050" , "d") from _call_BlinkXPS3_547
    kat "¿He dicho algo divertido?"
    mc "*Risa* No te puedes llegar a imaginar cuánto."
    call BlinkXPS3("c22s002_055" , "d") from _call_BlinkXPS3_548
    if kat._var("slim"):
        kat "Bueno, yo venía a por un café. Por suerte hoy no hay pasteles para que me deis envidia."
    else:
        kat "Bueno, yo venía a por un café. ¿Has hecho algún pastel hoy, [mar]?"
    call BlinkXPS3("c22s002_060" , "d") from _call_BlinkXPS3_549
    if kat._var("slim"):
        mom "Si quieres te preparo una tostada. Es sano."
    else:
        mom "Hay pastel en la nevera, pero es de ayer. Ahora te sirvo una ración."
    call BlinkXPS3("c22s002_065" , "f") from _call_BlinkXPS3_550
    "Unos minutos después, cuando [kat] se ha llevado su desayuno a su habitación."
    mom "¿Cómo fue la reunión con [ama], por cierto?"
    if ama._var("route"):
        mom "Aparte de los besos, claro. Me refiero a nivel profesional. *Risa*"
        mom "Por cierto, felicidades."
        mc "¿Qué? ¿Ya os habéis enterado?"
        call BlinkXPS3("c22s002_070" , "d") from _call_BlinkXPS3_551
        emm "Nos escribió anoche. En vez de hacerlo al grupo de WhatsUp nos envió mensajes individuales a todas."
        emm "Suponemos que no quería decirle nada a [eva]."
    else:
        mom "Nos dijo por el grupo de WhatsUp que habíais avanzado mucho."
    mc "¿Qué? ¿Tenéis un grupo de WhatsUp? ¿Y no me invitáis?"
    call BlinkXPS3("c22s002_075" , "d") from _call_BlinkXPS3_552
    mom "Tenemos que crear otro para toda la familia y añadirlo a él. El de ahora es solo para chicas."
    mc "No os olvidéis de invitar a [jam] al grupo nuevo."
    call BlinkXPS3("c22s002_080" , "d") from _call_BlinkXPS3_553
    emm "¡Oh! Mamá se ha explicado mal. El de ahora es solo para chicas y [jam]."
    emm "Me parto de risa cada vez que se mete contigo. *Risa*"
    mc "*Risa* ¡Puto traidor!"
    mc "Volviendo a la reunión con [ama], fue muy bien. Estuvimos compartiendo ideas sobre la compañía. Creo que podemos cambiarla para bien."
    call BlinkXPS3("c22s002_085" , "d") from _call_BlinkXPS3_554
    emm "Sobre eso... Creía que ya lo había dicho, pero Mamá me dijo que no. No quiero vender mi parte de NTR."
    emm "No quiero que nadie más tenga que pasar por lo mismo que [ama] y [eva]."
    mc "A veces estoy muy orgulloso de que seas mi hermana."
    call BlinkXPS3("c22s002_090" , "d") from _call_BlinkXPS3_555
    emm "Gracias..."
    if emm._var("route"):
        emm "Y no te olvides de que también soy tu novia."
    scene c22s002_005c with fade
    sai "Buenos días a todos."
    deb "Buenos días."
    if deb._var("route"):
        call BlinkXPS3("c22s002_105a" , "d") from _call_BlinkXPS3_556
        deb "¿Os importa si...?"
        scene c22s002_005d with dissolve
        mom "No nos tienes que preguntar, [deb.nick]."
        emm "Adelante, como si fuera tu novio..."
        call KissXPS3("c22s002_095" , "d") from _call_KissXPS3_7
        deb "Buenos días... *Susurrando* cielo."
        mc "Buenos días, preciosa."
        if sai._var("route"):
            call KissXPS3("c22s002_100" , "d") from _call_KissXPS3_8
            sai "Yo no pienso preguntar. *Risa*"
            mc "Ahora que los secretos han salido a la luz, creo que no es necesario."
    elif sai._var("route"):
        call KissXPS3("c22s002_100" , "d") from _call_KissXPS3_9
        sai "Supongo que no os tengo que preguntar si puedo besar a mi novio, ¿no? *Risa*"
        mc "Ahora que los secretos han salido a la luz, creo que no es necesario."
        scene c22s002_005h with dissolve
        mom "No, no nos tienes que preguntar, [sai]."
        emm "Adelante, como si fuera tu novio... *Risa*"
    call BlinkXPS3("c22s002_105b" , "d") from _call_BlinkXPS3_557
    deb "Yo sólo venía a por unos cafés para [lis], [kim], y para mí."
    deb "Los subiré a la habitación. [lis] y [kim] aún se están vistiendo."
    mc "Está recién hecho. Creo que vamos a tener que comprar otra cafetera a este paso. *Risa*"
    call BlinkXPS3("c22s002_110a" , "d") from _call_BlinkXPS3_558
    sai "Ponme otro a mí, [deb.nick], por favor."
    call BlinkXPS3("c22s002_110b" , "d") from _call_BlinkXPS3_559
    sai "[emm], ¿te importa si me siento?"
    call BlinkXPS3("c22s002_115" , "d") from _call_BlinkXPS3_560
    emm "No, no, adelante. Yo ya me he acabado mi café."
    call BlinkXPS3("c22s002_120" , "d") from _call_BlinkXPS3_561
    emm "Por cierto, hoy me caes mejor. *Risa*"
    call BlinkXPS3("c22s002_125" , "d") from _call_BlinkXPS3_562
    sai "¿Qué? ¿Por qué? ¿Te caía mal? ¿Ya no?"
    mc "Creo que tiene que ver con el color de tu pijama. *Risa*"
    call BlinkXPS3("c22s002_130" , "d") from _call_BlinkXPS3_563
    mom "*Risa* [emm] se enfadó porque no pintamos tu habitación de rosa."
    call BlinkXPS3("c22s002_135" , "d") from _call_BlinkXPS3_564
    emm "Creía que eras de esas chicas sin gusto que odian el rosa. *Risa* Y desde que estás aquí es la primera vez que te veo con algo rosa."
    emm "Bueno, es color salmón, pero me sirve. *Risa*"
    call BlinkXPS3("c22s002_140" , "d") from _call_BlinkXPS3_565
    deb "Bueno, en el Jazz Corner iba de rojo, aunque no sea lo mismo."
    mc "Para [emm], el rojo es casi tan bueno como el rosa, pero solo casi."
    call BlinkXPS3("c22s002_145" , "d") from _call_BlinkXPS3_566
    sai "No te preocupes, [emm]. Me gusta el rosa, aunque prefiero el blanco. Siempre que no sea rosa Barbara y Kendrick."
    sai "Y el amarillo es el color del conocimiento en India. Cuando [mar] me preguntó por el color, me pareció una buena idea."
    mc "Mejor que una habitación completamente rosa, seguro. *Risa*"
    call BlinkXPS3("c22s002_150" , "d") from _call_BlinkXPS3_567
    emm "*Grrr* A veces te odio, [mc]."
    mc "Mientras solo sea a veces..."
    call BlinkXPS3("c22s002_155a" , "d") from _call_BlinkXPS3_568
    emm "Sí, solo a veces. *Risa*"
    if emm._var("route"):
        call BlinkXPS3("c22s002_155b" , "d") from _call_BlinkXPS3_569
        emm "Por cierto, tú y yo tenemos que hacer una prueba. Cubrirá todas nuestras veces..."
        if dap._var("route") and eri._var("route"):
            mc "No todas. Son 48 horas después, con lo que no cubrirá la última vez."
        else:
            mc "Cuando quieras. Ya hace más 48 horas y sólo tendremos que esperar 24 horas más para saberlo."
        call BlinkXPS3("c22s002_160" , "d") from _call_BlinkXPS3_570
        deb "Habláis de..."
        call BlinkXPS3("c22s002_165" , "d") from _call_BlinkXPS3_571
        emm "Sí, de las pruebas rápidas de embarazo. Es una ventaja enorme saberlo tan pronto."
        if deb._var("route"):
            emm "A ver cuándo te la puedes hacer tú. *Risa*"
        call BlinkXPS3("c22s002_170" , "d") from _call_BlinkXPS3_572
        if dap._var("route") and eri._var("route"):
            emm "Pues si no cubre la última vez, mejor esperar. No tengo ganas de que me pinches más veces de lo necesario."
        else:
            emm "Cuando quieras podemos hacerla. Creo que mientras [lis] y [kim] se acaban de vestir tenemos tiempo..."
        if sai._var("route"):
            call BlinkXPS3("c22s002_175" , "d") from _call_BlinkXPS3_573
            if dap._var("route") and eri._var("route"):
                sai "Pues... nosotros... sí que hace más de 48 horas..."
            else:
                sai "Pues... nosotros... también hace más de 48 horas..."
            mc "Pues cuando quieras podemos subir a hacerla. Las tengo en mi habitación."
            scene c22s002_180AnBlink with dissolve
            sai "¿Ahora te va bien? Así después de hacerla me puedo vestir para ir a clase."
            mc "Perfecto. Vamos y ya acabaré de desayunar luego."
            if not dap._var("route") or not eri._var("route"):
                mc "Podemos hacer las dos a la vez."
    elif sai._var("route"):
        call BlinkXPS3("c22s002_185" , "d") from _call_BlinkXPS3_574
        mom "Por cierto, [sai]. [mc] te ha hablado de las pruebas de embarazo, ¿no?"
        mom "Sólo se necesitan 48 horas."
        mc "Sí, se lo he dicho."
        call BlinkXPS3("c22s002_190a" , "d") from _call_BlinkXPS3_575
        sai "¿Cómo sabes que hace más de 48 horas?"
        call BlinkXPS3("c22s002_195" , "d") from _call_BlinkXPS3_576
        mom "Porque duermo dos plantas por debajo de [mc]. *Risa* Y no fuisteis demasiado silenciosos."
        mc "¿Te despertamos?"
        call BlinkXPS3("c22s002_200" , "d") from _call_BlinkXPS3_577
        mom "Con la puerta del garaje, cuando llegasteis. Después ya no pude dormir en un rato."
        mc "Lo siento..."
        call BlinkXPS3("c22s002_190b" , "d") from _call_BlinkXPS3_578
        mc "Pues cuando quieras podemos subir a hacerla. Las tengo en mi habitación."
        scene c22s002_180AnBlink with dissolve
        sai "¿Ahora te va bien? Así después de hacerla me puedo vestir para ir a clase."
        mc "Perfecto. Vamos y ya acabaré de desayunar luego."
    else:
        call BlinkXPS3("c22s002_205" , "d") from _call_BlinkXPS3_579
        mc "¿Pasa algo, [deb.nick]?"
        deb "No sé si voy a poder llevar los tres cafés a la vez por las escaleras."
        mc "No te preocupes, te acompaño y ya acabaré de desayunar luego."
    if dap._var("route") and eri._var("route"):
        scene c22s002_005f with fade
    else:
        scene c22s002_005g with fade
    "Unos minutos después, de vuelta en la cocina..."
    if dap._var("route") and eri._var("route"):
        mc "Ya estoy de vuelta. A ver si ahora puedo acabarme el café."
    else:
        mc "Ya estamos de vuelta. A ver si ahora puedo acabarme el café."
    mc "[emm], ¿no quieres sentarte?"
    if emm._var("hadAnal"):
        call BlinkXPS3("c22s002_215" , "d") from _call_BlinkXPS3_580
        emm "No... no puedo..."
        mc "¿Por qué?"
        call BlinkXPS3("c22s002_220" , "d") from _call_BlinkXPS3_581
        emm "Por tu culpa. *Risa* Y por la mía por pedirlo..."
        mc "¡Ah! Por eso..."
        scene c22s002_225An with dissolve
        mom "¿Qué? ¿Por eso preguntabas ayer si hoy volveríamos a comer de pie?"
        call BlinkXPS3("c22s002_230" , "d") from _call_BlinkXPS3_582
        emm "Es que me encantó, pero llevo dos días arrepintiéndome."
        emm "Me pasó lo mismo la primera vez que lo hicimos... normal..."
        mc "Entonces será mejor no volver a probarlo."
        call BlinkXPS3("c22s002_235" , "d") from _call_BlinkXPS3_583
        emm "¿Qué? ¡NO! No me refería a eso. La primera vez normal también me arrepentí, y ahora ya no tengo molestias nunca."
        call BlinkXPS3("c22s002_240" , "d") from _call_BlinkXPS3_584
        emm "Supongo que pasará lo mismo por detrás, ¿no, Mamá?"
        call BlinkXPS3("c22s002_245" , "d") from _call_BlinkXPS3_585
        mom "Pues no lo sé. Yo no tengo experiencia en eso."
        if mar._var("route"):
            call BlinkXPS3("c22s002_250" , "d") from _call_BlinkXPS3_586
            emm "¡Pues lo tienes que probar! Te recomiendo que uses un plug más grande que el mío para ir acostumbrándote."
            emm "Pero es alucinante. Y nuestro chico es muy delicado... O todo lo delicado que se puede ser con Mjolnir."
            call BlinkXPS3("c22s002_255" , "d") from _call_BlinkXPS3_587
            mom "Bueno, creo que no es algo de lo que tengamos que hablar ahora..."
            call BlinkXPS3("c22s002_260" , "d") from _call_BlinkXPS3_588
            emm "¿Qué pusiste en el grupo de WhatsUp ayer? Que, si nos estamos convirtiendo en una familia, lo podemos hablar todo, ¿no?"
            call BlinkXPS3("c22s002_265a" , "d") from _call_BlinkXPS3_589
            mom "Pero eso no incluye que hable sobre lo que [mc] y yo hacemos en la intimidad contigo o con cualquier otra chica."
            mom "Si tú quieres hablar de ello, me parece bien, pero tienes que respetar a las que pensamos que lo que hacemos en privado debe quedarse en privado."
            call BlinkXPS3("c22s002_270c" , "d") from _call_BlinkXPS3_590
            mc "Mamá tiene razón. A mí no me importa que tú le expliques lo que quieras a ella, pero yo no lo voy a hacer."
            mc "Igual que no voy a explicarte lo que hago con ella. Para mí forma parte de la intimidad de la pareja."
            emm "Tenéis razón... Deberíamos ir bajando a la piscina, ¿no?"
        else:
            call BlinkXPS3("c22s002_265b" , "d") from _call_BlinkXPS3_591
            mom "Y antes de que me saquéis más secretos, deberíamos bajar a la piscina. *Risa*"
    else:
        call BlinkXPS3("c22s002_220" , "d") from _call_BlinkXPS3_592
        emm "No te preocupes. Vamos a bajar a yoga. No me gusta ser la última."
    stop music fadeout (1.5)
    mc "OK."
    return
label c22s002_MarAboutEdmund:
    if _in_replay:
        call mrS3_rename from _call_mrS3_rename_12
        call mrS3_mar_route from _call_mrS3_mar_route_1
        call mrS3_emm_route from _call_mrS3_emm_route_1
        if emm._var("route"):
            call mrS3_emm_hadAnal from _call_mrS3_emm_hadAnal_1
    call BlinkXPS3("c22s002_275a" , "d") from _call_BlinkXPS3_593
    if persistent.family:
        $ Mom = _("Mamá")
    else:
        $ Mom = mar.name
    play music ("music/OneLastChance.ogg")
    mom "¿Puedes ir bajando, [emm]? Tengo que hablar con [mc]."
    call BlinkXPS3("c22s002_280a" , "d") from _call_BlinkXPS3_594
    emm "¿Me tengo que ir?"
    call BlinkXPS3("c22s002_255" , "d") from _call_BlinkXPS3_595
    mom "Es algo que tengo que hablar con [mc] en privado, [emm]."
    if not emm._var("hadAnal"):
        call BlinkXPS3("c22s002_260" , "d") from _call_BlinkXPS3_596
        emm "¿Qué pusiste en el grupo de WhatsUp ayer? Que, si nos estamos convirtiendo en una familia, lo podemos hablar todo, ¿no?"
        mc "No sé de lo que quiere hablar pero, si quiere hablarlo en privado, creo que se lo debemos."
        call BlinkXPS3("c22s002_270a" , "d") from _call_BlinkXPS3_597
        mom "[mc] tiene razón. Lo que tengo que preguntarle le afecta principalmente a él."
        mom "A ti también, pero de otra forma. Y contigo también lo hablaré en su momento, y en privado."
    else:
        call BlinkXPS3("c22s002_270a" , "d") from _call_BlinkXPS3_598
        mom "Y antes de que protestes, esta es una de esas cosas que se tienen que hablar en privado."
    call BlinkXPS3("c22s002_270c" , "d") from _call_BlinkXPS3_599
    emm "Tenéis razón... Entonces voy a ir bajando a la piscina. Os dejo solos."
    call BlinkXPS3("c22s002_275b" , "f") from _call_BlinkXPS3_600
    "Cuando [emm] se ha ido..."
    mc "Dime. Parece serio..."
    mom "Lo es. ¿Recuerdas cuando, durante la reunión con [aar], dijiste que habías hablado con tu padre?"
    mom "Me había olvidado por completo, han pasado tantas cosas desde aquel día..."
    call BlinkXPS3("c22s002_280b" , "d") from _call_BlinkXPS3_601
    mom "Hoy, cuando me he levantado, me ha venido como un flash."
    mom "Parece que hayan pasado un par de meses en vez de... ¿cuántos días han pasado?"
    mc "Cinco días. Fue el jueves."
    call BlinkXPS3("c22s002_285" , "d") from _call_BlinkXPS3_602
    mom "Vale. En cinco días no has tenido tiempo de explicármelo, ¿verdad?"
    mc "[Mom!t], para mí también han pasado un montón de cosas. No hemos tenido un momento para hablarlo."
    call BlinkXPS3("c22s002_290" , "d") from _call_BlinkXPS3_603
    mom "Tienes razón... Hablar de tu padre saca lo peor de mí."
    mom "Explícame por qué y cómo estás en contacto con él."
    mc "Lo primero es decirte que, aunque parezca raro, creo que lo que me ha contado es verdad."
    call BlinkXPS3("c22s002_295" , "d") from _call_BlinkXPS3_604
    mom "No sé qué te habrá contado, pero no entiendo cómo puedes creerte nada de lo que diga."
    mc "Porque no tendría sentido negar algo para admitir algo más... importante."
    mom "Sigue."
    mc "Papá está en Bali. Cuando se fue de aquí fue a Aruba y después se fue a Bali."
    call BlinkXPS3("c22s002_300" , "d") from _call_BlinkXPS3_605
    mom "Destinos tropicales donde estar con su amante y todo el dinero que nos robó a nosotros y a la universidad."
    mom "Bien, típico de él."
    mc "..."
    call BlinkXPS3("c22s002_305" , "d") from _call_BlinkXPS3_606
    mom "¡Vale! Ya me callo."
    mc "La chica con la que se fugó no es su amante. Era una estudiante a la que estaba ayudando a instalarse en el hotel."
    mc "Ella le ayudó a instalarse en Aruba, ya que tenía amigos allí. Ahora está en Canadá de nuevo."
    call BlinkXPS3("c22s002_310a" , "d") from _call_BlinkXPS3_607
    mom "¿Y dices que le crees?"
    mc "Sí, [Mom!t]. Le creo. Después llegaré a eso. Pero eso no lo convierte en un santo."
    call BlinkXPS3("c22s002_310b" , "d") from _call_BlinkXPS3_608
    mom "¿Pero por qué se fue entonces? ¿Para ocultar sus delitos?"
    mc "Es más complicado que eso. NTR nos vigilaba a todos. [eva] y [ama] evitaban que se acercaran a vosotros, pero nadie evitaba que se acercaran a él."
    mc "Y él los descubrió, pero no sabía quieres eran. En el fondo no era tan mal jefe de seguridad."
    mc "Supongo que se cruzó con los que lo seguían a él y con los que os seguían a vosotras. Cuando se produjo el incendio en la universidad creía que habían querido matarlo."
    call BlinkXPS3("c22s002_315" , "d") from _call_BlinkXPS3_609
    mom "¿Por qué iban a querer matarlo? Él no tiene nada que ver con NTR."
    mc "No sabía que eran de NTR. Para él eran dos gemelos. Ahora sabemos que eran clones de la Serie G, y que había más de dos."
    mc "Pero él no tenía ni idea. Sabía que el incendio iba a descubrir sus robos a la universidad, con lo que cogió nuestro dinero y se fue."
    call BlinkXPS3("c22s002_320" , "d") from _call_BlinkXPS3_610
    mom "Bueno... no lo cogió todo..."
    mc "¿Cuánto dejó? Me dijiste que se había llevado vuestros ahorros."
    mom "Dejó el fondo de la universidad de [emm]. Y dinero para un par de meses de gastos. Se llevó el resto."
    mc "Eso encaja más con su historia."
    stop music fadeout (1.5)
    mc "Como te decía, se fue a Aruba a esconderse. Y sabes quién está en Aruba, ¿verdad?"
    call BlinkXPS3("c22s002_325" , "d") from _call_BlinkXPS3_611
    play music ("music/On-The-Rise.ogg")
    mom "NTR. Se fue huyendo de ellos y no pudo elegir peor sitio."
    mc "Exacto. A los pocos días se cruzó con otros Serie G. Creía que le habían seguido hasta allí y se fue a Bali."
    mc "En Indonesia no hay extradición a Estados Unidos y creía que \"los gemelos\" no le seguirían hasta allí. Y, obviamente, no le han seguido."
    if mar._var("route"):
        call BlinkXPS3("c22s002_330" , "d") from _call_BlinkXPS3_612
        mom "Si todo eso es así... quien le ha puesto los cuernos he sido yo, ¿no?... Me siento... sucia..."
        mom "Lo hice pensando que su engaño me justificaba hasta cierto punto, pero ahora..."
        mc "Ahora no cambia nada. Yo te quiero y tú me quieres. Cuando empezamos lo nuestro ninguno de los dos sabía nada."
        mc "No quieras culpabilizarte por una decisión que tomaste con la información de la que disponías."
        mc "Además, ya te he dicho que eso no lo convierte en un santo."
    call BlinkXPS3("c22s002_335" , "d") from _call_BlinkXPS3_613
    mom "¿Se lo has dicho? ¿Que NTR no le persigue?"
    mc "No. Para cuando lo supe todo, después de la reunión con Aaron, ya no hablaba con él."
    call BlinkXPS3("c22s002_340" , "d") from _call_BlinkXPS3_614
    mom "¿Por qué? ¿Qué pasó?"
    mc "Que demostró que, aunque aquella chica no fuera su amante, sigue siendo un cabrón."
    call BlinkXPS3("c22s002_345" , "d") from _call_BlinkXPS3_615
    mom "¿Qué ha hecho esta vez?"
    if persistent.family:
        mc "No te engañó hace dos meses."
        mc "Pero te engañó cuando estabas embarazada de [emm]."
    else:
        mc "Engañó a mi madre, Anna, unos años antes del accidente."
    call BlinkXPS3("c22s002_350" , "v") from _call_BlinkXPS3_616
    mom "¿Qué?"
    mc "Tiene una hija de la edad de [emm]."
    call BlinkXPS3("c22s002_350" , "v") from _call_BlinkXPS3_617
    mom "¿Qué? ¿Quién?"
    mc "No me lo quiso decir. Es por eso por lo que dejé de hablar con él."
    mc "Le dije que cuando estuviera dispuesto a decírmelo volviera a llamarme. No lo ha vuelto a hacer."
    call BlinkXPS3("c22s002_355" , "d") from _call_BlinkXPS3_618
    mom "Y por eso le crees cuando dice que no me engañó, ¿verdad?"
    mc "Sí, no tendría sentido negar que te engañó hace unos meses pero que tiene una hija por ahí."
    if persistent.family:
        mc "Es engañarte igualmente. Sea ahora o hace 19 años."
    else:
        mc "Es engañar a mi madre en vez de a ti."
    mc "Sigue siendo un cabrón. Pero por alguna razón le creo en lo que pasó hace un par de meses."
    call BlinkXPS3("c22s002_360" , "d") from _call_BlinkXPS3_619
    mom "Lo entiendo. Tiene sentido que le creas. Pero a mí me es difícil creerle."
    mc "Me dijo que no sabía lo que le había pasado aquella noche. Que solo fue una vez. Aunque no sé si creerle en eso."
    mc "No es que le vaya a perdonar por lo que hizo ni nada por el estilo, con lo que tampoco me importa demasiado."
    mc "Al menos en algo se comportó bien. El dinero que robaba de la universidad era para que a esa niña no le faltara de nada."
    call BlinkXPS3("c22s002_365" , "d") from _call_BlinkXPS3_620
    mom "¿Tenía que robar para eso?"
    mc "Era la forma de que a nosotros tampoco nos faltase de nada."
    mc "No tenía lógica quitárnoslo a nosotros para dárselo a ella, con lo que se lo robó a la universidad."
    call BlinkXPS3("c22s002_370" , "d") from _call_BlinkXPS3_621
    mom "Al final resultará que sí que le importábamos. Aunque me da lo mismo..."
    mom "Nos hizo mucho daño a [emm] y a mí. A ti también, pero no estabas aquí..."
    mc "Eso parece. Por eso no se llevó el dinero del fondo universitario de [emm]."
    mc "Pero aún hay más."
    call BlinkXPS3("c22s002_375" , "v") from _call_BlinkXPS3_622
    mom "¿Más? No sé si quiero oír qué más ha hecho."
    mc "No, [Mom!t]. En este caso lo he hecho yo."
    mc "Es posible que haya encontrado a mi medio-hermana."
    call BlinkXPS3("c22s002_380" , "d") from _call_BlinkXPS3_623
    mom "¿Quién? No me digas que es una de las estudiantes..."
    mc "No. O no del todo. Hoy llegan los test de ADN."
    mc "Creo... ella y yo creemos... que puede ser [sca]."
    call BlinkXPS3("c22s002_385" , "v") from _call_BlinkXPS3_624
    mom "¿Qué? ¡No puede ser!"
    mc "Las fechas cuadran. Ella no conoce a su verdadero padre, y sabemos que su padre le mandaba dinero a su madre."
    mc "También sabemos que ha dejado de mandárselo poco después de que Papá se fugara. Es demasiada casualidad."
    mc "Sólo te pido que no digas nada, ni siquiera a [sca], hasta que lo confirmemos."
    call BlinkXPS3("c22s002_390a" , "d") from _call_BlinkXPS3_625
    mom "Lo entiendo. No te preocupes."
    mc "Acordamos que no se lo diríamos a nadie hasta tener los resultados de ADN. Llegarán esta tarde."
    call BlinkXPS3("c22s002_390b" , "d") from _call_BlinkXPS3_626
    mom "Si es ella, ¿se lo diréis a la familia?"
    mom "Creo que ella se merece formar parte oficialmente de la familia, aunque ya lo sea de otra forma. Y la familia se merece saberlo."
    mc "Yo querría, pero es una decisión que tenemos que tomar juntos. Está preocupada e ilusionada a partes iguales."
    call BlinkXPS3("c22s002_395" , "h") from _call_BlinkXPS3_627
    "[mar] se lanza a darte el abrazo que desearía daros a [sca] y a ti. Se tiene que conformar contigo, al menos de momento."
    "Casi te tira de la silla."
    mom "Salga lo que salga en las pruebas de ADN, dímelo, por favor."
    mom "Ahora que tengo esa parte de la información, necesito saberlo."
    mc "No te preocupes. Intentaré convencer a [sca] para decírtelo."
    mc "Si sale negativo, no quiero tener que volver a explicar esta historia, con lo que no le diremos nada a nadie."
    mom "Te entiendo..."
    scene c22s002_395d with dissolve
    play sound ("music/knock.ogg")
    "*Knock-Knock*"
    deb "*A través de la puerta* [mar], eres la única que falta. Te estamos esperando."
    scene c22s002_400d with dissolve
    mom "Ahora voy, [deb.nick]."
    call BlinkXPS3("c22s002_400" , "d") from _call_BlinkXPS3_628
    mom "*Susurrando* [emm] les ha dicho algo. Si no, no hubiera llamado a la puerta."
    mom "*Susurrando* Me tengo que ir."
    if mar._var("route"):
        call KissXPS3("c22s002_405" , "d") from _call_KissXPS3_10
    mom "Hasta luego, [mc]."
    mc "Hasta luego, [Mom!t]."
    stop music fadeout (1.5)
    return
label c22s002_MeemawMassage:
    if _in_replay:
        call mrS3_rename from _call_mrS3_rename_13
        $ mc._var("relationships", 0, "set")
        call mrS3_mee_route from _call_mrS3_mee_route_1
        call mrS3_rels from _call_mrS3_rels
        if mc._var("relationships")==1 and not mee._var("route"):
            call mrS3_gf from _call_mrS3_gf
        elif mc._var("relationships")==2 and mee._var("route"):
            call mrS3_gf from _call_mrS3_gf_1
    scene c22s002_550a with fade
    call c22s000_gf from _call_c22s000_gf_1
    mee "... [mc] me está ayudando."
    play music ("music/Rise-Up.ogg")
    deb "Oh, eso está genial. Tener el apoyo de la familia con lo que estás pasando no tiene precio."
    deb "Sé que no es lo mismo, pero sabes que puedes contar con nosotras si necesitas cualquier cosa."
    mee "Gracias, cielo."
    lis "Aunque seamos nuevas en la familia queremos apoyarte."
    call addProfileImageS3 (3, "lisa_3", lis, _(": 15 - Especial"), "") from _call_addProfileImageS3
    mee "Chicas, me vais a poner la carne de gallina."
    call BlinkXPS3("c22s002_555" , "d") from _call_BlinkXPS3_629
    if persistent.family:
        $ Meemaw = _("Mamá")
    else:
        $ Meemaw = mee.name
    mom "¿Hay algún problema con el agua en casa de [nor], [Meemaw!t]?"
    mom "¿Necesitas ducharte aquí?"
    call BlinkXPS3("c22s002_560" , "d") from _call_BlinkXPS3_630
    mee "No, cielo. Venía para ver si [mc] podía ayudarme con el tratamiento. Si le va bien, claro."
    mc "Sí, ningún problema."
    mee "Como todas estaréis haciendo yoga, he pensado que podríamos usar uno de los baños de aquí."
    call BlinkXPS3("c22s002_565" , "d") from _call_BlinkXPS3_631
    mom "Ningún problema, podéis usar el de esta planta si queréis. Solo quedan [sai], [kim] y [kat] y tienen dos baños en su planta."
    mom "Además, es el que tiene la ducha más amplia."
    mom "Nosotras vamos a bajar antes de que se impacienten más."
    call BlinkXPS3("c22s002_570" , "f") from _call_BlinkXPS3_632
    mee "Si te preguntas por qué he querido hacerlo hoy en un baño, es para evitar manchar el suelo de tu habitación."
    mee "Podemos hacerlo en la ducha para evitar manchar el suelo del baño."
    mc "*Risa* Me parece perfecto, Meemaw. No tienes por qué darme explicaciones."
    if not mee._var("route"):
        scene black with dissolve
        "Los dos os quedáis en ropa interior y empiezas a darle el masaje tal como te enseñó la Dra. Milk."
        call BlinkXPS3("c22s002_815" , "d") from _call_BlinkXPS3_633
        "Una vez acabado el masaje..."
        mee "Gracias por todo. Ahora, si me dejas, me voy a dar una ducha."
        mc "Por supuesto."
        scene c22s002_815d with dissolve
        mee "Este champú, ¿lo has probado alguna vez?"
        mc "No, no suelo usar esta ducha."
        scene c22s002_820An with dissolve
        mee "¡Oops! Se me ha resbalado. No te agaches, ya lo cojo."
        scene c22s002_820e with dissolve
        stop music fadeout (1.5)
        mee "Ya está, ya lo tengo."
    else:
        play music ("music/Sad-Cinematic.ogg")
        call BlinkXPS3("c22s002_575" , "f") from _call_BlinkXPS3_634
        mee "¿Vas a quedarte vestido?"
        mc "No, pero estaba disfrutando de las vistas."
        call BlinkXPS3("c22s002_580" , "d") from _call_BlinkXPS3_635
        mee "No sé si sentirme halagada o molesta. No es lógico que un nieto le diga eso a su abuela."
        mc "No voy a decir que lo siento. No todos los nietos tienen una abuela como tú."
        call BlinkXPS3("c22s002_585" , "d") from _call_BlinkXPS3_636
        mee "[mc]..."
        mc "¿Pasa algo, Meemaw?"
        mee "No sé cómo decirte esto..."
        mc "Creo que hemos pasado el punto en que nos debemos avergonzar por decir algo, ¿no?"
        call BlinkXPS3("c22s002_590" , "d") from _call_BlinkXPS3_637
        mee "El otro día, en tu habitación... y el día anterior, en la consulta de la Dra. Milk... acabé con las bragas empapadas..."
        mc "¿Quieres que lo hagamos de otra forma? ¿Quieres que pare cuando estés a punto de llegar al orgasmo?"
        scene c22s002_595d with hpunch
        mee "¡No!"
        call BlinkXPS3("c22s002_595" , "d") from _call_BlinkXPS3_638
        mee "Digo... no hace falta... Me refería a si te importaría que me desnudara del todo..."
        mc "No, Meemaw, no me importaría. Ya te he visto desnuda una vez y sabes que la desnudez no me molesta."
        mc "Si te vas a sentir más cómoda, también me puedo desnudar yo."
        mc "Sería como si nos ducháramos juntos, como hacíamos [nor] y yo cuando era más joven."
        call BlinkXPS3("c22s002_600" , "d") from _call_BlinkXPS3_639
        mee "No sé si podría... No sé... Haz lo que quieras..."
        mc "Vale. Ve desnudándote. ¿Quieres que me gire?"
        scene c22s002_605a with dissolve
        mee "No hace falta..."
        scene c22s002_605b with dissolve
        mee "Como has dicho, ya me viste desnuda el día del secuestro y me vas a volver a ver ahora."
        scene c22s002_605c with dissolve
        mee "No tiene sentido que... nada tiene sentido."
        mc "Si quieres lo podemos dejar y esperar a que Tía [bet] pueda darte el masaje."
        scene c22s002_610d with dissolve:
            yalign 1.0
            linear 5.0 yalign 0.0
        pause (5.0)
        call BlinkXPS3("c22s002_610" , "d") from _call_BlinkXPS3_640
        call addProfileImageS3 (8, "olivia_8", mee, _(": 15 - Especial"), "a") from _call_addProfileImageS3_1
        mee "No, [mc]. Ya no hay vuelta atrás."
        mc "¡Wow, Meemaw! Me encanta que te sientas más cómoda conmigo."
        call BlinkXPS3("c22s002_615" , "d") from _call_BlinkXPS3_641
        mee "Si me sigues mirando así, voy a dejar de estar cómoda."
        mc "Perdón, ve entrando en la ducha. Voy a acabar de desnudarme."
        call BlinkXPS3("c22s002_620" , "f") from _call_BlinkXPS3_642
        mc "¿Cómo quieres que lo hagamos? ¿Como lo hicimos en mi habitación?"
        mc "Creo que funcionó muy bien, tanto a nivel tratamiento... como al otro nivel."
        mee "No me malinterpretes, me encantó... pero no sé si deberíamos seguir haciéndolo así."
        mc "*Risa* Lo dices después de quitarte las bragas para no empaparlas."
        call BlinkXPS3("c22s002_625" , "d") from _call_BlinkXPS3_643
        mee "No puedo controlar lo que hace mi cuerpo, [mc], pero puedo evitar ponérselo fácil."
        mc "*Risa* Y evitar llenar una lavadora de bragas. Lo entiendo."
        call BlinkXPS3("c22s002_630" , "d") from _call_BlinkXPS3_644
        if persistent.family:
            mee "Es que no creo que debas hacer esto con tu abuela."
        else:
            mee "Es que no creo que debas hacer esto conmigo."
        mc "¿Provocarte orgasmos?"
        call BlinkXPS3("c22s002_635" , "d") from _call_BlinkXPS3_645
        mee "Sí... no... no me refiero solo a eso... Un orgasmo es sólo algo físico..."
        mc "Que cuando te masajea [bet] no ocurre. Porque no ocurre, ¿verdad?"
        mee "No, no tengo orgasmos cuando me masajea mi hermana."
        mc "Entonces, ¿dónde está el problema con que los tengas conmigo? Sabes que no me importa."
        call BlinkXPS3("c22s002_640a" , "d") from _call_BlinkXPS3_646
        mee "¡Joder, [mc]! Hay que explicártelo todo..."
        call BlinkXPS3("c22s002_640b" , "d") from _call_BlinkXPS3_647
        mee "Haces que este viejo cuerpo sienta cosas que no sentía desde antes de que nacieras..."
        if persistent.family:
            mee "Cosas que no debería sentir a manos de mi nieto..."
        else:
            mee "Cosas que no debería sentir contigo..."
        call BlinkXPS3("c22s002_640c" , "d") from _call_BlinkXPS3_648
        mee "Me pides una cita... como si fuera lo más normal del mundo entre una abuela y su nieto..."
        mc "Es normal que un nieto lleve a su abuela a cenar, Meemaw."
        call BlinkXPS3("c22s002_640d" , "d") from _call_BlinkXPS3_649
        mee "Pero no es normal que la abuela esté ilusionada con esa cena."
        mee "No es normal que lleve dos días pensando en qué me voy a poner o qué va a pasar en esa cita."
        mee "Parezco una adolescente..."
        mc "¿Y eso es malo?"
        call BlinkXPS3("c22s002_645" , "d") from _call_BlinkXPS3_650
        mee "No es que sea malo..."
        mc "¿Lo que hacemos te hace sentir bien?"
        mee "Sí, pero..."
        mc "No tenemos por qué ir más allá de lo que estamos haciendo. Para eso está la cena."
        call BlinkXPS3("c22s002_650" , "d") from _call_BlinkXPS3_651
        mee "¿Qué va a pasar en esa cena, [mc]?"
        mc "Que decidirás si quieres algo más que los masajes. Y no me refiero a nivel físico."
        mc "Sé que a mucha gente le sonaría ridículo, y sabes que odio las etiquetas..."
        stop music fadeout (1.5)
        mc "Pero decidirás si quieres ser mi... novia. ¡Por Dios! Odio esa palabra."
        call BlinkXPS3("c22s002_655" , "d") from _call_BlinkXPS3_652
        play music ("music/LePrunierenFleur.ogg")
        mee "*Risa* Te entiendo. A mí me pasa lo mismo con esa palabra."
        call BlinkXPS3("c22s002_660" , "d") from _call_BlinkXPS3_653
        mee "Pero cuando la has pronunciado... se me ha puesto la piel de gallina."
        mc "¿Eso es bueno?"
        mee "Es bueno."
        mc "Tenemos que poner una fecha para esa cena, entonces."
        call BlinkXPS3("c22s002_665" , "d") from _call_BlinkXPS3_654
        mee "Podríamos hacerlo el jueves o el viernes. Tendría tiempo para comprarme algo bonito."
        mc "Aún no sé cuándo vamos a ir a Monterey, estamos esperando que [bet] diga algo."
        mc "Pero cuando volvamos, vamos a cenar. Buscaré un sitio bonito donde llevarte."
        call BlinkXPS3("c22s002_670" , "d") from _call_BlinkXPS3_655
        mee "Déjame a mí elegir el sitio."
        mee "Y empecemos ya antes de que te bese y esa cena deje de ser necesaria para decidir."
        scene c22s002_670An with dissolve
        "Te inclinas y besas suavemente los labios de Meemaw."
        "Ella entreabre su boca y deja que su lengua recorra tus labios."
        "Dejas que tu lengua salga de tu boca y roce levemente la suya."
        call BlinkXPS3("c22s002_675" , "d") from _call_BlinkXPS3_656
        mee "*Jadeo* Para ahora mismo si no quieres que hagamos algo de lo que los dos nos podamos arrepentir."
        mc "*Risa* No creo que podamos hacer nada de lo que me pueda arrepentir."
        mc "Pero tienes razón. Empecemos con ese masaje. *Risa* ¡Trae esas tetas aquí!"
        call BlinkXPS3("c22s002_680" , "f") from _call_BlinkXPS3_657
        "Meemaw apoya su espalda contra tu pecho, pero esta vez no apoya su culo contra Mjolnir."
        "La coges por los pechos, aprisionando sus pezones entre tus dedos. Los nódulos que te indicó la Dra. Milk no están duros hoy."
        "Pero su posición desplazada hace que la posición se note extraña."
        mc "Esta posición es nueva..."
        mee "Notarte rozando tu polla contra mi culo puede ser demasiado para mí."
        mee "Esta vez no hay tela que nos separe..."
        mc "Mjolnir va a echar de menos tu culo. *Risa*"
        call BlinkXPS3("c22s002_685" , "d") from _call_BlinkXPS3_658
        mee "¿Mjolnir? ¿Le has puesto nombre?"
        mc "*Risa* Mejor que no preguntes. Voy a empezar."
        scene c22s002_450pv with dissolve
        show c22s002_450v
        "Empiezas a masajear sus pechos. Te dedicas a magrear esas maravillosas tetas sin soltar la presa que tus dedos hacen sobre sus pezones."
        mee "*Gemido* Así no es como te enseñó la doctora..."
        "Su gemido te indica que no le importa que el tratamiento sea diferente hoy."
        mc "*Susurrándole al oído* Hoy no tienes aquellos bultos. He pensado que, quizás, prefieras algo más placentero."
        "Apoya su espalda contra tu pecho con más fuerza, como si las piernas no le sujetaran por un momento."
        mee "*Jadeo* Más placentero... sí... *Gemido* Está bien..."
        scene c22s002_690AnBlink with dissolve
        hide c22s002_450v
        "No puedes evitar notar cómo tu polla pasa a estar totalmente erecta."
        mee "*Gemido* Veo que no soy la única a quien le gusta esta aproximación... *Jadeo* más placentera..."
        "No hay forma humana de que puedas negarlo."
        mc "Es imposible que no me guste tener unas maravillosas tetas entre mis manos."
        call BlinkXPS3("c22s002_695a" , "d") from _call_BlinkXPS3_659
        mc "*Susurrándole al oído* Además, es aquí donde nos imaginé cuando estábamos en la consulta de la doctora."
        mc "*Susurrándole al oído* Si me puse cachondo imaginándonos, te puedes imaginar lo cachondo que me pone estar aquí contigo."
        mee "*Gemido* Me lo puedo imaginar..."
        if persistent.lactation:
            scene c22s002_455pv with dissolve
            show c22s002_455v
            "En el momento en que ha sido consciente de tu erección, notas cómo su cuerpo se estremece y los primeros rastros de leche empiezan a manar de su pecho."
            mc "Me encanta notar tu caliente leche en mis manos, Meemaw."
            mee "*Gemido* Sé que te gusta... *Jadeo* No me he ordeñado tan a fondo como otras veces... *Gemido* No hubiera servido de nada de todas formas."
        else:
            scene c22s002_450pv with dissolve
            show c22s002_450v
            "En el momento en que ha sido consciente de tu erección, notas cómo su cuerpo se estremece, aunque sorprendentemente la leche no hace aparición."
            mc "¿No hay leche hoy? ¿No te gusta tanto como el otro día?"
            mee "*Gemido* Hoy me he ordeñado diversas veces... *Jadeo* Quería evitar lo del otro día..."
        "Sus caderas empiezan a moverse, rozándose con las tuyas, aunque lejos de Mjolnir."
        mc "*Susurrándole al oído* Parece que tu culo echa de menos a Mjolnir tanto como él echa de menos a tu culo."
        mee "*Jadeo* Notarlo tan cerca y tan lejos a la vez... *Gemido* me está matando..."
        scene c22s002_690h with vpunch
        mee "*Gemido* ¿Puedo?"
        mc "*Risa* Creo que el orden debe ser a la inversa. Preguntar antes de tenerlo en la mano."
        mc "Pero sí, puedes."
        if persistent.lactation:
            scene c22s002_465pv with dissolve
            hide c22s002_455v
            show c22s002_465v
            "[mee] empieza a masturbarte lentamente, acompañando cada movimiento de su mano con un borbotón de leche saliendo de sus pechos."
        else:
            scene c22s002_460pv with dissolve
            hide c22s002_450v
            show c22s002_460v
            "[mee] empieza a masturbarte lentamente, acompañando cada movimiento de su mano con un gemido."
        mee "*Jadeo* Es enorme... *Gemido* Y está durísimo..."
        mc "*Susurrándole al oído* Si alguna vez dudas de si eres atractiva, recuerda este momento."
        "Puedes notar como su mano libre se acerca a su coño en un recorrido de caricias antes de cambiar de opinión. Parece que está en pleno conflicto."
        mee "*Gemido* No puedo hacerlo..."
        mc "*Susurrándole al oído* ¿Qué es lo que no puedes hacer, Meemaw?"
        call BlinkXPS3("c22s002_695b" , "d") from _call_BlinkXPS3_660
        mee "*Jadeo* Mi mano parece tener voluntad propia... *Gemido* Pero no puedo..."
        mc "*Susurrándole al oído* Quizás pueda ayudar en eso."
        if persistent.lactation:
            scene c22s002_475pv
            hide c22s002_465v
            show c22s002_475v
            pause (4.0)
            scene c22s002_475dv
        else:
            scene c22s002_470pv
            hide c22s002_460v
            show c22s002_470v
            pause (4.0)
            scene c22s002_470dv
        "Tu mano abandona su pecho, recorriendo el camino que lo separa de su coño, parándose nada más tocar su clítoris."
        mee "*GEMIDO* ¿Qué haces?"
        mc "*Susurrándole al oído* Mi mano quiere hacer lo que la tuya no se atreve."
        call BlinkXPS3("c22s002_700a" , "d") from _call_BlinkXPS3_661
        mee "Pero..."
        mc "*Susurrándole al oído* Ya lo hice el otro día en mi habitación, Meemaw."
        mee "Pero entonces llevaba bragas..."
        mc "*Susurrándole al oído* Y no tenías mi polla en la mano..."
        call BlinkXPS3("c22s002_700b" , "d") from _call_BlinkXPS3_662
        mee "Estoy siendo un poco hipócrita ¿verdad?"
        mee "Me encantan los orgasmos que me regalas pero me da reparo que me toques ahí abajo. Mientras yo te estoy masturbando..."
        mc "No es hipocresía, Meemaw. Quizás no estás preparada para esto. Aún."
        mc "Quizás después de la cita lo estés. Quizás no lo estés nunca."
        mc "Voy a retirar mi mano poco a poco. Si me dejas volver a tu pecho no volveré a bajar hoy."
        scene c22s002_700d with hpunch
        mee "¡No! Tienes tu mano ahí. Yo tengo mi mano alrededor tuyo."
        mee "Y yo no voy a retirarla."
        mee "No hace falta que tú tampoco la retires."
        mc "Entonces voy a empezar a moverla, si me lo permites."
        if persistent.lactation:
            scene c22s002_485pv with dissolve
            hide c22s002_475v
            show c22s002_485v
        else:
            scene c22s002_480pv with dissolve
            hide c22s002_470v
            show c22s002_480v
        "Sin esperar su respuesta tu dedo corazón empieza a acariciar su clítoris suavemente. Ella vuelve a gemir."
        mee "*Gemido* Hace décadas que nadie me había tocado ahí. *Gemido*"
        "Su botón del placer, ya hinchado en tu primer roce, se pone más duro con cada movimiento."
        mc "*Susurrándole al oído* Creo que ya era hora de que alguien le dedicara la atención que merece, ¿no?"
        "Su cuerpo se estremece de placer mientras te masturba torpemente."
        scene c22s002_530pv with dissolve
        hide c22s002_480v
        hide c22s002_485v
        show c22s002_530v
        if persistent.family:
            $ Meemaw = _("tu abuela")
        else:
            $ Meemaw = mee.name
        mee "*Jadeo* Tienes unos dedos maravillosos... *Gemido* Creo que me voy a correr... *Jadeo*"
        "El cuerpo de [Meemaw!t] se vuelve más sexual con cada uno de vuestros encuentros, intentando recuperar las más de dos décadas de orgasmos perdidos."
        mc "*Susurrándole al oído* Córrete para mí, Meemaw. Déjate ir."
        "Su cuerpo se empieza a tensar bajo tus dedos. Su mano sobre la tuya, sin decidirse a apartarla, tan solo acariciándola."
        "No intenta marcarte ningún tipo de ritmo, el que tú marcas es perfecto para su cuerpo mientras el de su otra mano empieza a fallar."
        if persistent.lactation:
            call OrgasmXS3("c22s002_705a") from _call_OrgasmXS3_19
        else:
            call OrgasmXS3("c22s002_705b") from _call_OrgasmXS3_20
        mee "*GEMIDO* ¡SÍ! *JADEO* *Sonidos ininteligibles*"
        if persistent.lactation:
            "Su cuerpo explota bajo tus manos, por arriba y por abajo, creando tres surtidores simultáneos."
        else:
            "Su cuerpo explota bajo tus manos, creando un surtidor en su parte baja en vez de en sus pechos que, ordeñados a fondo previamente, carecen de leche."
        mee "*JADEO* ¡Ufff! *JADEO* ¡Wow!"
        if persistent.lactation:
            scene c22s002_485pv with dissolve
            hide c22s002_530v
            show c22s002_485v
        else:
            scene c22s002_480pv with dissolve
            hide c22s002_530v
            show c22s002_480v
        "Continúas acariciando su clítoris mientras su cuerpo empieza a relajarse. No quieres que pierda toda la tensión."
        mee "*Gemido* Ya está, [mc]... *Gemido* Cada vez son mejores..."
        "No estás de acuerdo en que ya haya acabado."
        call BlinkXPS3("c22s002_710" , "d") from _call_BlinkXPS3_663
        mc "¿Estás segura de que ya está? ¿Quieres que acabe aquí la sesión de hoy?"
        mee "*Gemido* No... tú aún no te has... *Jadeo* corrido..."
        mc "No me refiero a eso. Ven, siéntate conmigo."
        if persistent.lactation:
            scene c22s002_710d with fade
        else:
            scene c22s002_710e with fade
        mee "Pero desde aquí arriba... no puedo llegar a ti."
        mc "Habrá tiempo para eso, pero recuerda que esto es por tus pechos, necesitan atención."
        call BlinkXPS3("c22s002_715a" , "d") from _call_BlinkXPS3_664
        mee "Pero ya están vacíos..."
        if persistent.lactation:
            mc "*Risa* Bueno, estoy casi seguro de que aún puedo conseguir algo más de leche. Además, hoy aún no la he probado."
        else:
            mc "*Risa* Estaban vacíos cuando hemos empezado, con lo que no veo ninguna diferencia."
        mc "Además, esos pezones están reclamando mi atención."
        if persistent.lactation:
            scene c22s002_715d with dissolve
        else:
            scene c22s002_715e with dissolve
        mee "Están muy sensibles después del masaje y el orgasmo..."
        mc "¿Sabes lo que me gusta? Que ya no dudes en decir orgasmo."
        call BlinkXPS3("c22s002_715b" , "d") from _call_BlinkXPS3_665
        mee "¿Tiene algún sentido ocultarlo? Nunca pensé que la galactorrea me iba a dejar tan sensible a esto..."
        mc "*Risa* Sigues negándolo, Meemaw. Con Tía [bet] no tienes orgasmos."
        mc "Creo que tiene más que ver con que sea yo quién hace esto."
        mee "¿A qué te refieres con \"esto\"? ¿A los masajes?"
        mc "A \"esto\"."
        if persistent.lactation:
            scene c22s002_495pv with dissolve
            hide c22s002_485v
            show c22s002_495v
        else:
            scene c22s002_490pv with dissolve
            hide c22s002_480v
            show c22s002_490v
        "Tu boca baja al pezón de [mee] y empiezas a dedicarle toda tu atención. Dedos y labios. Dientes y lengua. Dedicas todos tus recursos al pecho de [mee]."
        mee "*Gemido* ¡Oh! ¿A eso? *Jadeo* A [bet] no le dejaría hacerlo. *Risa* *Gemido*"
        if persistent.lactation:
            "El sabor de su leche en tu boca te pone más cachondo de lo que podías imaginar. Otras personas lo podrían encontrar enfermizo."
        else:
            "La ausencia de leche permite que te puedas dedicar con fragor a su pezón. Otras personas considerarían enfermizo lo que haces con el pecho de [mee]."
        "Para ti es totalmente natural. Y tórrido."
        mee "*JADEO* Vas a conseguir que me corra otra vez... *GEMIDO*"
        "Pobre [mee]. Aún no ha descubierto que esa era tu intención desde el principio."
        if persistent.lactation:
            call OrgasmXS3("c22s002_720a") from _call_OrgasmXS3_21
            mee "*GEMIDO* ¡SÍ! *JADEO* ¡Toma mi leche!"
            "Un borbotón de leche sale del pecho de [mee] llenando tu boca con el caliente y exquisito líquido."
        else:
            call OrgasmXS3("c22s002_720b") from _call_OrgasmXS3_22
            mee "*GEMIDO* ¡SÍ! *JADEO*"
        "Mientras su coño rocía tu pierna con su corrida, [Meemaw!t] no deja de gemir."
        "Cada vez tarda menos en correrse. Cada vez que se corre es más intenso."
        call BlinkXPS3("c22s002_725" , "d") from _call_BlinkXPS3_666
        mee "*Gemido* [mc]... no puedo más... no me aguanto ni sentada encima tuyo... *Jadeo*"
        mc "Recuéstate en la pared si quieres..."
        mee "*Respiración entrecortada* Y tú aún no te has corrido..."
        mc "No te preocupes por eso. Me encanta verte correrte a ti."
        if persistent.lactation:
            call BlinkXPS3("c22s002_730a" , "f") from _call_BlinkXPS3_667
        else:
            call BlinkXPS3("c22s002_730b" , "f") from _call_BlinkXPS3_668
        mee "Estoy agotada... Temo que las chicas me hayan oído... Me he dejado ir demasiado y he gritado."
        mc "Tampoco te preocupes por eso. Aún están en la piscina haciendo yoga. No te pueden haber oído."
        if persistent.lactation:
            call BlinkXPS3("c22s002_735a" , "d") from _call_BlinkXPS3_669
        else:
            call BlinkXPS3("c22s002_735b" , "d") from _call_BlinkXPS3_670
        mee "Es que he gritado mucho... Eres increíble con esa lengua..."
        mc "Gracias, pero aún no has descubierto lo bueno que puedo ser."
        if persistent.lactation:
            call BlinkXPS3("c22s002_740a" , "d") from _call_BlinkXPS3_671
        else:
            call BlinkXPS3("c22s002_740b" , "d") from _call_BlinkXPS3_672
        mee "¿Te refieres a...?"
        mc "Sí. Y si me dejas, te lo puedo enseñar."
        if persistent.lactation:
            call BlinkXPS3("c22s002_745a" , "d") from _call_BlinkXPS3_673
        else:
            call BlinkXPS3("c22s002_745b" , "d") from _call_BlinkXPS3_674
        mee "No creo que pueda tener más orgasmos hoy, [mc]. Estoy agotada. Las piernas no me aguantan."
        mc "*Risa* Por suerte, lo ideal es que estés tumbada."
        mc "Y si te hubiera preguntado antes, también habrías dicho que no ibas a tener más orgasmos. *Risa*"
        if persistent.lactation:
            call BlinkXPS3("c22s002_750a" , "d") from _call_BlinkXPS3_675
        else:
            call BlinkXPS3("c22s002_750b" , "d") from _call_BlinkXPS3_676
        mee "¿Cómo quieres que me ponga?"
        mc "*Risa* ¡Así me gusta! Que te dejes ir y quieras probar cosas nuevas."
        mee "Llegados a este punto, no creo que pueda oponer resistencia a nada de lo que me pidas."
        mc "Túmbate del todo."
        if persistent.lactation:
            call BlinkXPS3("c22s002_755a" , "f") from _call_BlinkXPS3_677
        else:
            call BlinkXPS3("c22s002_755b" , "f") from _call_BlinkXPS3_678
        mee "¿Te parece bien así? Nunca he hecho esto..."
        mc "¿Nunca?"
        mee "Ya sabes... en los 70 y los 80... había mucho pelo ahí abajo y no todos los hombres..."
        mc "Te entiendo. No te preocupes, estás perfecta."
        if persistent.lactation:
            scene c22s002_505pv with dissolve
        else:
            scene c22s002_500pv with dissolve
        "Hundes tu cara entre sus muslos y, en el momento en que tu lengua toca su clítoris, [Meemaw!t] vuelve a explotar en un sorprendente orgasmo."
        if persistent.lactation:
            call OrgasmXS3("c22s002_760a") from _call_OrgasmXS3_23
        else:
            call OrgasmXS3("c22s002_760b") from _call_OrgasmXS3_24
        mee "*GEMIDO* ¡JODER! *JADEO* ¡SÍ! *GEMIDO*"
        "Su corrida llena todos tus sentidos por sorpresa. No creías que fuera a ser tan rápido. Apenas te ha dado tiempo a empezar."
        if persistent.lactation:
            call BlinkXPS3("c22s002_765a" , "d") from _call_BlinkXPS3_679
        else:
            call BlinkXPS3("c22s002_765b" , "d") from _call_BlinkXPS3_680
        mc "¿Ya? Eso ha sido rápido..."
        mee "*Respiración entrecortada* Me he puesto cachondísima en el momento en que lo has propuesto... *Gemido* Pero no pares ahora..."
        if persistent.lactation:
            scene c22s002_505pv with dissolve
            hide c22s002_495v
            show c22s002_505v
        else:
            scene c22s002_500pv with dissolve
            hide c22s002_490v
            show c22s002_500v
        "El caballero que llevas dentro no puede negarle esa petición a una dama."
        mee "*JADEO* ¡POR EL AMOR DE DIOS! *GEMIDO* ¡ESTO ES LO MEJOR QUE HE PROBADO EN MI VIDA!"
        "Menos aún a una dama que vuelve a alcanzar el clímax en el momento en que reemprendes la acción de tu lengua."
        if persistent.lactation:
            "Ahora sus pechos sí que están totalmente vacíos. La velocidad de sus orgasmos no les da tiempo a llenarse entre uno y otro."
        mee "*GEMIDO* ¡NO PARES! *JADEO* ¡ES *Sonidos ininteligibles*!"
        "Continúas lamiendo, chupando, y mordisqueando. Te embarga una sensación de satisfacción con cada nuevo orgasmo."
        mee "*GEMIDO* ¡PARA, POR FAVOR! *GEMIDO* ¡NO PUEDO MÁS!"
        if persistent.lactation:
            call BlinkXPS3("c22s002_770a" , "d") from _call_BlinkXPS3_681
        else:
            call BlinkXPS3("c22s002_770b" , "d") from _call_BlinkXPS3_682
        mc "¿Quieres que pare?"
        mee "*Gemido* No puedo seguir así... *Jadeo* Debo haber perdido 10 kilos de líquido..."
        mc "Delicioso líquido, por cierto. *Risa*"
        if persistent.lactation:
            call BlinkXPS3("c22s002_775a" , "d") from _call_BlinkXPS3_683
        else:
            call BlinkXPS3("c22s002_775b" , "d") from _call_BlinkXPS3_684
        mee "*Gemido* Me voy a tener que quedar a vivir en esta ducha. *Risa* Tal como me tiemblan las piernas, no voy a poder andar en dos días. *Jadeo*"
        mc "Entonces descansa todo lo que quieras. Voy a vestirme antes de que las chicas acaben su sesión de yoga."
        if persistent.lactation:
            call BlinkXPS3("c22s002_780a" , "d") from _call_BlinkXPS3_685
        else:
            call BlinkXPS3("c22s002_780b" , "d") from _call_BlinkXPS3_686
        mee "¡No! No puedo andar, pero me puedo poner de rodillas. Ponte ahí."
        mee "No voy a permitir que te vayas a solucionar esa erección por ti mismo después de todo lo que me has hecho disfrutar a mí."
        mc "*Risa* Me encanta ver esa fiereza en tus ojos al ponerte al mando."
        if persistent.lactation:
            call BlinkXPS3("c22s002_785a" , "f") from _call_BlinkXPS3_687
        else:
            call BlinkXPS3("c22s002_785b" , "f") from _call_BlinkXPS3_688
        mc "¿Aquí estoy bien?"
        mee "Perfecto."
        if persistent.lactation:
            call BlinkXPS3("c22s002_790a" , "f") from _call_BlinkXPS3_689
        else:
            call BlinkXPS3("c22s002_790b" , "f") from _call_BlinkXPS3_690
        mee "Hace décadas que no hago esto. Disculpa si estoy un poco oxidada."
        "La idea de recibir tu primera paja de [Meemaw!t] es suficiente para ponerte cachondo. No cuentas su torpe intento de antes como la primera vez."
        mc "No te preocupes, Meemaw. Me va a gustar de todas formas."
        "O eso esperas."
        if persistent.lactation:
            scene c22s002_545pv
            hide c22s002_505v
            show c22s002_545v
            pause (6.0)
            scene c22s002_545dv
        else:
            scene c22s002_540pv
            hide c22s002_500v
            show c22s002_540v
            pause (6.0)
            scene c22s002_545dv
        if persistent.family:
            "Tu abuela empieza a hacerte una lenta paja para, tras un par de movimientos, introducirse tu polla en su boca antes de quedarse quieta."
        else:
            "[mee] empieza a hacerte una lenta paja para, tras un par de movimientos, introducirse tu polla en su boca antes de quedarse quieta."
        mc "¡Wow, Meemaw! ¡No me esperaba eso!"
        mee "*Ronroneo afirmativo*"
        "Con lo pequeña que es [mee], tu polla impacta en seguida en el fondo de su boca. Oyes una pequeña arcada. Cada vez estás más sorprendido."
        scene c22s002_520pv with dissolve
        hide c22s002_540v
        hide c22s002_545v
        show c22s002_520v
        "Su cabeza empieza a subir y a bajar a lo largo de tu astil. Con lo torpe que era con las manos, es una sorpresa su habilidad con la boca."
        mc "¡Wow, Meemaw! ¡Tampoco me esperaba eso!"
        "Su lengua hace maravillas en tu astil. Su garganta abraza tu glande. Sus labios no dejan de apretar tu polla en ningún momento."
        mee "*Gemido agradecido*"
        "Llevas cachondo desde lo que parecen ser horas. Con tanta habilidad, dudas que puedas aguantar mucho."
        if persistent.lactation:
            scene c22s002_515pv with dissolve
            hide c22s002_545v
            show c22s002_515v
        else:
            scene c22s002_510pv with dissolve
            hide c22s002_540v
            show c22s002_510v
        mc "Meemaw, no me queda mucha gasolina en el depósito."
        "A ella parece no importarle y usa más todavía su lengua. Sus labios aprietan aún más. Se introduce tu polla más al fondo."
        mee "*Jadeo inquisitivo*"
        "Sus jadeos en tu glande hacen que tu polla de saltos de alegría con cada vibración."
        mc "¿Si quiero correrme en tu boca? Me parecería increíblemente sexy."
        "Empieza a hacer vibrar su garganta de una forma más potente que los jadeos anteriores. Toda su boca vibra al unísono."
        mee "Ngggggghhhh"
        call OrgasmXS3("c22s002_795a") from _call_OrgasmXS3_25
        mc "¡Mpfft!"
        "Estallas sin remedio en la boca de [Meemaw!t]. Después de tanto rato cachondo, la descarga es enorme."
        mee "*Jadeo*"
        if persistent.family:
            "Tu abuela, experta mamadora, no deja escapar prácticamente ni una gota."
        else:
            "[mee], experta mamadora, no deja escapar prácticamente ni una gota."
        if persistent.lactation:
            scene c22s002_800aAnBlink with dissolve
        else:
            scene c22s002_800bAnBlink with dissolve
        mee "¿Te ha gustado, cielo?"
        mc "¡Ha sido increíble! Nunca me hubiera imaginado que tuvieras esas habilidades."
        if persistent.lactation:
            call BlinkXPS3("c22s002_805a" , "d") from _call_BlinkXPS3_691
        else:
            call BlinkXPS3("c22s002_805b" , "d") from _call_BlinkXPS3_692
        mee "*Risa* Nadie se plantea por norma las habilidades sexuales de sus abuelos."
        mc "Pues no saben lo que se pierden. *Risa*"
        mee "Voy a acabar de limpiarte. No hay que desperdiciar ni una gota de esta leche."
        if persistent.lactation:
            mee "Ya que tú no desperdicias una gota de la mía, yo no voy a hacerlo con la tuya."
        scene c22s002_810a with dissolve
        "[mee] se vuelve a meter tu polla en la boca para limpiarte a fondo."
        stop music fadeout (1.5)
        "Su traviesa lengua no pierde oportunidad en jugar con tu sensible glande y hacerte saltar de placer."
    scene c22s002_825An with dissolve
    play music ("music/WarIsComing.ogg")
    bet "Hola, venía a ver si necesitabais..."
    scene c22s002_825c with vpunch
    bet "¿QUÉ? ¿OTRA VEZ?"
    if mee._var("route"):
        if persistent.lactation:
            scene c22s002_830a with hpunch
            mee "*JADEO*"
            scene c22s002_835a with dissolve
        else:
            scene c22s002_830b with hpunch
            mee "*JADEO*"
            scene c22s002_835b with dissolve
    else:
        scene c22s002_830c with hpunch
        mee "¿Qué?"
        scene c22s002_835c with hpunch
    mee "¡[bet]! ¡Te lo puedo explicar!"
    scene c22s002_825d with hpunch
    bet "¡No hace falta! ¡Tengo ojos!"
    scene c22s002_825a with hpunch
    play sound ("music/DoorSlam.ogg")
    "*Blam*"
    call BlinkXPS3("c22s002_840" , "d") from _call_BlinkXPS3_693
    mee "Tengo que ir a hablar con ella..."
    mc "¿Qué quería decir con \"otra vez\"?"
    if mee._var("route"):
        mc "¿Le has dicho lo que estábamos haciendo?"
        call BlinkXPS3("c22s002_845" , "d") from _call_BlinkXPS3_694
        mee "No, no se lo he dicho."
    else:
        call BlinkXPS3("c22s002_845" , "d") from _call_BlinkXPS3_695
    mee "No tengo ni idea de a qué se refiere. Tengo que ir a hablar con ella, [mc]. No hay tiempo para esto ahora."
    mc "¿Quieres que te acompañe?"
    stop music fadeout (1.5)
    mee "No, es mi hermana. Creo que debo ser yo quién hable con ella."
    play music ("music/Wonder.ogg")
    call BlinkXPS3("c22s002_850" , "f") from _call_BlinkXPS3_696
    if mee._var("route"):
        "Después de ponerse de nuevo el albornoz y enjuagarse la boca para quitarse el sabor de tu semen..."
        mee "Me voy. Gracias por esta maravillosa mañana."
        mc "Creo que no hace falta darlas. Los dos lo hemos disfrutado por igual."
    else:
        mee "Me voy. Gracias por todo."
        mc "No tienes por qué darlas."
    if mee._var("route"):
        mc "Y hay que planificar esa cena para que decidas si quieres que seamos una pareja."
        mc "Si lo decides, podrás comunicárselo al resto y evitaremos problemas como el de Tía [bet]."
        scene c22s002_850d with dissolve
        "[mee] se lanza a tus labios y te besa apasionadamente."
        call BlinkXPS3("c22s002_855" , "d") from _call_BlinkXPS3_697
        mee "¿Realmente crees que es necesaria esa cena para que decida?"
        mee "Aunque no te diré mi respuesta ni lo haré oficial hasta después de esa cena."
        mee "Quiero mi cita. *Risa* Soy una mujer clásica."
        mc "Me parece bien."
        call BlinkXPS3("c22s002_860" , "d") from _call_BlinkXPS3_698
    else:
        call BlinkXPS3("c22s002_860" , "d") from _call_BlinkXPS3_699
    mee "Ahora me tengo que ir, de verdad. Necesito saber a qué se refería [bet]."
    mc "Te veo luego."
    if mee._var("route"):
        scene c22s002_850d with dissolve
        "Te da un último beso de despedida antes de irse."
    scene c22s002_825a with dissolve
    "Te quedas sólo en el baño, preguntándote qué quería decir [bet] con \"otra vez\"."
    if mee._var("route"):
        mcp "(Su sorpresa es lógica al encontrar a su hermana con mi polla en la boca.)"
        mcp "(Pero... ¿\"otra vez\"? Como si hubiera pillado a Meemaw con anterioridad...)"
        if persistent.family:
            mcp "(Y, por lo que sé, sólo pudo ser con el abuelo. Es el único hombre con el que ha estado Meemaw.)"
        else:
            mcp "(Y, por lo que sé, sólo pudo ser con John. Es el único hombre con el que ha estado Meemaw.)"
    scene black with dissolve
    "Vas a tu habitación a coger el albornoz y a darte una ducha. Tienes mucho sobre lo que pensar."
    stop music fadeout (1.5)
    "Unos minutos antes..."
    scene c22s002_865a with dissolve
    play music ("music/SneakySnitch.ogg")
    bet "Voy a ver si [mee] y [mc] necesitan ayuda con los masajes. Ha sido una buena sesión de yoga."
    mom "Están en el baño de al lado de la cocina. Pero supongo que ya habrán acabado, ¿no?"
    scene c22s002_865b with dissolve
    bet "Deberían haber acabado, pero a veces los nódulos de [mee] tardan en relajarse. Ayer estuve casi una hora."
    mom "Pues ve a verlos. Aunque ya llevan más de una hora. O esos nódulos están hechos de hormigón o ya habrán acabado. *Risa*"
    scene c22s002_865c with dissolve
    bet "{i}(A veces me gustaría estar en la posición de [mee]. Al menos ella tiene algo de intimidad con [mc].){/i}"
    bet "{i}(No seas injusta, [bet]. Ella tiene galactorrea y ha pasado por un cáncer.){/i}"
    bet "{i}(Sí, pero tiene las manos de [mc] recorriendo su cuerpo...){/i}"
    scene c22s002_865d with dissolve
    if mc._var("relationships")>1 and not mee._var("route"):
        bet "{i}(Lo que daría yo porque me mirase como a una de sus chicas.){/i}"
    elif mc._var("relationships")>2 and mee._var("route"):
        bet "{i}(Lo que daría yo porque me mirase como a una de sus chicas.){/i}"
    elif mc._var("relationships")==2 and mee._var("route"):
        $ gf = mc._var("girlfriend")
        bet "{i}(Lo que daría yo porque me mirase como a [gf].){/i}"
    elif mc._var("relationships")==1 and not mee._var("route"):
        $ gf = mc._var("girlfriend")
        bet "{i}(Lo que daría yo porque me mirase como a [gf].){/i}"
    else:
        bet "{i}(Lo que daría yo porque me mirase como a una mujer en vez de como a su tía abuela.){/i}"
    if oma._var("route"):
        bet "{i}(Pero desde que vi a [mc] y a [oma] en el jacuzzi no me lo puedo quitar de la cabeza...){/i}"
    bet "{i}(¡Eres idiota! Eres monja...){/i}"
    scene c22s002_865e with dissolve
    bet "{i}(Quizás después de la visita a Monterey dejes de serlo...){/i}"
    bet "{i}(¡Sigue soñando! ¿Crees que te va a mirar a ti? ¡Le triplicas la edad!){/i}"
    bet "{i}(Pero qué bonito es soñar...){/i}"
    scene c22s002_825An with dissolve
    stop music fadeout (1.5)
    bet "Hola, venía a ver si necesitabais..."
    scene black with dissolve
    return
label c22s003_AmaCalls:
    if _in_replay:
        call mrS3_rename from _call_mrS3_rename_14
        call mrS3_ama_route from _call_mrS3_ama_route_1
        call mrS3_dap_route from _call_mrS3_dap_route_1
        call mrS3_eri_route from _call_mrS3_eri_route_2
        if mc._var("relationships")<2:
            call mrS3_rels from _call_mrS3_rels_1
        if mc._var("relationships")==1 and not ama._var("route"):
            call mrS3_gf from _call_mrS3_gf_2
            $ gf = mc._var("girlfriend")
        elif mc._var("relationships")==2 and ama._var("route"):
            call mrS3_gf from _call_mrS3_gf_3
            $ gf = mc._var("girlfriend")
    scene black with dissolve
    "Tras salir de una ducha en la que, pese a que le has dado vueltas al asunto de [bet], no has conseguido llegar a ninguna conclusión."
    scene c22s003_005a with fade
    play sound ("music/RingtoneMC.ogg")
    "*Ring-Ring*"
    stop sound
    play music ("music/Sad-Piano.ogg")
    "No podía ser de otra forma, suena el teléfono tan solo unos minutos después de cambiarte de ropa."
    scene c22s003_005b with dissolve
    mc "Buenos días, [ama]. ¿Os encontráis mejor?"
    call BlinkXPS3 ("c22s003_010" , "d") from _call_BlinkXPS3_700
    ama "¿Puedes venir? Es urgente."
    play sound ("music/Desert-Eagle-Gunshot.ogg")
    "*Bang*"
    mc "¿Eso ha sido un disparo? ¿Estáis bien?"
    play sound ("music/Desert-Eagle-Gunshot.ogg")
    "*Bang*"
    call BlinkXPS3 ("c22s003_015" , "d") from _call_BlinkXPS3_701
    ama "Sí. Es [eva]. Por favor, ven cuanto antes."
    play sound ("music/Desert-Eagle-Gunshot.ogg")
    "*Bang*"
    mc "En diez minutos estoy ahí."
    play sound ("music/Desert-Eagle-Gunshot.ogg")
    "*Bang*"
    call BlinkXPS3 ("c22s003_020" , "f") from _call_BlinkXPS3_702
    "Diez minutos después..."
    mc "¿Qué pasa [ama]?"
    "No puedes evitar fijarte en la muñeca encima de la mesa."
    ama "Es [eva]. Está muy jodida desde anoche."
    mc "¿Qué pasó anoche?"
    call BlinkXPS3 ("c22s003_025" , "d") from _call_BlinkXPS3_703
    ama "Nos llamó Aaron. Gavin ha perdido el brazo."
    mc "¿Gavin? ¿Quién es Gavin?"
    call BlinkXPS3 ("c22s003_030" , "d") from _call_BlinkXPS3_704
    ama "Durante el secuestro... en la cocina... El Serie G a quién disparó [eva]."
    mc "¡Hostias! ¡Había olvidado su nombre! Recordaba a Erik y a Grant."
    mc "Parezco tonto... iba a preguntar si está grave."
    call BlinkXPS3 ("c22s003_035" , "d") from _call_BlinkXPS3_705
    ama "Sí, está grave. Fuera de peligro, pero grave."
    ama "Aunque le hicimos los primeros auxilios y lo evacuamos a Aruba en un avión medicalizado, no le han podido salvar el brazo."
    ama "[eva] le destrozó los nervios."
    mc "Pero eran los malos, no se debería sentir así. Nos salvasteis."
    call BlinkXPS3 ("c22s003_040" , "d") from _call_BlinkXPS3_706
    ama "[mc], parte del entrenamiento de los G lo hicieron [eva] y Diana. Conocíamos a los chicos desde que eran niños..."
    mc "Lo entiendo. ¿Cómo está ella?"
    call BlinkXPS3 ("c22s003_045a" , "d") from _call_BlinkXPS3_707
    ama "Muy jodida. Después de vaciar seis cargadores se ha metido en su habitación."
    ama "No quiere hablar conmigo. Por eso te he llamado."
    mc "¿Y cómo estás tú?"
    call BlinkXPS3 ("c22s003_045b" , "d") from _call_BlinkXPS3_708
    ama "Jodida, pero menos. No lo conocía tanto como [eva], y no fui yo quien disparó."
    ama "[eva] es quién necesita hablar ahora mismo, no te preocupes por mí."
    mc "¿Crees que va a querer hablar conmigo?"
    call BlinkXPS3 ("c22s003_050" , "d") from _call_BlinkXPS3_709
    ama "Hasta cierto punto representas la razón por la que disparó."
    ama "No por ti. Por la familia."
    ama "Una familia que ni siquiera sabíamos que teníamos por entonces."
    stop music fadeout (1.5)
    mc "Lo entiendo. Déjame intentarlo. Sólo espero que no me dispare."
    scene c17s005_040b with fade
    play sound ("music/knock.ogg")
    "*Knock-Knock*"
    play music ("music/SadSoul.ogg")
    mc "[eva], soy yo. ¿Puedo pasar?"
    eva "*A través de la puerta* ¡No!"
    mc "No me voy a ir a menos que salgas con un arma y me eches."
    eva "*A través de la puerta* No quiero ver a nadie, [mc]."
    mc "OK. Me voy."
    eva "*A través de la puerta* Gracias por entenderlo, [mc]."
    scene c17s005_040b with fade
    "Esperas un minuto al lado de la puerta antes de volver a llamar."
    play sound ("music/knock.ogg")
    "*Knock-Knock*"
    "No hay respuesta."
    play sound ("music/knock.ogg")
    "*Knock-Knock*"
    eva "*A través de la puerta* ¡Vete, [ama]!"
    mc "*Cambiando la voz* Traigo una entrega para la Srta. [eva] Gilford."
    eva "*A través de la puerta* [mc], no estoy de humor para bromas."
    mc "*Cambiando la voz* Es un abrazo del Sr. [mc] Marks."
    "Pasan unos segundos sin que se oiga nada."
    eva "*A través de la puerta* Pasa..."
    call BlinkXPS3 ("c22s003_055" , "d") from _call_BlinkXPS3_710
    mc "¿Cómo estás?"
    eva "Queriendo estar sola, pero no me dejáis."
    mc "¿Quieres ese abrazo?"
    call BlinkXPS3 ("c22s003_060" , "d") from _call_BlinkXPS3_711
    eva "Te he dicho que no estoy de humor para bromas, [mc]."
    eva "No quiero ponerme borde o maleducada, pero no es el mejor momento."
    mc "OK. Te entiendo."
    mc "¿Te importa si me siento?"
    call BlinkXPS3 ("c22s003_065" , "d") from _call_BlinkXPS3_712
    eva "Lo vas a hacer quiera o no quiera yo, ¿verdad?"
    mc "Sí."
    eva "Entonces siéntate."
    scene c22s003_070An
    "Te sientas en silencio durante un rato, mirándola, contagiándote de su tristeza."
    "No puedes sentirlo por Gavin más allá de que sea una persona que ha perdido un brazo. Una persona que ahora es tu responsabilidad."
    "Entraron en casa de tu familia y os amenazaron. Pusieron en peligro a [nor], [bet] y [mee]."
    "Ahora conoces su historia a través de las historias de [eva] y [ama]. Notas algo de empatía hacia él creciendo en ti."
    "Pero lo que te está rompiendo el alma es ver a [eva]."
    "Ver cómo juega con Fee mientras las lágrimas están a punto de asomar a sus ojos."
    "Decides levantarte."
    call BlinkXPS3 ("c22s003_075" , "d") from _call_BlinkXPS3_713
    eva "¿Ya te vas?"
    stop music fadeout (1.5)
    mc "No, no te vas a librar tan rápido de mí."
    play music ("music/Retrospection.ogg")
    scene c22s003_080d with dissolve
    mc "El abrazo que traía estaba a punto de caducar."
    scene c22s003_080e with dissolve
    eva "Gracias..."
    "Os pasáis un rato abrazados en silencio antes de que [eva] diga algo."
    call BlinkXPS3 ("c22s003_080" , "d") from _call_BlinkXPS3_714
    eva "No te vas a ir hasta que hable contigo de lo que me pasa, ¿verdad?"
    mc "Yo solo estoy disfrutando del abrazo. Si quieres hablar de ello, habla. Si no quieres, podemos seguir en silencio."
    mc "No me voy a ir a ninguna parte. Ni ahora ni nunca."
    call BlinkXPS3 ("c22s003_085" , "d") from _call_BlinkXPS3_715
    eva "Es que no lo vas a entender..."
    mc "Dame una oportunidad. No soy tan tonto como parezco."
    mc "Al menos a veces..."
    call BlinkXPS3 ("c22s003_090" , "d") from _call_BlinkXPS3_716
    eva "*Risa triste* Sólo a veces..."
    mc "Bueno, alguna que otra vez. Ahora he sido tan listo como para conseguir entrar en tu fortaleza. *Risa*"
    call BlinkXPS3 ("c22s003_095" , "d") from _call_BlinkXPS3_717
    eva "En más de un sentido..."
    eva "No sé qué tienes, pero haces que la gente se sienta cómoda hablando."
    mc "Será mi don de gentes. A veces puedo ser encantador."
    call BlinkXPS3 ("c22s003_100" , "d") from _call_BlinkXPS3_718
    eva "Gavin ha perdido el brazo, aunque supongo que [ama] ya te lo ha contado."
    mc "Sí, me lo ha contado."
    call BlinkXPS3 ("c22s003_105" , "d") from _call_BlinkXPS3_719
    eva "Si hubiera apuntado un par de centímetros a la derecha no hubiera pasado."
    mc "Y si no hubieras disparado, te hubiera disparado él."
    call BlinkXPS3 ("c22s003_110" , "d") from _call_BlinkXPS3_720
    eva "Gavin tenía la puntería de un stormtrooper. Nunca conseguí que mejorara."
    eva "Sin embargo, era bueno en el cuerpo a cuerpo."
    mc "¿Lo conocías mucho? Me refiero aparte del entrenamiento."
    call BlinkXPS3 ("c22s003_115" , "d") from _call_BlinkXPS3_721
    eva "Imagínate convivir con 500 personas las 24 horas del día durante 19 años. Cuando no estábamos en misiones, claro."
    eva "Doce o trece años en el caso de los G. Sí, nos conocíamos. No, no éramos amigos, pero nos llevábamos bien."
    mc "Entiendo..."
    call BlinkXPS3 ("c22s003_120" , "d") from _call_BlinkXPS3_722
    eva "No, [mc]. No lo puedes entender. Tenía mis órdenes y las cumplí. Y alguien salió herido en el proceso. Irreversiblemente."
    eva "Pero conocía a ese alguien."
    eva "He matado a gente, [mc]. Soy una puta asesina. Pero nunca había hecho daño a alguien a quien conociera."
    eva "O a alguien que no se lo mereciera."
    mc "¿Nunca?"
    call BlinkXPS3 ("c22s003_125" , "d") from _call_BlinkXPS3_723
    eva "No así, al menos."
    eva "Tu primer domingo aquí, evité que otro serie G os matara, en el bosque."
    mc "¿Cuando estaba con [eil]?"
    call BlinkXPS3 ("c22s003_130" , "d") from _call_BlinkXPS3_724
    eva "No, mientras vosotros comíais en casa. En el bosque estábamos él y yo. Él tenía un rifle de francotirador."
    eva "Sólo necesité un disparo de advertencia para que Gustav bajara el arma y pudiera apresarlo y traerlo a la base."
    eva "Aparte de un ataque de nervios, no recibió más daños."
    mc "No sé cómo darte las gracias por eso..."
    call BlinkXPS3 ("c22s003_135" , "d") from _call_BlinkXPS3_725
    eva "No hace falta que me las des. Eran mis órdenes. No lo hacía por ti, ni por la familia."
    eva "No erais nuestra familia aún. Ni siquiera lo erais el día del secuestro."
    mc "Lo sé..."
    call BlinkXPS3 ("c22s003_140" , "d") from _call_BlinkXPS3_726
    eva "Nunca he estado en las circunstancias en las que estuvieron Beatrice, Claire, o Diana."
    eva "Nunca tuve que luchar por mi vida contra nuestra gente."
    eva "Y la primera vez que lo hago, alguien sale herido."
    mc "Ellos querían hacernos daño, [eva]."
    call BlinkXPS3 ("c22s003_145" , "d") from _call_BlinkXPS3_727
    eva "Lo sé. Y Eric nos hubiese matado si hubiera tenido la oportunidad, como hicieron con mis hermanas."
    eva "Pero Gavin no. Gavin estaba ahí cumpliendo órdenes. Igual que yo. Y no se merecía acabar así..."
    mc "No quiero sonar insensible, pero prefiero que sea él quien haya acabado así en vez de ser tú."
    call BlinkXPS3 ("c22s003_150" , "d") from _call_BlinkXPS3_728
    eva "Gracias. Yo... Gracias..."
    call BlinkXPS3 ("c22s003_155" , "d") from _call_BlinkXPS3_729
    eva "No te puedes imaginar lo complicado que es todo en mi cabeza."
    eva "He herido a una persona a la que aprecio por salvar a una familia a la que quiero."
    eva "No sé qué le voy a decir la próxima vez que le vea..."
    mc "Los dos cumplíais órdenes, y tú estabas en el bando ganador."
    mc "Tú hiciste que ese bando ganara."
    call BlinkXPS3 ("c22s003_160" , "d") from _call_BlinkXPS3_730
    eva "Pero no se tenía que haber llegado a esto. Ha muerto gente en esta guerra clon. Mis hermanas."
    eva "Gavin ha perdido el brazo..."
    mc "Y Eric los dientes..."
    call BlinkXPS3 ("c22s003_165" , "d") from _call_BlinkXPS3_731
    eva "Eric es quien menos me importa. Los E tenían una vena cruel."
    mc "¿Clonamos dientes en NTR? *Risa*"
    call BlinkXPS3 ("c22s003_170" , "d") from _call_BlinkXPS3_732
    eva "*Risa triste* No, y tampoco brazos."
    eva "¿Qué va a hacer ahora?"
    mc "Supongo que le podemos buscar un puesto donde siga siendo útil con un solo brazo y donde se sienta a gusto."
    mc "Ahora soy su jefe y una de las cosas que debe hacer un jefe es conseguir sacar el mejor partido de sus empleados."
    call BlinkXPS3 ("c22s003_175" , "d") from _call_BlinkXPS3_733
    eva "No sé qué podría hacer con un solo brazo, la verdad..."
    eva "No sé qué podría hacer yo si sólo tuviera un brazo."
    mc "Seguramente patearías culos con un solo brazo, pero ¿sabes una cosa?"
    stop music fadeout (1.5)
    $ eva._var("chanceRoute", True)
    if persistent.walkthrough:
        $ wt1 = _("[gr]Ruta con [eva] abierta.")
        $ wt2 = _("[red]Ruta con [eva] cerrada.\n [red]ADVERTENCIA: No habrá más oportunidades de abrir la ruta con [eva].")
    else:
        $ wt1 = ""
        $ wt2 = ""
    menu:
        "Prefiero que mi pareja tenga los dos brazos." (wt=wt1):
            $ eva._var("route", True)
            $ mc._var("relationships", 1, "add")
            call c22s004_EveRoute from _call_c22s004_EveRoute
        "Prefiero que mi nueva prima tenga los dos brazos." (wt=wt2):
            call c22s004_EveNoRoute from _call_c22s004_EveNoRoute
    $ resetWalkthrough ()
    return
label c22s004_EveRoute:
    play music ("music/Looking-Forward.ogg")
    call BlinkXPS3 ("c22s003_180" , "h") from _call_BlinkXPS3_734
    eva "¿Qué? ¿Pareja? ¿Como si fuera tu novia?"
    mcp "(¡Por Dios! ¡Cómo odio esa palabra!)"
    mc "Sí, he dicho pareja. Como si fueras novia. ¿Demasiados disparos están afectando a tu audición?"
    call BlinkXPS3 ("c22s003_185" , "h") from _call_BlinkXPS3_735
    "[eva] salta como impulsada por un muelle."
    eva "¿Me estás tomando el pelo?"
    mc "No."
    call BlinkXPS3 ("c22s003_190" , "d") from _call_BlinkXPS3_736
    eva "¿Lo estás haciendo porque te doy pena?"
    mc "No."
    call BlinkXPS3 ("c22s003_195" , "d") from _call_BlinkXPS3_737
    eva "¿Entonces por qué? ¿Por qué ahora?"
    mc "Porque me gustas desde que te conocí... más o menos."
    mc "Y porque ahora [ama] y tú habéis arreglado vuestras diferencias."
    mc "¿No puedes aceptar una buena noticia cuando la escuchas? O lo que para ti es una buena noticia..."
    call BlinkXPS3 ("c22s003_200" , "d") from _call_BlinkXPS3_738
    eva "¿Y [ama]?"
    mc "[ama] no tiene nada que ver con lo que hagamos tú y yo."
    eva "¿Crees que se va a enfadar porque me hayas elegido a mí antes que a ella? También vas a querer salir con ella, ¿verdad?"
    mcp "(No le ha dicho lo que pasó ayer en el café.)"
    mc "No, no creo que se enfade."
    mc "Y no te tienes que preocupar por si salgo con ella o no. No sois un pack indivisible como los yogures."
    call BlinkXPS3 ("c22s003_205" , "d") from _call_BlinkXPS3_739
    eva "Pero..."
    mc "Yo esperaba un beso en vez de un interrogatorio."
    scene c22s003_210d with hpunch
    "La asesina pelirroja se lanza hacia ti, tumbándote en el arcón, y empieza a recorrer tus labios con ansia."
    "Y mucha más torpeza de la que hubieras esperado."
    call BlinkXPS3 ("c22s003_210" , "d") from _call_BlinkXPS3_740
    eva "¿Contento?"
    mc "Sí. ¿Y tú?"
    call BlinkXPS3 ("c22s003_215" , "d") from _call_BlinkXPS3_741
    eva "Ermmm... Sí..."
    mc "No creo que estés muy convencida."
    call BlinkXPS3 ("c22s003_220" , "d") from _call_BlinkXPS3_742
    eva "Me siento rara... hace unos minutos tenía ganas de llorar."
    eva "Ahora tengo ganas de reír. Y de llorar a la vez..."
    mc "Supongo que estás en medio de una montaña rusa emocional."
    call BlinkXPS3 ("c22s003_225" , "d") from _call_BlinkXPS3_743
    eva "Supongo... No sé cómo actuar ahora..."
    mc "¿Qué tal un largo abrazo? No hace falta que digas nada si no quieres."
    call BlinkXPS3 ("c22s003_230" , "d") from _call_BlinkXPS3_744
    eva "Creo que me puedo conformar con eso."
    mc "*Risa* No sé si sentirme como que mis abrazos son un premio menor."
    call BlinkXPS3 ("c22s003_235" , "d") from _call_BlinkXPS3_745
    eva "No te rías de mí. Lo que sí sé es que quiero tener una cita contigo."
    mc "¿Quieres que busque un sitio bonito?"
    call BlinkXPS3 ("c22s003_240" , "d") from _call_BlinkXPS3_746
    eva "No. Quiero planear la cita yo."
    eva "Estoy segura de que has tenido mil citas y no quiero que sea como ninguna que hayas tenido con anterioridad."
    mc "Me parece bien. Sorpréndeme."
    call BlinkXPS3 ("c22s003_245" , "v") from _call_BlinkXPS3_747
    eva "¡Mierda!"
    mc "¿Qué pasa, cielo?"
    call BlinkXPS3 ("c22s003_250" , "d") from _call_BlinkXPS3_748
    eva "Se lo tengo que contar a [ama]. Ahora."
    eva "Levántate. Vamos a decírselo. No quiero que piense que se lo estamos ocultando."
    mc "*Risa* Lo de estar quieta disfrutando del abrazo no se te da muy bien. Vamos."
    call BlinkXPS3 ("c22s003_255" , "f") from _call_BlinkXPS3_749
    eva "[ama], tenemos algo que decirte."
    call BlinkXPS3 ("c22s003_260" , "d") from _call_BlinkXPS3_750
    ama "¿Te encuentras mejor?"
    call BlinkXPS3 ("c22s003_265" , "d") from _call_BlinkXPS3_751
    eva "Mas o menos. Todavía me siento mal por Gavin..."
    eva "Pero... queríamos decirte que..."
    call BlinkXPS3 ("c22s003_270" , "d") from _call_BlinkXPS3_752
    eva "Ayúdame, [mc]..."
    mc "Nope. Esto es algo que tienes que hacer tú."
    call BlinkXPS3 ("c22s003_275" , "d") from _call_BlinkXPS3_753
    eva "*Grrr* ¡Capullo!"
    eva "¡Vale!"
    call BlinkXPS3 ("c22s003_280" , "h") from _call_BlinkXPS3_754
    eva "¡[mc] y yo estamos saliendo juntos! Aunque no sé por qué salgo con capullos."
    eva "¡Vamos a tener una cita!"
    call BlinkXPS3 ("c22s003_285" , "d") from _call_BlinkXPS3_755
    eva "Y nos hemos besado..."
    call BlinkXPS3 ("c22s003_295" , "h") from _call_BlinkXPS3_756
    ama "¡Eso es fantástico, [eva]!"
    call BlinkXPS3 ("c22s003_290" , "d") from _call_BlinkXPS3_757
    ama "Felicidades, [mc]. No podrías salir con nadie mejor."
    scene c22s003_300 with dissolve
    eva "Ahora solo falta que se decida contigo."
    if ama._var("route"):
        eva "Obviamente, me ha elegido a mi primero, pero me gustaría que también tú pudieras salir con él."
        call c22s004_Convo from _call_c22s004_Convo
        mcp "(No sé a qué juega, pero será mejor seguirle el juego. *Risa mental*)"
        call BlinkXPS3 ("c22s003_320" , "d") from _call_BlinkXPS3_758
        ama "Aunque si [mc] quiere salir conmigo, sabe lo que yo pienso y lo puede decir {b}ahora mismo{/b}."
        mc "Me encantaría. Estar con las dos sería maravilloso."
        scene c22s003_325a with hpunch
        eva "¡Felicidades, [ama]!"
        eva "¡Nuestro primer novio oficial y lo compartimos!"
        mc "¿Qué es eso del primer novio oficial?"
        scene c22s003_325d with dissolve
        eva "En una misión en Budapest tuvimos que fingir que salíamos con dos operativos de la serie F."
        ama "Ellos se hacían pasar por gemelos ricos y nosotras por sus novias."
        scene c22s003_325e with hpunch
        eva "¡Pero nunca pasó nada entre nosotros!"
        ama "Más allá de algún beso fingido."
        scene c22s003_330 with hpunch
        eva "¡Oops! ¡Te he abrazado y no te he dejado besar a tu novio!"
        mcp "(Cada vez odio más la palabra. Pero en esto es como una niña, y necesita poner etiquetas.)"
        scene c22s003_335 with dissolve
        ama "¿Puedo?"
        eva "¡Di que sí!"
        ama "*Susurrando* Me da un poco de vergüenza delante de [eva]."
        mc "Sólo hay una forma de superar la vergüenza, preciosa."
        scene c22s003_335d with dissolve
        "Sin dejarle responder, tu boca se acerca a la suya y le das un tierno beso."
        "Ella responde de forma mucho menos apasionada que el día anterior en el café."
        "La vergüenza es una barrera que le cuesta superar."
        call BlinkXPS3 ("c22s003_340" , "d") from _call_BlinkXPS3_759
        mc "¿Bien?"
        ama "Bien."
        call BlinkXPS3 ("c22s003_345" , "d") from _call_BlinkXPS3_760
        eva "¿Bien? ¡Ha sido precioso!"
        if mc._var("relationships")==3:
            if mar._var("route"):
                $ mc._var("girlfriend", mar.name.first_name)
            elif sai._var("route"):
                $ mc._var("girlfriend", sai.name.first_name)
            elif emm._var("route"):
                $ mc._var("girlfriend", emm.name.first_name)
            elif eri._var("route"):
                $ mc._var("girlfriend", eri.name.first_name)
            elif dap._var("route"):
                $ mc._var("girlfriend", dap.name.first_name)
            elif nor._var("route"):
                $ mc._var("girlfriend", nor.name.first_name)
            elif sca._var("route"):
                $ mc._var("girlfriend", sca.name.first_name)
            elif eil._var("route"):
                $ mc._var("girlfriend", eil.name.first_name)
            elif sam._var("route"):
                $ mc._var("girlfriend", sam.name.first_name)
            elif sim._var("route"):
                $ mc._var("girlfriend", sim.name.first_name)
            elif oma._var("route"):
                $ mc._var("girlfriend", oma.name.first_name)
            elif mad._var("route"):
                $ mc._var("girlfriend", mad.nick)
            elif meg._var("route"):
                $ mc._var("girlfriend", meg.name.first_name)
            elif deb._var("route"):
                $ mc._var("girlfriend", deb.nick)
            elif kia._var("route"):
                $ mc._var("girlfriend", kia.name.first_name)
        if mc._var("relationships")>3:
            eva "¡Ha sido como cuando besa a las otras chicas!"
        elif mc._var("relationships")==3:
            $ gf = mc._var("girlfriend")
            eva "Ha sido como cuando besa a [gf]."
        mc "¿Cómo querías que fuera?"
        call BlinkXPS3 ("c22s003_350" , "d") from _call_BlinkXPS3_761
        eva "No tengo ni idea... pero presenciar vuestro primer beso me ha hecho sentir especial."
        call BlinkXPS3 ("c22s003_355" , "d") from _call_BlinkXPS3_762
        eva "¡Tengo que irme!"
        mc "¿Dónde?"
        eva "¡Tengo que poner un mensaje en el grupo de WhatsUp! ¡Quiero que todas sepan que las dos estamos contigo!"
        scene c22s003_355An with dissolve
        eva "Y tengo que ducharme. Apesto."
        scene c22s003_360AnBlink with dissolve
        pause (2.0)
        mc "Y se fue."
        ama "Sí. Gracias por seguirme el juego."
        mc "¿A qué venía eso?"
        call BlinkXPS3 ("c22s003_365" , "d") from _call_BlinkXPS3_763
        ama "Ayer, cuando llegué, quería contárselo, pero [eva] estaba muy cansada y se fue a dormir en seguida. La tenía que despertar para ir a casa a cenar."
        ama "La despertó la llamada de [aar]. Y se puso como la has visto cuando has llegado."
        mc "Por eso llamaste para decir que no os encontrabais bien, ¿no?"
        call BlinkXPS3 ("c22s003_370" , "d") from _call_BlinkXPS3_764
        ama "Exacto. Ella no estaba de humor para socializar, y yo no quería dejarla sola, por muchas ganas que tuviera de volver a verte. De veros a todos."
        ama "Después de la llamada, no estaba de humor para nada, menos aún para que se lo contara."
        call BlinkXPS3 ("c22s003_375" , "d") from _call_BlinkXPS3_765
        ama "Ya has visto lo feliz que le ha hecho que la \"eligieras antes que a mí\"."
        mc "Si se lo hubieras dicho, se hubiera sentido más miserable aún, sumado a lo de Gavin."
        call BlinkXPS3 ("c22s003_380" , "d") from _call_BlinkXPS3_766
        ama "Exacto. Por eso envié el mensaje individualmente a todas las chicas."
        mc "Hablando del mensaje. Deberías avisar a [emm] de que no le responda diciendo que ya sabía lo tuyo."
        mc "Si lo lee en el grupo, es capaz de descubrirte."
        call BlinkXPS3 ("c22s003_385" , "d") from _call_BlinkXPS3_767
        ama "*Risa* No te preocupes."
        ama "Llamé a [emm] después de enviar el mensaje y le dije que, hasta que [eva] no dijera algo o yo lo publicara en el grupo, ella no sabía nada."
        mc "Me sorprende lo mucho que nos conoces, [ama]."
        call BlinkXPS3 ("c22s003_395" , "d") from _call_BlinkXPS3_768
        ama "*Risa* Gajes del oficio."
    else:
        call c22s004_Convo from _call_c22s004_Convo_1
        mcp "(No sé a qué juega, pero será mejor seguirle el juego.)"
        call BlinkXPS3 ("c22s003_320" , "d") from _call_BlinkXPS3_769
        ama "[mc] y yo decidimos ayer que no vamos a salir juntos de momento."
        ama "Entre otras cosas, con la preparación del viaje a Aruba y todo lo que hay que hacer, hubiera sido una distracción."
        mc "Entre otras cosas..."
        scene c22s003_400 with dissolve
        eva "Entonces yo también debería dejar de salir con él, ¿no?"
        ama "No hace falta. Las preparaciones las estoy llevando a cabo yo."
        ama "Tú disfruta de tu novio y yo me ocupo del resto."
        scene c22s003_325e with hpunch
        eva "¡Gracias, [ama]! ¡Eres la mejor hermana del mundo!"
        call BlinkXPS3 ("c22s003_405b" , "d") from _call_BlinkXPS3_770
        ama "Os voy a dejar solos un rato... Tengo cosas que hacer."
        call BlinkXPS3 ("c22s003_355" , "d") from _call_BlinkXPS3_771
        eva "¡No hace falta! ¡Tengo que irme!"
        mc "¿Dónde?"
        eva "¡Tengo que poner un mensaje en el grupo de WhatsUp! ¡Quiero que todas sepan que estamos juntos!"
        scene c22s003_355An with dissolve
        eva "Y tengo que ducharme. Apesto."
        scene c22s003_360AnBlink with dissolve
        pause (2.0)
        mc "Y se fue."
        ama "Sí. Gracias por seguirme el juego."
        mc "¿A qué venía eso?"
        call BlinkXPS3 ("c22s003_365" , "d") from _call_BlinkXPS3_772
        ama "Ayer, cuando llegué, quería contárselo, pero [eva] estaba muy cansada y se fue a dormir en seguida. La tenía que despertar para ir a casa a cenar."
        ama "La despertó la llamada de [aar]. Y se puso como la has visto cuando has llegado."
        mc "Por eso llamaste para decir que no os encontrabais bien, ¿no?"
        call BlinkXPS3 ("c22s003_370" , "d") from _call_BlinkXPS3_773
        ama "Exacto. Ella no estaba de humor para socializar, y yo no quería dejarla sola, por muchas ganas que tuviera de volver a veros a todos."
        ama "Después de la llamada, no estaba de humor para nada, menos aún para que se lo contara."
        call BlinkXPS3 ("c22s003_375" , "d") from _call_BlinkXPS3_774
        ama "Por eso tampoco le he dicho toda la verdad. No quiero estropear su felicidad ahora mismo."
        ama "Mejor ocultar un poco la verdad, aunque no sea mentira del todo."
        mc "Entre otras cosas..."
        call BlinkXPS3 ("c22s003_380" , "d") from _call_BlinkXPS3_775
        ama "Exacto. Hubiera sido una distracción empezar a salir contigo ahora, aunque no me importaría tener esa distracción. Hay otras razones, obviamente."
        ama "Pero no quiero que se sienta mal porque la hayas elegido a ella y no a mí."
        mc "Ciertamente, eres una muy buena hermana."
    scene c22s003_485d with fade
    stop music fadeout (1.5)
    "En ese momento suena tu teléfono."
    return
label c22s004_Convo:
    scene c22s003_305 with dissolve
    ama "No te preocupes por eso, habrá tiempo para decidirnos. Ahora tenéis que disfrutar vosotros."
    scene c22s003_310 with dissolve
    ama "Pero antes, tienes que recoger esas cajas de munición."
    scene c22s003_315An with dissolve
    eva "¿Qué cajas?"
    ama "¡Ah, no! Ya las he recogido yo. Me había olvidado..."
    return
label c22s004_EveNoRoute:
    call c00Renames from _call_c00Renames
    call changenicks from _call_changenicks_1
    play music ("music/Majestica.ogg")
    call BlinkXPS3 ("c22s003_410" , "d") from _call_BlinkXPS3_776
    eva "Has dicho prima y no novia."
    $ cousins = ""
    if dap._var("route"):
        if eri._var("route"):
            eva "Supongo que no te refieres a lo que haces con [dap.nick] y [eri.nick]..."
        else:
            eva "Supongo que no te refieres a lo que haces con [dap.nick]..."
    else:
        if eri._var("route"):
            eva "Supongo que no te refieres a lo que haces con [eri.nick]..."
    mc "[eva], te quiero, pero no de esa forma."
    mc "Quizás no sea el mejor momento para decirte algo así, pero tengo que ser sincero contigo y evitar que te hagas falsas esperanzas."
    call BlinkXPS3 ("c22s003_415" , "h") from _call_BlinkXPS3_777
    "Salta como impulsada por un resorte."
    eva "Pues llegas un poco tarde para eso... ¿Quieres que cambie algo de mí?"
    if dap._var("route"):
        eva "Creía que... tengo la cara de [dap.nick]... ¿Quieres que me haga una trenza?"
    elif eri._var("route"):
        eva "Creía que... tengo la cara de [eri.nick]... ¿Quieres que me haga gótica?"
    mc "No, [eva]. Eres perfecta tal como eres, pero no siento por ti lo que quieres que sienta."
    call BlinkXPS3 ("c22s003_420" , "d") from _call_BlinkXPS3_778
    eva "¿Entonces por qué no?"
    mc "Porque no le puedo decir al corazón de quién tiene que enamorarse."
    mc "Lo último que quiero es hacerte daño. Eres una mujer maravillosa, pero no siento nada romántico por ti."
    mc "Lo siento."
    call BlinkXPS3 ("c22s003_425" , "d") from _call_BlinkXPS3_779
    eva "Me siento como una idiota ahora mismo."
    mc "No tienes que sentirte así. Nadie elige de quién se enamora."
    eva "No me refiero a eso..."
    mc "¿Entonces a qué te refieres?"
    call BlinkXPS3 ("c22s003_430" , "d") from _call_BlinkXPS3_780
    eva "A que te estoy pidiendo explicaciones sobre algo que no tengo ningún derecho a hacer."
    mc "Eso casi suena como [ama]. Pero siempre me podrás pedir explicaciones sobre lo que quieras."
    if dap._var("route") or eri._var("route"):
        call BlinkXPS3 ("c22s003_435" , "d") from _call_BlinkXPS3_781
        eva "Incluso te he propuesto cambiar físicamente. Es algo que no debería hacer."
        eva "Yo soy yo y no tengo que parecerme a nadie."
        mc "Voy a repetirlo, [eva]. Eres perfecta como eres, pero yo no soy perfecto para ti."
    call BlinkXPS3 ("c22s003_440" , "d") from _call_BlinkXPS3_782
    eva "Y además, me he comportado muy mal con [ama] desde ayer."
    eva "Ella también conocía a Gavin, aunque no había tenido tanto trato con él como yo. También lo debe estar pasando mal."
    mc "Deberías hablar con ella y disculparte, si crees que lo has hecho mal."
    call BlinkXPS3 ("c22s003_445" , "d") from _call_BlinkXPS3_783
    eva "¿Puedes esperar aquí mientras hablo con ella?"
    eva "Me gustaría hablar en privado, si no te molesta."
    mc "Ningún problema. Es vuestra conversación y tus disculpas."
    eva "Te veo en cinco minutos."
    scene black with dissolve
    "Nunca te fíes de una mujer hermosa cuando diga cinco minutos."
    call BlinkXPS3 ("c22s003_450" , "f") from _call_BlinkXPS3_784
    "Tras quince minutos de mirar el móvil, aparece [eva] de nuevo."
    eva "Ya está. Ya me he disculpado."
    mc "¿Estás mejor?"
    call BlinkXPS3 ("c22s003_455" , "d") from _call_BlinkXPS3_785
    eva "Mucho mejor. Sienta bien quitarse ese peso de encima."
    if ama._var("route"):
        call BlinkXPS3 ("c22s003_460" , "d") from _call_BlinkXPS3_786
        eva "Por cierto, felicidades. No vas a encontrar a nadie mejor que mi hermana."
        scene c22s003_465 with dissolve
        eva "Bueno, sí, pero no quieres salir conmigo. *Risa*"
        mc "No sabía que te lo iba a decir ahora."
        call BlinkXPS3 ("c22s003_470" , "d") from _call_BlinkXPS3_787
        eva "Cuando llegó ayer yo estaba molida. Quería contármelo cuando me despertara, antes de ir a cenar a casa."
        eva "Pero me despertó la llamada de Aaron para decirnos lo de Gavin."
        eva "Supongo que me puse demasiado borde y no quería contármelo entonces."
        mc "Sabes que a mí no me gustan los secretos."
        call BlinkXPS3 ("c22s003_475" , "d") from _call_BlinkXPS3_788
        eva "Lo sé. Y en este caso era justificado. No sé cómo hubiera recibido la noticia antes de que llegaras."
        eva "Tus abrazos tienen algo de curativo. ¿Te lo han dicho alguna vez?"
        mc "*Risa* Sí, alguna vez me lo han dicho."
    scene c22s003_480AnBlink with dissolve
    eva "Ahora vas a tener que irte. Quiero ducharme. Apesto."
    eva "[ama] quería hablar contigo sobre algo del viaje a Aruba."
    mc "¿Te veo luego?"
    eva "¡Por supuesto!"
    scene c22s003_485d with fade
    stop music fadeout (1.5)
    "Nada más entrar en la sala de control, suena tu teléfono"
    return
label c22s003_IronFistCalls:
    if _in_replay:
        call mrS3_rename from _call_mrS3_rename_15
        call mrS3_ama_route from _call_mrS3_ama_route_2
        call mrS3_eva_route from _call_mrS3_eva_route
    play sound ("music/RingtoneMC.ogg")
    "*Ring-Ring*"
    stop sound
    mcp "(Número desconocido...)"
    scene c22s003_485e with dissolve
    play music ("music/Inspire.ogg")
    mc "Hola, [mc] Marks al habla."
    mcp "(Acabo de sonar super ridículo.)"
    man "Buenos días, Sr. Marks. Le llamo de Iron Fist, soy Jeff Sound, el asistente del Sr. Ichigo, Vicepresidente de Operaciones."
    mc "Un momento, Sr. Sound. Le pongo en manos libres, tengo una persona de mi equipo aquí que va a estar interesada en esta conversación."
    $ jef = TGCharacter ("Jeff Sound", color = "#ffffff")
    jef "Ningún problema, Sr. Marks."
    call BlinkXPS3 ("c22s003_485" , "d") from _call_BlinkXPS3_789
    ama "Buenos días, Sr. Sound. Soy [ama] Gilford. Le escucho bien."
    jef "Encantado de hablar con usted, Srta. Gilford. ¿O es Sra.?"
    call BlinkXPS3 ("c22s003_490" , "d") from _call_BlinkXPS3_790
    ama "Srta. está bien."
    mc "Dígame, Sr. Sound."
    jef "Les llamo porque han llegado a nosotros informaciones sobre el cambio de propiedad de NTR y..."
    mc "¿Me puede decir de dónde han sacado esa información? ¿Y este número de teléfono?"
    jef "Esa es una información reservada, Sr. Marks. No podemos revelar nuestras fuentes."
    call BlinkXPS3 ("c22s003_495" , "d") from _call_BlinkXPS3_791
    ama "Estaba hablando usted del cambio de propiedad de NTR. Siga, por favor."
    jef "Sí. Nos hemos enterado del cambio de propiedad y de que ésta ha recaído en un grupo representado por el Sr. Marks."
    ama "Exacto."
    jef "También nos han llegado noticias de que el Sr. Marks va a ocupar el puesto de CEO en breve."
    ama "Sí. Esas informaciones son exactas."
    jef "¿Me podrían decir quién es ese grupo de accionistas, por favor?"
    scene c22s003_500An with dissolve
    mc "Son..."
    ama "No creo que sea de su interés, Sr. Sound. Están representados por el Sr. Marks y él es capaz de hablar por ellos."
    ama "¿Quería algo más?"
    jef "También llamaba porque al Sr. Ichigo le gustaría reunirse con el Sr. Marks."
    mc "¿Por alguna razón en concreto?"
    jef "Una primera toma de contacto entre dos de las principales empresas del sector. El Sr. Ichigo se había reunido varias veces con el Sr. Daniels."
    call BlinkXPS3 ("c22s003_505" , "d") from _call_BlinkXPS3_792
    ama "*Pone el móvil en mute* Xabier Daniels era el jefe de GILF que empezó la Guerra Clon."
    "Asientes."
    mc "Desafortunadamente, el Sr. Daniels ya no trabaja con nosotros, pero si se trata de una visita de cortesía, no tengo ningún problema en conocer al Sr. Ichigo."
    jef "Muchas gracias, Sr. Marks. El Sr. Ichigo estará en Vandenberg mañana por la tarde, y dará una recepción para algunos clientes en su yate por la noche."
    jef "Le gustaría que acudiera."
    call BlinkXPS3 ("c22s003_510" , "d") from _call_BlinkXPS3_793
    ama "Imposible. El Sr. Marks tiene la agenda ocupada hasta el viernes. Debería ser a partir del sábado."
    jef "Déjeme mirar un tema. Un momento..."
    jef "El sábado es un buen día. Hay un evento más pequeño en el yate frente al puerto de Westport. Tendrán más oportunidades de conocerse."
    scene c22s003_515AnBlink with dissolve
    ama "El sábado entonces. ¿Transporte?"
    jef "Podemos enviar un helicóptero a recoger al Sr. Marks."
    ama "Y a mí. Iremos juntos."
    jef "Perfecto. Nos tendrán que indicar dónde quieren que les recojamos."
    scene c22s003_515An with dissolve
    "[ama] continúa atando detalles de la reunión, dando indicaciones y detalles, pero sin revelar ninguna información."
    "Consigue algunos nombres de las personas que asistirán al evento menor, y el Sr. Sound se compromete a enviarle la lista completa de invitados."
    "Aunque vaya vestida de mecánico, es mucho mejor en esto de lo que tú serías con un traje."
    "Unos minutos después os despedís del Sr. Sound."
    call BlinkXPS3 ("c22s003_520" , "f") from _call_BlinkXPS3_794
    ama "Ya está. El sábado nos reunimos con Ichigo."
    mc "He estado a punto de meter la pata con lo de los accionistas, ¿verdad?"
    call BlinkXPS3 ("c22s003_525" , "d") from _call_BlinkXPS3_795
    ama "Sí, un poco. Nunca des información si no es necesario. Si no tienen los nombres de los accionistas tienen que pasar por ti para todo."
    ama "Es nuestra forma de controlar el flujo de información. Cuánto más anónimas sean las chicas, mejor. No podrán contactarlas directamente."
    mc "Me viene muy grande todo esto."
    call BlinkXPS3 ("c22s003_530" , "d") from _call_BlinkXPS3_796
    ama "No te preocupes, aprenderás. Esto es nuevo para ti, pero al menos te das cuenta de cuándo estás a punto de cometer un error."
    ama "Lo que tienes que aprender es a darte cuenta antes de cometerlo."
    mc "Si no hubieras estado aquí... hubiera aceptado la reunión de mañana. ¿Por qué la has rechazado?"
    scene c22s003_535d with dissolve
    ama "*Risa* Porque la han propuesto ellos. Si nos negamos a su primera propuesta, se pueden poner ansiosos."
    ama "Si aceptamos una propuesta así con tan poca antelación, parece que estemos besándoles el culo."
    call BlinkXPS3 ("c22s003_535" , "d") from _call_BlinkXPS3_797
    ama "De esta forma demostramos que son ellos los que tienen interés y no nosotros."
    ama "Si no hubieran tenido el evento del sábado, posiblemente se hubieran tenido que inventar algo para forzar esa reunión informal."
    mc "Que de informal tendrá poco, ¿no?"
    call BlinkXPS3 ("c22s003_540" , "d") from _call_BlinkXPS3_798
    ama "Poquísimo. Vandenberg es una base de la Fuerza Aérea, más dedicada al espacio que a algo con lo que Iron Fist tenga algo que ver."
    ama "Te querían demostrar que son fuertes y que tienen contactos en todos lados. No te conocen y te quieren impresionar."
    ama "Seguro que al evento en Westport va algún coronel de Fort Hunter Liggett. Está a menos de dos horas."
    mc "Hay demasiados matices en todo esto y yo no tengo ni idea... Creo que tú, [eva], o [aar] seríais mejores CEO que yo."
    call BlinkXPS3 ("c22s003_545" , "d") from _call_BlinkXPS3_799
    ama "Nosotros somos operativos de campo. No tenemos ni idea de cómo gestionar una empresa, pero conocemos el negocio."
    ama "Nuestro problema es de visión, al menos el mío. Tengo una visión limitada del conjunto."
    ama "[aar] no es una figura cómoda en NTR para los que trabajaron bajo las órdenes de Xabier."
    ama "Y [eva] tiene el problema del martillo."
    mc "¿Martillo?"
    call BlinkXPS3 ("c22s003_550" , "d") from _call_BlinkXPS3_800
    ama "Para [eva], sus armas son sus herramientas. Su martillo. Y cualquier problema es un clavo."
    ama "Intentaría resolver cualquier problema con la fuerza, y no es la dirección que queremos darle a la empresa, ¿no?"
    mc "No, en eso tienes razón. *Risa* No queremos que hundan el yate de Ichigo."
    call BlinkXPS3 ("c22s003_555" , "d") from _call_BlinkXPS3_801
    ama "Bueno, tengo que arreglar unos temas para la reunión del sábado y buscar información sobre los asistentes. Te voy a tener que dejar."
    mc "¿Has pensado en pedirle ayuda a [jam]? Creo que os podría ser útil para buscar cosas."
    ama "No es mala idea. Le llamaré esta tarde, cuando volvamos de comer en casa de [nor]."
    call BlinkXPS3 ("c22s003_560" , "d") from _call_BlinkXPS3_802
    ama "Y, por cierto, gracias por lo de [eva]."
    mc "¿Gracias por qué? Es tu hermana, pero es mi prima."
    ama "Tienes razón, pero no por ello estoy menos agradecida por lo que has hecho."
    if eva._var("route"):
        mc "Y también mi novia, por lo que parece."
        call BlinkXPS3 ("c22s003_565" , "d") from _call_BlinkXPS3_803
        ama "*Risa* ¿Por qué odias tanto esa palabra?"
        mc "Porque cuando se dice tantas veces pierde el significado. Además nunca me han gustado las etiquetas."
        if ama._var("route"):
            mc "*Risa* Suena muy raro decir que las dos sois mis novias. Creo que no es el uso que tenían pensado cuando inventaron la puta palabra."
            call KissXPS3 ("c22s003_570" , "d") from _call_KissXPS3_11
            ama "Tienes razón. Te veo luego... novio. *Risa*"
        else:
            ama "No te entretengo más."
    else:
        if ama._var("route"):
            call KissXPS3 ("c22s003_570" , "d") from _call_KissXPS3_12
        ama "Te veo luego."
    stop music fadeout (1.5)
    mc "Hasta dentro de un rato."
    return
label c22s004_EriPregnancyResult:
    if _in_replay:
        call mrS3_rename from _call_mrS3_rename_16
        call mrS3_eri_route from _call_mrS3_eri_route_3
    scene black with dissolve
    "Conduces a casa esperando que [ama] tenga razón en que vas a aprender rápido el nuevo oficio."
    "Estás seguro de que no eres un buen negociador. Ni siquiera sabes que salario vas a tener y ya has aceptado el puesto."
    scene c22s004_005a with dissolve
    play music ("music/Happy-Sun.ogg")
    "Al volver a casa, encuentras a [eri] charlando con [kat] en la planta de las estudiantes."
    eri "... Creo que deberías unirte. El yoga puede ser divertido."
    kat "No me vas a convencer, [eri]. Hoy es mi día de descanso de hacer deporte."
    kat "Suficiente tengo con despertarme pronto porque [kim] pone la alarma para levantarse en un día que no tengo clase por la mañana."
    mc "Hola, chicas, ¿qué tal?"
    call BlinkXPS3 ("c22s004_010" , "d") from _call_BlinkXPS3_804
    kat "[eri] sigue la tendencia del día de intentar que me una a las sesiones de yoga. *Risa*"
    mc "Ya les has dicho que no te vas a unir mientras lleven ropa, ¿no?"
    call BlinkXPS3 ("c22s004_015" , "d") from _call_BlinkXPS3_805
    kat "*Risa* Ni siquiera entonces. Me sentaría en una tumbona a mirarlas."
    mc "*Risa* Guárdame un sitio en esa tumbona."
    call BlinkXPS3 ("c22s004_020" , "d") from _call_BlinkXPS3_806
    eri "*Risa* Y por eso no haremos nunca yoga desnudas. Queremos que os unáis, y no como público."
    mc "*Risa* Ya sabes que la flexibilidad no es lo mío."
    call BlinkXPS3 ("c22s004_025" , "d") from _call_BlinkXPS3_807
    kat "Bueno, yo voy a ir a estudiar un rato. Hoy quería acabar un informe sobre las belugas."
    mc "Las belugas son primas de las ballenas, ¿no?"
    call BlinkXPS3 ("c22s004_030" , "d") from _call_BlinkXPS3_808
    kat "No son primas de las ballenas. Son ballenas."
    kat "Pero bien hecho, [mc]. Ya era hora que te atrevieras."
    mc "¿Qué he hecho?"
    call BlinkXPS3 ("c22s004_035" , "d") from _call_BlinkXPS3_809
    kat "Insinuar que, al ser ballenas, tengo algún tipo de ventaja para escribir el informe. Es un buen chiste de gordos. Un poco cruel, pero es bueno."
    mc "¿Qué? ¡No! ¡No quería decir eso!"
    call BlinkXPS3 ("c22s004_040" , "d") from _call_BlinkXPS3_810
    eri "¡[mc]! ¿Cómo te atreves? No tienes que intentar acomplejar a nadie sobre su cuerpo."
    mc "¡De verdad! ¡No he insinuado nada de eso!"
    scene c22s004_045An with dissolve
    pause (2.0)
    eri "*Risa* Tenías razón..."
    kat "*Risa* Nunca falla..."
    mc "¿Qué está pasando aquí?"
    scene c22s004_045d with dissolve
    eri "*Risa* [kat] me estaba diciendo que si consigue que alguien piense que se ha metido con su físico sin darse cuenta, por norma se ponen incómodos."
    kat "*Risa* Y diez minutos después llegas tú y me das la oportunidad de demostrarlo. Gracias por ser mi conejillo de indias."
    mc "Sois malas personas. *Risa* Y yo he caído en vuestra broma. ¡Me voy a mi habitación hasta la hora de comer! Castigado por tonto. *Risa*"
    $ ambas = TGCharacter (_("Ambas"), color = "#ffffff")
    if eri._var("route") and persistent.pregnancy:
        pass
    else:
        ambas "Hasta luego, [mc]."
    stop music fadeout (1.5)
    return
label c22s004_EriPregnancy:
    if _in_replay:
        call mrS3_rename from _call_mrS3_rename_17
        $ mc._var("relationships", 1, "set")
        call mrS3_eri_pregnacyDiscovered from _call_mrS3_eri_pregnacyDiscovered
        call mrS3_nor_route from _call_mrS3_nor_route
        if not eri._var("pregnancyDiscovered"):
            call mrS3_emm_route from _call_mrS3_emm_route_2
            call mrS3_dap_route from _call_mrS3_dap_route_2
        if mc._var("relationships")<2 and eri._var("route"):
            call mrS3_rels from _call_mrS3_rels_2
    call BlinkXPS3 ("c22s004_050" , "d") from _call_BlinkXPS3_811
    call changenicks from _call_changenicks_2
    eri "Ahora subo a verte. Tengo un tema que tratar contigo."
    if eri._var("pregnant"):
        if dap._var("route") and emm._var("route"):
            pass
        else:
            $ eri._var("pregnancyDiscovered", True)
    mc "Ok."
    scene c21s001_020b with fade
    "Unos minutos después..."
    play sound ("music/knock.ogg")
    "*Knock-Knock*"
    play music ("music/Embrace.ogg")
    eri "*A través de la puerta* Soy yo. ¿Puedo pasar?"
    mc "Sí, entra."
    call BlinkXPS3 ("c22s004_055" , "f") from _call_BlinkXPS3_812
    mc "Dime. Parecía urgente."
    eri "No, todo lo contrario que urgente."
    eri "Hace un par de días que la prueba de embarazo tiene que haber dado los resultados..."
    mc "¡Es verdad! ¡Me había olvidado de ella!"
    mc "¿Quieres hacer los honores? Está en ese armario."
    if eri._var("pregnancyDiscovered"):
        call BlinkXPS3 ("c22s004_060a" , "f") from _call_BlinkXPS3_813
        eri "¡Verde! ¡Vamos a tener a Hope!"
        mc "¡Felicidades, futura mamá!"
        call KissXPS3 ("c22s004_065" , "d") from _call_KissXPS3_13
        eri "Felicidades a ti también, Papá."
        mc "Gracias, cielo."
        if nor._var("route"):
            mc "¿Has hablado con [nor] sobre lo del nombre?"
            call BlinkXPS3 ("c22s004_070" , "d") from _call_BlinkXPS3_814
            eri "Sí, le dije que me hacía mucha ilusión ponerle Hope a mi hija y no tuvo ningún problema."
            eri "Al fin y al cabo, el nombre lo había elegido yo."
            mc "Me alegra que lo hayáis podido resolver sin dramas."
        call BlinkXPS3 ("c22s004_075" , "d") from _call_BlinkXPS3_815
        eri "Y ¿ahora qué?"
        mc "Supongo que después de la Gran Revelación, debemos comunicar estas cosas a la familia, ¿no?"
        mc "Me he cansado de guardar cosas en secreto."
        call BlinkXPS3 ("c22s004_080" , "d") from _call_BlinkXPS3_816
        eri "Me parece buena idea. Me gustaría decírselo a mi madre y a mi hermana en persona."
        eri "Al resto se lo podemos decir en la comida y publicarlo en el grupo de WhatsUp."
        mc "En el que no estoy... *Risa*"
        call BlinkXPS3 ("c22s004_085" , "d") from _call_BlinkXPS3_817
        eri "*Risa* Y en el que no estarás. [emm] me ha dicho que crearemos otro contigo, pero ese es solo para chicas."
        mc "Y [jam]..."
        eri "*Risa* Y [jam]."
        call c22s004_diapers from _call_c22s004_diapers
        call BlinkXPS3 ("c22s004_090b" , "d") from _call_BlinkXPS3_818
        eri "Vamos a decírselo a [dap.nick] y a mi madre."
        mc "Cuando quieras."
        scene black with dissolve
        "Las reacciones de [nor] y [dap] por la llegada de Hope son de pura alegría."
        "Después, durante la comida, se lo comunicáis al resto de la familia y os llueven las felicitaciones."
        "[eri] lee las felicitaciones en el grupo de WhatsUp sin dejarte coger su teléfono. Empiezas a sentir curiosidad por lo que se habla en ese grupo."
        call c22s004_group from _call_c22s004_group
    else:
        call BlinkXPS3 ("c22s004_060b" , "f") from _call_BlinkXPS3_819
        eri "Rojo. Supongo que habrá que volver a intentarlo."
        if dap._var("route") and emm._var("route"):
            mc "O hacer otra prueba. Esa prueba la hicimos antes de la noche del domingo."
            call BlinkXPS3 ("c22s004_095" , "d") from _call_BlinkXPS3_820
            eri "¡Tienes razón! ¡Es posible que me quedara embarazada entonces!"
        mc "Ven aquí, cielo."
        call KissXPS3 ("c22s004_065" , "d") from _call_KissXPS3_14
        mc "Te quiero."
        eri "Yo también te quiero."
        call c22s004_diapers from _call_c22s004_diapers_1
        call BlinkXPS3 ("c22s004_090b" , "d") from _call_BlinkXPS3_821
        if dap._var("route") and emm._var("route"):
            eri "Vamos a hacer esa prueba y a comer. Me muero de hambre."
        else:
            eri "Vamos a comer. Me muero de hambre."
        scene black with dissolve
        "La comida transcurre sin incidentes."
        call c22s004_group from _call_c22s004_group_1
    stop music fadeout (1.5)
    return
label c22s004_diapers:
    if mc._var("relationships")>2:
        call BlinkXPS3 ("c22s004_090a" , "d") from _call_BlinkXPS3_822
        eri "Nos estamos poniendo muy pesadas con los embarazos, ¿verdad?"
        mc "No, cielo. Es raro, pero no os ponéis pesadas."
        call BlinkXPS3 ("c22s004_100" , "d") from _call_BlinkXPS3_823
        eri "Es que todas queremos que nuestros hijos crezcan juntos. Sería bonito..."
        mc "Sí que lo sería. Tienes razón. Un follón de pañales, pero bonito. *Risa*"
    else:
        call BlinkXPS3 ("c22s004_090a" , "d") from _call_BlinkXPS3_824
        eri "Me estoy poniendo muy pesada con el embarazo, ¿verdad?"
        mc "No, cielo. Es raro, pero no te pones pesada."
        call BlinkXPS3 ("c22s004_100" , "d") from _call_BlinkXPS3_825
        eri "Es que tengo muchas ganas de que llegue Hope. Sería tan bonito..."
        mc "Sí que lo sería. Tienes razón. Cambiar los pañales no tanto, por eso. *Risa*"
    mc "Habrá que darle trabajo a Meemaw con lo de los pañales. *Risa*"
    return
label c22s004_group:
    "Después de la fiesta de la piscina, la cocina parece casi vacía sin [meg], [mad.nick], [sam], [sim], [oma], [sai], [kim], [kia], [eil], ni [kat]."
    "Ni [jam]. Él está en el grupo, pero tú estás con las chicas."
    "Al final de la comida, [sca] ha creado un nuevo grupo en el que estás incluido. Por el número de notificaciones, es mucho menos activo que el grupo original."
    "[bet] y [mee] se evitan durante toda la comida, como si estuvieran incómodas la una al lado de la otra."
    return
label c22s004_ScarlettDNA:
    if _in_replay:
        call mrS3_rename from _call_mrS3_rename_18
        call mrS3_sca_route from _call_mrS3_sca_route
        call mrS3_sca_pregnant from _call_mrS3_sca_pregnant
    call changenicks from _call_changenicks_3
    scene c22s004_150a with dissolve
    "Poco después de comer, todos vais a cambiaros para pasar un rato en la piscina."
    play music ("music/CinematicFairyTaleStory.ogg")
    "Mientras esperas que las chicas acaben de ponerse sus bikinis, llega un mensajero con los test de ADN."
    scene c21s006_015d with fade
    "Vas casi corriendo a la habitación que comparten [dap] y [sca], intentando llegar antes de que bajen a la piscina."
    play sound ("music/knock.ogg")
    "*Knock-Knock*"
    mc "Soy yo. ¿Puedo pasar?"
    dap "*A través de la puerta* Sí, pasa. Nos estábamos acabando de cambiar."
    scene c22s004_150b with fade
    mc "¡Ha llegado la prueba de ADN!"
    sca "¡Ábrela! ¡Siento como si fuese el regalo de Navidad!"
    dap "Esperad. ¿Queréis que me vaya? Puedo esperaros en la piscina."
    mc "Por mí no hace falta, ¿[sca]?"
    scene c22s004_155 with dissolve
    sca "No, quiero que estés aquí. Eres la hermana que nunca tuve y ahora..."
    if persistent.family:
        mc "Ahora es posible que [emm] sea la hermana que siempre tuviste y nunca supiste."
    else:
        mc "Ahora es posible que yo sea el hermano que siempre tuviste y nunca supiste."
    sca "Lo que acaba de decir [mc]. Pero tú siempre serás mi hermana, [dap]. Quiero que estés con nosotros cuando lo abramos."
    dap "Gracias a los dos. Por confiar en mí y por querer que esté con vosotros en este momento."
    mc "En este momento y siempre, [dap.nick]."
    scene c22s004_165 with dissolve
    sca "Ábrela ya, por favor. La impaciencia me está matando."
    stop music fadeout (1.5)
    mc "Voy, no me metáis prisa. *Risa nerviosa*"
    if not persistent.family:
        scene c22s004_170d with dissolve
        play music ("music/Emotional-Piano-Sad.ogg")
        mc "0\% de compatibilidad."
        call BlinkXPS3 ("c22s004_175" , "d") from _call_BlinkXPS3_826
        mc "Lo siento, [sca]. No somos hermanos."
        sca "Bueno..."
        call BlinkXPS3 ("c22s004_180" , "d") from _call_BlinkXPS3_827
        sca "Me siento menos decepcionada de lo que hubiera esperado."
        sca "Tenías razón, estaba poniendo mis esperanzas en pruebas circunstanciales tan solo. Había muchas coincidencias, pero eran solo eso. Coincidencias."
        mc "Ven aquí, cielo."
        call BlinkXPS3 ("c22s004_185" , "d") from _call_BlinkXPS3_828
        sca "Por un lado tengo ganas de llorar, por otro, tengo ganas de reírme de mí misma."
        mc "Sabes que no vamos a dejar de buscar a tu padre, ¿verdad?"
        mc "Y también sabes que, aunque no sea por sangre, ya perteneces a esta familia."
        call BlinkXPS3 ("c22s004_190" , "d") from _call_BlinkXPS3_829
        dap "Si por sangre fuera, ninguno perteneceríamos a esta familia, [sca]. Lo que importa es que nos vemos como una familia, no el ADN."
        mc "Ven aquí, [dap.nick]. No puedes saber lo mucho que te quiero ahora mismo."
        scene c22s004_190d with dissolve
        sca "Gracias. Sois maravillosos todos. No podría pertenecer a una familia mejor."
        "El abrazo dura unos largos minutos en los que os prometéis que no dejaréis de buscar al padre de [sca] ni a tu medio hermana."
        scene c22s004_195 with dissolve
        sca "Deberíamos ir bajando a la piscina. Se van a preguntar dónde estamos y no quiero tener que dar explicaciones."
        mc "Yo pensaba ir un rato. Tengo que hacer unas cosas después."
        if sca._var("route"):
            scene c22s004_200 with hpunch
            "[sca] explota en una carcajada que os deja anonadados a [dap] y a ti."
            sca "*Risa*"
            mc "¿Qué pasa, [sca]? ¿Qué has pensado que sea tan gracioso?"
            scene c22s004_205 with dissolve
            sca "*Risa* Que al menos nuestros hijos no serán endogámicos."
            if not sca._var("pregnant"):
                sca "Si los tenemos, claro"
            mc "*Risa* No hay mal que por bien no venga."
            mc "*Risa* Además, te libras de tener una mierda de padre."
            dap "Me alegra que no lleve mis genes. *Risa* Tío Edmund queda expulsado de la familia."
        stop music fadeout (1.5)
    else:
        play music ("music/Acoustic-Inspirational.ogg")
        scene c22s004_170e with dissolve
        mc "99.7\% de compatibilidad. ¿Por qué no es un 100\%?"
        scene c22s004_170f with vpunch
        sca "{b}¿De verdad?{/b} ¿Somos hermanos?"
        mc "Bueno, medio-herm..."
        scene c22s004_170g with hpunch
        sca "¡Sí! ¡Sí! ¡Sí!"
        if sca._var("route"):
            scene c22s004_170h with hpunch
            "Tu nueva medio-hermana te besa de forma apasionada. Hay mucho alivio en ese beso."
        else:
            "Tu nueva medio-hermana te abraza con fuerza. Hay mucho alivio en ese abrazo."
        "Alivio por haber encontrado a una familia, aunque ya formara parte de ella."
        "Alivio porque por fin sabe quién es su padre."
        "Alivio por no tener que seguir buscando."
        call BlinkXPS3 ("c22s004_215" , "d") from _call_BlinkXPS3_830
        dap "Felicidades, chicos."
        mc "Gracias, [dap]."
        call BlinkXPS3 ("c22s004_220" , "d") from _call_BlinkXPS3_831
        sca "¿No me vas a felicitar por pertenecer a la familia?"
        mc "¿Por pertenecer a esta familia de bichos raros? *Risa* ¿Felicitaciones o condolencias?"
        call BlinkXPS3 ("c22s004_225" , "d") from _call_BlinkXPS3_832
        dap "No, no lo voy a hacer."
        dap "Para mí, ya eras mi hermana. Ya pertenecías a la familia."
        call BlinkXPS3 ("c22s004_230" , "d") from _call_BlinkXPS3_833
        dap "¿Ahora qué eres? ¿Una medio-prima?"
        dap "*Risa* Eso es casi como una desconocida."
        mc "*Risa* Ven aquí, [dap.nick]."
        scene c22s004_190d with dissolve
        sca "Aunque tienes razón, [dap], es un alivio haber descubierto quién es mi padre después de tantos años."
        mc "Aunque sea una mierda de padre. *Risa*"
        sca "*Risa* Exacto, aunque sea una mierda de padre."
        mc "Te entiendo. Yo solo hace una semana que sé que tengo una medio-hermana y no me quiero imaginar qué hubiera pasado si hubiera salido negativo."
        dap "Habláis demasiado en vez de disfrutar del abrazo."
        scene c22s004_235 with dissolve
        sca "Habrá que decírselo a la familia, ¿no?"
        mc "Sí."
        sca "No sé ni por dónde empezar. Creo que [mar] es la primera a quién se lo tendríamos que decir."
        mc "Yo le he adelantado algo. Hace unos días se me escapó que había hablado con mi... con nuestro padre, y hoy me ha tirado de la lengua."
        mc "No podía explicarle verdades a medias."
        dap "No me hubiera gustado estar en tu situación cuando has tenido que explicárselo."
        scene c22s004_240 with dissolve
        stop music fadeout (1.5)
        sca "No importa. Era quien más miedo me daba, por el daño que le podía hacer."
    call BlinkXPS3 ("c22s004_210" , "d") from _call_BlinkXPS3_834
    play music ("music/ChillUkelele.ogg")
    dap "Vamos a ir la piscina. Se me ha ocurrido una cosa."
    dap "Os espero allí. Dadme cinco de minutos para organizarlo todo. Necesito que alguien concreto esté allí."
    dap "Tú también ven, [mc]. La puedes seguir abrazando esos cinco minutos, si quieres."
    if _in_replay:
        $ AuxReplay = True
    call c22s004_ScarlettReveal from _call_c22s004_ScarlettReveal1
    return
label c22s004_ScarlettReveal:
    if _in_replay and not AuxReplay:
        call mrS3_rename from _call_mrS3_rename_19
        $ mc._var("edmundsStory", False)
    $ AuxReplay = False
    call changenicks from _call_changenicks_4
    if mc._var("edmundsStory"):
        scene c22s004_170g2 with fade
        "El abrazo dura cinco minutos que se hacen muy cortos. No necesitáis decir nada más de lo que vuestros brazos rodeando al otro dicen."
        call BlinkXPS3 ("c22s004_250" , "d") from _call_BlinkXPS3_835
        sca "No es que no se esté a gusto aquí, pero ¿vamos a la piscina? [dap.nick] se va a empezar a impacientar."
        mc "Vamos. Tengo curiosidad por ver qué se le ha ocurrido."
        if sca._var("route") and persistent.family:
            call KissXPS3 ("c22s004_255" , "d") from _call_KissXPS3_15
            sca "Te quiero, hermanito."
            mc "Te quiero, hermanita."
        elif sca._var("route"):
            call KissXPS3 ("c22s004_255" , "d") from _call_KissXPS3_16
            sca "Te quiero, [mc]."
            mc "Te quiero, [sca]."
        scene c22s004_260a with fade
        "Cuando llegáis a la piscina os encontráis con una escena un poco caótica."
    else:
        scene black with dissolve
        "Poco después de comer, mientras te estás poniendo el bañador para ir al jacuzzi, te llega un mensaje de [dap] diciéndote que te necesita en la piscina."
        scene c22s004_260a with fade
        "Cuando llegas a la piscina te encuentras con una escena un poco caótica."
    dap "[emm], quédate ahí un momento."
    emm "Pero, ¿a qué viene esto?"
    dap "Es una cosa que quiero probar."
    eri "¿Yo donde me pongo?"
    dap "Ve al lado de [eva]."
    dap "[ama], tú estás bien, a ese lado de [eva]."
    deb "¿Y yo?"
    dap "Quédate ahí, [deb.nick]."
    nor "¿Qué hago yo, cielo?"
    dap "Intercámbiate el sitio con Tía [bet]. Necesito que ella esté al lado de la abuela."
    call BlinkXPS3 ("c22s004_265" , "d") from _call_BlinkXPS3_836
    bet "¿Es necesario todo esto?"
    scene c22s004_260b with dissolve
    dap "Sí, Tía [bet]. Es necesario."
    dap "A ver, [emm], ponte al lado libre de [ama]."
    dap "[lis], tu ponte con [deb.nick]."
    mc "¿Dónde me pongo yo?"
    call BlinkXPS3 ("c22s004_270" , "d") from _call_BlinkXPS3_837
    dap "Tú ponte al lado de [emm]."
    mc "OK."
    dap "[sca], tú quédate ahí, donde estás."
    dap "Ahora me pongo yo al lado de [eri] y ya está todo."
    call BlinkXPS3 ("c22s004_275" , "d") from _call_BlinkXPS3_838
    dap "No sé si os habéis dado cuenta, pero os he puesto por parejas de hermanas, o más o menos."
    if mc._var("edmundsStory"):
        call BlinkXPS3 ("c22s004_285" , "d") from _call_BlinkXPS3_839
        "[mar] te mira inquisitivamente."
        if persistent.family:
            "Asientes."
        else:
            "Niegas con la cabeza."
    scene c22s004_280a with dissolve
    dap "La abuela y Tía [bet]."
    scene c22s004_280b1 with dissolve
    dap "[deb.nick] y [lis]."
    if persistent.family:
        scene c22s004_280c with dissolve
        dap "Mi madre y Tía [mar]."
    scene c22s004_280d with dissolve
    dap "Y aquí viene lo complicado..."
    dap "[eri] es mi hermana."
    if not persistent.family:
        dap "Le pese a quién le pese."
    dap "Pero, de alguna forma, también lo es [eva], ¿cierto?"
    todas "Cierto."
    scene c22s004_280e1 with dissolve
    dap "¿Alguien cree que [ama] y [eva] no son hermanas?"
    todas "¡No!"
    scene c22s004_280f with dissolve
    dap "Pero, igual que podemos considerar que [eva] es mi hermana y la de [eri], [ama] también lo es de [emm], ¿no?"
    todas "Por supuesto."
    scene c22s004_280g with dissolve
    dap "Y, obviamente, [emm] es la hermana de [mc]."
    if not persistent.family:
        dap "Aunque el día que descubrió que no compartían ADN renegase de ello..."
        scene c22s004_280h with dissolve
        emm "¡Hey! ¡Fue un momento de ofuscación! Sabes que nunca renunciaría a ti como hermano."
    call BlinkXPS3 ("c22s004_290" , "d") from _call_BlinkXPS3_840
    dap "Bueno, a lo que iba... creo que sólo nos faltan [sim] y [jam], pero no les iba a hacer venir para esto."
    dap "Lo que quiero decir, es que esta familia cada día es más rara."
    todas "*Risa*"
    call BlinkXPS3 ("c22s004_295" , "d") from _call_BlinkXPS3_841
    lis "Estoy de acuerdo. Me sorprendió la primera vez que llamé Tía [bet] a... Tía [bet]."
    lis "Ahora ya no puedo pensar en ella de otra forma. No me sale decir sólo [bet]."
    call BlinkXPS3 ("c22s004_300" , "d") from _call_BlinkXPS3_842
    nor "Y [oma] ha empezado a llamar Yaya [mee] a mi madre. *Risa*"
    call BlinkXPS3 ("c22s004_305" , "d") from _call_BlinkXPS3_843
    deb "Y no es la única. *Risa*"
    if mc._var("edmundsStory"):
        if persistent.family:
            call BlinkXPS3 ("c22s004_310a" , "d") from _call_BlinkXPS3_844
            "[sca], obviamente, sabe lo que está haciendo [dap] y está ansiosa por que llegue la revelación."
        else:
            call BlinkXPS3 ("c22s004_310b" , "d") from _call_BlinkXPS3_845
            "[sca] está tan perdida como tú, sin saber que se propone [dap]. Si el resultado hubiera sido diferente, lo entenderíais, pero ahora..."
    else:
        call BlinkXPS3 ("c22s004_310b" , "d") from _call_BlinkXPS3_1016
        "[sca] está tan perdida como tú, sin saber que se propone [dap]. Se ha quedado apartada sin saber qué pinta aquí..."
        "Crees que nadie sabe qué se propone [dap]."
    call BlinkXPS3 ("c22s004_315" , "d") from _call_BlinkXPS3_846
    dap "Bueno, pues quería hacer esto para dar la bienvenida a la familia a algunas de las nuevas hermanas."
    dap "Bienvenidas, [eva] y [ama]. Os dimos la bienvenida como individuos, ahora lo hacemos como pareja de hermanas."
    scene c22s004_280e2 with dissolve
    ama "Gracias, [dap]."
    eva "Gracias, supongo... No, no supongo. Gracias, [dap]"
    call BlinkXPS3 ("c22s004_320a" , "d") from _call_BlinkXPS3_847
    emm "*Susurrando* Le está quedando un poco cursi, ¿no? Bonito, pero cursi."
    mc "*Susurrando* Calla y escucha."
    call BlinkXPS3 ("c22s004_320b" , "d") from _call_BlinkXPS3_848
    dap "También os quiero dar la bienvenida a vosotras, [lis] y [deb.nick]."
    dap "Ya casi os considero unas primas reencontradas."
    scene c22s004_280b2 with dissolve
    deb "Gracias, [dap], es una familia maravillosa."
    lis "Lo mismo digo, [dap]."
    call BlinkXPS3 ("c22s004_325" , "d") from _call_BlinkXPS3_849
    dap "Y, como soy idiota, me he olvidado de algo..."
    stop music fadeout (1.5)
    if persistent.family and mc._var("edmundsStory"):
        dap "Ocupa tu lugar, [sca]."
        call c22s004_ScaPatch from _call_c22s004_ScaPatch
    else:
        dap "Ven a mi lado, [sca]."
        call c22s004_ScaUnPatch from _call_c22s004_ScaUnPatch
    return
label c22s004_ScaPatch:
    play music ("music/From-Above.ogg")
    scene c22s004_330An with dissolve
    "[sca] se dirige hacia ti y [emm]. Te apartas para dejarle un hueco entre ambos, que ocupa para sorpresa de todo el mundo."
    scene c22s004_335An with hpunch
    todas "{b}¿QUÉ?{/b}"
    "Tan solo [mar] evita la cara de sorpresa."
    "[ama] y [eva] sabían que buscabas a una hermana, pero no sabían quién era."
    call BlinkXPS3 ("c22s004_340" , "d") from _call_BlinkXPS3_850
    "[dap] ignora la pregunta que está en la boca de casi todas las mujeres y sigue hablando como si nada hubiera pasado."
    dap "Bienvenida oficialmente a la familia, [sca]. Ahora eres una Marks de pleno derecho."
    scene c22s004_345An with dissolve
    mom "Ven aquí, cielo."
    "[mar] se acerca a [sca], ignorando las caras de sorpresa del resto de mujeres, y se funde en un abrazo con la chica a medio camino."
    mom "Bienvenida a la familia, cariño."
    scene c22s004_350a with dissolve
    mee "¿Qué está pasando aquí?"
    scene c22s004_350b with dissolve
    "[dap] decide pasar a un segundo plano. Ella ha puesto los cimientos para esta situación."
    "Pero contar la verdad podría ser muy humillante para [mar]. No es algo a lo que tenga derecho."
    scene c22s004_345d with dissolve
    "[sca] está demasiado abrumada para hablar. El desarrollo del \"experimento de [dap]\" la ha dejado con las emociones a flor de piel."
    "Tú tampoco puedes dar las explicaciones por las mismas razones que [dap]. Te alegras de haber tenido la conversación con [mar] por la mañana."
    call BlinkXPS3 ("c22s004_355" , "d") from _call_BlinkXPS3_851
    mar "[sca] es la hija de Edmund. Me engañó hace años y este es el resultado."
    scene c22s004_335An2 with hpunch
    todas "¿QUÉ?"
    call BlinkXPS3 ("c22s004_355" , "d") from _call_BlinkXPS3_852
    mar "Sí, lleva años siendo un cabrón, por lo visto, pero..."
    mar "No creía que pudiera pensar esto, pero [sca] es un regalo que ha llegado a casa con retraso, aunque lo hemos tenido delante todos estos años."
    scene c22s004_355d with dissolve
    mar "Cielo, no eres mi hija, pero... ¿me permitirías ejercer de madre?"
    sca "No podría tener una madre mejor, [mar]."
    scene c22s004_360 with dissolve
    emm "¿Puedo abrazar a mi nueva hermana?"
    scene c22s004_365a with dissolve
    emm "Dos hermanas nuevas en una semana. Al final me voy a hacer un lío..."
    emm "Bienvenida a casa, hermanita."
    sca "Gracias, [emm]. Me alegra muchísimo que seas mi hermana."
    scene c22s004_365An1 with dissolve
    "El resto os vais turnando para abrazar a [sca]. Dándole la bienvenida a la familia."
    call c22s004_hugs from _call_c22s004_hugs
    "Sienta tan bien quitarse los secretos de encima..."
    "[dap] envía un mensaje al grupo de WhatsUp mientras el resto de las chicas acaban de abrazar a [sca]."
    "El resto de la familia también tiene derecho a saber la verdad."
    return
label c22s004_ScaUnPatch:
    call changenicks from _call_changenicks_5
    play music ("music/From-Above.ogg")
    scene c22s004_370 with hpunch
    sca "¿Qué?"
    call BlinkXPS3 ("c22s004_375" , "d") from _call_BlinkXPS3_853
    dap "Ven aquí. *Risa* Parezco una gaviota idiota con el ala levantada."
    scene c22s004_380An with dissolve
    sca "*Susurrando* ¿De qué va esto?"
    dap "Calla y escucha."
    call BlinkXPS3 ("c22s004_385" , "d") from _call_BlinkXPS3_854
    if mc._var("edmundsStory"):
        dap "Os habéis dado cuenta de que, menos con [lis] y [deb.nick], y con Tía [bet] y la abuela, el resto de las parejas de hermanos no lo son de sangre, ¿verdad?"
    else:
        dap "Os habéis dado cuenta con los ejemplos de [eva] y [ama] de que no es necesario compartir genes para ser hermanas."
    todas "Sí."
    call BlinkXPS3 ("c22s004_390" , "d") from _call_BlinkXPS3_855
    if mc._var("edmundsStory"):
        dap "He estado hablando estos días con mi madre sobre nuestro parentesco legal."
        dap "Ni siquiera soy adoptada. Ni siquiera es mi madre legalmente."
        dap "¿Alguien pone en duda que [nor] sea mi madre?"
    else:
        dap "Pero nadie duda de que sean hermanas. O de que [eva] sea mi hermana."
    todas "No."
    call BlinkXPS3 ("c22s004_395" , "d") from _call_BlinkXPS3_856
    if mc._var("edmundsStory"):
        mee "Yo lo hice durante años. Ya no."
    else:
        mee "Es tu hermana y es mi nieta perdida."
    call BlinkXPS3 ("c22s004_400" , "d") from _call_BlinkXPS3_857
    if mc._var("edmundsStory"):
        dap "Bien, Abuela. ¿O debería decir \"Sra. Que Se Hace Pasar Por Mi Abuela\"?"
    else:
        dap "Bien, Abuela. ¿O debería decir \"Sra. Que Se Hace Pasar Por La Abuela de [eva] y [ama]\"?"
    call BlinkXPS3 ("c22s004_405" , "d") from _call_BlinkXPS3_858
    if mc._var("edmundsStory"):
        mee "*Risa* Ni se te ocurra. Soy tu abuela te guste o no."
    else:
        mee "*Risa* Ni se te ocurra. Soy su abuela les guste o no."
    mee "Y, si quieren, también puedo serlo para cualquier chica que necesite una abuela."
    mee "No hago galletas, por cierto."
    todas "*Risa*"
    call BlinkXPS3 ("c22s004_410" , "d") from _call_BlinkXPS3_859
    dap "¿Puedo continuar? Gracias."
    dap "A lo que me refiero es a que esta familia es rara. Se ha creado a través de mentiras, secretos, y clonaciones."
    dap "¿Pero alguien duda de que sea una familia?"
    todas "No."
    scene c22s004_410d with dissolve
    deb "Es una familia increíble, [dap]. Los lazos de sangre importan menos que la voluntad de ser una familia."
    lis "Si leyera esto en un libro, no me lo creería. Vivirlo es totalmente diferente."
    call BlinkXPS3 ("c22s004_415" , "d") from _call_BlinkXPS3_860
    dap "Eso es exactamente lo que quiero decir."
    dap "Me da lo mismo lo que piense la gente de fuera de la familia."
    dap "Me da lo mismo lo que digan las leyes."
    call BlinkXPS3 ("c22s004_420" , "d") from _call_BlinkXPS3_861
    if mc._var("edmundsStory"):
        dap "Si [nor] es mi madre porque elegimos que lo sea..."
        dap "Si [mee] es mi abuela porque así lo hemos decidido..."
    else:
        dap "Si [ama] y [eva] son de la familia porque elegimos que lo sean..."
        dap "Si la abuela es también su abuela porque así lo han decidido..."
    mc "Y porque si no, seguramente sí que nos haría esas galletas y nos obligaría a comerlas como tortura."
    todas "*Risa*"
    call BlinkXPS3 ("c22s004_425" , "d") from _call_BlinkXPS3_862
    dap "Bueno, pues una vez establecida la premisa..."
    dap "He decidido que [sca] es mi hermana."
    call BlinkXPS3 ("c22s004_430" , "d") from _call_BlinkXPS3_863
    dap "Joder, me ha quedado totalmente anticlimático con tantas interrupciones."
    call BlinkXPS3 ("c22s004_435" , "d") from _call_BlinkXPS3_864
    mee "¡Ese lenguaje, señorita! Como tu abuela no te dejo usarlo."
    todas "*Risa*"
    mee "Y a ti tampoco, [sca], antes de que preguntes. Quiero que mis nietas hablen como señoritas bien educadas."
    call BlinkXPS3 ("c22s004_440" , "d") from _call_BlinkXPS3_865
    sca "..."
    scene c22s004_440d with hpunch
    sca "Gracias, [dap.nick]..."
    dap "Es lo menos que podía hacer. Sabes que te considero mi hermana. Ahora lo saben todos."
    scene c22s004_445 with dissolve
    eri "[dap], ¿puedes dejar de monopolizar a mi hermana? Yo también quiero abrazarla."
    scene c22s004_445d with dissolve
    sca "Me vais a hacer llorar..."
    eri "Yo llevaría un rato llorando. Ya sabes que soy muy llorona, y lo que ha dicho [dap] es muy bonito."
    scene c22s004_365An1 with dissolve
    "El resto os vais turnando para abrazar a [sca]. Todas dicen algo que la hace sentir querida."
    call c22s004_hugs from _call_c22s004_hugs_1
    "[sca] ha pasado de tener una madre de mierda a tener dos madres y dos abuelas maravillosas. Y un montón de hermanas."
    return
label c22s004_hugs:
    "La escena te recuerda mucho a la fiesta de la piscina, cuando [mee] contó su secreto sobre el cáncer."
    "No podrías estar más orgulloso de tu familia."
    stop music fadeout (1.5)
    return
label c22s004_BetCallsBishop:
    if _in_replay:
        call mrS3_rename from _call_mrS3_rename_20
        call mrS3_edmund_story from _call_mrS3_edmund_story_1
    play music ("music/In-The-Rain.ogg")
    call BlinkXPS3 ("c22s004_500" , "f") from _call_BlinkXPS3_866
    bet "Lo que pasa en esta familia es increíble."
    mc "Pero es para sentirse orgulloso de formar parte de ella."
    mc "El día menos pensado, pasará un perro callejero por delante de casa y le diremos \"Tú también eres de la familia\"."
    mc "Y que conste que no estoy comparando a [sca] con un perro callejero. Se merece formar parte de esta familia."
    call BlinkXPS3 ("c22s004_505" , "d") from _call_BlinkXPS3_867
    if persistent.family and mc._var("edmundsStory"):
        bet "Claro que sí. Es tu hermana. Y aunque no lo fuera, esa chica es adorable y necesita una familia que la quiera."
        mc "Sí, es sorprendente lo adorable que es con la mierda de padres que tiene."
    else:
        bet "Claro que sí. Es una chica adorable y necesita una familia que la quiera."
        mc "Sí, es sorprendente lo adorable que es con la madre que tiene."
    call BlinkXPS3 ("c22s004_510" , "d") from _call_BlinkXPS3_868
    bet "Quería hablar contigo de una cosa..."
    mc "Dime. ¿Tiene algo que ver con lo que ha pasado antes?"
    scene c22s004_515AnBlink
    bet "No. No quiero hablar de eso."
    mc "Quitarse los secretos de encima es liberador, [bet]. Y hablar las cosas también."
    call BlinkXPS3 ("c22s004_520" , "d") from _call_BlinkXPS3_869
    bet "Es posible, pero hoy no es el día."
    mc "Como quieras. ¿De qué querías hablar?"
    call BlinkXPS3 ("c22s004_525" , "d") from _call_BlinkXPS3_870
    bet "Me han llamado de Monterey después de comer. Tengo una cita con el secretario del obispo el jueves por la tarde."
    bet "¿Crees que me podrías llevar? Si no puedes, puedo ir en autobús."
    mc "Ningún problema. Voy a intentar mover el alquiler del coche de [emm] para el jueves, y así matamos dos pájaros de un tiro."
    call BlinkXPS3 ("c22s004_530" , "d") from _call_BlinkXPS3_871
    bet "Gracias, [mc]. Voy a ir a mi habitación, dime algo si no puedes mover lo de [emm], para sacar los billetes de autobús."
    mc "No me he explicado bien. Te voy a llevar el jueves sea como sea, aunque tenga que volver el día siguiente con [emm]."
    mc "No hemos tenido la oportunidad de pasar mucho tiempo juntos, y me parece un buen plan. No voy a dejar que hagas esto sola."
    call BlinkXPS3 ("c22s004_535" , "d") from _call_BlinkXPS3_872
    bet "¡Oh! ¡Gracias!"
    mc "Y cuando quieras hablar de lo que ha pasado antes en el baño, avísame."
    call BlinkXPS3 ("c22s004_540" , "d") from _call_BlinkXPS3_873
    bet "Lo haré. Hasta luego."
    stop music fadeout (1.5)
    mc "Hasta luego, Tía [bet]."
    return
label c22s004_MarChat:
    if _in_replay:
        call mrS3_rename from _call_mrS3_rename_21
    call changenicks from _call_changenicks_6
    play music ("music/i-feel-alive.ogg")
    call BlinkXPS3 ("c22s004_545" , "f") from _call_BlinkXPS3_874
    if persistent.family:
        mom "[dap] es increíble. La que ha montado para dar la noticia..."
        mc "No creo que fuera una noticia que se tuviera que dar por el grupo de WhatsUp."
        mc "Y necesitaba que tú colaboraras."
        mc "Siento que hayas tenido que dar tu parte de la noticia así."
        call BlinkXPS3 ("c22s004_550" , "d") from _call_BlinkXPS3_875
        mom "No te preocupes. He estado pensando en los dos posibles escenarios después de la conversación de esta mañana."
        mom "Si no lo hubiéramos hablado, seguramente me hubiera molestado enterarme de que soy una cornuda delante de todo el mundo."
        mc "Pasó hace 19 años..."
        call BlinkXPS3 ("c22s004_555" , "d") from _call_BlinkXPS3_876
        mom "Da lo mismo cuando pasara, [mc]."
        mom "Y realmente, me da lo mismo que pasara. Cada vez que pienso en tu padre, no puedo sentir nada que no sea enfado, pero cada vez menos."
        mc "Está fuera de nuestras vidas, no creo que volvamos a verlo nunca."
        call BlinkXPS3 ("c22s004_560" , "d") from _call_BlinkXPS3_877
        mom "Eso me da lo mismo también. No quiero verlo, pero no me derrumbaría si lo hiciera."
        mom "Además, nos ha dejado tres bonitos regalos aquí."
        mc "¿Tres? [emm], [sca], y... ¿la camioneta?"
        call BlinkXPS3 ("c22s004_565" , "d") from _call_BlinkXPS3_878
        mom "[emm], [sca], y tú, idiota. *Risa*"
        mc "*Risa* Al decir \"nos ha dejado\" creía que era a ti y a mí, con lo que no me incluía yo."
        mc "Estoy un poco denso hoy."
        call BlinkXPS3 ("c22s004_570" , "d") from _call_BlinkXPS3_879
        mom "*Risa* ¿Sólo hoy?"
        mom "Si no te importa, voy a volver con [sca] antes de que la abrumen demasiado."
    else:
        mom "[dap] es increíble. Ha montado todo esto para que [sca] no se sienta mal por cómo ha salido la prueba de ADN."
        mc "[sca] se ha decepcionado un poco cuando ha salido negativa. Creo que [dap.nick] lo ha hecho muy bien."
        call BlinkXPS3 ("c22s004_550" , "d") from _call_BlinkXPS3_880
        mom "Y nos hemos ahorrado las explicaciones incómodas si la prueba de ADN hubiera salido diferente."
        mc "Sí, y nos toca seguir buscando a su padre y a mi medio-hermana."
        call BlinkXPS3 ("c22s004_575" , "d") from _call_BlinkXPS3_881
        mom "Esa es la parte más complicada. ¿Tenéis algún hilo del que tirar?"
        mc "No. Los únicos que saben algo, Papá y la madre biológica de [sca] no van a decir nada."
        call BlinkXPS3 ("c22s004_580" , "d") from _call_BlinkXPS3_882
        mom "Con tu padre no se me ocurre ninguna idea, pero creo que con la madre de [sca] podría pensar en algo."
        mom "¿Todavía quedan clones en Newport?"
        mc "Creo que no, pero no tengo ni idea..."
        call BlinkXPS3 ("c22s004_570" , "d") from _call_BlinkXPS3_883
        mom "Si no te importa, voy a volver con [sca] antes de que la abrumen demasiado."
        mom "Después hablaré con [ama] y [eva]."
        mc "¿No me lo vas a contar?"
        call BlinkXPS3 ("c22s004_585" , "d") from _call_BlinkXPS3_884
        mom "De momento no. Tengo que acabar de pensar en algunas cosas. Cuando lo tenga todo ligado, os lo cuento."
    mc "Ningún problema. Estaré en mi habitación. Tengo algunas cosas que hacer."
    return
label c22s004_BookFerrarini:
    scene black with dissolve
    "Subes a tu habitación después de despedirte de todo el mundo y darle un largo abrazo a [sca]."
    "Consigues mover la reserva del Ferrarini de [emm] al jueves a mediodía."
    "Tendréis que pasar la noche en Monterey para devolverlo al día siguiente, con lo que reservas un hotel cerca del aeropuerto."
    "Una habitación sencilla para ti y una doble para [bet] y [emm]."
    stop music fadeout (1.5)
    "Cuando se lo dices a [emm] se emociona muchísimo y quiere empezar a preparar las maletas."
    return
label c22s005_SamCall:
    if _in_replay:
        call mrS3_rename from _call_mrS3_rename_22
        call mrS3_sam_route from _call_mrS3_sam_route
        if sam._var("route"):
            call mrS3_sam_pregnant from _call_mrS3_sam_pregnant
        call mrS3_eva_route from _call_mrS3_eva_route_1
        if not eva._var("route"):
            call mrS3_ama_route from _call_mrS3_ama_route_3
    play music ("music/Inspiring-Upbeat-Ambient.ogg")
    "Después de pasar un rato en la piscina charlando con todas las chicas, te llama [sam] para invitarte a té con pastas."
    "Parece empeñada en hacerte engordar otra vez, pero no puedes declinar la invitación."
    if sam._var("route"):
        "La prueba de embarazo hace un día que ha dado el resultado."
    "Quedáis para una hora después."
    scene c22s005_005a with fade
    "Llegas puntual a la hora acordada. Puedes oler las pastas desde la puerta. El niño gordo de tu pasado grita por salir."
    "*Ding-Dong*"
    call BlinkXPS3 ("c22s005_010" , "f") from _call_BlinkXPS3_885
    sam "Buenas tardes, [mc]. Pasa, acabo de sacar las pastas del horno."
    mc "¿[jam] y [sim] no están?"
    scene c22s005_005b with dissolve
    sam "[sim] está trabajando, llegará en un rato, y [jam] ha salido a tomar algo con un amigo."
    mc "¿Qué? ¿[jam] tiene amigos? ¿Quién es el otro pringado?"
    sam "*Risa* No tengo ni idea. Siéntate en el sofá. Ahora llevo las pastas y el té."
    call BlinkXPS3 ("c22s005_015" , "f") from _call_BlinkXPS3_886
    sam "Cuéntame qué novedades hay. Aparte de lo que se ha dicho en el grupo de WhatsUp, claro."
    mc "*Risa* Como no me habéis invitado, no sé lo que se ha comentado."
    call BlinkXPS3 ("c22s005_020" , "d") from _call_BlinkXPS3_887
    sam "Yo estaba en contra de dejarte fuera al principio, pero ha sido una buena idea. Hay cosas que otras chicas no se sentirían cómodas diciendo si estuvieras dentro."
    mc "*Risa* Pero se sienten cómodas si está [jam]."
    call BlinkXPS3 ("c22s005_025" , "d") from _call_BlinkXPS3_888
    sam "Es diferente y lo sabes..."
    if eva._var("route") or ama._var("route"):
        sam "Si una chica con pinta de peligrosa pregunta cuál es tu plato favorito porque quiere preparar una cita, por ejemplo, [jam] puede aportar algo."
        sam "Por cierto, felicidades."
        mc "Gracias."
        call BlinkXPS3 ("c22s005_030" , "d") from _call_BlinkXPS3_889
        sam "Si lo pregunta en un sitio donde tú lo puedes leer..."
        mc "Se perdería la sorpresa."
    else:
        sam "Hay cosas que podemos hablar entre chicas, y que las cohibiría si un chico hetero estuviera en el grupo."
        mc "Lo entiendo."
    mc "Pero un día le cogeré el móvil a [jam] para leer el grupo. *Risa* Aún recuerdo su contraseña."
    call BlinkXPS3 ("c22s005_035" , "d") from _call_BlinkXPS3_890
    sam "*Risa* No te lo recomendaría. Seguramente nos mirarías a todas de forma distinta. Se dicen muchas tonterías en ese grupo."
    mc "Cada vez tengo más ganas de leerlo. *Risa*"
    if persistent.family:
        call BlinkXPS3 ("c22s005_040" , "d") from _call_BlinkXPS3_891
        sam "También cosas serias. Ha sido una sorpresa lo de [sca] y lo de tu padre."
        mc "Ha sido muy emotivo. Todo el mundo veía a [sca] como parte de la familia... menos ella."
        mc "Ahora ya no puede negar que es una Marks más."
    if sam._var("route"):
        call c22s005_SamPregnancyResult from _call_c22s005_SamPregnancyResult
    return
label c22s005_SamPregnancyResult:
    mc "Pero hay algo que me preocupa..."
    call BlinkXPS3 ("c22s005_045" , "d") from _call_BlinkXPS3_892
    sam "¿Qué, cielo?"
    mc "Que, desde que he llegado, no me has dado ni un simple beso."
    scene c22s005_050An with dissolve
    pause (1.5)
    call BlinkXPS3 ("c22s005_050" , "d") from _call_BlinkXPS3_893
    sam "*Risa* Te he invitado a comer pastas sabrosas no a besar dulces labios."
    mc "Bueno, puedo hacer las dos cosas. *Risa* No son incompatibles."
    call BlinkXPS3 ("c22s005_055" , "d") from _call_BlinkXPS3_894
    sam "Seguramente te reirás de mí, y tienes que saber que el sexo contigo me encanta..."
    mc "A mí también, cariño."
    call BlinkXPS3 ("c22s005_060" , "d") from _call_BlinkXPS3_895
    sam "Que me interrumpas no me gusta tanto, sin embargo. *Risa*"
    sam "Pero a veces echo de menos que nos sentemos a charlar como hacíamos antes, cuando sólo era tu segunda madre."
    mc "[sam], siempre serás mi segunda madre..."
    if not persistent.family:
        mc "O tercera..."
    mc "Y me encanta charlar contigo, pero puedes besarme y podemos charlar. No está reñida una cosa con la otra."
    call BlinkXPS3 ("c22s005_065" , "d") from _call_BlinkXPS3_896
    sam "Si empiezo a besarte, no estoy segura de que hubiera podido parar antes de llevarte a la habitación. *Risa*"
    sam "Hace muchos días que tú y yo no..."
    mc "Lo sé. Estos días atrás han sido complicados."
    mc "Y aún tenemos que mirar la prueba de embarazo."
    call BlinkXPS3 ("c22s005_070" , "d") from _call_BlinkXPS3_897
    sam "No te puedes llegar a imaginar lo difícil que ha sido no mirarla cuando empezó a pitar."
    mc "Sí que me lo imagino."
    call BlinkXPS3 ("c22s005_075" , "d") from _call_BlinkXPS3_898
    sam "*Risa* Y yo tenía ganas de charlar contigo y ahora en lo único que voy a poder pensar es en la prueba."
    mc "Pues la miramos y seguimos charlando. *Risa* Salga lo que salga, tendremos temas nuevos de los que hablar."
    call BlinkXPS3 ("c22s005_080" , "d") from _call_BlinkXPS3_899
    sam "Sabes que si entras en esa habitación no vas a salir vestido independientemente del resultado, ¿no?"
    sam "Ya sea para celebrarlo o para buscar una nueva oportunidad, te voy a desnudar. *Risa*"
    mc "*Risa* Yo no he dicho que vaya a entrar. Puedes ir tú y traerlo."
    mc "Y creía que te daba lo mismo el resultado."
    call BlinkXPS3 ("c22s005_085" , "d") from _call_BlinkXPS3_900
    sam "Me daba lo mismo, y me sigue dando lo mismo. Si me quedo embarazada de ti me pondré muy contenta pese a los riesgos."
    sam "Si no me quedo embarazada, me pondré muy contenta porque nunca me veras en modo ballena. *Risa* Y podremos seguir intentándolo."
    mc "*Risa* Estoy seguro de que serás una ballena preciosa."
    call BlinkXPS3 ("c22s005_090" , "v") from _call_BlinkXPS3_901
    sam "¡Mielda! Me has convencido. Voy a buscar la prueba."
    mc "¿Quieres que te acompañe?"
    call BlinkXPS3 ("c22s005_095" , "d") from _call_BlinkXPS3_902
    sam "Claro. La saqué de la caja y la escondí debajo de los calcetines. En el momento en que quite los calcetines sabré el resultado."
    sam "Llevo dos días sin ponerme calcetines para no verlo. *Risa* No lo quería ver sin ti."
    mc "Vamos. *Risa* No hay razón para seguir esperando."
    call BlinkXPS3 ("c22s005_200" , "f") from _call_BlinkXPS3_903
    sam "Ahora que estoy aquí, me estoy empezando a poner nerviosa."
    stop music fadeout (1.5)
    mc "Cuanto más lo pienses, más nerviosa te pondrás *Risa* Hazlo como si arrancaras una tirita."
    play music ("music/IWonderWhatIllDoToday.ogg")
    if sam._var("pregnant"):
        $ sam._var("pregnancyDiscovered", True)
        call c22s005_SamPregnant from _call_c22s005_SamPregnant
    else:
        $ sam._var("pregnancyDiscovered", False)
        call c22s005_SamNotPregnant from _call_c22s005_SamNotPregnant
    stop music fadeout (1.5)
    mc "Me parece una idea estupenda. *Risa*"
    return
label c22s005_SamPregnant:
    scene c22s005_205An1 with dissolve
    pause (3.0)
    sam "¡Felicidades, Papá!"
    mc "¿Ha salido verde?"
    call BlinkXPS3 ("c22s005_210" , "d") from _call_BlinkXPS3_904
    sam "*Risa* ¿Qué he hecho yo para merecer un hombre así?"
    sam "Si hubiera salido rojo, ¿te hubiera felicitado y llamado Papá?"
    call c22s005_Kid from _call_c22s005_Kid
    sam "Bueno, de momento podemos ir practicando por si sale niña que no nos pille oxidados, ¿no?"
    return
label c22s005_SamNotPregnant:
    scene c22s005_205An2 with dissolve
    pause (3.0)
    sam "Pues no vamos a tener un hijo, de momento."
    scene c22s005_205d with dissolve
    sam "No verás mi modo ballena. *Risa*"
    mc "¿Ha salido rojo?"
    call BlinkXPS3 ("c22s005_210" , "d") from _call_BlinkXPS3_905
    sam "*Risa* ¿Qué he hecho yo para merecer un hombre así?"
    sam "Si hubiera salido verde, ¿te hubiera dicho que no íbamos a tener un hijo?"
    call c22s005_Kid from _call_c22s005_Kid_1
    sam "Bueno, de momento hay que repetir el intento para tener el primero, ¿no?"
    return
label c22s005_Kid:
    mc "*Risa* ¡Joder, [sam]! Era una forma de hablar..."
    call BlinkXPS3 ("c22s005_215" , "d") from _call_BlinkXPS3_906
    sam "¡Vigila esa boca! No voy a permitir que el padre de mi hijo hable así delante del niño."
    sam "Así que ve acostumbrándote a no decir tacos. No se los permito a mis hijos y no te los voy a permitir a ti."
    mc "¿Hijo? ¿No quieres una niña?"
    call BlinkXPS3 ("c22s005_220" , "d") from _call_BlinkXPS3_907
    sam "Me da lo mismo. Me ha salido hijo en vez de hija sin ninguna razón..."
    sam "Supongo que en el fondo no me da tanto lo mismo."
    mc "Pues que sea niño. Y si sale niña, hacemos otro intento. *Risa*"
    call BlinkXPS3 ("c22s005_225" , "d") from _call_BlinkXPS3_908
    return
label c22s005_SamSex:
    if _in_replay:
        call mrS3_rename from _call_mrS3_rename_23
        call mrS3_sam_pregnant from _call_mrS3_sam_pregnant_1
        call mrS3_sam_blackPanther from _call_mrS3_sam_blackPanther
        if sam._var("pregnant"):
            $ sam._var("pregnancyDiscovered", True)
        call mrS3_sim_route from _call_mrS3_sim_route
    scene c22s005_230An with dissolve
    play music ("music/SexyLoungeMusic.ogg")
    "[sam] empieza a besarte apasionadamente y, antes de que os deis cuenta, ambos estáis desnudos."
    "La ropa ha pasado mágicamente de estar en vuestros cuerpos a estar en el suelo."
    call BlinkXPS3 ("c22s005_240" , "d") from _call_BlinkXPS3_909
    mc "Vamos un poco acelerados hoy, ¿no?"
    sam "No quiero que pase como la última vez y que a [sim] le dé tiempo a llegar a casa."
    sam "Aunque ya lo sepa, prefiero tenerte para mí durante un rato."
    mc "Me parece perfecto. Yo también quiero tenerte para mí, sin interrupciones."
    scene c22s005_245An with dissolve
    sam "*Risa* ¿Qué haces?"
    if sam._var("pregnant"):
        sam "*Risa* ¿Me levantas ahora antes de que me ponga hecha una vaca?"
    mc "Llevarte a un sitio donde te voy a tener sólo para mí."
    call BlinkXPS3 ("c22s005_250" , "f") from _call_BlinkXPS3_910
    sam "¿Qué? ¿Aquí? ¿Al lado de la ventana? Nos pueden ver..."
    scene c22s005_250d with dissolve
    pause (1.0)
    call BlinkXPS3 ("c22s005_250" , "d") from _call_BlinkXPS3_911
    mc "Creo que son los ladrillos con las vistas más afortunadas del mundo. *Risa*"
    sam "¿No prefieres ir a la cama?"
    mc "Prefiero no perder ni un segundo llevándote a la cama. Esto va a dejar a tus pastitas a la altura del betún. *Risa*"
    call BlinkXPS3 ("c22s005_255" , "d") from _call_BlinkXPS3_912
    sam "*Risa* ¡Con mis pastitas no te metas!"
    if sam._var("naturalPubicHair"):
        mc "No me meto. Están deliciosas, pero no son rival para la Pantera Negra."
        call BlinkXPS3 ("c22s005_260a" , "d") from _call_BlinkXPS3_913
        sam "¿Pantera Negra? *Risa*"
        mc "Es peludito y tú eres felina, con lo que el nombre le pega."
    else:
        mc "No me meto. Están deliciosas, pero no son rival para el Gato Esfinge."
        call BlinkXPS3 ("c22s005_260b" , "d") from _call_BlinkXPS3_914
        sam "¿Gato Esfinge? *Risa*"
        mc "No tiene ni un pelo y tú eres felina, con lo que el nombre le pega."
    sam "¡Estás loco! *Risa*"
    mc "¿Un loco haría esto?"
    scene c22s005_265a with hpunch
    "Hundes tu cabeza entre sus piernas y das un simple lametón a su botón del placer."
    sam "*Gemido* Un loco no sé..."
    "Puedes asegurar que alguien loco por ella lo haría con gusto. Ese alguien eres tú."
    scene c22s005_100pv with dissolve
    show c22s005_100v with dissolve
    "Empiezas a trabajar con tu lengua recorriendo sus labios, provocándola con tus movimientos alrededor de su agujero."
    sam "*Gemido* ¿Cómo puedes conocer cada sitio que me gusta? *Jadeo*"
    mc "*Slurp incrédulo*"
    "No puedes creer que todavía no sepa que conoces su cuerpo tan bien como el tuyo, aunque solamente sea vuestra cuarta vez juntos."
    sam "*Jadeo* Sigue así... *Gemido* Me está encantando... *Gemido* Lentamente... *Jadeo*"
    "Lentamente por ahora. Sus húmedos labios en tus labios están pidiendo más. Sus caderas empiezan a moverse con más ansia."
    if sam._var("naturalPubicHair"):
        scene c22s005_105pv with dissolve
        hide c22s005_100v with dissolve
        show c22s005_105v with dissolve
    else:
        scene c22s005_110pv with dissolve
        hide c22s005_100v with dissolve
        show c22s005_110v with dissolve
    "Aceleras el movimiento de tu lengua de forma repentina tomando a [sam] por sorpresa."
    sam "*JADEO* ¡OOOOH! *GEMIDO* ¡Eso es mejor aún! *GEMIDO* ¡Sigue así!"
    mc "*Slurp afirmativo*"
    "Tu lengua continúa aumentando la velocidad, entrando dentro de [sam], recorriendo cada pliegue de sus labios, jugueteando con su clítoris."
    sam "*GEMIDO* ¡NO, NO, NO! *JADEO* ¡SÍ! *JADEO*"
    mc "*Slurp inquisitivo*"
    "[sam] empieza a desconcertarte. Sabes lo que su cuerpo te está pidiendo, pero no entiendes lo que quiere ella."
    if sam._var("naturalPubicHair"):
        call BlinkXPS3 ("c22s005_270a" , "d") from _call_BlinkXPS3_915
    else:
        call BlinkXPS3 ("c22s005_270b" , "d") from _call_BlinkXPS3_916
    hide c22s005_105v
    hide c22s005_110v
    sam "*GEMIDO* ¡PARA! *JADEO*"
    mc "¿Pasa algo, cielo?"
    if sam._var("naturalPubicHair"):
        call BlinkXPS3 ("c22s005_275a" , "d") from _call_BlinkXPS3_917
    else:
        call BlinkXPS3 ("c22s005_275b" , "d") from _call_BlinkXPS3_918
    sam "*Gemido* Quiero que me folles. *Jadeo* Aquí, en la mesa. *Jadeo* Fóllame. Ahora."
    mc "Pareces ansiosa..."
    sam "*Gemido* Que me la metas cuando estoy a punto de correrme es una de las mejores sensaciones. *Jadeo* Y estoy a punto..."
    if sam._var("naturalPubicHair"):
        scene c22s005_135pva with fade
    else:
        scene c22s005_140pva with fade
    mc "¿Lista?"
    sam "*Gemido* Hazlo ya, antes de que pierda esta sensación..."
    if sam._var("naturalPubicHair"):
        show c22s005_135va
        pause (0.5)
        scene c22s005_135dva
    else:
        show c22s005_140va
        pause (0.5)
        scene c22s005_140dva
    "Penetras a [sam] con una embestida profunda en la que llegas al fondo de su coño."
    if sam._var("naturalPubicHair"):
        call OrgasmXS3 ("c22s005_280a") from _call_OrgasmXS3_26
    else:
        call OrgasmXS3 ("c22s005_280b") from _call_OrgasmXS3_27
    sam "*GEMIDO* ¡SÍ! *JADEO*"
    "El orgasmo llega inmediatamente. Su coño estruja tu polla con fuerza mientras oleadas de placer recorren su cuerpo."
    sam "*GEMIDO* ¡Esto es lo mejor! *GEMIDO* ¡Muévete! *GEMIDO* ¡No me dejes perderlo!"
    if sam._var("naturalPubicHair"):
        scene c22s005_135pv with dissolve
        show c22s005_135v
        hide c22s005_135va
    else:
        scene c22s005_140pv with dissolve
        show c22s005_140v
        hide c22s005_140va
    "Empiezas a bombear con tus caderas siguiendo las órdenes de [sam]. No deseas que pierda la sensación que está recorriendo su cuerpo."
    sam "*Gemido* No sé cómo puedes hacerlo. *Jadeo*"
    "No tienes ni idea de a qué se refiere, pero parece bueno, con lo que sigues haciéndolo."
    sam "*Gemido* No te dejas un solo punto sensible por tocar. *Gemido*"
    "Ese es el secreto de dos cuerpos acoplándose inconscientemente el uno al otro para darse el máximo placer."
    scene c22s005_125pv with dissolve
    show c22s005_125v
    hide c22s005_135v
    hide c22s005_140v
    "Desde que la has penetrado, [sam] encadena orgasmo tras orgasmo luchando contra Mjolnir a cada embestida."
    sam "*GEMIDO* ¡Sigue así! *JADEO* ¡MÁS!"
    if sam._var("naturalPubicHair"):
        "El peludo coño de [sam] se intenta cerrar sobre su ástil mientras el martillo intenta abrirlo en una lucha sin fin, sin un ganador claro."
    else:
        "El depilado coño de [sam] se intenta cerrar sobre su ástil mientras el martillo intenta abrirlo en una lucha sin fin, sin un ganador claro."
    sam "*JADEO* ¡Más profundo! *GEMIDO* ¡Más rápido!"
    "No hay un ganador claro porque los dos dan y reciben placer al mismo tiempo, en un espectáculo de sexo generoso en el que se busca el placer del otro."
    scene c22s005_130pv with dissolve
    show c22s005_130v
    hide c22s005_125v
    "Pero todo combate llega a su fin, y éste está a punto de acabar por tu parte. El elástico coño de [sam] te acerca a tu límite a una velocidad increíble."
    sam "*JADEO* ¡NO PUEDO CREERLO! *JADEO* ¡NO PUEDO PARAR DE CORRERME! *JADEO*"
    "Puedes empezar a notar cómo tus piernas empiezan a tensarse con cada embestida, con la conocida sensación que anuncia tu orgasmo inminente."
    sam "*GEMIDO* ¡Córrete dentro! *GEMIDO* ¡No quiero que se desperdicie ni una gota de leche! *GEMIDO*"
    "Siempre es un placer hacer caso a [sam] cuando lo que dice tiene sentido. Cuando sus deseos coinciden con los tuyos."
    if not sam._var("pregnant") and persistent.pregnancy:
        if persistent.walkthrough:
            $ wt1 = _("[sam] embarazada.")
            $ wt2 = _("Sin consecuencias.")
        else:
            $ wt1 = ""
            $ wt2 = ""
        menu:
            "Correrte dentro." (wt=wt2):
                pass
            "Correrte dentro. Ir a por el bebé." (wt=wt1):
                $ sam._var("pregnant", True)
                play sound ("music/OldMusicBox5.ogg")
    if sam._var("naturalPubicHair"):
        call OrgasmXS3 ("c22s005_285a") from _call_OrgasmXS3_28
    else:
        call OrgasmXS3 ("c22s005_285b") from _call_OrgasmXS3_29
    mc "¡Mpfft!"
    "Descargas una gran cantidad de semen en el coño de [sam], del que escapan algunas gotas mientras sigues bombeando para maximizar vuestro placer."
    sam "*GEMIDO* ¡SÍ! *JADEO* ¡LA QUIERO TODA!"
    stop music fadeout (1.5)
    "Poco después, tras unas últimas embestidas, los dos os quedáis inmóviles."
    call BlinkXPS3 ("c22s005_290" , "d") from _call_BlinkXPS3_919
    play music ("music/Stardust.ogg")
    mc "Lo hemos conseguido. *Risa* No nos han interrumpido."
    sam "Sí, lo hemos conseguido. *Risa* ¿Sabes que cuando te ríes Mjolnir vibra dentro de mí?"
    mc "Y cuando te ríes tú mi corrida empieza a escaparse. *Risa*"
    call BlinkXPS3 ("c22s005_295" , "d") from _call_BlinkXPS3_920
    sam "¡Eso no lo podemos consentir! *Risa contenida* ¡Llévame a la cama!"
    if sam._var("pregnancyDiscovered"):
        mc "Ya estás embarazada, no hace falta que acapares mi corrida. *Risa*"
    else:
        mc "¿Tan ansiosa estás porque el próximo test salga positivo? *Risa*"
    call BlinkXPS3 ("c22s005_300" , "d") from _call_BlinkXPS3_921
    sam "¡No es eso! ¡Es que si empiezo a gotear voy a poner el suelo perdido!"
    mc "Entonces no se hable más. *Risa* A la cama."
    call BlinkXPS3 ("c22s005_305" , "f") from _call_BlinkXPS3_922
    "Sin salir de su interior la llevas a la cama y te tumbas delicadamente sin soltarla, empalándola en Mjolnir, que aún no muestra signos de flacidez."
    sam "Mmmm... eso me ha gustado... Creo que podría acostumbrarme a que me movieses así por la casa."
    mc "No estaría mal. De la cama a la mesa de la cocina. Después al mármol de la cocina. Más tarde a la ducha..."
    call BlinkXPS3 ("c22s005_310" , "d") from _call_BlinkXPS3_923
    sam "*Risa* Sí, semental, sí. Y vas a tener aguante para tanto."
    mc "Si no fuéramos siempre con prisas y con miedo a que nos pillasen, un día te lo demostraría. *Risa*"
    mc "Creía que ahora que todo ha salido a la luz sería distinto."
    call BlinkXPS3 ("c22s005_315" , "d") from _call_BlinkXPS3_924
    sam "Será distinto, pero aún no me siento cómoda teniendo sexo con [sim] o [jam] en casa."
    mc "Lo entiendo. Quizás podamos repetir una salida a un hotel, y esta vez quedarnos a dormir."
    if sam._var("naturalPubicHair"):
        scene c22s005_315d with dissolve
    else:
        scene c22s005_315e with dissolve
    pause (0.8)
    call BlinkXPS3 ("c22s005_315" , "d") from _call_BlinkXPS3_925
    sam "Me encantaría. Es que me sentiría rara si [jam] o [sim] supieran lo bien que me siento con Mjolnir dentro."
    mc "Supongo que se lo deben imaginar, [sam.nick]."
    call BlinkXPS3 ("c22s005_320" , "d") from _call_BlinkXPS3_926
    sam "Lo sé, pero una cosa es que sepan que tú y yo tenemos sexo, y otra diferente que estén en el salón escuchándome gemir."
    mc "*Risa* [jam] seguramente se reiría de ti durante un par de semanas, sobre todo si descubre que te avergüenza."
    call BlinkXPS3 ("c22s005_325" , "d") from _call_BlinkXPS3_927
    sam "*Risa* Seguro. [sim] seguramente no se reiría tanto."
    if sim._var("route"):
        sam "Si yo estuviera en el salón escuchándola gemir a ella... sé que tenéis sexo, pero no me imagino escucharos o veros. *Risa*"
    mc "Creía que lo habíais hablado la última vez."
    call BlinkXPS3 ("c22s005_330" , "d") from _call_BlinkXPS3_928
    sam "Hablamos de muchas cosas, pero ese tema no salió."
    sam "Nos había pillado a punto de empezar el segundo round. No era el momento de sacar temas que podían ser escabrosos."
    stop music fadeout (1.5)
    mc "Lo entiendo..."
    return
label c22s006_Simone:
    if _in_replay:
        call mrS3_rename from _call_mrS3_rename_24
        call mrS3_sam_route from _call_mrS3_sam_route_1
        if sam._var("route"):
            call mrS3_sam_pregnancyDiscovered from _call_mrS3_sam_pregnancyDiscovered
        call mrS3_sim_route from _call_mrS3_sim_route_1
        if sim._var("route"):
            call mrS3_sim_pregnancyBeforeSunday from _call_mrS3_sim_pregnancyBeforeSunday
    if sam._var("route"):
        scene c22s006_005a with hpunch
        play music ("music/MorningFunnyBeat.ogg")
        sim "*Desde el salón* ¡Ya estoy en casa!"
        scene c22s006_005b with hpunch
        sam "*Susurrando* ¡Tápate!"
        scene c22s006_005c with dissolve
        play sound ("music/knock.ogg")
        "*Knock-Knock*"
        sim "*A través de la puerta* Mamá, ¿estás ahí? ¿Puedo pasar?"
        call BlinkXPS3 ("c22s006_010" , "d") from _call_BlinkXPS3_929
        sam "Espera un momento... nos estamos vistiendo..."
        sim "*A través de la puerta* OK. Os espero en el sofá. He visto las pastitas... *Risa*"
        sim "*A través de la puerta* Aunque si necesitáis más tiempo, puedo irme y volver luego. Cogeré unas pastitas para el camino."
        mc "No hace falta, [sim]. Danos un momento para vestirnos."
        call BlinkXPS3 ("c22s006_015" , "f") from _call_BlinkXPS3_930
        sam "Vamos a vestirnos..."
        mc "¿Te sientes incómoda?"
        call BlinkXPS3 ("c22s006_020" , "f") from _call_BlinkXPS3_931
        sam "Es raro que tu hija sepa que acabas de tener sexo..."
        mc "Pero es mucho mejor que la última vez que nos pilló. *Risa*"
        call BlinkXPS3 ("c22s006_025" , "f") from _call_BlinkXPS3_932
        sam "Hemos charlado mucho desde entonces... al menos no ha entrado sin llamar. Suele hacerlo..."
        mc "Por eso me has dicho que me tapara, ¿no?"
        sim "*Desde el salón* Sabéis que este piso tiene unas paredes de mielda y que se oye todo, ¿verdad?"
        mc "*Risa* No pasa nada. Sin secretos."
        call BlinkXPS3 ("c22s006_030" , "d") from _call_BlinkXPS3_933
        sam "Vamos a vestirnos en silencio..."
        mc "*Risa* [sim], creo que tu madre está más incómoda que tú."
        sim "*Desde el salón* No tienes por qué estarlo, Mamá."
        if sim._var("route"):
            sim "*Desde el salón* Si te va a servir para estar menos incómoda, nuestra última vez fue en la fiesta de la piscina."
            call BlinkXPS3 ("c22s006_035" , "d") from _call_BlinkXPS3_934
            sam "*Susurrando* ¿Qué? ¿Cuándo?"
            "Te encoges de hombros."
        else:
            sim "*Desde el salón* No me voy a comportar como una niña malcriada como la última vez."
        call BlinkXPS3 ("c22s006_040" , "f") from _call_BlinkXPS3_935
        sam "¿Vamos?"
        mc "Me sorprende que no te hayas puesto la bata sexy del otro día..."
        call BlinkXPS3 ("c22s006_045" , "d") from _call_BlinkXPS3_936
        sam "*Susurrando* Creo que no me la voy a volver a poner nunca sin recordar aquella conversación."
        mc "*Risa* No importa, estás sexy te pongas lo que te pongas. Vamos antes de que [sim] se canse de esperarnos."
        mc "Pero sería adecuada. La bata de las veces que [sim] nos pilla juntos. *Risa*"
        call BlinkXPS3 ("c22s006_050a" , "f") from _call_BlinkXPS3_937
        stop music fadeout (1.5)
        sim "Hola de nuevo. Las pastas te han quedado buenísimas hoy, Mamá."
    else:
        call BlinkXPS3 ("c22s006_050b" , "d") from _call_BlinkXPS3_938
        sim "Hola. Natalie me ha traído a casa. ¿Has hecho pastas? Se huelen desde el ascensor."
    play music ("music/romantic-day.ogg")
    if sim._var("route"):
        call KissXPS3 ("c22s006_055" , "f") from _call_KissXPS3_17
        sim "Hola, cielo."
        mc "Hola, preciosa."
    else:
        mc "Hola, [sim]."
    if sam._var("pregnancyDiscovered"):
        call BlinkXPS3 ("c22s006_060" , "d") from _call_BlinkXPS3_939
        sam "Tenemos que contarte una cosa, [sim]."
        mc "No hay prisa, deja que se coma las pastas con tranquilidad."
        call BlinkXPS3 ("c22s006_065" , "d") from _call_BlinkXPS3_940
        sam "Cuanto antes mejor. Ya sabes que los secretos tienden a enquistarse y después no encuentras el momento."
        mc "Tienes razón..."
        call BlinkXPS3 ("c22s006_070" , "d") from _call_BlinkXPS3_941
        sim "Estás embarazada, ¿no?"
        call BlinkXPS3 ("c22s006_075" , "d") from _call_BlinkXPS3_942
        sam "¿Cómo lo sabes?"
        call BlinkXPS3 ("c22s006_080" , "d") from _call_BlinkXPS3_943
        sim "*Risa* Bueno, parece ser un secreto que compartís y acabáis de tener sexo, con lo que no es que hayáis roto."
        sim "Ayer oí un pitido en tu habitación, con lo que debe ser el test de embarazo."
        if not sim._var("route"):
            sim "[ama] me habló de ellos."
        call BlinkXPS3 ("c22s006_085" , "d") from _call_BlinkXPS3_944
        sim "Es fácil de deducir. *Risa* Aunque no os voy a felicitar por si estoy equivocada."
        sim "También es posible que queráis decirme que os vais de fin de semana romántico. *Risa*"
        call BlinkXPS3 ("c22s006_090" , "d") from _call_BlinkXPS3_945
        sam "Bueno... sí... vas a tener un hermano."
        mc "Tu hija es demasiado lista a veces."
        call BlinkXPS3 ("c22s006_095" , "v") from _call_BlinkXPS3_946
        sim "Ven aquí y dame un abrazo, Mamá. Felicidades."
        call BlinkXPS3 ("c22s006_100" , "d") from _call_BlinkXPS3_947
        sam "Gracias, cariño."
        if sim._var("route"):
            sim "Felicidades a ti también, cielo."
        else:
            sim "Felicidades a ti también, [mc]."
        sam "Tener un hijo a mi edad... ¿Quién me lo iba a decir a mí?"
        mc "Yo te lo podía haber dicho. Ya tienes dos. *Risa*"
        "Las felicitaciones y las risas continúan durante un rato antes de que las chicas vuelvan a sentarse."
        "No hay abrazos para ti."
        "Siempre te has fijado en que todo el mundo le toca la barriga a la embarazada cuando la felicitan."
        "Pero nadie le toca los huevos al padre diciendo \"¡Buen trabajo!\"."
        if sim._var("route"):
            call BlinkXPS3 ("c22s006_105" , "f") from _call_BlinkXPS3_948
            sim "Yo también os tengo que contar algo..."
            call BlinkXPS3 ("c22s006_110" , "d") from _call_BlinkXPS3_949
            if sim._var("pregnancyDiscovered"):
                sim "Yo también estoy embarazada..."
                call c22s006_HaveYouLookedAtIt from _call_c22s006_HaveYouLookedAtIt
            else:
                sim "Mi test ha dado negativo..."
                call c22s006_LookedAtIt from _call_c22s006_LookedAtIt
            call c22s006_Commando from _call_c22s006_Commando
            if sim._var("pregnancyDiscovered"):
                sam "Déjame abrazar a mi niña que ya no es tan niña, [mc]. *Risa* Me vais a hacer abuela..."
                scene c22s006_100d with dissolve
                sam "Felicidades, mi niña."
                sim "Gracias, Mamá. Me vas a tener que dar clases de cambio de pañales."
                sam "Aprenderemos juntas. Los modelos han cambiado desde que te los cambiaba a ti."
                sim "Por alguna razón, me hace ilusión que mi hijo y mi hermano crezcan juntos."
            else:
                call BlinkXPS3 ("c22s006_140" , "d") from _call_BlinkXPS3_950
                sim "Habrá que hacer otra prueba para saber si el domingo..."
                mc "Puedo traer una..."
                call BlinkXPS3 ("c22s006_145" , "d") from _call_BlinkXPS3_951
                sim "No hace falta. Cuando vayamos a tu casa la volvemos a hacer. Ya te he dicho que no tengo prisa."
        scene c22s006_200An with dissolve
        call c22s006_Talk from _call_c22s006_Talk
    else:
        scene c22s006_200An with dissolve
        "Pasáis un rato charlando sobre nimiedades."
        if sam._var("route"):
            "Nadie quiere hablar de lo que estabais haciendo cuando [sim] ha llegado."
        if sim._var("route"):
            call BlinkXPS3 ("c22s006_105" , "f") from _call_BlinkXPS3_952
            sim "Os tengo que contar algo..."
            call BlinkXPS3 ("c22s006_110" , "d") from _call_BlinkXPS3_953
            if sim._var("pregnancyDiscovered"):
                sim "Estoy embarazada..."
                call c22s006_HaveYouLookedAtIt from _call_c22s006_HaveYouLookedAtIt_1
            else:
                sim "Mi test de embarazo ha dado negativo..."
                call c22s006_LookedAtIt from _call_c22s006_LookedAtIt_1
            call c22s006_Commando from _call_c22s006_Commando_1
            if sim._var("pregnancyDiscovered"):
                sam "Déjame abrazar a mi niña que ya no es tan niña, [mc]. *Risa* Me vais a hacer abuela..."
                scene c22s006_100d with dissolve
                sam "Felicidades, mi niña."
                sim "Gracias, Mamá. Me vas a tener que dar clases de cambio de pañales."
                sam "Aprenderemos juntas. Los modelos han cambiado desde que te los cambiaba a ti."
                sim "Sé que vas a ser la mejor abuela del mundo."
            else:
                call BlinkXPS3 ("c22s006_140" , "d") from _call_BlinkXPS3_954
                sim "Habrá que hacer otra prueba para saber si el domingo..."
                mc "Puedo traer una..."
                call BlinkXPS3 ("c22s006_145" , "d") from _call_BlinkXPS3_955
                sim "No hace falta. Cuando vayamos a tu casa la volvemos a hacer. Ya te he dicho que no tengo prisa."
                if sam._var("route"):
                    call BlinkXPS3 ("c22s006_150" , "d") from _call_BlinkXPS3_956
                    sam "Yo también me tengo que hacer una. Mi test ha salido negativo, pero ¿quién sabe si con lo de hoy la cosa ha cambiado?"
                    call BlinkXPS3 ("c22s006_155" , "d") from _call_BlinkXPS3_957
                    sim "Entonces vamos el jueves y nos la hacemos las dos juntas."
                    mc "El jueves estaré en Monterey con [emm] y Tía [bet]."
                    call BlinkXPS3 ("c22s006_160" , "d") from _call_BlinkXPS3_958
                    sam "Pues entonces el viernes, o el sábado... no hay prisa. La gente normal tarda dos semanas o más en saberlo."
                    sam "Somos afortunadas de poder saberlo en tan solo tres o cuatro días."
        scene c22s006_200An with dissolve
        if sam._var("route") or sim._var("route"):
            call c22s006_Talk from _call_c22s006_Talk_1
    stop music fadeout (1.5)
    "Cuando se acerca la hora de la cena, pese a que te invitan a quedarte, decides ir a casa."
    return
label c22s006_HaveYouLookedAtIt:
    mc "¿Qué? ¿Ya lo has mirado? *Risa* ¿No podías aguantar la intriga?"
    return
label c22s006_LookedAtIt:
    mc "¿Lo has mirado ya? ¿Cómo te sientes?"
    call BlinkXPS3 ("c22s006_115" , "d") from _call_BlinkXPS3_959
    sim "Bien, te dije que quería tener un par de hijos, pero no que los quisiera tener ya. Aunque no me importaría, no tengo prisa."
    mc "Tenemos todo el tiempo del mundo, no te preocupes."
    return
label c22s006_Commando:
    call BlinkXPS3 ("c22s006_120" , "d") from _call_BlinkXPS3_960
    sim "No es que lo quisiera mirar sin ti. Esta mañana, mientras me vestía no he podido evitar verlo."
    mc "No pasa nada. Ven aquí, cielo. Quiero un abrazo."
    scene c22s006_120d with fade
    sim "No sabía si te enfadarías..."
    mc "No me puedo enfadar por algo como eso. Y menos aún si es por un accidente."
    call BlinkXPS3 ("c22s006_125" , "d") from _call_BlinkXPS3_961
    sam "Esas cosas las tienes que mirar con [mc], cielo. Así se comparten las emociones de otra forma."
    call BlinkXPS3 ("c22s006_130" , "d") from _call_BlinkXPS3_962
    sim "Lo escondí debajo de las bragas precisamente para no verlo, Mamá."
    call BlinkXPS3 ("c22s006_135" , "d") from _call_BlinkXPS3_963
    sam "*Risa* Lo tienes que esconder en el cajón de los calcetines, cielo. Puedes ir sin calcetines, pero no sin bragas."
    sam "A menos que te guste ir comando, claro. *Risa*"
    return
label c22s006_Talk:
    "Pasáis la tarde charlando sobre nombres de bebés, de pañales, y de todo lo que hay que tener en cuenta."
    "Siempre te sorprendía lo poco que sabías sobre embarazos cuando escuchabas este tipo de conversaciones en la TV."
    "Vas a tener que estudiar mucho cuando tengas tiempo libre. Si alguna vez lo tienes."
    return
label c22s007_LisChat:
    if _in_replay:
        call mrS3_rename from _call_mrS3_rename_25
        $ mc._var("relationships", 0, "set")
        call mrS3_deb_route from _call_mrS3_deb_route_1
        call mrS3_sai_route from _call_mrS3_sai_route_1
        call mrS3_lis_rps (-11, 0, +24) from _call_mrS3_lis_rps
        call mrS3_sam_pregnancyDiscovered from _call_mrS3_sam_pregnancyDiscovered_1
        call mrS3_sim_pregnancyDiscovered from _call_mrS3_sim_pregnancyDiscovered
        if sim._var("pregnancyDiscovered"):
            $ mc._var("relationships", 1, "add")
        if sam._var("pregnancyDiscovered"):
            $ mc._var("relationships", 1, "add")
        if mc._var("relationships")<2:
            call mrS3_rels from _call_mrS3_rels_3
        menu:
            "¿Estás en una relación con [dap] y con [eri]?"
            "Sí.":
                $ dap._var("route", True)
                $ eri._var("route", True)
            "No.":
                $ dap._var("route", False)
                $ eri._var("route", False)
                menu:
                    "¿Estás en una relación con [ama] y con [eva]?"
                    "Sí.":
                        $ ama._var("route", True)
                        $ eve._var("route", True)
                    "No.":
                        $ ama._var("route", False)
                        $ eva._var("route", False)
                        menu:
                            "¿Estás en una relación con [ama] y con [emm]?"
                            "Sí.":
                                $ ama._var("route", True)
                                $ emm._var("route", True)
                            "No.":
                                $ ama._var("route", False)
                                $ emm._var("route", False)
                                menu:
                                    "¿Estás en una relación con [eva] y con [eri]?"
                                    "Sí.":
                                        $ eva._var("route", True)
                                        $ eri._var("route", True)
                                    "No.":
                                        $ eva._var("route", False)
                                        $ eri._var("route", False)
                                        menu:
                                            "¿Estás en una relación con [dap] y con [eva]?"
                                            "Sí.":
                                                $ dap._var("route", True)
                                                $ eva._var("route", True)
                                            "No.":
                                                $ dap._var("route", False)
                                                $ eva._var("route", False)
                                                menu:
                                                    "¿Estás en una relación con [dap] y con [sca]?"
                                                    "Sí.":
                                                        $ dap._var("route", True)
                                                        $ sca._var("route", True)
                                                    "No.":
                                                        $ dap._var("route", False)
                                                        $ sca._var("route", False)
                                                        if persistent.family:
                                                            menu:
                                                                "¿Estás en una relación con [nor] y con [mar]?"
                                                                "Sí.":
                                                                    $ nor._var("route", True)
                                                                    $ mar._var("route", True)
                                                                "No.":
                                                                    $ nor._var("route", False)
                                                                    $ mar._var("route", False)
    scene black with dissolve
    "La cena en casa transcurre sin novedad."
    if sam._var("pregnancyDiscovered"):
        if sim._var("pregnancyDiscovered"):
            "Aparte de las felicitaciones por los nuevos embarazos, comunicados a través del grupo de WhatsUp, no pasa nada interesante."
        else:
            "Aparte de las felicitaciones por el nuevo embarazo, comunicados a través del grupo de WhatsUp, no pasa nada interesante."
    elif sim._var("pregnancyDiscovered"):
        "Aparte de las felicitaciones por el nuevo embarazo, comunicados a través del grupo de WhatsUp, no pasa nada interesante."
    if sam._var("pregnancyDiscovered") or sim._var("pregnancyDiscovered"):
        "Pese a la creación de un grupo en el que estás tú, el anuncio se ha hecho en el grupo en el que no estás. Cada vez lo odias más."
        "El anuncio se ha hecho durante la cena. Supones que el retraso se debe a que [jam] tenía que ser informado en persona en vez de por el grupo."
    call BlinkXPS3 ("c22s007_005" , "d") from _call_BlinkXPS3_964
    play music ("music/UnforeseenMotive.ogg")
    "Al acabar la cena, ayudas a [nor] a recoger la cocina y, de camino a casa, te encuentras con [deb.nick], que ha estado esperándote."
    deb "¿Puedes venir un momento a mi habitación? Hay una conversación pendiente..."
    mc "Por supuesto. ¿De qué quieres hablar?"
    deb "Mejor en mi habitación."
    mc "Ningún problema, pero ¿no molestaremos a [lis]?"
    call BlinkXPS3 ("c22s007_010" , "d") from _call_BlinkXPS3_965
    deb "No te preocupes por [lis]."
    call BlinkXPS3 ("c22s007_015" , "f") from _call_BlinkXPS3_966
    "Al llegar a la puerta de su habitación..."
    play sound ("music/knock.ogg")
    "*Knock-Knock*"
    deb "[lis], soy yo. Vengo con [mc]. ¿Podemos pasar?"
    lis "*A través de la puerta* Dadme un segundo, estoy acabando de ponerme el pijama."
    mc "¿De qué quieres hablar, [deb.nick]? ¿No sería mejor hablarlo en mi habitación o en otro sitio?"
    call BlinkXPS3 ("c22s007_020" , "d") from _call_BlinkXPS3_967
    if deb._var("route"):
        deb "No, cariño. Necesito que sea aquí."
    else:
        deb "No, [mc]. Necesito que sea aquí."
    mc "Sabes que estás sonando muy misteriosa, ¿no?"
    lis "*A través de la puerta* Ya podéis pasar."
    call BlinkXPS3 ("c22s007_025" , "d") from _call_BlinkXPS3_968
    deb "Pasa tú primero."
    mc "Pero..."
    deb "Pasa. Tú. Primero."
    mc "OK, OK."
    call BlinkXPS3 ("c22s007_030" , "d") from _call_BlinkXPS3_969
    mcp "(Creo que es la primera vez que entro en esta habitación desde que llegaron.)"
    mc "Hola de nuevo, [lis]. ¿Sabes de qué va esto?"
    stop music fadeout (1.5)
    lis "No sé de lo que estás hablando. ¿De qué va qué?"
    scene c22s007_030d with hpunch
    play sound ("music/DoorSlam.ogg")
    "*Blam*"
    play music ("music/Throne-King.ogg")
    deb "*A través de la puerta* Ya está. Ya podéis hablar."
    deb "*A través de la puerta* No pienso irme hasta que lo hagáis."
    mc "[deb.nick], ¿de qué va esto? ¿De qué tenemos que hablar?"
    call BlinkXPS3 ("c22s007_035" , "f") from _call_BlinkXPS3_970
    deb "Que te lo explique [lis]. Con todo lo que te gusta hablar, y con todo lo que le gusta a ella hablar de sí misma, sois incapaces de hablar de lo que importa."
    scene c22s007_040a with fade
    lis "¡[deb] Katherine Selden! ¡Abre esa puerta ahora mismo!"
    mc "[lis], ¿a qué se refiere?"
    call BlinkXPS3 ("c22s007_045" , "d") from _call_BlinkXPS3_971
    lis "¡A nada! ¡Se ha vuelto loca!"
    mc "No sé si loca, pero esto no es muy normal. Me siento como si me hubierais tendido una trampa de algún tipo. Y aún no sé por qué."
    lis "¡Yo estoy metida en la misma trampa que tú!"
    call BlinkXPS3 ("c22s007_050" , "f") from _call_BlinkXPS3_972
    deb "Llevas varios días diciendo que [mc] esto, [mc] lo otro..."
    if lis.rps < 0:
        deb "Aunque sea para decir que te cae mal."
    if deb._var("route"):
        deb "Parece que mi novio es tu tema favorito de conversación últimamente."
    else:
        deb "Parece que [mc] es tu tema favorito de conversación últimamente."
    deb "Si quieres decirle algo, díselo."
    call BlinkXPS3 ("c22s007_055" , "f") from _call_BlinkXPS3_973
    mc "[lis], ¿hay algo que me quieras decir?"
    if lis.rps < 0:
        mc "No sabía que te cayera mal..."
        lis "Empezamos con mal pie y aún no sé cómo tratarte. Pese a que nos has tratado bien... me desconciertas a veces."
    lis "Realmente no sé a lo que se refiere [deb.nick]..."
    if deb._var("route"):
        mc "¿Tiene algo que ver con que [deb.nick] y yo estemos saliendo?"
        scene c22s007_060a with vpunch
        lis "¿Qué? ¡No!"
        call BlinkXPS3 ("c22s007_065" , "f") from _call_BlinkXPS3_974
        deb "¡Mentirosa! Desde que nos besamos en el lago, cada vez hablas más de él."
        deb "¡Parece que estás celosa!"
        call BlinkXPS3 ("c22s007_070" , "f") from _call_BlinkXPS3_975
        mc "¿Es eso cierto, [lis]?"
        if lis.rps < 0:
            lis "Quizás he hablado más de ti con mi hermana, pero... es que me preocupa que le hagas daño. Aún no sé si puedo confiar en ti."
        else:
            lis "Quizás he hablado más de ti con mi hermana, pero... Sé que eres un buen tío y no le vas a hacer daño a propósito..."
            lis "Pero es mi hermana y... me preocupa..."
        if persistent.walkthrough:
            if lis.rps > -11:
                $ wt1 = "[gr][lis] + 15."
            else:
                $ wt1 = _("[gr][lis] + 15.\n[red] Tienes tantos puntos de relación negativos que no podrás abrir la ruta con [lis] independientemente de lo que elijas.")
            if lis.rps < 25:
                if lis.rps > -11:
                    $ wt2 = _("[red][lis] - 20.\n[red] ADVERTENCIA: No podrás abrir la ruta con [lis].")
                else:
                    $ wt2 = _("[red][lis] - 20.\n[red] Tienes tantos puntos negativos que no podrás abrir la ruta con [lis] independientemente de lo que elijas.")
            else:
                $ wt2 = _("[red][lis] - 20.")
        else:
            $ wt1 = ""
            $ wt2 = ""
        menu:
            "No le voy a hacer daño." (wt=wt1):
                $ lis.rp(+15)
                mc "Mi intención es hacerla feliz. Ya te dije que hacerle daño no entra en mis planes."
                mc "Es bueno que te preocupes por tu hermana, pero puedes confiar en mí. Al menos en esto."
                $ Aux = True
            "No te debo explicaciones sobre esto." (wt=wt2):
                $ lis.rp(-20)
                mc "Ya te dije que hacerle daño no entra en mis planes. Es todo lo que tienes que saber."
                $ Aux = False
        $ resetWalkthrough()
    else:
        if mc._var("relationships")>1:
            mc "Supongo que no tiene nada que ver con el harén, ¿no?"
        elif mc._var("relationships")==1:
            mc "Supongo que no tiene nada que ver con que salga con [gf], ¿no?"
        else:
            mc "Supongo que no tiene nada que ver con [ant], ¿no?"
        scene c22s007_060a with vpunch
        lis "¿Qué? ¡No!"
        call BlinkXPS3 ("c22s007_065" , "f") from _call_BlinkXPS3_976
        deb "¡Mentirosa!"
        if mc._var("relationships")>1:
            deb "Desde que te enteraste, no haces más que hablar de ello. Parece que quieras formar parte del harén."
        elif mc._var("relationships")==1:
            deb "Desde que te enteraste, no haces más que hablar de ellos. Parece que estás celosa."
        else:
            deb "Desde que te enteraste de lo de [ant], no haces más que hablar de [mc], como si quisieras llegar con él donde no llegaste con [ant]."
        call BlinkXPS3 ("c22s007_070" , "f") from _call_BlinkXPS3_977
        mc "¿Es eso cierto, [lis]?"
        if lis.rps < 0:
            lis "Quizás he hablado más de ti con mi hermana, pero... es que... todo es muy raro en esta familia. Y aún no confío en ti."
        else:
            lis "Quizás he hablado más de ti con mi hermana, pero... Sé que eres un buen tío... "
        if mc._var("relationships")>1:
            lis "Además, no soy nadie para pedir explicaciones sobre tu harén."
        elif mc._var("relationships")==1:
            lis "Además, me alegra que estés con [gf]. Por ella... Pero tengo dudas..."
            if sai._var("route"):
                lis "Después de vuestra relación en Portland..."
            else:
                lis "Después de la relación que tuviste con [sai]..."
        else:
            lis "No tiene nada que ver con [ant]. Además, no creo que sea nadie para preguntarte nada..."
        if persistent.walkthrough:
            if lis.rps > -11:
                $ wt1 = "[gr][lis] + 15."
            else:
                $ wt1 = _("[gr][lis] + 15.\n[red] Tienes tantos puntos de relación negativos que no podrás abrir la ruta con [lis] independientemente de lo que elijas.")
            if lis.rps < 25:
                if lis.rps > -11:
                    $ wt2 = _("[red][lis] - 20.\n[red] ADVERTENCIA: No podrás abrir la ruta con [lis].")
                else:
                    $ wt2 = _("[red][lis] - 20.\n[red] Tienes tantos puntos negativos que no podrás abrir la ruta con [lis] independientemente de lo que elijas.")
            else:
                $ wt2 = _("[red][lis] - 20.")
        else:
            $ wt1 = ""
            $ wt2 = ""
        menu:
            "Puedes preguntar lo que quieras, [lis]." (wt=wt1):
                $ lis.rp(+15)
                $ Aux = True
            "No te debo explicaciones sobre esto." (wt=wt2):
                $ lis.rp(-20)
                $ Aux = False
        $ resetWalkthrough()
    if lis.rps < 5:
        call BlinkXPS3 ("c22s007_075" , "d") from _call_BlinkXPS3_978
        if Aux:
            lis "Ahora que lo pienso, creo que sería un error meterme donde no me llaman."
        else:
            lis "Entonces no hay mucho más de lo que tengamos que hablar."
        lis "Abre la puerta, [deb.nick]. [mc] ya se va."
        scene black with dissolve
        "Vuelves a tu habitación sin decir una palabra, pese a la cara de sorpresa de [deb.nick] al abrir la puerta."
        stop music fadeout (1.5)
        "Tienes la impresión de que, de haber tratado a [lis] de forma diferente desde que llegó, vuestra relación podría ser diferente."
        return
    call BlinkXPS3 ("c22s007_080" , "d") from _call_BlinkXPS3_979
    lis "Lo sé. Sé que me estoy metiendo donde no me llaman..."
    mc "Pero ya habíamos hablado de esto. No entiendo a qué viene la encerrona de [deb.nick]."
    scene c22s007_085a with fade
    deb "A que no es de eso de lo que tenéis que hablar, par de idiotas."
    kat "¿Qué pasa, [deb.nick]?"
    kim "Te estamos oyendo desde nuestra habitación, ¿hay algún problema?"
    scene c22s007_090a with dissolve
    deb "No os preocupéis, he encerrado a [lis] con [mc]. Hasta que no se sincere con él, no van a salir."
    kat "Buena suerte con eso, tu hermana no es de las que habla de sus sentimientos."
    kat "*Susurrando* Por cierto, sabes que la puerta se abre hacia dentro, ¿no? Pueden salir cuando quieran."
    call BlinkXPS3 ("c22s007_095" , "f") from _call_BlinkXPS3_980
    mc "¿A qué se refiere, [lis]? ¿Sientes algo por mí?"
    call BlinkXPS3 ("c22s007_100" , "h") from _call_BlinkXPS3_981
    lis "Se refiere a que *Gritando* ¡HAY GENTE QUE SE METE DONDE NO LES LLAMAN!"
    _("[kat], [kim], y [deb.nick]") "*A través de la puerta* *Risa*"
    mc "No tenemos por qué hablarlo si no quieres. Tarde o temprano [deb.nick] se cansará nos tendrá que dejar salir."
    call BlinkXPS3 ("c22s007_105" , "d") from _call_BlinkXPS3_982
    lis "*Risa* Parece que aún no conoces a mi hermana. No te va a dejar salir hasta que yo no confiese que me gustas."
    deb "*A través de la puerta* ¡Por fin!"
    scene c22s007_110d with vpunch
    lis "{b}¿Que?{/b} ¡No quería decir eso!"
    call BlinkXPS3 ("c22s007_110" , "d") from _call_BlinkXPS3_983
    lis "Me refería a que... aunque me desconciertas... me pareces buena persona..."
    lis "No a que me gustes de esa forma..."
    if deb._var("route"):
        call BlinkXPS3 ("c22s007_115" , "d") from _call_BlinkXPS3_984
        lis "Nunca me podría gustar... el novio de mi hermana."
        lis "No le podría hacer eso..."
        deb "*A través de la puerta* Ya te he dicho que a mí no me importa. ¡[mc] y yo no tenemos una relación exclusiva!"
        $ Aux = False
        if dap._var("route") and eri._var("route"):
            $ Aux = True
        elif ama._var("route") and eva._var("route"):
            $ Aux = True
        elif ama._var("route") and emm._var("route"):
            $ Aux = True
        elif eri._var("route") and eva._var("route"):
            $ Aux = True
        elif dap._var("route") and eva._var("route"):
            $ Aux = True
        elif dap._var("route") and sca._var("route"):
            $ Aux = True
        elif mar._var("route") and nor._var("route") and persistent.family:
            $ Aux = True
        if Aux:
            deb "*A través de la puerta* ¡Además, no seríamos la primera pareja de hermanas con las que sale!"
        else:
            deb "*A través de la puerta* ¡Tan solo nos convertiría en la primera pareja de hermanas con las que sale!"
    mcp "([lis] miente fatal y está claro lo que está pasando aquí. ¿Pero qué quiero yo?)"
    stop music fadeout (1.5)
    if persistent.walkthrough:
        $ wt1 = _("[gr]Ruta con [lis] pre-abierta.\n[gr] [mc] actuará a su debido momento.")
        $ wt2 = _("[red]Ruta con [lis] cerrada.\n[red] ADVERTENCIA: No habrá más oportunidades de abrir la ruta.")
    else:
        $ wt1 = ""
        $ wt2 = ""
    menu:
        "(Estaría bien salir con [lis].)" (wt=wt1):
            $ lis._var("route", True)
            $ mc._var("relationships", 1, "add")
        "(No me interesa salir con [lis]. Pero tampoco quiero hacerle daño.)" (wt=wt2):
            $ lis._var("route", False)
    $ resetWalkthrough ()
    play music ("music/You-Know-Instrumental.ogg")
    if not lis._var("route"):
        mc "Bueno, entonces si yo no te gusto de esa forma, creo que [deb.nick] ha malinterpretado algo en vuestras conversaciones."
        call BlinkXPS3 ("c22s007_120" , "d") from _call_BlinkXPS3_985
        "Está a punto de decir algo, pero no dejas que te interrumpa."
        mc "Que ninguno de los dos nos gustemos de esa forma es una suerte. Así seguro que no hay malentendidos."
        mcp "(Y de esta forma, si realmente le gusto de esa forma, no se sentirá tan humillada o rechazada como si hubiera tenido que confesarlo.)"
        call BlinkXPS3 ("c22s007_125" , "d") from _call_BlinkXPS3_986
        lis "Sí, es una suerte... A veces mi hermana es idiota... Ella creía que tú..."
        mc "Que tú y yo podíamos hacer una buena pareja, pero creo que sólo veía dos amigos y lo ha malinterpretado."
        call BlinkXPS3 ("c22s007_130" , "d") from _call_BlinkXPS3_987
        lis "Gracias, [mc]. Por hacérselo ver."
        mc "No hay de qué, [lis]. Todo el mundo puede equivocarse..."
        scene c22s007_030d with dissolve
        mc "[deb.nick], ¿puedo salir ya? Creo que todo se ha aclarado ya."
        call BlinkXPS3 ("c22s007_135" , "d") from _call_BlinkXPS3_988
        deb "Sí, ya puedes salir."
        deb "Susurrando* Y gracias por como lo has llevado..."
        scene c22s007_135d with dissolve
        kat "Muy elegante tu forma de rechazarla."
        kim "Has evitado que se sintiera humillada. Eres un caballero."
        mc "No sé de qué estáis hablando. [deb.nick] ha malinterpretado una situación y se ha vuelto incómodo para [lis]."
        scene c22s007_135e with dissolve
        kat "Sí, sí. Malinterpretado."
        mc "Exacto, malinterpretado. Si alguno de los dos hubiera sentido algo que el otro no sentía, se podría haber sentido mal."
        mc "Por suerte {b}ninguno de los dos{/b} siente nada por el otro y tan solo somos amigos."
        kim "*Risa* Lo que he dicho. Un caballero. Gracias por portarte así con [lis]."
        scene c22s007_135f with dissolve
        kat "Sí, gracias. Me gustaría que cada vez que me rechacen lo hagan así."
        kim "Por suerte, [mc] {b}no ha tenido que rechazar a [lis]{/b}, ya que {b}ninguno de los dos{/b} siente nada por el otro y [deb.nick] se ha equivocado."
        kim "¿Lo entiendes, [kat]?"
        mc "Exacto. *Risa* Y ahora, si me lo permitís, voy a subir a mi habitación. Hasta mañana, chicas."
        scene c22s007_135h with dissolve
        kim "Hasta mañana, [mc]."
        kat "Te vemos mañana, [mc]."
        call c22s007_Lockdown from _call_c22s007_Lockdown
    else:
        mc "Bueno, si no te gusto de esa forma, no hay mucho que podamos hacer."
        call BlinkXPS3 ("c22s007_120" , "d") from _call_BlinkXPS3_989
        lis "Lo dices como si yo te gustara de esa forma..."
        mc "Sabiendo que tú no sientes nada por mí, aunque yo lo sintiera, no te lo podría decir."
        mc "El resultado es que tú estarías incómoda o yo acabaría humillado y rechazado. Con lo que mejor no hacerlo."
        call BlinkXPS3 ("c22s007_125" , "d") from _call_BlinkXPS3_990
        lis "Sí, mejor no hacerlo..."
        scene c22s007_140a with fade
        deb "¡Sois idiotas los dos!"
        kat "¿Tan difícil les es decir que los dos se gustan?"
        kim "Para [lis] es difícil, y ha empezado negándolo. Contradecirse ahora es más difícil todavía."
        call BlinkXPS3 ("c22s007_145" , "f") from _call_BlinkXPS3_991
        lis "¡Y más aún con público, joder!"
        mc "*Risa* Creo que es la primera vez que te oigo decir un taco."
        call BlinkXPS3 ("c22s007_150" , "d") from _call_BlinkXPS3_992
        lis "Es que me sacan de mis casillas... no es así como había pensado que pasaría..."
        if deb._var("route"):
            lis "Antes de que empezaras a salir con [deb.nick], claro..."
        mc "Cómo habías pensado que pasaría... ¿qué, exactamente?"
        call BlinkXPS3 ("c22s007_155" , "d") from _call_BlinkXPS3_993
        lis "Nada, una estupidez..."
        mc "OK, dado que no te gusto... de esa forma... habías pensado que en algún momento te pediría una cita o algo así y en como rechazarme, ¿no?"
        mc "Lo querías hacer de tal forma que yo no me sintiera humillado porque, a pesar de la imagen que das a veces, eres una buena chica."
        mc "Y con ese peinado, incluso parece que el palo por el culo que [kat] decía que tenías ha desaparecido."
        call BlinkXPS3 ("c22s007_160" , "d") from _call_BlinkXPS3_994
        lis "¡[mc]!" (multiple=2)
        kat "*A través de la puerta* ¡[mc]!" (multiple=2)
        mc "¡Hey! Me gusta más esta nueva versión de ti, pero déjame seguir. Estoy intentando atar cabos."
        mc "Como ahora tenemos público, tu plan de hacerlo en privado para que yo no me sintiera mal ha desaparecido."
        mc "Porque desde que [deb.nick] me ha metido en la habitación, crees que voy a pedirte esa cita o algo así, ¿no?"
        call BlinkXPS3 ("c22s007_165" , "d") from _call_BlinkXPS3_995
        lis "No. No es eso. [deb.nick] te ha metido en la habitación para que {b}yo{/b} te pida una cita o algo así."
        mc "¿Por qué ibas a hacerlo? No te gusto de esa forma..."
        scene c22s007_165d with dissolve
        lis "Porque mi hermana es idiota. Cree que tú me gustas de esa forma... y que... si me gustaras... yo sería lo suficientemente valiente como para hacerlo."
        lis "Lo suficientemente valiente como para decírtelo."
        mc "¿Y es verdad?"
        lis "No."
        mc "¿Lo de que no eres lo suficientemente valiente para decírmelo o lo de que no eres lo suficientemente valiente para pedirme esa cita?"
        lis "Ninguna de las dos cosas..."
        scene c22s007_165e with vpunch
        lis "¡Oh!"
        mc "[lis], ¿puedes mirarme un momento?"
        scene c22s007_140b with fade
        kim "¿Oyes algo, [deb.nick]? Llevan un minuto en silencio..."
        deb "Callad, no oigo nada..."
        kat "Lo ha matado y está descuartizando el cadáver con las tijeras de manualidades, seguro."
        deb "*Susurrando* Voy a abrir un poco la puerta..."
        scene c22s007_140c with dissolve
        deb "¡Oh!"
        scene c22s007_140d with dissolve
        deb "Chicas, nada que ver aquí. Voy a ir a la piscina un rato. Me he dejado un libro allí."
        kim "¿Se están besando? ¡Qué romántico!"
        kat "Lo matará en la noche de bodas. *Risa*"
        deb "Hasta luego, chicas."
        call c22s007_Lockdown from _call_c22s007_Lockdown_1
        stop music fadeout (1.5)
        call BlinkXPS3 ("c22s007_170" , "f") from _call_BlinkXPS3_996
        "Tras varios minutos ininterrumpidos de besos..."
        play music ("music/TheBritons.ogg")
        lis "¿Por qué me has besado?"
        mc "*Risa* Que me preguntes eso después de diez minutos devolviéndome el beso me desconcierta..."
        mc "Por cierto, besas mejor de lo que esperaba."
        call BlinkXPS3 ("c22s007_175" , "d") from _call_BlinkXPS3_997
        lis "¿Qué? ¿Esperabas que besara mal?"
        mc "No, pero no esperaba que besaras {b}tan{/b} bien."
        call BlinkXPS3 ("c22s007_180" , "d") from _call_BlinkXPS3_998
        lis "¿Cómo nos deja este beso?"
        mc "A mí me ha dejado contento. *Risa* Y con ganas de más."
        call BlinkXPS3 ("c22s007_185" , "d") from _call_BlinkXPS3_999
        lis "Pero... ¿significa que estamos saliendo juntos? ¿Que soy tu...?"
        mc "¡No digas esa palabra! *Risa* Significa que los dos hemos querido besarnos. Y que si quieres que seamos algo más que amigos, habrá más besos."
        call BlinkXPS3 ("c22s007_190" , "d") from _call_BlinkXPS3_1000
        lis "No sé qué responder a eso... pero sí cómo responder."
        scene c22s007_140e with dissolve
        "La boca de [lis] dice lo que sus palabras no pueden."
        "La princesa se pasa los siguientes minutos hablando en silencio."
        "Usa sus labios para dibujar el contorno de tu boca mientras su lengua empieza una larga amistad con la tuya."
        "Ahora es tu princesa."
        scene black with dissolve
        "Pasan varios minutos antes de que vuelvas a tu habitación con una sonrisa en la cara."
        "No ha habido ninguna palabra. No había nada que decir."
    stop music fadeout (1.5)
    return
label c22s007_Lockdown:
    scene c22s007_135g with fade
    kat "*Susurrando* ¿Quieres que le pida a [deb.nick] que os encierre en una habitación a vosotros también?"
    kim "*Susurrando* ¡[kat]! Aún tengo que hablar con [mar]... No sé ni por donde empezar esa conversación..."
    kat "*Susurrando* Le puedo decir a [deb.nick] que te encierre con [mar] en la cocina. *Risa* Pero que sea después de desayunar..."
    return
label c22s008_NoSca:
    "Te desnudas y te metes en la cama. Ha sido un día largo y estás cansado."
    if lis._var("route"):
        call c22s008_GroupMessages from _call_c22s008_GroupMessages
    scene black with dissolve
    "Después de reírte un rato por la confusión, te quedas dormido en seguida."
    return
label c22s008_GroupMessages:
    "Antes de que te entre sueño, suena tu móvil. Es un mensaje en el grupo."
    scene c22s008_005a with dissolve
    play music ("music/SadSummer.ogg")
    play sound ("music/notification.ogg")
    lis "¡Chicas! ¡[mc] y yo estamos saliendo juntos! O eso creo... (o_O)?"
    mcp "(¿Chicas? ¿No es consciente de que lo ha mandado al grupo en el que también estoy yo?)"
    "Empiezan a llegar mensajes de felicitación. Parece que nadie se ha dado cuenta."
    play sound ("music/notification.ogg")
    deb "Ahora vuelvo a la habitación y me lo explicas todo."
    play sound ("music/notification.ogg")
    kim "¿Ya se ha ido?"
    play sound ("music/notification.ogg")
    kat "¿Eyaculador precoz?"
    play sound ("music/notification.ogg")
    jam "O impotente. :D"
    "Varias chicas se ríen."
    play sound ("music/notification.ogg")
    sai "Os puedo asegurar que no lo es. ^^"
    if not sai._var("route"):
        play sound ("music/notification.ogg")
        sai "O no lo era hace dos meses."
    play sound ("music/notification.ogg")
    mar "¿Qué es eso de que solo lo crees, [lis]?"
    play sound ("music/notification.ogg")
    lis "No sé... no lo hemos hablado."
    play sound ("music/notification.ogg")
    lis "Tan solo nos hemos besado."
    play sound ("music/notification.ogg")
    lis "Mucho."
    if deb._var("route"):
        play sound ("music/notification.ogg")
        bet "¿Qué se siente al compartir chico con tu hermana?"
        play sound ("music/notification.ogg")
        deb "He sido yo quién ha forzado la situación. (✿◠‿◠)"
        play sound ("music/notification.ogg")
        deb "Estoy contenta con que lo hayan aclarado."
    play sound ("music/notification.ogg")
    dap "Acabo de salir de la ducha."
    play sound ("music/notification.ogg")
    dap "Felicidades, [lis]."
    play sound ("music/notification.ogg")
    dap "¡Mierda! [lis], lo has mandado al grupo en el que está [mc]."
    play sound ("music/notification.ogg")
    nor "¡Borrad todos los mensajes!"
    play sound ("music/notification.ogg")
    mee "Con un poco de suerte está durmiendo y no los ha visto."
    play sound ("music/notification.ogg")
    kia "¡Pero no sigáis escribiendo!"
    play sound ("music/notification.ogg")
    eil "Mamá, acabas de escribir para decirnos que no escribamos."
    play sound ("music/notification.ogg")
    eil "¿Te das cuenta de la ironía? XD"
    play sound ("music/notification.ogg")
    jam "Alguien habla de [mc] y perdéis el mundo de vista, chicas."
    play sound ("music/notification.ogg")
    jam "Si fuera guapo y estuviese en una silla de ruedas lo entendería, pero es [mc]. ;)"
    "Varias se ríen. Los mensajes van desapareciendo."
    play sound ("music/notification.ogg")
    meg "Has dicho guapo, con lo que supongo que no te refieres a ti mismo. XD"
    "Todas se ríen."
    play sound ("music/notification.ogg")
    jam "Te espero en el otro grupo, [meg]. Has cavado tu propia tumba. :D"
    play sound ("music/notification.ogg")
    eri "Chicas, borrad todo y pasemos al otro grupo."
    "No llegan más mensajes."
    "Dudas si hacerles saber que los has leído."
    return
label c22s008_Sca:
    if _in_replay:
        call mrS3_rename from _call_mrS3_rename_26
        call mrS3_edmund_story from _call_mrS3_edmund_story
        call mrS3_sca_route from _call_mrS3_sca_route_1
        call mrS3_lis_route from _call_mrS3_lis_route
        if lis._var("route"):
            call mrS3_sai_route from _call_mrS3_sai_route_2
            call mrS3_deb_route from _call_mrS3_deb_route_2
    call changenicks from _call_changenicks_7
    "Te desnudas y te metes en la cama. Después de todas las emociones del día, especialmente lo de [sca], necesitas una noche de descanso."
    if lis._var("route"):
        call c22s008_GroupMessages from _call_c22s008_GroupMessages_1
    scene c22s008_005b with dissolve
    play sound ("music/knock.ogg")
    "*Knock-Knock*"
    play music ("music/pianomatic.ogg")
    sca "*A través de la puerta* *Susurrando* ¿Estás despierto, [mc]?"
    mc "Sí, pasa."
    call BlinkXPS3 ("c22s008_010" , "d") from _call_BlinkXPS3_1001
    sca "¿Ibas a dormir ya? Puedo volver en otro momento."
    mc "No, no te preocupes, dime."
    call BlinkXPS3 ("c22s008_015" , "d") from _call_BlinkXPS3_1002
    sca "Me preguntaba si me dejarías dormir contigo."
    if sca._var("route"):
        sca "Solo dormir."
        mc "¿Solo dormir?"
    call BlinkXPS3 ("c22s008_020" , "d") from _call_BlinkXPS3_1003
    if mc._var("edmundsStory"):
        if persistent.family:
            sca "Después de lo emocionante que ha sido esta tarde, quiero dormir con mi hermano."
            sca "Siempre he querido tener una hermana con quien dormir. Cosas de hija única, supongo..."
            call BlinkXPS3 ("c22s008_025" , "d") from _call_BlinkXPS3_1004
            sca "No se lo digas a [emm], pero prefiero dormir contigo. No lo hubiera descubierto sin ti."
        else:
            sca "Después de la decepción de esta tarde, ha venido el bonito gesto de [dap.nick] y del resto de chicas."
            sca "Pero siempre he querido tener una hermana con quien dormir. Cosas de hija única, supongo..."
            call BlinkXPS3 ("c22s008_030" , "d") from _call_BlinkXPS3_1005
            sca "Y resulta que llevo días durmiendo con mi nueva hermana."
            sca "Si hubiera salido positivo, posiblemente estaría en la habitación de [emm] ahora mismo."
            call BlinkXPS3 ("c22s008_035" , "d") from _call_BlinkXPS3_1006
            sca "Pero estaba tan segura de que el test saldría positivo que ya había planeado dormir contigo también."
            if sca._var("route"):
                sca "Solo dormir."
    if not mc._var("edmundsStory") or sca._var("route"):
        sca "El día que viniste a casa de mi madre te tuve que echar. Pero me quedé con ganas de dormir contigo."
        sca "He pensado que podríamos continuar donde lo dejamos aquel día. En dormir juntos por primera vez."
    if sca._var("route"):
        mc "Por supuesto. Estoy desnudo bajo las sábanas. ¿Te importa?"
        call BlinkXPS3 ("c22s008_040" , "d") from _call_BlinkXPS3_1007
        sca "*Risa* No te preocupes. Creo que podré resistir la tentación."
        sca "Yo no me quitaré el pijama para no tentarte. *Risa*"
    else:
        mc "Dame un momento para ponerme algo. Estoy desnudo bajo las sábanas."
        scene c22s008_040d with dissolve
        sca "No te preocupes. No voy a mirar."
    call BlinkXPS3 ("c22s008_045" , "f") from _call_BlinkXPS3_1008
    mc "¿Estás bien?"
    "Hablas un poco más alto de lo habitual porque [sca] se ha quitado el audífono para dormir."
    sca "Genial, no te preocupes por mí."
    if sca._var("route"):
        call BlinkXPS3 ("c22s008_050" , "d") from _call_BlinkXPS3_1009
        sca "Desde la última lección que no había venido aquí. Fue el día que llegaron [lis], [deb.nick], [kim], y [kat]."
        mc "Ha pasado mucho tiempo y las cosas han cambiado mucho. Tú y yo aún no estábamos saliendo cuando entraste por la puerta."
        call BlinkXPS3 ("c22s008_055" , "d") from _call_BlinkXPS3_1010
        sca "Pero sí cuando salí. Pese a mi metedura de pata aquel día, lo recuerdo como un día feliz."
        sca "He tenido un montón de días felices últimamente. No recuerdo tantos buenos días seguidos en toda mi vida."
    mc "Me alegra mucho que estés aquí, que formes parte de la familia."
    if mc._var("edmundsStory"):
        if not persistent.family:
            call BlinkXPS3 ("c22s008_060" , "d") from _call_BlinkXPS3_1011
            sca "Aunque no compartamos padre..."
            mc "Como ha dicho [dap], si por los genes fuera, nadie sería parte de esta familia."
            mc "Tampoco comparto padres con [emm], y no por ello es menos mi hermana."
            call BlinkXPS3 ("c22s008_065" , "d") from _call_BlinkXPS3_1012
            sca "Tienes razón. Decidimos ser una familia. Y lo somos."
            sca "Al final sí que voy a dormir con mi hermano."
            mc "Esa es la actitud, cariño. Siempre me tendrás aquí."
        else:
            call BlinkXPS3 ("c22s008_060" , "d") from _call_BlinkXPS3_1013
            sca "No me puedo imaginar qué hubiera pasado si hubiera salido negativo."
            mc "Que formarías parte de esta familia igual. No comparto padres con [jam] y es mi hermano."
            call BlinkXPS3 ("c22s008_065" , "d") from _call_BlinkXPS3_1014
            sca "Tienes razón. Seríamos familia por elección."
            sca "Pero por alguna razón, me conforta saber que voy a dormir con mi hermano."
            mc "Siempre me tendrás aquí, cariño."
    call BlinkXPS3 ("c22s008_070" , "d") from _call_BlinkXPS3_1015
    sca "Pero como me vuelvas a comparar con un perro callejero, me convertiré en una hermana insoportable. *Risa*"
    mc "*Risa* ¿Te lo ha dicho? ¿Dónde queda el secreto de confesión de los católicos?"
    sca "*Risa* Creo que eso solo funciona con los curas, no con las monjas."
    scene c22s008_070d with fade
    "Pasáis un rato charlando antes de apagar las luces. Dormís plácidamente toda la noche en los brazos del otro."
    "Es una gran sensación dormir con una mujer a la que quieres como si fuera tu hermana."
    if mc._var("edmundsStory"):
        "Porque lo es."
        if not persistent.family:
            "Aunque un estúpido test de ADN diga lo contrario."
            "No vas a dejar que un maldito papel le quite la ilusión."
    if not mc._var("edmundsStory"):
        "O al menos la prima en quien [dap] la ha convertido."
    stop music fadeout (1.5)
    scene black with dissolve
    return



label c22s010_eoc:
    scene neweoc with fade
    python:
        _skipping = False
    pause (1.0)
    python:
        _skipping = True
    "{b}Esto es todo por esta versión. Por favor, graba aquí y nos vemos en la próxima actualización de My Dorm. Gracias por jugar y por tu apoyo. Espero que hayas disfrutado del juego.{/b}"
    pause (5.0)
    return

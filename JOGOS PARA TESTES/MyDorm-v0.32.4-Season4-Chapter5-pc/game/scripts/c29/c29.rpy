label c29:
    if mar._var("route"):
        $ mar._var("engaged", True)
    if kia._var("route"):
        $ kia._var("engaged", True)
    if mad._var("route"):
        $ mad._var("engaged", True)
    if sim._var("route"):
        $ sim._var("engaged", True)
    if "olg" not in globals () or not isinstance (olg, TGCharacter):
        $ olg      = TGCharacter ("Olga", color="#65f3ff")
    if lis._var("route"):
        call c29s001_LisParty from _call_c29s001_LisParty
        call c29s002_LisLewd from _call_c29s002_LisLewd
    else:
        call c29s001_noLis from _call_c29s001_noLis
    #Day change Friday
    call c29s003_KatKiss from _call_c29s003_KatKiss
    if kim._var("route"):
        call c29s003_KimPicnic from _call_c29s003_KimPicnic
    call c29s004_BetMeeCall from _call_c29s004_BetMeeCall
    call c29s004_SamMegMarTattoo from _call_c29s004_SamMegMarTattoo
    call c29s006_KiaSim from _call_c29s006_KiaSim
    if eri._var("route"):
        call c29s005_EriLewd from _call_c29s005_EriLewd
        if nor._var("route"):
            call c29s005_NorLewd from _call_c29s005_NorLewd
        else:
            call c29s005_noNorLewd from _call_c29s005_noNorLewd
    else:
        call c29s005_noEriLewd from _call_c29s005_noEriLewd
    #Day Change Saturday
    call c29s006_AmaEmm from _call_c29s006_AmaEmm
    call c29s006_DebEil from _call_c29s006_DebSim
    call c29s006_SaiEvaMad from _call_c29s006_SaiEvaMad
    call c29s007_OmaLis from _call_c29s007_OmaLis #charlan sobre la "detención"
    call c29s007_DapDebSca from _call_c29s007_DapDebSca #charlan sobre juegos
    if kia._var("route"):
        call c29s007_KiaWatersports from _call_c29s007_KiaWatersports
    if sca._var("route") and dap._var("route"):
        call c29s009_ScaDapTeaser from _call_c29s009_ScaDapTeaser
    return
    call eoc from _call_eoc
    return
label c29s001_LisParty:
    if _in_replay:
        $ mc._var("relationships", 0, "set")
        call mrS3_deb_route from _call_mrS3_deb_route_24
        call mrS3_rels from _call_mrS3_rels_36
    scene c29s001_005a with dissolve
    play music ("music/1000lichter.ogg")
    "Al llegar a Los Angeles, hay una limusina enviada por la amiga de [lis] esperándoos."
    "Casi podrías acostumbrarte a este tipo de servicio, aunque lo consideras excesivo."
    "Nunca habías subido a un helicóptero y llevas varios viajes en la última semana. Y lo de las limusinas... Con un Under habría habido suficiente."
    "Empiezas a pensar que el ecologista eres tú en vez de [lis]."
    call BlinkXS4("c29s001_010") from _call_BlinkXS4_419
    "Una vez dentro del coche..."
    mc "Sabía que faltaba algo. Me extrañaba que no llevaras pendientes."
    lis "Nunca te pongas unos pendientes grandes si vas a usar los auriculares de un helicóptero. Es fácil que se enreden."
    mc "*Risa* No me pondré pendientes en ese caso. O en ninguno."
    call BlinkXS4("c29s001_015") from _call_BlinkXS4_420
    lis "*Risa* Los chicos lo tenéis mucho más fácil. Casi no os despeináis. A veces os envidio."
    mc "*Risa* Eso sería como si yo envidiara a los hombres calvos porque ellos no pueden despeinarse."
    mc "A veces echo de menos el pelo largo que llevaba cuando volví de Portland. Después me doy cuenta de lo cómodo que es esto y se me pasa."
    call BlinkXS4("c29s001_020") from _call_BlinkXS4_421
    lis "¿Llevabas el pelo largo? No puedo imaginarte con el pelo largo."
    mc "¿No te ha enseñado [sai] ninguna foto de cuando estábamos en Portland?"
    call BlinkXS4("c29s001_025") from _call_BlinkXS4_422
    lis "Sí, pero deben ser más antiguas, porque llevabas el pelo como ahora y ella lo llevaba un poco más largo que yo."
    mc "Sí, esas son del principio de 'salir juntos'. Los últimos meses fueron una locura y no visité una peluquería... creo que desde antes de Navidad."
    mc "Cuando volví a casa fue una de las primeras cosas que hice. [nor] se reía de mí diciendo que parecía un bárbaro."
    mc "Lo llevaba un poco más corto de lo que lo llevas tú, pero no mucho más corto."
    call BlinkXS4("c29s001_030") from _call_BlinkXS4_423
    lis "Les preguntaré a las chicas si tienen fotos tuyas con el pelo largo. Conociéndote, estoy casi segura de que no te haces selfies."
    mc "*Risa* ¿Quieres apostar?"
    call BlinkXS4("c29s001_020") from _call_BlinkXS4_424
    lis "¿Qué? ¿Te haces selfies? Eres una de las pocas personas de las que nunca lo habría dicho..."
    mc "*Risa* No."
    call BlinkXS4("c29s001_035") from _call_BlinkXS4_425
    lis "*Risa* Idiota."
    mc "*Risa* Yo también te quiero."
    stop music fadeout (1.5)
    scene c29s001_040a with fade
    call BlinkXS4("c29s001_040") from _call_BlinkXS4_426
    "Al cabo de unos minutos llegáis al piso de la amiga de [lis]. El ascensor os deja en un pasillo que lleva al salón."
    if "sid" not in globals () or not isinstance (sid, TGCharacter):
        $ sid      = TGCharacter ("Sidney Todd", color="#25f3ff")
    if "jen" not in globals () or not isinstance (jen, TGCharacter):
        $ jen      = TGCharacter ("Jenny Thursday", color="#f5f3ff")
    if "hal" not in globals () or not isinstance (hal, TGCharacter):
        $ hal      = TGCharacter ("Halley Strawberry", color="#a5f3ff")
    if "ska" not in globals () or not isinstance (ska, TGCharacter):
        $ ska      = TGCharacter ("Scarlett Johnson", color="#35f3ff")
    if "tay" not in globals () or not isinstance (tay, TGCharacter):
        $ tay      = TGCharacter ("Taylor Shift", color="#15f3ff")
    play music ("music/Africa.ogg")
    lis "Vamos a buscar a Sidney. Quiero que la conozcas, aunque seguro que la has visto en alguna de sus series o películas. Lo petó en 'Eufórica'"
    mc "Espera. ¿Es esa Sidney? ¿Sidney Todd?"
    call BlinkXS4("c29s001_045") from _call_BlinkXS4_427
    lis "Sí. ¿No te lo había dicho? ¿Te gusta esa serie?"
    mc "No tuve tiempo de seguirla demasiado. Creo que vi uno o dos episodios donde todos los personajes me caían mal."
    call BlinkXS4("c29s001_050") from _call_BlinkXS4_428
    lis "*Risa* No se lo digas a Sidney. La han nominado a un Globo de Plata por ese papel."
    lis "Vamos a buscarla."
    scene c29s001_055a with fade
    lis "¡SIDNEY!"
    sid "¡[lis!u]! ¡Has llegado!"
    scene c29s001_055b with dissolve
    lis "Gracias por mandarnos el coche, Sid."
    sid "*Risa* Deja de crecer o al final vas a tener que pedirle ropa prestada a [deb]."
    lis "Ven. Quiero presentarte a alguien."
    scene c29s001_055c with dissolve
    lis "Sid, éste es [mc]. Mi novio."
    mc "Encantado de conocerte, Sidney."
    sid "Igualmente, [mc]. ¿Así que por fin alguien le ha echado el lazo a nuestra [lis]?"
    mc "*Risa* Eso parece."
    scene c29s001_055d with dissolve
    lis "*Risa* O a lo mejor he sido yo quién le ha echado el lazo a él."
    sid "*Risa* Entonces se puede considerar que está entre los hombres más afortunados del mundo, si te has interesado por él."
    mc "*Risa* Creo que te equivocas. No me considero entre los hombres más afortunados del mundo. Estoy en la cima de los hombres más afortunados."
    scene c29s001_055e with dissolve
    lis "*Risa* ¿Entiendes ahora por qué estoy con él?"
    sid "La verdad es que no es una respuesta que me esperara. *Risa* Pero si siempre es así, consérvalo cerca."
    mc "*Risa* Eso espero."
    scene c29s001_055f with dissolve
    lis "¡Oh! ¡Acabo de ver a Jenny! ¿Ha venido disfrazada?"
    sid "No. O puede que sí... Ha venido directamente de una sesión de fotos para su nueva serie."
    scene c29s001_055g with dissolve
    lis "Cuida de [mc] un rato, Sid. Voy a saludar a Jenny y la traigo para que la conozca."
    lis "*Risa* Que no se acerque ninguna pelandrusca a mi novio."
    sid "No te preocupes. *Risa* Defenderé su honor con mis garras."
    call KissXS4("c29s001_060") from _call_KissXS4_5
    call BlinkXS4("c29s001_060") from _call_BlinkXS4_429
    lis "Espérame aquí con Sidney. Vuelvo en un minuto."
    mc "No te preocupes. *Risa* Intentaré no aburrirla."
    scene c29s001_065a with fade
    call BlinkXS4("c29s001_065") from _call_BlinkXS4_430
    "Te acercas al bar con Sidney. Siempre te ha parecido estúpido cuando veías un bar completo en las películas sobre mansiones. Es la primera vez que lo ves fuera de la tele."
    sid "Así que tú eres el chico de [lis]. Cuando me escribió para decirme que vendría con alguien casi no me lo podía creer."
    if mc._var("relationships")>1:
        mcp "(No tengo ni idea de qué sabe sobre nosotros, la familia o el harén... Será mejor no dar ninguna información relevante.)"
    else:
        mcp "(No tengo ni idea de qué sabe sobre nosotros o la familia... Será mejor no dar ninguna información relevante.)"
    mc "Creo que si nos lo hubieran dicho a cualquiera de nosotros hace menos de un mes tampoco nos lo hubiéramos creído."
    call BlinkXS4("c29s001_070") from _call_BlinkXS4_431
    sid "¿Hace mucho que tú y ella os conocéis?"
    mc "*Risa* Menos de un mes."
    call BlinkXS4("c29s001_075") from _call_BlinkXS4_432
    sid "*Risa* Veo que tienes sentido del humor. Lo vas a necesitar con [lis]."
    sid "A veces necesita a alguien que le pare los pies cuando se emociona mucho con algo. Y siempre es mejor hacerlo con sentido del humor."
    mc "No te preocupes por eso. Mi función no es frenarle, sino acompañarla y animarla para que llegue a la meta que se ha marcado."
    mc "Por cierto, me gusta tu piso."
    call BlinkXS4("c29s001_085") from _call_BlinkXS4_433
    sid "Gracias. Es muy chulo, pero esta es precisamente la fiesta de despedida de este piso."
    mc "¿Dejas el piso? Es una pasada de sitio, y [lis] me ha dicho que tienes piscina arriba."
    sid "El sitio me gusta, pero es de alquiler. Pertenece a un productor británico y la distribución no es la mejor. El bar ocupa demasiado sitio y no lo puedo quitar."
    call BlinkXS4("c29s001_080") from _call_BlinkXS4_434
    sid "Este piso está pensado para dar fiestas más que para vivir. Me compré una casa el año pasado y, ahora que las reformas están acabadas, me mudaré ahí."
    sid "Ya me he llevado muchas cosas y ahora este piso me da la sensación de... vacío. La casa nueva es mucho más tranquila que este sitio, y más apartada."
    mc "El precio de la fama, supongo. Algo con lo que espero no tener que lidiar nunca."
    call BlinkXS4("c29s001_090") from _call_BlinkXS4_435
    sid "Tiene sus partes buenas y sus partes malas. Aunque hay más partes buenas que malas."
    mc "Me lo imagino. Si no, la gente huiría de la fama."
    mc "Por cierto, creía que habría más gente. [lis] habló de 60 o 70 personas."
    call BlinkXS4("c29s001_095a") from _call_BlinkXS4_436
    sid "Hay 80 personas invitadas, pero no vendrán todas ni coincidirán a la vez aquí. La gente va y viene, pero menos de la mitad estarán durante toda la fiesta."
    sid "Además, arriba en la azotea y en la piscina hay mucha gente ahora mismo. Hace buena noche y la gente quiere aprovechar y estar al aire libre."
    mc "Tienes razón, no había pensado que hubiera mucha gente en la piscina a estas horas."
    call BlinkXS4("c29s001_095b") from _call_BlinkXS4_437
    sid "Por cierto, ¿a qué te dedicas, [mc]? [lis] no me ha dicho nada sobre ti excepto que existes."
    mc "Mi familia tiene una empresa de alojamiento para universitarias. La hemos fundado este año."
    mc "*Risa* [lis] diría que soy el botones, pero soy el director financiero, entre otras cosas."
    call BlinkXS4("c29s001_095c") from _call_BlinkXS4_438
    sid "¡Oh, que interesante! ¿Es ahí donde conociste a [lis]?"
    sid "Hace un par de meses me dijo que se mudaría a un pueblo de la costa a estudiar. Según ella, 'como una chica normal'."
    sid "Supongo que su familia podría comprar la universidad entera, o como mínimo una mansión donde vivir mientras estudia."
    mc "Sí, [lis] se aloja en la residencia. Es la casa donde he vivido casi toda mi vida."
    mc "El ambiente es muy... familiar. Mi hermana y mi madre también viven ahí, y mi tía y mis primas en la casa de al lado, que también pertenece a la residencia."
    if not persistent.family:
        mc "(*Risa mental* Si te tuviera que explicar que no estamos relacionados, seguramente te explotaría la cabeza y acabaría la fiesta.)"
    call BlinkXS4("c29s001_100") from _call_BlinkXS4_439
    sid "Mmmm... Al decir una empresa de alojamiento, creía que tendríais varios edificios en diversas universidades."
    mc "Todo llegará. Como te he dicho, hemos empezado este año."
    call BlinkXS4("c29s001_105") from _call_BlinkXS4_440
    sid "¡Oh, no me malinterpretes! No soy de las personas que juzgan a otras por el tamaño de su cuenta bancaria."
    sid "Aquí en Hollywood todo parece moverse por el dinero y la fama, pero yo me crie en el Idaho rural."
    mc "No te estaba malinterpretando, no te preocupes. Tan solo aclaraba ese punto. No quiero parecer un tipo que tiene un hotel y dice que tiene una cadena."
    mc "Para nosotros ahora mismo es más importante que las chicas se sientan bien que cualquier otra cosa. Es a lo que me refería con ambiente familiar."
    scene c29s001_110d with dissolve
    pause (1.2)
    call BlinkXS4("c29s001_110") from _call_BlinkXS4_441
    sid "Mira, por ahí vuelve [lis] con Jenny. Voy a dejarte; tengo más invitados a los que debo atender."
    mc "No te preocupes. Encantado de conocerte."
    stop music fadeout (1.5)
    sid "Igualmente. Pasáoslo bien."
    scene c29s001_115a with fade
    play music ("music/Between-Heaven-And-Earth.ogg")
    lis "¿Ya se ha ido Sid? ¿Te ha dejado solo?"
    mc "Se acaba de ir. Ha esperado a ver que ya volvías."
    lis "Bueno, te presento a Jenny. Este es [mc], mi novio."
    mc "Encantado de conocerte, Jenny."
    jen "Lo mismo digo, [mc]."
    if deb._var("route"):
        jen "Veo que a nuestras altísimas amigas les ha sentado bien venir a California. No llevan un mes aquí y ya están las dos emparejadas."
        scene c29s001_115An with dissolve
        "Entiendes por el gesto de [lis] que Jenny no sabe que las dos están emparejadas contigo."
        mc "Cada una de ellas ha encontrado un tipo afortunado."
        scene c29s001_115e with dissolve
        lis "Aún no estoy segura de quién es más afortunado. Si nosotras o nuestro novio... Nuestros novios..."
    else:
        jen "Veo que a nuestra altísima amiga le ha sentado bien venir a California. No lleva un mes aquí y ya está emparejada."
        mc "[lis] ha encontrado a un tipo afortunado."
        scene c29s001_115e with dissolve
        lis "Aún no estoy segura de quién es más afortunado. Si él o yo."
    jen "*Risa* ¡Qué bonita es una relación cuando empieza!"
    mc "*Risa* Espero no poder compararla nunca con cómo es cuando acaba."
    scene c29s001_115f with dissolve
    jen "*Risa* Chica, mantén a este hombre cerca. Parece que él no tiene intención de dejarte escapar."
    lis "*Risita* Ya ha visto una de las peores partes de mí y eso no le ha asustado, con lo que..."
    jen "¿Una de tus peores partes? *Risa* ¿Cuál? ¡Tienes muchísimas!"
    lis "*Risa* Eres una perra mala, Jenny."
    mc "*Risa* ¿De verdad tienes partes malas, [lis]?"
    scene c29s001_115g with dissolve
    jen "Chicos, me alegro de haberos visto, pero he quedado con Saoirse arriba en la piscina y se estará preguntando dónde estoy."
    lis "¿Saoirse ha venido? ¡No sabía que iba a venir!"
    jen "Suspendieron el rodaje porque uno de los actores se ha roto una mano. ¿Por qué no vienes? Seguro que se alegra de verte."
    call BlinkXS4("c29s001_120") from _call_BlinkXS4_442
    lis "No quiero dejarte solo otra vez... ¿Subes a la piscina con nosotras?"
    mc "No te preocupes. Ve a saludar a tus amigas y te espero aquí, en la barra. Empiezo a tener algo de sed."
    call BlinkXS4("c29s001_130") from _call_BlinkXS4_443
    mc "Encantado de conocerte, Jenny."
    jen "Igualmente, [mc]. Siento robarte a tu novia, pero solo será un rato."
    mc "No te preocupes por eso."
    call KissXS4("c29s001_125") from _call_KissXS4_6
    call BlinkXS4("c29s001_125") from _call_BlinkXS4_444
    lis "¡Eres el mejor novio del mundo!"
    mc "*Risa* Y estaré aquí mismo, en la barra esperando a la mejor novia del mundo. Bueno, mejor aún en ese rincón."
    stop music fadeout (1.5)
    scene c29s001_130d with fade
    "Te diriges al camarero y pides un zumo de piña. No te apetece beber solo."
    "Al cabo de un rato..."
    play music ("music/ChillUkelele.ogg")
    wom "¡Hey, yo te conozco!"
    call BlinkXS4("c29s001_135") from _call_BlinkXS4_445
    mc "Hola... No recuerdo tu nombre. Nos vimos en el aeropuerto de San Luis hace un mes más o menos."
    olg "Olga. Es verdad, tu eras el que venía a recoger a aquella chica tan guapa... ¿Kim? ¿Kelly?"
    mc "[kim]. Soy [mc]."
    olg "Encantado de conocerte, [mc]. *Risa* Conocerte por segunda vez, claro."
    mc "Igualmente, Olga."
    call BlinkXS4("c29s001_140") from _call_BlinkXS4_446
    olg "¿Te importa si te hago compañía? Mi jefa estará ocupada un rato. Supongo que a quién hayas traído tú también."
    mc "No sé a lo que te refieres..."
    call BlinkXS4("c29s001_145") from _call_BlinkXS4_447
    olg "He supuesto que eras chófer o algo así... Si fuiste a buscar a [kim], y hoy estás aquí bebiendo un zumo..."
    mc "*Risa* Oh, no. He venido con mi novia. Es amiga de la anfitriona."
    call BlinkXS4("c29s001_150") from _call_BlinkXS4_448
    olg "¡Oops! Perdón."
    mc "No te preocupes. La confusión es normal. ¿Así que trabajas para alguien en esta fiesta?"
    call BlinkXS4("c29s001_155") from _call_BlinkXS4_449
    olg "Sí, soy su asistente personal. Pero me aburren estas fiestas."
    mc "Supongo que lo de conocer a ricos y famosos deja de ser interesante al tercero o al cuarto."
    call BlinkXS4("c29s001_160") from _call_BlinkXS4_450
    olg "*Risa* Exacto. Acaba siendo más interesante hablar con las personas que los rodean."
    olg "A menos que seas muy fan de alguien, claro."
    mc "No es mi caso, pero estoy seguro de que una de mis primas estaría totalmente embobada."
    mc "Hace un rato he visto a Taylor Shift. Es su cantante favorita."
    scene c29s001_160d with dissolve
    olg "Mírala. Ahí está."
    mc "¿La otra chica es...?"
    olg "Sí, es ella. Una chica muy maja."
    mc "Pues ahora mi prima estaría embobada totalmente. Sus dos cantantes favoritas en el mismo lugar."
    call BlinkXS4("c29s001_165") from _call_BlinkXS4_451
    olg "¿Quieres que les diga que quieres hacerte una selfie con ellas para enviársela a tu prima?"
    mc "No hace falta. No soy una persona muy de selfies ni de famosos. *Risa* Con decirle a [dap] que he estado en la misma fiesta que ellas se morirá de envidia."
    mc "Además, creo que este tipo de gente, los famosos, no vienen a estas fiestas a que los fans se hagan fotos con ellos."
    call BlinkXS4("c29s001_170") from _call_BlinkXS4_452
    olg "Es cierto que no les suele gustar, pero conozco a las dos, y seguramente no les importaría si se lo pidiera."
    olg "Sobre todo, si les digo que has venido desde San Luis. Eso deben ser... ¿Cuánto? ¿4 o 5 horas conduciendo?"
    mc "Más o menos, pero no vengo de San Luis, sino de Newport. Una ciudad cercana."
    call BlinkXS4("c29s001_175") from _call_BlinkXS4_453
    olg "¿De Newport? ¡Mi hermana y mi hermano viven allí! Bueno, mis medio-hermanos..."
    mc "*Risa* Creo que tú y yo estamos destinados a algo. Son demasiadas casualidades, ¿no?"
    call BlinkXS4("c29s001_180") from _call_BlinkXS4_454
    olg "*Risa* Tienes razón. Nos hemos encontrado un par de veces en sitios donde ninguno de los dos vivimos."
    olg "Y mi familia vive en la misma ciudad que tú. Lo que sería una casualidad tremenda es que los conocieras."
    mc "*Risa* Newport no es Los Angeles, pero tampoco es un pueblo de cien habitantes. No conozco a todo el mundo en la ciudad."
    mc "Además, he estado fuera unos años, estudiando en Portland."
    call BlinkXS4("c29s001_185") from _call_BlinkXS4_455
    olg "Bueno, creo que me toca irme. Por ahí viene mi jefa."
    mc "Encantado de volverte a ver, aunque haya sido para un encuentro casi tan breve como la última vez."
    olg "Igualmente, [mc]. Si algún día voy a visitar a mis hermanos, seguro que no nos encontramos."
    mc "*Risa* Apunta mi teléfono si quieres y cuando vayas, llámame."
    call BlinkXS4("c29s001_190a") from _call_BlinkXS4_456
    olg "Creo que prefiero que sigan siendo encuentros casuales. *Risa* Si planeamos algo podríamos perder nuestra magia."
    mc "*Risa* Como quieras. Hasta el próximo encuentro casual."
    scene c29s001_190ba with dissolve
    hal "Hola. ¿Interrumpo algo?"
    scene c29s001_190e with dissolve
    olg "No, Halley. Este es [mc]. Esta es Halley, mi jefa."
    hal "Hola, [mc]. ¿Te importa si te robo a mi asistente?"
    mc "Encantado de conocerte, Halley. Y no te preocupes, Olga es tu asistente, al fin y al cabo."
    scene c29s001_190f with dissolve
    hal "Nos podemos ir cuando quieras. O puedes quedarte, si lo prefieres."
    olg "No hace falta. Podemos irnos. *Risita* [mc] y yo preferimos los encuentros breves."
    call BlinkXS4("c29s001_190c") from _call_BlinkXS4_457
    olg "Bueno, [mc]. Hasta la próxima, ya sea en Newport, Nueva York, o en una isla del Caribe."
    mc "Hasta la próxima, Olga. Cuídate."
    call BlinkXS4("c29s001_190d") from _call_BlinkXS4_458
    hal "Hasta otra, [mc]."
    stop music fadeout (1.5)
    mc "Hasta otra, Halley."
    scene c29s001_130d with fade
    play music ("music/Sad-Cinematic.ogg")
    "Vuelves a quedarte solo en la barra. Pides otro zumo de piña."
    "Aunque solo es relativo, ya que la gente va yendo y viniendo sin interactuar contigo."
    "Supones que los habituales de estas fiestas se lo deben estar pasando bien."
    "Pero esperabas algo diferente en tu primera cita con [lis]. Entiendes que no ha visto a sus amigas desde hace tiempo, pero te sientes solo y aburrido."
    "Cuando vas por el tercer zumo de piña..."
    stop music fadeout (1.5)
    call BlinkXS4("c29s001_195") from _call_BlinkXS4_459
    ska "¿No te gustan las fiestas?"
    play music ("music/Sunny-Skies.ogg")
    mc "No demasiado... ¡Oh! Eres Scarlett Johnson..."
    call BlinkXS4("c29s001_200") from _call_BlinkXS4_460
    ska "*Risa* Sí, la última vez que lo comprobé, esa era yo."
    mc "Perdona. No estoy acostumbrado a estos ambientes. Ni a cruzarme con cantantes y actores cada dos minutos."
    mc "*Risa* Supongo que se me pasará dentro de cuatro o cinco famosos más."
    ska "*Risa* Hay gente a la que no se le pasa nunca. Pero es mejor acostumbrarse."
    mc "Soy [mc]. *Risa* No soy famoso."
    call BlinkXS4("c29s001_205") from _call_BlinkXS4_461
    ska "Déjame adivinar. Supongo que alguien te ha traído a esta fiesta en la que no conoces a nadie y te ha dejado solo."
    mc "Mas o menos. Mi novia es amiga de Sidney y de algunas otras personas aquí. Hacía tiempo que no las veía y se están poniendo al día."
    ska "Y, como es la primera vez que vienes a una fiesta de estas, no sabes con quién hablar."
    mc "Ni con quién, ni de qué hablar. No creo que tenga muchos intereses en común con el 90%% de gente en esta fiesta."
    mc "¡Hey! *Risa* ¡Pero estoy hablando con Scarlett Johnson!"
    mcp "(Y conozco a alguien que podría ser tu relevo haciendo de Natasha. Es un papel en el que [eva] encajaría perfectamente.)"
    call BlinkXS4("c29s001_210") from _call_BlinkXS4_462
    ska "*Risa* Con la que seguramente no tengas muchos intereses en común."
    mc "*Risa* Touché."
    call BlinkXS4("c29s001_215") from _call_BlinkXS4_463
    ska "La mayoría de nosotros somos personas normales, o intentamos seguir comportándonos como recordamos que hacíamos antes de todo esto."
    ska "Encontrarás unos cuantos que creen que por haber alcanzado la fama son especiales, pero no deja de ser un trabajo."
    mc "No te ofendas, pero ¿a qué edad empezaste a actuar? ¿Realmente recuerdas cómo era una vida normal antes de eso?"
    call BlinkXS4("c29s001_220a") from _call_BlinkXS4_464
    ska "*Risa* Ahora es mi turno de decir 'Touché'. No hay mucha gente que piense en eso."
    mc "Creo que te he visto actuando desde que nací. Es lógico pensar en eso."
    call BlinkXS4("c29s001_220b") from _call_BlinkXS4_465
    ska "*Risa* ¡No soy tan vieja!"
    mc "*Risa* Y yo no soy tan viejo como parezco."
    call BlinkXS4("c29s001_225") from _call_BlinkXS4_466
    ska "Mi primera película fue en 1994. ¿Dónde estabas tú entonces?"
    mc "Creo que ni siquiera era un pensamiento en la mente de mis padres por entonces. Mi madre tenía 12 años."
    call BlinkXS4("c29s001_230") from _call_BlinkXS4_467
    ska "*Risa* Me acabas de hacer sentir como un fósil. Como si no lo hicieran ya la mitad de las chicas en esta fiesta."
    mc "*Risa* Te he dicho que te he visto actuando desde que nací..."
    lis "Y mi novio nunca miente, Scarlett."
    scene c29s001_235a with dissolve
    ska "¿Qué? ¿Tú eres la que has dejado solo a este chico durante tanto rato, [lis]?"
    lis "No me hagas sentir culpable por eso. Ya me siento lo suficientemente mal."
    lis "Además, así ha tenido la oportunidad de conocerte."
    scene c29s001_235b with dissolve
    ska "No sabía que ibas a venir. Si lo hubiera sabido, habría reservado más tiempo para esta fiesta."
    ska "Y más aún si hubiera sabido que sales con este chico tan simpático. Pero me esperan en otro sitio."
    lis "Siempre estás super ocupada. Tienes que aprender a relajarte un poco."
    scene c29s001_235c with dissolve
    ska "*Risa* El día que aprendas tú en qué diccionario tienes que buscar la palabra 'relajarse'."
    lis "*Risa* Creo que te podría dar consejos sobre dónde buscarla. Yo ya la he encontrado."
    scene c29s001_235d with dissolve
    ska "Déjame mirarte..."
    ska "..."
    ska "No me había fijado, pero tienes razón. Hay algo diferente en ti, algo que dice que estás mucho mejor que la última vez que te vi."
    ska "Y ese pelo... me encanta. La [lis] de hace tres meses nunca lo hubiera llevado así."
    lis "Estoy mucho mejor, Scarlett. Mudarme a Newport ha tenido efectos... inesperados."
    mc "*Risa* También en Newport. El comercio de ropa se ha multiplicado en el último mes."
    scene c29s001_235e with dissolve
    lis "*Risa* Idiota."
    ska "*Risa* Si este es el resultado, es algo bueno. Y no me refiero solo a algo bueno para el comercio local en Newport."
    mc "*Risa* Hay un par de tiendas que están pensando en comprar alfombras rojas para cuando llega [lis]."
    scene c29s001_235f with dissolve
    ska "Chicos, me gustaría quedarme charlando con vosotros, pero ya os he dicho que me esperan en otro sitio."
    ska "Chris daba una fiesta también hoy. Solo para fósiles de más de 35."
    lis "¿Prat o Evan? He visto a Hemswort por aquí hace un rato, con lo que no puede ser él. Bueno, da lo mismo. Me caen bien los dos. Dales un beso de mi parte."
    mc "*Risa* No hace falta ni que los saludes de mi parte. Estoy seguro de que no se acordarán de mí."
    scene c29s001_235g with dissolve
    ska "¿Ya los has conocido? No me han dicho nada de que [lis] saliera con alguien."
    mc "*Risa* Nope. Por eso no se acordarán de mí."
    scene c29s001_235h with dissolve
    ska "*Risa* Me gusta el sentido del humor de tu novio."
    ska "Pero en serio, me tengo que ir o Chris me matará."
    lis "No te entretenemos más. Además, tengo que compensar a [mc] por dejarlo solo tanto rato."
    call BlinkXS4("c29s001_240") from _call_BlinkXS4_468
    ska "Cuida de esta chica. Es de las que valen la pena."
    stop music fadeout (1.5)
    mc "No te preocupes. Lo haré. Y ahora vete antes de que cualquiera de los Chris te mate."
    play music ("music/Separation.ogg")
    scene c29s001_245a with fade
    call BlinkXS4("c29s001_245") from _call_BlinkXS4_469
    lis "Siento haberte dejado solo. Quería volver, pero me he ido encontrando a gente y..."
    mc "No te preocupes, lo entiendo. Hacía meses que no veías a tus amigas y querías saludarlas."
    call BlinkXS4("c29s001_250") from _call_BlinkXS4_470
    lis "Sí, pero también quería estar contigo. Esto no es lo que tenía pensado para la primera cita."
    mc "[lis], a veces las cosas no salen como las planeamos. Y habrá más citas."
    call BlinkXS4("c29s001_255") from _call_BlinkXS4_471
    lis "Pero nunca más habrá una primera cita..."
    mc "Eso es fácil de arreglar. Te dejo."
    scene c29s001_255d with hpunch
    lis "¿Qué?"
    mc "¿Quieres salir conmigo?"
    scene c29s001_255d with hpunch
    lis "¿Qué?"
    mc "Si dices que sí, podemos empezar nuestra segunda primera cita ahora mismo."
    scene c29s001_255e with hpunch
    lis "¡Eres el mejor novio del mundo!"
    mc "*Risa* Ahora mismo sólo soy el mejor ex-novio del mundo. Aún no has dicho que sí."
    lis "¡Claro que quiero salir contigo!"
    stop music fadeout (1.5)
    scene c29s001_255f with dissolve
    "El alivio que la chica siente se refleja en cómo sus labios saludan a los tuyos."
    play music ("music/Stardust.ogg")
    "Lo que ha empezado como una noche extraña cambia en un momento. A mejor."
    scene c29s001_255g with dissolve
    "Los famosos y los amigos de [lis] dejan de existir y parece que estáis solos en la fiesta mientras vuestras lenguas se entrelazan."
    scene c29s001_255h with dissolve
    "Incluso la fiesta desaparece a vuestro alrededor. No hay piso. No hay música. No hay nada aparte de vosotros dos y de un largo beso."
    "Vuestro mundo en ese momento solo está habitado por vosotros dos."
    call BlinkXS4("c29s001_260") from _call_BlinkXS4_472
    mc "Esta fiesta acaba de mejorar mucho."
    lis "Gracias por dejarme... Y por volver a pedirme salir."
    mc "*Risa* No podía permitir que otro tipo se llevara a la chica más guapa de la fiesta ahora que estaba soltera de nuevo."
    call BlinkXS4("c29s001_265") from _call_BlinkXS4_473
    lis "*Risa* Pero que sea la última vez que me dejas. La próxima vez es posible que haya un cuchillo cerca."
    mc "No voy a tentar a la suerte una segunda vez. *Risa* Imagínate que hubieras dicho que no cuando te he pedido para salir."
    mc "Si quieres que esto acabe, tendrás que hacerlo tú."
    call BlinkXS4("c29s001_270") from _call_BlinkXS4_474
    lis "¿Querer que esto acabe? ¡Acaba de empezar!"
    scene c29s001_270d with dissolve
    lis "Ven, quiero bailar contigo."
    mc "Me parece una buena idea."
    scene c29s001_275An with dissolve
    "Pasáis los siguientes minutos bailando en silencio, sin saber si lo hacéis al ritmo de la inexistente música."
    "No hace falta decir nada. Vuestros brazos alrededor del otro dicen todo lo necesario."
    "No os importa lo que hacen otras personas a vuestro alrededor, porque no hay nadie más."
    "Tú tienes tu mundo entre tus brazos. Un mundo que te abraza a su vez."
    scene c29s001_280An with dissolve
    stop music fadeout (1.5)
    "Pero todo lo bueno acaba y alguien entra en vuestra burbuja particular."
    play music ("music/These-Little-Moments.ogg")
    jen "[lis], vengo a despedirme."
    lis "¿Ya te vas? ¡Hace menos de una hora que he llegado! Casi no hemos tenido tiempo de hablar."
    call BlinkXS4("c29s001_285a") from _call_BlinkXS4_475
    jen "¿Menos de una hora? ¡Qué bonito es el amor cuando empieza! Llevas más de una hora bailando con [mc]."
    jen "Todo el mundo está arriba desde hace rato. Os habéis quedado solos aquí."
    mc "¡Imposible! Diez minutos a lo sumo."
    call BlinkXS4("c29s001_285b") from _call_BlinkXS4_476
    jen "Llevo casi 30 minutos esperando a acercarme para despedirme de [lis]."
    jen "Parecíais tan dulces que no me he atrevido. Pero me tengo que ir. Mañana tengo rodaje."
    scene c29s001_285ca with dissolve
    lis "¿De verdad ha pasado tanto rato?"
    call BlinkXS4("c29s001_285d") from _call_BlinkXS4_477
    jen "Sí, y hace casi dos horas que te has ido de la piscina."
    jen "Esperaba poder charlar un rato más contigo, pero no pasa nada. Nos veremos en la siguiente fiesta."
    call BlinkXS4("c29s001_285e") from _call_BlinkXS4_478
    jen "Doy una fiesta en mi casa el mes que viene. Estás invitado, [mc]."
    mc "Gracias, pero será imposible. Me voy del país unos meses la semana próxima."
    jen "¡Qué lástima! Me hubiera gustado conocerte mejor."
    scene c29s001_285h with dissolve
    jen "Espero que tú sí que vengas, aunque sea sola."
    lis "No lo sé. El mes que viene tendré exámenes y el inicio del nuevo curso. Mándame un mensaje con los datos y te lo confirmo."
    scene c29s001_285i with dissolve
    jen "Genial. Te escribiré cuando sepa la fecha exacta. Nos vemos el mes que viene, [lis]."
    lis "Nos vemos pronto, Jenny."
    call BlinkXS4("c29s001_285f") from _call_BlinkXS4_479
    jen "Hasta otra, [mc]. Espero que vengas a alguna de mis fiestas cuando vuelvas al país."
    stop music fadeout (1.5)
    mc "Seguro. Hasta otra, Jenny."
    scene c29s001_290a with fade
    call BlinkXS4("c29s001_290") from _call_BlinkXS4_480
    play music ("music/Sad-Piano.ogg")
    lis "¿Quieres ir a la barra a por algo de beber y nos sentamos un rato?"
    mc "Sí. Mis pies me están diciendo que hemos bailado durante mucho rato, pero mi cabeza me dice que solo han sido unos minutos."
    call BlinkXS4("c29s001_295") from _call_BlinkXS4_481
    lis "Me está pasando lo mismo. No me puedo creer que hayamos estado bailando una hora."
    mc "Mis pies son como yo. No mienten. Y creo que Jenny ha dicho más de una hora."
    mc "Busca un sitio para sentarte. ¿Qué te traigo para beber?"
    scene c29s001_300d with fade
    "Después de recoger las bebidas te diriges hacia el sofá donde se ha sentado [lis]."
    "En una fiesta rodeada de famosos, está claro quién es la princesa de verdad."
    "Aunque en esta planta solo quedéis el barman y vosotros, da lo mismo."
    "[lis] reluciría más que cualquier joya en una cámara del tesoro."
    scene c29s001_300a with fade
    call BlinkXS4("c29s001_300") from _call_BlinkXS4_482
    mc "¿Pasa algo, [lis]?"
    lis "¿Por qué lo dices?"
    mc "Tu lenguaje corporal me dice que ha pasado algo."
    mc "Si es por haberme dejado solo un rato, no te preocupes. Lo entiendo."
    call BlinkXS4("c29s001_305") from _call_BlinkXS4_483
    lis "No es eso. O no es eso del todo."
    mc "Entonces explícame que pasa, por favor."
    lis "Tenía muchas ganas de venir a esta fiesta contigo y de volver a ver a mis amigas. De que las conocieras."
    mc "Es lógico. Hacía tiempo que no las veías."
    call BlinkXS4("c29s001_310") from _call_BlinkXS4_484
    lis "Sí, y ese tiempo me lo he pasado rodeada por los Marks y el resto de las chicas."
    mc "¿Qué tiene que ver eso?"
    lis "Cuando estaba arriba, en la piscina... sólo quería volver contigo."
    mc "Me siento halagado, pero entiendo que quisieras pasar tiempo con Jenny, Sidney, o quien fuera."
    call BlinkXS4("c29s001_315") from _call_BlinkXS4_485
    lis "Pero es que no es eso... Quería que me sacaras de ahí. Que aparecieras con tu brillante armadura y tu caballo blanco para rescatarme."
    lis "He descubierto que prefiero un minuto con [kim], [eva], [emm], o [mad.nick] a una hora con las chicas que consideraba mis amigas."
    call BlinkXS4("c29s001_320") from _call_BlinkXS4_486
    lis "Me habéis cambiado demasiado... Las conversaciones me parecían vacías. Sólo hablaban de rodajes, de discos, de quién salía con quién..."
    if mc._var("relationships")>1:
        lis "Yo quería hablar de la familia. Del harén. De [eva] y [ama]. De NTR y de la Guerra Clon..."
    else:
        lis "Yo quería hablar de la familia. De [eva] y [ama]. De NTR y de la Guerra Clon..."
    lis "Comparado con eso, hablar de a quién van a nominar para los Globos de Plata me parece... algo simplista..."
    mc "No puedes comparar amistades, [lis]. Lo que hay en casa es diferente a unas amigas que ves una vez al mes o cada dos meses en una fiesta."
    mc "Con las chicas de casa estás conviviendo todos los días, incluso varias veces por semana con las que no viven en casa..."
    call BlinkXS4("c29s001_325") from _call_BlinkXS4_487
    lis "A eso me refiero. Evolucionamos a la vez. Sabemos todo las unas de las otras. Lo bueno y lo malo. Somos amigas de verdad."
    lis "Jenny, Scarlett, o Sidney me caen muy bien, pero tenemos una relación... superficial."
    call BlinkXS4("c29s001_330") from _call_BlinkXS4_488
    if mc._var("relationships")>1:
        lis "A ellas nunca me atrevería a decirles que te comparto con otras mujeres."
        lis "O que salgo con el dueño de una empresa que hace cosas que serían ilegales en los Estados Unidos."
    else:
        lis "A ellas nunca me atrevería a decirles que salgo con el dueño de una empresa que hace cosas que serían ilegales en los Estados Unidos."
    lis "O que dos de mis mejores amigas son asesinas profesionales. Sólo verían eso. Se quedarían en la superficie."
    lis "No intentarían entender lo especiales que son [ama] y [eva]. Ni por lo que han pasado."
    mc "Y si a tus amigas les tienes que ocultar cosas que para ti son importantes..."
    call BlinkXS4("c29s001_335a") from _call_BlinkXS4_489
    lis "Exacto. Te planteas si son realmente tus amigas o solo chicas con las que te llevas bien en este entorno."
    mc "Lo entiendo. Creo que, en casa, has descubierto lo que son amigas de verdad."
    call BlinkXS4("c29s001_335b") from _call_BlinkXS4_490
    lis "Si tuviera que esconder un cadáver, estas 'amigas' se escandalizarían. ¿La 'pequeña [lis]' ha matado a alguien?"
    lis "[eva] traería una pala sin hacer preguntas. [ama] descuartizaría el cadáver y haría las preguntas luego. Pero no me juzgaría fueran cuales fueran las respuestas."
    lis "Y [emm] traería una bolsa con un lazo rosa para que el muerto llegara al más allá con estilo."
    call BlinkXS4("c29s001_335c") from _call_BlinkXS4_491
    lis "Creo que no sabía que carecía de amigas hasta hoy."
    mc "No careces de amigas. Tienes un montón esperándote en casa."
    call BlinkXS4("c29s001_340") from _call_BlinkXS4_492
    lis "Tienes razón... Sácame de aquí, por favor."
    mc "Creo que vas a tener que sacarme tú. No recuerdo dónde está el ascensor. Pero deberíamos despedirnos de Sidney antes."
    lis "Otra vez tienes razón."
    stop music fadeout (1.5)
    scene black with dissolve
    return
label c29s002_LisLewd:
    if _in_replay:
        $ mc._var("relationships", 1, "set")
        call mrS3_ama_route from _call_mrS3_ama_route_13
        call mrS3_sca_route from _call_mrS3_sca_route_9
        call mrS3_emm_route from _call_mrS3_emm_route_39
        call mrS3_kim_route from _call_mrS3_kim_route_11
        call mrS3_sai_route from _call_mrS3_sai_route_19
        call mrS3_deb_route from _call_mrS3_deb_route_25
        call mrS3_kia_route from _call_mrS3_kia_route_16
        call mrS3_mad_route from _call_mrS3_mad_route_16
        call mrS3_mar_route from _call_mrS3_mar_route_40
        call mrS3_sim_route from _call_mrS3_sim_route_21
        if mc._var("relationships")<11:
            menu:
                "¿En cuántas relaciones estás?"
                "Más de 10":
                    $ mc._var("relationships", 11, "set")
                "Entre 2 y 10":
                    $ mc._var("relationships", 3, "set")
                "Solo con [lis]":
                    $ mc._var("relationships", 1, "set")
    scene black with dissolve
    "No hay limusinas esta vez. [lis] llama a un Under que llega para recogeros en unos minutos y os lleva al hotel que la chica ha reservado."
    play music ("music/SaveMe.ogg")
    call BlinkXS4("c29s002_005") from _call_BlinkXS4_493
    lis "Ya estamos aquí. Siento si la habitación es pequeña."
    mc "Me gusta la habitación. No necesito nada más. Lo único necesario es que tú estés en ella."
    call BlinkXS4("c29s002_010") from _call_BlinkXS4_494
    lis "Si me paso con algunos gastos, mi padre comprobaría en qué me he gastado el dinero y..."
    mc "Y tendrías que dar explicaciones de por qué no te has quedado a dormir en casa de Sidney, ¿no?"
    call BlinkXS4("c29s002_015") from _call_BlinkXS4_495
    lis "Exacto... No es que quiera esconder que tú y yo estamos juntos, pero no quiero tener que darles explicaciones a mis padres."
    lis "No quiero estar preocupándome por el interrogatorio en nuestra primera noche juntos."
    mc "[lis], tampoco me tienes que dar explicaciones a mí. La habitación es más que suficiente."
    mc "No es un motel de mala muerte en mitad de la nada. Y, aunque lo fuera, sería suficiente."
    mc "Y, si alguna vez quieres ocultar tus gastos, dímelo y pagaré yo."
    mc "Siempre y cuando no se trate de ropa, claro. *Risa* No quiero tener que vender mis acciones de NTR para llenarte el armario."
    call BlinkXS4("c29s002_020") from _call_BlinkXS4_496
    lis "Eres un capullo. *Risa* Ni siquiera mi padre me dice cuánto puedo gastarme en ropa."
    mc "*Risa* Tu padre espera que tu ropa la pague tu futuro marido. Sabe que solo va a tener que pagar por tiempo limitado."
    lis "*Risa* Y ese futuro marido vas a ser tú y tienes que empezar a 'educarme', ¿no?"
    mc "Ya veremos."
    scene c29s002_020d with dissolve
    "La princesa se acerca a tus labios con una timidez que no ha mostrado en la fiesta."
    "Estar en solos en una habitación de hotel, y saber lo que va a pasar, o lo que puede pasar, está frenándola."
    call BlinkXS4("c29s002_025") from _call_BlinkXS4_497
    lis "¿Qué quieres decir con 'ya veremos'?"
    if kia._var("route") or mad._var("route") or mar._var("route") or sim._var("route"):
        mc "Sé que habéis estado hablando desde la primera propuesta de matrimonio, y sé que es posible que esperes que te lo proponga a ti."
        mc "Pero quiero que, cuando lo haga, sea algo natural. No quiero que sea algo forzado porque se lo he pedido a otra chica antes."
        mc "Y aunque lo hiciera, no sé si tú dirías que sí."
    else:
        mc "Que aún no te he pedido matrimonio ni lo voy a hacer hoy. Y aún no sé si tú dirías que sí."
    call BlinkXS4("c29s002_030") from _call_BlinkXS4_498
    lis "*Risita* Ya veremos."
    scene c29s002_030d with dissolve
    lis "Voy al baño a cambiarme."
    mc "¿De dónde han salido esas maletas?"
    call BlinkXS4("c29s002_035") from _call_BlinkXS4_499
    lis "Las mandé ayer al hotel. No esperabas que volviera mañana a casa con la misma ropa que llevo hoy, ¿no?"
    mc "*Risa* Ni me lo había planteado, si te soy sincero."
    scene c29s002_035d with dissolve
    lis "Me parece que voy a ser yo el que te tenga que educar."
    lis "En la pequeña tienes una muda de ropa, un neceser, y un pijama. [mar] me ayudó a meter todo lo que necesitas."
    lis "Espérame ahí."
    scene c29s002_035e with fade
    "Te pones rápidamente la parte inferior del pijama, guardas la maleta, y esperas a que [lis] termine de cambiarse."
    "Si ha hablado del pijama, no crees que sea lo mejor que la esperes desnudo."
    scene c29s002_035f with dissolve #reloj 10:10
    "Esperas..."
    scene c29s002_035g with fade #reloj 10:35
    "Sigues esperando..."
    scene c29s002_035e with dissolve
    mc "[lis], ¿todo bien ahí dentro?"
    lis "*Desde el baño* Sí, casi estoy lista..."
    scene c29s002_035h with fade #reloj 10:45
    "Esperas un poco más..."
    scene c29s002_035e with fade
    lis "*Desde el baño* ¿Listo?"
    mc "*Ronquido fingido*"
    lis "*Desde el baño* *Risa* ¡No he tardado tanto!"
    mc "*Risa* Tu definición de 'tanto' y la mía son diferentes."
    lis "*Desde el baño* Voy a salir..."
    stop music fadeout (1.5)
    scene c29s002_040d with fade:
        yalign 1.0
        linear 5.0 yalign 0.0
    pause (4.8)
    call BlinkXS3("c29s002_040") from _call_BlinkXS3_777
    play music ("music/SeeingHeaven.ogg")
    mc "..."
    call addProfileImageS3 (7, "lis_7", lis, __(": 15 - Especial"), "") from _call_addProfileImageS3_23
    lis "¿No vas a decir nada?"
    mc "No creo que pueda decir nada que le haga justicia a lo preciosa que estás ahora mismo."
    mc "El tiempo de espera ha valido la pena."
    call BlinkXS4("c29s002_045") from _call_BlinkXS4_500
    lis "Sobre eso..."
    mc "¿Hay algo que te preocupe, [lis]?"
    lis "No todo el rato que he estado ahí dentro me lo he pasado cambiándome..."
    mc "¿Qué has estado haciendo?"
    call BlinkXS4("c29s002_050") from _call_BlinkXS4_501
    lis "Me he pasado más de diez minutos dudando entre la lencería y el pijama..."
    mc "Siéntate conmigo, [lis]."
    scene c29s002_055a with fade
    call BlinkXS4("c29s002_055") from _call_BlinkXS4_502
    lis "Parezco tonta..."
    mc "No lo pareces. La primera vez es un paso muy importante en una relación."
    lis "Ya, pero yo quería..."
    mc "Y ya no quieres."
    call BlinkXS4("c29s002_060") from _call_BlinkXS4_503
    lis "Quiero. Pero me da miedo."
    mc "No es necesario que hagamos nada hoy, aparte de dormir."
    lis "Pero eso te decepcionaría..."
    mc "¿Decepcionarme? Me decepcionaría si no quisieras dormir abrazada a mí."
    mc "Pero no me voy a decepcionar por no tener sexo. ¡No soy un bonobo!"
    call BlinkXS4("c29s002_065") from _call_BlinkXS4_504
    lis "¿De verdad? ¿No vas a pensar que soy una cobarde?"
    if ama._var("route"):
        mc "¿Te acuerdas del día que Zeus rompió la cama?"
        lis "Sí, ¿pero qué tiene eso que ver?"
        mc "[ama] me dijo ese día que no quería tener una cita conmigo por miedo a lo que pudiera pasar."
        mc "¿Crees que [ama] es una cobarde? ¿Crees que yo pienso que es una cobarde?"
    elif sca._var("route"):
        if persistent.family and mc._var("edmundsStory"):
            mc "¿Te acuerdas del día en que llegaron los resultados de ADN de [sca]?"
        else:
            mc "¿Te acuerdas del día en que [dap] adoptó a [sca] como hermana?"
        lis "Sí, ¿pero qué tiene eso que ver?"
        mc "[sca] vino esa noche a dormir conmigo. Sólo a dormir."
        lis "Lo sé, y sé lo que pasó por la mañana."
        mc "Lo que pasó por la mañana no importa. Tan solo que ella sólo quería dormir abrazada a mí esa noche."
        mc "¿Crees que [sca] es una cobarde? ¿Crees que yo pienso que es una cobarde?"
    else:
        mc "¿Sabes que [eil] y yo pospusimos nuestra primera vez un par de veces?"
        lis "Sí, me lo ha contado... ¿Pero qué tiene eso que ver?"
        mc "¿Crees que [eil] es una cobarde? ¿Crees que yo pienso que es una cobarde?"
    call BlinkXS4("c29s002_070") from _call_BlinkXS4_505
    if ama._var("route"):
        lis "¡No! ¡Es una de las mujeres más valientes que conozco! Con su trabajo..."
    elif sca._var("route"):
        lis "¡No! ¡Es una de las mujeres más valientes que conozco! Atreverse a irse de casa así..."
    else:
        lis "¡No! ¡Es una de las mujeres más valientes que conozco! Enfrentarse a Solomon como lo ha hecho estos años..."
    mc "¿Entiendes ahora por qué no voy a pensar que eres una cobarde por no querer tener sexo hoy?"
    call BlinkXS4("c29s002_075") from _call_BlinkXS4_506
    lis "Pero el resto de las chicas van a..."
    mc "Lo que piensen el resto de las chicas sobre lo que hagamos tú y yo en una habitación de hotel no tiene por qué importarte."
    mc "Si ellas se han creado expectativas sobre lo que va a pasar esta noche, es su problema, no el tuyo. No el nuestro."
    call BlinkXS4("c29s002_080") from _call_BlinkXS4_507
    lis "No le debemos explicaciones a nadie, ¿verdad?"
    mc "No, [lis]. No les tenemos que dar explicaciones a nadie sobre lo que hagamos."
    mc "Si me preguntan no voy a mentir, pero no lo van a hacer."
    call BlinkXS4("c29s002_085") from _call_BlinkXS4_508
    lis "Pero a mí sí que me van a preguntar..."
    mc "Entonces les puedes decir la verdad. Diles que hemos bailado durante mucho rato y que me duelen los pies."
    call BlinkXS4("c29s002_090") from _call_BlinkXS4_509
    lis "¿Qué? ¿Eso es verdad?"
    mc "Claro que es verdad. He bailado más rato seguido que nunca. Ni siquiera en el Jazz Corner bailé tanto rato seguido."
    mc "Me senté un rato con [kat] para descansar. Pero mi princesa no me ha dejado descansar hoy."
    call BlinkXS4("c29s002_095") from _call_BlinkXS4_510
    lis "¿Me estás dando una excusa para poder contarles y que no me juzguen?"
    mc "No necesitas ninguna excusa. Lo que estoy diciendo es verdad. Y ni te van a juzgar, ni tienen derecho o razones para hacerlo."
    if ama._var("route"):
        mc "¿Alguien juzga a [ama]?"
    elif sca._var("route"):
        mc "¿Alguien juzga a [sca]?"
    else:
        mc "¿Alguien juzga a [eil]?"
    call BlinkXS4("c29s002_100") from _call_BlinkXS4_511
    lis "¿Me prometes que no te importa?"
    mc "Lo único que me importará es si tardas media hora en ponerte el pijama."
    mc "La lencería es preciosa, pero estoy seguro de que no vas a dormir cómoda."
    call BlinkXS4("c29s002_105") from _call_BlinkXS4_512
    lis "Espérame aquí. Sólo tardo un minuto."
    mc "Creo que te olvidas de algo."
    call KissXS4("c29s002_110") from _call_KissXS4_7
    call BlinkXS4("c29s002_110") from _call_BlinkXS4_513
    lis "*Risita* Creo que no me acostumbraré a esto. Espero no acostumbrarme pronto."
    mc "Lo harás. Ve a cambiarte, Princesa. Los pies me están matando."
    scene c29s002_110e with dissolve
    mc "Bonito culo, por cierto."
    lis "Con el pijama no será tan bonito. Despídete de él."
    scene c29s002_035e with fade
    "Decides que tienes que comprarle un reloj a [lis]. Sus minutos duran más que los del resto de mortales."
    "Pero esperar por ella vale la pena. Ya sea esperar a que se cambie o esperar a que esté preparada."
    stop music fadeout (1.5)
    scene c29s002_120d with fade:
        yalign 1.0
        linear 5.0 yalign 0.0
    pause (4.8)
    call BlinkXS3("c29s002_120") from _call_BlinkXS3_778
    play music ("music/thinking-of-you.ogg")
    lis "Ya estoy lista."
    mc "Estás muy mona con ese pijama, aunque me gusta más el de la vaca."
    lis "Lo usé anoche y lo he puesto para lavar esta mañana. No pensaba que acabaría usando pijama..."
    mc "Supongo que es lo bueno de llevar una maleta enorme cada vez que te mueves. O varias."
    call BlinkXS4("c29s002_125") from _call_BlinkXS4_514
    lis "*Risa* Si no hubiera preparado las maletas, no tendrías un pijama para dormir. Tan solo soy previsora."
    mc "¿Nadie te ha dicho que duermo desnudo?"
    call BlinkXS4("c29s002_130") from _call_BlinkXS4_515
    lis "Sí... Pero por si me echaba atrás decidí ponerte el pijama."
    lis "Si estuvieras desnudo ahora mismo... sería un recordatorio de que no he..."
    mc "Hiciste bien, Princesa. Aunque yo habría sido capaz de meterlo todo en una sola maleta. Una pequeña, como la mía."
    mc "¿Qué llevas en la tuya?"
    call BlinkXS4("c29s002_135") from _call_BlinkXS4_516
    lis "Sólo lo necesario. La ropa que llevaba hoy. La que me pondré mañana. Un par de mudas, por si la previsión del tiempo se ha equivocado."
    lis "Zapatos, botas por si llueve, el neceser, el secador de pelo... Nunca sabes qué potencia van a tener los secadores en los hoteles..."
    lis "La lencería, con sus zapatos a juego. El bolso de hoy y un par para mañana, un paraguas, gafas de sol, la tablet, los cargadores..."
    mc "*Risa* ¿Y un par de pajes, un unicornio, y un par de escoltas no cabían en la maleta?"
    call BlinkXS4("c29s002_140") from _call_BlinkXS4_517
    lis "*Risa* ¡No te rías de mí! ¡Todo eso es necesario!"
    lis "Si mañana llueve me darás las gracias por haber traído un paraguas."
    mc "Estoy seguro de que lo haré, pero no va a llover. Ni aquí ni en Newport."
    call BlinkXS4("c29s002_145") from _call_BlinkXS4_518
    lis "*Risa* Eso nunca lo puedes saber."
    mc "Mientras te esperaba he mirado la previsión del tiempo para mañana. *Risa* En los 50 estados."
    call BlinkXS4("c29s002_150") from _call_BlinkXS4_519
    lis "¡No he tardado tanto!"
    mc "*Risa* No voy a discutir sobre eso. Prefiero hacer esto."
    scene c29s002_150d with dissolve #beso
    "[lis] se tensa al primer contacto de tus labios con los suyos. Para ella no es lo mismo el beso que te ha dado antes de ir a cambiarse que un beso en la cama."
    "No sabe dónde puede llevar ese beso y casi puedes notar los engranajes de su cerebro haciendo cálculos."
    call BlinkXS4("c29s002_155") from _call_BlinkXS4_520
    "Cortas el beso antes de que sea más incómodo para ella."
    mc "Buenas noches, Princesa."
    lis "..."
    scene c29s002_150e with vpunch #beso apasionado
    "Ahora es ella la que te besa."
    "Ha descubierto que se puede dar un apasionado beso que no lleve a ningún otro sitio."
    "Un beso que sea el destino por sí mismo, no un camino hacia nada más."
    call BlinkXS4("c29s002_160") from _call_BlinkXS4_521
    "Y cuando el beso se empieza a volver demasiado apasionado, es ella quien lo corta."
    lis "Buenas noches, mi caballero."
    scene c29s002_160d with dissolve
    "[lis] baja la intensidad de la luz y se acurruca encima de ti. La sientes diminuta a tu lado, como un gatito mojado."
    "Nadie consideraría a [lis] una mujer baja, pero su actitud tímida al abrazarte para dormir juntos por primera vez hace que parezca más pequeña de lo que es."
    scene black with dissolve
    stop music fadeout (1.5)
    "El cansancio del día empieza a hacer mella en vosotros y te quedas dormido en seguida."
    centered "{size=+20}{b}DÍA 32 – VIERNES{/b}{/size}"
    scene c29s002_160e with fade
    play music ("music/UnforeseenMotive.ogg")
    "No eres capaz de saber cuánto tiempo has dormido cuando te despiertas, notando que la princesa no está en la cama contigo."
    "La has buscado inconscientemente mientras dormías y te despiertas sobresaltado al ver que no está."
    scene c29s002_160f with dissolve
    "La puerta del lavabo está abierta y la luz apagada. No se oye movimiento."
    mc "¿[lis]?"
    scene c29s002_160g with dissolve
    lis "*Desde el balcón* Aquí fuera."
    scene c29s002_165a with fade
    call BlinkXS4("c29s002_165") from _call_BlinkXS4_522
    mc "¿Qué haces aquí fuera? ¿Te he despertado moviéndome?"
    lis "No, no he podido pegar ojo todavía."
    mc "¿Llevo mucho rato durmiendo?"
    call BlinkXS4("c29s002_170") from _call_BlinkXS4_523
    lis "Alrededor de un par de horas. Estabas empezando a moverte mucho y he pensado que te estaba molestando."
    mc "No, ni siquiera me he enterado cuando te has levantado."
    scene c29s002_170d with dissolve
    mc "Cuando he salido he estado tentado de preguntarte si había algún guisante debajo de la cama que no te dejara dormir."
    mc "¿Te importa si me siento contigo?"
    scene c29s002_175a with fade
    call BlinkXS4("c29s002_175") from _call_BlinkXS4_524
    lis "Creo que el guisante está en el sótano del hotel. La princesa del cuento lo notaba debajo de... ¿eran siete colchones?"
    lis "*Risita* Las princesas de verdad ni siquiera nos tumbaríamos en una cama con un bulto tan grande. Yo tan solo no podía dormir."
    "No está borracha, pero puedes oler el whisky en su aliento, incluso a esta distancia."
    mc "*Risa* Veo que estás abrazando el papel de princesa."
    call BlinkXS4("c29s002_180") from _call_BlinkXS4_525
    lis "Si mi novio quiere que sea su princesa, seré su princesa. Si quiere que sea otra cosa, seré otra cosa."
    mc "Un tipo afortunado ese novio tuyo. Pero estoy seguro de que sólo quiere que seas una cosa."
    call BlinkXS4("c29s002_185") from _call_BlinkXS4_526
    lis "¿Qué?"
    mc "[lis]."
    call BlinkXS4("c29s002_190") from _call_BlinkXS4_527
    lis "¿Qué?"
    mc "*Risa* Me refiero a que tu novio solo quiere que seas [lis]. Que seas tú misma."
    call BlinkXS4("c29s002_195") from _call_BlinkXS4_528
    lis "*Risa* ¡Maldición, [mc]! ¡Dices una cosa tan bonita y te explicas fatal!"
    mc "Y, aunque te convirtieras en una camionera, seguirías siendo mi princesa."
    call BlinkXS4("c29s002_200") from _call_BlinkXS4_529
    lis "¿Aunque haya fastidiado nuestra primera cita y nuestra primera noche juntos?"
    mc "No has fastidiado nada, Princesa. Ha sido una cita rara, pero seguro que nos reiremos mucho cuando hablemos de ella en el futuro."
    lis "Apenas hemos pasado tiempo juntos..."
    mc "Mi dolor de pies dice lo contrario."
    mc "Que el rato que hemos pasado bailando se nos haya hecho corto no significa que no hayamos pasado más de la mitad de la noche juntos."
    call BlinkXS4("c29s002_205") from _call_BlinkXS4_530
    lis "¿Quieres que te dé un masaje en los pies?"
    mc "¿Sabes dar masajes en los pies?"
    call BlinkXS4("c29s002_210") from _call_BlinkXS4_531
    lis "*Risa* No tengo ni idea de dar masajes en los pies ni en ningún otro sitio. Por norma los masajes me los dan a mí."
    lis "Pero sé dónde me duelen a mí con lo que no debe ser tan difícil. Sólo tendré que apretar donde me duelan a mí."
    mc "Si te duelen los pies, yo sí que sé dar masajes. ¿Quieres uno?"
    call BlinkXS4("c29s002_215a") from _call_BlinkXS4_532
    lis "¿Por qué no me lo has ofrecido cuando hemos llegado? ¡Los pies me están matando!"
    lis "¡Ve a la habitación ahora mismo!"
    scene c29s002_215d with fade
    mc "Espera, ¿te has acostado con ese anillo? Parece un arma peligrosa..."
    call BlinkXS4("c29s002_215b") from _call_BlinkXS4_533
    lis "Me lo iba a quitar, pero mi mano ha acabado debajo tuyo y..."
    lis "Primero no quería despertarte, y, cuando he salido aquí, no tenía dónde dejarlo. No quiero dejarlo en el suelo y perderlo."
    stop music fadeout (1.5)
    mc "Bueno, pues quítatelo antes de tumbarte en la cama para el masaje. Parece que te puedes hacer daño con esas puntas si te rozas la cara."
    scene c29s002_220a with fade
    call BlinkXS4("c29s002_220") from _call_BlinkXS4_534
    play music ("music/You-Know-Instrumental.ogg")
    lis "¿Me pongo así o prefieres boca abajo?"
    mc "Tal como estás es perfecto. ¿Dónde te duele?"
    lis "Las plantas de los pies y los dedos, principalmente."
    scene c29s002_225a with dissolve
    mc "¿Aquí?"
    lis "Sí. Ahí molesta bastante."
    scene c29s002_225b with dissolve
    mc "¿Aquí también?"
    lis "Ahí algo menos. Pero es muy agradable."
    menu:
        "Besarle los pies":
            scene c29s002_225c with dissolve
            mc "¿Qué tal aquí?"
            lis "Eso es aún más agradable..."
        "No hacerlo":
            pass
    scene c29s002_225d with dissolve
    mc "Supongo que aquí también debe dolerte."
    lis "Sí, ahí también."
    lis "Déjame darme la vuelta. Las pantorrillas también las tengo cargadas."
    mc "Es normal. Te has pasado mucho rato con tacones."
    scene c29s002_230a with fade
    lis "Puedes seguir. *Risa* Ha parecido una orden, pero no lo era. Lo juro."
    mc "*Risa* No te preocupes, no me lo he tomado como una orden."
    mc "Además, me recomendaron que no te tratara como a una princesa."
    lis "Pero lo sigues haciendo..."
    scene c29s002_230b with dissolve
    mc "No te trato como a UNA princesa. Te trato como a MI princesa. La diferencia es importante."
    lis "Eso es muy agradable."
    "Por un momento no sabes si se refiere a cómo la tratas o a lo que estás haciendo en su pantorrilla."
    lis "Ahí lo tenía bastante cargado."
    mc "Puedo notar cómo se van relajando los músculos."
    scene c29s002_230c with dissolve
    mc "Parece que esta pantorrilla está más relajada que la otra."
    lis "Creo que soy yo al completo la que está más relajada. Tienes unas manos mágicas."
    lis "Puedes subir más arriba... si quieres."
    mc "¿A tus muslos?"
    scene c29s002_230d with dissolve
    lis "Mejor a mis hombros. Los noto tensos..."
    mc "¿Puedo sentarme sobre tu espalda? Será más cómodo."
    lis "O te sientas sobre mi espalda o te pones de pie. Y a ti también te duelen los pies, con lo que va a ser mi espalda."
    scene c29s002_235a with fade
    mc "¿Aquí es dónde te duele?"
    lis "No me duele. Tan sólo estoy tensa."
    mc "No es nada que un masaje no pueda arreglar."
    lis "Déjame hacer una cosa..."
    scene c29s002_235b with fade
    lis "Así va a ser mejor... Hay menos estorbos..."
    mc "Desde luego. Así no estorba nada..."
    mcp "(¿El whisky le ha dado valor líquido para hacer lo que no quería hacer cuando nos metimos en la cama?)"
    scene c29s002_235c with dissolve
    mc "Creo que ya te estas relajando."
    lis "Un poco... *Risita* Espero no relajarme tanto como para quedarme dormida."
    mc "Si te quedas dormida será una señal de que ya no estás tensa. Será bueno."
    mc "¿Cuánto has bebido?"
    scene c29s002_235d with dissolve
    lis "Una botellita del minibar. Me acababa de servir la segunda cuando has salido. Siempre me han parecido muy graciosas esas mini botellas."
    mc "Bueno, con una botellita no te puedes emborrachar."
    call BlinkXS4("c29s002_240") from _call_BlinkXS4_535
    lis "¿Te preocupa que me haya quitado el top por estar borracha?"
    mc "No. Me preocuparía que pudieras hacer algo de lo que te pudieras arrepentir, si estuvieras borracha."
    mc "Pero claramente no lo estás."
    lis "No, no lo estoy. Ni siquiera achispada."
    mc "Entonces sigamos con el masaje."
    scene c29s002_235c with fade
    mc "Ya casi está. Hombros completamente relajados. ¿Algún sitio más?"
    lis "Los muslos... Cuando has relajado las pantorrillas he podido notar que los muslos siguen tensos."
    mc "Notabas molestias en las pantorrillas y, al desaparecer, has sido consciente de las de los muslos, ¿no?"
    lis "Más o menos..."
    scene c29s002_245a with fade
    mc "Aquí estás tensa."
    lis "*Gemido* Sí, es justo ahí..."
    mc "Acabo en seguida. Están mucho mejor de lo que estaban las pantorrillas."
    lis "Puedes subir más... si quieres..."
    scene c29s002_245b with dissolve
    mc "No noto tensión aquí..."
    lis "No, pero es muy agradable..."
    mc "*Risa* ¿Hemos pasado del masaje relajante al agradable?"
    lis "*Risa* No es que antes no lo fuera, pero ahora es mejor todavía..."
    mc "Avísame cuando quieras que pare."
    lis "Cuando las ranas críen pelo. Tienes unas manos increíbles. Te podrías dedicar a esto profesionalmente."
    lis "Pero puedes subir un poco más..."
    scene c29s002_245c with dissolve
    mc "Esto es lo máximo que puedo subir si quiero mantenerme en los muslos."
    lis "No tienes por qué mantenerte en los muslos..."
    call BlinkXS4("c29s002_250") from _call_BlinkXS4_536
    lis "Además, creo que el famoso guisante me ha hecho una rozadura en el culo... ¿Puedes comprobarlo?"
    lis "Si tienes que quitarme los shorts, no hay ningún problema con ello."
    mcp "(No es el momento de preguntarle si está segura de esto. Ha tenido tiempo durante el masaje para pararlo, y si es lo que quiere...)"
    mc "Si es por temas de salud, habrá que comprobarlo. No queremos que esa rozadura se infecte, ¿no?"
    scene c29s002_255An with dissolve
    lis "¿Cómo está? *Risita* ¿Van a tener que operarme, Doctor?"
    mc "Parece que no. Lo único que veo es la perfección hecha culo. Ni una sola rozadura en la inmaculada piel."
    lis "Entonces creo que puedes seguir con el masaje..."
    mc "*Risa* Tienes suerte de que no cobre por horas."
    call BlinkXS4("c29s002_260") from _call_BlinkXS4_537
    lis "*Risa* Como puedes ver, no llevo dinero encima. No tendría dónde guardarlo."
    lis "¿Aceptas besos como pago?"
    stop music fadeout (1.5)
    mc "Sólo como adelanto."
    play music ("music/SexyLoungeMusic.ogg")
    scene c29s002_265a with dissolve
    "La chica se retuerce entre tus piernas para girarse y darte un pasional beso."
    "Cobrar en besos es una buena forma de alimentar la erección que se ha estado formando en tu pijama mientras recorrías la preciosa piel de [lis] con tus manos."
    scene c29s002_265b with dissolve
    "La princesa interrumpe el beso y vuelve a su posición inicial."
    lis "Como adelanto creo que ya está bien. Puedes seguir con el masaje."
    mc "¿Por dónde sigo?"
    scene c29s002_265An with dissolve
    lis "Me has quitado los pantalones por algo, ¿no? Creo que el interior de mis muslos también necesita un masaje..."
    "La forma nada sutil en la que ha abierto las piernas te indica claramente por dónde la chica quiere que sigas."
    mc "Me encanta el interior de los muslos..."
    scene c29s002_270a with dissolve
    "Pones cada una de tus manos en el interior de sus muslos, a una distancia prudencial de su coño y empiezas a acariciarlos."
    lis "Puedes subir AÚN más..."
    scene c29s002_270b with dissolve
    "Subes tus manos, acariciando la sedosa piel solo con las yemas de tus dedos, mientras notas cómo la carne de gallina empieza a hacer su aparición."
    "Puedes notar el calor que emana de la zona donde ambos muslos se juntan en un coño que parece que te está llamando."
    lis "*Gemido* Puedes..."
    scene c29s002_270c with dissolve
    $renpy.sound.play ("music/MoanLisa.ogg", loop=True)
    "Sabes lo que te va a pedir y no le dejas acabar la petición."
    lis "*GEMIDO* ...hacer exactamente eso..."
    mc "Lo sé."
    scene c29s002_885pv with dissolve
    show c29s002_885v
    "Empiezas a masajear su clítoris, duro y ardiente, haciendo movimientos circulares. Lentamente, incrementando y relajando la presión."
    lis "*Jadeo* ¡Maldición! *Gemido* ¡Creía que no ibas a hacerlo nunca! *Jadeo*"
    mc "He estado tentado de no hacerlo, por si era el whisky el que hablaba por ti."
    lis "*Gemido* Una sola botellita no iba a emborracharme. *Jadeo* No me has dejado beberme la otra. *Gemido*"
    "La erección en tus pantalones del pijama se está volviendo incómoda."
    lis "*Jadeo* Para, por favor. *Gemido*"
    scene c29s002_275a with fade
    hide c29s002_885v
    stop sound
    call BlinkXS4("c29s002_275") from _call_BlinkXS4_538
    "La chica vuelve a darse la vuelta, permitiéndote descubrir una pequeña línea que sube por su Monte de Venus."
    mc "¿Hay algo que no te esté gustando?"
    lis "No es eso... Si vamos a hacerlo, no quiero ser la única que se corra. Y quiero correrme contigo dentro."
    lis "Túmbate, por favor. Quiero tener el control para poder parar si duele mucho."
    mc "Como desees."
    scene c29s002_280a with fade
    call BlinkXS4("c29s002_280") from _call_BlinkXS4_539
    mc "¿Estoy bien aquí?"
    lis "Estarías perfecto si no llevases esos shorts."
    mc "Creo que es el momento de que trabajes un poco. *Risa* Yo te he desnudado a ti, te toca desnudarme a mí."
    lis "No voy a hacer que me lo repitas dos veces."
    scene c29s002_285An with dissolve
    "La princesa te desnuda e intenta disimular su sorpresa."
    call BlinkXS4("c29s002_290") from _call_BlinkXS4_540
    lis "Me habían dicho que era grande, pero no parece que sea para tanto, ¿no?"
    mc "*Risa* ¿Has visto las suficientes como para comparar?"
    call BlinkXS4("c29s002_295") from _call_BlinkXS4_541
    lis "*Risita* Aparte de en el porno y en los juegos de [deb.nick] no he visto ninguna."
    lis "Pero especialmente en esos juegos las hay que casi doblan tu tamaño."
    mc "Esos juegos son poco realistas..."
    if mc._var("relationships")>10:
        mc "Iba a poner como ejemplo los harenes con más de 10 chicas. *Risa* Pero mejor me callo."
    elif mc._var("relationships")>1:
        mc "Iba a poner como ejemplo los harenes. *Risa* Pero mejor me callo."
    else:
        mc "Iba a poner como ejemplo el pringado que vuelve a casa después de una temporada y descubre que es millonario. *Risa* Pero mejor me callo."
    call BlinkXS4("c29s002_300") from _call_BlinkXS4_542
    lis "*Risa* Sí, no es un buen ejemplo."
    mc "¿Cómo quieres hacerlo?"
    call BlinkXS4("c29s002_305") from _call_BlinkXS4_543
    lis "He leído sobre algunas posiciones que le dan el control a la mujer. Quiero probar algunas de ellas."
    mc "Cuando quieras. Sorpréndeme."
    scene c29s002_310a with fade
    "La chica se da la vuelta y apoya tu glande contra la entrada de su vagina."
    lis "¿Preparado?"
    mc "Puedes tomarte todo el tiempo que necesites. Mientras tanto, disfrutaré de las vistas."
    mc "¿Alguna vez te he dicho que me encanta tu culo?"
    lis "*Risita* Cuando me he ido a quitar la lencería y a ponerme el pijama. Y cuando me has quitado los pantalones."
    mc "No. Entonces te he dicho algo sobre un culo precioso y sobre la perfección hecha culo, pero no he dicho nada de lo mucho que me encanta."
    lis "¡No voy a discutir ahora por semántica!"
    scene c29s002_310b with vpunch
    "La perfección hecha culo baja unos centímetros, haciendo que el coño de [lis] engulla tu glande antes de pararse."
    lis "*Gemido* ¡Ooofff! *Jadeo*"
    mc "¿Estás bien?"
    lis "*Jadeo* Mejor de lo que esperaba. *Gemido* No ha dolido nada. *Jadeo*"
    mc "Eso es porque..."
    scene c29s002_310c with vpunch
    lis "*JADEO* ¡OOOFFF! *JADEO*"
    mc "... No has llegado al himen..."
    "Has podido notar cómo se rompía, pero ha sido una rotura suave, sin el ensordecedor y silencioso 'pop' al que estás acostumbrado."
    lis "*JADEO* Eso ha dolido un poco... *JADEO* Espero que cuando se rompa no duela mucho más. *JADEO*"
    mc "Ya se ha..."
    scene c29s002_310d with vpunch
    lis "*JADEO* ¡OOOFFF! *JADEO*"
    "La chica se empala hasta el fondo en Mjolnir con una facilidad asombrosa antes de que acabes la frase."
    if emm._var("route"):
        "Parece que ha leído las mismas técnicas sobre arrancarse la tirita que [emm]."
    mc "... Roto..."
    "Su coño, estrecho, caliente, y húmedo abraza a Mjolnir como si su vida dependiera de ello."
    call BlinkXS4("c29s002_315") from _call_BlinkXS4_544
    lis "¿Qué? ¿Ya está? ¿Eso es todo el dolor?"
    mc "Parece que sí. Hemos tenido suerte."
    call BlinkXS4("c29s002_320") from _call_BlinkXS4_545
    lis "*Risa nerviosa* Llevo días acojonada por esto y... ¿sólo esto?"
    if kim._var("route"):
        lis "Después de lo que me dijo [kim] sobre lo mucho que le había dolido..."
    else:
        lis "Después de lo que me dijo [sai] sobre lo mucho que le había dolido la primera vez..."
    mc "Cada chica es diferente, Princesa."
    call BlinkXS4("c29s002_325") from _call_BlinkXS4_546
    lis "¡[deb.nick] me ha hecho más daño muchas veces con sus pellizcos para que me callara!"
    mc "*Risa* No me imagino a [deb.nick] pellizcándote. Aunque tampoco me imaginaba a mi princesa tomando la iniciativa."
    lis "Voy a empezar a moverme. Dime si hago algo mal."
    mc "De momento, lo has hecho todo perfecto. Más que perfecto siendo tu primera vez."
    $renpy.sound.play ("music/MoanLisa.ogg", loop=True)
    scene c29s002_920pv with dissolve
    show c29s002_920v
    "La princesa empieza a moverse de una forma que nunca hubieras esperado de ella. Si no fuera por lo que acaba de hacer, te costaría creer que es su primera vez."
    lis "*GEMIDO* ¡SÍ! *JADEO*"
    "La estrechez de su coño y la excitación que te ha provocado el masaje hacen que estés a punto de explotar en sus primeros recorridos."
    lis "*JADEO* ¡MÁS! *GEMIDO*"
    "Con lo locuaz que suele ser [lis], esperabas más que monosílabos."
    scene c29s002_925pv with dissolve
    show c29s002_925v
    hide c29s002_920v
    "Pero ver su culo subir y bajar mientras su coño engulle tu polla como si se tratara de una mujer experta es hipnótico."
    lis "*GEMIDO* ¡OH, DIOS! *JADEO*"
    "Su coño, virgen hasta hace un momento, no deja de abrazar toda la longitud de tu polla mientras la chica experimenta un placer desconocido para ella."
    lis "*JADEO* ¡JODER! *GEMIDO*"
    "Crees que es la primera vez que escuchas la palabra en labios de [lis]. Esperas que sea una buena señal."
    scene c29s002_930pv with dissolve
    show c29s002_930v
    hide c29s002_925v
    "Te alegras de que [lis] no esté sintiendo casi ningún dolor en su primera vez. Claramente está disfrutándolo más de lo que esperaba."
    lis "*GEMIDO* ¡OH, SÍ! *JADEO*"
    "Y haciéndote disfrutar a ti de una forma que no esperabas debido a su inexperiencia. Su húmedo coño abraza tu astil en cada una de sus embestidas."
    lis "*JADEO* ¡INCREÍBLE! *GEMIDO*"
    "La palabra más larga que sale de su boca aparece cuando empieza a usar sus músculos pélvicos, como si lo hubiera recordado en ese momento."
    call BlinkXS4("c29s002_330") from _call_BlinkXS4_547
    lis "*Gemido* Déjame darme la vuelta... *Jadeo* Quiero probar otra posición antes de correrme. *Gemido*"
    mc "Puedes probar todas las posiciones que seas capaz de aguantar, Princesa."
    scene c29s002_940pv with fade
    show c29s002_940v
    hide c29s002_930v
    "Se da la vuelta y te vuelve a cabalgar. Esta chica te sigue sorprendiendo con su iniciativa."
    lis "*GEMIDO* ¡ME GUSTA! *JADEO*"
    "Tienes que hacer más trabajo que en la posición anterior, al no tener ella tanto punto de apoyo. No te importa lo más mínimo tener que hacer algo."
    lis "*JADEO* ¡FÓLLAME! *GEMIDO*"
    "Ella tiene suficiente con evitar que sus tetas aplasten tu cara."
    scene c29s002_935pv with fade
    show c29s002_935v
    hide c29s002_940v
    "En esta posición, con sus piernas totalmente abiertas, todavía notas la extrema estrechez de su húmedo túnel del amor."
    lis "*GEMIDO* ¡SÍ! *JADEO*"
    "Está siendo alucinante teniendo en cuenta que hace 15 minutos la princesa era virgen."
    lis "*JADEO* ¡QUIERO MÁS! *GEMIDO*"
    "Aún no lo sabes, pero el sexo con ella no hará más que mejorar con el tiempo."
    scene c29s002_945pv with fade
    show c29s002_945v
    hide c29s002_935v
    "Es vuestra primera vez juntos y ya estáis compenetrados como si hubierais tenido sexo decenas de veces antes."
    lis "*GEMIDO* ¡TE QUIERO! *JADEO*"
    "[lis] tiene un talento natural para esto que no podías imaginarte."
    mc "Yo también te quiero."
    "Su coño se cierra con fuerza sobre Mjolnir por el placer de escucharte decir esas palabras."
    scene c29s002_890pv with fade
    show c29s002_890v
    hide c29s002_945v
    "Sus tetas casi abofetean tu cara en cada uno de sus movimientos, regalándote una visión tan hipnótica como la de antes con su culo."
    lis "*GEMIDO* ¡CREO QUE ME HE CORRIDO 50 VECES YA! *JADEO*"
    "Te sorprende su frase. No sólo por la longitud de ésta, sino porque no has notado nada que te indique que se haya corrido."
    "No ha habido un aumento del volumen de los gemidos, aunque dudas de que puedan ser más altos, ni has notado cómo se tensaba más antes de explotar."
    "Cada mujer es diferente, pero si es verdad que [lis] se ha corrido 50 veces, significa que ella es MUY diferente de las demás."
    call BlinkXS4("c29s002_335") from _call_BlinkXS4_548
    lis "*JADEO* Cambiemos de posición otra vez. *GEMIDO* Quiero verte la cara cuando me vuelvas a llenar. *JADEO*"
    mcp "(¿QUÉ? ¿Volverla a llenar?)"
    mc "¿Volverte a llenar?"
    lis "*GEMIDO* Cuando te vuelvas a correr. *JADEO*"
    mc "[lis], aún no me he corrido..."
    call BlinkXS4("c29s002_340") from _call_BlinkXS4_549
    lis "*JADEO* ¿QUÉ? *GEMIDO* Habría jurado que... *JADEO*"
    mc "No, [lis]. Pero ese cambio de posición parece una gran idea."
    mc "Yo también quiero mirarte a los ojos cuando me corra, por mucho que me guste mirar tus tetas botando sobre mi pecho."
    scene c29s002_905pv with fade
    show c29s002_905v
    hide c29s002_945v
    "Tras unos ajustes en la postura, la princesa se vuelve a empalar en Mjolnir y continúa cabalgándote."
    lis "*GEMIDO* ¡ASÍ! *JADEO*"
    "Vuelve a los monosílabos, abrumada por el placer que siente en esta nueva postura."
    lis "*JADEO* ¡SÍ! *GEMIDO*"
    "Se penetra profundamente en cada uno de sus recorridos mientras usa el suelo pélvico para atrapar tu polla entre sus paredes."
    scene c29s002_900pv with fade
    show c29s002_900v
    hide c29s002_905v
    "Y, al final de cada uno de sus movimientos, puedes notar cómo impactas en la boca de su útero."
    lis "*GEMIDO* ¡DUELE! *JADEO* ¡PERO DOLOR BUENO! *GEMIDO*"
    "Sabes que es la primera vez que su cérvix recibe cualquier tipo de impacto, y con lo bruscos que son sus movimientos, el impacto no es suave."
    lis "*JADEO* ¡SIGUE! *GEMIDO*"
    "[lis] puede ser muchas cosas, pero definitivamente delicada en el sexo no es una de ellas."
    scene c29s002_910pv with fade
    show c29s002_910v
    hide c29s002_900v
    "Pero mientras os podáis adaptar al ritmo del otro, nada importa. Tan solo que ambos estéis disfrutando de vuestro primer encuentro."
    lis "*GEMIDO* ¡ME ENCANTA! *JADEO* ¡QUIERO MÁS! *GEMIDO*"
    "Esperabas algo más romántico en tu primera vez con la princesa, y más aún después de sus dudas, pero es una sorpresa bienvenida."
    lis "*JADEO* ¡ALUCINANTE! *GEMIDO*"
    "Vuestras sesiones sexuales cambiarán y se adaptarán con el tiempo y las circunstancias, pero [lis] nunca perderá la insaciabilidad."
    scene c29s002_915pv with fade
    show c29s002_915v
    hide c29s002_910v
    "Los descubrimientos que hagáis sobre el cuerpo del otro en los próximos años irán cambiando vuestra forma de hacer el amor."
    lis "*GEMIDO* ¡OH, DIOS! *JADEO*"
    "Los descubrimientos que [lis] está a punto de hacer sobre su propio cuerpo la cambiarán para siempre."
    mc "Estoy a punto de correrme, [lis]."
    "La chica no hace ningún movimiento para desempalarse de Mjolnir. Si realmente pensaba que ya te habías corrido..."
    lis "*JADEO* ¡LLÉNAME! *GEMIDO*"
    if persistent.pregnancy:
        if persistent.walkthrough:
            $ wt1 = _("[lis] embarazada.")
            $ wt2 = _("Sin consecuencias.")
        else:
            $ wt1 = ""
            $ wt2 = ""
        menu:
            "Correrte dentro. Ir a por el bebé." (wt = wt1):
                $ lis._var("pregnant", True)
                $ lis._var("undiscoveredPregnancy", True)
                play sound ("music/OldMusicBox5.ogg")
            "Correrte dentro." (wt = wt2):
                pass
    $ resetWalkthrough ()
    call OrgasmXS4("c29s002_345") from _call_OrgasmXS4_17
    mc "¡Mpfft!"
    $renpy.sound.play ("music/MoanLisa.ogg", loop=True)
    "Descargas una gran cantidad de tu semilla en el interior de la princesa, tomándola por sorpresa."
    lis "*GEMIDO* ¡ESTÁ CALIENTE! *JADEO*"
    scene c29s002_345d with hpunch
    "Por fin entiende que no te habías corrido. No sabes qué es lo que había notado, pero ahora descubre cómo se siente cuando te corres dentro de ella."
    lis "*JADEO* ¿QUÉ? *GEMIDO*"
    "Su cuerpo se tensa en un momento antes de explotar."
    call OrgasmXS4("c29s002_350") from _call_OrgasmXS4_18
    lis "*GEMIDO* ¡OH, DIOS MIO! *JADEO* ¿QUÉ ME ESTÁ PASANDO? *GEMIDO*"
    "En esta ocasión puedes notar cómo un potentísimo orgasmo recorre su cuerpo, haciendo que vibre entre tus brazos."
    lis "*JADEO* ¡ESTO ES INCREÍBLE! *GEMIDO*"
    scene c29s002_355An with dissolve
    "Se queda quieta, sin moverse, pero disfrutando de cada una de las oleadas que la recorren de arriba a abajo."
    "Sin retirar su mirada de tus ojos."
    "Su rostro muestra el placer que está notando por primera vez en su vida."
    stop music fadeout (1.5)
    scene c29s002_360a with fade
    call BlinkXS4("c29s002_360") from _call_BlinkXS4_550
    stop sound fadeout (1.5)
    "Al cabo de un rato, cuando recupera el control sobre los músculos de su cuerpo y especialmente de su cara..."
    play music ("music/Stardust.ogg")
    lis "*Gemido* ¿Qué demonios ha sido eso? *Jadeo*"
    mc "¿Lo mío o lo tuyo? Lo mío ha sido una corrida. Ya te había dicho que no había llegado todavía."
    call BlinkXS4("c29s002_365") from _call_BlinkXS4_551
    lis "*Jadeo* ¿Pero lo mío...? *Gemido* ¡Nunca había sentido algo así! *Jadeo*"
    mc "Eso ha sido un orgasmo..."
    call BlinkXS4("c29s002_370") from _call_BlinkXS4_552
    lis "*Risa* No me tomes por idiota, [mc]. Sé cómo es un orgasmo."
    lis "Son las pequeñas punzaditas de placer que siento cuando... juego conmigo misma... He tenido decenas mientras... follábamos."
    mc "¿Nunca has llegado a algo como esto?"
    call BlinkXS4("c29s002_375") from _call_BlinkXS4_553
    lis "¡No! Lo que tenía era 100 veces más pequeño..."
    mc "Creo que parabas de jugar contigo misma bastante antes de llegar al orgasmo, Princesa."
    call BlinkXS4("c29s002_380") from _call_BlinkXS4_554
    lis "¿QUÉ?"
    mc "*Risa* Creo que has tenido el primer orgasmo de tu vida."
    mc "¿Nunca habías hablado de esto con nadie?"
    call BlinkXS4("c29s002_385") from _call_BlinkXS4_555
    lis "¡Claro que sí!"
    mc "¿Y nunca has descrito tus orgasmos a alguien? ¿Tu hermana o alguna amiga?"
    lis "¡Por supuesto que no! ¡No tenía con qué compararlos!"
    mc "*Risa* Pues me alegra que el primer orgasmo de tu vida haya sido conmigo."
    scene c29s002_385d with dissolve
    "Ella también se alegra. Se alegra mucho. Acaba de descubrir todo un horizonte nuevo sobre lo que pueden ser las relaciones sexuales. Y le encanta."
    "No te extraña que tuviera miedo al dolor al hacerlo la primera vez si el 'premio' era lo que ella esperaba. Mucho dolor para poca recompensa."
    "Ahora que ha descubierto cómo es el jackpot, el miedo no volverá a hacer su aparición."
    call BlinkXS4("c29s002_390") from _call_BlinkXS4_556
    lis "Yo también me alegro. No me alegro de haber sido una idiota que no sabía cómo hacerse un dedo, pero..."
    lis "Me alegra que un orgasmo sea esto y de haberlo descubierto contigo. No me extraña que la gente se vuelva adicta al sexo si cada vez es así."
    mc "Entonces, doy por sentado que te ha gustado tu primera vez."
    call BlinkXS4("c29s002_395") from _call_BlinkXS4_557
    lis "¿Gustarme? ¡Ha sido lo más alucinante que he experimentado en mi vida!"
    lis "Pero es agotador..."
    mc "Has hecho tú casi todo el trabajo. Lo ideal es que nos lo repartamos."
    call BlinkXS4("c29s002_400") from _call_BlinkXS4_558
    lis "No me refiero a eso. Ha sido el orgasmo... Siento como si me hubiera atropellado un camión..."
    mc "Cuando son intensos pueden tener ese efecto. Lo que me ha sorprendido es que tardaras tanto en llegar."
    call BlinkXS4("c29s002_405") from _call_BlinkXS4_559
    lis "Supongo que era una barrera mental. Para mí, aunque parezca idiota, me llevaba corriendo un rato..."
    lis "Pero cuando he notado tu descarga caliente dentro de mí... Ha sido como si mi cuerpo tomase el control."
    lis "Como si me dijera 'Quita de aquí, tonta del culo. Déjame tomar los mandos'. No sabía qué me estaba pasando."
    mc "*Risa* Tienes un cuerpo muy hablador."
    call BlinkXS4("c29s002_410") from _call_BlinkXS4_560
    lis "Y, ahora mismo, totalmente agotado. Creo que el whisky de antes ha sido lo que ha bajado mis barreras para permitirle tomar el control."
    lis "Y ahora lo está pagando. Si bebes no conduzcas..."
    mc "¿Quieres dormir?"
    call BlinkXS4("c29s002_415") from _call_BlinkXS4_561
    lis "Quiero abrazarme a ti hasta que me quede dormida."
    mc "Esa es una de las partes que más me gustan del sexo. Los abrazos de después. ¿Hace falta que nos pongamos los pijamas otra vez?"
    lis "No. Creo que no vas a volver a usar un pijama cuando duermas conmigo. Nunca más."
    scene c29s002_415d with dissolve
    "[lis] vuelve a bajar la intensidad de las luces y se acurruca a tu lado en la misma posición que unas horas antes."
    "No necesitas verla para notar cómo sonríe hasta quedarse dormida."
    scene black with dissolve
    "Poco después, te quedas dormido tú también."
    stop music fadeout (1.5)
    scene c29s002_160e with fade
    "Otra vez te vuelves a despertar notando que la princesa no está en la cama contigo."
    play music ("music/Rise-Up.ogg")
    "Parece que has vuelto a buscarla mientras dormías y te has vuelto a despertar al notar su ausencia."
    scene c29s002_415e with dissolve
    "Todavía es muy pronto."
    scene c29s002_415f with dissolve
    "Esta vez la puerta del lavabo está cerrada."
    mc "¿[lis]?"
    lis "*Desde el lavabo* Estoy en el lavabo. Me iba a duchar."
    mc "¿Puedo ir a buscar mi beso de buenos días?"
    lis "*Desde el lavabo* *Risita* Me sentiría ofendida si no lo hicieras."
    scene c29s002_420d with fade:
        yalign 1.0
        linear 5.0 yalign 0.0
    pause (4.8)
    call BlinkXS3("c29s002_420") from _call_BlinkXS3_779
    mc "No sé por qué, pero me imaginaba que estarías con una toalla alrededor del cuerpo"
    call addProfileImageS3 (8, "lis_8", lis, __(": 15 - Especial"), "") from _call_addProfileImageS3_24
    lis "¿Qué sentido tiene? Ya me has visto desnuda y hemos follado. Siempre me ha parecido ridículo en las películas."
    lis "Aunque entiendo que es por un tema de audiencia y ratings."
    mc "Bueno, yo venía a por mi beso."
    call BlinkXS4("c29s002_425") from _call_BlinkXS4_562
    lis "Pues puedes venir aquí a recibirlo. No estarás esperando a que vaya yo, ¿verdad?"
    mc "No, pero es que me he quedado anonadado al verte así. Eres super sexy."
    scene c29s002_425d with dissolve
    "Entras en la ducha y coges a la princesa en brazos antes de atrapar sus labios entre los tuyos."
    "Te devuelve el beso apasionadamente. Cualquier barrera que existiera fue derribada ayer y no le importa que estéis desnudos mientras os besáis."
    call BlinkXS4("c29s002_430") from _call_BlinkXS4_563
    lis "*Risita* Me podría acostumbrar a desayunar besos."
    mc "*Risa* Es una buena forma de despertarse."
    mc "¿Cómo estás después de lo de anoche?"
    call BlinkXS4("c29s002_435") from _call_BlinkXS4_564
    lis "¿Después de lo de hace unas horas? Mejor de lo esperado."
    if deb._var("route"):
        lis "[deb.nick] me dijo que estaría dolorida y resentida, pero no me duele absolutamente nada."
    else:
        lis "[sai] me dijo que estaría dolorida y resentida, pero no me duele absolutamente nada."
    mc "Ya te dije que cada chica es diferente."
    scene c29s002_440a with dissolve #Prince Charming 17
    mc "Pues voy a dejar que mi princesa se duche con tranquilidad. Aún es pronto."
    lis "*Risa* Muy galante por tu parte. Quería ducharme y maquillarme antes de que te despertaras. Llevo pelos de loca..."
    mc "Voy a hacer como que no te he oído. Estás preciosa, Princesa."
    scene c29s002_440b with dissolve #ella Prince Charming 12
    lis "*Risita* Pero a la realeza se le besa la mano, no solo se le hace una reverencia."
    mc "*Risa* ¿No crees que estás abusando?"
    lis "*Risa* Nope."
    scene c29s002_440c with dissolve #él Prince Charming 12
    mc "¿Mejor ahora?"
    lis "Mucho mejor."
    scene c29s002_440d with dissolve #coño
    lis "*Risa* Pero mis ojos están aquí arriba..."
    mc "Lo sé, pero ayer no tuve tiempo de comprobar lo perfecto que es el afeitado. *Risa* O, para ser más exactos, estaba demasiado ocupado como para comprobarlo."
    lis "*Risa* Puedes mirarlo todo lo que quieras siempre y cuando no acerques las manos... Aún me tengo que duchar."
    stop music fadeout (1.5)
    mc "¿Quién ha dicho nada de las manos?"
    scene c29s002_440e with hpunch #comida
    play music ("music/Sexy-Background-Music.ogg")
    "Hundes tu cara entre sus piernas, rozando suavemente su clítoris con la lengua."
    $renpy.sound.play ("music/MoanLisa.ogg", loop=True)
    lis "*GEMIDO* ¡JODER! *JADEO* ¡Me ha recorrido un escalofrío de arriba a abajo! *GEMIDO*"
    scene c29s002_440f with dissolve #la mira
    mc "¿Un escalofrío bueno o uno malo?"
    lis "*Jadeo* ¡Uno buenísimo! *Gemido* ¿Quién te ha dicho que podías parar, campesino? *Jadeo*"
    mc "Lo siento, su alteza. Al decirme que aún te tenías que duchar, pensaba que..."
    lis "*Gemido* ¡Pues no pienses y vuelve ahí! *Jadeo*"
    scene c29s002_445An with dissolve
    "La giras para que apoye su espalda contra el cristal de la ducha mientras vuelves a hundir tu cara entre sus piernas."
    lis "*JADEO* ¡POR EL AMOR DE DIOS! *GEMIDO*"
    "Ya está húmeda nada más empezar a lamer. La anticipación es una perra mala."
    lis "*GEMIDO* ¿POR QUÉ NO HICIMOS ESTO ANOCHE? *JADEO*"
    "Casi se te escapa la risa al pensar en lo que hubiera dicho la [lis] de antes del whisky si lo hubieras intentado."
    lis "*JADEO* Ven aquí arriba. *GEMIDO* Quiero besarte y quiero que me folles. *JADEO*"
    scene c29s002_450a with dissolve
    "Te levantas a regañadientes. Creías que ibas a poder llevarla al orgasmo antes de levantarte."
    "La reluctancia desaparece en el momento en que sus labios tocan los tuyos."
    lis "*Gemido*"
    "Los pocos lengüetazos que has sido capaz de propinarle han sido suficientes para ponerla cachonda."
    "Sus gemidos en tu boca acaban de endurecer a Mjolnir, que ya estaba presentando sus respetos a la realeza."
    scene c29s002_450b with dissolve #oído
    lis "Te quiero dentro de mí..."
    mc "Mi princesa se ha levantado traviesa."
    lis "Puedo ser una princesa en público y una chica traviesa en privado."
    mc "Me encanta eso de ti."
    scene c29s002_455a with dissolve
    "Doblas un poco las rodillas y apoyas tu glande sobre su caliente raja. Ella se tiene que poner de puntillas para facilitar la postura."
    lis "*Gemido* No me hagas sufrir más. *Jadeo* Te quiero dentro. *Gemido*"
    mc "¿Poco a poco?"
    scene c29s002_950pv with hpunch
    "Introduces tu glande en el húmedo agujero, atento a cualquier señal de malestar por su parte después de lo de anoche."
    lis "*GEMIDO* ¡OOOFFF! *JADEO* ¡MÁS! *GEMIDO*"
    "Parece que [lis] se ha levantado insaciable después de descubrir cómo es un orgasmo de verdad. No hay señales de incomodidad."
    scene c29s002_455b with hpunch
    "Con un golpe de cadera metes todo Mjolnir en el interior de la chica. El abrazo de su coño es fuerte y húmedo. Sigue siendo tan estrecho como anoche."
    lis "*JADEO* ¡SÍ! *GEMIDO* ¡SIGUE! *JADEO*"
    "Discutir con Su Alteza en estos momentos no forma parte de tus planes. El momento de ir poco a poco ha quedado atrás."
    scene c29s002_950pv with fade
    show c29s002_950v
    hide c29s002_915v
    "Empiezas a embestir con tus caderas mientras hundes tus labios donde su cuello se junta con su clavícula y empiezas a repartir besos."
    lis "*GEMIDO* ¡JODER! *JADEO*"
    "La postura dista de ser cómoda por la diferencia de alturas, pero a ninguno de los dos parece importaros."
    lis "*JADEO* ¡LA SEGUNDA VEZ ES AÚN MEJOR! *GEMIDO*"
    "La segunda vez ella tan solo tiene que hacer el esfuerzo de mantenerse de pie mientras tú haces todo el trabajo."
    scene c29s002_955pv with fade
    show c29s002_955v
    hide c29s002_950v
    "Además, ya no hay miedo. Tan solo ansia por disfrutar del placer compartido."
    "Esperas que el cristal de la ducha esté bien anclado, ya que la espalda de [lis] apoyada sobre él hace que se mueva violentamente con cada una de tus embestidas."
    lis "*GEMIDO* ¡INCREÍBLE! *JADEO*"
    "No te extrañaría que el cristal se empañara por lo tórrido de la situación sin necesidad de abrir el grifo."
    "Es increíble cómo vuestros cuerpos se adaptan el uno al otro tan solo unas horas después de que la chica haya perdido su virginidad."
    scene c29s002_960pv with fade
    show c29s002_960v
    hide c29s002_955v
    lis "*JADEO* ¡NO PUEDE SER! *GEMIDO*"
    "No sabes a qué se refiere, pero puedes imaginártelo. Su cuerpo se ha empezado a tensar indicando la rápida llegada de su primer orgasmo."
    "¿Será multiorgásmica también [lis]? Una vez derribadas las barreras mentales que tenía, esta chica puede sorprenderte con cualquier cosa."
    lis "*GEMIDO* ¡ESTOY A PUNTO DE CORRERME! *JADEO*"
    "Tu intuición no te ha fallado. Debes tener un sexto sentido para detectar cuándo un orgasmo está llegando."
    call OrgasmXS4("c29s002_460") from _call_OrgasmXS4_19
    lis "*JADEO* ¡JODER, JODER, JODER! *GEMIDO*"
    "La chica que raramente juraba suelta tres tacos en rápida sucesión en el momento en que su orgasmo matutino hace su aparición."
    lis "*GEMIDO* ¡SIGUE! *JADEO*"
    "Anoche llegó al orgasmo justo después de ti y la sorpresa hizo que ahí acabara el polvo. Hoy quiere alargarlo lo máximo posible."
    scene c29s002_950pv with fade
    show c29s002_950v
    hide c29s002_960v
    "Continúas bombeando mientras intentas prolongar el primer orgasmo de [lis]. No sabes si será el último."
    lis "*JADEO* ¡OH, DIOS MÍO! *GEMIDO*"
    "Su cuerpo tiembla alrededor de Mjolnir. Tus labios siguen repartiendo besos. Tu orgasmo aún está lejos."
    lis "*GEMIDO* ¡LAS PIERNAS NO ME AGUANTAN! *JADEO*"
    "Estar de puntillas mientras la embistes con tu ariete no es una posición cómoda pese a que tiene apoyada la espalda contra el cristal."
    call BlinkXS4("c29s002_465") from _call_BlinkXS4_565
    "Detienes tus embestidas y la miras a los ojos. Esos ojos que podrían volver loco a cualquier hombre."
    mc "¿Quieres que vayamos a la cama?"
    lis "*Gemido* No. *Jadeo* Quiero ver cómo me follas. *Gemido*"
    stop sound fadeout (1.5)
    "Crees que en ningún momento ha hablado de hacer el amor. Te da lo mismo."
    scene c29s002_465d with dissolve #prince charming 14
    "[lis] se desempala de Mjolnir y te dirige de la mano hacia fuera de la ducha."
    lis "Ven al espejo."
    mc "*Risa* Me gusta la faceta de chica traviesa."
    scene c29s002_470a with fade
    call BlinkXS4("c29s002_470") from _call_BlinkXS4_566
    lis "Aquí está bien. Quiero verte, pero quiero saber si pongo las mismas caras que [sai] dice que pone."
    mc "*Risa* No las pones. Y las caras de [sai] son muy graciosas."
    if sai._var("route"):
        call BlinkXS4("c29s002_475") from _call_BlinkXS4_567
        lis "No sé si es muy correcto que hablemos de una de tus otras chicas ahora..."
        mc "Has sido tú quién ha sacado el tema, no yo. Además, ahora mismo solo hay una chica que me importe."
        call BlinkXS4("c29s002_470") from _call_BlinkXS4_568
        lis "*Risita* Tienes razón..."
    lis "Bueno, me dan lo mismo las caras de [sai] ahora mismo. Te estoy esperando; me siento vacía sin notar a Mjolnir dentro."
    $renpy.sound.play ("music/MoanLisa.ogg", loop=True)
    scene c29s002_970pv with dissolve
    show c29s002_970v
    hide c29s002_950v
    "Por un momento piensas que, tal y como ha construido la frase, parece que se refiera a un vacío existencial."
    "Afortunadamente no lo es y puedes llenar su vacío físico. Y empiezas a embestir nada más llenarlo."
    lis "*JADEO* ¡ME ENCANTA! *GEMIDO*"
    "A ti también. Está siendo una noche sorprendente... aunque ya haya amanecido."
    "Las sorpresas de [lis] y cómo está disfrutando del sexo en su primera vez le han dado a la noche un componente que no esperabas."
    scene c29s002_985pv with dissolve
    show c29s002_985v
    hide c29s002_970v
    "No puedes dejar de admirar lo estrecho que es el coño de [lis] después de todo el sexo que habéis tenido en las últimas horas."
    lis "*GEMIDO* ¡MÁS PROFUNDO! *JADEO*"
    "Al menos ha recuperado la capacidad de decir palabras de más de una sílaba, aunque eso te sorprende algo menos."
    lis "*JADEO* ¡SÍ! *GEMIDO*"
    "Parece que, en esta postura, mucho más cómoda para ella que la de la ducha, las piernas le aguantan mucho mejor."
    scene c29s002_990pv with dissolve
    show c29s002_990v
    hide c29s002_985v
    "Con tus manos apoyadas en su fantástico culo mientras Mjolnir bombea en su coño te preguntas qué fetiches descubrirá la princesa que tiene."
    "Si es que tiene alguno. Incluso te preguntas cuándo los descubrirá. ¿Será antes de que te vayas a Aruba?"
    lis "*GEMIDO* ¡ESTÁ LLEGANDO OTRO! *JADEO*"
    "Sabes que está sensible después de lo que pasó antes de dormir y de lo que habéis hecho en la ducha, pero no te podías imaginar que llegaría tan rápido."
    "Al menos ya has resuelto la duda sobre si sería multiorgásmica."
    call OrgasmXS4("c29s002_480") from _call_OrgasmXS4_20
    lis "*JADEO* ¡ES MÁS GRANDE QUE EL DE ANTES! *GEMIDO*"
    "Su voz denota una gran sorpresa mientras su cara denota un placer intenso. El mismo placer que te provoca notar cómo sus paredes se cierran sobre Mjolnir."
    "Sonríes para ti mismo por la alegría que sientes por haberle enseñado cómo se siente un orgasmo de verdad."
    scene c29s002_995pv with dissolve
    show c29s002_995v
    hide c29s002_990v
    "Continúas bombeando, buscando el tuyo."
    "Puedes percibir cómo va trepando por tus pantorrillas, en una familiar y bienvenida sensación."
    lis "*JADEO* ¡ADORO ESTA SENSACIÓN! *GEMIDO*"
    "Sus paredes vaginales se cierran con fuerza sobre Mjolnir por un instante, como si..."
    lis "*GEMIDO* ¡CAMBIA DE AGUJERO! *JADEO* ¡ESTÁ EMPEZANDO A DOLER UN POCO! *GEMIDO*"
    "Otra pregunta resuelta. Parece que el sexo anal está entre sus fetiches."
    if persistent.walkthrough:
        $ wt1 = _("Anal activado con [lis].\n Corrida en su culo o en su espalda.")
        $ wt2 = _("Anal desactivado con [lis].\n Corrida en su coño o en su espalda.")
    else:
        $ wt1 = ""
        $ wt2 = ""
    menu:
        "Cambiar de agujero." (wt = wt1):
            $ lis._var("anal", True)
        "No hacerlo." (wt = wt2):
            $ lis._var("anal", False)
            "Sin embargo, su petición llega tarde, ya que estás a punto de explotar."
            if persistent.pregnancy:
                if persistent.walkthrough:
                    $ wt1 = _("[lis] embarazada.")
                    $ wt2 = _("Sin consecuencias.")
                else:
                    $ wt1 = ""
                    $ wt2 = ""
                menu:
                    "Correrte dentro. Ir a por el bebé." (wt = wt1) if not lis._var("pregnant"):
                        $ lis._var("pregnant", True)
                        $ lis._var("undiscoveredPregnancy", True)
                        play sound ("music/OldMusicBox5.ogg")
                        call c29s002_pussy from _call_c29s002_pussy
                    "Correrte dentro." (wt = wt2):
                        call c29s002_pussy from _call_c29s002_pussy_1
                    "Correrte en su espalda." (wt=wt2):
                        call c29s002_back from _call_c29s002_back
            $ resetWalkthrough ()
    $ resetWalkthrough ()
    if lis._var("anal"):
        scene c29s002_485An1 with dissolve
        "Sacas tu polla de su coño y aprietas tu glande contra su ano, indicándole que vas a entrar."
        lis "*JADEO* Adelante. *GEMIDO*"
        "Ese 'Adelante' ha sonado más dubitativo de lo que te hubiera gustado."
        mc "Intenta relajarte."
        "Pero no es el momento de preguntarle si está segura."
        scene c29s002_485c with dissolve
        "Introduces la punta de Mjolnir lo suficiente como para que desaparezca. Continúas pendiente de si le haces daño."
        lis "*GEMIDO* ¡OOOFFF! *JADEO* Sólo ha sido la punta, ¿no? *GEMIDO*"
        mc "Sí, [lis]. Puedo parar si duele."
        lis "*Jadeo* No te preocupes. *Gemido* Es raro, pero no duele. *Jadeo* Sigue. *Gemido*"
        "O esta chica tiene una resistencia inusitada al dolor o hay algo que no entiendes. Su agujero es estrechísimo."
        scene c29s002_485d with dissolve
        "Metes tu polla hasta la mitad, esperando que en algún momento se queje por el dolor. No lo hace."
        lis "*GEMIDO* ¡Mmmmm! *JADEO* ¿Ya está toda? *GEMIDO*"
        mc "La mitad, más o menos. Puedo esperar a que te acostumbres."
        lis "*Jadeo* No hace falta. *Gemido* Puedes empezar a moverte. *Jadeo*"
        "Si hasta ahora creías que [lis] te había sorprendido, es el momento en el que tu mandíbula podría tocar tus rodillas, si no fuera porque su perfecto culo está en medio."
        scene c29s002_975pv with dissolve
        show c29s002_975v
        hide c29s002_995v
        "Empiezas a bombear, casi reluctantemente, preparado para parar cuando aparezca el dolor."
        "No parece que vaya a hacer su aparición. [lis] aprieta su esfínter aún más, mostrándote que había seguido tu consejo sobre relajarse."
        lis "*GEMIDO* ¡ALUCINANTE! *JADEO* CREO QUE ME PODRÍA CORRER HACIENDO ESTO. *GEMIDO*"
        "Definitivamente tiene un fetiche. Y si no lo tenía, lo tendrá cuando salgáis del lavabo."
        "Cada cosa que habéis probado le ha gustado. No podrías estar más contento por los descubrimientos que está haciendo sobre su cuerpo."
        scene c29s002_965pv with dissolve
        show c29s002_965v
        hide c29s002_975v
        "Casi la misma posición que hace unos minutos, tan solo cambiando el agujero y el ángulo necesario. Mismo placer en un agujero aún más estrecho que el anterior."
        lis "*JADEO* ¡ME ENCANTA! *GEMIDO*"
        "Los quejidos no hacen aparición, y dudas que el volumen de los gemidos pueda subir más. Compadeces a los huéspedes de la habitación de al lado."
        lis "*GEMIDO* ME GUSTA MÁS DE LA OTRA FORMA. *JADEO* PERO ESTO ES GENIAL TAMBIÉN. *GEMIDO*"
        "Si es capaz de articular frases completas mientras aprisiona a Mjolnir con dentro de su culo, significa que es algo menos bueno para ella."
        scene c29s002_980pv with dissolve
        show c29s002_980v
        hide c29s002_965v
        "Tu orgasmo, retrasado por el cambio de agujero, vuelve a trepar por tus pantorrillas otra vez, como diciendo, 'Ahí voy. Prepárate'."
        "Sí, a veces parece que los orgasmos hablen."
        lis "*JADEO* ¡ESTOY A PUNTO! *GEMIDO* ¡NO ME LO PUEDO CREER! *JADEO*"
        "Tú tampoco. Otra sorpresa más para la noche. Justo cuando creías que no estaba siendo tan bueno para ella."
        "Esperas que te sorprenda durante mucho tiempo."
        call OrgasmXS4("c29s002_490") from _call_OrgasmXS4_21
        lis "*GEMIDO* ¡JODER, SÍ, JODER! *JADEO*"
        "La princesa explota en un nuevo orgasmo en el que puedes notar cómo ha mojado tus piernas."
        "¿También esquirtea? ¿Va a sorprenderte con algo más?"
        scene c29s002_970pv with dissolve
        show c29s002_970v
        hide c29s002_980v
        "Continúas embistiendo, notando que tu clímax ya ha llegado a tus muslos."
        "El instinto animal hace que quieras acelerar. Tu parte racional te pide que no lo hagas. No quieres que [lis] tenga que volver de pie en el helicóptero."
        lis "*JADEO* ¡SÍ! *GEMIDO* ¡ALUCINANTE! *JADEO*"
        "Al menos no te ha sorprendido pensando que se había meado. Si confundía lo que fuera que experimentaba con orgasmos te puedes esperar cualquier cosa."
        "Tu orgasmo llega a tu culo. Es el momento de tomar una decisión."
        if persistent.walkthrough:
            $ wt1 = _("[lis] embarazada.")
            $ wt2 = _("Sin consecuencias.")
        else:
            $ wt1 = ""
            $ wt2 = ""
        menu:
            "Correrte dentro." (wt = wt2):
                call c29s002_ass from _call_c29s002_ass
            "Correrte en su espalda." (wt=wt2):
                call c29s002_back from _call_c29s002_back_1
        $ resetWalkthrough ()
    scene c29s002_510a with fade
    stop music fadeout (1.5)
    stop sound fadeout (1.5)
    call BlinkXS4("c29s002_510") from _call_BlinkXS4_569
    lis "Eso ha sido alucinante... Siempre había creído que era multiorgásmica, pero después de descubrir lo de antes de dormir..."
    play music ("music/romantic-day.ogg")
    mc "No estabas tan segura, ¿no?"
    call BlinkXS4("c29s002_520") from _call_BlinkXS4_570
    lis "Exacto... Pero tener todos esos orgasmos..."
    if lis._var("anal"):
        lis "Y tener más cuando te estabas follando mi culo..."
    lis "Ha sido increíble... Creo que me he vuelto adicta a ti."
    mc "Yo soy adicto a ti desde aquel beso en tu habitación."
    call BlinkXS4("c29s002_530") from _call_BlinkXS4_571
    lis "Pues ahora te voy a mandar a nuestra habitación. Me quiero duchar y no quiero que estés cerca."
    lis "Estoy medio dolorida... Con lo que no te vas a acercar a mí en un rato."
    mc "¿Duele más que anoche?"
    call BlinkXS4("c29s002_535") from _call_BlinkXS4_572 #sorprendida
    lis "¡Oh! Creo que me he explicado mal. Lo que me duele son las piernas."
    lis "Lo de estar de puntillas en la ducha me ha dejado un poco dolorida. Me voy a dar un masaje en las piernas con la alcachofa de la ducha."
    mc "*Risa* Y supongo que no prefieres que yo te dé el masaje en la cama."
    call BlinkXS4("c29s002_540") from _call_BlinkXS4_573
    lis "*Risa* Si me das un masaje en la cama, sé cómo vamos a acabar. Y aún tenemos que ducharnos, desayunar, y llegar a tiempo al helicóptero."
    mc "Bueno, yo sería capaz de saltarme la ducha y el desayuno, podríamos hacerlo en casa. Pero el helicóptero..."
    call KissXS4("c29s002_545") from _call_KissXS4_8
    call BlinkXS4("c29s002_545") from _call_BlinkXS4_574
    lis "Exacto. El helicóptero no esperará por nosotros. Con lo que te toca irte. Voy a echar de menos los abrazos de después del sexo."
    mc "Siempre podemos ir abrazados en el helicóptero, aunque no sea lo mismo."
    lis "Dudo que algo sea lo mismo después de lo de hoy. Ha sido la mejor noche de mi vida. ¡Tengo el mejor novio del mundo!"
    mc "*Risa* Un novio al que echas del lavabo."
    scene black with dissolve
    "No quieres entretenerla más y te vas a la habitación a esperar a que termine de ducharse."
    "Tras ducharte y vestiros (por suerte [lis] empieza a vestirse mientras te duchas y aún así acaba más tarde que tú), bajáis a desayunar al restaurante del hotel."
    "Casi parecería una luna de miel."
    "El hotel se encargará de enviar las maletas a casa."
    "Hacéis el viaje en el Under y en el helicóptero abrazados, o todo lo abrazados que se puede estar en un helicóptero."
    "[lis] se queda dormida sobre tu hombro. Disfrutas más el viaje de vuelta a casa de lo que disfrutaste el de ida a Los Angeles."
    "No necesitáis nada de lo que [lis] había traído por si la aplicación del tiempo se equivocaba."
    scene c29s002_550a with dissolve
    call BlinkXS4("c29s002_550") from _call_BlinkXS4_575
    "Al llegar a casa, acompañas a [lis] a su habitación."
    lis "Creo que con esto ha llegado el final de nuestra cita."
    mc "Todo lo bueno llega a su fin. Pero habrá más."
    call BlinkXS4("c29s002_555") from _call_BlinkXS4_576
    lis "Eso espero. *Risa* Mientras dormía en el helicóptero he soñado con cosas que quiero probar."
    mc "*Risa* Esa es mi chica traviesa."
    call BlinkXS4("c29s002_560") from _call_BlinkXS4_577
    lis "Y ahora creo que voy a entrar ahí dentro y a dormir hasta la cena. ¡Estoy agotada!"
    mc "Descansa, Princesa. Has dormido poquísimo esta noche."
    if kim._var("route"):
        call BlinkXS4("c29s002_565") from _call_BlinkXS4_578
        lis "Si no fuera porque tienes el pícnic con [kim] te diría de dormir juntos y abrazados. Me ha encantado hacerlo. Sería como una siesta antes de comer."
        mc "Habrá muchas oportunidades de volver a hacerlo."
        call KissXS4("c29s002_570") from _call_KissXS4_9
        call BlinkXS4("c29s002_570") from _call_BlinkXS4_579
        lis "Pues vete ya antes de que se haga tarde. [kim] te espera en la universidad y no tienes mucho tiempo."
        mc "Hasta luego, Princesa. Descansa."
        lis "Hasta luego, Mi Príncipe."
    else:
        call KissXS4("c29s002_570") from _call_KissXS4_10
        call BlinkXS4("c29s002_570") from _call_BlinkXS4_580
        lis "Voy a irme o me quedaría aquí todo el día besándote."
        mc "*Risa* Hasta luego, Princesa. Descansa."
        lis "Hasta luego, Mi Príncipe."
    scene c29s002_570e with dissolve
    lis "*A través de la puerta* ¡Ya he llegado!"
    deb "*A través de la puerta* ¡Me lo tienes que explicar todo!"
    stop music fadeout (1.5)
    mcp "*Risa mental* (Creo que es el momento idóneo para subir a mi habitación.)"
    scene black with dissolve
    return
label c29s002_ass:
    call OrgasmXS4("c29s002_495") from _call_OrgasmXS4_22
    $ Inside = True
    mc "¡Mpfft!"
    "Descargas una gran cantidad de semen en el interior de su culo, llenando sus intestinos."
    lis "*GEMIDO* ¡SÍ! *JADEO* ¡DÁMELA TODA! *GEMIDO*"
    "Y se la das toda, vaciando el contenido de tus pelotas mientras la chica aprieta su esfínter para ordeñar hasta la última gota."
    "Os quedáis unos momentos inmóviles, disfrutando de las sensaciones que recorren vuestros cuerpos."
    "Del placer compartido por segunda vez en una de las noches más extrañas de tu vida."
    return
label c29s002_pussy:
    call OrgasmXS4("c29s002_500") from _call_OrgasmXS4_23
    $ Inside = True
    mc "¡Mpfft!"
    "Descargas una gran cantidad de semen en el interior de su coño, llenando su útero."
    "Crees que en 48 horas tendrás que hacer una nueva prueba de embarazo."
    lis "*GEMIDO* ¡SÍ! *JADEO* ¡DÁMELA TODA! *GEMIDO*"
    "Y se la das toda, vaciando el contenido de tus pelotas mientras la chica aprieta sus músculos pélvicos para ordeñar hasta la última gota."
    "Os quedáis unos momentos inmóviles, disfrutando de las sensaciones que recorren vuestros cuerpos."
    "Del placer compartido por segunda vez en una de las noches más extrañas de tu vida."
    return
label c29s002_back:
    call OrgasmXS4("c29s002_505") from _call_OrgasmXS4_24
    $ Inside = False
    mc "¡Mpfft!"
    "Sales de su agujero para pintar un cuadro abstracto sobre su espalda."
    lis "*GEMIDO* ¡SÍ! *JADEO* ¡DÁMELA TODA! *GEMIDO*"
    "Y se la das toda, vaciando el contenido de tus pelotas mientras la chica disfruta de las últimas oleadas de su orgasmo."
    "Os quedáis unos momentos inmóviles, disfrutando de las sensaciones que recorren vuestros cuerpos."
    "Del placer compartido por segunda vez en una de las noches más extrañas de tu vida."
    return
label c29s001_noLis:
    scene c29s002_1000a with fade
    "Cuando el coche de [lis] desaparece en la distancia, subes a tu habitación a jugar a My Residence."
    "Tu MC acompaña a Karen a una fiesta en Broadway llena de famosos y gente no tan famosa pero más interesante."
    scene c29s002_1000b with dissolve
    "Después de eso, pasáis una tórrida noche en un hotel que la chica ha reservado en la ciudad."
    "Te parece que Clichecita no ha sabido captar las emociones que una chica experimenta en su primera vez."
    "O eso, o es que Karen es un animal hiper sexual."
    scene black with dissolve
    "Después de cenar, te acuestas pensando en si la fiesta a la que ha ido [lis] se parecerá en algo a la fiesta a la que has acompañado a Karen en el juego."
    return
label c29s003_KatKiss:
    if _in_replay:
        $ mc._var("relationships", 0, "set")
        call mrS3_lis_route from _call_mrS3_lis_route_20
        call mrS3_kat_route from _call_mrS3_kat_route
        call mrS3_kat_slim from _call_mrS3_kat_slim_4
        call mrS3_kim_route from _call_mrS3_kim_route_8
        call mrS3_mar_route from _call_mrS3_mar_route_20
        if kat._var("route") and mc._var("relationships") < 2:
            call mrS3_rels from _call_mrS3_rels_25
    scene c29s003_005a with fade
    play music ("music/SneakySnitch.ogg")
    if lis._var("route"):
        "Después de poner el móvil a cargar, bajas a la cocina a coger una botella de zumo de piña para subirla a tu habitación."
    else:
        centered "{size=+20}{b}DÍA 32 – VIERNES{/b}{/size}"
        "Te levantas descansado y bajas a desayunar algo."
    if kim._var("route"):
        "No tienes demasiado que hacer hasta que tengas que ir al pícnic con [kim] y vas a ver un par de capítulos de tus series favoritas."
    else:
        "Tienes la intención de ponerte al día con tus series favoritas."
    "Hoy no tienes ninguna llamada programada con Aaron."
    "Sorprendentemente, la cocina está vacía. Al menos por unos minutos."
    scene c29s003_010a with fade
    call BlinkXS4("c29s003_010") from _call_BlinkXS4_581
    kat "Hola, [mc]."
    mc "Hola, [kat]. ¿No tienes clases hoy?"
    if kat._var("route"):
        scene c29s003_010d with hpunch
        if mc._var("relationships")>1:
            "La última incorporación al harén te sorprende con un beso pasional e inesperado, dando un salto."
        else:
            "La preciosa mujer te sorprende con un beso pasional e inesperado, dando un salto."
        "Parece que vuestra conversación en la piscina de ayer ha puesto todo en su sitio. Y el sitio de sus labios es besando los tuyos."
    else:
        scene c29s003_010e with hpunch
        "La preciosa mujer te sorprende con un fuerte abrazo."
    call BlinkXS4("c29s003_015") from _call_BlinkXS4_582
    kat "Tengo clase esta tarde. Estaba estudiando en mi habitación cuando te he oído bajar por las escaleras."
    if kat._var("route"):
        kat "Me he puesto esto y he venido a darte un beso."
    else:
        kat "Me he puesto esto y he venido a darte un abrazo."
    kat "Sienta tan bien no tener que seguir evitándote..."
    mc "*Risa* ¿Estudias desnuda?"
    call BlinkXS4("c29s003_020") from _call_BlinkXS4_583
    kat "*Risa* ¡Qué bruto eres! Pero no, no estudio desnuda. O al menos no del todo. ¿Por qué lo preguntas?"
    if kat._var("route"):
        mc "*Risa* Por si alguna vez tengo que entrar sin llamar."
    else:
        mc "*Risa* Para saber que NO tengo que entrar sin llamar."
    call BlinkXS4("c29s003_025") from _call_BlinkXS4_584
    kat "Mejor que no lo hagas. *Risa* No podrías resistirte a estas curvas."
    if kat._var("slim"):
        kat "Al menos mientras las tenga. A este paso me voy a quedar tan delgada como [sca]."
    if not kim._var("route"):
        kat "Y a lo mejor a [kim] no le hace demasiada gracia que la pilles cambiándose. No entiendo cómo se puede cambiar tantas veces al cabo del día."
    mc "*Risa* Nota mental. No entrar sin llamar."
    call BlinkXS4("c29s003_030") from _call_BlinkXS4_585
    kat "Bueno, yo me voy a estudiar de nuevo."
    mc "¿Ya te vas?"
    if kat._var("route"):
        kat "Sí, sólo he venido a por el beso..."
        call BlinkXS4("c29s003_035") from _call_BlinkXS4_586
        kat "{i}(Y a comprobar que no soñé lo de ayer){/i}"
    else:
        kat "Sí, sólo he venido a por el abrazo. Me gusta que todo vuelva a la normalidad entre nosotros."
    mc "Puedes venir a por más tantas veces como quieras."
    if kat._var("route"):
        call KissXS4("c29s003_040") from _call_KissXS4_11
    call BlinkXS4("c29s003_040") from _call_BlinkXS4_587
    kat "*Risa* Podría correr el riesgo de que se convirtieran en una adicción."
    mc "*Risa* No hay nada malo en ello."
    kat "Hasta luego, [mc]."
    mc "Hasta luego, [kat]."
    scene c29s003_045An1 with dissolve
    kat "¡Oops! Hola, [mar]. Voy a mi habitación a estudiar. Adiós, [mar]."
    stop music fadeout (1.5)
    mom "Hola, [kat]."
    scene c29s003_045An2 with dissolve
    play sound ("music/DoorSlam.ogg")
    "*Blam*"
    mom "Adiós, [kat]."
    play music ("music/PositiveWoman.ogg")
    call BlinkXS4("c29s003_050") from _call_BlinkXS4_588
    mom "¿Le pasa algo?"
    if kat._var("route"):
        if mc._var("relationships")>1:
            mc "*Risa* Sólo está descubriendo las ventajas de pertenecer al harén."
        else:
            mc "*Risa* Sólo está descubriendo las ventajas de salir conmigo."
    else:
        mc "*Risa* Sólo está descubriendo las ventajas de volver a ser amigos después de aclararlo todo ayer."
    call BlinkXS4("c29s003_055") from _call_BlinkXS4_589
    mom "Menos mal que lo solucionasteis. [nor] empezaba a estar un poco histérica. [kat] no se decidía sobre qué hacer o cómo hacerlo y lo único que hacía era esconderse."
    mc "Bueno, creo que estaba en su derecho de tomarse el tiempo que necesitara para aclarar sus ideas. No ha debido de ser fácil para ella."
    call BlinkXS4("c29s003_060") from _call_BlinkXS4_590
    if kat._var("route"):
        mom "*Risa* Lo sé, no estoy criticando a tu nueva novia. Yo también pasé por lo mismo el día del desayuno de disfraces."
    else:
        mom "*Risa* Lo sé. Yo también pasé por lo mismo el día del desayuno de disfraces."
    mom "Pero a mí no me dejaste tiempo para pensar."
    mc "Diferentes personas y diferentes circunstancias."
    if mar._var("route"):
        mc "¿Te arrepientes de que no te dejara pensar?"
        call KissXS4("c29s003_065") from _call_KissXS4_12
        call BlinkXS4("c29s003_065") from _call_BlinkXS4_591
        mom "No me arrepiento de nada de lo que ha pasado entre nosotros desde que llegaste."
        mom "Gracias a eso, ahora soy tu esposa. No oficial, pero tu esposa, al fin y al cabo."
        if mc._var("relationships")>1:
            mom "Además, creo que soy la primera a la que llamas esposa, con lo que me siento más especial todavía."
            mc "Has sido la primera, y de momento la última, a la que se lo he llamado. Para mí era algo natural."
        mc "Y tú sabes que me da lo mismo que sea oficial o no, ¿verdad?"
        call BlinkXS4("c29s003_070") from _call_BlinkXS4_592
        mom "Lo sé y eso me hace aún más feliz."
        mom "Pero no sigas por ahí o tendré que llevarte a la habitación ahora mismo y he quedado con [sam] y [meg]."
    else:
        call BlinkXS4("c29s003_065") from _call_BlinkXS4_593
        mom "Lo sé. Cada una de nosotras es diferente."
        mom "Hoy he quedado con [sam.nick] y con [meg] en el centro."
    mom "Nunca podría haber imaginado que dos personas tan diferentes pudieran convertirse en mis amigas, y en amigas entre ellas."
    mc "¿Qué vais a hacer? ¿Habéis quedado para comer?"
    call BlinkXS4("c29s003_080") from _call_BlinkXS4_594
    mom "Sí, iremos a comer y queremos ir a mirar unas cosas. Quizás comprar algo de ropa y otras cosas."
    mom "Hoy se ocupa [nor] de la comida. Le he estado ayudando a preparar algunas cosas."
    if kim._var("route"):
        call BlinkXS4("c29s003_085") from _call_BlinkXS4_595
        mom "Ya he preparado la cesta para tu pícnic con [kim] y está en su nevera. Esta nevera siempre está llenísima."
        if persistent.family:
            mc "Gracias, Mamá. Con tantas chicas viviendo en casa y las que se quedan a dormir, la nevera se está quedando pequeña."
        else:
            mc "Gracias, [mar]. Con tantas chicas viviendo en casa y las que se quedan a dormir, la nevera se está quedando pequeña."
    else:
        call BlinkXS4("c29s003_085") from _call_BlinkXS4_596
        mom "En esta nevera está llenísima y le he llevado algunas cosas para que las guarde allí."
        mc "Con tantas chicas viviendo en casa y las que se quedan a dormir, la nevera se está quedando pequeña."
    mc "Deberíamos comprar una para el sótano. Y en casa de [nor] pasará lo mismo en un mes, cuando lleguen las chicas nuevas."
    call BlinkXS4("c29s003_090") from _call_BlinkXS4_597
    mom "Creo que sería una buena idea. Ahora me tengo que ir. Quiero cambiarme de camisa, y [meg] debe estar esperándome en la puerta del garaje."
    mc "¿No vais en su coche? ¿El tuyo tiene batería?"
    mom "Le cuesta una barbaridad meterlo y sacarlo, con lo que iremos con el mío. Y sí, tiene batería."
    if mar._var("route"):
        call KissXS4("c29s003_065") from _call_KissXS4_13
    call BlinkXS4("c29s003_065") from _call_BlinkXS4_598
    mom "Te veo luego."
    stop music fadeout (1.5)
    mc "Pasáoslo bien en la comida y las compras."
    return
label c29s003_KimPicnic:
    if _in_replay:
        $ mc._var("relationships", 1, "set")
        call mrS3_kat_route from _call_mrS3_kat_route_1
        call mrS3_lis_route from _call_mrS3_lis_route_21
        if not kat._var("route") and not lis._var("route"):
            call mrS3_sai_route from _call_mrS3_sai_route_10
            if not sai._var("route"):
                call mrS3_deb_route from _call_mrS3_deb_route_19
        if mc._var("relationships")<3:
            call mrS3_rels from _call_mrS3_rels_26
    scene drive_day with fade
    play music ("music/Embrace.ogg")
    "Cuando se acerca la hora de ir a comer, vas a la cocina de [nor] a por las cosas del pícnic y conduces hasta el campus."
    scene c29s003_100a with fade
    "Te diriges al área ajardinada de la universidad. Se te hace raro ser prácticamente el único hombre en el campus que no trabaja allí."
    "Siendo verano, esperabas que hubiera más chicos visitando a sus novias para disfrutar del soleado día, pero sólo has visto a un par de ellos."
    scene c29s003_100b with fade
    "Cuando llegas a la zona donde habías quedado con [kim], la ves sentada en un banco esperándote mientras lee un libro."
    "Los dos habéis llegado antes de la hora acordada. Los dos tenéis ganas de pasar tiempo juntos."
    scene c29s003_100c with dissolve
    "Te acercas sin que se dé cuenta de tu presencia."
    mc "Boo."
    call BlinkXS4("c29s003_105") from _call_BlinkXS4_599
    kim "*Risa* No me has asustado. Te he visto los pies... justo antes de que dijeras 'Boo'. Y el libro NO ha estado a punto de caerse."
    mc "*Risa* No era mi intención asustarte ni que el libro saliera volando. ¿Preparada para ir a comer?"
    call KissXS4("c29s003_110") from _call_KissXS4_14
    call BlinkXS4("c29s003_110") from _call_BlinkXS4_600
    kim "Ahora sí. Vamos, he encontrado un sitio chulo para comer."
    mc "¿Sabes que estaba enfadado con esta universidad cuando estaba en el instituto?"
    call BlinkXS4("c29s003_115") from _call_BlinkXS4_601
    kim "¿Por qué? Tu padre trabajaba aquí..."
    mc "*Risa* No tiene nada que ver con mi padre. Te pasas toda tu vida viendo pelis de universitarios tirados en el césped estudiando."
    mc "Y la universidad que tienes al lado de casa es solo para chicas y acabas yendo a Portland. No es el mejor clima para tirarse en el césped."
    call BlinkXS4("c29s003_120") from _call_BlinkXS4_602
    kim "Te entiendo. Yo quería estudiar en Cleveland, pero acabé incluso más al norte que tú. Y con más frío."
    mc "*Risa* Es verdad, vienes de Bellingham."
    kim "Sí. Ahí hace frío de verdad."
    call BlinkXS4("c29s003_125") from _call_BlinkXS4_603
    kim "Pero si no hubieras ido a Portland, no habrías conocido a Saira y no hubierais tenido vuestra relación abierta."
    if mc._var("relationships")>1:
        kim "Y sin eso, lo más probable es que no hubiera harén y que no estuviéramos juntos."
    mc "Visto así, tengo que estar agradecido de que esta universidad sea solo para chicas."
    mc "*Risa* Solo me ha hecho falta empezar a salir con una de las alumnas para poder tumbarme en el césped."
    if sai._var("route") or lis._var("route") or deb._var("route") or kat._var("route"):
        call BlinkXS4("c29s003_130") from _call_BlinkXS4_604
        kim "*Risa* ¿Sólo con una?"
        mc "Solo con una que importe en este momento."
        call BlinkXS4("c29s003_135") from _call_BlinkXS4_605
        kim "¿Siempre vas a intentar hacerme sentir especial?"
        mc "El día que deje de intentarlo, dímelo. Y si dejo de conseguirlo, también deberías decírmelo."
        mc "Intentar algo y conseguirlo no siempre se dan la mano."
    scene c29s003_135d with dissolve
    kim "Déjame recoger las cosas y nos vamos."
    mc "¿Te ayudo?"
    kim "No hace falta. Ni siquiera te voy a pedir que me lleves la mochila."
    scene c29s003_135e with dissolve
    kim "Por cierto, hay muchas más cosas que puedes hacer aparte de tumbarte en el césped."
    mc "Y esta es una de las que más me gustan."
    scene c29s003_140a with fade
    call BlinkXS4("c29s003_140") from _call_BlinkXS4_606
    "Una vez llegáis al sitio escogido por [kim] y estiráis la manta..."
    kim "Pues ya estamos aquí. ¿Qué ha preparado [mar]? ¡Me muero de hambre!"
    mc "La verdad es que no lo he mirado. He cogido la cesta y he venido aquí directamente."
    scene c29s003_145An with dissolve
    "[kim] estira la mano hacia la cesta con la comida e interrumpe el gesto a medio camino con un pequeño espasmo."
    mc "¿Pasa algo, [kim]?"
    call BlinkXS4("c29s003_150") from _call_BlinkXS4_607
    kim "Después de... lo que hicimos ayer... siento un pequeño dolor dependiendo que movimiento hago."
    kim "Al estirarme hacia la cesta me ha dado un pinchazo en... la parte baja de la barriga."
    mc "¿Duele mucho? Has dicho un pequeño dolor, pero..."
    call BlinkXS4("c29s003_155") from _call_BlinkXS4_608
    kim "Pero mi cara ha dicho que no era pequeño, ¿verdad?"
    mc "Sí..."
    kim "[kat] me ha dicho lo mismo esta mañana, mientras me vestía para venir a clase. [sai] me ha dicho que desaparecerá hoy o mañana."
    mc "Espero que sea hoy en vez de mañana."
    call BlinkXS4("c29s003_160") from _call_BlinkXS4_609
    kim "Yo también. Cada vez que me da un pinchazo es un poco menos doloroso que el anterior, pero todavía duele."
    mc "Lo siento..."
    call BlinkXS4("c29s003_165") from _call_BlinkXS4_610
    kim "No tienes que sentir nada. Lo hicimos juntos porque los dos lo deseábamos."
    mc "Lo sé, pero me jode que tengas que estar sufriendo uno o dos días por ello."
    call BlinkXS4("c29s003_170") from _call_BlinkXS4_611
    kim "Al menos [sai] dice que solo pasa una vez."
    mc "*Risa* Si pasara cada vez, creo que la humanidad se extinguiría por falta de sexo."
    call BlinkXS4("c29s003_175") from _call_BlinkXS4_612
    kim "*Risa* No creas. Si este es el precio a pagar por lo de ayer, creo que lo pagaría cada vez."
    stop music fadeout (1.5)
    mc "Mejor que no tengas que pagarlo. Pero has dicho que te tenías hambre. ¿Comemos?"
    play music ("music/CelticFlute.ogg")
    kim "*Risa* Sí, por favor. No quieres verme hambrienta y dolorida a la vez. Puedo ser un poco cascarrabias."
    scene c29s003_180An with dissolve
    "Coméis entre risas y bromas. La comida es interrumpida por besos de vez en cuando."
    "No es el tipo de pícnic que recordabas, pero no lo cambiarías por los que hacías cuando eras un niño."
    "Por un momento te imaginas este tipo de pícnic con Jamaal. Desagradable."
    "En la imagen mental, su silla de ruedas está encima de tus piernas."
    scene c29s003_185a with fade
    call BlinkXS4("c29s003_185") from _call_BlinkXS4_613
    "Al acabar de comer..."
    kim "Creo que ha sido el mejor pícnic de mi vida."
    mc "Yo creo que lo podemos repetir, pero aún no ha acabado."
    call BlinkXS4("c29s003_190") from _call_BlinkXS4_614
    kim "¿Qué quieres hacer ahora?"
    mc "Yo me quedaría así un rato. Las vistas de esos ojos son increíbles."
    mc "Y suele ser el momento de las conversaciones trascendentales de después de comer. *Risa*"
    call BlinkXS4("c29s003_195") from _call_BlinkXS4_615
    kim "Me gusta la parte de quedarnos así, pero no creo que sea una persona muy dada a conversaciones trascendentales. *Risa* Soy modelo."
    mc "*Risa* Podemos estar así en silencio, entonces."
    scene c29s003_200a with fade
    call BlinkXS4("c29s003_200") from _call_BlinkXS4_616
    "El silencio dura menos de un minuto."
    kim "Me alegra mucho que hayas arreglado las cosas con [kat]."
    mc "A mí también. La situación se estaba volviendo incómoda."
    call BlinkXS4("c29s003_205") from _call_BlinkXS4_617
    kim "Anoche volvía a ser ella misma por primera vez en días."
    if not kat._var("route"):
        mc "Su situación era complicada. Estaba viendo cosas donde no las había, tanto por su parte como por la mía."
        mc "Me alegra haber aclarado las cosas con ella. Ahora podemos volver a ser amigos."
        mc "Pero no hablemos de [kat] en nuestra primera comida juntos."
    else:
        mc "Su situación era complicada. Me alegro de que se haya resuelto."
        call BlinkXS4("c29s003_210") from _call_BlinkXS4_618
        kim "La tenías que haber visto anoche. Estaba emocionada. *Risa* Pero fuiste un poco capullo."
        mc "¿Por qué? ¿Qué hice?"
        call BlinkXS4("c29s003_215") from _call_BlinkXS4_619
        kim "*Risa* Cuando le dijiste que sentías que el universo del que hablaba no fuera el nuestro..."
        kim "Por lo que me dijo, le dieron ganas de meter la cabeza dentro del agua y no volver a salir."
        mc "*Risa* Menos mal que no lo hizo."
        mc "Pero me alegra que esté tan emocionada como yo."
        call BlinkXS4("c29s003_220") from _call_BlinkXS4_620
        kim "Creo que lo está aún más. Ayer no hacía más que preguntarme cosas..."
        mc "¿Sobre lo que hicimos tú y yo antes de que yo bajara a la piscina?"
        call BlinkXS4("c29s003_225") from _call_BlinkXS4_621
        kim "Sobre eso también, pero no le di detalles. Lo que pasó en esa habitación es nuestro. Tuyo y mío."
        kim "Quizás algún día hable de ello, pero, de momento, prefiero guardármelo para mí."
        mc "Suena lógico. Pero entonces, ¿qué te preguntaba?"
        call BlinkXS4("c29s003_230") from _call_BlinkXS4_622
        kim "Un montón de cosas."
        kim "Si podía besarte cuando quisiera delante de otras chicas o de [mar]..."
        kim "Si tenía que ir maquillada y bien vestida siempre o podía segur llevando su ropa..."
        if mc._var("relationships")==2:
            kim "Si tenía que comportarse de una forma distinta conmigo..."
        else:
            kim "Si tenía que comportarse de una forma distinta con las chicas del harén..."
        mc "No lo entiendo. No soy la primera persona con la que sale."
        call BlinkXS4("c29s003_235") from _call_BlinkXS4_623
        kim "Pero eres la primera persona con la que sale y con la que vive." id c29s003_KimPicnic_b3bd934d
        kim "No es lo mismo cuando solo ves a tu pareja cuando quedas con ella que si te la puedes encontrar recién levantada y aún sin peinar."
        mc "*Risa* ¿No te peinas nada más levantarte?"
        call BlinkXS4("c29s003_240") from _call_BlinkXS4_624
        kim "*Risa* Me peino después de ducharme. Y nos podemos cruzar mientras voy de mi habitación a la ducha."
        kim "A mí no me preocupa demasiado, igual que no me importa que me veas sin maquillar, pero era una de las preguntas que me hizo [kat]."
        mc "*Risa* Yo a veces bajo a desayunar sin peinarme."
        mc "Pero estamos hablando mucho de [kat] y poco de nosotros."
    mc "Nunca me has explicado por qué una modelo estudia Económicas."
    call BlinkXS4("c29s003_245") from _call_BlinkXS4_625
    kim "*Risa* Para tener un trabajo fiable cuando me rompa los dos tobillos desfilando."
    kim "*Risa* A veces da miedo subirse a una pasarela y ver la hostia que me podría dar."
    mc "*Risa* Eso demuestra lo valiente que eres. Desfilar sin armadura, conociéndote..."
    mc "Pero hablando en serio, ¿por qué Económicas?"
    call BlinkXS4("c29s003_250") from _call_BlinkXS4_626
    kim "Es fácil de explicar. Sé que la carrera de modelo no suele ser larga a menos que llegues a la cima."
    kim "Nunca he pensado que podría ser como Klaudia Schiffer o Noemi Campbell, con lo que lo más probable es que a los 30 no me contrate nadie ya."
    mc "Eso no tiene por qué ser así."
    call BlinkXS4("c29s003_255") from _call_BlinkXS4_627
    kim "No tiene por qué serlo, pero es mejor estar preparada por si lo es."
    kim "Si tengo que dejar de desfilar, lo que me gustaría sería ayudar a otras chicas que empiezan."
    kim "Y la mejor forma sería tener una agencia de modelos."
    mc "Es una buena idea. Pero ¿por qué Económicas y no Administración de Empresas o algo más relacionado con la moda?"
    call BlinkXS4("c29s003_260") from _call_BlinkXS4_628
    kim "*Risa* Porque mi orientador en el instituto se equivocó o me malinterpretó cuando le expliqué lo que quería hacer."
    kim "A mí me parecía raro que me recomendara Económicas, pero como nunca me ha gustado llevar la contraria a las personas que saben de lo que hablan..."
    mc "Pensaste que había algo que se te escapaba, ¿no?"
    call BlinkXS4("c29s003_265") from _call_BlinkXS4_629
    kim "Exacto. Y ahora estoy haciendo una carrera que... no es que no me guste, pero no le veo utilidad."
    kim "Seguramente acabaré con dos carreras o dejando ésta y aprovechando todo lo que pueda convalidar para pasarme a Administración de Empresas."
    kim "Si algún día tengo una empresa, necesitaré dominar cosas que no me enseñan en esta carrera."
    mc "Creo que no es necesario. [nor] y yo estudiamos Administración de Empresas."
    mc "No hace falta que sepas hacer todo lo referido a una empresa. Puedes dejarte ayudar si algún día lo necesitas."
    call BlinkXS4("c29s003_270") from _call_BlinkXS4_630
    kim "Creo que tú vas a estar muy ocupado, y a [nor] ya le damos demasiado trabajo."
    mc "A menos que quieras tener una agencia de modelos enorme, creo que podríamos hacerlo."
    mc "Y si tienes una agencia de modelos enorme, te dedicarás a otras cosas y tendrás un profesional para llevar la administración."
    call BlinkXS4("c29s003_275") from _call_BlinkXS4_631
    kim "Tienes razón. Como pensaba en algo pequeño... ya te he dicho que sería para ayudar a las chicas que empiezan... Creía que lo tendría que hacer todo yo, pero..."
    mc "Pero ahora tienes una familia a tu alrededor en la que te puedes apoyar. Podemos ayudarte de cien formas diferentes."
    mc "Y no lo digo sólo porque estemos saliendo juntos. Si no lo hiciéramos también te lo propondría."
    call BlinkXS4("c29s003_280") from _call_BlinkXS4_632
    kim "Esa es una de las cosas con las que me empecé a enamorar de ti."
    kim "Siempre estás pensando en cómo ayudar a los demás sin pensar en la carga de trabajo que eso te va a reportar."
    mc "No soy Elon Must. No pienso vivir para trabajar; prefiero trabajar para vivir."
    mc "Siempre tendré tiempo para ayudar a las personas que me importan."
    stop music fadeout (1.5)
    return
label c29s004_BetMeeCall:
    if _in_replay:
        call mrS3_kim_route from _call_mrS3_kim_route_9
    if kim._var("route"):
        call BlinkXS4("c29s004_005") from _call_BlinkXS4_633
        play sound ("music/RingtoneMC.ogg")
        "*Ring-Ring*"
        mc "Es Tía [bet]. Tengo que cogerlo."
        kim "No te preocupes. Dale un beso de mi parte. Yo voy a ir recogiendo esto mientras tanto."
        scene c29s004_010a with fade
    else:
        scene c29s004_015a with dissolve
        "Después de ver varios capítulos de una serie que hacía mucho que no veías..."
        play sound ("music/RingtoneMC.ogg")
        "*Ring-Ring*"
        scene c29s004_010a with fade
    stop sound
    mc "Buenas tardes, Tía [bet] y Meemaw."
    play music ("music/Morning-Sun.ogg")
    bet "Hola, [mc]."
    mee "¿Cómo estás, [mc]?"
    if kim._var("route"):
        mc "Yo estoy bien. Estoy con [kim] en el campus haciendo un pícnic. Os envía besos. ¿Y vosotras?"
        scene c29s004_010b with dissolve
        bet "¿Os estamos interrumpiendo una cita? No lo ha puesto en el grupo de Whatsup..."
        mee "Ya llamaremos más tarde. No es urgente."
        mc "No os preocupéis. [kim] ha ido a tirar la basura a los contenedores de reciclaje mientras hablo con vosotras."
        mc "¿Cómo estáis? ¿Qué tal la venta de la casa?"
    else:
        mc "Yo estoy bien. Me iba a poner a trabajar ahora. ¿Y vosotras? ¿Qué tal la venta de la casa?"
    bet "Os dejo que habléis de la casa. Ahora vuelvo."
    call BlinkXS4("c29s004_020") from _call_BlinkXS4_634
    mee "Muy bien, el chico del que te hablé ha estado aquí esta mañana y cree que se venderá bien."
    mee "Además, nos ha ahorrado un montón de trabajo."
    mc "¿Por qué? ¿Qué ha pasado?"
    call BlinkXS4("c29s004_025") from _call_BlinkXS4_635
    mee "Una casa se vende mejor si está decorada... Bueno, si está decorada con un mínimo gusto. Al menos para un cierto tipo de clientes."
    mee "Los compradores pueden ver cómo quedan los espacios de la casa y hacerse una idea de cómo les quedaría con sus muebles."
    mc "Lo entiendo. Es difícil hacerse una buena idea del tamaño de una habitación vacía."
    call BlinkXS4("c29s004_030") from _call_BlinkXS4_636
    mee "Exacto. Este chico es muy profesional y, cuando se lo he comentado, me ha ofrecido un servicio de mudanza después de la venta."
    mee "Con lo que sólo tendremos que empaquetar ropa y otros objetos personales. Pero no hará falta desmontar toda la casa."
    mc "Eso es genial. ¿Significa que volveréis antes de lo pensado?"
    call BlinkXS4("c29s004_035") from _call_BlinkXS4_637
    mee "Sí. En un par de horas vendrá el chico con el contrato."
    mee "El lunes vendrán los de la mudanza para etiquetar las cosas que se tienen que llevar a Newport y a llevarse lo que empaquetemos este fin de semana."
    mee "El martes volaremos de vuelta a San Luis por la mañana."
    mc "¡Estupendo! Eso significa que os veré antes de irme a Aruba."
    call BlinkXS4("c29s004_040") from _call_BlinkXS4_638
    mee "Sí, [bet] quería hablar contigo sobre eso, a ver si vuelve."
    bet "*Fuera de cámara* Ya estoy aquí."
    mc "¿De qué querías hablar, Tía [bet]?"
    scene c29s004_045aa with fade
    call BlinkXS4("c29s004_045a") from _call_BlinkXS4_639
    bet "*Risa* De cualquier cosa que no tenga que ver con vender la casa."
    mc "Supongo que es el tema favorito de Meemaw ahora mismo. Deformación profesional y esas cosas. Seguro que ha criticado cómo ha llevado el tema el chico ese."
    mee "*Fuera de cámara* *Risa* Os estoy escuchando..."
    bet "*Risa* Creo que la conoces demasiado bien. Ella hubiera hecho un montón de cosas diferentes de lo que ha hecho el agente inmobiliario."
    mc "Se ha pasado muchos años vendiendo casas. Sabe de lo que habla."
    call BlinkXS4("c29s004_045b") from _call_BlinkXS4_640
    bet "La verdad es que el chico ha sido muy amable y paciente. Yo no lo hubiera sido tanto si alguien me estuviera diciendo cómo tengo que hacer mi trabajo."
    mee "*Fuera de cámara* ¡Es que había cosas que él no estaba teniendo en cuenta!"
    bet "¿Ves? A eso me refiero. Aceptar consejos está bien. Que tu cliente te diga cómo se tienen que hacer las cosas es diferente."
    mc "*Risa* Me puedo imaginar la cara del vendedor cuando pensaba que iba a vender la casa de dos dulces ancianitas y se encuentra una fiera del mercado inmobiliario."
    call BlinkXS4("c29s004_045c") from _call_BlinkXS4_641
    bet "*Risa* Mas o menos ha sido eso. Por suerte mis clientes suelen estar anestesiados."
    mc "*Risa* No me imagino a uno de tus clientes diciendo 'opere un poco más a la izquierda'."
    mc "*Risa* Y por suerte no eres forense. Si te lo dijeran entonces sería para salir corriendo."
    call BlinkXS4("c29s004_050") from _call_BlinkXS4_642
    bet "Pero de lo que realmente quería hablar contigo es que ya he escrito a Aaron para decirle que iré a Aruba a intentar hacer la operación."
    mc "Eso es genial, Tía [bet]."
    bet "¿Puedes decirle a [ama] que se ocupe de mis billetes de avión? La he llamado hace un rato, pero no la he localizado."
    mc "Creo que no será necesario. Aunque [lis] se queje, pero creo que volaremos en uno de los aviones de la compañía."
    call BlinkXS4("c29s004_055") from _call_BlinkXS4_643
    bet "¡Oh! No había pensado en eso. Me tengo que acostumbrar a que mi sobrino nieto es el CEO de una compañía importante con aviones privados."
    mc "Si queréis puedo preguntarle a [ama] si el avión puede recogeros el martes y así os evitáis la escala en Dallas."
    call BlinkXS4("c29s004_060") from _call_BlinkXS4_644
    bet "*Risa* Estaría bien, pero prefiero que no hagas cosas raras con la compañía."
    mc "Como quieras. Por preguntarle a [ama] no perderíamos nada..."
    call BlinkXS4("c29s004_065") from _call_BlinkXS4_645
    bet "No te preocupes. Ya tenemos los billetes y, si los anulamos, a [mee] le va a dar un infarto por el dinero que perderemos."
    mc "Pero ahorraríais más si..."
    call BlinkXS4("c29s004_070") from _call_BlinkXS4_646
    bet "*Risa* ¿No conoces a [mee]? Le molestaría más el dinero que perdería en la anulación de lo que le alegraría lo que recuperaría."
    bet "Ahora está en ese modo de ahorrar todo lo que pueda para la casa nueva."
    mc "Es normal, en pocos años se fue de San Luis a Florida y ahora vuelve aquí. Son tres casas en poco tiempo."
    mee "*Fuera de cámara* [bet], sigo oyéndote. Y nos vamos a tener que ir a por cajas antes de que cierre la tienda."
    scene c29s004_010c with fade
    mee "Te echamos mucho de menos y esas cosas, pero si cierra la tienda no vamos a poder empaquetar la ropa."
    bet "*Risa* Ya conoces lo práctica que es [mee]."
    mc "Bueno, es comprensible. No os canséis demasiado tenéis todo el fin de semana para hacerlo."
    scene c29s004_010d with dissolve
    bet "*Risa* Si por [mee] fuera, lo acabaríamos esta noche, aunque después nos tuviéramos que pasar dos días en la cama para recuperarnos de los dolores de espalda."
    mee "*Risa* ¿Estás insinuando que te tengo esclavizada?"
    mc "*Risa* Creo que deberías invitar a Tía [bet] a alguna pizzería cuando vayáis a por las cajas, Meemaw. Como pago por toda la ayuda que te está prestando."
    scene c29s004_010e with dissolve
    bet "*Risa* ¡Sí!"
    mee "¡Pero ayer ya pedimos pizza!"
    mc "*Risa* Estoy seguro de que Tía [bet] agradecerá comer con cubiertos en vez de mancharse las manos de grasa..."
    bet "*Risa* ¡A mí me da lo mismo la grasa!"
    mc "Bueno, no os entretengo más. Os quiero."
    scene c29s004_010f with dissolve
    mee "Y nosotras a ti." (multiple=2)
    bet "Nosotras también." (multiple=2)
    if kim._var("route"):
        scene c29s004_010g with dissolve
        mee "Y cuida de [kim]. Después de lo de ayer tiene que estar dolorida."
        mc "*Risa* Vaya. Las noticias vuelan. Ya han llegado hasta Florida."
        bet "*Risa* ¿No te has enterado de que estamos en el Siglo XXI? Existe internet, las videollamadas y los grupos de WhatsUp."
    scene c29s004_010h with dissolve
    mee "Te dejamos antes de que cierren la tienda. Tenemos que volver para cuando esté aquí el chico con el contrato."
    bet "¡Ciao! *Risa* Tengo que practicar mi italiano para pedir la pizza correctamente."
    stop music fadeout (1.5)
    mc "Hasta el martes. Pasáoslo bien."
    return
label c29s004_SamMegMarTattoo:
    if _in_replay:
        $ mc._var("relationships", 0, "set")
        call mrS3_mar_route from _call_mrS3_mar_route_21
        call mrS3_meg_route from _call_mrS3_meg_route_4
        call mrS3_sam_route from _call_mrS3_sam_route_6
        call mrS3_bet_route from _call_mrS3_bet_route_9
        call mrS3_mee_route from _call_mrS3_mee_route_12
        if mc._var("relationships")<2:
            call mrS3_rels from _call_mrS3_rels_27
    scene c29s004_100a with dissolve
    play music ("music/Looking-Forward.ogg")
    "En un café al otro lado de Newport..."
    if mc._var("relationships")>0:
        mar "Pues ya está hecho. No ha sido para tanto, ¿no?"
        meg "Realmente creía que iba a ser mucho más. Ha sido muy soportable."
        sam "*Risa* Sois unas quejicas. Os habéis pasado todo el camino con miedo y ahora descubrís que no es para tanto."
        sam "Me teníais que haber hecho caso y os hubierais evitado preocupaciones."
        call BlinkXS4("c29s004_105") from _call_BlinkXS4_647
        if meg._var("route"):
            meg "Lo que me da más miedo es cómo se lo vamos a ocultar a [mc]. Si lo descubre, la sorpresa se puede ir a la mierda."
        else:
            meg "Lo que me da más miedo es cómo hacer que [mc] no se entere. Si lo descubre, la sorpresa se puede ir a la mierda."
        call BlinkXS4("c29s004_110") from _call_BlinkXS4_648
        if sam._var("route"):
            sam "Yo me voy a esconder de él durante unos días. No creo que pudiera ocultárselo en según qué circunstancias."
            if mc._var("relationships")>1:
                sam "Y por eso no lo hacemos todas a la vez. Conocemos a nuestro hombre y sabemos lo insaciable que puede ser."
        else:
            sam "Y por eso se está haciendo por grupos. Ya sabéis lo insaciable que puede llegar a ser."
        call BlinkXS4("c29s004_115") from _call_BlinkXS4_649
        if bet._var("route") and mee._var("route"):
            if persistent.family:
                mar "Al menos mi madre y [bet] no van a tener que hacer nada especial. Ha sido una gran idea hacerlo el día en que vuelven."
            else:
                mar "Al menos [mee] y [bet] no van a tener que hacer nada especial. Ha sido una gran idea hacerlo el día en que vuelven."
        elif bet._var("route"):
            mar "Al menos [bet] no va a tener que hacer nada especial. Ha sido una gran idea hacerlo el día en que vuelven."
        elif mee._var("route"):
            if persistent.family:
                mar "Al menos mi madre no va a tener que hacer nada especial. Ha sido una gran idea hacerlo el día en que vuelven."
            else:
                mar "Al menos [mee] no va a tener que hacer nada especial. Ha sido una gran idea hacerlo el día en que vuelven."
        else:
            if persistent.family:
                mar "Ha sido una gran idea hacerlo el día en que vuelven mi madre y [bet]. Se enfadarían si se lo perdieran."
            else:
                mar "Ha sido una gran idea hacerlo el día en que vuelven [mee] y [bet]. Se enfadarían si se lo perdieran."
        call BlinkXS4("c29s004_120") from _call_BlinkXS4_650
        meg "Yo también me enfadaría. Cualquiera que diga lo contrario mentiría. Por suerte hemos encontrado un momento en que a todas nos va bien."
        meg "Aunque yo tendré que volver a Westport en seguida. No me voy a poder quedar. Trabajo esa noche."
        call BlinkXS4("c29s004_125") from _call_BlinkXS4_651
        sam "Esperemos que el vuelo desde Florida no se retrase. Vamos a ir un poco justas de tiempo."
        sam "Yo también tengo turno de noche ese día."
    call BlinkXS4("c29s004_130") from _call_BlinkXS4_652
    mar "Bueno, pensemos en otras cosas en vez de en lo que no podemos controlar."
    mar "¿Sabéis que os vais a poner?"
    call BlinkXS4("c29s004_135") from _call_BlinkXS4_653
    if sam._var("route"):
        sam "*Risa* Yo quería ponerme el vestido de nuestra primera cita, pero no va a poder ser. No es... adecuado. Debería comprarme algo."
    else:
        sam "*Risa* Eso se lo dejo a las afortunadas. Yo no me tengo que preocupar por eso, pero quiero comprarme algo chulo para salir en la foto."
    call BlinkXS4("c29s004_140") from _call_BlinkXS4_654
    meg "Yo también debería comprarme algo. La mayoría de los vestidos que tengo son para el trabajo. Por norma me gusta ir cómoda."
    meg "Y no quiero hacerlo con algo que, en el fondo, es un uniforme. ¿Vamos a la tienda de [mad.nick]?"
    call BlinkXS4("c29s004_145") from _call_BlinkXS4_655
    mar "Yo os iba a proponer ir a la tienda de San Luis que me enseñó la chica aquella de la que os hablé, la que me encontré en la peluquería hace unos días."
    mar "Tienen cosas preciosas... Ya habéis visto las fotos que nos hizo [emm] en la piscina..."
    call BlinkXS4("c29s004_150") from _call_BlinkXS4_656
    sam "*Risa* ¡Eso es casi como engañar a [mad.nick]! Pero por ir a mirar no creo que se enfade..."
    call BlinkXS4("c29s004_155") from _call_BlinkXS4_657
    meg "No se lo digáis, pero a mí no me gusta comprar en la tienda de [mad.nick]. Las tallas que tiene no son para... chicas grandes."
    meg "En Westport no hay muchas tiendas de ropa, con lo que los vestidos para el trabajo los compro por internet. Estaría bien tener una alternativa cerca."
    call BlinkXS4("c29s004_160") from _call_BlinkXS4_658
    stop music fadeout (1.5)
    mar "Pues entonces está decidido. ¡Nos vamos de compras!"
    scene black with dissolve
    return
label c29s006_KiaSim:
    if _in_replay:
        $ mc._var("relationships", 0, "set")
        call mrS3_eil_route from _call_mrS3_eil_route_9
        call mrS3_oma_route from _call_mrS3_oma_route_8
        call mrS3_emm_route from _call_mrS3_emm_route_20
        call mrS3_mar_route from _call_mrS3_mar_route_22
        call mrS3_eri_route from _call_mrS3_eri_route_12
        call mrS3_dap_route from _call_mrS3_dap_route_12
        call mrS3_sai_route from _call_mrS3_sai_route_11
        call mrS3_nor_route from _call_mrS3_nor_route_12
        call mrS3_sca_route from _call_mrS3_sca_route_10
        call mrS3_sim_route from _call_mrS3_sim_route_8
        call mrS3_sam_route from _call_mrS3_sam_route_7
        call mrS3_kia_route from _call_mrS3_kia_route_15
        if mc._var("relationships")<3:
            call mrS3_rels from _call_mrS3_rels_28
    scene c29s006_200a with fade
    play music ("music/Inspiring-Upbeat-Ambient.ogg")
    "Por la tarde bajas a la piscina a relajarte un rato y te encuentras con [kia] y [sim] tomando el sol."
    mc "Buenas tardes, chicas."
    scene c29s006_200b with dissolve
    sim "Buenas tardes, [mc]."
    kia "Hola, [mc]. ¿Por qué no te sientas en esa tumbona y charlas un rato con nosotras?"
    mc "Me parece una idea fantástica. Había venido a darme un chapuzón rápido e iba a volver a mi habitación."
    mc "Nunca me ha gustado demasiado tostarme al sol solo, pero siempre tengo un rato para pasar con vosotras."
    scene c29s006_205a with fade
    call BlinkXS3("c29s006_205") from _call_BlinkXS3_780
    mc "¿Pasa algo, [sim]? Pareces preocupada..."
    sim "No, nada... [kia] y yo estábamos charlando cuando has llegado..."
    mc "¿Puedo preguntar sobre qué? ¿Puedo unirme a la conversación o es algo privado?"
    call BlinkXS3("c29s006_210") from _call_BlinkXS3_781
    kia "*Risa* No es nada que debamos ocultar. Estábamos hablando sobre sexo en grupo."
    kia "Ninguna de las dos lo hemos hecho nunca y nos parece raro a la vez que excitante."
    $ mc._var("groupSex", 0, "set")
    if eil._var("route") and oma._var("route"):
        $ mc._var("groupSex", 1, "add")
    if emm._var("route") and mar._var("route"):
        $ mc._var("groupSex", 1, "add")
    if emm._var("route") and eri._var("route") and dap._var("route"):
        $ mc._var("groupSex", 1, "add")
    if eil._var("route") and oma._var("route") and sai._var("route"):
        $ mc._var("groupSex", 1, "add")
    if nor._var("route") and eri._var("route"):
        $ mc._var("groupSex", 1, "add")
    if sca._var("route") and dap._var("route"):
        $ mc._var("groupSex", 1, "add")
    if mc._var("groupSex")>1:
        mc "Yo lo he probado y es muy diferente del sexo individual... pero eso ya lo sabéis."
    else:
        mc "Yo no lo he probado tampoco, pero creo que tiene que ser muy diferente del sexo individual."
    call BlinkXS3("c29s006_215") from _call_BlinkXS3_782
    mc "¿Hay alguien con quién quisieras probar, o era una conversación teórica?"
    if sim._var("route"):
        if sam._var("route"):
            mc "Ya dijiste que con tu madre nunca lo harías."
    sim "Era una conversación teórica. No estábamos diciendo nombres de candidatas."
    sim "Pero creo que nunca lo podría hacer con alguien de quien no fuera amiga."
    if sim._var("route"):
        sim "Y, obviamente, contigo."
    call BlinkXS3("c29s006_220") from _call_BlinkXS3_783
    mc "¿Y tú, [kia]?"
    kia "Pienso lo mismo que [sim]. Debería ser con alguien con quien tuviera complicidad y, obviamente, mi hija también está descartada."
    kia "Es más, creo que descartaría a cualquier mujer por debajo de 40 años. *Risita*"
    mc "¿Por qué? Yo creo que la edad no tiene nada que ver con eso..."
    call BlinkXS3("c29s006_225") from _call_BlinkXS3_784
    sim "*Risa* Cree que no podría seguir el ritmo de una jovencita."
    call BlinkXS3("c29s006_230") from _call_BlinkXS3_785
    kia "*Risa* Yo no he dicho eso, pero es posible que lo de seguir el ritmo tenga algo que ver..."
    mc "El sexo en grupo no tiene por qué ser un sprint. Creo que es más una maratón en la que la edad y la experiencia pueden ser beneficiosas."
    call BlinkXS3("c29s006_235") from _call_BlinkXS3_786
    kia "Bueno, sea como sea, en un hipotético caso donde pudiera elegir a cualquier mujer del mundo para hacer un trío..."
    kia "Creo que mis candidatas serían [mar], [nor], y [sam], por ese orden."
    $ haremN = 0
    if mar._var("route"):
        $ haremN = haremN + 1
    if nor._var("route"):
        $ haremN = haremN + 1
    if sam._var("route"):
        $ haremN = haremN + 1
    if kia._var("route"):
        if haremN == 3:
            mc "Sólo tenéis que hablarlo y ver si alguna de ellas está dispuesta... Y avisarme, claro"
        elif haremN == 2:
            mc "Sólo tenéis que hablarlo y ver si alguna de las que están conmigo está dispuesta... Y avisarme, claro"
        elif haremN == 1:
            mc "Sólo tenéis que hablarlo y ver si la que forma parte del harén está dispuesta... Y avisarme, claro"
        else:
            mc "Como ninguna está conmigo, creo que se quedará en un caso hipotético."
    else:
        if haremN == 3:
            mc "*Risa* No te las pienso prestar, con lo que creo que se quedará en un caso hipotético."
        elif haremN == 2:
            mc "*Risa* No te pienso prestar a las que están en el harén, y no sé si la otra..."
        elif haremN == 1:
            mc "*Risa* No te pienso prestar a la que está conmigo, y no sé si las otras..."
        else:
            mc "Las tres están libres, con lo que si encontráis un candidato masculino..."
    call BlinkXS3("c29s006_240") from _call_BlinkXS3_787
    kia "*Risa* Ya he dicho que era un caso hipotético, no algo que fuera a pasar."
    if kia._var("route") and haremN > 0:
        kia "*Risa* No empieces a hacer planes para llevarte a dos MILFs a la cama."
    mc "*Risa* Todos sabemos que lo hipotético deja de serlo cuando se convierte en real."
    call BlinkXS3("c29s006_245") from _call_BlinkXS3_788
    mc "¿Y tú, [sim]? ¿De verdad no tienes candidatas?"
    if sim._var("route"):
        if mc._var("relationships")>1:
            sim "*Risa* Yo no descartaría a nadie por su edad. Y tampoco descartaría a nadie que estuviera en el harén."
            if sam._var("route"):
                sim "Excepto mi a madre, claro."
            sim "Quizás no hoy o mañana, pero dentro de un tiempo creo que tendremos la confianza suficiente entre todas nosotras para que sea una cosa muy bonita."
        else:
            sim "*Risa* Yo no descartaría a nadie por su edad. Pero las únicas con las que me lo plantearía son las chicas de la familia."
            sim "Y como no estás con ninguna, es algo que no se va a dar. No creo que funcionara para algo de una sola noche."
    else:
        sim "Realmente no. *Risa* Creo que antes de plantearme algo así debería descubrir primero qué es lo que me gusta en el sexo."
    mc "Tiene sentido. El sexo en grupo puede servir para estrechar lazos, pero también puede no funcionar y estropear relaciones."
    call BlinkXS3("c29s006_250") from _call_BlinkXS3_789
    kia "¿Y tú? ¿Tienes pensado en alguien con quien tener sexo en grupo?"
    if mc._var("relationships")==1:
        mc "No. Soy monógamo y creo que podría ser problemático meter a una mujer B en mi relación sólo para tener un trío."
    elif mc._var("relationships")==0:
        mc "*Risa* Si ni siquiera tengo con quien tener sexo individual, menos aún con quien tener un trío. No he encontrado a la mujer A, menos aún a la B."
    elif mc._var("relationships")==2:
        mc "*Risa* Si sólo salgo con dos mujeres, no puede haber más candidatas. Meter a una mujer C sólo para un trío o un cuarteto sería problemático."
    else:
        mc "Estaría dispuesto a hacerlo con cualquier mujer del harén que lo proponga. Pero no voy a ser yo quién dé el primer paso."
        mc "Podría crear suspicacias si intento tener un trío con A y con B dejando fuera a C."
    call BlinkXS3("c29s006_255") from _call_BlinkXS3_790
    sim "*Risa* Me encanta que no hayas dicho nombres y que te hayas referido a las mujeres por letras. Nadie se puede dar por ofendida."
    mc "*Risa* No lo he dicho por eso, pero tienes razón. Creo que lo he hecho inconscientemente."
    mc "Cambiando de tema, creo que ya he recibido mi máxima dosis de sol por un día. Me estoy empezando a tostar."
    call BlinkXS3("c29s006_260") from _call_BlinkXS3_791
    kia "Mira, por ahí viene [eri]. Por desgracia sin bikini..."
    stop music fadeout (1.5)
    kia "Creo que tienes suerte y viene a buscarte."
    call BlinkXS3("c29s006_265") from _call_BlinkXS3_792
    play music ("music/i-feel-alive.ogg")
    eri "Hola, chicas. ¿Puedo robaros a [mc] un momento?"
    scene c29s006_200c with dissolve
    sim "Por supuesto. Creo que se iba a ir ya. No aguanta el sol demasiado rato."
    kia "Se estaba empezando a quejar sobre eso cuando has aparecido."
    call BlinkXS3("c29s006_270") from _call_BlinkXS3_793
    mc "¿Puedo ayudarte en algo?"
    eri "¿Sabes algo de electricidad? Hay un enchufe en mi habitación que no hace buen contacto y, antes de llamar a un electricista, quería preguntarte."
    mc "No sé demasiado, pero puedo desmontar el enchufe y comprobarlo. ¿Déjame ir a por la caja de herramientas y te veo en tu habitación?"
    scene c29s006_200d with dissolve
    mc "Hasta luego, chicas. Una conversación interesante."
    sim "*Risa* Hasta luego, [mc]. Ve con cuidado con el enchufe."
    kia "*Risa* No queremos tener que llevarte al hospital con los pelos de punta."
    scene c29s006_275a with fade
    call BlinkXS3("c29s006_275") from _call_BlinkXS3_794
    eri "¿De qué estabais hablando?"
    mc "Nada demasiado importante. Sobre posibles combinaciones de sexo en grupo."
    call BlinkXS3("c29s006_280") from _call_BlinkXS3_795
    eri "*Risa* Creo que eso puede ser MUY importante."
    mc "*Risa* Cierto, podría serlo."
    stop music fadeout (1.5)
    mc "Espérame en tu habitación. Estaré ahí en dos minutos."
    return
label c29s005_EriCommon:
    scene c29s005_005d with fade
    play music ("music/Higher-Instrumental.ogg")
    eri "Este es el enchufe que no está funcionando bien. He probado a cambiar la bombilla y no es el problema."
    call BlinkXS4("c29s005_005") from _call_BlinkXS4_659
    eri "También he probado a conectar la otra lámpara, que funciona bien en el otro enchufe, y no funciona en este."
    mc "Déjame echarle una ojeada. Si es algo del enchufe, quizás pueda arreglarlo. Si el problema está en otro sitio..."
    call BlinkXS4("c29s005_010") from _call_BlinkXS4_660
    eri "Habrá que llamar a un profesional, a menos que alguna de las chicas sepa algo de electricidad."
    mc "Y, si nadie sabe nada, podemos traer a Jamaal para que meta los dedos en el enchufe e ir haciendo pruebas."
    mc "*Risa* Cuando se le ponga el pelo tieso, significará que lo hemos arreglado."
    call BlinkXS4("c29s005_015") from _call_BlinkXS4_661
    eri "*Risa* A veces no sé cómo te aguanta. Bueno, cómo os aguantáis mutuamente."
    mc "*Risa* Hasta ahora, te podía haber dicho que era porque soy su único amigo, pero estando con Anthony ya no me sirve esa excusa."
    call BlinkXS4("c29s005_020") from _call_BlinkXS4_662
    eri "¿Estás celoso? ¿Crees que vas a perder a tu amigo?"
    mc "Ni en broma. Me alegro mucho por Jam y Anthony parece un buen tío. Lo que me jode es no poder seguir usando esa explicación."
    mc "¿Por qué no vas a cortar la electricidad? Quiero desmontar el enchufe, pero quiero sobrevivir a la experiencia."
    call BlinkXS4("c29s005_025") from _call_BlinkXS4_663
    eri "Voy abajo a cortar la luz y ahora subo."
    mc "Mejor quédate abajo. Te mandaré un mensaje cuando haya acabado, para que la vuelvas a conectar."
    mc "No quiero que nadie piense que ha habido un problema y conecte la luz cuando tenga los cables desconectados."
    call BlinkXS4("c29s005_030") from _call_BlinkXS4_664
    eri "OK. Voy a avisar a todo el mundo de que vamos a cortar la luz. Avísame cuando acabes."
    scene c29s005_035a with fade
    "Preparas la linterna que has traído para cuando [eri] corte la luz."
    mcp "(Espero acordarme de todo lo que me explicaron en el instituto sobre enchufes.)"
    scene c29s005_035b with fade
    "Unos minutos después..."
    mcp "(Arreglado y continúo vivo. No era tan complicado. Veamos si ahora no se incendia la casa.)"
    "Mandas un  mensaje a [eri] para que conecte la luz."
    scene c29s005_035c with dissolve
    mcp "(¡No sólo estoy vivo, sino que además funciona!)"
    "Mandas otro mensaje a [eri] para decirle que el enchufe está arreglado. Te contesta que va a avisar a todo el mundo de que el problema está resuelto."
    scene c29s005_035d with fade
    "Decides esperar mientras examinas la habitación. Crees que no habías vuelto desde la irrupción de Eric, Gavin y el resto de los clones."
    "No tuviste tiempo de fijarte demasiado en la decoración aquel día."
    "Esos dos posters han estado ahí desde hace años, cuando [eri] empezó su fase gótica."
    scene c29s005_035e with fade
    "La fotografía la recuerdas, pero los otros dos dibujos son nuevos."
    "El de la chica gótica huyendo del corazón es tan [eri]... Especialmente en la época en que llevaba el pelo largo."
    if eri._var("route"):
        mcp "(Por suerte ya no tiene que huir del amor...)"
        "Viéndolo todo en conjunto, te preguntas si los caballeros de la foto y el dibujo son, de alguna forma, una representación de ti."
    if emm.name.first_name[0] == "E":
        scene c29s005_035f with dissolve
        mcp "(¿Lo ha hecho [emm]? Sabía que tenía talento, pero no tanto.)"
    elif eri.name.first_name[0] == "E":
        scene c29s005_035f with dissolve
        mcp "(¿Lo ha hecho [eri]? No sabía que tuviera talento para dibujar.)"
    scene c29s005_035g with fade
    mcp "(Parece que [eri] se lo pasó bien el verano pasado. No sabía que tantos grupos góticos hacían conciertos en el condado.)"
    scene c29s005_035h with fade
    mcp "(¿[eri] sabe ruso... o el lenguaje que sea en que está escrito ese libro?)"
    if eri._var("route"):
        stop music fadeout (1.5)
        scene c29s005_060d with fade:
            yalign 1.0
            linear 5.0 yalign 0.0
        pause (4.8)
        call BlinkXS3("c29s005_060") from _call_BlinkXS3_796
    else:
        call BlinkXS4("c29s005_040") from _call_BlinkXS4_665
    eri "Antes de que preguntes, el libro no es mío. [eva] se lo dejó anoche aquí. Dice que prefiere leer las cosas en versión original."
    eri "Gracias por arreglar el enchufe. *Risa* Veo que sigues vivo."
    return
label c29s005_noEriLewd:
    if _in_replay:
        $ mc._var("relationships", 0, "set")
        $ eri._var("route", False)
    call c29s005_EriCommon from _call_c29s005_EriCommon
    mc "No hay de qué. Había un cable que no hacía buen contacto. Ha sido fácil."
    play sound ("music/notification.ogg")
    "*Ding*"
    call BlinkXS4("c29s005_045") from _call_BlinkXS4_666
    eri "¿Algo importante?"
    mc "Una notificación sobre un juego."
    scene c29s005_045d with dissolve
    mc "Han publicado unos renders especiales sobre lo que va a pasar en la próxima actualización."
    call BlinkXS4("c29s005_050") from _call_BlinkXS4_667
    eri "¡Joder! ¡Se parece a mí! Bueno, yo no tengo esos ojos ni esas tetas enormes, pero lleva un peinado muy parecido al mío y parece que es gótica."
    mc "*Risa* Pensé lo mismo la primera vez que la vi."
    if persistent.family:
        mc "Pero ella es una extraterrestre."
    else:
        mc "Pero ella es una extraterrestre en vez de una clon."
    scene c29s005_045e with dissolve
    mc "Y espera, que es aún más interesante. Dime que la capitana de su nave no se parece a tu madre. Van a tener un trío en la próxima actualización." id c29s005_noEriLewd_f1f0a978
    mc "*Risa* A veces me parece que me estoy volviendo loco con este juego."
    call BlinkXS4("c29s005_050") from _call_BlinkXS4_668
    eri "¡Hostias! ¡Son casi iguales! Aunque mi madre y yo nunca haríamos un trío, claro."
    eri "*Risa* ¡Y esa tiene las tetas aún más grandes que mi madre!"
    mc "Son muñecas estilizadas. Las proporciones son... un poco extrañas."
    call BlinkXS4("c29s005_055") from _call_BlinkXS4_669
    eri "*Risa* Creo que es una imagen que tardaré en quitarme de la cabeza."
    eri "Pero ahora me tengo que ir a la ducha antes de cenar."
    mc "OK. Yo voy a dejar las herramientas en el sótano de nuevo. Te veo luego."
    scene black with dissolve
    "Vuelves hacia tu casa pensando en lo que ha dicho [eri] sobre un trío con [nor]."
    stop music fadeout (1.5)
    mcp "(Quizás, en otras circunstancias...)"
    return
label c29s005_EriLewd:
    if _in_replay:
        $ mc._var("relationships", 1, "set")
        $ eri._var("route", True)
        call mrS3_emm_route from _call_mrS3_emm_route_21
        call mrS3_dap_route from _call_mrS3_dap_route_13
        call mrS3_nor_route from _call_mrS3_nor_route_13
        call mrS3_eri_pregnant from _call_mrS3_eri_pregnant_2
        if mc._var("relationships")==1:
            call mrS3_rels from _call_mrS3_rels_29
    call c29s005_EriCommon from _call_c29s005_EriCommon_1
    play music ("music/Bolero.ogg")
    mc "¿Crees que me importa el libro cuando apareces así en la habitación?"
    mc "¿Cuándo te has cambiado? ¿Cuándo has cogido la lencería?"
    call BlinkXS4("c29s005_065") from _call_BlinkXS4_670
    eri "*Risa* Sabía que no ibas a morir en el intento de arreglar el enchufe."
    eri "He dejado la lencería en la habitación de mi madre antes de ir a buscarte. Pero ha sido un mal plan."
    mc "*Risa* Déjame dudarlo. Ahora mismo me parece un plan fantástico."
    call BlinkXS4("c29s005_070") from _call_BlinkXS4_671
    eri "Mientras me cambiaba he pensado que, posiblemente, te fueras una vez vieras que la lámpara funcionaba..."
    eri "Me he cambiado muy rápido y no sé si hay algo fuera de su sitio."
    mc "Todo parece estar donde pertenece. Bueno... creo que realmente el sitio de esa lencería es en el suelo."
    call BlinkXS4("c29s005_075") from _call_BlinkXS4_672
    eri "*Risa* Pues tendrás que venir a arrancármela del cuerpo..."
    call BlinkXS4("c29s005_080") from _call_BlinkXS4_673
    eri "*Risa* Es una forma de hablar. Me gusta mucho y no quiero que la rompas. Rectifico a 'quitármela del cuerpo.'"
    mc "*Risa* Me parece una buena opción. Además, si hubieras venido con un látigo, me hubieras dado miedo, pero no hubiera desentonado."
    call BlinkXS4("c29s005_085") from _call_BlinkXS4_674
    eri "*Risa* Esta es la idea que [emm] tiene de la lencería que me gusta... Es la que me trajo del viaje a Monterey."
    mc "¿No te gusta? A mí me parece espectacular."
    if dap._var("route") and emm._var("route"):
        mc "Es de un estilo similar a la que llevabas el día que estuvimos con [emm] y con [dap] en mi habitación."
    scene c29s005_085d with dissolve
    eri "Me gusta, pero para hoy quería algo más... tierno. Más ñoño."
    call BlinkXS4("c29s005_090") from _call_BlinkXS4_675
    eri "Hace mucho que tú y yo no estamos a solas y es posible que sea la última vez antes de que te vayas."
    mc "Entonces, ¿por qué te la has puesto?"
    call BlinkXS4("c29s005_095") from _call_BlinkXS4_676
    eri "Porque [emm] me hizo prometerle que la estrenaría la próxima vez que estuviéramos juntos."
    mc "Vale. Ya te la has puesto y ya has cumplido tu promesa. Ahora es el momento de quitártela."
    mc "No hay nada más tierno que verte sin nada."
    mc "Pero antes..."
    scene c29s005_095d with dissolve
    "Coges a la preciosa mujer entre tus brazos y la besas como si hiciera siglos que no la ves."
    "Los tacones de las botas hacen que sea casi tan alta como tú."
    "El tacto del cuero bajo tus dedos es agradable, pero no supera a la sensación de sus labios sobre los tuyos."
    "Y no superará al tacto de tus dedos sobre su piel desnuda."
    call BlinkXS4("c29s005_100") from _call_BlinkXS4_677
    eri "Creo que es el momento de que empieces a desmontar la lencería. Yo me la he puesto y tú me la tienes que quitar."
    mc "Me gusta cómo suena. *Risa* Trabajo en equipo."
    scene c29s005_105a with dissolve
    mc "Empezaremos con estas correas..."
    scene c29s005_105b with fade
    mc "Mucho mejor así. Da menos impresión de que vayas a sacar un látigo en algún momento y azotarme con él."
    call BlinkXS4("c29s005_110") from _call_BlinkXS4_678
    eri "*Risa* ¿Te gustaría? Nunca te he imaginado en ese rol."
    mc "Dolor y placer no deberían juntarse nunca. ¿Te imaginas a alguien comiendo helado con una muela rota?"
    call BlinkXS4("c29s005_115") from _call_BlinkXS4_679
    eri "*Risa* ¡Me han dolido los dientes sólo de pensarlo! Por muy bueno que estuviera el helado no lo haría nunca."
    mc "Entonces somos de la misma opinión. Mejor dejamos el dolor apartado del placer."
    scene c29s005_105c with dissolve
    mc "Pero es el momento de quitar estos... ¿guantes? ¿Mitones? No sé cómo llamarlos."
    scene c29s005_105d with fade
    eri "Yo tampoco, pero me alegra que ya no esté. Aunque te recuerdo que hay otro en la otra mano."
    scene c29s005_105e with dissolve
    mc "*Risa* No soy un pulpo y además soy un hombre. No puedo hacer dos cosas a la vez."
    scene c29s005_105f with fade
    eri "Aunque hayas tardado, has conseguido que los guantes desaparezcan."
    mc "Más vale ir paso a paso, pero con seguridad."
    call BlinkXS4("c29s005_120") from _call_BlinkXS4_680
    mc "¿Te quito las botas?"
    eri "Sí, pero te vas a reír cuando las quites."
    mc "¿Llevas garras en vez de uñas?"
    call BlinkXS4("c29s005_125") from _call_BlinkXS4_681
    eri "*Risa* No, pero el diseñador de la lencería quiso ahorrar en tela."
    mc "Ahora has despertado mi curiosidad. Siéntate en el sofá."
    scene c29s005_105g with fade
    mc "Veamos a qué te refieres."
    scene c29s005_105h with fade
    mc "*Risa* ¿Qué? ¿Las medias son de broma?"
    eri "*Risa* Sí, solo cubren lo que se ve con las botas. Por eso nunca compro lencería en DAZ. Me gustan más otros diseñadores."
    scene c29s005_105i with fade
    mc "*Risa* No me sorprende. Al menos son fáciles de quitar."
    scene c29s005_105j with dissolve
    mc "La otra pierna no me va a sorprender tanto."
    scene c29s005_105k with fade
    mc "Es igual de bonita que la primera."
    scene c29s005_105l with dissolve
    eri "No empieces con los besos aún. Tienes más ropa que quitar."
    call BlinkXS4("c29s005_130") from _call_BlinkXS4_682
    mc "Pues te vas a tener que volver a levantar. No creo que pueda quitarte el body estando sentada."
    eri "Creo que no. Voy a aprovechar que estoy sentada para desnudarte a ti."
    mc "*Risa* Eres una mujer con muy buenas ideas."
    scene c29s005_105An with dissolve
    eri "Por suerte, eres mucho más rápido de desnudar que yo."
    eri "Hola, Mjolnir."
    eri "Veo que ya está preparado..."
    call BlinkXS4("c29s005_135") from _call_BlinkXS4_683
    mc "Es hora de que te pongas de pie para que pueda acabar con el trabajo."
    eri "Casi estoy tentada de no dejarte acabar... Pero no puedo esperar a que me desnudes del todo tampoco."
    mc "Creo que puedo acabar y entonces pasar a la cama..."
    scene c29s005_105p with dissolve
    eri "Creo que es una idea estupenda."
    scene c29s005_105q with fade
    mc "Yo también lo pienso. Ya te he dicho que no hay nada más tierno que tenerte desnuda delante de mí."
    scene c29s005_095e with dissolve
    "Volvéis a besaros. Ya no hay ropa que se interponga entre vuestras yemas de los dedos y vuestra piel."
    "Por mucho que te guste la lencería, nada supera el tacto de una piel que se va erizando poco a poco."
    call BlinkXS4("c29s005_140") from _call_BlinkXS4_684
    eri "Déjame guardar el edredón y ven a la cama."
    mc "*Risa* Sabes que yo sería de los que tira el edredón al suelo, ¿no?"
    scene c29s005_140d with dissolve
    eri "*Risa* Lo sé. Pero prefiero hacerte esperar un minuto más antes que tirar esto al suelo."
    stop music fadeout (1.5)
    mc "Si las vistas son así, no se puede considerar una espera."
    scene c29s005_145a with fade
    call BlinkXS4("c29s005_145") from _call_BlinkXS4_685
    play music ("music/KindofGirl.ogg")
    eri "¿Estás esperando a algo para venir a la cama conmigo?"
    mc "Estoy esperando a que mi mandíbula se pueda cerrar por sí misma. Estás espectacular, como siempre."
    call BlinkXS4("c29s005_150") from _call_BlinkXS4_686
    eri "Pues ven aquí. Nunca hemos tenido la oportunidad de estar los dos solos en una cama..."
    mc "Hace demasiado que no estamos solos."
    scene c29s005_155a with fade
    call BlinkXS4("c29s005_155") from _call_BlinkXS4_687
    eri "*Risita* Si llego a saber que un enchufe averiado me da la oportunidad de pasar tiempo contigo, lo hubiera roto yo misma."
    mc "*Risa* Sabes que tan solo tienes que pedirlo, ¿verdad?"
    call BlinkXS4("c29s005_160") from _call_BlinkXS4_688
    eri "También puedes pedirlo tú..."
    if mc._var("relationships")==1:
        mc "Sabes que he estado muy ocupado últimamente..."
        call BlinkXS4("c29s005_165") from _call_BlinkXS4_689
        eri "Lo sé, no te preocupes. Pero desde la playa no hemos tenido tiempo de estar solos y lo echaba de menos."
        mc "Tenía muchas ganas de poder dormir contigo una noche..."
    else:
        mc "A veces tengo un problema con eso. No sé si os vais a poner a discutir entre vosotras si te pido que pases la noche conmigo en vez de pedírselo a otra chica."
        mc "No sé si os habéis distribuido turnos o algo por el estilo."
        call BlinkXS4("c29s005_165") from _call_BlinkXS4_690
        eri "Nadie se va a enfadar. Aunque la situación no sea... normal... hemos hablado entre nosotras y lo entendemos."
        eri "Sabemos que tienes poco tiempo disponible, con lo que intentamos darte el espacio que necesitas."
        mc "Pero si un día quiero pasar la noche durmiendo contigo, nadie se va a enfadar, ¿no?"
    scene c29s005_165d with dissolve
    eri "Espero que no sólo sea dormir... "
    mc "Yo también lo espero. Seguramente Mjolnir se enfadaría si solo fuera una noche durmiendo."
    scene c29s005_165e with dissolve
    "La preciosa mujer no quiere seguir charlando. Habrá tiempo para eso después."
    "Es el momento de que vuestros labios hablen sin palabras."
    "Es el momento en que las palabras no son necesarias."
    scene c29s005_170An with dissolve
    "Sus labios dicen todo lo necesario mientras recorren tu torso, repartiendo besos en el camino que lleva a Mjolnir."
    "Produciendo escalofríos de placer que te recorren de arriba a abajo con cada húmedo roce de su boca."
    "Quieres que el recorrido de sus oscuros labios dure para siempre, a la vez que no puedes esperar a que llegue a su destino."
    "La anticipación es una perra mala."
    call BlinkXS4("c29s005_175") from _call_BlinkXS4_691
    eri "¿Puedo?"
    mc "*Risa* Me enfadaré si no lo haces, pero..."
    eri "Pero no te gusta estar pasivo. Lo sé."
    mc "*Risa* Veo que me conoces muy bien."
    eri "*Risa* Entre las chicas hablamos..."
    scene c29s005_180a with fade
    call BlinkXS4("c29s005_180") from _call_BlinkXS4_692
    "Sabes que [eri] era una de las mujeres más generosas del mundo y que tu petición no verbalizada no iba a caer en saco roto."
    eri "¿Mejor así?"
    mc "Totalmente mejor."
    scene c29s005_990pv with dissolve
    show c29s005_990v
    $renpy.sound.play ("music/MoanErika.ogg", loop=True)
    "Aunque esta vez su generosidad tiene un premio especial."
    "En cuanto tu lengua empieza a recorrer su coño, su boca empieza a trabajar sobre Mjolnir en una profunda mamada."
    eri "*Gemido*"
    "La anticipación no solo ha jugado a tu favor, sino también al de ella."
    "Su coño no podría estar más húmedo antes de que empezaras a recorrer cada uno de sus pliegues con tu igualmente húmeda lengua."
    scene c29s005_905pv with dissolve
    show c29s005_905v
    hide c29s005_990v
    "Puedes notar cómo la punta de Mjolnir roza la entrada de su garganta cada vez que sus labios tocan la base de tu polla."
    eri "*Jadeo*"
    "Sus jadeos y gemidos hacen que cada uno de ellos produzca unas vibraciones increíbles en su boca, que se transmiten a tu astil."
    eri "*Gemido*"
    "Mientras tanto, tu lengua no hace más que provocar esos mismos gemidos."
    scene c29s005_900pv with dissolve
    show c29s005_900v
    hide c29s005_905v
    "Ser generoso también tiene premio para ti, aunque no sea lo que provoca tu generosidad."
    "No puedes imaginar el sexo sin buscar el placer de tu compañera antes que el tuyo, aunque eso produzca que tu placer también aumente."
    eri "*Jadeo*"
    "Puedes empezar a notar cómo el cuerpo de [eri] empieza a tensarse bajo tus dedos."
    "Al final tendrás que creerte que tienes una lengua mágica si eres capaz de llevar a la chica al orgasmo tan rápido."
    call OrgasmXS4("c29s005_185") from _call_OrgasmXS4_25
    eri "*GEMIDO* *JADEO* *GEMIDO*"
    "La preciosa pelirroja convertida en morena explota en tus labios, llenando tu boca de sabores extraordinarios, sin dejar de prestar atención a Mjolnir."
    eri "*JADEO* *GEMIDO* *JADEO*"
    scene c29s005_910pv with dissolve
    show c29s005_910v
    hide c29s005_900v
    "Ella ha estado planeando esto desde antes de ir a buscarte a la piscina, excitándose con la idea de que paséis tiempo a solas."
    "La anticipación es una perra mala. Pero es bienvenida en estos casos."
    eri "*GEMIDO*"
    "Los orgasmos llegan uno tras otro, tensando y distendiendo el cuerpo de la hermosa mujer."
    "Aceleras el ritmo de tu lengua para incrementar la potencia de sus clímax."
    call BlinkXS4("c29s005_190") from _call_BlinkXS4_693
    "Inesperadamente, [eri] interrumpe su mamada."
    eri "*Gemido* ¿Te queda mucho para correrte? *Jadeo*"
    mc "Bastante..."
    "No has tenido tanto tiempo de anticipación como ella, para ti ha empezado cuando ha aparecido con la lencería."
    "La perra mala es un dóberman para ella. No le ha dado tiempo de pasar de cachorrito para ti."
    call BlinkXS4("c29s005_195") from _call_BlinkXS4_694
    eri "*Jadeo* ¿Podemos cambiar de postura? *Gemido* Te quiero dentro de mí. *Jadeo*"
    mc "Creo que acabas de decir las palabras mágicas. No hay nada que quiera más ahora mismo."
    scene c29s005_200a with fade
    call BlinkXS4("c29s005_200") from _call_BlinkXS4_695
    "[eri] se quita los pendientes tras decirte que pesan mucho y le están empezando a molestar."
    "Tras unos ajustes en la postura, te colocas entre sus piernas levantadas y apoyas tu glande en la entrada de su vagina."
    mc "¿Preparada?"
    eri "*Risa* Ya no soy virgen, ¿recuerdas? No me tienes que seguir tratando como a una muñeca de porcelana."
    mc "Siempre serás mi muñeca de porcelana. Te recuerdo que la porcelana aguanta el calor mejor que el acero."
    eri "Me gusta como suena. Empieza a mover esas caderas."
    scene c29s005_915pv with dissolve
    show c29s005_915v
    hide c29s005_910v
    "Pocas veces en tu vida te darán una orden que tengas más ganas de obedecer."
    if mc._var("relationships")>1:
        "Aunque con un harén a tu alrededor recibirás muchas órdenes. A veces serán veladas, otras no."
    else:
        "Aunque con una pareja como [eri] recibirás muchas órdenes. A veces serán veladas, otras no."
    eri "*GEMIDO* ¡Cómo echaba de menos esto! *JADEO*"
    if dap._var("route") and emm._var("route"):
        "Sabes que no se refiere sólo al sexo, sino a estar solos, como estuvisteis en la playa."
    else:
        "Sabes que ha pasado demasiado tiempo desde que estuvisteis solos en la playa."
    "Es el momento de corregir ese error. Es el momento de que te entregues, en cuerpo y alma, a la mujer que abraza tu polla con fuerza."
    scene c29s005_930pv with dissolve
    show c29s005_930v
    hide c29s005_915v
    "Su coño, húmedo por su anterior orgasmo, es tan estrecho como siempre. Un hogar para Mjolnir."
    eri "*JADEO* ¡Sigue así! *GEMIDO* ¡Me encanta ese ritmo! *JADEO*"
    "Es un ritmo confortable para ella, con el que la penetras profundamente, golpeando gentilmente su cérvix."
    eri "*GEMIDO* ¡ESTÁS TOCANDO TODOS LOS PUNTOS CORRECTOS! *JADEO*"
    "Es el momento en el que recuerda los consejos de [meg] y empieza a usar sus músculos pélvicos. Una oleada de placer recorre tu polla."
    scene c29s005_920pv with dissolve
    show c29s005_920v
    hide c29s005_930v
    "La textura de la sábana de satén hace que tus piernas se deslicen suavemente, casi como si patinaras hacia tu destino."
    "El sedoso, húmedo, y caliente interior de [eri] hace que ese destino sea perfecto."
    eri "*JADEO* ¡VOY A CORRERME DE UN MOMENTO A OTRO! *GEMIDO*"
    "Su cara, mostrando el placer que recorre su cuerpo, hace que las vistas sean inmejorables."
    "Siempre ha sido expresiva y te encanta que no se retenga durante el sexo."
    scene c29s005_925pv with dissolve
    show c29s005_925v
    hide c29s005_920v
    "No todas las mujeres se preocupan por cómo se ven mientras tienen sexo. [eri] no tiene de qué preocuparse. Está preciosa."
    eri "*GEMIDO* ¡NO PARES! *JADEO* ¡ESTOY A PUNTO! *GEMIDO*"
    "No tenías pensado parar. Esperas recibir toda la presión de su túnel cuando se corra."
    eri "*JADEO* ¡MÁS PROFUNDO! *GEMIDO*"
    "Y puedes notar que está a punto por cómo su cuerpo se comporta. Tu sexto sentido no te falla."
    "¿Quién quiere tener un sexto sentido que permita ver fantasmas si puede elegir uno que detecte orgasmos a punto de llegar?"
    call OrgasmXS4("c29s005_205") from _call_OrgasmXS4_26
    eri "*GEMIDO* ¡SÍ! *JADEO* ¡POR EL AMOR DE DIOS! *GEMIDO*"
    "Y la maravillosa presión hace su aparición, recorriendo tu polla desde la base a la punta con cada embestida."
    "[eri] pierde el control de su cuerpo durante unos alucinantes segundos, mientras es recorrida de arriba a abajo por oleadas de placer."
    eri "*JADEO* ¡MÁS DURO! *GEMIDO*"
    scene c29s005_935pv with dissolve
    show c29s005_935v
    hide c29s005_925v
    "La agarras por las muñecas y te inclinas sobre ella, evitando poner todo tu peso sobre sus antebrazos."
    "Apenas has parado de bombear durante un par de segundos por el cambio de postura."
    eri "*GEMIDO* ¡ASÍ! *JADEO* ¡FÓLLAME ASÍ! *GEMIDO*"
    "Tus caderas dan golpes secos que acaban en vuestras pelvis encontrándose con un sonido húmedo."
    "Su coño sigue cerrándose alrededor de Mjolnir como si de ello dependiera su vida y tu polla fuera un clavo ardiente."
    scene c29s005_940pv with dissolve
    show c29s005_940v
    hide c29s005_935v
    "No es una mala comparación. A pesar de la humedad, parece que Mjolnir esté a punto de ponerse a arder."
    eri "*JADEO* ¡NO PUEDO PARAR DE CORRERME! *GEMIDO* ¡ESTO ES ALUCINANTE! *JADEO*"
    "Poco a poco tu propio orgasmo empieza a trepar por tus pantorrillas en la conocida y bienvenida sensación."
    eri "*GEMIDO* ¡SIGUE ASÍ! *JADEO* ¡ME ENCANTA! *GEMIDO*"
    "Aún te queda un poco para llegar y, si eres capaz de aguantar, sabes que puedes hacer que tenga una decena más de orgasmos."
    scene c29s005_950pv with dissolve
    show c29s005_950v
    hide c29s005_940v
    "Tienes que intentar retrasar tu orgasmo todo lo posible para poder disfrutar de las expresiones que recorren la cara de [eri]."
    "La visión de sus perfectas tetas moviéndose al ritmo de tus embestidas hace difícil pensar en cualquier otra cosa."
    eri "*JADEO* ¡MAÑANA ME VA A DOLER TODO! *GEMIDO* ¡PERO NO PARES! *JADEO*"
    "El punto de no retorno se está acercando para ti, pero no tienes intención de parar hasta alcanzarlo."
    "Ver su cara mostrando el placer que tu bombeo produce en ella te hace querer seguir durante horas."
    scene c29s005_945pv with dissolve
    show c29s005_945v
    hide c29s005_950v
    "Aunque sabes que no vas a poder durar horas. Al menos en el primer asalto."
    eri "*GEMIDO* ¡SIGUE! *JADEO* ¡DAME TU LECHE! *GEMIDO*"
    "Tu orgasmo ya se ha arrastrado hasta tus muslos. No vas a poder contenerlo mucho más y [eri] empieza a notar los casi imperceptibles cambios en tu ritmo."
    eri "*JADEO* ¡NO SE TE OCURRA SACARME LA POLLA DE DENTRO! *GEMIDO*"
    "Te empieza a conocer tan bien como la conoces tú a ella y sabe que tu clímax está por llegar."
    if persistent.pregnancy and not eri._var("pregnant"):
        if persistent.walkthrough:
            $ wt1 = _("[eri] embarazada.")
            $ wt2 = _("Sin consecuencias.")
        else:
            $ wt1 = ""
            $ wt2 = ""
        menu:
            "Correrte dentro. Ir a por el bebé." (wt = wt1):
                $ eri._var("pregnant", True)
                $ eri._var("undiscoveredPregnancy", True)
                play sound ("music/OldMusicBox5.ogg")
            "Correrte dentro." (wt = wt2):
                pass
    $ resetWalkthrough ()
    call OrgasmXS4("c29s005_210") from _call_OrgasmXS4_27
    hide c29s005_945v
    mc "¡Mpfft!"
    "Sin poder retrasarlo más, te corres dentro de la preciosa mujer, llenándola hasta que su coño no puede aguantar toda tu leche en su interior."
    eri "*GEMIDO* ¡HAY MUCHÍSIMA! *JADEO*"
    stop sound fadeout (1.5)
    "Nunca te cansarás de estos momentos con [eri], en los que vuestros orgasmos se solapan uno con otro y vuestros fluidos se mezclan entre sí."
    scene c29s005_215a with fade
    call BlinkXS4("c29s005_215") from _call_BlinkXS4_696
    stop music fadeout (1.5)
    "Os quedáis inmóviles unos segundos, mientras las últimas oleadas de placer abandonan vuestros cuerpos."
    play music ("music/Majestica.ogg")
    mc "¿Qué tal?"
    eri "Tan increíble como la primera vez. Incluso mejor. Me parece que hace mil años de los nervios de aquel día."
    eri "¿Y para ti?"
    mc "Pienso lo mismo. *Risa* Y hoy no tendremos arena que se nos meta en el culo."
    call BlinkXS4("c29s005_220") from _call_BlinkXS4_697
    eri "*Risa* Tienes razón. Hay sitios donde la arena no debería llegar nunca."
    call BlinkXS4("c29s005_225") from _call_BlinkXS4_698
    eri "Pero ahora deberías soltarme las muñecas o me acabarán doliendo. Pesas un poco."
    "Te das cuenta de que, tras correrte, has apoyado más peso del que esperabas en sus antebrazos."
    mc "*Risa* Es una forma diplomática de llamarme gordo. Pero también es una oportunidad para tumbarnos abrazados."
    call BlinkXS4("c29s005_230") from _call_BlinkXS4_699
    eri "Eso es lo mejor del sexo, ¿no? Los abrazos de después."
    mc "Si no es lo mejor, está entre las mejores cosas."
    scene c29s005_235a with fade
    call BlinkXS4("c29s005_235") from _call_BlinkXS4_700
    "Tras el cambio de postura..."
    eri "Sabes que te voy a echar mucho de menos cuando estés en Aruba, ¿verdad?"
    mc "Y yo a ti. Pero puedes venir algún fin de semana cuando empieces la universidad."
    mc "Si vas a dejar de trabajar en el café, tendrás los fines de semana libres."
    call BlinkXS4("c29s005_240") from _call_BlinkXS4_701
    eri "No me acostumbro a tener dinero. Lo primero en lo que he pensado ha sido en cómo voy a ir si ya no trabajo."
    mc "Lo que me sorprende es que sigas trabajando después de haber cobrado el cheque de NTR."
    mc "Después de eso, tu sueldo en el café casi tiene que parecer calderilla."
    call BlinkXS4("c29s005_245") from _call_BlinkXS4_702
    eri "Me comprometí con Luca, el dueño del café, a trabajar hasta que empezara la universidad."
    eri "No me parecía correcto dejarlo en la estacada sólo porque haya cobrado un dinero inesperado."
    mc "Esas cosas son las que hacen de ti una persona maravillosa."
    mc "Yo habría dejado el trabajo sin dudarlo para poder tener más tiempo libre en el último verano antes de empezar la universidad."
    call BlinkXS4("c29s005_250") from _call_BlinkXS4_703
    eri "No lo hubieras hecho. Te pasaste dos años trabajando en Portland todos los fines de semana y festivos sin poder venir a casa."
    eri "Y, por lo que me dijiste, incluso ganaste lo suficiente como para ahorrar bastante dinero."
    eri "Podías haberlo dejado unos meses antes de acabar la carrera, pero no lo hiciste. ¿Por qué?"
    mc "*Risa* Tienes razón. Porque me había comprometido con mi jefe."
    call BlinkXS4("c29s005_255") from _call_BlinkXS4_704
    eri "*Risa* Somos un par de idiotas demasiado responsables."
    mc "*Risa* Supongo que es para compensar la falta de responsabilidad de [emm]."
    mc "¿Te imaginas lo que hubiera hecho ella en tu posición?"
    call BlinkXS4("c29s005_260") from _call_BlinkXS4_705
    eri "*Risa* Hubiera entrado en el café el día siguiente haciendo así con las dos manos."
    eri "*Risa* Y le hubiera tirado el uniforme a la cara a Luca."
    mc "*Risa* No me extrañaría. Pero ese Luca, ¿Tan mal jefe es?"
    call BlinkXS4("c29s005_265") from _call_BlinkXS4_706
    eri "¡Qué va! Es un buen tipo. Pero [emm] estaría en modo 'ya no necesito este trabajo'."
    eri "No pensaría en dejar la puerta abierta para poder volver algún día o en quedar bien. Ya la conoces."
    mc "*Risa* Creo que puedes eliminar todo lo que hay después de 'No pensaría' en esa frase."
    call BlinkXS4("c29s005_270") from _call_BlinkXS4_707
    eri "*Risa* Eres un capullo. Pero tienes razón. Aunque ha cambiado mucho en el último mes."
    eri "Creo que le ha hecho bien que estés por aquí. No sé cómo se va a comportar cuando te vayas."
    mc "Le tenemos que buscar algo que hacer; darle alguna responsabilidad con las chicas nuevas o algo así."
    mc "Y, obviamente, nombrar a alguien para que la supervise."
    call BlinkXS4("c29s005_275") from _call_BlinkXS4_708
    eri "A mí no me nombres supervisora. Pasaré algunos fines de semana en Aruba con mi novio."
    mc "Espero haber encontrado algún sitio chulo donde llevarte a cenar cuando vengas."
    call BlinkXS4("c29s005_280") from _call_BlinkXS4_709
    eri "Hablando de cenar... ¿Tienes hambre? El sexo me da hambre."
    mc "Ya casi es la hora de cenar. Nos deberíamos ir vistiendo y bajar, ¿no?"
    call BlinkXS4("c29s005_285") from _call_BlinkXS4_710
    eri "Tengo otro plan. No tengo ganas de vestirme."
    eri "Tú no te mueves de aquí. Hoy vas a pasar la noche conmigo."
    mc "¿No tengo opinión sobre eso?"
    call BlinkXS4("c29s005_290") from _call_BlinkXS4_711
    eri "¿Acaso tienes una opinión diferente?"
    mc "*Risa* No. Mi intención era que nos vistiéramos, bajar a cenar y después volver aquí."
    call BlinkXS4("c29s005_295") from _call_BlinkXS4_712
    eri "*Risa* Para eso no es necesario que nos vistamos. Te he dicho que tenía un plan, y mis planes funcionan mejor que los de [emm]."
    eri "Déjame mandarle un mensaje a mi madre para que nos suba algo."
    mc "OK... Pero..."
    call BlinkXS4("c29s005_300") from _call_BlinkXS4_713
    if nor._var("route"):
        eri "No va a ver nada que no haya visto ya. Yo no tengo intención de vestirme."
        mc "Tienes razón. Aún no me acostumbro a esto."
    else:
        eri "Puedes ponerte una almohada tapando a Mjolnir si te avergüenza que te vea desnudo. Yo no tengo intención de vestirme."
        mc "Desde aquel día en que me pilló en la ducha, después de la batalla de pintura, creo que ya no le sorprende nada."
    if mc._var("relationships")==1:
        mc "Y me alegra que todo el mundo sepa que estamos juntos."
    else:
        mc "Y me alegra que todas mis relaciones sean públicas."
    scene c29s005_300d with fade
    "Al cabo de un rato..."
    play sound ("music/knock.ogg")
    "*Knock-Knock*"
    nor "*A través de la puerta* ¿Puedo pasar? Os traigo la cena."
    eri "Pasa, Mamá."
    stop music fadeout (1.5)
    "Ni siquiera te pones el cojín encima para tapar a Mjolnir."
    return
label c29s005_noNorLewd:
    if _in_replay:
        call mrS3_eri_pregnant from _call_mrS3_eri_pregnant_3
    call BlinkXS4("c29s005_305") from _call_BlinkXS4_714
    play music ("music/LifeOfAWanderingWizard.ogg")
    nor "*Risa* Parece que alguien se lo está pasando bien aquí."
    "No se sorprende por veros desnudos a los dos. Haber salido a la luz tiene sus ventajas."
    nor "Recuerda abrir la ventana por la mañana. *Risita* Esto huele a sexo."
    call BlinkXS4("c29s005_310") from _call_BlinkXS4_715
    eri "No te preocupes, Mamá. Dormiremos con la ventana abierta."
    eri "El olor no va a hacer más que incrementarse en cuanto cenemos."
    call BlinkXS4("c29s005_315") from _call_BlinkXS4_716
    nor "Bueno, os dejo. Que aproveche."
    mc "Gracias, [nor]."
    nor "No me des las gracias y cuida bien de mi niña. No sé si vais a tener muchas más oportunidades de pasar una noche juntos antes de que te vayas."
    stop music fadeout (1.5)
    mc "No te preocupes. La cuidaré lo mejor que pueda."
    play music ("music/LePrunierenFleur.ogg")
    scene c29s005_320a with dissolve
    "Cenáis en el sofá de [eri], entre besos y risas."
    "Tu padre siempre estuvo en contra de que tuvierais sofás en las habitaciones. Decía que evitaría que hicierais cosas en familia."
    "Se equivocaba."
    scene c29s005_320An with dissolve
    "Pasáis el resto de la noche probando casi cada superficie posible, horizontal o vertical, donde hacer el amor."
    "Donde follar. Donde comeros el uno al otro."
    "La cena queda medio olvidada en el sofá de [eri], excepto cuando apartáis la bandeja para probar el postre."
    if persistent.pregnancy and not eri._var("pregnant"):
        "Es la última oportunidad de dejar a [eri] embarazada antes del viaje a Aruba."
        menu:
            "¿Quieres dejarla embarazada para que desarrolle la barriga cuando vuelvas?"
            "Sí":
                $ eri._var("pregnant", True)
                $ eri._var("undiscoveredPregnancy", True)
                play sound ("music/OldMusicBox5.ogg")
            "No":
                pass
    scene c29s005_325d with fade
    stop music fadeout (1.5)
    "Al cabo de bastantes horas, el agotamiento puede con vosotros y cuando estáis a punto de dar la noche por finalizada..."
    play sound ("music/notification.ogg")
    "*Ding-Ding*"
    eri "¿Es tu móvil? ¿A estas horas de la noche? ¿Quién puede ser?"
    play music ("music/Memories-Instrumental.ogg")
    mc "Será un email o una notificación. Voy a verlo."
    scene c29s005_045f with dissolve
    mc "*Risa* Es una notificación de un juego. Han publicado unos renders especiales."
    mc "Hay una chica que se parece a ti; y mira la capitana de su nave. Dime que no me estoy volviendo loco y que no se parece a tu madre."
    call BlinkXS4("c29s005_325") from _call_BlinkXS4_717
    eri "¡Joder! Si no fuera por los ojos enormes y porque tiene un cuerpo raro, te diría que es clavada a ella."
    mc "Yo pensé lo mismo la primera vez que la vi."
    eri "Pero tiene unas tetas incluso más grandes que las de mi madre."
    call BlinkXS4("c29s005_330") from _call_BlinkXS4_718
    eri "Me parece que me tendrás que explicar esa historia un día que tenga menos sueño y esté menos cansada."
    mc "Cuando quieras, pero creo que tienes razón. Es hora de que durmamos los dos solos por primera vez."
    eri "Si los abrazos son lo mejor del sexo, espero que dormir juntos sea incluso mejor."
    scene c29s005_330d with dissolve
    "Lo descubrís muy pronto, después de abrir la ventana para que entre el fresco aire nocturno."
    "Dormir juntos es fantástico."
    "Te despiertas un par de veces, cuando [eri] se mueve y la zona de tu piel en la que estaba se queda fría sin su contacto."
    stop music fadeout (1.5)
    "Pero siempre hay una parte de tu piel tocando la suya durante toda la noche."
    return
label c29s005_NorLewd:
    if _in_replay:
        $ mc._var("relationships", 2, "set")
        call mrS3_nor_pregnant from _call_mrS3_nor_pregnant_3
        call mrS3_eri_pregnant from _call_mrS3_eri_pregnant_4
        call mrS3_dap_route from _call_mrS3_dap_route_14
        call mrS3_emm_route from _call_mrS3_emm_route_22
        if mc._var("relationships")<3:
            call mrS3_rels from _call_mrS3_rels_30
    scene c29s005_335d with fade:
        yalign 1.0
        linear 5.0 yalign 0.0
    pause (4.8)
    call BlinkXS3("c29s005_335") from _call_BlinkXS3_797
    play music ("music/LePrunierenFleur.ogg")
    nor "*Risa* Parece que alguien se lo está pasando bien aquí."
    "No se sorprende por veros desnudos a los dos. Haber salido a la luz tiene sus ventajas."
    mc "*Risa* Y parece que te has vestido para unirte."
    call BlinkXS4("c29s005_340") from _call_BlinkXS4_719
    nor "El mensaje de [eri] decía 'Trae la cena para [mc], para ti, y para mí. Vístete sexy'. Y le he hecho caso."
    nor "Aquí está la cena y creo que esta lencería es de las más sexys que tengo."
    call BlinkXS4("c29s005_310") from _call_BlinkXS4_720
    eri "Te queda espectacular. Creo que es de los conjuntos más bonitos que te he visto."
    mc "Estoy de acuerdo contigo. Pero creo que está en desventaja, ¿no?"
    call BlinkXS4("c29s005_345") from _call_BlinkXS4_721
    nor "¿A qué te refieres?"
    mc "Nosotros ya estamos desnudos y tú aún estás vestida. Si vas a unirte, creo que debemos solucionar eso."
    nor "¿Antes de cenar?"
    call BlinkXS4("c29s005_350") from _call_BlinkXS4_722
    eri "*Risa* Creo que, ahora mismo, [mc] tiene más hambre de ti que de comida."
    mc "*Risa* Me conoces demasiado bien. No podría estar cenando sin pensar en lo que vendrá después."
    call BlinkXS4("c29s005_360") from _call_BlinkXS4_723
    eri "Pues puedes empezar a desnudarla antes de que lo haga ella. Ha sido muy sexy cuando me desnudabas a mí."
    eri "Quiero ver como desnudas a mi madre."
    if not persistent.family:
        mcp "(A veces me sorprende que la siga tratando como a su madre después de descubrir que es un clon.)"
        mcp "(Pero si yo puedo tratar a [mar] como a mi madre, aunque siempre supe que no lo es, me alegro de que [eri] siga haciéndolo con [nor].)"
    call BlinkXS4("c29s005_355") from _call_BlinkXS4_724
    "[nor] se inclina de forma poco natural para dejar la bandeja, realzando con el gesto sus partes más curvilíneas y usando la corta bata para ello." id c29s005_NorLewd_a62b414c
    nor "Permíteme que deje la bandeja aquí o lo vas a tener muy complicado. *Risita*"
    "Atrás quedó aquel tiempo en que pensaba que no era sexy."
    mc "Te gusta provocarme, ¿verdad? Estoy seguro de que sabes que la bata no te cubre el culo del todo."
    nor "*Risa* No puedo imaginarme a qué te refieres... Pero sí. Me encanta provocarte."
    call BlinkXS4("c29s005_365") from _call_BlinkXS4_725
    nor "*Risita* Además, mí me parece que sí que lo cubre..."
    mc "*Risa* Te aseguro que antes no lo cubría. Pero no voy a empezar a discutir sobre posiciones ahora mismo."
    mc "Habrá tiempo para eso luego. Ahora tengo una bata que quitar."
    nor "Empieza a quemarme sobre la piel..."
    scene c29s005_365d with dissolve
    mc "Sea como sea, estoy de acuerdo con [eri]. Te queda espectacular."
    eri "Es que mi madre tiene las curvas muy bien puestas. Justo en su sitio."
    nor "*Risa nerviosa* Al final me haréis ruborizar y no sabréis dónde empieza la lencería y dónde acaba mi piel."
    scene c29s005_365e with fade
    "Te acercas a [nor] y, tras retirar la bata de su hombro, plantas un tierno beso en su piel."
    mc "*Smooch*"
    "Quieres dejar sus labios para el final, cuando no haya más piel que desnudar."
    scene c29s005_365f with fade
    nor "*Gemido* Me acabas de poner la piel de gallina."
    "Esa era la idea, ¿no? Retrasas el momento de retirar tus labios unos segundos."
    "Pero tienes otro hombro que descubrir, y una preciosa mujer esperándoos en la cama, con lo que no puedes entretenerte demasiado."
    scene c29s005_365g with fade
    "El segundo hombro es tan suave como el primero. Tus labios se entretienen en él por igual."
    nor "*Jadeo* Me estás matando de anticipación."
    "La anticipación sigue siendo una perra mala. Una perra enorme en este caso."
    call BlinkXS4("c29s005_370") from _call_BlinkXS4_726
    eri "Me está matando a mí, y eso que yo sólo estoy esperando a que acabe..."
    eri "Quítale la bata antes de que inunde mi habitación con tanta humedad."
    scene c29s005_375a with fade
    "Sigues las instrucciones de la dueña de la habitación. No quieres tener que interrumpir la sesión para ir a buscar una fregona."
    "Te apartas un par de pasos para observar la obra de arte que es el cuerpo de [nor]."
    mc "*Silbido* Realmente increíble. Estás preciosa."
    mc "Date la vuelta, por favor. Quiero verte en cada ángulo."
    scene c29s005_375pv
    scene c29s005_375dv
    $ renpy.movie_cutscene("c29/c29s005_375vid.webm")
    "[nor] sabe perfectamente como provocarte y, dando un extraño giro sobre un solo pie, acaba en una postura que sabe que realza su perfecto culo."
    nor "¿Has podido verlo todo o tengo que repetirlo?"
    call BlinkXS4("c29s005_380") from _call_BlinkXS4_727
    hide c29s005_375vid
    eri "*Risa* Creo que se ha cortocircuitado. Ahora el peligro de inundación está en él babeando."
    mc "*Risa* No me he cortocircuitado, pero... ¿tú has visto ese culo?"
    call BlinkXS4("c29s005_385") from _call_BlinkXS4_728
    eri "*Risa* Claro que lo he visto. Y estoy esperando que quites el resto de ropa para que se nos una."
    if persistent.walkthrough:
        $ wt1 = _("Sin contenido lésbico... de momento.")
        $ wt2 = _("Sin consecuencias.")
    else:
        $ wt1 = ""
        $ wt2 = ""
    menu:
        "¿Quieres que [eri] te ayude a desnudar a [nor]?"
        "Si" (wt=wt1):
            $ eri._var("helpedNorah1", True)
            call c29s005_EriHelp1 from _call_c29s005_EriHelp1
        "No" (wt=wt2):
            $ eri._var("helpedNorah1", False)
            call c29s005_noEriHelp1 from _call_c29s005_noEriHelp1
    scene c29s005_440a with fade
    stop music fadeout (1.5)
    "Unos segundos después..."
    play music ("music/SensualJazzMedium2.ogg")
    mc "¿Cómo queréis proceder?"
    eri "Creo que quiero que sigas comiéndole el coño a mi madre. Quiero verla disfrutar."
    nor "¿Y tú?"
    scene c29s005_440b with dissolve
    eri "Yo le dedicaré atenciones a Mjolnir, preparándolo para ti."
    "Las palabras de [eri] provocan un pequeño espasmo de anticipación en tu polla."
    nor "O para ti. Yo voy a estar demasiado ocupada corriéndome en la boca de [mc]."
    mc "¿Podemos empezar y dejar la logística para luego?"
    scene c29s005_440c with dissolve
    eri "Este es un paso muy importante para las dos..."
    nor "No siempre puedes tener el primer trío con tu hija..."
    mc "Y hablar de ello no lo va a hacer más fácil. Hacerlo sí."
    nor "Tienes razón. Túmbate."
    $renpy.sound.play ("music/MoanNorah.ogg", loop=True)
    scene c29s005_975pv with fade
    show c29s005_975v
    "En el momento en que dejan de pensar, las dos fieras en la cama empiezan a actuar, con [nor] cabalgando tu boca mientras [eri] lame tu astil."
    nor "*Gemido* Me encanta... *Jadeo*"
    "Pero a [nor] siempre le ha gustado el sabor de Mjolnir y no pierde ocasión de metérselo en la boca de vez en cuando, ayudada por [eri]."
    nor "*Jadeo* Sabe diferente... *Gemido*"
    eri "Sabe a mí..."
    "Los restos del último orgasmo de [eri] aún deben estar aromatizando tu polla."
    scene c29s005_980pv with dissolve
    show c29s005_980v
    hide c29s005_975v
    "Mientras ellas degustan los fluidos de [eri] en tu polla, tú no dejas pasar la oportunidad de degustar los de [nor]."
    "Has podido notar, cuando le estabas quitando la bata, lo cachonda que se estaba poniendo. Más aún teniendo en cuenta que [eri] estaba mirando."
    nor "*Gemido* ¡Sigue ahí! *Jadeo* ¡Has encontrado el punto justo! *Gemido*"
    eri "*Risa juguetona* No debe ser fácil con ese enorme culo."
    nor "*Risa* Mañana voy a hacer ensalada de berros para comer. *Jadeo* Solo para ti. *Gemido*" id c29s005_NorLewd_3c00737e
    "Si tu mayor enemigo culinario es el brócoli, el de [eri] han sido siempre los berros."
    eri "*Risa* ¡Noooo!"
    scene c29s005_985pv with dissolve
    show c29s005_985v
    hide c29s005_980v
    "Obviamente, la amenaza de [nor] es fingida. Crees que no han entrado berros en la nevera desde hace años."
    "También crees que Mjolnir ya no puede crecer más, debido a las atenciones que las dos mujeres le están dedicando."
    eri "Creo que ya lo tienes a punto."
    nor "*Jadeo* No pienso bajar de aquí. *Gemido* Quiero ver cómo te folla. *Jadeo*"
    "Después del sexo con [eri], la proposición de [nor] casi te pilla por sorpresa, pero la entiendes perfectamente."
    "La complicidad entre madre e hija es enorme, y [nor] quiere disfrutar la escena a la vez que lo hace [eri]."
    stop sound fadeout (1.5)
    "[eri] no discute con su madre."
    scene c29s005_835pv with fade
    show c29s005_835v
    hide c29s005_985v
    $renpy.sound.play ("music/MoanErika.ogg", loop=True)
    "Tras ajustar las posturas, la gótica se empala en Mjolnir y empieza a cabalgarte a un ritmo lento."
    eri "*Gemido* Adoro el sexo a solas con [mc]. *Jadeo* Pero hacer esto contigo es increíble. *Gemido*"
    "Sabes a qué se refiere. Pese a que el culo de [nor] te tapa las vistas, te puedes imaginar que se están mirando a los ojos mientras una cabalga tu polla y la otra tu boca."
    nor "*Jadeo* Hay un momento y un lugar para todo. *Gemido* Y ya era hora de que hiciéramos esto juntas. *Jadeo*"
    "Después de la conversación que has tenido con [kia] y [sim], pensar que, mientras veníais hacia casa de [nor], [eri] ya estaba planeando esto..."
    "Cada vez adoras más a esta mujer. Sin su mensaje pidiendo la cena, esto no hubiera sido posible."
    scene c29s005_440d with dissolve
    "La complicidad entre las dos queda demostrada en que te están cabalgando, pero ambas se están dando la mano al mismo tiempo."
    "Es una experiencia compartida entre las dos, la primera vez que tienen sexo juntas sin contar aquel día en la piscina."
    stop sound fadeout (1.5)
    "Y, pese a todo, no te sientes un simple espectador, sino parte integral de una experiencia maravillosa para dos mujeres a las que amas."
    scene c29s005_965pv with fade
    show c29s005_965v
    hide c29s005_835v
    $renpy.sound.play ("music/MoanNorah.ogg", loop=True)
    eri "*GEMIDO* ¡Joder! *JADEO* Me pone cachondísima ver cómo te come. *GEMIDO*"
    "Mientras te cabalga, adelante y atrás, haciéndote sentir cada pliegue de su vagina, la chica te está acercando al séptimo cielo mientras tú las acercas a las dos."
    nor "*JADEO* ¡Es la mejor comida de coño en la historia de las grandes comidas de coño! *GEMIDO*"
    "Tu técnica no ha cambiado. La única diferencia es que ahora está viendo cómo disfruta [eri] del sexo."
    stop sound fadeout (1.5)
    "Sois una familia en la que os gusta hacer disfrutar a los demás, y ver cómo su hija está a punto de llegar al orgasmo hace que la experiencia para [nor] sea aún mejor."
    scene c29s005_830pv with fade
    show c29s005_830v
    hide c29s005_965v
    $renpy.sound.play ("music/MoanErika.ogg", loop=True)
    "Sabes que esta escena se va a repetir muchas veces a lo largo de los años."
    nor "*GEMIDO* ¡ESTOY A PUNTO DE LLEGAR! *JADEO*"
    "Con tus manos en su culo, puedes notar cómo sus músculos empiezan a tensarse."
    eri "*JADEO* ¡YO TAMBIÉN! *GEMIDO*"
    "La única pega que le encuentras a esta postura es que prácticamente no puedes ver a [eri] ni anticipar sus movimientos."
    "Está más sensible que [nor] por el sexo de hace un rato, y la cabalgata sobre Mjolnir la está llevando al límite."
    nor "*GEMIDO* ¡CÓRRETE PARA NOSOTROS! *JADEO*"
    call OrgasmXS4("c29s005_445") from _call_OrgasmXS4_28
    eri "*GEMIDO* ¡JODER, JODER, JODER! *JADEO* ¡SÍ! *GEMIDO*"
    "[eri] no puede retener más el orgasmo y su coño se abre como una presa dejando escapar todos sus fluidos."
    stop sound fadeout (1.5)
    "Los espasmos en su vagina empiezan a masajear tu polla como si le fuera la vida en ello."
    call OrgasmXS4("c29s005_450") from _call_OrgasmXS4_29
    $renpy.sound.play ("music/MoanNorah.ogg", loop=True)
    nor "*JADEO* ¡YO TAMBIÉN! *GEMIDO* ¡ME CORROO! *JADEO*"
    if persistent.family:
        "Ver a su hija correrse, hace que [nor] también explote. Ella lo hace en tu boca."
    else:
        "Ver a su hija correrse, aunque no sea su hija biológica, hace que [nor] también explote. Ella lo hace en tu boca."
    "Su orgasmo llena tus papilas gustativas y tu olfato del reconocible olor y sabor de [nor]."
    if not persistent.lesbian:
        if persistent.pregnancy and not eri._var("pregnant"):
            if persistent.walkthrough:
                $ wt1 = _("[eri] embarazada.")
                $ wt2 = _("Sin consecuencias.")
            else:
                $ wt1 = ""
                $ wt2 = ""
            menu:
                "Correrte dentro. Ir a por el bebé." (wt = wt1):
                    $ eri._var("pregnant", True)
                    $ eri._var("undiscoveredPregnancy", True)
                    play sound ("music/OldMusicBox5.ogg")
                "Correrte dentro." (wt = wt2):
                    pass
            $ resetWalkthrough ()
        call OrgasmXS4("c29s005_455a") from _call_OrgasmXS4_30
        hide c29s005_830v
        mc "¡Mpfft!"
        "Las sensaciones que recorren tu polla, sumadas a las que notas en tu boca hacen que te corras dentro de [eri] sin poder remediarlo."
        eri "*GEMIDO* ¡SÍ! *JADEO* DÁMELA TODA. *GEMIDO*"
        nor "*JADEO* LLÉNALA. *GEMIDO* ES LO MÁS BONITO QUE HE VISTO NUNCA. *JADEO*"
        stop sound fadeout (1.5)
        "Supones que no se refiere a verte correrte dentro de [eri], sino a los orgasmos casi simultáneos de los tres."
    else:
        scene c29s005_450An with dissolve
        stop sound fadeout (1.5)
        "Aunque no lo veas, pero puedes notar el cambio de postura y jurarías que, en medio de sus orgasmos, han empezado a besarse."
        nor "*GEMIDO* *SMOOCH* *JADEO*"
        eri "*JADEO* *SMOOCH* *GEMIDO*"
        $renpy.sound.play ("music/MoanErika.ogg", loop=True)
        "Aparte del cambio de postura, el sonido de los besos te confirma que tu intuición es correcta. Te gustaría poder ver ese momento especial entre ambas."
        scene c29s005_955pv with fade
        show c29s005_955v
        hide c29s005_830v
        "El larguísimo beso no evita que te sigan cabalgando. Aquel día en la piscina empezó algo entre ellas y hoy llega a su punto álgido."
        nor "*JADEO* *SMOOCH* *GEMIDO*"
        "Tampoco les afecta que sigan corriéndose, con los orgasmos llegando en rápida sucesión uno tras otro."
        eri "*GEMIDO* *SMOOCH* *JADEO*"
        stop sound fadeout (1.5)
        "A veces te preguntas si podrías mantener esa coordinación en medio de una oleada de orgasmos. O dos oleadas recorriendo los dos preciosos cuerpos."
        scene c29s005_960pv with fade
        show c29s005_960v
        hide c29s005_955v
        $renpy.sound.play ("music/MoanNorah.ogg", loop=True)
        "Pese a todo, sus movimientos no pierden un ritmo sincronizado por el tacto de sus manos sobre sus cuerpos y sus dedos entrelazados."
        "Cada una sabe cómo se va a mover la otra antes de que el movimiento se produzca. Sus labios unidos ayudan a que los movimientos se produzcan al unísono."
        eri "*JADEO* *SMOOCH* *GEMIDO*"
        nor "*GEMIDO* *SMOOCH* *JADEO*"
        "Sus bocas rozándose evitan que puedan decir alguna palabra. No es necesario. Sus labios dicen todo lo que tienen que decirse."
        stop sound fadeout (1.5)
        "En ese momento piensas que fue una mala idea hacer que [eva] retirara las cámaras."
        scene c29s005_970pv with fade
        show c29s005_970v
        hide c29s005_960v
        $renpy.sound.play ("music/MoanErika.ogg", loop=True)
        "Sigues comiéndote el coño de [nor] mientras perforas el de [eri], notando cómo tu orgasmo está a punto de llegar."
        "Dos coños chorreantes te están acercando rápidamente a tu límite. El sonido que hacen al besarse colabora en que la escena sea una de las más calientes que has vivido."
        mc "Estoy a punto de correrme..."
        eri "*JADEO* *SMOOCH* *GEMIDO*"
        nor "*GEMIDO* *SMOOCH* *JADEO*"
        "Ninguna de las dos hace ningún gesto que indique que vayan a interrumpir su cabalgata o su beso."
        "Es un momento de comunión entre los tres que guardaréis en vuestra memoria para el resto de vuestra vida."
        if persistent.pregnancy and not eri._var("pregnant"):
            if persistent.walkthrough:
                $ wt1 = _("[eri] embarazada.")
                $ wt2 = _("Sin consecuencias.")
            else:
                $ wt1 = ""
                $ wt2 = ""
            menu:
                "Correrte dentro. Ir a por el bebé." (wt = wt1):
                    $ eri._var("pregnant", True)
                    $ eri._var("undiscoveredPregnancy", True)
                    play sound ("music/OldMusicBox5.ogg")
                "Correrte dentro." (wt = wt2):
                    pass
            $ resetWalkthrough ()
        call OrgasmXS4("c29s005_455b") from _call_OrgasmXS4_31
        hide c29s005_970v
        mc "¡Mpfft!"
        "Las sensaciones que recorren tu polla, sumadas a las que notas en tu boca hacen que te corras dentro de [eri] sin poder remediarlo."
        eri "*GEMIDO* ¡SÍ! *JADEO* DÁMELA TODA. *GEMIDO*"
        nor "*JADEO* LLÉNALA. *GEMIDO* ES LO MÁS BONITO QUE HE VISTO NUNCA. *JADEO*"
        "Supones que no se refiere a verte correrte dentro de [eri], sino a los orgasmos casi simultáneos de los tres."
        stop sound fadeout (1.5)
        "El primero del trío para ti. No puedes saber cuántos lleva cada una de ellas."
    scene c29s005_460d with fade
    "Las dos mujeres se apoyan una en los brazos de la otra, buscando el apoyo que sus piernas, débiles después de los orgasmos, ya no pueden proporcionarles."
    eri "*GEMIDO* Ha sido alucinante... *JADEO*"
    "Su respiración entrecortada hace complicado entenderla por un momento, hasta que tu cerebro enlaza las sílabas que ha escuchado."
    nor "*JADEO* De los mejores sexos que he tenido nunca... *GEMIDO*"
    stop music fadeout (1.5)
    "Y la noche todavía es joven. Es posible que cambie de opinión antes de que os echéis a dormir."
    play music ("music/You-Know-Instrumental.ogg")
    mc "La próxima vez, me gustaría poder ver algo."
    call BlinkXS4("c29s005_460") from _call_BlinkXS4_729
    eri "*Risa* ¿El culo de mi madre no te dejaba ver nada?"
    eri "¡Pobrecito! Tener uno de los mejores culos del mundo sobre la cara le tapaba la visión."
    nor "*Risa* ¡Es que se queja por todo!"
    nor "Pero deberíamos cenar antes de que las hamburguesas se enfríen más aún."
    mc "*Risa* Me parece que eso significa que quieres descansar."
    scene c29s005_465a with fade
    call BlinkXS4("c29s005_465") from _call_BlinkXS4_730
    nor "Otra cadena de orgasmos como esta y me tendrías que llevar al hospital con deshidratación."
    nor "*Risa* Y a ver cómo le explico a [sam.nick] la razón de mi falta de líquidos."
    mc "*Risa* Entonces será mejor que cenemos."
    call BlinkXS4("c29s005_470") from _call_BlinkXS4_731
    eri "*Risa* Mi madre se hace mayor. Tú y yo hemos empezado hace mucho y es ella la que necesita descanso."
    mc "*Risa* La edad no perdona."
    scene c29s005_470d with dissolve
    nor "*Risa* Ensalada de berros con brócoli para mañana."
    if persistent.lesbian:
        scene c29s005_475An1 with fade
    else:
        scene c29s005_475An2 with fade
    "La cena transcurre entre risas y besos. Los tres sabéis que la noche no ha hecho más que empezar y coméis rápidamente."
    "Los lazos que os unen no tienen nada que ver con el sexo que vais a tener, pero las ganas de continuar hacen que la conversación tenga muchas bromas sexuales."
    "Y muchas amenazas risueñas que incluyen berros y brócoli."
    "Ninguno podríais decir cuánto tiempo habéis pasado comiendo, riendo, besándoos."
    scene c29s005_480a with fade
    "La espera para continuar se os ha hecho larga, pero las hamburguesas todavía están tibias y el vino aún está frío cuando los dejáis en la bandeja para volver a la cama."
    scene c29s005_480b with fade
    eri "Creo que es el momento de que le des a mi madre lo que se merece."
    mc "No podría estar más de acuerdo."
    nor "¿Y tú? ¿Qué vas a hacer mientras tanto?"
    scene c29s005_480c with dissolve
    eri "Depende de cómo os pongáis. Ya se me ocurrirá algo."
    mc "¿Dejamos a [nor] elección sobre qué posición quiere? *Risa* Ya sabes, tener una deferencia hacia nuestros mayores."
    nor "*Risa* Vas a comer brócoli durante meses."
    mc "*Risa* Lo dudo. Mi primera decisión como CEO en cuanto llegue a Aruba será prohibir el brócoli en el menú de la base."
    scene c29s005_480d with fade
    nor "*Gruñido risueño* Mis amenazas se han quedado vacías. ¿Te parece bien esta posición?"
    eri "*Risa* Creo que [mc] se acaba de cortocircuitar otra vez al ver ese culo."
    mc "*Beep* *Beep* Error de sistema... *Beeeeeep*"
    stop music fadeout (1.5)
    nor "*Risa* Sabéis que me siento muy expuesta ahora mismo, ¿verdad?"
    play music ("music/SexyLoungeMusic.ogg")
    scene c29s005_480An with dissolve
    "No contestas. Tan solo te sitúas detrás de ella y la penetras sin aviso."
    $renpy.sound.play ("music/MoanNorah.ogg", loop=True)
    nor "*GEMIDO* ¡Ooof! *JADEO* ¡Podrías haberme avisado! *GEMIDO*"
    "Su coño abraza tu polla con una fuerza húmeda. Estaba más que preparada para lo que iba a pasar."
    eri "Dadme un momento para que busque una posición cómoda."
    scene c29s005_880pv with fade
    "[eri] se coloca entre tus piernas, en una posición en la que puede lamerte los huevos y el astil de tu polla."
    eri "Ahora sí. Puedes empezar a moverte, [mc]."
    nor "*Risa* Eso debería decirlo yo, ¿no? *Jadeo* Soy la que tiene a Mjolnir dentro."
    show c29s005_880v
    "Sabes que no hace falta continuar la discusión fingida y empiezas a embestir a [nor], con tu pelvis impactando en su culo mientras perforas su coño."
    nor "*Gemido* Por bueno que seas con la lengua, Mjolnir es insuperable. *Jadeo*"
    "Bombeas alternando cambios de ritmo y pausas para darle a [eri] la oportunidad de recorrer cada pliegue de tu escroto con su lengua."
    "Dar placer a la madre mientras la hija te lo da a ti es una sensación increíble."
    eri "*Slurp*"
    scene c29s005_885pv with fade
    show c29s005_885v
    hide c29s005_880v
    "[eri] levanta sus caderas, cambiando de posición perceptiblemente. Buscando con su pelvis algo que estimule su coño."
    eri "*Slurp interrogativo*"
    "Llevas tu mano hacia atrás, buscando a ciegas su clítoris mientras sólo puedes imaginar cómo las tetas de [nor] se mueven con cada embestida."
    "Definitivamente, tienes que pedirle a [eva] que vuelva a instalar las cámaras. Y que te envíe los videos a un servidor privado."
    nor "*Jadeo* ¡Me encanta! *Gemido* ¡Es increíble! *Jadeo*"
    stop sound fadeout (1.5)
    "Su culo reverbera con cada uno de los impactos de tu pelvis en él."
    scene c29s005_890pv with fade
    show c29s005_890v
    hide c29s005_885v
    $renpy.sound.play ("music/MoanErika.ogg", loop=True)
    "Tus dedos no permiten que te olvides de [eri]. Una vez has encontrado su coño, empiezas a masajearlo, metiendo un dedo en su agujero del amor."
    "Debe estar muy sensible después del rato que lleváis en la cama."
    eri "*Gemido* *Slurp* *Jadeo*"
    nor "*JADEO* ¿Qué le estás haciendo a [eri]? *GEMIDO*"
    "Sus gemidos, aumentando de volumen al descubrir que [eri] también está disfrutando, muestran su excitación creciente."
    mc "Incluyéndola en el juego."
    stop sound fadeout (1.5)
    "En esta postura, las tetas de [eri] golpean tu culo en cada una de tus embestidas."
    scene c29s005_895pv with fade
    show c29s005_895v
    hide c29s005_890v
    $renpy.sound.play ("music/MoanNorah.ogg", loop=True)
    "Las dos mujeres se están acercando al orgasmo aún más rápido de lo que lo haces tú."
    nor "*GEMIDO* Voy a correrme de un momento a otro. *JADEO* ¡NO PARES! *GEMIDO*"
    "La tensión que tan bien conoces empieza a hacer su aparición en [nor]. La percibes claramente con tu mano apoyada en su culo."
    "Notas que [eri] también se acerca. Su lengua empieza a fallar su objetivo en alguna de tus embestidas."
    eri "*JADEO* *SLURP AFIRMATIVO* *GEMIDO*"
    "Parece que las dos van a volverse a correr a la vez, o con pocos segundos de diferencia. Tú no estás lejos."
    call OrgasmXS4("c29s005_485") from _call_OrgasmXS4_32
    nor "*GEMIDO* ¡SÍ! *JADEO* ¡SIGUE! *GEMIDO*"
    "Esta vez, [nor] es la primera en llegar a su destino. Su coño se cierra con fuerza sobre tu polla. Con más fuerza aún que hace unos segundos."
    stop sound fadeout (1.5)
    "Un temblor enorme la recorre de arriba a abajo, como un terremoto que sacude tu polla en su interior."
    $renpy.sound.play ("music/MoanErika.ogg", loop=True)
    call OrgasmXS4("c29s005_490") from _call_OrgasmXS4_33
    eri "*JADEO* ¡OH, SÍ! *GEMIDO* *SLURP* *JADEO*"
    "[eri] tan solo deja de lamer tus pelotas durante medio segundo antes de continuar tras su explosión."
    "Con las dos mujeres habiendo alcanzado el orgasmo, continúas embistiendo el coño de [nor]."
    if not persistent.lesbian:
        "No estás lejos de tu destino."
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
                "Correrte dentro." (wt = wt2):
                    pass
            $ resetWalkthrough ()
        call OrgasmXS4("c29s005_495") from _call_OrgasmXS4_34
        hide c29s005_895v
        mc "¡Mpfft!"
        "El coño de [nor] abrazando tu polla con fuerza hace que superes tu límite unos segundos después."
        if persistent.family:
            "Tu corrida es ingente. El descanso para cenar ha permitido que tus pelotas acumulen suficiente semen como para llenar a tu tía."
        else:
            "Tu corrida es ingente. El descanso para cenar ha permitido que tus pelotas acumulen suficiente semen como para llenar a la preciosa mujer."
        nor "*GEMIDO* ¡LLÉNAME HASTA EL BORDE! *JADEO*"
        stop sound fadeout (1.5)
        eri "*JADEO* *SLURP* *GEMIDO*"
    else:
        call BlinkXS4("c29s005_500") from _call_BlinkXS4_732
        nor "*GEMIDO* Necesito un cambio de postura... *JADEO* No veo nada desde aquí. *GEMIDO*"
        "Entiendes a lo que se refiere. Hace un rato estabas en la misma situación."
        eri "*JADEO* *SLURP AFIRMATIVO* *GEMIDO*"
        "Es difícil mostrar tu acuerdo con algo mientras tienes la lengua fuera lamiendo un escroto sin parecer idiota."
        stop sound fadeout (1.5)
        "[eri] lo consigue."
        scene c29s005_880pv with dissolve
        eri "*Jadeo* Ponte en el borde de la cama, Mamá. *Gemido*"
        "Reconoces el tono de voz. A la preciosidad que hay debajo de tus pelotas se le ha ocurrido una idea traviesa."
        scene c29s005_505d with fade
        "[nor] sigue las instrucciones de su hija, y cambia de postura tras unos segundos de pausa que permiten que tu orgasmo se aleje."
        nor "Así tampoco voy a ver nada..."
        eri "No te preocupes por eso."
        mc "Tú quizás no veas nada, pero nosotros tenemos unas vistas increíbles..."
        call BlinkXS4("c29s005_505") from _call_BlinkXS4_733
        eri "Ponte justo detrás de ella. Tengo una idea."
        mc "Sorpréndeme."
        scene c29s005_510a with fade
        call BlinkXS4("c29s005_510") from _call_BlinkXS4_734
        eri "Justo aquí. Así puedo colaborar mientras te la follas."
        scene c29s005_510d with dissolve
        eri "Sería como si te follaras mi mano y su coño  la vez."
        mc "*Risa* Estás traviesa..."
        nor "Chicos... Estoy notando la punta de Mjolnir rozando mi coño. ¿Vais a hablar de la postura mucho más rato?"
        call BlinkXS4("c29s005_515") from _call_BlinkXS4_735
        eri "*Risa* ¡No seas impaciente, Mamá!"
        scene c29s005_515d with hpunch
        $renpy.sound.play ("music/MoanErika.ogg", loop=True)
        eri "*Gemido* ¡Mamá!"
        nor "*Slurp*"
        mc "No sé quién de las dos está más traviesa. Pero creo que eso ha sido el pistoletazo de salida."
        scene c29s005_860pv with fade
        show c29s005_860v
        hide c29s005_895v
        "Empiezas a bombear con tus caderas en el coño de [nor] mientras observas cómo ella se come el coño de su hija."
        eri "*Gemido* Creo que no es la primera vez que mi madre hace eso... *Jadeo*"
        "De la forma decidida que [nor] ha atacado el coño de [eri], tú también lo crees."
        nor "*Gemido* *Slurp afirmativo* *Gemido*"
        stop sound fadeout (1.5)
        "Será una conversación para otro momento. No crees que [nor] pueda, o quiera, explicar sus anteriores experiencias con la lengua fuera de su boca."
        scene c29s005_875pv with fade
        show c29s005_875v
        hide c29s005_860v
        $renpy.sound.play ("music/MoanNorah.ogg", loop=True)
        "Es una lengua que tiene otras cosas que hacer en este momento."
        nor "*Jadeo* *Slurp* *Gemido*"
        "Aunque no tienes una visión directa de la acción, el lenguaje corporal de las dos mujeres te dice todo lo que necesitas saber."
        eri "*Gemido* ¡Así, Mamá! *Jadeo*"
        "Es extraño lo incestuoso que suena esa frase en los labios de [eri]. Incestuoso de una forma tierna, nada que ver con cómo demoniza la sociedad el incesto."
        stop sound fadeout (1.5)
        if not persistent.family:
            "Aunque no compartan ADN, son tan madre e hija como cualquier madre e hija biológicas. No es incesto legalmente, pero lo es a un nivel más profundo."
        scene c29s005_865pv with fade
        show c29s005_865v
        hide c29s005_875v
        $renpy.sound.play ("music/MoanErika.ogg", loop=True)
        "La mano de [eri] se mueve indecisa entre estrujar tu polla y acariciar el clítoris de [nor]."
        eri "*JADEO* ¡Así, [mc]! *GEMIDO* ¡Dale duro! *JADEO*"
        "Te resulta difícil contenerte mientras embistes la mano de la hija y el coño de la madre al mismo tiempo que se dan placer mutuamente."
        nor "*GEMIDO* *SLURP* *JADEO*"
        stop sound fadeout (1.5)
        "La situación es igual de excitante para las dos mujeres. Puedes notar cómo el cuerpo de [nor] se empieza a tensar."
        scene c29s005_870pv with fade
        show c29s005_870v
        hide c29s005_865v
        $renpy.sound.play ("music/MoanNorah.ogg", loop=True)
        "No podías imaginar que la sesión para estrechar lazos acabaría así."
        "Creías que eso sólo pasaba en los juegos y las películas porno."
        nor "*JADEO* *SLURP* *GEMIDO* *SLURP* *JADEO*"
        "Los sonidos de los lametones aceleran tal como [nor] se va acercando a su orgasmo."
        eri "*GEMIDO* ¡SÍ, [mc!u], HAZ QUE SE CORRA! *JADEO* ¡SÍ, MAMÁ, HAZ QUE ME CORRA! *GEMIDO*"
        "A [eri] no le queda mucho para correrse. Su lenguaje corporal, que tan bien conoces, te hace dudar de quién llegará antes al orgasmo."
        "Tan solo tienes que esperar unos segundos más para descubrirlo."
        call OrgasmXS4("c29s005_520") from _call_OrgasmXS4_35
        nor "*JADEO* ¡JODER! *GEMIDO* ¡SÍ! *JADEO*"
        "El coño de [nor] se hace más estrecho todavía sobre Mjolnir en el momento en que llega su clímax."
        eri "*GEMIDO* ¡BIEN HECHO, MAMÁ! *JADEO* ¡BIEN HECHO, [mc!u]! *GEMIDO*"
        stop sound fadeout (1.5)
        "Tu orgasmo también está llegando, alimentado por las oleadas que recorren el coño de [nor]."
        call OrgasmXS4("c29s005_525") from _call_OrgasmXS4_36
        $renpy.sound.play ("music/MoanErika.ogg", loop=True)
        eri "*JADEO* ¡JODER! *GEMIDO* ¡SÍ! *JADEO*"
        "[eri] se corre en el momento en que [nor] reanuda los lametones."
        nor "*GEMIDO* *SLURP* *JADEO*"
        "Las pareces vaginales de [nor] se cierran con fuerza sobre tu polla en el momento en que consigue su objetivo."
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
                "Correrte dentro." (wt = wt2):
                    pass
            $ resetWalkthrough ()
        call OrgasmXS4("c29s005_530") from _call_OrgasmXS4_37
        hide c29s005_870v
        mc "¡Mpfft!"
        "El coño de [nor] abrazando tu polla con fuerza hace que superes tu límite unos segundos después."
        if persistent.family:
            "Tu corrida es ingente. El descanso para cenar ha permitido que tus pelotas acumulen suficiente semen como para llenar a tu tía."
        else:
            "Tu corrida es ingente. El descanso para cenar ha permitido que tus pelotas acumulen suficiente semen como para llenar a la preciosa mujer."
        eri "*GEMIDO* ¡LLÉNALA HASTA EL BORDE! *JADEO*"
        nor "*JADEO* *SLURP* *GEMIDO*"
        stop sound fadeout (1.5)
    "La noche no podría acabar mejor."
    stop music fadeout (1.5)
    scene c29s005_535a with fade
    "Después de limpiaros, las dos mujeres se tumban encima tuyo para iniciar la sesión de abrazos."
    play music ("music/You-Know-Instrumental.ogg")
    eri "Eso ha sido increíble."
    if dap._var("route") and emm._var("route"):
        eri "Me ha gustado aún más que cuando lo hicimos con [emm] y [dap]."
        nor "Supongo que la complicidad entre nosotras es diferente..."
    nor "[mc] puede con dos mujeres o tres, o creo que incluso si fuéramos cuatro."
    mc "Es muy fácil con vosotras. Sois dos mujeres alucinantes."
    if mc._var("relationships")>2:
        scene c29s005_535b with dissolve
        nor "Creo que sería muy fácil con cualquiera a quien quieras y te quiera."
        nor "El sexo contigo es genial y todo el mundo en el harén está dispuesto a compartir."
        eri "Eso es cierto. Ha sido justo como esperaba que fuera."
        if dap._var("route"):
            scene c29s005_535c with dissolve
            eri "Para la próxima vez podríamos invitar a [dap]."
            nor "Sería increíble repetir esto con mis dos niñas..."
            mc "*Risa* Tendríamos que movernos a mi habitación. La cama es más grande."
            if persistent.lesbian:
                mc "Pero con [dap] no podríamos repetir la última parte. Sabéis que no quiere acercarse a otra chica a nivel sexual ni con un palo de diez metros."
                scene c29s005_535d with dissolve
                nor "*Risa* Pues puede mirar cuando lleguemos a esa parte. O mantenerte ocupado a ti."
                nor "Creo que cada vez que repitamos esto voy a querer probar los jugos de [eri]."
                eri "No sé qué pensaría [dap] de lo que ha pasado aquí. Por raro que parezca, no he sentido nada... lésbico... en lo que hemos hecho."
                eri "No me importaba que fuera una mujer quien me estuviera comiendo el coño. Era una persona a quien quiero y que me quiere."
                eri "No estoy... enamorada... de mi madre, pero no por ello hay menos amor entre nosotras. Es solo un tipo diferente de amor."
                mc "Entiendo lo que quieres decir. A veces se le da demasiada importancia a la manía que todo el mundo tiene por etiquetar las cosas."
        else:
            scene c29s005_535c with dissolve
            if mc._var("relationships")>3:
                eri "Para la próxima vez podríamos invitar a alguien más. Nosotras ya hemos estrechado lazos, y me gustaría que otras chicas lo experimentaran."
            else:
                eri "Para la próxima vez podríamos invitar a alguien más. Nosotras ya hemos estrechado lazos, y me gustaría que todo el harén lo hiciera."
            nor "Sería increíble repetir esto con todo el harén..."
            mc "*Risa* Tendríamos que movernos a mi habitación. La cama es más grande."
            if persistent.lesbian:
                mc "Aunque no sé qué pensaría ella de la última parte. Posiblemente alguien se podría escandalizar."
                call c29s005_tasteEri from _call_c29s005_tasteEri
    else:
        scene c29s005_535c with dissolve
        eri "Si decides incluir a alguna de las chicas nuevas en nuestra relación, podríamos invitarla."
        eri "Nosotras ya hemos estrechado lazos, y me gustaría que otras chicas lo experimentaran."
        nor "Sería increíble repetir esto con todo el harén... Si acabas teniendo uno."
        mc "*Risa* Tendríamos que movernos a mi habitación. La cama es más grande."
        if persistent.lesbian:
            mc "Aunque no sé qué pensaría ella de la última parte. Posiblemente alguien se podría escandalizar."
            call c29s005_tasteEri from _call_c29s005_tasteEri_1
    mc "Y, hablando de movernos, necesito levantarme un momento. Quiero un poco de vino."
    scene c29s005_535e with dissolve
    nor "*Risa* Ve a beber. Necesitas hidratarte para el siguiente asalto."
    eri "*Risa* ¿Quieres un tercer asalto?"
    scene c29s005_535f with fade
    nor "¡Por supuesto! Con lo difícil que es pillar a [mc] disponible, no le vamos a dejar acabar la noche después de sólo dos corridas, ¿no?"
    eri "Bueno, son tres. Nosotros hemos empezado antes. *Risa* Pero no sabía si, a tu edad, aún podrías aguantar más."
    scene c29s005_535g with fade
    nor "*Risa* Vas a comer berros durante MUCHO tiempo si sigues llamándome vieja. Un par de meses de comer berros te enseñarán a tener respeto por mis canas."
    eri "*Risa* Siempre puedes teñirte, pero las pocas canas que tienes te hacen una mujer muy interesante."
    scene c29s005_535h with fade
    eri "*Risa* Pero, si te sirve de consuelo, has envejecido mejor que el vino que se estaba bebiendo [mc]."
    nor "Bueno, entonces podemos dejarlo en un mes de comer berros. *Risa* A veces dices cosas bonitas."
    scene c29s005_535i with fade
    mc "No has envejecido. Has madurado como la buena fruta. Todos los melocotones del mundo envidiarían esa forma."
    eri "*Risa* Y el tamaño."
    nor "*Risa* ¡Melocotones de 20 libras!"
    scene c29s005_535j with fade
    "Es imposible resistirse a tan delicioso melocotón."
    mc "*Ñam*"
    nor "*Risa* ¡[mc]! ¡No me muerdas el culo!"
    eri "*Risa* Ya sabes que a [mc] siempre le gustaron los melocotones. ¿Cómo no iba a querer uno de 10 kilos?"
    scene c29s005_535k with fade
    mc "*Risa* Es que tu madre tiene un 'melocotón' delicioso. La última vez que estuvimos juntos ya lo mordisqueé."
    nor "*Risa* Parece que [mc] tiene una obsesión con mi culo."
    eri "¿Vosotros...?"
    mc "¿Nosotros qué, [eri]?"
    scene c29s005_535l with dissolve
    nor "*Risa* Creo que sé lo que vas a preguntar, pero quiero ver cómo lo preguntas."
    eri "*Risa* Eres malvada, Mamá. ¿Me quieres oír preguntarle a [mc] si ya te ha dado por culo? Es embarazoso."
    mc "*Risa* Yo también querría oírte preguntármelo, pero te voy a ahorrar el bochorno."
    scene c29s005_535m with dissolve
    if persistent.walkthrough:
        $ wt1 = _("Anal activado con [nor].")
        $ wt2 = _("Anal desactivado para [nor].")
    else:
        $ wt1 = ""
        $ wt2 = ""
    menu:
        "Aún no lo he hecho." (wt = wt1):
            $ nor._var("anal", True)
            call c29s005_norAnal from _call_c29s005_norAnal
        "No lo voy a hacer." (wt = wt2):
            $ nor._var("anal", False)
            mc "No lo voy a hacer. *Risa* Tengo miedo de que Mjolnir quede aplastado entre tanta carne. Prefiero mordisquearlo de vez en cuando."
            nor "*Risa* ¡Capullo!"
            eri "*Risa* Me parece una buena idea. Me gusta Mjolnir tal y como es. No quiero verlo convertido en una compresa."
            scene c29s005_535l with dissolve
            nor "*Risa* Voy a añadir col hervida a tu dieta de berros. Sé lo mucho que odias el olor."
            nor "*Risa* Te van a llamar Lady Col cuando acabes la dieta. Te vas a alimentar sólo de eso por meses."
            eri "*Risa* Si solo me alimento de eso, no voy a tener energía para otro trío como el de hoy."
            mc "Por cierto, yo ya estoy hidratado."
            scene c29s005_535n with dissolve
            nor "¿Ya?"
            mc "*Risa* Hace rato, pero me encanta veros fingir discutir."
            eri "*Risa* Fingir discutir es divertido."
            nor "¿Quién estaba fingiendo? ¿Tengo que añadir col y berros a la lista de la compra?"
            scene c29s005_570e with dissolve
            eri "Si queréis seguir vosotros. Yo estoy agotada."
            nor "Yo también. Ha sido todo muy intenso."
    $ resetWalkthrough ()
    mc "*Risa* Tenéis poca resistencia. Voy a decirle a [eva] que os ponga a correr mientras estoy fuera"
    mc "¿Queréis dormir ya?"
    scene c29s005_570f with dissolve
    eri "Yo estoy temiendo quedarme dormida a media frase."
    mc "*Risa* No sería la primera vez que lo haces. Podemos dar la noche por terminada y dormir."
    nor "¿Me puedo quedar a dormir con vosotros o preferís dormir solos?"
    scene c29s005_570g with dissolve
    eri "Como se te ocurra acercarte a esa puerta, no te mandaré mensajes para el próximo trío."
    mc "*Risa* Con esa amenaza, yo me quedaría. Yo también quiero que te quedes."
    nor "No quería irme, pero... Dado que es posible que sea la última noche que podáis pasar juntos antes del viaje a Aruba..."
    mc "También es posible que sea la última noche que pueda pasar contigo. Quédate."
    call KissXS4("c29s005_575") from _call_KissXS4_15
    nor "Eres un amor. No esperaba otra respuesta de ninguno de los dos, pero tenía que preguntar."
    if persistent.lesbian:
        call KissXS4("c29s005_580") from _call_KissXS4_16
    else:
        scene c29s005_580a
    nor "Gracias por dejarme quedarme, cielo."
    eri "No puedo permitir que te vayas, Mamá. Llevaba tiempo queriendo hacer esto."
    mc "¿Un trío con [nor]?"
    scene c29s005_580b with dissolve
    eri "*Risa* Eso también. Pero me refería a dormir los tres juntos."
    nor "Y creo que ha llegado el momento antes de que mi niña se quede dormida."
    mc "Estoy totalmente de acuerdo."
    call KissXS4("c29s005_585") from _call_KissXS4_17
    eri "Buenas noches, mi amor."
    mc "Buenas noches, mi vida."
    call KissXS4("c29s005_575") from _call_KissXS4_18
    nor "Buenas noches, [mc]."
    mc "Buenas noches, [nor]."
    if persistent.lesbian:
        call KissXS4("c29s005_580") from _call_KissXS4_19
    else:
        scene c29s005_580a with dissolve
    nor "Buenas noches, cielo."
    eri "Buenas noches, Mamá."
    scene c29s005_590a with fade
    "Apagáis las luces y os acomodáis para pasar la noche."
    "La conversación va decayendo hasta que [eri] se queda dormida a media frase."
    "[nor] y tú contenéis la risa a duras penas, pero no queréis despertar a la bella durmiente gótica."
    stop music fadeout (1.5)
    "Os quedáis dormidos poco después."
    scene black with dissolve
    return
label c29s005_noEriHelp1:
    scene c29s005_400a with fade
    mc "Voy a empezar por los zapatos y las medias. Al menos estas son normales."
    nor "¿Qué quieres decir con 'normales'?"
    scene c29s005_400b with fade
    mc "Nada que tenga que preocuparte. [eri] ha venido con unas medias que parecían una broma."
    scene c29s005_400c with dissolve #las dos medias quitadas. Plano general pillando a las dos
    nor "*Risa* ¿DAZ?"
    eri "*Risa* DAZ. El regalo de [emm]."
    scene c29s005_395i with dissolve
    mc "Creo que es el momento de revelar qué oculta este diminuto body."
    scene c29s005_395j with dissolve
    mc "Parece que alguien está excitado por la situación."
    call BlinkXS4("c29s005_405") from _call_BlinkXS4_736
    nor "¿Que mi hombre me desnude mientras mi hija nos mira no te parece una buena razón para estarlo?"
    mc "Me parece una de las mejores razones posibles."
    scene c29s005_400d with dissolve
    call c29s005_commonNoHelp from _call_c29s005_commonNoHelp
    return
label c29s005_commonNoHelp:
    mc "El otro está igual de duro."
    nor "*Risa* Estoy igual de excitada a izquierda y derecha."
    mc "Entonces habrá que dedicarles atención por igual."
    scene c29s005_410An with dissolve
    "Las enormes tetas de [nor] se sienten fantásticas en tus manos mientras sus erectos pezones son recorridos por tu lengua."
    "Casi se te escapa la risa al recordar el chiste sobre que las mujeres tienen dos tetas porque los hombres tienen dos manos."
    "Sería un buen momento para tener dos bocas y dos lenguas."
    "Tienes que dejar de pensar en cosas raras cuando tienes tan deliciosos pezones entre tus labios."
    call BlinkXS4("c29s005_415") from _call_BlinkXS4_737
    eri "Me estoy poniendo cachonda solo de veros."
    eri "Y no es por meteros prisa, pero estás tardando demasiado en desnudarla, y una cama vacía no es el mejor sitio donde estar, pese a lo tórrido que es veros."
    scene c29s005_400e with fade
    mc "Entonces habrá que continuar. No queremos que [eri] se quede dormida esperándonos, ¿verdad?"
    nor "Totalmente de acuerdo. Creía que habrías acabado a estas alturas. Nunca te has tomado tanto tiempo en desnudarme."
    scene c29s005_400An with fade
    mc "Siempre hay una primera vez para todo, y cuando el proceso es tan gratificante como el resultado..."
    nor "Las palabras adecuadas no van a hacer que tenga menos prisa por hacer esto."
    scene c29s005_400h with dissolve
    "Sabes perfectamente a lo que se refiere. Te levantas y la besas con pasión."
    "El proceso de desnudar a [nor] mientras [eri] os miraba te ha excitado más de lo que pensabas que lo haría."
    "Su húmedo aliento en tu boca mientras respira agitadamente es la única muestra que necesitas de que a ella la ha excitado tanto como a ti."
    scene c29s005_400i with fade
    "Interrumpes el beso y no tardas en comprobar que su boca no es el único lugar con labios húmedos."
    nor "*Gemido*"
    "Estás seguro de que, con [eri] esperándoos, [nor] no te va a dejar disfrutar más allá de unos pocos segundos, en cuanto se recupere de la sorpresa."
    "Sacas el máximo partido a esos segundos, memorizando cada aroma y cada sabor."
    scene c29s005_400j with fade #nor empuja a mc hacia la cama
    "Tal como pensabas, en cuanto la sorpresa desaparece, [nor] interrumpe tu visita a sus húmedos labios inferiores y te empuja hacia la cama."
    nor "No empieces por ahí. Alguien ha estado esperándonos durante demasiado tiempo."
    eri "A mí no me hubiera importado esperar más. Creo que puede ser muy caliente ver cómo [mc] te come."
    mc "Creo que entonces sabemos cómo podemos empezar..."
    return
label c29s005_EriHelp1:
    mc "¿Me ayudas a quitarle los zapatos y las medias mientras yo me ocupo de la parte de arriba?"
    scene c29s005_390a with fade
    call BlinkXS4("c29s005_390") from _call_BlinkXS4_738
    eri "Creía que no me lo ibas a pedir. Estás tardando demasiado en desnudarla, y una cama vacía no es el mejor sitio donde estar, pese a lo tórrido que es veros."
    mc "Pues puedes empezar con los zapatos. Por suerte sus medias son... normales."
    call BlinkXS4("c29s005_395") from _call_BlinkXS4_739
    nor "¿Qué quieres decir con 'normales'?"
    mc "Nada que tenga que preocuparte. [eri] ha venido con unas medias que parecían una broma."
    scene c29s005_395d with dissolve
    nor "*Risa* ¿DAZ?"
    eri "*Risa* DAZ. El regalo de [emm]."
    scene c29s005_395e with dissolve
    mc "Creo que es el momento de revelar qué oculta este diminuto body."
    scene c29s005_395f with dissolve
    mc "Parece que alguien está excitado por la situación."
    call BlinkXS4("c29s005_405") from _call_BlinkXS4_740
    nor "¿Que mi hombre y mi hija me estén desnudando no te parece una buena razón para estarlo?"
    mc "Me parece la mejor razón."
    scene c29s005_395g with dissolve
    mc "¿Cómo vas por ahí abajo?"
    eri "Más rápido que tú. *Risa* Ya casi he acabado. Sólo me queda esta media."
    scene c29s005_395h with fade #eri con una pierna sin zapato y sin media
    eri "Ya está hecho. Os espero en la cama. No os olvidéis de mí."
    if persistent.lesbian:
        if persistent.walkthrough:
            $ wt1 = _("Contenido lésbico.")
            $ wt2 = _("Sin consecuencias.")
        else:
            $ wt1 = ""
            $ wt2 = ""
        menu:
            "¿Quieres que [eri] te siga ayudando a desnudar a [nor] y participe en excitarla?"
            "Si" (wt=wt1):
                $ eri._var("helpedNorah2", True)
                call c29s005_EriHelp2 from _call_c29s005_EriHelp2
            "No" (wt=wt2):
                $ eri._var("helpedNorah2", False)
                call c29s005_noEriHelp2 from _call_c29s005_noEriHelp2
    return
label c29s005_noEriHelp2:
    "Mientras [eri] vuelve a la cama..."
    scene c29s005_400d with dissolve
    call c29s005_commonNoHelp from _call_c29s005_commonNoHelp_1
    return
label c29s005_EriHelp2:
    mc "No hace falta que te vayas. Tu madre tiene dos tetas y yo solo tengo una boca."
    scene c29s005_420aa with hpunch
    call BlinkXS4("c29s005_420a") from _call_BlinkXS4_741
    eri "¿Quieres decir que yo puedo...?"
    mc "Sólo si quieres y a [nor] le parece bien."
    call BlinkXS4("c29s005_420b") from _call_BlinkXS4_742
    nor "A mí me parece una idea increíble. Y sería una forma genial de estrechar lazos..."
    if persistent.family:
        nor "De bebé te encantaban mis tetas y nunca tenías suficiente. Veamos si te siguen gustando, aunque las circunstancias sean diferentes."
        call BlinkXS4("c29s005_425") from _call_BlinkXS4_743
        eri "No recuerdo aquella época, con lo que es el momento de crear recuerdos nuevos. En otras circunstancias."
    else:
        nor "Nunca pude amamantarte porque... ya sabes... no eres mi hija biológica... Pero podemos recuperar el tiempo perdido..."
        call BlinkXS4("c29s005_425") from _call_BlinkXS4_744
        eri "Que yo no sea tu hija biológica, no significa que seas menos mi madre. Es el momento de crear recuerdos nuevos."
    scene c29s005_430An with dissolve
    if persistent.family:
        "Tras mirarte por última vez, dándote la opción de echarte atrás, [eri] busca el pezón de [nor] de una forma que nunca hizo como bebé."
        "Acabas de descubrir que hay pocas cosas más sexis que una mujer adulta enganchada a las tetas de su madre."
    else:
        "Tras mirarte por última vez, dándote la opción de echarte atrás, [eri] busca el pezón de [nor] de una forma que nunca pudo hacer como bebé."
        "Acabas de descubrir que hay pocas cosas más sexis que una mujer adulta enganchada a las tetas de su madre."
        "Como [eri] ha dicho, no por ser ella un clon hace que [nor] sea menos su madre."
    if persistent.lactation and nor._var("pregnant"):
        "No puedes esperar a que llegue el momento en que esas tetas empiecen a producir leche para repetir esta escena."
    scene c29s005_435An with dissolve
    "Pero [nor] tiene una teta libre y no dejas que tu boca esté inactiva."
    "Casi se te escapa la risa al recordar el chiste sobre que las mujeres tienen dos tetas porque los hombres tienen dos manos."
    "Quien inventó el chiste no pensó en este escenario. Te faltan manos incluso teniendo en cuenta que sólo estás dedicando tu atención a una de las tetas de [nor]."
    "Tienes que dejar de pensar en cosas raras cuando tienes un pezón tan delicioso entre tus labios y un culo igual de alucinante en tu mano."
    scene c29s005_435e with dissolve
    nor "*Gemido* ¡Esto es alucinante! *Jadeo*"
    eri "*Slurp afirmativo*"
    mc "*Slurp*"
    scene c29s005_435f with dissolve
    "Quieres hacerlo aún más alucinante y bajas a la entrepierna de [nor], retirando el body en el proceso."
    "Descubres que sus labios están tan húmedos como sus tetas después de que dos bocas hayan dedicado su atención a sus pezones."
    nor "*GEMIDO*"
    scene c29s005_435g with dissolve
    eri "Parece que hay alguien ansioso por probar el plato principal."
    if persistent.family:
        "El comentario de tu preciosa prima no hace que dejes de lamer el coño de tu sexy tía."
    else:
        "El comentario de la preciosa chica no hace que dejes de lamer el coño de la sexy mujer."
    nor "Por mucho que me guste esto, creo que deberíamos seguir en la cama."
    "Sabías que este momento llegaría. No puedes estar más ansioso por llegar a la cama."
    return
label c29s005_tasteEri:
    scene c29s005_535d with dissolve
    nor "*Risa* Pues puede mirar cuando lleguemos a esa parte. O mantenerte ocupado a ti."
    nor "Creo que cada vez que repitamos esto voy a querer probar los jugos de [eri]."
    eri "No creo que haya nada raro en lo que ha pasado aquí. Por raro que parezca, no he sentido nada... lésbico... en lo que hemos hecho."
    eri "No me importaba que fuera una mujer quien me estuviera comiendo el coño. Era una persona a quien quiero y que me quiere."
    eri "No estoy... enamorada... de mi madre, pero no por ello hay menos amor entre nosotras. Es solo un tipo diferente de amor."
    mc "Entiendo lo que quieres decir. A veces se le da demasiada importancia a la manía que todo el mundo tiene por etiquetar las cosas."
    return
label c29s005_norAnal:
    mc "Aún no he tenido la oportunidad, pero es algo que me gustaría hacer algún día."
    eri "¿Por qué no hoy? Es un día para probar cosas nuevas y así yo puedo descansar un poco."
    if persistent.lesbian:
        eri "Llevo dos polvos, una paja, y una comida de coño. Así puedo miraros mientras lo hacéis."
    else:
        eri "Llevo dos polvos, y una paja. Así puedo miraros mientras lo hacéis."
    nor "Si estás interesado... pero no hay lubricante..."
    mc "Entonces tendré que ser ultra delicado."
    scene c29s005_535o with dissolve
    eri "Tengo aceite para bebés. Creo que puede servir."
    nor "Tráelo y probamos. Estoy segura de que algo ayudará."
    mc "Será mejor que hacerlo sin nada..."
    scene c29s005_540a with fade
    call BlinkXS4("c29s005_540") from _call_BlinkXS4_745
    nor "Ve con cuidado, por favor. Nunca ha entrado nada ahí."
    mc "Intentaré ser lo más cuidadoso posible, no te preocupes."
    scene c29s005_545An with dissolve
    "Cuando [eri] trae el aceite, embadurnas el ano de [nor] abundantemente. No queda mucho aceite y lo usas todo. Quieres lubricar bien a la expectante mujer."
    nor "*Jadeo* ¡Está frío!"
    mc "*Risa* Creo que eso es porque tú ya estás caliente."
    eri "Yo nunca he tenido interés en probarlo. Pero a lo mejor me hacéis cambiar de opinión."
    if persistent.family:
        nor "Hace tiempo que quería probarlo, pero tu padre no estaba interesado."
    else:
        nor "Hace tiempo que quería probarlo, pero Mike no estaba interesado."
        mcp "(Es curioso que, para [nor], ella sea la madre de [eri], pero sin embargo el Tío Mike solo sea 'Mike'.)"
        mcp "(Supongo que no pasó el tiempo suficiente con las gemelas para ganarse el título de 'Papá'.)"
    mc "Creo que esto ya está listo."
    scene c29s005_550a with fade
    "Te sitúas a la espalda de [nor], apoyando la punta de tu polla en su estrecho agujero."
    mc "¿Lista?"
    stop music fadeout (1.5)
    nor "Cuando quieras..."
    scene c29s005_550b with dissolve
    play music ("music/SexyLoungeMusic.ogg")
    "Introduces el glande dentro del precioso culo. El lubricante ha hecho su función y ha habido poca resistencia."
    "[nor] está relajada y eso ayuda. La experiencia, aunque sea su primera vez por la puerta trasera, ayuda mucho a que todo funcione sin problemas."
    mc "¿Estás bien?"
    nor "¿Ya está dentro?"
    eri "*Risa* Esa frase acabaría con la autoestima de muchos hombres."
    mc "*Risa* No con la mía. Pero solo está dentro la punta."
    nor "Todo va bien de momento. Puedes seguir."
    scene c29s005_550c with dissolve
    "Metes poco a poco la mitad de la polla dentro del melocotón más bonito del mundo. Sigue entrando sin problemas."
    nor "*Jadeo* Ahora sí que me empiezo a sentir llena. *Jadeo*"
    mc "¿Estás bien? Podemos parar si quieres."
    scene c29s005_550d with dissolve
    eri "¿Te duele? Si te duele mucho es mejor que lo dejes. Estoy segura de que a [mc] no le importará."
    nor "No, no duele. Es una sensación... extraña. Me recuerda a la primera vez que me acosté con [mc] después de casi dos décadas sin sexo."
    mc "[eri] tiene razón. Si en algún momento te duele, dímelo y paramos."
    nor "Creo que puedes seguir. Te lo diré si me duele. Te lo prometo. Pero de momento me gusta."
    scene c29s005_845pv with dissolve
    "Sigues metiendo a Mjolnir lentamente dentro de su estrecho agujero hasta que tu pelvis toca su culo. Sus cachetes se separan con el impacto."
    nor "*Jadeo* Ahora sí que está toda dentro, ¿no? *Gemido*"
    "El gemido al final de la pregunta te indica que le sigue gustando."
    mc "Bueno, queda un poco fuera, pero..."
    eri "*Risa* Creo que quiere decir que tu enorme culo le evita llegar hasta el final. ¿Cómo estás?"
    nor "*Risa* Teniendo en cuenta que mi hombre y mi hija me acaban de llamar culo gordo, estoy bien. No duele nada. Es una sensación extraña, pero agradable."
    nor "Creo que puedes empezar a moverte."
    scene c29s005_550An with dissolve
    $renpy.sound.play ("music/MoanNorah.ogg", loop=True)
    "Empiezas a bombear lentamente, haciendo una pequeña pausa cada pocos centímetros, esperando que [nor] se queje."
    mc "¿Qué tal estás? ¿Sigue sin doler?"
    nor "*Gemido* Calla y fóllame más rápido. *Gemido*"
    "Ya no hay jadeos. Solo gemidos. Es una buena señal."
    eri "Si le pudieras ver la cara... No es una cara de dolor, te lo aseguro."
    scene c29s005_845pv with dissolve
    show c29s005_845v
    "Si quiere que te folles su culo más rápido, no vas a ser tú quien le quite la idea de la cabeza."
    "Empiezas a bombear rápidamente, hipnotizado por el melocotón gigante. Atento a si aparecen las señales de dolor."
    nor "*GEMIDO* ¡Joder! *GEMIDO* ¡Mejor de lo que esperaba! *GEMIDO*"
    "La experiencia de la mujer se hace notar desde el primer momento. Relaja y tensa su esfínter al mismo ritmo que tú la embistes."
    eri "Me estoy poniendo cachonda sólo de veros. Mamá, te pones guapísima cuando te embiste..."
    stop sound fadeout (1.5)
    "El vínculo entre las dos mujeres está alcanzando niveles insospechados."
    scene c29s005_840pv with dissolve
    show c29s005_840v
    hide c29s005_845v
    $renpy.sound.play ("music/MoanErika.ogg", loop=True)
    "Para sorpresa de nadie, [eri] empieza a acariciar su coño mientras observa cómo golpeas contra el culo de [nor]."
    eri "*Gemido* No aguanto más... *Jadeo* Esto es demasiado tórrido... *Gemido*"
    "La visión de las dos mujeres en este momento es inmejorable. O casi."
    nor "*JADEO* ¡Sigue así, [mc]! *GEMIDO* ¡ME ESTÁ ENCANTANDO! *JADEO*"
    stop sound fadeout (1.5)
    "Nunca sospechaste que [nor], tan consciente de su cuerpo, pudiera disfrutar el sexo anal."
    scene c29s005_850pv with dissolve
    show c29s005_850v
    hide c29s005_840v
    $renpy.sound.play ("music/MoanNorah.ogg", loop=True)
    "Te alegra estar equivocado."
    if persistent.lesbian:
        nor "*GEMIDO* ¿Por qué no te acercas un poco? *JADEO*"
        eri "*JADEO* Porque he dicho que quería descansar. *GEMIDO* Quiero verte, no tener tu lengua en mi coño. *JADEO*"
        nor "*GEMIDO* Entonces sigue dándote placer, [eri]. *JADEO* [mc] me lo está dando a mí."
    else:
        nor "*GEMIDO* Sigue dándote placer, [eri]. *JADEO* [mc] me lo está dando a mí."
    eri "*JADEO* Es imposible no hacerlo. *GEMIDO* Estáis increíbles. *JADEO*"
    stop sound fadeout (1.5)
    "Sus voces dejan entrever lo excitadas que están por la escena. Tanto como lo estás tú."
    scene c29s005_855pv with dissolve
    show c29s005_855v
    hide c29s005_850v
    $renpy.sound.play ("music/MoanErika.ogg", loop=True)
    "Tu orgasmo se acerca y te inclinas sobre [nor] para embestirla con más fuerza."
    "Su estrecho esfínter está haciendo maravillas sobre tu astil, tensándose y relajándose al ritmo de tus embestidas."
    eri "*GEMIDO* NO VOY A PODER AGUANTAR MUCHO MÁS. *JADEO*"
    nor "*JADEO* YO TAMPOCO. *GEMIDO* CORRÁMONOS LOS TRES JUNTOS. *JADEO*"
    "[nor] puede leer las señales que tu polla lanza dentro de su culo y sabe que tú también estás a punto de correrte."
    "Se prepara un buen espectáculo de fuegos artificiales. El 4 de julio va a parecer silencioso en comparación."
    call OrgasmXS4("c29s005_555") from _call_OrgasmXS4_38
    eri "*JADEO* ¡POR DIOS! *GEMIDO* ¡ME CORRO! *JADEO*"
    "[eri] es la primera en llegar al clímax con una potente corrida."
    stop sound fadeout (1.5)
    "Si hubiera estado más cerca de la mujer del increíble melocotón, hubiera bañado su cara."
    call OrgasmXS4("c29s005_560") from _call_OrgasmXS4_39
    $renpy.sound.play ("music/MoanNorah.ogg", loop=True)
    nor "*GEMIDO* ¡YO TAMBIÉN! *JADEO* ¡NO ME LO PUEDO CREER! *GEMIDO*"
    "Ver la corrida de su hija en primer plano hace que [nor] no pueda retener más su clímax."
    "Su culo se cierra sobre tu polla con fuerza. Un caliente anillo que estruja tu astil con fuerza, llevándote más allá de tu límite."
    call OrgasmXS4("c29s005_565") from _call_OrgasmXS4_40
    mc "¡Mpfft!"
    "La presión en tu polla hace que sea imposible que retengas más tu propio orgasmo."
    if persistent.family:
        "Llenas los intestinos de tu tía con tu semilla, descargando tu caliente líquido en su interior."
    else:
        "Llenas los intestinos de [nor] con tu semilla, descargando tu caliente líquido en su interior."
    nor "*JADEO* ¡SÍ! *GEMIDO* ¡SE SIENTE TAN DIFERENTE! *JADEO*"
    scene c29s005_570a with fade
    "Cuando acaban las oleadas de orgasmos de las dos mujeres, sales del culo de [nor] y observas tu obra de arte."
    nor "*Respiración entrecortada* No voy a poder sentarme en un par de días... Necesito limpiarme."
    stop sound fadeout (1.5)
    scene c29s005_570b with fade
    "Os derrumbáis en la cama agotados después de la limpieza, con las dos mujeres de nuevo sobre tu pecho."
    stop music fadeout (1.5)
    eri "*Respiración pesada* Ha sido increíble veros... Casi me hace replantearme lo del sexo anal."
    play music ("music/You-Know-Instrumental.ogg")
    mc "Si alguna vez te apetece..."
    nor "Yo te lo recomendaría probar al menos una vez. Sigo prefiriendo el sexo vaginal, pero es muy bueno."
    scene c29s005_570c with dissolve
    eri "¿No te ha dolido nada?"
    nor "El lubricante ha ayudado. Y [mc] ha sido muy cuidadoso al principio."
    mc "*Risa* ¿Sólo al principio?"
    scene c29s005_570d with dissolve
    nor "*Risa* Sí, solo al principio. Después has sido un semental embistiéndome con fuerza, pero me ha encantado." id c29s005_norAnal_9350b423
    mc "*Risa* Si el resultado ha sido bueno, me parece que el modo semental ha sido el correcto."
    eri "Yo le estaba viendo la cara y te aseguro que el resultado ha sido buenísimo."
    eri "Quizás algún día me atreva."
    mc "¿Algún día? ¿Por qué no hoy? La noche es joven."
    scene c29s005_570e with dissolve
    eri "*Risa* Primero porque has agotado el aceite. Y después porque no podría ni siquiera ponerme en posición. Estoy agotada."
    nor "Yo también. Creo que todo ha sido muy intenso hoy."
    eri "*Risa* Además, no sé cómo estará Mjolnir después de la visita al culo de mi madre. Me da miedo mirarlo y descubrir que ha sido aplastado por una tonelada de melocotón."
    scene c29s005_535l with dissolve
    nor "*Risa* Voy a añadir col hervida a tu dieta de berros. Sé lo mucho que odias el olor."
    nor "*Risa* Te van a llamar Lady Col cuando acabes la dieta. Te vas a alimentar sólo de eso por meses."
    eri "*Risa* Si solo me alimento de eso, no voy a tener energía para otro trío como el de hoy."
    mc "¿Como el de hoy? ¿Ya hemos acabado?"
    return


label c29s006_AmaEmm:
    if _in_replay:
        call mrS3_eri_route from _call_mrS3_eri_route_13
        call mrS3_eva_route from _call_mrS3_eva_route_16
        call mrS3_ama_route from _call_mrS3_ama_route_14
        call mrS3_emm_route from _call_mrS3_emm_route_23
    scene black with dissolve
    centered "{size=+20}{b}DÍA 33 – SÁBADO{/b}{/size}"
    if eri._var("route"):
        scene c29s006_005a with dissolve
        "Te despiertas en una habitación vacía. La costumbre que tiene todo el mundo de dejarte dormir hasta tarde empieza a molestarte."
    else:
        scene c28s004_005a with dissolve
        "Te despiertas en tu habitación poco antes de que suene el despertador. Has descansado bien en una noche sin sueños."
    scene c29s006_005c with fade
    play music ("music/LifeOfAWanderingWizard.ogg")
    "Te das una ducha y bajas a la cocina a desayunar algo."
    "Al pasar por delante de la habitación de [emm] oyes voces en el interior."
    emm "*A través de la puerta* ¡Pero es injusto!"
    ama "*A través de la puerta* Lo sé, pero habrá tiempo para eso, [emm]."
    "La curiosidad sobre lo que [emm] considera injusto puede contigo."
    scene c29s006_010An with dissolve
    play sound ("music/knock.ogg")
    "*Knock-Knock*"
    mc "Chicas, ¿puedo pasar?"
    emm "*A través de la puerta* Sí, pasa."
    scene c29s006_010d with fade
    emm "¿Querías algo?"
    ama "Buenos días, [mc]."
    mc "Buenos días, [ama] y [emm]. Supongo que [emm] está enfadada por algo si ni siquiera me da los buenos días."
    call BlinkXS3("c29s006_015") from _call_BlinkXS3_798
    emm "Perdona. Buenos días."
    emm "Es que [ama] está siendo injusta conmigo."
    mc "¿Qué ha pasado?"
    emm "Que te lo explique ella... A ver si así se da cuenta..."
    call BlinkXS3("c29s006_020") from _call_BlinkXS3_799
    mc "Vale, [emm] está MUY enfadada por algo."
    ama "La entiendo. Quiere que hagamos entrenamientos intensivos de tiro, ella y yo, antes de que tú y yo nos vayamos a Aruba."
    mc "Pero tú no tienes tiempo para eso. Suficiente tienes con preparar toda la logística, aparte de estar vigilando la casa."
    ama "Es lo que le he dicho, le estoy diciendo que, cuando [eva] me releve tendremos tiempo de hacerlo."
    call BlinkXS3("c29s006_025") from _call_BlinkXS3_800
    mc "Y a ti, ¿por qué no te parece bien esa idea?"
    emm "Por muchas razones. Acabo de encontrar a mi hermana perdida y ahora os vais a ir un mes entero. Yo quería pasar tiempo con ella..."
    mc "Creo que tiene más que ver con pasar tiempo con [ama] que con ayudar a la vigilancia."
    mc "Pero parece que habéis pasado tiempo juntas. Si las dos aún estáis en pijama, supongo que [ama] ha dormido aquí."
    emm "Sí, pero no es suficiente... Tú te vas a pasar cinco o seis meses fuera, y ella se va a pasar uno allí y uno aquí, y después se volverá a ir."
    mc "¿No crees que estás siendo un poco egoísta? [ama] tiene muchísimas cosas que hacer antes de irnos..."
    call BlinkXS3("c29s006_030") from _call_BlinkXS3_801
    emm "No es sólo por egoísmo. Si soy buena disparando, puedo ayudar a [eva] a hacer guardias mientras [ama] está fuera..."
    mc "Puedes ayudar a [eva] vigilando las cámaras en la base. No hace falta que dispares a nadie."
    mc "Además, ¿renunciarías a lo que te queda de verano por ayudar a [eva]?"
    call BlinkXS3("c29s006_035") from _call_BlinkXS3_802
    emm "¡Por supuesto! ¡Ya no soy una niña pequeña! Una vez os vayáis, no va a haber mucho que hacer por aquí..."
    mc "Es muy loable por tu parte, pero creo que te equivocas. Van a llegar las chicas nuevas, y tendrás que ayudar a Mamá y a Tía [nor] a prepararlo todo."
    mc "Además, ¿quién mejor que mi hermanita para tener a todo el mundo vigilado dentro de la casa mientras [eva] vigila el perímetro?"
    call BlinkXS3("c29s006_040") from _call_BlinkXS3_803
    ama "No lo había pensado, pero creo que [mc] tiene razón. Si ayudas a [mar] y a [nor] y ayudas a que las chicas nuevas se integren en casa..."
    call BlinkXS3("c29s006_045") from _call_BlinkXS3_804
    emm "Querrás decir que se integren en la familia."
    mc "Creo que es pronto para eso. Aún no sabemos nada de ellas y no sabemos si serán buenas para la familia o si la familia será buena para ellas."
    call BlinkXS3("c29s006_050") from _call_BlinkXS3_805
    ama "[mc] tiene razón. Por mucho que nos guste cómo está funcionando la familia, no quiere decir que todo el mundo pueda o quiera encajar en ella."
    ama "[lis], [deb.nick], [kim], o [kat] han decidido que ésta es su segunda familia, pero porque llegaron cuando se estaba formando."
    ama "Quizás para las chicas nuevas sea un poco abrumador. O quizás seamos bichos raros para ellas."
    mc "Sólo hay que miraros a vosotras dos. Tendrán problemas para saber quién es el clon de quién."
    call BlinkXS3("c29s006_055") from _call_BlinkXS3_806
    emm "Lo estuve hablando ayer con [eva]. ¿Cómo se lo vamos a decir? Con las chicas de casa fue fácil, pero para las nuevas..."
    if persistent.family:
        emm "Lo de 'Hola, soy [emm], a mi clon la conoceréis de aquí a dos semanas cuando vuelva de Aruba' no me parece una buena idea."
    else:
        emm "Lo de 'Hola, soy [emm], a la chica de la que soy un clon la conoceréis de aquí a dos semanas cuando vuelva de Aruba' no me parece una buena idea."
    mc "*Risa* No, no parece una buena idea. Y no creo que esconder a [eva] hasta que sepamos más de ellas tampoco sea una buena idea. Ni que ella quisiera esconderse."
    call BlinkXS3("c29s006_060") from _call_BlinkXS3_807
    ama "*Risa* Por suerte, tú y yo estaremos en Aruba y no nos tendremos que comer ese problema. Se lo dejaremos a las que se queden aquí."
    ama "*Risa* Y que alguien intente esconder a [eva] si quiere morir."
    mc "*Risa* ¡No me puedo creer que vayamos a evitar comernos un problema!"
    call BlinkXS3("c29s006_065") from _call_BlinkXS3_808
    ama "Creo que es algo que no se puede planificar hasta que estén aquí y vean de qué pasta están hechas."
    ama "Yo aceptaré cualquier cosa que decidáis las que estáis aquí sobre cómo y cuándo contárselo."
    call BlinkXS3("c29s006_070") from _call_BlinkXS3_809
    emm "Yo he pensado que..."
    mc "*Risa* Esa frase me da miedo en tus labios."
    emm "Voy a ignorar lo que ha dicho [mc]. Yo he pensado que no es necesario decírselo a todas a la vez."
    emm "Quizás ir explicándoselo a las que veamos con más probabilidades de aceptarlo."
    mc "*Risa* Pues no daba tanto miedo..."
    call BlinkXS3("c29s006_075") from _call_BlinkXS3_810
    emm "*Risa* ¡Te estoy ignorando!"
    mc "Pero tienes razón. Creo que cuando conozcáis a cada una sabréis a quién se lo podéis decir en qué momento."
    mc "Es algo que iréis viendo vosotras en base a..."
    scene c29s006_080a with vpunch
    call BlinkXS3("c29s006_080") from _call_BlinkXS3_811
    emm "Voy a contarle mi idea a Mamá. Os veo luego."
    scene c29s006_080d with dissolve
    stop music fadeout (1.5)
    emm "¡Soy un genio! ¡Incluso [mc] ha reconocido que tengo razón!"
    scene c29s006_080e with dissolve
    play sound ("music/DoorSlam.ogg")
    "*Blam*"
    scene c29s006_085An with dissolve
    ama "..."
    play music ("music/From-Above.ogg")
    call BlinkXS3("c29s006_090") from _call_BlinkXS3_812
    ama "*Risa* ¡Me encanta esta chica!"
    mc "*Risa* No me extraña, dado que compartís material genético."
    mc "Siempre me he preguntado si entre clones sentís alguna afinidad o vínculo como los que se dice que tienen los gemelos."
    call BlinkXS3("c29s006_095") from _call_BlinkXS3_813
    ama "No. No hay nada de eso. O al menos que [emm] o yo hayamos experimentado. Ella también se lo preguntaba y hablamos de ello hace unos días."
    ama "Pero claro, el vínculo de los gemelos tampoco está demostrado. Los hay que dicen tenerlo y los hay que no sienten nada."
    if persistent.family:
        ama "[dap] y [eri] dicen que no tienen ningún vínculo sobrenatural, por ejemplo."
        mc "Lo sé. *Risa* [dap] pensaba que acabarían desarrollando telepatía o algo así cuando eran pequeñas."
    call BlinkXS3("c29s006_100") from _call_BlinkXS3_814
    ama "Hablando de clones..."
    mc "¿Gavin?"
    ama "Sí."
    mc "Supongo que [eva] te lo ha explicado. ¿Qué te parece?"
    call BlinkXS3("c29s006_105") from _call_BlinkXS3_815
    ama "Creo que es una buena idea. Si todo sale bien, puede ser un activo valioso."
    ama "Si no sale como esperamos, podrá ayudarnos con la vigilancia."
    mc "Y, sea como sea, [eva] se sentirá menos culpable y él se sentirá útil."
    call BlinkXS3("c29s006_110") from _call_BlinkXS3_816
    ama "Y nos relevará a nosotras de mucho trabajo. Hacer toda la vigilancia entre las dos mientras intentamos llevar una vida 'normal' está siendo un reto."
    mc "Le he estado dando vueltas a eso también. Creo que sería bueno que, cuando volvieras después de la primera rotación, trajeras más clones aparte de Gavin."
    mc "De series diferentes, para que no se vea que son clones entre ellos."
    call BlinkXS3("c29s006_115") from _call_BlinkXS3_817
    ama "¿No quieres que sigamos protegiendo a la familia nosotras?"
    mc "Claro que sí. Puedes dirigir el equipo, pero creo que eres demasiado valiosa como para que te pases horas mirando cámaras de seguridad."
    mc "Puedes hacer mucho más si delegas en Gavin y otros chicos el trabajo de nivel más bajo."
    mc "Después de la primera rotación estarás sola y tienes que dormir."
    call BlinkXS3("c29s006_120") from _call_BlinkXS3_818
    ama "Llevo tantos meses haciendo esto que ya lo encuentro normal, pero tienes razón. Aunque no sabría en quién puedo delegar..."
    mc "Bueno, vas a tener un mes en Aruba para poder descubrirlo y organizar un equipo. Incluso un par de equipos que puedan rotar entre aquí y allí."
    mc "Vosotras habéis sido prácticamente esclavas de la misión, y el tiempo de la esclavitud en NTR ha acabado."
    call BlinkXS3("c29s006_125") from _call_BlinkXS3_819
    ama "*Risa* ¿Quieres decir que los que vengan trabajarán ocho horas? Se van a reblandecer."
    mc "Estoy hablando en serio, [ama]. Quiero que los clones que decidan seguir trabajando para nosotros tengan una vida normal... o todo lo normal posible."
    mc "Quiero que tengan tiempo libre, que puedan ir al cine o a cenar. Que puedan formar sus propias familias si encuentran con quién hacerlo."
    call BlinkXS3("c29s006_130") from _call_BlinkXS3_820
    ama "Eso que dices es muy complicado. Sé que tu intención es buena, pero ¿quién va a querer formar una familia con un clon que envejece aceleradamente?"
    if ama._var("route"):
        mc "¿Crees que, si envejecieras aceleradamente, no estaría contigo?"
    elif eva._var("route"):
        mc "¿Crees que, si [eva] envejeciera aceleradamente, no estaría con ella?"
    else:
        mc "¿Crees que, si me enamorara de alguien que envejece aceleradamente, eso me detendría?"
    mc "Sería una buena razón para atesorar cada momento, porque serían aún más limitados."
    call BlinkXS3("c29s006_135") from _call_BlinkXS3_821
    ama "No, no lo creo. Pero no podría ser algo para toda la vida. Al menos no para toda tu vida..."
    mc "Eso nunca se puede saber. A mí estuvieron a punto de matarme. A muchos de nosotros. Nunca sabes cuánto va a durar una vida."
    mc "Pero no te centres sólo en lo de formar una familia. Quiero que puedan vivir su vida, y para eso necesitarán tiempo libre."
    mc "Tendrías que hacer cálculos para saber cuántos operativos necesitarías para cubrir todas las necesidades y, una vez estemos allí, elegir a los candidatos."
    call BlinkXS3("c29s006_140") from _call_BlinkXS3_822
    ama "Supongo que es el trabajo que me tocará hacer como jefa de seguridad, pero me cuesta mucho delegar en cosas que son importantes para mí."
    mc "¿Crees que no van a hacer un trabajo tan bueno como hacéis vosotras?"
    ama "No es eso. Sé que van a hacer un trabajo fantástico, incluso mejor que el nuestro porque van a poder cubrir más horas, pero..."
    mc "¿Pero...?"
    call BlinkXS3("c29s006_145") from _call_BlinkXS3_823
    ama "Me encanta ver a las chicas en la piscina cuando estoy vigilando en la base. O a [mar] cocinando. O a [nor] haciendo la colada."
    ama "Entregar esa parte de la vida familiar va a ser duro... No quiero perdérmelo..."
    mc "Si entregas esa parte de la vida familiar, podrás estar en la piscina, o ayudando a [mar] y a [nor], en vez de estar en la base."
    mc "No lo tendrás que ver a través de una pantalla, sino que podrás vivirlo. Ser parte de esa vida familiar más aún de lo que lo eres ahora mismo."
    call BlinkXS3("c29s006_150") from _call_BlinkXS3_824
    ama "¡Soy idiota! ¡Tienes razón!"
    mc "*Risa* Me voy a comprar una camiseta que ponga algo por el estilo. Nos ahorraríamos un montón de conversaciones."
    call BlinkXS3("c29s006_155") from _call_BlinkXS3_825
    ama "*Risa* Si llevaras una camiseta como esa, nadie de esta familia te daría nunca la razón. Ni siquiera cuando la tuvieras."
    mc "*Risa* Sólo por llevar la contraria, ¿no?"
    call BlinkXS3("c29s006_160") from _call_BlinkXS3_826
    ama "No voy a contestar a eso, porque sería como darte la razón."
    ama "Pero me voy a hacer unos cálculos para saber cuántos clones necesito para cubrir todos los turnos. Te veo luego."
    scene c29s006_160An with dissolve
    mc "Hasta luego..."
    if ama._var("route") and emm._var("route"):
        mcp "(Tengo que dejar de darles ideas que quieran explorar inmediatamente. Las dos se han ido sin darme un beso.)"
    elif ama._var("route"):
        mcp "(Tengo que dejar de darle ideas que quiera explorar inmediatamente. Se ha ido sin darme un beso.)"
    elif emm._var("route"):
        mcp "(Ha hecho lo mismo que [emm]. Tengo que dejar de darle ideas a [emm] que quiera explorar inmediatamente. Se ha ido sin darme un beso.)"
    else:
        mcp "(Tengo que dejar de darle ideas que quiera explorar inmediatamente. Me he acabado quedando solo.)"
    scene black with dissolve
    stop music fadeout (1.5)
    "Decides que es el momento de desayunar."
    return
label c29s006_DebEil:
    if _in_replay:
        call mrS3_eil_route from _call_mrS3_eil_route_10
        call mrS3_deb_route from _call_mrS3_deb_route_20
        call mrS3_mar_route from _call_mrS3_mar_route_23
    scene c29s006_400a with fade
    "Al entrar en la cocina..."
    play music ("music/RhythmPlay.ogg")
    deb "¿Ves? Este es el vestido que te decía. Creo que te quedaría genial."
    eil "Me gusta mucho, pero es carísimo. Creo que compraré algo más sencillo."
    deb "Por eso no te preocupes. Tómatelo como mi regalo de cumpleaños."
    scene c29s006_400b with dissolve
    eil "¡Pero mi cumpleaños fue en marzo!"
    deb "*Risa* Entonces tómatelo como mi regalo de cumpleaños con MUCHO retraso."
    mc "Hola, chicas. ¿Comprando ropa por internet?"
    call BlinkXS3("c29s006_405") from _call_BlinkXS3_827
    eil "Hola, [mc]. No estamos comprando por internet. [mad.nick] le envió a [lis] un email con las novedades que han llegado."
    mc "*Risa* A eso se le llama buen márquetin. Sabe que va a tener ventas aseguradas."
    call BlinkXS3("c29s006_410") from _call_BlinkXS3_828
    deb "*Risa* Creo que [lis] va a dejar de comprar ropa una temporada o tendrá que alquilar un trastero para tener dónde guardarla."
    deb "Ha comprado más ropa incluso de la que es normal en ella últimamente. Y yo también, con lo que no puede usar mi armario para guardar toda su ropa."
    mc "Me dijo que estaba usando el de [bet]..."
    call BlinkXS3("c29s006_415") from _call_BlinkXS3_829
    eil "Pero [bet] vuelve el martes y traerá ropa de Florida. Y en septiembre esos armarios serán para las chicas nuevas."
    eil "[lis] va a tener un problema para guardar toda la ropa."
    mc "De todas formas, se me hace extraño que tú compres vestidos caros. O que te los regale [deb.nick]."
    mc "Siempre has sido más de ir cómoda que con vestidos así."
    if eil._var("route"):
        mc "Además, tienes un novio que te puede comprar la ropa que necesites..."
    call BlinkXS3("c29s006_420") from _call_BlinkXS3_830
    eil "Bueno, una chica tiene que tener algo elegante, ¿no?"
    eil "Si surge la ocasión, no quiero tener que llevar el vestido con el que fui al baile de promoción."
    mc "Estabas monísima con aquel vestido."
    call BlinkXS3("c29s006_425") from _call_BlinkXS3_831
    deb "La verdad es que estaba muy guapa. Tú, sin embargo..."
    mc "*Risa* Yo parecía un tonel al que le hubieran puesto un smoking."
    call BlinkXS3("c29s006_430") from _call_BlinkXS3_832
    deb "*Risa* Yo no diría tanto, pero casi. Si ahora la ropa no te queda demasiado bien, por entonces era horrible."
    if deb._var("route"):
        mc "*Risa* Tener novia para esto..."
    mc "*Risa* ¿Quién quiere enemigos teniendo amigos como tú?"
    deb "*Risa* ¡Hey! ¡Fuiste tú el que empezó esto de no mentir nunca!"
    call BlinkXS3("c29s006_435") from _call_BlinkXS3_833
    eil "*Risa* [deb.nick] tiene razón. Tienes muchas cualidades, pero la elegancia nunca ha sido una de ellas."
    eil "*Risa* Lo bueno de eso es que, te pongas lo que te pongas, te va a quedar igual de mal."
    mc "*Risa* A veces os odio. Por suerte, lo tengo asumido y no le doy importancia."
    mc "Aparte de meteros con mi falta de elegancia, ¿tenéis algún plan para hoy? ¿Queréis que hagamos algo?"
    call BlinkXS3("c29s006_440") from _call_BlinkXS3_834
    deb "Yo tengo que estudiar un montón. Tengo que acabar Villette, de Charlotte Brontë. Voy a estar ocupada todo el fin de semana."
    mc "¡Uff! Eso suena tedioso."
    deb "No es tan interesante como Jane Eyre, pero me está gustando bastante."
    call BlinkXS3("c29s006_445") from _call_BlinkXS3_835
    mc "¿Y tú, [eil]? ¿Algún plan? ¿Trabajas hoy?"
    eil "Sí, trabajo esta tarde después de comer. Por la mañana está [eri] en el café y la relevaré yo."
    mc "¿[sca] sigue emocionada con el trabajo?"
    call BlinkXS3("c29s006_450") from _call_BlinkXS3_836
    eil "Emocionadísima. Aparte de un trabajo en una hamburguesería un par de semanas haciendo una sustitución, va a ser su primer trabajo de verdad."
    eil "Ayer fue a firmar el contrato y a recoger los uniformes. Hoy se pasará la mañana con [eri] en el café. Quiere aprenderlo todo antes de empezar el lunes."
    mc "¿Os deja trabajar tranquilas?"
    call BlinkXS3("c29s006_455") from _call_BlinkXS3_837
    eil "*Risa* Intenta no molestar con demasiadas preguntas, pero a veces no puede contenerse."
    mc "*Risa* Esa es nuestra [sca]. Cuando se emociona con algo no puede parar."
    eil "*Risa* Lo bueno es que el lunes no tendré casi nada que enseñarle."
    scene c29s006_460
    deb "Yo estaría al revés, acojonada por todo lo que puede salir mal en mi primer día de trabajo."
    deb "Estoy segura de que me aturdiría en el momento en que tuviera que preparar dos pedidos diferentes."
    call BlinkXS3("c29s006_465") from _call_BlinkXS3_838
    eil "Y a ella le pasará lo mismo. Pero el lunes estaré yo con ella, y el martes estaremos tanto [eri] como yo. Y al menos sabe llevar una bandeja."
    eil "Nadie le va a exigir que el primer día haga el mismo trabajo que hacemos las que llevamos meses ahí."
    mc "Sería injusto en sus primeros días. Sólo espero que no os dé más trabajo del que os quita."
    scene c29s006_470a with dissolve
    deb "Bueno, yo me tengo que ir a seguir leyendo. Os veo luego."
    eil "Yo también me voy a ir. Quiero hablar de unos temas con mi madre antes de que se vaya a la biblioteca."
    mc "Os veo luego, chicas. Yo voy a desayunar algo."
    scene c29s006_470b with fade
    "Te quedas solo en la cocina y tomas un desayuno ligero. A estas horas sólo queda un dónut después de que todo el mundo haya desayunado."
    stop music fadeout (1.5)
    if mar._var("route"):
        "Se te escapa una sonrisa al ver el tipo de dónut que te vas a comer."
    return
label c29s006_SaiEvaMad:
    if _in_replay:
        $ mc._var("relationships", 0, "set")
        call mrS3_edmund_Story from _call_mrS3_edmund_Story
        call mrS3_mad_route from _call_mrS3_mad_route_14
        call mrS3_sai_route from _call_mrS3_sai_route_12
        call mrS3_dap_route from _call_mrS3_dap_route_15
        call mrS3_sca_route from _call_mrS3_sca_route_11
        if not dap._var("route"):
            call mrS3_emm_route from _call_mrS3_emm_route_24
            if not emm._var("route"):
                call mrS3_eri_route from _call_mrS3_eri_route_14
                if not eri._var("route"):
                    call mrS3_mar_route from _call_mrS3_mar_route_24
                    if not mar._var("route"):
                        call mrS3_nor_route from _call_mrS3_nor_route_14
        if mc._var("relationships")<2:
            call mrS3_rels from _call_mrS3_rels_31
    scene c29s006_600a with fade
    "Mientras tanto, en un café al otro lado de Newport..."
    play music ("music/Looking-Forward.ogg")
    eva "Espero que [nor] tenga razón y no sea para tanto."
    if mad._var("route"):
        mad "Yo también. Me he pasado la noche pensando en ello."
    else:
        mad "Yo también. Por suerte, no tengo que pasar por ello."
    mad "¿Quién queda por venir?"
    if dap._var("route") and sca._var("route"):
        eva "Creo que sólo [dap] y [sca]. Vendrán el lunes, cuando [sca] salga de trabajar." id c29s006_SaiEvaMad_64a74a37
    elif dap._var("route"):
        eva "Creo que sólo [dap]. Vendrá el lunes, cuando [sca] salga de trabajar." id c29s006_SaiEvaMad_bfe8d490
    elif sca._var("route"):
        eva "Creo que sólo [sca]. Vendrá mañana, cuando salga de trabajar." id c29s006_SaiEvaMad_13ddcc41
    else:
        eva "Creo que no queda nadie más."
    if dap._var("route") and sca._var("route"):
        eva "[dap] se va a pasar la mañana en el café, dándole apoyo moral a [sca]."
    sai "No le demos más vueltas y cambiemos de tema. ¿Qué os parecen las chicas nuevas?"
    call BlinkXS3("c29s006_605") from _call_BlinkXS3_839
    eva "Tu prima es guapísima. Y el resto no se quedan atrás. Creo que la tal [zoe] me va a caer bien."
    eva "Pero la tal [cri.nick] me da mala espina."
    call BlinkXS3("c29s006_610") from _call_BlinkXS3_840
    mad "¿Por qué? [eri] dijo que [mc] había dicho lo mismo, pero supongo que no es por que vaya teñida."
    mad "Parece casualidad que las dos asiáticas de la familia vayamos teñidas, ¿no? Y a mí no me juzgáis por eso."
    call BlinkXS3("c29s006_615") from _call_BlinkXS3_841
    sai "*Risa* Me gusta que ya las consideres de la familia antes aún de que hayan llegado."
    call BlinkXS3("c29s006_620") from _call_BlinkXS3_842
    mad "¡Oops! Ni me había dado cuenta de que lo había hecho. Pero... es normal, ¿no?"
    mad "Lo hemos vivido con cada persona que se ha acercado a los Marks. Es lógico que les pase a las chicas nuevas también."
    call BlinkXS3("c29s006_625") from _call_BlinkXS3_843
    eva "¿Cada persona? *Risa* Querrás decir cada chica."
    eva "Por norma los hombres salen mal parados cuando se acercan a los Marks."
    call BlinkXS3("c29s006_630") from _call_BlinkXS3_844
    sai "No todos. Fíjate en Jamaal. Y si siguen saliendo juntos, creo que Anthony no tendrá ningún problema en unirse a la familia."
    call BlinkXS3("c29s006_635") from _call_BlinkXS3_845
    mad "No lo conozco aún, pero, por lo que me habéis contado, parece un tipo majo."
    call BlinkXS3("c29s006_640") from _call_BlinkXS3_846
    eva "Anthony es un... tío simpático. Y parece una persona interesante. Cuando lo investigué..."
    call BlinkXS3("c29s006_645") from _call_BlinkXS3_847
    mad "¿Lo investigaste? ¿Por qué? ¿Había algo sospechoso en él? ¿O nos has investigado a todas?"
    call BlinkXS3("c29s006_650") from _call_BlinkXS3_848
    eva "Bueno... investigué a su hermana, la médico de [mee]. Al investigarla a ella, empezaron a salir nombres y también los investigué. Anthony estaba entre ellos."
    eva "Y sí. También os he investigado a vosotras. *Risa* Si te acercas a los Marks vas a ser investigado."
    call BlinkXS3("c29s006_655") from _call_BlinkXS3_849
    sai "¡Pero eso es injusto! ¡Somos de la familia!"
    call BlinkXS3("c29s006_660") from _call_BlinkXS3_850
    eva "¿Tú sabías que ibas a ser de la familia cuando bajaste de aquel avión? Yo tampoco. Tenía que estar segura de que eras de fiar."
    eva "[ama] incluso investigó a Tía [bet] y a [mee] cuando llegaron."
    call BlinkXS3("c29s006_665") from _call_BlinkXS3_851
    mad "Entonces habéis investigado también a las chicas nuevas, ¿no? ¿Hay algo interesante que debamos saber?"
    call BlinkXS3("c29s006_670") from _call_BlinkXS3_852
    eva "Son chicas normales... O tan normales como sois vosotras."
    call BlinkXS3("c29s006_675") from _call_BlinkXS3_853
    mad "*Risa* No sé si sentirme halagada o insultada."
    mad "Pero aún no has dicho por qué te da mala espina [cri.nick]. ¿Es por algo que has descubierto cuando la investigabas?"
    call BlinkXS3("c29s006_680") from _call_BlinkXS3_854
    eva "No, sólo es una corazonada. Lo que me dijo [eri] sobre ella me puso los pelos de la nuca de punta y he aprendido a hacerle caso a mi instinto."
    eva "Después me dijo que [mc] había dicho lo mismo. Quizás compartimos instinto."
    call BlinkXS3("c29s006_685") from _call_BlinkXS3_855
    sai "Yo entiendo por qué [mc] reaccionó así. En Portland había una chica parecida. Pelo rosa, estudiaba Estudios de Género, y siempre estaba hablando del patriarcado."
    sai "Era compañera de habitación de una amiga mía y, cuando se enteró de que [mc] y yo teníamos una relación abierta, estuvo machacándome durante días."
    sai "Decía que era una nueva herramienta que había inventado el patriarcado para dominar a las mujeres. Una estupidez, vaya."
    call BlinkXS3("c29s006_690") from _call_BlinkXS3_856
    mad "Nunca entenderé por qué la gente se mete en las relaciones de los demás."
    if mc._var("relationships")>1:
        mad "No quiero saber qué pensaría tu amiga de que [mc] tenga un harén. Seguramente le daría una apoplejía."
    call BlinkXS3("c29s006_695") from _call_BlinkXS3_857
    eva "Supongo que por eso desconfía de [cri.nick]."
    if mc._var("relationships")>1 or emm._var("route") or nor._var("route") or eri._var("route") or mar._var("route") or dap._var("route"):
        eva "Las relaciones de [mc] no son muy... normales."
    elif sca._var("route") and persistent.family and mc._var("edmundsStory"):
        eva "Si [mc] está saliendo con su medio hermana..."
    eva "Y si alguien como tu amiga descubriera lo de los clones... No sé cómo reaccionaría."
    call BlinkXS3("c29s006_700") from _call_BlinkXS3_858
    sai "No era mi amiga. Era la compañera de habitación de una amiga mía."
    sai "Pero precisamente por eso tanto [mc] como yo vamos a desconfiar de ella hasta que demuestre que no nos tenemos que preocupar."
    sai "[mc] es mejor persona que yo en eso y seguramente haya decidido darle el beneficio de la duda. Yo prefiero ser cauta."
    call BlinkXS3("c29s006_705") from _call_BlinkXS3_859
    mad "Me parece lógico con vuestra experiencia con aquella chica de Portland."
    mad "¿Y tu prima? ¿Qué sabe de todo lo que está pasando en casa? ¿Qué le parece todo esto?"
    call BlinkXS3("c29s006_710") from _call_BlinkXS3_860
    sai "Sabe algunas cosas, pero no todo."
    if sai._var("route"):
        sai "Sabe que estoy con [mc]."
    else:
        sai "Sabe que [mc] y yo no hemos vuelto juntos."
    if mc._var("relationships")>1:
        sai "Pero no le he contado nada del harén. Creo que será mejor explicárselo en persona."
    sai "Y, obviamente, no sabe nada sobre NTR, clones, y guerras internas. No es que no me fíe de ella, pero es algo que no puedes explicar en una video conferencia."
    call BlinkXS3("c29s006_715") from _call_BlinkXS3_861
    eva "¿Cómo crees que se va a tomar lo de los clones?"
    call BlinkXS3("c29s006_720") from _call_BlinkXS3_862
    sai "Va a flipar. Siempre le ha gustado la ciencia ficción y lo que pasa en esta familia es lo más parecido que ha experimentado nunca."
    if persistent.family:
        sai "*Risa* Seguramente [ama] y tú no os la podáis quitar de encima durante meses."
    else:
        sai "*Risa* Seguramente [eri], [dap] y [emm] no se la puedan quitar de encima durante meses."
    sai "Pero lo va a aceptar sin ningún problema."
    call BlinkXS3("c29s006_725") from _call_BlinkXS3_863
    eva "Era una de las cosas que me preocupaban. No solo por ella, sino por todas las chicas nuevas."
    eva "[ama] no va a estar en casa cuando lleguen y [dap], [eri] y yo podríamos pasar por trillizas..."
    eva "Pero no quiero empezar la relación con las chicas nuevas mintiéndoles. Somos quienes somos. No somos trillizas."
    call BlinkXS3("c29s006_730") from _call_BlinkXS3_864
    mad "Joder, es complicado. No sé si yo sería capaz de decirle algo así a alguien que acaba de llegar a casa."
    mad "Al menos hasta no saber si podemos confiar en ellas. Es algo raro..."
    call BlinkXS3("c29s006_735") from _call_BlinkXS3_865
    if persistent.family:
        eva "*Risa* ¿Estás diciendo que soy rara? Te recuerdo que puedo sacarte uno de esos bonitos ojos con una cucharilla."
    else:
        eva "*Risa* ¿Estás diciendo que [emm], [dap], y [eri] son raras? Te recuerdo que puedo sacarte uno de esos bonitos ojos con una cucharilla."
    eva "*Risa* [sai] no es la única que puede amenazar con sacar ojos, ¿no?"
    call BlinkXS3("c29s006_740") from _call_BlinkXS3_866
    sai "*Risa* Sois unas idiotas. ¡Lo dije antes de conocer a [eil]! ¿Cuánto tiempo me lo vais a echar en cara?"
    scene c29s006_600b with dissolve
    mad "*Risa* El resto de tu vida." (multiple=2)
    eva "*Risa* Para siempre." (multiple=2)
    call BlinkXS3("c29s006_745") from _call_BlinkXS3_867
    sai "*Risa* Si lo llego a saber, no os lo cuento. Capullas."
    stop music fadeout (1.5)
    sai "Pero deberíamos irnos ya. No tengo por qué aguantaros y ya debe ser casi nuestro turno."
    return
label c29s007_OmaLis:
    if _in_replay:
        call mrS3_kat_route from _call_mrS3_kat_route_2
        call mrS3_kat_slim from _call_mrS3_kat_slim_3
        call mrS3_lis_route from _call_mrS3_lis_route_22
    scene black with dissolve
    play music ("music/LostVoices.ogg")
    "Pasas el resto de la mañana en tu habitación. Por extraño que parezca, nadie viene a verte."
    "Cuando bajas a la cocina a por agua, incluso parece que no haya nadie en casa."
    "O incluso que, por alguna razón, te están evitando. Cuando vuelves a tu habitación, oyes susurros y risas ahogadas detrás de las puertas." id c29s007_OmaLis_33b6db9a
    "Decides no llamar a ninguna de esas puertas. Aprovechas la tranquilidad para empezar a preparar maletas para el viaje a Aruba."
    "Ocupas parte del gimnasio para ir dejando las maletas que acabas. Por un momento, temes estar pareciéndote a [lis]."
    stop music fadeout (1.5)
    scene c29s007_005a with dissolve
    "Cuando bajas a comer..."
    play music ("music/MorningFunnyBeat.ogg")
    lis "*Risa* Eres demasiado imponente. Bueno, ya no, pero cuando te conocí me dabas un poco de miedo."
    oma "*Risa* Bueno, no nos conocimos en las mejores circunstancias. Estabas rodeada de imbéciles aquel día."
    oma "Creo que, de todos los que había en la playa, Anthony y tú erais los únicos con un cerebro funcional."
    mc "¿Qué tal, chicas? ¿No bajáis a comer?"
    scene c29s007_005b with dissolve
    lis "Bajaremos en un par de minutos."
    oma "Estamos esperando a que [kat] se acabe de cambiar. Hemos llegado hace unos minutos."
    mc "¿Dónde habéis ido? La casa estaba medio vacía."
    call BlinkXS4("c29s007_010") from _call_BlinkXS4_746
    lis "Hemos ido de compras..."
    mc "*Risa* No sé por qué, pero estando tú involucrada, era lo que me imaginaba."
    call BlinkXS4("c29s007_015") from _call_BlinkXS4_747
    oma "Bueno, todas teníamos algo que comprar, con lo que hemos aprovechado y hemos ido juntas."
    oma "*Risa* Ocho chicas de compras juntas es una forma de crear vínculos."
    mc "¿Ocho? ¿Vosotras tres y quién más?"
    call BlinkXS4("c29s007_020") from _call_BlinkXS4_748
    lis "También han venido [sai], [mad.nick], [eva], [nor], y [eri]."
    lis "[mar] nos habló de una tienda nueva en San Luis Obispo y queríamos probarla."
    mc "*Risa* Te tienes que 'Californiear' un poco más. Nadie le llama San Luis Obispo. Con San Luis hay suficiente."
    mc "Pero si iba [mad.nick] con vosotras..."
    call BlinkXS4("c29s007_025") from _call_BlinkXS4_749
    oma "*Risa* Ha podido ver qué vestidos tiene la competencia. Y se ha comprado uno precioso y super elegante."
    oma "Y va a quedar aún más bonito con las adaptaciones que le quiere hacer."
    mc "[mad.nick] tiene mucho talento. Me extraña que no haya diseñado ella misma el vestido."
    mc "Porque es para la gala en San Francisco, ¿verdad?"
    scene c29s007_030An with dissolve
    lis "Supongo que lo usará para la gala... Sí..."
    oma "Lo más probable... Es un vestido que no desentonaría en una gala..."
    lis "Pero lo de diseñar ella misma el vestido..."
    oma "Podría ser una gran idea..."
    mc "Chicas, ¿pasa algo? ¿Me estáis ocultando algo?"
    scene c29s007_030d with hpunch
    oma "¿Qué? ¿Ocultarte algo?"
    lis "¿A qué te refieres?"
    mc "*Risa* Sabéis que me he criado con [emm], ¿verdad?"
    mc "*Risa* Si existiera una 'cara de mentiroso', la Wiki tendría vuestras fotos para ilustrarla."
    call BlinkXS4("c29s007_035") from _call_BlinkXS4_750
    lis "¿Me estás llamando mentirosa?"
    if lis._var("route"):
        lis "¿No confías en tu princesa?"
    mc "*Risa* Eso es algo que [emm] también haría."
    call BlinkXS4("c29s007_040") from _call_BlinkXS4_751
    oma "Te puedo asegurar que no hemos dicho ninguna mentira."
    oma "Te recuerdo que en esta familia no mentimos. Y menos aún cuando hay cámaras cerca."
    mc "*Risa* Okay, okay. No hace falta que me miréis como si fuerais a asesinarme."
    mc "De todas formas, creo que no os voy a sacar ninguna información sobre ese vestido..."
    call BlinkXS4("c29s007_045") from _call_BlinkXS4_752
    kat "Chicas, ya estoy lista. Ya podemos ir a comer."
    mc "Hola, [kat]."
    scene c29s007_045d with hpunch
    kat "¡[mc]!"
    if kat._var("route"):
        scene c29s007_045e with hpunch
        "Con una velocidad sorprendente, [kat] se lanza a tus brazos a por un beso."
        "Si cada encuentro a partir de ahora va a ser así, no va a necesitar subir corriendo al lago muchas más veces."
        "Va a hacer mucho ejercicio corriendo hasta tus labios."
    else:
        scene c29s007_045f with hpunch
        "Con una velocidad sorprendente, [kat] se lanza hacia ti a por un abrazo."
        "Si cada encuentro a partir de ahora va a ser así, no va a necesitar subir corriendo al lago muchas más veces."
        "Va a hacer mucho ejercicio corriendo hasta tus brazos."
    call BlinkXS4("c29s007_050") from _call_BlinkXS4_753
    kat "Ya nos podemos ir. ¡Me muero de hambre!"
    if kat._var("slim"):
        kat "[nor] me ha prometido que la lasaña de verdura que ha preparado hoy me va a gustar."
        mc "*Risa* Al final le pillarás el gusto a la verdura."
        call BlinkXS4("c29s007_055") from _call_BlinkXS4_754
        kat "*Risa* Pero siempre echaré de menos la pizza."
        "Sabes que la salud de [kat] es lo más importante y que tiene por delante varios meses de dieta antes de resolver sus problemas."
        "También sabes que, solo con el ejercicio que está haciendo, también lo resolvería."
        mc "Solo hasta que consigas resolver tus problemas de azúcar. Después podrás comer pizza. Moderadamente."
        "También sabes que va a perder mucho peso en el proceso. Supones que, cuando vuelvas de Aruba, [kat] estará mucho más delgada."
    else:
        kat "Hoy estoy muy contenta de que no me convencieras para comer verduras. ¡[nor] ha hecho lasaña!"
        mc "*Risa* Estoy seguro de que te hubiera hecho una lasaña de verduras para ti."
        call BlinkXS4("c29s007_055") from _call_BlinkXS4_755
        kat "*Risa* Es mejor para ti que no me veas en modo envidiosa y odiando a cada una de las chicas mientras ellas se comen una lasaña de verdad."
        mc "*Risa* Estoy de acuerdo contigo en eso. Yo siempre estaba de mal humor cuando empezaba una dieta."
    kat "*Risa* ¿No sabes que el tomate es una fruta y el trigo para hacer la harina es un vegetal? Una pizza con piña es casi una ensalada de frutas."
    call BlinkXS4("c29s007_060") from _call_BlinkXS4_756
    oma "*Risa* Vámonos antes de que [kat] deje caer que le gusta la pizza con piña. Alguna de las chicas podría dejar de hablarle sólo por eso."
    mc "¿A ninguna os gusta la pizza con piña?"
    call BlinkXS4("c29s007_065") from _call_BlinkXS4_757
    lis "*Risa* No lo sabemos. Cuando alguien saca el tema, intentamos evitarlo. Hay gente muy militante en los dos bandos."
    mc "*Risa* Tienes razón. Mejor evitar el riesgo antes de crear una discusión."
    call BlinkXS4("c29s007_070") from _call_BlinkXS4_758
    kat "*Risa* ¡He dicho que me muero de hambre y seguís hablando de comida cuando hay una lasaña esperándome en casa de [nor]!"
    if kat._var("slim"):
        mc "*Risa* Vamos a ver qué tal están esa lasaña de verduras. Conociendo a [nor], seguro que está buenísima."
    else:
        mc "*Risa* Vamos a ver qué tal está esa lasaña. Conociendo a [nor], seguro que está buenísima."
    if kat._var("route"):
        scene c29s007_075 with dissolve
        "[kat] te coge de la mano para bajar la escalera. Te sientes genial al ver que está tan ilusionada como tú por la nueva relación."
        "Las otras dos chicas os miran tiernamente, alegrándose por ti y por su amiga."
        "[lis] no está dispuesta a reconocerlo todavía, pero hace tiempo que considera a [kat] una amiga."
    scene black with dissolve
    "No te equivocabas sobre lo sabrosa que está la lasaña."
    "Tampoco te equivocabas sobre que no podrías sacarles nada a las chicas sobre el vestido de [mad.nick]."
    stop music fadeout (1.5)
    "¿O es posible que, si no es para la gala, las ocho chicas hayan comprado vestidos para alguna ocasión especial que te estén ocultando?"
    return
label c29s007_DapDebSca:
    if _in_replay:
        call mrS3_deb_route from _call_mrS3_deb_route_21
        call mrS3_lis_route from _call_mrS3_lis_route_23
        call mrS3_kim_route from _call_mrS3_kim_route_10
    scene black with dissolve
    play music ("music/LostVoices.ogg")
    "Después de comer las chicas parecen seguir evitándote por alguna razón."
    "Empiezas a echar de menos que alguien venga a pedir tu ayuda con un enchufe o que te pida que la lleves a algún sitio."
    "La única interrupción es cuando [ama] viene a decirte que, si la necesitas, estará con [mar] y [nor] en la cocina de [nor], aprendiendo a cocinar."
    "Te sientes solo por primera vez desde que volviste a casa."
    "Decides bajar a la piscina. Seguro que, tarde o temprano, aparece alguien."
    scene c29s007_100a with dissolve
    stop music fadeout (1.5)
    "Para tu sorpresa, [dap], [sca], y [deb.nick] están en la piscina y no hacen ningún gesto que indique que quieran evitarte."
    play music ("music/m0450.ogg")
    "[sca] incluso te hace señas para que te acerques."
    "¿Estás volviéndote paranoico y malinterpretando la situación?"
    scene c29s007_100b with dissolve #hay más
    mc "Hola, chicas. ¿Qué tal?"
    todas "Bien, ¿y tú?"
    call BlinkXS4("c29s007_105") from _call_BlinkXS4_759
    sca "Estábamos intentando convencer a [deb.nick] para que se una a la partida de DnD."
    mc "¿Jugaremos mañana? No me habéis dicho nada..."
    call BlinkXS4("c29s007_110") from _call_BlinkXS4_760
    dap "No, no jugaremos mañana. He estado ocupada estos días y no tengo preparada la próxima sesión."
    dap "Incluiros a [mad.nick] y a ti ha creado ramificaciones que aún no tengo claras a dónde pueden llevar."
    mc "La próxima partida en la que pueda estar será al volver de Aruba, entonces."
    call BlinkXS4("c29s007_115") from _call_BlinkXS4_761
    sca "Depende... [dap] y yo hemos hablado de jugar contigo por videoconferencia. Supongo que tendrás libre algún domingo por la noche."
    mc "¿Se puede hacer eso? ¿Cómo sabréis lo que saco en los dados?"
    call BlinkXS4("c29s007_120") from _call_BlinkXS4_762
    deb "Porque todas sabemos que no mentirás si sacas una mala tirada."
    mc "*Risa* ¿De qué serviría? Hacer trampas en un juego mata la diversión."
    mc "¿Y te apetece unirte?"
    call BlinkXS4("c29s007_125") from _call_BlinkXS4_763
    deb "Siempre he querido probarlo, y [dap] es una gran contadora de historias, con lo que creo que estaría bien."
    deb "Además, sería otra forma de hacer más cosas con las chicas. Si no me gusta, [dap] podría matar a mi personaje para sacarlo de la historia."
    mc "Parece que ya te han convencido."
    call BlinkXS4("c29s007_145") from _call_BlinkXS4_764
    sca "*Risa* Podemos ser muy insistentes. ¿Qué te parece la idea?"
    mc "No tengo ni idea de cuánto tiempo libre tendré, y hay que tener en cuenta la diferencia horaria, pero me parece buena idea si se pudiera hacer."
    mc "Sería una forma de pasar tiempo con vosotras mientras estoy fuera."
    call BlinkXS4("c29s007_135") from _call_BlinkXS4_765
    dap "Espero que nos llames para más cosas que para jugar. Va a ser una partida cada dos o tres semanas, más o menos. Y te vamos a echar de menos todos los días."
    mc "Yo también, pero no sé si tendré tiempo para hacer 22 videoconferencias diarias."
    call BlinkXS4("c29s007_140") from _call_BlinkXS4_766
    deb "*Risa* Sólo serán 20. [ama] y Tía [bet] estarán allí contigo. ¿Quieres decir que no vas a poder sacar tiempo para hacer 20 llamadas al día?"
    mc "*Risa* ¿Os contentaréis con llamadas de 10 minutos cada una?"
    scene c29s007_100c with dissolve #hay mas
    todas "*Risa* ¡No!"
    mc "*Risa* Entonces creo que haremos algunas llamadas grupales."
    call BlinkXS4("c29s007_130") from _call_BlinkXS4_767
    sca "Hablando en serio, creo que no es necesario que llames a todas las chicas todos los días."
    sca "*Risa* Me puedes llamar a mí y yo les paso tus mensajes."
    mc "*Risa* Cuando has empezado con 'Hablando en serio', creía que ibas a aportar una solución que no incluyera tu asesinato."
    mc "Si me paso una semana sin hablar con cualquiera de vosotras y todos los días hablo contigo..."
    call BlinkXS4("c29s007_150") from _call_BlinkXS4_768
    dap "*Risa* Recordad que hay cámaras en la piscina. [eva] tiene que estar empezando a afilar cuchillos si está escuchando esto."
    mc "*Risa* [eva], sé que me estás escuchando, no te preocupes. Te prometo que no me pasaré una semana sin hablar contigo."
    call BlinkXS4("c29s007_155") from _call_BlinkXS4_769
    deb "*Risa* Creo que eso la calmará un poco. Además, ella pasará un mes contigo allí cuando vuelva [ama]."
    mc "Estaremos trabajando. No creo que eso pueda contar como pasar tiempo juntos."
    mc "Aunque supongo que tendremos tiempo para hacer cosas juntos después del trabajo."
    call BlinkXS4("c29s007_160") from _call_BlinkXS4_770
    sca "Sería raro que estuvieras empleando tu tiempo en hacer videoconferencias con Jamaal y con las chicas que nos quedamos y descuidaras a las que están allí contigo."
    if kim._var("route"):
        mc "Sería rarísimo e injusto. Ayer hice una videoconferencia con Meemaw y Tía [bet] cuando estaba acabando el picnic con [kim]."
        mc "Me sentí como si la videoconferencia le estuviera quitando a [kim] tiempo a solas conmigo. Sé que no es así, pero..."
    else:
        mc "Sería rarísimo e injusto. Sería como decir que prefiero a las chicas que os habéis quedado en casa."
    mc "¿Pero sabéis qué es lo raro de verdad?"
    scene c29s007_100d with dissolve #hay mas
    todas "¿Qué?"
    mc "Que vosotras dos estéis dentro de la piscina mientras nuestra sirena residente está fuera. ¿Nuestra sirenita desperdiciando la oportunidad de bañarse? Rarísimo."
    call BlinkXS4("c29s007_165") from _call_BlinkXS4_771
    deb "Bueno... No puedo bañarme hoy..."
    if deb._var("route"):
        mc "¿Por qué? ¿Te encuentras bien?"
        deb "Tengo un pequeño sangrado, y no puedo bañarme hasta que empiece a cicatrizar. No es nada serio, pero no quiero que se infecte y sea peor."
        mcp "(¡Mierda! ¿Le hice daño cuando estuvimos juntos?)"
    else:
        mcp "(¡Mierda! ¡Parezco idiota! Esta chica seguirá teniendo la regla... ¡Parece mentira que me haya criado entre mujeres!)"
    mc "En ese caso, no es tan raro... ¿Qué te pasa?"
    call BlinkXS4("c29s007_170b") from _call_BlinkXS4_772
    sca "¡[mc]! ¡Eso no se le pregunta a una chica cuando no puede bañarse!"
    mcp "(OK. Duda resuelta.)"
    call BlinkXS4("c29s007_170") from _call_BlinkXS4_773
    dap "¿Y tú? ¿Vas a meterte en la piscina con nosotras?"
    mc "Creo que no. Me quedaré sentado en el borde con [deb.nick]. Al menos podrá mojarse los pies."
    dap "Siempre intentando ser el caballero de la brillante armadura."
    mc "Lo hago sin intentarlo... Me sale de dentro."
    scene c29s007_100e with dissolve #Hay más
    deb "Chicas, id a nadar un rato. Os estabais quedando aquí para no dejarme sola, pero ahora tengo a [mc] para hacerme compañía."
    sca "¿No te importa? A nosotras no nos molesta quedarnos contigo toda la tarde."
    deb "No me importa, de verdad. Me estaba empezando a sentir culpable."
    dap "Entonces os dejamos un rato. Vamos a hacer unos largos y un par de carreras."
    stop music fadeout (1.5)
    mc "Pasáoslo bien. Estaremos aquí mismo."
    scene c29s007_175a with fade
    call BlinkXS4("c29s007_175") from _call_BlinkXS4_774
    play music ("music/AmbientPianoStrings.ogg")
    mc "¿Ya has acabado de leer Villette?"
    deb "Aún no. Me gusta, pero es un poco denso y no es un libro para leer demasiadas horas seguidas."
    deb "Me sorprende que recuerdes el título."
    mc "*Risa* Eso es una demostración de que estaba prestando atención, ¿no?"
    call BlinkXS4("c29s007_180") from _call_BlinkXS4_775
    if deb._var("route"):
        deb "*Risa* Tienes razón, pero no esperaba menos de mi novio."
    else:
        deb "*Risa* Tienes razón, pero no esperaba menos de un buen amigo."
    mc "Siempre presto atención a lo que dices." id c29s007_DapDebSca_ae797418
    call BlinkXS4("c29s007_185") from _call_BlinkXS4_776
    deb "Son increíbles, ¿verdad?"
    scene c29s007_190d with dissolve
    mc "¿[dap] y [sca]? Sí, pero no sé a qué te refieres."
    call BlinkXS4("c29s007_190") from _call_BlinkXS4_777
    deb "Iban a renunciar a su tarde en la piscina por no dejarme sola. Estaba a punto de irme a mi habitación cuando has llegado."
    deb "No quería que tuvieran que dejar de nadar por mí."
    mc "No estaban renunciando a nada, [deb.nick]. Estaban pasando tiempo contigo. Estoy seguro de que preferían eso a estar nadando y jugando en el agua."
    call BlinkXS4("c29s007_195") from _call_BlinkXS4_778
    deb "Nunca he tenido amigas así. Es raro, pero increíblemente bonito. [lis] piensa lo mismo."
    if lis._var("route"):
        call BlinkXS4("c29s007_200") from _call_BlinkXS4_779
        deb "Gracias por la noche con [lis], por cierto."
        mc "¿Gracias? No te entiendo..."
        deb "Me explicó que no se había portado bien durante la fiesta..."
        mc "Bueno, sus amigas estaban allí y hacía tiempo que no las veía."
        call BlinkXS4("c29s007_205") from _call_BlinkXS4_780
        deb "No me ha dado detalles, pero me dijo algo sobre descubrir dónde estaba la amistad de verdad."
        scene c29s007_205d with dissolve
        deb "Es genial que, aparte de su novio, te considere su amigo. La entiendo."
        if not deb._var("route"):
            deb "No por lo de novio, claro..."
        mc "No se refería a mí, [deb]. Sino a todas las chicas."
        call BlinkXS4("c29s007_210") from _call_BlinkXS4_781
        deb "Entonces la entiendo mejor aún. Creo que no se podrían tener mejores amigas que las que hemos encontrado en esta familia."
    else:
        call BlinkXS4("c29s007_205") from _call_BlinkXS4_782
        deb "Ayer, cuando volvió de la fiesta en LA, me dijo algo sobre descubrir dónde estaba la amistad de verdad."
        scene c29s007_205d with dissolve
    mc "Me encanta que os sintáis así. Creo que todo el mundo siente algo parecido."
    call BlinkXS4("c29s007_220") from _call_BlinkXS4_783
    deb "Nunca os he dado las gracias por confiar en nosotras con el tema de [ama] y [eva]..."
    mc "Y no hace falta darlas. Era una situación... diferente... y teníamos que confiar en vosotras o esconderlas a ellas."
    mc "Creo que hicimos bien en confiar en vosotras."
    call BlinkXS4("c29s007_225") from _call_BlinkXS4_784
    deb "Yo también pienso lo mismo. Creo que la fiesta de Navidad de [sca] en la playa hizo mucho para que nos sintiéramos integradas."
    deb "Pero que mostrarais esa confianza en nosotras fue el paso definitivo."
    deb "No lo hubiéramos sabido si no lo hubierais hecho, al menos inmediatamente, pero que mostrarais esa confianza en nosotras hizo que..."
    deb "Que sintiéramos que formábamos parte de algo más grande."
    mc "*Risa* Había una tercera opción, pero seguramente [eva] tendría que matarte si te la cuento."
    call BlinkXS4("c29s007_230") from _call_BlinkXS4_785
    deb "*Risa* ¡Muy gracioso! ¿Cuál era la tercera opción?"
    mc "Podríamos haberos mentido, o podríamos haber cerrado el dormitorio, o hacer la presentación de [eva] y [ama] en otro sitio."
    mc "Había muchas opciones, pero la única buena era confiar en vosotras."
    call BlinkXS4("c29s007_235") from _call_BlinkXS4_786
    deb "Me alegra que lo hicierais. Y me alegra poder considerar amigas a [ama] y a [eva]."
    mc "Os necesitan. Nos necesitan a todos. Necesitaban una familia, y ahora la tienen."
    call BlinkXS4("c29s007_240") from _call_BlinkXS4_787
    deb "Pero es un camino de dos direcciones. Nosotras también las necesitamos a ellas. Y las queremos. No me puedo imaginar mi vida sin las dos en ella."
    deb "O sin [dap] y [sca]. O sin ti... Creo que no podría renunciar a nadie de las personas que he conocido aquí."
    mc "¿Se lo has dicho alguna vez?"
    call BlinkXS4("c29s007_245") from _call_BlinkXS4_788
    deb "No. Me sentiría ridícula si lo hiciera. No vas por ahí diciéndole eso a una amiga sin venir a cuento."
    mc "A mí me lo acabas de decir, y creo que deberías decírselo a [ama]. [eva] ya te ha escuchado."
    call BlinkXS4("c29s007_250") from _call_BlinkXS4_789
    deb "¡Oh, mierda! [eva]... lo digo en serio... Os quiero a las dos. Siento no habértelo dicho antes."
    mc "Ahora solo falta que se lo digas a [ama]. No sería justo para ella que lo viera en una grabación en diferido."
    call BlinkXS4("c29s007_255") from _call_BlinkXS4_790
    deb "¿Sabes dónde está?"
    mc "[nor] y [mar] iban a enseñarle nociones básicas de cocina."
    scene c29s007_260a with fade
    call BlinkXS4("c29s007_260") from _call_BlinkXS4_791
    deb "Entonces voy para allá. Una vez se lo he dicho a [eva]... Me siento menos ridícula... ¿Vienes conmigo?"
    mc "Creo que debe ser una conversación entre vosotras. Y [mar] y [nor], obviamente."
    deb "Gracias, [mc]."
    scene c29s007_265a with fade
    "Tras despediros de [dap] y [sca], [deb.nick] se dirige a la cocina de [nor]."
    "Decides ir a darte una ducha y tú también te despides de las dos chicas que hay en el agua."
    scene c29s007_265b with fade
    "Después de intentar secarse infructuosamente las lágrimas que corren por sus mejillas, [eva] hace una copia del video de lo que acaba de pasar en la piscina."
    "Algún día descubrirás que el servidor privado de [eva] está lleno de recuerdos tiernos."
    scene c29s007_265c with fade
    "El servidor de [ama] también tiene muchos recuerdos, y tendrá uno más en cuanto vuelva a la base y pueda hacer una copia."
    "La verás reproduciendo esos recuerdos muchas veces durante el primer mes en Aruba."
    "Te unirás a ella muchas de esas veces."
    "Reiréis y lloraréis juntos mientras los veis."
    scene black with dissolve
    stop music fadeout (1.5)
    "Los dos servidores no harán más que crecer en los años venideros."
    return
label c29s007_KiaWatersports:
    if _in_replay:
        call mrS3_kia_urination from _call_mrS3_kia_urination
    scene black with dissolve
    call BlinkXS4("c29s007_300") from _call_BlinkXS4_792
    play music ("music/Bolero.ogg")
    "Después de la ducha, y de la cena, al volver a casa tras ayudar a [nor] a recoger la cocina..."
    mc "Hola, [kia]. No te he visto irte."
    kia "He venido a ayudar a [mar] a traer algunas cosas para guardar en la nevera."
    call KissXS4("c29s007_305") from _call_KissXS4_20
    call BlinkXS4("c29s007_305") from _call_BlinkXS4_793
    mc "Ya que estás aquí... ¿quieres subir a mi habitación un rato?"
    kia "Me gustaría, pero me duele la espalda y sé cómo acabaría."
    mc "¿Quieres un masaje? Soy bueno dándolos."
    call BlinkXS4("c29s007_310") from _call_BlinkXS4_794
    kia "No creo que un masaje vaya a ayudarme, pero gracias por ofrecerte."
    kia "Además, [kim], [eil], y [sai] me están esperando para ver una serie en la tele."
    mc "Entonces no te entretengo. Tómate un analgésico para el dolor de espalda antes de irte a la cama."
    call KissXS4("c29s007_305") from _call_KissXS4_21
    call BlinkXS4("c29s007_305") from _call_BlinkXS4_795
    kia "Lo haré. Hasta mañana, [mc]."
    mc "Hasta mañana, preciosa."
    mc "Voy al lavabo y subiré a mi habitación a leer unos correos, ya que mi bibliotecaria favorita no quiere subir."
    if kia._var("urination"):
        call BlinkXS4("c29s007_315") from _call_BlinkXS4_796
        kia "¿Vas al lavabo? ¿A orinar?"
        mc "Sí, ¿por qué?"
        kia "¿Puedo acompañarte? Las chicas pueden esperar un par de minutos más..."
        if persistent.walkthrough:
            $ wt1 = _("Escena de orina.")
            $ wt2 = _("Sin consecuencias.")
        else:
            $ wt1 = ""
            $ wt2 = ""
        menu:
            "Por supuesto" (wt=wt1):
                mc "Pero vamos ya. Realmente tengo ganas de mear."
                scene c29s007_325a with fade
                call BlinkXS4("c29s007_325") from _call_BlinkXS4_797
                mc "¿Cómo quieres hacerlo? ¿Quieres mirar? ¿Quieres tener a Mjolnir en la mano?"
                kia "¡Lo segundo! *Risa* ¡Oops! He sonado demasiado ansiosa."
                mc "*Risa* Pues puedes hacer los honores."
                scene c29s007_330AnBlink with dissolve
                "[kia] se arrodilla frente a ti y te desabrocha los pantalones para sacar a Mjolnir. Ya está en orden de batalla. Parece que a él también le excita la situación."
                kia "¿No va a ser difícil mear con una erección?"
                mc "*Risa* Por norma lo es. Pero me parece que encontrarás una solución. Es culpa tuya que esté así."
                scene c29s007_330g with fade
                "La pelirroja se pone a tu lado, agarrando tu polla con su mano, y apuntando al retrete."
                kia "Ya puedes mear."
                mc "*Risa* Lo dices como si fuera fácil. Y además sin levantar la tapa. Que [mar] no se entere."
                "Te sientes raro con la preciosa bibliotecaria cogiendo tu dura polla mientras espera que las primeras gotas de líquido dorado empiecen a salir."
                call BlinkXS4("c29s007_335") from _call_BlinkXS4_798
                kia "A lo mejor esto te ayuda..."
                mc "¿El qué?"
                kia "Esto."
                scene c29s007_335d with dissolve
                "Los labios de [kia] buscan los tuyos apasionadamente."
                "No sabes si el beso te ayudará a mear con una erección, pero sabes que va a incrementar la dureza de Mjolnir."
                scene c29s007_335e with dissolve
                "Un potente chorro hace su aparición en el momento en que dejas de pensar en lo rara que es la situación y empiezas a disfrutar del beso."
                call BlinkXS4("c29s007_340") from _call_BlinkXS4_799
                kia "¡Ha funcionado!"
                mc "*Risa* Tienes unos labios mágicos."
                scene c29s007_345An with dissolve
                "[kia] mira alternativamente al chorro que sale de tu polla y a ti."
                kia "¡Puedo notar cómo recorre tu polla por dentro! Es una sensación... extraña."
                mc "¿Es lo que esperabas?"
                call BlinkXS4("c29s007_350") from _call_BlinkXS4_800
                kia "No lo sé. No esperaba nada. Ha sido una ocurrencia del momento."
                kia "¿Crees que soy rara porque me guste esto?"
                mc "Si lo creyera no estaríamos aquí. Me has preguntado si me podías acompañar y..."
                scene c29s007_335f with dissolve
                "La madre de [eil] vuelve a besarte, sin dejarte acabar la frase, mientras el líquido dorado continúa fluyendo hasta agotarse por completo."
                "Continúa besándote una vez ha dejado de fluir."
                scene c29s007_355a with fade
                call BlinkXS4("c29s007_355") from _call_BlinkXS4_801
                mc "¿Estás segura de que no quieres subir a mi habitación?"
                kia "Por desgracia, lo estoy. Mi dolor de espalda no me permitiría darte lo que mereces."
                mc "Entonces sólo queda sacudir a Mjolnir, ¿no? ¿Quieres acabar el trabajo?"
                scene c29s007_360An with dissolve
                "[kia] sacude tu polla ligeramente hasta que dejan de salir las últimas gotas."
                scene c29s007_365An with dissolve
                "Cuando ya no queda nada, la pelirroja te sorprende metiéndose tu glande en la boca y recorriéndolo con su lengua."
                scene c29s007_365g with dissolve
                pause (1.5)
                call BlinkXS4("c29s007_365") from _call_BlinkXS4_802
                kia "Ya está. Limpia y a buen recaudo."
                mc "Eso ha sido sorprendente. Por un momento he pensado que..."
                call BlinkXS4("c29s007_370") from _call_BlinkXS4_803
                kia "*Risa* ¿Que te iba a hacer una mamada en el baño?"
                mc "*Risa* Sí. Es lo primero que se me ha pasado por la cabeza."
                call BlinkXS4("c29s007_375") from _call_BlinkXS4_804
                kia "¿Aún no me conoces? *Risa* Me gusta el sexo romántico."
                kia "No me veo haciéndote una mamada en un baño como si fuera una prostituta y estuviéramos en el baño de una gasolinera."
                kia "Esto es un poco pervertido, pero no es precisamente romántico."
                mc "No lo decía en ese sentido..."
                call BlinkXS4("c29s007_380") from _call_BlinkXS4_805
                kia "Lo sé. ¿Hay colutorio en este baño?"
                mc "Sí, en ese armario. ¿Por qué?"
                kia "Quiero enjuagarme la boca antes de darte el beso de buenas noches."
                menu:
                    "Me parece una buena idea.":
                        scene c29s007_390d with fade
                        "Tras enjuagarse la boca, la coges entre tus brazos y la besas apasionadamente."
                        "El sabor fresco del colutorio no deja adivinar que hace un momento te estaba limpiando la polla."
                        call BlinkXS4("c29s007_390") from _call_BlinkXS4_806
                        mc "Por desgracia, hay unas chicas esperándote para ver una serie."
                    "No hace falta.":
                        scene c29s007_390d with dissolve
                        "La coges entre tus brazos y la besas apasionadamente."
                        "Notas el sabor extraño, salado y con una reminiscencia de amoniaco, que la limpieza de polla ha dejado en su boca."
                        "Es extraño, pero no es desagradable. La mezcla con el sabor dulce de su pintalabios lo hace más extraño todavía."
                        call BlinkXS4("c29s007_385") from _call_BlinkXS4_807
                        kia "Eso ha sido inesperado..."
                        mc "Sabes que me gusta sorprenderte."
                        mc "Por desgracia, hay unas chicas esperándote para ver una serie."
                        call BlinkXS4("c29s007_390") from _call_BlinkXS4_808
                kia "Tienes razón. Voy a tener que irme o se empezarán a preguntar dónde estoy."
                scene c29s007_305a with fade
                call KissXS4("c29s007_305") from _call_KissXS4_22
                call BlinkXS4("c29s007_305") from _call_BlinkXS4_809
                "La acompañas al recibidor, donde os habéis encontrado hace unos minutos."
            "Prefiero no hacerlo" (wt=wt2):
                mc "Estuvo bien probarlo, y no digo que no lo vayamos a repetir, pero ahora tan solo necesito ir al lavabo."
                call BlinkXS4("c29s007_320") from _call_BlinkXS4_810
                kia "No te preocupes. Lo entiendo. La situación es diferente que en aquella ducha de aquel hotel."
                mc "No te molesta, ¿verdad?"
                kia "No. Es entendible. Es diferente hacerlo en el calor del momento que ahora."
                call KissXS4("c29s007_305") from _call_KissXS4_23
                call BlinkXS4("c29s007_305") from _call_BlinkXS4_811
                kia "Te dejo que vayas al lavabo antes de que tengas un accidente."
    kia "Hasta mañana, [mc]."
    mc "Hasta mañana, preciosa."
    scene black with dissolve
    stop music fadeout (1.5)
    "Subes a tu habitación, pensando que hubiera estado bien darle ese masaje en la espalda."
    return
label c29s009_ScaDapTeaser:
    scene c29s009_005a with fade
    "Te encuentras una sorpresa al llegar a tu habitación."
    dap "Creíamos que no ibas a llegar nunca."
    sca "Llevamos un rato esperándote."
    return

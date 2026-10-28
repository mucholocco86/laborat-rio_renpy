label c32:
    $ erc = TGCharacter ("Eric", color = "#663300")
    $ usn = Character("Usnavy", color="#0BCDF4")
    call c32_engaged from _call_c32_engaged
    if ama._var("route"):
        call c32s001_AmaDate from _call_c32s001_AmaDate
        call c32s001_AmaLewd from _call_c32s001_AmaLewd
    else:
        call c32s002_noAma from _call_c32s002_noAma
    #DayChange
    call c32s002_trainingCamp from _call_c32s002_trainingCamp
    call c32s002_choices from _call_c32s002_choices
    call c32s003_EmmPickup from _call_c32s003_EmmPickup
    call c32s003_JamPics from _call_c32s003_JamPics
    call c32s003_GavArm from _call_c32s003_GavArm
    call c32s003_redecor from _call_c32s003_redecor
    call c32s003_MaelDrug from _call_c32s003_MaelDrug
    call c32s004_Eric from _call_c32s004_Eric
    call c32s004_routine from _call_c32s004_routine
    call c32s004_MarSamArrival from _call_c32s004_MarSamArrival
    if mar._var("route") and sam._var("route"):
        call c32s005_MarSamThreesome from _call_c32s005_MarSamThreesome
    else:
        call c32s005_noThreesome from _call_c32s005_noThreesome
    if mar._var("route"):
        call c32s005_MarLewd from _call_c32s005_MarLewd
    else:
        call c32s005_noMarLewd from _call_c32s005_noMarLewd
    if sam._var("route"):
        call c32s005_SamLewd from _call_c32s005_SamLewd
    else:
        call c32s005_noSamLewd from _call_c32s005_noSamLewd
    call c32s006_AmaSecTeam from _call_c32s006_AmaSecTeam
    call c32s006_Hailey from _call_c32s006_Hailey
    call c32s006_Gav from _call_c32s006_Gav
    call c32s007_cult from _call_c32s007_cult
    call c32s007_teaser from _call_c32s007_teaser
    return
label c32_engaged:
    if sai._var("route"):
        $ sai._var("engaged", True)
    if mar._var("route"):
        $ mar._var("engaged", True)
    if emm._var("route"):
        $ emm._var("engaged", True)
    if eri._var("route"):
        $ eri._var("engaged", True)
    if nor._var("route"):
        $ nor._var("engaged", True)
    if dap._var("route"):
        $ dap._var("engaged", True)
    if sca._var("route"):
        $ sca._var("engaged", True)
    if eil._var("route"):
        $ eil._var("engaged", True)
    if sam._var("route"):
        $ sam._var("engaged", True)
    if sim._var("route"):
        $ sim._var("engaged", True)
    if oma._var("route"):
        $ oma._var("engaged", True)
    if eva._var("route"):
        $ eva._var("engaged", True)
    if mad._var("route"):
        $ mad._var("engaged", True)
    if meg._var("route"):
        $ meg._var("engaged", True)
    if ama._var("route"):
        $ ama._var("engaged", True)
    if mee._var("route"):
        $ mee._var("engaged", True)
    if kim._var("route"):
        $ kim._var("engaged", True)
    if kat._var("route"):
        $ kat._var("engaged", True)
    if deb._var("route"):
        $ deb._var("engaged", True)
    if lis._var("route"):
        $ lis._var("engaged", True)
    if bet._var("route"):
        $ bet._var("engaged", True)
    if kia._var("route"):
        $ kia._var("engaged", True)
    return
label c32s002_noAma:
    scene c32s002_550d with fade
    "Después de cenar..."
    play music ("music/1000lichter.ogg")
    mc "¿Qué haces, [ama]?"
    call BlinkXS4("c32s002_550") from _call_BlinkXS4_1870
    ama "Estaba mirando esta foto. Sé que es una foto genérica de un campo con margaritas, pero..."
    ama "Si no fuera por esa roca que está ahí en medio, pensaría que es el viejo campo de tiro."
    mc "¿El viejo campo de tiro?"
    call BlinkXS4("c32s002_555") from _call_BlinkXS4_1871
    ama "Supongo que [eva] te ha hablado de cuando nos apuntaban a la cabeza en el campo de tiro en el momento en que nos daban un arma."
    mc "Sí. Es inhumano."
    call BlinkXS4("c32s002_560") from _call_BlinkXS4_1872
    ama "Las series más mayores pasamos por eso. Los A, B, C, D, y nosotras. Creo que incluso los E."
    ama "Cuando los A fueron lo suficientemente mayores como para entrenar al resto de las series, despidieron a aquellos instructores."
    ama "Entonces, los A se negaron a usar ese campo de tiro para entrenarnos nunca más."
    call BlinkXS4("c32s002_565") from _call_BlinkXS4_1873
    ama "La excusa es que se había quedado pequeño para las series nuevas, que eran más numerosas. No cabían 20 Fs disparando allí."
    ama "Pero la verdadera razón es que nadie quería volver allí."
    mc "Lo entiendo. Supongo que lo pasasteis mal."
    call BlinkXS4("c32s002_570") from _call_BlinkXS4_1874
    ama "Ahora lo usan algunos de los chicos cuando quieren competir entre ellos."
    ama "Por norma, son chicos que no vivieron aquella época y a los que no van a dejar competir en el campo que está en uso."
    ama "El viejo campo de tiro se ha convertido en un oasis de tranquilidad."
    mc "Excepto cuando quieren competir, ¿no?"
    call BlinkXS4("c32s002_575") from _call_BlinkXS4_1875
    ama "No lo hacen a menudo. Los instructores, de los C a los F, los mantienen ocupados."
    ama "Pero es un sitio bonito con recuerdos feos. Te lo enseñaré cuando vayamos a la base de entrenamiento... si quieres."
    mc "Si lo vas a pasar mal volviendo allí, no es necesario."
    call BlinkXS4("c32s002_580") from _call_BlinkXS4_1876
    ama "Creo que volver allí después de tanto tiempo puede ser bueno. Para crear nuevos recuerdos."
    ama "Recuerdos diferentes para una empresa diferente."
    mc "Si es lo que piensas, de acuerdo. Aceptaré la visita turística al campo de tiro."
    call BlinkXS4("c32s002_585") from _call_BlinkXS4_1877
    ama "Pero ya hablaremos de eso mañana. Me caigo de sueño."
    mc "Entonces no te entretengo más. Ve a dormir."
    scene c32s002_585d with dissolve
    ama "Gracias por todo, [mc]."
    mc "Estoy aquí para lo que necesites."
    stop music fadeout (1.5)
    ama "Sabía que ibas a decir eso."
    scene c32s002_585e with fade
    play music ("music/Bolero.ogg")
    "Mientras [ama] va al lavabo antes de dormir, miras si hay alguna novedad en los foros de My Residence."
    "Parece que va a haber una cita con una de las humanas que hay infiltradas entre los aliens."
    "Estás seguro de que Clichecita habrá hecho algo interesante con ella."
    "Los niveles más altos entre sus suscriptores, que ya han jugado la actualización, dicen que la cita es muy bonita."
    "Ha sido la chica que más ha tardado en tener un momento íntimo con el MC y hay mucha expectación en los foros."
    stop music fadeout (1.5)
    return
label c32s001_AmaDate:
    if _in_replay:
        call mrS3_kim_saved from _call_mrS3_kim_saved_2
        $ ama._var("route", True)
        call c31s007_ama from _call_c31s007_ama_1
    call BlinkXS4("c32s001_005") from _call_BlinkXS4_1878
    play music ("music/Happy-Sun.ogg")
    ama "Gracias, [mc]. Y ahora deberíamos irnos."
    mc "¿Ya? ¿Con tanta prisa? Oranjestad va a seguir estando ahí si tardamos cinco minutos más."
    call BlinkXS4("c32s001_010") from _call_BlinkXS4_1879
    ama "Al final no iremos a Oranjestad. Le he pedido ayuda a [car], y tenemos una reserva en un pequeño restaurante."
    ama "Me ha dicho que está lejos de los sitios turísticos, con lo que estaremos casi solos. Pero nos tenemos que ir ya."
    mc "¿Tienes hambre?"
    call BlinkXS4("c32s001_015") from _call_BlinkXS4_1880
    ama "No, pero no quiero perderme la puesta de sol. ¿Sabes qué? Mejor conduzco yo o llegaremos tarde."
    mc "Eso suena interesante. A mí tampoco me gustaría perdérmela."
    scene c32s001_015d with fade
    "[ama] conduce como una posesa a través de las estrechas carreteras. Por suerte no hay demasiado tráfico."
    stop music fadeout (1.5)
    "Realmente tiene prisa por llegar a tiempo para ver el sol esconderse tras el horizonte."
    scene c32s001_015e with fade
    play music ("music/Bolero.ogg")
    "Al cabo de unos minutos, aparca el coche y os dirigís a una callejuela peatonal. Te coge de la mano nada más bajar del coche."
    "La calle tiene los típicos colores que has visto en todas las guías de viaje online sobre Aruba, aunque la arquitectura es algo diferente."
    "Hay una terraza con sombrillas en medio de la calle. Supones que es donde vais a cenar."
    call BlinkXS4("c32s001_020") from _call_BlinkXS4_1881
    ama "Ya hemos llegado."
    mc "¿Vamos a ir a ese restaurante de ahí?"
    ama "Sí, pero no en la terraza. Sígueme."
    call BlinkXS4("c32s001_025") from _call_BlinkXS4_1882
    "Al llegar a la altura de las sombrillas..."
    ama "Espérame un momento aquí. Tengo que entrar dentro."
    mc "No tardes. Ya te echo de menos."
    call KissXS4("c32s001_030") from _call_KissXS4_30
    call BlinkXS4("c32s001_030") from _call_BlinkXS4_1883
    ama "*Risita* Para que la espera se te haga más corta."
    mc "*Risa* Eso te da un par de segundos extra."
    scene c32s001_030e with dissolve
    "Miras a tu alrededor mientras esperas. Lo primero que te llama la atención es el letrero del restaurante."
    "En un país que vive del turismo, hubieras esperado el letrero en inglés, pero parece una mezcla de holandés, italiano, y español."
    "Debe estar en el idioma local. Papiamento o algo por el estilo."
    scene c32s001_030f with dissolve
    "Solo una de las cuatro mesas está ocupada, con lo que, a menos que la gente cene muy tarde aquí, vais a tener intimidad."
    "Le vas a tener que dar las gracias a [car] por recomendaros el precioso sitio."
    "Si hubieras tenido que planificarlo tú, seguramente hubieras mirado las mismas guías de viaje que mira todo el mundo."
    "Y hubieras acabado en un ruidoso restaurante rodeado de turistas que buscan exactamente lo mismo."
    $ saa = TGCharacter ("Saar", color = "#27f5ee")
    scene c32s001_030g with dissolve
    "Al cabo de unos minutos, [ama] aparece con la camarera."
    ama "[mc], esta es [saa], la dueña del restaurante."
    "Pues parece que no era la camarera."
    mc "Encantado de conocerte, [saa]."
    saa "Igualmente, [mc]. Seguidme, os he preparado una mesa en el muelle."
    mc "¿En el muelle?"
    "No has visto ningún muelle cerca, pero parecías un turista despistado fijándote en lo que no era importante."
    call BlinkXS4("c32s001_035") from _call_BlinkXS4_1884
    saa "Oma [car] me ha dicho que os trate como si fuerais de la realeza." id c32s001_AmaDate_53ee9166
    saa "Y el muelle tiene las mejores vistas."
    mc "Te seguimos."
    scene c32s001_040a with fade
    call BlinkXS4("c32s001_040") from _call_BlinkXS4_1885
    "El muelle está al final de la calle, tras unos arcos coloniales. Las sombrillas lo tapaban."
    "Las vistas de la puesta de sol sobre el Caribe son alucinantes."
    saa "Esa es vuestra mesa. Espero que os guste."
    mc "Es espectacular."
    scene c32s001_045d with dissolve
    ama "El sitio es precioso, [saa]. Masha danki."
    saa "An! Mi no tabata sa ku bo ta papia papiamentu."
    ama "Yo hablo un poco de papiamento, pero [mc] no. *Risa* Por la cara que pone, creo que le ha sonado a griego."
    call BlinkXS4("c32s001_045") from _call_BlinkXS4_1886
    saa "Perdón, [mc]. Es raro conocer turistas que hablen mi lengua, y he cambiado de idioma instintivamente."
    mc "No te preocupes, [saa]. *Risa* Esta es mi cara de '¿qué está pasando aquí?'"
    saa "Bueno, sentaos o si no os vais a perder la puesta de sol."
    scene c32s001_050a with fade
    saa "¿Queréis ver el menú o preferís algún plato típico Arubeño?"
    mc "Por mí está bien lo del plato típico. Si miro el menú voy a pedir algo que conozca, con lo que sorpréndeme."
    ama "Yo también prefiero algo típico."
    scene c32s001_050b with dissolve
    saa "¿Os gusta el queso?"
    mc "A mí me encanta."
    ama "¿Keshi yená? Por mí perfecto."
    scene c32s001_050c with dissolve
    saa "Es lo que iba a proponeros. Es un queso holandés relleno, [mc]. Casi es el plato nacional de Aruba."
    saa "Y es ideal para compartir."
    ama "Creo que te va a gustar. Además, NUNCA lleva brócoli."
    mc "Entonces me parece perfecto."
    scene c32s001_055aa with fade
    call BlinkXS4("c32s001_055a") from _call_BlinkXS4_1887
    "Después de que [saa] os tome nota del resto de la cena..."
    ama "Aunque [saa] es muy agradable, tenía ganas de que se fuera."
    mc "¿Por qué?"
    ama "Para pedirte que te levantes. Llevo un rato queriendo besarte."
    scene c32s001_055d with fade
    "Ninguno de los dos necesitáis decir nada. No es una primera cita al uso, y los besos forman parte de vuestra relación."
    "Pero es vuestro primer beso durante una puesta de sol. No será el último."
    scene c32s001_055ba with fade
    call BlinkXS4("c32s001_055b") from _call_BlinkXS4_1888
    "Cuando os volvéis a sentar..."
    mc "Supongo que nunca has estado aquí, ¿no? Tu cara de sorpresa al ver el muelle se parecía mucho a la que debía tener yo."
    ama "Este sitio es precioso. Sabes que no podíamos salir de la base si no era en una misión."
    ama "Las chicas éramos un poco diferentes, teníamos una parte de entrenamiento que incluía mezclarnos con la gente."
    ama "No todo era combate para nosotras. Pero siempre estábamos supervisadas, y nunca estuve aquí."
    mc "Entonces me parece un sitio aún más ideal. La primera vez para los dos."
    mc "Y lo de hablar papiamento, es otra sorpresa en la infinita caja de sorpresas de [ama], ¿no?"
    call BlinkXS4("c32s001_060") from _call_BlinkXS4_1889
    ama "En Aruba hay muchos idiomas. Nosotras crecimos con holandés, inglés y español como idiomas primarios."
    ama "Pero también aprendimos papiamento y otros idiomas criollos del Caribe. Aparte de los típicos: alemán, chino, francés..."
    mc "¿Cuántos idiomas hablas?"
    call BlinkXS4("c32s001_065") from _call_BlinkXS4_1890
    ama "Nunca los he contado. [eva] dice que son 17, pero lleva años diciendo que son 17, y aprendimos más idiomas después de eso."
    ama "Supongo que debo hablar unos 15 idiomas correctamente, con diferentes localismos, y alrededor de otros 15 con un acento bastante marcado."
    call BlinkXS4("c32s001_070") from _call_BlinkXS4_1891
    ama "Pero no quiero hablar de eso. ¿Qué te están pareciendo tus primeros días en la isla?"
    mc "Casi todo ha sido trabajar en cosas para las que no estaba preparado. Pero poco a poco me voy adaptando."
    mc "Esta noche va a ser el mejor momento desde que llegamos."
    mc "¿Y tú? ¿Cómo llevas el volver a Aruba?"
    call BlinkXS4("c32s001_075") from _call_BlinkXS4_1892
    ama "Es diferente de cómo había pensado que sería. Cambiar el puesto de operaciones a seguridad..."
    ama "A veces echo de menos entrenar con los chicos."
    mc "Sabes que puedes hacerlo, ¿no? Que ahora seas la jefa de seguridad, no significa que no puedas ir a disparar con no-tanques."
    call BlinkXS4("c32s001_080") from _call_BlinkXS4_1893
    ama "*Risa* ¡Es un...!"
    mc "*Risa* Un Bradley, un IFV, lo sé. Pero siempre te ríes cuando no me acuerdo del nombre."
    mc "Bueno, casi siempre. A veces me miras como preguntándote si alguna vez me lo aprenderé."
    call BlinkXS4("c32s001_085") from _call_BlinkXS4_1894
    ama "Y ya lo has hecho. Supongo que para ti también debe ser complicado. Demasiadas cosas nuevas."
    mc "Yo crecí sabiendo a distinguir entre modelos de coches y de consolas. Tú creciste sabiendo distinguir entre un Bradley y un T-72."
    mc "Tan solo tengo que aprender en unas semanas lo que tú llevas aprendiendo años."
    call BlinkXS4("c32s001_090") from _call_BlinkXS4_1895
    ama "No es necesario que aprendas cada modelo de arma que hay en el mundo. Eso sería casi imposible en tan poco tiempo, además de todo lo que tienes que hacer."
    ama "Creo que con que aprendas las categorías y para qué sirve cada cosa debería haber suficiente."
    call BlinkXS4("c32s001_095") from _call_BlinkXS4_1896
    ama "Tienes personal para diseñar las operaciones, con lo que no necesitas dominarlo perfectamente."
    ama "Pero al menos no pondrías cara de tonto cuando te hablen de rifles, escopetas y carabinas."
    mc "*Risa* ¿Pongo cara de tonto?"
    call BlinkXS4("c32s001_100") from _call_BlinkXS4_1897
    ama "*Risa* Prefiero no responder a esa pregunta. Es nuestra primera cita y no quiero que te sientas mal."
    ama "*Risa* Quiero que haya una segunda cita algún día."
    mc "*Risa* Me parece bien."
    mc "Solo tengo una pregunta. ¿Por qué hoy?"
    call BlinkXS4("c32s001_105") from _call_BlinkXS4_1898
    ama "Porque [bet] se quedaba en la base. No me hubiera sentido a gusto dejándola sola en casa."
    mc "Si es por eso, podríamos haber tenido la primera cita en Newport."
    mc "Hay algo más, seguro."
    call BlinkXS4("c32s001_110") from _call_BlinkXS4_1899
    ama "Sí. Ayer no pensaste que fuera una psicópata por tener... ya sabes."
    ama "No quería tener la primera cita hasta que no te lo hubiera enseñado."
    ama "No quería que, cuando te lo enseñara, creyeras que te habías acostado con una loca."
    mc "¿Acostarnos? Solo hemos hablado de salir a cenar."
    scene c32s001_115a with hpunch
    call BlinkXS4("c32s001_115") from _call_BlinkXS4_1900
    ama "¿QUÉ? ¿No quieres acostarte conmigo?"
    mc "*Risa* Por supuesto que quiero. Pero también quería ver esa cara de sorpresa."
    mc "*Risa* No soy el único en esta mesa que puede poner cara de tonto."
    call BlinkXS4("c32s001_120") from _call_BlinkXS4_1901
    ama "*Risa* Pero eres el único en esta mesa que no sabe romper una mano por trece sitios diferentes."
    mc "*Risa* Vale. No más bromas que te hagan poner cara de tonta. Ni que pongan en peligro mis manos."
    ama "*Risa* No queremos tener que amputarte las falanges y que acabes teniendo unas manos más pequeñas que [vin]."
    mc "*Risa* Nope."
    stop music fadeout (1.5)
    mc "Pero hablando en serio, creo que te preocupabas demasiado por mi reacción."
    call BlinkXS4("c32s001_125") from _call_BlinkXS4_1902
    play music ("music/Emotional-Piano-Sad.ogg")
    ama "Tampoco sabía cómo me iba a afectar volver a este sitio."
    ama "Me refiero a la base..."
    mc "Creo que lo estás llevando muy bien."
    mc "Por lo que me habéis explicado, creía que tendríais cuentas pendientes con vuestros antiguos instructores."
    call BlinkXS4("c32s001_130") from _call_BlinkXS4_1903
    ama "Los peores no están en la empresa ya. Cuando los A y los C pudieron entrenar al resto de las series, se deshicieron de los exmilitares externos."
    ama "Supongo que [eva] te ha hablado de cuando nos apuntaban a la cabeza en el campo de tiro en el momento en que nos daban un arma."
    mc "Sí, a eso me refería exactamente. Es inhumano."
    call BlinkXS4("c32s001_135") from _call_BlinkXS4_1904
    ama "Las series más mayores pasamos por eso. Los A, B, C, D, y nosotras. Creo que incluso los E."
    ama "Cuando despidieron a esos instructores, los A se negaron a usar ese campo de tiro para entrenarnos nunca más."
    call BlinkXS4("c32s001_140") from _call_BlinkXS4_1905
    ama "La excusa es que se había quedado pequeño para las series nuevas, que eran más numerosas. No cabían 20 Fs disparando allí."
    ama "Pero la verdadera razón es que nadie quería volver allí."
    mc "Lo entiendo. Supongo que lo pasasteis mal."
    call BlinkXS4("c32s001_145") from _call_BlinkXS4_1906
    ama "Ahora lo usan algunos de los chicos cuando quieren competir entre ellos."
    ama "Por norma son chicos que no vivieron aquella época y a los que no van a dejar competir en el campo que está en uso."
    ama "El viejo campo de tiro se ha convertido en un oasis de tranquilidad."
    mc "Excepto cuando quieren competir, ¿no?"
    call BlinkXS4("c32s001_150") from _call_BlinkXS4_1907
    ama "No lo hacen a menudo. Los instructores, de los C a los F, los mantienen ocupados."
    ama "Pero es un sitio bonito con recuerdos feos. Te lo enseñaré cuando vayamos a la base de entrenamiento... si quieres."
    mc "Si lo vas a pasar mal volviendo allí, no es necesario."
    call BlinkXS4("c32s001_155") from _call_BlinkXS4_1908
    ama "Como has dicho, creo que lo estoy llevando... bien."
    ama "Creo que volver allí después de tanto tiempo puede ser bueno. Para crear nuevos recuerdos contigo."
    mc "Si es lo que piensas, de acuerdo. Aceptaré la visita turística al campo de tiro."
    call BlinkXS4("c32s001_160") from _call_BlinkXS4_1909
    ama "El {b}viejo{/b} campo de tiro."
    ama "Y si seguimos hablando de cosas que ya no son importantes, nos vamos a perder la puesta de sol."
    mc "No voy a decidir qué es importante y qué no en este caso."
    stop music fadeout (1.5)
    mc "Demasiado tengo que decidirlo en la empresa."
    scene c32s001_160d with dissolve
    play music ("music/Afrobeat.ogg")
    "Os cogéis de la mano por encima de la mesa mientras miráis como una gigante bola de fuego continúa su inexorable viaje hacia el horizonte."
    "A veces te preocupan los cambios repentinos de humor de [ama]. Quizás este viaje ha llegado demasiado pronto para ella."
    scene c32s001_165a with fade
    call BlinkXS4("c32s001_165") from _call_BlinkXS4_1910
    saa "Chicos, os traigo la comida justo a tiempo para la puesta de sol. He añadido unas krokechi para que las probéis."
    saa "Espero que os guste el pescado y el marisco."
    mc "Por mí está perfecto."
    ama "Gracias, [saa]."
    saa "Buen provecho. Iré saliendo a veros por si necesitáis algo más."
    scene c32s001_165d with dissolve
    "Miras la apetitosa comida por un segundo antes de decidir que tiene una pinta estupenda."
    "Siempre has pensado que muchos turistas se pierden las delicadezas locales por ir a comer a lo seguro, a un MacDonalds."
    "Quizás el tragaldabas que llevas dentro es el que está dirigiendo tus pensamientos ahora mismo."
    call BlinkXS4("c32s001_170") from _call_BlinkXS4_1911
    ama "*Risa* Sé lo que vas a decir."
    mc "¿Qué voy a decir?"
    call BlinkXS4("c32s001_175") from _call_BlinkXS4_1912
    ama "*Fingiendo una voz masculina* Tiene buena pinta, pero estaría igual de a gusto comiéndome una hamburguesa."
    ama "*Fingiendo una voz masculina* Lo importante es que lo voy a compartir contigo."
    mc "*Risa* Casi has acertado. La segunda parte sería 'Lo importante es la compañía.'"
    mc "Pero precisamente estaba pensando en el desperdicio que sería comer una hamburguesa ahora mismo."
    mc "¡Esto tiene una pinta excelente! Y hamburguesas podemos comer las que queramos cuando volvamos a casa."
    call BlinkXS4("c32s001_180") from _call_BlinkXS4_1913
    ama "El Keshi yená está muy bueno. Las krokechi son como croquetas de pescado, pero redondas. No es mi plato favorito, pero también están buenas."
    mc "No te he preguntado nunca cuál es tu plato favorito. Y es la pregunta típica de la primera cita."
    call BlinkXS4("c32s001_185") from _call_BlinkXS4_1914
    ama "*Risa* Cualquier cosa que cocinen [mar] o [nor]. Cocinan genial, pero es que además... su comida sabe a hogar."
    mc "¿Ya las echas de menos? Conozco la sensación."
    call BlinkXS4("c32s001_190") from _call_BlinkXS4_1915
    ama "Echo de menos a todas, pero especialmente a ellas dos y a [eva]."
    ama "No me malinterpretes. Me encanta estar aquí contigo y con Tía [bet], poder dormir contigo cada noche..."
    mc "Pero no hay nada como estar en casa."
    call BlinkXS4("c32s001_195") from _call_BlinkXS4_1916
    ama "Exacto. Aunque haga poco tiempo que formo parte de la familia... Newport es más mi hogar de lo que nunca lo fue Aruba."
    mc "Me alegra que te sientas así respecto a Newport. Tenemos que conseguir que tu concepto de Aruba cambie."
    mc "Tenemos que crear recuerdos nuevos, como has dicho sobre el viejo campo de tiro."
    mc "Y vamos a empezar a hacerlo hoy."
    scene c32s001_200An with dissolve
    "Y creáis recuerdos nuevos."
    "Parece que la puesta de sol se detiene para daros el momento perfecto para cenar bajo su luz."
    "Para crear un recuerdo nuevo."
    "Disfrutáis de la exquisita cena que [saa] os ha preparado."
    "Realmente te daría lo mismo si fuera una hamburguesa. Lo importante es la compañía."
    scene c32s001_205a with dissolve
    "Ni siquiera la aparición de un barco turístico en el último minuto puede estropear la magia del momento."
    "Ninguno de los dos sois capaces de verlo."
    scene c32s001_205b with dissolve
    "Solo tenéis ojos el uno para el otro."
    "Tendréis que volver para ver la puesta de sol otro día."
    "Lo haréis."
    "Y volveréis a perdérosla."
    scene c32s001_210a with fade
    call BlinkXS4("c32s001_210") from _call_BlinkXS4_1917
    "Ni siquiera os habéis dado cuenta de que [saa] ha encendido las luces en algún momento."
    mc "Parece que nos hemos perdido la puesta de sol."
    ama "Había algo más interesante que mirar."
    mc "Esa debería haber sido mi frase..."
    ama "Somos un equipo. Da lo mismo quién diga las frases."
    call BlinkXS4("c32s001_215") from _call_BlinkXS4_1918
    ama "¿Sabes bucear?"
    mc "¿En plan bombonas de oxígeno y esas cosas? No lo he hecho nunca, pero no debe ser {b}tan{/b} difícil, ¿no?"
    ama "Es más difícil de lo que parece. Pero me refería a hacer snorkel."
    mc "¡Ah, sí! Eso sí que sé hacerlo."
    call BlinkXS4("c32s001_220") from _call_BlinkXS4_1919
    ama "Entonces vámonos. [car] me ha enviado la dirección de un sitio donde hacen inmersiones nocturnas."
    mc "¿Ahora?"
    call BlinkXS4("c32s001_225") from _call_BlinkXS4_1920
    ama "*Risa* Hacer inmersiones nocturnas cuando es de día no tiene demasiada gracia. Aparte de que es imposible."
    mc "*Risa* Vale, soy tonto. ¡Pero [car] quiere matarme!"
    call BlinkXS4("c32s001_230") from _call_BlinkXS4_1921
    ama "Ha sido idea mía. Le he preguntado a ella si sabía de algún sitio donde pudiéramos hacer snorkel."
    ama "Estoy segura de que ninguna de tus citas ha tenido una sesión de buceo."
    mc "Una vez más aciertas. Y una vez más, la caja de sorpresas de [ama] parece que no tiene fondo."
    scene c32s001_230d with fade
    "Antes de que puedas ir a pagar, [ama] te da un apasionado beso a la luz de las estrellas."
    "La cita está siendo fantástica."
    stop music fadeout (1.5)
    scene c32s001_235a with fade
    call BlinkXS4("c32s001_235") from _call_BlinkXS4_1922
    play music ("music/Ukulele-Life.ogg")
    "Una vez pagas la cuenta y os despedís de [saa], de vuelta en el coche..."
    ama "¿Te lo estás pasando bien? ¿La cita está yendo como pensabas?"
    mc "La cena y el sitio han sido geniales. Y la compañía inmejorable."
    mc "Pero, otra vez, esa debía ser mi frase."
    mc "¿Qué tal tu primera cita?"
    call BlinkXS4("c32s001_240") from _call_BlinkXS4_1923
    ama "Con ganas de que no termine nunca. Y con ganas de que acabe."
    mc "Sabes que no tenemos por qué ir a hacer snorkel si no quieres, ¿verdad?"
    mc "Si tienes ganas de que acabe, habrá más días en los que podamos hacerlo."
    call BlinkXS4("c32s001_245") from _call_BlinkXS4_1924
    ama "Pero entonces no sería una primera cita memorable."
    mc "*Risa* Esta vez te equivocas. Ya es memorable."
    call BlinkXS4("c32s001_250") from _call_BlinkXS4_1925
    ama "Dentro de 20 años, si tenemos hijos y te preguntan cómo fue nuestra primera cita..."
    ama "¿Quieres decirles 'fuimos a cenar y ya está'?"
    mc "*Risa* Me da lo mismo lo que piensen esos pequeños granujas sobre nuestra primera cita."
    mc "Además, no ha sido solo una cena."
    call BlinkXS4("c32s001_255") from _call_BlinkXS4_1926
    ama "*Risa* Sí, sí. *Imitando a [mc]* 'Me pasé dos horas viendo cómo el sol poniente se reflejaba en los ojos de vuestra madre.'"
    ama "'El mar palidecía de envidia ante tanta belleza. El universo paró el tiempo para que la puesta de sol durara más solo para nosotros.'"
    mc "*Risa* ¿De verdad sueno tan cursi?"
    call BlinkXS4("c32s001_260") from _call_BlinkXS4_1927
    ama "Eso era una imitación diluida de tu cursilería. Pero no por ello me gusta menos."
    mc "*Imitando a un tipo rudo* A ver, tú, conductora. ¿Falta mucho para llegar? ¡Conduces como una abuela!"
    call BlinkXS4("c32s001_265") from _call_BlinkXS4_1928
    ama "*Risa* Ni intentándolo te sale bien, [mc]. No va en tu carácter hablar así."
    ama "Y nadie quiere que lo hagas o ni siquiera que intentes cambiar. Eres un tipo duro en muchos otros sentidos."
    mc "*Risa* Creo que es la primera vez que alguien me llama tipo duro."
    call BlinkXS4("c32s001_270") from _call_BlinkXS4_1929
    ama "Poca gente ha visto cómo trataste a [kev] o a [sol]."
    ama "Alguien no es duro por cómo habla, sino por cómo se comporta cuando de verdad importa."
    mc "Bueno, con [sol] me tuvisteis que salvar el culo [eva] y tú. Y si no hubieras llegado a casa de [sca]..."
    call BlinkXS4("c32s001_275") from _call_BlinkXS4_1930
    ama "Eso no es importante. Lo que importa es que [kia] formaba parte de la familia y la defendiste."
    ama "Que defendiste a [sca] en su casa, enfrentándote a [kev]. Yo solo evité que te denunciaran."
    ama "Que te enfrentaste a unos mercenarios armados cuando [erc] os retuvo en casa de [nor]."
    if kim._var("saved"):
        ama "Que le paraste los pies a [ich] cuando fue necesario para defender a [kim]."
    ama "Muchos de esos tipos rudos a los que intentabas imitar se hubieran arrugado en esas circunstancias."
    call BlinkXS4("c32s001_280") from _call_BlinkXS4_1931
    ama "Y, por cierto, ya hemos llegado. No vuelvas a decir que conduzco como una abuela."
    stop music fadeout (1.5)
    mc "*Risa* Mientras no te diga que cocinas como una abuela, no te puedes quejar."
    scene c32s001_285a with fade
    play music ("music/Beach.ogg")
    "Pagáis por la excursión y subís a un precioso velero en el que os ponéis unos trajes de neopreno."
    "El tipo del barco os dice que habéis tenido suerte. Estaréis solos durante la excursión."
    "En la excursión anterior había ocho turistas rusos. Algunos borrachos. Dice que no ha sido una experiencia agradable."
    scene c32s001_285b with fade
    "Después de navegar un rato..."
    usn "Bueno, hemos llegado. Tan solo tenéis que disfrutar."
    "Habla con un acento colombiano tan fuerte que hace que [oma] parezca una nativa de Oxford."
    usn "Yo iluminaré las zonas más chulas con ese reflector de ahí atrás. Tenéis 45 minutos para disfrutar."
    call BlinkXS4("c32s001_290") from _call_BlinkXS4_1932
    ama "¿Hay alguna indicación de seguridad?"
    "Desde luego, a [ama] le queda mejor su traje de neopreno que a ti el tuyo."
    scene c32s001_285c with dissolve
    usn "*Risa* No os olvidéis de subir a la superficie a respirar."
    usn "Hablo en serio. No esperéis a que os falte el aire."
    usn "Es fácil perder la noción del tiempo ahí abajo, rodeados de tanta belleza."
    "Por la mirada del marinero, que recorre a [ama] de arriba a abajo, sabes a qué belleza se refiere."
    mc "Avísanos a {b}mi esposa{/b} y a mí cuando el tiempo se esté agotando, por favor."
    scene c32s001_285d with dissolve
    "Se da cuenta de que le has pillado mirando a tu esposa y responde visiblemente nervioso."
    usn "S-sí, sí... hare p-parpadear las l-luces cuando se e-empiece a agotar el t-tiempo..."
    "Quizás no necesites hablar como un tipo duro después de todo."
    scene c32s001_295a with fade
    call BlinkXS4("c32s001_295") from _call_BlinkXS4_1933
    ama "*Susurrando* ¿Ves como no te hace falta parecer un leñador para impresionar a la gente?"
    mc "No quería impresionar a nadie. Quería dejar claro que ahora eres mi esposa."
    call KissXS4("c32s001_300") from _call_KissXS4_31
    call BlinkXS4("c32s001_300") from _call_BlinkXS4_1934
    ama "Ahora y siempre. Sígueme... si puedes."
    scene c32s001_300e with dissolve
    "La preciosa mujer se pone las gafas y se sumerge con la agilidad de una orca buscando a su presa."
    stop music fadeout (1.5)
    "Los colores de su traje de neopreno ayudan a esa imagen."
    scene c32s001_305a with fade
    play music ("music/Paradise_Found.ogg")
    "Nada más meter la cabeza dentro del agua para seguir a la maravillosa espía te quedas sin respiración."
    "Y no por las razones obvias, como la falta de aire."
    "La belleza del paraje iluminado por los focos del barco es alucinante."
    scene c32s001_305b with fade
    "Parece que no tenéis ojos para verlo todo, y os vais señalando lo que no queréis que el otro se pierda."
    "Tú te das por contento con no perderte ninguna imagen de [ama]."
    scene c32s001_305c with fade
    "Verla bucear por debajo del agua, con todos sus músculos trabajando sin esfuerzo debería ser una atracción turística."
    "Pero prefieres tener esta imagen para ti solo."
    scene c32s001_305j with fade
    "Te da lo mismo que te llamen egoísta. Hoy [ama] es solo tuya."
    "Mañana la volverás a compartir con el mundo y con la familia."
    scene c32s001_305f with fade
    "Ella parece pensar algo parecido, escondiéndose de ti para aparecer tras una roca para lanzarte un beso."
    "Parece que estar liberada de la gravedad, hace que florezca su parte más juguetona."
    scene c32s001_305e with fade
    "Incluso cuando tiene que volver a la superficie a coger aire es la belleza y la elegancia personificada."
    "Supones que tu debes parecer mucho más torpe que ella en las mismas circunstancias."
    scene c32s001_315a with fade
    call BlinkXS4("c32s001_315") from _call_BlinkXS4_1935
    "Una de las veces que subís a coger aire..."
    ama "¿Te está gustando?"
    mc "Es precioso. Nunca había hecho esto y me está gustando."
    ama "Un día deberíamos certificarte para el uso de bombonas de oxígeno. Ahorraríamos el tener que subir a por aire."
    mc "Entonces no podríamos hablar en medio de la cita."
    ama "*Risa* ¿Quién ha dicho que eso sea algo malo?"
    scene c32s001_305d with fade
    "Volvéis a sumergiros. Empiezas a creer que tu fama de hablar demasiado debe tener algo de verdad."
    "La imagen de [ama] sumergiéndose detrás tuyo debe ser como la última imagen que ve una foca antes de que la orca la devore."
    scene c32s001_305g with fade
    "Supones que tú morirías con una sonrisa como la que muestra tu esposa."
    "Pero eres un pobre iluso. Ni en tus sueños podrías igualar la belleza de esa sonrisa."
    scene c32s001_305h with fade
    "Aunque una sonrisa te recorre por dentro al ver a la siempre seria mercenaria disfrutar bajo el agua."
    "Verla dejar de lado sus preocupaciones para tener un momento para ella es una experiencia tan bonita como su sonrisa."
    scene c32s001_305i with fade
    "[usn] os ha avisado que no veríais peces a estas horas, pero la belleza de los corales hace que ninguno penséis en ellos."
    "Una belleza solo superada por el cuerpo de [ama] en el traje de neopreno."
    scene c32s001_305k with fade
    "Ella sigue disfrutando, en modo juguetón, haciendo poses como si tuvieras una cámara para fotografiarla."
    "Por suerte, tu cerebro tiene la mejor cámara del mundo y nunca olvidarás estos momentos."
    scene c32s001_305n with fade
    "Incluso aunque lo intentaras, te sería totalmente imposible olvidar este día."
    "No sólo es una cita única, sino que ver a [ama] totalmente relajada es una experiencia inolvidable por sí misma."
    scene c32s001_305Anl with dissolve
    "Pero el tiempo pasa más rápido de lo que esperabais y el foco del barco empieza a parpadear."
    "Solo da tiempo para un rápido beso bajo el agua antes de tener que volver a la superficie."
    scene c32s001_305Anm with dissolve
    "Los 45 minutos de inmersión han pasado demasiado rápido para tu gusto."
    "En breve solo quedarán los recuerdos de una experiencia única."
    scene c32s001_310d with fade
    "Volvéis a regañadientes al barco, tristes porque la experiencia ha finalizado."
    "Ver a [ama] subir al barco disminuye un poco tu tristeza."
    scene c32s001_310a with fade
    ama "¿Te ha gustado?"
    "El tono juguetón de su voz comunica la sonrisa que las sombras de la noche esconden."
    mc "Ha sido precioso."
    ama "Pues sube al barco y vamos a casa. La cita no ha acabado."
    scene c32s001_315d with fade
    "Tras ducharos y volver a cambiaros, emprendéis el camino a la casa."
    stop music fadeout (1.5)
    "Los dos estáis ansiosos por continuar con la cita en la casa del CEO."
    return
label c32s001_AmaLewd:
    if _in_replay:
        call mrS3_eva_route from _call_mrS3_eva_route_22
    scene c32s001_320An with dissolve
    play music ("music/LePrunierenFleur.ogg")
    "Al llegar a la casa del CEO, vuestros labios parecen tener prisa en recorrer los labios del otro."
    "La tan esperada noche de bodas llega con casi una semana de retraso."
    "Os besáis todo el camino hasta tu habitación, sin que vuestros labios se separen en ningún momento."
    call BlinkXS4("c32s001_325") from _call_BlinkXS4_1936
    ama "Si sigues besándome así, me va a resultar muy difícil dejarte aquí."
    mc "¿Dejarme aquí? ¿Vas a irte?"
    call BlinkXS4("c32s001_330") from _call_BlinkXS4_1937
    ama "Nunca le he encontrado demasiado sentido a la lencería, pero [mad.nick] me convenció para comprarla."
    ama "Sé que no va a durar mucho sobre mi piel, pero..."
    mc "Pero quieres la experiencia completa."
    call KissXS4("c32s001_335") from _call_KissXS4_32
    call BlinkXS4("c32s001_335") from _call_BlinkXS4_1938
    ama "Sabía que lo entenderías."
    mc "No tardes demasiado. Estoy impaciente por ver esa lencería. Y por quitártela después."
    ama "Sólo serán unos minutos. Te lo prometo. Y se me van a hacer más largos a mí que a ti."
    stop music fadeout (1.5)
    scene c32s001_335e with fade
    "Aprovechas esos larguísimos minutos para desnudarte."
    "No pasan más de cinco o seis minutos antes de que los nudillos de [ama] suenen en la puerta. Te han parecido horas."
    play sound ("music/knock.ogg")
    "*Knock-Knock*"
    mc "Entra, cielo."
    play music ("music/SensualJazzMedium2.ogg")
    scene c32s001_340d with fade:
        yalign 1.0
        linear 5.0 yalign 0.0
    pause (5.0)
    call BlinkXS4 ("c32s001_340") from _call_BlinkXS4_1939
    ama "Espero que te guste..."
    call addProfileImageS3 (7, "ama_7", ama, __(": 15 - Especial"), "") from _call_addProfileImageS3_49
    "Durante un segundo no sabes si seguir babeando o contestarle. Cuando ese segundo finaliza, tu cerebro vuelve a funcionar."
    mc "Estás espectacular."
    call BlinkXS4("c32s001_345") from _call_BlinkXS4_1940
    ama "[mad.nick] dijo que iba con mi estilo... Mi color favorito es el verde y los cinturones le dan un aspecto militar..."
    ama "*Risa* Al menos según ella. Con lo incómodos que son, dudo que nadie se pusiera esto para una misión."
    mc "*Risa* No me imagino a [dam] o a [aar] con eso puesto. Y si alguna vez se lo ponen, no quiero verlos."
    mc "¿Son muy incómodos?"
    call BlinkXS4("c32s001_350") from _call_BlinkXS4_1941
    ama "Son tan incómodos que he estado a punto de no ponérmelos. No se lo digas a [mad.nick]."
    mc "Entonces, voy a tener que ayudarte a quitártelos. Lo último que queremos es que estés incómoda."
    call BlinkXS4("c32s001_355") from _call_BlinkXS4_1942
    ama "*Risita* Veo que tú ya te has puesto cómodo."
    mc "*Risa* Esa no suele ser la primera reacción que veo."
    mc "*Risa* ¿No hay ningún '¡Oh, Dios mío! Es más grande de lo que esperaba' ni ningún 'Eso no va a caber dentro de mí'?"
    call BlinkXS4("c32s001_360") from _call_BlinkXS4_1943
    ama "*Risa* Te he visto tantas veces a través de las cámaras que más bien sería justo al revés."
    ama "Si alguna vez veo otra polla, y no es que tenga intención de verla, reaccionaré con un '¿Solo eso? Mi marido está mejor dotado'."
    ama "Tan solo me sorprendió la primera noche que dormimos aquí. Mientras dormías la presionaste contra mí y... me asusté un poco."
    scene c32s001_360d with dissolve
    "Antes de que puedas decir ninguna tontería impulsada por tu ego, la rubia espía sella tus labios con los suyos."
    "Cualquier cosa que hubieras podido pensar es peor que el silencio lleno de mensajes que se produce durante el beso."
    "Los cinturones de la lencería rozan contra tu piel y puedes entender por qué a tu esposa le resultan incómodos."
    call BlinkXS4("c32s001_365") from _call_BlinkXS4_1944
    ama "Te quiero."
    mc "Yo también te quiero."
    ama "Y te querré aún más cuando me ayudes a quitarme los cinturones."
    scene c32s001_370a with dissolve
    pause (1.5)
    scene c32s001_370b with dissolve
    "Por suerte, son tan fáciles de quitar como incómodos."
    ama "A veces me pregunto si quién diseña lencería la ha usado alguna vez."
    mc "Al menos esta es rápida de quitar."
    call BlinkXS4("c32s001_375") from _call_BlinkXS4_1945
    ama "A eso me refiero. Si he tardado cuatro minutos en ponerme la lencería y tú tardas tres en quitármela, estamos desperdiciando siete minutos."
    mc "Esto no es una hoja de cálculo, [ama]. No todas las sumas dan los mismos resultados."
    mc "El proceso y la anticipación también cuentan."
    scene c32s001_370c with dissolve
    pause (1.5)
    scene c32s001_370d with dissolve
    "Para demostrárselo, retiras el sujetador, liberando dos perfectas tetas de su prisión mientras ella se quita como se llame lo que lleva al cuello."
    mc "¿Ves? Yo puedo disfrutar de cada segundo del proceso de desnudarte."
    ama "*Risa* Mientras sólo sean segundos... Al menos a mí me has ahorrado el trabajo."
    scene c32s001_380a with dissolve
    "No piensas contestar a eso. Tu lengua tiene cosas mejores que hacer. Hay unos duros pezones que tiene que conocer."
    ama "*Gemido* Me ha recorrido un escalofrío por la espalda."
    "Tampoco piensas contestar a eso. Menos aún con la lengua fuera. Sonarías como un idiota."
    scene c32s001_380b with dissolve
    "Tus labios bajan por los perfectos abdominales, mientras se incrementa la anticipación que los dos estáis experimentando."
    "Si alguien intentara usar esos durísimos abdominales como una tabla de carnicero, es posible que muchos cuchillos acabaran mellados."
    scene c32s001_370e with dissolve
    pause (1.5)
    scene c32s001_370f with dissolve
    "Tus manos llegan a la última pieza de ropa que cubre el deseado tesoro. Solo tardas un par de segundos en retirarla."
    "Una sorprendente línea oscura te espera bajo la gruesa tela."
    call BlinkXS4("c32s001_385") from _call_BlinkXS4_1946
    mc "No sé por qué lo imaginaba rubio..."
    if persistent.family:
        ama "Soy el clon de [emm]... "
    else:
        ama "[emm] es mi clon..."
    ama "En mi caso, las cortinas no combinan con la alfombra."
    mc "¿Nunca has pensado en teñírtelo?"
    call BlinkXS4("c32s001_390") from _call_BlinkXS4_1947
    ama "*Risa* Lo hice una vez, poco antes de que llegaran [mee] y Tía [bet]. Parecía que tenía un limón entre las piernas."
    ama "Pero creía que estarías más interesado en otras cosas en vez de en mi historial capilar."
    mc "¿Como, por ejemplo, hacerte pensar en otra cosa para sorprenderte?"
    scene c32s001_380c with hpunch
    "Hundes tu cara entre dos muslos que podrían ser donados como recambios de columnas griegas."
    "El agradable aroma del jabón de ducha se mezcla con el perfume aún más agradable de la humedad provocada por la excitación de la chica."
    ama "*Gemido* ¡Eso es un ataque a traición!"
    ama "*Jadeo* Y aún me tienes que quitar las botas..."
    call BlinkXS4("c32s001_395") from _call_BlinkXS4_1948
    mc "*Tono lastimero fingido* ¿Tenemos que quitar las botas?"
    ama "*Risa* Había oído hablar de tu fetiche con los tacones. Pero lo siento, hoy no."
    ama "Esas correas seguro que hacen daño a alguien. Y no iba a ser a mí."
    mc "*Risa* Vale, me has convencido. No quiero acabar sangrando como un cerdo en nuestra noche de bodas."
    scene c32s001_360e with fade
    "Tras ayudarle a quitarse las botas, vuestros labios vuelven a fundirse en un juego en el que [ama] es una experta."
    "Esta vez no hay cinturones ni tela entre vuestros cuerpos. Puedes sentir el calor que emana de su piel recorriendo la tuya."
    "Pero cualquier beso con [ama] es corto. Daría lo mismo que universos enteros murieran mientras os besáis. Siempre sabrían a poco."
    call BlinkXS4("c32s001_400") from _call_BlinkXS4_1949
    ama "*Jadeo* ¿Podemos pasar ya a la cama? Parecemos dos tontos, besándonos aquí de pie."
    mc "Parece que hay una mujer intentando encontrar un equilibrio entre la practicidad y sus deseos."
    scene c32s001_400d with dissolve
    ama "Y esa cama puede ser el equilibrio perfecto."
    scene c32s001_405An with dissolve
    "Lo que sigue es una eterna sesión de besos. Una sesión que dura un segundo."
    "No tienes ni idea de si algún universo muere mientras os besáis. No te importa."
    "Sería un universo muy desgraciado, ya que no tiene a [ama] en él..."
    "*Tos* Parece que me estoy volviendo tan cursi como [mc]. Espero que Trop no me despida, necesito este trabajo como Narrador."
    scene c32s001_410a with fade
    ama "¿Cómo quieres hacerlo?"
    mc "Tierno y salvaje a la vez. Pero creo que eres tú quién debería decidir cómo quieres que sea tu primera vez."
    call BlinkXS4("c32s001_415") from _call_BlinkXS4_1950
    ama "Lo de tierno me sirve. Lo de salvaje... no tanto."
    call BlinkXS4("c32s001_420") from _call_BlinkXS4_1951
    ama "Estoy un poco... asustada... Y no es por el dolor."
    ama "Y no me digas que, si quiero, podemos dejarlo para otro día."
    mc "No pensaba decírtelo."
    call BlinkXS4("c32s001_425") from _call_BlinkXS4_1952
    ama "¡Me sorprendes!"
    mc "Eres una de las personas más inteligentes que conozco y, desde luego, la más práctica. Y no tienes miedo de decir lo que piensas."
    mc "Si quisieras dejarlo para otro día, lo habrías dicho y no te hubieras puesto la lencería."
    mc "Te hubieras puesto el camisón de gatitos y estaríamos durmiendo abrazados."
    call BlinkXS4("c32s001_430") from _call_BlinkXS4_1953
    ama "Y a ti no te hubiera importado, claro."
    mc "Prefiero que pase lo que va a pasar. Pero ya te dije el día que Zeus rompió la cama que esperaría hasta que estuvieras preparada."
    mc "Al menos los gatitos de tu camisón no romperán esta cama."
    call BlinkXS4("c32s001_435") from _call_BlinkXS4_1954
    ama "*Risa* ¡Estás obsesionado con Zeus!"
    mc "No. *Risa* Estoy obsesionado contigo."
    scene c32s001_435d with dissolve
    "Te incorporas y hundes tu cara entre las dos preciosas tetas de [ama]."
    mc "*Brrrrrr*"
    ama "*Risa* ¡Deja de hacer payasadas!"
    "Si las payasadas sirven para hacer que se ría y se olvide de lo asustada que está, cumplen su función."
    call BlinkXS4("c32s001_440") from _call_BlinkXS4_1955
    ama "¿Te importa si me quedo arriba?"
    mc "¿Quieres tener el control?"
    ama "Quiero saber cuándo parar y cuándo continuar."
    stop music fadeout (1.5)
    mc "Entonces me parece perfecto."
    scene c32s001_445An with dissolve
    play music ("music/SexyLoungeMusic.ogg")
    "[ama] es una mujer práctica. Una vez decidido el 'cómo', solo queda por hacer el 'qué'."
    "La chica se empala en tu polla con un movimiento rápido. Ya ha dicho que no estaba asustada por el dolor."
    ama "*Jadeo* ¡Ufff! *Jadeo*"
    call BlinkXS4("c32s001_450") from _call_BlinkXS4_1956
    mc "Podías haberlo hecho más lentamente..."
    ama "*Jadeo* Y tú podías habérmelo dicho antes."
    mc "¿No lo has hablado con [mar] o alguna de las otras chicas?"
    call BlinkXS4("c32s001_455") from _call_BlinkXS4_1957
    ama "¡No! ¡Eso hubiera sido vergonzoso!"
    mc "¿Por no saber o por querer saber?"
    call BlinkXS4("c32s001_460") from _call_BlinkXS4_1958
    ama "Por las dos cosas. Pero ahora ya sé lo que es."
    mc "¿Cómo...?"
    $ renpy.sound.play("music/AmaMoan.ogg", loop=True)
    scene c32s001_900pv with dissolve
    show c32s001_900v
    "Ya deberías estar acostumbrado a que no te dejen acabar las preguntas. No te acostumbrarás nunca."
    "[ama] empieza a saltar sobre tu polla con movimientos cortos, como si se estuviera acostumbrando al cuerpo extraño que hay dentro de ella."
    ama "*Jadeo* Respira, [ama]. *Jadeo*"
    "Para alguien entrenado para soportar el dolor, el reconocimiento que esas dos palabras muestran es algo muy íntimo."
    "Aún no sabes si [ama] será habladora durante el sexo o no. Ni siquiera ella lo sabe."
    scene c32s001_915pv with dissolve
    show c32s001_915v
    hide c32s001_900v
    "No puedes dejar de observar cómo ella se desliza hasta hacer desaparecer a Mjolnir dentro de su coño."
    ama "*Jadeo*"
    "En cada recorrido, de tan solo un par de pulgadas, sobre tu astil la espía intenta tensar sus músculos."
    ama "*Jadeo* Mejor..."
    "Esos músculos que nunca te cansarás de mirar están aprendiendo un movimiento nuevo."
    scene c32s001_910pv with dissolve
    show c32s001_910v
    hide c32s001_915v
    "Las expresiones que pasan por su rostro te hablan del inicio de un placer controlado, pero también de intentos de controlar el dolor."
    "Quizás la velocidad de sus saltitos no sea la adecuada para una chica que pierde su virginidad."
    ama "*Jadeo* Está empezando a pasarse..."
    "Aunque [ama] no es una chica normal. Es dura como los clavos."
    "Pero nunca en la historia de los clavos ha habido uno con unas tetas comparables a las de tu esposa."
    scene c32s001_905pv with dissolve
    show c32s001_905v
    hide c32s001_910v
    "Paso a paso, saltito a saltito, ella se va acomodando a tu cuerpo. Acostumbrándose a Mjolnir dentro de ella."
    ama "*Jadeo* Poco a poco... *Jadeo susurrante* Adiós... *Jadeo*"
    "¿Se está despidiendo de su virginidad?"
    "Empiezas a pensar que, quizás, deberías haberla ayudado a relajarse antes de empezar. Si te hubiera dado la oportunidad."
    ama "*Gemido*"
    "Su primer gemido hace que una corriente de alivio y alegría te recorra de arriba a abajo."
    scene c32s001_925pv with dissolve
    show c32s001_925v
    hide c32s001_905v
    "Tras el gemido, la chica cambia de postura dejando caer su peso sobre ti. Empiezas a mover tus caderas para acompañar sus movimientos."
    ama "*Gemido* Ahora sí..."
    "Sigue habiendo dolor en su cara, pero se alterna con expresiones de placer."
    ama "*Gemido* Ahora lo empiezo a entender todo... *Gemido*"
    "Su frase más larga va acompañada de gemidos mientras embistes su coño. Esperas que lo que está empezando a entender sea cómo controlar su cuerpo."
    scene c32s001_930pv with dissolve
    show c32s001_930v
    hide c32s001_925v
    "Siguen siendo movimientos cortos, de alguna manera tiernos, tal y como había pedido ella antes de empezar."
    ama "*Gemido* Estoy empezando a notar cómo se acerca un orgasmo... *Gemido*"
    "El cuerpo de la chica también te lo dice a ti. Una vez ha encontrado la postura idónea, reacciona tensándose."
    ama "*Gemido* Pero es demasiado pronto... *Gemido*"
    "Estás a punto de reírte. Nunca es demasiado pronto para un orgasmo."
    "A menos que seas un hombre, claro."
    call OrgasmXS4("c32s001_465") from _call_OrgasmXS4_62
    ama "*GEMIDO* ¡NOOO! *GEMIDO*"
    "Su cuerpo se tensa con el vigor de unos músculos dignos de una culturista. Su coño se cierra con fuerza sobre tu polla."
    "No sabes a qué viene esa negación en medio del orgasmo, pero te alegras de que ella por fin lo haya alcanzado."
    call BlinkXS4("c32s001_470") from _call_BlinkXS4_1959
    ama "*GEMIDO* Lo siento... *GEMIDO*"
    "De pronto entiendes la negación."
    mc "Que hayas llegado al orgasmo no significa que esto haya acabado, cielo."
    scene c32s001_920pv with dissolve
    show c32s001_920v
    hide c32s001_930v
    "Empiezas a bombear con tus caderas para demostrarle lo equivocada que está."
    ama "*GEMIDO* ¡SÍ! *GEMIDO*"
    "Y el cuerpo de tu esposa vuelve a tensarse. Placer, descubrimiento y alegría se mezclan en sus movimientos y en sus expresiones."
    ama "*GEMIDO* ¡SIGUE! *GEMIDO*"
    "Una cita inolvidable continúa con una comunión entre dos cuerpos igual de inolvidable."
    scene c32s001_935pv with dissolve
    show c32s001_935v
    hide c32s001_920v
    "Con el Caribe como único testigo de vuestra unión, sigues bombeando sin apartar tu mirada del hermoso rostro de la chica."
    ama "*GEMIDO* ¡VIENE OTRO! *GEMIDO*"
    "Y el tuyo también se está acercando a marchas forzadas. Parece que vais a tener vuestro primer orgasmo simultáneo en vuestra primera vez."
    mc "Yo también estoy a punto."
    "Ella no deja de cabalgarte. Tú no dejas de bombear."
    ama "*GEMIDO* Hazlo dentro. *GEMIDO*"
    if persistent.walkthrough:
        $ wt1 = _("Sin consecuencias.")
        $ wt2 = _("[ama] embarazada.")
    else:
        $ wt1 = ""
        $ wt2 = ""
    if persistent.pregnancy:
        menu:
            "Correrte dentro. Ir a por el bebé." (wt=wt2):
                $ ama._var("pregnant", True)
                $ ama._var("undiscoveredPregnancy", True)
                play sound ("music/OldMusicBox5.ogg")
            "Correrte dentro." (wt = wt1):
                pass
    call DoubleOrgasmXS3("c32s001_470a") from _call_DoubleOrgasmXS3_3
    hide c32s001_935v
    ama "*GEMIDO* ¡SÍ! *GEMIDO* ¡POR FIN! *GEMIDO*"
    mc "¡Mpfft!"
    "La explosión casi simultánea, sin que ninguno de los dos sepa el orgasmo de quién ha provocado el del otro, sucede de golpe."
    "Llenas por primera vez el coño de tu esposa hasta que no puede retener todo tu semen."
    call BlinkXS4("c32s001_475") from _call_BlinkXS4_1960
    ama "*GEMIDO* ¡Está más caliente de lo que esperaba! *GEMIDO*"
    "Puedes notar cómo oleadas de placer recorren su túnel del amor mientras se cierra con fuerza sobre tu astil."
    "Lo que empezó con jadeos para controlar el dolor, ha acabado siendo un festival de gemidos."
    stop sound fadeout (1.5)
    "No ha habido ni un jadeo más después del primer gemido."
    stop music fadeout (1.5)
    scene c32s001_480a with fade
    call BlinkXS4("c32s001_480") from _call_BlinkXS4_1961
    "Unos minutos después..."
    play music ("music/AmbientPianoStrings.ogg")
    ama "Ha sido... diferente... de cómo me lo imaginaba."
    mc "¿En qué ha sido diferente?"
    call BlinkXS4("c32s001_485") from _call_BlinkXS4_1962
    ama "Diana nunca quiso hablar de ello. Sólo dijo que lo odiaba."
    ama "Clarice nos explicó cosas, pero su experiencia y esto no se parecen en nada."
    if eva._var("route"):
        ama "Y [eva] sólo me dijo que fue increíble, pero que no quería que mis expectativas se dispararan."
    mc "Es lógico. ¿Y cómo ha sido para ti?"
    call BlinkXS4("c32s001_490") from _call_BlinkXS4_1963
    ama "Al principio ha sido... duro. No me podía concentrar."
    ama "Era como si me pasara la vida por delante de los ojos. Pensaba en las chicas de casa, en mis hermanas..."
    ama "Pensaba en qué se les pasaría por la cabeza si pudieran verme en ese momento."
    mc "Supongo que se alegrarían de que hubieras dado un paso tan importante."
    call BlinkXS4("c32s001_495") from _call_BlinkXS4_1964
    ama "Yo también he pensado lo mismo. Por un momento, las he visto a todas sonriéndome, despidiéndose. Después han desaparecido."
    "Parece que, al fin y al cabo, no se despedía de su virginidad."
    ama "A partir de entonces, ha sido lo más alucinante que he experimentado en mi vida."
    call BlinkXS4("c32s001_500a") from _call_BlinkXS4_1965
    ama "¿No crees que estoy loca?"
    mc "Supongo que sí que lo estás. O para ser más exacto, espero que lo estés. Loca por mí."
    call BlinkXS4("c32s001_500b") from _call_BlinkXS4_1966
    ama "*Risa* ¿Alguna vez lo has dudado?"
    mc "Nunca."
    scene c32s001_500d with dissolve
    "La besas para demostrarle que nunca ha habido dudas por tu parte."
    "Tampoco ha habido prisas."
    "Dicen que lo bueno se hace esperar. Y la espera ha valido la pena."
    call BlinkXS4("c32s001_505") from _call_BlinkXS4_1967
    ama "¿Me perdonas por haberte hecho esperar tanto?"
    mc "No hay nada que perdonar, cielo. Tus dudas eran razonables. No querías odiarlo ni convertirte en una adicta."
    call BlinkXS4("c32s001_510") from _call_BlinkXS4_1968
    ama "*Risa* Te aseguro que no lo odio. ¿Sobre convertirme en una adicta...? Cuando se pase el dolor te daré mi respuesta."
    mc "¿Duele mucho?"
    call BlinkXS4("c32s001_515") from _call_BlinkXS4_1969
    ama "Menos de lo que me imaginaba, pero más de lo que esperaba."
    mc "Solo es la primera vez. El dolor no está ahí en las siguientes."
    call BlinkXS4("c32s001_520") from _call_BlinkXS4_1970
    ama "Es algo que descubriré otro día."
    call BlinkXS4("c32s001_500b") from _call_BlinkXS4_1971
    ama "*Risa* ¡No me mires como un cachorrito desconsolado! ¡No va a haber segundo asalto!"
    mc "*Risa* ¡No te miraba como un cachorrito!"
    call BlinkXS4("c32s001_525") from _call_BlinkXS4_1972
    ama "*Risa* ¡Sí que lo hacías! ¡Has puesto la misma cara que Zeus cuando se acaba el atún!"
    mc "*Risa* ¡No invoques al Rompedor de Camas!"
    scene c32s001_530An with dissolve
    mc "Si aparece, tendrá que dormir encima de estos músculos."
    mc "Me sentiría ridículo si le tuviera que decir a [car] que un gato ha roto la cama."
    ama "*Risa* Suenas ridículo cada vez que lo dices. La cama la rompimos entre todos."
    mc "Lo sé. Pero consigo que te rías cada vez que lo digo."
    call BlinkXS4("c32s001_535") from _call_BlinkXS4_1973
    ama "Gracias, [mc]."
    mc "¿Por hacerte reír?"
    ama "Especialmente por eso. Pero también por conseguir hacer lo que necesitamos en cada circunstancia."
    ama "¿Puedo contarte algo y me prometes que no te enfadarás?"
    mc "No puedo prometértelo, pero me sería muy difícil enfadarme contigo."
    call BlinkXS4("c32s001_540") from _call_BlinkXS4_1974
    ama "Al principio, cuando llegaste, no me caías bien. No entendía qué habían visto [sca] o [eil] en ti."
    ama "O qué veía [sai], aunque a ella no la conocía. Solo leía los informes y veía los videos que llegaban de Portland."
    call BlinkXS4("c32s001_545") from _call_BlinkXS4_1975
    ama "Tenías un cuerpo agradable de mirar, pero nada más. Tu actitud hacia las chicas me parecía paternalista."
    ama "Y además parecía que estabas jugando con ellas a un juego de seducción que podía hacerles daño."
    ama "Llevaba un mes vigilándolas y me había encariñado con ellas."
    mc "¿Qué cambió?"
    call BlinkXS4("c32s001_550") from _call_BlinkXS4_1976
    ama "Los moretones."
    mc "*Risa* ¿Ya no tenía un cuerpo agradable de mirar?"
    call BlinkXS4("c32s001_555") from _call_BlinkXS4_1977
    ama "*Risa* Bueno, no. Daba bastante pena mirarte."
    ama "Pero eso hizo que viera el cómo los habías conseguido. "
    call BlinkXS4("c32s001_560") from _call_BlinkXS4_1978
    ama "Hay operativos que lucen sus cicatrices como medallas. Tú te ganaste las medallas defendiendo a [eri]. Y entonces empecé a ver más allá."
    ama "No estabas jugando un juego. Estabas intentando que cada una de las personas a tu alrededor se sintieran mejor con ellas mismas."
    call BlinkXS4("c32s001_565") from _call_BlinkXS4_1979
    ama "[mar], [nor], [eri], [sca], [eil], [dap], [sam]..."
    ama "Incluso lo hiciste con [emm], teniendo en cuenta que se comportó como una niña malcriada el día que llegaste o la noche que fuisteis al Twins."
    mc "Cuando quieres a alguien, lo quieres con sus virtudes y sus defectos."
    call BlinkXS4("c32s001_570") from _call_BlinkXS4_1980
    ama "Pero eso me hizo darme cuenta de que te había malinterpretado."
    ama "Y a partir de entonces..."
    mc "*Risa* Caíste rendida a mis pies, enamorada hasta las trancas."
    call BlinkXS4("c32s001_575") from _call_BlinkXS4_1981
    ama "*Risa* No, eso empezó cuando [erc] entró en casa de [nor]. Y cuando te enfrentaste a [kev]."
    mc "Te olvidas de cuando gané la segunda pelea con Jack. *Risa* ¡Quiero todas mis medallas!"
    call BlinkXS4("c32s001_580") from _call_BlinkXS4_1982
    ama "Esa no la vimos. Teníamos cámaras dentro del café, no fuera."
    ama "Pero [oma] y [eil] nos la han explicado."
    mc "Y tú me salvaste con [kev]. Y [eva] y tú con [sol]."
    call BlinkXS4("c32s001_585") from _call_BlinkXS4_1983
    ama "Alguien tiene que proteger al protector, ¿no?"
    mc "¿Y quién os protege a vosotras?"
    call BlinkXS4("c32s001_590") from _call_BlinkXS4_1984
    ama "Nos protegemos la una a la otra. Y ahora te tenemos a ti para que nos protejas a las dos. Y al resto de la familia."
    "El tono de la chica te dice que se siente aliviada de compartir esa tarea contigo."
    mc "También me tienes para esto."
    scene c32s001_500d with dissolve
    "La vuelves a besar. Es un beso que intenta decir que siempre te tendrá a su lado mientras quiera."
    call BlinkXS4("c32s001_595") from _call_BlinkXS4_1985
    ama "*Risa* Por mucho que me beses así, no va a haber segundo round."
    mc "*Risa* Te aseguro que no era lo que intentaba."
    ama "Además, deberíamos dormir. Mañana hay que volver al trabajo."
    mc "¿Quieres ir a por un camisón? ¿Me pongo algo para dormir?"
    scene c32s001_500d with dissolve
    "Esta vez es ella la que te besa. Y ese beso dice que no va a haber ropa entre vosotros durante la noche."
    scene c32s001_600a with dissolve
    "Dormís desnudos en los brazos del otro por primera vez. Caéis dormidos en seguida."
    "La sesión de buceo seguida de la sesión de sexo ha agotado vuestra energía."
    stop music fadeout (1.5)
    scene black with dissolve
    centered "{size=+20}{b}DÍA 42 – LUNES{/b}{/size}"
    scene c32s001_600b with dissolve
    play music ("music/OctoBlues.ogg")
    "El sol, saliendo por encima del Caribe, te despierta al amanecer."
    "[ama] no está a tu lado. No te has dado cuenta de cuándo se ha ido."
    scene c32s001_600c with fade
    "Te levantas para ir a buscarla, sin éxito."
    mc "¿[ama]?"
    ama "*Desde la terraza* Arriba, en la piscina infinita."
    "Has estado tan ocupado estos días que todavía no has usado la piscina con vistas al mar."
    scene c32s001_600d with fade
    "Estás seguro de que, en ningún momento en su historia, esa piscina ha tenido un aspecto tan espectacular como ahora mismo."
    mc "Buenos días, cielo."
    call BlinkXS4("c32s001_605") from _call_BlinkXS4_1986
    ama "Buenos días, [mc]. Me encanta ver el amanecer desde aquí."
    mc "Es muy bonito, pero... ¿no tengo un beso de buenos días?"
    call addProfileImageS3 (8, "ama_8", ama, __(": 15 - Especial"), "") from _call_addProfileImageS3_50
    call BlinkXS4("c32s001_610") from _call_BlinkXS4_1987
    ama "*Risa* Hay la misma distancia desde aquí hasta ahí que desde ahí hasta aquí."
    ama "Si quieres un beso, puedes venir a buscarlo."
    scene c32s001_610d with dissolve
    "Quieres ese beso. Y te da lo mismo quién tenga que recorrer la distancia."
    "Alguien podría pensar que te dejas dominar por las mujeres de tu vida."
    "A ese alguien no le estarían esperando los labios de [ama], con lo que su opinión no cuenta."
    scene c32s001_610e with dissolve
    "El beso es fantástico en un paraje bellísimo."
    "Casi sería una lástima que los dos tuvierais los ojos cerrados y no lo vierais."
    "Casi."
    call BlinkXS4("c32s001_615") from _call_BlinkXS4_1988
    mc "Buenos días, [ama]."
    ama "Buenos días, cielo."
    mc "¿Hace mucho que te has despertado?"
    call BlinkXS4("c32s001_620") from _call_BlinkXS4_1989
    ama "Unos 40 minutos. Por norma duermes hasta más tarde y he venido aquí a ver amanecer."
    mc "Bueno, que hayas venido nos ha brindado una oportunidad de cerrar el círculo."
    mc "Empezamos la cita con un beso durante la puesta de sol y la acabamos con uno al amanecer."
    call BlinkXS4("c32s001_625") from _call_BlinkXS4_1990
    ama "¿Quién te ha dicho que la cita ha acabado?"
    mc "*Risa* ¿A qué te refieres?"
    scene c32s001_625d with dissolve
    ama "*Risita* A que mi marido se ha levantado con una erección matutina."
    ama "No puedo dejarle que vaya a trabajar así. Tengo que ser una buena esposa."
    call BlinkXS4("c32s001_630") from _call_BlinkXS4_1991
    ama "Que no pudiera con un segundo round anoche, no significa que no pueda por la mañana."
    ama "Si mi marido ha recuperado la suficiente energía, claro..."
    mc "*Risa* Tu marido ha recuperado la energía en el momento en que te ha visto."
    call BlinkXS4("c32s001_635") from _call_BlinkXS4_1992
    ama "¿Entonces a qué esperas para hacerme el amor al amanecer?"
    mc "Espero a estar en un sitio más cómodo. Propongo los escalones o una de las tumbonas de la terraza."
    scene c32s001_635d with dissolve
    ama "Empecemos por los escalones. Quiero hacerlo dentro del agua. Quiero saber qué se siente."
    mc "Me parece una idea perfecta."
    scene c32s001_635e with dissolve
    "La preciosa rubia se sienta en el último escalón, encarada hacia el sol naciente, y empieza a besarte."
    scene c32s001_635f with dissolve
    "La altura es perfecta para que Mjolnir apunte directamente a la entrada de su vagina."
    "Ella presiona con sus piernas contra tu culo, como si estuviera pidiéndote que no demores más el momento que está esperando."
    scene c32s001_640An with dissolve
    "Y no demoras el momento un segundo más de lo necesario."
    $ renpy.sound.play("music/AmaMoan.ogg", loop=True)
    ama "*Gemido*"
    "Puedes notar la humedad de tu mujer al penetrarla, tan diferente de la humedad del agua."
    scene c32s001_945pv with dissolve
    show c32s001_945v
    "Ella también se ha estado poniendo cachonda desde el momento en que has aparecido, esperando este momento."
    ama "*Gemido* Es tan diferente a ayer..."
    "Supones que se refiere a la ausencia de dolor... o al sentimiento ingravidez que el agua provoca."
    "No vas a preguntarle ahora mismo. Habrá tiempo para ello más tarde."
    ama "*Gemido* Puedo entender por qué la gente nunca tiene suficiente de esto..."
    scene c32s001_940pv with dissolve
    show c32s001_940v
    hide c32s001_945v
    "Tú también puedes. Los músculos de la rubia mercenaria se cierran con fuerza sobre tu astil, mientras la luz del sol naciente empieza a calentar tu espalda."
    "No te importa no estar viéndolo. Habrá más oportunidades para ver amanecer."
    "Pero sólo habrá una primera vez bajo la luz del alba con [ama]."
    ama "*Gemido* Es increíble..."
    "Lo que es increíble es que, después del dolor que experimentó ayer, haya querido repetir tan pronto."
    scene c32s001_955pv with dissolve
    show c32s001_955v
    hide c32s001_940v
    "Por suerte, la lubricación de la chica, la ingravidez que el agua proporciona, y tu ritmo lento, hacen que la experiencia sea menos dolorosa."
    ama "*Gemido* Me encanta cuando eres tan tierno..."
    "Sus músculos se vuelven a cerrar con fuerza sobre tu astil. Puedes notar cómo cada pliegue de su túnel del amor roza sobre tu polla."
    ama "*Gemido* Y estás tocando todos mis puntos correctos..."
    "Y ella colabora con ello, tensando y relajando sus músculos al ritmo de tus embestidas."
    scene c32s001_950pv with dissolve
    show c32s001_950v
    hide c32s001_955v
    "Tal como el sol va iluminando la belleza del entorno en el que está la casa del CEO, lo va volviendo más hermoso."
    ama "*Gemido* Más rápido..."
    "Con la resistencia del agua entre vuestros cuerpos y el resbaladizo suelo, es casi imposible que aceleres en esa posición."
    ama "*Gemido* Más salvaje..."
    "Tu mujer te sorprende. Ayer tan solo quería que fuera tierno."
    call BlinkXS4("c32s001_645") from _call_BlinkXS4_1993
    ama "*Gemido* Cambiemos de posición."
    mc "¿No te está gustando tanto como ayer?"
    ama "*Gemido* Sí, pero aquí no vas a poder acelerar. Y quiero probar cómo es tu propuesta de ayer de hacerlo más salvaje."
    mc "Como quieras. ¿Tumbonas o suelo?"
    ama "Borde de la piscina."
    call BlinkXS4("c32s001_650") from _call_BlinkXS4_1994
    "Tras salir de la piscina, adopta una posición sorprendente que te va a obligar a estar con el agua hasta las rodillas."
    ama "Así. Y no tardes mucho..."
    mc "¿No me dejas disfrutar de las vistas durante un segundo?"
    ama "*Risa* El segundo ya ha pasado."
    scene c32s001_655An with dissolve
    "Te acercas por detrás y la penetras en un rápido movimiento. Los 30 segundos que Mjolnir ha estado fuera de ella se han hecho eternos."
    ama "*GEMIDO*"
    "No, no has contado los segundos. Estabas demasiado ocupado mirando la belleza que está empalada en tu polla."
    ama "*GEMIDO* Puedes empezar a moverte cuando quieras."
    scene c32s001_990pv with dissolve
    show c32s001_990v
    hide c32s001_950v
    "Si quería sexo más rápido que antes, ahora no pierdes la oportunidad de hacerlo."
    "El sexo tierno es tu favorito, pero algo más salvaje, de vez en cuando, también es de tu agrado."
    ama "*GEMIDO* ¡Así! *GEMIDO*"
    "Con menos agua alrededor de tus piernas, es mucho más fácil acelerar el movimiento de tus caderas."
    "Y la posición elegida por [ama] hace que parezca sexo más duro de lo que realmente es."
    scene c32s001_980pv with dissolve
    show c32s001_980v
    hide c32s001_990v
    "A la chica también parece gustarle, ya que sus gemidos son más altos y más frecuentes."
    ama "*GEMIDO* ¡Es alucinante! *GEMIDO*"
    "No te importaría prolongar el inicio de la mañana un rato más, o incluso que os tomarais el día libre."
    "Pero sabes que [ama], siempre tan profesional, no querrá hacerlo, con lo que tenéis que sacarle todo el partido a este fugaz encuentro."
    ama "*GEMIDO* ¡SIGUE! *GEMIDO*"
    scene c32s001_985pv with dissolve
    show c32s001_985v
    hide c32s001_980v
    "Las increíbles vistas, y no me refiero al paisaje, solo son superadas por las sensaciones que su coño produce sobre tu polla."
    "Las rápidas embestidas hacen que la punta de Mjolnir roce en toda la longitud de sus paredes vaginales."
    ama "*GEMIDO* ¡VOY A CORRERME! *GEMIDO*"
    "Unas paredes vaginales que se van cerrando con fuerza sobre esa misma punta, incrementando las maravillosas sensaciones."
    "Todos los músculos de la chica se tensan a la vez, anunciando el inminente orgasmo."
    call OrgasmXS4("c32s001_655") from _call_OrgasmXS4_63
    ama "*GEMIDO* ¡SÍ! *JADEO* ¡ME ENCANTA! *GEMIDO*"
    "Cuando la tensión se libera, el cuerpo de la chica se comporta como un terremoto, con oleadas de músculos tensándose y relajándose."
    "A ti no te queda mucho combustible en el depósito, pero el suficiente como para poder bombear un rato más para prolongar su orgasmo mientras el tuyo se acerca."
    scene c32s001_995pv with dissolve
    show c32s001_995v
    hide c32s001_985v
    "Sigues embistiendo mientras el sol sigue subiendo sobre el horizonte."
    "Tu orgasmo y el amanecer son como dos fuerzas imparables de la naturaleza."
    ama "*GEMIDO*"
    "Las oleadas de orgasmos están dejando a tu esposa sin capacidad de articular frases completas."
    "Y tus caderas siguen embistiendo."
    call BlinkXS4("c32s001_660") from _call_BlinkXS4_1995
    ama "*GEMIDO* ¿Podemos volver a cambiar? *GEMIDO*"
    "No puedes verle la cara, pero su tono te dice que sabe que no es el mejor momento."
    ama "*GEMIDO* Quiero probar por detrás... *GEMIDO*"
    if persistent.walkthrough:
        $ wt1 = _("Sexo anal activado con [ama].")
        $ wt2 = _("Sexo anal desactivado con [ama].")
    else:
        $ wt1 = ""
        $ wt2 = ""
    menu:
        "¡Estupendo!" (wt=wt1):
            $ ama._var("anal", True)
            call c32s001_AmaAnal from _call_c32s001_AmaAnal
        "¡Tarde!" (wt = wt2):
            $ ama._var("anal", False)
            if persistent.pregnancy and not ama._var("pregnant"):
                if persistent.walkthrough:
                    $ wt1 = _("[ama] embarazada.")
                    $ wt2 = _("Sin consecuencias.")
                else:
                    $ wt1 = ""
                    $ wt2 = ""
                menu:
                    "Correrte dentro. Ir a por el bebé." (wt = wt1):
                        $ ama._var("pregnant", True)
                        $ ama._var("undiscoveredPregnancy", True)
                        play sound ("music/OldMusicBox5.ogg")
                    "Correrte dentro." (wt = wt2):
                        pass
            call OrgasmXS4("c32s001_665") from _call_OrgasmXS4_64
            hide c32s001_995v
            mc "¡Mpfft!"
            "Su sorprendente petición llega demasiado tarde, cuando tu orgasmo está llegando y te es imposible de parar."
            ama "*GEMIDO* ¡ESO TAMBIÉN ME VALE! *GEMIDO*"
            stop sound fadeout (1.5)
            "Descargas una ingente cantidad de semen dentro de tu esposa, llenándola hasta que empieza a salir, recorriendo tu astil."
    scene c32s001_705a with fade
    call BlinkXS4("c32s001_705") from _call_BlinkXS4_1996
    stop music fadeout (1.5)
    if ama._var("anal"):
        "Un rato después, cuando vuestras respiraciones se han normalizado, cogéis unas toallas para secaros el sudor..."
    else:
        "Un rato después, cuando vuestras respiraciones se han normalizado, cogéis unas toallas para secaros..."
    play music ("music/Memories-Instrumental.ogg")
    mc "¿Cómo estás?"
    ama "Menos dolorida que anoche, pero cansada. Ha sido muy intenso."
    mc "Como tu jefe puedo darte el día de fiesta si lo quieres."
    call BlinkXS4("c32s001_710") from _call_BlinkXS4_1997
    ama "*Risa* Estoy segura de que, si me cogiera el día de fiesta, tú también te quedarías en casa."
    ama "Y entonces no íbamos a descansar ninguno de los dos."
    mc "¿Tú también te has quedado con ganas de más asaltos?"
    call BlinkXS4("c32s001_715") from _call_BlinkXS4_1998
    ama "No voy a contestar a esa pregunta trampa."
    ama "Si digo que no parecerá que no me ha gustado. Si digo que sí, encontrarás alguna excusa para que nos quedemos en casa."
    mc "Todo el mundo tiene derecho a algún día de fiesta, ¿no?"
    mc "Si hemos dicho que ya no hay esclavos en NTR, no deberíamos esclavizarnos nosotros."
    call BlinkXS4("c32s001_720") from _call_BlinkXS4_1999
    ama "¿Serás tú quien le diga mañana a [car] que no hemos ido a trabajar por quedarnos follando?"
    mc "*Risa* Vale. Me acabas de convencer para ir a trabajar."
    call BlinkXS4("c32s001_725") from _call_BlinkXS4_2000
    ama "Pero antes de irnos..."
    scene c32s001_725d with dissolve
    "Esta vez, eres tú quién no le dejas acabar la frase."
    "Tus labios sellan los suyos como punto final a la maravillosa cita que empezó anoche."
    scene c32s001_725e with fade
    "Bueno... Punto final... Más bien punto y seguido..."
    "Quizás ducharos juntos no es la mejor idea si queríais ser puntuales en la llegada a la base..."
    scene c32s001_725f with fade
    "O vestiros en la misma habitación..."
    "Es difícil vestirse mientras tu polla está en su boca..."
    scene c32s001_725g with fade
    "O en cualquier parte dentro de ella..."
    "Pero ser el jefe tiene ciertas ventajas. Y esperas que [lar] no le diga a [car] que has llegado tarde."
    stop music fadeout (1.5)
    "Al menos, por una vez, has conseguido que [ama] se deje los tacones puestos."
    return
label c32s001_AmaAnal:
    scene c32s001_670a with fade
    call BlinkXS4("c32s001_670") from _call_BlinkXS4_2001
    "La chica se levanta, se desempala, y coge una toalla para secarse."
    ama "*Gemido* Vamos a las tumbonas antes de que Mjolnir empiece a... encoger."
    mc "No te preocupes. No va a encoger."
    ama "*Gemido* Esa postura me estaba matando..."
    scene c32s001_675a with fade
    call BlinkXS4("c32s001_675") from _call_BlinkXS4_2002
    "Te tumbas en una de las tumbonas mientras parece que [ama] se pregunta por un par de segundos cómo quiere posicionarse."
    mc "Como tú quieras."
    ama "Tan rápido como antes."
    scene c32s001_680a with fade
    call BlinkXS4("c32s001_680") from _call_BlinkXS4_2003
    "La posición escogida por tu esposa no es la que tú hubieras elegido, pero parece la adecuada después de una cadena de orgasmos."
    "Te va a dejar todo el trabajo a ti, permitiendo un descanso a las piernas de [ama] después de la anterior postura."
    ama "Cuando tú quieras."
    scene c32s001_685An with dissolve
    "Sin lubricante a mano, intentas ser lo más cuidadoso posible al penetrar su culo."
    ama "*JADEO* ¡JODER! *JADEO* ¡UFFF! *JADEO*"
    "Pese a que intenta relajar su esfínter, no puedes evitar que sienta un dolor intenso."
    call BlinkXS4("c32s001_690") from _call_BlinkXS4_2004
    mc "¿Estás segura de que quieres que sea tan rápido como antes?"
    ama "*JADEO* Segurísima. *GEMIDO* Ha sido más sorpresa que dolor. *JADEO*"
    "La presencia de los jadeos hace que pongas en duda esa afirmación. Al menos un poco."
    scene c32s001_970pv with dissolve
    show c32s001_970v
    hide c32s001_995v
    "Pero no es el momento de discutir sobre eso. Tienes que recuperar la excitación perdida durante el cambio de posición."
    "Empiezas a bombear mientras deslizas a la rubia mercenaria por tu polla."
    ama "*GEMIDO* ¡Justo así! *GEMIDO*"
    "Sorprendentemente, el dolor parece que pasa rápidamente. O al menos el placer lo sobrepasa."
    "Alguien podría decir que no hay mejor lubricante que la excitación o la curiosidad. Probablemente se equivocarían."
    scene c32s001_960pv with dissolve
    show c32s001_960v
    hide c32s001_970v
    "Sigues moviendo a la chica sobre tu polla como si de un juguete se tratara."
    "Con todos esos músculos, cualquiera podría pensar que debería pesar más. Aunque nadie se atrevería a decírselo a la cara."
    ama "*GEMIDO* ¡SÍ! *GEMIDO*"
    "Su posición, con las piernas cerradas, hace que el estrecho agujero sea más estrecho aún."
    "Lo que a su vez provoca que tu placer sea mayor, y el de la chica se vaya incrementando con cada embestida."
    scene c32s001_965pv with dissolve
    show c32s001_965v
    hide c32s001_960v
    "Sin ningún control por su parte, ni superficies en las que apoyarse excepto tu polla, tu pecho y tus muslos, tu esposa se bambolea con cada embestida."
    ama "*GEMIDO* ¡PAREZCO UN JUGUETE EN TUS MANOS! *GEMIDO* ¡ME ENCANTA! *GEMIDO*"
    "La dura mercenaria disfrutando mientras entrega el control es otro recuerdo que atesorarás para siempre."
    ama "*GEMIDO* ¡ESTOY A PUNTO DE CORRERME OTRA VEZ! *GEMIDO*"
    "Y su facilidad para llegar al orgasmo no será algo que olvides nunca."
    call OrgasmXS4("c32s001_695") from _call_OrgasmXS4_65
    ama "*GEMIDO* ¡SÍ! *GEMIDO* ¡ES SUPER INTENSO! *GEMIDO*"
    "Su esfínter se cierra con fuerza sobre tu polla, como un anillo de acero que hace que cada embestida a partir de entonces sea más difícil."
    "Más placentera."
    scene c32s001_975pv with dissolve
    show c32s001_975v
    hide c32s001_965v
    "Haciendo que tu orgasmo se acerque a pasos agigantados."
    ama "*GEMIDO* ¡CÓRRETE DENTRO! *GEMIDO* ¡QUIERO NOTAR TU SEMEN DENTRO DE MÍ! *GEMIDO*"
    "Ella puede notar cómo tu orgasmo se va acercando y empieza a dirigir tus movimientos."
    "La entrega de control tan solo ha sido momentánea y aparente."
    ama "*GEMIDO* ¡PUEDO NOTAR CÓMO TE TENSAS! *GEMIDO*"
    call OrgasmXS4("c32s001_700") from _call_OrgasmXS4_66
    mc "¡Mpfft!"
    "Y la tensión llega a su límite justo antes de que explotes en una catarata de semen dentro del culo de [ama]."
    ama "*GEMIDO* ¡MADRE MÍA! *GEMIDO* ¡ESTÁ MUY CALIENTE! *GEMIDO*"
    stop sound fadeout (1.5)
    "Cuando la explosión llega a su fin, parte de tu semen empieza a gotear por tu astil, saliéndose de un ano incapaz de retenerlo todo."
    return
label c32s002_trainingCamp:
    scene black with dissolve
    centered "{size=+20}{b}DÍA 43 – MARTES{/b}{/size}"
    scene c31s007_305e with dissolve
    play sound ("music/knock.ogg")
    "*Knock-Knock*"
    mc "Pasa, [ama]."
    play music ("music/On-The-Rise.ogg")
    scene c32s002_200a with fade
    call BlinkXS4("c32s002_200") from _call_BlinkXS4_2005
    mc "¿Necesitas volver a salir de aquí?"
    ama "No. TÚ necesitas salir de aquí."
    ama "Le he preguntado a [car], y tienes la agenda despejada durante toda la mañana."
    mc "¿Dónde vamos?"
    call BlinkXS4("c32s002_205") from _call_BlinkXS4_2006
    ama "Querías ver el campo de entrenamiento, ¿no?"
    ama "Ahora está casi vacío, con lo que es un buen momento."
    mc "¿Casi vacío? No tenemos demasiadas misiones en marcha."
    call BlinkXS4("c32s002_210") from _call_BlinkXS4_2007
    ama "*Risa* Es posible que le haya dicho a [aar] que mande a los chicos de maniobras hasta la tarde."
    mc "*Risa* ¿No quieres que me junte con tipos duros?"
    call BlinkXS4("c32s002_215") from _call_BlinkXS4_2008
    ama "No quiero que te juntes con NIÑOS duros. Aún no están preparados para conocerte."
    mc "¿Todavía entrenamos a los niños?"
    ama "Sí. Aún no has decidido qué hacer con ellos y [aar] no quiere que estén ociosos y perdiendo el tiempo."
    mc "Decidir qué hacer con ellos se acaba de convertir en una de mis principales prioridades. Yo creía que..."
    call BlinkXS4("c32s002_220") from _call_BlinkXS4_2009
    ama "¿Creías que [aar] iba a tomar esa decisión por ti? No puede hacerlo."
    ama "Es una orden que tiene que salir de este despacho. Sólo la puedes tomar tú."
    mc "¿Nos reunimos mañana y hablamos de eso? También tenemos que hablar del resto de peticiones que hicieron los operativos."
    mc "Pero quiero a los chicos más jóvenes lejos de las armas lo antes posible."
    call BlinkXS4("c32s002_225") from _call_BlinkXS4_2010
    ama "Creo que es una buena idea. Hay que buscar algo que hacer con ellos."
    ama "El problema lo tendrás con quien quiera ser operativo de campo. ¿Qué vas a hacer si uno de ellos quiere seguir entrenando con armas?"
    mc "Creo que ese es un puente que deberemos cruzar cuando se den las circunstancias."
    mc "Pero me parece que voy a tener que actuar como si fueran chicos normales. Hay una edad para el colegio y una edad para tomar decisiones."
    call BlinkXS4("c32s002_230") from _call_BlinkXS4_2011
    ama "*Risa* ¿Te das cuenta de que acabas de usar la palabra 'normales' para dejar a nuestros chicos fuera de ella?"
    mc "No me había dado cuenta. Y no me parece gracioso."
    ama "Lo que me parece gracioso a mí es que hace unos días querías echarle la bronca a [alb] por lo mismo."
    mc "Tienes razón. A veces el lenguaje nos juega malas pasadas porque estamos acostumbrados a usarlo de una forma concreta."
    mc "Pero nunca me oirás usar 'humanos' para dejar a los clones fuera de esa palabra. O al menos eso espero."
    call BlinkXS4("c32s002_235") from _call_BlinkXS4_2012
    ama "Yo también lo espero. Y ahora vístete. Los tejanos no son un buen atuendo para el campo de entrenamiento."
    mc "¿Me vas a poner a correr alrededor de los muros?"
    call BlinkXS4("c32s002_240") from _call_BlinkXS4_2013
    ama "¿Ya sabes lo de los muros? ¿[aar] te ha llevado allí?"
    mc "No, pero he consultado planos. Y me he quedado impresionado."
    mc "Los muros parecen lo suficientemente extensos como para que no sea agradable correr alrededor con este calor."
    call BlinkXS4("c32s002_245") from _call_BlinkXS4_2014
    ama "Entonces será mejor que te vistas rápido. O tendré que ponerte a correr."
    mc "¡A sus órdenes, mi comandante!"
    stop music fadeout (1.5)
    scene c32s002_250d with fade
    "Esta vez, [ama] conduce el mismo destartalado Humvee por una carretera normal."
    "Supones que los camiones de transporte necesitan asfalto por el que circular."
    scene c32s002_250e with fade
    play music ("music/SadSummer.ogg")
    "Tras pocos minutos, llegáis a la base principal. Es grande, pero no tanto como creías."
    "Los planos parecen haberte engañado. Aquí no cabe una pista de aterrizaje."
    "La base está vacía, excepto por unos cuantos guardias en las torres de vigilancia."
    call BlinkXS4("c32s002_255") from _call_BlinkXS4_2015
    mc "Creía que sería más grande."
    ama "Seguramente los planos que consultaste están desactualizados."
    ama "Esto se construyó hace un par de años, para imitar un puesto avanzado estadounidense en Jordania."
    ama "Excepto por el desierto, claro."
    mc "Entonces, ¿la pista de aterrizaje y los hangares...?"
    call BlinkXS4("c32s002_260") from _call_BlinkXS4_2016
    ama "Están más allá del muro norte. Un par de aviones de transporte, tres de entrenamiento, y un par más de helicópteros están allí."
    ama "Los veremos cuando acabe de enseñarte esto."
    ama "Y no, no tenemos aviones de combate por la misma razón por la que no tenemos tanques."
    ama "Lo más parecido que verás es esa belleza negra de ahí."
    mc "¿Eso es un helicóptero de ataque?"
    call BlinkXS4("c32s002_265") from _call_BlinkXS4_2017
    ama "Ahora más bien es un helicóptero de apoyo a tierra. Es un AH-60L."
    ama "Este lo... robaron unos D en Riohacha. Tiene ametralladoras y cohetes, pero no misiles Hellfire. Otra vez, no tenemos y no los necesitamos."
    mc "*Jadeo de sorpresa* ¿Robamos equipo a nuestros clientes?"
    call BlinkXS4("c32s002_270") from _call_BlinkXS4_2018
    ama "Robo o pago en especie. Como prefieras llamarlo."
    ama "No es política oficial de la empresa, pero si se niegan a pagar... No arriesgamos la vida por nada."
    "Te das cuenta de que, pese a todo, esa frase demuestra una lealtad a la empresa difícil de entender en el mundo fuera de NTR."
    call BlinkXS4("c32s002_275") from _call_BlinkXS4_2019
    ama "No ha habido más problemas con los pagos de Colombia."
    ama "La pérdida de ese helicóptero les dolió más a ellos del beneficio que nos aporta a nosotros."
    mc "¿Por qué?"
    call BlinkXS4("c32s002_280") from _call_BlinkXS4_2020
    ama "Tenemos una capacidad de despliegue limitada. No nos lo podemos llevar a una misión a Camboya, por ejemplo."
    ama "Bueno, podríamos, pero el gobierno americano no estaría muy contento si lo hiciéramos. Demasiado cerca de China, por si lo perdemos."
    ama "Y no tenemos la infraestructura para sacarle todo el partido posible. Recambios, armamento, etc."
    ama "Pero nos sirve para entrenar, por si necesitamos volar en uno algún día."
    mc "O si necesitamos robar otro."
    call BlinkXS4("c32s002_285") from _call_BlinkXS4_2021
    ama "*Risa* Exacto. La próxima vez, intentaremos no matar a ningún soldado en el proceso."
    "Lo casual de la frase, dicha entre risas, te hiela la sangre en las venas."
    ama "*Risa* Pero no aseguramos nada. Paga para asegurarte de que no necesitamos hacerlo."
    stop music fadeout (1.5)
    "No habías caído en la cuenta de que, para robar un helicóptero, los D tuvieron que matar a soldados colombianos."
    scene c32s002_290a with hpunch
    call BlinkXS4("c32s002_290") from _call_BlinkXS4_2022
    play music ("music/Sad-Piano.ogg")
    ama "¡Oh! ¡Mierda!"
    ama "¿He dicho eso riéndome?"
    mc "Me temo que sí..."
    call BlinkXS4("c32s002_295") from _call_BlinkXS4_2023
    ama "Ahora mismo me siento inhumana..."
    if persistent.family:
        ama "Tanto como nos ven los que consideran que los clones no somos personas..."
    ama "Esos soldados tendrían madres y familia que los echarán de menos..."
    mc "Sí..."
    $ dec = Character("Declan", color="#ffcc80")
    call BlinkXS4("c32s002_300") from _call_BlinkXS4_2024
    ama "Todos celebramos cuando Dax y [dec] trajeron ese helicóptero."
    ama "Colombia nos había intentado robar y nosotros les habíamos robado a ellos."
    ama "Nadie pensó en los 14 soldados que mataron entre los dos para llevarse el pájaro. A nadie le importaba."
    mc "No sabíais lo que era una familia más allá de estos muros. Era vosotros contra el resto del mundo."
    mc "Tú ahora lo sabes. Y entiendes lo que es la pérdida, o lo que sentirían [mar], [nor] o [emm] si no volvieras a casa de una misión."
    call BlinkXS4("c32s002_305") from _call_BlinkXS4_2025
    ama "En [mar] es en la primera que he pensado."
    ama "Y me he sentido avergonzada por lo que ella pensaría si me oyera decir eso..."
    mc "Estás cambiando, [ama]. Y eso es bueno. Pero es un proceso. No esperes ser una persona diferente de hoy para mañana."
    scene c32s002_305d with hpunch
    ama "Es... tan difícil."
    mc "No es difícil, [ama]. Es algo que requiere aprendizaje."
    mc "Mientras tú aprendías a disparar bazookas y a hablar 30 idiomas, nosotros aprendíamos a vivir en familia, a sentir empatía."
    mc "En menos de un mes has hecho un curso intensivo sobre familia y empatía, pero..."
    call BlinkXS4("c32s002_310") from _call_BlinkXS4_2026
    ama "Pero aún hablo el idioma de la empatía con un acento extraño, ¿no?"
    mc "Me gusta la analogía. Sí, es exactamente eso. Y de vez en cuando se te escapa una palabra en tu idioma nativo."
    mc "Pero eso se arregla con la práctica."
    scene c32s002_310d with fade
    "En ese momento, oís cómo se abren las puertas de la copia del puesto avanzado."
    stop music fadeout (1.5)
    "Un camión de transporte de tropas hace su aparición."
    call BlinkXS4("c32s002_315") from _call_BlinkXS4_2027
    play music ("music/OneLastChance.ogg")
    mc "Creía que íbamos a estar solos..."
    ama "Yo también. Nadie tenía que volver en dos horas más, al menos."
    scene c32s002_315d with fade
    mc "Hola, [dam]... Espera, tú no eres [dam]."
    $ cl1 = Character(_("Clon 1"), color="#afcc80")
    $ cl2 = Character(_("Clon 2"), color="#facc80")
    $ cl3 = Character(_("Clon 3"), color="#0fcc80")
    $ cl4 = Character(_("Todos los clones"), color="#00cc80")
    dec "Hola, Señor. Soy [dec]. ¿Cómo lo ha sabido?"
    scene c32s002_315e with dissolve
    dam "Porque soy inconfundible, [dec]. Creo que no me cansaré de decirlo."
    call BlinkXS4("c32s002_320") from _call_BlinkXS4_2028
    dam "Hey, [ama] y [mc]."
    mc "Hola, [dam]. Tenía entendido que estaríais de maniobras todo el día."
    dam "Uno de los chicos se ha hecho daño."
    scene c32s002_320d with dissolve
    dam "Llevad a Henry a la enfermería mientras yo hablo con el... jefe."
    "Los 'chicos' que han bajado del camión podrían tener tu edad. Se han quedado mirando tu interacción con [dam] y [dec]."
    dec "No te preocupes, Dam. Ya les acompaño yo."
    dec "Chicos, dejad de mirar embobados y seguidme."
    scene c32s002_325a with fade
    call BlinkXS4("c32s002_325") from _call_BlinkXS4_2029
    mc "¿El chico está bien?"
    dam "Sí, una torcedura de tobillo. Los H son pequeños pero duros. Estará andando en un par de horas."
    dam "Hemos avisado a la base y Doc ha dicho que estará aquí en cinco o seis minutos."
    "Algunos de los H y un G, crees que es [gid], se han refugiado a la sombra de una tienda. Observándoos."
    scene c32s002_325d with dissolve
    "Ni [dam] ni [ama] se molestan en presentártelos. Susurran con poco disimulo."
    cl1 "*Susurrando* ¿Cómo se atreve a vestirse como uno de nosotros? ¿Se va a poner a entrenar?"
    cl2 "*Susurrando* [gav] y [fred] dicen que es diferente, pero hasta que no lo vea..."
    call BlinkXS4("c32s002_330") from _call_BlinkXS4_2030
    mc "¿No hay médico en el puesto avanzado?"
    dam "[carl] actúa como enfermero. Los C son buenos con las cosas técnicas y él ya no puede combatir."
    mc "¿Sólo tenéis un enfermero?"
    gid "*Susurrando* Yo lo vi en la sala de espera mientras lo operaban..."
    cl1 "*Susurrando* Seguro que lo único que le importaba era si la operación salía bien y podía vender el brazo."
    cl2 "*Susurrando* A mí me dijeron que se quedó hasta el último momento. Incluso cuando la operación ya había acabado."
    cl3 "*Susurrando* Yo también lo vi. Y no era la cara de preocupación de alguien que piensa cuánto dinero puede sacar."
    call BlinkXS4("c32s002_335") from _call_BlinkXS4_2031
    ama "No es una zona de combate, sino de entrenamiento. Seguramente [carl] no ve a más de un chico al día."
    ama "Y Doc posiblemente no tenga que venir más de una vez al mes."
    cl1 "*Susurrando* Seguro que quiere ahorrar la gasolina que usa Doc cuando viene."
    cl3 "*Susurrando* ¿No lo has oído? Lo primero que ha hecho es preguntar por Henry."
    cl2 "*Susurrando* Parecía preocupado..."
    scene c32s002_335d with dissolve
    dam "Chicos, ¿queréis ver cómo se desenvuelve el jefe en el viejo campo de tiro?"
    mc "*Susurrando* ¿Qué haces?"
    cl2 "¡Sí!"
    cl1 "Si viste así, que se gane el derecho a hacerlo."
    cl3 "No es necesario, pero me gustaría ver de qué pasta está hecho."
    dam "Creo que voy a darles una paliza a él y a [ama]."
    scene c32s002_340d with dissolve
    ama "*Susurrando* [dam], ¿qué estás haciendo? No está preparado."
    call BlinkXS4("c32s002_340") from _call_BlinkXS4_2032
    ama "No es necesario que lo hagas, [mc]. Creo que [dam] quiere dejarte en ridículo."
    ama "Y a mí de paso también."
    mc "Lo voy a hacer, [ama]. No voy a fingir que soy alguien diferente de quién soy."
    call KissXS4("c32s002_345") from _call_KissXS4_33
    dam "Vamos al viejo campo de tiro. Señoritas, suban al camión."
    scene c32s002_350a with fade
    "[dam] conduce durante unos minutos hasta llegar al campo de tiro."
    "El viaje en la parte trasera del camión es incómodo. Aparte de los tres H, sólo está [gid], el G al que conociste en la sala de espera."
    "Ninguno os dirige la palabra a [ama] o a ti. [ama] está sumida en un silencio extraño."
    "Ella seguramente está preguntándose que vehículo va a usar para atropellar a [dam]. Y arrepintiéndose de no tener un tanque."
    scene c32s002_350b with fade
    "Al llegar al campo de tiro, los clones se quedan a vuestra espalda, excepto [dam]..."
    dam "Vamos a ponerlo fácil. 10 disparos, de pie, a 25 metros y sumamos puntuaciones."
    ama "*Susurrando* Nunca ha disparado a 25 metros, [dam]."
    scene c32s002_350c with dissolve
    dam "Si se quiere vestir como nosotros, tiene que demostrar que es uno de nosotros. ¿Verdad, chicos?"
    scene c32s002_350d with dissolve
    cl4 "*Gritando* ¡Sí!"
    scene c32s002_350e with dissolve
    dam "Que sea el original del viejo [aar] no va a eximirle de tener que enseñarnos lo bueno que es."
    dam "Hank, trae mi pistola del camión y algunos cargadores."
    scene c32s002_350f with dissolve
    cl2 "¿Qué?"
    cl1 "¿Tú lo sabías?"
    gid "Yo los vi juntos el domingo... [dam] tiene razón."
    cl3 "Os dije que era diferente..."
    scene c32s002_350g with fade
    dam "Las damas primero."
    ama "*Susurrando* Sigo sin entender qué quieres conseguir, capullo."
    dam "Mueve ese culo hasta la posición de tiro y demuéstranos que no te has oxidado con la vida cómoda en Newport."
    dam "Aquí tienes mi arma."
    scene c32s002_350h with fade
    dam "*Risa* ¿Veis, chicos? Hay que ser delicados cuando se le da algo a una dama."
    call KissXS4("c32s002_355") from _call_KissXS4_34
    play sound ("music/Desert-Eagle-Gunshot.ogg")
    "*Bang*"
    "Ver a [ama] disparar sin esfuerzo aparente eso como ver a un leopardo persiguiendo a una gacela."
    "Concentrada, haciendo un arte de la economía de movimientos."
    if ama._var("route"):
        "Preciosa y mortífera a la vez."
    else:
        "Mortífera."
    call BlinkXS4("c32s002_360") from _call_BlinkXS4_2033
    ama "Hecho. Hank, ve a contar las puntuaciones. Por favor."
    $ cl1 = Character("Hank", color="#afcc80")
    $ cl2 = Character("Heinrich", color="#facc80")
    $ cl3 = Character("Hugo", color="#0fcc80")
    cl1 "Sí, Señora."
    scene c32s002_365a with fade
    "[cl1] vuelve al cabo de un minuto. Ha ido y ha vuelto corriendo. Ni siquiera ha empezado a sudar bajo el sol veraniego del Caribe."
    "Tú estás empapado en sudor. En parte por el calor, en parte por el nerviosismo de lo que está pasando."
    cl1 "97.5 puntos, [ama]. Dos de los disparos ha dado en el 9 y otro en la línea entre el 9 y el 10. El resto en el 10."
    ama "Gracias, Hank."
    dam "*Risa* ¿Estás desentrenada? Dame el arma."
    scene c32s002_365b with dissolve
    "[ama] descarga el arma y se la entrega a [dam]. Estás seguro de que ese cañón tiene que estar muy caliente."
    dam "Veo que te enseñamos bien. Seguridad ante todo."
    ama "*Susurrando* Sabes que quedan 7 balas en ese cargador, ¿verdad? No me hagas decir por dónde te las quiero meter ahora mismo."
    mc "[ama]..."
    scene c32s002_365c with dissolve
    "Ambos te ignoran. [dam] vuelve a comprobar que la recámara está vacía antes de sacar un nuevo cargador."
    scene c32s002_365d with dissolve
    dam "Tu turno, jefe..."
    "Hace el gesto de darte el arma en 'modo damisela' como ha dicho antes. No crees que sea la forma más segura de darle un arma a nadie."
    dam "*Susurrando* Voy a dejar caer la pistola. No la cojas."
    mc "*Susurrando* ¿Qué?"
    scene c32s002_370An with dissolve
    "Sin dejarte reaccionar, [dam] deja caer el arma descargada de forma disimulada."
    "No entiendes nada de lo que está pasando."
    scene c32s002_370e with dissolve
    dam "Lo siento, jefe. Culpa mía. La he soltado antes de que la hubieras cogido. Pensaba que tendrías más reflejos."
    mc "¿Gracias?"
    "No entiendes a qué juega el mercenario."
    scene c32s002_370f with dissolve
    dam "Tu turno, {b}jefe{/b}. Recuerda que las balas salen por el agujero de delante."
    dam "*Susurrando* Haz muy desviado el primer disparo."
    dam "Y así es cómo se le entrega un arma a una {b}damisela con experiencia{/b}, chicos."
    dam "No lo intentéis con novatos. Ya veis lo que puede pasar."
    scene c32s002_375a with dissolve
    "Te sitúas en la posición que te enseñó [eva], pero esta vez decides usar las dos manos."
    "No se trata sólo de impresionar a una chica, sino a rudos mercenarios. Aunque la chica sea una ruda mercenaria."
    "Y sabes que no te vas a acercar a la puntuación de [ama]. Si consigues acertar al blanco a esta distancia, claro."
    "Una gota de sudor recorre tu nuca hasta juntarse con el mar de sudor que hay en tu espalda."
    "El blanco se ve lejísimos."
    call KissXS4("c32s002_375") from _call_KissXS4_35
    play sound ("music/Desert-Eagle-Gunshot.ogg")
    "*Bang*"
    "Intentas disparar bajo, tal y como [dam] te ha indicado. Obviamente, el blanco no se mueve."
    scene c32s002_375c with dissolve
    "Aparece una nube de polvo a la derecha del blanco, bastante arriba."
    scene c32s002_375b with dissolve
    dam "*Risa* ¿Eso es lo mejor que puedes hacer? Si algún día te enfrentas a un ejército de topos, a lo mejor les aciertas."
    cl1 "*Susurro risueño* Creo que desde que tenía siete años no he fallado tan estrepitosamente."
    cl2 "*Susurrando* No mientas. Por lo menos tenías ocho."
    cl3 "*Susurrando* Parece mentira que sea el original del viejo."
    gid "*Susurrando* A lo mejor no está acostumbrado al peso de la Glock..."
    scene c32s002_375a with dissolve
    "Esto debía ser lo que quería [dam]. Dejarte en ridículo delante del resto de los chicos."
    "Ajustas la puntería lo mejor que puedes. Con nueve balas no vas a poder llegar a la puntuación de [ama]."
    "Posiblemente no lo conseguirías con 90 balas."
    "Te concentras en el blanco, tal y como te enseñó [eva]."
    call KissXS4("c32s002_375") from _call_KissXS4_36
    play sound ("music/Desert-Eagle-Gunshot.ogg")
    "*Bang*"
    "Haces los nueve disparos en rápida sucesión, ajustando levemente la posición entre disparos."
    "Jurarías que la nube de polvo se ha levantado por detrás de la diana en cada uno de ellos, pero estabas demasiado concentrado para estar seguro."
    scene c32s002_380a with fade
    call BlinkXS4("c32s002_380") from _call_BlinkXS4_2034
    "Descargas el arma y se la entregas a [dam], mirándole directamente a los ojos desafiante."
    "Sabes que ha ganado, sea cual sea el juego al que está jugando."
    mc "Hecho."
    dam "*Risa* Ten cuidado, no se te vaya a caer la pistola."
    "Sin retirar la mirada de los ojos del mercenario..."
    mc "[gid], ¿puedes ir a comprobar, por favor?"
    scene c32s002_380d with fade
    "Un minuto después..."
    gid "48.5, Señor. Menos de la mitad que [ama]."
    "En cualquier otra circunstancia te sentirías orgulloso de ti mismo. Pero aún no entiendes a qué está jugando [dam]."
    "[ama] te mira con incredulidad y orgullo."
    call BlinkXS4("c32s002_385a") from _call_BlinkXS4_2035
    dam "No está mal para un novato. Y menos aún teniendo en cuenta que has desperdiciado la primera bala."
    dam "*Susurrando* No contestes."
    dam "Ahora te voy a enseñar lo que hace un hombre de verdad."
    "Sigues su consejo y no respondes a su provocación. Crees que empiezas a ver su juego."
    scene c32s002_390b with fade
    dam "Atentos, chicos. Mirad cómo se hace."
    call BlinkXS4("c32s002_385b") from _call_BlinkXS4_2036
    ama "*Susurrando* Me dan ganas de matarlo ahora mismo. ¿Dónde hay un Bradley cuando una lo necesita?"
    mc "*Susurrando* Aún no estoy seguro, pero creo que hay más de lo que estamos viendo."
    ama "*Susurrando* [dam] es bastante simple. No creo que haya pensado nada complicado."
    mc "*Susurrando* Dale el beneficio de la duda..."
    scene c32s002_390a with dissolve
    "[dam] se pone en posición de disparo con una mano."
    "Está claro que se está exhibiendo delante de los otros clones."
    call KissXS4("c32s002_390") from _call_KissXS4_37
    play sound ("music/Desert-Eagle-Gunshot.ogg")
    "*Bang*"
    "Dispara la primera bala."
    scene c32s002_390e with dissolve
    "La nube de polvo se levanta lejos del blanco, en una posición parecida a la de tu primer disparo."
    "Ahora entiendes su juego perfectamente."
    call KissXS4("c32s002_390") from _call_KissXS4_38
    play sound ("music/Desert-Eagle-Gunshot.ogg")
    "*Bang*"
    "Dispara por segunda vez."
    scene c32s002_390e with dissolve
    "La nube se levanta exactamente en el mismo sitio."
    call KissXS4("c32s002_390") from _call_KissXS4_39
    play sound ("music/Desert-Eagle-Gunshot.ogg")
    "*Bang*"
    "Dispara por tercera vez."
    scene c32s002_390c with dissolve
    "Esta vez, la nube de polvo se levanta detrás del blanco."
    call BlinkXS4("c32s002_395") from _call_BlinkXS4_2037
    dam "[cl2], dame tu pistola. Me parece que la mira de la mía se ha torcido cuando se ha caído."
    dam "Tengo que corregir el disparo hacia abajo y a la izquierda."
    scene c32s002_390a with dissolve
    "Tras cambiar de pistola, vuelve a la posición de disparo."
    call KissXS4("c32s002_390") from _call_KissXS4_40
    play sound ("music/Desert-Eagle-Gunshot.ogg")
    "*Bang*"
    "Realiza siete disparos uno detrás de otro."
    call BlinkXS4("c32s002_400") from _call_BlinkXS4_2038
    dam "Ahora sí. Tendré que revisar mi pistola al volver al puesto avanzado."
    dam "[cl3], ve a mirar las puntuaciones. Con sólo 8 disparos buenos, no puedo haber alcanzado a [ama]."
    scene c32s002_400d with fade
    "Al cabo de un par de minutos..."
    cl3 "62 puntos, [dam]. Uno de los tres primeros disparos ha dado en el objetivo, pero... en el uno. Debe haber sido el tercer disparo."
    cl3 "Del resto, un diez, tres nueves y tres ochos."
    call BlinkXS4("c32s002_405") from _call_BlinkXS4_2039
    dam "[cl2], me quedo tu arma. Parece que está un poco desviada también. Le echaré un vistazo."
    dam "No he ganado a [ama], pero está claro que estoy varios niveles por encima del... {b}jefe{/b}."
    call BlinkXS4("c32s002_410") from _call_BlinkXS4_2040
    gid "No seas injusto, [dam]. Con tu pistola averiada, él ha hecho... más de cinco puntos por disparo una vez lo corrigió."
    gid "Y solo necesitó un disparo para corregir. Tú has usado dos y has sacado un miserable uno al tercero."
    call BlinkXS4("c32s002_415") from _call_BlinkXS4_2041
    dam "Creo que te voy a poner a correr cuando volvamos al puesto avanzado. Pero tienes {b}algo{/b} de razón."
    dam "Por suerte, su función no es combatir, sino tomar decisiones."
    call BlinkXS4("c32s002_420") from _call_BlinkXS4_2042
    dam "Volvemos a la base, chicos. Creo que el jefe se ha ganado el derecho de ir delante conmigo."
    dam "Vosotros vais detrás como damiselas. Y nada de armar follón. La damisela más mortífera de la base os estará vigilando."
    stop music fadeout (1.5)
    scene c32s002_425a with fade
    call BlinkXS4("c32s002_425") from _call_BlinkXS4_2043
    "En el camión..."
    play music ("music/SneakySnitch.ogg")
    mc "*Susurrando* ¿Por qué, [dam]?"
    dam "¿Por qué, qué?"
    mc "*Susurrando* ¿Por qué has hecho el paripé con la pistola cayéndose?"
    call BlinkXS4("c32s002_430") from _call_BlinkXS4_2044
    dam "No hace falta que susurres. Ahí detrás no se oye nada."
    dam "[ama] me dijo que [eva] te había dado clases y quería ver cómo de bueno eras."
    call BlinkXS4("c32s002_440a") from _call_BlinkXS4_2045
    dam "Sabía que alguien te iba a retar tarde o temprano. ¿Por qué no yo?"
    dam "Todo el mundo dice que los D somos unos fanfarrones, no demasiado listos, y tenemos problemas con la autoridad. Con lo que era una buena opción."
    call BlinkXS4("c32s002_435") from _call_BlinkXS4_2046
    dam "*Risa* Pero no podía dejarte en ridículo delante de los chicos."
    dam "Te hubieran perdido el respeto."
    mc "Pero sabías que no podría igualar a [ama]..."
    call BlinkXS4("c32s002_440b") from _call_BlinkXS4_2047
    dam "Ni tú, ni yo, ni nadie, excepto [eva]. Y las otras chicas, claro. Pero ya no están."
    dam "¿Sabes algo de baloncesto?"
    mc "Un poco..."
    call BlinkXS4("c32s002_445") from _call_BlinkXS4_2048
    dam "Tú serías un jugador de instituto. No serías la estrella de tu equipo, pero por lo que he visto hoy, serías bueno."
    dam "Si entrenaras muchísimo, podrías llegar a jugar en la NCAA."
    dam "Un soldado regular, sería un jugador correcto en la NCAA."
    dam "Los SEAL, los Boinas verdes, etc., serían jugadores de la NBA. Algunos titulares, otros suplentes."
    dam "La mayoría de los clones seríamos las estrellas de nuestros equipos en la NBA."
    call BlinkXS4("c32s002_450") from _call_BlinkXS4_2049
    dam "[ama] y [eva] son como si Kareem, Magic, Michael, Larry, Lebron, y Kobe hubieran tenido una noche de sexo loca y hubieran nacido ellas."
    mc "¿Tan buenas son? Sé que son buenas, pero..."
    call BlinkXS4("c32s002_455") from _call_BlinkXS4_2050
    dam "¿Buenas? Son lo mejor que hay en el mercado de la muerte."
    dam "Saben hacer de todo, y todo bien. Te aseguro que me he esforzado en los siete últimos disparos."
    dam "Soy bueno, y no he llegado a una media de 9. [ama] lo ha hecho casi perfecto."
    call BlinkXS4("c32s002_460") from _call_BlinkXS4_2051
    dam "Nivel de tirador olímpico. Pero ella podría hacer lo mismo con un rifle, con un cuchillo, o con un lanzagranadas. Un tirador olímpico no."
    dam "Tampoco podría pilotar un avión o un helicóptero como [eva] o diseñar un puesto de defensa improvisado como [ama]."
    dam "Aunque con un lanzagranadas seguramente les ganaría yo. A ellas dos y al tirador olímpico."
    mc "*Risa* Y tendríamos que cambiar los blancos después de cada disparo."
    call BlinkXS4("c32s002_465") from _call_BlinkXS4_2052
    dam "*Risa* Me gusta tu sentido del humor. Creo que es la primera vez que te oigo reír."
    mc "Pero aún no me has dicho por qué. Lo de que querías ver lo bueno que era no me lo creo."
    mc "Podías haberme pedido ir los dos juntos y... examinarme."
    call BlinkXS4("c32s002_470a") from _call_BlinkXS4_2053
    dam "No lo entiendes. Ya te he dicho que alguien tenía que retarte tarde o temprano."
    dam "Desde que tuvimos la reunión y te vimos junto a [aar], sabemos de quién es el clon el viejo. Y los chicos hablan de eso."
    dam "El viejo era muy bueno en el campo de ahí atrás."
    call BlinkXS4("c32s002_470b") from _call_BlinkXS4_2054
    dam "Además, estuviste en la operación de [gav]. Alguien te vio marcharte de la sala de espera el último."
    dam "Estuviste más de 20 minutos ahí solo."
    mc "Quería hablar con [bet], la cirujana. No sólo porque sea mi tía y quisiera saber cómo estaba."
    mc "Quería saber detalles sobre [gav]. No sólo un 'Todo ha salido según lo esperado.'"
    dam "A eso me refiero."
    call BlinkXS4("c32s002_475") from _call_BlinkXS4_2055
    dam "Y, además, te has dado cuenta de que [dec] no era yo. ¿Cómo lo has hecho? Solo me viste una hora en una reunión."
    mc "No lo sé. Sabía que no eras tú un segundo después de pronunciar tu nombre."
    dam "¿Y eso es importante para ti?"
    mc "Por supuesto que lo es. He dicho que no sois esclavos. Sois tan personas como yo, y tenéis que mantener vuestra individualidad."
    mc "Y yo tengo que ser el primero que os trate como individuos."
    call BlinkXS4("c32s002_480") from _call_BlinkXS4_2056
    dam "¿Sabes cómo me llamaba Daniels después de más de 15 años de verme casi todos los días?"
    mc "No..."
    call BlinkXS4("c32s002_485") from _call_BlinkXS4_2057
    dam "*Fingiendo un acento despectivo* 'Eh, tú. Ese D de ahí.'"
    mc "No soy Daniels."
    call BlinkXS4("c32s002_490") from _call_BlinkXS4_2058
    dam "Lo sé. Lo demostraste el otro día en la reunión y lo has demostrado hoy. Por eso quiero ayudarte."
    dam "Daniels hubiera venido con traje y no hubiera aceptado el reto del campo de tiro."
    dam "Y él no hubiera sabido que [dec] no era yo."
    mc "*Risa* Bueno, [dec] no me ha pedido un Ferrarini."
    call BlinkXS4("c32s002_495") from _call_BlinkXS4_2059
    dam "*Risa* Te he dicho que me gustaba tu sentido del humor. Creo que me voy a arrepentir de haberlo dicho."
    dam "Pero a lo que iba. Eres diferente a Daniels, aunque nunca serás uno de los nuestros."
    call BlinkXS4("c32s002_500a") from _call_BlinkXS4_2060
    dam "Pero llevas los genes de [aar] y te intentas integrar con nosotros. Nos escuchas y demuestras que te preocupamos."
    dam "Esos chicos de ahí detrás dirán que casi me has dado una paliza en el campo de tiro con una pistola defectuosa."
    call BlinkXS4("c32s002_500b") from _call_BlinkXS4_2061
    dam "Aunque te haya ganado con mis siete balas contra tus nueve. Pero van a exagerar y, en unos días, alguien dirá que hiciste 70 puntos."
    dam "Al menos nadie es tan tonto como para decir que le has ganado a [ama]. Eso no se lo creería nadie."
    mc "Podían haberse dado cuenta de tu trampa."
    call BlinkXS4("c32s002_500c") from _call_BlinkXS4_2062
    dam "Los G, excepto [gav] y Grant, no son muy listos. Sabía que [gid] estaba predispuesto a apoyarte porque te vio en la sala de espera."
    dam "Los H son un poco más listos, pero en el momento en que [gid] ha caído en la trampa, ellos le han seguido."
    call BlinkXS4("c32s002_500d") from _call_BlinkXS4_2063
    dam "El equipo se jode todos los días y los chicos lo saben. Es más fácil pensar en eso que en que yo te estoy ayudando."
    dam "No vas a tener que demostrarle nada a nadie más."
    mc "Sí. Voy a tener que demostrar que todo lo que has dicho es cierto. Y pienso hacerlo."
    call BlinkXS4("c32s002_505") from _call_BlinkXS4_2064
    dam "*Risa* Más te vale hacerlo. Recuerda que yo soy el de los lanzagranadas y los cañones."
    mc "*Risa* Si me atacas con eso, no te daré el Ferrarini."
    call BlinkXS4("c32s002_510") from _call_BlinkXS4_2065
    dam "¿Qué? ¿Me vas a conceder el Ferrarini?"
    mc "*Risa* Nope."
    call BlinkXS4("c32s002_515") from _call_BlinkXS4_2066
    dam "*Gruñido* Odio tu sentido del humor."
    stop music fadeout (1.5)
    return
label c32s002_choices:
    scene black with dissolve
    centered "{size=+20}{b}DÍA 44 – MIÉRCOLES{/b}{/size}"
    scene c32s002_005a with fade
    mcp "(Mañana hará una semana que llegué a Aruba.)"
    mcp "(Hay muchísimas cosas que hacer, pero tengo que ir paso a paso.)"
    scene c31s007_305e with dissolve
    play sound ("music/knock.ogg")
    "*Knock-Knock*"
    play music ("music/UnforeseenMotive.ogg")
    mc "Pasa, [ama]."
    call BlinkXS4("c32s002_010") from _call_BlinkXS4_2067
    ama "Sabes que das grima cuando haces eso, ¿verdad?"
    mc "¿Hacer qué?"
    ama "Saber quién está llamando a la puerta por cómo suenan sus nudillos en la madera."
    mc "Es lógico. Tú eres suave, aunque no tanto como [car]. [vin] es tímido. [flo] y [mael] son decididos, pero de una forma distinta."
    mc "Y [aar] no llama nunca a la puerta."
    mc "No me visita nadie más, excepto [geo], de informática. Y puedo oír su voz desde aquí cuando le pregunta a [car] si estoy."
    call BlinkXS4("c32s002_015") from _call_BlinkXS4_2068
    ama "Tienes cara de estar sobrepasado. ¿Ha pasado algo?"
    mc "[vin] y sus diminutas manos se acaban de ir. Esta mañana me ha enviado los tres informes que le pedí el otro día."
    call BlinkXS4("c32s002_020") from _call_BlinkXS4_2069
    ama "Eso es más eficiente de lo que esperaba... ¿Por qué estás así, entonces?"
    mc "Porque he estado mirando los números, y creo que no voy a poder cumplir con las expectativas que se crearon en la reunión con los operativos."
    mc "No hay dinero para hacerlo todo, y no van a estar contentos. Tengo que dejar fuera una de las promesas que hicimos."
    call BlinkXS4("c32s002_025") from _call_BlinkXS4_2070
    ama "Si te puedo ayudar... Explícame cómo está la situación."
    ama "Ya les diste el estilo personal y el poder salir de la base. Este fin de semana saldrán los primeros."
    mc "Pero quedan las prótesis, el salario, el salario retroactivo, las posibles rescisiones de contrato, las promociones internas, y los pasaportes."
    call BlinkXS4("c32s002_030") from _call_BlinkXS4_2071
    ama "Bueno, no creo que sepamos el coste de cada una de esas cosas."
    mc "¡Oh, sí! Sí que lo sabemos. Hay unas manos enanas que teclean muy rápido."
    if ama._var("route"):
        "Te está costando concentrarte con la nueva blusa que lleva [ama]. ¿Le han crecido las tetas en los últimos tres días?"
    call BlinkXS4("c32s002_035") from _call_BlinkXS4_2072
    ama "¿El tema de los pasaportes también?"
    mc "Sí. Hablé con [flo] para ver si se le ocurría algo, al tener contactos con gobiernos extranjeros."
    mc "Le pasó las cifras a [vin] de lo que nos va a costar... en sobornos."
    mc "Y sobre el resto, [vin] ha hecho una estimación. Y no llegamos a todo."
    mc "Si al menos supiera cómo iba a afectar la opinión de los operativos si incumplo cada una de las promesas..."
    call BlinkXS4("c32s002_040") from _call_BlinkXS4_2073
    ama "Creo que en eso te puedo ayudar. Al fin y al cabo, soy un operativo más... o lo era hasta hace unos meses."
    ama "Si tuviera que puntuar del uno al diez cuánta infelicidad crea cada promesa que dejes fuera..."
    call BlinkXS4("c32s002_045") from _call_BlinkXS4_2074
    ama "Las prótesis serían un 9 para los que la necesitan, pero un 1 para el resto."
    ama "Si vamos a dejar de hacer misiones peligrosas, van a pensar que no las necesitarán nunca."
    ama "Con lo que diría que un 3 en general."
    mc "Eso me sirve. No me lo había planteado así."
    mc "Pero me fastidiaría dejar a [cal] sin su prótesis. Ha trabajado mucho para la de [gav]."
    ama "Por eso no envidio tu trabajo. No son decisiones fáciles."
    call BlinkXS4("c32s002_050") from _call_BlinkXS4_2075
    mc "¿Y si dejamos fuera el salario?"
    ama "Seguramente se te tirarían al cuello. Un 10, desde luego. Para todos."
    ama "Además, esa iba ligada al salario retroactivo. ¿Qué vas a hacer con eso?"
    mc "No lo sé aún. No puedo darles las dos cosas sin dejar otra cosa fuera."
    mc "Había pensado que darles el salario podría ser una buena idea."
    mc "No solo sería lo justo, sino también sería una forma de decir 'A partir de ahora, las cosas cambian.'"
    call BlinkXS4("c32s002_055") from _call_BlinkXS4_2076
    ama "Es buena idea. Y puedes negarles el salario retroactivo diciendo que eso es un problema de la dirección anterior."
    ama "Eso crearía... unos 6 puntos de infelicidad."
    mc "No podemos hacer eso. Es la empresa quien se lo debe. Y ahora la empresa somos nosotros."
    mc "Había pensado que, si es lo que dejamos fuera, que sea de forma temporal."
    mc "En plan, no os vamos a dar un millón a cada uno de la serie A, más lo que sea a los C, más lo que les toque a los D..."
    call BlinkXS4("c32s002_060") from _call_BlinkXS4_2077
    ama "*Risa* Y no te olvides de [eva] y de mí..."
    mc "*Risa* No me olvido. Estáis en el informe de 'Dedos de Halfling'."
    mc "Me refiero a no pagarlo todo de golpe. Darlo como un complemento al salario hasta que saldemos las cuentas con cada uno de ellos."
    mc "Estoy seguro de que sé en qué se gastaría el dinero [dam] si lo recibiera todo a la vez."
    call BlinkXS4("c32s002_065") from _call_BlinkXS4_2078
    ama "Eso no es asunto nuestro. Pero creo que me gusta tu idea."
    ama "Cuando [eva] y yo recibimos el dinero de las acciones acudimos a [mar] y [nor] para que nos orientaran sobre cómo gastarlo."
    call BlinkXS4("c32s002_070") from _call_BlinkXS4_2079
    ama "Los chicos no van a tenerlas a ellas aquí para preguntarles."
    ama "Pero si ligas la recepción del complemento a... no sé... algún tipo de clases de economía doméstica..."
    ama "Creo que eso rebajaría la infelicidad de 6 a 2 puntos. Saben que lo recibirán, aunque no de golpe."
    mc "Me parece una buena idea."
    call BlinkXS4("c32s002_075") from _call_BlinkXS4_2080
    ama "Claro, que podrías no darles el salario y darles los atrasos."
    ama "*Risa* Casi apostaría que muchos dejarían la empresa y nos ahorraríamos sus sueldos."
    mc "*Risa* ¿Abandonarían la empresa antes o después de matarme?"
    mc "Has dicho que me saltarían al cuello, y enfadar a 400 tíos que están entrenados para matar no me parece buena idea."
    call BlinkXS4("c32s002_080") from _call_BlinkXS4_2081
    ama "*Risa* [aar] y yo te defenderíamos."
    mc "*Risa* Vosotros dos os quedaríais también sin cobrar."
    ama "*Risa* Entonces voy a rectificar. [car] te defendería."
    mc "*Risa* Entonces estoy a salvo, mientras no salga del despacho."
    mc "Nadie se atrevería a pasar por encima de ella."
    call BlinkXS4("c32s002_085") from _call_BlinkXS4_2082
    ama "Bueno, sigamos antes de que digamos demasiadas tonterías y [car] entre a ver qué nos pasa."
    ama "¿Cuál es la siguiente promesa?"
    mc "Las rescisiones de contrato. Lo de que os podáis ir cuando queráis de la empresa."
    call BlinkXS4("c32s002_090") from _call_BlinkXS4_2083
    ama "¡Uff! Creo que si tuviera que puntuar la infelicidad que provocaría eso... Un 5 en general."
    mc "¿Sólo un 5?"
    call BlinkXS4("c32s002_095") from _call_BlinkXS4_2084
    ama "Hay algunos que es difícil que vayan a querer irse nunca. [aar], los C, los D..."
    ama "Son muy... mayores... para empezar a buscarse la vida fuera de aquí. Y pasa lo mismo que con las prótesis. Para ellos sería un 1."
    ama "Para los más jóvenes, quizás se acerque al 10. Si se lo niegas, se seguirían sintiendo esclavos. He hecho la media."
    mc "Lo entiendo. Un 5 entonces."
    call BlinkXS4("c32s002_100") from _call_BlinkXS4_2085
    ama "Estamos avanzando. ¿Siguiente?"
    mc "Lo siguiente sería el sistema de promociones internas y opositar a puestos diferentes."
    mc "Yo creía que eso iba a ser barato, pero cuando se lo expliqué a [vin] dijo que no era tan fácil."
    mc "Debería haber un programa de formación para los diversos puestos. E hizo el presupuesto. ¡Le encanta hacer presupuestos!"
    mc "No se debería aceptar que tú pidas el puesto de contable, por ejemplo, si no tienes formación para ello."
    call BlinkXS4("c32s002_105") from _call_BlinkXS4_2086
    ama "Me jode estar de acuerdo con [vin]."
    ama "Si lo planteas como algo a largo plazo, con programas de formación, vas a hacer muy felices a los más jóvenes."
    mc "Eso si no es la idea que dejamos fuera..."
    call BlinkXS4("c32s002_110") from _call_BlinkXS4_2087
    ama "Exacto. Si la dejas fuera enfadaría a muchos. Un 7 diría yo. Y tendría ramificaciones."
    ama "Por ejemplo, para el equipo de Newport. En vez de elegir voluntarios deberíamos elegir a dedo."
    mc "Pero si hay voluntarios suficientes podríamos elegir entre ellos."
    call BlinkXS4("c32s002_115a") from _call_BlinkXS4_2088
    ama "Estarías mandando un mensaje ambiguo. 'Para proteger a mi familia sí, para el resto no.'"
    mc "No lo había pensado así, pero tienes razón. No lo miraba desde la psicología de los chicos."
    call BlinkXS4("c32s002_115b") from _call_BlinkXS4_2089
    ama "Aunque podrías implementar el sistema de promociones para las cosas que estén preparados, como seguridad."
    ama "Y dejar los puestos que necesiten formación para más adelante. Imagina alguien de la Serie P que quiera ser médico."
    ama "Ahora tienen cinco años, aunque sus cuerpos tengan ocho. Da tiempo a que se formen para lo que quieran ser."
    call BlinkXS4("c32s002_115c") from _call_BlinkXS4_2090
    ama "Si lo hacemos así, sería un... ¿posiblemente un 2?"
    ama "Habrá alguno que quiera ser director financiero mañana, pero el resto lo entenderán."
    mc "Me gusta esa idea."
    mc "Además, podemos unirlo con un programa de educación normal para los más pequeños. Ya te dije ayer que no los quiero cerca de las armas."
    call BlinkXS4("c32s002_115d") from _call_BlinkXS4_2091
    ama "Podemos crear algo parecido a una escuela rural con profesores propios."
    ama "No puedes mandar a 20 chicos de la serie Q al mismo colegio."
    mc "Lo sé. Ya tengo presupuesto para ello, cortesía de [vin]. Esa opción ya está aprobada en mi cabeza."
    mc "Y sólo queda la última. Pasaportes."
    call BlinkXS4("c32s002_120") from _call_BlinkXS4_2092
    ama "No tiene sentido que les dejes rescindir el contrato y que no les des pasaportes. Ni a la inversa."
    mc "Lo sé. Son dos elecciones que van ligadas entre ellas. La una sin la otra no serviría de nada."
    mc "Pero, ya que estamos ordenándolas por impopularidad, ¿cuántos puntos le darías a esto si lo dejáramos fuera?"
    call BlinkXS4("c32s002_125") from _call_BlinkXS4_2093
    ama "Es complicado. Condenarías a una vida de parias a quien quisiera abandonar la empresa."
    ama "Aunque sería una forma de que no quisieran irse."
    mc "Eso es juego sucio, [ama]. No quiero parecerme a Daniels ni a Richards en eso."
    call BlinkXS4("c32s002_130") from _call_BlinkXS4_2094
    ama "Lo sé, sólo pensaba en voz alta."
    ama "Creo que un 6."
    mc "¿Más que no dejarles rescindir sus contratos? No lo entiendo."
    call BlinkXS4("c32s002_135") from _call_BlinkXS4_2095
    ama "Si podemos abandonar la empresa y no vivir una vida normal, nos estarías jodiendo más que si no nos dejas irnos."
    ama "Además, algunos pensarían lo mismo que tú, que es juego sucio."
    mc "Vale. Un 6 entonces. Recapitulemos..."
    mc "Si dejamos fuera las prótesis, un 3. El salario un 10."
    mc "El salario retroactivo un 6, pero si lo aplicamos con complementos mensuales a largo plazo, un 2."
    mc "Las rescisiones de contrato un 5. Las promociones internas, si aseguramos un programa de formación, un 2. Y los pasaportes un 6."
    call BlinkXS4("c32s002_140") from _call_BlinkXS4_2096
    ama "Creo que está claro. Tienes que elegir entre el salario retroactivo y las promociones internas."
    ama "Son las dos cosas a más largo plazo. El coste sería distribuido en el tiempo y les daría algo por lo que quedarse en la empresa."
    mc "Tienes razón. No me gusta dejar fuera de la lista ninguna de las dos, pero son las mejores candidatas."
    call BlinkXS4("c32s002_145") from _call_BlinkXS4_2097
    ama "Pero hay una petición de la que no hemos hablado."
    mc "¿Cuál?"
    ama "[erc]."
    mc "Eso lo voy a cumplir. Dije que tendría una revisión justa y la tendrá."
    mc "La semana que viene tengo planeado hablar con él."
    call BlinkXS4("c32s002_150") from _call_BlinkXS4_2098
    ama "[eva] va a querer estar presente."
    mc "Lo sé, pero va a ser imposible retrasarlo hasta que llegue."
    mc "Había pensado que estuviera por video conferencia."
    mc "Y eso me ha dado una idea. Pero acabemos antes con la decisión que tenemos que dejar fuera."
    call BlinkXS4("c32s002_155") from _call_BlinkXS4_2099
    ama "La decisión que TIENES que dejar fuera. Yo sólo soy la jefa de seguridad. Eso es responsabilidad del CEO."
    mc "*Risa* Así me gusta. Sin presión. Como tú puedes defenderte de los clones..."
    mc "Según tu ránking de impopularidad, las dos decisiones serían igual de impopulares, pero mucho menos que las otras."
    menu:
        "Incumplir el salario retroactivo.":
            $ salary = True
        "Incumplir el sistema de promociones.":
            $ salary = False
    call BlinkXS4("c32s002_160") from _call_BlinkXS4_2100
    ama "Creo que has tomado una buena decisión."
    if salary:
        ama "Si les vas dando los salarios atrasados a lo largo de unos años van a estar contentos durante esos años."
        ama "Imagínate que [dam] pudiera comprarse tres Ferrarinis de golpe."
        ama "Seguramente después habría envidias entre los que todavía tienen el dinero y los que lo han malgastado."
        mc "Tu idea de los cursos de economía es lo que me ha hecho decantarme por esa opción."
        mc "Sabemos que, de esta forma, van a recibir su dinero igualmente, pero van a tener tiempo para aprender a administrarlo."
    else:
        ama "Si lo hubieras implementado y alguien hubiera pedido el puesto de [mael] sin tener los conocimientos..."
        mc "Hubiera tenido que rechazar la petición y parecería una promesa cumplida en falso."
        ama "Pero sin embargo, les dejas la puerta abierta para formarse para esos puestos. Y para optar a los que sí saben desempeñar."
        mc "Por eso me he decantado por esta opción. Creo que va a ser más seguro para todos y vamos a evitar decepciones."
    call BlinkXS4("c32s002_165") from _call_BlinkXS4_2101
    ama "¿Cuándo se lo vas a decir?"
    mc "Después de lo de [erc]."
    mc "[fred] me dijo ayer que estaban pensando en reducir aún más el comité y delegar las conversaciones conmigo en [carl]."
    mc "Creo que quieren evitar otra reunión en la que esté [dam]."
    call BlinkXS4("c32s002_170") from _call_BlinkXS4_2102
    ama "*Risa* No les culpo."
    mc "*Risa* Yo tampoco, te lo aseguro. Aún estoy decidiendo si tenías razón en el avión cuando dijiste que querría atropellar a [dam]."
    mc "Aunque después de lo de ayer en el campo de tiro..."
    call BlinkXS4("c32s002_175") from _call_BlinkXS4_2103
    ama "Pero bueno, vamos a lo importante."
    ama "Has dicho que has tenido una idea respecto a que [eva] asista por videoconferencia."
    mc "Sí. Y creo que puede ser una buena solución."
    stop music fadeout (1.5)
    return
label c32s003_EmmPickup:
    if _in_replay:
        call mrS3_emm_route from _call_mrS3_emm_route_47
    scene black with dissolve
    centered "{size=+20}{b}DÍA 46 – VIERNES{/b}{/size}"
    scene c32s003_005a with fade
    call BlinkXS4("c32s003_005") from _call_BlinkXS4_2104
    "Un par de días después..."
    play sound ("music/notification.ogg")
    "*Notificación en el móvil*"
    mc "Un momento, [bet]."
    bet "No te preocupes. A mí me llegan mensajes de las chicas a menudo también."
    scene c32s003_005d with hpunch
    play music ("music/WarIsComing.ogg")
    mc "¿QUÉ?"
    call BlinkXS4("c32s003_010") from _call_BlinkXS4_2105
    bet "¿Qué pasa, [mc]?"
    mc "¡Mira esto!"
    scene c32s003_010d with dissolve
    mc "¡Dice que acaba de salir del taller de pintura!"
    call BlinkXS4("c32s003_015") from _call_BlinkXS4_2106
    bet "*Risa* ¡Es horrible! Y no me refiero a [emm]..."
    mc "¡Me gustaba esa camioneta!"
    mc "Y además dice que es la venganza por no hacer una videoconferencia con ella todos los días."
    call BlinkXS4("c32s003_020") from _call_BlinkXS4_2107
    bet "¿Cuánto hace que no hablas con ella?"
    mc "Tres o cuatro días... creo. O a lo mejor son dos... A veces pierdo la cuenta."
    mc "Como mínimo he hablado dos veces con ella desde que llegamos. A lo mejor tres..."
    call BlinkXS4("c32s003_025") from _call_BlinkXS4_2108
    bet "¿Qué? Yo hablo con todas en dos días. Llamo a la mitad un día y a la otra mitad el siguiente."
    bet "Y hablo con [mee], [mar] y [nor] todos los días."
    mc "¿De dónde sacas tiempo? A veces las llamo entre reunión y reunión. O a la hora de comer..."
    call BlinkXS4("c32s003_030") from _call_BlinkXS4_2109
    bet "*Risa* Yo no tengo que dirigir una empresa, solo tengo que controlar a un paciente."
    mc "*Risa* ¿Quieres un puesto como mi asistente?"
    bet "*Risa* Seguramente [car] me mataría. Prefiero seguir viva hasta que encendamos el brazo de [gav]... Como mínimo."
    mc "Me parece una buena idea. Especialmente el 'como mínimo'."
    call BlinkXS4("c32s003_035") from _call_BlinkXS4_2110
    bet "Deberías llamarla antes de que decida pintar también tu habitación."
    mc "Tienes razón... Odiaría tener que mudarme al volver a casa si mi habitación fuera rosa."
    bet "Entonces te dejo. No le eches demasiado la bronca."
    scene c32s003_040a with fade
    call BlinkXS4("c32s003_040") from _call_BlinkXS4_2111
    mc "Buenos días, [emm]."
    "De alguna forma consigue aparecer en pantalla posando, claramente enfadada."
    emm "¿Tengo que mandarte esa foto para que me llames?"
    stop music fadeout (1.5)
    mc "He estado super ocupado aquí, te lo aseguro. Pero no hay ni un día que no piense en ti."
    call BlinkXS4("c32s003_045") from _call_BlinkXS4_2112
    play music ("music/Vacation-Vibe.ogg")
    emm "Yo también te echo de menos."
    mc "Pero... estás en tu habitación..."
    call BlinkXS4("c32s003_050") from _call_BlinkXS4_2113
    emm "Sí, ¿y?"
    mc "Me has dicho que acababas de salir del taller de pintura."
    call BlinkXS4("c32s003_055") from _call_BlinkXS4_2114
    emm "*Risa* ¿Y has tenido un ataque al corazón?"
    mc "*Risa* Casi. Me encantaba esa camioneta hasta hace diez minutos."
    call BlinkXS4("c32s003_060") from _call_BlinkXS4_2115
    emm "¿No te gusta lo que le he hecho?"
    mc "Según las palabras de Tía [bet], es horrible. Yo pienso lo mismo."
    call BlinkXS4("c32s003_065") from _call_BlinkXS4_2116
    emm "¡No tenéis ni idea de colores! ¡Así queda preciosa!"
    mc "Espero que la pintes de nuevo de negro antes de que yo vuelva."
    call BlinkXS4("c32s003_070") from _call_BlinkXS4_2117
    emm "¿Qué va a pasar si no lo hago? ¿Me tendré que quedar la camioneta para mí porque tú ya no la querrás?"
    emm "La verdad es que está muy bien tener coche propio. Aunque todas me están explotando como taxista."
    mc "*Risa* Bienvenida a mi mundo. La diferencia es que yo lo hacía a gusto."
    call BlinkXS4("c32s003_075") from _call_BlinkXS4_2118
    emm "Yo también. Es una oportunidad de pasar aún más tiempo con todas las chicas."
    mc "Me gusta que te lo tomes así, [emm]. No todas las obligaciones tienen que ser malas."
    mc "¿Va todo bien en casa?"
    call BlinkXS4("c32s003_080") from _call_BlinkXS4_2119
    emm "Todo va bien. No te preocupes. No hace ni diez días que te has ido. No vamos a incendiar la casa ni nada por el estilo."
    mc "*Risa* No me refería a eso. Las estudiantes nuevas llegan en menos de dos semanas y habrá cosas que hacer."
    call BlinkXS4("c32s003_085") from _call_BlinkXS4_2120
    emm "Bueno, sí. El domingo moveremos las cosas de [eil], [kia] y la abuela a la vieja casa de [kia]."
    emm "Y adivina quién tiene una camioneta y se va a pasar todo el domingo teniendo que hacer viajes entre nuestra casa y la suya."
    mc "¿[sol] ya se ha ido de la casa? Creía que intentaría alargarlo lo máximo posible..."
    call BlinkXS4("c32s003_090") from _call_BlinkXS4_2121
    emm "Sí, hace días que se fue. Pero ninguna de ellas quería irse hasta que no fuera necesario."
    emm "Yo tampoco. Me va a tocar ir a buscarlas cada día..."
    mc "*Risa* Como has dicho, es una oportunidad para pasar más tiempo con ellas."
    mc "Aunque seguro que [eil] preferirá ir a casa en bici a subirse en esa camioneta rosa."
    call BlinkXS4("c32s003_095") from _call_BlinkXS4_2122
    emm "¿Te cuento un secreto?"
    mc "Sí. Y espero que no sea que has convencido a [eil] para que se vista de rosa permanentemente."
    call BlinkXS4("c32s003_100") from _call_BlinkXS4_2123
    emm "*Risa* Aún no lo he intentado."
    emm "Pero me acabas de dar una idea. Si le doy el cambiazo a su ropa por ropa mía, no tendrá más remedio que vestirse de rosa."
    mc "Creo que preferiría ir desnuda por la calle. Odia el rosa casi tanto como yo."
    mc "Pero me ibas a contar un secreto."
    call BlinkXS4("c32s003_105") from _call_BlinkXS4_2124
    emm "Lo de la camioneta lo he hecho con PaintStore. A ver si así te tomabas la molestia de llamarme."
    mc "No es ninguna molestia, pero encontrar tiempo es difícil."
    mc "Aunque creo que me voy a olvidar de llamarte los próximos días por ser tan malvada conmigo."
    call BlinkXS4("c32s003_110") from _call_BlinkXS4_2125
    emm "*Risa* ¡No te atreverás!"
    mc "*Risa* Ponme a prueba."
    emm "*Risa* Si lo haces, pintaré la camioneta de verdad."
    mc "*Risa* Si lo haces, le diré a Mamá que te quite las llaves y se las de a [eri]."
    call BlinkXS4("c32s003_115") from _call_BlinkXS4_2126
    emm "*Risa* Vale. Nada de pintar la camioneta. [eri] la devolvería a su aburrido color negro."
    mc "[eri] tiene buen gusto."
    call BlinkXS4("c32s003_120") from _call_BlinkXS4_2127
    if emm._var("route"):
        emm "Yo también, me casé contigo."
    else:
        emm "Yo también, aunque tú no los compartas."
    mc "No voy a discutir sobre eso."
    mc "Por cierto, creía que habíamos quedado en que nada de mentiras, ¿no?"
    call BlinkXS4("c32s003_125") from _call_BlinkXS4_2128
    emm "*Risa* ¿En qué he mentido?"
    mc "Me has dicho que acababas de salir del taller de pintura. Sé que era una broma, pero..."
    emm "*Risa* Revisa el mensaje. Pone 'la tienda de pintura', no 'el taller de pintura'. Paint Store Pro."
    emm "Es la aplicación que he usado para cambiarle el color. Técnicamente no he mentido. Tú has entendido lo que has querido entender."
    mc "*Risa* ¡Creo que he creado un monstruo!"
    scene c32s003_125An with dissolve
    "Pasáis un rato charlando en el que te pone al día de todas las novedades en casa."
    "Excepto por la mudanza del domingo, ya lo sabías todo, pero te encanta oír hablar a tu hermana."
    if emm._var("route"):
        "Oír reír a tu esposa."
    "Pero una llamada de [car] para avisarte de que [aar] ha llegado para la reunión que tenéis pendiente interrumpe vuestra conversación."
    call BlinkXS4("c32s003_130") from _call_BlinkXS4_2129
    mc "Te tengo que dejar ya."
    emm "*Risa* Aún no conozco a esa tal [car], pero ya me cae mal."
    emm "*Risa* ¿Puedo despedirla? Yo también soy accionista... Solo bromeo..."
    mc "Mejor que no la despidas. Es super eficiente. Si no la tuviera a ella, tendría aún menos tiempo para llamaros."
    call BlinkXS4("c32s003_135") from _call_BlinkXS4_2130
    emm "Entonces conservará su puesto... por ahora. Avisa a [aar] de que ya puede entrar para esa reunión aburrida."
    emm "Te quiero. No tardes tanto en llamarme."
    mc "Yo también te quiero. Intentaré no tardar."
    scene c31s007_305e with dissolve
    stop music fadeout (1.5)
    mc "Adelante, [aar]."
    return
label c32s003_JamPics:
    if _in_replay:
        call mrS3_ama_route from _call_mrS3_ama_route_24
    scene black with dissolve
    centered "{size=+20}{b}DÍA 47 – SÁBADO{/b}{/size}"
    scene c32s003_150a with fade
    "Al día siguiente, en casa, después de un día de reuniones..."
    play music ("music/Stardust.ogg")
    ama "Hoy he pasado a ver a [gav], parece que está muy ilusionado con el encendido del brazo mañana."
    bet "Se está recuperando mejor de lo que esperaba."
    bet "Uno de los cirujanos me ha dicho que es posible que tenga que ver con el envejecimiento acelerado de los clones."
    mc "¿Es eso posible?"
    scene c32s003_150b with dissolve
    bet "No solo es posible, sino que hay muchas probabilidades de que esté influyendo positivamente."
    bet "Me sorprendió el estado del muñón cuando lo examiné por primera vez."
    bet "No parecía el resultado de una amputación que se hubiera llevado a cabo hace menos de un mes. La cicatrización estaba avanzada."
    mc "¡Eso es increíble!"
    scene c32s003_150c with dissolve
    ama "Si los clones masculinos envejecen más rápido, supongo que tiene lógica que se curen más rápido también."
    bet "He pasado los últimos días mirando informes de cirugías y parece que es así casi siempre."
    mc "¿Casi siempre?"
    call BlinkXS4("c32s003_155") from _call_BlinkXS4_2131
    bet "Los tiempos de recuperación para una herida suelen ser más rápidos en el tejido muscular y óseo."
    bet "Pero no con los órganos internos. Una herida en un pulmón o en el hígado tiende a curarse al mismo ritmo que en..."
    mc "No digas 'una persona normal'."
    call BlinkXS4("c32s003_160") from _call_BlinkXS4_2132
    bet "*Risa* Iba a decir 'una persona con envejecimiento estándar.'"
    mc "Tenemos que buscar algún término más apropiado. Y más corto."
    call BlinkXS4("c32s003_165") from _call_BlinkXS4_2133
    bet "Lo que quería decir es que tengo muchos más datos de heridas en músculos y huesos que en órganos internos."
    bet "No sé si es un tema del tamaño reducido de la muestra o si es lo que está pasando en realidad."
    mc "¿Has probado a hablar con [mael] sobre el tema?"
    call BlinkXS4("c32s003_170") from _call_BlinkXS4_2134
    bet "Todavía no. Seguramente lo haga después de encender el brazo de [gav]."
    bet "Eso me proporcionará más datos. La operación combina tejido muscular, huesos, y tejido nervioso."
    mc "Lo entiendo. Si ves cómo se recupera cada uno de ellos..."
    call BlinkXS4("c32s003_175") from _call_BlinkXS4_2135
    ama "¿Se podría reproducir ese efecto?"
    ama "Me puedo imaginar a [flo] vendiéndoselo a deportistas de élite para curar sus lesiones más rápidamente."
    mc "No lo había pensado... ¿Es posible?"
    call BlinkXS4("c32s003_180") from _call_BlinkXS4_2136
    bet "Dudo mucho que se pueda reproducir sin acelerar el envejecimiento. Es algo que está en los genes de los chicos."
    bet "Y no creo que nadie acepte si le dices que se va a recuperar en tres meses de una lesión que tardaría seis."
    bet "Pero que va a perder dos meses de vida con ello. Me estoy inventando los números, antes de que preguntéis."
    mc "Hay deportistas que están muy locos y que querrían exprimir al máximo su tiempo en la élite."
    mc "Pero no creo que me sintiera cómodo si [deb.nick] lo usara..."
    call BlinkXS4("c32s003_185") from _call_BlinkXS4_2137
    ama "Sería su decisión. [deb.nick] es una chica inteligente y dudo que aceptara pagar ese precio."
    ama "Pero mientras [bet] hablaba, mi cabeza estaba dando vueltas..."
    mc "Sorpréndenos."
    call BlinkXS4("c32s003_190") from _call_BlinkXS4_2138
    ama "Parece que la curación funciona diferente según los órganos."
    ama "Imagina que se pudiera aislar el componente que hace que la piel se cure más rápido."
    ama "Envejecería más rápido, pero las heridas se cerrarían antes, previniendo infecciones. Y tener una piel más vieja no va a matar a nadie."
    call BlinkXS4("c32s003_195") from _call_BlinkXS4_2139
    bet "*Risa* Yo soy una muestra de ello. Aún estoy viva."
    bet "Pero tienes razón. Si se acelerara la curación de órganos independientes, como la piel, sería un avance increíble."
    call BlinkXS4("c32s003_200") from _call_BlinkXS4_2140
    bet "Por un momento he pensado en algunos lugares de África donde apenas hay antibióticos."
    bet "Pero sería difícil que ese tipo de tecnología llegara a sitios donde no llega un simple antibiótico."
    mc "¿Creéis que debería hablar con [mael] sobre el tema? Yo pienso que podría ser una buena dirección para la investigación."
    scene c32s003_205a with dissolve
    bet "Desde luego." (multiple=2)
    ama "Sí." (multiple=2)
    mc "No esperaba otra respuesta... Tengo una reunión con él la semana que viene. Se lo comentaré."
    mc "Supongo que a los clones femeninos no se les aplica, ¿cierto?"
    scene c32s003_205b with dissolve
    bet "No tienen envejecimiento acelerado, con lo que dudo que se curen más rápido."
    if persistent.family:
        ama "Nosotras no hemos notado nunca nada. Pero tampoco teníamos con qué comparar."
    else:
        ama "Supongo que habríais notado algo raro en [eri], [dap], o [emm]. Aunque es algo que puede pasar desapercibido."
    mc "Tenéis razón."
    scene c32s003_205c with dissolve
    bet "*Risa* ¿Nos compramos una camiseta que ponga eso?"
    ama "*Risa* Sería divertido que nosotras tuviéramos la camiseta y [mc] no la tuviera."
    mc "*Risa* Creo que [geo], de informática, se nos ha adelantado con lo de la camiseta."
    scene c32s003_205d with dissolve
    bet "*Risa* Tiene un gusto... discutible para la vestimenta."
    ama "No había hablado nunca con él antes, pero es un tipo tan divertido como sus camisetas."
    ama "En la de hoy ponía 'Si estoy comiendo, no soy de Soporte Técnico. Abre un ticket.'"
    mc "Hablando de informática..."
    mc "[ama], ¿me podrías dejar las fotos de las chicas mañana?"
    call BlinkXS4("c32s003_210") from _call_BlinkXS4_2141
    ama "¿Qué? ¿Por qué?"
    mc "Son las únicas que tienes y no querría que se dañaran más aún."
    mc "Están bastante desvaídas. Una polaroid no es el mejor sistema para mantener algo a largo plazo."
    mc "He pensado en digitalizarlas y mandárselas a Jamaal para ver si puede arreglarlas un poco. Hacer los colores más vivos y esas cosas."
    mc "Solo si tú quieres, claro."
    call BlinkXS4("c32s003_215") from _call_BlinkXS4_2142
    ama "¡Eso sería fantástico! No sé cómo no lo había pensado antes."
    call BlinkXS4("c32s003_220") from _call_BlinkXS4_2143
    bet "Es lógico que no lo hubieras pensado. En tu cabeza, esas fotos están ligadas al formato que tienen."
    bet "Y, si eres como yo en esto, no sabrías por dónde empezar a mejorar esas fotos."
    mc "Yo tampoco soy un genio del PaintStore, pero la broma de [emm] de ayer me dio la idea."
    call BlinkXS4("c32s003_225") from _call_BlinkXS4_2144
    ama "¿Qué broma?"
    scene c32s003_230An with dissolve
    "Les explicas la ocurrencia de [emm] con tu camioneta."
    "[ama] se sorprende de lo poco que llamas a casa. Ella hace doce o trece llamadas diarias."
    "A veces hablando con varias de las chicas a la vez."
    stop music fadeout (1.5)
    "Te empiezas a sentir mal porque el trabajo te está absorbiendo demasiado."
    return
label c32s003_GavArm:
    scene black with dissolve
    centered "{size=+20}{b}DÍA 48 – DOMINGO{/b}{/size}"
    scene c32s003_250a with fade
    play music ("music/Smoking Gun.ogg")
    bet "¿Estás listo?"
    gav "Estoy nervioso."
    mc "Es normal que lo estés."
    scene c32s003_250b with dissolve
    gav "También estoy ansioso. Cuando la Srta. [bet] me dijo que evolucionaba bien, creí que lo podríamos encender antes."
    bet "He preferido mantener la prudencia. Te has curado mejor de lo que esperaba en una semana, pero no tenemos todos los datos aún."
    bet "Vamos a quitar el cabestrillo. Intenta mantener el hombro quieto hasta que llegue [cal]."
    scene c32s003_250c with dissolve
    gav "Entiendo que hayas querido ser prudente, pero odio estar encerrado aquí."
    bet "No te preocupes. En cuanto llegue [cal] lo encenderemos. Debería estar aquí en unos minutos."
    mc "Por lo que me ha dicho, iba a revisar los últimos parámetros antes del encendido."
    mc "Piensa que también es importante para él."
    call BlinkXS4("c32s003_255") from _call_BlinkXS4_2145
    gav "Lo sé, y no quiero sonar desagradecido, pero ver la línea de meta tan cerca, pero que no se acerca, es complicado."
    mc "Lo entiendo. Una vez estuve ingresado en el hospital y los médicos, un día por la mañana, me dijeron que me darían el alta."
    mc "El alta no llegó hasta la tarde, y esas horas se hicieron eternas. Sé que no es lo mismo, pero..."
    call BlinkXS4("c32s003_260") from _call_BlinkXS4_2146
    gav "¿Qué te pasó para que te ingresaran en el hospital?"
    mc "Por aquel entonces era demasiado goloso, y me empaché con los postres de [sam.nick]."
    call BlinkXS4("c32s003_265") from _call_BlinkXS4_2147
    bet "*Risa* Es difícil dejar de comer los postres de [sam.nick]. O los de [mar], o los de [nor]."
    mc "Lo sé. Pero tú nunca te has empachado."
    bet "*Risa* Yo siempre dejo un hueco en mi barriga por si alguien ha hecho pizza de chocolate y plátano..."
    call BlinkXS4("c32s003_270a") from _call_BlinkXS4_2148
    gav "Es muy raro..."
    mc "¿Qué te parece tan raro? Aparte de ser una bomba calórica, la pizza de chocolate y plátano está buena."
    gav "No me refiero a eso. Cuando os vigilábamos erais... no sé... el enemigo."
    call BlinkXS4("c32s003_270b") from _call_BlinkXS4_2149
    gav "Ahora que os empiezo a conocer... Tengo ganas de conocer de nuevo a [nor] y a [mee]. Y pedirles disculpas por lo que pasó."
    gav "Y de probar todos esos postres de los que me ha hablado la Srta. [bet]."
    scene c32s003_275a with dissolve
    bet "A mí ya me las pediste y te dije que no era necesario. Cumplías órdenes."
    bet "El problema está en quien daba esas órdenes."
    gav "Lo sé, pero..."
    bet "Y el siguiente problema es que sigues llamándome 'Srta. [bet].' Pero de eso ya hablaremos."
    mc "A quien vas a tener que pedirle disculpas es a [emm]."
    call BlinkXS4("c32s003_280") from _call_BlinkXS4_2150
    gav "¿Por qué? ¡Nunca le hicimos nada!"
    mc "*Risa* Has dicho que tienes ganas de conocer a [nor] y a [mee]. No has dicho nada de ella."
    mc "Pero tranquilo, guardaremos tu secreto."
    call BlinkXS4("c32s003_285") from _call_BlinkXS4_2151
    gav "*Risa* Es una de las principales razones por las que quiero que esto salga bien."
    gav "Obviamente, volver a sentirme completo es la principal razón, pero..."
    call BlinkXS4("c32s003_290") from _call_BlinkXS4_2152
    gav "Devolverle a vuestra familia parte de lo que os intentamos quitar es una razón importante para mí también."
    gav "Sé que me dijiste que, si esto no salía bien, podría ocuparme de la vigilancia, pero..."
    gav "No sé... veros a través de cámaras no sería lo mismo. Y menos aún con lo que me ha contado la Srta. [bet]."
    mc "*Risa* No le hagas demasiado caso a Tía [bet], exagera un poco cuando habla de la familia."
    call BlinkXS4("c32s003_295") from _call_BlinkXS4_2153
    bet "¡No he exagerado NI UN ÁPICE! Todo lo que le he contado es verdad."
    mc "Pero seguro que sólo le has contado las cosas buenas."
    bet "¡Claro! El resto ya lo descubrirá por sí mismo."
    call BlinkXS4("c32s003_300") from _call_BlinkXS4_2154
    mc "¿Hay alguien a quién tengas ganas de conocer especialmente?"
    gav "A todas las chicas, a Jamaal, a Zeus... Pero creo que, por la información que tengo, a [sca] y a [dap]."
    gav "Y obviamente a [emm], en caso de que esto se esté grabando y el archivo acabe en sus manos."
    mc "*Risa* Buenas elecciones todas. Especialmente lo de [emm]. Nunca sabes qué puede hacerle a tu camioneta si se enfada."
    call BlinkXS4("c32s003_305") from _call_BlinkXS4_2155
    cal "Disculpad el retraso. Había algunos ajustes de última hora que tenía que hacer en el servidor."
    mc "No te preocupes, íbamos a empezar a mordernos las uñas en unos minutos."
    mc "¿Los ajustes han ido bien?"
    call BlinkXS4("c32s003_310") from _call_BlinkXS4_2156
    cal "Como el músculo se ha curado mejor de lo que esperábamos, podemos encenderlo con un poco más de potencia."
    cal "Aproximadamente la misma que tendría un brazo biológico. Creo que será una prueba mejor que con un brazo de potencia reducida."
    cal "El cuerpo y el cerebro de [gav] podrán adaptarse más rápidamente."
    mc "Es tu creación. Confío en ti totalmente para esto."
    mc "¿Alguna pregunta, [gav]?"
    scene c32s003_315a with dissolve
    gav "¿Qué tengo que hacer cuando lo enciendas?"
    gav "¿Tengo que dejar la mente en blanco o algo así?"
    cal "Justo lo contrario. Tienes que pensar lo que quieres hacer con el brazo, como harías con el izquierdo."
    cal "Empezaremos con pruebas sencillas, como tocarte la frente, primero con el brazo biológico y después con la prótesis."
    cal "Con la prótesis, intenta hacer los movimientos lentamente. No queremos que tu dedo atraviese tu cráneo si lo haces demasiado rápido."
    mc "*Sorprendido* ¿Puede hacer eso?"
    call BlinkXS4("c32s003_325") from _call_BlinkXS4_2157
    cal "Seguramente ahora mismo no, con la potencia que le he asignado. En funcionamiento completo, podría hacerlo."
    cal "Pero para cuando subamos la potencia al máximo, [gav] ya estará acostumbrado al peso y a la velocidad de reacción."
    scene c32s003_330a with dissolve
    bet "No te preocupes, cielo. No vas a romperte ningún hueso hoy. Iremos subiendo la potencia en los próximos días."
    gav "OK. Entendido. Pensar qué gesto quiero hacer y esperar que el brazo lo entienda y lo haga a una velocidad normal."
    bet "Normal no. Más lento de lo normal. No te puedes romper el cráneo, pero te podrías sacar un ojo."
    gav "Entendido. Cuando queráis."
    scene c32s003_330b with dissolve
    cal "En cuanto lo encienda, notarás un hormigueo en el hombro y la sensación de miembro fantasma al cabo de unos segundos."
    cal "A diferencia de un miembro fantasma de verdad, el brazo reaccionará a tus pensamientos porque realmente está ahí."
    cal "¿Preparado?"
    gav "Acojonado, pero preparado."
    scene c32s003_330c with dissolve
    cal "Ya está. En cuanto sientas el hormigueo piensa en el movimiento que quieres hacer. Aunque empezaremos con el brazo biológico."
    cal "De momento es mejor que no pienses en moverlo. Moverás el izquierdo, y después intentarás repetir el movimiento con el derecho."
    cal "Al principio tiene que ser un pensamiento consciente o tu subconsciente tomará el control."
    cal "Poco a poco deberías acostumbrarte a la sensación y lo acabarás notando como el otro brazo."
    gav "Ya empiezo a notar el hormigueo. Es como si tuviera el brazo entumecido. Pero lo noto."
    cal "Genial. Eso es lo que esperábamos. Ahora cierra la mano izquierda y..."
    scene c32s003_335An with dissolve
    "El brazo salta de golpe y empieza a moverse en un gesto que conoces muy bien de tus tiempos de adolescente."
    gav "¿Qué? ¡Para eso! ¡No es eso lo que quería hacer!"
    cal "Dame un segundo. Intenta mantener el brazo quieto."
    scene c32s003_340a with dissolve
    cal "Hecho. Desconectado. Déjame mirar unos parámetros."
    bet "¿Qué ha pasado? ¿Cómo lo has notado?"
    gav "Lo notaba como si hubiera dormido encima del brazo durante horas, pero como si fuera mío."
    scene c32s003_340d with dissolve
    gav "No sé por qué ha hecho... esos movimientos... No he pensado en moverlo. [cal] ha dicho que los primeros movimientos serían con el de verdad."
    mc "[cal] ha dicho que. si no lo controlabas con un pensamiento consciente, tu subconsciente tomaría el control..."
    call BlinkXS4("c32s003_345") from _call_BlinkXS4_2158
    gav "Pero no estaba pensando en... eso..."
    mc "El subconsciente puede ser un auténtico hijo de puta, [gav]. Y si eres diestro, supongo que llevas semanas sin..."
    gav "Pero no hubiese querido hacerlo... y menos aún aquí delante de la Srta. [bet], de ti, y de [cal]..."
    call BlinkXS4("c32s003_350") from _call_BlinkXS4_2159
    bet "Incluso no te lo recomendaría en las primeras semanas, hasta que tengas control del brazo."
    bet "Recuerda que es más fuerte que el brazo original. No quieres acabar con tus tesoros espachurrados entre plástico y titanio."
    mc "¡Que poco tacto tienes, Tía [bet]!"
    call BlinkXS4("c32s003_355a") from _call_BlinkXS4_2160
    bet "Si el chico no lo ha pensado conscientemente y lo intenta esta noche, podría tener un accidente."
    "[bet] no abre el puño, ilustrando en la mente de los tres hombres alrededor de la mesa un dolor que os podéis imaginar perfectamente."
    bet "Mejor que esté sobre aviso. Además, no sé cómo de agradable será el tacto en una zona sensible."
    mc "Creo que yo puedo pasar sin esa información."
    call BlinkXS4("c32s003_355b") from _call_BlinkXS4_2161
    cal "Hecho. He ajustado algún parámetro. ¿Probamos a encenderlo otra vez?"
    mc "¿Puedes gestionar los pensamientos subconscientes?"
    cal "No. Lo que he hecho es introducir un retraso en la respuesta."
    cal "Si un pensamiento subconsciente intenta tomar el control y [gav] se da cuenta, podrá rectificar con un pensamiento consciente."
    cal "¿Puedes ayudar a [gav] a poner el brazo encima de la mesa?"
    scene c32s003_340c with fade
    cal "Ahora notarás que el brazo tarda un poco en reaccionar a lo que le ordenes. Iremos gestionando eso tal como te adaptes."
    cal "¿Preparado?"
    gav "Estoy más acojonado que antes, pero estoy preparado."
    cal "Piensa en mantener la mano sobre la mesa. Las dos manos sobre la mesa."
    scene c32s003_355An with dissolve
    cal "Hecho."
    "Todos miráis fijamente el brazo de titanio. Se empieza a mover con ligeros espasmos. Pero nada que ver con los movimientos anteriores."
    gav "Juro que estoy pensando en mantenerlo quieto."
    bet "Lo estás haciendo muy bien, cielo."
    cal "Dale al brazo un poco de tiempo para entender cómo piensas."
    cal "Recuerda que hemos introducido un pequeño retraso entre lo que piensas y lo que el brazo hace."
    mc "Y no sé si servirá de algo, pero relájate. Como diría [emm], es jodido tener que pensar en todo momento."
    scene c32s003_355c with fade
    "Al cabo de unos minutos, el brazo se queda totalmente inmóvil."
    scene c32s003_360An with dissolve
    gav "¡Lo he hecho! Está quieto."
    mc "Te he dicho que podrías hacerlo."
    bet "¡Muy bien, cielo!"
    cal "Bueno, realmente se han acabado las baterías..."
    scene c32s003_360e with dissolve
    bet "¿Tan rápido?" (multiple=2)
    gav "¿Qué? ¿Ya?" (multiple=2)
    mc "Creía que durarían más de un par de minutos. ¿O es porque estamos con carga de pruebas?"
    cal "Es broma. Duran más de una semana con este nivel de carga. Alrededor de diez días con carga completa."
    cal "Pero mirad."
    scene c32s003_360f with fade
    "En el momento en que [gav] ha dejado de pensar en mantener el brazo quieto, su subconsciente ha tomado el mando."
    "Ha hecho el mismo gesto que hubiera hecho con su brazo biológico."
    gav "¡Funciona!"
    mc "Parece que [cal] es un cabrón astuto."
    bet "Te ha hecho dejar de pensar en el brazo por un segundo."
    cal "Sabía que sería difícil que se relajara si estaba pensando en el brazo..."
    mc "Lo has hecho bien, [cal]."
    mc "¿Cuál es el siguiente paso?"
    call BlinkXS4("c32s003_365") from _call_BlinkXS4_2162
    cal "Tenemos un montón de pruebas y de entrenamiento por delante."
    cal "Los parámetros que muestran los gráficos están dentro de lo esperado."
    cal "Habrá que hacer ajustes, pero vamos en el buen camino."
    mc "Tu prioridad absoluta ahora mismo es que ese brazo funcione tal y como lo diseñaste."
    call BlinkXS4("c32s003_370") from _call_BlinkXS4_2163
    cal "Pero [mael]..."
    mc "Si [mael] tiene alguna duda sobre mi orden de prioridades, dile que la puerta de mi despacho está abierta."
    scene c32s003_375g with dissolve
    bet "*Risa* Si [car] le deja entrar, claro."
    gav "[car] es una buena mujer, Srta. [bet]."
    cal "Sí, pero puede dar miedo y ser sobreprotectora con... Bueno, con sus prerrogativas como secretaria."
    mc "¿Podemos seguir con las pruebas? Me gustaría ver algún progreso antes de mi siguiente reunión."
    mc "Me refiero al progreso planificado. Que [gav] se esté cruzando de brazos me indica que todo va a ir bien."
    scene c32s003_375An1 with dissolve
    "Durante los siguientes minutos, [gav] hace ejercicios básicos, como abrir y cerrar ambas manos a la vez o levantarlas de la mesa."
    "El brazo mecánico tarda un poco en reaccionar, tal y como esperabais."
    scene c32s003_380a with dissolve
    cal "Dadme un segundo para que retoque los parámetros de retraso. Creo que vamos por el buen camino."
    mc "¿Cómo te sientes, [gav]? Recuerda que es el primer día y no creo que sea bueno que fuerces demasiado."
    bet "[mc] tiene razón. Tus músculos no están curados del todo."
    gav "No me duele nada ni me siento cansado..."
    scene c32s003_380b with dissolve
    gav "Hablando de eso... ¿El brazo nuevo puede cansarse? ¿Cómo lo notaré?"
    cal "Es complicado de explicar. Hay dos tipos de fatiga. Periférica y central."
    call BlinkXS4("c32s003_385") from _call_BlinkXS4_2164
    cal "La fatiga periférica se debe a el exceso o defecto de algunos compuestos químicos. Esa no la notarás, al menos en el brazo, pero sí en el hombro."
    cal "La fatiga central se produce porque tu cerebro sabe que deberías estar llegando a tu límite de ejercicio."
    cal "Reduce la frecuencia y la intensidad de las señales eléctricas que manda a los músculos."
    call BlinkXS4("c32s003_390") from _call_BlinkXS4_2165
    cal "También hay un cambio de balance en los compuestos químicos, como serotonina o dopamina."
    cal "Eso hace que TÚ te notes cansado."
    cal "Como tu hombro sigue siendo biológico y tu cerebro cree que tu brazo también lo es, es posible que sientas ese tipo de fatiga, aunque reducida."
    cal "Aunque creo que eso te lo podrá explicar mejor la Srta. [bet]."
    cal "Ya he reajustado el retraso. Prueba a repetir los ejercicios ahora."
    scene c32s003_375An2 with dissolve
    "[gav] repite los ejercicios de nuevo. Esta vez no se aprecia retraso en la copia de los movimientos."
    cal "Sigue habiendo unos milisegundos de retraso, pero lo iremos corrigiendo."
    gav "Ahora se nota más natural... Es casi como si el brazo fuera mío."
    gav "Tengo ganas de probarlo en el campo de tiro."
    bet "Para eso aún faltan algunos días, cielo. Acabas de aprender a cerrar las dos manos a la vez."
    scene c32s003_395a with dissolve
    mc "Me alegro mucho por ti, [gav]. Y por ti, [cal]. Buen trabajo."
    mc "Ahora os tengo que dejar; tengo una reunión en unos minutos. Gracias a todos por esto."
    scene c32s003_395b with hpunch
    gav "Gracias a ti, [mc]."
    "El tacto del brazo mecánico se nota raro durante el inesperado abrazo. La ternura del abrazo compensa su extrañeza."
    "Por un momento, antes de devolver el abrazo, entiendes cómo se siente [aar]."
    mc "*Risa* Creo que pasas demasiado tiempo con Tía [bet]."
    scene c32s003_400a with hpunch
    call BlinkXS4("c32s003_400") from _call_BlinkXS4_2166
    gav "¡Perdón, Señor! Me he extralimitado."
    mc "No lo has hecho, [gav]. Si me río por algo que haga alguien, significa que no me molesta."
    mc "Al menos sabemos que puedes dar abrazos sin partirle las costillas a nadie."
    call BlinkXS4("c32s003_405") from _call_BlinkXS4_2167
    cal "*Risa por lo bajo* Seguramente podrá hacerlo cuando el brazo tenga la potencia definitiva."
    mc "Entonces será mejor que aprenda a controlar la fuerza para entonces. *Risa* O no voy a dejarle que vuelva a abrazarme."
    mc "Seguid con las pruebas, por favor. [cal], mándame un informe cada día con los progresos... por email."
    mc "No creo que pueda asistir a todas las pruebas."
    scene c32s003_405d with dissolve
    "Te giras hacia la puerta cuando un pensamiento te asalta antes de abrirla."
    mcp "(Espero que los informes de [cal] no sean tan exhaustivos como los de [aar].)"
    stop music fadeout (1.5)
    mc "Informe ejecutivo, [cal]."
    return
label c32s003_redecor:
    scene black with dissolve
    centered "{size=+20}{b}DÍA 50 – MARTES{/b}{/size}"
    call BlinkXS4("c32s003_450") from _call_BlinkXS4_2168
    play music ("music/SaveMe.ogg")
    "Algunos días después, tras tener que insistirle a [ama] varias veces para que te preste las fotos..."
    mc "Buenos días, [car]."
    car "Buenos días, Sr. Marks."
    mc "[mc]."
    "Sabes que parece una batalla perdida, pero has ganado alguna batalla en tu vida por ser muy insistente."
    car "¿Puedo ayudarle en algo?"
    mc "Tengo una pregunta sobre mi despacho. ¿Hay alguna razón por la que parece sacado de un documental de la Segunda Guerra Mundial?"
    call BlinkXS4("c32s003_455") from _call_BlinkXS4_2169
    car "El Sr. Daniels lo mandó redecorar cuando el Sr. Richards murió."
    car "Hizo tapiar la habitación auxiliar y darle ese aspecto."
    mc "¿Habitación auxiliar?"
    call BlinkXS4("c32s003_460") from _call_BlinkXS4_2170
    car "Detrás de la pared que hay tras su silla hay un dormitorio. El Sr. Richards lo usaba cuando tenía que quedarse a dormir en las instalaciones."
    car "El Sr. Daniels dijo que no era necesario. Inicialmente tenía pensado usarlo como archivo extra, pero al final decidió tapiarlo."
    call BlinkXS4("c32s003_465") from _call_BlinkXS4_2171
    car "¿Querría usted recuperar la habitación con la reforma del despacho?"
    mc "No había pensado en reformarlo, tan solo había pensado en una mano de pintura y mobiliario... del Siglo XXI."
    mc "A veces me siento como si fuera el General Eisenhower en ese despacho."
    call BlinkXS4("c32s003_470") from _call_BlinkXS4_2172
    car "Ese era el efecto que buscaba el Sr. Daniels. Aunque él dijo General MacArthur."
    car "Puedo encargarme de la pintura y de los muebles si quiere."
    car "Y destapiar la habitación no sería demasiado problema si se hace antes de la pintura."
    mc "Me parece una buena idea. Creo que es un desperdicio de espacio tener una habitación tapiada."
    call BlinkXS4("c32s003_475") from _call_BlinkXS4_2173
    car "No se preocupe, entonces. Haré unas llamadas y lo tendrá hecho en menos de una semana."
    mc "Gracias, [car]."
    mc "Aparte de eso, ¿puedo pedirte un favor?"
    call BlinkXS4("c32s003_480") from _call_BlinkXS4_2174
    "La diminuta mujer casi se siente ofendida, pero te cuesta leer sus expresiones."
    car "Si es trabajo, no es un favor, soy su secretaria."
    mc "He intentado escanear un par de fotos con el escáner que tengo en el despacho, pero no consigo que tengan la resolución que quiero."
    mc "¿Hay algún escáner de mayor resolución que pueda usar?"
    call BlinkXS4("c32s003_485") from _call_BlinkXS4_2175
    car "El escáner de su despacho tiene varios años y... no es muy bueno. Los CEOs anteriores no lo usaban nunca."
    "Es la primera vez que no los nombra por sus apellidos. A lo mejor no es una batalla perdida al fin y al cabo."
    car "Si me deja las fotos, puedo enviar a alguien a escanearlas en el escáner de alta resolución del despacho de [mael]."
    "Un escalofrío te recorre de arriba a abajo. No estás dispuesto a desprenderte de las fotos y a que [car] se las de a alguien."
    "Son las únicas copias que existen y no quisieras que les pasara nada."
    call BlinkXS4("c32s003_490") from _call_BlinkXS4_2176
    "La anciana capta tus dudas, aunque las malinterpreta."
    car "Aunque si es algo demasiado privado... Puedo decirle a [mael] que usted mismo irá a escanearlas."
    mc "No es que sea privado, sino que... no me gustaría que les pasara nada a estas fotos. Son únicas y no hay más copias."
    mc "No me sentiría cómodo si se las dieras a alguien para escanearlas y se dañaran."
    call BlinkXS4("c32s003_495") from _call_BlinkXS4_2177
    "La secretaria se relaja visiblemente."
    car "Si quiere, puedo ocuparme personalmente de escanearlas. Le prometo que no les pasará nada."
    mc "No quisiera ser una molestia. No es un asunto de trabajo precisamente."
    car "No es una molestia. Tan solo son un par de fotos..."
    mc "De acuerdo. Muchas gracias, [car]."
    scene c32s002_005a with fade
    "Tras entregarle un sobre con las dos polaroids vas a tu despacho a leer informes de [aar] y [vin]."
    stop music fadeout (1.5)
    "Al cabo de unos minutos..."
    play music ("music/SCP-x6x.ogg")
    car "*A través de la pared* *SUSPIRO DE SORPRESA*"
    scene c32s003_495e with fade
    "Sales de la habitación rápidamente y la encuentras mirando la foto de Fiona. Casi temiendo tocarla."
    mc "¿Estás bien, [car]?"
    car "No."
    call BlinkXS4("c32s003_500") from _call_BlinkXS4_2178
    car "No sabía que existiera ninguna foto de Fiona..."
    mc "[ama] las tenía escondidas por miedo a que alguien se las quitara."
    call BlinkXS4("c32s003_505") from _call_BlinkXS4_2179
    car "Si Daniels o Richards lo hubieran sabido, seguro que se la hubieran quitado."
    "No puedes dejar de notar la ausencia del 'Sr.' en su frase."
    mc "Ahora nadie se las va a quitar. Pero son las únicas copias y quiero tenerlas en formato digital, para intentar repararlas."
    call BlinkXS4("c32s003_510") from _call_BlinkXS4_2180
    car "¿Le importa si hago una copia para mí? De las dos fotos. Por favor."
    "El tono lastimero en su voz hace que te sea muy difícil negarte. Pero no son tus fotos."
    mc "Supongo que no habrá problema, pero déjame consultarlo con [ama]. Las fotos no son mías y..."
    scene c32s003_510d with hpunch
    car "Gracias, Sr. Marks."
    "La sorpresa por el inapropiado abrazo hace que te olvides de recordarle que debe llamarte [mc]. Una oportunidad perdida para decantar la batalla a tu favor."
    mc "Las chicas te importan, ¿verdad?"
    call BlinkXS4("c32s003_515") from _call_BlinkXS4_2181
    car "He visto nacer a cada una de las series, Sr Marks. Me importan todos."
    car "Pero con las chicas... no sé... el sentimiento es un poco diferente."
    call BlinkXS4("c32s003_520") from _call_BlinkXS4_2182
    car "Las acuné a todas cuando nacieron. Fueron las únicas con las que me dejaron hacerlo."
    if persistent.family:
        car "Me alegro mucho de que [ama] y [eva] hayan encontrado a su familia después de todos estos años."
        car "Me alegré cuando me enteré de que habían conocido a [mar] y a [nor]. También por [aar]."
        mc "Parece que ellas lo han disfrutado más que [aar]."
        call BlinkXS4("c32s003_525") from _call_BlinkXS4_2183
        car "[aar] es de la primera serie. Alfred y Arnau eran su familia. Después 'adoptaron' a las chicas." id c32s003_redecor_9614a4a5
        car "Las chicas crecieron siendo seis, y teniendo a los A como si fueran sus primos mayores."
        car "También los B y los C estaban ahí, y después llegaron el resto de las series. Tienen un concepto más amplio de familia."
        mc "Lo entiendo."
        call BlinkXS4("c32s003_530") from _call_BlinkXS4_2184
        car "Algún día, me gustaría poder conocer a [emm], [dap] y [eri]. Para ver de dónde salieron mis chicas."
        mc "Estoy seguro de que lo harás. Las tres están deseando venir a conocer la empresa."
        mc "Sabiendo lo que sientes respecto a ellas, estoy seguro de que vendrán incluso antes de lo planeado."
        scene c32s003_510e with hpunch
        car "Gracias, Sr. Marks."
        mc "[mc]. O tendré que decirles que no vengan a la isla."
    else:
        car "Yo busqué a sus madres. En parte están aquí por culpa mía."
        car "Y, algún día, me gustaría poder conocer a [emm], [dap] y [eri]."
        mc "Espera... ¿Has dicho que buscaste a sus madres?"
        call BlinkXS4("c32s003_525") from _call_BlinkXS4_2185
        car "Sí. Mujeres sin recursos de la ciudad. Mujeres que querían abortar."
        car "No fue difícil pedirles que se las dieran a la empresa en adopción. A cambio de una compensación económica."
        mc "¿Mantenemos contacto con ellas? ¿Sabemos dónde están?"
        call BlinkXS4("c32s003_530") from _call_BlinkXS4_2186
        car "La empresa nunca ha tenido ningún interés en ellas después de pagarles. Y, sin recursos, les perdí la pista a la mayoría."
        car "Sé que las madres de Clarice y de [eva] murieron. Drogas... Pero del resto no tengo ninguna información."
        mc "¿Quieres una nueva tarea?"
        call BlinkXS4("c32s003_535") from _call_BlinkXS4_2187
        car "¿Qué? ¿En serio?"
        mc "Creo que [ama] debe tener el derecho a conocer a su madre biológica, si es posible y si ella quiere."
        scene c32s003_510e with hpunch
        car "Gracias, Sr. Marks. Me pondré a ello en seguida."
        mc "[mc]. O tendré que cancelar la tarea."
    car "Gracias, [mc]."
    stop music fadeout (1.5)
    "Parece que el nombre se le atraganta al decirlo. Pero es una pequeña victoria."
    return
label c32s003_MaelDrug:
    scene c32s003_540a with fade
    call BlinkXS4("c32s003_540") from _call_BlinkXS4_2188
    "Unas horas después, durante la reunión con [mael], tras explicarle la idea sobre aislar el gen del envejecimiento..."
    play music ("music/romantic-day.ogg")
    mael "¡Eso es imposible!"
    mc "No te voy a decir qué es posible y qué no lo es en tu campo, [mael]."
    mc "Pero fuiste tú el que habló sobre investigaciones de frontera. Creo que es una oportunidad."
    call BlinkXS4("c32s003_545") from _call_BlinkXS4_2189
    mael "Pero ¿aislar el gen de envejecimiento acelerado órgano a órgano?"
    mael "Eso es decididamente una locura. No se puede hacer."
    mc "Tan solo te pido que le eches una ojeada al asunto y pienses en qué puedes necesitar para hacerlo."
    mc "O para hacer las pruebas necesarias para descartarlo del todo."
    call BlinkXS4("c32s003_550") from _call_BlinkXS4_2190
    mael "No hace falta hacer ninguna prueba. Ya las hicimos hace años cuando investigamos como parar el envejecimiento a partir de cierta edad."
    mael "O lo aceleras todo o lo ralentizas todo. No puedes hacer envejecer el cerebro sin envejecer los pulmones."
    mael "Y no puedes ralentizar el crecimiento de los huesos sin ralentizar el crecimiento del hígado."
    mc "Espera. ¿Se hicieron pruebas para eliminar el envejecimiento acelerado?"
    call BlinkXS4("c32s003_555") from _call_BlinkXS4_2191
    mael "No para eliminarlo, sino para ralentizarlo. Para que los clones envejecieran a una velocidad... más o menos normal."
    mc "Supongo que fracasasteis. Siguen envejeciendo a ritmo acelerado. Excepto las chicas, claro."
    call BlinkXS4("c32s003_560") from _call_BlinkXS4_2192
    mael "¡No fracasamos! El experimento fue un éxito. ¡Conseguimos ralentizar el envejecimiento hasta 1.064!"
    mael "Y es independiente de la serie. Da lo mismo que sea un A, que envejece a 3x, o un J, que envejece a 1.7x."
    mc "¿Entonces por qué [aar] parece mi abuelo?"
    call BlinkXS4("c32s003_565") from _call_BlinkXS4_2193
    mael "Porque es caro y ni Richards ni Daniels veían ningún beneficio en ello."
    mael "Si tienes recambios para los clones que, eventualmente, tengas que retirar por ser demasiado viejos... Es más barato."
    mc "¿Me estás diciendo que les estamos quitando años de vida a los chicos por una cuestión de dinero?"
    mc "¿Tú crees que eso es normal? ¿De cuánto dinero estamos hablando?"
    call BlinkXS4("c32s003_570") from _call_BlinkXS4_2194
    mael "Sí. Fue una decisión económica."
    mael "Pero no es una decisión que tuviera que tomar yo. Eso lo tiene que decidir la persona que se sienta tras esta mesa."
    mc "Vale, pero ¿de cuánto dinero estamos hablando?"
    call BlinkXS4("c32s003_575") from _call_BlinkXS4_2195
    mael "Los experimentos fueron 'caros', pero si se implementara la fabricación en serie de la droga, unos $5,000 o $6,000 anuales por clon."
    "Haces unos cálculos mentales rápidos..."
    mc "¡Eso son menos de 3 millones al año para los 426 clones! Tú gastas mucho más cada mes en equipo de investigación."
    call BlinkXS4("c32s003_580") from _call_BlinkXS4_2196
    mael "El equipo de investigación es necesario."
    mc "Y darles una vida a nuestros chicos también es necesario. Ya no son recambios, ni son prescindibles."
    mc "Buscaré de dónde sacar los 3 millones para destinarlos a la fabricación y distribución de la droga."
    call BlinkXS4("c32s003_585") from _call_BlinkXS4_2197
    mael "Siempre y cuando no toques mis gastos en equipo de investigación."
    mael "Si recortas en eso, no podré clonar tu páncreas."
    mc "¿Mi páncreas?"
    call BlinkXS4("c32s003_590") from _call_BlinkXS4_2198
    mael "Me pediste que clonara órganos sueltos y que empezara por un páncreas."
    mc "*Risa* No te pedí que empezaras con un páncreas. Era un ejemplo. Me da lo mismo que sea un riñón o un corazón."
    mc "Quiero que investigues cómo clonar órganos sueltos. Y quiero que se puedan clonar de un donante de cualquier edad."
    call BlinkXS4("c32s003_595") from _call_BlinkXS4_2199
    mael "Eso lo complica todo. Nuestro proceso parte de tejido embrionario, no de órganos totalmente formados."
    mc "¿Se puede hacer?"
    call BlinkXS4("c32s003_600") from _call_BlinkXS4_2200
    mael "Con el suficiente tiempo y dinero... Se puede investigar, si hay un órgano que clonar. Al menos al principio." id c32s003_MaelDrug_79de1b96
    mael "No creo que pudiéramos clonar el brazo derecho de [gav], porque ya no existe. Ni siquiera si partiéramos de su brazo izquierdo."
    "En ese momento te das cuenta de que, por alguna razón, esperabas una respuesta diferente."
    "El útero de [mee] te viene a la mente por un segundo. Es una lástima que no sea ni siquiera una posibilidad."
    mc "De acuerdo, no recortaré tu presupuesto de investigación."
    mc "Tengo otra pregunta. ¿La droga para parar el envejecimiento...?"
    call BlinkXS4("c32s003_605") from _call_BlinkXS4_2201
    mael "Ralentizarlo para que sea casi normal."
    mc "Vale. La droga para ralentizar el envejecimiento para que sea casi normal, ¿sería aplicable a personas que envejecen a un ritmo normal?"
    mc "Podría ser la crema anti edad definitiva y [flo] estaría muy feliz de poder venderla."
    call BlinkXS4("c32s003_610") from _call_BlinkXS4_2202
    mael "¿Te has mirado alguna vez en un espejo? Aparentas más edad de la que tienes."
    mc "Lo sé. ¿Pero qué tiene que ver eso?"
    call BlinkXS4("c32s003_615") from _call_BlinkXS4_2203
    mael "Tú eres el donante cero."
    mael "Por entonces no lo sabíamos, pero esos genes que te hacen parecer más mayor se amplificaron accidentalmente en la clonación de los A."
    mael "Hemos ido ajustando esos genes durante años para que produzcan un crecimiento acelerado, pero no tanto como en los A."
    call BlinkXS4("c32s003_620") from _call_BlinkXS4_2204
    mael "Desde los G es 1.7. La anterior dirección lo consideró el valor adecuado."
    mc "¿Esos genes? ¿Me estás diciendo que todos los clones tienen esos genes que son míos?"
    call BlinkXS4("c32s003_625") from _call_BlinkXS4_2205
    mael "Sí. Creía que lo sabías..."
    mc "¡No tenía ni idea! ¡Joder! ¡De alguna forma soy el padre de todos ellos!"
    call BlinkXS4("c32s003_630") from _call_BlinkXS4_2206
    mael "No. No funciona así."
    mc "Explícamelo como si fuera idiota."
    call BlinkXS4("c32s003_635") from _call_BlinkXS4_2207
    "La cara que pone el científico te indica que es lo que ha estado haciendo hasta ahora."
    mael "Un humano tiene unos 19,500 genes con su código genético y alrededor de 40,000 genes RNA, que producen alrededor de tres mil millones de 'letras'."
    mael "Los genes del envejecimiento acelerado son un grupo de quince 'letras'."
    call BlinkXS4("c32s003_640") from _call_BlinkXS4_2208
    mael "Si coges dos humanos cualesquiera, comparten el 99.9%% de su ADN. 2,997,000,000 'letras'."
    mael "Si coges un padre y un hijo, comparten el 99.95%% de su ADN. 2,998,500,000 'letras'."
    mael "Tu compartes con los clones 2,997,000,015 'letras'. 99.9000005%%. Excepto con [aar], obviamente."
    call BlinkXS4("c32s003_645") from _call_BlinkXS4_2209
    mael "En cualquier caso, no eres su 'padre'. Y eso sería simplificándolo mucho y explicado para idiotas."
    mael "Escogerte a ti como donante cero y la amplificación de ese grupo de genes hizo que los planes originales de la empresa fracasaran."
    mael "Por otro lado, hizo que entendiéramos mucho mejor el envejecimiento acelerado."
    mc "Todo eso lo entiendo... más o menos. Pero qué tiene que ver con usar la droga antienvejecimiento contigo o conmigo."
    call BlinkXS4("c32s003_650") from _call_BlinkXS4_2210
    mael "Contigo podría funcionar porque tienes ese grupo de genes, aunque no lo tengas amplificado. Pero el resultado sería casi imperceptible."
    mael "En ti, la piel 'envejece' más rápido, pero el resto de tu cuerpo tiene tu edad. Por eso pareces mayor, pero tienes la energía que corresponde con tu edad."
    mael "Como te he dicho, hemos reducido el envejecimiento a 1.064. Excepto por tu piel, el resto de tu cuerpo no envejece a esa velocidad."
    call BlinkXS4("c32s003_655") from _call_BlinkXS4_2211
    mael "Si la usara yo, seguramente no tendría ningún efecto. No tengo ese grupo de genes, con lo que la droga no haría nada en mí."
    call BlinkXS4("c32s003_660") from _call_BlinkXS4_2212
    "Ves cómo se le ilumina la cara por un momento cuando se da cuenta de las implicaciones."
    mael "Pero con el presupuesto adecuado, podría intentar replicarlo para personas sin ese grupo de genes..."
    mc "*Risa* Casi puedo ver los símbolos de dólar en tus ojos, [mael]. No seas avaricioso."
    mc "De momento, he aceptado no recortar tu presupuesto. Aún tengo que encontrar tres millones anuales para las drogas de los clones."
    call BlinkXS4("c32s003_665") from _call_BlinkXS4_2213
    mael "Tenía que intentarlo..."
    mc "Y, en esta ocasión, yo tengo que negarme a aceptarlo. Quizás más adelante."
    stop music fadeout (1.5)
    mc "Pero sigamos. Tenemos un montón de trabajo pendiente."
    return
label c32s004_Eric:
    scene black with dissolve
    centered "{size=+20}{b}DÍA 52 – JUEVES{/b}{/size}"
    "Los días pasan demasiado rápido entre reuniones y diferentes tareas."
    "La remodelación de tu despacho empieza dos días después de hablar de ella con [car]."
    "Jamaal ya tiene las fotos de [ama]."
    scene c32s004_005a with dissolve
    "Y llega el día de enfrentarte a [erc]."
    play music ("music/AnxiousMarch.ogg")
    "[ama], [aar] y tú le visitáis en una sala habilitada para el interrogatorio. NTR no tiene una sala de interrogatorios como tal."
    "[eva] participa por videoconferencia."
    "El plan es que tú lleves el interrogatorio y ellos aporten preguntas que a ti se te puedan pasar. Están demasiado implicados emocionalmente."
    erc "*Risa* ¿Ez mi comité de ejecución?"
    "Su pronunciación, agravada por la falta de dientes, provoca un sonido siseante."
    aar "Cállate, [erc]."
    mc "Esto es una comisión de investigación. Aún no hay una sentencia."
    scene c32s004_005b with dissolve
    erc "Ezo no me lo ezperaba. Bueno, no me ezperaba zeguir vivo a eztaz alturaz."
    "Su mirada desafiante y su actitud de darle lo mismo lo que hagáis te congela la sangre en las venas."
    "Al mismo tiempo, hace que sientas un calor desagradable. Amenazó a tu familia. Posiblemente os hubiera matado si no hubiera sido por [ama] y [eva]."
    mc "Lo que tú esperaras es lo de menos. La empresa ya no se rige por los mismos principios que antes."
    mc "Estamos aquí para escuchar tu versión de lo que pasó en Newport. Tus compañeros lo han pedido y nosotros hemos aceptado."
    scene c32s004_005c with dissolve
    "Mira, risueño, a las cámaras apagadas en la pared, al fondo de la sala."
    erc "¿Ezoz perdedorez han pedido ezto? Eztoy muy zorprendido."
    erc "No zon capacez de atarze laz botaz zin que ze lo ordenen."
    call BlinkXS4("c32s004_010") from _call_BlinkXS4_2214
    eva "¿Le podemos disparar ya? Ha abierto la boca lo suficiente como para tener ganas de estar ahí y apretar yo misma el gatillo."
    mc "[eva], prometí una revisión justa del caso. No vamos a disparar a nadie. Aún."
    call BlinkXS4("c32s004_015") from _call_BlinkXS4_2215
    aar "¿Qué sabes de la operación de Portland?"
    aar "Los operativos que sobrevivieron sólo sabían lo que les había contado Enzo."
    scene c32s004_005d with dissolve
    erc "Yo no zé nada. Yo zólo cumplía órdenez."
    erc "Las órdenez noz fueron dadaz verbalmente a Enzo y a mí. No hay regiztro de ellaz."
    mc "Con lo que tenemos que creer en tu palabra, ¿no?"
    call BlinkXS4("c32s004_020") from _call_BlinkXS4_2216
    ama "¿De verdad le vas a creer?"
    mc "De momento tengo que creerle."
    call BlinkXS4("c32s004_025") from _call_BlinkXS4_2217
    "[ama] se tensa, reteniéndose de saltar la mesa y estrangular al mercenario que tiene delante."
    ama "¿Por qué los E estabais al mando de la operación?"
    scene c32s004_005e with dissolve
    erc "¿A quién iba a poner el Zr. Danielz al mando?"
    erc "Los C zon viejoz. Los D zon idiotaz. Los F... digamoz que zon demaziado jóvenez para una mizión azí."
    erc "Loz únicoz que podíamoz llevar a cabo el trabajo éramoz loz E."
    mc "¿Sabíais que la misión atentaba contra los principios fundacionales de NTR? ¿Contra la voluntad de los fundadores?"
    scene c32s004_005f with dissolve
    erc "No. No lo podíamoz zaber. Noz dijeron que [aar] y laz zorraz noz habían traicionado."
    call BlinkXS4("c32s004_030") from _call_BlinkXS4_2218
    eva "Matadlo ya, por favor. Esto es un paripé."
    mc "[eva]..."
    scene c32s004_005g with dissolve
    erc "Nueztraz órdenez eran eliminar a loz traidorez y a una familia que lez eztaba ayudando."
    erc "Zi hubiera dizpuezto de loz recurzoz que pedí, mi parte de la mizión ze hubiera completado."
    erc "Me zorprendí mucho cuando laz órdenez cambiaron y tuvimoz que azaltar tu caza para que firmaraiz aquellos papelez."
    mc "En aquel momento debiste saber que algo no iba bien, ¿no?"
    call BlinkXS4("c32s004_035") from _call_BlinkXS4_2219
    "[aar] no le deja contestar. Tiene otros intereses."
    aar "Sabemos que Enzo habló contigo por radio poco antes de morir. No me creo una palabra de que no supieras lo que estaba pasando."
    aar "¿Qué te dijo?"
    "Se está saltando el guion que habíais planificado."
    "No podías evitar que él, [ama] y [eva] estuvieran aquí, pero pensaste que era una mala idea desde el primer momento."
    scene c32s004_005h with dissolve
    erc "Conocíaz a Enzo. Era uno de los mejorez. Eztaba jodido. Ze le zalían las tripaz. Y tú habíaz ezcapado."
    erc "No podía confiar en loz F y loz G que quedaban para encontrarte y eliminarte."
    "Decides seguir la línea de interrogatorio de [aar]. Ya habrá tiempo de volver a Newport."
    mc "¿Por qué no podía confiar en ellos?"
    scene c32s004_005i with dissolve
    erc "Porque zon unoz inútilez zi no hay nadie para darlez órdenez."
    mc "Y sin embargo, son algunos de los que han pedido esta revisión."
    erc "Ez otra demostración de que zon tan idiotaz como loz D y tan blandoz como loz C."
    erc "Pero yo zoy inocente. Zólo cumplía órdenez."
    call BlinkXS4("c32s004_040") from _call_BlinkXS4_2220
    eva "¿Qué te dijo sobre mis hermanas?"
    eva "¿Cómo murieron?"
    scene c32s004_005j with dissolve
    erc "Murieron como perraz. Zé que Diana zuplicó por zu vida. Del rezto no zé nada."
    erc "Quizáz, zi ella hubiera tenido todavía laz doz piernaz para poder abrirlaz, Enzo le hubiera perdonado la vida."
    erc "Al menoz por un tiempo."
    "Ahora eres tú el que tiene que retenerse para no saltar la mesa y estrangularlo."
    call BlinkXS4("c32s004_045") from _call_BlinkXS4_2221
    ama "La pregunta es ¿por qué? Sabías que [aar] o nosotras éramos incapaces de traicionar a la empresa."
    ama "¿Qué os prometieron? Puedes hablar con sinceridad. Puedes ver que la cámara está apagada."
    scene c32s004_045d with dissolve
    "La cámara en la pared está apagada. Ni siquiera apunta a la mesa en la que estáis sentados."
    "Sabíais que, si grababais este interrogatorio preliminar, [erc] se iba a cerrar en banda."
    scene c32s004_005k with dissolve
    erc "Tu no lo entiendez. Erez una anomalía."
    if persistent.family:
        erc "Erez un clon que envejece a una velocidad normal."
    else:
        erc "No erez una de nozotroz, aunque te hayaz criado entre eztoz muroz."
    erc "El Zr. Danielz noz prometió un medicamento que pararía el envejecimiento zi cumplíamoz la mizión."
    call BlinkXS4("c32s004_050") from _call_BlinkXS4_2222
    aar "¿Y tú te lo creíste? ¡Ese medicamento no existe! Hay rumores desde hace años."
    aar "Creía que eras más inteligente que eso, [erc]. Un hijo de puta. Pero un hijo de puta inteligente."
    "No estás seguro de si llamar 'hijo de puta' a un clon que no ha tenido madre tendrá el mismo efecto que fuera de esta base."
    scene c32s004_005l with dissolve
    mc "Sólo os lo prometió a Enzo y a ti, supongo."
    erc "Por zupuezto. Éramoz loz que íbamoz a cargar con el pezo de la mizión, loz únicoz que zabíamoz lo que había en juego."
    scene c32s004_005m with dissolve
    erc "Pero eztoy zeguro de que eze medicamento exizte. ¿no?"
    "Puedes notar la duda en su voz. Parece que se está planteando si hicieron lo que hicieron persiguiendo un cuento de hadas."
    "Quizás es el momento de presionarle."
    mc "¿Los únicos que sabíais lo que había en juego? Con lo que cumplíais órdenes, pero sabíais que eran órdenes incorrectas."
    mc "Y todo por un medicamento que no existe."
    "Técnicamente es verdad. El medicamento no {b}detiene{/b} el envejecimiento."
    scene c32s004_005n with dissolve
    erc "¿De verdad no exizte? ¿Danielz noz engañó?"
    "Ya no es el Sr. Daniels."
    mc "Como CEO de la empresa te puedo asegurar que no tenemos nada que detenga el envejecimiento de los clones."
    call BlinkXS4("c32s004_055") from _call_BlinkXS4_2223
    eva "Matasteis a mis hermanas por nada, capullo. Traicionasteis a los fundadores por nada."
    eva "No había premio al final del arco iris para vosotros, aunque hubierais completado la misión."
    eva "Y vas a morir sabiendo que la cagaste por nada."
    scene c32s004_005o with dissolve
    erc "Danielz noz prometió que, cuando tomara el control total de NTR, tendríamoz ezoz medicamentoz."
    erc "Zi no exizten... ¿qué hubiera hecho?"
    mc "Supongo que lo mismo que le hizo a Arnau. Enzo y tú hubierais desaparecido sin dejar rastro."
    mc "Era una promesa que no podía cumplir."
    mc "Pero, lo siento por ti. Mucho."
    scene c32s004_060a with hpunch
    aar "¿Acabo de oírte decir que lo sientes por él? ¿Estás loco?"
    scene c32s004_060b with hpunch
    ama "Si no fuera por nosotras habría matado a la familia."
    scene c32s004_060c with hpunch
    eva "¡[gav] perdió el brazo por su culpa! ¡Y ya has oído como ha hablado de mis hermanas!"
    "Para [eva] es más fácil descargar en [erc] parte de la culpa que siente por el brazo de [gav]."
    scene c32s004_005o2 with dissolve
    "Entiendes el enfado de las chicas y de [aar], pero has detectado una grieta en la coraza de [erc] y es el momento de empujar."
    mc "Por lo que lo siento por ti es porque eres idiota."
    scene c32s004_005p with dissolve
    erc "¿Qué? ¡Zoy una víctima! ¡Fui engañado!"
    mc "Te engañaron en una parte, pero tú mismo te has delatado. Has dicho 'Cuando tomara el control total de NTR'."
    mc "Lo que indica que sabías lo que había en juego. Sabías lo que la misión representaba."
    mc "Sabías que estabas traicionando a los legítimos dueños de la empresa."
    scene c32s004_005q with dissolve
    erc "¿No lo haríaz tú zi pudieraz vivir maz añoz? Me da lo mizmo quien dirija la empreza zi podía ganar 20 añoz de vida."
    erc "Zi tuve que matar a Arnau, o zi teníamoz que matar a [aar] y a laz chicaz, era un precio pequeño a pagar."
    erc "Y zi morían algunoz F o G... en el fondo, zon prezcindiblez..."
    mc "Lo entiendo. Y por eso quiero anunciar ahora mismo que lo que sí existe es un medicamento que ralentiza el envejecimiento."
    scene c32s004_005r with hpunch
    aar "¿Qué? ¿Desde cuándo?" (multiple=2)
    erc "¡Entoncez exizte!\n¡Me haz engañado!" (multiple=2)
    mc "No te he engañado. Tu hablabas de un medicamento que lo detiene. Eso no existe. Este lo ralentiza."
    mc "Pero no te preocupes por la semántica. Tú no tendrás acceso a él."
    scene c32s004_005s with hpunch
    erc "¿Qué? ¿Por qué?"
    mc "Porque no completaste la misión. Porque Daniels no está al mando."
    mc "Porque, aunque pueda parecer cruel por mi parte, no voy a darle esa droga a alguien que traicionó los valores de la empresa."
    mc "Porque a partir de hoy no formas parte de la empresa. Menos aún siendo un asesino."
    scene c32s004_005t1 with dissolve
    erc "No matamoz a nadie en Newport."
    mc "Mataste a Arnau. Tú mismo lo has reconocido."
    scene c32s004_005t2 with dissolve
    erc "No tienez pruebaz. Mantendré mi verzión de que cumplía órdenez."
    mc "No eres muy listo, ¿verdad? Por mucho que desprecies a las otras series, creo que son mucho más inteligentes que tú."
    scene c32s004_005u with dissolve
    erc "¿De qué eztaz hablando?"
    mc "Te hemos dicho que este interrogatorio no se está grabando. Y no te hemos mentido."
    scene c32s004_005v with fade
    mc "Pero [eva] lo está retransmitiendo en directo a diversas salas en la base, donde lo están viendo tus excompañeros."
    scene c32s004_005w with fade
    mc "Puedes saludarlos a través de la cámara del portátil. Por cierto, todos llevan los cordones atados sin que nadie se lo ordene."
    scene c32s004_065a with fade
    "Te levantas de la silla sin dedicarle ningún pensamiento al asesino que tienes sentado delante."
    "No conociste a Arnau, pero, entre Daniels y él, te quitaron la oportunidad de hacerlo."
    mc "Creo que hemos acabado aquí. ¿Nos vamos?"
    erc "¡No puedez hacerme ezto!"
    scene c32s004_065b with fade
    "Recoges el portátil, porque decir que recoges a [eva] quedaría raro, y te diriges a la puerta sin esperar respuesta."
    "Te sientes como el detective pelirrojo de aquella serie de cuando eras un niño. Solo falta que la cabeza de [erc] explote a tu espalda."
    stop music fadeout (1.5)
    "La última vez que te sentiste así fue cuando conociste a la madre de [mad.nick]."
    scene c32s004_070a with fade
    play music ("music/ChillUkelele.ogg")
    call BlinkXS4("c32s004_070") from _call_BlinkXS4_2224
    aar "¿Cuándo ibas a decirnos lo del medicamento?"
    mc "Me enteré hace dos días de que existía. Ni Richards ni Daniels consideraron necesario dároslo."
    mc "Hoy he conseguido que [vin] asigne el dinero para fabricarlo."
    call BlinkXS4("c32s004_075") from _call_BlinkXS4_2225
    ama "¿De dónde va a salir el dinero? Tuvimos que rechazar algunas de las promesas que hiciste en la reunión con los operativos..."
    mc "He hablado con [mar] y con [nor]. Aceptarán un retraso en el cobro del dinero que la empresa les debe."
    mc "Eso dará para unos meses de tratamiento para todos los clones. Todos menos uno. Después de eso, ya encontraremos el dinero."
    call BlinkXS4("c32s004_080") from _call_BlinkXS4_2226
    eva "¡Hey! ¡Estoy aquí! ¿Podéis cambiarme de posición? Sólo veo el sobaco de [mc]."
    mc "Perdón, [eva]."
    call BlinkXS4("c32s004_085") from _call_BlinkXS4_2227
    eva "Gracias. Ya he cortado la retransmisión a las salas."
    eva "Me alegro mucho por los chicos, pero lo que más me alegra es cómo has llevado a [erc] a tu terreno."
    mc "Yo no he hecho nada. En el momento en que se ha sentido traicionado, él mismo se ha enterrado."
    call BlinkXS4("c32s004_090") from _call_BlinkXS4_2228
    eva "¿Cuándo lo vas a ejecutar? Espero que lo retrases hasta que esté ahí."
    mc "No voy a ejecutar a nadie, [eva]. Decidiremos qué hacer con él."
    mc "El cargo de asesinato debería ser suficiente para meterlo en una prisión... normal."
    call BlinkXS4("c32s004_095") from _call_BlinkXS4_2229
    ama "Pero no lo hemos grabado..."
    mc "Lo sé. No esperaba que confesara un asesinato en el primer interrogatorio."
    call BlinkXS4("c32s004_100") from _call_BlinkXS4_2230
    eva "*Tos* No lo {b}habéis{/b} grabado. Todos estos programas de videoconferencia tienen un pequeño botoncito rojo."
    eva "*Risita* Es posible que lo haya presionado por 'error'."
    mc "*Risa* A veces eres adorable, [eva]."
    call BlinkXS4("c32s004_105") from _call_BlinkXS4_2231
    aar "Los operativos de casi todas las series más mayores han visto el interrogatorio."
    aar "Creo que ellos también deberían opinar sobre qué hacer con [erc]. Ha dejado claro lo que piensa de ellos."
    mc "[aar], estamos haciendo cambios en la empresa, pero esto no es una democracia."
    mc "No voy a permitir que [erc] salga de esta sin un castigo sólo porque el resto de las series lo pida."
    call BlinkXS4("c32s004_110") from _call_BlinkXS4_2232
    aar "Lo entiendo, pero no te preocupes."
    aar "Después de lo que han escuchado, creo que pedirán un castigo más severo del que quieres aplicar."
    aar "Pero pienso que deberías escuchar sus propuestas, aunque no te ates a ellas."
    stop music fadeout (1.5)
    mc "Me parece una buena idea. Hablaré con [carl]. No quiero pasar por esto en una reunión con [dam]."
    return
label c32s004_routine:
    if _in_replay:
        call mrS3_sai_pregnant from _call_mrS3_sai_pregnant_5
        call mrS3_mar_pregnant from _call_mrS3_mar_pregnant_7
        call mrS3_emm_pregnant from _call_mrS3_emm_pregnant_4
        call mrS3_eri_pregnant from _call_mrS3_eri_pregnant_6
        call mrS3_nor_pregnant from _call_mrS3_nor_pregnant_6
        call mrS3_dap_pregnant from _call_mrS3_dap_pregnant_4
        call mrS3_sca_pregnant from _call_mrS3_sca_pregnant_6
        call mrS3_eil_pregnant from _call_mrS3_eil_pregnant_7
        call mrS3_sam_pregnant from _call_mrS3_sam_pregnant_5
        call mrS3_sim_pregnant from _call_mrS3_sim_pregnant_3
        call mrS3_oma_pregnant from _call_mrS3_oma_pregnant_6
        call mrS3_eva_pregnant from _call_mrS3_eva_pregnant_3
        call mrS3_mad_pregnant from _call_mrS3_mad_pregnant_3
        call mrS3_meg_pregnant from _call_mrS3_meg_pregnant_4
        call mrS3_ama_route from _call_mrS3_ama_route_25
        if ama._var("route"):
            call mrS3_ama_pregnant from _call_mrS3_ama_pregnant_1
        call mrS3_kim_pregnant from _call_mrS3_kim_pregnant_2
        call mrS3_kat_pregnant from _call_mrS3_kat_pregnant_1
        call mrS3_deb_pregnant from _call_mrS3_deb_pregnant_4
        call mrS3_lis_pregnant from _call_mrS3_lis_pregnant_3
        call mrS3_kia_pregnant from _call_mrS3_kia_pregnant_3
        call mrS3_bet_route from _call_mrS3_bet_route_15
        if bet._var("route"):
            call mrS3_bet_pregnant from _call_mrS3_bet_pregnant_3
    scene c32s004_115An with dissolve
    play music ("music/RhythmPlay.ogg")
    "Los días se suceden y cada vez consigues adaptar más tu agenda para acomodar más llamadas a casa."
    "Echas de menos a las chicas y a Jamaal, pero sobre todo echas de menos el sentimiento de una gran familia."
    call numberOfPregnanciesS3 (True, True, True, False, True, True, True, True, False, True) from _call_numberOfPregnanciesS3_2
    if mc._var("numberOfPregnancies") > 1:
        "Habláis de los bebés que están en camino y de cómo las diferentes chicas están llevando su embarazo."
    elif mc._var("numberOfPregnancies") > 0:
        "Habláis del bebé en camino y de cómo se está desarrollando el embarazo."
    "Habláis de cómo van las cosas en casa y habláis de la empresa."
    "Habláis de las preparaciones para la llegada de las estudiantes nuevas."
    "Y, cuando no hay nada nuevo de lo que hablar, tan sólo disfrutáis de poder veros y escucharos."
    scene c31s007_180c with fade
    "Mientras tanto, en la casa del CEO se ha instaurado una rutina nocturna."
    if not ama._var("route") and not bet._var("route"):
        "Todas las noches acabáis durmiendo los tres en tu cama, como reforzando el lazo familiar que os falta con las chicas de casa."
    else:
        "Algunas noches acabáis durmiendo los tres en tu cama, como reforzando el lazo familiar que os falta con las chicas de casa."
    if ama._var("route") and bet._var("route"):
        scene c32s004_120An1 with dissolve
        "El resto de las noches las repartes entre las dos mujeres con las que convives."
        "Algunas veces parece que se ponen de acuerdo en quién tiene que pasar la noche contigo."
        "En otras ocasiones, un beso en algún lugar de la casa acaba en tu habitación, mientras la otra mujer desaparece discretamente."
        "[ama] disfruta de su recién descubierta sexualidad, mientras que [bet] recupera los años perdidos."
        scene c32s004_125a with fade
        "El día que les propusiste un trío, sus miradas te hicieron pasar más miedo del que pasaste cuando [erc] entró en casa de [nor]."
        if mc._var("relationships")>2:
            "No todas las mujeres quieren hacer un trío con todas las otras chicas del harén."
        "El trío con [bet] y [ama] no se produjo durante vuestra estancia en Aruba."
    elif ama._var("route"):
        scene c32s004_120An2 with dissolve
        "El resto de las noches las pasas con [ama], que está disfrutando de su recién descubierta sexualidad."
        "[bet] suele desaparecer discretamente cuando ve que empezáis a besaros apasionadamente."
    elif bet._var("route"):
        scene c32s004_120An3 with dissolve
        "El resto de las noches las pasas con [bet], que está disfrutando de su recién redescubierta sexualidad y recuperando los años perdidos."
        "[ama] suele desaparecer discretamente cuando ve que empezáis a besaros apasionadamente."
    if bet._var("pregnant"):
        scene c32s004_125b with dissolve
        "Una mañana, después del desayuno, [bet] te informa de que está embarazada. Al final se ha decidido a hacer el test de embarazo."
        if ama._var("pregnant"):
            scene c32s004_125c with dissolve
            "Por la noche, es [ama] quien te informa de su embarazo."
    elif ama._var("pregnant"):
        scene c32s004_125c with dissolve
        "Una noche, después de cenar, [ama] te informa de que está embarazada."
    if persistent.family and ama._var("pregnant"):
        "Quiere hablar con [mael] para saber si hay alguna implicación por ser un clon. Por suerte, no la hay."
    scene c32s004_125d with fade
    "Salís los tres a cenar para celebrarlo al día siguiente."
    scene c31s007_180c with fade
    "Y la rutina continúa."
    scene c32s004_130b with fade
    call addProfileImageNoNotification (6, "oma_6", oma) from _call_addProfileImageNoNotification_192
    call addProfileImageNoNotification (6, "ama_6", ama) from _call_addProfileImageNoNotification_193
    call addProfileImageNoNotification (6, "mee_6", mee) from _call_addProfileImageNoNotification_194
    "Y, algunos domingos, las partidas de DnD continúan por videoconferencia."
    "[dap] ha convencido a todas las chicas para que se unan a las partidas."
    scene c32s004_130d with fade
    call addProfileImageNoNotification (6, "sim_6", sim) from _call_addProfileImageNoNotification_195
    call addProfileImageNoNotification (6, "meg_6", meg) from _call_addProfileImageNoNotification_196
    call addProfileImageNoNotification (6, "lis_6", lis) from _call_addProfileImageNoNotification_197
    "Es una forma de pasar más tiempo en familia y la mayoría de las chicas se unen encantadas."
    "Como era de esperar, la partida se convierte en un caos con tanta gente y [sca] deja de ser DM asistente para serlo a tiempo completo."
    scene c32s004_130c with fade
    call addProfileImageNoNotification (6, "bet_6", bet) from _call_addProfileImageNoNotification_198
    call addProfileImageNoNotification (6, "eil_6", eil) from _call_addProfileImageNoNotification_199
    call addProfileImageNoNotification (6, "kim_6", kim) from _call_addProfileImageNoNotification_200
    "Aunque la mayoría se hace personajes que se parecen a ellas, las elecciones de algunas de las chicas son extrañas."
    "Como, por ejemplo, la clériga de [bet] y su temible rodillo de combate."
    scene c32s004_130a with fade
    call addProfileImageNoNotification (6, "deb_6", kat) from _call_addProfileImageNoNotification_201
    call addProfileImageNoNotification (6, "kat_6", deb) from _call_addProfileImageNoNotification_202
    "O que [mar] decida que quiere jugar con el personaje de Marzia. O la enana de [deb.nick], obviamente, sin barba."
    "No todas las chicas encuentran el juego tan divertido como tú, pero todas continúan jugando."
    scene c32s004_130e with fade
    call addProfileImageNoNotification (6, "nor_6", nor) from _call_addProfileImageNoNotification_203
    call addProfileImageNoNotification (6, "eva_6", eva) from _call_addProfileImageNoNotification_204
    "Incluso [eva], que se enfada cada vez que su personaje falla un disparo 'fácil' con el arco. Fallar a una moneda a 50 pasos..."
    "Nadie quiere perderse lo que ha pasado en la partida y quedarse fuera de la conversación del día siguiente."
    scene c32s004_130f with fade
    call addProfileImageNoNotification (6, "sai_6", sai) from _call_addProfileImageNoNotification_205
    call addProfileImageNoNotification (6, "sam_6", sam) from _call_addProfileImageNoNotification_206
    "Y, a menos que sea por razones de trabajo, ninguna de las chicas quiere perderse una actividad en familia."
    "Comida en familia, tarde en la piscina, cena, y partida de DnD se convierten en vuestra rutina más de la mitad de los domingos."
    stop music fadeout (1.5)
    "Incluso una vez vuelvas a casa."
    return
label c32s004_MarSamArrival:
    if _in_replay:
        call mrS3_mar_route from _call_mrS3_mar_route_49
        if mar._var("route"):
            call mrS3_mar_pregnant from _call_mrS3_mar_pregnant_8
        call mrS3_sam_route from _call_mrS3_sam_route_26
        if sam._var("route"):
            call mrS3_sam_pregnant from _call_mrS3_sam_pregnant_6
        call mrS3_eva_route from _call_mrS3_eva_route_23
        if eva._var("route"):
            call mrS3_eva_pregnant from _call_mrS3_eva_pregnant_4
    scene black with dissolve
    centered "{size=+20}{b}DÍA 60 – VIERNES{/b}{/size}"
    scene c32s004_150a with fade
    play music ("music/Tiki-Bar-Mixer.ogg")
    "Cuando llevas poco más de tres semanas en la isla, aprovechando un viaje para llevar suministros a [eva], el avión trae un regalo de Newport."
    "Acudes al hangar junto con [ama] y [bet] a recibir vuestro regalo."
    scene c32s004_150b with fade
    "[mar] aparece en lo alto de la escalera tras unos eternos segundos de espera."
    if mar._var("route"):
        scene c32s004_150c with fade
        "Un momento después está entre tus brazos, presionando sus labios contra los tuyos."
    else:
        scene c32s004_150d with fade
        "Un momento después está entre tus brazos, dándote uno de esos abrazos que tanto has echado de menos."
    call BlinkXS4("c32s004_155") from _call_BlinkXS4_2233
    mom "Te he echado mucho de menos."
    mc "Yo también. Las tres semanas aquí se me han hecho más largas que los tres años en Portland."
    call BlinkXS4("c32s004_160") from _call_BlinkXS4_2234
    sam "*Risa* Espero que ese abrazo no le deje moretones en las costillas. No he traído el ungüento."
    if persistent.family:
        mc "Y yo espero que ocupes el lugar de mi madre mientras ella abraza a [bet] y a [ama]."
    else:
        mc "Y yo espero que ocupes el lugar de [mar] mientras ella abraza a [bet] y a [ama]."
    if sam._var("route"):
        scene c32s004_150e with fade
        "La enfermera ocupa tus brazos en el momento en que [mar] los deja libres. También tus labios."
    else:
        scene c32s004_150f with fade
        "La enfermera ocupa tus brazos en el momento en que [mar] los deja libres."
    call BlinkXS4("c32s004_165") from _call_BlinkXS4_2235
    sam "No sé si echaba más de menos estos abrazos o a ti. En casa nadie abraza tan bien como tú."
    mc "Yo echaba de menos las dos cosas. Y eso que Tía [bet] y [ama] abrazan muy bien."
    call BlinkXS4("c32s004_170") from _call_BlinkXS4_2236
    bet "Pero parece que nadie quiere abrazarme a mí. *Risa* ¡Me siento sola!"
    scene c32s004_170d with dissolve
    "Los abrazos entre las cuatro mujeres se suceden, y es el momento en que sientes tus brazos extrañamente vacíos."
    scene c32s004_170e with dissolve
    ama "Deberíamos irnos si queréis dejar las cosas en casa antes de que vayamos a comer."
    mom "Si es seguro dejar las maletas en el coche, no hace falta."
    mc "Todavía tenemos tiempo, ¿no? Hemos hecho la reserva para dentro de más de una hora."
    scene c32s004_170f with dissolve
    bet "Pero a lo mejor quieren ducharse y cambiarse antes de ir."
    mc "*Risa* Vale. Voy a llamar al restaurante y decirles que cambiamos la comida por una cena."
    sam "*Risa* No todas las mujeres tardamos dos horas en estar listas."
    mc "*Risa* Tienes razón. No todas las mujeres tardan tanto. Tú sí."
    sam "*Risa* Creo que voy a coger el avión de vuelta, si esta es la bienvenida que me espera."
    bet "Dejaos de bromas. Hay comida esperando."
    if mar._var("pregnant") and sam._var("pregnant"):
        scene c32s004_170g with dissolve
        mc "Antes de nada, ¿cómo están nuestras pequeñajas?"
    elif mar._var("pregnant"):
        scene c32s004_170i with dissolve
    elif sam._var("pregnant"):
        scene c32s004_170h with dissolve
    if mar._var("pregnant") or sam._var("pregnant"):
        if not mar._var("pregnant") or not sam._var("pregnant"):
            mc "Antes de nada, ¿cómo está nuestra pequeñaja?"
    if mar._var("pregnant") or sam._var("pregnant"):
        mom "Todo va genial. El martes acompañé a [sam.nick] al hospital y no hay nada de lo que preocuparse."
        sam "Estos padres primerizos... Hasta que no estés cambiando pañales no dejarás de preocuparte."
        mc "*Risa* Y entonces me preocuparé por otras cosas."
    scene c32s004_175a with fade
    "Una vez en el coche..."
    bet "Me alegró mucho cuando [mc] me dijo que veníais. Pero, ¿por qué habéis venido?"
    mc "*Risa* Ha sonado como si te molestara."
    scene c32s004_180a with dissolve
    mom "No le hagas caso, Tía [bet]."
    mom "Hacía siglos que [sam.nick] no tenía tres días libres seguidos."
    scene c32s004_185a with dissolve
    sam "Y [mar] no estará disponible a partir de la semana que viene, con la llegada de las estudiantes nuevas."
    sam "Cuando [eva] nos dijo que el avión volvía hoy y que podíamos aprovecharlo, no nos lo pensamos."
    mc "Recordadme que le dé un beso extra a [eva] la semana que viene."
    call BlinkXS4("c32s004_190") from _call_BlinkXS4_2237
    ama "¿Cómo está [eva]? A veces la noto rara por video conferencia, pero siempre me dice que no le pasa nada."
    ama "¿Sabéis algo más de las estudiantes nuevas? ¿Siguen mandando fotos?"
    scene c32s004_195a with dissolve #-2400
    mom "[eva] está bien, pero está muy cansada. Ahora tiene que hacer el trabajo que hacíais las dos y duerme muy poco."
    if eva._var("pregnant"):
        mom "Le hemos dicho que tiene que cuidarse y descansar, por el bebé, pero siempre dice que no tiene tiempo."
    mc "Bueno, cuando volváis el domingo os llevaréis a siete chicos que la ayudarán. Creo que eso le dará un poco de descanso." id c32s004_MarSamArrival_877b54bf
    scene c32s004_200a with dissolve #-2100
    sam "Estoy segura de que seguirá siendo una cabezona y no querrá descansar. Lo querrá hacer todo ella misma."
    sam "Y sobre las estudiantes nuevas..."
    mc "¿Qué pasa? ¿Hay algún problema con ellas? [eri] me dijo que eran muy simpáticas."
    scene c32s004_205a with dissolve #-1800
    mom "*Risa* [sam.nick] se siente un poco dejada de lado con ellas."
    mom "Desde que [eri] creó el grupo de WhatsUp para ellas, han ido entrando todas las chicas de casa."
    mom "Pero a las ancianas nos han dejado fuera."
    scene c32s004_210a with dissolve #-1500
    bet "Es normal. [nor] y tú sois sus caseras. [dap], [eri] y [sca] van a ser sus compañeras de piso hasta cierto punto."
    bet "Y las chicas de tu casa, incluyendo a [emm], [eil] y [sim] son estudiantes como ellas."
    mc "Si os sirve de consuelo, a mí tampoco me han metido en el grupo de WhatsUp. ¡Ni siquiera estoy en vuestro grupo!"
    call BlinkXS4("c32s004_215") from _call_BlinkXS4_2238
    ama "*Risa* ¿Dónde íbamos a poder criticarte si estuvieras?"
    mc "*Risa* ¿Usáis el grupo en el que no estoy para criticarme?"
    ama "*Risa* No me hagas responder a esa pregunta."
    mc "*Risa* Y tú no me hagas decirle a [geo] que te hackee el móvil y me mande los mensajes."
    scene c32s004_215d with dissolve
    todas "*Risa*"
    "[mar] y [sam] saben quién es [geo], y saben cómo son sus camisetas. Igual que saben quiénes son [mael], [cal], [dam] y [car]."
    "Incluso saben quién es [vin] y el tamaño que tienen sus manos."
    "Hablar de las personas a las que has conocido en Aruba no centra las conversaciones, pero es una parte de ellas."
    scene c32s004_220a with fade
    scene c32s004_220An with dissolve
    "Al final, ninguna de las dos mujeres necesita cambiarse, con lo que vais directamente al restaurante."
    "Vais a comer a un sitio que descubrió [bet]. Es la que más tiempo libre tiene de los tres y ha estado explorando la isla."
    "Especialmente los restaurantes."
    "Habláis sobre todo y sobre nada. La mayoría de lo que decís os lo habéis dicho previamente por videoconferencia."
    "Pero es agradable hacerlo en persona en vez de a través de una pantalla."
    "Hay muchas risas. También hay mucho más contacto del habitual. Como si todos quisierais aseguraros de que [mar] y [sam] están realmente allí."
    "Ni siquiera [bet] se queja porque el servicio sea lento. Todos disfrutáis del momento sin prisas."
    "La rama de la familia en Aruba ha crecido, aunque sólo sea por un par de días."
    "Es la excusa perfecta para cogerte tus primeros días libres desde que has llegado."
    stop music fadeout (1.5)
    scene c32s004_225d with fade
    "Al llegar a la casa del CEO, después de enseñarles un poco la ciudad, hay un coche de NTR esperándoos."
    play music ("music/ABCSong.ogg")
    "[aar] tiene cara de preocupación."
    call BlinkXS4("c32s004_225") from _call_BlinkXS4_2239
    mc "No esperaba verte aquí hoy."
    aar "No podía dejar de saludar a [mar]."
    mc "¿Y esa cara? ¿Ha pasado algo?"
    aar "Me preocupa que..."
    scene c32s004_230a with hpunch
    call BlinkXS4("c32s004_230") from _call_BlinkXS4_2240
    mom "¡No puede ser!"
    scene c32s004_235a with hpunch
    call BlinkXS4("c32s004_235") from _call_BlinkXS4_2241
    aar "Esto..."
    mom "¿Por qué no me habíais dicho que eras el clon de [mc]?"
    mc "No es algo que se pueda decir por videoconferencia."
    scene c32s004_240d with dissolve
    mom "Deja que te mire..."
    mom "No sé cómo no me di cuenta el día que te conocí..."
    mc "Sólo tenías ojos para [ama] y [eva]. Supongo que no nos miraste ni a [aar] ni a mí más de un segundo."
    mc "A ellas les pasó lo mismo, y lo conocen desde hace más tiempo."
    mc "Déjame que le presente a [sam.nick]."
    call BlinkXS4("c32s004_240") from _call_BlinkXS4_2242
    aar "*Susurrando* Gracias..."
    mc "No me lo agradezcas todavía."
    scene c32s004_245a with hpunch
    call BlinkXS4("c32s004_245") from _call_BlinkXS4_2243
    sam "Encantada de conocerte por fin, [aar]."
    aar "*Resignado* Igualmente, [sam]."
    sam "Llámame [sam.nick]."
    mc "*Risa* Te he dicho que no me lo agradecieras."
    scene c32s004_245d with dissolve
    "[bet] y [ama] miran la escena con expresiones risueñas que las otras dos mujeres no pueden entender."
    "[aar] y tú las entendéis perfectamente. Estás seguro de que han hecho apuestas sobre cuándo [aar] se acostumbrará a los abrazos de la familia."
    call BlinkXS4("c32s004_250") from _call_BlinkXS4_2244
    mom "[sam.nick], recuerda que no has traído el ungüento para los moretones."
    mc "*Risa* Eso suena a 'Suéltalo, que no lo he abrazado lo suficiente.'"
    call BlinkXS4("c32s004_255") from _call_BlinkXS4_2245
    mom "No es eso... del todo. Quiero hablar con [aar] de algunas cosas. Me parece que no se alimenta bien."
    mom "[ama], Tía [bet], y tú parece que sí que lo hacéis."
    call BlinkXS4("c32s004_260") from _call_BlinkXS4_2246
    bet "De nosotros se ocupa [car], aunque a veces pida combinaciones... controvertidas... en la pizza."
    bet "Creo que aún se está vengando por el día en que nos conocimos."
    call BlinkXS4("c32s004_265") from _call_BlinkXS4_2247
    ama "[aar] come lo mismo que el resto de los chicos."
    ama "Es nutritivo, pero ni es variado ni tiene nada que ver con lo que cocinas tú en casa, ... [mar]."
    call BlinkXS4("c32s004_270") from _call_BlinkXS4_2248
    mom "Si me decís qué ingredientes soléis usar, puedo diseñar menús semanales y mandároslos por email."
    mom "Al menos será comida más variada."
    scene c32s004_275An with dissolve
    "El pobre [aar] no sabe por dónde le están viniendo los tiros."
    "[mar] ni tan siquiera ha pisado la base de NTR y ya se quiere hacer cargo de la cocina."
    mc "Voy a ir bajando las maletas a vuestras habitaciones."
    call BlinkXS4("c32s004_280") from _call_BlinkXS4_2249
    stop music fadeout (1.5)
    sam "Te acompaño. *Susurrando* Tengo que pelearme contigo."
    play music ("music/Dark-Score.ogg")
    mc "¿Algo grave?"
    sam "*Susurrando* En privado."
    scene c32s004_285a with fade
    call BlinkXS4("c32s004_285") from _call_BlinkXS4_2250
    mc "¿Qué pasa, [sam.nick]?"
    sam "Estoy MUY enfadada contigo. Te dije que dejaras mis deudas en paz y que no quería que las pagaras."
    mc "No las he pagado. Las he comprado. Sabía que no querías que las pagara y no lo hubiera hecho a tus espaldas."
    call BlinkXS4("c32s004_290") from _call_BlinkXS4_2251
    sam "*Grrr* ¡Es casi lo mismo!"
    mc "No. Antes tenías cuatro préstamos con dos bancos diferentes."
    mc "Ahora tienes cuatro préstamos conmigo."
    call BlinkXS4("c32s004_295") from _call_BlinkXS4_2252
    sam "Y en vez de pagar más de $3,000 al mes en préstamos tengo que pagar $20. ¿Tú crees que es lógico?"
    mc "Yo lo hubiera dejado en un dólar al mes, pero [nor] pensó que era muy poco y que te ofenderías."
    mc "Lo dejamos en cinco dólares por préstamo."
    call BlinkXS4("c32s004_300") from _call_BlinkXS4_2253
    sam "¿Sois idiotas? ¿Creíais que no me iba a ofender con esto? ¡Te dije que no aceptábamos caridad!"
    mc "No es caridad. Vas a pagar todo lo que debes. Bueno, tú y tus herederos, durante los próximos cuatrocientos años más o menos."
    if sam._var("pregnant"):
        mc "Y si nuestro bebé quiere condonar su parte de la deuda cuando herede, será decisión suya. Se deberá dinero a sí mismo."
    call BlinkXS4("c32s004_305") from _call_BlinkXS4_2254
    sam "Voy a contestar a mi pregunta. Sí, sois idiotas. ¡No tenías por qué haberlo hecho!"
    if sam._var("route"):
        mc "Te equivocas. Si tengo los medios para que mi orgullosa y cabezota mujer pueda vivir más desahogada, no me voy a quedar de brazos cruzados."
    else:
        mc "Te equivocas. Si tengo los medios para que mi orgullosa y cabezota pseudo-madre pueda vivir más desahogada, no me voy a quedar de brazos cruzados."
    mc "No he pagado tus deudas. *Risa* Ahora me debes el dinero a mí y no voy a perdonarte ni un centavo."
    mc "Lo que me extraña es que no me hayas echado la bronca por videoconferencia."
    call BlinkXS4("c32s004_310") from _call_BlinkXS4_2255
    sam "No lo sabía. El primer cargo llegó ayer."
    sam "Los bancos sólo me habían avisado de que las deudas se habían subrogado a una empresa llamada MILFS. El nombre me pareció divertido."
    sam "No es la primera vez que me subrogan un crédito."
    call BlinkXS4("c32s004_315") from _call_BlinkXS4_2256
    sam "Cuando ayer vi los cargos, creía que había un error."
    sam "Hasta que vi que MILFS era el acrónimo de Marks Investment, Loan & Financial Services."
    sam "Como te iba a ver hoy, decidí no decir nada. Quería echarte la bronca cara a cara."
    mc "El nombre de la empresa fue idea de tu hijo."
    call BlinkXS4("c32s004_320") from _call_BlinkXS4_2257
    sam "¿Él estaba al tanto de esto? ¡Se va a quedar meses sin comer pastelillos!"
    mc "*Risa* Estoy tentado de decirte que sí solo para castigarlo."
    mc "Pero él solo sabía que iba a fundar una compañía financiera que iba a adquirir tus préstamos."
    mc "Mi idea inicial era que pudieras dejar de pagar si un mes lo necesitabas, pero [nor] pensó que rebajar la cuota sería mejor."
    mc "Nos dimos cuenta de que nunca dejarías de pagar, aunque tuvieras que comer ramen todos los días."
    call BlinkXS4("c32s004_325") from _call_BlinkXS4_2258
    sam "¡Por supuesto que no iba a dejar de pagar!"
    mc "Bueno, ahora no tienes por qué hacerlo. Son solo $20. *Risa* Y MILFS no te los va a perdonar."
    stop music fadeout (1.5)
    mc "Tú eres la primera clienta y [nor] actúa como administradora mientras estoy fuera, con lo que el nombre de la empresa va que ni pintado."
    call BlinkXS4("c32s004_330") from _call_BlinkXS4_2259
    play music ("music/RhythmPlay.ogg")
    sam "*Risa* ¡No lo había pensado! ¿Vas a ofrecer préstamos a todas las maduritas de Newport?"
    mc "*Risa* Aún no he decidido si voy a tener más clientes. Supongo que los emails de [mc]@milfs.com acabarían en la bandeja de spam de mucha gente."
    mc "Y muchos maridos tendrían que dar explicaciones a sus mujeres si reciben correo de MILFS."
    if sam._var("route"):
        call KissXS4("c32s004_335") from _call_KissXS4_41
    call BlinkXS4("c32s004_335") from _call_BlinkXS4_2260
    sam "Gracias por hacer esto, [mc]. Pero no vuelvas a hacer nada por el estilo sin mi consentimiento."
    mc "Si no pides préstamos nuevos, no tendré que volver a hacerlo."
    call BlinkXS4("c32s004_340") from _call_BlinkXS4_2261
    mom "Ah, estáis aquí. Os estaba buscando. [nor] me dio este paquete para ti."
    mc "¿Qué es?"
    mom "Como te decía en Navidad cuando eras un niño, ábrelo y lo sabrás."
    scene c32s004_340d with dissolve
    mc "*Risa*"
    "Solo a [nor] se le podría haber ocurrido hacer merchandising de la nueva empresa."
    mom "¿Qué pasa? Solo es una taza."
    scene c32s004_340e with dissolve
    mc "[nor] tiene ideas muy locas de vez en cuando."
    sam "*Risa* ¡Me encanta!"
    mom "No entiendo nada."
    mc "Es una larga historia. Aunque dudo que pueda convencer a [car] para que me haga el café en esta taza a partir de ahora."
    call BlinkXS4("c32s004_345") from _call_BlinkXS4_2262
    mom "Cuéntanos la historia durante la cena. Y tengo ganas de conocer a [car]. [ama] está hablando con ella ahora mismo."
    mc "¿Ha pasado algo?"
    mom "Le he pedido a [aar] que se quede a cenar, y no tenéis comida de verdad. [bet] me ha dicho que [car] envía la cena cada noche."
    call BlinkXS4("c32s004_350") from _call_BlinkXS4_2263
    bet "*Risa* No mientas, [mar]. No le has pedido que se quede. Casi le has obligado."
    bet "*Imitando a [mar]* 'Acabo de conocer al clon de mi niño. No voy a aceptar que te vayas a cenar rancho a la base.'"
    bet "*Imitando a [mar]* 'Y ahora vete a lavar las manos mientras voy a buscar a [mc]. Tengo algo que darle'"
    todas "*Risa*"
    scene c32s004_355a with fade
    scene c32s004_355An with dissolve
    "La cena transcurre entre risas e historias compartidas."
    "[sam] y [mar] alaban la elección de platos de [car], aunque se sorprenden de que [bet] solo tenga una pizza."
    "También explican un montón de historias antiguas de la familia. Algunas son embarazosas para ti."
    "[aar] las escucha todas ávidamente. Quizás es la primera vez que cena con una familia de verdad."
    "No será la última."
    scene c32s004_360An with dissolve
    "Después de cenar llegan las despedidas."
    "La incomodidad de [aar] con los abrazos sigue existiendo, pero esta noche ha hecho que, quizás, sea un poco más pequeña."
    "[mar] le pide que se una el día siguiente para la visita turística a la base y a la isla."
    stop music fadeout (1.5)
    "Para tu sorpresa, [aar] acepta encantado."
    return
label c32s005_MarSamThreesome:
    if _in_replay:
        call mrS3_mar_pregnant from _call_mrS3_mar_pregnant_9
        call mrS3_sam_pregnant from _call_mrS3_sam_pregnant_7
        call mrS3_mar_anal from _call_mrS3_mar_anal_1
        call mrS3_sam_blackPanther from _call_mrS3_sam_blackPanther_4
    scene c32s005_005a with fade
    "Después de cenar y de darte una ducha..."
    play sound ("music/knock.ogg")
    "*Knock-Knock*"
    mc "Pasad las dos."
    play music ("music/SensualJazzMedium2.ogg")
    scene c32s005_030a with fade
    sam "Aún me da miedo preguntar cómo sabes quién llama. O cómo sabes que estábamos las dos."
    mom "Hoy no me creo que sea porque has reconocido los nudillos."
    mc "Los nudillos eran los de [sam.nick]."
    mc "Pero sabía que no podríais decidir quién iba a dormir aquí hoy. Yo tampoco hubiera podido."
    mc "*Risa* Y, viendo cómo venís vestidas, no creo que tengáis mucha intención de dormir ninguna de las dos."
    scene c32s005_020d with fade:
        yalign 1.0
        linear 5.0 yalign 0.0
    pause (5.0)
    call BlinkXS4 ("c32s005_020") from _call_BlinkXS4_2264
    sam "*Risita* Al menos por un rato..."
    mc "Y supongo que ninguna estáis cansadas."
    scene c32s005_025d with fade:
        yalign 1.0
        linear 5.0 yalign 0.0
    pause (5.0)
    call BlinkXS4 ("c32s005_025") from _call_BlinkXS4_2265
    mom "*Risita* Para nosotras todavía es por la tarde."
    mc "*Risa* Bendito jet lag y benditas zonas horarias."
    scene c32s005_030b with dissolve
    mc "Pero ninguna de las dos habéis traído tacones... a veces os odio."
    sam "¡No cabían en la maleta!"
    mom "Mis tacones sí que cabían en la mía, pero no quería que [sam.nick] pareciera una enana."
    mc "[sam.nick], sabes que no hubieras pagado por exceso de equipaje si hubieras traído una maleta más grande, ¿no?"
    scene c32s005_030c with dissolve
    sam "Pero mis hijos se hubieran reído de mí si traigo una maleta grande para un fin de semana."
    mom "*Risa* Tienes que dejar de permitir que tus hijos dirijan tu vida. Eres una mujer casada."
    mc "Tú también. Y vuestro marido aún está esperando su beso."
    scene c32s005_035An with dissolve
    "Los besos con las dos mujeres se suceden rápidamente, durando lo justo para saciar el hambre, pero dejándote con ganas de más."
    "Lo que empezó como una broma entre ellas hablando de compartirte, se está convirtiendo en una realidad."
    "Una preciosa realidad."
    call BlinkXS4("c32s005_040") from _call_BlinkXS4_2266
    mom "¿Hace más calor de golpe o solo me lo parece a mí?"
    mc "*Risa* Estás en el Caribe. ¿Qué esperabas?"
    call BlinkXS4("c32s005_045") from _call_BlinkXS4_2267
    sam "No sé lo que pensará ella, pero yo espero que me empieces a desnudar."
    mc "Y nunca te ha gustado que te haga esperar."
    if persistent.family:
        mc "Pero si esto va de compartir, quiero compartir la tarea de desnudarte con mi madre."
    else:
        mc "Pero si esto va de compartir, quiero compartir la tarea de desnudarte con [mar]."
    call BlinkXS4("c32s005_050") from _call_BlinkXS4_2268
    mom "Yo empiezo por las medias, tú puedes empezar por dónde quieras."
    mc "*Risa* ¡Joder! Eso ha sido rápido y no he tenido que convencerte."
    mom "*Risa* Siempre te he dicho que el trabajo compartido se acaba antes. Y creo que [sam.nick] tiene prisa."
    scene c32s005_055An1 with dissolve
    "Con el trabajo repartido entre [mar] y tú, [sam] acaba casi desnuda en un santiamén."
    "Tan solo una fina capa de tela cubre su tesoro, y [mar] se aparta para dejarte finalizar el trabajo."
    if sam._var("naturalPubicHair"):
        scene c32s005_055An2 with dissolve
        "Cuando retiras las exiguas braguitas, aparece la mata de pelo que adoras."
    else:
        scene c32s005_055An3 with dissolve
        "Cuando retiras las exiguas braguitas, aparece el monte de venus perfectamente afeitado que adoras."
    call BlinkXS4("c32s005_060") from _call_BlinkXS4_2269
    mc "Preciosa como siempre..."
    sam "Y caliente como nunca..."
    sam "Pero ahora tienes a otra mujer que desnudar. Y no te pienso ayudar."
    call BlinkXS4("c32s005_065") from _call_BlinkXS4_2270
    mom "¡Eso no es justo!"
    call BlinkXS4("c32s005_070") from _call_BlinkXS4_2271
    sam "Quiero mirar cómo lo hace."
    sam "Quizás lo encontréis gracioso, pero me pone mucho la idea de veros juntos."
    if persistent.family:
        sam "Siempre he tenido un pequeño fetiche con el incesto y sois la primera pareja de madre e hijo que tengo la ocasión de ver."
    else:
        sam "Siempre he tenido un pequeño fetiche con el incesto y sois lo más parecido a una pareja de madre e hijo que voy a tener la ocasión de ver."
    mc "Si es por eso, no te preocupes. Voy a tener más ropa que disfrutar quitando."
    call BlinkXS4("c32s005_075") from _call_BlinkXS4_2272
    sam "Dadme un buen espectáculo..."
    mc "*Risa* Lo intentaremos."
    sam "Tómate tu tiempo..."
    call BlinkXS4("c32s005_080") from _call_BlinkXS4_2273
    mom "No voy a protestar por que se tome todo el tiempo del mundo."
    mom "No creo que pueda estar más cachonda de lo que estoy ahora mismo solo de pensarlo."
    scene c32s005_085a with dissolve
    "Sin responder a las provocaciones de las dos mujeres, decides empezar por retirar las medias de las larguísimas piernas de [mar]."
    scene c32s005_085b with dissolve
    mom "Hemos dicho que te tomes tu tiempo, pero no hace falta que vayas TAN lento. Me estás matando con la anticipación."
    sam "Deja que el chico disfrute del tacto de tu piel. Yo estoy disfrutando de las vistas."
    scene c32s005_085c with dissolve
    "La media desaparece demasiado rápido, dejando al descubierto la preciosa pierna."
    mc "La primera ya está. Vamos a por la segunda."
    mom "Espero que no tardes tanto como con la primera."
    call BlinkXS4("c32s005_095a") from _call_BlinkXS4_2274
    mc "¿Tienes prisa?"
    mom "No sé cómo responder a eso sin parecer una guarrilla."
    scene c32s005_090a with dissolve
    mc "Entonces no contestes."
    sam "*Risita* Creo que todos sabemos lo que ibas a contestar."
    scene c32s005_090b with dissolve
    "Te estás contagiando de la prisa inconfesa de [mar] y tus manos retiran la media más rápido que la anterior."
    call BlinkXS4("c32s005_095b") from _call_BlinkXS4_2275
    mom "Ya casi estás. Tienes la mitad del trabajo hecho."
    mc "Pero ahora viene lo más interesante. Y voy a tumbarte en la cama para ello."
    call BlinkXS4("c32s005_100") from _call_BlinkXS4_2276
    sam "Me gusta a dónde va esto. Estáis increíblemente sexis juntos, pero tumbados en la cama va a ser aún mejor."
    mc "Puedes unirte cuando quieras."
    sam "*Gemido* Lo haré, pero de momento me conformo con mirar."
    if sam._var("naturalPubicHair"):
        scene c32s005_110d with dissolve
    else:
        scene c32s005_110e with dissolve
    "No puedes evitar ver que la mano de la enfermera ha emprendido un viaje a su entrepierna y ha llegado a su destino."
    "Parece que la anticipación y alimentar su fetiche con el incesto están teniendo un efecto en ella."
    scene c32s005_115a with fade
    call BlinkXS4("c32s005_115") from _call_BlinkXS4_2277
    "Tumbas a [mar] en la cama para el siguiente paso en el proceso de desnudarla."
    "Te estás tomando tu tiempo, tal y como te han pedido, y tu polla empieza a estar incómoda dentro de tus shorts."
    mom "¿Vas a tardar mucho más o tenemos que empezar a desnudarte nosotras?"
    mc "En mi caso sólo hay una prenda y, aunque ahora mismo se sienta apretada, puedo esperar."
    scene c32s005_120An1 with dissolve
    "Levantas el... sujetador (o cómo se llame)... y un duro pezón te saluda con su presencia."
    scene c32s005_120c with dissolve
    "Tú lo saludas a él con tus labios."
    mom "*Gemido*"
    scene c32s005_120An2 with dissolve
    "Repites la operación con el otro pezón. Las dos mujeres cada vez están más impacientes, pero tú no lo estás menos."
    mom "*Jadeo*"
    call BlinkXS4("c32s005_125") from _call_BlinkXS4_2278
    "[sam] aparece por sorpresa detrás tuyo, abrazándote mientras presiona sus propios pezones contra tu espalda."
    sam "No puedo estar mirando más desde allí. Tengo que verlo desde más cerca."
    mc "Me extrañaba que tardaras tanto."
    scene c32s005_130a with dissolve
    mc "¿Has empezado a colaborar?"
    "[mar] se ha quitado el top (sí, acabo de mirar cómo se llama) mientras [sam] se ocupaba de distraerte."
    mom "La próxima vez voy a ponerte un límite de tiempo."
    "El último paso es eliminar las bragas del precioso conjunto."
    scene c32s005_130An with dissolve
    "En un movimiento que intentas alargar lo máximo posible, acabas retirando la fina tela que cubre tu destino."
    scene c32s005_130d with dissolve
    "Y no puedes evitar hundir tu cara en él una vez el tejido ha desaparecido."
    $ renpy.sound.play("music/MarMoan.ogg", loop=True)
    mom "*Gemido* Eso es un ataque a traición. *Jadeo* Pero [sam.nick]..."
    scene c32s005_135a with dissolve
    sam "Olvídate de mí. No voy a dejar que te tomes tu venganza y tardes una hora en desnudar a nuestro hombre."
    scene c32s005_135b with dissolve
    "La enfermera retira tus shorts hábilmente, dejando salir a Mjolnir de su estrecha prisión."
    sam "Tu hijo ya está más que preparado..."
    "[sam] empieza a lamerte las pelotas justo después de acabar la frase."
    scene c32s005_135c with dissolve
    mom "*Gemido* ¿Qué esperabas? *Jadeo*"
    sam "*Slurp*"
    mc "*Slurp*"
    scene c32s005_135d with dissolve
    mom "*Jadeo* ¡Parad un momento! *Gemido*"
    stop sound fadeout (1.5)
    scene c32s005_135e with dissolve
    mc "¿Qué pasa?"
    sam "¿Ha pasado algo?"
    mom "¿Eso del balcón es una cama?"
    scene c32s005_135f with dissolve
    sam "¿Tienes una cama en el balcón?"
    mc "Sí, pero no la he usado nunca."
    mom "Pues me parece que hoy es una buena oportunidad de hacerlo. Parece más grande que esta. ¿No crees, [sam.nick]?"
    mc "¿Queréis que cambiemos de cama JUSTO AHORA?"
    scene c32s005_135g with fade
    "Las dos mujeres se levantan y se dirigen al balcón."
    sam "Ni que tuviéramos demasiadas oportunidades de tener sexo mirando el Caribe."
    mom "¿Realmente vas a mirar el mar? Yo tengo cosas más interesantes que hacer."
    sam "Tienes razón..."
    scene c32s005_135h with dissolve
    sam "Eso es si nuestro hombre deja de mirarnos el culo, claro."
    mom "¿Vas a venir o nos vas a hacer esperar?"
    "No necesitas contestar a eso. No vas a perder tiempo haciéndolo."
    scene c32s005_140a with fade
    scene c32s005_140An with dissolve
    "Lo que sigue es una increíble sesión de besos, donde tener sólo una boca se convierte en un inconveniente."
    "Vas alternando tus labios de una mujer a otra mientras la cama se convierte en un laberinto de brazos y piernas."
    "Claro que la mujer que tiene sus labios libres no tarda en ocuparlos con otras zonas de tu piel."
    "Ninguna se acerca a Mjolnir durante el rato que duran los besos."
    scene c32s005_145a with dissolve
    "Pero cuando el calor de los besos empieza a amenazar con prender la cama en llamas, [mar] acaba con tu polla en la mano."
    mom "*Gemido* Lo siento, pero no aguanto más."
    sam "*Jadeo* Yo me he estado reteniendo..."
    mc "Yo aún tengo la boca libre..."
    scene c32s005_145b with dissolve
    "Mientras [mar] se mete tu polla en su boca, [sam] cabalga la tuya."
    $ renpy.sound.play("music/SamanthaMoan.ogg", loop=True)
    "No te referías a eso, pero no te vas a quejar. Y menos aún con la lengua fuera de la boca."
    sam "*Gemido* ¡Así! *Jadeo*"
    mom "*Slurp*"
    mc "*Slurp*"
    scene c32s005_900pv with dissolve
    show c32s005_900v
    "Las dos mujeres empiezan a turnarse para dedicar atenciones a tu polla, mientras tu lengua recorre cada pliegue del coño de [sam]."
    sam "*Gemido* ¡Joder! *Jadeo* ¡Echaba de menos esto! *Gemido*"
    "Por un segundo esperas que Jamaal asome su fea cara detrás de una palmera para decirle a su madre que tiene que poner un dólar en el tarro de los tacos."
    mom "*Jadeo* Disfrútalo, que luego será mi turno. *Gemido*"
    if persistent.family:
        "Cuando tu madre deja de lamer tu polla, su boca queda libre para hacer comentarios obvios."
    else:
        "Cuando [mar] deja de lamer tu polla, su boca queda libre para hacer comentarios obvios."
    scene c32s005_905pv with dissolve
    show c32s005_905v
    hide c32s005_900v
    "No tienes intención de que la noche acabe sin degustar el coño de [mar]."
    "Pero ahora es el momento de hacerlo con el de [sam]."
    sam "*Gemido* ¡Justo ahí! *Jadeo*"
    if sam._var("naturalPubicHair"):
        "Tu barba entrelazándose con la maravillosa mata de pelo de [sam] incrementa la sensación de ser acariciada por mil pequeños dedos."
    else:
        "Tu barba acariciando el depilado monte de Venus de [sam] incrementa la sensación de ser acariciada por mil pequeños dedos."
    mom "*Slurp*"
    scene c32s005_910pv with dissolve
    show c32s005_910v
    hide c32s005_905v
    "[mar] no tiene mucho más que añadir."
    "Está demasiado ocupada con su lengua recorriendo tu astil y controlando cuando la otra mujer se dobla sobre ti."
    if persistent.family:
        "Su cabeza aparece para introducirse tu polla en la boca durante unos segundos antes de liberarla de nuevo para que tu madre siga lamiendo."
    else:
        "Su cabeza aparece para introducirse tu polla en la boca durante unos segundos antes de liberarla de nuevo para que [mar] siga lamiendo."
    "Un sincronizado trabajo en equipo en el que [mar] dirige a Mjolnir donde debe estar en cada momento."
    "Ni en tus más húmedos sueños de adolescente hubieras pensado que estarías así con dos de las mujeres que te criaron."
    scene c32s005_915pv with dissolve
    show c32s005_915v
    hide c32s005_910v
    "Y menos aún en una isla del Caribe rodeados de palmeras bajo las estrellas."
    sam "*Gemido* ¿Cambiamos de posición? *Jadeo* Necesito eso dentro. *Gemido*"
    "La humedad del coño de [sam] empieza a superar la de tu lengua."
    mom "*Jadeo risueño* Alguien está impaciente. *Slurp* Cambiemos. *Jadeo*"
    "Sabes que llevarles la contraria sería una causa perdida. E 'impaciente' también se aplica a ti."
    if sam._var("naturalPubicHair"):
        scene c32s005_150a with fade
    else:
        scene c32s005_150b with fade
    "El cambio de posición parece prometedor, pero te parece que va a excluir un poco a [mar]."
    sam "*Gemido* ¿Vas a estar bien ahí abajo?"
    mom "*Jadeo* No te preocupes por mí y disfruta."
    if sam._var("naturalPubicHair"):
        scene c32s005_150An1 with dissolve
    else:
        scene c32s005_150An1 with dissolve
    if persistent.family:
        "Tu madre introduce tu polla en el coño de una de sus mejores amigas y se queda mirando su obra durante un segundo."
    else:
        "[mar] introduce tu polla en el coño de una de sus mejores amigas y se queda mirando su obra durante un segundo."
    sam "*Gemido* ¡Sí! *Gemido*"
    mom "*Jadeo* Estoy babeando solo de ver esto. *Gemido* Empieza a embestir, cielo. *Jadeo*"
    if sam._var("naturalPubicHair"):
        scene c32s005_920pv with dissolve
        show c32s005_920v
        hide c32s005_915v
    else:
        scene c32s005_925pv with dissolve
        show c32s005_925v
        hide c32s005_915v
    "Ese tipo de órdenes es mejor que cuando cualquiera de las dos te mandaba a hacer los deberes."
    sam "*GEMIDO* ¡Casi me corro! *JADEO*"
    "Al menos esta vez no te amenazarán sin golosinas si no terminas a tiempo. O posiblemente sí."
    mom "*Jadeo* Hazlo. *Gemido*"
    "Los gemidos de [mar] producen una sensación increíble cuando saca tu polla del coño de [sam] para metérsela en la boca."
    if sam._var("naturalPubicHair"):
        scene c32s005_930pv with dissolve
        show c32s005_930v
        hide c32s005_920v
    else:
        scene c32s005_935pv with dissolve
        show c32s005_935v
        hide c32s005_925v
    if persistent.family:
        "Tu madre espera impaciente su turno, mirando con la lengua fuera de su boca cómo perforas el coño de la enfermera."
    else:
        "[mar] espera impaciente su turno, mirando con la lengua fuera de su boca cómo perforas el coño de la enfermera."
    sam "*GEMIDO* ¡VOY A CORRERME! *JADEO* ¡ESTO SÍ QUE ES ALIMENTAR UN FETICHE! *GEMIDO*"
    "El cuerpo de [sam] se está tensando bajo tus dedos. Tener un fetiche con el incesto hace que su orgasmo se acerque rápidamente."
    mom "*Slurp*"
    "[mar] prefiere no decir nada. O no puede. O tiene la lengua fuera de la boca o tu polla dentro de ella."
    if sam._var("naturalPubicHair"):
        call OrgasmXS3("c32s005_155a") from _call_OrgasmXS3_80
    else:
        call OrgasmXS3("c32s005_155b") from _call_OrgasmXS3_81
    sam "*GEMIDO* ¡SÍ! *JADEO* ¡INCREÍBLE! *GEMIDO*"
    "Un orgasmo recorre el cuerpo de ébano justo cuando [mar] saca tu polla de su interior."
    "Sus fluidos salpican a la mujer que tiene entre sus piernas."
    mom "*GEMIDO* ¡Increíble! *GEMIDO*"
    "Parece que a [mar] no le importa."
    scene c32s005_940pv with dissolve
    show c32s005_940v
    hide c32s005_935v
    hide c32s005_930v
    "Y ella vuelve a meter tu polla en su amiga para que llegues al orgasmo que puede notar en sus dedos trepando por tu polla."
    sam "*GEMIDO* ¡DIOS MÍO! *JADEO* ¡ME ENCANTA! *GEMIDO*"
    "Tu límite se acerca rápidamente, impulsado por las contracciones del coño de [sam] y por la boca de [mar]."
    mom "*JADEO* Prepárate. *GEMIDO* ¡Aquí llega! *JADEO*"
    if persistent.family:
        "Es tu madre y te conoce mejor que nadie. Incluso en aspectos en los que no todas las madres conocen a sus hijos."
    else:
        "Es la mujer que te crió y te conoce mejor que nadie. Incluso en aspectos en los que no todas las madres conocen a sus hijos."
    if persistent.walkthrough:
        $ wt1 = _("Sin consecuencias.")
        $ wt2 = _("[sam] embarazada.")
    else:
        $ wt1 = ""
        $ wt2 = ""
    if persistent.pregnancy and not sam._var("pregnant"):
        menu:
            "Correrte dentro. Ir a por el bebé." (wt=wt2):
                $ sam._var("pregnant", True)
                $ sam._var("undiscoveredPregnancy", True)
                play sound ("music/OldMusicBox5.ogg")
            "Correrte dentro." (wt = wt1):
                pass
    if sam._var("naturalPubicHair"):
        call OrgasmXS3("c32s005_160a") from _call_OrgasmXS3_82
    else:
        call OrgasmXS3("c32s005_160b") from _call_OrgasmXS3_83
    mc "¡Mpfft!"
    "Sin poder contenerte más, explotas en el interior de [sam]."
    sam "*GEMIDO* ¡SÍ! *JADEO*"
    mom "*JADEO* ¡LLÉNALA! *GEMIDO*"
    stop sound fadeout (1.5)
    "Tu descarga de semen llena a la enfermera hasta que empieza a regalar por tu astil."
    scene c32s005_165a with fade
    call BlinkXS4("c32s005_165") from _call_BlinkXS4_2279
    "Cuando las respiraciones se normalizan..."
    mc "¿Ha sido suficiente para alimentar tu fetiche?"
    sam "Ha sido alucinante, pero... [mar] se ha quedado sin su ración..."
    if sam._var("naturalPubicHair"):
        call BlinkXS4("c32s005_170a") from _call_BlinkXS4_2280
    else:
        call BlinkXS4("c32s005_170b") from _call_BlinkXS4_2281
    mom "No te preocupes por mí. [mc] tiene mucha resistencia y un tiempo de recuperación muy rápido."
    mom "Y una polla que hay que limpiar."
    if sam._var("naturalPubicHair"):
        scene c32s005_170ad with dissolve
    else:
        scene c32s005_170bd with dissolve
    "[mar] se mete tu polla en la boca con la clara intención de mantenerte excitado, no solo de limpiarla."
    "Su lengua se entretiene en tu glande de una forma que no sería necesaria en una operación de limpieza."
    sam "Eso es super caliente. Creo que os voy a dejar un momento mientras voy a limpiarme."
    if persistent.lesbian:
        if sam._var("naturalPubicHair"):
            scene c32s005_170ae with dissolve
        else:
            scene c32s005_170be with dissolve
        "Una vez acaba de limpiar tu polla, [mar] te mira con una expresión muy fácil de leer."
        "No necesita palabras para preguntarte si le permites limpiar el coño de su amiga."
        menu:
            "Permitirlo.":
                $ mar._var("sam", True)
                if sam._var("naturalPubicHair"):
                    scene c32s005_170af with dissolve
                else:
                    scene c32s005_170bf with dissolve
                "En cuanto asientes con la cabeza, [mar] hunde su rostro entre los muslos de [sam] para sorpresa de esta."
                call BlinkXS4("c32s005_175") from _call_BlinkXS4_2282
                $ renpy.sound.play("music/SamanthaMoan.ogg", loop=True)
                sam "*JADEO* ¿QUÉ?"
                mc "No puedo negarle nada a mis chicas y lo sabes. ¿Qué tal lo hace?"
                call BlinkXS4("c32s005_180") from _call_BlinkXS4_2283
                sam "*GEMIDO* Sorprendentemente bien... *JADEO* Aunque tú eres mucho mejor. *GEMIDO*"
                mc "*Risa* No esperes que yo te haga una limpieza así."
                if sam._var("naturalPubicHair"):
                    scene c32s005_170ag with dissolve
                else:
                    scene c32s005_170bg with dissolve
                mom "*Slurp risueño*"
                "Crees que, a estas alturas, el coño de [sam] tiene que estar limpio como una patena. Pero [mar] sigue lamiendo."
                call BlinkXS4("c32s005_185") from _call_BlinkXS4_2284
                sam "*GEMIDO* [mar], para por favor. *JADEO* Estoy demasiado sensible. *GEMIDO*"
                if sam._var("naturalPubicHair"):
                    call BlinkXS4("c32s005_190a") from _call_BlinkXS4_2285
                else:
                    call BlinkXS4("c32s005_190b") from _call_BlinkXS4_2286
                stop sound fadeout (1.5)
                mom "Algún día no pararé. Notar tus fluidos mezclados con el semen de [mc] ha sido súper excitante."
                mc "Algún día, pero no hoy. Tampoco le podemos negar a [sam] el derecho a decidir parar."
                call BlinkXS4("c32s005_195") from _call_BlinkXS4_2287
                sam "Creo que no estaba preparada para esto. Voy al lavabo un momento."
            "No permitirlo":
                $ mar._var("sam", False)
    scene c32s005_195d with fade
    "Los dos seguís con la mirada a la enfermera de ébano tal y como se dirige al lavabo."
    sam "Podéis continuar sin mí. *Risita* Necesito un descanso."
    if mar._var("sam"):
        call BlinkXS4("c32s005_200") from _call_BlinkXS4_2288
        mom "¿Crees que he actuado muy impulsivamente?"
        mc "Cuando me has preguntado, creía que era algo de lo que habíais hablado."
        mc "Me he dado cuenta de que no lo era por cómo ha reaccionado [sam.nick]."
        mc "No creo que le haya desagradado, pero la sorpresa ha sido demasiado grande."
        call BlinkXS4("c32s005_205") from _call_BlinkXS4_2289
        mom "Mañana hablaré con ella del tema."
        mc "Supongo que es lo mejor. Pero ha sido muy excitante verte hacerlo."
        scene c32s005_205d with dissolve
        mom "*Risa* Puedo verlo."
    else:
        scene c32s005_205d with dissolve
        mom "Puedo ver que estás dispuesto a seguir las indicaciones de [sam.nick]."
    mc "*Risa* Eso ha sido culpa tuya y de tu lengua durante la limpieza."
    call BlinkXS4("c32s005_210") from _call_BlinkXS4_2290
    mom "Démosle un espectáculo para cuando vuelva."
    mc "¿Ya?"
    mom "Soy la única que está castigada sin un orgasmo. Y estoy cachondísima."
    mc "Cambiemos de posición para darle un mejor ángulo cuando llegue."
    scene c32s005_210d with fade
    mom "Así no podrá negarse a unirse."
    mc "Yo te aseguro que me uniría si fuera ella."
    mom "Espero que no tarde mucho en volver."
    call BlinkXS4("c32s005_215") from _call_BlinkXS4_2291
    sam "¿Aún no habéis empezado?"
    mc "Te estábamos esperando."
    sam "Empezad sin mí. Creo que me voy a quedar mirando un rato. Estáis increíbles."
    scene c32s005_215d with dissolve
    pause (1.5)
    scene c32s005_215e with vpunch
    "Es lo único que [mar] necesitaba oír como pistoletazo de salida."
    $ renpy.sound.play("music/MarMoan.ogg", loop=True)
    mom "*GEMIDO* ¡POR FIN! *JADEO*"
    "Ella se empala con fuerza en Mjolnir, que vuelve a estar tan duro como al principio de la noche."
    scene c32s005_975pv with dissolve
    show c32s005_975v
    hide c32s005_940v
    if persistent.family:
        "Mientras tu madre te cabalga con rapidez, impulsada por su excitación, [sam.nick] se sienta en el suelo a observaros mientras se acaricia."
    else:
        "Mientras [mar] te cabalga con rapidez, impulsada por su excitación, [sam.nick] se sienta en el suelo a observaros mientras se acaricia."
    mom "*GEMIDO* He estado esperando esto toda la noche. *JADEO*"
    "Su coño se cierra con fuerza sobre tu astil, como para dar más peso a sus palabras."
    sam "*JADEO* Yo también. *GEMIDO* Veros así es indescriptible. *JADEO*"
    "Nunca entenderás como pueden usar palabras como 'indescriptible' cuando tú apenas puedes hilvanar un par de pensamientos coherentes."
    if sam._var("naturalPubicHair"):
        scene c32s005_985pv with dissolve
        show c32s005_985v
        hide c32s005_975v
    else:
        scene c32s005_990pv with dissolve
        show c32s005_990v
        hide c32s005_975v
    "Que una mujer te cabalgue mientras la otra mira y se da placer es demasiado para tu cerebro."
    mom "*GEMIDO* ¡Más profundo! *JADEO* ¡Más duro! *GEMIDO*"
    "Aceleras cuanto puedes mientras la otra mujer sigue acariciándose."
    sam "*JADEO* Me encanta... *GEMIDO*"
    "Parece que veros a [mar] y a ti juntos le está provocando a [sam] el mismo placer que a vosotros estarlo."
    scene c32s005_980pv with dissolve
    show c32s005_980v
    hide c32s005_990v
    hide c32s005_985v
    "Descubrir ese fetiche incestuoso es una sorpresa hasta cierto punto."
    mom "*GEMIDO* ESTOY A PUNTO DE LLEGAR. *JADEO*"
    "Sus movimientos son algo más erráticos que hace un rato. Su excitación solo ha ido creciendo desde que han llegado a la habitación."
    sam "*JADEO* YO TAMBIÉN. *GEMIDO* ¡CORRÁMONOS A LA VEZ! *JADEO*"
    if persistent.lesbian:
        "Esperas que se refiera a ellas dos. A ti te queda un rato aún."
        call c32s005_lesbian from _call_c32s005_lesbian
    else:
        "Casi es un milagro que tu orgasmo llegue al mismo tiempo que el de las dos mujeres."
        if persistent.walkthrough:
            $ wt1 = _("Sin consecuencias.")
            $ wt2 = _("[mar] embarazada.")
        else:
            $ wt1 = ""
            $ wt2 = ""
        if persistent.pregnancy and not mar._var("pregnant"):
            menu:
                "Correrte dentro. Ir a por el bebé." (wt=wt2):
                    $ mar._var("pregnant", True)
                    $ mar._var("undiscoveredPregnancy", True)
                    play sound ("music/OldMusicBox5.ogg")
                "Correrte dentro." (wt = wt1):
                    pass
        if sam._var("naturalPubicHair"):
            scene c32s005_220An1 with dissolve
        else:
            scene c32s005_220An2 with dissolve
        hide c32s005_980v
        mc "¡Mpfft!"
        call c32s005_doubleOrgasm from _call_c32s005_doubleOrgasm
        stop sound fadeout (1.5)
        "El triple orgasmo simultáneo es casi sorprendente por el volumen de los gemidos de las dos mujeres."
        scene c32s005_240c with dissolve
        "Unos minutos después..."
    mom "Yo voy a necesitar ir al lavabo..."
    sam "Te acompaño."
    stop music fadeout (1.5)
    scene c32s005_260c with fade
    "Ves cómo las dos mujeres entran en la habitación y se dirigen al lavabo."
    play music ("music/Beach.ogg")
    "Unas vistas increíbles para terminar una noche increíble."
    scene c32s005_260d with fade
    "Y esperas a que vuelvan."
    "Y sigues esperando."
    scene black with dissolve
    "Y en algún momento tus ojos se cierran."
    scene c32s005_260e with fade
    "Y, cuando los vuelves a abrir, hay dos preciosas mujeres desnudas durmiendo a tu lado."
    "Vuelves a cerrarlos."
    scene black with dissolve
    stop music fadeout (1.5)
    call c32s005_saturday from _call_c32s005_saturday
    return
label c32s005_doubleOrgasm:
    sam "*GEMIDO* ¡SÍ! *JADEO*" (multiple=2)
    mom "*JADEO* ¡POR FIN! *GEMIDO*" (multiple=2)
    return
label c32s005_lesbian:
    if sam._var("naturalPubicHair"):
        scene c32s005_220An3 with dissolve
    else:
        scene c32s005_220An4 with dissolve
    call c32s005_doubleOrgasm from _call_c32s005_doubleOrgasm_1
    "El doble orgasmo simultáneo es casi sorprendente por el volumen de los gemidos de las dos mujeres."
    scene c32s005_980pv with dissolve
    show c32s005_980v
    "[mar] sigue cabalgándote mientras escuchas como [sam] sigue acariciándose para prolongar su orgasmo."
    mom "*GEMIDO* Sigue así... *JADEO*"
    "No tienes intención de parar, y los dos lo sabéis."
    sam "*GEMIDO* Una noche increíble... *JADEO*"
    if sam._var("naturalPubicHair"):
        call BlinkXS4("c32s005_225a") from _call_BlinkXS4_2292
    else:
        call BlinkXS4("c32s005_225b") from _call_BlinkXS4_2293
    hide c32s005_980v
    sam "Hacedme un poco de espacio. No puedo seguir mirando."
    mc "Estabas tardando en unirte."
    scene c32s005_230a with dissolve
    "Tras el cambio de posición..."
    sam "Si quieres..."
    if mar._var("sam"):
        sam "Antes me ha sorprendido que..."
    else:
        sam "Antes me ha parecido que..."
    scene c32s005_955pv with dissolve
    "[mar] ni siquiera contesta. Cambia su posición para llegar a los pezones de su amiga. Aunque para ello tenga que agarrarse a tu cuello."
    stop sound fadeout (1.5)
    mom "*Slurp*"
    $ renpy.sound.play("music/SamanthaMoan.ogg", loop=True)
    sam "*Gemido* Están muy sensibles..."
    show c32s005_955v
    "Tus caderas empiezan a bombear tras la interrupción para el cambio de posición, haciendo que la cara de [mar] se aplaste contra las tetas de [sam]."
    mom "*JADEO* *Slurp* *GEMIDO*"
    "Si la situación ha sido tórrida durante toda la noche, ahora lo es mucho más."
    sam "*GEMIDO* ¡POR DIOS! *JADEO* ¡ESTO ES DEMASIADO! *GEMIDO*"
    "Con una lengua en su coño y una boca en su pezón, la enfermera reanuda sus orgasmos."
    scene c32s005_945pv with dissolve
    show c32s005_945v
    hide c32s005_955v
    $ renpy.sound.play("music/MarMoan.ogg", loop=True)
    "[mar] la acompaña inmediatamente en los orgasmos compartidos, aplastando aún más su cara contra las tetas de su amiga."
    mom "*GEMIDO* *SLURP* *JADEO*"
    "Es una lástima no tener cámaras en el balcón."
    "[sam] tapa toda tu visión y tienes que imaginar lo que ocurre en base a lo que escuchas."
    sam "*JADEO* ¡OH, DIOS MÍO! *GEMIDO*"
    scene c32s005_950pv with dissolve
    show c32s005_950v
    hide c32s005_945v
    $ renpy.sound.play("music/SamanthaMoan.ogg", loop=True)
    "Con las dos mujeres experimentando orgasmo tras orgasmo, tan solo quedas tú por llegar a la meta."
    sam "*GEMIDO* ¡LLENA A TU MADRE! *JADEO*"
    "[sam] puede notar que estás a punto de tener un intenso orgasmo."
    mom "*JADEO* *SLURP* *GEMIDO*"
    "No puedes negarte a la petición 'silenciosa' de [mar]."
    if persistent.walkthrough:
        $ wt1 = _("Sin consecuencias.")
        $ wt2 = _("[mar] embarazada.")
    else:
        $ wt1 = ""
        $ wt2 = ""
    if persistent.pregnancy and not mar._var("pregnant"):
        menu:
            "Correrte dentro. Ir a por el bebé." (wt=wt2):
                $ mar._var("pregnant", True)
                $ mar._var("undiscoveredPregnancy", True)
                play sound ("music/OldMusicBox5.ogg")
            "Correrte dentro." (wt = wt1):
                pass
    call DoubleOrgasmXS3("c32s005_235") from _call_DoubleOrgasmXS3_4
    hide c32s005_950v
    $ renpy.sound.play("music/MarMoan.ogg", loop=True)
    mc "¡Mpfft!"
    sam "*JADEO* ¡SÍ! *GEMIDO*" (multiple=2)
    mom "*GEMIDO* ¡LLÉNAME! *JADEO*" (multiple=2)
    stop sound fadeout (1.5)
    "Descargas una gran cantidad de semen que se junta con los fluidos de sus orgasmos y empieza a bajar por tu polla."
    scene c32s005_240a with fade
    "Al cabo de unos minutos..."
    mc "Ha sido increíble."
    sam "No imaginaba que pudiera ser tan bueno."
    mom "Y no tiene por qué acabar aquí."
    mc "*Risa* Parece que alguien quiere recuperar un mes separados en una sola noche."
    if mar._var("anal"):
        call c32s005_anal from _call_c32s005_anal
    else:
        scene c32s005_240c with dissolve
        pass
    return
label c32s005_anal:
    scene c32s005_240b with dissolve
    mom "¿Has probado alguna vez por detrás?"
    sam "¡No! ¿Tú has visto lo grande que es Mjolnir?"
    mom "Lo he visto y lo he sentido. [mc] es muy cuidadoso."
    sam "Quizás algún día... Nunca he estado segura de si..."
    scene c32s005_240c with dissolve
    mom "¿Le hacemos una demostración?"
    mc "Creo que Mjolnir se acaba de despertar nada más oíros."
    sam "No hace falta, en serio. Yo estoy agotada y..."
    call BlinkXS4("c32s005_245a") from _call_BlinkXS4_2294
    mom "Puedes quedarte mirando como hace un rato. ¿Vienes, cielo?"
    mc "¿A la cama de dentro?"
    scene c32s005_240e with dissolve
    mom "No. Aquí. Y no hace falta que seas tan delicado como la última vez."
    mc "Imposible negarme viendo ese culo."
    call BlinkXS4("c32s005_245b") from _call_BlinkXS4_2295
    mc "¿Seguro que no quieres participar?"
    sam "Creo que me quedaré mirando. Pero desde muy cerca."
    scene c32s005_250An with dissolve
    "Te acercas a [mar] por detrás y penetras su culo en una sola embestida."
    $ renpy.sound.play("music/MarMoan.ogg", loop=True)
    mom "*GEMIDO* ¡UFFF! *JADEO*"
    "No es una venganza porque haya usado tu cuello como punto de apoyo hace un rato."
    scene c32s005_250c with dissolve
    sam "No me puedo creer que eso no haya dolido."
    mom "*Jadeo* Te lo juro. *Gemido* Supongo que llevar toda la noche tan excitada ayuda. *Jadeo*"
    mc "Y que hayas aprendido a relajar los músculos."
    mom "Puedes empezar a moverte cuando quieras."
    scene c32s005_960pv with dissolve
    show c32s005_960v
    "Bajo la atenta mirada de [sam], que ha agarrado tu astil, empiezas unas lentas embestidas en el culo de [mar]."
    mom "*GEMIDO* ¡ME ENCANTA! *JADEO* ¡LO QUE HACÉIS LOS DOS! *GEMIDO*"
    "Supones que la mano libre de [sam] está haciendo algo en [mar], pero no tienes forma de comprobarlo."
    sam "Si tú me has comido las tetas, no me vas a prohibir que te toque, ¿no?"
    "Ningún sonido sale de la boca de [mar] excepto más gemidos y jadeos."
    scene c32s005_965pv with dissolve
    show c32s005_965v
    hide c32s005_960v
    "Crees que te estás perdiendo algo en la evolución de la relación entre las dos mujeres."
    "Pero no es el momento de preguntar."
    mom "*JADEO* ¡SIGUE ASÍ! *GEMIDO*"
    sam "Visto desde aquí no da tanto miedo."
    "Quizás algún día se decida a probarlo. El tono de su voz deja claro que no será hoy."
    scene c32s005_970pv with dissolve
    show c32s005_970v
    hide c32s005_965v
    "El estrecho agujero de [mar] se cierra con fuerza sobre tu polla, indicando que su orgasmo se está acercando."
    mom "*GEMIDO* ¡ES ABRUMADOR! *JADEO*"
    "La fuerza de su esfínter hace que tu orgasmo también se acerque rápidamente."
    sam "Puedo notar cómo los dos estáis a punto de correros. ¡Es alucinante!"
    "Es tan alucinante como las sensaciones que recorren tu polla con cada embestida."
    scene c32s005_255An with dissolve
    hide c32s005_970v
    mom "*JADEO* ¡SÍ! *GEMIDO*"
    "[mar] se corre y su cuerpo se estremece de arriba a abajo con un fuerte orgasmo."
    mc "¡Mpfft!"
    "Su ano cerrándose sobre tu astil hace que tu orgasmo llegue inmediatamente."
    sam "¡Increíble!"
    stop sound fadeout (1.5)
    "Los dos os habéis olvidado de la enfermera por un segundo."
    scene c32s005_260a with fade
    "Retiras tu polla del estrecho agujero, del que sale una pequeña cantidad de semen bajo la atenta mirada de [sam]."
    sam "¡Me encanta ver esto!"
    return
label c32s005_saturday:
    centered "{size=+20}{b}DÍA 61 – SÁBADO{/b}{/size}"
    return
label c32s005_noThreesome:
    if _in_replay:
        call mrS3_mar_route from _call_mrS3_mar_route_50
        call mrS3_sam_route from _call_mrS3_sam_route_27
    scene c32s005_005a with fade
    "Después de cenar y de darte una ducha..."
    play sound ("music/knock.ogg")
    "*Knock-Knock*"
    mc "Pasa, [sam.nick]."
    play music ("music/RhythmPlay.ogg")
    scene c32s005_005b with fade
    mom "No solo está [sam.nick]."
    sam "Aún me da miedo preguntar cómo sabes quién llama."
    mc "¿Venís a dormir aquí las dos?"
    if mar._var("route"):
        scene c32s005_005c with dissolve
        mom "[sam.nick] quería dejarnos intimidad, pero sé que te echa de menos."
        sam "¡Hace casi un mes que no lo ves! Era lógico que quisierais pasar tiempo juntos..."
        mc "No te preocupes, pasaremos tiempo juntos."
        scene c32s005_005d with dissolve
        mom "*Risa* Seguramente te echaremos de la cama por la mañana. Hoy ha sido un día muy largo."
        mc "*Risa* Me parece que [sam.nick] ya está planificando fugarse de la cama antes de que nos despertemos."
        sam "*Risa* A mí nadie me echa de una cama si puedo evitarlo."
    elif sam._var("route"):
        scene c32s005_005e with dissolve
        if persistent.family:
            sam "Tu madre quería dejarnos intimidad, pero sé que te echa de menos."
        else:
            sam "[mar] quería dejarnos intimidad, pero sé que te echa de menos."
        mom "¡Hace casi un mes que no lo ves! Era lógico que quisierais pasar tiempo juntos..."
        mc "No te preocupes, pasaremos tiempo juntos."
        scene c32s005_005d with dissolve
        sam "*Risa* Hay una piscina con vistas al mar muy tentadora para pasar tiempo juntos."
        mc "*Risa* Hay dos, una en cada planta. Lo sabrías si no me hubieras querido echar la bronca."
        if persistent.family:
            mom "*Risa* Si no fuera porque sé que mi hijo es un dormilón diría que puede ser bonito al amanecer."
        else:
            mom "*Risa* Si no fuera porque sé que [mc] es un dormilón diría que puede ser bonito al amanecer."
    else:
        scene c32s005_005d2 with dissolve
        mom "Por supuesto." (multiple=2)
        sam "¿Acaso lo dudabas?" (multiple=2)
    mc "¿Queréis dormir dentro o en la cama del balcón?"
    scene c32s005_005f with dissolve
    mom "¿Tienes una cama en el balcón?"
    mc "Sí..."
    sam "¿No se moja?"
    mc "Está justo debajo de la piscina de la terraza y no se puede mojar."
    mc "Aún no la he usado nunca, pero supongo que debe ser muy agradable dormir escuchando el mar."
    scene c32s005_005g with dissolve
    pause (1.0)
    scene c32s005_005h with dissolve
    mom "En el balcón." (multiple=2)
    sam "Fuera." (multiple=2)
    scene c32s005_005i with fade
    "Pasáis un rato charlando, tan sólo por el placer de charlar."
    "Pero las dos mujeres caen rendidas al cabo de un rato. El día ha sido largo para ellas."
    scene black with dissolve
    stop music fadeout (1.5)
    call c32s005_saturday from _call_c32s005_saturday_1
    return
label c32s005_wakeUp:
    play music ("music/Beach.ogg")
    "Te despierta el sol sobre tu rostro, y al abrir los ojos te encuentras con [mar] mirándote."
    mc "Buenos días, ¿has dormido bien?"
    mom "He dormido genial. Tenías razón con lo de que era agradable dormir escuchando el mar."
    mc "¿Hace mucho que te has despertado?"
    if mar._var("route"):
        call BlinkXS4("c32s005_265") from _call_BlinkXS4_2296
    else:
        call BlinkXS4("c32s005_010b") from _call_BlinkXS4_2297
    mom "Hace un rato. Cuando [sam.nick] se ha ido."
    mc "¿Dónde está [sam.nick]?"
    if mar._var("route"):
        call BlinkXS4("c32s005_270") from _call_BlinkXS4_2298
    else:
        call BlinkXS4("c32s005_010c") from _call_BlinkXS4_2299
    mom "En la piscina de esta planta."
    return
label c32s005_MarLewd:
    if _in_replay:
        call mrS3_sam_route from _call_mrS3_sam_route_28
        call mrS3_mar_pregnant from _call_mrS3_mar_pregnant_10
    call BlinkXS4("c32s005_275") from _call_BlinkXS4_2300
    call c32s005_wakeUp from _call_c32s005_wakeUp
    mom "Me ha dicho que quería darnos intimidad cuando te despertaras."
    if sam._var("route"):
        mc "*Risa* Supongo que lo de ayer no le pareció lo suficientemente íntimo o que no quiere otro asalto."
        call BlinkXS4("c32s005_280") from _call_BlinkXS4_2301
        mom "Quiere otro asalto, pero a solas, como lo quiero yo."
        mom "Me ha dicho que, si tienes energías cuando acabes conmigo, te espera en la piscina."
    else:
        mc "A veces es adorable. Sobre todo, después de que le dijeras que por la mañana la echarías de la cama."
        call BlinkXS4("c32s005_280") from _call_BlinkXS4_2302
        mom "Es adorable casi siempre, menos cuando se pone en plan enfermera."
    stop music fadeout (1.5)
    mom "Pero ahora no es el momento de hablar de [sam.nick]. Quiero aprovechar esta intimidad."
    scene c32s005_285An with dissolve
    play music ("music/Too-Cool.ogg")
    "Iluminados por el naciente sol del Caribe, hacéis que vuestras bocas se encuentren."
    "Lo que empieza como unos tiernos besos, va subiendo de intensidad tal y como pasan los minutos."
    call BlinkXS4("c32s005_290") from _call_BlinkXS4_2303
    mom "*Gemido* No puedo esperar más. *Jadeo*"
    mc "Yo tampoco."
    scene c32s005_295a with fade #partir de la 805v
    "Apuntas tu polla al coño de [mar], duro como una piedra desde hace rato."
    mc "¿Preparada?"
    mom "Cuando quieras."
    scene c32s005_295b with hpunch
    $ renpy.sound.play("music/MarMoan.ogg", loop=True)
    mom "*GEMIDO* ¡Uff! *JADEO*"
    scene c32s005_800pv with dissolve
    show c32s005_800v
    "Empiezas a bombear con tus caderas, penetrando las húmedas entrañas de [mar]. No eres el único que se ha puesto cachondo con los besos."
    mom "*JADEO* ¡Justo así! *GEMIDO*"
    "Los besos continúan entre embestida y embestida. Nunca tenéis suficiente de la boca del otro."
    mom "*GEMIDO* ¡Me encanta! *JADEO*"
    "Sus húmedas paredes vaginales se cierran con fuerza sobre tu polla para corroborar sus palabras."
    scene c32s005_805pv with dissolve
    show c32s005_805v
    hide c32s005_800v
    "Cada una de tus embestidas producen un sonido húmedo que ninguno de los dos podéis oír, tapados por los gemidos de la mujer que tienes entre tus brazos."
    mom "*JADEO* ¡Echaba de menos estar a solas contigo! *GEMIDO*"
    "Ha sido duro estar un mes separados, y un fin de semana no puede compensarlo."
    "Pero tenéis que sacar el máximo de estos momentos juntos. Y pensáis hacerlo."
    mom "*GEMIDO* Necesito un cambio de posición. *JADEO* Me está entrando una rampa. *GEMIDO*"
    call BlinkXS4("c32s005_300") from _call_BlinkXS4_2304
    mc "*Risa* ¿Te falta entrenamiento?"
    mom "*Risa* Si mi marido no se hubiera ido al Caribe un mes..."
    mc "¿Cómo quieres ponerte?"
    mom "Mirando el amanecer. Es imposible hacerlo en casa."
    scene c32s005_305An with dissolve
    "Tras el cambio de posición, [mar] se empala en tu polla intentando perder el menor tiempo posible."
    mom "*GEMIDO* ¡Sigue! *JADEO*"
    scene c32s005_810pv with dissolve
    show c32s005_810v
    hide c32s005_805v
    "La posición, sin prácticamente apoyos, no es la más cómoda. Pero la compañía y el entorno son inmejorables."
    mom "*JADEO* Me encanta así. *GEMIDO*"
    "Las embestidas de tus caderas hacen que la hermosa mujer salte sobre tu polla en movimientos casi espasmódicos."
    "Atrapada entre tu pecho y tus manos en sus tetas, es como una muñeca con la que jugar."
    mom "*GEMIDO* ¡Justo ahí! *JADEO*"
    scene c32s005_815pv with dissolve
    show c32s005_815v
    hide c32s005_810v
    "Cada vez que la dejas caer, tu polla impacta contra su cérvix, en un impacto maravilloso."
    mom "*GEMIDO* *RESPIRACIÓN ENTRECORTADA*"
    "Cada uno de los impactos deja a tu esposa sin respiración."
    mom "*JADEO* *GEMIDO*"
    "Pese a lo incómodo de la posición, puedes notar cómo tu orgasmo empieza a trepar por tus pantorrillas."
    scene c32s005_820pv with dissolve
    show c32s005_820v
    hide c32s005_815v
    "También puedes notar cómo ella se va acercando al suyo con la misma inexorable fuerza con la que el sol se levanta."
    mom "*GEMIDO* Estoy a punto de correrme. *JADEO*"
    "La mayor diferencia es que tu esposa es mucho más bella de lo que cien amaneceres podrán ser nunca."
    "Lo sé. Cursi. Pero Trop me dijo que no me va a despedir por eso."
    mom "*JADEO* ¡Córrete dentro! *GEMIDO*"
    if persistent.walkthrough:
        $ wt1 = _("Sin consecuencias.")
        $ wt2 = _("[mar] embarazada.")
    else:
        $ wt1 = ""
        $ wt2 = ""
    if persistent.pregnancy and not mar._var("pregnant"):
        menu:
            "Correrte dentro. Ir a por el bebé." (wt=wt2):
                $ mar._var("pregnant", True)
                $ mar._var("undiscoveredPregnancy", True)
                play sound ("music/OldMusicBox5.ogg")
            "Correrte dentro." (wt = wt1):
                pass
    call OrgasmXS3("c32s005_310") from _call_OrgasmXS3_84
    mom "*GEMIDO* ¡SÍ! *GEMIDO*"
    mc "¡Mpfft!"
    "Los dos llegáis al orgasmo casi simultáneamente bajo el sol del Caribe."
    "Tu esposa es incapaz de retener todo tu semen dentro de ella."
    stop sound fadeout (1.5)
    scene c32s005_315a with fade
    call BlinkXS4("c32s005_315") from _call_BlinkXS4_2305
    "Tras unos minutos..."
    mc "Podría acostumbrarme a despertar así cuando vuelva a casa."
    mom "Allí no podríamos ver el amanecer."
    mc "*Risa* Pondré una bombilla naranja en mi habitación."
    call BlinkXS4("c32s005_320") from _call_BlinkXS4_2306
    mom "*Risa* No hace falta. Me gustaría igual si lo hiciéramos a oscuras."
    mc "A mí no. Verte es una de las mejores cosas de estar casados."
    call BlinkXS4("c32s005_325") from _call_BlinkXS4_2307
    if sam._var("route"):
        mom "Pues aún tienes que ver a otra de tus esposas. [sam.nick] te está esperando en la piscina."
        mom "Ella también se merece pasar un rato a solas contigo."
    else:
        mom "Pues vas a dejar de verme en breve. Deberías ir a ver a [sam.nick]."
    mom "Debe parecer una pasa después de tanto rato en remojo."
    mc "¿Qué vas a hacer tú?"
    call BlinkXS4("c32s005_330") from _call_BlinkXS4_2308
    call c32s005_marFarewell from _call_c32s005_marFarewell
    call KissXS4("c32s005_335") from _call_KissXS4_42
    call BlinkXS4("c32s005_335") from _call_BlinkXS4_2309
    mom "Hasta luego, mi amor."
    scene c32s005_335e with fade
    "Tu esposa se mete en la habitación, regalándote una última visión de su espectacular cuerpo."
    scene c32s005_335f with fade
    stop music fadeout (1.5)
    "Cuando desaparece, decides que es el momento de visitar la piscina."
    return
label c32s005_marFarewell:
    mom "Bueno, voy a darme una ducha. [ama] me pidió que le enseñara a hacer repostería."
    mc "Pero [car]..."
    if mar._var("route"):
        call BlinkXS4("c32s005_340") from _call_BlinkXS4_2310
    else:
        call BlinkXS4("c32s005_010j") from _call_BlinkXS4_2311
    mom "[ama] le pidió que no mandara desayuno hoy. Tía [bet] también nos ayudará."
    mc "*Risa* O se comerá los dónuts tal y como salgan del horno."
    mom "Es una posibilidad, pero entonces se quemará la lengua y no podrá hablar en todo el día."
    if sam._var("route"):
        mc "*Risa* Te veo luego. Voy a ver a [sam.nick]"
    else:
        mc "*Risa* Te veo luego. Yo también voy a darme una ducha y voy a ver a [sam.nick]"
    return
label c32s005_noMarLewd:
    if _in_replay:
        call mrS3_sam_route from _call_mrS3_sam_route_29
    call BlinkXS4("c32s005_010a") from _call_BlinkXS4_2312
    call c32s005_wakeUp from _call_c32s005_wakeUp_1
    if sam._var("route"):
        mom "Le he dicho que se quedara contigo en la cama, y que me iba a ir yo, pero ha dicho que lo de la piscina era muy tentador."
        mc "Iré dentro de un rato a verla."
        call BlinkXS4("c32s005_010d") from _call_BlinkXS4_2313
        mom "Mejor que vayas ahora."
        mc "Pero tú y yo no hemos tenido un rato para hablar a solas."
        call BlinkXS4("c32s005_010e") from _call_BlinkXS4_2314
        mom "Ya habrá tiempo para eso. Aún me queda un día y medio aquí."
        mom "Me siento lo suficientemente mal por no haberos dejado dormir juntos anoche."
        mc "No te preocupes por eso. Tanto [sam.nick] como yo lo entendemos perfectamente."
        mc "Aún os queda una noche aquí, y supongo que esta vez [sam.nick] no querrá compartir cama."
        call BlinkXS4("c32s005_010f") from _call_BlinkXS4_2315
        mom "*Risa* Aprovecharé para dormir con [ama]."
        mc "¿Qué tiene de divertido?"
        mom "*Risa* Que entiendo a [sam.nick]. Si hiciera un mes que no veo a mi marido, y no me refiero a tu padre..."
        mom "Seguramente lo hubiera despertado para tener sexo."
    else:
        mom "Ha dicho que quería darse un baño al amanecer."
        mc "Iré dentro de un rato a verla."
        call BlinkXS4("c32s005_010d") from _call_BlinkXS4_2316
        mom "Mejor que vayas ahora."
        mc "Pero tú y yo no hemos tenido un rato para hablar a solas."
        call BlinkXS4("c32s005_010g") from _call_BlinkXS4_2317
        mom "Ya tendremos tiempo para eso. Aún me queda un día y medio aquí."
        mc "Un día y medio pasa volando..."
        call BlinkXS4("c32s005_010f") from _call_BlinkXS4_2318
        mom "*Risa*"
        mc "¿Qué pasa?"
        mom "Me acabo de acordar de la fiesta de disfraces. Cuando... resolvimos... lo nuestro."
        mc "¿En qué has pensado?"
        call BlinkXS4("c32s005_010h") from _call_BlinkXS4_2319
        mom "En que, si hubiera acabado de otra forma, seguramente te hubiera despertado para tener sexo."
        mom "Entonces sí que hubiera pasado volando ese día y medio."
    mc "*Risa* ¡Qué directa eres!"
    call BlinkXS4("c32s005_010i") from _call_BlinkXS4_2320
    call c32s005_marFarewell from _call_c32s005_marFarewell_1
    stop music fadeout (1.5)
    return
label c32s005_pool1:
    "Al llegar a la piscina..."
    play music ("music/Beach.ogg")
    mc "Las vistas son espectaculares, ¿verdad?"
    if sam._var("route"):
        call BlinkXS4("c32s005_350") from _call_BlinkXS4_2321
    else:
        call BlinkXS4("c32s005_015a") from _call_BlinkXS4_2322

    sam "Buenos días, [mc]. Eran más chulas hace un rato, que el sol estaba más bajo en el horizonte."
    mc "¿Has dormido bien?"
    if sam._var("route"):
        call BlinkXS4("c32s005_355") from _call_BlinkXS4_2323
    else:
        call BlinkXS4("c32s005_015b") from _call_BlinkXS4_2324
    sam "He dormido muy bien. ¿Tú qué tal has dormido?"
    return
label c32s005_SamLewd:
    if _in_replay:
        call mrS3_mar_route from _call_mrS3_mar_route_51
        call mrS3_sam_pregnant from _call_mrS3_sam_pregnant_8
    scene c32s005_350d with fade
    call c32s005_pool1 from _call_c32s005_pool1
    if mar._var("route"):
        mc "Dudo que haya una mejor forma de dormir que con vosotras dos a mi lado."
    else:
        mc "He dormido genial."
    mc "Pero ahora creo que me merezco un rato a solas contigo."
    call BlinkXS4("c32s005_360") from _call_BlinkXS4_2325
    sam "Estoy totalmente de acuerdo con eso. Y nunca he tenido sexo en una piscina."
    if mar._var("route"):
        sam "Si te queda energía, claro. Desde esta piscina se escucha todo lo que pasa en el balcón de tu habitación."
        mc "*Risa* ¡Oops! Espero que no te hayas sentido demasiado abandonada."
        call BlinkXS4("c32s005_365") from _call_BlinkXS4_2326
        sam "Anoche te compartimos. Hoy queríamos un rato a solas contigo."
        sam "Yo no te hubiera dejado dormir tanto."
    sam "Además, llevo un rato esperando. Me voy a arrugar como una pasa."
    mc "¡Pero si acaba de salir el sol! Desde que estoy aquí, me levanto súper pronto."
    call BlinkXS4("c32s005_370") from _call_BlinkXS4_2327
    sam "Te levantas pronto, pero tardas mucho en entrar en la piscina..."
    mc "Entonces no se hable más."
    stop music fadeout (1.5)
    scene c32s005_375An with dissolve
    "Te quitas los shorts que te has puesto para hacer el corto recorrido de tu habitación a la piscina antes de entrar."
    play music ("music/Too-Cool.ogg")
    "Nunca sabes a quién te puedes encontrar si decides pasear desnudo por casa."
    scene c32s005_375d with dissolve
    "Sin mediar una palabra más, vuestros labios se unen en un apasionado beso."
    "La ingravidez que provoca el agua hace que la diferencia de altura con tu esposa prácticamente desaparezca."
    if sam._var("naturalPubicHair"):
        scene c32s005_375e with dissolve
        "Tu polla roza contra el abundante vello púbico de [sam]."
    else:
        scene c32s005_375f with dissolve
        "Tu polla roza contra el perfectamente depilado Monte de Venus de [sam]."
    call BlinkXS4("c32s005_380") from _call_BlinkXS4_2328
    sam "Parece que ya estás preparado."
    mc "Desde el momento en que has dicho que no habías tenido sexo en una piscina."
    mc "Si puedo ayudar a mi esposa a tener una experiencia nueva..."
    call BlinkXS4("c32s005_385") from _call_BlinkXS4_2329
    sam "Eso suena a que tú sí que has probado el sexo en una piscina..."
    mc "No voy a contestar a eso. Si no ha sido contigo, ahora mismo no cuenta."
    if sam._var("naturalPubicHair"):
        scene c32s005_390An1 with dissolve
    else:
        scene c32s005_390An2 with dissolve
    $ renpy.sound.play("music/SamanthaMoan.ogg", loop=True)
    "Penetras el coño de ébano con un movimiento de cadera. Su interior está tan caliente como dura está tu polla."
    sam "*Gemido* ¡Uff! *Jadeo*"
    call BlinkXS4("c32s005_395") from _call_BlinkXS4_2330
    sam "*Jadeo* Eso ha sido sorprendentemente rápido. *Gemido*"
    mc "Y tú ya estás extremadamente mojada. Y no me refiero al agua de la piscina."
    mc "Además, hace un momento decías que llevabas demasiado tiempo en la piscina."
    scene c32s005_855pv with dissolve
    show c32s005_855v
    "Empiezas un lento y rítmico embestir, ayudado por la ingravidez que el agua proporciona."
    mc "Y no queremos que te arrugues como una pasa."
    "La piscina de cristal es un lugar maravilloso para que tu esposa experimente con el sexo en el agua por primera vez."
    sam "*GEMIDO RISUEÑO* Tengo que recordarte que comas más fruta. *JADEO*"
    "Su faceta de madre y enfermera no desaparece ni siquiera mientras tu polla bombea dentro de su coño."
    scene c32s005_850pv with dissolve
    show c32s005_850v
    hide c32s005_855v
    "Su faceta de amante tampoco lo hace. [sam] es increíble."
    sam "*JADEO* ¡Me gusta! *GEMIDO*"
    "Pese a lo resbaladizo del suelo, [sam] es ligera como una pluma en el agua, lo que te permite moverla a lo largo de tu polla sin esfuerzo."
    sam "*GEMIDO* ¡Me encanta que me folles así! *JADEO*"
    "El sexo con [sam], casi siempre tierno, se ha convertido prácticamente en acrobático."
    scene c32s005_860pv with dissolve
    show c32s005_860v
    hide c32s005_850v
    "El coño de [sam] se empieza a cerrar con fuerza sobre tu polla mientras lo embistes hasta llegar al cérvix."
    sam "*JADEO* ¡MÁS DURO! *GEMIDO*"
    "Sigues al mismo ritmo. La posición y el agua entre vuestros cuerpos evita que puedas acelerar mucho más."
    "Y estás seguro de que, en la parte más profunda de la piscina, el sexo sería complicado para [sam]."
    stop sound fadeout (1.5)
    sam "*GEMIDO* Cambiemos de sitio. *JADEO*"
    scene c32s005_400d with fade
    "Parece que ella ha pensado lo mismo."
    "Cogiéndote de la mano, te dirige a una zona menos profunda, donde ella va a estar más cómoda."
    "Pero el agua entre ambos va a ser la misma."
    scene c32s005_400a with fade
    call BlinkXS4("c32s005_400") from _call_BlinkXS4_2331
    sam "*Gemido* Aquí. *Jadeo* Ponte detrás. *Gemido*"
    "Su respiración se ha normalizado un poco durante el recorrido."
    scene c32s005_405An with dissolve
    "Sigues sus instrucciones y te pones detrás suyo, penetrándola rápidamente para que no pierda la excitación."
    $ renpy.sound.play("music/SamanthaMoan.ogg", loop=True)
    sam "*GEMIDO*"
    scene c32s005_865pv with dissolve
    show c32s005_865v
    hide c32s005_860v
    "Empiezas a bombear con fuerza. Con el agua poco por encima de tu cintura, es mucho más fácil acelerar el ritmo."
    sam "*GEMIDO* ¡ASÍ MUCHO MEJOR! *JADEO*"
    "Ayudado por el agarre en sus brazos, embistes con toda la fuerza que las toneladas de agua que os rodean te permiten."
    sam "*JADEO* QUÉ BUENO ERES CUANDO NO ERES TIERNO. *GEMIDO*"
    "Te pilla totalmente por sorpresa. Siempre habías pensado que a [sam] le gustaba el sexo tierno."
    scene c32s005_875pv with dissolve
    show c32s005_875v
    hide c32s005_865v
    "No dejas de embestir con fuerza en el coño de la enfermera."
    "Si hoy lo prefiere más duro de lo habitual, es una buena oportunidad para hacerlo."
    sam "*GEMIDO* ¡JUSTO ASÍ! *JADEO* VOY A CORRERME EN CUALQUIER MOMENTO. *GEMIDO*"
    "A ti te queda aún un rato para llegar al orgasmo."
    "Pero con la velocidad de tus embestidas, ese rato se está acortando."
    call OrgasmXS3("c32s005_410") from _call_OrgasmXS3_85
    sam "*JADEO* ¡SÍ! *GEMIDO* ¡SIGUE! *JADEO*"
    "El orgasmo de tu esposa hace que su coño se cierre con fuerza sobre tu polla y sus fluidos se mezclen con el agua de la piscina."
    scene c32s005_870pv with dissolve
    show c32s005_870v
    hide c32s005_875v
    "Continúas embistiendo contra el estrecho coño que estruja tu astil como un húmedo guante."
    sam "*GEMIDO* ¡NO VOY A PODER AGUANTAR DE PIE MUCHO MÁS! *JADEO*"
    "Por suerte para ella, no va a tener la oportunidad de hacerlo. Tu orgasmo está recorriendo tus piernas velozmente."
    sam "*JADEO* ¡CÓRRETE DENTRO! *GEMIDO*"
    "No pensabas hacerlo en otro sitio. No quieres imaginar hilos de semen flotando en la piscina."
    if persistent.walkthrough:
        $ wt1 = _("Sin consecuencias.")
        $ wt2 = _("[sam] embarazada.")
    else:
        $ wt1 = ""
        $ wt2 = ""
    if persistent.pregnancy and not sam._var("pregnant"):
        menu:
            "Correrte dentro. Ir a por el bebé." (wt=wt2):
                $ sam._var("pregnant", True)
                $ sam._var("undiscoveredPregnancy", True)
                play sound ("music/OldMusicBox5.ogg")
            "Correrte dentro." (wt = wt1):
                pass
    call OrgasmXS3("c32s005_415") from _call_OrgasmXS3_86
    hide c32s005_870v
    mc "¡Mpfft!"
    "Cuando por fin llega tu orgasmo, vacías tus pelotas en el interior del coño de tu esposa."
    sam "*JADEO* ¡OH, SÍ! *GEMIDO*"
    "Os quedáis inmóviles unos momentos mientras vuestras respiraciones se normalizan después de los poderosos orgasmos."
    stop sound fadeout (1.5)
    scene c32s005_420a with fade
    call BlinkXS4("c32s005_420") from _call_BlinkXS4_2332
    "Abrazas por detrás a la diosa de ébano para darle el apoyo que sus piernas ya no le proporcionan."
    sam "Ha sido alucinante..."
    sam "¿Crees que nos habrán oído?"
    mc "*Risa* Estoy seguro de que sí."
    mc "Si en tus dónuts hay algún mensaje escrito con chocolate, tipo 'Ahhh', ya sabrás por qué es."
    call BlinkXS4("c32s005_425") from _call_BlinkXS4_2333
    sam "¿Mis dónuts? ¿Qué quieres decir?"
    call c32s005_donuts from _call_c32s005_donuts
    scene c32s005_425d with dissolve
    "La giras y la besas apasionadamente antes de que se vaya."
    stop music fadeout (1.5)
    "Está siendo una mañana fantástica."
    return
label c32s005_donuts:
    if persistent.family:
        mc "Mi madre y [ama] van a hacer repostería para desayunar. Con Tía [bet] robando ingredientes."
    else:
        mc "[mar] y [ama] van a hacer repostería para desayunar. Con Tía [bet] robando ingredientes."
    sam "Entonces será mejor que me olvide de la piscina y me duche antes de que [bet] nos deje sin desayuno."
    mc "Te veo arriba entonces."
    return
label c32s005_noSamLewd:
    if _in_replay:
        call mrS3_mar_route from _call_mrS3_mar_route_52
    scene c32s005_015a with fade
    call c32s005_pool1 from _call_c32s005_pool1_1
    mc "Genial. Tenemos que repetir lo de dormir los tres juntos cuando volvamos a casa."
    if mar._var("route"):
        call BlinkXS4("c32s005_015f") from _call_BlinkXS4_2334
        sam "Aunque me he sentido un poco culpable por no haberos dejado la cama para los dos."
        mc "No hay problema, [sam.nick]. Las dos estabais cansadas después del viaje."
        call BlinkXS4("c32s005_015c") from _call_BlinkXS4_2335
        sam "*Risa* Y tener sexo de reencuentro estando cansados no es lo mejor."
        mc "*Risa* Nope."
        call BlinkXS4("c32s005_015d") from _call_BlinkXS4_2336
        sam "Pues espero que no se canse demasiado hoy. Ya he hablado con [bet] y hoy dormiré con ella."
        mc "*Risa* No sé si agradecértelo o decirte que no hace falta."
        call BlinkXS4("c32s005_015e") from _call_BlinkXS4_2337
        sam "Mejor no digas nada. Desde esta piscina se escucha todo lo que pasa en el balcón de tu habitación."
        mc "*Risa* ¡Oops!"
    else:
        call BlinkXS4("c32s005_015f") from _call_BlinkXS4_2338
        sam "Espera, que salgo."
    call BlinkXS4("c32s005_015g") from _call_BlinkXS4_2339
    call c32s005_donuts from _call_c32s005_donuts_1
    scene c32s005_425e with fade
    stop music fadeout (1.5)
    "Antes de subir a comprobar cómo van los progresos con la repostería, pasas por tu habitación y compruebas el móvil."
    "Parece que va a haber una nueva actualización en breve y Clichecita ha publicado una previsualización."
    "Te recuerda a alguien, aunque no tienes claro a quién."
    return
label c32s006_AmaSecTeam:
    if _in_replay:
        call mrS3_mar_route from _call_mrS3_mar_route_53
        call mrS3_sam_route from _call_mrS3_sam_route_30
        if sam._var("route"):
            call mrS3_sam_pregnant from _call_mrS3_sam_pregnant_9
        call mrS3_salary from _call_mrS3_salary
    scene c32s006_005a with fade
    play music ("music/RhythmPlay.ogg")
    "Pasáis el día en familia, empezando con una visita a la empresa a la que [sam] no acude por recomendación de [ama]."
    "No existe un protocolo de visitas en la empresa y que la visite [mar] tiene lógica dado que es propietaria."
    "Pero [ama] no sabe cómo encajar a [sam] en los protocolos de seguridad."
    scene c32s006_005d with fade
    "[sam] no tiene ningún problema en quedarse en casa disfrutando del sol del Caribe mientras os espera."
    if sam._var("pregnant"):
        "Se está convirtiendo en toda una experta en la preparación de cócteles sin alcohol."
    scene c32s006_005b with fade
    "[mar] y [car] parecen encajar desde el primer momento. Se intercambian los correos electrónicos para mandarse recetas de cocina."
    scene c32s006_005c with fade
    "[aar] se une a vosotros durante la visita y es recibido con abrazos."
    "Es raro verlo vestido con algo diferente al uniforme habitual."
    scene c32s006_005e with fade
    "Al llegar a la sala de clonación, [mar] estalla en lágrimas."
    if persistent.family:
        "Ver el lugar en el que nacieron [eva] y [ama] es una experiencia dura para ella."
    else:
        "Ver el lugar en el que nacieron [emm], [dap] y [eri] es una experiencia dura para ella."
    scene c32s006_005f with fade
    "También es el lugar en el que nació [aar]."
    "Es la primera vez que ves a [aar] devolver un abrazo a alguien que no sea [ama] con una sonrisa en la cara."
    "Es una sonrisa triste, pero es una sonrisa."
    scene c32s006_010a with fade
    "Después de visitar la empresa, recogéis a [sam] para la visita a la isla y recorréis los preciosos paisajes de la isla."
    scene c32s006_010bAn with fade
    "Visitáis todas las atracciones turísticas que os da tiempo."
    scene c32s006_010c with fade
    "Y acabáis por pasando la tarde en una de las paradisiacas playas."
    "[mar], [sam], y [bet] insisten en embadurnaros a todos con crema solar."
    "[aar] te mira como preguntándote si siempre lo van a tratar como a un niño. Te encojes de hombros. Algún día se acostumbrará."
    "Mientras él sufre, disfrutas de las manos de [sam] recorriendo tu espalda."
    if mar._var("route") and sam._var("route"):
        if sam._var("naturalPubicHair"):
            scene c32s006_015An1a with dissolve
        else:
            scene c32s006_015An1b with dissolve
        "Y, por la noche, se vuelve a repetir la escena del día anterior."
        if persistent.lesbian:
            scene c32s006_015An2 with dissolve
            "Para sorpresa de nadie, la interacción entre las dos mujeres se vuelve más intensa después del experimento de la primera noche."
    elif mar._var("route") or sam._var("route"):
        if mar._var("route"):
            scene c32s006_020An with dissolve
            "Y, por la noche, [sam] decide dormir con [bet], dejándoos la cama a [mar] y a ti."
        else:
            scene c32s006_025An with dissolve
            "Y, por la noche, [mar] decide dormir con [ama], dejándoos la cama a [sam] y a ti."
    else:
        scene c32s006_030a with fade
        "Y, por la noche, vuelves a dormir con [mar] y [sam] bajo las estrellas."
    if mar._var("route") or sam._var("route"):
        "Es vuestra última noche juntos por una temporada, y ninguno de vosotros tiene prisa en dormir."
    scene black with dissolve
    centered "{size=+20}{b}DÍA 62 – DOMINGO{/b}{/size}"
    call BlinkXS4("c32s006_035") from _call_BlinkXS4_2340
    "El día siguiente, el día de la partida, llega demasiado pronto."
    ama "Les he dicho a los chicos del equipo de seguridad que estén aquí en una hora para presentároslos."
    ama "Después iremos al aeropuerto. Volarán con vosotros de vuelta a Newport."
    mc "¿A quién has escogido finalmente?"
    call BlinkXS4("c32s006_040") from _call_BlinkXS4_2341
    $ ces = TGCharacter ("Cesar", color = "#163300")
    $ fra = TGCharacter ("Frank", color = "#363330")
    $ hen = TGCharacter ("Henry", color = "#ff3300")
    $ isr = TGCharacter ("Isard", color = "#e3ff00")
    $ jan = TGCharacter ("Jan", color = "#e3ff00")
    $ kei = TGCharacter("Keylor", color="#0BCDF4")
    ama "He escogido a chicos de diferentes series. [ces], [dam], [fra], [hen], [isr], [jan] y [kei]. Así no habrá problemas si los ven juntos. "
    ama "Y, si se producen confusiones cuando se haga el relevo con otros chicos de la misma serie, siempre pueden pasar por gemelos."
    mc "*Risa* ¿Tenías ganas de deshacerte de [dam]?"
    call BlinkXS4("c32s006_045") from _call_BlinkXS4_2342
    ama "Su solicitud estaba la primera y creo que puede mostrar liderazgo en el equipo, después de lo que hizo en el viejo campo de tiro."
    mc "Me parece una buena elección."
    ama "Además, más que librarme de él, voy a tener que aguantarlo durante un mes cuando yo vuelva a Newport."
    call BlinkXS4("c32s006_050") from _call_BlinkXS4_2343
    mar "¿Siete chicos? ¿Necesitamos tanta seguridad? ¿Dónde los vamos a alojar?"
    mc "Se alojarán en la hacienda que [ama] y [eva] han usado como base. Ayudarán a reformarlo para que sea un sitio digno donde vivir."
    mc "Y son necesarios siete chicos porque no queremos que hagan lo mismo que hacían [eva] y [ama]. Se acabó estar de guardia 24 horas."
    mc "Con siete operativos y un octavo que se unirá en breve, se pueden montar turnos de descanso adecuados."
    call BlinkXS4("c32s006_055") from _call_BlinkXS4_2344
    mar "¿El octavo será [gav]?"
    mc "Si todo va como está planeado, sí. Aún está en proceso de recuperación."
    scene c32s006_055d with dissolve
    sam "Me hubiera gustado conocerlo y ver ese brazo... Tan sólo por temas médicos, claro."
    bet "Es muy buen chico y el brazo es espectacular. La semana próxima haremos una prueba de campo."
    bet "Si todo sale bien, seguramente volveré a casa con él en un par de semanas."
    sam "Entonces tendré la oportunidad de examinar ese brazo en persona. Tengo ganas de hacerlo... Y de conocer al chico, claro."
    mc "*Risa* Además, Tía [bet] ya le está enseñando costumbres de la familia. Se está acostumbrando a los abrazos."
    scene c32s006_060a with fade
    "Después de que [aar] llegue con una furgoneta llena de operativos y de las presentaciones, vais al aeropuerto y comienzan las despedidas."
    scene c32s006_060b with fade
    "La sucesión de abrazos es más triste que dos días atrás."
    scene c32s006_060c with fade
    stop music fadeout (1.5)
    "Para todos menos para [aar]."
    scene c32s006_065a with fade
    call BlinkXS4("c32s006_065") from _call_BlinkXS4_2345
    play music ("music/Miami-Nights.ogg")
    "Mientras [mar] y [sam] estrujan a [aar], aprovechas para despedirte de los operativos."
    mc "Cuidad de mi familia, [dam]."
    dam "Lo haremos, [mc]. [ces] será el jefe de uno de los turnos y yo de otro. [eva] dirigirá el tercero."
    mc "Se me hace raro no verte con el uniforme. No hacía falta que te vistieras tan... 'elegante'."
    call BlinkXS4("c32s006_070") from _call_BlinkXS4_2346
    if not salary:
        dam "Bueno, nos vas a pagar una fortuna en salarios atrasados, y por fin podré comprarme un Ferrarini Testabionda."
    else:
        dam "Bueno, aunque no nos pagues los salarios atrasados, con el sueldo podré alquilar un día un Ferrarini Testabionda."
    dam "Creo que va a parecer que estoy en aquella vieja serie de los 80... Pero debería ser Corrupción en Newport, en vez de en Miami."
    dam "*Risa* Me tenía que vestir para no desentonar con el coche."
    mc "*Risa* Vestido así y con un Ferrarini, va a parecer que el resto de los chicos te protegen a ti."
    call BlinkXS4("c32s006_075") from _call_BlinkXS4_2347
    dam "*Risa* Especialmente si estoy rodeado de chicas todo el día."
    mc "[dam]..."
    call BlinkXS4("c32s006_080") from _call_BlinkXS4_2348
    dam "¡Oh! No me malinterpretes. Tu familia está fuera de límites para mí y para cualquiera de los otros chicos."
    dam "Además, [ces] y yo tenemos una relación. Él seguramente me degollaría mientras duermo si intentara algo con alguna chica."
    mc "Bueno, creo que es mi turno de despedirme de las chicas ahora que han soltado a [aar]."
    mc "Estaremos en contacto."
    call BlinkXS4("c32s006_085") from _call_BlinkXS4_2349
    dam "[mc]..."
    mc "¿Sí?"
    dam "Gracias por esta oportunidad."
    mc "Dáselas a [ama]. Fue ella la que te escogió."
    dam "Pero fuiste tú quien cumplió sus promesas. Al menos casi todas."
    stop music fadeout (1.5)
    mc "Te dije que lo haría."
    scene c32s006_090a with fade
    call BlinkXS4("c32s006_090") from _call_BlinkXS4_2350
    play music ("music/SadSoul.ogg")
    mc "Ha llegado el momento de despedirnos, ¿no?"
    sam "Se me va a hacer duro volver a casa y dejaros aquí."
    mc "[ama] y [bet] volverán pronto a casa. Y, conmigo, siempre quedan las videoconferencias."
    sam "Pero no puedo hacer esto por videoconferencia."
    if sam._var("route"):
        scene c32s006_095a with dissolve
        "Tu esposa te da un apasionado beso de despedida. No sabéis cuándo podréis volver a veros."
        "Pero el beso dura demasiado poco. La despedida se está alargando demasiado y hay un plan de vuelo que cumplir."
    scene c32s006_095b with dissolve
    "La enfermera te da un abrazo de esos que hacen que necesites ungüento para los moretones."
    sam "Ve a despedirte de tu madre antes de que te secuestre y te suba a ese avión."
    mc "Te quiero, [sam.nick]."
    sam "Yo también, [mc]."
    scene c32s006_100a with fade
    call BlinkXS4("c32s006_100") from _call_BlinkXS4_2351
    mc "Creo que aquí acaba el fin de semana... ¿Te lo has pasado bien?"
    mom "Ha sido fantástico, pero ha acabado demasiado pronto. Si no fuera porque llegan las chicas nuevas, me quedaría una semana."
    mc "*Risa* ¿Dejarías a [sam.nick] sola en el avión con siete rudos mercenarios?"
    call BlinkXS4("c32s006_105") from _call_BlinkXS4_2352
    mom "*Risa* Seguramente los pondría firmes antes de aterrizar."
    mc "Estoy seguro de eso."
    call BlinkXS4("c32s006_110") from _call_BlinkXS4_2353
    mom "Y hablando de poner firmes a la gente. No trabajes tan duro."
    mom "[ama] me ha dicho que estos son los primeros días libres que te coges desde que has llegado."
    mc "Cuanto más duro trabaje, antes podré volver a casa."
    call BlinkXS4("c32s006_115") from _call_BlinkXS4_2354
    mom "E invita a [aar] a cenar algunos días. Asegúrate de que come bien. De alguna forma, es tu hermano."
    mc "Lo haré. Pero no para que coma bien, sino para que se vaya integrando en la familia."
    mc "Creo que, si tomas el control de la cocina, no va a tener ningún problema para comer bien."
    call BlinkXS4("c32s006_120") from _call_BlinkXS4_2355
    mom "Y..."
    mc "*Risa* Y no sabes qué consejos darme para alargar más esta despedida, ¿no?"
    scene c32s006_125a with dissolve
    mom "Me conoces demasiado bien. Te voy a echar mucho de menos."
    mc "Yo también a ti."
    if mar._var("route"):
        scene c32s006_125b with dissolve
        "[mar] te da un beso agridulce que sabe a despedida."
        "Es hora de que el avión parta."
    call BlinkXS4("c32s006_130") from _call_BlinkXS4_2356
    mc "Iros ya, o no podréis cumplir con el plan de vuelo."
    mc "Te quiero."
    mom "Yo también te quiero."
    stop music fadeout (1.5)
    scene c32s006_130d with dissolve
    "Cuando el avión cierra la puerta y recoge la escalera, es como si la isla perdiera parte de su brillo."
    play music ("music/RhythmPlay.ogg")
    bet "Sólo han sido dos días, pero me ha servido para darme cuenta de cuánto echo de menos a todo el mundo."
    ama "Yo estaba pensando que tengo ganas de que vuelva [eva]. No sólo por verla, sino para volver a casa por una temporada."
    mc "Creo que hasta [aar] va a echarlas de menos."
    aar "Son muy... agradables."
    mc "*Risa* Creo que te tendremos que dar nosotros su ración de abrazos."
    bet "*Risa* Y yo creo que, si lo hacemos, [aar] va a pedir el traslado a alguna oscura base en la Antártida."
    scene c32s006_130e with dissolve
    ama "*Risa* No tenemos bases en la Antártida, pero [aar] se acostumbrará a los abrazos antes de que te vayas, Tía [bet]."
    aar "¿Podéis dejar el tema de los abrazos de una vez?"
    mc "Sólo si vienes a cenar a casa. Órdenes de [mar]."
    aar "Trato hecho."
    ama "*Risa* Entonces dejaremos los abrazos para después de cenar."
    aar "*Gruñido*"
    todas "*Risa*"
    stop music fadeout (1.5)
    return
label c32s006_Hailey:
    scene black with dissolve
    centered "{size=+20}{b}DÍA 64 – MARTES{/b}{/size}"
    "Los días continúan con la rutina habitual, a la que se suman las cenas con [aar]."
    play music ("music/Fireflies-and-Stardust.ogg")
    call BlinkXS4("c32s006_150") from _call_BlinkXS4_2357
    "También continúan las videoconferencias a casa. Después de la visita de [sam] y [mar], echas de menos incluso más a las chicas en casa."
    mc "¿Así que ya ha llegado la primera estudiante? ¿Cómo es?"
    dap "*Risa* Guapísima."
    mc "*Risa* No me refería a eso, sino a nivel de personalidad."
    call BlinkXS4("c32s006_155") from _call_BlinkXS4_2358
    dap "Aún no lo sé. Es demasiado pronto para eso."
    dap "Pero ya ha habido un par de anécdotas divertidas."
    mc "Por ejemplo..."
    call BlinkXS4("c32s006_160") from _call_BlinkXS4_2359
    dap "La primera ha sido cuando atravesábamos SLO y dice..."
    scene c32s006_165a with dissolve
    $ hai = TGCharacter (persistent.haiName, color = "#7cb2db", lname = "Jenkinson")
    hai "En esta ciudad hay más gente que en todo mi condado..."
    hai "Mi hermano dice que voy a echar de menos los caballos, y creo que tiene razón."
    call BlinkXS4("c32s006_170") from _call_BlinkXS4_2360
    mc "Esta es la chica que venía de Alabama, ¿no? Si vive en el campo, el cambio de estilo de vida puede ser abrumador."
    dap "Sí, pero no es eso lo que me ha parecido divertido. He pensado en si mi madre le dejaría tener un caballo en el jardín."
    dap "La respuesta, obviamente, es que no, pero eso ha llevado a lo realmente divertido."
    mc "¿Qué ha pasado?"
    call BlinkXS4("c32s006_175") from _call_BlinkXS4_2361
    dap "Cuando hemos llegado a Newport, la hemos llevado a la tienda de [mad.nick] a comprarse un bañador."
    mc "*Risa* ¿Ya la estáis presentando a toda la familia?"
    call BlinkXS4("c32s006_180") from _call_BlinkXS4_2362
    dap "Aún no, pero una chica tiene que saber dónde comprar ropa en una ciudad nueva."
    dap "Cuando lleguen todas, haremos una comida de bienvenida, para que conozcan a todo el mundo."
    mc "Creo que es una buena idea. A [ama] le sigue preocupando cómo se van a integrar en la familia."
    mc "Pero no veo nada divertido en ir a comprar un bañador..."
    call BlinkXS4("c32s006_185") from _call_BlinkXS4_2363
    dap "*Risa* ¡Hombres...!"
    dap "Lo divertido es que... Espera. Te mando un vídeo."
    scene c32s006_190pv with fade
    show c32s006_190v
    mc "*Risa* Me recuerda a esa vieja peli de los 90 con la chica en el caballo de monedas."
    dap "Eso es lo que me ha parecido divertido. Tal y como iba vestida y diciendo que iba a echar de menos a los caballos..."
    dap "En cuanto lo ha visto, me ha dicho..."
    scene c32s006_165b with fade
    hai "Déjame subirme a ese caballo para mandarle una foto a mi hermano."
    scene c32s006_195a with fade
    call BlinkXS4("c32s006_195") from _call_BlinkXS4_2364
    dap "Y la he convencido para hacer un vídeo en vez de una foto."
    dap "Iba poniendo caras, como si fuera a toda velocidad en el caballo, pero a cámara lenta. No sé si me explico."
    mc "Parece una chica divertida. Y el caballo está hecho polvo. No lo recordaba así."
    dap "Creo que necesita una mano de pintura."
    call BlinkXS4("c32s006_200") from _call_BlinkXS4_2365
    dap "Pero hay algo de ella que no te va a gustar..."
    mc "¿Crees que puede ser problemática?"
    call BlinkXS4("c32s006_205") from _call_BlinkXS4_2366
    dap "*Risa* No, nada de eso, pero..."
    dap "*Risa* [emm] la ha convencido para que el bañador que se estaba comprando fuera... rosa..."
    mc "*Risa* ¡Otra mujer de rosa en casa! ¡Noooo!"
    call BlinkXS4("c32s006_210") from _call_BlinkXS4_2367
    dap "Creo que ha cedido por la presión de [emm]. No la veía muy convencida con el color."
    dap "Ya conoces a [emm] y lo insistente que puede ser."
    mc "*Risa* Habrá que dejar que [hai] pase tiempo con tu hermana para contrarrestar la influencia de [emm]."
    call BlinkXS4("c32s006_215") from _call_BlinkXS4_2368
    dap "*Risa* Bueno, de momento nos han nombrado a [emm] y a mí como comité de recepción."
    dap "Creo que es porque [emm] no se separa de tu camioneta y porque yo puedo controlarla si hace muchas locuras."
    dap "Con [eri] y [sca] trabajando, no quedaban muchas opciones."
    mc "¡Cómo habéis cambiado en los últimos meses! ¿Te acuerdas de cuando llegué?"
    mc "Las dos estabais buscándoos las cosquillas permanentemente."
    call BlinkXS4("c32s006_220") from _call_BlinkXS4_2369
    dap "Bueno, todo ha cambiado mucho en los últimos meses. Creo que las dos somos más maduras ahora."
    dap "Y, hablando de madurez, voy a dejarte y a ayudar a [hai] a deshacer las maletas."
    dap "Hemos llegado justo para la sesión de yoga de la tarde y ella ha decidido unirse. Supongo que habrá acabado de ducharse."
    mc "¿También hacéis yoga por la tarde?"
    call BlinkXS4("c32s006_225") from _call_BlinkXS4_2370
    dap "Con tanta gente y tantos horarios diferentes, hemos decidido hacer dos sesiones."
    dap "Así, las chicas que no pueden venir a la sesión de la mañana, se pueden apuntar por la tarde."
    mc "Supongo que es lo más lógico."
    scene c32s006_225d with dissolve
    dap "Me voy. Te veo mañana. Te quiero."
    stop music fadeout (1.5)
    mc "Yo también te quiero."
    return
label c32s006_Gav:
    scene black with dissolve
    centered "{size=+20}{b}DÍA 66 – JUEVES{/b}{/size}"
    play sound ("music/RingtoneMC.ogg")
    "*Ring-Ring*"
    stop sound
    scene c32s006_250d with fade
    play music ("music/These-Little-Moments.ogg")
    mc "Dime, [ama]. ¿Vas a tardar mucho en venir a buscarme? Vamos a llegar tarde."
    call BlinkXS4("c32s006_250") from _call_BlinkXS4_2371
    ama "¿No te acuerdas de que te dije que estaría aquí toda la mañana?"
    ama "Tienes que venir por tu cuenta. Hoy no te voy a hacer de chófer."
    mc "No me acordaba. Ahora cojo un coche y voy para allá."
    mc "Id empezando sin mí."
    call BlinkXS4("c32s006_255") from _call_BlinkXS4_2372
    ama "Deberías estar aquí..."
    mc "Lo sé, pero no quiero retrasarlo más. Todo el mundo debe estar muy ansioso."
    ama "Sí, especialmente [gav]."
    mc "Por eso debéis empezar sin mí. Ha sido mi error. En quince minutos estaré ahí."
    scene c32s006_260a with fade
    "Cuando llegas al campamento, [gav] está haciendo demostraciones del uso de su brazo."
    "Hoy es el día en que la potencia se ha puesto al máximo por primera vez."
    "Se ha despejado una zona donde puede hacer los ejercicios planeados y los operativos pueden observarlo."
    scene c32s006_260b with fade
    "La coordinación de movimientos y el manejo de objetos parece ir bien bajo la atenta mirada de [cal]."
    "Decides mantenerte a una distancia prudencial mezclado entre los clones que están mirando las pruebas en silencio."
    "No sólo para disimular que has llegado tarde, sino porque hoy el protagonista debe ser [gav]."
    "Algunos te ven llegar y te dejan un hueco. Otros no se dan ni cuenta de tu presencia."
    "Solo tienen ojos para su compañero. [gav] le cae bien a casi todo el mundo."
    scene c32s006_260c with fade
    "Los ejercicios de fuerza también dan el resultado esperado."
    "[gav] estaba especialmente ansioso con este desde que, hace tres días, no pudo completarlo."
    "Los nuevos ajustes que ha introducido [cal] parecen funcionar mejor de lo previsto."
    scene c32s006_260d with fade
    "Cuando la serie de ejercicios prevista finaliza, [gav] hace un ejercicio que no estaba en el plan."
    "El chico quiere probar el brazo más allá de lo que [cal], siempre conservador, está dispuesto a añadir al plan de ejercicios."
    "Es un éxito, y puedes escuchar murmullos de sorpresa entre los clones que tienes alrededor."
    scene c32s006_260e with fade
    "Cuando por fin acaba la serie de ejercicios, los clones se dispersan y te acercas a [cal] y a [gav]."
    "Ves que [bet], [ama], y [aar] también se acercan desde diversos puntos del campamento."
    scene c32s006_265a with fade
    call BlinkXS4("c32s006_265") from _call_BlinkXS4_2373
    mc "Felicidades, [gav]. Parece que todo ha ido bien, por lo que he podido ver."
    gav "Gracias, [mc]. [cal] dice que aún hay que ajustar unos parámetros, pero que el funcionamiento es mejor del esperado."
    mc "Eso es genial, [gav]. ¿Significa eso que podrás incorporarte al servicio en breve?"
    call BlinkXS4("c32s006_270") from _call_BlinkXS4_2374
    cal "No corras tanto, [mc]. Yo creo que, como mínimo, le queda una semana."
    mc "¿Una semana? ¡Yo estaba pensando en si estaría listo para volver con [eva] a Newport cuando ella se vaya dentro de más de un mes!"
    call BlinkXS4("c32s006_275") from _call_BlinkXS4_2375
    cal "Lo siento. Creía que..."
    mc "Nadie va a volver al servicio antes de estar listo, [cal]."
    mc "Pero... ¿Una semana? ¡Eso es fantástico!"
    call BlinkXS4("c32s006_280") from _call_BlinkXS4_2376
    bet "Si las pruebas de hoy salían como estaban previstas, habíamos planeado que volviera con [ama] y conmigo en un par de semanas."
    bet "Creo que podremos cumplir con el plan."
    mc "No sabía que tú volverías con [ama]..."
    call BlinkXS4("c32s006_285") from _call_BlinkXS4_2377
    bet "Si mi paciente está en Newport, yo debería estar allí."
    bet "Al menos hasta que construyáis la mano para [cal] y tenga que volver."
    mc "Entonces volverás pronto a Aruba."
    call BlinkXS4("c32s006_290") from _call_BlinkXS4_2378
    ama "Con [gav] en Newport, seremos nueve en el equipo de vigilancia."
    ama "Es una cifra adecuada para poder hacer tres turnos y tener descanso suficiente."
    ama "Los chicos del equipo han estado trabajando mucho para reformar la hacienda."
    mc "Eso lo dejo en vuestras manos."
    call BlinkXS4("c32s006_295") from _call_BlinkXS4_2379
    gav "Y hoy he demostrado que sirvo para más que mirar unas pantallas."
    mc "Lo he visto. Me alegro mucho por ti, [gav]."
    call BlinkXS4("c32s006_300") from _call_BlinkXS4_2380
    aar "Y esta tarde iremos al campo de tiro para hacer más pruebas. Esta vez sin espectadores."
    aar "Aunque tú puedes venir, claro. Eres el jefe."
    mc "No estaba previsto, y tengo una reunión con [vin] y sus manitas."
    call BlinkXS4("c32s006_305") from _call_BlinkXS4_2381
    aar "*Risa* No te envidio. Ya te mandaré un informe con los resultados de las pruebas."
    mc "*Risa* ¿Me lo puede mandar [cal]? Tú aún no has entendido el significado de 'conciso'."
    aar "*Risa* Al final te odiaré."
    mc "*Risa* Entonces dejaré de pedirte que vengas a casa a cenar."
    aar "*Risa* Vale, no te odiaré demasiado."
    scene c32s006_305d with fade
    "Por la tarde, después de la reunión con [vin] en tu oficina provisional, lees el informe de [cal] sobre las pruebas de tiro."
    "Son los mejores resultados que [gav] ha tenido nunca en el campo de tiro. Recuerdas que [eva] te dijo que no era muy bueno."
    "Está lejos de los valores de [ama] o incluso de [dam], pero ha pasado de ser uno de los peores G a estar en la parte superior."
    stop music fadeout (1.5)
    "El brazo mecánico le ha proporcionado una estabilidad que no tenía antes. Y solo puede mejorar tal como vaya entrenando."
    return
label c32s007_cult:
    if _in_replay:
        $ mc._var("relationships", 0, "set")
        call mrS3_eva_route from _call_mrS3_eva_route_24
        if eva._var("route"):
            call mrS3_eva_pregnant from _call_mrS3_eva_pregnant_5
        call mrS3_mar_route from _call_mrS3_mar_route_54
        call mrS3_rels from _call_mrS3_rels_43
    scene black with dissolve
    centered "{size=+20}{b}DÍA 69 – DOMINGO{/b}{/size}"
    call BlinkXS4("c32s007_005") from _call_BlinkXS4_2382
    play music "music/Ukulele-Life.ogg"
    mc "¿Ya estás lista para venir?"
    eva "Yo estoy lista desde hace un mes. Quien no estoy tan segura de que estén listos son los chicos."
    eva "Me da miedo dejarlos solos. Aún no se han aprendido el nombre de todo el mundo... Y ya llevan una semana aquí."
    mc "*Risa* ¿A veces dudan entre el nombre de dos de las 20 chicas? ¿Aún no saben el color favorito de cada una de ellas?"
    call BlinkXS4("c32s007_010") from _call_BlinkXS4_2383
    eva "¡No te rías! ¡Son cosas importantes!"
    eva "Si apareciera alguien disfrazado de [emm] pero se vistiera de... no sé... verde... a lo mejor no la detectarían..."
    mc "Estoy seguro de que, después de más de una semana ahí, ya saben que [emm] es la Reina Rosa."
    call BlinkXS4("c32s007_015") from _call_BlinkXS4_2384
    $ isr = TGCharacter ("Isard", color = "#e3ff00")
    eva "*Risa* Bueno, eso sí que lo saben. Creo que [isr] casi se sacó los ojos cuando vio la habitación de [emm] la primera vez."
    eva "Pero no estoy tan segura de que fueran a detectar a un clon de [eri] vestido de rosa."
    if persistent.family:
        mc "*Risa* Por suerte, el único clon de [eri] eres tú."
    else:
        mc "*Risa* Creo que la única que podría hacerse pasar por [eri] eres tú."
    mc "Y a ti te reconocerían al momento. [eri] no camina como si estuviera a punto de matar a alguien."
    call BlinkXS4("c32s007_020") from _call_BlinkXS4_2385
    eva "¡Yo tampoco lo hago! Eso sería como darle ventaja al enemigo por revelar mis intenciones."
    mc "*Risa* No cambies nunca, [eva]."
    if eva._var("pregnant") and eva._var("route"):
        call BlinkXS4("c32s007_025") from _call_BlinkXS4_2386
        eva "Bueno, gracias a ti y a tu semen mágico voy a cambiar. Me voy a poner gordísima."
        mc "*Risa* ¿Vas a dejar de ser un leopardo mortal para pasar a ser un hipopótamo igual de mortal?"
        call BlinkXS4("c32s007_030") from _call_BlinkXS4_2387
        eva "*Risa* ¡No te rías de mí! Y nunca le digas a una embarazada que parece un hipopótamo."
        mc "No te he dicho que lo parezcas. Solo he preguntado en qué te ibas a convertir. Aún no se te nota el embarazo."
        mc "Y cuando se te note, no me atreveré a decírtelo. Leí que los hipopótamos son los mamíferos que más muertes producen en África."
    call BlinkXS4("c32s007_035") from _call_BlinkXS4_2388
    eva "*Risa* Eres un capullo."
    if eva._var("route"):
        mc "*Risa* Pero no por ello estás deseando menos venir aquí y besarme."
        call BlinkXS4("c32s007_040") from _call_BlinkXS4_2389
        eva "¿Sólo besarte? Creo que no me conoces lo suficiente."
        mc "*Risa* Sí que te conozco, pero no sé si hay alguno de tus chicos escuchando esta conversación."
    else:
        mc "*Risa* Pero no por ello estás deseando menos venir aquí y abrazarme."
    call BlinkXS4("c32s007_045") from _call_BlinkXS4_2390
    stop music fadeout (1.5)
    eva "Volviendo al tema de los chicos..."
    play music ("music/Hidden Past.ogg")
    mc "¿Qué pasa con ellos?"
    eva "Hay algo con lo que no habíamos contado."
    mc "El alojamiento está controlado. La comida también. Ya les han llegado los primeros sueldos..."
    mc "¿Qué hemos obviado sobre ellos?"
    call BlinkXS4("c32s007_050") from _call_BlinkXS4_2391
    eva "No habíamos pensado en cómo los iban a ver las chicas nuevas."
    eva "Ya somos una familia rara de por sí, ¿pero tener tipos armados dando vueltas alrededor de un dormitorio universitario...?"
    eva "Creo que las chicas no lo están llevando muy bien."
    mc "No lo había pensado. Creía que sería como con vosotras al principio, que no sabíamos que estabais ahí."
    call BlinkXS4("c32s007_055") from _call_BlinkXS4_2392
    eva "Esa era nuestra idea, pero [mar] y [nor] obligan al que está vigilando el perímetro a venir de vez en cuando a tomar algo fresco."
    eva "Dicen que no pueden aceptar que estén dando vueltas todo su turno por el bosque con este calor."
    mc "¿Eso afecta a su efectividad para vigilar la casa?"
    mc "Tú mandas sobre el equipo de seguridad, si crees que [mar] y [nor] se están extralimitando..."
    call BlinkXS4("c32s007_060") from _call_BlinkXS4_2393
    eva "No, no te preocupes. Es bueno que vengan a la casa."
    eva "Conocen mejor a la familia y se hacen rutas mentales para ir de un sitio a otro si son necesarios."
    eva "Pero no habíamos contado con cómo impactaría eso a las chicas nuevas."
    mc "Mi prioridad es vuestra seguridad, no lo que seis chicas a las que no conozco piensen de esa seguridad."
    mc "¿Alguna se ha quejado?"
    call BlinkXS4("c32s007_065") from _call_BlinkXS4_2394
    eva "No, pero comentan cosas entre ellas. Y no solo de la seguridad."
    eva "Mira este video para hacerte una idea."
    scene c32s007_070a with fade
    $ nia = TGCharacter (persistent.niaName, color = "#bab55d", lname = "Serrat")
    $ pat = TGCharacter (persistent.patName, color = "#40bdce", lname = "Robinson", nick = persistent.patNick)
    $ cri = TGCharacter (persistent.criName, color = "#dcf4a7", lname = "Song", nick = persistent.criNick)
    $ zoe = TGCharacter (persistent.zoeName, color = "#5f40ce", lname = "Perceval")
    $ hai = TGCharacter (persistent.haiName, color = "#7cb2db", lname = "Jenkinson")
    $ kal = TGCharacter ("Kalyani", color = "#af6d16", lname = "Singh", nick = "Kaly")
    cri "No estoy segura de que esta familia sea muy normal."
    nia "La fiesta de bienvenida estuvo muy bien. A mí me parecen todas muy simpáticas."
    mc "¿Habéis puesto cámaras en la casa de [nor] para vigilarlas?"
    eva "Calla y escucha."
    call BlinkXS4("c32s007_075") from _call_BlinkXS4_2395
    cri "Pero ¿tener guardaespaldas? ¿En un dormitorio universitario con once chicas?"
    cri "¿Tú ves eso normal? Es imposible que esto tenga ingresos suficientes para pagar ese tipo de seguridad."
    call BlinkXS4("c32s007_080") from _call_BlinkXS4_2396
    nia "A mí también me pareció extraño al principio, pero [mar] me lo explicó."
    if mar._var("route"):
        nia "Me dijo que su marido dirige una empresa de seguridad privada."
    else:
        nia "Me dijo que su hijo dirige una empresa de seguridad privada."
    nia "Supongo que proteger a su familia está por encima del beneficio."
    call BlinkXS4("c32s007_085") from _call_BlinkXS4_2397
    cri "Eso puedo entenderlo, pero hay cosas que no me acaban de cuadrar."
    cri "Estamos en California, el único estado donde se puede beber alcohol a nuestra edad..."
    cri "¿Tú viste beber algo con alcohol a alguien en la fiesta de bienvenida? Aparte de nosotras, claro."
    call BlinkXS4("c32s007_090") from _call_BlinkXS4_2398
    nia "Bueno, yo no bebí alcohol. El vino sin alcohol que tienen es muy bueno."
    nia "Pero [mee] sí que estaba bebiendo vino de verdad. No me fijé en el resto."
    nia "No sé distinguir el vino de verdad del sin alcohol cuando lo veo en una copa."
    call BlinkXS4("c32s007_095") from _call_BlinkXS4_2399
    cri "Tienes razón, no había contado con eso. Pero cada vez que fui a servirme un vaso de vino había alguien sirviéndose un vaso sin alcohol."
    cri "Me pareció raro. Puedo entenderlo con [deb.nick] o [sim] porque son deportistas, pero ¿el resto? Me sorprendió."
    call BlinkXS4("c32s007_100") from _call_BlinkXS4_2400
    nia "A mí lo que me más me sorprendió es que, aparte del chico en la silla de ruedas, todas fuéramos chicas."
    call BlinkXS4("c32s007_115") from _call_BlinkXS4_2401
    cri "El 'chico en la silla de ruedas' se llama Jamaal. Es ofensivo que lo llames así."
    call BlinkXS4("c32s007_120") from _call_BlinkXS4_2402
    nia "Yo soy horrible para recordar nombres. Llevo dos días llamando Clara a [kia]."
    nia "Ella es super educada y no me ha sacado de mi error. Me lo ha dicho Katlyn hoy... O se llama [kat]..." id c32s007_cult_4319ddd8
    if mc._var("relationships")>1:
        nia "Pero, lo que quería decir es que no estaba ninguno de los maridos de las que están casadas."
        call BlinkXS4("c32s007_105") from _call_BlinkXS4_2403
        cri "A mí me dijeron que están trabajando fuera del país. Pero ¿te has dado cuenta de que ninguna lleva anillo?"
        cri "¿Y esos tatuajes? Da un poco de grima."
        call BlinkXS4("c32s007_110") from _call_BlinkXS4_2404
        nia "Debe ser una costumbre de aquí. Si sólo lo hubiera llevado una, me hubiera parecido algo divertido y romántico."
        nia "Cuando es más de una, parece un patrón. A lo mejor es una moda aquí en Newport."
    call BlinkXS4("c32s007_125") from _call_BlinkXS4_2405
    cri "No lo sé. Si coges todo por separado, son pequeñas cosas."
    cri "Si lo sumas todo... me parece que nos hemos infiltrado en una secta sin querer."
    call BlinkXS4("c32s007_130a") from _call_BlinkXS4_2406
    nia "*Risa* ¡Qué exagerada eres! Son pequeños cambios en las costumbres."
    nia "Aunque tienes razón en que parece una secta. *Risa* Todas parecen sacadas de una agencia de modelos."
    call BlinkXS4("c32s007_130b") from _call_BlinkXS4_2407
    cri "Yo no juzgo a la gente por su apariencia..."
    mc "Sabía que esa chica iba a ser rara..."
    call BlinkXS4("c32s007_130c") from _call_BlinkXS4_2408
    nia "Yo no estoy juzgando a nadie. Solo he dicho que todas son guapísimas."
    nia "Pero tú eres de San Diego. ¿Ahí no pasan estas cosas? ¿Los tatuajes, el alcohol?"
    call BlinkXS4("c32s007_135") from _call_BlinkXS4_2409
    cri "Todas mis amigas beben alcohol. Por eso me parece tan raro."
    cri "Y ninguna se haría tatuajes tan feos como esos para demostrar que es propiedad de un tío."
    cri "Hay algo que huele raro en este sitio."
    scene c32s007_140a with fade
    call BlinkXS4("c32s007_140") from _call_BlinkXS4_2410
    eva "Y siguieron dándole vueltas al tema durante un rato."
    eva "Esa [cri] tiene olfato para detectar cosas que no cuadran."
    mc "Me extraña que no dijeran nada sobre [eri], [dap] y tú."
    call BlinkXS4("c32s007_145") from _call_BlinkXS4_2411
    eva "*Risa* [nor] nos presentó como 'Mis hijas [dap] y [eri]. Y aquella de allí es [eva].'"
    eva "O se acercaba a donde estaba yo con una de las chicas y decía 'Aquellas son [eri] y [dap], mis hijas. Y a [eva] ya la conoces.'"
    mc "Una forma ingeniosa de que ellas pensaran que sois trillizas."
    call BlinkXS4("c32s007_150") from _call_BlinkXS4_2412
    eva "Y sin tener que mentirles. Tenías razón en que no debemos mentirles."
    eva "No sabemos cómo se van a integrar en la familia, y sería incómodo decirles después que les hemos mentido."
    mc "Te aseguro que al final me compraré esa camiseta."
    mc "¿Y [kal]? ¿Cómo se está integrando? Es la que más choque cultural tiene que experimentar."
    call BlinkXS4("c32s007_155") from _call_BlinkXS4_2413
    eva "Curiosamente, es la que mejor lo está llevando. Pensé que tendría más choque cultural."
    eva "Tener a [sai] al lado le está ayudando mucho, pero hay algo que no me acaba de gustar."
    eva "Pasa más tiempo en casa de [mar] con las chicas viejas que en casa de [nor] con las chicas nuevas."
    mc "¿Qué tiene eso de malo? Es lógico, si [sai] está allí."
    call BlinkXS4("c32s007_160") from _call_BlinkXS4_2414
    eva "Yo contaba con ella como infiltrada entre las nuevas una vez le contemos la verdad."
    mc "¿Le vais a contar la verdad tan pronto?"
    eva "[sai] está insistiendo y diciendo que es seguro hacerlo. Supongo que en unas semanas sabremos si es verdad."
    eva "Pero si se integra solamente con las primeras chicas, no la podremos usar para desviar los rumores con las nuevas."
    mc "Dale tiempo. Acaba de llegar y es normal que quiera pasar tiempo con su prima."
    mc "Y no deberíamos 'usar' a ninguna de las chicas."
    call BlinkXS4("c32s007_165") from _call_BlinkXS4_2415
    eva "Si los rumores entre ellas empiezan a crecer..."
    mc "Seguro que encontraréis una solución."
    call BlinkXS4("c32s007_170") from _call_BlinkXS4_2416
    eva "*Risa* {b}Encontrarán{/b}. En dos días no estaré aquí."
    mc "*Risa* En dos días tendrás que ponerte un chaleco antibalas para que no te rompa ninguna costilla abrazándote."
    stop music fadeout (1.5)
    eva "*Risa* Creo que pasaste demasiado tiempo con [dam] mientras estuvo ahí. Ni que pudieras romperme alguna costilla..."
    return
label c32s007_teaser:
    scene black with dissolve
    centered "{size=+20}{b}DÍA 71 – MARTES{/b}{/size}"
    call BlinkXS4("c32s007_200") from _call_BlinkXS4_2417
    "En la redecorada oficina..."
    ama "No entiendo por qué [eva] no ha querido que fuera a buscarla al aeropuerto."
    mc "Yo también se lo propuse. Me dijo que quería conducir hasta aquí."
    mc "Supuse que necesita hacer las paces con la isla a su propio ritmo, igual que hiciste tú."
    call BlinkXS4("c32s007_205") from _call_BlinkXS4_2418
    ama "Supongo que tienes razón, pero nunca hemos estado tanto tiempo separadas."
    ama "Tengo muchas ganas de verla de nuevo."
    mc "Yo también..."
    call BlinkXS4("c32s007_210") from _call_BlinkXS4_2419
    ama "Sé qué estás pensando."
    mc "Sorpréndeme."
    call BlinkXS4("c32s007_215") from _call_BlinkXS4_2420
    ama "Sabes que, ahora que [eva] está aquí, no puedes retrasar más lo de Daniels."
    ama "En un mes ni siquiera le has hecho una visita para hablar con él."
    mc "Si le hubiera visitado, lo más probable, visto cómo fue lo de [erc], es que hubiera tomado una decisión sin esperar a [eva]."
    mc "Pero te equivocas."
    call BlinkXS4("c32s007_220") from _call_BlinkXS4_2421
    ama "No me digas que estabas pensando que, ahora que ella llega, [bet] y yo nos vamos a ir."
    mc "Es exactamente en lo que estaba pensando."
    mc "Sé que vais a estar las tres aquí durante unos días, pero..."
    call BlinkXS4("c32s007_225") from _call_BlinkXS4_2422
    ama "Pero no quieres que suene a que tienes favoritas."
    mc "Lo que quería decir es que la casa va a parecer muy vacía sin Tía [bet] y sin ti."
    mc "Casi empezaba a parecer un hogar."
    call BlinkXS4("c32s007_230") from _call_BlinkXS4_2423
    ama "*Risa* En un hogar no me prohibirían la entrada a una habitación."
    mc "Bueno, he hecho unos cambios en la habitación de [eva] y..."
    car "*Desde fuera* *Jadeo de sorpresa*"
    eva "*Desde fuera* Hola, [car]."
    scene c32s007_235An with dissolve
    "Pasan unos segundos mientras [ama] y tú no sabéis si salir a darle la bienvenida a [eva] o esperar a que entre."
    eva "*Desde fuera* Libera las agendas de [mc] y de [ama] para todo el día, por favor."
    eva "*Desde fuera* Que no nos moleste nadie."
    scene c32s007_240a with fade
    call BlinkXS4("c32s007_240") from _call_BlinkXS4_2424
    eva "¡Ya estoy aquí!"
    eva "¿Quién quiere un abrazo?"
    scene c32s007_240d with hpunch
    ama "¡Bienvenida! No sabes lo mucho que te he echado de menos."
    eva "Yo también te he echado de menos. Pero ya estoy aquí. Se acabó el añorarme, al menos por unos días."
    "El silencioso abrazo entre las dos hermanas dura unos largos minutos mientras esperas ansioso porque llegue tu turno."
    "No te atreves a interrumpirlas haciéndoles sentir que estás esperando. Verlas abrazadas así es muy especial."
    if eva._var("route"):
        scene c32s007_240e with hpunch
        "Al cabo de un rato, tu esposa se lanza a tus labios. Es un beso con sabor a reencuentro."
        "La espera ha valido la pena."
        "Es un beso largo, dulce. Un beso que intenta recuperar un mes sin besos."
    scene c32s007_240f with dissolve
    eva "A ti también te he echado mucho de menos."
    mc "Yo también, cielo."
    "Vuestro abrazo también es largo. No tanto como el de las dos chicas, pero sirve como aperitivo del mes de abrazos que está por venir."
    call BlinkXS4("c32s007_245") from _call_BlinkXS4_2425
    eva "¿Qué le habéis hecho a [car]? Me ha dado un abrazo larguísimo. No es propio de ella."
    mc "*Risa* Creo que ella se está Marksificando un poco."
    call BlinkXS4("c32s007_250") from _call_BlinkXS4_2426
    ama "Hay muchas cosas que han empezado a cambiar por aquí."
    ama "Tener a [mc] y a Tía [bet] alrededor ha hecho que incluso [aar] acepte abrazos."
    call BlinkXS4("c32s007_255") from _call_BlinkXS4_2427
    mc "Habíamos pensado en llevarte a comer, pero no sabíamos cuánto ibas a tardar en llegar desde el aeropuerto."
    eva "Bueno, me he saltado todos los límites de velocidad de la isla para llegar lo más rápido posible."
    if eva._var("route") and ama._var("route"):
        eva "Pero tengo otros planes."
        scene c32s007_255d with dissolve
        eva "[ama], puedes quedarte o irte. Espero que te quedes."
        eva "Pero pienso meter a nuestro marido en esa habitación de ahí detrás ahora mismo."
        eva "Creo que [aar] y Tía [bet] tendrán que esperar un rato por su abrazo."
    else:
        scene c32s007_255d with dissolve
        eva "Lo de ir a comer me parece una idea fantástica. Tengo ganas de ver a [aar] y a Tía [bet]."
    return

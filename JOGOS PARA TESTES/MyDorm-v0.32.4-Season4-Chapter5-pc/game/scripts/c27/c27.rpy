label c27:
    $ mc._var("endOfSeason3", False)
    $ mc._var("preEndOfSeason3", True)
    if deb._var("route"):
        call c27s001_DebDate from _call_c27s001_DebDate
        call c27s002_AmaSimSamJam from _call_c27s002_AmaSimSamJam
        call c27s001_DebLewd from _call_c27s001_DebLewd
    else:
        call c27s001_NoDeb from _call_c27s001_NoDeb
        call c27s002_AmaSimSamJam from _call_c27s002_AmaSimSamJam_1
    call c27s002_AaronVC from _call_c27s002_AaronVC
    call c27s002_KiaEilNor from _call_c27s002_KiaEilNor
    call c27s002_AmaAtCollege1 from _call_c27s002_AmaAtCollege1
    call c27s002_LisShopping from _call_c27s002_LisShopping
    call c27s002_AmaAtCollege2 from _call_c27s002_AmaAtCollege2
    if mad._var("route"):
        call c27s003_MadLis from _call_c27s003_MadLis
        call c27s003_MadLewd from _call_c27s003_MadLewd
    else:
        call c27s003_NoMad from _call_c27s003_NoMad
        call c27s003_MadLis from _call_c27s003_MadLis_1
    #Day Change
    call c27s004_KatBreakfast from _call_c27s004_KatBreakfast
    call c27s004_MeeBetFarewell from _call_c27s004_MeeBetFarewell
    call c27s004_ScaInterview from _call_c27s004_ScaInterview
    call c27s005_PaintBasement from _call_c27s005_PaintBasement
    call c27s006_OmaHouse from _call_c27s006_OmaHouse
    if oma._var("route"):
        call c27s008_Oma from _call_c27s008_Oma
    else:
        $ mc._var("preEndOfSeason3", True)
        $ mc._var("endOfSeason3", True)
        call c27s008_NoOma from _call_c27s008_NoOma
    $ mc._var("preEndOfSeason3", True)
    if oma._var("route") and sai._var("route") and eil._var("route"):
        call c27s006_Teaser from _call_c27s006_Teaser
    elif oma._var("route"):
        call c27s006_NoThreesome from _call_c27s006_NoThreesome
    $ mc._var("endOfSeason3", True)
    ""
    return

label c27s001_DebDate:
    if _in_replay:
        call mrS3_deb_laptop from _call_mrS3_deb_laptop_2
        call mrS3_pregnancies(False, False, False, False, False, False, False, False, False, False) from _call_mrS3_pregnancies
        call numberOfPregnanciesS3 (False, False, False, False, False, False, False, False, False, False) from _call_numberOfPregnanciesS3
        if mc._var("numberOfPregnancies")==0:
            call mrS3_wantsChildren from _call_mrS3_wantsChildren
        call c26s008_DebTeaser from _call_c26s008_DebTeaser_1
    call BlinkXS3 ("c27s001_005") from _call_BlinkXS3_293
    play music ("music/Wonder.ogg")
    $ renpy.mark_label_unseen("c27s006_Teaser")
    $ renpy.mark_label_unseen("c27s006_NoThreesome")
    deb "Gracias, pero no intentes ruborizarme. Creo que ya lo has hecho suficiente con [kat] esta mañana."
    mc "No lo digo por ruborizarte, lo digo porque es verdad. Además, me encanta cómo te queda ese vestido."
    call BlinkXS3 ("c27s001_010") from _call_BlinkXS3_294
    deb "[kim] me ha dicho que... como tengo las piernas tan largas... un vestido asimétrico las realzaría."
    deb "No sé si creerla. Siempre he pensado que tengo las piernas {b}demasiado{/b} largas. No es una cosa que me guste realzar."
    mc "Cielo, no existen 'piernas {b}demasiado{/b} largas'."
    mc "Como se suele decir, las tuyas son tan largas que, al recorrerlas, apetece hacer un descanso a medio camino."
    call BlinkXPS3 ("c27s001_015" , "h") from _call_BlinkXPS3_2721
    deb "¡[mc]! ¡Eso ha sonado más travieso de lo que creo que querías sonar!"
    mc "*Risa* No te imaginas lo travieso que quería sonar."
    mc "Pero, ¿puedo besar a mi cita?"
    scene c27s001_015d with dissolve
    "La sirena no te contesta y toma la iniciativa por sí misma, besándote dulcemente. Los tacones y la diferencia de altura te hacen sentirte pequeño."
    "¡Cómo ha cambiado la nadadora! Ha pasado de inventarse juegos para robarte un beso a tomar la iniciativa."
    "Es un beso que te dejará con ganas de más cuando termine. Da lo mismo que dure un segundo o una hora."
    call BlinkXS3 ("c27s001_020") from _call_BlinkXS3_295
    "Cuando separa sus labios de los tuyos sientes una sensación de pérdida."
    deb "Vámonos antes de que tenga que llevarte a tu habitación a probar esa cama nueva."
    mc "*Risa* Ahora eres tú la que has sonado traviesa..."
    call BlinkXS3 ("c27s001_025") from _call_BlinkXS3_296
    deb "*Risa* Pero no más de lo que quería sonar."
    deb "Tengo intención de que me enseñes esa cama cuando volvamos de comer."
    "Otra vez te maravillas de lo mucho que ha evolucionado la siempre tímida [deb.nick]."
    mc "Entonces será mejor que nos vayamos. [emm] quería ser la primera en probar la cama."
    scene c27s001_025d with dissolve
    deb "Ya veremos..."
    mc "Me gusta esa nueva [deb.nick]. Pero espera..."
    call BlinkXS3 ("c27s001_030") from _call_BlinkXS3_297
    deb "¿Qué pasa?"
    mc "Quiero un beso antes de irnos."
    call BlinkXS3 ("c27s001_035") from _call_BlinkXS3_298
    deb "¡Soy idiota! ¡Estaba tan nerviosa por si te gustaría el vestido que ni he pensado en el beso!"
    mc "Y sigues nerviosa. Ya nos hemos besado."
    deb "¿Qué? ¿Cuándo?"
    mc "*Risa* Hace un minuto. Ven aquí."
    scene c27s001_035d with dissolve
    "Las tres pulgadas que [deb.nick] es más alta que tú, más los tacones suplen el escalón que ella está más abajo."
    "Por primera vez no tienes que inclinar tu cabeza hacia atrás para besarla. Lo echas de menos. Adoras la altura de la nadadora."
    call BlinkXS3 ("c27s001_040") from _call_BlinkXS3_299
    deb "Si me besas así, se me van a pasar los nervios. Pero creo que entonces podré pasar de la comida e ir directamente a ver esa cama."
    mc "Entonces dejaré de besarte hasta que acabemos de comer. Tengo muchas ganas de ir a comer contigo."
    call BlinkXS3 ("c27s001_045") from _call_BlinkXS3_300
    deb "Besar o comer. *Risa* Me pones entre la espada y la pared. Vámonos antes de que haga una locura."
    mc "Cualquier locura compartida me parecería bien. Pero podemos esperar a después de comer."
    stop music fadeout (1.5)
    call BlinkXPS3 ("c27s001_050" , "f") from _call_BlinkXPS3_2722
    "Una vez llegáis al restaurante..."
    play music ("music/Italy.ogg")
    deb "Es bonito. Me recuerda a un sitio en el que estuvimos hace un par de años, en Verona."
    deb "Se nota que es un decorado, pero está muy logrado."
    mc "¿Has viajado mucho fuera de Estados Unidos?"
    call BlinkXS3 ("c27s001_055") from _call_BlinkXS3_301
    deb "Un poco. Creo que este año es el primer verano que recuerdo sin ningún viaje al extranjero en los últimos 13 o 14 años."
    mc "¿En qué países has estado?"
    deb "Italia, Reino Unido, Portugal, España, Francia, Dinamarca, Suecia, Noruega, Suiza, Alemania, Grecia, Turquía, Japón, China, Australia, Nueva Zelanda, India, Vietnam..."
    call BlinkXS3 ("c27s001_060") from _call_BlinkXS3_302
    deb "¿Cuánto rato me vas a seguir dejando decir países?"
    mc "Pensaba dejarte hasta que recorrieras la ONU al completo. *Risa*"
    call BlinkXS3 ("c27s001_065") from _call_BlinkXS3_303
    deb "*Risa* No, qué va. En África sólo he estado en Marruecos, Túnez y Egipto. En Latino América sólo en México, Perú, Guatemala, Ecuador, Brasil y Colombia."
    deb "La Unión Europea la he recorrido entera, y de Asia me quedaban por decir Camboya y Tailandia. Creo que no me dejo ningún país de la lista..."
    mc "Es decir... unos 50 países en 13 o 14 años... es impresionante. Pero casi te daba tiempo a aterrizar y poco más, ¿no?"
    call BlinkXS3 ("c27s001_070") from _call_BlinkXS3_304
    deb "Bueno, en verano hacíamos viajes de un mes con mi madre cuando acababan las clases. Y después un par de semanas extras con mi padre en Agosto."
    deb "Suma a eso Acción de Gracias, Navidad... Quizás eran un par de meses viajando cada año. Y no son 50 países, sólo 48."
    mc "Sigue siendo impresionante."
    call BlinkXS3 ("c27s001_075") from _call_BlinkXS3_305
    deb "Hay países que me hubiera gustado ver más en profundidad. De algunos sólo he estado en una o dos ciudades."
    deb "Y hay otros a los que he ido varias veces, como Italia, Francia, España, Canadá..."
    mc "¿Tienes algún país favorito?"
    call BlinkXS3 ("c27s001_080") from _call_BlinkXS3_306
    deb "Muchos. No podría elegir uno. Cada país tiene su encanto, su cultura... Por norma mi país favorito es en el que estoy en ese momento."
    deb "Si empiezas a pensar cosas como 'esto era más bonito, o estaba más bueno, en otro sitio' no disfrutas lo que estás viviendo."
    deb "Me encanta viajar, y cuando estoy en un sitio sólo existe ese sitio. No puedo compararlo con otros."
    mc "Nunca lo había visto así. Siempre he oído a gente decir 'Estoy enamorado de Japón, Italia, o España'."
    mc "Tiene mucha más lógica cómo lo dices tú."
    call BlinkXS3 ("c27s001_085") from _call_BlinkXS3_307
    deb "¿Y tú? ¿En qué países has estado?"
    mc "De toda tu lista, sólo en Canadá. Fui a un concierto en Vancouver cuando estaba en Portland, el primer año."
    deb "¿Y sitios que no estén en mi lista?"
    mc "*Risa* Ninguno. No hemos viajado mucho, ni dentro ni fuera de Estados Unidos."
    mc "Pero estaré en Aruba, que no está en tu lista. *Risa*"
    call BlinkXS3 ("c27s001_090") from _call_BlinkXS3_308
    deb "Bueno, el status de Aruba como país es diferente a lo que estamos acostumbrados los americanos."
    deb "Casi sería como hablar de un estado de los Países Bajos. Como si habláramos de Virginia respecto a Estados Unidos."
    mc "Siempre he pensado que era un país independiente."
    call BlinkXS3 ("c27s001_095") from _call_BlinkXS3_309
    deb "Yo también. Nunca había leído nada sobre él hasta que decidiste irte allí."
    deb "Conozco gente que ha ido a hacer turismo, pero no sabía nada del país."
    mc "Es conmovedor que te preocupes así por mí."
    call BlinkXS3 ("c27s001_100") from _call_BlinkXS3_310
    deb "*Risa* Tenía que comprobar si iban a secuestrar a mi novio o algo así."
    mc "Creo que el riesgo de secuestro es más alto por parte de la empresa que del país."
    mc "*Risa* Y que me protejan de un posible secuestro también."
    deb "*Risa* Tienes razón. Yo no intentaría secuestrarte con [ama] o [eva] cerca. *Susurrando* Y un ejército de clones."
    call BlinkXS3 ("c27s001_105") from _call_BlinkXS3_311
    deb "Por suerte hoy no están en casa..."
    mc "Te noto muy traviesa hoy. *Risa* No me lo esperaba."
    call BlinkXS3 ("c27s001_110") from _call_BlinkXS3_312
    deb "Empecé a hacer bromas con [lis] anoche para ocultar lo insegura que me sentía."
    deb "¿Sabes lo de fingir una sonrisa hasta que sea real? Pues con las bromas sobre sexo funcionó. Tras varias bromas, dejé de preocuparme."
    deb "Empecé a verlo como la continuación de lo que hicimos en el lago. Se que es un paso más, y un paso muy importante, pero..."
    mc "Pero lo ves natural ahora, ¿no?"
    call BlinkXS3 ("c27s001_115") from _call_BlinkXS3_313
    deb "Lo veo el paso más natural del mundo. No es que no hayamos hecho cosas tórridas ya, con lo que el siguiente paso parece menos grande."
    deb "Y bromear anoche... y seguir bromeando contigo, hace que dé menos miedo."
    mc "Si tienes miedo..."
    call BlinkXS3 ("c27s001_120") from _call_BlinkXS3_314
    deb "De lo único que tengo miedo es de hacerte daño. *Risa* ¡Mis músculos son de acero!"
    mc "Preciosos músculos, por cierto."
    call BlinkXS3 ("c27s001_125") from _call_BlinkXS3_315
    deb "Pero no adelantemos acontecimientos y sigamos como si fuera una cita normal. ¿Cuál es tu libro favorito?"
    mc "¡Ufff! Esa es una pregunta complicada. Hay muchísimos libros que me gustan, pero si tuviera que elegir un favorito..."
    mc "Seguramente sería el tercero del Círculo del Tiempo. ¿Y el tuyo?"
    call BlinkXS3 ("c27s001_130") from _call_BlinkXS3_316
    deb "Yo lo tengo muy fácil. Orgullo y Prejuicio. Es el libro que me hizo amar los libros. Y por eso empecé a estudiar Literatura Inglesa."
    deb "He leído libros mejores, pero Orgullo y Prejuicio siempre tendrá un lugar especial en mi cabeza."
    mc "Suena a una relación especial con un libro. Yo también tengo un libro así, pero en sentido opuesto."
    mc "Estadística Avanzada (III) del último año de carrera. *Risa* Odié ese libro en cada una de sus páginas."
    call BlinkXS3 ("c27s001_135") from _call_BlinkXS3_317
    deb "*Risa* Puedo entenderlo. Hay libros académicos que parecen ser escritos para que odies cada momento que pasas estudiando esa asignatura."
    mc "Sí, hay profesores que deberían tener prohibido escribir libros."
    mc "Pero hablando de estudios, ¿por qué elegiste Newport?"
    call BlinkXS3 ("c27s001_140") from _call_BlinkXS3_318
    deb "Después de meses de chatear con Anthony, [lis] quería venir un fin de semana a conocerlo."
    deb "Cuando le dije que quería irme de Phoenix, empezó a planearlo todo para hacer el traslado aquí."
    deb "Tienen un buen programa de Literatura Inglesa y un entrenador conocido de natación, con lo que me pareció bien."
    mc "¿Cambiasteis de universidad por Anthony?"
    call BlinkXS3 ("c27s001_150") from _call_BlinkXS3_319
    deb "No, Anthony fue lo que hizo que [lis] se interesara por la NWU. Es una universidad pequeña que ni siquiera conocíamos."
    deb "Si no hubiera sido por él, habríamos acabado en alguna otra universidad. [lis] quería que estuviera en la costa."
    deb "De todas formas, sólo nos matriculamos para el curso de verano, con lo que era una decisión poco arriesgada para probar."
    mc "¿Sólo el curso de verano? Creía que os quedabais en septiembre también."
    call BlinkXS3 ("c27s001_145") from _call_BlinkXS3_320
    deb "Nos quedamos. Pero queríamos probar la universidad antes de decidir."
    deb "La universidad nos ha convencido lo suficiente. Y de todas formas yo no querría irme. Al menos no para volver a Phoenix."
    mc "Si quería costa, ¿cómo acabasteis en Phoenix en primer lugar?"
    call BlinkXS3 ("c27s001_155") from _call_BlinkXS3_321
    deb "Ella quería una universidad lejos de casa, para poder vivir su vida lejos donde nadie la conociera y lejos de la influencia de mi padre."
    deb "Cuando me tocó elegir universidad a mí, fui con ella."
    mc "Y después de un año, decidiste que querías irte de allí. ¿El clima?"
    call BlinkXS3 ("c27s001_160") from _call_BlinkXS3_322
    deb "No, un asistente de entrenador... demasiado cariñoso. Yo me sentía muy incómoda con él."
    deb "[lis] quería que lo denunciara, pero no tenía ninguna prueba, con lo que irme era lo mejor."
    mc "Cuando dices cariñoso..."
    call BlinkXS3 ("c27s001_165") from _call_BlinkXS3_323
    deb "Una mano que se escapa y toca donde no debe a la hora de corregir una postura. Abrazos que duran demasiado para celebrar victorias..."
    deb "Cosas así. Cosas que, visto desde fuera, pueden parecer que no son nada, pero cuando las vas sumando... te hacen sentir incómoda."
    mc "Es normal. ¿Cómo empezó? ¿Lo hacía con otras chicas también?"
    call BlinkXS3 ("c27s001_170") from _call_BlinkXS3_324
    deb "Cuando llegué, era muy simpático y me hizo sentir integrada en el equipo. Fue el primero que empezó a llamarme 'Deb'."
    if deb._var("laptop"):
        deb "Por eso me molestó cuando me lo llamaste tú. Sólo mi abuela y [lis] me llaman así y, si alguien aparte de ellas lo hace, lo voy a asociar con ese entrenador." id c27s001_DebDate_ea46801a
    else:
        deb "Por eso no me gusta que me llamen así. Sólo mi abuela y [lis] me llaman así y, si alguien aparte de ellas lo hace, lo voy a asociar con ese entrenador." id c27s001_DebDate_a42fff8c
    call BlinkXS3 ("c27s001_175") from _call_BlinkXS3_325
    deb "Poco a poco la cosa se fue poniendo más incómoda, pero como veía que con algunas de las otras chicas hacía lo mismo, pensé que era normal."
    deb "A ellas no parecía importarles. Era guapo y ellas se lo consentían. Pero a mí me molestaba. Intenté hablarlo con él, pero negó estar haciendo nada incorrecto."
    mc "Y decidiste irte. Si puedo hacer algo..."
    call BlinkXS3 ("c27s001_180") from _call_BlinkXS3_326
    deb "Gracias, pero no. Yéndome ha quedado resuelto."
    deb "Mis tiempos se resintieron. No iba a gusto a entrenar y se notaba. En dos años hay Juegos Olímpicos en París y me gustaría estar ahí."
    deb "Al menos intentarlo. Si seguía en Phoenix no iba a poder hacerlo. Con lo que el cambio es bienvenido."
    mc "¿Juegos Olímpicos? Entonces [sim] tenía razón. ¡Eres buenísima!"
    call BlinkXS3 ("c27s001_185") from _call_BlinkXS3_327
    deb "Ahora mismo no me clasificaría, pero si trabajo duro... Tengo una posibilidad. Quedan casi dos años para los Trials y sólo necesitaría unos meses para ponerme en forma."
    deb "Si Dara Vollmer y Dana Torres pudieron ganar medallas en las olimpiadas después de dar a luz...  " #Dara Torres y Dana Vollmer
    mc "No sé quiénes son. Supongo que nadadoras que han tenido hijos."
    call BlinkXS3 ("c27s001_190") from _call_BlinkXS3_328
    deb "Sí, las dos compitieron después de sus embarazos y las dos ganaron medallas en las olimpiadas. En Pekín y en Rio."
    deb "Pero claro, ellas eran mejores de lo que yo soy ahora antes de quedarse embarazadas..."
    mc "Te iba a preguntar si querías tener hijos, pero viendo que has investigado..."
    call numberOfPregnanciesS3 (False, False, False, False, False, False, False, False, False, False) from _call_numberOfPregnanciesS3_1
    call BlinkXS3 ("c27s001_195") from _call_BlinkXS3_329
    $ Aux = mc._var("numberOfPregnancies")
    if Aux == 10:
        deb "Todas las que se han hecho la prueba han salido positivas. Eso significa que quieres tener muchos hijos."
        deb "No me gustaría ser la única con la que no los tienes."
    elif Aux > 1 or mc._var("wantsChildren"):
        deb "Sabiendo que quieres tener hijos, me gustaría que los tuviéramos."
    else:
        deb "No sé si quieres tener hijos o no, pero a mí no me importaría."
    deb "Dentro de un año me afectaría más para mi carrera de nadadora. Si los quieres tener, ahora o justo después de unas olimpiadas serían los mejores momentos."
    mc "No había pensado en cómo te podría afectar en tu carrera. Me gusta que lo hayas hecho tú por los dos."
    call BlinkXS3 ("c27s001_200") from _call_BlinkXS3_330
    deb "Sé que quizás suene muy frío dicho así, pero uno de mis sueños es participar en unas olimpiadas. Y no quiero renunciar a él."
    mc "No te preocupes. No me ha sonado frío. Son cosas en las que, los que sólo hacemos deporte en los videojuegos, no solemos pensar."
    mc "Y, teniendo todo el tiempo del mundo para tener hijos, no tienes por qué renunciar a tus sueños."
    mc "Lo que me extraña es tu elección de estudios. ¿Literatura Inglesa en vez de algo relacionado con el deporte?"
    call BlinkXS3 ("c27s001_205") from _call_BlinkXS3_331
    deb "Mi segunda opción era Ciencias del Deporte, pero no estaba segura de si querría dedicarme a entrenar a otras nadadoras cuando dejase de nadar."
    deb "Sería una forma de seguir ligada al mundo de la natación, pero aún no estoy segura de querer hacerlo."
    mc "¿Prefieres ser una profesora de literatura en un instituto?"
    call BlinkXS3 ("c27s001_210") from _call_BlinkXS3_332
    deb "*Risa* Dudo que alguna vez pueda ser profesora de instituto. Los alumnos me tomarían el pelo. Hay que ser más dura de lo que soy yo para manejar un grupo de 20 adolescentes."
    deb "Elegí la carrera porque me encanta la literatura, no para ejercer. Ya sabes..."
    mc "Sí, dinero viejo y falta de necesidad de trabajar."
    call BlinkXS3 ("c27s001_220") from _call_BlinkXS3_333
    deb "Mas o menos. No somos dinero MUY viejo, pero lo suficiente. A principios del siglo pasado mi tatarabuelo era un pequeño granjero en Aurora."
    mc "De granjero a familia rica..."
    call BlinkXS3 ("c27s001_215") from _call_BlinkXS3_334
    deb "En la Gran Depresión y durante el Dust Bowl compró un montón de tierras a bajo precio en Illinois y Missouri. También algunas minas de plomo."
    deb "Él y mi bisabuelo diversificaron la fortuna durante la Segunda Guerra Mundial. Industria, investigación, contratos con el ejército..."
    deb "Nunca he sabido la lista completa de empresas en las que tenemos participación. Ni me interesa."
    mc "Supongo que tiene que ser complicado."
    call BlinkXS3 ("c27s001_225") from _call_BlinkXS3_335
    deb "Complicado y aburrido. Nunca me ha interesado el dinero. Quizás porque nunca me ha faltado."
    deb "A [lis], aunque tampoco le interese, siempre le ha gustado más todo lo que rodea el dinero. Alta sociedad, famosos, y todo eso."
    deb "Pero a mí no. El dinero tiene que servir para cubrir las necesidades propias y de la familia."
    mc "Es normal. En el fondo es para lo único que sirve. Una vez cubiertas las necesidades, el resto son caprichos."
    call BlinkXS3 ("c27s001_230") from _call_BlinkXS3_336
    deb "Por suerte, mis caprichos son relativamente baratos. *Risa* Libros, videojuegos, música..."
    mc "Hemos hablado de libros y videojuegos, pero nunca de música. ¿Qué música te gusta?"
    deb "Tengo gustos muy variados y que [lis] dice que no pegan demasiado. Pop, Folk, Blues, Metal, Rock, Clásica..."
    mc "*Risa* Es cierto que no pegan demasiado."
    scene c27s001_230d with dissolve
    deb "*Risa* Imagíname con una peluca barroca haciendo así. ¡Yeahhh!"
    mc "*Risa* Puedo hacerlo. Además, oliendo a pachuli, con un bolso de diseño y con una chaqueta de cuero."
    call BlinkXS3 ("c27s001_235") from _call_BlinkXS3_337
    deb "¡Ni siquiera yo iría así! *Risa* ¡[lis] no me dejaría salir de mi habitación! Bueno, de nuestra habitación."
    deb "Pero sea la música que sea, me gusta escucharla, no bailarla."
    mc "Bueno, en el Jazz Corner bailamos."
    call BlinkXS3 ("c27s001_240") from _call_BlinkXS3_338
    deb "No bailamos. Me hiciste volar."
    mc "La próxima vez te dejaré poner los pies en el suelo."
    deb "¿A riesgo de que te pise?"
    mc "Aceptaré ese riesgo. Aunque dudo que lo hagas. Deberías tener más seguridad en ti misma."
    mc "No eres [kim] y no vas a tropezarte con tus propios pies. Y ni siquiera ella me pisó."
    call BlinkXS3 ("c27s001_245") from _call_BlinkXS3_339
    deb "¡No te metas con [kim]! Yo sería incapaz de andar por una pasarela como lo hace ella."
    mc "No me estoy metiendo con ella. *Risa* Tan solo estoy haciendo una constatación de hechos."
    call BlinkXS3 ("c27s001_250") from _call_BlinkXS3_340
    deb "*Risita* Se puede tropezar con su sombra, ¿verdad?"
    mc "*Risa* Aún no la he visto hacerlo, pero estoy seguro de que sería capaz."
    mc "Tan solo estoy diciendo que si alguien como ella puede reunir la confianza para subirse a una pasarela, tu deberías reunirla para bailar."
    mc "Creo que tienes más miedo a lo que pensarán los que te vean que a pisarme."
    call BlinkXS3 ("c27s001_255") from _call_BlinkXS3_341
    deb "Un poco... No tengo demasiado ritmo..."
    mc "Pues aprovechando que te gustan los libros. Mark Twain dijo algo de lo que puedes aprender."
    mc "Tienes que bailar como si nadie te estuviera mirando, amar como si nunca te fueran a hacer daño, cantar como si nadie te estuviera escuchando y... algo más."
    call BlinkXS3 ("c27s001_260") from _call_BlinkXS3_342
    deb "...y vivir como si estuvieras en el cielo."
    deb "Lo segundo ya lo hago. Sé que no me vas a hacer daño. Lo del cielo... no soy creyente."
    mc "Pues hay que trabajar en el resto. Un día iremos tú y yo solos a bailar. A un sitio donde nadie te conozca."
    mc "Así, aunque te miren, dará lo mismo. ¿Qué te importa lo que piensen personas a las que no conoces?"
    mc "Yo estaré mirándote a los ojos, con lo que no sabré si bailas bien o mal. Ni me importará."
    call BlinkXS3 ("c27s001_265") from _call_BlinkXS3_343
    deb "¿Dónde has estado toda mi vida, [mc]?"
    mc "Esperando que vinieras a Newport."
    mc "Y cuando resolvamos lo de bailar, lo siguiente será un karaoke."
    call BlinkXS3 ("c27s001_270") from _call_BlinkXS3_344
    deb "¡No! *Risa* ¡Eso no, por favor!"
    deb "Una cosa es que no me veas bailar si estás mirándome a los ojos. Pero no vas a poder evitar escuchar lo mal que canto si vamos a un karaoke."
    mc "¿Tan mal cantas?"
    deb "Digamos que, si canto en la ducha, el champú se suicida. *Risa* No quiero torturar a nadie."
    mc "Entonces tendremos que hablar con [meg] para que te dé clases de canto."
    call BlinkXS3 ("c27s001_275") from _call_BlinkXS3_345
    deb "¿Sabes de lo que me acabo de dar cuenta?"
    mc "¿De qué?"
    deb "Esto no se parece a la típica cita de las películas."
    mc "¿Decepcionada?"
    call BlinkXS3 ("c27s001_280") from _call_BlinkXS3_346
    deb "Todo lo contrario. Es mucho mejor. Estamos hablando de un montón de cosas y no estoy nada nerviosa."
    mc "¿Por qué ibas a estar nerviosa? Tan solo estamos comiendo y charlando. Conociéndonos mejor."
    deb "Precisamente por eso. Todo es muy natural. Creía que iba a ser una situación tensa... ya sabes... por lo que vendrá después."
    mc "No he pensado ni por un momento en lo que vendrá después, [deb.nick]. Estoy disfrutando de cada minuto de esta comida contigo."
    call BlinkXS3 ("c27s001_285") from _call_BlinkXS3_347
    deb "Yo lo he pensado un par de veces, pero consigues que se me olvide. Es como estar comiendo... con un amigo..."
    mc "*Fingiendo sorpresa* ¿Ya no soy tu novio? *Risa*"
    mc "Hablando en serio, en eso consiste una cita. Creo que fuimos amigos antes que pareja, y eso no se debe perder."
    mc "No hay que estar hablando de amor y sentimientos todo el día, aunque suene poco romántico."
    call BlinkXS3 ("c27s001_290") from _call_BlinkXS3_348
    deb "Prefiero esto al romanticismo impostado. Para eso están los libros y los videojuegos."
    deb "Esto es más natural, más... auténtico. Pero no por ello menos sexy."
    deb "En realidad has estado hablando de amor todo el rato, interesándote por mí, queriendo llevarme a bailar..."
    deb "Si llevase bragas, las tendría mojadas después de todo lo que has dicho hoy."
    call BlinkXPS3 ("c27s001_290" , "h") from _call_BlinkXPS3_2723
    mc "*Susurrando* ¿No llevas bragas? Antes has dicho que estabas en modo travieso. Ahora me lo creo del todo."
    call BlinkXS3 ("c27s001_295a") from _call_BlinkXS3_349
    deb "Bueno, este vestido transparenta un poco dependiendo de cómo le dé la luz. [kim] y [lis] me han recomendado no llevarlas."
    deb "Además, han dicho que así habrá menos estorbos luego."
    call BlinkXS3 ("c27s001_295b") from _call_BlinkXS3_350
    deb "He estado de acuerdo con ellas. *Risita* Lo de no llevar sujetador ha sido idea mía."
    mc "Es decir... ¿me estás diciendo que estás desnuda debajo de ese ligero vestido?"
    mc "¿Sabes que ahora voy a ser yo el que no va a poder dejar de pensar en lo que pasará después?"
    call BlinkXS3 ("c27s001_300") from _call_BlinkXS3_351
    deb "*Risa* Creo que ha sido un error decírtelo. Ahora no vamos a poder dejar de pensar ninguno de los dos en eso."
    mc "A menos que reconduzcamos la conversación."
    scene c27s001_305An1 with dissolve
    "[deb.nick] mira a todos lados para comprobar que nadie os está mirando."
    scene c27s001_305AnBlink with dissolve
    deb "¿Estás seguro de que quieres que reconduzcamos la conversación?"
    mc "¡Eso es injusto! *Risa* ¡Ahora voy a tener que pedir la cuenta y nos vamos a quedar sin postre!"
    call BlinkXS3 ("c27s001_310") from _call_BlinkXS3_352
    deb "Nunca he sido de esas personas a las que les importa mucho el postre. Al menos hasta que empecé a probar los de [mar]."
    deb "Por muy buena que esté la comida aquí, creo que esa abuela italiana no está al mismo nivel que [mar]."
    if persistent.family:
        mc "*Risa* Dudo que haya mucha gente al mismo nivel que mi madre si se trata de postres. Ni siquiera [sam] o [nor], pese a que me encantan sus postres."
    else:
        mc "*Risa* Dudo que haya mucha gente al mismo nivel que [mar] si se trata de postres. Ni siquiera [sam] o [nor], pese a que me encantan sus postres."
    mc "¿Pido la cuenta, entonces?"
    call BlinkXS3 ("c27s001_315") from _call_BlinkXS3_353
    deb "Creía que ya la habrías pedido a estas alturas..."
    scene black with dissolve
    "Pides la cuenta, que tardan lo que te parece una eternidad en traer."
    "Por suerte, el camarero viene con el datáfono, ahorrándoos unos interminables segundos de espera por un segundo viaje."
    "Dejas una generosa propina y os marcháis."
    scene drive_day with fade
    stop music fadeout (1.5)
    "El viaje a casa se hace raro. ¿Ha estado siempre tan lejos tu casa del centro de la ciudad?"
    return
label c27s001_NoDeb:
    if _in_replay:
        call mrS3_lis_route from _call_mrS3_lis_route_7
        $ deb._var("route" , False)
        call mrS3_emm_route from _call_mrS3_emm_route_16
    scene c27s001_1000 with dissolve
    $ deb._var("chancePregnant" , True)
    "Después de que se vayan los montadores, juegas un rato a My Residence."
    "Tienes una cita más traviesa de lo esperado con Missy, la hermana deportista de Karen."
    "Desde que [deb.nick] te dijo lo de los parecidos, parece que estés alucinando."
    "Missy se parecería a la propia [deb.nick] si no fuera por el tamaño de sus tetas y porque es esgrimista en vez de nadadora."
    "Te preparas para bajar a comer en cuanto acabas la escena. Sabes que después de comer empezarán las visitas a ver... y a criticar... la cama."
    scene black with dissolve
    if lis._var("route"):
        call c27s001_DebVisit from _call_c27s001_DebVisit
    call c27s001_EmmVisit from _call_c27s001_EmmVisit
    return
label c27s001_DebLewd:
    if _in_replay:
        $ deb._var("route", True)
        call mrS3_meg_route from _call_mrS3_meg_route_3
        call mrS3_eva_route from _call_mrS3_eva_route_13
        if eva._var("route"):
            call mrS3_eva_choking from _call_mrS3_eva_choking
        call mrS3_lis_route from _call_mrS3_lis_route_8
        #call mrS3_emm_route from _call_mrS3_emm_route_17
    scene c27s001_320An with fade
    play music ("music/NightJazzBeats.ogg")
    "Al llegar a casa subís por las escaleras en un beso continuo. Vuestros labios están ansiosos del contacto con la boca del otro."
    "Casi podrías jurar que os habéis cruzado con alguien en las escaleras y los rellanos, pero no podrías asegurarlo."
    "El beso se hace corto. Las escaleras se hacen largas."
    call BlinkXPS3 ("c27s001_325" , "f") from _call_BlinkXPS3_2724
    "Llegáis a tu puerta sin aliento. El ascenso por las escaleras mientras os besáis hace que vuestros pulmones supliquen por un poco de aire."
    "Vuestros labios se separan reluctantemente para permitir la entrada del preciado gas."
    deb "¡Ufff! *Jadeo* Eso ha sido intenso."
    mc "Ahora no tienes que dudar entre besar y comer, con lo que..."
    call BlinkXS3 ("c27s001_330") from _call_BlinkXS3_354
    deb "Con lo que vamos a estrenar esa cama. No puedo esperar."
    mc "No hay por qué esperar, cielo. Sólo tienes que abrir la puerta que tienes a tu espalda."
    call BlinkXPS3 ("c27s001_335" , "f") from _call_BlinkXPS3_2725
    deb "Ya la he abierto y ya estamos dentro. ¿Ahora qué?"
    "Los nervios se reflejan en la cara de [deb.nick]. Los nervios y el deseo."
    deb "¿Me desnudo? Fue más fácil en el lago... tú llevabas la iniciativa... Y estaba casi desnuda."
    "Hablar va a servir de poco para calmarle los nervios."
    scene c27s001_345a with dissolve
    "Tus labios se posan en su hombro desnudo y puedes notar cómo un escalofrío la recorre de arriba a abajo."
    "La piel de gallina hace su aparición en el hermoso cuerpo de la nadadora."
    scene c27s001_345b with dissolve
    "Sin decir una palabra, continúas tu camino hacia la base de su cuello, repartiendo besos por el camino."
    deb "*Jadeo*"
    "Ella tampoco dice ni una palabra, pero su cuerpo y su agitada respiración dicen todo lo que necesitas saber."
    scene c27s001_345c with dissolve
    "Tus labios recorren su piel hasta su otro hombro, tan perfecto como el primero. Sus músculos siguen tensos."
    deb "*Gemido* *Respiración agitada*"
    "Sabes que las palabras sobran en este momento. No puedes decir nada que la calme, pero puedes hacer que se sienta deseada."
    "Porque realmente deseas lo que está a punto de pasar."
    scene c27s001_350An with dissolve
    "Con un lento movimiento de tu mano descubres uno de los deliciosos pechos de [deb.nick]."
    deb "*Jadeo*"
    "Sabes que se siente acomplejada por el tamaño de sus ridículamente perfectos pechos."
    "No hay absolutamente nada que desearas cambiar de ellos en este momento."
    scene c27s001_350d with dissolve
    "Llevas tus labios a su duro pezón y empiezas a juguetear con él."
    "Por un momento, en el restaurante cuando se ha bajado el vestido, has creído que le habías demostrado que no tiene por qué sentirse así."
    deb "*Gemido*"
    "Es el momento de seguir haciéndolo. Nunca te cansarás de jugar con sus pezones, que reaccionan a cada roce de tus labios."
    scene c27s001_355An with dissolve
    "Sin dejar de lamer el primer pezón, tu mano descubre el segundo. Igual de duro que el que tienes entre los labios."
    deb "*Jadeo*"
    "La piel de gallina sigue aumentando en el cuerpo perfectamente depilado de la sirena."
    scene c27s001_360a with dissolve
    "Cambias de pezón, dedicándote a lamerlo en vez de tan solo besarlo."
    "Tu mano se dispara a acariciar el pezón que tus labios han abandonado, húmedo con tu saliva."
    deb "*Gemido* Me encanta... *Gemido*" id c27s001_DebLewd_f2083693
    "Las primeras palabras que sus labios dejan escapar entre gemidos son para indicarte que estás en el buen camino."
    scene c27s001_365a with dissolve
    "Empiezas a recorrer su cuerpo con tu mano libre, hasta llegar a su musculoso muslo, tan duro como una roca."
    "En ese momento recuerdas lo que ha dicho de la falta de bragas."
    scene c27s001_370d with dissolve
    "Decides comprobarlo sutilmente. En vez de levantar el vestido directamente, abandonas sus pechos y bajas a besar las marmóreas columnas que son sus piernas."
    "Si los antiguos griegos hubieran tenido estos materiales, no habría tantos templos derruidos en el mundo."
    deb "*Jadeo*"
    "Sin embargo, no puedes imaginarte cómo quedarían unos templos si las columnas tuvieran la piel de gallina."
    scene c27s001_370a
    deb "*Gemido* Es una dulce tortura... *Jadeo* Esperar a que llegues a tu destino. *Gemido*"
    mc "¿Tienes prisa? ¿Algún sitio en el que estar?"
    deb "*Jadeo* No hay ningún sitio en el que quisiera estar ahora mismo excepto aquí. *Gemido*"
    mc "Entonces, disfruta de la tortura."
    scene c27s001_370e with dissolve
    "Finalmente, decides comprobar la falta de bragas. Un poco de anticipación está bien. Si entra en el terreno de la dulce tortura, es aún mejor."
    "La línea en la que la palabra 'dulce' desaparece puede ser borrosa."
    "Encuentras un monte de Venus perfectamente depilado, una vagina intensamente fragante y húmeda."
    scene c27s001_375e with hpunch
    "Sin poder resistirte, metes tu cabeza bajo el vestido, tu lengua en su vagina."
    deb "*GEMIDO* ¡Oh, sí! *JADEO*"
    "El cuerpo de la sirena se estremece por un momento."
    call BlinkXS3 ("c27s001_375") from _call_BlinkXS3_355
    deb "¿No me vas a desnudar para hacer eso?"
    mc "No pensaba que fuera necesario; eso ya lo hicimos en el lago. Hoy es un día para nuevas experiencias."
    mc "Además, llevo pensando en esto desde que me has dicho que no llevabas bragas."
    scene c27s001_375xAn with dissolve
    pause (2.0)
    call BlinkXS3 ("c27s001_375x") from _call_BlinkXS3_519
    deb "Prefiero verte a que tengas la cabeza debajo de mi vestido."
    scene c27s001_970pv with dissolve
    show c27s001_970v with dissolve
    "Vuelves a hundir tu cabeza entre sus piernas. Tu lengua saluda a su clítoris y la nadadora vuelve a estremecerse. Sabes que tienes que prepararla para lo que está por llegar."
    deb "*GEMIDO* ¡Justo ahí! *JADEO*"
    "Los gemidos de [deb.nick] son tan intensos como su sabor. Supones que ella también ha estado pensando en esto desde hace mucho. Quizás desde que se ha puesto el vestido."
    deb "*JADEO* ¡Es mejor que en el lago! *GEMIDO*"
    "Es terreno conocido para ella, ahora. Los nervios que tenía tumbada sobre aquella roca han desaparecido. Sabes que volverán cuando deis el siguiente paso."
    scene c27s001_970An with dissolve
    "La nadadora separa una de sus piernas para darte mejor acceso a su tesoro."
    deb "*GEMIDO* ¡Así mejor! *JADEO*"
    "Estás de acuerdo. Ni siquiera piensas en que está poniendo su zapato en el marco de la cama nueva."
    "Tampoco te importaría."
    "No es un gato."
    show c27s001_975v
    hide c27s001_970v
    "Con un acceso más libre a su centro de placer, tu lengua recorre cada pliegue y cada curva de su vagina, empapándose de su sabor."
    deb "*GEMIDO* ¡Esto es portentoso! *JADEO* ¡Voy a tener un orgasmo colosal! *GEMIDO*"
    "La estudiante de literatura empieza a usar palabras que normalmente no estarían en tu vocabulario."
    deb "*JADEO* ¡Voy a correrme! *GEMIDO* ¡No voy a poder refrenarlo! *JADEO*"
    "Creías que la tensión en su pierna, que no has dejado de acariciar, se debía a que estaba aguantando casi todo su peso sobre ella."
    "Te maravillabas de que pudiera aguantar el equilibrio sobre esos tacones con una sola pierna."
    deb "*GEMIDO* ¡Ya llega! *JADEO*"
    "Pero tan sólo era su orgasmo acercándose."
    call OrgasmXS3 ("c27s001_380") from _call_OrgasmXS3_70
    hide c27s001_970v
    deb "*GEMIDO* ¡SÍ! *JADEO* ¡INCREÍBLE! *GEMIDO*"
    "La sirena explota en tu boca, inundando tus sentidos con su aroma y su sabor."
    "Sus estremecimientos hacen que temas por su equilibrio por un momento, pero es capaz de mantenerlo apoyando un pie en la cama."
    call BlinkXPS3 ("c27s001_385" , "f") from _call_BlinkXPS3_2726
    "Al cabo de unos segundos..."
    deb "*Respiración entrecortada* Eso ha sido alucinante... pero necesito sentarme... las piernas no me aguantan..."
    mc "¿Sofá o cama?"
    scene c27s001_390An with dissolve
    deb "*Respiración entrecortada* Dudo que pueda llegar al sofá... Me tiembla todo."
    mc "Ahí estás preciosa."
    deb "*Respiración entrecortada* Puedes aprovechar para desnudarte mientras recupero la respiración..."
    scene c27s001_390e with fade
    "No te lo piensas ni un segundo. Tu ropa desaparece de tu cuerpo a una velocidad asombrosa antes de sentarte al lado de la hermosa mujer."
    deb "*Risa* Eso ha sido rápido. ¿No querías que me sintiera indefensa siendo la única que estaba desnuda?"
    mc "*Risa* Si quieres pensar que ha sido por eso..."
    mc "Pero no te voy a mentir. *Risa* No creo que te puedas sentir indefensa con esos hermosos músculos por todos lados."
    call BlinkXS3 ("c27s001_395") from _call_BlinkXS3_356
    deb "Sigo flipando con que no los consideres poco femeninos."
    mc "¿Qué tiene que ver la femineidad con tus músculos? No estamos hablando de que tengas unos bíceps como tu cabeza."
    mc "Tienes músculos por todos lados, pero en una proporción perfecta."
    mc "Quien piense que eres poco femenina no te ha visto con ese vestido... o sin él."
    call BlinkXS3 ("c27s001_400") from _call_BlinkXS3_357
    deb "¿Sabes que me pone muy cachonda que me digas esas cosas? Siempre he creído que... a los chicos no os gustaban las chicas con más músculos que vosotros."
    mc "¿Sabes que una erección no se puede fingir? Si estoy así es porque me gustas, [deb.nick]."
    call BlinkXS3 ("c27s001_405") from _call_BlinkXS3_358
    deb "Pues espero que te guste lo siguiente. Espero no hacerte daño con los dientes hoy."
    "Por un momento te sientes sorprendido. Creías que la preciosa mujer iba a ir a por el paso definitivo."
    "Pero entiendes que debe estar nerviosa, y seguir el camino conocido, el camino que ya recorristeis en el lago, es una forma de calmar esos nervios."
    "Es una forma de que cada paso sea tan solo un incremento sobre lo que ya habéis hecho."
    mc "No te preocupes. La última vez lo conseguiste hacer muy bien una vez te avisé del problema."
    mc "Casi parecía que tuvieras dientes retráctiles."
    call BlinkXS3 ("c27s001_410") from _call_BlinkXS3_359
    deb "*Risa* Acabas de sonar como si tuviera dientes de broma, de esos de vampiro para Halloween."
    mc "*Risa* No lo había pensado pero es un buen símil. No te tienes que preocupar por nada. Con esos dientes de Halloween seguro que lo haces genial."
    call BlinkXS3 ("c27s001_415") from _call_BlinkXS3_360
    deb "Y esta es una de las razones por las que te quiero. Haces que todo parezca tan fácil..."
    deb "Casi no me acuerdo de que debería estar nerviosa por lo que pasará después."
    mc "Solo pasara lo que..."
    scene c27s001_420a with hpunch
    "No te deja acabar la frase. Se lanza a tus labios con un beso ansioso, en el que hay tanta pasión como deseo. Pero no hay dudas. Esas se quedaron en el lago."
    "Su lengua recorre tus encías de una forma que la [deb.nick] de hace un par de semanas ni siquiera sabía que existía."
    "Cuando acaba con tus encías se entrelaza con tu lengua, en un baile para dos que casi parece un combate de anacondas."
    scene c27s001_420b with dissolve
    "Sin decir una palabra, interrumpe el beso de una forma tan abrupta que te deja boqueando como un pececillo en busca de aire."
    "Como un amante en busca la boca de su pareja."
    "Sus labios bajan a tu pecho repartiendo besos, haciendo el mismo camino que tú recorriste en su cuerpo encima de aquella roca."
    "Camino conocido, aunque en tu cuerpo en vez de en el suyo."
    scene c27s001_420c with dissolve
    "Conocías el siguiente paso que iban a dar sus labios antes de que abandonaran tu pecho."
    "Está copiando cada uno de tus movimientos, sabiendo lo mucho que le gustaron a ella."
    "Es una muestra más de la generosidad de la altísima mujer. Si ella lo disfrutó, tú también debes hacerlo."
    scene c27s001_420d with dissolve
    "Por fin, su boca llega a tu glande, el cuál besa profusamente. Lo de esta chica te está contagiando. Incluso la voz en tu cabeza empieza a sonar culta."
    "No hay rastro de sus dientes. Tan solo unos labios húmedos y calientes, con el ocasional roce de una lengua más húmeda aún."
    "Una respiración agitada que hace vibrar la punta de Mjolnir con cada beso."
    scene c27s001_425An with dissolve
    "Un gesto inesperado te sorprende profundamente cuando [deb.nick] lleva tu mano a su cabeza."
    mc "Eso es nuevo, [deb.nick]. La última vez no lo necesitaste..."
    call BlinkXS3 ("c27s001_430") from _call_BlinkXS3_361
    deb "La última vez quería ver si era capaz de hacerlo y descubrí que lo era."
    deb "Hoy quiero que tú marques el ritmo. Quiero que seas tú quien lleve la iniciativa y me pares cuando estés cerca." id c27s001_DebLewd_eadd58b9
    deb "Hoy quiero tu leche dentro de mí."
    mc "Pero las Olimpiadas... Un embarazo..."
    call BlinkXS3 ("c27s001_435") from _call_BlinkXS3_362
    deb "Ya te he dicho que ahora sería el mejor momento. O eso o esperar a después de París, si llego a ir."
    deb "Pero sólo si tú quieres."
    scene c27s001_980pv with dissolve
    show c27s001_980v
    "No te deja tomar una decisión. No es necesario tomarla todavía. Habrá tiempo más tarde."
    "Se mete tu polla en la boca y empieza una mamada no demasiado profunda."
    "Prefiere dedicarse a jugar con su lengua alrededor de la punta de Mjolnir."
    "Ahora no sabrías decir quién es la anaconda. Tampoco te importa demasiado."
    deb "*Gemido inquisitivo*"
    mc "Lo estás haciendo perfecto, [deb.nick]."
    "Realmente no le estás marcando ningún ritmo. Tu mano tan solo está apoyada en su cabeza, dándole una sensación de seguridad que no necesita."
    scene c27s001_985pv with dissolve
    show c27s001_985v
    hide c27s001_980v
    "En otras circunstancias estarías usando la mano que tienes en su cabeza para masajear su delicioso y húmedo coño."
    "Para ir poniéndola cachonda poco a poco en preparación para el siguiente paso."
    deb "*Gemido*"
    "Sus gemidos sobre tu polla, maravillosos gemidos, te dicen que no es necesario."
    "Tener en su boca lo que en breve tendrá en su coño es suficiente para que su excitación vaya en aumento."
    deb "*Jadeo*"
    "Estás seguro de que esos pensamientos están pasando por la mente de la nadadora en ese momento."
    scene c27s001_990pv with dissolve
    show c27s001_990v
    hide c27s001_985v
    "Sus labios alrededor de tu polla, haciendo la presión justa, mientras su lengua juguetea con la punta, hacen que te estés acercando a tu orgasmo."
    deb "*Gemido inquisitivo*"
    "Sus cambios de ritmo, sin necesidad de que tu mano le indique nada, son increíbles."
    "Aún te queda mucho, pero no quieres quedarte a punto de correrte. Quieres que disfrute su primera vez y quieres durar lo suficiente para proporcionarle el placer que merece."
    mc "Todavía me queda, pero puedes ir parando."
    "Entrar en ella y correrte inmediatamente no sería lo adecuado. Ni con ella ni con nadie."
    call BlinkXS3 ("c27s001_440") from _call_BlinkXS3_363
    "Retiras la mano de su cabeza para indicarle que pare."
    deb "¿Estoy haciendo algo mal?"
    mc "Justo lo contrario. No quiero quedarme demasiado cerca de correrme."
    deb "Entonces... ¿me tumbo?"
    mc "Creo que para la primera vez sería lo mejor. Habrá tiempo de probar otras posturas."
    call BlinkXPS3 ("c27s001_445" , "f") from _call_BlinkXPS3_2727
    "La preciosa muchacha se tumba en la cama, con el culo en el borde de la cama, ofreciéndote una vista maravillosa de su cuerpo desnudo."
    deb "¿Así estoy bien?"
    mc "Como estés más cómoda. Esa es una buena posición, pero si te apetece cualquier otra..."
    deb "*Risita* Me apetece esta. Prométeme que serás delicado."
    scene c27s001_900pv with dissolve
    show c27s001_900v
    hide c27s001_990v
    "Te sitúas entre sus piernas, frotando tu glande contra su húmeda raja. Lubricando a Mjolnir para que la penetración sea lo más delicada posible."
    mc "Te lo prometo. ¿Nerviosa?"
    deb "Un poco. Pero también ansiosa por hacerlo."
    deb "Además, en esta postura me siento a tu merced... y me gusta. Tú eres el que tienes la experiencia."
    "No crees que [deb.nick] sea de esas mujeres a las que les guste ser dominadas."
    "Ha estado bajo el dominio de [lis] durante años y, aunque era un dominio benévolo, es más feliz desde que se lo ha quitado de encima."
    mc "¿Preparada? Recuerda que tienes que relajarte."
    deb "Adelante."
    scene c27s001_905pv
    scene c27s001_905dv
    $ renpy.movie_cutscene("c27/c27s001_905vid.webm")
    #pause (3.03)
    "Metes tu polla poco a poco dentro de la chica, esperando alguna expresión de dolor para parar cuando se produzca."
    deb "*Jadeo*"
    "Ese único jadeo es la única muestra de incomodidad que deja escapar [deb.nick]."
    "Has hecho un buen trabajo preparándola para este momento."
    call BlinkXS3 ("c27s001_450") from _call_BlinkXS3_364
    mc "¿Estás bien, cielo?"
    deb "¿Ya está? ¿Ya no soy virgen?"
    mc "No, no lo eres. Pero ¿estás bien? ¿Sientes dolor?"
    call BlinkXS3 ("c27s001_455") from _call_BlinkXS3_365
    deb "No hay dolor. Una sensación de extrañeza y de incomodidad, pero no hay dolor."
    deb "Me siento... llena. ¿Qué tal tú?"
    mc "¿Yo? ¡Fantástico! Apretujado entre paredes de acero super estrechas."
    call BlinkXS3 ("c27s001_460") from _call_BlinkXS3_366
    "La presión desaparece como por arte de magia. O, para ser más exactos, en vez de parecer que Mjolnir está entre paredes de acero, parece estar en un guante de terciopelo."
    "Un guante que aprisiona, pero no estruja."
    mc "*Jadeo sorprendido* ¿Qué has hecho?"
    deb "[meg] me dio consejos sobre cómo usar el suelo pélvico durante el sexo."
    deb "Bueno, nos ha dado consejos a todas... ¿No te gusta?"
    mc "Me encanta, pero me sorprende. *Risa*"
    scene c27s001_460An with dissolve
    "[deb.nick] empieza a contraer y a relajar su vagina voluntariamente. Es una sensación alucinante."
    if meg._var("route"):
        "Te preguntas, si [meg] sabe hacer esto, por qué no lo ha hecho cuando habéis estado juntos."
        "Quizás tenga que ver con que la nadadora es más musculosa que la cantante."
    deb "¿Te gusta?"
    mc "¡Me encanta! Es... no sé cómo describirlo..."
    "Las sensaciones que recorren tu astil cuando aprieta y relaja sus músculos rítmicamente son como una presión que va desde la base hasta la punta."
    "Pero hay mucho más involucrado en ello. Es algo diferente de lo que has experimentado nunca."
    call BlinkXS3 ("c27s001_465") from _call_BlinkXS3_367
    deb "*Risita* Y yo siempre creí que los ejercicios de Kegel eran una tontería... ¡Ahora son útiles!"
    mc "*Risa* MUY útiles. Pero cuando estés preparada, deberías relajar esos músculos sobre los que tienes tanto control."
    call BlinkXS3 ("c27s001_470") from _call_BlinkXS3_368
    deb "Creo que ya estoy preparada. La incomodidad ha desaparecido."
    mc "Voy a empezar a moverme. Avísame si vuelve la incomodidad. O si aparece dolor."
    deb "Adelante..."
    scene c27s001_910pv with dissolve
    show c27s001_910v
    hide c27s001_900v
    "Empiezas a mover las caderas lentamente, atento a cualquier señal de que [deb.nick] no esté disfrutando."
    deb "*Gemido* ¡Oh, sí! *Jadeo* Así... lentamente... *Gemido*"
    "No puedes notar ninguna expresión de dolor en su rostro y poco a poco vas dejando de preocuparte."
    "Su cara tan solo refleja placer."
    scene c27s001_915pv with dissolve
    show c27s001_915v
    hide c27s001_910v
    "Encajáis como si estuvierais hechos el uno para el otro. Porque estáis hechos el uno para el otro."
    deb "*Jadeo* ¡Me encanta! *Gemido* ¡Es mucho mejor que lo de antes! *Jadeo*"
    "[deb.nick] intenta sincronizar los movimientos de sus músculos pélvicos con cada embestida."
    "No es sencillo para ella con todas las sensaciones que están recorriendo su cuerpo en este momento."
    "Pero lo intenta. Y cuando lo consigue, el resultado es alucinante."
    scene c27s001_920pv with dissolve
    show c27s001_920v
    hide c27s001_915v
    "Continúas bombeando lentamente, dándole a la nueva cama el mejor primer uso en el que nadie podría haber pensado."
    deb "*Gemido* ¡Oh, sí! *Jadeo* ¡Creo que te odio! *Gemido*"
    "No pierdes el suave ritmo al que se mueven tus caderas pese a la sorprendente frase."
    mc "¿Qué? ¿Por qué? ¿Qué he hecho?"
    "Por un momento piensas que le has hecho daño, pero su lenguaje corporal te indica lo contrario."
    scene c27s001_925pv with dissolve
    show c27s001_925v
    hide c27s001_920v
    "Su intensa mirada cada vez que te mira te dice que no te odia por eso."
    deb "*Jadeo* Por haberme dejado decidir que no hiciéramos esto en el lago. *Gemido* ¡Tenía tanto miedo que me perdí algo maravilloso! *Jadeo*"
    "Estás a punto de reírte. Ciertamente tenía miedo, y ciertamente fue una oportunidad perdida."
    "Pero tendréis todo el tiempo del mundo para recuperar el tiempo perdido."
    mc "Nunca te forzaré a hacer algo que no quieras hacer, cielo."
    "La han dominado demasiado durante toda su vida. Sus padres, [lis], sus entrenadores..."
    "No vas a ser el siguiente en esa lista de gente que le dice qué tiene que hacer y cuándo hacerlo."
    scene c27s001_475An with dissolve
    "Entonces llega la siguiente sorpresa de un día lleno de sorpresas."
    deb "*Gemido* Así mejor. *Jadeo* ¡Hazme tuya! *Gemido*"
    "Acabas de decirle que no la forzarás a hacer algo que no quiera hacer. ¿Incluye eso no dejarle probar lo que quiere?"
    call BlinkXS3 ("c27s001_475") from _call_BlinkXS3_369
    mc "¿Estás segura? No es algo que esperara de ti."
    deb "Todo el mundo me ha dominado toda mi vida, [mc]. Si quieres hacer esto, estoy dispuesta."
    $ deb._var("chanceChoking" , True)
    if persistent.walkthrough:
        $ wt1 = _("Probar el fetiche de asfixia con [deb.nick].")
        $ wt2 = _("No probar el fetiche de asfixia con [deb.nick].")
    else:
        $ wt1 = ""
        $ wt2 = ""
    menu:
        "Mantener tu mano en su cuello." (wt=wt1):
            $ deb._var("choking", True)
            scene c27s001_930pv with dissolve
            show c27s001_930v
            hide c27s001_925v
            "Sin ejercer demasiada presión en su cuello, empiezas a bombear con tus caderas. Suavemente."
            deb "*Gemido* Puedes apretar más si quieres. *Jadeo*"
            "Su actitud te sigue sorprendiendo. No podías esperar que la romántica [deb.nick] se comportara así."
            deb "*Jadeo*"
            "Tu mano busca la presión adecuada para darle la sensación que pide, pero a su vez no hacerle daño."
            "Esto no debería ser un juego de dominación."
            scene c27s001_935pv with dissolve
            show c27s001_935v
            hide c27s001_930v
            "Tu mirada se desplaza al espacio entre vuestros cuerpos, con una visión perfecta de su musculoso cuerpo recibiendo a Mjolnir."
            deb "*Gemido*"
            "Podrías estar mirando sus preciosos y pequeños pechos por horas. Sus increíbles abdominales por años."
            "El contraste entre vuestros tonos de piel es una visión que se graba en tus retinas para siempre."
            deb "*Jadeo*"
            scene c27s001_940pv with dissolve
            show c27s001_940v
            hide c27s001_935v
            "No te atreves a acelerar el ritmo, pese a que puedes notar cómo su cuerpo empieza a tensarse."
            "Si aceleras demasiado, corres el riesgo de perder el control y apretar su garganta más allá de la confortable presión que estás ejerciendo ahora mismo."
            deb "*Gemido estrangulado*"
            "Cuando la escuchas gemir, te das cuenta de que la forma de tensarse no es la que anuncia la llegada de un orgasmo."
            mc "¿Pasa algo, [deb.nick]? ¿Te duele? ¿Te molesta?"
            "Tu tono preocupado saca a la chica del pseudo trance en el que está."
            call BlinkXS3 ("c27s001_480") from _call_BlinkXS3_370
            deb "¿Puedes quitar la mano de mi cuello, por favor? No me está gustando."
            mc "Me lo tendrías que haber dicho antes."
            "Retiras tu mano de su cuello."
            call BlinkXS3 ("c27s001_485") from _call_BlinkXS3_371
            mc "¿Por qué me has pedido hacerlo, si no te gusta?"
            deb "No sabía si me iba a gustar, pero quería probarlo por ti."
        "Retirar la mano." (wt=wt2):
            $ deb._var("choking", False)
            mc "No es algo que me guste hacer, [deb.nick]."
            call BlinkXS3 ("c27s001_485") from _call_BlinkXS3_372
            "Retiras la mano."
            deb "*Suspiro* ¡Menos mal! No es algo que quiera hacer, pero estaba dispuesta a hacerlo si tú querías."
            mc "¿Por qué me has pedido hacerlo, si no quieres hacerlo?"
    $ resetWalkthrough()
    call BlinkXS3 ("c27s001_490") from _call_BlinkXS3_373
    deb "Como te he dicho antes, todo el mundo..."
    mc "Sí, todo el mundo te ha dominado siempre. Pero eso no es para nosotros, [deb.nick]."
    mc "Tenemos que hacer cosas que nos gusten a los dos, no sólo que me gusten a mí."
    if not deb._var("choking"):
        mc "Y, en este caso, ni siquiera me gusta."
    call BlinkXS3 ("c27s001_495") from _call_BlinkXS3_374
    deb "Entonces sigue lo que estabas haciendo al principio, pero más duro."
    mc "Así sí. Si te gusta algo de alguna forma concreta, dilo."
    scene c27s001_945pv with dissolve
    show c27s001_945v
    hide c27s001_940v
    "Vuelves a bombear, con tus manos otra vez sobre el colchón. Esta vez aceleras un poco el ritmo tal como te ha pedido."
    deb "*GEMIDO* ¡OH, SÍ! *JADEO* ¡MUCHO MEJOR ASÍ! *GEMIDO*"
    "Ya no tiene fuerza para mirarte entre embestidas, o tan solo se dedica a disfrutar de los embates de Mjolnir."
    deb "*JADEO* ¡ESTE RITMO ME ENCANTA! *GEMIDO* ¡Podrías haber empezado así! *JADEO*"
    "Dudas que hubiera disfrutado en su primera vez si hubieras empezado con este ritmo, pero decides no decir nada sobre ello."
    scene c27s001_955pv with dissolve
    show c27s001_955v
    hide c27s001_945v
    "Sus preciosos pechos moviéndose al ritmo de los golpes de tu ariete tienen algo de hipnótico."
    "No puedes entender cómo se podía sentir avergonzada de esos dos pequeños montes de perfección."
    deb "*GEMIDO* ¡ESTOY A PUNTO DE CORRERME OTRA VEZ! *JADEO* ¡ES INCREÍBLE! *GEMIDO*"
    "Como si fuera un pensamiento que se le había olvidado mientras disfrutaba de cada arremetida, vuelve a usar sus músculos de Kegel."
    "Había dejado de usarlos durante la conversación sobre el agarrarla por el cuello, y no había vuelto a ponerlos en funcionamiento."
    "El incremento de placer es instantáneo y maravilloso. Para ambos. Esta vez sincroniza sus movimientos con los tuyos." id c27s001_DebLewd_fe6bd9c7
    mc "*Jadeo*"
    deb "*JADEO*"
    scene c27s001_950pv with dissolve
    show c27s001_950v
    hide c27s001_955v
    "Vuestros orgasmos empiezan una involuntaria carrera para ver cuál de los dos llega antes."
    "Has hecho bien en parar la mamada cuando lo has hecho o ya te habrías corrido a estas alturas, a pesar de las interrupciones."
    deb "*JADEO* ¡ESTOY LLEGANDO! *GEMIDO* ¡CÓRRETE DENTRO! *JADEO*"
    "Tú también estás llegando. Por tu mente pasan Olimpiadas, embarazos, una carrera de natación frustrada..."
    "Pero también pasa por tu cabeza su comentario sobre que ahora es el mejor momento y una imagen de [deb.nick] con un bebé en brazos."
    if persistent.pregnancy:
        "Tanto ella como el bebé sonríen."
    $ deb._var("chancePregnant" , True)
    if persistent.pregnancy:
        if persistent.walkthrough:
            $ wt1 = _("[deb.nick] embarazada.\n No afectará demasiado a su carrera de natación.")
            $ wt2 = _("Sin consecuencias.")
        else:
            $ wt1 = ""
            $ wt2 = ""
        menu:
            "Correrte dentro. Ir a por el bebé." (wt = wt1):
                $ deb._var("pregnant", True)
                $ deb._var("undiscoveredPregnancy", True)
                play sound ("music/OldMusicBox5.ogg")
            "Correrte dentro." (wt = wt2):
                pass
    $ resetWalkthrough ()
    call OrgasmXS3 ("c27s001_500") from _call_OrgasmXS3_71
    deb "*GEMIDO* ¡SÍ! *JADEO*"
    mc "¡Mpfft!"
    "Vuestros orgasmos llegan simultáneamente. Sus músculos se cierran sobre Mjolnir mientras éste escupe su carga dentro de la muchacha."
    "Siempre has oído lo de que el tamaño no importa. Da lo mismo que [deb.nick] sea la mujer más alta con la que has estado."
    "Tu semilla se sale de su interior una vez su útero y su vagina se llenan hasta el borde."
    call BlinkXPS3 ("c27s001_505" , "f") from _call_BlinkXPS3_2728
    "Cuando vuestros orgasmos finalizan al cabo de un rato, el suyo durando más que el tuyo..."
    mc "¿Qué tal estás? ¿Dolor? ¿Incomodidad?"
    deb "Cansancio. Y eso que todo el trabajo lo has hecho tú."
    deb "Túmbate a mi lado."
    call BlinkXPS3 ("c27s001_510" , "f") from _call_BlinkXPS3_2729
    mc "Entonces, ¿no hay dolor?"
    deb "Siento como si me hubieran martilleado ahí abajo... *Risita* Mjolnir se ha ganado el nombre."
    deb "O a lo mejor me he pasado usando el suelo pélvico. *Risa* Voy a tener agujetas en el coño."
    call BlinkXS3 ("c27s001_515") from _call_BlinkXS3_375
    deb "Pero ha valido la pena. Pueden describirte el sexo de mil formas y nada se parece a la realidad."
    mc "Doy por sentado que te ha gustado, entonces."
    deb "¿Gustado? ¡Me ha encantado!"
    call BlinkXS3 ("c27s001_520") from _call_BlinkXS3_376
    deb "Pero puedes olvidarte de un segundo round. *Risa* Quiero volver a poder caminar con las piernas cerradas antes del próximo entrenamiento."
    mc "*Risa* ¿Cuándo es el próximo entrenamiento?"
    call BlinkXS3 ("c27s001_525") from _call_BlinkXS3_377
    deb "Mañana. No sé si llegaré a tiempo para poder cerrar las piernas y acabaré pareciendo una rana mientras nado."
    mc "Bueno, serás la rana más bonita del estanque. *Risa*"
    mc "Lagos, estanques, ranas, sirenas... Siempre acabamos relacionando todo con el agua, cuando estamos juntos."
    call BlinkXS3 ("c27s001_530") from _call_BlinkXS3_378
    deb "Bueno, el agua ha sido como una segunda casa para mí durante mucho tiempo."
    deb "Y me siento igual contigo."
    mc "Eso es muy bonito, [deb.nick]. Espero no decepcionarte nunca."
    call BlinkXS3 ("c27s001_535") from _call_BlinkXS3_379
    deb "No lo vas a hacer, no te preocupes."
    deb "Pero no te he preguntado... ¿Qué te ha parecido a ti?"
    mc "A mí me ha gustado mucho. Lo que haces con los músculos es alucinante."
    call BlinkXS3 ("c27s001_540") from _call_BlinkXS3_380
    deb "*Risita* Me alegra que en nuestra primera vez haya hecho algo que no esperabas."
    deb "Con la experiencia que tienes, suponía que lo habías probado todo."
    mc "Hay muchas cosas que probar en esta vida. Y cada vez es diferente. Pero tienes razón - no esperaba que hicieras eso."
    mc "Tampoco esperaba que me pidieras lo del cuello."
    if eva._var("choking"):
        call BlinkXS3 ("c27s001_545") from _call_BlinkXS3_381
        deb "[eva] me dijo que ella lo hizo y que le gustó."
        mc "Pero sus razones eran diferentes. Ella lo hacía para ceder el control."
    call BlinkXS3 ("c27s001_550") from _call_BlinkXS3_382
    deb "Yo nunca he tenido el control de nada en mi vida, [mc]."
    deb "Proponértelo ha sido una forma de continuar igual, pero creo que he cambiado un poco desde que vine a vivir aquí."
    mc "¿Un poco? Creo que la [deb.nick] que bajó de aquel avión no reconocería a esta [deb.nick]."
    mc "Pero la envidiaría. Eres mucho más libre de lo que eras entonces."
    call BlinkXS3 ("c27s001_555") from _call_BlinkXS3_383
    deb "Estoy de acuerdo. Seguramente aquella chica sí que hubiera aceptado y disfrutado que la agarraras por el cuello."
    deb "Si alguna vez hubiera reunido el valor para estar aquí, claro."
    mc "Hubiera tenido que pasar por una evolución similar a la que has pasado tú. Con lo que el resultado hubiera sido el mismo."
    mc "No creo que lo hubiera disfrutado."
    call BlinkXS3 ("c27s001_560") from _call_BlinkXS3_384
    deb "No me dejes volver a hacer una tontería así."
    mc "No creo que haya sido una tontería, [deb.nick]. Querías probarlo y estás en tu derecho de hacerlo."
    if deb._var("choking"):
        mc "Has descubierto que no te gusta y no lo repetirás. Pero no lo hubieras descubierto si no lo hubieras probado."
        mc "Además, cuando lo has descubierto, me lo has dicho. Ese es un paso muy importante."
    else:
        mc "Has descubierto que no querías hacerlo, cuando has puesto mi mano en tu cuello. Antes de que fuera tarde."
        mc "La próxima vez que quieras probar algo, no hace falta que sea yo el que te diga que no me gusta si descubres que no estás cómoda."
    call BlinkXS3 ("c27s001_565") from _call_BlinkXS3_385
    deb "No te preocupes, he aprendido la lección. Creo que a partir de ahora hablaré contigo de cualquier cosa que quiera probar antes de hacerlo."
    deb "Pensaré en cosas para la próxima vez."
    mc "Me parece una idea fantástica. Y que ya estés pensando en la próxima vez también me parece fantástico, ranita mía. *Risa*"
    call BlinkXS3 ("c27s001_570a") from _call_BlinkXS3_386
    deb "*Risa* ¡No te rías de una pobre chica que no puede juntar las piernas!"
    mc "Acostúmbrate. Si yo tengo que acostumbrarme a las trampas de las hermanas Selden, tú tienes que acostumbrarte a que me ría de todo."
    call BlinkXS3 ("c27s001_570b") from _call_BlinkXS3_387
    deb "Voy a vestirme."
    "En el momento en que [deb.nick] se sienta en el borde de la cama, te das cuenta de lo grande que es. La cama, no [deb.nick]. Está lejísimos."
    mc "¿Ya?"
    deb "Tengo que presentar un trabajo mañana en clase. Pero mi novio me ha secuestrado para comer."
    mc "*Risa* Deberías decirle a tu novio que no te secuestre cuando tengas cosas que hacer."
    call BlinkXS3 ("c27s001_570c") from _call_BlinkXS3_388
    deb "*Risa* Entonces nunca podría hacer nada con él. Entre clases y entrenamientos, soy una chica muy ocupada."
    call BlinkXPS3 ("c27s001_575" , "f") from _call_BlinkXPS3_2730
    stop music fadeout (1.5)
    "Una vez vestidos..."
    if lis._var("route"):
        deb "Por cierto, [lis] me ha dicho que vais a ir a la fiesta de Sidney..."
        call c27s001_DebVisit from _call_c27s001_DebVisit_1
    call KissXS3 ("c27s001_625") from _call_KissXS3_8
    call BlinkXS3 ("c27s001_625") from _call_BlinkXS3_389
    if lis._var("route"):
        deb "Pues después de haberme metido donde no me llaman, me voy. Tengo un trabajo que acabar."
    else:
        deb "Me tengo que ir ya. Tengo un trabajo que acabar."
    deb "Te veo luego, [mc]."
    stop music fadeout (1.5)
    mc "Hasta luego, [deb.nick]."
    if not _in_replay:
        call c27s001_EmmVisit from _call_c27s001_EmmVisit_1
    return
label c27s001_DebVisit:
    if not deb._var("route"):
        scene c27s002_245d with dissolve
        "Justo cuando terminas de vestirte..."
        play sound ("music/knock.ogg")
        "*Knock-Knock*"
        deb "*A través de la puerta* Soy yo, puedo pasar."
        mc "Pasa, [deb.nick], por favor."
        call BlinkXS3 ("c27s001_570d") from _call_BlinkXS3_390
        play music ("music/RhythmPlay.ogg")
        deb "¿Tienes un momento para hablar?"
        mcp "(¿Me estoy volviendo loco? Parece que [deb.nick] lleva el mismo vestido que Missy en el juego.)"
        mcp "(Ella ha jugado esta actualización ya... ¿Se ha comprado un vestido igual, en otro color?)"
        mc "Sí, por supuesto."
        call BlinkXS3 ("c27s001_575") from _call_BlinkXS3_391
        deb "Es sobre [lis]... Me ha dicho que vais a ir a la fiesta de Sidney."
    else:
        play music ("music/RhythmPlay.ogg")
    mc "No sé cómo se llama, pero supongo que sí. Sólo me dijo que era una fiesta que daba una amiga."
    mc "¿Tú no estabas invitada?"
    call BlinkXS3 ("c27s001_580") from _call_BlinkXS3_392
    deb "Me invitan a esas fiestas por obligación, pero es [lis] quién es su... amiga. No voy casi nunca, no estoy cómoda."
    mc "Has dicho 'amiga' como si realmente no lo fuera."
    call BlinkXS3 ("c27s001_585") from _call_BlinkXS3_393
    deb "No le digas a [lis] que te he dicho esto, pero... no la he visto nunca tan a gusto con ese tipo de 'amigas' como la veo con [kim] o con [eri]."
    deb "Aunque no es que la haya visto mucho, ya te he dicho que no voy demasiado a esas fiestas."
    mc "¿Cómo se conocieron?"
    call BlinkXS3 ("c27s001_590") from _call_BlinkXS3_394
    deb "Conoció a Sidney en una fiesta hace un par de años, una de las primeras a las que fue, y... congeniaron... al nivel que se congenia en esas fiestas."
    mc "No sé a lo que te refieres..."
    call BlinkXS3 ("c27s001_595") from _call_BlinkXS3_395
    deb "La mayoría de esas amistades son falsas. Ya sabes, ricos y famosos."
    deb "Si alguna de sus 'amigas', o incluso la propia [lis], dejara de ser rica o famosa, no la invitarían a ninguna de esas fiestas. Sería una paria."
    mc "Bueno, me imaginé que tenía dinero cuando [lis] me dijo lo de una 'pequeña fiesta con 70 o 90 personas'."
    call BlinkXS3 ("c27s001_600") from _call_BlinkXS3_396
    deb "No todos los asistentes a la fiesta son ricos. Hay un montón de gente revoloteando alrededor de esos ricos y famosos, buscando aprovecharse de ellos."
    deb "Siempre me he alegrado de no tener a ese tipo de gente alrededor. [lis] no ha tenido tanta suerte."
    mc "Lo entiendo."
    call BlinkXS3 ("c27s001_605") from _call_BlinkXS3_397
    deb "Volviendo a Sidney, ella es cuatro años mayor que [lis], con lo que te puedes imaginar que, aparte de todo lo que rodea a ese mundo, no tenían mucho en común."
    mc "Pero no entiendo qué tiene que ver esto conmigo."
    call BlinkXS3 ("c27s001_610") from _call_BlinkXS3_398
    deb "*Risa* Me he ido por las ramas."
    call BlinkXS3 ("c27s001_615") from _call_BlinkXS3_399
    deb "Tan solo quería advertirte de que es posible que la [lis] que veas en la fiesta no sea la misma a la que estás acostumbrado."
    deb "Allí se convertirá en una mariposa social y, después de que te presente a algunas de sus amigas, seguramente te sientas un poco solo."
    deb "No la juzgues por lo que pase en esa fiesta."
    mc "Es un ambiente en el que no he estado nunca, con lo que no creo que pueda juzgarla."
    call BlinkXS3 ("c27s001_620") from _call_BlinkXS3_400
    deb "Y después está la noche que pasaréis en el hotel..."
    if deb._var("route"):
        deb "Espero que seas tan tierno con ella como lo has sido conmigo. [lis] parece más dura que yo, pero..."
    else:
        deb "Espero que seas tierno con ella... [lis] parece más dura de lo que es, pero..."
    mc "Sé a lo que te refieres. Lo intentaré."
    if not deb._var("route"):
        call BlinkXS3 ("c27s001_625") from _call_BlinkXS3_401
        deb "Pues después de haberme metido donde no me llaman, me voy. Nos están esperando para comer."
        deb "Te veo luego, [mc]."
        mc "Hasta luego, [deb.nick]."
    return
label c27s001_EmmVisit:
    if _in_replay:
        call mrS3_emm_route from _call_mrS3_emm_route_17
        call mrS3_deb_route from _call_mrS3_deb_route_16
        if not deb._var("route"):
            call mrS3_lis_route from _call_mrS3_lis_route_10
    scene c27s002_245d with fade
    if deb._var("route") or lis._var("route"):
        "Un minuto después de irse [deb.nick]..."
    play sound ("music/knock.ogg")
    "*Knock-Knock*"
    emm "*A través de la puerta* [mc], ¿puedo pasar?"
    mc "Sí, pasa [emm]."
    play music ("music/Happy-Sun.ogg")
    call BlinkXPS3 ("c27s001_640" , "f") from _call_BlinkXPS3_2731
    mc "¿Te puedo ayudar en algo?"
    emm "He cometido un error. He comprado el material de fotografía sin entrega a domicilio. Habría que ir a buscarlo a Paso Robles."
    emm "¿Me podrás llevar a buscarlo? Por favor, por favor..."
    mc "Ningún problema. ¿Cuándo hay que ir?"
    call BlinkXS3 ("c27s001_645") from _call_BlinkXS3_402
    emm "Ummm... Pasado mañana."
    mc "Y ¿a qué viene tanta prisa?"
    call BlinkXS3 ("c27s001_650") from _call_BlinkXS3_403
    emm "Perdón... cuando me he dado cuenta de que había metido la pata..."
    mc "¿Ya has hablado con los pintores?"
    call BlinkXS3 ("c27s001_655") from _call_BlinkXS3_404
    emm "No pueden venir a pintar hasta dentro de dos semanas. Al final lo haré yo con Mamá y Tía [nor]."
    emm "[kim] ha dicho que también ayudará. Lo pintaremos mañana por la tarde."
    mc "Si tengo un rato te ayudaré a mover los trastos del sótano mañana por la mañana."
    call BlinkXS3 ("c27s001_660") from _call_BlinkXS3_405
    emm "¡Eso sería fantástico! Podríamos hacerlo cuando se vayan Tía [bet] y la abuela."
    mc "Me parece una buena idea. Pregúntale a Mamá qué se puede tirar y qué se tiene que guardar. Puedes marcarlo con pegatinas de colores."
    call BlinkXS3 ("c27s001_665") from _call_BlinkXS3_406
    emm "Sólo tengo pegatinas rosas..."
    mc "Perfecto. *Risa* Marca de rosa lo que se tenga que tirar."
    call BlinkXS3 ("c27s001_670") from _call_BlinkXS3_407
    emm "¿Por qué? ¡Puedo marcar de rosa lo que se tenga que guardar!"
    mc "Entonces, si a algo se le cae la pegatina, lo tiraremos por error."
    call BlinkXS3 ("c27s001_675") from _call_BlinkXS3_408
    emm "¡Jobar! Tienes razón. Me jode que el rosa se asocie con algo que haya que tirar."
    mc "*Risa* Todo el mundo lo asocia menos tú."
    if emm._var("route"):
        call KissXS3 ("c27s001_680") from _call_KissXS3_9
    call BlinkXS3 ("c27s001_680") from _call_BlinkXS3_409
    emm "No vas a conseguir ponerme de mal humor. ¡Voy a tener un estudio de fotografía en dos días!"
    mc "Tienes que dejar que la pintura se seque antes de montarlo todo, [emm]."
    emm "Bueno, pues en tres días. Hasta luego, [mc]."
    stop music fadeout (1.5)
    mc "Hasta luego, [emm]."
    return
label c27s002_AmaSimSamJam:
    scene c27s002_005d with fade
    "Mientras tanto, en el piso de los Washington..."
    play sound ("music/doorbell1.ogg")
    "*Ding-Dong*"
    sam "Ya voy..."
    play music ("music/RhythmPlay.ogg")
    call BlinkXS3 ("c27s002_005") from _call_BlinkXS3_410
    ama "Buenos días, Sra. Washington. ¿Está la Srta. Washington en casa?"
    call BlinkXS3 ("c27s002_010") from _call_BlinkXS3_411
    sam "Hola, [ama]. Sí, [sim] está en casa, pasa."
    call BlinkXS3 ("c27s002_005") from _call_BlinkXS3_412
    ama "Puede llamarme Srta. Gilford..."
    call BlinkXS3 ("c27s002_015") from _call_BlinkXS3_413
    sam "¿A qué vienen tantas formalidades? ¿Pasa algo?"
    call BlinkXS3 ("c27s002_020") from _call_BlinkXS3_414
    ama "Hoy vengo en... misión de trabajo..."
    ama "No sé cómo se hace esto. Creo que lo de los apellidos es más... no sé... oficial."
    call BlinkXS3 ("c27s002_025") from _call_BlinkXS3_415
    sam "*Risa* Si alguna vez tienes que venir al hospital, Dios no lo quiera, y me llamas Enfermera Washington, te pondré un enema de ortigas."
    sam "Que sea oficial no quiere decir que nos tengamos que tratar como desconocidas. Siéntate, por favor."
    call BlinkXS3 ("c27s002_030") from _call_BlinkXS3_416
    ama "¡Menos mal! Se me estaba haciendo rarísimo llamarte por tu apellido..."
    ama "¿Puedes avisar a [sim], por favor?"
    scene c27s002_035a with fade
    sim "¿Qué pasa [ama]? ¿Por qué estás tan elegante? ¿Vas a alguna parte?"
    sam "Viene en misión de trabajo. Creo que ese 'alguna parte' es aquí. Siéntate."
    call BlinkXS3 ("c27s002_040") from _call_BlinkXS3_417
    ama "Bueno, creo que esto se me da muy mal..."
    ama "Quería entregarte estos papeles, [sim]. Sólo tienes que firmarlos en la última hoja."
    scene c27s002_035b with dissolve
    sim "¿Qué es esto?"
    scene c27s002_035c with hpunch
    sim "¿Qué? ¿Una beca? ¿Para la universidad?"
    sam "¿Qué? ¿Esto ha sido idea de [mc]? Ayer en el super le dije que no aceptábamos caridad."
    call BlinkXS3 ("c27s002_045") from _call_BlinkXS3_418
    ama "Bueno, [mc] firmó esos papeles hace unos días. No creo que vuestra conversación de ayer haya tenido nada que ver."
    ama "Si lo firmas, puedo ir a la universidad a oficializar tu matrícula. Vamos un poco justos de tiempo."
    call BlinkXS3 ("c27s002_050") from _call_BlinkXS3_419
    sim "¡No puedo aceptar esto! No lo merezco y no vamos a aceptar caridad, como ha dicho mi madre."
    call BlinkXS3 ("c27s002_055") from _call_BlinkXS3_420
    ama "Yo no lo considero caridad. NTR ha creado una beca para la que eres la mejor candidata, con lo que no es como si [mc] estuviera pagando tu matriculación."
    call BlinkXS3 ("c27s002_060") from _call_BlinkXS3_421
    sim "¡Seguro que hay candidatas mejores! ¡Yo ya no puedo competir!"
    call BlinkXS3 ("c27s002_065") from _call_BlinkXS3_422
    ama "En el tiempo que he tenido para evaluar a todas las candidatas no he encontrado a nadie mejor."
    ama "Y la beca es para que estudies Ciencias del Deporte, no para que nades. Para que te conviertas en entrenadora."
    call BlinkXS3 ("c27s002_070") from _call_BlinkXS3_423
    sam "¿Cuándo te encargó [mc] que hicieras esto, [ama]?"
    call BlinkXS3 ("c27s002_075") from _call_BlinkXS3_424
    ama "[mc] firmó los papeles el Sábado y..."
    call BlinkXS3 ("c27s002_070") from _call_BlinkXS3_425
    sam "No te he preguntado cuándo lo firmó. Te estoy preguntando cuándo te encargó que estudiaras la creación de la beca."
    sam "Porque te lo encargó él, ¿no? ¿O ha sido idea tuya? ¿O de alguien más?"
    call BlinkXS3 ("c27s002_080") from _call_BlinkXS3_426
    ama "Bueno... Como CEO de NTR, me lo encargó él en cuanto firmó los papeles y..."
    call BlinkXS3 ("c27s002_085") from _call_BlinkXS3_427
    sim "Pero esos papeles... ¿los redactó él o se los entregaste tú? ¿O se los entregó alguna otra persona?"
    call BlinkXS3 ("c27s002_090") from _call_BlinkXS3_428
    ama "¿Qué más da quién redactara los requisitos de la beca? Lo importante es que lo firmes."
    scene c27s002_095a with dissolve
    sam "Está claro que no fue idea de [mc]. Si lo fuera, ella lo habría dicho sin dar tantos rodeos."
    sam "Apostaría algo a que 'alguien' escuchó tu conversación con [deb.nick] y [mc] sobre entrenar y sobre que hubieras querido estudiar educación deportiva."
    call BlinkXS3 ("c27s002_100") from _call_BlinkXS3_429
    sim "Tienes razón. Allí sólo estábamos [deb.nick], [mc], y yo. [deb.nick], pese a que tiene el dinero para hacerlo, no haría una beca a nombre de NTR."
    sim "Y [mc], como acabas de decir, está claro que no lo ha hecho."
    scene c27s002_035e with dissolve
    sim "¿O de [eva]?" (multiple=2)
    sam "¿Ha sido idea tuya?" (multiple=2)
    scene c27s002_035f with dissolve
    sam "Si hubiera sido de [eva], sería ella la que estuviera aquí."
    sim "Tienes razón. Además, [eva] no tendría tantos reparos en aceptar que la idea ha sido suya."
    sam "Ni en aceptar el agradecimiento por haber tenido la idea."
    call BlinkXS3 ("c27s002_105") from _call_BlinkXS3_430
    ama "¿Agradecimiento? ¿No estáis enfadadas porque le presentara los papeles a [mc]?"
    scene c27s002_035g with dissolve
    sim "¡Has caído en la trampa!" (multiple=2)
    sam "¡Lo sabía!"  (multiple=2)
    call BlinkXS3 ("c27s002_110") from _call_BlinkXS3_431
    sim "¡Se nota que no te has criado con mi madre! Ni Jamaal ni yo caemos en esas trampas desde hace años."
    sim "Pero ahora entiendo por qué a mi madre le gustaba tanto tendérnoslas."
    call BlinkXS3 ("c27s002_115") from _call_BlinkXS3_432
    ama "Entonces... ¿vas a firmar los papeles ahora que sabéis que no es cosa de [mc], [sim]?"
    scene c27s002_035h with dissolve
    sim "¡No! ¡No lo puedo aceptar!" (multiple=2)
    sam "¡Ya te hemos dicho que no aceptamos caridad!"  (multiple=2)
    call BlinkXS3 ("c27s002_120") from _call_BlinkXS3_433
    jam "¿Quieres firmar los putos papeles de una vez, [sim]?"
    jam "Y ya sé que tengo que poner un dólar en el bote de los tacos, pero es el dólar que menos me va a doler poner en mi vida."
    call BlinkXS3 ("c27s002_125") from _call_BlinkXS3_434
    jam "[ama] se ha molestado en crear una beca para ti y te pones... os ponéis las dos... hechas una furia."
    jam "Una cosa es no aceptar caridad, y otra distinta es no aceptar favores."
    call BlinkXS3 ("c27s002_130") from _call_BlinkXS3_435
    jam "Por cierto, hola, [ama]. Perdona a las irracionales Washington. Yo soy la parte que piensa. Esa beca, ¿te cuesta dinero a ti?"
    call BlinkXS3 ("c27s002_135") from _call_BlinkXS3_436
    ama "Hola, Jamaal. No, es dinero de NTR... Y tiene retorno de impuestos."
    call BlinkXS3 ("c27s002_140") from _call_BlinkXS3_437
    jam "¿Veis? ¡No es una maldita obra de caridad! Sí, otro dólar. Es una empresa haciendo algo que le beneficia a largo plazo."
    jam "¿La estaríais rechazando si fuese MocoSoft o FAPple en vez de NTR? Seguro que no pero, como es la empresa de [mc], hay que poner pegas, ¿no?"
    jam "¡Ni siquiera le habéis dado las gracias a [ama]!"
    scene c27s002_035i with dissolve
    sam "Tiene un poco de razón, ¿no? ¿Estamos siendo un poco irracionales?"
    sim "Es posible. ¡Mielda, no me gusta darle la razón a Jamaal!"
    scene c27s002_140d with dissolve
    jam "Entonces todo arreglado. Vuelvo a mi habitación. He dejado a medias el chat con un cliente."
    call BlinkXPS3 ("c27s002_145" , "f") from _call_BlinkXPS3_2732
    sim "Toma, aquí están los papeles firmados. Y gracias."
    sim "Pero, ¿cómo lo sabías? Nunca hemos hablado de ello..."
    call BlinkXS3 ("c27s002_150") from _call_BlinkXS3_438
    ama "El otro día, cuando estabas en la piscina con [mc] y [deb.nick]..."
    scene c27s002_155a with fade
    "Después de dar las explicaciones de cómo surgió el plan de la beca..."
    sim "Gracias, [ama]. No sé si hubiera podido estudiar sin lo que acabas de hacer."
    ama "No es sólo mérito mío. [mc] estuvo de acuerdo con la idea y fue quien dio la orden ejecutiva."
    sim "Seguramente no lo hubiera hecho si no hubiera sido por ti. Sabe cómo nos sentimos cuando se nos ofrece... caridad."
    ama "Yo también lo sé, pero esto no es caridad. Son negocios. Y un favor a una hermana."
    scene c27s002_155b with fade
    sam "Disculpa por cómo nos hemos comportado. Lo de ser irracional lo llevamos en la sangre."
    ama "No hay nada por lo que disculparse."
    sam "¿Has comido ya? ¿Quieres quedarte a comer?"
    ama "Me encantaría."
    sam "He hecho pierogi para nosotros tres, podemos dividirlos y hacer una ensalada más grande."
    jam "*Desde su habitación* ¡Noooo!"
    stop music fadeout (1.5)
    return
label c27s002_AaronVC:
    if _in_replay:
        call mrS3_deb_route from _call_mrS3_deb_route_14
        call mrS3_bet_route from _call_mrS3_bet_route_4
    scene c27s002_200d with fade
    if deb._var("route"):
        "Un par de minutos después de que [emm] se vaya..."
    else:
        "Nada más entrar en tu habitación después de comer..."
    play sound ("music/RingtoneMC.ogg")
    "*Ring-Ring*"
    mcp "(¿Videoconferencia con Aaron? No teníamos nada programado para hoy...)"
    stop sound
    call BlinkXS3 ("c27s002_200") from _call_BlinkXS3_439
    play music ("music/SadSoul.ogg")
    mc "Hola, Aaron. ¿Puedo ayudarte en algo?"
    aar "Bueno, llamaba para un par de cosas. La primera es que quiero asegurarme de que habéis recibido el dinero."
    mc "Sí, fue una sorpresa. Lo esperábamos hacia final de año."
    call BlinkXPS3 ("c27s002_205" , "f") from _call_BlinkXPS3_2733
    aar "Bueno, sobre eso... He descubierto que Daniels maquillaba los libros de contabilidad. [mar] y [nor] sólo estaban recibiendo la mitad de lo que les pertocaba."
    aar "Una de las transferencias era desviada como gastos. Se quedaba una parte. Richards lo hacía antes que él, con lo que..."
    mc "Le debemos un montón de dinero a [mar] y a [nor]. 20 años a $83,000... alrededor de $1,600,000."
    call BlinkXS3 ("c27s002_210") from _call_BlinkXS3_440
    aar "Bastante menos. Los primeros años era muy poco dinero, y después fue creciendo. Pero sí, NTR les debe algo menos de $900,000 a cada una."
    aar "Es algo que tendremos que solucionar, pero habrá tiempo para eso cuando estés aquí."
    call BlinkXS3 ("c27s002_215") from _call_BlinkXS3_441
    aar "¿Cómo ves tu sueldo de CEO? Creo que no habíamos hablado de ello en ningún momento."
    mc "Me sorprendió la cantidad. No esperaba tanto."
    aar "Era lo que cobraba Daniels, con lo que es difícil de justificar bajar tu sueldo."
    call BlinkXS3 ("c27s002_220") from _call_BlinkXS3_442
    aar "Sobre el tema de los sueldos... tengo que pedirte una cosa..."
    mc "Dime. Lo que necesites. Supongo que ahora que tienes el cargo de Director de Operaciones, te habrás subido el sueldo, ¿no?"
    call BlinkXS3 ("c27s002_225") from _call_BlinkXS3_443
    aar "Bueno, no es que me haya subido el sueldo. He cobrado un sueldo por primera vez en mi vida."
    mc "¿Qué? ¿No cobrabas? ¿Las chicas tampoco?"
    call BlinkXS3 ("c27s002_230") from _call_BlinkXS3_444
    aar "No. Ninguno de los operativos cobrábamos. Nuestro 'pago' era vivir en la base, alimentación, entrenamiento..."
    aar "Tampoco es que hubiéramos tenido dónde gastarlos. Imagínate 16 clones de la Serie G entrando a la vez en un bar de Oranjestad." id c27s002_AaronVC_a8247bb1
    mc "Lo entiendo."
    call BlinkXS3 ("c27s002_235") from _call_BlinkXS3_445
    aar "Por eso quiero pedirte el favor del que te hablaba. Las chicas nunca han tenido dinero propio. Ahora tienen más de $50,000 cada una." id c27s002_AaronVC_9493f119
    aar "Dudo que [ama] vaya a hacer alguna locura, pero... si pudieras vigilar un poco a [eva], me harías... nos harías un favor a todos."
    mc "Ningún problema. Creo que puedo convencer a [mar] y a [nor] para que les den una charla sobre el dinero."
    mc "Les dará la oportunidad de pasar más tiempo con ellas a solas y ejercer de madres."
    call BlinkXS3 ("c27s002_240") from _call_BlinkXS3_446
    aar "Perfecto. Entonces, creo que ahora viene el tema más complicado."
    $ bet.full = "Beatrix"
    aar "Necesitaría hablar con [bet.full]."
    mc "¿Con Tía [bet]? ¿Para qué?"
    aar "Es por un tema médico que..."
    mc "¿Te pasa algo? ¿Estás bien?"
    call BlinkXS3 ("c27s002_245") from _call_BlinkXS3_447
    aar "No, tranquilo, no es para mí. Hemos perdido al cirujano que teníamos en NTR y..."
    scene c27s002_245d with dissolve
    play sound ("music/knock.ogg")
    "*Knock-Knock*"
    mar "*A través de la puerta* Soy yo. ¿Puedo pasar?"
    mc "Sí, pasa. Estoy en una videoconferencia con Aaron."
    call BlinkXS3 ("c27s002_250") from _call_BlinkXS3_448
    mar "¿Hola, Aaron? ¿Qué tal todo por Aruba?"
    call BlinkXPS3 ("c27s002_255" , "x") from _call_BlinkXPS3_2734
    aar "Todo bien, [mar]. Estaba discutiendo unos temas con [mc]."
    call BlinkXPS3 ("c27s002_260" , "x") from _call_BlinkXPS3_2735
    mar "Entonces os dejo con vuestros asuntos. Lo que venía a decirle a..."
    scene c27s002_260An with dissolve
    mar "... [mc]..."
    mar "... no es..."
    mar "... urgente..."
    mc "¿Puedes decirle a Tía [bet] que venga, por favor? Aaron quiere hablar con ella."
    call BlinkXS3 ("c27s002_265") from _call_BlinkXS3_449
    mar "Sí... Ahora voy... a avisarla... Está en la piscina..."
    if persistent.family:
        mc "Gracias, Mamá."
    else:
        mc "Gracias, [mar]."
    call BlinkXPS3 ("c27s002_270" , "x") from _call_BlinkXPS3_2736
    mc "Si quieres esperamos que llegue Tía [bet] para seguir hablando de lo que necesitas de ella."
    mc "Mientras tanto voy pasando la video conferencia al portátil. Será más cómodo."
    mc "¿Qué ha pasado con el cirujano?"
    aar "El cirujano principal era Daniels."
    mc "Y supongo que ahora no puede trabajar con nosotros, ¿no?"
    call BlinkXPS3 ("c27s002_275" , "f") from _call_BlinkXPS3_2737
    aar "Es complicado... Aún tenemos que decidir qué vamos a hacer con él. Pero no me fiaría de que me operara, si fuera necesario."
    aar "Y sus ayudantes dan el nivel para operaciones más básicas. No para lo que necesitamos ahora mismo."
    mc "Sobre Daniels, ¿qué opciones tenemos?"
    call BlinkXPS3 ("c27s002_280" , "f") from _call_BlinkXPS3_2738
    aar "Como te digo, es complicado. No lo podemos entregar a la justicia de Aruba."
    aar "Ha ordenado asesinatos, pero todo saldría a la luz en un juicio público y eso es lo que menos nos conviene."
    mc "Lo entiendo. Nos tocará a nosotros impartir justicia, entonces."
    call BlinkXS3 ("c27s002_285") from _call_BlinkXS3_450
    aar "Justicia. Aunque no sea legal. Quiero consultarlo con las chicas cuando estén aquí. No es algo para tratar en una video conferencia."
    aar "De hecho, tenerlo 'prisionero' ya es ilegal. No tenemos ningún derecho legal a hacerlo, pero las autoridades de Aruba van a mirar hacia otro lado."
    mc "Supongo que tan ilegal como asesinarlo..."
    call BlinkXS3 ("c27s002_290") from _call_BlinkXS3_451
    aar "Por eso lo quiero consultar con las chicas. Si por mi fuera, le dispararía en la cabeza ahora mismo, pero ellas también tienen derecho a decidir qué hacer con él."
    aar "Sus hermanas murieron por culpa de Daniels, igual que mi hermano. Tienen el mismo derecho a decidir que yo."
    if persistent.walkthrough:
        $ wt1 = _("[mc] decidirá el destino de Daniels.")
        $ wt2 = _("[ama], [eva], y Aaron decidirán el destino de Daniels")
    else:
        $ wt1 = ""
        $ wt2 = ""
    menu:
        "También atacó a mi familia." (wt=wt1):
            $ mc._var("Daniels", True)
            mc "Creo que también deberíamos tener derecho a decidir, aunque gracias a vosotros no perdiéramos a nadie."
            call BlinkXS3 ("c27s002_295") from _call_BlinkXS3_452
            aar "Esperaba que dijeras algo así y lo considero lógico."
            aar "Pienso que, cuando estéis los tres aquí, habrá que decidir."
        "Lo considero lógico." (wt=wt2):
            $ mc._var("Daniels", False)
            mc "Creo que es un tema que deberíais decidir vosotros, gracias a vosotros nosotros no perdimos a nadie, y no creo que debamos intervenir en esa situación."
            call BlinkXS3 ("c27s002_295") from _call_BlinkXS3_453
            aar "No esperaba que dijeras algo así... Creía que ibas a querer participar en la decisión, aunque te agradezco que lo dejes en nuestras manos."
            aar "Pienso que, cuando estén las dos aquí, habrá que decidir."
    $ resetWalkthrough()
    mc "Me parece que no van a coincidir las dos allí. [eva] no está preparada para ver a Gavin todavía, con lo que se quedará aquí el primer mes."
    mc "Después rotarán. [ama] volverá a casa y [eva] estará allí conmigo."
    call BlinkXS3 ("c27s002_300") from _call_BlinkXS3_454
    aar "Entonces, durante la rotación. Habrá que hacer que coincidan las dos aquí para tomar esa decisión."
    mc "Por cierto, ¿cómo está Gavin?"
    aar "De eso es de lo que quiero hablar con [bet.full]."
    mc "Oigo pasos en la escalera. Debe ser ella."
    scene c27s002_245d with dissolve
    play sound ("music/knock.ogg")
    "*Knock-Knock*"
    bet "*A través de la puerta* Soy yo. [mar] me ha dicho que querías verme."
    mc "Sí, pasa, Tía [bet]."
    call BlinkXPS3 ("c27s002_305" , "f") from _call_BlinkXPS3_2739
    mc "Siéntate. Aaron quiere hablar contigo. Os presento."
    bet "Encantada de conocerte, Aaron."
    call BlinkXPS3 ("c27s002_310" , "x") from _call_BlinkXPS3_2740
    aar "Lo mismo digo, Sra. [bet.full]."
    scene c27s002_305An
    bet "..."
    mc "¿Qué pasa Tía [bet]?"
    call BlinkXS3 ("c27s002_315") from _call_BlinkXS3_455
    bet "Nadie me había dicho que Aaron era un clon tuyo."
    mc "¡Mierda, Tía [bet]! No se te puede ocultar nada. No se lo hemos dicho a nadie todavía."
    bet "Veros a la vez lo hace obvio. Seguramente no lo hubiera notado si os viera por separado. Como mucho hubiera pensado que tenéis un cierto parecido."
    mc "Ni Mamá ni Tía [nor] lo notaron durante la reunión que tuvimos con él..."
    call BlinkXS3 ("c27s002_320") from _call_BlinkXS3_456
    bet "*Risa* Supongo que sólo tenían ojos para [ama] y [eva]."
    bet "Además, la diferencia de edad aparente hace que el cerebro no os relacione. Nuestro cerebro no está preparado para procesar algo así."
    mc "Excepto el tuyo, por lo que parece..."
    call BlinkXPS3 ("c27s002_325" , "x") from _call_BlinkXPS3_2741
    aar "Le agradecería que no les dijera nada al resto de su familia, ni a [ama] y a [eva]."
    aar "No quiero que se sientan obligados a considerarme parte de la familia sólo porque compartamos genes."
    aar "Y se lo quiero decir a mis chicas en persona."
    call BlinkXPS3 ("c27s002_330" , "x") from _call_BlinkXPS3_2742
    bet "Lo entiendo, aunque no lo comparta. Pero voy a ponerte una condición, Aaron. Deja de llamarme Sra. [bet.full] y llámame [bet]."
    bet "*Risa* No eres mi sobrino, pero eres el clon de [mc] y me siento rara viendo a su cara llamándome así."
    call BlinkXPS3 ("c27s002_335" , "x") from _call_BlinkXPS3_2743
    aar "Me parece una condición que puedo cumplir. Mientras no me obligue a llamarla Tía [bet]..."
    aar "Pero no quiero entretenerla más de lo necesario, con lo que, si no le importa, voy a ir al grano."
    aar "No sé si se acuerda de Gavin..."
    call BlinkXPS3 ("c27s002_340" , "x") from _call_BlinkXPS3_2744
    bet "Sí, el chico que perdió el brazo por lo que pasó en nuestra cocina. ¿Qué le pasa?"
    call BlinkXPS3 ("c27s002_335b" , "x") from _call_BlinkXPS3_2745
    aar "Necesita una operación, y no tenemos un neurocirujano disponible. Creo que usted podría ser una buena opción."
    aar "Como además... no es demasiado legal en los Estados Unidos... debería hacerse aquí."
    call BlinkXPS3 ("c27s002_340b" , "x") from _call_BlinkXPS3_2746
    bet "¿De qué tipo de operación estamos hablando, Aaron? ¿Por qué no es legal aquí?"
    call BlinkXPS3 ("c27s002_310" , "f") from _call_BlinkXPS3_2747
    "Aaron pasa alrededor de 10 minutos explicando la operación a un nivel que incluso tú puedes entender."
    "Lo entiendes tan bien que, cuando acaba con la explicación, tienes la boca abierta por la sorpresa."
    mcp "(¡Oh, Dios mío! ¡Eso es pura ciencia ficción!)"
    call BlinkXPS3 ("c27s002_345" , "f") from _call_BlinkXPS3_2748
    bet "Parece una operación complicada y no sé si tengo los conocimientos para hacerla. No creo que NADIE tenga los conocimientos para hacerla."
    bet "Mándame toda la documentación de la que has hablado y lo estudiaré. ¿Cuándo se debería hacer?"
    call BlinkXPS3 ("c27s002_350" , "x") from _call_BlinkXPS3_2749
    aar "Por lo que me han dicho los cirujanos que tenemos aquí, cuanto antes mejor."
    aar "Lo ideal sería que, si decide hacerlo, acompañe a [mc] a Aruba cuando él venga."
    aar "Una vez esté aquí, tendrá tiempo de comentar todo el proceso junto con el equipo."
    call BlinkXPS3 ("c27s002_355" , "x") from _call_BlinkXPS3_2750
    bet "Suena a un buen plan. Aún quedan unos días para que [mc] vaya y tendré tiempo de estudiar la documentación y confirmarte si me veo preparada para hacer esa operación."
    bet "Si decidimos hacerlo, quiero tener el control absoluto en el proceso."
    bet "No quiero algo a medias tintas que pueda poner en peligro la vida del chico."
    call BlinkXPS3 ("c27s002_360" , "x") from _call_BlinkXPS3_2751
    aar "Me parece bien. Voy a pedirle al equipo que le mande toda la documentación lo antes posible."
    aar "Y ahora les tengo que dejar. Debo entrar en otra reunión."
    aar "Gracias, Sra. ... Gracias, [bet]."
    call BlinkXPS3 ("c27s002_365" , "f") from _call_BlinkXPS3_2752
    bet "¡Es increíble! Ya me parecía increíble lo de las pruebas de embarazo, pero esto..."
    mc "Aún estoy asombrado. ¿Te ves preparada para hacerlo?"
    call BlinkXS3 ("c27s002_370") from _call_BlinkXS3_457
    bet "No hay nadie preparado para hacerlo en el mundo, excepto el tal Daniels, quizás. Ha tenido años para familiarizarse con cerebros que envejecen aceleradamente."
    bet "Y estoy segura de que no soy la mejor opción para hacer esa operación, pero dudo que otros cirujanos con más reputación estuvieran dispuestos a hacerla."
    mc "Es comprensible. Por lo ilegal y porque habría que darles una información que no creo que NTR esté preparada para dar aún."
    call BlinkXS3 ("c27s002_375") from _call_BlinkXS3_458
    bet "*Risa* Decirle a alguien '¿Quieres hacer una operación ilegal en alguien que no debería existir?' no es la mejor forma de establecer un primer contacto."
    mc "*Risa* Desde luego que no."
    if bet._var("route"):
        mc "Hablando de cosas que no deberían existir... ¿Quieres hacerte la prueba de embarazo?"
        call BlinkXS3 ("c27s002_380") from _call_BlinkXS3_459
        bet "No hace falta. Tengo una edad y..."
        mc "Y me dijiste que las mujeres de la familia son fértiles hasta edades muy avanzadas..."
        call BlinkXS3 ("c27s002_385") from _call_BlinkXS3_460
        bet "Sí, pero no es lo que iba a decir. Mañana por la mañana me voy a Florida. Si hiciéramos la prueba ahora, no estaría lista cuando me fuera."
        bet "Si me hiciera la prueba, querría ver el resultado contigo. Habrá tiempo cuando vuelva de Florida, especialmente si voy a Aruba contigo."
        mc "Me parece una buena idea."
        call KissXS3 ("c27s002_390") from _call_KissXS3_10
    call BlinkXS3 ("c27s002_390") from _call_BlinkXS3_461
    bet "Voy a mi habitación a coger el móvil. Tengo ganas de recibir la información y empezar a estudiarla."
    bet "Te veo luego, [mc]."
    stop music fadeout (1.5)
    if bet._var("route"):
        mc "Te veo luego, [bet]."
    else:
        mc "Te veo luego, Tía [bet]."
    scene black with dissolve
    return
label c27s002_KiaEilNor:
    if _in_replay:
        call mrS3_kia_route from _call_mrS3_kia_route_9
    scene c27s002_400a with fade
    "Mientras tanto, en el salón de [nor]..."
    play music ("music/RhythmPlay.ogg")
    kia "Lo siento, [nor], pero ya lo hemos decidido."
    eil "No digas 'hemos decidido', Mamá. Di 'has decidido'. Yo no quiero irme. [eri] incluso me ha ofrecido compartir habitación cuando lleguen las chicas nuevas."
    nor "No quiero meterme entre vosotras dos, pero si [eil] quiere quedarse en casa, es bienvenida."
    call BlinkXS3 ("c27s002_405") from _call_BlinkXS3_462
    kia "Es nuestra casa. Deberíamos vivir allí una vez Solomon se vaya y podamos volver."
    kia "Quiero dejar de ser una carga para ti. Suficiente trabajo tendrás una vez lleguen las chicas nuevas."
    call BlinkXPS3 ("c27s002_410" , "x") from _call_BlinkXPS3_2753
    nor "No dais ningún trabajo, [kia]. ¿Comida? Viváis donde viváis espero que vengáis a comer o cenar todos los días."
    nor "Me fastidia que [sam] y [sim], [oma], [mad.nick], o [meg] sólo vengan un par de días por semana, tres como mucho, pero ellas nunca han vivido aquí."
    nor "Si lo hicierais vosotras después de estas dos semanas... Sería como si la casa estuviera vacía."
    call BlinkXPS3 ("c27s002_415" , "x") from _call_BlinkXPS3_2754
    eil "Bueno, más trabajo sí que damos. Hay más lavadoras que poner..."
    call BlinkXPS3 ("c27s002_420" , "x") from _call_BlinkXPS3_2755
    nor "¿Cuántas lavadoras has puesto en la última semana, [eil]? ¿Cuántas ha puesto tu madre?"
    nor "¡Desde que vivís aquí, pongo menos lavadoras que nunca! Entre vosotras y mi madre me estáis quitando un montón de trabajo."
    call BlinkXPS3 ("c27s002_425" , "x") from _call_BlinkXPS3_2756
    kia "Pero los gastos... La factura de la luz, del agua... la comida... todo eso te tiene que ocasionar gastos..."
    call BlinkXPS3 ("c27s002_430" , "x") from _call_BlinkXPS3_2757
    nor "Aún no ha llegado ninguna factura desde que estáis aquí, pero no creo que sea mucho el incremento, por mucho rato que os paséis con el secador."
    nor "¿Quieres pagar por esos gastos? No seas ridícula, [kia]. No sois inquilinas. Sois familia."
    if kia._var("route"):
        call BlinkXPS3 ("c27s002_435" , "x") from _call_BlinkXPS3_2758
        nor "Hablando de familia. ¿Ya le has dicho a [mc] lo del divorcio?"
        call BlinkXPS3 ("c27s002_440" , "x") from _call_BlinkXPS3_2759
        kia "No, y le pedí a [oma] que no le dijera nada. No quiero decirle nada hasta no haber decidido dónde vamos a vivir."
        kia "Si lo supiera, seguro que me presionaría para que nos quedáramos aquí."
        call BlinkXPS3 ("c27s002_445" , "x") from _call_BlinkXPS3_2760
        eil "Aún no conoces a [mc] lo suficiente, Mamá. Él buscaría soluciones y argumentos para que no te fueras."
        eil "Pero no te presionaría. La decisión es tuya y él la aceptará. Sólo te propondrá alternativas."
        call BlinkXPS3 ("c27s002_450" , "x") from _call_BlinkXPS3_2761
        kia "¿Y crees que eso no sería una forma de presión? Llevamos juntos diez días y le digo que me voy de casa para vivir en nuestra casa."
        kia "Si empieza a proponer alternativas y las rechazo todas... parecerá que no quiero vivir en la misma casa que él..."
        kia "Por eso es mejor hacerlo ahora que lo hemos decidido."
    else:
        call BlinkXPS3 ("c27s002_440" , "x") from _call_BlinkXPS3_2762
        kia "Bueno, da lo mismo. Nos iremos de casa para vivir en nuestra casa. Ya te he dicho que lo hemos decidido."
    call BlinkXPS3 ("c27s002_455" , "x") from _call_BlinkXPS3_2763
    eil "Y yo te he dicho que no 'hemos decidido' nada. Tú has tomado tu decisión. Yo la mía."
    eil "[nor] ha dicho que soy bienvenida, con lo que me voy a quedar aquí."
    call BlinkXPS3 ("c27s002_460" , "x") from _call_BlinkXPS3_2764
    nor "¿De verdad quieres volver a vivir en esa casa? ¿Tú sola?"
    nor "Lo único que te va a traer son malos recuerdos. Si [eil] fuera contigo, podríais crear recuerdos nuevos."
    nor "Pero le he ofrecido quedarse, ha aceptado, y no voy a retirar la invitación."
    call BlinkXPS3 ("c27s002_465" , "x") from _call_BlinkXPS3_2765
    kia "Lo sé, pero no es que quiera. Es que debo. Me estáis haciendo sentir incómoda con tanta amabilidad."
    kia "Una vez Solomon se vaya de casa, las circunstancias que os obligaron a acogernos habrán desaparecido."
    call BlinkXPS3 ("c27s002_470" , "x") from _call_BlinkXPS3_2766
    nor "*Risa* ¿Obligado? ¿Te has dado un golpe en la cabeza?"
    nor "Que viváis aquí es una de las mejores cosas que le han pasado a esta familia."
    nor "¡Entre vosotras, las estudiantes, mi madre y mi tía, la casa está más viva que nunca!"
    call BlinkXPS3 ("c27s002_475" , "x") from _call_BlinkXPS3_2767
    bet "He oído que alguien me nombraba... ¿Qué estáis discutiendo, si puedo preguntarlo?"
    scene c27s002_400b with dissolve
    nor "Hola, Tía [bet]."
    eil "Mi madre se ha vuelto idiota y quiere volver a nuestra casa..."
    kia "¡[eil]!"
    call BlinkXPS3 ("c27s002_480" , "x") from _call_BlinkXPS3_2768
    bet "Desde luego que te has vuelto idiota. ¿Quieres volver a vivir con Solomon?"
    if kia._var("route"):
        bet "¿Ahora que estás con [mc]? ¿Estás loca?"
    call BlinkXPS3 ("c27s002_485" , "x") from _call_BlinkXPS3_2769
    kia "No, no sería vivir con Solomon. Me ha pedido el divorcio y me cede la casa. Se irá... no sé cuándo se irá."
    scene c27s002_400c with dissolve
    nor "Y como [kia] ya era idiota de antes, cree que es una carga en casa y por eso quiere volver allí."
    kia "*Risa* ¡[nor]! ¿Todo el mundo va a llamarme idiota hoy?"
    eil "*Risa* Tiene razón. No en que seas una carga, claro. Ya querías irte antes de la fiesta de cumpleaños."
    eil "Si todo el mundo te llama idiota, por algo será..."
    call BlinkXPS3 ("c27s002_490" , "x") from _call_BlinkXPS3_2770
    bet "¿Puedo hacerte una propuesta, [kia]?"
    bet "Conseguirías lo que quieres y todas conseguiríamos que sigas viviendo 'en casa', que es lo que queremos el resto."
    bet "¿Cuántas habitaciones tiene tu casa?"
    call BlinkXPS3 ("c27s002_495" , "x") from _call_BlinkXPS3_2771
    kia "Cuatro, pero no lo entiendo. Son cosas incompatibles. O vivo aquí o no vivo aquí."
    kia "¿Y qué tiene que ver el número de habitaciones?"
    call BlinkXPS3 ("c27s002_500" , "x") from _call_BlinkXPS3_2772
    bet "[eri] y yo tenemos un plan. ¿Nos acogerías a [mee] y a mí durante unos meses?"
    bet "¿Y estarías interesada en vender tu casa y que construyéramos una aquí cerca si podemos comprar la parcela y construir en ella?"
    scene c27s002_400d with dissolve
    eil "¿Qué?" (multiple=2)
    kia "*Jadeo* ¿QUÉ?" (multiple=2)
    nor "¿Qué? ¿Qué parcela, Tía [bet]?"
    call BlinkXPS3 ("c27s002_505" , "x") from _call_BlinkXPS3_2773
    bet "Una de las que hay al otro lado de la carretera, o la de más allá de casa de [mar]."
    bet "Si conseguimos comprarla, voy a proponerle a [mee] que, en vez de comprar o alquilar algo en el centro, construyamos una casa ahí."
    bet "Si [kia] quiere, puede unirse a la iniciativa y podemos construir una casa más grande."
    scene c27s002_400e with dissolve
    eil "¡Di que sí, Mamá!"
    kia "¡Me encantaría!"
    call BlinkXPS3 ("c27s002_510" , "x") from _call_BlinkXPS3_2774
    bet "¡Estupendo! Tendríamos que saber quiénes son los dueños de la parcela que elijamos, y saber si podremos construir."
    bet "Supongo que después habrá que pedir permisos de construcción, pero de eso se ocupará [mee] si la convenzo..."
    call BlinkXPS3 ("c27s002_515" , "x") from _call_BlinkXPS3_2775
    nor "*Risa*"
    call BlinkXPS3 ("c27s002_520" , "x") from _call_BlinkXPS3_2776
    bet "¿De qué te ríes, [nor]?"
    call BlinkXPS3 ("c27s002_525" , "x") from _call_BlinkXPS3_2777
    nor "Las tres parcelas que hay al otro lado de la carretera, las tres de detrás de las casas, y la que hay más allá de casa de [mar] no las podréis comprar."
    nor "La propietaria es una bruja que no os las va a vender."
    nor "¡Son mías desde hace años! Las compró Mike para que nadie pudiera construir cerca nuestro."
    nor "Os las cederé gustosa, con un par de condiciones."
    scene c27s002_530d with dissolve
    nor "La primera es que mientras dure la construcción, vendréis todos los días a comer y a cenar."
    nor "La segunda es que te unas al proyecto de mi madre y mi tía."
    nor "Y no vas a dejar que dos ancianitas se tengan que ir lejos de su familia por no unirte a ellas, ¿verdad?"
    scene c27s002_400f with hpunch
    eil "¿Qué? ¿Son tuyas?" (multiple=2)
    kia "¿Qué? ¡Claro que me uniría!" (multiple=2)
    scene c27s002_400g with hpunch
    bet "¿Qué?"
    call BlinkXPS3 ("c27s002_530" , "x") from _call_BlinkXPS3_2778
    nor "*Risa* ¿Por qué creéis que mi parcela es más pequeña que la de [mar] y no tiene piscina?"
    nor "Mike se dejó un dineral en esas parcelas. Siempre quiso que las usara alguien de la familia cuando se quisiera independizar."
    nor "Creo que estaría contento de que seáis vosotras, aunque nunca le cayó muy bien Mamá."
    call BlinkXPS3 ("c27s002_535" , "x") from _call_BlinkXPS3_2779
    bet "*Risa* Esto parece el inicio del 'Barrio Marks'."
    scene c27s002_400h with dissolve
    "Las cuatro mujeres empiezan a hacer planes sobre la construcción de la casa."
    "Son castillos en el aire, ya que ni siquiera [nor] sabe qué hay que hacer para construir en esas parcelas."
    "Pero la ilusión de no separar a la familia es mayor que la posibilidad de que surjan problemas."
    stop music fadeout (1.5)
    scene black with dissolve
    return
label c27s002_AmaAtCollege1:
    scene c27s002_200d with fade
    "Pocos minutos después de que [bet] se haya ido..."
    play sound ("music/RingtoneMC.ogg")
    "*Ring-Ring*"
    scene c27s002_550a with dissolve
    stop sound
    mc "Hola, [ama]. ¿Cómo ha ido?"
    call BlinkXS3 ("c27s002_555") from _call_BlinkXS3_463
    play music ("music/Rise-Up.ogg")
    ama "¡Horrible! ¡Odio a los Washington!"
    mc "¿Qué ha pasado?"
    call BlinkXS3 ("c27s002_560") from _call_BlinkXS3_464
    ama "¡[sam] me ha hecho comer dos raciones de pierogi!"
    ama "¡Casi no puedo moverme! Voy a tener que correr muchos kilómetros en la cinta para quemar todas esas calorías."
    mc "*Risa* Los pierogi de [sam.nick] están buenísimos."
    call BlinkXS3 ("c27s002_565") from _call_BlinkXS3_465
    ama "¡Están deliciosos! Pero después de los primeros diez..."
    ama "Ahora mismo estoy mirando por el retrovisor con miedo de que salga con una bandeja para que me la lleve a la base."
    mc "¿Te has comido diez pierogis? No me extraña que no puedas moverte."
    call BlinkXS3 ("c27s002_570") from _call_BlinkXS3_466
    ama "He dicho los primeros diez... [sam.nick] me ha obligado a seguir comiendo..."
    mc "*Risa* ¿Qué hacía Jamaal mientras tanto?"
    call BlinkXS3 ("c27s002_575") from _call_BlinkXS3_467
    ama "Fingía llorar en un rincón porque me estaba comiendo sus pierogis. Pero finge muy mal. Se le escapaba la risa."
    ama "Había comida para alimentar un regimiento de soldados hambrientos."
    mc "Acostúmbrate a las comidas de [sam]."
    mc "¿Y el otro tema? ¿Cómo ha ido?"
    call BlinkXS3 ("c27s002_580") from _call_BlinkXS3_468
    ama "Igual de mal. Pero al final ha firmado."
    mc "Si ha firmado no habrá ido tan mal, ¿no?"
    ama "Jamaal les ha hecho entrar en razón, aunque parezca mentira."
    mc "A veces Jam es el más racional de esa familia. Algunas veces. De vez en cuando. En extrañas ocasiones."
    call BlinkXS3 ("c27s002_585") from _call_BlinkXS3_469
    ama "No esperes agradecimiento de [sim], por cierto. Me han sacado que había sido idea mía."
    mc "¿Te han tendido una trampa y has caído? ¿En plan 'No te va a pasar nada si dices que la idea ha sido tuya'?"
    call BlinkXS3 ("c27s002_590") from _call_BlinkXS3_470
    ama "¡Exactamente eso! O más bien 'Estaríamos agradecidas si nos dices que has sido tú'."
    ama "A veces odio a los civiles. ¡Estáis llenos de estratagemas traicioneras!"
    mc "*Risa* Eso es lo que se siente cuando tienes una madre, [ama]. Le acabarás cogiendo el gusto."
    call BlinkXS3 ("c27s002_595") from _call_BlinkXS3_471
    ama "Bueno, voy a ir a la universidad a formalizar la inscripción de [sim]."
    mc "Ya que vas, ¿me puedes hacer un favor?"
    ama "Sí, dime qué necesitas."
    mc "Matricula a [eil] también. En este caso, que lo cobren de mi cuenta."
    call BlinkXS3 ("c27s002_600") from _call_BlinkXS3_472
    ama "¿[eil]? No tengo su expediente. No sé en qué carrera tengo que matricularla..."
    mc "No te preocupes. Tienen el expediente en la universidad. Dejó la carrera el año pasado por culpa de Solomon."
    mc "Ahora que he cobrado el primer sueldo, puedo pagarle la inscripción para su último año. No tiene por qué pagar los errores de su padre."
    call BlinkXS3 ("c27s002_605") from _call_BlinkXS3_473
    ama "Es muy generoso por tu parte, pero no sé si podré hacerlo. Me costó conseguir una plaza para [sim], y..."
    mc "Si te ponen algún problema, pide ver al Decano Jonas y dile que vas de mi parte."
    call BlinkXS3 ("c27s002_610") from _call_BlinkXS3_474
    ama "Lo haré. Voy a ir yendo, antes de que se haga más tarde. Te veo luego."
    stop music fadeout (1.5)
    mc "Hasta luego, [ama]."
    scene black with dissolve
    return
label c27s002_LisShopping:
    if _in_replay:
        $ mc._var("relationships" , 0 , "set")
        call mrS3_lis_route from _call_mrS3_lis_route_9
        call mrS3_deb_route from _call_mrS3_deb_route_15
        call mrS3_mad_route from _call_mrS3_mad_route_5
        if mad._var("route"):
            call mrS3_mad_type2 from _call_mrS3_mad_type2
            call mrS3_mar_route from _call_mrS3_mar_route_14
            call mrS3_nor_route from _call_mrS3_nor_route_9
        if mc._var("relationships") < 2:
            call mrS3_rels from _call_mrS3_rels_17
    "Pasas un rato leyendo los informes financieros que te ha enviado Aaron. La contabilidad de Daniels era como mínimo 'creativa'."
    "La doble contabilidad es para novatos. Lo de Daniels, o lo de sus contables para ser más exactos, es verdadero arte para ocultar ingresos."
    scene c27s002_245d with dissolve
    play sound ("music/knock.ogg")
    "*Knock-Knock*"
    lis "*A través de la puerta* Soy yo, ¿puedo pasar?"
    mc "Entra, [lis]."
    if lis._var("route"):
        call KissXS3 ("c27s002_650") from _call_KissXS3_11
    call BlinkXS3 ("c27s002_650") from _call_BlinkXS3_475
    play music ("music/Memories-Instrumental.ogg")
    lis "Hola, [mc]."
    if lis._var("route"):
        mc "Hola, Princesa. ¿Puedo ayudarte en algo?"
    else:
        mc "Hola, [lis]. ¿Puedo ayudarte en algo?"
    call BlinkXS3 ("c27s002_655a") from _call_BlinkXS3_476
    lis "Venía a ver la cama nueva. ¡Es enorme! Van a ser geniales los abrazos de los domingos."
    mc "*Risa* En el momento en que se corra la voz sobre los abrazos, estaremos 23 ahí. No sé si cabremos."
    mc "Creo que será mejor mover los abrazos al jardín de [nor]. Allí se podría unir incluso Jamaal. *Risa* Aquí no va a subir."
    call BlinkXS3 ("c27s002_655b") from _call_BlinkXS3_477
    lis "Hablando de Jamaal..."
    mc "¿Qué pasa con él?"
    call BlinkXS3 ("c27s002_660") from _call_BlinkXS3_478
    lis "Esta mañana he visto a Anthony en la universidad. Me ha dicho que los viste juntos..."
    mc "Sí. No sabía que él me había visto."
    lis "Bueno, por lo visto se lo ha dicho Jamaal... Y que te ha dicho que salen juntos..."
    mc "¿Y hay algún problema con eso? Supongo que tú no tienes ningún problema con que salgan juntos."
    if lis._var("route"):
        mc "Tú sales conmigo y Anthony con Jamaal. No veo que haya ningún problema."
    call BlinkXS3 ("c27s002_665") from _call_BlinkXS3_479
    lis "No lo digo por mí. Lo digo por ti."
    mc "¿Por mí? Yo me alegro mucho por Jamaal. Anthony es un tipo afortunado si está saliendo con él."
    mc "*Risa* Y negaré haber dicho eso si alguna vez Jamaal me pregunta."
    call BlinkXS3 ("c27s002_670") from _call_BlinkXS3_480
    lis "Espera... ¿qué te ha contado Jamaal sobre Anthony?"
    mc "Todo. Cómo se conocieron, que tenía dudas sobre su sexualidad cuando estaba intentándolo contigo, cómo empezaron a salir cuando por fin se decidió..."
    mc "¿Por qué lo preguntas?"
    call BlinkXS3 ("c27s002_675") from _call_BlinkXS3_481
    lis "Me parece raro que no hagas ninguna broma ingeniosa sobre que Jamaal ha acabado saliendo con una chica."
    lis "Aunque Anthony ya no es una chica, claro. Pero ya sabes... hay gente que no acepta a los trans o que hacen bromas de mal gusto."
    mc "¿Ves? Eso no me lo había contado."
    scene c27s002_680d with dissolve
    lis "¡Oops! ¡Acabo de meter la pata!"
    call BlinkXS3 ("c27s002_680") from _call_BlinkXS3_482
    lis "Cuando has dicho que te lo había contado todo y lo de sus dudas..."
    mc "Bueno, parece que me ha contado todo lo que creía que yo debía saber en ese momento."
    mc "Me dijo que había cosas que no tenía el derecho a contarme. Supongo que se refería a esto."
    mc "Pero me da lo mismo. Jamaal está contento y supongo que Anthony también. Es suficiente para mí."
    call BlinkXS3 ("c27s002_685") from _call_BlinkXS3_483
    lis "Sí. Está muy contento. Lo ha pasado mal y estaba... confuso."
    lis "Cuando me lo explicó se sentía avergonzado, tanto por nuestra situación como por lo que ha tenido que pasar."
    lis "Me hizo prometer que no se lo contaría a nadie que lo conociera..."
    mc "*Risa* Y me lo has contado a mí por error. ¡Me encantan esos malentendidos!"
    call BlinkXS3 ("c27s002_690") from _call_BlinkXS3_484
    lis "*Risa* ¡Me has dicho que te lo había explicado todo!"
    mc "*Risa* Yo creía que me lo había explicado todo."
    mc "Pero no te preocupes. A mí no se me escapará."
    call BlinkXS3 ("c27s002_695") from _call_BlinkXS3_485
    lis "¡Eres un capullo!"
    mc "Es posible. *Risa* Me lo dicen mucho."
    if lis._var("route"):
        mc "Pero soy tu capullo."
        call KissXS3 ("c27s002_650") from _call_KissXS3_12
    call BlinkXS3 ("c27s002_650") from _call_BlinkXS3_486
    lis "En eso tienes razón."
    lis "Bueno, me voy, que tengo que coger el bus para ir a la tienda de [mad.nick]."
    mc "¿Vas a comprar más ropa? ¿No tienes suficientes con las cuatro maletas que trajiste?"
    mc "Mas todo lo que después trajeron los transportistas, claro. Tienes suerte de que tu habitación sea tan grande como la de [emm]."
    call BlinkXS3 ("c27s002_705a") from _call_BlinkXS3_487
    if lis._var("route"):
        lis "*Risa* ¿Vas a decirle a tu princesa cuánta ropa tiene que tener?"
    else:
        lis "*Risa* ¿Vas a decirle a una chica cuánta ropa tiene que tener?"
    lis "Parece mentira que te hayas criado rodeado de mujeres."
    mc "No me atrevería nunca a decir algo así. *Risa* Sólo preguntaba."
    mc "Pero no hace falta que cojas el bus. Tengo que ir al centro a comprar unas cosas yo también."
    mc "Las iba a comprar ayer, pero al encontrarme con Jamaal se me hizo tarde y me olvidé."
    call BlinkXS3 ("c27s002_700") from _call_BlinkXS3_488
    lis "¡Genial! Voy a coger el bolso y te espero abajo."
    mc "¿Vas a ir así?"
    call BlinkXS3 ("c27s002_705b") from _call_BlinkXS3_489
    lis "¿No te gusta?"
    mc "¡Me encanta! Pero me sorprende que quieras ir así fuera de casa. Hace unas semanas te hubieras preocupado por si te veía algún conocido."
    call BlinkXS3 ("c27s002_705c") from _call_BlinkXS3_490
    lis "Hace unas semanas no sabía lo que era ser libre de todas esas tonterías."
    lis "No voy a renunciar a ello."
    if lis._var("route"):
        call KissXS3 ("c27s002_650") from _call_KissXS3_13
    call BlinkXS3 ("c27s002_650") from _call_BlinkXS3_491
    if lis._var("route"):
        lis "Hasta ahora mismo. No me canso de besarte."
        mc "Hasta ahora mismo. Espero que no lo hagas nunca."
    else:
        lis "Hasta ahora mismo."
        mc "Te veo en un momento."
    scene drive_day
    stop music fadeout (1.5)
    "Conduces hasta la tienda de [mad.nick] y decides entrar a saludar."
    scene c27s002_710a with dissolve
    play music ("music/IWonderWhatIllDoToday.ogg")
    "Al llegar a la tienda, [mad.nick] está atendiendo a una clienta."
    mad "Buenas tardes, [lis] y [mc]. Dadme un segundo para que acabe una cosa."
    mc "No te preocupes."
    lis "Voy a ir mirando algo de ropa mientras acabas."
    call BlinkXPS3 ("c27s002_715" , "x") from _call_BlinkXPS3_2780
    lis "Deberíamos haber venido antes. Cada vez que la madre de [mad.nick] viene, la pone de mal humor."
    mc "¿Es su madre?"
    call BlinkXS3 ("c27s002_720") from _call_BlinkXS3_492
    lis "Sí, y su jefa. Tienen varias tiendas en el condado. Ella es la encargada de la tienda de Atascadero."
    if mad._var("sub") or mad._var("romance") and mar._var("fittingRoom"):
        mcp "(Ahora entiendo por qué no quería que le mandara las pruebas del chantaje a su jefe.)"
        mcp "(Hubiera sido malo si sólo hubiera sido su jefe, pero si además es su madre...)"
    mc "No tenía ni idea."
    call BlinkXS3 ("c27s002_725") from _call_BlinkXS3_493
    lis "Cuando se trata de trabajo, la Sra. Chang no trata a [mad.nick] como a una hija sino como a una empleada."
    lis "Y para dar ejemplo al resto de dependientas, es especialmente estricta con ella. Para que nadie la acuse de favoritismo."
    mc "Que la trate como a una empleada me parece lógico. Lo otro, no tanto."
    call BlinkXS3 ("c27s002_730") from _call_BlinkXS3_494
    lis "Y si como jefa es mala, como madre es de las que están encima permanentemente."
    lis "Ella y su padre se mudaron a Atascadero hace unos años y [mad.nick] se quedó aquí. No les sentó bien."
    lis "Desde entonces está encima de ella permanentemente. Intenta fiscalizar cómo vive, si tiene novio..."
    if mad._var("route"):
        mc "Lo que me da a entender que no le ha dicho que estamos juntos."
        if mc._var("relationships")>1:
            mc "Ni que hay un harén por en medio."
            call BlinkXS3 ("c27s002_735") from _call_BlinkXS3_495
            lis "Exacto. ¿Te imaginas contarle a alguien así que compartes novio con otras mujeres?"
            if mar._var("route") or nor._var("route"):
                mc "*Risa* Lo imagino perfectamente. Lo viví cuando Meemaw se enteró."
            else:
                mc "*Risa* Es normal que quiera ocultárselo a su madre si es así."
            lis "No todas las madres son como [mar]."
        else:
            call BlinkXS3 ("c27s002_735") from _call_BlinkXS3_496
            lis "Exacto. Quiere ahorrarse las charlas. No todas las madres son como [mar]."
            lis "Si le dice que sale contigo, va a tener que pasar por un interrogatorio."
    else:
        mc "Y es normal que [mad.nick] no quiera decirle nada, supongo."
        call BlinkXS3 ("c27s002_735") from _call_BlinkXS3_497
        lis "Exacto. Cuanto más encima está de ella, más evita [mad.nick] decirle nada. No todas las madres son como [mar]."
    if not persistent.family:
        lis "Ya sé que no es tu madre, pero es difícil verla de otra manera."
    mc "La verdad es que tengo mucha suerte."
    if lis._var("route"):
        mc "Hablando de madres... ¿Les has dicho algo a tus padres sobre nosotros?"
        call BlinkXS3 ("c27s002_740") from _call_BlinkXS3_498
        lis "Todavía no. Si lo hiciera, al día siguiente estarían aquí para conocerte. O en el mismo día, si se lo digo por la mañana."
        lis "No quiero ponerte en ese compromiso sin antes consultarlo contigo."
        mc "Si no te avergüenzas de mí o de nuestra relación, no tengo ningún problema en conocerlos."
        if deb._var("route"):
            mc "Pero quedaría el tema de [deb.nick]. No sé si estarían muy contentos de que salga con sus dos princesas."
            call BlinkXS3 ("c27s002_745") from _call_BlinkXS3_499
            lis "*Risa* Creía que la princesa era yo."
            mc "No sé si las dos sois sus princesas, pero las dos sois las mías."
            call BlinkXS3 ("c27s002_750") from _call_BlinkXS3_500
            lis "Seguramente si les dijéramos que las dos salimos contigo vendrían igual, pero con las escopetas de caza. *Risa*"
            mc "Un enfrentamiento a tiros entre tus padres y [ama] y [eva]... *Risa* Interesante."
        elif mc._var("relationships")>1:
            mc "Pero quedaría el tema del harén. No sé si estarían muy contentos de que salgas con alguien que sale con otras mujeres."
            call BlinkXS3 ("c27s002_750") from _call_BlinkXS3_501
            lis "Seguramente si se lo dijera vendrían igual, pero con las escopetas de caza. *Risa*"
            mc "Un enfrentamiento a tiros entre tus padres y [ama] y [eva]... *Risa* Interesante."
        call BlinkXS3 ("c27s002_755") from _call_BlinkXS3_502
        lis "Pero, en serio, no me avergüenzo de nada, con lo que lo tendrán que aceptar. Pero prefiero dejar pasar un tiempo antes de decírselo."
        lis "Lo de 'Mamá, llevo tres semanas aquí y estoy saliendo con alguien' no quedaría muy bien a los ojos de mis padres."
        mc "Se lo diremos cuando quieras. Cuenta conmigo para ello."
        call BlinkXS3 ("c27s002_760") from _call_BlinkXS3_503
        lis "Pienso que, como en el caso de [mad.nick], no tienen que tener voz ni voto en con quien salgo. Soy una adulta y es mi decisión."
        mc "Estoy de acuerdo, pero supongo que quieren cuidar de ti y evitar que cometas errores."
    stop music fadeout (1.5)
    scene c27s002_710b with fade
    mad "Ya hemos acabado, chicos. ¿En qué puedo ayudaros?"
    play music ("music/OneLastChance.ogg")
    mad "[mc], ven. Quiero presentarte a mi madre, Rose."
    scene c27s002_765a with dissolve
    mc "Encantado de conocerla, Sra. Chang."
    "Sra. Chang" "Igualmente. ¿Eres amigo de mi hija?"
    mc "Sí, somos buenos amigos."
    scene c27s002_765b with dissolve
    "Sra. Chang" "Y no tendrás un amigo soltero, ¿verdad? Porque tú estás con [lis], ¿verdad?"
    "Sra. Chang" "A este paso, [mad] va a parecer un meme. Llegará a los 30 sola y con su piso lleno de gatos. Ya ha empezado."
    "Te cae mal inmediatamente. Sabes que [mad.nick] odia que la llamen [mad] y, pese a todo, su madre usa ese nombre. Te enfadas inmediatamente."
    "Además, tiene una de esas sonrisas que no llegan a los ojos. Una sonrisa tan falsa como un billete naranja de 100 dólares."
    mcp "(¿Quién eres tú para decidir cómo tiene que vivir su vida [mad.nick]?)"
    mcp "(Si quiere tener diez gatos, ¿qué más da?)"
    "Tu enfado evita que pase por tu mente la idea de que, con diez gatos, vas a gastar un montón de dinero en camas."
    mc "Tengo amigos solteros..."
    "La sangre empieza a hervirte en las venas. Nunca has podido soportar este tipo de madre, y menos aún con lo que te ha dicho [lis]."
    if mad._var("route"):
        scene c27s002_770An
        "Miras a [mad.nick], que entiende tu pregunta y da su aprobación con un ligero asentimiento."
    scene c27s002_765b
    mc "Pero no se preocupe. No va a llegar sola ni a los 30 ni a los 27."
    if mad._var("route"):
        scene c27s002_775An1
        pause (2.5)
        "Rodeas a la diminuta mujer pese a su cara de perplejidad y besas dulcemente a [mad.nick]."
        "Al principio se tensa un poco por la sorpresa, quizás has malinterpretado su asentimiento."
        "No tarda en devolverte el beso. Abrazándote con fuerza. Como un náufrago agarrándose a una madera en medio de una tormenta."
        scene c27s002_765c with dissolve
        "Cuando vuelves a mirar a la odiosa mujer, su cara de sorpresa es genuina. Ya no hay falsedad en ella."
        mc "Va a llegar a los 30, a los 60, o a los 90 conmigo, si ella quiere."
        "Sra. Chang" "¿Qué? ¿Cuándo? ¿Desde cuándo?"
        "Sabes que enemistarte con tu futura suegra nada más conocerla no es una buena idea. Pero tienes que dejarle las cosas claras desde el principio."
        mc "Si [mad.nick] no se lo ha querido contar, pregúntese por qué."
        mc "Adiós, Sra. Chang. Yo que usted, empezaría a llamar a [mad.nick] por el nombre que ella prefiere."
        call BlinkXPS3 ("c27s002_780" , "x") from _call_BlinkXPS3_2781
        mc "Te espero en el café en el que te esperé la primera vez que fuimos a tu piso."
        "Falta menos de una hora para que cierre la tienda."
        mad "Hasta luego, [mc]."
    else:
        scene c27s002_775An2
        pause (2.5)
        "Rodeas a la diminuta mujer pese a su cara de perplejidad y abrazas fuertemente a [mad.nick]."
        "Su sorpresa no evita que te devuelva el abrazo. Con fuerza. Como un náufrago agarrándose a una madera en medio de una tormenta."
        mc "*Susurro* No estás sola."
        scene c27s002_765c with dissolve
        "Cuando vuelves a mirar a la odiosa mujer, su cara de sorpresa es genuina. Ya no hay falsedad en ella."
        mc "Va a llegar a los 30, a los 60, o a los 90 con una familia que no se mete en cómo vive su vida."
        mcp "(Y si por eso entiendes que estamos juntos, es tu problema.)"
        "Sra. Chang" "¿Qué? ¿Cuándo? ¿Desde cuándo?"
        mc "Si [mad.nick] no se lo ha querido contar, pregúntese por qué."
        mc "Adiós, Sra. Chang. Yo que usted, empezaría a llamar a [mad.nick] por el nombre que ella prefiere."
        call BlinkXPS3 ("c27s002_780" , "x") from _call_BlinkXPS3_2782
        mc "Te espero para tomar un café en las galerías cuando cierres, [mad.nick]."
        "Falta menos de una hora para que cierre la tienda."
        mad "Me parece una idea genial, [mc]."
    call BlinkXPS3 ("c27s002_785" , "f") from _call_BlinkXPS3_2783
    "Te diriges a despedirte de [lis]."
    if lis._var("route"):
        "Hay algo en su mirada que te dice que no es buena idea besarla para despedirte."
    mc "¿Necesitas que te lleve a casa luego?"
    lis "*Susurrando* No hace falta, gracias. Voy a quedarme aquí hasta que [mad.nick] cierre para evitar que su madre la bombardee a preguntas."
    if mad._var("route"):
        lis "*Susurrando* Después cogeré un Under para volver a casa y os dejo solos tomando ese café."
    else:
        lis "*Susurrando* Después la acompañaré a ese café, si no te importa."
        mc "Para nada. Eres bienvenida a ese café."
    scene c27s002_785d with hpunch
    lis "*Susurrando* ¡Eso ha sido increíble!"
    "No podías imaginar que [lis] pudiera saltar tanto."
    lis "*Susurrando* Cómo has dejado a su madre con la boca abierta... No mires, pero sigue con la boca abierta."
    if lis._var("route"):
        lis "*Susurrando* Empiezo a estar un poco menos asustada porque conozcas a mis padres."
        mc "*Susurrando* ¿Estabas asustada por mí? *Risa*"
        lis "*Susurrando* Un poco. Pero ahora empiezo a estar asustada por ellos. *Risa*"
    if mad._var("route"):
        mc "*Risa* Te veo en casa."
    else:
        mc "*Risa* Te veo en el café."
    scene c27s002_785e with fade
    "Te vas de la tienda sin una palabra más. Sintiéndote un como un personaje de una serie policiaca mala ambientada en Miami."
    "Sólo te falta ser pelirrojo y tener unas gafas de sol."
    stop music fadeout (1.5)
    "Y una explosión detrás tuyo. Casi esperas escuchar la cabeza de la madre de [mad.nick] explotar en cualquier momento."
    return
label c27s002_AmaAtCollege2:
    if _in_replay:
        call mrS3_mad_route from _call_mrS3_mad_route_6
    scene c27s002_800d with dissolve
    "Nada más salir de la tienda..."
    play sound ("music/RingtoneMC.ogg")
    "*Ring-Ring*"
    call BlinkXPS3 ("c27s002_800" , "f") from _call_BlinkXPS3_2784
    stop sound
    mc "Hola, [ama]. ¿Algún problema en la universidad?"
    play music ("music/Rise-Up.ogg")
    ama "Ya he hecho lo de [sim]. Pero hay un problema con lo de [eil]."
    mc "¿Qué ha pasado?"
    call BlinkXS3 ("c27s002_805") from _call_BlinkXS3_504
    ama "Alguien ha pagado su matrícula. Se te han adelantado."
    mc "¿Quién ha sido? ¿Lo has podido averiguar?"
    call BlinkXS3 ("c27s002_810") from _call_BlinkXS3_505
    ama "Me ha atendido Anthony y no me ha querido decir quién lo ha hecho, pero me lo puedo imaginar. [lis] y [deb.nick]."
    mc "Tiene lógica. Hasta ayer eran las únicas a las que les sobraba el dinero para hacerlo."
    mc "Me extraña que no hayan hecho lo mismo con [sim]."
    call BlinkXS3 ("c27s002_815") from _call_BlinkXS3_506
    ama "Sobre eso, a Anthony se le ha escapado algo. Ha dicho, 'Ellas lo intentaron, pero no teníamos su expediente'."
    ama "Ese 'Ellas' deja muy claro quiénes son."
    mc "*Risa* Por suerte no lo consiguieron, o te hubieras quedado sin los pierogis de agradecimiento."
    call BlinkXS3 ("c27s002_820a") from _call_BlinkXS3_507
    ama "*Risa* ¡No me hables de pierogis! Se me remueven en el estómago y a la vez tengo una sensación de antojo."
    mc "*Risa* ¿Sabes que cada vez estoy más orgulloso de todas vosotras?"
    call BlinkXS3 ("c27s002_820b") from _call_BlinkXS3_508
    ama "¿Por hacer lo que ibas a hacer tú? ¿No te sientes cómo si te hubieran robado la oportunidad de hacer algo por [eil]?"
    mc "No lo hacía por 'hacer algo por ella'. El objetivo era que ella volviera a estudiar, no que nadie me lo agradeciera."
    mc "Da lo mismo si el objetivo se ha cumplido gracias a las hermanas o a mí. Lo importante es que [eil] va a poder volver a la universidad."
    call BlinkXS3 ("c27s002_825") from _call_BlinkXS3_509
    ama "Al menos, a ti no te engordarán con una tonelada de pierogis."
    mc "Tienes que aprender que incluso a [sam.nick] le puedes decir que no quieres más."
    call BlinkXS3 ("c27s002_830") from _call_BlinkXS3_510
    ama "Pero estaban tan buenos..."
    mc "Y es agradable sentir el agradecimiento, ¿verdad?"
    call BlinkXS3 ("c27s002_835") from _call_BlinkXS3_511
    ama "Es una pasada. No por el agradecimiento en sí, sino por lo bien que me estaba sintiendo yo por haber pensado en una forma de ayudar."
    ama "Ver la alegría de [sim] porque por fin va a poder ir a la universidad ha sido increíble."
    ama "Saber que la idea que ha propiciado esa alegría ha sido mía... No sé... Produce una sensación de calor en el estómago."
    mc "*Risa* ¡Eso eran los pierogis!"
    call BlinkXS3 ("c27s002_840") from _call_BlinkXS3_512
    ama "*Risa* ¡Capullo! ¡No voy a comer en dos días!"
    mc "¿No vienes a cenar a casa hoy?"
    ama "*Risa* Sí. Por eso no he dicho en qué dos días. Seguramente me ponga a dieta cuando lleguemos a Aruba."
    mc "*Risa* ¿Entiendes ahora por qué estaba gordo?"
    call BlinkXS3 ("c27s002_845") from _call_BlinkXS3_513
    ama "Lo que no entiendo es cómo no te deprimiste cuando fuiste a Portland y tuviste que dejar de comer los platos de [mar], [nor], y [sam.nick]."
    mc "*Risa* Busqué un jefe que era un gourmet. Comer con él varios días por semana sirvió como sustituto."
    call BlinkXS3 ("c27s002_850") from _call_BlinkXS3_514
    ama "Bueno, [mc]. Te voy a dejar. Quiero ir a la base a ducharme antes de ir a casa a cenar. ¿Te veo luego?"
    if mad._var("route"):
        mc "No lo sé. Acabo de salir de la tienda de [mad.nick] y he tenido un encontronazo con su madre."
        mc "Le he dicho que esperaré a que cierre para tomar un café. No sé qué haremos luego."
        call BlinkXS3 ("c27s002_855") from _call_BlinkXS3_515
        ama "Vete a cenar con ella. Por lo que he oído, la madre es una bruja y seguro que [mad.nick] necesita un poco de apoyo."
        ama "O tráela a cenar a casa y le damos apoyo todas."
        mc "Mi idea era ir a cenar. Hace días que no hemos tenido tiempo a solas y..."
        call BlinkXS3 ("c27s002_860") from _call_BlinkXS3_516
        ama "Hazlo. Le diré a [mar] que no vienes ni a cenar ni a dormir."
        mc "Yo no he dicho nada de no ir a dormir."
        call BlinkXS3 ("c27s002_865") from _call_BlinkXS3_517
        ama "Bueno, esta vez soy yo la que toma la decisión por ti. ¿Cómo sienta cuando se cambian las tornas?"
        mc "*Risa* Sienta genial. Te veo mañana, [ama]."
        ama "Te veo mañana. Pasáoslo bien."
    else:
        mc "Sí. Acabo de salir de la tienda de [mad.nick] y he tenido un encontronazo con su madre."
        mc "Le he dicho que esperaré a que cierre para tomar un café. Después iré a casa."
        call BlinkXS3 ("c27s002_855") from _call_BlinkXS3_518
        ama "Parece una buena idea. Por lo que he oído, la madre es una bruja y seguro que [mad.nick] necesita un poco de apoyo."
        ama "O tráela a cenar a casa y le damos apoyo todas."
        mc "Se lo propondré, a ver qué le parece. Te veo luego."
        ama "Hasta luego, [mc]."
    stop music fadeout (1.5)
    scene black with dissolve
    return
label c27s003_NoMad:
    scene c27s003_1000 with fade
    "Llegas al café y, tras pedir un zumo de piña, juegas un rato a My Residence."
    "Tienes una tórrida escena con Dee-Dee en su piso."
    "Su perro no está en casa, con lo que, según el narrador, evitas tener que estar vigilando los muebles."
    mcp "(*Risa mental* ¡Ni que fuera Zeus!)"
    return
label c27s003_MadLis:
    if _in_replay:
        "La escena es más larga si no estás en ruta con [mad.nick]."
        call mrS3_lis_route from _call_mrS3_lis_route_11
        call mrS3_mad_route from _call_mrS3_mad_route_7
    if mad._var("route"):
        scene black with dissolve
        "Llegas al café y, tras pedir un zumo de piña, pasas un rato leyendo noticias en el móvil."
    scene c27s003_005a with fade
    "Al cabo de un rato llegan las chicas."
    play music ("music/MorningFunnyBeat.ogg")
    if mad._var("route"):
        call KissXS3("c27s003_010") from _call_KissXS3_14
        "[mad.nick] es la primera en besarte."
    call BlinkXS3("c27s003_010") from _call_BlinkXS3_520
    mad "Gracias por lo que has hecho en la tienda."
    mc "¿Te ha bombardeado tu madre mucho a preguntas?"
    mad "No ha podido gracias a [lis]."
    if lis._var("route"):
        call KissXS3("c27s003_015") from _call_KissXS3_15
        if mad._var("route"):
            "[lis] también quiere su beso. Te lo da en cuanto la dependienta se sienta."
        else:
            "[lis] te besa en cuanto la dependienta se sienta."
    call BlinkXS3("c27s003_015") from _call_BlinkXS3_521
    lis "Puedo convertirme en una Karen en cualquier momento, y ese ha sido el momento perfecto."
    lis "*Risa* Mi faceta de clienta odiosa que quiere que le enseñen todo puede ser muy útil."
    mc "*Risa* Y como la jefa ya estaba ahí, no podías pedir hablar con ella."
    call BlinkXS3("c27s003_020") from _call_BlinkXS3_522
    lis "Exacto, aparta y déjame sitio."
    mc "Lo hago porque te lo has ganado. *Risa*"
    call BlinkXPS3("c27s003_025" , "f") from _call_BlinkXPS3_2785
    mad "La verdad es que hacía mucho que no veía a mi madre tan sorprendida. Normalmente todo el mundo hace lo que ella quiere."
    if mad._var("route"):
        mc "Pues creo que, si alguna vez me invita a una reunión familiar, no voy a ser su yerno favorito."
    else:
        mc "Pues creo que ha encontrado un rival en mí."
    mc "No me estaba gustando cómo estaba hablando de ti con un tipo al que acaba de conocer. Ni que te llamara [mad], sabiendo lo poco que te gusta."
    call BlinkXS3("c27s003_030") from _call_BlinkXS3_523
    mad "Lo de [mad] nunca me ha gustado, pero lo entiendo. Es el nombre con el que ella siempre ha pensado en mí."
    mad "Pero no me gusta que quiera avergonzarme con lo de acabar siendo una solterona que acaba sola con la casa llena de gatos."
    if mad._var("route"):
        mc "Bueno, no vas a ser una solterona ni a estar sola. Y lo de los gatos... Si alguna vez tienes más de uno..."
    else:
        mc "Bueno, no vas a estar sola. Y lo de los gatos... Si alguna vez tienes más de uno..."
    call BlinkXS3("c27s003_035") from _call_BlinkXS3_524
    lis "Evitaremos que entren en tu habitación. *Risa* Espero que esa cama dure mucho."
    lis "La próxima vez tenemos que sustituir a Zeus por [mad.nick]."
    mc "*Risa* Podemos poner una lata de una tonelada de atún al lado de la piscina para evitar que se mueva de ahí."
    call BlinkXS3("c27s003_040") from _call_BlinkXS3_525
    mad "No os metáis con el pobre Zeus. Suficiente tiene con llevar dos días en el veterinario."
    mc "¿Qué? ¿Qué le pasa?"
    call BlinkXS3("c27s003_045") from _call_BlinkXS3_526
    mad "Algunas de las chicas le dieron de comer más de lo debido y se ha puesto enfermo."
    mad "Como, a pesar de eso, sigue siendo un comilón, el veterinario me sugirió que lo dejara allí, donde lo pueden controlar mejor."
    call BlinkXS3("c27s003_050") from _call_BlinkXS3_527
    mad "Me paso el día fuera de casa y no podría controlar si abre algún armario para coger comida."
    mc "*Risa* Deberías poner candados en todas las puertas donde haya comida."
    mc "Aunque visto lo listo que es, sería capaz de aprender a usar una ganzúa."
    call BlinkXS3("c27s003_055") from _call_BlinkXS3_528
    lis "[mad.nick], te aseguro que yo sólo le di un trozo pequeño de bacon."
    mc "Creo que el problema es que tú le diste bacon, [nor] salchichas, [dap] jamón, [eil] una lata de atún, [eri] varias latas..."
    mc "La próxima vez os deberíais poner de acuerdo en quién le da qué."
    call BlinkXS3("c27s003_060") from _call_BlinkXS3_529
    mad "Bueno, creo que lo que ha pasado nos servirá de lección a todos. Zeus incluido. Ha aprendido que, si come mucho, se pone malo."
    mad "Solo faltará que lo recuerde la próxima vez que tenga comida delante."
    mc "Eso va a ser más difícil. Pese a que parece bastante listo, me da la impresión de que, cuando hay comida por en medio, no piensa demasiado."
    if mad._var("route"):
        call BlinkXS3("c27s003_065") from _call_BlinkXS3_530
        lis "Bueno, parejita, yo os voy a dejar y voy a volver a casa."
        mc "¿Al final no has comprado nada? No veo bolsas..."
        call BlinkXS3("c27s003_070") from _call_BlinkXS3_531
        lis "Sí que he comprado, pero [mad.nick] lo enviará a casa. No quería ir cargada en el Under."
        mc "*Risa* ¿Tanto has comprado?"
        call BlinkXS3("c27s003_075") from _call_BlinkXS3_532
        mad "No lo quieras saber. *Risa* Creo que [lis] se ha convertido en una de mis mejores clientas en estas semanas."
        mc "*Risa* Al final va a tener que echar a [deb.nick] de la habitación para meter toda la ropa."
        if lis._var("route"):
            call KissXS3("c27s003_015") from _call_KissXS3_16
        call BlinkXS3("c27s003_015") from _call_BlinkXS3_533
        lis "No hace falta echarla. *Risa* Con ocupar sus armarios tengo suficiente."
        stop music fadeout (1.5)
        lis "Te veo en casa, [mc]. Hasta mañana, [mad.nick]."
    else:
        call BlinkXS3("c27s003_095") from _call_BlinkXS3_534
        lis "¿No le vas a contar a [mc] la gran noticia, [mad.nick]?"
        mc "¿Qué gran noticia? ¿Me he perdido algo?"
        call BlinkXS3("c27s003_100") from _call_BlinkXS3_535
        mad "Bueno, la iba a contar la próxima vez que fuera a casa..."
        mad "¡Mis diseños de vestidos han sido aceptados para el concurso al que los mandé! ¡Están en la fase final!"
        mc "¡Eso es fantástico, [mad.nick]! ¿Cuándo sabrás si has ganado?"
        call BlinkXS3("c27s003_105") from _call_BlinkXS3_536
        mad "A finales del mes que viene. Tendré que ir a San Francisco un día para la gala de entrega de premios."
        mad "¡Estoy super nerviosa!"
        mc "Me alegro muchísimo por ti."
        call BlinkXS3("c27s003_115") from _call_BlinkXS3_537
        lis "Yo me he pedido acompañarla si le llega una invitación de 'Srta. Chang +1'."
        lis "Yo seré el +1. *Risita* Me encantan las entregas de premios. Sobre todo si gana una amiga."
        call BlinkXS3("c27s003_120") from _call_BlinkXS3_538
        mad "Bueno, aún no sabemos si voy a ganar..."
        mc "Llegar a la final ya es un paso muy importante, reconocen que tienes talento."
        call BlinkXS3("c27s003_065") from _call_BlinkXS3_539
        lis "Bueno, deberíamos volver a casa, ¿no? Tengo ganas de ver las caras de las chicas cuando se enteren de lo de [mad.nick]."
        mc "¿Al final no has comprado nada? No veo bolsas..."
        call BlinkXS3("c27s003_070") from _call_BlinkXS3_540
        lis "Sí que he comprado, pero [mad.nick] lo enviará a casa. No quería ir cargada."
        mc "*Risa* ¿Tanto has comprado?"
        call BlinkXS3("c27s003_075") from _call_BlinkXS3_541
        mad "No lo quieras saber. *Risa* Creo que [lis] se ha convertido en una de mis mejores clientas en estas semanas."
        mc "*Risa* Al final va a tener que echar a [deb.nick] de la habitación para meter toda la ropa."
        call BlinkXS3("c27s003_080") from _call_BlinkXS3_542
        lis "No hace falta echarla. *Risa* Con ocupar sus armarios tengo suficiente."
        lis "¿Nos vamos? [mad.nick] también viene a cenar, ¿verdad?"
        mc "Claro. Le tiene que dar la noticia al resto de la familia."
        call BlinkXS3("c27s003_085") from _call_BlinkXS3_543
        mad "No sé, había sacado comida del congelador para hacerme esta noche..."
        mc "Y va a seguir estando ahí mañana, con lo que evitarás tener que sacarla."
        mc "Mejor estar en casa que sola en tu apartamento, teniendo en cuenta que no está Zeus."
        mc "Además, deberías ser tú quién les cuente a las chicas lo del concurso. Todos sabemos que [lis] no es buena guardando secretos."
        "Puedes oír cómo [lis] se remueve al lado tuyo. No te atreves a mirarla."
        call BlinkXS3("c27s003_090") from _call_BlinkXS3_544
        mad "Me has convencido. Creo que voy a ir con vosotros."
        scene drive_afternoon with fade
        "Conduces a casa mientras las dos chicas empiezan a hablar de lo que se van a poner para la gala de entrega de premios."
        mcp "(¡Por el amor de Dios! ¡Quedan casi dos meses y ya están planificando el vestuario!)"
        stop music fadeout (1.5)
        "Prefieres guardar silencio sobre el tema. Sabes que las dos van a lucir fantásticas lleven lo que lleven."
        scene c27s003_125a with fade
        play music ("music/RhythmPlay.ogg")
        "Al llegar a casa, la noticia de la visita de la madre de [mad.nick] ha corrido como la pólvora."
        "Todo el mundo quiere apoyar a la dependienta."
        scene c27s003_125b with fade
        "No pasa mucho tiempo antes de que [lis] explique la lección que le has dado a la Sra. Chang. Entonces las felicitaciones son para ti."
        "[mee] descubre que su antigua versión se parece más a la Sra. Chang de lo que le gustaría aceptar."
        scene c27s003_125c with fade
        "Cuando empieza la cena, después de llegar los Washington, [mad.nick] da las buenas noticias sobre el concurso."
        "[emm] se siente un poco decepcionada por que [lis] haya pedido la plaza de acompañante. Ni siquiera saben si existe esa plaza."
        scene c27s003_125d with fade
        "Después de cenar, [eri] le propone a [mad.nick] que se quede a dormir en su habitación."
        "Nadie quiere que la chica tenga que volver a su piso vacío."
        "Rápidamente van a ponerse pijamas a juego."
        scene c27s003_125e with fade
        "[oma] estaba esperando para proponerle que fuera a dormir a su apartamento. Ella también va a pasar la noche sola."
        call c27s003_AtHome from _call_c27s003_AtHome
        scene black with dissolve
        stop music fadeout (1.5)
        "Tú duermes solo."
        centered "{size=+20}{b}DÍA 30 – MIÉRCOLES{/b}{/size}"
    return
label c27s003_AtHome:
    if mad._var("route"):
        scene c27s003_125b with fade
        play music ("music/RhythmPlay.ogg")
        "Mientras tanto, en casa..."
        "Durante la cena, [lis] explica el encontronazo que has tenido con la Sra. Chang."
        "[mee] descubre que su antigua versión se parece más a la Sra. Chang de lo que le gustaría aceptar."
        "[emm] se da cuenta por fin de lo afortunada que ha sido al crecer teniendo a alguien como [mar] cerca."
        scene c27s003_125e with fade
        "Después de cenar, [oma] empieza a despedirse de todo el mundo, diciendo que vuelve a su apartamento."
    "[sai] interviene y le ofrece quedarse a dormir en su habitación. [eil] se apunta a dormir con ellas."
    scene c27s003_125f with fade
    "[emm] le sugiere a [eva] que se quede a dormir en la suya, a lo que la pelirroja acepta con una sonrisa radiante."
    "Y [mar] no pierde la oportunidad de proponérselo a [ama], con la excusa de que no debería pasar la noche sola en la base."
    "Ese tipo de rotaciones entre las habitaciones de las chicas se convertirá con el tiempo en una costumbre maravillosa que estrechará aún más los lazos de la familia."
    return
label c27s003_MadLewd:
    if _in_replay:
        $ mad._var("route", True)
        $ mc._var("relationships" , 1 , "set")
        call mrS3_mad_pregnant from _call_mrS3_mad_pregnant_1
        call mrS3_mad_type2 from _call_mrS3_mad_type2_1
        call mrS3_kia_route from _call_mrS3_kia_route_10
        call mrS3_deb_route from _call_mrS3_deb_route_17
        call mrS3_mee_route from _call_mrS3_mee_route_9
        call mrS3_bet_route from _call_mrS3_bet_route_5
        if mar._var("fittingRoom"):
            $ mar._var("route", True)
            $ mc._var("relationships" , 1 , "add")
        if mc._var("relationships")<2:
            call mrS3_rels from _call_mrS3_rels_18
    call BlinkXPS3 ("c27s003_130" , "f") from _call_BlinkXPS3_2786
    mc "¿Quieres que vayamos a cenar a algún sitio?"
    play music ("music/Fragile-Beauty.ogg")
    mad "Me encantaría, pero saqué comida del congelador anoche y, si no la cocino, se va a pasar."
    mad "¿Por qué no vienes a casa y cocino para los dos? No tengo el talento de [mar] o [nor], pero tampoco soy [mee]."
    mc "Me apetece mucho probar tu cocina. ¿Vamos?"
    call BlinkXPS3 ("c27s003_135" , "f") from _call_BlinkXPS3_2787
    "Una vez llegáis al piso de [mad.nick]..."
    mad "Ponte cómodo y sírvete algo de beber. Voy a cambiarme y a quitarme las lentillas."
    mc "Cuando dices cómodo..."
    call BlinkXS3 ("c27s003_140") from _call_BlinkXS3_545
    mad "*Risa* No me refería a que te desnudaras pero, si quieres, no hay ningún problema."
    scene c27s003_140d with dissolve
    mad "Ahorraremos tiempo... después."
    scene c27s003_140e with dissolve
    "Coges a la bella mujer por los hombros, la giras, y le das un apasionado beso."
    call BlinkXS3 ("c27s003_145") from _call_BlinkXS3_546
    mad "No me voy a quejar por recibir besos tuyos... *Risa* Pero ¿a qué ha venido este?"
    mc "A que te vas a cambiar y voy a estar cinco minutos sin verte. Aún no te has ido y ya te echo de menos."
    mc "Además, así tienes una muestra de lo que vendrá... después. *Risa*"
    call BlinkXS3 ("c27s003_150") from _call_BlinkXS3_547
    mad "Pues voy a cambiarme para que ese 'después' llegue pronto."
    mad "Tienes vino en ese armario. Sírvete una copa y otra para mí, por favor. Tinto."
    scene c27s003_150d with dissolve
    mc "No tardes..."
    mad "Intentaré no hacerlo..."
    scene c27s003_150e with dissolve
    "Sirves un par de copas de vino y te sientas a esperar."
    "La broma sobre ponerte cómodo ha estado bien, pero cenar desnudo no entra en tus planes."
    stop music fadeout (1.5)
    scene c27s003_155d with fade:
        yalign 1.0
        linear 5.0 yalign 0.0
    pause (4.5)
    call BlinkXS3 ("c27s003_155") from _call_BlinkXS3_548
    play music ("music/Inspire.ogg")
    mad "¿No ibas a ponerte cómodo?"
    call addProfileImageS3 (14, "maddie_14", mad, _(": 15 - Especial"), "x") from _call_addProfileImageS3_17
    mc "*Risa* Estoy cómodo. Quizás no tanto como tú, pero... *Risa* Tampoco voy a estar tan sexy."
    call BlinkXS3 ("c27s003_160") from _call_BlinkXS3_549
    mad "Eso debería decidirlo yo, ¿no?"
    mad "Aunque para mí estás sexy vestido o desnudo."
    mc "Mientras no me hagas ponerme un delantal... sólo un delantal... *Risa*"
    scene c27s003_165d with fade
    mad "*Risa* No me tientes a utilizarte como porno pinche de cocina."
    mc "¿Qué vas a hacer?"
    call BlinkXS3 ("c27s003_165") from _call_BlinkXS3_550
    mad "Intentar sorprenderte con lo que tengo disponible."
    mc "Me gusta la idea. Aunque ya me has sorprendido con el delantal."
    call BlinkXS3 ("c27s003_170") from _call_BlinkXS3_551
    mad "*Risa* No esperarías que cocinara desnuda, ¿no?"
    mc "*Risa* No, pero tampoco esperaba que cocinaras SÓLO con el delantal."
    scene c27s003_170d with dissolve
    mad "Pues ya somos dos los decepcionados. *Risa* Yo esperaba que llevaras menos ropa que yo a estas alturas."
    mc "¿Quién ha dicho que esté decepcionado? *Risa* ¿De verdad quieres que me quite la ropa?"
    call BlinkXS3 ("c27s003_175") from _call_BlinkXS3_552
    mad "Quedaría un poco raro si yo ceno desnuda y tú vestido, ¿no?"
    if mad._var("sub"):
        mad "Quizás cuando me usabas como esclava... pero ya no. Ahora somos una pareja normal."
    elif mad._var("dom"):
        mad "Si hubiéramos seguido con lo de ser tu ama, quizás hubiera sido al revés, pero ya no. Ahora somos una pareja normal."
    else:
        mad "Tan sólo somos una pareja normal que no tiene que rendir cuentas a nadie sobre la ropa que lleva para cenar, ¿no?"
    mc "Me gusta lo de 'pareja normal'. Tan solo una pareja normal que va a cenar desnuda."
    call BlinkXS3 ("c27s003_180") from _call_BlinkXS3_553
    "Te empiezas a quitar la ropa, sin separar tu mirada de los ojos de [mad.nick]." id c27s003_MadLewd_4003d1f0
    mad "Y a mí me gusta que me malcríes y que me des este tipo de caprichos."
    mc "Este tipo y cualquier otro capricho que tengas. Es mi función como tu pareja, ¿no?"
    mc "¿Te ayudo a algo?"
    mad "No hace falta. Seguramente nos estorbaríamos."
    scene c27s003_180An with dissolve
    "Ver a [mad.nick] moverse por la minúscula cocina del apartamento es fascinante."
    "Reír con ella mientras lo hace es maravilloso. Realmente parecéis una pareja normal."
    "Si no fuera porque te sientes un poco inútil por no poder ayudarla."
    call BlinkXPS3 ("c27s003_185" , "f") from _call_BlinkXPS3_2788
    mad "Ya está. Unos minutos de horno y estará listo."
    if persistent.family:
        mc "Tenía una pinta estupenda. Si está tan bueno como parece, creo que le tendrás que dar la receta a mi madre."
    else:
        mc "Tenía una pinta estupenda. Si está tan bueno como parece, creo que le tendrás que dar la receta a [mar]."
    mad "*Risa* Seguro que ella sería capaz de mejorarla y dejarme a la altura del betún. Ella podría ganar algún premio con mi receta, es una cocinera excelente."
    call BlinkXS3 ("c27s003_190") from _call_BlinkXS3_554
    mad "Ummm... ¿Qué tal es tu memoria espacial?"
    mc "*Risa* No recuerdo haber estado nunca en el espacio."
    call BlinkXS3 ("c27s003_195") from _call_BlinkXS3_555
    mad "¡Idiota! *Risa* No me refiero a eso. ¿Eres capaz de detectar cosas que han cambiado de sitio o que son más grandes o más pequeñas que la última vez que las viste?"
    mc "Ummm... No sé... No te has cortado el pelo, ¿verdad?"
    mad "*Risa* No."
    scene c27s003_195d with dissolve
    "Deja el delantal en la cocina y se dirige a su habitación, vestida sólo con las gafas. La sigues hipnotizado con la mirada."
    mad "Ven a mi habitación a ver si descubres qué ha cambiado."
    mc "La última vez que entraste ahí, no te veía el culo. *Risa* Ese es un buen cambio."
    mad "*Risa* ¡Idiota!"
    call BlinkXPS3 ("c27s003_200" , "f") from _call_BlinkXPS3_2789
    mad "A ver si eres capaz de descubrir qué es diferente de la última vez que estuviste aquí."
    mc "Es fácil. No está el cuadro de Zeus que estabas pintando."
    mad "Bien. Pero hay otra cosa más que también falta."
    mc "Ummm... ¿tus diseños de vestidos?"
    call BlinkXS3 ("c27s003_205") from _call_BlinkXS3_556
    mad "¡Sí! ¡Los han aceptado en el concurso y estoy en la fase final!"
    mc "¡Eso es genial, [mad.nick]! ¡Felicidades! ¿Cuándo te dirán si has ganado?"
    call BlinkXS3 ("c27s003_210") from _call_BlinkXS3_557
    mad "A finales de septiembre. Tengo que ir a una gala en San Francisco para saber si he ganado."
    mc "Me hubiera encantado acompañarte, pero estaré en Aruba en septiembre..."
    call BlinkXS3 ("c27s003_215") from _call_BlinkXS3_558
    mad "Lo sé. No te preocupes. Si gano habrá más galas, y si pierdo, no querrás estar a mi alrededor."
    mad "Me puedo poner muy gruñona cuando algo no sale como quiero."
    mc "Pero yo podría ayudarte a cambiar el estado de ánimo si te pones gruñona."
    call BlinkXS3 ("c27s003_220") from _call_BlinkXS3_559
    stop music fadeout (1.5)
    mad "¿Ah, sí? ¿Y cómo lo harías?"
    scene c27s003_220d with dissolve
    play music ("music/KindofGirl.ogg")
    mc "Lo primero sería darte un abrazo para consolarte. Sabes que abrazar se me da muy bien."
    mad "Creo que eso disminuiría mucho mi mal humor. Pero no lo haría desaparecer del todo."
    mc "Además quería abrazarte para felicitarte, pero como no te callas..."
    scene c27s003_220e with dissolve
    "Besas tiernamente a la preciosa mujer. Se estremece entre tus brazos como si fuera vuestro primer beso."
    if mad._var("dom") or mad._var("sub"):
        "La última vez que estuvisteis en esta habitación las cosas eran diferentes entre vosotros."
    "El beso se va volviendo más apasionado tal como pasan los segundos."
    "Si no fuera porque la comida estará lista en breve, la tumbarías en la cama ahora mismo."
    call BlinkXS3 ("c27s003_225") from _call_BlinkXS3_560
    mc "Lo siguiente sería besarte. Creo que eso ayudaría a rebajar tu mal humor."
    mad "*Respiración entrecortada* Creo que eso lo haría desaparecer por completo. No me quedaría aliento para gruñir."
    scene c27s003_225d with dissolve
    mad "Además, me daría la sensación de que me estás atracando, con ese cañón apoyado en mi estómago."
    mc "Llevo más de media hora mirándote cocinar sólo con un delantal. ¿Cómo creías que estaría?"
    scene c27s003_225e with dissolve
    mad "*Smooch* Suponía que estarías tan cachondo como lo estaba yo mientras sentía tu mirada recorriendo cada una de mis curvas."
    mc "No te equivocas... pero... ¿la comida?"
    scene c27s003_225f with dissolve
    mad "*Smooch* Le quedan unos minutos todavía. Y el horno se parará solo. *Smooch* ¿Vas a durar más de lo que tarda la comida en hacerse?"
    mc "Si sigues así, no. *Risa*"
    call BlinkXS3 ("c27s003_230") from _call_BlinkXS3_561
    mad "Entonces déjame ser una buena esposa y hacer algo por mi marido después de un duro día de trabajo."
    if mc._var("relationships")>1:
        mcp "(Esposa y marido. Es una bonita idea. Irreal, pero bonita.)"
    else:
        mcp "(Esposa y marido. Es una bonita idea.)"
    mc "*Risa* Te dejo hacerlo. Si alguna vez digo que no a eso, pídele a [ama] que me pegue un tiro."
    mc "Pero no he trabajado demasiado hoy."
    scene c27s003_230d with dissolve
    mad "*Risa* No he dicho que hayas sido tú el que ha tenido un duro día de trabajo."
    scene c27s003_920pv with dissolve
    show c27s003_920v
    "Se mete a Mjolnir en la boca sin dejarte responder, empezando una profunda mamada."
    "Si esta va a ser tu recompensa cada vez que tiene un día duro en el trabajo... se te pasa por la cabeza la Sra. Chang yendo todos los días a la tienda."
    mad "*Jadeo dubitativo*"
    "Pero algo parece no estar funcionando bien ahí abajo. [mad.nick] no parece cómoda por alguna razón."
    "Pese a que su mamada sin manos es tremenda, puedes notar que no lo está disfrutando tanto como tú."
    mc "¿Pasa algo, [mad.nick]?"
    call BlinkXS3 ("c27s003_235") from _call_BlinkXS3_562
    mad "No sé... hay algo incómodo con mi coleta..."
    scene c27s003_240AnBlink
    mad "Ya está. Hacer una mamada es como diseñar vestidos; hasta que no te haces un moño, no lo das todo. Mucho mejor así." #Giving a blow job is like designing dresses; until you don't make it into a bun, you haven't given it your all. Much better that way.
    mc "*Risa* No sé si servirá de algo, pero estás monísima con ese moño."
    call BlinkXS3 ("c27s003_245") from _call_BlinkXS3_563
    mad "*Risa* ¿Sólo con el moño?"
    mc "*Risa* Estás monísima lleves el pelo como lo lleves."
    mad "*Risa* Mejor. Ahora que me he acostumbrado a la coleta, me encanta y no voy a llevar el moño si no estoy diseñando vestidos."
    mad "O haciendo esto."
    scene c27s003_925pv with dissolve
    show c27s003_925v
    hide c27s003_920v
    "[mad.nick] reanuda su mamada con una energía diferente. Una vez la coleta deja de molestarle, es incluso más sublime que antes."
    "Su técnica sin manos es de las mejores que has probado nunca. Haciendo la presión justa con sus labios durante todo el trayecto."
    mad "*Jadeo afirmativo*"
    "Definitivamente más cómoda con el moño de lo que estaba con la coleta, la chica juguetea con su lengua alrededor de tu astil."
    "Sus movimientos son tan profundos que apenas puede jugar con la punta, que roza su úvula cada vez que llega al fondo del recorrido."
    scene c27s003_930pv with dissolve
    show c27s003_930v
    hide c27s003_925v
    if mad._var("dom"):
        "Parece imposible que sólo hace unos días fuera dominante contigo y ahora la tengas de rodillas a tus pies."
    elif mad._var("sub"):
        "Tenerla de rodillas a tus pies te recuerda cómo era vuestra relación hace sólo unos días, cuando era sumisa. Por suerte, eso ha quedado atrás."
    "Algunos tipos ven en las mamadas de rodillas un símbolo de sumisión. No es lo que está pasando aquí. Esto es fruto del amor."
    if mar._var("fittingRoom"):
        "Una relación que empezó de una forma extraña, pero que ha ido creciendo y evolucionando con el tiempo."
    else:
        "Una relación que encontraste donde no podías esperar, comprando un disfraz y viendo una vieja película."
    mad "*Gemido*"
    "El cambio de jadeos a gemidos te indica que la diseñadora se está empezando a poner tan cachonda como lo estás tú."
    "Quizás un cambio de posición sería bueno ahora mismo."
    scene c27s003_935pv
    scene c27s003_940pv
    $ renpy.movie_cutscene("c27/c27s003_935vid.webm")
    "No es lo que tenías en mente cuando has pensado en un cambio de posición, pero la dependienta mueve sus manos de sus muslos a tu culo."
    "La chica hace una pausa para ajustarse a la nueva posición antes de continuar con sus alucinantes movimientos."
    mad "*Gemido afirmativo*"
    "Su mamada era perfecta antes. Ahora que tiene sus manos para ayudarle a marcar el ritmo, puede superar la perfección."
    scene c27s003_940pv with dissolve
    show c27s003_940v
    hide c27s003_930v
    "Y la perfección queda superada. Sus suaves movimientos, que a su vez te obligan a mover tus caderas, son sublimes."
    "Como cuando suena una canción y no puedes evitar seguir el ritmo con el pie, tus caderas no pueden evitar seguir el ritmo de su cabeza y de sus manos."
    mad "*Gemido*"
    "No hay duda de que la mejor canción del mundo perdería en una competición con [mad.nick]."
    "Empiezas a pensar que, si sigue así, va a cenar antes que tú, pero no lo que hay en el horno."
    scene c27s003_945pv with dissolve
    show c27s003_945v
    hide c27s003_940v
    "Su respiración empieza a agitarse, produciendo que tu glande vibre al fondo de su boca con cada aliento que toma."
    "Si sigue así, no vas a poder durar mucho más. No quieres que esto acabe así. Al menos no todavía."
    mad "*Gemido inquisitivo*"
    "Algo en tu lenguaje corporal debe haber alertado a la diseñadora de tus dudas."
    "Vuestra compenetración y cómo os empezáis a conocer en vuestra tercera vez juntos empieza a ser increíble. Parece que llevéis años juntos."
    mc "Para un momento, [mad.nick], por favor."
    call BlinkXS3 ("c27s003_250") from _call_BlinkXS3_564
    mad "*Gemido* ¿A punto de correrte ya?"
    mc "No, pero acercándome rápidamente. Y no quiero que empieces a cenar sin mí."
    mc "Ese gemido me dice que tú también te estás poniendo cachonda."
    call BlinkXS3 ("c27s003_255") from _call_BlinkXS3_565
    mad "¿Cachonda? Creo que no he estado tan cachonda en mi vida."
    mc "Entonces vamos a la cama. No quiero ser el único que acabe antes de cenar."
    scene c27s003_255d with dissolve
    mad "A veces tienes unas ideas excelentes."
    mc "*Risa* ¿Como empezar a salir contigo, por ejemplo?"
    call BlinkXS3 ("c27s003_260") from _call_BlinkXS3_566
    if mad._var("sub"):
        mad "Como darle la vuelta a mi chantaje para que después se convirtiera en esto. Seguramente no estaríamos aquí si no lo hubieras hecho."
    elif mar._var("fittingRoom") and not mad._var("dom"):
        mad "Como perdonar mi intento de chantaje para que se convirtiera en esto. Seguramente no estaríamos aquí si no lo hubieras hecho."
    elif mad._var("dom"):
        mad "Como aceptar mi chantaje para que después se convirtiera en esto. Seguramente no estaríamos aquí si no lo hubieras hecho."
    else:
        mad "Como aceptar la invitación de una desconocida para ver una peli. Seguramente no estaríamos aquí si no lo hubieras hecho."
    mad "*Risa* Pero sí, empezar a salir conmigo es una de tus mejores ideas. Al menos desde mi punto de vista."
    mc "*Risa* También desde el mío. No hay ningún otro lugar en el que querría estar ahora mismo."
    call BlinkXS3 ("c27s003_265") from _call_BlinkXS3_567
    mad "*Risita* Pues espero que cambies de opinión. Yo quiero que estés dentro de mí."
    mc "*Risa* Bueno, mi afirmación anterior puede tener pequeños matices."
    scene c27s003_910pv with dissolve
    show c27s003_910v
    hide c27s003_945v
    "Los dos estáis tan cachondos que no son necesarios más juegos previos. Seguramente acabarías corriéndote si lo hicierais."
    mad "*Gemido* ¡Sí! *Jadeo* ¡Cómo he echado de menos esto! *Gemido*"
    "Volver a estar dentro del apretado coño de [mad.nick] se siente increíble. Está tan húmeda como sus gemidos te han hecho pensar."
    mad "*Jadeo* ¡Fóllame más duro! *Gemido*"
    "Pese a que la dependienta está muy cachonda, no ha tenido ninguna estimulación física en su coño durante la mamada."
    scene c27s003_900pv with dissolve
    show c27s003_900v
    hide c27s003_910v
    "Es algo que puedes solucionar y lo haces. Aceleras el ritmo de tu bombeo, devastando su coño a con cada nuevo empuje de tus caderas."
    "Su túnel se cierra con fuerza sobre tu polla, tan estrecho como siempre. Más húmedo que nunca."
    mad "*GEMIDO* ¡Sí, así! *JADEO* ¡Ese ritmo es alucinante! *GEMIDO*"
    "Mjolnir choca con su cérvix al final de cada una embestidas, martilleando el final de su túnel del amor."
    "Ninguno de los dos pensáis en ser delicados en ese momento. A ninguno de los dos os importa tener un poco de sexo más duro del habitual."
    scene c27s003_905pv with dissolve
    show c27s003_905v
    hide c27s003_900v
    "Han pasado muchos días desde la última vez que estuvisteis juntos y vuestros cuerpos reclaman recuperar el tiempo perdido."
    mad "*JADEO* ¡Si sigues así voy a correrme en seguida1 *GEMIDO* ¡No pares! *JADEO*" id c27s003_MadLewd_872405fc
    "Tú también te estás acercando, debido al tiempo de separación y a lo cachondo que te ha dejado la mamada."
    mad "*GEMIDO* ¡SIGUE ASÍ! *JADEO* ¡ESTOY A PUNTO! *GEMIDO*"
    "Pese a la ventaja con la que partías, parece que vas a perder la carrera por llegar primero al orgasmo. Estás contento por ello."
    call OrgasmXS3 ("c27s003_270") from _call_OrgasmXS3_72
    mad "*JADEO* ¡ME CORROOOO! *GEMIDO*"
    "La preciosa asiática se tensa hasta que parece que se va a romper para relajar todos sus músculos en una explosión de placer."
    "No hay momento en que esté más preciosa que cuando el placer recorre su cuerpo."
    scene c27s003_915pv with dissolve
    show c27s003_915v
    hide c27s003_905v
    "Continúas bombeando con tus caderas, recorriendo con tu mirada su cuerpo al mismo ritmo que las oleadas de placer recorren su vagina."
    "Es un acto animal, en el que buscas que tu orgasmo se una al suyo en una explosión conjunta de placer."
    mad "*GEMIDO* ¡POR ZEUS! *JADEO* ¡NO PARES! *GEMIDO*"
    "Pero también es un acto generoso, en el que intentas prolongar el placer de la muchacha lo máximo posible."
    "Tus continuas embestidas provocan orgasmo tras orgasmo en su precioso cuerpo. Pero el tuyo llama a la puerta con fuerza."
    if persistent.pregnancy and not mad._var("pregnant"):
        if persistent.walkthrough:
            $ wt1 = _("[mad.nick] embarazada.")
            $ wt2 = _("Sin consecuencias.")
        else:
            $ wt1 = ""
            $ wt2 = ""
        menu:
            "Correrte dentro. Ir a por el bebé." (wt = wt1):
                $ mad._var("pregnant", True)
                $ mad._var("undiscoveredPregnancy", True)
                play sound ("music/OldMusicBox5.ogg")
            "Correrte dentro." (wt = wt2):
                pass
    $ resetWalkthrough ()
    call OrgasmXS3 ("c27s003_275") from _call_OrgasmXS3_73
    hide c27s003_915v
    mc "¡Mpfft!"
    "Tu orgasmo deja de llamar y derriba la puerta de una patada. Descargas una cantidad ingente de tu semilla dentro de [mad.nick]."
    mad "*JADEO* ¡SÍ! *GEMIDO* ¡LLÉNAME! *JADEO*"
    "Cumples sus órdenes sin poder evitarlo. La llenas hasta que tu semen rebosa del estrecho y convulsionante coño de la dependienta."
    call BlinkXPS3 ("c27s003_280" , "f") from _call_BlinkXPS3_2790
    "Al cabo de un rato, cuando vuestra respiración se normaliza..."
    mc "¿Te ha gustado? ¿No he sido demasiado duro?"
    mad "¡Ha sido uno de los mejores polvos que hemos echado nunca!"
    mad "¡Me encanta este rollo como si fuéramos un matrimonio y me pone super cachonda!"
    mc "Bueno, lo somos en cierto modo. Pero entiendo lo que dices."
    call BlinkXS3 ("c27s003_285") from _call_BlinkXS3_568
    mad "Me he empezado a poner cachonda cuando estaba cocinando para ti..."
    mc "Para nosotros..."
    mad "Bueno, sí, para nosotros. Como un todo."
    call BlinkXS3 ("c27s003_290") from _call_BlinkXS3_569
    mad "Es como... no sé... las sitcoms de los 50 y los 60 en las que el marido vuelve del trabajo y la esposa está con la cena casi preparada."
    mc "*Risa* No puedo imaginarme a Lucy o a Samantha cocinando sólo con el delantal."
    mc "*Risa* O haciéndose un moño porque les molesta la coleta para hacerles una mamada a Ricky o a Darrin."
    stop music fadeout (1.5)
    call BlinkXS3 ("c27s003_295") from _call_BlinkXS3_570
    mad "*Risa* Samantha podría. Lucy llevaba el pelo demasiado corto."
    play sound ("music/OvenBell.ogg")
    "Horno" "*Ding*"
    stop sound
    play music ("music/Fragile-Beauty.ogg")
    mad "*Risa* Justo a tiempo. Salvados por la Campana de un segundo round."
    mad "Voy a lavarme las manos en la cocina. Tienes el lavabo a tu disposición para lavarte."
    mc "Sí, Mami. *Risa* Voy a lavarme las manos antes de cenar."
    call BlinkXPS3 ("c27s003_300" , "f") from _call_BlinkXPS3_2791
    "Después de pasar por el lavabo..."
    mad "La cena está lista. Espero que te guste."
    mc "Estoy seguro de que me gustará. Huele genial."
    call BlinkXPS3 ("c27s003_305" , "f") from _call_BlinkXPS3_2792
    mc "¡Está buenísimo! ¿Qué ingredientes lleva?"
    mad "*Risa* ¿Vas a cocinarlo alguna vez?"
    mc "*Risa* No..."
    mad "*Risa* Entonces, en vez de decirte qué lleva o darte la receta, dejaré que lo adivines."
    call BlinkXS3 ("c27s003_310") from _call_BlinkXS3_571
    mad "Aunque estabas justo ahí mientras yo estaba ahí atrás preparándolo..."
    mc "¿Realmente crees que podía mirar qué estabas cocinando mientras paseabas el culo por delante de mis ojos?"
    mc "Podrías haber metido un elefante en el horno y ni siquiera me hubiera dado cuenta."
    call BlinkXS3 ("c27s003_315") from _call_BlinkXS3_572
    mad "*Risa* Más razones para no darte la receta."
    mc "*Risa* ¿Qué he dicho ahora?"
    call BlinkXS3 ("c27s003_320") from _call_BlinkXS3_573
    mad "Si no detectarías un elefante porque tenía el culo al aire, no recordarás la receta si te la doy ahora porque tengo las tetas desnudas. *Risa*"
    mad "*Risa nerviosa* [kat] dice que tengo mejores tetas que culo. No sé qué opinas tú al respecto."
    mc "Ummm... Difícil elección. ¿Perfección superior o perfección inferior?"
    mc "Ambos. Ambos está bien." #Both. Both is good.
    mc "Pero tienes razón. No recordaría la receta con esas dos cosas preciosas apuntando en mi dirección."
    call BlinkXS3 ("c27s003_325") from _call_BlinkXS3_574
    mad "*Risa* Con lo que eres más de tetas que de culos."
    mc "*Risa* ¿Por quién me has tomado? ¡Me refería a tus ojos! Flipé con ellos la primera vez que los vi, y lo sigo haciendo."
    call BlinkXS3 ("c27s003_330") from _call_BlinkXS3_575
    mad "¡Maldición, [mc]! ¡Yo estaba intentando llevar la conversación a algo sexy y tú intentas ruborizarme!"
    mc "Bueno, tienes unos ojos muy sexys. Y más aún desde que los enmarcas con las gafas."
    mc "Creo que no hay nada en ti que no sea sexy."
    scene c27s003_330An with dissolve
    "La cena transcurre entre risas y bromas. El nivel de ingenio de las bromas va subiendo."
    "Bromeáis sobre muchas cosas, saltando de un tema a otro en un remolino de conversaciones."
    mcp "(Si no fuera por lo de cenar desnudos, realmente podría estar en una vieja sitcom con Mi Bella Dependienta.)" #I could dream of Maddie
    stop music fadeout (1.5)
    call c27s003_AtHome from _call_c27s003_AtHome_1
    scene c27s003_335d with fade
    play music ("music/Fragile-Beauty.ogg")
    "Después de cenar y recoger la cocina, en el apartamento de [mad.nick]..."
    mad "Tenemos una película que acabar. ¿Te apetece?"
    mc "Estaría bien. Es pronto para ir a dormir, ¿no?"
    call BlinkXS3 ("c27s003_335") from _call_BlinkXS3_576
    mad "¿A qué hora te tienes que ir?"
    mc "Por la mañana, después de desayunar."
    call BlinkXPS3 ("c27s003_340" , "h") from _call_BlinkXPS3_2793
    mad "¿Qué? ¿Quieres quedarte a dormir?"
    mc "Sólo si me dejas quedarme. Hoy no está Zeus y..."
    scene c27s003_340d with vpunch
    "La preciosa mujer se lanza a tus labios con una pasión desenfrenada y sorprendente."
    "Te lo tomas como que te va a dejar quedarte."
    call BlinkXS3 ("c27s003_345") from _call_BlinkXS3_577
    mad "¡Sí! ¡Claro que puedes quedarte! ¡Estaba a punto de proponértelo yo! ¡Nunca hemos dormido juntos!"
    mc "Sabes que puedes quedarte a dormir en mi casa cuando quieras, ¿verdad?"
    call BlinkXS3 ("c27s003_350") from _call_BlinkXS3_578
    mad "Lo sé, pero eso significaría que después me tienes que llevar a la tienda, y no quiero que te molestes o que tengas que madrugar."
    mad "Suficiente haces por todas nosotras llevándonos arriba y abajo."
    mc "No sería ninguna molestia, te lo aseguro."
    call BlinkXS3 ("c27s003_355") from _call_BlinkXS3_579
    mad "De todas formas, aunque parezca una tontería, prefiero que te quedes tú aquí a quedarme yo allí."
    mc "¿Por qué? ¿Qué diferencia ves?"
    call BlinkXS3 ("c27s003_360") from _call_BlinkXS3_580
    mad "Ya te he dicho que es una tontería, pero... esta noche me está haciendo pensar cómo podría ser nuestra vida si fuéramos un matrimonio."
    if mc._var("relationships")>1:
        mad "Ya sé que es imposible porque somos una Extraña Pareja, pero..." #An Odd Couple
    mc "¿Tienes papel y bolígrafo?"
    call BlinkXS3 ("c27s003_365") from _call_BlinkXS3_581
    mad "Sí, al lado del ordenador... ¿Por qué?"
    mc "Dame un segundo."
    scene c27s003_365d with fade
    "Te diriges al escritorio y coges un post-it."
    "Al contrario que en el caso de [mad.nick], la faceta artística no está entre tus mejores cualidades."
    "Gastas un par de post-its hasta que consigues lo que se parece a lo que quieres dibujar."
    scene c27s003_365e with fade
    "[mad.nick] te mira perpleja durante todo el proceso."
    call BlinkXPS3 ("c27s003_370" , "f") from _call_BlinkXPS3_2794
    "Vuelves al lado de la expectante muchacha y le das el post-it boca abajo."
    mc "Toma. No hace falta que contestes ahora mismo."
    mad "¿Qué has hecho?"
    mc "Léelo."
    scene c27s003_370d with hpunch
    mad "¿QUÉ?"
    scene c27s003_370e with vpunch
    mad "¡SÍ!"
    scene c27s003_370f with hpunch
    "Si el beso de antes era apasionado, este lo supera. No habías visto a [mad.nick] tan contenta nunca."
    "Un post-it puede ser poderoso."
    scene c27s003_370g with dissolve
    "Especialmente si en él pone '¿Quieres casarte conmigo?'"
    "'Este post-it se puede cambiar por un anillo de compromiso'"
    "El anillo te ha quedado horrible. Dibujar un círculo es más complicado de lo que parece. Pero te da lo mismo."
    "Y volver a por tus pantalones para buscar una moneda para hacer el círculo perfecto le hubiera quitado algo de misterio al proceso."
    call BlinkXS3 ("c27s003_375") from _call_BlinkXS3_582
    mad "¡No me esperaba algo así!"
    mc "Bueno, llevamos toda la noche hablando de sitcoms sobre parejas, con lo que he pensado que era lo adecuado."
    call BlinkXS3 ("c27s003_380") from _call_BlinkXS3_583
    if mc._var("relationships")>1:
        mad "Sé que es imposible que nos casemos, pero me hace mucha ilusión que me lo hayas pedido."
        mc "Bueno, no nos podemos casar oficialmente, pero..."
        call BlinkXPS3 ("c27s003_385" , "h") from _call_BlinkXPS3_2795
        mad "¡Por Zeus! ¡Eres un puto genio!"
        mc "¿Por qué? ¿Qué he hecho yo ahora?"
        mad "Has resuelto un problema sin saber ni siquiera que existía."
        mc "¿Qué problema?"
        mad "No te lo puedo decir, al menos no aún."
        mc "Puedo esperar a que estés preparada para contármelo, no hay ningún problema."
        call BlinkXS3 ("c27s003_390") from _call_BlinkXS3_584
        mad "Y sobre lo de que no nos podamos casar oficialmente, es sólo un papel. No voy a sentirme menos casada contigo por no firmarlo."
    else:
        mad "No puedes imaginarte la ilusión que me ha hecho que me lo pidas."
    mad "Hay muchas cosas que planear a partir de ahora."
    if bet._var("route") or mee._var("route"):
        mad "{i}(Tengo que hablar con Las Chicas de Oro mañana, antes de que se vayan a Florida.){/i}" #The Golden Girls
    mc "*Risa* No te preocupes, [mad.nick]. Vamos Día a Día." #One Day at A time
    mc "¿Ponemos esa película a ver si la acabamos?"
    scene c27s003_390d with dissolve
    mad "No. Quiero hacer el amor con mi prometido por primera vez. Habrá tiempo para ver la película después."
    stop music fadeout (1.5)
    if mc._var("relationships")>1:
        mc "*Risa* Y después dices que el puto genio soy yo."
    else:
        mc "*Risa* Creo que me voy a casar con un genio."
    scene c27s003_395a with fade
    play music ("music/KindofGirl.ogg")
    "Nada más entrar en la habitación, [mad.nick] te besa dulcemente."
    "Hay algo diferente en este beso. Más seguridad. El post-it le ha demostrado que vais a pasar el resto de vuestras vidas juntos."
    scene c27s003_395b with dissolve
    "Un simple post-it se ha convertido en un acto inesperado que le ha dado a vuestra relación un giro especial."
    "Sin decir una palabra, la chica te va guiando hacia la cama. Es imposible decir ninguna palabra cuando vuestras bocas están ocupadas."
    scene c27s003_395An with dissolve
    "Los besos se mueven a la cama, donde vuestras bocas y vuestros cuerpos no tienen suficiente con un solo beso."
    "Vuestras lenguas se entrelazan en un sensual baile para dos. Vuestras manos recorren el cuerpo del otro, que tan bien conocen."
    "Vuestras respiraciones se mezclan en un aliento compartido."
    call BlinkXS3 ("c27s003_400") from _call_BlinkXS3_585
    "Para cuando el largo beso acaba, Mjolnir está en orden de batalla."
    mad "¿Preparado? No puedo esperar más a sentirte dentro."
    mc "Cuando quieras. No puedo esperar más a estar dentro de ti."
    scene c27s003_400An with fade
    "Sin pensárselo dos veces se da la vuelta y se empala en Mjolnir."
    mad "*Gemido* ¡Ooof! *Jadeo*"
    "Ver su precioso cuerpo descendiendo por tu astil es una visión de la que nunca te cansarás en las próximas décadas."
    call BlinkXS3 ("c27s003_405") from _call_BlinkXS3_586
    mad "No hace ni dos horas que te tenía dentro y ya echaba de menos esto."
    "Te lo has pasado tan bien durante la cena y el rato en el sofá, que no eres consciente de que hayan pasado dos horas."
    mc "Hace dos horas te acostaste con tu novio. *Risa* Ahora te acuestas con tu prometido."
    call BlinkXS3 ("c27s003_410") from _call_BlinkXS3_587
    mad "*Risita* Entonces es como si fuera nuestra primera vez de nuevo."
    mc "Me encantan las primeras veces."
    scene c27s003_965pv with dissolve
    show c27s003_965v
    "A ella también le encantan. Empieza una lenta cabalgada sobre Mjolnir, intentando mirarte sin parecer un búho."
    "El placer que le está provocando la cabalgata se refleja claramente en su rostro."
    mad "*Gemido* Podría pasarme horas haciendo esto... *Jadeo*"
    mcp "(Lo dudo...)"
    "Sabes que [mad.nick] no se caracteriza por su resistencia. Es capaz de resistir varios asaltos, pero no hacer que éstos sean muy largos."
    "Y un post-it abandonado en el salón no va a cambiar eso."
    scene c27s003_955pv with dissolve
    show c27s003_955v
    hide c27s003_965v
    "Su lenta cabalgata no tiene la urgencia del polvo anterior. Busca maximizar tanto tu placer como el suyo, sin prisas."
    mad "*Jadeo* ¡Es fantástico! *Gemido*"
    "Su coño, tan estrecho como siempre pese a que hace dos horas lo estabas embistiendo, abraza con fuerza a Mjolnir cada vez que ella se desliza arriba y abajo."
    "Aún no lo sabes, pero esa estrechez se mantendrá casi intacta durante décadas."
    if mad._var("pregnant"):
        "Ni siquiera dar a luz hará que pierda mucha de esa flexibilidad que adoras."
    mad "*Gemido* Me encanta este ritmo... *Jadeo* Puedo notar cómo tocas en todos mis sitios correctos... *Gemido*"
    scene c27s003_960pv with dissolve
    show c27s003_960v
    hide c27s003_965v
    "También tú notas como ella roza en cada uno de los tuyos, ya sea durante el recorrido, o cuando lo finaliza rozando tu punta con la boca de su útero."
    "Si además a todo ello le sumas las increíbles vistas, no puedes evitar que tu orgasmo se acerque poco a poco."
    mad "*Jadeo* No voy a aguantar mucho más. *Gemido*"
    "Lo has pensado hace un momento. A [mad.nick] le cuesta mantener el ritmo en largas cabalgatas, cuando ella tiene que hacer la mayoría del trabajo."
    mc "¿Quieres que cambiemos de posición?"
    "No te queda mucho para llegar, pero si ella va a empezar a perder las fuerzas, un cambio de posición sería idóneo."
    scene c27s003_950pv with dissolve
    show c27s003_950v
    hide c27s003_960v
    mad "*GEMIDO* ¡NO! *JADEO* Me refiero a que... *GEMIDO* me voy a correr... *JADEO*"
    "Para tu sorpresa, y sin perder el ritmo, empieza a apretar sus músculos vaginales antes de llegar al orgasmo."
    if deb._var("route"):
        "Adoras las lecciones que [meg] les está dando a las chicas."
    "El aumento de presión hace que tu orgasmo llame a las puertas con fuerza."
    mad "*JADEO* ¡CÓRRETE DENTRO! *GEMIDO* ¡QUIERO RECIBIR LA PRIMERA DESCARGA DE MI FUTURO MARIDO! *JADEO*"
    "Esta chica definitivamente tiene un fetiche con el matrimonio."
    if persistent.pregnancy and not mad._var("pregnant"):
        if persistent.walkthrough:
            $ wt1 = _("[mad.nick] embarazada.")
            $ wt2 = _("Sin consecuencias.")
        else:
            $ wt1 = ""
            $ wt2 = ""
        menu:
            "Correrte dentro. Ir a por el bebé." (wt = wt1):
                $ mad._var("pregnant", True)
                $ mad._var("undiscoveredPregnancy", True)
                play sound ("music/OldMusicBox5.ogg")
            "Correrte dentro." (wt = wt2):
                pass
    $ resetWalkthrough ()
    call OrgasmXS3 ("c27s003_415") from _call_OrgasmXS3_74
    hide c27s003_950v
    mad "*GEMIDO* ¡SÍ! *JADEO* ¡TE QUIERO! *GEMIDO*"
    mc "¡Mpfft!"
    "Tu orgasmo y el de [mad.nick] llegan casi a la vez. Sus primeras contracciones provocando que no puedas aguantar más."
    "Tu explosión la vuelve a llenar, mezclando tu semilla con sus fluidos."
    call BlinkXPS3 ("c27s003_420" , "f") from _call_BlinkXPS3_2796
    "Cuando su orgasmo finaliza, mucho más tarde que el tuyo, se derrumba sobre tu pecho."
    mad "*Respiración entrecortada* Ha sido increíble."
    stop music fadeout (1.5)
    mc "*Risa* Estoy de acuerdo, pero creo que tienes un fetiche con el matrimonio."
    play music ("music/Beautiful-Day-Vocals.ogg")
    call BlinkXS3 ("c27s003_425") from _call_BlinkXS3_588
    "Se baja de encima tuyo y se tumba a tu lado."
    if mar._var("fittingRoom"):
        mad "No es eso... Tal como empezamos tú y yo, con el chantaje, nunca pensé que algún día pudiéramos estar prometidos."
    else:
        mad "No es eso... Cuando te invité a casa por primera vez, no pensé que algún día pudiéramos estar prometidos."
    mad "Ni siquiera entraba en mis planes enamorarme de ti."
    mc "*Risa* Pues me alegra que hayas cambiado de planes."
    call BlinkXS3 ("c27s003_430") from _call_BlinkXS3_589
    mad "*Risa* ¿Quién ha dicho que haya cambiado de planes o que me haya enamorado de ti?"
    mad "*Risa* Me he prometido contigo por tus millones y porque follas de puta madre."
    mc "*Risa* Sabes que puedo salir corriendo y romper el post-it, ¿verdad?"
    scene c27s003_430d with vpunch
    mad "*Risa* ¡No si salgo corriendo yo primero! ¡Voy a esconderlo hasta el momento de cambiarlo por un anillo real!"
    mc "*Risa* Ve poniendo la película mientras voy al lavabo."
    call BlinkXS3 ("c27s003_435") from _call_BlinkXS3_590
    mad "¿De verdad quieres ver la película?"
    mc "¿No quieres la experiencia completa de matrimonio? Acabar el día viendo una peli se parece bastante, ¿no?"
    mc "Esposa cocinando, sexo, cena, conversación, sexo, peli, y dormir... ¿No te apetece?"
    scene c27s003_440a with hpunch
    mad "¡Sí!"
    scene c27s003_440b with dissolve
    "Y tras eso, desaparece como una exhalación."
    "Sabes que tu descripción de la vida de pareja se aleja mucho de la realidad para la mayoría de las parejas normales."
    if mc._var("relationships")>1 or mar._var("fittingRoom"):
        "Sabes que tu relación con [mad.nick] dista mucho de ser normal. Y te encanta que no lo sea."
    else:
        "Esperas que tu relación con [mad.nick] nunca sea normal."
    scene c27s003_440c with fade
    "De vuelta al salón, continuáis la película donde la dejasteis aquella primera vez que parece tan lejana."
    "Si no fuera porque los dos la habéis visto varias veces, deberíais empezarla desde el principio."
    scene c27s003_440An with dissolve
    "Pasáis más tiempo mirándoos a los ojos que mirando la pantalla."
    "Siempre habrá tiempo para volver a ver la película, pero cada momento en el que no miras los espectaculares ojos de [mad.nick] parece un momento perdido."
    "No habláis. No tenéis mucho que añadir a lo que vuestros ojos dicen."
    scene c27s003_440g with fade
    "Pero el cansancio hace mella en la diseñadora de vestidos después de un largo día de trabajo, las emociones, y los dos asaltos de sexo."
    "Se queda dormida en tu regazo, respirando pausadamente."
    "Es una preciosa visión que guardas en tus recuerdos para siempre."
    "Tú tampoco planificabas enamorarte de la hermosa asiática."
    scene c27s003_440h with fade
    "Apagas la TV y la coges en brazos para llevarla a vuestra habitación, después de quitarle las gafas."
    "Nunca más volverás a pensar en ella como la habitación de [mad.nick] después de esta noche. Es vuestra habitación. Donde pasan cosas maravillosas."
    mcp "(Si viera ahora mismo como estamos, a punto de cruzar la puerta con ella en brazos, seguro que lo disfrutaría muchísimo.)"
    mcp "(Lo estoy disfrutando yo y no tengo ese fetiche con el matrimonio... ¿o sí que lo tengo?)"
    "De alguna forma, sabe lo que está pasando y se coge con fuerza a ti."
    scene c27s003_440i with fade
    "La tumbas delicadamente sobre la cama y te quedas observándola por largo tiempo."
    "La respiración tranquila y la cara de felicidad son relajantes para ti."
    mcp "(Yo sí que me podría pasar horas haciendo esto. Sólo mirándote.)"
    "Pero al cabo de un rato, empiezan a pesarte los ojos. Parece que cada vez que decís que podríais hacer algo durante horas, no duráis más de unos minutos."
    scene c27s003_440j with fade
    "Apagas la luz y le das un suave beso en la frente."
    mc "*Susurrando* Te quiero."
    scene c27s003_440k with hpunch
    "Tus palabras penetran entre las capas de sueños y llegan a su cerebro. Te abraza fuertemente."
    mad "*En sueños* Yo también te quiero."
    stop music fadeout (1.5)
    "Pasáis toda la noche abrazados, durmiendo juntos por primera vez."
    scene black with dissolve
    centered "{size=+20}{b}DÍA 30 – MIÉRCOLES{/b}{/size}"
    scene c27s003_440l with fade
    "Te despiertas solo en la cama. Ya es de día."
    "Escuchas el agua corriendo en el baño. Decides curiosear."
    play music ("music/CCFunk.ogg")
    call BlinkXPS3 ("c27s003_445" , "f") from _call_BlinkXPS3_2797
    "En cuanto entras al baño, recibido por una visión espectacular, [mad.nick] cierra el grifo."
    mc "Buenos días, cielo. ¿Hace mucho que te has despertado?"
    mad "Hola, cariño. Unos diez minutos. ¿Qué tal has dormido?"
    mc "Genial. Tenía un pulpo con moño abrazándome todo el rato. ¿Y tú?"
    mad "He dormido como hacía mucho que no dormía. Podría dormir abrazada a ti cada noche."
    mc "Por cierto, dejé tus gafas en la mesa de al lado del sofá."
    call BlinkXS3 ("c27s003_450") from _call_BlinkXS3_591
    mad "¿Cómo llegué a la cama? No lo recuerdo..."
    mc "Te llevé en brazos. *Risa* Crucé el umbral con la bella durmiente en brazos y ni se enteró."
    call BlinkXS3 ("c27s003_455a") from _call_BlinkXS3_592
    mad "¿Qué? ¿Me lo perdí?"
    mc "*Risa* Pensé exactamente lo mismo. Pero no quería despertarte."
    mc "Lo repetiremos en algún otro momento en el que estés despierta, no te preocupes."
    call BlinkXS3 ("c27s003_455b") from _call_BlinkXS3_593
    mad "Eso espero. Veo que hoy no has necesitado que Zeus te abra la puerta del baño."
    mc "*Risa* Ya que no está disponible, la he tenido que abrir yo."
    if mad._var("dom"):
        call BlinkXS3 ("c27s003_460") from _call_BlinkXS3_594
        mad "¿Y vas a quedarte ahí mirando? ¡Entra aquí ahora mismo! ¡Me estoy congelando!"
        mc "¿Vas a volverte a poner dominante? *Risa* Creía que ya habíamos dejado eso atrás."
        mad "Lo hemos dejado atrás, pero no me gustaría olvidarlo. Y hacerlo de vez en cuando, como juego, podría ser divertido."
        call BlinkXS3 ("c27s003_465") from _call_BlinkXS3_595
        mad "También me puedo poner en plan sumisa y pedírtelo por favor. *Risa* Por favor, Amo, ¿quieres ducharte conmigo?"
        mc "No hace falta. *Risa* Hazme un hueco."
    elif mad._var("sub"):
        call BlinkXS3 ("c27s003_465") from _call_BlinkXS3_596
        mad "¿Va mi amo a quedarse ahí mirando o quiere entrar a compartir la ducha con su gatita?"
        mc "¿Vas a volverte a poner sumisa? *Risa* Creía que ya habíamos dejado eso atrás."
        mad "Lo hemos dejado atrás, pero no me gustaría olvidarlo. Y hacerlo de vez en cuando, como juego, podría ser divertido."
        call BlinkXS3 ("c27s003_460") from _call_BlinkXS3_597
        mad "También me puedo poner en plan dominante. *Risa* ¡Entra aquí ahora mismo! ¡Me estoy congelando!"
        mc "No hace falta. *Risa* Hazme un hueco."
    else:
        call BlinkXS3 ("c27s003_465") from _call_BlinkXS3_598
        mad "¿Quieres ducharte? Casi estoy acabando..."
        mc "¿Estás segura de querer acabar antes de que entre?"
        mad "A eso me refería... Si quieres ducharte hay hueco para los dos."
        mc "Una idea estupenda."
        call BlinkXS3 ("c27s003_460") from _call_BlinkXS3_599
        mad "¡Pues ya estás tardando en entrar! *Risa* ¡Me estoy congelando!"
        mc "*Risa* Hazme un hueco."
    scene c27s003_470d with dissolve
    "Nada más entrar en la ducha, unos labios húmedos y sensuales te dan la mejor de las bienvenidas."
    "Si [mad.nick] podría dormir abrazada a ti cada noche, tú podrías acostumbrarte a despertarte así cada mañana."
    "No hace falta que digáis nada. Vuestras respiraciones en la boca del otro comunican todo lo necesario."
    call BlinkXS3 ("c27s003_470") from _call_BlinkXS3_600
    "Para cuando acaba el largo beso, los dos volvéis a estar excitados."
    mc "Buenos días, mi amor."
    mad "Buenos días, mi amor."
    "[mad.nick] levanta una pierna, indicando cuál es el siguiente paso que quiere que des."
    scene c27s003_980An with dissolve
    "Sin perder un momento penetras a la preciosa mujer, recibiendo un familiar, húmedo y caliente abrazo alrededor de Mjolnir."
    mad "*Gemido* ¡Oooff! *Jadeo*"
    "No hay mucho más que pueda decir para impulsarte a empezar a bombear con tus caderas."
    scene c27s003_970pv with dissolve
    show c27s003_970v
    "Empiezas un lento movimiento, intentando llegar a todos sus puntos sensibles con tu polla."
    "Disfrutando del húmedo y caliente tacto de su cuerpo, en contraste con tu seca piel."
    mad "*Jadeo* Si la pasada noche fue la mejor de mi vida... *Gemido* Esta es la mejor mañana... *Jadeo*"
    "La primera de cientos de mañanas que están por venir en los próximos años. Hacer el amor en la ducha se convertirá en uno de vuestros momentos favoritos del día."
    "Ummm... Un narrador no debería mentir... Hacer el amor en cualquier sitio se convertirá en uno de vuestros momentos favoritos del día."
    scene c27s003_980pv with dissolve
    show c27s003_980v
    hide c27s003_970v
    "Con vuestras caderas sincronizadas, el movimiento se convierte cada vez en más placentero. Mjolnir está hecho para el coño de [mad.nick]. [mad.nick] está hecha para ti."
    mad "*Gemido* ¡Menos mal que compré una ducha grande! *Jadeo*"
    "Pese a que la ducha es grande para una persona, estando dos personas dentro, la libertad de movimientos queda un poco restringida."
    "Por suerte, Mjolnir no ocupa espacio extra, estando en su propio espacio húmedo."
    mad "*JADEO* ¡ME ENCANTA! *GEMIDO* ¡SIGUE ASÍ! *JADEO*"
    "Esperas que los vecinos de [mad.nick] ya se hayan levantado. Si no lo han hecho, en vez de una alarma, les despertarán los gemidos de la dependienta."
    scene c27s003_975pv with dissolve
    show c27s003_975v
    "Lo tórrido de vuestro sexo hace que el vapor de la ducha no se disipe del todo a pesar de que hace un rato que el grifo está cerrado."
    mad "*GEMIDO* ¡VOY A CORRERME! *JADEO* ¡MI PRIMERA VEZ EN UNA DUCHA! *GEMIDO* ... CON ALGUIEN... *JADEO*" id c27s003_MadLewd_a808233a
    "Consigues contener la risa a duras penas por la última parte de su frase. Pero el tensar los músculos de tu estómago hace que Mjolnir se endurezca más aún."
    mad "*JADEO* ¡SÍ! *GEMIDO* ¡ASÍ MEJOR! *JADEO*"
    "Ahora es ella quien tensa los músculos alrededor de su vagina, consiguiendo que aprisione con más fuerza todavía a Mjolnir."
    "Cada movimiento os acerca a ambos a vuestros respectivos orgasmos en una mañana inolvidable."
    if persistent.pregnancy and not mad._var("pregnant"):
        if persistent.walkthrough:
            $ wt1 = _("[mad.nick] embarazada.")
            $ wt2 = _("Sin consecuencias.")
        else:
            $ wt1 = ""
            $ wt2 = ""
        menu:
            "Correrte dentro. Ir a por el bebé." (wt = wt1):
                $ mad._var("pregnant", True)
                $ mad._var("undiscoveredPregnancy", True)
                play sound ("music/OldMusicBox5.ogg")
            "Correrte dentro." (wt = wt2):
                pass
    $ resetWalkthrough ()
    call OrgasmXS3 ("c27s003_475") from _call_OrgasmXS3_75
    hide c27s003_975v
    mc "¡Mpfft!"
    mad "*GEMIDO* ¡SÍ! *JADEO* ¡ME CORROOOO! *GEMIDO*"
    "Esta vez eres tú quien se corre poco antes que ella, provocando su clímax con las primeras gotas de semen que salen de tu polla."
    "Vuestros orgasmos casi sincronizados sacuden vuestros cuerpos al unísono."
    call BlinkXPS3 ("c27s003_480" , "f") from _call_BlinkXPS3_2798
    stop music fadeout (1.5)
    "Al cabo de un rato..."
    play music ("music/AmbientPianoStrings.ogg")
    mad "Creo que te voy a dar una llave de mi piso..."
    mc "¿Por si me quedo a dormir más veces?"
    call BlinkXS3 ("c27s003_485") from _call_BlinkXS3_601
    mad "Por si no te quedas a dormir y pasas por aquí a esta hora. *Risa* Es la hora a la que me ducho siempre..."
    mc "*Risa* Ya sabes que tengo fama de levantarme tarde... Fama inmerecida... "
    mc "No creo que esté conduciendo a estas horas por el centro de la ciudad. Aunque podría hacerlo para repetir esto."
    call BlinkXS3 ("c27s003_490") from _call_BlinkXS3_602
    mad "*Risa* No me importaría que vinieras, pero no te voy a hacer madrugar. Tan solo espero que te quedes a dormir a menudo."
    mad "Cuando esté Zeus en casa no podrás dormir hasta tarde y tendrás que refugiarte conmigo en la ducha. *Risa*"
    mc "No me importaría que el gato me despertara si esta es la recompensa."
    mc "Pero creo que deberíamos terminar de ducharnos o vas a llegar tarde."
    call BlinkXS3 ("c27s003_495") from _call_BlinkXS3_603
    mad "Tienes razón... Pero no quiero que esta mañana acabe..."
    mc "Te prometo que habrá muchas mañanas como esta. Incluso mejores."
    scene c27s003_470d with dissolve
    "La preciosa mujer te da un dulce beso lleno de pasión, pero también de tristeza porque la mañana haya acabado y tengáis que volver a vuestra rutina."
    "Ella a la tienda y tú a casa a seguir planificando el viaje a Aruba."
    "Pero es un beso que también transmite esperanza por todas las mañanas que vendrán. Los dos sabéis que ésta no será la última."
    call BlinkXPS3 ("c27s003_500" , "f") from _call_BlinkXPS3_2799
    "Cuando salís de la ducha..."
    mad "¿Sabes lo que más me ha gustado de todo lo que ha pasado desde que entraste en el piso?"
    mc "¿El post-it? ¿La cena desnudos? ¿El sexo? ¿La ducha?"
    call BlinkXS3 ("c27s003_505") from _call_BlinkXS3_604
    mad "*Risa* Bueno, sí, todo eso me ha encantado. Pero lo que más me ha gustado es que todo se ha sentido muy natural. Como si fuéramos un matrimonio que lleva años juntos."
    mc "*Risa* Sigo pensando que tienes un fetiche con el matrimonio."
    call BlinkXS3 ("c27s003_510") from _call_BlinkXS3_605
    mad "*Risa* Después de las últimas 12 horas, creo que no lo puedo negar. Estoy permanentemente cachonda desde que me diste el post-it."
    mc "Puedes llamar a tu madre diciendo que estás enferma y no ir a la tienda."
    call BlinkXS3 ("c27s003_515") from _call_BlinkXS3_606
    mad "Entonces vendría aquí con un bote de caldo de pollo. Imagínate lo que pensaría si nos ve... Sería capaz de despedirme."
    mc "¿Te despediría tu propia madre?"
    mad "Por supuesto. Para ella sería una empleada que le ha mentido. Incluso yo lo consideraría lógico."
    call BlinkXS3 ("c27s003_520") from _call_BlinkXS3_607
    mad "Pero a lo que me iba. Excepto porque no hemos ido al lavabo y no nos hemos tirado pedos en presencia del otro, ha sido como estar casados."
    mad "Supongo que aún tenemos algunos límites que respetar."
    stop music fadeout (1.5)
    $ mad._var("chanceFart" , True)
    if persistent.walkthrough:
        $ wt1 = _("Más diálogo.")
        $ wt2 = _("Menos diálogo.")
    else:
        $ wt1 = ""
        $ wt2 = ""
    menu:
        "Tirarte un pedo." (wt = wt1):
            scene c27s003_520d with hpunch
            play sound ("music/fart.ogg")
            mc "*Pedo*"
            play music ("music/EpicFemaleSolo.ogg")
            scene c27s003_520e with hpunch
            mad "¿Qué?"
            scene c27s003_520f with hpunch
            play sound ("music/DoorSlam.ogg")
            "Sales del baño y cierras la puerta. Agarras la puerta con fuerza."
            mad "*A través de la puerta* ¿Qué?"
            play sound ("music/knock.ogg")
            "*Knock*"
            mad "*A través de la puerta* ¡Déjame salir!"
            scene c27s003_520f with hpunch
            play sound ("music/wood.ogg")
            pause 0.1
            play sound ("music/wood.ogg")
            "*Golpes en la puerta*"
            mad "*A través de la puerta* ¡Qué peste!"
            scene c27s003_520f with hpunch
            play sound ("music/wood.ogg")
            pause 0.1
            play sound ("music/wood.ogg")
            "*Golpes fuertes en la puerta*"
            mad "*A través de la puerta* ¡Por favor, [mc]!"
            scene c27s003_520f with hpunch
            play sound ("music/wood.ogg")
            pause 0.1
            play sound ("music/wood.ogg")
            "*Golpes fuertes en la puerta*"
            mad "*A través de la puerta* ¡Me muero!"
            "Los golpes cesan."
            "Esperas. No se oye nada."
            mc "¿[mad.nick]?"
            "Silencio."
            "Esperas. Sigue sin oírse nada."
            scene c27s003_520g with dissolve
            "Abres la puerta. Huele a pedo, pero no es de los peores que te has tirado."
            mc "*Risa* ¿Qué haces?"
            mad "Me he muerto."
            mc "*Risa* Levántate o llegarás tarde a la tienda."
            mad "Dile a mi madre que la quería... No, mejor díselo a [mar]."
            mad "Dile que la quería pese a haber criado un cerdo apestoso."
            mc "*Risa* Voy a ir vistiéndome."
            mad "¿Vas a dejar el cadáver de tu prometida tirado en el suelo?"
            mc "*Risa* ¿Te ayudo a levantarte?"
            mad "¿Ayudarme a levantarme? ¿Soy un zombi?"
            scene c27s003_520h with dissolve
            mc "*Risa* Venga, en serio. Vas a llegar tarde si sigues con las payasadas."
            scene c27s003_520i with dissolve
            "La ayudas a levantarse y te abraza fuertemente."
            mad "*Risita* Eso ha sido gracioso. Es algo que haría una pareja que lleva más de 20 años casados."
            mc "*Risa* Estabas muy graciosa tirada en el suelo, zombi mía."
            mad "*Risa* Gracias, pero es un juego que pueden jugar dos."
            stop music fadeout (1.5)
            mc "¿A qué te refieres?"
            scene c27s003_520j with dissolve
            play sound ("music/fart-vegan.ogg")
            mad "*Pedo*"
            mad "*Risa* ¡Corre insensato!" #Fly, you fool
            mc "*Risa* ¡Noooo!"
            stop sound
            scene c27s003_520f with dissolve
            play sound ("music/DoorSlam.ogg")
            "Sales corriendo del baño, cerrando la puerta detrás tuyo."
            mc "Voy a ir vistiéndome. *Risa* Si no estás muerta, te llevo al trabajo."
            mad "*A través de la puerta* ¿Por qué iba a morirme? *Risa* ¡Mis pedos huelen a rosas y arcoíris!"
            $ mad._var("fart", True)
        "No hacerlo." (wt = wt2):
            mc "*Risa* Creo que es bueno respetar ese tipo de límites."
            mc "Voy a ir vistiéndome mientras acabas de arreglarte."
            $ mad._var("fart", False)
    $ resetWalkthrough ()
    scene black with dissolve
    pause (0.1)
    call BlinkXS3 ("c27s003_525") from _call_BlinkXS3_608
    play music ("music/Happy-Sun.ogg")
    "Unos minutos después, tras tomar un café y hacer un desayuno ligero, llevas a [mad.nick] a la tienda."
    mad "Creo que aquí acaba nuestra maravillosa cita."
    mc "¿Te lo has pasado bien?"
    call BlinkXS3 ("c27s003_530") from _call_BlinkXS3_609
    mad "La mejor noche y la mejor mañana de mi vida."
    if mad._var("fart"):
        mad "Ni siquiera tu pedo apestoso ha conseguido estropearla."
        mc "*Risa* A mí no me culpes. Eras tú quien quería la experiencia matrimonial completa."
        mc "Y has tenido tu venganza."
    else:
        mc "Me alegra mucho que te lo hayas pasado tan bien como yo. Y que hayas podido alimentar tu fetiche."
    scene c27s003_530d with dissolve
    pause (1.0)
    call BlinkXS3 ("c27s003_530") from _call_BlinkXS3_610
    mad "No sé de lo que estás hablando. *Risa*"
    mad "Y no te voy a dar la oportunidad de aclararlo. Tengo que limpiar antes de abrir la tienda."
    mc "Ven a casa a cenar esta noche."
    mad "Sí, tengo que hablar con las chicas. Vendrá a buscarme [sam.nick]. Te veo esta noche."
    if mee._var("route") and bet._var("route"):
        mad "{i}(Y tengo que hablar con [mee] y Tía [bet] antes de que se vayan.)"
    elif mee._var("route"):
        mad "{i}(Y tengo que hablar con [mee] antes de que se vaya.)"
    elif bet._var("route"):
        mad "{i}(Y tengo que hablar con Tía [bet] antes de que se vaya.)"
    mc "Hasta la noche, [mad.nick]."
    scene drive_day with fade
    "Vuelves a casa con una sonrisa en la cara. Realmente ha sido fantástico desde que [mad.nick] y [lis] llegaron al café."
    stop music fadeout (1.5)
    if mad._var("fart"):
        "Incluyendo el pedo. Tu novia es una zombi."
    return
label c27s004_KatBreakfast:
    if _in_replay:
        call mrS3_mad_route from _call_mrS3_mad_route_8
    if mad._var("route"):
        scene black with dissolve
        "Al llegar a casa subes a tu habitación a ponerte ropa más cómoda."
        "Después decides ir a tomar un café y añadir algo a tu estómago para suplir el ligero desayuno que has tomado en el apartamento de [mad.nick]."
    else:
        "Cuando te despiertas, bajas a desayunar algo."
    scene c27s004_005a with fade
    play music ("music/Throne-King.ogg")
    "Al pasar por la planta de las estudiantes te encuentras con [kat] saliendo de su habitación mirando el móvil..."
    mc "Buenos días, [kat]. ¿Bajas a desayunar?"
    scene c27s004_005b with hpunch
    kat "¡Oh! Buenos días, [mc]."
    scene c27s004_005c with hpunch
    kat "Iba a desayunar, pero me acabo de acordar de algo..."
    scene c27s004_005d with hpunch
    play sound ("music/DoorSlam.ogg")
    "*Blam*"
    mcp "(¿Sigue enfadada por lo que fuera que pasó durante el desayuno de ayer?)"
    stop music fadeout (1.5)
    scene c27s004_010a with fade
    "Cuando llegas a la cocina la encuentras más concurrida de lo normal."
    play music ("music/RhythmPlay.ogg")
    mc "Buenos días, chicas."
    todas "Buenos días, [mc]."
    if mad._var("route"):
        mc "Me sorprende veros aquí."
        call BlinkXS3 ("c27s004_015") from _call_BlinkXS3_611
        ama "Bueno, anoche nos pusimos en plan familia y algunas nos quedamos a dormir."
        mc "¿Cómo os distribuisteis?"
        ama "Yo he compartido habitación con [mar], [eva] con [emm], y [oma] con [sai]."
        call BlinkXS3 ("c27s004_020") from _call_BlinkXS3_612
        oma "Y con [eil]. Te lo perdiste, estuvo muy bien. Estuvimos estrechando lazos."
        oma "Las que no tenemos tantas oportunidades de pasar tiempo en casa las tenemos que aprovechar."
        mc "Eso está genial. Deberíais hacerlo más a menudo."
        call BlinkXS3 ("c27s004_025") from _call_BlinkXS3_613
        eva "Por cierto, [lis] nos contó lo que hiciste con la madre de [mad.nick]. Bien hecho."
        eva "La única vez que la vi, me entraron ganas de dispararle."
        mc "*Risa* ¡[eva]!"
        eva "*Risa* O, como mínimo, de torturarla un poco."
        call BlinkXS3 ("c27s004_030") from _call_BlinkXS3_614
        emm "No todo el mundo tiene la suerte de tener una madre como la nuestra."
        mc "Tienes razón. No podríamos tener una madre mejor."
        call BlinkXS3 ("c27s004_035") from _call_BlinkXS3_615
        mom "Me vais a hacer ruborizar..."
        mc "¿Y qué tal la noche durmiendo en camas ajenas?"
    else:
        mc "¿Qué tal la noche durmiendo en camas ajenas?"
    call BlinkXS3 ("c27s004_040") from _call_BlinkXS3_616
    eva "Demasiado rosa para mi gusto en esa habitación, pero muy bien."
    mc "*Risa* Y lo dices mientras llevas un pijama rosa."
    call BlinkXS3 ("c27s004_045") from _call_BlinkXS3_617
    emm "No traía pijama y le he prestado uno mío. Pero con lo que acaba de decir, creo que le voy a obligar a quitárselo. *Risa*"
    call BlinkXS3 ("c27s004_050") from _call_BlinkXS3_618
    oma "Compartir cama con [sai] y [eil] es un poco complicado. *Risa* Creo que todas acabamos con pelo de las otras en la cara durante la noche."
    oma "Pero podría repetirlo en cualquier momento."
    call BlinkXS3 ("c27s004_055") from _call_BlinkXS3_619
    ama "Ha sido fantástico. Creo que yo también voy a repetir."
    ama "Antes de ir a dormir estuvimos en el comedor charlando con [kim], [deb.nick], y [lis]. [deb.nick] me prestó el pijama."
    call BlinkXS3 ("c27s004_060") from _call_BlinkXS3_620
    mom "Les estaba diciendo que dejaran un par de pijamas aquí cada una. Así se pueden quedar sin planearlo y tendrán ropa aquí."
    mc "Me parece una muy buena idea. *Risa* Aunque ya sabéis que yo considero los pijamas un atuendo innecesario."
    scene c27s004_010b with dissolve
    todas "*Risa*"
    mom "Creo que aún no hemos habilitado el interior de la casa como zona nudista. Ni creo que lo vayamos a hacer."
    oma "Es comprensible, [mar]. Quizás hubiera alguna chica que se sentiría incómoda."
    eva "No entiendo por qué. Yo normalmente no uso."
    ama "No a todas las mujeres les gusta que un hombre las vea desnudas. Imagínate a [kat] desnuda y cruzándose con [mc]."
    emm "Además, ¿os imagináis la cara de [kat] cuando bajara a desayunar si estuviéramos todas desnudas? *Risa*"
    mc "Por cierto, hablando de [kat]. ¿Sabéis si le pasa algo?"
    call BlinkXS3 ("c27s004_065") from _call_BlinkXS3_621
    mom "No, ha bajado a desayunar, pero ha subido a buscar el móvil. Estará aquí en un minuto, supongo. ¿Por qué lo preguntas?"
    mc "La he visto en el descansillo y me ha dicho que se había olvidado algo. Se ha metido en su habitación como una exhalación."
    mcp "(Pues parece que sí. Que sigue enfadada conmigo. No voy a decir que salía de su habitación con el móvil en la mano.)"
    call BlinkXS3 ("c27s004_070") from _call_BlinkXS3_622
    emm "El móvil, ¿no?"
    mc "Es posible..."
    scene black with dissolve
    "Pasas un rato hablando con las chicas mientras tomas un par de cafés y vuelves a tu habitación."
    "[kat] ha hecho muy buenas migas con [nor] y con [kim]. Quizás ellas sepan algo sobre lo que le pasa y por qué se enfadó."
    stop music fadeout (1.5)
    return
label c27s004_MeeBetFarewell:
    if _in_replay:
        call mrS3_mee_route from _call_mrS3_mee_route_10
        call mrS3_bet_route from _call_mrS3_bet_route_6
    "Cuando aún queda un rato para que [nor] tenga que llevar a [mee] y a [bet] al aeropuerto, vas a sus habitaciones a bajar sus maletas."
    call BlinkXS3 ("c27s004_100") from _call_BlinkXS3_623
    play music ("music/Sad-Cinematic.ogg")
    mc "Hola, Meemaw. ¿Necesitas ayuda con esa maleta?" id c27s004_MeeBetFarewell_f166efc0
    mee "Hola, [mc]. Ya casi está lista."
    if mee._var("route"):
        scene c27s004_105a with dissolve
        pause (0.8)
        scene c27s004_105d with dissolve
        pause (1.0)
        call BlinkXS3 ("c27s004_105") from _call_BlinkXS3_624
        mee "Lo que sí que necesitaba era un beso."
        mc "No te preocupes, de esos tengo muchos para darte."
    call BlinkXS3 ("c27s004_110") from _call_BlinkXS3_625
    mee "Se me va a hacer raro estar unos días fuera sin veros."
    mc "Espero que estés de vuelta antes de que me vaya a Aruba."
    call BlinkXS3 ("c27s004_115") from _call_BlinkXS3_626
    mee "Supongo que sí. Nunca he tenido demasiadas cosas en aquella casa, con lo que empaquetar será rápido con la ayuda de [bet]."
    mee "Y ponerla a la venta también. He hecho algunas llamadas y el hijo de un conocido es agente inmobiliario."
    mc "Entonces podemos esperar que estés de vuelta para el fin de semana, ¿no? *Risa*"
    call BlinkXS3 ("c27s004_120") from _call_BlinkXS3_627
    mee "*Risa* He dicho rápido, no inmediato. El chico ese pasará a ver la casa el viernes."
    mee "Supongo que estaremos de vuelta en menos de una semana."
    mc "Eso será genial. Yo me voy a finales de la semana que viene si todo va bien."
    scene c27s004_120d with dissolve
    mee "Te voy a echar mucho de menos."
    mc "Y yo a ti, Meemaw. Pero es menos de una semana."
    call BlinkXS3 ("c27s004_125") from _call_BlinkXS3_628
    mee "No me refería a estos días. Cuando vuelva, tú te irás y estarás fuera meses."
    mc "Bueno, no sé si podré venir en Acción de Gracias o en Navidad."
    mc "Pero de todas formas, también me puedes visitar en Aruba."
    call BlinkXS3 ("c27s004_130") from _call_BlinkXS3_629
    mee "¿Dónde vas a vivir allí? ¿En la base de NTR?"
    mc "No, hay una casa a disposición del CEO, en la costa. Aaron me mandó fotos y es chula."
    mc "Pero me voy a sentir muy solo allí."
    call BlinkXS3 ("c27s004_135") from _call_BlinkXS3_630
    mee "Bueno, vas con [ama] y después irá [eva]. ¿Vivirán contigo?"
    mc "Aún no lo hemos hablado. Aaron también es su familia y él vive en la base. No sé qué querrán hacer ellas."
    if mee._var("route"):
        call BlinkXS3 ("c27s004_140") from _call_BlinkXS3_631
        mee "Yo lo tendría clarísimo. ¿Cuántas camas hay en esa casa? Porque las querré probar todas cuando vaya a verte."
        mc "*Risa* Veo que alguien quiere recuperar el tiempo perdido."
        mc "*Risa* En ese caso, sería mejor para tus planes que [ama] y [eva] durmieran en la base."
        call BlinkXS3 ("c27s004_145") from _call_BlinkXS3_632
        if persistent.family:
            mee "*Risa* Seguro que sí. Lo de decirles 'vete a dormir al sofá porque mi nieto y yo vamos a follar en tu cama' no parece diplomático."
        else:
            mee "*Risa* Seguro que sí. Lo de decirles 'vete a dormir al sofá porque [mc] y yo vamos a follar en tu cama' no parece diplomático."
        if ama._var("route") and eva._var("route"):
            mc "*Risa* Creo que no lo sería. Además podría pasar que se quisieran unir, aunque en el caso de [ama] lo dudo."
            mc "Pero no me sorprendería que [eva] quisiera estrechar lazos contigo con un trío."
        elif ama._var("route"):
            mc "*Risa* Creo que no lo sería. Además podría pasar que [ama] uniera, aunque lo dudo."
        elif eva._var("route"):
            mc "*Risa* Creo que no lo sería. Además podría pasar que [eva] se quisiera unir. No me sorprendería que quisiera estrechar lazos contigo con un trío."
        else:
            mc "*Risa* Creo que no lo sería."
        mc "Pero podemos probar todas las camas no ocupadas."
        scene c27s004_145d with dissolve
        if persistent.family:
            "Tu abuela te da un beso como pocos nietos han recibido de sus abuelas."
        else:
            "[mee] te da un beso como pocos nietos han recibido de sus abuelas. Da lo mismo que no estéis emparentados. Siempre será tu abuela."
        "Es un beso que sabe a despedida."
    call BlinkXS3 ("c27s004_150") from _call_BlinkXS3_633
    mee "Deberías bajar la maleta e ir a ver a [bet]. Es posible que ella también necesite ayuda."
    mee "Y no quiero alargar nuestra despedida más de lo necesario o me voy a poner triste antes de irme."
    mc "De acuerdo. Y no te pongas triste. Nos veremos en menos de una semana."
    scene c27s004_120d with dissolve
    mee "Hasta dentro de una semana, [mc]."
    mc "Hasta dentro de una semana, Meemaw."
    scene c27s004_155a with fade
    call BlinkXS3 ("c27s004_155") from _call_BlinkXS3_634
    "Bajas la maleta de [mee] a la planta baja y vas a ver a [bet]."
    mc "Hola, Tía [bet]. ¿Necesitas ayuda con las maletas?"
    bet "No hace falta. Era solo una y la he bajado hace un rato. Ya está en el coche de [nor]."
    mc "Perfecto, acabo de bajar la de Meemaw. Dejo que te acabes de vestir, entonces."
    scene c27s004_155d with dissolve
    bet "Te voy a echar mucho de menos."
    mc "Y yo a ti, pero Meemaw me ha dicho que estaréis fuera menos de una semana."
    mc "Y después espero que vengas a Aruba conmigo para operar a Gavin."
    call BlinkXS3 ("c27s004_160") from _call_BlinkXS3_635
    bet "Aún tengo que acabar de estudiar la información que me ha mandado Aaron, pero creo que iré finalmente."
    bet "La perspectiva de hacer una operación que no se ha hecho nunca es el sueño de cualquier cirujano."
    mc "Entonces no tendrás mucho tiempo para echarme de menos."
    call BlinkXS3 ("c27s004_165") from _call_BlinkXS3_636
    bet "Pero entonces echaré de menos a todas las chicas. Incluso a [mee]."
    mc "Sobre eso no puedo hacer mucho. Yo también las voy a echar de menos."
    if not bet._var("route"):
        scene c27s004_155d with dissolve
        bet "Bueno, vete ya antes de que se me salten las lágrimas. Tengo que acabar de vestirme."
        mc "OK. Te veo abajo."
        if mad._var("route"):
            scene c25s007_010a with dissolve
            "Al pasar por delante de la puerta de [mee] oyes voces en el interior."
            mee "*A través de la puerta* Hola, [mad.nick], dime..."
    else:
        call BlinkXS3 ("c27s004_170") from _call_BlinkXS3_637
        bet "Por otro lado, tengo ganas de estar tiempo a solas contigo en Aruba."
        mc "No sé si vamos a tener mucho tiempo libre, pero lo pasaremos juntos."
        call BlinkXS3 ("c27s004_175") from _call_BlinkXS3_638
        bet "*Risa* Si hacer esa operación imposible no fuera incentivo suficiente para ir, pasar tiempo contigo en un paraíso tropical sería un aliciente extra."
        mc "*Risa* A mí lo del paraíso tropical no me suena demasiado bien. Calor, humedad, mosquitos..."
        call BlinkXS3 ("c27s004_180") from _call_BlinkXS3_639
        bet "*Risa* Entonces haremos el amor dentro de tu casa, bajo el aire acondicionado."
        mc "*Risa* Me parece una idea fantástica."
        scene c27s004_180d with dissolve
        "La ex-monja te da un beso dulce en el que hay anticipación, pero también algo de tristeza por el tiempo que vais a pasar separados."
        "No habéis tenido muchas oportunidades de pasar tiempo juntos desde el viaje a Monterey y ahora ella se tiene que ir."
        "Aún no sabes cuánto tiempo estará ella en Aruba para la operación, lo que sabes es que lo vais a aprovechar."
        call BlinkXS3 ("c27s004_185") from _call_BlinkXS3_640
        bet "Deberías irte antes de que te tumbe en la cama o perderé el avión."
        mc "*Risa* Entonces voy a dejar que te vistas. Te veo abajo, [bet]."
        if mad._var("route"):
            scene c27s004_185d with dissolve
            "*Ring-Ring*"
            "Mientras te diriges a la puerta de su habitación, suena el teléfono de [bet]."
            bet "Hola, [mad.nick], dime..."
    if mad._var("route"):
        mcp "(Estoy super contento con las dinámicas que se están creando en la familia. Que [mad.nick] llame para despedirse es una muestra de ello.)"
    scene black with dissolve
    "Bajas a la cocina a esperar a que las mujeres acaben de arreglarse y con la esperanza de poder preguntarle a [nor] o a [kim] sobre lo que le pasa a [kat]."
    scene c27s004_190a with fade
    "Por desgracia, preguntarles sobre [kat] con [kat] delante no es una opción."
    "Menos aún cuando [kat] rehúye tu mirada. Cada vez estás seguro de que le pasa algo."
    scene black with dissolve
    "La despedida de las dos mujeres es demasiado triste."
    "Es la primera vez desde que se empezó a formar el sentimiento familiar que alguien va a estar fuera durante una semana."
    "Se derraman algunas lágrimas, pero las chicas me han pedido que no diga quién lloró. Especialmente [eva]."
    "¡Oops! Me parezco a [lis] guardando secretos."
    scene c27s004_190b with dissolve
    "Cuando se van, tampoco tienes la oportunidad de hablar con [kim]. Vuelve a casa charlando con [kat]."
    "Bueno, habrá tiempo para hablar. O incluso es posible que a [kat] se le pase lo que sea que le está pasando."
    stop music fadeout (1.5)
    return
label c27s004_ScaInterview:
    if _in_replay:
        call mrS3_oma_route from _call_mrS3_oma_route_5
    scene black with dissolve
    "Ayudas a [emm] a mover los trastos del sótano. Ha hecho un buen trabajo con las pegatinas rosas."
    "Todos los trastos que hay que tirar son fácilmente identificables."
    "[emm] derrama algunas lágrimas cuando ve todas las pegatinas que ha perdido una vez subes las cosas a la camioneta."
    "Ha intentado recuperar las pegatinas sin éxito."
    "[oma] aprovecha su día de fiesta para ayudarte a llevar los trastos al chatarrero antes de comer."
    scene c27s002_245d with dissolve
    "Después de comer las chicas van a la piscina y tú vuelves a tu habitación..."
    play sound ("music/knock.ogg")
    "*Knock-Knock*"
    eri "*A través de la puerta* Somos nosotras, ¿podemos pasar?"
    play music ("music/RhythmPlay.ogg")
    mc "Adelante, tú y tu silenciosa compañera."
    scene c27s004_200a with dissolve
    eri "*Risa* Mi silenciosa compañera es [sca]."
    sca "Hola, [mc]."
    mc "¿Te pasa algo, [sca]?"
    call BlinkXS3 ("c27s004_205") from _call_BlinkXS3_641
    eri "Está nerviosa. [eil] me acaba de llamar para decirme que nuestro jefe quiere conocer a [sca]."
    eri "Ayer le hablamos de ella y hoy se pasará por el café. ¿Nos puedes llevar?"
    mc "Claro, ningún problema. ¿Cuándo os tengo que llevar?"
    call BlinkXS3 ("c27s004_210") from _call_BlinkXS3_642
    eri "Yo empiezo mi turno en 50 minutos. Si nos llevas a las dos, [sca] puede esperar allí hasta que llegue mi jefe."
    mc "OK. Podríamos salir en 30 minutos y llegamos con tiempo antes de que empieces el turno."
    call BlinkXS3 ("c27s004_215") from _call_BlinkXS3_643
    mc "No estés nerviosa, es sólo una entrevista de trabajo."
    sca "Es que va a ser mi primera entrevista. Mi madre no me dejaba trabajar, decía que me tenía que centrar en los estudios."
    mc "Eres lo suficientemente inteligente como para hacer las dos cosas, [sca]."
    mc "Además, estoy seguro de que tanto [eri] como [eil] te han dado consejos."
    call BlinkXS3 ("c27s004_220") from _call_BlinkXS3_644
    eri "Básicamente que se convierta en nuestra esclava mientras esté en el café. *Risa* Es broma."
    eri "Mi jefe no es muy exigente y ella viene recomendada por nosotras, con lo que tiene muchas posibilidades de que la contrate."
    call BlinkXS3 ("c27s004_225") from _call_BlinkXS3_645
    eri "Y una vez empiece a trabajar, [eil] y yo moveremos nuestros turnos para que una de las dos esté con ella cada día al menos las primeras semanas."
    mc "Estoy seguro de que eso la ayudará mucho."
    call BlinkXS3 ("c27s004_230") from _call_BlinkXS3_646
    mc "¿Ves? No tienes que estar nerviosa. [eri] y [eil] lo tienen todo planificado."
    sca "Pero es que ya me conocéis. Soy tímida y me cuesta mucho hablar con desconocidos..."
    sca "¿Y si empiezo a balbucear en la entrevista? ¿Y si me quedo en blanco?"
    mc "¿Y si se te escapa un eructo durante la entrevista?"
    call BlinkXPS3 ("c27s004_235" , "h") from _call_BlinkXPS3_2800
    sca "¿Qué?"
    mc "Te estás poniendo nerviosa pensando en todo lo que puede salir mal. *Risa* Yo solo te doy un escenario nuevo en el que no habías pensado."
    call BlinkXS3 ("c27s004_240") from _call_BlinkXS3_647
    sca "¡Eres un capullo! ¡Eso no ayuda!"
    mc "Sí que ayuda. *Risa* La [sca] tímida de hace un mes nunca me hubiera llamado capullo."
    mc "Ya no eres la que eras. Desde que llegaron las chicas te has abierto mucho y has perdido la timidez. No tienes que temer nada en la entrevista."
    call BlinkXS3 ("c27s004_245") from _call_BlinkXS3_648
    eri "¿Ves cómo hemos hecho bien en venir a ver a [mc]? Sabía que te quitaría los nervios."
    mc "Veo que no vas con el uniforme. ¿Hablaste con tu jefe respecto a la taquillas de [eil]?"
    call BlinkXS3 ("c27s004_250") from _call_BlinkXS3_649
    eri "Sí, y fue la cosa más tonta del mundo. Él creía que ya compartíamos taquilla porque somos amigas."
    eri "Dijo que todo el mundo lo hace..."
    mc "*Risa* Todo el mundo lo pensó menos vosotras. Sois demasiado legales."
    call BlinkXS3 ("c27s004_255") from _call_BlinkXS3_650
    sca "Pues voy a cambiarme de ropa para la entrevista. No creo que ir así sea lo mejor..."
    mc "Nope. En eso tienes razón. *Risa* Aunque yo te contrataría."
    scene c27s002_245d with dissolve
    "Las dos chicas se van y te dejan solo en la habitación."
    scene black with dissolve
    "Bajas a sacar la camioneta del garaje unos minutos antes de lo acordado."
    scene c27s004_200b with dissolve
    "[eri] y [sca] ya te están esperando. Los nervios no han desaparecido del todo."
    scene drive_day with dissolve
    "Durante el trayecto [sca] hace mil preguntas a [eri]. Quiere saber cómo funciona todo antes de la entrevista."
    scene c27s004_200c with fade
    "Al llegar al café, [eri] sustituye a [eil], que se sienta a tomar un café con [sca] y contigo."
    "El bombardeo de preguntas se dirige a la pelirroja ahora."
    call BlinkXPS3 ("c27s004_260" , "f") from _call_BlinkXPS3_2801
    "La llegada de [oma] salva tu salud mental. A la vigésima pregunta sobre la cafetera, tu cerebro se ha desconectado."
    oma "¿Qué tal? ¿Ya ha tenido la entrevista?"
    mc "No, aún no. El jefe llegará en una hora más o menos."
    oma "¿Te vas a quedar hasta que acabe la entrevista?"
    mc "Sí, entonces la llevaré a ella y a [eil] a casa. Quiero saber si le han dado el trabajo."
    call BlinkXS3 ("c27s004_265") from _call_BlinkXS3_651
    eil "No lo sabrá hoy. Hay un par de chicas más que vienen a hacer entrevistas después de ella."
    eil "Lo más probable es que mi jefe avise a la chica que contrate mañana."
    mc "De todas formas esperaré para llevaros a casa."
    call BlinkXS3 ("c27s004_270") from _call_BlinkXS3_652
    eil "No hace falta. Puedes llevar a [oma] y que ella me deje su coche y yo llevo a [sca]."
    eil "*Risa* De todas formas vamos a seguir ignorándote."
    mc "*Risa* Creo que puedo nombrar 17 partes de la cafetera ahora mismo. Y seis tipos de pastas que vendéis."
    call BlinkXS3 ("c27s004_275") from _call_BlinkXS3_653
    sca "Lo siento, [mc]. Sé que no soy una buena compañía cuando me pongo así. Quiero saber todo lo posible antes de la entrevista."
    mc "No te preocupes, es lógico. Va a ser tu primer trabajo."
    sca "Si consigo el trabajo..."
    mc "Cuando consigas el trabajo."
    call BlinkXS3 ("c27s004_280") from _call_BlinkXS3_654
    oma "Entonces, ¿me llevas a casa?"
    mc "Sí, si estas dos van a seguir ignorándome no tiene ningún sentido que me quede. *Risa*"
    oma "Tengo que pasar por mi apartamento a coger los pijamas para dejarlos en casa."
    mc "¿También te vas a quedar a dormir hoy?"
    call BlinkXS3 ("c27s004_290") from _call_BlinkXS3_655
    oma "No puedo. Empiezo mi turno a medianoche. Me iré después de cenar, pero así ya tendré los pijamas allí para el día que me pueda quedar."
    call BlinkXS3 ("c27s004_285") from _call_BlinkXS3_656
    oma "*Risa* ¡[sai] no tiene pijamas! Y no estoy acostumbrada a dormir en camisón."
    if oma._var("route"):
        mc "Pues te quedaba genial. Estabas super sexy."
    else:
        mc "Pues te quedaba muy bien."
    mc "Al menos te quedaba mejor de lo que le quedaba el pijama de [deb.nick] a [ama]."
    scene black with dissolve
    "Te despides de [sca], [eil] y [eri] y emprendes el camino al apartamento de [oma]."
    "Vive a dos calles y vais dando un paseo."
    if oma._var("route"):
        scene c27s004_200d with dissolve
        "Se te hace raro pasear cogido de la mano con [oma]. Maravillosamente raro."
        "No habéis hecho muchas cosas de las que hacen las parejas normales. Nunca habéis paseado ni salido a cenar."
        "Pero no por ello estás menos loco por ella. La normalidad está sobrevalorada."
    stop music fadeout (1.5)
    "Y vas a ver su apartamento por primera vez."
    return
label c27s005_PaintBasement:
    if _in_replay:
        call mrS3_nor_route from _call_mrS3_nor_route_10
        if nor._var("route"):
            call mrS3_nor_secondChance from _call_mrS3_nor_secondChance
        call mrS3_emm_route from _call_mrS3_emm_route_18
        if emm._var("route") or nor._var("route"):
            if persistent.lesbian:
                call mrS3_eri_route from _call_mrS3_eri_route_11
        if emm._var("route") and eri._var("route") and persistent.lesbian:
            call mrS3_dap_route from _call_mrS3_dap_route_10
        if emm._var("route") and persistent.lesbian:
            call mrS3_mar_route from _call_mrS3_mar_route_15
    scene c27s005_005a with fade
    play music ("music/Vacation-Vibe.ogg")
    "Mientras tanto, en el sótano..."
    mom "Parece que hace años que pintamos la habitación de [sai]."
    nor "Tienes razón. Aunque parezca mentira, no ha pasado un mes todavía de aquello."
    emm "Y aquel día estaba [mc] en vez de [kim]. Hoy no podremos humillarlo con una batalla de pintura."
    kim "¿Hicisteis una batalla de pintura?"
    call BlinkXS3 ("c27s005_010") from _call_BlinkXS3_657
    mom "Ya sabes cómo va esto. *Risa* [mc] dijo algo que no le gustó a [emm] y [emm] le pegó con el rodillo."
    mom "Acabamos haciendo una batalla [emm] y yo contra [nor] y [mc]."
    call BlinkXS3 ("c27s005_015") from _call_BlinkXS3_658
    kim "Me encanta cómo hacéis algo divertido de cualquier situación."
    call BlinkXS3 ("c27s005_020") from _call_BlinkXS3_659
    emm "No, [kim]. No es 'hacéis'. Ahora es 'hacemos'. Tienes que empezar a incluirte cuando hables de la familia."
    emm "Por cierto, la batalla la ganamos nosotras como es normal."
    call BlinkXS3 ("c27s005_025") from _call_BlinkXS3_660
    nor "*Risa* No estoy demasiado segura de que eso sea verdad."
    call BlinkXS3 ("c27s005_030") from _call_BlinkXS3_661
    emm "¡Por supuesto que ganamos nosotras!"
    call BlinkXS3 ("c27s005_035") from _call_BlinkXS3_662
    kim "¿A qué te refieres, [nor]?"
    call BlinkXS3 ("c27s005_040") from _call_BlinkXS3_663
    if nor._var("route"):
        nor "Perder aquella batalla de pintura fue el primer paso para que [mc] y yo acabáramos juntos."
        if not nor._var("routeSecondChance"):
            nor "Nos acabamos duchando juntos. Y no una ducha inocente como las que tomábamos cuando él era un niño."
            call BlinkXPS3 ("c27s005_045" , "h") from _call_BlinkXPS3_2802
            emm "¿Qué? ¿Follasteis aquel día? ¿En la ducha?"
            call BlinkXS3 ("c27s005_050") from _call_BlinkXS3_664
            nor "*Risa* No, pero aún no sé cómo conseguimos parar a tiempo. Fue muy tórrido."
        else:
            nor "Estuve a punto de meterme en la ducha con él."
            call BlinkXPS3 ("c27s005_045" , "h") from _call_BlinkXPS3_2803
            emm "¿Qué? ¿Follasteis aquel día? ¿En el baño?"
            call BlinkXS3 ("c27s005_050") from _call_BlinkXS3_665
            nor "*Risa* No, no me dejó entrar en la ducha, pero no sé qué hubiera pasado si me hubiera dejado."
    else:
        nor "Después de aquella batalla estaba buscando un sitio donde ducharme y quitarme la pintura. Encontré a [mc] en la ducha."
    nor "¿Os acordáis del pestillo roto en el baño? Creo que fui la primera en verlo desnudo desde que volvió a casa."
    call BlinkXS3 ("c27s005_055") from _call_BlinkXS3_666
    emm "Nope. *Risita* Yo lo vi el día anterior, en la ducha del gimnasio."
    emm "Y [sca] y [dap] un poco más tarde, en la piscina, mientras hacíamos una batalla de caballos."
    call BlinkXS3 ("c27s005_055b") from _call_BlinkXS3_667
    emm "Y [eri] ese mismo día, pero más tarde, también en la ducha del pestillo roto."
    emm "*Risa* Con lo que, como mínimo, fuiste la quinta, Tía [nor], dependiendo de si mi madre lo vio antes que tú."
    call BlinkXS3 ("c27s005_060") from _call_BlinkXS3_668
    mom "*Risa* Yo el día de la batalla de pintura, pero por la noche."
    mom "Todas lo visteis desnudo antes que yo."
    call BlinkXS3 ("c27s005_065") from _call_BlinkXS3_669
    kim "*Risa* Parece uno de esos juegos a los que juega [deb.nick]."
    call BlinkXS3 ("c27s005_070") from _call_BlinkXS3_670
    nor "La verdad es que pasaron cosas realmente extrañas en aquellos días después de la llegada de [mc]."
    nor "La paliza que recibió de Jack, el ex-novio de [eri]... Aunque después se la devolviera..."
    call BlinkXS3 ("c27s005_075") from _call_BlinkXS3_671
    mom "La fiesta de disfraces..."
    call BlinkXS3 ("c27s005_080") from _call_BlinkXS3_672
    emm "El juego de verdad o reto..."
    call BlinkXS3 ("c27s005_085") from _call_BlinkXS3_673
    kim "Y después pasó lo más raro. *Risa* Llegamos nosotras."
    scene c27s005_005b with dissolve
    todas "*Risa*"
    mom "Bueno, lo realmente raro fue la llegada de [sai]. *Risa* Nadie la esperaba."
    nor "*Risa* Bueno, todos la esperábamos, pero no esperábamos que fuera la novia de [mc] en Portland."
    call BlinkXS3 ("c27s005_090") from _call_BlinkXS3_674
    emm "Bueno, no era la novia exactamente, ¿no?"
    emm "Tenían una relación abierta y todo eso."
    call BlinkXS3 ("c27s005_095") from _call_BlinkXS3_675
    kim "A ver qué sorpresas nos deparan las chicas nuevas. Tengo ganas de conocerlas."
    kim "Y también tengo ganas de saber si se integrarán en la familia igual que nosotras."
    call BlinkXS3 ("c27s005_100") from _call_BlinkXS3_676
    nor "He intercambiado algunos correos con ellas, y parecen buenas chicas."
    nor "Pero hay uno de los correos que me ha sorprendido mucho. Espera que lo busco en el móvil."
    call BlinkXS3 ("c27s005_105") from _call_BlinkXS3_677
    emm "*Risa* ¿Ya son raras antes de llegar?"
    call BlinkXS3 ("c27s005_110") from _call_BlinkXS3_678
    mom "Ya sé a qué correo se refiere [nor]. Más que raro, es algo que nunca se nos hubiera ocurrido."
    call BlinkXS3 ("c27s005_115") from _call_BlinkXS3_679
    nor "Ya lo tengo. Os lo leo."
    nor "Querida Señora Marks,"
    nor "Soy [kal], una de las estudiantes que se van a alojar en su casa a partir del mes que viene."
    nor "Es mi primera experiencia viviendo en el extranjero y con chicas de otras culturas."
    nor "La universidad me ha informado de que todas las chicas somos de primer año, con lo que es posible que a ellas les pase lo mismo."
    call BlinkXS3 ("c27s005_120") from _call_BlinkXS3_680
    nor "No lo de diferentes culturas, claro, ya que ellas, por lo que tengo entendido son americanas."
    nor "Para empezar a conocernos, ya que vamos a compartir habitaciones durante al menos un año, me gustaría proponerle una idea."
    nor "Si fuera posible, nos podríamos hacer una foto cada una, y así sabríamos qué aspecto tenemos."
    nor "Para hacerlo más divertido, me gustaría proponer que fuera el mismo día a la misma hora, si fuera posible."
    nor "Así sería como si estuviéramos juntas por primera vez, aunque nos separen muchos kilómetros de distancia."
    call BlinkXS3 ("c27s005_125") from _call_BlinkXS3_681
    nor "He estado pensando en las diferencias horarias, y creo que hacerlo a las 19:00 GMT del 4 de agosto estaría bien."
    nor "De esa forma, en Estados Unidos serían entre las 11:00 y las 14:00, y las chicas no tendrían que madrugar demasiado."
    nor "Si le parece bien, por favor, reenvíe este correo a las chicas con las que compartiré casa."
    nor "Se lo enviaría yo, pero la Universidad no ha querido darme sus correos electrónicos."
    nor "Después, cada una de las que acepten hacerse la foto podemos enviárselas a usted para que nos las reenvíe al resto."
    call BlinkXS3 ("c27s005_130") from _call_BlinkXS3_682
    nor "Estoy muy emocionada por conocerla a usted y a su familia. Mi prima me ha contado cosas alucinantes."
    nor "Gracias por todo por adelantado,"
    nor "[kal] Singh"
    nor "Hace días que lo recibí y se lo mandé al resto de las chicas. El 4 de agosto es mañana. A ver cuántas responden."
    call BlinkXS3 ("c27s005_135") from _call_BlinkXS3_683
    kim "¿[kal]? Esa es la prima de [sai]."
    kim "Me hubiera gustado que la idea se nos hubiera ocurrido a nosotras antes de venir."
    kim "Aunque hubiera venido acojonada. [kat], [lis], [deb.nick], y [sai] son guapísimas..." id c27s005_PaintBasement_c04a8f0e
    call BlinkXS3 ("c27s005_140") from _call_BlinkXS3_684
    emm "*Risa* Claro, como tú eres la prima fea de Quasimodo te tendrías que preocupar por cómo son las demás."
    call BlinkXS3 ("c27s005_145") from _call_BlinkXS3_685
    mom "La belleza es subjetiva, [emm]. Puede que yo te vea muy guapa y que para otras chicas parezcas un orco..."
    call BlinkXS3 ("c27s005_150") from _call_BlinkXS3_686
    emm "¿Qué? ¿Un orco? ¿Yo?"
    call BlinkXS3 ("c27s005_155") from _call_BlinkXS3_687
    nor "*Risa* Uno orco rosa. Cambiarías la armadura por un vestidito mono... y rosa."
    scene c27s005_005b with dissolve
    todas "*Risa*"
    emm "*Risa* A veces os odio. Por suerte, soy la que tiene el mejor gusto para los colores en casa."
    emm "[kim] me cayó bien el día que llegó con aquel vestido rosa. ¿Os acordáis?"
    mom "Me encanta cómo le quedaba aquel vestido, pero no se lo he vuelto a ver puesto."
    kim "*Risa* No quiero que [emm] me lo robe. Aunque se lo puedo prestar un día."
    nor "*Risa* ¡No alimentes al orco!"
    todas "*Risa*"
    emm "*Risa* Cada vez os odio más veces."
    call BlinkXS3 ("c27s005_160") from _call_BlinkXS3_688
    emm "Cambiando de tema y hablando de otras chicas, aunque me consideren un orco. ¿Puedo hacerte una pregunta personal, Tía [nor]?"
    call BlinkXS3 ("c27s005_165") from _call_BlinkXS3_689
    nor "Claro, cielo, pregunta lo que quieras saber. Ya sabes que lo de tener secretos se nos ha dado mal."
    call BlinkXS3 ("c27s005_170") from _call_BlinkXS3_690
    emm "A ver... no es que tenga dudas, pero como tú eres más... lanzada... que mi madre..."
    emm "¿Alguna vez has tenido alguna experiencia con alguna chica?"
    call BlinkXS3 ("c27s005_175") from _call_BlinkXS3_691
    nor "*Risa* ¡Eso sí que es un cambio de tema!"
    if eri._var("route") and nor._var("route") and persistent.lesbian:
        nor "Pero sí. Tres veces, una en la universidad y otra poco después de acabar."
        nor "{i}(Espero que no se den cuenta de que falta una. No sé si [eri] querría que les dijera lo que pasó en la piscina.){/i}"
    else:
        nor "Pero sí. Dos veces, una en la universidad y otra poco después de acabar."
    call BlinkXS3 ("c27s005_180") from _call_BlinkXS3_692
    kim "¿Y cómo fue? ¿Tenías dudas sobre tu sexualidad?"
    call BlinkXS3 ("c27s005_185") from _call_BlinkXS3_693
    nor "No, cielo, nunca he tenido dudas, pero quería experimentar."
    nor "La primera vez no me gustó. La segunda fue mucho mejor."
    call BlinkXS3 ("c27s005_190") from _call_BlinkXS3_694
    emm "¡Me sorprendes mucho, Tía [nor]! Pensaba que podías haber probado, pero no repetido si no te gustó la primera vez."
    call BlinkXS3 ("c27s005_195") from _call_BlinkXS3_695
    nor "Bueno, la segunda vez fue con una persona especial. No especial en cuanto a que sintiera algo por ella, pero... especial."
    nor "Pero, ¿por qué lo preguntas?"
    call BlinkXS3 ("c27s005_200") from _call_BlinkXS3_696
    if persistent.lesbian and emm._var("route"):
        if mar._var("route"):
            emm "Por nada especial. Me he sentido tentada de experimentar en un par de ocasiones."
        elif eri._var("route") and dap._var("route"):
            emm "Por nada especial. Me he sentido tentada de experimentar en un par de ocasiones."
        else:
            emm "Por nada especial. Después de lo de los saludos con besos, me sentí tentada de experimentar."
    else:
        emm "Por nada especial. Cuando lo de los saludos con besos, pensé que experimentar podría estar bien. Después se me pasó."
    call BlinkXS3 ("c27s005_205") from _call_BlinkXS3_697
    kim "¿Y tú, [mar]? ¿Alguna experiencia?"
    call BlinkXS3 ("c27s005_210") from _call_BlinkXS3_698
    mom "*Risa* Según [emm] no soy lo suficientemente lanzada para probarlo."
    call BlinkXS3 ("c27s005_215") from _call_BlinkXS3_699
    emm "¡Mamá! Lo he dicho porque le pega más a Tía [nor]."
    call BlinkXS3 ("c27s005_220") from _call_BlinkXS3_700
    mom "Bueno, pues sí. Una vez en la universidad..."
    call BlinkXPS3 ("c27s005_215b" , "h") from _call_BlinkXPS3_2804
    emm "¿Qué?"
    if persistent.family:
        call BlinkXS3 ("c27s005_220") from _call_BlinkXS3_701
        mom "Poco después de que tu tía acabara la universidad."
        scene c27s005_225a with hpunch
        emm "¿QUÉ?" (multiple=2)
        kim "¿Vosotras dos?" (multiple=2)
        scene c27s005_225An with dissolve
        mom "*Risa*" (multiple=2)
        nor "*Risa*" (multiple=2)
        mom "Creo que deberíamos empezar a pintar o se va a hacer tarde."
        nor "Yo también creo lo mismo."
        call BlinkXS3 ("c27s005_230") from _call_BlinkXS3_702
        emm "¡No es justo! ¡Ahora quiero saber más!"
        scene c27s005_225b with dissolve
        mom "Yo creía que querías tener un estudio de fotografía."
        nor "Si no empezamos a pintar, no lo podrás tener montado para el fin de semana."
    else:
        call BlinkXS3 ("c27s005_220") from _call_BlinkXS3_703
        mom "No me gustó y no volví a repetir mientras estaba en la universidad."
        mom "Quizás es porque estábamos experimentando y no sentíamos nada la una por la otra..."
        scene c27s005_225a with dissolve
        emm "Me acabas de dejar sorprendida. No creía que hubieras probado algo así."
        kim "Yo también estoy sorprendida. No porque lo probaras, sino porque lo probaras con alguien por quién no sintieras nada."
        call BlinkXS3 ("c27s005_240") from _call_BlinkXS3_704
        mom "La universidad es un momento para experimentar. Yo no pensaba demasiado en esas cosas todavía."
        mom "A día de hoy no lo haría con nadie por quién no sintiera algo."
        scene c27s005_225b with dissolve
        mom "Pero creo que deberíamos empezar a pintar o no vamos a acabar nunca."
        nor "Estoy de acuerdo. Así estará seco para el fin de semana y [emm] podrá montar el estudio de fotografía."
    call BlinkXS3 ("c27s005_235") from _call_BlinkXS3_705
    emm "Vale, pero no es justo. Sabéis que voy a seguir preguntando por eso."
    scene c27s005_005b with dissolve
    stop music fadeout (1.5)
    todas "*Risa*"
    return
label c27s006_OmaHouse:
    if _in_replay:
        call mrS3_oma_route from _call_mrS3_oma_route_6
    scene c27s006_005a with fade
    call BlinkXS3 ("c27s006_005") from _call_BlinkXS3_706
    play music ("music/CumbiaColombiana.ogg")
    "En el apartamento de [oma]..."
    oma "Pues este es mi pasillo. Casi no se puede considerar un apartamento."
    oma "*Risa* Un pasillo con puertas a un lado."
    mc "*Risa* Pero es un pasillo muy bien arreglado para una persona."
    call BlinkXS3 ("c27s006_010") from _call_BlinkXS3_707
    oma "*Risa* El mayor problema es que puedo recordar y oler lo que cociné hace tres días cuando estoy viendo la tele."
    oma "No hay forma de que la campana se lleve todos los olores antes de que lleguen al sofá."
    mc "Si lo que cocinas está bueno..."
    call BlinkXS3 ("c27s006_015") from _call_BlinkXS3_708
    oma "No. Por muy bueno que esté, no quiero olerlo tres días después. Y abrir las ventanas no sirve de mucho."
    oma "Dan a un patio interior y entonces entran los olores de lo que cocinan los vecinos."
    mc "*Risa* Se pueden dar combinaciones horribles entonces."
    scene c27s006_015d with dissolve
    oma "Ven a mi habitación, te la enseño antes de coger los pijamas."
    mc "*Risa* ¿Has hecho la cama?"
    oma "No dormí aquí anoche, con lo que no era necesario. Pero la hago siempre que me levanto."
    scene c27s006_020d with fade
    oma "Pues esta es mi habitación. No es gran cosa pero suficiente para mí."
    oma "Al otro lado de esa pared está la habitación de invitados y detrás de ésta, el baño que también sirve de sala de la colada."
    mc "Me gustan los cuadros."
    call BlinkXS3 ("c27s006_020") from _call_BlinkXS3_709
    mc "Y ese póster de reclutamiento."
    oma "*Risa* A ti lo que te gusta es la chica."
    mc "Es mona."
    scene c27s006_020e with dissolve
    oma "Es el poster de reclutamiento que veía por todos lados cuando era adolescente."
    oma "Ver a una Latina tan mona con el uniforme me ayudó a cambiar mi idea sobre ser abogada. No es que me compare con ella, claro."
    call BlinkXS3 ("c27s006_025") from _call_BlinkXS3_710
    oma "Cuando vino a mi instituto a una de esas charlas que da la policía de vez en cuando, la idea ya estaba en mi cabeza y le pedí uno de los posters."
    oma "Su charla y las explicaciones que dio sobre cómo podía ayudar al vecindario me acabó de convencer."
    mc "Siempre pensé que la gente de esos carteles eran modelos."
    call BlinkXS3 ("c27s006_030") from _call_BlinkXS3_711
    oma "No en el caso de Esperanza. Ella es... o era... una patrullera, pero la escogieron para la campaña de reclutamiento y de relaciones públicas."
    mc "¿Has dicho 'era'...?"
    call BlinkXS3 ("c27s006_035") from _call_BlinkXS3_712
    oma "¡Oh, no! No me refiero a que haya muerto. *Risa* Me refería a que hace años de eso y a lo mejor ya es detective o sargento."
    mc "*Risa triste* Menos mal. Por un momento había pensado que..."
    call BlinkXS3 ("c27s006_040") from _call_BlinkXS3_713
    oma "Lo entiendo. Cada vez que sale alguna noticia de un policía que ha muerto en acto de servicio en cualquier parte del país mi madre me llama."
    oma "Hablamos todas las semanas por teléfono, pero cuando ve algo así en las noticias hace una video conferencia."
    mc "Quiere asegurarse de que estés bien. Y quiere verlo con sus propios ojos."
    call BlinkXS3 ("c27s006_045") from _call_BlinkXS3_714
    oma "Es exactamente eso, aunque ella no se dé cuenta. Da lo mismo si hemos hablado hoy. Si mañana muere un agente en Florida, mi madre hará una video llamada."
    mc "Es normal. Yo también lo haría. Es más, yo haría video conferencias en cada llamada."
    mc "Creo que me voy a pasar el día pegado a la cámara cuando esté en Aruba."
    scene c27s006_045d with dissolve
    oma "Te vamos a echar mucho de menos."
    mc "Y yo a vosotras. Va a ser raro estar tanto tiempo separados."
    if not oma._var("route"):
        call BlinkXS3 ("c27s006_050") from _call_BlinkXS3_715
        oma "Por suerte, aún quedan días para que te vayas."
        oma "Déjame coger los pijamas y el uniforme y vamos a casa."
        mc "Voy a cotillear tu piso un poco más y te espero al final del pasillo, en eso que llamas salón."
        call c27s006_ColombiaPics from _call_c27s006_ColombiaPics
        call c27s006_Ready from _call_c27s006_Ready
        stop music fadeout (1.5)
        return
    mc "Aunque puedes venir a verme cuando quieras o cuando puedas."
    oma "Lo he pensado. Este año aún me quedan dos semanas de vacaciones."
    mc "Pues espero que vengas a Aruba a verme, al menos parte de esas dos semanas."
    call BlinkXS3 ("c27s006_050") from _call_BlinkXS3_716
    oma "Déjame coger una cosa en el baño. Espérame aquí."
    mc "OK. ¿Tienes el uniforme y los pijamas en el baño?"
    scene c27s006_050d with dissolve
    oma "Ya te he dicho que también era la sala de lavandería. No tardo."
    call c27s006_ColombiaPics from _call_c27s006_ColombiaPics_1
    scene c27s006_060d with fade:
        yalign 1.0
        linear 5.0 yalign 0.0
    pause (4.5)
    call BlinkXS3 ("c27s006_060") from _call_BlinkXS3_717
    stop music fadeout (1.5)
    oma "Ya estoy lista."
    call addProfileImageS3 (5, "alexia_5", oma, _(": 15 - Especial"), "") from _call_addProfileImageS3_18
    return
label c27s006_ColombiaPics:
    scene c27s006_050e with fade
    mc "¿Los cuadros son de Colombia?"
    oma "*Desde el baño* Sí, me los regaló mi abuelo. No me gustan, pero me recuerdan a él, con lo que no quiero quitarlos."
    mc "Te entiendo. Creo que voy a tener fotos de todas vosotras en la casa de Aruba."
    scene c27s006_050f with fade
    mc "El salón es sorprendentemente cómodo."
    oma "*Desde el baño* Gracias. No me gusta tener demasiadas cosas, y menos en un piso tan pequeño."
    oma "*Desde el baño* Con todo lo que ahorré en decoración, compré un buen sofá."
    return
label c27s006_Ready:
    call BlinkXS3 ("c27s006_055") from _call_BlinkXS3_718
    oma "Ya estoy lista. Nos podemos ir cuando quieras."
    mc "Vamos, las chicas estarán deseando volverte a ver."
    return
label c27s006_Drive:
    scene drive_day with fade
    "Poco después volvéis a por la camioneta y sigues charlando con [oma] mientras la llevas a casa."
    "Nunca se había subido a tu camioneta y van dos veces en el mismo día."
    "Le gusta más que su viejo coche. No te sorprende."
    return
label c27s008_NoOma:
    call c27s006_Drive from _call_c27s006_Drive
    scene c27s008_1000 with fade
    "Mientras esperas que [eil] y [sca] vuelvan del café, subes a tu habitación a jugar a My Residence un rato."
    "Tienes una tórrida escena con Alejandra, la bombera Latina, que se disfraza de policía para la escena, reforzando su parecido con [oma]."
    return
label c27s006_Teaser:
    if _in_replay:
        $ mc._var("relationships", 3, "set")
        $ oma._var("route", True)
        $ eil._var("route", True)
        $ sai._var("route", True)
    scene c27s006_075a with fade
    call BlinkXS3 ("c27s006_075") from _call_BlinkXS3_719
    "Al cabo de un rato..."
    play sound ("music/doorbell1.ogg")
    "*Ding-Dong*"
    mc "¿Esperas a alguien?"
    oma "Es posible que sea mi casera."
    play music ("music/From-Above.ogg")
    mc "Inoportuna casera..."
    call BlinkXS3 ("c27s006_080") from _call_BlinkXS3_720
    oma "*Risa* Con los gritos que he estado dando, alguien podría pensar que me estaban asesinando."
    mc "*Risa* Espero que este no sea un apartamento de esos a los que no puedes traer visitas."
    call BlinkXS3 ("c27s006_085") from _call_BlinkXS3_721
    oma "No te preocupes, no lo es. Nunca cogería uno así porque no podría venir mi familia de San Diego a visitarme."
    oma "Sería bastante inutil tener una habitación de invitados si no puedo tener invitados."
    mc "No lo había pensado. *Risa* Creo que la sangre no ha vuelto a mi cerebro aún."
    scene c27s006_085d with dissolve
    oma "De todas formas no salgas y espérame aquí."
    mc "No te preocupes, no tengo ningún interés en tu casera. ¿Vas a abrirle así?"
    oma "Voy a ponerme el albornoz. Está en el baño."
    oma "También podría ser un paquete de Amazonian, pero lo esperaba para mañana. U otra cosa. En este edificio nunca puedes estar seguro de quién va a llamar a la puerta."
    scene c27s006_085e with dissolve
    "Alexia cierra la puerta corredera y te quedas solo con el póster de Esperanza."
    mcp "(Bueno, nos hemos quedado solos tú y yo. Espero que hayas disfrutado del espectáculo.)"
    "Esperanza no contesta. Te hubieras acojonado si lo hubiera hecho."
    "Escuchas voces en la puerta, casi susurros, pero no eres capaz de entender lo que dicen. Este piso tiene una acústica horrible."
    "No eres capaz ni siquiera de reconocer la voz de [oma]."
    "Pasan alrededor de cinco minutos antes de que la puerta vuelva a deslizarse."
    scene c27s006_090d with fade:
        yalign 1.0
        linear 5.0 yalign 0.0
    pause (4.5)
    call BlinkXS3 ("c27s006_090") from _call_BlinkXS3_722
    oma "Pues no, no era mi casera."
    call addProfileImageS3 (7, "alexia_7", oma, _(": 15 - Especial"), "") from _call_addProfileImageS3_19
    mc "¡Wow, [oma]! Eso es aún mejor que el disfraz de policía."
    mc "No sé cómo puedes meter el Yeti ahí dentro, parece cosa de magia."
    mc "¿Era una entrega de Amazonian con esa lencería?"
    call BlinkXS3 ("c27s006_095") from _call_BlinkXS3_723
    oma "Bueno, no era una entrega precisamente. La lencería me la regaló [emm] cuando volvisteis de Monterey. Tiene buen gusto y ha acertado con los colores."
    mc "¿Colores? Solo veo azul... Siempre he pensado que el azul te queda espectacular."
    scene c27s006_095d with dissolve
    oma "No es el único color que vas a ver hoy."
    scene c27s006_100d with fade:
        yalign 1.0
        linear 5.0 yalign 0.0
    pause (4.5)
    call BlinkXS3 ("c27s006_100") from _call_BlinkXS3_724
    eil "También tiene buen gusto para elegir el verde."
    call addProfileImageS3 (7, "eileen_7", eil, _(": 15 - Especial"), "") from _call_addProfileImageS3_20
    mc "¡Wow, [eil]! Ciertamente te queda muy vien el verde. Siempre ha sido tu color."
    mc "¿No tenías que llevar a [sca] a casa?"
    call BlinkXS3 ("c27s006_105") from _call_BlinkXS3_725
    eil "Ya lo he hecho. La entrevista ha ido bien."
    eil "Y en el camino de vuelta he recogido un paquete."
    mc "¿Qué? ¿Qué paquete? Si la lencería os la había comprado [emm]... ¿La has traído tú de casa?"
    scene c27s006_105d with dissolve
    eil "Ese paquete..."
    scene c27s006_110d with fade:
        yalign 1.0
        linear 5.0 yalign 0.0
    pause (4.5)
    call BlinkXS3 ("c27s006_110") from _call_BlinkXS3_726
    sai "El paquete soy yo. *Risa* Odio a la perra pelirroja por llamarme paquete."
    sai "Pero la adoro por haber propuesto esto. *Risa*"
    mc "¡Wow, [sai]! Uno de los paquetes más bonitos del mundo."
    scene c27s006_110e with dissolve
    mc "Sería difícil decidir qué paquete me gusta más."
    oma "¿Vas a quedarte babeando en la cama?"
    eil "¿O vas a venir a abrir tus regalos?"
    sai "Mi Pequeñín parece que quiere divertirse..."
    stop music fadeout (1.5)
    return
label c27s006_NoThreesome:
    scene c27s006_075a with fade
    call BlinkXS3 ("c27s006_075") from _call_BlinkXS3_727
    "Al cabo de un rato..."
    play music ("music/CumbiaColombiana.ogg")
    oma "Creo que deberíamos irnos a casa."
    mc "*Risa* ¿Ya te has cansado de mí? ¿No va a haber segundo round?"
    call BlinkXS3 ("c27s006_080") from _call_BlinkXS3_728
    oma "*Risa* ¡No seas tonto! ¡Nunca me cansaré de ti!"
    oma "Pero necesito descansar antes de entrar a trabajar. Si me sigues follando así voy a estar echa polvo esta noche."
    mc "Solo bromeaba. ¿Te has dado cuenta de que siempre parece que vamos con prisas?"
    if eil._var("route"):
        mc "El prado, el lago, el jacuzzi, hoy..."
    else:
        mc "El prado, el jacuzzi, hoy..."
    call BlinkXS3 ("c27s006_085") from _call_BlinkXS3_729
    oma "Un día te secuestraré toda la noche y no abriré las esposas para que no te puedas ir."
    oma "Pero solo después de cada asalto. Ya te he dicho que prefiero que tus manos recorran mi piel."
    mc "*Fingiendo sorpresa* ¡Agente Martinez! Secuestrarme sería delito... *Risa*"
    scene c27s006_085d with dissolve
    oma "¿Me denunciarías?"
    mc "Nope."
    oma "Es lo que me parecía. Ve vistiéndote que voy a preparar una bolsa con el uniforme y los pijamas."
    mc "OK, te espero al final del pasillo, en eso que llamas salón."
    call c27s006_Ready from _call_c27s006_Ready_1
    call c27s006_Drive from _call_c27s006_Drive_1
    stop music fadeout (1.5)
    return
label c27s008_Oma:
    if _in_replay:
        $ mc._var("relationsips", 1, "set")
        $ oma._var("route", True)
        call mrS3_eil_route from _call_mrS3_eil_route_7
        if eil._var("route"):
            call mrS3_sai_route from _call_mrS3_sai_route_8
        scene c27s006_060d with fade:
            yalign 1.0
            linear 5.0 yalign 0.0
        pause (4.5)
        call BlinkXS3 ("c27s006_060") from _call_BlinkXS3_730
        oma "Ya estoy lista."
    play music ("music/Bolero.ogg")
    mc "¡Wow, [oma]! ¿Vas a detenerme? No he puesto los pies encima del sofá. *Risa* ¡Lo juro!"
    call BlinkXS3("c27s008_005") from _call_BlinkXS3_731
    oma "*Risa* No me tientes. Pero una vez me pediste que te esposara."
    oma "¿Te has arrepentido?"
    mc "Nope. No me han esposado nunca, y creo que es algo que querría probar al menos una vez en la vida."
    scene c27s008_010AnBlink with dissolve
    oma "Déjame quitarme esto. Es incomodísima."
    mc "Además, seguro que nos molesta para hacer esto."
    scene c27s008_015d with dissolve
    "Te levantas del sofá, la coges entre tus brazos, y la besas con dulzura y pasión."
    "Te parece que hace siglos que no estáis juntos y, si te va a esposar, no vas a poder usar las manos."
    scene c27s008_015e with dissolve
    "Aprovechas para darles un buen uso en ese momento."
    "Ahora mismo te podrían detener por posesión de drogas. El cuerpo de [oma] es adictivo."
    call BlinkXS3("c27s008_015") from _call_BlinkXS3_732
    oma "Creo que voy a tener que detenerle, Señor."
    mc "¿Por qué? ¿De qué se me acusa, Agente?"
    scene c27s008_015f with dissolve
    oma "*Risita* Posesión de armas."
    mc "*Risa* ¡Pero ese arma no es mía, Agente!"
    call BlinkXS3("c27s008_020") from _call_BlinkXS3_733
    oma "¿Ah, no? ¿De quién es? ¿Va a decirme que no la ha visto nunca?"
    mc "No, la he visto muchas veces, pero ahora mismo es tuya."
    call BlinkXS3("c27s008_025") from _call_BlinkXS3_734
    oma "*Risa* Sabes que eso no te va a servir en un juicio, ¿verdad?"
    mc "Bueno, no esperaba llegar a juicio. *Guiño* Esperaba que pudiéramos llegar a algún tipo de acuerdo extrajudicial."
    call BlinkXS3("c27s008_030") from _call_BlinkXS3_735
    oma "¿Está intentando sobornarme, Sr. Marks?"
    mc "No, Agente. Nunca haría algo así..."
    mc "Además, lo de la posesión de armas es sólo una sospecha hasta que me registre, ¿no?"
    scene c27s008_035a with hpunch
    call BlinkXS3("c27s008_035") from _call_BlinkXS3_736
    oma "¡Las manos contra la pared!"
    mc "*Risa* Esto se pone interesante."
    call BlinkXS3("c27s008_040") from _call_BlinkXS3_737
    oma "Tiene derecho a guardar silencio."
    oma "Cualquier cosa que diga puede y será usada en su contra en un tribunal."
    mc "*Risa* Creía que ibas a buscar armas más abajo."
    call BlinkXS3("c27s008_045") from _call_BlinkXS3_738
    oma "Tiene el derecho a contar con un abogado."
    oma "Si no puede pagar un abogado, se le proporcionará uno de oficio."
    mc "La abogada que me hubiera gustado tener se acabó metiendo a policía."
    call BlinkXS3("c27s008_050") from _call_BlinkXS3_739
    oma "¡Y aquí aparece el arma que estaba buscando!"
    oma "No sé si calificarla como arma de gran calibre o de destrucción masiva..."
    mc "¿Por qué no los dos?"
    call BlinkXS3("c27s008_055") from _call_BlinkXS3_740
    oma "Creo que me lo voy a llevar detenido. Sígueme a la sala de interrogatorios para ser esposado."
    mc "*Risa* Espero que no le digas eso a los delincuentes de verdad y los esposes antes."
    scene c27s008_055d with dissolve
    oma "*Risa* Por norma ellos no quieren ser esposados. No es tu caso."
    oma "Sé que tú me vas a seguir."
    mc "Me conoces demasiado bien."
    scene c27s008_055e with fade
    oma "¿Qué tal?"
    mc "*Risa* Esperaba unas esposas de la policía."
    call BlinkXS3("c27s008_060") from _call_BlinkXS3_741
    oma "Esas seguramente te acabarían haciendo daño. ¿Son incómodas?"
    mc "No, los grilletes no son incómodos, pero la posición a la que me obliga la cadena sí que lo es."
    scene c27s008_060d with dissolve
    oma "Espera un segundo..."
    mc "Con estas vistas, puedes tomarte todo el tiempo que quieras. *Risa*"
    scene c27s008_060e with dissolve
    oma "Ya está..."
    mc "¿Sin cadena?"
    call BlinkXS3("c27s008_065") from _call_BlinkXS3_742
    oma "Has dicho que era incómodo. Haz como si estuviera ahí. Los grilletes los sigues llevando, con lo que la sensación será parecida."
    mc "Ummm... me gusta la idea. Más juego de rol todavía..."
    call BlinkXS3("c27s008_070") from _call_BlinkXS3_743
    oma "¿Quién ha dicho que fuera un juego de rol?"
    oma "Ahora, quédate ahí... encadenado... mientras te torturo para sacarte información."
    mc "Creía que la tortura estaba prohibida por la Convención de Ginebra, o la de Vodka..."
    scene c27s008_070d with dissolve
    oma "*Risa* No creo que la Convención de Ginebra diga nada de las detenciones policiales."
    oma "De todas formas, a nadie se le ocurrió poner ESTE TIPO de tortura en la Convención."
    mc "No me extraña... Seguramente si hubieran pensado en ello tampoco la hubieran prohibido..."
    scene c27s008_075AnBlink with dissolve
    oma "Seguramente no pensaban en este tipo de botas tampoco. Más bien en botas de soldados."
    mc "Con lo que un paso importante es eliminar esas botas."
    scene c27s008_080AnBlink with dissolve
    mc "¿También te quitas los guantes?"
    oma "Prefiero tener mi sentido del tacto intacto para poder manipular ese arma de gran calibre."
    mc "Me parece una muy buena razón para hacerlo."
    scene c27s008_085AnBlink with dissolve
    mc "Con la desaparición de ese cinturón, la cosa se está poniendo más interesante todavía."
    oma "¿No era lo suficientemente interesante para ti?"
    mc "*Risa* Por supuesto que lo era. Por eso he dicho 'todavía'."
    scene c27s008_090AnBlink with dissolve
    oma "*Risa* Entonces no me daré por ofendida."
    mc "Nunca querría ofenderte. Y menos aún cuando estoy indefenso, 'encadenado' a la cama."
    scene c27s008_095AnBlink with dissolve
    oma "Como puedes ver, yo no voy armada. No tengo dónde esconder un arma."
    mc "Déjame estar en desacuerdo. *Risa* En el Yeti se podrían esconder un par de tanques."
    scene c27s008_100d with hpunch
    oma "*Risa* ¡[mc]!"
    mc "Y esa sonrisa podría desarmar a ejércitos enteros."
    call BlinkXS3("c27s008_100") from _call_BlinkXS3_744
    oma "Eso me gusta más. ¿Qué tal la tortura hasta ahora?"
    mc "Las vistas son increíbles, pero esto de estar 'encadenado' y no poder usar las manos..."
    call BlinkXS3("c27s008_105") from _call_BlinkXS3_745
    oma "*Risa* Te he quitado la cadena, pero no voy a dejarte usar las manos o la tortura perdería efectividad."
    mc "Bueno, parece que ahora va a empezar una parte de la tortura que me va a gustar."
    mc "Aunque sabes que esto de estar pasivo no es lo mío..."
    oma "Calla y disfruta."
    scene c27s008_925pv with dissolve
    show c27s008_925v
    "La preciosa policía se mete a Mjolnir en la boca. Por suerte, los cargos son falsos y realmente no es un arma de fuego."
    "El pequeño striptease te ha puesto muy cachondo, sabiendo lo que vendría a continuación. O al menos imaginándolo."
    oma "*Gemido*"
    "Descubres que a ella la ha puesto tan cachonda como a ti en el momento en que empieza a gemir con tu polla entre sus labios."
    "Aún recuerdas la primera vez que [oma] te chupó la polla, en aquel prado. Ya no hay rastros de dientes en sus mamadas."
    scene c27s008_920pv with dissolve
    show c27s008_920v
    hide c27s008_925v
    "Su mirada recorre tu cuerpo de tu polla a tus ojos, dándole a la mamada un punto extra de morbo, sabiendo que estás 'encadenado'."
    "Te dan ganas de dejar el juego y acariciar su cara mientras su boca sube y baja a lo largo de tu astil, pero [oma] parecía más emocionada por el juego que tú."
    oma "*Jadeo*"
    "No quieres romper la magia del momento. No quieres interrumpir la increíble mamada que te está haciendo ni su fantasía de tenerte encadenado."
    "Quizás un día puedas encadenarla tu a ella. Encadenarla a ti, claro. Sus habilidades bucales están haciendo que te acerques peligrosamente a tu orgasmo."
    mc "Si sigues así me voy a correr, cielo."
    call BlinkXS3("c27s008_110") from _call_BlinkXS3_746
    oma "Ese es el objetivo. ¿Tienes algo mejor que hacer?"
    mc "Se me ocurren varias cosas..."
    oma "Habrá tiempo para eso. No tengo nada planeado hasta la hora de la cena."
    scene c27s008_930pv with dissolve
    show c27s008_930v
    hide c27s008_920v
    "[oma] continúa con la maravillosa mamada. Definitivamente no es una mujer a la que llevar la contraria."
    if oma._var("pregnant"):
        "Quizás vuestros hijos lo descuban a las malas cuando se convierta en la 'Mamá de la chancla' haciendo honor a su educación latina."
    else:
        "Si alguna vez tenéis hijos, quizás lo descubran a las malas cuando se convierta en la 'Mamá de la chancla' haciendo honor a su educación latina."
    "No te imaginas a la policía usando la chancla, pero la simple idea de verla blandiéndola acojona."
    oma "*Jadeo inquisitivo*"
    "Tus intentos de pensar en otra cosa para retrasar tu orgasmo fracasan miserablemente. Empieza a trepar por tus pantorrillas a una velocidad tremenda."
    mc "Estoy a punto de llegar..."
    "Tu frase es para [oma] como si escuchase llover. No te hace ni caso y sigue con su memorable mamada."
    call OrgasmXS3("c27s008_115") from _call_OrgasmXS3_76
    mc "¡Mpfft!"
    "Sin poder hacer nada por evitarlo, ni querer hacerlo, descargas una gran cantidad de semen en la boca de tu novia."
    oma "*Jadeo* *Gulp* *Gulp*"
    stop music fadeout (1.5)
    "Pese a sus esfuerzos por tragarlo todo, algo de tu semilla se escapa entre sus labios."
    scene c27s008_120AnBlink with dissolve
    play music ("music/pianomatic.ogg")
    oma "¿Contento y feliz?"
    mc "Sí y no. Sabes que me gusta que el placer sea mutuo. Pero ha sido increíblemente bueno."
    scene c27s008_125d with fade
    pause (1.5)
    call BlinkXS3("c27s008_125") from _call_BlinkXS3_747
    "Después de limpiar todo el semen que se le ha escapado..."
    if eil._var("route"):
        oma "En el bosque me llevaste tú hasta el orgasmo mientras [eil] te chupaba la polla. Era el momento de devolvértelo. Y ahora te tocará trabajar a ti."
        mc "¿Me vas a dejar volver a comerme al Yeti?"
        oma "Si creías que después de probarlo una vez no iba a repetir, creo que aún no me conoces. Ni sabes el talento que tienes para hacerlo."
    else:
        oma "No te preocupes, va a ser mutuo porque ahora te va a tocar trabajar a ti."
        mc "¿Me vas a dejar comerme al Yeti?"
        oma "Después de todo lo bueno que me han dicho [sai] y [eil] sobre tu lengua, creo que estoy preparada para probarlo."
    mc "Entonces ven aquí arriba... aún estoy encadenado, ¿no?"
    call BlinkXS3("c27s008_130") from _call_BlinkXS3_748
    oma "*Risa* ¡Por supuesto que estás encadenado! No dejarás de estarlo hasta que te lo diga."
    mc "*Risa* No me arriesgaré a que saques 'la chancla'. Voy a seguir encadenado."
    call BlinkXS3("c27s008_135") from _call_BlinkXS3_749
    oma "*Risa* ¿'La chancla'? ¡Esa es el arma de destrucción masiva que usan las madres latinas!"
    oma "Aún le tengo miedo a la chancla de mi madre."
    if oma._var("route") or mc._var("wantsChildren"):
        mc "Y vas a ser una madre latina preciosa. Y temible con 'la chancla'."
    else:
        mc "Y, si alguna vez tenemos hijos, vas a ser una madre latina preciosa. Y temible con 'la chancla'."
    call BlinkXS3("c27s008_140a") from _call_BlinkXS3_750
    oma "*Risa* No me digas que 'la chancla' es lo primero que aprendes en español."
    mc "No, también sé decir *Con acento español* 'jalapeños', 'chorizo' y 'croquetas'. Esas son difíciles."
    mc "Y Yeti. *Risa* Se me da bien decir cosas que se pueden comer."
    call BlinkXS3("c27s008_140b") from _call_BlinkXS3_751
    oma "Yeti se dice igual..."
    mc "Pues en vez de decirlo, tendré que probarlo. Ven aquí."
    scene c27s008_145d with fade
    oma "*Risa* Estás loco... Pero no hace falta que me lo digas dos veces."
    mc "¿Hace falta que diga que estoy loco por ti?"
    call BlinkXS3("c27s008_145") from _call_BlinkXS3_752
    oma "No hace falta que lo digas, pero me gusta oírlo."
    mc "Estoy loco por ti."
    mcp "(Estoy tan loco que no me sorprendería si el Yeti dijera 'Eres un mago, [mc]'.)" #Yer a wizard, [mc]
    stop music fadeout (1.5)
    oma "Y yo por ti."
    scene c27s008_945pv with dissolve
    show c27s008_945v
    hide c27s008_930v
    play music ("music/Bolero.ogg")
    "No hace falta que digas nada más antes de hundir tu lengua en el centro del Yeti, como un dulce puñal buscando su humedad."
    if eil._var("route"):
        "Parece que el trío en el lago derribó todas sus barreras mentales sobre ser comida. No vas a dejar que las vuelva a erigir nunca."
    else:
        "Parece que [eil], [sai], y [oma] hablaron de ti anoche cuando compartieron cama."
        "Si derribar las barreras mentales que [oma] tenía sobre ser comida es el premio, estrechar lazos entre ellas no es el único efecto positivo."
    oma "*Gemido* ¡Oh, sí! *Jadeo* ¡Eso es fantástico! *Gemido*"
    oma "*Jadeo* Ni siquiera me importa que uses las manos. *Gemido*"
    "Si te dieran una medalla cada vez que te han dicho eso, seguramente tendrías una desviación en la columna vertebral."
    "Nunca has entendido cómo hay tantos hombres malos en esto. Sólo hay que 'escuchar' al cuerpo de la mujer y darle lo que pide, sin prisas."
    scene c27s008_950pv with dissolve
    show c27s008_950v
    hide c27s008_945v
    "Ayuda mucho que ella se haya puesto cachondísima durante la mamada. Cualquier roce de tu lengua hace que su cuerpo se estremezca."
    if eil._var("route"):
        oma "*Gemido* Esto es mejor de lo que recordaba. *Jadeo* Te voy a esclavizar. *Gemido*"
    else:
        oma "*Gemido* Esto es mejor de lo que me habían dicho. *Jadeo* Te voy a esclavizar. *Gemido*"
    "No sería un mal sitio en el que pasar una condena a esclavitud. Al menos no pasarías frío en invierno con tanto pelo."
    oma "*GEMIDO* ¡Por Cristo Señor mío! *JADEO* Si sigues así, me voy a correr. *GEMIDO*"
    "Su coño, cada vez más húmedo, y no solo por tu saliva, te indica que la preciosa policía no te está mintiendo."
    scene c27s008_940pv with dissolve
    show c27s008_940v
    hide c27s008_950v
    "Tus caderas empiezan a moverse por sí solas, buscando penetrar lo que tu lengua está acariciando."
    oma "*JADEO* ¡SIGUE ASÍ! *GEMIDO* ¡ME TIEMBLAN LAS PIERNAS! *JADEO*"
    "El cuerpo de [oma] empieza a moverse cada vez más espasmódicamente, cada vez más tenso, indicándote que no va a tardar mucho en llegar a su clímax."
    "Aceleras los movimientos de tu lengua intentando que su orgasmo sea intenso."
    if not eil._var("route"):
        "Quieres demostrarle que no eres de los que se asustan por un poco de pelo. Aquella vez en el prado no te dejó comértela por sus experiencias anteriores."
    "Quieres que recupere las ocasiones perdidas en las que no ha dejado que nadie devore al Yeti."
    "¿Son los Yetis cazadores o presas? En este caso, lo tienes muy claro."
    call OrgasmXS3("c27s008_150") from _call_OrgasmXS3_77
    oma "*GEMIDO* ¡ME CORROOOO! *JADEO*"
    "Tu boca es inundada por una explosión de intenso sabor cuando los fluidos de [oma] surgen como un géiser."
    oma "*JADEO* ¡MIS PIERNAS NO ME AGUANTAN! *GEMIDO*"
    "Tras liberar la tensión acumulada, su cuerpo se va convirtiendo poco a poco en gelatina, sin fuerzas para más."
    scene c27s008_935pv with fade
    show c27s008_935v
    hide c27s008_940v
    "La preciosa mujer descabalga tu boca se tumba a tu lado acariciándose para prolongar las sensaciones que recorren su cuerpo."
    "Es una visión de la que dudas que alguna vez te canses. Hay pocos momentos en los que [oma] esté más guapa que cuando está disfrutando de los últimos coletazos de su orgasmo."
    oma "*Gemido* ¿Vas a quedarte ahí? *Jadeo* ¿No vas a abrazarme? *Gemido*"
    "La hipnótica visión de la hermosa mujer recorriendo su cuerpo con sus manos te ha hecho olvidar que no estás realmente encadenado."
    mc "Me parece recordar que estoy 'encadenado'. Alguien me ha dicho que me comporte como si lo estuviera hasta que me digan lo contrario."
    "Consigues alargar la visión unos segundos antes de contestar. La visión es buena. Los abrazos son mejores."
    oma "*Jadeo* Te libero de tus cadenas... *Gemido* Al menos por un rato... *Jadeo*"
    stop music fadeout (1.5)
    scene c27s008_155d with fade
    "Abrazas fuertemente a la hermosa policía. Puedes notar cada uno de sus latidos contra tu pecho, cada uno de sus jadeos en tu cuello."
    play music ("music/CumbiaColombiana.ogg")
    "Introduces un muslo entre los suyos, presionando contra el Yeti para alargar su placer."
    oma "*Gemido* Eso ha sido increíble. *Jadeo* Pero esto es lo mejor. *Gemido*"
    "No puedes negar que abrazar a alguien como [oma] después de que haya tenido un intenso orgasmo está entre las mejores sensaciones del mundo."
    if eil._var("route"):
        oma "Le tengo que comprar algo a [eil] como agradecimiento por haberme convencido de esto."
    else:
        oma "Les tengo que comprar algo a [eil] y a [sai] como agradecimiento por haberme convencido de esto."
    mc "*Risa* Creo que se darán por agradecidas si les cuentas cómo te sientes ahora mismo."
    mc "Bueno, eso si comparáis notas sobre mí, claro."
    scene c27s008_155e with hpunch
    oma "*Risa* ¡No me hagas reír ahora!"
    mc "*Risa* Me temo que eso significa que comparáis notas."
    call BlinkXS3("c27s008_155") from _call_BlinkXS3_753
    oma "Bueno... sí. Con [eil] es fácil de hacer. Desde aquel día en el lago me ha estado dando consejos. Es la que mejor te conoce en la cama."
    oma "[sai] también te conoce muy bien, pero incluso ella se ha sorprendido con alguna de las cosas que ha dicho [eil]."
    if not sai._var("route"):
        oma "Además, no está tan cómoda hablando de ti como [eil]. Ya sabes... al no volver con ella cuando vino..."
        mc "Es comprensible."
    call BlinkXS3("c27s008_160") from _call_BlinkXS3_754
    oma "Hay muy buen rollo entre las tres, pero creo que lo habría igual si tú no estuvieras en la ecuación."
    mc "*Risa* Me alegra saber que soy prescindible."
    call BlinkXS3("c27s008_165") from _call_BlinkXS3_755
    oma "*Risa* Eres muchas cosas, pero prescindible no es una de ellas."
    mc "*Risa* Eso me alegra más todavía."
    oma "Y para demostrártelo, vuelve a 'encadenarte'."
    mc "¿Qué vas a hacer ahora?"
    call BlinkXS3("c27s008_170") from _call_BlinkXS3_756
    oma "¿Qué opinas de redefinir la frase 'Que le den a la policía'?"
    mc "*Risa* Que es un giro interesante de los acontecimientos."
    "Mjolnir hace un rato que está preparado para el siguiente asalto."
    stop music fadeout (1.5)
    oma "Pues vuelve a tus cadenas. Es el momento de que le des a la policía."
    play music ("music/LePrunierenFleur.ogg")
    scene c27s008_900An with dissolve
    oma "¡Oooff!"
    "La preciosa Latina se empala en Mjolnir en un rápido movimiento que demuestra las ganas que tiene de continuar la increíble sesión de sexo."
    oma "*Gemido* ¿Estás bien ahí atrás? *Jadeo*"
    mc "Estoy genial, pero me encantaría poder tocar ese culo maravilloso ahora mismo."
    oma "Pues va a ser que no. Recuerda que estás 'encadenado'. Hoy eres mío."
    scene c27s008_915pv with dissolve
    show c27s008_915v
    hide c27s008_935v
    "[oma] no te deja protestar antes de empezar a mover su atlético y maravilloso cuerpo a lo largo de tu astil."
    oma "*Jadeo* Estoy super sensible después de lo de antes. *Gemido* Creo que me vas a hacer llegar demasiado rápido. *Jadeo*"
    "Tú apenas haces nada excepto un leve movimiento con tus caderas, pero no existe nada como 'demasiado rápido' en el caso de una mujer multiorgásmica."
    oma "*Gemido* Si no fuera tan avariciosa... *Jadeo*"
    "Te sorprende profundamente la frase de [oma]. Su generosidad está fuera de toda duda, después de asegurarse de que la tarde empezaba con tu orgasmo durante su mamada."
    scene c27s008_900pv with dissolve
    show c27s008_900v
    hide c27s008_915v
    "Además de regalarte unas vistas increíbles, aunque te niegue la posibilidad de unir el sentido del tacto al de la vista."
    mc "¿A qué te refieres?"
    "La lenta cabalgata de la hermosa mujer podría durar horas a ese ritmo si no fuera porque perderá parte de la coordinación en cuanto se corra."
    oma "*GEMIDO* [eil] me dijo que tenía que probar... *JADEO* a que me penetraras cuando estuviese a punto de llegar mientras me comías. *GEMIDO*"
    "Sabes que a [eil] siempre le ha gustado eso, con lo que no te extraña que se lo haya recomendado a su amiga. A su hermana."
    oma "*JADEO* Pero he sido avariciosa... *GEMIDO* He querido correrme en tu boca... *JADEO*"
    "Y volverá a correrse alrededor de tu polla. Por el volumen de sus gemidos, no tardará demasiado."
    mc "Tendremos miles de oportunidades de que lo pruebes."
    "Al pensar en ello, [oma] tensa sus músculos, haciendo que su vagina se cierre con fuerza sobre Mjolnir."
    scene c27s008_910pv with dissolve
    show c27s008_910v
    hide c27s008_900v
    "Su cara, que puedes ver de refilón en el espejo, refleja el placer que está sintiendo ahora mismo."
    oma "*GEMIDO* MILES DE OPORTUNIDADES... *JADEO* ME ENCANTA QUE PIENSES A LARGO PLAZO... *GEMIDO*"
    "El pausado ritmo le permite continuar moviéndose pese a que su coño está empezando a sufrir los primeros espasmos que anuncian su orgasmo."
    "A ti te queda aún un poco, pero ella está muy sensible después de que te hayas comido al Yeti."
    oma "*JADEO* ¡VOY A CORRERME! *GEMIDO* ¡NO PARES! *JADEO*"
    mc "Córrete para mí, preciosa."
    call OrgasmXS3("c27s008_175") from _call_OrgasmXS3_78
    oma "*GEMIDO* ¡SÍ! *JADEO* ¡POR EL AMOR DE DIOS! *GEMIDO*"
    "El coño de [oma] se cierra con fuerza sobre tu astil mientras oleadas orgásmicas la recorren de arriba a abajo."
    "Su cuerpo se tensa por un momento de una forma que no parece natural, aunque sea lo más natural del mundo."
    scene c27s008_905pv with dissolve
    show c27s008_905v
    hide c27s008_910v
    "Tras un momento de pausa, reanuda sus lentos movimientos mientras sus paredes vaginales se cierran alrededor de Mjolnir, estrujándolo."
    "La lentitud de éstos hace que pueda mantener el ritmo sin ningún problema pese a la tormenta orgásmica que está teniendo lugar en su coño."
    oma "*JADEO* ¡ESTO ES LO MEJOR DE TODO! *GEMIDO* ¡SIGUE FOLLÁNDOME! *JADEO*"
    "Tu límite se acerca a pasos agigantados debido a sus movimientos y a cómo su vagina se tensa alrededor de tu astil."
    mc "Estoy a punto de correrme, [oma]."
    "Sus movimientos no cesan y no muestra ninguna intención de descabalgarte."
    oma "*GEMIDO* ¡CÓRRETE DENTRO! *JADEO* ¡LLÉNAME! *GEMIDO*"
    "No tienes ningún problema en cumplir sus órdenes. Tampoco podrías haberlo evitado."
    if persistent.pregnancy and not oma._var("pregnant"):
        if persistent.walkthrough:
            $ wt1 = _("[oma] embarazada.")
            $ wt2 = _("Sin consecuencias.")
        else:
            $ wt1 = ""
            $ wt2 = ""
        menu:
            "Correrte dentro. Ir a por el bebé." (wt = wt1):
                $ oma._var("pregnant", True)
                $ oma._var("undiscoveredPregnancy", True)
                play sound ("music/OldMusicBox5.ogg")
            "Correrte dentro." (wt = wt2):
                pass
    $ resetWalkthrough ()
    call OrgasmXS3("c27s008_180") from _call_OrgasmXS3_79
    mc "¡Mpfft!"
    "Un volcán de semen entra en erupción dentro del coño de la preciosa mujer, superando su capacidad para retenerlo."
    oma "*JADEO* ¡HAY MUCHÍSIMA! *GEMIDO* ¡ESTÁ SUPER CALIENTE! *JADEO*"
    "Tu descarga provoca una nueva oleada de orgasmos que se superpone a la anterior, ordeñando hasta la última gota de tu semilla."
    call BlinkXS3("c27s008_185") from _call_BlinkXS3_757
    "Te da lo mismo que estés 'encadenado'. Abrazas desde atrás a la policía mientras los orgasmos se suceden en su cuerpo."
    oma "*GEMIDO* GRACIAS. *JADEO*"
    stop music fadeout (1.5)
    "Supones que el agradecimiento es por el abrazo. Notas como su cuerpo se desmadeja en tus brazos, relajándose tal como su último orgasmo finaliza."
    call BlinkXS3("c27s008_190") from _call_BlinkXS3_758
    play music ("music/IWonderWhatIllDoToday.ogg")
    oma "*Respiración entrecortada* Eso ha sido increíble, [mc]..."
    mc "Tú has hecho todo el trabajo."
    oma "*Respiración entrecortada* No me refiero sólo al sexo... el abrazo en el momento justo ha sido... alucinante..."
    mc "¿Pese a que me haya 'desencadenado' para hacerlo?"
    call BlinkXS3("c27s008_195") from _call_BlinkXS3_759
    oma "Pese a ello. *Risa* No usaré 'la chancla' contigo."
    "Su risa provoca que un poco más de tu semen se escape de su coño."
    mc "Creía que estaba reservada a los hijos..."
    oma "*Risa* Está reservada a cualquiera que nos lleve la contraria."
    call BlinkXS3("c27s008_200") from _call_BlinkXS3_760
    oma "Déjame bajar de aquí. Quiero mi momento mimos, mientras te miro."
    mc "Es algo en lo que nunca te voy a llevar la contraria. Y no por miedo a 'la chancla'... Al menos nunca reconoceré tenerle miedo."
    scene c27s008_205a with fade
    oma "¿Qué te ha parecido la primera vez en mi apartamento?"
    mc "Espectacular. Me ha gustado mucho, pero he descubierto que lo de los grilletes y yo no somos demasiado compatibles."
    oma "Estoy de acuerdo. Es una cosa que quería probar, pero prefiero notar tus manos sobre mi piel."
    mc "Habrá mucho tiempo para eso. ¿Tenemos tiempo para un segundo asalto sin grilletes?"
    call BlinkXS3("c27s008_210") from _call_BlinkXS3_761
    oma "Ummm... No lo sé. Seguro que tenemos tiempo antes de ir a casa a cenar, pero ahora mismo prefiero estar abrazada un rato contigo."
    if eil._var("route") and sai._var("route"):
        oma "Déjame descansar un poco antes del siguiente asalto. Ahora mismo estoy muy sensible ahí abajo."
    else:
        oma "Prefiero descansar un rato antes de ir a casa. Ahora mismo estoy muy sensible ahí abajo."
    mc "Nunca hemos tenido mucho tiempo para estar abrazados después del sexo. Es un cambio bienvenido."
    call BlinkXS3("c27s008_215") from _call_BlinkXS3_762
    oma "Al menos hoy no había riesgo de que nadie nos pillara. Es nuestra primera vez bajo techo y en una cama."
    mc "Bueno, las otras veces no nos pilló nadie."
    call BlinkXS3("c27s008_220") from _call_BlinkXS3_763
    oma "*Risa* Si quieres creer eso..."
    mc "¿Qué? ¿Quién?"
    oma "*Risa* No he dicho que nos pillaran."
    if eil._var("route"):
        call BlinkXS3("c27s008_225") from _call_BlinkXS3_764
        oma "Pero en el lago participó [eil]. No es una pillada, pero..."
        mc "Pero no estaríamos aquí si no te hubiera convencido para que siguiéramos juntos."
        call BlinkXS3("c27s008_230") from _call_BlinkXS3_765
        oma "Me sentí abrumada por un momento. Por suerte, [eil] supo darle la vuelta a la situación. Siempre le estaré agradecida por ello."
        mc "[eil] puede ser muy convincente a veces. Pero no se puede considerar que nos pillara. Participó, pero no nos pilló."
        mc "Hasta ahora no nos ha pillado nadie."
    else:
        call BlinkXS3("c27s008_225") from _call_BlinkXS3_766
        oma "Pero podrían haberlo hecho, especialmente en el jacuzzi. Fuimos un poco irresponsables."
        mc "Bueno, pero no lo hicieron. Hasta ahora no nos ha pillado nadie."
    oma "{i}(Si Tía [bet] no te ha dicho que nos vio, no seré yo quien te lo diga.){/i}" id c27s008_Oma_18acb1a5
    call BlinkXS3("c27s008_235") from _call_BlinkXS3_767
    oma "¿No te da un poco de morbo hacerlo en público, donde alguien pueda vernos?"
    mc "Le da un punto de... peligrosidad... que lo hace más excitante."
    call BlinkXS3("c27s008_240") from _call_BlinkXS3_768
    oma "Pero también me ha encantado aquí. Es como... más íntimo. Como si fueras más mío."
    mc "Aquí sólo existimos los dos. Y no puedo ser más tuyo de lo que ya lo soy."
    call BlinkXS3("c27s008_245") from _call_BlinkXS3_769
    if mc._var("relationships")>1:
        oma "Eso me encanta de ti. No importa con cuántas chicas estés. Cuando estamos juntos me haces sentir que solo estás conmigo. Que soy única."
    else:
        oma "Eso es una cosa que me encanta de estar contigo. Me haces sentir especial. Única."
    mc "Es que eres única, mi amor."
    scene c27s008_250An with dissolve
    "Pasáis un rato charlando. De vosotros y de la familia."
    "Del presente y del futuro. De tu viaje a Aruba y de lo mucho que os vais a echar de menos."
    "El tiempo pasa volando cuando tienes una preciosa Latina entre los brazos."
    "El tiempo pierde el sentido cuando tú mismo estás perdido en sus enormes ojos."
    stop music fadeout (1.5)
    return

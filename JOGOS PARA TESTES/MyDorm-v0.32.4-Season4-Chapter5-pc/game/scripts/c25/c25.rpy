label c25:
    call c25s001_Eva from _call_c25s001_Eva
    call c25s002_AmaHelo from _call_c25s002_AmaHelo
    call c25s002_IronFist from _call_c25s002_IronFist
    if kim._var("saved"):
        call c25s002_KimSaved from _call_c25s002_KimSaved
    else:
        call c25s002_NoKimSaved from _call_c25s002_NoKimSaved
    #day change Sunday
    call c25s003_MyResidence from _call_c25s003_MyResidence
    call c25s003_Yoga from _call_c25s003_Yoga
    if meg._var("route"):
        call c25s003_Meg from _call_c25s003_Meg
    else:
        call c25s003_NoMeg from _call_c25s003_NoMeg
    call c25s004_IceCream from _call_c25s004_IceCream
    call c25s004_KimDebLisaSai from _call_c25s004_KimDebLisaSai
    call c25s004_Pickles from _call_c25s004_Pickles
    call c25s004_GetMad from _call_c25s004_GetMad
    call c25s005_ZeusAtHome from _call_c25s005_ZeusAtHome
    call c25s006_AmaCuddle from _call_c25s006_AmaCuddle #Mar, Nor, Eri, Dap, Sai, Lis se unen. La cama se rompe
    if mee._var("iceCream"):
        call c25s007_iceCream from _call_c25s007_iceCream
    if mee._var("route"):
        call c25s007_MeeDate from _call_c25s007_MeeDate
    return
label c25s001_Eva:
    if _in_replay:
        call mrS3_eva_route from _call_mrS3_eva_route_6
    call BlinkXPS3 ("c25s001_010" , "f") from _call_BlinkXPS3_2052
    play music ("music/AmbientPianoStrings.ogg")
    "Al llegar a la galería de tiro, [eva] guarda la moto dentro de lo que parece un almacén vacío."
    eva "Ya estamos aquí. ¿Preparado para la clase de tiro? Hoy no será con munición de práctica."
    mc "Sí, hace días que no hemos practicado y..."
    call BlinkXPS3 ("c25s001_005" , "d") from _call_BlinkXPS3_2053
    eva "*Risa* ¡No has practicado tú! Yo practico todos los días."
    call BlinkXPS3 ("c25s001_015" , "d") from _call_BlinkXPS3_2054
    if not eva._var("route"):
        eva "Pero entiendo que has estado muy ocupado últimamente para practicar."
        mc "No he tenido tiempo ni de tumbarme a no hacer nada. Era uno de mis pasatiempos favoritos. *Risa*"
    else:
        eva "Pero entiendo que has estado muy ocupado últimamente para pasar tiempo conmigo y practicar."
        mc "[eva], siempre tendré tiempo para pasar tiempo contigo. Sea para disparar o para tumbarnos a tomar el sol sin hacer nada."
    call BlinkXPS3 ("c25s001_020" , "d") from _call_BlinkXPS3_2055
    eva "*Risa* Nunca entenderé cómo podéis desperdiciar el tiempo sin hacer nada. Aparte de aburrido... es un desperdicio enorme."
    eva "¡Hay un montón de cosas que hacer, que ver, que leer! Yo no tengo horas suficientes para hacer todo lo que me gustaría..."
    mc "Nadie las tiene, [eva]. ¿Qué te gustaría hacer?"
    call BlinkXPS3 ("c25s001_025" , "d") from _call_BlinkXPS3_2056
    eva "Hay mil cosas que me gustaría hacer, pero no hay tiempo para todo. Y menos aún para tumbarme a no hacer nada."
    eva "El otro día estaba viendo una película... la he empezado tres o cuatro veces... pero cuando matan a la madre del cervatillo... tengo que dejarlo."
    eva "Lo mismo que con la película en que muere el padre del leoncito. Me gustaría tener tiempo para acabar las dos."
    mc "Son muy buenas. Si quieres un día las acabamos de ver juntos. Te queda la mitad de cada película más o menos."
    call BlinkXPS3 ("c25s001_030" , "d") from _call_BlinkXPS3_2057
    eva "¿Te gustan esas películas? [ama] dice que son para niños... pero a mí me encantan."
    eva "Y a ella también. No le digas que te lo he dicho... La vi llorando después de lo del león."
    mc "*Risa* No te preocupes. Tu secreto está a salvo conmigo."
    call BlinkXPS3 ("c25s001_035" , "d") from _call_BlinkXPS3_2058
    eva "Vamos dentro. Ya llevamos dos minutos aquí, hablando sin hacer nada. Se te va a pasar el tiempo para entrenar."
    mc "*Risa* Estamos hablando. Eso es hacer algo."
    if eva._var("route"):
        mc "Y acabamos de planificar una cita para acabar de ver dos películas de dibujos animados."
    else:
        mc "Y acabamos de planificar ver dos películas de dibujos animados."
    call BlinkXPS3 ("c25s001_040" , "d") from _call_BlinkXPS3_2059
    eva "Vale, pero hemos venido a que entrenes con una pistola de verdad. Y es lo que vamos a hacer."
    mc "*Risa* También tienes que aprender a relajarte y a que los planes pueden cambiar sobre la marcha."
    mc "Por cierto, ¿por qué has guardado la moto en el almacén? El aparcamiento está vacío."
    call BlinkXPS3 ("c25s001_045" , "d") from _call_BlinkXPS3_2060
    eva "La primera razón es porque no quiero que cuando venga el helicóptero vea la moto y la matrícula. No sabemos qué intenciones tienen y no queremos darles pistas."
    mc "Me parece una buena razón, pero intuyo que hay una segunda razón más importante."
    call BlinkXPS3 ("c25s001_050" , "d") from _call_BlinkXPS3_2061
    eva "No más importante, pero casi. Si el piloto es torpe, no quiero que tire a mi niña al suelo."
    mc "*Risa* ¿Tu niña?"
    call BlinkXPS3 ("c25s001_055" , "d") from _call_BlinkXPS3_2062
    eva "*Risa* Mi niña, mi novia... llámala como quieras. Adoro esa moto."
    eva "Y, por cierto, felicidades. No has llorado viniendo hacia aquí."
    mc "*Risa* Ha sido intenso, pero menos de lo que esperaba."
    scene c25s001_055d with dissolve
    eva "*Risa* Entonces la próxima vez no me contendré."
    mc "*Risa* Te puedes seguir conteniendo. Por mí no lo hagas."
    call BlinkXPS3 ("c25s001_060" , "f") from _call_BlinkXPS3_2063
    eva "Bueno, aquí estamos. Disculpa el desorden, les dije que barrieran los cartuchos vacíos antes de cerrar ayer."
    eva "He dejado esas cajas de munición ahí. Espero que no la gastes toda."
    mc "¿Tanto voy a tener que disparar?"
    call BlinkXPS3 ("c25s001_065" , "d") from _call_BlinkXPS3_2064
    eva "Hoy vamos a entrenar el Taladro de Mozambique. Lo tienes que hacer seis veces." #Mozambique Drill
    mc "¿El Taladro de Mozambique?"
    scene c25s001_070AnBlink with dissolve
    eva "Dos tiros en el pecho y uno en la cabeza. Rápidamente."
    eva "¿Has visto las pelis de Jack Wick? Lo suele hacer bastante. Es una técnica muy buena para acabar con gente con chalecos antibalas."
    mc "Sí, las he visto. No parece demasiado complicado... ¿verdad?"
    call BlinkXPS3 ("c25s001_075" , "d") from _call_BlinkXPS3_2065
    eva "Hacerlo bien es más complicado de lo que parece. Porque además iré alejando el objetivo un metro cada vez que lo consigas."
    mc "OK. ¿Empezamos?"
    call BlinkXPS3 ("c25s001_080" , "f") from _call_BlinkXPS3_2066
    eva "OK. Te he traído la misma pistola con la que practicaste en el bosque."
    eva "Quería traerte una Desert Stork, pero [ama] ha dicho que sería mucho para ti. Ponte las gafas y los auriculares de protección."
    mc "Sabes que no entiendo de armas y no sé lo que es una Desert Stork, ¿verdad?"
    eva "Lo sé. Recuerda que el entrenamiento es para disparar con una sola mano. Si lo consigues hacer bien, el día que tengas que disparar con dos manos será más fácil."
    if not eva._var("route"):
        scene c25s001_080An1 with dissolve
        play sound ("music/Desert-Eagle-Gunshot.ogg")
        "Practicas durante bastante tiempo. Al principio, cuando los objetivos están cerca, es relativamente fácil."
        scene c25s001_080An2 with dissolve
        play sound ("music/Desert-Eagle-Gunshot.ogg")
        "Tal como [eva] los va alejando, se hace mucho más difícil. No sólo hacer el Taladro de Mozambique, sino acertar al objetivo."
        "Tienes que aguantar algunas miradas de desaprobación de [eva]."
        "Finalizas el entrenamiento habiendo conseguido el objetivo cuando la diana estaba a siete metros."
        call BlinkXPS3 ("c25s001_085" , "d") from _call_BlinkXPS3_2067
        "Más allá has acertado algunos disparos, pero no suficiente para los estándares de [eva]."
        eva "No ha estado mal, pero tienes que mejorar. Le diré a [ama] que te entrene en Aruba. Pon el seguro del arma y déjala en la estantería."
        mc "No sé si alguna vez me voy a enfrentar con alguien a tiros a esa distancia... o a alguna en realidad."
        call BlinkXPS3 ("c25s001_090" , "d") from _call_BlinkXPS3_2068
        eva "Es mejor que estés preparado por si lo tienes que hacer. Pero no hay tiempo para más."
        eva "Estoy escuchando la furgoneta de [ama] en el aparcamiento."
        mc "¿Hemos acabado entonces?"
        scene c25s001_090d with dissolve
        eva "Sí. No creo que tengamos muchas más oportunidades de entrenar antes de que os vayáis a Aruba."
        eva "Yo sí que te entrenaré allí. Me dará lo mismo que estés ocupado."
        mc "[eva]..."
        call BlinkXPS3 ("c25s001_095" , "d") from _call_BlinkXPS3_2069
        eva "Dime."
        mc "Gracias. Por el entrenamiento y por todo."
        call BlinkXPS3 ("c25s001_100" , "h") from _call_BlinkXPS3_2070
        eva "No hay de qué. Aunque me hayas hecho perder una apuesta."
        mc "¿Qué apuesta?"
        eva "Le había dicho a [ama] que no lo conseguirías pasados los seis metros."
        eva "Estoy orgullosa de ti."
        scene c25s001_090d with dissolve
        eva "Espera a que [ama] te traiga el traje. Puedes ducharte si quieres. Hay una ducha en la oficina."
        eva "Voy al lavabo mientras tanto. Deja el arma ahí y lo recogeré todo yo cuando os vayáis."
        scene c25s001_090e with dissolve
        "Y tras eso, tu entrenadora personal desaparece."
        stop music fadeout (1.5)
        return
    call BlinkXPS3 ("c25s001_105a" , "d") from _call_BlinkXPS3_2071
    eva "Bueno, puedes ir practicando mientras me cambio de ropa."
    mc "¿Te vas a cambiar?"
    scene c25s001_090d with dissolve
    eva "Sí. Para hacer el entrenamiento más interesante, vamos a jugar a un juego."
    mc "¿Qué juego?"
    eva "Ya lo verás. No seas impaciente."
    scene c25s001_090e with dissolve
    "Tras eso, desaparece."
    "Aprovechas los minutos en los que [eva] no está para recordar el tacto del arma. No quieres hacer ningún disparo antes de que ella vuelva."
    stop music fadeout (1.5)
    call BlinkXPS3 ("c25s001_105b" , "f") from _call_BlinkXPS3_2072
    eva "Ya estoy aquí de nuevo. Podemos empezar."
    play music ("music/AnxiousMarch.ogg")
    mc "¿Y ese cambio de ropa? A mí me parecía que estabas bien vestida para disparar."
    call BlinkXPS3 ("c25s001_110" , "d") from _call_BlinkXPS3_2073
    eva "*Risa* El que disparará eres tú, no yo. Pero voy a darte un incentivo."
    eva "Jugaremos a strip shooting. Cada vez que lo consigas, me quitaré una prenda de ropa. Con el otro traje duraría muy poco."
    mc "*Risa* Me parece muy interesante..."
    call BlinkXPS3 ("c25s001_115" , "d") from _call_BlinkXPS3_2074
    eva "Si lo consigues a la primera en cada distancia, además te llevarás un beso."
    mc "*Risa* Eso me parece más interesante todavía. ¿Empezamos?"
    scene c25s001_955pv with dissolve
    show c25s001_955v
    eva "*Risita* Y si aciertas en el centro, ya sea en el pecho o en la cabeza, a lo mejor te hago un baile..."
    mc "*Risa* Sin presión, ¿verdad?"
    eva "*Risa* Si alguna vez estás en un tiroteo de verdad, vas a tener mucha presión. *Risa* Te tengo que entrenar para que aciertes bajo presión o no serviría de nada."
    scene c25s001_120An1 with dissolve
    play sound ("music/Desert-Eagle-Gunshot.ogg")
    "La primera ronda, a cinco metros de distancia, es fácil. Lo consigues al segundo intento."
    "Pierdes el beso, pero te has ganado el baile. Has acertado en el centro en el cuarto y el sexto disparo."
    "Pones el seguro del arma antes de dejarla en la estantería, tal como [eva] te ha indicado."
    call BlinkXPS3 ("c25s001_125" , "d") from _call_BlinkXPS3_2075
    eva "Bien hecho. Te has ganado que me quite una prenda."
    mc "¡Las zapatillas no! *Risa* ¡Es injusto!"
    scene c25s001_125d with dissolve
    eva "*Risa* Si no las contamos como prenda, creo que el entrenamiento duraría muy poco. Y la diana estaba muy cerca. Creo que es premio suficiente."
    mc "Pero el baile sí que lo voy a tener, ¿verdad?"
    scene c25s001_960pv with dissolve
    show c25s001_960v
    hide c25s001_955v
    eva "Por supuesto. Has tenido dos aciertos."
    mc "Mi imaginación me está poniendo más presión aún. Te estoy imaginando haciendo eso sin ropa."
    eva "*Risita* Tan solo tienes que seguir acertando en el centro... "
    scene c25s001_120An2 with dissolve
    play sound ("music/Desert-Eagle-Gunshot.ogg")
    "[eva] aleja la diana a seis metros y vuelves a disparar."
    "Lo consigues a la primera y un acierto en el centro de la cabeza."
    call BlinkXPS3 ("c25s001_130" , "d") from _call_BlinkXPS3_2076
    eva "¡Bien hecho!"
    mc "¡Quiero mi beso!"
    eva "*Risa* Te lo has ganado esta vez."
    scene c25s001_130d with dissolve
    "[eva] se acerca a darte tu recompensa. Como ha dicho, es un gran incentivo."
    call BlinkXPS3 ("c25s001_135a" , "d") from _call_BlinkXPS3_2077
    mc "Y ahora quiero mi prenda y mi baile."
    eva "*Risa* Sobre el baile te he dicho a lo mejor..."
    mc "Pero estás deseando hacerlo, ¿verdad?"
    eva "*Risa* Creo que me conoces demasiado..."
    scene c25s001_135An with dissolve
    eva "Pero vamos a empezar pagando con esta camiseta..."
    mc "Me gusta la idea..."
    call BlinkXPS3 ("c25s001_135b" , "d") from _call_BlinkXPS3_2078
    scene c25s001_965pv with dissolve
    show c25s001_965v
    hide c25s001_960v
    eva "*Risa* ¿Contento con el baile?"
    "Ponerse un sujetador con volantes y hacer eso casi se podría considerar trampa. Hace parecer que sus tetas se mueven más de lo que lo hacen en realidad."
    mc "*Risa* Sí, aunque eso añade más presión todavía a los siete metros."
    eva "*Risa* Eso sólo quiere decir que el entrenamiento será mejor."
    mc "*Risa* Dudo que pueda ser mejor que esto."
    scene c25s001_120An3 with dissolve
    play sound ("music/Desert-Eagle-Gunshot.ogg")
    "[eva] aleja la diana a siete metros y vuelves a disparar."
    "Consigues hacer el Taladro de Mozambique al tercer intento y un acierto en el centro del pecho."
    "No va a haber beso esta vez."
    call BlinkXPS3 ("c25s001_140" , "d") from _call_BlinkXPS3_2079
    mc "Prenda y baile..."
    eva "No hay beso esta vez."
    mc "Lo sé..."
    call BlinkXPS3 ("c25s001_145" , "d") from _call_BlinkXPS3_2080
    eva "Suenas decepcionado."
    mc "Me gusta besarte..."
    scene c25s001_145d with dissolve
    eva "¿Te alegraría un poco si esta vez te dejo que seas tú quien me quite la prenda? Van a ser los shorts..."
    mc "*Risa* Sabes cómo alegrar a un hombre."
    scene c25s001_145An with dissolve
    eva "Sólo hay un hombre al que quiera alegrar."
    mc "*Risa* No me refería a eso, pero me alegra ser ese hombre."
    call BlinkXPS3 ("c25s001_150" , "d") from _call_BlinkXPS3_2081
    eva "*Risa* ¿De dónde has sacado que me refiera a ti? Me refería a... Jamaal..."
    mc "*Risa* Vale, me lo he ganado."
    eva "Y ahora vuelve a tu posición, déjame espacio para mi baile."
    scene c25s001_970pv with dissolve
    show c25s001_970v
    hide c25s001_965v
    "La preciosa mercenaria empieza a mover su culo sensualmente. Sigues pensando lo mismo sobre los volantes que hace unos minutos."
    eva "¿Te gusta lo que ves?"
    mc "Mucho."
    eva "Si sigues acertando me lo tendré que quitar..."
    mc "*Risa* Ahora tengo la duda de si seguir disparando o seguir mirando."
    call BlinkXPS3 ("c25s001_155" , "d") from _call_BlinkXPS3_2082
    call addProfileImageS3 (7, "eva_7", eva, _(": 15 - Especial"), "") from _call_addProfileImageS3_11
    eva "Seguir disparando. Esto sigue siendo un entrenamiento."
    mc "¡Ohhh! ¿Si pongo ojos de cachorrito me dejarás mirar un rato más?"
    call BlinkXPS3 ("c25s001_160" , "d") from _call_BlinkXPS3_2083
    eva "No."
    mc "Eres una maestra demasiado estricta. *Risa*"
    eva "Si perdemos tiempo en esto, no te va a dar tiempo a acabar. Ahora vienen los ocho metros."
    "Cambias la distancia a ocho metros sin esperar que lo haga [eva]."
    scene c25s001_120An4 with dissolve
    play sound ("music/Desert-Eagle-Gunshot.ogg")
    "La distancia parece que es demasiado para tus habilidades. En cada ronda de tres disparos aciertas uno o dos, pero nunca los tres."
    call BlinkXPS3 ("c25s001_165" , "d") from _call_BlinkXPS3_2084
    eva "¿Está muy lejos para ti? ¿O no quieres seguir con el striptease?"
    mc "*Risa* Creo que es la primera opción. Ocho metros es demasiado, aunque he acertado al menos un disparo en cada ronda."
    call BlinkXPS3 ("c25s001_170" , "d") from _call_BlinkXPS3_2085
    eva "¿Qué tal si te doy un incentivo, aunque no te lo hayas ganado?"
    mc "¿Otra prenda?"
    eva "No."
    stop music fadeout (1.5)
    eva "Me refiero a esto."
    play music ("music/Bolero.ogg")
    scene c25s001_975pv with dissolve
    show c25s001_975v
    hide c25s001_970v
    "[eva] se lanza a tus labios con una ansiedad que no ha demostrado en ninguna de las veces que os habéis besado anteriormente."
    "Parece que el juego de bailes y striptease ha hecho que tenga ganas de más. Igual que tú."
    "Sus labios aprisionan los tuyos en una batalla que los dos ganáis. Su lengua lucha con la tuya. Vuestros alientos se entremezclan."
    scene c25s001_175a with dissolve
    "Sin dejar de besarte, la preciosa pelirroja alarga la mano para coger la pistola."
    scene c25s001_175An with dissolve
    play sound ("music/Desert-Eagle-Gunshot.ogg")
    "*Bang*"
    scene c25s001_175An with dissolve
    play sound ("music/Desert-Eagle-Gunshot.ogg")
    "*Bang*"
    scene c25s001_175An with dissolve
    play sound ("music/Desert-Eagle-Gunshot.ogg")
    "*Bang*"
    "Dispara tres veces en rápida sucesión sin ni siquiera mirar a la diana."
    "No necesitas mirar para saber que ha acertado todos los disparos. Ni siquiera te importa si lo ha hecho."
    call BlinkXPS3 ("c25s001_180" , "d") from _call_BlinkXPS3_2086
    "La hermosa pelirroja interrumpe el beso y te mira con una pícara sonrisa."
    eva "Creo que me he ganado una prenda."
    mc "Creía que era yo el que se las había ganado."
    eva "*Risa* He disparado yo."
    mc "*Risa* Demuéstralo."
    call BlinkXPS3 ("c25s001_185" , "d") from _call_BlinkXPS3_2087
    eva "*Risa* Te propongo un trato. Todas tus prendas por todas las mías."
    mc "*Risa* Me parece un trato justo. Aunque eso acabará los incentivos para el entrenamiento."
    call BlinkXPS3 ("c25s001_190a" , "d") from _call_BlinkXPS3_2088
    eva "*Risa* Que le jodan al entrenamiento. La ropa me quema sobre la piel. Y seguro que empezabas a pagar prenda con las putas botas."
    mc "*Risa* ¡Ese lenguaje! ¡No estamos en un cuartel!"
    call BlinkXPS3 ("c25s001_190b" , "d") from _call_BlinkXPS3_2089
    eva "*Risa* Tienes suerte de que no estemos en un cuartel o ahora mismo estarías haciendo flexiones."
    eva "Desnúdate. ¡Ya!"
    scene c25s001_190a with dissolve
    eva "Y no mires."
    scene c25s001_190b with dissolve
    "Te sorprende que ahora se vuelva tímida después de como se ha estado comportando, pero puedes esperar un poco para verla desnuda."
    "Conociendo el fuego que la recorre, esperabas que os estuvierais arrancando la ropa mutuamente."
    "Acabas de desnudarte y te quedas mirando en dirección opuesta a ella."
    "Unos eternos segundos."
    eva "Ya puedes girarte."
    scene c25s001_195d with fade:
        yalign 1.0
        linear 5.0 yalign 0.0
    pause (5.0)
    call BlinkXPS3 ("c25s001_195" , "d") from _call_BlinkXPS3_2090
    mc "¡Wow!"
    call addProfileImageS3 (8, "eva_8", eva, _(": 15 - Especial"), "") from _call_addProfileImageS3_12
    eva "¿Te gusta lo que ves?"
    if dap._var("route") and eri._var("route"):
        call BlinkXPS3 ("c25s001_200" , "d") from _call_BlinkXPS3_2091
        eva "¡Qué tontería acabo de decir! ¡Ya has visto a [dap] y a [eri]!"
        if persistent.family:
            mc "Eso no importa. Aunque seas su clon, eres completamente distinta."
        else:
            mc "Eso no importa. Aunque sean tus clones, eres completamente distinta."
    elif dap._var("route"):
        call BlinkXPS3 ("c25s001_200" , "d") from _call_BlinkXPS3_2092
        eva "¡Qué tontería acabo de decir! ¡Ya has visto a [dap]!"
        if persistent.family:
            mc "Eso no importa. Aunque seas su clon, eres completamente distinta."
        else:
            mc "Eso no importa. Aunque sea tu clon, eres completamente distinta."
    elif eri._var("route"):
        call BlinkXPS3 ("c25s001_200" , "d") from _call_BlinkXPS3_2093
        eva "¡Qué tontería acabo de decir! ¡Ya has visto a [eri]!"
        if persistent.family:
            mc "Eso no importa. Aunque seas su clon, eres completamente distinta."
        else:
            mc "Eso no importa. Aunque sea tu clon, eres completamente distinta."
    mc "Me encanta verte así por primera vez."
    call BlinkXPS3 ("c25s001_205" , "d") from _call_BlinkXPS3_2094
    eva "¿Sólo la primera vez? *Risita* ¿Tan rápido te vas a cansar de mí?"
    mc "No me cansaré nunca ti, sabes que no quería decir eso."
    mc "*Risa* Además, creo que sería un deporte de riesgo. Y más aún en un sitio con tanta munición como este."
    call BlinkXPS3 ("c25s001_210" , "d") from _call_BlinkXPS3_2095
    eva "*Risa* Lo de hacerme reír... ¿es alguna táctica para que deje de estar nerviosa? Porque está funcionando."
    mc "Lo de hacerte reír es porque me encanta cómo suena tu risa, incluso cuando te ríes de mí."
    "Abres los brazos, invitándola a un abrazo."
    mc "Ven aquí."
    call BlinkXPS3 ("c25s001_215" , "d") from _call_BlinkXPS3_2096
    eva "Gracias. Esto es una de las cosas que más me gusta de estar contigo."
    eva "Ya me gustaba antes de estar contigo, pero ahora son especiales."
    mc "No hace falta que me des las gracias. Abrazarte me gusta casi tanto como besarte."
    call BlinkXPS3 ("c25s001_220" , "d") from _call_BlinkXPS3_2097
    eva "¿Cómo sigue ahora? ¿Te tengo que decir 'hazme el amor' o algo así?"
    mc "No hay una forma correcta o incorrecta de continuar. Tan solo tenemos que esperar a que estés lista para seguir."
    stop music fadeout (1.5)
    eva "Ya lo estoy..."
    play music ("music/KindofGirl.ogg")
    scene c25s001_225An with dissolve
    "Levantas a la preciosa pelirroja y la sientas en la estantería en la que hace un momento estaba la pistola."
    "Su culo tira la pistola al suelo. Por suerte, a ella no hay que recordarle que ponga el seguro después de disparar."
    call BlinkXPS3 ("c25s001_225" , "d") from _call_BlinkXPS3_2098
    eva "¡Hey! ¿Ahora te pones dominante?"
    mc "No, pero me acabas de decir que ya estabas lista para seguir."
    mc "*Risa* Y las dos balas que notaba perforándome el pecho me decían que tienes tantas ganas de seguir como yo."
    call BlinkXPS3 ("c25s001_230" , "d") from _call_BlinkXPS3_2099
    eva "*Risa* Ya sabes... dos tiros en el pecho..."
    mc "*Risa* Y uno en la cabeza..."
    scene c25s001_230d with dissolve
    "Vuestras lenguas se vuelven a entrelazar. Vuestros labios vuelven a jugar, cada vez con más ansia."
    call BlinkXPS3 ("c25s001_235" , "d") from _call_BlinkXPS3_2100
    eva "*Respiración entrecortada* Esto cada vez es mejor. Me podría pasar horas besándote."
    mc "Yo también, pero entonces no tendríamos tiempo para más."
    mc "Aunque no me importaría pasar así el tiempo hasta que llegue el helicóptero."
    call BlinkXPS3 ("c25s001_240" , "d") from _call_BlinkXPS3_2101
    eva "*Risita* Pero entonces no hubiera hecho falta que nos desnudáramos."
    mc "*Risa* Tienes razón. Y no voy a perder la oportunidad, ahora que te tengo así."
    scene c25s001_245a with dissolve
    "Bajas tu cabeza hacia uno de sus enhiestos pezones, extremadamente duro."
    eva "*Gemido* Me parece un buen lugar para empezar a aprovechar las oportunidades..."
    "Mjolnir hace rato que está en orden de batalla, deseoso de penetrar las defensas de [eva]."
    scene c25s001_245b with dissolve
    "Continúas descendiendo a través de sus abdominales, bombardeando con besos todo el camino."
    eva "*Jadeo* Dulce tortura..."
    mc "Si tanta tortura es, puedo parar si quieres..."
    call BlinkXPS3 ("c25s001_250" , "d") from _call_BlinkXPS3_2102
    eva "*Gemido* Aún quedan balas en el cargador de la pistola. ¿Estás seguro de querer parar?"
    mc "*Risa* Si las opciones son continuar o recibir un disparo, creo que tengo clara la elección."
    call BlinkXPS3 ("c25s001_255" , "d") from _call_BlinkXPS3_2103
    eva "*Risa* ¿Por quién me has tomado? Lo decía porque podías seguir entrenando..."
    eva "*Risa* Pero lo de pegarte un tiro tampoco es mala idea."
    mc "*Risa* Prefiero otro tipo de entrenamiento."
    scene c25s001_245c with dissolve
    "Ametrallas el interior de su muslo con más besos, intercalando algún mordisco."
    "Esos muslos podrían aplastar nueces entre ellos."
    eva "*Gemido* ¡Joder, [mc]! Me estás matando de anticipación..."
    "Con tu cara a la altura de su cadera, puedes oler que está tan cachonda como tú sin tener que acercar tu nariz a su conejo."
    mc "¿Quieres que deje los besos ya?"
    eva "*Jadeo* ¡Ni en broma!"
    scene c25s001_905pv with hpunch
    "Mientras cambias de muslo, aprovechas para hacer un ataque sorpresa sobre su húmeda raja por un segundo."
    eva "*GEMIDO* ¡OOOF!"
    scene c25s001_245d with dissolve
    "Mueves tu cabeza a su muslo derecho, repartiendo besos, lametones, y mordiscos por todo el camino entre la ingle y la rodilla."
    "Tan solo ha sido un ataque preventivo. Ahora tiene una pequeña muestra de lo que puede esperar."
    eva "*Jadeo* ¿Habías dicho algo sobre recibir un disparo?"
    eva "*Gemido* ¡Vuelve atrás ahora mismo! *Risa*"
    "La preciosa mercenaria está cada vez más impaciente."
    "Generar anticipación es bueno, pero hay que saber dónde están los límites... especialmente con una mujer que te puede partir el cuello con los muslos."
    scene c25s001_245e with hpunch
    "Vuelves al centro de su cuerpo, a su castillo nunca antes atacado, dispuesto a disfrutar del botín."
    eva "*GEMIDO* ¡OOOF! *JADEO* ¡Me encanta!"
    "Tus papilas gustativas reciben el asalto del sabor de sus jugos. Su olor terroso se infiltra en tu nariz."
    "Ser la primera persona que está en lo que, hasta hoy, era tierra de nadie, es una sensación maravillosa."
    scene c25s001_900pv with dissolve
    show c25s001_900v
    "Empiezas a lamer sus abundantes jugos. Está claramente tan cachonda como tú, pero quieres hacerle disfrutar del paquete completo."
    eva "*Jadeo* Un poco más arriba. *Gemido* Ahí es donde más me gusta. *Jadeo*"
    "Dice la bella pelirroja en el momento en que abandonas su clítoris para centrarte en sus labios."
    eva "*Gemido* ¡Te he dicho más arriba! *Jadeo* Pero ahí también me gusta... *Gemido*"
    mcp "(Paquete completo, cielo.)"
    "No vas a dejar que te diga cómo tienes que hacer una de las cosas que más te gustan. Al menos, sin apuntarte con un arma."
    scene c25s001_905pv with dissolve
    hide c25s001_900v
    show c25s001_905v
    "Sus labios se abren y se cierran al paso de tu lengua, que no deja un rincón sin recorrer, mientras sus piernas son recorridas por espasmos de placer."
    eva "*GEMIDO* No voy a aguantar mucho más, [mc]. *JADEO*"
    "Cada vez que tocas su duro botón del placer, su cuerpo se estremece con más fuerza que la vez anterior, indicándote que su orgasmo se acerca."
    eva "**JADEO* ¿Cómo he podido vivir sin esto? *GEMIDO*"
    "En el siguiente paso por su clítoris sus músculos se tensan mucho más que en las caricias anteriores."
    call OrgasmXS3 ("c25s001_260") from _call_OrgasmXS3_52
    eva "*GEMIDO* ¡JODER! *JADEO* ¡SIGUE ASÍ! *GEMIDO*"
    "Tu lengua es asaltada de nuevo por sus jugos, mucho más intensamente que antes debido a su orgasmo."
    "Sigues lamiendo."
    scene c25s001_910pv with dissolve
    hide c25s001_905v
    show c25s001_910v
    "Todos los juegos previos con el striptease han puesto muy cachonda a la mercenaria, hasta el punto de que su primer orgasmo ha llegado antes de lo que esperabas."
    eva "*GEMIDO* ¿Cómo puedes hacer sentirme así? *JADEO*"
    "La tensión en sus piernas empieza a desaparecer a la vez que las últimas oleadas de su orgasmo."
    eva "*Jadeo* Para, por favor. *Gemido* No puedo continuar... *Jadeo*"
    "Das un último lametón antes de mirarla a los ojos."
    call BlinkXPS3 ("c25s001_265" , "d") from _call_BlinkXPS3_2104
    mc "¿Necesitas descansar?"
    eva "*Respiración entrecortada* Necesito recuperar la respiración, pero también te quiero dentro de mí..."
    mc "¿Qué quieres que haga, entonces?"
    call BlinkXPS3 ("c25s001_270" , "d") from _call_BlinkXPS3_2105
    eva "Sube aquí y bésame."
    "Su tono es áspero. Una mezcla de orden y urgencia."
    mc "Eso puedo hacerlo..."
    scene c25s001_230d with dissolve
    "Estás tentado de subir lentamente repartiendo besos por su cuerpo, pero la urgencia en sus palabras te disuade de ello."
    "Cuando vuestros labios se unen, la preciosa asesina gime en tu boca."
    "No es la mejor forma de recuperar la respiración."
    scene c25s001_230e with dissolve
    "Mjolnir, en orden de batalla, presiona contra los abdominales de la ansiosa mujer."
    "No podrías decir qué está más duro."
    call BlinkXPS3 ("c25s001_275" , "d") from _call_BlinkXPS3_2106
    eva "Creo que ya estoy lista..."
    "Su tono refleja duda esta vez."
    mc "Si no quieres ir más allá hoy, podemos dejarlo para otro día."
    call BlinkXPS3 ("c25s001_280" , "d") from _call_BlinkXPS3_2107
    eva "No es eso..."
    mc "¿Qué es, entonces? [eva], la comunicación es necesaria en estos casos. Especialmente en nuestra primera vez juntos."
    call BlinkXPS3 ("c25s001_285" , "d") from _call_BlinkXPS3_2108
    eva "[eil] me dijo que la mayoría de las mujeres solo pueden tener un orgasmo... y yo ya lo he tenido."
    eva "También me dijo que tú disfrutas mucho más cuando tu pareja tiene orgasmos mientras le haces el amor."
    mc "¿Tienes miedo de que no me guste?"
    call BlinkXPS3 ("c25s001_290" , "d") from _call_BlinkXPS3_2109
    eva "Estoy asustada de que te guste menos de lo que podría gustarte. De lo que te gusta con otras chicas. [eil] me dijo que..."
    mc "[eva], [eil] no está aquí. Estamos tú y yo. Tenemos que descubrir cómo encajamos juntos, y eso no nos lo va a poder decir nadie."
    mc "Podemos hacer lo que tú quieras y parar cuando tú quieras. Ahora o más tarde. Para mí ya ha sido una experiencia increíble."
    call BlinkXPS3 ("c25s001_295" , "d") from _call_BlinkXPS3_2110
    eva "Pero quieres más, ¿verdad?"
    mc "Sólo si tú lo quieres."
    eva "Yo no quiero parar, pero..."
    "No quieres pasar los próximos minutos dando vueltas alrededor del mismo tema."
    scene c25s001_230f with dissolve
    "Apoyas tu glande contra su monte de Venus, rozando la capucha de su clítoris con la punta de tu polla."
    call BlinkXPS3 ("c25s001_300" , "v") from _call_BlinkXPS3_2111
    eva "*Risa* ¡Eso es trampa!"
    mc "Sabes cómo es la frase, ¿no? En el amor y en la guerra..."
    call BlinkXPS3 ("c25s001_300a" , "d") from _call_BlinkXPS3_2112
    eva "*Risa* ¿No existen las trampas?"
    mc "*Risa* No es exactamente así, pero me sirve."
    mc "¿Preparada?"
    scene c25s001_230g with dissolve
    "[eva] levanta sus caderas para que Mjolnir apunte a su entrada."
    eva "Cuando quieras."
    "Puedes notar el calor que emana de sus labios, que envuelven tu glande, su humedad mezclándose con tu líquido preseminal."
    eva "No hace falta que seas delicado."
    scene c25s001_230h with hpunch
    "Introduces la punta de tu polla dentro del estrecho coño de [eva]. No notas una resistencia que esperabas encontrar."
    eva "*GEMIDO* ¡OOOF!"
    "Dentro de la pelirroja todo es húmedo y duro. Sus músculos están tensos. Y hay muchos músculos apretando tu polla."
    call BlinkXPS3 ("c25s001_305" , "d") from _call_BlinkXPS3_2113
    mc "Tienes que relajarte o va a doler."
    eva "¿Más? ¿Doler más, me refiero?"
    mc "¿Te ha dolido mucho?"
    call BlinkXPS3 ("c25s001_310" , "d") from _call_BlinkXPS3_2114
    eva "Un poco... No esperaba que... Aunque no es nada que no pueda soportar. Ha sido un dolor momentáneo. Ya está pasando."
    mc "Cuanto más te relajes, antes pasará."
    call BlinkXPS3 ("c25s001_315" , "d") from _call_BlinkXPS3_2115
    eva "¿Cuánto hay dentro?"
    mc "Algo menos de un tercio."
    call BlinkXPS3 ("c25s001_320" , "d") from _call_BlinkXPS3_2116
    eva "¿Sólo?"
    mc "Solo. Podemos esperar a que te acostumbres o puedo salir."
    call BlinkXPS3 ("c25s001_325" , "d") from _call_BlinkXPS3_2117
    eva "No quiero que salgas. Creo que puedes empezar a moverte si quieres."
    mc "Voy..."
    scene c25s001_915pv with dissolve
    hide c25s001_910v
    show c25s001_915v
    "Empiezas a bombear con tus caderas, intentando no llegar al fondo para no producirle más dolor del necesario."
    mc "¿Va bien así?"
    eva "*Gemido* Sí... *Jadeo* El dolor está desapareciendo... *Gemido*"
    "Poco a poco va relajando los músculos. No por ello su agujero del amor es menos estrecho."
    eva "*Jadeo* Así es perfecto. *Gemido*"
    "Sus gemidos suben un poco de volumen, indicando que el dolor se está transformando en placer."
    scene c25s001_920pv with dissolve
    hide c25s001_915v
    show c25s001_920v
    "Empiezas a usar a Mjolnir como un ariete, entrando profundamente dentro de la mercenaria."
    eva "*GEMIDO* ¡Oh! *JADEO*"
    "Suena totalmente sorprendida por el cambio de ritmo."
    eva "*JADEO* ¡Eso es mejor aún! *GEMIDO*"
    "Totalmente relajada, empieza a disfrutar de veras. Ahora acompaña cada una de tus embestidas apretando sus músculos, potenciando el placer de ambos."
    eva "*JADEO* ¡Agárrame del cuello! *JADEO*"
    "Es tu momento de sorprenderte por su petición."
    $ eva._var("chanceChoking", True)
    if persistent.walkthrough:
        $ wt1 = _("Fetiche de asfixia activado con [eva].")
        $ wt2 = _("Fetiche de asfixia desactivado con [eva].\n Es la única chica con este fetiche.")
    else:
        $ wt1 = ""
        $ wt2 = ""
    menu:
        "Agarrarla por el cuello." (wt=wt1):
            $ eva._var("choking", True)
            scene c25s001_930pv with dissolve
            hide c25s001_920v
            show c25s001_930v
            "La sorpresa y el tono imperativo hacen que te sea imposible negarte a lo que te pide. La agarras por el cuello, sin apretar demasiado."
            "Justo lo suficiente como para que note la presión de tu mano sobre su garganta. Continúas embistiendo."
            eva "*GEMIDO* ¡SÍ! *JADEO* Me gusta sentirme a tu merced. *GEMIDO*"
            "La sensación de poder que da tenerla así es algo diferente de lo que has experimentado hasta ahora."
            "La brava mercenaria es la persona que menos hubieras imaginado pidiendo esto."
            eva "*JADEO* ¡Es increíble sentirse indefensa por una vez! *JADEO*"
            mcp "(Así que es eso, ¿no? Sabe que es la más fuerte de los dos y le gusta jugar el rol de damisela indefensa.)"
            "No hay humillación, no hay violencia. Tan solo dos amantes jugando un juego que sólo ellos entienden."
            scene c25s001_925pv with dissolve
            hide c25s001_930v
            show c25s001_925v
            "Continúas bombeando mientras la sujetas con una mano por su durísimo culo y con otra por el cuello."
            eva "*GEMIDO AHOGADO* ¡Sigue así! *JADEO* ¡Mi hombre! *GEMIDO*"
            "Puedes notar cómo sus paredes vaginales aprietan tu polla más todavía, como un puño de acero en un guante de terciopelo, desde que la estás asfixiando."
            "Aunque sólo sea de forma fingida."
        "No hacerlo." (wt=wt2):
            $ eva._var("choking", False)
            scene c25s001_925pv with dissolve
            hide c25s001_930v
            show c25s001_925v
            "Continúas bombeando, ignorando su petición, mientras la sujetas con ambas manos por su durísimo culo."
            eva "*GEMIDO AHOGADO* ¡Sigue así! *JADEO* ¡Mi hombre! *GEMIDO*"
            "Puedes notar cómo sus paredes vaginales aprietan tu astil en toda su longitud como un puño de acero en un guante de terciopelo pese a que no le hayas hecho caso."
    $ resetWalkthrough()
    eva "*JADEO* ¡Si sigues así voy a volver a correrme! *GEMIDO*"
    "El miedo por lo que le ha dicho [eil] sobre un único orgasmo ha desaparecido. Su cuerpo le dice que su segundo orgasmo está a punto de llegar."
    scene c25s001_330An with dissolve
    "Intentando afianzar los pies, pisas uno de los cartuchos que hay en el suelo. Rueda bajo tu pie y pierdes el equilibrio."
    if eva._var("choking"):
        "Arrastras a [eva] contigo, soltando su cuello para evitar hacerle daño. La mercenaria ha cerrado las piernas entorno a ti en el momento en que ha notado la falta de equilibrio."
    else:
        "Arrastras a [eva] contigo en tu caída. La mercenaria ha cerrado las piernas entorno a ti en el momento en que ha notado la falta de equilibrio."
    "Con más agilidad de la que podrías imaginar, destrenza su abrazo justo antes de tocar el suelo."
    scene c25s001_330d with vpunch
    eva "*GEMIDO* ¡OOOF! *JADEO*"
    "Eso no evita que se empale en Mjolnir al acabar la caída. En ningún momento habías entrado tan profundamente en ella."
    call BlinkXPS3 ("c25s001_335" , "d") from _call_BlinkXPS3_2118
    mc "Lo siento..."
    eva "¿Qué ha pasado?"
    mc "He pisado un cartucho. Creo que de una de las sesiones anteriores."
    eva "¿Estás bien?"
    mc "*Risa* Sí. El costalazo ha sido grande, pero no nada que no pueda soportar."
    call BlinkXPS3 ("c25s001_340" , "d") from _call_BlinkXPS3_2119
    eva "Los mataré por no haber barrido. Deja que me levante."
    mc "¿Te has hecho daño?"
    call BlinkXPS3 ("c25s001_345" , "d") from _call_BlinkXPS3_2120
    eva "No, pero tú sí, ¿no? No creo que puedas seguir."
    scene c25s001_350An with dissolve
    "Sin decir una palabra, la levantas a lo largo de tu astil y la vuelves a empalar en Mjolnir."
    scene c25s001_330e with vpunch
    eva "*JADEO* ¡OOOF! *JADEO*"
    call BlinkXPS3 ("c25s001_350" , "d") from _call_BlinkXPS3_2121
    eva "Parece que sí, que puedes seguir. *Risa*"
    mc "¿Y tú?"
    scene c25s001_935pv with dissolve
    hide c25s001_925v
    show c25s001_935v
    "Tampoco dice una palabra antes de empezar a cabalgarte, tomando la iniciativa."
    eva "*Gemido* ¿Crees que una caída...? *Jadeo* ¿...iba a impedirme seguir? *Gemido*"
    "No espera una respuesta. No la necesita. Sabe que conoces su fortaleza física."
    mc "Sabía que no lo haría. Eres una mujer fuerte."
    "Pero no sabes callarte ni debajo del agua. Tu respuesta provoca un espasmo de placer en sus muros interiores."
    "A veces te alegra no saber callarte."
    scene c25s001_945pv with dissolve
    hide c25s001_935v
    show c25s001_945v
    "Las vistas desde abajo son increíbles. El hermoso rostro de [eva], enmarcado por la fría luz de la galería de tiro, revela el placer que está sintiendo."
    eva "*Gemido* Me gusta incluso más así. *Jadeo*"
    if eva._var("choking"):
        "Dejarte tener el control por un momento ha sido arduo para ella. Le gusta recuperarlo una vez finalizado el cambio de roles."
    else:
        "Es una mujer acostumbrada a tener el control, lo que hace aún más sorprendente su petición de que la agarraras por el cuello."
    eva "*Jadeo* Me podría pasar horas haciendo esto. *Gemido*"
    "Sabes que tiene la resistencia necesaria para hacerlo. Sabes que tú también la tienes. Por desgracia, hay una reunión en un yate que evitará que lo hagáis."
    "Quizás otro día."
    scene c25s001_950pv with dissolve
    hide c25s001_945v
    show c25s001_950v
    "La coordinación en cada uno de sus movimientos te está llevando al séptimo cielo. Se mueve con precisión quirúrgica, no por ello menos apasionada."
    eva "*GEMIDO* ¿Crees que podré seguir...? *JADEO* ¿...después de correrme? *GEMIDO*"
    "La personalidad que no había hecho su aparición hasta entonces, la niña curiosa por las cosas nuevas, saca su cabeza."
    eva "*JADEO* Noto cómo está creciendo dentro de mí. *JADEO* Es una sensación maravillosa. *JADEO*"
    "El tuyo también está empezando a reptar por tus piernas. Llevas cachondo lo que parecen horas y no te queda mucho combustible para este primer asalto."
    scene c25s001_940pv with dissolve
    hide c25s001_955v
    show c25s001_940v
    "Sigue cabalgándote, luchando con su cuerpo por mantener la coordinación. Lo consigue a duras penas."
    eva "*GEMIDO* ¡No puedo retenerlo más! *GEMIDO* ¡Voy a correrme! *GEMIDO*"
    mc "No lo retengas; déjate ir. Yo también estoy a punto."
    "Su cuerpo se tensa un poco más por un momento, al descubrir las implicaciones de lo que acabas de decir, antes de continuar la salvaje cabalgata."
    eva "*JADEO* ¡CÓRRETE CONMIGO! *GEMIDO* ¡CÓRRETE DENTRO! *JADEO*"
    "Supones que, si no quieres morir estrangulado, más te vale hacerle caso."
    $ eva._var("chancePregnant", True)
    if persistent.pregnancy:
        if persistent.walkthrough:
            $ wt1 = _("[eva] embarazada.")
            $ wt2 = _("Sin consecuencias.")
        else:
            $ wt1 = ""
            $ wt2 = ""
        menu:
            "Correrte dentro. Ir a por el bebé." (wt = wt1):
                $ eva._var("pregnant", True)
                $ eva._var("undiscoveredPregnancy", True)
                play sound ("music/OldMusicBox5.ogg")
            "Correrte dentro." (wt = wt2):
                pass
        $ resetWalkthrough()
    call OrgasmXS3 ("c25s001_355") from _call_OrgasmXS3_53
    mc "¡Mpfft!" (multiple=2)
    eva "*GEMIDO* ¡SÍ! *JADEO*" (multiple=2)
    "Os corréis prácticamente a la vez. Un orgasmo provocando el otro. El segundo potenciando el primero."
    "A [eva] se le saltan las lágrimas."
    scene c25s001_980pv with dissolve
    hide c25s001_940v
    show c25s001_980v
    "Continúa cabalgando a Mjolnir para prolongar su placer. Para prolongar el tuyo."
    eva "*JADEO* ¡INCREÍBLE! *GEMIDO* ¡ALUCINANTE! *JADEO*"
    "Su coordinación, perfecta hace unos segundos, da paso a una serie de movimientos descontrolados mientras oleadas de placer la recorren."
    eva "*GEMIDO* ¡[eil] tenía razón! *JADEO* ¡ESTO ES LO MEJOR DEL MUNDO! *GEMIDO*"
    "Tienes que darle las gracias a [eil] por darle consejos. De pelirroja a pelirroja."
    scene c25s001_360d with dissolve
    hide c25s001_980v
    "Al cabo de unos segundos, sin desempalarse de Mjolnir, las fuerzas de [eva] desaparecen y cae rendida sobre tu pecho."
    stop music fadeout (1.5)
    call BlinkXPS3 ("c25s001_365" , "d") from _call_BlinkXPS3_2122
    eva "*Gemido* Gracias, [mc]."
    play music ("music/LostVoices.ogg")
    mc "*Risa* No hay que dar las gracias por algo así, [eva]. Lo hemos hecho juntos."
    mc "O, si quieres, yo también te puedo dar las gracias a ti."
    call BlinkXPS3 ("c25s001_370" , "d") from _call_BlinkXPS3_2123
    eva "*Gemido* No lo puedes entender... Me has hecho sentir lo suficientemente... segura... como para dejarme ir."
    mc "Entonces también te tengo que dar las gracias yo a ti."
    call BlinkXPS3 ("c25s001_375" , "d") from _call_BlinkXPS3_2124
    eva "*Jadeo* ¿Por qué?"
    mc "Por querer sentirte lo suficientemente segura como para hacerlo."
    mc "Sé que te cuesta renunciar al control."
    call BlinkXPS3 ("c25s001_380" , "d") from _call_BlinkXPS3_2125
    eva "*Risa* ¡Hey! Soy una sociópata, pero tengo mi corazoncito."
    mc "*Risa* No eres una sociópata, mi pequeña guerrera. Tan solo eres una preciosidad impulsiva."
    call BlinkXPS3 ("c25s001_385" , "d") from _call_BlinkXPS3_2126
    eva "¿Sabes que existen los sociópatas explosivos? Leyendo la definición encaja bien conmigo."
    mc "*Risa* Leyendo la definición de la enfermedad de Alzheimer, encaja con cuando bajo a la cocina y no recuerdo a qué."
    mc "Yo no me debo fiar de las películas, y tú debes aprender a no fiarte de todo lo que lees en internet."
    call BlinkXPS3 ("c25s001_390" , "d") from _call_BlinkXPS3_2127
    eva "*Risa* Touché."
    eva "¿Nos podemos levantar? Tengo un cartucho clavado en la rodilla desde que nos hemos caído."
    mc "¡Haberlo dicho antes!"
    call BlinkXPS3 ("c25s001_395" , "d") from _call_BlinkXPS3_2128
    eva "¿E interrumpir lo que acabamos de hacer? ¡Ni en broma!"
    mc "Va, levántate."
    call BlinkXPS3 ("c25s001_400" , "f") from _call_BlinkXPS3_2129
    "Os sentáis en el suelo, alejados de la rejilla donde habéis hecho el amor. Era realmente incómoda."
    mc "¿Te ha gustado?"
    eva "Me ha encantado. Ha sido lo más alucinante que he experimentado nunca."
    eva "Si lo que has hecho con la lengua supera a cualquier paja que me haya hecho nunca..."
    eva "Lo otro es... no sé... no tengo palabras para describirlo..."
    call BlinkXPS3 ("c25s001_405" , "d") from _call_BlinkXPS3_2130
    eva "¿Y a ti? ¿Te ha gustado?"
    mc "Mucho. Ha sido una experiencia increíble. Siento como que hemos conectado de una forma en que no lo habíamos hecho antes."
    call BlinkXPS3 ("c25s001_410" , "h") from _call_BlinkXPS3_2131
    eva "¡Esa es la palabra! Conexión."
    eva "No me había sentido conectada a nadie tanto como lo he hecho contigo hace un momento."
    call BlinkXPS3 ("c25s001_415" , "d") from _call_BlinkXPS3_2132
    eva "Ni siquiera con mis hermanas."
    mc "El sexo, cuando hay sentimientos involucrados, tiene ese efecto."
    call BlinkXPS3 ("c25s001_420" , "d") from _call_BlinkXPS3_2133
    eva "¿Crees que... estén donde estén... les molestará?"
    eva "Por un momento me he olvidado de ellas. No podía pensar en nada más que en lo que estábamos haciendo."
    mc "Estoy seguro de que no les molestará. Es un paso más en tu proceso de curación, [eva]."
    call BlinkXPS3 ("c25s001_425" , "d") from _call_BlinkXPS3_2134
    eva "*Risita* Eso ha sonado raro. 'Hola, soy [mc] y tengo una polla mágica con poderes curativos.'"
    mc "*Risa* Sabes que no lo decía por eso."
    call BlinkXPS3 ("c25s001_430" , "d") from _call_BlinkXPS3_2135
    eva "Lo sé. Pero no quiero hablar ahora de curaciones ni de mis hermanas."
    eva "Por un momento solo hemos existido tú y yo. Me gusta esa sensación."
    mc "A mí también."
    scene c25s001_430d with dissolve
    "Pasáis un rato en silencio, tan solo disfrutando del tacto de la piel desnuda del otro. Notando cómo vuestros latidos se acompasan."
    "No hay fantasmas para estropear el momento."
    call BlinkXPS3 ("c25s001_435" , "f") from _call_BlinkXPS3_2136
    "Pero [eva] aún no ha aprendido la lección sobre relajarse."
    eva "Voy a lavarme la cara. Creo que se me ha corrido la pintura. Es la primera vez que tengo un orgasmo tan intenso y tengo que estar horrible."
    mc "No estás horrible, cielo. Estás guapísima."
    mc "*Risa* Y espero que se te vuelva a correr en el segundo asalto."
    call BlinkXPS3 ("c25s001_440a" , "d") from _call_BlinkXPS3_2137
    eva "*Risa* ¡No va a haber segundo asalto!"
    eva "Yo tengo que volver a la base en la moto mientras tú vas al yate. *Risa* No sé si voy a poder sentarme en el sillín."
    call BlinkXPS3 ("c25s001_440b" , "d") from _call_BlinkXPS3_2138
    eva "Además, [ama] tiene que estar al caer y no hay tiempo."
    mc "¿Ya es la hora?"
    call BlinkXPS3 ("c25s001_445" , "d") from _call_BlinkXPS3_2139
    eva "Casi. Voy a lavarme. Debo oler a sexo y pólvora."
    call BlinkXPS3 ("c25s001_450" , "d") from _call_BlinkXPS3_2140
    eva "Mmmm... Alguien debería sacar una colonia que oliera así. Yo la compraría."
    mc "*Risa* Dame un beso antes de irte."
    scene c25s001_450d with dissolve
    "Vuestros labios se unen en un dulce beso. No hay urgencia en él. Tan solo muchos sentimientos compartidos."
    "El beso es muy corto. O eso te parece. Te hubiera parecido corto aunque hubiera durado una eternidad."
    scene c25s001_450e with fade
    eva "Tú deberías ducharte. Debes oler igual que yo. Hay una ducha en la oficina."
    scene c25s001_450f with dissolve
    eva "[ama] ya está llegando en la furgoneta. Puedo oírla."
    "Tú no oyes nada. Esta chica tiene unos sentidos más agudos que los tuyos."
    eva "Vístete si no quieres que te encuentre así."
    scene c25s001_450g with dissolve
    "Tras recoger toda la ropa que se ha quitado durante el striptease, la bella mercenaria desaparece."
    "Un poco más cerca de la curación."
    "Te vuelves a poner el traje de paracaidista mientras esperas que llegue [ama]."
    stop music fadeout (1.5)
    "Escuchas abrirse la puerta del almacén donde [eva] ha guardado la moto."
    return
label c25s002_AmaHelo:
    if _in_replay:
        call mrS3_eva_route from _call_mrS3_eva_route_7
    scene c25s002_005d with fade
    "Un minuto después..."
    play sound ("music/knock.ogg")
    "*Knock-Knock*"
    ama "*A través de la puerta* Soy yo. Dejad de disparar."
    play music ("music/i-feel-alive.ogg")
    mc "Pasa, [ama]. Estoy solo."
    call BlinkXP("c25s002_005" , "d") from _call_BlinkXP_3816
    ama "¿Dónde está [eva]?"
    mc "Ha ido al lavabo. En cuanto vuelva iré a darme una ducha."
    call BlinkXP("c25s002_010" , "d") from _call_BlinkXP_3817
    ama "Sí, será lo mejor. Hueles a pólvora..."
    mc "*Risa* Para una reunión con tipos malotes no me parece una mala colonia: *Con acento francés* Eau de pólvora."
    call BlinkXP("c25s002_015" , "d") from _call_BlinkXP_3818
    ama "No son tipos malotes, [mc]. Son asesinos como lo somos [eva] y yo. Ya has visto los expedientes."
    ama "Aparte de Ichigo y algunos militares, el resto son mafiosos y traficantes."
    ama "No es para tomárselo a broma."
    mc "No me lo tomo a broma, [ama]. Puedo bromear contigo, pero en ningún momento voy a tomármelo a broma."
    call BlinkXP("c25s002_020" , "d") from _call_BlinkXP_3819
    ama "Si algo bueno ha tenido NTR es que sólo ha aceptado gobiernos como clientes."
    ama "Es más... limpio."
    mc "Y será más limpio aún una vez nos libremos de esa parte del negocio, no te preocupes."
    call BlinkXP("c25s002_025" , "d") from _call_BlinkXP_3820
    if eva._var("route"):
        ama "¿Cómo ha ido el entrenamiento-cita?"
    else:
        ama "¿Cómo ha ido el entrenamiento?"
    mc "Muy bien. Creo que [eva] te debe dinero. He conseguido el objetivo a los siete metros."
    call BlinkXP("c25s002_030" , "d") from _call_BlinkXP_3821
    eva "¡Chivato! *Risa* Lo ha hecho mejor de lo que esperaba. Pero no es dinero lo que habíamos apostado."
    mc "¿Qué habíais apostado?"
    call BlinkXP("c25s002_035" , "d") from _call_BlinkXP_3822
    ama "[eva] va a tener que hacer la limpieza de la base hasta que nos vayamos a Aruba."
    ama "Le servirá de entrenamiento para cuando estemos fuera. No se le da muy bien la escoba. *Risa* Aún está buscando el gatillo."
    scene c25s002_035d with dissolve
    eva "*Grrrr*"
    mc "*Risa* Voy a ducharme."
    call BlinkXP("c25s002_035b" , "d") from _call_BlinkXP_3823
    ama "Ahora te llevo el traje a la oficina. Te esperamos aquí."
    scene c25s002_035e with dissolve
    "Después de la ducha, con el traje puesto..."
    mc "Cuando quieras."
    ama "Me dejas sin palabras." (multiple=2)
    eva "¡Wow! Me encanta ese traje." (multiple=2)
    mc "Gracias, chicas."
    call BlinkXP("c25s002_040" , "d") from _call_BlinkXP_3824
    eva "Voy a recoger todo esto un poco antes de volver a la base. Mañana vengo con las chicas..."
    eva "Me servirá de entrenamiento con la escoba."
    mc "*Risa* La parte peluda es la que va hacia el suelo."
    mc "*Risa* Quería devolvértela desde aquel día en el lago cuando me dijiste que la parte del agujero de la pistola es por donde salían las balas."
    scene c25s002_040d with dissolve
    eva "Muy gracioso..."
    eva "Os veo mañana. Suerte."
    call BlinkXP("c25s002_045" , "d") from _call_BlinkXP_3825
    ama "Nosotros vamos a esperar el helicóptero fuera. Debe estar a punto de llegar."
    mc "Como quieras."
    call BlinkXP("c25s002_050" , "f") from _call_BlinkXP_3826
    mc "Veo que tú también has escondido la furgoneta."
    ama "Si dices 'también' supongo que [eva] te ha explicado la razón para hacerlo."
    mc "Sí, la considero lógica. Son cosas en las que yo no pensaría nunca."
    call BlinkXP("c25s002_060" , "d") from _call_BlinkXP_3827
    ama "Para eso nos tienes a nosotras. Nos han entrenado para esto."
    mc "Y sois la mejor compañía que podría tener para hacer esto ¿Algún último consejo para la reunión?"
    call BlinkXP("c25s002_055" , "d") from _call_BlinkXP_3828
    ama "Lo mismo que te he dicho estos días. No muestres tus puntos débiles, no te comprometas a nada, y no caigas en ninguna provocación."
    ama "Ichigo va a aprovechar cualquier punto débil que pueda encontrar."
    mc "Por suerte, te tendré conmigo para evitar que cometa cualquier error infantil."
    call BlinkXP("c25s002_065" , "d") from _call_BlinkXP_3829
    ama "Tan solo tienes que pensar antes de actuar."
    stop music fadeout (1.5)
    ama "Es hora de prepararse. Oigo el helicóptero."
    $renpy.sound.play("music/helicopter.ogg", loop=True)
    scene c25s002_070a with fade
    "Un minuto después, aterriza un helicóptero en el aparcamiento. El ruido es ensordecedor."
    scene c25s002_070An with dissolve
    "???" "¿Señor Marks? ¿Señorita Gilford?"
    mc "Sí, y usted es..."
    "Kostner" "Kostner. ¿Me acompañan al helicóptero?"
    call BlinkXP("c25s002_075" , "f") from _call_BlinkXP_3830
    "Nada más sentaros, [ama] se pone unos auriculares y te indica que te pongas unos que hay colgando a tu espalda. Te los pones."
    mc "*Gritando* Ahora entiendo por qué gritan tanto en las películas cuando van en helicóptero."
    ama "No hace falta que grites demasiado con esto. De lo que pase en las películas..."
    mc "Lo sé, no me puedo fiar."
    ama "Será mejor que no digas nada en este viaje de lo que no quieras que se enteren."
    mc "Entendido."
    scene c25s002_075d with fade
    "El helicóptero viaja mar adentro durante varios minutos alejándose de la costa."
    "Es tu primera vez en un helicóptero lo que hace los primeros minutos emocionantes. Después, es como ir en un taxi ruidoso."
    call BlinkXP("c25s002_080" , "d") from _call_BlinkXP_3831
    mc "Creía que la reunión era en el puerto de Westport."
    ama "Creo que vamos a salir de las aguas territoriales de Estados Unidos."
    mc "¡Eso son 200 millas!"
    call BlinkXP("c25s002_085" , "d") from _call_BlinkXP_3832
    ama "*Risa* Eso es la Zona Económica Exclusiva, que son 200 millas NÁUTICAS. 225 millas terrestres."
    ama "Yo me refiero a las aguas territoriales. 12 millas náuticas, 13.5 millas terrestres."
    mc "¿Por qué tan lejos?"
    call BlinkXP("c25s002_090" , "d") from _call_BlinkXP_3833
    ama "Ya has visto la lista de invitados. Seguro que se hace algo ilegal en ese barco. Prostitución, drogas..."
    ama "En aguas territoriales se aplican las leyes americanas y podrían tener problemas."
    mc "Claro. Lo entiendo."
    scene c25s002_075e with fade
    "Unos minutos después, puedes ver el enorme yate flotando, majestuoso en medio de la nada, cuando el helicóptero gira para hacer la maniobra de aproximación."
    call BlinkXP("c25s002_095" , "d") from _call_BlinkXP_3834
    mc "¡Es enorme!"
    ama "*Risa* ¡Eso dijo ella!"
    mc "*Risa* ¡Qué gran serie!"
    scene c25s002_075e with fade
    mc "¿Eso son ametralladoras?"
    ama "Estaciones de armas. Pero sí, para ti, son ametralladoras."
    call BlinkXP("c25s002_100" , "d") from _call_BlinkXP_3835
    ama "Para mí estaciones bastante inútiles. No pueden cubrir todas las aproximaciones al barco."
    ama "Creo que están para impresionar. Supongo que más a clientes que a posibles asaltantes."
    ama "Ya he descubierto al menos tres puntos por donde subir al barco fuera del alcance de las estaciones de armas."
    mc "No dejas de sorprenderme..."
    return
label c25s002_IronFist:
    if _in_replay:
        call mrS3_kia_route from _call_mrS3_kia_route_5
        call mrS3_ama_route from _call_mrS3_ama_route_7
        call mrS3_kim_rps (5, 10, 15) from _call_mrS3_kim_rps
        $ jef = TGCharacter ("Jeff Sound", color = "#ffffff")
    scene c25s002_105a with fade
    "Al bajar del helicóptero, encuentras una sorpresa esperándote."
    stop sound fadeout (1.5)
    call BlinkXP ("c25s002_110" , "d") from _call_BlinkXP_3836
    mc "¿Qué hace [kim] aquí?"
    play music ("music/Dark-Score.ogg")
    ama "No tengo ni idea. Sabía que tenía un evento hoy en un yate, pero no podía imaginar que fuera aquí."
    ama "No des muestras de conocerla. Me parece que hay algo turbio aquí."
    mc "Tienes razón. Me parece que será lo mejor."
    ama "Vamos a acercarnos."
    call BlinkXP ("c25s002_115" , "d") from _call_BlinkXP_3837
    kim "¿[mc]? ¿[ama]? ¿Qué hacéis...?"
    mc "Sí. [mc] Marks, de NTR. Y mi asistente, la Señorita Gilford."
    call BlinkXP ("c25s002_120" , "d") from _call_BlinkXP_3838
    kim "Bienvenidos al Luxe. ¿Les apetece una copa de champagne?"
    mcp "(Chica lista. Se ha dado cuenta de que estoy fingiendo no conocerla y ha empezado a actuar profesionalmente.)"
    mc "No, gracias."
    call BlinkXP ("c25s002_125" , "d") from _call_BlinkXP_3839
    kim "El Sr. Ichigo está en la cubierta superior. ¿Me quieren acompañar, por favor?"
    mc "Adelante, por favor. Indíquenos el camino."
    scene c25s002_105b with fade
    "Seguís a [kim] a través de unas escaleras hasta la cubierta principal, donde está la piscina."
    "[ama] te va dando información de quién es quién. No es necesario. Esta vez has leído los expedientes, pero no la quieres interrumpir."
    ama "Fong, prostitución y tráfico de personas y armas. De una de las tríadas de San Francisco."
    ama "Davidovic, traficante de drogas y armas de Serbia."
    mc "Supongo que las chicas deben ser..."
    call BlinkXP ("c25s002_130" , "d") from _call_BlinkXP_3840
    ama "Prostitutas, supongo. Como te he dicho, si salíamos de las aguas territoriales sería por algo así."
    mc "Me da la sensación de estar en un videojuego o una película. Esto suena surrealista."
    scene c25s002_105c with fade
    "[kim] os lleva a la cubierta superior, donde Ichigo está hablando con un hombre y una mujer."
    ama "General Fuckebythenavele. Ejército."
    mcp "(¿Fuckebythenavele? Lo había leído en el expediente, pero creía que era algún tipo de broma de [ama].)"
    ama "Alejandra García, ministerio de interior de México."
    ama "Y, óbviamente, Ichigo."
    mc "Esta cubierta parece casi normal comparada con la de abajo."
    call BlinkXP ("c25s002_135" , "d") from _call_BlinkXP_3841
    mc "Casi me siento como un pececillo entre tiburones."
    ama "No te preocupes, lo harás bien."
    scene c25s002_105d with fade
    $ ich = Character ("Ichigo", color="#ffc300")
    $ gfu = Character ("Gen. Fuckebythenavele", color="#42644f")
    $ aga = Character ("Alejandra García", color="#ff0000")
    $ dav = Character ("Davidovic", color="#f30000")
    "Llegáis a donde están Ichigo y sus acompañantes."
    kim "Sr. Ichigo, el Señor Marks y la Señorita Gilford, de NTR."
    ich "Gracias, chica. Puedes volver al helipuerto."
    scene c25s002_105e with dissolve
    kim "Creo que eran los últimos invitados."
    ich "Te he dicho que vuelvas al helipuerto, chica. Eres necesaria allí."
    "El tono despreciativo de Ichigo te molesta por alguna razón. Seguramente porque va dirigido a [kim]."
    scene c25s002_105f with dissolve
    kim "Sí, Sr. Ichigo."
    scene c25s002_140a with dissolve
    ich "Encantado de conocerle por fin, Sr. Marks."
    mc "Igualmente, Sr. Ichigo. Un yate impresionante."
    ich "Gracias. Es uno de los activos más vistosos de Iron Fist."
    scene c25s002_140b with dissolve
    ich "Déjame presentarte a algunos de nuestros invitados, muchacho."
    ich "General Fuckebythenavele, el Sr. Marks y la Srta. Gilford, de NTR."
    gfu "Un placer conocerle. He trabajado en varias ocasiones con sus predecesores. Espero continuar la relación con usted."
    mc "Igualmente. Espero que nuestra relación con su gobierno sea tan provechosa para ambas partes como lo ha sido en el pasado."
    ich "La Sra. García, del Gobierno de México."
    aga "Encantada. No hemos trabajado juntos aún, pero esperamos tener la oportunidad de hacerlo en el futuro."
    mc "Encantado de conocerla. En NTR siempre estamos abiertos a nuevos socios comerciales."
    "[ama] estrecha las manos del general y la política en silencio."
    scene c25s002_140c with dissolve
    ich "Luego te presentaré al resto de asistentes. Mientras tanto, disfruta de la fiesta, muchacho."
    scene c25s002_140d with dissolve
    ich "¡Chica! Trae algo de beber a mis invitados."
    scene c25s002_140e with dissolve
    "Se acerca una de las camareras, uniformada como [kim]. Crees recordar que, cuando llevaste a [kim] al puerto, dijo que se llamaba Adeline."
    if kia._var("route"):
        "Ahora sabes de qué te sonaba la camarera del restaurante donde fuiste con [kia]."
    "Adeline" "¿Puedo traerles algo para beber?"
    ama "Agua para mí, por favor."
    mc "Un zumo de piña para mí, si es tan amable."
    "Adeline" "Ahora mismo."
    scene c25s002_140f with dissolve
    gfu "Ichigo, ¿no le ofreces las chicas a nuestro amigo?"
    ich "Oh, claro. Si te apetece, tan solo tienes que elegir una de las chicas. Hay camarotes privados en las cubiertas inferiores."
    gfu "*Risa* Cualquiera menos Alejandra, claro."
    aga "*Risa fingida* Sí, yo no estoy en el menú. Y para nosotras nunca traen chicos. ¿Lo ve justo, Srta. Gilford?"
    call BlinkXP ("c25s002_145" , "d") from _call_BlinkXP_3842
    ama "No se preocupe por mí, Sra. García. Yo no estaría interesada en los chicos que pudieran traer."
    scene c25s002_140g with dissolve
    ich "¡Oh! Entonces, también le extiendo la invitación por si quiere escoger cualquiera de las chicas, Srta. Gilford."
    mcp "(Ha dicho cualquiera. ¿Eso incluye a [kim]? No creo que sepa dónde se ha metido.)"
    scene c25s002_140h with fade
    "Al cabo de unos minutos, Ichigo y Alejandra se disculpan y os dejan a solas con el general."
    gfu "¿Qué le trae a esta fiesta, Sr. Marks? NTR suele ser más discreta."
    mc "El Sr. Ichigo me invitó para conocernos después del cambio de propiedad de NTR. Represento a los accionistas mayoritarios."
    mc "Tan solo es una visita de cortesía a un posible rival comercial."
    scene c25s002_140i with dissolve
    gfu "Ichigo es... un personaje interesante. Lleva años intentando que trabajemos con él, pero preferimos compañías más... respetables, como la suya."
    gfu "Dentro de lo respetable que se puede ser en este negocio, claro."
    mc "Bueno, desde NTR estamos intentando ser tan respetables como sea posible. Sabemos que no es un negocio limpio, pero al menos puede ser un negocio entre caballeros."
    scene c25s002_140j with dissolve
    gfu "*Risa* Un bonito objetivo. Pero todos los países necesitamos tener nuestros propios perros de presa sin tener responsabilidades si el perro hace algo que no debe."
    gfu "NTR es uno de esos perros. No te lo tomes como un insulto. Sois el perro más quirúrgico que hemos tenido nunca."
    mc "No se preocupe, General. No me lo tomo como una ofensa. Evitar daños colaterales es una de las políticas de NTR."
    call BlinkXP ("c25s002_150" , "d") from _call_BlinkXP_3843
    ama "Es una forma de que nadie se intente deshacer de un perro de presa que se ha vuelto rabioso e incómodo."
    scene c25s002_140k with dissolve
    gfu "Me gusta su política. Es una de las razones por las que es tan difícil que trabajemos con Iron Fist."
    gfu "Aparte de su lista de clientes, claro. Sería difícil defender en el Pentágono que trabajamos con los mismos tipos que las tríadas."
    mc "Lo entiendo. Entonces, ¿qué hace usted aquí, General?"
    scene c25s002_140l with dissolve
    gfu "Una cosa es no querer trabajar con ellos. Otra distinta insultarlos rechazando sus invitaciones."
    gfu "Ichigo puede ser despreciable, pero ya conoces el dicho, 'Los amigos cerca y los posibles enemigos más cerca aún'."
    gfu "Además, yo estoy aquí extraoficialmente, sin uniforme. No sé si me entiende."
    mc "Me parece una buena política."
    scene c25s002_140m with dissolve
    gfu "Ha sido soldado y mercenario en varios conflictos, y después fue operativo de campo en Iron Fist antes de ascender."
    gfu "Se quemó la cara en una de sus misiones. Sobre todo, no se lo menciones."
    gfu "Ya sabes lo que se dice de cuando solo tienes un martillo como ves los problemas."
    mc "Sí, todos los problemas se convierten en clavos."
    scene c25s002_155a with dissolve
    "Se os acerca un hombre al que no habías visto."
    jef "Sr. Marks, Srta. Gilford, soy Jeff Sound, hablamos por teléfono."
    mc "Encantado de conocerle, Sr. Sound."
    scene c25s002_155b with dissolve
    jef "¿Pueden acompañarme? El Sr. Ichigo querría reunirse con ustedes en el jacuzzi."
    mc "Creo que no vengo con el atuendo adecuado para una visita al jacuzzi, Sr. Sound."
    scene c25s002_155c with dissolve
    jef "No se preocupe, la reunión tendrá lugar en los sofás que hay al lado del jacuzzi, no dentro."
    mc "Perdón por el malentendido. Le seguimos."
    scene c25s002_160a with fade
    "Sound os deja en el jacuzzi, donde Ichigo ya está sentado en un sofá y hay una chica en topless dentro del agua."
    "Inteligentemente, el sofá donde se ha sentado solo tiene dos plazas, lo que va a obligar a [ama] a sentarse al lado del jacuzzi o a quedarse de pie."
    "Supones que la chica medio desnuda está para intentar despistaros tanto a [ama] como a ti, tras haber interpretado que [ama] era lesbiana."
    "Todo está perfectamente estudiado. Cada detalle cuenta."
    ich "Siéntate, muchacho."
    "Cada vez que te llama 'muchacho' tienes ganas de estrangularlo. Seguramente también está estudiado para sacarte de tus casillas."
    scene c25s002_160b with dissolve
    "Te sientas al lado de Ichigo. [ama] se sienta al lado del jacuzzi, ignorando a la mujer que hay dentro."
    mc "Aquí estamos. Las vibraciones se parecen poco a la reunión informal de la que habló Sound."
    scene c25s002_160c with dissolve
    ich "*Risa* ¿En cuantas reuniones formales has estado, muchacho? ¿Cuántas tenían putas?"
    mc "He estado en unas cuantas reuniones formales, aunque no había prostitutas en ninguna, en eso tiene razón."
    mcp "(¿Las reuniones con los profesores de la universidad se pueden considerar formales? Voy a tener que empezar a mentir si tengo que tratar con tipos como este.)"
    scene c25s002_160d with dissolve
    ich "Relájate, muchacho. Realmente es una reunión informal para tener un primer contacto. No pienses que esto te viene grande."
    "Deja caer la última frase precisamente para que pienses que no das la talla. Aparte de [ama] y [kim], es posible que seas la persona más joven en el barco."
    ich "Y para ver qué opinan vuestros accionistas sobre una absorción o una fusión."
    mc "No están interesados en vender."
    scene c25s002_160e with dissolve
    ich "Aún no sabes el precio que estamos dispuestos a pagar, muchacho."
    mc "No, pero sabemos lo que podéis pagar, y no es suficiente."
    call BlinkXP ("c25s002_165" , "d") from _call_BlinkXP_3844
    mc "¿Se lo explicas, [ama]?"
    ama "Sabemos que vuestra facturación es algo más de la mitad de la nuestra. Un tercio del valor de NTR aproximadamente."
    scene c25s002_170d with dissolve
    "Consulta el móvil un momento para comprobar la información que encontró Jamaal."
    call BlinkXP ("c25s002_170" , "d") from _call_BlinkXP_3845
    ama "Conociendo vuestro flujo de caja y vuestro presupuesto, creemos que podríais pagar, incluso con financiación externa, un máximo de 600 millones. Más cerca de 500."
    ama "Menos de dos tercios del valor de mercado de NTR, en el mejor de los casos. ¿Me equivoco?"
    "Tras ver que la prostituta no ejerce ningún efecto en [ama], Ichigo le hace una señal para que se vaya."
    scene c25s002_175a with dissolve
    ich "Las cifras estarían en esos valores, sí."
    "Se dirige a ti, como si [ama] no existiera. Si no existe, no hay que hacer caso de las cifras que ha puesto sobre la mesa. No le ha gustado que tuvierais esa información."
    ich "Por eso estaba proponiendo también una fusión, muchacho. Si unimos fuerzas..."
    mc "[ama], ¿puedes darnos números?"
    scene c25s002_175b with dissolve
    "Su falsa sonrisa se crispa por un momento al volver a dirigir la atención de la conversación sobre [ama]."
    call BlinkXP ("c25s002_180" , "d") from _call_BlinkXP_3846
    ama "El valor de mercado de Iron Fist, según nuestros cálculos, ronda los 650 millones. 700 como mucho."
    ama "El valor de NTR supera los 1,000 millones. Si hay una fusión, NTR será la entidad dominante."
    scene c25s002_175c with dissolve
    mc "Y eso no es lo que quieres, ¿verdad?"
    ich "Bueno, creo que esas cifras están un poco sesgadas."
    ich "Ahora mismo, NTR carece de liderazgo y dirección, lo cual rebaja el valor considerablemente. Nosotros podríamos darle el empuje que necesita."
    mc "¿Te parezco una persona que no proporciona liderazgo a la empresa?"
    scene c25s002_175d with dissolve
    ich "Sin querer insultarte, muchacho, no tienes experiencia en este negocio. Cero. O en ningún otro, excepto un dormitorio universitario."
    "Tu cara, que intentas mantener impasible, tiene que reflejar más de lo que esperabas."
    scene c25s002_175e with dissolve
    "La sonrisa de Ichigo se ensancha."
    ich "¿Creías que erais los únicos que sabían buscar información, muchacho?"
    "Mantienes el tono de voz lo más neutral posible."
    mc "Si creyéramos que no sabéis ni siquiera buscar en Foogle, no estaríamos perdiendo el tiempo reuniéndonos con vosotros."
    mc "Es cierto que no tengo experiencia en este negocio, pero tengo un equipo que sí que la tiene."
    mc "No es necesario saber pilotar una nave espacial para construirla. No es necesario ser un operativo de campo para dirigir NTR."
    scene c25s002_175f with dissolve
    ich "Bueno, muchacho, no hace falta que te pongas a la defensiva. Ya te he dicho que esto era una reunión informal."
    ich "Pero creo que sería bueno que le comunicaras a tu familia nuestra oferta. Te la enviaré la semana que viene."
    scene c25s002_175g with dissolve
    ich "¿Quieres que te la mande por correo electrónico o mando un mensajero a tu casa?"
    ich "Y no me refiero al campo de baseball en San Luis Obispo."
    mc "La puedes mandar por correo electrónico. Una vez la reciba, lo consultaré con el resto de los accionistas."
    scene c25s002_185An with dissolve
    "Miras a [ama], que asiente con la cabeza, felicitándote por no haberte comprometido a nada."
    scene c25s002_175h with dissolve
    ich "Entonces, muchacho..."
    "Tienes que mantener las manos quietas para no estrangularlo."
    ich "...vamos a la cubierta principal. Tienen que estar a punto de servir la cena."
    ich "Y esto es una reunión informal. No deberíamos hablar de negocios toda la noche."
    scene c25s002_190a with fade
    "Al llegar a la cubierta principal, ves que han retirado las tumbonas y han puesto algunas mesas altas."
    "No ves al General por ningún lado, pero el resto de los invitados que has visto están aquí, incluso uno que no habías visto hasta ahora. Alguien de Italia."
    ich "Bueno, creo que ha llegado el momento que todos estabais esperando. Veo que nuestro amigo [dav] ya tiene cara de tener hambre."
    dav "*Acento de Europa del Este* *Risa* Ya me conoces. Siempre dispuesto a comer."
    ich "Señoritas, pueden traer la comida."
    scene c25s002_190b with dissolve
    "Aparecen tres camareras con platos de comida que depositan en las mesas."
    dav "¿Sólo hay esto? *Risa* ¿No vas a dar de comer al resto de tus invitados, puto Japo? Esto se lo come [dav] él solo."
    scene c25s002_190An with dissolve
    "A Ichigo se le crispan las facciones por un momento pero disimula rápidamente. No sabes si por lo de 'Japo' o por lo desagradable que es el serbio."
    ich "Tranquilo, Dave, tenéis más comida dentro si queréis. Y bebida. Toda la que queráis."
    ich "Además, ahora llega el plato principal. No te va a decepcionar."
    stop music fadeout (1.5)
    scene c25s002_190e with dissolve
    ich "Podéis traer las bandejas."
    play music ("music/Epic-Adventure-Action.ogg")
    scene c25s002_190f with dissolve
    "Dos de los guardaespaldas traen las tumbonas con chicas sirviendo como bandejas de sushi. Siempre habías pensado que tenían que estar desnudas."
    "Estas conservan los ligueros y las medias, para dar más impresión de algo fetichista."
    "El espectáculo y la compañía te han quitado el poco hambre que pudieras haber tenido."
    dav "¡Eso le gusta más a [dav]!"
    scene c25s002_190g with dissolve
    "Nada más llegar las bandejas humanas, el serbio se lanza como una bestia sobre una de las chicas. El tipo de las tríadas hace lo mismo, más delicadamente."
    scene c25s002_190j with dissolve
    "El invitado que no reconoces, el italiano, y la política mejicana están asqueados con la actuación del serbio."
    scene c25s002_190h with dissolve
    "Te apartas del grotesco espectáculo y te apoyas en la borda, cerca de una de las estaciones de armas."
    "Se te pasa por la mente girar la ametralladora y barrer la cubierta del barco. Si no fuera por las chicas y porque no sabes disparar ametralladoras..."
    call BlinkXP ("c25s002_195" , "d") from _call_BlinkXP_3847
    ama "¿Estás muy asqueado?"
    mc "No te lo puedes llegar a imaginar. ¿Siempre son así estas 'fiestas'?"
    call BlinkXP ("c25s002_200" , "d") from _call_BlinkXP_3848
    ama "Es la primera en la que estoy. Me dan ganas de sacar el arma y hacer una barbaridad."
    mc "*Risa triste* Yo estaba pensando en las estaciones de armas hace un segundo."
    call BlinkXP ("c25s002_205" , "d") from _call_BlinkXP_3849
    ama "No sabía que iba a ser así. Ni que sabían lo de la familia y el dormitorio."
    ama "Si lo hubiera sabido, hubiéramos rechazado la invitación. Ha sido una muestra de que te han investigado."
    mc "Bueno, ahora lo sabemos. También sabremos cuánto ofrecen, aunque no vayamos a vender."
    call BlinkXP ("c25s002_210" , "d") from _call_BlinkXP_3850
    ama "¿De qué nos va a servir eso?"
    mc "Sabiendo cuanto ofrecen podemos saber cuánto tienen y, a través de eso, cuánto valen. Ya no será 500 o 600 millones. Será una cifra más concreta."
    call BlinkXP ("c25s002_215" , "d") from _call_BlinkXP_3851
    ama "Repito. ¿De qué nos va a servir eso? No estás pensando en comprar Iron Fist, ¿verdad? No podríamos hacerlo y..."
    mc "No sé de qué nos va a servir, [ama]. Pero parece que la información es poder en este juego. Y no, no quiero comprar... esto."
    mc "Si vamos a cerrar la parte de NTR dedicada a las operaciones encubiertas, no nos aportaría nada..."
    mc "Aparte de la satisfacción por eliminar Iron Fist, a Ichigo, y este puto barco."
    scene c25s002_220a with dissolve
    dav "¡Japo! Antes había tres tumbonas. ¿No hay tres chicas?"
    scene c25s002_220An with dissolve
    "Ichigo te mira antes de hacer una seña a uno de los guardaespaldas, que trae la tercera tumbona. Vacía."
    dav "¿Una tumbona sin chica? ¿Nos estás timando?"
    scene c25s002_220f with dissolve
    ich "Trae a la chica."
    "La mirada de Ichigo antes de pedir la tumbona te ha dado escalofríos."
    call BlinkXP ("c25s002_225" , "d") from _call_BlinkXP_3852
    mc "¿Qué está pasando, [ama]? ¿A qué ha venido esa mirada?"
    ama "No tengo ni idea. Debes estar preparado para cualquier cosa."
    scene c25s002_230a with fade
    "El guardaespaldas vuelve un par de minutos después, acompañando a [kim]. Hace bien no mirándote, con su mirada fija en Ichigo."
    "Cada vez estás más convencido de que vas a tener que usar la estación de armas."
    scene c25s002_230b with dissolve
    dav "¡Oh, sí! ¡La vaca suiza! A [dav] le gusta la idea."
    "O coger el arma de [ama] y pegarle un tiro al serbio."
    scene c25s002_230c with dissolve
    ich "Chica, quítate el uniforme y estírate en la tumbona. Déjate solo la ropa que llevan las otras chicas."
    kim "¿Qué?"
    scene c25s002_230An with dissolve
    "[kim] os mira incrédula y desamparada, alternando la mirada entre Ichigo y tú."
    "Ichigo te mira con aires de superioridad. Te ha demostrado que puede hacer daño a personas cercanas a ti."
    $ kim._var("chanceSaved", True)
    $ kim._var("chanceRoute", True)
    if persistent.walkthrough:
        if kim.rps>-5:
            $ wt1 = _("[gr][kim] + 30.\n[gr]Podrás abrir la ruta con [kim] más tarde a tu elección.")
        else:
            $ wt1 = _("[gr][kim] + 30.\n[red]No podrás abrir la ruta con [kim] debido a tus decisiones anteriores.")
        $ wt2 = _("[red][kim] - 50.\n[red]No podrás abrir la ruta con [kim].")
    else:
        $ wt1 = ""
        $ wt2 = ""
    menu:
        "Salvar al soldado [kim]." (wt=wt1):
            $ kim._var("saved", True)
            $ kim.rp (30)
            call c25s002_SaveKim from _call_c25s002_SaveKim
        "No hacerlo." (wt=wt2):
            $ kim._var("saved", False)
            $ kim.rp (-50)
            call c25s002_DontSaveKim from _call_c25s002_DontSaveKim
    $ resetWalkthrough()
    return
label c25s002_SaveKim:
    mc "Espera... Japo Cara Quemada."
    "Tú también quieres jugar al juego de sacar a la gente de sus casillas y vas con toda la artillería."
    scene c25s002_235a with hpunch
    "Ichigo se crispa. No era disgusto por el serbio."
    ich "¿Qué quieres, muchacho? Nuestro amigo serbio tiene hambre."
    mc "Me has dicho antes que me podía llevar a cualquier chica a un camarote privado. La elijo a ella."
    mc "Me la voy a llevar a un camarote ahora mismo."
    scene c25s002_235b with dissolve
    dav "¡Nos has dicho que cualquiera menos ella, Japo!"
    scene c25s002_235c with dissolve
    mc "A mí me ha dicho cualquier chica y quiero a esa. ¿O esa es la forma de hacer negocios de Iron Fist?"
    mc "¿Promete cosas que no puede cumplir?"
    scene c25s002_235d with dissolve
    aga "El Sr. Marks tiene razón. Le ha dicho que podía escoger cualquier chica. Yo estaba ahí."
    "Sabes que Alejandra está tan asqueada por el espectáculo como tú, y decide unirse a tu bando aunque no sabe lo que está en juego."
    scene c25s002_235An with dissolve
    ich "Todos tenéis razón. He dicho que estaba fuera de límites y he cometido un error al decirle al Sr. Marks que podía escoger cualquier chica."
    ich "Puedes escoger cualquier chica menos esta, muchacho. Esta es para disfrute de todos."
    scene c25s002_235g with hpunch
    "[kim] os mira a [ama] y a ti desvalida y asustada a partes iguales."
    mc "¿Así es como Iron Fist hace negocios? ¿Ichigo comete un error, promete algo que no puede, o no quiere, cumplir, y ahora se retracta?"
    mc "Espero que no os haga lo mismo cuando lo contratéis para una operación de la que dependan vuestras organizaciones."
    "Notas la mano de [ama] en la espalda, diciéndote que lo estás haciendo bien."
    scene c25s002_235d with dissolve
    aga "Ahí te ha pillado, Ichigo. Creo que le deberías permitir irse con la chica."
    aga "Estoy segura de que cualquiera de las chicas que se han estado paseando con las tetas al aire podrán sustituirla."
    aga "Incluso puedes dejar que [dav] escoja la que quiera como compensación."
    scene c25s002_235h with dissolve
    ich "Bueno, si lo he prometido, debo cumplir. Te puedes llevar a la chica y que [dav] elija su sustituta."
    "Temes por las otras camareras por un momento. Pero ellas no son familia."
    dav "A [dav] le parece una buena idea. Elijo a la puta de las tetas grandes. *Risa* ¡A ver cómo se aguanta el sushi en esas tetas!"
    scene c25s002_235i with hpunch
    "Coges a [kim] del brazo y te la llevas hacia el interior del barco antes de que alguien cambie de opinión."
    kim "¿Qué está pasando, [mc]?"
    mc "Luego, [kim]."
    stop music fadeout (1.5)
    return
label c25s002_DontSaveKim:
    call BlinkXP ("c25s002_240" , "d") from _call_BlinkXP_3853
    ama "Espera... Japo Cara Quemada."
    "Ella también quiere jugar al juego de sacar a la gente de sus casillas y va con toda la artillería."
    scene c25s002_235a with hpunch
    "Ichigo se crispa. No era disgusto por el serbio."
    ich "¿Qué quiere, Srta. Gilford? Nuestro amigo serbio tiene hambre."
    call BlinkXP ("c25s002_245" , "d") from _call_BlinkXP_3854
    ama "Me has dicho antes que me podía llevar a cualquier chica a un camarote privado. La elijo a ella."
    ama "Me la voy a llevar a un camarote ahora mismo."
    scene c25s002_235b with dissolve
    dav "¡Nos has dicho que cualquiera menos ella, Japo!"
    call BlinkXP ("c25s002_250" , "d") from _call_BlinkXP_3855
    ama "A mí me ha dicho cualquier chica y quiero a esa. ¿O esa es la forma de hacer negocios de Iron Fist?"
    ama "¿Promete cosas que no puede cumplir?"
    scene c25s002_235d with dissolve
    aga "La Srta. Gilford tiene razón. Le ha dicho que podía escoger cualquier chica. Yo estaba ahí."
    "Sabes que Alejandra está tan asqueada por el espectáculo como tú, y decide unirse al bando de [ama] aunque no sabe lo que está en juego."
    scene c25s002_235An with dissolve
    ich "Todos tenéis razón. He dicho que estaba fuera de límites y he cometido un error al decirle a la Srta. Gilford que podía escoger cualquier chica."
    ich "Puede escoger cualquier chica menos esta, Srta. Gilford. Esta es para disfrute de todos."
    scene c25s002_235g with hpunch
    "[kim] os mira a [ama] y a ti desvalida y asustada a partes iguales. Decides intervenir."
    mc "¿Así es como Iron Fist hace negocios? ¿Ichigo comete un error, promete algo que no puede, o no quiere, cumplir, y ahora se retracta?"
    mc "Espero que no os haga lo mismo cuando lo contratéis para una operación de la que dependan vuestras organizaciones."
    "Notas la mano de [ama] en tu brazo, diciéndote que lo estás haciendo bien."
    scene c25s002_235d with dissolve
    aga "Ahí te ha pillado, Ichigo. Creo que le deberías permitir irse con la chica."
    aga "Estoy segura de que cualquiera de las chicas que se han estado paseando con las tetas al aire podrán sustituirla."
    aga "Incluso puedes dejar que [dav] escoja la que quiera como compensación."
    scene c25s002_235h with dissolve
    ich "Bueno, si lo he prometido, debo cumplir. Te puedes llevar a la chica y que [dav] elija su sustituta."
    "Temes por las otras camareras por un momento. Todas miran asustadas a [dav]."
    "Pero ellas no son familia. Estás complacido de que [ama] haya sabido reaccionar."
    "Quizás puedas hacer lo mismo si elige a una camarera..."
    dav "A [dav] le parece una buena idea. Elijo a la puta de las tetas grandes. *Risa* ¡A ver cómo se aguanta el sushi en esas tetas!"
    scene c25s002_235j with hpunch
    "Ves que [ama] coge a [kim] del brazo y se la lleva hacia el interior del barco antes de que alguien cambie de opinión."
    kim "¿Qué está pasando, [ama]?"
    ama "Luego, [kim]."
    stop music fadeout (1.5)
    if _in_replay:
        call c25s002_NoKimSaved from _call_c25s002_NoKimSaved_1
    return
label c25s002_KimSaved:
    if _in_replay:
        call mrS3_kim_rps (5, 10, 15) from _call_mrS3_kim_rps_1
        call mrS3_kim_makeup from _call_mrS3_kim_makeup
        $ kim._var("saved", True)
        call mrS3_ama_route from _call_mrS3_ama_route_8
        $ aga = Character ("Alejandra García", color="#ff0000")
    call BlinkXPS3 ("c25s002_325" , "f") from _call_BlinkXPS3_2141
    play music ("music/UnforeseenMotive.ogg")
    "Mientras vas con [kim] hacia el camarote..."
    ama "{i}(Joder, como se ha complicado todo.){/i}"
    call BlinkXPS3 ("c25s002_255" , "d") from _call_BlinkXPS3_2142
    "Un par de minutos después..."
    aga "¿Qué tiene Ichigo contra vosotros? Lo de esa chica parecía algo personal."
    call BlinkXPS3 ("c25s002_330" , "d") from _call_BlinkXPS3_2143
    ama "No es un tema personal, sino de negocios. Estaba haciendo una competición a ver quién tenía la polla más grande."
    ama "La chica se aloja en el dormitorio universitario que es el negocio de la familia de [mc], e Ichigo quería demostrar que podía atacarnos por ahí."
    call BlinkXPS3 ("c25s002_260" , "d") from _call_BlinkXPS3_2144
    aga "Ichigo siempre me ha parecido un tipo muy zafio, pero usar a una chica así es demasiado incluso para él."
    aga "Ha tenido que aceptar la derrota temporalmente pero, si puedes, indícale a [mc] que no salga del camarote hasta que no acabe la fiesta."
    call BlinkXPS3 ("c25s002_335" , "d") from _call_BlinkXPS3_2145
    ama "Gracias, Alejandra. Lo haré."
    ama "Y gracias también por apoyarnos antes."
    call BlinkXPS3 ("c25s002_265" , "d") from _call_BlinkXPS3_2146
    aga "Como te he dicho, Ichigo me parece zafio y despreciable. No me gusta cómo trata a las mujeres en estas fiestas."
    aga "No es que me haya puesto de vuestro lado, pero me ha gustado verle mordiendo el polvo por una vez."
    call BlinkXPS3 ("c25s002_340" , "d") from _call_BlinkXPS3_2147
    ama "De todas formas, gracias."
    call BlinkXPS3 ("c25s002_270" , "d") from _call_BlinkXPS3_2148
    aga "Ahora te tengo que dejar. Tengo que seguir la conversación con nuestro amigo italiano."
    call BlinkXPS3 ("c25s002_345" , "d") from _call_BlinkXPS3_2149
    ama "Me gustaría llamarte algún día. Estamos reorientando el negocio y quizás México sería un buen sitio por el que comenzar."
    call BlinkXPS3 ("c25s002_270" , "d") from _call_BlinkXPS3_2150
    aga "Perfecto. Siempre es bueno tener otras opciones para según qué trabajos."
    stop music fadeout (1.5)
    scene c25s002_350a with fade
    "Mientras tanto..."
    play music ("music/Separation.ogg")
    "Cuando estás llegando a los camarotes, te cruzas con el general, que sale de una habitación con una de las chicas que había en la piscina."
    "Os ignoráis mutuamente más allá de una mirada. Tú sabes lo que él ha venido a hacer y el cree que tú vienes a lo mismo."
    scene c25s002_350b with fade
    "Entras en un camarote vacío y cierras la puerta con pestillo."
    "La cama está hecha, con lo que parece que nadie lo ha usado."
    call BlinkXPS3 ("c25s002_355" , "d") from _call_BlinkXPS3_2151
    kim "¿Qué ha pasado ahí? ¿Por qué quería el Sr. Ichigo que me desnudara?"
    kim "¿Qué hacéis aquí [ama] y tú? ¿Iron Fist es la compañía rival de la que hablabais?"
    mc "Sí, [kim]. Iron Fist es la empresa que quería comprar NTR. Y cuando nos hemos negado, han intentado usarte para castigarnos."
    mc "¿Es el mismo yate donde estuviste el miércoles?"
    call BlinkXPS3 ("c25s002_360" , "d") from _call_BlinkXPS3_2152
    kim "Sí, pero entonces era diferente. Sólo había militares de uniforme, y no vi nada como lo de las chicas sirviendo como bandejas de sushi."
    kim "Pero no me moví del helipuerto, con lo que tampoco puedo asegurar que no pasara."
    mc "¿Y las ametralladoras en la cubierta no te hicieron pensar nada raro?"
    call BlinkXPS3 ("c25s002_365" , "d") from _call_BlinkXPS3_2153
    kim "No soy estúpida, [mc]. Si hubiera visto las ametralladoras se lo hubiera comentado a [eva] y a [ama]. Me hubiera parecido sospechoso."
    kim "Pero estaban tapadas con unas lonas grises. Hasta que no he llegado hoy no las he visto."
    mc "Supongo que no había prostitutas tampoco, ¿no?"
    call BlinkXPS3 ("c25s002_370" , "d") from _call_BlinkXPS3_2154
    kim "No, ni tampoco mafiosos serbios, italianos, o chinos. Adeline ha estado conmigo casi toda la tarde, y era ella la que acompañaba a los invitados."
    kim "Lo mismo pasó el otro día, pero hacia el final del evento me hicieron ir a la cubierta de la piscina para ayudar a recoger."
    play sound ("music/notification.ogg")
    "Suena tu teléfono. Es un mensaje de [ama] indicándote que te quedes en el camarote hasta que ella te lo diga. No le dices nada a [kim]."
    call BlinkXPS3 ("c25s002_375" , "d") from _call_BlinkXPS3_2155
    kim "Hoy ha sido un poco diferente. Yo tenía órdenes de quedarme en el helipuerto hasta que llegara el último helicóptero."
    kim "Era el vuestro. No me habían dicho el nombre de la empresa."
    mc "Lo han hecho de tal forma que te mantenían apartada y segura hasta que fuera necesario utilizarte para intentar hacernos daño."
    mc "Siento que te hayas visto involucrada en esto."
    call BlinkXPS3 ("c25s002_380" , "h") from _call_BlinkXPS3_2156
    kim "Gracias por salvarme. Tú no tienes la culpa, pero has evitado que tuviera que hacer... eso."
    mc "No podía aceptar que te usaran para atacar a NTR. No por NTR, sino por ti."
    mc "Nunca he compartido lo de que los daños colaterales son necesarios, y a Ichigo parece que no le importaba usarte a ti para darnos una lección."
    call BlinkXPS3 ("c25s002_385" , "d") from _call_BlinkXPS3_2157
    kim "Pero la lección se la has dado tú. Espero que no tenga consecuencias para vosotros. Para mí..."
    mc "¿Qué puede hacer? No te contrató directamente. Tus jefes son la agencia, ¿no?"
    call BlinkXPS3 ("c25s002_390" , "d") from _call_BlinkXPS3_2158
    kim "Sí, pero si pone alguna queja en la agencia sobre mí, posiblemente no me vuelvan a contratar."
    mc "No lo había pensado... En ese caso podríamos hablar con la agencia. Supongo que no les gustará que te hayan querido usar como bandeja de sushi."
    call BlinkXPS3 ("c25s002_395" , "d") from _call_BlinkXPS3_2159
    kim "Sería mi palabra contra la del cliente. No serviría de nada. Cuando casi me obliga a desnudarme no había nadie más de la agencia."
    kim "Las chicas del sushi no eran de mi agencia, y las prostitutas tampoco."
    mc "¿La agencia abre mañana? Es domingo."
    call BlinkXPS3 ("c25s002_400" , "d") from _call_BlinkXPS3_2160
    kim "Creo que no. ¿Por qué lo preguntas?"
    mc "Porque se me está ocurriendo una idea. Tendré que hablar con [ama]."
    scene c25s002_400d with vpunch
    "[kim] se derrumba sobre la cama, con la cara ente las manos."
    mc "¿Estás bien, [kim]?"
    call BlinkXPS3 ("c25s002_405" , "d") from _call_BlinkXPS3_2161
    kim "Ha empezado a temblarme todo. Me he puesto muy nerviosa con la situación del Sr. Ichigo, y supongo que..."
    mc "La adrenalina del momento te está abandonando."
    kim "Sí, no sabía cómo reaccionar. Tenía ganas de salir corriendo, pero no había dónde huir."
    mc "¿Quieres tumbarte un rato? Parece que vamos a estar un rato aquí..."
    call BlinkXPS3 ("c25s002_410" , "d") from _call_BlinkXPS3_2162
    kim "No sé lo que quiero, [mc]. Quiero estar lejos de este barco..."
    mc "Lo entiendo."
    kim "Quiero que me abraces, sentirme segura..."
    mc "Eso puedo hacerlo, al menos lo de abrazarte. Ven aquí."
    call BlinkXPS3 ("c25s002_415" , "d") from _call_BlinkXPS3_2163
    kim "Se está bien aquí."
    mc "Podemos estar así todo el tiempo que quieras."
    if not kim.rps > 4:
        call c25s003_HeloTrip from _call_c25s003_HeloTrip
        call c25s002_KimHome from _call_c25s002_KimHome
    else:
        call BlinkXPS3 ("c25s002_420" , "d") from _call_BlinkXPS3_2164
        kim "Soy una cobarde, [mc]."
        mc "No lo eres, [kim]. Creo que nadie habría sabido reaccionar en tu situación."
        mc "Estoy seguro de que, si hubiera tardado un par de segundos en decirle a Ichigo que te traía al camarote, lo hubiera hecho [ama]."
        mc "Es la única que está entrenada para reaccionar rápido bajo presión."
        call BlinkXPS3 ("c25s002_425" , "d") from _call_BlinkXPS3_2165
        kim "Pero tú lo has hecho y no estás entrenado. Yo me he quedado ahí, sin saber que hacer, como un conejo deslumbrado por los faros de un coche."
        mc "No le des más vueltas. Lo importante es que estás a salvo."
        mc "Eso no te convierte en una cobarde."
        call BlinkXPS3 ("c25s002_430" , "d") from _call_BlinkXPS3_2166
        kim "Si no fuese una cobarde te estaría besando ahora mismo."
        mc "No tienes por qué hacerlo por agradecimiento. [ama] hubiera hecho lo mismo si le hubiera dado tiempo."
        call BlinkXPS3 ("c25s002_435" , "d") from _call_BlinkXPS3_2167
        kim "No sería... sólo... por agradecimiento..."
        if persistent.family:
            mc "Pero querías hablar con mi madre, ¿no?"
        else:
            mc "Pero querías hablar con [mar], ¿no?"
        call BlinkXPS3 ("c25s002_440" , "d") from _call_BlinkXPS3_2168
        kim "Sí, y lo hice mientras estabais en Monterey."
        kim "Otra muestra de cobardía. Me tuvo que obligar [kat]. Me hizo lo que [deb.nick] te hizo a ti con [lis]."
        $ kim._var("chanceRoute", True)
        if persistent.walkthrough:
            $ wt1 = _("[gr]Ruta con [kim] abierta.")
            $ wt2 = _("[red]Ruta con [kim] cerrada.\n[red]ADVERTENCIA: No habrá más oportunidades de abrir la ruta con [kim].")
        else:
            $ wt1 = ""
            $ wt2 = ""
        menu:
            "Espero que te diera autorización para salir conmigo.\nPorque voy a besarte." (wt=wt1):
                $ kim._var("route", True)
                call c25s002_KimRoute from _call_c25s002_KimRoute
                call c25s002_KimHome from _call_c25s002_KimHome_1
            "Espero que te gustara su respuesta, aunque eso no va a cambiar nada.\nTe quiero pero no de esa forma." (wt=wt2):
                $ kim._var("route", False)
                call c25s002_NoKimRoute from _call_c25s002_NoKimRoute
    return
label c25s002_KimRoute:
    call BlinkXPS3 ("c25s002_475" , "d") from _call_BlinkXPS3_2169
    kim "Me dijo que no le importaba que..."
    call BlinkXPS3 ("c25s002_480" , "h") from _call_BlinkXPS3_2170
    stop music fadeout (1.5)
    kim "¿QUÉ? ¿Has dicho que vas a besarme?"
    play music ("music/You-Know-Instrumental.ogg")
    scene c25s002_480d with hpunch
    "Vale más una imagen, o en este caso un beso, que mil palabras. Acallas sus preguntas poniendo tus labios sobre los suyos."
    "Se queda paralizada como un conejo deslumbrado por los faros de un coche."
    "Es como besar una estatua. Una estatua que respira en tu boca, y cuyos labios son deliciosamente suaves."
    scene c25s002_480e with dissolve
    "La parálisis tan solo dura unos segundos, hasta que su cerebro procesa lo que está pasando."
    "Entonces la estatua cobra vida y empieza a devolverte el beso torpemente, casi inconscientemente, dejándose llevar por sus instintos."
    scene c25s002_480f with hpunch
    "Por un momento se tensa antes de separarse de ti y darte la espalda."
    kim "¡No!"
    mc "¿No? ¿A qué te refieres?"
    call BlinkXPS3 ("c25s002_485" , "f") from _call_BlinkXPS3_2171
    kim "No soy estúpida, [mc]."
    mc "Lo sé, pero sigo sin saber a qué te refieres."
    call BlinkXPS3 ("c25s002_490" , "d") from _call_BlinkXPS3_2172
    kim "Sé para qué se usan estos camarotes..."
    mc "¿Crees que Ichigo y yo nos hemos puesto de acuerdo para que montase el espectáculo en la cubierta y tuviera la oportunidad de traerte aquí y tener sexo contigo?"
    kim "No... Dicho en voz alta... Parece que sí. Soy estúpida."
    mc "No lo eres. Hoy te han pasado cosas raras y tu mente aún las está procesando."
    call BlinkXPS3 ("c25s002_495" , "d") from _call_BlinkXPS3_2173
    kim "¿Como que me beses?"
    mc "Bueno, eso no lo consideraría raro. He estado esperando mucho tiempo para hacerlo."
    call BlinkXPS3 ("c25s002_500" , "d") from _call_BlinkXPS3_2174
    kim "Sabes que podrías haberlo hecho hace varios días, ¿verdad?"
    if persistent.family:
        mc "No. No hasta que no hubieras tenido la conversación con mi madre."
    else:
        mc "No. No hasta que no hubieras tenido la conversación con [mar]."
    mc "No te hubieras sentido a gusto si lo hubiera hecho antes de esa conversación."
    call BlinkXPS3 ("c25s002_505" , "d") from _call_BlinkXPS3_2175
    kim "Pero ahora... me sentiría a gusto si lo repitieras... Lo sabes, ¿verdad?"
    mc "*Risa* Lo sé."
    scene c25s002_480e with dissolve
    "Vuestros labios vuelven a unirse. Esta vez está preparada y el beso devuelto es mucho menos torpe."
    "Y mucho más largo."
    "La tensión de todo lo que ha pasado en la última hora desaparece por completo, sustituida por pasión."
    "El beso dura hasta que [kim] empieza a respirar entrecortadamente en tu boca."
    call BlinkXPS3 ("c25s002_510" , "d") from _call_BlinkXPS3_2176
    kim "*Jadeo* Deberías dejarme respirar. Tengo el corazón que parece que me va a explotar en el pecho."
    mc "*Risa* Eso no tiene que ver con la falta de aire, preciosa. El mío también está latiendo deprisa."
    call BlinkXPS3 ("c25s002_515" , "d") from _call_BlinkXPS3_2177
    kim "¡No te rías de mí!"
    mc "Nunca lo haría."
    if kim._var("makeup"):
        call BlinkXPS3 ("c25s002_520" , "d") from _call_BlinkXPS3_2178
        kim "¿Ni siquiera cuando me dijiste que debería usar el maquillaje corporal?"
        mc "Ni siquiera entonces. Te lo dije porque parecías más segura de ti misma y porque te importaba lo que tus compañeras pensaran."
        mc "No porque a mí no me guste tu piel."
        call BlinkXPS3 ("c25s002_525" , "d") from _call_BlinkXPS3_2179
        kim "¿De verdad te gusta?"
        mc "Es como un mapa que me encantaría pasarme una noche recorriendo."
        call BlinkXPS3 ("c25s002_530" , "d") from _call_BlinkXPS3_2180
        kim "Puedes hacerlo ahora..."
    else:
        call BlinkXPS3 ("c25s002_535" , "d") from _call_BlinkXPS3_2181
        kim "Lo sé. Lo descubrí el día que me dijiste que no necesitaba usar el maquillaje corporal."
        kim "Visto ahora que han pasado dos semanas... podías haberte reído de mí, y no lo hiciste."
        mc "Nunca me reiría de ti. Y menos por algo que para ti es tan importante."
        mc "Me gusta tu piel y..."
        call BlinkXPS3 ("c25s002_540" , "d") from _call_BlinkXPS3_2182
        kim "Y es como un mapa que te pasarías la noche recorriendo con los dedos..."
        mc "¿Te acuerdas?"
        call BlinkXPS3 ("c25s002_545" , "d") from _call_BlinkXPS3_2183
        kim "No podría olvidarlo. En ese momento empecé a sentir algo por ti. Aún no lo sabía, pero... me di cuenta de que no me mirabas como me mira todo el mundo."
        mc "[kim], eres especial. Eres preciosa. No eres como las demás chicas, cierto. Pero no por ello eres menos hermosa."
        call BlinkXPS3 ("c25s002_530" , "d") from _call_BlinkXPS3_2184
        kim "Sabes que podrías empezar a recorrer ese mapa ahora, ¿no?"
    mc "No creo que sea el lugar más adecuado para nuestra primera vez."
    scene c25s002_550a with hpunch
    kim "¿Qué? ¡No! ¡No me refería a eso!"
    kim "No me gustaría que nuestra primera vez fuera en este barco, ni en un camarote donde... ya sabes..."
    mc "Exacto. ¿A qué te referías, entonces?"
    call BlinkXPS3 ("c25s002_555" , "d") from _call_BlinkXPS3_2185
    kim "A que puedes recorrer el mapa... en las zonas visibles..."
    kim "Me encantaría sentir tus dedos sobre la piel, pero no me gustaría quitarme la ropa... aquí."
    mc "Me parece una idea genial. Túmbate mientras me quito la chaqueta."
    call BlinkXPS3 ("c25s002_560" , "f") from _call_BlinkXPS3_2186
    kim "¿Así?"
    mc "Así estás perfecta. Siempre estás perfecta."
    mc "¿Puedo empezar a recorrer el mapa con los dedos?"
    kim "Cuando quieras..."
    scene c25s002_560d with dissolve
    kim "¿Qué estás haciendo, [mc]?"
    mc "*Risa* Ya te lo he dicho, recorrer el mapa con los dedos."
    kim "[mc], ¿puedes mirarme un momento?"
    scene c25s002_565An with dissolve
    "Una almohada salta inesperadamente de la mano de [kim] a tu cara."
    kim "*Risa* Eso te pasa por reírte de mí. ¡Has dicho que nunca lo harías!"
    mc "*Risa* Al menos has quitado la chocolatina que había encima de la almohada antes de tirármela."
    call BlinkXPS3 ("c25s002_570" , "d") from _call_BlinkXPS3_2187
    kim "*Risa* Me la he comido antes, cuando has empezado a hacer el tonto con el mapa de la pared."
    mc "*Risa* He tenido suerte. No querría ser el protagonista del titular 'Pierde un ojo por culpa de una chocolatina'."
    mc "¿Preparada?"
    call BlinkXPS3 ("c25s002_575" , "d") from _call_BlinkXPS3_2188
    kim "Cuando quieras."
    mc "¿Por dónde quieres que empiece?"
    kim "Por donde quieras. Espero que en los próximos días encuentres el camino al tesoro en el mapa."
    kim "Cuando estemos en algún otro sitio."
    scene c25s002_580An with dissolve
    "Empiezas a recorrer la suave mano de la modelo, recorriendo con la yema de tu dedo la frontera en su piel donde cambia de color."
    mc "¿Ves? Si usaras maquillaje corporal, no podría hacer esto. Los exploradores se perderían sin un mapa que seguir."
    kim "*Risa* ¿Siempre le ves el lado bueno a las cosas?"
    call BlinkXPS3 ("c25s002_585" , "d") from _call_BlinkXPS3_2189
    mc "Si sólo tuviera que mirar el lado bueno de las cosas, nunca más podría apartar la mirada de donde la tengo puesta ahora mismo."
    kim "Es lo más bonito que me han dicho nunca, [mc]."
    scene c25s002_590An with dissolve
    mc "Este trozo en tu muslo me recuerda a un mapa medieval de Irlanda que vi una vez."
    mc "Me podría pasar horas recorriendo las costas de nuestra Irlanda particular."
    kim "Tus dedos me están dando escalofríos..."
    call BlinkXPS3 ("c25s002_595" , "d") from _call_BlinkXPS3_2190
    mc "¿Quieres que pare?"
    kim "Quiero que sigas recorriéndome, pero ya lo sabes... sólo las zonas visibles..."
    kim "Solo de pensar en quitarme la ropa aquí... "
    scene c25s002_600An with dissolve
    mc "Lo sé, preciosa. Le quitaría toda la magia."
    mc "Pero no te preocupes, hay suficientes zonas visibles que quiero recorrer."
    mc "Siempre me ha parecido espectacular esta forma, como si estuvieras en un baile de máscaras..."
    kim "Pero eso no es un mapa, entonces..."
    mc "Si me dejas decir la cursilada del día, te diré que es el mapa que lleva a tus ojos. Es una de las partes que más me gustan de ti."
    call BlinkXPS3 ("c25s002_605" , "d") from _call_BlinkXPS3_2191
    kim "*Risa* Sí. Ha sonado muy cursi. Pero me ha encantado."
    kim "Normalmente me dicen que parezco un mapache..."
    mc "¡Pues te nombro Miss Mapache California 2023! *Risa*"
    kim "*Risa* ¡Eres increíble!"
    call BlinkXPS3 ("c25s002_610" , "d") from _call_BlinkXPS3_2192
    mc "¿Sabes lo que le falta a este mapa?"
    kim "¿Qué?"
    mc "Besos. Le faltan muchos besos."
    scene c25s002_610d with dissolve
    "Vuelves a la mano, donde has empezado el recorrido por el mapa, repartiendo besos en sus nudillos, donde la piel cambia entre dos maravillosos colores."
    kim "Aquí arriba hay un lugar que no has explorado aún."
    call BlinkXPS3 ("c25s002_615" , "d") from _call_BlinkXPS3_2193
    kim "Creo que también necesita besos."
    mc "Pero eso sería hacer trampas. ¿Te he visto alguna vez sin pintalabios? Ni siquiera en la piscina puedo recordarte sin pintalabios."
    call BlinkXPS3 ("c25s002_620" , "d") from _call_BlinkXPS3_2194
    kim "Creo que la primera vez que subimos al lago no llevaba. Se me había acabado."
    kim "Siempre llevo. Tengo unos labios muy feos..."
    mc "Creo que eso debería decidirlo yo. Al menos decidir si me gustan."
    call BlinkXPS3 ("c25s002_625" , "d") from _call_BlinkXPS3_2195
    kim "Puedes empezar por explorarlos con los tuyos. A lo mejor consigues borrarlo..."
    mc "Suena como un buen plan."
    mc "Pero... es pintalabios de ese que no se quita ni con disolvente industrial, ¿verdad?"
    scene c25s002_625d with dissolve
    kim "*Risa* Sí."
    scene c25s002_625e with dissolve
    "A ninguno de los dos os importa."
    "Os besáis durante un largo rato. No sabéis si dos minutos o dos horas."
    scene c25s002_625f with dissolve
    "Tampoco os importa."
    play sound ("music/notification.ogg")
    "Podrían haber sido dos años y, pese a todo, cuando suena tu móvil os hubiera costado igual separaros."
    call BlinkXPS3 ("c25s002_630" , "f") from _call_BlinkXPS3_2196
    mc "Es [ama]. El helicóptero nos está esperando."
    kim "¿Nos vamos ya?"
    mc "Sí. Ha hablado con Sound sobre ti."
    kim "El Sr. Sound parece un buen tipo."
    "Ni un átomo de pintalabios ha desaparecido de los labios de la azafata."
    stop music fadeout (1.5)
    call c25s003_HeloTrip from _call_c25s003_HeloTrip_1
    return
label c25s002_KimHome:
    scene c25s002_295e with fade
    "El helicóptero os deja en el parking de la galería de tiro y [ama] os lleva a casa."
    "Estáis demasiado cansados para hablar sobre lo que ha pasado."
    scene c25s002_300a with dissolve
    play music ("music/Inspire.ogg")
    "Al llegar a casa..."
    kim "Gracias por todo, [ama]."
    ama "Yo no he hecho casi nada. Le tienes que dar las gracias al héroe de la noche."
    kim "Ahora lo haré, no te preocupes."
    if kim._var("route"):
        call KissXPS3 ("c25s002_635" , "d") from _call_KissXPS3_40
        kim "Te veo mañana, cielo. Estoy cansadísima."
    else:
        scene c25s002_635a with dissolve
        kim "Te veo mañana, [mc]. Estoy cansadísima."
    mc "Hasta mañana, guapísima. Descansa. Te lo mereces."
    scene c25s002_300e with dissolve
    "[kim] se mete en casa sin decir una palabra más y sin mirar atrás."
    if kim._var("route"):
        call BlinkXPS3 ("c25s002_320" , "f") from _call_BlinkXPS3_2197
        ama "*Risita* Parece que habéis aprovechado el tiempo en el camarote."
        mc "Bueno, hemos hablado, una cosa ha llevado a la otra y... supongo que mañana os lo explicará en el grupo de WhatsUp."
        mc "Por si tienes curiosidad, no nos hemos quitado la ropa. No era el mejor sitio para hacerlo."
        call BlinkXPS3 ("c25s002_640" , "d") from _call_BlinkXPS3_2198
        ama "No, [mc]. No tengo curiosidad. Tan solo me alegro por vosotros."
        mc "Gracias, [ama]."
    if ama._var("route"):
        call KissXPS3 ("c25s002_315" , "d") from _call_KissXPS3_41
    else:
        call BlinkXPS3 ("c25s002_320" , "d") from _call_BlinkXPS3_2199
    ama "Te veo mañana."
    mc "Hasta mañana, [ama]."
    scene c25s002_320d with dissolve
    mc "Espera, [ama]. Se me acaba de ocurrir una idea. ¿Tienes un momento?"
    scene black with dissolve
    "Unos minutos después subes a tu habitación, pensando que, quizás, con la idea que se te ha ocurrido a última hora, quizás puedas proteger un poco a [kim]."
    "Te desnudas y te metes en la cama. Compruebas el móvil un rato, esperando el correo electrónico que le has pedido a [ama]."
    "Te duermes antes de que llegue."
    if kim._var("route"):
        "Te despiertas en algún momento de la noche con una sensación extraña. Como de tener algo peludo en la boca."
        scene c25s002_640d with dissolve
        "Hay un precioso mapa con piernas acurrucado contra tu pecho, durmiendo profundamente."
        "Su respiración es relajada, como si estuviera en el lugar en el que se supone que debe estar."
        "Te duermes inmediatamente, sin ni siquiera pensar en que estás desnudo."
    stop music fadeout (1.5)
    return
label c25s002_NoKimRoute:
    if _in_replay:
        $ kim._var("saved", True)
        $ kim._var("route", False)
    call BlinkXPS3 ("c25s002_445" , "d") from _call_BlinkXPS3_2200
    kim "Lo entiendo. Y también entiendo por qué no me quisiste dar una respuesta antes de que hablara con ella."
    mc "¿Sí?"
    call BlinkXPS3 ("c25s002_450" , "d") from _call_BlinkXPS3_2201
    kim "Te lo acabo de decir. Soy una cobarde. Y, al no darme una pista antes de que hablara con ella me has obligado a hacer algo que tenía miedo de hacer."
    kim "Aunque [kat] tuviera que encerrarme con ella en la cocina."
    call BlinkXPS3 ("c25s002_455" , "d") from _call_BlinkXPS3_2202
    kim "De alguna forma siempre nos diriges a hacer lo que necesitamos hacer. Y además haces que parezca idea nuestra."
    kim "Gracias a haberlo hecho, [mar] y yo ahora estamos más unidas. Si me hubieras dicho que no querías salir conmigo, no hubiera pasado."
    kim "No hubiéramos tenido la conversación y no nos sentiríamos como..."
    mc "¿Como si fuera una segunda madre?"
    call BlinkXPS3 ("c25s002_460" , "d") from _call_BlinkXPS3_2203
    kim "¿Qué? ¿Cómo lo sabes?"
    mc "Porque yo pasé por algo parecido con [sam]. Conozco la sensación de sentirte unido a alguien como si fuera una segunda madre."
    if not persistent.family:
        mc "O una tercera, en mi caso."
    mc "Pero ¿puedo serte sincero?"
    call BlinkXPS3 ("c25s002_465" , "d") from _call_BlinkXPS3_2204
    kim "Por supuesto."
    mc "No lo hice para forzarte a una conversación con [mar] que te daba miedo, pero me alegro de que haya acabado así."
    call BlinkXPS3 ("c25s002_470" , "d") from _call_BlinkXPS3_2205
    kim "Entonces no quiero saber por qué lo hiciste. Prefiero seguir creyendo mi teoría."
    kim "¿Podemos quedarnos abrazados un rato?"
    mc "Tanto tiempo como quieras."
    stop music fadeout 1.5
    call c25s003_HeloTrip from _call_c25s003_HeloTrip_2
    call c25s002_KimHome from _call_c25s002_KimHome_2
    return
label c25s002_NoKimSaved:
    if _in_replay:
        $ jef = TGCharacter ("Jeff Sound", color = "#ffffff")
    scene c25s002_190h with fade
    play music ("music/UnforeseenMotive.ogg")
    "Vuelves a dar la espalda a la escena que se está desarrollando en la cubierta."
    "No tienes ninguna intención de participar."
    call BlinkXPS3 ("c25s002_255" , "d") from _call_BlinkXPS3_2206
    "Un par de minutos después..."
    aga "¿Qué tiene Ichigo contra vosotros? Lo de esa chica parecía algo personal."
    mc "No es un tema personal, sino de negocios. Estaba haciendo una competición a ver quién tenía la polla más grande."
    mc "La chica se aloja en el dormitorio universitario que es el negocio familiar e Ichigo quería demostrar que podía atacarnos por ahí."
    call BlinkXPS3 ("c25s002_260" , "d") from _call_BlinkXPS3_2207
    aga "Ichigo siempre me ha parecido un tipo muy zafio, pero usar a una chica así es demasiado incluso para él."
    aga "Ha tenido que aceptar la derrota temporalmente pero, si puedes, indícale a tu amiga que no salga del camarote hasta que no acabe la fiesta."
    mc "Gracias, Alejandra. Lo haré."
    mc "Y gracias también por apoyarnos antes."
    call BlinkXPS3 ("c25s002_265" , "d") from _call_BlinkXPS3_2208
    aga "Como te he dicho, Ichigo me parece zafio y despreciable. No me gusta cómo trata a las mujeres en estas fiestas."
    aga "No es que me haya puesto de vuestro lado, pero me ha gustado verle mordiendo el polvo por una vez."
    mc "De todas formas, gracias."
    call BlinkXPS3 ("c25s002_270" , "d") from _call_BlinkXPS3_2209
    aga "Ahora te tengo que dejar. Tengo que seguir la conversación con nuestro amigo italiano."
    mc "Me gustaría llamarte algún día. Estamos reorientando el negocio y quizás México sería un buen sitio por el que comenzar."
    aga "Perfecto. Siempre es bueno tener otras opciones para según qué trabajos."
    scene c25s002_190h with fade
    "Alejandra desaparece y vuelves a mirar al mar."
    "Mandas un mensaje a [ama] diciéndole que no abandonen el camarote hasta que las avises."
    scene c25s002_275a with fade
    "Al cabo de poco más de una hora..."
    scene c25s002_275b with dissolve
    jef "Sr. Marks, la velada está a punto de acabar. La mayoría de los invitados van a pasar la noche en el barco. ¿Qué desean hacer usted y su acompañante?"
    mc "Volveremos a tierra, si es posible. Y nos llevaremos a la chica del helipuerto."
    scene c25s002_275c with dissolve
    jef "No sé si lo de la chica va a ser posible..."
    mc "Hágalo posible, Sr. Sound. Por lo que sé, su contrato no incluía pasar la noche aquí."
    jef "Deme un minuto para comprobarlo."
    scene c25s002_275d with fade
    "Tras comprobar algo en el móvil..."
    jef "Tiene razón. Las azafatas y las camareras vuelven a tierra en la lancha en una hora más o menos."
    mc "Pues a esa azafata nos la llevaremos nosotros en el helicóptero."
    jef "Como desee. Avíseme cuando estén listos."
    scene c25s002_275e with fade
    "Avisas a [ama] de que puede salir del camarote y subís al helicóptero. Ichigo no está disponible para poder despediros de él."
    stop music fadeout (1.5)
    call c25s003_HeloTrip from _call_c25s003_HeloTrip_3
    call BlinkXPS3 ("c25s002_280" , "f") from _call_BlinkXPS3_2210
    "Al llegar al aparcamiento, [ama] va a por la furgoneta, dejándoos a [kim] y a ti a solas."
    play music ("music/SadSoul.ogg")
    kim "Antes de que lo preguntes, no, no sabía quiénes eran Iron Fist o que eran una empresa rival de NTR."
    "Está visiblemente molesta. Supones que esperaba que fueras tú quien intercediera por ella."
    kim "No, no había visto las ametralladoras la última vez. Estaban tapadas con lonas."
    kim "No, no había mafiosos tampoco la última vez. Tan solo militares de uniforme. Tampoco había mujeres desnudas que yo viera."
    mc "[kim], cálmate. Nadie te está acusando de nada."
    call BlinkXPS3 ("c25s002_285" , "d") from _call_BlinkXPS3_2211
    kim "Lo sé, pero son preguntas que [ama] me ha hecho, y es lógico que tú también quieras saber la respuesta."
    kim "No soy estúpida, ¿sabes? Si hubiera sospechado algo, os lo hubiera dicho."
    mc "Lo sé. Deberías..."
    call BlinkXPS3 ("c25s002_290" , "d") from _call_BlinkXPS3_2212
    kim "¿Qué? ¿Preguntar a la agencia cómo se llama cada cliente? ¿Informaros de quienes son esos clientes por si tienen algo que ver con vuestra empresa?"
    kim "No te preocupes, después de lo de hoy, lo más probable es que el Sr. Ichigo ponga alguna queja sobre mí y me despidan."
    mc "Si necesitas que hablemos con la agencia..."
    call BlinkXPS3 ("c25s002_295" , "d") from _call_BlinkXPS3_2213
    kim "¿Para qué? Vosotros no sois el cliente. Vuestra palabra no tiene ningún peso."
    mc "Pero..."
    kim "Pero nada, [mc]. Lo hecho, hecho está. Por suerte, [ama] ha evitado que pasara algo peor."
    scene c25s002_295d with dissolve
    "En ese momento, llega [ama] con la furgoneta, interrumpiendo la conversación."
    scene c25s002_295e with fade
    "El viaje a casa se produce en silencio, ninguna de las dos chicas tiene ganas de hablar."
    scene c25s002_300a with dissolve
    "Al llegar a casa..."
    kim "Gracias por lo que has hecho en el barco, [ama]."
    ama "No tienes por qué agradecérmelo, [kim]. La familia nos tenemos que cuidar."
    kim "Sí, la familia..."
    ama "Sube a dormir y cálmate. Mañana lo verás todo con otros ojos."
    scene c25s002_300d with dissolve
    kim "Hasta mañana, [mc]."
    mc "Hasta mañana, [kim]. Duerme bien."
    scene c25s002_300e with dissolve
    "[kim] se mete en casa sin mirar atrás o decir nada más."
    call BlinkXPS3 ("c25s002_305" , "d") from _call_BlinkXPS3_2214
    ama "No se lo tengas en cuenta. Está nerviosa y asustada por lo que ha estado a punto de pasarle."
    mc "Y decepcionada porque no he sido yo quién ha intervenido, ¿no?"
    call BlinkXPS3 ("c25s002_310" , "d") from _call_BlinkXPS3_2215
    if kim.rps>-45:
        ama "Creo que sí. Has actuado como el caballero de brillante armadura con varias de las chicas y, cuando ella lo ha necesitado, he tenido que hacerlo yo."
    else:
        ama "Hasta cierto punto. Creo que no esperaba que hicieras lo que he hecho yo, pero tampoco que te quedaras impasible."
    mc "Tienes razón. No he sabido reaccionar, y cuando he podido hacerlo, tú ya lo habías resuelto."
    ama "Al menos has soltado el discurso sobre la forma de hacer negocios de Iron Fist. Eso y lo que ha dicho Alejandra me han permitido sacarla de ahí."
    mc "Es poco consuelo, pero al menos todo ha acabado bien... o no tan mal como podía haberlo hecho."
    if ama._var("route"):
        call KissXPS3 ("c25s002_315" , "d") from _call_KissXPS3_42
    else:
        call BlinkXPS3 ("c25s002_320" , "d") from _call_BlinkXPS3_2216
    ama "No le des más vueltas. En cuanto tenga tiempo de pensar, se le pasará la decepción que tiene contigo ahora mismo. No siempre puedes hacerlo todo bien."
    ama "Hasta mañana, [mc]."
    mc "Hasta mañana, [ama]."
    scene c25s002_320d with dissolve
    mc "Espera, [ama]. Se me acaba de ocurrir una idea. ¿Tienes un momento?"
    scene black with dissolve
    "Unos minutos después subes a tu habitación, pensando que, quizás, podrías haber hecho las cosas de otra forma en el barco."
    stop music fadeout (1.5)
    "Al menos con la idea que se te ha ocurrido a última hora, quizás puedas proteger un poco a [kim]."
    return
label c25s003_HeloTrip:
    if kim._var("saved") and not kim._var("route"):
        play sound ("music/notification.ogg")
        "Sin que os deis cuenta, pasa el tiempo, hasta que suena tu móvil de nuevo. [ama] te indica que ya podéis salir de vuestro refugio."
    if kim._var("saved"):
        scene c25s002_275e with fade
        "Subís a cubierta y al helicóptero. Ichigo no está disponible para poder despediros de él."
    "Crees que es lo mejor."
    "El viaje en helicóptero pasa sin nada reseñable y os vuelve a dejar en el aparcamiento de la galería de tiro."
    return
label c25s003_MyResidence:
    if _in_replay:
        call mrS3_deb_laptop from _call_mrS3_deb_laptop_1
        call mrS3_deb_route from _call_mrS3_deb_route_9
    scene black with dissolve
    centered "{size=+20}{b}DÍA 27 – DOMINGO{/b}{/size}"
    if kim._var("route"):
        "Te despiertas antes de lo habitual y bajas a desayunar. [kim] ha desaparecido."
    else:
        "Te despiertas antes de lo habitual y bajas a desayunar."
    "Te estás muriendo de hambre. No cenaste en el barco y no tenías hambre al llegar a casa."
    scene c25s003_005a with dissolve
    play music ("music/SneakySnitch.ogg")
    "Al pasar por la planta de las estudiantes, ves a [deb.nick] con su portátil."
    mc "Buenos días, [deb.nick]. ¿Esperando a las chicas para hacer yoga? ¿O vas a salir a correr?"
    deb "Buenos días, [mc]. Iba a hacer yoga, pero me he entretenido con un juego. Lo dejaré para otro día."
    if deb._var("laptop"):
        mc "¿Alguna novela visual nueva?"
        call BlinkXPS3 ("c25s003_010" , "d") from _call_BlinkXPS3_2217
        deb "No, no he tenido tiempo de mirar ninguna más aparte de My Residence. Un día me tienes que recomendar alguna que no haya jugado."
        mc "He jugado a varias muy buenas. Princess on the Fly, Origin Tale, The Awesome Game, Puddles of Astrum, Basking All-Out, The Diner... y óbviamente My Residence." #mc "I played several really good ones. Princess on the Fly, Origin Tale, The Awesome Game, Puddles of Astrum, Basking All-Out, The Diner... and obviously My Residence."
    else:
        call BlinkXPS3 ("c25s003_015" , "d") from _call_BlinkXPS3_2218
        deb "Es una novela visual que estoy jugando..."
        mc "¿Una novela visual japonesa u occidental?"
        call BlinkXPS3 ("c25s003_020" , "d") from _call_BlinkXPS3_2219
        deb "Occidental, para adultos..."
        mc "¡[deb.nick]! ¡Me sorprendes!"
        call BlinkXPS3 ("c25s003_025" , "d") from _call_BlinkXPS3_2220
        deb "¿Qué pasa? ¡No hay nada de lo que avergonzarse!"
        mc "*Risa* Estoy de acuerdo. Yo también juego a novelas visuales."
        call BlinkXPS3 ("c25s003_030" , "d") from _call_BlinkXPS3_2221
        deb "¿De verdad? ¿A cuáles juegas?"
        mc "He jugado a varias. Princess on the Fly, Origin Tale, The Awesome Game, Puddles of Astrum, Basking All-Out, The Diner, My Residence..."
        call BlinkXPS3 ("c25s003_035" , "d") from _call_BlinkXPS3_2222
        deb "¿My Residence? Es precisamente la que estoy jugando ahora."
    call BlinkXPS3 ("c25s003_040" , "d") from _call_BlinkXPS3_2223
    deb "¿Te enteraste de que algún hijo de puta filtró la última actualización de My Residence?"
    mc "Sí. ¿Ha hecho Clichecita algún otro post mandando a tomar por culo al filtrador? No me importa si me haces algún spoiler."
    mc "Me gustó que casi toda la comunidad le apoyásemos. Tanto los que somos suscriptores como los que no lo son. Menos el hijo de puta, claro."
    call BlinkXPS3 ("c25s003_045" , "d") from _call_BlinkXPS3_2224
    deb "¡Ha hecho algo mucho mejor! *Risa* Ha mandado a Vee y a Mandy, las espías, en una misión para acabar con filtradores de juegos y moderadores fascistas de foros."
    mc "*Risa* Ese tío se va a meter en problemas algún día, lo van a banear de todos los foros. Pero es gracioso que haga cosas así. ¿Tienes alguna imagen?"
    scene c25s003_005b with dissolve
    deb "Sí, déjame mirar en la galería un momento."
    scene c25s003_005c with dissolve
    deb "Mira, aquí es cuando ya han acabado con él."
    mc "*Risa* ¡Qué graciosa es Mandy diciendo 'Un criminal menos en el mundo.' después de matar al filtrador!"
    mc "Y Vee diciendo 'Ahora, a por los moderadores fascistas'. Dan miedo."
    deb "*Risa* A mí me han hecho reír las pantallas y el cartel: 'El sótano de mi madre es mi castillo' y '¿Por qué no puedo encontrar mi culo con dos manos y una linterna'"
    mc "*Risa* Libro 1. Supongo que los filtradores necesitan instrucciones para eso."
    mc "*Risa* ¡Espera! ¿Eso es un consolador?"
    call BlinkXPS3 ("c25s003_050" , "d") from _call_BlinkXPS3_2225
    deb "Sí, y el papel higiénico al lado. Supongo que ha tirado de... clichés sobre perdedores. O tropes. *Risa*"
    mc "Lo que me gusta es que ninguna de las dos parece contenta. Como diciendo 'Es algo que había que hacer, no por ello nos gusta.'"
    call BlinkXPS3 ("c25s003_055" , "d") from _call_BlinkXPS3_2226
    deb "Exactamente eso. Te va a parecer gracioso, pero Vee y Mandy me recuerdan en cierta forma a [eva] y [ama]."
    mc "¡Qué va! [ama] y [eva] son mucho más tiernas. Vee y Mandy son mucho más despiadadas."
    mc "¿Has desayunado ya?"
    call BlinkXPS3 ("c25s003_060" , "d") from _call_BlinkXPS3_2227
    deb "Sí, hace un rato. No quería hacer yoga con el estómago vacío, y al final me he quedado jugando."
    mc "Pues te dejo jugando y voy a desayunar."
    if deb._var("route"):
        scene c25s003_005d with dissolve
        "Das un beso a la hermosa sirena, intentando no tirar el portátil."
        call BlinkXPS3 ("c25s003_060" , "d") from _call_BlinkXPS3_2228
    mc "Te veo luego. Me muero de hambre."
    stop music fadeout (1.5)
    deb "Hasta luego, [mc]."
    return
label c25s003_Yoga:
    if _in_replay:
        $ jef = TGCharacter ("Jeff Sound", color = "#ffffff")
        call mrS3_kim_route from _call_mrS3_kim_route
        if not kim._var("route"):
            call mrS3_kim_saved from _call_mrS3_kim_saved
            if kim._var("saved"):
                call mrS3_kim_rps (4, 10, 15) from _call_mrS3_kim_rps_2
            else:
                $ kim.rp (-5)
        call mrS3_kia_route from _call_mrS3_kia_route_6
        if kia._var("route"):
            call mrS3_mar_route from _call_mrS3_mar_route_9
            if mar._var("route"):
                call mrS3_sam_route from _call_mrS3_sam_route_4
                if sam._var("route"):
                    call mrS3_nor_route from _call_mrS3_nor_route_4
    scene c23s002_005a with fade
    "Al entrar en la cocina te invade el olor de croissants recién hechos."
    play music ("music/RayOfHope.ogg")
    "No puedes resistirte y, después de preparar un café, comes un par."
    scene c25s003_065a with dissolve
    "Mientras te tomas el café, te asomas a la ventana."
    "Recuerdas que [kia] dijo que un montón de chicas se apuntarían a la sesión de yoga de hoy."
    "A este paso vais a tener que ampliar la piscina."
    "Decides bajar a saludar y acabarte el café en la piscina. Estando todas juntas, va a ser más eficiente."
    scene c25s003_065d with fade
    mc "Buenos días, chicas. Hace un día genial para veros hacer yoga sin unirme. *Risa*"
    mcp "(No tengo intención de volver a ponerme las mallas de Tío Mike en mi vida.)"
    scene c25s003_065e with dissolve
    "Sin interrumpir sus ejercicios ni decir nada, todas te dedican una sonrisa."
    "Una preciosa imagen para empezar el día. Como has pensado, mucho más eficiente."
    kat "Me estás tapando las vistas, [mc]."
    call BlinkXPS3 ("c25s003_070" , "d") from _call_BlinkXPS3_2229
    mc "¡Oh, [kat]! Perdona, no te había visto."
    kat "*Risa* Lo difícil es no verme con lo que abulto, pero te entiendo. Es difícil apartar los ojos de esas trece mujeres."
    mc "*Risa* No las había contado."
    call BlinkXPS3 ("c25s003_075" , "d") from _call_BlinkXPS3_2230
    kat "*Risa* Bueno, aparte de mirar, no he tenido mucho que hacer en los últimos 10 minutos."
    kat "Y si no sales de en medio, no voy a poder seguir mirando."
    scene c25s003_075d with dissolve
    kat "{i}(¡Deja de mirar, [kat]! ¡Céntrate! Ni te va a mirar con el espectáculo que hay detrás suyo.){/i}"
    scene c25s003_075e with dissolve
    mc "¿Estoy bien aquí? ¿No te tapo las vistas ahora?"
    kat "Sí, ahí estás bien."
    kat "Además, justo a tiempo para el cambio de postura."
    scene c25s003_065b with dissolve
    mc "Casi parece que estén haciendo una coreografía, ¿no?"
    kat "Todas siguen lo que hace [nor]. Y quien no puede, sigue a [sai], que también conoce todos los movimientos."
    mc "*Risa* Veo que lo tienes todo estudiado."
    call BlinkXPS3 ("c25s003_080" , "d") from _call_BlinkXPS3_2231
    kat "*Risa* Bajar a desayunar aquí es una de las mejores vistas de la casa."
    mc "*Risa* No voy a decir lo contrario. ¿Bajas muy a menudo?"
    kat "No bajo todos los días. Cuando tengo clase a primera hora es complicado."
    mc "Entiendo. ¿Tienes algún plan para hoy?"
    call BlinkXPS3 ("c25s003_085" , "d") from _call_BlinkXPS3_2232
    kat "*Risa* NO ir a correr al lago es el primer plan. Hoy es mi día de descanso sin ejercicio."
    kat "El segundo era bajar aquí a ver a las chicas haciendo yoga. [eil], [oma], y [kia] no se apuntan nunca, y [sam] solo es la segunda vez que viene."
    kat "No podía perdérmelo."
    mc "¿Y más allá de ver chicas en leggins?"
    call BlinkXPS3 ("c25s003_090" , "d") from _call_BlinkXPS3_2233
    kat "*Risa* Más allá no he pensado nada."
    kat "Supongo que estudiar un rato, leer, y hacer el vago hasta la hora de comer."
    mc "*Risa* Es un plan perfecto para un domingo."
    scene c25s003_065c with dissolve
    kat "¡Oh, por el amor de Dios! Adoro esa postura. No sería capaz de hacerla aunque me pagaran por ello."
    mc "*Risa* Yo tampoco. ¿Entiendes ahora por qué no me apunto a las sesiones de yoga?"
    call BlinkXPS3 ("c25s003_095" , "d") from _call_BlinkXPS3_2234
    kat "Visto que compartimos gustos por las vistas... ¿por qué no quedamos para desayunar juntos alguna mañana?"
    call BlinkXPS3 ("c25s003_100a" , "h") from _call_BlinkXPS3_2235
    kat "{i}(¡Mierda, [kat]! ¡Eso ha sonado como si le pidieras una cita! ¿Dónde has dejado tu cerebro hoy?){/i}"
    mc "No te puedo asegurar nada, pero me parece una idea genial."
    call BlinkXPS3 ("c25s003_100b" , "h") from _call_BlinkXPS3_2236
    kat "{i}(¿Ha dicho que sí? ¿No podría haberse negado y así dejarme las cosas claras?){/i}"
    mcp "(¿De qué se sorprende? ¿No quiere que desayunemos juntos? ¿Por qué lo ha propuesto?)"
    play sound ("music/notification.ogg")
    "Suena tu móvil. Es el correo de [ama] con la información que le pediste anoche."
    mc "Dame un momento, tengo que leer un correo."
    scene c25s003_110a with dissolve
    kat "{i}(¡Joder, [mc]! ¿Lo puedes poner más difícil?){/i}"
    call BlinkXPS3 ("c25s003_105" , "d") from _call_BlinkXPS3_2237
    mc "[kat], te tengo que dejar. Tengo que hacer una llamada."
    kat "No te preocupes, aunque te vas a perder las últimas posturas."
    mc "*Risa* Las veré el día que desayunemos juntos. Cuento contigo como comentarista."
    stop music fadeout (1.5)
    mc "¿Puedes dejar mi taza en tu bandeja, por favor?"
    scene c25s003_110b with dissolve
    play music ("music/WarIsComing.ogg")
    "Te mueves a la puerta del garaje para llamar a Sound. Intentas mantener un tono amigable."
    mc "Buenos días, Jeff. Soy [mc] Marks. Espero no molestarte tan temprano."
    jef "Buenos días, Sr. Marks. No se preocupe. ¿En qué puedo ayudarle?"
    scene c25s003_110c with dissolve
    mc "Te llamaba por lo que pasó ayer en el barco. Con la chica..."
    jef "¿De qué quería hablar sobre ese tema?"
    mc "No sé lo que Ichigo tiene planeado con ella, pero no la vais a volver a contratar."
    jef "Perdone, Sr. Marks, pero no está en posición de decir quién puede o no puede contratar Iron Fist."
    scene c25s003_110d with dissolve
    "El tono amigable desaparece de tu voz."
    mc "Tiene razón. No puedo decirles a quién tienen que contratar."
    mc "Pero puedo revisar todos los contratos que nuestra división de Apoyo tiene con Iron Fist. Mis antecesores pusieron una cláusula que nos eximía en caso de fuerza mayor."
    jef "No puede hacer eso. La reputación de NTR..."
    scene c25s003_110e with dissolve
    mc "La reputación de NTR quedará intacta. Estaremos cumpliendo el contrato. Los contratos."
    mc "El martes hay un despliegue de operativos de Iron Fist en Venezuela usando un avión de NTR como transporte. Es posible que ese avión tenga algún problema con los motores."
    mc "Tres días después, extracción de esos operativos en la costa. Mmmm... creo que el barco que íbamos a enviar tiene un problema y hace aguas."
    mc "¿Sigo? Hay once contratos para los próximos tres meses."
    jef "No, Sr. Marks. No hace falta que continúe."
    scene c25s003_110f with dissolve
    mc "Ustedes nos necesitan a nosotros. Nosotros no les necesitamos a ustedes."
    mc "Ya sabe. No volverán a contratar a la Srta. Brown, ni harán ningún informe negativo sobre ninguno de sus dos contratos con ustedes."
    jef "Lo entiendo. Se lo comunicaré al Sr. Ichigo. Se pondrá en contacto con usted."
    scene c25s003_110g with dissolve
    mc "No hace falta que Ichigo pierda su tiempo llamándome. Que envíe un 'OK' junto a la oferta que me tiene que enviar para la absorción o fusión."
    mc "El mismo tipo de suspensión de contratos se aplicará si alguien de Iron Fist se acerca a alguien de mi familia, o si ponen alguna queja ante la agencia de la Srta. Brown."
    mc "¿Entendido?"
    jef "Entendido, Sr. Marks."
    mc "Que tenga un buen día, Sr. Sound."
    scene c25s003_110h with dissolve
    mcp "(Sound parece un buen tipo, pero tiene que defender su empresa. Supongo que es difícil trabajar para alguien como Ichigo.)"
    "Cuando estás a punto de girarte volver con [kat]..."
    stop music fadeout (1.5)
    kim "*Jadeo de sorpresa*"
    play music ("music/Vacation-Vibe.ogg")
    scene c25s003_110i with hpunch
    kim "¿Qué has hecho, [mc]?"
    mc "¿Cuánto llevas ahí, [kim]?"
    kim "Desde que has dicho algo de Venezuela..."
    call BlinkXPS3 ("c25s003_115" , "d") from _call_BlinkXPS3_2238
    kim "Y después has dicho lo de mi contrato y los informes a la agencia..."
    mc "No puedo dejar que seas una víctima en una guerra que no va contigo, [kim]. No sería justo."
    if kim.rps < 5:
        $ kim.rp (+5-kim.rps)
        $ notificacion = __("Relación con [kim] normalizada")
        $ renpy.notify (notificacion)
    if kim._var("route"):
        scene c25s003_120a with hpunch
        "Miss Mapache California 2023 se lanza a darte un beso en el que hay tanto agradecimiento como pasión."
    else:
        scene c25s003_120b with hpunch
        "[kim] se lanza a darte un abrazo en el que hay tanto agradecimiento como alivio."
    call BlinkXPS3 ("c25s003_125" , "d") from _call_BlinkXPS3_2239
    kim "Gracias, [mc]. No sé cómo darte las gracias por algo así..."
    mc "No hace falta darlas pero, de todas formas, lo acabas de hacer."
    if kim._var("route"):
        mc "Y no estoy para nada de acuerdo con que tengas los labios feos."
        call BlinkXPS3 ("c25s003_130" , "d") from _call_BlinkXPS3_2240
        kim "*Risa* Gracias. Pero no te acostumbres. Me encanta mi pintalabios."
    else:
        call BlinkXPS3 ("c25s003_130" , "d") from _call_BlinkXPS3_2241
    kim "¡Me voy a dar una ducha o, si no, se me van a adelantar!"
    if kim._var("route"):
        kim "Y no estás invitado, antes de que preguntes."
        mc "*Risa* Parece que las invitaciones no son necesarias entre nosotros, ¿no?"
        mc "Anoche me desperté con una preciosidad entre mis brazos."
        call BlinkXPS3 ("c25s003_135" , "d") from _call_BlinkXPS3_2242
        kim "¿Te molestó? Cada vez que cerraba los ojos... veía al Sr. Ichigo ordenándome que me desnudara..."
        kim "Pensé que dormir contigo me calmaría, y así fue."
        mc "No me ha molestado, [kim]. Pero despiértame la próxima vez. Al menos para darme un beso de buenas noches."
        scene c25s003_120a with dissolve
        "La hermosa modelo te da un beso de buenos días. La compensación no es algo por lo que vayas a quejarte."
        call BlinkXPS3 ("c25s003_130" , "d") from _call_BlinkXPS3_2243
        kim "Lo tendré en cuenta para la próxima vez. Voy a darme esa ducha."
    mc "Te veo luego, [kim]."
    scene c25s003_140a with dissolve
    "Te asomas para despedirte de [kat] y las chicas del yoga."
    if kia._var("route") and mar._var("route") and nor._var("route") and sam._var("route"):
        scene c25s003_140b with dissolve
        "La reacción al verte de [kia] especialmente, y de [mar], [nor], y [sam] es sospechosa."
        "Quizás solo creían que ya te habías ido y se han sorprendido al verte de nuevo."
        "O eso hubieras pensado hace tan solo unas semanas."
    else:
        "Están demasiado ocupadas para notar que has vuelto."
    call BlinkXPS3 ("c25s003_145" , "d") from _call_BlinkXPS3_2244
    mc "Te veo luego, [kat]."
    kat "Hasta luego, [mc]. Recuerda que tenemos una... {i}(¡No digas cita, no digas cita!){/i}... cita para desayunar."
    mc "No te preocupes, no la olvidaré."
    kat "{i}(¡Mierda, [kat]! ¡Lo has dicho!){/i}"
    scene black with dissolve
    "Subes a la habitación, contento por cómo ha ido la conversación con Sound."
    if not kim._var("saved"):
        "Estás contento de que la relación con [kim] se haya arreglado. Anoche estaba muy enfadada contigo."
    if kia._var("route") and mar._var("route") and nor._var("route") and sam._var("route"):
        "También estás confuso con la reacción de [mar], [nor], [sam], y [kia]. Ha sido solo un momento, pero era como si estuvieran planeando algo en lo que estabas involucrado."
    "Y has quedado para desayunar con [kat]..."
    scene black with hpunch
    stop music fadeout (1.5)
    mcp "(¡Un momento! ¿Ha dicho cita? No puede ser, ¿no?)"
    return
label c25s003_NoMeg:
    scene c25s003_150e with fade
    play music ("music/LifeOfAWanderingWizard.ogg")
    "Al llegar a tu habitación empiezas a jugar a My Residence. La conversación con [deb.nick] te ha hecho recordar que llevas varias actualizaciones de retraso."
    "Tienes una tórrida escena con Kimberly, la bailarina, que está en la habitación del MC cuando vuelve de desayunar."
    "[deb.nick] tenía parte de razón. Si Mandy y Vee tienen algo de [ama] y [eva], Kimberly tiene algo que te recuerda a [meg]."
    "Sin el comentario de [deb.nick] no crees que hubieras descubierto el parecido nunca."
    stop music fadeout (1.5)
    return
label c25s003_Meg:
    if _in_replay:
        $ mc._var("relationships", 1, "set")
        call mrS3_eil_route from _call_mrS3_eil_route_4
        call mrS3_kia_route from _call_mrS3_kia_route_7
        call mrS3_eva_route from _call_mrS3_eva_route_8
        if mc._var("relationships")==1:
            call mrS3_rels from _call_mrS3_rels_13
        call mrS3_meg_pregnant from _call_mrS3_meg_pregnant_1
    scene c25s003_150d with dissolve
    play music ("music/Gypsy-Jazz.ogg")
    "Al llegar a tu habitación, te encuentras una sorpresa en el sofá."
    mc "¡Hola, [meg]! ¿Puedo ayudarte en algo?"
    scene c25s003_150f with dissolve
    meg "Un momento que acabo la página, por favor."
    "Esperas."
    mc "¿Qué estás leyendo?"
    call BlinkXPS3 ("c25s003_150" , "d") from _call_BlinkXPS3_2297
    meg "Un libro sobre unos compositores que me gustan mucho."
    mc "Lo que a mí me gusta mucho es el conjunto que llevas."
    scene c25s003_155d with fade:
        yalign 1.0
        linear 5.0 yalign 0.0
    pause (5.0)
    call BlinkXPS3 ("c25s003_155" , "d") from _call_BlinkXPS3_2298
    call addProfileImageS3 (7, "megan_7", meg, _(": 15 - Especial"), "") from _call_addProfileImageS3_13
    meg "¿Esto? Es algo que he pensado que te podría gustar..."
    mc "Y has acertado completamente."
    mc "Pero... ¿quién eres y qué has hecho con [meg]?"
    call BlinkXPS3 ("c25s003_160" , "d") from _call_BlinkXPS3_2299
    meg "¿A qué te refieres?"
    mc "Mi [meg] nunca diría algo así. Estaría quejándose de que el modelo es precioso pero de que no le queda igual que le quedaría a [ama], o a [nor]."
    mc "¡Alien, sal del cuerpo de [meg]! *Risa* ¡Has poseído su cuerpo, pero no sabes cómo piensa!"
    call BlinkXPS3 ("c25s003_165" , "d") from _call_BlinkXPS3_2300
    meg "*Risa* A lo mejor tu [meg] ha descubierto que no necesita los abdominales de [ama] o las tetas de [nor] para gustarte."
    meg "A lo mejor, gracias a todo lo que le has dicho, se ha vuelto un poco más segura de sí misma."
    mc "*Risa* ¡Mierda! Ahora no sé si realmente eres tú. Los aliens pueden ser muy astutos... y un alien poseyendo el cuerpo de [meg] seguramente diría eso."
    call BlinkXPS3 ("c25s003_170" , "d") from _call_BlinkXPS3_2301
    meg "*Risa* ¿Crees que un alien sabría cómo besa tu [meg]?"
    mc "*Risa* No lo creo, si no han sido capaces de acceder a sus recuerdos."
    call BlinkXPS3 ("c25s003_175" , "d") from _call_BlinkXPS3_2302
    meg "Entonces, déjame demostrarte que soy yo. Aunque para poseer mi cuerpo se necesitaría una civilización completa de aliens. Hay mucho cuerpo que poseer."
    mc "Estoy esperando a las pruebas."
    scene c25s003_175d with dissolve
    "La bella cantante demuestra con sus labios que no hay ningún ente extraterrestre poseyéndola."
    "Reconocerías esos labios y esa forma de besar entre un millón de mujeres aunque tuvieras los ojos vendados."
    call BlinkXPS3 ("c25s003_180" , "d") from _call_BlinkXPS3_2303
    meg "¿Ya estás convencido de que soy yo? *Risa*"
    mc "Totalmente convencido."
    mc "¿Querías algo? Aparte de ese beso, claro."
    call BlinkXPS3 ("c25s003_185" , "d") from _call_BlinkXPS3_2304
    meg "Quería pasar un rato contigo. Ya que voy a pasar los fines de semana aquí y que tú nunca vienes a Westport..."
    mc "Ha sido una semana complicada con el viaje a Monterey, [meg]. A ver si la semana que viene tengo más tiempo libre."
    call BlinkXPS3 ("c25s003_190" , "d") from _call_BlinkXPS3_2305
    meg "No te preocupes, lo decía en broma. Pero un día podrías venir y verme cantar allí. Es un estilo diferente al del Jazz Corner."
    mc "Te prometo que iré si puedo. A ver si la semana que viene..."
    call BlinkXPS3 ("c25s003_195" , "d") from _call_BlinkXPS3_2306
    meg "Mi cama te echa de menos. Te podrías quedar a dormir el día que vengas."
    mc "La mía también a ti."
    meg "Pero la última vez que estuvimos juntos fue en la tuya..."
    mc "Y la siguiente también. *Risa*"
    call BlinkXPS3 ("c25s003_200" , "d") from _call_BlinkXPS3_2307
    meg "¿Sí? ¿Y cuándo va a ser esa siguiente vez?"
    meg "Había subido a ver si mientras las chicas estaban con el yoga..."
    mc "Me da lo mismo que hayan acabado. Sabes que no tenemos que rendir cuentas a nadie, ¿verdad?"
    call BlinkXPS3 ("c25s003_205" , "d") from _call_BlinkXPS3_2308
    meg "Se me hace raro acostarme contigo con tanta gente en casa..."
    mc "Te tendrás que ir acostumbrando. Creo que la casa nunca va a estar vacía a este paso."
    call BlinkXPS3 ("c25s003_210" , "d") from _call_BlinkXPS3_2309
    meg "Por eso te decía que vinieras a mi apartamento."
    mc "¿Quieres que esperemos a que vaya un día de la semana que viene?"
    call BlinkXPS3 ("c25s003_215" , "d") from _call_BlinkXPS3_2310
    meg "*Risa* No."
    mc "*Risa* Es lo que me parecía."
    mc "¿Cómo se quita eso que llevas puesto? ¿Te puedes dejar las medias puestas?"
    call BlinkXPS3 ("c25s003_220" , "d") from _call_BlinkXPS3_2311
    meg "*Risa* No lo vas a quitar tú y no, no me puedo dejar las medias puestas a menos que no quieras acceso a lo que cubren."
    mc "¡Oh! ¿Son de esas que lo cubren todo?"
    meg "Sí, llevan la braga incluida. *Risa* Y no te voy a permitir romperlas."
    mc "*Risa* Quedaría demasiado porno, ¿no?"
    call BlinkXPS3 ("c25s003_225" , "d") from _call_BlinkXPS3_2312
    meg "¡Los tíos sois la hostia! ¿Realmente creéis que si a una chica le rompéis la lencería que se ha comprado para vosotros va a tener ganas de sexo?"
    mc "*Risa* Creo que ningún tío se lo ha planteado nunca así."
    call BlinkXPS3 ("c25s003_230" , "d") from _call_BlinkXPS3_2313
    if mc._var("relationships")>1:
        meg "*Risa* Pues ya es hora de que te lo plantees antes de que rompas la lencería de alguna de las otras chicas."
        meg "Algunas mujeres pueden ser tan inocentes como para no advertirte antes."
    else:
        meg "*Risa* Pues ya es hora de que te lo plantees. Lencería rota significa noche, o mañana en este caso, sin sexo."
    mc "*Risa* Tomo nota. ¿Al menos puedo mirar cómo te la quitas?"
    scene c25s003_235d with dissolve
    meg "*Risa* Sólo si lo haces a una distancia prudencial."
    mc "Me quedaré en el rincón para no perderme el espectáculo."
    scene c25s003_235e with dissolve
    meg "No esperes mucho, sólo hay dos piezas que quitar."
    mc "Bueno, retirar la primera ya ha sido espectacular. Ahora veo lo de las bragas integradas."
    call BlinkXPS3 ("c25s003_235" , "d") from _call_BlinkXPS3_2314
    meg "Pues ahora ya está. Es tu turno."
    mc "Preciosa y encantadora como siempre."
    call BlinkXPS3 ("c25s003_240a" , "d") from _call_BlinkXPS3_2315
    meg "Puedes empezar a desnudarte. Me voy a quedar aquí mirando tal cómo has hecho tú."
    mc "Pero..."
    call BlinkXPS3 ("c25s003_240b" , "d") from _call_BlinkXPS3_2316
    meg "¿Dónde está el problema? ¿Sólo tú tienes derecho a mirar cómo se desnuda una mujer? Yo también quiero hacerlo."
    mc "*Risa* Puedo avisar a alguna mujer para que se desnude para ti."
    call BlinkXPS3 ("c25s003_245" , "d") from _call_BlinkXPS3_2317
    meg "*Risa* Que me hagas reír no significa que no vayas a desnudarte para mí."
    mc "Tenía que intentarlo..."
    mc "Voy a empezar."
    call BlinkXPS3 ("c25s003_250" , "d") from _call_BlinkXPS3_2318
    mc "Las zapatillas..."
    meg "Bien hecho. Empiezas por lo menos sexy. Sigue."
    call BlinkXPS3 ("c25s003_255" , "d") from _call_BlinkXPS3_2319
    mc "La camiseta..."
    meg "Ahora es casi como si llevaras un bañador. Todavía no es lo suficientemente sexy. Sigue."
    mc "*Risa* Eres muy exigente."
    meg "Sigue."
    call BlinkXPS3 ("c25s003_260" , "d") from _call_BlinkXPS3_2320
    mc "Los shorts..."
    meg "Eso es mucho más interesante. Y lo que parece interesante es el bulto que se marca en los calzoncillos."
    mc "*Risa* Me siento un hombre sexualizado."
    call BlinkXPS3 ("c25s003_265" , "d") from _call_BlinkXPS3_2321
    meg "Cariño, ERES un hombre sexualizado ahora mismo. *Risa*"
    mc "*Risa* Ah, okay. Sólo quería despejar la duda."
    meg "Continúa. La última prenda."
    call BlinkXPS3 ("c25s003_270" , "d") from _call_BlinkXPS3_2322
    mc "Los calzoncillos..."
    meg "Y veo que Mjolnir está medio preparado ya."
    mc "*Risa* Cuando has acabado de desnudarte estaba preparado del todo. No estoy acostumbrado a que me miren mientras me desnudo."
    call BlinkXPS3 ("c25s003_275" , "d") from _call_BlinkXPS3_2323
    meg "*Risa* ¿Mi hombre se ha despertado vergonzoso?"
    mc "*Risa* No es vergüenza. Es... falta de costumbre."
    call BlinkXPS3 ("c25s003_280" , "d") from _call_BlinkXPS3_2324
    meg "Pues siéntate en el sofá. Te mereces un premio por el striptease, aunque tenemos que trabajarlo un poco aún."
    mc "Tú también te mereces un premio... ¿no lo quieres?"
    stop music fadeout (1.5)
    meg "Luego, cuando Mjolnir esté en todo su esplendor."
    call BlinkXPS3 ("c25s003_285" , "f") from _call_BlinkXPS3_2325
    play music ("music/SensualJazzMedium2.ogg")
    "Te sientas en el sofá tal como el hermoso ruiseñor te ha indicado. Ella se arrodilla a tus pies."
    meg "Creo que nunca lo he visto tan flácido antes de empezar."
    mc "*Risa* Los nervios de mi primer striptease..."
    scene c25s003_965pv with dissolve
    show c25s003_965v
    "[meg] empieza a mover su mano a un ritmo maravilloso."
    meg "Ahora sabes lo que sentimos las chicas cuando nos toca hacerlo por primera vez como hoy. Siempre dudando de si habrá algo de nuestro cuerpo que no os gusta."
    "No lo habías pensado, pero es la primera vez que [meg] hace algo así contigo. Sabes que ahora se siente más segura que hace unas semanas, pero..."
    meg "Y que conste que no lo he hecho por venganza. Tenía ganas de que te desnudaras para mí."
    "Pese a que ahora entiendes cómo se puede sentir una chica haciéndolo, no te importaría repetir el striptease."
    scene c25s003_955pv with dissolve
    hide c25s003_965v
    show c25s003_955v
    "Puedes notar como Mjolnir va incrementando su dureza con cada paso de su mano por tu glande."
    meg "Me encanta tenerte en mi mano, notando como te vas poniendo cada vez más duro."
    "Es imposible que ella no lo note también. Tiene unas manos pequeñas y suaves que te paso a paso te van poniendo más cachondo."
    meg "¡Me está empezando a costar incluso cerrar la mano alrededor!"
    "No es necesario que lo haga. La sensación es igual de increíble, especialmente cuando se centra en la punta de tu polla."
    scene c25s003_960pv with dissolve
    hide c25s003_955v
    show c25s003_960v
    "Con lo silenciosa que es siempre mientras folláis, te sorprende lo parlanchina que es mientras te pajea."
    meg "Lo de metérmela entera en la boca... un día me gustaría lograrlo, pero no puedo desencajar la mandíbula como una serpiente. *Risita*"
    "Cuando lo ha intentado, sólo ha conseguido meterse la punta. [meg] tiene una boca maravillosa, pero no es muy grande."
    if eil._var("route"):
        meg "Le tengo que preguntar a [eil] cómo lo hace."
    else:
        meg "Le tengo que preguntar a [eil] cómo lo hacía."
    if kia._var("route") and eva._var("route"):
        mcp "([eil] les dio consejos a [kia] y a [eva]. ¿Se está convirtiendo en la chica a la que le preguntan cosas sobre mí?)"
    elif kia._var("route"):
        mcp "([eil] le dio consejos a [kia]. ¿Se está convirtiendo en la chica a la que le preguntan cosas sobre mí?)"
    elif eva._var("route"):
        mcp "([eil] le dio consejos a [eva]. ¿Se está convirtiendo en la chica a la que le preguntan cosas sobre mí?)"
    else:
        mcp "([eil] dando consejos sobre mí... ¿O es que [meg] tiene confianza con ella para preguntarle?)"
    mcp "(Si comparte habitación con [sai], ¿por qué no hacerlo con ella?)"
    "Tienes que descubrirlo. Pero ahora no es el momento. Es el momento de seguir disfrutando de las manos de la mujer de ojos verdes."
    call BlinkXPS3 ("c25s003_290" , "d") from _call_BlinkXPS3_2326
    hide c25s003_960v
    meg "Parece que ya está casi listo..."
    mc "¿Casi? *Risa* Dudo que pueda estar más duro."
    meg "Entonces es el momento del siguiente paso."
    scene c25s003_970pv with dissolve
    show c25s003_970v
    "[meg] lo intenta pero, como siempre, sólo consigue introducirse tu capullo en la boca."
    meg "¿*Slurp*?"
    "Compensa la falta de profundidad con un juego de lengua maravilloso que recorre todos los rincones de tu anatomía."
    mc "Alucinante, [meg]."
    "Es como si escribiera una sensual canción con su lengua y tu capullo fuera la partitura."
    call BlinkXPS3 ("c25s003_295" , "d") from _call_BlinkXPS3_2327
    hide c25s003_970v
    meg "Ahora sí que estás listo. Recuéstate en el sofá."
    mc "Como desees, mi precioso ruiseñor."
    scene c25s003_300a with fade
    "Una vez sentado tal como te indica [meg]..."
    scene c25s003_300b with vpunch
    meg "*Jadeo* ¡Ooof!"
    "La preciosa mujer se deja caer a lo largo de tu astil para convertirse en una preciosa brocheta."
    "Una brocheta donde Mjolnir se siente rodeado de humedad y fuertemente estrujado."
    scene c25s003_910pv with dissolve
    "Posiblemente la brocheta con las mejores vistas de la historia."
    meg "*Respiración entrecortada*"
    "Estás a punto de reírte. Hace un momento estabas pensando en que estaba más habladora de lo habitual."
    mc "¿Estás bien?"
    meg "*Jadeo afirmativo*"
    show c25s003_910v
    "[meg] no te da tiempo de pensar en nada más antes de empezar a moverse. En vez de pensar, disfrutas de las vistas."
    meg "*Gemido*"
    mcp "(¡Esta es mi [meg]! Ahora ya no hay duda de que ningún alien la ha poseído.)"
    "Contienes la risa a duras penas."
    meg "*Jadeo inquisitivo*"
    mc "Nada, no te preocupes..."
    scene c25s003_900pv with dissolve
    hide c25s003_910v
    show c25s003_900v
    "Dejas de pensar en tonterías y te centras en disfrutar de las sensaciones que las subidas y bajadas de la bella mujer producen en tu polla."
    meg "*Gemido*"
    "Te sientes afortunado de poder tener una mujer como [meg] contigo en estos momentos."
    meg "*Jadeo*"
    "Tan afortunado como se siente Mjolnir, siendo estrujado en cada uno de los viajes que da [meg] a lo largo de tu astil."
    scene c25s003_905pv with dissolve
    hide c25s003_900v
    show c25s003_905v
    "Es alucinante como, teniendo las piernas tan abiertas, el coño de [meg] no pierde ni un ápice de su estrechez."
    meg "*Gemido*"
    "Puedes notar cada uno de sus pliegues, bañados en sus cada vez más abundantes fluidos, con la punta de tu polla."
    meg "*JADEO*"
    "Ella también puede notar como impactas en cada uno de los puntos correctos, adaptando sus movimientos en cada recorrido."
    scene c25s003_915pv with dissolve
    hide c25s003_905v
    show c25s003_915v
    "Pese a lo que te gustan las vistas de su culo, te encantaría ver también cómo sus tetas botan en cada una de sus embestidas."
    meg "*JADEO*"
    "Tienes que recordar abrir el espejo la próxima vez que folléis en el sofá... o en la cama."
    meg "*JADEO*"
    "Difícilmente te vas a cansar nunca de mirar a [meg]."
    scene c25s003_305d with dissolve
    "[meg] para sus movimientos inesperadamente, quedándose completamente inmóvil."
    meg "*JADEO*"
    mc "¿Pasa algo, [meg]?"
    call BlinkXPS3 ("c25s003_305" , "d") from _call_BlinkXPS3_2328
    "Se gira sin dejarte salir de su interior."
    meg "Hace un minuto que tengo un calambre en una de las piernas... ¿puedo descansar un momento y cambiar de posición?"
    mc "¡Tenías que habérmelo dicho antes!"
    meg "Creía que podía aguantar..."
    mc "Túmbate en la cama. Podemos descansar y dejarlo para otro momento."
    call BlinkXPS3 ("c25s003_310" , "d") from _call_BlinkXPS3_2329
    "Se pone de pie de un salto."
    meg "¡No! Ahora mismo no estoy tan dolorida como cachonda. Y el dolor se me va a pasar en un minuto."
    meg "Ven a la cama."
    mc "*Risa* Como desees."
    call BlinkXPS3 ("c25s003_315" , "f") from _call_BlinkXPS3_2330
    "[meg] cojea hasta la cama y se tumba, mientras tú la rodeas."
    meg "¿Dónde vas?"
    mc "Ahora lo verás."
    scene c25s003_320a with dissolve
    meg "*Risa* ¿Vas a hacerme un baile mientras se me pasa el calambre?"
    mc "Nope. *Risa* Mejor todavía."
    scene c25s003_320b with dissolve
    "Sacas el espejo corredero de dentro del armario para sorpresa de la cantante."
    meg "¡Oh! ¡Eso es muy fetichista!"
    mc "*Risa* No es fetichista. De alguna forma tengo que saber cómo me queda la ropa, ¿no?"
    call BlinkXPS3 ("c25s003_325" , "d") from _call_BlinkXPS3_2331
    meg "*Risa* Por norma mal. La ropa te queda fatal. Estás mucho mejor desnudo. Tengo que hablar con [mar] para comprarte ropa nueva."
    meg "Ahora aparta de ahí. Quiero ver qué perspectiva se tiene desde aquí."
    call BlinkXPS3 ("c25s003_330" , "f") from _call_BlinkXPS3_2332
    "Te mueves detrás de [meg] para observarla a través del espejo."
    meg "Me encanta ese espejo. Lo tenías que haber sacado antes."
    mc "Bueno, tu calambre ha servido para eso. Se me ha ocurrido en el sofá poco antes de que lo dijeras."
    call BlinkXPS3 ("c25s003_335" , "d") from _call_BlinkXPS3_2333
    mc "¿Cómo estás?"
    meg "Bien, ya casi se ha pasado el calambre."
    scene c25s003_335d with dissolve
    mc "*Ñam*"
    scene c25s003_335e with hpunch
    meg "¡[mc]!"
    mc "¿Qué pasa? Sabes que me encanta tu culo."
    scene c25s003_335f with dissolve
    meg "Sí, lo sé. Pero aún no has acabado con lo que has empezado... No tendrás postre hasta que acabes."
    mc "¿Quieres decir que...?"
    call BlinkXPS3 ("c25s003_340" , "d") from _call_BlinkXPS3_2334
    meg "*Risa* Que no vas a morderme el culo si tienes otra cosa que comer."
    mc "Me siento como un halfling y su segundo desayuno. Un delicioso segundo desayuno."
    scene c25s003_980pv with dissolve
    hide c25s003_915v
    show c25s003_980v
    "Hundes tu cara en el segundo desayuno después de que [meg] cambie de posición, todavía húmedo de la sesión interrumpida en el sofá."
    meg "*Gemido*"
    "El terroso olor y el pungente sabor de [meg] invaden tus sentidos como una avalancha. Los gemidos se incrementan cada vez que rozas su clítoris."
    meg "*Jadeo*"
    "Podrías pasarte horas haciendo esto mientras notas el cuerpo de [meg] retorciéndose bajo tus dedos con cada lametón."
    scene c25s003_975pv with dissolve
    hide c25s003_980v
    show c25s003_975v
    "La respiración de la cantante se va agitando poco a poco, tal como va volviéndose a poner cachonda."
    meg "*JADEO*"
    "Mjolnir, que no ha llegado a ponerse completamente flácido, vuelve a estar preparado para penetrar tu desayuno."
    meg "*GEMIDO*"
    "Sigues lamiendo mientras los gemidos de [meg] te indican los puntos perfectos para seguir haciéndolo."
    call BlinkXPS3 ("c25s003_345" , "d") from _call_BlinkXPS3_2335
    meg "*Gemido* Para antes de que me corra..."
    "Una pequeña sensación de decepción te recorre por un momento."
    meg "*Jadeo* Quiero correrme contigo dentro."
    "Desaparece tan rápido como ha llegado."
    scene c25s003_350An with fade
    "Te sitúas a la espalda de [meg], una vez te ha dado espacio para que subas a la cama, y la penetras en un rápido movimiento guiado por tu deseo largamente contenido."
    meg "*JADEO* ¡OOOF!"
    "Mjolnir es recibido con un abrazo húmedo, caliente y confortable."
    scene c25s003_935pv with dissolve
    hide c25s003_975v
    show c25s003_930v
    "No esperas a que te dé luz verde para que empieces a moverte. Conoces el cuerpo de [meg] lo suficientemente bien como para saber que está preparada."
    meg "*GEMIDO*"
    "Su cuerpo vibra en cada una de tus embestidas, diciéndote a su manera que estaba muy cerca del orgasmo cuando te ha pedido que parases."
    meg "*JADEO*"
    "Diciéndotelo sin palabras. Unas palabras que nunca son necesarias con [meg]."
    scene c25s003_925pv with dissolve
    hide c25s003_930v
    show c25s003_925v
    "Odias follar encima del edredón por lo mucho que patina, tus rodillas acaban debajo de [meg], propiciando un extraño ángulo en tu penetración." id c25s003_Meg_cb8a482e
    meg "*GEMIDO* ¡Oh! *JADEO* ¡Me encanta esa postura! *GEMIDO*"
    "Sorprendido por escuchar su voz más allá de sus gemidos, la idea del alien poseyendo el cuerpo de [meg] vuelve a cruzar por tu mente. Casi te ríes."
    meg "*JADEO*"
    "Vuelves a enfocar toda tu atención en el ruiseñor descartando pensamientos peregrinos."
    call OrgasmXS3 ("c25s003_355") from _call_OrgasmXS3_54
    meg "*GEMIDO* ¡SÍ! *JADEO* ¡INCREÍBLE! *GEMIDO*"
    "Tus pensamientos peregrinos han evitado que detectaras que el orgasmo de la mujer de cuerpo generoso estaba a punto de llegar."
    meg "*JADEO* ¡SIGUE! *JADEO*"
    scene c25s003_935pv with dissolve
    hide c25s003_925v
    show c25s003_935v
    "Puedes notar cómo todo su cuerpo vibra bajo tu tacto, con cada uno de tus bombeos."
    meg "*GEMIDO*"
    "Su orgasmo hace que su sensibilidad aumente, viéndose reflejada en su rostro reaccionando a tus embestidas."
    meg "*JADEO*"
    "Ahora es el momento en que te alegras de haber abierto el espejo, para poder disfrutar de esa visión, aunque ello implique verte a ti mismo."
    "Siempre lo has considerado raro, un espejo debería servir para ver a la chica desde ángulos diferentes. Te gustaría ser un vampiro que no se reflejara en los espejos."
    meg "*GEMIDO*"
    "Pero entonces sí que sería raro. Estás a punto de reírte de nuevo ante la idea de ver a [meg] siendo embestida por un [mc] invisible."
    scene c25s003_920pv with dissolve
    hide c25s003_935v
    show c25s003_920v
    "Abandonas tus pensamientos extraños para centrarte en el ritmo de tus embestidas. Tu orgasmo se está acercando, acelerado por las oleadas de orgasmos de [meg]."
    meg "*JADEO*"
    "Empieza a reptar por tus pantorrillas y tus muslos. No vas a aguantar mucho más."
    meg "*GEMIDO*"
    "[meg] tampoco va a poder aguantar mucho más. Nunca se ha caracterizado por su resistencia, pero lo compensa con un maravilloso y voluptuoso cuerpo."
    if persistent.pregnancy and not meg._var("pregnant"):
        if persistent.walkthrough:
            $ wt1 = _("[meg] embarazada.")
            $ wt2 = _("Sin consecuencias.")
        else:
            $ wt1 = ""
            $ wt2 = ""
        menu:
            "Correrte dentro. Ir a por el bebé." (wt = wt1):
                $ meg._var("pregnant", True)
                $ meg._var("undiscoveredPregnancy", True)
                play sound ("music/OldMusicBox5.ogg")
            "Correrte dentro." (wt = wt2):
                pass
    $ resetWalkthrough ()
    call OrgasmXS3 ("c25s003_360") from _call_OrgasmXS3_55
    hide c25s003_920v
    mc "¡Mpfft!"
    "Explotas dentro de la preciosa cantante coincidiendo con su siguiente oleada de orgasmos, que ordeña cada gota de semen de tu polla."
    meg "*GEMIDO* ¡SÍ! *JADEO* ¡LLÉNAME! *GEMIDO*"
    "Cumples sus órdenes sin dudarlo. La paja y la mamada, la interrupción de antes, y después comerte su sabroso coño, ha hecho que tengas los huevos llenos a reventar."
    "Os quedáis un momento quietos disfrutando del orgasmo compartido."
    call BlinkXPS3 ("c25s003_365" , "f") from _call_BlinkXPS3_2336
    "Cuando Mjolnir empieza a perder su rigidez..."
    meg "*Gemido* No salgas o voy a llenar el edredón de semen."
    meg "*Jadeo* Te he dicho que me llenaras, pero creo que te lo has tomado demasiado literalmente. *Risa*"
    "Su risa reverbera a lo largo de tu astil, ordeñándote un poco más."
    mc "Nos podemos quedar así todo el rato que quieras, como dos perrillos. *Risa*"
    "Ahora es tu risa la hace que Mjolnir vibre."
    meg "*Gemido*"
    "Os quedáis en la misma posición unos maravillosos minutos."
    scene c25s003_365d with fade
    "Cuando por fin sales del coño de [meg], tu semilla gotea sobre el edredón pese al tiempo que habéis esperado."
    meg "Te lo he dicho. *Risa*"
    scene c25s003_365e with dissolve
    "Al reírse sale un borbotón de semen que chorrea por su pierna."
    stop music fadeout (1.5)
    mc "No te preocupes. Llevaré el edredón a lavar. Déjame quitarlo y túmbate conmigo."
    call BlinkXPS3 ("c25s003_370" , "f") from _call_BlinkXPS3_2337
    play music ("music/Rise-Up.ogg")
    "Una vez retirado el edredón..."
    meg "¿Te ha gustado lo del espejo? A mí me ha parecido alucinante. Ver tu cara mientras hacías que me corriera ha sido increíble."
    mc "*Risa* Yo estaba pensando lo mismo sobre la tuya, pero no me gusta ver la mía."
    call BlinkXPS3 ("c25s003_375" , "d") from _call_BlinkXPS3_2338
    meg "¿Por qué? A mí me parece una conexión muy íntima."
    meg "Al menos ninguno de los dos ponía caras extrañas."
    mc "*Risa* Bueno, mi cara es lo suficientemente extraña por sí misma."
    call BlinkXPS3 ("c25s003_380" , "d") from _call_BlinkXPS3_2339
    meg "*Risa* Creía que la insegura era yo. A mí me pareces muy guapo."
    mc "*Risa* [meg], tengo espejos..."
    meg "*Risa* Yo también y dices que te gusta mi cuerpo."
    scene c25s003_380d with dissolve
    mc "*Risa* Touché. Me encanta tu cuerpo, y ver tu culo en el espejo es precioso."
    meg "¿Ves? Yo sin embargo lo odio, pero mientras te guste a ti, por mí está bien."
    mc "Por cierto, has dicho que no podía morderte el culo hasta que acabara el segundo desayuno. ¿Puedo ahora?"
    call BlinkXPS3 ("c25s003_385" , "d") from _call_BlinkXPS3_2340
    meg "*Risita* ¿Cómo puede gustarte morderme el culo?"
    mc "*Risa* Porque es un culo maravilloso."
    mc "Y me lo has prometido."
    meg "Entonces tendré que cumplir mi promesa, aunque no recuerdo haberlo prometido."
    scene c25s003_385d with dissolve
    mc "*Ñam*"
    meg "*Risa* Me haces cosquillas con la barba."
    call BlinkXPS3 ("c25s003_390" , "d") from _call_BlinkXPS3_2341
    mc "Si te hace reír creo que voy a seguir haciéndolo."
    meg "Tengo una pregunta... ¿Sólo te gusta morderlo?"
    $ meg._var("chanceAnal")
    if persistent.pregnancy:
        if persistent.walkthrough:
            $ wt1 = _("[gr]Anal activado para [meg].")
            $ wt2 = _("[red]Anal desactivado para [meg].")
        else:
            $ wt1 = ""
            $ wt2 = ""
        menu:
            "Me gustaría hacer más cosas." (wt = wt1):
                $ meg._var("anal", True)
                call c25s003_AnalMeg from _call_c25s003_AnalMeg
            "Con morderlo tengo suficiente." (wt = wt2):
                $ meg._var("anal", False)
                call c25s003_NoAnalMeg from _call_c25s003_NoAnalMeg
    $ resetWalkthrough ()
    call BlinkXPS3 ("c25s003_465" , "d") from _call_BlinkXPS3_2342
    meg "Para mí, lo mejor de todo son tus abrazos de después del sexo. No me malinterpretes, el sexo es increíble, pero..."
    mc "Es algo que no voy a discutir. Me encanta abrazarte."
    mc "¿Puedo hacerte una pregunta?"
    meg "Claro, adelante."
    mc "Antes has dicho que [eil] te ha estado dando consejos."
    call BlinkXPS3 ("c25s003_470" , "d") from _call_BlinkXPS3_2343
    meg "Sí, ¿te molesta que hablemos de ti?"
    mc "No, en absoluto. Tan solo me sorprende que no le preguntes a [sai]. Compartís habitación al fin y al cabo."
    call BlinkXPS3 ("c25s003_475" , "d") from _call_BlinkXPS3_2344
    meg "[sai] da consejos sobre otras cosas, pero [eil] es mucho más abierta para darlos sobre... esto."
    mc "*Risa* ¿Se distribuyen el trabajo? ¿[sai] aconseja sobre dónde llevarme a cenar y [eil] sobre cómo comerme la polla?"
    call BlinkXPS3 ("c25s003_480" , "d") from _call_BlinkXPS3_2345
    meg "*Risa* ¡Qué bruto eres!"
    call BlinkXPS3 ("c25s003_485" , "d") from _call_BlinkXPS3_2346
    meg "Pero no estás muy equivocado. Espero que no te moleste que lo estén haciendo."
    mc "Como te he dicho, no me molesta. Era solo curiosidad."
    if kia._var("route") or eva._var("route"):
        mc "No eres la primera que ha hablado sobre un consejo de [eil] y tenía curiosidad por saber cómo funcionaba."
    call BlinkXPS3 ("c25s003_490" , "d") from _call_BlinkXPS3_2347
    meg "Y espera a saber que [mar] y [nor] también dan consejos. De otro estilo, pero también los dan."
    mc "¿De qué estilo?"
    meg "Eso se lo tendrás que preguntar a ellas. Son las que más años hace que te conocen, con lo que sus opiniones son muy interesantes."
    scene c25s003_490d with dissolve
    meg "Pero ahora me gustaría pasar un rato abrazada a mi novio sin hablar de otras mujeres antes de ir a ducharme."
    mc "Me parece una idea fabulosa."
    scene c25s003_490e with dissolve
    "Tal como ha pedido [meg], pasáis un rato abrazados, charlando de cosas importantes y otras sin importancia."
    "Tan solo una pareja teniendo una conversación mientras se abrazan tras una maravillosa sesión de sexo."
    scene black with dissolve
    stop music fadeout (1.5)
    "Tras más de media hora abrazados, [meg] se va a duchar y tú te vistes de nuevo."
    return
label c25s003_NoAnalMeg:
    call BlinkXPS3 ("c25s003_395" , "d") from _call_BlinkXPS3_2348
    meg "Entonces muérdelo un poco más antes de volver aquí a abrazarme."
    mc "*Risa* A sus órdenes."
    scene c25s003_385e with dissolve
    "Mordisqueas los cachetes de [meg] un rato más, pero el abrazo prometido es muy tentador."
    return
label c25s003_AnalMeg:
    call BlinkXPS3 ("c25s003_395" , "d") from _call_BlinkXPS3_2349
    stop music fadeout (1.5)
    meg "¿Qué te gustaría hacer con mi culo?"
    play music ("music/Sexy-Background-Music.ogg")
    mc "Por el momento seguir mordisqueándolo."
    scene c25s003_385e with dissolve
    "Mordisqueas los cachetes de [meg] un rato más, pero parece que hoy está abierta a más experimentos con su culo."
    meg "*Gemido risueño*"
    "Es la primera vez que te deja mordisquearlo sin poner ningún impedimento. Y la primera vez que gime con ello."
    call BlinkXPS3 ("c25s003_400" , "d") from _call_BlinkXPS3_2350
    mc "Y después... "
    meg "¿Te gustaría que probáramos la puerta de atrás?"
    mc "Me encantaría, pero me sorprendes."
    call BlinkXPS3 ("c25s003_405" , "d") from _call_BlinkXPS3_2351
    if mar._var("anal"):
        meg "Tanto [mar] como [eil] me han dicho que puede ser alucinante contigo."
    else:
        meg "[eil] me ha dicho que puede ser alucinante contigo."
    mcp "(Otra vez [eil] dando consejos sobre mí.)"
    if mar._var("anal"):
        if persistent.family:
            mcp "(¿Pero Mamá? Eso sí que es una sorpresa, aunque [meg] y ella están muy unidas desde aquella noche en el Jazz Corner.)"
        else:
            mcp "(¿Pero [mar]? Eso sí que es una sorpresa, aunque [meg] y ella están muy unidas desde aquella noche en el Jazz Corner.)"
        mc "Supongo que si te lo han dicho es porque a ellas les gusta. También supongo que depende de cada mujer."
    else:
        mc "Supongo que si te lo ha dicho es porque a ella le gusta. También supongo que depende de cada mujer."
    call BlinkXPS3 ("c25s003_410" , "d") from _call_BlinkXPS3_2352
    meg "Me gustaría probarlo..."
    "Nada como esa frase para que Mjolnir saque la cabeza para comprobar si tiene más trabajo."
    mc "A mí también."
    meg "¿Cómo me pongo? ¿Hay alguna postura que prefieras?"
    scene c25s003_410d with fade
    "Tras darle unas indicaciones, estáis listos para empezar el experimento."
    mc "Cuando quieras."
    meg "Podemos empezar ya. Ve poco a poco, por favor."
    mc "No te preocupes, seré delicado."
    scene c25s003_415An1 with dissolve
    "Introduces delicadamente la punta de tu polla en el estrecho agujero trasero de [meg]."
    meg "*Jadeo* ¡Ooof!"
    mc "¿Cómo estás?"
    call BlinkXPS3 ("c25s003_420" , "d") from _call_BlinkXPS3_2353
    meg "Sorprendentemente bien. Creía que me iba a doler."
    mc "¿No ha dolido nada?"
    meg "Un poco de incomodidad, pero nada que no pueda soportar. Esperaba algo más doloroso que una ligera incomodidad."
    mc "¿Puedo seguir entonces metiendo el resto?"
    scene c25s003_425a with hpunch
    meg "¿No está toda dentro?"
    mc "Nope. Sólo la punta."
    call BlinkXPS3 ("c25s003_430" , "d") from _call_BlinkXPS3_2354
    meg "*Risa* Ahora entiendo por qué no ha dolido. Mete el resto. DELICADAMENTE."
    scene c25s003_415An2 with dissolve
    "Siguiendo sus indicaciones y atento a cualquier señal de dolor, metes dos tercios de tu astil tan delicadamente como puedes."
    meg "*Jadeo* ¡Ooof!"
    mc "¿Ha aparecido el dolor que esperabas? ¿Estás bien?"
    call BlinkXPS3 ("c25s003_435" , "d") from _call_BlinkXPS3_2355
    meg "*Jadeo* Estoy bien. Es una sensación más extraña que dolorosa."
    mc "Ahora tienes más de la mitad dentro."
    meg "*Jadeo* Me siento mucho más... rellena... que antes. ¿Vas a meter el resto?"
    mc "No todavía. Podemos empezar con esto. Además, mi cadera está impactando en tu culo, con lo que no creo que pueda entrar mucho más."
    call BlinkXPS3 ("c25s003_430" , "d") from _call_BlinkXPS3_2356
    meg "*Risa* Tener un culo enorme tiene sus ventajas."
    mc "*Risa* Un culo enorme y precioso. Y muy estrecho. Más estrecho todavía cuando te ríes."
    call BlinkXPS3 ("c25s003_440" , "d") from _call_BlinkXPS3_2357
    meg "Creo que puedes empezar a moverte. Pero si es muy doloroso te diré que pares, lo siento."
    mc "No tienes por qué pedir disculpas. Consiste en que lo disfrutemos los dos, no en que te duela más de lo que puedas soportar."
    meg "Entonces puedes empezar."
    scene c25s003_940pv with dissolve
    #hide c25s003_935v
    show c25s003_940v
    "Coges a [meg] de una mano, para ayudarle a que sienta el ritmo mejor."
    "Empiezas a mover tus caderas, lentamente primero, incrementando el ritmo después, y volviéndolo a bajar. Atento en todo momento a las reacciones de [meg]."
    meg "*Gemido*"
    "No se queja de dolor, pero su estrechísimo ano aprieta tu polla con fuerza en cada embestida."
    mc "¿Qué tal? ¿Estás bien?"
    meg "*Jadeo afirmativo*"
    "Entiendes que le está gustando. Si no puede hablar significa que lo está disfrutando tanto como tú. Pese a todo sigues atento para parar si es necesario."
    scene c25s003_950pv with dissolve
    hide c25s003_940v
    show c25s003_950v
    "Los dos ignoráis el espejo esta vez. [meg] está concentrada en relajar sus músculos, mientras tú estás concentrado en controlar tus movimientos para no hacerle daño."
    meg "*GEMIDO*"
    "Su gemido sube de intensidad, lo que es una buena señal. Su cuerpo se tensa mucho cada vez que aceleras el ritmo."
    "Lo que pensabas que era una señal de incomodidad resulta ser una señal de placer."
    meg "*GEMIDO*"
    "Adaptándose a tu ritmo, empieza a apretar su esfínter en cada una de sus embestidas, para liberarlo cuando te retiras. Una sensación increíble."
    scene c25s003_945pv with dissolve
    hide c25s003_950v
    show c25s003_945v
    "Con su ciclo de apretar y relajar su culo, parece una experta. Es inconcebible que sea la primera vez que lo probáis. Tu orgasmo se acerca."
    meg "*{b}GEMIDO{/b}*"
    "Tienes dudas de que sus gemidos puedan subir más aún de volumen. Esperas no correrte antes que ella. Empiezas a apretar tus músculos para retenerlo."
    meg "*{b}GEMIDO{/b}*"
    "Pero es imposible. [meg] está haciendo cosas alrededor de tu polla que te están llevando más allá del punto de no retorno."
    call OrgasmXS3 ("c25s003_445") from _call_OrgasmXS3_56
    mc "¡Mpfft!"
    "Sin poderlo evitar, te corres dentro de su culo, llenando sus intestinos."
    meg "*{b}GEMIDO IMPERATIVO{/b}*"
    "Interpretas ese gemido como una orden de continuar con las embestidas. Ella debe estar a punto de llegar también."
    scene c25s003_950pv with dissolve
    hide c25s003_945v
    show c25s003_950v
    "Sigues bombeando, notando con la punta de tu polla toda la humedad de tu semen dentro de su culo. Mucho más lubricado ahora gracias a tus fluidos."
    meg "*{size=+30}{b}GEMIDO{/b}{/size}*"
    "Definitivamente sus gemidos podían subir de volumen. La voz de la cantante tiene mucha más potencia de la que esperabas."
    meg "*{size=+30}{b}GEMIDO{/b}{/size}*"
    "Su cuerpo por fin se tensa cuando estás llegando al final de tu resistencia."
    call OrgasmXS3 ("c25s003_450") from _call_OrgasmXS3_57
    meg "{size=+20}{b}*GEMIDO* ¡OH, SÍ! *JADEO* ¡INCREÍBLE! *GEMIDO*{/b}{/size}"
    "Notas cómo la trampa en la que se ha convertido su ano se cierra con fuerza sobre tu astil. Maravillosa trampa."
    "Tienes que dejar de bombear para evitar hacerle daño cuando está apretando con tanta fuerza."
    call BlinkXPS3 ("c25s003_455" , "f") from _call_BlinkXPS3_2358
    "Una vez han pasado un par de minutos en los que su orgasmo recorre todo su cuerpo..."
    meg "*Jadeo* [eil] tenía razón... Ha sido alucinante..."
    mc "¿Estás bien?"
    call BlinkXPS3 ("c25s003_460" , "d") from _call_BlinkXPS3_2359
    meg "*Jadeo* ¿Bien? Es un tipo diferente de orgasmo... *Jadeo* Pero... es tremendo... *Jadeo*"
    meg "*Jadeo* Ahora necesito descansar un rato... Ven aquí y abrázame."
    stop music fadeout (1.5)
    "Ese abrazo es muy tentador."
    play music ("music/Rise-Up.ogg")
    return
label c25s004_IceCream:
    if _in_replay:
        call mrS3_nor_route from _call_mrS3_nor_route_5
        call mrS3_mee_route from _call_mrS3_mee_route_4
    scene black with dissolve
    play sound ("music/notification.ogg")
    "[nor] te manda un mensaje preguntándote si le puedes llevar un bol de cristal que tiene [mar] en la cocina."
    scene c25s004_100a with fade
    play music ("music/RhythmPlay.ogg")
    "Tras pasar por la cocina para recoger el bol..."
    mc "Buenos días. Te traigo el bol que has pedido."
    nor "Gracias, [mc]."
    mc "¿Ha pasado algo catastrófico?"
    scene c25s004_100b with dissolve
    mee "No, le hemos mandado el mensaje a varias de las chicas, pero nadie contestaba."
    nor "No sé dónde se han metido todas. Por eso te lo hemos mandado a ti."
    mc "No me refería a eso. Me extraña que dejes que Meemaw se acerque a la cocina si no es para comer."
    call BlinkXPS3 ("c25s004_105" , "d") from _call_BlinkXPS3_2360
    mee "*Grrr*"
    call BlinkXPS3 ("c25s004_110" , "d") from _call_BlinkXPS3_2361
    nor "Hemos decidido hacer una sesión para estrechar lazos..."
    call BlinkXPS3 ("c25s004_115" , "d") from _call_BlinkXPS3_2362
    mee "Estrecharlos más aún..."
    call BlinkXPS3 ("c25s004_120" , "d") from _call_BlinkXPS3_2363
    nor "Sí, eso. Y ya sabes que los momentos de madre e hija cocinando juntas son un clásico."
    mc "*Risa* Sí, normalmente es la madre enseñándole a la hija."
    mc "*Risa* ¿Te va a enseñar a hacer carbón?"
    call BlinkXPS3 ("c25s004_125" , "d") from _call_BlinkXPS3_2364
    mee "Me va a enseñar ella a mí. Vamos a hacer helado."
    mc "Mmmmm... helado. ¿Necesitáis un catador? Ya sabéis, alguien imparcial que pueda dar una opinión sincera..."
    call BlinkXPS3 ("c25s004_130" , "d") from _call_BlinkXPS3_2365
    mee "Sí, por supuesto..."
    mc "Cuando esté preparado..."
    mee "*Risa* Por eso hemos pensado en Jamaal."
    mc "*Risa* Eso ha sido cruel, Meemaw."
    call BlinkXPS3 ("c25s004_135" , "d") from _call_BlinkXPS3_2366
    nor "*Risa* Eso te pasa por meterte con las dotes culinarias de mi madre."
    mc "Et tu, [nor]? [red]('¿Tú también, [nor]?'' en Latín, como la famosa frase de Julio César cuando Bruto lo traicionó.{/color})"
    call BlinkXPS3 ("c25s004_140" , "d") from _call_BlinkXPS3_2367
    nor "*Risa* Estamos en un momento de reforzar vínculos. Me tengo que poner de su lado."
    mc "Creo que me las pagaréis. *Risa* Mi venganza será tremenda."
    call BlinkXPS3 ("c25s004_155" , "d") from _call_BlinkXPS3_2368
    mee "Por si quieres probarlo a escondidas, prueba el del recipiente grande, por favor."
    mc "*Risa* ¿El pequeño es el que vas a preparar tú y no quieres que muera envenenado?"
    call BlinkXPS3 ("c25s004_150" , "h") from _call_BlinkXPS3_2369
    nor "¡[mc]! Para ya con la broma. Mi madre se está esforzando."
    mc "Vale, ya paro... ¿Qué pasa con el recipiente pequeño?"
    call BlinkXPS3 ("c25s004_145" , "d") from _call_BlinkXPS3_2370
    mee "Es un experimento que quería hacer. No sabemos cómo va a quedar."
    mc "¿Qué experimento? *Risa* ¿Vas a usar tu leche?"
    scene c25s004_100c with dissolve
    "Las dos se miran avergonzadas" id c25s004_IceCream_efb31452
    mc "¿Qué? ¿He acertado?"
    scene c25s004_100d with dissolve
    nor "Y a mí me ha parecido una buena idea..." (multiple=2)
    mee "Leí una receta en internet..." (multiple=2)
    nor "Era una forma de aprovecharla..." (multiple=2)
    mee "Estamos tirando mucha leche todos los días..." (multiple=2)
    nor "Y dejaros a vosotros el helado normal..." (multiple=2)
    mee "Pensábamos comerlo nosotras si sale bien..." (multiple=2)
    mc "Me parece una buena idea."
    scene c25s004_100e with hpunch
    nor "¿Qué?" (multiple=2)
    mee "¿Qué?" (multiple=2)
    $ mee._var("chanceIceCream", True)
    if persistent.walkthrough:
        $ wt1 = _("Comerás helado de leche materna.")
        $ wt2 = _("No comerás helado de leche materna.")
    else:
        $ wt1 = ""
        $ wt2 = ""
    menu:
        "Me encantaría probarlo." (wt = wt1):
            $ mee._var("iceCream", True)
        "No es que lo vaya a probar, pero me parece bien." (wt = wt2):
            $ mee._var("iceCream", False)
    $ resetWalkthrough()
    call BlinkXPS3 ("c25s004_160" , "d") from _call_BlinkXPS3_2371
    mee "Me sorprendes... creía que ibas a pensar que era raro hacer helado con mi leche."
    mc "No es lo más habitual, pero si la gente hace queso, ¿por qué no helado? Parece más sencillo de hacer, ¿no?"
    call BlinkXPS3 ("c25s004_165" , "d") from _call_BlinkXPS3_2372
    if persistent.lactation:
        nor "Creía que lo de querer probar la leche materna lo decías en broma. ¡Resulta que sí que tienes ese fetiche!"
    else:
        nor "Dijiste que no era uno de tus fetiches..."
    if mee._var("route"):
        scene c25s004_160d with dissolve
        pause (1.0)
        call BlinkXPS3 ("c25s004_165" , "d") from _call_BlinkXPS3_2373
    mc "No tiene nada que ver con un fetiche. *Risa* ¡Es helado, no sexo!"
    call BlinkXPS3 ("c25s004_170" , "d") from _call_BlinkXPS3_2374
    mee "Bueno, si [mc] quiere probarlo, deberíamos dejarle... por raro que sea."
    mc "Gracias, Meemaw. Aunque si va a llevar tu toque en la preparación, no sé si fiarme. *Risa* ¡Es broma!"
    call BlinkXPS3 ("c25s004_175" , "d") from _call_BlinkXPS3_2375
    mee "*Risa* Va a tener mucho más de mí que mi toque."
    mc "*Risa* Tienes razón."
    call BlinkXPS3 ("c25s004_180" , "d") from _call_BlinkXPS3_2376
    nor "Y ahora ya te puedes ir. Esto era una sesión para estrechar lazos madre-hija, no para que estés aquí interrumpiéndonos."
    mc "Vale, ya me voy."
    if nor._var("route"):
        call BlinkXPS3 ("c25s004_185" , "d") from _call_BlinkXPS3_2377
        nor "No sin antes darme un beso."
        scene c25s004_100f with dissolve
        "Rodeas la isla de la cocina y besas a [nor]."
        if not mee._var("route"):
            "Hace unos días, [mee] hubiera puesto el grito en el cielo. Ahora ya lo ha aceptado." id c25s004_IceCream_f4fbec9f
        else:
            "Estás tentado de hacer lo mismo con [mee], pero no podrás hacerlo hasta saber el resultado de la cita de esta noche." id c25s004_IceCream_f4e13850
    scene c25s004_100g with dissolve
    mc "Os veo luego, chicas."
    if mee._var("iceCream"):
        mc "Guardadme una porción de helado."
    nor "Hasta luego, [mc]." (multiple=2) id c25s004_IceCream_37856727
    mee "Hasta luego, cielo." (multiple=2)
    scene black with dissolve
    stop music fadeout (1.5)
    "Vuelves hacia tu habitación, quieres trabajar un poco en la contabilidad antes de la hora de comer."
    return
label c25s004_KimDebLisaSai:
    if _in_replay:
        call mrS3_kim_route from _call_mrS3_kim_route_1
        call mrS3_lis_route from _call_mrS3_lis_route_3
        call mrS3_deb_route from _call_mrS3_deb_route_10
    scene c25s004_200a with dissolve
    play music ("music/SneakySnitch.ogg")
    "Cuando estás a punto de llegar a la planta de las estudiantes escuchas voces..."
    sai "... Yo nunca lo llevaría a un restaurante vegetariano. Sería un fracaso anunciado."
    eil "*Risa* Estoy de acuerdo. Se pasaría la cena protestando por todo."
    if kim._var("route"):
        kim "¿Entonces dónde es un buen sitio para ir a comer con él? No quiero meter la pata el día que tengamos nuestra primera cita."
    elif deb._var("route"):
        deb "¿Entonces dónde es un buen sitio para ir a comer con él? No quiero meter la pata el día que tengamos nuestra primera cita."
    elif lis._var("route"):
        lis "¿Entonces dónde es un buen sitio para ir a comer con él? Yo soy vegana y..."
    else:
        kat "¿Entonces dónde lo llevaríais? No es que yo vaya a ir a cenar con él, pero..."
    mcp "([sai] y [eil] hablando de mí. Será mejor que no me oigan.)"
    scene c25s004_200b with dissolve
    mcp "(Desde aquí sólo puedo ver a [kat].)"
    if persistent.walkthrough:
        $ wt1 = _("Más diálogo.")
        $ wt2 = _("Menos diálogo.")
    else:
        $ wt1 = ""
        $ wt2 = ""
    menu:
        "Escuchar." (wt = wt1):
            $ mc._var("listenStairs", True)
            call c25s004_Listen from _call_c25s004_Listen
        "Hacerte notar." (wt = wt2):
            $ mc._var("listenStairs", False)
    $ resetWalkthrough()
    "Haces un poco de ruido en la escalera, forzando las pisadas en los escalones."
    mc "Hola, [kat]."
    scene c25s004_200c with hpunch
    kat "*Jadeo* ¿Qué? ¡Oh, hola [mc]!"
    "Oyes ruido de gente moviéndose."
    mc "¿Qué tal, [kat]? ¿Estás sola?"
    scene c25s004_200d with dissolve
    play sound ("music/Portazo.ogg")
    "*Blam*"
    "Oyes cerrarse la habitación de [sai]."
    call BlinkXPS3 ("c25s004_205" , "d") from _call_BlinkXPS3_2378
    kat "No, estoy con [eil]. Estábamos charlando."
    mc "Ah, okay. No os molesto. Iba de camino a mi habitación."
    call BlinkXPS3 ("c25s004_210" , "d") from _call_BlinkXPS3_2379
    "Subes hasta el rellano."
    mc "Hola, [eil]. ¿No trabajas hoy?"
    eil "Esta tarde. [eri] y yo entramos tarde hoy."
    mcp "(Conozco esa sonrisa. Ella sabe que yo sé que oculta algo.)"
    mc "Okay. Decídmelo si necesitáis que os lleve. Estaré en mi habitación trabajando un poco hasta la hora de comer."
    scene c25s004_200e with dissolve
    mc "Os veo luego, chicas."
    kat "Hasta luego, [mc]." (multiple=2)
    eil "Hasta luego, [mc]." (multiple=2)
    scene c25s004_200f with dissolve
    "Abres la puerta de tu habitación para dejar el móvil antes de ir al lavabo."
    "En el momento en que cierras tu puerta, oyes cómo se abre la de [sai]."
    sai "[kat], te tenías que ocupar de vigilar que no viniera nadie. Y menos aún [mc]."
    kat "Lo siento. La conversación estaba interesante y no lo he oído llegar."
    deb "A mí me ha pasado lo mismo. Estaba tan atenta a lo que decíais que no lo he oído llegar."
    if not deb._var("route"):
        deb "Y eso teniendo en cuenta que dudo que alguna vez vaya a cenar a solas con él."
    lis "Estoy en la misma situación que [deb.nick]."
    if deb._var("route") and not lis._var("route"):
        lis "Y eso teniendo en cuenta que dudo que alguna vez vaya a cenar a solas con él."
    kim "Es que lo explicáis de tal forma que es casi como estar ahí, en vuestras citas."
    if deb._var("route") and lis._var("route") and not kim._var("route"):
        kim "Aunque dudo que me vayan a servir de mucho esos conocimientos."
    eil "Chicas, no sé si nos ha oído, pero sabe que estaba pasando algo. Se lo he leído en la cara."
    if not mc._var("listenStairs"):
        mcp "(Será mejor que continúe con lo que iba a hacer. Si no las he querido escuchar antes, mejor será no hacerlo ahora.)"
    else:
        kat "Bueno, ya se ha ido. Ibas a hablar del columpio, [eil]."
        mcp "(Será mejor que continúe con lo que iba a hacer. Si van a empezar a hablar de [eil] y de mí en el columpio...)"
    stop music fadeout (1.5)
    scene black with dissolve
    "Vas al lavabo y trabajas durante una hora, hasta que empieza a entrarte sed. Sigues sin acordarte de coger una botella de agua."
    "Bajas a la cocina a beber algo."
    return
label c25s004_Listen:
    scene c25s004_200g with dissolve
    "Por sus voces las puedes imaginar sentadas en el suelo, alrededor de las dos maestras."
    "Casi se te escapa la risa y delatas tu presencia."
    call BlinkXPS3 ("c25s004_215" , "d") from _call_BlinkXPS3_2380
    kim "¿Dónde lo llevaste a cenar en tu primera cita, [sai]?"
    call BlinkXPS3 ("c25s004_220" , "d") from _call_BlinkXPS3_2381
    sai "Bueno, fue él quien me llevó a comer a mí, no a cenar. Fue en un restaurante escandinavo. Pero no fue la primera cita. Esa había sido en la cafetería de la que os he hablado."
    sai "Por si os interesa, pidió albóndigas suecas y smorrebrod, o como se diga."
    call BlinkXPS3 ("c25s004_225" , "d") from _call_BlinkXPS3_2382
    eil "*Risa* Me lo imaginaba. Lo que me hubiera sorprendido es que hubiese pedido arenque."
    call BlinkXPS3 ("c25s004_230" , "d") from _call_BlinkXPS3_2383
    deb "¿Y tú, [eil]? ¿Cómo fue vuestra primera cita?"
    call BlinkXPS3 ("c25s004_235" , "d") from _call_BlinkXPS3_2384
    eil "Te va a parecer gracioso, pero nunca tuvimos una 'primera cita'. Nos veíamos todos los días en el instituto, la cosa entre nosotros surgió poco a poco."
    eil "Para cuando nos dimos cuenta, estábamos saliendo y no habíamos tenido una cita. La mayoría de las veces comíamos con Jamaal. Imaginaos qué romántico era todo. *Risa*"
    call BlinkXPS3 ("c25s004_240" , "d") from _call_BlinkXPS3_2385
    if lis._var("route"):
        lis "A mí me gustaría tener una primera cita. Sería algo que recordar siempre y... no sé... como una fecha para nuestro aniversario de salir juntos."
    else:
        lis "Cuando salga con alguien, me gustaría tener una primera cita. Sería algo que recordar siempre y como una fecha para nuestro aniversario de salir juntos."
    lis "*Risita* Al menos hasta que pueda sustituírlo por el aniversario de boda."
    call BlinkXPS3 ("c25s004_245" , "d") from _call_BlinkXPS3_2386
    if lis._var("route"):
        deb "No digas tonterías, [lis]. Tienes marcado en tu diario el día que te besó por primera vez, cuando os encerré en nuestra habitación."
        deb "Creo que, cuando se cumpla un año de ese beso, lo celebrarás más que cuando se cumpla un año de vuestra futura primera cita."
    else:
        deb "No digas tonterías, [lis]. Si te hubiera besado cuando os encerré en nuestra habitación, tendrías ese día marcado en tu diario."
        deb "Creo que, cuando se cumpla un año de tu primer beso cuando salgas con alguien, lo celebrarás más que cuando se cumpla un año de vuestra futura primera cita."
    if deb._var("route"):
        deb "A mí me gustaría celebrar como nuestro aniversario el día que nos besamos en el lago por primera vez."
    call BlinkXPS3 ("c25s004_250" , "d") from _call_BlinkXPS3_2387
    kat "Pero eso es porque tú y [kim] sois unas románticas. *Risa* La mayoría de la gente celebra la boda."
    kat "Pero la pregunta importante es... ¿Lees el diario de tu hermana, [deb.nick]?"
    call BlinkXPS3 ("c25s004_255" , "d") from _call_BlinkXPS3_2388
    sai "Chicas, guardad vuestros diarios bajo llave. *Risa* Tenemos una espía."
    mcp "(*Risa mental* Sí, pero no tiene que ver con los diarios.)"
    call BlinkXPS3 ("c25s004_260" , "d") from _call_BlinkXPS3_2389
    lis "*Risa* Siempre se lo he dejado leer. Es un diario online y tiene permiso para leerlo... al menos tiene permisos para ver algunas entradas."
    lis "Nos ha ido muy bien algunas veces. Ya sabéis que a veces me pongo muy estúpida sin venir a cuento."
    todas "*Risa* Sí."
    call BlinkXPS3 ("c25s004_265" , "d") from _call_BlinkXPS3_2390
    kim "*Risa* Somos unas malas amigas... Tendríamos que haberle dicho, 'No, [lis], siempre que te pones estúpida es por una razón justificada.'"
    kim "*Risa* Pero mentir también es de malas amigas... Estoy en una encrucijada."
    todas "*Risa*"
    call BlinkXPS3 ("c25s004_270" , "d") from _call_BlinkXPS3_2391
    lis "*Risa* Te robaré el pintalabios como venganza por lo que acabas de decir."
    lis "Es broma. Me encanta que me digáis lo que hago mal. Hasta ahora sólo se atrevía [deb.nick]."
    call BlinkXPS3 ("c25s004_275" , "d") from _call_BlinkXPS3_2392
    kat "Chicas, nos estamos desviando del tema. Estábamos hablando de [mc]."
    kat "[eil], la última vez estabas diciendo algo de un columpio."
    call BlinkXPS3 ("c25s004_280" , "d") from _call_BlinkXPS3_2393
    eil "Bueno, ha habido varias veces en un columpio, pero..."
    mcp "(Creo que es el momento de hacerme notar. Si empiezan a hablar de sexo y me descubren escuchando se van a enfadar.)"
    mcp "(Especialmente si hablan de sexo conmigo.)"
    return
label c25s004_Pickles:
    if _in_replay:
        call mrS3_oma_pregnant from _call_mrS3_oma_pregnant
        if not oma._var("pregnant"):
            call mrS3_eri_pregnant from _call_mrS3_eri_pregnant
            if not eri._var("pregnant"):
                call mrS3_dap_pregnant from _call_mrS3_dap_pregnant
                if not dap._var("pregnant"):
                    call mrS3_nor_pregnant from _call_mrS3_nor_pregnant_1
                    if not nor._var("pregnant"):
                        call mrS3_sca_pregnant from _call_mrS3_sca_pregnant_2
                        if not sca._var("pregnant"):
                            call mrS3_meg_pregnant from _call_mrS3_meg_pregnant
                            if not meg._var("pregnant"):
                                call mrS3_sai_pregnant from _call_mrS3_sai_pregnant_1
                                if not sai._var("pregnant"):
                                    call mrS3_sam_pregnant from _call_mrS3_sam_pregnant_2
                                    if not sam._var("pregnant"):
                                        call mrS3_mar_pregnant from _call_mrS3_mar_pregnant_1
                                        if not mar._var("pregnant"):
                                            call mrS3_eil_pregnant from _call_mrS3_eil_pregnant_1
                                            if not eil._var("pregnant"):
                                                call mrS3_emm_pregnant from _call_mrS3_emm_pregnant
                                                if not mar._var("pregnant"):
                                                    call mrS3_mar_route from _call_mrS3_mar_route_10
                                        else:
                                            $ mar._var("route", True)
    $ pickles = True
    play music ("music/These-Little-Moments.ogg")
    if oma._var("pregnant"):
        call c25s004_OmaPickles from _call_c25s004_OmaPickles
    elif eri._var("pregnant"):
        call c25s004_EriPickles from _call_c25s004_EriPickles
    elif dap._var("pregnant"):
        call c25s004_DapPickles from _call_c25s004_DapPickles
    elif nor._var("pregnant"):
        call c25s004_NorPickles from _call_c25s004_NorPickles
    elif sca._var("pregnant"):
        call c25s004_ScaPickles from _call_c25s004_ScaPickles
    elif meg._var("pregnant"):
        call c25s004_MegPickles from _call_c25s004_MegPickles
    elif sai._var("pregnant"):
        call c25s004_SaiPickles from _call_c25s004_SaiPickles
    elif sam._var("pregnant"):
        call c25s004_SamPickles from _call_c25s004_SamPickles
    elif mar._var("pregnant"):
        call c25s004_MarPickles from _call_c25s004_MarPickles
    elif eil._var("pregnant"):
        call c25s004_EilPickles from _call_c25s004_EilPickles
    elif emm._var("pregnant"):
        call c25s004_EmmPickles from _call_c25s004_EmmPickles
    else:
        call c25s004_MarPickles from _call_c25s004_MarPickles_1
        $ pickles = False
    stop music fadeout (1.5)
    return
label c25s004_MarPickles:
    $ whoPickles = mar
    scene c25s004_005a with fade
    "Llegas a la cocina y ves a [mar] con la cabeza metida en la nevera."
    mc "¿Estás preparando la comida?"
    call BlinkXPS3 ("c25s004_010a" , "d") from _call_BlinkXPS3_2245
    if mar._var("pregnant"):
        mom "No, aún no. Me han apetecido pepinillos con helado de chocolate, pero no nos quedan pepinillos."
        mc "¡Aargh! *Risa* ¡Eso tiene que tener un gusto horrendo! No te he visto nunca comer algo así."
        mc "¿Es posible que sea un antojo del embarazo?"
        call BlinkXPS3 ("c25s004_015a" , "d") from _call_BlinkXPS3_2246
        if persistent.family:
            mom "No lo creo. No tuve antojos cuando estuve embarazada de ti ni de [emm]. Siempre he pensado que los antojos son una tontería para explotar a los pobres padres."
        else:
            mom "No lo creo. Siempre he pensado que los antojos son una tontería para explotar a los pobres padres."
        mom "Pero es posible... ahora que lo dices, suena asqueroso."
        mc "¿Quieres que vaya a comprar pepinillos?"
        call BlinkXPS3 ("c25s004_020a" , "d") from _call_BlinkXPS3_2247
        mom "Si no te importa... Pese a que suena asqueroso, me siguen apeteciendo."
        mc "No te preocupes, ahora voy a comprarlos."
    else:
        mom "Estaba empezando a prepararla, pero no hay suficiente pollo."
        mc "¿Quieres que vaya a comprar?"
        call BlinkXPS3 ("c25s004_020a" , "d") from _call_BlinkXPS3_2248
        mom "Si no te importa... Iba a hacer paella, aunque seguramente algún español me mataría si probase mi receta de paella."
        mc "*Risa* Ningún problema. Y seguramente ese español cambiaría la receta tradicional por la tuya en cuanto la probara. Tu paella está buenísima."
    if mar._var("route"):
        call KissXPS3 ("c25s004_025a" , "d") from _call_KissXPS3_43
        mom "Gracias, mi amor."
    call BlinkXPS3 ("c25s004_030a" , "d") from _call_BlinkXPS3_2249
    mom "¿Puedes pasar a buscar a [mad.nick] también? Así le ahorras tener que coger un Under para venir a comer."
    mc "Ningún problema. ¿La avisas tú de que voy a por ella?"
    return
label c25s004_EmmPickles:
    $ whoPickles = emm
    scene c25s004_005b with fade
    "Llegas a la cocina y ves a [emm] con la cabeza metida en la nevera."
    mc "¿Estás buscando algo para comer antes de la hora de la comida?"
    call BlinkXPS3 ("c25s004_010b" , "d") from _call_BlinkXPS3_2250
    emm "Me han apetecido pepinillos con helado de chocolate, pero no nos quedan pepinillos."
    mc "¡Aargh! *Risa* ¡Eso tiene que tener un gusto horrendo! No te he visto nunca comer algo así."
    mc "¿Es posible que sea un antojo del embarazo?"
    call BlinkXPS3 ("c25s004_015b" , "d") from _call_BlinkXPS3_2251
    if persistent.family:
        emm "No lo creo. Mamá siempre ha dicho que los antojos son una tontería para explotar a los pobres padres, y que ella no tuvo cuando estuvo embarazada."
    else:
        emm "No lo creo. Siempre he pensado que los antojos son una tontería para explotar a los pobres padres."
    emm "Pero es posible... ahora que lo dices, suena asqueroso."
    mc "¿Quieres que vaya a comprar pepinillos?"
    call BlinkXPS3 ("c25s004_020b" , "d") from _call_BlinkXPS3_2252
    emm "Si no te importa... Pese a que suena asqueroso, me siguen apeteciendo."
    mc "No te preocupes, ahora voy a comprarlos."
    call KissXPS3 ("c25s004_025b" , "d") from _call_KissXPS3_44
    emm "Gracias, mi amor."
    call BlinkXPS3 ("c25s004_030b" , "d") from _call_BlinkXPS3_2253
    emm "¿Puedes pasar a buscar a [mad.nick] también? Así le ahorras tener que coger un Under para venir a comer."
    mc "Ningún problema. ¿La avisas tú de que voy a por ella?"
    return
label c25s004_EriPickles:
    $ whoPickles = eri
    scene c25s004_005c with fade
    "Llegas a la cocina y ves a [eri] con la cabeza metida en la nevera."
    mc "¿Estás buscando algo para comer antes de la hora de la comida?"
    call BlinkXPS3 ("c25s004_010c" , "d") from _call_BlinkXPS3_2254
    eri "Me han apetecido pepinillos con helado de chocolate, pero no nos quedan pepinillos."
    mc "¡Aargh! *Risa* ¡Eso tiene que tener un gusto horrendo! No te he visto nunca comer algo así."
    mc "¿Es posible que sea un antojo del embarazo?"
    call BlinkXPS3 ("c25s004_015c" , "d") from _call_BlinkXPS3_2255
    if persistent.family:
        eri "No lo creo. Mi madre siempre ha dicho que los antojos son una tontería para explotar a los pobres padres, y que ella no tuvo cuando estuvo embarazada."
    else:
        eri "No lo creo. Siempre he pensado que los antojos son una tontería para explotar a los pobres padres."
    eri "Pero es posible... ahora que lo dices, suena asqueroso."
    mc "¿Quieres que vaya a comprar pepinillos?"
    call BlinkXPS3 ("c25s004_020c" , "d") from _call_BlinkXPS3_2256
    eri "Si no te importa... Pese a que suena asqueroso, me siguen apeteciendo."
    mc "No te preocupes, ahora voy a comprarlos."
    call KissXPS3 ("c25s004_025c" , "d") from _call_KissXPS3_45
    eri "Gracias, mi amor."
    call BlinkXPS3 ("c25s004_030c" , "d") from _call_BlinkXPS3_2257
    eri "¿Puedes pasar a buscar a [mad.nick] también? Así le ahorras tener que coger un Under para venir a comer."
    mc "Ningún problema. ¿La avisas tú de que voy a por ella?"
    return
label c25s004_DapPickles:
    $ whoPickles = dap
    scene c25s004_005d with fade
    "Llegas a la cocina y ves a [dap] con la cabeza metida en la nevera."
    mc "¿Estás buscando algo para comer antes de la hora de la comida?"
    call BlinkXPS3 ("c25s004_010d" , "d") from _call_BlinkXPS3_2258
    dap "Me han apetecido pepinillos con helado de chocolate, pero no nos quedan pepinillos."
    mc "¡Aargh! *Risa* ¡Eso tiene que tener un gusto horrendo! No te he visto nunca comer algo así."
    mc "¿Es posible que sea un antojo del embarazo?"
    call BlinkXPS3 ("c25s004_015d" , "d") from _call_BlinkXPS3_2259
    if persistent.family:
        dap "No lo creo. Mi madre siempre ha dicho que los antojos son una tontería para explotar a los pobres padres, y que ella no tuvo cuando estuvo embarazada."
    else:
        dap "No lo creo. Siempre he pensado que los antojos son una tontería para explotar a los pobres padres."
    dap "Pero es posible... ahora que lo dices, suena asqueroso."
    mc "¿Quieres que vaya a comprar pepinillos?"
    call BlinkXPS3 ("c25s004_020d" , "d") from _call_BlinkXPS3_2260
    dap "Si no te importa... Pese a que suena asqueroso, me siguen apeteciendo."
    mc "No te preocupes, ahora voy a comprarlos."
    call KissXPS3 ("c25s004_025d" , "d") from _call_KissXPS3_46
    dap "Gracias, mi amor."
    call BlinkXPS3 ("c25s004_030d" , "d") from _call_BlinkXPS3_2261
    dap "¿Puedes pasar a buscar a [mad.nick] también? Así le ahorras tener que coger un Under para venir a comer."
    mc "Ningún problema. ¿La avisas tú de que voy a por ella?"
    return
label c25s004_NorPickles:
    if _in_replay:
        call mrS3_nor_nick from _call_mrS3_nor_nick
    $ whoPickles = nor
    scene c25s004_005e with fade
    "Llegas a la cocina y ves a [nor] con la cabeza metida en la nevera."
    mc "¿Estás buscando algo para comer antes de la hora de la comida?"
    call BlinkXPS3 ("c25s004_010e" , "d") from _call_BlinkXPS3_2262
    nor "Me han apetecido pepinillos con helado de chocolate, pero no nos quedan pepinillos."
    mc "¡Aargh! *Risa* ¡Eso tiene que tener un gusto horrendo! No te he visto nunca comer algo así."
    mc "¿Es posible que sea un antojo del embarazo?"
    call BlinkXPS3 ("c25s004_015e" , "d") from _call_BlinkXPS3_2263
    if persistent.family:
        nor "No lo creo. Siempre he pensado que los antojos son una tontería para explotar a los pobres padres. Yo no tuve cuando estuve embarazada de las gemelas."
    else:
        nor "No lo creo. Siempre he pensado que los antojos son una tontería para explotar a los pobres padres."
    nor "Pero es posible... ahora que lo dices, suena asqueroso."
    mc "¿Quieres que vaya a comprar pepinillos?"
    call BlinkXPS3 ("c25s004_020e" , "d") from _call_BlinkXPS3_2264
    nor "Si no te importa... Pese a que suena asqueroso, me siguen apeteciendo."
    mc "No te preocupes, ahora voy a comprarlos."
    call KissXPS3 ("c25s004_025e" , "d") from _call_KissXPS3_47
    nor "Gracias, mi amor."
    $ uNick = nor._var("uNick")
    mc "No hay de qué, [uNick!t]."
    call BlinkXPS3 ("c25s004_030e" , "d") from _call_BlinkXPS3_2265
    nor "¿Puedes pasar a buscar a [mad.nick] también? Así le ahorras tener que coger un Under para venir a comer."
    mc "Ningún problema. ¿La avisas tú de que voy a por ella?"
    return
label c25s004_ScaPickles:
    $ whoPickles = sca
    scene c25s004_005f with fade
    "Llegas a la cocina y ves a [sca] con la cabeza metida en la nevera."
    mc "¿Estás buscando algo para comer antes de la hora de la comida?"
    call BlinkXPS3 ("c25s004_010f" , "d") from _call_BlinkXPS3_2266
    sca "Me han apetecido pepinillos con helado de chocolate, pero no nos quedan pepinillos."
    mc "¡Aargh! *Risa* ¡Eso tiene que tener un gusto horrendo! No te he visto nunca comer algo así."
    mc "¿Es posible que sea un antojo del embarazo?"
    call BlinkXPS3 ("c25s004_015f" , "d") from _call_BlinkXPS3_2267
    if persistent.family:
        sca "No lo creo. [nor] me ha dicho que los antojos son una tontería para explotar a los pobres padres, y que ella no tuvo cuando estuvo embarazada."
    else:
        sca "No lo creo. [nor] me ha dicho que los antojos son una tontería para explotar a los pobres padres."
    sca "Pero es posible... ahora que lo dices, suena asqueroso."
    mc "¿Quieres que vaya a comprar pepinillos?"
    call BlinkXPS3 ("c25s004_020f" , "d") from _call_BlinkXPS3_2268
    sca "Si no te importa... Pese a que suena asqueroso, me siguen apeteciendo."
    mc "No te preocupes, ahora voy a comprarlos."
    call KissXPS3 ("c25s004_025f" , "d") from _call_KissXPS3_48
    sca "Gracias, mi amor."
    mc "No hay de qué, mi precioso Koala."
    call BlinkXPS3 ("c25s004_030f" , "d") from _call_BlinkXPS3_2269
    sca "¿Puedes pasar a buscar a [mad.nick] también? Así le ahorras tener que coger un Under para venir a comer."
    mc "Ningún problema. ¿La avisas tú de que voy a por ella?"
    return
label c25s004_MegPickles:
    $ whoPickles = meg
    scene c25s004_005g with fade
    "Llegas a la cocina y ves a [meg] con la cabeza metida en la nevera."
    mc "¿Estás buscando algo para comer antes de la hora de la comida?"
    call BlinkXPS3 ("c25s004_010g" , "d") from _call_BlinkXPS3_2270
    meg "Me han apetecido pepinillos con helado de chocolate, pero no nos quedan pepinillos."
    mc "¡Aargh! *Risa* ¡Eso tiene que tener un gusto horrendo! No te he visto nunca comer algo así."
    mc "¿Es posible que sea un antojo del embarazo?"
    call BlinkXPS3 ("c25s004_015g" , "d") from _call_BlinkXPS3_2271
    if persistent.family:
        meg "No lo creo. [mar] me ha dicho que los antojos son una tontería para explotar a los pobres padres, y que ella no tuvo cuando estuvo embarazada." id c25s004_MegPickles_8e84f1ad
    else:
        meg "No lo creo. Siempre he pensado que los antojos son una tontería para explotar a los pobres padres."
    meg "Pero es posible... ahora que lo dices, suena asqueroso."
    mc "¿Quieres que vaya a comprar pepinillos?"
    call BlinkXPS3 ("c25s004_020g" , "d") from _call_BlinkXPS3_2272
    meg "Si no te importa... Pese a que suena asqueroso, me siguen apeteciendo."
    mc "No te preocupes, ahora voy a comprarlos."
    call KissXPS3 ("c25s004_025g" , "d") from _call_KissXPS3_49
    meg "Gracias, mi amor."
    call BlinkXPS3 ("c25s004_030g" , "d") from _call_BlinkXPS3_2273
    meg "¿Puedes pasar a buscar a [mad.nick] también? Así le ahorras tener que coger un Under para venir a comer."
    mc "Ningún problema. ¿La avisas tú de que voy a por ella?"
    return
label c25s004_SaiPickles:
    $ whoPickles = sai
    scene c25s004_005h with fade
    "Llegas a la cocina y ves a [sai] con la cabeza metida en la nevera."
    mc "¿Estás buscando algo para comer antes de la hora de la comida? ¿Ya se ha acabado el interrogatorio?"
    call BlinkXPS3 ("c25s004_010h" , "d") from _call_BlinkXPS3_2274
    sai "Me han apetecido pepinillos con helado de chocolate, pero no nos quedan pepinillos."
    mc "¡Aargh! *Risa* ¡Eso tiene que tener un gusto horrendo! No te he visto nunca comer algo así."
    mc "¿Es posible que sea un antojo del embarazo?"
    call BlinkXPS3 ("c25s004_015h" , "d") from _call_BlinkXPS3_2275
    if persistent.family:
        sai "No lo creo. [mar] me ha dicho que los antojos son una tontería para explotar a los pobres padres, y que ella no tuvo cuando estuvo embarazada."
    else:
        sai "No lo creo. Siempre he pensado que los antojos son una tontería para explotar a los pobres padres."
    sai "Pero es posible... ahora que lo dices, suena asqueroso."
    mc "¿Quieres que vaya a comprar pepinillos?"
    call BlinkXPS3 ("c25s004_020h" , "d") from _call_BlinkXPS3_2276
    sai "Si no te importa... Pese a que suena asqueroso, me siguen apeteciendo."
    mc "No te preocupes, ahora voy a comprarlos."
    call KissXPS3 ("c25s004_025h" , "d") from _call_KissXPS3_50
    sai "Gracias, mi amor."
    call BlinkXPS3 ("c25s004_030h" , "d") from _call_BlinkXPS3_2277
    sai "¿Puedes pasar a buscar a [mad.nick] también? Así le ahorras tener que coger un Under para venir a comer."
    mc "Ningún problema. ¿La avisas tú de que voy a por ella?"
    return
label c25s004_EilPickles:
    $ whoPickles = eil
    scene c25s004_005i with fade
    "Llegas a la cocina y ves a [eil] con la cabeza metida en la nevera."
    mc "¿Estás buscando algo para comer antes de la hora de la comida?"
    call BlinkXPS3 ("c25s004_010i" , "d") from _call_BlinkXPS3_2278
    eil "Me han apetecido pepinillos con helado de chocolate, pero no nos quedan pepinillos."
    mc "¡Aargh! *Risa* ¡Eso tiene que tener un gusto horrendo! No te he visto nunca comer algo así."
    mc "¿Es posible que sea un antojo del embarazo?"
    call BlinkXPS3 ("c25s004_015i" , "d") from _call_BlinkXPS3_2279
    eil "No lo creo. Mi madre siempre ha dicho que los antojos son una tontería para explotar a los pobres padres, y que ella no tuvo cuando estuvo embarazada."
    eil "Pero es posible... ahora que lo dices, suena asqueroso."
    mc "¿Quieres que vaya a comprar pepinillos?"
    call BlinkXPS3 ("c25s004_020i" , "d") from _call_BlinkXPS3_2280
    eil "Si no te importa... Pese a que suena asqueroso, me siguen apeteciendo."
    mc "No te preocupes, ahora voy a comprarlos."
    call KissXPS3 ("c25s004_025i" , "d") from _call_KissXPS3_51
    eil "Gracias, mi amor."
    call BlinkXPS3 ("c25s004_030i" , "d") from _call_BlinkXPS3_2281
    eil "¿Puedes pasar a buscar a [mad.nick] también? Así le ahorras tener que coger un Under para venir a comer."
    mc "Ningún problema. ¿La avisas tú de que voy a por ella?"
    return
label c25s004_SamPickles:
    $ whoPickles = sam
    scene c25s004_005j with fade
    "Llegas a la cocina y ves a [sam] con la cabeza metida en la nevera."
    mc "¿Estás buscando algo para comer antes de la hora de la comida?"
    call BlinkXPS3 ("c25s004_010j" , "d") from _call_BlinkXPS3_2282
    sam "Me han apetecido pepinillos con helado de chocolate, pero no nos quedan pepinillos."
    mc "¡Aargh! *Risa* ¡Eso tiene que tener un gusto horrendo! No te he visto nunca comer algo así."
    mc "¿Es posible que sea un antojo del embarazo?"
    call BlinkXPS3 ("c25s004_015j" , "d") from _call_BlinkXPS3_2283
    sam "No lo creo. Siempre he pensado que los antojos son una tontería para explotar a los pobres padres. Yo no tuve en ninguno de mis embarazos."
    sam "Pero es posible... ahora que lo dices, suena asqueroso."
    mc "¿Quieres que vaya a comprar pepinillos?"
    call BlinkXPS3 ("c25s004_020j" , "d") from _call_BlinkXPS3_2284
    sam "Si no te importa... Pese a que suena asqueroso, me siguen apeteciendo."
    mc "No te preocupes, ahora voy a comprarlos."
    call KissXPS3 ("c25s004_025j" , "d") from _call_KissXPS3_52
    sam "Gracias, mi amor."
    call BlinkXPS3 ("c25s004_030j" , "d") from _call_BlinkXPS3_2285
    sam "¿Puedes pasar a buscar a [mad.nick] también? Así le ahorras tener que coger un Under para venir a comer."
    mc "Ningún problema. ¿La avisas tú de que voy a por ella?"
    return
label c25s004_OmaPickles:
    $ whoPickles = oma
    scene c25s004_005k with fade
    "Llegas a la cocina y ves a [oma] con la cabeza metida en la nevera."
    mc "¿Estás buscando algo para comer antes de la hora de la comida?"
    call BlinkXPS3 ("c25s004_010k" , "d") from _call_BlinkXPS3_2286
    oma "Me han apetecido pepinillos con helado de chocolate, pero no nos quedan pepinillos."
    mc "¡Aargh! *Risa* ¡Eso tiene que tener un gusto horrendo! No te he visto nunca comer algo así."
    mc "¿Es posible que sea un antojo del embarazo?"
    call BlinkXPS3 ("c25s004_015k" , "d") from _call_BlinkXPS3_2287
    oma "No lo creo. [kia] me ha dicho que los antojos son una tontería para explotar a los pobres padres, y que ella no tuvo cuando estuvo embarazada."
    oma "Pero es posible... ahora que lo dices, suena asqueroso."
    mc "¿Quieres que vaya a comprar pepinillos?"
    call BlinkXPS3 ("c25s004_020k" , "d") from _call_BlinkXPS3_2288
    oma "Si no te importa... Pese a que suena asqueroso, me siguen apeteciendo."
    mc "No te preocupes, ahora voy a comprarlos."
    call KissXPS3 ("c25s004_025k" , "d") from _call_KissXPS3_53
    oma "Gracias, mi amor."
    call BlinkXPS3 ("c25s004_030k" , "d") from _call_BlinkXPS3_2289
    oma "¿Puedes pasar a buscar a [mad.nick] también? Así le ahorras tener que coger un Under para venir a comer."
    mc "Ningún problema. ¿La avisas tú de que voy a por ella?"
    return

    call eoc from _call_eoc24
label c25s004_GetMad:
    if _in_replay:
        menu:
            "¿Has ido a comprar pepinillos o pollo?"
            "Pepinillos":
                $ pickles = True
            "Pollo":
                $ pickles = False
        call mrS3_mad_route from _call_mrS3_mad_route_3
        if not mad._var("route"):
            $ mad._var("pregnant", False)
    scene drive_day with fade
    if pickles:
        "Conduces hasta la tienda y compras los pepinillos. También compras una lata de atún para el pequeño dictador."
        "Empiezas a estar un poco preocupado por si los antojos son reales."
    else:
        "Conduces hasta la tienda y compras el pollo que te ha pedido [mar]. También compras una lata de atún para el pequeño dictador."
    call BlinkXPS3 ("c25s004_035a" , "d") from _call_BlinkXPS3_2290
    play music ("music/MorningFunnyBeat.ogg")
    "Una vez hechas las compras, vas a casa de [mad.nick]."
    mc "Buenos días, [mad.nick]. ¿Estás lista para irnos?"
    mad "Aún no, tengo que hacer algunas cosas."
    if mad._var("route"):
        scene c25s004_035d with dissolve
        "La preciosa modista te besa apasionadamente. Hace demasiado tiempo que no habéis estado a solas."
        call BlinkXPS3 ("c25s004_035a" , "d") from _call_BlinkXPS3_2291
        mad "*Risita* Una cosa menos que hacer."
        if mad._var("pregnant"):
            call BlinkXPS3 ("c25s004_035b" , "d") from _call_BlinkXPS3_2292
            mad "Estaba a punto de prepararme unos pepinillos con helado de pistacho cuando has llegado, creía que ibas a tardar más. ¿Quieres?"
            if pickles:
                mc "No sé lo que os ha dado hoy con los pepinillos, pero no, gracias. Suena bastante asqueroso."
            else:
                mc "No, gracias. Suena bastante asqueroso."
            mad "Entonces, dame un momento para prepararle la comida a Zeus y nos podemos ir."
    if not mad._var("pregnant"):
        mad "Dame un momento para prepararle la comida a Zeus y nos podemos ir."
    scene c25s004_040a with dissolve
    $ zeu = TGCharacter ("Zeus", color = "#0023ff")
    $ cat = TGCharacter (_("Jodido Gato"), color = "#0023ff")
    zeu "*¿Miau?* (¿He oído algo sobre comida?)" id c25s004_GetMad_de9248c8
    scene c25s004_040b with dissolve
    zeu "*¡Miau!* *Miau...* (¡Otra vez tú! Pero esta vez hueles a lata de atún... lata de atún cerrada...)" id c25s004_GetMad_6bd709cd
    mc "Hola, Pequeñajo. ¿Me has echado de menos?"
    scene c25s004_040c with dissolve
    zeu "*¿Miau?* *¡Miau!* (¿Pequeñajo? ¡Para ti, es Lord Simba!)" id c25s004_GetMad_832eb124
    scene c25s004_040d with dissolve
    zeu "*Miau* *Purr* (Pero si me rascas así, puedes llamarme como quieras.)" id c25s004_GetMad_73bdd14d
    call BlinkXPS3 ("c25s004_045" , "d") from _call_BlinkXPS3_2293
    mad "Me encanta ver lo bien que se lleva contigo. *Risa* Más aún teniendo en cuenta que no le traes comida."
    mc "Le he comprado una lata de atún, pero me la he dejado en la camioneta."
    mc "Te iba a proponer que lo trajeras a casa, estoy seguro de que a las chicas les va a encantar conocerlo."
    scene c25s004_040e with dissolve
    zeu "*Miau* *Purr* (Normal, soy adorable... Especialmente una vez me coma esa lata que has olvidado.)" id c25s004_GetMad_2665f6a9
    call BlinkXPS3 ("c25s004_050" , "d") from _call_BlinkXPS3_2294
    mad "No sé, [mc]. Aunque contigo se lleve bien, no es muy sociable. No sé si arañará a alguna de las chicas."
    mc "Bueno, es tu gato. Tu lo conoces mejor que nadie."
    scene c25s004_040f with dissolve
    zeu "*Purr divertido* *¡Miau!* (*Risa* ¡Su gato! Estos humanos son tan graciosos... ¡Mascotas creyéndose los amos!)" id c25s004_GetMad_0a4d1a18
    mcp "(¿El gato se ha reido? Deben ser imaginaciones mías...)"
    call BlinkXPS3 ("c25s004_055" , "d") from _call_BlinkXPS3_2295
    mad "Zeus, ¿quieres venir a conocer a las chicas? ¿Te vas a portar bien? Seguro que hay comida para ti."
    mc "*Risa* Le hablas como si te entendiera."
    mad "Te sorprenderías de lo mucho que parece entender..."
    scene c25s004_040g with hpunch
    mc "¡Ostias! ¿Dónde ha ido?"
    mad "*Risa* Te he dicho que te sorprenderías."
    scene c25s004_040h with dissolve
    zeu "*¿Miau?* (¿Nos podemos ir a conocer a esas chicas que regalan comida?)" id c25s004_GetMad_70cbe712
    call BlinkXPS3 ("c25s004_060" , "d") from _call_BlinkXPS3_2296
    mad "*Risa* Ya está en la puerta esperando. No hay como decirle que hay comida en algún sitio."
    mad "Dame un momento para que coja el bolso y nos podemos ir. También tengo que coger otra cosa..."
    mc "*Risa* Te espero acariciando a Zeus."
    scene c25s004_040i with dissolve
    zeu "*¡Miau!* (¡Sí, caricias para Lord Simba!)" id c25s004_GetMad_b9015529
    scene drive_day with fade
    "Os ponéis en camino unos minutos después. Zeus se pasa todo el viaje con la cabeza dentro de la bolsa donde está la lata de atún."
    stop music fadeout (1.5)
    "Por suerte, no sabe abrirla... O es demasiado vago para hacerlo y está esperando que sus sirvientes humanos lo hagan por él."
    return
label c25s005_ZeusAtHome:
    if _in_replay:
        menu:
            "¿Has ido a comprar pepinillos o pollo?"
            "Pepinillos":
                $ pickles = True
            "Pollo":
                $ pickles = False
        if pickles:
            menu:
                "¿Para quién has ido a buscar los pepinillos?"
                "[oma]":
                    $ whoPickles = oma
                "[mar]":
                    $ whoPickles = mar
                "[emm]":
                    $ whoPickles = emm
                "[eri]":
                    $ whoPickles = eri
                "[dap]":
                    $ whoPickles = dap
                "[nor]":
                    $ whoPickles = nor
                "[sca]":
                    $ whoPickles = sca
                "[meg]":
                    $ whoPickles = meg
                "[sai]":
                    $ whoPickles = sai
                "[eil]":
                    $ whoPickles = eil
                "[sam]":
                    $ whoPickles = sam
        call mrS3_mad_route from _call_mrS3_mad_route_4
        if whoPickles == eri:
            $ eri._var("route", True)
        else:
            call mrS3_eri_route from _call_mrS3_eri_route_5
        if whoPickles == dap:
            $ dap._var("route", True)
        else:
            call mrS3_dap_route from _call_mrS3_dap_route_4
        if whoPickles == sca:
            $ sca._var("route", True)
        else:
            call mrS3_sca_route from _call_mrS3_sca_route_6
        call mrS3_kim_route from _call_mrS3_kim_route_2
        menu:
            "¿Vas a probar el helado de Meemaw?"
            "Sí.":
                $ mee._var("iceCream", True)
            "No.":
                $ mee._var("iceCream", False)
    call BlinkXPS3 ("c25s005_005" , "f") from _call_BlinkXPS3_2394
    if whoPickles == nor:
        "Al llegar a casa, vais directos a la cocina de [nor]."
        mc "Te dejo los pepinillos que me has pedido en la nevera."
        nor "Gracias, [mc]."
        nor "Hola, [mad.nick]."
    else:
        if not pickles:
            "Al llegar a casa, dejas el pollo que te ha pedido [mar] en la nevera y vais a la cocina de [nor]."
        else:
            "Al llegar a casa, dejas los pepinillos en la nevera, le mandas un mensaje a [whoPickles], y vais a la cocina de [nor]."
        nor "Hola, [mad.nick]. Hola de nuevo, [mc]."
    play music ("music/Happy-Sun.ogg")
    nor "¿Llevas un gato en la bolsa, [mad.nick]?"
    call BlinkXPS3 ("c25s005_010" , "d") from _call_BlinkXPS3_2395
    mad "Hola, [nor]. *Risa* Sí, es Zeus. Creo que está intentando abrir la lata de atún que [mc] le ha comprado."
    mc "Es un pequeño glotón. Te lo ganarás si le das comida."
    scene c25s005_015a with dissolve
    zeu "*Miau* (¿He oído que esta señora reparte comida?)"
    mc "*Risa* A veces creo que nos entiende. Oye la palabra 'comida' y se olvida de lo que estaba haciendo."
    call BlinkXPS3 ("c25s005_020" , "d") from _call_BlinkXPS3_2396
    mad "¿Quieres que lo deje en algún sitio donde no moleste? Está bien educado, y no va a hacer sus cosas en el suelo ni a arañar los muebles."
    call BlinkXPS3 ("c25s005_025" , "d") from _call_BlinkXPS3_2397
    nor "Si está bien educado lo puedes dejar suelto. ¿Le puedo dar un trozo de salchicha?"
    scene c25s005_015b with dissolve
    zeu "*Miau* (Si dices que no, sé dónde duermes. Mi cola puede meterse en tu boca sin que yo pueda, o quiera, hacer nada por evitarlo.)"
    call BlinkXPS3 ("c25s005_030" , "d") from _call_BlinkXPS3_2398
    mad "Creo que no habrá ningún problema. Come de todo."
    mc "*Risa* Además, Zeus tendrá una nueva mejor amiga."
    mc "Dame la bolsa, [mad.nick], voy a guardar las cosas en la nevera."
    scene c25s005_015An1 with dissolve
    "El gato, como siempre, parece entender lo que estáis diciendo y salta ágilmente de la bolsa a la isla de la cocina."
    zeu "*Miau* (Tienes mi autorización para alimentarme, humana.)"
    call BlinkXPS3 ("c25s005_035" , "h") from _call_BlinkXPS3_2399
    mad "¡Zeus! ¡Baja de ahí ahora mismo! Acabo de decirles que estás bien educado."
    scene c25s005_015g with dissolve
    zeu "*Miau lastimero* (Pero el tipo feo le ha dicho a la Alimentadora Suprema que si hay comida por en medio me olvido de todo...)"
    call BlinkXPS3 ("c25s005_035" , "d") from _call_BlinkXPS3_2400
    mad "Zeeeeus..."
    scene c25s005_015h with dissolve
    zeu "*Miaaaau* (Vaaaaale.)"
    scene c25s005_015An2 with dissolve
    "Baja del mostrador tan ágilmente como ha subido, aunque por alguna razón te parece que lo hace con cara de pena."
    "Rodea la isla de la cocina para ir a los pies de [nor]."
    call BlinkXPS3 ("c25s005_040" , "d") from _call_BlinkXPS3_2401
    nor "Realmente lo has educado muy bien. Felicidades, [mad.nick]. Siempre he oído que los gatos son más difíciles de educar que los perros."
    mc "*Risa* A mí siempre me han parecido más listos que los perros."
    mc "Un perro es como un niño pequeño, siempre haciendo ruido, necesitando atención, y emocionándose por todo."
    mc "Un gato es como un jubilado. *Risa* Se deja alimentar y sólo te presta atención cuando a él le da la gana."
    scene c25s005_015m with dissolve
    zeu "*Miau* (Escuchad a este tío. Sabe de lo que habla.)"
    zeu "*Miau?* (¿Dónde está mi salchicha?)" id c25s005_ZeusAtHome_c30791f8
    scene c25s005_045a with dissolve
    nor "¿Quieres un trozo de salchicha, chiquitín?"
    zeu "*Miau* (¡Sí! ¡Alimenta a tu Señor!)"
    scene c25s005_015n with dissolve
    "La salchicha desaparece en un momento en la boca del felino."
    zeu "*Miau* (He puesto mi sagrada zarpa sobre ti. Ahora eres mía.)"
    call BlinkXPS3 ("c25s005_050" , "d") from _call_BlinkXPS3_2402
    nor "*Risa* Es super bonito. Y muy simpático."
    mc "*Risa* Mientras le des comida seguirá siendo simpático, no lo dudes."
    call BlinkXPS3 ("c25s005_055" , "d") from _call_BlinkXPS3_2403
    mad "[mc], ¿podrías enseñarle la casa a Zeus mientras yo ayudo a [nor] con la comida? Sobre todo, enséñale dónde están los lavabos."
    mc "Estás de broma, ¿no?"
    mad "No, le he enseñado a hacer sus cosas en el retrete. Hay que dejar la puerta abierta y la tapa levantada."
    call BlinkXPS3 ("c25s005_060" , "d") from _call_BlinkXPS3_2404
    nor "Eso lo he visto en varias películas y en videos de internet. Parece que es algo común. Cada vez más gente vive en apartamentos."
    mc "Vamos, Zeus. Voy a enseñarte la casa y a presentarte al resto de la familia."
    scene c25s005_060d with dissolve
    "Antes de que te dé tiempo de irte con el gato aparecen las dos primeras chicas nuevas. Al menos nuevas para Zeus."
    dap "¿Has traído a Zeus, [mad.nick]?"
    mad "Sí, [mc] me ha dicho que os gustaría conocerlo."
    eri "No se ha equivocado. Tanto oír hablar de él, ya tenía ganas de verlo."
    scene c25s005_015o with dissolve
    zeu "*Miau* (Vuestro color de pelo me confunde. Pero ahora sois mías.)"
    mad "Creo que le habéis caído bien."
    scene c25s005_015p with dissolve
    eri "¡Es precioso!"
    dap "¡Y se deja tocar por desconocidos! Me encanta."
    zeu "*Miau* (Rascad, esclavas, rascad.)"
    if dap._var("route"):
        call KissXPS3 ("c25s005_070" , "d") from _call_KissXPS3_54
        dap "Hola, [mc]. Nos tienes que explicar lo que pasó en el barco. [kim] nos ha explicado algo, pero hay partes que no sabe."
        mc "Luego os lo explico."
    if eri._var("route"):
        call KissXPS3 ("c25s005_065" , "d") from _call_KissXPS3_55
        eri "Hola, cielo. Antes, durante el yoga, has desaparecido antes de que te saludara."
        mc "Hola, preciosa."
    if eri._var("route") or dap._var("route"):
        if mad._var("route"):
            scene c25s005_015An3 with dissolve
            zeu "*Miau* (Me confundes. Creía que estabas con mi sirvienta...)"
            if eri._var("route") and dap._var("route"):
                zeu "*Miau* (¿Pero también estás con estas dos chicas? ¡Debes ser el equivalente a un semental humano!)"
            else:
                zeu "*Miau* (¿Pero también esta chica? ¡Debes ser el equivalente a un semental humano!)"
            mc "Sí, Zeus, voy a enseñarte la casa. No me metas prisa."
        elif eri._var("route") and dap._var("route"):
            scene c25s005_015An3 with dissolve
            zeu "*Miau* (¿Estás con las dos chicas? ¡Debes ser el equivalente a un semental humano!)"
            mc "Sí, Zeus, voy a enseñarte la casa. No me metas prisa."
    mc "Os veo luego. Vamos, Zeus."
    scene c25s005_075d with fade
    "La primera parada es la sala de estar, donde están [kat] y [kim]."
    mc "Hola, chicas. Traigo visita."
    call BlinkXPS3 ("c25s005_075" , "d") from _call_BlinkXPS3_2405
    kim "¡Qué bonito! Supongo que este debe de ser Zeus."
    zeu "*Miau* (¡Mi fama me precede! Me gustas. Una vez conocí a una gata con la piel como la tuya. Ella era más guapa. Y más peluda.)"
    scene c25s005_015s with dissolve
    zeu "*Miau* (Mía.)"
    call BlinkXPS3 ("c25s005_080" , "d") from _call_BlinkXPS3_2406
    kat "¡Es precioso!"
    zeu "*Miau* (Tú también eres mía. Tienes pinta de ser mullida para echarme una siesta encima tuyo. Me entra sueño sólo de pensarlo.)"
    mc "Chicas, os tengo que dejar. Voy a seguir enseñándole la casa."
    if kim._var("route"):
        call KissXPS3 ("c25s005_085" , "d") from _call_KissXPS3_56
        kim "Me encanta poder hacer esto ahora."
        mc "A mí también, cielo."
    scene c25s005_075e with dissolve
    kim "Hasta luego, [mc]. ¿Vendrás a la clase de tiro de [eva]?"
    mc "No, tuve suficiente con la de ayer y tengo algunas cosas que hacer."
    kat "Bueno, entonces seremos solo chicas y armas."
    scene c25s005_015t with fade
    "La siguiente parada es el baño de la planta baja, dónde nada más levantar la tapa del retrete, Zeus se sube a él."
    zeu "*¿Miau?* (¿Vas a quedarte ahí mirando?)" id c25s005_ZeusAtHome_89fd84b0
    "Por alguna razón te sientes raro mirando cómo el gato hace sus cosas."
    scene c25s005_015u with fade
    "Te giras hasta que acaba, para darle un poco de intimidad. No tienes ni idea de si los gatos necesitan intimidad."
    "No sabe tirar de la cadena en este retrete y lo haces tú."
    call BlinkXPS3 ("c25s005_090" , "f") from _call_BlinkXPS3_2407
    "Al llegar a la habitación de [dap]..."
    sca "Mira que gracioso. Ha ido en seguida a ver el cuadro que [mad.nick] hizo de él."
    zeu "*Miau* (Mia. Te nombro Protectora del Sagrado Retrato del Gato Inteligente.)"
    sca "De pequeña quería tener un gato, pero mi madre no me hubiera dejado nunca."
    zeu "*¿Miau?* *Miau* (¿Tener? Voy a tener que educarte. Está claro quién es el inteligente aquí.)" id c25s005_ZeusAtHome_13721b2f
    if sca._var("route"):
        call KissXPS3 ("c25s005_095" , "d") from _call_KissXPS3_57
    mc "Le podemos preguntar a [nor] si te dejaría tener uno."
    sca "No hace falta. Creo que Zeus va a venir mucho por casa."
    zeu "*Miau* (Depende. De momento sólo me han dado un trozo de salchicha.)"
    call BlinkXPS3 ("c25s005_100" , "d") from _call_BlinkXPS3_2408
    "Salta del armario y sube con curiosidad al regazo de [oma]."
    zeu "*Miau* (Por alguna razón huelo a algo peludo aquí, pero esta chica está perfectamente depilada. Bueno, ahora es mía.)"
    oma "Parece que tiene curiosidad por mí. *Risa* Los cachorros son tan monos..."
    mc "*Risa* Creo que le atraen las novedades. Vamos, Zeus. Te tengo que acabar de enseñar la casa."
    scene c25s005_015v with fade
    "Cuando os cruzáis con [bet] en la planta superior..."
    zeu "*Bufido* (No me caes bien. Me parece que eres una rival por la comida.)"
    call BlinkXPS3 ("c25s005_105" , "d") from _call_BlinkXPS3_2409
    bet "Parece que no le gusto."
    mc "Es extraño. Eres la primera con la que reacciona así."
    mc "A lo mejor ya está cansado de pasear por toda la casa."
    call BlinkXPS3 ("c25s005_110" , "d") from _call_BlinkXPS3_2410
    bet "Puedo llevármelo a la cocina y darle algo de comer si quieres."
    mc "*Risa* Creo que eso le va a hacer muy feliz."
    scene c25s005_015x with dissolve
    zeu "*Miau* (La había juzgado mal. Alguien como ella seguro que sabe dónde está la mejor comida. Ahora es mía.)"
    mc "*Risa* Creo que ya es tu amigo."
    bet "*Risa* Sí. Los gatos son tan básicos..."
    scene c25s005_115a with fade
    "Durante la comida, Zeus hace nuevas amigas."
    scene c25s005_115b with fade
    "Todas quieren darle de comer algo."
    scene c25s005_115c with fade
    "[mad.nick] da por perdida la batalla por que no se suba a los muebles. El resto de las chicas lo están empezando a malcriar."
    "Al menos está lo suficientemente bien educado como para no coger la comida directamente de los platos."
    "O es lo suficientemente vago como para esperar a que se la den."
    scene c25s005_115An with fade
    "Al único que no se acerca es a Jamaal. De todas formas ninguno de los dos iba a compartir su comida con el otro."
    scene c25s005_115f with fade
    "Supones que, si los gatos tienen un calendario, Zeus estará deseando que lleguen los domingos a partir de ahora."
    call BlinkXPS3 ("c25s005_120" , "f") from _call_BlinkXPS3_2411
    "Al acabar de comer..."
    mad "Chicas, creo que es el momento de darle nuestro regalo a [mc]. Ha llegado esta mañana."
    mc "¿Un regalo? ¿Para mí?"
    call BlinkXPS3 ("c25s005_125" , "d") from _call_BlinkXPS3_2412
    mad "Es una tontería que les propuse a algunas de las chicas el viernes y les pareció una buena idea."
    mad "La he mandado a imprimir y me la han entregado poco antes de que llegaras a mi apartamento."
    mc "Pero no es mi cumpleaños ni nada por el estilo..."
    scene c25s005_125d with dissolve
    nor "Pero te lo mereces más ahora que si lo fuese."
    bet "Estoy de acuerdo con [nor]. Ha sido una gran idea por parte de [mad.nick]."
    mc "Dame ese paquete, [mad.nick]." id c25s005_ZeusAtHome_e9575096
    scene c25s005_125e with dissolve
    mc "¡Oh! ¿Una camiseta?"
    mc "*Risa* ¿A quién se le ha ocurrido la frase?"
    eri "Fue cosa de [mad.nick]. Nos pareció muy graciosa."
    dap "Póntela. Queremos ver cómo te queda."
    scene c25s005_125f with fade
    mc "*Risa* ¡Me encanta!"
    mc "'Desafié a la Iglesia y lo único que conseguí fue esta camiseta y un finiquito para mi tía.'"
    mc "Bien hecho, [mad.nick]. Y gracias a todas."
    scene c25s005_125g with dissolve
    todas "*Risa* No hay de qué."
    lis "[mad.nick] es una artista con buenas ideas."
    mad "Chicas... me vais a hacer ruborizar."
    scene black with dissolve
    "Después de unas cuantas risas y de que todos consigáis que [mad.nick] se ruborice, vas a tu habitación."
    "Zeus vuelve a ser el centro de atención después de la pequeña interrupción por la camiseta."
    if pickles:
        "Ir a comprar los pepinillos no te ha dejado acabar lo que estabas haciendo con la contabilidad del Dormitorio."
    else:
        "Ir a comprar el pollo no te ha dejado acabar lo que estabas haciendo con la contabilidad del Dormitorio."
    if mee._var("iceCream"):
        "[nor] te dice que el helado no está listo todavía. Prepararlo con la leche de [mee] ha sido más lento de lo esperado."
    stop music fadeout (1.5)
    return
label c25s006_AmaCuddle:
    if _in_replay:
        call mrS3_ama_route from _call_mrS3_ama_route_9
        call mrS3_mar_route from _call_mrS3_mar_route_11
        call mrS3_nor_route from _call_mrS3_nor_route_6
        call mrS3_eri_route from _call_mrS3_eri_route_6
        call mrS3_dap_route from _call_mrS3_dap_route_5
        call mrS3_lis_route from _call_mrS3_lis_route_4
        call mrS3_sai_route from _call_mrS3_sai_route_6
        call mrS3_eva_route from _call_mrS3_eva_route_9
        call mrS3_kim_saved from _call_mrS3_kim_saved_1
    scene c25s006_005a with dissolve
    "Al cabo de un rato..."
    play sound ("music/knock.ogg")
    "*Knock-Knock*"
    play music ("music/From-Above.ogg")
    ama "*A través de la puerta* Soy yo, ¿puedo pasar?"
    mc "Sí, pasa."
    call BlinkXPS3 ("c25s006_010" , "d") from _call_BlinkXPS3_2413
    mc "¿Te has cansado ya del gato?"
    ama "*Risa* No, pero están todas ocupadas con él, con lo que sabía que estarías solo."
    mc "¿Quieres hablar de algo?"
    if ama._var("route"):
        call KissXPS3 ("c25s006_015" , "d") from _call_KissXPS3_58
        ama "Bueno, quería besarte. *Risita*"
        mc "Me parece una buena forma de empezar."
        call BlinkXPS3 ("c25s006_020" , "d") from _call_BlinkXPS3_2414
        ama "Y quería darte las gracias por lo que hiciste ayer en el barco."
    else:
        call BlinkXPS3 ("c25s006_020" , "d") from _call_BlinkXPS3_2415
        ama "Quería darte las gracias por lo que hiciste ayer en el barco."
    mc "Es lo menos que podía hacer. Me pasé la mitad del tiempo que estuve allí queriendo darle un puñetazo en la cara a Ichigo."
    call BlinkXPS3 ("c25s006_025" , "d") from _call_BlinkXPS3_2416
    ama "Siempre tienes que sacar el caballero de brillante armadura, ¿no?"
    if kim._var("saved"):
        mc "Anoche lo retuve bastante. Lo que me extraña es que Alejandra nos apoyara."
    else:
        mc "Anoche lo retuve bastante. Fuiste tú quien intervino con lo de [kim] cuando yo me quedé paralizado. Lo que me extraña es que Alejandra nos apoyara."
    scene c25s006_030a with dissolve
    ama "Alejandra estaba allí por negocios. Por suficiente dinero, o en su caso cuando no hay otra opción, se puede aceptar cualquier insulto."
    if not kim._var("saved"):
        ama "Y fue tu discurso junto con el apoyo de Alejandra lo que me permitió sacar a [kim] de allí."
        ama "De todas formas, que no reaccionaras tan rápido como yo, no significa que no lo fueras a hacer. O eso quiero pensar."
    mc "¿Dónde vas? ¿Se ha acabado el abrazo?"
    scene c25s006_030b with dissolve
    ama "No, pero quiero quitarme las botas para continuarlo en la cama, si no te importa."
    mc "*Risa* No me importa."
    if ama._var("route"):
        mc "¿Sólo las botas?"
        call BlinkXPS3 ("c25s006_035" , "d") from _call_BlinkXPS3_2417
        ama "*Risa* Sí, sólo las botas. No estás pensando que tengo segundas intenciones, ¿verdad? Tan solo quiero un abrazo muy largo."
        call BlinkXPS3 ("c25s006_040" , "d") from _call_BlinkXPS3_2418
        ama "Y si cae algún beso no voy a decir que no, pero ya está."
        mc "Abrazos y besos me sirve."
    call BlinkXPS3 ("c25s006_045" , "d") from _call_BlinkXPS3_2419
    ama "¿Vienes?"
    mc "Déjame quitarme las zapatillas."
    scene c25s006_050a with fade
    ama "Se está bien aquí."
    mc "¿Pasa algo, [ama]? Hoy estás más dulce de lo normal. No es que tenga ninguna queja, pero..."
    if eva._var("route"):
        mc "¿Tiene algo que ver que ayer tuviera la cita-entrenamiento con [eva]?"
        call BlinkXPS3 ("c25s006_055" , "d") from _call_BlinkXPS3_2420
        ama "No, me he alegrado mucho por ella. Por vosotros dos. Cuando llegué a la base, estaba exultante."
        ama "*Risa* Y si tuvieras alguna queja porque hoy estoy más dulce, te ibas a tener que aguantar."
    else:
        call BlinkXPS3 ("c25s006_055" , "d") from _call_BlinkXPS3_2421
        ama "*Risa* Si tuvieras alguna queja porque hoy estoy más dulce, te ibas a tener que aguantar."
    if ama._var("route"):
        ama "Tan solo quiero pasar un rato a solas con mi novio, sin hacer nada. No hemos tenido mucho tiempo desde... aquel beso. Siempre estamos hablando de trabajo."
    if not ama._var("route"):
        ama "Tan solo quiero pasar un rato a solas con mi hermano, sin hacer nada. No hemos tenido muchas oportunidades de pasar tiempo juntos si no era por trabajo."
        mc "Un día tenemos que ir tú y yo a comer, o a cenar. Nada en plan cita. Sólo tú y yo pasando un rato juntos."
    else:
        mc "Tenemos que tener tú y yo también una cita algún día."
    call BlinkXPS3 ("c25s006_060" , "d") from _call_BlinkXPS3_2422
    ama "Estaría bien, pero vas a estar muy ocupado antes de que vayamos a Aruba. Una vez allí te llevaré a mi restaurante favorito."
    mc "¿Vendrás tú conmigo? ¿[eva] se quedará aquí protegiendo a la familia?"
    call BlinkXPS3 ("c25s006_065" , "d") from _call_BlinkXPS3_2423
    ama "Aún no está preparada para ver a Gavin. Aún está muy afectada por lo que pasó, con que perdiera el brazo. Estaré yo contigo el primer mes."
    ama "Después iremos rotando, un mes cada una allí mientras la otra está aquí."
    mc "Me parece una buena idea. ¿Estará preparada dentro de un mes?"
    call BlinkXPS3 ("c25s006_070" , "d") from _call_BlinkXPS3_2424
    if not ama._var("route"):
        ama "Eso espero. No tengo ganas de estar lejos de las chicas más de ese tiempo."
    else:
        ama "Eso espero. Se va a tener que enfrentar a ese tema tarde o temprano."
    if eva._var("route"):
        ama "Y, después de lo de ayer, dudo que ella quiera estar lejos de ti más de un mes."
    mc "¿Cómo te sientes tú por tener que volver a Aruba?"
    call BlinkXPS3 ("c25s006_075a" , "d") from _call_BlinkXPS3_2425
    ama "Tengo sentimientos conflictivos. Quiero enseñarte dónde crecimos, pero hay sitios que me traerán recuerdos tristes."
    mc "Lo entiendo."
    call BlinkXPS3 ("c25s006_075b" , "d") from _call_BlinkXPS3_2426
    ama "Y descubrirás una parte... monstruosa de mí."
    mc "No creo que haya ninguna parte monstruosa en ti, [ama]. Te obligaron a hacer cosas monstruosas, pero no eres un monstruo."
    call BlinkXPS3 ("c25s006_075c" , "d") from _call_BlinkXPS3_2427
    ama "No me refiero a eso. Te enseñaré mi posesión más preciada, y a lo mejor entonces piensas que estoy mal de la cabeza."
    mc "¿Qué es?"
    call BlinkXPS3 ("c25s006_075d" , "d") from _call_BlinkXPS3_2428
    ama "No sé si decírtelo... no me corresponde sólo a mí."
    mc "No te preocupes. Ya llegará el momento de hacerlo."
    ama "Gracias..."
    mc "Como supongo que tiene que ver con [eva], ¿le has dicho que me lo enseñarás cuando estemos allí?"
    call BlinkXPS3 ("c25s006_075e" , "d") from _call_BlinkXPS3_2429
    ama "No, aún no... Me da un poco de miedo decírselo."
    mc "No le des más vueltas. Si es una cosa vuestra, obviamente me gustaría saberlo, pero habrá tiempo, siempre y cuando [eva] acepte contármelo."
    ama "Gracias. Para nosotras es muy especial. Para otras personas sería algo... macabro."
    if eva._var("route"):
        mc "Hablando de cosas especiales. ¿Qué tiene de especial el collar de [eva]?"
        scene c25s006_075ed with hpunch
        mc "Le he visto ese corazón puesto cada vez que ha hecho algo... nuevo, por decirlo de alguna forma."
        mc "La primera visita con la familia, lo de ayer, y alguna vez más."
        call BlinkXPS3 ("c25s006_075f" , "d") from _call_BlinkXPS3_2430
        ama "No te lo puedo decir, [mc]. Se lo deberías preguntar a ella..."
        mc "No te preocupes. Espero que no sea nada... ¿cómo has dicho? Ah, sí. Macabro."
        scene c25s006_075ed with hpunch
        pause (0.8)
        call BlinkXPS3 ("c25s006_075f" , "d") from _call_BlinkXPS3_2431
    mc "Cambiando de tema. ¿Hay alguien a quien quieras evitar en Aruba?"
    call BlinkXPS3 ("c25s006_075g" , "d") from _call_BlinkXPS3_2432
    ama "Especialmente a Daniels. Por su culpa murieron tres de mis hermanas y Arnau, el hermano de Aaron."
    mc "Lo entiendo. No tienes por qué verlo. Aaron y yo nos podemos ocupar de hacer lo que sea necesario."
    if not ama._var("route"):
        call BlinkXPS3 ("c25s006_075h" , "d") from _call_BlinkXPS3_2433
        ama "Gracias. ¿Por qué no te callas y me dejas disfrutar de este abrazo en paz? No quiero pensar en trabajo."
    else:
        call BlinkXPS3 ("c25s006_075h" , "d") from _call_BlinkXPS3_2434
        ama "Gracias. Sois muy parecidos y no me vais a dejar hacer nada que me haga daño."
        mc "En eso consiste protegerte, ¿no? Me encanta que, alguna vez, podamos ser otros los que te protegemos a ti."
        call BlinkXPS3 ("c25s006_080" , "d") from _call_BlinkXPS3_2435
        ama "*Risa* El caballero de brillante armadura ha vuelto."
        mc "*Risa* Ni siquiera me había dado cuenta."
        mc "Pero no querías que habláramos de trabajo..."
        call BlinkXPS3 ("c25s006_085" , "d") from _call_BlinkXPS3_2436
        ama "No, quería disfrutar de un abrazo en silencio. *Risa* Pero eso contigo es imposible."
        mc "*Risa* ¿Hablo demasiado?"
        ama "*Risa* La mayoría del tiempo."
        mc "*Risa* Déjame hacerte una última pregunta y me callaré."
        call BlinkXPS3 ("c25s006_090" , "d") from _call_BlinkXPS3_2437
        ama "*Risa* Me das miedo. Haz esa pregunta."
        mc "Dices que tengo que esperar a llegar a Aruba para una cita contigo. ¿Por qué no podemos ir a cenar mañana, por ejemplo?"
        call BlinkXPS3 ("c25s006_095" , "d") from _call_BlinkXPS3_2438
        ama "Porque no soy como [sai]."
        mc "¿A qué te refieres?"
        ama "Sabes que [sai] estuvo planificando vuestra primera vez juntos desde vuestra primera cita, ¿no?"
        mc "Sí, lo ha comentado varias veces. Siempre me pareció gracioso que se pasara una semana planeándolo para que fuera perfecto."
        mc "¿Quieres decir que no quieres planearlo?"
        call BlinkXPS3 ("c25s006_100" , "d") from _call_BlinkXPS3_2439
        ama "Quiero decir que no quiero pensar en ello. A diferencia de [sai], no considero el sexo importante."
        ama "Sé que para ti sí que lo es, pero yo me podría pasar los próximos meses haciendo solo esto, abrazándonos."
        scene c25s006_100d with dissolve
        ama "Y esto."
        call BlinkXPS3 ("c25s006_100" , "d") from _call_BlinkXPS3_2440
        ama "Estar así, abrazados, es suficiente para mí ahora mismo."
        mc "¿Y qué tiene eso que ver con que salgamos a cenar?"
        call BlinkXPS3 ("c25s006_105" , "d") from _call_BlinkXPS3_2441
        ama "*Risa* Si planificamos una salida a cenar, los dos sabemos qué pasará después."
        mc "Sólo pasará lo que tú quieras que pase, [ama]."
        call BlinkXPS3 ("c25s006_110" , "d") from _call_BlinkXPS3_2442
        ama "La diferencia es que, entonces, querré que pase."
        ama "Mientras nos veamos un ratito aquí, un ratito allá, sin planificar nada... no hay expectativas. Ni tiempo para que pase nada."
        mc "Pero es que no es necesario que pase nada. Abrazarte me encanta."
        call BlinkXPS3 ("c25s006_115" , "d") from _call_BlinkXPS3_2443
        ama "Pero tarde o temprano querrás sexo. No me malinterpretes. Lo entiendo."
        ama "Pero quiero que mi... nuestra primera vez sea especial. Estar preparada."
        mc "Espera. ¿Has dicho tu primera vez?"
        call BlinkXPS3 ("c25s006_120" , "d") from _call_BlinkXPS3_2444
        ama "Sí..."
        mc "Creía que a todas las espías os entrenaban para..."
        if eva._var("route"):
            mc "Me sorprendió con [eva], pero me la podía imaginar estrangulando al instructor que se lo propusiera."
        call BlinkXPS3 ("c25s006_125" , "d") from _call_BlinkXPS3_2445
        ama "*Risa* Eso solo pasa en las películas sobre el KGB. Yo no tuve que hacer la fase avanzada del entrenamiento de seducción." id c25s006_AmaCuddle_7be4a361
        call BlinkXPS3 ("c25s006_130" , "d") from _call_BlinkXPS3_2446
        ama "Claire, y Diana sí que lo hicieron."
        ama "Ni [eva] ni yo lo hicimos. Creyeron que nuestras habilidades encajaban mejor en otros campos."
        mc "Es decir, ¿voy a ser el primer chico con el que estés?"
        call BlinkXPS3 ("c25s006_135" , "d") from _call_BlinkXPS3_2447
        ama "Sí... Aparte de algún beso fingido en alguna operación..."
        ama "De hecho, eres el primer chico a quien he besado de verdad..."
        mc "Y tienes miedo, ¿no?"
        ama "Es imposible no tenerlo. Claire se volvió adicta al sexo. Diana lo odió cada minuto. ¿Qué me va a pasar a mí?"
        mc "Que tú lo vas a hacer voluntariamente."
        if eva._var("route"):
            call BlinkXPS3 ("c25s006_140" , "d") from _call_BlinkXPS3_2448
            ama "[eva] lo hizo voluntariamente ayer y ya está pensando en la próxima vez. ¿Le está pasando lo mismo que a Claire?"
            mc "No, [ama]. No es eso."
        call BlinkXPS3 ("c25s006_145" , "d") from _call_BlinkXPS3_2449
        ama "¿Y si no me gusta? ¿Y si no te gusta... conmigo?"
        mc "Ese puente lo cruzaremos cuando toque. Pero estoy dispuesto a tener una relación basada en abrazos, si es necesario."
        mc "Y en besos. Muchos besos. Y quiero uno ahora."
        call BlinkXPS3 ("c25s006_150" , "d") from _call_BlinkXPS3_2450
        ama "Eso puedo hacerlo... pero no quiero que pase de ahí ahora mismo."
        mc "Solo quiero un beso, nada más."
        scene c25s006_100d with dissolve
        "[ama] te da un dubitativo beso."
        "En el momento en que vuestros alientos se entremezclan, las dudas empiezan a desaparecer en la preciosa mujer."
        "Cuando el beso se empieza a convertir en apasionado, [ama] rompe el contacto de vuestros labios y vuelve a su posición sobre tu pecho."
        call BlinkXPS3 ("c25s006_155" , "d") from _call_BlinkXPS3_2451
        ama "¿Contento?"
        mc "Muy contento. No necesito nada más."
        ama "*Susurrando* Yo tampoco..."
    scene c25s006_160a with dissolve
    stop music fadeout (1.5)
    "Pasáis un rato abrazados, en silencio, disfrutando de la compañía del otro."
    scene c25s006_160b with fade
    play sound ("music/knock.ogg")
    "*Knock-Knock*"
    mar "*A través de la puerta* Somos [nor] y yo. ¿Podemos pasar?"
    play music ("music/Inspiring-Upbeat-Ambient.ogg")
    "La rubia mercenaria contesta antes de que puedas decir nada."
    ama "Sí, adelante."
    scene c25s006_165a with dissolve
    mar "¡Oh, [ama]! No sabíamos que estabas aquí."
    nor "Veníamos a preguntarle a [mc] si sabía dónde estabas."
    call BlinkXPS3 ("c25s006_170" , "d") from _call_BlinkXPS3_2452
    ama "Estábamos charlando y hemos acabado aquí. ¿Por qué no os unís?"
    mc "Un abrazo en familia. Estaría bien."
    scene c25s006_165b with dissolve
    nor "Me parece una gran idea."
    mar "¿No molestamos?"
    mc "Nunca molestáis. Dejad la puerta abierta por si viene alguien más."
    scene c25s006_165c with dissolve
    "Os acomodáis los cuatro como podéis en la cama."
    nor "*Risa* Podríamos instaurar esto como costumbre los domingos. Y añadir al resto de las chicas."
    mc "*Risa* Creo que entonces debería comprar una cama más grande."
    ama "Siempre lo podemos hacer en el césped, en el jardín de [nor]."
    mom "*Risa* Creo que no me molestaría tener que lavar manchas verdes si es por un abrazo de familia."
    scene c25s006_175a with fade
    "Al cabo de un rato..."
    dap "¿Qué pasa aquí? ¿Reparto de abrazos?"
    eri "¿Hay sitio para dos más?"
    mc "Si encontráis dónde acomodaros, sois bienvenidas."
    scene c25s006_175b with fade
    "La logística de cuerpos, brazos, y piernas se vuelve más complicada, pero conseguís encontrar una posición cómoda para todos."
    "Las risas suben de volumen junto a las quejas por un codo o una rodilla que se le clava a alguien, o de alguien a quien se le mete el pelo de otro alguien en la boca."
    scene c25s006_175c with fade
    lis "*Risa* ¿Qué hacéis todos ahí arremolinados?"
    sai "*Risa* ¡Se escuchan las risas desde mi habitación!"
    mc "Si queréis uniros a las risas y al remolino, buscad un sitio."
    scene c25s006_175d with fade
    "Las nuevas chicas se unen al abrazo colectivo."
    "Te sientes aprisionado, chafado, apretujado... pero contento de cómo ha acabado la comida familiar."
    "Las risas siguen subiendo de volumen."
    scene c25s006_175e with fade
    zeu "*Miau* *¿Miau?* (Se han acabado el jamón y el atún. ¿Dónde hay más?)"
    scene c25s006_175d with dissolve
    mc "¿Ese es Zeus? ¿Cómo ha entrado en esta casa?"
    mom "*Risa* ¿Acaso hay algún otro gato en casa?"
    lis "*Risa* Depende de si [oma] se ha depilado desde la última vez."
    todas "*Risa*"
    scene c25s006_175f with dissolve
    zeu "*¡Miau!* (¡Esa es la voz de la chica que me ha dado bacon!)"
    scene c25s006_180An with dissolve
    "Zeus da un ágil salto que lo coloca encima de la cama, en uno de los pocos huecos no ocupados por el laberinto de piernas."
    scene c25s006_180e with hpunch
    "La cama cruje inesperadamente."
    scene c25s006_180f with vpunch
    play sound ("music/wood.ogg")
    "Antes de derrumbarse bajo el peso de ocho personas... y un gato."
    "Consigues evitar que [nor] se caiga de la cama, pero no puedes hacer lo mismo por [dap] o [sai]."
    scene c25s006_180g with fade
    ama "¿Estáis todos bien?"
    todas "Sí."
    mc "*Risa* ¡El puto gato se ha cargado la cama!"
    dap "*Risa* ¡No te metas con Zeus! ¡Él no tiene la culpa!"
    nor "*Risa* Técnicamente ha sido el último en subir. La gota que ha colmado el vaso."
    mom "*Risa* Creo que necesitarás una cama nueva."
    sai "*Risa* Aprovecha la oportunidad y compra una más grande."
    lis "*Risa* Una que vaya de pared a pared. Y que sea más resistente."
    eri "*Risa* Deberíamos ayudar a [mc] a recoger este desastre. Cuidado con las astillas."
    zeu "*¡Miau!* (¡Ya no fabrican las camas como antes!)"
    scene c25s006_180h with fade
    "Después de recoger las maderas rotas y poner el colchón en el suelo."
    mc "Creo que ya está todo."
    if eri._var("route"):
        call KissXPS3 ("c25s006_185" , "d") from _call_KissXPS3_59
    else:
        scene c25s006_185a with dissolve
    eri "Yo voy a ir a trabajar antes de que se haga tarde."
    mc "OK, te veo luego."
    if ama._var("route"):
        call KissXPS3 ("c25s006_190" , "d") from _call_KissXPS3_60
    else:
        scene c25s006_190a with dissolve
    ama "Yo voy a llevar a las chicas a la galería de tiro. Dejaré a [eri] y a [eil] en el café."
    mc "¿También vas a colaborar en el entrenamiento?"
    ama "*Risa* Solo estaré allí para asegurarme de que [eva] no hace ninguna locura."
    if mar._var("route"):
        call KissXPS3 ("c25s006_200" , "d") from _call_KissXPS3_61
    else:
        scene c25s006_200a with dissolve
    mom "Yo también voy a ir con ellas. No caben todas en la furgoneta y hace años que no disparo."
    mc "Id con cuidado."
    if dap._var("route"):
        call KissXPS3 ("c25s006_205" , "d") from _call_KissXPS3_62
    else:
        scene c25s006_205a with dissolve
    dap "Mamá no quiere venir y no quiere armas en casa..."
    mc "Bueno, tenemos las de [eva]. No creo que sea necesaria ninguna más."
    if nor._var("route"):
        call KissXPS3 ("c25s006_210" , "d") from _call_KissXPS3_63
    else:
        scene c25s006_210a with dissolve
    nor "Eso mismo le dije hace un par de días."
    if sai._var("route"):
        call KissXPS3 ("c25s006_215" , "d") from _call_KissXPS3_64
    else:
        scene c25s006_215a with dissolve
    sai "A mí tampoco me gustaría que hubiera armas en casa, pero no por ello voy a dejar de aprender a disparar."
    mc "Me parece razonable, siempre va bien saber lo básico."
    if lis._var("route"):
        call KissXPS3 ("c25s006_220" , "d") from _call_KissXPS3_65
    else:
        scene c25s006_220a with dissolve
    lis "Yo he disparado con escopetas y rifles, cuando mi padre intentaba enseñarme a cazar. Fallaba a propósito."
    lis "Pero tengo ganas de aprender a disparar una pistola."
    if not lis._var("route"):
        mc "*Risa* No te imagino matando animales. Eso iría en contra de todo lo que defiendes."
    else:
        mc "*Risa* No te imagino matando animales, Princesa. Eso iría en contra de todo lo que defiendes."
    call BlinkXPS3 ("c25s006_225" , "d") from _call_BlinkXPS3_2453
    lis "No mataría un animal si no fuera para defender a un ser humano. *Risa* Soy ecologista, pero no idiota."
    lis "Y ahora nos vamos antes de que a [eri] y a [eil] se les haga tarde para ir a trabajar."
    scene c25s006_225d with fade
    "Después de que todas se pongan de nuevo sus zapatos..."
    todas "Hasta luego, [mc]."
    mc "Hasta luego, chicas. Pasadlo bien."
    scene c25s006_225e with dissolve
    zeu "*¿Miau?* (Ahora que se han ido, ¿me das atún?)"
    mc "¿Qué te parece si vamos a la cocina y miramos si ha quedado algo de pollo para darte?"
    zeu "*Miau* (Pollo me sirve. Veo que empiezas a entenderme.)"
    scene black  with dissolve
    "Pasas un rato en la cocina dando de comer al puto gato que te ha roto la cama."
    "A este paso, va a engordar hasta parecer un tigre."
    "Después de darle de comer al gato, compras una cama por internet. No hay camas de titanio anti-gatos."
    stop music fadeout (1.5)
    "Pero hay camas grandes. Muy grandes."
    return
label c25s007_iceCream:
    if _in_replay:
        call mrS3_mee_route from _call_mrS3_mee_route_5
    play music ("music/SneakySnitch.ogg")
    "Después de ducharte, pasas por la cocina de [nor]. Hay un helado de leche materna esperándote."
    scene c25s007_005a with dissolve
    "Coges una porción pequeña del cuenco de helado que [mee] te había indicado."
    scene c25s007_005b with dissolve
    mcp "(¡Está bueno! No hay mucha diferencia con el helado normal.)"
    mcp "(Ni siquiera el toque de Meemaw ha podido estropearlo.)"
    scene c25s007_005c with dissolve
    mcp "(No sé por qué esperaba algo diferente. Es leche al fin y al cabo.)"
    if mee._var("route") and persistent.lactation:
        mcp "(Estoy acostumbrado a beber su leche y, si dejamos de lado el morbo del fetiche, no deja de ser leche.)"
    if mee._var("route"):
        mcp "(Creo que es hora de ir a buscar a Meemaw para nuestra cena.)"
    else:
        scene black with dissolve
        "Decides volver a tu habitación. Después de todo el día trabajando en la contabilidad, tienes ganas de jugar un rato."
    stop music fadeout (1.5)
    return
label c25s007_MeeDate:
    scene c25s007_010a with fade
    "Llegas a la puerta de la habitación de [mee]. Por alguna razón estás nervioso por la cita que no es una cita... aún."
    play sound ("music/knock.ogg")
    "*Knock-Knock*"
    mc "Meemaw, soy yo. ¿Puedo pasar?"
    mee "*A través de la puerta* Sí, pasa."
    scene c25s007_010b with dissolve
    mee "Estoy al fondo..."
    mc "¿Estás preparada para nuestra cena?"
    scene c25s007_015d:
        yalign 1.0
        linear 5.0 yalign 0.0
    pause (5.0)
    call BlinkXPS3 ("c25s007_015" , "d") from _call_BlinkXPS3_2454
    mee "No he estado más preparada para una cena en mi vida."
    call addProfileImageS3 (1, "olivia_01", mee, _(": 15 - Especial"), "") from _call_addProfileImageS3_14
    mc "¡Wow, Meemaw!"
    return

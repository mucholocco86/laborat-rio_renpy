label c18:
    call c18s001_Dinner from _call_c18s001_Dinner
    call c18s001_Scarlett from _call_c18s001_Scarlett
    call c18s001_Eva from _call_c18s001_Eva
    call c18s001_Kate from _call_c18s001_Kate
    call c18s001_Emma from _call_c18s001_Emma
    call c18s001_Saira from _call_c18s001_Saira
    call c18s001_Erika from _call_c18s001_Erika
    call c18s001_Debbie from _call_c18s001_Debbie
    call c18s001_Amanda from _call_c18s001_Amanda
    call c18s001_Lisa from _call_c18s001_Lisa
    call c18s001_Daphne from _call_c18s001_Daphne
    call c18s001_Kim from _call_c18s001_Kim
    call c18s001_Common from _call_c18s001_Common
    if sai._var("route"):
        call c18s002_Saira from _call_c18s002_Saira
    else:
        call c18s002_NoSaira from _call_c18s002_NoSaira
    call c18s003_Sunday from _call_c18s003_Sunday
    if dap._var("route") or sca._var("route"):
        call c18s003_DaphScarPregnancyResults from _call_c18s003_DaphScarPregnancyResults
    call c18s004_Meemaw from _call_c18s004_Meemaw
    call c18s005_BirthdayOne from _call_c18s005_BirthdayOne
    return
label c18_updateprofiles:
    python:
        for characterProfile in [ bet, dap, deb, eil, emm, eri, kat, kia, kim, lis, mar, mee, nor, sai, sam, sca, sim, oma, eva, ama, mad, meg ]:
            while len (characterProfile.profileImages) > 0:
                characterProfile.profileImages.pop (0)
    python:
        for characterProfile in [ bet, dap, deb, eil, emm, eri, kat, kia, kim, lis, mar, mee, nor, sai, sam, sca, sim, oma, eva, ama, mad, meg ]:
            characterProfile.addProfileImage ("00-casual", False)
            characterProfile.addProfileImage ("01-date", False)
            characterProfile.addProfileImage ("02-swimsuit", False)
            characterProfile.addProfileImage ("03-sports", False)
            characterProfile.addProfileImage ("04-work", False)
            characterProfile.addProfileImage ("05-costume", False)
            characterProfile.addProfileImage ("06-dnd", False)
            characterProfile.addProfileImage ("07-lingerie", False)
            characterProfile.addProfileImage ("08-nude", False)
            characterProfile.addProfileImage ("09-pregnant", False)
            characterProfile.addProfileImage ("10-pregnantnude", False)
            characterProfile.addProfileImage ("11-special", False)
            characterProfile.addProfileImage ("11-special", False)
            characterProfile.addProfileImage ("11-special", False)
            characterProfile.addProfileImage ("11-special", False)
    $ mar.profileImages.pop (0) # first remove
    $ mar.profileImages.insert (0, ("martha_0", None)) # then add new
    $ mar.profileImages.pop (1) # first remove
    $ mar.profileImages.insert (1, ("martha_1", None)) # then add new
    $ mar.profileImages.pop (2) # first remove
    $ mar.profileImages.insert (2, ("martha_2", None)) # then add new
    $ mar.profileImages.pop (3) # first remove
    $ mar.profileImages.insert (3, ("martha_3", None)) # then add new
    $ mar.profileImages.pop (4) # first remove
    $ mar.profileImages.insert (4, ("martha_4", None)) # then add new
    $ mar.profileImages.pop (5) # first remove
    $ mar.profileImages.insert (5, ("martha_5", None)) # then add new
    $ mar.profileImages.pop (7) # first remove
    $ mar.profileImages.insert (7, ("martha_7", None)) # then add new
    $ mar.profileImages.pop (8) # first remove
    $ mar.profileImages.insert (8, ("martha_8", "route")) # then add new
    $ oma.profileImages.pop (0) # first remove
    $ oma.profileImages.insert (0, ("alexia_0", None)) # then add new
    $ oma.profileImages.pop (2) # first remove
    $ oma.profileImages.insert (2, ("alexia_2", None)) # then add new
    $ oma.profileImages.pop (3) # first remove
    $ oma.profileImages.insert (3, ("alexia_3", None)) # then add new
    $ oma.profileImages.pop (4) # first remove
    $ oma.profileImages.insert (4, ("alexia_4", None)) # then add new
    $ oma.profileImages.pop (8) # first remove
    $ oma.profileImages.insert (8, ("alexia_8", "route")) # then add new
    $ ama.profileImages.pop (1) # first remove
    $ ama.profileImages.insert (1, ("amanda_01", None)) # then add new
    $ ama.profileImages.pop (4) # first remove
    $ ama.profileImages.insert (4, ("amanda_4", None)) # then add new
    $ ama.profileImages.pop (11) # first remove
    $ ama.profileImages.insert (11, ("amanda_11", None)) # then add new
    $ bet.profileImages.pop (0) # first remove
    $ bet.profileImages.insert (0, ("betty_0", None)) # then add new
    $ bet.profileImages.pop (2) # first remove
    $ bet.profileImages.insert (2, ("betty_2", None)) # then add new
    $ bet.profileImages.pop (3) # first remove
    $ bet.profileImages.insert (3, ("betty_3", None)) # then add new
    $ bet.profileImages.pop (4) # first remove
    $ bet.profileImages.insert (4, ("betty_4", None)) # then add new
    $ dap.profileImages.pop (0) # first remove
    $ dap.profileImages.insert (0, ("daphne_0", None)) # then add new
    $ dap.profileImages.pop (1) # first remove
    $ dap.profileImages.insert (1, ("daphne_1", None)) # then add new
    $ dap.profileImages.pop (2) # first remove
    $ dap.profileImages.insert (2, ("daphne_2", None)) # then add new
    $ dap.profileImages.pop (3) # first remove
    $ dap.profileImages.insert (3, ("daphne_3", None)) # then add new
    $ dap.profileImages.pop (5) # first remove
    $ dap.profileImages.insert (5, ("daphne_5", None)) # then add new
    $ dap.profileImages.pop (7) # first remove
    $ dap.profileImages.insert (7, ("daphne_7", None)) # then add new
    $ dap.profileImages.pop (8) # first remove
    $ dap.profileImages.insert (8, ("daphne_8", "route")) # then add new
    $ dap.profileImages.pop (11) # first remove
    $ dap.profileImages.insert (11, ("daphne_11", "route")) # then add new
    $ deb.profileImages.pop (0) # first remove
    $ deb.profileImages.insert (0, ("deborah_0", None)) # then add new
    $ deb.profileImages.pop (1) # first remove
    $ deb.profileImages.insert (1, ("deborah_1", None)) # then add new
    $ deb.profileImages.pop (2) # first remove
    $ deb.profileImages.insert (2, ("deborah_2", None)) # then add new
    $ deb.profileImages.pop (3) # first remove
    $ deb.profileImages.insert (3, ("deborah_3", None)) # then add new
    $ eil.profileImages.pop (0) # first remove
    $ eil.profileImages.insert (0, ("eileen_0", None)) # then add new
    $ eil.profileImages.pop (2) # first remove
    $ eil.profileImages.insert (2, ("eileen_2", None)) # then add new
    $ eil.profileImages.pop (3) # first remove
    $ eil.profileImages.insert (3, ("eileen_3", None)) # then add new
    $ eil.profileImages.pop (4) # first remove
    $ eil.profileImages.insert (4, ("eileen_4", None)) # then add new
    $ eil.profileImages.pop (8) # first remove
    $ eil.profileImages.insert (8, ("eileen_8", "route")) # then add new
    $ emm.profileImages.pop (0) # first remove
    $ emm.profileImages.insert (0, ("emma_0", None)) # then add new
    $ emm.profileImages.pop (1) # first remove
    $ emm.profileImages.insert (1, ("emma_1", None)) # then add new
    $ emm.profileImages.pop (2) # first remove
    $ emm.profileImages.insert (2, ("emma_2", None)) # then add new
    $ emm.profileImages.pop (3) # first remove
    $ emm.profileImages.insert (3, ("emma_3", None)) # then add new
    $ emm.profileImages.pop (4) # first remove
    $ emm.profileImages.insert (4, ("emma_4", None)) # then add new
    $ emm.profileImages.pop (5) # first remove
    $ emm.profileImages.insert (5, ("emma_5", None)) # then add new
    $ emm.profileImages.pop (7) # first remove
    $ emm.profileImages.insert (7, ("emma_7", "route")) # then add new
    $ emm.profileImages.pop (8) # first remove
    $ emm.profileImages.insert (8, ("emma_8", "route")) # then add new
    $ eri.profileImages.pop (0) # first remove
    $ eri.profileImages.insert (0, ("erika_0", None)) # then add new
    $ eri.profileImages.pop (1) # first remove
    $ eri.profileImages.insert (1, ("erika_1", None)) # then add new
    $ eri.profileImages.pop (2) # first remove
    $ eri.profileImages.insert (2, ("erika_2", None)) # then add new
    $ eri.profileImages.pop (3) # first remove
    $ eri.profileImages.insert (3, ("erika_3", None)) # then add new
    $ eri.profileImages.pop (4) # first remove
    $ eri.profileImages.insert (4, ("erika_4", None)) # then add new
    $ eri.profileImages.pop (5) # first remove
    $ eri.profileImages.insert (5, ("erika_5", None)) # then add new
    $ eri.profileImages.pop (8) # first remove
    $ eri.profileImages.insert (8, ("erika_8", "route")) # then add new
    $ eva.profileImages.pop (0) # first remove
    $ eva.profileImages.insert (0, ("eva_0", None)) # then add new
    $ eva.profileImages.pop (2) # first remove
    $ eva.profileImages.insert (2, ("eva_2", None)) # then add new
    $ eva.profileImages.pop (4) # first remove
    $ eva.profileImages.insert (4, ("eva_4", None)) # then add new
    $ kat.profileImages.pop (0) # first remove
    $ kat.profileImages.insert (0, ("kate_0", None)) # then add new
    $ kat.profileImages.pop (2) # first remove
    $ kat.profileImages.insert (2, ("kate_2", None)) # then add new
    $ kia.profileImages.pop (0) # first remove
    $ kia.profileImages.insert (0, ("kiara_0", None)) # then add new
    $ kia.profileImages.pop (2) # first remove
    $ kia.profileImages.insert (2, ("kiara_2", None)) # then add new
    $ kia.profileImages.pop (4) # first remove
    $ kia.profileImages.insert (4, ("kiara_4", None)) # then add new
    $ kim.profileImages.pop (0) # first remove
    $ kim.profileImages.insert (0, ("kim_0", None)) # then add new
    $ kim.profileImages.pop (2) # first remove
    $ kim.profileImages.insert (2, ("kim_2", None)) # then add new
    $ kim.profileImages.pop (3) # first remove
    $ kim.profileImages.insert (3, ("kim_3", None)) # then add new
    $ lis.profileImages.pop (0) # first remove
    $ lis.profileImages.insert (0, ("lisa_0", None)) # then add new
    $ lis.profileImages.pop (2) # first remove
    $ lis.profileImages.insert (2, ("lisa_2", None)) # then add new
    $ mad.profileImages.pop (0) # first remove
    $ mad.profileImages.insert (0, ("maddie_0", None)) # then add new
    $ mad.profileImages.pop (8) # first remove
    $ mad.profileImages.insert (8, ("maddie_8", "route")) # then add new
    $ meg.profileImages.pop (0) # first remove
    $ meg.profileImages.insert (0, ("megan_0", None)) # then add new
    $ meg.profileImages.pop (2) # first remove
    $ meg.profileImages.insert (2, ("megan_2", None)) # then add new
    $ meg.profileImages.pop (4) # first remove
    $ meg.profileImages.insert (4, ("megan_4", None)) # then add new
    $ meg.profileImages.pop (8) # first remove
    $ meg.profileImages.insert (8, ("megan_8", "route")) # then add new
    $ nor.profileImages.pop (0) # first remove
    $ nor.profileImages.insert (0, ("norah_0", None)) # then add new
    $ nor.profileImages.pop (1) # first remove
    $ nor.profileImages.insert (1, ("norah_1", None)) # then add new
    $ nor.profileImages.pop (2) # first remove
    $ nor.profileImages.insert (2, ("norah_2", None)) # then add new
    $ nor.profileImages.pop (3) # first remove
    $ nor.profileImages.insert (3, ("norah_3", None)) # then add new
    $ nor.profileImages.pop (4) # first remove
    $ nor.profileImages.insert (4, ("norah_4", None)) # then add new
    $ nor.profileImages.pop (5) # first remove
    $ nor.profileImages.insert (5, ("norah_5", None)) # then add new
    $ nor.profileImages.pop (7) # first remove
    $ nor.profileImages.insert (7, ("norah_7", None)) # then add new
    $ nor.profileImages.pop (8) # first remove
    $ nor.profileImages.insert (8, ("norah_8", "route")) # then add new
    $ mee.profileImages.pop (0) # first remove
    $ mee.profileImages.insert (0, ("olivia_0", None)) # then add new
    $ mee.profileImages.pop (1) # first remove
    $ mee.profileImages.insert (1, ("olivia_1", None)) # then add new
    $ mee.profileImages.pop (2) # first remove
    $ mee.profileImages.insert (2, ("olivia_2", None)) # then add new
    $ sai.profileImages.pop (0) # first remove
    $ sai.profileImages.insert (0, ("saira_0", None)) # then add new
    $ sai.profileImages.pop (1) # first remove
    $ sai.profileImages.insert (1, ("saira_1", None)) # then add new
    $ sai.profileImages.pop (2) # first remove
    $ sai.profileImages.insert (2, ("saira_2", None)) # then add new
    $ sai.profileImages.pop (8) # first remove
    $ sai.profileImages.insert (8, ("saira_8", None)) # then add new
    $ sam.profileImages.pop (0) # first remove
    $ sam.profileImages.insert (0, ("samantha_0", None)) # then add new
    $ sam.profileImages.pop (1) # first remove
    $ sam.profileImages.insert (1, ("samantha_1", None)) # then add new
    $ sam.profileImages.pop (2) # first remove
    $ sam.profileImages.insert (2, ("samantha_2", None)) # then add new
    $ sam.profileImages.pop (4) # first remove
    $ sam.profileImages.insert (4, ("samantha_4", None)) # then add new
    $ sam.profileImages.pop (7) # first remove
    $ sam.profileImages.insert (7, ("samantha_7", "route")) # then add new
    $ sam.profileImages.pop (8) # first remove
    $ sam.profileImages.insert (8, ("samantha_8", "route")) # then add new
    $ sca.profileImages.pop (0) # first remove
    $ sca.profileImages.insert (0, ("scarlett_0", None)) # then add new
    $ sca.profileImages.pop (1) # first remove
    $ sca.profileImages.insert (1, ("scarlett_1", None)) # then add new
    $ sca.profileImages.pop (2) # first remove
    $ sca.profileImages.insert (2, ("scarlett_2", None)) # then add new
    $ sca.profileImages.pop (5) # first remove
    $ sca.profileImages.insert (5, ("scarlett_5", None)) # then add new
    $ sca.profileImages.pop (7) # first remove
    $ sca.profileImages.insert (7, ("scarlett_7", "route")) # then add new
    $ sca.profileImages.pop (8) # first remove
    $ sca.profileImages.insert (8, ("scarlett_8", "route")) # then add new
    $ sim.profileImages.pop (0) # first remove
    $ sim.profileImages.insert (0, ("simone_0", None)) # then add new
    $ sim.profileImages.pop (1) # first remove
    $ sim.profileImages.insert (1, ("simone_1", None)) # then add new
    $ sim.profileImages.pop (2) # first remove
    $ sim.profileImages.insert (2, ("simone_2", None)) # then add new
    $ sim.profileImages.pop (8) # first remove
    $ sim.profileImages.insert (8, ("simone_8", "route")) # then add new
    $ eva.profileImages.pop (11) # first remove
    $ eva.profileImages.insert (11, ("eva_11", None)) # then add new
    $ mad.profileImages.pop (7) # first remove
    $ mad.profileImages.insert (7, ("maddie_7", "route")) # then add new
    $ mad.profileImages.pop (11) # first remove
    $ mad.profileImages.insert (11, ("maddie_11", "route")) # then add new
    $ mad.profileImages.pop (12) # first remove
    $ mad.profileImages.insert (12, ("maddie_12", "route")) # then add new
    $ ama.profileImages.pop (0) # first remove
    $ ama.profileImages.insert (0, ("amanda_00", None)) # then add new
    $ kia.profileImages.pop (6) # first remove
    $ kia.profileImages.insert (6, ("kiara_6", None)) # then add new
    $ eva.profileImages.pop (1) # first remove
    $ eva.profileImages.insert (1, ("eva_1", None)) # then add new
    return
label c18s001_Dinner:
    if _in_replay:
        menu:
            "¿Descubriste que la persona que hablaba por teléfono durante tu comida con Eileen era Anthony?"
            "Sí":
                $ mc._var("knowsAnthony" , True)
            "No":
                $ mc._var("knowsAnthony" , False)
    if not _in_replay:
        call c18_updateprofiles from _call_c18_updateprofiles
    play music ("music/I-Can-Feel-it-Coming.ogg")
    scene c17s005_055b with dissolve
    "El beso continúa unos segundos más antes de que Eva se separe."
    call BlinkXP ("c18s001_005" , "d") from _call_BlinkXP_2430
    mc "¿Sigues comprobando si voy a cortar el beso por ser demasiado largo? *Risa*"
    eva "¿Yoooo? ¿Cómo puedes pensar eso de mí? *Risita*"
    mc "Porque es lo que haría [emm] *Risa*"
    call BlinkXP ("c18s001_010" , "d") from _call_BlinkXP_2431
    eva "Bueno... si Amanda puede darte besos largos, ¿por qué no voy a poder yo? ¿O para mí sí que hay una duración de besos marcada?"
    eva "¿Ya es tu favorita?"
    mcp "(¿Estoy detectando una corriente de celos soterrada?)"
    mc "Eva, no hay ninguna duración de los besos, pero ese no es el espíritu. Es un saludo, no una competición."
    call BlinkXP ("c18s001_015" , "d") from _call_BlinkXP_2432
    eva "Todo en este mundo es una competición, [mc]."
    eva "¿Nos vamos? No quiero llegar tarde en mi primera cena."
    mc "Vamos. Llegamos con el tiempo un poco justo."
    call BlinkXP ("c18s001_020" , "d") from _call_BlinkXP_2433
    eva "Si me dejas conducir a mí, llegaremos a tiempo. Yo no conduzco como una abuela."
    mc "Ni en broma. *Risa*"
    stop music fadeout (1.5)
    scene black with dissolve
    "Llegáis justo a tiempo. No conduces tan lento como Eva ha insinuado."
    scene c18s001_025An with dissolve
    play music ("music/Acoustic-Inspirational.ogg")
    "Las reacciones al ver entrar a Eva son de sorpresa absoluta."
    "Todas las chicas se han arreglado, pero ninguna ha llegado al nivel de Eva."
    scene c18s001_025a with dissolve
    kat "¡Joder! Ahora sí que parezco una zarrapastrosa. Creo que me voy a ir a llorar a mi habitación. *Risa*"
    sai "Todas lo parecemos. Eva, estás fantástica."
    emm "No está fantástica. {b}Es fantástica{/b}."
    mcp "(Lo cual te convierte en fantástica a ti, ¿no? *Risa mental*)"
    scene c18s001_025b with dissolve
    kim "Estás guapísima, Eva."
    ama "Te he dicho un vestido bonito, ¡no ESE vestido! Vamos a ir a bailar, no a una cena en una embajada."
    dap "No hagas caso, Eva. Vas a ser la sensación del... del sitio al que vamos a ir."
    kim "Desde luego que sí. Lo serías incluso en la embajada de la que habla Amanda. *Risa*"
    scene c18s001_025c with dissolve
    eri "Pues ya estamos casi todas."
    mom "Sí, en cuanto lleguen el resto podemos empezar a cenar."
    nor "¡Qué envidia me dais las jóvenes!"
    mc "¿Vosotras no os habéis arreglado?"
    call BlinkXP ("c18s001_030" , "d") from _call_BlinkXP_2434
    nor "No, hoy es un día para las chicas y para ti. Nosotras nos quedaremos en casa después de un par de días ajetreados."
    call BlinkXP ("c18s001_035" , "d") from _call_BlinkXP_2435
    mom "Yo aún tengo que acabar algunas cosas que quiero que reposen para la comida de mañana."
    call BlinkXP ("c18s001_040" , "d") from _call_BlinkXP_2436
    dap "Yo he intentado convencerlas, pero todas han puesto alguna excusa."
    call BlinkXP ("c18s001_045" , "d") from _call_BlinkXP_2437
    emm "Ya sabéis cómo es esto. Llegas a los 25 y ya no quieres salir a bailar."
    emm "Aunque quizás la edad no tiene que ver. Ni siquiera Alexia o Simone han querido venir. Mañana tienen que madrugar las dos."
    call BlinkXP ("c18s001_050" , "d") from _call_BlinkXP_2438
    dap "No es que no hayan querido. Lexi se ha pasado patrullando todo el día."
    mcp "(¿Lexi? Eso es nuevo.)"
    mc "Entonces, ¿quiénes vamos a ir a lo que sea que vayamos a ir?"
    call BlinkXP ("c18s001_055" , "d") from _call_BlinkXP_2439
    kat "Amanda, Eva, Kim, Debbie, Lisa, Saira, Erika, Daphne, Scarlett, Emma, yo y... y yo. A mí me cuento doble porque abulto por dos. *Risa*"
    kat "Eileen decidirá cuando acabe de trabajar, por si está muy cansada."
    mc "Somos doce o trece entonces. Necesitaremos los tres coches."
    call BlinkXP ("c18s001_060" , "d") from _call_BlinkXP_2440
    ama "Yo puedo conducir uno de los coches, si queréis."
    call BlinkXP ("c18s001_065" , "d") from _call_BlinkXP_2441
    eri "Yo conduciré el otro. Después de la última vez que salimos, hoy no pienso beber. *Risa*"
    call BlinkXP ("c18s001_070" , "d") from _call_BlinkXP_2442
    eva "A veces me alegra que viváis en California. En cualquier otro estado solo [mc] y Eileen podrían beber."
    eva "Suerte que Arnold cambió esa ley absurda. Os podéis alistar en el ejército y matar gente en nombre de vuestro país con 18 pero no beber hasta los 21."
    call BlinkXP ("c18s001_075" , "d") from _call_BlinkXP_2443
    ama "O conducir a los 16..."
    call BlinkXP ("c18s001_080" , "d") from _call_BlinkXP_2444
    kim "Hay muchas razones para eso, chicas..."
    scene c18s001_080An with dissolve
    "Empieza una conversación sobre las implicaciones de beber alcohol a diversas edades que se alarga durante la cena."
    "[emm] ve bien que dejen beber a los 18. Si eres responsable para votar, también lo debes ser para beber. Ella nunca votaría a un gobernador que quisiera quitarle ese derecho."
    "[eri] es un poco más ambivalente. Su última experiencia con el alcohol le hace ser más prudente."
    "[mar] y [nor], y más tarde Meemaw y Kiara, creen que devolver la edad para beber a los 21 sería lo correcto."
    "Ninguna de ellas pudo beber legalmente hasta los 21 y no creen que les haya perjudicado."
    "Eva y Amanda hablan de cuando estuvieron en una misión en Burkina Faso con 14 años y pudieron beber alcohol con normalidad."
    "Eva se emborrachó."
    "Pero lo consideran una buena experiencia que les permitió empezar a conocer sus límites."
    "Betty considera que 16 debería ser suficiente para empezar a beber cerveza y vino, y 18 para licores. Sus experiencias en África han moldeado sus opiniones."
    "El resto de las chicas no tienen una opinión muy estricta en esto. Ven ventajas y desventajas en las diferentes edades."
    "Cuando ya no queda comida en los platos, el Under de Megan llega para llevarla al trabajo."
    "Las diferentes conversaciones continúan durante poco menos de una hora más, hasta que llega Eileen, que dice estar muy cansada para ir a bailar."
    call BlinkXP ("c18s001_085" , "d") from _call_BlinkXP_2445
    sai "Nos deberíamos ir yendo o se hará muy tarde, ¿no?"
    mc "Cuando queráis. Pero me tendréis que decir dónde vamos, si tengo que conducir yo."
    call BlinkXP ("c18s001_090" , "d") from _call_BlinkXP_2446
    lis "Bueno, vamos a ir al Jazz Corner, donde trabaja Megan."
    mc "Ah, OK. Sé dónde está. ¿Y ese era todo el secretismo?"
    call BlinkXP ("c18s001_095" , "d") from _call_BlinkXP_2447
    dap "No es que fuera secretismo, es que queríamos atar un par de cosas antes de ir."
    dap "Nadie había reservado la sala anexa hoy, y Megan ha conseguido que nos la dejen para nosotros."
    dap "Si no hubiéramos podido cogerla, una mesa para doce o trece hubiera sido difícil de conseguir y hubiéramos ido al Twins."
    mc "Pero una sala para nosotros en un local así tiene que salir carísima, ¿no?"
    call BlinkXP ("c18s001_100" , "d") from _call_BlinkXP_2448
    emm "Son las ventajas de conocer a la cantante titular. *Risa* Nos la ha conseguido gratis, pero tendremos que ir a la barra de la sala principal a por las copas."
    mc "Traducción: [mc], te va a tocar ir a por las copas."
    call BlinkXP ("c18s001_105" , "d") from _call_BlinkXP_2449
    sca "¡Como siempre! *Risa* Pero ya te acompañaré yo, como la última vez."
    mc "Bueno, pues podemos irnos cuando queráis."
    scene c18s001_105d with fade
    "Os despedís de las mujeres que se quedan en casa y unos minutos después estáis en el Jazz Corner. Megan os acompaña a la sala anexa."
    "La sala es un poco más grande que la mitad de la sala principal y cuenta con su propio escenario y barra, aunque hoy no están en uso."
    "En el escenario hay una pantalla dónde proyectarán las actuaciones de Megan en la sala principal."
    menu:
        "¿Quieres ver a las chicas en sus trajes de fiesta?"
        "Sí":
            scene c18s001_amanda with dissolve:
                yalign 1.0
                linear 5.0 yalign 0.0
            "Amanda, con un vestido que le ha prestado [emm]. Ella había venido en shorts a casa."
            scene c18s001_daphne with dissolve:
                yalign 1.0
                linear 5.0 yalign 0.0
            "[dap], otra vez con el pelo suelto, como la noche del Twins."
            scene c18s001_debbie with dissolve:
                yalign 1.0
                linear 5.0 yalign 0.0
            "Debbie. Parece que les ha cogido el gusto a los tops."
            scene c18s001_emma with dissolve:
                yalign 1.0
                linear 5.0 yalign 0.0
            "[emm] con un vestido un poco osado que le ha prestado Kim."
            scene c18s001_erika with dissolve:
                yalign 1.0
                linear 5.0 yalign 0.0
            "[eri]. fiel a su estilo."
            scene c18s001_eva with dissolve:
                yalign 1.0
                linear 5.0 yalign 0.0
            "Eva. Simplemente alucinante."
            scene c18s001_kate with dissolve:
                yalign 1.0
                linear 5.0 yalign 0.0
            "Kate, un vestido cómodo y sencillo, en su línea."
            scene c18s001_kim with dissolve:
                yalign 1.0
                linear 5.0 yalign 0.0
            "Kim. Hablando de vestidos osados."
            scene c18s001_lisa with dissolve:
                yalign 1.0
                linear 5.0 yalign 0.0
            "Lisa, también manteniendo su estilo. Si el vestido fuera más largo podría ir a la ópera con él."
            scene c18s001_megan with dissolve:
                yalign 1.0
                linear 5.0 yalign 0.0
            "Megan. El vestuario que le eligen es espectacular."
            scene c18s001_saira with dissolve:
                yalign 1.0
                linear 5.0 yalign 0.0
            "Saira, extrañamente vestida de rojo."
            scene c18s001_scarlett with dissolve:
                yalign 1.0
                linear 5.0 yalign 0.0
            "Scarlett, con otro vestido prestado por Kim."
        "No":
            pass
    $ resetWalkthrough ()
    call BlinkXP ("c18s001_110a" , "d") from _call_BlinkXP_2450
    meg "Y esta es la sala. Por aquella puerta podéis pasar a la sala principal a pedir las bebidas. Acordaos del código para poder volver a entrar."
    meg "Por aquella otra puerta tenéis los lavabos privados de esta sala."
    meg "En esa pantalla veréis una versión gigante de mí. Por suerte sólo me cogen de cintura para arriba, con lo que los michelines no se ven mucho. *Risa*"
    call BlinkXP ("c18s001_115" , "d") from _call_BlinkXP_2451
    kat "¡Eres muy exagerada! Tú apenas tienes. *Risa* Yo necesitaría la pantalla gigante del Heins Stadium."
    mc "Nunca he conocido una mujer que no se queje de que le sobran un par de kilos. *Risa* O de que le falten."
    call BlinkXP ("c18s001_110b" , "d") from _call_BlinkXP_2452
    meg "Yo os tengo que dejar, tengo que acabar de aclarar unas cosas con el jefe antes de la actuación."
    meg "Volveré entre actuaciones. Os veo luego."
    todas "Hasta luego, Megan."
    call BlinkXP ("c18s001_120" , "f") from _call_BlinkXP_2453
    sca "Id pensando que queréis beber, ya me ocupo yo de tomar nota."
    "Scarlett toma nota en su móvil de las bebidas que quiere cada una y te da el móvil."
    scene c18s001_125a with fade
    sca "Lisa y yo vamos al lavabo y te vemos en la barra. ¿Puedes ir pidiendo?"
    lis "Viendo lo bonito que es el local tengo ganas de ver el lavabo. Este sitio tiene una imagen años 30 muy cuidada."
    mc "¿Vas a hacer turismo en el lavabo? *Risa*"
    scene c18s001_125b with dissolve
    lis "No solo turismo..."
    sca "*Risa* Esas cosas no se le preguntan a una dama, [mc]. *Risa*"
    mc "*Risa* No tardéis o empezará a fundirse el hielo."
    scene c18s001_125c with dissolve
    sca "No tardamos nada. No es que Lisa les vaya a dejar un regalito apestoso. *Risa*"
    lis "¡Scarlett! *Risa* Las señoritas no hacemos eso. Dejamos rosas y arcoíris. *Risa*"
    mc "Bueno, os espero en la barra. No voy a poder traer doce bebidas yo solo."
    call BlinkXP ("c18s001_130" , "d") from _call_BlinkXP_2454
    stop music fadeout (1.5)
    "En cuanto entras en la sala principal, te encuentras con una cara conocida."
    play music ("music/AmbientPianoStrings.ogg")
    mc "¿Dra. Milk?"
    call BlinkXP ("c18s001_135" , "d") from _call_BlinkXP_2455
    hm "¡Oh, Sr. Marks! Puede llamarme Harley cuando no estoy en el hospital."
    mc "Sólo si usted me llama [mc]."
    python:
        if "har" not in globals () or not isinstance (har, TGCharacter):
            har = TGCharacter ("Harley", color = "#ffffff")
    call BlinkXP ("c18s001_140" , "d") from _call_BlinkXP_2456
    har "De acuerdo, [mc]. ¿Qué tal los masajes con la Sra. Pitt?"
    mc "Bien, gracias. Hoy le he explicado a mi tía cómo hacerlos. Parece que han ido bien."
    mc "Un segundo, por favor."
    scene c18s001_140d with dissolve
    "Le entregas el móvil de Scarlett al camarero con la lista de las bebidas."
    mc "¿Puede prepararme esto, por favor?"
    python:
        if "bam" not in globals () or not isinstance (bam, TGCharacter):
            bam = TGCharacter ("Barman", color = "#0023ff")
    bam "Sí, ahora mismo."
    call BlinkXP ("c18s001_145" , "d") from _call_BlinkXP_2457
    har "¿Ha venido solo?"
    mc "No, con parte de la familia. ¿Y usted?"
    call BlinkXP ("c18s001_150" , "d") from _call_BlinkXP_2458
    har "Tampoco. He venido con mi marido, Jeff, y mi herm... ano."
    mc "Ahora veo las tres bebidas. ¿Quiere que le ayude a llevárselas a la mesa mientras preparan mi pedido?"
    call BlinkXP ("c18s001_155" , "d") from _call_BlinkXP_2459
    har "No hace falta. Mi hermano ha ido al lavabo un momento y tiene que estar a punto de volver."
    har "Oh, hablando del Rey de Roma, por ahí viene."
    scene c18s001_160a with dissolve
    python:
        if "ant" not in globals () or not isinstance (ant, TGCharacter):
            ant = TGCharacter ("Anthony", color = "#0023ff")
    har "[mc], te presento a mi hermano Anthony."
    ant "Ya nos conocemos, Harley. Es el casero de Lisa, del que te hablé."
    mc "Hola Anthony, ¿qué tal?"
    scene c18s001_160b with dissolve
    ant "Hola, [mc], ¿Ha venido Lisa contigo?"
    mc "Sí, ahora vendrá a ayudarme a llevar las copas."
    ant "Cuídala. Es una chica fantástica."
    mc "Sí que lo es."
    scene c18s001_160c with dissolve
    lis "Hola, Anthony."
    "Se suceden las presentaciones al llegar las chicas."
    "La interacción entre Lisa y Anthony se ve más amistosa de lo que podrías haber esperado tras lo que te explicó Lisa ayer."
    scene c18s001_160d with dissolve
    har "Yo voy a llevar las bebidas a la mesa. Jeff debe estar preguntándose por qué tardamos tanto."
    har "Anthony, si te quieres quedar con tus amigos, por nosotros no hay problema."
    ant "Bueno... creo que será lo mejor si me voy contigo. He venido con vosotros al fin y al cabo."
    mc "Si cambias de opinión, avisa a Lisa. Estamos en la sala privada y tendríamos que venir a buscarte."
    scene c18s001_160e with dissolve
    lis "Sí, hazlo. Vamos cortas de chicos con los que bailar y las chicas van a querer conocerte."
    lis "Les he hablado mucho de ti."
    sca "Y, antes de que preguntes, todo lo que ha dicho ha sido bueno."
    scene c18s001_160f with dissolve
    ant "Bueno, hoy quería pasar un rato con mi hermana y mi cuñado. Hacía mucho que no salíamos."
    har "Pero nosotros no estaremos mucho rato. Seguramente después de la primera actuación de Megan, la chica que canta, nos vayamos. Tiene una voz increíble."
    har "Con lo que os podemos prestar a Anthony después. *Risa* Así no se siente mal por habernos abandonado y pasa un rato con esas chicas que parecen tan ansiosas por conocerlo."
    ant "Bueno, ya veremos..."
    scene c18s001_160g with dissolve
    sca "No vas a dejar a once damiselas en apuros con sólo un caballero con el que bailar, ¿no?"
    lis "No te presionamos más. Tienes mi número. Mándame un mensaje o llámame si quieres venir. Me gustaría que lo hicieras."
    mc "Anthony, no estás obligado. Ven sólo si quieres. Pero espero verte luego."
    scene c18s001_160h with dissolve
    ant "Bueno, si Harley y Jeff deciden irse pronto, te aviso."
    lis "Espero tu mensaje."
    mcp "(Este abrazo es mucho más cálido que el que se dieron cuando aún estaban descubriendo si querían salir juntos o no.)"
    call BlinkXP ("c18s001_165" , "d") from _call_BlinkXP_2460
    har "Encantada de conoceros, chicas. Y de verte a ti otra vez, [mc]. Ahora nos tenemos que ir antes de que mi marido se preocupe."
    mc "Igualmente, Harley."
    call BlinkXP ("c18s001_170" , "d") from _call_BlinkXP_2461
    lis "¡Qué casualidad que la hermana de Anthony sea la médico de Olivia! Sabía que su hermana mayor era médico, pero esto es mucha casualidad."
    if mc._var("knowsAnthony"):
        mc "Y por curiosidad, tiene otra hermana, ¿verdad?"
        lis "¿Cómo lo sabes? Olga es un par de años más joven que Harley y un año mayor que Anthony. Es con quién más unido está."
        mc "Has dicho su hermana mayor. He intuido que debía haber una intermedia."
        lis "Se mudó a San Francisco hace un par de semanas, el mismo día que llegamos nosotras aquí. Antes vivía en Seattle."
    mc "El mundo es un pañuelo..."
    scene c18s001_175a with fade
    "Volvéis con las bebidas a la sala privada. La seguridad con que Scarlett lleva la bandeja contrasta con lo torpes que os sentís Lisa y tú."
    "Suena música suave para entrar en ambiente antes de que la actuación de Megan comience."
    scene c18s001_175b with fade
    sai "Un brindis por las chicas del cumpleaños."
    todas "¡Sí!"
    sai "¡Brindo porque este año os traiga mucha felicidad!"
    todas "¡Salud!"
    scene c18s001_175c with dissolve
    "Después de los brindis, todas empiezan a hablar con todas sobre los planes del próximo año."
    stop music fadeout (1.5)
    "Casi parece que sea el cumpleaños de todas."
    return
label c18s001_Scarlett:
    if _in_replay:
        menu:
            "¿Estás en una relación con Scarlett?"
            "Sí":
                $ sca._var("route" , True)
            "No":
                $ sca._var("route" , False)
    call BlinkXP ("c18s001_250" , "d") from _call_BlinkXP_2462
    play music ("music/You-Know-Instrumental.ogg")
    sca "¿Bailas? La última vez no pude bailar contigo por culpa de aquellos dos chicos."
    mc "¡Por supuesto!"
    call BlinkXP ("c18s001_255" , "d") from _call_BlinkXP_2463
    "Os separáis un poco del grupo de chicas, para poder hablar en privado mientras bailáis."
    sca "Están super emocionadas con lo de mañana."
    mc "Es normal. Siempre se han puesto así en sus cumpleaños. Me fastidia no haber podido estar en los tres últimos."
    call BlinkXP ("c18s001_260" , "d") from _call_BlinkXP_2464
    sca "No es eso. Desde lo que dijiste en la cena de ayer sobre Amanda formando parte de la familia, no hacen más que hablar de ello."
    mc "No creo que dijera nada que no pensáramos todos. Y vuestras respuestas lo confirmaron."
    call BlinkXP ("c18s001_265" , "d") from _call_BlinkXP_2465
    sca "Sí, tienes razón. Pero ninguna de nosotras lo había verbalizado previamente."
    sca "Todas nos sentíamos parte de la familia, pero decirlo en alto y saber lo que pensaban las demás... ¡Phew!"
    call BlinkXP ("c18s001_270" , "d") from _call_BlinkXP_2466
    sca "Mientras hablabas con Amanda fuera, nosotras nos quedamos mirándonos las unas a las otras."
    sca "Después vinieron un montón de abrazos. No era necesario decir nada. Lo habíamos dicho todas sobre Amanda."
    call BlinkXP ("c18s001_275" , "d") from _call_BlinkXP_2467
    sca "Y en ese momento todas fuimos Amanda."
    sca "A algunas de nosotras se nos escaparon algunas lágrimas."
    mc "Les tengo que pedir ese video a Amanda y a Eva. *Risa*"
    call BlinkXP ("c18s001_280" , "d") from _call_BlinkXP_2468
    sca "Puedes reírte si quieres, pero fue muy emocionante. Y después Olivia dijo que sólo a ti se te podría ocurrir ponernos en esa situación."
    sca "Y las caras de todas decían que pensaban que tenía razón."
    mc "*Risa* ¡La culpa es de [mc]!" #Blame [mc]
    call BlinkXP ("c18s001_285" , "d") from _call_BlinkXP_2469
    sca "*Risa* No estaban buscando culpables. Cada una de nosotras estaba contenta sintiéndose parte de algo sin hablarlo con el resto."
    sca "Gracias a ti, nos hemos dado cuenta de que el resto sienten lo mismo. Nadie te culpa. Todo el mundo te lo agradece."
    mc "Creo que te lo deberían agradecer a ti."
    call BlinkXP ("c18s001_290a" , "d") from _call_BlinkXP_2470
    sca "¿A mí? ¿Qué he hecho yo ahora?"
    mc "Proponer la Navidad en la playa. Este sentimiento empezó allí."
    call BlinkXP ("c18s001_290b" , "d") from _call_BlinkXP_2471
    sca "Pero yo solo quise proponer algo divertido..."
    mc "Y fue divertido. Pero estar todos juntos también creó este sentimiento. Es tan culpa tuya como mía."
    sca "No lo había visto así..."
    call BlinkXP ("c18s001_295" , "d") from _call_BlinkXP_2472
    sca "Pero cambiando de tema antes de que me ruborice... ¿Sabes que Eva y Amanda también usan lengua de signos?"
    mc "No, no lo sabía. Supongo que tiene que ser útil para ellas poderse comunicar en silencio."
    call BlinkXP ("c18s001_300" , "d") from _call_BlinkXP_2473
    sca "Supongo... no les entiendo la mayoría de lo que señalan, pero está claro que son gestos rápidos y deliberados."
    sca "No mires, pero están discutiendo por algo."
    scene c18s001_300An with dissolve # (def)
    sca "Son gestos enfadados, y ni siquiera se están mirando directamente."
    call BlinkXP ("c18s001_300" , "d") from _call_BlinkXP_2474
    sca "Deben usar un lenguaje diferente del ASL."
    mc "Bueno, se criaron en Aruba, no sé qué hablarán allí."
    play sound ("music/notification.ogg")
    "Suena un móvil en algún sitio."
    call BlinkXP ("c18s001_305" , "d") from _call_BlinkXP_2475
    sca "Se lo puedes preguntar a Eva. Viene hacia aquí, creo que se ha acabado nuestro baile."
    sca "Todas van a querer bailar contigo. Eres el único chico."
    mc "Bailamos luego otra vez. La noche es larga."
    if sca._var("route"):
        scene c18s001_310An with dissolve # abc
        "Scarlett te hace los gestos de \"Te Quiero\", pero lo hace diferente."
        mc "Eso se ha visto diferente de como lo hice yo."
        call BlinkXP ("c18s001_315" , "d") from _call_BlinkXP_2476
        sca "*Risita* Es que no lo hiciste bien del todo. Mira, el \"Yo\" se hace así."
        scene c18s001_310a with dissolve
        pause (1.0)
        call BlinkXP ("c18s001_315" , "d") from _call_BlinkXP_2477
        sca "Lo que tú hiciste se parece más a \"A mí\". Dijiste algo como \"A mí te quiero\"."
        mc "¿Por qué no me lo dijiste?"
        call BlinkXP ("c18s001_320" , "d") from _call_BlinkXP_2478
        sca "¿Y fastidiar el momento? ¡No!"
        sca "Te tomaste el esfuerzo y entendí lo que querías decir. Era suficiente para mí. Era el gesto más bonito que habían hecho nunca por mí."
        mc "Pero lo podía haber hecho mejor."
        call BlinkXP ("c18s001_325" , "d") from _call_BlinkXP_2479
        sca "No, mi amor. No podías."
    stop music fadeout (1.5)
    return
label c18s001_Eva:
    call BlinkXP ("c18s001_330" , "d") from _call_BlinkXP_2480
    eva "¿Interrumpo algo? ¿Puedo robarte a [mc] por una canción, Scarlett?"
    play music ("music/Bolero.ogg")
    call BlinkXP ("c18s001_335" , "d") from _call_BlinkXP_2481
    sca "No interrumpes. Precisamente le estaba diciendo que todas íbamos a querer bailar con él."
    sca "Pasáoslo bien."
    call BlinkXP ("c18s001_340" , "d") from _call_BlinkXP_2482
    eva "Gracias, Scarlett."
    sca "Lo que necesites, guapísima."
    call BlinkXP ("c18s001_345" , "d") from _call_BlinkXP_2483
    eva "Me encanta este sitio, pero tenías razón. Voy demasiado vestida para esto."
    mc "No creo. Ya te he dicho antes que estás preciosa. Puede que no sea una embajada, como ha dicho Amanda, pero si estás cómoda con ese vestido, nadie se va a quejar."
    mc "¿De qué estabais discutiendo? ¿Hay algún problema entre vosotras?"
    call BlinkXP ("c18s001_350" , "d") from _call_BlinkXP_2484
    eva "¿Cómo sabes que estábamos discutiendo? Creía que solo sabias unas pocas palabras en lengua de signos."
    mc "Me lo ha dicho Scarlett. No os entendía, pero por vuestros gestos dice que quedaba claro que era una discusión."
    call BlinkXP ("c18s001_355" , "d") from _call_BlinkXP_2485
    eva "Me estaba acusando de algo y... la cosa se ha calentado..."
    mc "¿Puedo saber de qué te estaba acusando? ¿O es algo entre vosotras?"
    call BlinkXP ("c18s001_360" , "d") from _call_BlinkXP_2486
    eva "Ningún problema. Se está comportando como una niña celosa. Me acusaba de haberme puesto este vestido para ti."
    eva "Como ella se ha tenido que poner uno de los vestidos de [emm]..."
    mc "¿Para mí? ¿Por qué?"
    mc "¿Tiene algo que ver con que ayer la acusaras de flirtear conmigo?"
    call BlinkXP ("c18s001_365" , "h") from _call_BlinkXP_2487
    eva "¡Chivata!"
    mc "Igual de chivata que tú ahora mismo, Eva. *Risa*"
    call BlinkXP ("c18s001_370" , "d") from _call_BlinkXP_2488
    eva "Tienes razón..."
    mc "Y... ¿realmente te lo has puesto para mí?"
    eva "Me lo he puesto porque quería estar guapa."
    call BlinkXP ("c18s001_375" , "d") from _call_BlinkXP_2489
    eva "Además, no tendría mucho sentido querer seducirte con un vestido si ya me has visto solo con las bragas... ¿no?"
    mc "*Risa* No me recuerdes ese día. No sabía que eras tú."
    mc "Pero creo que sabes poco de la mentalidad masculina. *Risa*"
    call BlinkXP ("c18s001_380" , "d") from _call_BlinkXP_2490
    eva "¿A qué te refieres? ¿No te gusta el vestido?"
    mc "Me encanta."
    mc "Me refiero a que la mayoría de los hombres prefieren ganarse el derecho a ver una chica desnuda. Un poco de coqueteo, que te dejen queriendo más..."
    mc "Si consiguen el premio sin esfuerzo, no le dan el valor que tiene. No digo que no lo valoren, pero no lo hacen lo suficiente."
    call BlinkXP ("c18s001_385" , "d") from _call_BlinkXP_2491
    eva "Mmmm... tomo nota. Es decir... si quiero algo con un chico... debería dejarle con ganas de más, ¿no?"
    mc "Sí, pero ve con cuidado. Si se lo haces muchas veces, puede pensar que eres una calienta pollas y perder el interés. Tienes que medir cuántas veces puedes o debes hacerlo."
    scene c18s001_385d with dissolve
    eva "OK. Primera vez."
    mc "¿Qué?"
    scene c18s001_385e with dissolve
    mc "*Risa*"
    mcp "(Tía Betty estaría orgullosa de mí ahora mismo. Esta vez no hace falta que le pregunte a Eva si el chico al que se refiere soy yo.)"
    mcp "(Y sí, me ha dejado con ganas de más. ¿Qué voy a hacer con esta chica?)"
    stop music fadeout (1.5)
    return
label c18s001_Kate:
    if _in_replay:
        menu:
            "¿Qué hiciste cuando Kate te contó sus problemas de azúcar en la sangre?"
            "Convencer a Kate para hacer más deporte y comer más sano.":
                $ kat._var("slim", True)
            "Convencer a Kate SOLO para hacer más deporte.":
                $ kat._var("slim", False)
    call BlinkXP ("c18s001_390" , "f") from _call_BlinkXP_2492
    "Te diriges a la mesa donde están las bebidas. Apenas has tenido tiempo de probar tu zumo de piña."
    play music ("music/PositiveWoman.ogg")
    mc "¿Qué tal, Kate? ¿No bailas?"
    kat "No puedo bailar mientras te odio. *Risa*"
    mc "¿Qué? ¿Por qué? ¿Qué he hecho yo ahora? ¿Puedo sentarme?"
    call BlinkXP ("c18s001_395" , "f") from _call_BlinkXP_2493
    kat "Convencerme para hacer más deporte. *Risa* Tengo agujetas en las agujetas."
    kat "Yoga a primera hora, después Debbie me ha tenido media mañana nadando. Ayer Kim me sacó a correr 30 minutos por la carretera."
    if kat._var("slim"):
        call BlinkXP ("c18s001_400" , "d") from _call_BlinkXP_2494
        kat "Y para ponerlo peor, me he tenido que retener de comer todas las cosas deliciosas que han preparado [mar] y [nor]."
        kat "Y tengo que beber un cocktail sin alcohol. ¡Puagh! ¡Necesito mi azúcar intravenoso!"
        mc "Comer saludable es bueno. [mar] y [nor] cocinan muy saludable, con lo que podrás comer de todo, pero quizás en menos cantidad de lo que lo hacías antes."
    mc "Piensa que es por tu bien. Y hacer deporte es bueno. Te dará más resistencia."
    call BlinkXP ("c18s001_405" , "d") from _call_BlinkXP_2495
    kat "Lo sé, y todas me están ayudando mucho, pero duermo en la tercera planta."
    kat "Ayer casi tuve que subir el último tramo de escaleras a gatas. Las piernas se quejaban a cada escalón."
    mc "No hace falta que te esfuerces demasiado. Es mejor hacer las cosas bien y poco a poco que quemarte."
    if persistent.walkthrough:
        $ wt1 = "Kate + 5"
        $ wt2 = _("Sin consecuencias.")
    else:
        $ wt1 = ""
        $ wt2 = ""
    menu:
        "Invitarla a subir corriendo al lago." (wt = wt1):
            $ kat.rp (5)
            mc "Cuando hayas cogido un poco de resistencia, te llevaré a un lago precioso que hay en las colinas. Ya verás como vale la pena."
            call BlinkXP ("c18s001_410" , "d") from _call_BlinkXP_2496
            kat "Oh, eso sería genial. Debbie y Kim me han dicho que es precioso."
        "No decir nada." (wt = wt2):
            kat "Kim me ha dicho de subir un día corriendo al lago. Cuando haya conseguido que dar dos pasos no duela."
            mc "Cuando subáis avisadme y me apunto si puedo."
            call BlinkXP ("c18s001_410" , "d") from _call_BlinkXP_2497
            kat "Kim ya me ha dicho que las llevaste a ella y a Debbie y que es precioso."
    $ resetWalkthrough ()
    kat "También has estado allí con Eileen y Alexia... y Eva..."
    call BlinkXP ("c18s001_415" , "d") from _call_BlinkXP_2498
    kat "*Risa* ¡Y todas han estado contigo allí!"
    kat "¿Es como tu terreno de caza particular? ¿El sitio donde llevas a las chicas para deslumbrarlas con la belleza del lugar?"
    mc "*Risa* No es eso, Kate."
    if persistent.walkthrough:
        $ wt1 = "Kate + 10"
        $ wt2 = _("Sin consecuencias.")
    else:
        $ wt1 = ""
        $ wt2 = ""
    menu:
        "Tirarle los trastos." (wt = wt1):
            $ kat.rp (10)
            mc "Pero si te llevase a ti, el deslumbrado sería el lago. Y sí, sé que suena cursi."
            call BlinkXP ("c18s001_420" , "d") from _call_BlinkXP_2499
            kat "Y ahora quieres que me ruborice otra vez con tus piropos cursis."
            mc "Ya te dije que, si querías, podía dejar de hacerlo."
            call BlinkXP ("c18s001_425" , "d") from _call_BlinkXP_2500
            kat "Y yo te dije ayer que no me molestan."
            mc "Por lo que yo recuerdo, dijiste que no me atreviera a dejar de hacerlo. *Risa*"
            kat "Es bonito que un chico me diga esas cosas de vez en cuando, aunque sea en broma."
            play sound ("music/notification.ogg")
            "Suena un móvil, pero ella lo ignora."
            mc "¿Quién ha dicho que sea en broma?"
            call BlinkXP ("c18s001_430" , "d") from _call_BlinkXP_2501
            kat "¿Qué? ¿Lo dices en serio?"
        "No decir nada." (wt = wt2):
            play sound ("music/notification.ogg")
            "Suena un móvil."
    $ resetWalkthrough ()
    call BlinkXP ("c18s001_435" , "d") from _call_BlinkXP_2502
    emm "Hola, chicos. Kate, ¿te molesta que me lleve a mi hermano para bailar con él?"
    call BlinkXP ("c18s001_440" , "d") from _call_BlinkXP_2503
    kat "No, para nada. Todo tuyo. Llévatelo o al final me va a convencer para ir a correr. *Risa*"
    stop music fadeout (1.5)
    mc "Te veo luego, Kate, y, si quieres, seguimos la conversación. *Risa*"
    return
label c18s001_Emma:
    if _in_replay:
        $ dap._var("route" , False)
        $ dap._var("romance" , False)
        $ eri._var("route" , False)
        $ mar._var("route" , False)
        menu:
            "¿Estás en una relación con [emm]?"
            "Sí":
                $ emm._var("route" , True)
                menu:
                    "¿Estás en una relación con [dap]?"
                    "Sí":
                        $ dap._var("route" , True)
                        menu:
                            "¿[dap] intentó corromperte con mentiras?"
                            "Sí":
                                $ dap._var("romance" , False)
                            "No":
                                $ dap._var("romance" , True)
                    "No":
                        $ dap._var("route" , False)
                menu:
                    "¿Estás en una relación con [eri]?"
                    "Sí":
                        $ eri._var("route" , True)
                    "No":
                        $ eri._var("route" , False)
                menu:
                    "¿Estás en una relación con [mar!t]?"
                    "Sí":
                        $ mar._var("route" , True)
                    "No":
                        $ mar._var("route" , False)
            "No":
                $ emm._var("route" , False)
    call BlinkXP ("c18s001_450" , "f") from _call_BlinkXP_2504
    play music ("music/KindofGirl.ogg")
    emm "Ha sido una gran idea venir aquí. Una sala solo para nosotros es genial. Sin problemas con idiotas como en el Twins."
    mc "Y sin que todas me tengáis que besar para quitárnoslos de encima."
    call BlinkXP ("c18s001_455" , "d") from _call_BlinkXP_2505
    emm "Bueno... yo no tuve oportunidad de besarte."
    mc "Pero lo hiciste luego en mi habitación."
    if emm._var("route"):
        call BlinkXP ("c18s001_460" , "d") from _call_BlinkXP_2506
        emm "Y me muero de ganas de hacerlo aquí ahora. Pero, por una vez, no quiero ser el centro de atención."
        emm "[eri] lo sabe, pero [dap] no. También es su cumpleaños y no me gustaría que se sintiera mal."
        mc "¿Por qué iba a sentirse mal?"
        if dap._var("route"):
            call BlinkXP ("c18s001_465" , "d") from _call_BlinkXP_2507
            emm "Creo que a ella también le gustas, y no me refiero como primo."
            emm "Besarte aquí sería restregarle por la cara que yo estoy contigo y ella no."
            if dap._var("romance"):
                mcp "(Tu memoria es muy interesante, [emm]. Ya no recuerdas que, durante la primera comida con Meemaw y Tía Betty, dijo que salía con alguien.)"
            else:
                mcp "(Eres muy lista, [emm]. Seguro que recuerdas que, durante la primera comida con Meemaw y Tía Betty, dijo que había un chico que le interesaba y seguro que lo has relacionado conmigo.)"
            mc "Si no te equivocas, y es un \"si\" muy grande, tienes razón. La harías sentir mal. Es el problema de no querer hacerlo público, [emm]."
            if eri._var("route"):
                call BlinkXP ("c18s001_470" , "d") from _call_BlinkXP_2508
                emm "No creo que me equivoque. Ni siquiera [eri] le ha dicho que estáis juntos. Supongo que será porque ella también lo ha notado."
                mc "O porque quiere dejar pasar los cumpleaños para hacer el anuncio a toda la familia."
            mc "Pero deberíamos empezar a pensar cuándo quieres hacer público lo tuyo y lo mío."
        else:
            call BlinkXP ("c18s001_465" , "d") from _call_BlinkXP_2509
            emm "También es su fin de semana y sería un bombazo para todo el mundo."
            if eri._var("route"):
                emm "Y si [eri] también lo hiciera público..."
                mc "Tienes razón. Deberíamos pensar en cuándo quieres hacerlo público."
        if mar._var("route"):
            mc "Mamá, [eri], y Eileen ya lo saben. Tienes que decidir cuándo quieres decírselo al resto."
        else:
            mc "[eri], y Eileen ya lo saben. Tienes que decidir cuándo quieres decírselo al resto."
        call BlinkXP ("c18s001_475" , "d") from _call_BlinkXP_2510
        emm "¿Prometes no enfadarte?"
        mc "¿Qué has hecho ahora? ¿Delante de quién más se te ha escapado?"
        emm "No es eso... Hoy me he levantado con nauseas. No sé si es porque ayer comí como una cerda o... Hace nueve días de nuestra primera vez, y si estuviera embarazada..."
        call BlinkXP ("c18s001_480" , "d") from _call_BlinkXP_2511
        emm "El fin de semana que viene podría hacerme una prueba de embarazo."
        mc "¡Oh, mierda!"
        call BlinkXP ("c18s001_485a" , "d") from _call_BlinkXP_2512
        emm "¿Qué pasa? ¿No quieres tener un hijo conmigo?"
        "Le explicas lo de las pruebas rápidas de embarazo."
        call BlinkXP ("c18s001_485b" , "d") from _call_BlinkXP_2513
        emm "¿Por qué no me lo habías dicho antes?"
        mc "Estabas tan enfadada el día de la comida con Eva que... me olvidé. Creía habértelo dicho."
        call BlinkXP ("c18s001_490" , "d") from _call_BlinkXP_2514
        emm "En cuanto lleguemos a casa me la hago. Cubrirá nuestras dos veces y mañana lo podríamos saber."
        mc "24 horas después de hacer la prueba estaremos jugando a DnD. ¿Serás capaz de aguantar sin mirarlo hasta que acabe la partida?"
        call BlinkXP ("c18s001_495" , "d") from _call_BlinkXP_2515
        emm "Mierda, tienes razón. Y decirles a las chicas que nos tenemos que ir los dos a la vez... mejor no."
        emm "Mejor la hacemos mañana por la mañana y lo sabremos el lunes."
        mc "Me parece una buena idea. Me paso por tu habitación cuando me despierte."
    else:
        call BlinkXP ("c18s001_475" , "d") from _call_BlinkXP_2516
        emm "No me lo recuerdes... ¡Qué vergüenza!"
        mc "No pasa nada. Ya lo hablamos y todo quedó aclarado."
    play sound ("music/notification.ogg")
    "Suena un móvil justo en el momento en que se enciende el proyector y aparece Megan en la pantalla gigante."
    call BlinkXP ("c18s001_500" , "f") from _call_BlinkXP_2517
    stop music fadeout (1.5)
    meg "Buenas noches a todos. Voy a empezar con mi primera actuación de la noche."
    meg "Esta noche tengo a un grupo de amigos... a mi familia... en el local, con lo que hoy es muy emotivo para mí."
    meg "Tan solo espero que disfrutéis estas canciones. ¡Vamos allá!"
    return
label c18s001_Saira:
    if _in_replay:
        menu:
            "¿Estás en una relación con Saira?"
            "Sí":
                $ sai._var("route" , True)
                menu:
                    "¿Estás en una relación con alguien más?"
                    "Sí":
                        $ mc._var("relationships", 2, intention = "set")
                    "No":
                        $ mc._var("relationships", 0, intention = "set")
            "No":
                $ sai._var("route" , False)
    play music ("music/Beautiful-Day-Vocals.ogg")
    call BlinkXP ("c18s001_505" , "d") from _call_BlinkXP_2518
    sai "Creo que es mi turno de un baile contigo, ¿no?"
    mc "Por supuesto, además esta canción me encanta."
    call BlinkXP ("c18s001_510" , "d") from _call_BlinkXP_2519
    mc "¿Qué tal te lo estás pasando?"
    sai "Genial, la sala privada está muy bien y podemos bailar sin tener que luchar por el espacio."
    sai "Ni siquiera tenemos que luchar por ti..."
    mc "¿A qué te refieres?"
    call BlinkXP ("c18s001_515" , "d") from _call_BlinkXP_2520
    sai "A que [dap] es muy lista. Eres el único chico que hay, con lo que todas vamos a bailar contigo."
    sai "En vez de pelearnos por ver a quién le toca, ha montado un sistema de turnos."
    mc "*Risa* Algo así sólo se le podía haber ocurrido a [dap]."
    call BlinkXP ("c18s001_520" , "d") from _call_BlinkXP_2521
    sai "Scarlett también participó haciendo la app que cada una tenemos en el móvil."
    mc "¿Qué? ¿Tenéis una app para saber cuándo os toca bailar conmigo?"
    call BlinkXP ("c18s001_525" , "d") from _call_BlinkXP_2522
    sai "*Risa* Sí, pero no me mires así, Scarlett tenía la app medio hecha para otra cosa y la ha adaptado para esta noche."
    mc "¿Cómo ha funcionado cuando he ido a hablar con Kate?"
    call BlinkXP ("c18s001_530" , "d") from _call_BlinkXP_2523
    sai "Scarlett y [dap] te conocen muy bien y sabían que pasaría algo así. Tienen una opción para mover los turnos. Pero sólo los pueden mover ellas"
    mc "*Risa* Y todas vosotras confiáis de ellas para que los muevan sin hacer trampas, ¿no?"
    call BlinkXP ("c18s001_535" , "d") from _call_BlinkXP_2524
    sai "También han pensado en eso. Nos llega una notificación a todas con los cambios. No pueden moverlos sin que nos enteremos."
    sai "Así se fomenta la confianza, ¿no? *Risa*"
    mc "*Risa* Sois tremendas."
    call BlinkXP ("c18s001_540" , "d") from _call_BlinkXP_2525
    if sai._var("route") and mc._var("relationships")>1:
        sai "Estoy pensando en que deberíamos montar algo parecido a esta app para saber cuándo podemos tener tiempo a solas contigo cada una de las chicas de tu harén. *Risa*"
    elif sai._var("route"):
        sai "Estoy pensando en pedirle que haga una adaptación de la app para saber cuándo estás libre para tener tiempo a solas contigo. *Risa*"
    else:
        sai "Si hubiéramos vuelto a lo que teníamos en Portland, hubiese sido algo muy útil. Especialmente si estás con otras mujeres."
        mc "Sí, no hubiera estado mal tener algo así. *Risa*"
        mc "Aunque habría que poner algún botón para imprevistos que me llenasen la agenda por un par de días porque nadie más quiere o puede resolverlos."
    if sai._var("route"):
        mc "*Risa* No creo que sea tan difícil tener tiempo a solas conmigo, ¿no?"
        call BlinkXP ("c18s001_545" , "d") from _call_BlinkXP_2526
        sai "¿Lo estás diciendo en serio? ¡Llevo cuatro días aquí y me están saliendo telarañas esperándote! *Risa*"
        mc "*Risa* Sabes que no hace falta que me esperes y que tú puedes tomar la iniciativa cuando quieras, ¿no?"
        mc "No es que estemos en los 70 o en una película. Las chicas podéis decidir pasar a la acción y nadie os va a juzgar. *Risa*"
        mc "Además, somos tú y yo. Nunca has estado esperando a que yo actuara."
        call BlinkXP ("c18s001_550" , "d") from _call_BlinkXP_2527
        sai "Mmmm... Tienes razón. Lo pensaré... "
        mc "Una vez pase esta locura de fin de semana estaré mucho más libre. Al menos hasta que surja el siguiente problema que nadie más que yo pueda resolver. *Risa*"
    call BlinkXP ("c18s001_555" , "d") from _call_BlinkXP_2528
    sai "Te estamos exigiendo mucho entre todas, ¿no?"
    mc "No, Saira. Eso es lo mejor de todo. No exigís nada. Lo hago todo porque me apetece y me siento a gusto haciéndolo por vosotras."
    mc "Pero sois un montón, y siempre hay una urgencia, a alguien a quien llevar a algún sitio, algo que comprar, o algo en lo que ayudar."
    call BlinkXP ("c18s001_560" , "d") from _call_BlinkXP_2529
    sai "Sabes que casi todas tenemos carnet de conducir, ¿verdad? Las labores de taxista nos las podemos repartir entre nosotras y así tendrás más tiempo libre."
    mc "Lo sé, pero si me pides que te lleve a algún sitio, lo voy a hacer. No te voy a decir \"toma las llaves del coche y ve tú sola\"."
    mc "Además, ya te digo que disfruto haciéndolo. Hacer cosas con y para vosotras es pasar tiempo con vosotras."
    play sound ("music/notification.ogg")
    "Suena un móvil en algún lugar."
    call BlinkXP ("c18s001_565" , "d") from _call_BlinkXP_2530
    sai "Mi turno ha acabado. Te dejo en buenas manos."
    stop music fadeout (1.5)
    mc "*Risa* ¿Ves lo que te decía? Al final decidís mi agenda por mí."
    return
label c18s001_Erika:
    if _in_replay:
        $ sim._var("route" , False)
        $ sam._var("route" , False)
        $ nor._var("route" , False)
        $ oma._var("route" , False)
        $ emm._var("route" , False)
        $ eil._var("route" , False)
        $ mar._var("route" , False)
        menu:
            "¿Estás en una relación con [eri]?"
            "Sí":
                $ eri._var("route" , True)
                menu:
                    "¿Estás en una relación con [nor]?"
                    "Sí":
                        $ nor._var("route" , True)
                    "No":
                        $ nor._var("route" , False)
                        menu:
                            "¿Estás en una relación con Alexia?"
                            "Sí":
                                $ oma._var("route" , True)
                            "No":
                                $ oma._var("route" , False)
                                menu:
                                    "¿Estás en una relación con [emm]?"
                                    "Sí":
                                        $ emm._var("route" , True)
                                    "No":
                                        $ emm._var("route" , False)
                                        menu:
                                            "¿Estás en una relación con Eileen?"
                                            "Sí":
                                                $ eil._var("route" , True)
                                            "No":
                                                $ eil._var("route" , False)
                        menu:
                            "¿Estás en una relación con [mar!t]?"
                            "Sí":
                                $ mar._var("route" , True)
                            "No":
                                $ mar._var("route" , False)
                menu:
                    "¿Estás en una relación con Samantha?"
                    "Sí":
                        $ sam._var("route" , True)
                    "No":
                        $ sam._var("route" , False)
                        menu:
                            "¿Estás en una relación con Simone?"
                            "Sí":
                                $ sim._var("route" , True)
                            "No":
                                $ sim._var("route" , False)
            "No":
                $ eri._var("route" , False)
        menu:
            "¿Le cogiste el teléfono a tu padre cuando llamó?"
            "Sí":
                $ mc._var("edmundsStory", True)
            "No":
                $ mc._var("edmundsStory", False)
    scene c18s001_570An #abcd
    pause (3.2)
    call BlinkXP ("c18s001_575" , "d") from _call_BlinkXP_2531
    play music ("music/Be-The-One-Vocals.ogg")
    eri "¿Bailas?"
    mc "Claro, es tu turno, ¿no? *Risa*"
    call BlinkXP ("c18s001_580" , "d") from _call_BlinkXP_2532
    eri "*Risa* Sí, ahora me toca a mí."
    eri "¿Quién te lo ha dicho?"
    mc "Se dice el pecado, pero no el pecador."
    call BlinkXP ("c18s001_585" , "d") from _call_BlinkXP_2533
    eri "Tampoco importa. No es que lo quisiéramos guardar en secreto."
    eri "Pero ha sido una buena idea por parte de [dap] y Scarlett."
    eri "Si te tenemos que compartir, mejor hacerlo de forma ordenada."
    mc "Ha sido una buena idea, pero con fallos. ¿Qué pasaría si quiero bailar cuatro canciones seguidas contigo?"
    call BlinkXP ("c18s001_590" , "d") from _call_BlinkXP_2534
    eri "*Risa* Me vería obligada a rechazarte durante el resto de la noche."
    eri "Pero todas sabemos que no lo harás. No querrías que el resto de las chicas se sintieran mal."
    mc "¡Joder, [eri]! *Risa* Me conocéis demasiado bien."
    call BlinkXP ("c18s001_595" , "d") from _call_BlinkXP_2535
    eri "No se lo digas a nadie, pero creo que mi hermana y Scarlett están haciendo un experimento social contigo. *Risa*"
    call BlinkXP ("c18s001_600" , "d") from _call_BlinkXP_2536
    eri "Bueno... mi hermana desde siempre... ahora tengo otra."
    eri "Y Scarlett casi lo es también."
    if mc._var("edmundsStory"):
        mcp "(No vas desencaminada, pero creo que, como mucho, será prima)"
    call BlinkXP ("c18s001_605" , "d") from _call_BlinkXP_2537
    eri "Y el resto de las chicas... en un par de semanas nos vamos a empezar a llamar \"hermana\" las unas a las otras."
    eri "Antes Kim estaba hablando con Tía Betty y con Kiara. Ya es normal que la llamen \"Tía Betty\", pero es que ha llamado a Kiara \"Tía Kiara\"."
    mc "¿Se nos está yendo de las manos?"
    call BlinkXP ("c18s001_610" , "d") from _call_BlinkXP_2538
    eri "No, justo lo contrario. Es fantástico. Cuando mi madre me dijo que íbamos a tener chicas en casa, nunca me podría haber imaginado esto."
    if eri._var("route"):
        eri "Si ese test sale positivo... Hope va a tener muchas más tías de lo que podría haber esperado."
        mc "Seguro que se pelean por cambiarle los pañales. *Risa* Y eso nos dejará tiempo libre para nosotros."
        call BlinkXP ("c18s001_615" , "d") from _call_BlinkXP_2539
        if nor._var("route") or emm._var("route") or eil._var("route") or oma._var("route"):
            eri "Eso teniendo en cuenta que alguna de ellas tenga sus propios hijos."
            mc "Entonces dejaremos que Meemaw cambie los pañales de todos. *Risa* Ya sabes que está pidiendo bisnietos."
        else:
            eri "Podemos usar la app de Scarlett para que se organicen los turnos de cambio pañales. *Risa*"
            mc "Meemaw va a querer cambiarlos todos. *Risa* Ya sabes que está pidiendo bisnietos."
        mc "Si los pide, debe tomar responsabilidad sobre ellos."
        call BlinkXP ("c18s001_620" , "d") from _call_BlinkXP_2540
        eri "Solo de pensar que vamos a tener que decírselo... me da miedo cómo se lo va a tomar. Esté embarazada o no lo esté."
        if nor._var("route"):
            mc "Ya sabe que estoy con tu madre. Ladró un poco, pero tuvo que aceptarlo."
            call BlinkXP ("c18s001_625" , "d") from _call_BlinkXP_2541
            eri "¿Qué? ¿Cuándo?"
        elif mar._var("route"):
            mc "Ya sabe que estoy con alguien de la familia. Ladró un poco, pero tuvo que aceptarlo."
            call BlinkXP ("c18s001_625" , "d") from _call_BlinkXP_2542
            if emm._var("route"):
                eri "¿Qué? ¿Cuándo? No sabía que a [emm] también se le hubiera escapado con ella."
            else:
                eri "¿Qué? ¿Cuándo? No voy a preguntar con quién..."
        if mar._var("route") or nor._var("route"):
            if sam._var("route") or sim._var("route"):
                mc "El día que fuimos a la playa para la comida navideña."
            else:
                mc "El día que tuvimos la reunión con Aaron, Amanda, y Eva."
            call BlinkXP ("c18s001_630" , "d") from _call_BlinkXP_2543
            eri "Entonces creo que estoy preparada para hacerlo público. El martes sería un buen día."
        else:
            mc "Sigo pensando que le tenéis demasiado miedo. ¿Qué va a hacer? Ladrar un poco y aceptar lo que es un hecho sobre el que no tiene ningún control."
            call BlinkXP ("c18s001_630" , "d") from _call_BlinkXP_2544
            eri "Tienes razón. Creo que estoy preparada para hacerlo público. El martes sería un buen día."
        eri "Y si ese test sale positivo, soltamos las dos cosas a la vez."
        mc "Me parece una buena idea. *Risa* No le habrá dado tiempo de recuperarse de las emociones de los cumpleaños."
        call BlinkXP ("c18s001_635" , "d") from _call_BlinkXP_2545
        eri "Olvida lo del martes..."
        eri "Mejor no pongamos fecha o estaré nerviosa hasta que llegue."
        mc "No hay ningún problema. Solo una pregunta. ¿Se lo quieres decir solo a la familia o a todas las chicas?"
        call BlinkXP ("c18s001_640" , "d") from _call_BlinkXP_2546
        eri "A la familia. Y eso incluye a todas las chicas."
    else:
        mc "Hemos ampliado la familia sin darnos cuenta."
        eri "Desde luego."
        scene c18s001_640An with dissolve # (615a-620a-625a-630a-635a-640a)
        "Bailáis mientras charláis de cómo la llegada de las estudiantes y de Eva y Amanda ha cambiado vuestras vidas."
    play sound ("music/notification.ogg")
    "Suena un móvil."
    call BlinkXP ("c18s001_645" , "d") from _call_BlinkXP_2547
    eri "Mi turno ha acabado. No recuerdo a quién le tocaba ahora."
    mc "Dile a quien sea que le toque que me espere. Tengo que ir al lavabo un momento."
    eri "De acuerdo. No tardes o se van a acabar las canciones para bailar pegados."
    stop music fadeout (1.5)
    mc "Hasta ahora."
    return
label c18s001_Debbie:
    if _in_replay:
        menu:
            "¿Estás en una relación con Debbie?"
            "Sí":
                $ deb._var("route" , True)
                menu:
                    "¿Estás en una relación con [dap]?"
                    "Sí":
                        $ dap._var("route" , True)
                    "No":
                        $ dap._var("route" , False)
            "No":
                $ deb._var("route" , False)
    scene c18s001_650d with fade
    play music ("music/Separation.ogg")
    mcp "(Ciertamente Lisa tenía razón. Un baño acorde con el local, con una bonita antesala que parece ser que se usa también como guardarropía cuando alquilan la sala anexa.)"
    mcp "(Los lavabos de la sala principal no tienen una antesala como esta. Tampoco necesitan un guardarropía.)"
    mcp "(Hora de mear.)"
    call BlinkXP ("c18s001_650" , "f") from _call_BlinkXP_2548
    "Un momento después..."
    mc "Hey, Debbie, ¿estás esperando a alguna de las chicas?"
    if deb._var("route"):
        deb "No, te esperaba a ti."
        mc "¿A mí?"
        call BlinkXP ("c18s001_655" , "d") from _call_BlinkXP_2549
        deb "Sí, era mi turno de bailar contigo, pero como no lo voy a hacer, al menos quería pagarte un plazo de la Piedra Corazón."
        mc "Esos plazos siempre son bienvenidos."
        scene c18s001_655d with dissolve
        "Parece mentira que tan solo haya pasado un día y medio desde vuestra visita al lago."
        "Vuestros labios se unen con urgencia, como si hubieran pasado meses."
        call BlinkXP ("c18s001_660" , "d") from _call_BlinkXP_2550
        deb "*Suspiro* Supongo que lo de dejarme sin respiración en cada beso durará un poco todavía, ¿no?"
        mc "*Risa* Espero que dure muchos años."
        mc "¿Qué es eso de que no ibas a bailar conmigo? ¿Por qué? ¿Estás cansada después de estar nadando con Kate?"
        call BlinkXP ("c18s001_665" , "d") from _call_BlinkXP_2551
        deb "No, que va. Ha sido un entrenamiento suave. Al menos para mí. Para Kate ha sido duro, pero el único deporte que ha hecho el último año ha sido levantamiento de comida. *Risita*"
        mc "¿Entonces por qué no quieres bailar conmigo? ¿Te da vergüenza bailar conmigo delante de las chicas? ¿Creen que van a notar lo que hay entre nosotros?"
        call BlinkXP ("c18s001_670" , "d") from _call_BlinkXP_2552
        deb "No es eso... es que... soy muy mala bailando. Bailando sola. Bailar con un chico... no me lo he planteado nunca. Les sacaba una cabeza a casi todos los chicos del instituto."
        mc "A mí me sacas media cabeza con los tacones. Y no me importa."
        deb "Pero es que... el sentido del ritmo de la familia se lo llevó Lisa. Yo me llevé dos pies izquierdos."
        mc "Es decir, que tienes miedo de pisarme. *Risa*"
        call BlinkXP ("c18s001_675" , "d") from _call_BlinkXP_2553
        deb "¡No te rías! No tengo miedo de pisarte. Tienes miedo cuando hay una posibilidad de que algo pase. No sé cómo llamar a cuando tienes la certeza de que va a pasar..."
        mc "*Risa* Bien visto. Yo tampoco soy un gran bailarín, pero... ¿bailarías conmigo si te puedo asegurar que no me vas a pisar?"
        call BlinkXP ("c18s001_680" , "d") from _call_BlinkXP_2554
        deb "No puedes asegurar eso..."
        mc "Pero si lo hago, ¿bailarías?"
        deb "Sí, pero no va a pasar..."
        scene c18s001_685d with dissolve
        deb "[mc]... ¿Me estás tocando el culo? *Risa*"
        mc "Es el primer paso para bailar."
        scene c18s001_685e with vpunch
        mc "O el primer paso para volar."
        deb "*Suspiro de sorpresa*"
        call BlinkXP ("c18s001_685" , "d") from _call_BlinkXP_2555
        deb "¿Qué? ¿Estás loco? *Risa* ¡Bájame!"
        mc "No. Ahora me sacas la cabeza entera y no me puedes pisar, con lo que vamos a bailar."
        call BlinkXP ("c18s001_690" , "d") from _call_BlinkXP_2556
        deb "Lo he prometido, ¿no?"
        mc "Sí. Lo has hecho."
        deb "Pero bájame al suelo o te vas a destrozar la espalda."
        mc "No te preocupes y disfruta de nuestro primer baile."
        call BlinkXP ("c18s001_700" , "d") from _call_BlinkXP_2557
        deb "Sabes que, si alguna vez le ponemos una etiqueta a esto, serías el novio perfecto, ¿verdad?"
        mc "No sé si yo lo sería, pero tu sí que eres perfecta. Con etiqueta o sin ella."
        call BlinkXP ("c18s001_705" , "d") from _call_BlinkXP_2558
        deb "Gracias..."
        mc "¿Pasa algo, Debbie?"
        call BlinkXP ("c18s001_710" , "d") from _call_BlinkXP_2559
        deb "Sé que lo dices para hacerme sentir bien y porque suena romántico..."
        mc "Lo digo porque lo pienso."
        call BlinkXP ("c18s001_715" , "d") from _call_BlinkXP_2560
        deb "Pero soy enorme..."
        mc "Lo que significa que hay más Debbie para mí..."
        call BlinkXP ("c18s001_720" , "d") from _call_BlinkXP_2561
        deb "Desgarbada..."
        mc "Aún no me has pisado. *Risa*"
        call BlinkXP ("c18s001_725" , "d") from _call_BlinkXP_2562
        deb "*Risa* Eso es porque no me has dejado tocar el suelo..."
        scene c18s001_725d with vpunch
        mc "Ya está, ya estás tocando el suelo. Y sigues sin pisarme."
        call BlinkXP ("c18s001_730" , "d") from _call_BlinkXP_2563
        deb "Soy muy masculina... musculosa..."
        mc "¿Masculina? ¿De dónde has sacado esa idea? ¿En Aurora no existen los espejos?"
        mc "Y los músculos de tu culo se sienten perfectos en mis manos, y no puedo esperar a recorrer esos abdominales con las yemas de mis dedos. Tienes un cuerpo perfecto."
        scene c18s001_730d with hpunch
        deb "No me mientas, [mc]. Me gusta que me digas cosas bonitas, pero no que me mientas."
        mc "¿En qué he mentido? Nunca miento, Debbie."
        deb "Conozco mi cuerpo... A todos los chicos os gustan las tetas... y las mías... son inexistentes..."
        mc "Entonces, si no existen..."
        call BlinkXP ("c18s001_735" , "d") from _call_BlinkXP_2564
        mc "... no me puedes decir nada por NO tocarlas, como estoy haciendo ahora."
        deb "¡[mc]!"
        mc "¿Qué? Según acabas de decir no estoy tocando nada que exista."
        "Notas bajo tus dedos sus firmes y pequeños pechos sin sujetador. Sus pezones erectos. Unas tetas no necesitan ser enormes para ser perfectas."
        "Su cuerpo tiembla bajo tu tacto."
        scene c18s001_735d with dissolve
        mc "Afortunadamente, tu espalda sí que existe. *Smooch*"
        deb "Me acabas de poner la piel de gallina..."
        "Puedes notar como su vello se eriza con cada roce de tus labios."
        mc "¿Te gusta? *Smooch*"
        "Es una pregunta retórica. Sabes la respuesta."
        scene c18s001_735e with dissolve
        deb "Me encanta que me beses la espalda..."
        mc "Y a mí me encanta besarla. No puedo esperar a besar el resto de ti."
        call BlinkXP ("c18s001_740" , "d") from _call_BlinkXP_2565
        deb "Pero prefiero que tus labios se posen sobre los míos... "
        mc "Cualquier parte de ti me parece bien."
        scene c18s001_740d with dissolve
        "Mucho más ansiosa que antes. Mucho más pasional. Demostrarle que sus complejos son irreales le ha dado una confianza que antes no tenía."
        "Algún día se dará cuenta de lo preciosa que es a tus ojos."
        call BlinkXP ("c18s001_745" , "d") from _call_BlinkXP_2566
        deb "¿Cuándo has dicho que estaré preparada para el siguiente paso?"
        mc "No lo he dicho. *Risa* Pero pareces ansiosa."
        call BlinkXP ("c18s001_750" , "d") from _call_BlinkXP_2567
        deb "Si unos besos en la espalda me han hecho hervir la sangre... no sé qué pasará cuando tengas todo mi cuerpo a tu disposición."
        mc "Algo parecido a esto..."
        scene c18s001_750d with dissolve
        "El cuerpo de Debbie se vuelve a estremecer bajo tus labios, bajo tus dedos."
        "Besar sus abdominales es como besar una piedra con piel de gallina. Mucho más cálidos de lo que una piedra puede ser."
        call BlinkXP ("c18s001_755" , "d") from _call_BlinkXP_2568
        deb "O subes a mis labios de nuevo o te meto en el lavabo de caballeros. Y entonces alguna de las chicas sospechará."
        mc "Subir a tus labios o bajar a ellos... Difícil elección. *Risa*"
        scene c18s001_740e with dissolve
        "Decides subir."
        "La idea del lavabo de caballeros es tentadora, pero no es el momento."
        scene c18s001_760An with dissolve # aparece [dap] abc
        dap "Hola, chicos..."
        if dap._var("route"):
            dap "Vuestro secreto también está a salvo conmigo. *Risa*"
        dap "Seguid a lo vuestro..."
        call BlinkXP ("c18s001_765" , "d") from _call_BlinkXP_2569
        deb "¡[dap]! ¡Esto no es lo que parece!"
        mc "*Risa* Dijiste exactamente lo mismo con Eva."
        scene c18s001_770d with dissolve
        dap "No os preocupéis por mí. Solo iba al lavabo. Seguid a lo vuestro."
        scene c18s001_770e with dissolve
        pause (0.8)
        call BlinkXP ("c18s001_770" , "d") from _call_BlinkXP_2570
        dap "Ah, y felicidades. Me alegro mucho por vosotros."
        if dap._var("route"):
            dap "La primera chica del harén que conozco. *Risita*"
        scene c18s001_770e with dissolve
        pause (0.8)
        call BlinkXP ("c18s001_775a" , "d") from _call_BlinkXP_2571
        deb "Tengo que ir a hablar con ella."
        if dap._var("route"):
            deb "Suerte que la casa es de [mar] y no de Olivia. Si no, esto parecería una AVN, incluso sé el título que tendría."
            mc "Ve a hablar con ella si quieres, ahora compartís un secreto en los dos sentidos."
        else:
            mc "Ve a hablar con ella si quieres, pero si [dap] dice que no le importa, es que no le importa."
        call KissXP ("c18s001_780a" , "d") from _call_KissXP_77
        deb "Lo sé, pero prefiero hablar y aclarar las cosas."
        deb "Te veo luego. {size=20}Te quiero.{/size}"
        mc "¿Qué has dicho? No te he oído bien."
        scene c18s001_770f with dissolve
        deb "Que te veo luego."
        deb "Si quieres seguir el orden de turnos, te toca bailar con Amanda. Es la siguiente en la lista."
        scene c18s001_770e with dissolve
        mc "*Risa* No es lo que me ha parecido oír."
        stop music fadeout (1.5)
        mcp "(De vuelta al resto de chicas.)"
    else:
        deb "No, era mi turno de bailar contigo y, como tú has desaparecido, voy a aprovechar para hacer una visita que sólo yo puedo hacer. *Risita*"
        mc "¿Quieres que te espere para ese baile?"
        call BlinkXP ("c18s001_655" , "d") from _call_BlinkXP_2572
        deb "No hace falta. Ve a bailar con Amanda, si quieres, es la siguiente en la lista."
        mc "OK. Hasta ahora."
        stop music fadeout (1.5)
        deb "Hasta ahora."
    return
label c18s001_Amanda:
    scene c18s001_770g with fade
    play music ("music/I-Need-You-Now-Vocals.ogg")
    "Vuelves a la sala y te diriges a Amanda."
    call BlinkXP ("c18s001_775" , "d") from _call_BlinkXP_2573
    mc "Amanda, ¿te apetece bailar?"
    ama "Pero no es mi turno..."
    mc "No te preocupes por eso. Ya lo he hablado con Debbie."
    call BlinkXP ("c18s001_780" , "d") from _call_BlinkXP_2574
    ama "Entonces, encantada de bailar contigo. Es la última canción de Megan antes de su descanso."
    mc "Aprovechémosla entonces."
    call BlinkXP ("c18s001_785" , "d") from _call_BlinkXP_2575
    mc "¿Qué tal os lo estáis pasando?"
    ama "¡Genial! Estar aquí con las chicas y tener más rato para conocernos es muy divertido."
    mc "*Risa* Las conoces más que de sobras."
    call BlinkXP ("c18s001_790" , "d") from _call_BlinkXP_2576
    ama "Yo las conozco. Ellas aún no saben cómo soy. Al menos ya se están acabando las preguntas... raras."
    mc "¿Os han hecho muchas? ¿Me puedes poner un ejemplo de una de esas preguntas raras?"
    call BlinkXP ("c18s001_795" , "d") from _call_BlinkXP_2577
    ama "La más rara hasta ahora ha sido sobre si teníamos sexo con los clones XY."
    mc "*Risa* Esa ha sido [emm], seguro. No sé si quiero saber la respuesta."
    call BlinkXP ("c18s001_800" , "d") from _call_BlinkXP_2578
    ama "¿No saber la respuesta a si ha sido [emm] o a la pregunta? *Risa*"
    mc "A la pregunta."
    ama "Entonces te alegrará saber que no ha sido [emm]. Y la respuesta ha sido No. Pero no me preguntes quién ha sido. Era una conversación de chicas."
    mc "*Risa* Voy a empezar a recortar el tiempo que pasas con ellas, si empezáis a tener secretos."
    call BlinkXP ("c18s001_805" , "d") from _call_BlinkXP_2579
    ama "Atrévete si no valoras tu vida. Y no es que vayamos a matarte ni Eva ni yo, sino ellas. *Risa*"
    mc "Me lo creo. Ahora que os habéis encontrado os vais a hacer inseparables."
    mc "Cambiando de tema y hablando de preguntas raras. ¿Quién es mayor? ¿Eva o tú?"
    call BlinkXP ("c18s001_810" , "d") from _call_BlinkXP_2580
    if persistent.family:
        ama "Yo. El grupo A salimos del tanque antes que el grupo B. Técnicamente \"nací\" dos días antes que Eva."
    else:
        ama "Yo. Por dos días."
    ama "Siempre le ha desagradado ser la más pequeña."
    call BlinkXP ("c18s001_815" , "d") from _call_BlinkXP_2581
    ama "... desde que murió Fiona."
    mc "Espera... ¿Fiona era la más joven?"
    ama "Sí..."
    mc "Vuestros nombres entonces... ¿son por orden alfabético?"
    call BlinkXP ("c18s001_820" , "d") from _call_BlinkXP_2582
    ama "Sí, nos los pusieron Aaron y Arnau. Hasta entonces éramos los sujetos A, B, C, D, E, y F."
    mc "NTR os estaba deshumanizando..."
    if persistent.family:
        mc "Supongo que era más fácil para ellos hacerlo así que veros como personas. Como clones de su propia familia."
        call BlinkXP ("c18s001_825" , "d") from _call_BlinkXP_2583
    else:
        mc "Sin embargo, les pusieron nombres a [emm], [dap], y [eri]."
        call BlinkXP ("c18s001_825" , "d") from _call_BlinkXP_2584
        ama "Los nombres se los pusieron cuando las sacaron del laboratorio. No podían presentarle a [mar] una niña y decirle que se llamaba Experimento XX-0-A. Prefirieron llamarla [emm]."
    ama "Querían estudiar cómo ellas y nosotras nos desarrollábamos diferente al estar en la base o el mundo exterior, con una familia normal."
    mc "¿Normal? Creo que somos cualquier cosa menos normal."
    mc "Pero me alegra joderles el experimento."
    call BlinkXP ("c18s001_830" , "d") from _call_BlinkXP_2585
    ama "¿A qué te refieres con joderles el experimento? El experimento acabó con el accidente de avión."
    mc "Bueno, de todas formas no podría continuar. Ahora vosotras también estáis en la misma familia. Aunque cada vez es menos normal. Ya no habría nada que estudiar."
    mc "Y si no hay experimento que joder, igualmente me alegra que estéis aquí. Sólo espero que entrar en la familia no estropee la relación entre Eva y tú."
    mc "Antes os he visto discutir."
    call BlinkXP ("c18s001_835" , "d") from _call_BlinkXP_2586
    ama "Eva sigue dándole vueltas al beso de anoche. Pero se le pasará."
    mc "Y tú no la ayudas a olvidarlo acusándola de ponerse ese vestido por mí."
    call BlinkXP ("c18s001_840" , "h") from _call_BlinkXP_2587
    ama "¿Te lo ha dicho? ¡Chivata!"
    mc "*Risa* Las dos habéis dicho lo mismo de la otra. ¿Te das cuenta de lo ridículo que suena?"
    call BlinkXP ("c18s001_845" , "d") from _call_BlinkXP_2588
    ama "Ahora que lo has dicho... sí. Nos estamos comportando como niñas pequeñas. Todo esto es nuevo para nosotras..."
    mc "No pasa nada, Amanda. Pero no dejéis que os separe."
    mc "Además..."
    scene c18s001_845d with dissolve
    mc "*Susurrando* Tú también estás preciosa con ese vestido."
    call BlinkXP ("c18s001_850" , "d") from _call_BlinkXP_2589
    ama "¿De verdad lo crees? Gracias... Me lo ha prestado [emm], usamos casi la misma talla... *Risa* Lógicamente."
    mc "Aunque sea un vestido prestado estás tan bonita como cualquier otra chica esta noche. No puedo esperar a verte con un vestido elegido por ti."
    call BlinkXP ("c18s001_855" , "d") from _call_BlinkXP_2590
    ama "Me vas a hacer ruborizar."
    mc "Bueno, el estilo de Eva es el de una espía devora hombres. Quiero saber cuál es el tuyo. Seguro que estarás preciosa."
    call BlinkXP ("c18s001_860" , "d") from _call_BlinkXP_2591
    ama "¿Crees que debería ir a hablar con Eva? ¿Dejar las cosas claras?"
    mc "No lo sé. Tú la conoces mejor que yo. Si fuera [emm] yo lo haría."
    ama "Es que es la primera vez que estamos en esta situación. Nunca nos hemos peleado por un chico."
    call BlinkXP ("c18s001_865" , "h") from _call_BlinkXP_2592
    ama "¡Oh! ¡Mierda! ¡Olvida lo que he dicho!"
    mc "No he oído nada."
    mcp "(Pero supongo que lo que no he oído responde a mi pregunta sobre si estabas flirteando conmigo.)"
    call BlinkXP ("c18s001_870" , "d") from _call_BlinkXP_2593
    ama "Creo que voy a hablar con ella. Lisa es la siguiente."
    mc "Arregladlo antes de que se enquiste. Voy a ver a Lisa."
    scene c18s001_870d with dissolve
    ama "{i}(¿Cómo puedo haber sido tan tonta como para que se me escape? Al menos ahora la pelota está en tu tejado, [mc].){/i}"
    stop music fadeout (1.5)
    return
label c18s001_Lisa:
    if _in_replay:
        menu:
            "¿Estás en una relación con Debbie?"
            "Sí":
                $ deb._var("route" , True)
                menu:
                    "¿En cuántas relaciones estás?"
                    "Más de una":
                        $ mc._var("relationships", 2, intention = "set")
                    "Una o ninguna":
                        $ mc._var("relationships", 1, intention = "set")
            "No":
                $ deb._var("route" , False)
        menu:
            "¿Tienes Puntos de Relación positivos con Lisa?"
            "Sí":
                $ lis._var("relationshipPoints", 5, intention = "set")
            "No, un poco negativos":
                $ lis._var("relationshipPoints", -4, intention = "set")
            "No, muy negativos":
                $ lis._var("relationshipPoints", -20, intention = "set")
    $ Aux = False
    if lis.rps < 0 and not deb._var("route"):
        scene c18s001_870e with fade
        mcp "(Lisa me cae bien, pero yo a ella no. ¿Debería sacarla a bailar?)"
        play music ("music/SensualJazzMedium2.ogg")
        mcp "(Quizás sea una oportunidad para conocernos mejor.)"
        if persistent.walkthrough:
            $ wt1 = "Lisa +5"
            $ wt2 = "Lisa -25"
        else:
            $ wt1 = ""
            $ wt2 = ""
        menu:
            "Por supuesto." (wt = wt1):
                $ lis.rp(5)
                mcp "(No quiero que se sienta mal porque no la saque a bailar en su turno.)"
                call BlinkXP ("c18s001_875" , "d") from _call_BlinkXP_2594
                mc "Lisa, ¿te apetece bailar?"
                lis "Por supuesto. Te veo luego, [dap]."
                if lis.rps < 0:
                    lis "{i}(No quiero que se sienta mal porque yo sea la única que la rechaza.){/i}"
                else:
                    lis "{i}(No es tan mal chico como parecía al principio. Quizás me equivoqué juzgándolo.){/i}"
                if deb._var("route"):
                    lis "{i}(Además está con Debbie. Quizás sea buen momento para conocerlo mejor.){/i}"
            "Será mejor no hacerlo." (wt = wt2):
                $ lis.rp(-25)
                mcp "(No quiero que se sienta obligada a bailar conmigo exclusivamente porque lo dice una app.)"
                mcp "(Mejor voy a por otro zumo.)"
                $ Aux = True
                $ resetWalkthrough ()
                return
        $ resetWalkthrough ()
    else:
        call BlinkXP ("c18s001_880" , "d") from _call_BlinkXP_2595
        lis "Creo que me toca a mí bailar con el chico de la noche, ¿no?"
        play music ("music/SensualJazzMedium2.ogg")
        mc "Eso me han dicho. Pero si no te apetece..."
        lis "No te preocupes, me apetece."
        if deb._var("route"):
            lis "{i}(Además estás con Debbie. Quizás sea buen momento para conocerte mejor.){/i}"
    call BlinkXP ("c18s001_885" , "d") from _call_BlinkXP_2596
    lis "No soy muy buena bailarina. Me vas a tener que llevar tú."
    mc "*Risa* Si le preguntas a [emm], descubrirás que yo tampoco lo soy."
    mc "Pero me extraña tanto que chicas de clase alta no hayáis tomado clases de baile. Es lo que se ve en las películas. Danza, piano, y cosas por el estilo."
    if deb._var("route"):
        mc "Debbie también me ha dicho que era mala bailarina, aunque no me ha pisado ni una vez. *Risa*"
        call BlinkXP ("c18s001_890" , "d") from _call_BlinkXP_2597
        lis "¿Eh? No os he visto bailar... Me extraña tanto que mi hermana baile con un chico... Me hubiera gustado verlo."
        mc "Nos hemos cruzado en el guardarropía y hemos bailado allí."
        lis "Ah, OK. Un baile privado. Que romántico..."
    call BlinkXP ("c18s001_895" , "d") from _call_BlinkXP_2598
    lis "Sobre las clases de baile... Ni Debbie ni yo estábamos interesadas. Mis padres lo intentaron, pero nosotras nos negamos."
    lis "Yo por rebeldía tonta y Debbie porque nunca estuvo interesada. Siempre le interesaron más otras actividades."
    mc "Lo de la rebeldía te pega. *Risa* Y a Debbie lo de estar interesada en los deportes en vez de en la danza."
    call BlinkXP ("c18s001_900" , "d") from _call_BlinkXP_2599
    lis "*Risa* Sí, la verdad es que no quería ser un cliché de chica de clase alta y acabé siéndolo."
    lis "La chica blanca rica que va a manifestaciones de pro veganas y a protestas climáticas."
    mc "Bueno, me parecen buenas causas."
    call BlinkXP ("c18s001_905" , "d") from _call_BlinkXP_2600
    lis "Lo son. Pero, en la mayoría de los casos, sirven de muy poco y sólo a nivel local. Alguien debería hacer algo en las esferas políticas."
    mc "El problema es encontrar a ese alguien, ¿no? La clase política suele tener demasiados intereses cruzados y estar atada a demasiados lobbies."
    call BlinkXP ("c18s001_910" , "d") from _call_BlinkXP_2601
    lis "Sí, y la mayoría de gente concienciada también está muy politizada. El establishment los tacha de comunistas, con lo que es difícil que alguna vez tengan poder."
    mc "Y los que no estáis politizados, la base de esos movimientos, no estáis interesados en entrar en política. Tú estudias Arte, por ejemplo."
    call BlinkXP ("c18s001_915" , "d") from _call_BlinkXP_2602
    lis "*Risa* ¿Me ves como alcaldesa de un pueblo? No es algo para mí."
    mc "¿Por qué no? ¿Demasiadas responsabilidades? Al menos nadie te podría tachar de comunista."
    if persistent.walkthrough:
        $ wt1 = "Lisa +10"
        $ wt2 = _("Sin Consecuencias")
    else:
        $ wt1 = ""
        $ wt2 = ""
    menu:
        "Yo podría votarte." (wt = wt1):
            $ lis.rp(10)
            mc "Dependiendo de tu programa, obviamente. Sé que, al menos, serías honesta."
            call BlinkXP ("c18s001_920" , "d") from _call_BlinkXP_2603
            lis "¡Wow! Eso no me lo esperaba."
            mc "¿Por qué no? Ahora que te conozco mejor, creo que podrías hacer un buen trabajo como alcaldesa de donde sea."
        "No decir nada" (wt = wt2):
            lis "No es eso. No me veo ejerciendo la política. ¿Crees que alguien me votaría?"
    $ resetWalkthrough ()
    mc "No hubiera votado por la Lisa que conocí en el aeropuerto. Pero sí por la que está bailando conmigo ahora mismo."
    call BlinkXP ("c18s001_925" , "d") from _call_BlinkXP_2604
    lis "Me comporté como una imbécil, ¿verdad?"
    mc "Yo no diría eso, pero no fue demasiado agradable conocerte aquel día."
    lis "Lo siento..."
    mc "Un mal día lo tiene cualquiera. Nos has demostrado a todos que aquella Lisa no eras tú."
    mc "Si dejas que la gente te conozca, ¿por qué no te van a votar?"
    call BlinkXP ("c18s001_930" , "d") from _call_BlinkXP_2605
    lis "Se necesitan muchas cosas que no tengo. Carisma, contactos, pertenecer a un partido... Además, como has dicho, estudio Arte. No una carrera que tenga que ver con la política."
    mc "Tuvimos a Arnold como gobernador aquí. *Risa* No estoy seguro de que estudiara algo relacionado con la política."
    call BlinkXP ("c18s001_935" , "d") from _call_BlinkXP_2606
    lis "*Risa* Es verdad, los californianos sois raros. Elegís a un actor como gobernador."
    mc "*Risa* Los americanos somos raros. Elegimos a un actor como presidente... *Risa* Un actor que antes fue gobernador de California."
    lis "*Risa* Es verdad. Al menos él ganó la Guerra Fría. ¿Qué hizo Arnold?"
    mc "Permitirte beber alcohol esta noche. *Risa*"
    lis "*Risa* Punto para Arnold."
    if deb._var("route"):
        call BlinkXP ("c18s001_940" , "d") from _call_BlinkXP_2607
        lis "Sé que esto va a sonarte raro, pero ¿podemos hablar de Debbie?"
        mc "Lo que quieras. Es tu hermana y tienes todo el derecho a hablar de ella."
        call BlinkXP ("c18s001_945" , "d") from _call_BlinkXP_2608
        lis "Me preocupa cómo se siente. Cómo la haces sentir."
        mc "Ya te dije que no tengo intención de hacerle daño."
        call BlinkXP ("c18s001_950" , "d") from _call_BlinkXP_2609
        lis "Lo sé. Pero ayer, mientras me explicaba lo del lago... Nunca la había visto... la palabra que me viene a la cabeza es \"brillar\"... tanto como anoche."
        lis "Está muy ilusionada. Yo estoy muy contenta por ella, pero..."
        mc "Y te preocupa que acabe desilusionándola."
        call BlinkXP ("c18s001_955" , "d") from _call_BlinkXP_2610
        if mc._var("relationships") > 1:
            lis "Me ha dicho que estás saliendo con más chicas aparte de ella. Eso de por sí me desconcertó. Que lo hagas y que ella lo acepte me desconcierta aún más."
            mc "Sí, estoy saliendo con más chicas. Pero no engaño a nadie. Para mí, cada una de ellas es igual de importante."
        else:
            lis "Me preocupa que puedas acabar haciéndole daño sin querer. Sé que no vas a hacerlo a propósito."
            mc "Te prometo que voy a ir con todo el cuidado posible para evitar que eso pase."
        mc "Debbie es muy especial y la voy a tratar como se merece."
        if mc._var("relationships") > 1:
            call BlinkXP ("c18s001_960" , "d") from _call_BlinkXP_2611
            lis "¿Puedo preguntar cómo funciona eso de salir con más de una chica?"
            mc "Es muy fácil. Yo soy capaz de amar a diversas chicas a la vez. Pero cuando estoy con cualquiera de ellas, el resto no existe."
            mc "Cuando estaba con tu hermana en guardarropía, no importaba si salía con alguna de las chicas que había aquí fuera, en casa, o en cualquier otro lado."
            call BlinkXP ("c18s001_965" , "d") from _call_BlinkXP_2612
            lis "*Risa* Lo has dicho de una forma en que es imposible saber con quién más sales."
            mc "Cumplir con sus deseos es una forma de cuidarlas, Lisa."
            mc "Y ahora mismo, ninguna, incluyendo a Debbie, quiere hacer público lo nuestro."
            mc "Pero, sin querer molestarte, creo que tu pregunta va más allá... como si hubiera una cuestión personal tuya."
        else:
            call BlinkXP ("c18s001_960" , "d") from _call_BlinkXP_2613
            lis "¿Puedo preguntar si eres totalmente monógamo? Después de haber oído sobre tu relación con Saira..."
            mc "Por el momento lo soy. Estoy con Debbie y con nadie más. Pero no le hemos puesto ninguna etiqueta todavía."
            mc "Si me enamorara de otra persona, y esa persona quisiera estar conmigo, tendría que hablarlo con Debbie a ver cómo lo resolvemos."
            call BlinkXP ("c18s001_965" , "d") from _call_BlinkXP_2614
            lis "*Risa* Las famosas charlas de [mc], quien todo lo resuelve hablando."
            mc "Creo que hablar las cosas es la mejor forma de no hacer daño a nadie."
            mc "Pero, sin querer molestarte, lo preguntas como si quisieras que no fuera monógamo... por una cuestión tuya personal."
        mcp "(La conversación con Betty me está haciendo ver fantasmas donde quizás no los haya.)"
        call BlinkXP ("c18s001_970" , "h") from _call_BlinkXP_2615
        lis "¿Qué? ¡No! Sales con mi hermana... No podría salir contigo."
        mc "Nadie ha dicho nada de salir juntos tú y yo, pero..."
        mc "¿Me estás diciendo que si no saliera con Debbie te lo plantearías?"
        call BlinkXP ("c18s001_970b" , "d") from _call_BlinkXP_2616
        lis "Eso es algo que nunca sabremos, ¿no?"
    call BlinkXP ("c18s001_975" , "d") from _call_BlinkXP_2617
    play sound ("music/notification.ogg")
    kim "Lisa, tu móvil está sonando. Es Anthony."
    call BlinkXP ("c18s001_980" , "d") from _call_BlinkXP_2618
    lis "Tengo que cogerlo, [mc]. Seguimos hablando luego."
    mc "OK. ¿Podéis decirle a quién le toque ahora que voy a por un zumo a la barra? Vuelvo en un momento."
    lis "Le toca a [dap], pero no la veo por aquí. Estará en el lavabo. Pero ve, nosotras la avisamos."
    return
label c18s001_Daphne:
    if _in_replay:
        $ mc._var("relationships", 0, intention = "set")
        $ AuxReplay = 0
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
            "¿Estás en una relación con Debbie?"
            "Sí":
                $ deb._var("route" , True)
                $ mc._var("relationships", 1)
            "No":
                $ deb._var("route" , False)
        if mc._var("relationships") < 2:
            menu:
                "¿En cuántas relaciones estás?"
                "Más de una":
                    $ mc._var("relationships", 2, intention = "set")
                "Una o ninguna":
                    $ mc._var("relationships", 1, intention = "set")
        else:
            $ mc._var("relationships", 2, intention = "set")
        menu:
            "¿Bailaste con Lisa?"
            "Sí":
                $ Aux = False
            "No":
                $ Aux = True
    stop music fadeout (1.5)
    scene c18s002_005d with fade
    "Al volver con el zumo descubres que Anthony se ha unido a la fiesta y Lisa se lo está presentando al resto de chicas."
    play music ("music/Higher-Instrumental.ogg")
    scene c18s002_005e with dissolve
    pause (0.8)
    call BlinkXP ("c18s002_005" , "d") from _call_BlinkXP_2619
    if Aux:
        dap "Me han dicho que has desaparecido en el turno de Lisa. Voy a avisarla."
        mc "Mejor no. Está presentando a Anthony al resto de chicas. ¿A quién le toca ahora?"
        dap "A mí."
    else:
        dap "Es mi turno ahora, si no estás demasiado cansado."
        mc "Para ti nunca lo estoy."
    call BlinkXP ("c18s002_010" , "d") from _call_BlinkXP_2620
    mc "¿Qué tal te lo estás pasando en tu fiesta de cumpleaños?"
    dap "Genial, pero la fiesta es mañana. Falta demasiada gente hoy y no me parece una fiesta de verdad."
    mc "*Risa* Somos trece. Si cuentas a Anthony, catorce. La última vez que salimos éramos cinco."
    call BlinkXP ("c18s002_015" , "d") from _call_BlinkXP_2621
    dap "¡Las cosas han cambiado mucho en dos semanas! Y después de mañana... creo que nunca más sentiremos que una fiesta está completa a menos que estemos todas las chicas."
    mc "¿Las chicas? ¿Eso me deja fuera? *Risa*"
    call BlinkXP ("c18s002_020" , "d") from _call_BlinkXP_2622
    dap "Nunca te dejaría fuera. *Risa* Pero tú siempre estás para nosotras. No sé cómo puedes con todo."
    mc "Dividiendo el tiempo en pequeñas porciones. *Risa*"
    mc "Con esa app que habéis hecho Scarlett y tú puede ser más fácil."
    call BlinkXP ("c18s002_025" , "d") from _call_BlinkXP_2623
    if dap._var("route") and sca._var("route"):
        dap "La hicimos para dividirnos tu tiempo entre nosotras de tal forma que nunca discutiéramos. Solo ha habido que adaptarla."
        call c18s001_app2 from _call_c18s001_app2
    elif dap._var("route") or sca._var("route"):
        if mc._var("relationships") > 1:
            dap "La hicimos para que pudieras dividir tu tiempo entre el harén sin que nadie discutiera. Solo ha habido que adaptarla."
            call c18s001_app2 from _call_c18s001_app2_1
        else:
            call c18s001_app1 from _call_c18s001_app1
    else:
        call c18s001_app1 from _call_c18s001_app1_1
    mc "Ha sido una buena idea."
    if deb._var("route"):
        mc "Sobre el elefante en la habitación..."
        call BlinkXP ("c18s002_030" , "d") from _call_BlinkXP_2624
        dap "¿Debbie? No pasa nada. Me alegro mucho por vosotros. Es una chica genial."
        if dap._var("route"):
            dap "Hemos estado hablando en el lavabo. Ahora las dos sabemos que estás con la otra y a ninguna nos importa."
            if sca._var("route"):
                dap "Se me hace extraño saber de otra chica aparte de Scarlett, pero me alegra poder hablar de ello con Debbie."
            else:
                dap "Se me hace extraño saber de otra chica del harén, pero me alegra poder hablar de ello con Debbie."
        else:
            dap "Hemos estado hablando en el lavabo. Me ha pedido que guarde el secreto, que solo lo sabemos Lisa y yo."
            if sca._var("route"):
                dap "Se me hace extraño saber que estás con otra chica aparte de Scarlett, pero me alegra que sea Debbie."
        mc "Gracias por entenderlo. Se ha puesto muy nerviosa por un momento."
        call BlinkXP ("c18s002_035" , "d") from _call_BlinkXP_2625
        dap "¿Alguna chica más de la que tenga que saber? *Risa*"
        mc "Todas las chicas tenéis vuestros secretos, y no soy nadie para desvelarlos. *Risa*"
        dap "Tienes razón. *Risa* Seguramente te mataríamos entre todas si empiezas a hacerlo."
    if dap._var("route"):
        call BlinkXP ("c18s002_040" , "d") from _call_BlinkXP_2626
        dap "¿Sabes que estoy nerviosa por lo de mañana?"
        mc "¿A qué te refieres?"
        call BlinkXP ("c18s002_045" , "d") from _call_BlinkXP_2627
        dap "A la prueba de embarazo. Si sale positivo, me moriría de ganas por hacerlo público mañana mismo."
        dap "Y sería injusto para [eri] y [emm]. Voy a tener que guardar el secreto un par de días."
        mc "¿Y si sale negativo? ¿Te fastidiaría el cumpleaños?"
        call BlinkXP ("c18s002_050" , "d") from _call_BlinkXP_2628
        dap "No, si sale negativo no pasa nada. Nunca pensé que me quedaría embarazada a los 18. Ni siquiera antes de los 25."
        dap "Quiero tener a Maeve, pero no tengo demasiada prisa. No todas las chicas sueñan con quedarse embarazadas en su primera vez."
        mc "Esa debe ser la actitud."
    call BlinkXP ("c18s002_055" , "d") from _call_BlinkXP_2629
    dap "¿Quién crees que va a hacer topless mañana?"
    mc "Estoy casi seguro de que tu madre, [emm], y [eri]. Del resto no tengo ni idea. Quizás Sam y Eileen."
    call BlinkXP ("c18s002_060" , "d") from _call_BlinkXP_2630
    dap "¿[eri]? Estás loco."
    mc "Ella lo ha pedido para tu madre y va a querer apoyarla. Pero creía que ya se lo habrías preguntado a las chicas. Al menos a las que están aquí."
    call BlinkXP ("c18s002_065" , "d") from _call_BlinkXP_2631
    dap "Nadie se ha atrevido a sacar el tema. Incluso Scarlett ha cambiado de tema cuando he intentado dirigir la conversación hacia mañana."
    dap "Creo que la presencia de Jamaal las cohíbe un poco a todas. No lo conocen tanto como nosotros."
    mc "¿Jamaal? Creo que los únicos pezones que le podrían interesar de los que hay aquí serían los de Anthony y no sé si Anthony estaría interesado. *Risa*"
    call BlinkXP ("c18s002_070" , "d") from _call_BlinkXP_2632
    dap "¿Los tuyos no? *Risa*"
    mc "Jamaal sabe que no me van los tíos igual que yo sé que no le van las chicas. Nunca me vería así. Es como mi hermano."
    call BlinkXP ("c18s002_075" , "d") from _call_BlinkXP_2633
    if dap._var("route"):
        dap "*Risa* Y yo soy tu prima. Y eso no nos ha importado."
    else:
        dap "*Risa* ¿Estás seguro? Piensa que nadie elige de quién se enamora."
    mc "No me refiero a eso, sino a que SOLO me ve como a su hermano, no como un objetivo."
    call BlinkXP ("c18s002_080" , "d") from _call_BlinkXP_2634
    dap "¿Y tú? ¿Estás interesado en algunos pezones?"
    if dap._var("route"):
        mc "Principalmente en volver a ver los tuyos. Pero preferentemente en privado."
    else:
        mc "Soy un hombre de 21 años. *Risa* En todos. Es broma."
    dap "*Tsk* Sí, sí. Pero ¿alguna chica en particular mañana? Siempre has tenido un crush con Samantha."
    mc "Nadie en particular. Creo que no hay que sexualizar algo así. Es algo que [eri] pidió por [nor], para ir acostumbrando a la abuela."
    call BlinkXP ("c18s002_085" , "d") from _call_BlinkXP_2635
    dap "Me extraña tanto que la abuela no haya protestado. No me la imagino enseñando las tetas delante tuyo, pero tampoco aceptando que otras chicas lo hagan."
    dap "Por no hablar de Tía Betty. Es más cool de lo que recordaba, pero..."
    mc "Tía Betty se apuntaría a cualquier cosa que incomodara a Meemaw. *Risa* Si cree que la va a sacar de sus casillas, es capaz de hacer topless mañana."
    call BlinkXP ("c18s002_090" , "d") from _call_BlinkXP_2636
    dap "En eso tienes razón. Parece que siempre están discutiendo."
    mc "Tienen formas diferentes de ver las cosas, aunque Meemaw cada vez ladra menos."
    play sound ("music/notification.ogg")
    "Un móvil suena en alguna parte."
    call BlinkXP ("c18s002_095" , "d") from _call_BlinkXP_2637
    dap "Creo que con esto acaba mi tiempo. Te veo en la segunda ronda. Te toca con Megan. La habíamos programado para su descanso."
    stop music fadeout (1.5)
    mc "Te veo luego."
    return
label c18s001_app1:
    dap "La teníamos hecha para distribuirnos el tiempo de laboratorio en el instituto. Solo ha habido que adaptarla."
    return
label c18s001_app2:
    dap "Queríamos enseñártela cuando estuviera acabada, aún le quedan unos retoques, pero para esta noche ya nos servía."
    return
label c18s001_Kim:
    if _in_replay:
        menu:
            "¿Intentaste besar a Kim en el Verdad o Reto en la playa?"
            "Sí":
                $ kim._var("kissedBeach" , True)
            "No":
                $ kim._var("kissedBeach" , False)
        menu:
            "¿Cuántos Puntos de Relación tienes con Kim?"
            "Mas de 6":
                $ kim._var("relationshipPoints", 6, intention = "set")
            "Entre 0 y 5":
                $ kim._var("relationshipPoints", 5, intention = "set")
            "Entre -5 y 0":
                $ kim._var("relationshipPoints", -5, intention = "set")
            "Menos de -5":
                $ kim._var("relationshipPoints", -15, intention = "set")
    $ Aux = True
    scene c18s002_100d with dissolve
    play music ("music/Memories-Instrumental.ogg")
    "Buscas a Megan por la sala y no está en ningún sitio."
    call BlinkXP ("c18s002_100" , "d") from _call_BlinkXP_2638
    kim "Megan se ha tenido que ir, con lo que ahora es mi turno, si aún te quedan ganas de bailar."
    if kim._var("kissedBeach") or kim.rps > 6:
        mc "Perfecto. Tenemos que continuar la conversación de anoche."
    else:
        if persistent.walkthrough:
            $ wt1 = "Kim +5"
            $ wt2 = "Kim -5"
        else:
            $ wt1 = ""
            $ wt2 = ""
        menu:
            "Por supuesto." (wt = wt1):
                $ kim.rp(5)
                $ Aux = False
            "Estoy cansado." (wt = wt2):
                $ kim.rp(-5)
                mc "Creo que voy a ir a sentarme un rato."
                kim "Es normal. Llevas toda la noche de chica en chica."
                $ resetWalkthrough ()
                return
        $ resetWalkthrough ()
    if Aux:
        call BlinkXP ("c18s002_105" , "d") from _call_BlinkXP_2639
        kim "Ya te dije que no había nada de lo que hablar."
        mc "Y dijiste que esto de estar formando una familia podría evitar que tú y yo... y ahí lo dejaste."
        call BlinkXP ("c18s002_110" , "d") from _call_BlinkXP_2640
        kim "No debería haberlo dicho."
        mc "Sabes que, aunque estemos formando una familia, los típicos tabús familiares no se nos aplican, ¿verdad? A ti y a mí."
        if kim.rps > 6:
            mc "Con el beso de la playa dijiste que te sentías atraída por mí."
        if kim._var("kissedBeach"):
            mc "Y con mi beso te dije que yo me sentía atraído por ti."
        mc "¿Dónde ves el problema?"
        call BlinkXP ("c18s002_115" , "d") from _call_BlinkXP_2641
        kim "El problema lo veo en que estamos formando una familia. No voy a decir que te vea como a un hermano ni nada por el estilo."
        kim "Eres... un miembro más de la familia. Pero también lo es [mar], y no sé cómo vería que me liara con su hijo."
        mc "No creo que la opinión de mi madre tenga que influir en lo que hagamos tú y yo."
        call BlinkXP ("c18s002_120" , "d") from _call_BlinkXP_2642
        kim "No lo entiendes. Pero influye."
        if kim.rps > 0:
            kim "Me gustas, pero tengo que pensar si debo actuar sobre esos sentimientos."
        else:
            kim "Aún no sé si me gustas o me caes mal. Depende del día... pero tengo que pensar si debo actuar sobre esos sentimientos, si es que los tengo."
        mc "Lo entiendo. Una cosa es lo que crea yo y otra diferente lo que creas tú."
        kim "¿Podemos cambiar de tema?"
        mc "Por supuesto."
    call BlinkXP ("c18s002_125" , "d") from _call_BlinkXP_2643
    mc "Mañana es el fin de la locura. No me malinterpretes, adoro los cumpleaños de las chicas, especialmente después de haberme perdido los últimos tres..."
    kim "*Risa* Pero es agotador. Los últimos dos días parece que la vida en casa ha girado en torno a [emm], [eri], [dap] y sus cumpleaños."
    kim "Incluso la llegada de Eva y Amanda parecía un regalo anticipado para ellas."
    mc "Siempre ha sido un fin de semana especial. Pero este año todo parece sobredimensionado."
    call BlinkXP ("c18s002_130" , "d") from _call_BlinkXP_2644
    kim "Yo las entiendo. Este año estás tú. Están Amanda y Eva. Están Olivia y Betty. Estamos nosotras. Y son el centro de atención de todas."
    kim "Es como sus cumpleaños de siempre pero hasta las cejas de esteroides."
    mc "*Risa* Creo que no lo habría podido expresar mejor."
    call BlinkXP ("c18s002_135" , "d") from _call_BlinkXP_2645
    kim "Espero haber acertado con los regalos. Es complicado acertar... y no podía gastar mucho hasta que no me paguen por el trabajo de la semana que viene."
    mc "No creo que miren el valor sino la intención."
    kim "Eso espero..."
    call BlinkXP ("c18s002_140" , "d") from _call_BlinkXP_2646
    kim "¡Oh! Acabo de darme cuenta... ¿También son los cumpleaños de Eva y Amanda?"
    mc "No, fueron hace un mes más o menos."
    call BlinkXP ("c18s002_145" , "d") from _call_BlinkXP_2647
    kim "Menos mal... no les había comprado nada."
    mc "Aunque fueran sus cumpleaños, lo entenderían. Las conociste ayer. Pero no te preocupes. Solo son tres cumpleaños. Solo."
    call BlinkXP ("c18s002_150" , "d") from _call_BlinkXP_2648
    kim "Ayer... parece que ha pasado una vida entera, pero ayer hizo una semana que llegamos."
    kim "Mudarme a Newport es la mejor decisión que he tomado en mucho tiempo."
    kim "Vine por el calor y he encontrado el calor de una familia."
    mc "Eso te ha quedado... casi poético. Me alegra que te sientas así."
    mc "Tu familia de Cleveland... ¿has hablado con ellos?"
    call BlinkXP ("c18s002_155" , "d") from _call_BlinkXP_2649
    kim "Hablo todos los días y se lo he explicado todo... bueno, menos La Clonversación... y alguna cosa más."
    kim "Alucinan cuando les hablo de la familia. Dicen que nunca me habían visto adaptándome tan rápido a un sitio."
    mc "¿Te costaba adaptarte? No lo entiendo, eres muy sociable."
    call BlinkXP ("c18s002_160" , "d") from _call_BlinkXP_2650
    kim "Soy muy sociable porque lo ponéis muy fácil. Nadie juzga a nadie... bueno, quizás Olivia un poco."
    kim "Nadie hace comentarios para hacer daño a nadie. Todo el mundo ayuda a todo el mundo en lo que puede."
    kim "Y después estás tú. Parece que estás en todos sitios cuando alguna de nosotras te necesitamos."
    mc "Era una de mis funciones cuando erais solo clientas... eso ha sonado muy mal. *Risa*"
    mc "Ahora, además, lo hago por pasar tiempo con vosotras."
    call BlinkXP ("c18s002_165" , "d") from _call_BlinkXP_2651
    kim "Y nosotras te lo agradecemos. Mucho."
    kim "Es difícil tener una conversación con cualquiera de las chicas en la que no se hable de ti tarde o temprano."
    kim "No es que seas el centro de cada conversación, aún estamos en ese momento en que nos quedan planes y sueños que compartir, pero sueles aparecer en muchas de ellas."
    mc "*Risa* No sé si sentirme halagado o estudiado."
    call BlinkXP ("c18s002_170" , "d") from _call_BlinkXP_2652
    kim "*Risa* Halagado, por supuesto. Eres el único chico en una familia de mujeres."
    kim "Tengo ganas de conocer al tal Jamaal mañana, aunque puede cohibir a alguna de las chicas para ir en topless... o desnudas en el jacuzzi. Más incluso de lo que las cohíbes tú."
    mc "Jamaal es muy buen tío, pero no va a estar interesado en vosotras. Se pasará el día comiendo y metiéndose conmigo. Además, no puede subir las escaleras del jacuzzi. *Risa*"
    mc "¿Y yo os cohíbo? No lo había pensado."
    call BlinkXP ("c18s002_175" , "d") from _call_BlinkXP_2653
    kim "Algunas de nosotras somos conscientes de nuestro aspecto. No te voy a decir quiénes."
    kim "Desnudarse, aunque sea parcialmente delante de un chico, siempre es un paso importante. Especialmente si ese chico te gusta."
    mc "Bueno, si ese chico le gusta a alguien, todo el mundo sabe que a ese chico le gusta hablar las cosas. Especialmente si eso supone un problema."
    call BlinkXP ("c18s002_180" , "d") from _call_BlinkXP_2654
    kim "Quizás demasiado. A veces muy poco."
    mc "¿A qué te refieres?"
    play sound ("music/notification.ogg")
    "Un móvil suena en algún sitio."
    $ Aux = False
    if kim.rps > 0 and kim._var("kissedBeach"):
        $ Aux = True
    if kim.rps > 6:
        $ Aux = True
    if Aux:
        call BlinkXP ("c18s002_185" , "d") from _call_BlinkXP_2655
        kim "Te he dicho que me gustas y me has dejado cambiar de tema."
        mc "Me lo has pedido tú."
        call BlinkXP ("c18s002_190" , "d") from _call_BlinkXP_2656
        kim "Lo sé. Pero casi esperaba que siguieras hablando... que me intentaras convencer para que tomara una decisión..."
        kim "Ahora ha pasado el momento, pero en ese momento lo esperaba."
        mc "No voy a forzarte a tomar una decisión, Kim. Es algo que tienes que pensar tú y llegar a tus propias conclusiones."
        call BlinkXP ("c18s002_195" , "d") from _call_BlinkXP_2657
        kim "Ni siquiera me has dicho que yo también te gusto..."
        if kim._var("kissedBeach"):
            mc "Creo que ya te lo demostré en la playa."
        else:
            mc "Eres preciosa, Kim."
        mc "Pero yo tampoco he decidido si siento algo por ti más allá de... eso. Tan solo pensaba que debíamos hablarlo."
    else:
        call BlinkXP ("c18s002_185" , "d") from _call_BlinkXP_2658
        kim "A nada... "
        mc "A algo te tienes que estar refiriendo..."
    call BlinkXP ("c18s002_200a" , "d") from _call_BlinkXP_2659
    kat "Creo que es mi turno, Kim."
    call BlinkXP ("c18s002_200b" , "d") from _call_BlinkXP_2660
    kim "Todo para ti, Kate."
    kim "Te veo en mi siguiente turno, [mc]."
    mc "Hasta ahora, Kim."
    return
label c18s001_Common:
    if _in_replay:
        menu:
            "¿En cuántas relaciones estás?"
            "Más de una":
                $ mc._var("relationships", 2, intention = "set")
            "Una":
                $ mc._var("relationships", 1, intention = "set")
            "Ninguna":
                $ mc._var("relationships", 0, intention = "set")
    stop music fadeout (1.5)
    scene c18s002_205An # diversas imágenes d-Eri-e-dap-lis-a-kim-eva-b-emma-sca-c-
    "La noche continua con diversos bailes y conversaciones."
    play music ("music/Looking-Forward.ogg")
    "Pierdes la cuenta de cuántas veces has bailado con cada una de ellas y de los bailes en grupo que habéis hecho."
    "Pero el cansancio va haciendo mella en algunas de las chicas y decidís retiraros antes de que el Jazz Corner cierre."
    scene c18s002_205aa with fade
    "Os despedís de Megan y de Anthony y volvéis a casa."
    scene c18s002_205ab with fade
    "Llegáis a casa para dejar a las chicas y el coche que conduce Amanda."
    scene c18s002_210An with fade
    "Continuáis con una larga despedida."
    "Todas las chicas se abrazan mientras otras esperan su turno para darte el beso de buenas noches."
    scene c18s002_205ac with fade
    "Amanda y Eva se suben a tu pick up y las llevas a la base."
    "Casi estabas seguro de que se iban a pelear por quién se sienta delante."
    "Para tu sorpresa, no lo hacen y Amanda se sienta en el asiento delantero."
    stop music fadeout (1.5)
    scene c18s002_205ad with fade
    "Unos minutos después..."
    play music ("music/Majestica.ogg")
    mc "Bueno, aquí ha acabado la noche. Nos vemos mañana."
    ama "¿No tenemos beso de buenas noches?"
    "" (multiple=2)
    eva "Todas lo han tenido..." (multiple=2)
    mc "Escuchad. No quiero ser la causa de un problema entre vosotras. O entre vosotras y el resto de las chicas."
    mc "Sé que esto es nuevo para vosotras y también lo es para mí."
    mc "Creo que tenéis que hablar y marcar unos límites que las dos vayáis a respetar."
    call BlinkXP ("c18s002_215" , "d") from _call_BlinkXP_2661
    eva "¿A qué clase de límites te refieres?"
    mc "No te puedes enfadar porque Amanda me dé un beso una décima de segundo más largo que el tuyo."
    call BlinkXP ("c18s002_220" , "d") from _call_BlinkXP_2662
    mc "Y tú no puedes echarle en cara a tu {b}hermana{/b} que se haya puesto un vestido precioso."
    ama "Lo sé..."
    mc "Sé que os gusto... al menos físicamente. Pero {b}nunca{/b} os peleéis por un chico. Ni por nadie."
    mc "No vale la pena perder lo que tenéis por nada ni por nadie. Mucho menos por mí."
    scene c18s002_225a with dissolve
    ama "Hemos hablado en el Jazz Corner..."
    "" (multiple = 2)
    eva "Aún tenemos que pulir unos temas..." (multiple = 2)
    ama "Pero tienes razón..."
    "" (multiple = 2)
    eva "No vamos a volver a discutir por ti..." (multiple = 2)
    mc "Ni por nadie."
    scene c18s002_225b with dissolve
    ama "Ni por nadie..." (multiple=2)
    eva "Ni por nadie..." (multiple=2)
    call BlinkXP ("c18s002_230" , "d") from _call_BlinkXP_2663
    ama "Las dos queremos estar contigo. Pero yo no quiero perder a mi hermana."
    ama "No te ofendas, pero prefiero estar sin ti que sin Eva."
    mc "No me puedo ofender por eso. Es lógico."
    call BlinkXP ("c18s002_235" , "d") from _call_BlinkXP_2664
    eva "A mí me pasa lo mismo. Me puedo imaginar una vida sin ti, pero no sin Amanda."
    if mc._var("relationships") > 1:
        eva "Sabemos que, con tu harén, esto no es un problema para ti, pero es nuevo para nosotras."
    elif mc._var("relationships") == 1:
        eva "Sabemos que estás con alguien y no vemos cómo podemos encajar o incluso si podemos. Como has dicho, esto es nuevo para nosotras."
    else:
        eva "Sabemos la relación que tenías con Saira en Portland y no sabemos si podríamos tener algo así. Como has dicho, esto es nuevo para nosotras."
    eva "Ni siquiera sabemos si tú quieres tener algo con alguna de nosotras... o con las dos... No contestes."
    call BlinkXP ("c18s002_240" , "d") from _call_BlinkXP_2665
    ama "Se nos han ocurrido un par de ideas. A las dos nos gustas... y no sólo físicamente."
    ama "Tenemos que hablar entre nosotras a ver cómo actuamos sobre ello. Pero no va a haber más discusiones."
    mc "Me parece una buena idea, ya sabéis que..."
    scene c18s002_225c with dissolve
    ama "Hay que hablarlo todo. *Risa*" (multiple=2)
    eva "El método [mc]. *Risa*" (multiple=2)
    mc "*Risa* Sí, exactamente."
    mc "Os voy a dejar hablar sobre lo que tengáis que hablar. Vamos con esos besos."
    scene c18s002_225d with dissolve
    ama "Empieza tú, Eva."
    "" (multiple=2)
    eva "No, no, empieza tú." (multiple=2)
    scene c18s002_225An with dissolve # 225e, 245a
    "Coges a Eva de los hombros y la giras hacia ti."
    call KissXP ("c18s002_245" , "d") from _call_KissXP_78
    mc "Buenas noches, Eva."
    eva "Buenas noches, [mc]."
    call KissXP ("c18s002_250" , "d") from _call_KissXP_79
    mc "Buenas noches, Amanda."
    ama "Buenas noches, [mc]."
    scene c18s002_225f with dissolve
    eva "*Susurrando* ¡Ha empezado por mí!"
    ama "*Susurrando* ¡Ha dejado lo mejor para el final!"
    scene c18s002_225g with dissolve #las chicas no están
    mcp "(*Risa mental* Lo de estás chicas es increíble. Pueden ser todo un problema.)"
    mcp "(Tan solo espero que cumplan lo que han dicho y dejen de discutir.)"
    scene c13s001_085 with fade #puerta de habitación
    "Vuelves a casa y subes a tu habitación sin encender las luces. Es tarde y no quieres despertar a nadie."
    stop music fadeout (1.5)
    return
label c18s002_NoSaira:
    scene c18s002_300a with dissolve
    "Llegas sin sueño a tu habitación y decides jugar un rato a My Residence."
    "Hoy toca una escena con Aishwarya."
    return
label c18s002_Saira:
    if _in_replay:
        $ mc._var("relationships", 1, intention = "set")
        $ AuxReplay = 0
        menu:
            "¿Estás en una relación con Scarlett?"
            "Sí":
                $ sca._var("route" , True)
                $ mc._var("relationships", 1)
                menu:
                    "¿Estás en una relación con Eileen?"
                    "Sí":
                        $ eil._var("route" , True)
                        $ mc._var("relationships", 1)
                    "No":
                        $ eil._var("route" , False)
            "No":
                $ sca._var("route" , False)
        if mc._var("relationships") < 2:
            menu:
                "¿En cuántas relaciones estás?"
                "Más de una":
                    $ mc._var("relationships", 2, intention = "set")
                "Una":
                    $ mc._var("relationships", 1, intention = "set")
    scene c18s002_300b with dissolve
    "Al entrar en tu habitación te encuentras con que hay alguien en tu cama."
    mcp "(¿Saira? ¿Qué hace aquí? ¿Está dormida?)"
    mcp "(¿Cama o sofá? Si se ha quedado dormida no quiero despertarla.)"
    scene c18s002_300c with dissolve
    "Empiezas a desnudarte, intentando ser lo más silencioso posible."
    "Ha dejado su vestido y joyería en el sofá."
    mcp "(Pues va a ser cama. Si empiezo a mover todo esto, es probable que alguna de sus pulseras acabe cayendo al suelo y despertándola.)"
    "Cuando ya te has desnudado..."
    call BlinkXP ("c18s002_305" , "d") from _call_BlinkXP_2666
    sai "*Susurrando* ¿[mc]? Has tardado mucho en volver... me he quedado dormida..."
    mc "*Susurrando* Las cosas se han complicado con Eva y Amanda. Vuelve a dormir."
    sai "*Susurrando* No, enciende una luz... me has dicho que tomara la iniciativa y es lo que voy a hacer."
    call BlinkXP ("c18s002_310" , "d") from _call_BlinkXP_2667
    play music ("music/Sexy-Background-Music.ogg")
    mc "*Susurrando* Dijiste que no querías hacer nada con las otras chicas en la casa..."
    sai "*Susurrando* Eso fue antes de esta noche. Bailar contigo, tenerte entre mis brazos... No hay nadie durmiendo debajo hasta que vuelva Megan."
    sai "*Susurrando* Nadie se va a enterar si no me haces gritar demasiado fuerte."
    mc "*Susurrando* No puedo prometer nada. *Risa*"
    call BlinkXP ("c18s002_315" , "d") from _call_BlinkXP_2668
    sai "*Susurrando* Ven aquí. Hace mucho que no compartimos cama..."
    mc "*Susurrando* Esa es una oferta que no voy a poder rechazar."
    scene c18s002_315An with dissolve #def
    sai "*Susurrando* Entonces no te lo pienses más. Te estoy esperando."
    scene c18s002_320pv with dissolve
    show c18s002_320v with dissolve
    "Vuestros labios se juntan ansiosos, mientras vuestras manos recorren vuestros cuerpos con la misma o más ansia."
    "Las manos quieren su ración de piel. Los labios se han encontrado con anterioridad."
    "Los dedos hacen meses que no tocan la piel del otro."
    scene c18s002_325pv with dissolve
    hide c18s002_320v
    show c18s002_325v with dissolve
    "Puedes notar como sus enormes tetas de pezones erectos se frotan levemente contra tu pecho en los suaves movimientos del prolongado beso."
    "No tardas en sentir cómo tu erección empieza a crecer. Volver a tener el cuerpo de Saira entre tus brazos es maravilloso."
    sai "*Gemido*"
    scene c18s002_330pv with dissolve
    hide c18s002_325v
    show c18s002_330v with dissolve
    "Introduces tu muslo entre los suyos, presionando su entrepierna y notando el calor que sale de ella."
    sai "*Jadeo*"
    "También puedes notar lo húmeda que está. No eres el único que se ha puesto cachondo con el roce de vuestras manos."
    call BlinkXP ("c18s002_335" , "d") from _call_BlinkXP_2669
    hide c18s002_330v
    sai "*Susurrando* He echado mucho de menos esto. *Gemido* Sigues siendo tan bueno como siempre."
    mc "*Susurrando* Tú tampoco has perdido un ápice de tus talentos con esa lengua. *Risa*"
    sai "*Susurrando* Y puedo notar en mi estómago que ya estás preparado para mí."
    call BlinkXP ("c18s002_340" , "d") from _call_BlinkXP_2670
    sai "*Susurrando* ¿Te importa si pasamos de los preliminares?"
    sai "*Susurrando* También he echado de menos a mi bebé."
    mc "*Susurrando* Creo que es la primera vez que quieres saltarte los juegos previos. Siempre te han encantado."
    call BlinkXP ("c18s002_345" , "d") from _call_BlinkXP_2671
    sai "*Susurrando* Es la primera vez que tengo que volver a mi cama antes de que mi compañera de habitación vuelva de trabajar. *Risita*"
    mc "*Susurrando* Me parece una buena razón."
    sai "*Susurrando* Déjame darme la vuelta..."
    scene c18s002_350pv with dissolve
    "Saira se tumba en su posición favorita, apoyando su espalda en tu pecho."
    "Tu glande apuntando a su entrada."
    mc "*Susurrando* ¿Preparada?"
    sai "*Susurrando* Cuando quieras..."
    scene c18s002_350dv
    $ renpy.movie_cutscene ("c18/c18s002_350vid.webm", loops = 0)
    "Penetras a Saira en un movimiento rápido."
    sai "¡Ooof! ¡Cómo he echado de menos esto!"
    "Se acabaron los susurros."
    mc "*Susurrando* ¿Estás bien?"
    call BlinkXP ("c18s002_370a" , "d") from _call_BlinkXP_2672
    sai "Es imposible estar mejor. Estoy en los brazos del hombre al que amo."
    mc "*Susurrando* Y yo tengo a la mujer más bonita del mundo entre los míos."
    call BlinkXP ("c18s002_370b" , "d") from _call_BlinkXP_2673
    sai "No hace falta que sigas susurrando. *Risa* He sido una ilusa pensando que iba a poder aguantar los gemidos."
    mc "*Risa* Nunca has sido de gemir bajito. Lo más probable es que Megan se entere en el Jazz Corner. Con la música puesta. Mientras canta."
    call BlinkXP ("c18s002_370c" , "d") from _call_BlinkXP_2674
    sai "*Risa* Eres un exagerado. Pero eres MI exagerado."
    sai "Puedes empezar a moverte cuando quieras."
    scene c18s002_355pv with dissolve
    show c18s002_355v with dissolve
    "Tus caderas conocen el camino como si lo hubieran recorrido ayer. Tu cuerpo conoce cada movimiento que le va a proporcionar el deseado placer a Saira."
    sai "*Gemido* ¡Cuatro días esperando esto! *Jadeo* ¡Ha valido la pena!"
    "Es como montar en bicicleta. Da lo mismo que haga más de un mes de vuestra última vez juntos. Son cosas que no se olvidan."
    sai "*Jadeo* ¡Más rápido! *Gemido* ¡Quiero tu leche dentro de mí!"
    "Ansiosa como siempre, pero esta vez con una sensación de urgencia."
    mc "Y yo quiero que dure, mi vida."
    scene c18s002_360pv with dissolve
    hide c18s002_355v
    show c18s002_360v with dissolve
    "Su coño no está de acuerdo. Abraza toda la longitud de tu polla a cada embestida, como si no quisiera dejarte ir."
    sai "*Gemido* Pero... Megan... *Jadeo* va a llegar en breve..."
    "Está demasiado preocupada por acabar antes de que llegue Megan. No es lo que querías para vuestra primera vez juntos después de tanto tiempo."
    sai "*Jadeo* No quiero que sepa que me he acostado contigo..."
    "No. No vas a consentir que un momento así se estropee por las prisas."
    mc "¿Quién es Megan? No existe nadie en este mundo aparte de ti. De nosotros."
    scene c18s002_370j with hpunch
    if sca._var("route") or eil._var("route"):
        "Saira por fin se da cuenta de cómo funciona el harén. Por fin comprende que, en este momento, no hay nadie más en la casa, en tu vida, aparte de ella."
    else:
        "Saira por fin se da cuenta de cómo funciona vuestra nueva relación. Por fin comprende que, en este momento, no hay nadie más en la casa, en tu vida, aparte de ella."
    scene c18s002_365pv with dissolve
    hide c18s002_360v
    show c18s002_365v with dissolve
    "Continúas embistiendo con tus caderas, usando a Mjolnir como ariete, sin dejarle pensar. Podría haber replicado si hubieras parado."
    sai "*Gemido* ¡Tienes razón! *Jadeo*"
    "Su actitud cambia tras esa frase, mucho más relajada, centrada en disfrutar el momento. Y lo disfruta."
    mc "Solo tú y yo, mi amor."
    "Sigues bombeando, embelesado por el hipnótico movimiento de sus tetas en cada embestida. Has salvado el momento."
    sai "*Jadeo* Solo tú y yo."
    "Su cuerpo se empieza a tensar. Sabes que su orgasmo se está acercando, aunque aún le queda un poco. Te preparas para la llegada de su clímax mientras mantienes un ritmo constante."
    sai "Para un momento, por favor."
    call BlinkXP ("c18s002_370d" , "d") from _call_BlinkXP_2675
    "La petición te pilla por sorpresa."
    mc "¿Pasa algo? Me ha parecido que estabas a punto."
    sai "Lo estoy. Quiero ponerme arriba."
    mc "Me encanta..."
    scene c18s002_395pv with fade
    hide c18s002_365v
    "Saira realiza el cambio de posición rápidamente."
    "Sabes que ella siempre ha disfrutado de tener el control estando arriba. Desearías que no te diera la espalda."
    "Pero también sabes que vas a disfrutar cada segundo de ello, cada cambio de ritmo."
    show c18s002_395v with dissolve
    "Saira empieza a moverse violentamente. No quiere perder su inminente orgasmo."
    sai "*Gemido* ¡Oh, sí! *Jadeo* Esto es increíble."
    "En esta posición, sin apenas control sobre el ritmo, ella es una diosa que te sorprende con sus cambios de ritmo."
    sai "*Jadeo* No voy a aguantar mucho... *Gemido* Corrámonos juntos..."
    "Por muy excitante y placentero que sea, a ti aún te queda mucho por llegar."
    mc "Córrete para mí, mi vida. A mí me falta un poco."
    scene c18s002_390pv with dissolve
    hide c18s002_395v
    show c18s002_390v with dissolve
    "Puedes notar cómo tensa sus músculos vaginales, intentando contener el orgasmo, estrujando tu polla con ellos."
    sai "*Gemido* No... *Jadeo* Creo que puedo aguantar un rato aún."
    "Lo intenta, pero sus movimientos son cada vez más erráticos. Tensar sus músculos hace que las sensaciones para ella también sean más intensas."
    sai "*Jadeo* Un poco al menos..."
    "Sabes que no es cierto. Su orgasmo está llamando a las puertas y lo puedes notar en cómo tensa los brazos en cada recorrido."
    call OrgasmX ("c18s002_375") from _call_OrgasmX_53
    sai "*GEMIDO* ¡SÍ! ¡Oh, por favor! *JADEO* ¡Es ENORME!"
    "Sus músculos se ponen tan rígidos que parece que se va a romper en mil pedazos antes de liberar toda la tensión acumulada."
    "Ahora es cuando lo mejor está por llegar."
    scene c18s002_405pv with dissolve
    hide c18s002_390v
    show c18s002_405v with dissolve
    "Con movimientos espasmódicos, Saira continua la cabalgata. Más violentamente que antes si cabe."
    sai "*JADEO* ¡Te quiero! *GEMIDO* ¡Cómo te he echado de menos!"
    "Siempre te ha sorprendido lo mucho que Saira es capaz de hablar durante sus orgasmos, su capacidad para construir frases coherentes."
    sai "*GEMIDO* ¡Llegan más! *JADEO*"
    "Y su capacidad para tener múltiples orgasmos en una rápida sucesión."
    "Sus paredes vaginales casi se notan como si estuvieran en modo vibración. Sus orgasmos llegan uno tras otro, sin darle tiempo apenas a un par de movimientos entre ellos."
    scene c18s002_400pv with dissolve
    hide c18s002_405v
    show c18s002_400v with dissolve
    "Su coño sigue abrazando, exprimiendo, ordeñando, y estrujando tu polla cada vez que baja, liberándola de la presión por un breve instante antes de volver a empezar."
    sai "*JADEO* Es el mejor sexo que hemos tenido."
    "Las ganas acumuladas, el placer del reencuentro, hacen que sea especial. ¿El mejor? No estás seguro."
    mc "Tendremos que dejar un par de meses hasta el siguiente, si la espera te hace disfrutarlo tanto. *Risa*"
    sai "*GEMIDO* No me hagas reír mientras... *JADEO* subo y bajo o me voy a quedar sin respiración. *Risa ahogada*"
    "Reír y gemir al mismo tiempo. Esta chica tiene habilidades sorprendentes."
    "Pero la risa ha producido aún más vibraciones en su vagina, acercándote peligrosamente a tu límite."
    mc "Me queda muy poco, Saira."
    call BlinkXP ("c18s002_420" , "d") from _call_BlinkXP_2676
    sai "Espera, no te corras aún..."
    mc "¿Por qué? ¿Ahora te pones dominante? *Risa*"
    call BlinkXP ("c18s002_425" , "d") from _call_BlinkXP_2677
    sai "Quiero... quiero verte la cara mientras te corres... quiero que veas la mía mientras me corro."
    mc "Eso es nuevo, va a ser la primera vez."
    call BlinkXP ("c18s002_430" , "d") from _call_BlinkXP_2678
    sai "Ya no tengo miedo de enamorarme de ti."
    sai "Ya lo estoy."
    mc "Eso es de lo más bonito que me has dicho nunca."
    call BlinkXP ("c18s002_435" , "d") from _call_BlinkXP_2679
    sai "Sólo te pongo una condición... no te puedes reír si pongo caras raras cuando tenga otro orgasmo."
    mc "*Risa* Prometido."
    sai "Estoy hablando en serio..."
    mc "No creo que pongas caras extrañas, y si las pones no va a ser cosa de risa. Prometido."
    call BlinkXP ("c18s002_440" , "f") from _call_BlinkXP_2680
    "Saira cambia hábilmente de posición."
    "Sabes que la intimidad de poder mirarle a los ojos... poder miraros mutuamente por primera vez mientras hacéis el amor es un paso importante para ella."
    sai "¿Preparado?"
    mc "Para ti, siempre."
    call BlinkXP ("c18s002_445" , "d") from _call_BlinkXP_2681
    sai "Recuerda... nada de reírte."
    mc "Te lo he prometido, Saira."
    scene c18s002_450dv
    $ renpy.movie_cutscene ("c18/c18s002_450vid.webm", loops = 0)
    "Saira se empala en tu polla en un movimiento rápido. Entras con facilidad debido a la humedad de sus orgasmos anteriores."
    "Su coño es un segundo hogar para Mjolnir."
    sai "*Gemido*"
    "Se detiene un momento y te mira directamente a los ojos."
    call BlinkXP ("c18s002_455" , "d") from _call_BlinkXP_2682
    hide c18s002_450v
    sai "¿Estás bien?"
    mc "*Risa* Perfectamente. ¿Y tú?"
    call BlinkXP ("c18s002_460" , "d") from _call_BlinkXP_2683
    sai "Te he dicho que nada de risas..."
    mc "Nada de risas sobre tu cara. Pero es que esa pregunta me ha hecho mucha gracia."
    mc "Me acuerdo de nuestras primeras veces, que siempre te lo preguntaba yo. *Risa*"
    call BlinkXP ("c18s002_465" , "d") from _call_BlinkXP_2684
    sai "*Risa* Tienes razón. Eras muy consciente del efecto que producía ese monstruo."
    sai "Y sí. Estoy bien. Genial. Me encanta esta postura. Teníamos que haberla probado antes."
    mc "*Risa* Te lo propuse mil veces..."
    call BlinkXP ("c18s002_470" , "d") from _call_BlinkXP_2685
    sai "*Risa* Pues se va a convertir en mi postura favorita."
    sai "Voy a empezar a moverme."
    mc "Cuando..."
    scene c18s002_475pv with dissolve
    show c18s002_475v with dissolve
    "No te da tiempo a terminar la frase antes de empezar una salvaje cabalgata."
    sai "*Gemido* Así te noto... diferente..."
    "Sin perder el contacto visual en ningún momento."
    sai "*Jadeo* Me encanta mirarte a los ojos..."
    "Algo ha cambiado en Saira."
    sai "*Gemido* Te amo."
    mc "Y yo a ti, mi amor."
    scene c18s002_480pv with dissolve
    hide c18s002_475v
    show c18s002_480v with dissolve
    "Mjolnir entra y sale de la vagina de Saira a un ritmo constante marcado por Saira."
    sai "*Jadeo* No me vuelvas a hacer caso..."
    "Mientras tanto tú vas ayudando con pequeñas embestidas cuando ella está llegando al final de su recorrido."
    sai "*Gemido* ... cuando me vuelva a negar a probar algo."
    "Posiblemente la frase más peligrosa en boca de una novia. No me hagas caso cuando no quiera hacer algo."
    scene c18s002_495pv with dissolve
    hide c18s002_480v
    show c18s002_495v with dissolve
    "Novia... Saira es tu novia por fin. El pensamiento te golpea como un mazazo."
    sai "*Gemido* Es lo mejor que hemos hecho nunca..."
    "Por eso se atreve a mirarte a los ojos. Ya no sois amigos con derecho a roce. Es tu novia. Eres su novio."
    "Es solo una etiqueta y nunca te han importado, pero si esa etiqueta te permite poder hacerle el amor mientras te pierdes en los pozos de negrura de sus ojos... bienvenida sea."
    sai "*Jadeo* Me voy a correr otra vez... *Gemido* deja de mirarme..."
    mc "Nunca."
    "Mirar esos expresivos ojos mientras el placer recorre cada uno de sus rasgos es una de las ventajas de esa etiqueta."
    call OrgasmX ("c18s002_500") from _call_OrgasmX_54
    sai "*GEMIDO* ¡¡Me CORROOOOO!!"
    "Su cara es graciosa, pero no tanto como para sobrepasar tu autocontrol y arrancarte una carcajada."
    "Quizás se te escapa una sonrisa, pero nada más."
    scene c18s002_485pv with dissolve
    hide c18s002_495v
    show c18s002_485v with dissolve
    "Saira continúa su cabalgata, acumulando orgasmo tras orgasmo."
    sai "*JADEO* ¡Joder! ¡Mas rápido!"
    "Lo dice como si de ti dependiera. Ella tiene el control, subiendo y bajando a su antojo."
    sai "*GEMIDO* Te odio por permitirme que me negara a esto."
    "Ciertamente está siendo increíblemente bueno. Seguramente el mejor sexo que has tenido nunca con Saira."
    scene c18s002_490pv with dissolve
    hide c18s002_485v
    show c18s002_490v with dissolve
    "Notas cada uno de sus orgasmos recorriendo su vagina, aprisionando y estrujando tu astil."
    sai "*JADEO* ¡Oh, sí! ¡Aghhhh! ¡No paran de llegar!"
    "Lo sabes. El maravilloso sonido húmedo que se produce cada vez que vuestras pelvis chocan es señal inequívoca de que Saira está creando un lago en tu habitación."
    mc "Saira, vuelvo a estar a punto..."
    sai "*GEMIDO* Córrete dentro, por favor..."
    "Si ella lo pide..."
    if persistent.walkthrough:
        $ wt1 = _("Sin consecuencias.")
        $ wt2 = _("Saira embarazada.")
    else:
        $ wt1 = ""
        $ wt2 = ""
    menu:
        "Correrte dentro." (wt = wt1):
            pass
        "Correrte dentro. Ir a por el bebé" (wt = wt2) if persistent.pregnancy:
            play sound ("music/OldMusicBox5.ogg")
            $ sai._var("pregnant", True)
    $ resetWalkthrough ()
    call OrgasmX ("c18s002_505") from _call_OrgasmX_55
    mc "¡Mpfft!"
    "Explotas dentro de Saira, liberando una cantidad enorme de semen."
    sai "*GEMIDO* ¡Sí! *Jadeo*"
    "Los cambios de postura y las conversaciones sobre no reírte han hecho que tardes más de lo normal en correrte."
    sai "*Gemido* ¡Lléname!"
    "También han hecho que tu excitación haya alcanzado cotas muy altas y tu corrida ha sido ingente."
    call BlinkXP ("c18s002_510" , "f") from _call_BlinkXP_2686
    "Unos segundos después, cuando vuestros orgasmos finalizan..."
    sai "¿Te ha gustado?"
    mc "Mucho. ¿A ti?"
    sai "Muchísimo. Me ha encantado esta postura. La próxima vez quiero probar el misionero."
    mc "Ya has visto que no me he reído..."
    call BlinkXP ("c18s002_515" , "d") from _call_BlinkXP_2687
    sai "Porque eres un caballero que cumple sus promesas. *Risa*"
    sai "Hazme un poco de espacio. Las piernas ya no me aguantan."
    call BlinkXP ("c18s002_520" , "f") from _call_BlinkXP_2688
    sai "¿Te acuerdas la última vez que estuvimos así?"
    mc "Por supuesto. Nuestra última noche juntos."
    call BlinkXP ("c18s002_525" , "d") from _call_BlinkXP_2689
    sai "¿Te acuerdas de qué te pregunté?"
    mc "Hablamos de muchas cosas aquel día. De mi trabajo aquí, de lo de mi padre..."
    call BlinkXP ("c18s002_530" , "d") from _call_BlinkXP_2690
    sai "Y te pregunté si te podría visitar..."
    mc "Cierto."
    sai "Esperaba que pasara esto..."
    if mc._var("relationships")>1:
        call BlinkXP ("c18s002_535" , "d") from _call_BlinkXP_2691
        sai "Aunque en otras circunstancias..."
        mc "Saira, aceptaste que estuviera con otras chicas."
        call BlinkXP ("c18s002_540" , "d") from _call_BlinkXP_2692
        sai "¡Oh! No me malinterpretes... lo acepto y estoy esperando descubrir con quién más estás."
        sai "No podría imaginarme hacerme amiga de Eileen tan rápido como lo hice."
        if sca._var("route") and not sai._var("routeSecondChance"):
            sai "Y que me besaras delante de Scarlett en el aeropuerto nos ha unido mucho. Las dos sabemos que estamos contigo."
        mc "Por un momento me había parecido que iba a aparecer de nuevo la Saira Saca Ojos. *Risa*"
        call BlinkXP ("c18s002_545" , "d") from _call_BlinkXP_2693
        sai "*Risa* Para nada. Está muerta y enterrada. Además, aquella Saira hablaba demasiado. *Risita*"
        sai "Ya te digo que esperaba que pasara esto, no así, pero no me quejo."
    mc "Pues ha pasado. Y estoy muy contento de que haya pasado."
    mc "¿Te quieres quedar a dormir?"
    call BlinkXP ("c18s002_550" , "d") from _call_BlinkXP_2694
    sai "Quiero, pero no lo voy a hacer."
    sai "Megan llegará en breve del Jazz Corner y, si no me encuentra en la habitación, le será muy fácil deducir dónde estoy."
    mc "No sería muy difícil, ciertamente. *Risa*"
    call BlinkXP ("c18s002_555" , "d") from _call_BlinkXP_2695
    sai "Esta noche ha sido fantástica y no quiero estropearlo desvelando nuestro secreto."
    mc "¿Por qué lo ibas a estropear? Con ella no se cumple lo que dijiste de las otras chicas."
    call BlinkXP ("c18s002_560" , "d") from _call_BlinkXP_2696
    sai "Creo que a Megan le gustabas cuando estaba en Portland. Me llegaron rumores. Pero creo que no intentó nada porque sabía de nuestra relación."
    sai "Tengo que hablarlo con ella un día. Y no quiero que sea hoy. Ni este fin de semana."
    mc "*Risa* Es una conversación en la que me gustaría estar..."
    call BlinkXP ("c18s002_565" , "d") from _call_BlinkXP_2697
    sai "Y a la que no vas a estar invitado. *Risa* Acuérdate de lo que te he dicho en el club. No tienes que estar resolviéndolo todo, y ni siquiera sé si hay algo que resolver."
    sai "Megan es fantástica y nos ha conseguido el local para hoy. Ha sido un detalle hacia las chicas."
    mc "Creo que todo el mundo se lo ha pasado bien."
    call BlinkXP ("c18s002_570" , "d") from _call_BlinkXP_2698
    sai "Me hubiera gustado que viniera Eileen, pero con los cambios de turno que ha tenido que hacer para poder estar mañana en el cumpleaños estaba destrozada."
    mc "Trabajar de camarera no es un trabajo relajado."
    call BlinkXP ("c18s002_575" , "d") from _call_BlinkXP_2699
    sai "Lo sé, pero para mí la noche no ha sido completa sin ella ni Alexia."
    mc "Mañana estarán las dos. Mañana es el gran día."
    scene c18s002_580a with dissolve
    sai "Con lo que es el momento de que me vista y me vaya."
    mc "Muy a mi pesar."
    scene c18s002_580b with dissolve
    sai "Cuando lo hagamos público, dentro de unas semanas, me podré quedar todas las noches."
    if mc._var("relationships")>1:
        sai "Si no hay ninguna otra chica ocupando tu cama, claro."
    call BlinkXP ("c18s002_585" , "d") from _call_BlinkXP_2700
    sai "¿No dices que no? *Risa*"
    mc "Estaba embelesado por lo bonito que es tu cuerpo, Saira."
    scene c18s002_580c with dissolve
    sai "No es justo querer ruborizar a una chica que se tiene que ir ya. *Risita*"
    mc "Entiendo que te quieras ir, pero mi venganza es que bajarás un piso ruborizada."
    sai "Y con las piernas temblando."
    call BlinkXP ("c18s002_590" , "f") from _call_BlinkXP_2701
    "Unos minutos después."
    sai "Nos vemos mañana en el gran día."
    mc "Es un cumpleaños... o tres. Tampoco es que vayamos a hacer nada que no llevemos haciendo los últimos días. Una comida en familia, con la familia completa esta vez."
    mc "Una pregunta... ¿serás de las que hacen topless en la piscina?"
    call BlinkXP ("c18s002_595" , "d") from _call_BlinkXP_2702
    sai "Lo tendrás que descubrir mañana. *Risa*"
    sai "Pero no será porque no hayas tenido tiempo de ver a las chicas esta noche."
    mc "El día que no quiera verlas, mátame. *Risa*"
    call KissXP ("c18s002_600" , "d") from _call_KissXP_80
    sai "Hasta mañana, mi amor."
    mc "Hasta mañana, mi vida."
    scene c18s002_600c with dissolve
    stop music fadeout (1.5)
    mcp "(Se fue. ¡Qué ganas tengo de que todo salga a la luz para no tener que ir escondiéndome!)"
    return
label c18s003_Sunday:
    scene black with dissolve
    centered "{size=+20}{b}DÍA 20 – DOMINGO{/b}{/size}"
    if emm._var("route"):
        "Cuando te despiertas bajas un test de embarazo a la habitación de [emm], donde tomáis una muestra de sangre antes de ir a desayunar."
    else:
        "Bajas a desayunar. Extrañamente no hay nadie en la cocina."
    return
label c18s003_DaphScarPregnancyResults:
    if _in_replay:
        menu:
            "¿Estás en una relación con [dap]?"
            "Sí":
                $ dap._var("route" , True)
                menu:
                    "¿Está embarazada?"
                    "Si":
                        $ dap._var("pregnant" , True)
                    "No":
                        $ dap._var("pregnant" , False)
            "No":
                $ dap._var("route" , False)
                $ dap._var("pregnant" , False)
        menu:
            "¿Estás en una relación con Scarlett?"
            "Sí":
                $ sca._var("route" , True)
                menu:
                    "¿Está embarazada?"
                    "Si":
                        $ sca._var("pregnant" , True)
                    "No":
                        $ sca._var("pregnant" , False)
            "No":
                $ sca._var("route" , False)
                $ sca._var("pregnant" , False)
        menu:
            "¿Estás en una relación con [nor]?"
            "Sí":
                $ nor._var("route" , True)
            "No":
                $ nor._var("route" , False)
        menu:
            "¿Le cogiste el teléfono a tu padre cuando llamó?"
            "Sí":
                $ mc._var("edmundsStory", True)
            "No":
                $ mc._var("edmundsStory", False)
    "Después de desayunar vas a la habitación de [dap] y Scarlett."
    scene c17s003_005a with dissolve
    play sound ("music/knock.ogg")
    "*Knock-Knock*"
    mc "Soy yo. ¿Puedo pasar?"
    dap "*A través de la puerta* Sí, entra."
    scene c18s003_005a with dissolve
    play music ("music/These-Little-Moments.ogg")
    if dap._var("route") and sca._var("route"):
        mc "Buenos días, preciosas. No sé por qué, pero os imaginaba con los tests encima de la cama y mirándolos ansiosas esperando a que pitaran. *Risa*"
    else:
        mc "Buenos días, preciosas. No sé por qué, pero os imaginaba con el test encima de la cama y mirándolo ansiosas esperando a que pitara. *Risa*"
    dap "*Risa* ¿Qué crees que hay debajo del cojín?"
    sca "*Risa* ¿Por quién nos tomas?"
    if dap._var("route") and sca._var("route"):
        $ Aux = True
        scene c18s003_005b with dissolve
    else:
        scene c18s003_005c with dissolve
        $ Aux = False
    mc "¿Y el móvil?"
    dap "Si hubiera entrado mi madre..."
    sca "Como así ha sido..."
    dap "Y hubiera pitado el test en ese momento, podría decir que era una notificación del móvil."
    sca "Tía [nor] no hubiera sospechado."
    if nor._var("route"):
        mcp "(A menos que reconociera el pitido del test de embarazo.)"
    call BlinkXP ("c18s003_010" , "d") from _call_BlinkXP_2703
    dap "Pero se ha ido antes de que pitara. ¿No debería haber pitado ya?"
    mc "Faltan unos minutos para las 24 horas. Además no es 100\% exacto."
    if Aux or sca._var("route"):
        play sound ("music/buzz-buzz.ogg")
        "Justo en ese momento pita el test de Scarlett."
        call c18s003_Scarlett from _call_c18s003_Scarlett
    if dap._var("route"):
        play sound ("music/buzz-buzz.ogg")
        "Justo en ese momento pita el test de [dap]."
        call c18s003_Daphne from _call_c18s003_Daphne
    call BlinkXP ("c18s003_260" , "d") from _call_BlinkXP_2705
    "Al cabo de un rato..."
    dap "Te vamos a tener que echar. Nos tenemos que duchar antes de la comida."
    call BlinkXP ("c18s003_265" , "d") from _call_BlinkXP_2706
    sca "Tú tienes que ir a buscar a Maddie."
    mc "Es muy pronto todavía."
    sca "Y yo aún tengo que escoger mi bikini."
    mc "¿Bikini completo o solo la mitad?"
    call BlinkXP ("c18s003_270" , "d") from _call_BlinkXP_2707
    sca "Eso tendrás que esperar para verlo. *Risa*"
    if sca._var("route"):
        call KissXP ("c18s003_275" , "d") from _call_KissXP_81
        sca "Hasta luego, mi amor."
        mc "Hasta luego, mi vida."
    if dap._var("route"):
        call KissXP ("c18s003_280" , "d") from _call_KissXP_82
        dap "Te quiero."
        mc "Yo te quiero más."
    scene black with dissolve
    "Te sacan de la habitación casi a empujones."
    stop music fadeout (1.5)
    "Ciertamente es muy pronto para ir a buscar a Maddie, con lo que decides ir a tu habitación e informarte sobre Aruba."
    return
label c18s003_Daphne:
    if sca._var("route"):
        if dap._var("pregnant"):
            scene c18s003_020d with dissolve
        else:
            scene c18s003_020e with dissolve
    else:
        if dap._var("pregnant"):
            scene c18s003_020f with dissolve
        else:
            scene c18s003_020g with dissolve
    pause (1.0)
    if sca._var("route"):
        if dap._var("pregnant"):
            call BlinkXP ("c18s003_150" , "d") from _call_BlinkXP_2708
            dap "¡Positivo!"
            $ dap._var("pregnancyDiscovered", True)
            if sca._var("pregnant"):
                dap "¡Yo también voy a ser madre! Ya van dos de dos, [mc]."
                dap "¡Y tú también vas a ser tía, Scarlett!"
            else:
                dap "¡Voy a ser madre! ¡Vas a ser padre, [mc]!"
                dap "¡Y tú vas a ser tía, Scarlett!"
            mc "Vuelve al abrazo, Mami."
            call BlinkXP ("c18s003_155" , "d") from _call_BlinkXP_2709
            sca "¡Felicidades a los dos!"
            sca "Os parecerá una tontería pero me hace mucha ilusión ser la tía de Maeve."
            mc "No lo es. Eso sólo demuestra lo mucho que vas a querer a ese bebé."
            mc "¿Ninguna duda en tu caso, [dap]?"
            call BlinkXP ("c18s003_160" , "d") from _call_BlinkXP_2710
            if persistent.family:
                dap "Ninguna. La endogamia entre primos tiene un riesgo casi cero."
            else:
                dap "Ninguna. Si esto hubiera pasado hace unos meses quizás me hubiera preocupado un poco la endogamia. Pero tiene un riesgo casi cero entre primos."
                dap "Después de descubrir que no lo somos, ni siquiera eso me preocupa."
            call BlinkXP ("c18s003_165" , "d") from _call_BlinkXP_2711
            dap "¡Y además tenemos una empresa de tecnología punta en genética! Creo que podrán detectar cualquier cosa que surja."
            dap "¡Tenemos que ir a Aruba en cuanto podamos para comprobar que todo está bien!"
            if not persistent.family:
                dap "Soy un clon de Eva. No sé cómo eso puede afectar a nuestro bebé."
            mc "Iremos. Ayer estuve hablando con tu madre y seguramente tendré que ir en unas semanas.."
            if sca._var("pregnant"):
                mc "Me podéis acompañar las dos."
            else:
                mc "Me puedes acompañar, y Scarlett si lo necesita."
            call BlinkXP ("c18s003_170" , "d") from _call_BlinkXP_2712
            sca "Ya habíamos hablado de visitarte si al final aceptabas el trabajo. Tenemos muchas ganas de saber cómo funciona todo allí."
            mc "¡Esas son mis chicas!"
            scene c18s003_130a with dissolve
            "Os volvéis a abrazar los tres. El día ha empezado bien para [dap]."
            "Y en el caso de Scarlett, ha sido más importante resolver sus dudas y darle seguridad que el resultado del test."
        else:
            call BlinkXP ("c18s003_175" , "d") from _call_BlinkXP_2713
            dap "Negativo."
            if sca._var("pregnant"):
                dap "Me tendré que conformar con ser tía. *Risa* Al menos hasta que te lleve a otro hotel temático."
            else:
                dap "Tienes que empezar a apuntar mejor, [mc]. *Risa* Has fallado dos de dos."
            call BlinkXP ("c18s003_155" , "d") from _call_BlinkXP_2714
            sca "Al menos conservará su figura cuando vayamos a Aruba. Podrá lucir cuerpo en la playa."
            if sca._var("pregnant"):
                sca "Yo seguro que parezco una ballena enseguida."
            mc "¿A Aruba?"
            call BlinkXP ("c18s003_180" , "d") from _call_BlinkXP_2715
            dap "Nuestro novio va a estar allí, y no vamos a dejar de visitarle."
            call BlinkXP ("c18s003_185" , "d") from _call_BlinkXP_2716
            if sca._var("pregnant"):
                sca "Y, siendo una empresa de genética de tecnología punta especializada en clonar fetos, podrán ver si todo va bien con el bebé."
            sca "No te vas a librar de nosotras porque te vayas al Caribe."
            mc "No tengo ninguna intención de librarme de ninguna de vosotras."
            scene c18s003_130a with dissolve
            "Os volvéis a abrazar los tres. El día no ha empezado tan bien para [dap] como ella hubiera querido, pero se lo ha tomado mejor de lo que hubieras esperado.."
            "Y en el caso de Scarlett, ha sido más importante resolver sus dudas y darle seguridad que el resultado del test."
    else:
        if dap._var("pregnant"):
            call BlinkXP ("c18s003_190" , "d") from _call_BlinkXP_2717
            dap "¡Positivo!"
            mc "¡Ven aquí, Mamá!"
            scene c18s003_190d with dissolve
            "Os fundís en un abrazo que dice mucho de la alegría de [dap] por el resultado."
            call BlinkXP ("c18s003_195" , "d") from _call_BlinkXP_2718
            dap "El mejor regalo de cumpleaños que podría haber tenido."
            mc "Espero que lo que te he comprado también te guste. *Risa*"
            call BlinkXP ("c18s003_200" , "d") from _call_BlinkXP_2719
            sca "¡Felicidades! ¡Voy a ser tía! Estoy muy contenta por vosotros y por mí misma."
            mc "Gracias, Scarlett."
            mc "[dap], las funciones de una tía incluyen el cambio de pañales, ¿no?"
            call BlinkXP ("c18s003_205" , "d") from _call_BlinkXP_2720
            dap "Por supuesto. Seguro que Scarlett inventa una app para que le diga cuándo cambiarlos. *Risa*"
            mc "Scarlett, te nombro cambiadora de pañales oficial de Maeve. *Risa*"
            call BlinkXP ("c18s003_210" , "d") from _call_BlinkXP_2721
            sca "¡Puagh! Yo haré la app, pero para instalarla en el móvil de Olivia y que los cambie ella. *Risa*"
            sca "Me quedo con el título de Gestora de Cambios de Pañal. *Risa*"
            mc "Nos sirve, ¿verdad, [dap]?"
            call BlinkXP ("c18s003_215" , "d") from _call_BlinkXP_2722
            dap "¡Por supuesto! Ven aquí, Scarlett. Únete al abrazo. Sin tu idea de las lecciones esto no hubiera pasado."
            mc "Sí, Tía Scarlett, ven aquí."
            scene c18s003_130a with dissolve
            "Scarlett se une al abrazo. Contenta por su nueva sobrina."
            sca "Ahora hay que planificar el viaje a Aruba."
            mc "¿Aruba? ¿Por qué?"
            call BlinkXP ("c18s003_220" , "d") from _call_BlinkXP_2723
            if persistent.family:
                dap "Somos primos y en Aruba hay una empresa de ingeniería genética que clona bebés. Creo que es el mejor sitio para comprobar que no hay ningún problema."
                dap "Aunque la endogamia entre primos tiene un riesgo negligible, prefiero estar segura."
            else:
                dap "Soy un clon de Eva. No sé cómo eso puede afectar a nuestro bebé."
                dap "En Aruba hay una empresa de ingeniería genética que clona bebés. Creo que es el mejor sitio para comprobar que no hay ningún problema."
            call BlinkXP ("c18s003_225" , "d") from _call_BlinkXP_2724
            dap "Además, no creerás que te vas a librar de mis antojos, ¿verdad? *Risa*"
            mc "No tengo intención de hacerlo. *Risa*"
            call BlinkXP ("c18s003_230" , "d") from _call_BlinkXP_2725
            sca "Si no os molesta, yo os acompañaré. Mientras la ballena se hace las pruebas, yo podre lucir tipito en una playa caribeña. *Risa*"
            mc "Eres bienvenida, pero no te recomiendo llamar ballena a una mujer embarazada. *Risa*"
            scene c18s003_130a with dissolve
            "Os volvéis a abrazar los tres. El día ha empezado bien para [dap]."
        else:
            call BlinkXP ("c18s003_235" , "d") from _call_BlinkXP_2726
            dap "Negativo."
            mc "¿Decepcionada?"
            call BlinkXP ("c18s003_240" , "d") from _call_BlinkXP_2727
            dap "Para nada. Ya te dije ayer que nunca había pensado en quedarme embarazada a los 18."
            dap "Mañana es otra cosa, ya tendré 19. *Risa* Y si llega a los 20 o a los 23 da lo mismo. Lo divertido son los intentos."
            mc "Esa es la actitud."
            call BlinkXP ("c18s003_245" , "d") from _call_BlinkXP_2728
            sca "Al menos no serás una ballena cuando vayamos a Aruba."
            mc "¿Aruba?"
            call BlinkXP ("c18s003_250" , "d") from _call_BlinkXP_2729
            dap "Ya te dijimos que queríamos trabajar allí. Es muy pronto aún, tenemos que acabar las carreras... empezarlas para ser más exactos."
            dap "Pero queremos acompañarte cuando vayas, para ver las instalaciones, empezar a aprender cómo funciona todo y aprovechar el verano."
            call BlinkXP ("c18s003_255" , "d") from _call_BlinkXP_2730
            sca "No tenemos mucho que hacer hasta que no empiece el curso, con lo que nos ha parecido una buena idea."
            sca "Al menos pasar unos días allí hasta que te asientes. No te sentirás tan solo."
            mc "Me parece genial. Habría que hablarlo con Amanda y Eva, pero no creo que haya ningún problema. Pero ahora quiero un abrazo."
            scene c18s003_130a with dissolve
            "Los tres os fundís en un abrazo que inicia [dap] y al que se une Scarlett."
    return
label c18s003_Scarlett:
    call BlinkXP ("c18s003_015" , "v") from _call_BlinkXP_2704
    sca "¿Ha sido el mío? Me da miedo mirar..."
    mc "Sabes que no hay una sola oportunidad, ¿verdad? Si no sale positivo a la primera..."
    if sca._var("pregnant"):
        $ sca._var("pregnancyDiscovered", True)
        scene c18s003_020aAn with dissolve
        sca "¡Positivo!"
        mc "¡Ven aquí, Mamá!"
        call c18s003_convScar1 from _call_c18s003_convScar1_1
        call BlinkXP ("c18s003_025" , "d") from _call_BlinkXP_2731
        play music ("music/SadSoul.ogg")
        mc "¿Pasa algo, mi amor? ¿No estás contenta?"
        sca "No es eso..."
        call c18s003_convScar2 from _call_c18s003_convScar2_1
        call BlinkXP ("c18s003_035" , "d") from _call_BlinkXP_2732
        sca "No me malinterpretes... estoy contenta de llevar a nuestro hijo dentro..."
        mc "Nadie lo podría adivinar, Scarlett. Parece que la noticia no te ha gustado."
        call c18s003_convScar3 from _call_c18s003_convScar3_1
        if mc._var("edmundsStory"):
            sca "Es posible que seamos hermanos y que este hijo sea endogámico. Me preocupa..."
            call c18s003_convScar4 from _call_c18s003_convScar4
        call c18s003_convScar5 from _call_c18s003_convScar5
        call BlinkXP ("c18s003_085" , "d") from _call_BlinkXP_2733
        sca "Sé que [mar] va a estar ahí para nuestro bebé, y que [nor] va a actuar también de abuela. Y que va a tener muchas tías."
        mc "Y no te olvides de Meemaw y Tía Betty. Van a ser unas bisabuelas fantásticas."
        mc "Al menos cuando no estén en Florida."
        call BlinkXP ("c18s003_090" , "d") from _call_BlinkXP_2734
        sca "Pero... me gustaría que... en algún momento se lo pudiéramos decir a mi madre."
        mc "¿Qué? ¿Tal como te ha tratado?"
        call BlinkXP ("c18s003_095" , "d") from _call_BlinkXP_2735
        dap "[mc], es su madre. ¿No se lo vas a contar a Tío Edmund, por muy mal que se haya portado?"
        call c18s003_convScar6 from _call_c18s003_convScar6
        if mc._var("edmundsStory"):
            mc "Si por mí fuera, esperaría como mínimo a tener los resultados del test de ADN."
        else:
            mc "Si por mí fuera, esperaría un tiempo antes de decírselo, a que se calmen las aguas."
        call BlinkXP ("c18s003_105" , "d") from _call_BlinkXP_2736
        if mc._var("edmundsStory"):
            sca "Me parece una buena idea. Si somos medio hermanos... creo que podría decir cosas muy feas. Al menos iremos preparados. Y no es que tenga ganas de verla ahora mismo."
        else:
            sca "Me parece una buena idea. No tengo ganas de verla ahora mismo."
        sca "De todas formas, no tenía intención de contárselo enseguida. Primero se lo quiero contar a nuestra familia."
        call c18s003_convScar7 from _call_c18s003_convScar7
        mc "Ya te lo he dicho. Si quieres contárselo, no voy a poner ningún impedimento."
        call c18s003_convScar8 from _call_c18s003_convScar8
        call BlinkXP ("c18s003_125" , "d") from _call_BlinkXP_2737
        dap "¿Puede Tía [dap] pedir un abrazo de los futuros padres?"
        call c18s003_convScar9 from _call_c18s003_convScar9
        if dap._var("route"):
            sca "Ahora solo falta ver el de [dap]. Yo también quiero ser tía."
            dap "No tengo prisa en que pite. Se está muy bien aquí. Ese test de embarazo va a ser el mejor regalo de cumpleaños que voy a recibir hoy."
        else:
            dap "A veces me dais mucha envidia. Después pienso en que voy a poder jugar con el bebé y se me pasa."
            dap "Ese test de embarazo va a ser el mejor regalo de cumpleaños que voy a recibir hoy."
        mc "*Risa* Espero que no, pero ya tenemos una voluntaria para cambiar pañales, Scarlett."
        sca "*Risa* Creo que [dap] será la primera persona del mundo que se lea en profundidad el manual de los pañales y lo modifique para hacerlo más eficiente."
        dap "¡Puagh! Quiero jugar con el bebé. *Risa* Los pañales son cosa vuestra. Pero sí que me leeré el manual."
    else:
        scene c18s003_020bAn with dissolve
        sca "¡Negativo!"
        mc "Ven aquí. Dame un abrazo y un beso."
        call c18s003_convScar1 from _call_c18s003_convScar1
        call BlinkXP ("c18s003_025" , "d") from _call_BlinkXP_2738
        play music ("music/SadSoul.ogg")
        mc "No te pongas triste, habrá más oportunidades."
        sca "No es eso..."
        call c18s003_convScar2 from _call_c18s003_convScar2
        call BlinkXP ("c18s003_035" , "d") from _call_BlinkXP_2739
        sca "No me malinterpretes, me hubiera gustado quedarme embarazada... pero casi prefiero que no haya pasado."
        mc "¿Por qué? ¿Hay algo que deba saber?"
        call c18s003_convScar3 from _call_c18s003_convScar3
        if mc._var("edmundsStory"):
            sca "Aún no sabemos los resultados del test de ADN. Es posible que este bebé hubiera sido endogámico."
            call c18s003_convScar4 from _call_c18s003_convScar4_1
        call c18s003_convScar5 from _call_c18s003_convScar5_1
        call BlinkXP ("c18s003_085" , "d") from _call_BlinkXP_2740
        sca "Sé que [mar] estaría ahí para nuestro bebé, y que [nor] actuaría también de abuela. Y que tendría muchas tías."
        mc "Y no te olvides de Meemaw y Tía Betty. Serían unas bisabuelas fantásticas."
        mc "Al menos cuando no estén en Florida."
        call BlinkXP ("c18s003_090" , "d") from _call_BlinkXP_2741
        sca "Pero... me gustaría que... si en algún momento pasa, se lo pudiéramos decir a mi madre."
        mc "¿Qué? ¿Tal como te ha tratado?"
        call BlinkXP ("c18s003_095" , "d") from _call_BlinkXP_2742
        dap "[mc], es su madre. ¿No se lo contarías a Tío Edmund, por muy mal que se haya portado?"
        call c18s003_convScar6 from _call_c18s003_convScar6_1
        if mc._var("edmundsStory"):
            mc "Pero si hubiera salido positivo hoy, esperaría como mínimo a tener los resultados del test de ADN."
        else:
            mc "Pero si hubiera salido positivo hoy, esperaría un tiempo antes de decírselo, a que se calmen las aguas."
        call BlinkXP ("c18s003_105" , "d") from _call_BlinkXP_2743
        if mc._var("edmundsStory"):
            sca "Me parece una buena idea. Si somos medio hermanos... creo que podría decir cosas muy feas. Al menos iríamos preparados."
        else:
            sca "Me parece una buena idea. No tengo ganas de verla ahora mismo."
        sca "De todas formas, no tenía intención de contárselo enseguida. Primero se lo hubiera querido contar a nuestra familia."
        call c18s003_convScar7 from _call_c18s003_convScar7_1
        mc "Ya te lo he dicho. Si, cuando pase, quieres contárselo, no voy a poner ningún impedimento."
        call c18s003_convScar8 from _call_c18s003_convScar8_1
        call BlinkXP ("c18s003_125" , "d") from _call_BlinkXP_2744
        dap "¿Puede la futura Tía [dap] pedir un abrazo de los futuros padres?"
        call c18s003_convScar9 from _call_c18s003_convScar9_1
        if dap._var("route"):
            sca "Ahora solo falta ver el de [dap]. A mí me gustaría saber hoy que voy a ser tía."
            dap "No tengo prisa en que pite. Se está muy bien aquí. Ese test de embarazo podría haber sido el mejor regalo de cumpleaños que iba a recibir hoy."
            dap "Veros superar las dudas han superado a cualquier posible positivo. Y ese bebé llegará tarde o temprano."
        else:
            dap "A veces me dais mucha envidia. Después pienso en que voy a poder jugar con el bebé cuando [mc] apunte bien con sus soldaditos y se me pasa."
            dap "Ese test de embarazo podría haber sido el mejor regalo de cumpleaños que iba a recibir hoy."
        mc "*Risa* Espero que no, pero ya tenemos una voluntaria para cambiar pañales cuando llegue el bebé, Scarlett."
        sca "*Risa* Creo que [dap] será la primera persona del mundo que se lea en profundidad el manual de los pañales y lo modifique para hacerlo más eficiente."
        dap "¡Puagh! He dicho jugar con el bebé. *Risa* Los pañales son cosa vuestra. Pero sí que me leeré el manual."
    return
label c18s003_convScar1:
    scene c18s003_020b with dissolve
    "Os fundís en un abrazo y un beso..."
    stop music fadeout (1.5)
    "Pero es un beso dubitativo. Algo le pasa a Scarlett."
    return
label c18s003_convScar2:
    call BlinkXP ("c18s003_030" , "d") from _call_BlinkXP_2745
    dap "Díselo. Lo va a entender."
    mc "¿Qué me estáis ocultando? Habíamos quedado en hablarlo todo, ¿no?"
    return
label c18s003_convScar3:
    call BlinkXP ("c18s003_040" , "d") from _call_BlinkXP_2746
    sca "[dap] y yo hemos estado hablando sobre qué pasaría si salía positivo..."
    return
label c18s003_convScar4:
    call BlinkXP ("c18s003_045" , "d") from _call_BlinkXP_2747
    dap "Yo le he dicho que la endogamia en primera generación no tiene prácticamente riesgos."
    mc "¿De qué riesgos estamos hablando?"
    call BlinkXP ("c18s003_050" , "d") from _call_BlinkXP_2748
    dap "Negligibles. Los riesgos aumentan a partir de la tercera generación endogámica."
    dap "Cuarta en vuestro caso ya que solo seríais medio hermanos. Si es que lo sois."
    call BlinkXP ("c18s003_055" , "d") from _call_BlinkXP_2749
    sca "Lo sé, pero eso no hace que me vaya a preocupar menos..."
    mc "¿No crees que vas un poco rápido con las preocupaciones?"
    call BlinkXP ("c18s003_060" , "d") from _call_BlinkXP_2750
    sca "¿A qué te refieres?"
    mc "A que aún no sabemos si somos medio hermanos. Creo que no vale la pena preocuparse por los \"qué pasaría si...?\" hasta que no tengamos los resultados."
    call BlinkXP ("c18s003_065" , "d") from _call_BlinkXP_2751
    sca "Tienes razón... pero hay otro tema."
    mc "¿Qué pasa?"
    return
label c18s003_convScar5:
    call BlinkXP ("c18s003_070" , "d") from _call_BlinkXP_2752
    dap "No te enfades. Ponte en su situación e intenta entenderlo."
    mc "Me estáis preocupando."
    call BlinkXP ("c18s003_075" , "d") from _call_BlinkXP_2753
    sca "Yo he crecido sin padre. Sé que tú no vas a ser un padre ausente."
    mc "No tengo intención de serlo."
    call BlinkXP ("c18s003_080" , "d") from _call_BlinkXP_2754
    sca "También he crecido prácticamente sin mis abuelos. Vosotros teníais a Olivia."
    mc "Sí..."
    return
label c18s003_convScar6:
    if mc._var("edmundsStory"):
        mc "¿Te das cuenta de lo complicado que sería eso si somos medio hermanos?"
        mc "Papá, tu hija y yo vamos a tener un hijo juntos. Cuando nos acostamos no sabíamos que éramos hermanos porque eres un pedazo de mierda que guardó el secreto."
    else:
        mc "Para eso debería saber cómo contactar con él."
    mc "Pero sí. Lo entiendo."
    call BlinkXP ("c18s003_100" , "d") from _call_BlinkXP_2755
    sca "Entonces... ¿no te importaría decírselo a mi madre?"
    mc "Es tu madre. Haremos con ella lo que creas conveniente."
    return
label c18s003_convScar7:
    mc "Creo que después de la interpretación de Amanda en tu antigua casa, deberíamos esperar un tiempo antes de ver a tu madre y a Kevin."
    mc "Ellos creen que se me llevó detenido."
    scene c18s003_020b with hpunch
    "Scarlett se lanza a tus brazos de nuevo. Esta vez, las dudas han desaparecido."
    call BlinkXP ("c18s003_110" , "d") from _call_BlinkXP_2756
    sca "Gracias por ser comprensivo, mi amor. Sé que no se lo merece, pero es mi madre al fin y al cabo."
    return
label c18s003_convScar8:
    stop music fadeout (1.5)
    mc "Pero si aparece Kevin no puedo asegurar que no le vaya a volver a pegar."
    play music ("music/These-Little-Moments.ogg")
    call BlinkXP ("c18s003_115" , "d") from _call_BlinkXP_2757
    sca "*Risa* Siempre podemos mandar a Amanda para que lo detenga antes de reunirnos con mi madre."
    mc "*Risa* No estaría mal. Nada mal."
    call BlinkXP ("c18s003_120" , "d") from _call_BlinkXP_2758
    dap "Ahora que todo está resuelto y os volvéis a reír... ¿puedo decir algo?"
    mc "Claro que sí, [dap]."
    return
label c18s003_convScar9:
    todas "*Risa*"
    mc "Ven aquí, Tía [dap]."
    scene c18s003_130a with dissolve
    "Los tres os fundís en un abrazo de alegría compartida."
    return
label c18s004_Meemaw:
    $ Aux = 0
    if _in_replay:
        menu:
            "¿Has pre-abierto la relación con Meemaw?"
            "Sí":
                $ mee._var("route" , True)
                menu:
                    "¿Estás en una relación con [mar!t]?"
                    "Sí":
                        $ mar._var("route" , True)
                    "No":
                        $ mar._var("route" , False)
                        menu:
                            "¿Estás en una relación con [nor]?"
                            "Sí":
                                $ nor._var("route" , True)
                            "No":
                                $ nor._var("route" , False)
                                menu:
                                    "¿Estás en una relación con Eileen?"
                                    "Sí":
                                        $ eil._var("route" , True)
                                    "No":
                                        $ eil._var("route" , False)
                                        menu:
                                            "¿Estás en una relación con Samantha?"
                                            "Sí":
                                                $ sam._var("route" , True)
                                            "No":
                                                $ sam._var("route" , False)
                                                menu:
                                                    "¿Estás en una relación con Simone?"
                                                    "Sí":
                                                        $ sim._var("route" , True)
                                                    "No":
                                                        $ sim._var("route" , False)
            "No":
                $ mee._var("route" , False)
    call BlinkXP ("c18s004_005" , "d") from _call_BlinkXP_2759
    play music ("music/Fragile-Beauty.ogg")
    "Al volver a tu habitación te encuentras con Olivia esperándote."
    "Tiene mejor aspecto que estos últimos días. Supones que los efectos de la quimio están desapareciendo, aún le queda un poco para volver a ser ella misma."
    mc "Buenos días, Meemaw."
    mee "¿No tengo beso de buenos días hoy?"
    mc "No hace falta que lo pidas, puedes darlo tú si quieres."
    call KissXP ("c18s004_010" , "d") from _call_KissXP_83
    mee "Buenos días, [mc]."
    mc "Buenos días, Meemaw. ¿Puedo ayudarte en algo?"
    call BlinkXP ("c18s004_015" , "d") from _call_BlinkXP_2760
    mee "Si tienes un rato libre..."
    mc "Siempre tengo tiempo libre para ti."
    call BlinkXP ("c18s004_020" , "d") from _call_BlinkXP_2761
    mee "¿Puedes ayudarme con el masaje hoy?"
    mc "¿No te gustó cómo lo hizo Tía Betty ayer?"
    call BlinkXP ("c18s004_025" , "d") from _call_BlinkXP_2762
    mee "No es por eso. Hoy es domingo y ha ido a misa. Además tenía que hablar con el cura de algo, la llamó ayer."
    mc "Ah, OK. Perfecto. ¿Dónde lo quieres hacer? ¿Aquí?"
    if not mee._var("route"):
        call BlinkXP ("c18s004_030" , "d") from _call_BlinkXP_2763
        mee "Sí, aquí mismo va bien. Me he extraído la leche en casa de [nor] hace un momento."
        scene black with dissolve
        "Haces el masaje a Olivia tal y como te enseñó la Doctora Milk y vuelve a su habitación. Cada vez está más cómoda a tu alrededor con poca ropa."
        return
    call BlinkXP ("c18s004_035" , "d") from _call_BlinkXP_2764
    mee "Creo que el mejor sitio sería un baño. Por si... ya sabes."
    mc "Bueno, parece que sólo pasó en la consulta de la Doctora Milk. Ayer, mientras le enseñaba a Tía Betty, no pasó nada."
    mc "¿Te volvió a pasar cuando me fui y la dejé haciéndote el masaje?"
    call BlinkXP ("c18s004_040" , "d") from _call_BlinkXP_2765
    mee "No, no... no pasó nada. Estoy empezando a pensar que quizás la Doctora no extrajo toda la leche."
    mc "Meemaw... yo creo que sí que lo hizo bien. Una de las razones que dio para que pasara lo que pasó es que hubiera excitación sexual."
    mc "Y los dos sabemos que la hubo."
    call BlinkXP ("c18s004_045" , "d") from _call_BlinkXP_2766
    mee "No me lo recuerdes... ¡Qué vergüenza! Tener un orgasmo mientras mi nieto me masajeaba los pechos..."
    mc "No le des más importancia de la que tiene. Pasó y ya está. Ayer no pasó, con lo que lo podemos dejar como un incidente aislado."
    mc "Supongo que no volverá a pasar lo mismo, con lo que no hay peligro para el parqué."
    call BlinkXP ("c18s004_050" , "d") from _call_BlinkXP_2767
    mee "Cómo quieras, pero no te quejes si después tienes que fregar tu habitación. *Risa*"
    mc "*Risa* Si tengo que fregar la habitación significará que lo has disfrutado, con lo que no me quejaré."
    call BlinkXP ("c18s004_055a" , "d") from _call_BlinkXP_2768
    mee "¡[mc]!"
    mc "¿Qué? Si vuelve a pasar lo mismo..."
    call BlinkXP ("c18s004_055b" , "d") from _call_BlinkXP_2769
    mee "No va a pasar. Punto."
    mc "OK. Déjame quitarme la ropa... tan solo para prevenir. Puedes dejar el albornoz en la silla."
    call BlinkXP ("c18s004_060" , "d") from _call_BlinkXP_2770
    mee "{b}¿Qué?{/b} ¿Vas a desnudarte?"
    mc "No, Meemaw, sólo voy a quitarme los pantalones y la camiseta. Ya te digo que es solo para prevenir."
    mc "Tengo que ir a buscar a Maddie cuando acabemos con esto, y no quiero ir con manchas lácteas. *Risa*"
    call BlinkXP ("c18s004_065" , "d") from _call_BlinkXP_2771
    mee "Vale... Has dicho que lo deje en la silla, ¿no?"
    mc "Sí, o en el sofá. Donde quieras."
    stop music fadeout (1.5)
    call BlinkXP ("c18s004_070" , "f") from _call_BlinkXP_2772
    mee "Lista."
    play music ("music/SexyLoungeMusic.ogg")
    mc "Hoy llevas braguitas más sexys que las bragas de abuela que llevabas ayer. *Risa*"
    call BlinkXP ("c18s004_075" , "d") from _call_BlinkXP_2773
    mee "¿Me quieres hacer sentir incómoda?"
    mc "No es eso. Tan solo estaba bromeando. Bragas de abuela, siendo tú... tenía gracia..."
    mc "Ven aquí y empecemos."
    scene c18s004_080pv with dissolve
    show c18s004_080v with dissolve
    "Empiezas a masajear los pechos de Olivia mientras ella, como ayer delante de Betty, está tensa y rehúye el contacto de su espalda contigo."
    mc "¿Va bien así?"
    mee "Muy bien, está siendo como con Betty. No hay excitación. No sé qué me pasó en la consulta de la Doctora."
    mc "A lo mejor llevabas mucho tiempo sin un orgasmo y tu cuerpo te lo pedía."
    mee "Es posible... por alguna razón, cuando noté tu erección no pude evitar frotarme contigo."
    scene c18s004_085pv with dissolve
    hide c18s004_080v
    show c18s004_085v with dissolve
    mee "Estaba muy avergonzada... casi parecía una perra en celo."
    mc "No tienes por qué avergonzarte. Soy yo y, pase lo que pase, quedará entre nosotros. No voy a ir anunciando que mi Meemaw tuvo un orgasmo conmigo. Puedes relajarte si quieres."
    mee "Gracias, cielo. No es por que vayas a contarlo. Es que... imagínate si hubiera pasado lo mismo ayer, delante de Betty. Mi nieto produciéndome un orgasmo delante de mi hermana."
    mc "*Risa* Eso ha sonado muy sexy."
    scene c18s004_090a with dissolve
    hide c18s004_085v
    "Poco a poco se va relajando y acaba apoyando su espalda contra tu pecho desnudo. Su piel es muy suave."
    mee "*Risa* Creo que ves demasiado porno. No sé por qué los hombres tenéis esa fijación en acostaros con dos hermanas a la vez."
    mc "Y suma a eso que una de las hermanas es monja. *Risa* Hay todo un género de porno dedicado a las monjas."
    mc "Y no solo hermanas. Madres e hijas, abuelas y nietas, tías y primas... Las combinaciones son muchas."
    call BlinkXP ("c18s004_095" , "d") from _call_BlinkXP_2774
    mee "Yo me moriría de vergüenza si tuviera que tener sexo con cualquiera de la familia delante."
    if mar._var("route") or nor._var("route") or sam._var("route") or sim._var("route") or eil._var("route"):
        mee "Ya sé que a ti eso de la familia no te importa a la hora de tener sexo, pero..."
        $ Aux = 2
    mee "Y antes de que preguntes, eso incluye al resto de chicas. No podría hacer un trío contigo y con... yo qué sé... una de las estudiantes, por ejemplo."
    mc "Es divertido que pongas a una de las estudiantes como impedimento pero no a mí. *Risa*"
    scene c18s004_100pv with dissolve
    show c18s004_100v with dissolve
    mee "Bueno, eres el único chico de la familia. Aparte de Jamaal, claro. Con lo que serías el único candidato."
    "Olivia no se ha dado cuenta aún, pero puedes notar como un líquido caliente empieza a brotar de sus pezones. Hablar de tríos parece que la está poniendo cachonda."
    mc "Podrías haber dicho un trío con un desconocido y con una de las estudiantes. *Risa* Yo también soy de la familia..."
    scene c18s004_090pv with dissolve
    hide c18s004_100v
    show c18s004_090v with dissolve
    "Empiezas a notar como ella ha empezado a frotar su culo contra tu entrepierna, propiciando que te des cuenta de que a ti también te estaba empezando a poner cachondo hablar de tríos con tu abuela."
    mee "El sexo es algo privado entre dos personas. No hay por qué exhibirlo por ahí. Meter a una tercera persona rompería la intimidad necesaria."
    scene c18s004_105pv with dissolve
    hide c18s004_090v
    show c18s004_105v with dissolve
    mee "¡Por Dios! *Gemido* Soy un dinosaurio... parece que tengo conceptos del milenio pasado."
    if Aux > 1:
        mee "Hablar de tus parejas, así en plural... *Jadeo* Se me hace rarísimo."
    "Está tan enfrascada en la conversación que ni siquiera se ha dado cuenta de que ha empezado a gemir."
    mcp "(Esto va a acabar como en la consulta de la Harley.)"
    mee "Pero volviendo a lo del desconocido. *Gemido* No puedo concebir el sexo con un desconocido. *Jadeo* No me entra en la mente."
    mc "Cada cual tiene sus propios conceptos sobre lo que está bien y mal. Pero sabes que te estás contradiciendo, ¿verdad?"
    scene c18s004_110pv with dissolve
    hide c18s004_105v
    show c18s004_110v with dissolve
    "Tu erección ya está a su máximo tamaño. Te cuesta que no se salga de los calzoncillos."
    mee "*Gemido* ¿En qué?"
    mc "Has dicho que no podías concebir el sexo con la familia ni con un desconocido. Ni siquiera has sido capaz de ponerle nombre a la estudiante del trío."
    mee "*Jadeo* Exacto..."
    scene c18s004_115pv with dissolve
    hide c18s004_110v
    show c18s004_115v with dissolve
    mc "Pero sin embargo sí que me has nombrado a mí en ese trío..."
    mee "*Gemido* Estábamos hablando de ti..."
    mc "¿O acaso es que conmigo si te lo imaginas?"
    call BlinkXP ("c18s004_120" , "h") from _call_BlinkXP_2775
    hide c18s004_115v
    mee "*Jadeo* ¿Qué? ¡No!"
    mc "Entonces, ¿por qué puedes poner mi nombre en esa frase y no el de Kate, por ejemplo?"
    mc "¿Puedes imaginarte sexo conmigo pero no con Kate? ¿Es por eso por lo que has vuelto a frotar tu culo contra mí? ¿Es por eso por lo que estás a punto de tener otro orgasmo?"
    scene c18s004_110bpv with dissolve
    show c18s004_110bv with dissolve
    "Consciente ahora de lo que está haciendo, acelera el ritmo, como si, ciertamente, estuviera a punto de llegar."
    mee "*Gemido* Lo siento... [mc]... *Jadeo* No era consciente..."
    mc "No te preocupes, no sería el primer orgasmo..."
    if persistent.lactation:
        call OrgasmX ("c18s004_125a") from _call_OrgasmX_56
    else:
        call OrgasmX ("c18s004_125b") from _call_OrgasmX_57
    mee "*GEMIDO*"
    hide c18s004_110bv
    "Decir la palabra orgasmo hace que se libere todo lo que Olivia estaba conteniendo inconscientemente. Un par de chorros de leche salen de sus pechos."
    mee "*JADEO*"
    "Sus gemidos son de sorpresa y placer simultáneamente."
    call OrgasmX ("c18s004_130a") from _call_OrgasmX_58
    "Y es el momento de que seas tú el sorprendido, cuando Olivia te coge por el cuello y te besa, girando la cabeza hacia ti."
    mee "*GEMIDO*"
    "Su cuerpo sigue estremeciéndose bajo tus manos mientras te besa. Sus pechos siguen bombeando leche. Está claro que esta vez no es un único orgasmo."
    scene c18s004_130d with hpunch
    "Tu cuerpo actúa por instinto y llevas una mano a su entrepierna, apretándola contra sus húmedas bragas, estrujando sus labios y su hinchado clítoris."
    mee "*JADEO*"
    "Su cuerpo se vuelve a estremecer. Su jadeo en tu boca es una mezcla de sorpresa, protesta, y placer entremezclado."
    "Abre sus piernas ligeramente para darte un mejor acceso."
    mee "*GEMIDO*"
    if persistent.lactation:
        call OrgasmX ("c18s004_135a") from _call_OrgasmX_59
    else:
        call OrgasmX ("c18s004_135b") from _call_OrgasmX_60
    "La protesta dura poco. Los orgasmos duran más."
    mee "{b}*JADEO*{/b}"
    "Mantienes tu mano firme, quieta. No necesitas hacer nada más para que los orgasmos sigan llegando."
    mee "{b}*GEMIDO*{/b}"
    "El cuerpo de Olivia dice que está a punto de derrumbarse, sus piernas tiemblan y vibran a los lados de tu mano."
    if persistent.walkthrough:
        $ wt1 = _("Beber leche.")
        $ wt2 = _("No beber leche.")
    else:
        $ wt1 = ""
        $ wt2 = ""
    menu:
        "Segundo desayuno." (wt = wt1):
            $ Aux2 = True
        "No tengo sed." (wt = wt2):
            $ Aux2 = False
    $ resetWalkthrough ()
    scene c18s004_140a with dissolve
    "Te sientas en la cama con Olivia sentada encima de tu erección. Vuestros labios no se separan. Tu mano no abandona su entrepierna."
    mee "*Gemido*"
    "Sus gemidos empiezan a bajar de intensidad tal como sus fuerzas la abandonan."
    mee "*Jadeo*"
    call BlinkXP ("c18s004_145" , "d") from _call_BlinkXP_2776
    "La ayudas a tumbarse cuando sus orgasmos finalizan y finalmente separa sus labios de los tuyos. Tu mano derecha continúa firme contra su coño. Ella no protesta."
    mee "*Gemido* ¿Qué estás haciendo, [mc]?"
    mc "Queda un pecho por masajear, y no parece que vayas a aguantar de pie, con lo que tendré que hacer algo parecido a lo que hicimos en la silla de la consulta."
    call BlinkXP ("c18s004_150" , "d") from _call_BlinkXP_2777
    "Continúas presionando su vulva y su monte de Venus con tu mano, notando a través de las bragas su humedad y el bulto que produce su vello púbico."
    mee "*Jadeo* Voy a poner la cama perdida de leche..."
    mc "No te preocupes por eso ahora mismo."
    call BlinkXP ("c18s004_155" , "d") from _call_BlinkXP_2778
    "Tu contacto con sus partes íntimas hace que, pese a que sus orgasmos han finalizado de momento, su excitación y sus gemidos no desaparezcan."
    mee "*Gemido* Vas a necesitar las dos manos..."
    "Casi parece que ha olvidado que tu mano está allí."
    if Aux2:
        mc "Quizás no."
        scene c18s004_160a with vpunch
        "Nada más meterte su pezón en la boca, recibes una descarga de leche en tu lengua, que inunda tus papilas gustativas."
        "No eres capaz de capturarlo todo y algunas gotas se unen al reguero de leche que va cayendo por el pecho de Olivia."
        mee "*{b}*JADEO*{/b} ¿Qué estás haciendo? El masaje no era así."
        mc "*Con la boca llena de pezón* Estoy improvisando..."
        mee "*Gemido* Ve con cuidado... está muy sensible."
        "Con esa frase se acaban las protestas de Meemaw."
        scene c18s004_165pv
        show c18s004_165v with dissolve
        "Empiezas a succionar la leche que sale a borbotones del pezón de Olivia."
        mee "*Gemido*"
        "Es diferente hacerlo con una mano, aunque sabes perfectamente dónde apretar."
        mee "*Jadeo*"
        "Suples con tus labios el movimiento que haría la otra mano."
        scene c18s004_160b with dissolve
        if persistent.family:
            "Que sigue firme y quieta en la entrepierna de tu abuela."
        else:
            "Que sigue firme y quieta en la entrepierna de Olivia."
        mee "*GEMIDO* No he tenido tantos orgasmos nunca..."
        "Por un momento has pensado en quitarle las bragas y empezar a masturbarla. No es necesario. Quizás otro día."
        mee "*JADEO* No voy a poder ponerme de pie... en dos semanas."
        "Esperas que no sea cierto. Sería un poco incómodo de explicar al resto de la familia."
        scene c18s004_170pv
        hide c18s004_165
        show c18s004_170v with dissolve
        "Tu boca sigue succionando, recibiendo descarga tras descarga de leche."
        mee "*Gemido* Me estás matando..."
        "Tu mano sigue presionando sus braguitas, cada vez más húmedas."
        mee "*Jadeo* No voy a aguantar mucho más..."
        "El otro pecho sigue soltando leche, pero por suerte solo es un hilito. Parece que el masaje anterior lo ha dejado vacío."
        call OrgasmX ("c18s004_175") from _call_OrgasmX_61
        "El cuerpo de Olivia se tensa mucho más de lo que ha hecho anteriormente. La descarga definitiva llega a tu boca. Incluso el otro pecho, que pensabas vacío, explota en un blanco géiser."
    else:
        mc "No te preocupes."
        scene c18s004_180a with vpunch
        "En el momento en que empiezas a masajear el pecho de Olivia, sale disparada una descarga de su leche."
        mee "*{b}*JADEO*{/b} ¿Qué estás haciendo? Esa pierna...."
        scene c18s004_180b with dissolve
        mc "Estoy improvisando..."
        "Una vez has tenido que retirar tu mano de su entrepierna, la has sustituido con tu muslo."
        mee "*Gemido* Ve con cuidado... está muy sensible. Tanto el pecho como el..."
        scene c18s004_185pv
        show c18s004_185v with dissolve
        "Continúas masajeando su pecho, al que no le has dedicado atenciones antes. La leche sale a borbotones del pezón de Olivia."
        mee "*Gemido*"
        "Es diferente hacerlo en la cama de lo que lo fue en la silla. Mil veces más sexy."
        mee "*Jadeo*"
        "Suples con tu pierna la presión que hacías antes con la mano."
        scene c18s004_180c with dissolve
        if persistent.family:
            "Un muslo que mantienes apretando firme y quieto la entrepierna de tu abuela."
        else:
            "Un muslo que mantienes apretando firme y quieto la entrepierna de Olivia."
        mee "*GEMIDO* No he tenido tantos orgasmos nunca..."
        "Por un momento has pensado en quitarle las bragas y empezar a masturbarla. Pero necesitas las dos manos para el masaje. Además, no es necesario. Quizás otro día."
        mee "*JADEO* No voy a poder ponerme de pie... en dos semanas."
        "Esperas que no sea cierto. Sería un poco incómodo de explicar al resto de la familia."
        scene c18s004_190pv
        hide c18s004_185
        show c18s004_190v with dissolve
        "Tus manos, cada vez más empapadas, siguen masajeando el pecho de Olivia, recibiendo descarga tras descarga de leche."
        mee "*Gemido* Me estás matando..."
        "Tu muslo sigue presionando sus braguitas, cada vez más húmedas."
        mee "*Jadeo* No voy a aguantar mucho más..."
        "El otro pecho sigue soltando leche, pero por suerte solo es un hilito. Parece que el masaje anterior lo ha dejado vacío."
        call OrgasmX ("c18s004_195") from _call_OrgasmX_62
        "El cuerpo de Olivia se tensa mucho más de lo que ha hecho anteriormente. La descarga definitiva se derrama sobre tus manos. Incluso el otro pecho, que pensabas vacío, explota en un blanco géiser."
    mee "*GEMIDO* ¡Oh, sí!"
    "Las bragas, antes mojadas, pasan a estar empapadas."
    mee "*JADEO* ¡Por el amor de Dios!"
    "Sus pezones, tan generosos con la leche, cortan el suministro de golpe como si alguien hubiera pulsado un interruptor."
    "Ahora sabes que no queda más leche que extraer de ninguno de ellos."
    scene c18s004_160c with dissolve
    "Olivia se derrumba en la cama, perdida toda la tensión. Los ojos cerrados."
    mee "*Respiración entrecortada* Déjame descansar un momento..."
    mc "Todo el tiempo que necesites. Espero que te haya gustado."
    stop music fadeout (1.5)
    mee "Me ha..."
    play music ("music/Sad-Piano.ogg")
    call BlinkXP ("c18s004_200" , "d") from _call_BlinkXP_2779
    "De repente abre los ojos y mira al techo de la habitación. Evitando el contacto visual contigo. Una expresión triste pasa por su rostro."
    mee "*Susurrando* Perdóname..."
    mc "No tengo nada que perdonar, Meemaw."
    mc "No hay nada de lo que avergonzarse."
    call BlinkXP ("c18s004_205" , "d") from _call_BlinkXP_2780
    mee "No te preocupes, no te lo decía a ti."
    mc "¿Qué? No te entiendo..."
    mee "No hay nada que entender. Para ti solo tengo agradecimiento."
    call BlinkXP ("c18s004_210" , "d") from _call_BlinkXP_2781
    stop music fadeout (1.5)
    mee "Y sobre tu pregunta de antes... me ha encantado. Tenías razón."
    play music ("music/pianomatic.ogg")
    mc "¿Sobre qué? *Risa*"
    mee "Sobre que tenía que dejarme llevar y no pensar tanto."
    mc "*Risa* Si te ha gustado entonces ha valido la pena que tardaras en darte cuenta. Al menos te has dado cuenta a tiempo."
    call BlinkXP ("c18s004_215" , "d") from _call_BlinkXP_2782
    mee "Por lo que sí que te tengo que pedir perdón es por el beso... no sé qué me ha pasado."
    mc "Creo que hemos superado que un beso nos incomode, ¿no?"
    call BlinkXP ("c18s004_220" , "d") from _call_BlinkXP_2783
    mee "Pero ese beso... no era un saludo... me he dejado llevar demasiado."
    mc "¿Vamos a fijarnos en un beso cuando acabas de tener un millón de orgasmos?"
    call BlinkXP ("c18s004_225" , "d") from _call_BlinkXP_2784
    mee "*Risa* Tienes razón."
    mc "Si, suele pasar. *Risa* Espera, tengo que hacer una llamada."
    scene c18s004_225d with dissolve
    mc "Hola, ¿Profesor Wheelxair?. Soy [mc]. Querría unirme a los Y-Men."
    mc "¿Me está preguntando cual es mi superpoder? Romper el universo. He conseguido que mi Meemaw diga que tengo razón dos veces en un minuto."
    mee "*Risa*"
    mc "¡Hush, Meemaw! Esto es importante."
    mc "¿Qué? ¿Que soy demasiado poderoso y debería probar con Nicolas Cabreo? OK, OK. Hasta otra."
    call BlinkXP ("c18s004_230" , "d") from _call_BlinkXP_2785
    mee "*Risa* Estás loco. Supongo que tenía que ver con algo de superhéroes, ¿no?"
    mc "Sí. Era una broma que hacíamos Jamaal y yo hace tiempo. Cuando alguno conseguía hacer una cosa muy grande."
    call BlinkXP ("c18s004_235" , "d") from _call_BlinkXP_2786
    mee "Hablando de cosas MUY grandes... ¿cómo estás tú? ¿Te van a doler los huevos luego?"
    mc "No te preocupes por mí. No tienes que hacer nada."
    call BlinkXP ("c18s004_240" , "d") from _call_BlinkXP_2787
    mee "{b}¿Qué?{/b}"
    mcp "(Oh... Mierda... Creía que se estaba ofreciendo a... La conversación con Betty me sigue jugando malas pasadas.)"
    mc "Nada, que estaré bien."
    call BlinkXP ("c18s004_245" , "d") from _call_BlinkXP_2788
    mee "Creo que debería volver a mi habitación... quiero darme una ducha antes de la comida y... quiero ayudar a [nor] con la comida..."
    mcp "(Parece que la he incomodado con la insinuación de que podía hacer algo con mi erección.)"
    mc "¿Ahora te deja acercarte a la comida si no es para comértela? *Risa*"
    call BlinkXP ("c18s004_250a" , "d") from _call_BlinkXP_2789
    mee "*Risa* No."
    mee "Me refería a llevarla a la piscina tal como estuviera preparada."
    mcp "(Y gastar una broma ha hecho que se ovide de ello.)"
    call BlinkXP ("c18s004_250b" , "d") from _call_BlinkXP_2790
    mee "Además tú tienes que ir a buscar a Maddie, ¿no?"
    mc "Sí. No tiene coche."
    call BlinkXP ("c18s004_255" , "d") from _call_BlinkXP_2791
    mee "Pues vístete y ve a buscarla. Ya me ocupo yo de limpiar todo esto."
    mc "Lo podemos hacer entre los dos en un momento."
    mee "No, no. Ve a buscarla y no la hagas esperar. Es una chica demasiado guapa para estar esperando."
    call BlinkXP ("c18s004_260" , "f") from _call_BlinkXP_2792
    "Unos minutos después..."
    mc "Me voy ya. ¿Estás segura de que no quieres que te ayude?"
    mee "Segura. Dame un beso y vete."
    scene c18s004_260d with dissolve
    "Empiezas un beso que se parece a los de los saludos."
    "Olivia cambia el beso, modificandolo completamente. A mejor."
    "Se parece mucho más al beso durante el masaje."
    "Los besos de los saludos no tienen lengua. La lengua que empieza el juego no es la tuya."
    "Olivia no hace ademán de apartarse."
    call BlinkXP ("c18s004_265" , "d") from _call_BlinkXP_2793
    mee "*Suspiro* Vete si no quieres que empape también el albornoz."
    mc "Besas muy bien, Meemaw."
    mee "Y tú besas demasiado bien para el bien de los dos."
    call BlinkXP ("c18s004_270" , "d") from _call_BlinkXP_2794
    mc "Te veo luego, Meemaw."
    mee "Hasta luego, [mc]."
    call BlinkXP ("c18s004_275" , "d") from _call_BlinkXP_2795
    mee "Ah, una cosa... tenemos que mantenerlo en secreto."
    mc "No te preocupes. Nadie iba a creerse el millón de orgasmos."
    call BlinkXP ("c18s004_280" , "d") from _call_BlinkXP_2796
    mee "Me refiero a lo de que te he dado la razón dos veces. *Risa*"
    mc "*Risa* Tampoco se lo iba a creer nadie."
    scene black with dissolve
    return
label c18s005_BirthdayOne:
    if _in_replay:
        menu:
            "¿Estás en una relación con Maddie?"
            "Sí":
                $ mad._var("route" , True)
                menu:
                    "¿Espiaste a [mar!t] en el probador de la tienda de [mad.nick]?"
                    "Sí":
                        menu:
                            "¿Qué tipo de relación tienes con Maddie?"
                            "Romance":
                                $ mad._var("romance", True)
                                $ mad._var("dom", False)
                                $ mad._var("sub", False)
                            "Acepté el chantaje.":
                                $ mad._var("romance", False)
                                $ mad._var("dom", True)
                                $ mad._var("sub", False)
                            "Le di la vuelta al chantaje.":
                                $ mad._var("romance", False)
                                $ mad._var("dom", False)
                                $ mad._var("sub", True)
                    "No":
                        $ mad._var("romance", True)
                        $ mad._var("dom", False)
                        $ mad._var("sub", False)
            "No":
                $ mad._var("route" , False)
                $ mad._var("romance", True)
                $ mad._var("dom", False)
                $ mad._var("sub", False)
        menu:
            "¿Está [nor] embarazada?"
            "Sí":
                $ nor._var("pregnant" , True)
            "No":
                $ nor._var("pregnant" , False)
    stop music fadeout (1.5)
    if mad._var("route"):
        "Vas a casa de Maddie."
    else:
        "Compruebas el mensaje que te envió Maddie con su dirección y vas a buscarla."
    call BlinkXP ("c18s005_005" , "d") from _call_BlinkXP_2797
    play music ("music/Stardust.ogg")
    "Cuando llegas te está esperando en la calle."
    mc "Hola, Maddie."
    if mad._var("route"):
        mc "¿Son los cuadros?"
        mad "Sí, ¿me ayudas a subirlos atrás?"
        call KissXP ("c18s005_010" , "f") from _call_KissXP_84
        "Una vez los cuadros depositados en la parte de atrás de la pick up..."
        mc "Buenos días, Maddie."
        mad "Buenos días, [mc]."
        call BlinkXP ("c18s005_015" , "d") from _call_BlinkXP_2798
    else:
        mc "¿Qué llevas ahí?"
        mad "Son mis regalos para las chicas. Espero que les guste."
        mc "Espera, que te ayudo a subirlos atrás."
        call BlinkXP ("c18s005_015" , "f") from _call_BlinkXP_2799
    mc "¿Quieres poner algo más detrás?"
    mad "No hace falta. En la mochila solo llevo el bikini y una toalla... y mi documentación... y el maquillaje..."
    mc "Entonces ya nos podemos ir."
    if mad._var("route"):
        call BlinkXP ("c18s005_020" , "d") from _call_BlinkXP_2800
        mad "Tengo una pregunta sobre esas pruebas de embarazo que me comentaste."
        mc "¿Has notado algo raro? Me dijiste que estabas tomando la píldora."
        call BlinkXP ("c18s005_025" , "d") from _call_BlinkXP_2801
        mad "No, no. Tan solo es que... soy un poco tonta. Empecé a tomármela el sábado pasado, con lo que el viernes no hacía una semana y no es segura al 100\%."
        mad "Me di cuenta anoche, cuando vi las pastillas que faltaban en la caja."
        mc "¿Quieres que paremos en una farmacia?"
        call BlinkXP ("c18s005_030" , "d") from _call_BlinkXP_2802
        mad "No... tienen muchos efectos secundarios y, con esas pruebas mágicas que tienes, si puedo confirmar si estoy embarazada antes de decidir si la tomo o no..."
        mc "Me parece una buena razón, pero ¿no hay un tiempo máximo para tomárselas?"
        mad "Lo miré en la web de la Clínica Marzo ayer. 120 horas, o cinco días si eres malo en matemáticas."
        mc "Entonces no hay demasiada prisa. Si hacemos la prueba al acabar la partida de DnD, podremos saber el resultado mañana, que serían 72 horas más o menos."
        call BlinkXP ("c18s005_035" , "d") from _call_BlinkXP_2803
        mad "Eso sería perfecto."
        mcp "(¿Perfecto saber si está embarazada o perfecto tener el resultado antes de las 120 horas?)"
        mc "¿Nos vamos entonces?"
        stop music fadeout (1.5)
    mad "Cuando quieras."
    if mad._var("route"):
        play music ("music/What-Ive-Found.ogg")
        call BlinkXP ("c18s005_040" , "f") from _call_BlinkXP_2804
        "Maddie está silenciosa durante todo el trayecto, hasta que al final hace una pregunta que no esperabas, sin atreverse a mirarte."
        mad "Si sale positivo... ¿quieres que me tome la píldora del día después?"
        mc "Es algo que tienes que decidir tú, Maddie."
        mc "Si estabas tomando la píldora, supongo que no querías quedarte embarazada."
        call BlinkXP ("c18s005_045" , "d") from _call_BlinkXP_2805
        mad "Habíamos estado juntos sólo una vez..."
        if not mad._var("romance"):
            mad "Aparte del día en el probador."
        mad "No quería quedarme embarazada."
        if not mad._var("romance"):
            mc "A mí tampoco me gustaría que te quedaras embarazada. No con el tipo de relación que tenemos."
        else:
            if persistent.walkthrough:
                $ wt1 = _("Sin consecuencias.")
                $ wt2 = _("Maddie tomará la píldora del día después si está embarazada.")
            else:
                $ wt1 = ""
                $ wt2 = ""
            menu:
                "A mí no me desagrada la idea." (wt = wt1):
                    pass
                "A mí tampoco me gustaría." (wt = wt2):
                    $ mad._var("pill" , True)
            $ resetWalkthrough ()
            mc "Pero ya te digo que es una decisión que debes tomar tú. Y me gustaría que lo habláramos si se da el caso."
        call BlinkXP ("c18s005_050" , "d") from _call_BlinkXP_2806
        if mad._var("romance"):
            mad "Lo entiendo. Es demasiado pronto en la relación..."
            mc "No es sólo eso. No querías quedarte embarazada por alguna razón y decidiste tomar la píldora."
            mc "No creo que sólo por habernos acostado tenga que cambiar nada."
        else:
            mad "Lo entiendo. Tampoco es el tipo de relación que querría tener con el padre de mis hijos."
            mc "Entonces no hay mucho más que hablar."
        call BlinkXP ("c18s005_055" , "d") from _call_BlinkXP_2807
        mad "Tienes razón..."
        "Maddie se sume en un silencio incómodo hasta llegar a casa."
    scene c18s005_060a with fade
    stop music fadeout (1.5)
    "Llegas a casa y metes el coche en el garaje."
    play music ("music/Acoustic-Inspirational.ogg")
    scene c18s005_060b with fade #nor y eri en topless
    "Al salir del garaje te encuentras con [nor] y [eri], que están llevando comida hacia la piscina."
    nor "¿Ya habéis llegado? Bienvenida a casa, Maddie."
    eri "Hola, Maddie. Hacía mucho que no nos veíamos."
    eri "[mc], ¿puedes ayudar a mi madre a llevar esto a la piscina?"
    mc "Sí, ningún problema."
    scene c18s005_060c with dissolve
    eri "Yo me llevo a Maddie a mi habitación para que se cambie. ¿Vamos?"
    mad "Yo he traído un bañador... de cuerpo entero..."
    scene c18s005_060d with dissolve
    eri "Si quieres llevarlo no hay ningún problema. Si quieres ir como mi madre o yo, te puedo prestar algo."
    mad "[mc], ¿puedes dejar los paquetes en la pick up? Ya los cogeré luego..."
    if nor._var("pregnant"):
        call BlinkXP ("c18s005_065" , "d") from _call_BlinkXP_2808
        mc "Dame esa bandeja. Me prometiste no llevar peso."
        nor "Es solo una bandeja de vasos de plastico, no pesa."
        mc "Da lo mismo. Yo tengo dos manos y puedo llevar las dos bandejas."
        nor "Vaaaale..."
    call BlinkXP ("c18s005_070" , "d") from _call_BlinkXP_2809
    mc "Ya me imaginaba que vosotras dos haríais topless. [eri] porque lo pidió, y tú porque ella lo pidió por ti."
    nor "Lo sé. Ella no quería dejarme sola siendo la única que hace topless."
    mc "¿Sólo sois vosotras dos?"
    call BlinkXP ("c18s005_075" , "d") from _call_BlinkXP_2810
    nor "*Risa* Casi suenas decepcionado."
    mc "No, no, creía que al menos una o dos más se iban a unir. ¿Nadie más se ha atrevido?"
    call BlinkXP ("c18s005_080" , "d") from _call_BlinkXP_2811
    nor "Eso lo descubrirás en breve."
    stop music fadeout (1.5)
    return

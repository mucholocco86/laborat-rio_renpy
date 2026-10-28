label c28:
    call version28 from _call_version28_1
    call updateProfileImagesStartS4 from _call_updateProfileImagesStartS4
    call updateChances from _call_updateChances
    if oma._var("route") and sai._var("route") and eil._var("route"):
        call c28s001_foursome from _call_c28s001_foursome
    else:
        call c28s001_noFoursome from _call_c28s001_noFoursome
    call c28s002_Kim from _call_c28s002_Kim
    call c28s002_SimGrateful from _call_c28s002_SimGrateful

    if sim._var("route"):
        call c28s003_SimLewd from _call_c28s003_SimLewd #se queda a dormir
    else:
        call c28s003_noSimLewd from _call_c28s003_noSimLewd
    #Day change Thursday
    call c28s004_MarRing from _call_c28s004_MarRing
    call c28s004_ScaGetsJob from _call_c28s004_ScaGetsJob
    call c28s004_DebKiaraTalk from _call_c28s004_DebKiaraTalk
    call c28s005_EriNor from _call_c28s005_EriNor
    call c28s004_LisaDress from _call_c28s004_LisaDress
    call c28s005_GavCall from _call_c28s005_GavCall
    call c28s005_AmaMad from _call_c28s005_AmaMad
    call c28s006_Kim from _call_c28s006_Kim
    call c28s002_Kat from _call_c28s002_Kat
    if not kim._var("route"):
        call c28s006_noKimLewd from _call_c28s002_noKimLewd
    call c28s007_Lis from _call_c28s007_Lis
    call c28s007_Kev from _call_c28s007_Kev
    $ c28Finished = True
    return

label c28s001_foursome:
    if _in_replay:
        $ mc._var("relationships" , 3, "set")
        call mrS3_sai_pregnant from _call_mrS3_sai_pregnant_3
        call mrS3_oma_pregnant from _call_mrS3_oma_pregnant_2
        call mrS3_eil_pregnant from _call_mrS3_eil_pregnant_3
        call mrS3_kia_route from _call_mrS3_kia_route_11
        if mc._var("relationships")<4:
            call mrS3_rels from _call_mrS3_rels_19
    scene c27s006_110e with dissolve
    play music ("music/NightJazzBeats.ogg")
    mc "No dudéis ni por un momento que esos regalos se vayan a quedar sin abrir."
    scene c28s001_005a with dissolve
    "Te acercas a [sai] y la besas apasionadamente. Su cuerpo vibra bajo tus manos."
    "Sabes que está excitada por lo que está a punto de pasar. Hablasteis varias veces de hacer un trío mientras estabais en Portland."
    "Nunca surgió la oportunidad o nunca encontrasteis a la chica adecuada. Nunca se planteó hacer un trío con un chico."
    "Ahora, su primera experiencia de sexo en grupo va a ser con dos mujeres a las que ha empezado a considerar más que amigas."
    call BlinkXS4 ("c28s001_010") from _call_BlinkXS4
    sai "Creo que hay una perra pelirroja esperando su beso. *Risa*"
    sai "*Risa* Después de las bromas que hemos hecho sobre sacarle los ojos, no quiero que use mis ideas contra mí."
    mc "No queremos que esos preciosos ojos oscuros acaben en un tarro, ¿no?"
    call BlinkXS4 ("c28s001_015") from _call_BlinkXS4_1
    eil "No se los sacaría a ella. *Risa* Recuerda que soy la Primera Concubina del harén."
    eil "*Risa* Si no soy importante para el sultán, quizás sean sus ojos los que acaben en un tarro."
    mc "¡Vamos, [eil]! Te juro que, en este momento, lo significas todo."
    mc "Las tres lo significáis todo."
    call BlinkXS4 ("c28s001_020") from _call_BlinkXS4_2
    oma "*Risa* ¿Y tus pensamientos se vuelven impuros al verla vestida así?"
    mc "*Risa* Al veros a las tres. Pero dame un momento antes de que la Primera Concubina me saque los ojos."
    scene c28s001_005b with dissolve
    "Coges a la hermosa pelirroja entre tus brazos y tus labios encuentran los suyos, entreabiertos para recibir tu lengua."
    "Su respiración transmite tanta excitación como los temblores de [sai]. No eres el único que está excitado por lo que va a pasar."
    "Va a ser su segundo sexo en grupo después de estar con [oma] en el bosque. Se pasó días hablando de aquel trío." id c28s001_foursome_fec024e6
    "Aquello lo propició ella, y esto parece que también. Adoras a [eil]."
    call BlinkXS4 ("c28s001_025") from _call_BlinkXS4_3
    eil "Creo que es el momento de que beses a nuestra policía o es capaz de arrestarnos a todos."
    mc "Yo no lo recomiendo. Las esposas son bastante incómodas."
    call BlinkXS4 ("c28s001_030") from _call_BlinkXS4_4
    oma "*Risa* Sabes que te las puedes quitar cuando quieras, ¿verdad?"
    mc "*Risa* Esperaba a que me dieras permiso para hacerlo. Decidimos probar y no es lo mío."
    oma "Tampoco lo mío. Prefiero sentir tus manos recorriendo mi piel."
    scene c28s001_005c with fade
    "Después de quitarte las esposas, abrazas fuertemente a [oma] mientras vuestros labios se unen otra vez."
    "Hace diez minutos que la tenías entre tus brazos y hace nueve que la echabas de menos."
    "Su cuerpo reacciona diferente a las otras dos mujeres, más tranquila después de haberte tenido para ella sola hace un rato."
    call BlinkXS4 ("c28s001_035") from _call_BlinkXS4_5
    sai "¿Vamos a caber todos en esa cama? Me parece un poco pequeña, ¿no?"
    mc "No te preocupes, encontraremos la forma de hacerlo."
    call BlinkXS4 ("c28s001_040") from _call_BlinkXS4_6
    oma "Creo que [sai] tiene razón. Id ocupándoos de nuestro invitado mientras yo hago algo."
    mc "¿Qué vas a hacer?"
    oma "Voy a probar algo. Intenta no correrte antes de que vuelva."
    mc "Creo que va a ser complicado con las dos fierecillas."
    call BlinkXS4 ("c28s001_045") from _call_BlinkXS4_7
    eil "No prometemos nada, pero, de momento, túmbate. Mjolnir ya está preparado para nosotras."
    mc "*Risa* ¿No puedo desenvolver mis regalos?"
    call BlinkXS4 ("c28s001_050") from _call_BlinkXS4_8
    sai "Habrá tiempo para eso. Pero nuestro regalo ya está desenvuelto y no queremos desaprovecharlo."
    sai "Por una vez, te toca obedecer órdenes y estar calladito."
    mc "Entonces me tendré que tumbar. ¿De verdad tengo que estar callado?"
    $ oma.nick = "Lexi"
    scene c28s001_055a with fade
    sai "Y no empieces a discutir." (multiple=2)
    eil "Puedes hablar, pero poco." (multiple=2)
    stop music fadeout (1.5)
    mc "Vale. Hablar poco y no discutir. Creo que puedo hacerlo."
    scene c28s001_055b with fade
    play music ("music/SensualJazzMedium2.ogg")
    sai "¿Qué le hacemos?"
    eil "Creo que lo que hablamos anoche estaría bien para empezar. Aunque falte [oma.nick]..."
    mc "¿Habláis de lo que me vais a hacer cuando compartís habitación?"
    scene c28s001_055c with hpunch
    sai "¡Por supuesto! Entre otras muchas cosas." (multiple=2)
    eil "¿Qué te hemos dicho de estar callado?" (multiple=2)
    mc "Pero me parece un tema muy interesante... Mis chicas hablando de mí..."
    scene c28s001_055d with dissolve
    sai "No hablamos sólo de ti, pero cuando [eil] propuso hacer esto, empezamos a fantasear..."
    eil "No esperábamos que la oportunidad llegara tan pronto, con lo que los planes son un poco... vagos."
    mc "*Risa* Estoy seguro de que no me voy a quejar por ello."
    scene c28s001_900pv with dissolve
    show c28s001_900v
    eil "Eso espero. Esto siempre te encantó, pero me faltaban manos."
    "Mientras [sai] te masturba y te acaricia los huevos, [eil] se dedica a acariciarte y a excitar tu glande con sus dedos."
    sai "A mí me pasaba lo mismo. Soy India, pero no soy Kali."
    "Notar las cuatro manos de las dos mujeres recorriendo tu cuerpo a la vez es una sensación increíble."
    mc "¿Qué tiene que ver tu prima en esto?"
    sai "He dicho Kali, no [kal.nick]."
    "No notas la diferencia en la pronunciación. Pero en ese momento te da lo mismo."
    call version28 from _call_version28_2
    scene c28s001_905pv with dissolve
    show c28s001_905v
    hide c28s001_900v
    "En ese momento lo que echas de menos es un espejo en el techo y poder observar los cuerpos de las dos mujeres."
    "Cuerpos muy diferentes, pero los dos preciosos. Los conoces a la perfección, pero nunca te cansarás de ellos."
    eil "¿Qué tal? ¿Cómo te sientes manoseado por dos mujeres a la vez?"
    mc "..."
    sai "*Risa* Le hemos dicho que esté callado y creo que nos va a hacer caso. Puedes contestar."
    mc "¿Mi ex-novia del instituto y mi ex-no-novia de la universidad jugando con Mjolnir? Creo que hay pocas cosas mejores. Al menos hasta que se una [oma]."
    sai "¡No me recuerdes lo tonta que fui! Y menos ahora que yo tengo el poder."
    "[sai] aprieta tus huevos entre sus dedos en un gesto juguetón. Lejos de ser doloroso, es sólo un pequeño aviso de que no te metas con ella."
    "Siempre le ha gustado tener el poder. O al menos una ilusión de poder que nunca ha utilizado."
    scene c28s001_910pv with dissolve
    show c28s001_910v
    hide c28s001_905v
    eil "Bueno, ahora las dos somos tus novias y no vamos a cometer los mismos errores que cometimos, ni siquiera cuando te marches."
    "Tienen más en común de lo que les hubiera gustado aceptar hace unas semanas. Tu relación a distancia con [eil] no funcionó."
    "La de [sai] no llegó a existir por su miedo a una relación a distancia. Ahora pasaréis meses separados, pero esta vez no habrá rupturas."
    sai "¡Céntrate, [eil]! ¡No hables de cosas tristes! Y tú no contestes. Relájate y disfruta."
    "No pensabas contestar. Tener a las dos mujeres produciendo sensaciones increíbles en tu polla no te deja mucho espacio para pensar en una respuesta ingeniosa."
    "Prefieres disfrutar de cada roce de sus dedos y mantenerte callado."
    call BlinkXS4 ("c28s001_060") from _call_BlinkXS4_9
    hide c28s001_910v
    oma "Ya está. Ya podéis venir."
    mc "¿A dónde? ¿Qué has hecho?"
    oma "Ya lo verás. Chicas, dejad a Mjolnir un rato."
    scene c28s001_055e with dissolve
    eil "Has aguantado como un campeón sin correrte."
    sai "*Risita* Me ha costado mantener el ritmo lento. Hubiera sido egoísta por nuestra parte hacer que te corrieras antes de que volviera [oma]."
    mc "*Risa* Sabéis que sois unas perras malas, ¿verdad?"
    scene c28s001_055f with dissolve
    eil "*Risa* Yo sí. [sai] me lo recuerda cada día."
    sai "*Risa* Pero pese a todo la quiero."
    oma "*Risa* Sin ella no estaríamos aquí ni habría un harén. Pero incluso sin harén la querríamos igual."
    eil "*Risa* Chicas, me vais a hacer ruborizar."
    mc "*Risa* Te pones guapísima cuando te ruborizas."
    scene c28s001_055g with dissolve
    eil "¿Te vas a quedar ahí o vas a venir a ver que ha preparado [oma]? ¿O tenemos que empezar sin ti?"
    oma "¡[eil]!" (multiple=2)
    sai "*Risa* No podemos empezar sin él." (multiple=2)
    stop music fadeout (1.5)
    mc "*Risa* Ahora voy."
    scene c28s001_065a with fade
    play music ("music/SensualJazzMedium2.ogg")
    mc "¿Qué has hecho, [oma]?"
    oma "Es un edredón enorme y súper mullido. Va a ser casi como estar en una cama."
    eil "No es tan grande como tu cama nueva, pero nos servirá para los cuatro."
    sai "¿Cómo lo hacemos? Se me hace un poco raro estar aquí en plan... 'Vamos a follar'..."
    mc "Empecemos como empezaríamos si estuviéramos solos... Ya estáis descalzas, pero todavía hay mucho regalo que desenvolver."
    scene c28s001_065b with fade
    "Abrazas a [sai] mientras la besas profusamente en su cuello. Sabes perfectamente cuáles son sus puntos débiles."
    sai "*Gemido* Me parece una forma excelente de empezar."
    "Las otras dos mujeres, con más experiencia en sexo grupal, os dan privacidad. Sabes que va a durar poco."
    scene c28s001_065An with dissolve
    "El sujetador desaparece poco después, mientras tus manos continúan recorriendo su cuerpo."
    sai "Primer regalo desenvuelto. Pero no olvides los demás."
    mc "Nunca lo haría, o correríamos el riesgo de que empecéis a tomaros celos."
    scene c28s001_070a with dissolve
    "Sin soltar a [sai], te giras hacia [oma], que está esperando su beso y lo recibe con pasión."
    sai "Me está poniendo muy cachonda esto..."
    "Las otras chicas no se quedan paradas. Se ha roto el hielo y todas quieren un trozo de ti."
    eil "Yo llevo cachonda desde que estábamos en la habitación."
    "[oma] no dice nada. Tan solo recorre con su lengua cada rincón de tu boca."
    scene c28s001_070An with dissolve
    "Para sorpresa de todos, [eil] elimina las bragas de [sai] de la ecuación en vez de hacerte algo a ti."
    sai "¡[eil.nick]! ¿Qué haces?"
    call BlinkXS4 ("c28s001_075") from _call_BlinkXS4_10
    eil "Quitarle un poco de trabajo a [mc]. Es demasiado lento desnudándonos y sabéis que nos esperan para cenar. No tenemos toda la tarde."
    mc "¡Hey! Este momento es irrepetible y no quiero ir con prisas."
    scene c28s001_080An with dissolve
    mc "Pero tienes parte de razón. Quiero ver a mis mujeres desnudas lo antes posible."
    todas "*Risa*"
    call BlinkXS4 ("c28s001_085") from _call_BlinkXS4_11
    eil "Por eso nos hemos quitado los zapatos nosotras. *Risa* Son muy bonitos, pero demasiado delicados para tus manos impacientes."
    mc "Lo dices como si no pudiera ser delicado..."
    call BlinkXS4 ("c28s001_090") from _call_BlinkXS4_12
    sai "*Risa* Puedes ser delicado en muchas cosas. Desnudar a una mujer no es una de ellas."
    mc "*Risa* Es muy complicado retenerse cuando sabes lo que hay debajo."
    scene c28s001_095An
    eil "¡Dios mío! Nunca dejaré de sorprenderme con lo peludo que es. No sé cómo puedes meter al Yeti en esas bragas diminutas, [oma.nick]."
    mc "*Risa* ¿Bragas mágicas?"
    call BlinkXS4 ("c28s001_100") from _call_BlinkXS4_13
    oma "Si [meg] pudo meter su coche en el garaje de [nor], mi Yeti cabe en unas bragas."
    mc "*Risa* Creo que ese garaje también es mágico."
    call BlinkXS4 ("c28s001_095") from _call_BlinkXS4_14
    mc "Pues sólo quedas tú..."
    eil "*Risa* Y me siento demasiado vestida ahora mismo."
    mc "Creo que te podemos ayudar entre todos."
    scene c28s001_105a with dissolve
    "La pelirroja se acerca y planta un sensual beso en tus labios. Sabes que ya está cachonda por cómo está respirando en tu boca."
    "Nunca hablasteis de tener un trío mientras estabais en el instituto, pero sabes que disfrutó mucho el trío con [oma]."
    "Añadir a [sai] es como cerrar el círculo. Nunca hubieras pensado que se harían tan amigas."
    scene c28s001_105An1 with dissolve
    "Tus manos eliminan el sujetador de la camarera. Delicadamente. No quieres que te acusen de ser un bruto."
    "Y quieres que pueda volver a usar esa lencería. Aún mejor si es en las mismas circunstancias."
    scene c28s001_105An2 with dissolve
    "Las otras dos chicas se toman su 'venganza' y retiran las bragas de la animadora a la que no has dejado de besar."
    sai "Parecía fácil cuando lo ha hecho ella... a mí se me ha liado con el liguero..."
    oma "Había que desabrocharlo antes. *Risa* Y te atreves a decir que [mc] no es delicado."
    scene c28s001_105f with dissolve
    sai "*Risa* Tenía ganas de ver cómo lo llevaba [eil.nick]. Yo casi afeitado, ella recortado y tú... el Yeti."
    oma "Tres chicas y tres formas distintas. Creo que [mc] no se va a quejar de la variedad."
    scene c28s001_105g with dissolve
    eil "*Risa* Si yo lo llevase como el Yeti, parecería un Big Foot, siendo tan pelirroja."
    mc "Sabéis que no me importa cómo lo llevéis, ¿verdad? Sois tres preciosas mujeres; las tres sois diferentes, pero las tres sois increíbles."
    scene c28s001_110a with dissolve
    "[eil] abandona tus brazos para arrodillarse al lado de sus amigas."
    eil "A veces parece increíble que siempre tengas las palabras adecuadas para hacernos sentir especiales."
    mc "No hace falta que os haga sentir especiales. Lo sois."
    oma "Y tú eres muy especial para nosotras. Nunca había hecho esto antes... con otras dos chicas. Pero nos haces sentir seguras."
    sai "Sabes las vueltas que le dimos a un trío en Portland. No lo dudé ni un momento cuando [eil] lo propuso anoche."
    mc "Eso es porque..."
    scene c28s001_110An with dissolve
    "Sin dejarte acabar la frase, tres bocas empiezan a recorrer a Mjolnir. Mejor seguir callado."
    eil "Duro como una roca..."
    "Es difícil no estarlo cuando tienes tres mujeres como estas dedicando sus atenciones a tu polla."
    oma "Me sorprendería si no fuera así..."
    "Si las cuatro manos de antes eran alucinantes, no tienes palabras para describir cómo se sienten los seis labios y las tres lenguas."
    sai "*Risita* Somos irresistibles..."
    "No lo vas a negar. Entre la doble paja de antes y la triple mamada de ahora, no crees que puedas durar mucho."
    scene c28s001_110g with dissolve
    "Todo se detiene abruptamente."
    sai "No querrás correrte ya, ¿verdad?"
    oma "Creo que estas dos chicas necesitan un poco de la atención de Mjolnir..."
    eil "Y no sólo en nuestras bocas. Túmbate."
    scene c28s001_115a with fade
    "Las obedeces sin rechistar, sin saber qué tienen planeado."
    oma "¿Cuál de vosotras quiere empezar con el plato fuerte?"
    sai "¿No quieres empezar tú? Es tu casa..."
    eil "Creo que deberías empezar tú, [sai]. [oma.nick] ha tenido a [mc] para ella sola un rato y supongo que querrá descansar."
    scene c28s001_115b with dissolve
    sai "¿Y tú? ¿No quieres participar?"
    eil "Yo puedo esperar y ser la última. No tengo prisa. [oma] y yo ya lo hicimos hace días y por eso pienso que deberías empezar tú."
    mc "Chicas, estoy aquí abajo..."
    oma "Venga, elegir vuestros sitios antes de que nuestro chico se aburra."
    mc "*Risa* No os preocupéis, no me aburro en absoluto. Veros planificar algo así me hace pensar en [emm]."
    scene c28s001_115c with dissolve
    sai "No te metas con [emm]."
    eil "*Risa* No sé si enfadarme porque te has metido con [emm] o porque nos has comparado con [emm]."
    oma "*Risa* Sea como sea, las vas a pagar."
    call BlinkXS4 ("c28s001_120") from _call_BlinkXS4_15
    "[oma] se deja caer sobre tu pecho. Su duro culo, aposentado sin delicadeza, casi te hace perder el aire."
    oma "No nos hagas caso. Yo me siento honrada si me comparas con [emm]. Si no fuera por estas dos, sería un manojo de nervios ahora mismo."
    oma "Acuérdate de cómo estaba en el lago..."
    mc "Guapísima. Estabas guapísima."
    scene c28s001_120An with dissolve
    "[sai] se sitúa, como siempre, de espaldas a ti, y se empala en tu polla sin mediar palabra. Notas cómo su húmedo coño abraza a Mjolnir en todo el recorrido."
    sai "*Gemido* Necesitaba esto... *Jadeo*"
    mc "*Risa* Yo llevo tumbado aquí un rato..."
    scene c28s001_120f with dissolve
    eil "Pues es hora de que dejes de descansar. Te estás volviendo vago."
    mc "Pero nadie presta atención a [oma]... Déjame un momento a ver si..."
    call BlinkXS4 ("c28s001_125") from _call_BlinkXS4_16
    oma "A [oma] déjala tranquila. Aún estoy sensible después de lo de antes y..."
    scene c28s001_125e with hpunch
    oma "*Gemido* ¡Oh!"
    scene c28s001_125d with dissolve
    mc "¿Estás segura de que quieres que te deje tranquila?"
    oma "No. Ya no estoy segura de nada."
    call BlinkXS4 ("c28s001_130") from _call_BlinkXS4_17
    sai "Lo siento chicas, pero no puedo esperar más..."
    sai "Sentir esta polla, inmóvil dentro de mí, es demasiado."
    scene c28s001_920pv with dissolve
    show c28s001_920v
    "La hermosa mujer de piel olivácea empieza a cabalgarte, poniendo todo en marcha como si no hubiera habido una pausa desde que os habéis movido al salón."
    sai "*Gemido* ¡Oh, sí! *Jadeo* Mucho mejor así. *Gemido*"
    "Su cuerpo se mueve a un ritmo confortable para ella, chocando de vez en cuando con [oma], a la que has empezado a masturbar."
    oma "*Jadeo* ¡Por el amor de Dios! *Gemido* ¿Por qué no se nos ocurrió esto antes? *Jadeo*"
    "El coño de [oma], cerrándose alrededor de tu dedo, está tan húmedo como el que está abrazando tu polla."
    eil "*Gemido* Porque nunca habíamos dormido juntas. *Jadeo* Ni tenido horas para planearlo. *Gemido*"
    "Los sabores de [eil] inundan tu lengua mientras recorres cada pliegue de su vagina."
    scene c28s001_925pv with dissolve
    show c28s001_925v
    hide c28s001_920v
    "Tener a las tres mujeres encima tuyo, proporcionándoles placer a la vez, es una sensación muy satisfactoria."
    oma "*Jadeo* ¡Justo ahí! *Gemido* ¡Tu dedo es CASI tan bueno como tu lengua! *Jadeo*"
    "Pese a la posición poco natural de tu brazo, consigues que la preciosa colombiana disfrute de tu dedo."
    eil "*Gemido* Lo único que puede competir con su lengua es Mjolnir. *Jadeo* Y esa polla ganaría por poco. *Gemido*"
    "Conoces el cuerpo de [eil] lo suficiente como para saber que no le queda mucho para llegar a su primer orgasmo."
    sai "*Jadeo* Cuando estés aquí me lo dices. *Gemido* Esta polla es increíble, y aún más sabiendo que estáis detrás mío. *Jadeo*"
    "A [sai] tampoco le queda demasiado. Si a ti te ha puesto muy cachondo estar con tres mujeres, a ellas les ha puesto igual de cachondas compartirte."
    scene c28s001_930pv with dissolve
    show c28s001_930v
    hide c28s001_925v
    "La que más lejos parece de llegar a su orgasmo es [oma], pero eso se debe a que tu dedo no es tan hábil como tu lengua o tu polla."
    "Y a que ella ya ha tenido varios orgasmos en el rato que habéis estado a solas."
    eil "*Gemido* Si sigues así no voy a poder aguantar mucho más. *Jadeo* A mí no me queda casi nada. *Gemido*"
    "Lo sabes y no tienes intención de bajar el ritmo. También sabes que [sai] está muy cerca."
    sai "*Jadeo* Corrámonos a la vez, [eil.nick]. *Gemido* Lo he estado reteniendo... *Jadeo*"
    "De querer sacarle los ojos a esperarla para correrse... ¡Cómo ha cambiado todo en unas pocas semanas!"
    oma "*Gemido* A mí no me esperéis... *Jadeo* Aún me queda... *Gemido*"
    "No le queda tanto como quiere hacerles creer a las otras dos chicas, pero quiere ir a su ritmo."
    call OrgasmXS4 ("c28s001_135") from _call_OrgasmXS4
    eil "*JADEO* ¡SÍ! *GEMIDO* ¡JODER! *JADEO*"
    "La primera en explotar es [eil], regalándote todos sus jugos en un intenso orgasmo que recorre su cuerpo, casi haciéndole perder el precario equilibrio."
    oma "*Gemido* [sai], es tu turno. *Jadeo*"
    "El cuerpo de la preciosa estudiante está a punto de alcanzar el pico de tensión que precede a su orgasmo."
    sai "*Jadeo* Casi... *Gemido* ahí... *Jadeo*"
    "Sabes que el 'casi' va a durar poco. Puedes notar cómo su coño empieza a estrujar a Mjolnir."
    call OrgasmXS4 ("c28s001_140") from _call_OrgasmXS4_1
    sai "*GEMIDO* ¡AARGHHH! *JADEO* ¡ES ENORME! *GEMIDO*"
    "Su coño abraza con fuerza tu astil. Tan solo puedes imaginar la cara que estará poniendo ahora mismo."
    oma "*Jadeo* Los vecinos van a pensar que están matando a alguien. *Gemido*"
    "Tan solo esperas que no llamen a la policía. No sería divertido que un compañero de [oma] la llamase a ver si está bien."
    eil "*Gemido* Mientras no te llamen para ver si estás viva en medio del orgasmo... *Jadeo*"
    "A veces te sorprendes de cuantas veces [eil] y tú pensáis lo mismo al mismo tiempo."
    scene c28s001_915pv with dissolve
    show c28s001_915v
    hide c28s001_930v
    "Mientras las mujeres que tienes empaladas en tu polla y en tu lengua continúan con sus orgasmos, te centras en la mujer sentada sobre tu pecho."
    eil "*JADEO* Sólo quedáis tú y [mc]... *GEMIDO* Correos antes de que las piernas dejen de aguantarme. *JADEO*"
    sai "*GEMIDO* Las mías se están convirtiendo en gelatina... *JADEO* No quiero parar antes de que os corráis. *GEMIDO*"
    "No te extraña que las tres chicas quieran que sus orgasmos coincidan en el tiempo. Se está creando una hermandad sorprendente entre ellas."
    "Tú has estado reteniendo tu orgasmo, pero ya está trepando por tus pantorrillas. Quieres ser el último en correrte."
    oma "*JADEO* Casi he llegado... *GEMIDO* Ese dedo es como un Mjolnir diminuto... *JADEO*"
    "Por cómo se mueven sus labios, sabes que ella está colaborando, acariciando su clítoris. Supones que el dedo al que se refiere es el tuyo."
    call OrgasmXS4 ("c28s001_145") from _call_OrgasmXS4_2
    hide c28s001_915v
    oma "*GEMIDO* ¡JODER! *JADEO* ¡OH, DIOS MÍO! *GEMIDO*"
    "[oma] no tarda en explotar alrededor de tu dedo y de los suyos, tensándose hasta casi romperse por enésima vez desde que habéis llegado a su apartamento."
    eil "*JADEO* Ya solo quedas tú... *GEMIDO*"
    sai "*GEMIDO* Y está a punto... *JADEO* Puedo notarlo... *GEMIDO*"
    "Cada vez te cuesta más retener tu clímax, y ya no tiene sentido una vez las tres mujeres se han corrido y empiezan a moverse como muñecas descoyuntadas."
    if persistent.pregnancy and not sai._var("pregnant"):
        if persistent.walkthrough:
            $ wt1 = _("[sai] embarazada.")
            $ wt2 = _("Sin consecuencias.")
        else:
            $ wt1 = ""
            $ wt2 = ""
        menu:
            "Correrte dentro. Ir a por el bebé." (wt = wt1):
                $ sai._var("pregnant", True)
                $ sai._var("undiscoveredPregnancy", True)
                play sound ("music/OldMusicBox5.ogg")
            "Correrte dentro." (wt = wt2):
                pass
    $ resetWalkthrough ()
    call OrgasmXS4 ("c28s001_150") from _call_OrgasmXS4_3
    mc "¡Mpfft!"
    "Mientras las tres mujeres alcanzan los picos de sus orgasmos, descargas una enorme cantidad de semen en el coño de [sai]."
    sai "*JADEO* ¡SÍ! *GEMIDO* ¡LLÉNAME! *JADEO*"
    "Su vagina intenta ordeñar hasta la última gota de tu semen, que sigue siendo abundante después de tus dos orgasmos con [oma]."
    scene c28s001_155a with fade
    stop music fadeout (1.5)
    "Al cabo de un rato, las tres mujeres se derrumban, agotadas por sus orgasmos..."
    play music ("music/Stardust.ogg")
    eil "*Gemido* ¿Qué os ha parecido, chicas? *Jadeo* Para mí ha sido increíble... *Gemido* Pero creo que no nos hemos puesto bien... *Jadeo*"
    "La mente de [eil], después de haber propuesto la experiencia, empieza a buscar cómo mejorarla."
    mc "¿No os ha gustado?"
    oma "*Jadeo* Creo que sé a lo que se refiere [eil]. *Gemido* Me ha encantado... *Jadeo* Pero no nos veíamos las unas a las otras... *Gemido*"
    "Eso explica la frase de [eil]. Sin verse, ha sido casi como si estuvieran individualmente contigo."
    "Ha sido totalmente diferente para ti. Las podías notar a las tres."
    sai "*Gemido* Creo que, para la próxima vez, debemos estudiarlo mejor... *Jadeo*"
    mc "¿Próxima vez? ¿Ya hemos acabado?"
    scene c28s001_155b with dissolve
    "Las tres mujeres te miran divertidas a la vez que expectantes."
    eil "*Risa* ¿Llevas media tarde con [oma] y crees que vas a poder con un segundo asalto con nosotras?"
    sai "*Risa* Para ti los asaltos son individuales. Sólo te corres una vez. A veces compadezco a los hombres."
    oma "*Risa* ¡Es un semental! Seguro que se recupera muy rápido para el segundo asalto."
    "No ha soltado tu polla, cubierta de tu semen y los jugos de [sai], en ningún momento, y sus caricias han hecho que no hayas perdido la erección."
    mc "*Risa* Estoy seguro de que, con las debidas atenciones, no voy a tardar mucho en estar preparado."
    scene c28s001_155c with dissolve
    sai "¿Os ocupáis vosotras de mantenerlo entretenido mientras voy a lavarme? Los dedos de [mc] ya me estaban buscando de nuevo..."
    oma "No te preocupes, no se va a aburrir. Pero no tardes demasiado, o [eil] y yo empezaremos sin ti."
    eil "Yo necesito echarme agua en la cara. Esos orgasmos han sido muy intensos y estoy acalorada. Te acompaño."
    mc "Pues me quedo con [oma], recibiendo atenciones como un señor."
    todas "*Risa*"
    call BlinkXS4 ("c28s001_160") from _call_BlinkXS4_18
    oma "¿Qué te ha parecido la sorpresa que te hemos preparado?"
    mc "Ha sido increíble. Sois muy peligrosas si se os deja planear cosas, pero no me quejo del resultado."
    mc "¿Y a ti? ¿Qué tal tu segundo sexo en grupo?"
    call BlinkXS4 ("c28s001_165") from _call_BlinkXS4_19
    oma "Diferente de la primera vez. Mucho más relajada. Aquella vez estaba muy nerviosa."
    oma "Si no hubiera sido por [eil]..."
    mc "Si no hubiera sido por [eil], tampoco hubiera pasado lo de hoy, por lo que he entendido."
    eil "*Gritando desde el lavabo* Estoy oyendo mi nombre. Espero que no me critiquéis."
    mc "*Risa* No te preocupes."
    call BlinkXS4 ("c28s001_170") from _call_BlinkXS4_20
    oma "Tienes razón. Fue la artífice de aquello y lo ha sido también de lo de hoy."
    oma "Pero basta de charlas. Tengo que preparar a Mjolnir para cuando vuelvan las chicas."
    mc "Míralo y dime si necesita preparación."
    scene c28s001_170d with dissolve
    oma "No necesito mirarlo, lo tengo en la mano y sé lo duro que está. Me refiero a si has recuperado el aliento."
    mc "*Risa* Sabiendo lo que viene, me moriría de vergüenza si tardara más de cinco minutos en estar listo."
    mc "Espero no tardar más de cinco minutos al menos hasta cumplir los 50."
    oma "Espero que ni siquiera entonces. Pero habrá que limpiarlo un poco antes del siguiente capítulo..."
    scene c28s001_170e with dissolve
    "[oma] se mete tu polla en la boca para limpiarlo de los restos de tu anterior corrida."
    "Si no hubieras estado duro como una piedra antes de que lo hiciera, lo estarías ahora."
    "Aún hay esperanza para el [mc] de 50 años."
    call BlinkXS4 ("c28s001_175") from _call_BlinkXS4_21
    oma "Tiene un sabor diferente, mezclado con los jugos de [sai]..."
    mc "¿Agradable o desagradable?"
    oma "Tan solo diferente. Sabes que yo, a diferencia de [eil], no tengo curiosidad por las chicas."
    if persistent.lesbian:
        mc "Lo sé. Aún no ha encontrado con quién experimentar."
    else:
        mc "Lo sé. Pero creo que es más curiosidad académica que real."
    scene c28s001_175d with dissolve
    oma "¡Chicas! Estáis tardando mucho y Mjolnir ya está listo. Y yo no voy a poder contenerme..."
    sai "*Desde el lavabo* Empieza tú."
    eil "*Desde el lavabo* No hace falta que nos esperes."
    call BlinkXS4 ("c28s001_180") from _call_BlinkXS4_22
    oma "*Risa* Eres testigo de que me han dado autorización."
    mc "*Risa* Sí, Agente. Puedo declararlo en el juicio."
    stop music fadeout (1.5)
    oma "Pues prepárate. Allá voy."
    scene c28s001_185AnBlink with dissolve
    play music ("music/CCFunk.ogg")
    "[oma] se sube encima tuyo y se empala en Mjolnir. Puedes notar lo húmeda que está después de todo lo que ha pasado desde que habéis abandonado el café."
    oma "*Gemido* Nunca me cansare de esto. *Jadeo* Sentir cómo me distiendes cuando entras es alucinante. *Gemido*"
    "Ese primer abrazo también es increíble para ti."
    mc "Te entiendo."
    scene c28s001_940pv with dissolve
    show c28s001_940v
    "[oma] empieza a subir y a bajar a lo largo del astil de tu polla, sin mostrar signos de cansancio después de todo lo que ha pasado en su habitación."
    oma "*Jadeo* Tampoco me cansaré nunca de esto. *Gemido* Nunca me cansaré de ti. *Jadeo*"
    "No crees que puedas cansarte nunca de la hermosa colombiana. Por tu mente pasa una imagen de los dos repitiendo esto cuando seáis ancianos."
    mc "Yo tampoco, mi amor."
    "Obviamente no será en un edredón en el suelo. Necesitaréis camas cómodas."
    oma "*Gemido* ¡Chicas! *Jadeo* ¡Venid rápido! *Gemido* ¡La fiesta ha empezado! *Jadeo*"
    scene c28s001_185g with fade
    eil "*Risa* Lo estamos viendo..."
    sai "*Risa* La perra no nos ha esperado."
    mc "*Risa* Le habéis dado autorización para empezar."
    oma "*Risa* Sois unas pinches hijueputas. *Gemido* ¡Uníos ya!"
    "Eso suena a mezcla de Méjico y Colombia. Criarse en San Diego, con la mezcla de culturas, produce expresiones extrañas."
    scene c28s001_950pv with dissolve
    show c28s001_950v
    hide c28s001_940v
    oma "*Gemido* ¿Os vais a quedar ahí de pie? *Jadeo* Uníos antes de que nuestro hombre se corra. *Gemido*"
    mc "No os preocupéis por mí, aún me queda para correrme. Pero os podéis unir cuando queráis."
    sai "Creo que esta vez prefiero mirar. Antes me lo he perdido todo..."
    eil "¿Nos sentamos en el sofá y los miramos follar?"
    sai "Yo creo que voy a ir mejor a la alfombra. Te dejo el sofá para ti."
    scene c28s001_935pv with dissolve
    show c28s001_935v
    hide c28s001_950v
    "[oma] continúa cabalgándote como si la conversación que acaba de suceder no hubiera tenido lugar."
    oma "*Jadeo* Ellas se lo pierden... *Gemido*"
    "Hay un sonido un poco extraño en su voz que no eres capaz de concretar entre sus gemidos. Quizás no era la escena de sexo en grupo que estaba esperando."
    mc "¿Decepcionada?"
    oma "*Gemido* No. *Jadeo* Si no quieren participar... *Gemido* Descubriré si me gusta follar con público... *Jadeo*"
    "Es algo en lo que no habías pensado. Sabes que [sai] odia mostrar su cara cuando se corre, pero ¿cómo se sienten [oma] y [eil] sobre tener sexo con las otras chicas mirando?" id c28s001_foursome_8d2457a2
    scene c28s001_190a with dissolve
    eil "Pues espero que te guste... Estáis espectaculares..."
    sai "Me estoy poniendo cachonda sólo con veros..."
    eil "Deberíamos pedirles a [ama] y a [eva] cámaras para grabar esto... Cuando lo repitamos..."
    sai "Sería un buen material para pajas cuando [mc] esté en Aruba..."
    mc "No sé si podremos repetirlo antes de que me vaya..."
    scene c28s001_190b with dissolve
    eil "Pues habrá que grabarlo en la memoria..."
    sai "Creo que va a ser difícil borrarlo..."
    scene c28s001_190c with dissolve
    eil "¡Por el amor de Dios! Ver el precioso cuerpo de [oma] subiendo y bajando por Mjolnir es increíble..."
    sai "Deberíamos haber cogido los móviles y grabarlo... pero no pienso ir a por él ahora..."
    scene c28s001_945pv with dissolve
    show c28s001_945v
    hide c28s001_935v
    "[oma] se tensa por un momento. Te preguntas si su orgasmo está a punto de llegar, pero la tensión pasa inmediatamente."
    oma "*Jadeo* No te lo vas a creer. *Gemido*" id c28s001_foursome_3989cdbd
    mc "¿Han empezado a tocarse? Yo también me pajearía si sólo pudiera verte."
    "Se vuelve a tensar inmediatamente. Esta vez no es sorpresa, sino placer por tus palabras."
    oma "*Gemido* ¿Cómo sabes lo que están haciendo? *Jadeo*"
    mc "Conozco demasiado bien a mis chicas..."
    "Sabías que [eil] lo iba a hacer en el momento en que ha propuesto ir al sofá."
    "Si [sai] se hubiera sentado con ella, estás casi seguro de que [eil] intentaría magrearla mientras se pajean."
    scene c28s001_965pv with dissolve
    show c28s001_965v
    hide c28s001_945v
    "Pero [sai] ha elegido ir a la alfombra, con lo que queda en algo individual."
    sai "*Gemido* Joder. *Jadeo* Sois alucinantemente hermosos follando juntos. *Gemido*"
    "La ubicación en la que están evita que las mires. De todas formas, no querrías apartar los ojos de [oma]."
    sai "*Jadeo* Es una de las cosas más bonitas que he visto nunca. *Gemido*"
    "Y te estás perdiendo la mitad de la acción por tenerlas a tu espalda. Hay que estudiar mejor las posiciones para la próxima vez."
    scene c28s001_960pv with dissolve
    show c28s001_960v
    hide c28s001_965v
    eil "*Gemido* Te dije que [oma] era espectacular. *Jadeo* Y desde aquí arriba os veo a los tres. *Gemido*"
    "Al final resulta que eres el que tienes las peores vistas, pero, de todas formas, no te quejarás por sólo poder mirar a [oma]." id c28s001_foursome_91e6cc73
    eil "*Jadeo* Y tengo ganas de ver cómo te corres tú, [sai]. *Gemido* No sabría decir cuál de las dos está más buena. *Jadeo*"
    "Tú no podrías decir cuál de las tres está más buena. Son tres mujeres alucinantes. Y tú eres un hombre afortunado."
    eil "*Gemido* A mí me queda poco para correrme... *Jadeo* No voy a poder esperaros... *Gemido*"
    scene c28s001_955pv with dissolve
    show c28s001_955v
    hide c28s001_960v
    oma "*Jadeo* Yo también estoy a punto... *Gemido* Me está poniendo muy cachonda la situación. *Jadeo*"
    "Y tú sin poder tener una buena panorámica. Aunque cueste creerlo, imaginarte la escena que ocurre a tus espaldas también te está poniendo cachondo."
    sai "*Gemido* A mí no me esperéis... *Jadeo* Mis pajas suelen ser larguísimas. *Gemido*"
    "Sus pajas son largas cuando se las hace ella. Cuando se las has hecho tú, se corre tan rápido como follando."
    eil "*Jadeo* Ve a tu ritmo... *Gemido* No es una competición... *Jadeo*"
    "[eil] sabe que todo es una competición para [sai]. O al menos lo era hace unas semanas."
    call OrgasmXS4 ("c28s001_195") from _call_OrgasmXS4_4
    eil "*GEMIDO* ¡SÍ! *JADEO* ¡JODER! *GEMIDO* ¡OS QUIERO A TODOS! *JADEO*"
    "Tal como ha anunciado, la primera en correrse es [eil], aunque no lo puedes ver, imaginas cómo su cuerpo se estará tensando en este momento."
    "Es una maravillosa imagen que has visto cientos de veces y no te cansarás de ver nunca."
    "Perdértelo esta vez tiene un sabor agridulce."
    call OrgasmXS4 ("c28s001_200") from _call_OrgasmXS4_5
    hide c28s001_955v
    oma "*JADEO* ¡HOSTIA PUTA! *GEMIDO* ¡ESTO ES INCREÍBLE! *JADEO*"
    "No te pierdes el orgasmo de [oma], sin embargo. Como siempre, se pone guapísima al correrse."
    "Es otra visión de la que nunca tienes suficiente. La tórrida dulzura del momento suaviza la parte amarga de haberte perdido el orgasmo de [eil]."
    "Adoras a estas mujeres y no quieres perderte ninguno de sus momentos de placer."
    "Las convulsiones en su coño están a punto de llevarte más allá de tu límite."
    if persistent.lesbian:
        scene c28s001_210AnBlink with dissolve
    "[oma] disfruta de los últimos coletazos de sus orgasmos mientras ve a sus dos amigas, a sus dos hermanas, disfrutar en diferentes puntos de los suyos."
    "[eil] lidiando con las últimas oleadas de los suyos, mientras [sai] espera que llegue el suyo."
    $ eil._var("bicurious" , False)
    if not persistent.lesbian:
        #"Niegas con la cabeza. No sabes cómo va a reaccionar [sai] y, además, sabes que está a punto de correrse."
        pass
    else:
        oma "*Jadeo* *Susurrando* Mira a [eil]... *Gemido* Creo que quiere decirte algo... *Jadeo*"
        scene c28s001_215An with dissolve
        "La pelirroja hace una seña en dirección a [sai], pidiéndote permiso para ayudarla."
        "Son hermanas en esto, pero sabe que [sai] es tu novia y no la suya."
        "Pero sabes que lleva tiempo queriendo experimentar y sería una forma de cerrar el círculo que iniciaron hace tiempo."
        if persistent.walkthrough:
            $ wt1 = _("[eil] ayudará a [sai] a alcanzar el orgasmo.")
            $ wt2 = _("Sin consecuencias.")
        else:
            $ wt1 = ""
            $ wt2 = ""
        menu:
            "Asientes con la cabeza." (wt = wt1):
                $ eil._var("bicurious" , True)
            "Niegas con la cabeza." (wt = wt2):
                "No sabes cómo va a reaccionar [sai] si [eil] empieza a acariciarla. Además, sabes que la mujer morena está a punto de correrse."
    $ resetWalkthrough ()
    if eil._var("bicurious"):
        "Ha estado deseando hacerlo desde el trío en el bosque, y no crees que sea bueno denegarle la oportunidad." id c28s001_foursome_2eae200f
        "Seguramente te hubieras negado si te lo hubiera preguntado sobre [oma], ya que ha dicho explícitamente que no le interesan las chicas y no sabes cómo podría reaccionar."
        scene c28s001_225An2 with dissolve
        "[eil] baja del sofá y pone sus dedos sobre la mano que la otra chica está usando para masturbarse." id c28s001_foursome_b043ecb9
        sai "*Jadeo*"
        "La sorpresa se refleja en los oscuros ojos por un momento, hasta que entiende los motivos de la caricia."
        scene c28s001_225f with dissolve
        eil "¿Me permites ayudarte?"
        sai "*Gemido* Nunca he hecho nada con otra chica..."
        eil "Yo tampoco, pero si te apetece probar... Sin ninguna obligación..."
        call BlinkXS4 ("c28s001_230") from _call_BlinkXS4_23
        sai "*Jadeo* ¿Pararás si te lo pido?"
        call BlinkXS4 ("c28s001_235") from _call_BlinkXS4_24
        eil "Por supuesto. A lo mejor soy horrible haciéndolo..."
        eil "La experiencia que tenemos es con [mc], y las dos sabemos lo bueno que es..."
        scene c28s001_240An with dissolve
        "Las dos te miran por un momento."
        "[eil] excitada, esperando que no cambies de opinión."
        "[sai] dudosa, pidiéndote autorización para aceptar."
        "En ningún momento ha retirado la mano de su coño, presionando sus labios para no perder el orgasmo que estaba a punto de llegar."
        "Pero también protegiéndolo hasta que dieras tu visto bueno a lo que está por pasar."
        "Asientes a las dos mujeres."
        sai "*Gemido* Adelante..."
        eil "Túmbate..."
        scene c28s001_980pv with dissolve
        show c28s001_980v
        "[oma] no ha dejado de cabalgarte en los segundos que ha durado la conversación. Tu orgasmo, a punto de llegar, se ha alejado un poco, pero retorna con fuerza."
        sai "*GEMIDO* ¡Joder! *JADEO* ¡Esperaba un dedo, no la lengua! *GEMIDO*"
        "Por un momento, piensas que le va a pedir a la pelirroja que pare."
        eil "*Slurp Inquisitivo*"
        "Parece que [eil] ha pensado lo mismo."
        oma "*GEMIDO* ¡SI NO DICE NADA, SIGUE COMIÉNDOTELA! *JADEO*"
        "Todos habéis pensado lo mismo. Pero la petición de [sai] no llega a producirse."
        "Sin embargo, tu límite está sobrepasado y no puedes retrasar más tu orgasmo."
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
        call OrgasmXS4 ("c28s001_205") from _call_OrgasmXS4_6
        mc "¡Mpfft!"
        "Sin poder aguantar más, explotas en el interior de [oma], soltando un gran géiser de semen que la llena por completo."
        oma "*GEMIDO* ¡JODER, SÍ! *JADEO* ¡LLÉNAME! *GEMIDO*"
        "Tu chorro de leche la pilla en medio del punto álgido de uno de sus orgasmos, incrementando aún más su placer."
        eil "*Gemido* *Slurp* *Jadeo*"
        "Sabes que [eil], con su generosidad habitual, no va a dejar de lamer a [sai] para ver cómo te corres."
        sai "*Jadeo* Aún me queda un poco... *Gemido*"
        "Su voz te indica que le queda menos de lo que dice."
        scene c28s001_970pv with dissolve
        show c28s001_970v
        hide c28s001_980v
        "[eil] sigue lamiendo el coño de su amiga, en la primera experiencia lésbica de ambas."
        eil "*Gemido* *¿Slurp? *Jadeo*"
        "Sus gemidos te indican que lo está disfrutando. No crees que nunca se vuelva bisexual, pero crees que le podría gustar dar placer a otras mujeres a las que quiere." id c28s001_foursome_fd6774ea
        sai "*Jadeo* Vas bien... *Gemido* Un poco más arriba... *Jadeo*"
        scene c28s001_245a with dissolve
        "[oma] se baja de encima tuyo antes de que acaben sus orgasmos para permitirte darte la vuelta y poder observar el espectáculo."
        "Tu cuello se lo agradece inmensamente. Parece que la generosidad es una característica de todas estas chicas."
        oma "Son alucinantes. ¿Te pone cachondo verlas?"
        mc "Acabo de correrme... pero sí... es un espectáculo precioso... y tórrido."
        "Ninguno de los dos sois capaces de apartar los ojos de las dos mujeres."
        oma "Yo no me atrevería. Ni a hacerlo ni a dejar que me lo hagan..."
        mc "Yo no le hubiera dado autorización si hubieras sido tú."
        scene c28s001_245b with dissolve
        mc "Dijiste que no estabas interesada y, hasta que no digas lo contrario, no lo haría."
        sai "*Gemido* ¡Joder! *Jadeo* ¡Parecéis comentaristas en un partido de cricket! *Gemido*"
        "Tiene razón. Estáis hablando de ellas como si fuera un espectáculo sólo para vuestros ojos."
        oma "¿Por qué no te unes y le comes el coño a [eil]? Veros a los tres sería la guinda del pastel."
        "Ni siquiera intenta susurrar."
        scene c28s001_245c with dissolve
        "[eil] deja por un segundo de lamer el coño de su hermana de otro continente para lanzarte una fiera mirada."
        eil "¡Quédate ahí!"
        "Su tono no deja lugar a dudas. Quiere disfrutar la experiencia completa sin tu lengua distrayéndola."
        scene c28s001_975pv with dissolve
        show c28s001_975v
        hide c28s001_970v
        "La  chica irlandesa vuelve a hundir su boca en el coño de la mujer india, lamiendo y chupando donde cree que va a producir más placer a su amiga."
        sai "*GEMIDO* Si sigues así voy a correrme en seguida. *JADEO* Eres CASI tan buena como [mc]. *GEMIDO*"
        eil "*Gemido* *Slurp feliz* *Jadeo*"
        "Casi te sientes ofendido. Si [eil] es casi tan buena como tú en su primera vez..."
        "Pero, pensándolo bien, tiene cierto sentido. Su lengua toca los mismos puntos sensibles de [sai] que la tuya ha tocado mil veces en [eil]."
        sai "*JADEO* Estoy llegando... *GEMIDO* ¡Es como tener un [mc] pelirrojo entre las piernas! *JADEO*"
        "Eso confirma tu teoría de que [eil] está usando tus movimientos. Te sientes orgulloso de la pelirroja."
        call OrgasmXS4 ("c28s001_250") from _call_OrgasmXS4_7
        hide c28s001_975v
        sai "*JADEO* ¡SÍ! *GEMIDO* ¡NO PARES! *JADEO*"
        "Tu preciosa novia morena explota en la boca de tu preciosa novia pelirroja, dejándose ir totalmente, sin avergonzarse de sus caras graciosas."
        "Está entre amigas."
        eil "*Gemido* *Slurp* *Slurp* *Jadeo*"
        "Está entre hermanas."
        "[eil] sigue chupando durante unos segundos más, intentando prolongar el orgasmo de su amiga."
        stop music fadeout (1.5)
        call BlinkXS4 ("c28s001_255") from _call_BlinkXS4_25
        oma "Ha sido precioso verlas así."
        play music ("music/RhythmPlay.ogg")
        mc "[eil] siempre ha sido muy generosa con el sexo. Creo que este era uno de los últimos pasos que le quedaba por dar."
        scene c28s001_255d with fade
        "Demostrando que tienes razón, la pelirroja se ha situado a espaldas de su amiga, como el respaldo de una silla, mientras las últimas oleadas de orgasmos recorren el cuerpo de [sai]."
        eil "Aprendí de ti y contigo. No concibo el sexo si no es así."
        sai "Por lo que a mí respecta, podéis ser los dos todo lo generosos que queráis. Ha sido alucinante."
        mc "*Risa* Lo seremos, no lo dudes. Aprendimos juntos y yo tampoco concibo el sexo sin generosidad."
        call BlinkXS4 ("c28s001_260") from _call_BlinkXS4_26
        oma "Ha sido la primera vez que veo a dos lesbianas en directo teniendo sexo. Si no acabara de follar contigo, estaría cachonda."
        oma "Y eso no quiere decir que quisiera estar ahí. No tengo curiosidad por probarlo. Pero ha sido muy tórrido."
        mc "*Risa* Bueno, al menos una no tiene peligro de convertirse en lesbiana."
        scene c28s001_260d with dissolve
        eil "*Risa* ¡No somos lesbianas!"
        sai "*Risa* Yo diría que ni siquiera bisexuales."
        mc "*Risa* Eso quiere decir que no me vais a sustituir, ¿no?"
        call BlinkXS4 ("c28s001_265") from _call_BlinkXS4_27
        sai "Es difícil de explicar... Lo más tórrido de la situación no es que me estuviera comiendo el coño una chica."
        sai "Es que me lo estaba comiendo [eil]. Mientras mi novio estaba mirando."
        sai "Lo estaba disfrutando porque sabía que el amor de mi vida estaba disfrutando mientras miraba." id c28s001_foursome_ec1f9faa
        call BlinkXS4 ("c28s001_270") from _call_BlinkXS4_28
        sai "Lo siento por la perra pelirroja. *Risa* Nunca me voy a enamorar de ella, con lo que puede estar bien, pero nunca va a estar tan bien como cuando me lo haces tú."
        sai "*Risa* Y no te preocupes. Nunca querré sustituirte."
        mc "Entiendo lo que quieres decir."
        call BlinkXS4 ("c28s001_275") from _call_BlinkXS4_29
        eil "Yo tampoco querré sustituirte. Sé que [sai] quiso que hicierais un trío con otra chica en Portland, con lo que..."
        eil "La relación con [sai] es especial. Y no tiene nada que ver con que la quiera como a una hermana."
        eil "A mi madre también la quiero y nunca me atrevería a hacer algo así con ella. Y eso que, si me gustasen las mujeres, mi madre sería más mi tipo que [sai]."
        mc "*Risa* No te atreverías a decir eso si las piernas de [sai] no fueran de gelatina."
        mc "*Risa* Aprovecha ahora, que no tiene fuerza para sacarte esos preciosos ojos azules."
        call BlinkXS4 ("c28s001_280") from _call_BlinkXS4_30
        oma "Pero, después de esto, creo que [eil] merece un premio. Es la única a la que no te has follado."
        scene c28s001_280d with dissolve
        oma "Y veo que Mjolnir ya se ha recuperado por completo."
        mc "Ver a dos de mis chicas dando y recibiendo placer me pone cachondo. No puedo evitarlo."
    else:
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
        call OrgasmXS4 ("c28s001_205") from _call_OrgasmXS4_8
        mc "¡Mpfft!"
        "Sin poder aguantar más, explotas en el interior de [oma], soltando un gran géiser de semen que la llena por completo."
        oma "*GEMIDO* ¡JODER, SÍ! *JADEO* ¡LLÉNAME! *GEMIDO*"
        "Tu chorro de leche la pilla en medio del punto álgido de uno de sus orgasmos, incrementando aún más su placer."
        eil "*Gemido* Sois alucinantes... *Jadeo*"
        "La voz de [eil], recuperándose de sus orgasmos, suena ronca, cachonda, animal..."
        sai "*Jadeo* A mí aún me queda... *Gemido*"
        "Su voz te indica que le queda menos de lo que dice."
        "Unos segundos después, los gemidos de [sai] demuestran que no te equivocabas."
        call OrgasmXS4 ("c28s001_220") from _call_OrgasmXS4_9
        sai "*GEMIDO* ¡ME CORROOOO! *JADEO* ¡UNA DE LAS MEJORES PAJAS DE MI VIDA! *GEMIDO*"
        "La preciosa India se tensa como hace siempre, poniendo una de sus divertidas caras que las otras chicas no han visto nunca."
        scene c28s001_225An1 with dissolve
        "[eil] baja del sofá y la abraza por detrás de una forma nada sexual. Sabe aceptar los límites que pones."
        eil "Ya está, cariño. Déjate ir."
        "Sabes que, cuando estéis a solas, te dirá lo mucho que le hubiera gustado ayudarla, pero que acepta tu decisión."
        "También sabes que no volverá a preguntártelo con ninguna otra chica."
        scene c28s001_280a with fade
        call BlinkXS4 ("c28s001_280") from _call_BlinkXS4_31
        stop music fadeout (1.5)
        "Descansáis un rato mientras charláis de lo alucinante que está siendo la tarde, hasta que..."
        play music ("music/RhythmPlay.ogg")
        oma "Creo que [eil] merece un premio ahora. Es la única a la que no te has follado."
        scene c28s001_280d with dissolve
        oma "Y veo que Mjolnir ya se ha recuperado por completo."
        mc "Ver a dos de mis chicas abrazadas mientras le toco el culo a la otra me pone cachondo. No puedo evitarlo."
    sai "Yo puedo notar como los pezones de [eil] se están poniendo duros ahora mismo tan solo de pensarlo."
    scene c28s001_280e with dissolve
    sai "Yo me voy a quedar fuera de este asalto. No quiero nada cerca de mi coño en los próximos dos días. Está ardiendo."
    oma "Yo también me voy a quedar fuera. Prefiero mirar en este asalto. ¿Nos sentamos en el sofá?"
    sai "*Risa* Sí, pero lo de no tener nada cerca te incluye a ti."
    eil "¿Voy o vienes?"
    mc "Creo que el edredón es más cómodo que la alfombra."
    scene c28s001_285d with fade
    stop music fadeout (1.5)
    "[eil] se acerca a ti mientras te levantas y se lanza a tus brazos. Quiere su ración de besos."
    play music ("music/Bolero.ogg")
    "Nunca ha sabido tener sexo sin besos antes. En eso sois iguales. El sexo sin besos es para desconocidos."
    "Sus enhiestos pezones se clavan en tu pecho con fuerza, duros como una piedra. Duros como Mjolnir."
    scene c28s001_285e with dissolve
    "Mientras os besáis las otras dos mujeres se han sentado en el sofá y os observan con cariño, agotadas después de sus orgasmos de hace unos momentos."
    sai "Me estoy dando cuenta de que me encanta ver a [mc] con otras mujeres. Antes contigo, ahora con [eil]..."
    if eil._var("bicurious"):
        oma "Veros juntas ha sido tórrido, pero prefiero verlo a él con otra mujer."
    oma "Es que verlo con otra mujer sabiendo que nunca dejará de ser nuestro es totalmente diferente a si tuviéramos miedo de perderlo."
    sai "Creo que tienes razón. Desde que el harén es público la sensación es diferente a como era antes. Creo que odio los secretos."
    call BlinkXS4 ("c28s001_285") from _call_BlinkXS4_32
    if eil._var("bicurious"):
        eil "*Risa* Ahora son ellas las que retransmiten el partido de cricket."
    eil "Dice que no le gustan los secretos la que no quiere contarles a sus padres que está contigo."
    sai "*Grrr*"
    mc "Creo que se refiere a los secretos dentro del harén."
    eil "*Susurrando* Lo sé, pero me encanta picarla."
    call BlinkXS4 ("c28s001_290") from _call_BlinkXS4_33
    eil "¿Te acuerdas del campamento de animadoras? ¿Quieres hacerlo como aquel día en el lago?"
    mc "¿Aún eres tan flexible?"
    eil "*Risa* ¿Me estás llamando vieja? Sólo hay una forma de comprobarlo..."
    if eil._var("bicurious"):
        eil "*Susurrando* Estoy cachondísima después de lo de [sai]. No hace falta que vayas con cuidado."
    else:
        eil "*Susurrando* Llevo un rato cachondísima. No hace falta que vayas con cuidado."
    scene c28s001_295An with dissolve
    "[eil] se pone en la incómoda posición y la penetras en un rápido movimiento facilitado por lo húmedo que está su coño."
    eil "*Gemido* ¡Por el amor de Dios! *Jadeo* Creía que mi turno no iba a llegar... *Gemido*"
    mc "Nunca te dejaría sin tu ración de Mjolnir. ¿Estás cómoda?"
    eil "Tan cómoda como lo estuve hace cuatro años, cuando probamos esta posición por primera vez. Puedes empezar cuando quieras."
    scene c28s001_990pv with dissolve
    show c28s001_990v
    "No dejas que te lo repita dos veces. Sabes que esta posición la agota pese a que a los dos os encanta. Empiezas a bombear con tus caderas."
    eil "*Jadeo* ¡Oh, sí! *Gemido* Tan increíble como siempre... *Jadeo*"
    "Salir con una animadora tiene sus ventajas. La flexibilidad de la muchacha es una de ellas. Ser envidiado por todo el mundo que te despreciaba no era tan importante."
    eil "*Gemido* ¡Amo a Mjolnir! *Jadeo* ¡Y al hombre que hay detrás de él! *Gemido*"
    "No siempre detrás de una gran polla hay un gran hombre. Ella parece pensar que, en este caso, sí que lo hay."
    scene c28s001_295d with dissolve
    sai "Nos está vacilando, ¿verdad? Si yo hago eso me acabaría rompiendo."
    oma "*Risa* Sí, definitivamente nos está vacilando. Eso no puede ser cómodo."
    mc "*Risa* ¿Cómo va el partido de cricket?"
    sai "*Risa* ¿No puedes concentrarte si hablamos?" (multiple=2)
    oma "*Risa* ¡Calla y folla!" (multiple=2)
    scene c28s001_995pv with dissolve
    show c28s001_995v
    hide c28s001_990v
    "Decides ignorar a las comentaristas y centrarte en la animadora. Ahora mismo, [eil] lo significa todo. Sigues escuchando como hablan en susurros."
    eil "*Gemido risueño* Olvídalas y deja que babeen. *Jadeo* Son unas perras envidiosas. *Gemido*"
    "Casi cualquier mujer envidiaría la flexibilidad de [eil]. Tú prefieres disfrutarla."
    eil "*Jadeo* Ya estoy a punto... *Gemido* No voy a aguantar nada... *Jadeo*"
    "Después de todo lo que ha pasado durante la tarde, no te sorprende. Lo que te sorprende es que todavía tengáis energía para seguir."
    call OrgasmXS4 ("c28s001_300") from _call_OrgasmXS4_10
    eil "*GEMIDO* ¡POR EL AMOR DE DIOS! *JADEO* ¡ES UN ORGASMO ENORME! *GEMIDO*"
    "El coño de la pelirroja empieza a estrujar con fuerza a Mjolnir, pidiéndole una descarga de tu semilla en su interior."
    "La fuerza que ejerce, y lo rápido que ha llegado su orgasmo, es una clara muestra de lo cachonda que estaba antes de empezar."
    if eil._var("bicurious"):
        "Comerle el coño a una mujer por primera vez ha tenido que ser una experiencia alucinante para ella."
    eil "*JADEO* ¡NO PARES! *GEMIDO* ¡SIGUEN LLEGANDO! *JADEO*"
    scene c28s001_985pv with dissolve
    show c28s001_985v
    hide c28s001_995v
    "Continúas bombeando con tus caderas, cada vez más cerca de tu propio orgasmo. El abrazo de sus paredes vaginales te está llevando muy rápido a la meta."
    eil "*GEMIDO* ¡ERES INCREÍBLE! *JADEO* ¡QUÉ AGUANTE TIENES! *GEMIDO*"
    "Tu aguante está llegando a su fin debido a las rápidas embestidas que cada vez encuentran una mayor resistencia."
    eil "*JADEO* ¡CAMBIA DE AGUJERO! *GEMIDO* ¡MI COÑO NO PUEDE MÁS! *JADEO*"
    "[eil] perdió la virginidad por la puerta de atrás contigo hace años, pero no por ello te sorprende menos su petición."
    if persistent.walkthrough:
        $ wt1 = _("Sólo permitirá corrida en el culo o corrida en la cara de las tres chicas.\n Habilita Anal para [eil].")
        $ wt2 = _("Sólo permitirá corrida vaginal o corrida en la cara de las tres chicas.\n Deshabilita Anal para [eil].")
    else:
        $ wt1 = ""
        $ wt2 = ""
    menu:
        "Cambiar a anal." (wt = wt1):
            $ eil._var("anal", True)
        "Seguir con sexo vaginal." (wt = wt2):
            $ eil._var("anal", False)
    $ resetWalkthrough ()
    if not eil._var("anal"):
        "Estás a punto de llegar a tu orgasmo y no vale la pena cambiar ahora. Sabes que te correrías nada más entrar en su culo."
        if persistent.walkthrough:
            $ wt1 = _("[eil] embarazada.")
            $ wt2 = _("Sin consecuencias.")
        else:
            $ wt1 = ""
            $ wt2 = ""
        menu:
            "Correrte dentro. Ir a por el bebé." (wt = wt1) if persistent.pregnancy and not eil._var("pregnant"):
                $ eil._var("pregnant", True)
                $ eil._var("undiscoveredPregnancy", True)
                call c28s001_vaginalEil from _call_c28s001_vaginalEil
                play sound ("music/OldMusicBox5.ogg")
            "Correrte dentro." (wt = wt2):
                call c28s001_vaginalEil from _call_c28s001_vaginalEil_1
            "Correrte en la cara de las chicas." (wt = wt2):
                call c28s001_tripleHeadshot from _call_c28s001_tripleHeadshot
        $ resetWalkthrough ()
        hide c28s001_985v
    else:
        scene c28s001_305An with dissolve
        "Cambias rápidamente a su estrecho agujero mientras cambiáis de posición a una en la que [eil] está más cómoda."
        eil "*GEMIDO* ¡OOOFFF! *JADEO*"
        "Su paja anterior ha dilatado su agujero trasero lo suficiente como para que entres sin hacerle daño."
        eil "*JADEO* ¡EMPIEZA A MOVERTE! *GEMIDO* ¡NO LO PIERDAS! *JADEO*"
        "La pausa momentánea ha retrasado tu orgasmo un poco, pero no por ello la pelirroja deja de pensar en ti."
        scene c28s001_885pv with dissolve
        show c28s001_885v
        hide c28s001_985v
        "Tus caderas empiezan a moverse a un ritmo pausado que sabes que es confortable para la ex animadora."
        eil "*GEMIDO* ¡JUSTO ASÍ! *JADEO* ¡SABES CÓMO ME GUSTA! *GEMIDO*"
        "Ciertamente lo sabes y siempre te ha sorprendido la facilidad de la camarera para llegar al orgasmo durante el sexo anal."
        "En este caso no tiene que llegar, sino que la cascada de orgasmos producidos hace un momento continúan uno tras otro."
        eil "*JADEO* Tías... *GEMIDO* No sabéis lo que os perdéis... *JADEO*"
        scene c28s001_310a with dissolve
        "Las otras dos mujeres os miran boquiabiertas, con un poco de envidia en sus caras por el conocimiento que tenéis del cuerpo del otro."
        "Ni siquiera con [sai] llegaste al nivel de compenetración que tienes con [eil], ya que estuviste con ella menos tiempo que con la pelirroja."
        oma "¿Ves? Eso no descarto probarlo algún día..."
        sai "Pese a lo grande que es Mi Pequeñín, duele menos de lo que parece que debería..."
        "Continúa la retransmisión del partido de cricket. Nunca te ha interesado el cricket."
        scene c28s001_895pv with dissolve
        show c28s001_895v
        hide c28s001_885v
        "Continúas con tus suaves embestidas mientras los continuos orgasmos siguen recorriendo el cuerpo de [eil]."
        eil "*GEMIDO* ¡NO PUEDO PARAR DE CORRERME! *JADEO* ¡ES MARAVILLOSO! *GEMIDO*"
        "Ella también ignora la retransmisión del partido después de haberlas querido incluir en su momento de placer."
        "Su cuerpo vibra y se retuerce bajo el tuyo, en una reverberación de cada uno de los golpes de tus caderas sobre su culo."
        eil "*JADEO* ¿CUANTO TE QUEDA PARA CORRERTE? *GEMIDO* CREO QUE ESTÁS LLEGANDO... *JADEO*"
        scene c28s001_890pv with dissolve
        show c28s001_890v
        hide c28s001_895v
        mc "Estoy casi a punto, cielo..."
        "La compenetración va en los dos sentidos y ella también sabe cómo tu cuerpo cambia sutilmente sus embestidas cuando estás a punto de correrte."
        eil "*GEMIDO* HAZLO DONDE QUIERAS... *JADEO*"
        eil "*JADEO* PERO NO VUELVAS A MI COÑO PARA CORRERTE... *GEMIDO*"
        "No pensabas hacerlo después de descubrir los problemas de infecciones que eso podría provocar."
        if eil._var("pregnant"):
            "Tu bebé está ahí dentro y tienes que cuidarlo incluso antes de que nazca."
        if persistent.walkthrough:
            $ wt2 = _("Sin consecuencias.")
        else:
            $ wt2 = ""
        menu:
            "Correrte dentro." (wt = wt2):
                call c28s001_analEil from _call_c28s001_analEil
            "Correrte en la cara de las chicas." (wt = wt2):
                call c28s001_tripleHeadshot from _call_c28s001_tripleHeadshot_1
        $ resetWalkthrough ()
        hide c28s001_890v
    scene c28s001_310b with fade
    stop music fadeout (1.5)
    "Después de limpiaros un poco..."
    play music ("music/RhythmPlay.ogg")
    oma "Hay que repetir esto. Me ha encantado."
    mc "¿Ya ha acabado? ¿Ya estáis sin energía?"
    sai "*Risa* No me digas que aún puedes aguantar unos cuantos asaltos más. Creía que [oma] te había cansado antes de que llegáramos."
    mc "Creo que aún tengo gasolina para un par de asaltos más."
    eil "Estoy segura de que la tendrías, pero tenemos que volver a casa."
    call BlinkXS4 ("c28s001_315") from _call_BlinkXS4_34
    oma "Lo de llamar a [nor] y decirle que no iremos a cenar porque vamos a exprimirte aún más no es una opción."
    mc "Lo tendremos que dejar para la próxima ocasión, entonces."
    call BlinkXS4 ("c28s001_320") from _call_BlinkXS4_35
    sai "Para la próxima podríamos incluir a más chicas."
    if kia._var("route"):
        sai "Me encantaría que [kia] se uniera a nosotras... Otras chicas han elegido a [mar] o [nor] como segundas madres. A mí me gusta [kia]." id c28s001_foursome_ce985d63
        mc "No sé qué opinaría [eil] sobre eso..."
        call BlinkXS4 ("c28s001_325") from _call_BlinkXS4_36
        eil "¿Mi madre? ¡Ni en broma! Ella no estaría cómoda en algo así, y menos aún si estoy yo. A mí no me importaría."
        if eil._var("bicurious"):
            eil "Incluso le podría dar el mismo tratamiento que a [sai]... Sería una forma de estrechar lazos... Pero no me atrevería porque ella no lo aceptaría."
    if mc._var("relationships")==3:
        mc "No hay más chicas..."
    else:
        mc "No sé qué chicas del harén querrían unirse..."
    call BlinkXS4 ("c28s001_330") from _call_BlinkXS4_37
    oma "No estoy segura de si has cerrado el harén. Aún tienen que llegar las chicas nuevas y..."
    mc "¿Y...?"
    call BlinkXS4 ("c28s001_335") from _call_BlinkXS4_38
    oma "No, nada..."
    mc "¿Qué me estoy perdiendo?"
    call BlinkXS4 ("c28s001_340") from _call_BlinkXS4_39
    eil "Creo que no somos nosotras las que tenemos que hablar de eso. Es tu decisión y todas la aceptaremos."
    mc "¿Pero de quién estáis hablando? No entiendo nada..."
    call BlinkXS4 ("c28s001_345") from _call_BlinkXS4_40
    sai "Me encanta que sigas siendo inocente a veces y no pilles algunas situaciones, aunque cada vez sean menos."
    sai "Ya lo descubrirás el día que decidas quitarle el 'no' a 'no-cita'. Si es que decides quitárselo, claro."
    mc "¿Que? ¿[kat]? ¿Estáis locas? ¡Es lesbiana! ¡No tiene ningún interés en mí!"
    scene c28s001_350a with dissolve
    oma "Pobrecillo..."
    eil "Con tantas novias y todavía no sabe nada sobre las mujeres..."
    sai "Piensa un poco mientras nos duchamos, [mc]."
    mc "Supongo que no estoy invitado a esa ducha..."
    scene c28s001_350b with dissolve
    oma "La ducha es pequeña. No todos vivimos en mansiones con baños enormes."
    eil "*Risa* Y los melones de [sai] ocupan mucho espacio."
    if sai._var("pregnant"):
        eil "*Risa* Cuando le empiecen a crecer, va a usar la piscina como bañera."
    sai "*Risa* Bueno, eso compensa que tú tienes las tetas pequeñas."
    if eil._var("pregnant"):
        sai "*Risa* Cuando te empiecen a crecer por el embarazo, a lo mejor llegan a una medida normal."
    oma "Pero puedes mirar desde el pasillo mientras esperas a que acabemos."
    mc "No voy a decir que no a eso. Mis ojos nunca se cansan de miraros."
    scene c28s001_350c with fade
    "Las chicas se duchan bajo tu atenta mirada en una ducha que es ciertamente pequeña para las tres."
    "Hay muchas risas durante esa ducha, en la que rememoran todo lo que ha pasado durante la tarde."
    scene c28s001_350d with fade
    "Después son ellas las que te observan a ti mientras te duchas."
    "Aunque sus miradas se dirigen más a Mjolnir que a tus ojos. Ellas tampoco se cansan de mirarte."
    "Estás tentado de decirles dónde están tus ojos, pero sabes que no va a servir de nada."
    scene black with fade
    "Volvéis a casa con los dos coches. [eil] en el de [oma] y [sai] en tu camioneta."
    "Intentas que te explique a qué se refería con su comentario sobre [kat]. Sin éxito."
    stop music fadeout (1.5)
    "Cada vez estás más convencido de que tienes que hablar con [nor] o [kim] sobre ella."
    return
label c28s001_tripleHeadshot:
    scene c28s001_355a with dissolve
    "Sales de dentro de [eil] cuando estás a punto de correrte."
    mc "Chicas, venid. Quiero pintaros la cara a las tres."
    oma "*Risa* ¡Voy!"
    sai "*Risa* ¡Travieso!"
    scene c28s001_355An with fade
    mc "¡Mpfft!"
    "Con las tres arrodilladas delante tuyo, tu abundante orgasmo llega enseguida."
    "Hay suficiente leche como para cubrir las tres preciosas caras que te miran con miradas traviesas."
    eil "*Gemido* ¡Qué gran final!"
    oma "¡Para la primera vez de muchas!"
    sai "¡Es sorprendente que aún te quede tanta leche!"
    scene c28s001_355f with dissolve
    "[eil] se mete la punta de Mjolnir en la boca para engullir los últimos restos de tu semen."
    oma "Cuando [eil] suelte tu polla, ¿puedes traernos algo para limpiarnos? Hay servilletas de papel en la cocina."
    eil "*Slurp*"
    sai "*Risa* Creo que eso significa que la va a tener en la boca un rato."
    sai "Ya voy yo a por las servilletas."
    return
label c28s001_analEil:
    call OrgasmXS4 ("c28s001_360") from _call_OrgasmXS4_11
    mc "¡Mpfft!"
    "Explotas dentro del culo de [eil], llenándole el estrecho agujero con tu leche. Sorprendido de la cantidad que aún eres capaz de eyacular."
    eil "*GEMIDO* ¡SÍ! *JADEO* ¡DÁMELA TODA! *GEMIDO* ¡LLÉNAME! *JADEO*"
    "Y la llenas. Hasta que algo se escapa incluso a través de su apretado esfínter."
    scene c28s001_890pv with fade
    eil "*Gemido* Ha sido increíble... *Jadeo* Siempre es increíble contigo..."
    eil "*Jadeo* Voy a necesitar algo con lo que limpiarme o se va a salir todo cuando me levante... Y voy a inundar el edredón."
    scene c28s001_355a with dissolve
    mc "Chicas, ¿podéis traer algo para limpiarnos, por favor?"
    sai "¡Voy!"
    oma "Hay servilletas de papel en la cocina."
    return
label c28s001_vaginalEil:
    call OrgasmXS4 ("c28s001_365") from _call_OrgasmXS4_12
    mc "¡Mpfft!"
    "Explotas dentro del coño de [eil], llenándole el estrecho agujero con tu leche. Sorprendido de la cantidad que aún eres capaz de eyacular." id c28s001_vaginalEil_4477732b
    eil "*GEMIDO* ¡SÍ! *JADEO* ¡DÁMELA TODA! *GEMIDO* ¡LLÉNAME! *JADEO*"
    "Y la llenas. Hasta que algo se escapa a través de su estrecho coño y de Mjolnir actuando como tapón." id c28s001_vaginalEil_e2f8a4a8
    scene c28s001_990pv with fade
    eil "*Gemido* Ha sido increíble... *Jadeo* Siempre es increíble contigo..."
    eil "*Jadeo* Voy a necesitar algo con lo que limpiarme o se va a salir todo cuando me levante... Y voy a inundar el edredón."
    scene c28s001_355a with dissolve
    mc "Chicas, ¿podéis traer algo para limpiarnos, por favor?"
    sai "¡Voy!"
    oma "Hay servilletas de papel en la cocina."
    return
label c28s001_noFoursome:
    scene black with dissolve
    "Al volver a casa, [eil] te dice que la entrevista de [sca] ha ido bien. Mañana le dirán algo sobre el trabajo."
    scene c28s001_1000 with fade
    "Subes a tu habitación y juegas un rato a My Residence antes de cenar."
    "Tienes una tórrida escena de sexo en grupo con Aishwarya, Alejandra, y Laoise."
    "Aishwarya y Laoise no intentan sacarse los ojos la una a la otra."
    "Laoise incluso acaba descubriendo que tiene cierta curiosidad por cómo sabe el coño de su amiga."
    return
label c28s002_Kim:
    if _in_replay:
        call mrS3_kat_slim from _call_mrS3_kat_slim_2
        call mrS3_kim_route from _call_mrS3_kim_route_5
    scene c28s002_005a with fade
    call BlinkXS4 ("c28s002_005") from _call_BlinkXS4_41
    play music ("music/romantic-day.ogg")
    "Después de cenar, tras ayudar a [nor] a recoger la cocina, mientras vuelves hacia tu habitación..."
    mc "Hey, [kim]. ¿Qué haces aquí?"
    kim "Estoy esperando a las chicas. Vamos a dar un paseo por la carretera para bajar la cena."
    kim "Han ido a ponerse calzado cómodo."
    mc "¿Una nueva costumbre?"
    call BlinkXS4 ("c28s002_010") from _call_BlinkXS4_42
    kim "*Risa* Todas nos hemos engordado un par de libras como mínimo desde que llegamos."
    if kat._var("slim"):
        kim "Todas menos [kat], claro."
    kim "Hoy hemos decidido que daremos un paseo cada noche. [kat] es la única que ha decidido no apuntarse."
    mc "*Risa* Comer todos los días la comida de [mar] y [nor] tiene efectos secundarios."
    mc "Hablando de [kat], ¿sabes si está enfadada conmigo? Lleva evitándome desde la no-cita."
    call BlinkXS4 ("c28s002_015") from _call_BlinkXS4_43
    kim "*Susurrando* Ahora no es un buen momento para hablar de eso, [mc]. Podría estar detrás de la puerta esperando al resto de las chicas."
    mc "Eso que estás diciendo significa que algo pasa, ¿no?"
    kim "*Susurrando* Sí, pero será mejor que lo hablemos mañana."
    mc "Me parece una buena idea."
    call version28 from _call_version28_3
    if kim._var("route"):
        call BlinkXS4 ("c28s002_020") from _call_BlinkXS4_44
        kim "Cambiando de tema, te invito a comer el viernes. Acabo las clases a mediodía y podríamos hacer algo."
        mc "¿Algo en plan cita?"
        call BlinkXS4 ("c28s002_025") from _call_BlinkXS4_45
        kim "Yo había pensado en algo más informal que una cita."
        kim "Después de lo que pasó en el barco de Iron Fist, creo que invertir parte de mi sueldo de esa noche en invitarte a comer estaría bien."
        mc "Sabes que no hace falta, ¿verdad?"
        call BlinkXS4 ("c28s002_030") from _call_BlinkXS4_46
        kim "Lo sé, pero quiero hacerlo. Cuesta tanto tener tiempo a solas contigo..."
        mc "Lo siento, [kim]. Últimamente he estado muy ocupado preparando el viaje a Aruba."
        mc "Me da la impresión de que me paso el día leyendo informes."
        call BlinkXS4 ("c28s002_035") from _call_BlinkXS4_47
        kim "Entonces, ¿eso es un sí?"
        mc "Sí, claro que es un sí. ¿Quieres que busque algún sitio para ir a comer?"
        scene c28s002_035d with hpunch
        "La preciosa modelo te besa con alegría. Aquella noche en el barco de Iron Fist cambió muchas cosas en ella."
        "Le dio una seguridad en sí misma que no tenía anteriormente. La [kim] de antes no hubiera tomado la iniciativa para invitarte a comer."
        "Si no odiaras tanto a Ichigo, casi le tendrías que estar agradecido."
        call BlinkXS4 ("c28s002_040") from _call_BlinkXS4_48
        kim "Invito yo, con lo que buscaré algún sitio. No es una cita, no va a ser ningún sitio romántico ni nada por el estilo."
        kim "Sólo quiero pasar un rato a solas con mi novio."
        mc "Me parece una idea estupenda."
        call BlinkXS4 ("c28s002_045") from _call_BlinkXS4_49
        kim "Cuando lo tenga decidido te aviso, no sea que no te guste el sitio..."
        mc "No te preocupes, mientras tengan un plato sin brócoli no va a haber ningún problema."
        call BlinkXS4 ("c28s002_050") from _call_BlinkXS4_50
        kim "*Risa* ¿Incluso si el único plato sin brócoli es una pizza con piña?"
        mc "No voy a responder a esa pregunta. *Risa* Ese tema podría ser motivo de ruptura para algunas parejas."
        call BlinkXS4 ("c28s002_055") from _call_BlinkXS4_51
        kim "Si sirve de algo, nunca la pediría, pero no tengo ningún problema en comerla si es una pizza para compartir."
        kim "No es mi favorita ni mucho menos, pero no me resulta desagradable."
        kim "La que no soporto es la pizza con kiwi."
        mc "*Risa* Creo que el tipo que inventó la pizza con kiwi quería convertirse en el más odiado de la humanidad. Por suerte, no se ha hecho popular."
    call BlinkXS4 ("c28s002_060") from _call_BlinkXS4_52
    kim "¿Cuánto se puede tardar en cambiarse de zapatos?"
    if kim._var("route"):
        mc "*Risa* Para querer pasar tiempo a solas conmigo, tienes muchas ganas de irte con las chicas ahora que estamos a solas..."
    else:
        mc "*Risa* Pareces un chico esperando a su cita."
    call BlinkXS4 ("c28s002_065") from _call_BlinkXS4_53
    kim "¡Oh! *Risa* ¡No lo decía por eso! Es que a veces entiendo cuando los chicos os quejáis de lo que tardamos las mujeres en estar listas."
    kim "¡Es sólo cambiarse unos zapatos! ¡No tienen que maquillarse ni probarse ropa nueva!"
    mc "*Risa* Bienvenida al mundo de los hombres."
    scene c28s002_070a with dissolve
    stop music fadeout (1.5)
    "En ese momento se abre la puerta."
    play music ("music/LifeOfAWanderingWizard.ogg")
    deb "¿De qué os estáis riendo?"
    mc "Mejor no lo quieras saber. *Risa*"
    lis "No hemos tardado mucho, ¿verdad?"
    kim "Precisamente de eso nos estábamos riendo."
    sai "[lis] ha tenido que ir al lavabo."
    scene c28s002_070b with dissolve
    lis "¡[sai]!"
    sai "¿Qué? Podías haber ido a lavarte los dientes. Yo lo he hecho mientras te esperábamos."
    sai "*Risa* Ahora todo el mundo sabe a lo que has ido."
    deb "[lis] cree que el resto de los mortales pensamos que las princesas no cagan. *Risa*"
    lis "¡[deb.nick]!"
    kim "Chicas, vámonos antes de que acabemos de hacer la digestión... *Risa* Aunque [lis] parece que ya la ha hecho."
    scene c28s002_070c with dissolve
    lis "*Risa* ¡Os odio!"
    todas "*Risa*"
    mc "Que vaya bien el paseo, chicas."
    scene c28s002_070d with dissolve
    todas "Hasta mañana, [mc]."
    scene c28s002_070e with dissolve
    "Te sientes tentado de llamar a la puerta de la habitación que [kim] y [kat] comparten aprovechando que estará sola."
    stop music fadeout (1.5)
    "Lo piensas mejor y decides esperar a tener toda la información después de hablar con [kim] mañana."
    return
label c28s002_SimGrateful:
    if _in_replay:
        call mrS3_sim_route from _call_mrS3_sim_route_6
    scene c28s002_100a with fade
    call BlinkXS4 ("c28s002_100") from _call_BlinkXS4_54
    "Al llegar a tu habitación..."
    play music ("music/LostVoices.ogg")
    mc "Hola, [sim]. ¿Puedo ayudarte en algo?"
    sim "Venía tan solo a darte las gracias por lo que hicisteis [ama] y tú."
    mc "Yo no tuve nada que ver, [sim]. Fue idea de [ama]. Yo solo firmé el papeleo."
    call BlinkXS4 ("c28s002_105") from _call_BlinkXS4_55
    sim "Bueno, si no lo hubieras firmado, [ama] no podría haberlo hecho."
    mc "Estoy seguro de que hubiera encontrado la manera de hacerlo. Se preocupa mucho por todas vosotras."
    call BlinkXS4 ("c28s002_110") from _call_BlinkXS4_56
    sim "¿Puedo decirte una cosa? Llevo desde el cumpleaños de las chicas queriéndome quitar el peso de encima..."
    mc "Lo que quieras. ¿Es tan grave?"
    call BlinkXS4 ("c28s002_115") from _call_BlinkXS4_57
    sim "No sé si es grave. Y decírtelo ahora puede parecer que es por las razones equivocadas, pero me siento súper culpable..."
    mc "¿Qué has hecho para sentirte culpable, [sim]?"
    mc "¿Tiene algo que ver con la beca?"
    call BlinkXS4 ("c28s002_120") from _call_BlinkXS4_58
    sim "No, no. No tiene nada que ver con la beca... Tiene que ver con [ama] y [eva]..."
    mc "¿Qué pasa con ellas? ¿Han hecho algo? Me estás empezando a preocupar."
    call BlinkXS4 ("c28s002_125") from _call_BlinkXS4_59
    sim "No han sido ellas. Fui yo..."
    mc "¿Qué hiciste?"
    sim "Las prejuzgue. Cuando mi madre me habló de ellas por primera vez... No me parecía normal. Ni siquiera bien."
    if persistent.family:
        sim "Clones de mis amigas, unas asesinas, se iban a unir a la familia..."
    else:
        sim "Mis amigas eran clones y ahora las chicas de las que eran clones, unas asesinas, se iban a unir a la familia..."
    sim "No era natural... No quería ni tan solo conocerlas..."
    mc "Hasta que las conociste."
    call BlinkXS4 ("c28s002_130") from _call_BlinkXS4_60
    sim "Hasta que [emm] estuvo hablando de ellas sin parar en la fiesta de cumpleaños, antes de que llegaran."
    sim "Si [emm] las podía aceptar y sentirse ilusionada con ellas, teniendo en cuenta que a ella le afectaba más que a mí, ¿quién era yo para no hacerlo?"
    sim "Y después las conocí y todas las barreras mentales que tenía desaparecieron."
    mc "A todos nos costó un poco aceptar su existencia. No es algo que pase normalmente."
    call BlinkXS4 ("c28s002_135") from _call_BlinkXS4_61
    sim "Pero parece ser que yo fui la única que las prejuzgué. El resto las aceptasteis enseguida. Yo tuve que esperar a conocerlas."
    sim "Y desde entonces me siento culpable por haber reaccionado así."
    mc "No tienes por qué hacerlo. Lo que es extraño es que todo el mundo las aceptase tan rápido."
    mc "La mayoría de las chicas tuvo un baño de realidad inmediato. Se enteraron de su existencia el mismo día que las conocieron."
    mc "En tu caso..."
    call BlinkXS4 ("c28s002_140") from _call_BlinkXS4_62
    sim "En mi caso tuve tiempo de darle vueltas a la cabeza. Pero se las di en el sentido equivocado. No quería que unas asesinas formaran parte de la familia..."
    sim "Sé que no tengo derecho a decidir quién forma parte de la familia, pero es como me sentía. Y me siento culpable por haberme sentido así."
    mc "No le des más vueltas. Supongo que, en el momento en que las conociste, esos prejuicios desaparecieron."
    call BlinkXS4 ("c28s002_145") from _call_BlinkXS4_63
    call version28 from _call_version28_4
    sim "¡Claro! Pasaron a ser dos personas en vez de dos conceptos. Verlas con la mirada ilusionada por formar parte de algo como esta familia..."
    sim "Las tenías que haber visto en el jacuzzi... Eran como dos niñas pequeñas... Como si también fuera su cumpleaños y esta familia fuera su regalo..."
    mc "No te equivocas demasiado. Lo han pasado mal y aquel día fue importante para ellas."
    mc "Creo que tenían un poco de miedo a cómo las recibiríais las que aún no las conocíais."
    call BlinkXS4 ("c28s002_150") from _call_BlinkXS4_64
    sim "Por eso necesitaba contárselo a alguien. Me comporté mal con ellas antes de conocerlas..."
    mc "A mí no me parece algo de lo que te debas preocupar pero, si te vas a quedar más tranquila, creo que deberías hablar con ellas."
    mc "Creo que incluso les podría gustar tener esa conversación contigo."
    call BlinkXS4 ("c28s002_155") from _call_BlinkXS4_65
    sim "¿Qué? ¿Confesarles que las prejuzgué? ¡Pensarán que soy idiota!"
    mc "Es posible, pero también se darán cuenta de que dejaste de hacerlo en el momento en que les pusiste cara... aunque ya sabías qué cara tendrían..."
    mc "Digamos que en el momento en que las individualizaste. Como has dicho, cuando se convirtieron en personas en vez de conceptos."
    mc "Eso les va a gustar. Sabes que siempre buscan individualizarse, sobre todo [eva], y que les expliques lo que me has explicado a mí..." id c28s002_SimGrateful_06b5d016
    call BlinkXS4 ("c28s002_160") from _call_BlinkXS4_66
    if sim._var("route"):
        sim "¡Tienes razón! ¡Hablaré mañana con ellas en el desayuno!"
    else:
        sim "¡Tienes razón! ¡Voy a hablar con ellas antes de que se acuesten!"
    mc "¿Dónde dormían hoy? Al final no me he enterado porque he empezado a recoger los platos."
    sim "[ama] con [emm] y [eva] con [nor]."
    if not sim._var("route"):
        sim "Yo duermo en la habitación de [eri] hoy, con lo que empezaré con [ama]."
    scene c28s002_160d with dissolve
    sim "Gracias por la conversación. Me he quitado un peso de encima."
    mc "Estoy para ti cuando lo necesites."
    stop music fadeout (1.5)
    return
label c28s003_noSimLewd:
    scene c28s003_1000 with fade
    "Cuando [sim] se va, juegas un rato a My Residence, donde tienes una tórrida escena con Nina."
    "La hija de Sabrina se queda a dormir en la habitación de tu personaje por primera vez, teniendo una larga escena de sexo."
    return
label c28s003_SimLewd:
    if _in_replay:
        $ mc._var("relationships", 1, "set")
        call mrS3_sim_pregnant from _call_mrS3_sim_pregnant_1
        call mrS3_kia_route from _call_mrS3_kia_route_12
        call mrS3_mad_route from _call_mrS3_mad_route_9
        call mrS3_eil_route from _call_mrS3_eil_route_8
        call mrS3_sai_route from _call_mrS3_sai_route_9
        call mrS3_oma_route from _call_mrS3_oma_route_7
        call mrS3_mar_route from _call_mrS3_mar_route_16
        if mc._var("relationships")<2:
            call mrS3_rels from _call_mrS3_rels_20
    call BlinkXS4 ("c28s003_005") from _call_BlinkXS4_67
    play music ("music/Majestica.ogg")
    mc "¿Y tú? ¿Dónde vas a dormir? ¿Te quedas con alguna de las chicas?"
    sim "Pensaba quedarme aquí. He oído que esa cama es muy cómoda."
    mc "¿Sólo dormir?"
    scene c28s003_975pv with dissolve
    show c28s003_975v
    "La chica no contesta. Al menos no con palabras, aunque sus labios no se mantienen cerrados durante mucho tiempo."
    "Es un beso suave a la vez que apasionado. Un beso que marca el reencuentro de vuestras bocas tras varios días sin tiempo de calidad a solas."
    "Los voluptuosos labios de [sim] son tan suaves que nunca te podrías cansar de ellos."
    "Esperas que ella nunca se canse de los tuyos."
    call BlinkXS4 ("c28s003_010") from _call_BlinkXS4_68
    hide c28s003_975v
    sim "¿Te sirve eso como respuesta?"
    mc "Hasta cierto punto... *Risa* ¿Es un beso de buenas noches?"
    call BlinkXS4 ("c28s003_015") from _call_BlinkXS4_69
    sim "*Risa* ¡Me voy a casar con un tonto!"
    mc "No debe ser demasiado tonto si se va a casar contigo, ¿no?"
    call BlinkXS4 ("c28s003_020") from _call_BlinkXS4_70
    sim "Creo que me he adelantado y no te he dejado pedírmelo."
    sim "Yo no necesito un anillo para sentir que soy tu prometida."
    if mad._var("route"):
        sim "Ni un post-it."
    mc "*Risa* No sé a lo que te refieres, pero..."
    call BlinkXS4 ("c28s003_025") from _call_BlinkXS4_71
    sim "[mc] Marks. ¿Quieres casarte conmigo? No tengo un anillo que darte ahora mismo, pero quería hacerlo."
    mc "¿Qué? ¿De verdad? ¿No debería hacer eso yo?"
    call BlinkXS4 ("c28s003_030") from _call_BlinkXS4_72
    if mc._var("relationships")>1:
        if mad._var("route") or kia._var("route"):
            sim "No es necesario, no tienes que pedírnoslo tú a todas."
            if kia._var("route") and mad._var("route"):
                sim "Llevas dos, y dicen que el tres es un número muy importante, ¿no?"
            elif kia._var("route"):
                if mc._var("relationships")==2:
                    sim "Después de lo de [kia], esperaba que me lo pidieras tarde o temprano. Prefiero no esperar."
                else:
                    sim "Después de lo de [kia], esperaba ser la siguiente. Prefiero no esperar."
            else:
                if mc._var("relationships")==2:
                    sim "Después de lo de [mad.nick], esperaba que me lo pidieras tarde o temprano. Prefiero no esperar." id c28s003_SimLewd_2f75c9e8
                else:
                    sim "Después de lo de [mad.nick], esperaba ser la siguiente. Prefiero no esperar." id c28s003_SimLewd_82d35bc7
        else:
            sim "No es necesario, quiero ser tu primera prometida, aunque no nos podamos casar nunca."
            sim "No voy a esperar que se lo pidas antes a otra."
    else:
        sim "Creo que es el próximo paso, ¿no?"
        sim "Con lo que te costó empezar a salir conmigo, no quiero que pasen años antes de que me pidas que nos casemos."
    scene c28s003_030d with hpunch
    mc "¡Sí! ¡Sí quiero!"
    sim "*Risa* Acabas de parecer una de esas chicas de los videos de TicTac."
    sim "Lo has hecho a propósito, ¿verdad?"
    scene c28s003_030e with dissolve
    mc "*Risa* Por supuesto. ¿Puedo besar a mi prometida?"
    sim "Creía que no me lo ibas a pedir nunca..."
    scene c28s003_030f with dissolve
    "El beso de antes era apasionado. Este lo es aún más. Vuestro primer beso una vez prometidos. No será el último."
    "Afortunadamente, el beso no sabe diferente. Los besos de [sim] siempre han sido perfectos, insuperables."
    "Cualquier cambio sólo hubiera podido empeorarlos."
    call BlinkXS4 ("c28s003_035") from _call_BlinkXS4_73
    sim "*Jadeo* Mi primer beso como prometida. Sigue siendo tan bueno como siempre."
    mc "*Risa* Que me hayas pedido matrimonio, aunque sea sin anillo, no va a cambiar nuestros besos."
    call BlinkXS4 ("c28s003_040") from _call_BlinkXS4_74
    sim "Bueno, creo que lo del anillo tradicional no va conmigo..."
    mc "¿No quieres un anillo?"
    sim "Seguro que lo acabaría perdiendo. Soy un desastre con la joyería."
    mc "*Risa* Siempre te lo puedes tatuar en el dedo."
    call BlinkXS4 ("c28s003_045") from _call_BlinkXS4_75
    sim "*Risita* Sería una forma de no perderlo."
    mc "Y tendríamos otra tatuada en la familia aparte de [eri]."
    call BlinkXS4 ("c28s003_050") from _call_BlinkXS4_76
    sim "Cambiando de tema... ¿Tienes algún pijama para prestarme?"
    mc "Creo que sólo tengo un pijama, pero ¿para qué necesitas un pijama? En esta habitación suele hacer calor."
    call BlinkXS4 ("c28s003_055") from _call_BlinkXS4_77
    sim "Nunca duermo desnuda, pero..."
    mc "Pero tampoco duermes nunca con tu prometido. Siempre hay una primera vez para todo."
    call BlinkXS4 ("c28s003_060") from _call_BlinkXS4_78
    sim "Si llego a saber que esta noche tu habitación estaba libre, hubiera traído la lencería que me regaló [emm]."
    sim "Es muy bonita. Me saqué una foto para mandártela, pero al final pensé que sería mejor que la vieras en persona."
    mc "Y sabiendo que existe esa foto, ¿crees que no te voy a pedir que me la enseñes?"
    call BlinkXS4 ("c28s003_065") from _call_BlinkXS4_79
    sim "*Risa* La iluminación es horrible y te acabo de decir que es mejor que la veas en persona."
    mc "*Risa* Porfa, porfa, porfa..."
    sim "*Risa* No vas a parar hasta que te la enseñe, ¿verdad?"
    mc "*Risa* Porfa, porfa, porfa..."
    scene c28s003_065d with fade
    call addProfileImageS3 (7, "sim_7", sim, _(": 15 - Especial"), "") from _call_addProfileImageS3_21
    sim "No juzgues demasiado. Ya te he dicho que la luz era horrible."
    mc "¡Aparta ese móvil de mí antes de que te lo averíe con las babas! ¡Estás espectacular!"
    call BlinkXS4 ("c28s003_070") from _call_BlinkXS4_80
    sim "Gracias... ¿Te gusta?"
    mc "Es clásica, pero te queda super sexy."
    mc "Ese es el apartamento de [oma], ¿no?"
    call BlinkXS4 ("c28s003_075") from _call_BlinkXS4_81
    sim "Sí, quedamos ahí algunas de las chicas para ver una serie en la tele y para enseñarnos la lencería que nos había comprado [emm]."
    sim "Acabamos probándonoslas y haciendo un mini pase de modelos."
    if eil._var("route") and sai._var("route") and oma._var("route"):
        sim "Como el que te han hecho a ti esta tarde, pero sin sexo. *Risita*"
    mc "Lo que me sorprende es la falta de rosa en la lencería que compró [emm]..."
    call BlinkXS4 ("c28s003_080") from _call_BlinkXS4_82
    sim "*Risa* ¡Tienes razón! Pero no te preocupes, ella compró los mismos modelos en rosa... para su propio uso."
    mc "No sé por qué, pero no me sorprende. Se tuvo que dejar un dineral en lencería."
    mc "Lo que me preocupa de la tuya es que parece difícil de quitar."
    stop music fadeout (1.5)
    sim "Sólo si no tienes delicadeza. Lleva unos corchetes por detrás que..."
    scene c28s003_080An with dissolve
    play music ("music/LePrunierenFleur.ogg")
    mc "Por alguna razón, hoy prefiero que no haya corchetes. Me encanta como te queda esta blusa, pero me gustará más cuando no la lleves puesta."
    sim "*Risa* ¡Sr. Marks! ¿Está usted intentando desnudarme?"
    mc "Sí. *Risa* Creía que había quedado claro. ¿Algún problema con ello?"
    call BlinkXS4 ("c28s003_085") from _call_BlinkXS4_83
    sim "Ninguno. *Risa* Solo era por aclarar las cosas. Puedes seguir."
    mc "A sus órdenes, Señorita Washington. *Risa*"
    scene c28s003_090An with dissolve
    "Tu boca baja, casi impulsada por su propia voluntad, buscan sus pezones, duros como piedras, capaces de cortar cristal."
    "Su cuerpo se estremece al primer contacto de tus labios sobre su sensible piel."
    sim "*Gemido* Puede continuar, Sr. Marks."
    scene c28s003_095An with dissolve
    "Te dedicas a juguetear con su pezón entre tus labios, rozándolo con la lengua, mordisqueándolo suavemente."
    sim "*Jadeo* Sabe que tiene una lengua fantástica, ¿verdad, Sr. Marks?"
    "El tono juguetón con el que te llama por tu apellido hace que la situación parezca algo inapropiado entre un jefe y su secretaria, o algo así."
    sim "*Gemido* ¿O debería llamarte Sr. NTR?"
    "Supones que se refiere a la beca."
    call BlinkXS4 ("c28s003_100") from _call_BlinkXS4_84
    mc "¿Aún tienes clavada la espina de la beca? No tuve nada que ver. La idea fue de [ama]."
    sim "Lo sé, no lo decía por eso..."
    mc "¿Entonces?"
    sim "Nada, una tontería... Continuemos. Creo que tu camiseta me está molestando."
    scene c28s003_105An with dissolve
    sim "Así mucho mejor..."
    mc "Sabes que, aunque sea una tontería, me lo puedes decir."
    sim "Lo sé, pero prefiero que lo olvides de momento. Te lo explico luego."
    scene c28s003_110An with dissolve
    "Ahora es ella la que se dedica a acariciar tus pezones con su lengua." id c28s003_SimLewd_fa74c059
    "Recorre tu areola con su lengua y es tu turno de que te recorran escalofríos."
    "No piensas insistir en preguntar a qué se refería. No quieres matar el ánimo. Ya habrá tiempo para eso luego."
    scene c28s003_115a with fade
    call BlinkXS4 ("c28s003_115") from _call_BlinkXS4_85
    sim "Estos pantalones también me molestan..."
    mc "Puedes quitármelos cuando quieras. A mí me están empezando a molestar también."
    scene c28s003_120An with dissolve
    "En unos rápidos movimientos te quita los pantalones y los calzoncillos, encontrándose cara a cara con Mjolnir."
    sim "Hola, amigo mío."
    mc "*Risa* ¿Hablas con Mjolnir?"
    call BlinkXS4 ("c28s003_125") from _call_BlinkXS4_86
    sim "*Risa* Hay que ser educada, ¿no?"
    scene c28s003_120d with dissolve
    sim "¿No te pongo cachondo hoy?"
    mc "Por supuesto. ¿Por qué lo preguntas?"
    call BlinkXS4 ("c28s003_130") from _call_BlinkXS4_87
    if eil._var("route") and sai._var("route") and oma._var("route"):
        sim "Lo veo diferente... Más pequeño... ¿Tanto te han cansado las chicas esta tarde?"
    elif oma._var("route"):
        sim "Lo veo diferente... Más pequeño... ¿Tanto te ha cansado [oma] esta tarde?"
    else:
        sim "Lo veo diferente... Más pequeño... ¿Has tenido un día muy duro?"
    sim "Incluso diría que ha cambiado de color... ¿Quieres que lo dejemos para otro día?"
    mc "Estoy un poco cansado hoy, pero eso no va a evitar que haga el amor con mi prometida."
    if mad._var("route"):
        mc "Y antes de que preguntes, no. No tengo un fetiche con el matrimonio."
        call BlinkXS4 ("c28s003_135") from _call_BlinkXS4_88
        sim "*Risa* Eso se lo dejamos a [mad.nick]."
        mc "*Risa* Sí, será lo mejor."
    else:
        pass
        call BlinkXS4 ("c28s003_135") from _call_BlinkXS4_89
    sim "Me parece una buena idea lo de hacer el amor con mi prometido."
    sim "Se me hace raro ser la única vestida... o más o menos vestida."
    mc "Eso tiene fácil solución. Ya te he dicho que esa blusa me gustaría más cuando no la llevaras puesta."
    scene c28s003_140An with dissolve
    call version28 from _call_version28_5
    "En unos segundos consigues que la diosa de ébano esté totalmente desnuda para ti."
    "Tus ojos tienen dificultades para decidir en qué parte de su perfecto cuerpo fijarse. Lo quieres ver todo a la vez."
    "Afortunadamente, vas a tener tiempo para grabar la imagen de su piel en tus retinas."
    mc "Espero que ya no creas que estás demasiado vestida."
    call BlinkXS4 ("c28s003_145") from _call_BlinkXS4_90
    sim "*Risa* Ahora no puedo estar más desnuda, con lo que... voy a tumbarme..."
    mc "Vamos a tumbarnos, querrás decir..."
    call BlinkXS4 ("c28s003_150") from _call_BlinkXS4_91
    sim "No, tú quédate ahí. Quiero aprovechar que hoy el Cockzilla no da tanto miedo para probar algo."
    mc "*Risa* Me encanta cuando quieres probar cosas..."
    sim "Es nuestra tercera vez juntos. Mi tercera vez en total. Aún tengo mil cosas que probar."
    scene c28s003_155a with fade
    call BlinkXS4 ("c28s003_155") from _call_BlinkXS4_92
    sim "Acércate."
    mc "¿No vas a acabar con dolor de cuello así?"
    call BlinkXS4 ("c28s003_160") from _call_BlinkXS4_93
    sim "Por eso se llama probar cosas. *Risita* Si veo que es incómodo, te diré de cambiar de postura."
    mc "Me parece un buen plan."
    scene c28s003_160d with dissolve
    mc "¿Aquí estoy bien?"
    sim "Perfecto, creo..."
    scene c28s003_910pv with dissolve
    show c28s003_910v
    mc "¡Oh! ¡Eso no me lo esperaba!"
    "Debido a la posición en la que está y a lo que ha dicho sobre el tamaño de Mjolnir, esperabas que te hiciera una garganta profunda."
    "Pero en vez de ello se dedica a chupar tus huevos mientras acaricia tu astil. Si esta era la prueba que quería hacer, estás contento de haberte afeitado hace poco."
    "No tienes ninguna queja por cómo ha empezado su prueba. Pero tienes la corazonada de que no va a acabar aquí."
    sim "*Slurp*"
    scene c28s003_905pv with dissolve
    show c28s003_905v
    hide c28s003_910v
    "El roce de su lengua en tu escroto es maravilloso. Notar cómo sus sensuales labios se cierran sobre uno de tus huevos es increíble."
    "Mientras tanto, su mano ejerce la presión perfecta sobre tu polla, moviéndola para que tus pelotas se balanceen dentro de su boca."
    "Empiezas a pensar que hacer esta prueba es una idea fantástica cuando de sus labios empiezan a escaparse pequeños gemidos y jadeos."
    sim "*Gemido* *Slurp* *Jadeo*"
    scene c28s003_900pv with dissolve
    show c28s003_900v
    hide c28s003_905v
    "No pasa mucho tiempo antes de que la diosa de ébano lleve su mano libre a su coño, demostrando que se está poniendo cachonda."
    sim "*Jadeo* *Slurp* *Gemido*"
    "Te sientes un poco inútil sin poder ayudarla en su placer, pero la posición no invita al contorsionismo."
    sim "*Gemido* *Slurp* *Jadeo*"
    "La preciosa escena de tu prometida dándote placer mientras se lo da a sí misma es alucinante."
    scene c28s003_915pv with dissolve
    show c28s003_915v
    hide c28s003_900v
    "Sabías que la prueba que [sim] quería hacer no iba a quedar en una chupada de huevos."
    sim "*Jadeo* *Slurp* *Gemido*"
    "Cuando empieza a juguetear con tu glande, sin meterse toda tu polla en la boca, sabes que ni siquiera va a quedar en esto."
    sim "*Gemido* *Slurp* *Jadeo*"
    "Empiezas a juguetear con sus pezones para no sentirte tan pasivo. Siempre te es difícil recibir placer sin dar nada a cambio."
    scene c28s003_920pv with dissolve
    show c28s003_920v
    hide c28s003_915v
    sim "*Jadeo* *Slurp* *Gemido*"
    "El juego de sus labios y su lengua alrededor de tu capullo es aún mejor que lo que estaban haciendo en tus huevos."
    "[sim] se está convirtiendo en una mujer muy generosa en lo que al sexo se refiere."
    sim "*Gemido* *Slurp* *Jadeo*"
    "No puedes esperar a tener su coño a tu alcance para empezar a darle placer también tú."
    scene c28s003_925pv with dissolve
    show c28s003_925v
    hide c28s003_920v
    "Puedes ver como sus caderas se empiezan a mover, ansiando una polla que tiene en la boca."
    sim "*Jadeo* *Slurp* *Gemido*"
    "Sabes que, si sigue así vas a correrte muy rápido. La punta de tu polla está recibiendo muchísima atención y no vas a poder aguantar mucho más."
    "No sabes si su prueba ha finalizado, con lo que decides informarle de que va a llevarte al orgasmo."
    sim "*Gemido* *Slurp* *Jadeo*"
    mc "[sim], si sigues así voy a correrme..."
    scene c28s003_160e with hpunch
    "La única muestra de haberte escuchado que da es para meterse tu polla hasta la garganta."
    "Al final, la prueba es la que pensabas desde el principio. Tan solo necesitabas un poco de paciencia para llegar al final de la prueba." id c28s003_SimLewd_1b440ae9
    sim "*Jadeo* *Slurp* *Gemido*"
    scene c28s003_930pv with dissolve
    show c28s003_930v
    hide c28s003_925v
    "La agarras por la nuca y empiezas a bombear con tus caderas, follándote su garganta y notando cómo la punta de tu polla roza con su úvula."
    sim "*Arcada*"
    "El primer recorrido produce una arcada en la chica. Por un momento te preocupas y paras de bombear."
    scene c28s003_930pv with dissolve
    mc "¿Estás bien? Si la prueba no es lo que esperabas..."
    sim "*Gemido* *Slurp afirmativo* *Jadeo*"
    mc "¿Sigo?"
    sim "*Gemido* *Slurp afirmativo* *Jadeo*"
    show c28s003_930v
    "Reemprendes las embestidas con tu polla en su boca, atento a si se vuelven a repetir las arcadas."
    sim "*Jadeo* *Slurp* *GEMIDO*"
    scene c28s003_935pv with dissolve
    show c28s003_935v
    hide c28s003_930v
    "Sus gemidos, cada vez más altos, te dicen que la prueba está saliendo a su entera satisfacción."
    "También a la tuya. No podías imaginar que [sim] tuviera este fetiche."
    sim "*GEMIDO* *Slurp* *JADEO*"
    "Hay tantas cosas que aún desconocéis el uno del otro..."
    "Lo bueno es que, con el espíritu aventurero que está demostrando la nadadora, podréis probar muchas cosas en el futuro y descubrir nuevos placeres compartidos."
    scene c28s003_940pv with dissolve
    show c28s003_940v
    hide c28s003_935v
    "Tu orgasmo se acerca a pasos agigantados, haciendo que tus tensas pantorrillas den pequeños saltos cuando tu glande choca con su garganta."
    sim "*JADEO* *Slurp* *GEMIDO*"
    "No vas a poder aguantar mucho más y no sabes si [sim] va a poder tragar todo lo que estás preparando."
    mc "Estoy a punto de llegar. ¿Paro?"
    sim "*GEMIDO* *SLURP NEGATIVO* *JADEO*"
    "Es increíble cómo eres capaz de entender perfectamente sus 'slurps'. Hace tantos años que os conocéis que no hacen falta palabras entre vosotros."
    call OrgasmXS4 ("c28s003_165") from _call_OrgasmXS4_13
    hide c28s003_940v
    mc "¡Mpfft!"
    "Descargas toda la leche acumulada en tus huevos en su garganta."
    sim "*GEMIDO* *SLURP TRIUNFAL* *JADEO*"
    "La posición de su cuello permite que no se pierda ni una gota, tragando todo tu semen de inmediato tal como sale de tu polla."
    "Tu descarga dura unos increíbles segundos en los que [sim] no deja de masajear tu astil con su lengua, intentando exprimir hasta la última gota."
    scene c28s003_170a with fade
    call BlinkXS4 ("c28s003_170") from _call_BlinkXS4_94
    sim "*Jadeo* ¿Qué tal? *Gemido*"
    mc "Puedes hacer todas las pruebas que quieras si son como esta. Ha sido fantástico."
    mc "Pero creo que te has quedado sin tu orgasmo..."
    call BlinkXS4 ("c28s003_175") from _call_BlinkXS4_95
    sim "Si no recuerdo mal, mi prometido tiene un agujero en medio de la cara. Lo veo abrirse y cerrarse mientras habla."
    sim "Le puedes dar un buen uso mientras te recuperas. Supongo que necesitarás diez minutos o así, ¿no?"
    sim "*Susurrando* Es otra cosa que también quiero probar..."
    mc "Más bien cinco. He dicho que estoy cansado, no muerto."
    scene c28s003_180a with fade
    call BlinkXS4 ("c28s003_180") from _call_BlinkXS4_96
    "Rodeas a una expectante [sim] y te tumbas en la cama."
    mc "Te estoy esperando. Trae mi postre aquí."
    sim "Creía que... el borde de la cama... "
    mc "Si lo prefieres, puedo volver ahí." id c28s003_SimLewd_268648aa
    sim "No es necesario... no sabía cómo querías hacerlo..."
    "De pronto está insegura por alguna razón que no comprendes."
    mc "¿Pasa algo, [sim]?"
    call BlinkXS4 ("c28s003_185") from _call_BlinkXS4_97
    sim "Es la primera vez que me vas a comer ahí abajo..."
    mc "Lo sé, y estoy ansioso por hacerlo."
    sim "Estoy muy mojada... si me pongo encima tuyo... a lo mejor goteo... por eso pensaba... que en el borde de la cama..."
    mc "Sabes que cuando tengas un orgasmo voy a bebérmelo todo, ¿verdad?"
    mc "No solo no me importa si goteas, cielo. Me encantará que lo hagas."
    call BlinkXS4 ("c28s003_190") from _call_BlinkXS4_98
    sim "¿Vas a hacerme llegar al orgasmo antes de recuperarte? Soy lenta con las pajas y, aunque las chicas me hayan dicho lo contrario, no debes ser muy diferente, ¿no?"
    mc "Tendrás que experimentarlo por ti misma, cielo. Y aunque me recupere, puedo seguir comiéndote durante horas. *Risa* Yo estaré tumbado."
    mc "Siendo la primera vez que te como, quiero que experimentes el viaje completo."
    call BlinkXS4 ("c28s003_195") from _call_BlinkXS4_99
    sim "Me acabas de convencer. ¿Cómo me pongo?"
    mc "Ponte de rodillas encima de mi cara. Bueno, tus rodillas en el colchón, no encima de mi cara."
    call BlinkXS4 ("c28s003_200") from _call_BlinkXS4_100
    sim "*Risa* ¿Me estás llamando tonta?"
    mc "*Risa* No, pero llevas los mismos genes que Jamaal, con lo que nunca podré estar seguro de si solo finges inteligencia."
    sim "*Risa* A veces te odio."
    scene c28s003_205a with fade
    call BlinkXS4 ("c28s003_205") from _call_BlinkXS4_101
    sim "¿Estoy bien aquí?"
    mc "Perfecta. Déjame probar una cosa."
    scene c28s003_985pv with fade
    "Compruebas que tu lengua pueda llegar a los labios inferiores de [sim] sin tener que dejarte el cuello en el proceso."
    scene c28s003_210a with hpunch
    call BlinkXS4 ("c28s003_210") from _call_BlinkXS4_102
    sim "*GEMIDO* ¿QUÉ HA SIDO ESO? *JADEO*"
    mc "La comprobación de que estás en el sitio perfecto. ¿Sigues pensando que es igual que una paja?"
    scene c28s003_990pv with dissolve
    show c28s003_990v
    "Sin dejarle responder, empiezas a lamer el chorreante coño de la nadadora."
    sim "*JADEO* ¡JODEL! *GEMIDO* ¡Las chicas tenían razón! *JADEO*"
    "Escuchar nunca se le ha dado bien a [sim]. Debería prestar más atención a las chicas con más experiencia que ella."
    sim "*GEMIDO* ¡Esto es mejor de lo que podía haber esperado! *JADEO*"
    "No ha goteado, pero vas recogiendo todos sus jugos tal como van haciendo aparición entre sus labios."
    call OrgasmXS4 ("c28s003_215") from _call_OrgasmXS4_14
    sim "*JADEO* ¡IMPOSIBLE! *GEMIDO* ¡INCREÍBLE! *JADEO*"
    "Para ser lenta con las pajas y creer que iba a durar lo mismo, ha explotado en tu boca tras tan solo unos cuantos lengüetazos."
    "Sigues lamiendo. Nunca más va a ser la primera vez que le comes el coño, y quieres que su recuerdo sea imborrable."
    scene c28s003_985pv with dissolve
    show c28s003_985v
    hide c28s003_990v
    "Sus generosos e hinchados labios se adaptan a tu lengua a la perfección mientras ésta recorre cada rincón."
    sim "*GEMIDO* ¡POR DIOS! *JADEO* ¡ALUCINANTE! *GEMIDO*"
    "Se acabaron los comentarios con más de un par de palabras. Orgasmo tras orgasmo recorren a la diosa de ébano y no es capaz de articular frases largas."
    sim "*JADEO* ¡MIELDA, MIELDA, MIELDA! *GEMIDO*"
    "No te sorprende la facilidad de palabra de tu prometida, aunque dudas que pueda escribir un libro."
    scene c28s003_980pv with dissolve
    show c28s003_980v
    hide c28s003_985v
    "Su cuerpo empieza a comportarse de una forma extraña. La fluidez de sus movimientos ha desaparecido por completo."
    sim "*GEMIDO* ¡NO PUEDO MÁS! *JADEO* ¡ESTO NO ES NORMAL! *GEMIDO*"
    "No te atreves a parar los movimientos de tu lengua. Ni te atreves ni quieres hacerlo."
    sim "*JADEO* ¡VOY A CAMBIAR DE POSTURA! *GEMIDO*"
    "Parece que, al final, es demasiado para ella. Estás contento de que haya disfrutado su primera vez. Se ha merecido un descanso antes del plato principal."
    scene c28s003_220An with dissolve
    "Para tu sorpresa, [sim] no quiere descansar. Cambia tu boca por Mjolnir y se mete la punta dentro de su chorreante coño."
    sim "*GEMIDO* ¡Jodel! *JADEO* ¡[eil] tenía razón! *GEMIDO*"
    "[eil] es la única chica que ha cortado una comida de coño para empalarse en Mjolnir. O era la única chica hasta ahora."
    "Parece que [sim] ha aprendido a escuchar. Al menos cuando le interesa."
    scene c28s003_945pv with dissolve
    show c28s003_945v
    hide c28s003_980v
    "Manteniendo precariamente su equilibrio sobre tus muslos y sin penetrarse del todo con Mjolnir, [sim] empieza a mover sus caderas."
    "Es casi una repetición de cuando jugaba con tu glande con su boca, pero esta vez con su vagina."
    sim "*JADEO* ¡ME ENCANTA! *GEMIDO*"
    "La altura a la que está, te da un perfecto acceso a su clítoris, que sigues acariciando después de haberlo lamido."
    "Sus orgasmos siguen llegando, haciendo que su equilibrio sea aún más inestable."
    scene c28s003_955pv with dissolve
    show c28s003_955v
    hide c28s003_945v
    sim "*GEMIDO* Debe haber un lugar especial en el cielo para los hombres que masajean el clítoris de sus mujeres cuando tienen la polla dentro. *JADEO*"
    "No lo sabes ni te importa. La reacción de su cuerpo a tus caricias es premio suficiente."
    "Y su juego de caderas mientras tiene tu glande dentro es totalmente alucinante. Puedes notar cómo su túnel vaginal se cierra con fuerza sobre tu glande."
    "Los consejos de [meg] sobre el uso de los músculos vaginales son una maravilla. Y [sim] vuelve a demostrar que sabe escuchar."
    sim "*JADEO* La posición es incómoda... *GEMIDO* Pero se siente increíble... *JADEO*"
    scene c28s003_950pv with dissolve
    show c28s003_950v
    hide c28s003_955v
    "La mezcla de placer y agotamiento que cruza por su rostro te dice todo lo que necesitas saber."
    "Puede cambiar de posición cuando quiera, ya que, por primera vez en vuestras sesiones de sexo, ella lleva el mando. Pero no lo hace."
    sim "*GEMIDO* Voy a empezar a follarte... *JADEO* No puedo esperar más. *GEMIDO*"
    "Pero, sin embargo, ahí sigue, masajeando tu glande con la entrada de su vagina mientras tu acaricias su clítoris." id c28s003_SimLewd_34c70102
    "Podrías pasarte mucho tiempo así, pero sabes que la mujer no va a poder aguantar mucho más."
    scene c28s003_960pv with dissolve
    show c28s003_960v
    hide c28s003_950v
    "Ella también lo sabe y, sin llegar a hacer penetraciones profundas, empieza a subir y a bajar a lo largo de tu astil."
    sim "*JADEO* ¡ESTO ES MEJOR AÚN! *GEMIDO* ¡TE QUIERO! *JADEO*"
    "Mueves tus manos para darle apoyo y ayudarle a marcar el ritmo. Su agotamiento es patente y sus movimientos no son tan fluidos como antes."
    mc "Yo también te quiero."
    "No es una frase vacía. Realmente amas a esta mujer, independientemente de si estáis follando, besándoos, o sólo mirándoos a los ojos."
    scene c28s003_965pv with dissolve
    show c28s003_965v
    hide c28s003_960v
    "Su túnel vaginal se contrae con fuerza sobre Mjolnir por el placer que su cascada de orgasmos y tus palabras le producen."
    "Sabes que las palabras pueden ser poderosas. Pero veinte orgasmos uno detrás de otro también pueden serlo."
    sim "*GEMIDO* ¡LO... SÉ! *JADEO*"
    "Vuelven las frases cortas. Se empieza a quedar sin aliento después de estar corriéndose ininterrumpidamente durante los últimos minutos."
    "Tú estás llegando al punto en que tu orgasmo te va a dejar sin respiración por un par de segundos."
    scene c28s003_970pv with dissolve
    show c28s003_970v
    hide c28s003_965v
    "A veces envidias a las mujeres y su capacidad de llegar decenas de veces al clímax una tras otra. Sólo a veces."
    "Entonces recuerdas el placer de provocarle esas decenas de orgasmos a una mujer a la que amas y dejas de envidiarlas."
    sim "*JADEO* ¿Estás a punto de llegar? *GEMIDO* Noto tu polla palpitar dentro de mí. *JADEO*"
    "En vuestra tercera vez juntos, se ha convertido en una experta en leer tu lenguaje corporal y los pequeños cambios en Mjolnir cuando tu orgasmo se acerca."
    mc "Casi estoy ahí..."
    "Si hubiera preguntado unos segundos después, la pregunta no hubiera sido necesaria. La descarga de leche que vas a soltar en su interior hubiera sido respuesta suficiente."
    if persistent.pregnancy and not sim._var("pregnant"):
        if persistent.walkthrough:
            $ wt1 = _("[sim] embarazada.")
            $ wt2 = _("Sin consecuencias.")
        else:
            $ wt1 = ""
            $ wt2 = ""
        menu:
            "Correrte dentro. Ir a por el bebé." (wt = wt1):
                $ sim._var("pregnant", True)
                $ sim._var("undiscoveredPregnancy", True)
                play sound ("music/OldMusicBox5.ogg")
            "Correrte dentro." (wt = wt2):
                pass
    $ resetWalkthrough ()
    call OrgasmXS4 ("c28s003_225") from _call_OrgasmXS4_15
    mc "¡Mpfft!"
    "Tu aguante llega a su límite y descargas una gran cantidad de semen en el interior de tu prometida."
    sim "*GEMIDO* ¡SÍ! *JADEO*"
    "Tu segunda corrida de la noche no es tan abundante como la primera, pero no por ello es menos placentera."
    "Incluso tus huevos tienen un límite con el semen que pueden crear en un solo día."
    scene c28s003_230a with fade
    call BlinkXS4 ("c28s003_230") from _call_BlinkXS4_103
    stop music fadeout (1.5)
    "Al cabo de unos minutos, cuando vuelve a recuperar el control de su cuerpo, [sim] se derrumba sobre tu pecho." id c28s003_SimLewd_22afc360
    play music ("music/Separation.ogg")
    mc "¿Qué tal tus pruebas? Hoy hemos hecho muchas cosas nuevas."
    sim "¡Todo lo que hemos hecho ha sido nuevo! Y me ha parecido increíble."
    mc "Y lo siguiente que vamos a probar va a ser dormir juntos. ¿Te mueves mucho?"
    call BlinkXS4 ("c28s003_235") from _call_BlinkXS4_104
    sim "*Risa* Por lo que dice mi madre, me muevo como una pelota en un terremoto."
    sim "Yo espero que tú no ronques mucho. *Risa*"
    mc "Nadie se ha quejado hasta ahora. *Risa* Si descontamos a tu hermano en aquel campamento al que fuimos con 14 años."
    mc "*Risa* Pero sabemos que tu hermano no es de fiar."
    mc "¿Tienes sueño?"
    call BlinkXS4 ("c28s003_240") from _call_BlinkXS4_105
    sim "Más que tener sueño, estoy cansada. He trabajado esta mañana, y esta tarde he estado nadando con [deb.nick]. ¿Y tú?"
    mc "Estoy cansado también. Ha sido un día muy largo."
    call BlinkXS4 ("c28s003_245") from _call_BlinkXS4_106
    sim "¿Dormimos entonces?"
    if mar._var("route") or kia._var("route"):
        $ onlyOne = False
        mc "Si quieres sí, pero tengo una pregunta. ¿Qué era eso de Sr. NTR?"
        call BlinkXS4 ("c28s003_250") from _call_BlinkXS4_107
        sim "*Risa* Una tontería. Sé que mi hermano y tú jugáis a novelas visuales, pero nunca me han llamado la atención."
        sim "Pero desde que me enteré de que [deb.nick] juega, me ha explicado un poco de qué va."
        mc "Qué tu ídolo se interese por algo tiene ese efecto secundario."
        call BlinkXS4 ("c28s003_255") from _call_BlinkXS4_108
        sim "No creo que sea un tipo de juego que vaya a jugar. Prefiero vivirlo en vez de leerlo."
        sim "Pero [deb.nick] me explicó la terminología y, cuando llegó a lo de NTR, no podíamos parar de reírnos."
        mc "Normal, es el nombre de la empresa y... Tu hermano también se rio. Creía que le estaba tomando el pelo." id c28s003_SimLewd_7fda4888
        call BlinkXS4 ("c28s003_260") from _call_BlinkXS4_109
        sim "No solo por eso. Aunque es gracioso."
        if mar._var("route") and kia._var("route"):
            sim "Pero lo más gracioso es que, desde tu punto de vista, les has hecho netori a Solomon y a tu padre."
            sim "Pero desde su punto de vista, les has hecho un NTR como un camión. Aunque tu padre aún no lo sabe."
            sim "En una novela visual donde ellos fueran los protagonistas, tú serías el 'malo'."
        elif mar._var("route"):
            $ onlyOne = True
            sim "Pero lo más gracioso es que, desde tu punto de vista, le has hecho netori a tu padre."
        else:
            $ onlyOne = True
            sim "Pero lo más gracioso es que, desde tu punto de vista, le has hecho netori a Solomon."
        if onlyOne:
            if mar._var("route"):
                sim "Pero desde su punto de vista, le has hecho un NTR como un camión. Al menos cuando se entere." id c28s003_SimLewd_eddd4742
            else:
                sim "Pero desde su punto de vista, le has hecho un NTR como un camión."
            sim "En una novela visual donde él fuera el protagonista, tú serías el 'malo'."
        mc "*Risa* Se me pasó por la cabeza una vez."
        if not onlyOne:
            mc "Ciertamente, sería NTR de manual desde sus puntos de vista. Pero me alegra estar en el bando de los 'malos' por una vez."
        elif mar._var("route"):
            if persistent.family:
                mc "Mi padre y mi madre no han roto oficialmente porque no han hablado desde que se fue, con lo que, técnicamente, mi madre le ha puesto los cuernos conmigo."
            else:
                mc "Mi padre y [mar] no han roto oficialmente porque no han hablado desde que se fue, con lo que, técnicamente, [mar] le ha puesto los cuernos conmigo."
            mc "Ciertamente, sería NTR de manual desde el punto de vista de mi padre. Pero me alegra estar en el bando de los 'malos' por una vez."
        else:
            mc "Si tenía que estar en el bando de los 'malos' alguna vez, me alegra que sea en la historia de la que Solomon es protagonista."
        call BlinkXS4 ("c28s003_265") from _call_BlinkXS4_110
        sim "¿No te ha molestado que haya hecho una broma sobre eso?"
        mc "En absoluto. Sabes que me gusta reírme de cualquier cosa."
        sim "Entonces, ¿podemos dormir ya? Me estoy empezando a caer de sueño..."
    mc "Me parece una idea estupenda."
    scene c28s003_270a with fade
    "Os acurrucáis el uno en brazos del otro preparándoos para pasar vuestra primera noche juntos."
    sim "Se nos olvida algo..."
    mc "¿El qué?"
    call KissXS4 ("c28s003_275") from _call_KissXS4
    sim "Esto. Buenas noches, mi amor."
    mc "Buenas noches. Te quiero."
    sim "Yo también."
    scene c28s003_270a with dissolve
    "[sim] vuelve a su posición entre tus brazos. Se siente bien notar su peso sobre tu pecho."
    "Es algo de lo que nunca te cansarás en los años venideros."
    scene c28s003_270b with fade
    "Apagas la luz con un comando de voz en el momento en el que [sim] empieza a respirar profundamente."
    "Quizás deberías haber empezado a salir con ella antes."
    scene black with dissolve
    "Te duermes pensando en si [eil] hubiera aceptado un harén en el instituto."
    if not mar._var("route") and not kia._var("route"):
        "Su comentario llamándote Sr. NTR no vuelve a tu cabeza."
    stop music fadeout (1.5)
    return
label c28s004_MarRing:
    if _in_replay:
        call mrS3_sim_route from _call_mrS3_sim_route_7
        call mrS3_mar_route from _call_mrS3_mar_route_17
        call mrS3_lis_route from _call_mrS3_lis_route_13
        call mrS3_kia_route from _call_mrS3_kia_route_13
        call mrS3_mad_route from _call_mrS3_mad_route_10
        if mc._var("relationships")<2:
            call mrS3_rels from _call_mrS3_rels_21
    scene black with dissolve
    centered "{size=+20}{b}DÍA 31 – JUEVES{/b}{/size}"
    scene c28s004_005a with dissolve
    if sim._var("route"):
        "Cuando te despiertas, [sim] no está en la habitación. Dormías tan plácidamente que no te has dado cuenta de cuándo se ha ido."
    else:
        "Te despiertas descansado después de una noche en la que has tenido la enorme cama para ti solo."
    play music ("music/SaveMe.ogg")
    "Decides bajar a la cocina a desayunar. Por alguna razón te has despertado hambriento."
    scene c28s004_010a with fade
    call BlinkXS4 ("c28s004_010") from _call_BlinkXS4_111
    if persistent.family:
        mc "Buenos días, Mamá."
    else:
        mc "Buenos días, [mar]."
    mom "Buenos días, dormilón."
    mc "¿Es muy tarde? Ni siquiera he mirado el reloj al despertarme."
    call BlinkXS4 ("c28s004_015") from _call_BlinkXS4_112
    mom "*Risa* Ni te has peinado."
    mom "Y sí, es tarde. Aunque no es el día que más tarde te has levantado."
    mc "*Risa* Otra vez con la fama de dormilón. Inmerecida totalmente."
    call BlinkXS4 ("c28s004_020") from _call_BlinkXS4_113
    mom "Desayuna algo antes de que se te haga más tarde y se te junte con la hora de comer."
    mom "Hoy he hecho donuts, pero no quedan muchos. ¿Te preparo un café?"
    mc "Gracias, no hace falta. Lo preparo yo."
    if mar._var("route"):
        call KissXS4 ("c28s004_025") from _call_KissXS4_1
    call BlinkXS4 ("c28s004_025") from _call_BlinkXS4_114
    mom "¿Qué planes tienes para hoy?"
    if lis._var("route"):
        mc "Esta noche voy a la fiesta de la amiga de [lis]. Aparte de eso no tengo nada especial planeado."
    mc "Seguir leyendo documentación sobre NTR. Aaron me manda un montón de documentos todos los días."
    if mad._var("route") or kia._var("route"):
        call BlinkXS4 ("c28s004_030") from _call_BlinkXS4_115
        mom "*Risita* ¿Alguna nueva propuesta de matrimonio?"
        mc "*Risa* Veo que las noticias vuelan."
        call BlinkXS4 ("c28s004_035") from _call_BlinkXS4_116
        mom "¿Esperabas algo distinto?"
        mc "No. *Risa* Pero no es algo que se planee."
        call BlinkXS4 ("c28s004_040") from _call_BlinkXS4_117
        mom "*Risa* La mayoría de los hombres lo planean... Algunos durante meses o años."
        if mad._var("route") and kia._var("route"):
            mc "Yo no. En los dos casos fue algo que parecía natural en aquel momento."
        else:
            mc "Yo no. En aquel momento parecía lo más natural del mundo."
        mc "Si lo hubiera tenido que planear, seguramente no lo hubiera hecho. Al menos no antes de ir a Aruba."
        call BlinkXS4 ("c28s004_045") from _call_BlinkXS4_118
        mom "Creo que es bueno que lo hayas hecho antes de irte."
        mc "¿Por qué? No es que me vaya a la guerra o algo por el estilo."
        call BlinkXS4 ("c28s004_050") from _call_BlinkXS4_119
        if mad._var("route") and kia._var("route"):
            mom "Las dos tendrán más razones para esperar ansiosas a que vuelvas."
            if sim._var("route"):
                "Por alguna razón, está omitiendo a [sim]. ¿No se lo ha contado aún o como ha sido ella la que te lo ha propuesto no viene a cuento?"
        else:
            mom "Ella tendrá más razones para esperar ansiosa a que vuelvas."
        mc "*Risa* Creía que mi arrebatadora personalidad era suficiente."
        if mc._var("relationships")>1:
            call BlinkXS4 ("c28s004_055") from _call_BlinkXS4_120
            mom "¿Qué piensas hacer respecto a las bodas? ¿Te vas a casar con alguien en realidad?"
            mc "¿Firmar un papel y esas cosas? No puedo. No podría elegir a una sola por encima del resto."
            mc "Se me ocurrirá algo, pero no me importa nada firmar ese papel o no hacerlo."
        else:
            call BlinkXS4 ("c28s004_055") from _call_BlinkXS4_121
            mom "¿Habéis planificado alguna fecha?"
            mc "No, fue todo muy rápido. No sé ni siquiera si querrá hacerlo realmente."
            if mad._var("route"):
                mc "Obviamente, no sería en una iglesia. Ya conoces a [mad.nick] y sabes que le tiene un poco de alergia a las iglesias."
            else:
                mc "Además, está el tema del divorcio por en medio. Hasta que no lo consiga, no hay nada que planear."
        mc "Pero sólo estamos hablando de mí."
    mc "¿Qué planes tienes tú para hoy?"
    call version28 from _call_version28_6
    call BlinkXS4 ("c28s004_060") from _call_BlinkXS4_122
    mom "*Risa* Cocinar para mucha gente. Hacer la colada. Limpiar la casa. Leer unos correos electrónicos... Lo normal."
    mc "Vaya, lo normal para un ama de casa. *Risa*"
    mom "*Risa* Es lo que soy."
    if mar._var("route"):
        scene c28s004_065An1 with dissolve
        mc "Ummm..."
        mom "¿Qué pasa?"
        scene c28s004_065An2 with dissolve
        mom "*Risa* ¡No!"
        mc "*Risa* Sí."
        scene c28s004_065d with dissolve
        if persistent.family:
            mc "Mamá, ¿quieres casarte conmigo?"
        else:
            mc "[mar], ¿quieres casarte conmigo?"
        mom "*Risa* ¿Con un dónut?"
        mc "Es lo más parecido a un anillo que hay por aquí."
        if mad._var("route") or kia._var("route"):
            mc "Y sabes que lo del anillo de pedida estándar no es lo mío."
        call BlinkXS4 ("c28s004_070") from _call_BlinkXS4_123
        mom "¿Lo estás diciendo en serio?"
        mc "Claro que sí. *Risa* Y espero una respuesta antes de que me empiece a doler la rodilla."
        call BlinkXS4 ("c28s004_075") from _call_BlinkXS4_124
        mom "¡Por supuesto que sí!"
        scene c28s004_075d with hpunch
        "Os lanzáis a los brazos del otro, vuestros labios buscándose para decirse cosas que las palabras no pueden expresar."
        "Hay alegría en el beso. Hay esperanza. Hay ilusión."
        "Hay falta de aire."
        call BlinkXS4 ("c28s004_080") from _call_BlinkXS4_125
        "Todo lo bueno acaba, y os separáis reluctantemente."
        mom "¡Estás loco!"
        mc "Si yo estoy loco por proponerlo, tu debes estar loca por aceptarlo."
        mom "Estaría loca si no lo hubiera hecho."
        call BlinkXS4 ("c28s004_085a") from _call_BlinkXS4_126
        mom "*Risa* Pero la mayoría de gente hace esto durante una cita o algo por el estilo."
        mc "*Risa* Y la mayoría de gente hace esto sin un dónut. No saben lo que se pierden."
        mc "Además, aunque me encantan las citas contigo, no creo que necesitemos seguir los protocolos. Me parecía natural pedírtelo ahora."
        call BlinkXS4 ("c28s004_085b") from _call_BlinkXS4_127
        mom "Natural e inesperado. Pero tienes razón, prefiero esto aquí que en un restaurante rodeados de gente que se pongan a grabar con los móviles." id c28s004_MarRing_2d9ac8e8
        mom "Es más natural. Más... nuestro."
        scene c28s004_085d with dissolve
        mom "¡[mc]! ¡Ni se te ocurra comerte mi anillo de compromiso!"
        call BlinkXS4 ("c28s004_090") from _call_BlinkXS4_128
        mc "Perdón, es la costumbre. *Risa* ¿Te lo vas a poner?"
        mom "No me cabría en el dedo y se acabaría rompiendo, pero voy a conservar ese dónut para siempre."
        mc "¿Lo vas a congelar?"
        mom "Algo se me ocurrirá."
        if persistent.family or mc._var("relationships")>1:
            call BlinkXS4 ("c28s004_095") from _call_BlinkXS4_129
            mom "Pero sabes que no nos vamos a poder casar nunca, ¿verdad?"
            if persistent.family:
                mom "No creo que nunca dejen que una madre se case con su hijo."
            else:
                if mc._var("relationships")==2:
                    mom "Tu otra novia me mataría si te casas conmigo y no con ella."
                else:
                    mom "El resto me mataría si te casas conmigo y no con ellas."
            mc "No necesito que ningún gobierno me diga con quién puedo casarme."
            mc "Desde este momento me considero casado contigo."
        else:
            call BlinkXS4 ("c28s004_095") from _call_BlinkXS4_130
            mom "No me casé con tu padre y ahora me voy a casar contigo..."
            mc "No lo digas en futuro. Desde este momento me considero casado contigo."
        call BlinkXS4 ("c28s004_100") from _call_BlinkXS4_131
        mom "*Risa* ¿Un dónut como anillo de pedida y también como anillo de bodas? Te salgo barata..."
        mc "*Risa* Y más barata aún teniendo en cuenta que el dónut lo has cocinado tú."
        call BlinkXS4 ("c28s004_105") from _call_BlinkXS4_132
        mom "Bueno, algún día lo cambiaré por algo más permanente."
        mc "Si quieres podemos ir a comprar un anillo mañana."
        call BlinkXS4 ("c28s004_110") from _call_BlinkXS4_133
        mom "No hay prisa en comprarlo. Como has dicho, ya nos podemos considerar casados desde este momento."
        mom "Y ahora quiero un beso de mi marido."
        scene c28s004_075d with dissolve
        "Vuestras bocas se vuelven a juntar, firmando con vuestros labios un inexistente papel que sella vuestro matrimonio."
        "Te alegra poder pensar en [mar] como tu esposa."
        "Y no tiene nada que ver con la manía que le tienes a la palabra 'novia'."
    stop music fadeout (1.5)
    return
label c28s004_ScaGetsJob:
    if _in_replay:
        call mrS3_mar_route from _call_mrS3_mar_route_18
        call mrS3_dap_route from _call_mrS3_dap_route_11
        call mrS3_mad_route from _call_mrS3_mad_route_11
    scene c28s004_150a with hpunch
    "La puerta se abre de golpe."
    play music ("music/Swing.ogg")
    sca "¡Tía [mar], [mc]! ¡He conseguido el trabajo!"
    dap "*Risa* Creo que he visto esta escena seis veces en los últimos 15 minutos."
    if mar._var("route"):
        scene c28s004_150b with hpunch
        sca "¡Oops! ¡Perdón! ¿Interrumpo algo?"
        dap "Creo que sí. Ya volveremos."
        mc "No os preocupéis."
    mc "Felicidades, [sca]. ¿Ves como no tenías que estar preocupada?"
    call BlinkXS4 ("c28s004_155") from _call_BlinkXS4_134
    call version28 from _call_version28_7
    mom "Felicidades, cariño. ¿Cuándo empiezas a trabajar?"
    call BlinkXS4 ("c28s004_160") from _call_BlinkXS4_135
    sca "El lunes. Mañana por la tarde tengo que ir a la oficina en San Luis para firmar el contrato y que me den los uniformes."
    mc "Si quieres puedo llevarte, aún no tengo nada importante que hacer mañana por la tarde."
    call BlinkXS4 ("c28s004_165") from _call_BlinkXS4_136
    sca "No hace falta, pero gracias. Se lo he pedido a Tía [nor]."
    mc "*Risa* ¿Vais a ir con su coche? Te arriesgas a no llegar."
    call BlinkXS4 ("c28s004_170") from _call_BlinkXS4_137
    dap "Yo le he dicho lo mismo. *Risa* Me ha dicho que le pedirá el coche a Tía [mar] para asegurarse de que no pasa nada."
    call BlinkXS4 ("c28s004_175") from _call_BlinkXS4_138
    mom "Ningún problema, puede cogerlo cuando quiera."
    mc "*Risa* Sólo falta que no te dejes las luces encendidas y te quedes sin batería."
    call BlinkXS4 ("c28s004_180") from _call_BlinkXS4_139
    mom "Si pasa eso, [nor] tendrá que coger tu camioneta. *Risa* Seguro que no te ríes tanto entonces."
    mc "¡Nooo! *Risa* Tengo que ir a comprobar si tu coche tiene batería."
    call BlinkXS4 ("c28s004_185") from _call_BlinkXS4_140
    sca "Ahora estoy nerviosa por si tendrán uniformes de mi talla... O si me quedará bien."
    mc "Si te hacen ir a las oficinas, seguro que tienen uniformes de diversas tallas. No tienes por qué preocuparte."
    call BlinkXS4 ("c28s004_190") from _call_BlinkXS4_141
    call version28 from _call_version28_8
    dap "Y seguro que le queda bien. A las chicas delgadas y con tetas pequeñas como ella toda la ropa les queda bien."
    scene c28s004_190d with dissolve
    dap "¿Has hecho donuts, Tía [mar]? ¿Puedo coger uno?"
    if mar._var("route"):
        scene c28s004_195d with hpunch
        mom "¡No! ¡Ese no!"
        call BlinkXS4 ("c28s004_200") from _call_BlinkXS4_142
        dap "¿Qué le pasa a este dónut?"
        mc "Que lo he tocado yo."
        scene c28s004_195e with dissolve
        pause (1.3)
        call BlinkXS4 ("c28s004_195") from _call_BlinkXS4_143
        mom "Ya conoces la costumbre que tiene [mc] de tocarlo todo..."
        call BlinkXS4 ("c28s004_205") from _call_BlinkXS4_144
        sca "¿Ha usado ese dónut como anillo de compromiso?"
        call BlinkXS4 ("c28s004_210a") from _call_BlinkXS4_145
        mom "*Risita* ¡Sí!"
        mc "Creo que me estoy volviendo demasiado previsible. *Risa*"
        call BlinkXS4 ("c28s004_210b") from _call_BlinkXS4_146
        dap "¿Con un dónut? Es un poco cutre, ¿no?"
        call BlinkXS4 ("c28s004_215") from _call_BlinkXS4_147
        sca "No le hagas caso. Yo creo que es super dulce."
        sca "¡Felicidades! Supongo que ha dicho que sí, viendo su reacción con el dónut."
        mc "Sí, ha dicho que sí."
        call BlinkXS4 ("c28s004_220") from _call_BlinkXS4_148
        dap "*Risa* Yo creía que Tía [mar] era la lista de la familia."
        if dap._var("route"):
            mc "*Risa* Supongo que eso quiere decir que no quieres que te lo pida a ti cuando tenga la ocasión."
            call BlinkXS4 ("c28s004_225") from _call_BlinkXS4_149
            dap "*Risa* Si soy la única a la que no se lo pides, tu personaje de DnD tendrá una vida muuuuy corta."
            dap "Ya sabes... un rayo que cae en tu saco de dormir, una caída que acaba con tu propia daga en tu garganta... Esas cosas que pasan cuando no le pides matrimonio al DM..."
        else:
            mc "*Risa* Precisamente porque es la lista de la familia es por lo que ha aceptado."
        dap "Felicidades a los dos."
        if mad._var("route"):
            call BlinkXS4 ("c28s004_235") from _call_BlinkXS4_150
            sca "Pero, después de lo de [mad.nick] yo creía que..."
            scene c28s004_240a with hpunch
            mar "¡Hush!" (multiple=2)
            dap "¡[sca]!" (multiple=2)
            scene c28s004_240b with hpunch
            sca "¡Oops! Perdón..."
            mc "¿Qué pasa?"
            scene c28s004_230e with dissolve
            todas "Nada, nada. No te preocupes."
            mc "*Risa* Eso casi me preocupa más que si no hubierais dicho nada."
            mc "Pero supongo que no os voy a sacar ninguna información."
            todas "Ni una palabra."
    else:
        call BlinkXS4 ("c28s004_230") from _call_BlinkXS4_151
        mom "Sí, coge los que quieras."
    scene c28s004_230f with dissolve
    mc "Por cierto, ¿por qué vais disfrazadas?"
    dap "Nos estábamos probando ropa cuando [sca] ha recibido la llamada." id c28s004_ScaGetsJob_dc53d40d
    sca "Queríamos hacer unas fotos de cosplay para subirlas a InstaPic."
    scene c28s004_230d with fade
    if mar._var("route"):
        "Después de eso, pasáis un rato charlando de la propuesta de matrimonio y del trabajo de [sca]."
        if mad._var("route"):
            "Obviamente, lo que fuera a escapársele a [sca] no vuelve a hacer su aparición en la conversación."
    else:
        "Pasáis un rato charlando del trabajo de [sca], intentando sin éxito quitarle los nervios."
    "Al cabo de un rato las chicas deciden seguir visitando a todo el mundo para dar la noticia. Hay una nueva camarera en la familia."
    scene black with dissolve
    stop music fadeout (1.5)
    "Tú vuelves a tu habitación. Estás seguro de que Aaron te habrá mandado dos o tres correos a estas horas."
    return
label c28s004_DebKiaraTalk:
    if _in_replay:
        $ mc._var("relationships", 0, "set")
        call mrS3_kia_route from _call_mrS3_kia_route_14
        call mrS3_mad_route from _call_mrS3_mad_route_12
        call mrS3_mar_route from _call_mrS3_mar_route_19
        call mrS3_deb_route from _call_mrS3_deb_route_18
        call mrS3_bet_route from _call_mrS3_bet_route_8
        call mrS3_mee_route from _call_mrS3_mee_route_11
        if mc._var("relationships")<2:
            call mrS3_rels from _call_mrS3_rels_22
    scene c28s004_250a with fade
    play music ("music/RhythmPlay.ogg")
    kia "Ahora te busco ese libro. Me extraña que no tengan las memorias de Dana Torres en la universidad."
    deb "No es que no lo tengan. Es que solo tienen un ejemplar y alguien lo ha cogido justo hoy."
    deb "Tengo ganas de leerlo y no quiero esperar a que lo devuelvan."
    call BlinkXS4 ("c28s004_255") from _call_BlinkXS4_152
    kia "¿Por eso has pensado en mí?"
    kia "*Risa* Solo me quieres por mis libros..."
    call BlinkXS4 ("c28s004_260") from _call_BlinkXS4_153
    deb "*Risa* Sabes que no es verdad. Te quiero por muchas más cosas. Pero adoro tus libros y que nos podamos sentar en la piscina a hablar de ellos."
    deb "No hay mucha gente en casa con quien hablar de algunos libros."
    call BlinkXS4 ("c28s004_265") from _call_BlinkXS4_154
    kia "Tienes razón. No hay muchos fans de Jane Austen en casa."
    kia "¿Quieres llevarte algún libro más?"
    call BlinkXS4 ("c28s004_270") from _call_BlinkXS4_155
    deb "Sí. Mira a ver si tenéis '¿Por qué Tía [kia] no nos ha dicho que ayer fue su cumpleaños?'"
    deb "Dicen que es un clásico sobre la gente que cree que no tiene nada que celebrar."
    call BlinkXS4 ("c28s004_275") from _call_BlinkXS4_156
    kia "¿Me vas a echar la bronca por no celebrar mi cumpleaños?"
    call BlinkXS4 ("c28s004_280") from _call_BlinkXS4_157
    deb "Esa era una de mis ideas cuando venía hacia aquí. [eil] nos lo ha dicho esta mañana."
    deb "Primero le hemos echado la bronca a ella por no decírnoslo antes para prepararte una fiesta sorpresa."
    call BlinkXS4 ("c28s004_285") from _call_BlinkXS4_158
    kia "No me gustan las fiestas sorpresa, y no me gusta celebrar mi cumpleaños."
    kia "Con lo que es mejor que [eil] os lo haya dicho cuando ya ha pasado. De todas formas, le echaré bronca por decíroslo." id c28s004_DebKiaraTalk_cf466563
    call BlinkXS4 ("c28s004_290") from _call_BlinkXS4_159
    deb "Se le ha escapado. Estábamos tomando el sol y [sca] ha venido preguntando las fechas de nacimiento."
    deb "Quiere hacer algo con una app para que no se nos olvide nunca felicitarnos entre nosotras."
    deb "[eil] ha dicho su fecha de nacimiento y la tuya. Todas hemos flipado cuando nos hemos dado cuenta de que tu cumpleaños fue ayer."
    call BlinkXS4 ("c28s004_295") from _call_BlinkXS4_160
    kia "¿[eil] no os ha dicho por qué no lo celebro?"
    call BlinkXS4 ("c28s004_300") from _call_BlinkXS4_161
    deb "Nos ha dicho que no te gusta hacerlo, pero no nos ha querido contar por qué." id c28s004_DebKiaraTalk_3602b04a
    call BlinkXS4 ("c28s004_305") from _call_BlinkXS4_162
    kia "Mis cumpleaños dejaron de ser importantes cuando nació ella. No porque naciera ella, claro."
    kia "Pero es cuando todo se empezó a ir a la mierda con Solomon."
    call BlinkXS4 ("c28s004_310") from _call_BlinkXS4_163
    kia "Cada vez tenía menos ganas de celebrar nada que no tuviera que ver directamente con [eil]."
    kia "Ella no tenía que pagar las consecuencias de un matrimonio infeliz."
    call BlinkXS4 ("c28s004_315") from _call_BlinkXS4_164
    kia "Y celebrar mi cumpleaños era un recordatorio de que... no sé..."
    kia "Cuando Solomon empezó a olvidarlos casi me alegré. Se convirtió en una costumbre no celebrarlos. Porque no había nada que celebrar."
    call BlinkXS4 ("c28s004_320") from _call_BlinkXS4_165
    deb "Pero ahora Solomon no está, con lo que sería un buen momento para volver a celebrarlos."
    deb "No te vas a librar. Recuerda lo bien que estuvo la fiesta de las chicas."
    call BlinkXS4 ("c28s004_325") from _call_BlinkXS4_166
    kia "*Risa* Ellas cumplían 19. ¡Yo cumpliré 48 en mi próximo cumpleaños!"
    kia "*Risa* No creo que sea algo para celebrar."
    call BlinkXS4 ("c28s004_330") from _call_BlinkXS4_167
    call version28 from _call_version28_9
    deb "Pues celebremos el primer año sin Solomon el día de tu cumpleaños."
    if kia._var("route"):
        deb "Y tu primer año con [mc]."
    deb "Al menos así no coincidirá con el cumpleaños de las chicas. Y si no quieres, te haremos una fiesta sorpresa."
    call BlinkXS4 ("c28s004_335") from _call_BlinkXS4_168
    kia "*Risa* Las fiestas sorpresa las odiaba antes de conocer a Solomon. Ni se os ocurra hacerme una si no queréis verme enfadada de verdad."
    kia "Voy a buscarte ese libro antes de que llegue más gente."
    scene c28s004_250b with fade
    deb "*Escribiendo en el grupo de WhatsUp 'Fiesta sorpresa para [kia]'* Chicas, fiesta sorpresa de mañana anulada. Parece que realmente no le gustan." id c28s004_DebKiaraTalk_5a865f4a
    eil "*En el grupo de WhatsUp* Os lo he dicho. Sé cómo es mi madre..."
    sca "*En el grupo de WhatsUp* Mañana preguntaré en el grupo general a quién le gustan las fiestas sorpresa. Así [kia] puede decir que a ella no."
    sca "*En el grupo de WhatsUp* Lo añadiré a la ficha de cada una en la app."
    sai "*En el grupo de WhatsUp* Eso le quitará algo de sorpresa a las fiestas. Pero puedes apuntar que a mí no me desagradan."
    if mad._var("route") and mc._var("relationships")>1:
        scene c28s004_340a with fade
        call BlinkXS4 ("c28s004_340") from _call_BlinkXS4_169
        "Un par de minutos después..."
        kia "Aquí tienes el libro. ¿Necesitas alguna cosa más?"
        call BlinkXS4 ("c28s004_345") from _call_BlinkXS4_170
        if kia._var("route"):
            deb "Como tu fuiste la primera..."
        deb "¿Quería preguntarte qué te parece la idea de [mad.nick] sobre los anillos?"
        deb "Creo que resolvería el problema del que se estuvo hablando el otro día en el grupo de WhatsUp."
        call BlinkXS4 ("c28s004_350") from _call_BlinkXS4_171
        kia "A mí me parece una idea buenísima. Ponerse de acuerdo iba a ser muy difícil."
        if kia._var("route"):
            kia "Yo ya tengo mi anillo y tenía pensado hacer uno de verdad con la misma forma, pero..."
        call BlinkXS4 ("c28s004_355") from _call_BlinkXS4_172
        deb "Yo creo que iba a ser imposible ponerse de acuerdo."
        deb "Ya sabes, diferentes gustos y diferentes expectativas..."
        call BlinkXS4 ("c28s004_360") from _call_BlinkXS4_173
        if mar._var("route"):
            kia "Y después de lo de [mar] de hoy... Creo que no se puede ser más original."
            kia "Ya me dirás tú dónde podría encontrar [mar] un anillo con forma de dónut."
        kia "Además, creo que lo de [mad.nick] con el post-it es casi insuperable."
        call BlinkXS4 ("c28s004_365") from _call_BlinkXS4_174
        deb "La verdad es que ya empiezo a tener ganas de que llegue el día..."
        if not deb._var("route"):
            deb "Aunque no vaya a participar, me encantaría estar ahí cuando suceda."
        call BlinkXS4 ("c28s004_370") from _call_BlinkXS4_175
        kia "[mad.nick] decía que no hay demasiada prisa, pero creo tampoco hay demasiado tiempo."
        kia "La semana que viene se irá a Aruba, y la idea de [mad.nick] era para hacerla antes de que se fuera."
        if not kia._var("route") and not deb._var("route"):
            kia "Las chicas van a tener que darse prisa."
        elif not kia._var("route") and deb._var("route"):
            kia "Vais a tener que daros un poco de prisa."
        elif kia._var("route"):
            kia "Vamos a tener que darnos prisa."
        call BlinkXS4 ("c28s004_375") from _call_BlinkXS4_176
        if bet._var("route") or mee._var("route"):
            deb "Hay que esperar a que vuelvan las Chicas de Oro. No se puede hacer nada antes de que regresen."
        else:
            deb "Aunque las Chicas de Oro no estén implicadas, creo que habría que esperar a que estén aquí para hacerlo."
        if meg._var("route"):
            deb "Y [meg] tendrá que venir también... Tienes razón, no hay muchos días en que lo podamos hacer..."
        scene c28s004_250c with dissolve
        "Las dos mujeres continúan charlando un rato, haciendo planes sobre la idea de [mad.nick]."
        "¿Quién podía pensar que un post-it cambiaría el futuro de la familia?"
    stop music fadeout (1.5)
    return
label c28s005_EriNor:
    if _in_replay:
        $ mc._var("relationships", 0, "set")
        call mrS3_pat_file from _call_mrS3_pat_file
        call mrS3_nor_route from _call_mrS3_nor_route_11
        call mrS3_rels from _call_mrS3_rels_23
    scene c28s005_005a with fade
    "Pasas toda la mañana leyendo los informes de Aaron. Te inunda con tanta información que te sientes sobrepasado."
    play music ("music/Sad-Cinematic.ogg")
    "Desde informes financieros, pasando por listas de compras e inventarios, a los informes detallados de todas las misiones que NTR ha hecho en los últimos años."
    "Te detienes especialmente en los informes de las misiones que han hecho [eva] y [ama], sorprendiéndote por las muchas cosas que han hecho."
    "También lees los informes de las misiones de Beatrice, Clarice, y Diana. Es una forma de saber más sobre las chicas que nunca conocerás. No hay informes sobre Fiona." id c28s005_EriNor_cd3ff40a
    "Hay muchos informes que descartas o lees tan solo por encima. No crees que tu trabajo como CEO incluya saber cuántos rollos de papel higiénico se gastan mensualmente en la base."
    "Tienes que decirle a Aaron que sólo te envíe la documentación relevante o no vas a poder leerlo todo antes de ir a Aruba."
    "Después de comer, encuentras un informe financiero que llama tu atención. No acabas de entenderlo y decides ir a consultarlo con [nor]."
    "Desde el desayuno solo has salido de tu habitación para comer. Ir a ver a [nor] servirá para despejar la cabeza después de tantas horas leyendo documentación."
    python:
        if "kal" not in globals () or not isinstance (kal, TGCharacter):
            kal = TGCharacter ("Kalyani", color = "#af6d16", lname = "Singh", nick = "Kaly")
            kal._var ("birthday", "2021-09-09")
            kal._var ("age", 18)
            kal._var ("job", _("estudiante"))

        if "pat" not in globals () or not isinstance (pat, TGCharacter):
            if mc._var("lookedCharlotte"):
                pat = TGCharacter (pat.name.first_name, color = "#40bdce", lname = "Robinson", nick = pat.nick)
            else:
                pat = TGCharacter ("Charlotte", color = "#40bdce", lname = "Robinson", nick = "Charlie")
            pat._var ("birthday", "2021-01-02")
            pat._var ("age", 18)
            pat._var ("job", _("estudiante"))

        if "zoe" not in globals () or not isinstance (zoe, TGCharacter):
            zoe = TGCharacter ("Zoe", color = "#5f40ce", lname = "Perceval")
            zoe._var ("birthday", "2021-05-28")
            zoe._var ("age", 18)
            zoe._var ("job", _("estudiante"))

        if "cri" not in globals () or not isinstance (cri, TGCharacter):
            cri = TGCharacter ("Christine", color = "#dcf4a7", lname = "Song", nick = "Christy")
            cri._var ("birthday", "2021-08-07")
            cri._var ("age", 18)
            cri._var ("job", _("estudiante"))

        if "nia" not in globals () or not isinstance (nia, TGCharacter):
            nia = TGCharacter ("Nia", color = "#bab55d", lname = "Serrat")
            nia._var ("birthday", "2021-08-20")
            nia._var ("age", 18)
            nia._var ("job", _("estudiante"))

        if "hai" not in globals () or not isinstance (hai, TGCharacter):
            hai = TGCharacter ("Hailey", color = "#7cb2db", lname = "Jenkinson")
            hai._var ("birthday", "2021-09-03")
            hai._var ("age", 18)
            hai._var ("job", _("estudiante"))
    scene c28s005_005b with fade
    stop music fadeout (1.5)
    "Al llegar a la cocina de [nor]..."
    play music ("music/Gypsy-Jazz.ogg")
    eri "¡Esta es preciosa!"
    nor "Todas lo son. *Risa* Parece que en la universidad hicieron un cásting para enviarnos a las chicas más guapas."
    scene c28s005_005c with dissolve
    eri "*Risa* Tienes razón."
    nor "Aunque las más guapas ya estaban aquí. Nadie supera a mis dos niñas."
    eri "*Risa* ¡Mamá!"
    mc "Hola, chicas. ¿Qué hacéis?"
    scene c28s005_005d with dissolve
    nor "Hola, [mc]. Han llegado las fotos de las nuevas estudiantes."
    mc "¿Para los expedientes? Ya teníamos esas fotos, ¿no?"
    if mc._var("lookedCharlotte"):
        mc "Vi la foto de [pat]..."
    eri "No, ha sido una idea que ha tenido [kal.nick], la prima de [sai]. Debían hacerse una foto a la vez, estuvieran donde estuvieran." id c28s005_EriNor_b984b454
    mc "*Risa* Espero que no hubiera ninguna en el lavabo."
    call BlinkXS4("c28s005_010") from _call_BlinkXS4_177
    call version28 from _call_version28_10
    nor "*Risa* ¡Qué bruto eres! Supongo que, en ese caso, la hubieran enviado más tarde."
    nor "No creo que una foto sentada en el retrete sea la mejor presentación, pero con las chicas jóvenes nunca lo puedes saber."
    call BlinkXS4("c28s005_015") from _call_BlinkXS4_178
    eri "¡Mamá! ¡No todas nos tomamos fotos cada vez que respiramos!"
    eri "Hasta ahora no hemos tenido ninguna selfie-adicta."
    mc "Recuerda el meme. Neil Armstrong fue a la luna y tomó tres fotos. Ashley fue al lavabo y tomó 45."
    call BlinkXS4("c28s005_020") from _call_BlinkXS4_179
    eri "*Risa* Eres un capullo. Y tú también perteneces a la generación selfie."
    mc "*Risa* Sí, pero yo soy feo, con lo que no me saco fotos."
    mc "A ver esas fotos de las chicas nuevas."
    call BlinkXS4("c28s005_025") from _call_BlinkXS4_180
    nor "*Risa* Sabía que no te ibas a poder resistir. Y eso que no sabes que algunas están en bikini."
    if mc._var("lookedCharlotte"):
        mc "*Risa* Bueno, ya he visto fotos de [kal] y de [pat]. Me faltan las otras cuatro. No quiero discriminar a nadie."
    else:
        mc "*Risa* Bueno, ya he visto fotos de [kal]. Me faltan las otras cinco. No quiero discriminar a nadie."
    call BlinkXS4("c28s005_030") from _call_BlinkXS4_181
    eri "Hay una que no ha enviado la foto todavía. A lo mejor no lo hace. Era opcional, aunque las indicaciones de [kal.nick] eran que tenían que hacerlas hace un par de horas." id c28s005_EriNor_cdc0fb39
    mc "Bueno, pues enseñadme las fotos de las otras. Empiezo a tener curiosidad por cómo son."
    scene c28s005_035a with dissolve
    nor "Esta es [kal.nick], pero ya lo sabes por las fotos que te había enseñado [sai]." id c28s005_EriNor_aa5bf397
    mc "¿Sigue de vacaciones por Europa? Eso no parece la India."
    nor "Sí, en el correo dice que está en Alemania ahora."
    eri "Es guapísima. No sé si me parece más guapa ella o [sai]."
    mc "[sai] siempre habla de ella como 'mi prima la guapa'. *Risa* A lo mejor el resto de sus primas son horribles."
    call BlinkXS4("c28s005_040") from _call_BlinkXS4_182
    eri "Maldición, hasta yo la llamaría 'mi prima la guapa'. *Risa* Aunque [emm] se enfadaría si me oyera."
    mc "*Risa* Puedo imaginarme a [emm] entrando en modo asesina psicópata si te oye decir algo como eso."
    scene c28s005_035b with dissolve
    nor "Esta es... ¿cómo se llamaba esta, [eri]?"
    $ nia.name.first_name = renpy.input (_("¿Cómo se llama esta chica?"), default = "Nia")
    $ persistent.niaName = nia.name.first_name
    $ nia.color = "#bab55d"
    eri "[nia] Serrat. Es de Nueva York."
    mc "¿Otra deportista? ¿Viene becada?"
    call BlinkXS4("c28s005_045") from _call_BlinkXS4_183
    nor "En su expediente no pone nada sobre deporte. Estudia Administración de Empresas. Supongo que tan solo estaba jugando un partido de voleibol cuando tocó hacer la foto."
    mc "Pues al fotógrafo le ha quedado una foto fantástica. A ver la siguiente..."
    scene c28s005_035c with dissolve
    eri "Esta es... espera que mire el nombre..."
    $ hai.name.first_name = renpy.input (_("¿Cómo se llama esta chica?"), default = "Hailey")
    $ persistent.haiName = hai.name.first_name
    $ hai.color = "#7cb2db"
    eri "[hai] Jenkinson. De Verbena, Alabama. Estudia trabajo social."
    mc "Me recuerda a alguien y no sé a quién."
    call BlinkXS4("c28s005_050") from _call_BlinkXS4_184
    eri "A mí me ha pasado lo mismo."
    eri "Mi madre dice que se parece a una chica en una vieja peli, en que está montada en un caballo de esos para niños que les echas una moneda."
    mc "¡Maldición! Es verdad. Recuerdo esa peli."
    call BlinkXS4("c28s005_055") from _call_BlinkXS4_185
    nor "¡Hey! *Risa* ¡La peli no es tan vieja! Debía tener 12 o 14 años cuando la vi por primera vez."
    mc "*Levanta una ceja*"
    nor "*Risa* Vale, sí. Es una peli vieja. Veamos la siguiente foto antes de que tenga que ir a cambiarme los pañales de anciana."
    mc "*Risa* La peli es vieja. Tú eres solo una veterana. Pero sí, siguiente foto."
    scene c28s005_035d with dissolve
    $ persistent.patName = pat.name.first_name
    $ persistent.patNick = pat.nick
    eri "Esta es [pat], pero prefiere que la llamemos [pat.nick]. Es la más joven de todas."
    $ persistent.patNick = pat.nick
    eri "Va a estudiar medicina, con lo que es probable que vaya a clases con [sca]."
    if mc._var("lookedCharlotte"):
        eri "Pero eso ya lo sabes, miraste su expediente."
    mc "No sé por qué, pero me suena de algo."
    call BlinkXS4("c28s005_060") from _call_BlinkXS4_186
    eri "¿No la recuerdas?"
    mc "¿Debería?"
    call BlinkXS4("c28s005_065") from _call_BlinkXS4_187
    nor "¿Te acuerdas de cuando [dap] y [sca] no eran amigas aún porque se consideraban rivales por ser la que sacaba mejores notas?"
    mc "Sí, pero de eso hace muchísimo. Son amigas desde... ¿que tenían diez u once?"
    call BlinkXS4("c28s005_070") from _call_BlinkXS4_188
    eri "Sí, desde que tuvieron que hacer un trabajo en parejas y se dieron cuenta de que podían ser aliadas. Yo lo hice con [emm]."
    eri "[pat.nick] y Patricia eran las mejores amigas de [sca] por entonces. [pat.nick] vivía aquí, en Newport, hasta que sus padres se mudaron de vuelta a Charlotte."
    eri "Vino a casa un par de veces."
    mc "Debe ser de eso que me suena, pero no soy capaz de recordarla."
    call BlinkXS4("c28s005_075") from _call_BlinkXS4_189
    nor "Era una niña y ahora es una mujer. No me extraña que no seas capaz de reconocerla."
    mc "Me parece que le pasaría lo mismo a cualquiera que me hubiera conocido hace diez años y viera una foto mía actual."
    call BlinkXS4("c28s005_080") from _call_BlinkXS4_190
    nor "*Risa* Casi te pasó a ti cuando me viste al volver de la universidad, y yo no era una foto."
    mc "*Risa* Es que faltaba la mitad de mi Tía [nor] cuando volví."
    mc "Pero sigamos con las fotos. Queda otra, ¿no?"
    scene c28s005_035e with dissolve
    nor "Sí, también está en una playa o algo así."
    $ cri.name.first_name = renpy.input (_("¿Cómo se llama esta chica?"), default = "Christine")
    nor "Pero prefiere que la llamen por el diminutivo..."
    $ cri.nick = renpy.input (_("¿Cuál es el diminutivo que usa?"), default = "Christy")
    $ persistent.criName = cri.name.first_name
    $ persistent.criNick = cri.nick
    $ cri.color = "#dcf4a7"
    mc "*Risa* Parece que esta no quería que le sacaran la foto."
    call BlinkXS4("c28s005_085") from _call_BlinkXS4_191
    eri "*Risa* Tienes razón. Nos ha dicho que se la ha sacado su padre por sorpresa."
    eri "Dice que una foto es solo una imagen que no refleja su personalidad y que no iba a enviarla, pero que su padre ha insistido."
    mc "¡Ufff! ¿Es de esas? Es una simple foto..."
    call BlinkXS4("c28s005_090") from _call_BlinkXS4_192
    nor "Ya sabes cómo son algunas chicas a esta edad. Algunas son muy vehementes en sus creencias."
    nor "Y otras están muy inseguras de su físico como para que una foto sea su presentación."
    call BlinkXS4("c28s005_095") from _call_BlinkXS4_193
    eri "No todas somos así, Mamá."
    mc "Creo que se refiere a las chicas 'normales'. Por suerte tú eres especial."
    call BlinkXS4("c28s005_100") from _call_BlinkXS4_194
    nor "Ayer mismo, hablando de esta iniciativa de [kal.nick], [kim] dijo que hubiera venido insegura si hubiera visto fotos de [lis], [deb.nick], [sai], y [kat]."
    nor "Creo que seríamos el resto las que hubiéramos estado inseguras si ella nos hubiera mandado una foto como estas."
    mc "No tenéis que estarlo. Sabéis que todas tenéis un tipo de belleza diferente, pero eso no os hace menos hermosas que las otras, ¿no?"
    call BlinkXS4("c28s005_105a") from _call_BlinkXS4_195
    eri "Las mujeres somos así, [mc]. Lo raro es que no hayan aparecido envidias entre nosotras..."
    eri "Creo que, si no se hubiera creado el sentimiento de pertenencia a algo mayor, sí que hubieran aparecido."
    mc "Entonces me alegro de que el sentimiento de familia esté ahí. Podríais convertir la casa en un infierno si empezáis con las envidias."
    mc "¿Qué estudia [cri]?"
    call BlinkXS4("c28s005_105b") from _call_BlinkXS4_196
    nor "Una doble licenciatura en Leyes y Estudios de Género."
    mc "La segunda carrera y el pelo verde explica lo de que la foto es solo una imagen y blah blah blah."
    call BlinkXS4("c28s005_105c") from _call_BlinkXS4_197
    eri "No empieces a juzgarlas antes de que lleguen."
    mc "No sé por qué, pero esa chica creo que puede ser problemática..."
    eri "Creo que será mejor esperar a conocerla para sacar conclusiones, ¿no?"
    mc "Tienes razón... a lo mejor es como lo de [lis] con el veganismo y el ecologismo. Pasados los primeros días no ha dado ningún problema."
    mc "Pero... ¿podéis volver a enseñarme las fotos de las chicas en bikini?"
    call BlinkXS4("c28s005_110") from _call_BlinkXS4_198
    nor "*Risa* ¿Estás empezando a babear?"
    if mc._var("relationships")>1:
        nor "¿O es que estás pensando en meterlas en el harén?"
    mc "*Risa* No es eso. Es que me ha parecido ver algo, pero no estoy seguro."
    scene c28s005_110An with dissolve
    nor "Aquí las tienes. ¿Qué has visto?"
    mc "Dame un segundo..."
    mc "..."
    scene c28s005_035b with dissolve
    mc "Ahí está. ¿Sabéis si se conocen? ¿Han ido juntas a Aruba?"
    scene c28s005_005An
    eri "¿Cómo sabes que es Aruba?" (multiple=2)
    nor "¿Qué?" (multiple=2)
    scene c28s005_035b with dissolve
    mc "Mira ahí. Los dos tíos paseando por la playa. Uno es Aaron y va con un clon de la Serie G."
    nor "No me había dado cuenta..."
    eri "Estábamos mirando a [nia]..."
    nor "¿Cómo sabes que es Aaron? No se le ve la cara..."
    mc "Mira la foto de [pat]..."
    scene c28s005_035d with dissolve
    mc "En esta foto se ve también a Aaron y al G. Incluso a [nia] saltando en su partido de volleyball."
    nor "¡Qué vista tienes!"
    eri "*Risa* Que hayas visto a Aaron teniendo en cuenta que está encima del culo de [pat.nick]..."
    mc "*Risa* Por eso no lo he visto la primera vez..."
    mc "Tampoco me he fijado en que el bikini y la funda del móvil la van a convertir en amiga de [emm]. *Risa*"
    scene c28s005_005g with dissolve
    nor "*Risa* Yo sí que me había fijado en eso. No es exactamente rosa, sino coral oscuro, pero a [emm] le va a encantar."
    mc "Rosa, coral, fucsia... Sabéis que soy un tío, ¿verdad? *Risa* Sólo hay seis colores en el mundo. Diez a lo sumo. El resto son tonos de esos colores."
    eri "*Risa* A veces me sorprende que te aguantemos..."
    eri "¿Pero [cri.nick]? ¿Por qué crees que también está en Aruba?"
    scene c28s005_035e with dissolve
    mc "Porque [pat] está detrás. Fíjate en la rubia con el móvil rosa... coral... detrás de [cri]. Lleva el mismo bikini."
    mc "Y el colchón de la tumbona es igual, y a la siguiente tumbona le falta el colchón. ¿Cuántas probabilidades hay de que sea otra chica en otro sitio?"
    eri "¡Es verdad! ¡Es ella!"
    nor "Y [cri.nick] está en una posición en la que tapa a quienquiera que estuviese sacando la foto de [pat.nick]."
    call BlinkXS4("c28s005_115") from _call_BlinkXS4_199
    eri "Si no han ido juntas, se van a llevar una sorpresa cuando vean las fotos."
    eri "Ellas van a reconocer el sitio sin fijarse en cosas como las tumbonas o Aaron."
    mc "Pueden empezar a crear lazos allí en vez de esperar a llegar aquí. ¿Cuándo llegan?"
    call BlinkXS4("c28s005_120") from _call_BlinkXS4_200
    nor "Entre el 2 y el 4 de septiembre. La primera en llegar será [kal.nick]."
    mc "¿Os dais cuenta de que ya las estáis llamando por los diminutivos?"
    call BlinkXS4("c28s005_125") from _call_BlinkXS4_201
    eri "Es mejor que empecemos a pensar en ellas de la forma en que prefieren que las llamen."
    eri "No queremos que les pase como a [mad.nick] con su madre."
    mc "Tienes razón, no lo había pensado."
    play sound ("music/notification.ogg")
    "*Ding-Ding*"
    call BlinkXS4("c28s005_130") from _call_BlinkXS4_202
    nor "Espera, ha entrado un correo nuevo."
    nor "Roger Perceval... es el mismo apellido que el de la chica que falta..."
    mc "¿Cómo se llama?"
    $ zoe.name.first_name = renpy.input (_("¿Cómo se llama la última chica?"), default = "Zoe")
    $ persistent.zoeName = zoe.name.first_name
    $ zoe.color = "#5f40ce"
    nor "..."
    call BlinkXS4("c28s005_135a") from _call_BlinkXS4_203
    nor "*Risa*"
    mc "¿Qué pasa?"
    call BlinkXS4("c28s005_130") from _call_BlinkXS4_204
    nor "Os lo leo..."
    nor "Sra. Marks,"
    nor "Soy Roger, el hermano de [zoe]. Mi hermana no quería enviarles la foto, pero como supongo que sería la única en no hacerlo, le he sacado la foto yo."
    nor "Sé que quizás sea un poco inapropiada, pero es que la he despertado para hacérsela. Salimos de fiesta anoche y aún no se había levantado."
    nor "Llevo corriendo delante de ella un rato porque quería quitarme el móvil. XD. Me va a odiar por esto, al menos durante cinco minutos."
    nor "Un saludo,"
    nor "Roger"
    call BlinkXS4("c28s005_135b") from _call_BlinkXS4_205
    eri "La odio antes de conocerla. *Risa*"
    mc "¿Por qué?"
    scene c28s005_035f with dissolve
    eri "¡Mira! Se ha ido a dormir maquillada y está guapísima recién levantada en vez de parecer un oso panda o un payaso."
    mc "*Risa* ¿Detecto un poco de envidia?"
    eri "¿Un poco? *Risa* Si yo me fuera a dormir maquillada acabaría con pintalabios por toda la almohada y por toda la cara."
    nor "*Risa* Y esa almohada la ibas a lavar tú. El pintalabios se lava fatal."
    mc "*Risa* No me parecen buenas razones para odiarla. Le deberíais preguntar que marca de pintalabios usa."
    mc "No la juzguéis hasta que no llegue aquí."
    eri "Touché."
    call BlinkXS4("c28s005_140") from _call_BlinkXS4_206
    eri "¿Qué estudiaba [zoe], Mamá?"
    mc "¿Y de dónde es?"
    call BlinkXS4("c28s005_145") from _call_BlinkXS4_207
    nor "Estudia Ingeniería Informática y es de Boston."
    mc "Es decir... Futuras Doctora, Ingeniera, Abogada, Administradora de Empresas... y Estudios de Género... ¿Y las otras dos?"
    nor "[kal.nick] estudia Arte, como [lis] y [emm], y [hai] estudia Trabajo Social. [emm] y [kal.nick] seguro que comparten clases."
    mc "*Risa* Con un poco de suerte, [kal] no pasa por una época rosa como Picasso..."
    call BlinkXS4("c28s005_150") from _call_BlinkXS4_208
    eri "No coinciden ninguna en los estudios, pero tampoco en de dónde son."
    eri "India, Massachusetts, Alabama, Carolina del Norte, Nueva York, y California."
    mc "¿Quién era la de California?"
    call BlinkXS4("c28s005_155") from _call_BlinkXS4_209
    nor "[cri.nick], la que te cae mal. *Risa* Es de San Diego, como [oma]... Bueno, donde se crió [oma]."
    mc "No me cae mal. Me genera desconfianza. Hay muy buen rollo en la familia ahora mismo para que venga alguien problemático."
    mc "Y sólo es una intuición. No digo que lo sea."
    nor "Por cierto, supongo que venías por algo que no eran las fotos... ¿Necesitabas algo?"
    mc "Te he mandado un correo con un informe financiero que no acabo de entender. ¿Me puedes echar una mano?"
    call BlinkXS4("c28s005_160") from _call_BlinkXS4_210
    eri "Si vais a hablar de cosas aburridas, me voy a mi habitación. Mándame el número de teléfono de [zoe], Mamá."
    mc "*Risa* ¿Vas a escribirle un WhatsUp para preguntarle por la marca de maquillaje que usa?"
    scene c28s005_160d with dissolve
    eri "*Risa* Obviamente..."
    mc "*Risa* Sois tan previsibles..."
    call BlinkXS4("c28s005_165") from _call_BlinkXS4_211
    nor "Veamos ese informe financiero..."
    scene c28s005_165d with fade
    "Pasáis un rato estudiando el informe, hasta descubrir que es un informe falsificado para poder cuadrar los libros de la doble contabilidad."
    "Difícilmente lo hubieras podido descubrir sin la ayuda de [nor]."
    scene c28s005_170a with fade
    pause (0.25)
    call BlinkXS4("c28s005_170") from _call_BlinkXS4_212
    nor "Pues ya está. Por eso no lo entendías."
    mc "Este Xabier Daniels era un genio del mal, al menos en cuanto a esconder dinero..."
    mc "Por cierto, lo de [eri] con el maquillaje me ha dado una idea."
    if persistent.family:
        mc "Cuando les mandes las fotos a las chicas nuevas, ¿por qué no les sugieres crear un grupo de WhatsUp con ellas, tú, y mi madre?"
    else:
        mc "Cuando les mandes las fotos a las chicas nuevas, ¿por qué no les sugieres crear un grupo de WhatsUp con ellas, tú, y [mar]?"
    mc "Puedes decirles que es por si necesitan información de Newport, o de nuestra casa."
    call BlinkXS4("c28s005_175") from _call_BlinkXS4_213
    nor "¿Por qué? Si necesitan saber algo, me mandan un correo."
    mc "Ya, pero no se pueden comunicar entre ellas directamente si no es pasando por ti."
    mc "Si se parecen en algo al resto de vosotras, crearán un nuevo grupo entre ellas para estar en contacto antes de venir."
    mc "Si no, al menos tendrán un sitio donde compartir sus inquietudes sobre la mudanza a un sitio nuevo."
    call BlinkXS4("c28s005_180") from _call_BlinkXS4_214
    nor "¡Eres un genio! No se me había ocurrido. Precisamente lo de las fotos empezó con el correo que [kal.nick] me escribió porque no podía escribirles a ellas."
    nor "Ahora les pediré permiso para crear el grupo. Creo que es una idea genial."
    mc "Perfecto. Pues voy a ir a seguir estudiando la documentación. Tengo una llamada con Aaron en un rato."
    if nor._var("route"):
        call KissXS4("c28s005_185") from _call_KissXS4_2
    call BlinkXS4("c28s005_185") from _call_BlinkXS4_215
    nor "Perfecto, te veo luego."
    mc "Hasta luego, [nor]."
    stop music fadeout (1.5)
    scene black with dissolve
    return
label c28s004_LisaDress:
    if _in_replay:
        call mrS3_lis_route from _call_mrS3_lis_route_14
        call mrS3_eva_route from _call_mrS3_eva_route_15
        call mrS3_emm_route from _call_mrS3_emm_route_19
    scene c28s004_500a with fade
    "Mientras lees expedientes, en la habitación de [lis] y [deb.nick]..."
    play music ("music/PositiveWoman.ogg")
    lis "Chicas, necesito consejo. ¿Qué vestido me pongo para la fiesta?"
    emm "Algo rosa. El rosa siempre queda bien en las fiestas."
    eva "No le hagas ni puto caso. Algo color crema. El crema te queda muy bien."
    call BlinkXS4("c28s004_505") from _call_BlinkXS4_216
    lis "No me estáis ayudando, chicas. El rosa no es mi color habitual. Y el vestido crema que tengo es demasiado formal para esa fiesta."
    lis "Había pensado en algún vestido de colores claros, quiero algo que transmita alegría. Aunque negro también estaría bien."
    call BlinkXS4("c28s004_520") from _call_BlinkXS4_217
    emm "El negro te queda muy bien, pero empecemos con las preguntas básicas."
    emm "¿Cuántos vestidos tienes que sean candidatos para ponerte en esa fiesta?"
    call BlinkXS4("c28s004_515") from _call_BlinkXS4_218
    lis "Unos 43. No, espera. 42. A uno se le descosió la cremallera."
    lis "Tengo algunos en la habitación de [bet]... Ella tiene tan poca ropa..."
    call BlinkXS4("c28s004_530") from _call_BlinkXS4_219
    eva "*Risa* ¿42 vestidos? Creo que no te va a dar tiempo de probártelos todos. Dentro de un mes y medio tengo que estar en Aruba. *Risa*"
    eva "Era imposible que quepan todos en ese armario. Y el armario de [bet] tiene que estar llenísimo con tantos vestidos."
    eva "*Risa* Te podemos guardar unos cuantos en la base antes de que el armario de [bet] explote..."
    call BlinkXS4("c28s004_525") from _call_BlinkXS4_220
    call version28 from _call_version28_11
    lis "¡Chicas, no es broma!"
    if lis._var("route"):
        lis "Pero quiero estar guapa para la cita con [mc]."
        call BlinkXS4("c28s004_510") from _call_BlinkXS4_221
        emm "[eva] tiene razón. Para cuando acabes de probarte los 42 vestidos, hará una semana que ha acabado la fiesta."
        emm "Lleves lo que lleves le vas a gustar a [mc]."
        call BlinkXS4("c28s004_535") from _call_BlinkXS4_222
        if emm._var("route") and eva._var("route"):
            lis "¿Qué llevasteis puesto vosotras en vuestra primera cita con él?"
        elif emm._var("route") or eva._var("route"):
            lis "¿Qué llevaste puesto tú en tu primera cita con él?"
        else:
            lis "Es que no sé qué ponerme, y [deb.nick] no es de mucha ayuda..."
        if emm._var("route"):
            call BlinkXS4("c28s004_540") from _call_BlinkXS4_223
            emm "Yo fui con shorts y camiseta, y me puse la lencería en el bosque."
            emm "No hemos tenido una cita 'normal'. No podía esperar a tenerla y pasamos de los besos a la cama."
        if eva._var("route"):
            call BlinkXS4("c28s004_545") from _call_BlinkXS4_224
            eva "Yo fui con el traje de misión negro. Es el que uso para ir en moto. Allí me puse unos shorts y una camiseta que me prestó [dap]."
            eva "Debajo llevaba un sujetador y unas bragas monos, pero no en plan lencería sexy... Aunque a él le pareció sexy..."
            eva "Lo mío no lo considerarías una cita normal, pero para mí fue la mejor que pude tener."
    call BlinkXS4("c28s004_550") from _call_BlinkXS4_225
    eva "Haz una cosa, reduce esos 42 vestidos a cinco y pruébatelos. Te daremos nuestra opinión sincera sobre cual te queda mejor."
    if lis._var("route"):
        eva "Espero que no tengas 40 tipos de lencería distinta..."
    call BlinkXS4("c28s004_555") from _call_BlinkXS4_226
    emm "*Risa* De todas formas, si ninguno va a ser rosa, ninguno te quedará perfecto."
    emm "Y por mucho que me gustara tu estilo Jackie, no pega con la 'nueva tú' para ir a una fiesta."
    call BlinkXS4("c28s004_560") from _call_BlinkXS4_227
    lis "Parece una buena idea... pero reducir a solo cinco va a ser complicado..."
    lis "Aunque si el estilo Jackie no lo puedo usar, quedan muchos menos. Principalmente vestidos que no me he puesto nunca."
    call BlinkXS4("c28s004_565") from _call_BlinkXS4_228
    emm "Tengo una idea aún mejor. Elige seis. Y no nos enseñes el que tú prefieres ponerte."
    emm "Si lo que te digamos sobre los otros cinco no te hacen dudar, ponte ese."
    emm "Es como cuando tomas una decisión tirando una moneda. En el momento en que la moneda empieza a volar, ya sabes lo que quieres que salga."
    call BlinkXS4("c28s004_570") from _call_BlinkXS4_229
    eva "¿Tomas decisiones tirando una moneda? ¿No sopesas los pros y los contras de las diversas opciones?"
    call BlinkXS4("c28s004_575") from _call_BlinkXS4_230
    emm "Sólo a veces..."
    call BlinkXS4("c28s004_580") from _call_BlinkXS4_231
    if persistent.family:
        eva "*Risa* Creo que en el laboratorio se equivocaron de alguna forma muy extraña y tu clon soy yo en vez de [ama]."
    else:
        eva "*Risa* Creo que en el laboratorio se equivocaron de alguna forma muy extraña y tú eres un clon mío en vez de ser el de [ama]."
    eva "[ama] nunca haría eso, pero nunca le he visto nada malo a lo de la moneda."
    todas "*Risa*"
    call BlinkXS4("c28s004_585") from _call_BlinkXS4_232
    lis "Voy a empezar a probarme los vestidos o no acabaremos nunca. ¡Son cinco vestidos!"
    lis "Ya he decidido cuál será el sexto que no os enseñaré. Creo que le pega a la 'nueva [lis]'."
    lis "Voy a probarme el primero..."
    scene c28s004_590d with fade:
        yalign 1.0
        linear 5.0 yalign 0.0
    pause (4.8)
    call BlinkXS3("c28s004_590") from _call_BlinkXS3_770
    lis "¿Qué os parece este?"
    call BlinkXS4("c28s004_595a") from _call_BlinkXS4_233
    eva "Me gusta. Es muy atrevido, teniendo en cuenta que no vas a poder llevar ropa interior con él."
    call BlinkXS4("c28s004_595b") from _call_BlinkXS4_234
    emm "A mí me gusta, pero creo que pegaría más si fuerais a un club en vez de a una fiesta en una casa."
    emm "*Risa* Además te vas a tener que estar bajando el vestido toda la noche si no quieres enseñar tus tesoros."
    call BlinkXS4("c28s004_600") from _call_BlinkXS4_235
    lis "Descartado. Vamos a por el siguiente."
    scene c28s004_605d with fade:
        yalign 1.0
        linear 5.0 yalign 0.0
    pause (4.8)
    call BlinkXS3("c28s004_605") from _call_BlinkXS3_771
    lis "A este le pasa lo mismo, ¿no?"
    scene c28s004_605e with dissolve
    eva "*Risa* Sí, y además pareces un limón."
    if lis._var("route"):
        eva "*Risa* No necesitas eso para que [mc] te exprima."
    emm "*Risa* [eva] tiene razón. El corte es muy bonito, pero el color no te pega nada."
    call BlinkXS4("c28s004_610") from _call_BlinkXS4_236
    lis "Es lo que he pensado siempre que me lo he querido poner. En blanco sería mucho más bonito. Me equivoqué al comprarlo en este color."
    lis "Descartado. Sólo quedan tres."
    scene c28s004_615d with fade:
        yalign 1.0
        linear 5.0 yalign 0.0
    pause (4.8)
    call BlinkXS3("c28s004_615") from _call_BlinkXS3_772
    lis "Este me gusta mucho, pero..."
    call BlinkXS4("c28s004_620") from _call_BlinkXS4_237
    emm "¿Qué hemos dicho del estilo Jackie? Vas a una fiesta, no a una gala."
    emm "Pero esa chaquetilla te la voy a robar algún día. *Risa*" #bolero
    call BlinkXS4("c28s004_625") from _call_BlinkXS4_238
    eva "[emm] tiene razón. Aunque es bonito, se ve antiguo y no vas a poder bailar con eso puesto."
    call BlinkXS4("c28s004_630") from _call_BlinkXS4_239
    lis "Otro descartado..."
    scene c28s004_635d with fade:
        yalign 1.0
        linear 5.0 yalign 0.0
    pause (4.8)
    call BlinkXS3("c28s004_635") from _call_BlinkXS3_773
    lis "El top me gusta, pero el conjunto lo encuentro un poco soso..."
    call BlinkXS4("c28s004_640") from _call_BlinkXS4_240
    emm "El top me gusta tanto que te lo voy a coger prestado algún día."
    emm "Pero la falda no te pega a menos que vayas a ir a bailar salsa."
    call BlinkXS4("c28s004_645") from _call_BlinkXS4_241
    eva "No estoy de acuerdo con [emm]. A mí me gusta el conjunto. Y el color te pega mucho."
    call BlinkXS4("c28s004_650") from _call_BlinkXS4_242
    lis "Por fin hemos encontrado un candidato. Al menos el top. Vamos a por el último."
    scene c28s004_655d with fade:
        yalign 1.0
        linear 5.0 yalign 0.0
    pause (4.8)
    call BlinkXS3("c28s004_655") from _call_BlinkXS3_774
    lis "Este es el último... Me gusta, aunque el color no demasiado. No sé si me acaba de convencer..."
    lis "Es más sexy que los últimos dos."
    scene c28s004_660a with dissolve
    emm "Si quieres ir de secretaria sexy está genial."
    eva "A mí me parece muy chulo. Te realza las curvas en los sitios correctos."
    emm "*Risa* Por eso he dicho lo de secretaria sexy. Para mí es el mejor."
    call BlinkXS4("c28s004_665") from _call_BlinkXS4_243
    lis "¿Entonces os gusta o no?"
    scene c28s004_660b with dissolve
    eva "A mí me gusta mucho. De todos los que has enseñado, yo elegiría este."
    emm "Yo también. Es moderno, es sexy, y te queda genial. Los tíos van a tener problemas para apartar la mirada de ti."
    if lis._var("route"):
        call BlinkXS4("c28s004_670") from _call_BlinkXS4_244
        lis "El único tío que quiero que me mire es tu hermano."
        call BlinkXS4("c28s004_675") from _call_BlinkXS4_245
        emm "Pues no vas a tener ningún problema con eso. Se va a quedar embobado."
    call BlinkXS4("c28s004_680") from _call_BlinkXS4_246
    lis "Entonces este es el que debería competir con el que había elegido yo."
    call BlinkXS4("c28s004_685") from _call_BlinkXS4_247
    eva "¿Te hemos hecho dudar con los comentarios? ¿Este ha desbancado al que tú querías?"
    call BlinkXS4("c28s004_690") from _call_BlinkXS4_248
    lis "No. *Risa* Ha sido como lo de la moneda que habéis dicho antes."
    lis "Esperaba que le encontrarais pegas a todos los vestidos que me he probado."
    scene c28s004_660c with dissolve
    eva "¿Entonces por qué te los has probado?"
    emm "[eva], ¿conoces a alguna mujer a la que no le guste probarse cosas? [ama] y tú no contáis."
    call BlinkXS4("c28s004_695") from _call_BlinkXS4_249
    eva "*Risa* ¡A mí me gusta probarme ropa! Soy casi una chica normal."
    todas "*Risa*"
    scene black with dissolve
    "Las chicas pasan un rato ayudando a [lis] a recoger los vestidos."
    if lis._var("route"):
        "Con la lencería es mucho más fácil. [lis] no quiere ofender a [emm], y usará la que le compró en Monterey. No hay show con la lencería."
        "Además, le queda genial, con lo que no tiene dudas en este caso. La única duda que tiene es sobre el color. Cree que [emm] no acertó."
        "[emm] le dice que no la tenían en el color que ella cree que le hubiera pegado más."
        "Decide buscar el mismo modelo por internet en el color que ella prefiere."
    stop music fadeout (1.5)
    return
label c28s005_GavCall:
    if _in_replay:
        call mrS3_lis_route from _call_mrS3_lis_route_15
    call BlinkXS4 ("c28s005_200") from _call_BlinkXS4_250
    "La llamada con Aaron se desarrolla con normalidad. Un montón de datos sobre operaciones en curso, suministros, y un montón de otras pequeñeces."
    play music ("music/SneakySnitch.ogg")
    "Empiezas a pensar que la decisión de Aaron de dar un paso al lado cuando llegues a Aruba va a ser buena."
    "Su visión de la empresa todavía es la de un operativo de campo, con lo que le da demasiada importancia a las misiones."
    "Incluso sabiendo que esa parte de la empresa va a desaparecer."
    "Ahora mismo, la empresa está en un impasse. Se mantiene por inercia y por los temas que ya estaban en marcha antes de la Guerra Clon."
    "Pero nadie se atreve a dar un paso adelante en ninguna dirección."
    "Vas a tener que buscar un puesto en el que Aaron pueda ser productivo y relevante."
    "Cuando por fin habéis tratado todas las pequeñeces..."
    mc "Creo que, con eso, ya está todo, ¿no?"
    aar "De lo que queríamos tratar hoy, sí."
    mc "¿Hay algún otro tema?"
    call BlinkXS4 ("c28s005_205") from _call_BlinkXS4_251
    aar "Hay alguien que quiere hablar contigo. Creo que deberías escucharle."
    mc "¿Quién?"
    call BlinkXS4 ("c28s005_210") from _call_BlinkXS4_252
    aar "Gavin. Hoy los médicos le han dejado salir de la base por primera vez y hemos estado hablando."
    aar "Bueno, llevamos varios días hablando. No lo conocía demasiado, pero es buen chico."
    mc "¿Cuándo habéis estado paseando por la playa?"
    call BlinkXS4 ("c28s005_215") from _call_BlinkXS4_253
    call version28 from _call_version28_12
    aar "¿Tienes a gente espiándome? ¿No te fías de mí?"
    mc "No, Aaron. No es mi estilo. Alguien nos ha mandado una foto desde Aruba y te he visto."
    mc "Para ser más exactos, he descubierto que era Aruba porque tú salías en la foto."
    call BlinkXS4 ("c28s005_220") from _call_BlinkXS4_254
    aar "Disculpa, supongo que es la costumbre de desconfiar de todo el mundo."
    mc "No te preocupes. No sabía que con quien paseabas fuera Gavin... Únicamente sabía que era un G."
    mc "Aunque ahora que sé que es el, me doy cuenta de que había notado algo raro en sus brazos... como si le faltara uno."
    call BlinkXS4 ("c28s005_230") from _call_BlinkXS4_255
    aar "Bueno, distinguir a los clones es difícil. *Risa* A veces me cuesta incluso a mí."
    aar "Supongo que va en lo de ser clones."
    mc "El otro día [eva] intentó disfrazarse de [dap] y las distinguí perfectamente."
    mc "Para mí es fácil con ellas. Las veo todos los días."
    call BlinkXS4 ("c28s005_225") from _call_BlinkXS4_256
    aar "Supongo que, con el tiempo, acabarás distinguiendo al resto de series. Pero lleva tiempo, especialmente con gente con la que no has tratado mucho."
    aar "¿Le puedo decir a Gavin que pase?"
    stop music fadeout (1.5)
    mc "Sí, sí, por supuesto."
    scene c28s005_235a with fade
    call BlinkXS4 ("c28s005_235") from _call_BlinkXS4_257
    $ gav = TGCharacter ("Gavin", color = "#669300", lname = "Gates")
    play music ("music/WarIsComing.ogg")
    gav "Buenas tardes, Señor."
    mc "Buenas tardes, Gavin. Llámame [mc]. ¿De qué querías hablar conmigo?"
    mc "¿Cómo estás del... brazo?"
    call BlinkXS4 ("c28s005_240") from _call_BlinkXS4_258
    gav "El brazo... o la queda de él... va bien, de momento."
    gav "Los médicos me empiezan a dejar hacer vida normal. Esperan que en menos de un mes pueda volver a los entrenamientos."
    gav "Dependiendo de cómo vaya la próxima operación, claro."
    mc "¿No es demasiado pronto?"
    call BlinkXS4 ("c28s005_245") from _call_BlinkXS4_259
    gav "No debería serlo. Pero debo mantener el brazo izquierdo y las piernas en forma."
    mc "Bueno, los médicos saben mucho más de eso que yo."
    mc "Pero supongo que no querías hablar conmigo de tu herida."
    call BlinkXS4 ("c28s005_250") from _call_BlinkXS4_260
    gav "No, Señor. Sólo quería pedirle disculpas a usted y a su familia por lo que pasó aquel día."
    gav "Yo sólo cumplía órdenes. Ninguno sabíamos las implicaciones de lo que estábamos haciendo allí, excepto Eric."
    mc "Lo entiendo."
    call BlinkXS4 ("c28s005_255") from _call_BlinkXS4_261
    gav "No, Señor. No lo entiende. Fuimos engañados. Eric nos dijo que ustedes eran una amenaza para NTR."
    gav "Tan sólo defendíamos a nuestra familia. Nuestro hogar."
    call BlinkXS4 ("c28s005_260") from _call_BlinkXS4_262
    gav "Hasta que Aaron nos explicó todo lo que había pasado y lo que estaba en juego no comprendimos lo engañados que estuvimos."
    gav "Por suerte, en nuestra operación no murió nadie, pero..."
    mc "Pero tú perdiste un brazo. Debe ser duro..."
    call BlinkXS4 ("c28s005_265") from _call_BlinkXS4_263
    gav "No me refiero a eso. En la otra operación..."
    mc "En la que murieron Beatrice, Clarice, y Diana..." id c28s005_GavCall_427e14bf
    call BlinkXS4 ("c28s005_270") from _call_BlinkXS4_264
    gav "Exacto. Frederic está en una depresión constante desde que se enteró de que no tenía que haber muerto nadie."
    gav "Ellos estaban igual de engañados por Enzo que nosotros por Eric."
    mc "No tenéis por qué sentiros culpables. Como dices, os engañaron."
    call BlinkXS4 ("c28s005_275") from _call_BlinkXS4_265
    gav "Pero es algo que no podemos evitar, Señor. Por eso le pido disculpas. Principalmente en mi nombre, pero también en nombre de todos los que participamos."
    mc "Aunque no sea necesario, disculpas aceptadas."
    call BlinkXS4 ("c28s005_280") from _call_BlinkXS4_266
    gav "También querría pedirle que, si la operación va bien, me permita ser útil a su familia."
    mc "¿A qué te refieres?"
    call BlinkXS4 ("c28s005_285") from _call_BlinkXS4_267
    gav "Aaron me ha dicho que [ama] y [eva] se turnarán entre aquí y protegiendo a su familia, Señor."
    gav "Si todo va bien, me gustaría ir con [ama] cuando ella vuelva a Newport. No puede estar despierta las 24 horas y..."
    mc "Para, para. ¿Quieres convertirte en el guardaespaldas de mi familia?"
    call BlinkXS4 ("c28s005_290") from _call_BlinkXS4_268
    gav "Sí, Señor. Es una forma de compensarles por lo que me Eric me obligó a hacer."
    mc "Gavin, creo que es demasiado pronto para tomar esa decisión. Debería hablarlo con [ama] y [eva] y..."
    call BlinkXS4 ("c28s005_295") from _call_BlinkXS4_269
    gav "Incluso, si la operación no sale bien, podría monitorizar las cámaras desde la base y..."
    mc "Gavin, [ama] y [eva] tienen poder de decisión sobre eso."
    call BlinkXS4 ("c28s005_300") from _call_BlinkXS4_270
    gav "Pero Aaron nos dijo que podríamos dedicarnos a lo que quisiéramos cuando se acaben los contratos pendientes..."
    mc "Y es cierto, pero..."
    gav "Pues yo quiero dedicarme a asegurarme de que nadie más ataca a su familia. Creo que se lo debo..."
    gav "Creo que se lo debemos a [ama] y a [eva]."
    mcp "(Cuesta estar hablando con él y recordar que tiene la edad mental de un adolescente.)"
    mcp "(Se siente culpable y está sobrerreaccionando.)"
    mc "Hablaré con ellas, no te preocupes."
    call BlinkXS4 ("c28s005_305") from _call_BlinkXS4_271
    gav "Gracias, Señor."
    "En ese momento te das cuenta de que ha estado llamándote 'Señor' toda la conversación."
    mcp "(Supongo que algunas costumbres pueden tardar en cambiar.)"
    gav "Solo era eso, Señor. Muchas gracias, Señor. No quiero entretenerle más, Señor."
    stop music fadeout (1.5)
    scene c28s005_305d with dissolve
    "Y con eso desaparece de la pantalla."
    scene c28s005_310a with fade
    call BlinkXS4 ("c28s005_310") from _call_BlinkXS4_272
    play music ("music/SneakySnitch.ogg")
    aar "Es un poco... vehemente. Pero es buen chico."
    mc "No lo pongo en duda, pero eso ha sido casi una trampa, Aaron."
    call BlinkXS4 ("c28s005_315") from _call_BlinkXS4_273
    aar "No te has comprometido a nada, sólo a hablar con [ama] y [eva]."
    aar "Esa era mi idea. Si se lo propongo yo por video conferencia se van a sentir mal. Casi obligadas a aceptar."
    aar "Si se lo dices tú en persona..."
    mc "Entiendo. Hablaré con ellas. Pero la próxima vez, avísame de qué va esto."
    scene c28s005_320a with dissolve
    aar "*Risa* Señor. Sí, Señor."
    scene c28s005_320b with dissolve
    mcp "(Será cabrón. *Risa* ¡Ha colgado!)"
    mcp "(También debo recordar que Aaron no tiene una edad mental de 60 y pico de años...)"
    mcp "(Tengo que hablar con las chicas. Creo que [eva] especialmente estará interesada, dependiendo de los plazos.)"
    mcp "(Si Gavin puede volver aquí con [ama], [eva] evitaría verlo hasta después de su primera rotación en Aruba.)"
    mcp "(Voy a beber algo en la cocina mientras maduro la idea.)"
    stop music fadeout (1.5)
    scene c28s005_320c with fade
    play music ("music/SadSummer.ogg")
    "Cuando pasas por la planta de las estudiantes ves a [eva] y [emm]."
    emm "¡Esos vestidos son una pasada! Lástima del color y de que algunos no eran adecuados para una fiesta."
    eva "Le quedan muy bien, y tiene muy buen gusto. Incluso para el color."
    mc "Hola, chicas. ¿Qué hacéis aquí?" id c28s005_GavCall_8661b425
    if lis._var("route"):
        scene c28s005_320d with dissolve
        emm "Estábamos ayudando a [lis] a elegir..."
        eva "¡Hush, [emm]!"
        mc "¿A elegir vestidos para la fiesta de esta noche?"
        scene c28s005_320e with dissolve
        emm "Sí..."
        eva "*Entre dientes* Bocazas... Al menos no has dicho nada de la lencería..."
    else:
        scene c28s005_320f with dissolve
        emm "Estábamos ayudando a [lis] a elegir vestidos."
        eva "Se va a una fiesta a Los Angeles esta noche."
    mc "Está bien que la ayudéis. Espero que no hayas insistido demasiado en que se vista de rosa, [emm]."
    call BlinkXS4 ("c28s005_325") from _call_BlinkXS4_274
    eva "*Risa* Sí que ha insistido, pero [lis] no le ha hecho ni caso. Al menos con el color."
    mc "¿Puedo hablar un rato a solas contigo, [eva]?"
    emm "Yo os dejo para que habléis. Si me quedo seguro que me criticáis por algo."
    call BlinkXS4 ("c28s005_330") from _call_BlinkXS4_275
    eva "¿Conmigo? Sí, por supuesto."
    mc "¿Sabes dónde está [ama]?"
    eva "Ha ido al centro a comprar unas cosas..."
    stop music fadeout (1.5)
    mc "Bueno, ya hablaré con ella más tarde, entonces. Siéntate conmigo y hablemos."
    scene black with dissolve
    return
label c28s005_AmaMad:
    if _in_replay:
        call mrS3_ama_route from _call_mrS3_ama_route_12
        if ama._var("route"):
            call mrS3_mad_route from _call_mrS3_mad_route_13
            if mc._var("relationships")<2:
                call mrS3_rels from _call_mrS3_rels_24
    scene c28s005_350a with dissolve
    play music ("music/RhythmPlay.ogg")
    "Mientras tanto, en la tienda de [mad.nick]..."
    mad "¿Qué es lo que necesitas exactamente?"
    ama "Trajes para ir a la oficina. Si voy a actuar como jefa de seguridad quiero vestirme como una jefa."
    ama "Allí todo el mundo está acostumbrado a verme con ropa de entrenamiento. Así marcaré una diferencia en el rol con la vestimenta."
    call BlinkXS4 ("c28s005_355") from _call_BlinkXS4_276
    mad "Si cambias el aspecto al que están acostumbrados, cambiarás la percepción que tienen de ti. Bien pensado."
    mad "¿Algo más?"
    call version28 from _call_version28_13
    call BlinkXS4 ("c28s005_360") from _call_BlinkXS4_277
    if not ama._var("route"):
        ama "No, nada más. Creo que voy a estar muy ocupada para necesitar algo más."
        scene c28s005_360d with dissolve
        mad "OK. Déjame ver qué tengo para ti."
    else:
        ama "Vestidos. Sexys, a ser posible."
        call BlinkXS4 ("c28s005_365") from _call_BlinkXS4_278
        mad "*Risa* Si vas a tener a [mc] para ti sola durante un mes puede ser que necesites MUCHOS vestidos."
        mad "¿Busco también lencería sexy?"
        call BlinkXS4 ("c28s005_370") from _call_BlinkXS4_279
        ama "Nunca le he encontrado el sentido a la lencería..."
        ama "Supongo que te la pones para impresionar, pero en cuanto te ven debes querer quitártela..."
        call BlinkXS4 ("c28s005_375") from _call_BlinkXS4_280
        mad "*Risa* O que te la quiten."
        mad "Pero a la mayoría de los chicos les gusta."
        if mad._var("route"):
            call BlinkXS4 ("c28s005_380") from _call_BlinkXS4_281
            ama "¿Sabes si a [mc] le gusta? ¿Has usado alguna vez con él? ¿Cuál ha sido su reacción?"
            call BlinkXS4 ("c28s005_385") from _call_BlinkXS4_282
            mad "Sí, le gusta. Sí, he usado. *Risa* ¿Babear?"
        mad "¿Estás nerviosa por ese tiempo que vas a pasar a solas con él?"
        call BlinkXS4 ("c28s005_390") from _call_BlinkXS4_283
        ama "Creo que la palabra nerviosa no llega a describir cómo me siento."
        ama "Quiero hacerlo, pero tengo miedo... Va a ser mi primera vez."
        call BlinkXS4 ("c28s005_395") from _call_BlinkXS4_284
        mad "Ya has oído lo que dicen las chicas. Es súper tierno, especialmente en las primeras veces."
        if mad._var("route"):
            mad "Oyéndolas hablar, me hubiera gustado perder la virginidad con él."
        mad "Creo que no debes preocuparte por nada."
        call BlinkXS4 ("c28s005_400") from _call_BlinkXS4_285
        ama "No me da miedo por él, sino por mí. No sé cómo me voy a sentir... durante o después."
        call BlinkXS4 ("c28s005_405") from _call_BlinkXS4_286
        mad "Mira, [ama]. Mi experiencia dice que la primera vez es una mierda. No sabes qué hacer ni cómo ponerte para estar cómoda."
        mad "Además, estás super nerviosa y da lo mismo que sepas que te tienes que relajar. No puedes hacerlo. Las expectativas son altísimas."
        mad "Y sobre cómo te vas a sentir después, es fácil. Dolorida."
        call BlinkXS4 ("c28s005_410") from _call_BlinkXS4_287
        mad "Pero oyes lo que cuentan las chicas y parece que [mc] tenga una polla mágica que no hace daño."
        if mad._var("route"):
            mad "Que sí, que estoy de acuerdo en que Mjolnir es mágico, pero..."
        mad "Lo mejor que puedes hacer es no crearte expectativas. Vas a estar un mes allí con él."
        mad "Si la primera vez no es tan buena como esperabas, seguro que alguna de las otras 29 lo serán. Posiblemente la segunda o la tercera."
        call BlinkXS4 ("c28s005_415") from _call_BlinkXS4_288
        ama "*Risa* Lo dices como si fuéramos a hacerlo todos los días..."
        ama "Eso sería casi como si fuera adicta al sexo, ¿no?"
        call BlinkXS4 ("c28s005_420") from _call_BlinkXS4_289
        mad "*Risa* ¿Eso es lo que te preocupa? No, mi niña. Eso sería lo más normal."
        if mad._var("route"):
            mad "¿Un mes a solas con nuestro novio sin tener que compartirlo con nadie? ¿Dónde tengo que firmar?"
        elif mc._var("relationships")>1:
            mad "¿Un mes a solas con tu novio sin tener que compartirlo con el resto del harén? Si yo fuera tú, firmaría ahora mismo."
        else:
            mad "¿Un mes a solas con tu novio con el que estás empezando? Si yo fuera tú, firmaría ahora mismo."
        mad "Quizás no todos los días, porque tendrás que descansar uno o dos días después de la primera vez, pero después..."
        call BlinkXS4 ("c28s005_425") from _call_BlinkXS4_290
        ama "Me quitas un peso de encima... creía que... no sé... tengo tantas cosas que aprender..."
        call BlinkXS4 ("c28s005_430") from _call_BlinkXS4_291
        mad "Tendrás tiempo para aprender lo que necesites. Y ya conoces a [mc]. Tiene mucha paciencia con todo."
        mad "Yo no tengo tanta paciencia, con lo que lo primero que vas a aprender es qué vestidos te gustan."
        scene c28s005_360d with dissolve
        mad "Voy a coger algunos trajes para que te los pruebes mientras busco vestidos que puedan ir con tu estilo." id c28s005_AmaMad_34fabdeb
        call BlinkXS4 ("c28s005_435") from _call_BlinkXS4_292
        ama "*Risita* Y no te olvides de la lencería..."
        if mad._var("route"):
            ama "Y, cuando acabemos, me gustaría hablar de tu idea sobre los anillos..."
    scene black with dissolve
    "[ama] acabó comprando mucho más de lo que esperaba. También pasa mucho más tiempo en la tienda de [mad.nick] del que tenía pensado."
    "Los trajes para la oficina van a ser una sorpresa para quién ha visto a [ama] sólo con ropa militar."
    stop music fadeout (1.5)
    if ama._var("route"):
        "Los vestidos y la lencería van a ser una bonita sorpresa para alguien durante el primer mes en Aruba."
    return
label c28s006_Kim:
    if _in_replay:
        call mrS3_kim_route from _call_mrS3_kim_route_6
        call mrS3_lis_route from _call_mrS3_lis_route_16
    scene black with dissolve
    "Después de la llamada a traición con Aaron, sigues leyendo los nuevos documentos que te ha enviado al acabar la reunión."
    play music ("music/thinking-of-you.ogg")
    "Hace calor y te quitas la camiseta mientras lees. No quieres poner el aire acondicionado para el poco rato que vas a estar leyendo."
    "¿Te está empezando a influenciar [lis] con su concepto del ahorro energético?"
    scene c28s006_005a with dissolve
    "Cuando acabas de leer el último informe del día..."
    play sound ("music/knock.ogg")
    "*Knock-Knock*"
    kim "*A través de la puerta* Soy yo, ¿puedo pasar?"
    mc "Sí, pasa, [kim]."
    call BlinkXS4 ("c28s006_010") from _call_BlinkXS4_293
    mc "Hola, [kim], ¿te puedo ayudar en algo?"
    if kim._var("route"):
        call c28s006_KimLewd from _call_c28s006_KimLewd
    else:
        call c28s006_KimOnKate from _call_c28s006_KimOnKate
    return
label c28s006_KimOnKate:
    if kim._var("route"):
        call BlinkXS4 ("c28s006_710") from _call_BlinkXS4_294
    kim "Ayer me preguntaste si a [kat] le pasa algo desde vuestra no-cita."
    kim "¿Aún lo quieres saber?"
    if oma._var("route") and eil._var("route") and sai._var("route"):
        mc "Por supuesto. Ayer [sai] dijo algo que me sorprendió y he estado atando algunos cabos, pero necesito confirmación antes decidir que paso dar."
    else:
        mc "Por supuesto. Últimamente he estado atando algunos cabos, pero necesito confirmación antes decidir que paso dar."
    if not kim._var("route"):
        call BlinkXS4 ("c28s006_015") from _call_BlinkXS4_295
    else:
        call BlinkXS4 ("c28s006_715") from _call_BlinkXS4_296
    kim "*Risa* Es una posición muy cómoda para ti. No te arriesgas..."
    mc "[kat] es una chica compleja y lo que menos querría es que nuestra amistad sufriera porque yo he malinterpretado las señales."
    mc "Y sabiendo su relación pasada con algunos tipos, lo que menos querría sería hacerle daño de alguna manera por estar equivocado."
    if not kim._var("route"):
        call BlinkXS4 ("c28s006_020") from _call_BlinkXS4_297
    else:
        call BlinkXS4 ("c28s006_720") from _call_BlinkXS4_298
    kim "A veces olvido lo considerado que eres."
    kim "La mayoría de los hombres que conozco intentarían follarse a una mujer tan guapa como [kat] sin pensar en sus sentimientos."
    kim "Tú intentas saber cuáles son esos sentimientos antes de hacer nada. Muy encomiable por tu parte."
    mc "Hacer daño a alguien gratuitamente es una de las cosas que más odio."
    if not kim._var("route"):
        call BlinkXS4 ("c28s006_025") from _call_BlinkXS4_299
    else:
        call BlinkXS4 ("c28s006_725") from _call_BlinkXS4_300
    kim "Lo entiendo."
    kim "[kat] está en una encrucijada emocional ahora mismo. Se ha pasado años construyendo un castillo anti-hombres alrededor de sus sentimientos."
    kim "Y has llegado tú y has abierto una brecha en las murallas con gestos amables y tratándola como si fuera una chica normal."
    mc "Es una chica normal..."
    if not kim._var("route"):
        call BlinkXS4 ("c28s006_030") from _call_BlinkXS4_301
    else:
        call BlinkXS4 ("c28s006_730") from _call_BlinkXS4_302
    kim "Ella no es normal; es especial. Detrás de ese sentido del humor caustico hay una chica muy sensible."
    kim "Ha usado ese sentido del humor para protegerse. Forma parte de su castillo."
    kim "Y llegas tú como un ariete y derrumbas esas fortificaciones. Un ariete mucho más sutil que los que usa [emm], pero no por ello menos efectivo."
    mc "Pero yo no tenía intención de..."
    if not kim._var("route"):
        call BlinkXS4 ("c28s006_035") from _call_BlinkXS4_303
    else:
        call BlinkXS4 ("c28s006_735") from _call_BlinkXS4_304
    kim "Da lo mismo cuáles fueran tus intenciones, [mc]. Le has demostrado a [kat] que no todos los hombres son unos capullos."
    kim "Le has enseñado que hay hombres sensibles que tienen en consideración los sentimientos de los demás. Y esta conversación es un ejemplo de ello."
    mc "¿Qué crees que debería hacer?"
    if not kim._var("route"):
        call BlinkXS4 ("c28s006_040") from _call_BlinkXS4_305
    else:
        call BlinkXS4 ("c28s006_740") from _call_BlinkXS4_306
    kim "*Risa* Lo que más te gusta hacer."
    if kim._var("route"):
        kim "*Risa* Y no me refiero a lo que acabamos de hacer nosotros. Habla con ella."
    else:
        kim "Habla con ella."
    if not kim._var("route"):
        call BlinkXS4 ("c28s006_045") from _call_BlinkXS4_307
    else:
        call BlinkXS4 ("c28s006_745") from _call_BlinkXS4_308
    kim "No importa si quieres tener algo romántico con ella o no. Pero tienes que hablar con ella."
    kim "Ella lleva todo el día cabizbaja y pensativa. Creo que la ventana de oportunidad se está cerrando para que lo arregléis."
    if lis._var("route"):
        mc "Hablaré con ella mañana, cuando vuelva de la fiesta de [lis]."
    else:
        mc "Hablaré con ella mañana cuando tenga la oportunidad."
    if not kim._var("route"):
        call BlinkXS4 ("c28s006_050a") from _call_BlinkXS4_309
    else:
        call BlinkXS4 ("c28s006_750") from _call_BlinkXS4_310
    kim "¿Qué parte de que la ventana de oportunidad se está cerrando no has entendido?"
    kim "Mañana a lo mejor es tarde, si le dejas reconstruir sus muros."
    kim "Cuando he venido aquí, ella bajaba a la piscina y no había ninguna otra chica allí. Deberías ir a hablar con ella. Ahora mejor que mañana."
    if not kim._var("route"):
        mc "Me parece una buena idea. Voy a ir a hablar con ella. Gracias, [kim]."
        call BlinkXS4 ("c28s006_050b") from _call_BlinkXS4_311
    else:
        mc "¿No te importa?"
        call BlinkXS4 ("c28s006_755") from _call_BlinkXS4_312
        kim "Al contrario. Estoy deseando que se resuelva esta situación."
        kim "[kat] no es la misma desde vuestra no-cita y quiero que vuelva a ser la que era antes. Deberías ir cuanto antes."
        if persistent.lesbian:
            call BlinkXS4 ("c28s006_760") from _call_BlinkXS4_313
            kim "Además..."
            mc "¿En qué estás pensando?"
            kim "Sé que suena un poco raro decirte esto después de acostarnos juntos por primera vez..."
            mc "No lo sé. Aún no me has dicho nada."
            call BlinkXS4 ("c28s006_765") from _call_BlinkXS4_314
            kim "Si decidieras que [kat] entrara en el harén y ella quisiera... me gustaría que... pero sólo si los dos queréis..."
            mc "[kim], suéltalo ya, estás balbuceando."
            call BlinkXS4 ("c28s006_770") from _call_BlinkXS4_315
            kim "Si los dos quisierais, me gustaría que tuviéramos un trío algún día."
            kim "Me gusta [kat]. La considero super atractiva, aunque no tenga sentimientos por ella más allá de la amistad. Y siempre he querido probar el sexo con otra chica."
            kim "No me considero lesbiana ni bisexual, pero tengo curiosidad por probarlo y sé que ella tiene experiencia y se siente atraída por mí..."
            mc "Con lo que no hay mejor candidata. Lo entiendo. Pero creo que es muy pronto para hablar de eso."
            mc "Aún no sabemos qué pasará cuando hable con ella."
            call BlinkXS4 ("c28s006_775") from _call_BlinkXS4_316
            kim "Lo sé, pero quería que supieras que me apetecería probarlo algún día si los dos estáis de acuerdo y ella entra en el harén."
            kim "Y no vamos a saber qué pasará cuando hables con ella si sigues aquí sentado."
        mc "*Risa* ¿Me estás echando?"
        call BlinkXS4 ("c28s006_780") from _call_BlinkXS4_317
        kim "No, pero no quieres que a alguna otra chica se le ocurra bajar a la piscina antes de que hables con [kat]."
        kim "Además, yo necesito un rato para recuperarme de lo que acabamos de hacer."
        if lis._var("route"):
            kim "Y no tienes mucho tiempo antes de que te tengas que empezar a preparar para la fiesta de [lis]."
        mc "Tienes razón. Voy a ir a hablar con ella. Gracias, [kim]."
        call KissXS4 ("c28s006_785") from _call_KissXS4_3
        call BlinkXS4 ("c28s006_785") from _call_BlinkXS4_318
    mc "Te veo luego."
    stop music fadeout (1.5)
    kim "Hasta luego."
    return
label c28s006_noKimLewd:
    if _in_replay:
        call mrS3_lis_route from _call_mrS3_lis_route_17
    scene c28s006_1000 with fade
    if lis._var("route"):
        "Al volver a tu habitación después de ducharte, te vistes y decides jugar a My Residence para matar el rato hasta que tengas que bajar a buscar a [lis]."
    else:
        "Al volver a tu habitación después de ducharte, te vistes y decides jugar a My Residence para matar el rato."
    "Tienes una tierna escena con Meg, la actriz con vitiligo que tanto te recuerda a [kim], en la que ella pierde la virginidad."
    "Tu harén va creciendo en el juego. Viendo lo bonita que ha sido la escena Meg, te planteas si hubiera sido una buena idea empezar una relación con [kim]."
    "Decides que no lo es. Si lo hubiera sido, ya lo hubieras hecho cuando tuviste la oportunidad."
    return
label c28s006_KimLewd:
    kim "Venía a hablar de lo de mañana. Se me ha ocurrido una idea..."
    mc "¿Ya has encontrado un sitio para ir a comer?"
    call BlinkXS4 ("c28s006_055") from _call_BlinkXS4_319
    kim "Bueno... Hablando con [sam] y con [mar] me han dado una idea, no ha sido mérito mío."
    kim "Les he dicho que quería hacer algo relajado para pasar tiempo contigo a solas y..."
    mc "Y [sam] te ha sugerido un picnic, ¿verdad?"
    call BlinkXS4 ("c28s006_060") from _call_BlinkXS4_320
    kim "¿Cómo lo sabes?"
    mc "*Risa* A [sam] le encantan los picnics. Íbamos mucho de pequeños a hacer picnics al parque, cuando ella tenía una tarde libre."
    mc "Para ella era algo relajado, con todas las chicas corriendo por allí, haciendo carreras que siempre ganaba [sim], para enfado de [emm]."
    mc "Jamaal y yo hacíamos alguna travesura cuando [sam] no miraba. Era difícil ser sigilosos con la silla de Jam."
    call BlinkXS4 ("c28s006_065") from _call_BlinkXS4_321
    kim "Algo me han contado sobre esos picnics. Y, por lo que me han dicho, no hacíais tantas travesuras como piensas."
    kim "Pero sí, [sam] los guarda en un buen recuerdo. Solo había que verle la cara de felicidad mientras lo explicaba."
    kim "¿Te apetece que vayamos de picnic? [mar] ha dicho que nos prepararía algo para comer."
    mc "Si consiste en pasar tiempo contigo, me da lo mismo si es un picnic o un restaurante con tres estrellas Michelon."
    mc "De lo que tengo ganas es de pasar tiempo a solas contigo."
    call BlinkXS4 ("c28s006_070") from _call_BlinkXS4_322
    kim "Entonces es un picnic. Me apetece mucho. Hace siglos que no voy de picnic, y tengo ganas de ir contigo."
    mc "Entonces está decidido."
    call BlinkXS4 ("c28s006_075") from _call_BlinkXS4_323
    kim "Hablando de pasar tiempo juntos... ¿tienes algo que hacer ahora mismo?"
    mc "Acabo de terminar de leer unos informes, con lo que estoy libre."
    if lis._var("route"):
        mc "Al menos hasta que tenga que ir a buscar a [lis] para ir a la fiesta de su amiga."
    mc "¿Quieres que hagamos algo?"
    call BlinkXS4 ("c28s006_080") from _call_BlinkXS4_324
    kim "Pues sí, me gustaría un beso y unos abrazos de mi novio..."
    mc "Sabes que no es necesario que los pidas, ¿verdad? *Risa* Puedes besarme cuando quieras sin mi permiso."
    scene c28s006_085a with dissolve
    "Dudosa al principio, sin saber dónde puede llevar ese beso, posa sus labios sobre los tuyos."
    "Sabe a colutorio, lo cual, varias horas después de comer, te demuestra que venía preparada para este beso."
    scene c28s006_085b with dissolve
    "Su boca se entreabre para dar la bienvenida a tu lengua. Espera que tú vayas dando los pasos una vez ella ha iniciado el beso."
    "La falta de experiencia de la modelo se nota en cada uno de sus movimientos."
    "Nunca ha sido una gran besadora. Apasionada, pero no hábil. Pero hoy está especialmente rígida."
    call BlinkXS4 ("c28s006_090") from _call_BlinkXS4_325
    kim "Ahora quiero mi abrazo..."
    mc "No tienes ni por qué pedirlo. Me encanta abrazarte."
    call BlinkXS4 ("c28s006_095") from _call_BlinkXS4_326
    kim "Pero no aquí..."
    mc "¿Dónde lo quieres, entonces?"
    call BlinkXS4 ("c28s006_100") from _call_BlinkXS4_327
    kim "Quiero que me abraces en la cama. Túmbate. Será casi como un adelanto del picnic."
    mc "¿Estás segura? Es muy fácil que unos abrazos en la cama se nos vayan de las manos..."
    call BlinkXS4 ("c28s006_105a") from _call_BlinkXS4_328
    kim "Si sigues preguntando, quizás me entren dudas. Ahora mismo no las tengo."
    kim "Pero si no quieres..."
    mc "Por supuesto que quiero. Ya estuvimos en una cama en el barco."
    call BlinkXS4 ("c28s006_105b") from _call_BlinkXS4_329
    kim "Por eso no tengo dudas. Sé que eres capaz de contenerte. Túmbate."
    scene c28s006_110a with fade
    call BlinkXS4 ("c28s006_110") from _call_BlinkXS4_330
    mc "¿No vienes?"
    kim "Sí, pero verte ahí, sin camiseta..."
    stop music fadeout (1.5)
    mc "¿Quieres que me ponga una?"
    scene c28s006_115d with dissolve
    pause (1.5)
    call BlinkXS4 ("c28s006_115") from _call_BlinkXS4_331
    play music ("music/Salsa.ogg")
    kim "Creo que será mejor si yo me quito mi camisa, ¿no?"
    kim "Al fin y al cabo, ya me viste en topless..."
    mc "Eso va a hacer que sea más difícil contenerme, pero me encanta hacia dónde va esto."
    call BlinkXS4 ("c28s006_120") from _call_BlinkXS4_332
    kim "Esto sólo va hacia unos abrazos en una cama, [mc]."
    mc "Me encantan los abrazos en la cama."
    kim "Hazme un hueco."
    scene c28s006_120d with fade
    kim "Se está bien aquí..."
    mc "La cama es muy cómoda..."
    kim "No me refiero a eso..."
    mc "Lo sé."
    call BlinkXS4 ("c28s006_125") from _call_BlinkXS4_333
    kim "No sé cómo hacer esto..."
    mc "¿Ser abrazada? Yo diría que se te da bien. *Risa*"
    call BlinkXS4 ("c28s006_130") from _call_BlinkXS4_334
    kim "*Risa* No me lo estás poniendo fácil."
    mc "*Risa* Te pongo muy fácil abrazarme. Yo estoy quieto."
    call BlinkXS4 ("c28s006_135") from _call_BlinkXS4_335
    kim "¿Cómo lo hiciste con las otras chicas?"
    mc "Es muy sencillo..."
    scene c28s006_140a with dissolve
    mc "Pasé un brazo por aquí..."
    scene c28s006_140b with dissolve
    mc "El otro por aquí..."
    scene c28s006_140c with dissolve
    mc "Se estira de la otra persona para acercarla a mí y..."
    mc "Abrazo completado. ¿Ves? ¿Es fácil? ¿No os enseñan en Ohio a abrazar desde pequeños?"
    call BlinkXS4 ("c28s006_145") from _call_BlinkXS4_336
    kim "*Risa* ¿Me estás tomando el pelo?"
    mc "*Risa* Supongo que sí, porque supongo que no te refieres a dar y recibir abrazos."
    mc "Pero has dicho que esto sólo iba hacia unos abrazos en la cama."
    call BlinkXS4 ("c28s006_150") from _call_BlinkXS4_337
    kim "Me he asustado cuando me he quitado la camisa..."
    mc "No tienes por qué asustarte, [kim]. La primera vez puede dar un poco de miedo, pero es normal."
    mc "*Risa* Aunque no es el primer abrazo que te doy..."
    scene c28s006_150d with dissolve
    mc "Vale, ya paro..."
    call BlinkXS4 ("c28s006_155") from _call_BlinkXS4_338
    kim "No es eso lo que me daba miedo. Las chicas me han dicho que eres muy tierno."
    mc "Entonces no entiendo de qué te has asustado."
    call BlinkXS4 ("c28s006_160") from _call_BlinkXS4_339
    kim "Me ha dado la impresión de que me estaba comportando... como si fuera una guarrilla."
    kim "No quiero que pienses que... soy así."
    mc "Cielo, sólo te has quitado la camisa. No creo que pueda pensar nada malo de ello."
    call BlinkXS4 ("c28s006_170") from _call_BlinkXS4_340
    kim "Si no me hubiera asustado, me habría quitado los shorts... y las bragas..."
    mc "¿Creías que si te desnudabas pensaría que eres una guarrilla?"
    kim "Sí..."
    mc "¿Y qué pensarías tú si hubiera sido yo quién te hubiera quitado los shorts y las bragas?"
    call BlinkXS4 ("c28s006_165") from _call_BlinkXS4_341
    kim "Pensaría que eres el hombre con experiencia y que estás tomando la iniciativa..."
    mc "¿Pero? Se puede oír el 'pero' al final de esa frase."
    kim "Pero seguiría sin saber cómo pasamos de estar abrazados a... al sexo..."
    stop music fadeout (1.5)
    mc "No hay una forma correcta o incorrecta de hacerlo. Pero a mí me gusta empezar así..."
    scene c28s006_175a with dissolve
    play music ("music/SexyLoungeMusic.ogg")
    "La tumbas sobre su espalda y empiezas a besarla, tiernamente al principio para hacerla sentir cómoda con la idea de desnudarse completamente delante de ti por primera vez."
    "Sigue igual de rígida, si no más, que la primera vez que te ha besado, hace unos minutos."
    scene c28s006_175b with dissolve
    "Intentas que el beso sea dinámico cambiando de posición."
    "No quieres que sienta que la estás besando, sino que os estáis besando mutuamente."
    scene c28s006_175c with dissolve
    "Poco a poco, los nervios desaparecen mientras aparece la piel de gallina."
    "Paso a paso, va perdiendo la rigidez, sintiéndose más cómoda con vuestros besos."
    scene c28s006_175d with dissolve
    "Al cabo de unos minutos, el beso es tan apasionado como cualquiera que hayas dado en tu vida."
    "La modelo no se ha convertido en una gran besadora en esos minutos, pero está perdiendo el miedo al mismo ritmo que la respiración."
    call BlinkXS4 ("c28s006_180") from _call_BlinkXS4_342
    "Aún no tiene controlado lo de besar y respirar al mismo tiempo."
    kim "*Jadeo* Creo que lo estoy entendiendo... Y que ya estoy preparada..."
    mc "¿Para quitarte los shorts?"
    call BlinkXS4 ("c28s006_185") from _call_BlinkXS4_343
    kim "*Jadeo* Para que me los quites tú. Pero sólo si podemos seguir con los besos después..."
    mc "Creo que es algo que podemos hacer tanto rato como quieras."
    kim "*Jadeo* Pero primero quiero que tú te quites tus shorts."
    mc "*Risa* ¿Sólo los shorts?"
    call BlinkXS4 ("c28s006_190") from _call_BlinkXS4_344
    kim "*Risa* ¿Siempre intentas ser tan gracioso cuando una chica te pide que te desnudes?"
    mc "*Risa* Depende del día y de la chica."
    kim "*Risa* Pues menos bromear y más desnudarse."
    scene c28s006_195a with fade
    call BlinkXS4 ("c28s006_195") from _call_BlinkXS4_345
    mc "¿Me los quito ya?"
    kim "Estoy esperando..."
    scene c28s006_200a with dissolve
    pause (1.5)
    scene c28s006_200b with dissolve
    pause (1.5)
    scene c28s006_200c with hpunch
    kim "¿Qué? ¡Esa cosa es enorme!"
    mc "*Risa* No lo llames 'Esa cosa' si no quieres que se ofenda."
    call BlinkXS4 ("c28s006_205") from _call_BlinkXS4_346
    kim "A ver... sé cómo funciona la anatomía femenina y... sé que va a caber... pero da miedo..."
    mc "*Risa* Sabe hacer una cosa para quitar el miedo."
    kim "¿Va a encogerse?"
    scene c28s006_895pv with dissolve
    show c28s006_895v
    mc "*Risa* No, pero sabe imitar a un helicóptero."
    kim "*Risa* No quita el miedo, pero es gracioso. Creía que sería más rígido, más duro."
    mc "*Risa* Si estuviera duro del todo no podría hacer el helicóptero. Cuando crezca más lo verás."
    scene c28s006_210a with hpunch
    call BlinkXS4 ("c28s006_210") from _call_BlinkXS4_347
    kim "¿Qué? ¿Va a crecer más?"
    mc "En cuanto te quite los pantalones. Me extraña que no esté en orden de batalla, a lo mejor me has contagiado los nervios."
    call BlinkXS4 ("c28s006_215") from _call_BlinkXS4_348
    kim "Pues creo que es un buen momento para que me los quites. Estoy ardiendo ahí abajo desde los besos."
    mc "Acércate..."
    scene c28s006_220a with fade
    call BlinkXS4 ("c28s006_220") from _call_BlinkXS4_349
    mc "¿Puedo?"
    kim "Hazlo antes de que pierda el valor."
    scene c28s006_220d with dissolve
    pause (1.2)
    scene c28s006_220e with dissolve
    mc "¿Ves? Ahora es como si fueras en bikini y en topless. No hay nada que temer."
    kim "*Risa* Excepto lo que tienes entre las piernas."
    mc "*Risa* Tampoco le tienes que tener miedo. Por cierto, preciosas braguitas."
    call BlinkXS4 ("c28s006_225") from _call_BlinkXS4_350
    kim "No sabía dónde íbamos a llegar o si me iba a quitar los shorts... No quería venir con bragas de abuela..."
    kim "Hay que vestirse para la ocasión, ¿no?"
    mc "Y es aún mejor desvestirse para la ocasión."
    scene c28s006_220f with dissolve
    pause (1.2)
    scene c28s006_220g with dissolve
    kim "Pues ya estamos los dos desnudos..."
    call BlinkXS4 ("c28s006_230") from _call_BlinkXS4_351
    kim "¿Cómo continúa esto? ¿Vas a...?"
    mc "Voy a continuar donde lo hemos dejado. Me gustaría seguir besándote."
    mcp "(Y que estés menos tensa en el proceso.)"
    kim "Me parece una buena idea..."
    scene c28s006_930pv with fade
    show c28s006_930v
    hide c28s006_895v
    "Te tumbas sobre ella y empiezas a besarla. Vuelve a estar rígida como una estatua. Una preciosa estatua que los antiguos griegos envidiarían." id c28s006_KimLewd_5cd65604
    "No sabes si la pausa para desnudaros ha hecho que pierda el momento en el que estaba tan solo hace unos minutos."
    "O posiblemente se ha dado cuenta de que la ventana de oportunidad para echarse atrás se está cerrando y le están entrando dudas."
    call BlinkXS4 ("c28s006_235") from _call_BlinkXS4_352
    mc "¿Estás bien, [kim]?"
    kim "Me siento... rara... Tengo ganas de que pase, pero... también tengo miedo de no saber qué hacer."
    mc "No te preocupes por eso. Verás que es más sencillo de lo que parece. Tu cuerpo sabrá qué hacer si te relajas y le dejas tomar el control."
    mc "Túmbate boca abajo."
    scene c28s006_235d with hpunch
    kim "¿Qué? ¿Quieres empezar por detrás?"
    mc "*Risa* No, pero voy a intentar ayudar a que te relajes."
    scene c28s006_235e with fade
    kim "¿Así estoy bien? ¿Qué vas a hacer?"
    mc "Lo descubrirás en un momento."
    scene c28s006_935pv with fade
    show c28s006_935v
    hide c28s006_930v
    "Empiezas a repartir caricias y besos por su espalda, de una forma tierna y suave. Intentas que sea más relajante que sensual. Tan solo un suave roce de tus dedos en su espalda."
    kim "Eso es muy agradable..."
    "Tu intento de que no sea sensual es un completo fracaso. Con tu polla entre sus cachetes, la chica aprieta su culo contra ti."
    kim "Y eso también es muy agradable..."
    "Puedes notar cómo la preciosa modelo está perdiendo sus inhibiciones cada segundo que tus manos acarician su espalda."
    mc "¿Te sientes más relajada?"
    call BlinkXS4 ("c28s006_240") from _call_BlinkXS4_353
    kim "Mucho más. Ahora es el momento de que tú te tumbes boca arriba."
    mc "Se pone interesante... ¿Qué vas a hacer?"
    kim "Lo descubrirás en un momento. *Risita*"
    mc "Empiezas a devolvérmelas. *Risa* Creo que ese es un síntoma de que estás más confortable."
    scene c28s006_245a with fade
    call BlinkXS4 ("c28s006_245") from _call_BlinkXS4_354
    mc "¿Así estoy bien?"
    kim "*Risa* ¿Así es cómo sueno yo cuando lo pregunto?"
    mc "*Risa* Suenas mucho más sexy. Todo suena más sexy con tus palabras saliendo de entre esos hermosos labios."
    call BlinkXS4 ("c28s006_250") from _call_BlinkXS4_355
    kim "Sabes que no hace falta que me conquistes a estas alturas, ¿verdad?"
    mc "Voy a intentar conquistarte todos los días, cielo. El día que deje de intentarlo, no te mereceré."
    scene c28s006_940pv with fade
    show c28s006_940v
    hide c28s006_935v
    "La chica se monta encima de tus piernas y empieza a rozar su cuerpo contra el tuyo, atrapando a Mjolnir entre vosotros."
    kim "No creo que te sea demasiado difícil si sigues así..."
    "Sus labios se acercan a los tuyos lo suficiente como para que puedas notar un leve contacto que ella rompe juguetonamente antes de que se convierta en un beso de verdad."
    mc "*Risa* ¿Esto es algún tipo de castigo?"
    kim "He oído que provocar es algo bueno, ¿no te gusta?"
    "La línea entre provocar y calientapollas es delgada y se tiene que recorrer con cuidado."
    scene c28s006_945pv with dissolve
    show c28s006_945v
    hide c28s006_940v
    "Pero parece que [kim] sabe recorrerla. Retuerce su cuerpo cada vez que se acerca y se aleja de tus labios para acariciar a Mjolnir entre sus duras y suaves tetas."
    mc "Me encanta..."
    kim "*Gemido* Pero esto me está empezando a poner muy cachonda..."
    "Cada vez que sus labios se acercan a los tuyos, cuando presiona a Mjolnir entre vuestros estómagos, se le escapa un pequeño gemido."
    kim "*Gemido* Creo que es el momento del siguiente paso... Estoy empezando a arder ahí abajo..."
    "No podrías estar más de acuerdo con esta chica. El leve contacto de tu polla contra su piel te está volviendo loco."
    scene c28s006_255aa with hpunch
    "La giras de espaldas a la cama y la besas. Tus labios no soportan más los leves contactos y necesitan sentir los suyos."
    "Perdido todo reparo, la estudiante te devuelve el beso con su torpeza habitual, pero con mucha más pasión que hace unos minutos."
    stop music fadeout (1.5)
    "Parece que llevar la iniciativa en el juego ha hecho que haya perdido el miedo."
    scene c28s006_255aAn with dissolve
    play music ("music/You-Know-Instrumental.ogg")
    "Sin prácticamente dejarle pensar, decides dar el siguiente paso, recorriendo el mapa de su piel hasta el destino justo por encima de su entrepierna."
    "Podrías perderte en su perfecta piel incluso teniendo un mapa a tu disposición."
    if not kim._var ("makeup"):
        "Nunca entenderás por qué en algún momento de su vida quiso esconder la belleza de sus manchas con maquillaje. No lo volverá a hacer nunca."
    else:
        "Una vez estuviste equivocado sobre su intención de esconder la belleza de sus manchas. No lo volverás a estar, ni ella volverá a querer taparla con maquillaje."
    kim "*Gemido* Se me está poniendo la piel de gallina..."
    "Lo puedes notar bajo tus dedos, bajo tus labios. Los diminutos montículos que revelan excitación han hecho su aparición por todo su cuerpo."
    scene c28s006_915pv with dissolve
    show c28s006_915v
    hide c28s006_945v
    "Vuelves a actuar sin dejarle pensar. Introduces tu cabeza entre sus maravillosos muslos y empiezas a lamer su centro de placer."
    kim "*GEMIDO* ¿QUÉ? *JADEO*"
    "Deberá hacer algo más que gemir si quiere decirte que pares. No lo hace."
    kim "*JADEO* ¡OH! *GEMIDO*"
    "Está incluso más húmeda de lo que podrías haber imaginado después de tanto beso y tanta provocación."
    scene c28s006_925pv with dissolve
    show c28s006_925v
    hide c28s006_915v
    "Saber que estás donde ningún hombre ha estado antes tiene un componente excitante."
    "Saber que vas a introducirla en el maravilloso mundo del sexo es incomparable."
    kim "*GEMIDO* ASÍ... *JADEO*"
    "No sabes si [kim] es mujer de pocas palabras o es que lo que está sintiendo la está abrumando."
    "Prefieres seguir lamiendo y descubrirlo más tarde."
    kim "*JADEO* ¿YA? *GEMIDO*"
    call OrgasmXS4 ("c28s006_255b") from _call_OrgasmXS4_16
    kim "*GEMIDO* ¡SÍ! *JADEO* ¡SIGUE! *GEMIDO*"
    "Las señales habituales no se han producido y su orgasmo te ha pillado por sorpresa."
    "No ha habido un incremento gradual de la tensión en su cuerpo. En un momento dado estaba relajada y un segundo después explotaba en tu boca."
    scene c28s006_920pv with dissolve
    show c28s006_920v
    hide c28s006_925v
    "Una maravillosa explosión de sabores que disfrutas profundamente, sabiendo que es su primer orgasmo producido por otra persona en su centro de placer."
    "Sigues lamiendo cada curva y cada pliegue de su coño para prolongar el clímax lo máximo posible."
    kim "*JADEO* ¡OOOFFF! *GEMIDO*"
    "El orgasmo se dilata en el tiempo sin ser seguido por otros en la habitual oleada a la que estás acostumbrado."
    "Sólo puedes notar un orgasmo, pero es largo y poderoso, recorriendo su cuerpo de arriba a abajo."
    kim "*GEMIDO* ¡PARA, [mc!u]! *JADEO* ¡POR FAVOR! *GEMIDO*"
    kim "*JADEO* ¡NO PUEDO CONTINUAR MÁS ASÍ! *GEMIDO*"
    call BlinkXS4 ("c28s006_260") from _call_BlinkXS4_356
    mc "¿Quieres que paremos?"
    kim "*Gemido* Quiero sentirte dentro. *Jadeo*"
    kim "*Jadeo* Después de tantos orgasmos... *Gemido* No creo que esté más preparada nunca. *Jadeo*"
    call BlinkXS4 ("c28s006_265") from _call_BlinkXS4_357
    kim "¿He dicho algo malo?"
    "Tu cara debe reflejar tu perplejidad. Jurarías que sólo ha tenido un orgasmo. Pero no es el momento de hablar de ello."
    "Estarías jurando en falso, aunque sólo fuera por desconocimiento de cómo funciona el cuerpo de la modelo."
    mc "No, nada."
    mc "Entonces, ¿quieres que sigamos?"
    scene c28s006_270a with fade
    call BlinkXS4 ("c28s006_270") from _call_BlinkXS4_358
    kim "Ven a mí..."
    "Difícil rechazar la propuesta. Pocas veces te han dado una orden que hayas cumplido tan a gusto."
    scene c28s006_275a with fade
    "Te sitúas entre sus piernas, con Mjolnir apoyado en la entrada de su coño, presionando contra sus labios."
    mc "¿Preparada?"
    kim "Sí... Ve con cuidado, por favor..."
    stop music fadeout (1.5)
    mc "Lo intentaré."
    scene c28s006_275An1 with dissolve
    play music ("music/UnforeseenMotive.ogg")
    "Introduces la punta de Mjolnir con toda la suavidad de la que eres capaz."
    kim "*JADEO* ¡OOOFFF! *JADEO*"
    "El coño de [kim] es extremadamente estrecho. Tu glande se encuentra agradablemente aprisionado en su interior."
    call BlinkXS4 ("c28s006_280") from _call_BlinkXS4_359
    mc "¿Estás bien?"
    kim "Es un poco molesto, pero menos de lo que esperaba. Además, Mjolnir ha entrado en seguida."
    kim "Supongo que estar tan húmeda ha ayudado. ¿Cómo lo notas tú?"
    mc "Muy estrecho. De momento sólo está dentro la punta y..."
    scene c28s006_280d with hpunch
    kim "¿Qué? ¿Solo la punta?"
    mc "He dicho que intentaría ir con cuidado. Meter todo Mjolnir de golpe sería lo contrario de ir con cuidado."
    call BlinkXS4 ("c28s006_285") from _call_BlinkXS4_360
    kim "Tienes razón...."
    kim "¿Puedes entrar un poco más?"
    mc "Voy a hacerlo, pero si notas alguna incomodidad, dímelo. Y, sobre todo, intenta relajarte. Cuanto más te relajes, menos dolerá."
    kim "Lo intentaré."
    scene c28s006_275An2 with dissolve
    "La penetras un poco más, lentamente, hasta que notas con la punta de la polla una resistencia que te indica que has llegado al himen."
    kim "Eso es un poco más molesto..."
    mc "Estoy tocando tu himen. Es el momento de parar si no estás segura. Una vez roto..."
    call BlinkXS4 ("c28s006_290") from _call_BlinkXS4_361
    kim "Lo sé. Una vez roto ya no seré virgen. Pero no quiero parar."
    kim "Puedes continuar."
    scene c28s006_275An3 with dissolve
    "Esta vez no le das consejos. Tiene que pasar por este momento en sus condiciones y no puedes aconsejarle nada que no le hayas dicho antes."
    "Notas cómo su himen se rompe en silencio, pero lo que sientes en tu polla es como un 'pop' atronador."
    scene c28s006_290d with hpunch
    kim "*JADEO* ¡AARGH! *JADEO* ¡PARA, POR FAVOR! *JADEO*"
    "Parece que las lágrimas están a punto de hacer su aparición en sus ojos. Te sientes mal por ella."
    kim "*JADEO* ¡ESO HA DOLIDO MUCHO MÁS DE LO QUE ESPERABA! *JADEO*"
    mc "Lo siento... Intenta relajarte..."
    call BlinkXS4 ("c28s006_295") from _call_BlinkXS4_362
    kim "*JADEO* ¿QUÉ TE CREES QUE INTENTO? *JADEO* ¡Pero no es fácil! *JADEO*"
    kim "*JADEO* ¡Siento como si me hubieran dado una puñalada con un cuchillo ardiendo! *Jadeo*"
    "Sus jadeos empiezan a bajar de volumen y ha dejado de gritarte. Al menos no te grita tan fuerte..."
    mc "Más que un cuchillo, ha sido un martillo..."
    "Quizás no sea el mejor momento para una broma, pero no has podido resistirte."
    scene c28s006_295d with dissolve
    "Estás seguro de que la has cagado. Su mirada te dice que te podías haber ahorrado la broma."
    call BlinkXS4 ("c28s006_300") from _call_BlinkXS4_363
    kim "*Risa* ¡Te odio! *Jadeo* Me duele todo y tú estás haciendo bromas."
    kim "*Risa* ¡Ouch! *Jadeo* Y si me río me duele más. *Risa* Y te odio aún más por hacerme reír."
    mc "*Risa* Pues deja de reírte."
    call BlinkXS4 ("c28s006_305") from _call_BlinkXS4_364
    kim "*Risa contenida* Verte la cara de preocupación cuando has dicho lo del martillo..."
    mc "Es que me he dado cuenta de que quizás no era lo idóneo en el momento en que lo he dicho."
    mc "¿Duele mucho?"
    call BlinkXS4 ("c28s006_310") from _call_BlinkXS4_365
    kim "Ha dolido mucho. Pero ahora se está empezando a pasar. Creo que la risa ha hecho que... me relaje. Sí, ya sé que lo tenía que haber hecho antes."
    mc "Podemos esperar a que desaparezca del todo el dolor. Aunque volverá, pero menos intenso."
    kim "Creo que puedes empezar a moverte sin que desee matarte. Pero hazlo despacio, por favor."
    scene c28s006_965pv with dissolve
    show c28s006_965v
    hide c28s006_920v
    stop music fadeout (1.5)
    "Empiezas a mover tus caderas, a una velocidad lenta, atento a las reacciones de [kim]."
    play music ("music/SexyLoungeMusic.ogg")
    mc "¿Va bien a este ritmo? ¿Duele mucho?"
    kim "*Jadeo* Aún duele un poco... *Jadeo* Pero el ritmo me gusta... *Jadeo*"
    "Aún no han aparecido los gemidos, pero las expresiones de dolor han desaparecido casi por completo."
    kim "*Jadeo* ¿Siempre duele tanto? *Jadeo*"
    mc "Depende de cada chica, pero hablemos de eso después. Concéntrate en relajarte."
    "Sabes que la curiosidad es normal en estos momentos, pero cuanto menos piense en el dolor y más se relaje, antes empezará a disfrutarlo."
    scene c28s006_970pv with dissolve
    show c28s006_970v
    hide c28s006_965v
    "Tú también empiezas a concentrarte en tus sensaciones. El coño de [kim] es tan estrecho como te había parecido en un primer momento."
    "Abraza toda la longitud de tu astil en cada una de tus lentas y profundas embestidas. Llegas al fondo del túnel del amor, rozando la boca de su útero."
    kim "*Jadeo* Se está empezando a pasar el dolor... *Jadeo*"
    "La chica se está empezando a relajar por fin y eso hace que empiece a sentir otras cosas aparte del dolor."
    "Pero no por ello el interior de su vagina se siente menos estrecho."
    scene c28s006_975pv with dissolve
    show c28s006_975v
    hide c28s006_970v
    kim "*Jadeo* El dolor se está empezando a convertir... *Gemido* en algo placentero... *Jadeo*"
    "Aparece el primer gemido."
    "Su cara empieza a reflejar el cambio de dolor por placer. Está mucho más relajada y está recogiendo los frutos de seguir tus consejos."
    "Estás seguro de que el resto de las chicas también le han dado consejos sobre este momento, pero tiene que ser complicado seguirlos mientras el dolor te atenaza."
    kim "*Gemido* Se está convirtiendo en algo bueno... *Jadeo* Realmente bueno... *Gemido*"
    "Puedes notar cómo empieza a usar su suelo pélvico, incrementando la presión sobre tu astil. Ha recuperado el control lo suficiente como para recordar los consejos."
    kim "*Jadeo* Puedes aumentar el ritmo... *Gemido* Me está empezando a gustar... *Jadeo*"
    scene c28s006_900pv with dissolve
    show c28s006_900v
    hide c28s006_975v
    "Intentas subir el ritmo y mantenerte atento a sus cambios de expresión por si el dolor reaparece."
    kim "*GEMIDO* ¡Sí! *JADEO* ¡Así es mejor! *GEMIDO*"
    "Es complicado retenerte cuando su húmedo coño aprieta tu polla como un puño de acero en un guante de terciopelo durante unos segundos antes de liberar la presión."
    "El dolor parece haber desaparecido por completo. O al menos haber sido superado por el placer."
    kim "*JADEO* ¡Sigue así! *GEMIDO*"
    scene c28s006_905pv with dissolve
    show c28s006_905v
    hide c28s006_900v
    "Piensas seguir así durante un rato. La interrupción debido a su dolor ha hecho que tu excitación baje un poco, con lo que aún te queda un rato para correrte."
    "¿Dónde querrá que te corras? No habéis hablado de hijos ni de si está usando algún método anticonceptivo, aunque no tendría lógica que lo hiciera."
    kim "*GEMIDO* ¡OH, DIOS MÍO! *JADEO* ¡Esto es mejor de lo que podía esperar! *GEMIDO*"
    "La tensión producida por el miedo ha sido sustituida por la tensión provocada por el placer. Un cambio bienvenido."
    "Ahora, por fin, está empezando a disfrutar y a descubrir que el sexo también puede ser placentero. Debe ser placentero."
    scene c28s006_910pv with dissolve
    show c28s006_910v
    hide c28s006_905v
    kim "*JADEO* ¿TE QUEDA MUCHO PARA LLEGAR? *GEMIDO* YO CASI ESTOY AHÍ. *JADEO*"
    mc "Sí, aún me queda. Pero no te preocupes. Déjalo fluir."
    "Casi te da un poco de pena que vuestra primera vez juntos los orgasmos no sean simultáneos. Pero es algo que muchas parejas no consiguen nunca."
    "Su coño se tensa alrededor de tu polla como no lo había hecho antes. Ahora descubres que las señales que anuncian su orgasmo son más internas de lo normal en [kim]."
    kim "*JADEO* ¡NO VOY A PODER ESPERARTE! *GEMIDO* ¡ESTÁ LLEGANDO! *JADEO*"
    mc "Córrete para mí, preciosa."
    scene c28s006_315An with hpunch
    kim "*GEMIDO* ¡ME CORROOOO! *JADEO* ¡OH, SÍ! *GEMIDO*"
    "La preciosa estudiante se incorpora para acabar su primera oleada de orgasmos con un beso, gimiendo en tu boca."
    "Su coño se cierra con fuerza... con más fuerza aún... sobre tu polla, intentando ordeñarte incluso antes de que te corras."
    scene c28s006_950pv with dissolve
    show c28s006_950v
    hide c28s006_910v
    "Sigues bombeando con tus caderas, embistiendo con Mjolnir en el profundo y estrecho pozo de placer en el que se ha convertido la estudiante."
    "Sincronizas tus movimientos para que tus labios se queden a unos milímetros de los suyos. La venganza por la provocación de antes es dulce."
    kim "*GEMIDO* ¡TE ODIO! *JADEO RISUEÑO* ¡TE QUIERO! *GEMIDO*"
    "Ha entendido perfectamente lo que estás haciendo y se siente en el lado malo de la broma ahora mismo, buscando tus labios sin éxito."
    "El efecto queda un poco paliado por los orgasmos que recorren su cuerpo."
    scene c28s006_955pv with dissolve
    show c28s006_955v
    hide c28s006_950v
    kim "*JADEO RISUEÑO* ¿Vamos a empezar con las venganzas en nuestra primera vez juntos? *GEMIDO RISUEÑO*"
    "La musicalidad de su risa mientras gime resuena en la habitación. Vas a amar ese sonido el resto de su vida."
    mc "*Risa* Has empezado tú..."
    "Vuestra primera vez juntos marcará el resto de vuestra relación. Estará repleta de bromas, risas, y provocaciones. Será adorable."
    kim "*GEMIDO RISUEÑO* La venganza puede ser un camino de dos direcciones. *JADEO RISUEÑO*"
    scene c28s006_960pv with dissolve
    show c28s006_960v
    hide c28s006_955v
    "Pero su risa, unida a las oleadas que recorren sus paredes vaginales y masajean tu polla, están a punto de llevarte al orgasmo."
    mc "[kim], estoy a punto de llegar..."
    "Siendo vuestra primera vez juntos, quieres que la experiencia sea completa, pero también quieres su autorización."
    kim "*JADEO* ¡Córrete dentro! *GEMIDO* ¡Por favor! *JADEO*"
    "Lo hubieras hecho sin el 'por favor', aunque hubiera sonado como una orden. Te parece suficiente luz verde como para dejarte ir."
    $ kim._var ("chancePregnant", True)
    if persistent.pregnancy:
        if persistent.walkthrough:
            $ wt1 = _("[kim] embarazada.")
            $ wt2 = _("Sin consecuencias.")
        else:
            $ wt1 = ""
            $ wt2 = ""
        menu:
            "Correrte dentro. Ir a por el bebé." (wt = wt1):
                $ kim._var("pregnant", True)
                $ kim._var("undiscoveredPregnancy", True)
                play sound ("music/OldMusicBox5.ogg")
            "Correrte dentro." (wt = wt2):
                pass
    $ resetWalkthrough ()
    scene c28s006_320An with hpunch
    mc "¡Mpfft!"
    "Después de toda la excitación, los juegos, y las provocaciones, descargas una ingente cantidad de semen en el coño de [kim]."
    "Ella aprovecha el momento en que te quedas inmóvil debido a tu orgasmo para lanzarse a tus labios, colgándose de tu cuello."
    kim "*GEMIDO*"
    "Imposible seguir embistiendo cuando estás atrapado por su brazo, por su coño, y por sus labios."
    "Os quedáis inmóviles unos preciosos momentos, en los que su coño masajea tu astil, exprimiendo hasta la última gota."
    "Es imposible que una chica sepa, en su primera vez, lo increíble que es esa sensación. Alguien le ha tenido que dar consejos sobre eso."
    scene c28s006_325a with fade
    call BlinkXS4 ("c28s006_325") from _call_BlinkXS4_366
    stop music fadeout (1.5)
    "Cuando vuestros orgasmos llegan a su fin os sentáis en la cama, con la chica apoyada sobre tu pecho, mientras la abrazas por detrás."
    play music ("music/pianomatic.ogg")
    "El larguísimo clímax de [kim] ha hecho que, al final, sí que sean simultáneos."
    kim "*Jadeo* ¿Qué tal lo he hecho?"
    mc "Depende. ¿Te ha gustado?"
    call BlinkXS4 ("c28s006_330") from _call_BlinkXS4_367
    kim "¡Me ha encantado!... Pese al dolor..."
    mc "Entonces lo has hecho muy bien."
    call BlinkXS4 ("c28s006_335") from _call_BlinkXS4_368
    kim "¿Me estás diciendo que sólo depende de si a mí me ha gustado? ¿Qué hay de ti?"
    mc "Yo he disfrutado de cada segundo de ello. Bueno, excepto cuando el dolor ha sido insoportable para ti."
    mc "Pero por mucho que a mí me haya gustado, si tú no lo hubieras disfrutado significaría que algo hemos... he... hecho mal."
    call BlinkXS4 ("c28s006_340") from _call_BlinkXS4_369
    "Se desentiende de tu abrazo para enfrentarse a ti cara a cara."
    kim "Entiendo lo que quieres decir. Pero no estoy de acuerdo."
    kim "Si lo hemos hecho juntos y algo hubiera salido mal, lo hubiéramos hecho mal los dos, no tú."
    kim "Y no me sirve que me digas que no me puedes cargar con la responsabilidad en mi primera vez."
    mc "Es que no te puedo cargar con la responsabilidad en tu primera vez."
    mc "Pero como a ambos nos ha gustado, no hay que darle más vueltas."
    mc "¿Cómo va el dolor?"
    call BlinkXS4 ("c28s006_345") from _call_BlinkXS4_370
    kim "Una vez los orgasmos han acabado, está volviendo a doler un poco..."
    kim "Pero es muy soportable. Me he hecho más daño muchas veces... cayéndome."
    mc "Espera. ¿Has dicho orgasmos? Me había parecido que tan sólo era uno. Uno muy largo, pero uno."
    call BlinkXS4 ("c28s006_350") from _call_BlinkXS4_371
    kim "*Risa* ¿Uno? Mientras me comías he dejado de contar al llegar a una docena."
    kim "Y mientras teníamos sexo ni siquiera he empezado a contar. Han llegado demasiado seguidos uno detrás del otro."
    mc "*Risa* Creo que tengo que revisar mi sentido arácnido. Hubiera jurado que habías tenido uno cada vez."
    mc "Supongo que tengo que aprender las señales que tu cuerpo manda."
    call BlinkXS4 ("c28s006_355") from _call_BlinkXS4_372
    kim "Vas a tener muchas oportunidades de aprender. Y yo quiero aprenderlo todo sobre tu cuerpo también."
    mc "Siempre me gustó ir a clase, y más aún los proyectos en grupo."
    mc "*Risa* Estoy seguro de que disfrutaré más aprendiendo sobre tu cuerpo que haciendo trabajos con Jamaal."
    call BlinkXS4 ("c28s006_360") from _call_BlinkXS4_373
    kim "*Risa* Eso espero. Pero las lecciones tendrán que esperar unos días."
    kim "Necesito recuperarme un poco de esto."
    mc "Es normal. Algo se ha roto dentro de ti y tiene que curarse."
    call BlinkXS4 ("c28s006_365") from _call_BlinkXS4_374
    kim "Y hablando de aprender..."
    mc "¿Qué?"
    kim "[kat]."
    mc "¿Qué pasa con [kat]?"
    call c28s006_KimOnKate from _call_c28s006_KimOnKate_1
    return
label c28s002_Kat:
    if _in_replay:
        call mrS3_lis_route from _call_mrS3_lis_route_18
        call mrS3_kim_route from _call_mrS3_kim_route_7
        call mrS3_kat_rps (5, 5, 10) from _call_mrS3_kat_rps_2
    scene black with dissolve
    call notificationS3 (1, kim) from _call_notificationS3_2
    play music ("music/On-The-Rise.ogg")
    if not kim._var("route"):
        "Bajas a la piscina sin ponerte una camiseta, esperando que [kat] aún esté sola en la piscina."
    else:
        "Te limpias, te pones los shorts y bajas a la piscina, esperando que [kat] aún esté sola en la piscina." id c28s002_Kat_39251870
    "Si alguna de las otras chicas está allí, seguramente no tendrás oportunidad de hablar con ella."
    scene c28s002_200d with fade
    "Al llegar a la puerta, ves a [sam] que se dirige a la piscina."
    mc "Hey, [sam]."
    call BlinkXS4 ("c28s002_200") from _call_BlinkXS4_375
    sam "Hola, [mc]. ¿Vas a la piscina? ¿No llevas toalla?"
    mc "Sí y no. Voy a la piscina a ver si puedo hablar con [kat]. [kim] me ha dicho que estaba sola."
    mc "¿Tú también vas a la piscina?"
    call BlinkXS4 ("c28s002_205") from _call_BlinkXS4_376
    sam "Iba a ir con [nor] y [mar], pero creo que las voy a esperar aquí mientras se cambian en vez de en la piscina."
    mc "Es decir, tú también sabes que a [kat] le pasa algo conmigo y no quieres molestar, ¿no?"
    call BlinkXS4 ("c28s002_210") from _call_BlinkXS4_377
    sam "*Risa* Creo que te estás volviendo demasiado listo."
    sam "Ve y soluciona lo que está pasando antes de que baje alguna otra de las chicas."
    mc "Gracias, [sam]."
    scene c28s002_215d with dissolve
    "Al llegar a la piscina, ves que [kat] está sola en el agua. Vas a tener la oportunidad de arreglar las cosas."
    stop music fadeout (1.5)
    mc "Hola, [kat]."
    scene c28s002_215a with hpunch
    call BlinkXS4 ("c28s002_215") from _call_BlinkXS4_378
    play music ("music/OneLastChance.ogg")
    kat "¡Oh! ¡Hola, [mc]!"
    mc "¿Qué haces tan sola en la piscina? ¿Esperas a alguien?"
    call BlinkXS4 ("c28s002_220") from _call_BlinkXS4_379
    kat "No... Había bajado a refrescarme un rato... pero ya me iba..."
    mc "¿Vuelves a esquivarme? No hemos hablado desde la no-cita..."
    scene c28s002_225d with dissolve
    pause (1.5)
    call BlinkXS4 ("c28s002_225") from _call_BlinkXS4_380
    kat "No es que te esté esquivándote, es que me siento un poco estúpida y... Bueno, sí. Te estoy esquivando."
    mc "¿Por qué, [kat]? ¿He hecho algo malo?"
    if kat.rps<5:
        call BlinkXS4 ("c28s002_230") from _call_BlinkXS4_381
        kat "No, [mc]. Tú no has hecho nada malo. He malinterpretado las señales que me daba a mí misma y no quiero hacerte daño."
        mc "¿Hacerme daño? ¿A mí? ¿Por qué?"
        call BlinkXS4 ("c28s002_235") from _call_BlinkXS4_382
        kat "Después de la no-cita... No entendía lo que sentía cuando estaba cerca de ti."
        kat "Por un momento... Por tres o cuatro días, más bien... Incluso antes de la no-cita... He estado dudando de si me estabas empezando a gustar... a nivel romántico."
        mc "Tal como lo dices, parece que has llegado a la conclusión de que no te gusto a ese nivel."
        call BlinkXS4 ("c28s002_240") from _call_BlinkXS4_383
        kat "Exacto. He descubierto que lo que estaba sintiendo es que puedo confiar en ti y estar confortable a tu lado, pero no hay nada romántico."
        kat "No estoy acostumbrada a sentirme así cerca de un tío, y... No sé... Lo estaba confundiendo con otra cosa."
        mc "Y por eso me estabas esquivando. Necesitabas aclarar tus ideas."
        mc "Pero ¿qué tiene que ver eso con hacerme daño?"
        call BlinkXS4 ("c28s002_245") from _call_BlinkXS4_384
        kat "*Risa* Eres un jodido caballero de la brillante armadura siempre buscando damiselas que salvar."
        mc "*Risa* Me lo han dicho alguna vez. Pero sigo sin entender qué tiene que ver eso con hacerme daño."
        call BlinkXS4 ("c28s002_250") from _call_BlinkXS4_385
        kat "Si no te hubiera estado esquivando estos últimos dos días, seguro que hubieras venido en plan caballero salvador."
        kat "Yo, estando confundida como estaba, seguramente hubiera caído en tus brazos sin remedio y..."
        mc "Y después te hubieras arrepentido. Me hubieras dejado y me hubieras hecho daño."
        call BlinkXS4 ("c28s002_255") from _call_BlinkXS4_386
        kat "Exacto. No quería que pasara eso hasta que descubriera qué sentía por ti."
        kat "Si hubiera descubierto que me gustabas a ese nivel, no hubiera habido otro caballero por el que me hubiera gustado más ser salvada."
        mc "Pero dices que lo has resuelto ya y, pese a todo, me ibas a seguir esquivando. ¿Por qué?"
        call BlinkXS4 ("c28s002_260") from _call_BlinkXS4_387
        kat "Creo que he estado transmitiendo las señales equivocadas. No quería que..."
        mc "¿Que pensara que te habías enamorado de mí y que mi orgullo masculino se viera herido al descubrir que no lo habías hecho?"
        stop music fadeout (1.5)
        mc "No te preocupes, [kat]."
        scene c28s002_265An with dissolve
        "*Splash*"
        play sound ("music/Splash.ogg")
        call BlinkXS4 ("c28s002_270") from _call_BlinkXS4_388
        play music ("music/Vacation-Vibe.ogg")
        kat "¿Qué haces? ¿Por qué te has metido en el agua ahora?"
        mc "Porque creo que este puede ser el principio de una gran amistad."
        scene c28s002_270d with dissolve
        mc "¿Amigos?"
        kat "Siempre va bien tener un amigo que abraza de puta madre."
        kat "El día que una chica me deje, puedo venir a por un abrazo como este."
        mc "*Risa* O el día que una beluga te llame prima."
    else:
        call BlinkXS4 ("c28s002_230") from _call_BlinkXS4_389
        kat "No, [mc], no has hecho nada malo, pero no estoy preparada para esto."
        mc "¿Qué es 'esto'? Si no me lo explicas, no podemos hablarlo. Y si no lo hablamos, no podemos arreglarlo."
        mc "No quiero que estés evitándome hasta que me vaya a Aruba."
        mc "Si lo quieres hacer, tendré que aceptarlo, pero preferiría que no lo hicieras."
        call BlinkXS4 ("c28s002_260") from _call_BlinkXS4_390
        kat "Es que yo tampoco quiero evitarte, pero no sé cómo enfrentar la situación. Esto es nuevo para mí."
        kat "O estaba tan enterrado que es como si lo fuera."
        mc "Sigues sin decirme que es 'esto'."
        call BlinkXS4 ("c28s002_285") from _call_BlinkXS4_391
        kat "No se me da bien hablar de mis sentimientos..."
        mc "A nadie se le da bien. Decimos un montón de tonterías y balbuceamos. Hablar de sentimientos es complicado."
        kat "Y más aún cuando temes hacer el ridículo."
        mc "No vas a hacer el ridículo digas lo que digas."
        call BlinkXS4 ("c28s002_235") from _call_BlinkXS4_392
        kat "Después de la no-cita... No entendía lo que sentía cuando estaba cerca de ti."
        kat "Por un momento... Por tres o cuatro días, más bien... Incluso antes de la no-cita... He estado dudando de si me estabas empezando a gustar... a nivel romántico."
        mc "Tal como lo dices, parece que has llegado a la conclusión de que no te gusto a ese nivel."
        call BlinkXS4 ("c28s002_240") from _call_BlinkXS4_393
        kat "He descubierto que lo que estaba sintiendo es que puedo confiar en ti y estar confortable a tu lado..."
        kat "No estoy acostumbrada a sentirme así cerca de un tío, y... No sé... Creía que lo estaba confundiendo con otra cosa."
        mc "Y por eso me estabas esquivando. Necesitabas aclarar tus ideas."
        mc "Pero podíamos haberlo hablado..."
        call BlinkXS4 ("c28s002_245") from _call_BlinkXS4_394
        kat "*Risa* Eres un jodido caballero de la brillante armadura siempre buscando damiselas que salvar."
        mc "*Risa* Me lo han dicho alguna vez."
        call BlinkXS4 ("c28s002_250") from _call_BlinkXS4_395
        kat "No necesitaba que me salvaran. Necesitaba aclararme."
        kat "Si no te hubiera estado esquivando estos últimos dos días, seguro que hubieras venido en plan caballero salvador."
        kat "Yo, estando confundida como estaba, seguramente hubiera caído en tus brazos sin remedio y..."
        mc "Y después te hubieras arrepentido..."
        call BlinkXS4 ("c28s002_290") from _call_BlinkXS4_396
        kat "¿Has oído hablar del multiverso y los universos paralelos?"
        kat "¿Sabes que, si esa teoría es cierta, hay un universo en el que tenemos esta conversación, pero estamos en un árbol en vez de en una piscina?"
        kat "En uno de esos universos, yo soy una ardilla y tú un loro."
        "El cambio de tema te pilla un poco a traspiés. Sabes que a [kat] no le gusta hablar de sus sentimientos, pero..."
        mc "Sí, claro que he oído hablar de ello. He leído un montón de cómics sobre eso. Pero ¿a qué viene eso?"
        call BlinkXS4 ("c28s002_295") from _call_BlinkXS4_397
        kat "Pues que, en algunos de esos universos paralelos, no soy una ardilla, pero tampoco soy una lesbiana idiota que no sabe lo que quiere."
        kat "Y, en al menos uno de esos universos, tú me estas besando en este mismo momento."
        if persistent.walkthrough:
            $ wt1 = _("Ruta con [kat] abierta.")
            $ wt2 = _("Ruta con [kat] cerrada.")
        else:
            $ wt1 = ""
            $ wt2 = ""
        menu:
            "Besarla." (wt = wt1):
                $ kat._var("route", True)
            "No besarla." (wt = wt2):
                $ kat._var("route", False)
        $ resetWalkthrough ()
        scene c28s002_265An with dissolve
        "*Splash*"
        play sound ("music/Splash.ogg")
        call BlinkXS4 ("c28s002_270") from _call_BlinkXS4_398
        kat "¿Qué haces? ¿Por qué te has metido en el agua ahora?"
        mc "Siento mucho que este no sea ese universo, [kat]."
        call BlinkXS4 ("c28s002_275") from _call_BlinkXS4_399
        kat "¿Ves? No debería haber hablado de esto contigo. Ahora me siento idiota."
        stop music fadeout (1.5)
        if kat._var("route"):
            call c28s002_KatRoute from _call_c28s002_KatRoute
        else:
            call c28s002_noKatRoute from _call_c28s002_noKatRoute
    kat "*Risa* Capullo. Abrázame fuerte y calla."
    if lis._var("route"):
        kat "Al menos hasta que te tengas que ir a cambiar para la cita con [lis]."
    scene black with dissolve
    if kat._var("route"):
        "Alternáis besos y abrazos hasta que [sam], [nor], y [mar] hacen su aparición en la piscina."
    else:
        "Continuáis con los abrazos hasta que [sam], [nor], y [mar] hacen su aparición en la piscina."
    "Os han dejado privacidad para arreglar las cosas, pero ellas también quieren su ración de sol y relax."
    "Su llegada marca el momento de dejarlas solas para que [kat] les explique cómo ha ido." id c28s002_Kat_d7138312
    if lis._var("route"):
        "Vuelves a tu habitación para ducharte y prepararte para ir a buscar a [lis]."
    else:
        "Vuelves a tu habitación y te das una ducha antes de la cena."
    stop music fadeout (1.5)
    call notificationS3 (2, kat) from _call_notificationS3_3
    $ kat._var("chanceRoute" , True)
    return
label c28s002_noKatRoute:
    mc "No debes sentirte idiota. Creo que los dos hemos malinterpretado lo que está pasando."
    play music ("music/Memories-Instrumental.ogg")
    mc "Dices que crees que puedes confiar en mí y estar confortable a mi lado, y que no estás acostumbrada a eso con un tío."
    call BlinkXS4 ("c28s002_335") from _call_BlinkXS4_400
    kat "Es exactamente lo que he dicho..."
    mc "Pero fíjate que en ningún momento has hablado de que te sientas atraída por mí, o que sientas algo por mí aparte de sentirte a gusto a mi lado."
    mc "Esa no es una base para empezar una relación, [kat]. Yo me siento a gusto al lado de Jamaal y confío en él, pero no empezaría una relación con él."
    call BlinkXS4 ("c28s002_300") from _call_BlinkXS4_401
    kat "¿Quieres decir que estoy confundiendo descubrir que eres un buen tío con sentir algo por ti?"
    mc "No soy yo quien tiene que ponerles nombre a tus sentimientos, [kat], pero sé que el tipo aquel en el instituto te hizo daño."
    mc "Y que has evitado a los tíos como a la peste desde entonces."
    mc "Supongo que descubrir que hay un tío que no te va a hacer daño por nada del mundo puede ser confuso."
    call BlinkXS4 ("c28s002_340") from _call_BlinkXS4_402
    kat "Es posible que tengas razón... Ahora que lo dices... nunca me he imaginado formando una familia contigo..."
    mc "Ya hemos formado una familia juntos, [kat]. No es una familia tradicional, pero es una familia."
    kat "Quizás necesito más tiempo para analizar lo que siento desde esa nueva perspectiva..."
    kat "¿Me puedes dar un abrazo?"
    scene c28s002_270d with dissolve
    mc "¿Amigos? Tómate el tiempo que quieras, pero no sigas evitándome. Eso no es lo que hacen los amigos."
    kat "Siempre va bien tener un amigo que abraza de puta madre."
    kat "El día que una chica me deje, puedo venir a por un abrazo como este."
    mc "*Risa* O el día que una beluga te llame prima."
    return
label c28s002_KatRoute:
    mc "No debes sentirte idiota. El que debe sentirse idiota es nuestro universo, porque va con retraso."
    play music ("music/Fragile-Beauty.ogg")
    call BlinkXS4 ("c28s002_300") from _call_BlinkXS4_403
    kat "¿Qué quieres decir?"
    mc "Has dicho que en algún universo te estaba besando hace un minuto."
    scene c28s002_305a with dissolve
    "Sin dejarla responder, la coges entre tus brazos y le das un suave beso en los labios."
    "La sorpresa se muestra en sus ojos. Tú no cierras los tuyos. No quieres perderte nada de vuestro primer beso."
    "Besarla es como besar a una estatua. Petrificada, sin mover un músculo. Por un momento piensas que incluso su corazón ha dejado de latir."
    scene c28s002_305An with dissolve
    "Pero [kat] no es una mujer que se deje sobrepasar por los acontecimientos y recupera el control de su cuerpo unos segundos después."
    "Cierra sus ojos y entreabre su boca, invitándote a entrar en ella por primera vez. No será la última."
    "No te sorprende que sea una gran besadora. En un solo movimiento, mientras vuestras lenguas se entrelazan, hay tanta ternura como pasión y alivio."
    call BlinkXS4 ("c28s002_310") from _call_BlinkXS4_404
    "Al cabo de un segundo o de una hora, vuestros labios se separan mientras vuestras miradas se unen."
    kat "*Jadeo* ¿Qué ha sido eso, [mc]?"
    mc "La demostración de que nuestro universo no es idiota del todo y le gusta recuperar el tiempo perdido."
    kat "*Jadeo* ¿Significa eso que tú y yo...?"
    mc "Significa que tú y yo nos hemos besado, sí."
    call BlinkXS4 ("c28s002_315") from _call_BlinkXS4_405
    kat "*Jadeo* Pero... ¿significa que tú y yo somos algo?"
    mc "A mí me gusta pensar que soy algo. Una persona o algo así... Sobre ti... no estoy tan seguro. *Risa* Dudo entre persona y beluga."
    call BlinkXS4 ("c28s002_320") from _call_BlinkXS4_406
    kat "*Risa* Eres un capullo."
    mc "*Risa* ¿Ves? Eso también es ser algo."
    mc "Pero si a lo que te refieres es a si estamos saliendo o algo así, la respuesta es no."
    call BlinkXS4 ("c28s002_325") from _call_BlinkXS4_407
    kat "¿Qué? Entonces ¿a qué ha venido ese beso?"
    mc "Ese beso ha venido a que me apetecía besarte. Y había un universo en el que ya te había besado."
    mc "Pero has dicho que en otro universo no serías una lesbiana idiota. *Risa* Lo de idiota lo puedo aceptar, es parte de tu encanto."
    mc "Pero, hasta que no cambies 'lesbiana' por 'bisexual' o por 'hetero', no vamos a empezar a salir juntos."
    call BlinkXS4 ("c28s002_330") from _call_BlinkXS4_408
    kat "*Risa* ¡Voy a salir con un idiota!"
    mc "Sólo si lo cambias."
    kat "*Risa* Dalo por cambiado, idiota mío."
    call BlinkXS4 ("c28s002_345") from _call_BlinkXS4_409
    kat "Al menos ya sé a qué sabe un beso de verdad de un chico..."
    mc "*Risa* Espero que nunca te canses nunca del sabor."
    kat "Te aseguro que nunca vas a tener que preocuparte por eso. "
    scene c28s002_305An with dissolve
    "Esta vez es ella quien te besa, sellando el inicio de lo que va a ser una preciosa relación."
    "Nunca os cansaréis de meteros el uno con el otro, haciendo que vuestra relación sea única. Tampoco se cansará del sabor de tus besos."
    "La seguridad que tus brazos y tus labios le van a dar a [kat] van a hacer de ella una mujer inmensamente feliz."
    "Y tú vas a reescribir el significado de la palabra 'felicidad' cada vez que vuestros labios se rocen."
    "También vais a reescribir el significado de muchos insultos."
    scene c28s002_270d with dissolve
    "Pero la resistencia de [kat] y su necesidad de aire marcan el final de vuestro beso."
    "Lo cambia por un abrazo en el que te aprieta con fuerza, como si quisiera asegurarse de que no está en un sueño del que no tiene ningún deseo de despertar."
    mc "¿Ahora vienen los abrazos?"
    kat "Siempre va bien tener un novio que abraza de puta madre."
    kat "El día que tenga un disgusto, puedo venir a por un abrazo como este."
    mc "*Risa* O el día que una beluga te llame prima."
    return
label c28s007_Lis:
    if _in_replay:
        call mrS3_lis_route from _call_mrS3_lis_route_19
    scene black with dissolve
    play music ("music/PositiveWoman.ogg")
    if not lis._var("route"):
        "Bajas a beber agua a la cocina. Necesitas recordar que te tienes que comprar una mini nevera para tu habitación cuando vuelvas de Aruba."
        scene c28s007_005d with fade:
            yalign 1.0
            linear 5.0 yalign 0.0
        pause (4.8)
        call BlinkXS3("c28s007_005") from _call_BlinkXS3_775
        "Al pasar por la planta de las estudiantes..."
        mc "¡Wow, [lis]! ¡Estás super elegante! ¿Vas a la fiesta de tu amiga?"
        lis "Sí, el coche me está esperando abajo para llevarme al helicóptero."
        mc "*Risa* No me acostumbro a esas cosas. Coger un helicóptero para ir a una fiesta."
        call BlinkXS4 ("c28s007_010") from _call_BlinkXS4_410
        lis "Conducir hasta L.A. es demasiado para una fiesta, con lo que es la mejor opción."
        mc "*Risa* Supongo que has dejado de pensar que mi camioneta es demasiado contaminante."
        call BlinkXS4 ("c28s007_015") from _call_BlinkXS4_411
        lis "*Risa* No tengas demasiado en cuenta lo que dije el primer día. Estaba un poco a la defensiva."
        mc "¿Quieres que te acompañe al coche?"
        call BlinkXS4 ("c28s007_020") from _call_BlinkXS4_412
        lis "Me encantaría, si no tienes nada que hacer."
        mc "Si hacemos una parada en la cocina, te acompaño. Iba a beber algo."
        lis "Ningún problema. *Risa* Aunque el chófer lleva un rato esperando, no le importará esperar un par de minutos más."
        scene c28s007_025a with fade
        call BlinkXS4 ("c28s007_025") from _call_BlinkXS4_413
        lis "Bueno, el coche ya está aquí..."
        mc "Pásatelo bien en L.A. ¿Volverás a dormir?"
        lis "No, me quedaré a dormir en casa de mi amiga. Volveré mañana a mediodía más o menos."
        mc "Disfruta de la fiesta, [lis]."
        scene black with dissolve
        "Esperas hasta que el coche se pierde de vista antes de volver a tu habitación."
        stop music fadeout (1.5)
        return
    "Un par de minutos antes de la hora prevista, bajas a buscar a [lis]."
    scene c26s008_005a with dissolve
    play sound ("music/knock.ogg")
    "*Knock-Knock*"
    mc "[lis], soy yo. ¿Estás lista?"
    lis "*A través de la puerta* ¿Ya es la hora? ¡Dame... cinco minutos, por favor!"
    mcp "(*Risa mental* Si conozco a [lis], esos cinco minutos se van a convertir en algunos más.)"
    scene c26s008_005b with dissolve
    "Te sientas en el sofá a esperarla mientras miras el móvil hasta que, al cabo de quince minutos, oyes cómo se abre la puerta."
    scene c28s007_005d with fade:
        yalign 1.0
        linear 5.0 yalign 0.0
    pause (4.8)
    call BlinkXS3("c28s007_005") from _call_BlinkXS3_776
    mc "¡Wow, [lis]! ¡Estás guapísima!"
    call addProfileImageS3 (1, "lis_1", lis, __(": 15 - Especial"), "") from _call_addProfileImageS3_22
    lis "Gracias, [mc]. Tú también."
    lis "Tenemos que darnos prisa. El coche nos está esperando abajo para llevarnos al helicóptero."
    mc "*Risa* No me acostumbro a esas cosas. Coger un helicóptero para ir a una fiesta."
    call BlinkXS4 ("c28s007_010") from _call_BlinkXS4_414
    lis "Sé que suena un poco raro, pero ya te acostumbrarás."
    mc "*Risa* Supongo que has dejado de pensar que mi camioneta es demasiado contaminante."
    call BlinkXS4 ("c28s007_015") from _call_BlinkXS4_415
    lis "No tengas demasiado en cuenta todo lo que dije el primer día. Ya no soy la misma chica, aunque el medio ambiente me siga preocupando." id c28s007_Lis_3043b801
    mc "¿Vamos entonces? No queremos que tu chófer se impaciente. Con que tu novio haya tenido que esperarte hay suficiente, ¿no?"
    call BlinkXS4 ("c28s007_020") from _call_BlinkXS4_416
    lis "*Risa* Una chica necesita tiempo para ponerse guapa para su novio."
    mc "Tú no necesitas tiempo para eso. Estás guapísima siempre."
    call KissXS4 ("c28s007_030") from _call_KissXS4_4
    call BlinkXS4 ("c28s007_030") from _call_BlinkXS4_417
    lis "Eres adorable, [mc]. Pero hay un chófer esperando."
    mc "Por cierto, me encanta el vestido. Muy acorde a la nueva tú."
    lis "*Risita* No vas a conseguir más besos hasta que no estemos en el coche, con lo que guárdate las cosas bonitas para después."
    scene c28s007_025a with fade
    call BlinkXS4 ("c28s007_025") from _call_BlinkXS4_418
    lis "Bueno, parece que no se ha impacientado tanto como para irse..."
    mc "*Risa* Es una suerte, o me tocaría conducir hasta L.A."
    lis "No, tan sólo hasta donde nos espera el helicóptero."
    mc "Pues vamos antes de que el piloto se impaciente y nos deje en tierra."
    scene black with dissolve
    "Os subís al coche y empieza el viaje a una de las noches más raras de tu vida."
    "Hasta entonces. Vas a tener muchas noches más raras después de esta."
    stop music fadeout (1.5)
    return
label c28s007_Kev:
    scene c28s007_100a with fade
    "Mientras tanto, en algún otro lugar de Newport..."
    play sound ("music/doorbell1.ogg")
    "*Ding-Dong*"
    play music ("music/Dark-Score.ogg")
    if "kev" not in globals () or not isinstance (kev, TGCharacter):
        $ kev      = TGCharacter ("Kevin", color="#25f3ff")
    if "mj" not in globals () or not isinstance (mj, TGCharacter):
        $ mj       = TGCharacter (_("Señora Russell"), color="#31f3ff")
    scene c28s007_100f with dissolve
    kev "¡Voy!"
    scene c28s007_100b with dissolve
    mj "¿Quién es?"
    kev "No lo sé, cielo. Aún no he abierto."
    scene c28s007_100c with dissolve
    kev "Puta loca... ¿Cree que tengo telepatía o la app del timbre en el culo?"
    scene c28s007_100d with dissolve
    kev "Oh, eres tú. No te esperaba hasta más tarde."
    scene c28s007_100e with dissolve
    sol "Me ha traído un vecino y así me ahorraba el Under."
    sol "Gracias por acogerme, Kevin. Sólo será una temporada hasta que encuentre un trabajo."
    scene c28s007_100g with dissolve
    sol "Si no hubiera sido por ese hijo de puta del que te hablé y todas sus zorras..."
    stop music fadeout (1.5)
    return

label c20:
    call c20s001_Setup from _call_c20s001_Setup
    call c20s001_NovumTemplum from _call_c20s001_NovumTemplum
    call c20s002_Tavern from _call_c20s002_Tavern
    call c20s002_AMosquitoe from _call_c20s002_AMosquitoe
    if not sca._var("rejectedBeagan"):
        call c20s003_SexWithPia from _call_c20s003_SexWithPia
        call c20s003_DevilAngelTeam from _call_c20s003_DevilAngelTeam
        call c20s003_SexWithAeliaAndPaula from _call_c20s003_SexWithAeliaAndPaula
    else:
        call c20s003_DevilAngelTeam from _call_c20s003_DevilAngelTeam_1
    call c20s004_Farewell from _call_c20s004_Farewell
    call c20s005_EndGameFarewell from _call_c20s005_EndGameFarewell
    call c20s005_GivingMaddieARide from _call_c20s005_GivingMaddieARide
    if kia._var("route"):
        call c20s006_ReturningHome from _call_c20s006_ReturningHome
    if dap._var("route") and emm._var("route") and eri._var("route"):
        call c20s007_Teaser from _call_c20s007_Teaser
    return
label c20_DefineCharacters:
    define scad = Character("Beagan (Scarlett)", color="#33f3ff")
    define scadd = Character(_("Beagan (Imaginación)"), color="#33f3ff")
    define emmd = Character("Paula ([emm])", color="#8f497b")
    define emmdd = Character(_("Paula (Imaginación)"), color="#8f497b")
    define erid = Character("Aelia ([eri])", color="#7b7b7b")
    define eridd = Character(_("Aelia (Imaginación)"), color="#7b7b7b")
    define dapd = Character("Pia ([dap])", color="#e85613")
    define dapdd = Character(_("Pia (Imaginación)"), color="#e85613")
    define madd = Character("Fang (Maddie)", color="#c4ff33")
    define mcd = Character("Vilfredo ([mc])", color="#9042f5")
    define mcdd = Character(_("Vilfredo (Imaginación)"), color="#9042f5")
    define mcpd = Character("Vilfredo ([mc])", what_italic = True, color="#9042f5")
    define unk = Character("???")
    define marziad = Character("Marzia")
    define marzia = Character(_("Marzia (Imaginación)"))
    define wil = Character(_("Hijo de Granjero #3"))
    define thi = Character("Thiel", color="#e5bc22")
    define jup = Character(_("Júpiter"), color = "#0023ff")
    define sold = Character("Solomon", color="#ff0000")
    define erkd = Character("Euricus", color="#fbff00")
    if not _in_replay:
        $ sam.profileImages.pop (13) # first remove
        $ sam.profileImages.insert (13, ("samantha_13", None)) # then add new
        $ mar.profileImages.pop (13) # first remove
        $ mar.profileImages.insert (13, ("martha_13", None)) # then add new
        $ emm.profileImages.pop (13) # first remove
        $ emm.profileImages.insert (13, ("emma_13", None)) # then add new
        $ oma.profileImages.pop (13) # first remove
        $ oma.profileImages.insert (13, ("alexia_13", None)) # then add new
        $ eri.profileImages.pop (13) # first remove
        $ eri.profileImages.insert (13, ("erika_13", None)) # then add new
        $ eil.profileImages.pop (13) # first remove
        $ eil.profileImages.insert (13, ("eileen_13", None)) # then add new
        $ mad.profileImages.pop (13) # first remove
        $ mad.profileImages.insert (13, ("maddie_13", None)) # then add new
        $ sca.profileImages.pop (13) # first remove
        $ sca.profileImages.insert (13, ("scarlett_13", None)) # then add new
        $ dap.profileImages.pop (13) # first remove
        $ dap.profileImages.insert (13, ("daphne_13", None)) # then add new
        $ sai.profileImages.pop (13) # first remove
        $ sai.profileImages.insert (13, ("saira_13", None)) # then add new
        $ ama.profileImages.pop (13) # first remove
        $ ama.profileImages.insert (13, ("amanda_13", None)) # then add new
        $ nor.profileImages.pop (13) # first remove
        $ nor.profileImages.insert (13, ("norah_13", None)) # then add new
        $ eva.profileImages.pop (13) # first remove
        $ eva.profileImages.insert (13, ("eva_13", None)) # then add new
        $ mee.profileImages.pop (13) # first remove
        $ mee.profileImages.insert (13, ("olivia_13", None)) # then add new
        $ bet.profileImages.pop (13) # first remove
        $ bet.profileImages.insert (13, ("betty_13", None)) # then add new
        $ kim.profileImages.pop (13) # first remove
        $ kim.profileImages.insert (13, ("kim_13", None)) # then add new
        $ kia.profileImages.pop (13) # first remove
        $ kia.profileImages.insert (13, ("kiara_13", None)) # then add new
        $ sim.profileImages.pop (13) # first remove
        $ sim.profileImages.insert (13, ("simone_13", None)) # then add new
    return
label c20s001_Setup: #1
    if _in_replay:
        menu:
            "¿Estás en una relación con [dap]?"
            "Sí":
                $ dap._var("route" , True)
            "No":
                $ dap._var("route" , False)
    call c20_DefineCharacters from _call_c20_DefineCharacters
    call BlinkXP ("c20s001_005" , "d") from _call_BlinkXP_3548
    play music ("music/ABCSong.ogg")
    mc "Entonces, ¿cómo funciona esto? ¿Tú nos explicas lo que pasa y nosotros decidimos qué hacemos?"
    dap "Más o menos. En base a lo que tu personaje sabe hacer... ahora te pasaré la hoja de personaje para que lo sepas..."
    dap "Tú decides lo que quieres hacer o no. Pero siempre intentando mantenerte fiel a cómo has diseñado a tu personaje, su personalidad, sus creencias... y sus habilidades."
    call BlinkXP ("c20s001_010" , "d") from _call_BlinkXP_3549
    sca "Por ejemplo, mi hechicera, no va a poder decir que le pega con la espada a alguien, porque no tiene espada y tiene otras herramientas más útiles."
    sca "Además de que tiene cierta alergia a meterse en combate cuerpo a cuerpo."
    mc "Entonces es un poco como teatro de improvisación..."
    call BlinkXP ("c20s001_015" , "d") from _call_BlinkXP_3389
    dap "Es exactamente eso, pero como es un juego, tú dirás qué quieres hacer, yo decidiré la dificultad, y tirarás un dado. No usamos del todo las reglas del libro oficial, pero se parecen."
    mc "Vale, lo entiendo. ¿Pero cómo sabré qué aspecto tiene cada cosa? ¿Vas a describir absolutamente todo? Puede ser un poco aburrido tener que describir de qué madera está hecha una mesa, ¿no?"
    call BlinkXP ("c20s001_020" , "d") from _call_BlinkXP_3390
    dap "*Risa* No hace falta llegar a ese nivel de detalle. Yo te diré que hay una mesa, y tú te la imaginas. Da lo mismo que tú la imagines de pino y Scarlett de nogal."
    dap "Si la mesa tiene algo importante, por ejemplo un dibujo, eso sí que lo describiré."
    mc "Pero entonces, cada uno estaremos imaginando cosas diferentes, ¿no? Aunque supongo que no es importante..."
    call BlinkXP ("c20s001_025" , "d") from _call_BlinkXP_3391
    eri "No, no lo es. Mi personaje tiene cuernos. Da lo mismo que los imagines de vaca o de carnero."
    eri "¿[emm] no ha llegado aún? Creía que seríamos las últimas."
    mc "No, sólo queda ella."
    call BlinkXP ("c20s001_030" , "d") from _call_BlinkXP_3392
    mad "Piensa también que nosotros vamos a tener que describir cosas. Por ejemplo, mi personaje se parece mucho a mí, pero tiene el pelo completamente negro, típico asiático."
    mad "Si es importante, lo describimos. Si no, no. Por ejemplo, nunca te diré de qué color lleva pintadas las uñas Fang, o si las lleva pintadas. Porque no es importante."
    call BlinkXP ("c20s001_035" , "d") from _call_BlinkXP_3393
    emm "¿Cómo que no es importante? Paula usa la manicura francesa... *Risa* Aunque supongo que aquí será la manicura gala."
    mc "Quizás lo que es importante para tu personaje no lo es para otros. Creo que lo voy entendiendo."
    call BlinkXP ("c20s001_040" , "d") from _call_BlinkXP_3394
    dap "Bueno, pues podemos empezar, ¿no?"
    dap "Ahora que la artista está aquí, os hemos preparado esto. Son nuestros pequeños regalos por uniros a nuestra noche de Damiselas y Dragones."
    dap "Las ha pintado [emm]."
    call BlinkXP ("c20s001_045" , "d") from _call_BlinkXP_3395
    mad "¡Oh, es preciosa! ¡Muchas gracias!"
    call BlinkXP ("c20s001_050" , "d") from _call_BlinkXP_3396
    mc "¡Es increíble! No es exactamente como me imaginaba mi personaje, pero es muy bonita."
    mc "Supongo que el rango de figuras a elegir es limitado, y esta se parece lo suficiente."
    dap "Por eso quise hacer los personajes el miércoles. Así hemos tenido tiempo de comprarlas y de que [emm] las pintara."
    mc "Muchas gracias a las dos. Es una pasada."
    scene c20s001_055a with dissolve
    eri "Estas son las nuestras. [emm] es una artista pintando figuritas."
    emm "Gracias, [eri]. Es muy divertido pensar en cómo se ven los personajes y pintarlos para que lo reflejen."
    mc "Son preciosas también."
    scene c20s001_055b with dissolve
    dap "Y estas son las de Scarlett y la mía. Fue la única figura que encontré con martillo, armadura, y trenza. Como siempre, [emm] hizo un gran trabajo."
    sca "Todas estamos muy agradecidas a [emm]. Nunca encontré una figura que se pareciera a como imagino a Beagan, mi hada, pero me encanta cómo la pintó [emm]."
    mc "Me encantan todas. [emm], tienes talento para esto."
    mad "Desde luego que sí. Yo no podría darles tantos detalles aunque quisiera, en una cosa tan pequeña."
    call BlinkXP ("c20s001_060" , "d") from _call_BlinkXP_3397
    emm "Bueno, ¿empezamos a jugar o me vais a hacer ruborizar?"
    mc "Si te ruborizas, tus mejillas se pondrán rosas e irán a juego con tu pijama, con lo que supongo que estarás contenta. *Risa*"
    mc "Pero mejor que empecemos antes de que se haga más tarde."
    call BlinkXP ("c20s001_065" , "d") from _call_BlinkXP_3398
    dap "Pues la cosa empieza en una taberna casi vacía. Vilfredo ([mc]) y Fang (Maddie) habéis llegado a Novum Templum, un pueblo a unas 50 millas romanas (74 km, 46 millas) al sur de Vindobona (Viena)."
    dap "Trabajabais como guardias de caravanas y os habéis quedado sin trabajo. Vuestra caravana continuará hacia Vindobona siguiendo a una cohorte que se dirige a la ciudad."
    dap "Os habéis separado para ver si había alguna caravana que escoltar de vuelta a Italia y habéis quedado en la taberna. Vilfredo es el primero en llegar."
    dap "Ya os puse en antecedentes antes de lo que habíais encontrado. Espero que lo recordéis."
    scene c20s001_070a with dissolve
    dap "¿Qué haces, [mc]?"
    stop music fadeout (1.5)
    mc "No sé, supongo que me acerco al tabernero..."
    scene c20s001_070b with pixellate
    play music ("music/dnd/medieval-loop-one.ogg")
    dap "Tabernera... Una cosa curiosa que habéis visto es que, en este pueblo, hay muy pocos hombres."
    if dap._var("route"):
        mcp "(Es difícil imaginarse la taberna de una forma diferente a como era el Black Crow Inn donde estuvimos [dap] y yo.)"
    mc "Me acerco a pedir una cerveza... Hay cerveza, ¿no?"
    dap "*Risa* Sí, hay cerveza. Pídeme la cerveza."
    mc "¿A tí? Creía que tú formabas parte del grupo, no sabía que eras la tabernera."
    scene c20s001_075a with pixellate
    pause (0.3)
    call BlinkXP ("c20s001_075" , "d") from _call_BlinkXP_3399
    sca "Todos los personajes que no llevamos los que estamos sentados alrededor de la mesa, los interpreta [dap]. La tabernera, el centurión, los malos, etc."
    mc "Eso tiene que ser muy complicado... pero empiezo a entenderlo... Volvamos a ello."
    scene c20s001_070b with pixellate
    mcd "Buenos días, Sra. Tabernera..."
    mc "¿Cómo es la tabernera, [dap]?"
    dap "Cocina genial, con lo que la diseñé para que se pareciera a Tía [mar]..."
    emm "Pero pelirroja. *Risa*"
    dap "*Risa* Sí, en este pueblo verás que casi todas las mujeres son pelirrojas. Imáginate a Tía [mar], pero pelirroja."
    mc "OK, volvamos a ello... antes de que alguien se enfade porque hayas diseñado una [mar] pelirroja."
    call BlinkXP ("c20s001_080" , "d") from _call_BlinkXP_3400
    mcd "Buenos dias, Hermosa Tabernera, ¿me podrías servir dos cervezas? ¿Y si puede ser, también vuestro nombre?"
    eri "*Risa* ¿Estás ligando con Marzia?"
    mc "No. *Risa* Pero llamarle Hermosa Tabernera cada vez no me parece apropiado."
    unk "Siéntese en esa mesa y ahora se la llevo."
    dap "Tira por Carisma. Necesitas sacar 12 o más, incluído tu bono de Carisma, lo puedes ver en tu ficha. Con ese dado no, con el más grande. 13+3."
    marziad "Y me llamo Marzia, Señor..."
    if not _in_replay:
        $ mar.profileImages.pop (6) # first remove
        $ mar.profileImages.insert (6, ("martha_6", None)) # then add new
        $ texto = str(mar.name)
        $ renpy.notify ("Profile Image unlocked for "+str(texto)+": 07 - DnD")
    mcd "Vilfredo il Bisteccone."
    scene c20s001_085a with pixellate
    call BlinkXP ("c20s001_085" , "d") from _call_BlinkXP_3401
    mc "Una pregunta, [dap]. Si todo el mundo habla latín aún, mi nombre no tiene mucho sentido, es en italiano..."
    dap "El latín ha evolucionado en los últimos 900 años de guerras e invasiones. No es el mismo latín que se hablaba en la época de la República."
    dap "Además, hay dialectos. No hablan el mismo latín en Egipto que en Roma. Como no tengo ni idea de latín, Scarlett y yo decidimos que el italiano era un sustituto aceptable como dialecto para esta zona."
    mc "Ah, vale. Pues me siento a esperar que la Hermosa Marzia me traiga mi cerveza."
    scene c20s001_090aa with pixellate
    call BlinkXP ("c20s001_090a" , "d") from _call_BlinkXP_3402
    dap "*En el mundo real* A los pocos minutos ves llegar a Fang, el personaje de Maddie. Descríbete, Maddie."
    mad "*En el mundo real* 26 años, alta, pelo largo en una coleta, armadura de cuero, un arco... y un tigre como compañero. Se llama Júpiter."
    mc "*En el mundo real* Yo soy un SemiElfo, con armadura de cuero, y coleta. Mi tono de piel es un poco oscuro, ya que mi parte élfica es de un elfo oscuro varias generaciones atrás."
    mcp "(Hay algo mal con el personaje de Maddie... todo el mundo sabe que, para las armaduras femeninas, cuanto menos cubren, más protegen, ¿no?)"
    scene c20s001_090d with dissolve:
        yalign 1.0
        linear 5.0 yalign 0.0
    pause (5.0)
    call BlinkXP ("c20s001_090b" , "d") from _call_BlinkXP_3403
    if not _in_replay:
        $ mad.profileImages.pop (6) # first remove
        $ mad.profileImages.insert (6, ("maddie_6", None)) # then add new
        $ texto = str(mad.name)
        $ renpy.notify ("Profile Image unlocked for "+str(texto)+": 07 - DnD")
    mcp "(Mucho mejor.)"
    call BlinkXP ("c20s001_095a" , "d") from _call_BlinkXP_3404
    marzia "¡Hey, tú! No puedes entrar aquí con ese animal..."
    scene c20s001_090f with dissolve
    mcp "(Júpiter... equivalente romano de...)"
    scene c20s001_090g with dissolve
    mcp "(Zeus. *Risa*)"
    jup "*Ronroneo*"
    call BlinkXP ("c20s001_095b" , "d") from _call_BlinkXP_3405
    marzia "Con ese animal precioso y que no le demos un poco de leche."
    mcp "(¡Claro! ¡También me puedo imaginar diálogos poco importantes si [dap] no dice lo contrario!)"
    dap "*En el mundo real* ¿Qué contestas, [mc]?"
    mc "*En el mundo real* Perdón, me había perdido en mis pensamientos... ¿Puedes repetirme la pregunta?"
    call BlinkXP ("c20s001_095c" , "d") from _call_BlinkXP_3406
    madd "¿Has encontrado alguna caravana?"
    mcd "No, no hay nadie en este pueblo que nos quiera contratar de vuelta a Italia."
    call BlinkXP ("c20s001_100" , "d") from _call_BlinkXP_3407
    madd "A mí me ha pasado lo mismo. Es un pueblo muy pequeño y las caravanas vienen tan solo a cargar grano y se van. Por lo visto tienen un excedente enorme, pero la nuestra era la última."
    madd "Creo que tendremos más suerte si vamos a Vindobona. Es la frontera y posiblemente hayan caravanas que vayan a comerciar con los Enanos."
    mcd "Pues acabémonos las cervezas y vamos a los establos. ¡Camino a Vindobona!"
    call BlinkXP ("c20s001_105" , "h") from _call_BlinkXP_3408
    dap "*En el mundo real* Mientras os tomáis las cervezas entra de golpe una chica, de unos 18 años, en la taberna. Es una chica con orejas de gato y cola de zorro."
    unk "¡Marzia! ¡Han venido los inquisidores de BDSM! ¡Están montando follón en el foro!"
    mc "*En el mundo real* ¿BDSM? Estás de broma, ¿no?"
    dap "*En el mundo real* No, es una organización de fanáticos religiosos, los Bellum Dei Salvum Me (La Guerra Sagrada Me Salvó). *Risa* Más tarde descubrí lo que significaban esas siglas..."
    sca "*En el mundo real* Ni siquiera la traducción es del todo correcta. La hicimos con Foogle. Y espera a ver como se llaman algunos de los miembros."
    call BlinkXP ("c20s001_110" , "d") from _call_BlinkXP_3409
    marziad "¿Dónde están las Protectoras, Thiel?"
    emm "*En el mundo real* *Risita* Esas somos nosotras..."
    eri "*En el mundo real* ¡Calla, [emm]!"
    call BlinkXP ("c20s001_115" , "d") from _call_BlinkXP_3410
    thi "Han salido esta mañana al Bosque del Este. No han vuelto todavía."
    thi "¿Vienes antes de que hagan daño a alguien?"
    call BlinkXP ("c20s001_120" , "d") from _call_BlinkXP_3411
    marziad "Sí, voy."
    marziad "¡Alba! ¡Ocúpate de los clientes!"
    call BlinkXP ("c20s001_125" , "d") from _call_BlinkXP_3412
    madd "Deberíamos ir a ver. ¡Odio a esos fanáticos religiosos!"
    mcd "Vamos, aunque no sé si deberíamos intervenir. No sabemos de qué va todo esto."
    madd "Yo sí. Hace unos años quemaron una ménagerie en Capua porque decían que había brujas faéricas allí. Fue donde rescaté a Júpiter."
    stop music fadeout (1.5)
    jup "*Ronroneo enfadado*"
    return
label c20s001_NovumTemplum: #2
    call c20_DefineCharacters from _call_c20_DefineCharacters_1
    scene c20s001_130a with fade
    play music ("music/dnd/battle-of-the-creek.ogg")
    dap "*En el mundo real* Salís de la taberna y os dirigís al foro. Es un foro minúsculo, pero es que el pueblo es muy pequeño."
    dap "*En el mundo real* Poco más de veinte casas, la taberna, unos almacenes de grano, una herrería, un templo clásico y las ruinas de un templo élfico dentro de un recinto amurallado."
    dap "*En el mundo real* Hace siglos era un fuerte de las legiones que servía para controlar la entrada a la ruta de los Alpes."
    dap "*En el mundo real* Delante del templo clásico veis un grupo de seis personas. Dos alabarderos, dos arqueras, un guerrero y un clérigo. El clérigo empieza a hablar justo cuando llegáis."
    dap "*En el mundo real* No hay prácticamente nadie escuchándolo."
    unk "¡Hemos venido a salvar vuestras almas! ¡Los Dioses saben que algunas mujeres pelirrojas pueden absorber vuestras almas y entregárselas a los Demonios de las Islas!"
    unk "Si habéis visto a alguna mujer pelirroja hacer sus obras demoniacas, hemos venido a salvaros. ¡Las quemaremos a todas!"
    unk "Podéis darle su nombre al Decanus Euricus y nos encargaremos de ella para protegeros."
    scene c20s001_130b with hpunch
    mc "*En el mundo real* ¿Eric?"
    sca "*En el mundo real* Ya te he dicho que fliparías con cómo se llamaban algunos de los BDSM. [dap] los diseñó mucho antes de saber nada de NTR."
    mc "*En el mundo real* ¿Puedo matar a ese capullo?"
    call BlinkXP ("c20s001_135" , "d") from _call_BlinkXP_3413
    erkd "¿Me eztáz amenazando, pedazo de miedda? ¿Noz conocemoz de algo?"
    mcp "([dap] lo ha dicho con su voz normal, pero yo no puedo evitar oirlo como hablaría alguien sin dientes.)"
    mc "*En el mundo real* Espera... no lo ha dicho Vilfredo, lo he dicho yo..."
    dap "*En el mundo real* Ya te he dicho que jugamos con normas un poco especiales. Lo que digas alrededor de la mesa, lo dice tu personaje."
    sca "*En el mundo real* Era la única forma en que [emm] no se pusiera a hablar de ropa o de la última serie que había visto en Netflics."
    emm "*En el mundo real* La culpa siempre es mía... *Gruñido* Pero sí, Euricus te ha oído. Si quieres decir algo como jugador y no personaje tienes que hacer la señal de Tiempo Muerto."
    mc "*En el mundo real* ¡Ufff! ¡A ver cómo salgo yo de esta!"
    mcd "A ver, Decanus... No es que te amenace, es que me recuerdas a alguien a quien tengo muchas ganas de partirle la cara."
    call BlinkXP ("c20s001_140" , "d") from _call_BlinkXP_3414
    erkd "Puez entoncez no moleztez y déjanoz ceguid con nueztda mición. Loz Diocez noz han encadgado acabad con la invacion de bdujaz pelidojaz que vienen de Bditania."
    mcd "Y venís al pueblo donde más pelirrojas he visto en mi vida, ¿no? Dejad a esta gente en paz. No creo que haya ninguna bruja o ningún hada por aquí a las que tengáis que cazar."
    "Scarlett le pasa una nota a [dap]. Ella asiente."
    dap "*En el mundo real* Ahora, Scarlett."
    call BlinkXP ("c20s001_145" , "d") from _call_BlinkXP_3415
    scad "Hay un hada que también es bruja, o hechicera, como prefieras. Pero no pelirroja. ¡Rubia natural!"
    sca "*En el mundo real* Mi personaje es un hada. Ahora mismo mide lo mismo que una persona normal, pero puede cambiar de tamaño."
    sca "*En el mundo real* Es rubia, con un peinado parecido al de Amanda pero al revés y ondulado."
    sca "*En el mundo real* Llevo una falda y un top verdes. Lleva unos tatuajes en el lado izquierdo de la cara y está volando a tres o cuatro metros del suelo."
    mcp "(Es fácil imaginársela como vino al desayuno de disfraces, pero esa falda parece que da demasiado calor...)"
    scene c20s001_150d with dissolve:
        yalign 1.0
        linear 5.0 yalign 0.0
    pause (5.0)
    call BlinkXP ("c20s001_150" , "d") from _call_BlinkXP_3416
    if not _in_replay:
        $ sca.profileImages.pop (6) # first remove
        $ sca.profileImages.insert (6, ("scarlett_6", None)) # then add new
        $ renpy.notify ("Profile Image unlocked for Scarlett: 07 - DnD")
    mcp "(Así, más fresquita y más protegida. Y más parecida a la figurita.)"
    scene c20s001_150e with dissolve
    dapd "Y si buscáis una pelirroja que pueda mandar vuestra alma al infierno, venid a probar mi martillo. Por el poder de Vulcano os castigaré si osáis tocar a esta buena gente."
    erid "No sé que tenéis contra el infierno, mi padre dice que es acogedor..."
    emmd "Tu padre es una sucia criatura del infierno, y pese a todo me tomaría antes una cerveza con él que con esta basura que está contaminando este pueblo respirando su aire."
    "Las chicas empiezan a describir a sus personajes. Tú tienes otra idea."
    scene c20s001_160d with dissolve:
        yalign 1.0
        linear 5.0 yalign 0.0
    pause (5.0)
    call BlinkXP ("c20s001_160" , "d") from _call_BlinkXP_3417
    if not _in_replay:
        $ dap.profileImages.pop (6) # first remove
        $ dap.profileImages.insert (6, ("daphne_6", None)) # then add new
        $ texto = str(dap.name)
        $ renpy.notify ("Profile Image unlocked for "+str(texto)+": 07 - DnD")
    mcp "(Esa armadura era demasiado pesada.)"
    scene c20s001_165d with dissolve:
        yalign 1.0
        linear 5.0 yalign 0.0
    pause (5.0)
    call BlinkXP ("c20s001_165" , "d") from _call_BlinkXP_3418
    if not _in_replay:
        $ eri.profileImages.pop (6) # first remove
        $ eri.profileImages.insert (6, ("erika_6", None)) # then add new
        $ texto = str(eri.name)
        $ renpy.notify ("Profile Image unlocked for "+str(texto)+": 07 - DnD")
    mcp "(Menos hebillas significa menos ruido y más sigilo, ¿no?)"
    scene c20s001_155d with dissolve:
        yalign 1.0
        linear 5.0 yalign 0.0
    pause (5.0)
    call BlinkXP ("c20s001_155" , "d") from _call_BlinkXP_3419
    if not _in_replay:
        $ emm.profileImages.pop (6) # first remove
        $ emm.profileImages.insert (6, ("emma_6", None)) # then add new
        $ texto = str(emm.name)
        $ renpy.notify ("Profile Image unlocked for "+str(texto)+": 07 - DnD")
    mcp "(Ese escudo no parece suficiente protección contra las alabardas. Ahora tu armadura es algo mejor.)"
    scene c20s001_170An
    mcp "(¡Hostias! ¡La cara que pondría el personaje de [emm] si se diera cuenta de que le he reducido su armadura!)"
    mcp "(Mejor vuelvo a prestar atención a la partida...)"
    call BlinkXP ("c20s001_175" , "d") from _call_BlinkXP_3420
    erkd "No oz acedquéiz al Hedmano Zolomon. Tenemoz derecho a eztad aquí y pdedicar nuestdaz cdeenciaz."
    mcp "(¿Solomon? ¿Va a haber también un Jack, un Kevin, y un Jonas?)"
    call BlinkXP ("c20s001_180" , "d") from _call_BlinkXP_3421
    erid "Tenéis derecho a predicar vuestras creencias. No tenéis ningún derecho a amenazar a la gente, y menos aún a quemarla."
    "Habla con mucha calma. Como Amanda habló con Solomon. No puedes evitar imaginártela haciéndose la manicura mientras pronuncia esas palabras."
    call BlinkXP ("c20s001_185" , "d") from _call_BlinkXP_3422
    sold "¡Deus Vult! ¡Marte lo pide! ¡Nundina lo pide! ¡Tenemos que acabar con las criaturas de la noche para que este mundo vuelva a ser de los humanos!"
    sold "¡Aberraciones como vosotras tienen que desaparecer!"
    mcp "(Ver... imaginar esa cara me está haciendo crecer la agresividad.)"
    mcd "A ver, capullo... No entiendo mucho de Dioses y Diosas. Pero si quieres erradicar a las razas, vete... {i}(¿cuanto era?){/i}... 100 millas al norte y encontrarás un montón de Enanos."
    mcd "Deja a esta pobre gente en paz, aquí todo el mundo es humano."
    dap "*En el mundo real* ¡Ejem!"
    call BlinkXP ("c20s001_190" , "d") from _call_BlinkXP_3423
    sold "¿Veis, buenas gentes? ¡Una escoria semielfa está haciéndose pasar por humano delante de vuestras narices cuando sus orejas lo delatan!"
    mcp "(¡Mierda, es verdad!)"
    mcd "Me refería a los habitantes de Novum Templum... Yo solo estoy de paso hacia la frontera..."
    dap "*En el mundo real* Tira por Carisma. Necesitas más de 18. El otro dado..."
    mc "*Tiempo Muerto* Pero antes era más de 12..."
    dap "*En el mundo real* Ahora es más difícil. Por norma no digo lo que necesitáis, pero como es tu primera partida, te lo pongo fácil. 7+3. Ves que Solomon te ignora."
    call BlinkXP ("c20s001_195" , "d") from _call_BlinkXP_3424
    marzia "No sois bienvenidos aquí. Como miembro del Consejo de Mujeres os pido que os vayáis. De todas formas, puedes ver que no habéis congregado una gran audiencia."
    dap "*En el mundo real* Ciertamente, veis que, aparte de Marzia, Thiel, y vosotros, solo hay cinco o seis personas más. Un par de ellos parecen claramente forasteros."
    call BlinkXP ("c20s001_200" , "d") from _call_BlinkXP_3425
    emmd "Ya habéis oído a la dama. Os queremos fuera de este pueblo antes de que caiga el sol."
    call BlinkXP ("c20s001_205" , "d") from _call_BlinkXP_3426
    dapd "Que aquí no haya Vigiles (algo parecido a la policía en el Imperio Romano) no significa que esto sea un pueblo sin ley."
    dapd "El Consejo de Mujeres nos ha pedido que velemos por la seguridad de los habitantes de Novum Templum."
    call BlinkXP ("c20s001_210" , "d") from _call_BlinkXP_3427
    dap "*En el mundo real* Solomon alza el brazo en dirección a Marzia y a Thiel. Con el pulgar hacia abajo."
    sold "¡Coged a esa perra pelirroja y a la aberración que tiene como mascota! A ver si tiene valor para prohibirnos estar aquí cuando esté encadenada."
    scene c20s001_215a with dissolve
    dap "*En el mundo real* Uno de los alabarderos se dirige a Marzia. ¿Qué hacéis?"
    emm "*En el mundo real* Paula se interpone entre el alabardero y ella."
    dap "*En el mundo real* Estás al otro lado de la plaza, demasiado lejos. Eso podrían hacerlo [mcd] o [madd]. O Scarlett podría lanzar algún hechizo."
    mc "*En el mundo real* Me interpongo yo. Desenvaino las armas."
    eri "*En el mundo real* Yo me acerco por el otro flanco... hacia donde está el otro alabardero."
    sca "*En el mundo real* Me hago pequeña y subo volando al almacén que hay delante del templo."
    mad "*En el mundo real* Saco una flecha y apunto a las arqueras. Júpiter se pone en posición amenazante."
    scene c20s001_215An with dissolve
    mcp "(Mejor que vuelva a ser un tigre en este caso.)"
    dap "*En el mundo real* Pia se desplaza hacia el centro del foro."
    dap "*En el mundo real* Scarlett, ¿puedes poner las figuras? Ya sabes la disposición inicial."
    sca "*En el mundo real* [mc], pon estas figuras y esos dados ahí y ahí, por favor."
    scene c20s001_220a with pixellate
    sca "Los d4 son los alabarderos, los d6 las arqueras, el d8 Euricus, el d10 Solomon, y los d12 Marzia, rojo, y Thiel, naranja. Júpiter es el d6 naranja."
    dap "[mc], el alabardero intenta apartarte con su arma. ¿Qué haces?"
    mc "¿Puedo apartar el arma?"
    dap "Tira el dado. Necesitas más de 15. 1. ¡Uff!. Scarlett, pon otro d12 a la izquierda de Marzia, delante de Thiel."
    mc "Eso es malo, ¿no? ¿No le sumo nada?"
    scene c20s001_220An with pixellate
    dap "*En el mundo real* Apartas la alabarda, pero no mides correctamente la fuerza, y tanto el alabardero como tú perdéis un poco el equilibrio."
    dap "*En el mundo real* El contrapeso del arma impacta contra la mejilla de un chico que ha avanzado al lado de Marzia, intentando proteger a Thiel."
    dap "*En el mundo real* *Tirando dados* Le hace un pequeño corte en la mejilla. Un uno en el dado es la peor puntuación posible, [mc]. Se llama pifia."
    dap "*En el mundo real* Y ahora viene mi pifia como DM. No le he puesto nombre al chico. *Risa* Lo tengo apuntado como"
    wil "¡Ahhh!"
    mc "*En el mundo real* ¿Puedo apuñalar al alabardero?"
    dap "*En el mundo real* No. Es el momento en que el resto hagan sus acciones. *Tira dados* Las arqueras sacan flechas de sus carcaj y te apuntan. Maddie."
    scene c20s001_225An with dissolve
    mad "*En el mundo real* Les digo que no hagan nada con la cabeza mientras las apunto alternativamente."
    madd "Bajad los arcos. Puedo dispararos a ambas antes de que soltéis la segunda flecha."
    mad "*En el mundo real* *Tirando dados* 18 - 1. Me parece que me creen."
    mad "*Risita* *Tiempo Muerto* Es una fanfarronada, pero ellas no lo saben, [mc]. Es una de las cosas buenas de esto; ni tú sabes el nivel que tienen ellos ni ellos el que tienes tú."
    dap "*En el mundo real* [emm]. Tu turno."
    scene c20s001_230An with dissolve
    emm "*En el mundo real* Cargo contra Euricus, pero contengo el golpe. Me pongo delante de Euricus, en posición amenazadora."
    emmd "Dile a tu gente que baje las armas."
    emm "*En el mundo real* *Tirando dados* Carisma 20 + 3. Se ha cagado patas abajo."
    dap "*En el mundo real* Genial. [eri]."
    eri "*En el mundo real* Me acerco al otro alabardero por detrás y le pongo un cuchillo en el cuello. Supongo que está distraído y tengo algún bonus. 14 + 4"
    scene c20s001_235An with dissolve
    erid "*Susurrando* Será mejor que sueltes ese pincho. No queremos que te hagas daño. Ni quiero hacértelo yo."
    scene c20s001_240An with dissolve
    dap "*En el mundo real* *Tira dados* El alabardero suelta la alabarda."
    scene c20s001_245a with dissolve
    dap "*En el mundo real* Euricus levanta las manos en señal de derrota. No le ha dado tiempo a sacar las armas."
    erkd "No hace falta luchad. Ya noz vamoz. No queremoz pdedicad en lugarez donde no zomoz bienvenidoz."
    call BlinkXP ("c20s001_250" , "d") from _call_BlinkXP_3428
    sold "¡No tenéis derecho a echarnos! ¡Estamos aquí para salvar vuestras almas! Os convertiréis en lemures si morís después de que una pelirroja os absorba el alma..."
    call BlinkXP ("c20s001_255" , "d") from _call_BlinkXP_3429
    dapd "No somos malas... es que hemos nacido así. *Risa*" #We're not bad... we've just born that way.
    dap "*Tiempo Muerto* *Risita* Siempre he querido hacer un homenaje a esa frase de Jessica Hare. Menos mal que no la habéis cagado."
    scene c20s001_245b with dissolve
    erkd "No le hagáiz mucho caso. No zabe aceptad una dedota ni irce cuando zobda en algún citio."
    call BlinkXP ("c20s001_260" , "d") from _call_BlinkXP_3430
    sold "¡Decanus! ¡Esa no es una conducta propia de un servidor de Marte!"
    sold "¡Informaré a nuestro amado lider de tus palabras!"
    scene c20s001_245c with dissolve
    dap "*En el mundo real* Los BDSM se dirigen a las puertas en las murallas del pueblo bajo la atenta mirada de las Protectoras. Euricus y Solomon están claramente discutiendo."
    dap "*En el mundo real* No hay nadie para abrir las puertas. Parecen un poco humillados por tener que abrir las pesadas puertas ellos mismos."
    mc "*Tiempo Muerto* Pero las puertas estaban abiertas cuando hemos llegado con la caravana. ¿No se cerraban solo de noche?"
    stop music fadeout (1.5)
    scene c20s001_265a with pixellate
    call BlinkXP ("c20s001_265" , "d") from _call_BlinkXP_3431
    sca "Las ha cerrado Beagan con magia cuando hemos llegado al pueblo. Hay otros cinco BDSM fuera, cuatro alabarderos y un arquero, y no quería que intervinieran."
    sca "Me he imaginado lo que estaba pasando dentro al no ir acompañados de un clérigo. Ese fue el final de nuestra última partida. [dap] siempre nos deja con ganas de más."
    call BlinkXP ("c20s001_270" , "d") from _call_BlinkXP_3432
    dap "El encuentro ha acabado. *Risa* Por una vez lo habéis resuelto sin tener que matar a nadie. La gente empieza a dispersarse ¿Qué hacéis?"
    mc "Yo quiero ver cómo está el chaval que ha recibido la hostia con la alabarda."
    scene c20s001_275a with pixellate
    call BlinkXP ("c20s001_275" , "d") from _call_BlinkXP_3433
    play music ("music/dnd/sunguard.ogg")
    dap "*En el mundo real* No es un chaval, tiene unos 18."
    mcd "¿Cómo estás chaval?"
    wil "Bien, Señor. Ha sido muy valiente lo que ha hecho, defendiendo a las mujeres. Gracias..."
    call BlinkXP ("c20s001_280" , "d") from _call_BlinkXP_3434
    mcd "Marzia, ¿puedes traer algo para limpiar la herida y curarle?"
    marziad "Sí, ahora mismo voy."
    mc "*En el mundo real* Ayudo a levantarse al chaval."
    call BlinkXP ("c20s001_285" , "d") from _call_BlinkXP_3435
    dapd "Bueno, las curaciones son mi especialidad... ni siquiera quedará cicatriz."
    call BlinkXP ("c20s001_290" , "d") from _call_BlinkXP_3436
    dap "*En el mundo real* Mmmm..."
    wil "Si no le importa, Señora, preferiría el método tradicional de curación... no es que tenga nada en contra de la magia..."
    scene c20s001_290An with dissolve
    dap "*En el mundo real* Veis que dirige una fugaz mirada a Thiel, la chica gato. Retira la mirada en cuanto se da cuenta de que ella también lo está mirando."
    call BlinkXP ("c20s001_295a" , "d") from _call_BlinkXP_3437
    wil "*Susurrando* A las chicas les gustan las cicatrices, ¿verdad?"
    mcd "*Susurrando* *Risa* Sí, muchacho, les gustan."
    wil "Además, servirá de recordatorio de cuando echasteis a los BDSM del pueblo."
    call BlinkXP ("c20s001_295b" , "d") from _call_BlinkXP_3438
    mcd "¿Quieres ser legionario? En el ejército conseguirás muchas más cicatrices."
    wil "No, señor, solo quiero ayudar a mi madre y a mis hermanas en la granja. Faltan hombres en este pueblo."
    call BlinkXP ("c20s001_300" , "d") from _call_BlinkXP_3439
    madd "Vilfredo, deberíamos partir hacia Vindobona o se nos hará de noche en el camino."
    mcd "Perfecto, vamos a los establos a coger los caballos y nos vamos."
    call BlinkXP ("c20s001_305" , "d") from _call_BlinkXP_3440
    marziad "No sabéis lo lejos que está Vindobona, ¿verdad? No llegaréis allí antes de que se ponga el sol y cierren las puertas. Son unas seis horas cabalgando."
    marziad "A menos que queráis reventar los caballos."
    marziad "Pero podéis dormir en la posada hoy y partir mañana por la mañana. Las habitaciones corren de mi cuenta."
    mcd "Gracias, ¿que te parece, Madd... digo... Fang?"
    call BlinkXP ("c20s001_310" , "d") from _call_BlinkXP_3441
    madd "No es mala idea. Muchas gracias, Marzia."
    call BlinkXP ("c20s001_315" , "d") from _call_BlinkXP_3442
    scad "Dejadnos invitaros a una cerveza."
    mcd "Eso lo podemos aceptar sin problema."
    mcd "Pero antes..."
    scene c20s001_325pv
    show c20s001_325v
    pause (13.03)
    scene c20s001_325dv
    mc "*En el mundo real* Le lanzo una moneda al chaval. Se lo ha ganado, al menos por la cicatriz que llevará de por vida por mi culpa."
    mc "*Risa* *Tiempo Muerto* Me siento culpable por un personaje que no tiene nombre siquiera."
    scene c20s001_330d with dissolve
    hide c20s001_325v
    wil "¡Oh! ¡Gracias, Señor!"
    mcd "Te lo has ganado, muchacho. Siempre hay que defender a los más débiles."
    eri "*Risa* *Tiempo Muerto* Te recuerdo que Vilfredo es tu personaje, no eres tú."
    emm "*Risa* *Tiempo Muerto* Y no eres un caballero, eres un pícaro."
    mc "*Risa* *Tiempo Muerto* Lo sé, pero lo diseñé como un defensor de las damas. Y el chaval apunta maneras."
    call BlinkXP ("c20s001_330" ,"d") from _call_BlinkXP_3443
    wil "¡Lo haré! ¡Guardaré su moneda como recordatorio!"
    mcd "Hazlo muchacho."
    stop music fadeout (1.5)
    mc "*En el mundo real* Ya nos podemos ir a tomar esa cerveza, paga..."
    scene c20s001_335a with pixellate
    play music ("music/ChillUkelele.ogg")
    mc "Beagan."
    mc "¡Vaya! Yo estaba contentísimo con el dibujo que había hecho [emm] de mi personaje... ¡Pero el tuyo es espectacular!"
    sca "Todos los ha dibujado [emm]. Es nuestra artista residente."
    mc "¿Me dejáis ver los vuestros, chicas?"
    scene c20s001_335b with fade
    "El resto de las chicas te pasan sus hojas de personaje para que admires las obras de arte de [emm]."
    mc "Son alucinantes, [emm]."
    emm "Gracias..."
    mc "Pero tengo una pregunta... Tú y [eri] os apellidáis igual... ¿Casualidad?"
    call BlinkXP ("c20s001_340" , "d") from _call_BlinkXP_3444
    eri "*Risa* No, no es casualidad. Forma parte de la historia de nuestros personajes. ¿Se lo explicamos o es demasiado pronto?"
    call BlinkXP ("c20s001_345" , "d") from _call_BlinkXP_3445
    if persistent.family:
        emm "Te lo podemos explicar, pero recuerda que tú lo sabes, pero tu personaje no. Somos hermanas de madre."
        emm "Nuestra madre tenía... ¿cómo decirlo?... Una moral distraída... *Risa*"
    else:
        emm "Te lo podemos explicar, pero recuerda que tú lo sabes, pero tu personaje no. Venimos de una familia rara."
        emm "Aunque no lo seamos, nos consideramos hermanas. Pertenecemos a una famila que tiene una antigua conexión con las criaturas de otros planos de existencia."
    call BlinkXP ("c20s001_350" , "d") from _call_BlinkXP_3446
    if persistent.family:
        eri "Básicamente, se follaba a cualquier criatura mágica que pudiera encontrar. Primero se folló al padre del personaje [emm], un Ángel, y nació Paula."
        eri "Un año después conoció un Diablo. Y también acabaron en la cama. Y nueve meses después apareció Aelia. Livia es el nombre de la familia de nuestra madre."
    else:
        eri "Una de las mujeres de la familia obliga a sus esclavas a follarse criaturas mágicas. Primero consiguió que un Ángel se follara a una de sus esclavas y nació Paula."
        eri "Un año después hizo que otra esclava se acostara con un Diablo y apareció Aelia. Livia es el apellido de esa mujer. Cuando nos manumitió, nos dio su apellido."
    mc "*Risa* Una mujer interesante, la Señora Livia. ¿Alguna más que tenga una historia divertida?"
    call BlinkXP ("c20s001_355" , "d") from _call_BlinkXP_3447
    dap "*Risa* ¡A mí no me mires! Yo soy normal, o más o menos. Como tú."
    dap "Durante las Guerras Enanas, hace unos 150 años, una antepasada mía intimó, no sabemos si voluntariamente o no, con un elfo bajo el sol de Tarraco."
    dap "La sangre élfica nunca desaparece del todo."
    call BlinkXP ("c20s001_360" , "d") from _call_BlinkXP_3448
    sca "Lo mío es más sencillo. Soy de Hibernia (Irlanda). Las Hadas conquistaron las Islas Británicas mientras los Romanos se pegaban, y perdían, con los Elfos en la Galia."
    sca "Estoy en el continente en... una misión que sólo [dap] conoce."
    call BlinkXP ("c20s001_365" , "d") from _call_BlinkXP_3449
    mc "¿Y tu, Maddie? Tu personaje es asiática, pero te apellidas Josephus. Es raro, ¿no?"
    mad "Bueno, mis abuelos llegaron a Siria huyendo de las criaturas que habitan en Asia Oriental hace 60 años. Cambiaron su apellido cuando llegaron, como casi todos los refugiados."
    mad "Pero seguimos manteniendo las costumbres de nuestra patria, Wu, como puedes ver por mi nombre."
    mc "Oh, genial. Todas tenéis una historia chula... Yo... soy un SemiElfo cuya antepasada fue violada por un Drow. Fin de la historia. *Risa*"
    call BlinkXP ("c20s001_370" , "d") from _call_BlinkXP_3450
    dap "Eso se aprende tal como vayas jugando más. Conocerás el mundo y podrás añadir cosas a la historia de tu próximo personaje."
    call BlinkXP ("c20s001_380" , "d") from _call_BlinkXP_3451
    sca "Además, jugar con un personaje que es una hoja en blanco puede ser muy divertido. No estás atado por un pasado y puedes escribir tu futuro."
    stop music fadeout (1.5)
    sca "¿Seguimos? Se está haciendo tarde..."
    return
label c20s002_Tavern: #3
    if _in_replay:
        menu:
            "¿Cuántas relaciones tienes?"
            "Una":
                $ mc._var("relationships", 1, intention = "set")
            "Más de una":
                $ mc._var("relationships", 2, intention = "set")
            "Ninguna":
                $ mc._var("relationships", 0, intention = "set")
        call c20_DefineCharacters from _call_c20_DefineCharacters_2
    scene c20s002_005a with pixellate
    call BlinkXP ("c20s002_005" , "f") from _call_BlinkXP_3452
    play music ("music/dnd/tavern-loop-one.ogg")
    dap "*En el mundo real* Volvéis a la taberna donde Marzia os sirve unas cervezas."
    marziad "Beagan, las apunto en tu cuenta, ¿no?"
    call BlinkXP ("c20s002_010" , "d") from _call_BlinkXP_3453
    scad "Esta ronda, sí."
    scene c20s002_015An
    scad "Ahora mejor. *Risa*"
    mcd "¿Por qué te has reducido? ¿Lo de tener tamaño humano tiene duración?"
    call BlinkXP ("c20s002_020" , "d") from _call_BlinkXP_3454
    scad "No, que va. Es por una razón mucho más sencilla. La cerveza no cambia de tamaño, pero me dura más. *Risa* Les ahorro unas monedas a mis compañeras."
    call BlinkXP ("c20s002_025" , "d") from _call_BlinkXP_3455
    dapd "No voy a decir que sea una borracha, pero... Beagan es muy considerada con nosotras aunque time a Marzia."
    call BlinkXP ("c20s002_030" , "d") from _call_BlinkXP_3456
    emmd "Técnicamente no es un timo. Marzia sirve una cerveza y cobra una cerveza. Si Beagan consigue pasar la tarde con una sola cerveza no es un timo."
    emmd "Si pensara que está timando a Marzia no le permitiría hacerlo."
    call BlinkXP ("c20s002_035" , "d") from _call_BlinkXP_3457
    erid "¿Y qué ibas a hacer para evitarlo?"
    scene c20s002_040AnBlink with dissolve
    scad "Seguro que Paula pediría una cerveza para mí en cada ronda, aunque no pudiera bebérmela."
    scad "Y no se la dejaría beber a nadie. Ya sabéis que los Paladines no saben divertirse y a veces no dejan divertirse a los demás."
    call BlinkXP ("c20s002_045" , "d") from _call_BlinkXP_3458
    emmd "Exacto... Pero estamos descuidando a nuestros invitados"
    mcd "No te preocupes por nosotros. Me parece muy inteligente lo que ha hecho Beagan."
    call BlinkXP ("c20s002_050" , "d") from _call_BlinkXP_3459
    emmd "No, no, explicadnos qué hacéis en Novum Templum o se pasarán la tarde metiéndose conmigo. Y mis votos me impiden aplastarles la cara."
    emmd "{b}Teóricamente{/b} son mis amigas..."
    call BlinkXP ("c20s002_055" , "d") from _call_BlinkXP_3460
    madd "Nos contrataron como guardias de una caravana en... *Maddie consulta sus notas* Aquileia para ir a Vindobona, parando en algunos pueblos mineros en la ruta de las montañas."
    madd "Cuando hemos llegado a Novum Templum, Marius, el jefe de la caravana, nos ha despedido porque había una cohorte que seguía el mismo camino y ya no nos necesitaban."
    mcd "Hemos intentado encontrar alguna caravana que vuelva a Italia, pero no hay nada aquí. Después de un mes viajando por las montañas, nos quedamos tirados al salir de ellas."
    call BlinkXP ("c20s002_060" , "d") from _call_BlinkXP_3461
    dapd "Seguramente tengáis más suerte en Vindobona. Por norma las caravanas van por la ruta del este. Sólo las caravanas mineras cruzan las montañas."
    mcd "Por eso nos iremos mañana. Aquí no hay trabajo para nosotros."
    call BlinkXP ("c20s002_065" , "d") from _call_BlinkXP_3462
    erid "Si alguna vez volvéis a pasar por aquí, no dudéis en visitarnos. No ha estado mal que hayáis intentado defender a Marzia y a Thiel."
    erid "Incluso sin conocerlas de nada."
    call BlinkXP ("c20s002_070" , "d") from _call_BlinkXP_3463
    madd "Yo sé de lo que son capaces los BDSM. Y Júpiter también. Defender a alguien de esa escoria es un placer."
    "Maddie explica lo de la menagerie de Capua otra vez."
    scene c20s002_075a with pixellate
    call BlinkXP ("c20s002_075" , "d") from _call_BlinkXP_3464
    mc "Espera, eso ya lo has explicado, ¿no?"
    mad "Sí, pero los personajes de ellas no estaban en la taberna. Aunque ellas estuvieran aquí por comodidad de todos, van a pretender que no lo saben si no lo explico con sus personajes presentes."
    mad "Hay algunos DMs, la mayoría, que hacen salir a los jugadores de la habitación cuando sus personajes no están."
    call BlinkXP ("c20s002_080" , "d") from _call_BlinkXP_3465
    dap "Yo lo hago, pero solo cuando es imprescindible y puede afectar a otras acciones simultáneas. Depende del tipo de escena o lo que vaya a durar, puede ser aburrido para las que están esperando."
    if persistent.family:
        dap "Tenemos un pacto entre damas para no usar lo que nuestros personajes no saben, como lo que te han dicho [eri] y [emm] de la madre de sus personajes."
    else:
        dap "Tenemos un pacto entre damas para no usar lo que nuestros personajes no saben, como lo que te han dicho [eri] y [emm] sobre cómo nacieron."
    mc "Ah, vale lo entiendo, mejor así. Si me mandas solo al salón, no te aseguro que no me quede dormido en el sofá. *Risa*"
    scene c20s002_085a with pixellate
    call BlinkXP ("c20s002_085" , "d") from _call_BlinkXP_3466
    dapd "Nosotras nos cruzamos con ese clérigo hace una semana. Estaba predicando en un pueblo minero a un par de días de aquí al que fuimos a ayudar... en un asunto."
    dapd "Allí todo el mundo es humano y no hay pelirrojas, con lo que no amenazó con quemar a nadie."
    call BlinkXP ("c20s002_090" , "d") from _call_BlinkXP_3467
    erid "Pero vimos cómo se las gastaba cuando nos vio. Es un fanático de esos que quieren exterminar a todas las razas del mundo y que vuelva a se totalmente humano, como dicen que era antaño."
    call BlinkXP ("c20s002_095" , "d") from _call_BlinkXP_3468
    emmd "Para hacer eso se necesitarían siglos de guerras, y él es un clérigo de Marte, el dios de la guerra, con lo que su dios estaría contento."
    emmd "Hay muchos como él dando vueltas por las fronteras del Imperio, provocando a la gente para que presionen a los gobernadores de las provincias fronterizas."
    emmd "Y la gente no es muy lista. Sólo quieren que su vecino Elfo se vaya al infierno. No ven las vidas inocentes que eso costaría."
    mcd "Eso es mezquino..."
    call BlinkXP ("c20s002_100" , "d") from _call_BlinkXP_3469
    scad "Sí, pero llevamos demasiados siglos de paz para el gusto de Marte y otros dioses de la guerra."
    scad "En Las Islas, los clérigos de nuestros dioses de la guerra llevan décadas queriendo invadir la Galia."
    mcd "Pero eso es territorio Enano. ¿Entraríais en guerra con ellos?"
    call BlinkXP ("c20s002_105" , "d") from _call_BlinkXP_3470
    scad "Los Enanos están al Este y al Sur de la Galia, nuestros clérigos quieren invadir las cuencas del Sequana (Sena) y del Liger (Loira), donde solo viven humanos."
    scad "Aunque pertenezcan a los Reinos Enanos, sólo son granjeros, casi esclavos. Los clérigos dicen que los \"liberaríamos\". En realidad pasarían a ser nuestros esclavos."
    mcd "Pero si los Enanos salen de sus montañas..."
    call BlinkXP ("c20s002_110" , "d") from _call_BlinkXP_3471
    scad "Siempre dicen que ¿qué es lo peor que nos puede pasar? Nos podrían hacer retroceder hasta el mar. Volveríamos a nuestras Islas y ya está."
    scad "No es que los Enanos vayan a hacer un tunel uniendo Britania y la Galia. *Risa* ¡Eso no se puede hacer!"
    scad "Por suerte para nosotros, nadie hace caso de los clérigos de los dioses de la guerra. Ni a nuestros reyes, siquiera. Somos demasiado independientes para eso."
    call BlinkXP ("c20s002_115" , "d") from _call_BlinkXP_3472
    madd "¿Y entre los Enanos y los Elfos? ¿Sabéis si sus dioses también están promoviendo la guerra?"
    call BlinkXP ("c20s002_120" , "d") from _call_BlinkXP_3473
    dapd "Los Enanos no lo necesitan. Están en guerra permanente entre ellos. Además, los Reinos de Carpathia y los de Caucasia están en una guerra defensiva con las hordas del Este."
    dapd "Los que quieren guerrear se van allí. Si no fuera por ellos, seguramente el Imperio estaría lleno de criaturas con la piel verde."
    call BlinkXP ("c20s002_125" , "d") from _call_BlinkXP_3474
    emmd "Y los Elfos llevan más de cien años queriendo recuperar Hispania pero, sin el apoyo del Emperador, no tienen nada que hacer."
    emmd "Pero viven más que las hadas, con lo que tienen paciencia. Casi todos ellos recuerdan aún cuando vivían allí y esperan que los Reinos Enanos se maten entre ellos."
    call BlinkXP ("c20s002_130" , "d") from _call_BlinkXP_3475
    erid "Entonces podrán volver y reinar sobre las ruinas. Muy élfico. Van de pacíficos comedores de flores, pero son unos rastreros que conspiran por la espalda."
    erid "Estoy segura de que tienen agentes promoviendo la guerra entre el Reino de los Pirineos y... ¿yo que sé?... no me sé el nombre de todos los Reinos Enanos."
    erid "A veces parece que hay uno debajo de cada puta colina del mundo."
    call BlinkXP ("c20s002_135" , "d") from _call_BlinkXP_3476
    scad "Si no recuerdo mal... *Hic* hay ocho o nueve reinos solo en Hispania. Pero lucharían como uno solo si alguien fuera a invadirlos."
    scad "Los que lucharon en La Conquista de Hispania ahora son los que dirigen el cotarro. *Hic*"
    mcd "Es decir, los Enanos peleando, los Elfos conspirando y los clérigos de Humanos y Hadas promoviendo la guerra... casi se puede ver un patrón, ¿no?"
    call BlinkXP ("c20s002_140" , "d") from _call_BlinkXP_3477
    madd "Desde luego, lo parece. Que los Elfos conspiren y que los Enanos peleen es normal. Pero si sumamos el resto..."
    madd "Parece que los dioses están jugando un juego en el que somos los peones."
    mcd "Lo que suele ser habitual..."
    call BlinkXP ("c20s002_145" , "d") from _call_BlinkXP_3478
    dapd "¿Pedimos algo para cenar? Tanto charlar me está dando hambre."
    call BlinkXP ("c20s002_150" , "d") from _call_BlinkXP_3479
    scad "Para mí no pidas nada. *Hic* Cogeré un trozo de lo tuyo... y ahora las monedas me las ahorro yo. *Risita*"
    mcd "Me parece una buena idea pedir la cena. Ha sido un día largo y mañana tenemos una larga cabalgata."
    call BlinkXP ("c20s002_155" , "f") from _call_BlinkXP_3480
    "Después de pedir la cena y que Marzia os la traiga..."
    emmd "Y a vosotros... ¿no os interesaría estableceros aquí?"
    emmd "Siempre van bien más manos... y armas... para defender los asentamientos de las montañas..."
    call BlinkXP ("c20s002_160" , "d") from _call_BlinkXP_3481
    madd "Yo, al menos, no tengo intención todavía de sentar la cabeza y establecerme en un sitio fijo. Hay mucho mundo que recorrer. Por eso me hice guardia de caravanas."
    mcd "A mí no me importaría establecerme algún día en algún sitio, pero creo que es pronto todavía."
    madd "Tengo una duda... Os han llamado Las Protectoras... ¿A qué se debe?"
    call BlinkXP ("c20s002_165" , "d") from _call_BlinkXP_3482
    dapd "A una combinación de estar en el lugar adecuado en el momento adecuado. Hace ocho años, una partida de Bárbaros del Norte atacaron el pueblo."
    dapd "Nunca hemos sabido cómo evitaron las patrullas la frontera. Pero era una partida pequeña, unos 20."
    dapd "Asaltaron los muros por la noche y quemaron el templo élfico de la plaza. Dicen que era bonito. No tocaron ningún otro edificio."
    dapd "Mataron a casi todos los hombres que intentaron defender el pueblo y se llevaron a casi todas las mujeres."
    call BlinkXP ("c20s002_170" , "d") from _call_BlinkXP_3483
    scad "Nosotras llegamos un par de días después, íbamos de paso... *Hic* a alguna parte."
    scad "Seguimos a la partida durante una semana, en los que iban dejando un rastro de destrucción."
    scad "Cuando los alcanzamos sólo quedaban unos 15 y llevaban más de 40 mujeres cautivas y varios niños, como Thiel, que no era de aquí, y el chico que se ha llevado el golpe de alabarda."
    call BlinkXP ("c20s002_175" , "d") from _call_BlinkXP_3484
    emmd "No podíamos dejar que se las llevaran, con lo que atacamos su campamento una noche y matamos a unos cuantos. El resto salió huyendo."
    emmd "Aunque fuera poco honorable, era necesario por un bien mayor."
    call BlinkXP ("c20s002_180" , "d") from _call_BlinkXP_3485
    erid "Rescatamos a las mujeres y las trajimos aquí. La mayoría era de Novum Templum al fin y al cabo."
    erid "Había algunas que no eran de aquí, como Thiel. Era un cachorrito negro monísimo por entonces. *Risa*"
    call BlinkXP ("c20s002_185" , "d") from _call_BlinkXP_3486
    scad "¡Eso es racista!"
    call BlinkXP ("c20s002_190a" , "d") from _call_BlinkXP_3487
    erid "No lo es. *Risa* Somos las únicas del pueblo que tenemos adornos en la cabeza. Sabes que adoro a la chica."
    call BlinkXP ("c20s002_190b" , "d") from _call_BlinkXP_3488
    erid "Nos ofrecieron una de las casas que habían quedado vacías, pero no podíamos aceptarlo, no pensábamos quedarnos."
    call BlinkXP ("c20s002_195" , "d") from _call_BlinkXP_3489
    emmd "Marzia nos ofreció entonces habitaciones en la posada. Las aceptamos por un par de semanas y ya llevamos ocho años aquí..."
    mc "*Tiempo Muerto* Espera... ¿Ocho años? ¿Qué edades tienen vuestros personajes?"
    scene c20s002_200a with pixellate
    call BlinkXP ("c20s002_200" , "d") from _call_BlinkXP_3490
    emm "Paula tiene 29 y Aelia, [eri], tiene 27. No soy muy buena dibujando chicas más adultas. Todas me salen muy jóvenes."
    scene c20s002_200d with dissolve
    dap "Pia tiene 43 pero aparenta 30 y pocos. Piensa que, en esos 8 años, casi no hemos salido de aventuras. Hemos ayudado a reconstruir el pueblo y poco más."
    sca "Beagan aparenta 31 años humanos... 126 años reales."
    sca "La edad de Beagan puede salir en la conversación y hacer como que lo sabes. Todo el mundo sabe que las hadas envejecen lento."
    mc "¡Joder! Yo os imaginaba como sois ahora... Vilfredo tiene 21, soy el más joven, ¿no?"
    call BlinkXP ("c20s002_205" , "d") from _call_BlinkXP_3491
    mad "Conmigo lo has acertado. Fang tiene mi edad. Pero no hace falta que las imagines más viejas. Cómo ves tú a los personajes en tu mente sólo depende de ti."
    mcp "(Como ha pasado con vuestras armaduras o con Júpiter, claro. Es más fácil seguir imaginándoos tal y como sois.)"
    mc "Ok, ¿seguimos? El mundo me está pareciendo super interesante."
    scene c20s002_195a with pixellate
    call BlinkXP ("c20s002_195" , "d") from _call_BlinkXP_3492
    emmd "Como te decía, nos ofrecieron habitaciones. Desde entonces hemos ayudado a las mujeres del pueblo a recuperarse. Pero faltan hombres. Muchos hombres."
    emmd "Somos más de 50 mujeres y sólo hay once hombres. Y la mayoría eran niños hace 8 años."
    mcd "Eso podría ser tentador para más de un hombre..."
    call BlinkXP ("c20s002_210" , "d") from _call_BlinkXP_3493
    dapd "El Consejo de Mujeres incluso aprobó una ley para que un hombre pudiera vivir con más de una mujer, pero eso no ha atraído a muchos. Solo a un forastero."
    dapd "Se marchó seis meses después. Dijo que si era malo tener una jefa como mujer, tener dos que, además, no se ponían de acuerdo, era lo peor que había vivido."
    mcd "*Risa* Puedo entenderle..."
    "Todas te miran con una ceja levantada. No a Vilfredo. A ti."
    mcd "No porque sean mujeres, sino porque servir a dos amos que dan órdenes contradictorias es complicado."
    eri "*Tiempo Muerto* Bien salvado... *Risa*"
    if mc._var("relationships")>1:
        emm "*Tiempo Muerto* Parecía que te arrepentías del harén. *Risa*"
        mc "*Tiempo Muerto* De eso nunca me arrepentiré. *Risa*"
    scene c20s002_210An with dissolve
    "Pasáis un rato en el que os explican a Maddie y a ti más cosas del mundo que [dap] ha diseñado, del pueblo, de los conflictos, de la política."
    "[dap] ha hecho un mundo creíble y profundo basado en una premisa muy original."
    "Durante casi toda la conversación, se mantienen fieles a sus personajes, solo haciendo la señal de Tiempo Muerto cuando tienen que aclarar algo que sus personajes no pueden decir."
    "[emm] lo ve todo desde un punto de vista honorable, mientras Scarlett lo ve desde un punto de vista travieso. [eri] parece tener una perspectiva más cínica."
    "[dap] actua de forma diferente. Siendo la DM a la vez que un personaje, no muestra juicios absolutos. Supones que, al saber todo lo que pasa y el por qué, mantiene la distancia."
    "[dap] os indica que se está haciendo tarde."
    call BlinkXP ("c20s002_215" , "d") from _call_BlinkXP_3494
    madd "Creo que yo voy a retirarme a mi habitación ya. La compañía es grata pero mañana tenemos una larga cabalgata. Y Vilfredo cabalga lento como un viejo Halfling."
    stop music fadeout (1.5)
    mcd "Ja. Ja. Yo también voy a irme a la cama. Fang tiene razón. Mañana tenemos que madrugar para llegar a Vindobona. Y no cabalgo tan lento."
    return
label c20s002_AMosquitoe: #4
    if _in_replay:
        call c20_DefineCharacters from _call_c20_DefineCharacters_3
        menu:
            "¿Estás en una relación con Scarlett?"
            "Sí":
                $ sca._var("route" , True)
            "No":
                $ sca._var("route" , False)
    scene c20s002_300a with pixellate
    play music ("music/ChillUkelele.ogg")
    call BlinkXP ("c20s002_300" , "d") from _call_BlinkXP_3495
    dap "Vale, mandadme un mensaje con lo que queréis hacer durante la noche. Puede ser dormir, salir a ver el pueblo de noche... lo que queráis dentro de la lógica."
    "Escribes un mensaje en el que indicas que vas a dormir. [dap] te pregunta si vestido o desnudo. Desnudo, obviamente."
    "Todas las chicas mandan sus mensajes y [dap] tira unos dados detras de la pantalla del DM."
    call BlinkXP ("c20s002_305" , "d") from _call_BlinkXP_3496
    dap "[eri] y [emm], tenéis que abandonar la habitación un momento. Os aviso cuando podáis volver. Maddie, tú puedes quedarte o irte con [emm] y [eri], como quieras."
    "Maddie se queda."
    dap "Fang y Vilfredo suben a sus habitaciones. Son habitaciones sencillas pero limpias, con la chimenea encendida y mezcla de muebles de diferentes épocas. Os preparáis para dormir."
    dap "Scarlett, vamos a hacer esto por mensaje..."
    scene c20s002_305d with dissolve
    "Las chicas empiezan a escribirse mensajes la una a la otra. No entiendes nada por un momento."
    "Scarlett de vez en cuando tira un dado. Tras la tercera tirada pone mala cara."
    call BlinkXP ("c20s002_310" , "d") from _call_BlinkXP_3497
    dap "¿Qué percepción pasiva tenías, [mc]?"
    mc "Diez."
    call BlinkXP ("c20s002_315" , "d") from _call_BlinkXP_3498
    dap "Cuando estás a punto de quedarte dormido, oyes un zumbido parecido al de un mosquito en tu oreja derecha."
    mc "Lo aparto."
    stop music fadeout (1.5)
    dap "Tira el d20. 14. Le das un golpe al \"mosquito\"."
    scene c20s002_320a with pixellate
    scene c20s002_320An
    play music ("music/SensualJazzMedium2.ogg")
    scad "¡Ahhhhh!"
    mcd "¿Beagan? ¿Qué haces en mi habitación?"
    if not _in_replay:
        $ sca.profileImages.pop (12) # first remove
        $ sca.profileImages.insert (12, ("scarlett_12", None)) # then add new
        $ renpy.notify ("Profile Image unlocked for Scarlett: 12 - DnD Lingerie")
    call BlinkXP ("c20s002_325" , "d") from _call_BlinkXP_3499
    scad "Bueno... Como sé que mañana te marchas... y como sabes que hay pocos hombres en la zona... había pensado..."
    mcd "Habías pensado... ¿Qué?"
    call BlinkXP ("c20s002_330" , "d") from _call_BlinkXP_3500
    scad "¿Sexo sin compromiso? *Risa*"
    scad "Sé que suena un poco desesperado, pero... por si te apetecía..."
    if persistent.walkthrough:
        $ wt1 = _("Escena sexual con Beagan. \nPosiblemente también con [dapd], [erid], y [emmd]. \nNo está vinculada con tus relaciones en el mundo real.")
        $ wt2 = _("Una noche sin sexo para Vilfredo.")
    else:
        $ wt1 = ""
        $ wt2 = ""
    menu:
        "Me parece bien." (wt = wt1):
            $ sca._var("rejectedBeagan" , False)
            call c20s003_SexWithBeagan from _call_c20s003_SexWithBeagan
        "Lo siento Beagan." (wt = wt2):
            $ sca._var("rejectedBeagan" , True)
            mcd "Por muy exótico que pueda parecerme, no concibo el sexo sin sentimientos."
            call BlinkXP ("c20s002_335" , "d") from _call_BlinkXP_3501
            scad "Lo entiendo... Bueno, no lo entiendo... la razón de ser del sexo es divertirse."
            mcd "Tenemos formas diferentes de verlo, Beagan."
            call BlinkXP ("c20s002_340" , "d") from _call_BlinkXP_3502
            scad "Entonces... hasta mañana, ¿no?"
            mcd "Sí, nos veremos mañana para despedirnos antes de emprender camino a Vindobona."
            stop music fadeout (1.5)
            scene c20s003_005aa with pixellate
            call BlinkXP ("c20s003_005a" , "d") from _call_BlinkXP_3503
            dap "Scarlett, sales de la habitación sintiéndote un poco estúpida."
    $ resetWalkthrough ()
    return
label c20s003_DevilAngelTeam: #5
    if _in_replay:
        menu:
            "¿Rechazaste a Beagan, el Hada de Scarlett?"
            "No":
                $ sca._var("rejectedBeagan" , False)
            "Sí":
                $ sca._var("rejectedBeagan" , True)
        call c20_DefineCharacters from _call_c20_DefineCharacters_4
        call BlinkXP ("c20s003_005a" , "d") from _call_BlinkXP_3504d
    if not sca._var("rejectedBeagan"):
        scene c20s003_005aa with pixellate
        call BlinkXP ("c20s003_005a" , "d") from _call_BlinkXP_3504
    play music ("music/ChillUkelele.ogg")
    dap "Voy a avisar a [eri] y [emm]. Podéis quedaros o iros. Será corto."
    "Cuando llegan las chicas, os quedáis todos."
    call BlinkXP ("c20s003_005b" , "f") from _call_BlinkXP_3505
    dap "Bueno, [eri], explica que haces."
    call BlinkXP ("c20s003_010" , "d") from _call_BlinkXP_3506
    eri "Aelia se viste con el traje negro sexy que compró en Carnuntum y va a visitar a Paula, como ya te he escrito en el mensaje."
    call BlinkXP ("c20s003_015" , "d") from _call_BlinkXP_3507
    dap "OK, [emm]. Tu también me has dicho que te vestías sexy y esperabas a Aelia."
    dap "Suena tu puerta."
    call BlinkXP ("c20s003_020" , "d") from _call_BlinkXP_3508
    bet "Vuestro concepto de sexy es diferente del que teníamos en mi época. *Risa* No creo que esos pijamas puedan excitar a nadie, quizás el de [emm]."
    mc "Se refieren a sus personajes, Tía Betty. Y veo que tú has traído la costumbre del topless a casa, ¿no? *Risa*"
    call BlinkXP ("c20s003_025" , "d") from _call_BlinkXP_3509
    bet "Ya sabes que [nor] aprobó que cada cual fuera como quisiera en casa. Hoy hace calor y no vais a ver nada que no hayáis visto esta tarde."
    mc "Tienes razón..."
    bet "Creía que ya habríais acabado. Sólo bajaba a por un vaso de agua. ¿Puedo quedarme?"
    call BlinkXP ("c20s003_030" , "d") from _call_BlinkXP_3510
    bet "Si queréis puedo ir a ponerme algo..."
    mcp "(Se acaba de dar cuenta de que posiblemente esté haciendo que las chicas no se sientan cómodas. La fiesta topless ya ha acabado.)"
    mc "Por mí no hay problema. Como has dicho, no vamos a ver nada que no hayamos visto hoy."
    call BlinkXP ("c20s003_035" , "d") from _call_BlinkXP_3511
    eri "No es necesario, Tía Betty..."
    scene c20s003_040An with dissolve
    eri "Como has dicho... hace calor."
    mcp "([eri], como siempre, intentando que todo el mundo se sienta cómodo.)"
    call BlinkXP ("c20s003_045" , "d") from _call_BlinkXP_3512
    dap "Sí, después de llevarlas libres todo el día, casi me siento incómoda llevándolas tapadas. *Risa*"
    call BlinkXP ("c20s003_050" , "d") from _call_BlinkXP_3513
    emm "¿Ves, Tía Betty? No hace falta que estés incómoda si quieres quedarte."
    mcp "([emm], como siempre, con la sutileza de un ariete.)"
    call BlinkXP ("c20s003_055" , "d") from _call_BlinkXP_3514
    sca "*Risa* Conmigo no contéis. No llevo bragas debajo del camisón."
    call BlinkXP ("c20s003_060" , "d") from _call_BlinkXP_3515
    mad "Y, si no os importa, yo voy a conservar la camiseta... Al menos para que Scarlett no se sienta incómoda. *Risa*"
    mcp "(Si Maddie se sentía un poco incómoda con el topless al principio, quizás esto sea demasiado para ella en su primer día en casa.)"
    call BlinkXP ("c20s003_065" , "d") from _call_BlinkXP_3516
    bet "Oh, genial entonces. Me sentaré aquí e intentaré no estorbar."
    stop music fadeout (1.5)
    scene c20s003_070e with pixellate
    dap "*En el mundo real* Bueno, continuemos. [emm], alguien llamaba a la puerta de Paula."
    play music ("music/dnd/the-capital-city.ogg")
    emm "*En el mundo real* Voy a abrir."
    scene c20s003_070d with dissolve:
        yalign 1.0
        linear 5.0 yalign 0.0
    pause (5.0)
    call BlinkXP ("c20s003_070" , "d") from _call_BlinkXP_3517
    erid "Venia a buscarte... chico nuevo en el pueblo y esas cosas."
    if not _in_replay:
        $ eri.profileImages.pop (12) # first remove
        $ eri.profileImages.insert (12, ("erika_12", None)) # then add new
        $ texto = str(eri.name)
        $ renpy.notify ("Profile Image unlocked for "+str(texto)+": 12 - DnD Lingerie")
    scene c20s003_075d with dissolve
    emmd "Sabía que vendrías. Pero esta vez no voy a caer en tu trampa."
    call BlinkXP ("c20s003_075" , "d") from _call_BlinkXP_3518
    erid "Nadie lo diría por como te has vestido."
    scene c20s003_080d with dissolve:
        yalign 1.0
        linear 5.0 yalign 0.0
    pause (5.0)
    call BlinkXP ("c20s003_080" , "d") from _call_BlinkXP_3519
    if not _in_replay:
        $ emm.profileImages.pop (12) # first remove
        $ emm.profileImages.insert (12, ("emma_12", None)) # then add new
        $ texto = str(emm.name)
        $ renpy.notify ("Profile Image unlocked for "+str(texto)+": 12 - DnD Lingerie")
    emmd "Porque sabía que vendrías y te pondrías insistente."
    emmd "No quiero caer en tu trampa, pero tampoco quiero que discutamos como aquella vez en Mediolanum (Milán)."
    call BlinkXP ("c20s003_085" , "d") from _call_BlinkXP_3520
    erid "Entonces, ¿hace falta que intente convencerte?"
    call BlinkXP ("c20s003_090" , "d") from _call_BlinkXP_3521
    emmd "Una chica puede estar buscando el amor de su vida y no por ello renunciar al sexo casual, ¿no?"
    call BlinkXP ("c20s003_095" , "d") from _call_BlinkXP_3522
    erid "*Risa* A mí no me lo preguntes, pregúntaselo a tu diosa y a tus votos."
    erid "Yo voy a intentar follarme a ese SemiElfo. Algo bueno tenían que hacer los elfos..."
    scene c20s003_100AnBlink with dissolve
    erid "¿Vienes?"
    call BlinkXP ("c20s003_105" , "d") from _call_BlinkXP_3523
    emmd "¡Oh, Vesta! ¡Perdóname porque la carne es débil!"
    stop music fadeout (1.5)
    scene c20s003_110a with pixellate
    call BlinkXP ("c20s003_110" , "d") from _call_BlinkXP_3524
    bet "*Risa* ¡Qué poco hubieras durado como monja!"
    play music ("music/ChillUkelele.ogg")
    call BlinkXP ("c20s003_115" , "d") from _call_BlinkXP_3525
    emm "*Risa* Paula, mi personaje, siempre ha tenido algunos problemas con sus votos. El sexo está permitido, no es una virgen Vestal, pero lo recomendado es..."
    call BlinkXP ("c20s003_120" , "d") from _call_BlinkXP_3526
    eri "No follarte todo lo que se mueva. *Risa* Por suerte para Paula, solo es una recomendación."
    call BlinkXP ("c20s003_125" , "d") from _call_BlinkXP_3527
    emm "Vesta es la diosa del hogar y la fidelidad, no de las mojigatas reprimidas. *Risa*"
    call BlinkXP ("c20s003_130" , "d") from _call_BlinkXP_3528
    emm "¡Oops! ¡Lo siento, Tía Betty! No quería decir que las monjas fuerais mojigatas reprimidas."
    call BlinkXP ("c20s003_135" , "d") from _call_BlinkXP_3529
    bet "*Risa* No pasa nada, cielo. Eso se aplica al 99\% de monjas. Y no preguntes por el otro 1\%."
    stop music fadeout (1.5)
    todas "*Risa*"
    if sca._var("rejectedBeagan"):
        scene c20s003_140a with pixellate
        call BlinkXP ("c20s003_140" , "d") from _call_BlinkXP_3530
        play music ("music/dnd/the-capital-city.ogg")
        dap "*En el mundo real* Bueno, sigamos. Cuando salís al pasillo os encontráis con Beagan."
        scad "No hace falta que vayáis. Me ha dicho que no quiere sexo sin sentimientos."
        call BlinkXP ("c20s003_145" , "d") from _call_BlinkXP_3531
        emmd "¿Nos lo podemos quedar?"
        call BlinkXP ("c20s003_150" , "d") from _call_BlinkXP_3532
        erid "¿Ya lo has intentado, Beagan? Eres rápida para ser tan pequeña..."
        call BlinkXP ("c20s003_155" , "d") from _call_BlinkXP_3533
        if persistent.family:
            scad "Yo no tenía una hermana a la que convencer. *Risa* Eres muy lenta para cruzar el pasillo."
        else:
            scad "Yo no tenía una Paladín a la que convencer. *Risa* Eres muy lenta para cruzar el pasillo."
        call BlinkXP ("c20s003_160" , "d") from _call_BlinkXP_3534
        erid "Pues entonces, cada una a su habitación, ¿no?"
        call BlinkXP ("c20s003_165" , "d") from _call_BlinkXP_3535
        scad "Si tú quieres puedes venir a la mía..."
        call BlinkXP ("c20s003_170" , "d") from _call_BlinkXP_3536
        erid "Eso pasó una vez y te dije que no volvería a pasar. No volverás a pillarme borracha."
        call BlinkXP ("c20s003_175" , "d") from _call_BlinkXP_3537
        emmd "Sois unas pervertidas..."
        call BlinkXP ("c20s003_180" , "d") from _call_BlinkXP_3538
        scad "Y tú una aburrida. *Risa* ¡Hasta mañana!"
        scene c20s003_180d with dissolve
        erid "Hasta mañana, Hada traviesa."
        emmd "Buenas noches, Hada putilla."
        call BlinkXP ("c20s003_185" , "d") from _call_BlinkXP_3539
        mcp "(Si el personaje de [dap] no viene a mi habitación, me la puedo imaginar escuchando detrás de la puerta la conversación de estas tres.)"
        stop music fadeout (1.5)
        dapdd "*Susurrando* ¡Mierda!"
        if not _in_replay:
            $ dap.profileImages.pop (12) # first remove
            $ dap.profileImages.insert (12, ("daphne_12", None)) # then add new
            $ texto = str(dap.name)
            $ renpy.notify ("Profile Image unlocked for "+str(texto)+": 12 - DnD Lingerie")
    return
label c20s003_SexWithBeagan: #4
    call BlinkXP ("c20s003_200" , "h") from _call_BlinkXP_3540
    scad "¿Qué? ¿Así? ¿Nada de \"solo busco a mi amor verdadero\" y cosas por el estilo?"
    mcd "Bueno, lo estoy buscando, pero la búsqueda puede ser divertida, ¿no?"
    call BlinkXP ("c20s003_205" , "d") from _call_BlinkXP_3541
    scad "*Risa* Me gusta como piensas."
    sca "*Tiempo muerto* Ermmm... [dap]..."
    scene c20s003_210a with pixellate
    call BlinkXP ("c20s003_210" , "d") from _call_BlinkXP_3542
    sca "¿Tenemos que interpretar la escena? No creía que [mc] fuera a aceptar..."
    mc "*Risa* Ha aceptado Vilfredo, no yo."
    call BlinkXP ("c20s003_215" , "d") from _call_BlinkXP_3543
    dap "Supongo que no hace falta... las otras veces que alguna de vosotras se ha follado viajeros... sólo hemos tirado a ver si se quedaba embarazada."
    dap "No sabría ni cómo jugar esto de otra forma..."
    call BlinkXP ("c20s003_220" , "d") from _call_BlinkXP_3544
    mad "Mi antiguo DM nos hacía describir el sexo sólo si hacíamos algo fuera de lo común. El resto es responsabilidad de la imaginación del jugador."
    mc "No me parece una mala idea. Dejaré que empiece Scarlett, en caso de que tenga alguna idea curiosa, siendo un hada."
    call BlinkXP ("c20s003_225" , "d") from _call_BlinkXP_3545
    sca "Es buena idea. Vilfredo dormía desnudo, ¿no?"
    mc "Sí, ni siquiera en mi imaginación puedo forzarme a dormir vestido. *Risa*"
    sca "Entonces..."
    scene c20s003_230pv with pixellate
    show c20s003_230v
    sca "*En el mundo real* Beagan se abraza a la polla de Vilfredo como si fuera un árbol, subiendo y bajando por toda su longitud."
    "Empiezas a imaginar lo placentero que podría ser algo así. Lo es y mucho."
    "No hace falta describir el resto del encuentro. Tu imaginación se encarga de ello, ayudada por cada comentario de Scarlett. El resto del encuentro se muestra en tu cabeza."
    scadd "¿Te gusta esto?"
    "Puedes imaginar la sensación y tiene que ser placentera."
    if sca._var("route"):
        "Conoces perfectamente el cuerpo de Scarlett e imaginas cómo su cuerpo rozaría con tu polla."
    "También puedes imaginar que pasaría si su vestido sufriera un problema y sus pechos quedasen al aire."
    scene c20s003_235pv with dissolve
    hide c20s003_230v
    show c20s003_235v
    "Dicho y hecho, es fácil de imaginar."
    mcdd "Me encanta, Beagan. Mucho mejor ahora."
    "Notar sus pechos deslizándose por tu ástil mejora mucho la sensación."
    scadd "Tienes una mente traviesa, Vilfredo. Me encanta."
    "Sería mejor incluso sin nada de ropa."
    scene c20s003_240d with dissolve
    hide c20s003_235v
    pause (0.8)
    scene c20s003_240e with dissolve
    pause (0.7)
    call BlinkXP ("c20s003_240" , "d") from _call_BlinkXP_3546
    scadd "Eso es fácil de conseguir, recuerda que soy una hechicera."
    "Parece que te lea la mente."
    scadd "Es que te la leo. Esto está pasando en tu imaginación tan solo. En el mundo real están pasando otras cosas a las que no estás prestando atención."
    "Pues tiene razón. Hace un par de minutos que no prestas atención a lo que se dice alrededor de la mesa."
    scene c20s003_245a with pixellate
    call BlinkXP ("c20s003_245" , "d") from _call_BlinkXP_3547
    sca "Utilizo la habilidad de cambiar de tamaño de formas imaginativas... "
    mcp "(Creo que es momento de volver a mis ensoñaciones y ver... imaginar a qué se refiere.)"
    scene c20s003_250pv with pixellate
    show c20s003_250va
    pause (4.0)
    scene c20s003_250dv
    "Beagan realmente utiliza de forma imaginativa sus cambios de tamaño."
    "Pasa de su tamaño hada a su tamaño humano sin separar sus labios de tu glande."
    "Finaliza el movimiento introduciéndose tu polla hasta la garganta."
    scene c20s003_250pvb with dissolve
    hide c20s003_250va
    show c20s003_250vb
    "Empieza entonces una mamada lenta pero profunda."
    sca "*En el mundo real* Beagan utiliza el cambio de tamaño para encoger un poco en el camino de subida, de forma que la garganta haga más presión."
    mcp "(¡Wow! Eso tiene que sentirse increíble.)"
    if sca._var("route"):
        mcp "(Parece mentira que hace tan solo dos semanas no tuviera ninguna experiencia en cuanto a sexo se refiere.)"
    "La sensación es increíble, o imaginas cómo de increíble debe ser, con sus tatuajes iluminándose en cada recorrido cada vez que cambia su tamaño."
    "Es imperceptible a la vista, pero totalmente perceptible a lo largo de tu polla."
    mcp "(¡Alucinante! Creía que sería difícil para mí imaginar todo esto... pero es casi como si estuviera allí.)"
    "No crees que puedas aguantar mucho más."
    call BlinkXP ("c20s003_270" , "d") from _call_BlinkXP_3550
    hide c20s003_250vb
    scadd "¿Tienes ganas de que te cabalgue un hada? ¿Lo has probado alguna vez?"
    mcdd "Sí y no. Pero estoy ansioso por hacerlo."
    scadd "Mejor, con las alas se me da mal la postura del prosélito (misionero). *Risa* Me siento aprisionada."
    call BlinkXP ("c20s003_280" , "f") from _call_BlinkXP_3551
    "Beagan te cabalga, apoyando tu glande contra la entrada de su coño, manteniéndose en el aire con un ligero aleteo."
    "No te cuesta imaginar que los pesos y las presiones son totalmente diferentes a como suelen ser con una humana."
    scadd "¿Preparado?"
    mcdd "Nunca lo he estado más."
    show c20s003_275v
    pause (1.6)
    scene c20s003_275dv
    hide c20s003_275v
    "Beagan se deja caer, empalándose en tu polla mientras aletea para reducir la velocidad del descenso."
    scadd "¡Oh, por Lugh! ¡Ahora entiendo lo que se debe sentir al ser una brocheta!"
    "Tú te sientes como el relleno de un pavo... o de un pollo. No había pavos en Europa en aquella época. El coño de Beagan es mas estrecho de lo que creías."
    call BlinkXP ("c20s003_285" , "d") from _call_BlinkXP_3552
    scadd "Dame un momento para que me acostumbre a esto... No puedo bajar del todo..."
    mcdd "Tómate todo el tiempo que necesites, no tenemos demasiada prisa..."
    call BlinkXP ("c20s003_290" , "d") from _call_BlinkXP_3553
    scadd "Si alguna vez te quedas sin trabajo... otra vez... en las legiones siempre necesitan arietes... *Risa*"
    mcdd "*Risa* No creo que sea para tanto..."
    scadd "Tu nunca has tenido algo como eso dentro de ti... supongo... con los elfos nunca se sabe... *Risa* Y tú eres SemiElfo."
    call BlinkXP ("c20s003_295" , "d") from _call_BlinkXP_3554
    scadd "Voy a empezar a moverme... espero poder andar después de esto. Y si no puedo... tengo alas..."
    mcdd "Cuando quieras, pero yo no te recomendaría cambiar de tamaño ahora... ya está muy justo..."
    call BlinkXP ("c20s003_300" , "d") from _call_BlinkXP_3555
    scadd "*Risa* Estoy un poco loca. Pero solo un poco, no tanto como para hacer eso..."
    scene c20s003_255pv with dissolve
    "Beagan empieza a moverse, con movimientos cortos, a un ritmo muy placentero."
    show c20s003_255v
    scadd "¡Wow! *Gemido* Si dejase de aletear por un momento llegarías a mi estómago..."
    "Tiene razón, puedes notar tu polla impactando en su cérvix al final de cada uno de los recorridos."
    mcdd "Entonces será mejor que no dejes de hacerlo. *Risa* Hay mucha cerveza ahí."
    "Sus aleteos provocan diferentes sensaciones en tu cuerpo. Es como follar con el aire acondicionado a toda velocidad."
    "Además, hacen que Beagan sea ligera como una pluma."
    scene c20s003_260pv with dissolve
    hide c20s003_255v
    show c20s003_260v
    scadd "*Jadeo* Me estoy poniendo más cachonda que una dragona en celo. *Gemido*"
    "Eso debe ser un montón de calor, ¿no? Es la primera vez que oyes esa expresión, pero también es la primera vez que te follas un hada."
    scadd "*Gemido* Si sigues así, me vas a destrozar... *Jadeo* Afortunadamente, no necesito montar un caballo..."
    "Las bromas durante el sexo parecen encajar con el carácter travieso del hada."
    mcdd "Es lo bueno de tener alas. No vas a necesitar usar las piernas en los próximos días..."
    scene c20s003_265pv with dissolve
    hide c20s003_260v
    show c20s003_265v
    scadd "*Gemido* No podría usarlas aunque quisiera. Ni siquiera juntarlas... *Jadeo* Voy a acabar con agujetas en las alas."
    "Puedes notar como el coño faérico empieza a estrujar tu polla con más fuerza. Sus tatuajes no brillan, con lo que no está cambiando de tamaño."
    scadd "*Jadeo* Estoy a punto de correrme, Vilfredo."
    "No era un cambio de tamaño, sino su vagina preparándose para no desperdiciar ni una sola gota de tu leche."
    scadd "*GEMIDO* ¡Está llegando!"
    sca "*En el mundo real* Por cierto, [mc]... cuando Beagan tiene un orgasmo..."
    call OrgasmX ("c20s003_305") from _call_OrgasmX_71
    hide c20s003_260v
    sca "*En el mundo real* ...¡Brilla!"
    scadd "*JADEO* ¡OH, SÍ! ¡POR LUGH!"
    "El brillo intenso de Beagan se transforma en calor en el interior de su vagina. Un calor que, unido a sus contracciones, te provocan un orgasmo instantáneo."
    scadd "*GEMIDO* ¡Córrete dentro de mí!" (multiple=2)
    sca "*En el mundo real* Córrete dentro" (multiple=2)
    "Arriesgada decisión con un tipo que se va a ir al día siguiente. ¿Pueden las Hadas y los SemiElfos tener hijos?"
    "De todas formas, no tienes elección."
    call OrgasmX ("c20s003_310") from _call_OrgasmX_72
    mcdd "¡Mpfft!"
    "Descargas una gran cantidad de leche en el interior del hada."
    scadd "*JADEO* ¡Dáme toda tu leche!"
    "En algún lugar lejano, en el mundo real, puedes oír como [dap] tira unos dados."
    play sound ("music/OldMusicBox5.ogg")
    scene c20s003_315a with pixellate
    call BlinkXP ("c20s003_315" , "d") from _call_BlinkXP_3556
    dap "¿Qué sale de un Hada y un SemiElfo? ¿Un semihadelfo? *Risa*"
    mc "¿La he dejado embarazada?"
    dap "Según esta tabla, incluso con todos los penalizadores por razas diferentes... sí. Vilfredo va a ser padre, aunque él no lo sepa."
    call BlinkXP ("c20s003_320" , "d") from _call_BlinkXP_3557
    sca "Mañana se va a Vindobona. ¡A saber si alguna vez se entera! *Risa*"
    mc "Me voy, pero volveré." #I shall return
    sca "[dap] se encargará de darte razones para ello. *Risa*"
    scene c20s003_325a with pixellate
    call BlinkXP ("c20s003_325" , "d") from _call_BlinkXP_3558
    "Vuelves a tus ensoñaciones justo cuando Beagan se derrumba encima tuyo, sus alas y tatuajes todavía brillando mientras las últimas oleadas de orgasmos recorren su cuerpo."
    scadd "¡Ha sido espectacular!"
    mcdd "Lo que ha sido espectacular ha sido lo de tus alas. ¡Wow!"
    call BlinkXP ("c20s003_330" , "d") from _call_BlinkXP_3559
    scadd "Es muy bonito, como una explosión de luz cuando mi cuerpo explota de placer."
    "Sus alas y tatuajes siguen brillando en flashes con la llegada de oleadas de pequeños orgasmos."
    mcdd "Aunque supongo que tiene contrapartidas. No puedes fingir un orgasmo..."
    call BlinkXP ("c20s003_335" , "d") from _call_BlinkXP_3560
    scadd "Esa es parte de la maldición. La bruja que me la echó era muy mala con la lengua y no le gustó que fingiera para hacerla sentir mejor."
    scadd "Ahora no puedo engañar a nadie, aunque contigo no ha sido necesario."
    mcdd "Espera... ¿Es una maldición? Debe ser la maldición más bonita de la historia."
    call BlinkXP ("c20s003_340" , "d") from _call_BlinkXP_3561
    scadd "*Risa* Bueno, sí y no. Es imposible hacer algunas cosas sin que se entere nadie cuando nos vamos de aventuras y tenemos que acampar al raso."
    "Dice mientras se lleva la mano a su clítoris."
    scadd "La vida del aventurero puede ser muy solitaria... *Risa*"
    mcdd "*Risa* Perder privacidad y ganar en belleza... difícil elección."
    stop music fadeout (1.5)
    scene c20s003_345d with dissolve
    dap "*En el mundo real* Después de estar abrazándoos un poco... supongo que lo hacéis si no decís lo contrario... alguien llama a la puerta."
    play sound ("music/knock.ogg")
    "*Knock-knock*"
    dapd "*A través de la puerta* Soy Pia, ¿puedo pasar?"
    mcd "Dame un segundo... estoy desnudo..."
    mad "*En el mundo real* Tu habitación parece una estación de metro. ¿Es Fang la única que se ha ido a dormir?"
    dap "*En el mundo real* Sí. *Risa*"
    scene c20s003_345An with vpunch #abc
    scad "*Susurrando* Déjame esconderme... si me pilla aquí va a echarme la bronca porque dice que soy demasiado putilla..."
    mcd "*Susurrando* Escóndete en el armario. Yo voy a taparme..."
    scene c20s003_350An with dissolve # Beagan se esconde en el armario. abcde
    scad "*Susurrando* Ya..."
    scene c20s003_345d with dissolve
    return
label c20s003_SexWithPia: #6
    if _in_replay:
        call c20_DefineCharacters from _call_c20_DefineCharacters_5
    scene c20s003_345d with dissolve
    play music ("music/dnd/chivalry-fair.ogg")
    mcd "Pasa, Pia."
    call BlinkXP ("c20s003_355" , "f") from _call_BlinkXP_3562
    dap "*En el mundo real* Entra Pia con un... pijama... tipo oriental, como de bailarina de los siete velos. Y un saco de comida."
    dapd "Perdona que te moleste a estas horas, pero... Marzia ha preparado unas provisiones para vuestro viaje de mañana."
    mcd "¡Oh! Gracias, Pia. ¿Puedes dejarlas ahí, encima de la silla, por favor?"
    mcd "No me puedo levantar ahora mismo..."
    call BlinkXP ("c20s003_360" , "d") from _call_BlinkXP_3563
    dapd "Es cierto... estás desnudo debajo de la manta..."
    mcd "Si te molesta, puedo ponerme algo..."
    call BlinkXP ("c20s003_365" , "d") from _call_BlinkXP_3564
    dapd "¡No, no! Estás en tu habitación... no debería decirte como debes estar."
    mcd "Veo que tú también te has puesto cómoda para pasar la noche..."
    scene c20s003_370d with dissolve:
        yalign 1.0
        linear 5.0 yalign 0.0
    pause (5.0)
    call BlinkXP ("c20s003_370" , "d") from _call_BlinkXP_3565
    if not _in_replay:
        $ dap.profileImages.pop (12) # first remove
        $ dap.profileImages.insert (12, ("daphne_12", None)) # then add new
        $ texto = str(dap.name)
        $ renpy.notify ("Profile Image unlocked for "+str(texto)+": 12 - DnD Lingerie")
    dapd "¿Te gusta? Se lo compré a un comerciante de Petra. Es fresco para dormir... y muy bonito..."
    if persistent.walkthrough:
        $ wt1 = _("Escena sexual con Pia. \nNo está vinculada con tus relaciones en el mundo real.")
        $ wt2 = _("Sin consecuencias.")
    else:
        $ wt1 = ""
        $ wt2 = ""
    menu:
        "Y muy sexy." (wt = wt1):
            $ dap._var("rejectedPia" , False)
        "Supongo que para dormir está bien." (wt = wt2):
            $ dap._var("rejectedPia" , True)
            mcd "Que es lo que debería hacer yo."
            call BlinkXP ("c20s003_375" , "d") from _call_BlinkXP_3566
            dap "*En el mundo real* Ves como una expresión de decepción pasa por la cara de Pia un momento antes de volver a sonreír."
            call BlinkXP ("c20s003_380" , "d") from _call_BlinkXP_3567
            dapd "Bueno, pues voy a dejar que descanses o si no, mañana te va a costar mucho cabalgar hasta Vindobona."
            dapd "Buenas noches, Vilfredo."
            mcd "Buenas noches, Pia."
            scene c20s003_345d with dissolve
            "*Blam*"
            mcd "Me parece que la he ofendido de algún modo..."
            call BlinkXP ("c20s003_385" , "d") from _call_BlinkXP_3568
            scad "Venía a lo mismo que yo, pero Pia no es tan directa... Ella se lo pierde..."
            scad "¿Puedo salir ya?"
            stop music fadeout (1.5)
            mcd "Supongo. Podemos continuar donde lo hemos dejado..."
            return
    $ resetWalkthrough ()
    call BlinkXP ("c20s003_390" , "d") from _call_BlinkXP_3569
    stop music fadeout (1.5)
    dapd "Es incluso más sexy si le voy quitando piezas..."
    scene c20s003_400An with dissolve
    play music ("music/KindofGirl.ogg")
    mc "*En el mundo real* Lanzo una mirada hacia el armario... Beagan está ahí..."
    sca "*En el mundo real* Beagan asiente..."
    call BlinkXP ("c20s003_390" , "d") from _call_BlinkXP_3570
    mcd "Me lo tendrás que demostrar, no puedo imaginármelo sin verlo..."
    scene c20s003_395AnBlink with dissolve
    dap "*En el mundo real* Pía empieza a quitarse prendas, aunque no es demasiado hábil o sexy haciéndolo."
    mcp "(Eso tiene fácil arreglo... me la puedo imaginar más sexy de lo que [dap] dice.)"
    dapdd "La chaqueta es lo primero que sobra... Siempre duermo sin ella..."
    mcdd "Con la chimenea encendida, debe hacer mucho calor para dormir con la chaqueta..."
    scene c20s003_405AnBlink with dissolve
    dapdd "Lo siguiente es la falda exterior. No sé por qué le ponen esta cosa."
    dapdd "Lo único que hace es enredarse en las piernas..."
    mcdd "Entonces mejor sin ella..."
    scene c20s003_410AnBlink with dissolve
    dapdd "Y queda la falda... con todas estas cadenitas... me quedan marcas en las piernas..."
    mcdd "Y no podemos consentir eso... son unas piernas preciosas..."
    call BlinkXP ("c20s003_415" , "d") from _call_BlinkXP_3571
    dapdd "¿Ves como era más sexy cuando le quitaba piezas?"
    mcdd "Tenías razón, pero yo aún veo un par de piezas."
    call BlinkXP ("c20s003_420" , "d") from _call_BlinkXP_3572
    dapdd "¿Quieres que me lo quite todo?"
    mcdd "Esta cama es un espacio libre de ropa... si quieres entrar te sobran dos piezas."
    mcdd "La joyería... y los tacones... te los puedes dejar puestos si quieres."
    call BlinkXP ("c20s003_425" , "d") from _call_BlinkXP_3573
    dapdd "¿De dónde has sacado la idea de que quiera entrar en la cama contigo?"
    mcdd "De que ahí vas a coger frío. Aquí, al lado de la chimenea, se está mejor."
    mcdd "Y de que se te dan mal los faroles, Pia."
    scene c20s003_430AnBlink with dissolve
    dapdd "Tienes razón... nunca se me han dado bien."
    dapdd "Y también tienes razón en que empieza a hacer frío aquí..."
    mcdd "Tus pezones lo están gritando al mundo... Una última pieza..."
    scene c20s003_435AnBlink with dissolve
    dapdd "Creo que con esto ya está todo. ¿Tengo permiso para entrar en la cama?"
    mcdd "Por supuesto. Entra antes de que te pida que des una vuelta para observar toda tu belleza."
    scene c20s003_440pv
    show c20s003_440v
    pause (2.83)
    scene c20s003_440dv
    dapdd "*Risa* Eso es fácil de resolver."
    mcdd "Preciosa..."
    call BlinkXP ("c20s003_445" , "d") from _call_BlinkXP_3574
    hide c20s003_440v
    dapdd "Hazme un hueco en la cama ahora. Al final voy a coger frío."
    mcdd "Ponte al lado de la chimenea para entrar en calor."
    call BlinkXP ("c20s003_450" , "f") from _call_BlinkXP_3575
    dap "*En el mundo real* Cuando Pia acaba de desnudarse, se mete en la cama con Vilfredo."
    mc "*En el mundo real* Sí, antes de que pille un resfriado. *Risa*"
    dapd "Dime, Vilfredo, ¿tienes un dragón bajo la manta o es que te alegras de verme?"
    dap "*En el mundo real* *Tiempo muerto* Adoro esa película."
    mcd "Es algo que tendrás que descubrir tú. Sea como sea, entrarás en calor."
    call BlinkXP ("c20s003_455" , "d") from _call_BlinkXP_3576
    dap "*En el mundo real* Pia es bastante indecisa en el sexo. Deja que Vilfredo lleve la iniciativa."
    mc "*En el mundo real* Entonces no voy a hacerla esperar. *Risa*"
    mcdd "Veo que tus pezones se han puesto muy duros... por el frío... ¿Quieres que les de calor?"
    dapdd "Sí, sí... por el frío... haz que entren en calor antes de que te salte un ojo... por favor."
    call BlinkXP ("c20s003_460" , "d") from _call_BlinkXP_3577
    mcdd "Lo puedo hacer con mis manos... suelen estar calientes..."
    dapdd "Eso se me parece bien... están entrando en calor..."
    call BlinkXP ("c20s003_465" , "d") from _call_BlinkXP_3578
    mcdd "O puedo usar mi aliento para calentarlos..."
    dapdd "*Gemido* Eso me parecería mejor todavía... No creo que se vayan a calentar más con tus manos."
    scene c20s003_470pv with dissolve
    show c20s003_470v
    "Los pezones de Pia, duros por la excitación, reaccionan a tu lengua poniéndose aún más enhiestos."
    dapdd "*Jadeo* Eso es lo que necesitaba para entrar en calor..."
    "Su respiración empieza a agitarse mientras con una pierna te abraza la espalda."
    dapdd "*Gemido* Tienes una lengua fantástica, Vilfredo, espero que la sepas usar en otros sitios también..."
    "Apenas has empezado y ya está pidiendo más. Vas a disfrutar de sus pezones un rato antes de plantearte cómo recorres su cuerpo."
    scene c20s003_475pv with dissolve
    hide c20s003_470v
    show c20s003_475v
    "Moviendo tus caderas empiezas a frotar a Mjolnir... No, no... el Martillo de Vulcano... por el vello púbico y por la húmeda raja de Pia."
    dapdd "*Jadeo* Si sigues así no voy a dejarte que utilices la lengua en ningún otro sitio... *Gemido* Cada uno de tus roces me pone más caliente..."
    "De su coño emana tanto calor como de la fragua de su Dios. Es lógico en una clériga del Dios Herrero."
    dapdd "*Gemido* Ejem... Cada vez estoy entrando más en calor..."
    "Mientras siga con jugando al juego de tener frío, no vas a abandonar sus pezones."
    scene c20s003_515a with dissolve
    hide c20s003_475v
    dapdd "*Jadeo* Déjame ponerme encima, por favor... *Gemido* Ya no aguanto más... *Jadeo* Te necesito dentro de mí."
    "Si te lo pide tan educadamente, no vas a poder negarte, ¿no?"
    mcdd "Como desees."
    call BlinkXP ("c20s003_520" , "f") from _call_BlinkXP_3579
    "Cuando Pia se monta encima tuyo, propiciandote una visión increible de sus tetas, no puedes evitar admirar la belleza de la clériga de Vulcano."
    dapdd "Cuando quieras. Será mejor que lo hagas como si arrancaras una tirita... hace mucho tiempo que no hago esto..."
    scene c20s003_525pv
    show c20s003_525v
    pause (0.3)
    scene c20s003_525dv
    hide c20s003_525v
    "Penetras a Pia con un rápido movimiento, tal como te ha pedido."
    dapdd "*Gemido* ¡Ooof!"
    "Su coño está húmedo, caliente y estrecho."
    scene c20s003_515b with dissolve
    dapdd "*Jadeo* Déjame un segundo para que me acostumbre a esto."
    "Con tu cara entre sus tetas, podrías esperar todo el tiempo del mundo."
    scene c20s003_515c with dissolve
    sca "*En el mundo real* Beagan abre un poco... más... el armario, para tener mejor visión de la escena. Empieza a tocarse..."
    "Escuchas un ligero crujido en el armario donde se ha escondido Beagan."
    dapdd "*Gemido* Cuando quieras..."
    "Una mujer que cumple su palabra cuando dice que estará lista en un segundo... Esta chica es un tesoro."
    scene c20s003_480pv
    show c20s003_480v
    "Empiezas a bombear con tus caderas. El coño de Pia es una funda perfecta para el Martillo de Vulcano."
    dapdd "*Gemido* ¡Rayos y truenos! Esto es increíble..."
    "Sus tetas rebotando en tu cara y despues en tu pecho mientras tus manos notan los firmes músculos de sus piernas hacen que ciertamente lo sea."
    dapdd "*Jadeo* ¡Más profundo!"
    "No es difícil cumplir con su petición. Te estabas reteniendo un poco..."
    scene c20s003_490pv
    hide c20s003_480v
    show c20s003_490v
    "Después de todo, había dicho que hacía mucho tiempo que no hacía esto."
    dapdd "*Gemido* ¡Justo así! *Jadeo* ¡Me encanta!"
    "A ti también. Pia cada vez está más húmeda, su vagina más caliente. Tener a la semielfa encima, adaptándose a cada uno de tus movimientos es alucinante."
    dapdd "*Jadeo* Si Beagan me viera... *Gemido* Siempre dice que me tengo que dejar ir más..."
    "Se llevaría una sorpresa si mirase hacia el armario. Por suerte, tiene la cabeza girada hacia la chimenea."
    scene c20s003_505pv
    hide c20s003_490v
    show c20s003_505v
    "Tú puedes mirar libremente. Las hermosas vistas de sus tetas en tu cara no evitan que puedas tener linea de visión con la traviesa hada mientras se da placer."
    dapdd "*Gemido* Yo no soy tan abierta como ella para el sexo... *Jadeo* Aunque parezca lo contrario con cómo me he comportado esta noche."
    "Sólo esperas que Pia sea tan insaciable como el hada. Hace diez minutos estaba teniendo un orgasmo tras otro y ahora está utilizando sus dedos para conseguir otro."
    dapdd "*Jadeo* Si me viera ahora... si cualquiera de ellas me viera... *Gemido* perdería mi altura moral... "
    mcdd "No te preocupes por ellas ahora mismo. Tan solo disfruta del momento."
    call OrgasmX ("c20s003_485") from _call_OrgasmX_73
    hide c20s003_505v
    scadd "*Sonidos amortiguados*"
    "El orgasmo de Beagan te pilla por sorpresa. Ha sido muy rápida."
    "Sus alas se iluminan con mucha más intensidad que antes, iluminando el interior del armario."
    "Afortunadamente, Pia está mirando hacia otro lado. Los sonidos del crepitar del fuego y de vuestros cuerpos chocando tapan los producidos por Campanilla."
    call BlinkXP ("c20s003_530" , "d") from _call_BlinkXP_3580
    sca "*En el mundo real* Le pido permiso a Vilfredo para que me deje interactuar con él y con Pia."
    "El hada te hace señas, consciente de que la estás mirando, pidiéndote permiso para unirse. Su cara traviesa indica que está ansiosa."
    if persistent.walkthrough:
        $ wt1 = _("Un {b}poco{/b} de interacción lésbica.")
        $ wt2 = _("Sin interación lésbica.")
    else:
        $ wt1 = ""
        $ wt2 = ""
    menu:
        "¿Le indicas algo a Beagan?"
        "Dar rienda suelta a Beagan." (wt = wt1):
            mc "*En el mundo real* Le indico que se una, puede ser divertido y no estoy seguro de qué puede hacer la pequeñaja."
            "Le haces señas para que se una a la fiesta. No sabes qué es lo que puede hacer."
            $ sca._var("LooseBeagan" , True)
        "Restringir a Beagan." (wt = wt2):
            mc "*En el mundo real* Le indico que se una, puede ser divertido. También le hago señas diciéndole que sólo interactúe conmigo."
            "Le haces señas para que se una a la fiesta. No sabes qué es lo que puede hacer, con lo que le indicas que se lo tome con calma."
            $ sca._var("LooseBeagan" , False)
    sca "*En el mundo real* Con sigilo, Beagan se dirige a los huevos de Vilfredo y los empieza a chupar."
    sca "*En el mundo real* Los masajea con una mano. Con la otra se masajea a si misma. *Risita*"
    scene c20s003_495pv with fade
    show c20s003_495v
    dap "*En el mundo real* *Tira dados* Beagan está super cachonda. *Risita*"
    "Al cabo de unos segundos puedes notar la diminuta lengua de Beagan en tus huevos mientras estos saltan con cada uno de tus movimientos."
    "Te imaginas que puede ser complicado, dado su tamaño, mantener el contacto con ellos. Debe ser como estar en un rodeo."
    if sca._var("LooseBeagan"):
        call c20s003_BeaganOrgasm from _call_c20s003_BeaganOrgasm
    scene c20s003_510pv with fade
    show c20s003_510v
    "Mientras el hada sigue haciendo de las suyas, tú sigues bombeando en el, cada vez más, húmedo coño de Pia."
    dapdd "*Gemido* ¿Has oído algo?"
    mcdd "No, nada..."
    "Estás hipnotizado por el movimiento de las tetas de Pia tan cerca de tu cara."
    if sca._var("LooseBeagan"):
        sca "*En el mundo real* Beagan mete la lengua en el ano de Pia. A ver si encuentra el palo que suele tener metido ahí."
        scene c20s003_500b with hpunch
        todas "*En el mundo real* *Risa*"
        dapdd "*Gemido* ¡Oh, Vilfredo! *Jadeo* ¡Me encanta eso!"
        "Vilfredo no tiene ni idea a lo que se refiere. Tú sí."
        "No puedes evitar que se te escape una sonrisa pensando en la estirada Pia disfrutando con una lengua en su culo."
    dapd "*Jadeo* Estoy a punto de llegar... No pares ahora..."
    if not sca._var("LooseBeagan"):
        call c20s003_BeaganOrgasm from _call_c20s003_BeaganOrgasm_1
    else:
        sca "*En el mundo real* Beagan abandona el culo de Pia y se dirige a chupar un pezón. Una última ayuda para que alcance el orgasmo."
        scene c20s003_500c with vpunch
        dapdd "*Jadeo* ¡Oh, Mi Dulce SemiElfo! Tu lengua en mi pezón se nota como un diminuto placer."
        "Con el hada en tu campo de visión, pero fuera del de Pia, no puedes evitar dejar escapar una sonrisa."
    dapdd "*Gemido* Estoy a punto de llegar..."
    if not sca._var("LooseBeagan"):
        sca "*En el mundo real* Beagan se aparta antes de que la empape con sus fluidos."
    if sca._var("LooseBeagan"):
        call OrgasmX ("c20s003_535a") from _call_OrgasmX_74
    else:
        call OrgasmX ("c20s003_535b") from _call_OrgasmX_75
    "El clímax de Pia llega poco después que sus palabras, tensando todo su cuerpo."
    dapdd "*GEMIDO* ¡OH, SÍ! ¡Alucinante! *JADEO* ¡NO PARES!"
    "No brilla como el hada, pero está igualmente preciosa durante su momento de máximo placer."
    dapdd "*JADEO* ¡Córrete dentro, por favor!"
    "La presión de su coño a lo largo de tu astil se hace cada vez más fuerte, llevándote a tu propio clímax."
    call OrgasmX ("c20s003_540") from _call_OrgasmX_76
    mcdd "¡Mpfft!"
    "Descargas toda tu semilla en coño de Pia, que la recibe sin dejar escapar casi nada."
    "Tras unos pocos movimientos más de tus caderas, os quedáis inmóviles, con tu polla todavía dentro de la clériga."
    scene c20s003_545a with dissolve
    "A los pocos segundos, puedes notar una lengua diminuta limpiando de tu astil el semen que se ha escapado del interior de Pia."
    "La sensación es muy agradable."
    call BlinkXP ("c20s003_550" , "f") from _call_BlinkXP_3581
    dap "*En el mundo real* Cuando acabáis, Pia se tumba a tu lado con una expresión de sorpresa en su cara."
    dapd "Así que esto es lo que llaman orgasmo... no me lo imaginaba así... Ha sido increíble."
    mcd "¿Tu primer orgasmo? No me ha parecido que fueras virgen..."
    call BlinkXP ("c20s003_560" , "d") from _call_BlinkXP_3582
    dapd "No lo soy, supongo que ha sido una mala elección de amantes hasta ahora..."
    mcd "Me alegra haberte enseñado lo placentero que puede ser el sexo."
    call BlinkXP ("c20s003_555" , "d") from _call_BlinkXP_3583
    dapd "No digo que no haya sido placentero hasta ahora, pero... no se había acercado a esto nunca."
    mcd "Pues me alegra que hayas llegado a esto."
    call BlinkXP ("c20s003_565" , "d") from _call_BlinkXP_3584
    dapd "Si Beagan me viera ahora mismo seguro que se reía de mí. *Risita*"
    mcd "No creo que se riera. *Risa*"
    call BlinkXP ("c20s003_570" , "d") from _call_BlinkXP_3585
    scad "*Risa* ¿Por qué crees que me reiría? Estoy muy contenta de que por fin me entiendas."
    call BlinkXP ("c20s003_575" , "d") from _call_BlinkXP_3586
    dapd "¡Oh! ¿Cuánto tiempo llevas aquí?"
    call BlinkXP ("c20s003_580" , "d") from _call_BlinkXP_3587
    scad "Desde bastante antes de que llegaras tú. *Risa* Pero no sentada en tu rodilla."
    call BlinkXP ("c20s003_585" , "d") from _call_BlinkXP_3588
    dapd "¿Y has estado mirando?"
    call BlinkXP ("c20s003_590" , "d") from _call_BlinkXP_3589
    scad "Y no solo mirando. *Risa* Afortunadamente los huevos de Vilfredo están afeitados. Si no, me podría haber hecho un abrigo."
    if sca._var("LooseBeagan"):
        scad "Además, ¿quién crees que te ha lamido el culo? *Risa* ¿De quién crees que era la diminuta lengua en tu pezón?"
        call BlinkXP ("c20s003_595" , "d") from _call_BlinkXP_3590
        dapd "¿Eras tú? ¡Pervertida!"
        call BlinkXP ("c20s003_600" , "d") from _call_BlinkXP_3591
        scad "¡Te ha encantado! *Imitando a Pia* ¡Oh, Mi Dulce SemiElfo! Tu lengua en mi pezón se nota como un diminuto placer. *Risa*"
    stop music fadeout (1.5)
    return
label c20s003_BeaganOrgasm:
    sca "*En el mundo real* Cuando está a punto de llegar al orgasmo, Beagan se sube a horcajadas a la polla de Vilfredo, restregándose hasta acabar."
    scene c20s003_500a with vpunch
    hide c20s003_495v
    scadd "¡Yihay!"
    "Tal como pensabas, debe ser como un rodeo."
    return
label c20s003_SexWithAeliaAndPaula: #7
    if _in_replay:
        menu:
            "¿Rechazaste a Pia?"
            "No":
                $ dap._var("rejectedPia" , False)
            "Sí":
                $ dap._var("rejectedPia" , True)
        call c20_DefineCharacters from _call_c20_DefineCharacters_6
    call BlinkXP ("c20s003_605" , "d") from _call_BlinkXP_3592
    dap "Llegáis a la puerta de Vilfredo. ¿Llamáis?"
    call BlinkXP ("c20s003_610" , "d") from _call_BlinkXP_3593
    eri "No me tientes... *Risa* Sí, llamamos."
    scene c20s003_345d with pixellate
    dap "*En el mundo real* Llaman a la puerta..."
    play sound ("music/knock.ogg")
    "*Knock-Knock*"
    play music ("music/dnd/woods-of-imagination.ogg")
    erid "Somos Aelia y Paula. ¿Podemos pasar?"
    mcd "Dadme un momento... estoy desnudo."
    if dap._var("rejectedPia"):
        call BlinkXP ("c20s003_615" , "d") from _call_BlinkXP_3594
        scad "*Susurrando* Pues será mejor que no salga... *Risita*"
        scad "*Susurrando* Ya las puedes hacer pasar..."
        scad "*Susurrando* Haz como si no estuviera o sospecharán."
    else:
        scene c20s003_620An with dissolve
        scad "*Susurrando* De vuelta al armario, ¿no? *Risita*"
        call BlinkXP ("c20s003_625" , "d") from _call_BlinkXP_3595
        dapd "*Susurrando* Yo no voy a caber en el armario. Mejor me meto debajo de la cama."
        call BlinkXP ("c20s003_630" , "f") from _call_BlinkXP_3596
        dapd "*Susurrando* Ya las puedes hacer pasar, no esperes que salga de aquí. Con que me haya visto Beagan tengo suficiente para una noche..."
        dapd "*Susurrando* Haz como si no estuviera o sospecharán."
    scene c20s003_345d with fade
    mcd "Ya podéis pasar"
    scene c20s003_640a with fade
    erid "Buenas noches, guapetón." (multiple=2)
    emmd "Buenas noches, Vilfredo." (multiple=2)
    mcd "Buenas noches, chicas. ¿Puedo hacer algo por vosotras?"
    call BlinkXP ("c20s003_645" , "d") from _call_BlinkXP_3597
    emmd "Bueno... veníamos a ver si... podíamos hacer algo por ti para que la habitación fuera más acogedora."
    call BlinkXP ("c20s003_650" , "d") from _call_BlinkXP_3598
    if persistent.family:
        erid "Lo que mi hermana quiere decir es que veníamos a ver si quieres que nos metamos debajo de tu manta, para darte calor."
    else:
        erid "Lo que Paula quiere decir es que veníamos a ver si quieres que nos metamos debajo de tu manta, para darte calor."
    scene c20s003_655AnBlink with dissolve
    emmd "¡Aelia! No es eso lo que quería decir... exactamente..."
    call BlinkXP ("c20s003_660" , "d") from _call_BlinkXP_3599
    erid "Sabes que me da rabia que te pongas a dar vueltas a las cosas porque no puedes o no quieres mentir."
    erid "En vez de tener que escucharte dando vueltas, prefiero ir directa a lo que venimos a hacer."
    mcp "(Lástima que no existieran las palomitas de maíz. Esto es un espectáculo digno de ver comiendo un cubo de palomitas.)"
    call BlinkXP ("c20s003_665" , "d") from _call_BlinkXP_3600
    emmd "Pero es que yo... quería saber si estabas cómodo..."
    call BlinkXP ("c20s003_670" , "d") from _call_BlinkXP_3601
    erid "¿Estás cómodo, SemiElfo?"
    mcd "Sí, por supuesto..."
    call BlinkXP ("c20s003_675" , "d") from _call_BlinkXP_3602
    erid "Vale, ya está. Ya sabes que está cómodo. Puedes irte a tu habitación si quieres..."
    call BlinkXP ("c20s003_680" , "d") from _call_BlinkXP_3603
    emmd "Bueno... también había venido... por lo otro..."
    scene c20s003_685a with pixellate
    call BlinkXP ("c20s003_685" , "d") from _call_BlinkXP_3604
    bet "[emm], tu personaje es la cosa más indecisa del mundo... *Risa* Y se le da fatal disimular."
    call BlinkXP ("c20s003_690" , "d") from _call_BlinkXP_3605
    emm "Es una Paladín, tiene que hacer como que se resiste al sexo fácil. *Risa*"
    call BlinkXP ("c20s003_695" , "d") from _call_BlinkXP_3606
    mad "Lo que me está dejando anonadada es lo putillas que sois todas. *Risa*"
    call BlinkXP ("c20s003_700" , "d") from _call_BlinkXP_3607
    sca "Las diseñamos hace unos siete meses. Con el tema de los exámenes no hemos podido jugar mucho."
    sca "Si nosotras no teníamos sexo, al menos que lo tuvieran nuestros personajes. *Risa*"
    call BlinkXP ("c20s003_705" , "d") from _call_BlinkXP_3608
    eri "Como no había ningún chico en el grupo y [dap] diseñó un pueblo lleno de mujeres, nos tenemos que conformar con los viajeros. *Risa*"
    call BlinkXP ("c20s003_710a" , "d") from _call_BlinkXP_3609
    dap "¡Hey! Hay una explicación al por qué sólo hay mujeres, y lo sabes. Si hubierais hecho las misiones correctamente, ya habría más hombres."
    dap "Pero sigamos antes de que se haga más tarde y empecéis a criticarlo todo."
    call BlinkXP ("c20s003_715a" , "d") from _call_BlinkXP_3610
    if dap._var("rejectedPia"):
        mad "Sí, sigamos. Ver la cara de [mc] mientras se imagina el sexo con Beagan ha sido muy divertido. *Risa*"
    else:
        mad "Sí, sigamos. Ver la cara de [mc] mientras se imagina el sexo con Beagan y Pia ha sido muy divertido. *Risa*"
    call BlinkXP ("c20s003_720" , "d") from _call_BlinkXP_3611
    bet "¡Eso me lo he perdido! Seguid, y perdón por la interrupción."
    call BlinkXP ("c20s003_715b" , "d") from _call_BlinkXP_3612
    mad "¡Oops, perdón! No sé si lo tendría que haber dicho..."
    call BlinkXP ("c20s003_710b" , "d") from _call_BlinkXP_3613
    dap "No pasa nada... ya sabían lo que iba a pasar, pero no con quién iba a aceptar [mc] pasar un rato."
    call BlinkXP ("c20s003_710c" , "d") from _call_BlinkXP_3614
    dap "Sigamos... [mc], Paula ha dicho que venía también por lo otro..."
    scene c20s003_680ba with pixellate
    call BlinkXP ("c20s003_680b" , "d") from _call_BlinkXP_3615
    mcd "¿Y qué es lo otro, Paula?"
    emmd "Bueno... yo quería saber..."
    call BlinkXP ("c20s003_725" , "d") from _call_BlinkXP_3616
    erid "Paula quería saber si quieres hacerle el amor."
    erid "Yo tengo suficiente con que me folles salvajemente. *Risa*"
    call BlinkXP ("c20s003_730" , "d") from _call_BlinkXP_3617
    emmd "¡Aelia! ¡Lo vas a asustar!"
    mcd "No os preocupéis. No me asusto con facilidad..."
    if persistent.walkthrough:
        $ wt1 = _("Escena sexual con Paula y Aelia. \nNo está vinculada con tus relaciones en el mundo real.")
        $ wt2 = _("Sin consecuencias.")
    else:
        $ wt1 = ""
        $ wt2 = ""
    menu:
        "Me parece bien vuestra propuesta." (wt = wt1):
            $ mc._var("rejectedAeliaPaula" , False)
            if _in_replay:
                $ AuxReplay = True
            else:
                $ AuxReplay = False
            if dap._var("rejectedPia"):
                mcpd "(Supongo que a esto se refería Beagan con que hiciera como que no está o sospecharían.)"
            else:
                mcpd "(Supongo que a esto se refería Pia con que hiciera como que no está o sospecharían.)"
            call c20s004_SexWithAeliaPaula from _call_c20s004_SexWithAeliaPaula
        "Pero no me parece bien lo que proponéis." (wt = wt2):
            $ mc._var("rejectedAeliaPaula" , True)
            if _in_replay:
                $ AuxReplay = True
            else:
                $ AuxReplay = False
            call c20s003_RejectAeliaPaula from _call_c20s003_RejectAeliaPaula
    return
label c20s003_RejectAeliaPaula:
    if _in_replay and not AuxReplay:
        menu:
            "¿Rechazaste a Pia?"
            "No":
                $ dap._var("rejectedPia" , False)
            "Sí":
                $ dap._var("rejectedPia" , True)
        call c20_DefineCharacters from _call_c20_DefineCharacters_7
    scene c20s003_640b with fade
    mcd "Estoy cansado después de todo el día cabalgando y mañana tengo mucho camino que recorrer."
    call BlinkXP ("c20s003_735" , "d") from _call_BlinkXP_3618
    emmd "Lo entendemos. Será mejor que nos vayamos a la cama también nosotras."
    eri "*En el mundo real* ¿Hay ropa por el suelo?"
    if dap._var("rejectedPia"):
        dap "*En el mundo real* No, no hay nada. Vilfredo ha recogido su ropa cuando se ha desnudado, supongo."
        mc "*En el mundo real* Sí, está en el armario de al lado de la chimenea."
        call BlinkXP ("c20s003_740" , "d") from _call_BlinkXP_3619
        erid "Hemos sido un poco egoístas viniendo sin pensar en que pudieras estar cansado."
    else:
        dap "*En el mundo real* Ahora que te fijas, sí. Ves el pijama que compró Pia hace unos meses, el oriental."
        scene c20s003_740AnBlink with dissolve
        erid "Lo entendemos. Alguien te ha debido dejar cansado..."
    call BlinkXP ("c20s003_745" , "d") from _call_BlinkXP_3620
    erid "Vámonos, Paula. Dejemos al SemiElfo descansar..."
    call BlinkXP ("c20s003_750" , "d") from _call_BlinkXP_3621
    erid "Hasta mañana, SemiElfo."
    mcd "Hasta mañana, Aelia."
    call BlinkXP ("c20s003_755" , "d") from _call_BlinkXP_3622
    if not dap._var("rejectedPia"):
        emm "*En el mundo real* Yo ni he pensado en la ropa, con lo que Paula tampoco se fija."
    emmd "Hasta mañana, Vilfredo. Espero que os despidáis mañana, antes de iros."
    mcd "No lo dudes, Paula. Hasta mañana."
    scene c20s003_345d with dissolve
    play sound ("music/portazo.ogg")
    "*Blam*"
    mcd "Me parece que se han decepcionado un poco..."
    if not dap._var("rejectedPia"):
        call BlinkXP ("c20s003_760" , "d") from _call_BlinkXP_3623
        dapd "Aelia ha visto mi ropa en el suelo. La ha movido de sitio para que yo sepa que lo sabe."
        dapd "Voy a hablar con ella..."
        call BlinkXP ("c20s003_765" , "f") from _call_BlinkXP_3624
        dapd "Te veo mañana, Vilfredo."
        mcd "¿No vas a volver?"
        call BlinkXP ("c20s003_770" , "d") from _call_BlinkXP_3625
        dapd "No, lo siento. Tengo que hablar con mi amiga. No me gustaría que esto se enquistase entre nosotras."
        dapd "Hasta mañana, Vilfredo."
        mcd "Hasta mañana, Pia."
        scene c20s003_345d with dissolve
        play sound ("music/portazo.ogg")
        "*Blam*"
    call BlinkXP ("c20s003_775" , "d") from _call_BlinkXP_3626
    mcd "Pues quedamos tú y yo, como al principio... ¿Seguimos donde lo hemos dejado?"
    scad "¿Te ha parecido bonito?"
    mcd "¿Qué? ¿A qué te refieres?"
    call BlinkXP ("c20s003_780" , "d") from _call_BlinkXP_3627
    scad "A mentirle a mis amigas. Les has dicho que estabas cansado."
    scene c20s003_785AnBlink with dissolve
    scad "Si tan cansado estás, mejor te dejo dormir."
    scad "Hasta mañana, Vilfredo."
    scene c20s003_345d with dissolve
    play sound ("music/portazo.ogg")
    "*Blam*"
    sca "*En el mundo real* Beagan se va sin darle tiempo a Vilfredo a responder."
    stop music fadeout (1.5)
    mc "*En el mundo real* Pues me tocará dormir solo, ¿no?"
    scene c20s003_790a with pixellate
    play music ("music/ChillUkelele.ogg")
    call BlinkXP ("c20s003_790" , "d") from _call_BlinkXP_3628
    dap "Pues sí. El resto de la noche pasa sin incidentes."
    call BlinkXP ("c20s003_795" , "d") from _call_BlinkXP_3629
    bet "Vaya, me he quedado sin ver la cara de [mc] mientras se imagina el sexo. *Risa*"
    mc "¡No ha sido para tanto!"
    call BlinkXP ("c20s003_800" , "d") from _call_BlinkXP_3630
    mad "*Risa* ¡Tú no te veías la cara!"
    call BlinkXP ("c20s003_805" , "d") from _call_BlinkXP_3631
    eri "*Risa* Nosotras también nos lo hemos perdido, Tía Betty."
    call BlinkXP ("c20s003_810" , "d") from _call_BlinkXP_3632
    sca "En la próxima sesión, lo tienes que grabar con el móvil, Maddie. *Risa* Tú lo tienes delante."
    mc "Chicas, ¿de verdad ponía caras?"
    call BlinkXP ("c20s003_815" , "d") from _call_BlinkXP_3633
    dap "Me recordabas a cuando éramos pequeños y Tía [mar] decía que iba a hacer pastel de chocolate. *Risa*"
    dap "Y te pasabas un par de días imaginando lo sabroso que iba a estar. *Risa*"
    call BlinkXP ("c20s003_820" , "d") from _call_BlinkXP_3634
    emm "¡Chicas! ¡Esta es una zona común y hay cámaras! *Risa* Les podemos pedir las grabaciones a Amanda y a Eva."
    emm "Si es tan espectacular como decís, yo también quiero verlo."
    mc "*Risa* ¡Ni se os ocurra!"
    call BlinkXP ("c20s003_825" , "d") from _call_BlinkXP_3635
    stop music fadeout (1.5)
    dap "Ya hablaremos de eso mañana. Se está haciendo tarde y no va a dar tiempo de jugar todo lo que tengo planeado si seguís así."
    return
label c20s004_SexWithAeliaPaula:
    if _in_replay and not AuxReplay:
        menu:
            "¿Rechazaste a Pia?"
            "No":
                $ dap._var("rejectedPia" , False)
            "Sí":
                $ dap._var("rejectedPia" , True)
        menu:
            "¿Cuántas relaciones tienes?"
            "Una":
                $ mc._var("relationships", 1, intention = "set")
            "Más de una":
                $ mc._var("relationships", 2, intention = "set")
            "Ninguna":
                $ mc._var("relationships", 0, intention = "set")
        call c20_DefineCharacters from _call_c20_DefineCharacters_8
    scene c20s003_640c with dissolve
    play music ("music/SexyLoungeMusic.ogg")
    emmd "¡Genial! Nunca me he foll... nunca he hecho el amor con un SemiElfo..."
    if persistent.family:
        erid "Paula colecciona razas. *Risa* Ha sacado los gustos de la nuestra madre."
    else:
        erid "Paula colecciona razas. *Risa* Ha sacado los gustos de la Dómina Livia."
    mcd "Pero ¿qué dirían vuestras amigas si se enteraran?"
    eri "*En el mundo real* ¿Hay ropa tirada por el suelo?"
    if dap._var("rejectedPia"):
        dap "*En el mundo real* No, no hay nada por el suelo. Parece que Vilfredo es un tipo ordenado."
        call BlinkXP ("c20s004_005" , "d") from _call_BlinkXP_3636
    else:
        dap "*En el mundo real* Ahora que te fijas, sí. Ves el pijama que compró Pia hace unos meses, el oriental."
        scene c20s003_740bAnBlink with dissolve
    erid "Seguramente no pasaría nada. Pia tiene un palo metido en el culo y aunque estuviera escondida debajo de la cama no se atrevería a salir."
    erid "Y sería mejor que la mariposilla no se atreviera a aparecer. Ahora eres todo nuestro. *Risa*"
    call BlinkXP ("c20s004_010" , "d") from _call_BlinkXP_3637
    emmd "A mí no me importaría que se uniera cualquiera de las dos. Pero Pia no lo haría nunca. Es un poco frígida."
    emmd "Y Beagan... va en solitario. Nunca se ha querido unir a nosotras."
    if dap._var("rejectedPia"):
        mcd "{i}(Con Beagan en el armario, no estoy seguro de qué hacer.){/i}"
    else:
        mcd "{i}(Con Beagan en el armario y Pia bajo la cama, no estoy seguro de qué hacer.){/i}"
    scene c20s004_015a with pixellate
    mc "Chicas, no sé cómo actuar en esta situación..."
    sca "No te preocupes por nosotras, [mc]..."
    dap "Ya tenía previsto que pasara algo así."
    call BlinkXP ("c20s004_020" , "d") from _call_BlinkXP_3638
    bet "¿Tienes a las dos escondidas en tu habitación?"
    if dap._var("rejectedPia"):
        mc "No, Tia Betty, solo al hada de Scarlett. He rechazado a [dap]."
    else:
        mc "Sí. Y ahora me voy a sentir mal..."
    mc "Aunque no sé si debería haberlo dicho..."
    call BlinkXP ("c20s004_025" , "d") from _call_BlinkXP_3639
    dap "No pasa nada... ya sabían lo que iba a pasar, pero no con quién ibas a aceptar pasar un rato."
    dap "Si no hubieras aceptado con ninguna, ellas no hubieran llegado hasta tu puerta. Se habrían cruzado con Beagan en el pasillo."
    call BlinkXP ("c20s004_030" , "d") from _call_BlinkXP_3640
    if mc._var("relationships") > 1:
        bet "Estás hecho todo un machote... al menos tu personaje. El harén te está sirviendo de entrenamiento. *Risa*"
    else:
        bet "Estás hecho todo un machote... al menos tu personaje. *Risa*"
    call BlinkXP ("c20s003_715a" , "d") from _call_BlinkXP_3641
    mad "Sigamos, quiero ver la cara que pone el machote ahora, imaginándose el sexo con el equipo Ángel y Diablo."
    call BlinkXP ("c20s003_720" , "d") from _call_BlinkXP_3642
    bet "Sí, sí, seguid. Yo también tengo ganas de verlo."
    mc "No les hagas caso, no ha sido para tanto"
    call BlinkXP ("c20s003_800" , "d") from _call_BlinkXP_3643
    mad "*Risa* ¡Tú no te veías la cara!"
    call BlinkXP ("c20s003_805" , "d") from _call_BlinkXP_3644
    eri "*Risa* [emm] y yo también nos lo hemos perdido, Tía Betty. Pero tenemos la oportunidad de verlo ahora."
    call BlinkXP ("c20s003_810" , "d") from _call_BlinkXP_3645
    sca "Deberías grabarlo con el móvil, Maddie. *Risa* Tú lo tienes delante."
    mc "Chicas, ¿de verdad ponía caras?"
    call BlinkXP ("c20s003_815" , "d") from _call_BlinkXP_3646
    dap "Me recordabas a cuando éramos pequeños y Tía [mar] decía que iba a hacer pastel de chocolate. *Risa*"
    dap "Y te pasabas un par de días imaginando lo sabroso que iba a estar. *Risa*"
    call BlinkXP ("c20s003_820" , "d") from _call_BlinkXP_3647
    emm "¡Chicas! ¡Esta es una zona común y hay cámaras! *Risa* Les podemos pedir las grabaciones a Amanda y a Eva."
    emm "Si es tan espectacular como decís, yo también quiero verlo."
    mc "*Risa* ¡Ni se os ocurra!"
    call BlinkXP ("c20s003_825" , "d") from _call_BlinkXP_3648
    dap "Ya hablaremos de eso mañana. Se está haciendo tarde y no va a dar tiempo de jugar todo lo que tengo planeado si seguís así."
    scene c20s004_035a with pixellate
    call BlinkXP ("c20s004_035" , "d") from _call_BlinkXP_3649
    erid "¿Cómo quieres hacerlo? ¿Por separado o las dos juntas?"
    mcd "No me atrevería a separar una pareja tan perfecta... *Risa*"
    call BlinkXP ("c20s004_040" , "d") from _call_BlinkXP_3650
    emmd "Tienes que saber una cosa antes de empezar... no te puedes correr dentro."
    emmd "Nuestra naturaleza extraplanar hace que nos siente mal después... Es como si nuestro cuerpo luchara contra una infección..."
    emm "*En el mundo real* Eso es por cortesía de [dap], fue la condición que puso por aceptar algunas de las peticiones que le hicimos para nuestros personajes."
    dap "*En el mundo real* Sabéis que tenéis una misión pendiente para poder resolverlo. Si hablarais menos y jugarais más..."
    mcd "No hay problema sabiéndolo con antelación. Tampoco sería correcto correr el riesgo de dejaros embarazadas antes de irme, ¿no?"
    scene c20s004_045d with dissolve
    pause 0.8
    call BlinkXP ("c20s004_045" , "d") from _call_BlinkXP_3651
    emmd "Entonces será mejor que me empiece a quitar ropa... Este vestido es precioso, pero... tiene demasiadas piezas."
    mcd "Me gusta hacia dónde va esto..."
    scene c20s004_055d with dissolve
    emmd "Y este corsé siempre me ha parecido de lo más incómodo... Si no fuera tan bonito..."
    mcd "Nunca he entendido el uso de los corsés. Parecen una herramienta de tortura."
    call BlinkXP ("c20s004_055" , "d") from _call_BlinkXP_3652
    emmd "Lo son. Pero ya estoy libre de él."
    scene c20s004_050pv with dissolve
    show c20s004_050v
    pause (1.8)
    scene c20s004_050dv
    call BlinkXP ("c20s004_060" , "d") from _call_BlinkXP_3653
    erid "Por eso yo no los uso. Me gustan las prendas fáciles de quitar, siempre que sean sexys, claro..."
    mcd "Y ese atuendo cumplía ambas funciones. Sexy y fácil de quitar."
    call BlinkXP ("c20s004_065" , "d") from _call_BlinkXP_3654
    emmd "El mío también es fácil de terminar de quitar..."
    mcd "Y estás tan sexy como Aelia."
    scene c20s004_070b with fade
    erid "¿Vienes? ¿O tenemos que hacer nosotras todo el trabajo?"
    emmd "Esa cama va a ser pequeña para los tres... Tenemos que convencer a Marzia para que compre camas más grandes."
    mcd "No os preocupéis, ya voy yo. Estoy ansioso por acariciar esos preciosos cuerpos."
    scene c20s004_070a with dissolve
    mcd "¿Veis lo que os decía? Nunca me atrevería a separar una pareja tan perfecta. Mis manos estan llenas de vosotras."
    erid "Las nuestras también están llenas de ti, con lo que ninguna de nosotras se va a quejar."
    emmd "Bueno, con el tamaño que tiene, quizás yo sí me queje un poco. *Risita*"
    scene c20s004_070c with dissolve
    mcd "¿Y tú, mi preciosa Diablesa? ¿También te quejarás?"
    erid "A mí no me desagrada un poco de dolor mezclado con el placer, SemiElfo."
    eri "*En el mundo real* Que conste en acta que esto es cosa de mi personaje. Odio el dolor. *Risita*"
    emmd "Al engendro del infierno puedes hacerle lo que quieras. Yo prefiero que me foll... que me hagas el amor dulcemente."
    scene c20s004_070d with dissolve
    mcd "¿Y también interactuáis entre vosotras? ¿O sólo lo vais a hacer conmigo?"
    if dap._var("rejectedPia"):
        mcd "Nunca he estado con dos mujeres a la vez... hasta hace poco, al menos."
    else:
        mcd "Nunca he estado con dos mujeres a la vez..."
    mcd "No sé muy bien cómo funciona con vosotras dos."
    if persistent.lesbian:
        $ lesbianAngelDevil = True
    else:
        if persistent.walkthrough:
            $ wt1 = _("Paula y Aelia interactuarán. \nNo afectará a los comportamientos de [eri] y [emm] en el mundo real.")
            $ wt2 = _("Paula y Aelia no interactuarán.")
        else:
            $ wt1 = ""
            $ wt2 = ""
        menu:
            "Me gustaría que lo hicierais." (wt = wt1):
                $ lesbianAngelDevil = True
            "Es algo que no me gustaría ver." (wt = wt2):
                $ lesbianAngelDevil = False
    if lesbianAngelDevil:
        erid "Si no te importa, nos gusta darnos cariño entre nosotras..."
        emmd "Aunque seguramente tengamos suficiente contigo..."
        mcd "No tengo ningún problema en que todos nos demos placer a todos."
        scene c20s004_070e with dissolve
        "Aelia te rodea para recibir cariño de Paula, mientras tus labios y manos empiezan a recorrer su piel y tu astil encaja perfectamente entre sus nalgas."
        show c20s004_075v with dissolve
        emmdd "¿Ya estás húmeda, chiquitina? Aún no hemos empezado y ya lo puedo notar a través de tus bragas..."
        eridd "Ahora mismo tengo dos rabos en mi espalda... el SemiElfo se está frotando con mi culo..."
        mcdd "Si quieres dejo de hacerlo..."
        eridd "Será mejor que no se te ocurra... *Gemido* Mi rabo es más grande que el tuyo... *Jadeo* y puntiagudo..."
        scene c20s004_080pv with dissolve
        hide c20s004_075v
        "Aelia cambia de postura, apretando su culo más todavía contra tu polla, mientras, con una mano, coge tu astil."
    else:
        emmd "No te preocupes, creo que tendremos suficiente con lo que tengo en la mano."
        erid "Paula es demasiado mojigata para disfrutar lo que yo puedo hacerle, y es con la única que lo haría."
        scene c20s004_080pv with dissolve
        "Aelia se acerca a la Aasimar, apretando su culo contra tu polla, mientras coge con una mano tu astil."
    show c20s004_080v
    "Paula te acaricia un hombro mientras con su otra mano masajea tu glande."
    "Tú empiezas a acariciar su coño por encima de las bragas. Está húmeda. Dedicas tu otra mano a su pecho libre, jugando con su pezón."
    eridd "*Jadeo* Creo que tu polla encaja perfectamente en mi culo... y en mi mano..."
    emmdd "*Gemido* Tan solo espero que seas tan hábil con ella como eres con tus manos..."
    mcdd "Intentaré no decepcionaros... Vuestras manos a la vez en mi polla se sienten increíbles. No puedo esperar a tener todo vuestro cuerpo para mí."
    emmdd "*Jadeo* Pero tú sabes que no he venido solo para que me hagas una paja, ¿verdad?"
    eridd "*Gemido* No seas avariciosa, Paula, todo llegará... *Jadeo* Tiene que ser bueno si estás respirando tan agitadamente..."
    emmdd "*Jadeo* Lo es... *Gemido* Pero creo que es momento de cambiar... yo también quiero notar esa polla."
    mad "*En el mundo real* Míralo, Betty, esa es la cara a la que nos referíamos. *Risa*"
    bet "*En el mundo real* Sólo le falta babear. *Risa*"
    mc "*En el mundo real* Dejadme imaginar esto en paz. *Risa* No todos los días se hace un trío con un ángel y un demonio."
    eri "*En el mundo real* Semi-ángel y Semi-{b}diablo{/b}. *Risa*"
    emm "*En el mundo real* No es que le importe mucho. *Risa* Pondria la misma cara si hiciera un trío con una orco y una goblin."
    mc "*En el mundo real* La-la-la. No os escucho. Paula quiere cambiar de posición. *Risa* Tengo que complacerla."
    scene c20s004_070f with dissolve
    hide c20s004_080v
    "Las dos chicas se arrodillan delante de ti, mirándote desde abajo."
    if persistent.family:
        emmdd "No me extraña que hicieras gemir a mi hermana. Es una herramienta impresionante."
    else:
        emmdd "No me extraña que hicieras gemir a Aelia. Es una herramienta impresionante."
    "La Diablesa te mira con una sonrisa pícara."
    eridd "Y espera a notarla en movimiento..."
    scene c20s004_070g with dissolve
    emmdd "No puedo esperar, Vilfredo. Dime si lo hago al ritmo que te gusta."
    if persistent.family:
        eridd "Estoy segura que lo vas a disfrutar. *Risa* Las manos de mi hermana son... angelicales."
    else:
        eridd "Estoy segura que lo vas a disfrutar. *Risa* Las manos de Paula son... angelicales."
    mcdd "¿Y qué vas a hacer tú mientras ella juega con mi martillo?"
    eridd "Algo de lo que también estoy segura que te va a gustar."
    scene c20s004_085pv with dissolve
    show c20s004_085v
    "La Paladín empieza una lenta paja mientras la Pícara te masajea los huevos y lame tu capullo de vez en cuando."
    emmdd "¿Tú estás segura de que vas a poder meterte esto dentro?"
    if persistent.family:
        "Los movimientos de la cabeza de Aelia parecen extraños, supones que es consciente de dónde están sus cuernos y quiere evitar destrozar la angelical cara de su hermana."
    else:
        "Los movimientos de la cabeza de Aelia parecen extraños, supones que es consciente de dónde están sus cuernos y quiere evitar destrozar la angelical cara de Paula."
    eridd "Estoy deseando probarlo. ¿Me dejarás a mí probar primero?"
    scene c20s004_140pv with dissolve
    hide c20s004_085v
    show c20s004_140v
    emmdd "Por supuesto. Sabes que no te podría negar nada..."
    eridd "¿Tienes mucho aguante, SemiElfo? ¿Podrás darnos placer a ambas sin correrte?"
    mcdd "Eso espero, preciosa. Y si no, la noche es larga... No hay por qué acabarlo todo tras el primer round."
    emmdd "Tan solo espero que Pia y Beagan no nos interrumpan... Siempre se meten donde no deben y suelen ser inoportunas."
    if not dap._var("rejectedPia"):
        scene c20s004_145a with hpunch
        "Te parece oír un gruñido amortiguado debajo de la cama."
    scene c20s004_145b with hpunch
    hide c20s004_140v
    "Estás seguro de escuchar una risita dentro del armario."
    mcdd "Pero antes hay que quitaros el exceso de ropa, ¿verdad? No queremos estropear esas braguitas tan monas que lleváis."
    scene c20s004_090An with fade
    "Ambas se ponen de pie, aprisionando tu cabeza entre sus increíbles culos. No puedes dejar de besar el diabólico culo de Aelia mientras le bajas las bragas."
    eridd "Tus labios se notan húmedos y calientes en mi culo... Me gusta..."
    emmdd "Dame el mismo tratamiento a mí. Yo también quiero notarlo..."
    scene c20s004_095An with dissolve
    "Mientras la Diablesa se arrodilla a tu lado, eliminas las bragas de la Paladín de la ecuación."
    eridd "Esto sigue duro como una piedra..."
    "Con la pícara agarrando tu polla por el astil y rodeado por dos mujeres como estas, es difícil que baje en un futuro cercano."
    emmdd "Tenías razón en cuanto a sus labios. Se notan tan bien en mis nalgas..."
    call BlinkXP ("c20s004_150" , "f") from _call_BlinkXP_3655
    eridd "Pues es un buen momento para empezar antes de que nos interrumpan..."
    call BlinkXP ("c20s004_155a" , "d") from _call_BlinkXP_3656
    emmdd "Súbete al arcón, tipo rana... así me podré meter entre las piernas de Vilfredo y hacerle... cosas... mientras te foll... mientras te hace el amor."
    mcdd "Suena prometedor."
    scene c20s004_145d with fade
    eridd "¿Así mejor?"
    call BlinkXP ("c20s004_155b" , "d") from _call_BlinkXP_3657
    emmdd "Mucho mejor... estás muy sexy así."
    emmdd "Guárdame un poco de SemiElfo para mí."
    scene c20s004_110pv with fade
    if persistent.family:
        "Te colocas detrás de la Diablesa mientras el Ángel se sitúa entre tus piernas. Nada más penetrar a su hermana, empieza a lamer tus huevos."
    else:
        "Te colocas detrás de la Diablesa mientras el Ángel se sitúa entre tus piernas. Nada más penetrar a su compañera, empieza a lamer tus huevos."
    show c20s004_110v
    "El coño de Aelia es estrecho y húmedo. Despide un calor infernal, lo que parece adecuado para una mujer como ella."
    eridd "*Gemido* ¡Ooof! Mejor de lo que prometía, Paula..."
    "La lengua de Paula recorre tus huevos y tu perineo, sin molestarse en contestar a la mujer que está siendo follada como una rana."
    emmdd "*Slurp* *Slurp*"
    "La sensación combinada del coño de una y la lengua de la otra es increíble."
    scene c20s004_105pv with dissolve
    hide c20s004_110v
    show c20s004_105v
    "Esperas que haya tiempo para un segundo round. No estás tan seguro como hace unos minutos de poder complacer a ambas mujeres sin correrte."
    emmdd "*Slurp* *Gemido* *Slurp*"
    "Puedes notar los gemidos de Paula en tus huevos. Estás seguro que ha empezado a darse placer mientras lame tus huevos."
    eridd "*Jadeo* La posición es incómoda... *Gemido* Pero es increíble, parece que vas a romper mi cérvix... *Jadeo* Duele un poco, pero me encanta..."
    "Cada recorrido acaba con tu glande golpeando el final de su vagina. Intentas retenerte un poco."
    scene c20s004_100pv with dissolve
    hide c20s004_105v
    show c20s004_100v
    "La Diablesa lo nota y empuja su pelvis contra ti en cada movimiento, indicándote que no bajes el ritmo."
    eridd "*Gemido* ¿Te estás tocando, Paula? *Jadeo* Puedo oir tus gemidos."
    "Ella puede oirlos, tu los notas en tus huevos con cada lametón."
    emmdd "*Slurp afirmativo* *Jadeo* *Slurp*"
    "Te sorprende lo mucho que se puede transmitir en un simple Slurp."
    if lesbianAngelDevil:
        eridd "*Gemido* Pues puedes usar tu lengua en mí, si llegas... *Jadeo* Estoy a punto de llegar."
        scene c20s004_115pv with dissolve
        hide c20s004_100v
        show c20s004_115v
        if persistent.family:
            "La Paladín abandona tus huevos y se dedica al clítoris de su hermana en una posición muy forzada. Echas de menos esa lengua."
        else:
            "La Paladín abandona tus huevos y se dedica al clítoris de la Pícara en una posición muy forzada. Echas de menos esa lengua."
        emmdd "*Slurp húmedo* *Jadeo* *Slurp húmedo*"
        "El coño de la mujer cornuda se estrecha inmediatamente al notar el primer lametón."
        eridd "¡OH, SÍ! *GEMIDO* ¡La mejor polla de la historia y la lengua que más me conoce!"
        "Sigues notando los gemidos de Paula en tus huevos, estás seguro que están a punto de rozar su barbilla en cada embestida."
        eridd "*JADEO* ¡NO PARÉIS! *GEMIDO* ¡ESTOY A PUNTO DE CORRERME!"
    else:
        eridd "*JADEO* ¡NO PARES! *GEMIDO* ¡ESTOY A PUNTO DE CORRERME!"
    emmdd "*Slurp afirmativo* *GEMIDO* *SLURP*"
    if lesbianAngelDevil:
        scene c20s004_160An1 with hpunch
        hide c20s004_115v
    else:
        scene c20s004_160An2 with hpunch
        hide c20s004_100v
    eridd "*GEMIDO* ¡SÍ! *JADEO* ¡ME CORROOO!"
    emmdd "*JADEO* *SLURP* *GEMIDO* *¡SLUUUURP!*"
    if persistent.family:
        "Las dos hermanas, tan diferentes entre ellas, se corren simultaneamente casi arrastrándote a tu própio orgasmo."
    else:
        "Las dos amigas, tan diferentes entre ellas, se corren simultaneamente casi arrastrándote a tu própio orgasmo."
    "Tienes que parar tus embestidas un momento para evitar correrte en ese momento."
    "Te ha parecido ver un fuerte resplandor verde saliendo del armario donde se esconde Beagan."
    mcpd "(El Hada se ha estado divirtiendo. *Risa Mental*)"
    if not dap._var("rejectedPia"):
        mcpd "(¿Qué estará haciendo Pia?)"
    scene c20s004_170An with fade
    "Abandonas reluctantemente el coño de Aelia. Cada fibra de tu ser te pide que continúes bombeando hasta correrte."
    call BlinkXP ("c20s004_175a" , "f") from _call_BlinkXP_3658
    "Unos segundos después..."
    eridd "Ha sido muy bueno, Vilfredo, y te has podido contener. Gracias..."
    mcdd "¿No más \"SemiElfo\"? ¿Me he ganado el honor de ser Vilfredo?"
    call BlinkXP ("c20s004_175b" , "d") from _call_BlinkXP_3659
    eridd "*Risa* Creo que sí, te lo has ganado."
    call BlinkXP ("c20s004_180" , "d") from _call_BlinkXP_3660
    emmdd "Muy bonito y blah blah blah pero, si os ponéis a hablar ahora, eso se va a bajar antes de que me toque mi turno."
    mcd "¿De verdad crees que esto se va a bajar mientras tenga dos preciosidades desnudas en mi habitación?"
    if dap._var("rejectedPia"):
        mcpd "(Bueno, tres preciosidades...)"
    else:
        mcpd "(Bueno, cuatro preciosidades...)"
    call BlinkXP ("c20s004_185" , "d") from _call_BlinkXP_3661
    emmdd "*Risita* Mejor no correr riesgos... vamos a la cama."
    mcdd "Después de tí, Ángel mío. *Risa*"
    call BlinkXP ("c20s004_190" , "d") from _call_BlinkXP_3662
    eridd "Esperad un momento... Paula, ¿no preferirías tener sexo de pie, desde atrás?"
    call BlinkXP ("c20s004_195" , "d") from _call_BlinkXP_3663
    emmdd "Sabes que me gusta mucho, pero el pobre Vilfredo a lo mejor necesita un descanso... después de darte lo tuyo... *Risita*"
    mcdd "Por mí no te preocupes, si prefieres esa posición..."
    scene c20s004_200An with dissolve
    "*Blam*"
    mcpd "(Espero que Beagan no estuviera pegada a la puerta. No se ha oído ningún quejido, con lo que parece que todo va bien ahí dentro.)"
    call BlinkXP ("c20s004_205" , "d") from _call_BlinkXP_3664
    eridd "Dejadme la cama para mí, para miraros como si fuera la primera fila del anfiteatro."
    eridd "Podéis follar... o lo que sea... contra ese armario. Tendré unas vistas impresionantes mientras descanso un poco."
    eridd "Yo sí que lo necesito."
    call BlinkXP ("c20s004_210" , "d") from _call_BlinkXP_3665
    emmdd "¡Qué buena idea! ¡Sabes que me encanta que mires!"
    mcdd "A mí no me importa, aunque preferiría que participaras."
    call BlinkXP ("c20s004_215" , "f") from _call_BlinkXP_3666
    eridd "Déjame recuperar el aliento y quizás me una."
    scene c20s004_125pv with dissolve
    "Te colocas detrás de Paula mientras ella apoya las manos en las dos puertas del armario."
    emmdd "Puedes ir a saco, no hace falta que me des tiempo para acostumbrarme a nada. Me gusta un poco duro..."
    mcdd "Como desees..."
    mcp "(Si hubiera dicho esto en la partida en vez de en mi imaginación, [emm] estaría contentísima. Es su película favorita.)"
    show c20s004_125v
    "Tal como desea, la penetras con fuerza y empiezas a bombear inmediatamente."
    emmdd "*Jadeo* ¡Wow! ¡Esto empieza bien!"
    if persistent.family:
        "Está caliente como su hermana. Es igual de estrecha que ella. Y está más húmeda todavía, después de su primer orgasmo."
    else:
        "Está tan caliente como Aelia. Es igual de estrecha que ella. Y está más húmeda todavía, después de su primer orgasmo."
    eridd "*Gemido* Ya te lo he dicho... El chico es bueno..."
    "Parece que la Diablesa no va a recuperar el aliento sino que lo va a usar para gemir."
    scene c20s004_120pv with dissolve
    hide c20s004_125v
    show c20s004_120v
    "Temías que el armario se tambaleara mucho y acabarais haciendo un cócktail de Hada, pero es robusto y apenas se mueve."
    emmdd "*Gemido* ¡Fóllame como a una de tus chicas Galas! *Jadeo* ¡Estás tocando todos mis puntos sensibles!"
    mcp "(*Risa Mental* Era dibújame, pero lo dejaremos pasar. ¿Ya no es hacer el amor?)"
    "Tu risa mental casi hace que Vilfredo pierda el ritmo, tienes que mantenerte concentrado en la escena que estás imaginando."
    eridd "*Jadeo* No os podéis imaginar lo tórridos que estáis los dos juntos..."
    scene c20s004_165pv with dissolve
    hide c20s004_120v
    show c20s004_165v
    "Te lo puedes imaginar. El culo de Paula rebotando contra tu pelvis cada vez que empujas el Martillo del Dios hasta el fondo de su vagina es una vista preciosa."
    emmdd "*Jadeo* ¡Es el mejor polvo que he echado en mi vida!"
    "Saber que la Diablesa está detrás tuyo, mirándoos y dándose placer hace que te pongas más cachondo todavía."
    if persistent.family:
        eridd "*Gemido* ¡Así! ¡Destrózale el coño a la pánfila de mi hermana!"
    else:
        eridd "*Gemido* ¡Así! ¡Destrózale el coño a esa pánfila!"
    eridd "*Jadeo* ¡Pretende buscar el amor verdadero y lo único que desea... *Gemido* es que la follen como a una perra!"
    scene c20s004_130pv with dissolve
    hide c20s004_165v
    show c20s004_130v
    "Te sorprende cómo Aelia habla de Paula. Hasta ahora han parecido buenas amigas."
    emmdd "*Gemido* ¡Sí! *Jadeo* ¡Fóllame como a una perra!"
    "Otra vez te sorprendes. El cambio de actitud ha sido total. Ya no habla de hacer el amor. Ahora solo quiere sexo."
    eridd "*Jadeo* Eso es, déjate ir. *Gemido*"
    "¡Eso es! Su coño se estrecha mientras habla. Necesitaba un empujón de la Pícara para dejarse ir totalmente."
    call OrgasmX ("c20s004_220") from _call_OrgasmX_77
    hide c20s004_130v
    if not lesbianAngelDevil:
        scene c20s004_130pv with dissolve
        show c20s004_130v
    eridd "*GEMIDO* ¡SÍ! ¡ME CORROOOO! *JADEO* ¡Como me pone cuando te dejas ir, perra mala!"
    if persistent.family:
        "El coño de Paula vuelve a tensarse. A ella también le pone cachonda que su hermana se corra viéndonos."
    else:
        "El coño de Paula vuelve a tensarse. A ella también le pone cachonda que su compañera se corra viéndonos."
    if lesbianAngelDevil:
        scene c20s004_130pv with dissolve
        show c20s004_130v
        emmdd "*Gemido* ¡Pues ven aquí antes de que me corra! *JADEO* Vilfredo está haciendolo demasiado bien..."
        eridd "*Jadeo* Dame un segundo... *Gemido* Estoy acabando..."
        emmdd "*GEMIDO* ¡Ven ya!"
        "Otra vez el cambio de actitud. Ahora es ella la dominante de la relación entre las dos mujeres."
        scene c20s004_135pv with fade
        hide c20s004_130v
        show c20s004_135v
        "Aelia se arrodilla debajo de Paula, agarrando su pezón entre sus labios y acariciando el clítoris del Ángel."
        eridd "¿Así, cielo?"
        "Puedes notar los dedos de la Pícara rozando tu astil en cada embestida. Cada vez que entras o sales de la Paladín."
        emmdd "*GEMIDO* ¡Exactamente así, engendro del infierno!"
        "El coño de Paula se tensa y se estrecha con fuerza, señal de que el orgasmo está a punto de llegar."
        if not dap._var("rejectedPia"):
            scene c20s004_225An1 with hpunch
        else:
            scene c20s004_225An3 with hpunch
        hide c20s004_135v
    else:
        if not dap._var("rejectedPia"):
            scene c20s004_225An2 with hpunch
        else:
            scene c20s004_225An4 with hpunch
    emmdd "*JADEO* ¡OH, SÍ! *GEMIDO* ¡POR VESTA!"
    "A los pocos segundos el cuerpo de la paladina explota entre oleadas de placer."
    if not lesbianAngelDevil:
        scene c20s004_130pv with dissolve
        show c20s004_130v
    emmdd "*GEMIDO* ¡Sigue follándome hasta que estés a punto de correrte!"
    "No tiene en cuenta que ambas te han masturbado y que te has follado a Aelia."
    mcdd "Ya estoy a punto..."
    if not lesbianAngelDevil:
        eridd "¡Voy!"
    scene c20s004_230a with fade
    "Las dos chicas se arrodillan a tus pies, esperando tu corrida."
    menu:
        "¿Dónde quieres correrte?"
        "Correrte en sus caras.":
            call c20s004_Faces from _call_c20s004_Faces
        "Correrte en sus tetas.":
            call c20s004_Tits from _call_c20s004_Tits
    scene c20s004_230b with fade
    emm "*En el mundo real* Me gustaría saber que está pasando por su cabeza ahora mismo... *Risa* Hace unos minutos que está ausente..."
    eri "*En el mundo real* Cuando acabe el sexo volverá con nosotras. *Risa* Y se encontrará que Paula y Aelia van a pasar la noche en su cama."
    "Las dos mujeres se tumban en la cama invitadoramente tras quitarse los zapatos y otros accesorios."
    "De alguna forma la conversación en el mundo real ha entrado en tu mente a través de tus ensoñaciones."
    emmd "¿Vienes?"
    mcd "¿Segundo round?"
    erid "No, hoy no. Mañana te espera una larga cabalgata. Pero si alguna vez vuelves a pasar por Novum Templum me apunto. "
    scene c20s004_230c with fade
    "Te tumbas entre las dos bellezas y os acomodáis en la estrecha cama."
    mcd "Entonces... ¿Os quedáis a dormir?"
    emmd "Sí. No vas a echar a dos chicas desnudas de tu habitación, ¿no? *Risa*"
    erid "Ni vas a dejar a una chica desnuda dormir en el armario, ¿verdad?"
    erid "Beagan, puedes salir y unirte si quieres, pero no hagas travesuras."
    scene c20s004_260An with dissolve
    "El Hada abre el armario y revolotea hasta sentarse en la base de tu flácida polla."
    scad "Creo que voy a estar mejor aquí que en el armario. *Risa* Hay que decirle a Marzia que limpie más a fondo. Había una bola de pelusa como mi cabeza."
    emmd "*Risa* Bueno, tu cabeza es pequeña."
    erid "*Risa* Mientras no sea como la de Paula, ya sabes que tiene la cabeza grande..."
    scene c20s004_260e with dissolve
    emmd "*Risa* No te metas conmigo. Ya pareces Pia, siempre metiéndose con todo el mundo."
    if not dap._var("rejectedPia"):
        scad "Hablando de Pia..."
        erid "Puedes salir de debajo de la cama, Pia. O te vas a comer todos los pedos que Paula se tire por la noche."
        emmd "¡Yo no me tiro pedos mientras duermo! *Risa* ¡Son fragantes arcoiris!"
        call BlinkXP ("c20s004_265" , "f") from _call_BlinkXP_3667
        dapd "¿Cómo sabías que estaba ahí abajo?"
        scene c20s004_260e with dissolve
        erid "La próxima vez que quieras esconderte, recuerda esconder también tu ropa."
        emmd "Únete a nosotras. La cama es estrecha pero te haremos hueco."
        scad "Esto no lo hemos hecho nunca, dormir las cuatro con el mismo hombre."
        scene c20s004_260f with dissolve
        dapd "Siempre hay una primera vez para todo. Buenas noches."
        todas "Buenas noches."
    else:
        scad "La pobre Pia estará durmiendo sola en su habitación."
        erid "Ni se te ocurra invitarla ahora o mañana nos dará la charla."
        emmd "Dejemos dormir a Vilfredo o vendrá Fang a despertarlo y nos pillará aquí a todas. Buenas noches a todos."
        todas "Buenas noches."
    stop music fadeout (1.5)
    mcd "Buenas noches, chicas."
    return
label c20s004_Faces:
    call OrgasmX ("c20s004_235") from _call_OrgasmX_78
    mcdd "¡Mpfft!"
    "Explotas llenando sus caras de semen alternativamente."
    emmdd "¡Sí! ¡Dame toda tu leche!"
    eridd "¡Cubre nuestras caras con tu semilla!"
    scene c20s004_240a with dissolve
    eridd "Ha sido fantástico, Vilfredo..."
    emmdd "Una de las mejores noches de nuestra vida."
    if lesbianAngelDevil:
        scene c20s004_240b with dissolve
        "Sin que te sorprenda nada de estas dos mujeres, empiezan a lamerse todo tu semen de sus caras hasta no dejar ni una gota."
    else:
        scene c20s004_240d with dissolve
        "Se dirigen al armario de al lado de la chimenea, donde Marzia te ha dicho que están guardadas las toallas, y se limpian el semen de sus caras."
    return
label c20s004_Tits:
    call OrgasmX ("c20s004_250") from _call_OrgasmX_79
    mcdd "¡Mpfft!"
    "Explotas llenando sus tetas de semen alternativamente."
    emmdd "¡Sí! ¡Dame toda tu leche!"
    eridd "¡Cubre nuestras tetas con tu semilla!"
    scene c20s004_255a with dissolve
    eridd "Ha sido fantástico, Vilfredo..."
    emmdd "Una de las mejores noches de nuestra vida."
    if lesbianAngelDevil:
        scene c20s004_255b with dissolve
        "Sin que te sorprenda nada de estas dos mujeres, empiezan a lamerse todo tu semen de sus tetas hasta no dejar ni una gota."
    else:
        scene c20s004_250d with dissolve
        "Se dirigen al armario de al lado de la chimenea, donde Marzia te ha dicho que están guardadas las toallas, y se limpian el semen de sus caras."
    return
label c20s004_Farewell: #8
    if _in_replay and not AuxReplay:
        menu:
            "¿Rechazaste a Beagan?"
            "No":
                $ sca._var("rejectedBeagan" , False)
                menu:
                    "¿Rechazaste a Aelia y a Paula?"
                    "No":
                        $ mc._var("rejectedAeliaPaula" , False)
                    "Sí":
                        $ mc._var("rejectedAeliaPaula" , True)
            "Sí":
                $ sca._var("rejectedBeagan" , True)
                $ mc._var("rejectedAeliaPaula" , True)
        call c20_DefineCharacters from _call_c20_DefineCharacters_9
    call BlinkXP ("c20s003_825" , "d") from _call_BlinkXP_3668
    play music ("music/dnd/one-bard-band.ogg")
    dap "Por la mañana canta un gallo."
    if sca._var("rejectedBeagan"):
        $ mc._var("rejectedAeliaPaula" , True)
        $ dap._var("rejectedPia" , True)
    if not mc._var("rejectedAeliaPaula"):
        dap "Vilfredo se despierta solo en su cama."
    if sca._var("rejectedBeagan"):
        scene c20s003_345d with pixellate
        dap "Llaman a la puerta."
        play sound ("music/knock.ogg")
        "*Knock-Knock*"
        marziad "*A través de la puerta* Soy Marzia. ¿Puedo pasar?"
        mcd "Sí, pasa, por favor."
        call BlinkXP ("c20s004_300" , "d") from _call_BlinkXP_3669
        marziad "Buenos días, Vilfredo. El desayuno está listo y os he preparado unas provisiones para vuestro viaje."
        marziad "Pia me ha dicho que te las de a ti. No entiendo por qué. Las tienes abajo, al lado de la barra."
        mcd "Gracias, Marzia. Ahora me vestiré e iré a recogerlas."
    call BlinkXP ("c20s004_305" , "f") from _call_BlinkXP_3670
    dap "*En el mundo real* Vilfredo y Fang se reúnen en la sala común para desayunar antes de partir."
    mcd "Marzia nos ha preparado unas provisiones para el viaje. Acuérdate de agradecérselo."
    madd "No lo dudes. Deberíamos acabar esto e irnos si no queremos que nos pille la lluvia en el camino. Lloverá hacia mediodía."
    mcd "Perfecto. ¿Tienes que coger algo de tu habitación? Yo lo he bajado todo ya."
    call BlinkXP ("c20s004_310" , "d") from _call_BlinkXP_3671
    madd "Yo también. Júpiter está fuera guardando mis alforjas."
    mcdd "Pues cuando quieras, nos podemos ir."
    scene c20s004_315a with fade
    dap "*En el mundo real* Os despedís de Marzia..."
    mad "*En el mundo real* Nos aseguramos de darle las gracias por las provisiones."
    scene c20s004_315b with fade
    mad "*En el mundo real* También nos despedimos de Alba, la chica a la que gritó que se ocupara de los clientes cuando llegaron los BDSM. Supongo que debe ser su ayudante."
    mc "*En el mundo real* Ni siquiera me acordaba de ella... no hemos interactuado con ella para nada."
    mad "*En el mundo real* Bueno, se supone que si es la camarera de la taberna, nos habrá traído comida o bebida."
    dap "*En el mundo real* Bien visto, Maddie. Scarlett, [eri], y [emm] casi siempre se olvidan de ella."
    dap "*En el mundo real* No hay rastro de Beagan, Aelia, Paula, o Pia."
    mc "*En el mundo real* Le pedimos a Marzia que nos despida de ellas y nos vamos a los establos. No olvido las provisiones."
    scene c20s004_320a with fade
    dap "*En el mundo real* De camino a los establos veis a Thiel y el chico de la alabarda charlando, sentados en un banco."
    scene c20s004_320b with dissolve
    dap "*En el mundo real* ¡Están cogidos de la mano! *Risa* Parece que tu fallo crítico ha creado una pareja en el pueblo."
    scene c20s004_320a with dissolve
    mc "*En el mundo real* Me acerco a ellos para despedirnos... pero solo si no parece que vaya a interrumpir algo."
    mad "*En el mundo real* Yo también me acerco. Quiero despedirme de los tortolitos."
    scene c20s004_320c with dissolve
    mcd "Thiel, [wil], nos vamos ya. Un placer haberos conocido."
    madd "Lo mismo digo, chicos."
    call BlinkXP ("c20s004_325" , "d") from _call_BlinkXP_3672
    thi "Muchas gracias por lo de ayer. Es una lástima que no se puedan quedar ustedes en el pueblo. La Señora Paula ya nos ha dicho que se tienen que marchar."
    call BlinkXP ("c20s004_330" , "d") from _call_BlinkXP_3673
    madd "Sí, muchacha. Vamos a buscar trabajo a Vindobona."
    mcd "Nos han dicho que aquí no vamos a encontrar trabajo escoltando caravanas."
    call BlinkXP ("c20s004_335" , "d") from _call_BlinkXP_3674
    wil "Pero aquí hay mucho trabajo si lo quieren, hay muchas granjas sin manos que las trabajen. O podrían trabajar para las Protectoras."
    mcd "Suena tentador, pero no es el tipo de trabajo que buscamos ahora mismo."
    call BlinkXP ("c20s004_340" , "d") from _call_BlinkXP_3675
    thi "Es una lástima. Echaré de menos a Júpiter, Señora. Me cae muy bien. Me ha pedido que le dé las gracias por lo de Capua. No me ha dicho de qué se trata."
    call BlinkXP ("c20s004_345" , "h") from _call_BlinkXP_3676
    madd "¿Qué? ¿Puedes hablar con Júpiter?"
    call BlinkXP ("c20s004_350" , "d") from _call_BlinkXP_3677
    thi "Claro... Soy una chica gato, al fin y al cabo. Habla con un acento raro, pero nos entendemos."
    mcd "*Risa* Me parece la mejor explicación que he oído nunca."
    thi "Él le entiende casi todo lo que dice, al menos cuando habla Latín, pero no puede contestarle."
    call BlinkXP ("c20s004_355" , "d") from _call_BlinkXP_3678
    mad "*En el mundo real* Abrazo a Júpiter."
    madd "Sabes que eres mi compañero, gatito."
    jup "*Ronroneo*"
    thi "Dice que no podría tener una compañera mejor."
    scene c20s004_320c with dissolve
    mcd "Sólo queríamos despedirnos, chicos. Ha sido un placer conoceros."
    call BlinkXP ("c20s004_360" , "d") from _call_BlinkXP_3679
    wil "Guardaré su moneda siempre, Señor. Muchas gracias."
    mcd "*Susurrando* Si puedo darte un consejo, ponte un nombre más fácil de recordar, [wil]."
    mc "*En el mundo real* *Risa*"
    call BlinkXP ("c20s004_365a" , "d") from _call_BlinkXP_3680
    wil "¡Oh, lo haré! Cuando tenga mi propia AVN."
    call BlinkXP ("c20s004_365a" , "v") from _call_BlinkXP_3681
    mc "*En el mundo real* ¿Qué? ¿AVN?" (multiple=2)
    mcd "¿Qué quieres decir con AVN?" (multiple=2)
    call BlinkXP ("c20s004_365b" , "d") from _call_BlinkXP_3682
    wil "Oh, sí, Señor. Agrum Vaccis Nostrum. Nuestro propio campo con vacas, para alimentar a mi familia."
    mcd "Me habías asustado, creía que te referías a otra cosa..."
    dap "*En el mundo real* *Risa* Eso es porque tienes una mente traviesa."
    scene c20s004_320c with dissolve
    thi "No queremos entretenerles más, o si no van a llegar cuando las puertas de Vindobona ya estén cerradas."
    mcd "Gracias, Thiel. Si volvemos a hacer esta ruta pararemos a saludaros."
    madd "Cuidaos, chicos."
    wil "Tengan cuidado ustedes en el camino. A veces... pasan cosas... y los viajeros desaparecen."
    scene c20s004_370a with fade
    dap "*En el mundo real* Cuando llegáis a los establos, veis que Paula, Aelia, Beagan y Pia están allí. Esta vez sin armaduras."
    scene black with dissolve
    centered "{size=+20}{b}DÍA 21 – LUNES{/b}{/size}"
    call BlinkXP ("c20s004_375" , "d") from _call_BlinkXP_3683
    dapd "Creía que habíais decidido quedaros."
    call BlinkXP ("c20s004_380" , "d") from _call_BlinkXP_3684
    erid "Si nosotras tuviéramos que ir a Vindobona, Pia nos hubiera hecho salir al amanecer."
    call BlinkXP ("c20s004_385" , "d") from _call_BlinkXP_3685
    scad "Y se hubiera pasado el camino quejándose de que no había dormido suficiente."
    call BlinkXP ("c20s004_390" , "d") from _call_BlinkXP_3686
    emmd "No os metáis con Pia. Al menos nos evita tener que hacer todos los cálculos de las provisiones que necesitamos."
    call BlinkXP ("c20s004_395" , "d") from _call_BlinkXP_3687
    mad "Muchas gracias por las cervezas de anoche, chicas."
    mcd "Y por lo de después... la cena... me refiero..."
    scene c20s004_370b with dissolve
    emmd "Hemos ensillado vuestros caballos..."
    erid "Y os hemos puesto un par de mantas extra, en caso de que encontréis una caravana que vaya más al norte de Vindobona. Hace frío allí."
    dapd "Si volvéis a pasar por Novum Templum, no os olvidéis de parar a saludar."
    scad "Y a traernos noticias de lo que pasa en el resto del Imperio. Casi no nos enteramos de nada aquí."
    stop music fadeout (1.5)
    scene c20s004_400a with pixellate
    call BlinkXP ("c20s004_400" , "d") from _call_BlinkXP_3688
    mad "¿Queda mucho, [dap]? Mañana me tengo que levantar pronto para abrir la tienda."
    mad "No quiero estropear la partida, pero si va a durar mucho más, ¿podríamos dejarlo para otro día?"
    call BlinkXP ("c20s004_405a" , "d") from _call_BlinkXP_3689
    dap "Solo quedan diez minutos a lo sumo. Vamos a acelerar un poco."
    dap "Acabáis las despedidas y emprendéis camino. Es un día soleado. Parece que la amenaza de lluvia va desapareciendo tal como vais hacia el norte."
    if not mc._var("rejectedAeliaPaula"):
        call BlinkXP ("c20s004_405b" , "d") from _call_BlinkXP_3690
        emm "Vaya, yo quería despedirme de Vilfredo como es debido."
        call BlinkXP ("c20s004_405c" , "d") from _call_BlinkXP_3691
        eri "[emm], Maddie es la única aquí que tiene que madrugar. Tenemos que adaptar la partida a ella."
        eri "Y ni se te ocurra sentirte mal, Maddie. Lo hacemos encantadas."
        call BlinkXP ("c20s004_405d" , "d") from _call_BlinkXP_3692
        mad "Gracias, [eri]."
    call BlinkXP ("c20s004_405e" , "d") from _call_BlinkXP_3693
    dap "Bueno, vamos a acelerar un poco."
    dap "Cuando lleváis un par de horas cabalgando oís un ruido. Tirad por Percepción."
    call BlinkXP ("c20s004_410" , "d") from _call_BlinkXP_3694
    mad "15. Con los bonos sumados, 18."
    mc "12... ¿qué bonos había que sumar?... Ah, sí, Sabiduría. No tengo bono. 12."
    scene c20s004_415a with pixellate #hay varias más con zoom
    play music ("music/dnd/folkvangr.ogg")
    dap "*En el mundo real* Miráis al cielo, hacia el Norte, y veis un dragón, rojo infernal, volando hacia el Oeste."
    dap "*En el mundo real* Maddie, tu dirías que es un ejemplar muy viejo, y que llevaba algo en las garras, pero no puedes percibir qué es."
    dap "*En el mundo real*  Además, ves al Noreste una pequeña columna de humo."
    call BlinkXP ("c20s004_420a" , "d") from _call_BlinkXP_3695
    madd "¿Has visto el dragón?"
    mcd "Nunca había visto uno. Creo que será difícil olvidarlo..."
    call BlinkXP ("c20s004_420b" , "d") from _call_BlinkXP_3696
    madd "Hay humo allí. Deberíamos acercarnos."
    mcd "Te sigo. A lo mejor alguien necesita ayuda."
    scene c20s004_425e with dissolve
    madd "Por aquí. Este camino parece llevar hacia el humo."
    scene c20s004_425d with fade
    dap "*En el mundo real* Llegáis a un claro al lado del camino, donde alguien ha acampado para comer."
    dap "*En el mundo real* No hay nadie, pero el fuego está encendido aún con carne en el espeto. Obiamente, la columna de humo salía de aquí."
    mad "*En el mundo real* Busco huellas. 8+3. 11. No creo que encuentre nada demasiado interesante."
    dap "*En el mundo real* Ves huellas que van en varias direcciones. El grupo más numeroso va al Norte."
    call BlinkXP ("c20s004_425" , "d") from _call_BlinkXP_3697
    madd "El grupo que había acampado aquí se ha separado. Vamos a seguir las huellas que van al Norte."
    mcd "Como quieras. Tu te mueves por los bosques mejor que yo."
    scene c20s004_430a with dissolve
    dap "*En el mundo real* Llegáis a un claro en el que encontráis una escena dantesca. Hay un par de cadáveres quemados. Uno boca arriba y el otro boca abajo."
    dap "*En el mundo real* No parecen haber sido atacados aquí, sino un poco antes, donde habéis visto hierba quemada. Parece que han corrido hasta aquí antes de morir."
    dap "*En el mundo real* Reconocéis la armadura que llevaban los alabarderos en uno de los cadáveres. No lleva la capa."
    mc "*En el mundo real* Le doy la vuelta al otro."
    scene c20s004_430b with dissolve
    dap "*En el mundo real* Incluso antes de darle la vuelta, reconoces la armadura. Es la misma que llevaba Euricus, aunque le faltan algunas piezas."
    dap "*En el mundo real* En el momento en que le das la vuelta, lo reconoces pese a que está bastante churruscado."
    mad "*En el mundo real* ¿Está el cadáver de Solomon por algún lado?"
    dap "*En el mundo real* Tira por Inteligencia."
    mad "*En el mundo real* ¡Sí! 20 natural. Pero le resto 1. Fang no es muy inteligente."
    dap "*En el mundo real* Para nosotras, un 20 natural siempre es un éxito crítico. Así simplificamos las normas."
    scene c20s004_430An with dissolve
    dap "*En el mundo real* Recuerdas la cosa negra que llevaba el dragón entre las garras. Crees que podría ser Solomon."
    mad "*En el mundo real* ¡Sí! !Acabar como el almuerzo de un dragón! ¡Ahí tienes tu criatura roja infernal chupadora de almas! ¡Jódete, cabrón! ¡Uy, perdón!"
    todas "*Risa*"
    call BlinkXP ("c20s004_435" , "d") from _call_BlinkXP_3698
    madd "Creo que deberíamos volver a Novum Templum, Vilfredo. Deberíamos avisarles de que hay un dragón en las inmediaciones."
    mcd "Me parece que no deben saberlo, o nos lo hubieran dicho. ¡Volvamos!"
    madd "Vamos. Vindobona tendrá que esperar."
    scene c20s004_435d with dissolve
    mcd "Fang, presiento que este es el comienzo de una hermosa amistad." #Fang, I think this is the beginning of a beautiful friendship
    scene c20s004_440a with pixellate
    call BlinkXP ("c20s004_440" , "d") from _call_BlinkXP_3699
    stop music fadeout (1.5)
    dap "Y con esto acaba la sesión de hoy. Espero que os haya gustado."
    return
label c20s005_EndGameFarewell: #9
    if _in_replay and not AuxReplay:
        menu:
            "¿Rechazaste a Beagan?"
            "No":
                $ sca._var("rejectedBeagan" , False)
                menu:
                    "¿Rechazaste a Pia?"
                    "No":
                        $ dap._var("rejectedPia" , False)
                    "Sí":
                        $ dap._var("rejectedPia" , True)
                menu:
                    "¿Rechazaste a Aelia y a Paula?"
                    "No":
                        $ mc._var("rejectedAeliaPaula" , False)
                    "Sí":
                        $ mc._var("rejectedAeliaPaula" , True)
            "Sí":
                $ sca._var("rejectedBeagan" , True)
                $ mc._var("rejectedAeliaPaula" , True)
                $ dap._var("rejectedPia" , True)
        call c20_DefineCharacters from _call_c20_DefineCharacters_10
        call BlinkXP ("c20s004_440" , "d") from _call_BlinkXP_3700
        dap "Y con esto acaba la sesión de hoy. Espero que os haya gustado."
    play music ("music/ChillUkelele.ogg")
    call BlinkXP ("c20s005_005" , "d") from _call_BlinkXP_3701
    mad "Como introducción al mundo y al grupo ha sido fantástico."
    mad "No es la típica forma de introducir nuevos miembros en plan \"Os encontráis en una taberna y parecéis amigos de toda la vida\"."
    if not sca._var("rejectedBeagan"):
        call BlinkXP ("c20s005_010" , "d") from _call_BlinkXP_3702
        sca "Es más un \"Os encontráis en el foro y os folláis al Semielfo\". *Risa*"
        todas "*Risa*"
        if not mc._var("rejectedAeliaPaula"):
            call BlinkXP ("c20s005_015" , "d") from _call_BlinkXP_3703
            emm "*Risa* Había que darle razones para volver, ¿no?"
            mc "*Risa* Creo que [dap] nos hubiera dado razones suficientes igualmente."
            call BlinkXP ("c20s005_020" , "d") from _call_BlinkXP_3704
            eri "Ahora hay que darle razones a [madd] para que se quede."
    call BlinkXP ("c20s005_025" , "d") from _call_BlinkXP_3705
    dap "Por eso habéis conocido a unos enemigos comunes. Además, Vilfredo y Fang volverán para dar la noticia del dragón."
    dap "Suma a eso que ahora Fang tiene una razón para quedarse. Tiene un intérprete para hablar con Júpiter."
    if not sca._var("rejectedBeagan"):
        call BlinkXP ("c20s005_030" , "d") from _call_BlinkXP_3706
        mad "Y visto lo que pasó anoche, quizás se plantee probar a Vilfredo. Aunque también podría haberlo hecho en Vindobona."
        if not mc._var("rejectedAeliaPaula") and not dap._var("rejectedPia"):
            call BlinkXP ("c20s005_035" , "d") from _call_BlinkXP_3707
            mad "*Risa* Es la única idiota que se fue a dormir y se quedó sin diversión."
        call BlinkXP ("c20s005_040" , "d") from _call_BlinkXP_3708
        bet "A mí me ha parecido muy interesante descubrir esas facetas de mis cuatro sobrinas."
    else:
        call BlinkXP ("c20s005_040" , "d") from _call_BlinkXP_3709
        bet "A mí me ha parecido muy interesante descubrir esas facetas de mis cuatro sobrinas, aunque [mc] las rechazara."
    call BlinkXP ("c20s005_045" , "d") from _call_BlinkXP_3710
    dap "¿Por qué no te unes, Tía Betty? Siempre hay espacio para más Clérigos en el grupo. Los hechizos de curación de Pia no son eternos y ahora somos más."
    call BlinkXP ("c20s005_050" , "d") from _call_BlinkXP_3711
    bet "*Risa* ¿Me estás diciendo que me una al grupo y me haga una monja curandera en vez de follarme al Semielfo?"
    bet "¿Tú te das cuenta de la ironía de eso? *Risa* Me he pasado casi toda mi vida siendo precisamente una monja curandera."
    call BlinkXP ("c20s005_055" , "d") from _call_BlinkXP_3712
    sca "*Risa* Creo que [dap] no lo había pensado. Si quieres puedes jugar con un guerrero o un mago..."
    sca "Aunque te hagas una monja, te puedes follar a [mc] igualmente. *Risa*"
    if not sca._var("rejectedBeagan") and not dap._var("rejectedPia"):
        sca "Sólo tienes que ver a [dap], la Semielfa putilla. *Risa*"
    call BlinkXP ("c20s005_055b" , "d") from _call_BlinkXP_3713
    bet "Me ha parecido que os lo pasabais muy bien. Podría ser divertido unirme, ahora que parece que no voy a volver a Florida."
    call BlinkXP ("c20s005_060" , "d") from _call_BlinkXP_3714
    bet "Pero dejadme pensarlo unos días..."
    mcp "(Al menos hasta la visita a Monterey, ¿no?)"
    call BlinkXP ("c20s005_065" , "d") from _call_BlinkXP_3715
    emm "No es que te quiera echar, Mads, pero ¿tú no tenías que madrugar?"
    call BlinkXP ("c20s005_070" , "d") from _call_BlinkXP_3716
    mad "Sí, pero una de las cosas más divertidas de las partidas es comentarlas luego... Estoy dispuesta a sacrificar una hora de sueño."
    call BlinkXP ("c20s005_075" , "d") from _call_BlinkXP_3717
    eri "No es necesario, Maddie. Mañana iremos todas a la tienda y comentaremos la partida si quieres. Así puedes dormir tranquilamente hoy."
    call BlinkXP ("c20s005_080" , "d") from _call_BlinkXP_3718
    sca "Prometemos no comentar nada antes de ir, para que no te pierdas nada de la conversación."
    call BlinkXP ("c20s005_085" , "d") from _call_BlinkXP_3719
    mad "Chicas, os lo agradezco. Ha sido un día largo y empiezo a estar cansada."
    if not sca._var("rejectedBeagan"):
        call BlinkXP ("c20s005_090" , "d") from _call_BlinkXP_3720
        mad "Casi tanto como Vilfredo. *Risa*"
        mc "¡Hey! El Semielfo ya ha recargado las baterías. Está listo para más rounds. *Risa*"
    call BlinkXP ("c20s005_095" , "d") from _call_BlinkXP_3721
    dap "Entonces quedamos así. Mañana en la tienda. No te queremos entretener más y sentirnos culpables si te quedas dormida en un probador. *Risa*"
    todas "*Risa*"
    call BlinkXP ("c20s005_100" , "d") from _call_BlinkXP_3722
    mad "Gracias, chicas."
    mc "Te llevo. ¿Tienes que coger alguna cosa?"
    call BlinkXP ("c20s005_105" , "d") from _call_BlinkXP_3723
    mad "Tengo la mochila en la habitación de [eri]. Ahora bajo con ella. Las cajas de los cuadros ya están en la camioneta."
    mc "Perfecto entonces. Voy al lavabo y te veo en el garaje."
    eri "Te acompaño, Maddie."
    scene black with dissolve
    stop music fadeout (1.5)
    "Te despides de las chicas y de Tía Betty y vas al lavabo."
    if kia._var("route"):
        call c20s005_Kia from _call_c20s005_Kia
    return
label c20s005_Kia: #10
    if _in_replay:
        menu:
            "¿Estás en una relación con Maddie?"
            "Sí":
                $ mad._var("route" , True)
            "No":
                $ mad._var("route" , False)
    call BlinkXP ("c20s005_110" , "f") from _call_BlinkXP_3724
    play music ("music/CelticFlute.ogg")
    "Al salir del lavabo, te encuentras con Kiara en el pasillo."
    mc "¡Hola, Kiara! Perdón si te he despertado."
    if not _in_replay:
        $ kia.profileImages.pop (7) # first remove
        $ kia.profileImages.insert (7, ("kiara_7", "route")) # then add new
        $ texto = str(mar.name)
        $ renpy.notify ("Profile Image unlocked for Kiara: 08 - Lingerie")
    kia "No te preocupes. No podía dormir y te he escuchado subir las escaleras. He venido a ver si tenías un momento para hablar."
    mc "Ahora no es buen momento, Kiara. Tengo que llevar a Maddie a casa."
    if mad._var("route"):
        call BlinkXP ("c20s005_115" , "d") from _call_BlinkXP_3725
        kia "¿Vas a volver a casa o te vas a quedar a dormir?"
        call BlinkXP ("c20s005_120" , "v") from _call_BlinkXP_3726
        kia "No te estoy fiscalizando... Es que me gustaría hablar contigo..."
    else:
        call BlinkXP ("c20s005_125" , "d") from _call_BlinkXP_3727
        kia "¿Vas a tardar mucho? Me gustaría hablar contigo..."
    mc "La llevo a casa y vuelvo en seguida. ¿Quieres que hablemos cuando vuelva?"
    call BlinkXP ("c20s005_130" , "d") from _call_BlinkXP_3728
    kia "Me parece fantástico. Te veo en un rato, entonces."
    mc "¿No vas a darme un beso antes de irme?"
    call BlinkXP ("c20s005_135" , "d") from _call_BlinkXP_3729
    kia "Creía que era solamente en los buenos días y buenas noches..."
    mc "Así era antes de que tú y yo estuviéramos juntos."
    mc "Porque estamos juntos, ¿verdad?"
    call BlinkXP ("c20s005_140" , "d") from _call_BlinkXP_3730
    kia "De eso es de lo que quiero hablar contigo... Pero mejor luego, cuando vuelvas."
    mc "Como desees."
    scene c20s005_145a with dissolve
    kia "Hasta dentro de un rato, [mc]."
    stop music fadeout (1.5)
    mc "Hasta luego, Kiara."
    if _in_replay:
        call c20s006_ReturningHome from _call_c20s006_ReturningHome_1
    return
label c20s005_GivingMaddieARide:#11
    if _in_replay:
        menu:
            "¿Estás en una relación con Maddie?"
            "Sí":
                $ mad._var("route" , True)
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
                        menu:
                            "¿Estás en alguna las rutas de dominación con Maddie?"
                            "Sí":
                                menu:
                                    "¿Cómo es la relación?"
                                    "La domino":
                                        $ mad._var("dom" , False)
                                        $ mad._var("sub" , True)
                                    "Me dejo dominar":
                                        $ mad._var("dom" , True)
                                        $ mad._var("sub" , False)
                                $ mad._var("romance" , False)
                                $ mar._var("route", True)
                                $ mar._var("fittingRoom" , True)
                            "No, no espié a [mar], con lo que no apareció la opción":
                                $ mad._var("romance" , True)
                                $ mad._var("dom" , False)
                                $ mad._var("sub" , False)
                                $ mar._var("fittingRoom" , False)
                            "No, pero espié a [mar]":
                                $ mad._var("romance" , True)
                                $ mad._var("dom" , False)
                                $ mad._var("sub" , False)
                                $ mar._var("fittingRoom" , True)
                        menu:
                            "¿Estás saliendo con alguien aparte de Maddie y [mar]?"
                            "Sí":
                                $ mc._var("relationships", 3, intention = "set")
                            "No":
                                $ mc._var("relationships", 2, intention = "set")
                    "No":
                        $ mar._var("route" , False)
                        $ mad._var("romance" , True)
                        $ mad._var("dom" , False)
                        $ mad._var("sub" , False)
                        $ mar._var("fittingRoom" , False)
            "No":
                $ mad._var("route" , False)
    call BlinkXP ("c20s005_200" , "f") from _call_BlinkXP_3731
    play music ("music/romantic-day.ogg")
    "Unos minutos después, después de haber sacado la camioneta del garaje..."
    mad "Ya nos podemos ir. Ya me he despedido de las chicas y de Betty."
    mc "Cuando quieras podemos irnos, entonces."
    call BlinkXP ("c20s005_205" , "f") from _call_BlinkXP_3732
    "Al llegar al edificio de Maddie le ayudas a subir las cajas de los cuadros y te despides de ella."
    mad "Muchas gracias por todo, [mc]. Ha sido un día fantástico."
    mc "Bienvenida a la familia. Bienvenida a los Locos Marks. *Risa* Espero que, a partir de ahora vengas a casa más a menudo."
    if not mad._var("route"):
        call BlinkXP ("c20s005_210" , "d") from _call_BlinkXP_3733
        mad "Lo haré, no lo dudes. Ahora, si no te importa, debería irme a dormir."
        mc "Ningún problema. ¿Zeus está durmiendo? Me gustaría conocerlo."
        scene c20s005_215a with dissolve
        python:
            if "zeu" not in globals () or not isinstance (zeu, TGCharacter):
                zeu = TGCharacter ("Zeus", color = "#0023ff")
                cat = TGCharacter (_("Jodido Gato"), color = "#0023ff")
        "Parece que el gato ha oído su nombre y aparece para saludar."
        zeu "*Ronroneo* (¿Quién eres tú? ¿Vienes a acariciarme? ¡Bien hecho, humano!)"
        mc "*Risa* Parece que me ha oído."
        mad "*Risa* En cuanto oye su nombre aparece como salido de la nada. Si son mis amigas se vuelve a esconder."
        mad "Parece que contigo tiene curiosidad."
        scene c20s005_215b with dissolve
        zeu "*Ronroneo* (Sus amigas son idiotas y se ríen como gallinas. Eres un humano que acaricia bien, me gustas.)"
        mc "Encantado de conocerte por fin, Zeus. He visto unos cuadros fantásticos tuyos."
        zeu "*Ronroneo* (Soy muy versátil. Gótico y Científico a la vez. No hablaremos del vestido rosa. Eso nunca pasó. Tengo que hablar con mi psicólogo.)"
        call BlinkXP ("c20s005_205" , "d") from _call_BlinkXP_3734
        mc "Bueno, Maddie, te dejo ir a acostarte. A ver si mañana puedo pasarme por la tienda con las chicas para comentar la partida."
        mad "OK. Hasta mañana, [mc]."
        scene black with dissolve
        stop music fadeout (1.5)
        "Te subes a la camioneta y emprendes el camino a casa."
        return
    call BlinkXP ("c20s005_210" , "d") from _call_BlinkXP_3735
    mad "Lo haré. No puedo dejar a Vilfredo solo en el bosque, habiendo un dragón rondando por ahí. *Risa*"
    mc "No me refiero solo a las partidas de DnD. Me refiero a las actividades familiares."
    mc "Le has caído genial a todo el mundo que no te conocía, y ya les gustabas a las que te conocían."
    if mad._var("dom") or mad._var("sub"):
        call BlinkXP ("c20s005_220" , "d") from _call_BlinkXP_3736
        mad "Sobre eso..."
        mc "¿Qué pasa Maddie?"
        if mad._var("dom"):
            call BlinkXP ("c20s005_225" , "d") from _call_BlinkXP_3737
            mad "Me mentiste..."
            mc "¿En qué? No lo entiendo. Nunca te he mentido."
            call BlinkXP ("c20s005_230" , "d") from _call_BlinkXP_3738
            mad "Estás saliendo con [mar]..."
            if mar._var("pregnancyDiscovered"):
                mad "Incluso está embarazada..."
            mc "Nunca te dije que no lo estuviera haciendo..."
            call BlinkXP ("c20s005_235" , "d") from _call_BlinkXP_3739
            mad "Pero aceptaste mi chantaje."
            mc "Porque quería ver dónde iba. Quería probar como era sentirse dominado."
            call BlinkXP ("c20s005_240" , "d") from _call_BlinkXP_3740
            mad "Me estás diciendo que nunca tuve poder sobre ti, ¿no?"
            mc "No es eso. Tenías poder sobre mí porque yo te lo dejaba tener. No porque el secreto que guardabas fuera a hacerme daño si lo revelabas."
            mc "Seguramente [mar] se sentiría halagada si lo hicieras."
            call BlinkXP ("c20s005_245" , "d") from _call_BlinkXP_3741
            mad "Me alegro de que lo hicieras. Aunque me he sentido un poco idiota cuando he descubierto la verdad."
            mad "Y eso me lleva a otra pregunta..."
            mc "Dime, Maddie. Sabes que puedes hablar de cualquier cosa conmigo."
            call BlinkXP ("c20s005_250" , "d") from _call_BlinkXP_3742
            mad "¿Quiere decir eso que estabas conmigo porque querías? ¿No porque yo te obligara?"
            mc "Sí. Estaba contigo porque quería. No podías obligarme, Maddie. El secreto no tenía ningún poder sobre mí."
            call BlinkXP ("c20s005_255" , "d") from _call_BlinkXP_3743
            mad "Entonces te libero. No quiero estar contigo así."
        else:
            call BlinkXP ("c20s005_225" , "d") from _call_BlinkXP_3744
            mad "Me mentiste..."
            mc "¿En qué? No lo entiendo. Nunca te he mentido."
            call BlinkXP ("c20s005_230" , "d") from _call_BlinkXP_3745
            mad "Estás saliendo con [mar]..."
            if mar._var("pregnancyDiscovered"):
                mad "Incluso está embarazada..."
            mc "Nunca te dije que no lo estuviera haciendo..."
            call BlinkXP ("c20s005_235" , "d") from _call_BlinkXP_3746
            mad "Pero mi intento de chantaje..."
            mc "Tú intentaste chantajearme antes de que estuviéramos juntos. Nada cambia."
            call BlinkXP ("c20s005_240" , "d") from _call_BlinkXP_3747
            mad "Me estás diciendo que, aunque hubiera salido bien nunca hubiera tenido poder sobre ti, ¿no?"
            mc "Más o menos. A menos que yo te lo hubiera dejado tener. Seguramente [mar] se sentiría halagada si lo hicieras."
            mc "Pero le dimos la vuelta y ahora soy yo el que tiene poder sobre ti, ¿no?"
            call BlinkXP ("c20s005_245" , "d") from _call_BlinkXP_3748
            mad "Me alegro de que lo hicieras. Aunque me he sentido un poco idiota cuando he descubierto la verdad."
            mad "Y eso me lleva a otra pregunta..."
            mc "Dime, Maddie. Sabes que puedes hablar de cualquier cosa conmigo."
            call BlinkXP ("c20s005_250" , "d") from _call_BlinkXP_3749
            mad "¿Quiere decir eso que estás conmigo sólo porque tienes poder sobre mí?"
            mc "No. Estoy contigo porque quiero estarlo. No esperaba estarlo en estas circunstancias, pero me gusta estar contigo."
            call BlinkXP ("c20s005_255" , "d") from _call_BlinkXP_3750
            mad "Entonces, si quieres, puedes denunciarme a mi jefe."
            mad "No quiero estar contigo así."
        call BlinkXP ("c20s005_255" , "h") from _call_BlinkXP_3751
        mc "{b}¿Qué?{/b} ¿Estás rompiendo conmigo?"
        scene c20s005_255d with dissolve
        mad "Sí. Espérame aquí un momento. Ahora vuelvo."
        mc "¿Me he perdido algo? No te entiendo."
        scene c20s005_215a with dissolve
        zeu "¡Miau! (¿Qué le has hecho ahora? ¡Me caías bien!)"
        mc "Hola, pequeñín. ¿Sabes que le ha pasado a Maddie? ¿Me has echado de menos?"
        zeu "¡Miau! (No tengo ni idea de qué le has hecho. Y sobre echarte de menos, depende. ¿Me has traído atún para una cena tardía?)"
        scene c20s005_215b with dissolve
        zeu "*Ronroneo* (Vale, te perdono... Pero que no se vuelva a repetir.)"
        mc "Yo también te he echado de menos. Tus cuadros han triunfado mucho."
        zeu "*Ronroneo* (Soy muy versátil. Gótico y Científico a la vez. No hablaremos del vestido rosa. Eso nunca pasó. Tengo que hablar con mi psicólogo.)"
        call BlinkXP ("c20s005_260" , "f") from _call_BlinkXP_3752
        mad "Hola, [mc]. ¿Puedo ayudarte en algo?"
        mc "Hola de nuevo, Maddie. ¿Esas gafas?"
        call BlinkXP ("c20s005_265" , "d") from _call_BlinkXP_3753
        mad "Creo que te equivocas. Maddie vive aquí, pero no lleva gafas. Yo soy Madison... No... Claire... Kent."
        mcp "(OK. Sigamos el juego. Solo te falta una cabina de teléfono para cambiarte de vestimenta.)"
        mc "Perdón por la confusión. Mi amiga me ha dicho algo que no entiendo y se ha ido."
        call BlinkXP ("c20s005_270" , "d") from _call_BlinkXP_3754
        mad "Sí, ha roto contigo. No quiere seguir teniendo la relación que ha tenido hasta ahora."
        mad "Es una lástima... hacíais tan buena pareja..."
        mc "Pero no lo entiendo..."
        call BlinkXP ("c20s005_275" , "d") from _call_BlinkXP_3755
        mad "Es muy fácil de entender. Después de ver lo que puede ser tener una relación completa... romántica... contigo. No quiere tener un sucedáneo."
        if mad._var("sub"):
            mad "Dice que fue divertido, pero que no es lo suyo. Prefiere perder su trabajo a perder la oportunidad de tener algo más sincero contigo."
        else:
            mad "Dice que fue divertido, pero que no es lo suyo. Prefiere perder su poder, si es que lo tenía, a perder la oportunidad de tener algo más sincero contigo."
        mc "Yo pienso lo mismo. Tú no estabas hoy en mi casa, pero con todo el mundo tengo una relación basada en el respeto, no en guardar secretos."
        mc "Yo esperaba que nuestra relación evolucionara hacia algo más romántico. Pero si ha roto conmigo, creo que debería irme..."
        call BlinkXP ("c20s005_280a" , "v") from _call_BlinkXP_3756
        mad "¿Qué? ¡No!"
        call BlinkXP ("c20s005_280b" , "d") from _call_BlinkXP_3757
        mad "Digo..."
        mad "Puedo hacer que Maddie vuelva, si quieres. Estoy segura de que le gustaría oir lo que has dicho."
        mc "Sí, por favor. Hazla volver."
        scene c20s005_285d with dissolve
        mad "Un momento, por favor."
        call BlinkXP ("c20s005_285" , "d") from _call_BlinkXP_3758
        mad "Me ha dicho Claire que quieres hablar conmigo. Sobre por qué he roto contigo."
        mc "¿A qué viene esto, Maddie?"
        call BlinkXP ("c20s005_290" , "d") from _call_BlinkXP_3759
        mad "No sabía cómo decirte que quiero estar contigo... "
        if mc._var("relationships")==2:
            mad "... como estás con [mar]..."
        else:
            mad "... como estás con el resto de las chicas..."
        mad "Quiero una relación de verdad. Me gusta mucho lo que tenemos, pero... después de ver lo que podría tener... quiero más."
        mc "Y se te ha ocurrido este juego."
        call BlinkXP ("c20s005_295" , "d") from _call_BlinkXP_3760
        mad "Llevo desde la Gran Revelación pensando cómo hacerlo. Y al final no he usado ninguna de las ideas que tenía."
        mad "Quería hablarlo en la piscina, pero justo en ese momento ha llegado Debbie..."
        mad "Quiero olvidar lo que hemos hecho hasta ahora y empezar desde cero. ¿Crees que podríamos probarlo?"
        mc "No. Lo siento, Maddie."
        call BlinkXP ("c20s005_300" , "d") from _call_BlinkXP_3761
        mad "Pero..."
        mc "Déjame hablar un momento."
        mc "No quiero olvidar lo que hemos hecho hasta ahora. Creo que la evolución natural de lo que estábamos haciendo es lo que vamos a hacer ahora."
        mc "Pero eso no significa que no nos lo hayamos pasado bien."
        mc "Podemos tener una relación de verdad, pero sin dejar de hacer las cosas divertidas que hemos hecho hasta ahora."
        call BlinkXP ("c20s005_305" , "d") from _call_BlinkXP_3762
        mad "Me parece bien... ¿Significa que ahora soy una más de tus novias?"
        mc "No me gustan las etiquetas, pero si a ti te gustan, sí, eres una más."
        scene c20s005_305d with hpunch
        "Maddie se lanza a tus brazos buscando tus labios en un beso lleno de alivio."
        "El beso dura unos segundos antes de que se separe de ti."
        call BlinkXP ("c20s005_310" , "d") from _call_BlinkXP_3763
        mad "¡Gracias, [mc]! Estaba aterrorizada de planteártelo."
        mc "No me des las gracias. Los dos ganamos con este cambio. Es lo que los dos queremos."
        if mad._var("dom"):
            mc "Y nunca me pareció que estuvieras muy a gusto en el papel de dominatrix."
            call BlinkXP ("c20s005_315" , "d") from _call_BlinkXP_3764
            mad "No, no lo estaba. Me gustó probarlo y tener el control... pensar que tenía el control..."
        else:
            mc "Aunque me pareció que estabas muy a gusto en el papel de gatita sumisa."
            call BlinkXP ("c20s005_315" , "d") from _call_BlinkXP_3765
            mad "Si, lo estaba. Me gustó probarlo y saber que no tenía el control..."
        mad "Pero no estoy hecha para eso. Soy demasiado... normal..."
        if mc._var("relationships") > 2:
            mc "*Risa* No, Maddie. No eres normal. No creo que \"normal\" incluya compartir a su novio con otras mujeres."
        else:
            mc "*Risa* No, Maddie. No eres normal. No creo que \"normal\" incluya compartir a su novio con su suegra."
        mc "Pero me encanta que no seamos normales en esto. Además, ¿quién define qué es normal y qué no?"
        mc "Y la gente a la que le gusta la dominación también son normales. Con otros gustos, pero normales."
        call BlinkXP ("c20s005_320" , "d") from _call_BlinkXP_3766
        mad "¿Quieres quedarte a dormir? Nuestra primera vez como pareja..."
        mc "No, Maddie. Es tarde... hace ya un par de horas que es tarde... y tienes que descansar. Mañana madrugas."
        call BlinkXP ("c20s005_325" , "d") from _call_BlinkXP_3767
        mad "Tienes razón, es tardísimo. Nuestra primera vez tendrá que esperar."
        mc "Sólo te pido una cosa. Pídele a Claire las gafas para lo próxima vez. *Risa* Estaba super sexy."
        call BlinkXP ("c20s005_330" , "d") from _call_BlinkXP_3768
        mad "*Risa* Sólo las uso cuando estoy en el ordenador muchas horas y me quito las lentillas. Normalmente no las necesito."
        mc "Pues creo que las vamos a usar lejos del ordenador también. Estás monísima con ellas."
        call BlinkXP ("c20s005_335" , "d") from _call_BlinkXP_3769
        mad "*Risa* Eso tiene fácil arreglo."
    if mad._var("romance"):
        call BlinkXP ("c20s005_340" , "d") from _call_BlinkXP_3770
        mad "Dame un segundo que me quite las lentillas. Los ojos me pican muchísimo."
        mc "No sabía que llevaras lentillas... pero ve, no te preocupes."
        scene c20s005_215a with dissolve
        zeu "¡Miau! (¡Has vuelto! ¡Espero que vengas dispuesto a acariciarme!)"
        mc "Hola, pequeñín. ¿Me has echado de menos?"
        zeu "¡Miau! (¿Me has traído atún para una cena tardía esta vez?)"
        scene c20s005_215b with dissolve
        zeu "*Ronroneo* (Vale, te perdono... Pero que no se vuelva a repetir.)"
        mc "Yo también te he echado de menos. Tus cuadros han triunfado mucho."
        zeu "*Ronroneo* (Soy muy versátil. Gótico y Científico a la vez. No hablaremos del vestido rosa. Eso nunca pasó. Tengo que hablar con mi psicólogo.)"
        call BlinkXP ("c20s005_260" , "d") from _call_BlinkXP_3771
        mad "Ya estoy."
        mc "¡Wow! Te quedan genial. Deberías llevarlas más a menudo."
        call BlinkXP ("c20s005_345" , "d") from _call_BlinkXP_3772
        mad "Gracias. ¿Quieres quedarte a dormir?"
        mc "No, Maddie. Es tarde... hace ya un par de horas que es tarde... y tienes que descansar. Mañana madrugas."
        call BlinkXP ("c20s005_350" , "d") from _call_BlinkXP_3773
        mad "Tienes razón, es tardísimo. Espero que el día que te quedes llegue pronto."
        mc "No tardará, te lo prometo."
    scene c20s005_305e with dissolve
    "Os dais un beso de buenas noches, sabiendo que el día siguiente os volveréis a ver en la tienda."
    call BlinkXP ("c20s005_360" , "h") from _call_BlinkXP_3774
    mad "¡Oh, mierda!"
    mc "¿Qué pasa, Maddie?"
    call BlinkXP ("c20s005_365" , "d") from _call_BlinkXP_3775
    mad "Habíamos dicho de hacer el test de embarazo al acabar la partida de DnD y nos hemos olvidado los dos."
    mc "¡Es verdad! No he pensado en el test en todo el día, lo siento. Mañana te lo llevo a la tienda. Aún estaremos dentro del plazo de las 120 horas para la píldora."
    call BlinkXP ("c20s005_370" , "d") from _call_BlinkXP_3776
    mad "Sobre eso... Si no te importa... Preferiría no tomarla."
    if mad._var("dom") or mad._var("sub"):
        mad "Nuestra relación ha cambiado y..."
    else:
        mad "Después de todo lo que ha pasado hoy..."
    mc "Te entiendo. Pero ¿quieres saber igualmente si estás embarazada?"
    call BlinkXP ("c20s005_375" , "d") from _call_BlinkXP_3777
    mad "No. Quiero tener la experiencia de novia normal. Quiero enterarme cuando tenga un retraso y poder llamarte emocionada sin saber si estoy embarazada o no."
    mad "Si a ti te parece bien, claro."
    mc "Me parece perfecto, Maddie. Los tests rápidos son fantásticos, pero le quitan un poco de esa emoción de la que hablas."
    call BlinkXP ("c20s005_380" , "d") from _call_BlinkXP_3778
    mad "Y ahora te voy a echar de mi casa antes de que empiece a bostezar. No sería muy glamouroso que me vieras hasta la campanilla cuando bostece."
    mc "*Risa* No te preocupes. Descansa y nos vemos mañana."
    scene c20s005_305e with dissolve
    "Os volvéis a dar otro beso de buenas noches y te marchas a casa antes de volver a enzarzaros en otro tema de conversación."
    stop music fadeout (1.5)
    return
label c20s006_ReturningHome:#12
    scene c20s006_005a with fade
    "Cuando llegas a casa, ves a Kiara de pie, al lado del garaje. Se ha cambiado de ropa."
    play music ("music/thinking-of-you.ogg")
    call BlinkXP ("c20s006_010" , "f") from _call_BlinkXP_3779
    mc "Hola de nuevo, Kiara. Iba a ir a buscarte a tu habitación."
    kia "Eileen está durmiendo. Es muy tarde y mañana trabaja por la mañana."
    mc "Tú también. Quizás deberías estar durmiendo."
    call BlinkXP ("c20s006_015" , "d") from _call_BlinkXP_3780
    kia "Lo he intentado, pero no puedo pegar ojo. Por eso necesito hablar."
    mc "¿Quieres que pasemos dentro y hablemos?"
    call BlinkXP ("c20s006_020" , "d") from _call_BlinkXP_3781
    kia "Mejor vayamos a sentarnos en la piscina. Así no molestaremos a nadie."
    mc "Y nadie nos oirá."
    kia "Exacto."
    scene c20s006_005b with dissolve
    "Kiara anda el camino hacia las tumbonas en silencio, delante tuyo. Parece que está ordenando sus ideas, como si estuviera preparando un discurso."
    scene c20s006_005c with dissolve
    "Solo hay un problema. No hay tumbonas al llegar. Las han recogido después de la fiesta."
    "Ninguno de los dos os habéis dado cuenta mientras andabais hacia donde suelen estar."
    call BlinkXP ("c20s006_025" , "d") from _call_BlinkXP_3782
    kia "Vaya, han recogido las tumbonas. Tendremos que ir dentro."
    mc "Podemos sentarnos en el borde de la piscina, como hemos hecho antes."
    kia "Como quieras..."
    scene c20s006_035d with fade
    "Una vez descalzos y sentados, con los pies en el agua, Kiara se mantiene en silencio."
    call BlinkXP ("c20s006_030" , "d") from _call_BlinkXP_3783
    mc "Kiara, ¿de qué quieres hablar? Me estás preocupando."
    kia "De nosotros..."
    call BlinkXP ("c20s006_035" , "d") from _call_BlinkXP_3784
    kia "No estoy segura de que lo que he hecho esta tarde haya sido lo mejor que podría haber hecho."
    mc "¿Qué has hecho? ¿Besarme?"
    call BlinkXP ("c20s006_040" , "d") from _call_BlinkXP_3785
    kia "Sí. Delante de todas las chicas..."
    mc "Y, por lo que me ha parecido, todas te han felicitado por dar el paso de dejar tu pasado atrás, ¿no?"
    mc "Precisamente el día en que han visto cómo era tu pasado..."
    call BlinkXP ("c20s006_045" , "d") from _call_BlinkXP_3786
    kia "Sí... pero es mi vida, no la suya..."
    mc "Y ninguna de ellas te va a forzar a dar ningún paso que no quieras dar, Kiara."
    call BlinkXP ("c20s006_050" , "d") from _call_BlinkXP_3787
    kia "A eso me refiero... ahora que he recuperado un poco el control de mi vida..."
    kia "No sé que se espera de mí..."
    mc "Nadie espera nada de ti. Lo que esperamos todos, yo incluído, es que consigas ser feliz en esta familia como no lo fuiste en tu familia anterior."
    call BlinkXP ("c20s006_055a" , "d") from _call_BlinkXP_3788
    kia "No me digas que nadie espera que nos acostemos juntos hoy."
    mc "¿Qué? ¡No! ¡Eso no lo espero ni siquiera yo!"
    scene c20s006_055d with dissolve
    pause (0.9)
    call BlinkXP ("c20s006_055b" , "d") from _call_BlinkXP_3789
    kia "Me acabas de mirar las tetas..."
    mc "No me malinterpretes. Si me lo propusieras, no diría que no ni por todo el oro del mundo. Pero no creo que sea el momento correcto."
    call BlinkXP ("c20s006_060" , "d") from _call_BlinkXP_3790
    kia "Pues dile eso a mi hija... "
    mc "¿Eileen? ¿Qué te ha dicho?"
    call BlinkXP ("c20s006_065a" , "d") from _call_BlinkXP_3791
    kia "Me ha intentado convencer de que fuera a tu habitación esta noche. Cuando le he dicho que no, me ha preguntado que cuánto voy a esperar para tener sexo contigo."
    mc "Kiara, ha sido un día muy largo y todo el mundo tiene mucho que procesar. Tú, Eileen, y yo."
    call BlinkXP ("c20s006_065b" , "d") from _call_BlinkXP_3792
    kia "Lo sé, pero no lo entiendes... Soy una mujer que... no sé... Siempre han tomado decisiones por mí. Me las han impuesto."
    kia "Y Eileen lo sabe. Ahora es ella la que intenta hacerlo."
    mc "Eileen es una persona muy sexual. Demuestra su amor con sexo, entre otras cosas."
    call BlinkXP ("c20s006_070" , "d") from _call_BlinkXP_3793
    kia "Lo sé..."
    mc "Pero si le das un momento para pensar se dará cuenta de que tú no eres igual. O al menos no pareces serlo."
    call BlinkXP ("c20s006_075a" , "d") from _call_BlinkXP_3794
    kia "No, no lo soy... para mí el sexo... Siempre he oído que debería ser... no sé... especial. Y nunca lo ha sido..."
    call BlinkXP ("c20s006_075b" , "d") from _call_BlinkXP_3795
    kia "El beso de esta tarde me ha erizado el pelo de sitios donde no sabía que tenía pelo."
    kia "Pero no quiero pensar en nada más allá de ese beso... por ahora..."
    mc "No hay ningún problema con eso. No lo hay conmigo ni lo hay con nadie más. Porque nadie más que tú y yo decidiremos cuándo va a pasar."
    call BlinkXP ("c20s006_080" , "d") from _call_BlinkXP_3796
    kia "Entonces... ¿no te importa ir paso a paso?"
    mc "No, no me importa. Es más, mañana te voy a invitar a cenar, si quieres."
    mc "Quizás, si empezamos a salir como una pareja tradicional te sientas más cómoda. Pero sólamente si quieres ir a cenar conmigo. Nadie te puede forzar a ello."
    call BlinkXP ("c20s006_085" , "d") from _call_BlinkXP_3797
    kia "Sí, quiero. Pero mejor a comer. Si salimos de noche, Eileen me va a interrogar cuando volvamos."
    mc "Perfecto. Tenemos una cita para comer."
    mc "Y recuerda que, aunque Eileen te interrogue, no tienes porqué contarle nada que no quieras contarle."
    call BlinkXP ("c20s006_090" , "d") from _call_BlinkXP_3798
    kia "Lo sé. Ni sentirme forzada a hacer lo que ella quiera que haga."
    mc "Exacto."
    scene c20s006_095AnBlink with dissolve
    kia "Aunque {b}tú{/b} la mandes a que me de la charla y me convenza de cosas, como has hecho esta tarde."
    mc "No, Kiara. No la he mandado a que te convenciera de nada. Estabas preocupada por cómo se sentiría si tú y yo empezábamos algo."
    mc "Sólo le he dicho que te dijera cómo se sentiría. No tenía que ir más allá."
    call BlinkXP ("c20s006_100" , "d") from _call_BlinkXP_3799
    kia "*Risa* ¿No conoces a mi hija? ¿Creías que iba a parar después de decírmelo?"
    mc "En un principio, sí, era lo que esperaba."
    mc "Cuando he visto cómo ha reaccionado cuando... durante el incidente... Creo que estaba muy ansiosa de librarse de su padre."
    call BlinkXP ("c20s006_105" , "d") from _call_BlinkXP_3800
    kia "Es gracioso que digas \"su padre\" en vez de \"Solomon\" o \"tu marido\"."
    kia "Es como si no quisieras recordarme que estoy casada con el padre de Eileen."
    mc "Es que no quiero recordártelo. Estais casados sobre el papel, pero has dicho que no volverás con él nunca."
    mc "En este caso, vuestro matrimonio es únicamente una formalidad hasta que te divorcies."
    call BlinkXP ("c20s006_110" , "d") from _call_BlinkXP_3801
    kia "Sabes que somos católicos, ¿verdad? Solomon nunca me concederá el divorcio."
    mc "Pues tendremos que buscar alguna forma de adecuar nuestra relación a tus creencias religiosas."
    mc "No tengo ni idea de como puede afectarte esto."
    call BlinkXP ("c20s006_115" , "d") from _call_BlinkXP_3802
    kia "Entonces todo arreglado. Mañana comemos juntos y ya veremos... A ver como evoluciona esto... ¿Nos vamos a dormir?"
    mc "Sólo tengo una pregunta antes de irnos."
    mc "El salto de cama que llevabas antes... ¿Ibas a ir a mi habitación? ¿Te había convencido Eileen?"
    call BlinkXP ("c20s006_120" , "d") from _call_BlinkXP_3803
    kia "Casi. Me había vestido así por si reunía el valor para hacerlo."
    kia "Cuando te he oído subir las escaleras, he pensado que sería un buen momento para hablarlo en vez de plantarme en tu habitación como una buscona."
    call BlinkXP ("c20s006_125" , "d") from _call_BlinkXP_3804
    kia "Por lo que estaba diciendo Eile, tenías que estar ansioso por que lo hiciera."
    kia "Por suerte, tenías que llevar a Maddie a casa y eso me ha salvado de hacer algo de lo que después seguramente me hubiera arrepentido."
    call BlinkXP ("c20s006_130" , "d") from _call_BlinkXP_3805
    kia "*Risa* No se lo tengas en cuenta a la chica."
    mc "Creo que es al revés. Creo que le tenemos que agradecer a Maddie que nos podamos tomar nuestro tiempo y hacer las cosas a nuestro ritmo."
    call BlinkXP ("c20s006_135" , "d") from _call_BlinkXP_3806
    kia "Visto así... tienes razón."
    call BlinkXP ("c20s006_140" , "d") from _call_BlinkXP_3807
    "Kiara se calza y se levanta para irse. Haces lo mismo."
    kia "¿Me acompañas a casa de [nor]?"
    mc "Sólo si me prometes que esta vez habrá beso de despedida y que dejarás de llamarla casa de [nor]. También es tu casa ahora."
    call BlinkXP ("c20s006_145" , "d") from _call_BlinkXP_3808
    kia "*Risa* Me parece bien. ¿Me acompañas a casa?"
    stop music fadeout (1.5)
    mc "No has dicho nada del beso..."
    scene c20s006_145d with hpunch
    play music ("music/i-feel-alive.ogg")
    "Kiara se lanza a por tus labios, con la misma dulzura y avidez que ha hecho por la tarde, sorprendiéndote con ambas."
    call BlinkXP ("c20s006_150" , "d") from _call_BlinkXP_3809
    kia "¿Te parece suficiente promesa?"
    mc "Me parece perfecta."
    scene c20s006_155a with fade #cogidos de la mano
    "El camino de la piscina hasta la casa de [nor], la casa de Kiara, no os debería llevar más de dos o tres minutos. Os lleva más de quince."
    scene c20s006_155b with fade #beso
    "Os paráis cada pocos metros para volver a besaros."
    scene c20s006_155c with fade #cogidos de la mano
    "Y esos pocos metros los recorréis, a paso lento, cogidos de la mano, intentando alargar la experiencia lo máximo posible."
    scene c20s006_155d with fade #beso
    "Pero al final llegáis a la puerta principal. Un último beso antes de separaros."
    call BlinkXP ("c20s006_160" , "d") from _call_BlinkXP_3810
    kia "Pues hasta aquí ha llegado nuestro paseo..."
    mc "Si por mí fuera, lo podríamos repetir todas las noches."
    call BlinkXP ("c20s006_165" , "d") from _call_BlinkXP_3811
    kia "No creo que me sentara bien una ducha fría todas las noches a la 1:00 AM... o la hora que sea ya."
    mc "¿Vas a darte una ducha ahora?"
    call BlinkXP ("c20s006_170" , "d") from _call_BlinkXP_3812
    kia "No preguntes lo que no quieras saber. Y no te ofrezcas a enjabonarme la espalda. *Risa*"
    mc "*Risa* No lo voy a hacer. Seguramente no me conformaría con la espalda."
    call BlinkXP ("c20s006_175" , "d") from _call_BlinkXP_3813
    kia "Entonces, hasta mañana a la hora de comer, ¿no?"
    mc "Sí, no creo que esté levantado cuando vayas a trabajar. ¿Quieres que te pase a buscar sobre la 1:00 PM?"
    kia "Es una buena hora. Normalmente salgo entre la 1:00 y la 1:30 a comer. Tengo una hora de tiempo."
    mc "Buscaré algún sitio cerca de la biblioteca para ir a comer. Y no, no vamos a ir al puesto de los perritos calientes en nuestra primera cita."
    call BlinkXP ("c20s006_180" , "d") from _call_BlinkXP_3814
    kia "*Risita* Me parece bien, aunque casi consideraría este paseo como nuestra primera cita."
    mc "Lo será si acaba en beso."
    scene c20s006_155d with dissolve #beso
    "Acaba en beso. Un beso que dice que mañana habrá más. Un beso que sabe a despedida, aunque solo sea por doce horas."
    "Un beso en el que no hay dudas, que empieza a un ritmo suave y que acelera poco a poco. Como esperas que pase con vuestra relación."
    call BlinkXP ("c20s006_185" , "d") from _call_BlinkXP_3815
    kia "Hasta mañana, [mc]. Esperaré ansiosa que vengas a buscarme."
    mc "Hasta mañana, Kiara. Yo estaré ansioso por ir."
    mc "*Risa* Y tampoco vamos a ir al puesto de los perritos calientes en nuestra segunda cita, ahora que ésta cuenta como la primera."
    stop music fadeout (1.5)
    scene black with dissolve
    return
label c20s007_Teaser:
    scene black with dissolve
    "Al volver a tu habitación..."
    scene c20s007_005a
    emm "¡Has tardado muchísimo en volver!"
    dap "Estábamos a punto de irnos. Menos mal que has llegado ahora."
    if mad._var("route"):
        eri "Creíamos que te ibas a quedar a dormir en casa de Maddie."
    else:
        eri "O de llamarte para saber si te había pasado algo."
    return

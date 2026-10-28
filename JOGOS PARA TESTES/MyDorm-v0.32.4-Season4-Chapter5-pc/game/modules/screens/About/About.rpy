screen About ():
    tag menu
    use MenuBackground ()
    use ModalScreen ()
    use ScreenBackground ()
    use Menu ()
    use MenuTitle (_("Acerca de"))
    python:
        marginLeft = getScreenDim (MenuScreenLeft)
        marginTop = getScreenDim (MenuScreenTop, False)
        marginRight = getScreenDim (MenuScreenRight)
        marginBottom = getScreenDim (MenuScreenBottom, False)
    vpgrid style "MenuVPGrid":
        cols 1
        margin (marginLeft * 2, 0, marginRight * 2)
        pos (marginLeft, marginTop)
        xspacing MenuGridSpacing
        yspacing MenuGridSpacing * 2
        xysize (1.0 - marginLeft - marginRight, 1.0 - marginTop - marginBottom)
        mousewheel True
        scrollbars "vertical"
        yfill True
        vbox:

            label _("Acerca de Ren'Py") style "MenuLabel"
            text _("Hencho con {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].") style "MenuText"

            label _("Licencia") style "MenuLabel"
            text _("Este programa contiene software gratuito bajo varias licencias, incluida la licencia MIT y la licencia pública general reducida de GNU.") style "MenuText"
            text _("La lista completa de programas, con enlaces al código fuente completo, puede consultarse {a=https://www.renpy.org/l/license}aquí{/a}.") style "MenuText"

            label _("Contribuyentes") style "MenuLabel"
            text _("Revisión parcial por Blkcrow820, Skyborn, Horny Toad, Elhemeer, Brother George y RiamMar. Traducciones AI por MrGeH. Gracias chicos.") style "MenuText"
            text _("Todos los errores de traducción sólo pueden atribuirse al pobre inglés de Tropecita Games y RiamMar.") style "MenuText"
            text _("Los correctores aún no han terminado con todo el contenido.") style "MenuText"
            text _("Consejos sobre cómo mejorar el código de RiamMar.") style "MenuText"
            text _("Código e idea para las imágenes de perfil scrollables por Trminator.") style "MenuText"

            label _("Créditos de la música") style "MenuLabel"
            text _("Tema principal 'My Dorm' (Rhythm & Play) by Demon Sound") style "MenuText"
            text _("https://uppbeat.io/t/zoo/the-road-ahead Código de licencia: 73KUSPSVPAXEXAR9") style "MenuText"
            text _("https://uppbeat.io/t/yeti-music/peaceful-morning Código de licencia: FCXAYDJ3RQQR2NMW") style "MenuText"
            text _("https://uppbeat.io/t/northwestern/only-you Código de licencia: FYJSGSDOSE7S0RHB") style "MenuText"
            text _("https://uppbeat.io/t/roo-walker/life-made-more Código de licencia: RTVLVKMMDHXOPCYL") style "MenuText"
            text _("https://uppbeat.io/t/giulio-fazio/epic-choir-of-the-damned Código de licencia: 4B803GLCW1WBG94Y") style "MenuText"
            text _("https://uppbeat.io/t/sky-toes/the-long-ride-home Código de licencia: L3KNXAE1RICGFF5Z") style "MenuText"
            text _("https://uppbeat.io/t/prigida/moonshine Código de licencia: MIETOJBCJKPMQDUV") style "MenuText"
            text _("https://uppbeat.io/t/sensho/forgiveness Código de licencia: NHO5MDHVT7NGF1QF") style "MenuText"
            text _("http://ccmixter.org/files/JeffSpeed68/45309 por Stefan Kartenberg") style "MenuText"
            text _("https://www.youtube.com/watch?v=O1xKrGZHUBk por Simusique") style "MenuText"
            text _("http://ccmixter.org/files/JeffSpeed68/55439 por Stefan Kartenberg") style "MenuText"
            text _("http://ccmixter.org/files/sleeperspaceborn/61593 por sleeperspaceborn") style "MenuText"
            text _("http://ccmixter.org/files/geoffpeters/31388 por geoffpeters") style "MenuText"
            text _("http://ccmixter.org/files/mactonite/64666 por darkroom") style "MenuText"
            text _("http://ccmixter.org/files/airtone/65028 por airtone") style "MenuText"
            text _("http://ccmixter.org/files/airtone/64741 por airtone") style "MenuText"
            text _("http://ccmixter.org/files/SkyeJordan/63132 por Skye Jordan") style "MenuText"
            text _("https://freesound.org/people/envirOmaniac2/sounds/411628/ por envirOmaniac2") style "MenuText"
            text _("http://ccmixter.org/files/SkyeJordan/64168 por Skye Jordan") style "MenuText"
            text _("http://ccmixter.org/files/Hervich/63355 por Hervich") style "MenuText"
            text _("http://ccmixter.org/files/VJ_Memes/35657 por Jeris") style "MenuText"
            text _("http://ccmixter.org/files/Milky_Blue/64832 por Milky Blue") style "MenuText"
            text _("http://ccmixter.org/files/geoffpeters/59774 por geoffpeters") style "MenuText"
            text _("http://ccmixter.org/files/airtone/64427 por airtone") style "MenuText"
            text _("https://www.no-copyright-music.com/happy-inspirational/ por Liborio Conti") style "MenuText"


            label _("Créditos de la música") style "MenuLabel"
            text _("https://www.steven-obrien.net/") style "MenuText"
            text _("Refined - Simone en l'Escargot") style "MenuText"
            text _("Happy Camper - Simone en el parque") style "MenuText"
            text _("Ambient Swarm - Llamada desde Aruba") style "MenuText"
            text _("One Last Chance - Oficina de Jonas") style "MenuText"
            text _("Whimsical Wonderland - Felicitación navideña") style "MenuText"
            text _("Utilizado de forma gratuita bajo una licencia Creative Commons Atribución-SinDerivadas 4.0: https://creativecommons.org/licenses/by-nd/4.0/deed.es") style "MenuText"
            text _("https://www.chosic.com/download-audio/37419/") style "MenuText"


            label _("Efectos de sonido") style "MenuLabel"
            text _("{a=https://freesound.org/people/joedeshon/sounds/117415/}Wooden door close{/a} por joedeshon") style "MenuText"
            text _("{a=https://freesound.org/people/13F_Panska_Tlolkova_Matilda/sounds/378322/}Atmosphere{/a} por 13F_Panska_Tlolkova_Matilda") style "MenuText"
            text _("{a=https://freesound.org/people/squareal/sounds/237374/}Car Driving Interior{/a} por squareal") style "MenuText"
            text _("{a=https://freesound.org/people/Sheyvan/sounds/524290/}Water Splashes and Waves{/a} por Sheyvan") style "MenuText"
            text _("{a=https://freesound.org/people/geodylabs/sounds/122810/}Shower{/a} por geodylabs") style "MenuText"
            text _("https://freesound.org/people/ueb_designer/sounds/365174/ por ueb_designer") style "MenuText"
            text _("https://freesound.org/people/estmarolm89/sounds/609802/ por estmarolm89") style "MenuText"
            text _("https://freesound.org/people/szegvari/sounds/530699/ por szegvari") style "MenuText"
            text _("https://freesound.org/people/MSXP/sounds/573840/ por MSXP") style "MenuText"
            text _("https://freesound.org/people/Sandermotions/sounds/277019/ por Sandermotions") style "MenuText"
            text _("https://freesound.org/people/CJDeets/sounds/476740/ por CJDeets") style "MenuText"
            text _("https://freesound.org/people/JayHu/sounds/506103/ por JayHu") style "MenuText"
            text _("https://freesound.org/people/mnsh2/sounds/594661/ por mnsh2") style "MenuText"
            text _("https://freesound.org/people/OwlStorm/sounds/212176/ por OwlStorm") style "MenuText"
            text _("https://freesound.org/people/guinefurrie/sounds/439559/ por guinefurrie") style "MenuText"
            text _("https://freesound.org/people/SharinSharon/sounds/485465/ por SharingSharon") style "MenuText"
            text _("https://freesound.org/people/BurghRecords/sounds/463903/ por BurghRecords") style "MenuText"
            text _("https://freesound.org/people/Vidrik/sounds/384214/ por Vidrik") style "MenuText"
            text _("https://freesound.org/people/Cell31_Sound_Productions/sounds/192250/ por Cell31_Sound_Productions") style "MenuText"
            text _("https://freesound.org/people/khenshom/sounds/534473/ por khenshom") style "MenuText"
            text _("https://freesound.org/people/khenshom/sounds/534474/ por khenshom") style "MenuText"
            text _("https://freesound.org/people/bluedeer/sounds/579256/ por bluedeer") style "MenuText"
            text _("https://freesound.org/people/klankbeeld/sounds/624373/ por klankbeeld") style "MenuText"
            text _("https://freesound.org/people/cheatinggf/sounds/649185/ por cheatinggf") style "MenuText"
            text _("https://freesound.org/people/InspectorJ/sounds/418042/ por InspectorJ") style "MenuText"
            text _("https://freesound.org/people/scampsie/sounds/417091/ por scampsie") style "MenuText"
            text _("https://freesound.org/people/InspectorJ/sounds/406048/ por InspectorJ") style "MenuText"
            text "https://freesound.org/people/LittleRainySeasons/sounds/351526/ by LittleRainySeasons" style "MenuText"


            null height MenuLabelTextSize * 2

image splash = "gui/main_menu.png"
label splashscreen:
    $ persistent.intro = False
    scene black with dissolve
    pause 0.5
    scene splash with dissolve
    pause 1.0
    $ renpy.show_screen ("Splash1")
    pause 2.5
    $ renpy.hide_screen ("Splash1")
    pause 0.5
    $ renpy.show_screen ("Splash2")
    pause 2.0
    $ renpy.hide_screen ("Splash2")
    pause 1.0
    if persistent.dialogueBoxHeight < 30:
        $ persistent.dialogueBoxHeight = 200
    if persistent.dialogueBoxWidth < 800:
        $ persistent.dialogueBoxWidth = 1920
    if not persistent.age:
        "My Dorm es un juego para adultos. Esta verificación se llevará a cabo solo una vez."
        menu:
            "¿Eres mayor de edad en el lugar donde resides?"
            "Sí.":
                $ persistent.age = True
            "No.":
                $ persistent.age = False
                "Lo siento, no puedes jugar a My Dorm. Nos vemos cuando tengas edad suficiente."
                $ renpy.quit()
#    scene neweoc with fade
#    $ continuar = False
    #python:
    #    import webbrowser
#    while not continuar:
#        menu:
#            "Estas chicas necesitan tu apoyo. Hay muchas formas en las que puedes ayudarlas."
            #"Apoya My Dorm en Patreon":
            #    $ renpy.open_url("https://www.patreon.com/bePatron?u=70740879")
            #"Apoya My Dorm en Subscribestar":
#                $ renpy.open_url("https://subscribestar.adult/tropecitagames")
#            "Únete a nuestro Discord":
#                $ renpy.open_url("https://discord.gg/D5hNSYN9BM")
#            "Ir al menú principal":
#                $ continuar = True
    return

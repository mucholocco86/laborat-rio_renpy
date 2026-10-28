label eoc:
    scene neweocs4l with fade
    #python:
    #    _skipping = False
    #pause (1.0)
    python:
        _skipping = True
    #"Esto ha sido todo por la Temporada 3 de My Dorm. Sí, la temporada acaba aquí."
    #"Por favor, graba aquí y nos vemos en la próxima actualización de My Dorm. Gracias por jugar y por tu apoyo. Espero que hayas disfrutado del juego."
    $ menuExit = False
    while not menuExit:
        menu:
            "{b}Esto es todo por esta versión. Por favor, graba aquí y nos vemos en la próxima actualización de My Dorm. Gracias por jugar y por tu apoyo. Espero que hayas disfrutado del juego.{/b}"
            "Steam S1":
                $ renpy.run(OpenURL ("https://store.steampowered.com/app/3510160?utm_source=endmenu&utm_campaign=v028&utm_medium=button"))
            "Steam S2":
                $ renpy.run(OpenURL ("https://store.steampowered.com/app/4178920?utm_source=endmenu&utm_campaign=v028&utm_medium=button"))
            "Steam S3":
                $ renpy.run(OpenURL ("https://store.steampowered.com/app/4873630/My_Dorm__Season_3/"))
            "Patreon":
                $ renpy.run(OpenURL ("https://www.patreon.com/bePatron?u=70740879"))
            "Subscribestar":
                $ renpy.run(OpenURL ("https://subscribestar.adult/tropecitagames"))
            "Salir al menú principal":
                $ menuExit = True
    return

screen MenuNavigation ():
    python:
        menuMarginX = getScreenDim (0.025)
        menuMarginY = getScreenDim (0.025, False)
        menuSpacing = int (MenuGridSpacing / 2)
        buttons = []
        if main_menu:
            pass
            ##################### Hide New Game ###############
            buttons.append ([ _("Nueva partida"), "New Game", [ Start ("part2") ], main_menu ])
        else:
            buttons.append ([ _("Menú principal"), "Main Menu", [ MainMenu () ], not main_menu ])
        ################# Hide Import #######################
        #buttons.append ([ _("Importar"), "Game Import", [ Show ("GameImport") ], True ])
        buttons.append ([ _("Historial"), "History", [ ShowMenu ("History") ], not main_menu ])
        buttons.append ([ _("Grabar"), "Game Save", [ ShowMenu ("GameSave") ], not main_menu ])
        buttons.append ([ _("Cargar"), "Game Load", [ ShowMenu ("GameLoad") ], True ])
        buttons.append ([ _("Settings"), "Settings", [ ShowMenu (myDormMenu.getCurrentTab ("Settings")) ], True ])
        buttons.append ([ _("Galería"), "Gallery", [ ShowMenu ("Gallery") ], True ])
        buttons.append ([ _("Acerca de"), "About", [ ShowMenu ("About") ], True ])
        buttons.append ([ _("Ayuda"), "Help", [ ShowMenu (myDormMenu.getCurrentTab ("Help")) ], renpy.variant ("pc") or renpy.variant ("web") and not renpy.variant ("mobile") ])
        # it's better to have the save and load button next to each other
        # adjust this to ceiling in the if clause, depending on buttons in the bottom menus
        buttonListHalfLength = len (buttons) / 2
        buttonListHalfLengthIndex = int (buttonListHalfLength)
        # use comments on if clause to deactivate it, if it's an even number or
        # if you change the order of buttons and thus the position of the save/load buttons
        if buttonListHalfLengthIndex < buttonListHalfLength:
            buttonListHalfLengthIndex += 1

# Show Quit button
    if not main_menu or renpy.variant ("pc"):
        frame style "MenuNavigationQuitButtonFrame":
            pos (1.0 - menuMarginX, 1 - menuMarginY)
            vbox style "MyDormBoxRight":
                spacing menuSpacing
                if not renpy.variant ("pc"):
                    hbox style "MyDormBoxRight":
                        spacing menuSpacing
                        null height 0
                if not main_menu:
                    hbox style "MyDormBoxRight":
                        spacing menuSpacing
                        use MenuButton (_("Volver"), "Quit", [ Return () ])
                else:
                    hbox style "MyDormBoxRight":
                        spacing menuSpacing
                        null height 0
                if renpy.variant ("pc"):
                    hbox style "MyDormBoxRight":
                        spacing menuSpacing
                        use MenuButton (_("Salir"), "Quit", [ Quit (confirm=not main_menu) ])

# General buttons as defines in "buttons"
    frame style "MenuNavigationGeneralButtonsFrame":
        pos (0.55, 1 - menuMarginY)
        vbox style "MyDormBoxCentered":
            spacing menuSpacing
            hbox style "MyDormBoxCentered":
                spacing menuSpacing
                for (buttonLabel, buttonIcon, buttonAction, buttonTrigger) in buttons [0:buttonListHalfLengthIndex]:
                    use MenuButton (buttonLabel, buttonIcon, buttonAction, buttonTrigger)
            hbox style "MyDormBoxCentered":
                spacing menuSpacing
                for (buttonLabel, buttonIcon, buttonAction, buttonTrigger) in buttons [buttonListHalfLengthIndex: len (buttons)]:
                    use MenuButton (buttonLabel, buttonIcon, buttonAction, buttonTrigger)

screen GameLoad ():
    tag menu
    use MenuBackground ()
    use ModalScreen ()
    use ScreenBackground ()
    use Menu ()
    use MenuTitle (_("Cargar una partida anterior"))
    use GameSaveLoadMenu ("load")
    use GameSaveLoadFileSlots ("load")
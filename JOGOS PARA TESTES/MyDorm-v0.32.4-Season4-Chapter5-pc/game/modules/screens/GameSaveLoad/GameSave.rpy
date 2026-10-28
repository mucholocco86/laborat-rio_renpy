screen GameSave ():
    tag menu
    use MenuBackground ()
    use ModalScreen ()
    use ScreenBackground ()
    use Menu ()
    use MenuTitle (_("Grabar tu partida"))
    use GameSaveLoadMenu ("save")
    use GameSaveLoadFileSlots ("save")
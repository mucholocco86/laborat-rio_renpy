screen JK_MoveCopySaves(playthrough):
    layer "JK_Overlay"
    style_prefix 'JK'
    modal True

    default source_playthrough = playthrough
    default destination_playthrough = None
    default saves_to_process = []
    default show_thumbnails = False
    default last_selected_save = None

    default view_model = None

    use JK_Dialog(title="Mover/copiar salvamentos" if destination_playthrough else "Selecionar outra jornada", message=None if destination_playthrough else "Selecione a jornada de destino para mover ou copiar os salvamentos.", close_action=Hide("JK_MoveCopySaves")):
        style_prefix "JK"

        if source_playthrough and destination_playthrough:
            $ view_model = view_model or JK.MoveCopySavesViewModel(source_playthrough, destination_playthrough)

            if view_model.processing:

                use JK_MoveCopySavesProcessing(view_model)
            elif view_model.error:

                use JK_MoveCopySavesError(view_model)
            elif view_model.success:

                use JK_MoveCopySavesSuccess()
            else:

                use JK_MoveCopySavesSelectSaves(view_model, saves_to_process, show_thumbnails, last_selected_save)
        else:

            use JK_MoveCopySavesSelectOtherPlaythrough(source_playthrough, destination_playthrough)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

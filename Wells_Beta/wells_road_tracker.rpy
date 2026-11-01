## =============================================================================
## WELLS ROAD TRACKER — PAINEL DE CHECKPOINTS
## Layout adaptável com os mesmos recursos visuais da tela Save/Load do Wells.
## =============================================================================

default wells_pending_load = None

screen wells_road_tracker():
    modal True
    zorder 200
    tag menu

    add Solid("#000000aa")

    $ wells_tracker_records = wells_tracker_list_records()

    frame:
        xalign 0.5
        yalign 0.4
        background Frame("wells/gui/frame_menu.png", 10, 10)
        xsize wells_ui(1450)
        ysize wells_ui(820)
        xpadding wells_ui(50)
        ypadding wells_ui(40)

        fixed:
            xfill True
            yfill True

            hbox:
                xalign 0.5
                ypos wells_ui_signed(8)

                textbutton _("Registrar checkpoint"):
                    xpadding wells_ui(14)
                    ypadding wells_ui(5)
                    idle_background Frame("wells/gui/Button-idle.png", 5, 5)
                    hover_background Frame("wells/gui/Button-hover.png", 5, 5)
                    action Function(wells_salvar_checkpoint)
                    text_size wells_ui(18)
                    text_hover_color "#2bff00"

            side "c r":
                ypos wells_ui(65)
                xsize wells_ui(1250)
                ysize wells_ui(565)
                xalign 0.5
                spacing wells_ui(22)

                viewport:
                    id "wells_tracker_slots"
                    xsize wells_ui(1210)
                    ysize wells_ui(565)
                    mousewheel True
                    draggable True

                    if not wells_tracker_records:
                        text "Nenhum checkpoint registrado ainda.":
                            xalign 0.5
                            yalign 0.5
                            size wells_ui(24)
                            color "#c8c8c8"
                    else:
                        vbox:
                            xfill True
                            spacing wells_ui(24)

                            # Mantém as mesmas medidas da grade de slots do Wells.
                            for row_start in range(0, len(wells_tracker_records), 3):
                                hbox:
                                    xalign 0.5
                                    spacing wells_ui(35)

                                    for record in wells_tracker_records[row_start:row_start + 3]:
                                        frame:
                                            xysize (wells_ui(360), wells_ui(262))
                                            spacing wells_ui(5)
                                            background None

                                            fixed:
                                                xfill True
                                                yfill True

                                                button:
                                                    xysize (wells_ui(360), wells_ui(230))
                                                    background Solid("#080808")
                                                    sensitive record.get("version") == 3
                                                    action SetVariable("wells_pending_load", record["filename"])

                                                    vbox:
                                                        spacing wells_ui(5)
                                                        xfill True

                                                        $ preview = wells_tracker_preview(record.get("image_name"), record.get("asset_file"))
                                                        if preview is not None:
                                                            add Transform(preview, xsize=wells_ui(360), ysize=wells_ui(185))
                                                        else:
                                                            add Solid("#111111") xsize wells_ui(360) ysize wells_ui(185)

                                                        text record["filename"]:
                                                            xalign 0.5
                                                            size wells_ui(18)
                                                            color "#ffffff"

                                                button:
                                                    xalign 1.0
                                                    yalign 0.0
                                                    xpadding 0
                                                    ypadding 0
                                                    xysize (wells_ui(72), wells_ui(28))
                                                    idle_background Frame("wells/gui/Button-idle.png", 3, 3)
                                                    hover_background Frame("wells/gui/Button-hover.png", 3, 3)
                                                    action Function(wells_tracker_delete, record["filename"])
                                                    text "Excluir" xalign 0.5 yalign 0.5 size wells_ui(20) hover_color "#2bff00"

                                            text wells_tracker_format_time(record.get("timestamp", 0)):
                                                xalign 0.5
                                                yalign 1.0
                                                size wells_ui(22)
                                                color "#2bff00"

                vbar:
                    value YScrollValue("wells_tracker_slots")
                    top_bar Frame("wells/gui/vertical_cheia.png", 0, 0)
                    bottom_bar Frame("wells/gui/vertical_vazia.png", 0, 0)
                    thumb Frame("wells/gui/v_pino.png", 10, 0) xsize wells_ui(20)

    button:
        xpadding 0
        ypadding 0
        xysize (wells_ui(180), wells_ui(45))
        xalign 0.5
        yalign 0.985
        idle_background Frame("wells/gui/Button-idle.png", 5, 5)
        hover_background Frame("wells/gui/Button-hover.png", 5, 5)
        action Hide("wells_road_tracker")
        text _("Voltar") xalign 0.5 yalign 0.5 size wells_ui(22) hover_color "#2bff00"

    if wells_pending_load:
        add Solid("#000000c0")

        frame:
            xalign 0.5
            yalign 0.5
            background Frame("wells/gui/frame_menu.png", 10, 10)
            xsize wells_ui(620)
            padding (wells_ui(30), wells_ui(24), wells_ui(30), wells_ui(24))

            vbox:
                spacing wells_ui(24)
                xalign 0.5

                text "Carregar este checkpoint?":
                    xalign 0.5
                    size wells_ui(28)
                    color "#ffffff"
                    text_align 0.5

                text "O jogo será reiniciado e reconstruído até este ponto.":
                    xalign 0.5
                    size wells_ui(20)
                    color "#c8c8c8"
                    text_align 0.5

                hbox:
                    spacing wells_ui(24)
                    xalign 0.5

                    textbutton _("Confirmar"):
                        xpadding wells_ui(24)
                        ypadding wells_ui(8)
                        idle_background Frame("wells/gui/Button-idle.png", 5, 5)
                        hover_background Frame("wells/gui/Button-hover.png", 5, 5)
                        action Function(wells_tracker_request_load, wells_pending_load)
                        text_size wells_ui(22)
                        text_hover_color "#2bff00"

                    textbutton _("Cancelar"):
                        xpadding wells_ui(24)
                        ypadding wells_ui(8)
                        idle_background Frame("wells/gui/Button-idle.png", 5, 5)
                        hover_background Frame("wells/gui/Button-hover.png", 5, 5)
                        action SetVariable("wells_pending_load", None)
                        text_size wells_ui(22)
                        text_hover_color "#2bff00"

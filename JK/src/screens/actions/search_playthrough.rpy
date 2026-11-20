screen JK_SearchPlaythrough(search_all=False):
    layer "JK_Overlay"
    style_prefix "JK"
    modal True

    default search = ""
    default view_model = JK.SearchPlaythroughViewModel(search_playthroughs=search_all)
    default search_input = JK.TextInput("search", auto_focus=True)
    default focused_button = None

    if JK.TextInput.is_active("search"):
        key 'K_ESCAPE' action JK.TextInput.SetActiveAction(None)

    python:
        hide_action = Hide("JK_SearchPlaythrough")

        def result_to_text(result):
            t = result[0]
            
            if t == "PLAYTHROUGH_NAME":
                return "Nome da jornada"
            elif t == "PLAYTHROUGH_DESCRIPTION":
                return "Descrição da jornada"
            elif t == "FILE_PAGE_NAME":
                return "Nome da página"
            elif t == "SAVE_NAME":
                return "Nome do salvamento"
            elif t == "SAVE_CHOICE":
                return "Escolha"

        def result_to_action(result):
            t = result[0]
            playthrough = result[2]
            
            if t == "PLAYTHROUGH_NAME":
                return JK.Playthroughs.ActivatePlaythroughAction(playthrough)
            elif t == "PLAYTHROUGH_DESCRIPTION":
                return JK.Playthroughs.ActivatePlaythroughAction(playthrough)
            elif t == "FILE_PAGE_NAME":
                return [JK.Playthroughs.ActivatePlaythroughAction(playthrough), FilePage(result[3])]
            elif t == "SAVE_NAME":
                page, _ = JK.Utils.split_slotname(result[3])
                return [JK.Playthroughs.ActivatePlaythroughAction(playthrough), FilePage(page)]
            elif t == "SAVE_CHOICE":
                page, _ = JK.Utils.split_slotname(result[3])
                return [JK.Playthroughs.ActivatePlaythroughAction(playthrough), FilePage(page)]

    if JK.Settings.searchPlaythroughKey:
        key JK.Settings.searchPlaythroughKey action JK.SearchPlaythroughViewModel.SetSearchAllAction(view_model, False)

    if JK.Settings.searchPlaythroughsKey:
        key JK.Settings.searchPlaythroughsKey action JK.SearchPlaythroughViewModel.SetSearchAllAction(view_model, True)

    use JK_Dialog(title="Pesquisar jornada", close_action=Hide("JK_SearchPlaythrough")):
        style_prefix "JK"

        button:
            action NullAction()
            key_events True

            has vbox
            add search_input.displayable(placeholder="Pesquisar")
            $ view_model.set_search_text(search)
            frame style "JK_default" background "#ffffff22" hover_background JK.Colors.hover ysize 2 offset JK.scaled((0, 2))

        hbox:
            xalign 1.0

            use JK_Checkbox(checked=view_model.search_playthroughs, text="Pesquisar jornadas", size=15, action=JK.SearchPlaythroughViewModel.SetSearchEnabledAction(view_model, "search_playthroughs"))
            use JK_Checkbox(checked=view_model.search_playthrough_names, text="Pesquisar nomes de jornadas", size=15, action=JK.SearchPlaythroughViewModel.SetSearchEnabledAction(view_model, "search_playthrough_names"), disabled=not view_model.search_playthroughs)
            use JK_Checkbox(checked=view_model.search_playthrough_descriptions, text="Pesquisar descrições de jornadas", size=15, action=JK.SearchPlaythroughViewModel.SetSearchEnabledAction(view_model, "search_playthrough_descriptions"), disabled=not view_model.search_playthroughs)
            use JK_Checkbox(checked=view_model.search_page_names, text="Pesquisar nomes de páginas", size=15, action=JK.SearchPlaythroughViewModel.SetSearchEnabledAction(view_model, "search_page_names"))
            use JK_Checkbox(checked=view_model.search_save_names, text="Pesquisar nomes dos salvamentos", size=15, action=JK.SearchPlaythroughViewModel.SetSearchEnabledAction(view_model, "search_save_names"))
            use JK_Checkbox(checked=view_model.search_choices, text="Pesquisar escolhas", size=15, action=JK.SearchPlaythroughViewModel.SetSearchEnabledAction(view_model, "search_choices"))

        if view_model.searching or view_model.search_after_cache_is_built:
            text "Pesquisando..."

        if view_model.searched and len(view_model.search_text) > 0:
            if len(view_model.results) > 0:
                text "Encontrado: {}".format(len(view_model.results))
            else:
                text "Nenhum resultado"

            viewport:
                mousewheel True
                draggable True
                scrollbars "vertical"
                vscrollbar_unscrollable "hide"
                pagekeys True
                ymaximum 0.85

                has vbox
                for result in view_model.results:
                    python:
                        hovered = result == focused_button
                        i = 0

                        result_type = result[0]
                        highlighted_string = result[1]
                        playthrough = result[2]

                    button:
                        action [result_to_action(result), hide_action]
                        hovered SetScreenVariable("focused_button", result)
                        style ("JK_row_button" if i % 2 == 0 else "JK_row_odd_button")
                        selected False

                        $ i += 1

                        hbox:
                            xfill True
                            ysize JK.scaled(40)

                            hbox:
                                align (0.0, 0.5)
                                spacing JK.scaled(5)

                                text "{size=-5}" + result_to_text(result) + "{/size}" yalign 0.5 color JK.Colors.text_light
                                text highlighted_string

                                if result_type in ("SAVE_NAME", "SAVE_CHOICE"):
                                    text "{size=-5}(" + result[3] + "){/size}" yalign 0.5 color JK.Colors.text_light

                                if result_type in ("PLAYTHROUGH_DESCRIPTION"):
                                    text "{size=-5}(" + playthrough.name + "){/size}" yalign 0.5 color JK.Colors.text_light

                            if hovered:
                                hbox:
                                    xalign 1.0

                                    if result_type in ("SAVE_NAME", "SAVE_CHOICE"):
                                        $ page, _ = JK.Utils.split_slotname(result[3])
                                    elif result_type in ("FILE_PAGE_NAME"):
                                        $ page = result[3]

                                    if result_type in ("FILE_PAGE_NAME", "SAVE_NAME", "SAVE_CHOICE"):
                                        use JK_IconButton(icon="\ue8a0", tt="Exibir página", action=[JK.Playthroughs.ActivatePlaythroughAction(playthrough), FilePage(page), hide_action])

                                    if result_type in ("SAVE_NAME", "SAVE_CHOICE"):
                                        $ page, slot = JK.Utils.split_slotname(result[3])
                                        use JK_IconButton(icon="\ue1c4", tt="Carregar salvamento", action=[JK.Playthroughs.ActivatePlaythroughAction(playthrough), FilePage(page), FileLoad(slot, confirm=True, page=page), hide_action])


        hbox:
            style_prefix "JK_dialog_action_buttons"
            xfill True
            yfill True

            vbox xalign 1.0:

                hbox:
                    use JK_IconButton(icon="\ue5cd", text="Fechar", action=Hide("JK_SearchPlaythrough"))
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

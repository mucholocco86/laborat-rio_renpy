screen JK_EditPlaythrough(playthrough, isEdit=False, editing_template=False, duplicating=False):
    layer "JK_Overlay"
    style_prefix 'JK'
    modal True

    $ playthrough = playthrough or JK.Playthroughs.get_instance_for_edit()

    default name = playthrough.name or ''
    default originalname = name if isEdit else ''
    default description = playthrough.description or ''
    default storeChoices = playthrough.storeChoices
    default autosaveOnChoices = playthrough.autosaveOnChoices
    default useChoiceLabelAsSaveName = playthrough.useChoiceLabelAsSaveName
    default enabledSaveLocations = playthrough.enabledSaveLocations or False
    default moveSaveDirectory = True


    default name_input = JK.TextInput("name", auto_focus=True)
    default description_input = JK.TextInput("description", multiline=True)

    python:
        if editing_template:
            submitAction = [
                JK.Settings.SaveDefaultPlaythroughTemplateAction(playthrough, name, description, storeChoices, autosaveOnChoices, useChoiceLabelAsSaveName, enabledSaveLocations)
            ]
        elif duplicating:
            submitAction = [
                JK.Playthroughs.DuplicatePlaythroughAction(playthrough, name, description, storeChoices, autosaveOnChoices, useChoiceLabelAsSaveName, enabledSaveLocations, moveSaveDirectory)
            ]
        else:
            submitAction = [
                JK.Playthroughs.AddOrEditAction(playthrough, name, description, storeChoices, autosaveOnChoices, useChoiceLabelAsSaveName, enabledSaveLocations, moveSaveDirectory)
            ]

        submitAction.append(Hide('JK_EditPlaythrough'))

        name_conflicting = not editing_template and name != originalname and not JK.Playthroughs.is_valid_name(name)
        name_invalid = name_conflicting or len(name) == 0

        is_save_disabled = enabledSaveLocations != False and len(enabledSaveLocations) == 0
        if not editing_template:
            is_save_disabled = is_save_disabled or name_invalid

        title = ""
        if editing_template:
            title = "Editar modelo padrão"
        elif isEdit:
            title = "Editar jornada"
        elif duplicating:
            title = "Duplicar \"" + playthrough.name + "\""
        else:
            title = "Nova jornada"

    key 'ctrl_K_DELETE' action Show("JK_RemovePlaythroughConfirm", playthrough=playthrough)

    if not is_save_disabled:
        key "ctrl_K_s" action submitAction

    use JK_Dialog(title=title, close_action=Hide("JK_EditPlaythrough")):
        style_prefix "JK"

        viewport:
            mousewheel True
            draggable True
            scrollbars "vertical"
            vscrollbar_unscrollable "hide"
            pagekeys True
            ymaximum 0.85

            has vbox
            button:
                action name_input.get_enable_action()
                key_events True

                has vbox
                use JK_Title("Nome")
                add name_input.displayable(placeholder="Clique aqui para começar a escrever")
                frame style "JK_default" background "#ffffff22" hover_background JK.Colors.hover ysize 2 offset JK.scaled((0, 2))

            text "{size=-5}Este nome já existe.{/size}" color (JK.Colors.error if name_conflicting else "#00000000") offset JK.scaled((10, 2))

            use JK_YSpacer(2)

            if playthrough.id != 1:
                python:
                    allSaveLocations = JK.SaveSystem.get_all_native_save_locations_for_options()
                    computedDirectory = "[[Playthrough name]"

                if not editing_template:
                    python:
                        computedDirectory = playthrough.directory if playthrough.directory and not moveSaveDirectory else (JK.Utils.name_to_directory_name(name) if name else None) or ""

                    use JK_Title("Pasta", 2)
                    hbox:
                        offset JK.scaled((15, 0))

                        text "saves/" color '#e5e5e5'
                        text "[computedDirectory]" color JK.Colors.theme

                        hbox yalign 0.5 xoffset JK.scaled(5):
                            if isEdit:
                                use JK_IconButton(icon="\ue2c8", action=JK.OpenDirectoryAction(path=computedDirectory, cwd=renpy.config.savedir), size=20, tt="Abrir pasta da jornada", tt_side="right")
                            else:
                                use JK_IconButton(icon="\ue2c8", action=JK.OpenDirectoryAction(path=renpy.config.savedir), size=20, tt="Abrir a pasta onde esta jornada será criada", tt_side="right")

                    if isEdit and playthrough.id > 1 and name != originalname and not name_invalid:
                        use JK_Checkbox(checked=moveSaveDirectory, text="Renomear a pasta também", action=ToggleScreenVariable('moveSaveDirectory', True, False))

                if len(allSaveLocations) > 1:
                    hbox:
                        use JK_Checkbox(checked=enabledSaveLocations != False, text="Gerenciar locais de salvamento", action=ToggleScreenVariable('enabledSaveLocations', allSaveLocations, False))
                        use JK_Helper("Aqui você define onde os salvamentos desta jornada serão armazenados.\nPor padrão, o Ren’Py mantém os salvamentos em dois locais {color=[JK.Colors.warning]}(isso varia conforme a plataforma){/color}: na pasta do jogo e na pasta do usuário. Se quiser desativar um desses locais para economizar espaço, faça isso aqui.")

                    if enabledSaveLocations != False:
                        hbox:
                            use JK_XSpacer()

                            $ platform_specific_library_name = "Library" if renpy.macintosh else ("%APPDATA%" if renpy.windows else "Home")

                            vbox:
                                for location in allSaveLocations:
                                    python:
                                        locationType = "Extra"
                                        path = location


                                        if location == "USER":
                                            locationType = platform_specific_library_name
                                            path = renpy.config.savedir

                                        elif location == "GAME":
                                            locationType = "Arquivos do jogo"
                                            path = os.path.join(renpy.config.gamedir, "saves")

                                        fullPath = os.path.join(path, computedDirectory)

                                    hbox:
                                        use JK_Checkbox(checked=location in enabledSaveLocations, text=locationType + " - {color=#818181}{size=-5}" + fullPath + "{/size}{/c}", action=ToggleSetMembership(enabledSaveLocations, location))

                                        hbox:
                                            xpos 0.5
                                            xanchor 0.5
                                            ypos 0.5
                                            yanchor 0.5

                                            if isEdit:
                                                use JK_IconButton(icon="\ue2c8", action=JK.OpenDirectoryAction(path=fullPath), size=15, color="#818181", tt="Abrir pasta", hover_color=JK.Colors.hover)
                                            else:
                                                use JK_IconButton(icon="\ue2c8", action=JK.OpenDirectoryAction(path=path), size=15, color="#818181", tt="Abrir pasta", hover_color=JK.Colors.hover)

                                if len(enabledSaveLocations) == 0:
                                    use JK_YSpacer(3)

                                    text "Pelo menos um local precisa estar ativado!" color JK.Colors.error xoffset JK.scaled(10)

                                if "USER" not in enabledSaveLocations and len(enabledSaveLocations) == 1:
                                    use JK_YSpacer(3)

                                    text "Atenção: sem [platform_specific_library_name], seus salvamentos ficarão armazenados somente na pasta do jogo. Se desinstalar o jogo, você também {u}perderá seu progresso{/u}." color JK.Colors.warning xoffset JK.scaled(10)

            use JK_YSpacer()

            button:
                action description_input.get_enable_action()
                key_events True

                has vbox
                use JK_Title("Descrição")
                add description_input.displayable(placeholder="Clique aqui para começar a escrever")
                frame style "JK_default" background "#ffffff22" hover_background JK.Colors.hover ysize 2 offset JK.scaled((0, 2))

            use JK_YSpacer()

            use JK_Title("Opções")
            hbox:
                xfill True

                vbox:
                    hbox:
                        use JK_Checkbox(checked=autosaveOnChoices, text="Salvar automaticamente ao escolher", action=ToggleScreenVariable('autosaveOnChoices', True, False), disabled=not JK.Utils.has_cols_and_rows_configuration())
                        use JK_Helper("Este sistema salva automaticamente seu progresso antes de cada escolha, facilitando a criação de cópias e o acompanhamento da jornada.\n\n{color=[JK.Colors.warning]}Não confunda com o recurso “Salvamento automático” nativo do Ren’Py.{/color}")

                    if not JK.Utils.has_cols_and_rows_configuration():
                        text "{size=-7}{color=[JK.Colors.error]}Este jogo usa uma configuração de salvamento incomum, então o salvamento automático não funcionará sem ajustes.{/color}\n{color=[JK.Colors.text_primary]}Para ativar esta opção, siga estas etapas:\n  1) conte as colunas e linhas da grade de salvamentos;\n  2) abra as configurações, localize {color=[JK.Colors.theme]}\"Grade personalizada de slots\"{/color} e ative a opção. Esta mensagem desaparecerá;\n  3) informe os valores correspondentes.\nSe o salvamento automático continuar sem funcionar, procure ajuda no {a=[JK.DISCORD_URL]}Discord{/a} ou no {a=https://github.com/[JK.MOD_GITHUB_OWNER]/[JK.MOD_GITHUB_REPO]/issues}GitHub{/a}.\n\n{color=[JK.Colors.info]}Para abrir rapidamente as configurações correspondentes, {a=JK_Run:JK.Settings.ShowSaveLoadAction()}clique aqui{/a}.{/color}{/color}{/size}" offset JK.scaled((35, -5))

                    hbox:
                        offset JK.scaled((15, 0))

                        use JK_Checkbox(checked=useChoiceLabelAsSaveName, text="Usar o texto da escolha como nome do salvamento\n{size=-7}(Válido somente para salvamentos automáticos criados por este mod){/size}", action=ToggleScreenVariable('useChoiceLabelAsSaveName', True, False), disabled=not JK.Utils.has_cols_and_rows_configuration() or not autosaveOnChoices)

            use JK_YSpacer()

            if isEdit or duplicating:
                use JK_Title("Miniatura")
                hbox:
                    frame style "JK_default":
                        xysize JK.scaled((350, 250))

                        if playthrough.hasThumbnail():
                            add playthrough.getThumbnail(width=JK.scaled(350), height=JK.scaled(350))
                        else:
                            button:
                                style_prefix ""
                                action None
                                xalign 0.5
                                yalign 0.5

                                use JK_Icon(icon="\ue3f4", color="#333")

                    use JK_XSpacer(3)

                    vbox:

                        use JK_IconButton(icon="\ue3f4", text="Usar a cena atual como miniatura", action=JK.Playthroughs.SetThumbnail(playthrough=playthrough))


                        if playthrough.hasThumbnail():
                            use JK_IconButton(icon="\ue92b", text="Remover miniatura", action=Function(playthrough.removeThumbnail, _update_screens=True), color=JK.Colors.danger)

        hbox:
            xfill True
            yfill True

            style_prefix "JK_dialog_action_buttons"

            if not isEdit and not editing_template and not duplicating:
                vbox xalign 0.0:
                    hbox:
                        use JK_IconButton(icon="\uead3", text="Editar valores padrão", action=Show("JK_EditPlaythrough", playthrough=None, editing_template=True), tt="Clique aqui para editar os valores padrão de novas jornadas")

            vbox:
                if isEdit and playthrough.id != 1:

                    hbox:
                        use JK_IconButton(icon="\ue92b", text="Remover", action=Show("JK_RemovePlaythroughConfirm", playthrough=playthrough), color=JK.Colors.danger, key="alt_K_r")


                hbox:
                    if editing_template:
                        use JK_IconButton(icon="\ue161", text="Salvar modelo", action=submitAction, key="alt_K_s", disabled=is_save_disabled)
                    else:
                        use JK_IconButton(icon="\ue161", text="Salvar", action=submitAction, disabled=is_save_disabled, key="alt_K_s")

                if not isEdit and not editing_template and not duplicating:
                    hbox:
                        use JK_IconButton(icon="\uebbd", text="Criar a partir de uma pasta existente", action=Show("JK_SelectExistingDirectoryForNewPlaythrough"), tt="Você pode usar uma pasta existente para criar uma jornada. O nome e o local serão preenchidos automaticamente.", tt_side="left")


                hbox:
                    use JK_IconButton(icon="\ue5cd", text="Fechar", action=Hide("JK_EditPlaythrough"))
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

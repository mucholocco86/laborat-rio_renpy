screen JK_Settings_LoadSave():
    vbox:
        hbox:
            $ sub_text = ""
            if hasattr(renpy.store.gui, "file_slot_cols") and hasattr(renpy.store.gui, "file_slot_rows"):
                $ sub_text = "\n{color=[JK.Colors.text_light]}{size=-5}Valores de configuração: [renpy.store.gui.file_slot_cols], [renpy.store.gui.file_slot_rows]{/size}{/color}"

            use JK_Checkbox(checked=JK.Settings.customGridEnabled, text="Grade personalizada de slots" + sub_text, action=JK.Settings.ToggleEnabledAction("customGridEnabled"))
            use JK_Helper("Quando ativado, serão exibidas opções para informar o número de colunas e linhas da grade de slots nas telas de salvamento do jogo. Isso é necessário porque alguns jogos usam sistemas personalizados que o salvamento automático e o salvamento rápido do mod não conseguem detectar.")

        if JK.Settings.customGridEnabled:
            use JK_YSpacer(2)

            hbox:
                use JK_XSpacer()

                hbox:
                    vbox:
                        text "Colunas" xalign 0.5
                        hbox:
                            use JK_IconButton(icon="\ue15b", action=JK.Settings.DecrementAction("customGridX", min=1))

                            text str(JK.Settings.customGridX) yalign 0.5

                            use JK_IconButton(icon="\ue145", action=JK.Settings.IncrementAction("customGridX"))

                    use JK_XSpacer(2)

                    vbox:
                        text "Linhas" xalign 0.5
                        hbox:
                            use JK_IconButton(icon="\ue15b", action=JK.Settings.DecrementAction("customGridY", min=1))

                            text str(JK.Settings.customGridY) yalign 0.5

                            use JK_IconButton(icon="\ue145", action=JK.Settings.IncrementAction("customGridY"))

                grid JK.Settings.customGridX JK.Settings.customGridY spacing JK.scaled(5) offset JK.scaled((100, 0)) yalign 0.5:
                    for x in range(0, JK.Settings.customGridX):
                        for y in range(0, JK.Settings.customGridY):
                            frame style "JK_default" xysize JK.scaled((10, 10)) background JK.Colors.theme

            use JK_YSpacer(2)

        hbox:
            use JK_Checkbox(checked=JK.Settings.offsetSlotAfterManualSaveIsLoaded, text="Sempre avançar um slot após carregar um salvamento manual", action=JK.Settings.ToggleEnabledAction("offsetSlotAfterManualSaveIsLoaded"))
            use JK_Helper("Quando ativado, carregar um salvamento avança um slot e impede que o próximo salvamento automático ou rápido sobrescreva o salvamento manual.")
            use JK_ToggleSettingGlobalizationButton("offsetSlotAfterManualSaveIsLoaded")

        hbox:
            use JK_Checkbox(checked=JK.Settings.offsetSlotAfterManualSave, text="Avançar um slot após fazer um salvamento manual", action=JK.Settings.ToggleEnabledAction("offsetSlotAfterManualSave"))
            use JK_Helper("Quando ativado, um salvamento manual avança um slot e impede que o próximo salvamento automático ou rápido o sobrescreva.")
            use JK_ToggleSettingGlobalizationButton("offsetSlotAfterManualSave")

        use JK_YSpacer()

        use JK_Title("Pesquisar")

        vbox:
            hbox:
                text "Atalho para pesquisar jornadas" yalign 0.5
                use JK_ToggleSettingGlobalizationButton("searchPlaythroughKey")

            use JK_KeyInput(assignment=JK.Settings.searchPlaythroughKey, action=JK.Settings.get_set_key_action("searchPlaythroughKey"), supress_ctrl_warning=True)

        use JK_YSpacer(2)

        vbox:
            hbox:
                text "Atalho para pesquisar em todas as jornadas" yalign 0.5
                use JK_ToggleSettingGlobalizationButton("searchPlaythrougshKey")

            use JK_KeyInput(assignment=JK.Settings.searchPlaythroughsKey, action=JK.Settings.get_set_key_action("searchPlaythroughsKey"), supress_ctrl_warning=True)

        use JK_YSpacer()

        vbox:
            hbox:
                use JK_Title("Telas")

                hbox:
                    yalign 0.5

                    use JK_Helper("Aqui você pode selecionar quais telas correspondem às telas de salvar e carregar. O painel lateral aparecerá nas telas selecionadas.")

            use JK_YSpacer(3)

            hbox:
                use JK_XSpacer()

                vbox:
                    use JK_SettingsLoadSaveScreens()

                    use JK_YSpacer(2)

                    hbox:
                        use JK_IconButton("\ue8fb", text="Clique aqui para abrir esta seção separadamente", action=[Show("JK_SettingsLoadSaveScreensStandalone"), JK.SetSidepanelVisibilityAction(None), Hide("JK_Settings")])
                        use JK_Helper("Clique para isolar a seção {color=[JK.Colors.theme]}{b}Telas{/b}{/color} e ocultar as demais configurações.\nNesse modo, você acompanha em tempo real as telas exibidas e escolhe os nomes corretos com retorno visual imediato.")

            use JK_YSpacer()

            use JK_Title("Paginação")

            hbox:
                use JK_XSpacer()

                vbox:
                    hbox:
                        use JK_Checkbox(checked=JK.Settings.seamlessPagination, text="Usar paginação contínua", action=JK.Settings.ToggleEnabledAction("seamlessPagination"))
                        use JK_Helper("Quando ativada, a página atual permanece centralizada, facilitando a navegação entre muitas páginas. A numeração pode mudar de posição, o que talvez cause estranheza no início.\n\n{b}{color=[JK.Colors.theme]}Exemplo{/color}{/b}\n\n{b}Normal:{/b}\nPágina atual = 7\nPáginas = {b}1 2 3 4 5 6 {color=[JK.Colors.selected]}7{/color} 8 9{/b}\n\n{b}Contínua:{/b}\nPágina atual = 7\nPáginas = {b}3 4 5 6 {color=[JK.Colors.selected]}7{/color} 8 9 10 11{/b}")
                        use JK_ToggleSettingGlobalizationButton("seamlessPagination")

                    use JK_YSpacer(2)

                    use JK_Title("Personalização", 2)

                    hbox:
                        use JK_XSpacer()

                        vbox:
                            hbox:
                                use JK_Checkbox(checked=JK.Settings.paginationGoTo, text="Exibir botão “Ir para”", action=JK.Settings.ToggleEnabledAction("paginationGoTo"))
                                use JK_ToggleSettingGlobalizationButton("paginationGoTo")

                            hbox:
                                use JK_Checkbox(checked=JK.Settings.paginationAutoSaves, text="Exibir botão de salvamentos automáticos", action=JK.Settings.ToggleEnabledAction("paginationAutoSaves"))
                                use JK_ToggleSettingGlobalizationButton("paginationAutoSaves")

                            hbox:
                                use JK_Checkbox(checked=JK.Settings.paginationQuickSaves, text="Exibir botão de salvamentos rápidos", action=JK.Settings.ToggleEnabledAction("paginationQuickSaves"))
                                use JK_ToggleSettingGlobalizationButton("paginationQuickSaves")

                            hbox:
                                use JK_Checkbox(checked=JK.Settings.paginationFirstPage, text="Exibir o botão “Ir para a primeira página”", action=JK.Settings.ToggleEnabledAction("paginationFirstPage"))
                                use JK_ToggleSettingGlobalizationButton("paginationFirstPage")

                            hbox:
                                use JK_Checkbox(checked=JK.Settings.paginationBigJump, text="Exibir botões << e >>", action=JK.Settings.ToggleEnabledAction("paginationBigJump"))
                                use JK_ToggleSettingGlobalizationButton("paginationBigJump")

                            hbox:
                                use JK_Checkbox(checked=JK.Settings.paginationNumbers, text="Exibir números das páginas", action=JK.Settings.ToggleEnabledAction("paginationNumbers"))
                                use JK_ToggleSettingGlobalizationButton("paginationNumbers")

                            hbox:
                                use JK_Checkbox(checked=JK.Settings.paginationLastPage, text="Exibir o botão “Ir para a última página”", action=JK.Settings.ToggleEnabledAction("paginationLastPage"))
                                use JK_ToggleSettingGlobalizationButton("paginationLastPage")

                    use JK_YSpacer(2)

                    use JK_Title("Pré-visualização", 3)

                    use JK_YSpacer(3)

                    hbox:
                        use JK_XSpacer(2)

                        use JK_PaginationContent(JK.Pagination.get_content())
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

screen JK_Settings_QuickSave():
    vbox:
        hbox:
            use JK_Checkbox(checked=JK.Settings.quickSaveEnabled, text="Ativado", action=JK.Settings.ToggleEnabledAction("quickSaveEnabled"))
            use JK_ToggleSettingGlobalizationButton("quickSaveEnabled")

        hbox:
            use JK_XSpacer()

            vbox:
                hbox:
                    use JK_Checkbox(checked=JK.Settings.quickSaveNotificationEnabled, text="Exibir notificação ao fazer um salvamento rápido", action=JK.Settings.ToggleEnabledAction("quickSaveNotificationEnabled"), disabled=not JK.Settings.quickSaveEnabled)
                    use JK_ToggleSettingGlobalizationButton("quickSaveNotificationEnabled", disabled=not JK.Settings.quickSaveEnabled)

                hbox:
                    use JK_Checkbox(checked=JK.Settings.offsetSlotAfterQuickSave, text="Avançar um slot após o salvamento rápido", action=JK.Settings.ToggleEnabledAction("offsetSlotAfterQuickSave"), disabled=not JK.Settings.quickSaveEnabled)
                    use JK_Helper("Quando ativado, um salvamento rápido avança um slot e impede que o próximo salvamento automático ou rápido o sobrescreva.", disabled=not JK.Settings.quickSaveEnabled)
                    use JK_ToggleSettingGlobalizationButton("offsetSlotAfterQuickSave", disabled=not JK.Settings.quickSaveEnabled)

                hbox:
                    use JK_Checkbox(checked=JK.Settings.pageFollowsQuickSave, text="Mudar de página conforme o slot do salvamento rápido", action=JK.Settings.ToggleEnabledAction("pageFollowsQuickSave"), disabled=not JK.Settings.quickSaveEnabled)
                    use JK_ToggleSettingGlobalizationButton("pageFollowsQuickSave", disabled=not JK.Settings.quickSaveEnabled)

                use JK_YSpacer(2)

                hbox:
                    text "Atalho para salvamento rápido" yalign 0.5:
                        if not JK.Settings.quickSaveEnabled:
                            color JK.Colors.disabled
                    use JK_ToggleSettingGlobalizationButton("quickSaveKey", disabled=not JK.Settings.quickSaveEnabled)

                use JK_KeyInput(assignment=JK.Settings.quickSaveKey, action=JK.Settings.get_set_key_action("quickSaveKey"), disabled=not JK.Settings.quickSaveEnabled)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

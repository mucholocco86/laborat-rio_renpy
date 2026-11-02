screen JK_Settings(section="ACCESSIBILITY"):
    layer "JK_Overlay"
    style_prefix 'JK'
    modal True

    default original_size_adjustment = JK.Settings.sizeAdjustment
    default active_section = section

    python:
        reset_size_adjustment_hint = "Se algo der errado, você pode reverter o valor de uma destas formas:\n  a) pela caixa de confirmação;\n  b) aguardando 60 segundos;\n  c) pressionando {b}CTRL + SHIFT + ALT + P{/b} ao mesmo tempo."

        default_close_action = Hide("JK_Settings")
        close_action = default_close_action
        if original_size_adjustment != JK.Settings.sizeAdjustment and JK.Settings.sizeAdjustment != 0:
            close_action = [JK.ShowConfirmAction(title="Há um ajuste de tamanho ainda não aplicado. Deseja aplicá-lo agora?", message=reset_size_adjustment_hint, yes=[JK.Settings.ApplySizeAdjustmentAction(), default_close_action], yes_text="Aplicar agora", yes_color=JK.Colors.success, no_text="Voltar")]

        sections = [
            ("ACCESSIBILITY", "\ue84e", "Acessibilidade"),
            ("AUTOSAVE", "\ue167", "Salvamento automático"),
            ("QUICKSAVE", "\ue161", "Salvamento rápido"),
            ("SIDEPANEL", "\ue8aa", "Painel lateral"),
            
            ("SAVE_LOAD", "\ue0e0", "Salvar/Carregar"),
            ("CUSTOMIZATION", "\ue40a", "Personalização"),
            ("UPDATES", "\ue8d7", "Atualizações"),
        ]

        if renpy.config.developer:
            sections.append(("DEBUG", "\ue868", "Depuração"))

    use JK_Dialog(title="Configurações", close_action=close_action):
        style_prefix "JK"

        grid len(sections) 1:
            xfill True

            style_prefix "JK_Settings_Tab"

            for section in sections:
                button:
                    xfill True

                    if section[0] == "DEBUG":
                        selected JK.Settings.debugEnabled
                        style "JK_Settings_Tab_button_debug"
                        action JK.Settings.ToggleEnabledAction("debugEnabled")

                    else:
                        selected section[0] == active_section
                        action SetScreenVariable("active_section", section[0])

                    vbox:
                        xalign 0.5

                        if section[1]:
                            hbox:
                                xalign 0.5

                                use JK_Icon(section[1])

                        use JK_YSpacer(4)

                        text section[2]

        use JK_YSpacer(2)

        viewport:
            mousewheel True
            draggable True
            scrollbars "vertical"
            vscrollbar_unscrollable "hide"
            pagekeys True
            ymaximum 0.85

            if active_section == "ACCESSIBILITY":
                use JK_Settings_Accessibility(original_size_adjustment, reset_size_adjustment_hint)
            elif active_section == "AUTOSAVE":
                use JK_Settings_Autosave()
            elif active_section == "QUICKSAVE":
                use JK_Settings_QuickSave()
            elif active_section == "SIDEPANEL":
                use JK_Settings_Sidepanel()
            elif active_section == "MEMORIES":
                use JK_Settings_Memories()
            elif active_section == "SAVE_LOAD":
                use JK_Settings_LoadSave()
            elif active_section == "UPDATES":
                use JK_Settings_Updates()
            elif active_section == "CUSTOMIZATION":
                use JK_Settings_Customization()

        hbox:
            xfill True
            yfill True

            vbox:
                yalign 1.0

                use JK_Title(JK.MOD_NAME + " v" + JK.MOD_VERSION)

                use JK_YSpacer(2)

                use JK_Title("Encontrou algum problema?", size=3, color=JK.Colors.error)
                text "Acesse nosso {a=[JK.DISCORD_URL]}Discord{/a} ou o {a=https://github.com/[JK.MOD_GITHUB_OWNER]/[JK.MOD_GITHUB_REPO]}GitHub{/a}."

            hbox:
                style_prefix "JK_dialog_action_buttons"

                vbox:

                    hbox:
                        use JK_IconButton(icon="\ue8ba", text="Redefinir", action=Show("JK_ResetSettingsConfirm"), color=JK.Colors.danger)


                    hbox:
                        use JK_IconButton(icon="\ue5cd", text="Fechar", action=close_action)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

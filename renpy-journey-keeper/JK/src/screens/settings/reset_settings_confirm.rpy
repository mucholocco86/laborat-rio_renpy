screen JK_ResetSettingsConfirm():
    layer "JK_Overlay"
    style_prefix 'JK'
    modal True

    default include_global = False

    use JK_Dialog(title="Redefinir configurações", close_action=Hide("JK_ResetSettingsConfirm")):
        style_prefix "JK"

        vbox xalign 0.5 yalign 0.5:
            if include_global:
                text "Deseja mesmo restaurar todas as configurações, inclusive as globais, para os valores padrão?"
            else:
                text "Deseja mesmo restaurar todas as configurações locais para os valores padrão?"

            use JK_YSpacer(offset=2)

            hbox xalign 0.5:
                use JK_Checkbox(checked=include_global, text="Incluir configurações globais", action=ToggleScreenVariable('include_global', True, False))

        hbox:
            xfill True
            yfill True

            style_prefix "JK_dialog_action_buttons"

            vbox:

                hbox:
                    use JK_IconButton(icon="\ue8ba", text="Redefinir tudo" if include_global else "Redefinir", action=[JK.Settings.ResetAction(include_global), Hide("JK_ResetSettingsConfirm")], color=JK.Colors.danger)


                hbox:
                    use JK_IconButton(icon="\ue5cd", text="Fechar", action=Hide("JK_ResetSettingsConfirm"))
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

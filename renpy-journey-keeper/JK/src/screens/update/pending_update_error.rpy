screen JK_PendingUpdateError(release, error):
    style_prefix 'JK'
    modal True

    vbox:
        xfill True
        yfill True
        ymaximum 0.85

        vbox align (0.5, 0.5):
            hbox xalign 0.5:
                use JK_Title("Erro", color=JK.Colors.danger)

            use JK_YSpacer(offset=2)

            vbox xalign 0.5:
                text error xalign 0.5 text_align 0.5

                use JK_YSpacer(offset=2)

                if JK.Updater.rpa_locked_exception:
                    text "O Ren’Py mantém o arquivo antigo do mod aberto e isso impede a atualização. Esse comportamento é comum no Ren’Py 8 ou superior." text_align 0.5 xalign 0.5
                    use JK_YSpacer(4)
                    text "Para tentar resolver, clique em {a=JK_Run:JK.Updater.RestartGameAction()}Recarregar e atualizar{/a}. O jogo será recarregado e talvez libere o arquivo. Se o problema continuar, outro programa pode estar usando-o." text_align 0.5 xalign 0.5
                    use JK_YSpacer(4)
                    text "Como alternativa, feche o jogo, abra a pasta {a=JK_Run:JK.OpenGameDirectoryAction()}/game{/a} e renomeie o arquivo {i}\"[JK.Updater.temp_asset_name]\"{/i} para {i}\"[JK.Updater.asset_name]\"{/i}." text_align 0.5 xalign 0.5

                    use JK_ErrorFooter("PENDING_UPDATE_ERROR_RPY8_EXPECTED")
                else:
                    use JK_ErrorFooter()


    hbox:
        xfill True
        yfill True

        style_prefix "JK_dialog_action_buttons"

        vbox:
            if JK.Updater.rpa_locked_exception:

                hbox:
                    use JK_IconButton(icon="\ue5d5", text="Recarregar e atualizar", action=JK.Updater.RestartGameAction())
            else:

                hbox:
                    use JK_IconButton(icon="\ue5d5", text="Tentar novamente", action=JK.Updater.InstallUpdateAction(release))


            hbox:
                use JK_IconButton(icon="\ue5cd", text="Fechar", action=Hide("JK_PendingUpdate"))
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

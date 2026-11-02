screen JK_PendingUpdateSuccess():
    style_prefix 'JK'
    modal True

    vbox:
        xfill True
        yfill True
        ymaximum 0.85

        vbox align (0.5, 0.5):
            use JK_Title("Atualização instalada com sucesso.", color=JK.Colors.success)
            use JK_InfoBox("Reinicie o jogo para ver as alterações.")


    hbox:
        xfill True
        yfill True

        style_prefix "JK_dialog_action_buttons"

        vbox:

            hbox:
                use JK_IconButton(icon="\ue9ba", text="Reiniciar o jogo", action=JK.Updater.RestartGameAction())


            hbox:
                use JK_IconButton(icon="", text="OK", action=Hide("JK_PendingUpdate"))
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

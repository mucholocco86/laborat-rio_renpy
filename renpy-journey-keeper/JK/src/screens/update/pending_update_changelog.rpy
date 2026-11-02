screen JK_PendingUpdateChangelog(release):
    style_prefix 'JK'
    modal True

    viewport:
        mousewheel True
        draggable True
        scrollbars "vertical"
        vscrollbar_unscrollable "hide"
        pagekeys True
        ymaximum 0.85

        has vbox
        text release.changelog or "{i}\"Parece que eu estava com tanta pressa que esqueci de escrever as alterações desta versão. Desculpe!\"{/i}\n -- Smrdgy"

        use JK_YSpacer(offset=2)

        text "Para consultar as alterações, acesse {a=https://github.com/[JK.MOD_GITHUB_OWNER]/[JK.MOD_GITHUB_REPO]/commits/}o histórico de commits{/a}."

    hbox:
        xfill True
        yfill True

        style_prefix "JK_dialog_action_buttons"

        hbox:
            style_prefix "JK"

            text "{a=https://github.com/[JK.MOD_GITHUB_OWNER]/[JK.MOD_GITHUB_REPO]/releases/latest}{color=[JK.Colors.text_light]}Para baixar manualmente, clique aqui.{/color}{/a}" yalign 0.5
            use JK_Icon(icon="\ue895", size=20, color=JK.Colors.text_light, hover_color=JK.Colors.text_light)

        vbox:

            hbox:
                use JK_IconButton(icon="\ue884", text="Baixar e instalar", action=JK.Updater.InstallUpdateAction(release), color=JK.Colors.success)


            hbox:
                use JK_IconButton(icon="\ue14b", text="Ignorar esta versão", action=[JK.Updater.SkipUpdateAction(release.version), Hide("JK_PendingUpdate")])


            hbox:
                use JK_IconButton(icon="\ue888", text="Desativar atualizações", action=[JK.Updater.DisableUpdatesAction(), Hide("JK_PendingUpdate")], color=JK.Colors.danger)


            hbox:
                use JK_IconButton(icon="\ue5cd", text="Fechar", action=Hide("JK_PendingUpdate"))
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

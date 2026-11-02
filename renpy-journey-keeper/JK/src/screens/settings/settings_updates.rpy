screen JK_Settings_Updates():
    default releases_view_model = JK.ReleasesViewModel()

    vbox:
        hbox:
            text "Estas configurações são sempre globais." color JK.Colors.status_enabled_disabled yalign 0.5

            use JK_ToggleSettingGlobalizationButton("", disabled=True, force_enabled=True)

        use JK_YSpacer()

        hbox:
            hbox yalign 0.5:
                python:
                    if JK.Updater.latest:
                        state = "{a=[JK.Updater.latest.url]}[JK.Updater.latest.version]"
                    elif JK.Updater.loading:
                        state = "{color=[JK.Colors.info]}Carregando...{/color}"
                    else:
                        state = "{color=[JK.Colors.na]}N/A{/color}"

                text "Versão mais recente: {}".format(state)

                if JK.Updater.latest and JK.Updater.latest.version == JK.MOD_VERSION:
                    text "{size=-5} (Você tem a versão mais recente.){/size}" color JK.Colors.success yalign 0.5

            use JK_IconButton("\ue5d5", text="Atualizar lista", action=JK.Updater.CheckForUpdateAction())

            if not JK.Updater.installed and JK.Updater.latest and JK.Updater.latest.version:
                use JK_IconButton(icon="\ue8d7", text="Baixar e instalar {}".format(JK.Updater.latest.version), action=JK.Updater.InstallUpdateAction(JK.Updater.latest))

        if JK.Updater.installed:
            hbox:
                button yalign 0.5:
                    action NullAction()
                    use JK_Icon("\uf05a", size=20, color=JK.Colors.warning)

                text "Há uma atualização pronta para ser instalada." color JK.Colors.warning yalign 0.5

                use JK_IconButton(text="Clique aqui para recarregar o jogo", action=JK.Updater.RestartGameAction())
        elif JK.Updater.error:
            text JK.Updater.error color JK.Colors.error

        use JK_Checkbox(checked=JK.Settings.updaterEnabled, text="Verificar atualizações sempre que o jogo iniciar", action=JK.Settings.ToggleEnabledAction("updaterEnabled"))

        hbox:
            use JK_XSpacer()

            vbox:
                use JK_Checkbox(checked=JK.Settings.noUpdatePrompt, text="Não mostrar aviso de atualização", action=JK.Settings.ToggleEnabledAction("noUpdatePrompt"), disabled=not JK.Settings.updaterEnabled)

                hbox:
                    use JK_XSpacer()

                    vbox:
                        use JK_Checkbox(checked=JK.Settings.autoUpdateWithoutPrompt, text="Instalar a atualização automaticamente", action=JK.Settings.ToggleEnabledAction("autoUpdateWithoutPrompt"), disabled=not JK.Settings.noUpdatePrompt)

        use JK_Title("Registro de alterações")

        if releases_view_model.releases:
            for release in releases_view_model.releases:
                vbox:
                    hbox:
                        use JK_Title(release.version, 2, color=JK.Colors.warning)

                        hbox yalign 0.5:
                            use JK_IconButton(icon="\ue895", action=OpenURL(release.url), tt="Abrir no navegador", size=20)
                            $ confirm_action = JK.ShowConfirmAction(title="Instalar {{color=[JK.Colors.theme]}}{}{{/color}}?".format(release.version), message="{color=[JK.Colors.warning]}Atenção: versões antigas podem causar falhas, corromper suas jornadas ou redefinir suas configurações.{/color}", yes=JK.Updater.InstallUpdateAction(release), yes_text="Baixar e instalar", yes_icon="\uf090", yes_color=JK.Colors.danger)
                            use JK_IconButton(icon="\uf090", action=confirm_action, tt="Baixar e instalar {}".format(release.version), size=20)

                    if release.changelog:
                        text release.changelog
                    else:
                        text "(Sem descrição)" color JK.Colors.na

                    use JK_YSpacer(2)
        else:
            use JK_IconButton(icon="\uf090", text="Carregando..." if releases_view_model.loading else "Carregar versões", action=Function(releases_view_model.fetch_all_releases))

            if releases_view_model.error:
                text releases_view_model.error color JK.Colors.error
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

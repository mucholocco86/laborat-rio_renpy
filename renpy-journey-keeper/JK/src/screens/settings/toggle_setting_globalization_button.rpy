screen JK_ToggleSettingGlobalizationButton(key, disabled=False, force_enabled=False):
    if JK.UserDir.is_available():
        $ enabled = force_enabled or key in JK.Settings.globalizedSettings

        hbox yalign 0.5:
            use JK_IconButton(icon="\ue80b" if enabled else "\uf1ca", action=JK.Settings.ToggleGlobalizedSettingAction(key), color=JK.Colors.success if enabled else JK.Colors.text_light, size=20, tt="Desativar o compartilhamento global desta configuração" if enabled else "Ative o compartilhamento global desta configuração para usar o mesmo valor em todos os jogos.\nNo momento, está {color=[JK.Colors.error]}desativado{/color}.", disabled=disabled, hover_color=JK.Colors.hover, disabled_color=JK.Colors.status_enabled_disabled if enabled else JK.Colors.disabled)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

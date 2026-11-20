screen JK_Settings_Autosave():
    vbox:
        hbox:
            use JK_Checkbox(checked=JK.Settings.autosaveNotificationEnabled, text="Exibir notificação ao salvar automaticamente", action=JK.Settings.ToggleEnabledAction("autosaveNotificationEnabled"))
            use JK_ToggleSettingGlobalizationButton("autosaveNotificationEnabled")

        hbox:
            use JK_Checkbox(checked=JK.Settings.pageFollowsAutoSave, text="Mudar de página conforme o slot do salvamento automático", action=JK.Settings.ToggleEnabledAction("pageFollowsAutoSave"))
            use JK_ToggleSettingGlobalizationButton("pageFollowsAutoSave")

        hbox:
            use JK_Checkbox(checked=JK.Settings.autosaveOnSingletonChoice, text="Salvar automaticamente mesmo quando houver apenas uma escolha", action=JK.Settings.ToggleEnabledAction("autosaveOnSingletonChoice"))
            use JK_Helper("Quando ativado, o mod criará um salvamento automático mesmo quando houver apenas uma escolha.")
            use JK_ToggleSettingGlobalizationButton("autosaveOnSingletonChoice")







        hbox:
            use JK_Checkbox(checked=JK.Settings.showConfirmOnLargePageJump, text="Pedir confirmação quando houver um salto inesperado de página", action=JK.Settings.ToggleEnabledAction("showConfirmOnLargePageJump"))
            use JK_Helper("Quando ativado, uma confirmação aparecerá se a página avançar mais de uma página durante o jogo.")
            use JK_ToggleSettingGlobalizationButton("showConfirmOnLargePageJump")

        use JK_YSpacer(2)

        hbox:
            text "Tecla modificadora para impedir o salvamento automático" yalign 0.5
            use JK_Helper("Enquanto esta tecla estiver pressionada, escolhas não gerarão salvamentos automáticos.")
            use JK_ToggleSettingGlobalizationButton("preventAutosaveModifierKey")

        use JK_Radio(checked=not JK.Settings.preventAutosaveModifierKey, text="Nenhum", action=JK.Settings.SetAction("preventAutosaveModifierKey", None))
        use JK_Radio(checked="ALT" == JK.Settings.preventAutosaveModifierKey, text="Alt", action=JK.Settings.SetAction("preventAutosaveModifierKey", "ALT"))
        use JK_Radio(checked="SHIFT" == JK.Settings.preventAutosaveModifierKey, text="Shift", action=JK.Settings.SetAction("preventAutosaveModifierKey", "SHIFT"))

        use JK_YSpacer(2)

        hbox:
            text "Atalho para alternar o salvamento automático" yalign 0.5
            use JK_ToggleSettingGlobalizationButton("autosaveKey")

        use JK_KeyInput(assignment=JK.Settings.autosaveKey, action=JK.Settings.get_set_key_action("autosaveKey"))

        use JK_YSpacer()

        use JK_Title("Avançado", color=JK.Colors.warning)

        hbox:
            use JK_Checkbox(checked=JK.Settings.preventAutosavingWhileNotInGame, text="Restringir o salvamento automático durante o jogo", action=JK.Settings.TogglePreventAutosavingWhileNotInGameEnabledAction())
            use JK_Helper("Alguns jogos não indicam corretamente quando a partida começa, o que pode impedir o salvamento automático nas escolhas. Desativar esta opção {b}pode{/b} resolver o problema.\n\n{color=[JK.Colors.warning]}Atenção: desativá-la pode causar perda de salvamentos. Por exemplo, uma verificação de idade 18+ pode sobrescrever o slot 1-1 se aparecer antes do menu principal.{/color}\n\n{color=[JK.Colors.text_light]}Para quem conhece o funcionamento interno do Ren’Py: este mod aguarda o rótulo {u}start{/u} antes de permitir qualquer salvamento automático.{/color}")

        hbox:
            use JK_Checkbox(checked=JK.Settings.autosaveOnNormalButtonsWithJump, text="Salvar automaticamente ao clicar em botões comuns", action=JK.Settings.ToggleEnabledAction("autosaveOnNormalButtonsWithJump"))
            use JK_Helper("{color=[JK.Colors.info]}Se as escolhas não estiverem acionando os salvamentos automáticos como esperado, ativar esta opção pode ajudar.{/color}\n\nQuando ativada, cada botão se comporta como uma escolha e aciona um salvamento automático ao ser clicado. Porém, somente os botões que representam escolhas no jogo se qualificam.\n{color=[JK.Colors.warning]}Alguns botões que não são escolhas, como os de navegação livre, também podem acionar salvamentos automáticos.{/color}\n\n{b}Para usuários avançados:{/b}\nO salvamento automático ocorre somente em botões com uma ação Jump, considerando apenas interações relacionadas à navegação. Não é possível refinar mais esse filtro.", side="right")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

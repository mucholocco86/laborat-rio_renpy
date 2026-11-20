screen JK_ErrorFooter(source=None):
    default report_it_text = "{a=[JK.DISCORD_URL]}Discord{/a} ou {a=https://github.com/[JK.MOD_GITHUB_OWNER]/[JK.MOD_GITHUB_REPO]/issues}GitHub{/a}"

    if source == "PENDING_UPDATE_ERROR_RPY8_EXPECTED":
        text "Se isso não foi causado por uma ação sua e o problema continuar após reiniciar o jogo, informe em " + report_it_text xalign 0.5 text_align 0.5
    else:
        text "Consulte log.txt para mais informações" xalign 0.5 text_align 0.5

        use JK_YSpacer(2)

        text "Se isso não foi causado por uma ação sua (por exemplo, permissões incorretas ou arquivos excluídos manualmente), informe em " + report_it_text xalign 0.5 text_align 0.5
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

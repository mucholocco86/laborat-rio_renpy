screen JK_PendingUpdateReloadAndUpdate():
    style_prefix "JK"
    modal True

    python:
        class Reload(renpy.ui.Action):
            def __call__(self):
                renpy.utter_restart()

    vbox:
        xfill True
        yfill True

        vbox:
            xalign 0.5
            yalign 0.5

            hbox:
                xalign 0.5

                use JK_Title("Recarregando...")

            use JK_YSpacer(2)

            if JK.Updater.rpa_locked_exception:
                text "Isso pode levar um minuto. O jogo será recarregado duas vezes: primeiro para liberar o arquivo do mod e depois para aplicar a atualização." xalign 0.5 text_align 0.5


    timer 0.1 action Reload()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

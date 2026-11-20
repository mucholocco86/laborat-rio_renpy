screen JK_MovePlaythroughDirectoryError(playthrough, errors=[]):
    layer "JK_Overlay"
    style_prefix "JK"
    modal True

    $ errorsLen = len(errors)

    use JK_Dialog(title="Falha ao renomear as pastas", close_action=Hide("JK_MovePlaythroughDirectoryError")):
        viewport:
            mousewheel True
            draggable True
            scrollbars "vertical"
            vscrollbar_unscrollable "hide"
            pagekeys True
            ymaximum 0.85

            has vbox
            text "Não foi possível mover {b}{color=[JK.Colors.theme]}[errorsLen]{/c}{/b} pasta(s):"

            use JK_YSpacer(offset=3)

            for error in errors:
                python:
                    errorText = ""

                    if error[1] == "LOCATION_EXISTS":
                        errorText = "A pasta já existe"
                    else:
                        errorText = error[1]

                hbox:
                    button:
                        action JK.OpenDirectoryAction(path=error[0])

                        has hbox yalign 0.5
                        text error[0] yalign 0.5

                        text "  "

                        use JK_Icon(icon="\ue2c8")

                    text " - " + errorText color JK.Colors.error yalign 0.5

        hbox:
            xfill True
            yfill True

            style_prefix "JK_dialog_action_buttons"

            vbox:

                hbox:
                    use JK_IconButton(icon="\ue15a", text="Sobrescrever", action=JK.ShowConfirmAction(title="Sobrescrever pastas em conflito", message="Tem certeza? Isso excluirá todos os dados armazenados nessas pastas.\n\nEsta ação {u}{color=[JK.Colors.error]}é irreversível{/c}{/u}.", yes=[Hide("JK_MovePlaythroughDirectoryError"), JK.Playthroughs.ForceRenamePlaythroughAction(playthrough)], yes_color=JK.Colors.danger), color=JK.Colors.danger, spacing=JK.scaled(5))


                hbox:
                    use JK_IconButton(icon="\ue5cd", text="Fechar", action=Hide("JK_MovePlaythroughDirectoryError"))
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

screen JK_RemovePlaythroughConfirm(playthrough):
    layer "JK_Overlay"
    style_prefix 'JK'
    modal True

    default delete_files = False

    $ deleteAction = [JK.Playthroughs.RemoveAction(playthrough.id, delete_files), Hide("JK_RemovePlaythroughConfirm"), Hide("JK_EditPlaythrough")]

    use JK_Dialog(title="Excluir jornada", close_action=Hide("JK_RemovePlaythroughConfirm")):
        key 'K_RETURN' action deleteAction
        key 'K_KP_ENTER' action deleteAction

        text "Tem certeza de que deseja remover \"[playthrough.name]\"?" xalign .5

        frame:
            background None
            xalign 0.5
            padding (0, 10, 0, 0)

            use JK_Checkbox(checked=delete_files, text="Excluir arquivos", action=ToggleScreenVariable('delete_files', True, False))

        frame:
            background None
            padding (0, 0, 10, 0)
            xalign 0.5

            has hbox yalign .5
            use JK_InfoBox("Se você excluir os arquivos, não poderá recuperar esta jornada.")

        python:
            removeText = "Remover e excluir arquivos" if delete_files else "Remover"

        hbox:
            xfill True
            yfill True

            style_prefix "JK_dialog_action_buttons"

            vbox:

                hbox:
                    use JK_IconButton(icon="\ue92b", text=removeText, action=deleteAction, color=JK.Colors.danger)


                hbox:
                    use JK_IconButton(icon="\ue5cd", text="Fechar", action=Hide("JK_RemovePlaythroughConfirm"))
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

screen JK_QuickSaveOverwriteConfirm():
    layer "JK_Overlay"
    style_prefix 'JK'

    default title = "Tem certeza de que deseja sobrescrever este salvamento?"

    python:
        close_action = Hide("JK_QuickSaveOverwriteConfirm")
        overwrite_action = [JK.Playthroughs.QuickSaveAction(force=True), Hide("JK_QuickSaveOverwriteConfirm")]
        skip_one_action = [Hide("JK_QuickSaveOverwriteConfirm"), JK.Playthroughs.QuickSaveAction(move_one=True)]

    use JK_Dialog(title=title, close_action=close_action):
        vbox:
            xfill True

            python:
                page, slot, _ = JK.Autosaver.get_current_slot()

            add FileScreenshot(name=slot, page=page) xalign 0.5

            text "[renpy.store.JK_ActiveSlot]" xalign 0.5 text_align 0.5

        hbox:
            xfill True
            yfill True

            style_prefix "JK_dialog_action_buttons"

            vbox:

                hbox:
                    use JK_IconButton(icon="\ue161", text="Sobrescrever", action=overwrite_action, color=JK.Colors.danger)


                hbox:
                    use JK_IconButton(icon="\ue3cd", text="Salvar no próximo slot", action=skip_one_action)


                hbox:
                    use JK_IconButton(icon="\ue5cd", text="Não", action=close_action)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

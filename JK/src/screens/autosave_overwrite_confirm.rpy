screen JK_AutosaveOverwriteConfirm():
    default title = "Tem certeza de que deseja sobrescrever este salvamento?"
    default message = "Ao escolher “Não e desativar salvamento automático”, o recurso ficará desativado até você ativá-lo novamente."

    layer "JK_Overlay"
    style_prefix 'JK'

    use JK_Dialog(title=title, message=message, close_action=[JK.Autosaver.ConfirmDialogCloseAction(), Hide("JK_AutosaveOverwriteConfirm")]):
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
                    use JK_IconButton(icon="\ue161", text="Sobrescrever", action=[JK.Autosaver.ConfirmDialogSaveAction(), JK.Autosaver.ConfirmDialogCloseAction(), Hide("JK_AutosaveOverwriteConfirm")], color=JK.Colors.danger)


                hbox:
                    use JK_IconButton(icon="\ue3cd", text="Salvar no próximo slot", action=[JK.Autosaver.MoveOneSlotOverAction(), Hide("JK_AutosaveOverwriteConfirm"), JK.Autosaver.TrySavePendingSaveAction()])


                hbox:
                    use JK_IconButton(icon="\ue044", text="Pular desta vez", action=[JK.Autosaver.ConfirmDialogCloseAction(), Hide("JK_AutosaveOverwriteConfirm")])


                hbox:
                    use JK_IconButton(icon="\ue5cd", text="Não e desativar salvamento automático", action=[JK.Playthroughs.ToggleAutosaveOnChoicesForActiveAction(), JK.Autosaver.ConfirmDialogCloseAction(), Hide("JK_AutosaveOverwriteConfirm")])
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

screen JK_ExitMemoryConfirm():
    layer "screens"
    style_prefix "JK"
    modal True

    $ returnAction = [JK.Memories.ExitMemory(), MainMenu(confirm=False)]

    use JK_Dialog(title="Sair da memória", close_action=Return()):
        key 'K_RETURN' action returnAction
        key 'K_KP_ENTER' action returnAction

        vbox:
            hbox:
                xfill True

                text "Deseja sair desta memória?" xalign 0.5 text_align 0.5

            hbox:
                xfill True
                yfill True

                style_prefix "JK_dialog_action_buttons"

                vbox:

                    hbox:
                        use JK_IconButton(icon="\ue9ba", text="Sair da memória", action=returnAction, key="alt_K_e")


                    hbox:
                        use JK_IconButton(icon="\ue5c4", text="Retornar", action=Return())
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

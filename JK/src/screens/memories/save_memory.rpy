screen JK_SaveMemory():
    layer "JK_Overlay"
    style_prefix 'JK'
    modal True

    default name = ''

    default name_input = JK.TextInput("name", auto_focus=True)

    python:
        submitAction = [
            JK.Memories.CreateMemory(name=name),
            Hide('JK_SaveMemory')
        ]

    use JK_Dialog(title="Salvar memória", close_action=Hide("JK_SaveMemory")):
        style_prefix "JK"

        vbox:
            text "Nome:"
            add name_input.displayable(placeholder="Digite um nome ou deixe em branco para gerar um automaticamente")

        hbox:
            xfill True
            yfill True

            style_prefix "JK_dialog_action_buttons"

            vbox:

                hbox:
                    use JK_IconButton(icon="\ue161", text="Salvar", action=submitAction, key="alt_K_s")


                hbox:
                    use JK_IconButton(icon="\ue5cd", text="Fechar", action=Hide("JK_SaveMemory"))
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

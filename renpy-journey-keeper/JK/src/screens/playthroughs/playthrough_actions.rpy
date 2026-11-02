screen JK_PlaythroughActions(playthrough):
    layer "JK_Overlay"
    style_prefix 'JK'
    modal True

    use JK_Dialog(title="Ações da jornada", close_action=Hide("JK_PlaythroughActions")):
        style_prefix "JK"

        hbox:
            xfill True
            yfill True

            style_prefix "JK_dialog_action_buttons"

            vbox:

                hbox:
                    use JK_IconButton(icon="\ue8b6", text="Pesquisar jornada", action=[Show("JK_SearchPlaythrough"), Hide("JK_PlaythroughActions")], key="alt_K_f")


                hbox:
                    use JK_IconButton(icon="\uebbd", text="Duplicar jornada", action=[Show("JK_EditPlaythrough", playthrough=playthrough.copy().remove_unique_data(), duplicating=True), Hide("JK_PlaythroughActions")], key="alt_K_d")


                hbox:
                    use JK_IconButton(icon="\ue617", text="Gerenciar salvamentos", action=[Show("JK_SavesList", playthrough=playthrough), Hide("JK_PlaythroughActions")], key="alt_K_e")


                hbox:
                    use JK_IconButton(icon="\ue089", text="Organizar salvamentos em sequência", action=[JK.Playthroughs.TrySequentializeSaves(playthrough), Hide("JK_PlaythroughActions")], disabled=not JK.Utils.has_cols_and_rows_configuration(), key="alt_K_s")


                hbox:
                    use JK_IconButton(icon="\uf184", text="Exibir linha do tempo de escolhas", action=[Show("JK_ChoicesTimeline", playthrough=playthrough), Hide("JK_PlaythroughActions")], key="alt_K_t")


                hbox:
                    use JK_IconButton(icon="\ueb7d", text="Mover/copiar salvamentos", action=[Show("JK_MoveCopySaves", playthrough=playthrough), Hide("JK_PlaythroughActions")], key="alt_K_m")


                hbox:
                    use JK_IconButton(icon="\ue5cd", text="Fechar", action=Hide("JK_PlaythroughActions"))
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

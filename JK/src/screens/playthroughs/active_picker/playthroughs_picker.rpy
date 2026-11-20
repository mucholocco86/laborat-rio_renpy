screen JK_PlaythroughsPicker():
    layer "JK_Overlay"
    style_prefix 'JK'
    modal True

    default reorder_source = None


    $ playthroughs = [p for p in JK.Playthroughs.playthroughs if p.id != 2]

    use JK_Dialog(title="Selecionar uma jornada", close_action=Hide("JK_PlaythroughsPicker")):
        style_prefix "JK"

        hbox:
            xfill True


            hbox:
                spacing 10
                xalign 0.5

                use JK_IconButton(icon="\ue5c3", text="Grade", action=JK.Settings.SetAction("playthroughsViewMode", "grid"), toggled=JK.Settings.playthroughsViewMode == "grid", toggled_color=JK.Colors.selected)
                use JK_IconButton(icon="\ue8e9", text="Linhas", action=JK.Settings.SetAction("playthroughsViewMode", "rows"), toggled=JK.Settings.playthroughsViewMode == "rows", toggled_color=JK.Colors.selected)

        use JK_YSpacer(2)

        viewport:
            mousewheel True
            draggable True
            scrollbars "vertical"
            vscrollbar_unscrollable "hide"
            pagekeys True
            ymaximum 0.9

            if JK.Settings.playthroughsViewMode == "grid":
                use JK_PlaythroughsGridPicker(playthroughs, reorder_source)
            elif JK.Settings.playthroughsViewMode == "rows":
                use JK_PlaythroughsTablePicker(playthroughs, reorder_source)


        hbox:
            xfill True
            yfill True

            style_prefix "JK_dialog_action_buttons"

            vbox xalign 0.0:

                hbox:
                    if JK.UserDir.is_available:
                        use JK_IconButton(icon="\ue884", text="Importar de outro jogo", action=Show("JK_ImportPlaythroughs"))

            vbox xalign 1.0:

                hbox:
                    use JK_IconButton(icon="\ue5cd", text="Fechar", action=Hide("JK_PlaythroughsPicker"))
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

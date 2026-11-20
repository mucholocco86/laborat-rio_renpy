screen JK_SavesListNoSaves():
    style_prefix 'JK'
    modal True

    vbox:
        xfill True
        yfill True
        ymaximum 0.85

        vbox align (0.5, 0.5):
            use JK_Title("Nenhum salvamento", color=JK.Colors.error)


    hbox:
        xfill True
        yfill True

        style_prefix "JK_dialog_action_buttons"

        vbox:

            hbox:
                use JK_IconButton(icon="", text="OK", action=Hide("JK_SavesList"))
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

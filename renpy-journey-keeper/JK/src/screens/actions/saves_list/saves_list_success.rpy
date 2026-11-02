screen JK_SavesListSuccess(view_model):
    style_prefix 'JK'
    modal True

    vbox:
        xfill True
        yfill True
        ymaximum 0.85

        vbox align (0.5, 0.5):
            use JK_Title("Done", color=JK.Colors.success)


    hbox:
        xfill True
        yfill True

        style_prefix "JK_dialog_action_buttons"

        vbox:

            hbox:
                if view_model.return_on_success:
                    use JK_IconButton(icon="", text="OK", action=JK.SavesListViewModel.ClearSuccessAction(view_model))
                else:
                    use JK_IconButton(icon="", text="OK", action=Hide("JK_SavesList"))
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

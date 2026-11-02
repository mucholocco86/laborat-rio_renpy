screen JK_ChoicesTimelineLoading(view_model):
    style_prefix 'JK'
    modal True

    python:
        loaded = view_model.loaded
        to_load = view_model.to_load








    vbox:
        xfill True
        yfill True
        ymaximum 0.85

        vbox align (0.5, 0.5):
            xfill True
            xmaximum 0.85

            hbox xalign 0.5:
                use JK_Title("Reading saves...")

            use JK_YSpacer()

            text "[loaded]/[to_load]" xalign 0.5
            bar value loaded range to_load


    hbox:
        xfill True
        yfill True

        style_prefix "JK_dialog_action_buttons"

        vbox:




            hbox:
                use JK_IconButton(icon="\ue5cd", text="Close", action=Hide("JK_ChoicesTimeline"))
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

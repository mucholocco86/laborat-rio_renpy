






init 180 screen history():
    predict False tag menu


    use game_menu(_("History"), scroll=("vpgrid" if getattr(gui, "history_height", None) else "viewport"), yinitial=1.0):

        style_prefix "history"

        for h in _history_list:

            window:

                has fixed
                yfit True

                if h.who:

                    label h.who:
                        style "history_name"
                        substitute False
                        text_color godson_name_color_for(h.who)
                        text_outlines [(3, "#000000D0", 0, 2)]

                $ what = renpy.filter_text_tags(h.what, allow=getattr(gui, "history_allow_tags", { "alt", "noalt", "rt", "rb", "art" }))

                text what:
                    substitute False

        if not _history_list:

            label _("The dialogue history is empty.")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

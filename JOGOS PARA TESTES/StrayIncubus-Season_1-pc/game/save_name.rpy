init offset = 99

default persistent.save_naming = True


init -999 python:

    def pages_range():
        page = int(persistent._file_page)

        if page % 10 == 0:
            return (page // 10) - 1
        else:
            return page // 10


    if persistent.pages_range is None:
        if unicode(persistent._file_page).isnumeric():
            persistent.pages_range = pages_range()
        else:
            persistent.pages_range = 0

    class FilePageNewcode(Action, DictEquality):
        """
         :doc: file_action

         Sets the file page to `page`, which should be one of "auto", "quick",
         or an integer.
         """

        def __init__(self, page):
            self.page = str(page)

            if page == "auto":
                self.alt = _("File page auto")
            elif page == "quick":
                self.alt = _("File page quick")
            else:
                self.alt = _("File page [text]")

        def __call__(self):
            if not self.get_sensitive():
                return

            persistent._file_page = self.page

            if unicode(self.page).isnumeric():
                persistent.pages_range = pages_range()

            renpy.restart_interaction()

        def get_selected(self):
            return self.page == persistent._file_page

        def predict(self):
            _predict_file_page(self.page)


    class FilePageNextNewcode(Action, DictEquality):
        """
        :doc: file_action

        Goes to the next file page.

        `max`
            If set, this should be an integer that gives the number of
            the maximum file page we can go to.

        `wrap`
            If true, we can go to the first page when on the
            last file page if `max` is set.

        `auto`
            If true and wrap is set, this can bring the player to
            the page of automatic saves.

        `quick`
            If true and wrap is set, this can bring the player to
            the page of automatic saves.
        """

        alt = _("Next file page.")

        def __init__(self, max=None, wrap=False, auto=True, quick=True, increment=1):

            page = persistent._file_page

            if page == "auto":
                if increment == 10:
                    page = str((persistent.pages_range + 1) * 10 + 1)
                elif config.has_quicksave and quick:
                    page = "quick"
                else:
                    page = "1"

            elif page == "quick":
                if increment == 10:
                    page = str((persistent.pages_range + 1) * 10 + 1)
                else:
                    page = "1"

            else:
                page = int(page) + increment

                if max is not None:
                    if page > max:
                        if wrap:
                            if config.has_autosave and auto:
                                page = "auto"
                            elif config.has_quicksave and quick:
                                page = "quick"
                            else:
                                page = "1"
                        else:
                            page = None

                if page is not None:
                    page = str(page)

            self.page = page

        def __call__(self):
            if not self.get_sensitive():
                return

            persistent._file_page = self.page

            if unicode(self.page).isnumeric():
                persistent.pages_range = pages_range()

            renpy.restart_interaction()

        def get_sensitive(self):
            return self.page is not None

        def predict(self):
            _predict_file_page(self.page)


    class FilePagePreviousNewcode(Action, DictEquality):
        """
         :doc: file_action

         Goes to the previous file page, if possible.

        `max`
            If set, this should be an integer that gives the number of
            the maximum file page we can go to. This is required to enable
            wrap.

        `wrap`
            If true, we can go to the last page when on the first file page if max is set.

        `auto`
            If true, this can bring the player to
            the page of automatic saves.

        `quick`
            If true, this can bring the player to
            the page of automatic saves.

         """

        alt = _("Previous file page.")

        def __init__(self, max=None, wrap=False, auto=True, quick=True, decrement=1):

            if wrap and max is not None:
                max = str(max)
            else:
                max = None

            page = persistent._file_page

            if page == "auto":
                if decrement == 10 and persistent.pages_range > 0:
                    page = str((persistent.pages_range - 1) * 10 + 1)
                else:
                    page = max

            elif page == "quick":
                if decrement == 10 and persistent.pages_range > 0:
                    page = str((persistent.pages_range - 1) * 10 + 1)
                elif decrement == 1 and config.has_autosave and auto:
                    page = "auto"
                else:
                    page = max

            elif page == "1":
                if decrement == 1 and config.has_quicksave and quick:
                    page = "quick"
                elif decrement == 1 and config.has_autosave and auto:
                    page = "auto"
                else:
                    page = max

            else:
                if int(page) <= decrement:
                    page = max
                else:
                    page = str(int(page) - decrement)

            self.page = page

        def __call__(self):
            if not self.get_sensitive():
                return

            persistent._file_page = self.page

            if unicode(self.page).isnumeric():
                persistent.pages_range = pages_range()

            renpy.restart_interaction()

        def get_sensitive(self):
            return self.page

        def predict(self):
            _predict_file_page(self.page)



screen screen_save_name(slot):
    modal True
    zorder 200
    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:
        vbox:
            spacing 25
            xsize 650

#            if FileLoadable(slot):
#                label _("Save name ({color=#f00}overwrite{/color}):") style "confirm_prompt"
#            else:
#                label _("Save name ({color=#00ff00}new{/color}):") style "confirm_prompt"

            input:
                value VariableInputValue('save_name')
                length 30
                xalign 0.5
                exclude "\\[{"

            hbox:
                xfill True
                textbutton _("Yes") action FileAction(slot, confirm=False), Hide("screen_save_name") xalign 0.5
                textbutton _("No") action Hide("screen_save_name") xalign 0.5

    ## Right-click and escape answer "no".
    key "game_menu" action Hide("screen_save_name")

    ## Return of Enter answer "yes".
    key "K_RETURN" action FileAction(slot, confirm=False), Hide("screen_save_name")
    key "K_KP_ENTER" action FileAction(slot, confirm=False), Hide("screen_save_name")

screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))

    use game_menu(title):

        frame:
            style "empty"
            style_prefix "check"
            xsize 435
            xalign 0.93
            ypos -0.07

#            if persistent.save_naming:
#                textbutton _("Save naming enabled") action ToggleField(persistent,"save_naming")
#            else:
#                textbutton _("Save naming disabled") action ToggleField(persistent,"save_naming")

        fixed:

            ## This ensures the input will get the enter event before any of the
            ## buttons do.
            order_reverse True

            ## The page name, which can be edited by clicking on a button.
            button:
                style "page_label"

                key_events True
                ypos -0.07
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value

            ## The grid of file slots.
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.38

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        if renpy.current_screen().screen_name[0] == "load":
                            action FileAction(slot)
                        else:
                            # Highlight if the current save slot is the last save
                            selected (str(persistent._file_page) + "-" + str(slot) == renpy.newest_slot("[0-9]"))
                            if persistent.save_naming:
                                action SetVariable("save_name", FileSaveName(slot)), Show("screen_save_name", slot=slot)
                            else:
                                action SetVariable("save_name", FileSaveName(slot)), FileAction(slot)

                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                            style "slot_time_text"

                        text FileSaveName(slot).replace("[","[[").replace("{","{{"):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)

            ## Buttons to access other pages.
            hbox:
                style_prefix "page"
                ypos 0.93
                xalign 0.5
                yalign 1.0

                spacing gui.page_spacing

                textbutton _("<<") action FilePagePreviousNewcode(decrement=10)

                null width 25

                textbutton _("<") action FilePagePreviousNewcode()

                null width 10

                if config.has_autosave:
                    textbutton _("{#auto_page}A") xminimum 80 text_size 35 text_xalign 0.5 action FilePageNewcode("auto")

                if config.has_quicksave:
                    textbutton _("{#quick_page}Q") xminimum 80 text_size 35 text_xalign 0.5 action FilePageNewcode("quick")

                ## range(1, 10) gives the numbers from 1 to 9.
                for page in range( (persistent.pages_range * 10) + 1 , (persistent.pages_range * 10) + 11 ):
                    textbutton "[page]" xminimum 70 text_size 35 text_xalign 0.5 action FilePageNewcode(page)

                null width 10

                textbutton _(">") action FilePageNextNewcode()

                null width 25

                textbutton _(">>") action FilePageNextNewcode(increment=10)

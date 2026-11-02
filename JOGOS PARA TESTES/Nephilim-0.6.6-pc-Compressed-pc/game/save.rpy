init offset = 99

default persistent.save_naming = True
default page_range_min = 1
default page_range_max = 10

screen screen_save_name(slot):
    modal True
    zorder 200
    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:
        vbox:
            spacing 25
            xsize 650

            if FileLoadable(slot):
                label _("Save name ({color=#f00}overwrite{/color}):") style "confirm_prompt"
            else:
                label _("Save name ({color=#00ff00}new{/color}):") style "confirm_prompt"

            input:
                value VariableInputValue('save_name')
                length 30
                xalign 0.5

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
            xsize 860
            xalign 0.15
            ypos -0.07

            if persistent.save_naming:
                imagebutton auto "gui/button/save_naming_on_%s.png" action ToggleField(persistent,"save_naming")
            else:
                imagebutton auto "gui/button/save_naming_off_%s.png" action ToggleField(persistent,"save_naming")

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
            vpgrid cols gui.file_slot_cols:
                mousewheel True
                arrowkeys True
                draggable True
                scrollbars "vertical"
                side_xalign 0.0
                # ypos 250
                ymaximum 675
                style_prefix "slot"
                xalign 0.5
                yalign 0.2
                spacing gui.slot_spacing

                for i in range(1 * 100):

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

                        if persistent.relation_eu_measurements:
                            text FileTime(slot, format=_("{#file_time}%A, %d %B %Y, %H:%M"), empty=_("Empty")):
                                style "slot_time_text"
                        else:
                            text FileTime(slot, format=_("{#file_time}%A, %B %d, %Y, %H:%M"), empty=_("Empty")):
                                style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)
## BadMustard's code optional for delete file button be sure to get the images
                        if FileLoadable(slot):
                            imagebutton:
                                auto "images/delete/delete_%s.png"
                                action FileDelete(slot)
                                xalign 1.0
                                xoffset 15
                                yoffset -85 # 1920x1080  adjust as required
                                #yoffset -65 #1280x720  adjust as required
                                ## BadMustard's code optional stop just remove if not needed
                        ## BadMustard's code Stop (first section)
            ## Buttons to access other pages.
            vbox:
                style_prefix "page"
                xalign 0.5
                yalign 1.0
                hbox:
                    xalign 0.5

                    spacing gui.page_spacing

                    if page_range_min > 1:
                        textbutton _("<<") action [ SetVariable("page_range_min", page_range_min -9), SetVariable("page_range_max", page_range_max -9)]
                    textbutton _("<") action FilePagePrevious()

                    if config.has_autosave:
                        textbutton _("{#auto_page}A") action FilePage("auto")

                    if config.has_quicksave:
                        textbutton _("{#quick_page}Q") action FilePage("quick")

                    ## range(1, 10) gives the numbers from 1 to 9.
                    for page in range(page_range_min, page_range_max):
                        textbutton "[page]" action FilePage(page)

                    if page_range_max < 9999:
                        textbutton _(">") action FilePageNext()
                        textbutton _(">>") action [ SetVariable("page_range_min", page_range_min +9), SetVariable("page_range_max", page_range_max +9)]


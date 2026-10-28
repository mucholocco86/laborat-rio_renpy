init offset = 95


init -145 python:

    GODSON_SAVE_ALIGNMENT_VISUALS = {
    "neutral": (
        "NEUTRAL",
        "#718A96",
        "#718A9626",
        "#718A9670",
        "gui/neturalicon.png",
    ),
    "good": (
        "GOOD",
        "#479EF5",
        "#479EF526",
        "#479EF570",
        "gui/goodicon.png",
    ),
    "supergood": (
        "SUPER GOOD",
        "#E6EDF3",
        "#E6EDF326",
        "#E6EDF370",
        "gui/supergoodicon.png",
    ),
    "evil": (
        "EVIL",
        "#C94B58",
        "#C94B5826",
        "#C94B5870",
        "gui/evilicon.png",
    ),
    "sexaddict": (
        "SEX ADDICT",
        "#7D429F",
        "#7D429F26",
        "#7D429F70",
        "gui/sexaddicticon.png",
    ),
    "superevil": (
        "SUPER EVIL",
        "#2EDFE4",
        "#2EDFE426",
        "#2EDFE470",
        "gui/superevilicon.png",
    ),
}

    _godson_save_alignment_cache = { }
    GODSON_VISIBLE_SAVE_PAGES = 7


    def godson_alignment_from_values(values):
        """Returns one route key, following the priority used by the choice UI."""
        
        if values.get("supergood", False):
            return "supergood"
        elif values.get("superevil", False):
            return "superevil"
        elif values.get("evil", False):
            return "evil"
        elif values.get("sexaddict", False):
            return "sexaddict"
        elif values.get("good", False):
            return "good"
        
        return "neutral"


    def godson_current_alignment():
        current_store = renpy.store
        current_values = {
        "supergood": getattr(current_store, "supergood", False),
        "superevil": getattr(current_store, "superevil", False),
        "evil": getattr(current_store, "evil", False),
        "sexaddict": getattr(current_store, "sexaddict", False),
        "good": getattr(current_store, "good", False),
    }
        
        return godson_alignment_from_values(current_values)


    def godson_add_alignment_to_save(save_json):
        """Writes the active route into the metadata of every new save."""
        
        save_json["godson_alignment"] = godson_current_alignment()



    if not any(
    getattr(callback, "__name__", "") == "godson_add_alignment_to_save"
    for callback in config.save_json_callbacks
):
        config.save_json_callbacks.append(godson_add_alignment_to_save)


    def godson_full_slot_name(slot, page=None):
        """Resolves a visible slot number exactly as Ren'Py's file actions do."""
        
        if page is None:
            page = renpy.store.persistent._file_page
        
        try:
            page = int(page)
            page += (
            renpy.store.persistent._file_folder
            * renpy.config.file_pages_per_folder
        )
        except (TypeError, ValueError):
            pass
        
        if renpy.config.linear_saves_page_size is not None:
            try:
                return str(
                (int(page) - 1) * renpy.config.linear_saves_page_size
                + int(slot)
            )
            except (TypeError, ValueError):
                pass
        
        page = str(page)
        slot = str(slot)
        
        if renpy.config.file_slotname_callback is not None:
            return renpy.config.file_slotname_callback(page, slot)
        
        return page + "-" + slot


    def godson_saved_alignment(slot_name):
        """Returns the alignment stored in a slot, including pre-patch saves."""
        
        modified_time = renpy.slot_mtime(slot_name)
        if modified_time is None:
            return None
        
        cache_key = (slot_name, modified_time)
        if cache_key in _godson_save_alignment_cache:
            return _godson_save_alignment_cache[cache_key]
        
        alignment = None
        
        try:
            metadata = renpy.slot_json(slot_name) or { }
            alignment = metadata.get("godson_alignment", None)
        except Exception:
            alignment = None
        
        
        
        if alignment not in GODSON_SAVE_ALIGNMENT_VISUALS:
            try:
                save_values = renpy.get_save_data(slot_name) or { }
                alignment = godson_alignment_from_values(save_values)
            except Exception:
                alignment = "neutral"
        
        if len(_godson_save_alignment_cache) > 96:
            _godson_save_alignment_cache.clear()
        
        _godson_save_alignment_cache[cache_key] = alignment
        return alignment


    def godson_alignment_visuals(alignment):
        return GODSON_SAVE_ALIGNMENT_VISUALS.get(
        alignment,
        GODSON_SAVE_ALIGNMENT_VISUALS["neutral"],
    )


    def godson_current_manual_save_page():
        """Returns a usable numeric page while Auto or Quick Saves are open."""
        
        try:
            return max(1, int(renpy.store.persistent._file_page))
        except (TypeError, ValueError):
            return 1


    def godson_visible_save_pages():
        """Creates a sliding row of numbered pages with no upper limit."""
        
        current_page = godson_current_manual_save_page()
        half_window = GODSON_VISIBLE_SAVE_PAGES // 2
        first_page = max(1, current_page - half_window)
        
        return range(first_page, first_page + GODSON_VISIBLE_SAVE_PAGES)


transform -95 godson_save_alignment_glow:


    alpha 0.42
    ease 1.6 alpha 1.0
    ease 1.6 alpha 0.42
    repeat


init screen file_slots(title):

    default page_name_value = FilePageNameInputValue(
        pattern=_("Page {}"),
        auto=_("Automatic saves"),
        quick=_("Quick saves"),
    )

    use game_menu(title):

        fixed:

            order_reverse True

            button:
                style "page_label"
                key_events True
                xalign 0.5
                xoffset 64
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value

            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"
                xalign 0.5
                xoffset 64
                yalign 0.5
                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):
                    $ slot = i + 1
                    $ full_slot_name = godson_full_slot_name(slot)
                    $ slot_alignment = godson_saved_alignment(full_slot_name)

                    button:
                        action FileAction(slot)


                        at ui_button_motion
                        has fixed




                        fixed:
                            xsize 768
                            ysize 432
                            xpos 16
                            ypos 6
                            clipping True

                            add Solid("#080506"):
                                xsize 768
                                ysize 432

                            add FileScreenshot(slot):
                                xpos 14
                                ypos 14
                                xysize (740, 404)
                                fit "cover"

                            add "gui/christmas_noir/save_thumbnail_frame.png"

                        text FileTime(
                            slot,
                            format=_("{#file_time}%A, %B %d %Y, %H:%M"),
                            empty=_("empty slot"),
                        ):
                            style "slot_time_text"
                            xalign 0.5


                            ypos 468
                            text_align 0.5

                        text FileSaveName(slot):
                            style "slot_name_text"
                            xalign 0.5
                            ypos 500
                            text_align 0.5

                        if slot_alignment:
                            $ alignment_label, alignment_color, alignment_tint, alignment_edge, alignment_icon = godson_alignment_visuals(slot_alignment)
                            $ alignment_caption = alignment_label + " ALIGNMENT"
                            $ alignment_glow_image = "gui/aaa_main_menu/save_alignment_glow_" + slot_alignment + ".png"
                            $ alignment_pill_image = "gui/aaa_main_menu/save_alignment_pill_" + slot_alignment + ".png"

                            fixed:


                                xsize 540
                                ysize 130
                                xalign 0.5


                                ypos 478

                                add alignment_glow_image:
                                    xsize 540
                                    ysize 130
                                    xalign 0.5
                                    yalign 0.5
                                    at godson_save_alignment_glow

                                fixed:
                                    xsize 430
                                    ysize 58
                                    xalign 0.5
                                    yalign 0.5




                                    add alignment_pill_image

                                    hbox:
                                        xalign 0.5
                                        yalign 0.5
                                        spacing 14

                                        add alignment_icon:
                                            xysize (38, 38)
                                            fit "contain"
                                            yalign 0.5

                                        text alignment_caption:
                                            style "godson_save_alignment_text"
                                            color alignment_color
                                            outlines [(3, alignment_edge, 0, 0), (2, "#000000D9", 0, 1)]
                                            yalign 0.5

                        key "save_delete" action FileDelete(slot)

            vbox:
                xalign 0.5
                xoffset 64
                yalign 1.0
                yoffset -8
                spacing 10


                hbox:
                    xalign 0.5
                    spacing 8

                    textbutton "\u2039":
                        style "godson_pager_arrow_button"
                        action FilePagePrevious(auto=False, quick=False)
                        sensitive godson_current_manual_save_page() > 1
                        selected False
                        tooltip _("Previous save page")

                    for page in godson_visible_save_pages():
                        textbutton str(page):
                            style "godson_pager_page_button"
                            action FilePage(page)

                    textbutton "\u203A":
                        style "godson_pager_arrow_button"
                        action FilePageNext(auto=False, quick=False)
                        selected False
                        tooltip _("Next save page")


                hbox:
                    xalign 0.5
                    spacing 10

                    if config.has_autosave:
                        textbutton _("{#auto_page}AUTO SAVES"):
                            style "godson_pager_utility_button"
                            action FilePage("auto")
                            tooltip _("Automatic saves")

                    if config.has_quicksave:
                        textbutton _("{#quick_page}QUICK SAVES"):
                            style "godson_pager_utility_button"
                            action FilePage("quick")
                            tooltip _("Quick saves")

                    null width 26

                    text _("FAST JUMP"):
                        style "godson_pager_jump_label"
                        yalign 0.5

                    textbutton "-20":
                        style "godson_pager_jump_button"
                        action FilePage(max(1, godson_current_manual_save_page() - 20))
                        sensitive godson_current_manual_save_page() > 1
                        selected False
                        tooltip _("Jump back 20 save pages")

                    textbutton "-10":
                        style "godson_pager_jump_button"
                        action FilePage(max(1, godson_current_manual_save_page() - 10))
                        sensitive godson_current_manual_save_page() > 1
                        selected False
                        tooltip _("Jump back 10 save pages")

                    textbutton "+10":
                        style "godson_pager_jump_button"
                        action FilePage(godson_current_manual_save_page() + 10)
                        selected False
                        tooltip _("Jump forward 10 save pages")

                    textbutton "+20":
                        style "godson_pager_jump_button"
                        action FilePage(godson_current_manual_save_page() + 20)
                        selected False
                        tooltip _("Jump forward 20 save pages")


style godson_save_alignment_text is text:
    font "fonts/Louis George Cafe Bold.ttf"
    size 28
    kerning 2
    outlines [(2, "#000000D9", 0, 1)]
    text_align 0.5


style godson_pager_page_button is page_button:
    xminimum 94
    yminimum 60
    xpadding 16
    ypadding 6


style godson_pager_page_button_text is page_button_text:
    size 42
    text_align 0.5


style godson_pager_arrow_button is godson_pager_page_button:
    xminimum 78


style godson_pager_arrow_button_text is godson_pager_page_button_text:
    size 36


style godson_pager_utility_button is page_button:
    xminimum 210
    yminimum 50
    xpadding 22
    ypadding 5


style godson_pager_utility_button_text is page_button_text:
    size 30
    kerning 2
    text_align 0.5


style godson_pager_jump_button is page_button:
    xminimum 98
    yminimum 50
    xpadding 14
    ypadding 5


style godson_pager_jump_button_text is page_button_text:
    size 31
    text_align 0.5


style godson_pager_jump_label is text:
    font "fonts/Louis George Cafe Bold.ttf"
    size 25
    color "#D8B768"
    kerning 3
    outlines [(1, "#000000B8", 0, 1)]
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

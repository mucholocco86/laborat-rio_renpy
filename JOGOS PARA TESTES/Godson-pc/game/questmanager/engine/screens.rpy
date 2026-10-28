

default journal_left_page_adjustment = ui.adjustment()
default journal_right_page_adjustment = ui.adjustment()

screen button_open():
    zorder 1
    textbutton "Open diary" action Show("diary") style "open_diary_screen_btn"

screen diary():
    zorder diary_zorder
    modal True
    add "#0005"
    add "open_book" pos (1355, 740)

    default left_categories = collections.OrderedDict()
    default right_categories = collections.OrderedDict()

    for k, v in quest.quests_dict.items():
        for lpage in left_page:
            if k == lpage:
                $ left_categories[k] = v
            else:
                $ right_categories[k] = v

    fixed:
        pos (1448, 808)
        xysize (565, 680)

        use events_page(journal_left_page_adjustment, left_categories)
        vbar:
            xanchor 1.
            style "vscrollbar"
            unscrollable "hide"
            adjustment journal_left_page_adjustment

    fixed:
        pos (2103, 808)
        xysize (565, 680)

        use events_page(journal_right_page_adjustment, right_categories)
        vbar:
            xpos 1.
            style "vscrollbar"
            unscrollable "hide"
            adjustment journal_right_page_adjustment

    imagebutton:
        pos (2523+257, 1016+81)
        idle "book_close_idle"
        hover "book_close_hover"
        action Hide("diary")


screen events_page(adjustment, categories):
    viewport:
        draggable True
        mousewheel "change"
        yadjustment adjustment
        has vbox
        add Solid("#f00", ysize=0)
        for k, v in categories.items():
            if k:
                null height 25
                add "journal_divider" xalign .5
                null height 15
            use evs_block(k, v)


screen evs_block(cat, evlist, prefix=" {b}-{/b} ", completed_suffix="{image=completed}", progress_suffix="{image=in_progress}", unknown=_("? ? ?")):
    text "~ "+__(cat)+" ~":
        style "category_style"
    null height 20
    for k,v in evlist.items():
        text prefix+(__(v.title) if v.state != "pending" else __(unknown))+(completed_suffix if v.state == "completed" else (progress_suffix if v.state == "in progress" else "")):
            size 25 and 35

            if v.state == "pending":
                style "quest_pending_style"

            if v.state == "unlocked":
                style "quest_unlocked_style"

            if v.state == "in progress":
                style "quest_in_progress_style"

            if v.state == "completed":
                style "quest_completed_style"

            if v.state == "done":
                style "quest_done_style"

            if v.state == "failed":
                style "quest_failed_style"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

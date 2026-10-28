



init -1:



    define diary_zorder = 0


    define diary_modal = False




    define left_page = {_("General"),}





image open_book = "questmanager/assets/open_book.png"
image book_close_idle = "questmanager/assets/book_close_idle.png"
image book_close_hover = "questmanager/assets/book_close_hover.png"
image completed = "questmanager/assets/completed.png"
image in_progress = "questmanager/assets/in_progress.png"
image journal_divider = "questmanager/assets/journal_divider.png"







style category_style is text:
    xalign 0.5
    color "#63050e"
    font "questmanager/assets/PermanentMarker-Regular.ttf"
    size 45
    bold False
    italic False
    strikethrough False





style quest_pending_style is text:
    color "#172993"
    font "fonts/VioletSans-Regular.otf"
    size 35
    bold False
    italic False
    strikethrough False


style quest_unlocked_style is text:
    color "#172993"
    font "fonts/VioletSans-Regular.otf"
    size 35
    bold False
    italic False
    strikethrough False


style quest_in_progress_style is text:
    color "#172993"
    font "fonts/VioletSans-Regular.otf"
    size 35
    bold False
    italic False
    strikethrough False


style quest_completed_style is text:
    yalign .5
    color "#172993"
    font "fonts/VioletSans-Regular.otf"
    size 35
    bold False
    italic True
    strikethrough False


style quest_done_style is text:
    color "#172993"
    font "fonts/VioletSans-Regular.otf"
    size 35
    bold False
    italic False
    strikethrough True


style quest_failed_style is text:
    color "#e12345"
    font "fonts/VioletSans-Regular.otf"
    size 35
    bold False
    italic False
    strikethrough True




style open_diary_screen_btn is button:


    xysize (120,55)

style open_diary_screen_btn is text:
    size 35
    xalign .5
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

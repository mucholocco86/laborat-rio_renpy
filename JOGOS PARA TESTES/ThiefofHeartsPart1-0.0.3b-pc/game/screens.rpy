init offset = -1










style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)





















screen say(who, what):
    style_prefix "say"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"




    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0

init:

    style multiple2_say_window:
        xsize 500
        background None

    style block1_multiple2_say_window:
        xalign 0.3

    style block2_multiple2_say_window:
        xalign 0.7



    style multiple3_say_window:
        xsize 500
        background None

    style block1_multiple3_say_window:
        xalign 0.0

    style block2_multiple3_say_window:
        xalign 0.4

    style block3_multiple3_say_window:
        xalign 0.8


init python:



    def flash(out_time, hold_time, in_time, color_in):
        return Fade(out_time, hold_time, in_time, color=color_in)
















init python:
    config.character_id_prefixes.append('namebox')

style window is default



style say_label is text_label_style
style say_dialogue is text_dialogue_style
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height


style window_no_textbox:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height


style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos



style text_dialogue_style:
    color "#FFFFFF"
    outlines [(2, "#000000", 1, 1)]

style text_label_style:
    outlines [(4, "#000000", 1, 1)]










screen input(prompt):
    style_prefix "input"

    window:

        has vbox:
            xanchor gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

        text prompt style "input_prompt"
        input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width










screen choice(items):
    if v_choice_type == "main":
        window:
            area (400, 100, 1200, 700)
            has viewport:
                if len(items) >= 6:
                    scrollbars "vertical"
                    mousewheel True
                    draggable True

                style_prefix "choice"

            vbox:
                spacing 20
                for i in items:
                    textbutton ("%s {color=#33ff33}(%s){/color}" % (i.caption, i.kwargs["wt"]) if persistent.v_walkthrough_enabled and i.kwargs.get('wt') else i.caption) action i.action
    else:
        style_prefix "choice"

        vbox:
            for i in items:
                textbutton ("%s {color=#33ff33}(%s){/color}" % (i.caption, i.kwargs["wt"]) if persistent.v_walkthrough_enabled and i.kwargs.get('wt') else i.caption) action i.action


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 405
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")







screen quick_menu():


    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.01
            yalign 1.0

            textbutton _("Back") action Rollback()
            textbutton _("History") action ShowMenu('history')
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Save") action ShowMenu('save')
            textbutton _("Q.Save") action QuickSave()
            textbutton _("Q.Load") action QuickLoad()
            textbutton _("Prefs") action ShowMenu('preferences')




init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.button_text_properties("quick_button")











style main_menu_style is button:
    xalign 0.5

style special_menu_style is button:
    xalign 0.5

style main_menu_style_text is text:
    outlines [ (2, "#000000", 0, 0) ]
    hover_color '#c94444'
    font "fonts/Righteous.ttf"

style special_menu_style_text is text:
    outlines [ (2, "#000000", 0, 0) ]
    color '#FCB74E'
    hover_color '#9a480d'
    font "fonts/Righteous.ttf"

screen navigation():
    if renpy.get_screen("main_menu"):

        if mm_show:
            add "logo_main_menu_small_part1" xalign 0.5 yalign 0.87

            hbox:
                style_prefix "navigation"
                xalign 0.5

                yalign 0.95

                spacing gui.navigation_spacing

                if main_menu:

                    textbutton _("Start") action Start() style "main_menu_style"

                else:

                    textbutton _("Save") action ShowMenu("save") style "main_menu_style"

                textbutton _("Load") action ShowMenu("load") style "main_menu_style"

                if _in_replay:

                    textbutton _("End Replay") action EndReplay(confirm=True) style "main_menu_style"

                elif not main_menu:

                    textbutton _("Main Menu") action MainMenu() style "main_menu_style"

                textbutton _("Settings") action ShowMenu("preferences") style "main_menu_style"

                textbutton _("Game Tablet") action ShowMenu('scr_mm_main') style "main_menu_style"

                textbutton _("About") action ShowMenu("TOH_About") style "main_menu_style"

                if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):


                    textbutton _("Help") action ShowMenu("help") style "main_menu_style"

                textbutton _("Support Our Work") action ShowMenu("toh_support") style "special_menu_style"

                if renpy.variant("pc"):



                    textbutton _("Quit") action Quit(confirm=not main_menu) style "main_menu_style"

            imagebutton idle "gui/logos/btn_ss_logo_idle.png" hover "gui/logos/btn_ss_logo_hover.png" xalign 0.99 yalign 0.95 action OpenURL(url="https://subscribestar.adult/mrdotsgames")

            imagebutton idle "gui/logos/btn_patreon_logo_idle.png" hover "gui/logos/btn_patreon_logo_hover.png" xalign 0.99 yalign 0.86 action OpenURL(url="https://patreon.com/mrdotsgames")

            imagebutton idle "gui/logos/btn_discord_idle.png" hover "gui/logos/btn_discord_hover.png" xalign 0.99 yalign 0.77 action OpenURL(url="https://discord.gg/JbyH5HUnBh")
            if not renpy.variant("small"):
                textbutton "{size=20}v[config.version] (Changelog)" xalign 0.99 yalign 0.99 style "main_menu_style" action ShowMenu("toh_changelog")
            else:
                textbutton "{size=30}v[config.version] (Changelog)" xalign 0.99 yalign 0.99 style "main_menu_style" action ShowMenu("toh_changelog")


            if mm_movie_active == True:
                imagebutton idle "gui/menu_buttons/btn_mm_movie_idle.png" hover "gui/menu_buttons/btn_mm_movie_hover.png" xalign 0.01 yalign 0.98 action SetVariable("mm_movie_active",False)
            else:
                imagebutton idle "gui/menu_buttons/btn_mm_slideshow_idle.png" hover "gui/menu_buttons/btn_mm_slideshow_hover.png" xalign 0.01 yalign 0.98 action SetVariable("mm_movie_active",True)

            if mm_show == True:
                imagebutton idle "gui/menu_buttons/btn_mm_hide_idle.png" hover "gui/menu_buttons/btn_mm_hide_hover.png" xalign 0.05 yalign 0.98 action SetVariable("mm_show",False)
            else:
                imagebutton idle "gui/menu_buttons/btn_mm_hide_hover.png" xalign 0.05 yalign 0.98 action SetVariable("mm_show",True)
        else:

            if mm_movie_active == True:
                imagebutton idle "gui/menu_buttons/btn_mm_movie_idle.png" hover "gui/menu_buttons/btn_mm_movie_hover.png" xalign 0.01 yalign 0.98 action SetVariable("mm_movie_active",False)
            else:
                imagebutton idle "gui/menu_buttons/btn_mm_slideshow_idle.png" hover "gui/menu_buttons/btn_mm_slideshow_hover.png" xalign 0.01 yalign 0.98 action SetVariable("mm_movie_active",True)


            if mm_show == True:
                imagebutton idle "gui/menu_buttons/btn_mm_hide_idle.png" hover "gui/menu_buttons/btn_mm_hide_hover.png" xalign 0.05 yalign 0.98 action SetVariable("mm_show",False)
            else:
                imagebutton idle "gui/menu_buttons/btn_mm_hide_hover.png" xalign 0.05 yalign 0.98 action SetVariable("mm_show",True)



    else:

        vbox:
            style_prefix "hnavigation"
            xpos gui.navigation_xpos
            yalign 0.5
            spacing gui.navigation_spacing

            if main_menu:

                textbutton _("Start") action Start()

            else:

                textbutton _("Save") action ShowMenu("save")

            textbutton _("Load") action ShowMenu("load")

            if _in_replay:

                textbutton _("End Replay") action EndReplay(confirm=True)

            elif not main_menu:

                textbutton _("Main Menu") action MainMenu()

            textbutton _("Settings") action [ShowMenu("preferences")]

            if not main_menu:

                textbutton _("Game Tablet") action ShowMenu('scr_mm_main')

            textbutton _("About") action ShowMenu("TOH_About")

            textbutton _("Support Our Work") action ShowMenu("toh_support") style "special_menu_style"

            if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):


                textbutton _("Help") action ShowMenu("help")

            if renpy.variant("pc"):



                textbutton _("Quit") action Quit(confirm=not main_menu)

style navigation_button is gui_button
style navigation_button_text is gui_button_text

style hnavigation_button is gui_button
style hnavigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")
    xalign 0.5

style hnavigation_button_text:
    xalign 0.5

style hnavigation_button_text:
    xalign 0.5







init:
    $ persistent.v_mm_sound_alternative = False

screen main_menu():
    tag menu



    if mm_movie_active:
        if persistent.mm_video == "default":
            add Movie(size=(1920, 1080), channel="movie_mm", play="gui/videos/toh_slideshow_2.webm")
        else:
            add Movie(size=(1920, 1080), channel="movie_mm", play="gui/videos/toh_slideshow_1.webm")


    else:
        add gui.main_menu_background


    frame:
        style "main_menu_frame"



    use navigation

    if gui.show_name:

        vbox:
            style "main_menu_vbox"

            text "[config.name!t]":
                style "main_menu_title"

            text "[config.version]":
                style "main_menu_version"


style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 420
    yfill True



style main_menu_vbox:
    xalign 1.0
    xoffset -30
    xmaximum 1200
    yalign 1.0
    yoffset -30

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)
    font "DejaVuSans.ttf"

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")











screen game_menu(title, scroll, yinitial=0.0):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        has hbox


        frame:
            style "game_menu_navigation_frame"

        frame:
            style "game_menu_content_frame"

            if scroll == "viewport":

                viewport:
                    yinitial yinitial
                    scrollbars "vertical"
                    mousewheel True
                    draggable True
                    pagekeys True

                    side_yfill True

                    has vbox
                    transclude

            elif scroll == "vpgrid":

                vpgrid:
                    cols 1
                    yinitial yinitial

                    scrollbars "vertical"
                    mousewheel True
                    draggable True
                    pagekeys True

                    side_yfill True

                    transclude

            else:

                transclude

    use navigation

    textbutton _("Return"):
        style "return_button"

        action Return()

    text title xalign 0.5 yalign 0.05 size 50

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 45
    top_padding 180

    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 420
    yfill True

style game_menu_content_frame:
    left_margin 60
    right_margin 30
    top_margin 15

style game_menu_viewport:
    xsize 1380

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 15

style game_menu_label:
    xpos 75
    ysize 180

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -45









screen about():
    tag menu





    use game_menu(_("About"), scroll="viewport"):

        text _("MrDotsGames was founded in September 2016.")
        text _("")
        text _("So far we have released and completed three games - DMD, Melody and Sunshine Love.")
        text _("")
        text _("Our mission is to create classic Adult Visual Novels that you want to play again and again for many years to come.")
        text _("")
        text _("We strive to always deliver quality updates and to continually evolve as developers.")
        text _("")
        text _("Our team consists of:")
        text _("")
        text _("MrDots (Creator, Coding, Rendering, Beta Testing)")
        text _("")
        text _("HearszAM (Chief Scene Writer, Coding, Beta Testing, Promotions)")
        text _("")
        text _("Mistress Elemental (Rendering, Coding, Beta Testing)")
        text _("")
        text _("HyperServer (Ideas, Writing, Coding, Character Development, Beta Testing)")
        text _("")
        text _("Kasami (Rendering)")
        text _("")
        text _("To learn more about our journey so far, please check out our promotional video for MrDotsGames:")
        text _("{a=https://www.youtube.com/watch?v=7cuCxasLzwc&t=3s&ab_channel=MrDotsGames}https://www.youtube.com/watch?v=7cuCxasLzwc&t=3s&ab_channel=MrDotsGames{/a}")


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size










init python:
    class UserSaveName(FileSave):
        def __init__(self, name, confirm=True, newest=True, page=None, cycle=False):
            super(UserSaveName, self).__init__(name=name, confirm=confirm, newest=newest, page=page, cycle=cycle)
        
        def __call__(self):
            renpy.call_in_new_context("get_save_name")
            return super(UserSaveName, self).__call__()

label get_save_name:
    show screen save
    if persistent.enable_save_name:
        $ save_name = renpy.call_screen("modal_input", prompt="Enter a description for your save file (Hit ESC to save without one):", default="(None)", length=10)
    $ renpy.retain_after_load()
    return

screen modal_input:
    modal True
    add "bg/bg black.png" alpha 0.9


    vbox:

        text prompt style "input_prompt"
        input id "input" style "input_text" length 40 allow "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ 0123456789 -/*"
        xalign 0.5
        yalign 0.05

screen save():
    add "gui/TOH_screens/load_save/toh_load_save_bg.jpg"
    add "bg/bg black.png" alpha 0.8
    tag menu

    use file_slots(_("Save"))


screen load():
    add "gui/TOH_screens/load_save/toh_load_save_bg.jpg"
    add "bg/bg black.png" alpha 0.8
    tag menu

    use file_slots(_("Load"))


screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))

    use game_menu(title, scroll="viewport"):

        fixed:



            order_reverse True


            button:
                style "page_label"

                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value


            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):
                    $ slot = i + 1
                    button:
                        action If(title.lower() == "save", true=UserSaveName(slot), false=FileAction(slot))

                        vbox:
                            add FileScreenshot(slot) xalign 0.5

                            text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                                style "slot_time_text"
                            text FileSaveName(slot):
                                style "slot_name_text" color "#f4eb42"
                        if FileLoadable(slot):
                            imagebutton:
                                idle "gui/delete_save_idle.png"
                                hover "gui/delete_save_hover.png"

                                action FileDelete(slot)
                                xalign 0.98
                                yalign 0.02


            vbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                hbox:
                    xalign 0.5

                    spacing gui.page_spacing

                    textbutton _("<") action FilePagePrevious()

                    if config.has_autosave:
                        textbutton _("{#auto_page}A") action FilePage("auto")

                    if config.has_quicksave:
                        textbutton _("{#quick_page}Q") action FilePage("quick")


                    for page in range(1, 10):
                        textbutton "[page]" action FilePage(page)
                    if (not FileCurrentPage() == "auto" and "quick") and FileCurrentPage().isnumeric():
                        if int(FileCurrentPage()) >= 10:
                            textbutton "..." action NullAction()
                            textbutton FileCurrentPage() action NullAction()
                    textbutton _(">") action FilePageNext()

                if config.has_sync:
                    if CurrentScreenName() == "save":
                        textbutton _("Upload Sync"):
                            action UploadSync()
                            xalign 0.5
                    else:
                        textbutton _("Download Sync"):
                            action DownloadSync()
                            xalign 0.5


style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 75
    ypadding 5

style page_label_text:
    textalign 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.button_text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.button_text_properties("slot_button")









style word_list is button:
    background "#FFFF00"

style word_list_text is text:
    size 45
    hover_color "#FF00FF"
    outlines [ (0, "#0000FF", 1, 1) ]
    color "#FF0000"

style disable_button is button

style disable_button_text is button_text:
    color "#11111150"

init -1:
    $ v_pref_tab = 0

screen preferences():
    $ tooltip = GetTooltip()
    tag menu

    use game_menu(_("Settings"), scroll="viewport"):
        vbox:
            hbox:
                xpos 0.1
                xfill True
                textbutton "GAME" action SetVariable("v_pref_tab", 0)
                textbutton "AUDIO" action SetVariable("v_pref_tab", 1)

            add "gui/TOH_screens/settings/separator.png" alpha 0.2 xalign 0.4

        if v_pref_tab == 0:
            vbox:



                ypos 0.1
                if renpy.variant("pc"):
                    hbox:
                        button:
                            text _("Display")
                            xsize 500
                        style_prefix "radio"
                        textbutton _("Window") action Preference("display", "window") tooltip "Set game window to windowed mode."
                        textbutton _("/")
                        textbutton _("Fullscreen") action Preference("display", "fullscreen") tooltip "Set game window to fullscreen mode."

                    add "gui/TOH_screens/settings/separator.png" alpha 0.2

                hbox:
                    style_prefix "check"
                    button:
                        text _("Custom Save Names")
                        xsize 500
                    textbutton _("Enabled") action SetField(persistent, "enable_save_name", True) tooltip "Custom names can be used for saves."
                    textbutton _("/")
                    textbutton _("Disable") action SetField(persistent, "enable_save_name", False) tooltip "A basic timestamp for saves will be used."

                add "gui/TOH_screens/settings/separator.png" alpha 0.2

                hbox:
                    style_prefix "radio"
                    button:
                        text _("Rollback Side")
                        xsize 500
                    textbutton _("Disable") action Preference("rollback side", "disable") tooltip "Rollback will be disabled."
                    textbutton _("/")
                    textbutton _("Left") action Preference("rollback side", "left") tooltip "Touches or clicks to the left side of the window will cause the dialogue to roll back."
                    textbutton _("/")
                    textbutton _("Right") action Preference("rollback side", "right") tooltip "Touches or clicks to the right side of the window will cause the dialogue to roll back."

                add "gui/TOH_screens/settings/separator.png" alpha 0.2


                hbox:
                    style_prefix "check"
                    button:
                        text _("Skip Dialogue")
                        xsize 500
                    textbutton _("Unseen Dialogue") action Preference("skip", "toggle") tooltip "When skipping dialogue, dialogue that you have not seen will be skipped."
                    textbutton _("/")
                    textbutton _("After Choices") action Preference("after choices", "toggle") tooltip "When skipping dialogue, dialogue after a choice is made will be skipped."
                    textbutton _("/")
                    textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle")) tooltip "When skipping dialogue, transistions like dissolve and fade will be skipped also."
                add "gui/TOH_screens/settings/separator.png" alpha 0.2
                add "gui/TOH_screens/settings/separator.png" alpha 0.2

                hbox:
                    style_prefix "check"
                    button:
                        text _("Dialogue Box")
                        xsize 500
                    textbutton _("Enabled") action SetField(persistent, "v_textbox_dialogue", True) tooltip "Enable the dialogue textbox."
                    textbutton _("/")
                    textbutton _("Disable") action SetField(persistent, "v_textbox_dialogue", False) tooltip "Disable the dialogue textbox."









                add "gui/TOH_screens/settings/separator.png" alpha 0.2

                hbox:
                    style_prefix "radio"
                    button:
                        text _("Dialogue Text Position")
                        xsize 500
                    textbutton _("Left") action [gui.SetPreference("dialogue_xpos", 0.195), gui.SetPreference("dialogue_text_xalign",0.0)] tooltip "Align the dialogue text to the left side of the dialogue box."
                    textbutton _("/")
                    textbutton _("Center") action [gui.SetPreference("dialogue_xpos", 0.5), gui.SetPreference("dialogue_text_xalign",0.5)] tooltip "Align the dialogue text to the center of the dialogue box."
                    textbutton _("/")
                    textbutton _("Right") action [gui.SetPreference("dialogue_xpos", 0.805), gui.SetPreference("dialogue_text_xalign",1.0)] tooltip "Align the dialogue text to the right side of the dialogue box."

                add "gui/TOH_screens/settings/separator.png" alpha 0.2

                hbox:
                    style_prefix "check"
                    button:
                        text _("Dialogue Text Speed")
                        tooltip ""
                        xsize 350
                    hbox:
                        xpos 200
                        bar value Preference("text speed"):
                            style "my_bar"
                            xysize (300,30)
                            ypos 10
                            tooltip "The speed at which the dialoge will be fully displayed on screen."
                add "gui/TOH_screens/settings/separator.png" alpha 0.2

                hbox:
                    style_prefix "check"
                    button:
                        text _("Auto-Forward Time")
                        xsize 350
                    hbox:
                        xpos 200
                        bar value Preference("auto-forward time"):
                            style "my_bar"
                            xysize (300,30)
                            ypos 10
                            tooltip "When \"Auto\" is enabled in the dialogue, this is the speed to which the text will advance to the next line."
                add "gui/TOH_screens/settings/separator.png" alpha 0.2

                hbox:
                    style_prefix "radio"
                    button:
                        text _("Speaker's Name Position")
                        xsize 500
                    textbutton _("Left") action gui.SetPreference("name_xpos", 0.25) tooltip "The speaker's name will appear to the left of the dialoge window."
                    textbutton _("/")
                    textbutton _("Center") action gui.SetPreference("name_xpos", 0.5) tooltip "The speaker's name will appear in the center of the dialoge window."
                    textbutton _("/")
                    textbutton _("Right") action gui.SetPreference("name_xpos", 0.75) tooltip "The speaker's name will appear to the right of the dialoge window."

                add "gui/TOH_screens/settings/separator.png" alpha 0.2

                if renpy.variant("pc"):
                    hbox:
                        style_prefix "radio"
                        button:
                            text _("UI Text Size")
                            xsize 500
                        textbutton _("Normal") action [gui.SetPreference("text_size", 33), gui.SetPreference ("name_text_size", 45) , gui.SetPreference ("interface_text_size", 33), gui.SetPreference ("label_text_size", 36), gui.SetPreference ("slot_button_text_size", 24)] tooltip "Set the game's text to the normal/default size."
                        textbutton _("/")
                        textbutton _("Big") action [gui.SetPreference("text_size", 38), gui.SetPreference ("name_text_size", 50), gui.SetPreference ("interface_text_size", 38), gui.SetPreference ("label_text_size", 41), gui.SetPreference ("slot_button_text_size", 28)] tooltip "Set the game's text to a slightly bigger size."
                        textbutton _("/")
                        textbutton _("Bigger!") action [gui.SetPreference("text_size", 43), gui.SetPreference ("name_text_size", 55), gui.SetPreference ("interface_text_size", 43), gui.SetPreference ("label_text_size", 46), gui.SetPreference ("slot_button_text_size", 34)] tooltip "Set the game's text to a much bigger size."

                    add "gui/TOH_screens/settings/separator.png" alpha 0.2

                hbox:
                    style_prefix "radio"
                    button:
                        text _("Font Style")
                        xsize 500
                    textbutton _("Righteous") action gui.SetPreference("font", "fonts/Righteous.ttf") tooltip "Set the game's font to Righteous."
                    textbutton _("/")
                    textbutton _("Georgia") action gui.SetPreference("font", "fonts/georgia.ttf") tooltip "Set the game's font to Georgia."
                    textbutton _("/")
                    textbutton _("OpenSans") action gui.SetPreference("font", "fonts/OpenSans-Regular.ttf") tooltip "Set the game's font to OpenSans Regular."

                add "gui/TOH_screens/settings/separator.png" alpha 0.2

                hbox:
                    style_prefix "radio"
                    button:
                        text _("Main Menu Video")
                        xsize 500
                    textbutton _("Default") action SetField(persistent, "mm_video", "default") tooltip "Change the main menu video to the default track."
                    textbutton _("/")
                    textbutton _("Alternative") action SetField(persistent, "mm_video", "alternative") tooltip "Change the main menu video to the alternative track."


        if v_pref_tab == 1:

            vbox:
                ypos 0.1

                xmaximum 500
                hbox:
                    if config.has_music:
                        style_prefix "check"
                        button:
                            text _("Music Volume")
                            xsize 500
                        hbox:
                            xpos 200
                            bar value Preference("music volume"):
                                style "my_bar"
                                xysize (300,30)
                                ypos 5
                                tooltip "Adjusting the game's music volume. Also effects some scenes where music is played."
                add "gui/TOH_screens/settings/separator.png" alpha 0.2

                hbox:
                    if config.has_sound:
                        style_prefix "check"
                        button:
                            text _("Sound Effects Volume")
                            xsize 500
                        hbox:
                            xpos 200
                            bar value Preference("sound volume"):
                                style "my_bar"
                                xysize (300,30)
                                ypos 5
                                tooltip "Adjusting the game's sound effects volume. Sound effects, videos and other audio except music and sex sounds."
                add "gui/TOH_screens/settings/separator.png" alpha 0.2

                hbox:
                    if config.has_sound:
                        style_prefix "check"
                        button:
                            text _("Sex Effects Volume")
                            xsize 500
                        hbox:
                            xpos 200
                            bar value MixerValue('sex'):
                                style "my_bar"
                                xysize (300,30)
                                ypos 5
                                tooltip "Adjusting the game's sex effects volume. Only effects the sex sounds played."
                add "gui/TOH_screens/settings/separator.png" alpha 0.2
                add "gui/TOH_screens/settings/separator.png" alpha 0.2

                hbox:
                    if config.has_sound:
                        style_prefix "check"
                        button:
                            text _("Mute Audio When Game's Not In Focus")
                            xsize 500
                        textbutton _("Enabled") action Preference("audio when unfocused", "disable") tooltip "When Enabled, the game's sound will be muted when minimized or not the primary window that's in focus."
                        textbutton _("/")
                        textbutton _("Disable") action Preference("audio when unfocused", "enable") tooltip "When Disabled, the game's sound will contunie to play when minimized or not the primary window that's in focus."
                add "gui/TOH_screens/settings/separator.png" alpha 0.2

                hbox:
                    if config.has_sound:
                        style_prefix "check"
                        button:
                            text _("Mute All")
                            xsize 500
                        hbox:
                            xpos 200
                            textbutton _("Mute") action Preference("all mute", "toggle") tooltip "Mute/Unmute all game sounds."
                add "gui/TOH_screens/settings/separator.png" alpha 0.2

                hbox:
                    style_prefix "check"
                    button:
                        text _("Show Text Descriptions of Sound Effects")
                        xsize 500
                    textbutton _("Enabled") action SetField(persistent, "v_sounds_text_on", True) tooltip "Text for many sound effects will be displayed. Example \"Knock, knock, knock.\" lines would be seen."
                    textbutton _("/")
                    textbutton _("Disable") action SetField(persistent, "v_sounds_text_on", False) tooltip "Text for many sound effects will not be displayed. Example \"Knock, knock, knock.\" lines would not be seen."
                add "gui/TOH_screens/settings/separator.png" alpha 0.2

                hbox:
                    style_prefix "check"
                    button:
                        text _("Main Menu Music")
                        xsize 500
                    textbutton _("Default") action [SetField(persistent, "mm_music", "default"),Play("music", "gui/main_menu_music.ogg")] tooltip "Change the main menu music to the default track."
                    textbutton _("/")
                    textbutton _("Alternative") action [SetField(persistent, "mm_music", "alternative"),Play("music", "gui/main_menu_music_alt.ogg")] tooltip "Change the main menu music to the alternative track."
                add "gui/TOH_screens/settings/separator.png" alpha 0.2



        if v_pref_tab == 2:
            if renpy.variant("pc"):
                vpgrid:

                    area (0, 0, 1380, 780)
                    cols 2
                    rows 3
                    spacing 5
                    draggable True
                    mousewheel True


                    vbox:
                        yalign 0.0
                        hbox:
                            vbox:
                                label _("Enable Secret Scenes")
                                style_prefix "radio"
                                if persistent.v_secrets_locked:
                                    textbutton _("Unlock Feature") action Show('unlock_code', what='secrets', password='opening', tier='$10') tooltip "Unlocks an icon in the corner of the game when the current scene has an unfound secret available."
                                else:
                                    textbutton _("Enabled") action SetField(persistent,"v_secrets_enabled", True) tooltip "Secret scenes will be enabled and will play when they have been discovered."
                                    textbutton _("Disabled (Default)") action [SetField(persistent,"v_secrets_enabled", False),Jump("reset_both_secret_values")] tooltip "Secret locations and scenes will not be available."
                        text _("")

                        if persistent.v_secrets_enabled:
                            hbox:
                                vbox:
                                    label _("Secrets Icon Visible")
                                    style_prefix "radio"
                                    textbutton _("Enabled") action SetField(persistent,"v_secrets_icon_enabled", True) tooltip "Show the icon in the corner of the game when the current scene has an unfound secret available."
                                    textbutton _("Disabled (Default)") action [SetField(persistent,"v_secrets_icon_enabled", False),Jump("reset_reappear_secret_value")] tooltip "Disable the secret icon."
                            text _("")

                        if persistent.v_secrets_icon_enabled:
                            hbox:
                                vbox:
                                    label _("Secrets Icon Reappearing")
                                    style_prefix "radio"
                                    textbutton _("Enabled") action SetField (persistent,"v_secrets_reappear", True) tooltip "Shows the secrets icon a scenes where the secret has already been discovered."
                                    textbutton _("Disabled (Default)") action SetField (persistent,"v_secrets_reappear", False) tooltip "The secrets icon will remain hidden in scenes the secret has already been discovered."
                            text _("")
                    vbox:

                        hbox:
                            vbox:
                                label _("Customize Names and Relationships")
                                style_prefix "radio"
                                if (v_allow_redefine):
                                    textbutton _("Redefine Now") action ShowMenu("set_rel") tooltip "Bring up the menu to change character names and their relationships."
                                else:
                                    style "disable_button"
                                    textbutton _("Unlocks after being defined ingame")
                        text _("")
                        hbox:
                            vbox:
                                label _("In-Game Walkthrough")
                                style_prefix "radio"
                                if persistent.v_walkthrough_locked:
                                    textbutton _("Unlock Feature") action Show('unlock_code', what='walkthrough', password='rebound', tier='$15') tooltip "Unlock the in game walkthrough for all choices to find the best outcome for your playthrough."
                                else:
                                    textbutton _("Enabled (Default)") action SetField (persistent,"v_walkthrough_enabled", True) tooltip "Enable the in-game walktrough."
                                    textbutton _("Disabled") action SetField (persistent,"v_walkthrough_enabled", False) tooltip "Disable the in-game walktrough."
                        text _("")
                        hbox:
                            for filename, prefname, varname, defaultvalue in extra_prefs:
                                if renpy.loadable(filename):
                                    vbox:
                                        label prefname
                                        style_prefix "radio"
                                        textbutton (_("Enabled (Default)") if defaultvalue else _("Enabled")) action SetField (persistent, varname, True)
                                        textbutton (_("Disabled") if defaultvalue else _("Disabled (Default)")) action SetField (persistent, varname, False)
            else:
                vpgrid:

                    area (0, 0, 1380, 780)
                    cols 2
                    rows 3
                    spacing 5
                    draggable True
                    mousewheel True
































                    vbox:

                        hbox:
                            vbox:
                                label _("Customize Names and Relationships")
                                style_prefix "radio"
                                if (v_allow_redefine):
                                    textbutton _("Redefine Now") action ShowMenu("set_rel") tooltip "Bring up the menu to change character names and their relationships."
                                else:
                                    style "disable_button"
                                    textbutton _("Unlocks after being defined ingame")
                        text _("")
                        hbox:
                            vbox:
                                label _("In-Game Walkthrough")
                                style_prefix "radio"
                                if persistent.v_walkthrough_locked:
                                    textbutton _("Unlock Feature") action Show('unlock_code', what='walkthrough', password='rebound', tier='$15') tooltip "Unlock the in game walkthrough for all choices to find the best outcome for your playthrough."
                                else:
                                    textbutton _("Enabled (Default)") action SetField (persistent,"v_walkthrough_enabled", True) tooltip "Enable the in-game walktrough."
                                    textbutton _("Disabled") action SetField (persistent,"v_walkthrough_enabled", False) tooltip "Disable the in-game walktrough."
                        text _("")
                        hbox:
                            for filename, prefname, varname, defaultvalue in extra_prefs:
                                if renpy.loadable(filename):
                                    vbox:
                                        label prefname
                                        style_prefix "radio"
                                        textbutton (_("Enabled (Default)") if defaultvalue else _("Enabled")) action SetField (persistent, varname, True)
                                        textbutton (_("Disabled") if defaultvalue else _("Disabled (Default)")) action SetField (persistent, varname, False)

    if tooltip:
        text "[tooltip]" xalign 0.75 yalign 1.0





















style set_rel_text_button is button:
    color "#dec06e"
    hover_color "#d2793d"
    size 20
    ypos -8

style set_rel_text:
    color "#ffffff"
    size 32


screen set_rel():
    key "K_ESCAPE" action Hide("set_rel")
    modal True
    imagebutton idle "bg_changelog" action NullAction()
    add Solid("#000000") alpha 0.7
    text "{size=60}Redefine Relationships{/size}" xalign 0.5 yalign 0.02 outlines [ (3, "#000000", 0, 0) ]
    viewport:

        xysize (1300, 750)
        xalign 0.5
        yalign 0.5
        has viewport:
            style_prefix "rel"
            scrollbars "vertical"
            mousewheel True
            draggable True
            xalign 0.5
            yalign 0.0

        vbox:
            hbox:
                text _("Your name is") style "char_info_title"
                textbutton _("[y_name]") action Show('rename', var_name_to_change='y_name') text_style "char_info_button"
                textbutton _("[y_lastname]") action Show('rename', var_name_to_change='y_lastname') text_style "char_info_button"
                text _("and you live with following people:") style "char_info_title"
            text _("")
            hbox:
                text _("- Your younger") style "char_info_title"
                textbutton _("[a_mc_rel]") action Show('rename', var_name_to_change='a_mc_rel') text_style "char_info_button"
                textbutton _("[a_name]") action Show('rename', var_name_to_change='a_name') text_style "char_info_button"
                text _("- she calls you her") style "char_info_title"
                textbutton _("[a_mc_address]") action Show('rename', var_name_to_change='a_mc_address') text_style "char_info_button"
                text _("for short.") style "char_info_title"
            hbox:
                text _("   (So you're her older") style "char_info_title"
                textbutton _("[mc_a_rel]") action Show('rename', var_name_to_change='mc_a_rel') text_style "char_info_button"
                text _(", and you call her your") style "char_info_title"
                textbutton _("[mc_a_address]") action Show('rename', var_name_to_change='mc_a_address') text_style "char_info_button"
                text _(".)") style "char_info_title"
            text _("")
            hbox:
                text _("- Your older") style "char_info_title"
                textbutton _("[b_mc_rel]") action Show('rename', var_name_to_change='b_mc_rel') text_style "char_info_button"
                textbutton _("[b_name]") action Show('rename', var_name_to_change='b_name') text_style "char_info_button"
                text _("- she calls you her") style "char_info_title"
                textbutton _("[b_mc_address]") action Show('rename', var_name_to_change='b_mc_address') text_style "char_info_button"
                text _("for short.") style "char_info_title"
            hbox:
                text _("   (So you're her younger") style "char_info_title"
                textbutton _("[mc_b_rel]") action Show('rename', var_name_to_change='mc_b_rel') text_style "char_info_button"
                text _(", and you call her your") style "char_info_title"
                textbutton _("[mc_b_address]") action Show('rename', var_name_to_change='mc_b_address') text_style "char_info_button"
                text _(".)") style "char_info_title"
            hbox:
                text _("   (When speaking about them both, you refer to them as your") style "char_info_title"
                textbutton _("[mc_a_b_rel]s") action Show('rename', var_name_to_change='mc_a_b_rel') text_style "char_info_button"
                text _(".)") style "char_info_title"
            text _("")
            hbox:
                text _("- Your") style "char_info_title"
                textbutton _("[v_mc_rel]") action Show('rename', var_name_to_change='v_mc_rel') text_style "char_info_button"
                textbutton _("[v_name]") action Show('rename', var_name_to_change='v_name') text_style "char_info_button"
                textbutton _("[lastname]") action Show('rename', var_name_to_change='lastname') text_style "char_info_button"
                text _(" is married to") style "char_info_title"
                textbutton _("[vic_name]") action Show('rename', var_name_to_change='vic_name') text_style "char_info_button"
                text _(".") style "char_info_title"
            hbox:
                text _("   (You are her") style "char_info_title"
                textbutton _("[mc_v_rel]") action Show('rename', var_name_to_change='mc_v_rel') text_style "char_info_button"
                text _("and call her") style "char_info_title"
                textbutton _("[mc_v_address]") action Show('rename', var_name_to_change='mc_v_address') text_style "char_info_button"
                text _(", but she calls you by your name.)") style "char_info_title"
            text _("")
            hbox:
                text _("- Your") style "char_info_title"
                textbutton _("[vic_mc_rel]") action Show('rename', var_name_to_change='vic_mc_rel') text_style "char_info_button"
                textbutton _("[vic_name]") action Show('rename', var_name_to_change='vic_name') text_style "char_info_button"
                textbutton _("[lastname]") action Show('rename', var_name_to_change='lastname') text_style "char_info_button"
                text _(" is married to") style "char_info_title"
                textbutton _("[v_name]") action Show('rename', var_name_to_change='v_name') text_style "char_info_button"
                text _(".") style "char_info_title"
            hbox:
                text _("   (You are his") style "char_info_title"
                textbutton _("[mc_vic_rel]") action Show('rename', var_name_to_change='mc_vic_rel') text_style "char_info_button"
                text _("and call him") style "char_info_title"
                textbutton _("[mc_vic_address]") action Show('rename', var_name_to_change='mc_vic_address') text_style "char_info_button"
                text _(", but he calls you by your name.)") style "char_info_title"
            hbox:
                text _("   (When speaking about them both, you refer to them as your") style "char_info_title"
                textbutton _("[mc_v_vic_rel]s") action Show('rename', var_name_to_change='mc_v_vic_rel') text_style "char_info_button"
                text _(".)") style "char_info_title"
            text _("")
            hbox:
                text _("Together you are one big happy") style "char_info_title"
                textbutton _("[private_group]") action Show('rename', var_name_to_change ='private_group') text_style "char_info_button"
                text _(".") style "char_info_title"
            hbox:
                text _("People who've never meet our [private_group], see us as a") style "char_info_title"
                textbutton _("[public_group]") action Show('rename', var_name_to_change ='public_group') text_style "char_info_button"
                text _(".") style "char_info_title"

    add "gui/TOH_screens/settings/separator.png" alpha 0.2 yalign 0.89 xalign 0.5

    textbutton _("Restore Factory Default to All"):
        style "return_button"
        yalign 0.99
        xalign 0.3
        text_outlines [(3, "#000000", 0, 0)]
        action Confirm('Are you sure you want to reset all values to default"?', Function(factory_restore_all))

    textbutton _("Return"):
        style "return_button"
        yalign 0.99
        xalign 0.8
        text_outlines [(3, "#000000", 0, 0)]
        action Hide("set_rel")







style rel_button_text:
    color "#00ff00"
    hover_color "#ff0000"
    text_align 0.5

style rel_text:
    color "#FF0000"

screen rename(var_name_to_change):









    python:
        def change(var_name_to_change,val, return_key):
            if return_key: 
                
                if (getattr(renpy.store, "stored_input", "") == ""):
                    setattr(renpy.store, var_name_to_change, val)
                
                else:
                    setattr(renpy.store, var_name_to_change, getattr(renpy.store, "stored_input", ""))
            
            
            renpy.hide_screen("rename")



        def restore_factory(what_to_change):
            rel_dict = {"y_name" : "Jack",
                        "b_name" : "Bella",
                        "a_name" : "Ariel",
                        "v_name" : "Vivian",
                        "vic_name" : "Victor",
                        "lastname" : "Smith",
                        "y_lastname" : "Aroxson",
                        "mc_a_rel" : "roommate",
                        "a_mc_rel" : "roommate",
                        "mc_b_rel" : "roommate",
                        "b_mc_rel" : "roommate",
                        "v_mc_rel" : "landlady",
                        "mc_v_rel" : "tenant",
                        "vic_mc_rel" : "landlord",
                        "mc_vic_rel" : "tenant",
                        "mc_a_address" : "mate",
                        "a_mc_address" : "mate",
                        "mc_b_address" : "mate",
                        "b_mc_address" : "mate",
                        "mc_v_address" : "miss Smith",
                        "mc_vic_address" : "Mister Smith",
                        "private_group" : "team",
                        "public_group" : "group",
                        "mc_a_b_rel" : "roommate",
                        "mc_v_vic_rel" : "landlord"}
            setattr(renpy.store, what_to_change, rel_dict[what_to_change])
            Hide("rename")



        val = getattr(renpy.store, var_name_to_change,"")




        if show_default_value:
            setattr(renpy.store, "stored_input", val)
        else:
            setattr(renpy.store, "stored_input", "")





    style_prefix "game_menu"
    imagebutton idle "bg_main_menu" action NullAction()
    add "bg black" alpha 0.7
    fixed:
        vbox:
            if renpy.variant("pc"):
                null height (0.2 * config.screen_height)
            else:
                null height (0.02 *config.screen_height)
            hbox:
                xalign 0.5
                frame:

                    xalign 0.5
                    xmaximum 1100
                    ymaximum 300
                    has vbox
                    if renpy.variant("pc"):
                        hbox:
                            xalign 0.5
                            text "   Display current values as default input,   "
                        hbox:
                            xalign 0.5
                            text "or keep empty field? "
                    else:
                        hbox:
                            xalign 0.5
                            text "   Show current values as defaults, or empty field?  "
                    hbox:
                        xalign 0.5
                        style_prefix "radio"
                        textbutton ("Current Value") action SetVariable("show_default_value", True)
                        text "       "
                        textbutton ("Empty Value") action SetVariable("show_default_value", False)
            if renpy.variant("pc"):
                null height (0.1 * config.screen_height)
            else:
                null height (0.01 * config.screen_height)
            hbox:
                xfill True
                frame:
                    padding (10,20,10,20)
                    xalign 0.5
                    text _("   Please enter your new value (max 15 Characters) - currently: {color=f1e582}"+val+"{/color}   ")
            text ""
            hbox:
                xfill True
                if renpy.variant("pc"):
                    frame:
                        xalign 0.5
                        xmaximum 320
                        ymaximum 60
                        input id "input" default "":
                            style "input_text"
                            length 15
                            allow "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_-+.\///"
                            value NameInputValue("stored_input", "rename")
                        key "K_RETURN" action [Function(change,var_name_to_change,val,True)]
                        key "K_ESCAPE" action [Function(change,var_name_to_change,val,False)]
                else:
                    frame:
                        xalign 0.9
                        xmaximum 320
                        ymaximum 60
                        input id "input" default "":
                            style "input_text"
                            length 15
                            allow "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_-+.\///"
                            value NameInputValue("stored_input", "rename")
                        key "K_RETURN" action [Function(change,var_name_to_change,val,True)]
                        key "K_ESCAPE" action [Function(change,var_name_to_change,val,False)]
                    textbutton ("{color=FF0000}SUBMIT{/color}") action [Function(change,var_name_to_change,val,True)]
            null height (0.1 * config.screen_height)
            frame:
                padding (10,20,10,20)
                xalign 0.5
                text _("NOTE: When definding relationships with multiple people, do not use the\nplural version. For example, use {color=#f1e582}roommate{/color} instead of {color=#f1e582}roommate's{/color} or {color=#f1e582}roommates{/color}")
            null height (0.1 * config.screen_height)
            if not renpy.variant("small"):
                hbox:
                    spacing 20
                    text _("     ")
                    textbutton ("{color=FF0000}RETURN{/color}") action Hide('rename')
                    text "      "
                    textbutton ("Restore Default") action Confirm('Are you sure you want to reset this value to default"?', Function(restore_factory, var_name_to_change))


    if renpy.variant("small"):

        imagebutton:
            xalign 0.25
            yalign 0.3
            auto "btn_mm_back_%s" action Hide("rename",dissolve)







        textbutton ("Restore Default"):
            xalign 0.8
            yalign 0.3
            action Confirm('Are you sure you want to reset this value to default"?', Function(restore_factory, var_name_to_change))







init:
    screen unlock_code(what, password, tier):
        modal True
        default input_password = ""
        add Solid("#000000") alpha 0.5
        if renpy.variant("pc"):
            frame:
                xysize (455, 718)
                xalign 0.5
                yalign 0.5

                background "gui/popup message/popup_base.jpg"

                text "IMPORTANT:\nTo get this code, you must become a [tier] subscriber.\nPlease go here to get your code:":
                    ypos 574
                    font "DejaVuSans.ttf"
                    color "#000000"
                    size 16

                input id "gallery_pass" value ScreenVariableInputValue("input_password") pixel_width 370 xpos 35 ypos 410 allow "abcdefghijklmnopqrstuvwxyz"
                imagebutton:
                    idle "gui/popup message/button_idle.png"
                    hover "gui/popup message/button_hover.png"
                    insensitive "gui/popup message/button_insensitive.png"
                    sensitive input_password == password
                    action [SetField(persistent, "v_{}_locked".format(what), False), SetField (persistent,"v_{}_enabled".format(what), True),Hide("unlock_code")]

                    xalign 0.5
                    ypos 476
                imagebutton:
                    idle "gui/popup message/patreon_link_idle.png"
                    hover "gui/popup message/patreon_link_hover.png"

                    action OpenURL(url="https://patreon.com/mrdotsgames")

                    xpos 0.1
                    ypos 0.935

                imagebutton:
                    idle "gui/popup message/ss_link_idle.png"
                    hover "gui/popup message/ss_link_hover.png"

                    action OpenURL(url="https://subscribestar.adult/mrdotsgames")

                    xpos 0.5
                    ypos 0.935


                imagebutton:
                    idle "gui/popup message/delete_save_idle.png"
                    hover "gui/popup message/delete_save_hover.png"

                    action Hide("unlock_code")

                    xalign 1.0
                    ypos -2

        else:

            frame:
                xysize (455, 718)
                xalign 0.3
                yalign 0.05

                background "gui/popup message/popup_base_mobile.jpg"

                text "IMPORTANT:\nTo get this code, you must become a [tier] subscriber.\nPlease go here to get your code:":
                    xpos 12
                    ypos 120
                    font "DejaVuSans.ttf"
                    color "#000000"
                    size 16

                input id "gallery_pass" value ScreenVariableInputValue("input_password") pixel_width 370 xalign 0.5 yalign 0.01 allow "abcdefghijklmnopqrstuvwxyz"
            imagebutton:
                idle "gui/popup message/button_idle.png"
                hover "gui/popup message/button_hover.png"
                insensitive "gui/popup message/button_insensitive.png"
                sensitive input_password == password
                action [SetField(persistent, "v_{}_locked".format(what), False), SetField (persistent,"v_{}_enabled".format(what), True),Hide("unlock_code")]
                xalign 0.7
                yalign 0.1

            imagebutton:
                idle "gui/popup message/patreon_link_idle.png"
                hover "gui/popup message/patreon_link_hover.png"

                action OpenURL(url="https://patreon.com/mrdotsgames")

                xalign 0.40
                yalign 0.18

            imagebutton:
                idle "gui/popup message/ss_link_idle.png"
                hover "gui/popup message/ss_link_hover.png"

                action OpenURL(url="https://subscribestar.adult/mrdotsgames")

                xalign 0.47
                yalign 0.18


            imagebutton:
                idle "gui/popup message/delete_save_idle.png"
                hover "gui/popup message/delete_save_hover.png"

                action Hide("unlock_code")

                xalign 0.78
                yalign 1

style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 3

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 338

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.button_text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.button_text_properties("check_button")

style slider_slider:
    xsize 525

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize 675










screen history():




    predict False tag menu

    use game_menu(_("History"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0):

        style_prefix "history"

        for h in _history_list:

            window:


                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"
                        substitute False



                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute False

        if not _history_list:
            label _("The dialogue history is empty.")




define gui.history_allow_tags = { "alt", "noalt", "rt", "rb", "art" }


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    textalign gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    textalign gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5











screen help():
    tag menu


    default device = "info"

    use game_menu(_("Help"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 23

            hbox:
                textbutton _("Info") action SetScreenVariable("device", "info")
                textbutton _("Keyboard") action SetScreenVariable("device", "keyboard")
                textbutton _("Mouse") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")


            if device == "info":
                use info_help
            elif device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help



screen info_help():
    text _("For any help with anything to do with our games, the best way to do that is to join our unofficial Discord page here: {a=https://discord.gg/JbyH5HUnBh}https://discord.gg/JbyH5HUnBh{/a}")
    text _("Leave your questions or feedback in the #general channel - the channel that corresponds with the game you’re interested in e.g. #general-toh for any comments or questions about 'Thief of Hearts'.")
    text _("")
    text _("Alternatively, you can check out our blog, tutorials and also our FAQs under the 'Help' section: {a=https://mrdotsgames.com/}https://mrdotsgames.com/{/a}")
    text _("")
    text _("As per usual, you can leave questions on our {a=https://patreon.com/mrdotsgames}Patreon{/a} or {a=https://subscribestar.adult/mrdotsgames}Subscribestar{/a} pages, but the best way for a quicker response will be through our discord.")

screen keyboard_help():

    hbox:
        label _("Enter")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Space")
        text _("Advances dialogue without selecting choices.")

    hbox:
        label _("Arrow Keys")
        text _("Navigate the interface.")

    hbox:
        label _("Escape")
        text _("Accesses the game menu.")

    hbox:
        label _("Ctrl")
        text _("Skips dialogue while held down.")

    hbox:
        label _("Tab")
        text _("Toggles dialogue skipping.")

    hbox:
        label _("Page Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Page Down")
        text _("Rolls forward to later dialogue.")

    hbox:
        label "H"
        text _("Hides the user interface.")

    hbox:
        label "S"
        text _("Takes a screenshot.")

    hbox:
        label "V"
        text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")

    hbox:
        label "Shift+A"
        text _("Opens the accessibility menu.")


screen mouse_help():

    hbox:
        label _("Left Click")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Middle Click")
        text _("Hides the user interface.")

    hbox:
        label _("Right Click")
        text _("Accesses the game menu.")

    hbox:
        label _("Mouse Wheel Up\nClick Rollback Side")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Mouse Wheel Down")
        text _("Rolls forward to later dialogue.")


screen gamepad_help():

    hbox:
        label _("Right Trigger\nA/Bottom Button")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Left Trigger\nLeft Shoulder")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Right Shoulder")
        text _("Rolls forward to later dialogue.")


    hbox:
        label _("D-Pad, Sticks")
        text _("Navigate the interface.")

    hbox:
        label _("Start, Guide")
        text _("Accesses the game menu.")

    hbox:
        label _("Y/Top Button")
        text _("Hides the user interface.")

    textbutton _("Calibrate") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 12

style help_button_text:
    properties gui.button_text_properties("help_button")

style help_label:
    xsize 375
    right_padding 30

style help_label_text:
    size gui.text_size
    xalign 1.0
    textalign 1.0















screen confirm(message, yes_action, no_action):



    modal True

    zorder 200

    if message == layout.QUIT:
        use my_exit_screen
    else:

        style_prefix "confirm"

        add "gui/overlay/confirm.png"

        frame:

            has vbox:
                xalign .5
                yalign .5
                spacing 45

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 150

                textbutton _("Yes") action yes_action
                textbutton _("No") action no_action


    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    textalign 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.button_text_properties("confirm_button")









screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        has hbox:
            spacing 9

        text _("Skipping")

        text "▸" at tt_delayed_blink(0.0, 1.0) style "skip_triangle"
        text "▸" at tt_delayed_blink(0.2, 1.0) style "skip_triangle"
        text "▸" at tt_delayed_blink(0.4, 1.0) style "skip_triangle"



transform tt_delayed_blink(delay, cycle):
    alpha .5

    pause delay
    block:

        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:


    font "DejaVuSans.ttf"









screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at tt_notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform tt_notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .50 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")









screen nvl(dialogue, items):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing


        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)



        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            has fixed:
                yfit gui.nvl_height is None

            if d.who is not None:

                text d.who:
                    id d.who_id

            text d.what:
                id d.what_id




define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    textalign gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    textalign gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    textalign gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.button_text_properties("nvl_button")











screen bubble(who, what):
    style_prefix "bubble"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "bubble_namebox"

                text who:
                    id "who"

        text what:
            id "what"

style bubble_window is empty
style bubble_namebox is empty
style bubble_who is default
style bubble_what is default

style bubble_window:
    xpadding 30
    top_padding 5
    bottom_padding 5

style bubble_namebox:
    xalign 0.5

style bubble_who:
    xalign 0.5
    textalign 0.5
    color "#000"

style bubble_what:
    align (0.5, 0.5)
    text_align 0.5
    layout "subtitle"
    color "#000"

define bubble.frame = Frame("gui/bubble.png", 55, 55, 55, 95)
define bubble.thoughtframe = Frame("gui/thoughtbubble.png", 55, 55, 55, 55)

define bubble.properties = {
    "bottom_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "bottom_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "top_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "top_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "thought" : {
        "window_background" : bubble.thoughtframe,
    }
}

define bubble.expand_area = {
    "bottom_left" : (0, 0, 0, 22),
    "bottom_right" : (0, 0, 0, 22),
    "top_left" : (0, 22, 0, 0),
    "top_right" : (0, 22, 0, 0),
    "thought" : (0, 0, 0, 0),
}






style pref_vbox:
    variant "medium"
    xsize 675



screen quick_menu():
    variant "touch"

    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Back") action Rollback()
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Menu") action ShowMenu()
            textbutton _("Hide") action HideInterface()

style window:
    variant "small"


style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"


style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 510

style game_menu_content_frame:
    variant "small"
    top_margin 0

style pref_vbox:
    variant "small"
    xsize 600

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_vbox:
    variant "small"
    xsize None

style slider_slider:
    variant "small"
    xsize 900
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

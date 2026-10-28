init -1 style default:
    properties gui.text_properties()
    language gui.language
init offset = -1
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


style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)


style namebox:
    xpos gui.name_xpos
    xanchor 0.5
    xsize 100
    ypos gui.name_ypos
    ysize gui.namebox_height
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign 0.5
    yalign 0.5
    outlines [ (3, "#000", 1, 1) ]

style say_dialogue:
    properties gui.text_properties("dialogue")
    xpos gui.dialogue_xpos
    xsize 1600
    ypos gui.dialogue_ypos
    outlines [ (absolute(3), "#000", absolute(1), absolute(1)) ]










init -499 screen nvl(dialogue, items=None):


    if nvl_mode == "phone":
        use PhoneDialogue(dialogue, items)
    else:


        window:
            style "nvl_window"

            has vbox
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


init -499 screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            has fixed
            yfit gui.nvl_height is None

            if d.who is not None:

                text d.who:
                    id d.who_id

            text d.what:
                id d.what_id




define 1 config.nvl_list_length = gui.nvl_list_length

init 1 style nvl_window is default
init 1 style nvl_entry is default

init 1 style nvl_label is say_label
init 1 style nvl_dialogue is say_dialogue

init 1 style nvl_button is button
init 1 style nvl_button_text is button_text

init 1 style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

init 1 style nvl_entry:
    xfill True
    ysize gui.nvl_height

init 1 style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    text_align gui.nvl_name_xalign

init 1 style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

init 1 style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    text_align gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

init 1 style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

init 1 style nvl_button_text:
    properties gui.button_text_properties("nvl_button")






screen input(prompt):
    style_prefix "input"

    window:

        has vbox
        xalign gui.dialogue_text_xalign
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

init 1 python:
    global dialogue_updated
    dialogue_updated = True


init 1 python:
    def display_dialogue(speaker, what):
        global display_speaker_name, display_dialogue_text
        display_speaker_name = str(speaker)
        display_dialogue_text = str(what)


screen choice(items):
    style_prefix "choice"

    vbox:
        text "{color=#3CDFFF}{font=fonts/jenriv-titling-bold.otf}%s{/font}{/color}{size=55} {color=#ffffff}{font=fonts/VioletSans-Regular.otf}%s{/font}{/color}{size=58}" % ("", "") xalign 0.0 xpos -200 ypos -250




        for i in range(len(items)):

            $ icon_path = "gui/neturalicon.png"
            if supergood:
                $ icon_path = "gui/supergoodicon.png"
            elif superevil:
                $ icon_path = "gui/superevilicon.png"
            elif evil:
                $ icon_path = "gui/evilicon.png"
            elif sexaddict:
                $ icon_path = "gui/sexaddicticon.png"
            elif good:
                $ icon_path = "gui/goodicon.png"



            hbox:
                spacing 25
                xalign 0.0

                add icon_path xalign 0.0

                textbutton items[i].caption action items[i].action text_outlines [ (absolute(3), "#000", absolute(1), absolute(1)) ] text_xalign 0.0 xalign 0.0







define config.narrator_menu = True


style choice_vbox:
    xpos 1200
    ypos 1720
    xsize 2232
    spacing gui.choice_spacing

style choice_button:
    background None
    xalign 0.0
    yalign 0.0
    xsize 1600

style choice_button_text:
    font gui.choice_button_text_font
    size gui.choice_button_text_size
    xalign 0.0
    color gui.choice_button_text_idle_color
    hover_color gui.choice_button_text_hover_color
    insensitive_color gui.choice_button_text_insensitive_color









screen quick_menu():


    zorder 100

    if quick_menu:

        vbox:
            style_prefix "quick"

            xalign 1.0
            yalign 0.98

            textbutton _("Back") action Rollback() text_outlines [ (absolute(3), "#000", absolute(1), absolute(1)) ] text_xalign 1.0 xalign 1.0
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True) text_outlines [ (absolute(3), "#000", absolute(1), absolute(1)) ] text_xalign 1.0 xalign 1.0
            textbutton _("Auto") action Preference("auto-forward", "toggle") text_outlines [ (absolute(3), "#000", absolute(1), absolute(1)) ] text_xalign 1.0 xalign 1.0
            textbutton _("Q Save") action QuickSave() text_outlines [ (absolute(3), "#000", absolute(1), absolute(1)) ] text_xalign 1.0 xalign 1.0
            textbutton _("Q Load") action QuickLoad() text_outlines [ (absolute(3), "#000", absolute(1), absolute(1)) ] text_xalign 1.0 xalign 1.0
            textbutton _("Config") action ShowMenu('preferences') text_outlines [ (absolute(3), "#000", absolute(1), absolute(1)) ] text_xalign 1.0 xalign 1.0




init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.button_text_properties("quick_button")











screen navigation():

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.5

        spacing gui.navigation_spacing

        if main_menu:

            textbutton _("Start") action Start()

        else:

            textbutton _("History") action ShowMenu("history")

            textbutton _("Save") action ShowMenu("save")

        textbutton _("Load") action ShowMenu("load")

        textbutton _("Options") action ShowMenu("preferences")

        if _in_replay:

            textbutton _("End Replay") action EndReplay(confirm=True)

        elif not main_menu:

            textbutton _("Main Menu") action MainMenu()

        textbutton _("About") action ShowMenu("about")

        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):


            textbutton _("Controls") action ShowMenu("controls")

        if renpy.variant("pc"):



            textbutton _("Quit") action Quit(confirm=not main_menu)


style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")



init 1:
    default is_press_any_key_shown = False



transform 1 fade_in_out:
    alpha 0.0
    linear 1.0 alpha 1.0
    pause 0.5
    linear 1.0 alpha 0.0
    repeat

label main_menu_actions:

    call screen main_menu

    return


default 1 day_mode = True



default 1 show_buttons = True

init -499 screen main_menu():
    style_prefix "main_menu" tag menu



    if day_mode:
        add gui.main_menu_background
    else:
        add gui.main_menu_background2



    if show_buttons:
        textbutton _("Start") action Start() text_size 95 text_outlines [ (absolute(3), "#000", absolute(1), absolute(1)) ] xanchor 0.0 yanchor 1.0 xpos 300 ypos 1080 - -900 text_xalign 0.0
        textbutton _("Load") action ShowMenu("load") text_size 95 text_outlines [ (absolute(3), "#000", absolute(1), absolute(1)) ] xanchor 0.0 yanchor 1.0 xpos 700 ypos 1080 - -900 text_xalign 0.0
        textbutton _("Options") action ShowMenu("preferences") text_size 95 text_outlines [ (absolute(3), "#000", absolute(1), absolute(1)) ] xanchor 0.0 yanchor 1.0 xpos 1050 ypos 1080 - -900 text_xalign 0.0
        textbutton _("About") action ShowMenu("about") text_size 95 text_outlines [ (absolute(3), "#000", absolute(1), absolute(1)) ] xanchor 0.0 yanchor 1.0 xpos 1550 ypos 1080 - -900 text_xalign 0.0
        textbutton _("Patreon") action OpenURL("https://patreon.com/cheesecake3d") text_size 95 text_outlines [ (absolute(3), "#000", absolute(1), absolute(1)) ] xanchor 0.0 yanchor 1.0 xpos 1950 ypos 1080 - -900 text_xalign 0.0
        textbutton _("Discord") action OpenURL("https://discord.gg/cheesecake") text_size 95 text_outlines [ (absolute(3), "#000", absolute(1), absolute(1)) ] xanchor 0.0 yanchor 1.0 xpos 2500 ypos 1080 - -900 text_xalign 0.0
        textbutton _("Controls") action ShowMenu("controls") text_size 95 text_outlines [ (absolute(3), "#000", absolute(1), absolute(1)) ] xanchor 0.0 yanchor 1.0 xpos 3020 ypos 1080 - -900 text_xalign 0.0
        textbutton _("Quit") action Quit(confirm=not main_menu) text_size 95 text_outlines [ (absolute(3), "#000", absolute(1), absolute(1)) ] xanchor 0.0 yanchor 1.0 xpos 3350 ypos 1080 - -900 text_xalign 0.0




style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 840
    yfill True

    background "gui/overlay/main_menu.png"

style main_menu_vbox:
    xalign 1.0
    xoffset -60
    xmaximum 2400
    yalign 1.0
    yoffset -60

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")











screen game_menu(title, scroll=None, yinitial=0.0):

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


    label title text_outlines [ (absolute(3), "#000", absolute(1), absolute(1)) ]

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
    bottom_padding 90
    top_padding 360

    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 840
    yfill True

style game_menu_content_frame:
    left_margin 120
    right_margin 60
    top_margin 30

style game_menu_viewport:
    xsize 2760

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 30

style game_menu_label:
    xpos 150
    ysize 360

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -90









screen about():
    tag menu





    use game_menu(_("About"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text _("Version [config.version!t]\n")


            if gui.about:
                text "[gui.about!t]\n"

            text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")



define gui.about = ""


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size







init 1 python:
    style.slot_time_text.font = "fonts/jenriv-titling-bold.otf"




screen save():
    tag menu


    use file_slots(_("Save"))


screen load():
    tag menu


    use file_slots(_("Load"))


screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))


    $ num_to_letter = {
        1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G', 8: 'H', 9: 'I', 10: 'J',
        11: 'K', 12: 'L', 13: 'M', 14: 'N', 15: 'O', 16: 'P', 17: 'Q', 18: 'R', 19: 'S'
    }

    use game_menu(title):

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
                        action FileAction(slot)
                        has vbox
                        add FileScreenshot(slot) xalign 0.5
                        text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                            style "slot_time_text"
                        text FileSaveName(slot):
                            style "slot_name_text"
                        key "save_delete" action FileDelete(slot)

            hbox:
                style_prefix "page"
                xalign 0.5
                yalign 1.0
                spacing gui.page_spacing

                if config.has_autosave:
                    textbutton _("{#auto_page}Auto Saves") action FilePage("auto")

                if config.has_quicksave:
                    textbutton _("{#quick_page}Quick Saves") action FilePage("quick")


                for page in range(1, 20):
                    textbutton num_to_letter[page] action FilePage(page)




style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 150
    ypadding 9

style page_label_text:
    text_align 0.5
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








screen preferences():
    tag menu


    default prefscreen_TabShowing = "Visuals"

    use game_menu(_("Preferences"), scroll="viewport"):
        vbox:
            yalign 0.1
            frame:
                background None
                xsize 2400
                xmargin 35
                xminimum 2200
                has hbox
                spacing 20
                xminimum 2500
                textbutton "Graphics" action [With(dissolve),SetScreenVariable("prefscreen_TabShowing","Visuals")] text_xalign 0.5 text_outlines [ (absolute(3), "#000", absolute(1), absolute(1)) ] xalign 0.0
                textbutton "Text" action [With(dissolve),SetScreenVariable("prefscreen_TabShowing","Text")] text_xalign 0.5 text_outlines [ (absolute(3), "#000", absolute(1), absolute(1)) ] xalign 0.5
                textbutton "Sound" action [With(dissolve),SetScreenVariable("prefscreen_TabShowing","Audio")] text_xalign 0.5 text_outlines [ (absolute(3), "#000", absolute(1), absolute(1)) ] xalign 1.0
            frame:
                background Frame("gui-menu-frame",top=120,left=120)
                xmargin 35
                xsize 2600
                xminimum 3800
                yminimum 1500
                padding (35,0)
                yalign 0.5
                if prefscreen_TabShowing == "Visuals":
                    vbox:
                        yalign 0.1
                        spacing 10
                        if renpy.variant("pc"):
                            hbox:
                                yalign 1.0
                                textbutton _("Display ") text_size 60 action NullAction() sensitive False text_yalign 1.0 ysize 100 text_outlines [ (absolute(3), "#000", absolute(1), absolute(1)) ] text_color '#3CDFFF'
                                textbutton _("Windowed") action Preference("display", "window") text_size 60 text_font "fonts/jenriv-titling-bold.otf" text_yalign 1.0 ysize 100 text_outlines [ (absolute(3), "#000", absolute(1), absolute(1)) ]
                                textbutton _("Fullscreen") action Preference("display", "fullscreen") text_size 60 text_font "fonts/jenriv-titling-bold.otf" text_yalign 1.0 ysize 100 text_outlines [ (absolute(3), "#000", absolute(1), absolute(1)) ]
                            hbox:
                                yalign 1.0
                                textbutton _("Frame Skipping ") text_size 60 action NullAction() sensitive False text_yalign 1.0 ysize 100 text_outlines [ (absolute(3), "#000", absolute(1), absolute(1)) ] text_color '#3CDFFF'
                                textbutton _("On") action Preference("gl tearing", False) text_size 60 text_font "fonts/jenriv-titling-bold.otf" text_yalign 1.0 ysize 100 text_outlines [ (absolute(3), "#000", absolute(1), absolute(1)) ]
                                textbutton _("Off") action Preference("gl tearing", True) text_size 60 text_font "fonts/jenriv-titling-bold.otf" text_yalign 1.0 ysize 100 text_outlines [ (absolute(3), "#000", absolute(1), absolute(1)) ]
                            hbox:
                                yalign 1.0
                                textbutton _("Power Save Mode") text_size 60 action NullAction() sensitive False text_yalign 1.0 ysize 100 text_outlines [ (absolute(3), "#000", absolute(1), absolute(1)) ] text_color '#3CDFFF'
                                textbutton _("On") action Preference("gl powersave", True) text_size 60 text_font "fonts/jenriv-titling-bold.otf" text_yalign 1.0 ysize 100 text_outlines [ (absolute(3), "#000", absolute(1), absolute(1)) ]
                                textbutton _("Off") action Preference("gl powersave", False) text_size 60 text_font "fonts/jenriv-titling-bold.otf" text_yalign 1.0 ysize 100 text_outlines [ (absolute(3), "#000", absolute(1), absolute(1)) ]
                                textbutton _("Auto") action Preference("gl powersave", "auto") text_size 60 text_font "fonts/jenriv-titling-bold.otf" text_yalign 1.0 ysize 100 text_outlines [ (absolute(3), "#000", absolute(1), absolute(1)) ]

                if prefscreen_TabShowing == "Text":
                    vbox:
                        spacing 15
                        yalign 0.1
                        vbox:
                            xmaximum 3000
                            hbox:
                                textbutton _("Rollback Side") text_size 60 action NullAction() sensitive False text_yalign 1.0 ysize 100 text_outlines [ (absolute(3), "#000", absolute(1), absolute(1)) ] text_color '#3CDFFF'
                                textbutton _("Disable") action Preference("rollback side", "disable") text_size 60 text_font "fonts/jenriv-titling-bold.otf" text_yalign 1.0 ysize 100 text_outlines [ (absolute(3), "#000", absolute(1), absolute(1)) ]
                                textbutton _("Left") action Preference("rollback side", "left") text_size 60 text_font "fonts/jenriv-titling-bold.otf" text_yalign 1.0 ysize 100 text_outlines [ (absolute(3), "#000", absolute(1), absolute(1)) ]
                                textbutton _("Right") action Preference("rollback side", "right") text_size 60 text_font "fonts/jenriv-titling-bold.otf" text_yalign 1.0 ysize 100 text_outlines [ (absolute(3), "#000", absolute(1), absolute(1)) ]
                            hbox:
                                textbutton _("Skip") text_size 60 action NullAction() sensitive False text_yalign 1.0 ysize 100 text_outlines [ (absolute(3), "#000", absolute(1), absolute(1)) ] text_color '#3CDFFF'
                                textbutton _("Unseen Text") action Preference("skip", "toggle") text_size 60 text_font "fonts/jenriv-titling-bold.otf" text_yalign 1.0 ysize 100 text_outlines [ (absolute(3), "#000", absolute(1), absolute(1)) ]
                                textbutton _("After Choices") action Preference("after choices", "toggle") text_size 60 text_font "fonts/jenriv-titling-bold.otf" text_yalign 1.0 ysize 100 text_outlines [ (absolute(3), "#000", absolute(1), absolute(1)) ]
                                textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle")) text_size 60 text_font "fonts/jenriv-titling-bold.otf" text_yalign 1.0 ysize 100 text_outlines [ (absolute(3), "#000", absolute(1), absolute(1)) ]
                            hbox:
                                textbutton _("Auto") text_size 60 action NullAction() sensitive False text_yalign 1.0 ysize 100 text_outlines [ (absolute(3), "#000", absolute(1), absolute(1)) ] text_color '#3CDFFF'
                                textbutton _("Wait for Voice") action Preference("wait for voice", "toggle") text_size 60 text_font "fonts/jenriv-titling-bold.otf" text_yalign 1.0 ysize 100 text_outlines [ (absolute(3), "#000", absolute(1), absolute(1)) ]
                        vbox:
                            vbox:
                                spacing 20
                                xmaximum 2200
                                textbutton _("Text Speed") text_size 60 action NullAction() sensitive False text_yalign 1.0 ysize 100 text_outlines [ (absolute(3), "#000", absolute(1), absolute(1)) ] text_color '#3CDFFF'
                                bar value Preference("text speed")

                                textbutton _("Auto Forward Time") text_size 60 action NullAction() sensitive False text_yalign 1.0 ysize 100 text_outlines [ (absolute(3), "#000", absolute(1), absolute(1)) ] text_color '#3CDFFF'
                                bar value Preference("auto-forward time")





                if prefscreen_TabShowing == "Audio":

                    vbox:
                        spacing 10
                        yalign 0.1

                        if config.has_music:

                            textbutton _("Music & Animation Sound"):
                                text_size 60
                                action NullAction()
                                sensitive False
                                text_yalign 1.0
                                ysize 100
                                text_outlines [ (absolute(3), "#000", absolute(1), absolute(1)) ]
                                text_color "#3CDFFF"

                            hbox:
                                xmaximum 2200

                                bar value Preference("music volume")

                                textbutton _("Mute"):
                                    action Preference("music mute", "toggle")
                                    text_outlines [ (absolute(3), "#000", absolute(1), absolute(1)) ]

                        if config.has_sound:

                            textbutton _("Sound Effects"):
                                text_size 60
                                action NullAction()
                                sensitive False
                                text_yalign 1.0
                                ysize 100
                                text_outlines [ (absolute(3), "#000", absolute(1), absolute(1)) ]
                                text_color "#3CDFFF"

                            hbox:
                                xmaximum 2200

                                bar value Preference("sound volume")

                                textbutton _("Mute"):
                                    action Preference("sound mute", "toggle")
                                    text_outlines [ (absolute(3), "#000", absolute(1), absolute(1)) ]

                        textbutton _("UI Hover & Click Sounds"):
                            text_size 60
                            action NullAction()
                            sensitive False
                            text_yalign 1.0
                            ysize 100
                            text_outlines [ (absolute(3), "#000", absolute(1), absolute(1)) ]
                            text_color "#3CDFFF"

                        hbox:
                            xmaximum 2200

                            textbutton _("Mute Both"):
                                action Preference("mixer ui_sfx mute", "toggle")
                                text_outlines [ (absolute(3), "#000", absolute(1), absolute(1)) ]

                        if config.has_voice:

                            textbutton _("Voice Volume"):
                                text_size 60
                                action NullAction()
                                sensitive False
                                text_yalign 1.0
                                ysize 100
                                text_outlines [ (absolute(3), "#000", absolute(1), absolute(1)) ]
                                text_color "#FCEE0C"

                            hbox:
                                xmaximum 2200

                                bar value Preference("voice volume")

                                textbutton _("Mute"):
                                    action Preference("voice mute", "toggle")
                                    text_outlines [ (absolute(3), "#000", absolute(1), absolute(1)) ]

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
    bottom_margin 6

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 675

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
    xsize 1050

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 30

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize 1350










screen history():
    tag menu



    predict False

    use game_menu(_("History"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0):

        style_prefix "history"

        for h in _history_list:

            window:


                has fixed
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




define gui.history_allow_tags = set()


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

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
    text_align gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5








screen help():
    tag menu


    default device = "keyboard"

    use game_menu(_("Help"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 45

            hbox:

                textbutton _("Keyboard") action SetScreenVariable("device", "keyboard")
                textbutton _("Mouse") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


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
    xmargin 24

style help_button_text:
    properties gui.button_text_properties("help_button")

style help_label:
    xsize 750
    right_padding 60

style help_label_text:
    size gui.text_size
    xalign 1.0
    text_align 1.0















screen confirm(message, yes_action, no_action):


    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        has vbox
        xalign .5
        yalign .5
        spacing 90

        label _(message):
            style "confirm_prompt"
            xalign 0.5

        hbox:
            xalign 0.5
            spacing 300

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
    text_align 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.button_text_properties("confirm_button")









screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        has hbox
        spacing 18

        text _("Skipping")

        text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
        text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
        text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"



transform delayed_blink(delay, cycle):
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

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")









screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox
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

            has fixed
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
    text_align gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    text_align gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.button_text_properties("nvl_button")







style pref_vbox:
    variant "medium"
    xsize 1350



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
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

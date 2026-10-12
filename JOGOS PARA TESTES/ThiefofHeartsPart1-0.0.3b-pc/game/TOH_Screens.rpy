init:
    $ mm_movie_active = True
    $ mm_show = True
    $ v_pref_tab = 0
    $ v_pref_names = ["GAME",  "EXTRAS", "AUDIO"]



    $ v_settings_display_text = "WINDOW"

init python:
    if renpy.variant("small"):
        style.window.background = ConditionSwitch(
            "persistent.v_textbox_dialogue == True", "gui/phone/textbox.png",
            "persistent.v_textbox_dialogue == False", "gui/no_textbox.png")
    else:
        style.window.background = ConditionSwitch(
            "persistent.v_textbox_dialogue == True", "gui/textbox.png",
            "persistent.v_textbox_dialogue == False", "gui/no_textbox.png")

style btntop_button_text is text:
    size 25

style btntopidle_button_text is text:
    size 25
    color "#828282"
    hover_color "#ffffff"
style pref_bar:
    size 25
    color "#828282"

style buttonz_button_text is text:
    size 25
    color "#ffffff"
    hover_color "#982d2d"
    insensitive_color "#888"


init -5 python:

    style.my_bar = Style(style.default)
    style.my_bar.xmaximum = 315 
    style.my_bar.ymaximum = 30 
    style.my_bar.left_gutter = 5
    style.my_bar.right_gutter = 5

    style.my_bar.left_bar = Frame("gui/TOH_screens/bar/bar_full.png", 0, 0)
    style.my_bar.right_bar = Frame("gui/TOH_screens/bar/bar_empty.png", 0, 0)

    style.my_bar.thumb = "gui/TOH_screens/bar/bar_thumb.png"
    style.my_bar.thumb_shadow = None
    style.my_bar.thumb_offset = 5



screen btn_settings:
    tag menu
    if v_pref_tab == 0:
        add "gui/TOH_screens/settings/bg_settings_topbuttons_frame_center.png"
        imagebutton:
            auto "gui/TOH_screens/settings/btn_next_%s.png"
            action SetVariable("v_pref_tab",1)
            xalign 0.57
            yalign 0.89
        fixed:
            textbutton _("{color=#ffffff}{size=25}Next{/size}{/color}") xalign 0.555 yalign 0.886

        imagebutton:
            auto "gui/TOH_screens/settings/btn_back_%s.png"
            action SetVariable("v_pref_tab",2)
            xalign 0.40
            yalign 0.89
        fixed:
            textbutton _("{color=#ffffff}{size=25}Back{/size}{/color}") xalign 0.42 yalign 0.886





        text "{size=25}GAME SETTINGS{/size}" xalign 0.49 yalign 0.22



        vbox:

            vbox:

                xpos 500
                ypos 300
                xmaximum 500
                if renpy.variant("pc"):
                    hbox:
                        button:
                            text _("{size=25}DISPLAY{/size}")
                            xsize 500
                        style_prefix "radio"
                        textbutton _("{size=25}Window{/size}") action Preference("display", "window")
                        textbutton _("/") style_prefix "buttonz"
                        textbutton _("{size=25}Fullscreen{/size}") action Preference("display", "fullscreen")

                    add "gui/TOH_screens/settings/separator.png" alpha 0.2

                    hbox:
                        style_prefix "radio"
                        button:
                            text _("{size=25}ROLLBACK SIDE{/size}")
                            xsize 500
                        textbutton _("{size=25}Disable{/size}") action Preference("rollback side", "disable")
                        textbutton _("/") style_prefix "buttonz"
                        textbutton _("{size=25}Left{/size}") action Preference("rollback side", "left")
                        textbutton _("/") style_prefix "buttonz"
                        textbutton _("{size=25}Right{/size}") action Preference("rollback side", "right")

                    add "gui/TOH_screens/settings/separator.png" alpha 0.2

                hbox:
                    style_prefix "check"
                    button:
                        text _("{size=25}SKIP TEXT{/size}")
                        xsize 500
                    textbutton _("{size=25}Unseen Text{/size}") action Preference("skip", "toggle")
                    textbutton _("/") style_prefix "buttonz"
                    textbutton _("{size=25}After Choices{/size}") action Preference("after choices", "toggle")
                    textbutton _("/") style_prefix "buttonz"
                    textbutton _("{size=25}Transitions{/size}") action InvertSelected(Preference("transitions", "toggle"))

                add "gui/TOH_screens/settings/separator.png" alpha 0.2


                hbox:
                    style_prefix "check"
                    button:
                        text _("{size=25}CUSTOM SAVE NAMES{/size}")
                        xsize 500
                    textbutton _("{size=25}Enabled{/size}") action SetField(persistent, "enable_save_name", True)
                    textbutton _("{size=25}Disable{/size}") action SetField(persistent, "enable_save_name", False)

                add "gui/TOH_screens/settings/separator.png" alpha 0.2

                hbox:
                    style_prefix "check"
                    button:
                        text _("{size=25}TEXTBOX OPACITY{/size}")
                        xsize 350
                    hbox:
                        xpos 200
                        bar value FieldValue(persistent, "dialogueBoxOpacity", range=1.0, style="slider"):
                            style "my_bar"
                            xysize (300,30)
                            ypos 5

                add "gui/TOH_screens/settings/separator.png" alpha 0.2

                hbox:
                    style_prefix "check"
                    button:
                        text _("{size=25}TEXT SPEED{/size}")
                        xsize 350
                    hbox:
                        xpos 200
                        bar value Preference("text speed"):
                            style "my_bar"
                            xysize (300,30)
                            ypos 5

                add "gui/TOH_screens/settings/separator.png" alpha 0.2

                hbox:
                    style_prefix "check"
                    button:
                        text _("{size=25}AUTO-FORWARD TIME{/size}")
                        xsize 350
                    hbox:
                        xpos 200
                        bar value Preference("auto-forward time"):
                            style "my_bar"
                            xysize (300,30)
                            ypos 5

                add "gui/TOH_screens/settings/separator.png" alpha 0.2

                hbox:
                    style_prefix "radio"
                    button:
                        text _("{size=25}FONT STYLE{/size}")
                        xsize 500
                    textbutton _("{size=25}Righteous{/size}") action gui.SetPreference("font", "fonts/Righteous.ttf")
                    textbutton _("{size=25}Georgia{/size}") action gui.SetPreference("font", "fonts/georgia.ttf")
                    textbutton _("{size=25}OpenSans{/size}") action gui.SetPreference("font", "fonts/OpenSans-Regular.ttf")

                add "gui/TOH_screens/settings/separator.png" alpha 0.2

                hbox:
                    style_prefix "radio"
                    button:
                        text _("{size=25}TEXT SIZE{/size}")
                        xsize 500
                    textbutton _("{size=25}Normal{/size}") action [gui.SetPreference("text_size", 33), gui.SetPreference ("name_text_size", 45) , gui.SetPreference ("interface_text_size", 33), gui.SetPreference ("label_text_size", 36), gui.SetPreference ("slot_button_text_size", 24)]
                    textbutton _("{size=25}Big{/size}") action [gui.SetPreference("text_size", 38), gui.SetPreference ("name_text_size", 50), gui.SetPreference ("interface_text_size", 38), gui.SetPreference ("label_text_size", 41), gui.SetPreference ("slot_button_text_size", 28)]
                    textbutton _("{size=25}Bigger!{/size}") action [gui.SetPreference("text_size", 43), gui.SetPreference ("name_text_size", 55), gui.SetPreference ("interface_text_size", 43), gui.SetPreference ("label_text_size", 46), gui.SetPreference ("slot_button_text_size", 34)]

                add "gui/TOH_screens/settings/separator.png" alpha 0.2

                if renpy.variant("pc"):
                    hbox:
                        button:
                            text _("{size=25}CUSTOM MOUSE POINTER{/size}")
                            xsize 500
                        style_prefix "radio"
                        textbutton _("{size=25}Yes{/size}") action SetVariable ("default_mouse","new")
                        textbutton _("/") style_prefix "buttonz"
                        textbutton _("{size=25}No{/size}") action SetVariable ("default_mouse","default")


        textbutton v_pref_names[0] style_prefix "btntop" xalign 0.485 yalign 0.15 action SetVariable("v_pref_tab",0)
        textbutton v_pref_names[2] style_prefix "btntopidle" xalign 0.412 yalign 0.15 action SetVariable("v_pref_tab",2)
        textbutton v_pref_names[1] style_prefix "btntopidle" xalign 0.58 yalign 0.15 action SetVariable("v_pref_tab",1)

    if v_pref_tab == 1:
        add "gui/TOH_screens/settings/bg_settings_topbuttons_frame_right.png"
        imagebutton:
            auto "gui/TOH_screens/settings/btn_next_%s.png"
            action SetVariable("v_pref_tab",2)
            xalign 0.57
            yalign 0.89
        fixed:
            textbutton _("{color=#ffffff}{size=25}Next{/size}{/color}") xalign 0.555 yalign 0.886

        imagebutton:
            auto "gui/TOH_screens/settings/btn_back_%s.png"
            action SetVariable("v_pref_tab",0)
            xalign 0.40
            yalign 0.89
        fixed:
            textbutton _("{color=#ffffff}{size=25}Back{/size}{/color}") xalign 0.42 yalign 0.886

        text "{size=25}EXTRAS SETTINGS{/size}" xalign 0.49 yalign 0.22

        textbutton v_pref_names[0] style_prefix "btntopidle" xalign 0.485 yalign 0.15 action SetVariable("v_pref_tab",0)
        textbutton v_pref_names[2] style_prefix "btntopidle" xalign 0.412 yalign 0.15 action SetVariable("v_pref_tab",2)
        textbutton v_pref_names[1] style_prefix "btntop" xalign 0.58 yalign 0.15 action SetVariable("v_pref_tab",1)

    if v_pref_tab == 2:
        add "gui/TOH_screens/settings/bg_settings_topbuttons_frame_left.png"
        imagebutton:
            auto "gui/TOH_screens/settings/btn_next_%s.png"
            action SetVariable("v_pref_tab",0)
            xalign 0.57
            yalign 0.89
        fixed:
            textbutton _("{color=#ffffff}{size=25}Next{/size}{/color}") xalign 0.555 yalign 0.886

        imagebutton:
            auto "gui/TOH_screens/settings/btn_back_%s.png"
            action SetVariable("v_pref_tab",1)
            xalign 0.40
            yalign 0.89
        fixed:
            textbutton _("{color=#ffffff}{size=25}Back{/size}{/color}") xalign 0.42 yalign 0.886



        text "{size=25}AUDIO SETTINGS{/size}" xalign 0.49 yalign 0.22


        vbox:

            vbox:

                xpos 500
                ypos 300
                xmaximum 500
                hbox:
                    if config.has_music:
                        style_prefix "check"
                        button:
                            text _("{size=25}MUSIC VOLUME{/size}")
                            xsize 500
                        hbox:
                            xpos 200
                            bar value Preference("music volume"):
                                style "my_bar"
                                xysize (300,30)
                                ypos 5

                add "gui/TOH_screens/settings/separator.png" alpha 0.2


                hbox:
                    if config.has_sound:
                        style_prefix "check"
                        button:
                            text _("{size=25}SOUND EFFECTS VOLUME{/size}")
                            xsize 500
                        hbox:
                            xpos 200
                            bar value Preference("sound volume"):
                                style "my_bar"
                                xysize (300,30)
                                ypos 5
                add "gui/TOH_screens/settings/separator.png" alpha 0.2

                hbox:
                    if config.has_sound:
                        style_prefix "check"
                        button:
                            text _("{size=25}Sex Effects Volume{/size}")
                            xsize 500
                        hbox:
                            xpos 200
                            bar value MixerValue('sex'):
                                style "my_bar"
                                xysize (300,30)
                                ypos 5
                                tooltip "Adjusting the game's sex effects volume. Only effects the sex sounds played."

                add "gui/TOH_screens/settings/separator.png" alpha 0.2

                hbox:
                    if config.has_sound:
                        style_prefix "check"
                        button:
                            text _("{size=25}MUTE ALL{/size}")
                            xsize 500
                        hbox:
                            xpos 200
                            textbutton _("{size=25}Mute{/size}") action Preference("all mute", "toggle")


        textbutton v_pref_names[0] style_prefix "btntopidle" xalign 0.485 yalign 0.15 action SetVariable("v_pref_tab",0)
        textbutton v_pref_names[2] style_prefix "btntop" xalign 0.412 yalign 0.15 action SetVariable("v_pref_tab",2)
        textbutton v_pref_names[1] style_prefix "btntopidle" xalign 0.58 yalign 0.15 action SetVariable("v_pref_tab",1)

    imagebutton:
        auto "gui/TOH_screens/settings/btn_exit_%s.png"
        action Return()
        xalign 0.1
        yalign 0.89
    fixed:
        textbutton _("{color=#ffffff}{size=25}Exit{/size}{/color}") xalign 0.145 yalign 0.886



style text_about_style:
    size 25
    outlines [ (3, "#000000", 0, 0)]

style text_about_style_small:
    size 40
    outlines [ (3, "#000000", 0, 0)]



screen TOH_About:
    tag menu
    add "exit"
    add "black" alpha 0.3
    if renpy.variant("small"):
        viewport:
            xalign 0.2
            yalign 0.2
            scrollbars "vertical"
            mousewheel True
            draggable True
            xmaximum 1700
            ymaximum 800
            has vbox

            text _("{size=50}{color=#0ea359}ABOUT{/color}{/size}") style "text_about_style"
            text _("")
            text _("MrDotsGames was founded in September 2016.") style "text_about_style_small"
            text _("So far we have released and completed three games - DMD, Melody and Sunshine Love.") style "text_about_style_small"
            text _("")
            text _("Our mission is to create classic Adult Visual Novels that you want to play again and again for many years to come.") style "text_about_style_small"
            text _("We strive to always deliver quality updates and to continually evolve as developers.") style "text_about_style_small"
            text _("")
            text _("Our team consists of:") style "text_about_style_small"
            text _("")
            text _("{color=#edce6f}MrDots {/color}(Creator, Coding, Rendering, Beta Testing)") style "text_about_style_small"
            text _("{color=#edce6f}HearszAM {/color}(Chief Scene Writer, Coding, Beta Testing, Promotions)") style "text_about_style_small"
            text _("{color=#edce6f}Mistress Elemental {/color}(Rendering, Coding, Beta Testing)") style "text_about_style_small"
            text _("{color=#edce6f}HyperServer {/color}(Ideas, Writing, Coding, Character Development, Beta Testing)") style "text_about_style_small"
            text _("{color=#edce6f}Kasami {/color}(Rendering)") style "text_about_style_small"
            text _("")
            text _("To learn more about our journey so far, please check out our promotional video for MrDotsGames:") style "text_about_style_small"
            text _("{a=https://www.youtube.com/watch?v=7cuCxasLzwc&t=3s&ab_channel=MrDotsGames}https://www.youtube.com/watch?v=7cuCxasLzwc&t=3s&ab_channel=MrDotsGames{/a}") style "text_about_style_small"
    else:
        vbox:
            xalign 0.2
            yalign 0.2
            text _("{size=40}{color=#0ea359}ABOUT{/color}{/size}") style "text_about_style"
            text _("")
            text _("MrDotsGames was founded in September 2016.") style "text_about_style"
            text _("So far we have released and completed three games - DMD, Melody and Sunshine Love.") style "text_about_style"
            text _("")
            text _("Our mission is to create classic Adult Visual Novels that you want to play again and again for many years to come.") style "text_about_style"
            text _("We strive to always deliver quality updates and to continually evolve as developers.") style "text_about_style"
            text _("")
            text _("Our team consists of:") style "text_about_style"
            text _("")
            text _("{color=#edce6f}MrDots {/color}(Creator, Coding, Rendering, Beta Testing)") style "text_about_style"
            text _("{color=#edce6f}HearszAM {/color}(Chief Scene Writer, Coding, Beta Testing, Promotions)") style "text_about_style"
            text _("{color=#edce6f}Mistress Elemental {/color}(Rendering, Coding, Beta Testing)") style "text_about_style"
            text _("{color=#edce6f}HyperServer {/color}(Ideas, Writing, Coding, Character Development, Beta Testing)") style "text_about_style"
            text _("{color=#edce6f}Kasami {/color}(Rendering)") style "text_about_style"
            text _("")
            text _("To learn more about our journey so far, please check out our promotional video for MrDotsGames:") style "text_about_style"
            text _("{a=https://www.youtube.com/watch?v=7cuCxasLzwc&t=3s&ab_channel=MrDotsGames}https://www.youtube.com/watch?v=7cuCxasLzwc&t=3s&ab_channel=MrDotsGames{/a}") style "text_about_style"






    if renpy.variant("small"):
        hbox:
            xalign 0.5
            yalign 0.9
            textbutton _("Support Our Work") action ShowMenu("toh_support") style "special_menu_style"
    else:
        hbox:
            xalign 0.5
            yalign 0.8
            textbutton _("Support Our Work") action ShowMenu("toh_support") style "special_menu_style"

    imagebutton:
        xalign 0.01
        yalign 0.98
        auto "btn_mm_back_%s" action Return()



screen TOH_settings():
    key [ 'mouseup_3' ] action Return()
    tag menu
    add "gui/TOH_screens/settings/toh_settings_bg.jpg"
    add "bg/bg black.png" alpha 0.8
    add "gui/TOH_screens/settings/bg_settings_frame.png"

    text "SETTINGS" xalign 0.485 yalign 0.09
    use game_menu(_("Settings"), scroll="viewport"):
        if v_pref_tab == 0:
            add "gui/TOH_screens/settings/bg_settings_topbuttons_frame_center.png"
            imagebutton:
                auto "gui/TOH_screens/settings/btn_next_%s.png"
                action SetVariable("v_pref_tab",1)
                xalign 0.57
                yalign 0.89
            fixed:
                textbutton _("{color=#ffffff}{size=25}Next{/size}{/color}") xalign 0.555 yalign 0.886

            imagebutton:
                auto "gui/TOH_screens/settings/btn_back_%s.png"
                action SetVariable("v_pref_tab",2)
                xalign 0.40
                yalign 0.89
            fixed:
                textbutton _("{color=#ffffff}{size=25}Back{/size}{/color}") xalign 0.42 yalign 0.886





            text "{size=25}GAME SETTINGS{/size}" xalign 0.49 yalign 0.22







screen toh_file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))
    text "{size=45}[title] Game{/size}" xalign 0.5 yalign 0.05

    if title == "Load":
        add "gui/TOH_screens/settings/bg_settings_topbuttons_frame_left.png" xpos 0.05
        textbutton _("{size=35}Load{/size}") style_prefix "btntop" xalign 0.465 yalign 0.145 action ShowMenu('load')
        textbutton _("{size=35}Save{/size}") style_prefix "btntopidle" xalign 0.58 yalign 0.145 action ShowMenu('save')
    else:
        add "gui/TOH_screens/settings/bg_settings_topbuttons_frame_right.png"
        textbutton _("{size=35}Load{/size}") style_prefix "btntopidle" xalign 0.465 yalign 0.145 action ShowMenu('load')
        textbutton _("{size=35}Save{/size}") style_prefix "btntop" xalign 0.58 yalign 0.145 action ShowMenu('save')





    fixed:

        frame:
            background Frame("gui/TOH_screens/load_save/toh_frame1.png", 1, 1)
            xalign 0.5
            yalign 0.5
            has grid gui.file_slot_cols gui.file_slot_rows:
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
            yalign 0.9
            button:
                style "page_label"

                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value

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
                if not FileCurrentPage() == "auto" and "quick":
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
    imagebutton:
        auto "gui/TOH_screens/settings/btn_exit_%s.png"
        action Return()
        xalign 0.01
        yalign 0.92
    fixed:
        textbutton _("{color=#ffffff}{size=25}Exit{/size}{/color}") xalign 0.055 yalign 0.916
init:
    default whom = ""

screen buttonExample:
    add "gui/TOH_screens/settings/separator.png" alpha 0.2
    imagebutton:
        focus_mask True
        auto "gui/TOH_screens/settings/btn_exit_%s.png"
        hovered (SetVariable("whom", "Exit"))
        unhovered (SetVariable("whom", "Exit"))
        action [SetVariable("whom", ""), Hide("buttonExample"), Jump ("awayFromHere")]


    text whom

screen TOH_pause_menu():
    key [ 'mouseup_3' ] action Return()
    tag menu
    add "gui/main_menu.jpg"
    add "bg/bg black.png" alpha 0.8

    text "PAUSE MENU" xalign 0.485 yalign 0.09

    fixed:
        xpos 0.42
        ypos 0.01
        imagebutton:
            auto "gui/TOH_screens/settings/btn_exit_%s.png"
            action Return()
            xalign 0.01
            yalign 0.92
        fixed:
            textbutton _("{color=#ffffff}{size=25}Exit{/size}{/color}") xalign 0.055 yalign 0.916

style text_changelog_style:
    size 35
    outlines [ (3, "#000000", 0, 0)]

style text_changelog_style_button:
    size 35
    outlines [ (3, "#000000", 0, 0)]

default v_toh_changelog_total_pages = 2
default v_toh_changelog_page = 0
default v_toh_changelog_tab = 0

screen toh_changelog:
    add "bg_changelog"
    add "black" alpha 0.5
    tag menu
    vbox:
        xalign 0.5

        if v_toh_changelog_page == 0:
            text _("{size=40}{color=#0ea359}v0.0.3b (Episode 03){/color}{/size}") style "text_changelog_style"
            vbox:
                xalign 0.5
                hbox:
                    textbutton "{u}DESCRIPTION{/u}" action SetVariable ("v_toh_changelog_tab",0) text_outlines [ (2, "#000000", 0, 0)]
                    text "   "
                    textbutton "{u}TECHNICAL DETAILS{/u}" action SetVariable ("v_toh_changelog_tab",1) text_outlines [ (2, "#000000", 0, 0)]
                    text "   "
                    textbutton "{u}BUG FIXES{/u}" action SetVariable ("v_toh_changelog_tab",2) text_outlines [ (2, "#000000", 0, 0)]
                viewport:
                    xalign 0.5
                    yalign 0.2
                    xmaximum 1200
                    ymaximum 800
                    scrollbars "vertical"
                    mousewheel True
                    draggable True
                    if v_toh_changelog_tab == 0:
                        vbox:
                            xpos 100
                            text _("Welcome back to next instalment of {i}Thief of Hearts{/i}, where the thrilling journey of close calls and high-stakes tension continues!") style "text_changelog_style"
                            text _("") style "text_changelog_style"
                            text _("In this engaging third episode, you and the people you work with are preparing for the ultimate heist - stealing a famous painting from the local Art Gallery.") style "text_changelog_style"
                            text _("") style "text_changelog_style"
                            text _("But before you get to this point, you will have to make decisions on who you can trust, or who to keep your eye on. You may also be required to impersonate another person as part of the main goal and plan..") style "text_changelog_style"
                            text _("") style "text_changelog_style"
                            text _("Allies you have made can offer you some handy information or things you can use now or in the future. They may also tempt you so you can fulfil some of your innermost desires.") style "text_changelog_style"
                            text _("") style "text_changelog_style"
                            text _("There will always be options and chances where you can enhance your thieving skills while furthering your relationship with those close to you. ") style "text_changelog_style"
                            text _("") style "text_changelog_style"
                            text _("But it’s not just about being serious all the time. Being a thief can be a lot of fun too, whether that be trying on clothes with Ariel and Bella, being invited over to Zora’s lavish apartment in town, running into a familiar face at a local club or helping Vivian regain her confidence and self-esteem by showing her how much you care.") style "text_changelog_style"
                            text _("") style "text_changelog_style"
                            text _("Unlock the sexy side of these characters and you can enjoy the show!") style "text_changelog_style"
                            text _("") style "text_changelog_style"
                            text _("And there are also a couple of fun mini-games to look forward to during the main scene in this episode!") style "text_changelog_style"
                            text _("") style "text_changelog_style"
                            text _("This is the big job that you and the team have been working towards for a long time. And you only get one shot at getting it right, because one slip-up could mean ending up behind bars. ") style "text_changelog_style"
                            text _("") style "text_changelog_style"
                            text _("Know who to trust, back your instincts and above all else, don’t get caught! ") style "text_changelog_style"
                            text _("") style "text_changelog_style"
                    elif v_toh_changelog_tab == 1:
                        vbox:
                            xpos 100
                            text _("Scenes: 24+") style "text_changelog_style"
                            text _("Images: 2700+") style "text_changelog_style"
                            text _("Lewd Images: 100+") style "text_changelog_style"
                            text _("Animations: 90+") style "text_changelog_style"
                            text _("Sound FX Files: 38+") style "text_changelog_style"
                            text _("Music Files: 24+") style "text_changelog_style"
                            text _("") style "text_changelog_style"
                            text _("Some Sound FXs/Music were made with {a=https://suno.com/}Suno{/a}") style "text_changelog_style"
                    else:
                        vbox:
                            xpos 100
                            text _("{color=#0ea359}v0.0.3b{/color}") style "text_changelog_style"
                            text _("") style "text_changelog_style"
                            text _("01. Fixed the end game transfer logic to Part 2 to add a few more missing variables, and transfer over the settings from the vault so it does not need to be unlocked again.") style "text_changelog_style"
                            text _("") style "text_changelog_style"
                            text _("02. Fixed the method in which the tablet wallpapers were unlocked. Unlocked wallpapers you obtained should still be unlocked, but the order/numbering is now static so if any are missing, you will see a locked screen when selecting one.") style "text_changelog_style"
                            text _("") style "text_changelog_style"
                            text _("03. Fixed the animations from 0.0.3a that were redone but got placed in the wrong folder during the build process and the old videos never got overwritten.") style "text_changelog_style"
                            text _("") style "text_changelog_style"
                            text _("04. Fixed a few more spelling, grammar and script tweaks since the 0.0.3a update. (Thanks to everyone who reported them!)") style "text_changelog_style"
                            text _("") style "text_changelog_style"

                            text _("") style "text_changelog_style"
                            add "gui/TOH_screens/settings/separator.png" alpha 0.6 xalign 0.5
                            text _("") style "text_changelog_style"

                            text _("{color=#0ea359}v0.0.3a{/color}") style "text_changelog_style"
                            text _("") style "text_changelog_style"
                            text _("01. Fixed a missing animation for the Day 01 scene with Megan.") style "text_changelog_style"
                            text _("") style "text_changelog_style"
                            text _("02. Some fixes to point assignments during the Day 02 scene when the MC goes over to Zora\'s Place.") style "text_changelog_style"
                            text _("") style "text_changelog_style"
                            text _("03. Zora\'s pubic hair has grown back for the for the Day 02 scene when the MC goes over to Zora\'s Place.") style "text_changelog_style"
                            text _("") style "text_changelog_style"
                            text _("04. Various animations that were rendered at lower quality due to time constraints were re-rendered at higher quality for the Day 02 scene when the MC goes over to Zora\'s Place.") style "text_changelog_style"
                            text _("") style "text_changelog_style"
                            text _("05. Added some additional animations for Day 04 scene with [b_name] during the Maze Minigame.") style "text_changelog_style"
                            text _("") style "text_changelog_style"
                            text _("06. Fixed various spelling, grammar and script tweaks throughout the 0.0.3 update. (Thanks to everyone who reported them!)") style "text_changelog_style"
                            text _("") style "text_changelog_style"
                            text _("07. Added game transfer for Part 2 of Thief of Hearts and updated the build\'s name and UI elements, making this Part 1.") style "text_changelog_style"
                            text _("") style "text_changelog_style"

                            text _("") style "text_changelog_style"
                            add "gui/TOH_screens/settings/separator.png" alpha 0.6 xalign 0.5
                            text _("") style "text_changelog_style"

                            text _("{color=#0ea359}v0.0.3{/color}") style "text_changelog_style"
                            text _("") style "text_changelog_style"
                            text _("01. Zora review screen details fixed and now viewable.") style "text_changelog_style"
                            text _("") style "text_changelog_style"
                            text _("02. Zora animations added in where they were previously missing.") style "text_changelog_style"
                            text _("") style "text_changelog_style"
                            text _("03. Fixed minor errors in the game walkthrough with the directions for the Maze secret scene.") style "text_changelog_style"
                            text _("") style "text_changelog_style"
                            text _("04. Bonus scene featuring Officer Justice was not unlocking properly. That has been fixed now.") style "text_changelog_style"
                            text _("") style "text_changelog_style"
                            text _("05. Adjusted a missing sound effect during the changing room scene with [a_name].") style "text_changelog_style"
                            text _("") style "text_changelog_style"
                            text _("06. Various render graphic glitches that have been fixed or replaced.") style "text_changelog_style"


        if v_toh_changelog_page == 1:
            text _("{size=40}{color=#0ea359}v0.0.2a (Episode 02){/color}{/size}") style "text_changelog_style"
            vbox:
                xalign 0.5
                hbox:
                    textbutton "{u}DESCRIPTION{/u}" action SetVariable ("v_toh_changelog_tab",0) text_outlines [ (2, "#000000", 0, 0)]
                    text "   "
                    textbutton "{u}TECHNICAL DETAILS{/u}" action SetVariable ("v_toh_changelog_tab",1) text_outlines [ (2, "#000000", 0, 0)]
                    text "   "
                    textbutton "{u}BUG FIXES{/u}" action SetVariable ("v_toh_changelog_tab",2) text_outlines [ (2, "#000000", 0, 0)]
                viewport:
                    xalign 0.5
                    yalign 0.2
                    xmaximum 1200
                    ymaximum 800
                    scrollbars "vertical"
                    mousewheel True
                    draggable True
                    if v_toh_changelog_tab == 0:
                        vbox:
                            xpos 100
                            text _("Welcome back to Thief of Hearts, where the thrilling journey of close calls and high-stakes tension continues!") style "text_changelog_style"
                            text _("") style "text_changelog_style"
                            text _("In this gripping second episode, your resilience will be pushed to the limit, as will your mental strength while you navigate a very dangerous predicament to start off with.") style "text_changelog_style"
                            text _("") style "text_changelog_style"
                            text _("From being held a knifepoint to forming unlikely alliances, breaking and entering and cracking a safe, who knows what unexpected twists await our fearless young thief.") style "text_changelog_style"
                            text _("") style "text_changelog_style"
                            text _("As always, the people closest to you will either continue to show their loyalty, or further complicate things for you. These relationships are just another puzzle for you to solve, still with some missing pieces to be discovered.") style "text_changelog_style"
                            text _("") style "text_changelog_style"
                            text _("But remain focused on the ultimate goal: complete each job, and avoid being caught.") style "text_changelog_style"
                            text _("") style "text_changelog_style"
                            text _("Use your best instincts to navigate your way through not only the various challenges and interactions wth other characters, but your love life too!") style "text_changelog_style"
                            text _("") style "text_changelog_style"
                            text _("And most importantly, be careful who to trust, as one wrong decision could change everything...") style "text_changelog_style"
                            text _("") style "text_changelog_style"

                    elif v_toh_changelog_tab == 1:
                        vbox:
                            xpos 100
                            text _("Scenes: 20+") style "text_changelog_style"
                            text _("Images: 2700+") style "text_changelog_style"
                            text _("Lewd Images: 80") style "text_changelog_style"
                            text _("Animations: 40+") style "text_changelog_style"
                            text _("Sound FX Files: 34+") style "text_changelog_style"
                            text _("Music Files: 42+") style "text_changelog_style"
                            text _("") style "text_changelog_style"
                            text _("Some Sound FXs/Music were made with {a=https://suno.com/}Suno{/a}") style "text_changelog_style"
                    else:
                        vbox:
                            xpos 100
                            text _("{color=#0ea359}v0.0.2a{/color}") style "text_changelog_style"
                            text _("01. Various grammar and spelling fixes.") style "text_changelog_style"
                            text _("") style "text_changelog_style"
                            text _("02. Fixed the bug where the game returns to the main menu during the scene where the MC and Ariel are spying on Victor.") style "text_changelog_style"
                            text _("") style "text_changelog_style"
                            text _("03. Jump scene codes missing for one of the Zora options.") style "text_changelog_style"
                            text _("") style "text_changelog_style"
                            text _("04. Fixed an issue with Juliet fantasy scene not counting for the end of episode stat screen.") style "text_changelog_style"
                            text _("") style "text_changelog_style"
                            text _("05. Fixed a set of lines with one of Bella’s scenes coded incorrectly.") style "text_changelog_style"
                            text _("") style "text_changelog_style"
                            text _("06. Slight changes to previous dialogue or descriptions so the story all makes sense.") style "text_changelog_style"
                            text _("") style "text_changelog_style"
                            text _("07. Added extra variables to earlier choices that will apply to scenes in Episode 3 and beyond.") style "text_changelog_style"
                            text _("") style "text_changelog_style"
                            text _("08. Slight changes to the description for options for the In-Game WT.") style "text_changelog_style"
                            text _("") style "text_changelog_style"
                            text _("09. Fixed details for allocation of an Ariel Heart that wasn’t working properly.") style "text_changelog_style"
                            text _("") style "text_changelog_style"
                            text _("10. Fixed several quotation marks that weren’t applied correctly the first time.") style "text_changelog_style"
                            text _("") style "text_changelog_style"
                            text _("11. Adjusted the volume for sound FX and Music in various scenes.") style "text_changelog_style"
                            text _("") style "text_changelog_style"
                            text _("12. Fixed various renders, slight clippings on character clothing, body parts, etc.") style "text_changelog_style"
                            text _("") style "text_changelog_style"
                            text _("13. Fixed the length of time with images staying on the screen before the scene moves forward.") style "text_changelog_style"
                            text _("") style "text_changelog_style"
                            text _("14. Changed specific mp3 files to ogg, for better quality.") style "text_changelog_style"
                            text _("") style "text_changelog_style"
                            text _("15. Added some extra sound FX.") style "text_changelog_style"
                            text _("") style "text_changelog_style"
                            text _("16. Ariel date renders reworked (Better face expressions and poses).") style "text_changelog_style"

                            text _("") style "text_changelog_style"
                            add "gui/TOH_screens/settings/separator.png" alpha 0.6 xalign 0.5
                            text _("") style "text_changelog_style"

                            text _("{color=#0ea359}v0.0.2{/color}") style "text_changelog_style"
                            text _("01. Initial BETA release.") style "text_changelog_style"


        if v_toh_changelog_page == 2:
            text _("{size=40}{color=#0ea359}v0.0.1b (Episode 01){/color}{/size}") style "text_changelog_style"
            vbox:
                xalign 0.5
                hbox:
                    textbutton "{u}DESCRIPTION{/u}" action SetVariable ("v_toh_changelog_tab",0) text_outlines [ (2, "#000000", 0, 0)]
                    text "   "
                    textbutton "{u}TECHNICAL DETAILS{/u}" action SetVariable ("v_toh_changelog_tab",1) text_outlines [ (2, "#000000", 0, 0)]
                    text "   "
                    textbutton "{u}BUG FIXES{/u}" action SetVariable ("v_toh_changelog_tab",2) text_outlines [ (2, "#000000", 0, 0)]
                viewport:
                    xalign 0.5
                    yalign 0.2
                    xmaximum 1200
                    ymaximum 800
                    scrollbars "vertical"
                    mousewheel True
                    draggable True
                    if v_toh_changelog_tab == 0:
                        vbox:
                            xpos 100
                            text _("Welcome to Thief of Hearts: An electrifying saga where every choice shapes your destiny!") style "text_changelog_style"
                            text _("") style "text_changelog_style"
                            text _("In this thrilling first episode, you'll dive headfirst into the lives of our captivating characters. Discover their unique skills, uncover their vulnerabilities, and follow their daily routines—from their workplaces to their favorite pastimes.") style "text_changelog_style"
                            text _("") style "text_changelog_style"
                            text _("Forge alliances carefully as you navigate thrilling heists and hone your skills in the subtle art of thieving. Whether it’s a daring theft or a simple maneuver, your decisions will define success or failure.") style "text_changelog_style"
                            text _("") style "text_changelog_style"
                            text _("Trust is a rare commodity in this world. Some will aid your cause, while others may deceive. Take time to unravel their intentions before pledging loyalty or enmity.") style "text_changelog_style"
                            text _("") style "text_changelog_style"
                            text _("But beware: not everyone is what they seem. Some allies may hide darker intentions, while enemies could prove unexpectedly helpful. Take your time to unravel their motives before committing to alliances or rivalries.") style "text_changelog_style"
                            text _("") style "text_changelog_style"
                            text _("In addition to completing tasks crucial to your progress as the story unfolds, we’ve included several delightful extras and rewards. These include bonus 'hidden' scenes, an in-game walkthrough for assistance, and a collection of secret images that further showcase our stunning female characters.") style "text_changelog_style"
                            text _("") style "text_changelog_style"
                            text _("Note: Having access to some of these extras will depend on which tier amount subscription you are on. So, make sure to check out what each tier amount will give you.") style "text_changelog_style"
                            text _("") style "text_changelog_style"
                            text _("If you’re on the $20+ tier, you will gain access to everything!") style "text_changelog_style"
                            text _("") style "text_changelog_style"
                            text _("Join us on this exhilarating journey where every heartbeat counts and trust is your most valuable asset. Are you ready to steal the show?") style "text_changelog_style"
                    elif v_toh_changelog_tab == 1:
                        vbox:
                            xpos 100
                            text _("Scenes: 40+") style "text_changelog_style"
                            text _("Images: 5000+") style "text_changelog_style"
                            text _("Lewd Images: 132") style "text_changelog_style"
                            text _("Animations: 40+") style "text_changelog_style"
                            text _("Sound FX Files: 120+") style "text_changelog_style"
                            text _("Music Files: 60+") style "text_changelog_style"
                            text _("") style "text_changelog_style"
                            text _("Some Sound FXs/Music were made with {a=https://suno.com/}Suno{/a}") style "text_changelog_style"
                    else:
                        vbox:
                            xpos 100
                            text _("{color=#0ea359}v0.0.1b{/color}") style "text_changelog_style"
                            text _("01. Updated some renders at the end of the episode so the unknown female character is wearing the correct dress.") style "text_changelog_style"
                            text _("") style "text_changelog_style"
                            text _("02. Completely revamped the non-canon bonus scene with Megan and the limo driver.") style "text_changelog_style"
                            text _("") style "text_changelog_style"
                            text _("03. Various grammar and spelling fixes.") style "text_changelog_style"

                            text _("") style "text_changelog_style"
                            add "gui/TOH_screens/settings/separator.png" alpha 0.6 xalign 0.5
                            text _("") style "text_changelog_style"

                            text _("{color=#0ea359}v0.0.1a{/color}") style "text_changelog_style"
                            text _("01. Shortened the duration the Secret Scenes icon is visible to make it easier to narrow down the secret's location.") style "text_changelog_style"
                            text _("") style "text_changelog_style"
                            text _("02. Increased the Secret Scenes icon size, as well as changed the glow color to be more noticeable when the mouse is hovered over the secret location.") style "text_changelog_style"
                            text _("") style "text_changelog_style"
                            text _("03. Fixed an issue with the Secret Scenes toggles from not resetting correctly when the previous toggles were turned off.") style "text_changelog_style"
                            text _("") style "text_changelog_style"
                            text _("04. Fixed a bug where the achievements tab for Megan was not being properly unlocked so it could be viewed outside of a player's game. In order to view her achievements now, it will require you to play through the Day 2 scene when the MC first encounters Megan once more. After that, the tab will be correctly visible outside of a player's game.") style "text_changelog_style"
                            text _("") style "text_changelog_style"
                            text _("05. Fixed various issues where Victor's name and relationship were hard coded near the end of the update.") style "text_changelog_style"
                            text _("") style "text_changelog_style"
                            text _("06. Fixed a bug where if the player never unlocks the in-game walkthrough, it would cause two of the choice menu's during the game to throw an error.") style "text_changelog_style"
                            text _("") style "text_changelog_style"
                            text _("07. Fixed the vault code text so it's aligned correctly when entering codes") style "text_changelog_style"
                            text _("") style "text_changelog_style"
                            text _("08. Fixed the name and dialogue text from sometimes being outside the dialogue box.") style "text_changelog_style"
                            text _("") style "text_changelog_style"
                            text _("09. Fixed issues with the Android release and text not being aligned properly. Also added the options to adjust the name and dialogue text alignment.") style "text_changelog_style"
                            text _("") style "text_changelog_style"
                            text _("10. Many renders from different scenes had visual bugs that been corrected.") style "text_changelog_style"
                            text _("") style "text_changelog_style"
                            text _("11. Various fixes were made to the script where dialogue was inconsistent between events, the incorrect words were used, lines were duplicated, spelled wrong, or had bad formatting.") style "text_changelog_style"

                            text _("") style "text_changelog_style"
                            add "gui/TOH_screens/settings/separator.png" alpha 0.6 xalign 0.5
                            text _("") style "text_changelog_style"

                            text _("{color=#0ea359}v0.0.1{/color}") style "text_changelog_style"
                            text _("01. Initial BETA release.") style "text_changelog_style"
    if v_toh_changelog_page > 0:
        hbox:
            xpos 0.2
            ypos 0.9
            textbutton "NEWER" action SetVariable ("v_toh_changelog_page", v_toh_changelog_page - 1) text_outlines [ (2, "#000000", 0, 0)]

    if v_toh_changelog_page < v_toh_changelog_total_pages:
        hbox:
            xpos 0.7
            ypos 0.9
            textbutton "OLDER" action SetVariable ("v_toh_changelog_page", v_toh_changelog_page + 1) text_outlines [ (2, "#000000", 0, 0)]

    imagebutton:
        xalign 0.01
        yalign 0.98
        auto "btn_mm_back_%s" action Return()



screen toh_support():
    tag menu
    add "bg_support"
    add "black" alpha 0.3


    if renpy.variant("small"):
        viewport:
            xalign 0.2
            yalign 0.2
            scrollbars "vertical"
            mousewheel True
            draggable True
            xmaximum 1700
            ymaximum 800
            has vbox:
                xalign 0.2
                yalign 0.2
            text _("{size=50}{color=#0ea359}SUPPORT OUR WORK!{/color}{/size}") style "text_about_style"
            text _("")
            text _("Thank you so much for playing our new visual novel!") style "text_about_style_small"
            text _("To be able to continue creating Adult games for a living, we rely on paying subscribers to develop projects just like Thief of Hearts.") style "text_about_style_small"
            text _("So if you enjoyed what you have seen, we’d like to invite you to join several other thousands of MrDotsGames subscribers.") style "text_about_style_small"
            text _("")
            text _("{size=50}{color=#0ea359}OUR TIER SYSTEM{/color}{/size}") style "text_about_style_small"
            text _("")
            text _("For as little as $1US a month, you can get access to frequent content that we share through our two main platforms - Patreon and Subcribestar.") style "text_about_style_small"
            text _("Other tiers contain cool inclusions such as bonus images, animations, wallpaper images, game walkthroughs and cheat codes.") style "text_about_style_small"
            text _("The higher the tier that you subscribe to, the more you get!") style "text_about_style_small"
            text _("Please check out our subscription pages for more details on what you get for each tier amount.") style "text_about_style_small"
            text _("")
            text _("Patreon: {a=https://www.patreon.com/mrdotsgames/}https://www.patreon.com/mrdotsgames/{/a}") style "text_about_style_small"
            text _("Subscribestar: {a=https://subscribestar.adult/mrdotsgames}https://subscribestar.adult/mrdotsgames{/a}") style "text_about_style_small"
            text _("")
            text _("{u}Social Media:{/u}") style "text_about_style_small"
            text _("You can follow us here on all of our socials at: {a=https://linktr.ee/mrdotsgames}https://linktr.ee/mrdotsgames{/a}") style "text_about_style_small"
            text _("{a=https://x.com/mrdotsgames}X(Twitter){/a} / {a=https://www.instagram.com/mrdots_games/}Instagram{/a} / {a=https://www.youtube.com/channel/UCXYrwcINrN-Q8YbVdS5Q_vg}YouTube{/a} / {a=https://discord.gg/JbyH5HUnBh}Discord{/a}") style "text_about_style_small"
            text _("To get the latest updates, you can follow our website blog here: {a=https://mrdotsgames.com/blog/}https://mrdotsgames.com/blog/{/a}") style "text_about_style_small"
            text _("Scroll down to the bottom right-hand side of the page, enter your email and click 'Follow Me'. ") style "text_about_style_small"
            text _("Go ahead, it’s free to subscribe!") style "text_about_style_small"

    else:
        vbox:
            xalign 0.2
            yalign 0.2
            text _("{size=40}{color=#0ea359}SUPPORT OUR WORK!{/color}{/size}") style "text_about_style"
            text _("")
            text _("Thank you so much for playing our new visual novel!") style "text_about_style"
            text _("To be able to continue creating Adult games for a living, we rely on paying subscribers to develop projects just like Thief of Hearts.") style "text_about_style"
            text _("So if you enjoyed what you have seen, we’d like to invite you to join several other thousands of MrDotsGames subscribers.") style "text_about_style"
            text _("")
            text _("{size=40}{color=#0ea359}OUR TIER SYSTEM{/color}{/size}") style "text_about_style"
            text _("")
            text _("For as little as $1US a month, you can get access to frequent content that we share through our two main platforms - Patreon and Subcribestar.") style "text_about_style"
            text _("Other tiers contain cool inclusions such as bonus images, animations, wallpaper images, game walkthroughs and cheat codes.") style "text_about_style"
            text _("The higher the tier that you subscribe to, the more you get!") style "text_about_style"
            text _("Please check out our subscription pages for more details on what you get for each tier amount.") style "text_about_style"
            text _("")
            text _("Patreon: {a=https://www.patreon.com/mrdotsgames/}https://www.patreon.com/mrdotsgames/{/a}") style "text_about_style"
            text _("Subscribestar: {a=https://subscribestar.adult/mrdotsgames}https://subscribestar.adult/mrdotsgames{/a}") style "text_about_style"
            text _("")
            text _("{u}Social Media:{/u}") style "text_about_style"
            text _("You can follow us here on all of our socials at: {a=https://linktr.ee/mrdotsgames}https://linktr.ee/mrdotsgames{/a}") style "text_about_style"
            text _("{a=https://x.com/mrdotsgames}X(Twitter){/a} / {a=https://www.instagram.com/mrdots_games/}Instagram{/a} / {a=https://www.youtube.com/channel/UCXYrwcINrN-Q8YbVdS5Q_vg}YouTube{/a} / {a=https://discord.gg/JbyH5HUnBh}Discord{/a}") style "text_about_style"
            text _("To get the latest updates, you can follow our website blog here: {a=https://mrdotsgames.com/blog/}https://mrdotsgames.com/blog/{/a}") style "text_about_style"
            text _("Scroll down to the bottom right-hand side of the page, enter your email and click 'Follow Me'. ") style "text_about_style"
            text _("Go ahead, it’s free to subscribe!") style "text_about_style"


    imagebutton:
        xalign 0.01
        yalign 0.98
        auto "btn_mm_back_%s" action Return()

















define gui.choice_button_text_outlines = [( 2, "#292929", 0, 0 )]

style generic_button_style:
    yoffset 20
    xoffset 100
    size 40
    color "#fff"

style generic_button_style_outline:
    yoffset 20
    xoffset 100
    size 40
    color "#fff"
    outlines [ (3, "#000000", 0, 0) ]

screen my_exit_screen:
    add "images/bg/exit2.jpg"
    add "bg black" alpha 0.6
    text "Are you sure you want to quit?":
        size 70 xalign 0.5 yalign 0.5
        outlines [( 2, "#292929", 0, 0 )]
    hbox:
        xalign 0.5
        yalign 0.8
        spacing 400
        imagebutton:
            auto "gui/menu_buttons/btn_generic_%s.png"
            foreground Text(_("YES"),style="generic_button_style")
            action yes_action
        imagebutton:
            auto "gui/menu_buttons/btn_generic_%s.png"
            foreground Text(_("NO"),style="generic_button_style")
            action no_action



style tx_button:
    color "#ffffff"
    hover_color "#d9c23e"
    outlines [ (2, "#000000", 0, 0) ]



screen scr_ep01_09_01_quiz_choice(items):


    vbox:
        xalign 0.5
        yalign 0.5
        spacing 100
        xsize 500
        vbox:
            xalign 0.5
            spacing 100
            for i in items:

                textbutton ("{size=50}%s\n{/size} {color=#33ff33}(%s){/color}" % (i.caption, i.kwargs["wt"]) if persistent.v_walkthrough_enabled and i.kwargs.get('wt') else i.caption) action i.action text_style "tx_button"


screen scr_ep01_09_01_quiz_choice_small(items):


    vbox:
        xalign 0.5
        yalign 0.5
        spacing 100
        xsize 400
        vbox:
            xalign 0.5
            spacing 100
            for i in items:

                textbutton ("{size=40}%s\n {color=#33ff33}(%s){/color}{/size}" % (i.caption, i.kwargs["wt"]) if persistent.v_walkthrough_enabled and i.kwargs.get('wt') else i.caption) action i.action text_style "tx_button"






screen scr_tobecontinued_01:
    modal True
    timer 3 action [Hide("scr_tobecontinued_01"), Jump("lb_review_end_01")]
    imagebutton idle "bg tobecontinued" action [Hide("scr_tobecontinued_01"), Jump("lb_review_end_01")]


label lb_chapter_end_01:
    window hide
    $ quick_menu = False
    call screen scr_tobecontinued_01



label lb_chapter_end_02:
    window hide
    $ quick_menu = False
    call screen scr_tobecontinued_02

screen scr_tobecontinued_02:
    modal True
    timer 3 action [Hide("scr_tobecontinued_02"), Jump("lb_review_end_02")]
    imagebutton idle "bg tobecontinued" action [Hide("scr_tobecontinued_02"), Jump("lb_review_end_02")]

label lb_chapter_end_03:
    window hide
    $ quick_menu = False
    call screen scr_tobecontinued_03

screen scr_tobecontinued_03:
    modal True
    timer 3 action [Hide("scr_tobecontinued_03"), Jump("lb_review_end_03")]
    imagebutton idle "bg tobecontinued" action [Hide("scr_tobecontinued_03"), Jump("lb_review_end_03")]





style text_endofversion_style:
    size 30
    outlines [ (3, "#000000", 0, 0)]

label lb_end_of_version:

    if v_review_episode == 3:
        $ quick_menu = False
        show screen_transfer
        $ v_transfer_name = renpy.input("This is the end of Part 1. Enter a name for this playthrough to save its choices for transfer to Part 2, or leave blank to skip:")
        if v_transfer_name:
            if v_transfer_name in tohpart1.part1_part2_transfer:
                menu:
                    "You've already transferred a playthrough with that name. Would you like to overwrite it?"
                    "Yes":
                        pass
                    "No":
                        call screen scr_endofversion
            $ tohpart1.part1_part2_transfer[v_transfer_name] = {

                'justice_love_level': justice_love_level,
                'ariel_love_level': ariel_love_level,
                'bella_love_level': bella_love_level,
                'vivian_love_level': vivian_love_level,
                'megan_love_level': megan_love_level,
                'juliet_love_level': juliet_love_level,
                'zora_love_level': zora_love_level,
                'megan_known': megan_known,
                'juliet_known': juliet_known,
                'zora_known': zora_known,

                'y_name': y_name,
                'b_name': b_name,
                'a_name': a_name,
                'v_name': v_name,
                'vic_name': vic_name,
                'lastname': lastname,
                'y_lastname': y_lastname,
                'mc_a_rel': mc_a_rel,
                'a_mc_rel': a_mc_rel,
                'mc_b_rel': mc_b_rel,
                'b_mc_rel': b_mc_rel,
                'v_mc_rel': v_mc_rel,
                'mc_v_rel': mc_v_rel,
                'vic_mc_rel': vic_mc_rel,
                'mc_vic_rel': mc_vic_rel,
                'mc_a_b_rel': mc_a_b_rel,
                'mc_v_vic_rel': mc_v_vic_rel,


                'mc_a_address': mc_a_address,
                'a_mc_address': a_mc_address,
                'mc_b_address': mc_b_address,
                'b_mc_address': b_mc_address,

                'v_pre_address': v_pre_address,
                'vic_pre_address': vic_pre_address,

                'mc_v_address': mc_v_address,
                'mc_vic_address': mc_vic_address,

                'private_group': private_group,
                'public_group': public_group,

                'name': name,
                'address': address,
                'address2': address2,
                'lname': lname,
                'rel': rel,
                'rel2': rel2,
                'var_name': var_name,
                'stored_input': stored_input,
                'show_default_value': show_default_value,

                'v_ep01_03_03_Outside_Ariels_Room': v_ep01_03_03_Outside_Ariels_Room,
                'v_ep01_04_01_Bella_Work_Date': v_ep01_04_01_Bella_Work_Date,
                'v_ep01_05_01_Ariels_Work_Date': v_ep01_05_01_Ariels_Work_Date,
                'v_ep01_06_01_Vivian_Work_Date': v_ep01_06_01_Vivian_Work_Date,
                'v_ep01_06_02_Tattoo_Parlour_Tip': v_ep01_06_02_Tattoo_Parlour_Tip,

                'v_ep01_09_01_Mikayla_Sex_path': v_ep01_09_01_Mikayla_Sex_path,
                'v_ep01_09_01_Tasha_and_Mikayla_Sex_path': v_ep01_09_01_Tasha_and_Mikayla_Sex_path,
                'v_ep01_09_01_Tasha_Sex_path': v_ep01_09_01_Tasha_Sex_path,

                'v_ep01_13_03_Ariels_Room': v_ep01_13_03_Ariels_Room,

                'v_ep02_01_04_Switch_The_Drives': v_ep02_01_04_Switch_The_Drives,
                'v_ep02_01_04_Leave_a_Note': v_ep02_01_04_Leave_a_Note,

                'v_ep02_03_09_mc_tattoo_girl_finishing_location': v_ep02_03_09_mc_tattoo_girl_finishing_location,

                'v_ep02_04_01_megan_work_with_her': v_ep02_04_01_megan_work_with_her,

                'v_ep03_megan_oral_sex': v_ep03_megan_oral_sex,
                'v_ep03_Room_Search_Took_Photo': v_ep03_Room_Search_Took_Photo,

                'v_ep3_sex_with_Zora': v_ep3_sex_with_Zora,

                'v_ep03_03_04_lucy_kiss': v_ep03_03_04_lucy_kiss,

                'v_ep03_01_01_megan_beating_guy': v_ep03_01_01_megan_beating_guy,

                'v_mm_background': persistent.v_mm_background,

                'v_mm_custom_background': persistent.v_mm_custom_background,

                'v_mm_background_slot3': persistent.v_mm_background_slot3,
                'v_mm_background_slot4': persistent.v_mm_background_slot4,
                'v_mm_background_slot5': persistent.v_mm_background_slot5,



                'v_stats_task_1': v_stats_task_1,
                'v_stats_task_2': v_stats_task_2,
                'v_stats_task_3': v_stats_task_3,
                'v_stats_task_4': v_stats_task_4,
                'v_stats_task_5': v_stats_task_5,
                'v_stats_task_6': v_stats_task_6,
                'v_stats_task_7': v_stats_task_7,
                'v_stats_task_8': v_stats_task_8,
                'v_stats_task_9': v_stats_task_9,
                'v_stats_task_10': v_stats_task_10,
                'v_stats_task_11': v_stats_task_11,
                'v_stats_task_12': v_stats_task_12,
                'v_stats_task_13': v_stats_task_13,
                'v_stats_task_14': v_stats_task_14,
                'v_stats_task_15': v_stats_task_15,
                'v_stats_task_16': v_stats_task_16,
                'v_stats_task_17': v_stats_task_17,
                'v_stats_task_18': v_stats_task_18,
                'v_stats_task_19': v_stats_task_19,
                'v_stats_task_20': v_stats_task_20,
                'v_stats_task_21': v_stats_task_21,
                'v_stats_task_22': v_stats_task_22,
                'v_stats_task_23': v_stats_task_23,
                'v_stats_task_24': v_stats_task_24,
                'v_stats_task_25': v_stats_task_25,
                'v_stats_task_26': v_stats_task_26,


                'v_stats_task_1_completed': v_stats_task_1_completed,
                'v_stats_task_2_completed': v_stats_task_2_completed,
                'v_stats_task_3_completed': v_stats_task_3_completed,
                'v_stats_task_4_completed': v_stats_task_4_completed,
                'v_stats_task_5_completed': v_stats_task_5_completed,
                'v_stats_task_6_completed': v_stats_task_6_completed,
                'v_stats_task_7_completed': v_stats_task_7_completed,
                'v_stats_task_8_completed': v_stats_task_8_completed,
                'v_stats_task_9_completed': v_stats_task_9_completed,
                'v_stats_task_10_completed': v_stats_task_10_completed,
                'v_stats_task_11_completed': v_stats_task_11_completed,
                'v_stats_task_12_completed': v_stats_task_12_completed,
                'v_stats_task_13_completed': v_stats_task_13_completed,
                'v_stats_task_14_completed': v_stats_task_14_completed,
                'v_stats_task_15_completed': v_stats_task_15_completed,
                'v_stats_task_16_completed': v_stats_task_16_completed,
                'v_stats_task_17_completed': v_stats_task_17_completed,
                'v_stats_task_18_completed': v_stats_task_18_completed,
                'v_stats_task_19_completed': v_stats_task_19_completed,
                'v_stats_task_20_completed': v_stats_task_20_completed,
                'v_stats_task_21_completed': v_stats_task_21_completed,
                'v_stats_task_22_completed': v_stats_task_22_completed,
                'v_stats_task_23_completed': v_stats_task_23_completed,
                'v_stats_task_24_completed': v_stats_task_24_completed,
                'v_stats_task_25_completed': v_stats_task_25_completed,
                'v_stats_task_26_completed': v_stats_task_26_completed,



                'v_stats_poi_1': v_stats_poi_1,
                'v_stats_poi_2': v_stats_poi_2,
                'v_stats_poi_3': v_stats_poi_3,
                'v_stats_poi_4': v_stats_poi_4,
                'v_stats_poi_5': v_stats_poi_5,
                'v_stats_poi_6': v_stats_poi_6,
                'v_stats_poi_7': v_stats_poi_7,
                'v_stats_poi_8': v_stats_poi_8,


                'v_stats_future_tasks_1': v_stats_future_tasks_1,
                'v_stats_future_tasks_2': v_stats_future_tasks_2,
                'v_stats_future_tasks_3': v_stats_future_tasks_3,
                'v_stats_future_tasks_4': v_stats_future_tasks_4,
                'v_stats_future_tasks_5': v_stats_future_tasks_5,
                'v_stats_future_tasks_6': v_stats_future_tasks_6,
                'v_stats_future_tasks_7': v_stats_future_tasks_7,
                'v_stats_future_tasks_8': v_stats_future_tasks_8,




                'v_stats_task_1_rating': v_stats_task_1_rating,
                'v_stats_task_2_rating': v_stats_task_2_rating,
                'v_stats_task_3_rating': v_stats_task_3_rating,
                'v_stats_task_4_rating': v_stats_task_4_rating,
                'v_stats_task_5_rating': v_stats_task_5_rating,
                'v_stats_task_6_rating': v_stats_task_6_rating,
                'v_stats_task_7_rating': v_stats_task_7_rating,
                'v_stats_task_8_rating': v_stats_task_8_rating,
                'v_stats_task_9_rating': v_stats_task_9_rating,
                'v_stats_task_10_rating': v_stats_task_10_rating,
                'v_stats_task_11_rating': v_stats_task_11_rating,
                'v_stats_task_12_rating': v_stats_task_12_rating,
                'v_stats_task_13_rating': v_stats_task_13_rating,
                'v_stats_task_14_rating': v_stats_task_14_rating,
                'v_stats_task_15_rating': v_stats_task_15_rating,
                'v_stats_task_16_rating': v_stats_task_16_rating,
                'v_stats_task_17_rating': v_stats_task_17_rating,
                'v_stats_task_18_rating': v_stats_task_18_rating,
                'v_stats_task_19_rating': v_stats_task_19_rating,
                'v_stats_task_20_rating': v_stats_task_20_rating,
                'v_stats_task_21_rating': v_stats_task_21_rating,
                'v_stats_task_22_rating': v_stats_task_22_rating,
                'v_stats_task_23_rating': v_stats_task_23_rating,
                'v_stats_task_24_rating': v_stats_task_24_rating,
                'v_stats_task_25_rating': v_stats_task_25_rating,
                'v_stats_task_26_rating': v_stats_task_26_rating,

                'v_ep01_mansionhall_vivian': v_ep01_mansionhall_vivian,
                'v_ep02_03_08_fitness_session_with_juliet_fight': v_ep02_03_08_fitness_session_with_juliet_fight,
                'v_ep02_03_08_fitness_session_with_juliet_fight_win': v_ep02_03_08_fitness_session_with_juliet_fight_win,
                'v_ep02_03_01_Dream_Choice': v_ep02_03_01_Dream_Choice,


                'v_ep01_vivian_respect_counter': v_ep01_vivian_respect_counter,
                'v_ep01_vivian_cocky_counter': v_ep01_vivian_cocky_counter,
                'v_ep01_vivian_arrogant_counter': v_ep01_vivian_arrogant_counter,
                'v_ep01_vivian_dates_counter': v_ep01_vivian_dates_counter,
                'vivian_harem_points_counter': vivian_harem_points_counter,
                'v_ep03_vivian_hearts_counter': v_ep03_vivian_hearts_counter,

                'v_ep01_bella_respect_counter': v_ep01_bella_respect_counter,
                'v_ep01_bella_cocky_counter': v_ep01_bella_cocky_counter,
                'v_ep01_bella_arrogant_counter': v_ep01_bella_arrogant_counter,
                'v_ep02_bella_fantasy_counter': v_ep02_bella_fantasy_counter,
                'v_ep03_bella_fantasy_counter': v_ep03_bella_fantasy_counter,
                'v_ep01_bella_dates_counter': v_ep01_bella_dates_counter,
                'bella_harem_points_counter': bella_harem_points_counter,

                'v_ep01_ariel_respect_counter': v_ep01_ariel_respect_counter,
                'v_ep01_ariel_cocky_counter': v_ep01_ariel_cocky_counter,
                'v_ep01_ariel_arrogant_counter': v_ep01_ariel_arrogant_counter,
                'v_ep02_ariel_fantasy_counter': v_ep02_ariel_fantasy_counter,
                'v_ep03_ariel_fantasy_counter': v_ep03_ariel_fantasy_counter,
                'v_ep01_ariel_dates_counter': v_ep01_ariel_dates_counter,
                'v_ep02_ariel_dates_counter': v_ep02_ariel_dates_counter,
                'v_ep02_ariel_hearts_counter': v_ep02_ariel_hearts_counter,
                'v_ep03_ariel_hearts_counter': v_ep03_ariel_hearts_counter,
                'ariel_harem_points_counter': ariel_harem_points_counter,

                'v_ep01_megan_respect_counter': v_ep01_megan_respect_counter,
                'v_ep01_megan_cocky_counter': v_ep01_megan_cocky_counter,
                'v_ep01_megan_arrogant_counter': v_ep01_megan_arrogant_counter,
                'v_ep03_megan_respect_counter': v_ep03_megan_respect_counter,
                'v_ep03_megan_cocky_counter': v_ep03_megan_cocky_counter,
                'v_ep03_megan_arrogant_counter': v_ep03_megan_arrogant_counter,
                'v_ep03_megan_fantasy_counter': v_ep03_megan_fantasy_counter,
                'v_ep01_megan_dates_counter': v_ep01_megan_dates_counter,

                'v_ep01_zora_respect_counter': v_ep01_zora_respect_counter,
                'v_ep01_zora_cocky_counter': v_ep01_zora_cocky_counter,
                'v_ep01_zora_arrogant_counter': v_ep01_zora_arrogant_counter,
                'v_ep02_zora_fantasy_counter': v_ep02_zora_fantasy_counter,

                'v_ep01_juliet_respect_counter': v_ep01_juliet_respect_counter,
                'v_ep01_juliet_cocky_counter': v_ep01_juliet_cocky_counter,
                'v_ep01_juliet_arrogant_counter': v_ep01_juliet_arrogant_counter,
                'v_ep02_juliet_fantasy_counter': v_ep02_juliet_fantasy_counter,

                'v_ep03_justice_fantasy_counter': v_ep03_justice_fantasy_counter,
                'v_ep03_othergirls_fantasy_counter': v_ep03_othergirls_fantasy_counter,
                'v_ep03_othergirls_dates_counter': v_ep03_othergirls_dates_counter,

                'v_ep03_othergirls_dates_counter': v_ep03_othergirls_dates_counter,

                'per_v_walkthrough_locked': persistent.v_walkthrough_locked,
                'per_v_walkthrough_enabled': persistent.v_walkthrough_enabled,
                'per_v_lewd_images_extra_locked': persistent.v_lewd_images_extra_locked,
                'per_v_lewd_images_extra_enabled': persistent.v_lewd_images_extra_enabled,
                'per_v_anim_enabled': persistent.v_anim_enabled,
                'per_v_sex_anim_enabled_locked': persistent.v_sex_anim_enabled_locked,
                'per_v_sex_anim_enabled': persistent.v_sex_anim_enabled,
                'per_v_secrets_locked': persistent.v_secrets_locked,
                'per_v_secrets_enabled': persistent.v_secrets_enabled,
                'per_v_secrets_icon_enabled': persistent.v_secrets_icon_enabled,
                'per_v_secrets_reappear': persistent.v_secrets_reappear

            }

            python:
                try:
                    tohpart1.save()
                except:
                    v_part1_part2_transfer_failed = True
            if v_part1_part2_transfer_failed:
                $ renpy.choice_for_skipping()
                "Your choices could not be transferred automatically. This is common on Android and does not indicate a problem with your device. Please save your game now, and then manually copy it to Part 2's saves directory."

        scene black
        with dissolve
        scene black
        with Pause (2)
        call screen scr_endofversion
    else:





        scene black
        with dissolve
        scene black
        with Pause (2)
        call screen scr_endofversion

screen scr_endofversion:

    modal True
    add "bg_end_of_version"
    add Solid("#000000") alpha 0.5
    vbox:
        xmaximum 1200
        xalign 0.5
        yalign 0.25
        text _("{size=40}{color=#0ea359}THANK YOU FOR PLAYING!{/color}{/size}") xalign 0.5 style "text_endofversion_style"
        text _("")
        text _("The team and I would like to say a huge thank you to every single one of you for playing our new game Thief of Hearts and for supporting us with any of our other projects since we started creating visual novels (way back in September 2016).") style "text_endofversion_style"
        text _("") style "text_endofversion_style"
        text _("We hope you will continue to follow and support us during our journey.") style "text_endofversion_style"
        text _("These games are created for you more than anyone else, and without your financial support, patience and feedback, none of this would be possible.") style "text_endofversion_style"
        text _("We always strive to make the best games possible and to always complete them. ") style "text_endofversion_style"
        text _("A special thanks to anyone who has helped us out during the creation of:") style "text_endofversion_style"
        text _("") style "text_endofversion_style"
        add "toh_logo" xalign 0.5
        text _("") style "text_endofversion_style"
        text _("               Follow and support us by checking out our various socials below:") style "text_endofversion_style"

    text _("{a=https://mrdotsgames.com/}OFFICIAL SITE{/a} / {a=https://www.patreon.com/mrdotsgames/}PATREON{/a} / {a=https://subscribestar.adult/mrdotsgames}SUBSCRIBESTAR{/a} / {a=https://www.spicygaming.net/team/@Mr.%20Dots%20Games/games}SPICYGAMING{/a} / {a=https://x.com/mrdotsgames}X(TWITTER){/a} / {a=https://www.instagram.com/mrdots_games/}INSTAGRAM{/a} / {a=https://discord.gg/JbyH5HUnBh}DISCORD{/a} / {a=https://www.youtube.com/@mrdotsgames}YOUTUBE{/a}") xalign 0.5 yalign 0.87 style "text_endofversion_style"

    textbutton _("{size=50}MAIN MENU{/size}") action MainMenu(confirm=False) xalign 0.5 yalign 0.97 text_style "char_info_button"













screen scr_ep03_levers_screen:

    modal True
    add "bg/levers/levers_background.jpg"
    add Solid("#000000") alpha 0.5
    vbox:
        xmaximum 1200
        xalign 0.5
        yalign 0.20
        text _("{size=40}{color=#0ea359}LASER BEAM MINI-GAME{/color}{/size}") xalign 0.5 style "text_endofversion_style"
        text _("")
        text _("When the game starts you will see a panel with nine red buttons.") style "text_endofversion_style"
        text _("Here you will need to select the correct buttons to turn the laser beams off.") style "text_endofversion_style"
        text _("")
        text _("The buttons run from left to right, top to bottom, in order from 1 to 9.") style "text_endofversion_style"
        text _("Therefore, the top row would be 1-2-3, middle row is 4-5-6, and the bottom row 7-8-9.") style "text_endofversion_style"
        text _("")
        text _("If the panel is still showing any red buttons, you can select “Reset the mini-game” at the top left-corner of the screen to start again.") style "text_endofversion_style"
        text _("")
        text _("HINT: It's possible to light up all of the buttons to green with your first four choices.") style "text_endofversion_style"
        text _("")
        text _("If you want to skip the mini-game, choose that option which is also at the top of the screen.") style "text_endofversion_style"
        text _("However, you will unlock a bonus render of Bella if you beat the mini-game. It will be in the Wallpaper menu.") style "text_endofversion_style"
        text _("")
        text _("Best of luck!") style "text_endofversion_style"

    textbutton _("{size=50}PROCEED WITH THE MINI-GAME{/size}") action [Hide("scr_ep03_levers_screen"),SetVariable("v_ep03_04_03_levers_minigame", True),Jump("lb_ep3_levers_minigame")] xalign 0.5 yalign 0.97 text_style "char_info_button"


screen scr_ep03_maze_screen:
    modal True
    add "bg/levers/levers_background.jpg"
    add Solid("#000000") alpha 0.5
    vbox:
        xmaximum 1200
        xalign 0.5
        yalign 0.20
        text _("{size=40}{color=#0ea359}MAZE MINI-GAME{/color}{/size}") xalign 0.5 style "text_endofversion_style"
        text _("")
        text _("")
        text _("When the game starts you will be given various options with directions on the screen to choose from.") style "text_endofversion_style"
        text _("These directions will move you through a door and into the next room.") style "text_endofversion_style"
        text _("")
        text _("You will need to choose the correct option - “Go North/East/West/South” - until you exit the maze.") style "text_endofversion_style"
        text _("")
        text _("If you want to skip the mini-game, choose the “Give up” option.") style "text_endofversion_style"
        text _("However, you will unlock a bonus render of Bella if you beat the mini-game.") style "text_endofversion_style"
        text _("It will be in the Wallpaper menu.") style "text_endofversion_style"
        text _("")
        text _("We've also hidden a Non-Canon scene in one of the rooms to find, somewhere in the maze.") style "text_endofversion_style"
        text _("")
        text _("Best of luck!") style "text_endofversion_style"

    textbutton _("{size=50}PROCEED WITH THE MINI-GAME{/size}") action [Hide("scr_ep03_maze_screen"),SetVariable("v_ep03_04_03_maze_minigame", True),Jump("lb_ep03_04_03_Maze_Minigame")] xalign 0.5 yalign 0.97 text_style "char_info_button"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

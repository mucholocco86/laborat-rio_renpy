default persistent.text_offset = 1

define gui.notify_ypos = 180
define gui.notify_text_size = 32

style say_dialogue:
    properties gui.text_properties("dialogue")
    line_spacing 3
    xpos gui.dialogue_xpos

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    xpos -4
    yalign 0.5

style choice_button_text is default:
    outlines [ (1.5, '#000000', 1, 1)]

    properties gui.button_text_properties("choice_button")

screen say(who, what):
    style_prefix "say"

    window:
        id "window"
        if persistent.quick_menu:
            # 32 = Height of the quick menu
            ypos 1080 - persistent.textbox_height - 32
        else:
            ypos 1080 - persistent.textbox_height
        xsize persistent.textbox_width + 274
        ysize persistent.textbox_height
        background Frame(Transform("gui/textbox.png", alpha=persistent.textbox_opacity))

        vbox:
            xpos gui.name_xpos
            ypos 40
            xsize persistent.textbox_width
            spacing 15

            if who is not None:

                window:
                    id "namebox"
                    style "namebox"
                    text who id "who" outlines [ (1.5, "#000", 0, 0) ]

            text what id "what":
                size persistent.text_size
                outlines [ (absolute(persistent.text_outline), "#000", absolute(persistent.text_offset), absolute(persistent.text_offset)) ]

screen preferences():

    tag menu

    key 'game_menu' action Return()

    add "gui/msp5/pref_bg.png"
    label _("{color=#f1f1f1}{size=100}PREFERENCES") xpos 110 ypos 25

    default edit_mode   = False

    viewport:
        xsize 1060
        ysize 721
        xpos 140
        ypos 219
        scrollbars "vertical"
        mousewheel True
        draggable True
        pagekeys True
        vbox:
            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:

                    label _("Text Speed")

                    bar value Preference("text speed")

                    label _("Auto-Forward Time")

                    bar value Preference("auto-forward time")
            null height (4 * gui.pref_spacing)
            hbox:
                style_prefix "slider"
                vbox:

                    if config.has_music:
                        label _("Music Volume")

                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:

                        label _("Sound Volume")

                        hbox:
                            bar value Preference("sound volume")

                            if config.sample_sound:
                                textbutton _("Test") action Play("sound", config.sample_sound)


                    #if config.has_voice:
                        #label _("Voice Volume")
                        #hbox:
                        #    bar value Preference("voice volume")
                        #    if config.sample_voice:
                        #        textbutton _("Test") action Play("voice", config.sample_voice)

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        textbutton _("Mute All"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"

            null height (4 * gui.pref_spacing)

            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:
                    label _("Text Size ([persistent.text_size]/50)")
                    bar:
                        value FieldValue(persistent, "text_size", offset=20, range=30, style="slider")
                    textbutton _("Set to default") action InvertSelected(SetVariable("persistent.text_size", gui.text_size))


                    label _("Text Outline ([persistent.text_outline]/4)")
                    bar:
                        value FieldValue(persistent, "text_outline", range=4, style="slider")
                    textbutton _("Set to default") action InvertSelected(SetVariable("persistent.text_outline", 2))

                    label _("Text Outline Offset ([persistent.text_offset]/4)")
                    bar:
                        value FieldValue(persistent, "text_offset", range=4, style="slider")
                    textbutton _("Set to default") action InvertSelected(SetVariable("persistent.text_offset", 1))

            null height (4 * gui.pref_spacing)
            hbox:
                style_prefix "slider"
                vbox:
                    $ percent_value = int(persistent.textbox_opacity * 100)
                    label _("Textbox Opacity ([percent_value]%)")
                    bar:
                        value FieldValue(persistent, "textbox_opacity", range=1.0, style="slider")
                    textbutton _("Set to default") action InvertSelected(SetVariable("persistent.textbox_opacity", 0.0))


                    label _("Textbox Width ([persistent.textbox_width]/1646)")
                    bar:
                        value FieldValue(persistent, "textbox_width", offset=1116, range=530, style="slider")
                    textbutton _("Set to default") action InvertSelected(SetVariable("persistent.textbox_width", gui.dialogue_width))

                    label _("Textbox Height ([persistent.textbox_height]/350)")
                    bar:
                        value FieldValue(persistent, "textbox_height", offset=100, range=250, style="slider")
                    textbutton _("Set to default") action InvertSelected(SetVariable("persistent.textbox_height", gui.textbox_height))
            null height (4 * gui.pref_spacing)
    viewport:
        xsize 480
        ysize 633
        xpos 1300
        ypos 219
        scrollbars "vertical"
        mousewheel True
        draggable True
        pagekeys True
        vbox:
            xalign 0.5
            yalign 0.5
            
            if not main_menu and not _in_replay and nicknameunlock:
                vbox:
                    label _("Edit Nickname")
                    if not edit_mode:
                        textbutton '[nickname]' action SetScreenVariable('edit_mode', True)
                    else:
                        key 'dismiss' action SetScreenVariable('edit_mode', False)
                        key 'input_enter' action SetScreenVariable('edit_mode', False)
                        input:
                            value FieldInputValue(store, 'nickname', returnable=True)
            if renpy.variant("pc"):

                vbox:
                    style_prefix "radio"
                    label _("Display")
                    textbutton _("Window") action Preference("display", "window")
                    textbutton _("Fullscreen") action Preference("display", "fullscreen")
            
            # Note to translators: This preference menu appears automatically
            # when more than one language is available. By default, it will use
            # the internal language name of your translation. If you want to
            # provide a better title for your language, add a snippet like this
            # to the top of your screens.rpy translation file (but outside any
            # "translate strings" block):
            #
            # init python:
            #     language_titles["chinese"] = "中文"
            #     language_title_fonts["chinese"] = "tl/chinese/font/Thin.ttf"
            #
            # You can omit setting a different font if you don't need it, but if
            # you do set one, you of course need to provide that font with your
            # translation files.
            if len(renpy.known_languages()) > 0:
                vbox:
                    style_prefix "radio"
                    label _("Language")
                    textbutton _("English{#prefs}"):
                        action Language(None)
                    for lang in renpy.known_languages():
                        $ option_title = language_titles.get(lang, lang)
                        $ option_font = language_title_fonts.get(lang, None)
                        textbutton option_title:
                            action Language(lang)
                            if option_font is not None:
                                text_font option_font

            vbox:
                style_prefix "radio"
                label _("Rollback Side")
                textbutton _("Disable") action Preference("rollback side", "disable")
                textbutton _("Left") action Preference("rollback side", "left")
                textbutton _("Right") action Preference("rollback side", "right")

            vbox:
                style_prefix "check"
                label _("Skip")
                textbutton _("Unseen Text") action Preference("skip", "toggle")
                textbutton _("After Choices") action Preference("after choices", "toggle")
                #textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))

            vbox:
                style_prefix "radio"
                label _("Quick Menu")
                textbutton _("Enabled") action SetField(persistent,"quick_menu", True)
                textbutton _("Disabled") action SetField(persistent,"quick_menu", False)
            
            vbox:
                style_prefix "radio"
                label _("Interface Motion")
                textbutton _("Enabled") action SetField(persistent,"motion", 1.0)
                textbutton _("Disabled") action SetField(persistent,"motion", .0)

                ## Additional vboxes of type "radio_pref" or "check_pref" can be
                ## added here, to add additional creator-defined preferences.

            null height (4 * gui.pref_spacing)


    # textbutton "Return" action Return()    xpos 91    yalign 0.93    yoffset -45
    default return_h = None
    button:
        action Return()
        focus_mask True
        image "gui/msp5/return.png"
        image im.MatrixColor("gui/msp5/return.png", im.matrix.colorize('#f1f1f180', '#f1f1f180')):
            if return_h == 1:
                at transform:
                    easein_quint (0.5 * persistent.motion) alpha 1.0 blur 0
            elif return_h == 0:
                at transform:
                    easein_quint (0.5 * persistent.motion) alpha 0.0 blur 5
            else:
                at transform:
                    alpha 0.0
        hovered [ SetLocalVariable("return_h", 1) ]
        unhovered [ SetLocalVariable("return_h", 0) ]
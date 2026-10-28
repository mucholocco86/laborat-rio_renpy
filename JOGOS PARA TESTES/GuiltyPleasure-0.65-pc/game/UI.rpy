

screen main_menu:
    if main_menu:
        add "gui/MM_Background.png"
        #text "Guilty Pleasure" style "mm_title"
        imagebutton:
            idle "gui/patreon_idle.png"
            hover "gui/patreon_hover.png"
            action OpenURL("https://www.patreon.com/Quonix")
            xalign 1.01
            yoffset 20
    else:
        use ingame
    style_prefix "mm"
    hbox:
        if main_menu:
            button:
                text _("Start")
                action Start()
        else:
            button:
                text _("Save")
                action ShowMenu("save")
        button:
            text _("Load")
            action ShowMenu("load")
        button:
            text _("Preferences")
            action ShowMenu("preferences")
        if main_menu:
            button:
                text _("Quit")
                action Quit(confirm=not main_menu)
        else:
            button:
                text _("Main Menu")
                action MainMenu()

    if not main_menu:
        imagebutton:
            focus_mask True
            idle "gui/close_idle.png"
            hover "gui/close_hover.png"
            action Return()

style mm_title:
    color "#9f3541"
    outlines [ (absolute(4), "#fff", absolute(0), absolute(0)) ]
    size 80
    bold True
    pos (101, 4)

style mm_button:
    background "gui/Button_idle.png"
    hover_background "gui/Button_hover.png"
    xysize (455, 113)
    focus_mask True
    #activate_sound "audio/button.ogg"

style mm_hbox:
    yalign 0.99
    xoffset 10
    xsize 1920

style mm_text:
    xalign 0.5
    yalign 0.5
    italic True
    bold True
    outlines [ (absolute(2), "#fff", absolute(0), absolute(0)) ]
    selected_outlines [ (absolute(0), "#fff", absolute(0), absolute(0)) ]
    yoffset 5
    hover_size 37
    selected_underline True
    #selected_hover_size 42
    #selected_size 40
    selected_color "#fff"
    hover_color "#a04751"
    color "#9f3541"

screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))

    use main_menu

    add "gui/menu_bg.png"

    fixed:
        yoffset 51
        ## This ensures the input will get the enter event before any of the
        ## buttons do.
        order_reverse True

        ## The page name, which can be edited by clicking on a button.
        button:
            style "page_label"

            key_events True
            xalign 0.5
            yalign 0.1
            action page_name_value.Toggle()

            input:
                style "inputs_input"
                value page_name_value

        ## The grid of file slots.
        grid gui.file_slot_cols gui.file_slot_rows:
            style_prefix "slot"

            xalign 0.5
            yalign 0.4

            spacing gui.slot_spacing

            for i in range(gui.file_slot_cols * gui.file_slot_rows):

                $ slot = i + 1

                button:
                    action FileAction(slot)

                    idle_background "gui/button/slot_background.png"
                    idle_foreground "gui/button/slot_foreground.png"
                    hover_foreground "gui/button/slot_foreground_hover.png"
                    xalign 0.5
                    has vbox

                    add FileScreenshot(slot) xalign 0.5


                    text FileTime(slot, format="{#file_time}%A, %B %d %Y, %H:%M", empty=_("Empty Slot")):
                        yoffset 20
                        outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ]
                        hover_size 23
                        xalign 0.5
                        size 18

                    text FileSaveName(slot):
                        style "slot_name_text"

                    key "save_delete" action FileDelete(slot)

        ## Buttons to access other pages.
        hbox:
            style_prefix "mm_page"

            ysize 100

            xalign 0.5
            yalign 0.84

            spacing gui.page_spacing

            textbutton "<" action FilePagePrevious()

            if config.has_autosave:
                textbutton "{#auto_page}A" action FilePage("auto")

            if config.has_quicksave:
                textbutton "{#quick_page}Q" action FilePage("quick")

            ## range(1, 10) gives the numbers from 1 to 9.
            for page in range(1, 10):
                textbutton "[page]" action FilePage(page)

            textbutton ">" action FilePageNext()

    if main_menu:
        imagebutton:
            focus_mask True
            idle "gui/close_idle.png"
            hover "gui/close_hover.png"
            action Hide("load")

style mm_page_button_text:
    #hover_size 40
    italic True
    bold True
    #selected_hover_size 42
    #selected_size 40
    hover_color "#a04751"
    hover_outlines [ (absolute(2), "#fff", absolute(0), absolute(0)) ]
    idle_outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ]

#style mm_page_button:
    #activate_sound "audio/button.ogg"

style mm_fspage_text:
    xalign 0.5
    italic True
    bold True
    yoffset 5
    #hover_size 40
    #selected_hover_size 42
    #selected_size 40
    hover_color "#a04751"
    hover_outlines [ (absolute(2), "#fff", absolute(0), absolute(0)) ]
    idle_outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ]

screen preferences():

    tag menu

    use main_menu

    add "gui/menu_bg.png"

    vbox:
        xalign 0.65
        yalign 0.45

        hbox:
            box_wrap True
            spacing 50
            xoffset 80
            ysize 235
            style_prefix "mm_pref"

            vbox:
                style_prefix "mm_pref"
                text _("Language")
                textbutton "English" action Language(None)
                textbutton "Italiano" action Language("italian")
                textbutton "Turkce" action Language("turkish")
                textbutton "Deutsch" action Language("german")

            if renpy.variant("pc") or renpy.variant("web"):

                vbox:
                    text _("Display")
                    textbutton _("Window") action Preference("display", "window")
                    textbutton _("Fullscreen") action Preference("display", "fullscreen")

            vbox:
                text _("Rollback Side")
                textbutton _("Disable") action Preference("rollback side", "disable")
                textbutton _("Left") action Preference("rollback side", "left")
                textbutton _("Right") action Preference("rollback side", "right")

            vbox:
                xsize 500
                text _("Skip")
                textbutton _("Unseen Text") action Preference("skip", "toggle")
                textbutton _("After Choices") action Preference("after choices", "toggle")
                textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))

            ## Additional vboxes of type "radio_pref" or "check_pref" can be
            ## added here, to add additional creator-defined preferences.

        null height (4 * gui.pref_spacing)

        hbox:
            style_prefix "slider"
            box_wrap True
            xalign 0.5
            yoffset -20
            vbox:

                text _("Text Speed") style "mm_pref_text"

                bar value Preference("text speed")

                text _("Auto-Forward Time") style "mm_pref_text"

                bar value Preference("auto-forward time")

                text _("Textbox Opacity") style "mm_pref_text"
                bar value FieldValue(persistent, "KoGa3TextboxOpacity", range=1.0) style "slider_slider"

                # null height gui.pref_spacing
                # hbox:
                    # ysize 80
                    # textbutton _("Quick Menu"):
                        # action ToggleVariable("quick_menu", True, False)
                        # style "mm_pref_button"
                        # text_style "mm_pref_button_text"

                #=====================================KoGa3 additions====================================#
                text _("\nMod KoGa3") style "mm_pref_text"
                textbutton _("Settings..."):
                    style "mm_pref_button"
                    sensitive True
                    action [
                    Show("KoGa3ScreenBlank"),
                    Show("KoGa3GameSettings") ]
                #=====================================KoGa3 additions====================================#

            vbox:

                if config.has_music:
                    text _("Music Volume") style "mm_pref_text"

                    hbox:
                        bar value Preference("music volume")

                if config.has_sound:

                    text _("Sound Volume") style "mm_pref_text"

                    hbox:
                        bar value Preference("sound volume")

                        if config.sample_sound:
                            textbutton _("Test") action Play("sound", config.sample_sound)


                if config.has_voice:
                    text _("Voice Volume") style "mm_pref_text"

                    hbox:
                        bar value Preference("voice volume")

                        if config.sample_voice:
                            textbutton _("Test") action Play("voice", config.sample_voice)

                if config.has_music or config.has_sound or config.has_voice:
                    null height gui.pref_spacing
                    hbox:
                        ysize 80
                        textbutton _("Mute All"):
                            action Preference("all mute", "toggle")
                            style "mm_pref_button"
                            text_style "mm_pref_button_text"

                text _("\nMod KoGa3: Main menu music") style "mm_pref_text"         #KoGa3
                hbox:
                    hbox:
                        style_prefix "check"
                        if persistent.KoGa3main_menu_music is True:

                            textbutton _("ON"):
                                style "mm_pref_button"
                                text_style "mm_pref_button_text"
                                #selected False
                                action [ 
                                Stop("music"), 
                                SetVariable("persistent.KoGa3main_menu_music", False) ]

                        else:
                            textbutton _("OFF"):
                                style "mm_pref_button"
                                text_style "mm_pref_button_text"
                                #selected False
                                #sensitive True
                                action [ 
                                Play("music", "/music/Introspection.mp3"), 
                                SetVariable("persistent.KoGa3main_menu_music", True) ]

    if main_menu:
        imagebutton:
            focus_mask True
            idle "gui/close_idle.png"
            hover "gui/close_hover.png"
            action Hide("preferences")

style mm_pref_text:
    italic True
    bold True
    yoffset 5
    #hover_size 40
    #selected_hover_size 42
    #selected_size 40

style mm_pref_button_text:
    italic True
    bold True
    yoffset 5
    #hover_size 40
    #selected_hover_size 42
    #selected_size 40
    hover_color "#a04751"
    hover_outlines [ (absolute(2), "#fff", absolute(0), absolute(0)) ]
    idle_outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ]

style mm_pref_button:
    xoffset 30
    #activate_sound "audio/button.ogg"

screen ingame():
    tag menu

    style_prefix "mm"
    hbox:
        yalign 0.0
        button:
            text _("Relationships")
            action ShowMenu("Relationship")
        button:
            text _("Credits")
            action ShowMenu("Credits")
        button:
            text _("Story Map")
            action ShowMenu("StoryMap")
        button:
            text _("Hidden Gallery")
            action ShowMenu("HGallery")

screen Credits():
    add "gui/menu_bg.png"

    tag menu

    use main_menu

    style_prefix "credits"
    viewport:
        mousewheel True
        draggable True
        yoffset 150
        xoffset 230
        spacing 20
        ysize 750
        xsize 1479
        vbox:
            xsize 1479
            xalign 0.5
            text _("Special Thanks") size 45 layout "nobreak"
            hbox:
                xalign 0.5
                yoffset 40
                vbox:
                    xsize 500
                    text "Studio Kuma"
                    text "Adeptus Celeng"
                vbox:
                    xsize 500
                    text "PandaPenguinGames"
                    text "Redoxa"
                    text _("You")
                vbox:
                    xsize 500
                    text "Boom's Attic Games"
                    text "Hopes Gaming"
            text _("Supporters") size 45 layout "nobreak" yoffset 80
            hbox:
                ysize 750
                xalign 0.5
                yoffset 120
                vbox:
                    xsize 500
                    text "Ttej Smith"
                    text "Darkbay101"
                    text "Marcos"
                    text "Kiyoshi Nariko"
                    text "Spagett"
                    text "KomaB"
                    text "Mdiizzle"
                    text "Anonymous"
                    text "Ed"
                    text "pjlbel481"
                    text "Rannell"
                    text "Bone-"
                    text "Nickles1206"
                    text "Stein"
                    text "Marcos Augusto"
                    text "Hong Kong Phooey"
                    text "Lufyris"
                    text "Draagon"
                vbox:
                    xsize 500
                    text "Lucky"
                    text "VNwhiteknight"
                    text "Granny977"
                    text "PoseidonsKnight"
                    text "Jjj13"
                    text "Keenir"
                    text "Armykracker"
                    text "KS Man"
                    text "Ethan M"
                    text "Alex"
                    text "Aries W"
                    text "RecklessMexican"
                    text "Rugrat"
                    text "Kaizo"
                    text "PortgasDLuigi"
                    text "Lulux"
                    text "Pietro-I"
                    text "Solfuccord"
                vbox:
                    xsize 500
                    text "DaOcker"
                    text "Creationism"
                    text "Dutch"
                    text "Chadsgn"
                    text "Cell"
                    text "Huw Gryffin"
                    text "Johnny44"
                    text "Blinkz0"
                    text "Pope Kiko"
                    text "KinGofecchi03"
                    text "xProtege16x"
                    text "Jeff L"
                    text "Selinor"
                    text "Castor833"
                    text "Maj"
                    text "Tromzaar"
                    text "Paul de Wys"
                    text "Kurate"

style credits_text:
    italic True
    bold True
    yoffset 5
    xalign 0.5

screen Relationship():
    add "gui/menu_bg_2.png"

    tag menu

    button:
        style "inputDisable"
        action DisableAllInputValues()

    use main_menu

    default inputAlex = nameAlex("Alex")
    default inputB = relInput("B")
    default inputBr = relInput("Br")
    default inputSo = relInput("So")
    default inputNe = relInput("Ne")

    style_prefix "inputs"

    add "gui/RelB.png" xpos 175 ypos 117

    button:
        pos (782, 316)
        action inputBr.Toggle(), SetVariable("changesMade", True)
        input:
            value inputBr

    text "You are Rachel and Lilly's..." pos (1282, 316) yoffset 15

    button:
        pos (782, 425)
        action inputB.Toggle(), SetVariable("changesMade", True)
        input:
            value inputB

    text "They also call you..." pos (1282, 425) yoffset 15

    button:
        pos (782, 534)
        action inputSo.Toggle(), SetVariable("changesMade", True)
        input:
            value inputSo

    text "You are Tasha's..." pos (1282, 534) yoffset 15

    button:
        pos (782, 643)
        action inputNe.Toggle(), SetVariable("changesMade", True)
        input:
            value inputNe

    text "And Christine's..." pos (1282, 643) yoffset 15

    fixed:
        area (683, 157, 1237, 60)
        button:
            align (0.5, 0.5)
            xysize (None, None)
            action inputAlex.Toggle(), SetVariable("changesMade", True)
            has hbox
            input:
                value inputAlex
            add "gui/button/Icons_Relationships.png" yoffset 4 xoffset -10

    imagebutton:
        xalign 1.0
        ypos 852
        idle "gui/Right.png"
        hover "gui/Right_hover.png"
        action ShowMenu("RelationshipLillyRachel")

    imagebutton:
        xpos 688
        ypos 852
        idle "gui/Left.png"
        hover "gui/Left_hover.png"
        action ShowMenu("RelationshipA")

screen RelationshipLillyRachel():
    add "gui/menu_bg_2.png"

    tag menu

    button:
        style "inputDisable"
        action DisableAllInputValues()

    use main_menu

    default inputS = relInput("S")
    default inputSi = relInput("Si")
    default inputD = relInput("D")
    default inputNi = relInput("Ni")

    style_prefix "inputs"

    add "gui/RelS.png" xpos 175 ypos 117

    button:
        pos (782, 316)
        action inputSi.Toggle(), SetVariable("changesMade", True)
        input:
            value inputSi

    text "Lilly, just like Rachel, is your..." pos (1282, 316) yoffset 15

    button:
        pos (782, 425)
        action inputS.Toggle(), SetVariable("changesMade", True)
        input:
            value inputS

    text "You also call her..." pos (1282, 425) yoffset 15


    button:
        pos (782, 534)
        action inputD.Toggle(), SetVariable("changesMade", True)
        input:
            value inputD

    text "She is also Tasha's..." pos (1282, 534) yoffset 15

    button:
        pos (782, 643)
        action inputNi.Toggle(), SetVariable("changesMade", True)
        input:
            value inputNi

    text "And Christine's..." pos (1282, 643) yoffset 15

    fixed:
        area (683, 157, 1237, 60)
        text "Lilly & Rachel" style "inputs_input"

    imagebutton:
        xalign 1.0
        ypos 852
        idle "gui/Right.png"
        hover "gui/Right_hover.png"
        action ShowMenu("RelationshipTasha")

    imagebutton:
        xpos 688
        ypos 852
        idle "gui/Left.png"
        hover "gui/Left_hover.png"
        action ShowMenu("Relationship")

screen RelationshipTasha():
    add "gui/menu_bg_2.png"

    tag menu

    button:
        style "inputDisable"
        action DisableAllInputValues()

    use main_menu

    default inputM = relInput("M")
    default inputMo = relInput("Mo")

    style_prefix "inputs"

    add "gui/RelM.png" xpos 175 ypos 117

    button:
        pos (782, 316)
        action inputMo.Toggle(), SetVariable("changesMade", True)
        input:
            value inputMo

    text "Tasha is your..." pos (1282, 316) yoffset 15

    button:
        pos (782, 425)
        action inputM.Toggle(), SetVariable("changesMade", True)
        input:
            value inputM

    text "You also call her..." pos (1282, 425) yoffset 15


    fixed:
        area (683, 157, 1237, 60)
        text "Tasha" style "inputs_input"

    imagebutton:
        xalign 1.0
        ypos 852
        idle "gui/Right.png"
        hover "gui/Right_hover.png"
        action ShowMenu("RelationshipA")

    imagebutton:
        xpos 688
        ypos 852
        idle "gui/Left.png"
        hover "gui/Left_hover.png"
        action ShowMenu("RelationshipLillyRachel")

screen RelationshipA():
    add "gui/menu_bg_2.png"

    tag menu

    button:
        style "inputDisable"
        action DisableAllInputValues()

    use main_menu

    default inputA = relInput("A")
    default inputAu = relInput("Au")

    style_prefix "inputs"

    if Act59MetA:
        add "gui/RelA.png" xpos 175 ypos 117
    else:
        add "gui/RelAB.png" xpos 175 ypos 117

    button:
        pos (782, 316)
        action inputA.Toggle(), SetVariable("changesMade", True)
        input:
            value inputA

    text "This is your..." pos (1282, 316) yoffset 15

    button:
        pos (782, 425)
        action inputAu.Toggle(), SetVariable("changesMade", True)
        input:
            value inputAu

    text "You also call her..." pos (1282, 425) yoffset 15

    imagebutton:
        xalign 1.0
        ypos 852
        idle "gui/Right.png"
        hover "gui/Right_hover.png"
        action ShowMenu("Relationship")

    imagebutton:
        xpos 688
        ypos 852
        idle "gui/Left.png"
        hover "gui/Left_hover.png"
        action ShowMenu("RelationshipTasha")

style inputs_input:
    xalign 0.5
    yalign 0.5
    xysize (382, 70)
    italic True
    bold True
    color "#fff"
    layout "nobreak"
    caret "HrelCaret"
    hover_caret "relCaret"
    hover_size 30
    selected_hover_size 32
    selected_size 30
    hover_color "#a04751"
    hover_outlines [ (absolute(2), "#fff", absolute(0), absolute(0)) ]
    kerning 5

style inputs_button:
    key_events True
    xsize 382
    ysize 70
    #activate_sound "audio/button.ogg"

style inputDisable:
    xfill True
    yfill True

image relCaret:
    "gui/caret1.png"
    pause 0.7
    "gui/caret2.png"
    pause 0.7
    repeat

image HrelCaret:
    "gui/caret3.png"
    pause 0.7
    "gui/caret4.png"
    pause 0.7
    repeat

screen StoryMap():
    add "gui/menu_bg.png"

    tag menu

    use main_menu

    vpgrid:
        mousewheel True
        draggable True
        yoffset 150
        xoffset 230
        #spacing 20
        ysize 750
        xsize 1950
        scrollbars "vertical"

        vscrollbar_xoffset 100
        vscrollbar_yoffset 58
        vscrollbar_ysize 698

        cols 3

        #$ Gslots = len(gal)
        #$ Rows = ((Gslots / 3) + 1)

        #grid 3 Rows:
        xspacing 125
        yspacing 15
        for i in gal:
            frame:
                background None
                padding (0, 0)
                xysize (394, 275)
                hbox:
                    xalign 0.5 yoffset 20
                    text i.name
                    for a in i.hid:
                        if findHG(a, "name") in persistent.foundHGal or KoGa3GalleryUnlock == 1:
                            add "gui/pic.png" yoffset 1
                        else:
                            add "gui/pic1.png" yoffset 1
                button:
                    yoffset 8
                    focus_mask True
                    yalign 1.0
                    xysize (394, 225)
                    foreground Frame("gui/galForeground.png")
                    if renpy.seen_image(i.check) or KoGa3GalleryUnlock == 1:
                        hover_foreground Frame("gui/galHover.png")
                        background Frame("images/StoryMap/B" + i.image)
                        action Function(renpy.call_replay, i.label, scope={"MCName" : MCName, "rel" : rel})
                    else:
                        background Frame("gui/LockedGal.png")
                        action NullAction()
                hbox:
                    xalign 0.5
                    yoffset -70
                    for i in range(0, 3):
                        add "gui/pic.png"
                    for i in range(0, 2):
                        add "gui/pic1.png"

        #for r in range((Rows * 3) - Gslots):
        #    frame:
        #        xysize(1, 1)

    vbox:
        yoffset 325
        xoffset 5
        if KoGa3GalleryUnlock == 1:
            textbutton _("Mod:"):
                text_style "KoGa3_button_text"
                text_outlines [ (absolute(1), "#000", absolute(0), absolute(0)) ]
                selected False
                action [
                SetVariable("KoGa3GalleryUnlock", 0) ]
            textbutton _("{color=[KoGa3Color3]}ON {/color}"):
                text_style "KoGa3_button_text"
                text_outlines [ (absolute(1), "#000", absolute(0), absolute(0)) ]
                selected False
                action [
                SetVariable("KoGa3GalleryUnlock", 0) ]
        if KoGa3GalleryUnlock == 0:
            textbutton _("Mod:"):
                text_style "KoGa3_button_text"
                text_outlines [ (absolute(1), "#000", absolute(0), absolute(0)) ]
                selected False
                action [
                SetVariable("KoGa3GalleryUnlock", 1) ]
            textbutton _("{color=[KoGa3Color4]}OFF{/color}"):
                text_style "KoGa3_button_text"
                text_outlines [ (absolute(1), "#000", absolute(0), absolute(0)) ]
                selected False
                action [
                SetVariable("KoGa3GalleryUnlock", 1) ]

screen HGallery():
    add "gui/menu_bg.png"

    tag menu

    key "alt_shift_K_u" action Function(UnlockHG)

    use main_menu

    vpgrid:
        mousewheel True
        draggable True
        yoffset 150
        xoffset 230
        #spacing 20
        ysize 750
        xsize 1950
        scrollbars "vertical"

        vscrollbar_xoffset 100
        vscrollbar_yoffset 58
        vscrollbar_ysize 698

        cols 3

        #$ Gslots = len(hGal)
        #$ Rows = ((Gslots / 3) + 1)

        #grid 3 Rows:
        xspacing 125
        yspacing 65

        for i in hGal:
            frame:
                background None
                padding (0, 0)
                xysize (394, 225)
                button:
                    yalign 1.0
                    xysize (394, 225)
                    foreground Frame("gui/galForeground.png")
                    if i.name in persistent.foundHGal or KoGa3GalleryUnlock == 1:
                        hover_foreground Frame("gui/galHover.png")
                        background Frame("images/HG/Buttons/B" + i.image.replace("png", "webp"))
                        action ShowMenu("HGalleryBig", i)
                    else:
                        background Frame("gui/LockedGal.png")
                        action NullAction()

        #for r in range((Rows * 3) - Gslots):
        #    frame:
        #        xysize(1, 1)

    vbox:
        yoffset 325
        xoffset 5
        if KoGa3GalleryUnlock == 1:
            textbutton _("Mod:"):
                text_style "KoGa3_button_text"
                selected False
                action [
                SetVariable("KoGa3GalleryUnlock", 0) ]
            textbutton _("{color=[KoGa3Color3]}ON {/color}"):
                text_style "KoGa3_button_text"
                selected False
                action [
                SetVariable("KoGa3GalleryUnlock", 0) ]
        if KoGa3GalleryUnlock == 0:
            textbutton _("Mod:"):
                text_style "KoGa3_button_text"
                selected False
                action [
                SetVariable("KoGa3GalleryUnlock", 1) ]
            textbutton _("{color=[KoGa3Color4]}OFF{/color}"):
                text_style "KoGa3_button_text"
                selected False
                action [
                SetVariable("KoGa3GalleryUnlock", 1) ]

screen HGalleryBig(Himage):

    add Himage.anim()

    modal True

    button:
        xfill True
        yfill True
        action Hide("HGalleryBig")

screen HGButtons(name):
    layer "master"

    if not name in persistent.foundHGal:
        imagebutton:
            focus_mask True
            idle "images/HG/" + findHG(name, "button")
            hover im.MatrixColor("images/HG/" + findHG(name, "button"), im.matrix.brightness(0.05))
            action AddToSet(persistent.foundHGal, name), Notify("Hidden Gallery Image Found!")

        if KoGa3ChoiceOption == 1:
            imagebutton:
                xalign 0.0
                yalign 0.0
                idle "KoGa3Lightbulb.png"
                hover "KoGa3Lightbulb.png"
                action NullAction()
                hovered Show ("KoGa3HGButtonsText")
                unhovered Hide ("KoGa3HGButtonsText")

screen KoGa3HGButtonsText:
    hbox:
        xalign 0.05
        yalign 0.0
        textbutton _("Gallery unlock available\n     (search for a disc)"):
            text_style persistent.KoGa3_QuickMenu1_button_font
            text_size 28
            sensitive False
            action NullAction()


#---------------------Quick menu---------------------#
define persistent.KoGa3QuickMenuButton = 1
define persistent.KoGa3QuickMenuShow = 1
define persistent.KoGa3_QuickMenu1_button_font = "KoGa3_QuickMenu1_button_text"
define KoGa3QuickMenuTextSizedefault = 20
define KoGa3TextOutline4default = 2
define KoGa3TextOutline5default = 0
define KoGa3TextOutline6default = 0
define persistent.KoGa3QuickMenuTextSize = KoGa3QuickMenuTextSizedefault
define persistent.KoGa3TextOutline4 = KoGa3TextOutline4default
define persistent.KoGa3TextOutline5 = KoGa3TextOutline5default
define persistent.KoGa3TextOutline6 = KoGa3TextOutline6default

define persistent.KoGa3QuickMenuItemBack = True
define persistent.KoGa3QuickMenuItemHist = False
define persistent.KoGa3QuickMenuItemSkip = True
define persistent.KoGa3QuickMenuItemAuto = True
define persistent.KoGa3QuickMenuItemSave = True
define persistent.KoGa3QuickMenuItemLoad = True
define persistent.KoGa3QuickMenuItemQSave = True
define persistent.KoGa3QuickMenuItemQLoad = True
define persistent.KoGa3QuickMenuItemPrefs = True
define persistent.KoGa3QuickMenuItemModmenu = True
define persistent.KoGa3QuickMenuIconOrText = 0
screen quick_menu():
    ## Ensure this appears on top of other screens.
    zorder 100

    if quick_menu == True and persistent.KoGa3QuickMenuButton == 2:
        mousearea:
            area (0, 980, 1920, 100)
            hovered SetVariable("persistent.KoGa3QuickMenuShow", 1)
            unhovered SetVariable("persistent.KoGa3QuickMenuShow", 0)

    if quick_menu == True and persistent.KoGa3QuickMenuShow == 1:
        if persistent.KoGa3QuickMenuIconOrText == 1:
            hbox:
                style_prefix "quick"
                $ persistent.KoGa3_QuickMenu1_button_font = "KoGa3_QuickMenu1_button_text"
                $ persistent.KoGa3_QuickMenu2_button_font = "KoGa3_QuickMenu2_button_text"
                xalign 0.5
                yalign 1.0
                if persistent.KoGa3QuickMenuItemBack:
                    textbutton _("Back"):
                        text_style persistent.KoGa3_QuickMenu1_button_font
                        text_size persistent.KoGa3QuickMenuTextSize
                        text_outlines [ (absolute(persistent.KoGa3TextOutline4), "#000", absolute(persistent.KoGa3TextOutline5), absolute(persistent.KoGa3TextOutline6)) ]
                        action Rollback()
                if persistent.KoGa3QuickMenuItemHist:
                    textbutton _("Hist"):
                        text_style persistent.KoGa3_QuickMenu1_button_font
                        text_size persistent.KoGa3QuickMenuTextSize
                        text_outlines [ (absolute(persistent.KoGa3TextOutline4), "#000", absolute(persistent.KoGa3TextOutline5), absolute(persistent.KoGa3TextOutline6)) ]
                        action ShowMenu('history')
                if persistent.KoGa3QuickMenuItemSkip:
                    textbutton _("Skip"):
                        text_style persistent.KoGa3_QuickMenu1_button_font
                        text_size persistent.KoGa3QuickMenuTextSize
                        text_outlines [ (absolute(persistent.KoGa3TextOutline4), "#000", absolute(persistent.KoGa3TextOutline5), absolute(persistent.KoGa3TextOutline6)) ]
                        action Skip() alternate Skip(fast=True, confirm=True)
                if persistent.KoGa3QuickMenuItemAuto:
                    textbutton _("Auto"):
                        text_style persistent.KoGa3_QuickMenu1_button_font
                        text_size persistent.KoGa3QuickMenuTextSize
                        text_outlines [ (absolute(persistent.KoGa3TextOutline4), "#000", absolute(persistent.KoGa3TextOutline5), absolute(persistent.KoGa3TextOutline6)) ]
                        action Preference("auto-forward", "toggle")
                if persistent.KoGa3QuickMenuItemSave:
                    textbutton _("Save"): 
                        text_style persistent.KoGa3_QuickMenu1_button_font
                        text_size persistent.KoGa3QuickMenuTextSize
                        text_outlines [ (absolute(persistent.KoGa3TextOutline4), "#000", absolute(persistent.KoGa3TextOutline5), absolute(persistent.KoGa3TextOutline6)) ]
                        action ShowMenu('save')
                if persistent.KoGa3QuickMenuItemLoad:
                    textbutton _("Load"): 
                        text_style persistent.KoGa3_QuickMenu1_button_font
                        text_size persistent.KoGa3QuickMenuTextSize
                        text_outlines [ (absolute(persistent.KoGa3TextOutline4), "#000", absolute(persistent.KoGa3TextOutline5), absolute(persistent.KoGa3TextOutline6)) ]
                        action ShowMenu('load')
                if persistent.KoGa3QuickMenuItemQSave:
                    textbutton _("Q.Save"):
                        text_style persistent.KoGa3_QuickMenu1_button_font
                        text_size persistent.KoGa3QuickMenuTextSize
                        text_outlines [ (absolute(persistent.KoGa3TextOutline4), "#000", absolute(persistent.KoGa3TextOutline5), absolute(persistent.KoGa3TextOutline6)) ]
                        action QuickSave()
                if persistent.KoGa3QuickMenuItemQLoad:
                    textbutton _("Q.Load"):
                        text_style persistent.KoGa3_QuickMenu1_button_font
                        text_size persistent.KoGa3QuickMenuTextSize
                        text_outlines [ (absolute(persistent.KoGa3TextOutline4), "#000", absolute(persistent.KoGa3TextOutline5), absolute(persistent.KoGa3TextOutline6)) ]
                        action QuickLoad()
                if persistent.KoGa3QuickMenuItemPrefs:
                    textbutton _("Prefs"):
                        text_style persistent.KoGa3_QuickMenu1_button_font
                        text_size persistent.KoGa3QuickMenuTextSize
                        text_outlines [ (absolute(persistent.KoGa3TextOutline4), "#000", absolute(persistent.KoGa3TextOutline5), absolute(persistent.KoGa3TextOutline6)) ]
                        action ShowMenu('preferences')
                if persistent.KoGa3QuickMenuItemModmenu:
                    hbox:
                        spacing 10
                        if KoGa3ModMenuButtonPressed == False:
                            textbutton _("Mod menu"):
                                text_style persistent.KoGa3_QuickMenu1_button_font
                                text_size persistent.KoGa3QuickMenuTextSize
                                text_outlines [ (absolute(persistent.KoGa3TextOutline4), "#000", absolute(persistent.KoGa3TextOutline5), absolute(persistent.KoGa3TextOutline6)) ]
                                selected False 
                                action [ 
                                SetVariable ("KoGa3ModMenuButtonPressed", True),
                                Hide("KoGa3ScreenAudio"),   #old Mod button
                                Show("KoGa3ScreenModMenu") ] 

                        if KoGa3ModMenuButtonPressed == True:
                            textbutton _("Close Mod menu"):
                                text_style persistent.KoGa3_QuickMenu1_button_font
                                text_size persistent.KoGa3QuickMenuTextSize
                                text_outlines [ (absolute(persistent.KoGa3TextOutline4), "#000", absolute(persistent.KoGa3TextOutline5), absolute(persistent.KoGa3TextOutline6)) ]
                                selected False 
                                action [
                                SetVariable ("KoGa3ModMenuButtonPressed", False),
                                Hide("KoGa3ScreenCheat"), 
                                Hide("KoGa3ScreenModMenu"), 
                                Hide("KoGa3ScreenCheatMore1"), 
                                Hide("KoGa3ScreenJukebox"), 
                                Hide("KoGa3QuickMusicMenu"), 
                                Hide("KoGa3ScreenBlank"), 
                                Hide("KoGa3ScreenAudioMenu"), 
                                Hide("KoGa3GameSettingsQuickMenu"), 
                                Hide("KoGa3GameSettings") ] 
        else:
            hbox:
                ysize 80
                xalign 0.5
                yalign 1.0

                imagebutton:
                    idle "gui/button/bttn_box_idle_fastforward.png"
                    hover "gui/button/bttn_box_hover_fastforward.png"
                    selected_idle "gui/button/bttn_box_selected_fastforward.png"
                    selected_hover "gui/button/bttn_box_selected_fastforward.png"
                    yalign 1.0
                    action Skip()
                imagebutton:
                    idle "gui/button/bttn_box_idle_autoplay.png"
                    hover "gui/button/bttn_box_hover_autoplay.png"
                    selected_idle "gui/button/bttn_box_selected_autoplay.png"
                    selected_hover "gui/button/bttn_box_selected_autoplay.png"
                    yalign 1.0
                    action Preference("auto-forward", "toggle")
                imagebutton:
                    idle "gui/button/bttn_box_idle_save.png"
                    hover "gui/button/bttn_box_hover_save.png"
                    yalign 1.0
                    action ShowMenu('save')
                imagebutton:
                    idle "gui/button/bttn_box_idle_settings.png"
                    hover "gui/button/bttn_box_hover_settings.png"
                    yalign 1.0
                    action ShowMenu('preferences')

                if KoGa3ModMenuButtonPressed == False:      #KoGa3
                    imagebutton:
                        idle "/bttn_box_idle_Mod.png"
                        hover "/bttn_box_hover_Mod.png"
                        yalign 1.0
                        action [
                        SetVariable ("KoGa3ModMenuButtonPressed", True),
                        Hide("KoGa3ScreenAudio"),   #old Mod button
                        Show("KoGa3ScreenModMenu") ] 
                if KoGa3ModMenuButtonPressed == True:
                    imagebutton:
                        idle "/bttn_box_hover_Mod.png"
                        hover "/bttn_box_selected_Mod.png"
                        yalign 1.0
                        action [
                        SetVariable ("KoGa3ModMenuButtonPressed", False),
                        Hide("KoGa3ScreenCheatMore1"), #not used so far
                        Hide("KoGa3ScreenJukebox"), 
                        Hide("KoGa3GameSettings"), 
                        Hide("KoGa3ScreenModMenu") ] 




screen modalS(nr):
    button:
        xfill True
        yfill True
        if nr == 1:
            action Hide("Relationship"), Hide("modalS"), Jump("tut")
        elif nr == 2:
            action Hide("modalS"), Jump("tut2")
        else:
            action Hide("preferences"), Hide("modalS"), Jump("V1Act1")

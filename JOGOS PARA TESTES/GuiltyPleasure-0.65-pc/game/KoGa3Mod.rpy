#Mod for the game Guilty Pleasure / KoGa3#

init python:
    def convert_float_into_time(t):
        i, f = divmod(t, 1)
        i = int(i)
        m, s = divmod(i, 60)
        h, m = divmod(m, 60)
        return "{:02}:{:02}".format(m, s)

# new audio channel for the game      #not used
init python:
    renpy.music.register_channel("music1", mixer="music")
    renpy.music.register_channel("sound1", mixer="sfx")
    renpy.music.register_channel("sound2", mixer="sfx")


#---------------------shortcut key for Mod menu screen---------------------#
init python:
    # key: Shift + k.
    config.keymap['KoGa3ScreenModMenu'] = "shift_K_k"
define config.overlay_screens = ["keymap", "quick_menu"]
screen keymap:
    key "KoGa3ScreenModMenu":
        action [ 
        SetVariable ("KoGa3ModMenuButtonPressed", True),
        Show("KoGa3ScreenModMenu") ] 


#---------------------Textbutton / Colors---------------------#
init python:

    style.KoGa3_text.font = "KoGa3.ttf"     #insensitive
    style.KoGa3_text.color = "#c4aead"      #"#808080" "#ffffff"
    style.KoGa3_text.size = 30
    #style.KoGa3_text.line_spacing = 30
    style.KoGa3_text.outlines = [ (absolute(2), "#000000", absolute(0), absolute(0)) ]

    style.KoGa3_1_text.font = "KoGa3.ttf"   #selected 1
    style.KoGa3_1_text.color = "#c4aead"    #"#808080" "#ffffff"
    style.KoGa3_1_text.size = 30
    #style.KoGa3_1_text.line_spacing = 30
    style.KoGa3_1_text.outlines = [ (absolute(3), "#000000", absolute(1), absolute(1)) ]        #Android: 4

    style.KoGa3_1a_text.font = "KoGa3.ttf"   #selected 1
    style.KoGa3_1a_text.color = "#c4aead"    #"#808080" "#ffffff"
    style.KoGa3_1a_text.size = 28
    #style.KoGa3_1a_text.line_spacing = 28
    style.KoGa3_1a_text.outlines = [ (absolute(3), "#000000", absolute(1), absolute(1)) ]       #Android: 4

    style.KoGa3_2_text.font = "KoGa3.ttf"   #selected 2
    style.KoGa3_2_text.color = "#ffffff"    #"#808080" "#ffffff"
    style.KoGa3_2_text.size = 30
    style.KoGa3_2_text.line_spacing = 30
    style.KoGa3_2_text.outlines = [ (absolute(2), "#000000", absolute(0), absolute(0)) ]


    style.KoGa3_button_text.font = "KoGa3.ttf"
    style.KoGa3_button_text.color = "#87cefa"    #"#808080" "#ffffff"
    style.KoGa3_button_text.hover_color = "#c90016"
    style.KoGa3_button_text.selected_color = "#ffff00"
    style.KoGa3_button_text.insensitive_color = "#c4aead"
    style.KoGa3_button_text.size = 30
    style.KoGa3_button_text.outlines = [ (absolute(2), "#000000", absolute(0), absolute(0)) ]

    style.KoGa3_1_button_text.font = "KoGa3.ttf"
    style.KoGa3_1_button_text.color = "#87cefa"
    style.KoGa3_1_button_text.hover_color = "#c90016"
    style.KoGa3_1_button_text.selected_color = "#ffff00"
    style.KoGa3_1_button_text.insensitive_color = "#c4aead"
    style.KoGa3_1_button_text.size = 30
    style.KoGa3_1_button_text.outlines = [ (absolute(3), "#000000", absolute(1), absolute(1)) ]   #Android: 4

    style.KoGa3_1a_button_text.font = "KoGa3.ttf"
    style.KoGa3_1a_button_text.color = "#87cefa"
    style.KoGa3_1a_button_text.hover_color = "#c90016"
    style.KoGa3_1a_button_text.selected_color = "#ffff00"
    style.KoGa3_1a_button_text.insensitive_color = "#c4aead"
    style.KoGa3_1a_button_text.size = 28
    style.KoGa3_1a_button_text.outlines = [ (absolute(3), "#000000", absolute(1), absolute(1)) ]  #Android: 4


    style.KoGa3_QuickMusic1_button_text.font = "KoGa3.ttf"
    style.KoGa3_QuickMusic1_button_text.color = "#87cefa"    #"#808080" "#ffffff"
    style.KoGa3_QuickMusic1_button_text.hover_color = "#c90016"
    style.KoGa3_QuickMusic1_button_text.selected_color = "#ffff00"  #"#ffffff"
    style.KoGa3_QuickMusic1_button_text.insensitive_color = "#c4aead"
    style.KoGa3_QuickMusic1_button_text.size = 25
    style.KoGa3_QuickMusic1_button_text.outlines = [ (absolute(1), "#000000", absolute(0), absolute(0)) ]

    style.KoGa3_QuickMenu1_button_text.font = "KoGa3.ttf"
    style.KoGa3_QuickMenu1_button_text.color = "#ffffff"
    style.KoGa3_QuickMenu1_button_text.hover_color = "#87cefa"
    style.KoGa3_QuickMenu1_button_text.selected_color = "#ffffff"
    style.KoGa3_QuickMenu1_button_text.insensitive_color = "#a9a9a9"
    #style.KoGa3_QuickMenu1_button_text.size = 22
    style.KoGa3_QuickMenu1_button_text.outlines = [ (absolute(2), "#000000", absolute(0), absolute(0)) ]

    style.KoGa3_QuickMenu2_button_text.font = "KoGa3.ttf"
    style.KoGa3_QuickMenu2_button_text.color = "#ffffff"
    style.KoGa3_QuickMenu2_button_text.hover_color = "#87cefa"
    style.KoGa3_QuickMenu2_button_text.selected_color = "#ffffff"
    style.KoGa3_QuickMenu2_button_text.insensitive_color = "#a9a9a9"
    #style.KoGa3_QuickMenu2_button_text.size = 22
    #style.KoGa3_QuickMenu2_button_text.outlines = [ (absolute(1), "#000000", absolute(0), absolute(0)) ]


    #buttons 2-5 for the info screen
    style.KoGa3_2_button_text.font = "KoGa3.ttf"
    style.KoGa3_2_button_text.color = "#ff9999"
    style.KoGa3_2_button_text.hover_color = "#800000"
    style.KoGa3_2_button_text.selected_color = "#ff9999"
    style.KoGa3_2_button_text.size = 25
    style.KoGa3_2_button_text.outlines = [ (absolute(2), "#000000", absolute(0), absolute(0)) ]

    style.KoGa3_3_button_text.font = "KoGa3.ttf"
    style.KoGa3_3_button_text.color = "#98fb98"
    style.KoGa3_3_button_text.hover_color = "#2a8000"
    style.KoGa3_3_button_text.selected_color = "#98fb98"
    style.KoGa3_3_button_text.size = 25
    style.KoGa3_3_button_text.outlines = [ (absolute(2), "#000000", absolute(0), absolute(0)) ]

    style.KoGa3_4_button_text.font = "KoGa3.ttf"
    style.KoGa3_4_button_text.color = "#87cefa"
    style.KoGa3_4_button_text.hover_color = "#0000cd"
    style.KoGa3_4_button_text.selected_color = "#87cefa"
    style.KoGa3_4_button_text.size = 25
    style.KoGa3_4_button_text.outlines = [ (absolute(2), "#000000", absolute(0), absolute(0)) ]

    style.KoGa3_5_button_text.font = "KoGa3.ttf"
    style.KoGa3_5_button_text.color = "#ffffff"
    style.KoGa3_5_button_text.hover_color = "#696969"
    style.KoGa3_5_button_text.selected_color = "#ffffff"
    style.KoGa3_5_button_text.size = 25
    style.KoGa3_5_button_text.outlines = [ (absolute(2), "#000000", absolute(0), absolute(0)) ]

default KoGa3_status_button_text = "KoGa3_5_button_text"
default KoGa3ButtonTextSize = 30
default KoGa3ButtonTextSize1 = 25   #Button size in Mod menu for color buttons
define KoGa3Color1 = "#c4aead"      #{color=#c4aead}     {/color}
define KoGa3Color2 = "#ffff00"      #{color=#ffffff}     {/color}
define KoGa3Color3 = "#00fa9a"      #{color=#ffffff}    {/color}
define KoGa3Color4 = "#ff0000"      #{color=#ffffff}     {/color}
define KoGa3xsize1 = 400
define KoGa3xsize2 = 110
define KoGa3xsize3 = 110
define KoGa3xsize4 = 90


#---------------------blank screen---------------------#
screen KoGa3ScreenBlank:
    add "/KoGa3MenuBack.png"
    modal True


#---------------------set Mod menu---------------------#
screen KoGa3ScreenModMenu:
    add "/KoGa3MenuBack.png"
    modal True
    vbox:
        xalign 0.5
        #yalign 0.5
        spacing -4
        textbutton (""):
            text_style "KoGa3_button_text"
            sensitive False
            action NullAction()
        textbutton _("━━━━━━━━━━━━━━━━━━━ Mod menu ━━━━━━━━━━━━━━━━━━━"):
            text_style "KoGa3_button_text"
            sensitive False
            action NullAction()

        textbutton _("Additional game settings..."):
            text_style "KoGa3_button_text"
            selected False
            sensitive True
            action [ 
            Hide("KoGa3ScreenModMenu"),
            Show("KoGa3GameSettings") ]

        textbutton _("━━━━━━━━━━━━━━━━━━━━━ Audio ━━━━━━━━━━━━━━━━━━━━━"):
            text_style "KoGa3_button_text"
            sensitive False
            action NullAction()
        if KoGa3SSound == 1:
            textbutton _("Sound effects like door knocking: {color=[KoGa3Color2]}ON{/color}"):
                text_style "KoGa3_button_text"
                selected False
                action [
                Stop ("sound1"),
                Stop ("sound2"),
                SetVariable("KoGa3HSound", 0),
                SetVariable("KoGa3SSound", 0) ]
        if KoGa3SSound == 0:
            textbutton _("Sound effects like door knocking: {color=[KoGa3Color2]}OFF{/color}"):
                text_style "KoGa3_button_text"
                selected False
                action [
                Play("audio", "/audio/Knock_01.mp3"), 
                SetVariable("KoGa3HSound", 1),
                SetVariable("KoGa3SSound", 1) ]
        if KoGa3ESound == 1:
            textbutton _("Human erotic sounds: {color=[KoGa3Color2]}ON{/color}"): 
                text_style "KoGa3_button_text"
                selected False
                action [
                Stop ("sound1"),
                Stop ("sound2"),
                SetVariable("KoGa3ESound", 0) ]
        if KoGa3ESound == 0:
            textbutton _("Human erotic sounds: {color=[KoGa3Color2]}OFF{/color}"): 
                text_style "KoGa3_button_text"
                selected False
                action [
                Play("audio", "/audio/Female-Moan_01.mp3"), 
                SetVariable("KoGa3ESound", 1) ]
        hbox:
            spacing 45
            #textbutton ("{color=[KoGa3Color2]}SFX volume:   {/color}"):
            textbutton ("SFX volume:    "):
                text_style "KoGa3_button_text"
                sensitive False
                action NullAction()
            bar:
                xsize 575
                ypos 5
                value Preference("sound volume")
        #text "-----------------------------------------------------------------------"
        text ""
        hbox:
            spacing 20
            textbutton ("Game music: "):
                text_style "KoGa3_button_text"
                sensitive False
                action NullAction()
            if KoGa3Music == 0:
                textbutton _("Original"):
                    text_style "KoGa3_button_text"
                    selected True
                    action NullAction()
            else:
                textbutton _("Original"):
                    text_style "KoGa3_button_text"
                    selected False
                    action [ 
                    Stop ("music"), 
                    Stop ("music1"), 
                    Play("music", OriginalCurrentMusic), 
                    SetVariable("KoGa3Music", 0) ]
            if KoGa3Music == 1:
                textbutton _("Mod"):
                    text_style "KoGa3_button_text"
                    selected True
                    action NullAction()
            else:
                textbutton _("Mod"):
                    text_style "KoGa3_button_text"
                    selected False
                    action [ 
                    Stop ("music"), 
                    Stop ("music1"), 
                    Play("music", KoGa3CurrentMusic), 
                    SetVariable("KoGa3Music", 1) ]
            if KoGa3Music == 2:
                textbutton _("OFF"):
                    text_style "KoGa3_button_text"
                    selected True
                    action NullAction()
            else:
                textbutton _("OFF"):
                    text_style "KoGa3_button_text"
                    selected False
                    action [ 
                    Stop ("music"), 
                    Stop ("music1"), 
                    SetVariable("KoGa3Music", 2) ]
        hbox:
            spacing 45
            #textbutton ("{color=[KoGa3Color2]}Music volume: {/color}"):
            textbutton ("Music volume: "):
                text_style "KoGa3_button_text"
                sensitive False
                action NullAction()
            bar:
                xsize 575
                ypos 5
                value Preference("music volume")
        #text "-----------------------------------------------------------------------"
        textbutton _("Mod Music Jukebox..."):
            text_style "KoGa3_button_text"
            sensitive True
            action [ 
            Hide("KoGa3ScreenModMenu"),
            Show("KoGa3ScreenJukebox") ]
        textbutton _("━━━━━━━━━━━━━━━━━━━━━ Cheat ━━━━━━━━━━━━━━━━━━━━━"):
            text_style "KoGa3_button_text"
            sensitive False
            action NullAction()
        textbutton ("Game progress (info):  [KoGa3GameProgress]"):
            text_style "KoGa3_button_text"
            sensitive False
            action NullAction()
        textbutton _("Name change...") text_style "KoGa3_button_text" action Hide("KoGa3ScreenModMenu"), Show ("KoGa3ScreenBlank"), Call("KoGa3NameChange")
        if KoGa3ChoiceOption == 1:
            textbutton _("Game choices help (walkthrough):  {color=[KoGa3Color2]}ON{/color}"):
                text_style "KoGa3_button_text"
                selected False
                action [
                SetVariable("KoGa3ChoiceView1", KoGa3ChoiceTextOFF),
                SetVariable("KoGa3ChoiceView1a", KoGa3ChoiceTextOFF),
                SetVariable("KoGa3ChoiceView2", KoGa3ChoiceTextOFF),
                SetVariable("KoGa3ChoiceView3", KoGa3ChoiceTextOFF),
                SetVariable("KoGa3ChoiceOption", 0) ]
        if KoGa3ChoiceOption == 0:
            textbutton _("Game choices help (walkthrough):  {color=[KoGa3Color2]}OFF{/color}"):
                text_style "KoGa3_button_text"
                selected False
                action [
                SetVariable("KoGa3ChoiceView1", "\n{color=#7cfc00}recommended by me{/color}"),
                SetVariable("KoGa3ChoiceView1a", "\n{color=#7cfc00}recommended by me so far{/color}"),
                SetVariable("KoGa3ChoiceView2", "\n{color=#0000ff}choice is not essential{/color}"),
                SetVariable("KoGa3ChoiceView3", "\n{color=#ff0000}bad choice{/color}"),
                SetVariable("KoGa3ChoiceOption", 1) ]
        if KoGa3GalleryUnlock == 1:
            textbutton _("Story map/Gallery unlock:  {color=[KoGa3Color2]}ON{/color}"):
                text_style "KoGa3_button_text"
                selected False
                action [
                SetVariable("KoGa3GalleryUnlock", 0) ]
        if KoGa3GalleryUnlock == 0:
            textbutton _("Story map/Gallery unlock:  {color=[KoGa3Color2]}OFF{/color}"):
                text_style "KoGa3_button_text"
                selected False
                action [
                SetVariable("KoGa3GalleryUnlock", 1) ]
        #textbutton ("Show/Hide status info"):
        #    action ToggleScreen("KoGa3ScreenStats")
        #textbutton ("Cheat Menu..."):
        #    selected False
        #    sensitive True
        #    action [
        #    Hide("KoGa3ScreenModMenu"), 
        #    SetVariable("stealthTemp", stealth), 
        #    SetVariable("charismaTemp", charisma), 
        #    SetVariable("prowessTemp", prowess), 
        #    SetVariable("sharonsavelaurieptsTemp", 
        #    sharonsavelauriepts), 
        #    SetVariable("laurieslaveorloverpointsTemp", 
        #    laurieslaveorloverpoints), 
        #    Show("KoGa3ScreenCheat") ]
        textbutton ("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"):
            text_style "KoGa3_button_text"
            sensitive False
            action NullAction()
        textbutton _("Close"):
            text_style "KoGa3_button_text"
            selected False
            action [
            SetVariable ("KoGa3ModMenuButtonPressed", False),
            Hide("KoGa3ScreenModMenu") ]

#info: game variables first set
#line 514:  vVboob = False
#line 915:  vShowerPic = False


#---------------------set name change---------------------#
label KoGa3NameChange:
    menu:
        "MC first name: {color=[KoGa3Color2]}[MCName]{/color},\n{color=[KoGa3Color2]}[rel.Br]{/color} / {color=[KoGa3Color2]}[rel.B]{/color}  to the girls  -  change...":
            $ MCName = renpy.input("What is your first name?", default=MCName)
            python:
                MCNameUP = MCName.upper()
            $ rel.Br = renpy.input("You are their (long term, maybe Brother)?", default=rel.Br)
            $ rel.B = renpy.input("You are their (short term, maybe Bro)?", default=rel.B)
            jump KoGa3NameChange
        "{color=[KoGa3Color2]}[TashaName]{/color}, your {color=[KoGa3Color2]}[rel.Mo]{/color} / {color=[KoGa3Color2]}[rel.M]{/color},\nYou are her {color=[KoGa3Color2]}[rel.So]{/color}  -  change...":
            $ TashaName = renpy.input("What is her first name?", default=TashaName)
            python:
                TashaNameUP = TashaName.upper()
            $ rel.Mo = renpy.input("You call her (long term, maybe Mother)?", default=rel.Mo)
            $ rel.M = renpy.input("You call her (short term, maybe Mom)?", default=rel.M)
            $ rel.So = renpy.input("You are her (maybe Son)?", default=rel.So)
            jump KoGa3NameChange
        "{color=[KoGa3Color2]}[LillyName]{/color}, your {color=[KoGa3Color2]}[rel.Si]{/color} / {color=[KoGa3Color2]}[rel.S]{/color},\n[TashaName]'s {color=[KoGa3Color2]}[rel.D]{/color}  -  change...":
            $ LillyName = renpy.input("What is her first name?", default=LillyName)
            python:
                LillyNameUP = LillyName.upper()
            $ rel.Si = renpy.input("You call her (long term, maybe Sister)?", default=rel.Si)
            $ rel.S = renpy.input("You call her (short term, maybe Sis)?", default=rel.S)
            $ rel.D = renpy.input("She is [TashaName]'s [rel.D] (maybe Daughter)?", default=rel.D)
            jump KoGa3NameChange
        "{color=[KoGa3Color2]}[RachelName]{/color}, your {color=[KoGa3Color2]}[rel.Si]{/color} / {color=[KoGa3Color2]}[rel.S]{/color},\n[TashaName]'s {color=[KoGa3Color2]}[rel.D]{/color}  -  change...":
            $ RachelName = renpy.input("What is her first name?", default=RachelName)
            python:
                RachelNameUP = RachelName.upper()
            $ rel.Si = renpy.input("You call her (long term, maybe Sister)?", default=rel.Si)
            $ rel.S = renpy.input("You call her (short term, maybe Sis)?", default=rel.S)
            $ rel.D = renpy.input("She is [TashaName]'s [rel.D] (maybe Daughter)?", default=rel.D)
            jump KoGa3NameChange
        "{color=[KoGa3Color2]}[ChristineName]{/color}, your {color=[KoGa3Color2]}[rel.A]/[rel.Au]{/color},\nYou are her {color=[KoGa3Color2]}[rel.Ne]{/color}  -  change...":
            $ ChristineName = renpy.input("What is her first name?", default=ChristineName)
            python:
                EllaNameUP = ChristineName.upper()
            $ rel.A = renpy.input("You call her (long term, maybe Aunt)?", default=rel.A)
            $ rel.Au = renpy.input("You call her also (maybe Auntie)?", default=rel.Au)
            $ rel.Ne = renpy.input("You are her (maybe Nephew)?", default=rel.Ne)
            jump KoGa3NameChange
        "{color=[KoGa3Color2]}[MayaName]{/color}, your tutoring student  -  change...":
            $ MayaName = renpy.input("What is her first name?", default=MayaName)
            python:
                MayaNameUP = MayaName.upper()
            jump KoGa3NameChange
        "{color=[KoGa3Color2]}[EileenName]{/color}, [MayaName]'s aunt  -  change...":
            $ EileenName = renpy.input("What is her first name?", default=EileenName)
            python:
                EileenNameUP = EileenName.upper()
            jump KoGa3NameChange

        #"\"[XXXName]\", your [rel.Au]/[rel.A]  -  change...":
        #    $ XXXName = renpy.input("What is her first name?", default=XXXName)
        #    python:
        #        XXXNameUP = XXXName.upper()
        #    $ rel.Au = renpy.input("You call her (long)?", default=rel.Au)
        #    $ rel.A = renpy.input("You call her (short)?", default=rel.A)
        #    jump KoGa3NameChange

        "Done":
            hide screen KoGa3ScreenBlank
            show screen KoGa3ScreenModMenu
            pause
            return


#---------------------Jukebox---------------------#
screen KoGa3ScreenJukebox:
    default soundis = False
    default p = None
    #style_prefix "musiccontrols"
    add "/KoGa3MenuBack.png"
    modal True
    vbox:
        xalign 0.5
        #yalign 0.5
        spacing -4
        textbutton (""):
            text_style "KoGa3_button_text"
            sensitive False
            action NullAction()
        hbox:
            timer .1 repeat True action SetScreenVariable("p",p)
            $ KoGa3CurrentMusicName = renpy.music.get_playing(channel='music')
            if isinstance(renpy.music.is_playing(channel='music'), int):
                if renpy.music.get_pos(channel='music'):
                    textbutton ("━━━━━━━━━━━━━━━━━━━━ Jukebox ━━━━━━ "):
                        text_style "KoGa3_button_text"
                        sensitive False
                        action NullAction()
                    $ p = renpy.music.get_pos(channel='music')
                    $ p_variable =  " {} / {}".format(convert_float_into_time(renpy.music.get_pos(channel='music')), convert_float_into_time(renpy.music.get_duration(channel='music')))
                    textbutton ("[p_variable]"):
                        text_style "KoGa3_button_text"
                        sensitive False
                        action NullAction()
                else:
                    textbutton ("━━━━━━━━━━━━━━━━━━━━ Jukebox ━━━━━━━━━━━━━━━━━━━━"):
                        text_style "KoGa3_button_text"
                        sensitive False
                        action NullAction()
        hbox:
            spacing 13
            textbutton ("Mod music (a-z):"):
                text_style "KoGa3_button_text"
                sensitive False
                action [
                SetVariable("KoGa3JukeboxButton", 1) ]
            if KoGa3JukeboxButton is 1:
                textbutton ("1-12"):
                    text_style "KoGa3_button_text"
                    selected True
                    #sensitive False
                    action NullAction()
            else:
                textbutton ("1-12"):
                    text_style "KoGa3_button_text"
                    selected False
                    action [
                    SetVariable("KoGa3JukeboxButton", 1) ]
            if KoGa3JukeboxButton is 2:
                textbutton ("13-24"):
                    text_style "KoGa3_button_text"
                    selected True
                    #sensitive False
                    action NullAction()
            else:
                textbutton ("13-24"):
                    text_style "KoGa3_button_text"
                    selected False
                    action [
                    SetVariable("KoGa3JukeboxButton", 2) ]
            if KoGa3JukeboxButton is 3:
                textbutton ("25-31"):
                    text_style "KoGa3_button_text"
                    selected True
                    #sensitive False
                    action NullAction()
            else:
                textbutton ("25-31"):
                    text_style "KoGa3_button_text"
                    selected False
                    action [
                    SetVariable("KoGa3JukeboxButton", 3) ]

            if KoGa3JukeboxButton is 5:
                textbutton ("   Orig. tracks"):
                    text_style "KoGa3_button_text"
                    selected True
                    #sensitive False
                    action NullAction()
            else:
                textbutton ("   Orig. tracks"):
                    text_style "KoGa3_button_text"
                    selected False
                    action [
                    SetVariable("KoGa3JukeboxButton", 5) ]
        textbutton ("────────────────────────────────────────────────"):
            text_style "KoGa3_button_text"
            sensitive False
            action NullAction()

#music 01-12
        if KoGa3JukeboxButton is 1:
            textbutton ("Abstract Fantasy.mp3 (MC theme 5)"):
                text_style "KoGa3_button_text"
                #selected False
                sensitive True
                action [ 
                Stop("music"), 
                Stop("music1"), 
                #SetVariable("KoGa3Jukebox", MusicMark1/MusicMC5),
                Play("music", "/music/Abstract Fantasy.mp3") ]
            textbutton ("Annihilation.mp3 (Serious theme 3)"):
                text_style "KoGa3_button_text"
                #selected False
                sensitive True
                action [ 
                Stop("music"), 
                Stop("music1"), 
                #SetVariable("KoGa3Jukebox", MusicMark1/MusicSerious3),
                Play("music", "/music/Annihilation.mp3") ]
            textbutton ("Bitcoin.mp3 (Serious theme 2)"):
                text_style "KoGa3_button_text"
                #selected False
                sensitive True
                action [ 
                Stop("music"), 
                Stop("music1"), 
                #SetVariable("KoGa3Jukebox", MusicMark1/MusicSerious2),
                Play("music", "/music/Bitcoin.mp3") ]
            textbutton ("Causmic_Contact.mp3 (Sexy theme 3)"):
                text_style "KoGa3_button_text"
                #selected False
                sensitive True
                action [ 
                Stop("music"), 
                Stop("music1"), 
                #SetVariable("KoGa3Jukebox", MusicMark1/MusicSexy3),
                Play("music", "/music/Causmic_Contact.mp3") ]
            textbutton ("Cosmic Glow.mp3 (Sexy theme 7)"):
                text_style "KoGa3_button_text"
                #selected False
                sensitive True
                action [ 
                Stop("music"), 
                Stop("music1"), 
                #SetVariable("KoGa3Jukebox", MusicMark1/MusicSexy7),
                Play("music", "/music/Cosmic Glow.mp3") ]
            textbutton ("Crystal Motions.mp3 (Party theme 5)"):
                text_style "KoGa3_button_text"
                #selected False
                sensitive True
                action [ 
                Stop("music"), 
                Stop("music1"), 
                #SetVariable("KoGa3Jukebox", MusicParty5),
                Play("music", "/music/Crystal Motions.mp3") ]
            textbutton ("Cybernetics.mp3 (Sexy theme 11)"):
                text_style "KoGa3_button_text"
                #selected False
                sensitive True
                action [ 
                Stop("music"), 
                Stop("music1"), 
                #SetVariable("KoGa3Jukebox", MusicMark1/MusicSexy11),
                Play("music", "/music/Cybernetics.mp3") ]
            textbutton ("Decibel - Research.mp3 (Sexy theme 9)"):
                text_style "KoGa3_button_text"
                #selected False
                sensitive True
                action [ 
                Stop("music"), 
                Stop("music1"), 
                #SetVariable("KoGa3Jukebox", MusicMark1/MusicSexy9),
                Play("music", "/music/Decibel - Research.mp3") ]
            textbutton ("Drive.mp3 (Mark / Party theme 1)"):
                text_style "KoGa3_button_text"
                #selected False
                sensitive True
                action [ 
                Stop("music"), 
                Stop("music1"), 
                #SetVariable("KoGa3Jukebox", MusicMark1/MusicParty1),
                Play("music", "/music/Drive.mp3") ]
            textbutton ("Ear Candy.mp3 ([RachelName] theme 1)"):
                text_style "KoGa3_button_text"
                #selected False
                sensitive True
                action [ 
                Stop("music"), 
                Stop("music1"), 
                #SetVariable("KoGa3Jukebox", MusicRachel1),
                Play("music", "/music/Ear Candy.mp3") ]
            textbutton ("Exiled.mp3 (Serious theme 1)"):
                text_style "KoGa3_button_text"
                #selected False
                sensitive True
                action [ 
                Stop("music"), 
                Stop("music1"), 
                #SetVariable("KoGa3Jukebox", MusicMark1/MusicSerious1),
                Play("music", "/music/Exiled.mp3") ]
            textbutton ("fearless-first.mp3 (Party theme 3)"):
                text_style "KoGa3_button_text"
                #selected False
                sensitive True
                action [ 
                Stop("music"), 
                Stop("music1"), 
                #SetVariable("KoGa3Jukebox", MusicParty3),
                Play("music", "/music/fearless-first.mp3") ]

#music 13-24
        if KoGa3JukeboxButton is 2:
            textbutton ("Fly Away.mp3 (MC theme 7)"):
                text_style "KoGa3_button_text"
                #selected False
                sensitive True
                action [ 
                Stop("music"), 
                Stop("music1"), 
                #SetVariable("KoGa3Jukebox", MusicMC7),
                Play("music", "/music/Fly Away.mp3") ]
            textbutton ("Gold Skies.mp3 (Sexy theme 10)"):
                text_style "KoGa3_button_text"
                #selected False
                sensitive True
                action [ 
                Stop("music"), 
                Stop("music1"), 
                #SetVariable("KoGa3Jukebox", MusicSexy10),
                Play("music", "/music/Gold Skies.mp3") ]
            textbutton ("Groove Day.mp3 (Party theme 2)"):
                text_style "KoGa3_button_text"
                #selected False
                sensitive True
                action [ 
                Stop("music"), 
                Stop("music1"), 
                #SetVariable("KoGa3Jukebox", MusicParty2),
                Play("music", "/music/Groove Day.mp3") ]
            textbutton ("Immersion.mp3 (Sexy theme 2)"):
                text_style "KoGa3_button_text"
                #selected False
                sensitive True
                action [ 
                Stop("music"), 
                Stop("music1"), 
                #SetVariable("KoGa3Jukebox", MusicSexy2),
                Play("music", "/music/Immersion.mp3") ]
            textbutton ("Inspirational Pop.mp3 (Sexy theme 5)"):
                text_style "KoGa3_button_text"
                #selected False
                sensitive True
                action [ 
                Stop("music"), 
                Stop("music1"), 
                #SetVariable("KoGa3Jukebox", MusicSexy5),
                Play("music", "/music/Inspirational Pop.mp3") ]
            textbutton ("Inspiring ABM_2.mp3 (MC theme 2)"):
                text_style "KoGa3_button_text"
                #selected False
                sensitive True
                action [ 
                Stop("music"), 
                Stop("music1"), 
                #SetVariable("KoGa3Jukebox", MusicMC2),
                Play("music", "/music/Inspiring ABM_2.mp3") ]
            textbutton ("Introspection.mp3 (Main menu theme)"):
                text_style "KoGa3_button_text"
                #selected False
                sensitive True
                action [ 
                Stop("music"), 
                Stop("music1"), 
                #SetVariable("KoGa3Jukebox", MusicMenu1),
                Play("music", "/music/Introspection.mp3") ]
            textbutton ("Medical.mp3 ([LillyName] theme 1)"):
                text_style "KoGa3_button_text"
                #selected False
                sensitive True
                action [ 
                Stop("music"), 
                Stop("music1"), 
                #SetVariable("KoGa3Jukebox", MusicLily1),
                Play("music", "/music/Medical.mp3") ]
            textbutton ("Medicine.mp3 (Home theme 1)"):
                text_style "KoGa3_button_text"
                #selected False
                sensitive True
                action [ 
                Stop("music"), 
                Stop("music1"), 
                #SetVariable("KoGa3Jukebox", MusicHome1),
                Play("music", "/music/Medicine.mp3") ]
            textbutton ("Minimal Corporate Ambient.mp3 (MC theme 3)"):
                text_style "KoGa3_button_text"
                #selected False
                sensitive True
                action [ 
                Stop("music"), 
                Stop("music1"), 
                #SetVariable("KoGa3Jukebox", MusicMC3),
                Play("music", "/music/Minimal Corporate Ambient.mp3") ]
            textbutton ("Night Chase - Raz Burg.mp3 ([MayaName] theme 1)"):
                text_style "KoGa3_button_text"
                #selected False
                sensitive True
                action [ 
                Stop("music"), 
                Stop("music1"), 
                #SetVariable("KoGa3Jukebox", MusicMaya1),
                Play("music", "/music/Night Chase - Raz Burg.mp3") ]
            textbutton ("Places Of Happy People.mp3 (MC theme 4)"):
                text_style "KoGa3_button_text"
                #selected False
                sensitive True
                action [ 
                Stop("music"), 
                Stop("music1"), 
                #SetVariable("KoGa3Jukebox", MusicMC4),
                Play("music", "/music/Places Of Happy People.mp3") ]

#music 25-31
        if KoGa3JukeboxButton is 3:
            textbutton ("Scientistication.mp3 (Sexy theme 4)"):
                text_style "KoGa3_button_text"
                #selected False
                sensitive True
                action [ 
                Stop("music"), 
                Stop("music1"), 
                #SetVariable("KoGa3Jukebox", MusicSexy4),
                Play("music", "/music/Scientistication.mp3") ]
            textbutton ("Sehnsucht.mp3 (Christine theme 1)"):
                text_style "KoGa3_button_text"
                #selected False
                sensitive True
                action [ 
                Stop("music"), 
                Stop("music1"), 
                #SetVariable("KoGa3Jukebox", MusicChristine1),
                Play("music", "/music/Sehnsucht.mp3") ]
            textbutton ("Sexy.mp3 (Sexy theme 1)"):
                text_style "KoGa3_button_text"
                #selected False
                sensitive True
                action [ 
                Stop("music"), 
                Stop("music1"), 
                #SetVariable("KoGa3Jukebox", MusicSexy1),
                Play("music", "/music/Sexy.mp3") ]
            textbutton ("Sweet heat.mp3 (Party theme 4)"):
                text_style "KoGa3_button_text"
                #selected False
                sensitive True
                action [ 
                Stop("music"), 
                Stop("music1"), 
                #SetVariable("KoGa3Jukebox", MusicMark1/MusicParty4),
                Play("music", "/music/Sweet heat.mp3") ]
            textbutton ("Technological.mp3 (Sexy theme 8)"):
                text_style "KoGa3_button_text"
                #selected False
                sensitive True
                action [ 
                Stop("music"), 
                Stop("music1"), 
                #SetVariable("KoGa3Jukebox", MusicSexy8),
                Play("music", "/music/Technological.mp3") ]
            textbutton ("Wake up and smile.mp3 (MC theme 1)"):
                text_style "KoGa3_button_text"
                #selected False
                sensitive True
                action [ 
                Stop("music"), 
                Stop("music1"), 
                #SetVariable("KoGa3Jukebox", MusicMC1),
                Play("music", "/music/Wake up and smile.mp3") ]
            textbutton ("Where I Find You_cut.mp3 ([TashaName] theme 1)"):
                text_style "KoGa3_button_text"
                #selected False
                sensitive True
                action [ 
                Stop("music"), 
                Stop("music1"), 
                #SetVariable("KoGa3Jukebox", MusicMC1),
                Play("music", "/music/Where I Find You_cut.mp3") ]

#music Orig. tracks
        if KoGa3JukeboxButton is 5:
            textbutton ("- Original: eau-de-summer.ogg -"):
                text_style "KoGa3_button_text"
                #selected False
                sensitive True
                action [ 
                Stop("music"), 
                Stop("music1"), 
                Play("music", "audio/eau-de-summer.ogg") ]
            textbutton ("- Original: every-so-often.ogg -"):
                text_style "KoGa3_button_text"
                #selected False
                sensitive True
                action [ 
                Stop("music"), 
                Stop("music1"), 
                Play("music", "audio/every-so-often.ogg") ]
            textbutton ("- Original: harem-avenue.ogg -"):
                text_style "KoGa3_button_text"
                #selected False
                sensitive True
                action [ 
                Stop("music"), 
                Stop("music1"), 
                Play("music", "audio/harem-avenue.ogg") ]
            textbutton ("- Original: millennial-bonefire.ogg -"):
                text_style "KoGa3_button_text"
                #selected False
                sensitive True
                action [ 
                Stop("music"), 
                Stop("music1"), 
                Play("music", "audio/millennial-bonefire.ogg") ]
            textbutton ("- Original: my-foster-castle.ogg -"):
                text_style "KoGa3_button_text"
                #selected False
                sensitive True
                action [ 
                Stop("music"), 
                Stop("music1"), 
                Play("music", "audio/my-foster-castle.ogg") ]

        textbutton ("────────────────────────────────────────────────"):
            text_style "KoGa3_button_text"
            sensitive False
            action NullAction()
        hbox:
            spacing 30
            textbutton ("Pause music"):
                text_style "KoGa3_button_text"
                #sensitive True
                action PauseAudio('music', value="toggle")
            if KoGa3MainMenu == 1:
                if KoGa3CurrentMusicName == KoGa3CurrentMusic:
                    textbutton (""):
                        text_style "KoGa3_button_text"
                        sensitive True
                        action [ 
                        Play("music", MusicMenu1) ]
                else:
                    textbutton ("back to the menu title"):
                        text_style "KoGa3_button_text"
                        sensitive True
                        action [ 
                        Play("music", MusicMenu1) ]

            if KoGa3MainMenu == 0:
                if KoGa3Music == 1:
                    if KoGa3CurrentMusicName == KoGa3CurrentMusic:
                        textbutton (""):
                            text_style "KoGa3_button_text"
                            sensitive True
                            action [ 
                            Stop("music"), 
                            Stop("music1"), 
                            Play("music", KoGa3CurrentMusic) ]
                    else:
                        textbutton ("back to the game title"):
                            text_style "KoGa3_button_text"
                            sensitive True
                            action [ 
                            Stop("music"), 
                            Stop("music1"), 
                            Play("music", KoGa3CurrentMusic) ]
                if KoGa3Music == 0:
                    if KoGa3CurrentMusicName == OriginalCurrentMusic:
                        textbutton (""):
                            text_style "KoGa3_button_text"
                            sensitive True
                            action [ 
                            Stop("music"), 
                            Stop("music1"), 
                            Play("music", OriginalCurrentMusic) ]
                    else:
                        textbutton ("back to the game title"):
                            text_style "KoGa3_button_text"
                            sensitive True
                            action [ 
                            Stop("music"), 
                            Stop("music1"), 
                            Play("music", OriginalCurrentMusic) ]

        textbutton ("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"):
            text_style "KoGa3_button_text"
            sensitive False
            action NullAction()
        if KoGa3MainMenu == 1:
            textbutton ("Back"):
                text_style "KoGa3_button_text"
                sensitive True
                action [
                SetVariable("KoGa3MainMenu", 0),
                Hide("KoGa3ScreenJukebox"), ]
        else:
            textbutton ("Back"):
                text_style "KoGa3_button_text"
                sensitive True
                action [
                Hide("KoGa3ScreenJukebox"), 
                Show("KoGa3ScreenModMenu") ]


#---------------------add. game settings---------------------#
screen KoGa3GameSettings:
    if not main_menu:
        add "/KoGa3MenuBack_settings.png"
    modal True
    vbox:
        xalign 0.5
        spacing -12
        null height (34)

        if _menu:
            if renpy.variant("touch"):
                textbutton _("━━━━━━━━━━━━━ Hardware settings ━━━━━━━━━━━━━━"):
                    text_style "KoGa3_1_button_text"
                    sensitive False
                    action NullAction()
                hbox:
                    hbox:
                        xsize 350
                        textbutton ("Performance Mode:"):
                            text_style "KoGa3_1a_button_text"
                            sensitive False
                            action NullAction()
                    hbox:
                        xsize 150
                        textbutton _("ON "):
                            text_style "KoGa3_1a_button_text"
                            action Preference("gl powersave", True)
                    hbox:
                        xsize 150
                        textbutton _("OFF"):
                            text_style "KoGa3_1a_button_text"
                            action Preference("gl powersave", False)
                    hbox:
                        textbutton _("Auto"):
                            text_style "KoGa3_1a_button_text"
                            action Preference("gl powersave", "auto")

                null height (25)

                hbox:
                    hbox:
                        xsize 350
                        textbutton ("Video Mode:"):
                            text_style "KoGa3_1a_button_text"
                            sensitive False
                            action NullAction()
                    hbox:
                        xsize 235
                        textbutton _("Hardware"):
                            text_style "KoGa3_1a_button_text"
                            action SetVariable("config.hw_video", True)
                    hbox:
                        textbutton _("Software"):
                            text_style "KoGa3_1a_button_text"
                            action SetVariable("config.hw_video", False)

            else:
                textbutton _("━━━━━━━━━━━━━━━ Mod settings ━━━━━━━━━━━━━━━━"):
                    text_style "KoGa3_1_button_text"
                    sensitive False
                    action NullAction()

            null height (35)

        #################################################################################
        if not _menu:
            textbutton _("━━━━━━━━━━━━━━━━━ Mod menu ━━━━━━━━━━━━━━━━━"):
                text_style "KoGa3_1_button_text"
                sensitive False
                action NullAction()
            # hbox:
                # hbox:
                    # xsize 245
                    # textbutton ("Music Mod: "):
                        # text_style "KoGa3_1a_button_text"
                        # sensitive False
                        # action NullAction()
                # hbox:
                    # xsize 240
                    # if KoGa3Music == 1:
                        # textbutton _("ON "):
                            # text_style "KoGa3_1a_button_text"
                            # selected False
                            # action [ 
                            # Stop ("music"), 
                            # Stop ("music1"), 
                            # Play("music", KoGa3CurrentMusic), 
                            # SetVariable("KoGa3Music", 1) ]
                    # if KoGa3Music == 2:
                        # textbutton _("OFF"):
                            # text_style "KoGa3_1a_button_text"
                            # selected False
                            # action [ 
                            # Stop ("music"), 
                            # Stop ("music1"), 
                            # SetVariable("KoGa3Music", 2) ]

                # textbutton _("Music Jukebox..."):
                    # text_style "KoGa3_1a_button_text"
                    # selected False
                    # sensitive True
                    # action [ 
                    # Hide("KoGa3GameSettings"),
                    # Show("KoGa3ScreenJukebox") ]

            #################################################################################

            # hbox:
                # textbutton ("Game progress (info):  [KoGa3GameProgress]"):
                    # text_style "KoGa3_1a_button_text"
                    # sensitive False
                    # action NullAction()
            # null height (15)

            # hbox:
                # hbox:
                    # xsize 225
                    # textbutton ("Choice hints: "):
                        # text_style "KoGa3_1a_button_text"
                        # sensitive False
                        # action NullAction()
                # hbox:
                    # xsize 260
                    # if KoGa3ChoiceOption == 0:
                        # textbutton _("OFF"):
                            # text_style "KoGa3_1a_button_text"
                            # selected False
                            # action [
                            # SetVariable ("KoGa3ChoiceOption", 1),
                            # SetVariable ("KoGa3AutoWTChange1", "\n{color=#ffdf00}"),
                            # SetVariable ("KoGa3WTChange", "\n{color=#008000}"),
                            # SetVariable ("KoGa3WTChange1", "\n{color=#ffdf00}"),
                            # SetVariable ("KoGa3WTChange2", "\n{color=#ff0000}") ]
                    # else:
                        # textbutton _("ON "):
                            # text_style "KoGa3_1a_button_text"
                            # selected False
                            # action [
                            # SetVariable ("KoGa3ChoiceOption", 0),
                            # SetVariable ("KoGa3AutoWTChange1", "{alt}"),
                            # SetVariable ("KoGa3WTChange", "{alt}"),
                            # SetVariable ("KoGa3WTChange1", "{alt}"),
                            # SetVariable ("KoGa3WTChange2", "{alt}")]

                # textbutton _("Change MC name..."):
                    # text_style "KoGa3_1a_button_text"
                    # selected False
                    # action [
                    # Hide("KoGa3GameSettings"),
                    # Show("KoGa3ScreenBlank"),
                    # Call("KoGa3NameChange") ]

            # null height (35)

        #################################################################################

        hbox:
            hbox:
                xsize 50
                if KoGa3DialogOptions == 0:
                    textbutton _("+"):
                        text_style "KoGa3_1a_button_text"
                        selected False
                        action [
                        SetVariable("KoGa3DialogOptions", 1),
                        SetVariable("KoGa3ChoiceOptions", 0),
                        SetVariable("KoGa3QuickMenuOptions", 0) ]

                if KoGa3DialogOptions == 1:
                    textbutton _("─"):
                        text_style "KoGa3_1a_button_text"
                        selected False
                        action SetVariable("KoGa3DialogOptions", 0)
            hbox:
                #######################################
                $ KoGa3TextboxOpacityPercent = int(persistent.KoGa3TextboxOpacity * 100)
                if persistent.KoGa3TextboxOpacity == KoGa3TextboxOpacitydefault and persistent.pref_text_size == pref_text_sizedefault and persistent.KoGa3xposOffset == KoGa3xposOffsetdefault and persistent.KoGa3yposOffset == KoGa3yposOffsetdefault and persistent.KoGa3TextOutline1 == KoGa3TextOutline1default and persistent.KoGa3TextOutline2 == KoGa3TextOutline2default and persistent.KoGa3TextOutline3 == KoGa3TextOutline3default and persistent.KoGa3DialogCentered == False:
                    textbutton _("{color=[KoGa3Color1]}──────────── Dialog settings ──────────────"):
                        text_style "KoGa3_1_button_text"
                        if KoGa3DialogOptions == 0:
                            action [
                            SetVariable("KoGa3DialogOptions", 1),
                            SetVariable("KoGa3ChoiceOptions", 0),
                            SetVariable("KoGa3QuickMenuOptions", 0) ]
                        if KoGa3DialogOptions == 1:
                            action SetVariable("KoGa3DialogOptions", 0)
                else:
                    hbox:
                        textbutton _("{color=[KoGa3Color1]}──────────── Dialog settings ──────"):
                            text_style "KoGa3_1_button_text"
                            if KoGa3DialogOptions == 0:
                                action [
                                SetVariable("KoGa3DialogOptions", 1),
                                SetVariable("KoGa3ChoiceOptions", 0),
                                SetVariable("KoGa3QuickMenuOptions", 0) ]
                            if KoGa3DialogOptions == 1:
                                action SetVariable("KoGa3DialogOptions", 0)
                        textbutton _("(reset)"):
                            text_style "KoGa3_1a_button_text"
                            selected False
                            action [
                            SetVariable("persistent.KoGa3TextboxOpacity", KoGa3TextboxOpacitydefault),
                            SetVariable("persistent.pref_text_size", pref_text_sizedefault),
                            SetVariable("persistent.KoGa3xposOffset", KoGa3xposOffsetdefault),
                            SetVariable("persistent.KoGa3yposOffset", KoGa3yposOffsetdefault),
                            SetVariable("persistent.KoGa3TextOutline1", KoGa3TextOutline1default),
                            SetVariable("persistent.KoGa3TextOutline2", KoGa3TextOutline2default),
                            SetVariable("persistent.KoGa3TextOutline3", KoGa3TextOutline3default),
                            SetVariable("persistent.KoGa3DialogCentered", False),
                            SetVariable("persistent.KoGa3DialogOptions", 1),
                            SetVariable("persistent.KoGa3QuickMenuButton", 1),
                            SetVariable("persistent.KoGa3QuickMenuShow", 1)]

        #################################################################################

        if KoGa3DialogOptions == 1:
            hbox:
                hbox:
                    xsize 50
                hbox:
                    vbox:
                        spacing -8
                        hbox:
                            text _("Dialogue box opacity  (current: [KoGa3TextboxOpacityPercent]%)"):
                                style "KoGa3_1a_text"
                        hbox:
                            ypos 5
                            textbutton _(" "):
                                text_style "KoGa3_1a_button_text"
                                sensitive False
                                action NullAction()
                            bar:
                                xsize 700
                                value FieldValue(persistent, "KoGa3TextboxOpacity", range=1.0, style="slider")

                        null height (25)

                        hbox:
                            text _("Dialogue box horizontal size offset (current: [persistent.KoGa3xposOffset])"):
                                style "KoGa3_1a_text"
                        hbox:
                            ypos 5
                            textbutton _(" "):
                                text_style "KoGa3_1a_button_text"
                                sensitive False
                                action NullAction()
                            bar:
                                xsize 700
                                value FieldValue(object=persistent, field='KoGa3xposOffset', range=600, max_is_zero=False, style=u'slider', offset=-300, step=1)

                        hbox:
                            text _("Dialogue box vertical offset (current: [persistent.KoGa3yposOffset])"):
                                style "KoGa3_1a_text"
                        hbox:
                            ypos 5
                            textbutton _(" "):
                                text_style "KoGa3_1a_button_text"
                                sensitive False
                                action NullAction()
                            bar:
                                xsize 700
                                value FieldValue(object=persistent, field='KoGa3yposOffset', range=500, max_is_zero=False, style=u'slider', offset=-200, step=1)

                        null height (25)

                        hbox:
                            text _("Dialogue text font size  (current: [persistent.pref_text_size]/75)"):
                                style "KoGa3_1a_button_text"
                        hbox:
                            ypos 5
                            textbutton _(" "):
                                text_style "KoGa3_1a_button_text"
                                sensitive False
                                action NullAction()
                            bar:
                                xsize 700
                                value FieldValue(object=persistent, field='pref_text_size', range=75, max_is_zero=False, style=u'slider', offset=0, step=1)

                        hbox:
                            text _("Dialogue text font outline  (current: [persistent.KoGa3TextOutline1]/10)"):
                                style "KoGa3_1a_button_text"
                        hbox:
                            ypos 5
                            textbutton _(" "):
                                text_style "KoGa3_1a_button_text"
                                sensitive False
                                action NullAction()
                            bar:
                                xsize 700
                                value FieldValue(persistent, "KoGa3TextOutline1", range=10, style="slider")

                        hbox:
                            hbox:
                                text _("   offset horizontal ([persistent.KoGa3TextOutline2])       offset vertical ([persistent.KoGa3TextOutline3])"):
                                    style "KoGa3_1a_button_text"
                        hbox:
                            ypos 5
                            textbutton _(" "):
                                text_style "KoGa3_1a_button_text"
                                sensitive False
                                action NullAction()
                            bar:
                                xsize 335
                                value FieldValue(persistent, "KoGa3TextOutline2", range=10, max_is_zero=False, style=u'slider', offset=-5, step=1)
                            textbutton _(" "):
                                text_style "KoGa3_1a_button_text"
                                sensitive False
                                action NullAction()
                            bar:
                                xsize 335
                                value FieldValue(persistent, "KoGa3TextOutline3", range=10, max_is_zero=False, style=u'slider', offset=-5, step=1)

                        hbox:
                            text _("Dialog alignment/position:"):
                                style "KoGa3_1a_button_text"
                            if persistent.KoGa3DialogCentered == False:
                                textbutton _("Left"):
                                    text_style "KoGa3_1a_button_text"
                                    selected False
                                    action SetVariable ("persistent.KoGa3DialogCentered", True)
                            else:
                                textbutton _("Center"):
                                    text_style "KoGa3_1a_button_text"
                                    selected False
                                    action SetVariable ("persistent.KoGa3DialogCentered", False)

                        null height (25)

        #################################################################################

        hbox:
            hbox:
                xsize 50
                if KoGa3ChoiceOptions == 0:
                    textbutton _("+"):
                        text_style "KoGa3_1a_button_text"
                        selected False
                        action [
                        SetVariable("KoGa3DialogOptions", 0),
                        SetVariable("KoGa3ChoiceOptions", 1),
                        SetVariable("KoGa3QuickMenuOptions", 0) ]
                if KoGa3ChoiceOptions == 1:
                    textbutton _("─"):
                        text_style "KoGa3_1a_button_text"
                        selected False
                        action SetVariable("KoGa3ChoiceOptions", 0)
            hbox:
                #######################################
                if persistent.KoGa3ChoiceTextSize == KoGa3ChoiceTextSizedefault and persistent.KoGa3TextOutline7 == KoGa3TextOutline7default and persistent.KoGa3TextOutline8 == KoGa3TextOutline8default and persistent.KoGa3TextOutline9 == KoGa3TextOutline9default and persistent.KoGa3ChoiceYpos == KoGa3ChoiceYposdefault and persistent.KoGa3ChoiceButtonWidth == KoGa3ChoiceButtonWidthdefault and persistent.KoGa3ChoiceBackground == True and persistent.KoGa3ChoiceAlign == "center":
                    textbutton _("{color=[KoGa3Color1]}──────────── Choice settings ──────────────"):
                        text_style "KoGa3_1_button_text"
                        if KoGa3ChoiceOptions == 0:
                            action [
                            SetVariable("KoGa3DialogOptions", 0),
                            SetVariable("KoGa3ChoiceOptions", 1),
                            SetVariable("KoGa3QuickMenuOptions", 0) ]
                        if KoGa3ChoiceOptions == 1:
                            action SetVariable("KoGa3ChoiceOptions", 0)
                else:
                    hbox:
                        textbutton _("{color=[KoGa3Color1]}──────────── Choice settings ──────"):
                            text_style "KoGa3_1_button_text"
                            if KoGa3ChoiceOptions == 0:
                                action [
                                SetVariable("KoGa3DialogOptions", 0),
                                SetVariable("KoGa3ChoiceOptions", 1),
                                SetVariable("KoGa3QuickMenuOptions", 0) ]
                            if KoGa3ChoiceOptions == 1:
                                action SetVariable("KoGa3ChoiceOptions", 0)
                        textbutton _("(reset)"):
                            text_style "KoGa3_1a_button_text"
                            selected False
                            action [
                            SetVariable("persistent.KoGa3ChoiceTextSize", KoGa3ChoiceTextSizedefault),
                            SetVariable("persistent.KoGa3TextOutline7", KoGa3TextOutline7default),
                            SetVariable("persistent.KoGa3TextOutline8", KoGa3TextOutline8default),
                            SetVariable("persistent.KoGa3TextOutline9", KoGa3TextOutline9default),
                            SetVariable("persistent.KoGa3ChoiceYpos", KoGa3ChoiceYposdefault),
                            SetVariable("persistent.KoGa3ChoiceButtonWidth", KoGa3ChoiceButtonWidthdefault),
                            SetVariable("persistent.KoGa3ChoiceBackground", True),
                            SetVariable("persistent.KoGa3ChoiceAlign", "center") ]

        #################################################################################

        if KoGa3ChoiceOptions == 1:
            hbox:
                hbox:
                    xsize 50
                hbox:
                    vbox:
                        spacing -8

                        hbox:
                            text _("Choice box vertical offset (current: [persistent.KoGa3ChoiceYpos])"):
                                style "KoGa3_1a_text"
                        hbox:
                            ypos 5
                            textbutton _(" "):
                                text_style "KoGa3_1a_button_text"
                                sensitive False
                                action NullAction()
                            bar:
                                xsize 700
                                value FieldValue(object=persistent, field='KoGa3ChoiceYpos', range=1080, max_is_zero=False, style=u'slider', offset=-450, step=1)

                        hbox:
                            text _("Choice box horizontal size (current: [persistent.KoGa3ChoiceButtonWidth])"):
                                style "KoGa3_1a_text"
                        hbox:
                            ypos 5
                            textbutton _(" "):
                                text_style "KoGa3_1a_button_text"
                                sensitive False
                                action NullAction()
                            bar:
                                xsize 700
                                value FieldValue(object=persistent, field='KoGa3ChoiceButtonWidth', range=1800, max_is_zero=False, style=u'slider', offset=0, step=1)

                        null height (25)

                        hbox:
                            text _("Choice text font size  (current: [persistent.KoGa3ChoiceTextSize]/75)"):
                                style "KoGa3_1a_button_text"
                        hbox:
                            ypos 5
                            textbutton _(" "):
                                text_style "KoGa3_1a_button_text"
                                sensitive False
                                action NullAction()
                            bar:
                                xsize 700
                                value FieldValue(object=persistent, field='KoGa3ChoiceTextSize', range=75, max_is_zero=False, style=u'slider', offset=0, step=1)

                        hbox:
                            text _("Choice text font outline  (current: [persistent.KoGa3TextOutline7]/10)"):
                                style "KoGa3_1a_button_text"
                        hbox:
                            ypos 5
                            textbutton _(" "):
                                text_style "KoGa3_1a_button_text"
                                sensitive False
                                action NullAction()
                            bar:
                                xsize 700
                                value FieldValue(persistent, "KoGa3TextOutline7", range=10, style="slider")

                        hbox:
                            hbox:
                                text _("   offset horizontal ([persistent.KoGa3TextOutline8])       offset vertical ([persistent.KoGa3TextOutline9])"):
                                    style "KoGa3_1a_button_text"
                        hbox:
                            ypos 5
                            textbutton _(" "):
                                text_style "KoGa3_1a_button_text"
                                sensitive False
                                action NullAction()
                            bar:
                                xsize 335
                                value FieldValue(persistent, "KoGa3TextOutline8", range=10, max_is_zero=False, style=u'slider', offset=-5, step=1)
                            textbutton _(" "):
                                text_style "KoGa3_1a_button_text"
                                sensitive False
                                action NullAction()
                            bar:
                                xsize 335
                                value FieldValue(persistent, "KoGa3TextOutline9", range=10, max_is_zero=False, style=u'slider', offset=-5, step=1)

                        hbox:
                            text _("Choice background:"):
                                style "KoGa3_1a_button_text"
                            if persistent.KoGa3ChoiceBackground == False:
                                textbutton _("OFF"):
                                    text_style "KoGa3_1a_button_text"
                                    selected False
                                    action SetVariable ("persistent.KoGa3ChoiceBackground", True)
                            else:
                                textbutton _("ON "):
                                    text_style "KoGa3_1a_button_text"
                                    selected False
                                    action SetVariable ("persistent.KoGa3ChoiceBackground", False)

                        hbox:
                            text _("Choice button alignment:"):
                                style "KoGa3_1a_button_text"
                            if persistent.KoGa3ChoiceAlign == "right":
                                textbutton _("Right"):
                                    text_style "KoGa3_1a_button_text"
                                    selected False
                                    action SetVariable ("persistent.KoGa3ChoiceAlign", "left")
                            if persistent.KoGa3ChoiceAlign == "left":
                                textbutton _("Left"):
                                    text_style "KoGa3_1a_button_text"
                                    selected False
                                    action SetVariable ("persistent.KoGa3ChoiceAlign", "center")
                            if persistent.KoGa3ChoiceAlign == "center":
                                textbutton _("Center"):
                                    text_style "KoGa3_1a_button_text"
                                    selected False
                                    action SetVariable ("persistent.KoGa3ChoiceAlign", "right")

                        null height (25)

        #################################################################################

        hbox:
            hbox:
                xsize 50
                if KoGa3QuickMenuOptions == 0:
                    textbutton _("+"):
                        text_style "KoGa3_1a_button_text"
                        selected False
                        action [
                        SetVariable("KoGa3DialogOptions", 0),
                        SetVariable("KoGa3ChoiceOptions", 0),
                        SetVariable("KoGa3QuickMenuOptions", 1) ]
                if KoGa3QuickMenuOptions == 1:
                    textbutton _("─"):
                        text_style "KoGa3_1a_button_text"
                        selected False
                        action [
                        SetVariable("KoGa3QuickMenuOptions", 0) ]
            hbox:
                if KoGa3QuickMenuOptions == 0:
                    textbutton _("{color=[KoGa3Color1]}────────── Quick menu settings ────────────"):
                        text_style "KoGa3_1_button_text"
                        action [
                        SetVariable("KoGa3DialogOptions", 0),
                        SetVariable("KoGa3ChoiceOptions", 0),
                        SetVariable("KoGa3QuickMenuOptions", 1) ]
                if KoGa3QuickMenuOptions == 1:
                    textbutton _("{color=[KoGa3Color1]}────────── Quick menu settings ────────────"):
                        text_style "KoGa3_1_button_text"
                        action [
                        SetVariable("KoGa3QuickMenuOptions", 0) ]

        #################################################################################

        if KoGa3QuickMenuOptions == 1:
            hbox:
                hbox:
                    xsize 50
                hbox:
                    vbox:
                        hbox:
                            hbox:
                                xsize 300
                                text _("Quick menu: "):
                                    xpos 4
                                    ypos 4
                                    style "KoGa3_1a_text"
                            hbox:
                                xsize 150
                                if persistent.KoGa3QuickMenuButton == 1:
                                    textbutton _("ON "):
                                        text_style "KoGa3_1a_button_text"
                                        selected True
                                        action NullAction()
                                else:
                                    textbutton _("ON "):
                                        text_style "KoGa3_1a_button_text"
                                        selected False
                                        action [ 
                                        SetVariable("persistent.KoGa3QuickMenuButton", 1),
                                        SetVariable("persistent.KoGa3QuickMenuShow", 1) ]
                            hbox:
                                xsize 150
                                if persistent.KoGa3QuickMenuButton == 2:
                                    textbutton _("Auto"):
                                        text_style "KoGa3_1a_button_text"
                                        selected True
                                        action NullAction()
                                else:
                                    textbutton _("Auto"):
                                        text_style "KoGa3_1a_button_text"
                                        selected False
                                        action [ 
                                        SetVariable("persistent.KoGa3QuickMenuButton", 2),
                                        SetVariable("persistent.KoGa3QuickMenuShow", 0) ]
                            hbox:
                                if persistent.KoGa3QuickMenuButton == 0:
                                    textbutton _("OFF"):
                                        text_style "KoGa3_1a_button_text"
                                        selected True
                                        action NullAction()
                                else:
                                    textbutton _("OFF"):
                                        text_style "KoGa3_1a_button_text"
                                        selected False
                                        action [ 
                                        SetVariable("persistent.KoGa3QuickMenuButton", 0),
                                        SetVariable("persistent.KoGa3QuickMenuShow", 0) ]

                        hbox:
                            hbox:
                                xsize 355
                                textbutton ("Quick menu buttons: "):
                                    text_style "KoGa3_1a_button_text"
                                    sensitive False
                                    action NullAction()
                            hbox:
                                #xsize 200
                                if persistent.KoGa3QuickMenuIconOrText == 0:
                                    textbutton _("Icons"):
                                        text_style "KoGa3_1a_button_text"
                                        selected False
                                        action [
                                        SetVariable ("persistent.KoGa3QuickMenuIconOrText", 1)]
                                else:
                                    textbutton _("Text"):
                                        text_style "KoGa3_1a_button_text"
                                        selected False
                                        action [
                                        SetVariable ("persistent.KoGa3QuickMenuIconOrText", 0)]

                        if persistent.KoGa3QuickMenuIconOrText == 1:
                            textbutton _("More Quick menu settings..."):
                                text_style "KoGa3_1a_button_text"
                                selected False
                                sensitive True
                                action [ 
                                Hide("KoGa3GameSettings"),
                                Show("KoGa3GameSettingsQuickMenu") ]

        textbutton ("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"):
            text_style "KoGa3_1_button_text"
            sensitive False
            action NullAction()
        if main_menu is True or KoGa3ModMenuButtonPressed is False:
            hbox:
                spacing 30
                textbutton _("Back"):
                    text_style "KoGa3_1_button_text"
                    sensitive True
                    action [
                    Hide("KoGa3GameSettings"), 
                    Hide("KoGa3ScreenBlank") ]
        else:
            hbox:
                spacing 30
                textbutton _("Back"):
                    text_style "KoGa3_1_button_text"
                    sensitive True
                    action [
                    Hide("KoGa3GameSettings"), 
                    Hide("KoGa3ScreenBlank"), 
                    Show("KoGa3ScreenModMenu") ]
                textbutton _("Close"):
                    text_style "KoGa3_1_button_text"
                    selected False
                    action [
                    SetVariable ("KoGa3ModMenuButtonPressed", False),
                    Hide("KoGa3GameSettings"), 
                    Hide("KoGa3ScreenBlank") ]


#---------------------add. game settings Quick Menu---------------------#
screen KoGa3GameSettingsQuickMenu:
    if not main_menu:
        add "/KoGa3MenuBack_settings.png"
    modal True
    vbox:
        xalign 0.5
        spacing -12
        null height (34)

        if persistent.KoGa3TextOutline4 == KoGa3TextOutline4default and persistent.KoGa3TextOutline5 == KoGa3TextOutline5default and persistent.KoGa3TextOutline6 == KoGa3TextOutline6default and persistent.KoGa3QuickMenuTextSize == KoGa3QuickMenuTextSizedefault:
            textbutton _("━━━━━━━━━━ More Quick menu settings ━━━━━━━━━━"):
                text_style "KoGa3_1_button_text"
                sensitive False
                action NullAction()
        else:
            hbox:
                textbutton _("━━━━━━━━━━ More Quick menu settings ━━━"):
                    text_style "KoGa3_1_button_text"
                    sensitive False
                    action NullAction()
                textbutton _("(reset)"):
                    text_style "KoGa3_1_button_text"
                    selected False
                    action [
                    SetVariable("persistent.KoGa3TextOutline4", KoGa3TextOutline4default),
                    SetVariable("persistent.KoGa3TextOutline5", KoGa3TextOutline5default),
                    SetVariable("persistent.KoGa3TextOutline6", KoGa3TextOutline6default),
                    SetVariable("persistent.KoGa3QuickMenuTextSize", KoGa3QuickMenuTextSizedefault) ]

        hbox:
            hbox:
                xsize 300
                text _("Quick menu: "):
                    style "KoGa3_1a_text"
            hbox:
                xsize 150
                if persistent.KoGa3QuickMenuButton == 1:
                    textbutton _("ON "):
                        text_style "KoGa3_1a_button_text"
                        selected True
                        action NullAction()
                else:
                    textbutton _("ON "):
                        text_style "KoGa3_1a_button_text"
                        selected False
                        action [ 
                        SetVariable("persistent.KoGa3QuickMenuButton", 1),
                        SetVariable("persistent.KoGa3QuickMenuShow", 1) ]
            hbox:
                xsize 150
                if persistent.KoGa3QuickMenuButton == 2:
                    textbutton _("Auto"):
                        text_style "KoGa3_1a_button_text"
                        selected True
                        action NullAction()
                else:
                    textbutton _("Auto"):
                        text_style "KoGa3_1a_button_text"
                        selected False
                        action [ 
                        SetVariable("persistent.KoGa3QuickMenuButton", 2),
                        SetVariable("persistent.KoGa3QuickMenuShow", 0) ]
            hbox:
                if persistent.KoGa3QuickMenuButton == 0:
                    textbutton _("OFF"):
                        text_style "KoGa3_1a_button_text"
                        selected True
                        action NullAction()
                else:
                    textbutton _("OFF"):
                        text_style "KoGa3_1a_button_text"
                        selected False
                        action [ 
                        SetVariable("persistent.KoGa3QuickMenuButton", 0),
                        SetVariable("persistent.KoGa3QuickMenuShow", 0) ]

        textbutton _("───────────────────────────────────────────"):
            text_style "KoGa3_1_button_text"
            sensitive False
            action NullAction()

        null height (20)

        vbox:
            spacing -8
            hbox:
                text _("Quick menu text font size  (current: [persistent.KoGa3QuickMenuTextSize]/40)"):
                    style "KoGa3_1a_button_text"
            hbox:
                ypos 5
                textbutton _(" "):
                    text_style "KoGa3_1a_button_text"
                    sensitive False
                    action NullAction()
                bar:
                    xsize 750
                    value FieldValue(object=persistent, field='KoGa3QuickMenuTextSize', range=40, max_is_zero=False, style=u'slider', offset=0, step=1)

            hbox:
                text _("Quick menu text font outline  (current: [persistent.KoGa3TextOutline4]/10)"):
                    style "KoGa3_1a_button_text"
            hbox:
                ypos 5
                textbutton _(" "):
                    text_style "KoGa3_1a_button_text"
                    sensitive False
                    action NullAction()
                bar:
                    xsize 750
                    value FieldValue(object=persistent, field='KoGa3TextOutline4', range=10, max_is_zero=False, style=u'slider', offset=0, step=1)

            hbox:
                hbox:
                    text _("   offset horizontal ([persistent.KoGa3TextOutline5])       offset vertical ([persistent.KoGa3TextOutline6])"):
                        style "KoGa3_1a_button_text"
            hbox:
                ypos 5
                textbutton _(" "):
                    text_style "KoGa3_1a_button_text"
                    sensitive False
                    action NullAction()
                bar:
                    xsize 360
                    value FieldValue(object=persistent, field='KoGa3TextOutline5', range=10, max_is_zero=False, style=u'slider', offset=-5, step=1)
                textbutton _(" "):
                    text_style "KoGa3_1a_button_text"
                    sensitive False
                    action NullAction()
                bar:
                    xsize 360
                    value FieldValue(object=persistent, field='KoGa3TextOutline6', range=10, max_is_zero=False, style=u'slider', offset=-5, step=1)

        null height (34)

        hbox:
            hbox:
                xsize 50
                if KoGa3QuickMenuItems == 0:
                    textbutton _("+"):
                        text_style "KoGa3_1a_button_text"
                        selected False
                        action [
                        SetVariable("KoGa3QuickMenuItems", 1) ]
                if KoGa3QuickMenuItems == 1:
                    textbutton _("─"):
                        text_style "KoGa3_1a_button_text"
                        selected False
                        action SetVariable("KoGa3QuickMenuItems", 0)

            hbox:
                textbutton _("{color=[KoGa3Color1]}────────── Quick menu items ─────────────"):
                    text_style "KoGa3_1_button_text"
                    if KoGa3QuickMenuItems == 0:
                        action [
                        SetVariable("KoGa3QuickMenuItems", 1) ]
                    if KoGa3QuickMenuItems == 1:
                        action [
                        SetVariable("KoGa3QuickMenuItems", 0) ]

        #################################################################################
        if KoGa3QuickMenuItems == 1:
            hbox:
                hbox:
                    xsize 50
                    textbutton _(" "):
                        text_style "KoGa3_1_button_text"
                        sensitive False
                        action NullAction()
                vbox:
                    spacing -10

                    hbox:
                        hbox:
                            xsize 550
                            textbutton ("Button \"Back\" is:"):
                                text_style "KoGa3_1a_button_text"
                                sensitive False
                                action NullAction()
                        hbox:
                            xsize 200
                            if persistent.KoGa3QuickMenuItemBack == False:
                                textbutton _("OFF"):
                                    text_style "KoGa3_1a_button_text"
                                    selected False
                                    action SetVariable ("persistent.KoGa3QuickMenuItemBack", True)
                            else:
                                textbutton _("ON "):
                                    text_style "KoGa3_1a_button_text"
                                    selected False
                                    action SetVariable ("persistent.KoGa3QuickMenuItemBack", False)

                    hbox:
                        hbox:
                            xsize 550
                            textbutton ("Button \"Hist\" (History) is:"):
                                text_style "KoGa3_1a_button_text"
                                sensitive False
                                action NullAction()
                        hbox:
                            xsize 200
                            if persistent.KoGa3QuickMenuItemHist == False:
                                textbutton _("OFF"):
                                    text_style "KoGa3_1a_button_text"
                                    selected False
                                    action SetVariable ("persistent.KoGa3QuickMenuItemHist", True)
                            else:
                                textbutton _("ON "):
                                    text_style "KoGa3_1a_button_text"
                                    selected False
                                    action SetVariable ("persistent.KoGa3QuickMenuItemHist", False)

                    hbox:
                        hbox:
                            xsize 550
                            textbutton ("Button \"Hide\" (hide textbox) is:"):
                                text_style "KoGa3_1a_button_text"
                                sensitive False
                                action NullAction()
                        hbox:
                            xsize 200
                            if persistent.KoGa3QuickMenuItemHide == False:
                                textbutton _("OFF"):
                                    text_style "KoGa3_1a_button_text"
                                    selected False
                                    action SetVariable ("persistent.KoGa3QuickMenuItemHide", True)
                            else:
                                textbutton _("ON "):
                                    text_style "KoGa3_1a_button_text"
                                    selected False
                                    action SetVariable ("persistent.KoGa3QuickMenuItemHide", False)

                    hbox:
                        hbox:
                            xsize 550
                            textbutton ("Button \"Skip\" is:"):
                                text_style "KoGa3_1a_button_text"
                                sensitive False
                                action NullAction()
                        hbox:
                            xsize 200
                            if persistent.KoGa3QuickMenuItemSkip == False:
                                textbutton _("OFF"):
                                    text_style "KoGa3_1a_button_text"
                                    selected False
                                    action SetVariable ("persistent.KoGa3QuickMenuItemSkip", True)
                            else:
                                textbutton _("ON "):
                                    text_style "KoGa3_1a_button_text"
                                    selected False
                                    action SetVariable ("persistent.KoGa3QuickMenuItemSkip", False)

                    hbox:
                        hbox:
                            xsize 550
                            textbutton ("Button \"Auto\" is:"):
                                text_style "KoGa3_1a_button_text"
                                sensitive False
                                action NullAction()
                        hbox:
                            xsize 200
                            if persistent.KoGa3QuickMenuItemAuto == False:
                                textbutton _("OFF"):
                                    text_style "KoGa3_1a_button_text"
                                    selected False
                                    action SetVariable ("persistent.KoGa3QuickMenuItemAuto", True)
                            else:
                                textbutton _("ON "):
                                    text_style "KoGa3_1a_button_text"
                                    selected False
                                    action SetVariable ("persistent.KoGa3QuickMenuItemAuto", False)

                    hbox:
                        hbox:
                            xsize 550
                            textbutton ("Button \"Save\" is:"):
                                text_style "KoGa3_1a_button_text"
                                sensitive False
                                action NullAction()
                        hbox:
                            xsize 200
                            if persistent.KoGa3QuickMenuItemSave == False:
                                textbutton _("OFF"):
                                    text_style "KoGa3_1a_button_text"
                                    selected False
                                    action SetVariable ("persistent.KoGa3QuickMenuItemSave", True)
                            else:
                                textbutton _("ON "):
                                    text_style "KoGa3_1a_button_text"
                                    selected False
                                    action SetVariable ("persistent.KoGa3QuickMenuItemSave", False)

                    hbox:
                        hbox:
                            xsize 550
                            textbutton ("Button \"Load\" is:"):
                                text_style "KoGa3_1a_button_text"
                                sensitive False
                                action NullAction()
                        hbox:
                            xsize 200
                            if persistent.KoGa3QuickMenuItemLoad == False:
                                textbutton _("OFF"):
                                    text_style "KoGa3_1a_button_text"
                                    selected False
                                    action SetVariable ("persistent.KoGa3QuickMenuItemLoad", True)
                            else:
                                textbutton _("ON "):
                                    text_style "KoGa3_1a_button_text"
                                    selected False
                                    action SetVariable ("persistent.KoGa3QuickMenuItemLoad", False)

                    hbox:
                        hbox:
                            xsize 550
                            textbutton ("Button \"Q.Save\" is:"):
                                text_style "KoGa3_1a_button_text"
                                sensitive False
                                action NullAction()
                        hbox:
                            xsize 200
                            if persistent.KoGa3QuickMenuItemQSave == False:
                                textbutton _("OFF"):
                                    text_style "KoGa3_1a_button_text"
                                    selected False
                                    action SetVariable ("persistent.KoGa3QuickMenuItemQSave", True)
                            else:
                                textbutton _("ON "):
                                    text_style "KoGa3_1a_button_text"
                                    selected False
                                    action SetVariable ("persistent.KoGa3QuickMenuItemQSave", False)

                    hbox:
                        hbox:
                            xsize 550
                            textbutton ("Button \"Q.Load\" is:"):
                                text_style "KoGa3_1a_button_text"
                                sensitive False
                                action NullAction()
                        hbox:
                            xsize 200
                            if persistent.KoGa3QuickMenuItemQLoad == False:
                                textbutton _("OFF"):
                                    text_style "KoGa3_1a_button_text"
                                    selected False
                                    action SetVariable ("persistent.KoGa3QuickMenuItemQLoad", True)
                            else:
                                textbutton _("ON "):
                                    text_style "KoGa3_1a_button_text"
                                    selected False
                                    action SetVariable ("persistent.KoGa3QuickMenuItemQLoad", False)

                    hbox:
                        hbox:
                            xsize 550
                            textbutton ("Button \"Prefs\" (game settings) is:"):
                                text_style "KoGa3_1a_button_text"
                                sensitive False
                                action NullAction()
                        hbox:
                            xsize 200
                            if persistent.KoGa3QuickMenuItemPrefs == False:
                                textbutton _("OFF"):
                                    text_style "KoGa3_1a_button_text"
                                    selected False
                                    action SetVariable ("persistent.KoGa3QuickMenuItemPrefs", True)
                            else:
                                textbutton _("ON "):
                                    text_style "KoGa3_1a_button_text"
                                    selected False
                                    action SetVariable ("persistent.KoGa3QuickMenuItemPrefs", False)

                    hbox:
                        hbox:
                            xsize 550
                            textbutton ("Button \"Mod menu\" is:"):
                                text_style "KoGa3_1a_button_text"
                                sensitive False
                                action NullAction()
                        hbox:
                            xsize 200
                            if persistent.KoGa3QuickMenuItemModmenu == False:
                                textbutton _("OFF"):
                                    text_style "KoGa3_1a_button_text"
                                    selected False
                                    action SetVariable ("persistent.KoGa3QuickMenuItemModmenu", True)
                            else:
                                textbutton _("ON "):
                                    text_style "KoGa3_1a_button_text"
                                    selected False
                                    action SetVariable ("persistent.KoGa3QuickMenuItemModmenu", False)

        textbutton ("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"):
            text_style "KoGa3_1_button_text"
            sensitive False
            action NullAction()

        hbox:
            spacing 30
            textbutton _("Back"):
                text_style "KoGa3_1_button_text"
                selected False
                sensitive True
                action [
                Hide("KoGa3GameSettingsQuickMenu"), 
                # Hide("KoGa3ScreenBlank"), 
                Show("KoGa3GameSettings") ]
            textbutton _("Close"):
                text_style "KoGa3_1_button_text"
                selected False
                sensitive True
                action [
                SetVariable ("KoGa3ModMenuButtonPressed", False),
                Hide("KoGa3ScreenBlank"), 
                Hide("KoGa3ScreenCheat"), 
                Hide("KoGa3ScreenCheatMore1"), 
                Hide("KoGa3ScreenModMenu"), 
                Hide("KoGa3ScreenJukebox"), 
                Hide("KoGa3GameSettings"), 
                Hide("KoGa3GameSettingsQuickMenu"), 
                Hide("KoGa3ScreenAudioMenu") ] 




#---------------------music---------------------#

#Game menu, Options:
define MusicMainMenu = "/music/Introspection.mp3"       #changed with v0.2
define MusicMenu1 = "/music/Introspection.mp3"          #changed with v0.2


#Home themes:
define MusicHome1 = "/music/Medicine.mp3"

#MC themes:
define MusicMC1 = "/music/Wake up and smile.mp3"
define MusicMC2 = "/music/Inspiring ABM_2.mp3"
define MusicMC3 = "/music/Minimal Corporate Ambient.mp3"#new with V0.3
define MusicMC4 = "/music/Places Of Happy People.mp3"   #new with V0.12
define MusicMC5 = "/music/Abstract Fantasy.mp3"         #new with V0.20
define MusicMC6 = "/music/Sehnsucht.mp3"                #new with V0.22 / also MusicChristine1
define MusicMC7 = "/music/Fly Away.mp3"                 #new with V0.23

#Home themes / Party Themes:
define MusicMark1 = "/music/Drive.mp3"
define MusicParty1 = "/music/Drive.mp3"
define MusicParty2 = "/music/Groove Day.mp3"            #new with V0.2 / also MusicSexy6
define MusicParty3 = "/music/fearless-first.mp3"        #new with V0.2
define MusicParty4 = "/music/Sweet heat.mp3"            #new with V0.17
define MusicParty5 = "/music/Crystal Motions.mp3"       #new with V0.18

#Rachel themes:
define MusicRachel1 = "/music/Ear Candy.mp3"

#Maya themes:
define MusicMaya1 = "/music/Night Chase - Raz Burg.mp3"

#Lily themes:
define MusicLily1 = "/music/Medical.mp3"                #new with V0.7

#Tasha themes:
define MusicTasha1 = "/music/Where I Find You_cut.mp3"  #new with V0.10

#Christine themes:
define MusicChristine1 = "/music/Sehnsucht.mp3"         #new with V0.13 / also MusicMC6

#Serious themes:
define MusicSerious1 = "/music/Exiled.mp3"              #new with V0.11
define MusicSerious1a = "<from 22>/music/Exiled.mp3"    #(new with V0.11)
define MusicSerious2 = "/music/Bitcoin.mp3"             #new with V0.11
define MusicSerious3 = "/music/Annihilation.mp3"        #new with V0.38

#Sexy themes:
define MusicSexy1 = "/music/Sexy.mp3"
define MusicSexy2 = "/music/Immersion.mp3"
define MusicSexy3 = "/music/Causmic_Contact.mp3"        #new with V0.2
define MusicSexy3a = "<from 21>/music/Causmic_Contact.mp3" #new with V0.53
define MusicSexy4 = "/music/Scientistication.mp3"       #new with V0.6
define MusicSexy5 = "/music/Inspirational Pop.mp3"      #new with V0.7
define MusicSexy6 = "/music/Groove Day.mp3"             #new with V0.2 / also MusicParty2
define MusicSexy7 = "/music/Cosmic Glow.mp3"            #new with V0.12
define MusicSexy7a = "<from 22>/music/Cosmic Glow.mp3"  #new with V0.13
define MusicSexy8 = "/music/Technological.mp3"          #new with V0.15
define MusicSexy9 = "/music/Decibel - Research.mp3"     #new with V0.17
define MusicSexy10 = "/music/Gold Skies.mp3"            #new with V0.26
define MusicSexy10a = "<from 10>/music/Gold Skies.mp3"  #new with V0.26
define MusicSexy11 = "/music/Cybernetics.mp3"           #new with V0.35

#Silence:
define MusicSilence = "<silence 10.0>"


#Original music tracks
define Musictevery_so_often = "audio/every-so-often.ogg"
define Musicmillennial_bonefire = "audio/millennial-bonefire.ogg"
define Musicharem_avenue = "audio/harem-avenue.ogg"
define Musiceau_de_summer = "audio/eau-de-summer.ogg"               #new with v0.6
define Musicmy_foster_castle = "audio/my-foster-castle.ogg"         #new with v0.6



#---------------------audio effects V2020-06-13---------------------#
#sound effects#
define audio.Alarm_Beep_01_5x = "/audio/Alarm_Beep_01.mp3"
#define audio.Beep_01 = "/audio/Beep_01.mp3"
#define audio.Birds_Chirping_01 = "/audio/Birds-Chirping_01.mp3"
#define audio.Bone_Cracking_01 = "/audio/Bone-Cracking_01.mp3"
#define audio.Bump_01 = "/audio/Bump_01.mp3"
#define audio.Car_Horn_01 = "/audio/Car-Horn_01.mp3"
#define audio.Cat_Meow_01 = "<from 0.0 to 1.0>/audio/Cat-Meow_01.mp3"
#define audio.Cat_Meow_02 = "<from 4.7 to 5.8>/audio/Cat-Meow_01.mp3"
#define audio.Cat_Purr_01 = "/audio/Cat-Purr_01.mp3"
#define audio.Cha_Ching_01 = "/audio/Cha-Ching_01.mp3"
#define audio.Door_Breaking_01 = "/audio/Door-Breaking_01.mp3"
#define audio.Door_close_01 = "/audio/Door-close_01.mp3"
#define audio.Door_Lock_01 = "/audio/Door-Lock_01.mp3"
define audio.Door_Open_01 = "/audio/Door-open_01.mp3"
define audio.Door_Open_Close_01 = "/audio/Door-Open-Close_01.mp3"
define audio.Door_Open_Close_01a = "<from 0 to 1.0>/audio/Door-Open-Close_01.mp3"
define audio.Door_Open_Close_01b = "<from 2.2 to 2.9>/audio/Door-Open-Close_01.mp3"
define audio.Door_Open_Close_02 = "/audio/Door-Open-Close_02.mp3"
define audio.Door_Open_Close_02a = "<from 3.5 to 4.3>/audio/Door-Open-Close_02.mp3"
define audio.Door_Open_Close_02b = "<from 0 to 0.8>/audio/Door-Open-Close_02.mp3"
#define audio.Door_Slam_01 = "/audio/Door-Slam_01.mp3"
define audio.Doorbell_01 = "/audio/Doorbell_01.mp3"
#define audio.Eat_Munch_01 = "/audio/Eat-Munch_01.mp3"
#define audio.Elevator_01 = "/audio/Elevator_01.mp3"
#define audio.Flamethrower_01 = "/audio/Flamethrower_01.mp3"
define audio.Glass_clinking_01 = "/audio/Glass-clinking_01.mp3"
#define audio.Gun_cocking_01 = "/audio/Gun_cocking_01.mp3"
#define audio.Gunshot_02 = "/audio/Gunshot_02.mp3"
#define audio.Hiss_01 = "/audio/Hiss_01.mp3"
define audio.Knock_01 = "/audio/Knock_01.mp3"   # info: 3x
define audio.Knock_01_2x = "<from 0.00 to 0.44>/audio/Knock_01.mp3"
define audio.Knock_01_4x = [ "<from 0.00 to 0.44>/audio/Knock_01.mp3", "<from 0.00 to 0.44>/audio/Knock_01.mp3" ]
#define audio.Knock_02 = "/audio/Knock_02.mp3"
#define audio.Music_Loud_01 = "/audio/Music-Loud_01.mp3"
#define  audio.Noise_01 = "/audio/Noise_01.mp3"
#define audio.Phone_buzzer_01_1x = "<from 0.15 to 1.4>/audio/Phone-Buzzer_01.mp3"
#define audio.Phone_buzzer_01_2x = "/audio/Phone-Buzzer_01.mp3"
#define audio.Phone_Dialing_01 = "/audio/Phone-Dialing_01.mp3"
#define audio.Phone_Dialing_01a = "<from 0.0 to 1.5>/audio/Phone-Dialing_01.mp3"
#define audio.Phone_Dialing_01b = "<from 1.9 to 3.4>/audio/Phone-Dialing_01.mp3"
define audio.Phone_Hungup_01 = "<from 0.0 to 0.3>/audio/Phone-Hungup_01.mp3"
#define audio.Phone_Notification_01 = "/audio/Phone-Notification_01.mp3"
#define audio.Phone_Notification_01a = "<from 0.0 to 0.35>/audio/Phone-Notification_01.mp3"
#define audio.Phone_Notification_02 = "/audio/Phone-Notification_02.mp3"
define audio.Phone_Ringing_01 = "<from 0.0 to 3.0>/audio/Phone-Ringing_01.mp3"
#define audio.Punch_01 = "/audio/Punch_01.mp3"
#define audio.Punch_02 = "/audio/Punch_02.mp3"
#define audio.Punch_03 = "/audio/Punch_03.mp3"
define audio.Punch_04 = "/audio/Punch_04.mp3"
#define audio.Rustle_01 = "/audio/Rustle_01.mp3"
#define audio.Rustle_02 = "/audio/Rustle_02.mp3"         #added 06.06.2020#
#define audio.School_Bell_01 = "/audio/School-Bell_01.mp3"
#define audio.Scratch_01 = "/audio/Scratch_01.mp3"
define audio.shop_doorbell_01 = "/audio/shop-doorbell_01.mp3"
#define audio.Slap_01 = "/audio/Slap_01.mp3"
#define audio.TaDa_01 = "/audio/TaDa_01.mp3"
#define audio.Toilet_Flush_01 = "/audio/Toilet-Flush_01.mp3"
#define audio.Zipper_01 = "/audio/Zipper_01.mp3"         #added 06.06.2020#


#human sounds - female#
#define audio.Female_Aah_01 = "/audio/Female-Aah_01.mp3"
#define audio.Female_Aahh_01 = "/audio/Female-Aahh_01.mp3"
#define audio.Female_Aahh_02 = "/audio/Female-Aahh_02.mp3"
#define audio.Female_Agh_01 = "/audio/Female-Agh_01.mp3"
#define audio.Female_Agh_02 = "/audio/Female-Agh_02.mp3"
#define audio.Female_Ah_01 = "/audio/Female-Ah_01.mp3"
#define audio.Female_Ah_02 = "/audio/Female-Ah_02.mp3"
#define audio.Female_Ah_03 = "/audio/Female-Ah_03.mp3"
#define audio.Female_Ahem_01 = "/audio/Female-Ahem_01.mp3"
#define audio.Female_Ahem_02 = "/audio/Female-Ahem_02.mp3"
#define audio.Female_Ahh_02 = "/audio/Female-Ahh_02.mp3"
#define audio.Female_Ahh_03 = "/audio/Female-Ahh_03.mp3"
#define audio.Female_Ahmm_01 = "/audio/Female-Ahmm_01.mp3"
define audio.Female_Breathe_01 = "<from 0.0 to 0.9>/audio/Female-Breathe_01.mp3"
define audio.Female_Breathe_01a = "<from 0.9 to 2.9>/audio/Female-Breathe_01.mp3"
define audio.Female_Breathe_01_2x = "/audio/Female-Breathe_01.mp3"
#define audio.Female_Breathe_01a = "<from 0.95 to 1.65>/audio/Female-Breathe_01.mp3"
#define audio.Female_Caugh_01_1x = "<from 1.0 to 1.5>/audio/Female-Caugh_01.mp3"
#define audio.Female_Caugh_01_2x = "<from 0.5 to 1.5>/audio/Female-Caugh_01.mp3"
#define audio.Female_Caugh_01_3x = "/audio/Female-Caugh_01.mp3"
#define audio.Female_Cry_01 = "</audio/Female-Cry_01.mp3"  #full, 4.5sec)
#define audio.Female_Cry_01a = "<from 1.8 to 2.4>/audio/Female-Cry_01.mp3"  #sniff#
#define audio.Female_Cry_01b = "<from 0.0 to 1.1>/audio/Female-Cry_01.mp3"  #short1#
#define audio.Female_Cry_01c = "<from 2.5 to 4.5>/audio/Female-Cry_01.mp3"  #short2#
#define audio.Female_Eww_01 = "/audio/Female-Eww_01.mp3"
#define audio.Female_Gasp_01 = "/audio/Female-Gasp_01.mp3"
#define audio.Female_Gasp_02 = "/audio/Female-Gasp_02.mp3"
define audio.Female_Gasp_03a = "/audio/Female-Gasp_03a.mp3"
#define audio.Female_Giggle_01 = "/audio/Female-Giggle_01.mp3"
#define audio.Female_Giggle_01_2x = "<from 0.35 to 0.85>/audio/Female-Giggle_01.mp3"
#define audio.Female_Hah_01 = "/audio/Female-Hah_01.mp3"
#define audio.Female_Hahh_01 = "/audio/Female-Hahh_01.mp3"
#define audio.Female_Hm_01 = "/audio/Female-Hm_01.mp3"
#define audio.Female_Hm_01a = "/audio/Female-Hm_01a.mp3"
#define audio.Female_Hm_02 = "/audio/Female-Hm_02.mp3"
#define audio.Female_Hm_02a = "/audio/Female-Hm_02a.mp3"
#define audio.Female_Hm_03 = "/audio/Female-Hm_03.mp3"
#define audio.Female_Hm_04 = "/audio/Female-Hm_04.mp3"
#define audio.Female_Hm_05 = "/audio/Female-Hm_05.mp3"
#define audio.Female_Hmh_01 = "/audio/Female-Hmh_01.mp3"
define audio.Female_Hmm_01 = "/audio/Female-Hmm_01.mp3"
define audio.Female_Hmph_01 = "/audio/Female-Hmph_01.mp3"
#define audio.Female_Hngh_01 = "/audio/Female-Hngh_01.mp3"
#define audio.Female_Huh_01 = "/audio/Female-Huh_01.mp3"
#define audio.Female_Laugh_01_2x = "<from 0.9 to 1.4>/audio/Female-Laugh_01.mp3"
#define audio.Female_Laugh_01_3x = "<from 0.65 to 1.4>/audio/Female-Laugh_01.mp3"
#define audio.Female_Laugh_01a_2x = "<from 0.65 to 1.2>/audio/Female-Laugh_01.mp3"
#define audio.Female_Laugh_01a_3x = "<from 0.0 to 0.9>/audio/Female-Laugh_01.mp3"
#define audio.Female_Laugh_01_5x = "audio/Female-Laugh_01.mp3"
#define audio.Female_Laugh_02_1x = "<from 0.25 to 0.5>/audio/Female-Laugh_02.mp3"
#define audio.Female_Laugh_02_2x = "<from 0.25 to 1.2>/audio/Female-Laugh_02.mp3"
#define audio.Female_Laugh_02_3x = "/audio/Female-Laugh_02.mp3"
#define audio.Female_Laugh_03_2x = "<from 0.65 to 0.9>/audio/Female-Laugh_03.mp3"
#define audio.Female_Laugh_03_3x = "<from 0.5 to 0.9>/audio/Female-Laugh_03.mp3"
#define audio.Female_Laugh_03_4x = "/audio/Female-Laugh_03.mp3"
#define audio.Female_Laugh_04_2x = "<from 0.0 to 0.7>/audio/Female-Laugh_04.mp3"
#define audio.Female_Laugh_04_3x = "/audio/Female-Laugh_04.mp3"
#define audio.Female_Laugh_05_2x = "<from 0.4 to 0.8>/audio/Female-Laugh_05.mp3"
#define audio.Female_Laugh_05_3x = "<from 0.24 to 0.8>/audio/Female-Laugh_05.mp3"
#define audio.Female_Laugh_05_4x = "/audio/Female-Laugh_05.mp3"
#define audio.Female_Laugh_07_2x = "<from 0.2 to 0.65>/audio/Female-Laugh_07.mp3"
#define audio.Female_Laugh_07_3x = "<from 0.0 to 0.65>/audio/Female-Laugh_07.mp3"
#define audio.Female_Laugh_07_4x = "/audio/Female-Laugh_07.mp3"
#define audio.Female_Laugh_08_2x = "<from 0.5 to 1.05>/audio/Female-Laugh_08.mp3"
#define audio.Female_Laugh_08_3x = "/audio/Female-Laugh_08.mp3"
#define audio.Female_Mm_Hm_01 = "/audio/Female-Mm-Hm_01.mp3"
#define audio.Female_Moo_01 = "/audio/Female-Moo_01.mp3"
#define audio.Female_No_01 = "/audio/Female-No_01.mp3"
#define audio.Female_No_02 = "/audio/Female-No_02.mp3"
#define audio.Female_No_02a = "<from 0.45 to 1.70>/audio/Female-No_02.mp3"
#define audio.Female_No_03 = "/audio/Female-No_03.mp3"
#define audio.Female_Oh_01 = "/audio/Female-Oh_01.mp3"
#define audio.Female_Oh_Wow_01 = "/audio/Female-Oh-Wow_01.mp3"
#define audio.Female_Oh_Wow_01a = "<from 0.0 to 0.38>/audio/Female-Oh-Wow_01.mp3"
#define audio.Female_Oh_Wow_01b = "<from 0.38 to 1.0>/audio/Female-Oh-Wow_01.mp3"
#define audio.Female_Ohh_01 = "/audio/Female-Ohh_01.mp3"
#define audio.Female_Ohh_01a = "<from 1.0 to 2.45>/audio/Female-Ohh_01.mp3"
#define audio.Female_Ohh_01b = "<from 0.0 to 0.85>/audio/Female-Ohh_01.mp3"
#define audio.Female_Oohh_01 = "/audio/Female-Oohh_01.mp3"
#define audio.Female_Panting_01_1x = "<from 0.0 to 1.8>/audio/Female-Panting_01.mp3"
#define audio.Female_Panting_01_2x = "<from 0.0 to 3.7>/audio/Female-Panting_01.mp3"
#define audio.Female_Panting_01_3x = "<from 0.0 to 5.5>/audio/Female-Panting_01.mp3"
define audio.Female_Panting_04_2x = "/audio/Female-Panting_04_2x.mp3"
#define audio.Female_Phew_01 = "/audio/Female-Phew_01.mp3"
#define audio.Female_scream_01 = "/audio/Female-scream_01.mp3"
#define audio.Female_scream_02 = "/audio/Female-scream_02.mp3"
#define audio.Female_scream_03 = "/audio/Female-scream_03.mp3"
#define audio.Female_Sigh_01 = "/audio/Female-Sigh_01.mp3"
#define audio.Female_Sigh_02 = "/audio/Female-Sigh_02.mp3"
#define audio.Female_Sigh_02a = "/audio/Female-Sigh_02a.mp3"
#define audio.Female_Sigh_03 = "/audio/Female-Sigh_03.mp3"
#define audio.Female_Sigh_04 = "/audio/Female-Sigh_04.mp3"
#define audio.Female_Strangle_01 = "/audio/Female-Strangle_01.mp3"
#define audio.Female_Strangle_01a = "<from 0.0 to 0.25>/audio/Female-Strangle_01.mp3"
#define audio.Female_Strangle_01b = "<from 0.5 to 1.05>/audio/Female-Strangle_01.mp3"
#define audio.Female_Tongue_out_01 = "/audio/Female-Tongue-out_01.mp3"
#define audio.Female_Wahoo_01 = "/audio/Female-Wahoo_01.mp3"
#define audio.Female_Whimper_01 = "/audio/Female-Whimper_01.mp3"
#define audio.Female_Yawn_01 = "/audio/Female-Yawn_01.mp3"
#define audio.Female_Yawn_02 = "/audio/Female-Yawn_02.mp3"
#define audio.Female_Yawn_03 = "/audio/Female-Yawn_03.mp3"


#human sounds - man#
#define audio.Man_Aaah_01 = "/audio/Man-Aaah_01.mp3"
#define audio.Man_Aaah_02 = "/audio/Man-Aaah_02.mp3"
#define audio.Man_Aaah_03 = "/audio/Man-Aaah_03.mp3"
#define audio.Man_Ah_01 = "/audio/Man-Ah_01.mp3"
#define audio.Man_Ah_02 = "/audio/Man-Ah_02.mp3"
#define audio.Man_Ah_03 = "/audio/Man-Ah_03.mp3"
#define audio.Man_Ahem_01 = "/audio/Man-Ahem_01.mp3"
#define audio.Man_Ahh_01 = "/audio/Man-Ahh_01.mp3"
#define audio.Man_Ahh_02 = "/audio/Man-Ahh_02.mp3"
#define audio.Man_Ahh_03 = "/audio/Man-Ahh_03.mp3"
#define audio.Man_Boo_01 = "/audio/Man-Boo_01.mp3"
#define audio.Man_AhHah_01 = "/audio/Man-AhHah_01.mp3"
#define audio.Man_Aw_01 = "/audio/Man-Aw_01.mp3"
#define audio.Man_Burp_01 = "/audio/Man-Burp_01.mp3"
#define audio.Man_Gasp_01 = "/audio/Man-Gasp_01.mp3"
#define audio.Man_Gasp_02 = "/audio/Man-Gasp_02.mp3"
#define audio.Man_Grunt_01 = "/audio/Man-Grunt_01.mp3"
#define audio.Man_Gulp_01 = "/audio/Man-Gulp_01.mp3"
#define audio.Man_Hm_01 = "/audio/Man-Hm_01.mp3"
#define audio.Man_Hm_02 = "/audio/Man-Hm_02.mp3"
#define audio.Man_Hmph_01 = "/audio/Man-Hmph_01.mp3"
#define audio.Man_Huh_01 = "/audio/Man-Huh_01.mp3"
#define audio.Man_Laugh_01_2x = "<from 0.37 to 0.8>/audio/Man-Laugh_01.mp3"
#define audio.Man_Laugh_01_3x = "/audio/Man-Laugh_01.mp3"
#define audio.Man_Laugh_01b_2x = "<from 0.20 to 0.65>/audio/Man-Laugh_01b.mp3"
#define audio.Man_Laugh_01b_3x = "/audio/Man-Laugh_01b.mp3"
#define audio.Man_Laugh_02_2x = "<from 0.0 to 0.65>/audio/Man-Laugh_02.mp3"
#define audio.Man_Laugh_02_3x = "/audio/Man-Laugh_02.mp3"  
#define audio.Man_Laugh_03_2x = "<from 0.2 to 0.6>/audio/Man-Laugh_03.mp3"   
#define audio.Man_Laugh_03_3x = "/audio/Man-Laugh_03.mp3"               #check!#
#define audio.Man_Laugh_04_2x = "<from 0.0 to 0.45>/audio/Man-Laugh_04.mp3"
#define audio.Man_Laugh_04_3x = "/audio/Man-Laugh_04.mp3"
#define audio.Man_Laugh_05_2x = "<from 0.0 to 0.5>/audio/Man-Laugh_05.mp3" 
#define audio.Man_Laugh_05_3x = "<from 0.0 to 0.8>/audio/Man-Laugh_05.mp3" 
#define audio.Man_Laugh_05_4x = "/audio/Man-Laugh_05.mp3"
#define audio.Man_Laugh_06_2x = "<from 1.7 to 2.1>/audio/Man-Laugh_06.mp3"
#define audio.Man_Laugh_06_3x = "<from 1.45 to 2.1>/audio/Man-Laugh_06.mp3"
#define audio.Man_Mmm_01 = "/audio/Man-Mmm_01.mp3"
#define audio.Man_Moan_Pain_01 = "/audio/Man-Moan-Pain_01.mp3"
#define audio.Man_Moan_Pain_01a = "<from 0.75 to 1.4>/audio/Man-Moan-Pain_01.mp3"
#define audio.Man_Noo_01 = "/audio/Man-Noo_01.mp3"
#define audio.Man_Oh_01 = "/audio/Man-Oh_01.mp3"
#define audio.Man_Oh_02 = "/audio/Man-Oh_02.mp3"    #(OhShit)
#define audio.Man_Oh_03 = "/audio/Man-Oh_03.mp3"
#define audio.Man_Panting_01 = "/audio/Man-Panting_01.mp3"
#define audio.Man_Scream_01 = "/audio/Man-Scream_01.mp3"
#define audio.Man_Shh_01 = "/audio/Man-Shh_01.mp3"
#define audio.Man_Sigh_01 = "/audio/Man-Sigh_01.mp3"
#define audio.Man_Sigh_02 = "/audio/Man-Sigh_02.mp3"
#define audio.Man_Sigh_03 = "/audio/Man-Sigh_03.mp3"
#define audio.Man_Ugh_01 = "/audio/Man-Ugh_01.mp3"
#define audio.Man_Ugh_02 = "/audio/Man-Ugh_02.mp3"
#define audio.Man_Umm_01 = "/audio/Man-Umm_01.mp3"
#define audio.Man_Whoa_01 = "/audio/Man-Whoa_01.mp3"
#define audio.Man_Yawn_01 = "/audio/Man-Yawn_01.mp3"
#define audio.Man_Yawn_02 = "/audio/Man-Yawn_02.mp3"


#human sounds - unisex#
#define audio.Human_Eat_Munch_01 = "/audio/Eat-Munch_01.mp3"
#define audio.Human_Hiss_02 = "/audio/Hiss_02.mp3"
#define audio.Human_Gag_01 = "/audio/Human-Gag_01.mp3"
#define audio.Human_Gulp_01 = "/audio/Human-Gulp_01.mp3"
#define audio.Human_Heartbeat_01 = "/audio/Human-Heartbeat_01.mp3"
#define audio.Human_Pissing_01 = "/audio/Human-Pissing_01.mp3"
#define audio.Human_Psst_01 = "/audio/Human-Psst_01.mp3"
#define audio.Human_Shh_01 = "/audio/Human-Shh_01.mp3"
#define audio.Human_Slurp_01 = "/audio/Human-Slurp_01.mp3"
#define audio.Human_Slurp_01a = "<from 0.2 to 2.0>/audio/Human-Slurp_01.mp3"
#define audio.Human_Slurp_02 = "/audio/Human-Slurp_02.mp3"
define audio.Human_Slurp_03 = "/audio/Human-Slurp_03.mp3"
define audio.Human_Slurp_03a = "/audio/Human-Slurp_03a.mp3"
#define audio.Human_Sniff_01 = "/audio/Human-Sniff_01.mp3"
#define audio.Human_Sniff_02 = "/audio/Human-Sniff_02.mp3"
#define audio.Human_Snore_01 = "/audio/Human-Snore_01.mp3"
#define audio.Human_Snore_01a = "<from 1.2 to 4.5>/audio/Human-Snore_01.mp3"
#define audio.Human_Toothbrush_01 = "/audio/Human-Toothbrush_01.mp3"
#define audio.Human_Whistle_01 = "/audio/Human-Whistle_01.mp3"
#define audio.Human_Whistle_02 = "/audio/Human-Whistle_02.mp3"
#define audio.Human_Whistle_03 = "/audio/Human-Whistle_03.mp3"


#--erotic moaning--#
#define audio.Female_Ah_04 = "/audio/Female-Ah_04.mp3"
#define audio.Female_Ah_04a = "<from 0.0 to 3.5>/audio/Female-Ah_04.mp3"
#define audio.Female_Ahh_01 = "/audio/Female-Ahh_01.mp3"
#define audio.Female_Ahh_04 = "/audio/Female-Ahh_04.mp3"
define audio.Female_Ahh_05 = "/audio/Female-Ahh_05.mp3"
define audio.Female_AhhHahHah_01 = "/audio/Female-AhhHahHah_01.mp3"
define audio.Female_AhhOh_01 = "/audio/Female-AhhOh_01.mp3"
define audio.Female_HahhHahhHahh_01 = "/audio/Female-HahhHahhHahh_01.mp3"
define audio.Female_Mm_01 = "/audio/Female-Mm_01.mp3"
#define audio.Female_Mm_01a = "<from 0.35 to 1.15>/audio/Female-Mm_01.mp3"
#define audio.Female_Mm_01b = "<from 0.0 to 0.4>/audio/Female-Mm_01.mp3"
#define audio.Female_Mm_01c = "<from 0.0 to 0.25>/audio/Female-Mm_01.mp3"
#define audio.Female_Mm_02 = "/audio/Female-Mm_02.mp3"
#define audio.Female_Mm_02a = "<from 0.0 to 1.6>/audio/Female-Mm_02.mp3"
#define audio.Female_Mm_02b = "<from 0.0 to 4.0>/audio/Female-Mm_02.mp3"
#define audio.Female_Mm_02c = "<from 5.5 to 7.0>/audio/Female-Mm_02.mp3"
#define audio.Female_Mm_02d = "<from 2.5 to 4.0>/audio/Female-Mm_02.mp3"
#define audio.Female_Mm_03 = "/audio/Female-Mm_03.mp3"
#define audio.Female_Mm_03a = "/audio/Female-Mm_03a.mp3"
define audio.Female_Mmm_01 = "/audio/Female-Mmm_01.mp3"
#define audio.Female_Mmm_02 = "/audio/Female-Mmm_02.mp3"
define audio.Female_Moan_01 = "/audio/Female-Moan_01.mp3"
#define audio.Female_Moan_02 = "/audio/Female-Moan_02.mp3"
#define audio.Female_Moan_03 = "/audio/Female-Moan_03.mp3"
define audio.Female_Moan_04 = "/audio/Female-Moan_04.mp3"
#define audio.Female_Moan_05 = "/audio/Female-Moan_05.mp3"
#define audio.Female_Moan_05a = "<from 0.0 to 0.9>/audio/Female-Moan_05.mp3"   #Mmm
#define audio.Female_Moan_06 = "/audio/Female-Moan_06.mp3"   #Ohh Ahh 7x
#define audio.Female_Moan_06a = "<from 0.9 to 1.6>/audio/Female-Moan_06.mp3"   #Ohh 1x
#define audio.Female_Moan_06b = "<from 0.0 to 2.4>/audio/Female-Moan_06.mp3"   #Ohh 3x
#define audio.Female_Moan_06c = "<from 2.4 to 3.3>/audio/Female-Moan_06.mp3"   #Ahh 1x
#define audio.Female_Moan_06d = "<from 3.3 to 5.3>/audio/Female-Moan_06.mp3"   #Ahh 2x
#define audio.Female_Moan_multi_01 = "/audio/Female-Moan-multi_01.mp3"
#define audio.Female_Moan_multi_01a = "<from 3.2 to 5.0>/audio/Female-Moan-multi_01.mp3"
define audio.Female_Ohh_02 = "/audio/Female-Ohh_02.mp3"
define audio.Human_Kiss_01 = "/audio/Human-Kiss_01.mp3"
define audio.Human_Kiss_01a = "/audio/Human-Kiss_01a.mp3"
define audio.Human_Kiss_02 = "/audio/Human-Kiss_02.mp3"
#define audio.Human_Kiss_03 = "/audio/Human-Kiss_03.mp3"
define audio.Human_Sex_01 = "/audio/Human-Sex_01.mp3"
define audio.Human_Sex_02 = "/audio/Human-Sex_02.mp3"
#define audio.Man_Ah_04 = "/audio/Man-Ah_04.mp3"
#define audio.Man_Ah_05 = "/audio/Man-Ah_05.mp3"
#define audio.Man_Ah_05a = "<from 0.0 to 1.5>/audio/Man-Ah_05.mp3"
#define audio.Man_Ah_05b = "<from 1.5 to 3.5>/audio/Man-Ah_05.mp3"
define audio.Man_Fapping_01 = "/audio/Man-Fapping_01.mp3"
define audio.Man_Fapping_02 = "/audio/Man-Fapping_02.mp3"
#define audio.Man_Mm_01 = "/audio/Man-Mm_01.mp3"
#define audio.Man_Moan_01 = "/audio/Man-Moan_01.mp3"
#define audio.Man_Moan_02 = "/audio/Man-Moan_02.mp3"


#---------------------set variable game beginning---------------------#

default KoGa3ModMenuButtonPressed = False
default KoGa3MainMenu = 0
default KoGa3DialogOptions = 1
default KoGa3QuickMenuOptions = 0
default KoGa3QuickMenuItems = 1
default KoGa3CheatButton = 1
default KoGa3CheatChapterButton = 1
default KoGa3ScreenStatsFull = 0
default KoGa3GameProgress = "n/a"
default KoGa3ChoiceOptions = 0

default KoGa3GalleryUnlock = 1
default KoGa3ModStart = 1

default KoGa3MusicChannel = 0
default KoGa3JukeboxButton = 1
default OriginalCurrentMusic = Musictevery_so_often
default KoGa3CurrentMusic = MusicMenu1
default KoGa3Music = 1    #variable music                                                   #WT: 0 / AudioWT: 1
default KoGa3SSound = 1   #variable sound effects              (bump, knock, ...)           #WT: 0 / AudioWT: 1
default KoGa3HSound = 1   #variable human sounds               (haha, sigh, shh,...)        #WT: 0 / AudioWT: 1
default KoGa3ESound = 1   #variable human erotic               (moaning and kissing)        #WT: 0 / AudioWT: 1



#---------------------set variable name setting---------------------#


#--------------settings best choice option---------------#
default KoGa3ChoiceOption = 1
default KoGa3ChoiceText1 = "\n{color=#008000}recommended by me{/color}"
default KoGa3ChoiceText1a = "\n{color=#008000}recommended by me so far{/color}"
default KoGa3ChoiceText2 = "\n{color=#0000ff}choice is not essential{/color}"
default KoGa3ChoiceText3 = "\n{color=#ff0000}bad choice{/color}"
default KoGa3ChoiceTextOFF = ""
default KoGa3ChoiceView1 = KoGa3ChoiceText1
default KoGa3ChoiceView1a = KoGa3ChoiceText1a
default KoGa3ChoiceView2 = KoGa3ChoiceText2
default KoGa3ChoiceView3 = KoGa3ChoiceText3

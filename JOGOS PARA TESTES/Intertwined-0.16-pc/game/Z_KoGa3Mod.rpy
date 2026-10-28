
#Mod for the game Intertwined  / KoGa3#

# new audio channel for the game
# init python:
    # renpy.music.register_channel("sound1", mixer="sfx")
    # renpy.music.register_channel("sound2", mixer="sfx")
    # renpy.music.register_channel("music1", mixer="music")


#jukebox playing time conversion
# init python:
    # def convert_float_into_time(t):
        # i, f = divmod(t, 1)
        # i = int(i)
        # m, s = divmod(i, 60)
        # h, m = divmod(m, 60)
        # return "{:02}:{:02}".format(m, s)

####### Info: defined game points from script.rpy #######
### Character Points
#Alexis_Points = 0
#Emily_Points = 0
#Melissa_Points = 0
#Erynn_Points = 0
#Layla_Points = 0
#Elena_Points = 0
#Nikki_Points = 0
#Cara_Points = 0
#Tori_Points = 0
#Adriana_Points = 0
#Gabi_Points = 0
#Naomi_Points = 0
#Natasha_Points = 0
#Lakeyn_Points = 0
#Valeria_Points = 0
#Sienna_Points = 0
#Brooke_Points = 0
#Zach_Points = 0
#Darryl_Points = 0
#Iris_Points = 0
#Mira_Points = 0
#ShaCarri_Points = 0        #not used in the Mod, not checked in the game
#Andres_Points = 0
#Ximena_Points = 0
#Marisol_Points = 0
#Alexis_SP = 0
#Nikki_SPoints = 0
### Event Points
#MC_GoodStudent = 0
#Nikki_Weekend_Points = 0
#Nikki_Visit_Points = 0
#Cara_Weekend_Points = 0
#Cara_Visit_Points = 0
#Alexis_JealousyPoints = 0
#Alexis_BeachPoints = 0
#Ethan_Punch = 0            #not used in the game so far
#Ethan_WallPunch = 0        #not used in the Mod, only checked once in that scene
#Gabi_Suspicion = 0
#Gabi_Jealousy = 0
####### Info: the followin "sex counters" in script.rpy are not used so far in my Mod #######


#---------------------shortcut key for Mod menu screen---------------------#
init python:
    # key: Shift + k.
    config.keymap['KoGa3ScreenCheat'] = "shift_K_k"
define config.overlay_screens = ["keymap", "quick_menu"]
screen keymap:
    key "KoGa3ScreenCheat":
        action [ 
        SetVariable ("Alexis_PointsTemp", Alexis_Points),
        SetVariable ("Emily_PointsTemp", Emily_Points),
        SetVariable ("Melissa_PointsTemp", Melissa_Points),
        SetVariable ("Erynn_PointsTemp", Erynn_Points),
        SetVariable ("Layla_PointsTemp", Layla_Points),
        SetVariable ("Elena_PointsTemp", Elena_Points),
        SetVariable ("Nikki_PointsTemp", Nikki_Points),
        SetVariable ("Cara_PointsTemp", Cara_Points),
        SetVariable ("Tori_PointsTemp", Tori_Points),
        SetVariable ("Adriana_PointsTemp", Adriana_Points),
        SetVariable ("Naomi_PointsTemp", Naomi_Points),
        SetVariable ("Nikki_Weekend_PointsTemp", Nikki_Weekend_Points),
        SetVariable ("Cara_Weekend_PointsTemp", Cara_Weekend_Points),
        SetVariable ("Gabi_PointsTemp", Gabi_Points),               #not checked in the game
        SetVariable ("Natasha_PointsTemp", Natasha_Points),         #not checked in the game
        SetVariable ("Lakeyn_PointsTemp", Lakeyn_Points),
        SetVariable ("Valeria_PointsTemp", Valeria_Points),
        SetVariable ("Sienna_PointsTemp", Sienna_Points),
        SetVariable ("Brooke_PointsTemp", Brooke_Points),
        SetVariable ("Iris_PointsTemp", Iris_Points),
        SetVariable ("Zach_PointsTemp", Zach_Points),
        SetVariable ("Nikki_Visit_PointsTemp", Nikki_Visit_Points),
        SetVariable ("Cara_Visit_PointsTemp", Cara_Visit_Points),
        SetVariable ("Alexis_JealousyPointsTemp", Alexis_JealousyPoints),
        SetVariable ("Mira_PointsTemp", Mira_Points),               #not checked in the game
        SetVariable ("Alexis_SPTemp", Alexis_SP),                   #added with v0.13
        SetVariable ("Nikki_SPointsTemp", Nikki_SPoints),           #new with v0.13
        SetVariable ("MC_GoodStudentTemp", MC_GoodStudent),         #new with v0.10.5
        SetVariable ("Alexis_BeachPointsTemp", Alexis_BeachPoints), #new with v0.11
        SetVariable ("Gabi_SuspicionTemp", Gabi_Suspicion),         #new with v0.14
        SetVariable ("Gabi_JealousyTemp", Gabi_Jealousy),           #new with v0.14
        SetVariable ("Andres_PointsTemp", Andres_Points),           #new with v0.14
        SetVariable ("Darryl_PointsTemp", Darryl_Points),           #new with v0.15
        SetVariable ("Marisol_PointsTemp", Marisol_Points),         #new with v0.15
        SetVariable ("Ximena_PointsTemp", Ximena_Points),           #new with v0.15
        SetVariable ("KoGa3ModMenuButtonPressed", True),
        Show("KoGa3ScreenCheat") ] 


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
define KoGa3Color3 = "#ffffff"      #{color=#ffffff}     {/color}

define KoGa3ModMenu_xsize1 = 425    #450
define KoGa3ModMenu_xsize2 = 100     #65
define KoGa3ModMenu_xsize3 = 125    #75
define KoGa3ModMenu_xsize4 = 90

define KoGa3ModMenu_xsize5 = 575
define KoGa3ModMenu_xsize6 = 225
define KoGa3ModMenu_xsize7 = 150


#---------------------blank screen---------------------#
screen KoGa3ScreenBlank:
    add "/KoGa3MenuBack.png"
    modal True


#---------------------Stats screen---------------------#
screen KoGa3ScreenStats():
    hbox:
        xalign 0.5
        yalign 0.0
        if KoGa3ScreenStatsFull == 0:   #"Dummy"
            #textbutton (""):
            textbutton (""):
                text_style KoGa3_status_button_text
                text_size 23
                selected False 
                action [ 
                SetVariable ("Alexis_PointsTemp", Alexis_Points),
                SetVariable ("Emily_PointsTemp", Emily_Points),
                SetVariable ("Melissa_PointsTemp", Melissa_Points),
                SetVariable ("Erynn_PointsTemp", Erynn_Points),
                SetVariable ("Layla_PointsTemp", Layla_Points),
                SetVariable ("Elena_PointsTemp", Elena_Points),
                SetVariable ("Nikki_PointsTemp", Nikki_Points),
                SetVariable ("Cara_PointsTemp", Cara_Points),
                SetVariable ("Tori_PointsTemp", Tori_Points),
                SetVariable ("Adriana_PointsTemp", Adriana_Points),
                SetVariable ("Naomi_PointsTemp", Naomi_Points),
                SetVariable ("Nikki_Weekend_PointsTemp", Nikki_Weekend_Points),
                SetVariable ("Cara_Weekend_PointsTemp", Cara_Weekend_Points),
                SetVariable ("Gabi_PointsTemp", Gabi_Points),               #not used
                SetVariable ("Natasha_PointsTemp", Natasha_Points),         #not used
                SetVariable ("Lakeyn_PointsTemp", Lakeyn_Points),
                SetVariable ("Valeria_PointsTemp", Valeria_Points),
                SetVariable ("Sienna_PointsTemp", Sienna_Points),
                SetVariable ("Brooke_PointsTemp", Brooke_Points),
                SetVariable ("Iris_PointsTemp", Iris_Points),
                SetVariable ("Zach_PointsTemp", Zach_Points),
                SetVariable ("Nikki_Visit_PointsTemp", Nikki_Visit_Points),
                SetVariable ("Cara_Visit_PointsTemp", Cara_Visit_Points),
                SetVariable ("Alexis_JealousyPointsTemp", Alexis_JealousyPoints),
                SetVariable ("Mira_PointsTemp", Mira_Points),               #not used
                SetVariable ("Alexis_SPTemp", Alexis_SP),                   #added with v0.13
                SetVariable ("Nikki_SPointsTemp", Nikki_SPoints),           #new with v0.13
                SetVariable ("MC_GoodStudentTemp", MC_GoodStudent),         #new with v0.10.5
                SetVariable ("Alexis_BeachPointsTemp", Alexis_BeachPoints), #new with v0.11
                SetVariable ("Gabi_SuspicionTemp", Gabi_Suspicion),         #new with v0.14
                SetVariable ("Gabi_JealousyTemp", Gabi_Jealousy),           #new with v0.14
                SetVariable ("Andres_PointsTemp", Andres_Points),           #new with v0.14
                SetVariable ("Darryl_PointsTemp", Darryl_Points),           #new with v0.15
                SetVariable ("Marisol_PointsTemp", Marisol_Points),         #new with v0.15
                SetVariable ("Ximena_PointsTemp", Ximena_Points),           #new with v0.15
                SetVariable ("KoGa3ModMenuButtonPressed", True),
                Show("KoGa3ScreenCheat") ] 
        if KoGa3ScreenStatsFull == 1 or KoGa3ScreenStatsFull == 2:
        #KoGa3ScreenStatsFull 1
            if KoGa3ScreenStatsFull == 1:
                textbutton ("Alexis:[Alexis_Points]  Emily:[Emily_Points]  Melissa:[Melissa_Points]  Layla:[Layla_Points]  Elena:[Elena_Points]  Erynn:[Erynn_Points]  Cara:[Cara_Points]  Nikki:[Nikki_Points]  Brooke:[Brooke_Points]  Adriana:[Adriana_Points]  Naomi:[Naomi_Points]  Tori:[Tori_Points]  Lakeyn:[Lakeyn_Points]  Iris:[Iris_Points]  Valeria:[Valeria_Points]  Sienna:[Sienna_Points]"):
                    text_style KoGa3_status_button_text
                    text_size 23
                    selected True 
                    action [ 
                    SetVariable ("Alexis_PointsTemp", Alexis_Points),
                    SetVariable ("Emily_PointsTemp", Emily_Points),
                    SetVariable ("Melissa_PointsTemp", Melissa_Points),
                    SetVariable ("Erynn_PointsTemp", Erynn_Points),
                    SetVariable ("Layla_PointsTemp", Layla_Points),
                    SetVariable ("Elena_PointsTemp", Elena_Points),
                    SetVariable ("Nikki_PointsTemp", Nikki_Points),
                    SetVariable ("Cara_PointsTemp", Cara_Points),
                    SetVariable ("Tori_PointsTemp", Tori_Points),
                    SetVariable ("Adriana_PointsTemp", Adriana_Points),
                    SetVariable ("Naomi_PointsTemp", Naomi_Points),
                    SetVariable ("Nikki_Weekend_PointsTemp", Nikki_Weekend_Points),
                    SetVariable ("Cara_Weekend_PointsTemp", Cara_Weekend_Points),
                    SetVariable ("Gabi_PointsTemp", Gabi_Points),               #not used
                    SetVariable ("Natasha_PointsTemp", Natasha_Points),         #not used
                    SetVariable ("Lakeyn_PointsTemp", Lakeyn_Points),
                    SetVariable ("Valeria_PointsTemp", Valeria_Points),
                    SetVariable ("Sienna_PointsTemp", Sienna_Points),
                    SetVariable ("Brooke_PointsTemp", Brooke_Points),
                    SetVariable ("Iris_PointsTemp", Iris_Points),
                    SetVariable ("Zach_PointsTemp", Zach_Points),
                    SetVariable ("Nikki_Visit_PointsTemp", Nikki_Visit_Points),
                    SetVariable ("Cara_Visit_PointsTemp", Cara_Visit_Points),
                    SetVariable ("Alexis_JealousyPointsTemp", Alexis_JealousyPoints),
                    SetVariable ("Mira_PointsTemp", Mira_Points),               #not used
                    SetVariable ("Alexis_SPTemp", Alexis_SP),                   #added with v0.13
                    SetVariable ("Nikki_SPointsTemp", Nikki_SPoints),           #new with v0.13
                    SetVariable ("MC_GoodStudentTemp", MC_GoodStudent),         #new with v0.10.5
                    SetVariable ("Alexis_BeachPointsTemp", Alexis_BeachPoints), #new with v0.11
                    SetVariable ("Gabi_SuspicionTemp", Gabi_Suspicion),         #new with v0.14
                    SetVariable ("Gabi_JealousyTemp", Gabi_Jealousy),           #new with v0.14
                    SetVariable ("Andres_PointsTemp", Andres_Points),           #new with v0.14
                    SetVariable ("Darryl_PointsTemp", Darryl_Points),           #new with v0.15
                    SetVariable ("Marisol_PointsTemp", Marisol_Points),         #new with v0.15
                    SetVariable ("Ximena_PointsTemp", Ximena_Points),           #new with v0.15
                    SetVariable ("KoGa3ModMenuButtonPressed", True),
                    Show("KoGa3ScreenCheat") ] 

                textbutton (">> "):
                    text_style KoGa3_status_button_text
                    text_size 23
                    selected False 
                    action [ 
                    SetVariable ("KoGa3ScreenStatsFull", 2) ]

            if KoGa3ScreenStatsFull == 2:
            #KoGa3ScreenStatsFull 2
                textbutton ("Andres:[Andres_Points]  Darryl:[Darryl_Points]  Marisol:[Marisol_Points]  Ximena:[Ximena_Points]  Zach:[Zach_Points]  Alexis beach:[Alexis_BeachPointsTemp]  Alexis SP:[Alexis_SP]  Cara-Wkd:[Cara_Weekend_Points]  Cara-Vis:[Cara_Visit_Points]  Nikki-Wkd:[Nikki_Weekend_Points]  Nikki-Vis:[Nikki_Visit_Points]  Nikki SP:[Nikki_SPoints]  Gabi jealousy:[Gabi_Jealousy] "):
                    text_style KoGa3_status_button_text
                    text_size 23
                    selected True 
                    action [ 
                    SetVariable ("Alexis_PointsTemp", Alexis_Points),
                    SetVariable ("Emily_PointsTemp", Emily_Points),
                    SetVariable ("Melissa_PointsTemp", Melissa_Points),
                    SetVariable ("Erynn_PointsTemp", Erynn_Points),
                    SetVariable ("Layla_PointsTemp", Layla_Points),
                    SetVariable ("Elena_PointsTemp", Elena_Points),
                    SetVariable ("Nikki_PointsTemp", Nikki_Points),
                    SetVariable ("Cara_PointsTemp", Cara_Points),
                    SetVariable ("Tori_PointsTemp", Tori_Points),
                    SetVariable ("Adriana_PointsTemp", Adriana_Points),
                    SetVariable ("Naomi_PointsTemp", Naomi_Points),
                    SetVariable ("Nikki_Weekend_PointsTemp", Nikki_Weekend_Points),
                    SetVariable ("Cara_Weekend_PointsTemp", Cara_Weekend_Points),
                    SetVariable ("Gabi_PointsTemp", Gabi_Points),               #not used
                    SetVariable ("Natasha_PointsTemp", Natasha_Points),         #not used
                    SetVariable ("Lakeyn_PointsTemp", Lakeyn_Points),
                    SetVariable ("Valeria_PointsTemp", Valeria_Points),
                    SetVariable ("Sienna_PointsTemp", Sienna_Points),
                    SetVariable ("Brooke_PointsTemp", Brooke_Points),
                    SetVariable ("Iris_PointsTemp", Iris_Points),
                    SetVariable ("Zach_PointsTemp", Zach_Points),
                    SetVariable ("Nikki_Visit_PointsTemp", Nikki_Visit_Points),
                    SetVariable ("Cara_Visit_PointsTemp", Cara_Visit_Points),
                    SetVariable ("Alexis_JealousyPointsTemp", Alexis_JealousyPoints),
                    SetVariable ("Mira_PointsTemp", Mira_Points),               #not used
                    SetVariable ("Alexis_SPTemp", Alexis_SP),                   #added with v0.13
                    SetVariable ("Nikki_SPointsTemp", Nikki_SPoints),           #new with v0.13
                    SetVariable ("MC_GoodStudentTemp", MC_GoodStudent),         #new with v0.10.5
                    SetVariable ("Alexis_BeachPointsTemp", Alexis_BeachPoints), #new with v0.11
                    SetVariable ("Gabi_SuspicionTemp", Gabi_Suspicion),         #new with v0.14
                    SetVariable ("Gabi_JealousyTemp", Gabi_Jealousy),           #new with v0.14
                    SetVariable ("Andres_PointsTemp", Andres_Points),           #new with v0.14
                    SetVariable ("Darryl_PointsTemp", Darryl_Points),           #new with v0.15
                    SetVariable ("Marisol_PointsTemp", Marisol_Points),         #new with v0.15
                    SetVariable ("Ximena_PointsTemp", Ximena_Points),           #new with v0.15
                    SetVariable ("KoGa3ModMenuButtonPressed", True),
                    Show("KoGa3ScreenCheat") ] 

                textbutton ("<< "):
                    text_style KoGa3_status_button_text
                    text_size 23
                    selected False 
                    action [ 
                    SetVariable ("KoGa3ScreenStatsFull", 1) ]


#---------------------Cheat menu---------------------#
screen KoGa3ScreenCheat:
    add "/KoGa3MenuBack.png"
    modal True
    vbox:
        xalign 0.5
        spacing -12
        null height (54)

        textbutton _("━━━━━━━━━━━━━━━━━━━ Mod menu ━━━━━━━━━━━━━━━━━━━"):
            text_style "KoGa3_1_button_text"
            sensitive False
            action NullAction()

        if not renpy.loadable("1Mod.rpyc"):

            hbox:
                textbutton ("Game progress (info):  [KoGa3GameProgress]"):
                    text_style "KoGa3_1a_button_text"
                    sensitive False
                    action NullAction()

        hbox:
            textbutton _("Additional game settings..."):
                text_style "KoGa3_1_button_text"
                selected False
                sensitive True
                action [ 
                Hide("KoGa3ScreenCheat"),
                Show("KoGa3GameSettings") ]

        textbutton ("────────────────────────────────────────────────"):
            text_style "KoGa3_1_button_text"
            sensitive False
            action NullAction()

        if _in_replay:
            hbox:
                spacing 15
                textbutton ("(in Replay not available)"):
                    text_style "KoGa3_1_button_text"
                    sensitive False
                    action NullAction()
        else:
            hbox:
                spacing 15
                textbutton ("Relationships:"):
                    text_style "KoGa3_1_button_text"
                    sensitive False
                    action NullAction()
                if KoGa3CheatButton is 1:
                    textbutton ("Ep1-3"):
                        text_style "KoGa3_1_button_text"
                        selected True
                        action NullAction()
                else:
                    textbutton ("Ep1-3"):
                        text_style "KoGa3_1_button_text"
                        selected False
                        action [
                        SetVariable("KoGa3CheatButton", 1) ]
                if KoGa3CheatButton is 2:
                    textbutton ("Ep4-7"):
                        text_style "KoGa3_1_button_text"
                        selected True
                        action NullAction()
                else:
                    textbutton ("Ep4-7"):
                        text_style "KoGa3_1_button_text"
                        selected False
                        action [
                        SetVariable("KoGa3CheatButton", 2) ]
                if KoGa3CheatButton is 3:
                    textbutton ("Ep8-11"):
                        text_style "KoGa3_1_button_text"
                        selected True
                        action NullAction()
                else:
                    textbutton ("Ep8-11"):
                        text_style "KoGa3_1_button_text"
                        selected False
                        action [
                        SetVariable("KoGa3CheatButton", 3) ]
                if KoGa3CheatButton is 4:
                    textbutton ("Ep12-15"):
                        text_style "KoGa3_1_button_text"
                        selected True
                        action NullAction()
                else:
                    textbutton ("Ep12-15"):
                        text_style "KoGa3_1_button_text"
                        selected False
                        action [
                        SetVariable("KoGa3CheatButton", 4) ]

                if KoGa3CheatButton is 5:
                    textbutton ("More"):
                        text_style "KoGa3_1_button_text"
                        selected True
                        action NullAction()
                else:
                    textbutton ("More"):
                        text_style "KoGa3_1_button_text"
                        selected False
                        action [
                        SetVariable("KoGa3CheatButton", 5) ]
            textbutton ("────────────────────────────────────────────────"):
                text_style "KoGa3_1_button_text"
                sensitive False
                action NullAction()
            if KoGa3CheatButton == 1:   #Ep1-3
                hbox:
                    hbox:
                        xsize KoGa3ModMenu_xsize1
                        textbutton "EP1: Alexis Points:":
                            text_style "KoGa3_1_button_text"
                            sensitive False
                            action NullAction()
                    hbox:
                        xsize KoGa3ModMenu_xsize2
                        textbutton "{color=[KoGa3Color3]}[Alexis_Points]":
                            text_style "KoGa3_1_button_text"
                            sensitive False
                            action NullAction()
                    hbox:
                        xsize KoGa3ModMenu_xsize2
                        textbutton _("+1") text_style "KoGa3_1_button_text" action SetVariable("Alexis_Points", Alexis_Points +1)
                    hbox:
                        xsize KoGa3ModMenu_xsize2
                        #if Alexis_Points >= 1:
                        textbutton _("-1") text_style "KoGa3_1_button_text" action SetVariable("Alexis_Points", Alexis_Points -1)
                    hbox:
                        xsize KoGa3ModMenu_xsize3
                        if Alexis_Points != Alexis_PointsTemp:
                            textbutton ("Reset") text_style "KoGa3_1_button_text" action SetVariable("Alexis_Points", Alexis_PointsTemp)

                hbox:
                    hbox:
                        xsize KoGa3ModMenu_xsize1
                        textbutton "EP1: Emily Points:":
                            text_style "KoGa3_1_button_text"
                            sensitive False
                            action NullAction()
                    hbox:
                        xsize KoGa3ModMenu_xsize2
                        textbutton "{color=[KoGa3Color3]}[Emily_Points]":
                            text_style "KoGa3_1_button_text"
                            sensitive False
                            action NullAction()
                    hbox:
                        xsize KoGa3ModMenu_xsize2
                        textbutton _("+1") text_style "KoGa3_1_button_text" action SetVariable("Emily_Points", Emily_Points +1)
                    hbox:
                        xsize KoGa3ModMenu_xsize2
                        #if Emily_Points >= 1:
                        textbutton _("-1") text_style "KoGa3_1_button_text" action SetVariable("Emily_Points", Emily_Points -1)
                    hbox:
                        xsize KoGa3ModMenu_xsize3
                        if Emily_Points != Emily_PointsTemp:
                            textbutton ("Reset") text_style "KoGa3_1_button_text" action SetVariable("Emily_Points", Emily_PointsTemp)

                hbox:
                    hbox:
                        xsize KoGa3ModMenu_xsize1
                        textbutton "EP1: Melissa Points:":
                            text_style "KoGa3_1_button_text"
                            sensitive False
                            action NullAction()
                    hbox:
                        xsize KoGa3ModMenu_xsize2
                        textbutton "{color=[KoGa3Color3]}[Melissa_Points]":
                            text_style "KoGa3_1_button_text"
                            sensitive False
                            action NullAction()
                    hbox:
                        xsize KoGa3ModMenu_xsize2
                        textbutton _("+1") text_style "KoGa3_1_button_text" action SetVariable("Melissa_Points", Melissa_Points +1)
                    hbox:
                        xsize KoGa3ModMenu_xsize2
                        #if Melissa_Points >= 1:
                        textbutton _("-1") text_style "KoGa3_1_button_text" action SetVariable("Melissa_Points", Melissa_Points -1)
                    hbox:
                        xsize KoGa3ModMenu_xsize3
                        if Melissa_Points != Melissa_PointsTemp:
                            textbutton ("Reset") text_style "KoGa3_1_button_text" action SetVariable("Melissa_Points", Melissa_PointsTemp)

                hbox:
                    hbox:
                        xsize KoGa3ModMenu_xsize1
                        textbutton "EP1: MC good student:":
                            text_style "KoGa3_1_button_text"
                            sensitive False
                            action NullAction()
                    hbox:
                        xsize KoGa3ModMenu_xsize2
                        textbutton "{color=[KoGa3Color3]}[MC_GoodStudent]":
                            text_style "KoGa3_1_button_text"
                            sensitive False
                            action NullAction()
                    hbox:
                        xsize KoGa3ModMenu_xsize2
                        textbutton _("+1") text_style "KoGa3_1_button_text" action SetVariable("MC_GoodStudent", MC_GoodStudent +1)
                    hbox:
                        xsize KoGa3ModMenu_xsize2
                        #if MC_GoodStudent >= 1:
                        textbutton _("-1") text_style "KoGa3_1_button_text" action SetVariable("MC_GoodStudent", MC_GoodStudent -1)
                    hbox:
                        xsize KoGa3ModMenu_xsize3
                        if MC_GoodStudent != MC_GoodStudentTemp:
                            textbutton ("Reset") text_style "KoGa3_1_button_text" action SetVariable("MC_GoodStudent", MC_GoodStudentTemp)

                hbox:
                    hbox:
                        xsize KoGa3ModMenu_xsize1
                        textbutton "EP2: Layla Points:":
                            text_style "KoGa3_1_button_text"
                            sensitive False
                            action NullAction()
                    hbox:
                        xsize KoGa3ModMenu_xsize2
                        textbutton "{color=[KoGa3Color3]}[Layla_Points]":
                            text_style "KoGa3_1_button_text"
                            sensitive False
                            action NullAction()
                    hbox:
                        xsize KoGa3ModMenu_xsize2
                        textbutton _("+1") text_style "KoGa3_1_button_text" action SetVariable("Layla_Points", Layla_Points +1)
                    hbox:
                        xsize KoGa3ModMenu_xsize2
                        #if Layla_Points >= 1:
                        textbutton _("-1") text_style "KoGa3_1_button_text" action SetVariable("Layla_Points", Layla_Points -1)
                    hbox:
                        xsize KoGa3ModMenu_xsize3
                        if Layla_Points != Layla_PointsTemp:
                            textbutton ("Reset") text_style "KoGa3_1_button_text" action SetVariable("Layla_Points", Layla_PointsTemp)

                hbox:
                    hbox:
                        xsize KoGa3ModMenu_xsize1
                        textbutton "EP2: Elena Points:":
                            text_style "KoGa3_1_button_text"
                            sensitive False
                            action NullAction()
                    hbox:
                        xsize KoGa3ModMenu_xsize2
                        textbutton "{color=[KoGa3Color3]}[Elena_Points]":
                            text_style "KoGa3_1_button_text"
                            sensitive False
                            action NullAction()
                    hbox:
                        xsize KoGa3ModMenu_xsize2
                        textbutton _("+1") text_style "KoGa3_1_button_text" action SetVariable("Elena_Points", Elena_Points +1)
                    hbox:
                        xsize KoGa3ModMenu_xsize2
                        #if Elena_Points >= 1:
                        textbutton _("-1") text_style "KoGa3_1_button_text" action SetVariable("Elena_Points", Elena_Points -1)
                    hbox:
                        xsize KoGa3ModMenu_xsize3
                        if Elena_Points != Elena_PointsTemp:
                            textbutton ("Reset") text_style "KoGa3_1_button_text" action SetVariable("Elena_Points", Elena_PointsTemp)

                hbox:
                    hbox:
                        xsize KoGa3ModMenu_xsize1
                        textbutton "EP3: Erynn Points:":
                            text_style "KoGa3_1_button_text"
                            sensitive False
                            action NullAction()
                    hbox:
                        xsize KoGa3ModMenu_xsize2
                        textbutton "{color=[KoGa3Color3]}[Erynn_Points]":
                            text_style "KoGa3_1_button_text"
                            sensitive False
                            action NullAction()
                    hbox:
                        xsize KoGa3ModMenu_xsize2
                        textbutton _("+1") text_style "KoGa3_1_button_text" action SetVariable("Erynn_Points", Erynn_Points +1)
                    hbox:
                        xsize KoGa3ModMenu_xsize2
                        #if Erynn_Points >= 1:
                        textbutton _("-1") text_style "KoGa3_1_button_text" action SetVariable("Erynn_Points", Erynn_Points -1)
                    hbox:
                        xsize KoGa3ModMenu_xsize3
                        if Erynn_Points != Erynn_PointsTemp:
                            textbutton ("Reset") text_style "KoGa3_1_button_text" action SetVariable("Erynn_Points", Erynn_PointsTemp)

                hbox:
                    hbox:
                        xsize KoGa3ModMenu_xsize1
                        textbutton "EP3: Tori Points:":
                            text_style "KoGa3_1_button_text"
                            sensitive False
                            action NullAction()
                    hbox:
                        xsize KoGa3ModMenu_xsize2
                        textbutton "{color=[KoGa3Color3]}[Tori_Points]":
                            text_style "KoGa3_1_button_text"
                            sensitive False
                            action NullAction()
                    hbox:
                        xsize KoGa3ModMenu_xsize2
                        textbutton _("+1") text_style "KoGa3_1_button_text" action SetVariable("Tori_Points", Tori_Points +1)
                    hbox:
                        xsize KoGa3ModMenu_xsize2
                        #if Tori_Points >= 1:
                        textbutton _("-1") text_style "KoGa3_1_button_text" action SetVariable("Tori_Points", Tori_Points -1)
                    hbox:
                        xsize KoGa3ModMenu_xsize3
                        if Tori_Points != Tori_PointsTemp:
                            textbutton ("Reset") text_style "KoGa3_1_button_text" action SetVariable("Tori_Points", Tori_PointsTemp)

            if KoGa3CheatButton == 2:   #Ep4-7
                hbox:
                    hbox:
                        xsize KoGa3ModMenu_xsize1
                        textbutton "EP4: Cara Points:":
                            text_style "KoGa3_1_button_text"
                            sensitive False
                            action NullAction()
                    hbox:
                        xsize KoGa3ModMenu_xsize2
                        textbutton "{color=[KoGa3Color3]}[Cara_Points]":
                            text_style "KoGa3_1_button_text"
                            sensitive False
                            action NullAction()
                    hbox:
                        xsize KoGa3ModMenu_xsize2
                        textbutton _("+1") text_style "KoGa3_1_button_text" action SetVariable("Cara_Points", Cara_Points +1)
                    hbox:
                        xsize KoGa3ModMenu_xsize2
                        #if Cara_Points >= 1:
                        textbutton _("-1") text_style "KoGa3_1_button_text" action SetVariable("Cara_Points", Cara_Points -1)
                    hbox:
                        xsize KoGa3ModMenu_xsize3
                        if Cara_Points != Cara_PointsTemp:
                            textbutton ("Reset") text_style "KoGa3_1_button_text" action SetVariable("Cara_Points", Cara_PointsTemp)

                hbox:
                    hbox:
                        xsize KoGa3ModMenu_xsize1
                        textbutton "EP4: Nikki Points:":
                            text_style "KoGa3_1_button_text"
                            sensitive False
                            action NullAction()
                    hbox:
                        xsize KoGa3ModMenu_xsize2
                        textbutton "{color=[KoGa3Color3]}[Nikki_Points]":
                            text_style "KoGa3_1_button_text"
                            sensitive False
                            action NullAction()
                    hbox:
                        xsize KoGa3ModMenu_xsize2
                        textbutton _("+1") text_style "KoGa3_1_button_text" action SetVariable("Nikki_Points", Nikki_Points +1)
                    hbox:
                        xsize KoGa3ModMenu_xsize2
                        #if Nikki_Points >= 1:
                        textbutton _("-1") text_style "KoGa3_1_button_text" action SetVariable("Nikki_Points", Nikki_Points -1)
                    hbox:
                        xsize KoGa3ModMenu_xsize3
                        if Nikki_Points != Nikki_PointsTemp:
                            textbutton ("Reset") text_style "KoGa3_1_button_text" action SetVariable("Nikki_Points", Nikki_PointsTemp)

                hbox:
                    hbox:
                        xsize KoGa3ModMenu_xsize1
                        textbutton "EP4: Lakeyn Points:":
                            text_style "KoGa3_1_button_text"
                            sensitive False
                            action NullAction()
                    hbox:
                        xsize KoGa3ModMenu_xsize2
                        textbutton "{color=[KoGa3Color3]}[Lakeyn_Points]":
                            text_style "KoGa3_1_button_text"
                            sensitive False
                            action NullAction()
                    hbox:
                        xsize KoGa3ModMenu_xsize2
                        textbutton _("+1") text_style "KoGa3_1_button_text" action SetVariable("Lakeyn_Points", Lakeyn_Points +1)
                    hbox:
                        xsize KoGa3ModMenu_xsize2
                        #if Lakeyn_Points >= 1:
                        textbutton _("-1") text_style "KoGa3_1_button_text" action SetVariable("Lakeyn_Points", Lakeyn_Points -1)
                    hbox:
                        xsize KoGa3ModMenu_xsize3
                        if Lakeyn_Points != Lakeyn_PointsTemp:
                            textbutton ("Reset") text_style "KoGa3_1_button_text" action SetVariable("Lakeyn_Points", Lakeyn_PointsTemp)

                hbox:
                    hbox:
                        xsize KoGa3ModMenu_xsize1
                        textbutton "EP4: Brooke Points:":
                            text_style "KoGa3_1_button_text"
                            sensitive False
                            action NullAction()
                    hbox:
                        xsize KoGa3ModMenu_xsize2
                        textbutton "{color=[KoGa3Color3]}[Brooke_Points]":
                            text_style "KoGa3_1_button_text"
                            sensitive False
                            action NullAction()
                    hbox:
                        xsize KoGa3ModMenu_xsize2
                        textbutton _("+1") text_style "KoGa3_1_button_text" action SetVariable("Brooke_Points", Brooke_Points +1)
                    hbox:
                        xsize KoGa3ModMenu_xsize2
                        #if Brooke_Points >= 1:
                        textbutton _("-1") text_style "KoGa3_1_button_text" action SetVariable("Brooke_Points", Brooke_Points -1)
                    hbox:
                        xsize KoGa3ModMenu_xsize3
                        if Brooke_Points != Brooke_PointsTemp:
                            textbutton ("Reset") text_style "KoGa3_1_button_text" action SetVariable("Brooke_Points", Brooke_PointsTemp)

                hbox:
                    hbox:
                        xsize KoGa3ModMenu_xsize1
                        textbutton "EP5: Adriana Points:":
                            text_style "KoGa3_1_button_text"
                            sensitive False
                            action NullAction()
                    hbox:
                        xsize KoGa3ModMenu_xsize2
                        textbutton "{color=[KoGa3Color3]}[Adriana_Points]":
                            text_style "KoGa3_1_button_text"
                            sensitive False
                            action NullAction()
                    hbox:
                        xsize KoGa3ModMenu_xsize2
                        textbutton _("+1") text_style "KoGa3_1_button_text" action SetVariable("Adriana_Points", Adriana_Points +1)
                    hbox:
                        xsize KoGa3ModMenu_xsize2
                        #if Adriana_Points >= 1:
                        textbutton _("-1") text_style "KoGa3_1_button_text" action SetVariable("Adriana_Points", Adriana_Points -1)
                    hbox:
                        xsize KoGa3ModMenu_xsize3
                        if Adriana_Points != Adriana_PointsTemp:
                            textbutton ("Reset") text_style "KoGa3_1_button_text" action SetVariable("Adriana_Points", Adriana_PointsTemp)

                hbox:
                    hbox:
                        xsize KoGa3ModMenu_xsize1
                        textbutton "EP6: Naomi Points:":
                            text_style "KoGa3_1_button_text"
                            sensitive False
                            action NullAction()
                    hbox:
                        xsize KoGa3ModMenu_xsize2
                        textbutton "{color=[KoGa3Color3]}[Naomi_Points]":
                            text_style "KoGa3_1_button_text"
                            sensitive False
                            action NullAction()
                    hbox:
                        xsize KoGa3ModMenu_xsize2
                        textbutton _("+1") text_style "KoGa3_1_button_text" action SetVariable("Naomi_Points", Naomi_Points +1)
                    hbox:
                        xsize KoGa3ModMenu_xsize2
                        #if Naomi_Points >= 1:
                        textbutton _("-1") text_style "KoGa3_1_button_text" action SetVariable("Naomi_Points", Naomi_Points -1)
                    hbox:
                        xsize KoGa3ModMenu_xsize3
                        if Naomi_Points != Naomi_PointsTemp:
                            textbutton ("Reset") text_style "KoGa3_1_button_text" action SetVariable("Naomi_Points", Naomi_PointsTemp)

                hbox:
                    hbox:
                        xsize KoGa3ModMenu_xsize1
                        textbutton "EP6: Cara Weekend:":
                            text_style "KoGa3_1_button_text"
                            sensitive False
                            action NullAction()
                    hbox:
                        xsize KoGa3ModMenu_xsize2
                        textbutton "{color=[KoGa3Color3]}[Cara_Weekend_Points]":
                            text_style "KoGa3_1_button_text"
                            sensitive False
                            action NullAction()
                    hbox:
                        xsize KoGa3ModMenu_xsize2
                        textbutton _("+1") text_style "KoGa3_1_button_text" action SetVariable("Cara_Weekend_Points", Cara_Weekend_Points +1)
                    hbox:
                        xsize KoGa3ModMenu_xsize2
                        #if Cara_Weekend_Points >= 1:
                        textbutton _("-1") text_style "KoGa3_1_button_text" action SetVariable("Cara_Weekend_Points", Cara_Weekend_Points -1)
                    hbox:
                        xsize KoGa3ModMenu_xsize3
                        if Cara_Weekend_Points != Cara_Weekend_PointsTemp:
                            textbutton ("Reset") text_style "KoGa3_1_button_text" action SetVariable("Cara_Weekend_Points", Cara_Weekend_PointsTemp)

                hbox:
                    hbox:
                        xsize KoGa3ModMenu_xsize1
                        textbutton "EP6: Nikki Weekend:":
                            text_style "KoGa3_1_button_text"
                            sensitive False
                            action NullAction()
                    hbox:
                        xsize KoGa3ModMenu_xsize2
                        textbutton "{color=[KoGa3Color3]}[Nikki_Weekend_Points]":
                            text_style "KoGa3_1_button_text"
                            sensitive False
                            action NullAction()
                    hbox:
                        xsize KoGa3ModMenu_xsize2
                        textbutton _("+1") text_style "KoGa3_1_button_text" action SetVariable("Nikki_Weekend_Points", Nikki_Weekend_Points +1)
                    hbox:
                        xsize KoGa3ModMenu_xsize2
                        #if Nikki_Weekend_Points >= 1:
                        textbutton _("-1") text_style "KoGa3_1_button_text" action SetVariable("Nikki_Weekend_Points", Nikki_Weekend_Points -1)
                    hbox:
                        xsize KoGa3ModMenu_xsize3
                        if Nikki_Weekend_Points != Nikki_Weekend_PointsTemp:
                            textbutton ("Reset") text_style "KoGa3_1_button_text" action SetVariable("Nikki_Weekend_Points", Nikki_Weekend_PointsTemp)

            if KoGa3CheatButton == 3:   #Ep8-11

                hbox:
                    hbox:
                        xsize KoGa3ModMenu_xsize1
                        textbutton "EP8: Valeria Points:":
                            text_style "KoGa3_1_button_text"
                            sensitive False
                            action NullAction()
                    hbox:
                        xsize KoGa3ModMenu_xsize2
                        textbutton "{color=[KoGa3Color3]}[Valeria_Points]":
                            text_style "KoGa3_1_button_text"
                            sensitive False
                            action NullAction()
                    hbox:
                        xsize KoGa3ModMenu_xsize2
                        textbutton _("+1") text_style "KoGa3_1_button_text" action SetVariable("Valeria_Points", Valeria_Points +1)
                    hbox:
                        xsize KoGa3ModMenu_xsize2
                        #if Valeria_Points >= 1:
                        textbutton _("-1") text_style "KoGa3_1_button_text" action SetVariable("Valeria_Points", Valeria_Points -1)
                    hbox:
                        xsize KoGa3ModMenu_xsize3
                        if Valeria_Points != Valeria_PointsTemp:
                            textbutton ("Reset") text_style "KoGa3_1_button_text" action SetVariable("Valeria_Points", Valeria_PointsTemp)

                hbox:
                    hbox:
                        xsize KoGa3ModMenu_xsize1
                        textbutton "EP8: Iris Points:":
                            text_style "KoGa3_1_button_text"
                            sensitive False
                            action NullAction()
                    hbox:
                        xsize KoGa3ModMenu_xsize2
                        textbutton "{color=[KoGa3Color3]}[Iris_Points]":
                            text_style "KoGa3_1_button_text"
                            sensitive False
                            action NullAction()
                    hbox:
                        xsize KoGa3ModMenu_xsize2
                        textbutton _("+1") text_style "KoGa3_1_button_text" action SetVariable("Iris_Points", Iris_Points +1)
                    hbox:
                        xsize KoGa3ModMenu_xsize2
                        #if Iris_Points >= 1:
                        textbutton _("-1") text_style "KoGa3_1_button_text" action SetVariable("Iris_Points", Iris_Points -1)
                    hbox:
                        xsize KoGa3ModMenu_xsize3
                        if Iris_Points != Iris_PointsTemp:
                            textbutton ("Reset") text_style "KoGa3_1_button_text" action SetVariable("Iris_Points", Iris_PointsTemp)

                hbox:
                    hbox:
                        xsize KoGa3ModMenu_xsize1
                        textbutton "EP8: Zach Points:":
                            text_style "KoGa3_1_button_text"
                            sensitive False
                            action NullAction()
                    hbox:
                        xsize KoGa3ModMenu_xsize2
                        textbutton "{color=[KoGa3Color3]}[Zach_Points]":
                            text_style "KoGa3_1_button_text"
                            sensitive False
                            action NullAction()
                    hbox:
                        xsize KoGa3ModMenu_xsize2
                        textbutton _("+1") text_style "KoGa3_1_button_text" action SetVariable("Zach_Points", Zach_Points +1)
                    hbox:
                        xsize KoGa3ModMenu_xsize2
                        #if Zach_Points >= 1:
                        textbutton _("-1") text_style "KoGa3_1_button_text" action SetVariable("Zach_Points", Zach_Points -1)
                    hbox:
                        xsize KoGa3ModMenu_xsize3
                        if Zach_Points != Zach_PointsTemp:
                            textbutton ("Reset") text_style "KoGa3_1_button_text" action SetVariable("Zach_Points", Zach_PointsTemp)

                hbox:
                    hbox:
                        xsize KoGa3ModMenu_xsize1
                        textbutton "EP8: Alexis SP:":
                            text_style "KoGa3_1_button_text"
                            sensitive False
                            action NullAction()
                    hbox:
                        xsize KoGa3ModMenu_xsize2
                        textbutton "{color=[KoGa3Color3]}[Alexis_SP]":
                            text_style "KoGa3_1_button_text"
                            sensitive False
                            action NullAction()
                    hbox:
                        xsize KoGa3ModMenu_xsize2
                        textbutton _("+1") text_style "KoGa3_1_button_text" action SetVariable("Alexis_SP", Alexis_SP +1)
                    hbox:
                        xsize KoGa3ModMenu_xsize2
                        #if Alexis_SP >= 1:
                        textbutton _("-1") text_style "KoGa3_1_button_text" action SetVariable("Alexis_SP", Alexis_SP -1)
                    hbox:
                        xsize KoGa3ModMenu_xsize3
                        if Alexis_SP != Alexis_SPTemp:
                            textbutton ("Reset") text_style "KoGa3_1_button_text" action SetVariable("Alexis_SP", Alexis_SPTemp)

                hbox:
                    hbox:
                        xsize KoGa3ModMenu_xsize1
                        textbutton "EP8: Alexis Jealousy:":
                            text_style "KoGa3_1_button_text"
                            sensitive False
                            action NullAction()
                    hbox:
                        xsize KoGa3ModMenu_xsize2
                        textbutton "{color=[KoGa3Color3]}[Alexis_JealousyPoints]":
                            text_style "KoGa3_1_button_text"
                            sensitive False
                            action NullAction()
                    hbox:
                        xsize KoGa3ModMenu_xsize2
                        textbutton _("+1") text_style "KoGa3_1_button_text" action SetVariable("Alexis_JealousyPoints", Alexis_JealousyPoints +1)
                    hbox:
                        xsize KoGa3ModMenu_xsize2
                        #if Alexis_JealousyPoints >= 1:
                        textbutton _("-1") text_style "KoGa3_1_button_text" action SetVariable("Alexis_JealousyPoints", Alexis_JealousyPoints -1)
                    hbox:
                        xsize KoGa3ModMenu_xsize3
                        if Alexis_JealousyPoints != Alexis_JealousyPointsTemp:
                            textbutton ("Reset") text_style "KoGa3_1_button_text" action SetVariable("Alexis_JealousyPoints", Alexis_JealousyPointsTemp)

                hbox:
                    hbox:
                        xsize KoGa3ModMenu_xsize1
                        textbutton "EP8: Darryl Points:":
                            text_style "KoGa3_1_button_text"
                            sensitive False
                            action NullAction()
                    hbox:
                        xsize KoGa3ModMenu_xsize2
                        textbutton "{color=[KoGa3Color3]}[Darryl_Points]":
                            text_style "KoGa3_1_button_text"
                            sensitive False
                            action NullAction()
                    hbox:
                        xsize KoGa3ModMenu_xsize2
                        textbutton _("+1") text_style "KoGa3_1_button_text" action SetVariable("Darryl_Points", Darryl_Points +1)
                    hbox:
                        xsize KoGa3ModMenu_xsize2
                        #if Darryl_Points >= 1:
                        textbutton _("-1") text_style "KoGa3_1_button_text" action SetVariable("Darryl_Points", Darryl_Points -1)
                    hbox:
                        xsize KoGa3ModMenu_xsize3
                        if Darryl_Points != Darryl_PointsTemp:
                            textbutton ("Reset") text_style "KoGa3_1_button_text" action SetVariable("Darryl_Points", Darryl_PointsTemp)

                hbox:
                    hbox:
                        xsize KoGa3ModMenu_xsize1
                        textbutton "EP9: Nikki Visit Points:":
                            text_style "KoGa3_1_button_text"
                            sensitive False
                            action NullAction()
                    hbox:
                        xsize KoGa3ModMenu_xsize2
                        textbutton "{color=[KoGa3Color3]}[Nikki_Visit_Points]":
                            text_style "KoGa3_1_button_text"
                            sensitive False
                            action NullAction()
                    hbox:
                        xsize KoGa3ModMenu_xsize2
                        textbutton _("+1") text_style "KoGa3_1_button_text" action SetVariable("Nikki_Visit_Points", Nikki_Visit_Points +1)
                    hbox:
                        xsize KoGa3ModMenu_xsize2
                        #if Nikki_Visit_Points >= 1:
                        textbutton _("-1") text_style "KoGa3_1_button_text" action SetVariable("Nikki_Visit_Points", Nikki_Visit_Points -1)
                    hbox:
                        xsize KoGa3ModMenu_xsize3
                        if Nikki_Visit_Points != Nikki_Visit_PointsTemp:
                            textbutton ("Reset") text_style "KoGa3_1_button_text" action SetVariable("Nikki_Visit_Points", Nikki_Visit_PointsTemp)

                hbox:
                    hbox:
                        xsize KoGa3ModMenu_xsize1
                        textbutton "EP9: Cara Visit Points:":
                            text_style "KoGa3_1_button_text"
                            sensitive False
                            action NullAction()
                    hbox:
                        xsize KoGa3ModMenu_xsize2
                        textbutton "{color=[KoGa3Color3]}[Cara_Visit_Points]":
                            text_style "KoGa3_1_button_text"
                            sensitive False
                            action NullAction()
                    hbox:
                        xsize KoGa3ModMenu_xsize2
                        textbutton _("+1") text_style "KoGa3_1_button_text" action SetVariable("Cara_Visit_Points", Cara_Visit_Points +1)
                    hbox:
                        xsize KoGa3ModMenu_xsize2
                        #if Cara_Visit_Points >= 1:
                        textbutton _("-1") text_style "KoGa3_1_button_text" action SetVariable("Cara_Visit_Points", Cara_Visit_Points -1)
                    hbox:
                        xsize KoGa3ModMenu_xsize3
                        if Cara_Visit_Points != Cara_Visit_PointsTemp:
                            textbutton ("Reset") text_style "KoGa3_1_button_text" action SetVariable("Cara_Visit_Points", Cara_Visit_PointsTemp)

                hbox:
                    hbox:
                        xsize KoGa3ModMenu_xsize1
                        textbutton "EP11: Sienna Points:":
                            text_style "KoGa3_1_button_text"
                            sensitive False
                            action NullAction()
                    hbox:
                        xsize KoGa3ModMenu_xsize2
                        textbutton "{color=[KoGa3Color3]}[Sienna_Points]":
                            text_style "KoGa3_1_button_text"
                            sensitive False
                            action NullAction()
                    hbox:
                        xsize KoGa3ModMenu_xsize2
                        textbutton _("+1") text_style "KoGa3_1_button_text" action SetVariable("Sienna_Points", Sienna_Points +1)
                    hbox:
                        xsize KoGa3ModMenu_xsize2
                        #if Sienna_Points >= 1:
                        textbutton _("-1") text_style "KoGa3_1_button_text" action SetVariable("Sienna_Points", Sienna_Points -1)
                    hbox:
                        xsize KoGa3ModMenu_xsize3
                        if Sienna_Points != Sienna_PointsTemp:
                            textbutton ("Reset") text_style "KoGa3_1_button_text" action SetVariable("Sienna_Points", Sienna_PointsTemp)

                hbox:
                    hbox:
                        xsize KoGa3ModMenu_xsize1
                        textbutton "EP11: Alexis Beach Points:":
                            text_style "KoGa3_1_button_text"
                            sensitive False
                            action NullAction()
                    hbox:
                        xsize KoGa3ModMenu_xsize2
                        textbutton "{color=[KoGa3Color3]}[Alexis_BeachPoints]":
                            text_style "KoGa3_1_button_text"
                            sensitive False
                            action NullAction()
                    hbox:
                        xsize KoGa3ModMenu_xsize2
                        textbutton _("+1") text_style "KoGa3_1_button_text" action SetVariable("Alexis_BeachPoints", Alexis_BeachPoints +1)
                    hbox:
                        xsize KoGa3ModMenu_xsize2
                        #if Alexis_BeachPointsTemp >= 1:
                        textbutton _("-1") text_style "KoGa3_1_button_text" action SetVariable("Alexis_BeachPoints", Alexis_BeachPoints -1)
                    hbox:
                        xsize KoGa3ModMenu_xsize3
                        if Alexis_BeachPoints != Alexis_BeachPointsTemp:
                            textbutton ("Reset") text_style "KoGa3_1_button_text" action SetVariable("Alexis_BeachPoints", Alexis_BeachPointsTemp)

            if KoGa3CheatButton == 4:   #Ep12-15
                hbox:
                    hbox:
                        xsize KoGa3ModMenu_xsize1
                        textbutton "EP13: Nikki SPoints:":
                            text_style "KoGa3_1_button_text"
                            sensitive False
                            action NullAction()
                    hbox:
                        xsize KoGa3ModMenu_xsize2
                        textbutton "{color=[KoGa3Color3]}[Nikki_SPoints]":
                            text_style "KoGa3_1_button_text"
                            sensitive False
                            action NullAction()
                    hbox:
                        xsize KoGa3ModMenu_xsize2
                        textbutton _("+1") text_style "KoGa3_1_button_text" action SetVariable("Nikki_SPoints", Nikki_SPoints +1)
                    hbox:
                        xsize KoGa3ModMenu_xsize2
                        #if Nikki_SPointsTemp >= 1:
                        textbutton _("-1") text_style "KoGa3_1_button_text" action SetVariable("Nikki_SPoints", Nikki_SPoints -1)
                    hbox:
                        xsize KoGa3ModMenu_xsize3
                        if Nikki_SPoints != Nikki_SPointsTemp:
                            textbutton ("Reset") text_style "KoGa3_1_button_text" action SetVariable("Nikki_SPoints", Nikki_SPointsTemp)

                hbox:
                    hbox:
                        xsize KoGa3ModMenu_xsize1
                        textbutton "EP14: Andres Points:":
                            text_style "KoGa3_1_button_text"
                            sensitive False
                            action NullAction()
                    hbox:
                        xsize KoGa3ModMenu_xsize2
                        textbutton "{color=[KoGa3Color3]}[Andres_Points]":
                            text_style "KoGa3_1_button_text"
                            sensitive False
                            action NullAction()
                    hbox:
                        xsize KoGa3ModMenu_xsize2
                        textbutton _("+1") text_style "KoGa3_1_button_text" action SetVariable("Andres_Points", Andres_Points +1)
                    hbox:
                        xsize KoGa3ModMenu_xsize2
                        #if Andres_PointsTemp >= 1:
                        textbutton _("-1") text_style "KoGa3_1_button_text" action SetVariable("Andres_Points", Andres_Points -1)
                    hbox:
                        xsize KoGa3ModMenu_xsize3
                        if Andres_Points != Andres_PointsTemp:
                            textbutton ("Reset") text_style "KoGa3_1_button_text" action SetVariable("Andres_Points", Andres_PointsTemp)

                hbox:
                    hbox:
                        xsize KoGa3ModMenu_xsize1
                        textbutton "EP14: Gabi Jealousy:":
                            text_style "KoGa3_1_button_text"
                            sensitive False
                            action NullAction()
                    hbox:
                        xsize KoGa3ModMenu_xsize2
                        textbutton "{color=[KoGa3Color3]}[Gabi_Jealousy]":
                            text_style "KoGa3_1_button_text"
                            sensitive False
                            action NullAction()
                    hbox:
                        xsize KoGa3ModMenu_xsize2
                        textbutton _("+1") text_style "KoGa3_1_button_text" action SetVariable("Gabi_Jealousy", Gabi_Jealousy +1)
                    hbox:
                        xsize KoGa3ModMenu_xsize2
                        #if Gabi_JealousyTemp >= 1:
                        textbutton _("-1") text_style "KoGa3_1_button_text" action SetVariable("Gabi_Jealousy", Gabi_Jealousy -1)
                    hbox:
                        xsize KoGa3ModMenu_xsize3
                        if Gabi_Jealousy != Gabi_JealousyTemp:
                            textbutton ("Reset") text_style "KoGa3_1_button_text" action SetVariable("Gabi_Jealousy", Gabi_JealousyTemp)

                hbox:
                    hbox:
                        xsize KoGa3ModMenu_xsize1
                        textbutton "EP14: Gabi Suspicion:":
                            text_style "KoGa3_1_button_text"
                            sensitive False
                            action NullAction()
                    hbox:
                        xsize KoGa3ModMenu_xsize2
                        textbutton "{color=[KoGa3Color3]}[Gabi_Suspicion]":
                            text_style "KoGa3_1_button_text"
                            sensitive False
                            action NullAction()
                    hbox:
                        xsize KoGa3ModMenu_xsize2
                        textbutton _("+1") text_style "KoGa3_1_button_text" action SetVariable("Gabi_Suspicion", Gabi_Suspicion +1)
                    hbox:
                        xsize KoGa3ModMenu_xsize2
                        #if Gabi_SuspicionTemp >= 1:
                        textbutton _("-1") text_style "KoGa3_1_button_text" action SetVariable("Gabi_Suspicion", Gabi_Suspicion -1)
                    hbox:
                        xsize KoGa3ModMenu_xsize3
                        if Gabi_Suspicion != Gabi_SuspicionTemp:
                            textbutton ("Reset") text_style "KoGa3_1_button_text" action SetVariable("Gabi_Suspicion", Gabi_SuspicionTemp)

                hbox:
                    hbox:
                        xsize KoGa3ModMenu_xsize1
                        textbutton "EP15: Marisol Points:":
                            text_style "KoGa3_1_button_text"
                            sensitive False
                            action NullAction()
                    hbox:
                        xsize KoGa3ModMenu_xsize2
                        textbutton "{color=[KoGa3Color3]}[Marisol_Points]":
                            text_style "KoGa3_1_button_text"
                            sensitive False
                            action NullAction()
                    hbox:
                        xsize KoGa3ModMenu_xsize2
                        textbutton _("+1") text_style "KoGa3_1_button_text" action SetVariable("Marisol_Points", Marisol_Points +1)
                    hbox:
                        xsize KoGa3ModMenu_xsize2
                        #if Marisol_PointsTemp >= 1:
                        textbutton _("-1") text_style "KoGa3_1_button_text" action SetVariable("Marisol_Points", Marisol_Points -1)
                    hbox:
                        xsize KoGa3ModMenu_xsize3
                        if Marisol_Points != Marisol_PointsTemp:
                            textbutton ("Reset") text_style "KoGa3_1_button_text" action SetVariable("Marisol_Points", Marisol_PointsTemp)

            if KoGa3CheatButton == 5:   #more points
                textbutton _("(Info: points below are not used in the game so far)"):
                    text_style "KoGa3_1_button_text"
                    selected True
                    sensitive False
                    action NullAction()

                null height 20

                hbox:
                    hbox:
                        xsize KoGa3ModMenu_xsize1
                        textbutton "Gabi Points:":
                            text_style "KoGa3_1_button_text"
                            sensitive False
                            action NullAction()
                    hbox:
                        xsize KoGa3ModMenu_xsize2
                        textbutton "{color=[KoGa3Color3]}[Gabi_Points]":
                            text_style "KoGa3_1_button_text"
                            sensitive False
                            action NullAction()
                    hbox:
                        xsize KoGa3ModMenu_xsize2
                        textbutton _("+1") text_style "KoGa3_1_button_text" action SetVariable("Gabi_Points", Gabi_Points +1)
                    hbox:
                        xsize KoGa3ModMenu_xsize2
                        #if Gabi_Points >= 1:
                        textbutton _("-1") text_style "KoGa3_1_button_text" action SetVariable("Gabi_Points", Gabi_Points -1)
                    hbox:
                        xsize KoGa3ModMenu_xsize3
                        if Gabi_Points != Gabi_PointsTemp:
                            textbutton ("Reset") text_style "KoGa3_1_button_text" action SetVariable("Gabi_Points", Gabi_PointsTemp)

                hbox:
                    hbox:
                        xsize KoGa3ModMenu_xsize1
                        textbutton "Mira Points:":
                            text_style "KoGa3_1_button_text"
                            sensitive False
                            action NullAction()
                    hbox:
                        xsize KoGa3ModMenu_xsize2
                        textbutton "{color=[KoGa3Color3]}[Mira_Points]":
                            text_style "KoGa3_1_button_text"
                            sensitive False
                            action NullAction()
                    hbox:
                        xsize KoGa3ModMenu_xsize2
                        textbutton _("+1") text_style "KoGa3_1_button_text" action SetVariable("Mira_Points", Mira_Points +1)
                    hbox:
                        xsize KoGa3ModMenu_xsize2
                        #if Mira_Points >= 1:
                        textbutton _("-1") text_style "KoGa3_1_button_text" action SetVariable("Mira_Points", Mira_Points -1)
                    hbox:
                        xsize KoGa3ModMenu_xsize3
                        if Mira_Points != Mira_PointsTemp:
                            textbutton ("Reset") text_style "KoGa3_1_button_text" action SetVariable("Mira_Points", Mira_PointsTemp)

                hbox:
                    hbox:
                        xsize KoGa3ModMenu_xsize1
                        textbutton "Natasha Points:":
                            text_style "KoGa3_1_button_text"
                            sensitive False
                            action NullAction()
                    hbox:
                        xsize KoGa3ModMenu_xsize2
                        textbutton "{color=[KoGa3Color3]}[Natasha_Points]":
                            text_style "KoGa3_1_button_text"
                            sensitive False
                            action NullAction()
                    hbox:
                        xsize KoGa3ModMenu_xsize2
                        textbutton _("+1") text_style "KoGa3_1_button_text" action SetVariable("Natasha_Points", Natasha_Points +1)
                    hbox:
                        xsize KoGa3ModMenu_xsize2
                        #if Natasha_Points >= 1:
                        textbutton _("-1") text_style "KoGa3_1_button_text" action SetVariable("Natasha_Points", Natasha_Points -1)
                    hbox:
                        xsize KoGa3ModMenu_xsize3
                        if Natasha_Points != Natasha_PointsTemp:
                            textbutton ("Reset") text_style "KoGa3_1_button_text" action SetVariable("Natasha_Points", Natasha_PointsTemp)

            textbutton ("────────────────────────────────────────────────"):
                text_style "KoGa3_1_button_text"
                sensitive False
                action NullAction()

            hbox:
                if not renpy.loadable("1Mod.rpyc"):
                    hbox:
                        xsize 215
                        textbutton ("Choice hints:"):
                            text_style "KoGa3_1a_button_text"
                            sensitive False
                            action NullAction()
                    hbox:
                        xsize 260
                        if KoGa3ChoiceOption == 0:
                            textbutton _("OFF"):
                                text_style "KoGa3_1a_button_text"
                                selected False
                                action [
                                SetVariable ("KoGa3ChoiceOption", 1),
                                SetVariable ("KoGa3AutoWTChange1", "\n{color=#ffdf00}"),
                                SetVariable ("KoGa3WTChange", "\n{color=#008000}"),
                                SetVariable ("KoGa3WTChange1", "\n{color=#ffdf00}"),
                                SetVariable ("KoGa3WTChange2", "\n{color=#ff0000}") ]
                        else:
                            textbutton _("ON "):
                                text_style "KoGa3_1a_button_text"
                                selected False
                                action [
                                SetVariable ("KoGa3ChoiceOption", 0),
                                SetVariable ("KoGa3AutoWTChange1", "{alt}"),
                                SetVariable ("KoGa3WTChange", "{alt}"),
                                SetVariable ("KoGa3WTChange1", "{alt}"),
                                SetVariable ("KoGa3WTChange2", "{alt}")]
                hbox:
                    textbutton _("More cheat options..."):
                        text_style "KoGa3_1_button_text" 
                        action Hide("KoGa3ScreenCheat"), Show("KoGa3ScreenCheatMore1")

            if KoGa3ScreenStatsFull == 1 or KoGa3ScreenStatsFull == 2:
                hbox:
                    #xsize 400
                    spacing 15
                    hbox:
                        #xsize 400
                        spacing 5
                        textbutton ("Status infos:"):
                            text_style "KoGa3_1_button_text"
                            sensitive False
                            action NullAction()

                        textbutton ("ON "):
                            text_style "KoGa3_1_button_text"
                            selected False
                            action [
                            SetVariable("KoGa3ScreenStatsFull", 0),
                            Hide("KoGa3ScreenStats") ]

                    textbutton "   color:":
                        text_style "KoGa3_1_button_text"
                        sensitive False
                        action NullAction()
                    textbutton ("{size=30}red{/size}"):
                        text_style "KoGa3_2_button_text"
                        action SetVariable("KoGa3_status_button_text", "KoGa3_2_button_text")
                    textbutton ("{size=30}green{/size}"):
                        text_style "KoGa3_3_button_text"
                        action SetVariable("KoGa3_status_button_text", "KoGa3_3_button_text")
                    textbutton ("{size=30}blue{/size}"):
                        text_style "KoGa3_4_button_text"
                        action SetVariable("KoGa3_status_button_text", "KoGa3_4_button_text")
                    textbutton ("{size=30}gray{/size}"):
                        text_style "KoGa3_5_button_text"
                        action SetVariable("KoGa3_status_button_text", "KoGa3_5_button_text")
            if KoGa3ScreenStatsFull == 0:
                hbox:
                    #xsize 400
                    spacing 5
                    textbutton ("Status infos:"):
                        text_style "KoGa3_1_button_text"
                        sensitive False
                        action NullAction()
                    textbutton ("OFF"):
                        text_style "KoGa3_1_button_text"
                        selected False
                        action [
                        SetVariable("KoGa3ScreenStatsFull", 1),
                        Show("KoGa3ScreenStats") ]

        textbutton ("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"):
            text_style "KoGa3_1_button_text"
            sensitive False
            action NullAction()
        textbutton _("Close"):
            text_style "KoGa3_1_button_text"
            action [
            SetVariable ("KoGa3ModMenuButtonPressed", False),
            Hide("KoGa3ScreenCheat") ]


#---------------------Cheat more menu---------------------#
init:
    $ gamevariable_listP1=[]
    #Ep1
    $ gamevariable_listP1.append(["Alexis_Friends","EP1"])
    $ gamevariable_listP1.append(["Alexis_Intro_Ignore","EP1"])
    $ gamevariable_listP1.append(["Alexis_Intro_Join","EP1"])
    $ gamevariable_listP1.append(["Alexis_Sex","EP1"])
    $ gamevariable_listP1.append(["MC_Week1_Monday_Skip","EP1"])
    $ gamevariable_listP1.append(["Melissa_Intro_Hug","EP1"])
    $ gamevariable_listP1.append(["Melissa_Intro_Sunbath","EP1"])
    $ gamevariable_listP1.append(["Rachel_End","EP1"])
    $ gamevariable_listP1.append(["Rachel_Intro_BJ","EP1"])
    $ gamevariable_listP1.append(["Rachel_Intro_CheckOut","EP1"])
    #Ep2
    $ gamevariable_listP1.append(["Alexis_Week1_Monday_BarWait","EP2"])
    $ gamevariable_listP1.append(["Alexis_Week1_Monday_TellZach","EP2"])
    $ gamevariable_listP1.append(["Elena_Week1_Tuesday_Intervene","EP2"])
    $ gamevariable_listP1.append(["Elena_Week1_Tuesday_Science_Complain","EP2"])
    $ gamevariable_listP1.append(["Erynn_Week2_Tuesday_AlexisFight","EP2"])
    $ gamevariable_listP1.append(["Layla_Week1_Monday_Four","EP2"])
    $ gamevariable_listP1.append(["Layla_Week1_Monday_Legs","EP2"])
    $ gamevariable_listP1.append(["Layla_Week1_Monday_Payattention","EP2"])
    $ gamevariable_listP1.append(["Layla_Week1_Monday_Sand","EP2"])
    #Ep3
    $ gamevariable_listP1.append(["Alexis_Lexi","EP3"])
    $ gamevariable_listP1.append(["Alexis_Week1_Wednesday_PhoneHome","EP3"])
    $ gamevariable_listP1.append(["Alexis_Week1_Wednesday_PhoneIgnore","EP3"])
    $ gamevariable_listP1.append(["Alexis_Week1_Wednesday_PhonePickup","EP3"])
    $ gamevariable_listP1.append(["Dylan_Week1_Assumption","EP3"])
    $ gamevariable_listP1.append(["Elena_Cute","EP3"])
    $ gamevariable_listP1.append(["Elena_Week1_TrainKiss","EP3"])
    $ gamevariable_listP1.append(["Elena_Week1_TrainKissLayla","EP3"])
    $ gamevariable_listP1.append(["Erynn_Week1_Cupsize","EP3"])
    $ gamevariable_listP1.append(["Erynn_Week1_ShowerJoin","EP3"])
    $ gamevariable_listP1.append(["Erynn_Week1_Stay","EP3"])
    $ gamevariable_listP1.append(["Layla_Week1_Piggyback","EP3"])
    $ gamevariable_listP1.append(["Layla_Week1_Wednesday_HallwayTalk","EP3"])
    $ gamevariable_listP1.append(["Layla_Week1_Wednesday_ParkHelp","EP3"])
    $ gamevariable_listP1.append(["Layla_Week1_Wednesday_ParkStay","EP3"])
    $ gamevariable_listP1.append(["Mike_Name","EP3"])
    $ gamevariable_listP1.append(["Sienna_Name","EP3"])
    $ gamevariable_listP1.append(["Tori_Sex","EP3"])
    $ gamevariable_listP1.append(["Tori_Week1_Interested","EP3"])
    #Ep4
    $ gamevariable_listP1.append(["Alexis_Week1_Concert","EP4"])    #new with v0.15.4
    $ gamevariable_listP1.append(["Alexis_Week1_Saturday_JokePicture","EP4"])
    $ gamevariable_listP1.append(["Alexis_Week1_Saturday_Picture","EP4"])
    $ gamevariable_listP1.append(["Alexis_Week1_Saturday_Picture_Night","EP4"])
    $ gamevariable_listP1.append(["Alexis_Week1_Sunday_Chocolate","EP4"])
    $ gamevariable_listP1.append(["Alexis_Week1_Sunday_Concert_Great","EP4"])
    $ gamevariable_listP1.append(["Alexis_Week1_Sunday_Concert_Sing","EP4"])
    $ gamevariable_listP1.append(["Alexis_Week1_Sunday_Flower","EP4"])
    $ gamevariable_listP1.append(["Andres_FB_Punch","EP4"])
    $ gamevariable_listP1.append(["Cara_Cheat","EP4"])
    $ gamevariable_listP1.append(["Cara_FB_BikeCity","EP4"])
    $ gamevariable_listP1.append(["Cara_FB_Choose","EP4"])
    $ gamevariable_listP1.append(["Cara_FB_Club_Dance","EP4"])
    $ gamevariable_listP1.append(["Cara_FB_CopyAssignment","EP4"])
    $ gamevariable_listP1.append(["Cara_FB_Masturbate","EP4"])
    $ gamevariable_listP1.append(["Cara_FB_OfferBikeRide","EP4"])
    $ gamevariable_listP1.append(["Cara_FB_StudyTogether","EP4"])
    $ gamevariable_listP1.append(["Cara_FB_Talk","EP4"])
    $ gamevariable_listP1.append(["Cara_Girlfriend","EP4"])
    $ gamevariable_listP1.append(["Elena_Week1_Saturday_Beach_Reminder","EP4"])
    $ gamevariable_listP1.append(["Elena_Week1_Saturday_Beach_Sunscreen","EP4"])
    $ gamevariable_listP1.append(["Elena_Week1_Saturday_Beach_Tease","EP4"])
    $ gamevariable_listP1.append(["Elena_Week1_Saturday_Beach_Towel","EP4"])
    $ gamevariable_listP1.append(["Emily_Week1_Saturday_BeachInvite","EP4"])
    $ gamevariable_listP1.append(["Emily_Week1_Saturday_Lie","EP4"])
    $ gamevariable_listP1.append(["Erynn_Week1_Saturday_LookBoobs","EP4"])
    $ gamevariable_listP1.append(["Erynn_Week1_Saturday_Picture","EP4"])
    $ gamevariable_listP1.append(["Erynn_Week1_Saturday_Pool","EP4"])
    $ gamevariable_listP1.append(["FB_Riverside_Nathan_Fight","EP4"])
    $ gamevariable_listP1.append(["Julia_FB_Sex","EP4"])
    $ gamevariable_listP1.append(["Lakeyn_End","EP4"])
    $ gamevariable_listP1.append(["Lakeyn_FB_Sex","EP4"])
    $ gamevariable_listP1.append(["Layla_Week1_Saturday_Beach","EP4"])
    $ gamevariable_listP1.append(["Layla_Week1_Saturday_BeachInvite","EP4"])
    $ gamevariable_listP1.append(["Layla_Week1_Saturday_Beach_Boobs","EP4"])
    $ gamevariable_listP1.append(["Layla_Week1_Saturday_Beach_Forget","EP4"])
    $ gamevariable_listP1.append(["Layla_Week1_Saturday_Beach_Kiss","EP4"])
    $ gamevariable_listP1.append(["Layla_Week1_Saturday_Beach_Massage","EP4"])
    $ gamevariable_listP1.append(["Layla_Week1_Saturday_Beach_Ocean","EP4"])
    $ gamevariable_listP1.append(["Layla_Week1_Saturday_Beach_Slap","EP4"])
    $ gamevariable_listP1.append(["Layla_Week1_Saturday_Beach_UnderwaterKiss","EP4"])
    $ gamevariable_listP1.append(["Layla_Week1_Saturday_Ignore","EP4"])
    $ gamevariable_listP1.append(["Layla_Week1_Saturday_Pareo","EP4"])
    $ gamevariable_listP1.append(["Layla_Week1_Saturday_Picture","EP4"])
    $ gamevariable_listP1.append(["Layla_Week1_Saturday_PictureElena","EP4"])
    $ gamevariable_listP1.append(["Melissa_Week1_Saturday_Payback","EP4"])
    $ gamevariable_listP1.append(["Nikki_Cheat","EP4"])
    $ gamevariable_listP1.append(["Nikki_FB_Butt","EP4"])
    $ gamevariable_listP1.append(["Nikki_FB_Carry","EP4"])
    $ gamevariable_listP1.append(["Nikki_FB_Choose","EP4"])
    $ gamevariable_listP1.append(["Nikki_FB_Club_Carry","EP4"])
    $ gamevariable_listP1.append(["Nikki_FB_Dance","EP4"])
    $ gamevariable_listP1.append(["Nikki_FB_Help","EP4"])
    $ gamevariable_listP1.append(["Nikki_FB_Pancakes","EP4"])
    $ gamevariable_listP1.append(["Nikki_FB_ParkFlirt","EP4"])
    $ gamevariable_listP1.append(["Nikki_FB_PureEvil","EP4"])
    $ gamevariable_listP1.append(["Nikki_FB_Room_Stay","EP4"])
    $ gamevariable_listP1.append(["Nikki_FB_Run","EP4"])
    $ gamevariable_listP1.append(["Nikki_FB_Run_Peak","EP4"])
    $ gamevariable_listP1.append(["Nikki_FB_ShowerheadStory","EP4"])
    $ gamevariable_listP1.append(["Nikki_FB_TouchBoobs","EP4"])
    $ gamevariable_listP1.append(["Nikki_Girlfriend","EP4"])
    $ gamevariable_listP1.append(["Nikki_SP","EP4"])
    $ gamevariable_listP1.append(["Rachel_Week1_Saturday_KickOut","EP4"])
    $ gamevariable_listP1.append(["Rachel_Week1_Saturday_Picture","EP4"])
    $ gamevariable_listP1.append(["Rachel_Week1_Saturday_Sex","EP4"])
    $ gamevariable_listP1.append(["Riverside_FB_NikkiCaraChoice","EP4"])
    $ gamevariable_listP1.append(["Riverside_Friends","EP4"])
    #Ep5
    $ gamevariable_listP1.append(["Adriana_Week2_Monday_TestBack","EP5"])
    $ gamevariable_listP1.append(["Adriana_Week2_Monday_Truth","EP5"])
    $ gamevariable_listP1.append(["Cara_Week2_Tuesday_Phonecall","EP5"])
    $ gamevariable_listP1.append(["Elena_Week2_Tuesday_CheerHot","EP5"])
    $ gamevariable_listP1.append(["Elena_Week2_Tuesday_RecruitJoke","EP5"])
    $ gamevariable_listP1.append(["Erynn_Week2_Monday_Bed","EP5"])
    $ gamevariable_listP1.append(["Erynn_Week2_Monday_GoToErynn","EP5"])
    $ gamevariable_listP1.append(["Erynn_Week2_Tuesday_AlexisFight","EP5"])
    $ gamevariable_listP1.append(["Erynn_Week2_Tuesday_CorrectHer","EP5"])
    $ gamevariable_listP1.append(["Erynn_Week2_Tuesday_Gift","EP5"])
    $ gamevariable_listP1.append(["Erynn_Week2_Tuesday_Pickup","EP5"])
    $ gamevariable_listP1.append(["Erynn_Week2_Tuesday_Shirt","EP5"])
    $ gamevariable_listP1.append(["Gabi_End","EP5"])
    $ gamevariable_listP1.append(["Gabi_Week2_Tuesday_Pullout","EP5"])
    $ gamevariable_listP1.append(["Layla_Week2_Detention","EP5"])
    $ gamevariable_listP1.append(["Layla_Week2_Monday_LucasHelp","EP5"])
    $ gamevariable_listP1.append(["Layla_Week2_Monday_Wait","EP5"])
    $ gamevariable_listP1.append(["Layla_Week2_Tuesday_Lie","EP5"])
    $ gamevariable_listP1.append(["Layla_Week2_Tuesday_Sergeant","EP5"])
    $ gamevariable_listP1.append(["Melissa_Week2_Monday_Milf","EP5"])
    $ gamevariable_listP1.append(["Mike_Week2_Monday_Surname","EP5"])
    $ gamevariable_listP1.append(["Natasha_Week2_Tuesday_MikeSex","EP5"])
    $ gamevariable_listP1.append(["Nikki_Week2_Tuesday_Phonecall","EP5"])
    $ gamevariable_listP1.append(["Week2_Monday_Bar_Stay","EP5"])
    $ gamevariable_listP1.append(["Week2_Monday_Erynn_Ethan","EP5"])
    $ gamevariable_listP1.append(["Week2_Monday_Erynn_Hair","EP5"])
    $ gamevariable_listP1.append(["Week2_Monday_Erynn_Help","EP5"])
    $ gamevariable_listP1.append(["Zach_Week2_Monday_House","EP5"])
    $ gamevariable_listP1.append(["Zach_Week2_Monday_Sister","EP5"])
    #Ep6
    $ gamevariable_listP1.append(["Alexis_Week2_Wednesday_Breakup","EP6"])
    $ gamevariable_listP1.append(["Alexis_Week2_Wednesday_Tell","EP6"])
    $ gamevariable_listP1.append(["Cara_Week2_Weekend_SexInside","EP6"])
    $ gamevariable_listP1.append(["Erynn_Friends","EP6"])
    $ gamevariable_listP1.append(["Erynn_Week2_Thursday_Confront","EP6"])
    $ gamevariable_listP1.append(["Erynn_Week2_Tuesday_Fly","EP6"])
    $ gamevariable_listP1.append(["Layla_Friends","EP6"])
    $ gamevariable_listP1.append(["Layla_Week2_Wednesday_CheckOut","EP6"])
    $ gamevariable_listP1.append(["Layla_Week2_Wednesday_Chichis","EP6"])
    $ gamevariable_listP1.append(["Layla_Week2_Wednesday_HelpUp","EP6"])
    $ gamevariable_listP1.append(["Layla_Week2_Wednesday_Knows","EP6"])
    $ gamevariable_listP1.append(["Layla_Week2_Wednesday_Rude","EP6"])
    $ gamevariable_listP1.append(["Layla_Week2_Wednesday_SpanishHelp","EP6"])
    $ gamevariable_listP1.append(["Melissa_Week2_Tuesday_Dream","EP6"])
    $ gamevariable_listP1.append(["Melissa_Week2_Wednesday_Stories","EP6"])
    $ gamevariable_listP1.append(["Naomi_Week2_Wednesday_Math_Answer","EP6"])
    $ gamevariable_listP1.append(["Nikki_Week2_Weekend_Handle","EP6"])
    $ gamevariable_listP1.append(["Nikki_Week2_Weekend_Movie","EP6"])
    $ gamevariable_listP1.append(["Nikki_Week2_Weekend_SexInside","EP6"])
    $ gamevariable_listP1.append(["Riverside_End","EP6"])
    #Ep7
    $ gamevariable_listP1.append(["Adriana_Week2_Sunday_Dinner","EP7"])
    $ gamevariable_listP1.append(["Alexis_End","EP7"])
    $ gamevariable_listP1.append(["Alexis_Week2_Sunday_Honest","EP7"])
    $ gamevariable_listP1.append(["Alexis_Week2_Sunday_PhoneSex","EP7"])
    $ gamevariable_listP1.append(["Alexis_Week3_Tuesday_Date","EP7"])
    $ gamevariable_listP1.append(["Alexis_Week3_Tuesday_LexySexySong","EP7"])
    $ gamevariable_listP1.append(["Brooke_Week2_Saturday_TurnDown","EP7"])
    $ gamevariable_listP1.append(["Elena_Friends","EP7"])
    $ gamevariable_listP1.append(["Elena_Week3_Monday_Backflip","EP7"])
    $ gamevariable_listP1.append(["Elena_Week3_Monday_CheerTraining","EP7"])
    $ gamevariable_listP1.append(["Elena_Week3_Monday_Help","EP7"])
    $ gamevariable_listP1.append(["Emily_Week2_Saturday_Checkup","EP7"])
    $ gamevariable_listP1.append(["Erynn_End","EP7"])
    $ gamevariable_listP1.append(["Erynn_Week3_Monday_Alexis_Mention","EP7"])
    $ gamevariable_listP1.append(["Erynn_Week3_Monday_Blackmailhelp","EP7"])
    $ gamevariable_listP1.append(["Erynn_Week3_Monday_Help","EP7"])
    $ gamevariable_listP1.append(["Erynn_Week3_Monday_Makeout","EP7"])
    $ gamevariable_listP1.append(["Erynn_Week3_Tuesday_Sandwich","EP7"])
    $ gamevariable_listP1.append(["Layla_Week2_Sunday_TV_Makeout","EP7"])
    $ gamevariable_listP1.append(["Layla_Week3_Monday_Spanish_Fail","EP7"])
    $ gamevariable_listP1.append(["Layla_Week3_Tuesday_Race","EP7"])
    $ gamevariable_listP1.append(["Layla_Week3_Tuesday_Race_Win","EP7"])
    $ gamevariable_listP1.append(["Layla_Week3_Tuesday_Train","EP7"])
    $ gamevariable_listP1.append(["Team_Triss","EP7"])
    $ gamevariable_listP1.append(["Team_Yennefer","EP7"])
    $ gamevariable_listP1.append(["Valeria_Friends","EP7"])
    $ gamevariable_listP1.append(["Valeria_Week3_Monday_Meet","EP7"])
    $ gamevariable_listP1.append(["Valeria_Week3_Monday_NotMyType","EP7"])
    $ gamevariable_listP1.append(["Week3_Monday_Spanish_Blackmail","EP7"])
    $ gamevariable_listP1.append(["Week3_Monday_Spanish_Steal","EP7"])
    #Ep8
    $ gamevariable_listP1.append(["Adriana_Week3_Saturday_TC_Pick","EP8"])
    $ gamevariable_listP1.append(["Alexis_Dating","EP8"])
    $ gamevariable_listP1.append(["Alexis_Girlfriend","EP8"])
    $ gamevariable_listP1.append(["Alexis_SecretPath","EP8"])
    $ gamevariable_listP1.append(["Alexis_Week3_Sunday_BubbleIce","EP8"])
    $ gamevariable_listP1.append(["Alexis_Week3_Sunday_Dorm_StripteaseCute","EP8"])
    $ gamevariable_listP1.append(["Alexis_Week3_Sunday_Meet","EP8"])
    $ gamevariable_listP1.append(["Alexis_Week3_Sunday_NewBartender","EP8"])
    $ gamevariable_listP1.append(["Alexis_Week3_Sunday_PizzaJoke","EP8"])
    $ gamevariable_listP1.append(["Alexis_Week3_Wednesday_TC_Breakup","EP8"])
    $ gamevariable_listP1.append(["Alexis_Week3_Wednesday_TC_FriendsButKissedLayla","EP8"])
    $ gamevariable_listP1.append(["Alexis_Week4_Monday_Meet","EP8"])
    $ gamevariable_listP1.append(["Elena_Week3_Saturday_TC_Threewaykiss","EP8"])
    $ gamevariable_listP1.append(["Emily_Week3_Sunday_DareTell","EP8"])
    $ gamevariable_listP1.append(["Emily_Week3_Sunday_Surprise","EP8"])
    $ gamevariable_listP1.append(["Erynn_LikeMC","EP8"])
    $ gamevariable_listP1.append(["Erynn_Week3_Wednesday_Lying","EP8"])
    $ gamevariable_listP1.append(["Gabi_Week3_Friday_TC_Picture","EP8"])
    $ gamevariable_listP1.append(["Gabi_Week3_Saturday_TC_CumInside","EP8"])
    $ gamevariable_listP1.append(["Gabi_Week3_Saturday_TC_Sex","EP8"])
    $ gamevariable_listP1.append(["Iris_Week3_Sunday_Meet","EP8"])
    $ gamevariable_listP1.append(["Iris_Week3_Sunday_Meet","EP8"])
    $ gamevariable_listP1.append(["Layla_Dating","EP8"])
    $ gamevariable_listP1.append(["Layla_LikeMC","EP8"])
    $ gamevariable_listP1.append(["Layla_Week3_Friday_TC_Wager","EP8"])
    $ gamevariable_listP1.append(["Layla_Week3_Saturday_TC_Swap","EP8"])
    $ gamevariable_listP1.append(["Layla_Week3_Wednesday_TC_AlexisTalk","EP8"])
    $ gamevariable_listP1.append(["Layla_Week3_Wednesday_TC_Alexis_DateBoth","EP8"])
    $ gamevariable_listP1.append(["Layla_Week3_Wednesday_TC_Kiss","EP8"])
    $ gamevariable_listP1.append(["Layla_Week3_Wednesday_TC_TrainingPartner","EP8"])
    $ gamevariable_listP1.append(["Layla_Week4_Monday_FailTest","EP8"])
    $ gamevariable_listP1.append(["Layla_Week4_Monday_Hottub","EP8"])
    $ gamevariable_listP1.append(["Layla_Week4_Monday_Hottub_BJ","EP8"])
    $ gamevariable_listP1.append(["MC_Week3_Saturday_TC_Cheer_Late","EP8"])
    $ gamevariable_listP1.append(["MC_Week3_Saturday_TC_Win","EP8"])
    $ gamevariable_listP1.append(["ShaCarri_End","EP8"])
    $ gamevariable_listP1.append(["TC_Pool_Elena","EP8"])
    $ gamevariable_listP1.append(["TC_Pool_Layla","EP8"])
    $ gamevariable_listP1.append(["TC_Pool_Sienna","EP8"])
    $ gamevariable_listP1.append(["TC_Pool_Valeria","EP8"])
    $ gamevariable_listP1.append(["Tori_End","EP8"])
    $ gamevariable_listP1.append(["Tori_LickAss","EP8"])
    $ gamevariable_listP1.append(["Tori_Week3_Friday_TC_Step","EP8"])
    $ gamevariable_listP1.append(["Tori_Week3_Saturday_TC_LickAss","EP8"])
    $ gamevariable_listP1.append(["Tori_Week3_Saturday_TC_Sex","EP8"])
    $ gamevariable_listP1.append(["Tori_Week3_Wednesday_TC_Fun","EP8"])
    $ gamevariable_listP1.append(["Valeria_Week3_Saturday_TC_Peek","EP8"])
    $ gamevariable_listP1.append(["Valeria_Week3_Saturday_TC_Swap","EP8"])
    $ gamevariable_listP1.append(["Valeria_Week3_Saturday_Tea","EP8"])
    $ gamevariable_listP1.append(["Valeria_Week3_Thursday_TC_Massage","EP8"])
    $ gamevariable_listP1.append(["Valeria_Week3_Wednesday_Pictures","EP8"])
    $ gamevariable_listP1.append(["Week3_Friday_TC_Kickball","EP8"])
    $ gamevariable_listP1.append(["Zach_Week3_Saturday_TC_Swap","EP8"])
    $ gamevariable_listP1.append(["Zach_Week3_Thursday_TC_Box","EP8"])
    $ gamevariable_listP1.append(["Zach_Week3_Wednesday_Seats","EP8"])
    $ gamevariable_listP1.append(["Zach_Week3_Wednesday_TC_Girlshower","EP8"])
    #Ep9
    $ gamevariable_listP1.append(["Alexis_RiversideStory","EP9"])
    $ gamevariable_listP1.append(["Cara_MeetEmily","EP9"])
    $ gamevariable_listP1.append(["Cara_Solo","EP9"])
    $ gamevariable_listP1.append(["Cara_Visit","EP9"])
    $ gamevariable_listP1.append(["Cara_Week4_Thursday_Dress_Like","EP9"])
    $ gamevariable_listP1.append(["Cara_Week4_Thursday_Dress_Sex","EP9"])
    $ gamevariable_listP1.append(["Cara_Week4_Wednesday_Visit_Breakup","EP9"])
    $ gamevariable_listP1.append(["Cara_Week4_Wednesday_Visit_Knows","EP9"])
    $ gamevariable_listP1.append(["Elena_End","EP9"])
    $ gamevariable_listP1.append(["Iris_FB_Outfit_DontLike","EP9"])
    $ gamevariable_listP1.append(["Layla_End","EP9"])
    $ gamevariable_listP1.append(["Layla_Week4_Thursday_WingmanVal","EP9"])
    $ gamevariable_listP1.append(["Layla_Week4_Thursday_HoldPenis","EP9"])
    $ gamevariable_listP1.append(["Layla_Week4_Thursday_Val_NakedRun","EP9"])
    $ gamevariable_listP1.append(["Layla_Week4_Thursday_Val_NakedRun","EP9"])
    $ gamevariable_listP1.append(["MC_Girlfriend_Riverside","EP9"])
    $ gamevariable_listP1.append(["MC_Week4_Thursday_SleepInEmilyBed","EP9"])
    $ gamevariable_listP1.append(["MC_Week4_Wednesday_BedOccupied","EP9"])
    $ gamevariable_listP1.append(["Mike_Week4_Thursday_NikkiCaraDad","EP9"])
    $ gamevariable_listP1.append(["Naomi_Week4_Thursday_Watch","EP9"])
    $ gamevariable_listP1.append(["Nikki_MeetEmily","EP9"])
    $ gamevariable_listP1.append(["Nikki_Solo","EP9"])
    $ gamevariable_listP1.append(["Nikki_Visit","EP9"])
    $ gamevariable_listP1.append(["Nikki_Week4_Thursday_ArmwrestlingWin","EP9"])
    $ gamevariable_listP1.append(["Nikki_Week4_Thursday_Handstand_Help","EP9"])
    $ gamevariable_listP1.append(["Nikki_Week4_Thursday_Lotion","EP9"])
    $ gamevariable_listP1.append(["Nikki_Week4_Thursday_LotionMC","EP9"])
    $ gamevariable_listP1.append(["Nikki_Week4_Thursday_Swimsuit_Option1_Like","EP9"])
    $ gamevariable_listP1.append(["Nikki_Week4_Wednesday_Visit_Breakup","EP9"])
    $ gamevariable_listP1.append(["Nikki_Week4_Wednesday_Visit_Knows","EP9"])
    $ gamevariable_listP1.append(["Tori_Week3_Thursday_School_HJ","EP9"])
    $ gamevariable_listP1.append(["Tori_Week4_Thursday_SeeCara","EP9"])
    $ gamevariable_listP1.append(["Tori_Week4_Thursday_SeeNikki","EP9"])
    $ gamevariable_listP1.append(["Valeria_Week4_Friday_Help","EP9"])
    $ gamevariable_listP1.append(["Valeria_Week4_Thursday_MeetNikki","EP9"])
    #Ep10
    $ gamevariable_listP1.append(["Adriana_Week5_Monday_SlapAss","EP10"])
    $ gamevariable_listP1.append(["Alexis_Week4_Friday_Blackmail_Involve","EP10"])
    $ gamevariable_listP1.append(["Alexis_Week4_Saturday_Cara_Phone","EP10"])
    $ gamevariable_listP1.append(["Alexis_Week5_Monday_Date_Cancel","EP10"])
    $ gamevariable_listP1.append(["Alexis_Week5_Monday_Makeup","EP10"])
    $ gamevariable_listP1.append(["Cara_Week4_Friday_LickAss","EP10"])
    $ gamevariable_listP1.append(["Cara_Week4_Friday_Play","EP10"])
    $ gamevariable_listP1.append(["Cara_Week4_Friday_SleepBed","EP10"])
    $ gamevariable_listP1.append(["Cara_Week4_Saturday_Anal_Suggestion","EP10"])
    $ gamevariable_listP1.append(["Cara_Week4_Saturday_Bed","EP10"])
    $ gamevariable_listP1.append(["Cara_Week4_Saturday_Game_Change","EP10"])
    $ gamevariable_listP1.append(["Cara_Week4_Saturday_LickAss","EP10"])
    $ gamevariable_listP1.append(["Cara_Week4_Saturday_Sexgame","EP10"])
    $ gamevariable_listP1.append(["Cara_Week4_Wednesday_AlexisLaylaBreakUp","EP10"])
    $ gamevariable_listP1.append(["Darryl_SeeNikkiMC","EP10"])
    $ gamevariable_listP1.append(["Elena_Week5_Monday_Beach","EP10"])
    $ gamevariable_listP1.append(["Elena_Week5_Monday_Beach_Hero","EP10"])
    $ gamevariable_listP1.append(["Emily_Week4_Sunday_DateJohn","EP10"])
    $ gamevariable_listP1.append(["Emily_Week4_Sunday_Sexy","EP10"])
    $ gamevariable_listP1.append(["Erynn_Week4_Friday_Slap","EP10"])
    $ gamevariable_listP1.append(["Erynn_Week4_Saturday_CaraLie","EP10"])
    $ gamevariable_listP1.append(["Erynn_Week4_Saturday_Jump","EP10"])
    $ gamevariable_listP1.append(["Erynn_Week4_Saturday_Jump_Cara","EP10"])
    $ gamevariable_listP1.append(["Erynn_Week4_Saturday_Jump_Nikki","EP10"])
    $ gamevariable_listP1.append(["Erynn_Week4_Saturday_NikkiLie","EP10"])
    $ gamevariable_listP1.append(["Erynn_Week4_Sunday_OfferBikeRide","EP10"])
    $ gamevariable_listP1.append(["MC_Bike","EP10"])
    $ gamevariable_listP1.append(["MC_NoFriends","EP10"])
    $ gamevariable_listP1.append(["Melissa_End","EP10"])
    $ gamevariable_listP1.append(["Melissa_Week4_Saturday_Dream","EP10"])
    $ gamevariable_listP1.append(["Melissa_Week4_Saturday_Kiss","EP10"])
    $ gamevariable_listP1.append(["Nikki_Week4_Friday_Oral","EP10"])
    $ gamevariable_listP1.append(["Nikki_Week4_Friday_SleepBed","EP10"])
    $ gamevariable_listP1.append(["Nikki_Week4_Saturday_Bed","EP10"])
    $ gamevariable_listP1.append(["Nikki_Week4_Saturday_Icecubes","EP10"])
    $ gamevariable_listP1.append(["Nikki_Week4_Saturday_Sex_Inside","EP10"])
    $ gamevariable_listP1.append(["Nikki_Week4_Wednesday_AlexisLaylaBreakUp","EP10"])
    $ gamevariable_listP1.append(["Valeria_LikeMC","EP10"])
    $ gamevariable_listP1.append(["Valeria_Week5_Monday_Kiss","EP10"])
    $ gamevariable_listP1.append(["Valeria_Week5_Monday_Photobooth","EP10"])
    $ gamevariable_listP1.append(["Valeria_Week5_Monday_Picture","EP10"])
    $ gamevariable_listP1.append(["Week5_Monday_Prettiest_Layla","EP10"])
    $ gamevariable_listP1.append(["Week5_Monday_Prettiest_Tori","EP10"])
    $ gamevariable_listP1.append(["Week5_Monday_Prettiest_Valeria","EP10"])
    #Ep11
    $ gamevariable_listP1.append(["Adriana_Week5_Wednesday_Kiss","EP11"])
    $ gamevariable_listP1.append(["Alexis_Week5_Photoshoot_DogPicture","EP11"])
    $ gamevariable_listP1.append(["Alexis_Week5_Wednesday_Beach","EP11"])
    $ gamevariable_listP1.append(["Alexis_Week5_Wednesday_Beach_CumFace","EP11"])
    $ gamevariable_listP1.append(["Alexis_Week5_Wednesday_Beach_CumMouth","EP11"])
    $ gamevariable_listP1.append(["Alexis_Week5_Wednesday_Beach_CumTits","EP11"])
    $ gamevariable_listP1.append(["Alexis_Week5_Wednesday_Beach_Join","EP11"])
    $ gamevariable_listP1.append(["Alexis_Week5_Wednesday_Beach_SP","EP11"])
    $ gamevariable_listP1.append(["Alexis_Week5_Wednesday_Beach_Sex","EP11"])
    $ gamevariable_listP1.append(["Alexis_Week5_Wednesday_Club_KissIris","EP11"])
    $ gamevariable_listP1.append(["Alexis_Week5_Wednesday_Run","EP11"])
    $ gamevariable_listP1.append(["Elena_LikeMC","EP11"])
    $ gamevariable_listP1.append(["Elena_Week5_Tuesday_Hottub_69","EP11"])
    $ gamevariable_listP1.append(["Elena_Week5_Tuesday_Hottub_Grab","EP11"])
    $ gamevariable_listP1.append(["Elena_Week5_Tuesday_Hottub_Threeway","EP11"])
    $ gamevariable_listP1.append(["Emily_Week5_Wednesday_BeachInvite_Adriana","EP11"])
    $ gamevariable_listP1.append(["Erynn_Week5_Tuesday_Photoshoot","EP11"])
    $ gamevariable_listP1.append(["Erynn_Week5_Tuesday_Photoshoot_Checkout","EP11"])
    $ gamevariable_listP1.append(["Erynn_Week5_Tuesday_Photoshoot_HiddenFeelings","EP11"])
    $ gamevariable_listP1.append(["Erynn_Week5_Tuesday_Photoshoot_Join","EP11"])
    $ gamevariable_listP1.append(["Erynn_Week5_Tuesday_Room_Kiss","EP11"])
    $ gamevariable_listP1.append(["Erynn_Week5_Tuesday_SlapAss","EP11"])
    $ gamevariable_listP1.append(["Erynn_Week5_Tuesday_Wakeup","EP11"])
    $ gamevariable_listP1.append(["Erynn_Week5_Wednesday_Beach_Join","EP11"])
    $ gamevariable_listP1.append(["Iris_Week5_Wednesday_Beach_Join","EP11"])
    $ gamevariable_listP1.append(["Iris_Week5_Wednesday_Beach_Sex","EP11"])
    $ gamevariable_listP1.append(["KFM_Fuck_Alexis","EP11"])
    $ gamevariable_listP1.append(["KFM_Fuck_Erynn","EP11"])
    $ gamevariable_listP1.append(["KFM_Fuck_Iris","EP11"])
    $ gamevariable_listP1.append(["KFM_Kill_Alexis","EP11"])
    $ gamevariable_listP1.append(["KFM_Kill_Erynn","EP11"])
    $ gamevariable_listP1.append(["KFM_Kill_Iris","EP11"])
    $ gamevariable_listP1.append(["KFM_Marry_Alexis","EP11"])
    $ gamevariable_listP1.append(["KFM_Marry_Erynn","EP11"])
    $ gamevariable_listP1.append(["KFM_Marry_Iris","EP11"])
    $ gamevariable_listP1.append(["Layla_Girlfriend","EP11"])
    $ gamevariable_listP1.append(["Layla_Week5_Tuesday_Hottub_69","EP11"])
    $ gamevariable_listP1.append(["Layla_Week5_Tuesday_Hottub_Chickenbreast","EP11"])
    $ gamevariable_listP1.append(["Layla_Week5_Tuesday_Hottub_Grab","EP11"])
    $ gamevariable_listP1.append(["Layla_Week5_Tuesday_Hottub_Towel","EP11"])
    $ gamevariable_listP1.append(["Layla_Week5_Wednesday_BreakUp","EP11"])
    $ gamevariable_listP1.append(["Layla_Week5_Wednesday_ClubDate","EP11"])
    $ gamevariable_listP1.append(["Layla_Week5_Wednesday_FirstTime","EP11"])
    $ gamevariable_listP1.append(["Layla_Week5_Wednesday_LikeElenaKnow","EP11"])
    $ gamevariable_listP1.append(["Sienna_Week5_Tuesday_Hottest","EP11"])
    $ gamevariable_listP1.append(["Sienna_Week5_Tuesday_Hottub_Sex","EP11"])
    $ gamevariable_listP1.append(["Tori_Week5_Wednesday_Beach_LickAss","EP11"])
    $ gamevariable_listP1.append(["Tori_Week5_Wednesday_Beach_Sex","EP11"])
    #Ep12
    $ gamevariable_listP1.append(["Alexis_Week5_Thursday_BreakUpTalk","EP12"])
    $ gamevariable_listP1.append(["Alexis_Week5_Thursday_KissWon","EP12"])
    $ gamevariable_listP1.append(["Brooke_Week5_Thursday_BikeRide","EP12"])
    $ gamevariable_listP1.append(["Brooke_Week5_Thursday_CollegeEmily","EP12"])
    $ gamevariable_listP1.append(["Brooke_Week5_Thursday_MommyBrooke","EP12"])
    $ gamevariable_listP1.append(["Brooke_Week5_Thursday_Peek","EP12"])
    $ gamevariable_listP1.append(["Brooke_Week5_Thursday_Picture","EP12"])
    $ gamevariable_listP1.append(["Emily_Week5_Thursday_WitnessKissErynn","EP12"])
    $ gamevariable_listP1.append(["Erynn_Week5_Thursday_FridayBeach","EP12"])
    $ gamevariable_listP1.append(["Erynn_Week5_Thursday_Handjob","EP12"])
    $ gamevariable_listP1.append(["Erynn_Week5_Thursday_Photo","EP12"])
    $ gamevariable_listP1.append(["Erynn_Week5_Thursday_Shower","EP12"])
    $ gamevariable_listP1.append(["Erynn_Week5_Thursday_SniffPanties","EP12"])
    $ gamevariable_listP1.append(["Erynn_Week5_Thursday_WashBack","EP12"])
    $ gamevariable_listP1.append(["Ethan_Week5_Thursday_Phone","EP12"])
    $ gamevariable_listP1.append(["Ethan_Week5_Thursday_Plan","EP12"])
    $ gamevariable_listP1.append(["Ethan_Week5_Thursday_Punch","EP12"])
    $ gamevariable_listP1.append(["Gabi_Week5_Thursday_Picture","EP12"])
    $ gamevariable_listP1.append(["Gianna_Week5_Thursday_CheckOut","EP12"])
    $ gamevariable_listP1.append(["Gianna_Week5_Thursday_Domino","EP12"])
    $ gamevariable_listP1.append(["Iris_Week5_Thursday_BikeRepair","EP12"])
    $ gamevariable_listP1.append(["John_Week5_Thursday_BikeRide","EP12"])
    $ gamevariable_listP1.append(["Valeria_Week5_Thursday_2ndChance","EP12"])
    $ gamevariable_listP1.append(["Valeria_Week5_Thursday_Headscratches","EP12"])
    $ gamevariable_listP1.append(["Ximena_Week5_Thursday_Watch","EP12"])
    #Ep13
    $ gamevariable_listP1.append(["Alexis_Week5_Sunday_Roleplay","EP13"])
    $ gamevariable_listP1.append(["Alexis_Week5_Thursday_BarKiss","EP13"])
    $ gamevariable_listP1.append(["Alexis_Week5_Thursday_BreakUp","EP13"])
    $ gamevariable_listP1.append(["Alexis_Week5_Thursday_BreakUp_Alexis","EP13"])
    $ gamevariable_listP1.append(["Alexis_Week5_Thursday_Enzo","EP13"])
    $ gamevariable_listP1.append(["Alexis_Week5_Thursday_Fantasy_BDSM","EP13"])
    $ gamevariable_listP1.append(["Alexis_Week5_Thursday_Fantasy_Roleplay","EP13"])
    $ gamevariable_listP1.append(["Alexis_Week5_Thursday_Fantasy_Threesome","EP13"])
    $ gamevariable_listP1.append(["Alexis_Week5_Thursday_Fantasy_Threesome_Erynn","EP13"])
    $ gamevariable_listP1.append(["Alexis_Week5_Thursday_Fantasy_Threesome_Ximena","EP13"])
    $ gamevariable_listP1.append(["Alexis_Week5_Thursday_Fantasy_Voyeurism","EP13"])
    $ gamevariable_listP1.append(["Cara_Week5_Saturday_Anal","EP13"])
    $ gamevariable_listP1.append(["Cara_Week5_Saturday_LickAss","EP13"])
    $ gamevariable_listP1.append(["Emily_Week5_Sunday_Hug","EP13"])
    $ gamevariable_listP1.append(["Erynn_Week5_Friday_Beach_Ass","EP13"])
    $ gamevariable_listP1.append(["Erynn_Week5_Friday_Beach_Body","EP13"])
    $ gamevariable_listP1.append(["Erynn_Week5_Friday_Beach_Boobs","EP13"])
    $ gamevariable_listP1.append(["Erynn_Week5_Friday_Beach_Bush","EP13"])
    $ gamevariable_listP1.append(["Erynn_Week5_Friday_Beach_DM","EP13"])
    $ gamevariable_listP1.append(["Erynn_Week5_Friday_Beach_Face","EP13"])
    $ gamevariable_listP1.append(["Erynn_Week5_Friday_Beach_LandingStrip","EP13"])
    $ gamevariable_listP1.append(["Erynn_Week5_Friday_Beach_Legs","EP13"])
    $ gamevariable_listP1.append(["Erynn_Week5_Friday_Beach_OceanPee","EP13"])
    $ gamevariable_listP1.append(["Erynn_Week5_Friday_Beach_Shallow","EP13"])
    $ gamevariable_listP1.append(["Erynn_Week5_Friday_Beach_Shaved","EP13"])
    $ gamevariable_listP1.append(["Erynn_Week5_Friday_Beach_WellKept","EP13"])
    $ gamevariable_listP1.append(["Erynn_Week5_Friday_Date","EP13"])
    $ gamevariable_listP1.append(["Erynn_Week5_Friday_Date_Cancel","EP13"])
    $ gamevariable_listP1.append(["Erynn_Week5_Friday_DressingRoomHelp","EP13"])
    $ gamevariable_listP1.append(["Erynn_Week5_Sunday_Bath","EP13"])
    $ gamevariable_listP1.append(["Haley_Week5_Saturday_Masturbate","EP13"])
    $ gamevariable_listP1.append(["Haley_Week5_Saturday_SexWatch","EP13"])
    $ gamevariable_listP1.append(["Lakeyn_Week5_Friday_PlayAlong","EP13"])
    $ gamevariable_listP1.append(["Layla_Week5_Sunday_LakeynKnow","EP13"])
    $ gamevariable_listP1.append(["Layla_Week5_Sunday_SantiagoDadKnow","EP13"])
    $ gamevariable_listP1.append(["MC_MeetDonovan","EP13"])
    $ gamevariable_listP1.append(["MC_Week5_Friday_RiversideVisit","EP13"])
    $ gamevariable_listP1.append(["Mira_End","EP13"])
    $ gamevariable_listP1.append(["Mira_Week5_Saturday_Like","EP13"])
    $ gamevariable_listP1.append(["Nikki_Week5_Friday_CumInside","EP13"])
    $ gamevariable_listP1.append(["Nikki_Week5_Friday_CumOnBack","EP13"])
    $ gamevariable_listP1.append(["Nikki_Week5_Friday_CumOnTits","EP13"])
    $ gamevariable_listP1.append(["Nikki_Week5_Saturday_FartLaugh","EP13"])
    $ gamevariable_listP1.append(["Valeria_Week5_Friday_Date","EP13"])
    $ gamevariable_listP1.append(["Valeria_Week5_Friday_Date_Leave","EP13"])
    $ gamevariable_listP1.append(["Valeria_Week5_Friday_NudePicture","EP13"])
    $ gamevariable_listP1.append(["Valeria_Week5_Friday_Stay","EP13"])
    $ gamevariable_listP1.append(["Valeria_Week5_Thursday_CancelDate","EP13"])
    #Ep14
    $ gamevariable_listP1.append(["Adriana_Week6_Monday_DontTell","EP14"])
    $ gamevariable_listP1.append(["AlexisValeria","EP14"])
    $ gamevariable_listP1.append(["Andres_Week6_Monday_Hug","EP14"])
    $ gamevariable_listP1.append(["Brooke_Week6_Monday_ManagerPosition","EP14"])
    $ gamevariable_listP1.append(["ElenaLayla_Week6_Monday_BikeRevScare","EP14"])
    $ gamevariable_listP1.append(["Emily_Week6_Monday_FirstBikeRide","EP14"])
    $ gamevariable_listP1.append(["Erynn_Week6_Monday_ReadLetter","EP14"])
    $ gamevariable_listP1.append(["Erynn_Week6_Monday_WriteLetter","EP14"])
    $ gamevariable_listP1.append(["Iris_LikeMC","EP14"])
    $ gamevariable_listP1.append(["Iris_Week6_Monday_CheatKiss","EP14"])
    $ gamevariable_listP1.append(["Iris_Week6_Monday_Garage_Sex","EP14"])
    $ gamevariable_listP1.append(["LayLena","EP14"])
    $ gamevariable_listP1.append(["Layla_Week6_Monday_Spanish_OfferHelp","EP14"])
    $ gamevariable_listP1.append(["MC_Week6_Monday_WinGame","EP14"])
    $ gamevariable_listP1.append(["Melissa_LikeMC","EP14"])
    $ gamevariable_listP1.append(["Melissa_Week6_Monday_Compliment","EP14"])
    $ gamevariable_listP1.append(["Melissa_Week6_Monday_Sex","EP14"])
    $ gamevariable_listP1.append(["NikkiCara_Week6_Monday_MiraLie","EP14"])
    $ gamevariable_listP1.append(["NikkiCara_Week6_Monday_MiraMention","EP14"])
    $ gamevariable_listP1.append(["Riverside_MiraTruth","EP14"])
    $ gamevariable_listP1.append(["Valeria_Week6_Monday_EmoDate","EP14"])
    $ gamevariable_listP1.append(["Week6_Monday_BBQ_Invitation","EP14"])
    $ gamevariable_listP1.append(["Week6_Monday_Relay_PickLayla","EP14"])
    $ gamevariable_listP1.append(["Week6_Monday_Relay_PickTori","EP14"])
    $ gamevariable_listP1.append(["Zach_Week6_Monday_BikeSuspect","EP14"])
    $ gamevariable_listP1.append(["Zach_Week6_Monday_Punch","EP14"])
    #Ep15
    $ gamevariable_listP1.append(["Adriana_Week6_Tuesday_ImagineBJ","EP15"])
    $ gamevariable_listP1.append(["Adriana_Week6_Tuesday_ParkingKiss","EP15"])
    $ gamevariable_listP1.append(["Adriana_Week6_Tuesday_PhoneNumber","EP15"])
    $ gamevariable_listP1.append(["Adriana_Week6_Tuesday_VeganJoke","EP15"])
    $ gamevariable_listP1.append(["Alexis_Week6_Tuesday_Break","EP15"])
    $ gamevariable_listP1.append(["Alexis_Week6_Tuesday_Fight","EP15"])
    $ gamevariable_listP1.append(["Alexis_Week6_Tuesday_GoodGirl","EP15"])
    $ gamevariable_listP1.append(["Alexis_Week6_Tuesday_MSU_Help","EP15"])
    $ gamevariable_listP1.append(["Alexis_Week6_Tuesday_MSU_Jealous","EP15"])
    $ gamevariable_listP1.append(["Alexis_Week6_Tuesday_MSU_Play","EP15"])
    $ gamevariable_listP1.append(["Alexis_Week6_Tuesday_Phone_Ignore","EP15"])
    $ gamevariable_listP1.append(["Alexis_Week6_Tuesday_PreviousHookups","EP15"])
    $ gamevariable_listP1.append(["Alexis_Week6_Tuesday_Shower_CumFace","EP15"])
    $ gamevariable_listP1.append(["CaraNikki_Week6_Wednesday_BikiniShopping","EP15"])
    $ gamevariable_listP1.append(["CaraNikki_Week6_Wednesday_SaturdayClub","EP15"])
    $ gamevariable_listP1.append(["Cara_Week6_Wednesday_Breakup","EP15"])
    $ gamevariable_listP1.append(["Dani_Week6_Wednesday_Rumour","EP15"])
    $ gamevariable_listP1.append(["Darryl_Week6_Wednesday_School_Confront","EP15"])
    $ gamevariable_listP1.append(["Emily_Week6_Tuesday_SlapAss","EP15"])
    $ gamevariable_listP1.append(["Erynn_Week6_Tuesday_AlexisBreakupNotKnow","EP15"])
    $ gamevariable_listP1.append(["Erynn_Week6_Tuesday_BJ","EP15"])
    $ gamevariable_listP1.append(["Erynn_Week6_Tuesday_MSU_Note","EP15"])
    $ gamevariable_listP1.append(["Erynn_Week6_Tuesday_MSU_Paper","EP15"])
    $ gamevariable_listP1.append(["Gabi_Week6_Wednesday_School_Ignore","EP15"])
    $ gamevariable_listP1.append(["Lakeyn_Week6_Tuesday_CatchUp","EP15"])
    $ gamevariable_listP1.append(["Lakeyn_Week6_Tuesday_CheckOut","EP15"])
    $ gamevariable_listP1.append(["Layla_Week6_Tuesday_MonroeBBQ_1v1","EP15"])
    $ gamevariable_listP1.append(["MC_Week6_Wednesday_OnTheList","EP15"])
    $ gamevariable_listP1.append(["MC_Week6_Wednesday_RobIsYourNewBestFriend","EP15"])
    $ gamevariable_listP1.append(["MC_Week6_Wednesday_School_Kiss","EP15"])
    $ gamevariable_listP1.append(["MC_Week6_Wednesday_Speedo","EP15"])
    $ gamevariable_listP1.append(["NikkiCara_Week6_Wednesday_Breakup","EP15"])
    $ gamevariable_listP1.append(["Nikki_Week6_Wednesday_Breakup","EP15"])
    $ gamevariable_listP1.append(["Nikki_Week6_Wednesday_CaraPicture","EP15"])
    $ gamevariable_listP1.append(["Nikki_Week6_Wednesday_Goddess","EP15"])
    $ gamevariable_listP1.append(["Nikki_Week6_Wednesday_LeggingsCameltoe","EP15"])
    $ gamevariable_listP1.append(["Nikki_Week6_Wednesday_PullUpComp","EP15"])
    $ gamevariable_listP1.append(["Nikki_Week6_Wednesday_School_Jealousy","EP15"])
    $ gamevariable_listP1.append(["Riverside_Girlfriend","EP15"])
    $ gamevariable_listP1.append(["Sienna_Week6_Tuesday_SexProposition","EP15"])
    $ gamevariable_listP1.append(["Sienna_Week6_Wednesday_Sex","EP15"])
    $ gamevariable_listP1.append(["Tori_Week6_Wednesday_GrabAss","EP15"])
    $ gamevariable_listP1.append(["Tori_Week6_Wednesday_ShowerSex","EP15"])
    $ gamevariable_listP1.append(["Valeria_Dating","EP15"])
    $ gamevariable_listP1.append(["Valeria_End","EP15"])
    $ gamevariable_listP1.append(["Valeria_Week6_Tuesday_EmoCancel","EP15"])
    $ gamevariable_listP1.append(["Valeria_Week6_Tuesday_EmoDate","EP15"])
    $ gamevariable_listP1.append(["Valeria_Week6_Tuesday_EmoHairCute","EP15"])
    $ gamevariable_listP1.append(["Valeria_Week6_Tuesday_GeographyProject","EP15"])
    $ gamevariable_listP1.append(["Valeria_Week6_Tuesday_LikeEmoLook","EP15"])
    $ gamevariable_listP1.append(["Valeria_Week6_Wednesday_KnowYoungMC","EP15"])
    $ gamevariable_listP1.append(["Valeria_Week6_Wednesday_MomBadSide","EP15"])
    $ gamevariable_listP1.append(["Valeria_Week6_Wednesday_Shortcut","EP15"])
    $ gamevariable_listP1.append(["Valeria_Week6_Wednesday_SolName","EP15"])
    $ gamevariable_listP1.append(["Valeria_Week6_Wednesday_Spanish","EP15"])
    $ gamevariable_listP1.append(["Week6_Tuesday_Monroe_BBQ","EP15"])
    $ gamevariable_listP1.append(["Ximena_Week6_Tuesday_Cinema","EP15"])
    $ gamevariable_listP1.append(["Ximena_Week6_Tuesday_FavouriteActress","EP15"])
    $ gamevariable_listP1.append(["Ximena_Week6_Tuesday_GrabAss","EP15"])
    $ gamevariable_listP1.append(["Ximena_Week6_Tuesday_Kiss","EP15"])
    $ gamevariable_listP1.append(["Ximena_Week6_Wednesday_Gabi_End","EP15"])
    $ gamevariable_listP1.append(["Ximena_Week6_Wednesday_Valeria_Aunt","EP15"])
    #Ep16
    $ gamevariable_listP1.append(["MC_Week6_Wednesday_EthanCrash_Call","EP16"])
    $ gamevariable_listP1.append(["Erynn_Week6_Wednesday_TellEverything","EP16"])
    $ gamevariable_listP1.append(["Erynn_Week6_Wednesday_StayOver","EP16"])
    $ gamevariable_listP1.append(["MC_Week6_Wednesday_Dogs","EP16"])
    $ gamevariable_listP1.append(["MC_Week6_Wednesday_Cats","EP16"])
    $ gamevariable_listP1.append(["Erynn_Week6_Wednesday_StayOver_Past","EP16"])
    $ gamevariable_listP1.append(["Erynn_Week6_Wednesday_StayOver_RightHere","EP16"])
    $ gamevariable_listP1.append(["Erynn_Week6_Wednesday_StayOver_Mountains","EP16"])
    $ gamevariable_listP1.append(["Iris_Week6_Thursday_Hospital_Kiss","EP16"])


screen KoGa3ScreenCheatMore1():
    add "/KoGa3MenuBack.png"
    modal True
    frame:
        xsize 975 ysize 900
        xalign 0.53
        ypos 34 #yalign 0.5
        background (None)

        vbox:
            xalign 0.5
            spacing -12
            textbutton _("━━━━━━━━━━━━━━ Game variables for EP: ━━━━━━━━━━━━━━"):
                text_style "KoGa3_1_button_text"
                sensitive False
                action NullAction()

            hbox:
                spacing 10
                if KoGa3CheatChapterButton is 1:
                    textbutton ("1"):
                        text_style "KoGa3_1a_button_text"
                        selected True
                        action NullAction()
                else:
                    textbutton ("1"):
                        text_style "KoGa3_1a_button_text"
                        selected False
                        action [
                        SetVariable("KoGa3CheatChapterButton", 1) ]

                if KoGa3CheatChapterButton is 2:
                    textbutton ("2"):
                        text_style "KoGa3_1a_button_text"
                        selected True
                        action NullAction()
                else:
                    textbutton ("2"):
                        text_style "KoGa3_1a_button_text"
                        selected False
                        action [
                        SetVariable("KoGa3CheatChapterButton", 2) ]

                if KoGa3CheatChapterButton is 3:
                    textbutton ("3"):
                        text_style "KoGa3_1a_button_text"
                        selected True
                        action NullAction()
                else:
                    textbutton ("3"):
                        text_style "KoGa3_1a_button_text"
                        selected False
                        action [
                        SetVariable("KoGa3CheatChapterButton", 3) ]

                if KoGa3CheatChapterButton is 4:
                    textbutton ("4"):
                        text_style "KoGa3_1a_button_text"
                        selected True
                        action NullAction()
                else:
                    textbutton ("4"):
                        text_style "KoGa3_1a_button_text"
                        selected False
                        action [
                        SetVariable("KoGa3CheatChapterButton", 4) ]

                if KoGa3CheatChapterButton is 5:
                    textbutton ("5"):
                        text_style "KoGa3_1a_button_text"
                        selected True
                        action NullAction()
                else:
                    textbutton ("5"):
                        text_style "KoGa3_1a_button_text"
                        selected False
                        action [
                        SetVariable("KoGa3CheatChapterButton", 5) ]

                if KoGa3CheatChapterButton is 6:
                    textbutton ("6"):
                        text_style "KoGa3_1a_button_text"
                        selected True
                        action NullAction()
                else:
                    textbutton ("6"):
                        text_style "KoGa3_1a_button_text"
                        selected False
                        action [
                        SetVariable("KoGa3CheatChapterButton", 6) ]

                if KoGa3CheatChapterButton is 7:
                    textbutton ("7"):
                        text_style "KoGa3_1a_button_text"
                        selected True
                        action NullAction()
                else:
                    textbutton ("7"):
                        text_style "KoGa3_1a_button_text"
                        selected False
                        action [
                        SetVariable("KoGa3CheatChapterButton", 7) ]

                if KoGa3CheatChapterButton is 8:
                    textbutton ("8"):
                        text_style "KoGa3_1a_button_text"
                        selected True
                        action NullAction()
                else:
                    textbutton ("8"):
                        text_style "KoGa3_1a_button_text"
                        selected False
                        action [
                        SetVariable("KoGa3CheatChapterButton", 8) ]

                if KoGa3CheatChapterButton is 9:
                    textbutton ("9"):
                        text_style "KoGa3_1a_button_text"
                        selected True
                        action NullAction()
                else:
                    textbutton ("9"):
                        text_style "KoGa3_1a_button_text"
                        selected False
                        action [
                        SetVariable("KoGa3CheatChapterButton", 9) ]

                if KoGa3CheatChapterButton is 10:
                    textbutton ("10"):
                        text_style "KoGa3_1a_button_text"
                        selected True
                        action NullAction()
                else:
                    textbutton ("10"):
                        text_style "KoGa3_1a_button_text"
                        selected False
                        action [
                        SetVariable("KoGa3CheatChapterButton", 10) ]

                if KoGa3CheatChapterButton is 11:
                    textbutton ("11"):
                        text_style "KoGa3_1a_button_text"
                        selected True
                        action NullAction()
                else:
                    textbutton ("11"):
                        text_style "KoGa3_1a_button_text"
                        selected False
                        action [
                        SetVariable("KoGa3CheatChapterButton", 11) ]

                if KoGa3CheatChapterButton is 12:
                    textbutton ("12"):
                        text_style "KoGa3_1a_button_text"
                        selected True
                        action NullAction()
                else:
                    textbutton ("12"):
                        text_style "KoGa3_1a_button_text"
                        selected False
                        action [
                        SetVariable("KoGa3CheatChapterButton", 12) ]

                if KoGa3CheatChapterButton is 13:
                    textbutton ("13"):
                        text_style "KoGa3_1a_button_text"
                        selected True
                        action NullAction()
                else:
                    textbutton ("13"):
                        text_style "KoGa3_1a_button_text"
                        selected False
                        action [
                        SetVariable("KoGa3CheatChapterButton", 13) ]

                if KoGa3CheatChapterButton is 14:
                    textbutton ("14"):
                        text_style "KoGa3_1a_button_text"
                        selected True
                        action NullAction()
                else:
                    textbutton ("14"):
                        text_style "KoGa3_1a_button_text"
                        selected False
                        action [
                        SetVariable("KoGa3CheatChapterButton", 14) ]

                if KoGa3CheatChapterButton is 15:
                    textbutton ("15"):
                        text_style "KoGa3_1a_button_text"
                        selected True
                        action NullAction()
                else:
                    textbutton ("15"):
                        text_style "KoGa3_1a_button_text"
                        selected False
                        action [
                        SetVariable("KoGa3CheatChapterButton", 15) ]

                if KoGa3CheatChapterButton is 16:
                    textbutton ("16"):
                        text_style "KoGa3_1a_button_text"
                        selected True
                        action NullAction()
                else:
                    textbutton ("16"):
                        text_style "KoGa3_1a_button_text"
                        selected False
                        action [
                        SetVariable("KoGa3CheatChapterButton", 16) ]


            textbutton ("────────────────────────────────────────────────"):
                text_style "KoGa3_1_button_text"
                sensitive False
                action NullAction()

            viewport id "vp":
                draggable True
                mousewheel True
                scrollbars "vertical"
                xalign 0.5
                yalign 0.0
                vbox:
                    xalign 0.5
                    spacing -19

                    ################### Episode 1 ###################### 
                    if KoGa3CheatChapterButton == 1:
                        for i in gamevariable_listP1:
                            if i[1] == "EP1":
                                hbox:
                                    textbutton i[0]:
                                       #  selected False
                                        text_style "KoGa3_1a_button_text"
                                        action ToggleVariable(i[0])

                    ################### Episode 2 ###################### 
                    if KoGa3CheatChapterButton == 2:
                        for i in gamevariable_listP1:
                            if i[1] == "EP2":
                                hbox:
                                    textbutton i[0]:
                                       #  selected False
                                        text_style "KoGa3_1a_button_text"
                                        action ToggleVariable(i[0])

                    ################### Episode 3 ###################### 
                    if KoGa3CheatChapterButton == 3:
                        for i in gamevariable_listP1:
                            if i[1] == "EP3":
                                hbox:
                                    textbutton i[0]:
                                       #  selected False
                                        text_style "KoGa3_1a_button_text"
                                        action ToggleVariable(i[0])

                    ################### Episode 4 ###################### 
                    if KoGa3CheatChapterButton == 4:
                        for i in gamevariable_listP1:
                            if i[1] == "EP4":
                                hbox:
                                    textbutton i[0]:
                                       #  selected False
                                        text_style "KoGa3_1a_button_text"
                                        action ToggleVariable(i[0])

                    ################### Episode 5 ###################### 
                    if KoGa3CheatChapterButton == 5:
                        for i in gamevariable_listP1:
                            if i[1] == "EP5":
                                hbox:
                                    textbutton i[0]:
                                       #  selected False
                                        text_style "KoGa3_1a_button_text"
                                        action ToggleVariable(i[0])

                    ################### Episode 6 ###################### 
                    if KoGa3CheatChapterButton == 6:
                        for i in gamevariable_listP1:
                            if i[1] == "EP6":
                                hbox:
                                    textbutton i[0]:
                                       #  selected False
                                        text_style "KoGa3_1a_button_text"
                                        action ToggleVariable(i[0])

                    ################### Episode 7 ###################### 
                    if KoGa3CheatChapterButton == 7:
                        for i in gamevariable_listP1:
                            if i[1] == "EP7":
                                hbox:
                                    textbutton i[0]:
                                       #  selected False
                                        text_style "KoGa3_1a_button_text"
                                        action ToggleVariable(i[0])

                     ################### Episode 8 ###################### 
                    if KoGa3CheatChapterButton == 8:
                        for i in gamevariable_listP1:
                            if i[1] == "EP8":
                                hbox:
                                    textbutton i[0]:
                                       #  selected False
                                        text_style "KoGa3_1a_button_text"
                                        action ToggleVariable(i[0])

                    ################### Episode 9 ###################### 
                    if KoGa3CheatChapterButton == 9:
                        for i in gamevariable_listP1:
                            if i[1] == "EP9":
                                hbox:
                                    textbutton i[0]:
                                       #  selected False
                                        text_style "KoGa3_1a_button_text"
                                        action ToggleVariable(i[0])

                    ################### Episode 10 ###################### 
                    if KoGa3CheatChapterButton == 10:
                        for i in gamevariable_listP1:
                            if i[1] == "EP10":
                                hbox:
                                    textbutton i[0]:
                                       #  selected False
                                        text_style "KoGa3_1a_button_text"
                                        action ToggleVariable(i[0])

                    ################### Episode 11 ###################### 
                    if KoGa3CheatChapterButton == 11:
                        for i in gamevariable_listP1:
                            if i[1] == "EP11":
                                hbox:
                                    textbutton i[0]:
                                       #  selected False
                                        text_style "KoGa3_1a_button_text"
                                        action ToggleVariable(i[0])

                    ################### Episode 12 ###################### 
                    if KoGa3CheatChapterButton == 12:
                        for i in gamevariable_listP1:
                            if i[1] == "EP12":
                                hbox:
                                    textbutton i[0]:
                                       #  selected False
                                        text_style "KoGa3_1a_button_text"
                                        action ToggleVariable(i[0])

                    ################### Episode 13 ###################### 
                    if KoGa3CheatChapterButton == 13:
                        for i in gamevariable_listP1:
                            if i[1] == "EP13":
                                hbox:
                                    textbutton i[0]:
                                       #  selected False
                                        text_style "KoGa3_1a_button_text"
                                        action ToggleVariable(i[0])

                    ################### Episode 14 ###################### 
                    if KoGa3CheatChapterButton == 14:
                        for i in gamevariable_listP1:
                            if i[1] == "EP14":
                                hbox:
                                    textbutton i[0]:
                                       #  selected False
                                        text_style "KoGa3_1a_button_text"
                                        action ToggleVariable(i[0])

                    ################### Episode 15 ###################### 
                    if KoGa3CheatChapterButton == 15:
                        for i in gamevariable_listP1:
                            if i[1] == "EP15":
                                hbox:
                                    textbutton i[0]:
                                       #  selected False
                                        text_style "KoGa3_1a_button_text"
                                        action ToggleVariable(i[0])

                    ################### Episode 16 ###################### 
                    if KoGa3CheatChapterButton == 16:
                        for i in gamevariable_listP1:
                            if i[1] == "EP16":
                                hbox:
                                    textbutton i[0]:
                                       #  selected False
                                        text_style "KoGa3_1a_button_text"
                                        action ToggleVariable(i[0])

            textbutton ("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"):
                text_style "KoGa3_1_button_text"
                sensitive False
                action NullAction()
            hbox:
                spacing 50
                textbutton _("Back"):
                    text_style "KoGa3_1_button_text" 
                    action [
                    Hide("KoGa3ScreenCheatMore1"), 
                    Show("KoGa3ScreenCheat") ]
                textbutton _("Close"):
                    text_style "KoGa3_1_button_text"
                    selected False
                    action [
                    SetVariable ("KoGa3ModMenuButtonPressed", False),
                    Hide("KoGa3ScreenCheatMore1") ]


#---------------------add. game settings---------------------#
screen KoGa3GameSettings:
    if not main_menu:
        add "/KoGa3MenuBack_settings.png"
    modal True
    vbox:
        xalign 0.5
        spacing -12
        null height (54)

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

            hbox:
                # hbox:
                    # xsize 245
                    # textbutton ("Walkthrough: "):
                        # text_style "KoGa3_1a_button_text"
                        # sensitive False
                        # action NullAction()
                # hbox:
                    # xsize 240
                    # if KoGa3WTChange == "\n{size=1}{color=#363636}":
                        # textbutton _("OFF"):
                            # text_style "KoGa3_1a_button_text"
                            # selected False
                            # action [
                            # SetVariable ("KoGa3WTChange", "\n{size=32}{color=#008000}"),
                            # SetVariable ("KoGa3WTChange1", "\n{size=32}{color=#ffdf00}"),
                            # SetVariable ("KoGa3WTChange2", "\n{size=32}{color=#ff0000}") ]
                    # else:
                        # textbutton _("ON "):
                            # text_style "KoGa3_1a_button_text"
                            # selected False
                            # action [
                            # SetVariable ("KoGa3WTChange", "\n{size=1}{color=#363636}"),
                            # SetVariable ("KoGa3WTChange1", "\n{size=1}{color=#363636}"),
                            # SetVariable ("KoGa3WTChange2", "\n{size=1}{color=#363636}") ]

                textbutton _("Change MC name..."):
                    text_style "KoGa3_1a_button_text"
                    selected False
                    action [
                    Hide("KoGa3GameSettings"),
                    Show("KoGa3ScreenBlank"),
                    Call("KoGa3NameChange") ]

            null height (35)

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
                        spacing -10
                        hbox:
                            hbox:
                                xsize 340
                                textbutton _("Quick menu:"):
                                    text_style "KoGa3_1a_button_text"
                                    sensitive False
                                    action NullAction()
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
                        null height 10
                        hbox:
                            hbox:
                                xsize 340
                                textbutton _("Quick menu buttons:"):
                                    text_style "KoGa3_1a_button_text"
                                    sensitive False
                                    action NullAction()
                            hbox:
                                #xsize 200
                                if persistent.KoGa3QuickMenuIcons is True:
                                    textbutton _("Icons"):
                                        text_style "KoGa3_1a_button_text"
                                        selected False
                                        action [
                                        SetVariable ("persistent.KoGa3QuickMenuIcons", False)]
                                else:
                                    textbutton _("Text"):
                                        text_style "KoGa3_1a_button_text"
                                        selected False
                                        action [
                                        SetVariable ("persistent.KoGa3QuickMenuIcons", True)]
                        null height 15
                        hbox:
                            hbox:
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
                    Show("KoGa3ScreenCheat") ]
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

        vbox:
            spacing -12
            hbox:
                hbox:
                    xsize 340
                    textbutton _("Quick menu:"):
                        text_style "KoGa3_1a_button_text"
                        sensitive False
                        action NullAction()
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
            null height 10
            hbox:
                hbox:
                    xsize 340
                    textbutton _("Quick menu buttons:"):
                        text_style "KoGa3_1a_button_text"
                        sensitive False
                        action NullAction()
                hbox:
                    #xsize 200
                    if persistent.KoGa3QuickMenuIcons is True:
                        textbutton _("Icons"):
                            text_style "KoGa3_1a_button_text"
                            selected False
                            action [
                            SetVariable ("persistent.KoGa3QuickMenuIcons", False)]
                    else:
                        textbutton _("Text"):
                            text_style "KoGa3_1a_button_text"
                            selected False
                            action [
                            SetVariable ("persistent.KoGa3QuickMenuIcons", True)]

        textbutton _("───────────────────────────────────────────"):
            text_style "KoGa3_1_button_text"
            sensitive False
            action NullAction()

        null height (20)

        vbox:
            spacing -8
            hbox:
                xpos 6
                text _("Quick menu font size  (current: [persistent.KoGa3QuickMenuTextSize]/40)"):
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
                xpos 6
                text _("Quick menu font outline  (current: [persistent.KoGa3TextOutline4]/10)"):
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
                    spacing -13

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


#-----------------------set name----------------------#
label KoGa3NameChange:
    menu:
        "MC first name: {color=[KoGa3Color2]}[name]{/color} - change...":
            $ name = renpy.input("What is your first name?", default=name)
            $ name = name.strip()
            $ persistent.nameRePlay = name    #old, not used anymore since v0.12
            $ persistent.player_name = name
            $ entered_name = name
            jump KoGa3NameChange
        "Back":
            hide screen KoGa3ScreenBlank
            show screen KoGa3GameSettings
            pause
            return






#--------------set default game variables---------------#
init 999 python:
    Adriana_Points = 0
    Alexis_BeachPoints = 0
    Alexis_JealousyPoints = 0
    Alexis_Points = 0
    Alexis_SP = 0
    Andres_Points = 0
    Brooke_Points = 0
    Cara_Points = 0
    Cara_Visit_Points = 0
    Cara_Weekend_Points = 0
    Darryl_Points = 0
    Elena_Points = 0
    Emily_Points = 0
    Erynn_Points = 0
    Gabi_Jealousy = 0
    Gabi_Points = 0
    Gabi_Suspicion = 0
    Iris_Points = 0
    Julia_Points = 0
    Lakeyn_Points = 0
    Layla_Points = 0
    MC_GoodStudent = 0
    Marisol_Points = 0
    Melissa_Points = 0
    Mira_Points = 0
    Naomi_Points = 0
    Natasha_Points = 0
    Nikki_Points = 0
    Nikki_SPoints = 0
    Nikki_Visit_Points = 0
    Nikki_Weekend_Points = 0
    Rachel_Points = 0
    ShaCarri_Points = 0
    Sienna_Points = 0
    Tori_Points = 0
    Valeria_Points = 0
    Ximena_Points = 0
    Zach_Points = 0


    Adriana_PointsTemp = 0
    Alexis_BeachPointsTemp = 0
    Alexis_JealousyPointsTemp = 0
    Alexis_PointsTemp = 0
    Alexis_SPTemp = 0
    Andres_PointsTemp = 0
    Brooke_PointsTemp = 0
    Cara_PointsTemp = 0
    Cara_Visit_PointsTemp = 0
    Cara_Weekend_PointsTemp = 0
    Darryl_PointsTemp = 0
    Elena_PointsTemp = 0
    Emily_PointsTemp = 0
    Erynn_PointsTemp = 0
    Gabi_JealousyTemp = 0
    Gabi_PointsTemp = 0
    Gabi_SuspicionTemp = 0
    Iris_PointsTemp = 0
    Julia_PointsTemp = 0
    Lakeyn_PointsTemp = 0
    Layla_PointsTemp = 0
    MC_GoodStudentTemp = 0
    Marisol_PointsTemp = 0
    Melissa_PointsTemp = 0
    Mira_PointsTemp = 0
    Naomi_PointsTemp = 0
    Natasha_PointsTemp = 0
    Nikki_PointsTemp = 0
    Nikki_SPointsTemp = 0
    Nikki_Visit_PointsTemp = 0
    Nikki_Weekend_PointsTemp = 0
    Rachel_PointsTemp = 0
    ShaCarri_PointsTemp = 0
    Sienna_PointsTemp = 0
    Tori_PointsTemp = 0
    Valeria_PointsTemp = 0
    Ximena_PointsTemp = 0
    Zach_PointsTemp = 0


    #defaults for cheat (in the Ep scripts only set with $, not defaulted)
    #Ep1
    Alexis_Friends = False
    Alexis_Sex = False
    Alexis_Intro_Ignore = False
    Alexis_Intro_Join = False
    Rachel_Intro_CheckOut = False
    Rachel_Intro_BJ = False
    Rachel_End = False
    Melissa_Intro_Hug = False
    Melissa_Intro_Sunbath = False
    MC_Week1_Monday_Skip = False
    #Ep2
    Layla_Week1_Monday_Payattention = False
    Layla_Week1_Monday_Four = False
    Layla_Week1_Monday_Legs = False
    Layla_Week1_Monday_Sand = False
    Alexis_Week1_Monday_TellZach = False
    Alexis_Week1_Monday_BarWait = False
    Elena_Week1_Tuesday_Science_Complain = False
    Elena_Week1_Tuesday_Intervene = False
    Erynn_Week2_Tuesday_AlexisFight = False
    #Ep3
    Layla_Week1_Wednesday_HallwayTalk = False
    Layla_Week1_Wednesday_ParkHelp = False
    Layla_Week1_Wednesday_ParkStay = False
    Alexis_Week1_Wednesday_PhonePickup = False
    Alexis_Week1_Wednesday_PhoneHome = False
    Alexis_Week1_Wednesday_PhoneIgnore = False
    Alexis_Lexi = False
    Mike_Name = False
    Tori_Sex = False
    Sienna_Name = False
    Dylan_Week1_Assumption = False
    Tori_Week1_Interested = False
    Elena_Cute = False
    Erynn_Week1_Stay = False
    Erynn_Week1_ShowerJoin = False
    Elena_Week1_TrainKissLayla = False
    Elena_Week1_TrainKiss = False
    Layla_Week1_Piggyback = False
    Erynn_Week1_Cupsize = False
    #Ep4
    Cara_FB_Club_Dance = False
    Lakeyn_FB_Sex = False
    Lakeyn_End = False
    Nikki_FB_Butt = False
    Nikki_FB_Pancakes = False
    Nikki_FB_PureEvil = False
    Cara_FB_OfferBikeRide = False
    Cara_FB_BikeCity = False
    Nikki_FB_Run = False
    Nikki_FB_Run_Peak = False
    Cara_FB_Talk = False
    Nikki_FB_TouchBoobs = False
    Nikki_FB_Carry = False
    Nikki_FB_ShowerheadStory = False
    Cara_FB_Masturbate = False
    Cara_FB_CopyAssignment = False
    Cara_FB_StudyTogether = False
    Nikki_FB_ParkFlirt = False
    Nikki_FB_Help = False
    Nikki_FB_Dance = False
    Nikki_FB_Club_Carry = False
    Nikki_FB_Room_Stay = False
    Riverside_Friends = False
    Riverside_FB_NikkiCaraChoice = False
    Nikki_FB_Choose = False
    Cara_FB_Choose = False
    Andres_FB_Punch = False
    Nikki_SP = False
    Cara_Girlfriend = False
    Nikki_Girlfriend = False
    FB_Riverside_Nathan_Fight = False
    Julia_FB_Sex = False
    Nikki_Cheat = False
    Cara_Cheat = False
    Erynn_Week1_Saturday_Picture = False
    Layla_Week1_Saturday_BeachInvite = False
    Layla_Week1_Saturday_Ignore = False
    Erynn_Week1_Saturday_Pool = False
    Melissa_Week1_Saturday_Payback = False
    Erynn_Week1_Saturday_LookBoobs = False
    Emily_Week1_Saturday_Lie = False
    Emily_Week1_Saturday_BeachInvite = False
    Layla_Week1_Saturday_Beach = False
    Layla_Week1_Saturday_Beach_Kiss = False
    Layla_Week1_Saturday_Beach_Slap = False
    Layla_Week1_Saturday_Beach_Massage = False
    Layla_Week1_Saturday_Beach_Ocean = False
    Layla_Week1_Saturday_Beach_Boobs = False
    Layla_Week1_Saturday_Beach_UnderwaterKiss = False
    Layla_Week1_Saturday_Pareo = False
    Layla_Week1_Saturday_Beach_Forget = False
    Elena_Week1_Saturday_Beach_Sunscreen = False
    Elena_Week1_Saturday_Beach_Towel = False
    Elena_Week1_Saturday_Beach_Reminder = False
    Elena_Week1_Saturday_Beach_Tease = False
    Layla_Week1_Saturday_Picture = False
    Layla_Week1_Saturday_PictureElena = False
    Rachel_Week1_Saturday_Picture = False
    Alexis_Week1_Saturday_Picture = False
    Rachel_Week1_Saturday_KickOut = False
    Rachel_Week1_Saturday_Sex = False
    Alexis_Week1_Saturday_Picture_Night = False
    Alexis_Week1_Saturday_JokePicture = False
    Alexis_Week1_Sunday_Flower = False
    Alexis_Week1_Sunday_Chocolate = False
    Alexis_Week1_Sunday_Concert_Sing = False
    Alexis_Week1_Sunday_Concert_Great = False
    Alexis_Week1_Concert = False
    #Ep5
    Layla_Week2_Detention = False
    Adriana_Week2_Monday_TestBack = False
    Mike_Week2_Monday_Surname = False
    Adriana_Week2_Monday_Truth = False
    Layla_Week2_Monday_Wait = False
    Layla_Week2_Monday_LucasHelp = False
    Week2_Monday_Erynn_Help = False
    Week2_Monday_Erynn_Hair = False
    Melissa_Week2_Monday_Milf = False
    Week2_Monday_Erynn_Ethan = False
    Erynn_Week2_Monday_GoToErynn = False
    Week2_Monday_Bar_Stay = False
    Zach_Week2_Monday_House = False
    Zach_Week2_Monday_Sister = False
    Gabi_End = False
    Erynn_Week2_Monday_Bed = False
    Cara_Week2_Tuesday_Phonecall = False
    Nikki_Week2_Tuesday_Phonecall = False
    Erynn_Week2_Tuesday_Shirt = False
    Natasha_Week2_Tuesday_MikeSex = False
    Layla_Week2_Tuesday_Lie = False
    Layla_Week2_Tuesday_Sergeant = False
    Gabi_Week2_Tuesday_Pullout = False
    Elena_Week2_Tuesday_CheerHot = False
    Elena_Week2_Tuesday_RecruitJoke = False
    Erynn_Week2_Tuesday_CorrectHer = False
    Erynn_Week2_Tuesday_Gift = False
    Erynn_Week2_Tuesday_Pickup = False
    Erynn_Week2_Tuesday_AlexisFight = False
    #Ep6
    Erynn_Week2_Tuesday_Fly = False
    Melissa_Week2_Tuesday_Dream = False
    Melissa_Week2_Wednesday_Stories = False
    Naomi_Week2_Wednesday_Math_Answer = False
    Layla_Week2_Wednesday_Rude = False
    Layla_Week2_Wednesday_HelpUp = False
    Layla_Week2_Wednesday_Knows = False
    Alexis_Week2_Wednesday_Tell = False
    Alexis_Week2_Wednesday_Breakup = False
    Layla_Friends = False
    Layla_Week2_Wednesday_SpanishHelp = False
    Layla_Week2_Wednesday_CheckOut = False
    Layla_Week2_Wednesday_Chichis = False
    Erynn_Week2_Thursday_Confront = False
    Erynn_Friends = False
    Riverside_End = False
    Nikki_Week2_Weekend_Movie = False
    Nikki_Week2_Weekend_Handle = False
    Nikki_Week2_Weekend_SexInside = False
    Cara_Week2_Weekend_SexInside = False
    #Ep7
    Emily_Week2_Saturday_Checkup = False
    Brooke_Week2_Saturday_TurnDown = False
    Team_Triss = False
    Team_Yennefer = False
    Adriana_Week2_Sunday_Dinner = False
    Alexis_Week2_Sunday_Honest = False
    Layla_Week2_Sunday_TV_Makeout = False
    Alexis_Week2_Sunday_PhoneSex = False
    Valeria_Week3_Monday_Meet = False
    Valeria_Week3_Monday_NotMyType = False
    Week3_Monday_Spanish_Steal = False
    Week3_Monday_Spanish_Blackmail = False
    Layla_Week3_Monday_Spanish_Fail = False
    Elena_Week3_Monday_Help = False
    Elena_Week3_Monday_CheerTraining = False
    Elena_Week3_Monday_Backflip = False
    Erynn_Week3_Monday_Help = False
    Erynn_Week3_Monday_Blackmailhelp = False
    Erynn_End = False
    Alexis_End = False
    Elena_Friends = False
    Valeria_Friends = False
    Erynn_Week3_Monday_Alexis_Mention = False
    Erynn_Week3_Monday_Makeout = False
    Erynn_Week3_Tuesday_Sandwich = False
    Layla_Week3_Tuesday_Train = False
    Layla_Week3_Tuesday_Race = False
    Layla_Week3_Tuesday_Race_Win = False
    Alexis_Week3_Tuesday_Date = False
    Alexis_Week3_Tuesday_LexySexySong = False
    #Ep8
    Erynn_Week3_Wednesday_Lying = False
    Zach_Week3_Wednesday_Seats = False
    Valeria_Week3_Wednesday_Pictures = False
    Layla_Week3_Wednesday_TC_Kiss = False
    Layla_Week3_Wednesday_TC_TrainingPartner = False
    Tori_Week3_Wednesday_TC_Fun = False
    Layla_Week3_Wednesday_TC_AlexisTalk = False
    Zach_Week3_Wednesday_TC_Girlshower = False
    Iris_Week3_Sunday_Meet = False
    Alexis_Week3_Wednesday_TC_Breakup = False
    Layla_Week3_Wednesday_TC_Alexis_DateBoth = False
    Layla_LikeMC = False
    Layla_Dating = False
    Alexis_Dating = False
    Valeria_Week3_Thursday_TC_Massage = False
    Alexis_Week3_Wednesday_TC_FriendsButKissedLayla = True
    Zach_Week3_Thursday_TC_Box = False
    Layla_Week3_Friday_TC_Wager = False
    TC_Pool_Layla = False
    TC_Pool_Elena = False
    TC_Pool_Sienna = False
    TC_Pool_Valeria = False
    Tori_Week3_Friday_TC_Step = False
    Gabi_Week3_Friday_TC_Picture = False
    Week3_Friday_TC_Kickball = False
    ShaCarri_End = False
    MC_Week3_Saturday_TC_Win = False
    Tori_End = False
    Tori_LickAss = False
    Tori_Week3_Saturday_TC_Sex = False
    Tori_Week3_Saturday_TC_LickAss = False
    MC_Week3_Saturday_TC_Cheer_Late = False
    Gabi_Week3_Saturday_TC_Sex = False
    Gabi_Week3_Saturday_TC_CumInside = False
    Valeria_Week3_Saturday_Tea = False
    Adriana_Week3_Saturday_TC_Pick = False
    Elena_Week3_Saturday_TC_Threewaykiss = False
    Valeria_Week3_Saturday_TC_Swap = False
    Zach_Week3_Saturday_TC_Swap = False
    Layla_Week3_Saturday_TC_Swap = False
    Valeria_Week3_Saturday_TC_Peek = False
    Emily_Week3_Sunday_DareTell = False
    Emily_Week3_Sunday_Surprise = False
    Alexis_Week3_Sunday_BubbleIce = False
    Alexis_Week3_Sunday_Meet = False
    Erynn_LikeMC = False
    Iris_Week3_Sunday_Meet = False
    Alexis_Girlfriend = False
    Alexis_Week4_Monday_Meet = False
    Alexis_Week3_Sunday_PizzaJoke = False
    Alexis_Week3_Sunday_Dorm_StripteaseCute = False
    Layla_Week4_Monday_FailTest = False
    Alexis_SecretPath = False
    Layla_Week4_Monday_Hottub = False
    Layla_Week4_Monday_Hottub_BJ = False
    Alexis_Week3_Sunday_NewBartender = False
    #Ep9
    Layla_End = False
    Elena_End = False
    Nikki_Solo = False
    Nikki_Visit = False
    Nikki_MeetEmily = False
    Cara_Solo = False
    Cara_Visit = False
    Cara_MeetEmily = False
    Cara_Week4_Wednesday_Visit_Breakup = False
    Nikki_Week4_Wednesday_Visit_Breakup = False
    Alexis_RiversideStory = False
    Iris_FB_Outfit_DontLike = False
    Nikki_Week4_Wednesday_Visit_Knows = False
    Cara_Week4_Wednesday_Visit_Knows = False
    MC_Week4_Wednesday_BedOccupied = False
    MC_Week4_Thursday_SleepInEmilyBed = False
    MC_Girlfriend_Riverside = False
    # Layla_Week4_Thursday_Val_NakedRun = False #double set
    Layla_Week4_Thursday_HoldPenis = False
    Tori_Week3_Thursday_School_HJ = False
    Layla_Week4_Thursday_Val_NakedRun = False
    Layla_Week4_Thursday_WingmanVal = False
    Tori_Week4_Thursday_SeeNikki = False
    Tori_Week4_Thursday_SeeCara = False
    Mike_Week4_Thursday_NikkiCaraDad = False
    Nikki_Week4_Thursday_Swimsuit_Option1_Like = False
    Nikki_Week4_Thursday_ArmwrestlingWin = False
    Nikki_Week4_Thursday_Lotion = False
    Nikki_Week4_Thursday_LotionMC = False
    Nikki_Week4_Thursday_Handstand_Help = False
    Naomi_Week4_Thursday_Watch = False
    Cara_Week4_Thursday_Dress_Like = False
    Cara_Week4_Thursday_Dress_Sex = False
    Valeria_Week4_Thursday_MeetNikki = False
    Valeria_Week4_Friday_Help = False
    #Ep10
    Erynn_Week4_Friday_Slap = False
    Alexis_Week4_Friday_Blackmail_Involve = False
    Nikki_Week4_Friday_Oral = False
    Nikki_Week4_Friday_SleepBed = False
    Cara_Week4_Friday_Play = False
    Cara_Week4_Friday_LickAss = False
    Cara_Week4_Friday_SleepBed = False
    Erynn_Week4_Saturday_Jump_Cara = False
    Erynn_Week4_Saturday_Jump_Nikki = False
    Erynn_Week4_Saturday_Jump = False
    Erynn_Week4_Saturday_NikkiLie = False
    Erynn_Week4_Saturday_CaraLie = False
    Melissa_Week4_Saturday_Kiss = False
    Melissa_End = False
    Melissa_Week4_Saturday_Dream = False
    MC_NoFriends = False
    Darryl_SeeNikkiMC = False
    Nikki_Week4_Saturday_Icecubes = False
    Nikki_Week4_Saturday_Bed = False
    Nikki_Week4_Saturday_Sex_Inside = False
    Cara_Week4_Saturday_LickAss = False
    Alexis_Week4_Saturday_Cara_Phone = False
    Cara_Week4_Saturday_Bed = False
    Cara_Week4_Saturday_Anal_Suggestion = False
    Cara_Week4_Saturday_Sexgame = False
    Cara_Week4_Saturday_Game_Change = False
    Nikki_Week4_Wednesday_AlexisLaylaBreakUp = False
    Cara_Week4_Wednesday_AlexisLaylaBreakUp = False
    MC_Bike = False
    Emily_Week4_Sunday_Sexy = False
    Emily_Week4_Sunday_DateJohn = False
    Erynn_Week4_Sunday_OfferBikeRide = False
    Week5_Monday_Prettiest_Layla = False
    Week5_Monday_Prettiest_Valeria = False
    Week5_Monday_Prettiest_Tori = False
    Valeria_Week5_Monday_Picture = False
    Valeria_LikeMC = False
    Valeria_Week5_Monday_Photobooth = False
    Valeria_Week5_Monday_Kiss = False
    Alexis_Week5_Monday_Date_Cancel = False
    Alexis_Week5_Monday_Makeup = False
    Adriana_Week5_Monday_SlapAss = False
    Elena_Week5_Monday_Beach_Hero = False
    Elena_Week5_Monday_Beach = False
    #Ep11
    Erynn_Week5_Tuesday_Photoshoot = False
    Erynn_Week5_Tuesday_Wakeup = False
    Erynn_Week5_Tuesday_SlapAss = False
    Erynn_Week5_Tuesday_Photoshoot_Join = False
    Erynn_Week5_Tuesday_Photoshoot_HiddenFeelings = False
    Erynn_Week5_Tuesday_Photoshoot_Checkout = False
    Alexis_Week5_Photoshoot_DogPicture = False
    Erynn_Week5_Tuesday_Room_Kiss = False
    Sienna_Week5_Tuesday_Hottest = False
    Layla_Week5_Tuesday_Hottub_Towel = False
    Elena_Week5_Tuesday_Hottub_69 = False
    Layla_Week5_Tuesday_Hottub_69 = False
    Sienna_Week5_Tuesday_Hottub_Sex = False
    Elena_Week5_Tuesday_Hottub_Grab = False
    Layla_Week5_Tuesday_Hottub_Grab = False
    Layla_Week5_Tuesday_Hottub_Chickenbreast = False
    Elena_Week5_Tuesday_Hottub_Threeway = False
    Elena_LikeMC = False
    Alexis_Week5_Wednesday_Run = False
    Emily_Week5_Wednesday_BeachInvite_Adriana = False
    Alexis_Week5_Wednesday_Beach = False
    Alexis_Week5_Wednesday_Beach_SP = False
    Tori_Week5_Wednesday_Beach_Sex = False
    Tori_Week5_Wednesday_Beach_LickAss = False
    Iris_Week5_Wednesday_Beach_Sex = False
    Alexis_Week5_Wednesday_Beach_Sex = False
    KFM_Kill_Alexis = False
    KFM_Kill_Erynn = False
    KFM_Kill_Iris = False
    KFM_Fuck_Alexis = False
    KFM_Fuck_Erynn = False
    KFM_Fuck_Iris = False
    KFM_Marry_Alexis = False
    KFM_Marry_Erynn = False
    KFM_Marry_Iris = False
    Alexis_Week5_Wednesday_Beach_Join = False
    Erynn_Week5_Wednesday_Beach_Join = False
    Iris_Week5_Wednesday_Beach_Join = False
    Alexis_Week5_Wednesday_Beach_CumMouth = False
    Alexis_Week5_Wednesday_Beach_CumFace = False
    Alexis_Week5_Wednesday_Beach_CumTits = False
    Alexis_Week5_Wednesday_Club_KissIris = False
    Adriana_Week5_Wednesday_Kiss = False
    Layla_Week5_Wednesday_ClubDate = False
    Layla_Week5_Wednesday_FirstTime = False
    Layla_Week5_Wednesday_LikeElenaKnow = False
    Layla_Girlfriend = False
    Layla_Week5_Wednesday_BreakUp = False
    #Ep12
    Emily_Week5_Thursday_WitnessKissErynn = False
    Erynn_Week5_Thursday_FridayBeach = False
    Erynn_Week5_Thursday_Shower = False
    Erynn_Week5_Thursday_Photo = False
    Erynn_Week5_Thursday_SniffPanties = False
    Erynn_Week5_Thursday_Handjob = False
    Erynn_Week5_Thursday_WashBack = False
    Valeria_Week5_Thursday_Headscratches = False
    Alexis_Week5_Thursday_BreakUpTalk = False
    Valeria_Week5_Thursday_2ndChance = False
    Alexis_Week5_Thursday_KissWon = False
    Brooke_Week5_Thursday_Peek = False
    Brooke_Week5_Thursday_CollegeEmily = False
    Brooke_Week5_Thursday_MommyBrooke = False
    Brooke_Week5_Thursday_Picture = False
    Gabi_Week5_Thursday_Picture = False
    Iris_Week5_Thursday_BikeRepair = False
    Ximena_Week5_Thursday_Watch = False
    Brooke_Week5_Thursday_BikeRide = False
    John_Week5_Thursday_BikeRide = False
    Ethan_Week5_Thursday_Plan = False
    Ethan_Week5_Thursday_Punch = False
    Ethan_Week5_Thursday_Phone = False
    Gianna_Week5_Thursday_CheckOut = False
    Gianna_Week5_Thursday_Domino = False
    #Ep13
    Alexis_Week5_Thursday_Enzo = False
    Alexis_Week5_Thursday_BarKiss = False
    Alexis_Week5_Thursday_BreakUp = False
    Valeria_Week5_Thursday_CancelDate = False
    Alexis_Week5_Thursday_BreakUp_Alexis = False
    Alexis_Week5_Thursday_Fantasy_Roleplay = False
    Alexis_Week5_Thursday_Fantasy_Voyeurism = False
    Alexis_Week5_Thursday_Fantasy_Threesome = False
    Alexis_Week5_Thursday_Fantasy_Threesome_Erynn = False
    Alexis_Week5_Thursday_Fantasy_Threesome_Ximena = False
    Alexis_Week5_Thursday_Fantasy_BDSM = False
    Erynn_Week5_Friday_Date = False
    Erynn_Week5_Friday_Date_Cancel = False
    Erynn_Week5_Friday_DressingRoomHelp = False
    Erynn_Week5_Friday_Beach_Face = False
    Erynn_Week5_Friday_Beach_Boobs = False
    Erynn_Week5_Friday_Beach_Ass = False
    Erynn_Week5_Friday_Beach_Legs = False
    Erynn_Week5_Friday_Beach_Body = False
    Erynn_Week5_Friday_Beach_Bush = False
    Erynn_Week5_Friday_Beach_WellKept = False
    Erynn_Week5_Friday_Beach_LandingStrip = False
    Erynn_Week5_Friday_Beach_Shaved = False
    Erynn_Week5_Friday_Beach_OceanPee = False
    Erynn_Week5_Friday_Beach_DM = False
    Erynn_Week5_Friday_Beach_Shallow = False
    Valeria_Week5_Friday_Date = False
    Valeria_Week5_Friday_Stay = False
    Valeria_Week5_Friday_Date_Leave = False
    Valeria_Week5_Friday_NudePicture = False
    MC_MeetDonovan = False
    Lakeyn_Week5_Friday_PlayAlong = False
    Nikki_Week5_Friday_CumInside = False
    Nikki_Week5_Friday_CumOnBack = False
    Nikki_Week5_Friday_CumOnTits = False
    Mira_Week5_Saturday_Like = False
    Mira_End = False
    MC_Week5_Friday_RiversideVisit = False
    Nikki_Week5_Saturday_FartLaugh = False
    Haley_Week5_Saturday_SexWatch = False
    Haley_Week5_Saturday_Masturbate = False
    Cara_Week5_Saturday_LickAss = False
    Cara_Week5_Saturday_Anal = False
    Erynn_Week5_Sunday_Bath = False
    Emily_Week5_Sunday_Hug = False
    Alexis_Week5_Sunday_Roleplay = False
    Layla_Week5_Sunday_SantiagoDadKnow = False
    Layla_Week5_Sunday_LakeynKnow = False
    #Ep14
    Emily_Week6_Monday_FirstBikeRide = False
    ElenaLayla_Week6_Monday_BikeRevScare = False
    Week6_Monday_Relay_PickLayla = False
    Week6_Monday_Relay_PickTori = False
    Layla_Week6_Monday_Spanish_OfferHelp = False
    LayLena = False
    Valeria_Week6_Monday_EmoDate = False
    Week6_Monday_BBQ_Invitation = False
    AlexisValeria = False
    Zach_Week6_Monday_Punch = False
    Adriana_Week6_Monday_DontTell = False
    Zach_Week6_Monday_BikeSuspect = False
    Brooke_Week6_Monday_ManagerPosition = False
    Iris_LikeMC = False
    Iris_Week6_Monday_Garage_Sex = False
    Iris_Week6_Monday_CheatKiss = False
    Andres_Week6_Monday_Hug = False
    Erynn_Week6_Monday_ReadLetter = False
    Erynn_Week6_Monday_WriteLetter = False
    MC_Week6_Monday_WinGame = False
    NikkiCara_Week6_Monday_MiraLie = False
    NikkiCara_Week6_Monday_MiraMention = False
    Riverside_MiraTruth = False
    Melissa_Week6_Monday_Compliment = False
    Melissa_LikeMC = False
    Melissa_Week6_Monday_Sex = False
    #Ep15
    Erynn_Week6_Tuesday_AlexisBreakupNotKnow = False
    Erynn_Week6_Tuesday_BJ = False
    Sienna_Week6_Tuesday_SexProposition = False
    Alexis_Week6_Tuesday_MSU_Help = False
    Alexis_Week6_Tuesday_MSU_Play = False
    Erynn_Week6_Tuesday_MSU_Paper = False
    Erynn_Week6_Tuesday_MSU_Note = False
    Alexis_Week6_Tuesday_MSU_Jealous = False
    Alexis_Week6_Tuesday_Fight = False
    Lakeyn_Week6_Tuesday_CheckOut = False
    Lakeyn_Week6_Tuesday_CatchUp = False
    Alexis_Week6_Tuesday_PreviousHookups = False
    Valeria_Week6_Tuesday_GeographyProject = False
    Emily_Week6_Tuesday_SlapAss = False
    Week6_Tuesday_Monroe_BBQ = False
    Layla_Week6_Tuesday_MonroeBBQ_1v1 = False
    Adriana_Week6_Tuesday_VeganJoke = False
    Valeria_Week6_Tuesday_EmoCancel = False
    Alexis_Week6_Tuesday_Phone_Ignore = False
    Adriana_Week6_Tuesday_ParkingKiss = False
    Adriana_Week6_Tuesday_ImagineBJ = False
    Alexis_Week6_Tuesday_Shower_CumFace = False
    Alexis_Week6_Tuesday_GoodGirl = False
    Adriana_Week6_Tuesday_PhoneNumber = False
    Valeria_Dating = False
    Valeria_End = False
    Valeria_Week6_Tuesday_EmoDate = False
    Valeria_Week6_Tuesday_LikeEmoLook = False
    Valeria_Week6_Tuesday_EmoHairCute = False
    Ximena_Week6_Tuesday_Cinema = False
    Ximena_Week6_Tuesday_FavouriteActress = False
    Ximena_Week6_Tuesday_GrabAss = False
    Ximena_Week6_Tuesday_Kiss = False
    Alexis_Week6_Tuesday_Break = False
    Sienna_Week6_Wednesday_Sex = False
    CaraNikki_Week6_Wednesday_BikiniShopping = False
    CaraNikki_Week6_Wednesday_SaturdayClub = False
    Nikki_Week6_Wednesday_CaraPicture = False
    Gabi_Week6_Wednesday_School_Ignore = False
    MC_Week6_Wednesday_School_Kiss = False
    Dani_Week6_Wednesday_Rumour = False
    Valeria_Week6_Wednesday_Spanish = False
    Tori_Week6_Wednesday_GrabAss = False
    Darryl_Week6_Wednesday_School_Confront = False
    Cara_Week6_Wednesday_Breakup = False
    Nikki_Week6_Wednesday_Breakup = False
    Riverside_Girlfriend = False
    NikkiCara_Week6_Wednesday_Breakup = False
    MC_Week6_Wednesday_RobIsYourNewBestFriend = False
    Tori_Week6_Wednesday_ShowerSex = False
    MC_Week6_Wednesday_OnTheList = False
    Nikki_Week6_Wednesday_School_Jealousy = False
    Nikki_Week6_Wednesday_LeggingsCameltoe = False
    Nikki_Week6_Wednesday_Goddess = False
    MC_Week6_Wednesday_Speedo = False
    Nikki_Week6_Wednesday_PullUpComp = False
    Ximena_Week6_Wednesday_Gabi_End = False
    Ximena_Week6_Wednesday_Valeria_Aunt = False
    Valeria_Week6_Wednesday_SolName = False
    Valeria_Week6_Wednesday_MomBadSide = False
    Valeria_Week6_Wednesday_KnowYoungMC = False
    Valeria_Week6_Wednesday_Shortcut = False
    #Ep16
    MC_Week6_Wednesday_EthanCrash_Call = False
    Erynn_Week6_Wednesday_TellEverything = False
    Erynn_Week6_Wednesday_StayOver = False
    MC_Week6_Wednesday_Dogs = False
    MC_Week6_Wednesday_Cats = False
    Erynn_Week6_Wednesday_StayOver_Past = False
    Erynn_Week6_Wednesday_StayOver_RightHere = False
    Erynn_Week6_Wednesday_StayOver_Mountains = False
    Iris_Week6_Thursday_Hospital_Kiss = False


#--------------various Mod variables---------------#
default KoGa3ModMenuButtonPressed = False
default KoGa3MainMenu = 0
default KoGa3ModStart = 0
default KoGa3DialogOptions = 1
default KoGa3QuickMenuOptions = 0
default KoGa3QuickMenuItems = 1
default KoGa3CheatButton = 1
default KoGa3CheatChapterButton = 1
default KoGa3ScreenStatsFull = 0
default KoGa3GameProgress = "n/a"
default KoGa3ChoiceOptions = 0
# default name = "Nico"

default KoGa3ChoiceOption = 1                                                   # for WT Mod
default KoGa3WTChange = "\n{color=#008000}"                                     # green
#default KoGa3WTChange1 = "\n{size=32}{color=#0000ff}"                          # blue
default KoGa3WTChange1 = "\n{color=#ffdf00}"                                    # yellow
default KoGa3WTChange2 = "\n{color=#ff0000}"                                    # red
#default KoGa3WTChange = "\n{size=1}{color=#363636}"                            # info: WT Off

default KoGa3AutoWTChange1 = "\n{color=#ffdf00}"                                # yellow, for fergzWT

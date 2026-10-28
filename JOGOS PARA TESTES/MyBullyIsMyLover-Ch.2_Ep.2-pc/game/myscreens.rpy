style points_nav_vbox:
    xalign 0.95
    yalign 0.43
    spacing 10


style char_nav_vbox:
    spacing 15

style char_info_grid:
    xalign 0.15
    yalign 0.15
    xspacing 5
    yspacing 5

style char_info2_vbox:
    xalign 0.3
    yalign 0.6

style menu_nav_grid:
    xalign 0.888
    yalign 0.5
    xspacing 10
    yspacing 10

style supp_nav_vbox:
    spacing 5

init python:
    def hide_all():
        renpy.hide_screen("aine")
        renpy.hide_screen("emma")
        renpy.hide_screen("gwen")
        renpy.hide_screen("lily")
        renpy.hide_screen("sky")
        renpy.hide_screen("klara")
        renpy.hide_screen("freya")
        renpy.hide_screen("naomi")
    def hide_aine():
        renpy.hide_screen("emma")
        renpy.hide_screen("gwen")
        renpy.hide_screen("lily")
        renpy.hide_screen("sky")
        renpy.hide_screen("klara")
        renpy.hide_screen("freya")
        renpy.hide_screen("naomi")
    def hide_emma():
        renpy.hide_screen("aine")
        renpy.hide_screen("gwen")
        renpy.hide_screen("lily")
        renpy.hide_screen("sky")
        renpy.hide_screen("klara")
        renpy.hide_screen("freya")
        renpy.hide_screen("naomi")
    def hide_gwen():
        renpy.hide_screen("emma")
        renpy.hide_screen("aine")
        renpy.hide_screen("lily")
        renpy.hide_screen("sky")
        renpy.hide_screen("klara")
        renpy.hide_screen("freya")
        renpy.hide_screen("naomi")
    def hide_lily():
        renpy.hide_screen("emma")
        renpy.hide_screen("gwen")
        renpy.hide_screen("aine")
        renpy.hide_screen("sky")
        renpy.hide_screen("klara")
        renpy.hide_screen("freya")
        renpy.hide_screen("naomi")
    def hide_sky():
        renpy.hide_screen("emma")
        renpy.hide_screen("gwen")
        renpy.hide_screen("lily")
        renpy.hide_screen("aine")
        renpy.hide_screen("klara")
        renpy.hide_screen("freya")
        renpy.hide_screen("naomi")
    def hide_klara():
        renpy.hide_screen("emma")
        renpy.hide_screen("gwen")
        renpy.hide_screen("lily")
        renpy.hide_screen("sky")
        renpy.hide_screen("aine")
        renpy.hide_screen("freya")
        renpy.hide_screen("naomi")
    def hide_freya():
        renpy.hide_screen("emma")
        renpy.hide_screen("gwen")
        renpy.hide_screen("lily")
        renpy.hide_screen("sky")
        renpy.hide_screen("aine")
        renpy.hide_screen("klara")
        renpy.hide_screen("naomi")
    def hide_naomi():
        renpy.hide_screen("emma")
        renpy.hide_screen("gwen")
        renpy.hide_screen("lily")
        renpy.hide_screen("sky")
        renpy.hide_screen("aine")
        renpy.hide_screen("klara")
        renpy.hide_screen("freya")

init -2:
    transform info_fade:
        alpha 0.0
        easein 1.0 alpha 1.0

screen showpoints():
    imagebutton auto "gui/button/menu_%s.png" xpos 1793 ypos 40 focus_mask True action [ShowMenu("show_spread")] idle "gui/button/menu_%s.png" hover "gui/button/menuh_%s.png" style "gallery_char_button"
screen showpoints2():
    imagebutton auto "gui/button/menuh_%s.png" xpos 1793 ypos 40 focus_mask True action [Return(), Hide("supporters"), Hide("charinfo"), hide_all] idle "gui/button/menuh_%s.png" style "gallery_char_button"

screen characters():
    textbutton ("Characters") xalign 0.85 yalign 0.8
screen discord():
    textbutton ("Discord") xalign 0.85 yalign 0.8
screen patreon():
    textbutton ("Patreon") xalign 0.85 yalign 0.8
screen pref():
    textbutton ("Preferences") xalign 0.85 yalign 0.8
screen rep():
    textbutton ("Scenes") xalign 0.85 yalign 0.8
screen supp():
    textbutton ("Supporters") xalign 0.85 yalign 0.8
screen gal():
    textbutton ("Gallery") xalign 0.85 yalign 0.8

screen rename():
    frame:
        xalign 0.5 ypos 50
        vbox:
            text _("Character Name:")
            input default "":
                pixel_width(500)
                value VariableInputValue("name")
            textbutton "{space=90}OK":
                action Jump("continued")
                keysym('K_RETURN', 'K_KP_ENTER')

label continued:
    $ name = name.strip()
    if name == "":
        $ name="Kei"

    hide screen rename


screen charinfo():
    imagebutton auto "gui/button/foreground_%s.png" idle "gui/button/foreground_%s.png"
    imagebutton auto "gui/button/ainecm_%s.png" focus_mask True action NullAction() idle "gui/button/ainecm_%s.png" hover "gui/button/ainehcm_%s.png" hovered [Show("aine"), Play("sound", "audio/switchclick.mp3")] unhovered Hide("aine")
    imagebutton auto "gui/button/emmacm_%s.png" focus_mask True action NullAction() idle "gui/button/emmacm_%s.png" hover "gui/button/emmahcm_%s.png" hovered [Show("emma"), Play("sound", "audio/switchclick.mp3")] unhovered Hide("emma")
    imagebutton auto "gui/button/gwencm_%s.png" focus_mask True action NullAction() idle "gui/button/gwencm_%s.png" hover "gui/button/gwenhcm_%s.png" hovered [Show("gwen"), Play("sound", "audio/switchclick.mp3")] unhovered Hide("gwen")
    imagebutton auto "gui/button/skycm_%s.png" focus_mask True action [ShowMenu("skyrelationship"), Play("sound", "audio/click.ogg")] idle "gui/button/skycm_%s.png" hover "gui/button/skyhcm_%s.png" hovered [Show("sky"), Play("sound", "audio/switchclick.mp3")] unhovered Hide("sky")
    imagebutton auto "gui/button/klaracm_%s.png" focus_mask True action [ShowMenu("klararelationship"), Play("sound", "audio/click.ogg")] idle "gui/button/klaracm_%s.png" hover "gui/button/klarahcm_%s.png" hovered [Show("klara"), Play("sound", "audio/switchclick.mp3")] unhovered Hide("klara")
    imagebutton auto "gui/button/lilycm_%s.png" focus_mask True action NullAction() idle "gui/button/lilycm_%s.png" hover "gui/button/lilyhcm_%s.png" hovered [Show("lily"), Play("sound", "audio/switchclick.mp3")] unhovered Hide("lily")
    imagebutton auto "gui/button/freyacm_%s.png" focus_mask True action NullAction() idle "gui/button/freyacm_%s.png" hover "gui/button/freyahcm_%s.png" hovered [Show("freya"), Play("sound", "audio/switchclick.mp3")] unhovered Hide("freya")
    imagebutton auto "gui/button/naomicm_%s.png" focus_mask True action NullAction() idle "gui/button/naomicm_%s.png" hover "gui/button/naomihcm_%s.png" hovered [Show("naomi"), Play("sound", "audio/switchclick.mp3")] unhovered Hide("naomi")
    imagebutton auto "gui/button/mooncm_%s.png" focus_mask True action NullAction() idle "gui/button/mooncm_%s.png" hover "gui/button/moonhcm_%s.png" hovered [Show("moon"), Play("sound", "audio/switchclick.mp3")] unhovered Hide("moon")

    imagebutton auto "gui/button/return_%s.png" xpos 30 ypos 970 focus_mask True action [Return(), Play("sound", "audio/click.ogg")] idle "gui/button/return_%s.png" hover "gui/button/returnh_%s.png" hovered Play("sound", "audio/switchclick.mp3")

screen aine():
    textbutton ("{font=Copperplate.ttf}[ainepoint]") xpos 135 ypos 709
    if aineroute:
        textbutton ("{font=Copperplate.ttf}Yes") xpos 130 ypos 787
    else:
        textbutton ("{font=Copperplate.ttf}No") xpos 130 ypos 787
screen emma():
    textbutton ("{font=Copperplate.ttf}[emmapoint]") xpos 354 ypos 709
    if emmaroute:
        textbutton ("{font=Copperplate.ttf}Yes") xpos 344 ypos 787
    else:
        textbutton ("{font=Copperplate.ttf}No") xpos 344 ypos 787
screen gwen():
    textbutton ("{font=Copperplate.ttf}[gwenpoint]") xpos 565 ypos 709
    if gwenroute:
        textbutton ("{font=Copperplate.ttf}Yes") xpos 557 ypos 787
    else:
        textbutton ("{font=Copperplate.ttf}No") xpos 557 ypos 787
screen sky():
    textbutton ("{font=Copperplate.ttf}[skypoint]") xpos 780 ypos 709
    if skyroute:
        textbutton ("{font=Copperplate.ttf}Yes") xpos 770 ypos 787
    else:
        textbutton ("{font=Copperplate.ttf}No") xpos 770 ypos 787
screen klara():
    textbutton ("{font=Copperplate.ttf}[klarapoint]") xpos 989 ypos 709
    if klararoute:
        textbutton ("{font=Copperplate.ttf}Yes") xpos 982 ypos 787
    else:
        textbutton ("{font=Copperplate.ttf}No") xpos 982 ypos 787
screen lily():
    textbutton ("{font=Copperplate.ttf}[lilypoint]") xpos 1207 ypos 709
    if lilyroute:
        textbutton ("{font=Copperplate.ttf}Yes") xpos 1198 ypos 787
    else:
        textbutton ("{font=Copperplate.ttf}No") xpos 1198 ypos 787
screen freya():
    textbutton ("{font=Copperplate.ttf}[freyapoint]") xpos 1425 ypos 709
    if freyaroute:
        textbutton ("{font=Copperplate.ttf}Yes") xpos 1415 ypos 787
    else:
        textbutton ("{font=Copperplate.ttf}No") xpos 1415 ypos 787
screen naomi():
    textbutton ("{font=Copperplate.ttf}[naomipoint]") xpos 1635 ypos 709
    if naomiroute:
        textbutton ("{font=Copperplate.ttf}Yes") xpos 1623 ypos 787
    else:
        textbutton ("{font=Copperplate.ttf}No") xpos 1623 ypos 787
screen moon():
    textbutton ("{font=Copperplate.ttf}[moonpoint]") xpos 1846 ypos 709
    if moonroute:
        textbutton ("{font=Copperplate.ttf}Yes") xpos 1836 ypos 787
    else:
        textbutton ("{font=Copperplate.ttf}No") xpos 1836 ypos 787

screen day_monday():
    imagebutton:
        idle "DayMonday.png"
        xalign .005
        yalign .01

screen day_tuesday():
    imagebutton:
        idle "DayTuesday.png"
        xalign .005
        yalign .01

screen day_wednesday():
    imagebutton:
        idle "DayWednesday.png"
        xalign .005
        yalign .01

screen day_thursday():
    imagebutton:
        idle "DayThursday.png"
        xalign .005
        yalign .01

screen day_friday():
    imagebutton:
        idle "DayFriday.png"
        xalign .005
        yalign .01

screen day_saturday():
    imagebutton:
        idle "DaySaturday.png"
        xalign .005
        yalign .01

screen day_sunday():
    imagebutton:
        idle "DaySunday.png"
        xalign .005
        yalign .01

label hide_days:
    hide screen day_monday
    hide screen day_tuesday
    hide screen day_wednesday
    hide screen day_thursday
    hide screen day_friday
    hide screen day_saturday
    hide screen day_sunday

style spread_list_button:
    xsize 360
    ysize 70
    left_padding 100
    right_padding 20
    top_padding 8
    bottom_padding 8
    background Frame("bin/assets/gallery/namebox.png", 12, 12)
    hover_background Frame("bin/assets/gallery/namebox.png", 12, 12)

style spread_list_button_text:
    font "bin/assets/faces/LaParisienne.otf"
    size 36
    color "#ffffff"
    outlines [(2, "#00000099", 0, 0)]
    text_align 0.0
    xalign 0.0
    yalign 0.5

transform spread_dim_in:
    subpixel True
    alpha 0.0
    ease .12 alpha 1.0

transform spread_name_in:
    subpixel True
    alpha 0.0
    xoffset 20
    easein_quart .20 alpha 1.0 xoffset 0

transform spread_list_anim(delay=0.0):
    subpixel True
    alpha 0.0
    xoffset 70
    matrixcolor BrightnessMatrix(0.0)

    pause delay
    easein_quart .25 alpha 1.0 xoffset 0

    on idle:
        easeout_quart .08 matrixcolor BrightnessMatrix(0.0) xoffset 0

    on hover:
        easeout_quart .08 matrixcolor BrightnessMatrix(.15) xoffset 14

screen show_spread():

    use showpoints2

    add Solid("#000000a4")

    fixed:
        xpos 1400
        ypos 50

        textbutton "{font=bin/assets/faces/LaParisienne.otf}{size=-5}Name: [mc]{/size}{/font}":
            xpos 130
            ypos 0
            at spread_list_anim(0.03)

        vbox:
            xpos 0
            ypos 70
            spacing 12

            textbutton "MC Rename":
                style "spread_list_button"
                text_style "spread_list_button_text"
                action [ShowMenu("rename"), Play("sound9", "audio/click.ogg")]
                hover_sound "audio/switchclick.mp3"
                at spread_list_anim(0.06)

            textbutton "Gallery":
                style "spread_list_button"
                text_style "spread_list_button_text"
                action [ui.callsinnewcontext("call_gallery"), Hide("show_spread"), ShowMenu("gallery"), Play("sound9", "audio/click.ogg")]
                hover_sound "audio/switchclick.mp3"
                at spread_list_anim(0.09)

            textbutton "Settings":
                style "spread_list_button"
                text_style "spread_list_button_text"
                action [ShowMenu("preferences"), Hide("show_spread"), Play("sound9", "audio/click.ogg")]
                hover_sound "audio/switchclick.mp3"
                at spread_list_anim(0.12)

            #textbutton "Supporters":
            #    style "spread_list_button"
            #    text_style "spread_list_button_text"
            #    action [Show("supporters"), Hide("show_spread"), Play("sound", "audio/click.ogg")]
            #    at spread_list_anim(0.12)

            textbutton "Discord":
                style "spread_list_button"
                text_style "spread_list_button_text"
                action [OpenURL("http://discord.gg/a3HZsV2"), Play("sound9", "audio/click.ogg")]
                hover_sound "audio/switchclick.mp3"
                at spread_list_anim(0.15)

            textbutton "Patreon":
                style "spread_list_button"
                text_style "spread_list_button_text"
                action [OpenURL("http://patreon.com/NiiChan029"), Play("sound9", "audio/click.ogg")]
                hover_sound "audio/switchclick.mp3"
                at spread_list_anim(0.18)

screen supporters():
    imagebutton auto "gui/button/suppboard_%s.png" xpos 1000 ypos 351 focus_mask True idle "gui/button/suppboard_%s.png" 
    imagebutton auto "gui/button/close_%s.png" xpos 1240 ypos 360 focus_mask True action [Hide("supporters"), Play("sound", "audio/click.ogg")] idle "gui/button/close_%s.png" hover "gui/button/closeh_%s.png"

    viewport:
        xalign 0.618 ypos 0.40 xysize (280, 350)

        scrollbars "vertical"
        spacing 5

        draggable True
        mousewheel True
        arrowkeys True

        vbox:
            style_prefix "supp_nav"
            text ("{size=-10}Staff:{/size}")
            text ("{size=-15}Pezzo\nOEJ\nAltimos\nMarkX\nKainan\nMidgar\nlonely neet\nElasstommer{/size}")
            text ("{size=-10}\n$100 Supporters:{/size}")
            text ("{size=-15}kainan\nkingkable300\nMarkX\nCorky{/size}")
            text ("{size=-10}\n$50 Supporters:{/size}")
            text ("{size=-15}Caribdis\nCodingPianist\ncplustry\nDayleen\nDwenneven\nL. Heelsmaster\nOEJ123{/size}")
            text ("{size=-10}\n$20 Supporters:{/size}")
            text ("{size=-15}Anders Brøndum\nBangNi\nBbean16\nBigGuy0729\nChris Logan\nCorey Smith\nDarrin Soo\nDavid Washington\nDCThePlayboy\ndorktron2006\nfainted.浪人\nFirebison\nhaitso\nJagage\nleo200076\nLyn\nMaple\nMcRnB\nMen Lin\nMercyNoNo\nMescalink\nMike2051\nmj\nNick Lehman\npoin\nSam\nShikujin\nSilverRook\nSoftDomForU\nStephan Legaard\nXesc\nYen Tsung Yen\nZeus Guzman\nZiyu Deng{/size}")
            text ("{size=-10}\n$10 Supporters:{/size}")
            text ("{size=-15}Aaron DuBose\nAksy Ptj\nAlean Chang\nAlexander Gibson\nAnthony Holder\nAntonio Bejarano \nB D\nbear54\nBjörn\nBRAD MENTZER\nBrice Delzangles\nCal Hughes\nCaprice Dhusara\nCarl Theobald\nchance mullins\nChris J Hogeweide\nCyberArsonist\ndap \nDeltor\nDisMel\nDominic Ross\nEDWARD A STEVENSON\nElderLichJoe\nElvin \nFictional Themepark\nFOG\nGanos \nGarret Adamson\nHalcyon\nHank Rockwell\nHaziq Ifwatt\nHermel Baloloy\nHighlorddefiler\nHunt\nitsmikeb\nJackson Krejci\nJames Kingsford\nJared \nJAYDE Greninija\nJef Campforts\nJosh\nJosh sapp\nKamaralyn\nKing\nKyle Thompson\nLilredexpress\nLink2626\nLord Rogue\nLusio\nmacrobe\nMaya Heart\nMsissy4\nNathen Drake\nNoah Lin\nPaul Boros\nPervector\nPhillip Cooper\nPie34\nRalph Cristobal\nRay Provencher (Razor McBlade)\nRaziel_Kaine92\nRedkiller7700\nRust\nrvau\nsean mahan\nSera Mochi\nSeymour Nuts\nShadow\nShardas\nSleepfishl\nSolstorm\nStephen Foster\nStephen Godfrey\nSteven Cox\nsteven walker\nStorm Walker\nTadxSarah\nTerje \nThe Darkness In You\nTim Lanham\ntim216\nTOCS4\nTyler Hoffman\nVrodHogrider\nWayne Stout\nWildo\nWL \nxXAlphAXx18\n宇傑 鄭{/size}")
            text ("{size=-15}\nAnd to all $5 and $1 supporters!{/size}")
            text ("{size=-10}\nThank you all so much for supporting me and my game! Words couldn't express how thankful I am for your support. I really appreciate it!\n\nAlso a huge credit to my friend {b}Elasstommer{/b} for the proof reading! You're a life saver my man!{/size}")


screen patreonpagepop:
    imagebutton:
        idle "gui/button/patreonpop.png"
        hover "gui/button/patreonpoph.png"
        hovered Play("sound", "audio/switchclick.mp3")
        action [OpenURL("http://patreon.com/NiiChan029"), Play("sound9", "audio/click.ogg")]
        xpos 520
        ypos 200
screen freeroam_help():
    hbox:
        xalign 0.99
        yalign 0.01

        textbutton "HELP" action [Show("freeroam_wt_help"), Hide("freeroam_help")] text_size 24 style "mod_text"

screen freeroam_wt_help():
    modal False

    frame:
        xsize 550
        ysize 700
        xalign 1.0
        yalign 0.0

        vbox:
            xfill True
            if livingfirst:
                text "Go to the Hall > Living Room." style "mod_text"
            elif gardenfirst:
                text "Go to the Garden." style "mod_text"
            elif bedroomfirst:
                text "Go to the Bedroom." style "mod_text"
            elif phonesurvival:
                text "Go the Corridor > Office." style "mod_text"
            elif safesurvival:
                text "Go to the Bedroom > Safe Room > Open the safe." style "mod_text"
            text ""
            text "Full quickest path: Hall > Living Room > Garden > Bedroom > Corridor > Office > Bedroom > Safe Room > Open the safe." style "mod_text"
            textbutton "Close" action [Hide("freeroam_wt_help"), Show("freeroam_help")] text_size 35 xpos(0.45)

style mod_text:
    size 25
    color "#FFFFFF" 
    outlines [ (absolute(2), "#000", absolute(1), absolute(1)) ]

screen freeroam_help2():
    zorder 99
    hbox:
        xalign 0.99
        yalign 0.01

        textbutton "HELP" action [Show("freeroam_wt_help2"), Hide("freeroam_help2")] text_size 24 style "mod_text"

screen freeroam_wt_help2():
    modal False
    zorder 99
    default show_full = False

    frame:
        xsize 550
        ysize 700
        xalign 1.0
        yalign 0.35

        vbox:
            style_prefix "mod"
            xfill True

            if not show_full:
                if crimehar1:
                    text "- Speak with Harley Jones (go right twice)"
                elif crimedoor1:
                    text "- Try opening the locked door on the left side of the corridor (go back, left)"
                elif eround == 1:
                    text "- Speak with Clonk - Vote"
                elif not crimekeyfirst and not crimekey:
                    text "- Inspect the reception"
                elif crimekeyfirst2:
                    text "- Go back to the locked room and open it"
                elif not crimegemage:
                    text "- Speak with Gemini (wheelchair)"
                elif not crimeharage:
                    text "- Speak with Harley Jones"
                elif eround == 2:
                    text "- Go Vote"
                elif not lastpostit:
                    text "- Go back to the locked room and open the briefcase"
                elif lastph:
                    text "- Speak with Harley Jones"
                elif crimebae2:
                    text "- Speak with sister Baek (outside)"
                else:
                    text "- Vote twice"

            if show_full:
                text "- Speak with Harley Jones (go right twice)"
                text "- Try opening the locked door on the left side of the corridor"
                text "- Speak with Clonk - Vote"
                text "- Inspect the reception"
                text "- Go back to the locked room and open it"
                text "- Speak with Gemini, Harley Jones, and go Vote"
                text "- Go back to the locked room and open the briefcase"
                text "- Speak with Harley Jones"
                text "- Speak with sister Baek (outside)"
                text "- Go Vote"
                text "- Vote again"

            null height 25
            if not show_full:
                textbutton "Full quickest path" action SetScreenVariable("show_full", True) text_size 35 xalign 0.5
            else:
                textbutton "Hide full path" action SetScreenVariable("show_full", False) text_size 35 xalign 0.5

            null height 25
            textbutton "Close" action [Hide("freeroam_wt_help2"), Show("freeroam_help2")] text_size 35 xalign 0.5


# Cheats

screen cheats():
    tag menu

    add "gallery/galleryback.jpg"
    style_prefix "cheats"

    vbox:
        # Paths
        xpos 0.05
        ypos 0.08

        if anniepath:
            textbutton "On Annie's path" action SetVariable("anniepath", False)
        else:
            textbutton "Not on Annie's path" action SetVariable("anniepath", True)

        if nancypath:
            textbutton "On Nancy's path" action SetVariable("nancypath", False)
        else:
            textbutton "Not on Nancy's path" action SetVariable("nancypath", True)

        if daliapath:
            textbutton "On Dalia's path" action SetVariable("daliapath", False)
        else:
            textbutton "Not on Dalia's path" action SetVariable("daliapath", True)

        if penelopepath:
            textbutton "On Penelope's path" action SetVariable("penelopepath", False)
        else:
            textbutton "Not on Penelope's path" action SetVariable("penelopepath", True)

        if lunapath:
            textbutton "On Luna's path" action SetVariable("lunapath", False)
        else:
            textbutton "Not on Luna's path" action SetVariable("lunapath", True)

        if alexpath:
            textbutton "On Alex's path" action SetVariable("alexpath", False)
        else:
            textbutton "Not on Alex's path" action SetVariable("alexpath", True)

        if novapath:
            textbutton "On Nova's path" action SetVariable("novapath", False)
        else:
            textbutton "Not on Nova's path" action SetVariable("novapath", True)

        if calypsopath:
            textbutton "On Calypso's path" action SetVariable("calypsopath", False)
        else:
            textbutton "Not on Calypso's path" action SetVariable("calypsopath", True)

        if harempath:
            textbutton "On Harem path" action SetVariable("harempath", False)
        else:
            textbutton "Not on Harem path" action SetVariable("harempath", True)

        textbutton "Eternals" action NullAction()

        if pregnancy:
            textbutton "Pregnancy enabled" action SetVariable("pregnancy", False)
        else:
            textbutton "Pregnancy disabled" action SetVariable("pregnancy", True)

        if not amuletofblair:
            textbutton "Didn't take Amulet {image=/mod_additions/check_mark.webp}" action SetVariable("amuletofblair", True)
        else:
            textbutton "Took Amulet" action SetVariable("amuletofblair", False)

        if vasilhelp:
            textbutton "Helped Vasil get an egg" action SetVariable("vasilhelp", False)
        elif not vasilhelp:
            textbutton "Helped Commander Hasler place the bomb" action [SetVariable("vasilhelp", True), SetVariable("freemercer", True)]

        null height 50

        textbutton "Change first/last name" action ui.callsinnewcontext("mod_name_change")

    text "Points" xpos 588 ypos 0.03

    vbox:
        # Points
        xpos 0.3
        ypos 0.08
        spacing -3
        style_prefix "cheats_points"

        hbox:
            textbutton "-" action SetVariable("annie_points", annie_points-1)
            text "[annie_points]"
            textbutton "+" action SetVariable("annie_points", annie_points+1)

            null width 50
            if chopchop == 3:
                textbutton "Pendant {image=/mod_additions/check_mark.webp}" action SetVariable("chopchop", 1) text_size 40 text_font "poiretone.ttf"
            else:
                textbutton "{s}Pendant" action SetVariable("chopchop", 3) text_size 40 text_font "poiretone.ttf"

        hbox:
            textbutton "-" action SetVariable("nancy_points", nancy_points-1)
            text "[nancy_points]"
            textbutton "+" action SetVariable("nancy_points", nancy_points+1)

            null width 50
            if nancymommy:
                textbutton "Mommy" action SetVariable("nancymommy", False) text_size 40 text_font "poiretone.ttf"
            else:
                textbutton "{s}Mommy" action SetVariable("nancymommy", True) text_size 40 text_font "poiretone.ttf"

        hbox:
            textbutton "-" action SetVariable("dalia_points", dalia_points-1)
            text "[dalia_points]"
            textbutton "+" action SetVariable("dalia_points", dalia_points+1)

        hbox:
            textbutton "-" action SetVariable("penelope_points", penelope_points-1)
            text "[penelope_points]"
            textbutton "+" action SetVariable("penelope_points", penelope_points+1)

            null width 50
            if grimoirerest:
                textbutton "Restoration {image=/mod_additions/check_mark.webp}" action [SetVariable("grimoirerest", False), SetVariable("grimoiredest", True)] text_size 40 text_font "poiretone.ttf"
            else:
                textbutton "{s}Restoration" action [SetVariable("grimoirerest", True), SetVariable("grimoiredest", False)] text_size 40 text_font "poiretone.ttf"

        hbox:
            textbutton "-" action SetVariable("luna_points", luna_points-1)
            text "[luna_points]"
            textbutton "+" action SetVariable("luna_points", luna_points+1)

        hbox:
            textbutton "-" action SetVariable("alex_points", alex_points-1)
            text "[alex_points]"
            textbutton "+" action SetVariable("alex_points", alex_points+1)

        hbox:
            textbutton "-" action SetVariable("nova_points", nova_points-1)
            text "[nova_points]"
            textbutton "+" action SetVariable("nova_points", nova_points+1)

        hbox:
            if calypso_points > 0:
                textbutton "-" action SetVariable("calypso_points", calypso_points-1)
                text "[calypso_points]"
                textbutton "+" action SetVariable("calypso_points", calypso_points+1)
            else:
                textbutton "-" action SetVariable("calypso_interest", calypso_interest-1)
                text "[calypso_interest]"
                textbutton "+" action SetVariable("calypso_interest", calypso_interest+1)

        null height 70

        hbox:
            textbutton "-" action SetVariable("money", money-100)
            text "[money]"
            textbutton "+" action SetVariable("money", money+100)





    textbutton "Back" action ShowMenu("point") xalign 0.5 ypos 0.92

    textbutton "To game" action Return() xpos 0.7 ypos 0.92

style cheats_points_text:
    size 40
    font "poiretone.ttf"
    yalign 0.2
    xalign 0.5

style cheats_points_button_text:
    size 50
    yalign 0.0
    font "ade1.ttf"

style cheats_points_hbox:
    spacing 10

label mod_name_change:
    scene galleryback
    $ mc = renpy.input("What is your name? (Default: Orion)", exclude='\\[{')
    $ mc = mc.title()
    $ mc = mc.strip()
    if mc == "":
        $ mc = "Orion"
    if mc == "Alex":
        "{i}Be aware! There's another important character with this name in the game! Consider choosing another one."
    if mc == "Jerry":
        "{i}Be aware! There's another important character with this name in the game! Consider choosing another one."
    if mc == "Benjamin":
        "{i}Be aware! There's another important character with this name in the game! Consider choosing another one."
    if mc == "William":
        "{i}Be aware! There's another important character with this name in the game! Consider choosing another one."
    $ lastname = renpy.input("What is your last name? (Default: Richards)", exclude='\\[{')
    $ lastname = lastname.title()
    if lastname == "":
        $ lastname = "Richards"
    $ namelong = mc[-1]*5
    return


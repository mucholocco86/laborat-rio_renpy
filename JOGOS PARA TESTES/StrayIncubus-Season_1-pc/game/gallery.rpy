default mc_name = "Zycris"
default callmommy = 0
label gallery:
    $ galleryevents = [
    #0     #1                   #2              #3
    ["C2", "G0",                "cat_extra_iru",          2 ], #0
    ["C2", "G1",                "g_1",       persistent.g_1to3_unlock], #1
    ["C2", "kidnapped",         "g_2",       persistent.g_1to3_unlock], #2
    ["C2", "G3",                "g_3",       persistent.g_1to3_unlock], #3
    ["C3", "G4",                "g_4",       persistent.g_4_unlock], #4
    ["C3", "G5",                "g_5",       persistent.g_5_unlock], #5
    ["C3", "G6",                "g_6",       persistent.g_6_unlock], #6
    ["C3", "torr_scene",        "g_7",       persistent.g_7_unlock], #7
    ["C3", "nixie_scene",       "g_8",       persistent.g_8_unlock], #8
    ["C4", "torr_hj_scene",     "g_9",       persistent.g_9_unlock], #9
    ["C4", "maidens_scene_1",   "g_10",      persistent.g_10_unlock], #10
    ["C4", "maidens_scene_2",   "g_11",      persistent.g_11_unlock], #11
    ["C5", "G12",               "g_12",      persistent.g_12_unlock], #12
    ["C5", "G13",               "g_13",      persistent.g_13_unlock], #13
    ["C5", "G14",               "g_14",      persistent.g_14_unlock], #14
    ["C5", "G15",               "g_15",      persistent.g_15_unlock], #15
    ["C5", "G16",               "g_16",      persistent.g_16_unlock], #16
    ["C5", "G17",               "g_17",      persistent.g_17_unlock], #17
    ["C6", "G18",               "g_18",      persistent.g_18_unlock], #18
    ["C6", "G19",               "g_19",      persistent.g_19_unlock], #19
    ["C6", "G20",               "g_20",      persistent.g_20_unlock], #20
    ["C6", "G21",               "g_21",      persistent.g_21_unlock], #21
    ["C7", "G22",               "g_22",      persistent.g_22_unlock], #22
    ["C7", "G23",               "g_23",      persistent.g_23_unlock], #23
    ["C7", "G24",               "g_24",      persistent.g_24_unlock], #24
    ["C7", "G25",               "g_25",      persistent.g_25_unlock], #25
    ["C7", "G26",               "g_26",      persistent.g_26_unlock], #26
    ["C8", "G27",               "g_27",      persistent.g_27_unlock], #27
    ["C8", "G28",               "g_28",      persistent.g_28_unlock], #28
    ["C8", "G29",               "g_29",      persistent.g_29_unlock], #29
    ["C8", "G30",               "g_30",      persistent.g_30_unlock], #30
    ["C9", "G31",               "g_31",      persistent.g_31_unlock], #31
    ["C9", "G32",               "g_32",      persistent.g_32_unlock], #32
    ["C9", "G33",               "g_33",      persistent.g_33_unlock], #33
    ["C10","G34",               "g_34",      persistent.g_34_unlock], #34
    ["C10","G35",               "g_35",      persistent.g_35_unlock], #35
    ["C10","G36",               "g_36",      persistent.g_36_unlock], #36
    ["C10","G37",               "g_37",      persistent.g_37_unlock], #37
    ["C10","G38",               "g_38",      persistent.g_38_unlock], #38
    ["C10","G39",               "g_39",      persistent.g_39_unlock], #39
    ["C11","G40",               "g_40",      persistent.g_40_unlock], #40
    ["C11","G41",               "g_41",      persistent.g_41_unlock], #41
    ["C11","G42",               "g_42",      persistent.g_42_unlock], #42
    ["C11","G43",               "g_43",      persistent.g_43_unlock], #43
    ["C11","G44",               "g_44",      persistent.g_44_unlock], #44
    ["C11","G45",               "g_45",      persistent.g_45_unlock], #45
    ["C11","G46",               "g_46",      persistent.g_46_unlock], #46
    ["C11","G47",               "g_47",      persistent.g_47_unlock], #47
    ["C11","G48",               "g_48",      persistent.g_48_unlock], #48
    ["C11","G49",               "g_49",      persistent.g_49_unlock], #49
    ]
    scene black
    if persistent.g_1to3_unlock == 1:
        $ renpy.mark_label_seen("G1")
        $ renpy.mark_label_seen("G3")
    if persistent.g_4_unlock == 1:
        $ renpy.mark_label_seen("G4")
    if persistent.g_5_unlock == 1:
        $ renpy.mark_label_seen("G5")
    if persistent.g_6_unlock == 1:
        $ renpy.mark_label_seen("G6")
    call screen replaygalleryv2()
    return

screen replaygalleryv2():
    add "others/wood.png"
    textbutton "BACK":
        action [Hide("replaygallery2"), Return()]
        xalign 0.95
        yalign 0.25
        text_size 60
        text_outlines [ (absolute(2), "#000000", absolute(0), absolute(0)) ]
    if callmommy == 1:
        textbutton "Mommy Roleplay On":
            action SetVariable("callmommy", 0)
            xalign 0.95
            yalign 0.7
            text_size 30
            text_outlines [ (absolute(2), "#000000", absolute(0), absolute(0)) ]
    if callmommy == 0:
        textbutton "Mommy Roleplay Off":
            action SetVariable("callmommy", 1)
            xalign 0.95
            yalign 0.7
            text_size 30
            text_outlines [ (absolute(2), "#000000", absolute(0), absolute(0)) ]
    use rgalgrit()
    vbar value YScrollValue("vp") xpos 0.0
    if Unlockcounter >= 10:
        if not Unlockcheat:
            textbutton "Unlock":
                xalign 0.95
                yalign 0.85
                text_size 60
                text_color "#ff0000"
                text_outlines [ (absolute(2), "#000000", absolute(0), absolute(0)) ]
                action ToggleVariable("Unlockcheat")
        else:
            textbutton "Lock":
                xalign 0.95
                yalign 0.85
                text_size 60
                text_outlines [ (absolute(2), "#000000", absolute(0), absolute(0)) ]
                action ToggleVariable("Unlockcheat")
screen rgalgrit():
    vpgrid id "vp":
        xsize 1600
        ysize 980
        xpos 50
        ypos 50
        cols 3
        xspacing 125
        yspacing 34
        mousewheel True
        pagekeys True
        #scrollbars "vertical"
        for e in galleryevents:
            if e[3] == 2:
                imagebutton:
                    idle ("cat_extra_iru")
                    action SetVariable("Unlockcounter", Unlockcounter+1)
            else:
                if Unlockcheat:
                    imagebutton:
                        idle ("{}_l".format(e[2]))
                        hover ("{}".format(e[2]))
                        action Replay("{}".format(e[1]), scope={"came_from_gallery": 1,"calling_serena_mommy": callmommy, "calling_s_mom": callmommy}, locked=False )
                else:
                    if e[3] == 1:
                        imagebutton:
                            idle ("{}_l".format(e[2]))
                            hover ("{}".format(e[2]))
                            action Replay("{}".format(e[1]), scope={"came_from_gallery": 1, "calling_serena_mommy": callmommy, "calling_s_mom": callmommy})
                    else:
                        imagebutton:
                            idle ("{}_l1".format(e[2]))
                            action NullAction()

default Unlockcounter = 0
default Unlockcheat = False

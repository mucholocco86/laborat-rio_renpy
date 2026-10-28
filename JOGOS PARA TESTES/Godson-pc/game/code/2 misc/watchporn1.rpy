label watchporn:

    label video1:
        $ renpy.block_rollback()
        $ cum_hovered = False
        $ cam_hovered = False
        $ sex_hovered = False
        $ sexy_hovered = False

        scene porn1
        with ffastfade
        call screen vid2buttons

    label video2:
        $ renpy.block_rollback()
        $ cum_hovered = False
        $ cam_hovered = False
        $ sex_hovered = False
        $ sexy_hovered = False

        scene porn2
        with ffastfade
        call screen vid2buttons

    label video3:
        $ renpy.block_rollback()
        $ cum_hovered = False
        $ cam_hovered = False
        $ sex_hovered = False
        $ sexy_hovered = False

        scene porn3
        with ffastfade
        call screen vid2buttons


    screen vid2buttons:

        imagebutton:
            idle "gui/redarrow.png"
            hover "gui/redarrow_hover.png"
            action [Jump("room224"), SetVariable('cum_hovered', False)]
            hovered [SetVariable('cum_hovered', True)]
            unhovered [SetVariable('cum_hovered', False)]
            xpos 150 ypos 1700
        if cum_hovered:
            text " Go Back" xpos 400 ypos 1750 font "fonts/nexa-bold.otf" outlines [ (absolute(3), "#000", absolute(1), absolute(1)) ]

        imagebutton:
            idle "gui/videoicon1.png"
            hover "gui/videoicon1hovered.png"
            action [Jump("video1"), SetVariable('cam_hovered', False)]
            hovered [SetVariable('cam_hovered', True)]
            unhovered [SetVariable('cam_hovered', False)]
            xpos 165 ypos 1400
        if cam_hovered:
            text "  Video 1" xpos 400 ypos 1470 font "fonts/nexa-bold.otf" outlines [ (absolute(3), "#000", absolute(1), absolute(1)) ]


        imagebutton:
            idle "gui/videoicon1.png"
            hover "gui/videoicon1hovered.png"
            action [Jump("video2"), SetVariable('sex_hovered', False)]
            hovered [SetVariable('sex_hovered', True)]
            unhovered [SetVariable('sex_hovered', False)]
            xpos 170 ypos 1100
        if sex_hovered:
            text "  Video 2" xpos 400 ypos 1200 font "fonts/nexa-bold.otf" outlines [ (absolute(3), "#000", absolute(1), absolute(1)) ]


        imagebutton:
            idle "gui/videoicon1.png"
            hover "gui/videoicon1hovered.png"
            action [Jump("video3"), SetVariable('sexy_hovered', False)]
            hovered [SetVariable('sexy_hovered', True)]
            unhovered [SetVariable('sexy_hovered', False)]
            xpos 170 ypos 800
        if sexy_hovered:
            text "  Video 3" xpos 400 ypos 900 font "fonts/nexa-bold.otf" outlines [ (absolute(3), "#000", absolute(1), absolute(1)) ]
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

screen map_screen:
    tag map_screen
    modal False

    if persistent.map_fast_travel and map_fast_travel_enabled and len(map_system_list)>0:
        imagebutton:
            idle "map_button_proximity_idle"
            hover "map_button_proximity_hover"
            action Show("map_minimap_screen")
            xalign 0.994
            yalign 0.998
            yoffset 9 * persistent.scale_factor
            xoffset 1 * persistent.scale_factor

        imagebutton:
            idle "map_button_idle"
            hover "map_button_hover"
            action Show("map_minimap_screen")
            xalign 0.98
            yalign 0.98

screen map_minimap_screen:
    tag map_minimap_screen
    modal True
    add "map_transparent_bg"
    imagebutton:
        idle "map_transparent_button"
        hover "map_transparent_button"
        action Hide("map_minimap_screen")
        xalign 0.5
        yalign 0.5

    vpgrid:
        yfill True
        xsize 0.224
        xalign 1.0
        xmaximum 300 * persistent.scale_factor
        xminimum 300 * persistent.scale_factor
        ypos 0
        cols 1
        spacing 0
        draggable False
        mousewheel True

        scrollbars "vertical"
        side_xalign 0.502

        for x in range(0,len(map_system_list)):
            vbox:
                imagebutton at map_system_zoom:
                    idle map_system_list[x][0]
                    hover map_system_list[x][0]
                    if freeRoamID == "ep9_1" or freeRoamID == "ep9_2" or freeRoamID == "ep9_4" or freeRoamID == "ep11_4" or freeRoamID == "ep11_4b" or freeRoamID == "ep11_4c" or freeRoamID == "ep12_3":
                        action (Hide("newmoneymsg"),Hide("dance_filter_screen"),Hide("map_minimap_screen"),Jump(map_system_list[x][1]))
                    elif freeRoamID == "ep11_2":
                        action (Hide("newmoneymsg"),Function(fadeSFX2),Hide("map_minimap_screen"),Jump(map_system_list[x][1]))
                    else:
                        action (Hide("newmoneymsg"),Hide("map_minimap_screen"),Jump(map_system_list[x][1]))
                    xalign 0.5
                    yalign 0.5
                text "%s" % map_system_list[x][2] xalign 0.5 yalign 0.5 style "map_system_text_style"
style map_system_text_style:
    font "fonts/candara.ttf"
    color "#ffffff"
    size 30 * persistent.scale_factor
    outlines [(1, "#000000", 0, 0)]
    hover_outlines [(1, "#000000", 0, 0)]

transform map_system_zoom:
    zoom 0.15

screen map_tutorial_screen:
    tag map_tutorial_screen
    modal True
    imagebutton:
        idle "map_tutorial_screen_button"
        hover "map_tutorial_screen_button"
        action Hide("map_tutorial_screen")

screen map_screen_notification:
    tag map_screen_notification
    modal False
    timer 2 action Hide("map_screen_notification")

    imagebutton:
        idle "map_button_hover"
        hover "map_button_hover"
        action NullAction()
        xalign 0.98
        yalign 0.98
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

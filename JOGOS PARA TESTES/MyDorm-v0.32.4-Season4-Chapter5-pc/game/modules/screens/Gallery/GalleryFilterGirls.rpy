screen GalleryFilterGirls():
    modal True

    python:
        focus = get_focus_rect ()

    frame:
        background None
        align (0.5, 0.5)
        xysize (1.0, 1.0)
        pos (0.5, 0.5)
        button:
            xysize (1.0, 1.0)
            keysym "game_menu"
            action Hide ("GalleryFilterGirls")
    frame:
        background Solid ("#000000aa")
        # Position the frame at mouse pointer position
        #pos (renpy.get_mouse_pos ()[0] - 10, renpy.get_mouse_pos ()[1] + 20)
        pos (focus ["x"], focus ["y"] + focus ["height"])
        xsize (focus ["width"])
        padding (10, 5, 10, 5)
        ymaximum 900
        vpgrid:
            cols 1
            mousewheel True
            draggable True
            xfill True
            vbox:
                xfill True
                button:
                    xsize 1.0
                    padding (5, 5)
                    selected_background Solid ("02ffbf66")
                    hover_background Solid ("ffffff66")
                    text _("All")
                    action [ SetVariable ("gallery_girl_filter", "All"), Hide ("GalleryFilterGirls") ]

                # Sort the dictionary by translated value
                for filter_item in sorted (
                    list (
                        set (
                            [ x for n in (item ["girls"] for item in gallery_items) for x in n ]
                        )
                    )
                ):
                    button:
                        xsize 1.0
                        padding (5, 2)
                        selected_background Solid ("02ffbf66")
                        hover_background Solid ("ffffff66")
                        text _(filter_item.capitalize ())
                        action [ SetVariable ("gallery_girl_filter", filter_item), Hide ("GalleryFilterGirls") ]
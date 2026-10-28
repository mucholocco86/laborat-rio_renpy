screen GalleryContent():
    tag menuScreen
    python:
        marginLeft = getScreenDim (MenuScreenLeft)
        marginTop = getScreenDim (MenuScreenTop, False)
        marginRight = getScreenDim (MenuScreenRight)
        marginBottom = getScreenDim (MenuScreenBottom, False)
        slotMarginVertical = int (marginLeft * config.screen_height) * 2
        slotMarginHorizontal = slotMarginVertical * 2
    vpgrid style "MenuVPGrid":
        cols 4
        margin (marginLeft * 2, 10, marginRight * 2, 10)
        pos (marginLeft, marginTop)
        scrollbars "vertical"
        draggable True
        mousewheel True
        xspacing slotMarginHorizontal
        yspacing slotMarginVertical
        xysize (1.0 - marginLeft - marginRight, 1.0 - marginTop - marginBottom)
        yfill True
        for gallery_item in gallery_items:
            if (
                (
                    gallery_girl_filter in gallery_item ["girls"] or
                    gallery_girl_filter == "All"
                )
                and
                (
                    gallery_kink_filter in gallery_item ["kinks"] or
                    gallery_kink_filter == "All"
                )
            ):
                button style "GameSaveLoadFileSlotsButton":
                    if renpy.seen_label (gallery_item ["label"]) or persistent.gallery_unlocked:
                        add Transform (gallery_item ["image"], xysize = (384, 216))
                        action Replay (gallery_item ["label"], locked = False, scope = replay_scope)
                    else:
                        add Transform (gallery_item ["image"], xysize = (384, 216), blur = 20)  # increase or decrease to make the image more or less recognizable
                        action NullAction ()
                    frame style "GameSaveLoadFileSlotFrame":
                        text gallery_item ["title"] style "TextSmallCentered"

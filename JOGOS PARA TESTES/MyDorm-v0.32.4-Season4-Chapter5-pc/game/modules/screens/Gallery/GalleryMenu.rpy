screen GalleryMenu ():
    tag subMenu
    python:
        menuMarginX = getScreenDim (0.025)
        menuMarginY = getScreenDim (0.025, False)
        menuSpacing = menuMarginX * getSmallerScreenDimension ()
    frame style "MenuScreenButtonsFrame":
        pos (1.0 - menuMarginX, menuMarginY)
        hbox:
            spacing menuSpacing
            use MenuButton (
                (
                    _("Desbloqueada")
                    if persistent.gallery_unlocked else
                    _("Bloqueada")
                ),
                "Unhide" if persistent.gallery_unlocked else "Hide",
                [
                    ToggleField (
                        persistent,
                        "gallery_unlocked",
                        true_value = True,
                        false_value = False
                    )
                ]
            )

            use MenuButton (
                _("{color=#02ffbf}Chicas:{/color} [gallery_girl_filter!tc]"),
                "Family",
                [ Show ("GalleryFilterGirls") ],
                True
            )

            use MenuButton (
                _("{color=#02ffbf}Fetiches:{/color} [gallery_kink_filter!tc]"),
                "Gallery",
                [ Show ("GalleryFilterKinks") ],
                True
            )

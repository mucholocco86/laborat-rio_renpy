screen History ():
    tag menu
    use MenuBackground ()
    use ModalScreen ()
    use ScreenBackground ()
    use Menu ()
    use MenuTitle (_("Historia"))
    python:
        marginLeft = getScreenDim (MenuScreenLeft)
        marginTop = getScreenDim (MenuScreenTop, False)
        marginRight = getScreenDim (MenuScreenRight)
        marginBottom = getScreenDim (MenuScreenBottom, False)
    vpgrid style "MenuVPGrid":
        cols 1
        margin (marginLeft * 2, 0, marginRight * 2)
        pos (marginLeft, marginTop)
        xspacing MenuGridSpacing
        yspacing MenuGridSpacing * 2
        xysize (1.0 - marginLeft - marginRight, 1.0 - marginTop - marginBottom)
        mousewheel True
        scrollbars "vertical"
        yinitial 1.0
        vbox:
            if not _history_list:
                text _("La historia del diálogo está vacía.")
            else:
                $ previousWho = ""
                for dialogue in _history_list:
                    vbox:
                        if dialogue.who:
                            if dialogue.who != previousWho:
                                $ previousWho = dialogue.who
                                label dialogue.who style "HistoryLabel":
                                    if "color" in dialogue.who_args:
                                        text_color dialogue.who_args ["color"]
                            else:
                                null height int (MenuLabelTextSize / 2)
                        text dialogue.what style "MenuText"
                null height MenuLabelTextSize * 2
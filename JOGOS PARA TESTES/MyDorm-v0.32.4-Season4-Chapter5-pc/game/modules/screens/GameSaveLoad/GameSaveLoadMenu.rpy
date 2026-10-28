screen GameSaveLoadMenu (saveOrLoad="save"):
    python:
        numberOfSavePages = 10
        menuMarginX = getScreenDim (MenuScreenLeft)
        menuMarginY = getScreenDim (0.025, False)
        menuSpacing = menuMarginX * getSmallerScreenDimension ()
        buttons = []
        currentPage = FileCurrentPage ()
        if currentPage not in ("auto", "quick") and int (currentPage) - 10 > 0:
            buttons.append ([ "\u2906", "", [ FilePage (int (currentPage) - 10) ], True ])
        if currentPage in ("auto", "quick"):
            buttons.append ([ "\u2906", "", [ FilePage (1) ], True ])
        buttons.append ([ "\u21e6", "", [ FilePagePrevious () ], True ])
        # if saveOrLoad in ("load", "import"):
        #     buttons.append ([ "Part 1", "", [ Show ("GameImport") ], True ])
        if config.has_autosave:
            buttons.append ([ _("{#auto_page}A"), "", [ FilePage ("auto") ], True ])
        if config.has_quicksave:
            buttons.append ([ _("{#quick_page}Q"), "", [ FilePage ("quick") ], True ])
        pageFromToCheck = currentPage in ("auto", "quick") or int (currentPage) < 8
        fromPage = 1 if pageFromToCheck else int (currentPage) - 7
        toPage = numberOfSavePages + 1 if pageFromToCheck else int (currentPage) + 3
        for page in range (fromPage, toPage):
            buttons.append ([ str (page), "", [ FilePage (page) ], True ])
        buttons.append ([ "\u21e8", "", [ FilePageNext () ], True ])
        if currentPage not in ("auto", "quick"):
            buttons.append ([ "\u2907", "", [ FilePage (int (currentPage) + 10) ], True ])
        else:
            buttons.append ([ "\u2907", "", [ FilePage (10) ], True ])
    frame style "MenuScreenButtonsFrame":
        pos (1.0 - menuMarginX, menuMarginY)
        hbox:
            spacing menuSpacing
            for (buttonLabel, buttonIcon, buttonAction, buttonTrigger) in buttons:
                python:
                    isActive = (
                        str (currentPage) == str (buttonLabel)
                        or
                        currentPage == "auto" and buttonLabel == _("{#auto_page}A")
                        or
                        currentPage == "quick" and buttonLabel == _("{#quick_page}Q")
                    )
                use MenuButton (buttonLabel, buttonIcon, buttonAction, buttonTrigger, showButtonText = True, isSquare = True, isActive = isActive)
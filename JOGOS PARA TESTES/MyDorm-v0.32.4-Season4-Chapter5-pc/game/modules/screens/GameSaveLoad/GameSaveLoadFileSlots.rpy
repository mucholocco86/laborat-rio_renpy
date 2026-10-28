screen GameSaveLoadFileSlots (saveOrLoad="save"):
# FilePageNameInputValue (pattern="Page {}", auto="Automatic saves", quick="Quick saves")
    python:
        clickToSave = _("haz clic para guardar")
        emptyName = _("ranura vacía")
        emptySaveName = clickToSave if saveOrLoad == "save" else emptyName
        marginLeft = getScreenDim (MenuScreenLeft)
        marginTop = getScreenDim (MenuScreenTop, False)
        marginRight = getScreenDim (MenuScreenRight)
        marginBottom = getScreenDim (MenuScreenBottom, False)
        slotMarginVertical = int (marginLeft * config.screen_height) * 2
        slotMarginHorizontal = slotMarginVertical * 2
    frame:
        background None
        margin (marginLeft, marginTop, marginRight, marginBottom)
        xysize (1.0, 1.0)
        vbox:
            anchor (0.5, 0.5)
            pos (0.5, 0.5)
            spacing slotMarginVertical
            $ slotIndex = 0
            for slotIndexRow in range (3):
                hbox:
                    spacing slotMarginHorizontal
                    for slotIndexCol in range (4):
                        python:
                            slotIndex += 1
                            # slotIndexName = "part2-" + str (slotIndex)
                            slotName = FileTime (slotIndex, format="{#file_time}%B %d %Y, %H:%M", empty=emptySaveName)
                            fileSaveName = FileSaveName (slotIndex)
                            newestSave = FileNewest (slotIndex)
                            if saveOrLoad == "save":
                                buttonAction = FileSave (slotIndex)
                            elif not slotName == emptyName:
                                buttonAction = FileLoad (slotIndex)
                            else:
                                buttonAction = NullAction ()
                        vbox:
                            button style "GameSaveLoadFileSlotsButton":
                                action [ buttonAction ]
                                add FileScreenshot (slotIndex) xalign 0.5
                                frame style "GameSaveLoadFileSlotFrame":
                                    vbox xanchor 0.5 xpos 0.5 xalign 0.5:
                                        text slotName style "TextSmall" + ("Highlight" if newestSave else "")
                                        if fileSaveName:
                                            text fileSaveName style "TextSmallCentered" + ("Highlight" if newestSave else "")
                                if saveOrLoad == "save" and not slotName == emptySaveName:
                                    frame style "GameSaveLoadFileSlotEditFrame":
                                        button:
                                            action [ If (saveOrLoad == "save", true = ShowMenu ("GameSaveName", slotIndex = slotIndex, frameMargin = slotMarginVertical), false = FileSave (slotIndex)) ]
                                            text "\u270F"
                                    frame style "GameSaveLoadFileSlotDeleteFrame":
                                        button:
                                            action [ If (saveOrLoad == "save", true = ShowMenu ("GameSaveDelete", slotIndex = slotIndex, frameMargin = slotMarginVertical), false = FileSave (slotIndex)) ]
                                            text "\u2715"

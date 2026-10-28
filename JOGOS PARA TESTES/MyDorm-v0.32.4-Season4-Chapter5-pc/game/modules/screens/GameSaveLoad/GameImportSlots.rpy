init python:
    def sortBySlotMTime (slotItem):
        return renpy.slot_mtime (slotItem)

screen GameImportSlots (saveOrLoad="save"):
# FilePageNameInputValue (pattern="Page {}", auto="Automatic saves", quick="Quick saves")
    python:
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
            vpgrid:
                xspacing 20
                yspacing 20
                cols 4
                draggable True
                mousewheel True
                scrollbars "vertical"
                xalign 0.5
                python:
                    loopIndex = 0
                    saveSlotList = renpy.list_slots (regexp="^part1-")
                for saveGameData in sorted (saveSlotList, key=sortBySlotMTime):
                    $ loopIndex += 1
                    python:
                        slotTime = renpy.time.strftime ("%B %d %Y, %H:%M", renpy.time.localtime (renpy.slot_mtime (saveGameData)))
                        slotImage = renpy.slot_screenshot (saveGameData)
                        fileSaveName = renpy.slot_json (saveGameData) ["_save_name"]
                    hbox:
                        button style "GameSaveLoadFileSlotsButton":
                            action [ Function (renpy.load, saveGameData) ]
                            add slotImage xalign 0.5
                            frame style "GameSaveLoadFileSlotFrame":
                                vbox xanchor 0.5 xpos 0.5 xalign 0.5:
                                    text str (slotTime) style "TextSmallCentered"
                                    text str (fileSaveName) style "TextSmallCentered"
                $ vpgridFillRange = 12 - loopIndex if loopIndex < 12 else 4 - loopIndex % 4
                for vpgridFillLoop in range (0, vpgridFillRange):
                    hbox:
                        null
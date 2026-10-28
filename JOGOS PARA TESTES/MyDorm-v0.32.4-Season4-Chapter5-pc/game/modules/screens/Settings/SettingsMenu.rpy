screen SettingsMenu ():
    tag subMenu
    python:
        menuMarginX = getScreenDim (0.025)
        menuMarginY = getScreenDim (0.025, False)
        menuSpacing = menuMarginX * getSmallerScreenDimension ()
        buttons = []
        for (settingsTabLabel, settingsTab) in myDormMenu.getTabs ("Settings"):
            buttons.append ( [ settingsTabLabel, settingsTab, [ SetDict (myDormMenu.currentTab, "Settings", settingsTab), Function (myDormMenu.showCurrentTab, "Settings") ], True ])
    frame style "MenuScreenButtonsFrame":
        pos (1.0 - menuMarginX, menuMarginY)
        hbox:
            spacing menuSpacing
            for (buttonLabel, buttonIcon, buttonAction, buttonTrigger) in buttons:
                use MenuButton (buttonLabel, buttonIcon, buttonAction, buttonTrigger)
# Todo: Make "high prio" init
# add a dict for all the mod menues and screens
# a modder adds a new entry in their mod with
# MyDormSettingsModMenus.update ({...})
# For additional content in existing screens
# MyDormSettingsModScreen.update ({...})
# make the buttons here globally accessible (similar to the rest of this ToDo), so modders can add new "tabs"
#    use SettingsModMenu ()
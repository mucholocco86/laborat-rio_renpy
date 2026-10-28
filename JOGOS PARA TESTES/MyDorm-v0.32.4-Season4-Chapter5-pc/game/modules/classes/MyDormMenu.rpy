init -10000 python:

    class MyDormMenu:

        currentTab = {} # set in __init__ to first list value tabs dictionary
        tabs = {
            "Help"      : [ (_("Teclado"), "Keyboard"), (_("Ratón"), "Mouse"), (_("Mando de juego"), "Gamepad") ],
            "Settings"  : [ (_("General"), "General"), (_("Menú"), "Menu"), (_("Diálogo"), "Dialogue"), (_("Opciones"), "Choices"), ("Language", "Languages") ]
        }

        def __init__ (self):
            for menuScreen, menuTabs in self.tabs.items ():
                self.currentTab.update ({ menuScreen : menuTabs [0][1] })
            return

        def getCurrentTab (self, screenName):
            if screenName in self.currentTab:
                return self.toScreenName (screenName, self.currentTab [screenName])
            return None

        def getTabScreenNames (self, screenName):
            tabsList = []
            if screenName in self.tabs.keys ():
                for tab in self.tabs [screenName]:
                    tabsList.append (self.toScreenName (screenName + "Tab", tab))
            return tabsList

        def getTabs (self, screenName):
            if screenName in self.tabs:
                return self.tabs [screenName]
            return None

        def toScreenName (self, prefix, stringValue):
            if type (stringValue) is tuple:
                strVal, stringValue = stringValue
            stringValue = prefix + " Tab " + stringValue
            return stringValue.title ().replace (" ", "")

        def showCurrentTab (self, screenName, isScreenCall=False):
            currentTab = self.getCurrentTab (screenName)
            if isScreenCall:
                renpy.call_screen (currentTab)
            else:
                renpy.transition (config.enter_transition)
                renpy.show_screen (currentTab)

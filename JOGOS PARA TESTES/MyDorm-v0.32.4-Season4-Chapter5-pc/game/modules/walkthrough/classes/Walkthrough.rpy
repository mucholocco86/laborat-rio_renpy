init python:
    class Walkthrough:

        def __init__ (self):
            self.colors = {
                "negative" : "cc9933",
                "neutral" :  "cccccc",
                "positive" : "3399cc"
            }
            self.replacements = {}
            self.textSize = str (int (0.5 * gui.label_text_size))

        def addGeneralInfo (self, files):
            for filename, languages in files.items (): 
                for language, menus in languages.items ():
                    for menuLineNumber, textsToFormat in menus.items ():
                        for textKey, texts in textsToFormat.items ():
                            newTextItem = "{size=" + self.textSize + "}{i}"
                            for key, text in texts.items ():
                                newTextItem += "\n{color=" + self.getColor (text ["color"]) + "}" + text ["value"] +"{/color}"
                            newTextItem += "{/i}{/size}"
                            self.updateReplacements (filename, language, menuLineNumber, textKey, self.getReplacementItem (filename, language, menuLineNumber, textKey) + newTextItem)
            return

        def addInfoAboutVariables (self, files):
            for filename, languages in files.items ():
                for language, menus in languages.items ():
                    for menuLineNumber, choiceItems in menus.items ():
                        for textKey, characterItems in choiceItems.items ():
                            newTextItem = "{size=" + self.textSize + "}{i}"
                            for characterName, infoItems in characterItems.items ():
                                newTextItem +=  "\n" + characterName + ":"
                                for infoVariable, infoValue in infoItems.items ():
                                    newTextItem += " {color=" + self.getColor (infoValue) + "}" + infoVariable + " " + ("+" if infoValue > 0 else "") + str (infoValue) + "{/color},"
                                newTextItem = newTextItem[:-1]
                            newTextItem = newTextItem + "{/i}{/size}"
                            self.updateReplacements (filename, language, menuLineNumber, textKey, newTextItem + self.getReplacementItem (filename, language, menuLineNumber, textKey))
            return

        def addToTranslations (self, language, items):
            if not language in self.translations.keys ():
                self.translations.update ({ language : {} })
            self.translations [language].update (items)

        def clearLines (self):
            self.replacements.clear ()
            return

        def configure (self, values):
            for key, value in values.items ():
                self.config.update ({ key : value })

        def getChoiceSwitches (self):
            return sorted (self.choiceSwitches.items ())

        def getColor (self, value):
            if isinstance (value, int):
                return self.colors ["positive"] if value > 0 else self.colors ["negative"] if value < 0 else self.colors ["neutral"]
            elif value in self.colors.keys ():
                return self.colors [value]
            else:
                return self.colors ["neutral"]

        def getReplacementItem (self, filename, language, menuLineNumber, key):
            if filename in self.replacements.keys ():
                if language in self.replacements [filename].keys ():
                    if menuLineNumber in self.replacements [filename][language].keys ():
                        if key in self.replacements [filename][language][menuLineNumber].keys ():
                            return self.replacements [filename][language][menuLineNumber][key]
            return ""

        def str (self, value):
            if not value:
                return type (value)
            return str (value)

        def updateReplacements (self, filename, language, menuLineNumber, textKey, newTextItem):
            if not filename in self.replacements:
                self.replacements.update ({ filename : {} })
            if not language in self.replacements [filename]:
                self.replacements [filename].update ({ language : {} })
            if not menuLineNumber in self.replacements [filename][language]:
                self.replacements [filename][language].update ({ menuLineNumber : {} })
            self.replacements [filename][language][menuLineNumber].update ({ textKey : newTextItem })
            return

    walkthrough = Walkthrough ()
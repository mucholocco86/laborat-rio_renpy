init 9999 python:
    # save the say_menu_text_filter callback here, so we can add it in our own
    Walkthrough_replaceSayMenuTextFilterCallback = config.say_menu_text_filter

    def Walkthrough_SayMenuTextFilterCallback (searchString):
        # if there is another callback in use, this will call it (see line 3)
        if Walkthrough_replaceSayMenuTextFilterCallback:
            searchString = Walkthrough_replaceSayMenuTextFilterCallback (searchString)
        fileName = renpy.get_filename_line ()[0][0:-4]
        lineNumber = renpy.get_filename_line ()[1]
        # remove unneccesary whitespaces etc.
        searchString = searchString.strip ()
        if persistent.walkthrough:
            replacements = walkthrough.replacements
            fileHasWalkthrough = False
            for fname in replacements:
                if fileName in (fname, "game/" + fname): # rpa files don't need the game path
                    fileHasWalkthrough = True
                    if fileName == "game/" + fname:
                        fileName = fname # we don't use the game path to target content files in the walkthrough files
                    break
            if fileHasWalkthrough:
                replacements = replacements [fileName]
                if persistent.lang in replacements: # check if language is in WT
                    replacements = replacements [persistent.lang]
                    if lineNumber in replacements:  # check if menu line has a WT info
                        replacements = replacements [lineNumber]
                        if searchString in replacements:
                            searchString = searchString + replacements [searchString]
        return searchString# + "\n" + fileName + " " + str (lineNumber)

    config.say_menu_text_filter = Walkthrough_SayMenuTextFilterCallback
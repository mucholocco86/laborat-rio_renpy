screen ProfileDetailsBio(characterProfile):
    default ScreenActiveInput = None
    python:
        from datetime import datetime
        attributeList = {
            0 : (_("Cumpleaños"), "birthday"),
            1 : (_("Edad"), "age"),
            #2 : (_("Altura"), "height"),
            2 : (_("Altura"), "altura"),
            3 : (_("Relation"), "role"),
            5 : (_("Trabajo"), "job"),
        }
        if characterProfile._var ("profession"):
            attributeList.update ({ 4 : (_("Profesión"), "profession") })
        if characterProfile._var ("traits, physical"):
            attributeList.update ({ 6 : (_("Rasgos físicos"), "traits, physical") })
        if characterProfile._var ("traits, mental"):
            attributeList.update ({ 7 : (_("Rasgos mentales"), "traits, mental") })
    vpgrid:
        cols 1
        draggable True
        mousewheel True
        scrollbars "vertical"
        xfill True
        yfill True
        xysize (900, 900)
        vbox:
            for thisKey, (thisLabel, thisField) in sorted (attributeList.items ()):
                hbox:
                    label renpy.translate_string (thisLabel).capitalize () + ": " style "ProfileLabel"
                    if characterProfile._var (thisField):
                            if thisField == "birthday":
                                python:
                                    bdate = datetime.strptime (characterProfile._var (thisField), "%Y-%m-%d")
                                    birthday = bdate.strftime ('%d') + ". "
                                    birthday += renpy.translate_string (bdate.strftime ("%B"))
                                text str (birthday) style "Profile_text"
                            else:
                                python:
                                    thisValue = characterProfile._var (thisField)
                                    if isinstance (thisValue, str) and "," in thisValue:
                                        thisNewVal = []
                                        thisValue = thisValue.split (",")
                                        for thisVal in thisValue:
                                            thisNewVal += [ renpy.translate_string (thisVal) ]
                                        thisValue = ", ".join (thisNewVal)
                                    elif isinstance (thisValue, str):
                                        thisValue = renpy.translate_string (thisValue)
                                text str (thisValue).capitalize () style "Profile_text"
                    elif hasattr (characterProfile, thisField):
                        text renpy.translate_string (str (getattr (characterProfile, thisField))).capitalize () style "Profile_text"
            python:
                theseDecisions = {}
                if characterProfile.defaultName in Decisions:
                    theseDecisions = Decisions [characterProfile.defaultName]
            for thisKey, theseValues in sorted (theseDecisions.items ()):
                python:
                    if len (theseValues) == 4:
                        thisField, thisLabel, thisDescription, thisDependency = theseValues
                        thisDependency = characterProfile._var (thisDependency)
                    else:
                        thisField, thisLabel, thisDescription = theseValues
                        thisDependency = True
                if thisDependency:
                    null height 30
                    if thisDescription not in [ "InputTrigger", "LewdInputTrigger", "MCLewdInputTrigger", "RPTrigger" ]:
                        vbox:
                            hbox:
                                hbox:
                                    button style "ProfilesButton":
                                        # varvar is an actual function and is the wrapper for characterProfile._var()
                                        # Do not touch this or it will most likely break!
                                        action [ SelectedIf (characterProfile._var (thisField)), Function (varvar, characterProfile, thisField, True) ]
                                        text _("Sí") style "ProfilesButton_text"
                                    button style "ProfilesButton":
                                        action [ SelectedIf (not characterProfile._var (thisField)), Function (varvar, characterProfile, thisField, False) ]
                                        text _("No") style "ProfilesButton_text"
                                label renpy.translate_string (thisLabel).capitalize () style "ProfileLabel"
                            text renpy.translate_string (thisDescription).capitalize ()
                    elif thisDescription in [ "LewdInputTrigger" ]:
                        vbox:
                            hbox:
                                label renpy.translate_string (thisLabel).capitalize ()  + ": " style "ProfileLabel"
                                hbox:
                                    if ScreenActiveInput == thisField:
                                        frame:
                                            style "ProfilesInputFrame"
                                            input style "ProfilesInput":
                                                changed characterProfile.setMCLewdName
                                                default characterProfile.name.lewd
                                        pass
                                    else:
                                        button style "ProfilesInputButton":
                                            action [ SetLocalVariable ("ScreenActiveInput", thisField) ]
                                            text str (characterProfile.name.lewd) style "ProfilesInputButton_text"
                    elif thisDescription in [ "MCLewdInputTrigger" ]:
                        vbox:
                            hbox:
                                label renpy.translate_string (thisLabel).capitalize () + ": " style "ProfileLabel"
                                hbox:
                                    if ScreenActiveInput == thisField:
                                        frame:
                                            style "ProfilesInputFrame"
                                            input style "ProfilesInput":
                                                changed characterProfile.setMCLewdName
                                                default characterProfile.name.mcLewd
                                        pass
                                    else:
                                        button style "ProfilesInputButton":
                                            action [ SetLocalVariable ("ScreenActiveInput", thisField) ]
                                            text str (characterProfile.name.mcLewd) style "ProfilesInputButton_text"
                    elif thisDescription in [ "RPTrigger" ]:
                        python:
                            thisFunction = getattr (characterProfile, thisField)
                            thisValue = thisFunction ()
                        vbox:
                            hbox:
                                label renpy.translate_string (thisLabel).capitalize () + ": " style "ProfileLabel"
                                hbox:
                                    button style "ProfilesButton":
                                        # varfunc is an actual function and is the wrapper for characterProfile."thisField" ()
                                        # Do not touch this or it will most likely break!
                                        action [ Function (varfunc, characterProfile, thisField, -1) ]
                                        text "-" style "ProfilesButton_text"
                                    frame:
                                        background None
                                        xsize 100
                                        xalign 0.5
                                        text str (thisValue) xalign 0.5 text_align 0.5
                                    button style "ProfilesButton":
                                        action [ Function (varfunc, characterProfile, thisField, +1) ]
                                        text "+" style "ProfilesButton_text"
                            text _("Se necesitan al menos cinco (5) puntos para tener la opción de iniciar una relación de amantes.")

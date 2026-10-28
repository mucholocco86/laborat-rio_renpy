screen ProfilesEditCharacterName(characterProfile):
    python:
        buttonAction = {
            "apply" : [ Hide ("ProfilesEditCharacterName"), Function (characterProfile.setName) ],
            "cancel" : [ Hide ("ProfilesEditCharacterName") ]
        }
        if not hasattr (characterProfile, "profilePicture"):
            setattr (characterProfile, profilePicture, (characterProfile.name.last_name + "_" + characterProfile.defaultName).lower ())
        profileImage = "images/profiles/characters/" + characterProfile.profilePicture
        fileExtensions = [ "png", "webp" ]
        hasProfileImage = False
        for fileExtension in fileExtensions:
            profileImageWithExtension = profileImage + "." + fileExtension
            if renpy.loadable (profileImageWithExtension):
                hasProfileImage = True
                profileImage = profileImageWithExtension
                break
        if not hasProfileImage:
            profileImage = "images/profiles/characters/" + (characterProfile.name.last_name + "_" + characterProfile.defaultName).lower ()
            for fileExtension in fileExtensions:
                profileImageWithExtension = profileImage + "." + fileExtension
                if renpy.loadable (profileImageWithExtension):
                    hasProfileImage = True
                    profileImage = profileImageWithExtension
                    break
        boxHeight = 0.5
        boxWidth = 0.3
    use ModalScreen (buttonAction ["cancel"], ModalBackgroundColor)
    frame style "ConfirmFrame":
        xysize (boxHeight, boxWidth)
        use Borders ()
        hbox style "MyDormBoxCentered":
            vbox style "MyDormBox":
                image profileImage zoom 0.35 xalign 0.5
                text _("Cambiar el nombre de este personaje") style "TextMediumCentered"
                frame style "ProfilesInputFrame":
                    xsize 0.5
                    input value VariableInputValue (characterProfile.defaultName [0:3].lower () + ".name.first_name") style "ProfilesInput" xsize 1.0
        button:
            style "MyDormButton"
            anchor (1.0, 0.0)
            pos (0.985, 0.05)
            action [ Hide () ]
            text _("Atrás") style "MyDormButton"
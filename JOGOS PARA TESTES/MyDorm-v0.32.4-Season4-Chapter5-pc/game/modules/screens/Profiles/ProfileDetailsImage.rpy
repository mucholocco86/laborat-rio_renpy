screen ProfileDetailsImage(characterProfile):
    default ScreenCurrentProfileImage = None
    default profileImageLargePath = "images/profiles/large/"
    vbox:
        xysize (0.5, 1.0)
        frame:
            background None
            align (0.5, 0.5)
            xysize (920, 910)
            yoffset -5
            python:
                profileImages = characterProfile.profileImages
                auxSizeA = 900
                auxSizeB = 900
                auxSizeC = 900
                auxSizeD = 900
                if characterProfile.isProfileImageIndexAvailable (characterProfile.getDefaultProfileImageIndex()):
                    ScreenCurrentProfileImage = characterProfile.getDefaultProfileImageIndex()
                else:
                    if ScreenCurrentProfileImage is None:
                        for profileImageIndex in range (len (characterProfile.profileImages)):
                            if characterProfile.isProfileImageAvailable (characterProfile.profileImages [profileImageIndex][0]):
                                ScreenCurrentProfileImage = profileImageIndex
                                break
                    elif len (characterProfile.profileImages) == 0:
                        ScreenCurrentProfileImage = None
                    elif not characterProfile.isProfileImageAvailable (characterProfile.profileImages [ScreenCurrentProfileImage][0]):
                        ScreenCurrentProfileImage = 0
                if ScreenCurrentProfileImage is not None:
                    profileImagePath = "images/profiles/"
                    profileImage, profileImageFilter = characterProfile.profileImages [ScreenCurrentProfileImage]
                    if characterProfile.isProfileImageAvailable (profileImage):
                        for fileExtension in [ "png", "webp" ]:
                            profileImageIsOnDrive = False
                            if renpy.loadable (profileImagePath + profileImage + "." + fileExtension):
                                profileImageIsOnDrive = True
                                break
                        if not profileImageIsOnDrive:
                            profileImage = "notAvailable"
                            fileExtension = "png"
                        pdp = Image (profileImagePath + profileImage + "." + fileExtension)
                        pdpImageSize = renpy.image_size (pdp)
                        if pdpImageSize [0]  <= pdpImageSize [1]:
                            auxSizeC = int (pdpImageSize [0] / pdpImageSize [1] * auxSizeA)
                        else:
                            auxSizeD = int (pdpImageSize [1] / pdpImageSize [0] * auxSizeA)
                    else:
                        profileImage = "notAvailable"
                        fileExtension = "png"
                        pdp = Image (profileImagePath + profileImage + "." + fileExtension)
                        pdpImageSize = renpy.image_size (pdp)

            if ScreenCurrentProfileImage is not None:
                imagebutton:
                    align (0.5, 0.5)
                    xysize (auxSizeC, auxSizeD)
                    idle im.Scale(pdp,auxSizeC,auxSizeD)
                    hover im.Scale(pdp,auxSizeC,auxSizeD)
                    sensitive renpy.loadable (profileImageLargePath + profileImage + "_large.webp")
                    action [ SelectedIf (False), ShowMenu ("ProfileImageScrollable",characterProfile, Image(profileImageLargePath + profileImage + "_large.webp")) ]

            frame style "ProfilesImageButtonFrame":
                vbox:
                    spacing 10
                    for imageIndex in range (len (characterProfile.profileImages)):
                        button:
                            style "ProfilesButtonNoMargin"
                            if characterProfile.isProfileImageAvailable (characterProfile.profileImages [imageIndex][0]):
                                action [ SelectedIf(ScreenCurrentProfileImage == imageIndex), SetLocalVariable ("ScreenCurrentProfileImage", imageIndex), Function(characterProfile.setDefaultProfileImageIndex, imageIndex=imageIndex) ]
                            text str (imageIndex + 1) style "ProfileButton_text"
            # python:
            #     previousImage = ScreenCurrentProfileImage - 1
            #     if previousImage >= 0:
            #         for imageIndex in range (0, previousImage, -1):
            #             previousImage = None
            #             if characterProfile.isProfileImageAvailable (characterProfile.profileImages [imageIndex][0]):
            #                 previousImage = imageIndex
            #                 break
            #     else:
            #         previousImage = None
            #     nextImage = ScreenCurrentProfileImage + 1
            #     if nextImage < len (characterProfile.profileImages):
            #         for imageIndex in range (nextImage, len (characterProfile.profileImages)):
            #             nextImage = None
            #             if characterProfile.isProfileImageAvailable (characterProfile.profileImages [imageIndex][0]):
            #                 nextImage = imageIndex
            #                 break
            #     else:
            #         nextImage = None
            # if previousImage is not None:
            #     frame style "ProfilesImageButtonFrameNext":
            #         button:
            #             style "ProfilesButtonNoMargin"
            #             action [ SetLocalVariable ("ScreenCurrentProfileImage", previousImage)]
            #             text "\u2906" style "ProfileButton_text"
            # if nextImage is not None:
            #     frame style "ProfilesImageButtonFramePrevious":
            #         button:
            #             style "ProfilesButtonNoMargin"
            #             action [ SetLocalVariable ("ScreenCurrentProfileImage", nextImage)]
            #             text "\u2907" style "ProfileButton_text"
init offset = 100

screen choice(items):
    style_prefix "choice"
    vbox:
        spacing 10
        yalign 0.6
        for n, i in enumerate(items, 1):
            if n < 10:
                key str(n) action i.action
                key "K_KP" + str(n) action i.action
                textbutton str(n) + ". " + i.caption action i.action

screen gallery():
    style_prefix "gallery"
    modal True

    default replaysshow = []
    default local_dict = {}
    default filter_scene_screen = ""
    default filter_girl_screen = ""

    default thumb_width = 400
    default thumb_height = 225

    #
    # Gallery background
    #
    add "gallery/galleryback.jpg"

    #
    # Return button
    #
    textbutton _("Return"):
        style_prefix "normal"
        align (0.9, 0.05)
        keysym "game_menu"
        hover_sound audio.neon
        action Hide("gallery", transition=dissolve)


    # Restrain the list according to the filters selected
    $ replaysshow = []
    for r in replays:
        if (filter_scene == "all" or filter_scene in r[4]) and (filter_girl == "all" or filter_girl in r[5]):

            # Construction of the list of variables to pass to the replay
            $ local_dict = {}
            for s in r[6]:
                $ local_dict.update({s : getattr(store, s)})

            $ replaysshow.append([r[0], r[1], r[2], r[3], r[4], r[5], local_dict])

    # Get translated value for the 2 filters
    $ filter_scene_screen = renpy.substitute(filter_scene_list[filter_scene])
    $ filter_girl_screen = renpy.substitute(filter_girl_list[filter_girl])

    hbox:
        align (0.5, 0.05)
        spacing 40

        #
        # Scene filter
        #
        textbutton _("{color=#02ffbf}Filter:{/color} [filter_scene_screen!t]"):
            style "galleryfilter_button"
            action Show("filter_scene")

        #
        # Girl filter
        #
        textbutton _("{color=#02ffbf}Girl:{/color} [filter_girl_screen!t]"):
            style "galleryfilter_button"
            action Show("filter_girl")

        if not persistent.gallery_unlocked:
            textbutton "Unlock scenes" action SetVariable("persistent.gallery_unlocked", True) style "galleryfilter_button"
        elif persistent.gallery_unlocked:
            textbutton "Lock scenes" action SetVariable("persistent.gallery_unlocked", False) style "galleryfilter_button"


    #
    # Thumbnails gallery
    #
    frame:
        ysize (thumb_height + 26 + 10) * 3 + 100
        align (0.48, 0.75)

        vpgrid:
            cols 3
            spacing 29
            draggable True
            mousewheel True

            scrollbars "vertical"

            # Since we have scrollbars, we have to position the side, rather
            # than the vpgrid proper.
            # side_xalign 0.9
            side_spacing 20

            for r in replaysshow:
                vbox:
                    xsize thumb_width
                    spacing 7

                    frame:
                        style "empty"
                        xysize (thumb_width, thumb_height)

                        # Scene thumbnail
                        imagebutton:
                            pos (5, 3)
                            idle "gallery/" + r[1] + ".jpg"
                            hover im.MatrixColor("gallery/" + r[1] + ".jpg", im.matrix.tint(1.00, 1.00, 0.20) * im.matrix.brightness(0.25))
                            insensitive im.Blur(im.Grayscale("gallery/" + r[1] + ".jpg"), 3.4)
                            sensitive renpy.seen_image(r[0]) or persistent.gallery_unlocked
                            hover_sound audio.neon
                            action Replay(r[2], scope=r[6], locked=False)

                        # "LOCKED" word displayed above the thumbnail if the scene is locked
                        if not renpy.seen_image(r[0]) and not persistent.gallery_unlocked:
                            add Text("LOCKED", style="locked_gallery")

                        # Add a neon frame around the thumbnail
                        add "gallery/neon.png"

                    # Title of the scene
                    text r[3] xalign 0.5 size 27 style "galle"


screen ekabarlunapennychoice():
    modal True
    add "ff 85"
    imagemap:
        ground "ekabaridle"
        idle "ekabaridle"
        hover "ekabarhover"
        hotspot (150, 79, 474, 898) action Jump('werewolfhelpm') hovered [ Play ("sound", "audio/sfx/uis.mp3")]
        hotspot (1329, 63, 487, 920) action Jump('vampirehelpm') hovered [ Play ("sound", "audio/sfx/uis.mp3")]

        textbutton "Mod: Both" align (0.52, 0.95) action Jump("mod_vamp_wolf_help") text_size 60 hovered [ Play ("sound", "audio/sfx/uis.mp3")]

screen piratecrew:
    modal True
    add "gg 6"
    imagemap:
        ground "crewidle"
        idle "crewidle"
        hover "crewhover"
        hotspot (83, 58, 595, 779) action Jump('piratecrewreddss') hovered [ Play ("sound", "audio/sfx/uis.mp3")]
        hotspot (684, 57, 552, 807) action Jump('piratecrewlorrdy') hovered [ Play ("sound", "audio/sfx/uis.mp3")]
        hotspot (1247, 58, 571, 781) action Jump('piratecrewscarlet') hovered [ Play ("sound", "audio/sfx/uis.mp3")]

    text "[pink]Nova +1" pos (0.185, 0.7)
    text "[pink]Nancy +1" ypos 0.7 xalign 0.5

define trial1 = [ 
    {'label': 'Whatever', 'scene': 'trial1a'},
    {'label': '[gr]I understand', 'scene': 'trial1b'},
    {'label': 'Fuck you', 'scene': 'trial1c'},
]
define trial2 = [ 
    {'label': 'I want a lawyer', 'scene': 'trial2a'},
    {'label': 'Trial by combat', 'scene': 'trial2b'},
    {'label': '[gr]Ask for an introduction', 'scene': 'trial2c'},
]
define trial3 = [ 
    {'label': 'I am her owner', 'scene': 'trial3a'},
    {'label': 'We’re friends', 'scene': 'trial3b'},
    {'label': '[gr]I am her servant', 'scene': 'trial3c'},
]
define trial4 = [ 
    {'label': 'Tell the truth', 'scene': 'trial4a'},
    {'label': '[gr]Lie', 'scene': 'trial4b'},
]
define trial5 = [ 
    {'label': 'She saved me', 'scene': 'trial5a'},
    {'label': '[gr]We were attacked', 'scene': 'trial5b'},
    {'label': 'I don’t know', 'scene': 'trial5c'},
]
define trial6 = [ 
    {'label': '[gr]I was useful to her', 'scene': 'trial6a'},
    {'label': 'She owed me', 'scene': 'trial6b'},
    {'label': 'We became lovers', 'scene': 'trial6c'},
]
define trial7 = [ 
    {'label': '[gr]Anima the Radiant', 'scene': 'trial7a'},
    {'label': 'Anala the Resplendent', 'scene': 'trial7b'},
    {'label': 'Anira the Shining', 'scene': 'trial7c'},
]
define trial8 = [ 
    {'label': 'Draxus', 'scene': 'trial8a'},
    {'label': 'Zephyros', 'scene': 'trial8b'},
    {'label': '[gr]Yliar', 'scene': 'trial8c'},
]
define trial9 = [ 
    {'label': '[gr]Raewyn', 'scene': 'trial9a'},
    {'label': 'Sylvannus', 'scene': 'trial9b'},
    {'label': 'Galnar', 'scene': 'trial9c'},
]
define trial10 = [ 
    {'label': '44', 'scene': 'trial10b'},
    {'label': '68', 'scene': 'trial10c'},
    {'label': '[gr]84', 'scene': 'trial10d'},
]
define trial11 = [ 
    {'label': '[gr]Elarisil', 'scene': 'trial11b'},
    {'label': 'Lalariel', 'scene': 'trial11c'},
    {'label': 'Tomodin', 'scene': 'trial11d'},
]
define trial12 = [ 
    {'label': '[gr]Accept', 'scene': 'trial12a'},
    {'label': 'Refuse', 'scene': 'trial12b'},
]
define trial13 = [ 
    {'label': 'I am innocent', 'scene': 'trial13a'},
    {'label': '[gr]I want to call a witness', 'scene': 'trial13b'},
    {'label': 'You will regret this', 'scene': 'trial13c'},
]
define trial14 = [ 
    {'label': 'Arannis', 'scene': 'trial14a'},
    {'label': '[gr]Lorelei', 'scene': 'trial14b'},
]

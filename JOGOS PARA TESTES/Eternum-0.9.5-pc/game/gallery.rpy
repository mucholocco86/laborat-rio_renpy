
init offset = 99

default persistent.gallery_unlocked = False
default filter_scene = "all"
default filter_character = "all"

define filter_scene_list = {
    "all" : _("All{#gallery,scenefilter}"),
    "exhibition" : _("Exhibition"),
    "teasing" : _("Teasing"),
    "fingering" : _("Fingering"),
    "handjob" : _("Handjob"),
    "rub" : _("Rubbing"),
    "blowjob" : _("Blowjob"),
    "cun" : _("Cunnilingus"),
    "vaginal" : _("Vaginal Sex"),
    "cumshot" : _("Cumshot"),
    "creampie" : _("Creampie"),
    "swallow" : _("Cum Swallow"),
    "footjob" : _("Footjob"),
    "boobjob" : _("Boobjob"),
    "sextoy" : _("Sex Toy"),
    "anal" : _("Anal Sex"),
    "group" : _("Group Sex"),
}

define filter_girl_list = {
    "all" : _("All{#gallery,girlfilter}"),
    "annie" : "Annie",
    "nancy" : "Nancy",
    "dalia" : "Dalia",
    "penelope" : "Penelope",
    "luna" : "Luna",
    "side" : _("Side Girls"),
    "alex" : "Alex",
    "nova" : "Nova",
    "calypso" : "Calypso"
}

# 0 : Condition (an image name): If the player already seen this image, the replay will be unlocked
# 1 : Thumbnail image name
# 2 : Label name: Which label will be played by the replay
# 3 : Description: Description displayed under the thumbnail
# 4 : Filters
# 5 : Characters involved
# 6 : Scope (List of variables to pass to the replay)

define replays = [
    ["db 62", "ga_dalia1", "ga_dalia1", _("Shower Show"), ["exhibition"], ["dalia"], ["mc"]],
    ["eva 44", "ga_side1", "ga_side1", _("Blurred Realities"), ["blowjob","vaginal","cumshot"], ["side"], ["mc"]],
    ["an 91", "ga_annie1", "ga_annie1", _("Midnight Comfort"), ["cumshot", "rub"], ["annie"], ["mc"]],
    ["aaw 163", "ga_penny1", "ga_penny1", _("Perfect Shot"), ["exhibition","teasing"], ["penelope"], ["mc"]],
    ["bbb 99", "ga_nova1", "ga_nova1", _("Devious Games"), ["blowjob"], ["nova"], ["mc"]],
    ["bbb 125", "ga_side2", "ga_side2", _("Egyptian Plunder"), ["vaginal","cumshot"], ["side"], ["mc"]],
    ["bt 70", "ga_nancy1", "ga_nancy1", _("Forbidden Fruit"), ["cun","teasing"], ["nancy"], ["mc"]],
    ["cd 76", "ga_dalia2", "ga_dalia2", _("Still Waters"), ["blowjob","swallow"], ["dalia"], ["mc"]],
    ["cx 64", "ga_annie2", "ga_annie2", _("Space Odyssey"), ["fingering", "handjob", "rub"], ["annie"], ["mc"]],
    ["ccc 80", "ga_alex1", "ga_alex1", _("Fancy Evening"), ["handjob","blowjob", "cumshot", "swallow"], ["alex"], ["mc"]],
    ["dm 71", "ga_luna1", "ga_luna1", _("Mexican Feast"), ["teasing","fingering"], ["luna"], ["mc", "lastname", "anniepath"]],
    ["dr 104", "ga_nova2", "ga_nova2", _("Daring Challenge"), ["exhibition","sextoy"], ["nova"], ["mc", "maatsexvariant", "maatsex"]],
    ["dpp 83", "ga_penny2", "ga_penny2", _("Honor Mission"), ["cumshot","rub", "boobjob"], ["penelope"], ["mc", "novadildo", "dare3", "lastname"]],
    ["ds 47", "ga_nancy2", "ga_nancy2", _("Emergency Stop"), ["cumshot","vaginal","blowjob"], ["nancy"], ["mc", "nancymommy"]],
    ["eaa 99", "ga_annie3", "ga_annie3", _("Nighttime Cookies"), ["cumshot","blowjob", "cun"], ["annie"], ["mc", "nancypath"]],
    ["eec 88", "ga_side3", "ga_side3", _("Royal Protocol"), ["cumshot","handjob"], ["side", "calypso"], ["mc"]],
    ["ed 140", "ga_dalia3", "ga_dalia3", _("Magnetic Sandstorm"), ["cumshot","blowjob", "cun", "rub", "swallow"], ["dalia"], ["mc", "calypsohandjob", "penelopepath"]],
    ["eee 115", "ga_alex2", "ga_alex2", _("Christened Apartment"), ["cun","vaginal", "footjob", "creampie"], ["alex"], ["mc", "alexkisswest"]],
    ["fl 184", "ga_luna2", "ga_luna2", _("Handy Hideaway"), ["fingering","handjob", "blowjob", "cumshot", "swallow"], ["luna"], ["mc"]],
    ["fg 141", "ga_penny3", "ga_penny3", _("Motor Madness"), ["handjob","vaginal", "cumshot", "creampie"], ["penelope"], ["mc", "pennyrough"]],
    ["fc 84", "ga_nova3", "ga_nova3", _("Rushed Break"), ["handjob","vaginal", "blowjob", "cumshot", "creampie"], ["nova"], ["mc", "novadildo", "crimesuccess"]],
    ["gt 115", "ga_novanancy", "ga_novanancy", _("Bermuda Triangle"), ["handjob","vaginal", "blowjob", "creampie", "group"], ["nova", "nancy"], ["mc", "namelong", "nancymommy", "favoriteposenova", "maatsexvariant"]],
    ["ga 74", "ga_annie4", "ga_annie4", _("Room Service"), ["fingering","vaginal", "cun", "cumshot", "creampie", "rub"], ["annie"], ["mc", "daliapath"]],
    ["gx 94", "ga_alex3", "ga_alex3", _("Quick Splash"), ["blowjob","vaginal", "cumshot"], ["alex"], ["mc"]],
    ["gd 121b", "ga_dalia4", "ga_dalia4", _("Desert Heat"), ["blowjob","vaginal", "creampie", "swallow", "rub"], ["dalia"], ["mc", "namelong"]],
    ["qc 109", "ga_calypso1", "ga_calypso1", _("Royal Proxy"), ["blowjob","vaginal", "cumshot", "fingering", "cun", "group", "sextoy", "teasing"], ["side", "calypso"], ["mc", "namelong", "mcshort", "mc_dash"]],
    ["qp 189", "ga_penny4", "ga_penny4", _("Knotty List"), ["blowjob","vaginal", "handjob", "creampie", "anal"], ["penelope"], ["mc", "namelong", "mcshort", "mc_dash"]],
    ["qss 83", "ga_alexdalia", "ga_alexdalia", _("Third Degree"), ["blowjob","vaginal", "boobjob", "group", "handjob", "cumshot"], ["alex", "dalia"], ["mc", "namelong", "mcshort", "mc_dash"]],
    ["qaa 75", "ga_luna3", "ga_luna3", _("Paranormal Activity"), ["fingering","vaginal", "creampie", "cumshot"], ["luna"], ["mc", "namelong", "mcshort", "mc_dash"]],
    #["", "","",[""],[""]]
]


screen filter_scene():
    style_prefix "filter_select"
    modal True

    frame:
        background Frame("filter_select_background", gui.notify_frame_borders, tile=gui.frame_tile)
        # Position the frame at mouse pointer position
        pos(renpy.get_mouse_pos()[0], renpy.get_mouse_pos()[1])
        ymaximum 900

        vbox:
            spacing 30

            viewport:
                scrollbars "vertical"
                mousewheel True
                draggable True
                side_spacing 20

                vbox:
                    textbutton _("All") action [ SetVariable("filter_scene", "all"), Hide("filter_scene") ]

                    # Sort the dictionary by translated value
                    for fil in sorted(filter_scene_list.items(), key=lambda item: renpy.substitute(item[1])):
                        # Display all values except for "all" (already displayed just above)
                        if fil[0] != "all":
                            textbutton _(fil[1]):
                                action [ SetVariable("filter_scene", fil[0]), Hide("filter_scene") ]

            textbutton _("Cancel") keysym "game_menu" action Hide("filter_scene") xalign 0.5


style filter_select_viewport is viewport
style filter_select_viewport:
    xfill False
    yfill False

style filter_select_vscrollbar is vscrollbar
style filter_select_vscrollbar:
    unscrollable "hide"

screen filter_girl():
    modal True

    add "points"
    imagemap:
        ground "points"
        idle "points2_gallery"
        hover "points3_gallery"

        if annieu:
            hotspot (66, 51, 357, 465) action [ Play("soundlow", "neon.mp3"), SetVariable("filter_girl", "annie"), Hide("filter_girl") ] hover_sound audio.neon
        if nancyu:
            hotspot (436, 20, 350, 470) action [ Play("soundlow", "neon.mp3"), SetVariable("filter_girl", "nancy"), Hide("filter_girl") ] hover_sound audio.neon
        if penelopeu:
            hotspot (793, 27, 353, 496) action [ Play("soundlow", "neon.mp3"), SetVariable("filter_girl", "penelope"), Hide("filter_girl") ] hover_sound audio.neon
        if daliau:
            hotspot (1175, 38, 325, 463) action [ Play("soundlow", "neon.mp3"), SetVariable("filter_girl", "dalia"), Hide("filter_girl") ] hover_sound audio.neon
        if lunau:
            hotspot (1526, 31, 344, 485) action [ Play("soundlow", "neon.mp3"), SetVariable("filter_girl", "luna"), Hide("filter_girl") ] hover_sound audio.neon
        if alexu:
            hotspot (67, 514, 357, 474) action [ Play("soundlow", "neon.mp3"), SetVariable("filter_girl", "alex"), Hide("filter_girl") ] hover_sound audio.neon
        if novau:
            hotspot (443, 508, 342, 486) action [Play("soundlow", "neon.mp3"), SetVariable("filter_girl", "nova"), Hide("filter_girl") ] hover_sound audio.neon
        if sideu:
            hotspot (787, 512, 414, 488) action [ Play("soundlow", "neon.mp3"), SetVariable("filter_girl", "side"), Hide("filter_girl") ] hover_sound audio.neon

        hotspot (1251, 653, 573, 228) action [ Play("soundlow", "neon.mp3"), SetVariable("filter_girl", "all"), Hide("filter_girl") ] hover_sound audio.neon

    key "game_menu" action Hide("filter_girl")


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
                            add Text(_("LOCKED"), style="locked_gallery")

                        # Add a neon frame around the thumbnail
                        add "gallery/neon.png"

                    # Title of the scene
                    text r[3] xalign 0.5 size 27 style "galle"

style galle:
    font "poiretone.ttf"
    outlines [(1 ,"#ecfefb80"),]

style locked_gallery:
    align (0.5, 0.5)
    size 75
    color "#ffffff"
    font gui.interface_text_font


style gallery_vscrollbar is vscrollbar:
    unscrollable "hide"


style galleryfilter_button:
    xsize 400

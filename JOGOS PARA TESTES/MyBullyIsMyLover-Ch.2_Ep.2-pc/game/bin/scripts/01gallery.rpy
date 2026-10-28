style gallery_text_face is default:
    font "bin/assets/faces/LaParisienne.otf"
    size 48
    color "#f1f1f1"

style gallery_text_name is default:
    font "bin/assets/faces/LaParisienne.otf"
    size 60
    color "#f1f1f1"

style gallery_text_points is default:
    font "bin/assets/faces/LaParisienne.otf"
    size 40
    color "#ffffff"

style gallery_text_route is default:
    font "bin/assets/faces/LaParisienne.otf"
    size 35
    color "#ffffff"

style gallery_text_button is default:
    font "bin/assets/faces/LaParisienne.otf"
    size 32
    color "#f1f1f1"
    outlines [ (1, "#00000000", 0, 0) ]

style gallery_text_title is default:
    font "bin/assets/faces/LaParisienne.otf"
    size 54
    color "#f1f1f1"

style gallery_text_locked is default:
    font "bin/assets/faces/LaParisienne.otf"
    size 54
    color "#d0d0d0"

style gallery_text_locked_sub is default:
    font "bin/assets/faces/LaParisienne.otf"
    size 24
    color "#b8b8b8"


init python:

    def _predict_gallery_assets():
        renpy.start_predict_screen("gallery")
        paths = [
            'bin/assets/gallery/gallery bg.png',
            'bin/assets/gallery/plate.png',
            'bin/assets/gallery/plate shadow.png',
            'bin/assets/gallery/face prev.png',
        ]
        for c in chars:
            paths += [c.background, c.body, c.head]
        for p in paths:
            renpy.start_predict(p)
            renpy.cache_pin(p)
    config.start_callbacks.append(_predict_gallery_assets)

    class GalleryItem:
        def __init__(self, label, thumb):
            self.label = label
            self.thumb = thumb

    sky_gl   = [GalleryItem("skyfirsttime", "i101"),
                GalleryItem("mytruefeelings", "i497"),
                GalleryItem("skycelebratewear1", "i623"),
                GalleryItem("skycelebratewear2", "i624"),
                GalleryItem("skytruthconfession", "ch1ep1_573"),
                GalleryItem("midnightbeachsexonsteroids", "ch1ep1_1381"),
                GalleryItem("skystressrelief", "ch1ep4_184")
    ]

    lily_gl  = []

    aine_gl  = [GalleryItem("ainethumbsuck", "ep7_624"),
                GalleryItem("relaximadoctor", "ch1ep1_1472"),
                GalleryItem("crackinganaineopen", "ch1ep3p2_361"),
                GalleryItem("ainepubtensionbuildup", "ch1ep3p2_548"),
                GalleryItem("aineonsteroids", "ch1ep3p2_931")
    ]

    emma_gl  = [GalleryItem("emmaxmcfirst", "ep7_442"),
                GalleryItem("emmaroleplay", "ese_294"),
                GalleryItem("emmapreggospecial", "ese_885"),
                GalleryItem("insubordinatepussy", "ch2ep2_1498")
    ]

    gwen_gl  = [GalleryItem("gwenmcpast", "i218"),
                GalleryItem("gwenhandjob", "ep3_409"),
                GalleryItem("gwenfirstarcfun", "ep4_291"),
                GalleryItem("gwenmorningsex", "ep6_771"),
                GalleryItem("gwenanal", "ch1ep2_1039"),
                GalleryItem("gwencumback", "ch2ep1_544")
    ]

    klara_gl = [GalleryItem("klaradrunkshow", "ch1ep2_543"),
                GalleryItem("forbiddenfruit", "ch2ep1_922")
    ]

    freya_gl = [GalleryItem("freyapantstease", "ep6_920"),
                GalleryItem("freyatitplay", "ch1ep1_658"),
                GalleryItem("freyasucknosuck", "ch1ep3_107"),
                GalleryItem("freyastitchcosplay", "ch1ep3_311"),
                GalleryItem("freyacarblowjob", "ch2ep1_306")
    ]

    naomi_gl = [GalleryItem("naomishowerfix", "ch1ep3p2_141")
    ]

    moon_gl  = [GalleryItem("moonlightskinnydip", "ch1ep1_1233"),
                GalleryItem("moonlollipopplay", "ch1ep2_230"),
                GalleryItem("kaitosorareunion", "ch1ep4_1152")
    ]

    class GalleryChar:
        def __init__(self, name, gallery, head, body, background, full_name=None):
            self.name       = name
            self.full_name  = full_name if full_name else name.title()
            self.gallery    = gallery
            self.head       = head
            self.body       = body
            self.background = background

    sky_g   = GalleryChar(name='sky',   full_name='Sky Hahn',         gallery=sky_gl,   head='bin/assets/gallery/sky_f.png',   body='bin/assets/gallery/sky_b.png',   background='bin/assets/gallery/sky_bg.png')
    lily_g  = GalleryChar(name='lily',  full_name='Lily Kim',         gallery=lily_gl,  head='bin/assets/gallery/lily_f.png',  body='bin/assets/gallery/lily_b.png',  background='bin/assets/gallery/lily_bg.png')
    aine_g  = GalleryChar(name='aine',  full_name='Aine Agnor',       gallery=aine_gl,  head='bin/assets/gallery/aine_f.png',  body='bin/assets/gallery/aine_b.png',  background='bin/assets/gallery/aine_bg.png')
    emma_g  = GalleryChar(name='emma',  full_name='Emma Meyer',       gallery=emma_gl,  head='bin/assets/gallery/emma_f.png',  body='bin/assets/gallery/emma_b.png',  background='bin/assets/gallery/emma_bg.png')
    gwen_g  = GalleryChar(name='gwen',  full_name='Gwen Wilson',      gallery=gwen_gl,  head='bin/assets/gallery/gwen_f.png',  body='bin/assets/gallery/gwen_b.png',  background='bin/assets/gallery/gwen_bg.png')
    klara_g = GalleryChar(name='klara', full_name='Klara Hahn',       gallery=klara_gl, head='bin/assets/gallery/klara_f.png', body='bin/assets/gallery/klara_b.png', background='bin/assets/gallery/klara_bg.png')
    freya_g = GalleryChar(name='freya', full_name='Freya Agnor',      gallery=freya_gl, head='bin/assets/gallery/freya_f.png', body='bin/assets/gallery/freya_b.png', background='bin/assets/gallery/freya_bg.png')
    naomi_g = GalleryChar(name='naomi', full_name='Naomi Rosenthal',  gallery=naomi_gl, head='bin/assets/gallery/naomi_f.png', body='bin/assets/gallery/naomi_b.png', background='bin/assets/gallery/naomi_bg.png')
    moon_g  = GalleryChar(name='moon',  full_name='"Moon Chi(?)"',    gallery=moon_gl,  head='bin/assets/gallery/moon_f.png',  body='bin/assets/gallery/moon_b.png',  background='bin/assets/gallery/moon_bg.png')

    chars = [
        sky_g,
        lily_g,
        aine_g,
        emma_g,
        gwen_g,
        klara_g,
        freya_g,
        naomi_g,
        moon_g,
        ]

    N = len(chars)

    def infinite_offset(i, item_width=480, num_items=N):
        center = (num_items - 1) // 2
        delta  = (i - center) % num_items
        if delta > center:
            delta -= num_items
        return -delta * item_width


transform char_focus(n, v, r, c):
    subpixel True
    transform_anchor True
    anchor (0.5, 1.0)
    easein_quart .5 zoom n alpha c matrixcolor BrightnessMatrix(v) * SaturationMatrix(r)


style gallery_char_button:
    activate_sound "audio/click.ogg"
    hover_sound "audio/switchclick.mp3"

default nav_target = None

screen gallery():

    tag menu

    modal True

    add 'bin/assets/gallery/gallery bg.png' align (.5, .5)

    key 'game_menu' action Return()

    default sel_offset = 344
    default sel_index  = 3
    default active_c   = chars[sel_index]
    default hovered_c  = None

    add active_c.background

    frame background None:

        xysize (config.screen_width, config.screen_height)
        align (.5, .5)

        hbox id 'characters':

            spacing 0
            align (.5, 1.0)

            for x in range(-N, 2 * N):

                $ i = x % N
                $ item = chars[i]

                $ raw  = abs(i - sel_index)
                $ dist = raw if raw <= N//2 else N - raw

                $ zoom_val, bright_val, saturation_val, alpha = (
                    (1.00,  0.00, 1.00, 1.0 ) if dist == 0 else
                    (0.65,  -1.0 ,  .0,  .75) if dist == 1 else
                    (0.45,  -.95 ,  .0,  .5 ) if dist == 2 else
                    (0.35,  -1.0 ,  .0,  .25)
                )

                frame:

                    background None

                    xysize (480, 1080)
                    align (.5, 1.0)
                    offset (0, 6)

                    image item.body align (.5, 1.0) offset (0, 6):
                        at char_focus(zoom_val/2, bright_val, saturation_val, alpha)

                    at transform:
                        subpixel True
                        easein_quart .5 offset (sel_offset, 0)

        vbox:

            align (.0, .5)
            offset (46, 0)
            spacing 12

            for i in range(N):

                button:
                    style "gallery_char_button"

                    action [
                        SetScreenVariable("hovered_c", None),
                        ShowMenu('active_gallery', chars[i], _transition=None)
                    ]

                    hovered [
                        SetScreenVariable('sel_offset', infinite_offset(i)),
                        SetScreenVariable('sel_index', i),
                        SetScreenVariable('active_c', chars[i]),
                        SetScreenVariable("hovered_c", chars[i])
                    ]

                    xysize (437, 97)

                    frame:
                        xysize (437, 97)
                        image 'bin/assets/gallery/plate shadow.png' align (.0, .0) offset (-24, -18)
                        image 'bin/assets/gallery/plate.png' align (.5, .5)
                        image AlphaMask(chars[i].head, 'bin/assets/gallery/face prev.png') align (.0, .5) offset (-6, 0)
                        text chars[i].name.title() style "gallery_text_face" align (1.0, .5) offset (-32, 0)

                    at transform:

                        subpixel True

                        on idle:
                            easein_quart .5 matrixcolor BrightnessMatrix(.0) offset (0, 0)
                        on hover:
                            easein_quart .5 matrixcolor BrightnessMatrix(.125) offset (24, 0)

    for i in range(N):

        showif hovered_c is chars[i]:

            frame:
                background Solid("#00000000")
                xsize 400
                ysize 140
                xalign 1.0
                yalign 0.0
                xoffset -40
                yoffset 40

                at transform:
                    subpixel True
                    on show:
                        xoffset 120
                        alpha 0.0
                        easein_quart .6 xoffset -40 alpha 1.0
                    on hide:
                        xoffset -40
                        easein_quart .3 xoffset 120 alpha 0.0

                vbox:
                    xalign 0.5
                    yalign 0.2
                    spacing 8

                    text chars[i].full_name style "gallery_text_name" xalign 0.5

                    text "Points: [getattr(store, chars[i].name + 'point')]" style "gallery_text_points" xalign 0.5

                    text "Route: [('Yes' if getattr(store, chars[i].name + 'route') else 'No')]" style "gallery_text_route" xalign 0.5

    vbox:
        align  (1.0, 1.0)
        offset (-50, -50)
        spacing 8
        button:
            style "gallery_char_button"

            xysize (240, 64)

            background Solid('#16161680')

            text 'Specials' style "gallery_text_button" align (.5, .5)

            action ShowMenu('special')

            at transform:

                on idle:
                    easein_quart .5 matrixcolor InvertMatrix(.0)
                on hover:
                    easein_quart .5 matrixcolor InvertMatrix(1.0)

        button:
            style "gallery_char_button"

            xysize (240, 64)

            background Solid('#16161680')

            text 'Return' style "gallery_text_button" align (.5, .5)

            action Return()

            at transform:

                on idle:
                    easein_quart .5 matrixcolor InvertMatrix(.0)
                on hover:
                    easein_quart .5 matrixcolor InvertMatrix(1.0)


################################################################################
## Active Gallery Screen (per-character scene list)
################################################################################

screen active_gallery(character):

    tag menu

    key 'game_menu' action ShowMenu('gallery')

    add character.background

    add character.body:
        align (.5, .5)
        offset (0, 0)
        zoom .5
        at transform:
            easein_quart 1.25 offset (512, 0)

    button:
        style "gallery_char_button"
        align  (1.0, 1.0)
        offset (-50, -50)
        xysize (240, 64)

        background Solid('#16161680')

        text 'Return' style "gallery_text_button" align (.5, .5)

        action ShowMenu('gallery')

        at transform:

            on idle:
                easein_quart .5 matrixcolor InvertMatrix(.0)
            on hover:
                easein_quart .5 matrixcolor InvertMatrix(1.0)

    hbox:

        align  (.0, .0)
        offset (50, 50)
        spacing 8

        vpgrid id 'gallery':

            cols 3
            spacing 8
            xysize (None, 980)

            mousewheel 'vertical'
            draggable  True
            scrollbars None

            for x, y in enumerate(character.gallery):

                button:

                    xysize (308, 173)

                    action Replay(y.label)

                    image y.thumb xysize (308, 173):
                        align (.5, .5)
                        at transform:

                            on idle:
                                easein_quart .5 matrixcolor BrightnessMatrix(.0) blur 0
                            on hover:
                                easein_quart .5 matrixcolor BrightnessMatrix(.125) blur 0
                            on insensitive:
                                matrixcolor SaturationMatrix(.0) blur 30

                    at transform:
                        subpixel True
                        align (.5, .5)
                        alpha .0
                        zoom  .0
                        pause x * .1
                        easein_quart .5 alpha 1.0 zoom 1.0


################################################################################
## Specials Screen
################################################################################

define specials = [
    ("skypause", "skypause"),
    ("emmapause", "emmapause"),
    ("gwenpause", "gwenpause"),
    ("lilypause", "lilypause"),
    ("ainepause", "ainepause"),
    ("freyapause", "freyapause"),
    ("ainepause2", "ainepause2"),
    ("jessherapause", "jessherapause"),
    ("gwenpause2", "gwenpause2"),
    ("klaraherapause", "klaraherapause"),
    ("ainepause3", "ainepause3"),
    ("naomipause", "naomipause"),
    ("lilypause2", "lilypause2"),
    ("emmapause2", "emmapause2"),
    ("thunderchan3", "thunderchan3"),
    ("thunderchan2", "thunderchan2"),
    ("thunderchan4", "thunderchan4"),
    ("thunderchan", "thunderchan"),
    ("ainepause4", "ainepause4"),
    ("klarapause", "klarapause"),
    ("moonpause", "moonpause"),
    ("naomipause2", "naomipause2"),
    ("klarapause2", "klarapause2"),
    ("lilyannepause", "lilyannepause"),
    ("emmapause3", "emmapause3"),
    ("ainepause5", "ainepause5"),
    ("moonpause2", "moonpause2"),
    ("gwenpause3", "gwenpause3"),
    ("skypause2", "skypause2"),
    ("klarapause3", "klarapause3"),
    ("shupause", "shupause"),
    ("naomipause3", "naomipause3"),
    ("clairepause", "clairepause"),
    ("moonpause3", "moonpause3"),
    ("aoifepause", "aoifepause"),
    ("skypause3", "skypause3"),
]

transform special_feature_intro:
    subpixel True
    alpha 0.0
    xoffset 120
    easein_quart .45 alpha 1.0 xoffset 0

transform special_card_state(t=0.0):
    subpixel True
    alpha 0.0
    xoffset -40
    pause t
    easein_quart .35 alpha 1.0 xoffset 0

    on idle:
        easein_quart .35 matrixcolor BrightnessMatrix(.0) offset (0, 0)
    on hover:
        easein_quart .35 matrixcolor BrightnessMatrix(.125) offset (20, 0)
    on insensitive:
        matrixcolor SaturationMatrix(0.0) * BrightnessMatrix(-0.25)

transform special_button_fx:
    on idle:
        easein_quart .35 matrixcolor InvertMatrix(.0)
    on hover:
        easein_quart .35 matrixcolor InvertMatrix(1.0)
    on insensitive:
        matrixcolor SaturationMatrix(0.0) * BrightnessMatrix(-0.35)

transform special_scroll_fx:
    on idle:
        easein_quart .35 matrixcolor BrightnessMatrix(.0)
    on hover:
        easein_quart .35 matrixcolor BrightnessMatrix(.125)

transform special_preview_hover:
    on idle:
        easein_quart .35 matrixcolor BrightnessMatrix(.0)
    on hover:
        easein_quart .35 matrixcolor BrightnessMatrix(.15)
    on insensitive:
        matrixcolor SaturationMatrix(0.0) * BrightnessMatrix(-0.30)


screen special():

    modal True

    key "game_menu" action Hide("special")

    default special_entries = list(reversed(specials))
    default sel_special = 0
    default active_special = special_entries[0]

    add "bin/assets/gallery/gallery bg.png" align (.5, .5)
    add Solid("#00000040")

    # Title
    frame:
        background None
        align (.0, .0)
        offset (46, 42)
        xysize (460, 110)

        image "bin/assets/gallery/plate shadow.png" align (.0, .0) offset (-24, -12)
        image "bin/assets/gallery/plate.png" align (-.6, .0)

        text "Special Images" style "gallery_text_title" align (.42, .5)

    # Left list
    frame:
        background None
        align (.0, .5)
        offset (46, 80)
        xysize (520, 900)

        vpgrid id "special_list":

            cols 1
            spacing 12
            xysize (480, 820)

            mousewheel "vertical"
            draggable True
            scrollbars None

            for idx, entry in enumerate(special_entries):

                $ is_unlocked = renpy.seen_label(entry[0])

                button:
                    style "gallery_char_button"
                    xysize (460, 112)

                    sensitive is_unlocked
                    action Replay(entry[0])

                    hovered If(
                        is_unlocked,
                        true=[
                            SetScreenVariable("sel_special", idx),
                            SetScreenVariable("active_special", entry)
                        ],
                        false=None
                    )

                    frame:
                        background None
                        xysize (460, 112)

                        image "bin/assets/gallery/plate shadow.png" align (.0, .0) offset (-24, -12)
                        image "bin/assets/gallery/plate2.png" align (-.6, .0)

                        add AlphaMask(
                            Transform(entry[1], xysize=(430, 96), fit="cover"),
                            "bin/assets/gallery/plate2.png"
                        ):
                            align (.0, .0)
                            offset (-6, 0)
                            at special_preview_hover

                    at special_card_state()

        vbar value YScrollValue("special_list") base_bar Solid("#00000080") thumb Solid("#f1f1f1") xysize (16, 820):
            align (1.0, .5)
            at special_scroll_fx

    # Right preview panel
    frame:
        background None
        align (.82, .5)
        xysize (760, 900)
        at special_feature_intro

        if renpy.seen_label(active_special[0]):

            add Transform(active_special[1], xysize=(580, 650), fit="cover", align=(.73, .5))

        else:

            add Solid("#00000090") align (.73, .5) xysize (580, 650)

            text "Locked" style "gallery_text_locked" align (.73, .5)

            text "Preview hidden" style "gallery_text_locked_sub" align (.73, .5) offset (0, 42)

    # Return
    button:
        style "gallery_char_button"
        align (1.0, 1.0)
        offset (-50, -50)
        xysize (240, 64)

        background Solid("#16161680")

        text "Return" style "gallery_text_button" align (.5, .5)

        action [Hide("special"), With(Dissolve(.25))]

        at special_button_fx

style mm_text_button is default:
    font "bin/assets/faces/CoquetteBold.ttf"
    size 32
    color "#ffd1d1"

style mm_text_social is default:
    font "bin/assets/faces/CoquetteBold.ttf"
    size 32
    color "#ffd1d1"


screen _scr_mm_btn(action, text):

    button:
        style "gallery_char_button"
        xysize (208, 48)
        align  (.5 , .5)

        action action

        image 'bin/assets/main menu/mm_btn.png' align (.5, .5):
            at transform:
                subpixel True
                alpha .0
                zoom  .0
                on idle:
                    easein_quart .3 alpha .0 zoom .0
                on hover:
                    easein_quart .3 alpha 1.0 zoom 1.0
                on selected_idle:
                    parallel:
                        easein_quart .3 alpha 1.0 zoom 1.0
                    parallel:
                        ease 2.5 u_intensity 2.0
                        ease 2.5 u_intensity .0
                        repeat
                on selected_hover:
                    parallel:
                        easein_quart .3 alpha 1.0 zoom 1.0
                    parallel:
                        ease 2.5 u_intensity 2.0
                        ease 2.5 u_intensity .0
                        repeat

        text text style "mm_text_button" align (.5, .5):
            at transform:
                on idle:
                    easein_quart .5 matrixcolor InvertMatrix(.0)
                on hover:
                    easein_quart .5 matrixcolor InvertMatrix(1.0)

        at transform:

            shader "rgb_jitter"
            u_intensity .0

            subpixel True

            on idle:
                easein_quart .5 u_intensity .0
            on hover:
                u_intensity 10.0
                easein_quart .5 u_intensity .0

screen _scr_mm_soc(action, icon):

    button:
        style "gallery_char_button"
        xysize (48, 48)
        align  (.5, .5)

        action action

        image 'bin/assets/main menu/[icon].png' align (.5, .5) xysize (48, 48):
            at transform:
                subpixel True
                on idle:
                    easein_quart .5 zoom 1.0
                on hover:
                    easein_quart .5 zoom 1.15

        text icon.title() style "mm_text_social" align (.5, .5):
            at transform:
                subpixel True
                alpha .0
                rotate 270
                on idle:
                    easein_quart .5 offset (0, 40) alpha .0
                on hover:
                    easein_quart .5 offset (0, 100) alpha 1.0

transform ui_fadein:
    alpha 0.0
    easein_quart 2.0 alpha 1.0

transform null_transform:
    pass

transform mm_screen_fadein:
    alpha 1.0
    easein_quart 1.0 alpha 0.0

screen main_menu():

    tag menu

    fixed:
        add "bg_mainmenu_movie"
        if not renpy.session.get('mm_intro_done', False):
            add Solid("#000") at mm_screen_fadein
            timer 1.0 action Function(renpy.session.update, {'mm_intro_done': True})

    if not renpy.session.get('mm_ui_visible', False):
        button:
            xysize (1920, 1080)
            background None
            action [Function(renpy.session.update, {'mm_ui_visible': True}), RestartStatement()]

    if renpy.session.get('mm_ui_visible', False):

        image 'bin/assets/main menu/overlay.png' align (.5, .5) at ui_fadein
        image 'bin/assets/main menu/logo.png' align (.0, 1.0) offset (50, -50) at ui_fadein

        hbox:
            align  (.0, .0)
            offset (50, 50)
            spacing 24
            at ui_fadein

            use _scr_mm_soc(OpenURL('http://patreon.com/NiiChan029'), 'patreon')
            use _scr_mm_soc(OpenURL('http://discord.gg/a3HZsV2'), 'discord')
            use _scr_mm_soc(OpenURL('https://subscribestar.adult/niichan'), 'subscribestar')

        hbox:
            align  (1.0, .0)
            offset (-50, 50)
            spacing 24
            at ui_fadein

            use _scr_mm_btn(Start(), 'Start')
            use _scr_mm_btn(ShowMenu('load'), 'Load')
            use _scr_mm_btn(ShowMenu("gallery"), 'Gallery')
            use _scr_mm_btn(ShowMenu('preferences'), 'Settings')
            use _scr_mm_btn(ShowMenu('about'), 'About')

        if renpy.variant("pc"):
            frame:
                background None
                align (1.0, 1.0)
                offset (-50, -50)
                at ui_fadein

                use _scr_mm_btn(Quit(confirm=False), 'Quit')

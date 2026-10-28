screen game_menu(title, scroll=None, yinitial=0.0):

    tag menu

    key 'game_menu' action Return()

    add "bg_mainmenu_movie"
    add Solid("#cfc4e0b2")

    image 'bin/assets/main menu/overlay.png' align (.5, .5)

    #image 'bin/assets/main menu/logo.png' align (.0, 1.0) offset (50, -50)

    hbox:
        align  (.0, .0)
        offset (50, 50)
        spacing 24

        #use _scr_mm_soc(OpenURL('http://patreon.com/NiiChan029'), 'patreon')
        #use _scr_mm_soc(OpenURL('http://discord.gg/a3HZsV2'), 'discord')

        # Return button lives with the social buttons on the left
        # so it doesn't shift the nav buttons out of alignment.
        use _scr_mm_btn(Return(), 'Return')
        if not main_menu:
            use _scr_mm_btn(MainMenu(confirm=True), 'Main Menu')
        elif _in_replay:
            use _scr_mm_btn(EndReplay(confirm=True), 'End Replay')

    # Shared nav buttons — same order, count, and position as main menu
    hbox:
        align  (1.0, .0)
        offset (-50, 50)
        spacing 24

        if main_menu:
            use _scr_mm_btn(Start(), 'Start')
        else:
            use _scr_mm_btn(ShowMenu('save'), 'Save')
        use _scr_mm_btn(ShowMenu('load'), 'Load')
        use _scr_mm_btn(ShowMenu("gallery"), 'Gallery')
        use _scr_mm_btn(ShowMenu('preferences'), 'Settings')
        use _scr_mm_btn(ShowMenu('about'), 'About')

    frame:

        background None
        xysize (1820, 882)
        align  (.5  , 1.0)
        offset (0   , -50)

        if scroll == "viewport":

            viewport:
                yinitial yinitial
                scrollbars "vertical"
                mousewheel True
                draggable True
                pagekeys True

                side_yfill True

                vbox:
                    transclude

        elif scroll == "vpgrid":

            vpgrid:
                cols 1
                yinitial yinitial

                scrollbars "vertical"
                mousewheel True
                draggable True
                pagekeys True

                side_yfill True

                transclude

        else:

            transclude

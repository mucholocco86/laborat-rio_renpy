################################################################################
## Initialization
################################################################################

init offset = -1

################################################################################
## Styles
################################################################################

style default:
    properties gui.text_properties()
    language gui.language
    outlines [(0, "#000000", 1, 1)]

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")

style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5

style say_label:
    outlines [(0, "#ffffff", 1, 1)]

style label_text is gui_text:
    properties gui.text_properties("label", accent=True)
    outlines [(0, "#ffffff", 1, 1)]

style prompt_text is gui_text:
    properties gui.text_properties("prompt")

style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size + 5
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"

style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)

################################################################################
## In-game screens
################################################################################

## Say screen ##################################################################
##
## The say screen is used to display dialogue to the player. It takes two
## parameters, who and what, which are the name of the speaking character and
## the text to be displayed, respectively. (The who parameter can be None if no
## name is given.)
##
## This screen must create a text displayable with id "what", as Ren'Py uses
## this to manage text display. It can also create displayables with id "who"
## and id "window" to apply style properties.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):
    style_prefix "say"

    window:
        id "window"
        at Transform(alpha=0.0 if hud_cycle_state == 2 else 1.0)

        # This takes your PNG and applies the slider value to it
        background Transform("gui/textbox/textbox.png", alpha=persistent.text_box_opacity)

        if who is not None:
            window:
                id "namebox"
                style "namebox"

                # Adjust the value higher (e.g., 0.6) to move it lower
                yalign 0.2

                text who id "who"

        text what id "what"


    if hud_cycle_state != 2 and not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0

## Make the namebox available for styling through the Character object.
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label

style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos

## Input screen ################################################################
##
## This screen is used to display renpy.input. The prompt parameter is used to
## pass a text prompt in.
##
## This screen must create an input displayable with id "input" to accept the
## various input parameters.
##
## https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    on "show" action Function(show_osk_if_controller)

    if osk_visible():

        frame:
            background Solid("#0a050fcc")
            xfill True
            ypos 0
            padding (60, 28)

            vbox:
                xalign 0.5
                spacing 18

                text prompt:
                    xalign 0.5
                    color "#f0e8f5"
                    size 36
                    font gui.interface_text_font

                # Active-input indicator: input + a cyan underline bar.
                vbox:
                    xalign 0.5
                    spacing 4

                    input id "input":
                        xalign 0.5
                        color "#4ceefc"
                        size 32

                    frame:
                        background Solid("#4ceefc")
                        xsize 360
                        ysize 3
                        xalign 0.5

    else:

        window:

            vbox:
                xalign gui.dialogue_text_xalign
                xpos gui.dialogue_xpos
                xsize gui.dialogue_width
                ypos gui.dialogue_ypos

                text prompt style "input_prompt"
                input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width

## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    style_prefix "choice"

    if hud_cycle_state != 2:

        vbox:
            for i in items:
                ## Prepend a small bullet to options the player has previously
                ## picked at this exact menu (any save). See game/choice_tracker.rpy.
                $ _cx_marker = u"{color=#d10089}•{/color}  " if cx_is_seen(i.caption) else u""
                textbutton (_cx_marker + "[i.caption!t]"):
                    action [Function(cx_record_choice, i.caption), i.action]
                    xpos 0 + (items.index(i) * -50)

init -1 style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.98
    ypos 1000
    yanchor 1.0

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.text_properties("choice_button")

## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.

screen quick_menu():

    ## Ensure this appears on top of other screens.
    zorder 100

    ## Keyboard shortcuts listed in Preferences > Controls.
    key "K_h" action Function(cycle_hud_state)
    key "mousedown_2" action Function(cycle_hud_state)
    key "K_p" action ShowMenu("save")
    key "K_l" action ShowMenu("load")
    key "K_a" action Preference("auto-forward", "toggle")

    if quick_menu and hud_cycle_state == 0:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0
            yoffset -4
            spacing 28

            textbutton _("Back") action Rollback()
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Save") action ShowMenu('save')
            textbutton _("Q.Save") action QuickSave()
            textbutton _("Q.Load") action QuickLoad()
            textbutton _("Prefs") action ShowMenu('preferences')

## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
init python:
    def cycle_hud_state():
        store.hud_cycle_state = (store.hud_cycle_state + 1) % 3
        renpy.restart_interaction()

    config.overlay_screens.append("quick_menu")

default quick_menu = True
default hud_cycle_state = 0

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.button_text_properties("quick_button")
    size 20
    kerning 1.2
    idle_color "#c2c2ce"
    hover_color "#ff54b8"
    selected_idle_color "#4ceefc"
    selected_hover_color "#ff54b8"
    insensitive_color "#5a5a66"
    outlines [(2, "#05020a80", 0, 0)]

################################################################################
## Main and Game Menu Screens
################################################################################

init -10 python:
    _NAV_GLASS_RECT = (0, 0, 395, 1080)
    _HEADER_GLASS_RECT = (0, 0, 1920, 60)

    _OUTER_GLASS_SOURCE = "gui/gallery_menu.png"

    def _make_glass(rect):
        return Composite(
            (rect[2], rect[3]),
            (0, 0), Crop(rect, Transform(_OUTER_GLASS_SOURCE, blur=24)),
            (0, 0), Solid("#05020a9d"),
            (0, 0), Solid("#b566d900"),
        )

    NAV_GLASS_BG = _make_glass(_NAV_GLASS_RECT)
    HEADER_GLASS_BG = _make_glass(_HEADER_GLASS_RECT)
    GALLERY_BG = _make_glass((0, 0, 1920, 1080))

    def _vgrad(width, height, top_hex, bot_hex, steps=60):
        top = Color(top_hex)
        bot = Color(bot_hex)
        args = [(width, height)]
        denom = float(max(1, steps - 1))
        band_h = int(round(height / float(steps))) + 1
        for i in range(steps):
            t = i / denom
            c = top.interpolate(bot, t)
            y = int(round(i * height / float(steps)))
            args.append((0, y))
            args.append(Solid(c.hexcode, xysize=(width, band_h)))
        return Composite(*args)

    NAV_EDGE_GRADIENT = _vgrad(1, 1080, "#4ceefc", "#d10089")
    INNER_SIDEBAR_EDGE_GRADIENT = _vgrad(1, 1080, "#d10089", "#4ceefc")

    def _hgrad(width, height, stops, steps=120):
        if len(stops) < 2:
            raise ValueError("_hgrad requires at least two colour stops")
        colors = [Color(s) for s in stops]
        args = [(width, height)]
        denom = float(max(1, steps - 1))
        band_w = int(round(width / float(steps))) + 1
        seg_count = len(colors) - 1
        for i in range(steps):
            t = i / denom
            seg_t = t * seg_count
            seg_i = min(int(seg_t), seg_count - 1)
            local_t = seg_t - seg_i
            c = colors[seg_i].interpolate(colors[seg_i + 1], local_t)
            x = int(round(i * width / float(steps)))
            args.append((x, 0))
            args.append(Solid(c.hexcode, xysize=(band_w, height)))
        return Composite(*args)

    HEADER_BG_GRADIENT = _hgrad(1920, 60, [
        "#0a0a14",
        "#15090f",
        "#120713",
    ], steps=1920)

    HEADER_EDGE_GRADIENT = _hgrad(1920, 1, [
        "#4ceefc", # left (cyan)
        "#d10089", # middle (pink/magenta)
        "#d1008900", # right (faded out)
    ])

    def _action_selected(a):
        """Safely query an Action's selected state for the magenta accent bar."""
        try:
            return bool(a.get_selected())
        except Exception:
            return False

screen outer_nav_pill(label, action, centered=False, xsize=None, default_focus=False):
    button:
        style "hnavigation_button"
        action action
        default_focus default_focus

        if xsize is not None:
            xsize xsize

        if centered:
            text label style "hnavigation_button_text" xalign 0.5 yalign 0.5
        else:
            hbox:
                spacing 14
                yalign 0.5

                if _action_selected(action):
                    add Solid("#d10089") xysize (3, 30)
                else:
                    null width 3 height 24

                text label style "hnavigation_button_text"

## Split into two completely separate screens so each is independently
## cached/predicted by Ren'Py.

screen main_menu_nav():

    vbox:
        # Align 0.0 is left/top, 1.0 is right/bottom
        # xalign 0.0 = Left, yalign 1.0 = Bottom
        xalign 0.0
        yalign 1.0

        xoffset 20
        yoffset -120

        spacing 10

        if not is_steam_build():

            imagebutton:
                idle ("gui/button/patreon.png")
                hover ("gui/button/patreon1.png")
                action OpenURL("https://patreon.valerianyx.com")

            imagebutton:
                idle ("gui/button/subscribestar.png")
                hover ("gui/button/subscribestar1.png")
                action OpenURL("https://subscribestar.valerianyx.com")

        imagebutton:
            idle ("gui/button/steam.png")
            hover ("gui/button/steam1.png")
            action OpenURL("https://steam.valerianyx.com")

        imagebutton:
            idle ("gui/button/discord.png")
            hover ("gui/button/discord1.png")
            action OpenURL("https://discord.valerianyx.com")

        imagebutton:
            idle ("gui/button/website.png")
            hover ("gui/button/website1.png")
            action OpenURL("https://valerianyx.com")

    vbox:
        xalign 1.0
        yalign 1.0
        xoffset -60
        yoffset -100

        if all(renpy.seen_label(lbl) for lbl in GALLERY_LABELS):
            imagebutton:
                idle ("gui/button/Bikini.png")
                hover ("gui/button/Bikini1.png")
                action ToggleField(persistent, "alt_menu_bg")
                at transform:
                    rotate 8

    hbox:
        xalign 0.5
        yalign 0.95

        spacing 20

        use outer_nav_pill(_("START"), Start(), centered=True, xsize=220, default_focus=True)

        if cb_has_save():
            use outer_nav_pill(_("CONTINUE"), cb_continue_action(), centered=True, xsize=220)

        use outer_nav_pill(_("LOAD"), ShowMenu("load"), centered=True, xsize=220)

        use outer_nav_pill(_("GALLERY"), ShowMenu("girls_gallery"), centered=True, xsize=220)

        use outer_nav_pill(_("SETTINGS"), ShowMenu("preferences"), centered=True, xsize=220)

        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

            ## The quit button is banned on iOS and unnecessary on Android and
            ## Web.
            use outer_nav_pill(_("QUIT"), Quit(confirm=True), centered=True, xsize=220)

screen game_menu_nav():

    frame:
        xpos 0
        yfill True
        xsize 395
        padding (20, 140, 20, 30)
        background NAV_GLASS_BG

        side "t b":
            spacing 0

            vbox:
                spacing 8

                use outer_nav_pill(_("SAVE"), ShowMenu("save"))

                use outer_nav_pill(_("LOAD"), ShowMenu("load"))

                use outer_nav_pill(_("GALLERY"), ShowMenu("girls_gallery"))

                use outer_nav_pill(_("SETTINGS"), ShowMenu("preferences"))

                use outer_nav_pill(_("CREDITS"), ShowMenu("credits"))

                if _in_replay:

                    use outer_nav_pill(_("END REPLAY"), EndReplay(confirm=True))

                else:

                    use outer_nav_pill(_("MAIN MENU"), MainMenu())

                null height 18

                use outer_nav_pill(_("RETURN"), Return())

            vbox:
                spacing 8
                yalign 1.0

                if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

                    use outer_nav_pill(_("QUIT"), Quit(confirm=False))

    hbox:
        xalign 0.0
        yalign 1.0
        xoffset 14
        yoffset - 10
        spacing 10

        textbutton _("NEWS / UPDATES"):
            action OpenURL("https://valerianyx.com/news/")
            style "gm_footer_link"

        textbutton _("MUSIC"):
            action OpenURL("https://valerianyx.com/music/")
            style "gm_footer_link"

    add NAV_EDGE_GRADIENT xpos 394 ypos 0

screen prefs_nav_pill(label, tab_id):
    button:
        style "hnavigation_button"
        action SetVariable("pref_active_tab", tab_id)
        selected pref_active_tab == tab_id

        hbox:
            spacing 14
            yalign 0.5

            if pref_active_tab == tab_id:
                add Solid("#d10089") xysize (3, 30)
            else:
                null width 3 height 24

            text label style "hnavigation_button_text"

screen prefs_nav():

    frame:
        xpos 0
        yfill True
        xsize 395
        padding (20, 40, 20, 30)
        background NAV_GLASS_BG

        vbox:
            spacing 0

            text _("PREFERENCES") style "game_menu_label_text" xpos 14
            null height 10
            add Solid("#d100894d") xsize 320 ysize 1
            null height 22

            vbox:
                spacing 8

                use prefs_nav_pill(_("DISPLAY"),       "display")
                use prefs_nav_pill(_("READING"),       "reading")
                if config.has_music or config.has_sound or config.has_voice:
                    use prefs_nav_pill(_("AUDIO"),     "audio")
                use prefs_nav_pill(_("CONTROLS"),      "controls")
                use prefs_nav_pill(_("ACCESSIBILITY"), "accessibility")
                use prefs_nav_pill(_("STATS"),         "stats")
                if ANALYTICS_AVAILABLE:
                    use prefs_nav_pill(_("PRIVACY"),   "privacy")
                use prefs_nav_pill(_("SYSTEM"),        "system")

                null height 18
                add Solid("#d100894d") xsize 320 ysize 1
                null height 12

                if main_menu:
                    use outer_nav_pill(_("RETURN"), Return())
                elif _in_replay:
                    use outer_nav_pill(_("RETURN"), ShowMenu("replay_menu"))
                else:
                    use outer_nav_pill(_("RETURN"), ShowMenu("save"))

    add NAV_EDGE_GRADIENT xpos 394 ypos 0

style navigation_button is gui_button
style navigation_button_text is gui_button_text
style hnavigation_button is navigation_button
style hnavigation_button_text is navigation_button_text

style navigation_button:
    xsize 200
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")
    xalign 0.5

style hnavigation_button:
    background None
    hover_background Solid("#d1008922")
    selected_background Solid("#d1008938")
    selected_hover_background Solid("#d1008955")
    padding (14, 14)
    xsize 350

style hnavigation_button_text:
    color "#f0e8f5"
    hover_color "#ffffff"
    selected_color "#ffffff"
    selected_hover_color "#ffffff"
    insensitive_color "#8b7a99"
    size 24
    kerning 6
    outlines []
    font gui.interface_text_font
    xalign 0.0

style gm_footer_link is empty:
    background Solid("#96415214")
    hover_background Solid("#8d364746")
    padding (18, 12)

style gm_footer_link_text is gui_text:
    color "#d5c4e1"
    hover_color "#ffffff"
    size 19
    kerning 3
    outlines []
    font gui.interface_text_font

## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

image mm_scroll:
    contains:
        "gui/main_menu_scroll.png"
        xpos 0.0
    contains:
        "gui/main_menu_scroll.png"
        xpos -6144

    # Move the whole container
    subpixel True
    xpos 0.0
    linear 45.0 xpos -6144
    repeat

image mm_scroll_bikini:
    contains:
        "gui/main_menu_scroll_bikini.png"
        xpos 0.0
    contains:
        "gui/main_menu_scroll_bikini.png"
        xpos -6144

    # Move the whole container
    subpixel True
    xpos 0.0
    linear 45.0 xpos -6144
    repeat

## ── CONTINUE button helpers ──────────────────────────────────────────────
init -5 python:

    def cb_latest_slot():
        try:
            names = renpy.list_saved_games(fast=True)
        except Exception:
            return None
        latest = None
        latest_mtime = -1.0
        for n in names:
            if n.startswith("_"):
                continue
            try:
                mt = renpy.slot_mtime(n) or 0
            except Exception:
                mt = 0
            if mt > latest_mtime:
                latest_mtime = mt
                latest = n
        return latest

    def cb_has_save():
        return cb_latest_slot() is not None

    def cb_continue_action():
        slot = cb_latest_slot()
        if not slot:
            return None
        return FileLoad(slot, slot=True, confirm=False)

screen main_menu():

    ## This ensures that any other menu screen is replaced.
    tag menu

    ## Prevent screenshot hotkeys from firing while in menu UI.
    key "screenshot" action NullAction()

    ## Show the one-time anonymous-analytics disclosure on first launch.
    on "show" action If(ANALYTICS_AVAILABLE and not persistent.analytics_notice_shown, Show("analytics_notice"))

    style_prefix "main_menu"

    #add gui.main_menu_background
    #add "mm_scroll"
    if persistent.alt_menu_bg:
        add gui.main_menu_background #base image
        add "mm_scroll"#if you want scroll
    else:
        add gui.main_menu_background #image with bikini's
        add "mm_scroll_bikini"

    add "gui/button/Title.png":
        xalign 0.5      # Centers it horizontally
        ypos 700        # Adjust this number to move it up or down
        xanchor 0.5     # Ensures the center of the image is the pivot point

    ## This empty frame darkens the main menu.
    frame:
        pass

    ## The use statement includes another screen inside this one. The actual
    ## contents of the main menu are in the navigation screen.
    use main_menu_nav

    #if gui.show_name:

        #vbox:
            #textbutton(""):
                #area(100, 100, 550, 350)
                #background "gui/button/Title.png"
            #text "[config.name!t]":
                #style "main_menu_title"

            #text "[config.version]":
                #style "main_menu_version"

style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

#style main_menu_frame:
    #xsize 420
    #yfill True

    #background "gui/overlay/main_menu.png"

style main_menu_vbox:
    xalign 1.0
    xoffset -30
    xmaximum 1200
    yalign 1.0
    yoffset -30

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")

## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the background, title, and navigation.
##
## The scroll parameter can be None, or one of "viewport" or "vpgrid". When
## this screen is intended to be used with one or more children, which are
## transcluded (placed) inside it.

screen game_menu(title, scroll=None, yinitial=0.0):

    style_prefix "game_menu"

    ## Prevent screenshot hotkeys from firing while in menu UI.
    key "screenshot" action NullAction()

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        hbox:

            ## Reserve space for the navigation section.
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

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

    use game_menu_nav

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")

style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is hnavigation_button
style return_button_text is hnavigation_button_text

style game_menu_navigation_frame:
    xsize 395
    yfill True

style game_menu_content_frame:
    left_margin 0
    right_margin 0
    top_margin 0
    background Solid("#0a050fcc")

style game_menu_viewport:
    xsize 1380

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 0

style game_menu_label:
    xpos 75
    ysize 180

style game_menu_label_text:
    size 24
    color "#4ceefc"
    kerning 3
    outlines []
    font gui.interface_text_font
    yalign 0.5

style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size

## Load and Save screens #######################################################
##
## These screens are responsible for letting the player save the game and load
## it again. The actual layout (folder sidebar + scrollable slot grid) lives
## in `save_browser.rpy` so it can be iterated on or reverted without
## touching the rest of `screens.rpy`.
##
## https://www.renpy.org/doc/html/screen_special.html#save
## https://www.renpy.org/doc/html/screen_special.html#load

screen save():

    tag menu

    on "show" action Function(intertwined_set_pause_screen, "save")

    use sf_save_browser(mode="save")

screen load():

    tag menu

    on "show" action Function(intertwined_set_pause_screen, "load")

    use sf_save_browser(mode="load")

## Replay landing screen #######################################################

screen replay_menu():

    tag menu

    on "show" action Function(intertwined_set_pause_screen, "replay_menu")

    use game_menu(_("Replay")):

        $ replay_display = (_in_replay or "").replace("_", " ")

        frame:
            background None
            xfill True
            yfill True

            vbox:
                xalign 0.5
                yalign 0.5
                spacing 14

                text _("CURRENTLY REPLAYING") style "game_menu_label_text" xalign 0.5
                text "[replay_display]":
                    xalign 0.5
                    size 32
                    color "#f0e8f5"
                    font gui.interface_text_font
                    kerning 4

                null height 36

                text _("Use END REPLAY in the side menu to exit the replay, or RETURN to resume it."):
                    xalign 0.5
                    text_align 0.5
                    size 18
                    color "#bbbbbb"
                    xmaximum 600

style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 75
    ypadding 5

style page_label_text:
    text_align 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.button_text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.button_text_properties("slot_button")

## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

## NOTE: `screen preferences()` has been moved to its own file:
##           game/preferences.rpy

style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 3

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 338

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style radio_button_text:
    properties gui.button_text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.button_text_properties("check_button")

style slider_slider:
    xsize 525

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize 675

## History screen ##############################################################
##
## This is a screen that displays the dialogue history to the player. While
## there isn't anything special about this screen, it does have to access the
## dialogue history stored in _history_list.
##
## https://www.renpy.org/doc/html/history.html

screen history():

    tag menu

    ## Avoid predicting this screen, as it can be very large.
    predict False

    use game_menu(_("History"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0):

        style_prefix "history"

        for h in _history_list:

            window:

                ## This lays things out properly if history_height is None.
                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"

                        ## Take the color of the who text from the Character, if
                        ## set.
                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what

        if not _history_list:
            label _("The dialogue history is empty.")

## This determines what tags are allowed to be displayed on the history screen.

define gui.history_allow_tags = set()

style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5

## Help screen #################################################################
##
## A screen that gives information about key and mouse bindings. It uses other
## screens (keyboard_help, mouse_help, and gamepad_help) to display the actual
## help.

screen help():

    tag menu

    default device = "keyboard"

    use game_menu(_("Help"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 23

            hbox:

                textbutton _("Keyboard") action SetScreenVariable("device", "keyboard")
                textbutton _("Mouse") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help

screen keyboard_help():

    hbox:
        label _("Enter")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Space")
        text _("Advances dialogue without selecting choices.")

    hbox:
        label _("Arrow Keys")
        text _("Navigate the interface.")

    hbox:
        label _("Escape")
        text _("Accesses the game menu.")

    hbox:
        label _("Ctrl")
        text _("Skips dialogue while held down.")

    hbox:
        label _("Tab")
        text _("Toggles dialogue skipping.")

    hbox:
        label _("Page Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Page Down")
        text _("Rolls forward to later dialogue.")

    hbox:
        label "H"
        text _("Hides the user interface.")

    hbox:
        label "S"
        text _("Takes a screenshot.")

    hbox:
        label "V"
        text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")

screen mouse_help():

    hbox:
        label _("Left Click")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Middle Click")
        text _("Hides the user interface.")

    hbox:
        label _("Right Click")
        text _("Accesses the game menu.")

    hbox:
        label _("Mouse Wheel Up\nClick Rollback Side")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Mouse Wheel Down")
        text _("Rolls forward to later dialogue.")

screen gamepad_help():

    hbox:
        label _("Right Trigger\nA/Bottom Button")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Left Trigger\nLeft Shoulder")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Right Shoulder")
        text _("Rolls forward to later dialogue.")

    hbox:
        label _("D-Pad, Sticks")
        text _("Navigate the interface.")

    hbox:
        label _("Start, Guide")
        text _("Accesses the game menu.")

    hbox:
        label _("Y/Top Button")
        text _("Hides the user interface.")

    textbutton _("Calibrate") action GamepadCalibrate()

style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 12

style help_button_text:
    properties gui.button_text_properties("help_button")

style help_label:
    xsize 375
    right_padding 30

style help_label_text:
    size gui.text_size
    xalign 1.0
    text_align 1.0

################################################################################
## Additional screens
################################################################################

## Confirm screen ##############################################################
##
## The confirm screen is called when Ren'Py wants to ask the player a yes or no
## question.
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 45

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 150

                textbutton _("Yes") action yes_action
                textbutton _("No") action no_action

    ## Right-click and escape answer "no".
    key "game_menu" action no_action

style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    text_align 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.button_text_properties("confirm_button")

## Skip indicator screen #######################################################
##
## The skip_indicator screen is displayed to indicate that skipping is in
## progress.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 9

            text _("Skipping")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"

## This transform is used to blink the arrows one after another.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat

style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/textbox/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## We have to use a font that has the BLACK RIGHT-POINTING SMALL TRIANGLE
    ## glyph in it.
    font "DejaVuSans.ttf"

## Notify screen ###############################################################
##
## The notify screen is used to show the player a message. (For example, when
## the game is quicksaved or a screenshot has been taken.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')

transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0

style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/textbox/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")

## NVL screen ##################################################################
##
## This screen is used for NVL-mode dialogue and menus.
##
## https://www.renpy.org/doc/html/screen_special.html#nvl

screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## Displays dialogue in either a vpgrid or the vbox.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## Displays the menu, if given. The menu may be displayed incorrectly if
        ## config.narrator_menu is set to True, as it is above.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0

screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id

## This controls the maximum number of NVL-mode entries that can be displayed at
## once.
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/textbox/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    text_align gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    text_align gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.button_text_properties("nvl_button")

################################################################################
## Mobile Variants
################################################################################

style pref_vbox:
    variant "medium"
    xsize 675

## Since a mouse may not be present, we replace the quick menu with a version
## that uses fewer and bigger buttons that are easier to touch.
screen quick_menu():
    variant "touch"

    zorder 100

    ## Keep keyboard behavior consistent across variants.
    key "K_h" action Function(cycle_hud_state)
    key "mousedown_2" action Function(cycle_hud_state)
    key "K_p" action ShowMenu("save")
    key "K_l" action ShowMenu("load")
    key "K_a" action Preference("auto-forward", "toggle")

    if quick_menu and hud_cycle_state == 0:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0
            spacing 28

            textbutton _("Back") action Rollback()
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Prefs") action ShowMenu('preferences')
            textbutton _("Menu") action ShowMenu()

style window:
    variant "small"
    background "gui/phone/textbox.png"

style radio_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 510

style game_menu_content_frame:
    variant "small"
    top_margin 0

style pref_vbox:
    variant "small"
    xsize 600

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_pref_vbox:
    variant "small"
    xsize None

style slider_pref_slider:
    variant "small"
    xsize 900

################################################################################
## On-screen keyboard (fallback for controller users on non-Steam builds)
################################################################################
##
## Shown via osk_activate_for() when a text input is activated while a
## controller is plugged in on a non-Steam build. Steam builds let the Steam
## overlay handle it; desktop+keyboard users just type normally.

screen onscreen_keyboard():
    tag onscreen_keyboard
    zorder 500
    modal True

    default osk_shift = False

    frame:
        style "osk_frame"
        align (0.5, 0.92)

        has vbox
        spacing 8
        xalign 0.5

        # Row 1 - digits
        hbox:
            xalign 0.5
            spacing 6
            for ch in "1234567890":
                textbutton "[ch]":
                    action [Function(osk_append, ch), SetScreenVariable("osk_shift", False)]
                    style "osk_button"

        # Row 2 - qwerty
        hbox:
            xalign 0.5
            spacing 6
            for ch in "qwertyuiop":
                $ glyph = ch.upper() if osk_shift else ch
                textbutton "[glyph]":
                    action [Function(osk_append, glyph), SetScreenVariable("osk_shift", False)]
                    style "osk_button"

        # Row 3 - asdf
        hbox:
            xalign 0.5
            spacing 6
            for ch in "asdfghjkl":
                $ glyph = ch.upper() if osk_shift else ch
                textbutton "[glyph]":
                    action [Function(osk_append, glyph), SetScreenVariable("osk_shift", False)]
                    style "osk_button"

        # Row 4 - shift / zxcv / del
        hbox:
            xalign 0.5
            spacing 6
            textbutton _("SHIFT"):
                action ToggleScreenVariable("osk_shift")
                selected osk_shift
                style "osk_button_special"
            for ch in "zxcvbnm":
                $ glyph = ch.upper() if osk_shift else ch
                textbutton "[glyph]":
                    action [Function(osk_append, glyph), SetScreenVariable("osk_shift", False)]
                    style "osk_button"
            textbutton _("DEL"):
                action Function(osk_backspace)
                style "osk_button_special"

        # Row 5 - space / done
        hbox:
            xalign 0.5
            spacing 6
            textbutton _("SPACE"):
                action [Function(osk_append, " "), SetScreenVariable("osk_shift", False)]
                style "osk_button_space"
            textbutton _("DONE"):
                action Function(osk_done)
                style "osk_button_special"

style osk_frame is empty:
    background Solid("#0a050fee")
    padding (28, 22)

style osk_button is empty:
    background Solid("#1a0d28")
    hover_background Solid("#4ceefc")
    xsize 60
    ysize 52

style osk_button_text is gui_text:
    color "#f0e8f5"
    hover_color "#0a050f"
    size 24
    xalign 0.5
    yalign 0.5
    font gui.interface_text_font

style osk_button_special is osk_button:
    xsize 110
    selected_background Solid("#d10089")

style osk_button_special_text is osk_button_text:
    size 18
    kerning 3
    color "#f0e8f5"
    selected_color "#f0e8f5"

style osk_button_space is osk_button:
    xsize 420

style osk_button_space_text is osk_button_text:
    size 18

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


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

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
    ysize gui.slider_size
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

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what" size persistent.text_size line_spacing persistent.text_spacing kerning persistent.text_kerning


    ## If there's a side image, display it above the text. Do not display on the
    ## phone variant - there's no room.
    if not renpy.variant("small"):
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

    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

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

    vbox:
        for i in items:
            textbutton i.caption action i.action


## When this is true, menu captions will be spoken by the narrator. When false,
## menu captions will be displayed as empty buttons.
define config.narrator_menu = True


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 405
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")


## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.
init:
    transform customzoom:
        zoom 0.7

screen quick_menu():

    ## Ensure this appears on top of other screens.
    zorder 100

    if quick_menu:

        imagebutton:
            xpos 1836
            ypos 711
            auto "gui/button/quick_menu/auto_%s.png"
            action Rollback()
            at transform:
                rotate 180

        imagebutton:
            xpos 1795
            ypos 785
            auto "gui/button/quick_menu/auto_%s.png"
            action Preference("auto-forward", "toggle")

        imagebutton:
            xpos 1850
            ypos 785
            auto "gui/button/quick_menu/skip_%s.png"
            action Skip() alternate Skip(fast=True, confirm=True)

        imagebutton:
            xpos 1850
            ypos 845
            auto "gui/button/quick_menu/load_%s.png"
            action ShowMenu('load')

        imagebutton:
            xpos 1795
            ypos 845
            auto "gui/button/quick_menu/save_%s.png"
            action ShowMenu('save')

        imagebutton:
            xpos 1795
            ypos 905
            auto "gui/button/quick_menu/qs_%s.png"
            action QuickSave()

        imagebutton:
            xpos 1850
            ypos 905
            auto "gui/button/quick_menu/ql_%s.png"
            action QuickLoad()

        imagebutton:
            xpos 1795
            ypos 965
            auto "gui/button/quick_menu/history_%s.png"
            action HideInterface()

        imagebutton:
            xpos 1850
            ypos 965
            auto "gui/button/quick_menu/settings_%s.png"
            action ShowMenu('preferences')

        if _in_replay:
            imagebutton:
                xpos 1730
                ypos 1020
                auto "gui/button/quick_menu/end_%s.png"
                action EndReplay(confirm=True)
                at customzoom


## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.button_text_properties("quick_button")


################################################################################
## Main and Game Menu Screens
################################################################################

## Navigation screen ###########################################################
##
## This screen is included in the main and game menus, and provides navigation
## to other menus, and to start the game.

screen navigation():

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.5

        spacing gui.navigation_spacing

        if main_menu:

            textbutton _("Start") action Start()

        else:

            textbutton _("History") action ShowMenu("history")

            textbutton _("Save") action ShowMenu("save")

        textbutton _("Load") action ShowMenu("load")

        textbutton _("Preferences") action ShowMenu("preferences")

        if _in_replay:

            textbutton _("End Replay") action EndReplay(confirm=True)

        elif not main_menu:

            textbutton _("Main Menu") action MainMenu()

        textbutton _("About") action ShowMenu("about")

        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

            ## Help isn't necessary or relevant to mobile devices.
            textbutton _("Help") action ShowMenu("help")

        if renpy.variant("pc"):

            ## The quit button is banned on iOS and unnecessary on Android and
            ## Web.
            textbutton _("Quit") action Quit(confirm=not main_menu)


style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")


## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

#screen main_menu():
#    tag menu # This ensures that any other menu screen is replaced.
#    add Movie(play="gui/main_menu.webm", loop=True, size=(1920,1080)) # Adds background image for the main menu
#
#    #Imagebutton code
#    imagebutton auto "gui/button/start_%s.png" xpos 840 ypos 920 focus_mask True action [Start(), Play("sound9", "audio/click.ogg")] idle "gui/button/start_%s.png" hover "gui/button/starth_%s.png" hovered Play("sound9", "audio/switchclick.mp3")
#    imagebutton auto "gui/button/load_%s.png" xpos  1050 ypos 920 focus_mask True  action [ShowMenu('load'), Play("sound9", "audio/click.ogg")] idle "gui/button/load_%s.png" hover "gui/button/loadh_%s.png" hovered Play("sound9", "audio/switchclick.mp3")
#    imagebutton auto "gui/button/pref_%s.png" xpos 1260 ypos 920 focus_mask True action [ShowMenu('preferences'), Play("sound9", "audio/click.ogg")] idle "gui/button/pref_%s.png" hover "gui/button/prefh_%s.png" hovered Play("sound9", "audio/switchclick.mp3")
#    imagebutton auto "gui/button/about_%s.png" xpos 1470 ypos 920 focus_mask True action [ShowMenu('about'), Play("sound9", "audio/click.ogg")] idle "gui/button/about_%s.png" hover "gui/button/abouth_%s.png" hovered Play("sound9", "audio/switchclick.mp3")
#    imagebutton auto "gui/button/quit_%s.png" xpos 1680 ypos 920 focus_mask True action [Quit(confirm=False), Play("sound9", "audio/click.ogg")] idle "gui/button/quit_%s.png" hover "gui/button/quith_%s.png" hovered Play("sound9", "audio/switchclick.mp3")
#    imagebutton auto "gui/button/scenes_%s.png" xpos 1350 ypos 1000 focus_mask True action [ui.callsinnewcontext("call_gallery"), ShowMenu("gallery"), Play("sound9", "audio/click.ogg")] idle "gui/button/scenes_%s.png" hover "gui/button/scenesh_%s.png" hovered Play("sound9", "audio/switchclick.mp3")
#    imagebutton auto "gui/button/gallery_%s.png" xpos 1140 ypos 1000 focus_mask True action [ShowMenu("special"), Play("sound9", "audio/click.ogg")] idle "gui/button/gallery_%s.png" hover "gui/button/galleryh_%s.png" hovered Play("sound9", "audio/switchclick.mp3")
#
#    imagebutton:
#        idle "gui/dc.png"
#        hover "gui/dch.png"
#        hovered Play("sound", "audio/switchclick.mp3")
#        action [OpenURL("http://discord.gg/a3HZsV2"), Play("sound9", "audio/click.ogg")]
#        xalign .01
#        yalign .01
#    imagebutton:
#        idle "gui/patreon.png"
#        hover "gui/patreonh.png"
#        hovered Play("sound", "audio/switchclick.mp3")
#        action [OpenURL("http://patreon.com/NiiChan029"), Play("sound9", "audio/click.ogg")]
#        xalign .10
#        yalign .0005
#    imagebutton:
#        idle "gui/title.png"
#        xalign .03
#        yalign .87
#    imagebutton:
#        idle "gui/ep.png"
#        xalign .12
#        yalign .97
#    #imagebutton:
#        #idle "gui/button/juicetea.png"
#        #hover "gui/button/juiceteah.png"
#        #hovered Play("sound", "audio/switchclick.mp3")
#        #action [OpenURL("https://twitter.com/JuiceTeaMusic"), Play("sound9", "audio/click.ogg")]
#        #xalign .99
#        #yalign .01


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

    if main_menu:
        imagebutton auto "gui/button/start_%s.png" xpos 115 ypos 220 focus_mask True action [Start(), Play("sound9", "audio/click.ogg")] idle "gui/button/start_%s.png" hover "gui/button/starth_%s.png" hovered Play("sound9", "audio/switchclick.mp3")
    else:
        imagebutton auto "gui/button/save_%s.png" xpos 115 ypos 220 focus_mask True action [ShowMenu("save"), Play("sound9", "audio/click.ogg")] idle "gui/button/save_%s.png" hover "gui/button/saveh_%s.png" hovered Play("sound9", "audio/switchclick.mp3")

    imagebutton auto "gui/button/load_%s.png" xpos  115 ypos 320 focus_mask True  action [ShowMenu('load'), Play("sound9", "audio/click.ogg")]idle "gui/button/load_%s.png" hover "gui/button/loadh_%s.png" hovered Play("sound9", "audio/switchclick.mp3")
    imagebutton auto "gui/button/prefgm_%s.png" xpos 115 ypos 420 focus_mask True action [ShowMenu('preferences'), Play("sound9", "audio/click.ogg")] idle "gui/button/prefgm_%s.png" hover "gui/button/prefgmh_%s.png" hovered Play("sound9", "audio/switchclick.mp3")

    if not main_menu:
        imagebutton auto "gui/button/main_%s.png" xpos 115 ypos 520 focus_mask True action [MainMenu(), Play("sound9", "audio/click.ogg")] idle "gui/button/main_%s.png" hover "gui/button/mainh_%s.png" hovered Play("sound9", "audio/switchclick.mp3")
        imagebutton auto "gui/button/scenes_%s.png" xpos 115 ypos 620 focus_mask True action [ui.callsinnewcontext("call_gallery"), ShowMenu("gallery"), Play("sound9", "audio/click.ogg")] idle "gui/button/scenes_%s.png" hover "gui/button/scenesh_%s.png" hovered Play("sound9", "audio/switchclick.mp3")
        imagebutton auto "gui/button/about_%s.png" xpos 115 ypos 720 focus_mask True action [ShowMenu('about'), Play("sound9", "audio/click.ogg")] idle "gui/button/about_%s.png" hover "gui/button/abouth_%s.png" hovered Play("sound9", "audio/switchclick.mp3")
        imagebutton auto "gui/button/quit_%s.png" xpos 115 ypos 820 focus_mask True action [Quit(confirm=not main_menu), Play("sound9", "audio/click.ogg")] idle "gui/button/quit_%s.png" hover "gui/button/quith_%s.png" hovered Play("sound9", "audio/switchclick.mp3")
        imagebutton auto "gui/button/return_%s.png" xpos 115 ypos 950 focus_mask True action [Return(), Play("sound9", "audio/click.ogg")] idle "gui/button/return_%s.png" hover "gui/button/returnh_%s.png" hovered Play("sound9", "audio/switchclick.mp3")
    else:
        imagebutton auto "gui/button/scenes_%s.png" xpos 115 ypos 520 focus_mask True action [ui.callsinnewcontext("call_gallery"), ShowMenu("gallery"), Play("sound9", "audio/click.ogg")] idle "gui/button/scenes_%s.png" hover "gui/button/scenesh_%s.png" hovered Play("sound9", "audio/switchclick.mp3")
        imagebutton auto "gui/button/about_%s.png" xpos 115 ypos 620 focus_mask True action [ShowMenu('about'), Play("sound9", "audio/click.ogg")] idle "gui/button/about_%s.png" hover "gui/button/abouth_%s.png" hovered Play("sound9", "audio/switchclick.mp3")
        imagebutton auto "gui/button/quit_%s.png" xpos 115 ypos 720 focus_mask True action [Quit(confirm=not main_menu), Play("sound9", "audio/click.ogg")] idle "gui/button/quit_%s.png" hover "gui/button/quith_%s.png" hovered Play("sound9", "audio/switchclick.mp3")
        imagebutton auto "gui/button/return_%s.png" xpos 115 ypos 950 focus_mask True action [Return(), Play("sound9", "audio/click.ogg")] idle "gui/button/return_%s.png" hover "gui/button/returnh_%s.png" hovered Play("sound9", "audio/switchclick.mp3")

    hbox:
        xpos 365
        yalign 0.10
        spacing 30
        add "gui/icons/{}.png".format(title) yalign 0.5
        label title.upper()

style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 45
    top_padding 180

    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 420
    yfill True

style game_menu_content_frame:
    left_margin -30
    right_margin 30
    top_margin 20

style game_menu_viewport:
    xsize 1380

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 15

style game_menu_label_text:
    size 70
    color gui.accent_color
    kerning 10
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -45


## About screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.

screen about():

    tag menu

    default current_section = "summary"

    use game_menu(_("About")):

        style_prefix "about"

        fixed:

            # Section nav row, using the same radio-style buttons as the
            # preferences screen so visual language stays consistent.
            hbox:
                xalign 0.5
                yalign 0.0
                spacing 14

                imagebutton:
                    auto "gui/button/radio_%s_background.png"
                    foreground Text(_("Summary"), style="custom_btn_txt")
                    hover_foreground Text(_("Summary"), style="custom_btn_txt_hover")
                    selected_foreground Text(_("Summary"), style="custom_btn_txt_hover")
                    action SetScreenVariable("current_section", "summary")
                    selected (current_section == "summary")
                    at pref_button_float

                imagebutton:
                    auto "gui/button/radio_%s_background.png"
                    foreground Text(_("Special Thanks"), style="custom_btn_txt")
                    hover_foreground Text(_("Special Thanks"), style="custom_btn_txt_hover")
                    selected_foreground Text(_("Special Thanks"), style="custom_btn_txt_hover")
                    action SetScreenVariable("current_section", "thanks")
                    selected (current_section == "thanks")
                    at pref_button_float

                imagebutton:
                    auto "gui/button/radio_%s_background.png"
                    foreground Text(_("Soundtracks"), style="custom_btn_txt")
                    hover_foreground Text(_("Soundtracks"), style="custom_btn_txt_hover")
                    selected_foreground Text(_("Soundtracks"), style="custom_btn_txt_hover")
                    action SetScreenVariable("current_section", "ost")
                    selected (current_section == "ost")
                    at pref_button_float

                imagebutton:
                    auto "gui/button/radio_%s_background.png"
                    foreground Text(_("Info"), style="custom_btn_txt")
                    hover_foreground Text(_("Info"), style="custom_btn_txt_hover")
                    selected_foreground Text(_("Info"), style="custom_btn_txt_hover")
                    action SetScreenVariable("current_section", "info")
                    selected (current_section == "info")
                    at pref_button_float

            # Content viewport for the selected section.
            viewport:
                xalign 0.5
                yalign 1.0
                ysize 720
                xmaximum 1400
                mousewheel True
                draggable True

                vbox:
                    xalign 0.5
                    xmaximum 1340
                    spacing 12

                    label "[config.name!t]"

                    if current_section == "summary":
                        text gui.about_summary style "about_text"
                    elif current_section == "thanks":
                        text gui.about_thanks style "about_text"
                    elif current_section == "ost":
                        text gui.about_ost style "about_text"
                    else:
                        text _("Version [config.version!t]") style "about_text"
                        text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].") style "about_text"
                        text "[renpy.license!t]" style "about_text"


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text:
    size 24
    color "#2E2A3D"
    outlines []
    antialias True

style about_nav_button is default
style about_nav_button_text is default

style about_label_text:
    size gui.label_text_size
    color gui.slot_accent_color
    outlines []
    antialias True


style about_nav_button:
    background None
    xpadding 18
    ypadding 8

style about_nav_button_text:
    font gui.interface_text_font
    size 26
    color gui.slot_muted_color
    hover_color gui.slot_accent_color
    selected_color gui.slot_accent_strong
    outlines []
    antialias True

transform about_nav_hover:
    subpixel True

    on idle:
        easein_quart .25 matrixcolor BrightnessMatrix(0.0) yoffset 0

    on hover:
        easein_quart .25 matrixcolor BrightnessMatrix(.10) yoffset -3


## Load and Save screens #######################################################
##
## These screens are responsible for letting the player save the game and load
## it again. Since they share nearly everything in common, both are implemented
## in terms of a third screen, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load

screen save():

    tag menu

    use file_slots(_("Save"))


screen load():

    tag menu

    use file_slots(_("Load"))

transform slot_panel_in:
    subpixel True
    alpha 0.0
    easein_quart .20 alpha 1.0

transform slot_drop_in(delay=0.0):
    subpixel True
    alpha 0.0
    yoffset -70
    pause delay
    easein_quart .40 alpha 1.0 yoffset 0

transform slot_item_hover:
    subpixel True

    on idle:
        easein_quart .20 matrixcolor BrightnessMatrix(0.0) yoffset 0

    on hover:
        easein_quart .20 matrixcolor BrightnessMatrix(.08) yoffset -4

transform page_nav_in(delay=0.0):
    subpixel True
    alpha 0.0
    yoffset -14
    pause delay
    easein_quart .28 alpha 1.0 yoffset 0

# Hover for new save/load cards. Reverted to first strength.
transform new_slot_card_hover:
    subpixel True

    on idle:
        easein_quart .25 matrixcolor BrightnessMatrix(0.0) yoffset 0

    on hover:
        easein_quart .25 matrixcolor BrightnessMatrix(.08) yoffset -4

# Drop shadow that fades in on card hover.
transform new_slot_shadow_hover:
    subpixel True
    alpha 0.0

    on idle:
        easein_quart .35 alpha 0.0

    on hover:
        easein_quart .35 alpha 1.0

# Brighten only on arrow hover. Removing zoom: scaling the rounded pill
# was producing sub-pixel edge artifacts that read as crossing lines.
transform new_arrow_hover:
    subpixel True

    on idle:
        easein_quart .25 matrixcolor BrightnessMatrix(0.0)

    on hover:
        easein_quart .25 matrixcolor BrightnessMatrix(.18)

screen file_slots(title):

    default page_name_value = FilePageNameInputValue(
        pattern=_("Page {}"),
        auto=_("Automatic saves"),
        quick=_("Quick saves")
    )

    use game_menu(title):

        fixed:

            order_reverse True

            # Title block at top. Standalone, not wrapping grid (vbox was
            # collapsing grid to single column).
            vbox:
                xalign 0.5
                ypos -25
                spacing 4
                at slot_panel_in

                hbox:
                    xalign 0.5
                    spacing 16
                    add gui.slot_sparkle_lg yalign 0.5
                    text title:
                        style "new_slot_title"
                        yalign 0.5
                    add gui.slot_sparkle_lg yalign 0.5

                add gui.slot_divider xalign 0.5

                button:
                    style "new_page_label"
                    key_events True
                    xalign 0.5
                    action page_name_value.Toggle()

                    hbox:
                        spacing 8
                        yalign 0.5
                        add gui.slot_sparkle yalign 0.5
                        input:
                            style "new_page_label_text"
                            value page_name_value
                        add gui.slot_sparkle yalign 0.5

            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "new_slot"
                xalign 0.5
                yalign 0.45
                spacing gui.slot_spacing
                at slot_panel_in

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1
                    $ row = i // gui.file_slot_cols
                    $ col = i % gui.file_slot_cols

                    # Top row drops first, left to right.
                    $ slot_delay = (row * 0.08) + (col * 0.03)
                    $ slot_label = "%02d" % slot

                    button:
                        action FileAction(slot)
                        key "save_delete" action FileDelete(slot)
                        focus_mask True
                        at new_slot_card_hover
                        background None
                        xsize gui.slot_button_width
                        ysize gui.slot_button_height
                        padding (0, 0)

                        fixed:
                            xsize gui.slot_button_width
                            ysize gui.slot_button_height
                            at slot_drop_in(slot_delay)

                            # Drop shadow, fades in on hover
                            add Frame(gui.slot_card_shadow, gui.slot_card_shadow_borders, tile=False):
                                xsize (gui.slot_button_width + gui.slot_card_shadow_pad * 2)
                                ysize (gui.slot_button_height + gui.slot_card_shadow_pad * 2)
                                xpos -gui.slot_card_shadow_pad
                                ypos -gui.slot_card_shadow_pad
                                at new_slot_shadow_hover

                            # Frosted card bg
                            add Frame(gui.slot_card_bg, gui.slot_card_borders, tile=False):
                                xsize gui.slot_button_width
                                ysize gui.slot_button_height

                            fixed:
                                # Content area, with internal padding
                                xpos gui.slot_card_padding
                                ypos gui.slot_card_padding
                                xsize (gui.slot_button_width - gui.slot_card_padding * 2)
                                ysize (gui.slot_button_height - gui.slot_card_padding * 2)

                                if FileLoadable(slot):
                                    vbox:
                                        xalign 0.5
                                        yalign 0.0
                                        spacing 22

                                        add Transform(AlphaMask(FileScreenshot(slot), gui.slot_thumb_mask), zoom=1.06) xalign 0.5

                                        hbox:
                                            xalign 0.5
                                            spacing 36

                                            hbox:
                                                spacing 5
                                                add "gui/icons/icon_calendar.png" yalign 0.5
                                                text FileTime(slot, format=_("{#file_date}%b %d, %Y"), empty=""):
                                                    style "new_slot_footer"
                                                    yalign 0.5

                                            hbox:
                                                spacing 5
                                                add "gui/icons/icon_clock.png" yalign 0.5
                                                text FileTime(slot, format=_("{#file_clock}%H:%M"), empty=""):
                                                    style "new_slot_footer"
                                                    yalign 0.5

                                else:
                                    vbox:
                                        align (0.5, 0.5)
                                        spacing 8
                                        add "gui/icons/icon_box.png" xalign 0.5
                                        hbox:
                                            xalign 0.5
                                            spacing 6
                                            add gui.slot_sparkle yalign 0.5
                                            text _("Empty Slot"):
                                                style "new_slot_empty_label"
                                                yalign 0.5
                                            add gui.slot_sparkle yalign 0.5

                                # Slot number badge flush with thumbnail top-left.
                                frame:
                                    style "new_slot_badge"
                                    xpos 1
                                    ypos 0
                                    text slot_label style "new_slot_badge_text"

            frame:
                style "new_page_pill"
                xalign 0.5
                yalign 1.0
                yoffset -30
                at page_nav_in(.18)

                hbox:
                    style_prefix "new_page"
                    spacing 2

                    textbutton _("<"):
                        style "new_page_arrow"
                        action [FilePagePrevious(), With(gui.slot_page_xition)]
                        at new_arrow_hover

                    if config.has_autosave:
                        textbutton _("{#auto_page}A"):
                            action [FilePage("auto"), With(gui.slot_page_xition)]

                    if config.has_quicksave:
                        textbutton _("{#quick_page}Q"):
                            action [FilePage("quick"), With(gui.slot_page_xition)]

                    for page in range(1, 21):
                        textbutton "[page]":
                            action [FilePage(page), With(gui.slot_page_xition)]

                    textbutton _(">"):
                        style "new_page_arrow"
                        action [FilePageNext(), With(gui.slot_page_xition)]
                        at new_arrow_hover


# Legacy styles, left in place because other screens may inherit them
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


# New styles for reworked file_slots screen, namespaced new_*
style new_slot_title is default:
    font gui.slot_title_font
    size gui.slot_title_size
    color gui.slot_title_color
    bold False
    italic False
    outlines []
    antialias True

style new_page_label is default:
    xpadding 12
    ypadding 4

style new_page_label_text is default:
    font gui.interface_text_font
    size gui.slot_subtitle_size
    color gui.slot_muted_color
    hover_color gui.slot_accent_color
    text_align 0.5
    layout "subtitle"
    outlines []
    antialias True

style new_slot_button is default:
    xsize gui.slot_button_width
    ysize gui.slot_button_height

style new_slot_badge is default:
    background Frame(gui.slot_badge_bg, gui.slot_badge_borders, tile=False)
    xminimum 42
    yminimum 32
    xpadding 10
    ypadding 4

style new_slot_badge_text is default:
    font gui.interface_text_font
    size gui.slot_badge_size
    color gui.slot_badge_text_color
    bold True
    xalign 0.5
    yalign 0.5
    outlines []
    antialias True

style new_slot_footer is default:
    font gui.interface_text_font
    size gui.slot_footer_size
    color gui.slot_muted_color
    outlines []
    antialias True

style new_slot_empty_label is default:
    font gui.interface_text_font
    size gui.slot_empty_label_size
    color gui.slot_muted_color
    outlines []
    antialias True

style new_page_pill is default:
    background Frame(gui.slot_card_bg, gui.slot_card_borders, tile=False)
    xpadding 14
    ypadding 6

style new_page_button is default:
    xminimum 32
    yminimum 32
    xpadding 8
    ypadding 4
    yalign 0.5
    selected_background Frame(gui.slot_badge_bg, gui.slot_badge_borders, tile=False)

style new_page_button_text is default:
    font gui.interface_text_font
    size gui.slot_subtitle_size
    color gui.slot_muted_color
    hover_color gui.slot_accent_color
    selected_color gui.slot_badge_text_color
    outlines []
    antialias True

# Arrow buttons use a dedicated 48x48 pill image (no Frame). Frame at
# small render sizes was producing crossing-line artifacts.
style new_page_arrow is new_page_button:
    background gui.slot_arrow_bg
    xsize 48
    ysize 48
    xpadding 0
    ypadding 0
    yalign 0.5
    selected_background None

style new_page_arrow_text is new_page_button_text:
    color gui.slot_accent_color
    hover_color gui.slot_accent_strong
    text_align 0.5
    xalign 0.5
    yalign 0.5


## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

transform pref_group_left(delay=0.0):
    subpixel True
    alpha 0.0
    xoffset -40
    yoffset 12
    pause delay
    easein_quart .45 alpha 1.0 xoffset 0 yoffset 0

transform pref_group_right(delay=0.0):
    subpixel True
    alpha 0.0
    xoffset 40
    yoffset 12
    pause delay
    easein_quart .45 alpha 1.0 xoffset 0 yoffset 0

transform pref_group_up(delay=0.0):
    subpixel True
    alpha 0.0
    yoffset 80
    pause delay
    easein_quart .80 alpha 1.0 yoffset 0

transform pref_button_float:
    subpixel True

    on idle:
        easein_quart .25 yoffset 0

    on hover:
        easein_quart .25 yoffset -3

define persistent.text_size = 30
define persistent.text_spacing = 0
default persistent.text_kerning = 0.0

screen preferences():

    tag menu
    default _tab = "general"

    use game_menu(_("Preferences"), scroll=None):

        add "gui/icons/preferences2.png":
            align (0.1, -0.02)
            offset (40, 40)
            at transform:
                subpixel True
                block:
                    rotate 0.0
                    linear 5.0 rotate 360.0
                    repeat

        frame:
            background None
            xfill True
            yfill True

            # ===== SIDEBAR =====
            vbox:
                xpos 175
                ypos 130
                spacing 8
                xsize 220

                for tab_id, tab_label in [
                    ("general", _("General")),
                    ("cursor", _("Cursor")),
                    ("audio", _("Audio")),
                    ("accessibility", _("Accessibility")),
                    ("controls", _("Controls")),
                ]:
                    textbutton tab_label:
                        action SetScreenVariable("_tab", tab_id)
                        xsize 220
                        ysize 52
                        text_align (.0, .5)
                        text_size 28
                        text_color ("#6960a7" if _tab == tab_id else "#2E2A3D")
                        text_hover_color "#484271"
                        text_outlines []
                        background ("#00000010" if _tab == tab_id else None)
                        hover_background "#00000027"
                        left_padding 20

            # ===== CONTENT =====
            frame:
                xalign 0.50
                yalign 0.3
                background None
                xsize 750
                ysize 500

                # --- GENERAL ---
                if _tab == "general":
                    hbox:
                        xfill True
                        spacing 60
                        at pref_group_up(0.00)

                        if renpy.variant("pc") or renpy.variant("web"):
                            vbox:
                                style_prefix "radio"
                                spacing 14
                                label _("DISPLAY")

                                imagebutton:
                                    auto "gui/button/radio_%s_background.png"
                                    foreground Text(_("Window"), style="custom_btn_txt")
                                    hover_foreground Text(_("Window"), style="custom_btn_txt_hover")
                                    action Preference("display", "window")
                                    at pref_button_float

                                imagebutton:
                                    auto "gui/button/radio_%s_background.png"
                                    foreground Text(_("Fullscreen"), style="custom_btn_txt")
                                    hover_foreground Text(_("Fullscreen"), style="custom_btn_txt_hover")
                                    action Preference("display", "fullscreen")
                                    at pref_button_float

                        vbox:
                            style_prefix "radio"
                            spacing 14
                            label _("LANGUAGE")

                            imagebutton:
                                auto "gui/button/radio_%s_background.png"
                                foreground Text("English", style="custom_btn_txt")
                                hover_foreground Text("English", style="custom_btn_txt_hover")
                                action Language(None)
                                at pref_button_float

                            imagebutton:
                                auto "gui/button/radio_%s_background.png"
                                foreground Text("中文", style="custom_btn_txt_cn")
                                hover_foreground Text("中文", style="custom_btn_txt_cn_hover")
                                action Language("chinese")
                                at pref_button_float

                        vbox:
                            style_prefix "radio"
                            spacing 14
                            label _("SKIP")

                            imagebutton:
                                auto "gui/button/radio_%s_background.png"
                                foreground Text(_("Unseen Text"), style="custom_btn_txt")
                                hover_foreground Text(_("Unseen Text"), style="custom_btn_txt_hover")
                                action Preference("skip", "toggle")
                                at pref_button_float

                            imagebutton:
                                auto "gui/button/radio_%s_background.png"
                                foreground Text(_("After Choices"), style="custom_btn_txt")
                                hover_foreground Text(_("After Choices"), style="custom_btn_txt_hover")
                                action Preference("after choices", "toggle")
                                at pref_button_float

                            imagebutton:
                                auto "gui/button/radio_%s_background.png"
                                foreground Text(_("Transitions"), style="custom_btn_txt")
                                hover_foreground Text(_("Transitions"), style="custom_btn_txt_hover")
                                action InvertSelected(Preference("transitions", "toggle"))
                                at pref_button_float

                # --- AUDIO ---
                elif _tab == "audio":
                    vbox:
                        spacing 40
                        at pref_group_up(0.00)

                        hbox:
                            xfill True
                            spacing 60

                            if config.has_music:
                                vbox:
                                    style_prefix "slider"
                                    xsize 350
                                    label _("MUSIC VOLUME")
                                    bar value Preference("music volume") style "bar"

                            if config.has_sound:
                                vbox:
                                    style_prefix "slider"
                                    xsize 350
                                    label _("SOUND VOLUME")
                                    bar value Preference("sound volume") style "bar"

                            if config.has_voice:
                                vbox:
                                    style_prefix "slider"
                                    xsize 350
                                    label _("VOICE VOLUME")
                                    bar value Preference("voice volume") style "bar"

                        if config.has_music or config.has_sound or config.has_voice:
                            imagebutton:
                                auto "gui/button/radio_%s_background.png"
                                foreground Text(_("Mute All"), style="custom_btn_txt")
                                hover_foreground Text(_("Mute All"), style="custom_btn_txt_hover")
                                action Preference("all mute", "toggle")
                                at pref_button_float

                # --- ACCESSIBILITY ---
                elif _tab == "accessibility":
                    vbox:
                        spacing 48
                        at pref_group_up(0.00)

                        hbox:
                            xfill True
                            spacing 60

                            vbox:
                                style_prefix "slider"
                                xsize 350
                                label _("TEXT SPEED")
                                bar value Preference("text speed") style "bar"

                            vbox:
                                style_prefix "slider"
                                xsize 350
                                label _("AUTO-FORWARD TIME")
                                bar value Preference("auto-forward time") style "bar"

                            vbox:
                                style_prefix "slider"
                                xsize 350
                                label _("DIALOGUE SIZE")
                                bar value FieldValue(persistent, "text_size", range=24, offset=16, step=2) style "bar"

                        hbox:
                            xfill True
                            spacing 60
                            vbox:
                                style_prefix "slider"
                                xsize 350
                                label _("TEXT SPACING")
                                bar value FieldValue(persistent, "text_kerning", range=5.0, offset=-1.0, step=0.5) style "bar"

                            vbox:
                                style_prefix "slider"
                                xsize 350
                                label _("LINE SPACING")
                                bar value FieldValue(persistent, "text_spacing", range=20, offset=0, step=2) style "bar"

                # --- CONTROLS ---
                elif _tab == "controls":
                    vbox:
                        xalign 0.65
                        spacing 24
                        at pref_group_up(0.00)

                        text _("KEYBOARD SHORTCUTS"):
                            size 30
                            color "#00000094"
                            kerning 2.5
                            outlines []

                        for key, desc in [
                            ("Space / Enter", _("Advance dialogue")),
                            ("Ctrl", _("Skip text")),
                            ("Tab", _("Toggle skip")),
                            ("H", _("Hide interface")),
                            ("S", _("Screenshot")),
                            ("F", _("Toggle fullscreen")),
                            ("Scroll Up", _("Rollback")),
                            ("Scroll Down", _("Roll forward")),
                            ("Esc", _("Game menu")),
                        ]:
                            hbox:
                                spacing 20
                                text key:
                                    size 22
                                    color "#000000e8"
                                    min_width 220
                                    outlines []
                                text desc:
                                    size 22
                                    color "#000000a2"
                                    outlines []

                # --- CURSOR ---
                elif _tab == "cursor":
                    hbox:
                        xfill True
                        spacing 60
                        at pref_group_up(0.00)

                        vbox:
                            style_prefix "radio"
                            spacing 14
                            label _("CURSOR COLOR")

                            for cursor_id, cursor_label in [
                                ("default", _("Default")),
                                ("purple", _("Purple")),
                                ("seafoam", _("Seafoam")),
                                ("sunsetpink", _("Sunset Pink")),
                                ("honeycore", _("Honeycore")),
                            ]:
                                imagebutton:
                                    auto "gui/button/radio_%s_background.png"
                                    foreground Text(cursor_label, style="custom_btn_txt")
                                    hover_foreground Text(cursor_label, style="custom_btn_txt_hover")
                                    selected (persistent.cursor_style == cursor_id)
                                    action [
                                        SetField(persistent, "cursor_style", cursor_id),
                                        SetVariable("default_mouse", get_cursor_key(cursor_id, persistent.cursor_animated))
                                    ]
                                    at pref_button_float

                        vbox:
                            style_prefix "radio"
                            spacing 14
                            label _("ANIMATION")

                            imagebutton:
                                auto "gui/button/radio_%s_background.png"
                                foreground Text(_("Animated"), style="custom_btn_txt")
                                hover_foreground Text(_("Animated"), style="custom_btn_txt_hover")
                                selected persistent.cursor_animated
                                action [
                                    SetField(persistent, "cursor_animated", True),
                                    SetVariable("default_mouse", persistent.cursor_style)
                                ]
                                at pref_button_float

                            imagebutton:
                                auto "gui/button/radio_%s_background.png"
                                foreground Text(_("Static"), style="custom_btn_txt")
                                hover_foreground Text(_("Static"), style="custom_btn_txt_hover")
                                selected (not persistent.cursor_animated)
                                action [
                                    SetField(persistent, "cursor_animated", False),
                                    SetVariable("default_mouse", persistent.cursor_style + "_static")
                                ]
                                at pref_button_float


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

style slider_label_text:
    size 30

style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style custom_btn_txt:
    xoffset 65
    yoffset 9
    size 26
    color "#2E2A3D"
    outlines []

style custom_btn_txt_hover:
    xoffset 65
    yoffset 8
    color "#fff"
    size 26
    outlines []

style custom_btn_txt_cn_hover:
    xoffset 65
    yoffset 8
    color "#fff"
    size 26
    font "tl/chinese/font/JiYingHuiPianHeYuan.ttf"
    outlines []

style custom_btn_txt_cn:
    xoffset 65
    yoffset 9
    color "#2E2A3D"
    size 26
    font "tl/chinese/font/JiYingHuiPianHeYuan.ttf"
    outlines []

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 5
    kerning 10

style pref_label_text:
    yalign 1.0
    outlines []
    color "#2E2A3D"
    # size 30

style pref_vbox:
    xsize 338

style radio_vbox:
    spacing 10

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

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
    xsize 400


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
                        substitute False

                        ## Take the color of the who text from the Character, if
                        ## set.
                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute False

        if not _history_list:
            label _("The dialogue history is empty.")


## This determines what tags are allowed to be displayed on the history screen.

define gui.history_allow_tags = set()


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

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

style confirm_text_subtitle is default:
    font "bin/assets/faces/LaParisienne.otf"
    size 22
    color "#ffffff94"
    kerning 2.5
    outlines []

style confirm_text_heading is default:
    font "bin/assets/faces/LaParisienne.otf"
    size 40
    color "#ffffffe8"
    outlines []

style confirm_text_description is default:
    font "bin/assets/faces/LaParisienne.otf"
    size 28
    color "#ffffff94"
    outlines []


style quit_style_buttons:
    font "bin/assets/faces/LaParisienne.otf"
    outlines []

transform confirm_bg_fade:
    subpixel True
    alpha 0.0
    easein 0.25 alpha 1.0

transform confirm_frame_enter:
    subpixel True
    alpha 0.0 zoom 0.96
    easein 0.3 alpha 1.0 zoom 1.0

transform confirm_from_top(delay=0):
    subpixel True
    alpha 0.0 yoffset -40
    pause delay
    easein 0.35 alpha 1.0 yoffset 0

transform confirm_from_left(delay=0):
    subpixel True
    alpha 0.0 xoffset -40
    pause delay
    easein 0.35 alpha 1.0 xoffset 0

transform confirm_from_right(delay=0):
    subpixel True
    alpha 0.0 xoffset 40
    pause delay
    easein 0.35 alpha 1.0 xoffset 0

transform confirm_from_bottom(delay=0):
    subpixel True
    alpha 0.0 yoffset 40
    pause delay
    easein 0.35 alpha 1.0 yoffset 0

transform confirm_icon_pulse:
    subpixel True
    alpha 0.0 yoffset -40 zoom 1.0
    easein 0.35 alpha 1.0 yoffset 0 zoom 1.0
    pause 0.3
    block:
        ease 0.8 zoom 1.2
        ease 0.8 zoom 1.0
        repeat

screen confirm(message, yes_action, no_action):

    modal True
    add Solid("#000000b0") at confirm_bg_fade

    $ is_load    = "load" in message.lower()
    $ is_menu    = "title" in message.lower() or "main menu" in message.lower()
    $ is_quit    = "quit" in message.lower()
    $ is_delete  = "delete" in message.lower()
    $ is_save    = "overwrite" in message.lower()
    $ is_replay  = "replay" in message.lower()
    $ is_skip    = "skip" in message.lower()

    $ icon_rotation = 0 if is_load else (180 if is_delete else 90)

    frame at confirm_frame_enter:
        background "#34344bea"
        padding (64, 52)
        align (.5, .5)
        xsize 520

        vbox:
            spacing 0
            xalign .5

            # --- Icon, isolated from vbox flow ---
            fixed:
                xalign .5
                xsize 64
                ysize 64
                add Transform("/gui/icons/load.png", zoom=0.7, rotate=icon_rotation) align (.5, .5) at confirm_icon_pulse

            null height 24

            # --- Subtitle label ---
            text (
                "LOAD SAVE" if is_load
                else "MAIN MENU" if is_menu
                else "DELETE SAVE" if is_delete
                else "OVERWRITE SAVE" if is_save
                else "END REPLAY" if is_replay
                else "SKIP AHEAD" if is_skip
                else "QUIT GAME"
            ) style "confirm_text_subtitle" xalign .5 at confirm_from_left(0.1)

            null height 12

            # --- Heading ---
            text (
                "Loading a save file..." if is_load
                else "Return to title?" if is_menu
                else "Delete this save?" if is_delete
                else "Overwrite this save?" if is_save
                else "End this replay?" if is_replay
                else "Skip to the next choice?" if is_skip
                else "Ready to leave?"
            ) style "confirm_text_heading" xalign .5 at confirm_from_right(0.15)

            null height 10

            # --- Description ---
            text (
                "Your current progress will be lost." if is_load
                else "Your current progress will be lost." if is_menu
                else "This action cannot be undone." if is_delete
                else "The existing save will be replaced." if is_save
                else "You will return to where you started." if is_replay
                else "Unread dialogue will be skipped." if is_skip
                else "Unsaved progress will be lost."
            ) style "confirm_text_description" xalign .5 at confirm_from_left(0.2)

            null height 40

            hbox:
                spacing 16
                xalign .5

                # --- Confirm button ---
                textbutton (
                    "Load" if is_load
                    else "Leave" if is_menu
                    else "Delete" if is_delete
                    else "Overwrite" if is_save
                    else "End" if is_replay
                    else "Skip" if is_skip
                    else "Quit"
                ) at confirm_from_bottom(0.25):
                    style "quit_style_buttons"
                    action yes_action
                    xsize 192
                    ysize 58
                    text_align (.5, .5)
                    background "#ffffff10"
                    hover_background "#ffffff1a"
                    text_style "quit_style_buttons"

                # --- Cancel button ---
                textbutton (
                    "Cancel" if (is_load or is_delete or is_save or is_replay or is_skip)
                    else "Stay"
                ) at confirm_from_bottom(0.35):
                    style "quit_style_buttons"
                    action no_action
                    xsize 192
                    ysize 58
                    text_align (.5, .5)
                    background "#ffffffe8"
                    hover_background "#ffffffcc"
                    text_color "#111118"
                    text_style "quit_style_buttons"



style confirm_secondary_txt:
    color "#ffffffbf"
    size 26
    font "DejaVuSans.ttf"
    xalign .5
    yalign .5

style confirm_primary_txt:
    color "#111118"
    size 26
    font "DejaVuSans.ttf"
    xalign .5
    yalign .5


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
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
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

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


## NVL screen ##################################################################
##
## This screen is used for NVL-mode dialogue and menus.
##
## https://www.renpy.org/doc/html/screen_special.html#nvl





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

    background "gui/nvl.png"
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
init:
    transform mobilecustomzoom:
        zoom 1.2

transform rotate_180:
    rotate 180

screen quick_menu():
    variant "touch"

    zorder 100

    if quick_menu:

        imagebutton:
            xpos 1824
            ypos 709
            auto "gui/button/quick_menu/auto_%s.png"
            action Rollback()
            at mobilecustomzoom, rotate_180

        imagebutton:
            xpos 1780
            ypos 785
            auto "gui/button/quick_menu/auto_%s.png"
            action Preference("auto-forward", "toggle")
            at mobilecustomzoom

        imagebutton:
            xpos 1840
            ypos 785
            auto "gui/button/quick_menu/skip_%s.png"
            action Skip() alternate Skip(fast=True, confirm=True)
            at mobilecustomzoom

        imagebutton:
            xpos 1840
            ypos 845
            auto "gui/button/quick_menu/load_%s.png"
            action ShowMenu('load')
            at mobilecustomzoom

        imagebutton:
            xpos 1780
            ypos 845
            auto "gui/button/quick_menu/save_%s.png"
            action ShowMenu('save')
            at mobilecustomzoom

        imagebutton:
            xpos 1780
            ypos 905
            auto "gui/button/quick_menu/qs_%s.png"
            action QuickSave()
            at mobilecustomzoom

        imagebutton:
            xpos 1840
            ypos 905
            auto "gui/button/quick_menu/ql_%s.png"
            action QuickLoad()
            at mobilecustomzoom

        imagebutton:
            xpos 1780
            ypos 965
            auto "gui/button/quick_menu/history_%s.png"
            action HideInterface()
            at mobilecustomzoom

        imagebutton:
            xpos 1840
            ypos 965
            auto "gui/button/quick_menu/settings_%s.png"
            action ShowMenu('preferences')
            at mobilecustomzoom

        if _in_replay:
            imagebutton:
                xpos 1730
                ypos 1025
                auto "gui/button/quick_menu/end_%s.png"
                action EndReplay(confirm=True)
                at customzoom

style window:
    variant "small"
    background "gui/phone/textbox.png"

style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

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

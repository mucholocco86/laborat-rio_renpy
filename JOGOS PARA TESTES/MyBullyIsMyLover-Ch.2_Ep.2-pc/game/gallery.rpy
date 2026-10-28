default persistent.name = False
default persistent.gallery_name = "Kei"

label call_gallery:
    if not persistent.name:
        $ persistent.gallery_name = renpy.input("Please enter your name:")
        $ persistent.name = True
    return

image gal_bg:
    "gui/main_menu.png"
    alpha 0.9

style gallery_nav_vbox:
    xalign 0.03
    yalign .01
    yspacing 100

style gallery_stuff_grid:
    xalign 0.7
    yalign 0.5
    xspacing 20
    yspacing 20

style gallery_stuff_hbox:
    xalign 0.5
    yanchor 0.9
    ypos 0.95
    spacing 20


# screen gallery():
#     tag menu
#     use gallery_navigation

screen gallery_navigation():
    tag menu

    add "gal_bg"


    style_prefix "gallery_nav"

        ## Add Characters
    imagebutton auto "gui/button/sky_%s.png" xpos 140 ypos 70 focus_mask True action [Show("gallery_sky"), Play("sound", "audio/click.ogg")] idle "gui/button/sky_%s.png" hover "gui/button/skyh_%s.png" hovered Play("sound", "audio/switchclick.mp3")
    imagebutton auto "gui/button/lily_%s.png" xpos 140 ypos 160 focus_mask True action [Show("gallery_lily"), Play("sound", "audio/click.ogg")] idle "gui/button/lily_%s.png" hover "gui/button/lilyh_%s.png" hovered Play("sound", "audio/switchclick.mp3")
    imagebutton auto "gui/button/aine_%s.png" xpos 140 ypos 250 focus_mask True action [Show("gallery_aine" ), Play("sound", "audio/click.ogg")] idle "gui/button/aine_%s.png" hover "gui/button/aineh_%s.png" hovered Play("sound", "audio/switchclick.mp3")
    imagebutton auto "gui/button/emma_%s.png" xpos 140 ypos 340 focus_mask True action [Show("gallery_emma"), Play("sound", "audio/click.ogg")] idle "gui/button/emma_%s.png" hover "gui/button/emmah_%s.png" hovered Play("sound", "audio/switchclick.mp3")
    imagebutton auto "gui/button/gwen_%s.png" xpos 140 ypos 430 focus_mask True action [Show("gallery_gwen"), Play("sound", "audio/click.ogg")] idle "gui/button/gwen_%s.png" hover "gui/button/gwenh_%s.png" hovered Play("sound", "audio/switchclick.mp3")
    imagebutton auto "gui/button/klara_%s.png" xpos 140 ypos 520 focus_mask True action [Show("gallery_klara"), Play("sound", "audio/click.ogg")] idle "gui/button/klara_%s.png" hover "gui/button/klarah_%s.png" hovered Play("sound", "audio/switchclick.mp3")
    imagebutton auto "gui/button/freya_%s.png" xpos 140 ypos 610 focus_mask True action [Show("gallery_freya"), Play("sound", "audio/click.ogg")] idle "gui/button/freya_%s.png" hover "gui/button/freyah_%s.png" hovered Play("sound", "audio/switchclick.mp3")
    imagebutton auto "gui/button/naomi_%s.png" xpos 140 ypos 700 focus_mask True action [Show("gallery_naomi"), Play("sound", "audio/click.ogg")] idle "gui/button/naomi_%s.png" hover "gui/button/naomih_%s.png" hovered Play("sound", "audio/switchclick.mp3")
    imagebutton auto "gui/button/moon_%s.png" xpos 140 ypos 790 focus_mask True action [Show("gallery_moon"), Play("sound", "audio/click.ogg")] idle "gui/button/moon_%s.png" hover "gui/button/moonh_%s.png" hovered Play("sound", "audio/switchclick.mp3")

    imagebutton auto "gui/button/return_%s.png" xpos 95 ypos 950 focus_mask True action [Return(), Play("sound", "audio/click.ogg")] idle "gui/button/return_%s.png" hover "gui/button/returnh_%s.png" hovered Play("sound", "audio/switchclick.mp3")


screen gallery_sky():
    tag menu
    use gallery_navigation
    default cg_page = 1

    hbox:
        style_prefix "gallery_stuff"

    if cg_page == 1:
        grid 3 3:
            style_prefix "gallery_stuff"

            ## There always needs to be 6 elements. Replace with null if no scene
            imagebutton:
                action Replay("skyfirsttime")
                idle Transform("i101", zoom=0.2)
                insensitive Transform("locked", zoom=0.2)
            imagebutton:
                action Replay("mytruefeelings")
                idle Transform("i497", zoom=0.2)
                insensitive Transform("locked", zoom=0.2)
            imagebutton:
                action Replay("skycelebratewear1")
                idle Transform("i623", zoom=0.2)
                insensitive Transform("locked", zoom=0.2)
            imagebutton:
                action Replay("skycelebratewear2")
                idle Transform("i624", zoom=0.2)
                insensitive Transform("locked", zoom=0.2)
            imagebutton:
                action Replay("skytruthconfession")
                idle Transform("ch1ep1_573", zoom=0.2)
                insensitive Transform("locked", zoom=0.2)
            imagebutton:
                action Replay("midnightbeachsexonsteroids")
                idle Transform("ch1ep1_1381", zoom=0.2)
                insensitive Transform("locked", zoom=0.2)
            imagebutton:
                action Replay("skystressrelief")
                idle Transform("ch1ep4_184", zoom=0.2)
                insensitive Transform("locked", zoom=0.2)
            null
            null

screen gallery_lily():
    tag menu
    use gallery_navigation
    default cg_page = 1

    hbox:
        style_prefix "gallery_stuff"


    if cg_page == 1:
        grid 3 2:
            style_prefix "gallery_stuff"

            ## There always needs to be 6 elements. Replace with null if no scene
            null
            null
            null
            null
            null
            null

screen gallery_aine():
    tag menu
    use gallery_navigation
    default cg_page = 1

    hbox:
        style_prefix "gallery_stuff"


    if cg_page == 1:
        grid 3 2:
            style_prefix "gallery_stuff"

            ## There always needs to be 6 elements. Replace with null if no scene
            imagebutton:
                action Replay("ainethumbsuck")
                idle Transform("ep7_624", zoom=0.2)
                insensitive Transform("locked", zoom=0.2)
            imagebutton:
                action Replay("relaximadoctor")
                idle Transform("ch1ep1_1472", zoom=0.2)
                insensitive Transform("locked", zoom=0.2)
            imagebutton:
                action Replay("crackinganaineopen")
                idle Transform("ch1ep3p2_361", zoom=0.2)
                insensitive Transform("locked", zoom=0.2)
            imagebutton:
                action Replay("ainepubtensionbuildup")
                idle Transform("ch1ep3p2_548", zoom=0.2)
                insensitive Transform("locked", zoom=0.2)
            imagebutton:
                action Replay("aineonsteroids")
                idle Transform("ch1ep3p2_931", zoom=0.2)
                insensitive Transform("locked", zoom=0.2)
            null

screen gallery_emma():
    tag menu
    use gallery_navigation
    default cg_page = 1

    hbox:
        style_prefix "gallery_stuff"


    if cg_page == 1:
        grid 3 2:
            style_prefix "gallery_stuff"

            ## There always needs to be 6 elements. Replace with null if no scene
            imagebutton:
                action Replay("emmaxmcfirst")
                idle Transform("ep7_442", zoom=0.2)
                insensitive Transform("locked", zoom=0.2)
            imagebutton:
                action Replay("emmaroleplay")
                idle Transform("ese_294", zoom=0.2)
                insensitive Transform("locked", zoom=0.2)
            imagebutton:
                action Replay("emmapreggospecial")
                idle Transform("ese_885", zoom=0.2)
                insensitive Transform("locked", zoom=0.2)
            null
            null
            null

screen gallery_gwen():
    tag menu
    use gallery_navigation
    default cg_page = 1

    hbox:
        style_prefix "gallery_stuff"


    if cg_page == 1:
        grid 3 2:
            style_prefix "gallery_stuff"

            ## There always needs to be 6 elements. Replace with null if no scene
            imagebutton:
                action Replay("gwenmcpast")
                idle Transform("i218", zoom=0.2)
                insensitive Transform("locked", zoom=0.2)
            imagebutton:
                action Replay("gwenhandjob")
                idle Transform("ep3_409", zoom=0.2)
                insensitive Transform("locked", zoom=0.2)
            imagebutton:
                action Replay("gwenfirstarcfun")
                idle Transform("ep4_291", zoom=0.2)
                insensitive Transform("locked", zoom=0.2)
            imagebutton:
                action Replay("gwenmorningsex")
                idle Transform("ep6_771", zoom=0.2)
                insensitive Transform("locked", zoom=0.2)
            imagebutton:
                action Replay("gwenanal")
                idle Transform("ch1ep2_1039", zoom=0.2)
                insensitive Transform("locked", zoom=0.2)
            null

screen gallery_klara():
    tag menu
    use gallery_navigation
    default cg_page = 1

    hbox:
        style_prefix "gallery_stuff"


    if cg_page == 1:
        grid 3 2:
            style_prefix "gallery_stuff"

            ## There always needs to be 6 elements. Replace with null if no scene
            imagebutton:
                action Replay("klaradrunkshow")
                idle Transform("ch1ep2_543", zoom=0.2)
                insensitive Transform("locked", zoom=0.2)
            imagebutton:
                action Replay("forbiddenfruit")
                idle Transform("ch2ep1_922", zoom=0.2)
                insensitive Transform("locked", zoom=0.2)
            null
            null
            null
            null

screen gallery_freya():
    tag menu
    use gallery_navigation
    default cg_page = 1

    hbox:
        style_prefix "gallery_stuff"


    if cg_page == 1:
        grid 3 2:
            style_prefix "gallery_stuff"

            ## There always needs to be 6 elements. Replace with null if no scene
            imagebutton:
                action Replay("freyapantstease")
                idle Transform("ep6_920", zoom=0.2)
                insensitive Transform("locked", zoom=0.2)
            imagebutton:
                action Replay("freyatitplay")
                idle Transform("ch1ep1_658", zoom=0.2)
                insensitive Transform("locked", zoom=0.2)
            imagebutton:
                action Replay("freyasucknosuck")
                idle Transform("ch1ep3_107", zoom=0.2)
                insensitive Transform("locked", zoom=0.2)
            imagebutton:
                action Replay("freyastitchcosplay")
                idle Transform("ch1ep3_311", zoom=0.2)
                insensitive Transform("locked", zoom=0.2)
            null
            null

screen gallery_naomi():
    tag menu
    use gallery_navigation
    default cg_page = 1

    hbox:
        style_prefix "gallery_stuff"


    if cg_page == 1:
        grid 3 2:
            style_prefix "gallery_stuff"

            ## There always needs to be 6 elements. Replace with null if no scene
            imagebutton:
                action Replay("naomishowerfix")
                idle Transform("ch1ep3p2_141", zoom=0.2)
                insensitive Transform("locked", zoom=0.2)
            null
            null
            null
            null
            null

screen gallery_moon():
    tag menu
    use gallery_navigation
    default cg_page = 1

    hbox:
        style_prefix "gallery_stuff"


    if cg_page == 1:
        grid 3 2:
            style_prefix "gallery_stuff"

            ## There always needs to be 6 elements. Replace with null if no scene
            imagebutton:
                action Replay("moonlightskinnydip")
                idle Transform("ch1ep1_1233", zoom=0.2)
                insensitive Transform("locked", zoom=0.2)
            imagebutton:
                action Replay("moonlollipopplay")
                idle Transform("ch1ep2_230", zoom=0.2)
                insensitive Transform("locked", zoom=0.2)
            imagebutton:
                action Replay("kaitosorareunion")
                idle Transform("ch1ep4_1152", zoom=0.2)
                insensitive Transform("locked", zoom=0.2)
            null
            null
            null

init offset = -2









init python:
    gui.init(3840, 2160)












define 2 gui.nvl_borders = Borders(0, 15, 0, 30)



define 2 gui.nvl_list_length = None



define 2 gui.nvl_height = 173



define 2 gui.nvl_spacing = 15



define 2 gui.nvl_name_xpos = 645
define 2 gui.nvl_name_ypos = 0
define 2 gui.nvl_name_width = 225
define 2 gui.nvl_name_xalign = 1.0


define 2 gui.nvl_text_xpos = 675
define 2 gui.nvl_text_ypos = 12
define 2 gui.nvl_text_width = 885
define 2 gui.nvl_text_xalign = 0.0



define 2 gui.nvl_thought_xpos = 360
define 2 gui.nvl_thought_ypos = 0
define 2 gui.nvl_thought_width = 1170
define 2 gui.nvl_thought_xalign = 0.0


define 2 gui.nvl_button_xpos = 675
define 2 gui.nvl_button_xalign = 0.0





define gui.accent_color = '#3CDFFF'


define gui.idle_color = '#888888'



define gui.idle_small_color = '#aaaaaa'


define gui.hover_color = '#3CDFFF'



define gui.selected_color = '#3CDFFF'


define gui.insensitive_color = '#8888887f'



define gui.muted_color = '#add8e6'
define gui.hover_muted_color = '#3CDFFF'


define gui.text_color = '#ffffff'
define gui.interface_text_color = '#ffffff'


init python:
    style.say_label.font = "font/Cyberpunk.otf"



define gui.text_font = "fonts/VioletSans-Regular.otf"


define gui.name_text_font = "fonts/jenriv-titling-bold.otf"


define gui.interface_text_font = "fonts/jenriv-titling-bold.otf"

define gui.interface_text_font2 = "fonts/nexa-bold.otf"


define gui.text_size = 58


define gui.name_text_size = 55


define gui.interface_text_size = 66


define gui.label_text_size = 72


define gui.notify_text_size = 48


define gui.title_text_size = 150



define 2 gui.main_menu_background = "gui/gamelogo.png"

define gui.game_menu_background = None

define 2 gui.main_menu_background = "gui/gamelogo.png"







define gui.textbox_height = 555



define gui.textbox_yalign = 1.0


define gui.name_xpos = 1165
define gui.name_ypos = 51



define gui.name_xalign = 0.0



define gui.namebox_width = None
define gui.namebox_height = None



define gui.namebox_borders = Borders(5, 5, 5, 5)



define gui.namebox_tile = False

init 2 python:

    renpy.music.register_channel("sound2", "sound", True)
    renpy.music.register_channel("music2", "music", True)
    renpy.music.register_channel("sound3", "sound", True)
    renpy.music.register_channel("music3", "music", True)
    renpy.music.register_channel("music4", "music", True)
    renpy.music.register_channel("music7", "music", True)


    renpy.music.register_channel(
    "narration",
    mixer="narration",
    loop=False,
    stop_on_mute=True
)






init -498 screen the_example():
    modal True
    zorder 9999
    vbox:
        text "Just an example. Click 'End' on the bottom right." size 50 outlines [(3, "#000", 1, 1)]
        xpos 1200
        ypos 1790
        xsize 1600
    vbox:
        textbutton "End" action Return()
        xpos 2300
        ypos 2050
label show_screen_the_example:
    $ renpy.show_screen("the_example")
    $ renpy.pause(hard=True)
    $ renpy.hide_screen("the_example")
    return

init -498 screen valhalla():
    modal True
    zorder 9999
    vbox:
        text "A French phrase. It means, something (such as an appealing quality) that cannot be adequately described or expressed." size 50 outlines [(3, "#000", 1, 1)]
        xpos 1200
        ypos 1777
        xsize 1600
    vbox:
        textbutton "End" action Return()
        xpos 2300
        ypos 2050
label jesay:
    $ renpy.show_screen("valhalla")
    $ renpy.pause(hard=True)
    $ renpy.hide_screen("valhalla")
    return

init -498 screen explain_the_god():
    modal True
    zorder 9999
    vbox:
        text "Nebula is a revered cosmic deity believed in by people across the galaxy. As a divine being, Nebula embodies the wonders of the universe and holds great significance in the beliefs of spacefaring civilizations. It is an ethereal entity, characterized by its radiant celestial form and shimmering stardust." size 50 outlines [(3, "#000", 1, 1)]
        xpos 1200
        ypos 1790
        xsize 1600
    vbox:
        textbutton "End" action Return()
        xpos 2300
        ypos 2050
label show_screen_explain_the_god:
    $ renpy.show_screen("explain_the_god")
    $ renpy.pause(hard=True)
    $ renpy.hide_screen("explain_the_god")
    return

init -498 screen emperor():
    modal True
    zorder 9999
    vbox:
        text "The Emperor is the enigmatic leader of the universe, presiding over the council members of all species. Shrouded in mystery, The Emperor remains unseen and rarely intervenes in council affairs unless the fate of the entire galaxy is at stake. Their presence symbolizes a higher authority, guiding the cosmic order from behind the scenes." size 50 outlines [(3, "#000", 1, 1)]
        xpos 1200
        ypos 1790
        xsize 1600
    vbox:
        textbutton "End" action Return()
        xpos 2300
        ypos 2050
label show_screen_emperor:
    $ renpy.show_screen("emperor")
    $ renpy.pause(hard=True)
    $ renpy.hide_screen("emperor")
    return

init -498 screen collective():
    modal True
    zorder 9999
    vbox:
        text "The Collective is an elite interstellar military force, transcending race and uniting humans, aliens, and more. Led by the Human Council, it represents the pinnacle of cooperation, showcasing the shared dedication to protect and advance the interests of all species. Together, they forge an indomitable alliance, guarding the galaxy with unwavering resolve." size 50 outlines [(3, "#000", 1, 1)]
        xpos 1200
        ypos 1790
        xsize 1600
    vbox:
        textbutton "End" action Return()
        xpos 2300
        ypos 2050
label show_screen_collective:
    $ renpy.show_screen("collective")
    $ renpy.pause(hard=True)
    $ renpy.hide_screen("collective")
    return

init -498 screen martha():
    modal True
    zorder 9999
    vbox:
        text "Councilor Martha is the esteemed leader of the Human Council and visionary creator of 'The Collective'. She stands as a beacon of unity among council members. Through hereditary succession, the position remains within her family, fostering a legacy of trust. This enduring lineage empowers Councilor Martha to wield influence that transcends generations, guiding species towards harmony and peace." size 50 outlines [(3, "#000", 1, 1)]
        xpos 1200
        ypos 1765
        xsize 1600
    vbox:
        textbutton "End" action Return()
        xpos 2300
        ypos 2050
label show_screen_martha:
    $ renpy.show_screen("martha")
    $ renpy.pause(hard=True)
    $ renpy.hide_screen("martha")
    return

init -498 screen avon():
    modal True
    zorder 9999
    vbox:
        text "Avon is a picturesque and mountainous planet, captivated with its breathtaking beauty. Vast ranges sculpt the landscape, adorned with majestic peaks, serene valleys, lush forests, cascading waterfalls, and crystalline lakes. Avon's natural grandeur offers a sanctuary where awe-inspiring vistas and tranquility coexist, making it the perfect planet to settle down and raise a family on." size 50 outlines [(3, "#000", 1, 1)]
        xpos 1200
        ypos 1765
        xsize 1600
    vbox:
        textbutton "End" action Return()
        xpos 2300
        ypos 2050
label show_screen_avon:
    $ renpy.show_screen("avon")
    $ renpy.pause(hard=True)
    $ renpy.hide_screen("avon")
    return

init -498 screen nebulaa():
    modal True
    zorder 9999
    vbox:
        text "Nebula Mist is a synthetic inhalant, granting euphoria similar to marijuana, and favored in Neon City for its vibrant sensations." size 50 outlines [(3, "#000", 1, 1)]
        xpos 1200
        ypos 1777
        xsize 1600
    vbox:
        textbutton "End" action Return()
        xpos 2300
        ypos 2050
label show_screen_nebulaa:
    $ renpy.show_screen("nebulaa")
    $ renpy.pause(hard=True)
    $ renpy.hide_screen("nebulaa")
    return







define gui.dialogue_xpos = 1165
define gui.dialogue_ypos = 215


define gui.dialogue_width = 2232



define gui.dialogue_text_xalign = 0.0








define gui.button_width = None
define gui.button_height = None


define gui.button_borders = Borders(12, 12, 12, 12)



define gui.button_tile = False


define gui.button_text_font = gui.interface_text_font2


define gui.button_text_size = gui.interface_text_size


define gui.button_text_idle_color = gui.idle_color
define gui.button_text_hover_color = gui.hover_color
define gui.button_text_selected_color = gui.selected_color
define gui.button_text_insensitive_color = gui.insensitive_color



define gui.button_text_xalign = 0.0








define gui.radio_button_borders = Borders(54, 12, 12, 12)

define gui.check_button_borders = Borders(54, 12, 12, 12)

define gui.confirm_button_text_xalign = 0.5

define gui.page_button_borders = Borders(30, 12, 30, 12)

define gui.quick_button_borders = Borders(30, 12, 30, 0)
define gui.quick_button_text_size = 42
define gui.quick_button_text_idle_color = gui.idle_small_color
define gui.quick_button_text_selected_color = gui.accent_color













define gui.choice_button_height = 120
define gui.choice_button_tile = False
define gui.choice_button_borders = Borders(200, 30, 60, 10)
define gui.choice_button_text_font = gui.text_font
define gui.choice_button_text_size = 50
define gui.choice_button_text_xalign = 0.0
define gui.choice_button_text_yalign = 1.0
define gui.choice_button_text_idle_color = "#cccccc"
define gui.choice_button_text_hover_color = '#3CDFFF'
define gui.choice_button_text_insensitive_color = "#444444"









define gui.slot_button_width = 828
define gui.slot_button_height = 618
define gui.slot_button_borders = Borders(30, 30, 30, 30)
define gui.slot_button_text_size = 42
define gui.slot_button_text_xalign = 0.5
define gui.slot_button_text_idle_color = gui.idle_small_color
define gui.slot_button_text_selected_idle_color = gui.selected_color
define gui.slot_button_text_selected_hover_color = gui.hover_color


define config.thumbnail_width = 768
define config.thumbnail_height = 432


define gui.file_slot_cols = 3
define gui.file_slot_rows = 2









define gui.navigation_xpos = 120


define gui.skip_ypos = 30


define gui.notify_ypos = 135


define gui.choice_spacing = 3


define gui.navigation_spacing = 12


define gui.pref_spacing = 30


define gui.pref_button_spacing = 0


define gui.page_spacing = 0


define gui.slot_spacing = 30


define gui.main_menu_text_xalign = 1.0








define gui.frame_borders = Borders(12, 12, 12, 12)


define gui.confirm_frame_borders = Borders(120, 120, 120, 120)


define gui.skip_frame_borders = Borders(48, 15, 150, 15)


define gui.notify_frame_borders = Borders(48, 15, 120, 15)


define gui.frame_tile = False











define gui.bar_size = 75
define gui.scrollbar_size = 36
define gui.slider_size = 75


define gui.bar_tile = False
define gui.scrollbar_tile = False
define gui.slider_tile = False


define gui.bar_borders = Borders(12, 12, 12, 12)
define gui.scrollbar_borders = Borders(12, 12, 12, 12)
define gui.slider_borders = Borders(12, 12, 12, 12)


define gui.vbar_borders = Borders(12, 12, 12, 12)
define gui.vscrollbar_borders = Borders(12, 12, 12, 12)
define gui.vslider_borders = Borders(12, 12, 12, 12)



define gui.unscrollable = "hide"







define config.history_length = 250



define gui.history_height = 420



define gui.history_name_xpos = 465
define gui.history_name_ypos = 0
define gui.history_name_width = 465
define gui.history_name_xalign = 1.0


define gui.history_text_xpos = 510
define gui.history_text_ypos = 6
define gui.history_text_width = 2220
define gui.history_text_xalign = 0.0







define gui.nvl_borders = Borders(0, 30, 0, 60)



define gui.nvl_list_length = None



define gui.nvl_height = 345



define gui.nvl_spacing = 30



define gui.nvl_name_xpos = 1290
define gui.nvl_name_ypos = 0
define gui.nvl_name_width = 450
define gui.nvl_name_xalign = 1.0


define gui.nvl_text_xpos = 1350
define gui.nvl_text_ypos = 24
define gui.nvl_text_width = 1770
define gui.nvl_text_xalign = 0.0



define gui.nvl_thought_xpos = 720
define gui.nvl_thought_ypos = 0
define gui.nvl_thought_width = 2340
define gui.nvl_thought_xalign = 0.0


define gui.nvl_button_xpos = 1350
define gui.nvl_button_xalign = 0.0







define gui.language = "unicode"






init python:



    if renpy.variant("touch"):
        
        gui.quick_button_borders = Borders(120, 42, 120, 0)
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

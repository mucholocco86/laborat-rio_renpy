init offset = -2









init python:
    if persistent.resolution_4k and persistent.installed_4k:
        gui.init(3840, 2160)
    else:
        gui.init(1920, 1080)


init -1901 python:
    persistent.img_dir = "images"
    if persistent.resolution_4k == None:
        persistent.resolution_4k = False
    if renpy.loadable("scripts/4k.rpyc"):
        persistent.installed_4k = True
        config.images_directory = 'images_4k'
    else:
        persistent.installed_4k = False
    persistent.resolution_changed = False
    def _scan_images_directory():
        
        import os
        
        if not config.images_directory:
            return
        
        prefix = config.images_directory.rstrip('/') + '/'
        
        for fn in renpy.list_files():
            if not fn.startswith(prefix):
                continue
            
            basename = os.path.basename(fn)
            base, ext = os.path.splitext(basename)
            
            if not ext.lower() in [ ".jpg", ".jpeg", ".png", ".webp" ]:
                continue
            
            base = base.lower()
            
            if renpy.has_image(base, exact=True):
                continue
            
            renpy.image(base, fn)
    if persistent.resolution_4k and persistent.installed_4k:
        persistent.active_4k = True
        persistent.img_dir = "images_4k"
        _scan_images_directory()
        config.late_images_scan = False
        persistent.scale_factor = 2
        config.image_cache_size_mb = 8000
        config.image_cache_size = 200
    else:
        persistent.active_4k = False
        persistent.scale_factor = 1
        config.image_cache_size_mb = 300
        config.image_cache_size = None












define gui.accent_color = '#019fe6'


define gui.idle_color = '#555555'



define gui.idle_small_color = '#888888'


define gui.hover_color = '#ff9c27'



define gui.selected_color = '#e2e2e2'


define gui.insensitive_color = '#aaaaaa'



define gui.muted_color = '#66a3a3'
define gui.hover_muted_color = '#99c1c1'


define gui.text_color = '#ffffff'
define gui.interface_text_color = '#000000'





define gui.text_font = "fonts/Audrey-Bold.otf"


define gui.name_text_font = "fonts/Redressed.ttf"



define gui.interface_text_font = "fonts/Redressed.ttf"


define gui.text_size = 33 * persistent.scale_factor


define gui.name_text_size = 56 * persistent.scale_factor


define gui.interface_text_size = 36 * persistent.scale_factor


define gui.label_text_size = 36 * persistent.scale_factor


define gui.notify_text_size = 24 * persistent.scale_factor


define gui.title_text_size = 75 * persistent.scale_factor






define gui.main_menu_background = "[persistent.img_dir]/gui/ts3.jpg"
define gui.game_menu_background = "[persistent.img_dir]/gui/ts3.jpg"








define gui.textbox_height = 278 * persistent.scale_factor



define gui.textbox_yalign = 1.0




define gui.name_xpos = 360 * persistent.scale_factor

define gui.name_ypos = 50 * persistent.scale_factor



define gui.name_xalign = 0.0




define gui.namebox_width = None
define gui.namebox_height = None



define gui.namebox_borders = Borders(5 * persistent.scale_factor, 5 * persistent.scale_factor, 5 * persistent.scale_factor, 5 * persistent.scale_factor)



define gui.namebox_tile = False





define gui.dialogue_xpos = 402 * persistent.scale_factor

define gui.dialogue_ypos = 125 * persistent.scale_factor


define gui.dialogue_width = 1116 * persistent.scale_factor



define gui.dialogue_text_xalign = 0.0









define gui.button_width = None
define gui.button_height = None


define gui.button_borders = Borders(6 * persistent.scale_factor, 6 * persistent.scale_factor, 6 * persistent.scale_factor, 6 * persistent.scale_factor)



define gui.button_tile = False


define gui.button_text_font = gui.interface_text_font


define gui.button_text_size = gui.interface_text_size * persistent.scale_factor


define gui.button_text_idle_color = gui.idle_color
define gui.button_text_hover_color = gui.hover_color
define gui.button_text_selected_color = gui.selected_color
define gui.button_text_insensitive_color = gui.insensitive_color



define gui.button_text_xalign = 0.0








define gui.radio_button_borders = Borders(27 * persistent.scale_factor, 6 * persistent.scale_factor, 6 * persistent.scale_factor, 6 * persistent.scale_factor)

define gui.check_button_borders = Borders(27 * persistent.scale_factor, 6 * persistent.scale_factor, 6 * persistent.scale_factor, 6 * persistent.scale_factor)

define gui.confirm_button_text_xalign = 0.5

define gui.page_button_borders = Borders(15 * persistent.scale_factor, 6 * persistent.scale_factor, 15 * persistent.scale_factor, 6 * persistent.scale_factor)

define gui.quick_button_borders = Borders(15 * persistent.scale_factor, 6 * persistent.scale_factor, 15 * persistent.scale_factor, 0 * persistent.scale_factor)
define gui.quick_button_text_size = 21 * persistent.scale_factor
define gui.quick_button_text_idle_color = gui.idle_small_color
define gui.quick_button_text_selected_color = gui.accent_color












define gui.choice_button_width = 1185 * persistent.scale_factor
define gui.choice_button_height = None
define gui.choice_button_tile = False
define gui.choice_button_borders = Borders(150 * persistent.scale_factor, 12 * persistent.scale_factor, 150 * persistent.scale_factor, 8 * persistent.scale_factor)
define gui.choice_button_text_font = gui.text_font
define gui.choice_button_text_size = gui.text_size * persistent.scale_factor
define gui.choice_button_text_xalign = 0.5
define gui.choice_button_text_idle_color = "#474747"
define gui.choice_button_text_hover_color = "#ffffff"











define gui.slot_button_width = 370 * persistent.scale_factor
define gui.slot_button_height = 260 * persistent.scale_factor
define gui.slot_button_borders = Borders(10 * persistent.scale_factor, 10 * persistent.scale_factor, 10 * persistent.scale_factor, 10 * persistent.scale_factor)
define gui.slot_button_text_size = 25 * persistent.scale_factor
define gui.slot_button_text_xalign = 0.5
define gui.slot_button_text_yalign = 0.9
define gui.slot_button_text_idle_color = gui.idle_small_color
define gui.slot_button_text_selected_idle_color = gui.selected_color
define gui.slot_button_text_selected_hover_color = gui.hover_color




define config.thumbnail_width = 354 * persistent.scale_factor + (20 * (persistent.scale_factor-1))
define config.thumbnail_height = 191 * persistent.scale_factor + (20 * (persistent.scale_factor-1))


define gui.file_slot_cols = 4
define gui.file_slot_rows = 3









define gui.navigation_xpos = 60 * persistent.scale_factor


define gui.skip_ypos = 15 * persistent.scale_factor


define gui.notify_ypos = 68 * persistent.scale_factor


define gui.choice_spacing = 33 * persistent.scale_factor


define gui.navigation_spacing = 6 * persistent.scale_factor


define gui.pref_spacing = 10 * persistent.scale_factor


define gui.pref_button_spacing = 0 * persistent.scale_factor


define gui.page_spacing = 0 * persistent.scale_factor


define gui.slot_spacing = 5 * persistent.scale_factor


define gui.main_menu_text_xalign = 1.0








define gui.frame_borders = Borders(6 * persistent.scale_factor, 6 * persistent.scale_factor, 6 * persistent.scale_factor, 6 * persistent.scale_factor)


define gui.confirm_frame_borders = Borders(60 * persistent.scale_factor, 60 * persistent.scale_factor, 60 * persistent.scale_factor, 60 * persistent.scale_factor)


define gui.skip_frame_borders = Borders(24 * persistent.scale_factor, 8 * persistent.scale_factor, 75 * persistent.scale_factor, 8 * persistent.scale_factor)


define gui.notify_frame_borders = Borders(24 * persistent.scale_factor, 8 * persistent.scale_factor, 60 * persistent.scale_factor, 8 * persistent.scale_factor)


define gui.frame_tile = False











define gui.bar_size = 38 * persistent.scale_factor
define gui.scrollbar_size = 18 * persistent.scale_factor
define gui.slider_size = 38 * persistent.scale_factor


define gui.bar_tile = False
define gui.scrollbar_tile = False
define gui.slider_tile = False


define gui.bar_borders = Borders(6 * persistent.scale_factor, 6 * persistent.scale_factor, 6 * persistent.scale_factor, 6 * persistent.scale_factor)
define gui.scrollbar_borders = Borders(6 * persistent.scale_factor, 6 * persistent.scale_factor, 6 * persistent.scale_factor, 6 * persistent.scale_factor)
define gui.slider_borders = Borders(6 * persistent.scale_factor, 6 * persistent.scale_factor, 6 * persistent.scale_factor, 6 * persistent.scale_factor)


define gui.vbar_borders = Borders(6 * persistent.scale_factor, 6 * persistent.scale_factor, 6 * persistent.scale_factor, 6 * persistent.scale_factor)
define gui.vscrollbar_borders = Borders(6 * persistent.scale_factor, 6 * persistent.scale_factor, 6 * persistent.scale_factor, 6 * persistent.scale_factor)
define gui.vslider_borders = Borders(6 * persistent.scale_factor, 6 * persistent.scale_factor, 6 * persistent.scale_factor, 6 * persistent.scale_factor)



define gui.unscrollable = "hide"







define config.history_length = 250



define gui.history_height = 120 * persistent.scale_factor




define gui.history_name_xpos = 233 * persistent.scale_factor
define gui.history_name_ypos = 0 * persistent.scale_factor
define gui.history_name_width = 233 * persistent.scale_factor
define gui.history_name_xalign = 1.0


define gui.history_text_xpos = 255 * persistent.scale_factor
define gui.history_text_ypos = 3 * persistent.scale_factor
define gui.history_text_width = 1110 * persistent.scale_factor
define gui.history_text_xalign = 0.0







define gui.nvl_borders = Borders(0 * persistent.scale_factor, 15 * persistent.scale_factor, 0 * persistent.scale_factor, 30 * persistent.scale_factor)



define gui.nvl_list_length = 6



define gui.nvl_height = 173 * persistent.scale_factor



define gui.nvl_spacing = 15 * persistent.scale_factor



define gui.nvl_name_xpos = 645 * persistent.scale_factor
define gui.nvl_name_ypos = 0 * persistent.scale_factor
define gui.nvl_name_width = 225 * persistent.scale_factor
define gui.nvl_name_xalign = 1.0


define gui.nvl_text_xpos = 675 * persistent.scale_factor
define gui.nvl_text_ypos = 12 * persistent.scale_factor
define gui.nvl_text_width = 885 * persistent.scale_factor
define gui.nvl_text_xalign = 0.0



define gui.nvl_thought_xpos = 360 * persistent.scale_factor
define gui.nvl_thought_ypos = 0 * persistent.scale_factor
define gui.nvl_thought_width = 1170 * persistent.scale_factor
define gui.nvl_thought_xalign = 0.0


define gui.nvl_button_xpos = 675 * persistent.scale_factor
define gui.nvl_button_xalign = 0.0







define gui.language = "unicode"






























init python:
    def pick_style_default():
        style.window.background = Image("%s/gui/onepixel.png" % persistent.img_dir, xalign=0.5, yalign=1.0)
        
        style.say_dialogue.xsize = 1116 * persistent.scale_factor
        style.say_dialogue.xpos = 402 * persistent.scale_factor
        style.say_dialogue.xalign = 0.0
        style.say_dialogue.text_align = 0.0
        style.say_dialogue.xoffset = 402 * persistent.scale_factor
        style.namebox.xalign= 0.0
        style.say_label.xpos = 0 * persistent.scale_factor
        style.say_label.xoffset = 360 * persistent.scale_factor
        style.say_label.text_align = 0.0
        style.say_label.xalign = 0.0
        style.rebuild()
        return

    def pick_style_centered():
        style.window.background = Image("%s/gui/textbox_new.png" % persistent.img_dir, xalign=0.5, yalign=1.0)
        style.say_dialogue.xsize = 950 * persistent.scale_factor
        style.say_dialogue.xpos = 498 * persistent.scale_factor
        style.say_dialogue.xalign = 0.5
        style.say_dialogue.text_align = 0.5
        style.say_dialogue.xoffset = 0 * persistent.scale_factor
        style.namebox.xalign=0.5
        style.say_label.xoffset = 0 * persistent.scale_factor
        style.say_label.text_align = 0.5
        style.say_label.xalign = 0.5
        style.rebuild()
        return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

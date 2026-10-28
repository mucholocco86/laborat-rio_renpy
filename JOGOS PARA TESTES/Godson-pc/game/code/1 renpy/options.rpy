





init python:
    config.keymap["anykey"] = [
    'K_q','K_w','K_e','K_r','K_t','K_y','K_u','K_i','K_o','K_p',
    'K_a','K_s','K_d','K_f','K_g','K_h','K_j','K_k','K_l',
    'K_z','K_x','K_c','K_v','K_b','K_n','K_m'
]




define config.name = _("Godson")




define gui.show_name = True




define config.version = "0.3.1"




define config.default_fullscreen = True




init 999 python:
    if not persistent._set_preferences:
        _preferences.gl_powersave = False
        
        if renpy.windows:
            _preferences.renderer = "angle2"


define gui.about = _p("""
""")


define build.directory_name = "Godson"




define build.name = "Godson v0.3.1"







define config.has_sound = True
define config.has_music = True
define config.has_voice = True



define config.main_menu_music = "music/Godson Theme.wav"
define config.main_menu_music_fadein = 0.0
























define config.enter_transition = dissolve
define config.exit_transition = dissolve




define config.intra_transition = dissolve




define config.after_load_transition = None




define config.end_game_transition = None















define config.window = "auto"




define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)







default preferences.text_cps = 135





default preferences.afm_time = 15
















define config.save_directory = "Godson Remake-999999999"

define config.mouse = {
    "default": [("gui/cursor_default2.png", 0, 0)],
    "good": [("gui/cursor_default2good.png", 0, 0)],
    "supergood": [("gui/cursor_defaultsupergood.png", 0, 0)],
    "evil": [("gui/cursor_defaultevil.png", 0, 0)],
    "netural": [("gui/cursor_default2netural.png", 0, 0)],
    "sexaddict": [("gui/cursor_default2sexaddict.png", 0, 0)],
    "superevil": [("gui/cursor_defaultsuperevil.png", 0, 0)],
}







define config.windows_icon = "game"


define config.window_icon = "gui/window_icon.png"







init python:




















    build.classify('**~', None)
    build.classify('**.rpy', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)



    build.classify('game/**.**', 'archive')

    build.archive("archive", "all")



    build.documentation('*.html')
    build.documentation('*.txt')
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

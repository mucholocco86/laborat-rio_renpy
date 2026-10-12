








default persistent.enable_save_name = 1
default persistent.v_sounds_text_on = True
default persistent.v_musicplayer_available = True
default persistent.v_textbox_dialogue = False
default persistent.dialogueBoxOpacity = 1.0
default persistent.v_allow_previous_names = False






define config.name = _("Thief of Hearts Part 1")





define gui.show_name = False




define config.version = "0.0.3b"


define config.mouse = { }
define config.mouse['new'] = [ ( "gui/mouse_cursor_0.png", 0, 0) ]





define gui.about = _p("""
""")






define build.name = "ThiefofHeartsPart1"








define config.has_sound = True
define config.has_music = True
define config.has_voice = True

init -1 python:
    renpy.music.register_channel("movies_with_sound", mixer="sfx", loop=False, stop_on_mute=True, movie=True) 
    renpy.music.register_channel("music2", mixer="music", loop=False, stop_on_mute=True, movie=False) 
    renpy.music.register_channel("sex1", mixer="sex", loop=False, stop_on_mute=True, movie=False) 
    renpy.music.register_channel("sex2", mixer="sex", loop=False, stop_on_mute=True, movie=False) 
    renpy.music.register_channel("sex3", mixer="sex", loop=False, stop_on_mute=True, movie=False) 
    renpy.music.register_channel("sex4", mixer="sex", loop=False, stop_on_mute=True, movie=False) 
    renpy.music.register_channel("sound2", mixer="sfx", loop=False, stop_on_mute=True, movie=False) 
    renpy.music.register_channel("sound3", mixer="sfx", loop=False, stop_on_mute=True, movie=False) 
    renpy.music.register_channel("sound4", mixer="sfx", loop=False, stop_on_mute=True, movie=False) 
    renpy.music.register_channel("ambient", mixer="sfx", loop=False, stop_on_mute=True, movie=False) 
    renpy.music.register_channel("ambient2", mixer="sfx", loop=False, stop_on_mute=True, movie=False) 
    renpy.music.register_channel("ambient3", mixer="sfx", loop=False, stop_on_mute=True, movie=False) 
































default persistent.mm_music = "default"












define fast_dissolve = { "master": Dissolve(0.5) }
define faster_dissolve = { "master": Dissolve(0.2) }
define slow_dissolve = { "master": Dissolve(1.5) }
define normal_dissolve = { "master": Dissolve(1.0) }

init python:

    config.layers = [ 'master', 'transient', 'anim_layer','anim_layer_2','screens', 'overlay', 'ontop']

init -1:
    transform tt_top:
        xpos 0
        ypos -1920
        easein 6 xpos 0 ypos 0

    transform tt_bottom:
        xpos 0
        ypos 0
        easein 9 xpos 0 ypos -1920

    transform tt_side:
        xpos 0
        ypos 0
        easein 6 xpos -1200 ypos 0



define config.enter_transition = dissolve
define config.exit_transition = dissolve




define config.intra_transition = dissolve




define config.after_load_transition = None




define config.end_game_transition = None






init python:
    import locale
    myloacl=(locale.getdefaultlocale())[0]













define config.window = "hide"




define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)







default preferences.text_cps = 45





default preferences.afm_time = 15
















define config.save_directory = "ThiefofHearts-Saves"






define config.window_icon = "gui/window_icon.png"






init python:




















    build.archive("misc_images", "all")
    build.archive("rewards", "all")


    build.archive("01_sound_effects", "all")
    build.archive("01_img", "all")
    build.archive("01_scripts", "all")
    build.archive("01_extras", "all")


    build.archive("02_sound_effects", "all")
    build.archive("02_img", "all")
    build.archive("02_scripts", "all")
    build.archive("02_extras", "all")

    build.archive("03_sound_effects", "all")
    build.archive("03_img", "all")
    build.archive("03_scripts", "all")
    build.archive("03_extras", "all")

    build.classify("game/sound effects/01/**.**", "01_sound_effects")
    build.classify("game/images/Episode 01/**.**", "01_img")
    build.classify("game/scripts/Episode 01/**.**", "01_scripts")
    build.classify("game/images/Extras/Episode 01/**.**", "01_extras")

    build.classify("game/sound effects/02/**.**", "02_sound_effects")
    build.classify("game/images/Episode 02/**.**", "02_img")
    build.classify("game/scripts/Episode 02/**.**", "02_scripts")
    build.classify("game/images/Extras/Episode 02/**.**", "02_extras")

    build.classify("game/sound effects/03/**.**", "03_sound_effects")
    build.classify("game/images/Episode 03/**.**", "03_img")
    build.classify("game/scripts/Episode 03/**.**", "03_scripts")
    build.classify("game/images/Extras/Episode 03/**.**", "03_extras")


    build.classify("game/images/**.**", "misc_images")






    build.classify('**~', None)
    build.classify('**.rpy', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    build.classify('**/desktop.ini', None)



    build.classify("game/**.png", "archive")
    build.classify("game/**.webm", "archive")
    build.classify("game/**.jpg", "archive")
    build.classify("game/**.rpy", "archive")
    build.classify("game/**.rpyc", "archive")
    build.classify("game/**.**", "archive")





    build.documentation('*.html')
    build.documentation('*.txt')
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

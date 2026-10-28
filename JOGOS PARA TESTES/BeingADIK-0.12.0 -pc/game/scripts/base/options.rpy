













define config.name = _("Being a DIK")





define gui.show_name = True




define config.version = "0.12.0"





define gui.about = _p("""
""")






define build.name = "BeingADIK"







define config.has_sound = True
define config.has_music = True
define config.has_voice = True











if persistent.mm_song[1] == None:
    define config.main_menu_music = "Dirty Toy Company - Over the Horizon","music/patched/track_previous.mp3"
else:
    define config.main_menu_music = persistent.mm_song[1]










define config.enter_transition = dissolve
define config.exit_transition = dissolve




define config.intra_transition = dissolve




define config.after_load_transition = None




define config.end_game_transition = None
















define config.window = "auto"




define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)







default preferences.text_cps = 0





default preferences.afm_time = 15


















define config.save_directory = "BeingaDIKSeason3-Patreon-1535311494"
define config.default_fullscreen = False












define config.window_icon = "gui/window_icon.png"






init python:



















    build.archive("scripts", "all")
    build.archive("base", "all")
    build.archive("images", "all")
    build.archive("movies", "all")
    build.archive("gui", "all")
    build.archive("images_4k", "all")
    build.archive("movies_4k", "all")
    build.archive("gui_4k", "all")
    build.archive("sound", "all")
    build.archive("gallery", "all")
    build.archive("gallery_4k", "all")
    build.archive("fonts", "all")
    build.archive("movies_ep_interlude", "all")
    build.archive("movies_ep9", "all")
    build.archive("movies_ep10", "all")
    build.archive("movies_ep11", "all")
    build.archive("movies_ep12", "all")
    build.archive("movies_ep_interlude_4k", "all")
    build.archive("movies_ep9_4k", "all")
    build.archive("movies_ep10_4k", "all")
    build.archive("movies_ep11_4k", "all")
    build.archive("movies_ep12_4k", "all")
    build.archive("minigames", "all")
    build.archive("minigames_4k", "all")
    build.archive("start_images", "all")
    build.archive("start_images_4k", "all")

    build.archive("music_ep1", "all")
    build.archive("music_ep2", "all")
    build.archive("music_ep3", "all")
    build.archive("music_ep4", "all")
    build.archive("music_ep5", "all")
    build.archive("music_ep6", "all")
    build.archive("music_ep7", "all")
    build.archive("music_ep8", "all")
    build.archive("music_epi", "all")
    build.archive("music_ep9", "all")
    build.archive("music_ep10", "all")
    build.archive("music_ep11", "all")
    build.archive("music_ep12", "all")
    build.archive("ep_interlude_images", "all")
    build.archive("ep9_images", "all")
    build.archive("ep9_patch", "all")
    build.archive("ep10_images", "all")
    build.archive("phone", "all")
    build.archive("ep10_patch", "all")
    build.archive("ep11_images", "all")
    build.archive("ep12_images", "all")

    build.archive("scripts_4k", "all")
    build.archive("ep_interlude_images_4k", "all")
    build.archive("ep9_images_4k", "all")
    build.archive("ep9_patch_4k", "all")
    build.archive("ep10_images_4k", "all")
    build.archive("phone_4k", "all")
    build.archive("ep10_patch_4k", "all")
    build.archive("ep11_images_4k", "all")
    build.archive("ep12_images_4k", "all")






    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    build.classify("game/**.rpy", None)
    build.classify('**.docx', None)
    build.classify('**.txt', None)
    build.classify('**.bat', None)

    build.classify("game/images/start_images/**.**", "start_images")
    build.classify("game/images_4k/start_images/**.**", "start_images_4k")

    build.classify("game/images/movies/ep12/**.**","movies_ep12")
    build.classify("game/images/ep12/**.**", "ep12_images")
    build.classify("game/images/phone_content/ep12/**.**", "ep12_images")
    build.classify("game/images/rewards/ep12/**.**", "ep12_images")

    build.classify("game/images_4k/movies/ep12/**.**","movies_ep12_4k")
    build.classify("game/images_4k/ep12/**.**", "ep12_images_4k")
    build.classify("game/images_4k/phone_content/ep12/**.**", "ep12_images_4k")
    build.classify("game/images_4k/rewards/ep12/**.**", "ep12_images_4k")


    build.classify("game/images/movies/ep11/**.**","movies_ep11")
    build.classify("game/images/ep11/**.**", "ep11_images")
    build.classify("game/images/phone_content/ep11/**.**", "ep11_images")
    build.classify("game/images/rewards/ep11/**.**", "ep11_images")

    build.classify("game/images_4k/movies/ep11/**.**","movies_ep11_4k")
    build.classify("game/images_4k/ep11/**.**", "ep11_images_4k")
    build.classify("game/images_4k/phone_content/ep11/**.**", "ep11_images_4k")
    build.classify("game/images_4k/rewards/ep11/**.**", "ep11_images_4k")


    build.classify("game/images/movies/ep10/**.**","movies_ep10")
    build.classify("game/images/ep10/patched/**.**", "ep10_patch")
    build.classify("game/images/ep10/**.**", "ep10_images")
    build.classify("game/images/phone_content/ep10/**.**", "ep10_images")
    build.classify("game/images/rewards/ep10/**.**", "ep10_images")
    build.classify("game/images/minigames/**.**", "minigames")

    build.classify("game/images_4k/movies/ep10/**.**","movies_ep10_4k")
    build.classify("game/images_4k/ep10/patched/**.**", "ep10_patch_4k")
    build.classify("game/images_4k/ep10/**.**", "ep10_images_4k")
    build.classify("game/images_4k/phone_content/ep10/**.**", "ep10_images_4k")
    build.classify("game/images_4k/rewards/ep10/**.**", "ep10_images_4k")
    build.classify("game/images_4k/minigames/**.**", "minigames_4k")


    build.classify("game/images/movies/ep9/**.**","movies_ep9")
    build.classify("game/images/ep9/patched/**.**", "ep9_patch")
    build.classify("game/images/ep9/**.**", "ep9_images")
    build.classify("game/images/phone_content/ep9/**.**", "ep9_images")
    build.classify("game/images/rewards/ep9/**.**", "ep9_images")
    build.classify("game/images/ep8/freeroam_desk/**.**", "ep9_images")

    build.classify("game/images_4k/movies/ep9/**.**","movies_ep9_4k")
    build.classify("game/images_4k/ep9/patched/**.**", "ep9_patch_4k")
    build.classify("game/images_4k/ep9/**.**", "ep9_images_4k")
    build.classify("game/images_4k/phone_content/ep9/**.**", "ep9_images_4k")
    build.classify("game/images_4k/rewards/ep9/**.**", "ep9_images_4k")
    build.classify("game/images_4k/ep8/freeroam_desk/**.**", "ep9_images_4k")


    build.classify("game/images/movies/epi/**.**","movies_ep_interlude")
    build.classify("game/images/ep_interlude/**.**", "ep_interlude_images")
    build.classify("game/images/phone_content/episode_interlude/**.**", "ep_interlude_images")
    build.classify("game/images/ep8/**.**", "ep_interlude_images")
    build.classify("game/images/new_phone/**.**", "phone")
    build.classify("game/images/rewards/epi/**.**", "ep_interlude_images")

    build.classify("game/images_4k/movies/epi/**.**","movies_ep_interlude_4k")
    build.classify("game/images_4k/ep_interlude/**.**", "ep_interlude_images_4k")
    build.classify("game/images_4k/phone_content/episode_interlude/**.**", "ep_interlude_images_4k")
    build.classify("game/images_4k/ep8/**.**", "ep_interlude_images_4k")
    build.classify("game/images_4k/new_phone/**.**", "phone_4k")
    build.classify("game/images_4k/rewards/epi/**.**", "ep_interlude_images_4k")

    build.classify("game/scripts/4k.rpyc", "scripts_4k")
    build.classify("game/*.rpyc", "scripts")
    build.classify("game/scripts/**.**", "scripts")
    build.classify("game/images/classes/**.**", "images")
    build.classify("game/images/freeroam_common/**.**", "images")
    build.classify("game/images_4k/classes/**.**", "images_4k")
    build.classify("game/images_4k/freeroam_common/**.**", "images_4k")
    build.classify("game/music/ep1/**.**","music_ep1")
    build.classify("game/music/ep2/**.**","music_ep2")
    build.classify("game/music/ep3/**.**","music_ep3")
    build.classify("game/music/ep4/**.**","music_ep4")
    build.classify("game/music/ep5/**.**","music_ep5")
    build.classify("game/music/ep6/**.**","music_ep6")
    build.classify("game/music/ep7/**.**","music_ep7")
    build.classify("game/music/ep8/**.**","music_ep8")
    build.classify("game/music/ep_interlude/**.**","music_epi")
    build.classify("game/music/ep9/**.**","music_ep9")
    build.classify("game/music/ep10/**.**","music_ep10")
    build.classify("game/music/ep11/**.**","music_ep11")
    build.classify("game/music/ep12/**.**","music_ep12")
    build.classify("game/sound_effects/**.**","sound")
    build.classify("game/images_4k/rewards/**.**", "images_4k")
    build.classify("game/images_4k/movies/**.**","movies_4k")
    build.classify("game/images/rewards/**.**", "images")
    build.classify("game/images/movies/**.**","movies")
    build.classify("game/fonts/**.**", "fonts")

    build.classify("game/images/gallery/**.**", "gallery")
    build.classify("game/images/gui/**.**", "gui")
    build.classify("game/images/**.**", "images")
    build.classify("game/images_4k/gallery/**.**", "gallery_4k")
    build.classify("game/images_4k/gui/**.**", "gui_4k")
    build.classify("game/images_4k/**.**", "images_4k")
    build.classify("game/gui/**.**", "gui")

    build.classify("game/**.png", "archive")
    build.classify("game/**.ico", "archive")
    build.classify("game/**.icns", "archive")
    build.classify("game/**.webm", "archive")

    build.classify("game/**.rpyc", "archive")
    build.classify("game/**.mp3", "archive")


    build.documentation('*.html')
    build.documentation('*.txt')
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

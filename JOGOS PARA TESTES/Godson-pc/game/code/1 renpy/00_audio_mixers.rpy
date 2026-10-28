





define godson_default_music_volume = 1.0
define godson_default_sfx_volume = 1.0
define godson_default_animation_volume = 0.80
define godson_default_voice_volume = 0.85
define godson_default_other_volume = 1.0




define config.movie_mixer = "animation"




init 999 python:
    renpy.music.register_channel(
    "movie",
    mixer="animation",
    loop=False,
    stop_on_mute=False,
    movie=True,
)




default preferences.volume.music = godson_default_music_volume
default preferences.volume.sfx = godson_default_sfx_volume
default preferences.volume.animation = godson_default_animation_volume
default preferences.volume.voice = godson_default_voice_volume
default preferences.volume.other = godson_default_other_volume
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

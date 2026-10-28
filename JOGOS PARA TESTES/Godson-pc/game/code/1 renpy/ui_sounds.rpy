init offset = -1








init -1 python:

    _godson_ui_channels = tuple(
    "ui_sfx_{:02d}".format(i) for i in range(1, 17)
)

    for _godson_ui_channel in _godson_ui_channels:
        renpy.music.register_channel(
        _godson_ui_channel,
        mixer="ui_sfx",
        loop=False,
    )


    _godson_original_play = getattr(
    renpy.exports,
    "_godson_original_play",
    renpy.exports.play,
)
    renpy.exports._godson_original_play = _godson_original_play

    _godson_ui_next_channel = 0

    def _godson_play_with_ui_overlap(filename, channel=None, **kwargs):
        global _godson_ui_next_channel
        
        
        
        
        if channel is not None:
            return _godson_original_play(filename, channel=channel, **kwargs)
        
        channel_count = len(_godson_ui_channels)
        
        
        for offset in range(channel_count):
            index = (_godson_ui_next_channel + offset) % channel_count
            candidate = _godson_ui_channels[index]
            
            if not renpy.music.is_playing(candidate):
                _godson_ui_next_channel = (index + 1) % channel_count
                return _godson_original_play(
                filename,
                channel=candidate,
                **kwargs
            )
        
        
        
        candidate = _godson_ui_channels[_godson_ui_next_channel]
        _godson_ui_next_channel = (
        _godson_ui_next_channel + 1
    ) % channel_count
        
        return _godson_original_play(filename, channel=candidate, **kwargs)

    renpy.exports.play = _godson_play_with_ui_overlap


    renpy.play = _godson_play_with_ui_overlap



style button:
    hover_sound "music/uihoversound2.wav"
    activate_sound "music/uiclicksound3.wav"




style quick_button:
    hover_sound "music/uihoversound2.wav"
    activate_sound "music/uiclicksound3.wav"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

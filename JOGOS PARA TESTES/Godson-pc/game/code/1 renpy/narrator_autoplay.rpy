





default persistent.narrator_autoplay = True
default _narrator_autoplay_generation = 0
default _narrator_autoplay_active = False
default _narrator_autoplay_voice_seen = False
default _narrator_autoplay_voice_finished_at = None

define NARRATOR_AUTOPLAY_DELAY = 0.5


init 100 python:
    import time

    def narrator_autoplay_character_callback(event, interact=True, **kwargs):
        """
    Arms narrator autoplay for one narrator line without changing the
    player's normal Auto preference.
    """
        
        if event == "begin":
            store._narrator_autoplay_generation += 1
            store._narrator_autoplay_active = bool(
            interact and persistent.narrator_autoplay
        )
            store._narrator_autoplay_voice_seen = False
            store._narrator_autoplay_voice_finished_at = None
        
        elif event == "end":
            store._narrator_autoplay_active = False
            store._narrator_autoplay_voice_seen = False
            store._narrator_autoplay_voice_finished_at = None


    class NarratorVoiceAutoAdvance(Action):
        """
    Watches the voice channel for the currently displayed narrator line.
    Returning True ends only that say interaction, exactly like a normal
    dismiss click.
    """
        
        def __init__(self, generation):
            self.generation = generation
        
        def __call__(self):
            if self.generation != store._narrator_autoplay_generation:
                return None
            
            if not persistent.narrator_autoplay:
                return None
            
            if not store._narrator_autoplay_active:
                return None
            
            if renpy.music.is_playing(channel="voice"):
                store._narrator_autoplay_voice_seen = True
                store._narrator_autoplay_voice_finished_at = None
                return None
            
            if store._narrator_autoplay_voice_seen:
                if store._narrator_autoplay_voice_finished_at is None:
                    store._narrator_autoplay_voice_finished_at = time.time()
                    return None
                
                elapsed = (
                time.time()
                - store._narrator_autoplay_voice_finished_at
            )
                
                if elapsed >= NARRATOR_AUTOPLAY_DELAY:
                    store._narrator_autoplay_active = False
                    store._narrator_autoplay_voice_seen = False
                    store._narrator_autoplay_voice_finished_at = None
                    return True
            
            return None


init 101 python:


    nar = Character(
    "Narrator",
    callback=narrator_autoplay_character_callback,
)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

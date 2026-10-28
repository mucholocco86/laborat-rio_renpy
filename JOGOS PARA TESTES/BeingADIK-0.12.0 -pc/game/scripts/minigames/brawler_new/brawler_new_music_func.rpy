init python:
    def bn_play_song(bn_list):
        global mphone_music_genre
        renpy.music.stop("music",1)
        
        renpy.music.set_volume(1.0,channel='music')
        renpy.sound.set_volume(1.0,channel='sfx1')
        renpy.sound.set_volume(1.0,channel='sfx2')
        if not bn_list:
            mphone_music_genre = 4
            mphone_next_song()
            return
        current_music_list = []
        
        current_music_list.append("music/ep1/credits.mp3")
        current_music_list.append("music/ep1/emptyv.mp3")
        current_music_list.append("music/ep1/food_chain.mp3")
        current_music_list.append("music/ep1/time_goes_by.mp3")
        current_music_list.append("music/ep2/heavy.mp3")
        current_music_list.append("music/ep2/metal.mp3")
        current_music_list.append("music/ep4/driving_rock.mp3")
        current_music_list.append("music/ep4/drum_bass.mp3")
        current_music_list.append("music/ep7/licensed_music/track46.mp3")
        current_music_list.append("music/ep9/licensed_music/track118.mp3")
        current_music_list.append("music/ep_interlude/licensed_music/track95.mp3")
        current_music_list.append("music/ep_interlude/licensed_music/track96.mp3")
        current_music_list.append("music/ep_interlude/licensed_music/track104.mp3")
        current_music_list.append("music/ep_interlude/licensed_music/track105.mp3")
        current_music_list.append("music/ep10/faked_reality.mp3")
        current_music_list.append("music/ep10/isolation.mp3")
        current_music_list.append("music/ep10/see_you_smile.mp3")
        current_music_list.append("music/ep10/licensed_music/burn_you_down.mp3")
        current_music_list.append("music/ep10/licensed_music/over_the_horizon.mp3")
        current_music_list.append("music/ep10/licensed_music/stand_and_fight.mp3")
        
        renpy.random.shuffle(current_music_list)
        renpy.music.play(current_music_list[len(current_music_list)-1])
        renpy.music.queue(current_music_list)
        return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

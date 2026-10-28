init python:
    def mphone_next_song():
        global mphone_music_favs
        global mphone_music_genre
        renpy.music.stop("music",1)
        mphone_current_music_list = []
        for x in range(0,len(persistent.mphone_music_list)):
            if mphone_music_genre == 0 or (mphone_music_genre == 4 and persistent.mphone_music_list[x][2]) or (mphone_music_genre == persistent.mphone_music_list[x][3]):
                mphone_current_music_list.append(persistent.mphone_music_list[x][1])
        if len(mphone_current_music_list) > 0:
            renpy.random.shuffle(mphone_current_music_list)
            renpy.music.play(mphone_current_music_list[len(mphone_current_music_list)-1])
            renpy.music.queue(mphone_current_music_list)
        return

    def mphone_next_genre():
        global mphone_genre_list
        global mphone_genre_count
        
        if mphone_genre_count+1< len(mphone_genre_list):
            mphone_genre_count += 1
        else:
            mphone_genre_count = 0
        return

    def mphone_play_song(i):
        global mphone_music_favs
        global mphone_music_genre
        renpy.music.stop("music",1)
        mphone_current_music_list = []
        for x in range(0,len(persistent.mphone_music_list)):
            if mphone_music_genre == 0 or (mphone_music_genre == 4 and persistent.mphone_music_list[x][2]) or (mphone_music_genre == persistent.mphone_music_list[x][3]):
                mphone_current_music_list.append(persistent.mphone_music_list[x][1])
        renpy.random.shuffle(mphone_current_music_list)
        mphone_current_music_list.append(i)
        renpy.music.play(mphone_current_music_list[len(mphone_current_music_list)-1])
        renpy.music.queue(mphone_current_music_list)
        return

    def mphone_play_songs(list):
        global mphone_music_favs
        global mphone_music_genre
        renpy.music.stop("music",1)
        mphone_current_music_list = []
        for x in range(0,len(persistent.mphone_music_list)):
            if mphone_music_genre == 0 or (mphone_music_genre == 4 and persistent.mphone_music_list[x][2]) or (mphone_music_genre == persistent.mphone_music_list[x][3]):
                mphone_current_music_list.append(persistent.mphone_music_list[x][1])
        renpy.random.shuffle(mphone_current_music_list)
        for i in reversed(list):
            mphone_current_music_list.insert(0,i)
        renpy.music.play(mphone_current_music_list[0])
        del mphone_current_music_list[0]
        renpy.music.queue(mphone_current_music_list)
        return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

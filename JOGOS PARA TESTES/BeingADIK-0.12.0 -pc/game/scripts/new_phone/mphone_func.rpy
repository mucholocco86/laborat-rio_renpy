init python:
    def mphone_init_phone_screen():
        global mphone_use_favs
        global mphone_wallpaper_list
        global mphone_current_wallpaper
        global mphone_bios_app_exception
        
        mphone_bios_app_exception = False
        if mphone_use_favs:
            tmpList = []
            for x in range(0,len(mphone_wallpaper_list)):
                if mphone_wallpaper_list[x][1]:
                    tmpList.append(x)
            if len(tmpList) > 0:
                renpy.random.shuffle(tmpList)
                mphone_current_wallpaper = tmpList[0]
        mphone_count_notifications()
        renpy.start_predict_screen("mphone_bios_app_screen")
        return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

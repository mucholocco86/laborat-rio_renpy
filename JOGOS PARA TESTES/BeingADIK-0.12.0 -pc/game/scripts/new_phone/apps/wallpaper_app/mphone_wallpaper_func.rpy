init python:
    def unlock_wallpapers_s2():
        global mphone_wallpaper_list
        for x in range(0,len(persistent.art_unlocked_lvl1)):
            if persistent.art_unlocked_lvl1[x] and len(persistent.art_unlocked_lvl1) == len(mphone_wallpaper_list)-2:
                mphone_wallpaper_list[x+2][2] = True
            elif persistent.art_unlocked_lvl1[x] and len(persistent.art_unlocked_lvl1) == len(mphone_wallpaper_list):
                if x < 10:
                    mphone_wallpaper_list[x+2][2] = True
                elif x > 10:
                    mphone_wallpaper_list[x+2][2] = True
        
        
        
        
        
        
        
        return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

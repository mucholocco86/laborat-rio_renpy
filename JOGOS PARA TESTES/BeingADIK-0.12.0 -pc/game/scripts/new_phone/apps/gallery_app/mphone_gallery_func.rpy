init python:
    def CustomWallpaperMask(d):
        return AlphaMask(d,"mphone_screen_alpha2")
    def mgallery_init_chat_album():
        global mphone_chat_history_list
        global mphone_app_gallery_photos_list
        global mphone_app_gallery_new
        for idx in range(0,len(mphone_chat_history_list)):
            if mphone_chat_history_list[idx][0] == "Jade":
                if "chat_jade_pic2_ep7_thumb" in mphone_chat_history_list[idx][2]:
                    mphone_app_gallery_photos_list.insert(0,"chat_jade_pic2_ep7_zoomed")
                if "chat_jade_pic1_ep7_thumb" in mphone_chat_history_list[idx][2]:
                    mphone_app_gallery_photos_list.insert(0,"chat_jade_pic1_ep7_zoomed")
            
            if mphone_chat_history_list[idx][0] == "Quinn":
                if "chat_quinn_pic1_ep7_thumb" in mphone_chat_history_list[idx][2]:
                    mphone_app_gallery_photos_list.insert(0,"chat_quinn_pic1_ep7_zoomed")
            
            if mphone_chat_history_list[idx][0] == "Jill":
                if "chat_jill_pic3_ep7_thumb" in mphone_chat_history_list[idx][2]:
                    mphone_app_gallery_photos_list.insert(0,"chat_jill_pic3_ep7_zoomed")
                if "chat_jill_pic2_ep7_thumb" in mphone_chat_history_list[idx][2]:
                    mphone_app_gallery_photos_list.insert(0,"chat_jill_pic2_ep7_zoomed")
                if "chat_jill_pic1_ep7_thumb" in mphone_chat_history_list[idx][2]:
                    mphone_app_gallery_photos_list.insert(0,"chat_jill_pic1_ep7_zoomed")
        
        for idx in range(0,len(mphone_chat_history_list)):
            if mphone_chat_history_list[idx][0] == "Sage":
                if "chat_sage_pic1_ep8_thumb" in mphone_chat_history_list[idx][2]:
                    mphone_app_gallery_photos_list.insert(0,"chat_sage_pic1_ep8_zoomed")
            
            if mphone_chat_history_list[idx][0] == "Jade":
                if "chat_jade_pic2_ep8_thumb" in mphone_chat_history_list[idx][2]:
                    mphone_app_gallery_photos_list.insert(0,"chat_jade_pic2_ep8_zoomed")
                if "chat_jade_pic1_ep8_thumb" in mphone_chat_history_list[idx][2]:
                    mphone_app_gallery_photos_list.insert(0,"chat_jade_pic1_ep8_zoomed")
            
            if mphone_chat_history_list[idx][0] == "Maya":
                if "chat_maya_pic1_ep8_thumb" in mphone_chat_history_list[idx][2]:
                    mphone_app_gallery_photos_list.insert(0,"chat_maya_pic1_ep8_zoomed")
            
            if mphone_chat_history_list[idx][0] == "Nora":
                if "chat_nora_pic2_ep8_thumb" in mphone_chat_history_list[idx][2]:
                    mphone_app_gallery_photos_list.insert(0,"chat_nora_pic2_ep8_zoomed")
                if "chat_nora_pic1_ep8_thumb" in mphone_chat_history_list[idx][2]:
                    mphone_app_gallery_photos_list.insert(0,"chat_nora_pic1_ep8_zoomed")
        
        for idx in range(0,len(mphone_chat_history_list)):
            if mphone_chat_history_list[idx][0] == "Sage":
                if "chat_sage_pic3_ep9_thumb" in mphone_chat_history_list[idx][2]:
                    mphone_app_gallery_photos_list.insert(0,"chat_sage_pic3_ep9_zoomed")
                if "chat_sage_pic2_ep9_thumb" in mphone_chat_history_list[idx][2]:
                    mphone_app_gallery_photos_list.insert(0,"chat_sage_pic2_ep9_zoomed")
                if "chat_sage_pic1_ep9_thumb" in mphone_chat_history_list[idx][2]:
                    mphone_app_gallery_photos_list.insert(0,"chat_sage_pic1_ep9_zoomed")
        mphone_app_gallery_new = True
        return
    def mgallery_init_album():
        global ep9_photos
        global mphone_app_gallery_photos_list
        global mphone_app_gallery_new
        global branchJill
        global branchIsabella
        
        if not branchJill and not branchIsabella:
            mphone_app_gallery_photos_list.insert(0,"ep10_mains1_pic1")
        if branchIsabella:
            mphone_app_gallery_photos_list.insert(0,"ep10_mains2_pic1")
        if branchJill:
            mphone_app_gallery_photos_list.insert(0,"ep10_mains3_pic1")
        if not branchJill:
            mphone_app_gallery_photos_list.insert(0,"ep10_group6_pic1")
        mphone_app_gallery_photos_list.insert(0,"ep10_group5_pic1")
        mphone_app_gallery_photos_list.insert(0,"ep10_group4_pic1")
        mphone_app_gallery_photos_list.insert(0,"ep10_group3_pic1")
        mphone_app_gallery_photos_list.insert(0,"ep10_group2_pic1")
        mphone_app_gallery_photos_list.insert(0,"ep10_group1_pic1")
        mphone_app_gallery_photos_list.insert(0,"ep10_leon_pic2")
        mphone_app_gallery_photos_list.insert(0,"ep10_leon_pic1")
        mphone_app_gallery_photos_list.insert(0,"ep10_heather_pic1")
        mphone_app_gallery_photos_list.insert(0,"ep10_zoey_picture4")
        mphone_app_gallery_photos_list.insert(0,"ep10_zoey_picture3")
        mphone_app_gallery_photos_list.insert(0,"ep10_tommy_pic1")
        mphone_app_gallery_photos_list.insert(0,"ep10_tiffani_pic1")
        mphone_app_gallery_photos_list.insert(0,"ep10_nick_pic1")
        mphone_app_gallery_photos_list.insert(0,"ep10_becky_pic1")
        mphone_app_gallery_photos_list.insert(0,"ep10_derek_pic1")
        mphone_app_gallery_photos_list.insert(0,"ep10_elena_pic1")
        mphone_app_gallery_photos_list.insert(0,"ep10_jamie_pic1")
        
        if ep9_photos[0]:
            mphone_app_gallery_photos_list.insert(0,"ep10_camila_pic2")
        if ep9_photos[1]:
            mphone_app_gallery_photos_list.insert(0,"ep10_camila_pic1")
        if ep9_photos[2]:
            mphone_app_gallery_photos_list.insert(0,"ep10_isabella_pic1")
            mphone_app_gallery_photos_list.insert(0,"ep10_isabella_pic2")
        if ep9_photos[3]:
            mphone_app_gallery_photos_list.insert(0,"ep10_isabella_pic1")
            mphone_app_gallery_photos_list.insert(0,"ep10_isabella_pic3")
        if ep9_photos[4]:
            mphone_app_gallery_photos_list.insert(0,"ep10_jill_pic1")
            mphone_app_gallery_photos_list.insert(0,"ep10_jill_pic2")
            mphone_app_gallery_photos_list.insert(0,"ep10_jill_pic3")
        if ep9_photos[5]:
            mphone_app_gallery_photos_list.insert(0,"ep10_jm_pic1")
            mphone_app_gallery_photos_list.insert(0,"ep10_jm_pic2")
            mphone_app_gallery_photos_list.insert(0,"ep10_jm_pic4")
            mphone_app_gallery_photos_list.insert(0,"ep10_jm_pic5")
        if ep9_photos[6]:
            mphone_app_gallery_photos_list.insert(0,"ep10_jm_pic1")
            mphone_app_gallery_photos_list.insert(0,"ep10_jm_pic3")
            mphone_app_gallery_photos_list.insert(0,"ep10_jm_pic4")
            mphone_app_gallery_photos_list.insert(0,"ep10_jm_pic5")
        if ep9_photos[7]:
            mphone_app_gallery_photos_list.insert(0,"ep10_quinn_picture1")
            mphone_app_gallery_photos_list.insert(0,"ep10_quinn_picture2")
        if ep9_photos[8]:
            mphone_app_gallery_photos_list.insert(0,"ep10_quinn_picture1")
            mphone_app_gallery_photos_list.insert(0,"ep10_quinn_picture3")
        if ep9_photos[9]:
            mphone_app_gallery_photos_list.insert(0,"ep10_riona_pic1")
        if ep9_photos[10]:
            mphone_app_gallery_photos_list.insert(0,"ep10_sage_pic1")
            mphone_app_gallery_photos_list.insert(0,"ep10_sage_pic2")
            mphone_app_gallery_photos_list.insert(0,"ep10_sage_pic3")
        if ep9_photos[11]:
            mphone_app_gallery_photos_list.insert(0,"ep10_sage_pic1")
            mphone_app_gallery_photos_list.insert(0,"ep10_sage_pic2")
            mphone_app_gallery_photos_list.insert(0,"ep10_sage_pic4")
        if ep9_photos[12]:
            mphone_app_gallery_photos_list.insert(0,"ep10_sarah_melanie_pic1")
        if ep9_photos[13]:
            mphone_app_gallery_photos_list.insert(0,"ep10_sarah_melanie_pic2")
        if ep9_photos[14]:
            mphone_app_gallery_photos_list.insert(0,"ep10_zoey_picture1")
            mphone_app_gallery_photos_list.insert(0,"ep10_zoey_picture2")
        if ep9_photos[15]:
            mphone_app_gallery_photos_list.insert(0,"ep10_josy_pic1")
        if ep9_photos[16]:
            mphone_app_gallery_photos_list.insert(0,"ep10_sarah_melanie_pic4")
        if ep9_photos[17]:
            mphone_app_gallery_photos_list.insert(0,"ep10_sarah_melanie_pic3")
        mphone_app_gallery_new = True
        return

    def mgallery_add_photo(fname):
        global mphone_app_gallery_photos_list
        global mphone_app_gallery_new
        notify_photo = False
        if not fname in mphone_app_gallery_photos_list:
            mphone_app_gallery_photos_list.insert(0,fname)
            notify_photo = not mphone_app_gallery_new
            mphone_app_gallery_new = True
        if notify_photo:
            showNotificationMsg("Photo added to your phone gallery!")
        return

    def mphone_custom_wallpaper_get_width(fname):
        if fname == "chat_jade_pic1_ep8_zoomed" or fname == "chat_jade_pic2_ep8_zoomed" or fname == "chat_sage_pic1_ep8_zoomed":
            return 612
        if fname == "chat_jade_pic1_ep7_zoomed" or fname == "chat_jade_pic2_ep7_zoomed":
            return 678
        if fname == "chat_jill_pic1_ep7_zoomed" or fname == "chat_jill_pic2_ep7_zoomed" or fname == "chat_jill_pic3_ep7_zoomed":
            return 677
        if fname == "chat_maya_pic1_ep8_zoomed":
            return 680
        if fname == "chat_quinn_pic1_ep7_zoomed" or fname == "chat_sage_pic1_ep9_zoomed" or fname == "chat_sage_pic2_ep9_zoomed" or fname == "chat_sage_pic3_ep9_zoomed":
            return 665
        if fname == "chat_nora_pic1_ep8_zoomed" or fname == "chat_nora_pic2_ep8_zoomed":
            return 601
        if fname == "chat_jacob_pic1_ep10_zoomed":
            return 600
        if fname == "ep10_bella_solo_pic0" or fname == "ep10_bella_solo_pic2" or fname == "chat_rio_pic1_ep10_zoomed" or fname == "chat_rio_pic1b_ep10_zoomed" or fname == "ep10_bbq_lily_pic1" or fname == "ep10_josy_solo_pic1" or fname == "chat_derek_pic1_ep10_zoomed":
            return 720
        if fname == "ep10_jill_solo_pic1" or fname == "ep10_lily_english_pic" or fname == "ep10_quinn_solo_pic0":
            return 720
        if fname == "ep11_msolo_pic1" or fname == "chat_zoey_pic1_ep11_zoomed" or fname == "chat_zoey_pic2_ep11_zoomed":
            return 720
        if fname == "chat_sarah_pic1_ep11_zoomed" or fname == "chat_sage_pic3_ep11_zoomed" or fname == "chat_sage_pic2_ep11_zoomed" or fname == "chat_sage_pic1_ep11_zoomed":
            return 720
        if fname == "chat_nicole_pic1_ep11_zoomed" or fname == "chat_melanie_pic1_ep11_zoomed" or fname == "chat_melanie_pic2_ep11_zoomed":
            return 720
        if fname == "chat_lily_pic2_ep11_zoomed" or fname == "chat_lily_pic1_ep11_zoomed":
            return 720
        if fname == "chat_camila_pic1_ep11_zoomed" or fname == "chat_camila_pic2_ep11_zoomed" or fname == "chat_camila_pic3_ep11_zoomed":
            return 720
        if fname == "chat_jill_pic1_ep11_zoomed":
            return 600
        if fname == "chat_sage_group_pic1_ep11_zoomed":
            return 1080
        if fname == "chat_bianca_pic1_ep12_zoomed" or fname == "chat_bianca_pic2_ep12_zoomed":
            return 600
        if fname == "ep12_diane1":
            return 720
        if fname == "ep12_np_jill_picture" or fname == "ep12_bikini_minny" or fname == "ep12_bella_solo_pic1" or fname == "ep12_josy_solo_pic1" or fname == "ep12_maya_solo_pic2" or fname == "ep12_maya_solo_pic3" or fname == "ep12_sage_solo_pic2":
            return 720
        if fname == "ep12_bikini_dawe":
            return 1080
        
        
        
        return 1920

    def mphone_custom_wallpaper_get_start_xpos(fname):
        val = mphone_custom_wallpaper_get_width(fname) * persistent.scale_factor
        return (int) ((val * 0.9167 - 470)/2)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

init python:
    def calcWallpapers():
        global foundWallpapers
        foundWallpapers = 0
        for x in persistent.art_unlocked_lvl1:
            if x:
                foundWallpapers += 1
        return

    def calcScenes():
        global unlockedScenes
        unlockedScenes = 0
        if persistent.epi_lewd_zoey:
            unlockedScenes += 1
        if persistent.epi_lewd_eb:
            unlockedScenes += 1
        if persistent.ep9_lewd_jade:
            unlockedScenes += 1
        if persistent.ep9_lewd_jill:
            unlockedScenes += 1
        if persistent.ep9_lewd_sage1:
            unlockedScenes += 1
        if persistent.ep9_lewd_lily:
            unlockedScenes += 1
        if persistent.ep9_lewd_sage2:
            unlockedScenes += 1
        if persistent.ep9_lewd_maya:
            unlockedScenes += 1
        if persistent.ep9_lewd_camila:
            unlockedScenes += 1
        if persistent.ep9_lewd_heather:
            unlockedScenes += 1
        if persistent.ep9_lewd_cumpetition:
            unlockedScenes += 1
        if persistent.ep9_lewd_isabella:
            unlockedScenes += 1
        if persistent.ep9_lewd_jm2:
            unlockedScenes += 1
        if persistent.ep9_lewd_isabella2:
            unlockedScenes += 1
        if persistent.ep9_lewd_jill2:
            unlockedScenes += 1
        if persistent.ep9_lewd_jm:
            unlockedScenes += 1
        if persistent.ep9_lewd_sage3:
            unlockedScenes += 1
        if persistent.ep9_lewd_ln:
            unlockedScenes += 1
        if persistent.ep9_lewd_quinn:
            unlockedScenes += 1
        if persistent.ep9_lewd_others:
            unlockedScenes += 1
        if persistent.ep9_lewd_sm:
            unlockedScenes += 1
        
        if persistent.ep10_lewd_cathy:
            unlockedScenes += 1
        if persistent.ep10_lewd_madame1:
            unlockedScenes += 1
        if persistent.ep10_lewd_madame2:
            unlockedScenes += 1
        if persistent.ep10_lewd_madame3:
            unlockedScenes += 1
        if persistent.ep10_lewd_josy:
            unlockedScenes += 1
        if persistent.ep10_lewd_jm:
            unlockedScenes += 1
        if persistent.ep10_lewd_maya:
            unlockedScenes += 1
        if persistent.ep10_lewd_sage:
            unlockedScenes += 1
        if persistent.ep10_lewd_sage2:
            unlockedScenes += 1
        if persistent.ep10_lewd_jill:
            unlockedScenes += 1
        if persistent.ep10_lewd_isabella:
            unlockedScenes += 1
        if persistent.ep10_lewd_nicole:
            unlockedScenes += 1
        if persistent.ep10_lewd_riona:
            unlockedScenes += 1
        if persistent.ep10_lewd_nora:
            unlockedScenes += 1
        if persistent.ep10_lewd_lily:
            unlockedScenes += 1
        if persistent.ep10_lewd_quinn:
            unlockedScenes += 1
        
        if persistent.ep11_lewd_madame:
            unlockedScenes += 1
        if persistent.ep11_lewd_tiffani:
            unlockedScenes += 1
        if persistent.ep11_lewd_lily:
            unlockedScenes += 1
        if persistent.ep11_lewd_becky:
            unlockedScenes += 1
        if persistent.ep11_lewd_tara:
            unlockedScenes += 1
        if persistent.ep11_lewd_jm:
            unlockedScenes += 1
        if persistent.ep11_lewd_jill:
            unlockedScenes += 1
        if persistent.ep11_lewd_jill2:
            unlockedScenes += 1
        if persistent.ep11_lewd_bella:
            unlockedScenes += 1
        if persistent.ep11_lewd_bella2:
            unlockedScenes += 1
        if persistent.ep11_lewd_sage:
            unlockedScenes += 1
        if persistent.ep11_lewd_sage2:
            unlockedScenes += 1
        if persistent.ep11_lewd_camila:
            unlockedScenes += 1
        if persistent.ep11_lewd_lynette:
            unlockedScenes += 1
        if persistent.ep11_lewd_jade:
            unlockedScenes += 1
        if persistent.ep11_lewd_sarah:
            unlockedScenes += 1
        if persistent.ep11_lewd_melanie:
            unlockedScenes += 1
        if persistent.ep11_lewd_elena:
            unlockedScenes += 1
        
        if persistent.ep12_lewd_nora:
            unlockedScenes += 1
        if persistent.ep12_lewd_cathy:
            unlockedScenes += 1
        if persistent.ep12_lewd_ts:
            unlockedScenes += 1
        if persistent.ep12_lewd_nicole:
            unlockedScenes += 1
        if persistent.ep12_lewd_josy:
            unlockedScenes += 1
        if persistent.ep12_lewd_maya:
            unlockedScenes += 1
        if persistent.ep12_lewd_quinn:
            unlockedScenes += 1
        if persistent.ep12_lewd_bianca:
            unlockedScenes += 1
        if persistent.ep12_lewd_elena:
            unlockedScenes += 1
        if persistent.ep12_lewd_isabella:
            unlockedScenes += 1
        if persistent.ep12_lewd_jade:
            unlockedScenes += 1
        if persistent.ep12_lewd_jill:
            unlockedScenes += 1
        if persistent.ep12_lewd_quinn2:
            unlockedScenes += 1
        if persistent.ep12_lewd_sage:
            unlockedScenes += 1
        if persistent.ep12_lewd_sally:
            unlockedScenes += 1
        if persistent.ep12_lewd_zoey:
            unlockedScenes += 1
        
        if steamAchievements and unlockedScenes == persistent.totalScenes:
            achievement.grant("IDS3_13")
            achievement.Sync()
        return

    def calcRenders():
        global foundCards
        foundCards =  persistent.rew_mixed_unlocked + persistent.rew_josy_unlocked + persistent.rew_jill_unlocked + persistent.rew_maya_unlocked + persistent.rew_sage_unlocked + persistent.rew_isa_unlocked + persistent.rew_cam_unlocked + persistent.rew_2d_unlocked + persistent.rew_zoey_unlocked + persistent.rew_lily_unlocked
        if steamAchievements and foundCards == persistent.totalCards:
            achievement.grant("IDS3_12")
            achievement.Sync()
        return

    def dk(point):
        global tmpdik
        global totalChickChoices
        global totalDikChoices
        if point > 0:
            totalDikChoices += 1
        elif point < 0:
            totalChickChoices += 1
        tmpdik = tmpdik + point
        return

    def mny(mony):
        global money
        global earnedMoney
        global spentMoney
        global wallet_lvl
        
        money += mony
        if (money > 10 and wallet_lvl == 3):
            money = 10
        elif (money > 8 and wallet_lvl == 2):
            money = 8
        elif (money > 6 and wallet_lvl == 1):
            money = 6
        elif money > 5 and wallet_lvl == 0:
            money = 5
        elif money < 0:
            money = 0
        
        if steamAchievements and mony > 0 and not config.console and not config.developer:
            earnedMoney += mony
            if earnedMoney >= 20:
                achievement.grant("NOTSOPOORAFTERALL")
                achievement.Sync()
        elif steamAchievements and mony < 0 and not config.console and not config.developer:
            spentMoney -= mony
            if spentMoney >= 20:
                achievement.grant("POORAGAIN")
                achievement.Sync()
        return

    def updateDikScore():
        global dtype
        global dik
        global majordik
        global majorchick
        global tmpdik
        global permanent_affinity
        global affinity
        
        dik = dik + tmpdik
        tmpdik = 0
        if affinity == "DIK":
            if dik > 20:
                dik = 20
            elif dik < 5:
                dik = 5
            if dik >=15:
                dtype = 3
            elif dik >=10 :
                dtype = 2
            else:
                dtype = 1
        elif affinity == "CHICK":
            if dik > -5:
                dik = -5
            elif dik < -20:
                dik = -20
            if dik <=-15:
                dtype = -3
            elif dik <=-10:
                dtype = -2
            else:
                dtype = -1
        else:
            if dik > 9:
                dik = 9
            elif dik < -9:
                dik = -9
            if dik >=5:
                dtype = 1
            elif dik <5 and dik >-5:
                dtype = 0
            else:
                dtype = -1
        return

    def addDPenalty():
        global dpenalty
        dpenalty += 1
        return

    def addNPenalty():
        global npenalty
        npenalty += 1
        return

    def addCPenalty():
        global cpenalty
        cpenalty += 1
        return

init -1500 python:
    from store import persistent, renpy, config, Action

    mybackends = [ ]

    class MyBackend(object):
        def activate_overlay_to_store(self, appid, flags):
            """
            Called to open the steam store overlay
            """
        def is_subscribed_app(appid):
            """
            Called to check if user owns app
            """

    steam_maximum_framerate = 15
    class MySteamBackend(MyBackend):
        
        def __init__(self):
            renpy.maximum_framerate(steam_maximum_framerate)
        
        def activate_overlay_to_store(self, appid, flags):
            steam.activate_overlay_to_store(appid, flags)
        
        def is_subscribed_app(self, appid):
            return steam.is_subscribed_app(appid)

    try:
        import _renpysteam as steam
        renpy.write_log("Imported steam.")
    except Exception as e:
        steam = None
        renpy.write_log("Importing _renpysteam: %r", e)

    if steam is not None:
        
        want_version = 2
        
        if steam.version < want_version:
            raise Exception("_renpysteam module is too old. (want version %d, got %d)" % (steam.version, want_version))
        
        if steam.init():
            renpy.write_log("Initialized steam.")
            mybackends.insert(0, MySteamBackend())
        else:
            renpy.write_log("Failed to initialize steam.")
            steam = None

    def activate_overlay_to_store(appid, flags):
        for i in mybackends:
            i.activate_overlay_to_store(appid, flags)

    def is_subscribed_app(appid):
        for i in mybackends:
            return i.is_subscribed_app(appid)

init python:
    def updatePersistentRenderCount():
        persistent.rew_josy_unlocked = 0
        persistent.rew_maya_unlocked = 0
        persistent.rew_isa_unlocked = 0
        persistent.rew_cam_unlocked = 0
        persistent.rew_sage_unlocked = 0
        persistent.rew_jill_unlocked = 0
        persistent.rew_mixed_unlocked = 0
        persistent.rew_2d_unlocked = 0
        persistent.rew_zoey_unlocked = 0
        persistent.rew_lily_unlocked = 0
        
        
        for x in persistent.art_unlocked_lvl1:
            if x:
                persistent.rew_2d_unlocked += 1
        for x in persistent.art_unlocked_lvl2:
            if x:
                persistent.rew_2d_unlocked += 1
        for x in persistent.art_unlocked_lvl3:
            if x:
                persistent.rew_2d_unlocked += 1
        
        if persistent.ep7_wpi1:
            persistent.rew_2d_unlocked += 1
        if persistent.ep7_wpi2:
            persistent.rew_2d_unlocked += 1
        if persistent.ep7_wpj1:
            persistent.rew_2d_unlocked += 1
        if persistent.ep7_wpj2:
            persistent.rew_2d_unlocked += 1
        if persistent.ep7_wpjo1:
            persistent.rew_2d_unlocked += 1
        if persistent.ep7_wpjo2:
            persistent.rew_2d_unlocked += 1
        if persistent.ep7_wpm1:
            persistent.rew_2d_unlocked += 1
        if persistent.ep7_wpm2:
            persistent.rew_2d_unlocked += 1
        if persistent.ep7_wps1:
            persistent.rew_2d_unlocked += 1
        if persistent.ep7_wps2:
            persistent.rew_2d_unlocked += 1
        
        if persistent.ep8_wpi1:
            persistent.rew_2d_unlocked += 1
        if persistent.ep8_wpj1:
            persistent.rew_2d_unlocked += 1
        if persistent.ep8_wpjo1:
            persistent.rew_2d_unlocked += 1
        if persistent.ep8_wpm1:
            persistent.rew_2d_unlocked += 1
        if persistent.ep8_wpq1:
            persistent.rew_2d_unlocked += 1
        if persistent.ep8_wps1:
            persistent.rew_2d_unlocked += 1
        if persistent.ep8_wpe1:
            persistent.rew_2d_unlocked += 1
        if persistent.ep8_wpmad1:
            persistent.rew_2d_unlocked += 1
        if persistent.ep8_wpjade1:
            persistent.rew_2d_unlocked += 1
        
        if persistent.epi_card1:
            persistent.rew_2d_unlocked += 1
        if persistent.epi_card2:
            persistent.rew_2d_unlocked += 1
        if persistent.epi_card3:
            persistent.rew_2d_unlocked += 1
        if persistent.epi_card4:
            persistent.rew_2d_unlocked += 1
        
        if persistent.epi_card5:
            persistent.rew_mixed_unlocked += 1
        if persistent.epi_card6:
            persistent.rew_mixed_unlocked += 1
        if persistent.epi_card7:
            persistent.rew_mixed_unlocked += 1
        if persistent.epi_card8:
            persistent.rew_mixed_unlocked += 1
        if persistent.epi_card9:
            persistent.rew_mixed_unlocked += 1
        if persistent.epi_card10:
            persistent.rew_mixed_unlocked += 1
        if persistent.epi_card11:
            persistent.rew_mixed_unlocked += 1
        if persistent.epi_card12:
            persistent.rew_mixed_unlocked += 1
        
        
        if persistent.ep9_cardji1:
            persistent.rew_jill_unlocked += 1
        if persistent.ep9_cardji2:
            persistent.rew_jill_unlocked += 1
        if persistent.ep9_cardji3:
            persistent.rew_jill_unlocked += 1
        if persistent.ep9_cardji4:
            persistent.rew_jill_unlocked += 1
        if persistent.ep9_cardji5:
            persistent.rew_jill_unlocked += 1
        if persistent.ep9_cardji6:
            persistent.rew_jill_unlocked += 1
        if persistent.ep9_cardji7:
            persistent.rew_jill_unlocked += 1
        if persistent.ep9_cardji8:
            persistent.rew_jill_unlocked += 1
        if persistent.ep9_cardji9:
            persistent.rew_jill_unlocked += 1
        if persistent.ep9_cardji10:
            persistent.rew_jill_unlocked += 1
        if persistent.ep9_cardji11:
            persistent.rew_jill_unlocked += 1
        if persistent.ep9_cardji12:
            persistent.rew_jill_unlocked += 1
        if persistent.ep9_cardji13:
            persistent.rew_jill_unlocked += 1
        if persistent.ep9_cardji14:
            persistent.rew_jill_unlocked += 1
        if persistent.ep9_cardji15:
            persistent.rew_jill_unlocked += 1
        if persistent.ep9_cardji16:
            persistent.rew_jill_unlocked += 1
        if persistent.ep9_cardji17:
            persistent.rew_jill_unlocked += 1
        if persistent.ep9_cardji18:
            persistent.rew_jill_unlocked += 1
        if persistent.ep9_cardji19:
            persistent.rew_jill_unlocked += 1
        if persistent.ep9_cardji20:
            persistent.rew_jill_unlocked += 1
        
        if persistent.ep9_card1:
            persistent.rew_2d_unlocked += 1
        if persistent.ep9_card2:
            persistent.rew_2d_unlocked += 1
        if persistent.ep9_card3:
            persistent.rew_2d_unlocked += 1
        if persistent.ep9_card4:
            persistent.rew_2d_unlocked += 1
        if persistent.ep9_card5:
            persistent.rew_2d_unlocked += 1
        if persistent.ep9_card6:
            persistent.rew_2d_unlocked += 1
        if persistent.ep9_card7:
            persistent.rew_2d_unlocked += 1
        if persistent.ep9_card8:
            persistent.rew_2d_unlocked += 1
        if persistent.ep9_card9:
            persistent.rew_mixed_unlocked += 1
        if persistent.ep9_card10:
            persistent.rew_mixed_unlocked += 1
        if persistent.ep9_card11:
            persistent.rew_mixed_unlocked += 1
        if persistent.ep9_card12:
            persistent.rew_mixed_unlocked += 1
        if persistent.ep9_card13:
            persistent.rew_mixed_unlocked += 1
        if persistent.ep9_card14:
            persistent.rew_mixed_unlocked += 1
        if persistent.ep9_card15:
            persistent.rew_mixed_unlocked += 1
        if persistent.ep9_card16:
            persistent.rew_mixed_unlocked += 1
        if persistent.ep9_card17:
            persistent.rew_2d_unlocked += 1
        if persistent.ep9_card18:
            persistent.rew_2d_unlocked += 1
        if persistent.ep9_card19:
            persistent.rew_2d_unlocked += 1
        if persistent.ep9_card20:
            persistent.rew_2d_unlocked += 1
        
        if persistent.ep9_cardjo1:
            persistent.rew_josy_unlocked += 1
        if persistent.ep9_cardjo2:
            persistent.rew_josy_unlocked += 1
        if persistent.ep9_cardjo3:
            persistent.rew_josy_unlocked += 1
        if persistent.ep9_cardjo4:
            persistent.rew_josy_unlocked += 1
        if persistent.ep9_cardjo5:
            persistent.rew_josy_unlocked += 1
        if persistent.ep9_cardjo6:
            persistent.rew_josy_unlocked += 1
        if persistent.ep9_cardjo7:
            persistent.rew_josy_unlocked += 1
        if persistent.ep9_cardjo8:
            persistent.rew_josy_unlocked += 1
        if persistent.ep9_cardjo9:
            persistent.rew_josy_unlocked += 1
        if persistent.ep9_cardjo10:
            persistent.rew_josy_unlocked += 1
        if persistent.ep9_cardjo11:
            persistent.rew_josy_unlocked += 1
        if persistent.ep9_cardjo12:
            persistent.rew_josy_unlocked += 1
        if persistent.ep9_cardjo13:
            persistent.rew_josy_unlocked += 1
        if persistent.ep9_cardjo14:
            persistent.rew_josy_unlocked += 1
        if persistent.ep9_cardjo15:
            persistent.rew_josy_unlocked += 1
        if persistent.ep9_cardjo16:
            persistent.rew_josy_unlocked += 1
        if persistent.ep9_cardjo17:
            persistent.rew_josy_unlocked += 1
        if persistent.ep9_cardjo18:
            persistent.rew_josy_unlocked += 1
        if persistent.ep9_cardjo19:
            persistent.rew_josy_unlocked += 1
        if persistent.ep9_cardjo20:
            persistent.rew_josy_unlocked += 1
        
        if persistent.ep10_card1:
            persistent.rew_mixed_unlocked += 1
        if persistent.ep10_card2:
            persistent.rew_mixed_unlocked += 1
        if persistent.ep10_card3:
            persistent.rew_mixed_unlocked += 1
        if persistent.ep10_card4:
            persistent.rew_mixed_unlocked += 1
        if persistent.ep10_card5:
            persistent.rew_mixed_unlocked += 1
        if persistent.ep10_card6:
            persistent.rew_mixed_unlocked += 1
        if persistent.ep10_card7:
            persistent.rew_mixed_unlocked += 1
        if persistent.ep10_card8:
            persistent.rew_mixed_unlocked += 1
        if persistent.ep10_card13:
            persistent.rew_2d_unlocked += 1
        if persistent.ep10_card14:
            persistent.rew_2d_unlocked += 1
        if persistent.ep10_card15:
            persistent.rew_2d_unlocked += 1
        if persistent.ep10_card16:
            persistent.rew_2d_unlocked += 1
        if persistent.ep10_card11:
            persistent.rew_2d_unlocked += 1
        if persistent.ep10_card12:
            persistent.rew_2d_unlocked += 1
        if persistent.ep10_card9:
            persistent.rew_2d_unlocked += 1
        if persistent.ep10_card10:
            persistent.rew_2d_unlocked += 1
        
        if persistent.ep10_cardsa1:
            persistent.rew_sage_unlocked += 1
        if persistent.ep10_cardsa2:
            persistent.rew_sage_unlocked += 1
        if persistent.ep10_cardsa3:
            persistent.rew_sage_unlocked += 1
        if persistent.ep10_cardsa4:
            persistent.rew_sage_unlocked += 1
        if persistent.ep10_cardsa5:
            persistent.rew_sage_unlocked += 1
        if persistent.ep10_cardsa6:
            persistent.rew_sage_unlocked += 1
        if persistent.ep10_cardsa7:
            persistent.rew_sage_unlocked += 1
        if persistent.ep10_cardsa8:
            persistent.rew_sage_unlocked += 1
        if persistent.ep10_cardsa9:
            persistent.rew_sage_unlocked += 1
        if persistent.ep10_cardsa10:
            persistent.rew_sage_unlocked += 1
        if persistent.ep10_cardsa11:
            persistent.rew_sage_unlocked += 1
        if persistent.ep10_cardsa12:
            persistent.rew_sage_unlocked += 1
        if persistent.ep10_cardsa13:
            persistent.rew_sage_unlocked += 1
        if persistent.ep10_cardsa14:
            persistent.rew_sage_unlocked += 1
        if persistent.ep10_cardsa15:
            persistent.rew_sage_unlocked += 1
        if persistent.ep10_cardsa16:
            persistent.rew_sage_unlocked += 1
        if persistent.ep10_cardsa17:
            persistent.rew_sage_unlocked += 1
        if persistent.ep10_cardsa18:
            persistent.rew_sage_unlocked += 1
        if persistent.ep10_cardsa19:
            persistent.rew_sage_unlocked += 1
        if persistent.ep10_cardsa20:
            persistent.rew_sage_unlocked += 1
        
        if persistent.ep10_cardzo1:
            persistent.rew_zoey_unlocked += 1
        if persistent.ep10_cardzo2:
            persistent.rew_zoey_unlocked += 1
        if persistent.ep10_cardzo3:
            persistent.rew_zoey_unlocked += 1
        if persistent.ep10_cardzo4:
            persistent.rew_zoey_unlocked += 1
        if persistent.ep10_cardzo5:
            persistent.rew_zoey_unlocked += 1
        if persistent.ep10_cardzo6:
            persistent.rew_zoey_unlocked += 1
        if persistent.ep10_cardzo7:
            persistent.rew_zoey_unlocked += 1
        if persistent.ep10_cardzo8:
            persistent.rew_zoey_unlocked += 1
        if persistent.ep10_cardzo9:
            persistent.rew_zoey_unlocked += 1
        if persistent.ep10_cardzo10:
            persistent.rew_zoey_unlocked += 1
        if persistent.ep10_cardzo11:
            persistent.rew_zoey_unlocked += 1
        if persistent.ep10_cardzo12:
            persistent.rew_zoey_unlocked += 1
        if persistent.ep10_cardzo13:
            persistent.rew_zoey_unlocked += 1
        if persistent.ep10_cardzo14:
            persistent.rew_zoey_unlocked += 1
        if persistent.ep10_cardzo15:
            persistent.rew_zoey_unlocked += 1
        if persistent.ep10_cardzo16:
            persistent.rew_zoey_unlocked += 1
        if persistent.ep10_cardzo17:
            persistent.rew_zoey_unlocked += 1
        if persistent.ep10_cardzo18:
            persistent.rew_zoey_unlocked += 1
        if persistent.ep10_cardzo19:
            persistent.rew_zoey_unlocked += 1
        if persistent.ep10_cardzo20:
            persistent.rew_zoey_unlocked += 1
        
        
        if persistent.ep11_cardmy1:
            persistent.rew_maya_unlocked += 1
        if persistent.ep11_cardmy2:
            persistent.rew_maya_unlocked += 1
        if persistent.ep11_cardmy3:
            persistent.rew_maya_unlocked += 1
        if persistent.ep11_cardmy4:
            persistent.rew_maya_unlocked += 1
        if persistent.ep11_cardmy5:
            persistent.rew_maya_unlocked += 1
        if persistent.ep11_cardmy6:
            persistent.rew_maya_unlocked += 1
        if persistent.ep11_cardmy7:
            persistent.rew_maya_unlocked += 1
        if persistent.ep11_cardmy8:
            persistent.rew_maya_unlocked += 1
        if persistent.ep11_cardmy9:
            persistent.rew_maya_unlocked += 1
        if persistent.ep11_cardmy10:
            persistent.rew_maya_unlocked += 1
        if persistent.ep11_cardmy11:
            persistent.rew_maya_unlocked += 1
        if persistent.ep11_cardmy12:
            persistent.rew_maya_unlocked += 1
        if persistent.ep11_cardmy13:
            persistent.rew_maya_unlocked += 1
        if persistent.ep11_cardmy14:
            persistent.rew_maya_unlocked += 1
        if persistent.ep11_cardmy15:
            persistent.rew_maya_unlocked += 1
        if persistent.ep11_cardmy16:
            persistent.rew_maya_unlocked += 1
        if persistent.ep11_cardmy17:
            persistent.rew_maya_unlocked += 1
        if persistent.ep11_cardmy18:
            persistent.rew_maya_unlocked += 1
        if persistent.ep11_cardmy19:
            persistent.rew_maya_unlocked += 1
        if persistent.ep11_cardmy20:
            persistent.rew_maya_unlocked += 1
        
        if persistent.ep11_cardly1:
            persistent.rew_lily_unlocked += 1
        if persistent.ep11_cardly2:
            persistent.rew_lily_unlocked += 1
        if persistent.ep11_cardly3:
            persistent.rew_lily_unlocked += 1
        if persistent.ep11_cardly4:
            persistent.rew_lily_unlocked += 1
        if persistent.ep11_cardly5:
            persistent.rew_lily_unlocked += 1
        if persistent.ep11_cardly6:
            persistent.rew_lily_unlocked += 1
        if persistent.ep11_cardly7:
            persistent.rew_lily_unlocked += 1
        if persistent.ep11_cardly8:
            persistent.rew_lily_unlocked += 1
        if persistent.ep11_cardly9:
            persistent.rew_lily_unlocked += 1
        if persistent.ep11_cardly10:
            persistent.rew_lily_unlocked += 1
        if persistent.ep11_cardly11:
            persistent.rew_lily_unlocked += 1
        if persistent.ep11_cardly12:
            persistent.rew_lily_unlocked += 1
        if persistent.ep11_cardly13:
            persistent.rew_lily_unlocked += 1
        if persistent.ep11_cardly14:
            persistent.rew_lily_unlocked += 1
        if persistent.ep11_cardly15:
            persistent.rew_lily_unlocked += 1
        if persistent.ep11_cardly16:
            persistent.rew_lily_unlocked += 1
        if persistent.ep11_cardly17:
            persistent.rew_lily_unlocked += 1
        if persistent.ep11_cardly18:
            persistent.rew_lily_unlocked += 1
        if persistent.ep11_cardly19:
            persistent.rew_lily_unlocked += 1
        if persistent.ep11_cardly20:
            persistent.rew_lily_unlocked += 1
        
        if persistent.ep11_card1:
            persistent.rew_mixed_unlocked += 1
        if persistent.ep11_card2:
            persistent.rew_mixed_unlocked += 1
        if persistent.ep11_card3:
            persistent.rew_mixed_unlocked += 1
        if persistent.ep11_card4:
            persistent.rew_mixed_unlocked += 1
        if persistent.ep11_card5:
            persistent.rew_mixed_unlocked += 1
        if persistent.ep11_card6:
            persistent.rew_mixed_unlocked += 1
        if persistent.ep11_card7:
            persistent.rew_mixed_unlocked += 1
        if persistent.ep11_card8:
            persistent.rew_mixed_unlocked += 1
        if persistent.ep11_card9b:
            persistent.rew_mixed_unlocked += 1
        if persistent.ep11_card10b:
            persistent.rew_mixed_unlocked += 1
        if persistent.ep11_card11b:
            persistent.rew_mixed_unlocked += 1
        if persistent.ep11_card12b:
            persistent.rew_mixed_unlocked += 1
        if persistent.ep11_card9:
            persistent.rew_2d_unlocked += 1
        if persistent.ep11_card10:
            persistent.rew_2d_unlocked += 1
        if persistent.ep11_card11:
            persistent.rew_2d_unlocked += 1
        if persistent.ep11_card12:
            persistent.rew_2d_unlocked += 1
        
        if persistent.ep12_cardisa1:
            persistent.rew_isa_unlocked += 1
        if persistent.ep12_cardisa2:
            persistent.rew_isa_unlocked += 1
        if persistent.ep12_cardisa3:
            persistent.rew_isa_unlocked += 1
        if persistent.ep12_cardisa4:
            persistent.rew_isa_unlocked += 1
        if persistent.ep12_cardisa5:
            persistent.rew_isa_unlocked += 1
        if persistent.ep12_cardisa6:
            persistent.rew_isa_unlocked += 1
        if persistent.ep12_cardisa7:
            persistent.rew_isa_unlocked += 1
        if persistent.ep12_cardisa8:
            persistent.rew_isa_unlocked += 1
        if persistent.ep12_cardisa9:
            persistent.rew_isa_unlocked += 1
        if persistent.ep12_cardisa10:
            persistent.rew_isa_unlocked += 1
        if persistent.ep12_cardisa11:
            persistent.rew_isa_unlocked += 1
        if persistent.ep12_cardisa12:
            persistent.rew_isa_unlocked += 1
        if persistent.ep12_cardisa13:
            persistent.rew_isa_unlocked += 1
        if persistent.ep12_cardisa14:
            persistent.rew_isa_unlocked += 1
        if persistent.ep12_cardisa15:
            persistent.rew_isa_unlocked += 1
        if persistent.ep12_cardisa16:
            persistent.rew_isa_unlocked += 1
        if persistent.ep12_cardisa17:
            persistent.rew_isa_unlocked += 1
        if persistent.ep12_cardisa18:
            persistent.rew_isa_unlocked += 1
        if persistent.ep12_cardisa19:
            persistent.rew_isa_unlocked += 1
        if persistent.ep12_cardisa20:
            persistent.rew_isa_unlocked += 1
        
        if persistent.ep12_cardcam1:
            persistent.rew_cam_unlocked += 1
        if persistent.ep12_cardcam2:
            persistent.rew_cam_unlocked += 1
        if persistent.ep12_cardcam3:
            persistent.rew_cam_unlocked += 1
        if persistent.ep12_cardcam4:
            persistent.rew_cam_unlocked += 1
        if persistent.ep12_cardcam5:
            persistent.rew_cam_unlocked += 1
        if persistent.ep12_cardcam6:
            persistent.rew_cam_unlocked += 1
        if persistent.ep12_cardcam7:
            persistent.rew_cam_unlocked += 1
        if persistent.ep12_cardcam8:
            persistent.rew_cam_unlocked += 1
        if persistent.ep12_cardcam9:
            persistent.rew_cam_unlocked += 1
        if persistent.ep12_cardcam10:
            persistent.rew_cam_unlocked += 1
        if persistent.ep12_cardcam11:
            persistent.rew_cam_unlocked += 1
        if persistent.ep12_cardcam12:
            persistent.rew_cam_unlocked += 1
        if persistent.ep12_cardcam13:
            persistent.rew_cam_unlocked += 1
        if persistent.ep12_cardcam14:
            persistent.rew_cam_unlocked += 1
        if persistent.ep12_cardcam15:
            persistent.rew_cam_unlocked += 1
        if persistent.ep12_cardcam16:
            persistent.rew_cam_unlocked += 1
        if persistent.ep12_cardcam17:
            persistent.rew_cam_unlocked += 1
        if persistent.ep12_cardcam18:
            persistent.rew_cam_unlocked += 1
        if persistent.ep12_cardcam19:
            persistent.rew_cam_unlocked += 1
        if persistent.ep12_cardcam20:
            persistent.rew_cam_unlocked += 1
        
        if persistent.ep12_card1:
            persistent.rew_mixed_unlocked += 1
        if persistent.ep12_card2:
            persistent.rew_mixed_unlocked += 1
        if persistent.ep12_card3:
            persistent.rew_mixed_unlocked += 1
        if persistent.ep12_card4:
            persistent.rew_mixed_unlocked += 1
        if persistent.ep12_card5:
            persistent.rew_mixed_unlocked += 1
        if persistent.ep12_card6:
            persistent.rew_mixed_unlocked += 1
        if persistent.ep12_card7:
            persistent.rew_mixed_unlocked += 1
        if persistent.ep12_card8:
            persistent.rew_mixed_unlocked += 1
        if persistent.ep12_card9:
            persistent.rew_mixed_unlocked += 1
        if persistent.ep12_card10:
            persistent.rew_mixed_unlocked += 1
        if persistent.ep12_card11:
            persistent.rew_mixed_unlocked += 1
        if persistent.ep12_card12:
            persistent.rew_mixed_unlocked += 1
        if persistent.ep12_card13:
            persistent.rew_mixed_unlocked += 1
        if persistent.ep12_card14:
            persistent.rew_mixed_unlocked += 1
        if persistent.ep12_card15:
            persistent.rew_2d_unlocked += 1
        if persistent.ep12_card16:
            persistent.rew_2d_unlocked += 1
        if persistent.ep12_card17:
            persistent.rew_2d_unlocked += 1
        if persistent.ep12_card18:
            persistent.rew_2d_unlocked += 1
        if persistent.ep12_card19:
            persistent.rew_2d_unlocked += 1
        
        return
init 2:
    $ updatePersistentRenderCount()


init python:
    def updateTaskList():
        global current_task
        global current_optional_task
        global task_list
        global chat_new_tasks
        global branchIsabella
        global ep11_mg_party
        
        current_task = ""
        for x in task_list:
            if x != "":
                current_task += x
                current_task += "\n"
        if current_task == "" and freeRoamID == "ep9_1":
            if branchIsabella and wt_ep9_branch_numbers < 2:
                current_task = "Wait for Bella by your window"
            else:
                current_task = "Go to Derek's closet"
            chat_new_tasks = True
        elif current_task == "" and freeRoamID == "ep9_2":
            current_task = "Talk to Sage"
            chat_new_tasks = True
        elif current_task == "" and freeRoamID == "ep9_4":
            if branchMayaJosy or (pathMayaJosy and (branchSage or branchJill or branchIsabella)):
                if persistent.mod_wtenabled:
                    current_task = "Talk to Maya & Josy (Upper Main room)"
                else:
                    current_task = "Talk to Maya & Josy"
            elif branchSage:
                if persistent.mod_wtenabled:
                    current_task = "Talk to Maya & Josy (Upper Main room)"
                else:
                    current_task = "Talk to Maya & Josy"
            elif branchJill:
                if persistent.mod_wtenabled:
                    current_task = "Talk to Maya & Josy (Upper Main room)"
                else:
                    current_task = "Talk to Maya & Josy"
            elif branchIsabella and wt_ep9_branch_numbers < 2:
                current_task = "Talk to Bella"
            else:
                current_task = "End the night with someone\nOr\nTalk to Maya & Josy"
                
            if wt_ep9_branch_numbers > 1:
                if persistent.mod_wtenabled:
                    current_task = "Talk to Maya & Josy (Upper Main room)"
                else:
                    current_task = "Talk to Maya & Josy"
                    
                if branchIsabella:
                    if persistent.mod_wtenabled:
                        current_task = current_task+ "\nOr\nTalk to Bella (Main Party room)"
                    else:
                        current_task = current_task+ "\nOr\nTalk to Bella"
                if branchAlone:
                    if persistent.mod_wtenabled:
                        current_task = "End the night with someone\nOr\n"+current_task
                    else:
                        current_task = "End the night with someone\nOr\n"+current_task
            chat_new_tasks = True
        elif current_task == "" and freeRoamID == "ep10_1":
            current_task = "Talk to Sage"
            chat_new_tasks = True
        elif current_task == "" and freeRoamID == "ep10_2":
            current_task = "Exit your room"
            chat_new_tasks = True
        elif current_task == "" and freeRoamID == "ep10_3":
            current_task = "Go to your tent"
            chat_new_tasks = True
        elif current_task == "" and freeRoamID == "ep10_4":
            current_task = "Exit your room"
            chat_new_tasks = True
        elif current_task == "" and freeRoamID == "ep10_5":
            current_task = "Snoop around for the binder"
            chat_new_tasks = True
        elif current_task == "" and freeRoamID == "ep11_1":
            current_task = "Exit your room"
            chat_new_tasks = True
        elif current_task == "" and freeRoamID == "ep11_2":
            current_task = "Plan the party on your couch"
            chat_new_tasks = True
        elif current_task == "" and freeRoamID == "ep11_3":
            current_task = "Go to bed"
            chat_new_tasks = True
        elif current_task == "" and freeRoamID == "ep11_4":
            current_task = "Talk to Derek"
            chat_new_tasks = True
        elif current_task == "" and freeRoamID == "ep11_4b":
            if ep11_mg_party:
                current_task = "Talk to Zoey"
            else:
                current_task = "Go to Tommy's room"
            chat_new_tasks = True
        elif current_task == "" and freeRoamID == "ep11_4c":
            current_task = "Talk to Zoey"
            chat_new_tasks = True
        elif current_task == "" and freeRoamID == "ep11_5":
            current_task = "Exit your room"
            chat_new_tasks = True
        elif current_task == "" and freeRoamID == "ep12_1":
            current_task = "Exit your room"
            chat_new_tasks = True
        elif current_task == "" and freeRoamID == "ep12_2":
            current_task = "Exit your room"
            chat_new_tasks = True
        elif current_task == "" and freeRoamID == "ep12_3":
            if persistent.mod_wtenabled:
                current_task = "Greet Riona (3F corridor)"
            else:
                current_task = "Greet Riona"
            chat_new_tasks = True
        elif current_task == "" and freeRoamID == "ep12_3b":
            if persistent.mod_wtenabled:
                current_task = "Talk to Nick (Dance floor)"
            else:
                current_task = "Talk to Nick"
            chat_new_tasks = True
        elif current_task == "" and freeRoamID == "ep12_3c":
            current_task = "Go to the balcony"
            chat_new_tasks = True
            
            renpy.show_screen("freeroam_help")
        elif current_task == "" and freeRoamID == "ep12_4":
            current_task = "Lie down on the bed"
            chat_new_tasks = True
        return


    def calcArt():
        global foundArt
        foundArt = 0
        for x in persistent.art_unlocked_lvl1:
            if x:
                foundArt += 1
        for x in persistent.art_unlocked_lvl2:
            if x:
                foundArt += 1
        for x in persistent.art_unlocked_lvl3:
            if x:
                foundArt += 1
        if persistent.ep7_wpi1:
            foundArt += 1
        if persistent.ep7_wpi2:
            foundArt += 1
        if persistent.ep7_wpj1:
            foundArt += 1
        if persistent.ep7_wpj2:
            foundArt += 1
        if persistent.ep7_wpjo1:
            foundArt += 1
        if persistent.ep7_wpjo2:
            foundArt += 1
        if persistent.ep7_wpm1:
            foundArt += 1
        if persistent.ep7_wpm2:
            foundArt += 1
        if persistent.ep7_wps1:
            foundArt += 1
        if persistent.ep7_wps2:
            foundArt += 1
        if persistent.ep8_wpi1:
            foundArt += 1
        if persistent.ep8_wpj1:
            foundArt += 1
        if persistent.ep8_wpjo1:
            foundArt += 1
        if persistent.ep8_wpq1:
            foundArt += 1
        if persistent.ep8_wps1:
            foundArt += 1
        if persistent.ep8_wpjade1:
            foundArt += 1
        if persistent.ep8_wpmad1:
            foundArt += 1
        if persistent.ep8_wpe1:
            foundArt += 1
        if persistent.ep8_wpm1:
            foundArt += 1
        if persistent.epi_card1:
            foundArt += 1
        if persistent.epi_card2:
            foundArt += 1
        if persistent.epi_card3:
            foundArt += 1
        if persistent.epi_card4:
            foundArt += 1
        if persistent.ep9_card1:
            foundArt += 1
        if persistent.ep9_card2:
            foundArt += 1
        if persistent.ep9_card3:
            foundArt += 1
        if persistent.ep9_card4:
            foundArt += 1
        if persistent.ep9_card5:
            foundArt += 1
        if persistent.ep9_card6:
            foundArt += 1
        if persistent.ep9_card7:
            foundArt += 1
        if persistent.ep9_card8:
            foundArt += 1
        if persistent.ep9_card17:
            foundArt += 1
        if persistent.ep9_card18:
            foundArt += 1
        if persistent.ep9_card19:
            foundArt += 1
        if persistent.ep9_card20:
            foundArt += 1
        if persistent.ep10_card13:
            foundArt += 1
        if persistent.ep10_card14:
            foundArt += 1
        if persistent.ep10_card15:
            foundArt += 1
        if persistent.ep10_card16:
            foundArt += 1
        if persistent.ep10_card11:
            foundArt += 1
        if persistent.ep10_card12:
            foundArt += 1
        if persistent.ep10_card9:
            foundArt += 1
        if persistent.ep10_card10:
            foundArt += 1
        if persistent.ep11_card9:
            foundArt += 1
        if persistent.ep11_card10:
            foundArt += 1
        if persistent.ep11_card11:
            foundArt += 1
        if persistent.ep11_card12:
            foundArt += 1
        if persistent.ep12_card15:
            foundArt += 1
        if persistent.ep12_card16:
            foundArt += 1
        if persistent.ep12_card17:
            foundArt += 1
        if persistent.ep12_card18:
            foundArt += 1
        if persistent.ep12_card19:
            foundArt += 1
        return

label end_freeroam:
$ renpy.block_rollback()
hide screen wt_tasks_shown
hide screen mphone_tasks_app_screen_wtmod
hide screen freeroam_help
hide screen freeroam_wt_help
$ chat_new_tasks = False
$ current_task = ""
$ freeRoamID = ""
$ loopMusic = False
$ pack_quest_available = False
$ disabled_apps = ["music","brawler","tripletile","shuffle"]
$ task_list = [""]
$ optional_task_list = [""]
$ map_system_list = []
$ mphone_contacts_clear()
$ updateTaskList()
$ mphone_rooster_clear()
$ mphone_pack_quest_clear()
$ map_fast_travel_enabled = True
hide screen map_screen
hide screen map_minimap_screen
$ renpy.pause(2)
$ randInt = renpy.random.randint(0, 17)
$ renpy.jump(phone_clear_jump_label)

label startEvent:
$ renpy.block_rollback()
$ map_fast_travel_enabled = False
$ tmpAppList = disabled_apps
$ disabled_apps = ["music","brawler","tripletile","contacts","rooster","shuffle"]
if currentEvent in event_list:
    $ event_list.remove(currentEvent)
$ renpy.jump(currentEvent)

label endEvent:
$ renpy.block_rollback()
$ map_fast_travel_enabled = True
$ disabled_apps = tmpAppList
show screen new_phone_screen
if len(map_system_list)>0:
    show screen map_screen
$ renpy.jump(currentFreeRoamLabel)

init python:
    def desk_check_unlocked_2d(i,x):
        global breakup
        global freeRoamID
        global currentEpisode
        if i < 11:
            if persistent.art_unlocked_lvl1[i-1]:
                if currentEpisode > 11 and freeRoamID == "ep12_4" and ((i== 4 and "Isabella" in breakup) or (i== 6 and "Jill" in breakup) or (i== 13 and "Sage" in breakup) or (i== 7 and "Josy" in breakup) or (i== 9 and "Maya" in breakup)):
                    if x:
                        if i+1 > len(persistent.art_unlocked_lvl1):
                            return 0
                        else:
                            return desk_check_unlocked_2d(i+1, x)
                    else:
                        if i-1 < 0:
                            return 0
                        else:
                            return desk_check_unlocked_2d(i-1, x)
                else:
                    return i
            else:
                if x:
                    if i+1 > len(persistent.art_unlocked_lvl1):
                        return 0
                    else:
                        return desk_check_unlocked_2d(i+1, x)
                else:
                    if i-1 < 0:
                        return 0
                    else:
                        return desk_check_unlocked_2d(i-1, x)
        else:
            if currentEpisode > 9 and i == 16 and persistent.art_unlocked_lvl1[10]:
                return i
            elif i == 16:
                if x:
                    return 0
                else:
                    return desk_check_unlocked_2d(i-1, x)
            elif persistent.art_unlocked_lvl1[i]:
                return i
            else:
                if x:
                    if i+1 > len(persistent.art_unlocked_lvl1):
                        return 0
                    else:
                        return desk_check_unlocked_2d(i+1, x)
                else:
                    if i-1 < 0:
                        return 0
                    else:
                        return desk_check_unlocked_2d(i-1, x)
        return i

    def desk_check_second_unlocked_2d(i,x):
        global breakup
        global freeRoamID
        if i == 1 and persistent.ep7_wpi1 and not ("Isabella" in breakup and freeRoamID == "ep12_4"):
            return i
        elif i == 2 and persistent.ep7_wpi2 and not ("Isabella" in breakup and freeRoamID == "ep12_4"):
            return i
        elif i == 3 and persistent.ep7_wpj1 and not ("Jill" in breakup and freeRoamID == "ep12_4"):
            return i
        elif i == 4 and persistent.ep7_wpj2 and not ("Jill" in breakup and freeRoamID == "ep12_4"):
            return i
        elif i == 5 and persistent.ep7_wpjo1 and not ("Josy" in breakup and freeRoamID == "ep12_4"):
            return i
        elif i == 6 and persistent.ep7_wpjo2 and not ("Josy" in breakup and freeRoamID == "ep12_4"):
            return i
        elif i == 7 and persistent.ep7_wpm1 and not ("Maya" in breakup and freeRoamID == "ep12_4"):
            return i
        elif i == 8 and persistent.ep7_wpm2 and not ("Maya" in breakup and freeRoamID == "ep12_4"):
            return i
        elif i == 9 and persistent.ep7_wps1 and not ("Sage" in breakup and freeRoamID == "ep12_4"):
            return i
        elif i == 10 and persistent.ep7_wps2 and not ("Sage" in breakup and freeRoamID == "ep12_4"):
            return i
        elif i == 11 and persistent.ep8_wpi1 and not ("Isabella" in breakup and freeRoamID == "ep12_4"):
            return i
        elif i == 12 and persistent.ep8_wpj1 and not ("Jill" in breakup and freeRoamID == "ep12_4"):
            return i
        elif i == 13 and persistent.ep8_wpjo1 and not ("Josy" in breakup and freeRoamID == "ep12_4"):
            return i
        elif i == 14 and persistent.ep8_wpm1 and not ("Maya" in breakup and freeRoamID == "ep12_4"):
            return i
        elif i == 15 and persistent.ep8_wpq1:
            return i
        elif i == 16 and persistent.ep8_wps1 and not ("Sage" in breakup and freeRoamID == "ep12_4"):
            return i
        elif i == 17 and persistent.ep8_wpe1:
            return i
        elif i == 18 and persistent.ep8_wpjade1:
            return i
        elif i == 19 and persistent.epi_card1:
            return i
        else:
            if x:
                if i+1 > 20:
                    return 0
                else:
                    return desk_check_second_unlocked_2d(i+1, x)
            else:
                if i-1 < 0:
                    return 0
                else:
                    return desk_check_second_unlocked_2d(i-1, x)
        return i

    def in_bios(item):
        global mphone_bios_chars_list
        return in_bios_reg(mphone_bios_chars_list, item)

    def in_bios_reg(my_list, item):
        if item in my_list:
            return True
        else:
            return any(in_bios_reg(sublist, item) for sublist in my_list if isinstance(sublist, list))

    def fadeSFX2():
        renpy.music.stop(channel="sfx2", fadeout=3)
        return

    def get_class_performance():
        global failedEnglish
        global failedMath
        global failedGender
        global failedEnglishS3
        global failedMathS3
        global failedScienceS3
        global passedEnglish
        global passedMath
        global passedGender
        global passedEnglishS3
        global passedMathS3
        global passedScienceS3
        global maxedEnglish
        global maxedMath
        global maxedGender
        global maxedMath_s2
        global maxedEnglish_s2
        global maxedGender_s2
        global maxedEnglishS3
        global maxedMathS3
        global maxedScienceS3
        if failedEnglish + failedMath + failedGender + failedEnglishS3 + failedMathS3 + failedScienceS3 == 0:
            if passedEnglish + passedMath + passedGender + passedEnglishS3 + passedMathS3 + passedScienceS3 == maxedEnglish + maxedMath + maxedGender + maxedMath_s2 + maxedEnglish_s2 + maxedGender_s2 + maxedEnglishS3 + maxedMathS3 + maxedScienceS3:
                return 0
            else:
                return 1
        elif failedEnglish + failedMath + failedGender + failedEnglishS3 + failedMathS3 + failedScienceS3 < 12:
            return 2
        return 3

    def calculateGirlsDrinking():
        global ep12_drinking_list
        global ep12_girl_count
        global branchSage
        global ep2QuinnSawYouAndSage
        global p2SageGuitarTeacher
        global rejectedSage
        global ep3_choseSage
        global ep4_fuckedSage
        global ep5_fuckedSage
        global ep7_sage_lewd
        global ep8_sage_stay_night
        global ep8_told_sage_chad_troy
        global ep8_sq_lewd
        global ep2_fuckedJosy
        global ep5_fucked_josy
        global pathMayaJosy
        global branchMayaJosy
        global ep7_josy_lewd
        global ep7_josy_lewd2
        global ep8_josy_lewd
        global ep2_fingeredMaya
        global ep3_mayaLewd
        global ep5_fucked_maya
        global pathMayaJosy
        global branchMayaJosy
        global ep7_solo_mayaandpathMayaJosy
        global ep8_maya_lewd
        global branchIsabella
        global ep4_bella_lewd
        global ep5_bella_lewd
        global ep6_bella_lewd
        global ep7_bella_lewd
        global branchJill
        global ep4_touchedJillsBreasts
        global ep5_kissed_jill
        global ep11_sally_kiss
        global ep9_tara_kiss
        global ep11_tara_lewd
        global ep8_sarah_lewd
        global ep7_becky_lewd
        global ep11_becky_lewd
        global ep11_tiffani_lewd
        global ep9_tiffani_lick
        global ep1_lewd_camila_quinn
        global ep2_wonCumpetition
        global ep3_fuckedRionaQuinn
        global mbios_history_quinn
        global ep4_quinn_lewd
        global ep6_quinn_lewd
        global ep7_quinn_lewd
        global ep8_sq_lewd
        global ep11_elena_lewd
        global ep9_heather_lewd
        global ep11_dildo_sucking_girl
        global ep2_fuckHOT
        global ep4_fuckedMelanie
        global ep5_hot_lewd
        global ep6_sarah_lewd
        global ep8_sarah_lewd
        global ep9_sarah_melanie_lewd
        global ep11_sarah_lewd
        global ep2_fuckHOT
        global quinn_shop_japanese_lvl
        global ep3_fuckedRionaQuinn
        global ep5_fuckedRiona
        global ep7_riona_lewd
        global ep7_rica_lewd
        global ep10_riona_lewd
        global ep9_riona_choice
        global ep2_fuckHOT
        global ep4_fuckedMelanie
        global ep5_hot_lewd
        global ep8_melanie_lewd
        global ep9_sarah_melanie_lewd
        global ep11_mel_lewd
        global ep1_lewd_camila_quinn
        global quinn_shop_spicy_lvl
        global ep3_fuckedCamilaAndMona
        global ep5_fuckedCamila
        global ep7_camila_lewd
        global ep7_rica_lewd
        global ep7_rica_lewd
        global ep9_camila_lewd
        global ep11_sage_camila_lewd
        global ep11_camila_lewd
        global ep4_grindedLily
        global ep5_lily_lewd
        global ep7_lily_lewd
        global ep8_lily_lewd
        global ep9_lily_nicole_lewd
        global ep9_others_texted
        global ep9_cumpetition_join
        global ep10_rolling
        global ep12_bianca_lewd
        global ep11_bianca_dick
        global ep3_envyLewd
        global ep6_envy_lewd
        global ep8_envy_lewd
        global ep9_lily_nicole_lewd
        global ep9_cumpetition_join
        global ep4_lickedAshley
        global ep12_ts_lewd
        global ep6_envy_lewd
        global ep8_sandy_lewd
        global ep12_ts_lewd
        global ep8_sarah_lewd
        global ep3_acceptedJade
        global ep4_roseLewd
        global ep11_helped_erin_mia
        global ep11_mistletoe
        
        ep12_drinking_list = []
        ep12_girl_count = 0
        
        if branchSage or ep2QuinnSawYouAndSage or (ep2SageGuitarTeacher and not rejectedSage) or ep3_choseSage or ep4_fuckedSage or ep5_fuckedSage or ep7_sage_lewd or (ep8_sage_stay_night and not ep8_told_sage_chad_troy) or ep8_sq_lewd:
            ep12_drinking_list.append("Sage")
        ep12_drinking_list.append("Josy")
        ep12_drinking_list.append("Maya")
        if branchIsabella or ep4_bella_lewd or ep5_bella_lewd or ep6_bella_lewd or ep7_bella_lewd:
            ep12_drinking_list.append("Isabella")
        if branchJill or ep4_touchedJillsBreasts or ep5_kissed_jill:
            ep12_drinking_list.append("Jill")
        if ep11_sally_kiss:
            ep12_girl_count += 1
            ep12_drinking_list.append("Sally")
        if ep9_tara_kiss or ep11_tara_lewd or ep8_sarah_lewd:
            ep12_girl_count += 1
            ep12_drinking_list.append("Tara")
        if ep7_becky_lewd or ep11_becky_lewd == 4:
            ep12_girl_count += 1
            ep12_drinking_list.append("Becky")
        
        ep12_girl_count += 1
        ep12_drinking_list.append("Zoey")
        
        if ep11_tiffani_lewd or ep9_tiffani_lick:
            ep12_girl_count += 1
            ep12_drinking_list.append("Tiffani")
        if ep1_lewd_camila_quinn or ep2_wonCumpetition or ep3_fuckedRionaQuinn or "Quinn didn't like that I entered her room without being invited. But she didn't seem to mind it after it turned physical." in mbios_history_quinn or ep4_quinn_lewd or ep6_quinn_lewd or ep7_quinn_lewd or ep8_sq_lewd:
            ep12_girl_count += 1
            ep12_drinking_list.append("Quinn")
        if ep11_elena_lewd:
            ep12_girl_count += 1
            ep12_drinking_list.append("Elena")
        if ep9_heather_lewd == 2 or ep11_dildo_sucking_girl == "Heather":
            ep12_girl_count += 1
            ep12_drinking_list.append("Heather")
        if ep2_fuckHOT or ep4_fuckedMelanie or ep5_hot_lewd or ep6_sarah_lewd or ep8_sarah_lewd or ep9_sarah_melanie_lewd or ep11_sarah_lewd:
            ep12_girl_count += 1
            ep12_drinking_list.append("Sarah")
        if ep2_fuckHOT or quinn_shop_japanese_lvl>0 or ep3_fuckedRionaQuinn or ep5_fuckedRiona or (ep7_riona_lewd and not ep7_rica_lewd) or ep7_rica_lewd or ep10_riona_lewd or ep9_riona_choice == "DIK":
            ep12_girl_count += 1
            ep12_drinking_list.append("Riona")
        if ep2_fuckHOT or ep4_fuckedMelanie or ep5_hot_lewd or ep8_melanie_lewd or ep9_sarah_melanie_lewd or ep11_mel_lewd:
            ep12_girl_count += 1
            ep12_drinking_list.append("Melanie")
        if ep1_lewd_camila_quinn or quinn_shop_spicy_lvl>0 or ep3_fuckedCamilaAndMona or ep5_fuckedCamila or (ep7_camila_lewd and not ep7_rica_lewd) or ep7_rica_lewd or ep9_camila_lewd or ep11_camila_lewd:
            if not ep11_sage_camila_lewd:
                ep12_girl_count += 1
                ep12_drinking_list.append("Camila")
        if ep4_grindedLily or ep5_lily_lewd or ep7_lily_lewd or ep8_lily_lewd or ep9_lily_nicole_lewd or ep9_others_texted[4] or ep9_cumpetition_join or ep10_rolling:
            ep12_girl_count += 1
            ep12_drinking_list.append("Lily")
        if ep12_bianca_lewd or ep11_bianca_dick == 2:
            ep12_drinking_list.append("Bianca")
        
        if ep3_envyLewd>0 or ep6_envy_lewd or ep8_envy_lewd or ep9_lily_nicole_lewd or ep9_cumpetition_join:
            ep12_girl_count += 1
            ep12_drinking_list.append("Nicole")
        if ep4_lickedAshley:
            ep12_girl_count += 1
            ep12_drinking_list.append("Ashley")
        
        if ep12_ts_lewd or ep6_envy_lewd or ep8_sandy_lewd:
            ep12_girl_count += 1
            ep12_drinking_list.append("Sandy")
        if ep12_ts_lewd:
            ep12_girl_count += 1
            ep12_drinking_list.append("Tania")
        if ep8_sarah_lewd:
            ep12_girl_count += 1
            ep12_drinking_list.append("Kylie")
        if ep3_acceptedJade:
            ep12_drinking_list.append("Jade")
        if ep4_roseLewd:
            ep12_girl_count += 1
            ep12_drinking_list.append("Rose")
        
        if ep11_helped_erin_mia:
            ep12_girl_count += 2
            ep12_drinking_list.append("Mia")
            ep12_drinking_list.append("Erin")
        if ep11_mistletoe > 0:
            ep12_girl_count += 1
            ep12_drinking_list.append("Felicia")
            if ep11_mistletoe > 1:
                ep12_girl_count += 2
                ep12_drinking_list.append("Leanne")
                ep12_drinking_list.append("Charlotte")
        return

# Decompiled by unrpyc {v1.3.2}: https://github.com/CensoredUsername/unrpyc dev-branch

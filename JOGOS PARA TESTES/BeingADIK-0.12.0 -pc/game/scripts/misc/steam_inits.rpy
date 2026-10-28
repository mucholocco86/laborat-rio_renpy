init:
    $ achievement.register("IDS3_06")
    $ achievement.register("IDS3_07")
    $ achievement.register("IDS3_08")
    $ achievement.register("IDS3_09")
    $ achievement.register("IDS3_10")
    $ achievement.register("IDS3_11")
    $ achievement.register("IDS3_12")
    $ achievement.register("IDS3_13")
    $ achievement.register("IDS3_25")
    $ achievement.register("IDS3_26")
    $ achievement.register("IDS3_27")
    $ achievement.register("IDS3_28")
    $ achievement.register("IDS3_29")
    $ achievement.register("IDS3_46")

    if persistent.vaultin == None:
        $ persistent.vaultin = False
    if persistent.vault9 == None:
        $ persistent.vault9 = False
    if persistent.vault10 == None:
        $ persistent.vault10 = False
    if persistent.vault11 == None:
        $ persistent.vault11 = False
    if persistent.vault12 == None:
        $ persistent.vault12 = False


init python:
    def pq_ach_func():
        global steamAchievements
        global currentEpisode
        if steamAchievements and not config.console and not config.developer:
            if currentEpisode == 9 and persistent.pack_quest4_completed:
                achievement.grant("IDS3_26")
                achievement.Sync()
            elif currentEpisode == 10 and persistent.pack_quest5_completed:
                achievement.grant("IDS3_27")
                achievement.Sync()
            elif currentEpisode == 11 and persistent.pack_quest6_completed:
                achievement.grant("IDS3_28")
                achievement.Sync()
            elif currentEpisode == 12 and persistent.pack_quest7_completed:
                achievement.grant("IDS3_29")
                achievement.Sync()
            if persistent.pack_quest4_completed and persistent.pack_quest5_completed and persistent.pack_quest6_completed and persistent.pack_quest7_completed:
                achievement.grant("IDS3_25")
                achievement.Sync()
        return

    def vault_ach_func():
        global steamAchievements
        global currentEpisode
        global vault_ep5
        global vault_ep6
        if steamAchievements and not config.console and not config.developer:
            if currentEpisode == 0:
                persistent.vaultin = True
                achievement.grant("IDS3_07")
                achievement.Sync()
            elif currentEpisode == 9:
                persistent.vault9 = True
                achievement.grant("IDS3_08")
                achievement.Sync()
            elif currentEpisode == 10:
                persistent.vault10 = True
                achievement.grant("IDS3_09")
                achievement.Sync()
            elif currentEpisode == 11:
                persistent.vault11 = True
                achievement.grant("IDS3_10")
                achievement.Sync()
            elif currentEpisode == 12:
                persistent.vault12 = True
                achievement.grant("IDS3_11")
                achievement.Sync()
            if persistent.vaultin and persistent.vault9 and persistent.vault10 and persistent.vault11 and persistent.vault12:
                achievement.grant("IDS3_06")
                achievement.Sync()
        return

label check_steam_achievements_label:


return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

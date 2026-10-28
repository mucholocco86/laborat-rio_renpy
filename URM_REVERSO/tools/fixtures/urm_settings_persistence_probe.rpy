# Isolated probe distinguishing URM per-game persistent settings from global settings ZIP.
label urm_settings_probe_write_start:
    $ x52URM.Settings.seenWelcome = 2
    $ x52URM.Settings.warningDisabled = True
    $ x52URM.Settings.autoUpdateCheck = False
    $ x52URM.Settings.lastLoadedFile = None
    $ x52URM.Settings.showChoicesNotification = True
    $ x52URM.Settings.showWatchPanel = False
    $ x52URM.States.updateNotificationShown = True
    $ x52URM.afterLoad()
    $ x52URM.Settings.lastLoadedFile = None
    $ x52URM.Settings.set("textboxesEnabled", True, globalSetting=False)
    $ renpy.persistent.save()
    $ x52URM.Settings.set("quickmenuEnabled", True, globalSetting=True)
    python:
        import json, os, zipfile
        settings_path = os.path.join(x52URM.Settings.saveDir, "settings")
        with zipfile.ZipFile(settings_path, "r") as zf:
            global_data = json.loads(zf.read("json"))
        assert global_data["quickmenuEnabled"] is True
        print("URM_SETTINGS_WRITE", renpy.store.persistent.URMSettings, global_data, settings_path)
    "URM settings write probe completed."
    $ renpy.quit()

label urm_settings_probe_load_start:
    $ x52URM.Settings.seenWelcome = 2
    $ x52URM.Settings.warningDisabled = True
    $ x52URM.Settings.autoUpdateCheck = False
    $ x52URM.Settings.lastLoadedFile = None
    $ x52URM.Settings.showChoicesNotification = True
    $ x52URM.Settings.showWatchPanel = False
    $ x52URM.States.updateNotificationShown = True
    $ x52URM.afterLoad()
    $ x52URM.Settings.lastLoadedFile = None
    $ per_game = x52URM.Settings.get("textboxesEnabled")
    $ global_value = x52URM.Settings.get("quickmenuEnabled")
    $ global_only = x52URM.Settings.get("quickmenuEnabled", globalSetting=True)
    $ print("URM_SETTINGS_AFTER_NEW_PROCESS", per_game, global_value, global_only, renpy.store.persistent.URMSettings, x52URM.Settings._m1_settings__globalSettings)
    $ assert per_game is True
    $ assert global_value is True
    $ assert global_only is True
    "URM per-game persistent and global settings loaded independently."
    $ renpy.quit()

testcase urm_settings_probe_write:
    run Jump("urm_settings_probe_write_start")
    "URM settings write probe completed."

testcase urm_settings_probe_load:
    run Jump("urm_settings_probe_load_start")
    "URM per-game persistent and global settings loaded independently."

# Isolated runtime probe of original URM .urm persistence. Ren'Py 7.4.11 only.
default urm_file_probe_value = 0

label urm_file_probe_write_start:
    $ x52URM.Settings.seenWelcome = 2
    $ x52URM.Settings.warningDisabled = True
    $ x52URM.Settings.autoUpdateCheck = False
    $ x52URM.Settings.lastLoadedFile = None
    $ x52URM.Settings.showChoicesNotification = True
    $ x52URM.Settings.showWatchPanel = False
    $ x52URM.States.updateNotificationShown = True
    $ x52URM.afterLoad()
    $ x52URM.Settings.lastLoadedFile = None
    $ x52URM.Var("urm_file_probe_value").setValue(7)
    $ x52URM.VarsStore.remember("urm_file_probe_value", "Runtime probe value")
    $ x52URM.VarsStore.freeze("urm_file_probe_value")
    $ x52URM.VarsStore.monitor("urm_file_probe_value")
    $ x52URM.VarsStore.watch("urm_file_probe_value", "Runtime probe watch")
    $ print("URM_FILE_PROBE_BEFORE_SAVE", urm_file_probe_value, x52URM.VarsStore.store, x52URM.VarsStore.watchedStore)
    $ result = x52URM.URMFiles.save("urm-runtime-persistence-probe", overwrite=True)
    $ assert result is True
    $ print("URM_FILE_PROBE_SAVED", result, x52URM.URMFiles.file.filename, x52URM.URMFiles.file.storeNames)
    "URM file write probe completed."
    $ renpy.quit()

label urm_file_probe_load_start:
    $ x52URM.Settings.seenWelcome = 2
    $ x52URM.Settings.warningDisabled = True
    $ x52URM.Settings.autoUpdateCheck = False
    $ x52URM.Settings.lastLoadedFile = None
    $ x52URM.Settings.showChoicesNotification = True
    $ x52URM.Settings.showWatchPanel = False
    $ x52URM.States.updateNotificationShown = True
    $ x52URM.afterLoad()
    $ x52URM.Settings.lastLoadedFile = None
    $ assert urm_file_probe_value == 0
    $ result = x52URM.URMFiles.load("urm-runtime-persistence-probe.urm")
    $ assert result is True
    $ print("URM_FILE_PROBE_AFTER_LOAD", urm_file_probe_value, x52URM.URMFiles.file.storeNames, x52URM.VarsStore.store, x52URM.VarsStore.watchedStore)
    $ assert urm_file_probe_value == 0
    $ assert x52URM.VarsStore.has("urm_file_probe_value")
    $ assert x52URM.VarsStore.isWatched("urm_file_probe_value")
    $ assert x52URM.VarsStore.isFrozen("urm_file_probe_value")
    $ assert x52URM.VarsStore.isMonitored("urm_file_probe_value")
    "URM metadata loaded while game variable remains at its process default."
    $ renpy.quit()

testcase urm_file_probe_write:
    run Jump("urm_file_probe_write_start")
    "URM file write probe completed."

testcase urm_file_probe_load:
    run Jump("urm_file_probe_load_start")
    "URM metadata loaded while game variable remains at its process default."

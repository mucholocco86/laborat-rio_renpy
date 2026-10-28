# Isolated two-process probe for original URM labels and text replacements stores.
label urm_store_probe_label:
    return

label urm_store_probe_write_start:
    $ x52URM.Settings.seenWelcome = 2
    $ x52URM.Settings.warningDisabled = True
    $ x52URM.Settings.autoUpdateCheck = False
    $ x52URM.Settings.lastLoadedFile = None
    $ x52URM.Settings.showChoicesNotification = True
    $ x52URM.Settings.showWatchPanel = False
    $ x52URM.States.updateNotificationShown = True
    $ x52URM.afterLoad()
    $ x52URM.Settings.lastLoadedFile = None
    $ x52URM.LabelsStore.remember("urm_store_probe_label", "Persisted label title")
    $ x52URM.TextRepl.add("WellsProbeChoice", "URMLoadedChoice", caseInsensitive=False, replacePartialWords=False)
    $ print("URM_LABELS_BEFORE_SAVE", x52URM.LabelsStore.store)
    $ print("URM_REPLACEMENTS_BEFORE_SAVE", x52URM.TextRepl.store)
    $ result = x52URM.URMFiles.save("urm-label-replacements-probe", overwrite=True)
    $ assert result is True
    $ print("URM_LABEL_REPL_SAVED", x52URM.URMFiles.file.filename, x52URM.URMFiles.file.storeNames)
    "URM labels and replacements write probe completed."
    $ renpy.quit()

label urm_store_probe_load_start:
    $ x52URM.Settings.seenWelcome = 2
    $ x52URM.Settings.warningDisabled = True
    $ x52URM.Settings.autoUpdateCheck = False
    $ x52URM.Settings.lastLoadedFile = None
    $ x52URM.Settings.showChoicesNotification = True
    $ x52URM.Settings.showWatchPanel = False
    $ x52URM.States.updateNotificationShown = True
    $ x52URM.afterLoad()
    $ x52URM.Settings.lastLoadedFile = None
    $ result = x52URM.URMFiles.load("urm-label-replacements-probe.urm")
    $ assert result is True
    $ assert x52URM.LabelsStore.has("urm_store_probe_label")
    $ assert x52URM.LabelsStore.store["urm_store_probe_label"]["name"] == "Persisted label title"
    $ assert x52URM.TextRepl.store["WellsProbeChoice"]["replacement"] == "URMLoadedChoice"
    $ filtered = renpy.config.say_menu_text_filter("WellsProbeChoice")
    $ print("URM_LABEL_REPL_AFTER_LOAD", x52URM.LabelsStore.store, x52URM.TextRepl.store, filtered)
    $ assert filtered == "URMLoadedChoice"
    $ assert renpy.has_label("urm_store_probe_label")
    "URM labels and replacement rules restored in a fresh process."
    $ renpy.quit()

testcase urm_label_replacements_write:
    run Jump("urm_store_probe_write_start")
    "URM labels and replacements write probe completed."

testcase urm_label_replacements_load:
    run Jump("urm_store_probe_load_start")
    "URM labels and replacement rules restored in a fresh process."

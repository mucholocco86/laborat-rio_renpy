# Isolated runtime probe for original URM textbox customization store.
define urm_textbox_probe_character = Character("Textbox probe")
define urm_textbox_probe_other = Character("Other probe")

label urm_textbox_probe_write_start:
    $ x52URM.Settings.seenWelcome = 2
    $ x52URM.Settings.warningDisabled = True
    $ x52URM.Settings.autoUpdateCheck = False
    $ x52URM.Settings.lastLoadedFile = None
    $ x52URM.Settings.showChoicesNotification = True
    $ x52URM.Settings.showWatchPanel = False
    $ x52URM.States.updateNotificationShown = True
    $ x52URM.afterLoad()
    $ x52URM.Settings.lastLoadedFile = None
    $ x52URM.TextBox.Settings = x52URM.TextBoxSettings("urm_textbox_probe_character")
    $ x52URM.TextBox.Settings.enableTemp("urm_textbox_probe_character")
    $ x52URM.TextBox.Settings.whoSize = 44
    $ x52URM.TextBox.Settings.whoColor = "#12AB34"
    $ x52URM.TextBox.Settings.whatBold = True
    $ x52URM.TextBox.Settings.commitTemp("urm_textbox_probe_character")
    $ print("URM_TEXTBOX_BEFORE_SAVE", x52URM.TextBoxSettings.store)
    $ result = x52URM.URMFiles.save("urm-textbox-customization-probe", overwrite=True)
    $ assert result is True
    $ print("URM_TEXTBOX_SAVED", x52URM.URMFiles.file.filename, x52URM.URMFiles.file.storeNames)
    "URM textbox write probe completed."
    $ renpy.quit()

label urm_textbox_probe_load_start:
    $ x52URM.Settings.seenWelcome = 2
    $ x52URM.Settings.warningDisabled = True
    $ x52URM.Settings.autoUpdateCheck = False
    $ x52URM.Settings.lastLoadedFile = None
    $ x52URM.Settings.showChoicesNotification = True
    $ x52URM.Settings.showWatchPanel = False
    $ x52URM.States.updateNotificationShown = True
    $ x52URM.afterLoad()
    $ x52URM.Settings.lastLoadedFile = None
    $ result = x52URM.URMFiles.load("urm-textbox-customization-probe.urm")
    $ assert result is True
    $ x52URM.TextBox.Settings = x52URM.TextBoxSettings(urm_textbox_probe_character)
    $ print("URM_TEXTBOX_AFTER_LOAD", x52URM.TextBoxSettings.store, x52URM.TextBox.Settings.whoSize, x52URM.TextBox.Settings.whoColor, x52URM.TextBox.Settings.whatBold)
    $ assert x52URM.TextBox.Settings.whoSize == 44
    $ assert x52URM.TextBox.Settings.whoColor == "#12AB34"
    $ assert x52URM.TextBox.Settings.whatBold is True
    $ x52URM.TextBox.Settings = x52URM.TextBoxSettings(urm_textbox_probe_other)
    $ assert x52URM.TextBox.Settings.whoSize == x52URM.TextBoxSettings.defaultValues["whoSize"]
    "URM textbox settings restored for the matching character."
    $ renpy.quit()

testcase urm_textbox_probe_write:
    run Jump("urm_textbox_probe_write_start")
    "URM textbox write probe completed."

testcase urm_textbox_probe_load:
    run Jump("urm_textbox_probe_load_start")
    "URM textbox settings restored for the matching character."

# Isolated runtime probe for URM Snapshots shallow values.
default urm_snapshot_probe_scalar = 10
default urm_snapshot_probe_list = [1, 2]
default urm_snapshot_probe_dict = {"a": 1}

label urm_snapshot_probe_start:
    $ x52URM.Settings.seenWelcome = 2
    $ x52URM.Settings.warningDisabled = True
    $ x52URM.Settings.autoUpdateCheck = False
    $ x52URM.Settings.lastLoadedFile = None
    $ x52URM.Settings.showChoicesNotification = True
    $ x52URM.Settings.showWatchPanel = False
    $ x52URM.States.updateNotificationShown = True
    $ x52URM.afterLoad()
    $ x52URM.Snapshots.create("shallow-probe")
    $ assert x52URM.Var("urm_snapshot_probe_scalar").setValue(20)
    $ assert x52URM.Var("urm_snapshot_probe_list[0]").setValue(9)
    $ assert x52URM.Var('urm_snapshot_probe_dict["a"]').setValue(9)
    $ changed = x52URM.Snapshots.findChanges("shallow-probe")
    $ names = sorted([entry["old"].name for entry in changed])
    $ print("URM_SNAPSHOT_PROBE_VALUES", urm_snapshot_probe_scalar, urm_snapshot_probe_list, urm_snapshot_probe_dict)
    $ print("URM_SNAPSHOT_PROBE_CHANGED_NAMES", names)
    $ assert "urm_snapshot_probe_scalar" in names
    $ assert "urm_snapshot_probe_list" not in names
    $ assert "urm_snapshot_probe_dict" not in names
    "URM snapshot shallow-reference probe completed."
    $ renpy.quit()

testcase urm_snapshot_probe:
    run Jump("urm_snapshot_probe_start")
    "URM snapshot shallow-reference probe completed."

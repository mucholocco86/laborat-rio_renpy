# Isolated runtime probe for URM Snapshots shallow values and equality comparison.
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
    $ renpy.store.urm_snapshot_probe_scalar = 20
    $ renpy.store.urm_snapshot_probe_list[0] = 9
    $ renpy.store.urm_snapshot_probe_dict["a"] = 9
    $ print("URM_SNAPSHOT_PROBE_AFTER_MUTATION", renpy.store.urm_snapshot_probe_scalar, renpy.store.urm_snapshot_probe_list, renpy.store.urm_snapshot_probe_dict)
    $ changed = x52URM.Snapshots.findChanges("shallow-probe")
    $ names = sorted([entry["old"].name for entry in changed])
    $ print("URM_SNAPSHOT_PROBE_CHANGED_NAMES", names)
    $ assert names == ["urm_snapshot_probe_scalar"]

    $ renpy.store.urm_snapshot_probe_list = [3, 4]
    $ renpy.store.urm_snapshot_probe_dict = {"a": 3}
    $ changed_after_replacement = x52URM.Snapshots.findChanges("shallow-probe")
    $ replacement_names = sorted([entry["old"].name for entry in changed_after_replacement])
    $ print("URM_SNAPSHOT_PROBE_REPLACED_NAMES", replacement_names)
    $ assert replacement_names == ["urm_snapshot_probe_dict", "urm_snapshot_probe_list", "urm_snapshot_probe_scalar"]

    $ x52URM.Snapshots.create("equal-content-probe")
    $ renpy.store.urm_snapshot_probe_list = [3, 4]
    $ renpy.store.urm_snapshot_probe_dict = {"a": 3}
    $ changed_equal_content = x52URM.Snapshots.findChanges("equal-content-probe")
    $ equal_content_names = sorted([entry["old"].name for entry in changed_equal_content])
    $ print("URM_SNAPSHOT_PROBE_EQUAL_CONTENT_NAMES", equal_content_names)
    $ assert equal_content_names == []

    "URM snapshot shallow-reference probe completed."
    $ renpy.quit()

testcase urm_snapshot_probe:
    run Jump("urm_snapshot_probe_start")
    "URM snapshot shallow-reference probe completed."

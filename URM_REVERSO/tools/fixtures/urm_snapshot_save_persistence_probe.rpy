# Two-process test of whether the original URM Snapshots object is included in a native Ren'Py save.
# Ren'Py 7.4.11 and the unchanged URM package; disposable copy only.

default urm_snapshot_save_probe_value = 17

label urm_snapshot_save_write_start:
    $ x52URM.Settings.seenWelcome = 2
    $ x52URM.Settings.warningDisabled = True
    $ x52URM.Settings.autoUpdateCheck = False
    $ x52URM.Settings.lastLoadedFile = None
    $ x52URM.Settings.showChoicesNotification = True
    $ x52URM.Settings.showWatchPanel = False
    $ x52URM.States.updateNotificationShown = True
    $ x52URM.afterLoad()
    $ x52URM.Settings.lastLoadedFile = None

    "Checkpoint before snapshot save."
    $ renpy.fix_rollback()

    $ assert not x52URM.Snapshots.exists("native-save-probe")
    $ x52URM.Snapshots.create("native-save-probe")
    $ assert x52URM.Snapshots.exists("native-save-probe")
    $ print("URM_SNAPSHOT_SAVE_BEFORE", x52URM.Snapshots.snapshotNames, x52URM.Snapshots.getSnapshotTime("native-save-probe"))
    $ renpy.save("urm-snapshot-native-save-probe", "URM snapshot persistence probe")
    if renpy.session.get("urm_snapshot_fresh_load_marker", False):
        jump urm_snapshot_save_verify
    $ print("URM_SNAPSHOT_SAVE_AFTER", x52URM.Snapshots.snapshotNames)
    "Snapshot was created and native save was written."
    $ renpy.quit()

label urm_snapshot_save_load_start:
    $ renpy.session.pop("urm_snapshot_fresh_load_marker", None)
    $ assert renpy.can_load("urm-snapshot-native-save-probe")
    $ assert not x52URM.Snapshots.exists("native-save-probe")
    $ renpy.session["urm_snapshot_fresh_load_marker"] = True
    $ print("URM_SNAPSHOT_NEW_PROCESS_BEFORE_LOAD", x52URM.Snapshots.snapshotNames)
    $ renpy.load("urm-snapshot-native-save-probe")

label urm_snapshot_save_verify:
    $ restored = x52URM.Snapshots.exists("native-save-probe")
    $ print("URM_SNAPSHOT_AFTER_FRESH_PROCESS_LOAD", x52URM.Snapshots.snapshotNames, restored, urm_snapshot_save_probe_value)
    $ assert renpy.session.get("urm_snapshot_fresh_load_marker", False)
    $ assert restored is False
    "Fresh process did not restore the URM snapshot object."
    $ renpy.quit()

testcase urm_snapshot_native_save_write:
    run Jump("urm_snapshot_save_write_start")
    "Checkpoint before snapshot save."
    type RETURN
    "Snapshot was created and native save was written."

testcase urm_snapshot_native_save_load:
    run Jump("urm_snapshot_save_load_start")
    "Fresh process did not restore the URM snapshot object."

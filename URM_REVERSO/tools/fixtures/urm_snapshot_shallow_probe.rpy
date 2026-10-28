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
    $ names = sorted([entry["old"].name for entry in changed if entry["old"].name.startswith("urm_snapshot_probe_")])
    $ print("URM_SNAPSHOT_PROBE_CHANGED_NAMES", names)
    $ if names != ["urm_snapshot_probe_scalar"]: raise Exception("unexpected in-place diff: {}".format(names))

    $ renpy.store.urm_snapshot_probe_list = [3, 4]
    $ renpy.store.urm_snapshot_probe_dict = {"a": 3}
    $ changed_after_replacement = x52URM.Snapshots.findChanges("shallow-probe")
    $ replacement_names = sorted([entry["old"].name for entry in changed_after_replacement if entry["old"].name.startswith("urm_snapshot_probe_")])
    $ print("URM_SNAPSHOT_PROBE_REPLACED_NAMES", replacement_names)
    $ if replacement_names != ["urm_snapshot_probe_dict", "urm_snapshot_probe_list", "urm_snapshot_probe_scalar"]: raise Exception("unexpected replacement diff: {}".format(replacement_names))

    $ x52URM.Snapshots.create("equal-content-probe")
    $ renpy.store.urm_snapshot_probe_list = [3, 4]
    $ renpy.store.urm_snapshot_probe_dict = {"a": 3}
    $ changed_equal_content = x52URM.Snapshots.findChanges("equal-content-probe")
    $ equal_content_names = sorted([entry["old"].name for entry in changed_equal_content if entry["old"].name.startswith("urm_snapshot_probe_")])
    $ print("URM_SNAPSHOT_PROBE_EQUAL_CONTENT_NAMES", equal_content_names)
    $ if equal_content_names: raise Exception("equal-content replacements appeared in diff: {}".format(equal_content_names))

    $ renpy.store.urm_snapshot_probe_edit_target = 10
    $ x52URM.Snapshots.create("edit-probe")
    $ renpy.store.urm_snapshot_probe_edit_target = 20
    $ edit_changes = x52URM.Snapshots.findChanges("edit-probe")
    $ edit_entry = [entry for entry in edit_changes if entry["old"].name == "urm_snapshot_probe_edit_target"][0]
    $ old_editable = edit_entry["old"].isEditable
    $ new_editable = edit_entry["new"].isEditable
    $ old_value_before = edit_entry["old"].value
    $ new_value_before = edit_entry["new"].value
    $ old_edit_result = edit_entry["old"].setValue("30")
    $ current_after_old_edit = renpy.store.urm_snapshot_probe_edit_target
    $ new_edit_result = edit_entry["new"].setValue("30")
    $ current_after_new_edit = renpy.store.urm_snapshot_probe_edit_target
    $ print("URM_SNAPSHOT_PROBE_EDIT_VARS", old_editable, new_editable, old_value_before, new_value_before)
    $ print("URM_SNAPSHOT_PROBE_EDIT_RESULTS", old_edit_result, current_after_old_edit, new_edit_result, current_after_new_edit, edit_entry["old"].value)
    $ if old_editable or not new_editable: raise Exception("unexpected editability flags")
    $ if old_value_before != 10 or new_value_before != 20: raise Exception("unexpected old/new values")
    $ if old_edit_result or current_after_old_edit != 20: raise Exception("snapshot-side Var changed current gameplay")
    $ if not new_edit_result or current_after_new_edit != 30 or edit_entry["old"].value != 10: raise Exception("current-side Var did not edit gameplay independently")

    "URM snapshot shallow-reference probe completed."
    $ renpy.quit()

testcase urm_snapshot_probe:
    run Jump("urm_snapshot_probe_start")
    "URM snapshot shallow-reference probe completed."

# Isolated runtime probe for URM Snapshots shallow values and equality comparison.
default urm_snapshot_probe_scalar = 10
default urm_snapshot_probe_list = [1, 2]
default urm_snapshot_probe_dict = {"a": 1}
default urm_snapshot_probe_deleted = 41

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

    $ x52URM.Snapshots.create("deleted-probe")
    $ delattr(renpy.store, "urm_snapshot_probe_deleted")
    $ deleted_changes = x52URM.Snapshots.findChanges("deleted-probe")
    $ deleted_entry = [entry for entry in deleted_changes if entry["old"].name == "urm_snapshot_probe_deleted"][0]
    $ deleted_old_value = deleted_entry["old"].value
    $ deleted_new_value = deleted_entry["new"].value
    $ deleted_old_editable = deleted_entry["old"].isEditable
    $ deleted_new_editable = deleted_entry["new"].isEditable
    $ deleted_new_type = deleted_entry["new"].varType
    $ deleted_new_set_result = deleted_entry["new"].setValue("42")
    $ print("URM_SNAPSHOT_PROBE_DELETED_VAR", deleted_old_value, deleted_new_value, deleted_old_editable, deleted_new_editable, deleted_new_type, deleted_new_set_result, hasattr(renpy.store, "urm_snapshot_probe_deleted"))
    $ if deleted_old_value != 41 or deleted_new_value is not None: raise Exception("unexpected deleted variable values")
    $ if deleted_old_editable or not deleted_new_editable or deleted_new_type != "unknown": raise Exception("unexpected deleted variable editor flags")
    $ if deleted_new_set_result or hasattr(renpy.store, "urm_snapshot_probe_deleted"): raise Exception("deleted variable unexpectedly recreated by setValue")

    $ x52URM.Snapshots.create("added-probe")
    $ setattr(renpy.store, "urm_snapshot_probe_added", 7)
    $ added_changes = x52URM.Snapshots.findChanges("added-probe")
    $ added_entry = [entry for entry in added_changes if entry["old"].name == "urm_snapshot_probe_added"][0]
    $ added_old_value = added_entry["old"].value
    $ added_new_value = added_entry["new"].value
    $ added_old_editable = added_entry["old"].isEditable
    $ added_new_editable = added_entry["new"].isEditable
    $ added_old_type = added_entry["old"].varType
    $ added_old_set_result = added_entry["old"].setValue("8")
    $ added_new_set_result = added_entry["new"].setValue("8")
    $ print("URM_SNAPSHOT_PROBE_ADDED_VAR", added_old_value, added_new_value, added_old_editable, added_new_editable, added_old_type, added_old_set_result, added_new_set_result, renpy.store.urm_snapshot_probe_added, added_entry["old"].value)
    $ if added_old_value is not None or added_new_value != 7: raise Exception("unexpected added variable values")
    $ if added_old_editable or not added_new_editable or added_old_type != "unknown": raise Exception("unexpected added variable editor flags")
    $ if added_old_set_result or not added_new_set_result or renpy.store.urm_snapshot_probe_added != 8 or added_entry["old"].value is not None: raise Exception("added variable edit routing failed")

    $ renpy.store.urm_snapshot_probe_pair_common = 1
    $ renpy.store.urm_snapshot_probe_pair_old_only = 11
    $ x52URM.Snapshots.create("pair-a")
    $ renpy.store.urm_snapshot_probe_pair_common = 2
    $ delattr(renpy.store, "urm_snapshot_probe_pair_old_only")
    $ renpy.store.urm_snapshot_probe_pair_new_only = 22
    $ x52URM.Snapshots.create("pair-b")
    $ pair_changes = x52URM.Snapshots.findChanges("pair-a", "pair-b")
    $ pair_by_name = dict((entry["old"].name, entry) for entry in pair_changes if entry["old"].name.startswith("urm_snapshot_probe_pair_"))
    $ common_entry = pair_by_name["urm_snapshot_probe_pair_common"]
    $ old_only_entry = pair_by_name["urm_snapshot_probe_pair_old_only"]
    $ new_only_entry = pair_by_name["urm_snapshot_probe_pair_new_only"]
    $ pair_summary = (common_entry["old"].value, common_entry["new"].value, old_only_entry["old"].value, old_only_entry["new"].value, new_only_entry["old"].value, new_only_entry["new"].value)
    $ pair_editable = (common_entry["old"].isEditable, common_entry["new"].isEditable, old_only_entry["old"].isEditable, old_only_entry["new"].isEditable, new_only_entry["old"].isEditable, new_only_entry["new"].isEditable)
    $ pair_edit_old = common_entry["old"].setValue("99")
    $ pair_edit_new = common_entry["new"].setValue("99")
    $ print("URM_SNAPSHOT_PROBE_PAIR_VALUES", pair_summary)
    $ print("URM_SNAPSHOT_PROBE_PAIR_EDITABLE", pair_editable)
    $ print("URM_SNAPSHOT_PROBE_PAIR_SET_RESULTS", pair_edit_old, pair_edit_new, renpy.store.urm_snapshot_probe_pair_common)
    $ if pair_summary != (1, 2, 11, None, None, 22): raise Exception("unexpected snapshot pair values: {}".format(pair_summary))
    $ if pair_editable != (False, False, False, False, False, False): raise Exception("snapshot pair Var unexpectedly editable: {}".format(pair_editable))
    $ if pair_edit_old or pair_edit_new or renpy.store.urm_snapshot_probe_pair_common != 2: raise Exception("snapshot pair editor changed a snapshot or gameplay value")

    "URM snapshot shallow-reference probe completed."
    $ renpy.quit()

testcase urm_snapshot_probe:
    run Jump("urm_snapshot_probe_start")
    "URM snapshot shallow-reference probe completed."

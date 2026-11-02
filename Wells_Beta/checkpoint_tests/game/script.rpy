default evRel = 0
default kaRel = 0
default active_patch = False
default wells_test_capture_error = None
default wells_test_replay_debug = None
default wells_test_auto_restart = False
default wells_test_force_mismatch = False
default wells_test_checkpoint_file = None

image wells_test_entry_anchor = Solid("#3b2020")
image wells_test_anchor = Solid("#243044")

init -100 python:
    # Stand-ins are used only to compile the shared panel module in this fixture.
    def wells_ui(value):
        return value

    def wells_ui_signed(value):
        return value

    def wells_test_expect(condition, message):
        if not condition:
            raise Exception(message)

screen choice(items):
    modal True
    vbox:
        xpos 0
        ypos 0
        xsize config.screen_width
        ysize config.screen_height
        spacing 0
        for i in items:
            textbutton i.caption action i.action:
                xfill True
                ysize int(config.screen_height / len(items))


label wells_checkpoint_entry:
    show wells_test_entry_anchor
    menu:
        "Escolha A":
            $ evRel += 10
            $ kaRel = 3
            $ active_patch = True
            jump wells_checkpoint_target

        "Escolha B":
            $ evRel -= 10
            $ kaRel = 1
            jump wells_checkpoint_target

label wells_checkpoint_target:
    if wells_tracker_replay is not None:
        "Intervening unseen dialogue."
    if wells_test_force_mismatch:
        $ evRel = -1
        $ kaRel = -1
        $ active_patch = False
    show wells_test_anchor
    $ wells_test_anchor_state = _wells_tracker_current_anchor()
    python:
        _wells_ctx = renpy.game.context()
        _wells_layers = getattr(getattr(_wells_ctx, "scene_lists", None), "layers", {})
        _wells_scene_names = {}
        for _wells_layer, _wells_entries in _wells_layers.items():
            _wells_scene_names[_wells_layer] = [
                (getattr(_wells_entry, "tag", None), getattr(_wells_entry, "name", None))
                for _wells_entry in _wells_entries
            ]
        wells_test_expect(wells_test_anchor_state is not None, "No active image anchor; scene layers={!r}".format(_wells_scene_names))
    if wells_test_auto_restart:
        python:
            wells_test_payload = _wells_tracker_read_json(wells_test_checkpoint_file)
            wells_test_expect(wells_tracker_replay is None, "Full restart replay did not finish at the saved image: {!r}".format(wells_tracker_replay))
            wells_test_expect(evRel == wells_test_payload["variables"].get("evRel"), "Full restart did not restore evRel from JSON: {!r}".format(evRel))
            wells_test_expect(kaRel == wells_test_payload["variables"].get("kaRel"), "Full restart did not restore kaRel from JSON: {!r}".format(kaRel))
            wells_test_expect(active_patch is wells_test_payload["variables"].get("active_patch"), "Full restart did not restore active_patch from JSON: {!r}".format(active_patch))
            with io.open(os.path.join(WELLS_TRACKER_DIR, "runtime_restart_passed.txt"), "w", encoding="utf-8") as wells_test_result_file:
                wells_test_result_file.write("passed")
        $ renpy.quit()
    else:
        $ wells_salvar_checkpoint()
        pause 0.1
    return

label main_menu:
    return

label start:
    if wells_test_auto_restart:
        if wells_tracker_replay is not None:
            $ wells_test_checkpoint_file = wells_tracker_replay.get("filename")
            $ wells_test_force_mismatch = True
            jump wells_checkpoint_entry
        $ wells_test_records = wells_tracker_list_records()
        $ wells_test_expect(wells_test_records, "Full restart fixture has no captured JSON checkpoint.")
        $ wells_test_checkpoint_file = wells_test_records[0]["filename"]
        $ wells_test_payload = _wells_tracker_read_json(wells_test_checkpoint_file)
        $ wells_test_expect(wells_test_payload.get("version") == WELLS_TRACKER_VERSION, "Restart fixture checkpoint version is invalid: {!r}".format(wells_test_payload))
        $ wells_test_expect(wells_test_payload.get("checkpoint_image"), "Restart fixture checkpoint has no image anchor: {!r}".format(wells_test_payload))
        $ wells_test_expect(isinstance(wells_test_payload.get("choices"), list), "Restart fixture choices are invalid: {!r}".format(wells_test_payload))
        $ wells_test_expect(isinstance(wells_test_payload.get("variables"), dict), "Restart fixture variables are invalid: {!r}".format(wells_test_payload))
        $ evRel = -1
        $ kaRel = -1
        $ active_patch = False
        $ wells_tracker_request_load(wells_test_checkpoint_file)
        $ renpy.quit()
    # Keep the test game in a stable interaction instead of bouncing back to
    # the main menu while Ren'Py's test runner drives the fixture.
    pause 3600

testcase wells_checkpoint_capture:
    run Jump("wells_checkpoint_entry")
    click "Escolha A"
    python:
        wells_test_expect(len(wells_tracker_choices) == 1, "Expected one captured choice; got {!r}; capture_error={!r}".format(wells_tracker_choices, wells_test_capture_error))
        wells_test_expect(wells_tracker_choices[0]["selected_label"] == "Escolha A", "Wrong selected label: {!r}".format(wells_tracker_choices[0]))
        wells_test_expect(wells_tracker_choices[0]["choice_value"] == 0, "Wrong choice return value: {!r}".format(wells_tracker_choices[0]))
        wells_test_records = wells_tracker_list_records()
        wells_test_expect(wells_test_records, "No checkpoint JSON; error={!r}, anchor={!r}, directory={!r}, files={!r}".format(wells_test_capture_error, wells_test_anchor_state, WELLS_TRACKER_DIR, os.listdir(WELLS_TRACKER_DIR) if os.path.isdir(WELLS_TRACKER_DIR) else None))
        wells_test_payload = _wells_tracker_read_json(wells_test_records[0]["filename"])
        wells_test_expect(wells_test_payload["version"] == 3, "Unexpected payload version: {!r}".format(wells_test_payload))
        wells_test_expect(wells_test_payload.get("script_node") is not None, "Checkpoint did not capture a script-node anchor: {!r}".format(wells_test_payload))
        wells_test_expect(wells_test_payload["choices"][0]["selected_label"] == "Escolha A", "Choice missing from payload: {!r}".format(wells_test_payload))
        wells_test_expect(wells_test_payload["variables"].get("evRel") == 10, "evRel not captured: {!r}".format(wells_test_payload.get("variables")))
        wells_test_expect(wells_test_payload["variables"].get("kaRel") == 3, "kaRel not captured: {!r}".format(wells_test_payload.get("variables")))
        wells_test_expect(wells_test_payload["variables"].get("active_patch") is True, "active_patch not captured: {!r}".format(wells_test_payload.get("variables")))
        renpy.save("wells_normal_save_probe")
        wells_test_expect(renpy.can_load("wells_normal_save_probe"), "Normal Ren'Py save could not be loaded")

testcase wells_checkpoint_rebuild:
    python:
        store.wells_test_replay_debug = None
        store.wells_tracker_choices = []
        store.evRel = -1
        store.kaRel = -1
        store.active_patch = False
        wells_test_records = wells_tracker_list_records()
        wells_test_expect(wells_test_records, "Capture fixture must write a checkpoint before rebuild")
        wells_test_payload = _wells_tracker_read_json(wells_test_records[0]["filename"])
        wells_test_original_skip_unseen = renpy.game.preferences.skip_unseen
        wells_test_original_skip_after_choices = renpy.game.preferences.skip_after_choices
        _wells_tracker_write_pending(wells_test_records[0]["filename"])
        wells_test_expect(os.path.isfile(WELLS_TRACKER_PENDING), "Checkpoint request did not leave a pending-load marker")
        with io.open(WELLS_TRACKER_PENDING, "r", encoding="utf-8") as wells_test_pending_stream:
            wells_test_expect(wells_test_pending_stream.read().strip() == wells_test_records[0]["filename"], "Pending-load marker has the wrong checkpoint")
        wells_test_expect(_wells_tracker_activate_pending_load(), "Bootstrap did not activate the pending checkpoint")
        wells_test_expect(wells_tracker_replay.get("filename") == wells_test_records[0]["filename"], "Bootstrap activated the wrong checkpoint")
    $ renpy.config.skipping = "fast"
    run Jump("wells_checkpoint_entry")
    pause until eval (wells_tracker_replay is None) timeout 30.0
    python:
        wells_test_expect(wells_tracker_replay is None, "Replay did not finish: {!r}".format(wells_tracker_replay))
        wells_test_expect(store.evRel == wells_test_payload["variables"].get("evRel"), "evRel was not restored from JSON: {!r}; replay={!r}".format(store.evRel, store.wells_test_replay_debug))
        wells_test_expect(store.kaRel == wells_test_payload["variables"].get("kaRel"), "kaRel was not restored from JSON: {!r}; replay={!r}".format(store.kaRel, store.wells_test_replay_debug))
        wells_test_expect(store.active_patch is wells_test_payload["variables"].get("active_patch"), "active_patch was not restored from JSON: {!r}".format(store.active_patch))
        wells_test_expect(renpy.game.preferences.skip_unseen == wells_test_original_skip_unseen, "skip-unseen preference was not restored")
        wells_test_expect(renpy.game.preferences.skip_after_choices == wells_test_original_skip_after_choices, "skip-after-choices preference was not restored")
        wells_test_expect(renpy.config.skipping is None, "Skip mode was not restored")
        wells_test_expect(len(store.wells_tracker_choices) == 1, "Replay choice count is wrong: {!r}".format(store.wells_tracker_choices))
        wells_test_expect(wells_tracker_choices[0]["selected_label"] == "Escolha A", "Replay selected wrong choice: {!r}".format(wells_tracker_choices))

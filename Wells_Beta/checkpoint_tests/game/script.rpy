default evRel = 0
default kaRel = 0
default active_patch = False

image wells_test_anchor = Solid("#243044")

init -100 python:
    # Stand-ins are used only to compile the shared panel module in this fixture.
    def wells_ui(value):
        return value

    def wells_ui_signed(value):
        return value

label wells_checkpoint_entry:
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
    show wells_test_anchor
    pause 0.1
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
        assert wells_test_anchor_state is not None, "No active image anchor; scene layers={!r}".format(_wells_scene_names)
    $ wells_salvar_checkpoint()
    return

label start:
    # Keep the test game in a stable interaction instead of bouncing back to
    # the main menu while Ren'Py's test runner drives the fixture.
    pause 3600

testcase wells_checkpoint_capture:
    run Call("wells_checkpoint_entry")
    click pos (640, 340)
    python:
        assert len(wells_tracker_choices) == 1
        assert wells_tracker_choices[0]["selected_label"] == "Escolha A"
        assert wells_tracker_choices[0]["choice_value"] == 0
        wells_test_records = wells_tracker_list_records()
        assert wells_test_records, "No checkpoint JSON; anchor={!r}, directory={!r}, files={!r}".format(wells_test_anchor_state, WELLS_TRACKER_DIR, os.listdir(WELLS_TRACKER_DIR) if os.path.isdir(WELLS_TRACKER_DIR) else None)
        wells_test_payload = _wells_tracker_read_json(wells_test_records[0]["filename"])
        assert wells_test_payload["version"] == 3
        assert wells_test_payload["choices"][0]["selected_label"] == "Escolha A"
        assert wells_test_payload["variables"]["evRel"] == 10
        assert wells_test_payload["variables"]["kaRel"] == 3
        assert wells_test_payload["variables"]["active_patch"] is True

testcase wells_checkpoint_rebuild:
    $ wells_tracker_choices = []
    $ evRel = -1
    $ kaRel = -1
    $ active_patch = False
    $ wells_tracker_replay = {
        "filename": "test.json",
        "choices": [{
            "choice_value": 0,
            "selected_index": 0,
            "selected_label": "Escolha A",
            "source_file": None,
            "options": [
                {"label": "Escolha A", "value": 0},
                {"label": "Escolha B", "value": 1},
            ],
        }],
        "cursor": 0,
        "anchor": {"image_name": "wells_test_anchor", "asset_file": None, "script_node": None},
        "variables": {"evRel": 56, "kaRel": 12, "active_patch": True},
    }
    $ renpy.config.skipping = "fast"
    run Call("wells_checkpoint_entry")
    python:
        assert wells_tracker_replay is None
        assert evRel == 56
        assert kaRel == 12
        assert active_patch is True
        assert len(wells_tracker_choices) == 1
        assert wells_tracker_choices[0]["selected_label"] == "Escolha A"

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
    $ renpy.log("WELLS_TEST_ANCHOR " + repr(wells_test_anchor_state))
    if wells_test_anchor_state is None:
        $ renpy.log("WELLS_TEST_ANCHOR_MISSING")
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
        assert wells_test_records
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

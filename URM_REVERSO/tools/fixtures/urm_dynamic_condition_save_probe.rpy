# Native Ren'Py save/load after editing and selecting a dynamic Choice through original URM UI.
default urm_dynamic_save_gate = 0
default urm_dynamic_save_route = None

label urm_dynamic_save_probe_start:
    if renpy.test.testexecution.urm_dynamic_save_reentered:
        jump urm_dynamic_save_probe_verify

    $ urm_dynamic_save_gate = 0
    $ urm_dynamic_save_route = None
    $ renpy.config.fix_rollback_without_choice = False
    $ renpy.game.context().rollback = True
    $ renpy.store._rollback = True
    $ x52URM.Settings.seenWelcome = 2
    $ x52URM.Settings.warningDisabled = True
    $ x52URM.Settings.autoUpdateCheck = False
    $ x52URM.Settings.lastLoadedFile = None
    $ x52URM.Settings.showChoicesNotification = True
    $ x52URM.Settings.showWatchPanel = False
    $ x52URM.States.updateNotificationShown = True
    $ x52URM.afterLoad()

    menu:
        "Native save route A":
            $ urm_dynamic_save_route = "A"
        "Native save route B":
            $ urm_dynamic_save_route = "B"
        "Save route C" if urm_dynamic_save_gate == 1:
            $ urm_dynamic_save_route = "C"

    $ renpy.fix_rollback()
    if urm_dynamic_save_route == "C":
        "Save probe route C."
        jump urm_dynamic_save_probe_save
    elif urm_dynamic_save_route == "B":
        "Save probe route B."
    else:
        "Save probe route A."

label urm_dynamic_save_probe_continue:
    "Save probe continuation."
    jump urm_dynamic_save_probe_continue

label urm_dynamic_save_probe_save:
    if renpy.test.testexecution.urm_dynamic_save_reentered:
        jump urm_dynamic_save_probe_verify
    if urm_dynamic_save_gate != 1 or urm_dynamic_save_route != "C":
        $ raise Exception("Save probe reached save point without edited condition and route C")
    $ print("DYNAMIC_SAVE_BEFORE_SAVE", urm_dynamic_save_gate, urm_dynamic_save_route, renpy.game.context().current)
    if renpy.can_load("urm-dynamic-choice-edit-roundtrip"):
        $ renpy.unlink_save("urm-dynamic-choice-edit-roundtrip")
    $ renpy.save("urm-dynamic-choice-edit-roundtrip", "Dynamic Choice edited state")
    if renpy.test.testexecution.urm_dynamic_save_reentered:
        jump urm_dynamic_save_probe_verify
    $ renpy.test.testexecution.urm_dynamic_save_reentered = True
    $ urm_dynamic_save_gate = 0
    $ urm_dynamic_save_route = "mutated-after-save"
    $ print("DYNAMIC_SAVE_MUTATED_AFTER_SAVE", urm_dynamic_save_gate, urm_dynamic_save_route)
    $ renpy.load("urm-dynamic-choice-edit-roundtrip")

label urm_dynamic_save_probe_verify:
    $ print("DYNAMIC_SAVE_AFTER_LOAD", urm_dynamic_save_gate, urm_dynamic_save_route, renpy.game.context().current)
    "Native save/load restored the edited Choice state."
    return

testcase urm_dynamic_condition_save_load_runtime:
    $ renpy.test.testexecution.urm_dynamic_save_reentered = False
    run Jump("urm_dynamic_save_probe_start")
    "Native save route B"
    "Save probe route B."
    type PAGEUP
    type PAGEUP
    type alt_c
    type alt_3
    type alt_c
    $ x52URM.CodeView.handleVarClicked("urm_dynamic_save_gate")
    type BACKSPACE
    type "1"
    type RETURN
    $ renpy.hide_screen("URM_CodeView")
    type alt_e
    "Save probe route C."
    "Native save/load restored the edited Choice state."
    assert urm_dynamic_save_gate == 1
    assert urm_dynamic_save_route == "C"
    assert renpy.test.testexecution.urm_dynamic_save_reentered is True
    $ renpy.quit()
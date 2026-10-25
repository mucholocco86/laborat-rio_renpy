# Two-process probe: original URM edits a dynamic Choice, native save is loaded by a fresh Ren'Py process.
default urm_dynamic_fresh_gate = 0
default urm_dynamic_fresh_route = None

label urm_dynamic_fresh_write_start:
    $ urm_dynamic_fresh_gate = 0
    $ urm_dynamic_fresh_route = None
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
        "Native fresh route A":
            $ urm_dynamic_fresh_route = "A"
        "Native fresh route B":
            $ urm_dynamic_fresh_route = "B"
        "Fresh save route C" if urm_dynamic_fresh_gate == 1:
            $ urm_dynamic_fresh_route = "C"

    $ renpy.fix_rollback()
    if urm_dynamic_fresh_route == "C":
        "Fresh save route C reached."
        jump urm_dynamic_fresh_save_point
    elif urm_dynamic_fresh_route == "B":
        "Native fresh route B reached."
    else:
        "Native fresh route A reached."

label urm_dynamic_fresh_continue:
    "Fresh process probe continuation."
    jump urm_dynamic_fresh_continue

label urm_dynamic_fresh_save_point:
    $ assert urm_dynamic_fresh_gate == 1 and urm_dynamic_fresh_route == "C"
    if renpy.session.get("urm_dynamic_fresh_load_marker", False):
        jump urm_dynamic_fresh_verify
    if renpy.can_load("urm-dynamic-choice-fresh-process"):
        $ renpy.unlink_save("urm-dynamic-choice-fresh-process")
    $ print("DYNAMIC_FRESH_BEFORE_SAVE", urm_dynamic_fresh_gate, urm_dynamic_fresh_route)
    $ renpy.save("urm-dynamic-choice-fresh-process", "Fresh-process dynamic Choice")
    if renpy.session.get("urm_dynamic_fresh_load_marker", False):
        jump urm_dynamic_fresh_verify
    $ urm_dynamic_fresh_gate = 0
    $ urm_dynamic_fresh_route = "mutated-after-save-process-1"
    $ print("DYNAMIC_FRESH_AFTER_SAVE_MUTATION", urm_dynamic_fresh_gate, urm_dynamic_fresh_route)
    $ renpy.quit()

label urm_dynamic_fresh_load_start:
    if not renpy.can_load("urm-dynamic-choice-fresh-process"):
        $ raise Exception("Fresh-process probe save slot is missing")
    $ renpy.session["urm_dynamic_fresh_load_marker"] = True
    $ print("DYNAMIC_FRESH_BEFORE_LOAD", urm_dynamic_fresh_gate, urm_dynamic_fresh_route)
    $ x52URM.Gamesaves.load("urm-dynamic-choice-fresh-process")
    "Confirm original URM save load."

label urm_dynamic_fresh_verify:
    $ print("DYNAMIC_FRESH_AFTER_LOAD", urm_dynamic_fresh_gate, urm_dynamic_fresh_route, renpy.game.context().current)
    if urm_dynamic_fresh_gate != 1 or urm_dynamic_fresh_route != "C":
        $ raise Exception("Fresh-process load did not restore the saved condition and route")
    "Fresh process restored edited Choice state."
    $ renpy.quit()

testcase urm_dynamic_condition_fresh_write:
    run Jump("urm_dynamic_fresh_write_start")
    "Native fresh route B"
    "Native fresh route B reached."
    type PAGEUP
    type PAGEUP
    type alt_c
    type alt_3
    type alt_c
    $ x52URM.CodeView.handleVarClicked("urm_dynamic_fresh_gate")
    type BACKSPACE
    type "1"
    type RETURN
    $ renpy.hide_screen("URM_CodeView")
    type alt_e
    "Fresh save route C reached."

testcase urm_dynamic_condition_fresh_load:
    $ renpy.session.pop("urm_dynamic_fresh_load_marker", None)
    run Jump("urm_dynamic_fresh_load_start")
    "Confirm original URM save load."
    type RETURN
    "Fresh process restored edited Choice state."
# Integrated probe: edit a condition variable through the original URM_modify_value screen.
default urm_dynamic_editor_gate = 0
default urm_dynamic_editor_route = None

init python:
    _urm_dynamic_editor_original_show_screen = renpy.show_screen
    def _urm_dynamic_editor_show_screen(name, *args, **kwargs):
        if name == "URM_choices":
            target = [c for c in (x52URM.Choices.currentChoices or []) if c.text == "Editor route C"]
            print("DYNAMIC_EDITOR_CHOICES", urm_dynamic_editor_gate,
                  [(c.isVisible, c._m1_choices__index) for c in target])
        elif name in ("URM_CodeView", "URM_modify_value"):
            print("DYNAMIC_EDITOR_SCREEN", name,
                  args[0].name if name == "URM_modify_value" and args else "")
        return _urm_dynamic_editor_original_show_screen(name, *args, **kwargs)
    renpy.show_screen = _urm_dynamic_editor_show_screen

label urm_dynamic_editor_probe_start:
    $ urm_dynamic_editor_gate = 0
    $ urm_dynamic_editor_route = None
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
        "Native editor route A":
            $ urm_dynamic_editor_route = "A"
        "Native editor route B":
            $ urm_dynamic_editor_route = "B"
        "Editor route C" if urm_dynamic_editor_gate == 1:
            $ urm_dynamic_editor_route = "C"

    $ renpy.fix_rollback()
    if urm_dynamic_editor_route == "A":
        "Editor probe route A."
    elif urm_dynamic_editor_route == "B":
        "Editor probe route B."
    else:
        "Editor probe route C."

label urm_dynamic_editor_probe_continue:
    "Dynamic editor probe continuation."
    jump urm_dynamic_editor_probe_continue

testcase urm_dynamic_condition_editor_rollback_runtime:
    run Jump("urm_dynamic_editor_probe_start")
    "Native editor route B"
    "Editor probe route B."
    type PAGEUP
    type PAGEUP
    type alt_c
    type alt_3
    type alt_c
    $ x52URM.CodeView.handleVarClicked("urm_dynamic_editor_gate")
    type BACKSPACE
    type "1"
    type RETURN
    $ print("DYNAMIC_EDITOR_AFTER_INPUT", urm_dynamic_editor_gate,
            renpy.get_screen("URM_modify_value"), renpy.get_screen("URM_CodeView"))
    $ renpy.hide_screen("URM_CodeView")
    type alt_e
    "Editor probe route C."
    assert urm_dynamic_editor_gate == 1
    assert urm_dynamic_editor_route == "C"
    "Dynamic editor probe continuation."
    type PAGEUP
    $ print("DYNAMIC_EDITOR_RB_1", urm_dynamic_editor_gate, urm_dynamic_editor_route, renpy.game.log.rollback_limit)
    type PAGEUP
    $ print("DYNAMIC_EDITOR_RB_2", urm_dynamic_editor_gate, urm_dynamic_editor_route, renpy.game.log.rollback_limit)
    type PAGEUP
    $ print("DYNAMIC_EDITOR_RB_3", urm_dynamic_editor_gate, urm_dynamic_editor_route, renpy.game.log.rollback_limit)
    type PAGEUP
    $ print("DYNAMIC_EDITOR_RB_4", urm_dynamic_editor_gate, urm_dynamic_editor_route, renpy.game.log.rollback_limit)
    $ target = [c for c in (x52URM.Choices.currentChoices or []) if c.text == "Editor route C"]
    $ print("DYNAMIC_EDITOR_RESULT", urm_dynamic_editor_gate, urm_dynamic_editor_route,
            [(c.isVisible, c._m1_choices__index) for c in target])
    assert urm_dynamic_editor_gate == 0
    assert urm_dynamic_editor_route is None
    assert bool(target and target[0].isVisible is False)
    $ renpy.quit()
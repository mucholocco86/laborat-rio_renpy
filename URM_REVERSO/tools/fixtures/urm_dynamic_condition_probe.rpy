# Isolated runtime probe: a condition-backed Choice changes after URM Var.setValue.
default urm_dynamic_probe_enabled = False
default urm_dynamic_probe_route = None
default urm_dynamic_probe_screen_shown = False
default urm_dynamic_probe_false_seen = False
default urm_dynamic_probe_true_seen = False
default urm_dynamic_probe_set_succeeded = False

init python:
    _urm_dynamic_probe_original_show_screen = renpy.show_screen
    def _urm_dynamic_probe_show_screen(name, *args, **kwargs):
        if name == "URM_choices":
            renpy.store.urm_dynamic_probe_screen_shown = True
            choices = x52URM.Choices.currentChoices or []
            target = [c for c in choices if c.text == "Dynamic route C"]
            renpy.store.urm_dynamic_probe_false_seen = bool(target and target[0].isVisible is False)
            print("DYNAMIC_PROBE_SCREEN", name, "enabled", renpy.store.urm_dynamic_probe_enabled,
                  "target", [(c.isVisible, c._m1_choices__index) for c in target])
        return _urm_dynamic_probe_original_show_screen(name, *args, **kwargs)
    renpy.show_screen = _urm_dynamic_probe_show_screen

label urm_dynamic_condition_probe_start:
    $ urm_dynamic_probe_route = None
    $ urm_dynamic_probe_enabled = False
    $ urm_dynamic_probe_screen_shown = False
    $ urm_dynamic_probe_false_seen = False
    $ urm_dynamic_probe_true_seen = False
    $ urm_dynamic_probe_set_succeeded = False
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
        "Native route A":
            $ urm_dynamic_probe_route = "A"
        "Native route B":
            $ urm_dynamic_probe_route = "B"
        "Dynamic route C" if urm_dynamic_probe_enabled:
            $ urm_dynamic_probe_route = "C"

    $ renpy.fix_rollback()
    if urm_dynamic_probe_route == "A":
        "Dynamic probe route A."
    elif urm_dynamic_probe_route == "B":
        "Dynamic probe route B."
    else:
        "Dynamic probe route C."

label urm_dynamic_condition_probe_continue:
    "Dynamic condition probe continuation."
    jump urm_dynamic_condition_probe_continue

testcase urm_dynamic_condition_probe_runtime:
    run Jump("urm_dynamic_condition_probe_start")
    "Native route B"
    "Dynamic probe route B."
    type PAGEUP
    type PAGEUP
    type alt_c
    $ urm_dynamic_probe_set_succeeded = x52URM.Var("urm_dynamic_probe_enabled").setValue(True)
    $ choices = x52URM.Choices.currentChoices or []
    $ target = [c for c in choices if c.text == "Dynamic route C"]
    $ urm_dynamic_probe_true_seen = bool(target and target[0].isVisible is True)
    $ print("DYNAMIC_PROBE_AFTER_EDIT", urm_dynamic_probe_set_succeeded,
            urm_dynamic_probe_enabled, [(c.isVisible, c._m1_choices__index) for c in target])
    assert urm_dynamic_probe_screen_shown is True
    assert urm_dynamic_probe_false_seen is True
    assert urm_dynamic_probe_set_succeeded is True
    assert urm_dynamic_probe_true_seen is True
    $ renpy.restart_interaction()
    type alt_3
    type RETURN
    "Dynamic probe route C."
    assert urm_dynamic_probe_route == "C"
    $ print("DYNAMIC_PROBE_RESULT", urm_dynamic_probe_enabled, urm_dynamic_probe_route)
    $ renpy.quit()

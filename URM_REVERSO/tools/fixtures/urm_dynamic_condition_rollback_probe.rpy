# Isolated follow-up: rollback the condition variable after dynamic URM Choice selection.
default urm_dynamic_rb_enabled = False
default urm_dynamic_rb_route = None
default urm_dynamic_rb_screen_shown = False
default urm_dynamic_rb_false_seen = False

init python:
    _urm_dynamic_rb_original_show_screen = renpy.show_screen
    def _urm_dynamic_rb_show_screen(name, *args, **kwargs):
        if name == "URM_choices":
            renpy.store.urm_dynamic_rb_screen_shown = True
            choices = x52URM.Choices.currentChoices or []
            target = [c for c in choices if c.text == "Dynamic rollback route C"]
            renpy.store.urm_dynamic_rb_false_seen = bool(target and target[0].isVisible is False)
            print("DYNAMIC_RB_SCREEN", renpy.store.urm_dynamic_rb_enabled,
                  [(c.isVisible, c._m1_choices__index) for c in target])
        return _urm_dynamic_rb_original_show_screen(name, *args, **kwargs)
    renpy.show_screen = _urm_dynamic_rb_show_screen

label urm_dynamic_rollback_probe_start:
    $ urm_dynamic_rb_route = None
    $ urm_dynamic_rb_enabled = False
    $ urm_dynamic_rb_screen_shown = False
    $ urm_dynamic_rb_false_seen = False
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
        "Native rollback route A":
            $ urm_dynamic_rb_route = "A"
        "Native rollback route B":
            $ urm_dynamic_rb_route = "B"
        "Dynamic rollback route C" if urm_dynamic_rb_enabled:
            $ urm_dynamic_rb_route = "C"

    $ renpy.fix_rollback()
    if urm_dynamic_rb_route == "A":
        "Dynamic rollback route A."
    elif urm_dynamic_rb_route == "B":
        "Dynamic rollback route B."
    else:
        "Dynamic rollback route C."

label urm_dynamic_rollback_probe_continue:
    "Dynamic rollback probe continuation."
    jump urm_dynamic_rollback_probe_continue

testcase urm_dynamic_condition_rollback_runtime:
    run Jump("urm_dynamic_rollback_probe_start")
    "Native rollback route B"
    "Dynamic rollback route B."
    type PAGEUP
    type PAGEUP
    type alt_c
    $ urm_dynamic_rb_set_succeeded = x52URM.Var("urm_dynamic_rb_enabled").setValue(True)
    $ choices = x52URM.Choices.currentChoices or []
    $ target = [c for c in choices if c.text == "Dynamic rollback route C"]
    assert urm_dynamic_rb_set_succeeded is True
    $ print("DYNAMIC_RB_AFTER_EDIT", urm_dynamic_rb_enabled, [(c.isVisible, c._m1_choices__index) for c in target])
    assert bool(target and target[0].isVisible is True)
    $ renpy.restart_interaction()
    type alt_3
    type RETURN
    "Dynamic rollback route C."
    "Dynamic rollback probe continuation."
    type PAGEUP
    $ print("DYNAMIC_RB_STEP_1", urm_dynamic_rb_enabled, urm_dynamic_rb_route, renpy.game.context().current, renpy.game.log.rollback_limit)
    type PAGEUP
    $ print("DYNAMIC_RB_STEP_2", urm_dynamic_rb_enabled, urm_dynamic_rb_route, renpy.game.context().current, renpy.game.log.rollback_limit)
    type PAGEUP
    $ print("DYNAMIC_RB_STEP_3", urm_dynamic_rb_enabled, urm_dynamic_rb_route, renpy.game.context().current, renpy.game.log.rollback_limit)
    type PAGEUP
    $ print("DYNAMIC_RB_STEP_4", urm_dynamic_rb_enabled, urm_dynamic_rb_route, renpy.game.context().current, renpy.game.log.rollback_limit)
    $ choices = x52URM.Choices.currentChoices or []
    $ target = [c for c in choices if c.text == "Dynamic rollback route C"]
    $ print("DYNAMIC_RB_RESULT", urm_dynamic_rb_enabled, urm_dynamic_rb_route,
            [(c.isVisible, c._m1_choices__index) for c in target])
    assert urm_dynamic_rb_enabled is False
    assert urm_dynamic_rb_route is None
    assert bool(target and target[0].isVisible is False)
    $ renpy.quit()
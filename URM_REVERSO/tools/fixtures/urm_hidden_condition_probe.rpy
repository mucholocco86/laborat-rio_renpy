# Disposable integration probe: can the original URM select a false-condition menu item?
default urm_hidden_probe_route = None
default urm_hidden_probe_screen_shown = False
default urm_hidden_probe_false_item = False

init python:
    _urm_hidden_probe_original_show_screen = renpy.show_screen
    def _urm_hidden_probe_show_screen(name, *args, **kwargs):
        if name == "URM_choices":
            renpy.store.urm_hidden_probe_screen_shown = True
            hidden = [c for c in (x52URM.Choices.currentChoices or []) if c.text == "Hidden route C"]
            renpy.store.urm_hidden_probe_false_item = bool(hidden and not hidden[0].isVisible)
            print("HIDDEN_PROBE_SCREEN", name, "fixed", renpy.game.log.rollback_is_fixed,
                  "false_item_seen", renpy.store.urm_hidden_probe_false_item,
                  "choices", [(c.text, c.isVisible, c._m1_choices__index) for c in (x52URM.Choices.currentChoices or [])])
        return _urm_hidden_probe_original_show_screen(name, *args, **kwargs)
    renpy.show_screen = _urm_hidden_probe_show_screen

    _urm_hidden_probe_original_choice_call = renpy.ui.ChoiceReturn.__call__
    def _urm_hidden_probe_choice_call(self):
        print("HIDDEN_PROBE_CHOICERETURN", "label", self.label, "value", self.value,
              "fixed", renpy.game.log.rollback_is_fixed)
        rv = _urm_hidden_probe_original_choice_call(self)
        print("HIDDEN_PROBE_CHOICERETURN_RESULT", rv)
        return rv
    renpy.ui.ChoiceReturn.__call__ = _urm_hidden_probe_choice_call

label urm_hidden_condition_probe_start:
    $ urm_hidden_probe_route = None
    $ urm_hidden_probe_screen_shown = False
    $ urm_hidden_probe_false_item = False
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
            $ urm_hidden_probe_route = "A"
        "Native route B":
            $ urm_hidden_probe_route = "B"
        "Hidden route C" if False:
            $ urm_hidden_probe_route = "C"

    $ renpy.fix_rollback()
    if urm_hidden_probe_route == "A":
        "Hidden probe route A."
    elif urm_hidden_probe_route == "B":
        "Hidden probe route B."
    else:
        "Hidden probe route C."

label urm_hidden_condition_probe_continue:
    "Hidden condition probe continuation."
    jump urm_hidden_condition_probe_continue

testcase urm_hidden_condition_probe_runtime:
    run Jump("urm_hidden_condition_probe_start")
    "Native route B"
    "Hidden probe route B."
    type PAGEUP
    type PAGEUP
    type alt_c
    type alt_3
    type RETURN
    "Hidden probe route C."
    "Hidden condition probe continuation."
    assert urm_hidden_probe_route == "C"
    assert urm_hidden_probe_screen_shown is True
    assert urm_hidden_probe_false_item is True
    $ print("HIDDEN_PROBE_RESULT", urm_hidden_probe_route,
            renpy.game.context().current, renpy.game.log.rollback_is_fixed)
    $ renpy.quit()

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

    _urm_hidden_probe_original_rollback = renpy.python.RollbackLog.rollback
    def _urm_hidden_probe_trace_rollback(self, checkpoints, force=False, label=None,
                                         greedy=True, on_load=False, abnormal=True,
                                         current_label=None):
        print("HIDDEN_POST_ROLLBACK_BEGIN", checkpoints, force,
              "route", renpy.store.urm_hidden_probe_route,
              "fixed", self.rollback_is_fixed, "limit", self.rollback_limit,
              "boundary", self.fixed_rollback_boundary,
              "current", renpy.game.context().current,
              "forward", self.forward_info())
        try:
            return _urm_hidden_probe_original_rollback(
                self, checkpoints, force=force, label=label, greedy=greedy,
                on_load=on_load, abnormal=abnormal, current_label=current_label)
        finally:
            print("HIDDEN_POST_ROLLBACK_END",
                  "route", renpy.store.urm_hidden_probe_route,
                  "fixed", self.rollback_is_fixed, "limit", self.rollback_limit,
                  "boundary", self.fixed_rollback_boundary,
                  "current", renpy.game.context().current,
                  "forward", self.forward_info())

    renpy.python.RollbackLog.rollback = _urm_hidden_probe_trace_rollback

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
    $ renpy.rollback(checkpoints=1, label="urm_hidden_probe_after_rollback")
    jump urm_hidden_condition_probe_continue

label urm_hidden_probe_after_rollback:
    $ print("HIDDEN_POST_ROLLBACK_RESULT_1", urm_hidden_probe_route,
            renpy.game.context().current, renpy.game.log.rollback_is_fixed,
            renpy.can_rollback(), renpy.roll_forward_info())
    $ renpy.rollback(checkpoints=1)

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
    assert urm_hidden_probe_route == "C"
    assert urm_hidden_probe_screen_shown is True
    assert urm_hidden_probe_false_item is True
    type RETURN
    "Hidden condition probe continuation."
    type RETURN
    assert urm_hidden_probe_route is None
    assert renpy.in_fixed_rollback() is True
    assert renpy.can_rollback() is True
    $ print("HIDDEN_POST_ROLLBACK_TESTCASE", urm_hidden_probe_route,
            renpy.game.context().current, renpy.game.log.rollback_is_fixed,
            renpy.can_rollback(), renpy.roll_forward_info())
    $ renpy.quit()

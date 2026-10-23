# Full original URM package probe, staged unchanged in a disposable Ren'Py 7.4.11 game.
# Exercises the real overlay notification, URM_choices screen and URMChoice.Action.

default urm_real_loader_probe_route = None

init python:
    def urm_real_loader_probe_dump(tag):
        log = renpy.game.log
        print("REAL_URM_BOUNDARY", tag,
              "route", renpy.store.urm_real_loader_probe_route,
              "limit", log.rollback_limit,
              "can", renpy.can_rollback(),
              "fixed", log.rollback_is_fixed,
              "forward", log.forward_info(),
              "current", renpy.game.context().current,
              "context_rollback", renpy.game.context().rollback,
              "store_rollback", renpy.store._rollback)

    _urm_real_loader_probe_original_rollback = renpy.python.RollbackLog.rollback
    _urm_real_loader_probe_original_choice_return = renpy.ui.ChoiceReturn.__call__

    def _urm_real_loader_probe_trace_choice_return(self):
        print("REAL_URM_CHOICERETURN", "fixed_before",
              renpy.game.log.rollback_is_fixed, "label", self.label,
              "index", self.index)
        rv = _urm_real_loader_probe_original_choice_return(self)
        print("REAL_URM_CHOICERETURN_RESULT", rv,
              "fixed_after", renpy.game.log.rollback_is_fixed)
        return rv

    renpy.ui.ChoiceReturn.__call__ = _urm_real_loader_probe_trace_choice_return

    def _urm_real_loader_probe_trace_rollback(self, checkpoints, force=False, label=None,
                                             greedy=True, on_load=False, abnormal=True,
                                             current_label=None):
        print("REAL_URM_ROLLBACK_BEGIN", checkpoints, force, self.rollback_is_fixed,
              renpy.game.context().current, self.fixed_rollback_boundary,
              self.forward_info())
        try:
            return _urm_real_loader_probe_original_rollback(
                self, checkpoints, force=force, label=label, greedy=greedy,
                on_load=on_load, abnormal=abnormal, current_label=current_label)
        finally:
            print("REAL_URM_ROLLBACK_END", self.rollback_is_fixed,
                  renpy.game.context().current, self.fixed_rollback_boundary,
                  self.forward_info())

    renpy.python.RollbackLog.rollback = _urm_real_loader_probe_trace_rollback

label urm_real_loader_choices_boundary_start:
    $ urm_real_loader_probe_route = None
    $ renpy.config.fix_rollback_without_choice = False

    # Keep rollback enabled in the isolated test context; the subsequent menu,
    # fix_rollback, and PAGEUP events use the SDK's real rollback implementation.
    $ renpy.game.context().rollback = True
    $ renpy.store._rollback = True

    # Configure the original URM instance before installing its real overlay.
    $ x52URM.Settings.seenWelcome = 2
    $ x52URM.Settings.warningDisabled = True
    $ x52URM.Settings.autoUpdateCheck = False
    $ x52URM.Settings.lastLoadedFile = None
    $ x52URM.Settings.showChoicesNotification = True
    $ x52URM.Settings.showWatchPanel = False
    $ x52URM.States.updateNotificationShown = True
    $ x52URM.afterLoad()

    $ print("REAL_URM_READY", x52URM.version,
            "choice_api", x52URM.Choices.isDisplayingChoice,
            "fixed", renpy.in_fixed_rollback(), "can", renpy.can_rollback())

    menu:
        "Native route A":
            $ urm_real_loader_probe_route = "A"
        "Native route B":
            $ urm_real_loader_probe_route = "B"

    $ renpy.fix_rollback()
    $ urm_real_loader_probe_dump("AFTER_FIX")

    if urm_real_loader_probe_route == "A":
        "Fixed boundary probe route A."
    else:
        "Fixed boundary probe route B."

label urm_real_loader_choices_boundary_continue:
    "Full URM loader continuation checkpoint."
    jump urm_real_loader_choices_boundary_continue

testcase urm_real_loader_choices_boundary_runtime:
    run Jump("urm_real_loader_choices_boundary_start")
    "Native route B"
    "Fixed boundary probe route B."
    type PAGEUP
    type PAGEUP
    type alt_c
    type alt_1
    type RETURN
    "Fixed boundary probe route A."
    "Full URM loader continuation checkpoint."
    $ urm_real_loader_probe_dump("AFTER_URM_SELECTION")
    assert urm_real_loader_probe_route == "A"
    assert renpy.in_fixed_rollback() is False
    $ renpy.quit()

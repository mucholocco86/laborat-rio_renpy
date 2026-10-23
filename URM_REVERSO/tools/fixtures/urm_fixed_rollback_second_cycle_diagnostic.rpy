# Isolated real-boundary fixed rollback probe (Ren'Py 7.4.11).
# This fixture invokes renpy.fix_rollback() after a native menu selection,
# then uses PAGEUP to roll back across that decision and tries the URM action.

default urm_second_cycle_probe_route = None
default urm_second_cycle_probe_context_before = None
default urm_second_cycle_probe_fixed_before_urm = None
default urm_second_cycle_probe_forward_before_urm = None
default urm_second_cycle_probe_fixed_after_urm = None
default urm_second_cycle_probe_boundary_before_urm = None
default urm_second_cycle_probe_boundary_after_fix = None
default urm_second_cycle_probe_native_a_sensitive = None
default urm_second_cycle_probe_native_b_sensitive = None
default urm_second_cycle_probe_trace_enabled = False

init python:
    def urm_second_cycle_probe_dump(tag):
        log = renpy.game.log
        print("SECOND_CYCLE_STATE", tag, "limit", log.rollback_limit,
              "can", renpy.can_rollback(), "context_rollback", renpy.game.context().rollback,
              "store_rollback", renpy.store._rollback, "fixed", log.rollback_is_fixed,
              "forward", log.forward_info(), "loglen", len(log.log),
              "boundary", log.fixed_rollback_boundary,
              "current", renpy.game.context().current)

    _urm_second_cycle_original_fix = renpy.python.RollbackLog.fix_rollback
    def _urm_second_cycle_trace_fix(self):
        urm_second_cycle_probe_dump("FIX_BEFORE")
        rv = _urm_second_cycle_original_fix(self)
        urm_second_cycle_probe_dump("FIX_AFTER")
        return rv
    renpy.python.RollbackLog.fix_rollback = _urm_second_cycle_trace_fix

    _urm_second_cycle_original_checkpoint = renpy.python.RollbackLog.checkpoint
    def _urm_second_cycle_trace_checkpoint(self, data=None, keep_rollback=False, hard=True):
        rv = _urm_second_cycle_original_checkpoint(self, data=data, keep_rollback=keep_rollback, hard=hard)
        urm_second_cycle_probe_dump("CHECKPOINT")
        return rv
    renpy.python.RollbackLog.checkpoint = _urm_second_cycle_trace_checkpoint

    def urm_second_cycle_probe_select(label, index):
        renpy.store.urm_second_cycle_probe_fixed_before_urm = renpy.game.log.rollback_is_fixed
        renpy.store.urm_second_cycle_probe_forward_before_urm = renpy.roll_forward_info()
        renpy.store.urm_second_cycle_probe_boundary_before_urm = renpy.game.log.fixed_rollback_boundary
        renpy.store.urm_second_cycle_probe_native_a_sensitive = renpy.ui.ChoiceReturn("Route A", 0).get_sensitive()
        renpy.store.urm_second_cycle_probe_native_b_sensitive = renpy.ui.ChoiceReturn("Route B", 1).get_sensitive()
        renpy.game.log.rollback_is_fixed = False
        rv = renpy.ui.ChoiceReturn(label, index)()
        renpy.store.urm_second_cycle_probe_fixed_after_urm = renpy.game.log.rollback_is_fixed
        renpy.session["urm_second_cycle_probe_action_records"].append(
            (label, index, renpy.store.urm_second_cycle_probe_fixed_before_urm,
             renpy.store.urm_second_cycle_probe_forward_before_urm,
             renpy.store.urm_second_cycle_probe_native_a_sensitive,
             renpy.store.urm_second_cycle_probe_native_b_sensitive, rv,
             renpy.store.urm_second_cycle_probe_fixed_after_urm,
             renpy.store.urm_second_cycle_probe_boundary_before_urm))
        print("BOUNDARY_URM_ACTION", renpy.store.urm_second_cycle_probe_fixed_before_urm,
              renpy.store.urm_second_cycle_probe_forward_before_urm,
              renpy.store.urm_second_cycle_probe_native_a_sensitive,
              renpy.store.urm_second_cycle_probe_native_b_sensitive,
              renpy.store.urm_second_cycle_probe_boundary_before_urm,
              rv, renpy.store.urm_second_cycle_probe_fixed_after_urm)
        return rv

    _urm_boundary_original_rollback = renpy.python.RollbackLog.rollback

    def _urm_boundary_trace_rollback(self, checkpoints, force=False, label=None,
                                     greedy=True, on_load=False, abnormal=True,
                                     current_label=None):
        traced = renpy.session.get("urm_second_cycle_probe_trace_enabled", False)
        if traced:
            print("BOUNDARY_ROLLBACK_BEGIN", checkpoints, force, self.rollback_is_fixed,
                  renpy.game.context().current, self.fixed_rollback_boundary,
                  self.forward_info())
        try:
            return _urm_boundary_original_rollback(
                self, checkpoints, force=force, label=label, greedy=greedy,
                on_load=on_load, abnormal=abnormal, current_label=current_label)
        finally:
            if traced:
                print("BOUNDARY_ROLLBACK_END", self.rollback_is_fixed,
                      renpy.game.context().current, self.fixed_rollback_boundary,
                      self.forward_info())

    renpy.python.RollbackLog.rollback = _urm_boundary_trace_rollback

screen urm_second_cycle_probe_overlay():
    modal renpy.in_fixed_rollback()
    zorder 300

    if renpy.in_fixed_rollback():
        frame:
            xalign 0.5
            yalign 0.5

            vbox:
                spacing 12
                text "Real fixed rollback boundary probe"
                textbutton "URM route A":
                    action [
                        Hide("urm_second_cycle_probe_overlay"),
                        Function(urm_second_cycle_probe_select, "Route A", 0, _update_screens=False),
                    ]
                textbutton "URM route B":
                    action [
                        Hide("urm_second_cycle_probe_overlay"),
                        Function(urm_second_cycle_probe_select, "Route B", 1, _update_screens=False),
                    ]

label urm_fixed_rollback_second_cycle_start:
    $ urm_second_cycle_probe_route = None
    $ urm_second_cycle_probe_trace_enabled = True
    $ renpy.session["urm_second_cycle_probe_trace_enabled"] = True
    $ renpy.session["urm_second_cycle_probe_route_executed"] = []
    $ renpy.session["urm_second_cycle_probe_action_records"] = []
    $ urm_second_cycle_probe_fixed_before_urm = None
    $ urm_second_cycle_probe_forward_before_urm = None
    $ urm_second_cycle_probe_fixed_after_urm = None
    $ urm_second_cycle_probe_boundary_before_urm = None
    $ urm_second_cycle_probe_boundary_after_fix = None
    $ urm_second_cycle_probe_context_before = renpy.game.context().rollback
    $ renpy.game.context().rollback = True
    $ renpy.store._rollback = True
    $ renpy.config.fix_rollback_without_choice = False

    $ print("BOUNDARY_BEFORE_MENU", renpy.in_fixed_rollback(), renpy.roll_forward_info(),
            renpy.game.context().current, renpy.game.log.fixed_rollback_boundary)
    show screen urm_second_cycle_probe_overlay

    menu:
        "Native route A":
            $ urm_second_cycle_probe_route = "A"
            $ renpy.session["urm_second_cycle_probe_route_executed"].append("A")

        "Native route B":
            $ urm_second_cycle_probe_route = "B"
            $ renpy.session["urm_second_cycle_probe_route_executed"].append("B")

    $ renpy.fix_rollback()
    $ urm_second_cycle_probe_boundary_after_fix = renpy.game.log.fixed_rollback_boundary
    $ print("BOUNDARY_AFTER_MENU", urm_second_cycle_probe_route, renpy.in_fixed_rollback(),
            renpy.roll_forward_info(), urm_second_cycle_probe_boundary_after_fix)
    $ urm_second_cycle_probe_dump("AFTER_MENU")

    if urm_second_cycle_probe_route == "A":
        "Fixed boundary probe route A."
    else:
        "Fixed boundary probe route B."

label urm_fixed_rollback_second_cycle_done:
    "Second-cycle continuation checkpoint."
    jump urm_fixed_rollback_second_cycle_done


testcase urm_fixed_rollback_second_cycle_diagnostic:
    run Jump("urm_fixed_rollback_second_cycle_start")
    "Native route B"
    "Fixed boundary probe route B."
    type PAGEUP
    type PAGEUP
    "URM route A"
    "Fixed boundary probe route A."
    type RETURN
    "Second-cycle continuation checkpoint."
    $ urm_second_cycle_probe_dump("BEFORE_SECOND_PAGEUPS")
    type PAGEUP
    type PAGEUP
    $ urm_second_cycle_probe_dump("AFTER_SECOND_PAGEUPS")
    type PAGEUP
    $ urm_second_cycle_probe_dump("AFTER_THIRD_PAGEUP")
    $ renpy.quit()
    $ renpy.quit()

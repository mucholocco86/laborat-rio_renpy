# Isolated real-boundary fixed rollback probe (Ren'Py 7.4.11).
# This fixture invokes renpy.fix_rollback() after a native menu selection,
# then uses PAGEUP to roll back across that decision and tries the URM action.

default urm_boundary_probe_route = None
default urm_boundary_probe_context_before = None
default urm_boundary_probe_fixed_before_urm = None
default urm_boundary_probe_forward_before_urm = None
default urm_boundary_probe_fixed_after_urm = None
default urm_boundary_probe_boundary_before_urm = None
default urm_boundary_probe_boundary_after_fix = None
default urm_boundary_probe_native_a_sensitive = None
default urm_boundary_probe_native_b_sensitive = None
default urm_boundary_probe_trace_enabled = False

init python:
    def urm_boundary_probe_select(label, index):
        renpy.store.urm_boundary_probe_fixed_before_urm = renpy.game.log.rollback_is_fixed
        renpy.store.urm_boundary_probe_forward_before_urm = renpy.roll_forward_info()
        renpy.store.urm_boundary_probe_boundary_before_urm = renpy.game.log.fixed_rollback_boundary
        renpy.store.urm_boundary_probe_native_a_sensitive = renpy.ui.ChoiceReturn("Route A", 0).get_sensitive()
        renpy.store.urm_boundary_probe_native_b_sensitive = renpy.ui.ChoiceReturn("Route B", 1).get_sensitive()
        renpy.game.log.rollback_is_fixed = False
        rv = renpy.ui.ChoiceReturn(label, index)()
        renpy.store.urm_boundary_probe_fixed_after_urm = renpy.game.log.rollback_is_fixed
        print("BOUNDARY_URM_ACTION", renpy.store.urm_boundary_probe_fixed_before_urm,
              renpy.store.urm_boundary_probe_forward_before_urm,
              renpy.store.urm_boundary_probe_native_a_sensitive,
              renpy.store.urm_boundary_probe_native_b_sensitive,
              renpy.store.urm_boundary_probe_boundary_before_urm,
              rv, renpy.store.urm_boundary_probe_fixed_after_urm)
        return rv

    _urm_boundary_original_rollback = renpy.python.RollbackLog.rollback

    def _urm_boundary_trace_rollback(self, checkpoints, force=False, label=None,
                                     greedy=True, on_load=False, abnormal=True,
                                     current_label=None):
        traced = renpy.store.urm_boundary_probe_trace_enabled
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

screen urm_boundary_probe_overlay():
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
                        Hide("urm_boundary_probe_overlay"),
                        Function(urm_boundary_probe_select, "Route A", 0, _update_screens=False),
                    ]

label urm_fixed_rollback_boundary_start:
    $ urm_boundary_probe_route = None
    $ urm_boundary_probe_trace_enabled = True
    $ urm_boundary_probe_fixed_before_urm = None
    $ urm_boundary_probe_forward_before_urm = None
    $ urm_boundary_probe_fixed_after_urm = None
    $ urm_boundary_probe_boundary_before_urm = None
    $ urm_boundary_probe_boundary_after_fix = None
    $ urm_boundary_probe_context_before = renpy.game.context().rollback
    $ renpy.game.context().rollback = True
    $ renpy.store._rollback = True
    $ renpy.config.fix_rollback_without_choice = False

    $ print("BOUNDARY_BEFORE_MENU", renpy.in_fixed_rollback(), renpy.roll_forward_info(),
            renpy.game.context().current, renpy.game.log.fixed_rollback_boundary)
    show screen urm_boundary_probe_overlay

    menu:
        "Native route A":
            $ urm_boundary_probe_route = "A"

        "Native route B":
            $ urm_boundary_probe_route = "B"

    $ renpy.fix_rollback()
    $ urm_boundary_probe_boundary_after_fix = renpy.game.log.fixed_rollback_boundary
    $ print("BOUNDARY_AFTER_MENU", urm_boundary_probe_route, renpy.in_fixed_rollback(),
            renpy.roll_forward_info(), urm_boundary_probe_boundary_after_fix)

    if urm_boundary_probe_route == "A":
        "Fixed boundary probe route A."
    else:
        "Fixed boundary probe route B."

label urm_fixed_rollback_boundary_done:
    return


testcase urm_fixed_rollback_real_boundary_urm_override:
    run Jump("urm_fixed_rollback_boundary_start")
    "Native route B"
    "Fixed boundary probe route B."
    type PAGEUP
    type PAGEUP
    "URM route A"
    "Fixed boundary probe route A."
    label urm_fixed_rollback_boundary_done
    assert urm_boundary_probe_boundary_after_fix is not None
    assert urm_boundary_probe_route == "A"
    assert urm_boundary_probe_fixed_before_urm is True
    assert urm_boundary_probe_forward_before_urm == 1
    assert urm_boundary_probe_fixed_after_urm is False
    assert urm_boundary_probe_native_a_sensitive is False
    assert urm_boundary_probe_native_b_sensitive is True
    $ renpy.quit()

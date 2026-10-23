# Full original URM variable editor probe, staged unchanged in a disposable Ren'Py 7.4.11 game.
# It opens Choices -> CodeView -> URM_modify_value, edits an int, and reads it in the selected branch.

default urm_edit_probe_value = 1
default urm_edit_probe_route_value = None
default urm_edit_probe_modify_seen = False
default urm_edit_probe_code_seen = False

init python:
    _urm_edit_probe_original_show_screen = renpy.show_screen

    def _urm_edit_probe_trace_show_screen(name, *args, **kwargs):
        if name == "URM_CodeView":
            renpy.store.urm_edit_probe_code_seen = True
            print("URM_EDIT_CODEVIEW_SHOWN", "fixed", renpy.game.log.rollback_is_fixed,
                  "current", renpy.game.context().current)
        elif name == "URM_modify_value":
            renpy.store.urm_edit_probe_modify_seen = True
            var = args[0] if args else kwargs.get("var")
            print("URM_EDIT_MODIFY_SCREEN_SHOWN", getattr(var, "name", None),
                  "value", getattr(var, "value", None),
                  "fixed", renpy.game.log.rollback_is_fixed,
                  "current", renpy.game.context().current)
        return _urm_edit_probe_original_show_screen(name, *args, **kwargs)

    renpy.show_screen = _urm_edit_probe_trace_show_screen

    _urm_edit_probe_original_rollback = renpy.python.RollbackLog.rollback

    def _urm_edit_probe_trace_rollback(self, checkpoints, force=False, label=None,
                                       greedy=True, on_load=False, abnormal=True,
                                       current_label=None):
        print("URM_EDIT_ROLLBACK_BEGIN", checkpoints, force,
              "fixed", self.rollback_is_fixed,
              "value", renpy.store.urm_edit_probe_value,
              "current", renpy.game.context().current,
              "boundary", self.fixed_rollback_boundary,
              "forward", self.forward_info())
        try:
            return _urm_edit_probe_original_rollback(
                self, checkpoints, force=force, label=label, greedy=greedy,
                on_load=on_load, abnormal=abnormal, current_label=current_label)
        finally:
            print("URM_EDIT_ROLLBACK_END",
                  "fixed", self.rollback_is_fixed,
                  "value", renpy.store.urm_edit_probe_value,
                  "current", renpy.game.context().current,
                  "boundary", self.fixed_rollback_boundary,
                  "forward", self.forward_info())

label urm_real_loader_variable_edit_start:
    $ urm_edit_probe_value = 1
    $ urm_edit_probe_route_value = None
    $ urm_edit_probe_modify_seen = False
    $ urm_edit_probe_code_seen = False
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

    $ _urm_edit_probe_original_set_value = x52URM.Var.setValue
    $ _urm_edit_probe_original_handle_change = x52URM.StoreMonitor.handleVarChange

    python:
        _urm_edit_probe_original_set_value = x52URM.Var.setValue
        _urm_edit_probe_original_handle_change = x52URM.StoreMonitor.handleVarChange

        def _urm_edit_probe_trace_set_value(self, newValue=None, *args, **kwargs):
            oldValue = self.value
            rv = _urm_edit_probe_original_set_value(self, newValue, *args, **kwargs)
            print("URM_EDIT_VAR_SET", self.name, "old", oldValue,
                  "new", self.value, "result", rv,
                  "fixed", renpy.game.log.rollback_is_fixed,
                  "limit", renpy.game.log.rollback_limit,
                  "force_checkpoint", renpy.game.context().force_checkpoint)
            return rv

        def _urm_edit_probe_trace_handle_change(self, varName, oldValue, newValue):
            if varName == "urm_edit_probe_value":
                print("URM_EDIT_MONITOR_HANDLE", varName, oldValue, newValue,
                      "fixed", renpy.game.log.rollback_is_fixed,
                      "limit", renpy.game.log.rollback_limit,
                      "current", renpy.game.context().current)
            return _urm_edit_probe_original_handle_change(self, varName, oldValue, newValue)

        x52URM.Var.setValue = _urm_edit_probe_trace_set_value
        x52URM.StoreMonitor.handleVarChange = _urm_edit_probe_trace_handle_change

    menu:
        "Native route A":
            $ urm_edit_probe_route_value = urm_edit_probe_value
        "Native route B":
            $ urm_edit_probe_route_value = urm_edit_probe_value

    $ renpy.fix_rollback()
    $ print("URM_EDIT_AFTER_FIX", urm_edit_probe_route_value,
            urm_edit_probe_value, renpy.in_fixed_rollback(),
            renpy.can_rollback(), renpy.game.log.fixed_rollback_boundary)

    if urm_edit_probe_route_value == urm_edit_probe_value:
        "Edit probe route reached."
    else:
        "Edit probe route mismatch."

label urm_real_loader_variable_edit_continue:
    "URM variable edit continuation checkpoint."
    jump urm_real_loader_variable_edit_continue

testcase urm_real_loader_variable_edit_runtime:
    run Jump("urm_real_loader_variable_edit_start")
    "Native route B"
    "Edit probe route reached."
    type PAGEUP
    type PAGEUP
    type alt_c
    type alt_1
    type alt_s
    $ x52URM.CodeView.handleVarClicked("urm_edit_probe_value")
    type BACKSPACE
    type "7"
    type RETURN
    type ESCAPE
    type alt_e
    "Edit probe route reached."
    "URM variable edit continuation checkpoint."
    assert urm_edit_probe_value == 7
    assert urm_edit_probe_route_value == 7
    assert urm_edit_probe_code_seen is True
    assert urm_edit_probe_modify_seen is True
    $ print("URM_EDIT_RUNTIME_RESULT", urm_edit_probe_value,
            urm_edit_probe_route_value, renpy.in_fixed_rollback(),
            renpy.can_rollback())
    $ renpy.quit()

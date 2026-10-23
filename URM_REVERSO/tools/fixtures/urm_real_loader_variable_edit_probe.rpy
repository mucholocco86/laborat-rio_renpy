# Full original URM variable editor probe, staged unchanged in a disposable Ren'Py 7.4.11 game.
default urm_edit_probe_trace_enabled = True
# It opens Choices -> CodeView -> URM_modify_value, edits an int, and reads it in the selected branch.

default urm_edit_probe_value = 1
default urm_edit_probe_route_value = None
default urm_edit_probe_modify_seen = False
default urm_edit_probe_monitor_called = False
default urm_edit_probe_force_trace_enabled = False
default urm_edit_probe_code_seen = False

init python:
    # Diagnostic only: trace writes to Context.force_checkpoint in this disposable fixture.
    _urm_edit_probe_context_class = renpy.execution.Context
    _urm_edit_probe_original_context_setattr = _urm_edit_probe_context_class.__setattr__

    def _urm_edit_probe_trace_context_setattr(self, name, value):
        if name == "force_checkpoint" and getattr(renpy.store, "urm_edit_probe_force_trace_enabled", False):
            import sys
            frame = sys._getframe(1)
            caller_chain = []
            for _urm_edit_force_depth in range(6):
                if frame is None:
                    break
                caller_chain.append((frame.f_code.co_name, frame.f_code.co_filename, frame.f_lineno))
                frame = frame.f_back
            try:
                old_value = getattr(self, "force_checkpoint")
            except Exception:
                old_value = "<unset>"
            print("URM_EDIT_CONTEXT_FORCE_WRITE", old_value, value,
                  "context_current", getattr(self, "current", None),
                  "active_current", renpy.game.context().current,
                  "log_force", renpy.game.log.force_checkpoint,
                  "stack", caller_chain)
        return _urm_edit_probe_original_context_setattr(self, name, value)

    _urm_edit_probe_context_class.__setattr__ = _urm_edit_probe_trace_context_setattr

    _urm_edit_probe_original_begin = renpy.python.RollbackLog.begin
    def _urm_edit_probe_trace_begin(self, force=False):
        tracing = getattr(renpy.store, "urm_edit_probe_force_trace_enabled", False)
        if tracing:
            print("URM_EDIT_BEGIN_START", force,
                  "context_force", renpy.game.context().force_checkpoint,
                  "log_force", self.force_checkpoint,
                  "current", renpy.game.context().current)
        try:
            return _urm_edit_probe_original_begin(self, force=force)
        finally:
            if tracing:
                print("URM_EDIT_BEGIN_END", force,
                      "context_force", renpy.game.context().force_checkpoint,
                      "log_force", self.force_checkpoint,
                      "current", renpy.game.context().current)

    renpy.python.RollbackLog.begin = _urm_edit_probe_trace_begin

    _urm_edit_probe_original_show_screen = renpy.show_screen

    def _urm_edit_probe_trace_show_screen(name, *args, **kwargs):
        if name == "URM_CodeView":
            renpy.store.urm_edit_probe_code_seen = True
            print("URM_EDIT_CODEVIEW_SHOWN", "fixed", renpy.game.log.rollback_is_fixed,
                  "current", renpy.game.context().current)
        elif name == "URM_modify_value":
            renpy.store.urm_edit_probe_modify_seen = True
            var = args[0] if args else kwargs.get("var")
            prior_values = []
            for rb in renpy.game.log.log:
                changes = rb.stores.get("store", {})
                if "urm_edit_probe_value" in changes:
                    prior_values.append((rb.context.current, changes["urm_edit_probe_value"]))
            current_changes = renpy.game.log.current.stores.get("store", {})
            if "urm_edit_probe_value" in current_changes:
                prior_values.append(("current", current_changes["urm_edit_probe_value"]))
            print("URM_EDIT_PRE_EDIT_RECORD_VALUES", prior_values)
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

    # Install the diagnostic wrapper; previously it was defined but never assigned.
    renpy.python.RollbackLog.rollback = _urm_edit_probe_trace_rollback

    _urm_edit_probe_original_complete = renpy.python.RollbackLog.complete
    def _urm_edit_probe_trace_complete(self, begin=False):
        tracing = getattr(renpy.store, "urm_edit_probe_trace_enabled", False)
        if tracing:
            before_store = self.current.stores.get("store", {}) if self.current is not None else {}
            before_old = renpy.store.__dict__.old.as_dict().get("urm_edit_probe_value", "<missing>")
            print("URM_EDIT_COMPLETE_BEGIN", begin,
                  "log_force", self.force_checkpoint,
                  "context_force", renpy.game.context().force_checkpoint,
                  "did_interaction", self.did_interaction,
                  "current", renpy.game.context().current,
                  "record_id", id(self.current),
                  "stores_id", id(before_store),
                  "target_pre", before_store.get("urm_edit_probe_value", "<missing>"),
                  "store_old", before_old)
        try:
            return _urm_edit_probe_original_complete(self, begin)
        finally:
            if tracing:
                current_changes = self.current.stores.get("store", {})
                has_target = "urm_edit_probe_value" in current_changes
                print("URM_EDIT_COMPLETE_END", begin,
                      "log_force", self.force_checkpoint,
                      "context_force", renpy.game.context().force_checkpoint,
                      "did_interaction", self.did_interaction,
                      "target_in_record", has_target,
                      "record_old", current_changes.get("urm_edit_probe_value"),
                      "record_id", id(self.current),
                      "stores_id", id(current_changes),
                      "record_repr", repr(current_changes),
                      "current", renpy.game.context().current)

    renpy.python.RollbackLog.complete = _urm_edit_probe_trace_complete

    _urm_edit_probe_original_get_changes = renpy.python.StoreDict.get_changes
    def _urm_edit_probe_trace_get_changes(self, cycle, *args, **kwargs):
        result = _urm_edit_probe_original_get_changes(self, cycle, *args, **kwargs)
        tracing = (self is renpy.store.__dict__ and
                   getattr(renpy.store, "urm_edit_probe_trace_enabled", False))
        if tracing:
            import sys
            frame = sys._getframe(1)
            caller_chain = []
            for _urm_edit_frame_depth in range(5):
                if frame is None:
                    break
                caller_chain.append((frame.f_code.co_name, frame.f_code.co_filename, frame.f_lineno))
                frame = frame.f_back
            caller = caller_chain[0][0] if caller_chain else None
            changes = result[0] if isinstance(result, tuple) else result
            try:
                has_target = "urm_edit_probe_value" in changes
            except Exception:
                has_target = False
            old_value = changes.get("urm_edit_probe_value") if has_target else None
            target_in_store = "urm_edit_probe_value" in self
            print("URM_EDIT_STORE_CHANGES", cycle, "has_target", has_target,
                  "old", old_value, "target_in_store", target_in_store,
                  "is_main_store", self is renpy.store.__dict__,
                  "store_id", id(self), "main_store_id", id(renpy.store.__dict__),
                  "result_type", type(result), "delta_type", type(changes),
                  "dict_binding", repr(dict), "dict_binding_type", type(dict),
                  "direct_has_target", has_target, "caller", caller,
                  "caller_chain", caller_chain,
                  "modify_screen_open", bool(renpy.get_screen("URM_modify_value")),
                  "delta_id", id(changes), "delta_repr", repr(changes),
                  "current", renpy.store.urm_edit_probe_value,
                  "context_force", renpy.game.context().force_checkpoint,
                  "log_force", renpy.game.log.force_checkpoint,
                  "node", renpy.game.context().current)
        return result

    renpy.python.StoreDict.get_changes = _urm_edit_probe_trace_get_changes

    _urm_edit_probe_original_store_begin = renpy.python.StoreDict.begin
    def _urm_edit_probe_trace_store_begin(self):
        tracing = (self is renpy.store.__dict__ and
                   getattr(renpy.store, "urm_edit_probe_trace_enabled", False))
        if tracing:
            before = self.old.as_dict().get("urm_edit_probe_value", "<missing>")
            print("URM_EDIT_STORE_BEGIN_BEFORE", before,
                  "current", renpy.store.urm_edit_probe_value,
                  "node", renpy.game.context().current)
        rv = _urm_edit_probe_original_store_begin(self)
        if tracing:
            after = self.old.as_dict().get("urm_edit_probe_value", "<missing>")
            print("URM_EDIT_STORE_BEGIN_AFTER", after,
                  "current", renpy.store.urm_edit_probe_value,
                  "node", renpy.game.context().current)
        return rv

    renpy.python.StoreDict.begin = _urm_edit_probe_trace_store_begin

    _urm_edit_probe_original_rollback_record = renpy.python.Rollback.rollback
    def _urm_edit_probe_trace_rollback_record(self):
        tracing = getattr(renpy.store, "urm_edit_probe_trace_enabled", False)
        target_values = []
        if tracing:
            for store_name, changes in self.stores.items():
                if "urm_edit_probe_value" in changes:
                    target_values.append((store_name, changes["urm_edit_probe_value"]))
            print("URM_EDIT_RECORD_ROLLBACK_BEGIN", target_values,
                  "current", renpy.store.urm_edit_probe_value,
                  "record_context", self.context.current)
        try:
            return _urm_edit_probe_original_rollback_record(self)
        finally:
            if tracing:
                print("URM_EDIT_RECORD_ROLLBACK_END", target_values,
                      "current", renpy.store.urm_edit_probe_value,
                      "record_context", renpy.game.context().current)

    renpy.python.Rollback.rollback = _urm_edit_probe_trace_rollback_record

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
    $ urm_edit_probe_force_trace_enabled = True
    $ x52URM.afterLoad()
    $ x52URM.VarsStore.monitor("urm_edit_probe_value")
    $ print("URM_EDIT_MONITOR_CONFIG", x52URM.VarsStore.isMonitored("urm_edit_probe_value"))
    $ _urm_edit_probe_original_notification_add = x52URM.Notifications.add

    python:
        _urm_edit_probe_original_notification_add = x52URM.Notifications.add

        def _urm_edit_probe_trace_notification_add(self, **kwargs):
            if kwargs.get("text") == "urm_edit_probe_value":
                renpy.store.urm_edit_probe_monitor_called = True
                print("URM_EDIT_NOTIFICATION", kwargs)
            return _urm_edit_probe_original_notification_add(self, **kwargs)

        x52URM.Notifications.add = _urm_edit_probe_trace_notification_add

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

        def _urm_edit_probe_trace_handle_change(varName, oldValue, newValue):
            if varName == "urm_edit_probe_value":
                print("URM_EDIT_MONITOR_HANDLE", varName, oldValue, newValue,
                      "fixed", renpy.game.log.rollback_is_fixed,
                      "limit", renpy.game.log.rollback_limit,
                      "current", renpy.game.context().current)
            return _urm_edit_probe_original_handle_change(varName, oldValue, newValue)

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
    $ renpy.hide_screen('URM_CodeView')
    type alt_e
    "Edit probe route reached."
    "URM variable edit continuation checkpoint."
    assert urm_edit_probe_value == 7
    assert urm_edit_probe_route_value == 7
    assert urm_edit_probe_code_seen is True
    assert urm_edit_probe_modify_seen is True
    assert x52URM.VarsStore.isMonitored("urm_edit_probe_value") is True
    assert urm_edit_probe_monitor_called is False
    $ print("URM_EDIT_RUNTIME_RESULT", urm_edit_probe_value,
            urm_edit_probe_route_value, renpy.in_fixed_rollback(),
            renpy.can_rollback())
    type PAGEUP
    $ print("URM_EDIT_AFTER_PAGEUP_1", urm_edit_probe_value,
            urm_edit_probe_route_value, renpy.in_fixed_rollback(),
            renpy.can_rollback(), renpy.game.log.rollback_limit,
            renpy.game.context().current, renpy.game.log.forward_info())
    type PAGEUP
    $ print("URM_EDIT_AFTER_PAGEUP_2", urm_edit_probe_value,
            urm_edit_probe_route_value, renpy.in_fixed_rollback(),
            renpy.can_rollback(), renpy.game.log.rollback_limit,
            renpy.game.context().current, renpy.game.log.forward_info())
    type PAGEUP
    $ print("URM_EDIT_AFTER_PAGEUP_3", urm_edit_probe_value,
            urm_edit_probe_route_value, renpy.in_fixed_rollback(),
            renpy.can_rollback(), renpy.game.log.rollback_limit,
            renpy.game.context().current, renpy.game.log.forward_info())
    type PAGEUP
    $ print("URM_EDIT_AFTER_PAGEUP_4", urm_edit_probe_value,
            urm_edit_probe_route_value, renpy.in_fixed_rollback(),
            renpy.can_rollback(), renpy.game.log.rollback_limit,
            renpy.game.context().current, renpy.game.log.forward_info())
    $ print("URM_EDIT_AFTER_ROLLBACK_SWEEP", urm_edit_probe_value,
            urm_edit_probe_route_value, renpy.in_fixed_rollback(),
            renpy.can_rollback(), renpy.game.log.rollback_limit,
            renpy.game.context().current, renpy.game.log.fixed_rollback_boundary)
    assert urm_edit_probe_value == 1
    assert urm_edit_probe_route_value is None
    $ renpy.quit()

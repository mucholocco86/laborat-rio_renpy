init 9999 python in JK:
    _constant = True

    def _m1_after_load_callback__after_load_callback():
        Autosaver.prevent_autosaving = False
        
        if(Autosaver.active_slot_pending != None):
            Autosaver.suppress_autosave_confirm = False
            Autosaver.set_active_slot(Autosaver.active_slot_pending)
            Autosaver.active_slot_pending = None
            
            if Settings.offsetSlotAfterManualSaveIsLoaded:
                Autosaver.set_next_slot()
        
        Autosaver.after_load_save_position_pending = True

    if hasattr(renpy.config, "after_load_callbacks"):
        renpy.config.after_load_callbacks.append(_m1_after_load_callback__after_load_callback)
    else:
        # Ren'Py 6.99 has no after_load_callbacks list. Its successful load
        # exits RollbackLog.unfreeze by raising a context-restart exception.
        _m1_legacy_original_unfreeze = renpy.python.RollbackLog.unfreeze

        def _m1_legacy_unfreeze_with_callbacks(self, roots, label=None):
            try:
                return _m1_legacy_original_unfreeze(self, roots, label)
            except (renpy.game.RestartTopContext, renpy.game.RestartContext):
                _m1_after_load_callback__after_load_callback()
                raise

        renpy.python.RollbackLog.unfreeze = _m1_legacy_unfreeze_with_callbacks
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

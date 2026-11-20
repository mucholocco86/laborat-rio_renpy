init 9999 python in JK:
    _constant = True

    def _m1_loadsave__before_load(slotname):
        Autosaver.active_slot_pending = slotname
        Autosaver.prevent_confirm_on_large_page_jump = True
        Autosaver.suppress_autosave_confirm = False

    def _m1_loadsave__before_save(slotname):

        if AutosaverClass.PendingSaveClass.temp_save_slotname in slotname:
            return

        if Settings.offsetSlotAfterManualSave:
            Autosaver.set_active_slot(slotname)

            if not Utils.is_displaying_choices_in_any_context():
                Autosaver.set_next_slot()

    def _m1_loadsave__unwrap_jk_wrapper(func):
        # Only remove wrappers installed by this JK module. Other mods may
        # legitimately use an attribute named "_original" for their own hooks.
        while getattr(func, "_jk_loadsave_wrapper", False):
            func = func._jk_loadsave_original

        return func

    def _m1_loadsave__load_partial(func, *args, **kwargs):
        func = _m1_loadsave__unwrap_jk_wrapper(func)

        def new_funct(*new_args, **new_kwargs):
            new_kwargs.update(kwargs.copy())

            if new_args and new_args[0]:
                _m1_loadsave__before_load(new_args[0])

            Memories.memoryInProgress = False

            return func(*(args + new_args), **new_kwargs)

        new_funct._jk_loadsave_wrapper = True
        new_funct._jk_loadsave_original = func

        return new_funct

    def _m1_loadsave__save_partial(func, *args, **kwargs):
        func = _m1_loadsave__unwrap_jk_wrapper(func)

        def new_funct(*new_args, **new_kwargs):
            new_kwargs.update(kwargs.copy())

            if new_args and new_args[0]:
                _m1_loadsave__before_save(new_args[0])

            return func(*(args + new_args), **new_kwargs)

        new_funct._jk_loadsave_wrapper = True
        new_funct._jk_loadsave_original = func

        return new_funct


    renpy.load = _m1_loadsave__load_partial(renpy.load)
    renpy.save = _m1_loadsave__save_partial(renpy.save)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

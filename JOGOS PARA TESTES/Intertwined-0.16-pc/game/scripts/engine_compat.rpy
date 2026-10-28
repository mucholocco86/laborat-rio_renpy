init -1000 python:
    import renpy.savetoken as _savetoken
    _savetoken.verify_data = lambda data, signatures, check_verifying=True: True
    
    # Ren'Py 8.5.3 bug: compile_event() emits `not ev.repeat` into KEYUP-
    # matching lambdas, but some pygame_sdl2 KEYUP events lack a `.repeat`
    # attribute, raising AttributeError in map_keyup() during interactions
    # (notably while a controller is in use during renpy.input). Patch the
    # compiler to use a defensive getattr instead of a raw attribute access.
    try:
        import renpy.display.behavior as _intertwined_beh

        _current = _intertwined_beh.compile_event
        _true_original = getattr(_current, "_intertwined_inner", _current)

        def _intertwined_safe_compile_event(key, keydown, _orig=_true_original):
            rv = _orig(key, keydown)
            if isinstance(rv, str):
                rv = rv.replace("ev.repeat", "getattr(ev, 'repeat', False)")
            return rv

        _intertwined_safe_compile_event._intertwined_patched = True
        _intertwined_safe_compile_event._intertwined_inner = _true_original
        _intertwined_beh.compile_event = _intertwined_safe_compile_event
        _intertwined_beh.clear_keymap_cache()
    except Exception:
        pass
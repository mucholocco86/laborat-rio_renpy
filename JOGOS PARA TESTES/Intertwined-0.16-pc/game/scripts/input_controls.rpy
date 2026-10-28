init python:
    _last_input_source = "kbm"
    _LAST_INPUT_AXIS_DEADZONE = 8000
    _LAST_INPUT_MOUSE_PIXELS = 4

    # Debug flag: when True, input source is locked to keyboard/mouse
    _FORCE_DISABLE_CONTROLLER = False

    def is_controller_active():
        if _FORCE_DISABLE_CONTROLLER:
            return False
        return _last_input_source == "controller"

    def _has_real_controller():
        try:
            import renpy.display.controller as _rdc
            return bool(getattr(_rdc, "controllers", None))
        except Exception:
            return False

    def _observe_input_event(ev):
        global _last_input_source
        if getattr(store, "_FORCE_DISABLE_CONTROLLER", False):
            return
        try:
            import pygame_sdl2 as _p
        except Exception:
            return

        new_source = None
        t = ev.type

        if t == _p.KEYDOWN or t == _p.MOUSEBUTTONDOWN:
            new_source = "kbm"
        elif t == _p.MOUSEMOTION:
            rel = getattr(ev, "rel", (0, 0))
            if abs(rel[0]) + abs(rel[1]) >= _LAST_INPUT_MOUSE_PIXELS:
                new_source = "kbm"
        elif t in (
                getattr(_p, "CONTROLLERBUTTONDOWN", -1),
                _p.JOYBUTTONDOWN,
                _p.JOYHATMOTION,
            ):
            new_source = "controller"
        elif t in (
                getattr(_p, "CONTROLLERAXISMOTION", -1),
                _p.JOYAXISMOTION,
            ):
            if abs(getattr(ev, "value", 0)) >= _LAST_INPUT_AXIS_DEADZONE:
                new_source = "controller"
        elif t == getattr(_p, "CONTROLLERDEVICEREMOVED", -1):
            if not _has_real_controller():
                new_source = "kbm"

        if new_source and new_source != _last_input_source:
            _last_input_source = new_source
            try:
                osk_reconcile()
            except Exception:
                pass

    def _intertwined_install_input_observer():
        try:
            import renpy.display.controller as _rdc
            if getattr(_rdc.event, "_intertwined_wrapped", False):
                return
            _orig_event = _rdc.event

            def _wrapped(ev):
                if getattr(store, "_FORCE_DISABLE_CONTROLLER", False) and _is_controller_event(ev):
                    return None
                try:
                    _observe_input_event(ev)
                except NameError:
                    pass
                return _orig_event(ev)

            _wrapped._intertwined_wrapped = True
            _rdc.event = _wrapped
        except Exception:
            pass

    _CONTROLLER_EVENT_TYPES = None

    def _is_controller_event(ev):
        global _CONTROLLER_EVENT_TYPES
        try:
            import pygame_sdl2 as _p
        except Exception:
            return False
        if _CONTROLLER_EVENT_TYPES is None:
            names = (
                "CONTROLLERBUTTONDOWN", "CONTROLLERBUTTONUP",
                "CONTROLLERAXISMOTION",
                "CONTROLLERDEVICEADDED", "CONTROLLERDEVICEREMOVED",
                "CONTROLLERDEVICEREMAPPED",
                "JOYBUTTONDOWN", "JOYBUTTONUP", "JOYAXISMOTION",
                "JOYHATMOTION", "JOYBALLMOTION",
                "JOYDEVICEADDED", "JOYDEVICEREMOVED",
            )
            _CONTROLLER_EVENT_TYPES = frozenset(
                getattr(_p, n) for n in names if hasattr(_p, n)
            )
        return ev.type in _CONTROLLER_EVENT_TYPES

    def _intertwined_unbind_help_f1_key():
        """Unbind the F1 key from the help menu."""
        try:
            keys = list(config.keymap.get("help", []))
            filtered = [k for k in keys if k not in ("f1", "K_F1")]
            config.keymap["help"] = filtered
        except Exception:
            pass

    def _intertwined_unbind_default_hide_windows_keys():
        """Remove default hide-interface bindings that conflict with HUD cycling."""
        try:
            keys = list(config.keymap.get("hide_windows", []))
            filtered = [k for k in keys if k not in ("h", "K_h", "mousedown_2", "mouseup_2")]
            config.keymap["hide_windows"] = filtered
        except Exception:
            pass

    _intertwined_install_input_observer()
    _intertwined_unbind_help_f1_key()
    _intertwined_unbind_default_hide_windows_keys()

    if getattr(store, "_FORCE_DISABLE_CONTROLLER", False):
        try:
            import renpy.display.controller as _rdc_off
            _rdc_off.ignore = True
        except Exception:
            pass
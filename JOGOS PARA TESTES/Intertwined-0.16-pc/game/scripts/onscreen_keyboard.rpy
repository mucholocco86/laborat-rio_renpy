init python:
    _OSK_KNOWN_INPUTS = (
        ("input", "input"),
        ("sf_save_browser", "save_input"),
        ("player_name_screen", "name_input"),
    )

    def _find_editable_input():
        from renpy.display.behavior import Input, inputs as _registered

        for screen_name, widget_id in _OSK_KNOWN_INPUTS:
            try:
                w = renpy.get_widget(screen_name, widget_id)
            except Exception:
                w = None
            if isinstance(w, Input) and getattr(w, "editable", False):
                return w

        for inp in _registered:
            if getattr(inp, "editable", False):
                return inp

        try:
            sl = renpy.display.interface.scene_lists
        except Exception:
            return None

        seen = set()

        def walk(d):
            if d is None or id(d) in seen:
                return None
            seen.add(id(d))
            if isinstance(d, Input) and getattr(d, "editable", False):
                return d
            try:
                children = d.visit() or ()
            except Exception:
                children = ()
            for c in children:
                r = walk(c)
                if r is not None:
                    return r
            return None

        try:
            for layer_name in list(sl.layers.keys()):
                for entry in sl.layers[layer_name]:
                    d = getattr(entry, "displayable", None)
                    r = walk(d)
                    if r is not None:
                        return r
        except Exception:
            pass
        return None

    def _mutate_input(new_content, new_caret):
        inp = _find_editable_input()
        if inp is None:
            return
        inp.caret_pos = max(0, min(new_caret, len(new_content)))
        inp.update_text(new_content, inp.editable)
        try:
            import renpy.display.render as _r
            _r.redraw(inp, 0)
        except Exception:
            pass
        renpy.restart_interaction()

    def osk_append(ch):
        inp = _find_editable_input()
        if inp is None:
            return
        pos = inp.caret_pos
        content = inp.content[:pos] + ch + inp.content[pos:]
        _mutate_input(content, pos + len(ch))

    def osk_backspace():
        inp = _find_editable_input()
        if inp is None or inp.caret_pos == 0:
            return
        pos = inp.caret_pos
        content = inp.content[:pos - 1] + inp.content[pos:]
        _mutate_input(content, pos - 1)

    def osk_done():
        inp = _find_editable_input()
        renpy.hide_screen("onscreen_keyboard")
        try:
            renpy.set_editable_input_value(None, False)
        except Exception:
            pass
        renpy.restart_interaction()

        if inp is None:
            return None

        if inp.value is not None:
            try:
                return inp.value.enter()
            except Exception:
                return None
        else:
            return inp.content

    def osk_visible():
        try:
            return renpy.get_screen("onscreen_keyboard") is not None
        except Exception:
            return False

    def osk_reconcile():
        want = (
            is_controller_active()
            and _find_editable_input() is not None
        )
        have = osk_visible()
        if want and not have:
            renpy.show_screen("onscreen_keyboard")
            renpy.restart_interaction()
        elif have and not want:
            renpy.hide_screen("onscreen_keyboard")
            renpy.restart_interaction()

    def show_osk_if_controller():
        osk_reconcile()

    def osk_force_show():
        if is_controller_active():
            if not osk_visible():
                renpy.show_screen("onscreen_keyboard")
                renpy.restart_interaction()

    def osk_force_hide():
        if osk_visible():
            renpy.hide_screen("onscreen_keyboard")
            renpy.restart_interaction()

    def osk_activate_for(iv, variable_name=None):
        ev = iv.Enable()
        if ev is not None:
            renpy.run(ev)
        osk_reconcile()
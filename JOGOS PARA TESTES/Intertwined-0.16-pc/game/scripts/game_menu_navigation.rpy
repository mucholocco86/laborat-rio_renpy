init python:

    if not hasattr(store, "_intertwined_last_pause_screen"):
        store._intertwined_last_pause_screen = "save"
    if not hasattr(store, "_intertwined_last_pause_context"):
        store._intertwined_last_pause_context = None

    _INTERTWINED_PAUSE_SCREENS = frozenset({
        "save",
        "load",
        "preferences",
        "girls_gallery",
        "replay_menu",
    })

    def intertwined_set_pause_screen(name):
        try:
            if isinstance(name, str) and name in _INTERTWINED_PAUSE_SCREENS:
                store._intertwined_last_pause_screen = name
        except Exception:
            pass

    def intertwined_get_pause_screen():
        try:
            name = getattr(store, "_intertwined_last_pause_screen", "save")
            if isinstance(name, str) and name in _INTERTWINED_PAUSE_SCREENS:
                return name
        except Exception:
            pass
        return "save"

    def intertwined_pause_context_key():
        try:
            cur = renpy.game.context().current
            if isinstance(cur, str):
                return ("label", cur)
            if isinstance(cur, tuple) and cur:
                return ("file", str(cur[0]))
        except Exception:
            pass
        try:
            fn, _ln = renpy.get_filename_line()
            fn = (fn or "").replace("\\", "/")
            return ("file", fn)
        except Exception:
            return None

    def _intertwined_pause_menu():
        if store._in_replay:
            renpy.call_in_new_context("_game_menu", _game_menu_screen="replay_menu")
        else:
            key = intertwined_pause_context_key()
            last_key = getattr(store, "_intertwined_last_pause_context", None)
            if key != last_key:
                store._intertwined_last_pause_screen = "save"
                store._intertwined_last_pause_context = key
            renpy.call_in_new_context("_game_menu", _game_menu_screen=intertwined_get_pause_screen())

    config.game_menu_action = _intertwined_pause_menu
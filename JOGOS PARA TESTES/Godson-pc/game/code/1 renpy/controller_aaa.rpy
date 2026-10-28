init offset = 180


default -180 godson_frontend_nav_focus = "new_game"
default -180 godson_ingame_nav_focus = "resume"
default -180 godson_preferences_tab = "visuals"
default -180 godson_controls_tab = "gamepad"
default -180 persistent.godson_keyboard_bindings = { }
default -180 persistent.godson_gamepad_bindings = { }


init -5 python:




    config.keymap["godson_tab_left"] = [ "K_q" ]
    config.keymap["godson_tab_right"] = [ "K_e" ]

    for old_action in ("rollback",):
        while old_action in config.pad_bindings.setdefault("pad_leftshoulder_press", [ ]):
            config.pad_bindings["pad_leftshoulder_press"].remove(old_action)
        while old_action in config.pad_bindings.setdefault("repeat_pad_leftshoulder_press", [ ]):
            config.pad_bindings["repeat_pad_leftshoulder_press"].remove(old_action)

    for old_action in ("rollforward",):
        while old_action in config.pad_bindings.setdefault("pad_rightshoulder_press", [ ]):
            config.pad_bindings["pad_rightshoulder_press"].remove(old_action)
        while old_action in config.pad_bindings.setdefault("repeat_pad_rightshoulder_press", [ ]):
            config.pad_bindings["repeat_pad_rightshoulder_press"].remove(old_action)

    if "godson_tab_left" not in config.pad_bindings.setdefault("pad_leftshoulder_press", [ ]):
        config.pad_bindings["pad_leftshoulder_press"].append("godson_tab_left")
    if "godson_tab_right" not in config.pad_bindings.setdefault("pad_rightshoulder_press", [ ]):
        config.pad_bindings["pad_rightshoulder_press"].append("godson_tab_right")

    GODSON_CONTROL_ROWS = (
    ("dismiss", _("Confirm / Advance"), _("Select a menu item or advance dialogue.")),
    ("game_menu", _("Menu / Back"), _("Open the system menu or return from the current screen.")),
    ("rollback", _("Rollback"), _("Return to an earlier interaction.")),
    ("rollforward", _("Roll Forward"), _("Move forward after rolling back.")),
    ("skip", _("Hold to Skip"), _("Skip dialogue while the control is held.")),
    ("toggle_skip", _("Toggle Skip"), _("Turn skipping on or off.")),
    ("hide_windows", _("Hide Interface"), _("Temporarily hide dialogue and interface elements.")),
    ("screenshot", _("Screenshot"), _("Save a screenshot of the current screen.")),
    ("focus_up", _("Navigate Up"), _("Move focus upward through menus and choices.")),
    ("focus_down", _("Navigate Down"), _("Move focus downward through menus and choices.")),
    ("focus_left", _("Navigate Left"), _("Move focus left through menus and controls.")),
    ("focus_right", _("Navigate Right"), _("Move focus right through menus and controls.")),
    ("godson_tab_left", _("Previous Tab"), _("Switch to the previous Options or Controls tab.")),
    ("godson_tab_right", _("Next Tab"), _("Switch to the next Options or Controls tab.")),
)

    GODSON_KEYBOARD_CHOICES = (
    ("K_RETURN", _("Enter")),
    ("K_SPACE", _("Space")),
    ("K_ESCAPE", _("Escape")),
    ("K_TAB", _("Tab")),
    ("K_UP", _("Up Arrow")),
    ("K_DOWN", _("Down Arrow")),
    ("K_LEFT", _("Left Arrow")),
    ("K_RIGHT", _("Right Arrow")),
    ("K_w", _("W")),
    ("K_a", _("A")),
    ("K_s", _("S")),
    ("K_d", _("D")),
    ("K_q", _("Q")),
    ("K_e", _("E")),
    ("K_PAGEUP", _("Page Up")),
    ("K_PAGEDOWN", _("Page Down")),
    ("K_HOME", _("Home")),
    ("K_END", _("End")),
    ("K_LCTRL", _("Left Ctrl")),
    ("K_RCTRL", _("Right Ctrl")),
    ("K_LSHIFT", _("Left Shift")),
    ("K_RSHIFT", _("Right Shift")),
    ("K_h", _("H")),
    ("K_F12", _("F12")),
)

    GODSON_GAMEPAD_CHOICES = (
    ("pad_a_press", _("A / Cross")),
    ("pad_b_press", _("B / Circle")),
    ("pad_x_press", _("X / Square")),
    ("pad_y_press", _("Y / Triangle")),
    ("pad_leftshoulder_press", _("LB / L1")),
    ("pad_rightshoulder_press", _("RB / R1")),
    ("pad_lefttrigger_pos", _("LT / L2")),
    ("pad_righttrigger_pos", _("RT / R2")),
    ("pad_leftstick_press", _("Left Stick Click")),
    ("pad_rightstick_press", _("Right Stick Click")),
    ("pad_back_press", _("View / Select")),
    ("pad_start_press", _("Menu / Start")),
    ("pad_guide_press", _("Guide")),
    ("pad_dpup_press", _("D-Pad Up")),
    ("pad_dpdown_press", _("D-Pad Down")),
    ("pad_dpleft_press", _("D-Pad Left")),
    ("pad_dpright_press", _("D-Pad Right")),
)

    GODSON_MOUSE_ROWS = (
    (_("Left Click"), _("Advance dialogue and activate the highlighted interface item.")),
    (_("Right Click"), _("Open the system menu or return from the current screen.")),
    (_("Middle Click"), _("Hide the dialogue and interface.")),
    (_("Wheel Up"), _("Rollback to an earlier interaction.")),
    (_("Wheel Down"), _("Roll forward after rolling back.")),
)





    GODSON_ACTION_GROUPS = {
    "dismiss": ("dismiss", "button_select", "bar_activate", "bar_deactivate"),
    "game_menu": ("game_menu",),
    "rollback": ("rollback",),
    "rollforward": ("rollforward",),
    "skip": ("skip",),
    "toggle_skip": ("toggle_skip",),
    "hide_windows": ("hide_windows",),
    "screenshot": ("screenshot",),
    "focus_up": ("focus_up", "bar_up", "viewport_uparrow"),
    "focus_down": ("focus_down", "bar_down", "viewport_downarrow"),
    "focus_left": ("focus_left", "bar_left", "viewport_leftarrow"),
    "focus_right": ("focus_right", "bar_right", "viewport_rightarrow"),
    "godson_tab_left": ("godson_tab_left",),
    "godson_tab_right": ("godson_tab_right",),
}

    GODSON_REPEAT_ACTIONS = frozenset((
    "rollback", "rollforward",
    "focus_up", "focus_down", "focus_left", "focus_right",
    "bar_up", "bar_down", "bar_left", "bar_right",
    "viewport_uparrow", "viewport_downarrow", "viewport_leftarrow", "viewport_rightarrow",
))

    GODSON_KEYBOARD_PREFIXES = (
    "anyrepeat_", "repeat_", "noshift_", "shift_", "anymod_",
    "ctrl_", "alt_", "meta_", "osctrl_",
)

    def godson_action_targets(action_name):
        return GODSON_ACTION_GROUPS.get(action_name, (action_name,))

    def godson_base_event(event):
        event = str(event)
        if event.startswith("repeat_pad_"):
            return event[7:]
        
        changed = True
        while changed:
            changed = False
            for prefix in GODSON_KEYBOARD_PREFIXES:
                if event.startswith(prefix):
                    event = event[len(prefix):]
                    changed = True
                    break
        return event

    def godson_is_keyboard_event(event):
        event = godson_base_event(event)
        return event.startswith("K_") or event.startswith("KP_")

    def godson_is_gamepad_event(event):
        return godson_base_event(event).startswith("pad_")

    def godson_event_matches_device(event, device):
        if device == "keyboard":
            return godson_is_keyboard_event(event)
        if device == "gamepad":
            return godson_is_gamepad_event(event)
        return False

    def godson_device_events(action_name, device):
        primary_action = godson_action_targets(action_name)[0]
        answer = [ ]
        
        if device == "keyboard":
            for event in config.keymap.get(primary_action, [ ]):
                if godson_is_keyboard_event(event):
                    base = godson_base_event(event)
                    if base not in answer:
                        answer.append(base)
        
        elif device == "gamepad":
            for event, actions in config.pad_bindings.items():
                if primary_action in actions:
                    base = godson_base_event(event)
                    if base.startswith("pad_") and base not in answer:
                        answer.append(base)
        
        return answer



    GODSON_DEFAULT_KEYMAP = {
    target: tuple(config.keymap.get(target, [ ]))
    for action_name, _title, _description in GODSON_CONTROL_ROWS
    for target in godson_action_targets(action_name)
}
    GODSON_DEFAULT_PAD_BINDINGS = {
    event: tuple(actions)
    for event, actions in config.pad_bindings.items()
}

    def godson_saved_bindings(device):
        attribute = "godson_keyboard_bindings" if device == "keyboard" else "godson_gamepad_bindings"
        saved = getattr(persistent, attribute, None)
        if not isinstance(saved, dict):
            saved = { }
            setattr(persistent, attribute, saved)
        return saved

    def godson_keyboard_event_for_target(event, target):
        if target in GODSON_REPEAT_ACTIONS:
            return "anyrepeat_" + event
        return event

    def godson_remove_keyboard_group(action_name):
        for target in godson_action_targets(action_name):
            config.keymap[target] = [
            event for event in config.keymap.get(target, [ ])
            if not godson_is_keyboard_event(event)
        ]

    def godson_add_keyboard_group(action_name, event):
        for target in godson_action_targets(action_name):
            config.keymap.setdefault(target, [ ]).append(
            godson_keyboard_event_for_target(event, target)
        )

    def godson_remove_pad_targets(targets, only_event=None):
        only_event = godson_base_event(only_event) if only_event else None
        for physical_event in list(config.pad_bindings.keys()):
            if only_event and godson_base_event(physical_event) != only_event:
                continue
            config.pad_bindings[physical_event] = [
            action for action in config.pad_bindings.get(physical_event, [ ])
            if action not in targets
        ]

    def godson_add_gamepad_group(action_name, event):
        base_event = godson_base_event(event)
        targets = godson_action_targets(action_name)
        base_actions = config.pad_bindings.setdefault(base_event, [ ])
        
        for target in targets:
            if target not in base_actions:
                base_actions.append(target)
        
        repeat_targets = [ target for target in targets if target in GODSON_REPEAT_ACTIONS ]
        if repeat_targets:
            repeat_actions = config.pad_bindings.setdefault("repeat_" + base_event, [ ])
            for target in repeat_targets:
                if target not in repeat_actions:
                    repeat_actions.append(target)

    def godson_set_binding(device, action_name, event, remember=True, close_picker=True, restart=True):
        saved = godson_saved_bindings(device)
        event = godson_base_event(event) if event else ""
        
        if event:
            
            
            
            for other_action, _title, _description in GODSON_CONTROL_ROWS:
                if other_action == action_name:
                    continue
                if event in godson_device_events(other_action, device):
                    if device == "keyboard":
                        for target in godson_action_targets(other_action):
                            config.keymap[target] = [
                            old_event for old_event in config.keymap.get(target, [ ])
                            if godson_base_event(old_event) != event
                        ]
                    else:
                        godson_remove_pad_targets(godson_action_targets(other_action), event)
                    if remember:
                        saved[other_action] = ""
        
        if device == "keyboard":
            godson_remove_keyboard_group(action_name)
            if event:
                godson_add_keyboard_group(action_name, event)
        else:
            godson_remove_pad_targets(godson_action_targets(action_name))
            if event:
                godson_add_gamepad_group(action_name, event)
        
        if remember:
            saved[action_name] = event
            renpy.save_persistent()
        
        renpy.clear_keymap_cache()
        if close_picker:
            renpy.hide_screen("godson_binding_picker")
        if restart:
            renpy.restart_interaction()

    def godson_apply_saved_bindings():
        for device in ("keyboard", "gamepad"):
            saved = godson_saved_bindings(device)
            for action_name, event in saved.items():
                if action_name not in GODSON_ACTION_GROUPS:
                    continue
                godson_set_binding(
                device,
                action_name,
                event,
                remember=False,
                close_picker=False,
                restart=False,
            )

    def godson_binding_label(event, device):
        if not event:
            return _("UNBOUND")
        choices = GODSON_KEYBOARD_CHOICES if device == "keyboard" else GODSON_GAMEPAD_CHOICES
        for candidate, label in choices:
            if candidate == godson_base_event(event):
                return label
        return godson_base_event(event).replace("K_", "").replace("pad_", "").replace("_press", "").replace("_pos", "").replace("_", " ").title()

    def godson_current_binding(action_name, device):
        events = godson_device_events(action_name, device)
        if not events:
            return _("UNBOUND")
        labels = [ godson_binding_label(event, device) for event in events[:2] ]
        return " / ".join(labels)

    def godson_binding_is_current(action_name, device, event):
        return godson_base_event(event) in godson_device_events(action_name, device)

    def godson_assign_binding(device, action_name, event):
        godson_set_binding(device, action_name, event)

    def godson_unbind_control(device, action_name):
        godson_set_binding(device, action_name, "")

    def godson_reset_bindings(device):
        saved = godson_saved_bindings(device)
        saved.clear()
        
        all_targets = set(
        target
        for action_name, _title, _description in GODSON_CONTROL_ROWS
        for target in godson_action_targets(action_name)
    )
        
        if device == "keyboard":
            for target in all_targets:
                preserved = [
                event for event in config.keymap.get(target, [ ])
                if not godson_is_keyboard_event(event)
            ]
                defaults = [
                event for event in GODSON_DEFAULT_KEYMAP.get(target, ( ))
                if godson_is_keyboard_event(event)
            ]
                config.keymap[target] = preserved + defaults
        else:
            godson_remove_pad_targets(all_targets)
            for physical_event, actions in GODSON_DEFAULT_PAD_BINDINGS.items():
                restored = [ action for action in actions if action in all_targets ]
                if restored:
                    destination = config.pad_bindings.setdefault(physical_event, [ ])
                    for action in restored:
                        if action not in destination:
                            destination.append(action)
        
        renpy.clear_keymap_cache()
        renpy.save_persistent()
        renpy.restart_interaction()

    def godson_first_sensitive_choice(items):
        for index, item in enumerate(items):
            action = getattr(item, "action", None)
            if action is not None and action.get_sensitive():
                return index
        return 0

    def godson_cycle_preferences_tab(direction):
        tabs = ("visuals", "text", "audio")
        current = getattr(store, "godson_preferences_tab", "visuals")
        if current not in tabs:
            current = "visuals"
        store.godson_preferences_tab = tabs[(tabs.index(current) + direction) % len(tabs)]
        renpy.restart_interaction()

    def godson_cycle_controls_tab(direction):
        tabs = ("gamepad", "keyboard", "mouse")
        current = getattr(store, "godson_controls_tab", "gamepad")
        if current not in tabs:
            current = "gamepad"
        store.godson_controls_tab = tabs[(tabs.index(current) + direction) % len(tabs)]
        renpy.restart_interaction()

    godson_apply_saved_bindings()
    renpy.clear_keymap_cache()


init screen controls():
    tag menu

    key "godson_tab_left" action Function(godson_cycle_controls_tab, -1)
    key "godson_tab_right" action Function(godson_cycle_controls_tab, 1)

    use game_menu(_("CONTROLS"), scroll="viewport"):
        vbox:
            spacing 30
            xfill True

            hbox:
                spacing 18

                textbutton _("GAMEPAD"):
                    style "ui_preferences_tab"
                    selected godson_controls_tab == "gamepad"
                    action SetVariable("godson_controls_tab", "gamepad")
                    default_focus godson_controls_tab == "gamepad"
                    at ui_button_motion

                textbutton _("KEYBOARD"):
                    style "ui_preferences_tab"
                    selected godson_controls_tab == "keyboard"
                    action SetVariable("godson_controls_tab", "keyboard")
                    default_focus godson_controls_tab == "keyboard"
                    at ui_button_motion

                textbutton _("MOUSE"):
                    style "ui_preferences_tab"
                    selected godson_controls_tab == "mouse"
                    action SetVariable("godson_controls_tab", "mouse")
                    default_focus godson_controls_tab == "mouse"
                    at ui_button_motion

            text _("LB / RB  SWITCH TABS"):
                style "ui_preferences_description"
                xalign 1.0
                color "#E7C764"

            if godson_controls_tab == "gamepad":
                use godson_control_device_panel("gamepad", _("CONTROLLER LAYOUT"), _("D-pad or sticks navigate, A / Cross selects, B / Circle returns, and LB / RB changes tabs."))





            elif godson_controls_tab == "keyboard":
                use godson_control_device_panel("keyboard", _("KEYBOARD LAYOUT"), _("Choose a command, select a new key, and the change takes effect immediately."))





            else:
                frame:
                    style "godson_controls_panel"
                    xfill True

                    has vbox
                    spacing 22

                    text _("MOUSE REFERENCE") style "godson_controls_heading"
                    text _("Mouse bindings are intentionally read-only so the essential point-and-click controls always remain available.") style "godson_controls_copy"

                    for mouse_title, mouse_description in GODSON_MOUSE_ROWS:
                        frame:
                            style "godson_controls_readonly_row"
                            xfill True

                            has hbox
                            spacing 34
                            xfill True

                            text mouse_title style "godson_controls_action_text" xsize 430
                            text mouse_description style "godson_controls_description_text" xsize 1850


init screen godson_control_device_panel(device, heading, copy_text):
    frame:
        style "godson_controls_panel"
        xfill True

        has vbox
        spacing 20

        hbox:
            xfill True

            vbox:
                spacing 6
                text heading style "godson_controls_heading"
                text copy_text style "godson_controls_copy"

            null width 40

            textbutton _("RESET DEFAULTS"):
                style "godson_controls_reset_button"
                action Confirm(
                        _("Reset all [device] controls to the Ren'Py defaults?"),
                        Function(godson_reset_bindings, device),
                    )
                at ui_button_motion

        null height 4

        for action_name, action_title, action_description in GODSON_CONTROL_ROWS:
            button:
                style "godson_controls_binding_row"
                action Show("godson_binding_picker", device=device, action_name=action_name, action_title=action_title)
                at ui_button_motion

                has hbox
                spacing 32
                xfill True

                vbox:
                    spacing 3
                    xsize 1780

                    text action_title style "godson_controls_action_text"
                    text action_description style "godson_controls_description_text"

                frame:
                    style "godson_controls_binding_badge"

                    text godson_current_binding(action_name, device):
                        style "godson_controls_binding_text"
                        xalign 0.5
                        yalign 0.5


init screen godson_binding_picker(device, action_name, action_title):
    modal True
    zorder 500

    add Solid("#030202E8")

    key "game_menu" action Hide("godson_binding_picker")

    frame:
        style "godson_binding_picker_frame"
        xalign 0.5
        yalign 0.5

        has vbox
        spacing 26
        xfill True

        text _("REMAP [action_title]") style "godson_binding_picker_title" xalign 0.5
        text _("Choose one control. If it is already assigned elsewhere, Godson will move it here so a single press never triggers two commands."):
            style "godson_binding_picker_copy"
            xalign 0.5
            text_align 0.5

        frame:
            style "godson_binding_picker_current"
            xalign 0.5

            text _("CURRENT: {}").format(godson_current_binding(action_name, device)):
                style "godson_controls_binding_text"
                xalign 0.5

        viewport:
            xfill True
            ysize 820
            mousewheel True
            draggable True
            scrollbars "vertical"

            has vpgrid
            cols 3
            spacing 18
            xfill True

            for event, event_label in (GODSON_KEYBOARD_CHOICES if device == "keyboard" else GODSON_GAMEPAD_CHOICES):
                textbutton event_label:
                    style "godson_binding_choice_button"
                    selected godson_binding_is_current(action_name, device, event)
                    default_focus godson_binding_is_current(action_name, device, event)
                    action Function(godson_assign_binding, device, action_name, event)
                    at ui_button_motion

        hbox:
            spacing 22
            xalign 0.5

            textbutton _("UNBIND"):
                style "godson_controls_reset_button"
                action Function(godson_unbind_control, device, action_name)
                at ui_button_motion

            textbutton _("CANCEL"):
                style "godson_controls_reset_button"
                action Hide("godson_binding_picker")
                at ui_button_motion


style godson_controls_panel is ui_preferences_panel:
    padding (34, 30)

style godson_controls_heading is ui_preferences_label:
    size 34
    color "#F4D77B"
    outlines [(2, "#100A04", 0, 1)]

style godson_controls_copy is ui_preferences_description:
    size 23
    color "#CABD9F"
    outlines [(1, "#080604", 0, 1)]

style godson_controls_binding_row is button:
    xfill True
    yminimum 116
    padding (28, 18)
    background Frame("gui/christmas_noir/button_idle.png", 32, 20)
    hover_background Frame("gui/christmas_noir/button_hover.png", 32, 20)
    selected_background Frame("gui/christmas_noir/button_selected.png", 32, 20)

style godson_controls_action_text is text:
    font "fonts/jenriv-titling-bold.otf"
    size 29
    color "#F2E7CB"
    hover_color "#FFE39A"
    outlines [(2, "#090603", 0, 1)]

style godson_controls_description_text is text:
    font "fonts/jenriv-titling-bold.otf"
    size 21
    color "#BFB298"
    hover_color "#E8D5AA"
    outlines [(1, "#090603", 0, 1)]

style godson_controls_binding_badge is frame:
    xsize 690
    ysize 70
    yalign 0.5
    padding (20, 12)
    background Frame("gui/christmas_noir/tab_idle.png", 24, 16)

style godson_controls_binding_text is text:
    font "fonts/jenriv-titling-bold.otf"
    size 24
    color "#F5D471"
    outlines [(2, "#130B04", 0, 1)]

style godson_controls_reset_button is ui_preferences_button:
    xminimum 420
    yminimum 68

style godson_controls_readonly_row is frame:
    yminimum 92
    padding (26, 16)
    background Frame("gui/christmas_noir/button_idle.png", 32, 20)

style godson_binding_picker_frame is frame:
    xsize 2860
    ysize 1540
    padding (62, 48)
    background Frame("gui/christmas_noir/panel_strong.png", 70, 70)

style godson_binding_picker_title is text:
    font "fonts/jenriv-titling-bold.otf"
    size 48
    color "#F5D36B"
    outlines [(3, "#100904", 0, 2)]

style godson_binding_picker_copy is text:
    font "fonts/jenriv-titling-bold.otf"
    size 25
    color "#D4C6A6"
    xmaximum 2300
    outlines [(1, "#080604", 0, 1)]

style godson_binding_picker_current is frame:
    xsize 1200
    ysize 78
    padding (24, 15)
    background Frame("gui/christmas_noir/tab_idle.png", 24, 16)

style godson_binding_choice_button is ui_preferences_button:
    xminimum 790
    yminimum 82
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

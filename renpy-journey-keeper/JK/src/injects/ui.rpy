init 9999 python in JK:
    _constant = True

    def _m1_ui__can_perform_autosave():
        
        return not Autosaver.prevent_autosaving and not Memories.memoryInProgress and not renpy.store._in_replay and (Settings.autosaveOnSingletonChoice or Utils.is_displaying_multiple_choices())

    def _m1_ui__choice_return_call_partial(func, *args, **kwargs):
        if hasattr(func, "_original"):
            func = func._original
        
        def new_funct(*new_args, **new_kwargs):
            new_kwargs.update(kwargs.copy())
            
            Autosaver.handle_choice_selection(new_args[0])
            
            fn = func(*(args + new_args), **new_kwargs)
            
            return fn
        
        new_funct._original = func
        
        return new_funct

    def _m1_ui__button_init_partial(func, *args, **kwargs):
        if hasattr(func, "_original"):
            func = func._original
        
        def new_init_funct(button, *new_args, **new_kwargs):
            new_kwargs.update(kwargs.copy())
            
            func(button, *(args + new_args), **new_kwargs)
            
            
            if not Settings.autosaveOnNormalButtonsWithJump:
                return
            
            class Action(renpy.ui.Action):
                def __init__(self, button, action, node):
                    self.button = button
                    self.original_action = action
                    self.node = node
                
                def __call__(self, *args, **kwargs):
                    
                    if Settings.autosaveOnNormalButtonsWithJump:
                        Autosaver.handle_any_button_click(self.button)
                    
                    return renpy.display.behavior.run(self.original_action, *args, **kwargs)
            
            
            node = None
            
            
            if isinstance(button.action, renpy.ast.Jump) or isinstance(button.action, renpy.store.Jump):
                node = button.action
            
            elif isinstance(button.action, list) or isinstance(button.action, python_list):
                for n in button.action:
                    if isinstance(n, renpy.ast.Jump) or isinstance(n, renpy.store.Jump):
                        node = n
            
            
            
            if isinstance(node, renpy.ast.Jump) or isinstance(node, renpy.store.Jump):
                button.action = Action(button, button.action, node)
        
        new_init_funct._original = func
        
        return new_init_funct

    renpy.ui.ChoiceReturn.__call__ = _m1_ui__choice_return_call_partial(renpy.ui.ChoiceReturn.__call__)
    renpy.display.behavior.Button.__init__ = _m1_ui__button_init_partial(renpy.display.behavior.Button.__init__)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

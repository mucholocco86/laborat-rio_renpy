init 9999 python in JK:
    _constant = True

    def _m1_statement_callback__wait_for_start_label_callback(statement):
        if Autosaver.prevent_autosaving and statement == "label":
            current = renpy.game.context().current
            script = renpy.game.script.lookup(current)
            
            if script.name == "start":
                Autosaver.prevent_autosaving = False

    renpy.config.statement_callbacks.append(_m1_statement_callback__wait_for_start_label_callback)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

init 9999 python in JK:
    _constant = True

    def _m1_save_json_callback__save_json_callback(json):
        if Autosaver.pending_save:
            json["_JK_choice"] = Autosaver.pending_save.choice
        
        elif Settings.debugEnabled:
            print("Nenhuma escolha foi registrada", json)
            renpy.notify("Nenhuma escolha foi registrada")

    renpy.config.save_json_callbacks.append(_m1_save_json_callback__save_json_callback)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

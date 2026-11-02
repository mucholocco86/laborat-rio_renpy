init 9999 python in JK:
    _constant = True

    def _m1_start_interact_callback__start_interact_callback():
        SaveSystem.override_native_location()
        renpy.loadsave.clear_cache()
        SaveSystem.multilocation.scan()
        
        if(not renpy.get_screen('JK_SidepanelHolder')):
            renpy.show_screen('JK_SidepanelHolder')
        
        if(not renpy.get_screen('JK_Overlay')):
            renpy.show_screen('JK_Overlay')
        
        if renpy.store.persistent.JK_SizeAdjustmentRollbackValue != None and renpy.get_screen("JK_ConfirmSizeAdjustment") is None:
            renpy.show_screen('JK_ConfirmSizeAdjustment')

    renpy.config.start_interact_callbacks.append(_m1_start_interact_callback__start_interact_callback)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

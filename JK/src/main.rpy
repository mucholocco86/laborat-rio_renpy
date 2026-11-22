init -1 python in JK:
    _constant = True

    print("Initializing {} v{}".format(MOD_NAME, MOD_VERSION))

    Settings = SettingsClass()

init python in JK:
    _constant = True

    SaveSystem = SaveSystemClass()
    Playthroughs = PlaythroughsClass()
    Autosaver = AutosaverClass()
    Pagination = PaginationClass()
    Memories = MemoriesClass()

    # Ren'Py 7.4+ supports filename prefixes. Ren'Py 6.99 uses
    # searchpath directories instead, so keep JK assets discoverable there too.
    if hasattr(renpy.config, "search_prefixes"):
        if "JK/src/assets/" not in renpy.config.search_prefixes:
            renpy.config.search_prefixes.append("JK/src/assets/")
    else:
        import os
        jk_asset_path = os.path.join(renpy.config.gamedir, "JK", "src", "assets")
        if jk_asset_path not in renpy.config.searchpath:
            renpy.config.searchpath.append(jk_asset_path)

init 9999 python in JK:
    _constant = True

    if not 'n_e_s_w' in renpy.config.gestures:
        renpy.config.gestures['n_e_s_w'] = Settings.changeSidepanelVisibilityKey

    if not "JK_Sidepanel" in renpy.config.layers:
        renpy.config.layers.append("JK_Sidepanel")
        renpy.config.context_clear_layers.append("JK_Sidepanel")

    if not "JK_Overlay" in renpy.config.layers:
        renpy.add_layer("JK_Overlay", above="JK_Sidepanel")
        renpy.config.context_clear_layers.append("JK_Overlay")

    print("{} is ready".format(MOD_NAME))
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

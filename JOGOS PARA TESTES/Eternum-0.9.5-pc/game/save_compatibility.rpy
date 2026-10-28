
default game_version = 0

label after_load:

    if game_version < 0.4:
        window hide

        # Unlock all looks for old saves
        $ looks["annie"] = [ 0, 1, 2, 3, 4 ]
        $ looks["nancy"] = [ 0, 1, 2, 3, 4 ]
        $ looks["penelope"] = [ 0, 1, 2, 3, 4, 5, 6, 7 ]
        $ looks["dalia"] = [ 0, 1, 2, 3, 4, 5 ,6 ]
        $ looks["luna"] = [ 0, 1, 2, 3, 4 ]
        $ looks["alex"] = [ 0, 1, 2, 3 ]
        $ looks["nova"] = [ 0, 1, 2, 3, 4 ]

    # Update Annie's variable for 0.9
    $ interstellarm2 = interstellarm

    $ namelong = mc[-1]*5
    if nickname != "Nobody":
        $ nicknameunlock = True

    # Must be the last line of the "after_load" label
    $ game_version = myconfig.version

    return

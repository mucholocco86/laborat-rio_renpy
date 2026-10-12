## Default Version For New Game
default save_name = _(config.name + " v" + config.version)

label after_load:
    $ loaded_game = True

    if _in_replay:
        $ renpy.block_rollback()
        return

    $ save_name = _(config.name + " v" + config.version)

    return

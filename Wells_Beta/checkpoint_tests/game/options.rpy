# Minimal Ren'Py project used only by the Wells checkpoint runtime tests.
define config.name = "Wells Checkpoint Probe"
define config.version = "1.0"
define config.save_directory = "wells-checkpoint-probe"

init -2000 python:
    # The archived Ren'Py 6.99 test SDK omits this config list.
    if not hasattr(config, "overlay_functions"):
        config.overlay_functions = []
    if not hasattr(config, "predict_callbacks"):
        config.predict_callbacks = []
    if not hasattr(config, "renpy_base"):
        import os
        config.renpy_base = os.path.dirname(renpy.__file__)
    if not hasattr(config, "mode_callbacks"):
        config.mode_callbacks = []
    if not hasattr(config, "interact_callbacks"):
        config.interact_callbacks = []
    if not hasattr(config, "change_language_callbacks"):
        config.change_language_callbacks = []

    if not hasattr(config, "start_interact_callbacks"):
        config.start_interact_callbacks = []

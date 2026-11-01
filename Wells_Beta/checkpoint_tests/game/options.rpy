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

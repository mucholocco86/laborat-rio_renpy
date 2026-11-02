init python in JK:

    def _m1_JK_Run_hyperlink_handler__run(arg):
        renpy.python.py_exec("renpy.run({})".format(arg))

    renpy.config.hyperlink_handlers["JK_Run"] = _m1_JK_Run_hyperlink_handler__run
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

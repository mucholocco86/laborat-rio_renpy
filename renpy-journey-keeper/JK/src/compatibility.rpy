init -10000 python in JK:
    _constant = True

    # Preserve Python built-ins even when a game defines characters or
    # variables with the same names (for example, ``min``).
    try:
        import builtins as _python_builtins
    except ImportError:
        import __builtin__ as _python_builtins

    PY_MINIMUM = _python_builtins.min
    PY_MAXIMUM = _python_builtins.max
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

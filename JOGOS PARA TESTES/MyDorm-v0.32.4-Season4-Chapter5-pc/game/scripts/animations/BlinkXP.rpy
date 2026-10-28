label BlinkXP (x, p = "d"):
    $ Ba = x+"a"
    $ Bb = x+"b"
    $ Bc = x+"c"
    $ T1 = renpy.random.randint (3, 7)/10
    $ T2 = renpy.random.randint (15, 30)/10
    image blinkX:
        Ba with dissolve
        T1
        Bb with dissolve
        0.2
        Bc with dissolve
        0.25
        Bb with dissolve
        0.2
        Ba with dissolve
        T2
        repeat
    if p == "d":
        scene blinkX with dissolve
    elif p == "h":
        scene blinkX with hpunch
    elif p == "v":
        scene blinkX with vpunch
    elif p == "f":
        scene blinkX with fade
    else:
        scene blinkX
    return
label BlinkXPS3 (x, p = "d"):
    $ Ba = x+"a"
    $ Bb = x+"b"
    $ Bc = x+"c"
    $ T1 = renpy.random.randint (3, 7)/10
    $ T2 = renpy.random.randint (15, 30)/10
    image blinkX:
        Ba with dissolve
        T1
        Bb with dissolve
        0.2
        Bc with dissolve
        0.25
        Bb with dissolve
        0.2
        Ba with dissolve
        T2
        repeat
    if p == "d":
        scene blinkX with dissolve
    elif p == "h":
        scene blinkX with hpunch
    elif p == "v":
        scene blinkX with vpunch
    elif p == "f":
        scene blinkX with fade
    else:
        scene blinkX
    return
label BlinkXS3 (x):
    $ Ba = x+"a"
    $ Bb = x+"b"
    $ Bc = x+"c"
    $ T1 = renpy.random.randint (3, 7)/10
    $ T2 = renpy.random.randint (15, 30)/10
    image blinkX:
        Ba with dissolve
        T1
        Bb with dissolve
        0.2
        Bc with dissolve
        0.25
        Bb with dissolve
        0.2
        Ba with dissolve
        T2
        repeat
    scene blinkX with dissolve
    return
label BlinkXS4 (x):
    $ Ba = x+"a"
    $ Bb = x+"b"
    $ Bc = x+"c"
    $ T1 = renpy.random.randint (3, 7)/10
    $ T2 = renpy.random.randint (15, 30)/10
    image blinkX:
        Ba with dissolve
        T1
        Bb with dissolve
        0.2
        Bc with dissolve
        0.25
        Bb with dissolve
        0.2
        Ba with dissolve
        T2
        repeat
    scene blinkX with dissolve
    return

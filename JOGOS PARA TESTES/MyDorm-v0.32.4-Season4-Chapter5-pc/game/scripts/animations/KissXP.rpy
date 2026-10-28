label KissXP (x, p = "d"):
    $ Ba = x + "a"
    $ Bb = x + "b"
    image KissX:
        Ba with dissolve
        1.0
        Bb with dissolve
        1.0
        Ba with dissolve
    if p == "d":
        scene KissX with dissolve
    elif p == "h":
        scene KissX with hpunch
    elif p == "v":
        scene KissX with vpunch
    elif p == "f":
        scene KissX with fade
    else:
        scene KissX
    return
label KissXPS3 (x, p = "d"):
    $ Ba = x + "a"
    $ Bb = x + "b"
    image KissX:
        Ba with dissolve
        1.0
        Bb with dissolve
        1.0
        Ba with dissolve
    if p == "d":
        scene KissX with dissolve
    elif p == "h":
        scene KissX with hpunch
    elif p == "v":
        scene KissX with vpunch
    elif p == "f":
        scene KissX with fade
    else:
        scene KissX
    return
label KissXS3 (x):
    $ Ba = x + "a"
    $ Bb = x + "d"
    image KissX:
        Ba with dissolve
        1.0
        Bb with dissolve
        1.0
        Ba with dissolve
    scene KissX with dissolve
    pause 2.0
    return
label KissXS4 (x):
    $ Ba = x + "a"
    $ Bb = x + "d"
    image KissX:
        Ba with dissolve
        1.0
        Bb with dissolve
        1.0
        Ba with dissolve
    scene KissX with dissolve
    pause 2.0
    return

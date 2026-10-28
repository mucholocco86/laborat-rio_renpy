label BlinkXP2 (x, p = "d"):
    $ Ba = x + "d"
    $ Bb = x + "e"
    $ Bc = x + "f"
    image blinkX2:
        Ba with dissolve
        0.5
        Bb with dissolve
        0.3
        Bc with dissolve
        0.5
        Bb with dissolve
        0.3
        Ba with dissolve
        2.5
        repeat
    if p == "d":
        scene blinkX2 with dissolve
    elif p == "h":
        scene blinkX2 with hpunch
    elif p == "v":
        scene blinkX2 with vpunch
    elif p == "f":
        scene blinkX2 with fade
    else:
        scene blinkX2
    return
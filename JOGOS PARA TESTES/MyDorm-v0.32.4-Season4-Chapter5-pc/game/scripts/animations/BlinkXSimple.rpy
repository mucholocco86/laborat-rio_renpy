label BlinkXSimple (x):
    $ Ba = x + "a"
    $ Bb = x + "b"
    $ Bc = x + "c"
    $ bt = x + "Blink"
    image bt:
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
    return
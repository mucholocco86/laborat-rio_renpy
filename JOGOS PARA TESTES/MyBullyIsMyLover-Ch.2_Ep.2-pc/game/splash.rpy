label splashscreen:
    scene black
    with Pause(1)

    show logo
    with dissolve
    pause 11.0

    scene black
    with dissolve
    with Pause(2)

    scene disclaimer
    with dissolve
    $ renpy.pause()

    scene black
    with Dissolve(1.0)
    return

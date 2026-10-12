#Start Chaper
label ch2sc27_b:

    #play music morning_1

    # start scene 2
        window hide dissolve
        play music dark_1 fadein 2.0
        scene black with Dissolve (2.0)
        $ renpy.pause(0.5)
        scene ss43 with Dissolve (2.0)
        $ renpy.pause()
        scene ch2sc27_01 with Dissolve(2.0)
        $ renpy.pause()
        scene ch2sc27_02 with dissolve
        $ renpy.pause()
        scene ch2sc27_03 with dissolve
        $ renpy.pause()
        scene ch2sc27_04 with dissolve
        uk "Sir."
        scene ch2sc27_05 with dissolve
        ukta "What?"
        scene ch2sc27_04 with dissolve
        uk "One of our couriers has brought news."
        scene ch2sc27_05 with dissolve
        ukta "Speak."
        scene ch2sc27_06 with dissolve
        uk "Sir, it’s about him."
        uk "He’s alive, on his way to the capital."
        uk "Shado-jin Rol has not reported back at the appointed time."
        scene ch2sc27_05 with dissolve
        ukta "Perfect."
        scene ch2sc27_06 with dissolve
        uk "Sir?"
        uk "Shouldn't we-"
        scene ch2sc27_05 with dissolve
        ukta "Leave."
        scene ch2sc27_07 with dissolve
        with vpunch
        uk "At once sir!"
        scene ch2sc27_08 with dissolve
        $ renpy.pause()
        scene ch2sc27_09 with dissolve
        $ renpy.pause()
        scene ch2sc27_10 with dissolve
        $ renpy.pause(0.5)
        ukta "It was only a matter of time until you decided to seek me out."
        ukta "Taking down Rol, that's quite a feat, you're full of surprises..."
        ukta "Yet, it wasn't entirely unexpected..."
        ukta "I look forward to meeting you... Nephilim."
        scene black with Dissolve(3)
        stop music fadeout 2.0
        $ renpy.pause(0.5)
        jump ch2sc28

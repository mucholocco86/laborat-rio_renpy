#Start Chaper
label ch2sc15fb15:

    #play music morning_1

    # start scene 2
        window hide dissolve
        play music dark_1 fadein 2.0
        scene black with Dissolve (2.0)
        scene ch2sc15_fb15_01 with Dissolve(2.0)
        $ renpy.pause()
        ".."
        "...."
        "......"
        window show dissolve
        scene nephilim_ch2 with Dissolve(2)
        $ renpy.pause()
        scene ch2sc15_fb15_03 with dissolve
        stop music fadeout 2.0
        mc "Is that where we're heading?"
        scene ch2sc15_fb15_02 with dissolve
        play music chill_3 fadein 2.0
        oe "..."
        scene ch2sc15_fb15_03 with dissolve
        mc "What’s out there?"
        scene ch2sc15_fb15_04 with dissolve
        oe "..."
        scene ch2sc15_fb15_05 with dissolve
        mc "Always with the silence..."
        scene ch2sc15_fb15_06 with dissolve
        $ renpy.pause()
        scene ch2sc15_fb15_07 with dissolve
        mc "We’ve been on the road for several moons now."
        mc "The least you can do is tell me where we’re going."
        scene ch2sc15_fb15_08 with dissolve
        with vpunch
        mc "{b}Old man!{/b}"
        scene ch2sc15_fb15_09 with dissolve
        stop music fadeout 2.0
        with vpunch
        oe "{b}Quiet boy!{/b}"
        scene ch2sc15_fb15_10 with dissolve
        mc "..."
        scene ch2sc15_fb15_11 with dissolve
        mc "Wha-"
        scene ch2sc15_fb15_12 with dissolve
        play music darknight_3 fadein 1.0
        uk "Hrrraahhrr!!"
        scene ch2sc15_fb15_13 with dissolve
        oe "Watch out!"
        scene ch2sc15_fb15_14 with dissolve
        $ renpy.pause(0.5)
        scene ch2sc15_fb15_15 with dissolve
        with vpunch
        $ renpy.pause(1.5)
        scene ch2sc15_fb15_16 with dissolve
        "The ugly creature appears to be knocked out with just one punch from Oren."
        scene ch2sc15_fb15_17 with dissolve
        mc "Woah! You made that look easy, old man!"
        scene ch2sc15_fb15_18 with dissolve
        with vpunch
        oe "{b}Get down boy!{/b}"
        scene ch2sc15_fb15_19 with dissolve
        $ renpy.pause()
        scene ch2sc15_fb15_20 with dissolve
        $ renpy.pause()
        scene ch2sc15_fb15_21 with dissolve
        $ renpy.pause()
        scene ch2sc15_fb15_22 with dissolve
        $ renpy.pause()
        scene ch2sc15_fb15_23 with dissolve
        with vpunch
        $ renpy.pause()
        scene ch2sc15_fb15_24 with dissolve
        $ renpy.pause()
        scene ch2sc15_fb15_25 with dissolve
        $ renpy.pause()
        scene ch2sc15_fb15_26 with dissolve
        with vpunch
        $ renpy.pause()
        scene ch2sc15_fb15_27 with dissolve
        stop music fadeout 2.0
        uk "Hrerrhhhrhh... hHhHrr..."
        scene ch2sc15_fb15_28 with dissolve
        play music explore_1 fadein 2.0
        mc "W-What was that ugly thing?"
        scene ch2sc15_fb15_29 with dissolve
        oe "Goblin. Foul creature."
        scene ch2sc15_fb15_30 with dissolve
        mc "Goblins are real?"
        scene ch2sc15_fb15_31 with dissolve
        oe "Lesson one. Trust your eyes, boy."
        scene ch2sc15_fb15_32 with dissolve
        mc "Trust my... What does that even mean?"
        scene ch2sc15_fb15_33 with dissolve
        oe "Time to move."
        oe "Goblins rarely venture far from their nest, others might have heard us."
        scene ch2sc15_fb15_34 with dissolve
        mc "W-Wait up!"
        scene black with dissolve
        "Over the next few moons, the two of you continue to traverse all sorts of unfamiliar terrain."
        scene ch2sc15_fb15_35 with dissolve
        $ renpy.pause()
        scene ch2sc15_fb15_36 with dissolve
        $ renpy.pause()
        scene ch2sc15_fb15_37 with dissolve
        $ renpy.pause()
        scene ch2sc15_fb15_38 with dissolve
        $ renpy.pause()
        scene ch2sc15_fb15_39 with dissolve
        $ renpy.pause()
        stop music fadeout 2.0
        scene black with dissolve
        "Finally reaching what appears to be your destination."
        play music explore_2 fadein 1.0
        "You’ve been traveling further and further east for the past few moons. The landscape and vegetation has changed drastically."
        scene ch2sc15_fb15_40 with dissolve
        $ renpy.pause()
        scene ch2sc15_fb15_40 with dissolve
        "It’s almost as if no human influence is felt in this region of Midomir, and yet..."
        "There’s magnificent architecture here, unlike anything you’ve seen back home."
        "It seems the old man is familiar with the area and knows where you’re headed... the Sen'ju region."
        oe "We're here... Nakajima, this'll be our home for a while."
        mc "Naka... jima? How long will we stay?"
        oe "As long as it takes, boy."
        scene black with Dissolve(3)

        stop music fadeout 2.0
        jump ch2sc16

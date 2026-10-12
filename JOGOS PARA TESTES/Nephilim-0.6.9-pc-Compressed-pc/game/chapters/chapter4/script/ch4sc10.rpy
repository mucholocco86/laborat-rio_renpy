label ch4sc10:

    window hide dissolve
    play music explore_2 fadein 1.0
    scene black with Dissolve (1.0)
    #

    scene ch4sc10_001 with Dissolve(2.0)
    $ renpy.pause(1)
    "Over the next week, you and Flynn bond with the crew of the Bloody Banshee."
    scene ch4sc10_002 with dissolve
    $ renpy.pause(1)
    if kelly_sex == True:
        scene ch4sc10_002 with Dissolve(1.3)
        $ renpy.pause(1)
        scene ch4sc10_003 with Dissolve(1.3)
        $ renpy.pause(1)
        scene ch4sc9_0136 with Dissolve(1.3)
        $ renpy.pause(1)
        scene ch4sc9_0140 with Dissolve(1.3)
        $ renpy.pause(1)
        scene ch4sc10_002 with dissolve
        $ renpy.pause(1)
        scene ch4sc9_099 with dissolve
        $ renpy.pause(1.5)
        scene ch4sc9_0117 with dissolve
        $ renpy.pause(1.5)
        scene ch4sc9_0125 with dissolve
        $ renpy.pause(1.5)
        scene ch4sc10_004 with dissolve
        $ renpy.pause(1)
        scene ch4sc10_005 with dissolve
        $ renpy.pause(1)
        scene ch4sc9_0136 with dissolve
        $ renpy.pause(1)
        scene ch4sc9_0142 with dissolve
        $ renpy.pause(1)
        scene ch4sc10_005 with dissolve
        $ renpy.pause(1)
        scene ch4sc10_006 with dissolve
        $ renpy.pause(1)
        scene ch4sc10_007 with dissolve
        $ renpy.pause(1)
        scene ch4sc10_003 with dissolve
        $ renpy.pause(1)
        scene ch4sc10_008 with dissolve
        $ renpy.pause(2)
        scene ch4sc10_009 with dissolve
        $ renpy.pause(2)
        scene ch4sc10_010 with dissolve
        $ renpy.pause(1)
        scene ch4sc10_011 with dissolve
        $ renpy.pause(2)
        scene ch4sc9_099 with dissolve
        $ renpy.pause(1.5)
        scene ch4sc9_0117 with dissolve
        $ renpy.pause(1.5)
        scene ch4sc9_0125 with dissolve
        $ renpy.pause(1.5)
        scene ch4sc9_0136 with dissolve
        $ renpy.pause(1)
        scene ch4sc10_012 with dissolve
        $ renpy.pause(1.7)
        scene ch4sc10_013 with dissolve
        $ renpy.pause(1.7)
        scene ch4sc10_005 with dissolve
        $ renpy.pause(1.7)
        scene ch4sc10_010 with dissolve
        $ renpy.pause(1)
        scene ch4sc10_014 with dissolve
        $ renpy.pause(1.7)
        scene ch4sc10_015 with dissolve
        $ renpy.pause(1.7)
        scene ch4sc10_011 with dissolve
        $ renpy.pause(1.7)
        scene ch4sc10_004 with dissolve
        $ renpy.pause(2)
        scene ch4sc10_007 with dissolve
        $ renpy.pause(2)
        scene ch4sc10_008 with dissolve
        $ renpy.pause(2)
        scene ch4sc10_009 with dissolve
        $ renpy.pause(2)
        scene ch4sc10_014 with dissolve
        $ renpy.pause(1.7)
        scene ch4sc10_015 with dissolve
        $ renpy.pause(1.7)
        scene black with Dissolve(2)
    else:
        scene ch4sc10_002 with dissolve
        $ renpy.pause(1)
        scene ch4sc10_003 with dissolve
        $ renpy.pause(1)
        scene ch4sc9_0136 with dissolve
        $ renpy.pause(1)
        scene ch4sc9_0140 with dissolve
        $ renpy.pause(1)
        scene ch4sc10_002 with dissolve
        $ renpy.pause(1)
        scene ch4sc10_004 with dissolve
        $ renpy.pause(1)
        scene ch4sc10_005 with dissolve
        $ renpy.pause(1)
        scene ch4sc9_0136 with dissolve
        $ renpy.pause(1)
        scene ch4sc9_0142 with dissolve
        $ renpy.pause(1)
        scene ch4sc10_005 with dissolve
        $ renpy.pause(1)
        scene ch4sc10_006 with dissolve
        $ renpy.pause(1)
        scene ch4sc10_007 with dissolve
        $ renpy.pause(1)
        scene ch4sc10_003 with dissolve
        $ renpy.pause(1)
        scene ch4sc10_008 with dissolve
        $ renpy.pause(2)
        scene ch4sc10_009 with dissolve
        $ renpy.pause(2)
        scene ch4sc10_010 with dissolve
        $ renpy.pause(1)
        scene ch4sc10_011 with dissolve
        $ renpy.pause(2)
        scene ch4sc9_0136 with dissolve
        $ renpy.pause(1)
        scene ch4sc10_012 with dissolve
        $ renpy.pause(1.7)
        scene ch4sc10_013 with dissolve
        $ renpy.pause(1.7)
        scene ch4sc10_005 with dissolve
        $ renpy.pause(1.7)
        scene ch4sc10_010 with dissolve
        $ renpy.pause(1)
        scene ch4sc10_014 with dissolve
        $ renpy.pause(1.7)
        scene ch4sc10_015 with dissolve
        $ renpy.pause(1.7)
        scene ch4sc10_011 with dissolve
        $ renpy.pause(1.7)
        scene ch4sc10_004 with dissolve
        $ renpy.pause(2)
        scene ch4sc10_007 with dissolve
        $ renpy.pause(2)
        scene ch4sc10_008 with dissolve
        $ renpy.pause(2)
        scene ch4sc10_009 with dissolve
        $ renpy.pause(2)
        scene ch4sc10_014 with dissolve
        $ renpy.pause(1.7)
        scene ch4sc10_015 with dissolve
        $ renpy.pause(1.7)
        scene black with Dissolve(2)
    scene ch4sc10_016 with Dissolve(2)
    stop music fadeout 1.0

    kl "{b}*Shouts* Kira! We’re here!{/b}"
    play music explore_1 fadein 1.0
    scene ch4sc10_017 with dissolve
    ki "Finally!"
    ki "Once we're docked, you're in charge of stocking the ship with supplies!"
    scene ch4sc10_018 with dissolve
    mc "Did Kelly just announce we’re here?"
    mc "I thought it would take more than a week to reach Inmortui?"
    scene ch4sc10_019 with dissolve
    ki "*Scoffs* We’re not at Inmortui."
    ki "We’re taking a little detour."
    scene ch4sc10_018 with dissolve
    mc "What the fuck, Kira? That wasn’t our deal."
    mc "I don’t have time for this shit!"
    scene ch4sc10_019 with dissolve
    ki "Boohoo! 'Cause we’re here now and I’m taking you to meet someone."
    scene ch4sc10_018 with dissolve
    mc "Who?!"
    scene ch4sc10_019 with dissolve
    ki "My fath- The pirate king. Captain Blackheart."
    ki "You'd better tell him what you’re after. He isn’t known for his hospitality or his patience."
    scene ch4sc10_018 with dissolve
    mc "Where the fuck are we, Kira?"
    scene ch4sc10_019 with Dissolve(2)
    ki "Here it is!"
    scene ch4sc10_021 with Dissolve(2)
    $ renpy.pause(1)
    ki "{b}Looter’s Bay.{/b}"
    scene ch4sc10_022 with Dissolve(2)
    $ renpy.pause(1)
    ki "Home..."
    mct "*Exhales deeply* Stay calm... just a little detour... if I kill them now, I won't be able to reach Inmortui."
    scene black with Dissolve(2)
    stop music fadeout 1.0
    jump ch4sc11

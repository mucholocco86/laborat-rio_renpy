label ch3sc13:

    window hide dissolve
    play music explore_1 fadein 1.0
    scene black with Dissolve (1.0)
    scene ch3sc13_intro with Dissolve(2.0)
    $ renpy.pause(2)
    scene ch3sc13_001 with Dissolve(2.0)
    $ renpy.pause(1)
    mc "I suppose I should think about upgrading my outfit as well."
    scene ch3sc13_002 with dissolve
    mc "I’ll wait til we have a bit more coin, though."
    mc "Hopefully Eliza is right about us getting more lucrative quests as we advance in the guild."
    $ renpy.pause(1)
    with vpunch
    scene ch3sc13_003 with dissolve
    mct "Huh..?"
    uk "{b}SCOUNDREL!!{/b}"
    with vpunch
    scene ch3sc13_004 with dissolve
    mct "Hmm. Sounds familiar..."
    uk "Ye tryin' te rob me?!"
    scene ch3sc13_005 with dissolve
    mct "Definitely came from back there."
    scene ch3sc13_006 with dissolve
    with vpunch
    br "{b}ARE YE MAD?!{/b}"
    scene ch3sc13_007 with dissolve
    uk "Sir, this is the standard rate we offer for such... basic items."
    br "Basic... items..."
    scene ch3sc13_008 with dissolve
    with vpunch
    br "{b}YER TRYING TE TRICK ME NOW?!{/b}"
    br "This is fine steel! Nothing basic about it!"
    scene ch3sc13_009 with dissolve
    uk "N-No sir, I’m sorry but we can’t offer you more than this."
    scene ch3sc13_010 with dissolve
    br "Arrrgh! Blasted! Fine..."
    br "Ye better bring plenty o'coins next time."
    scene ch3sc13_011 with dissolve
    mc "Hey Borri. I thought it was you I heard back here."
    scene ch3sc13_012 with dissolve
    br "Arh! [mc]! Can ye believe this fella tryin' te rob me blind!?"
    br "*Scoffs* Basic steel he says?"
    scene ch3sc13_013 with dissolve
    uk "Sir... I already explained-"
    scene ch3sc13_014 with dissolve
    with vpunch
    br "Silence, ye scoundrel!"
    br "Get outta here before I eat ye alive!"
    scene ch3sc13_015 with dissolve
    with vpunch
    br "{b}Be gone!{/b}"
    uk "{b}Aaarrrhhh!! Mercy!{/b}"
    scene ch3sc13_016 with dissolve
    mc "Dwarves eat people? That's the first I've heard of it."
    scene ch3sc13_017 with dissolve
    br "Hah! Don’t be gross, [mc]."
    br "Naye, we much prefer pork I tell ye! *Chuckles*"
    scene ch3sc13_018 with dissolve
    br "Did you see the look on his face, though? *Chuckles*"
    br "Nothing like a good ol'fashioned scare te make sure he remembers."
    scene ch3sc13_016 with dissolve
    mc "You definitely gave him a good scare."
    mc "I almost saw his soul leave his body. Mind telling me what’s going on?"
    scene ch3sc13_019 with dissolve
    br "Argh! Yer being dramatic, [mc]."
    br "Ye know I deliver armaments from nearby villages ter the capital..."
    scene ch3sc13_020 with dissolve
    br "Swords, shields, spears and armor, ye know?"
    scene ch3sc13_021 with dissolve
    mc "Ah, so that’s what you do? That explains the cart you were wheeling around when we first met."
    mc "And let me guess, he didn’t pay the agreed price?"
    scene ch3sc13_022 with dissolve
    br "Yer a smart lad, [mc]! Now I’m short two silvers fer the next delivery."
    br "*Heavy sigh* These deliveries don’t pay as much as they used te, I’m afraid..."
    scene ch3sc13_023 with dissolve
    mc "I suppose times of peace is not exactly the best for the armors and weapons industry..."
    mc "Hmm..."
    mc "Here’s an idea, why don’t you sign up with the Adventurers Guild?"
    scene ch3sc13_024 with dissolve
    br "Me? An adventurer?"
    br "Ye takin' the piss, lad?"
    ###CHOICE###
    menu:
        "Be serious.":
            scene ch3sc13_025 with dissolve
            mc "Why not? Eliza and I finished our first Quest earlier today... ten silvers for our trouble."
            scene ch3sc13_026 with dissolve
            br "Hmmm..."
            "Uncertainty creases his face as the dwarf mulls over the idea."
            br "Hhrrhmmhrrhh..."
            scene ch3sc13_027 with dissolve
            br "Ten silvers, ye say?"
            scene ch3sc13_028 with dissolve
            mc "Ten silvers."
            scene ch3sc13_029 with dissolve
            br "For one days work? Bloody hells..."
            scene ch3sc13_028 with dissolve
            mc "Half a days work."
            scene ch3sc13_029 with dissolve
            br "*Scoffs* Heh! Ye really think I could be suited fer such things, lad?"
            br "Me? Hhrrm... I haven't done that kind o' work before."
            br "Ten silvers, he says... HhrmMhmm..."
            scene ch3sc13_028 with dissolve
            mc "I wouldn’t suggest it otherwise."
            mc "Sometimes, trying something different can set you on a new path in life."
            mc "One that's more... rewarding too."
            scene ch3sc13_030 with dissolve
            br "Alright! Alright! Ye convinced me, lad. Don't go all sentimental on me now, ye hear?"
            br "I’ll go sign up with yer guild tomorrow!"

        "Joke around.":
            scene ch3sc13_028 with dissolve
            mc "With your temperament, Borri, you'd be sure to scare off potential contracts."
            scene ch3sc13_031 with dissolve
            br "Arrgh! I knew ye were messin' with me!"
            scene ch3sc13_032 with dissolve
            mc "You just make it too easy, Borri."
            scene ch3sc13_028 with dissolve
            mc "But really, I think you'd fit in well with the guild."
            scene ch3sc13_031 with dissolve
            br "Can ye say if the coin is any good?"
            scene ch3sc13_033 with dissolve
            br "If I don’t bring home a good amount o' coin, me wife will skin me arse, lad."
            scene ch3sc13_032 with dissolve
            mc "Then why are you worried? There seems to be plenty left to skin..."
            scene ch3sc13_035 with dissolve
            mc "With an ass that big, you won’t be able to keep up."
            scene ch3sc13_036 with dissolve
            br "Hah! Ye think yer funny? Tomorrow I’ll go sign up with the guild and prove ye wrong, lad!"
            br "Ye better watch out. Before ye know it, Borri will be hoarding all the quests!"

    scene ch3sc13_037 with dissolve
    mct "It'll be good for him to do something different... being underpaid in a stale industry won't do him any good."
    mct "I have a feeling he'll make a great adventurer."
    mct "And the guild has been low on recruits, so filling the ranks will benefit us all."
    scene ch3sc13_038 with dissolve
    br "So, where yer headin' lad?"
    br "I don't see the lass, Eliza, with ye?"
    scene ch3sc13_039 with dissolve
    mc "I’m meeting up with her at the tavern later... The Drunken Rooster I think it's called?"
    mc "She went to get us a room and then she wanted to purchase a new outfit with the coin we earned."
    mc "For now, I’m just roaming the city a bit. Seeing if anything catches my eye and getting my bearings."
    scene ch3sc13_036 with dissolve
    br "Ah! Then I'll meet ye at the tavern later for some ales!"
    scene ch3sc13_040 with dissolve
    mc "Great."
    mc "See you then, Borri."

    if borri_ring == True:
        scene ch3sc13_041 with dissolve
        br "The ales are on me, lad!"
        br "As thanks fer finding me ring back in the woods!"
        scene ch3sc13_042 with dissolve
        mc "You're welcome, glad we could help you with that."
        mc "I'll be having a few ales on your expense later! *Chuckles*"
        br "*Chuckles* Hm!"
        $ borri_trust += 2
        "Borri appreciates you being honest about his ring, his trust has increased by {size=+3}{b}{color=#2bff8b}2{/color}{/b}{/size}."

    else:
        scene ch3sc13_041 with dissolve
        br "Aye, catch ye later!"

    scene black with Dissolve(2)
    stop music fadeout 2.0
    $ renpy.pause(0.5)
    jump ch3sc14

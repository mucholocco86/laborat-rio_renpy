
label ch3sc4:

    window hide dissolve
    play music explore_1 fadein 1.0
    scene black with Dissolve (2.0)
    "Back on the streets of the capital..."
    scene ch3sc04_001 with Dissolve(2.0)
    $ renpy.pause(1)
    el "This is so exciting! I can’t believe we are official members of the guild now!"
    el "I'm surprised we got accepted so easily."
    scene ch3sc04_002 with dissolve
    mc "Well, given their current situation, it would have been foolish of him to decline us."
    mc "Sounds like the guild need all the help it can get."
    scene ch3sc04_003 with dissolve
    el "I think he accepted us 'cause he could sense we'll become great adventurers!"
    scene ch3sc04_004 with dissolve
    mc "Only time will tell."
    mc "Either way, we should watch out for anything that could be connected to the recruiting issue or the kidnappings."
    scene ch3sc04_005 with dissolve
    el "Right! First we should get our equipment checked and prepared."
    el "Then we can head back to Sylph."
    scene ch3sc04_006 with dissolve
    el "Dalen said she would have a quest ready for us."
    el "I can't wait to see what it is! This is so exciting!"
    scene ch3sc04_007 with dissolve
    mct "*Chuckles* It’s cute how excited she seems to be about getting a quest."
    menu:
        "Hold her hand." if True:
            scene ch3sc04_008 with dissolve
            mct "I'm glad I'm able to share this moment with her."
            mct "We've come a long way already."
            scene ch3sc04_008a with dissolve
            $ renpy.pause(1.2)
            scene ch3sc04_008b with dissolve
            $ renpy.pause(1.2)
            scene ch3sc04_008c with dissolve
            el "Careful, [mc]."
            scene ch3sc04_008d with dissolve
            mc "Mh?"
            scene ch3sc04_008e with dissolve
            el "Holding a girl's hand in public?"
            el "Keep doing things like this, and a girl might think you like her."
            scene ch3sc04_008d with dissolve
            mc "A girl might be right."
            scene ch3sc04_008e with dissolve
            el "A girl is always right! *Giggling*"
            el "And she thinks you should..."
            scene ch3sc04_008f with dissolve
            el "You should keep doing it!"
            el "Yes, that would definitely be the right thing to do..."
            scene ch3sc04_008g with dissolve
            mc "Don’t worry."
            mc "I’m not letting go of this cute little hand of yours... it belongs to me now."
            scene ch3sc04_008h with dissolve
            el "You say the silliest things."
            "Eliza feels great comfort in holding your hand, her trust has increased by {size=+3}{b}{color=#2bff8b}1{/color}{/b}{/size}."
            el "Come on, let’s go. I’m intrigued to find out more about our first quest!"
            scene ch3sc04_008i with dissolve
            mc "Honestly, I’m looking forward to it as well."
            $ eliza_trust += 1
            el "What do you think it'll be? Helping a cat out of a tree? Returning chickens to their owner?"
            el "No, it has to be more involved than that, it's our recruitment quest!"
            mc "*Chuckles* I'm not sure, maybe we'd have to catch a thief? Or return stolen goods?"
            mc "Could be anything, as adventurers, our contracts could easily have us traveling outside Luxenford as well."
            el "Hmm! Guess we'll find out when we return to Sylph."

        "Don’t hold her hand." if True:
            scene ch3sc04_009 with dissolve
            mc "Let’s get going. The sooner we start our quest, the better."
            scene ch3sc04_010 with dissolve
            el "I can’t wait to get started on our first mission!"
            el "I don’t feel like we can truly call ourselves members til we’ve completed at least one quest."

    scene black with Dissolve(2)
    stop music fadeout 2.0
    jump ch3sc5

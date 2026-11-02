#Start Chaper
label ch2sc28:

    #play music morning_1

    # start scene 2
        window hide dissolve
        play music explore_1 fadein 2.0
        scene black with Dissolve (2.0)
        scene ss92 with Dissolve (2.0)
        $ renpy.pause()
        scene ch2sc28_01 with Dissolve(2.0)
        $ renpy.pause()
        scene ch2sc28_02 with dissolve
        el "*Sigh* We’ve been traveling for days and we still haven't found a tavern!"
        scene ch2sc28_03 with dissolve
        mc "Are you saying you’re too fancy to sleep on the ground?"
        scene ch2sc28_04 with dissolve
        el "*Giggles* Yes... that's exactly what I’m saying!"
        scene ch2sc28_05 with dissolve
        el "Now, let’s find a tavern! I’m thirsty for any type of ale, and my butt desperately needs the comfort of a bed!"
        scene ch2sc28_06 with dissolve
        mc "Ales do sound good."
        scene ch2sc28_07 with dissolve
        mc "Alright, let’s see if we can find a tavern."
        mc "I’ve noticed more travelers on the road the last few miles."
        scene ch2sc28_08 with dissolve
        mc "Are you thinking what I’m thinking?"
        scene ch2sc28_09 with dissolve
        el "Hmmm... We’ve seen more travelers recently?"
        el "And more travelers means there’s a place to rest nearby, either a settlement or tavern?"
        scene ch2sc28_10 with dissolve
        mc "Exactly, let’s pick up the pace. I can see a mug with my name on it."

        if eliza_relationship == True:
            scene ch2sc28_11 with dissolve
            with vpunch
            el "Yes! Let’s go! Before they drink all our ale!"
            scene ch2sc28_12 with dissolve
            mc "What do you think you’re doing?"
            scene ch2sc28_13 with dissolve
            el "I’m mounting you silly!"
            el "Don't you like having my legs wrapped around you?"
            scene ch2sc28_12 with dissolve
            mc "When you put it like that..."
            scene ch2sc28_14 with dissolve
            el "That’s what I like to hear!"
            el "*Giggling* Now, to the nearest tavern my steed!"
            scene ch2sc28_15 with dissolve
            mc "Buckle up, kitten. You’re in for a ride!"
            scene ch2sc28_16 with dissolve
            $ renpy.pause()
            scene ch2sc28_17 with dissolve
            $ renpy.pause(1)
            mct "*Chuckles* This'll get her heart rate up."
            play music chill_2 fadein 1.0
            scene ch2sc28_18 with dissolve
            $ renpy.pause()
            scene ch2sc28_19 with dissolve
            with vpunch
            el "{b}Aaaaiiihihaaaa!{/b}"
            "You set off at full-speed, the world around you turns to a blur as you zoom through the woods."
            scene ch2sc28_20 with dissolve
            el "{size=+3}{b}*Squeals loudly* OH MY GAWWWHHD!!{/b}{/size}"
            el "{size=+3}{b}*Squeals loudly* M-MY EYES CAN'T KEEP UP!! AYYYHH!!{/b}{/size}"
            scene ch2sc28_21 with dissolve
            $ renpy.pause(0.5)
            uk "Hmm, nothing interesting ever happens in these parts..."
            scene ch2sc28_22 with dissolve
            $ renpy.pause(1)
            scene ch2sc28_23 with dissolve
            with vpunch
            $ renpy.pause(0.5)
            el "Aaahh! That was wild!!"
            scene ch2sc28_24 with dissolve
            el "Thank you for the ride, handsome."
            el "*Whispers* {size=-10}{b}My legs are trembling.{/b}{/size}"
            scene ch2sc28_25 with dissolve
            $ renpy.pause()
            el "Mwaaah!"
            "Her kiss lingers for several seconds before she breaks away."
            scene ch2sc28_24 with dissolve
            el "Definitely won’t be the last time I ride you."
            scene ch2sc28_25 with dissolve
            el "*Mwah* Let's get your eyes back to normal before we head inside... Mmmh."
            stop music fadeout 1.0
            scene ch2sc28_30 with Dissolve(2)
            play music chill_3 fadein 1.0
            el "Come, come! I need to sit down before my legs turn to jelly!"
            el "My head is even spinning slightly after that ride..."
            scene ch2sc28_31 with dissolve
            mc "Ladies first."
            scene ch2sc28_32 with dissolve
            el "My, my... What a gentleman!"
            el "*Whispers* {size=-10}{b}I could get used to this...{/b}{/size}"
            stop music fadeout 2.0
            scene black with Dissolve(2)
            jump ch2sc29
        else:
            scene black with dissolve
            "You reach a tavern after a few miles."
            scene ch2sc28_26 with dissolve
            el "Ahh! Would you look at that! I knew a tavern was nearby!"
            scene ch2sc28_17 with dissolve
            mc "Oh, did you now? So what was all that talk about you never finding a bed again?"
            mc "That you would have to make your own bed out of leaves and carry it with you..."
            scene ch2sc28_28 with dissolve
            el "Okay. I may have been a bit dramatic... I was desperate, alright?"
            scene ch2sc28_29 with dissolve
            mc "You sure were."
            scene ch2sc28_30 with dissolve
            el "Hush! Let’s go inside and enjoy our evening!"
            scene ch2sc28_31 with dissolve
            mc "After you, m’lady."
            scene ch2sc28_32 with dissolve
            el "*Giggles* Why thank you. Such a gentleman."
            stop music fadeout 2.0
            scene black with Dissolve(2)
            jump ch2sc29

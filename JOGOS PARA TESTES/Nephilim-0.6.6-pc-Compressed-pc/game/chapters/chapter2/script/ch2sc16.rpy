#Start Chaper
label ch2sc16:

    #play music morning_1

    # start scene 2
        window hide dissolve
        play music morning_1 fadein 1.0
        scene black with Dissolve (2.0)
        scene ch2sc16_01 with Dissolve(2.0)
        $ renpy.pause()
        scene ch2sc16_02 with dissolve
        $ renpy.pause()
        scene ch2sc16_03 with dissolve
        $ renpy.pause()
        scene ch2sc16_04 with dissolve
        $ renpy.pause()
        scene ch2sc16_05 with dissolve
        mct "It’s been a while since I've dreamt about those days, about... her father."
        scene ch2sc16_06 with dissolve
        mct "His final words to me were... 'Find her, [mc]. Find her, and watch over her'."
        scene ch2sc16_07 with dissolve
        mct "Was that just a final plea from a regretful father, or is there more to it?"
        scene ch2sc16_08 with dissolve
        mct "Blazes... that old man! Always so cryptic and secretive."
        scene ch2sc16_09 with dissolve
        mct "I’ll protect her."
        mct "Not because you wanted me to, but because... I care about her."
        scene ch2sc16_10 with dissolve
        mct "Heh... she looks peaceful."
        scene ch2sc16_11 with dissolve
        $ renpy.pause()
        scene ch2sc16_11 with dissolve
        mct "How could someone as delicate and beautiful as Eliza be related to that old skeever?"
        mct "Her mother must've carried the gene pool, no doubt."
        scene ch2sc16_11 with dissolve
        ###Choice###
        menu:
            "Kiss her forehead.":
                scene ch2sc16_12 with dissolve
                $ renpy.pause()
                scene ch2sc16_13 with dissolve
                $ renpy.pause()
                scene ch2sc16_14 with dissolve
                $ renpy.pause(1)
                el "Nnhh..."
                scene ch2sc16_15 with dissolve
                $ renpy.pause(1)
                el "*Giggles softly* ..."
                scene ch2sc16_14 with dissolve
                $ renpy.pause(1)
                scene ch2sc16_12 with dissolve
                el "Hhrrmmm. What was that for?"
                scene ch2sc16_17 with dissolve
                $ renpy.pause(1)
                scene ch2sc16_18 with dissolve
                mc "Just felt like it."
                scene ch2sc16_16 with dissolve
                el "Is it morning already?"
                scene ch2sc16_15 with dissolve
                mc "Sadly, yes. I slept better than I have in a long time..."
                scene ch2sc16_16 with dissolve
                el "Mmmh... me too, I haven't felt this comfortable for as long as I can remember."
                scene ch2sc16_20 with dissolve
                mc "I could’ve easily slept until noon after yesterday's events."
                scene ch2sc16_19 with dissolve
                el "*Yawns* Yes! Let’s just have a little nap?"
                scene ch2sc16_21 with dissolve
                mc "Eliza..."
                mc "I'm afraid you'll have to postpone any naps."
                scene ch2sc16_16 with dissolve
                el "*Sigh* I know, I know."
                el "We have errands to run before we leave."
                scene ch2sc16_21 with dissolve
                mc "I have to visit an old family friend."
                scene ch2sc16_23 with dissolve
                mc "I suppose you could stay in bed a while longer."
                scene ch2sc16_24 with dissolve
                el "Uhh, can I? It’s just what I need!"
                scene ch2sc16_25 with dissolve
                el "My butt will love you for it!"
                scene ch2sc16_26 with dissolve
                mc "I’m sure it will... Just don’t nap too long."
                mc "You’re in charge of buying supplies from the market before we depart."
                scene ch2sc16_25 with dissolve
                el "I won’t forget!"
                scene ch2sc16_27 with dissolve
                el "I’ll make sure we have plenty of provisions, at least a week’s worth!"
                scene ch2sc16_28 with dissolve
                mc "Perfect, I’ll find you later."
                scene ch2sc16_29 with dissolve
                el "Byyee! Oh, say hi to your friend from me!"
                el "Tell him Eliza is watching your back so he won't have to worry!"
                scene ch2sc16_28 with dissolve
                mc "He doesn’t know who you are."
                scene ch2sc16_29 with dissolve
                el "*Giggles* I’m sure I'll meet him someday!"
                el "So you better put in a good word for me!"
                scene ch2sc16_28 with dissolve
                mc "*Chuckles* Sure... be ready with the provisions. We’re leaving as soon as I get back!"
                mc "We'll want to set out as early as possible to make some proper progress towards Luxenford."
                scene ch2sc16_29 with dissolve
                el "Yes, boss!"
                scene black with Dissolve(2)
                jump ch2sc17

            "Poke her.":
                scene ch2sc16_30 with dissolve
                $ renpy.pause(1.5)
                scene ch2sc16_31 with dissolve
                $ renpy.pause(1.5)
                scene ch2sc16_30 with dissolve
                $ renpy.pause(1.5)
                scene ch2sc16_31 with dissolve
                $ renpy.pause(1.5)
                scene ch2sc16_14 with dissolve
                $ renpy.pause()
                scene ch2sc16_15 with dissolve
                $ renpy.pause()
                scene ch2sc16_16 with dissolve
                el "Hrrhh. What time is it?"
                scene ch2sc16_17 with dissolve
                $ renpy.pause()
                scene ch2sc16_18 with dissolve
                mc "Time to get up, we have a bunch to do before we leave."
                scene ch2sc16_15 with dissolve
                $ renpy.pause()
                scene ch2sc16_16 with dissolve
                el "But I had such a nice dream!"
                scene ch2sc16_20 with dissolve
                mc "All good things come to an end. Let’s go."
                scene ch2sc16_16 with dissolve
                el "Urrh. Alright, alright!"
                scene ch2sc16_19 with dissolve
                el "*Yaawns*"
                scene ch2sc16_21 with dissolve
                mc "You’ll handle getting our provisions at the market, while I meet with an old family friend."
                scene ch2sc16_16 with dissolve
                el "Okay, I’ll make sure we’re well stocked!"
                scene ch2sc16_21 with dissolve
                mc "Good, See you later."
                scene ch2sc16_14 with dissolve
                el "..."
                scene ch2sc16_19 with dissolve
                el "Bye bye!"
                scene ch2sc16_23 with dissolve
                mc "Better not find you lazing around when I get back."
                scene ch2sc16_24 with dissolve
                el "What? Little ol’ me sleeping in? No chance!"
                scene ch2sc16_29 with dissolve
                el "Just out of curiosity, what would happen if I did?"
                scene ch2sc16_23 with dissolve
                mc "Your ass would be toast."
                scene ch2sc16_25 with dissolve
                el "Noo! Not my bum!"
                scene ch2sc16_27 with dissolve
                el "It feels nice and comfy just the way it is!"
                scene ch2sc16_25 with dissolve
                el "No need for any toasting around here!"
                scene ch2sc16_28 with dissolve
                mc "Bye!"
                scene ch2sc16_23 with dissolve
                mc "Oh, and I left some coins with Clark for the provisions. Just swing by when you’re dressed."
                scene ch2sc16_29 with dissolve
                el "Great! Will do!"
                stop music fadeout 2.0
                scene black with Dissolve(2)
                jump ch2sc17

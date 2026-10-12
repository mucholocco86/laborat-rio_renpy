# Start Chaper
label ch1sc1:

    #play music music_name
    stop music fadeout 2.0
    window show dissolve
    play music intro_1
    #show ch1sc0 with Dissolve (4.0)
    show namescreen_01 with fade

    "This is you. You have a long journey ahead, filled with adventure, friendship, love, lust, betrayal..."
    "But first you must decide on a name. How else will the bards write songs about your heroism?"
    "You are going to be a hero... right?"

# Player name
    python:
        mc = renpy.input("What is your name? Default is Noah")
        mc = mc.strip()
        if mc == "":
            mc = "Noah"
            persistent.mc = mc
        else:
            persistent.mc = mc

# start scene 1
    window hide dissolve
    scene black with Dissolve (2.0)

    #scene lewd_warning with dissolve
    #$ renpy.pause(2)
    #scene lewd_warning1 with dissolve
    #$ renpy.pause()
    #scene lewd_warning2 with dissolve
    #$ renpy.pause()
    #scene lewd_warning3 with dissolve
    #$ renpy.pause()
    #scene lewd_warning4 with dissolve
    #$ renpy.pause()
    #scene black with Dissolve (2.0)
    scene intro_1 with dissolve
    al "Hi there! I’m Alice. My boss, the developer, has asked me to meet you here!"
    scene intro_2 with dissolve
    al "He wanted me to give you a few details about the game, and how it plays."
    scene intro_3 with dissolve
    al "I’m sure a smart individual such as yourself can figure it out, no problem!"
    scene intro_4 with dissolve
    al "But he always reminds me that I have too much faith in people."
    al "So please bear with me!"
    scene intro_3 with dissolve
    al "Anywho... let’s get right to it!"
    al "As you totally already know, Nephilim is a {b}Medieval, Dark/High fantasy story.{/b}"
    al "It takes place in a world known as {b}Midomir{/b}, during a medieval time period."
    al "This means that you'll encounter various different species, such as gods and goddesses, angels and demons-"
    al "-Devils and fairies, dwarves and elves and so many more!"
    al "In Nephilim each species and kingdom has their own societal rules and beliefs they follow..."
    al "Human society is a Patriarchy which means it's dominated by men and favors them over women."
    al "Us women are often treated inferior to men or as a property of our spouses, while the men are free to do as they please."
    al "Can you believe it? Some women are sentenced to death for infidelity, while the men can take as many partners as they see fit?"
    al "So not fair! Ugh! Anyways, what this means for you is that you can pick and choose which of us girls you'd like to surround yourself with."
    al "You want only one of us? Great! You want to have a little fun on the side? Great! You want to marry all of us? Awesome!"
    al "During the story you will be able to make choices. BIG surprise, I know!"
    scene intro_4 with dissolve
    al "Some choices will {color=#00ff00}increase{/color} how much a person trusts you."
    al "While other choices can {color=#f00}decrease{/color} their trust in you!"
    scene intro_3 with dissolve
    al "Depending on how much they trust you, you may be able to romance some characters!"
    al "Trust will also be used to determine friendships and whether someone will help you on certain quests."
    scene intro_1 with dissolve
    al "Or some of them could betray you if their trust diminishes too much."
    al "That is definitely a possibility!"
    scene intro_2 with dissolve
    al "Other than trust, some choices will also build your personal morality towards {color=#87e1fa}Light{/color} or {color=#f00}Dark.{/color}"
    al "Each morality will have its own ending, and the boss assured me they will be quite different!"
    al "I should probably mention that most {color=#ff8cdd}romance{/color} options are neutral (available to both paths). However, there will be some that are tied to a specific path."
    scene intro_1 with dissolve
    al "Oh, and if you wish, you can hide/show the textbox by pressing *H* key, or pressing the middle mouse button."
    al "You know, in case you wish to have a better view!"
    scene intro_5 with dissolve
    al "Oh shoot! I didn’t realize how long I’ve been yapping on for!"
    scene intro_6 with dissolve
    al "I’m so sorry! We’ll probably see each other again..."
    scene intro_7 with dissolve
    al "Please, it’s time for your adventure in Midomir to begin. Enjoy!"
    scene intro_8 with dissolve
    with vpunch
    al "Ow! Who forgot to put the books away? This place is a mess!"
    al "How am I supposed to get to lunch in time with all of you making such a mess!?"
    scene black with Dissolve(2)
    stop music fadeout 1.0
    $ renpy.pause(1)
    play music mmm_elven_forest fadein 1.0
    scene ch1sc1_01b with Dissolve(4)
    $ renpy.pause(1)
    mct "We should be cooking the mushrooms we foraged earlier."
    mct "It's been twenty minutes since I got the fire going... how long does she need to bathe?"
    scene ch1sc1_01c with dissolve
    $ renpy.pause(1)
    mct "The lake we passed earlier is only about five minutes away..."
    mct "Maybe I'll go look for her, I'm famished."
    scene black with Dissolve(2)
    $ renpy.pause(1)
    scene ch1sc1_01d with Dissolve(4)
    $ renpy.pause()
    mc "There you are..."
    scene ch1sc1_01e with dissolve
    $ renpy.pause()
    el "Here I am..."
    scene elmc_1 with Dissolve(2)
    $ renpy.pause(1)
    "As you arrive at the lake you're met with the sight of Eliza bathing under the moonlight."
    mct "Five hells... she's not even out of the water or getting dressed yet."
    mc "I'm hungry... I've got the fire going."
    el "Nice!"
    "Eliza's belly rumbles..."
    el "You didn't hear that!"
    mc "*Chuckles* You're still getting shy about me hearing your stomach growling?"
    mc "It happens several times a day with how little we've been eating."
    el "I-I'm a woman!"
    el "A woman's stomach never growls! I've told you this!"
    mc "Right... and you never snore either."
    el "Exactly! *Giggling*"
    el "But you do! Biiiiig time!"
    mc "I wouldn't know."
    el "Then you'll have to take my word for it."
    mc "And you'll have to take me for my word when I say... hurry up."
    el "*Giggling* Or what?"
    mc "Or I'll get in the water... grab you... carry your ass back to camp."
    el "See... you think you're threatening me, but really you're just making me a promise!"
    mc "*Exhales* Eliza... I'm starving, you must be as well."
    el "Mmh... I won't take much longer."
    el "Did you see all the mushrooms I managed to gather?"
    mc "Yeah, you did well."
    mc "While mushrooms don't exactly make me salivate... it'll be filling enough until we reach Riverside."
    el "I think I know something that does make you salivate though..."
    el "*Giggling* Mmh!"
    mc "How's your leg?"
    mc "You took quite the tumble earlier when you were climbing that rock."
    el "Oh it's fine, really."
    el "I might get a tiny bruise but I didn't twist anything."
    mc "Good."
    el "Awwh! Look at you being all worried about me!"
    mc "You know I do."
    el "MMh... I know."
    el "It's still quite nice though, when you reveal it."
    el "We'll arrive at Riverside tomorrow, correct?"
    mc "Tonight."
    el "*Gasps* Tonight!? But it's already dark?"
    mc "We're not that far, we'll just have dinner and rest for a bit."
    el "Okay, go back and throw the mushrooms on those rocks near the fire while I finish up."
    el "That should sear them nicely and gives me a few minutes to dry off and get dressed."
    mc "Alright, I'll see you in a few then."
    scene black with Dissolve(2)
    $ renpy.pause(1)
    scene elmc_intro1 with Dissolve(4)
    window show dissolve
    $ renpy.pause(1)
    mct "{i}...{/i}"
    mct "{i}Ten summers...{/i}"
    mct "{i}Ten summers... And ten winters, since I've been back here.{/i}"
    elt "{i}*Exhales* Hnnghh... My legs are killing me, we've been on the road for several days.{/i}"
    elt "{i}Sleeping on the ground and foraging for mushrooms and berries... not exactly pleasant.{/i}"
    elt "{i}I wonder why we stopped, does he want to setup camp for the night?{/i}"
    elt "{i}No, that can't be it, he said earlier we were relatively close.{/i}"
    $ renpy.pause()
    scene ch1sc1_03 with dissolve
    mc "Eliza, we're here."
    scene ch1sc1_02 with dissolve
    el "Here? Already?"
    el "So this is Riversi-"
    scene ch1sc1_03 with dissolve
    mc "Home..."
    mc "It used to be my home. A long time ago..."
    scene ch1sc1_04 with dissolve
    el "How does it feel to see it again?"
    el "Does it bring back a lot of memories?"
    scene ch1sc1_05 with dissolve
    mc "..."
    "You remain silent, contemplating what to say."
    "You feel something touching your hand."
    scene ch1sc1_06 with dissolve
    "Eliza gently places her hand in yours, squeezing softly."
    "Her small fingers seem to fit perfectly between yours."
    scene elmc_intro2 with dissolve
    el "I'm not going anywhere... take your time."
    mc "It... it feels different. I don't belong here anymore."
    mc "The place itself... it looks the same as it did back then."
    mc "But I've changed... So much has changed."
    elt "{i}I wish I could do something more to comfort him.{/i}"
    scene ch1sc1_08 with dissolve
    mct "{i}I'm not the little boy who used to live here anymore...{/i}"
    mct "{i}I was so naive back then. Adventure this... treasure that...{/i}"
    scene ch1sc1_04 with dissolve
    el "[mc]... What happened back then?"
    scene ch1sc1_02 with dissolve
    el "I can see the pain all over your face, you hide it well..."
    el "But, you don't need to hide it from me."
    el "Not after what we've been through."
    scene elmc_intro2 with dissolve
    mc "Eliza..."
    el "[mc]... I'm here with you. No going back, remember?"
    el "We've got each other's backs."

    #Choice 0a-0b
    menu:
        "Share your past with Eliza.":
            $ eliza_trust += 1
            mc "*Sighs* I've come to understand how stubborn you can be..."
            el "*Giggles softly* You should be used to it by now!"
            mc "So where should I even begin?"
            scene elmc_intro1 with dissolve
            elt "{i}It seems he's finally comfortable enough with me to share his past.{/i}"
            elt "{i}This is a big step for him... It means the world to me that he's willing to let me in.{/i}"
            scene elmc_intro2 with dissolve
            el "It's okay... Take your time."
            el "Start from the beginning. *Softly squeezes your hand* And pause if you need to."
            "Eliza appreciates you sharing this with her."
            "Eliza's trust has increased by {size=+3}{b}{color=#2bff8b}1{/color}{/b}{/size}."
            mc "It all began the day of my tenth summer..."
            scene black with Dissolve (2.0)
            jump ch1sc2

        "Tell Eliza to leave it alone.":
            scene ch1sc1_03 with dissolve
            mc "Leave it alone Eliza... I don't want to talk about it."
            scene elmc_intro1 with dissolve
            elt "{i}Why won't he open up to me?{/i}"
            elt "{i}We've been through a lot together in a short amount of time. *Sighs* I'll have to be patient.{/i}"
            elt "{i}I wouldn't like to be pushed on a sensitive subject either... When he's ready, I'll be here.{/i}"
            scene ch1sc1_02 with dissolve
            el "I'm sorry, okay? I won't press the matter further..."
            el "Just know I'm here for you, [mc]."
            scene ch1sc1_03 with dissolve
            mc "... You don't have to feel sorry, I'm just not ready to talk about it."
            scene ch1sc1_03 with dissolve
            mc "Let's go. It's been close to a week since we had a proper meal."
            scene ch1sc1_02 with dissolve
            el "Or a proper bed! As much as I love the starry nights-"
            el "I'm afraid my back won't endure another night on the cold ground."
            scene ch1sc1_07 with dissolve
            mct "{i}All these memories... That day ten summers ago changed everything...{/i}"
            scene black with Dissolve (2.0)
            #stop music fadeout 2.0
            jump ch1sc2

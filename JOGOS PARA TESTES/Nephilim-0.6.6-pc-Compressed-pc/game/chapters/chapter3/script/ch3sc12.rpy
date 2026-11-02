
label ch3sc12:

    window hide dissolve
    play music explore_1 fadein 1.0
    scene black with Dissolve (2.0)
    scene ss16 with Dissolve(2.0)
    $ renpy.pause()
    scene ch3sc12_001 with Dissolve(2.0)
    $ renpy.pause(1)
    sy "*Humms softly*"
    scene ch3sc12_002 with dissolve
    syt "..."
    show sylph_idle1 with fade
    $ renpy.pause(2, hard=True)
    syt "I wonder if they are doing alright?"
    syt "The quest should be pretty straightforward, from what I could tell."
    syt "And [mc]... he has so much magic within him."
    syt "I'm sure they're fiiiiine."
    syt "Would he? Mmhm, no! There's no way he would be interested in someone like me, right?"
    syt "I'm just a silly fae, confined to this guild."
    syt "What use could I be to someone like him?"
    scene ch3sc12_002 with dissolve
    $ renpy.pause(1.2)
    scene ch3sc12_003 with dissolve
    el "Hiii Sylph! We’re back!"
    scene ch3sc12_004 with dissolve
    sy "Oh my! You guys sure work fast!"
    scene ch3sc12_005 with dissolve
    syt "See? I knew they'd handle it, easy peasy!"
    scene ch3sc12_006 with dissolve
    sy "Seems like Dalen has sized you up perfectly!"
    scene ch3sc12_007 with dissolve
    $ renpy.pause()
    scene ch3sc12_008 with dissolve
    el "Are you saying you didn’t have faith in us?"
    scene ch3sc12_009 with dissolve
    sy "No way!"
    sy "I totally had faith!"
    scene ch3sc12_010 with dissolve
    sy "Yuuuup, yup, yup!"
    sy "That’s me, the little ole faith-fae!"
    scene ch3sc12_011 with dissolve
    el "Riiiight..."
    scene ch3sc12_012 with dissolve
    mc "Sylph, was there any reward for this quest? Or was it just a trial run?"
    scene ch3sc12_013 with dissolve
    sy "Oh! Right! Right, right, right!"
    scene ch3sc12_014 with dissolve
    sy "Just a moment!"
    scene ch3sc12_015 with dissolve
    $ renpy.pause()
    scene ch3sc12_016 with dissolve
    sy "It should be right over here. I remember placing it here earlier."
    scene ch3sc12_017 with dissolve
    sy "You’ve definitely earned a reward. A raven came by earlier with a letter stating your work was satisfactory."
    sy "Dalen will be very pleased with your success!"
    sy "So am I, in fact!"

    if eliza_relationship == True:
        scene ch3sc12_018 with dissolve
        elt "She’s got to be doing this on purpose."
        scene ch3sc12_019 with dissolve
        elt "Calm down, Eliza."
        elt "It’s Sylph... She might be a bit aloof but she’s a fae!"
        elt "It’s not like she'd intentionally try to seduce [mc]. Right?"
        elt "Then again... she's perking her ass all over the place? Hnngh!"
        scene ch3sc12_020 with dissolve
        sy "Here, ten silvers! I know it’s not much, but it was only a D-Rank quest."

    elif True:
        scene ch3sc12_020 with dissolve
        sy "Here, ten silvers! I know it’s not much, but it was only a D-Rank quest."

    scene ch3sc12_021 with dissolve
    $ renpy.pause()
    scene ch3sc12_022 with dissolve
    el "Are you kidding me, Sylph? This is great!"
    scene ch3sc12_023 with dissolve
    sy "Here you go, [mc]."
    "As Sylph hands you the coins, her tiny fingers stroke your hand gently."
    scene ch3sc12_024 with dissolve
    "Her fingers are so elegant to the touch, you can even feel the magic essence flowing within her fingertips."
    mc "Thank you, Sylph."
    scene ch3sc12_025 with dissolve
    $ renpy.pause()
    scene ch3sc12_026 with dissolve
    sy "No, [mc]. Thank you for joining us. We need this as much as you do."
    sy "It means... it means a lot."
    scene ch3sc12_027 with dissolve
    sy "Now get outta here you two!"
    sy "You're new to town. I'm sure there's a bunch of things you want to do!"
    scene ch3sc12_028 with dissolve
    sy "But remember to check back tomorrow. There might be a new quest available then!"
    scene ch3sc12_029 with dissolve
    mc "Will do, Sylph. Give Dalen our regards."
    scene ch3sc12_030 with dissolve
    sy "Sure thing. I can't wait to tell him of your success! See you tomorrow!"
    stop music fadeout 2.0
    scene black with dissolve
    $ renpy.pause(1.2)
    scene ch3sc12_031 with dissolve
    play music tavern_2 fadein 1.0
    el "*Stretches* Mhh! Can you feel it?"
    el "Mmmh! It feels just wonderful!"
    scene ch3sc12_032 with dissolve
    mc "Feel what?"
    el "*Giggling happily*"
    scene ch3sc12_033 with dissolve
    el "The success of our first quest, silly!"
    el "It went much better than we could have hoped for."
    scene ch3sc12_034 with dissolve
    mc "Yeah it was rather straightfoward, and we got paid a decent amount."
    mc "It does feel good, can't deny that."
    scene ch3sc12_035 with dissolve
    el "Even if you tried to deny it, your smile tells me all I need to know!"
    el "Your loving every moment of being an adventurer! As do I for that matter!"
    scene ch3sc12_034 with dissolve
    mc "I'm glad you're taking a liking to it, this is what I've always wanted to do."
    mc "Why don’t you head over to the tavern we passed by earlier, and make sure there’s a room for us tonight?"
    scene ch3sc12_035 with dissolve
    el "Great idea!"
    el "I was hoping we could've stayed at the guild..."
    scene ch3sc12_036 with dissolve
    el "But Sylph said they were renovating the sleeping quarters."
    el "I suppose it'll be a while till we can leave tavern beds behind us."
    scene ch3sc12_034 with dissolve
    mc "We’ll make do with taverns for now."
    mc "I didn’t expect our first reward to be so generous, though."
    scene ch3sc12_036 with dissolve
    el "Same! Ten silvers for a D rank quest?"
    el "We’ll be rich in no time if it’s always like this. *Giggles*"
    el "Think about all the things we could buy after a few quests!"
    scene ch3sc12_037 with dissolve
    el "But I'm getting ahead of myself."
    el "Okay. I’ll head over and get us a room before they’re all taken."
    scene ch3sc12_038 with dissolve
    mc "Sounds good. I’ll find you later."
    scene ch3sc12_039 with dissolve
    el "Oh, wait! W-Would it be completely shameless of me to spend a few silvers on a new outfit?"
    el "I saw this really cute outfit earlier when we passed by a store, and it looks practical too!"
    scene ch3sc12_040 with dissolve
    el "I know we don’t have much."
    ###Choice###
    menu:
        "Sure, go get yourself geared up." if True:
            scene ch3sc12_041 with dissolve
            mc "I don’t see why not."
            mc "You’ve been training hard and did well on our first quest."
            scene ch3sc12_042 with dissolve
            mc "Go on, pick out something you really like."
            mc "But before you buy it, remember to try it on."
            mc "You have to be nimble in it, that's one of your strengths."
            scene ch3sc12_043 with dissolve
            el "R-Really?! {b}Yay!{/b}"
            scene ch3sc12_044 with dissolve
            with vpunch
            el "{b}You’re the best!{/b}"
            el "Thank you, [mc]! Thank you, thank you!"
            el "I promise I'll test it before buying anything! I can't wait to show you!"
            scene ch3sc12_045 with dissolve
            "She plants her soft wet lips on your cheek in excitement, while she caresses your cheek."
            el "{b}Mwaaah!{/b}"
            scene ch3sc12_046 with dissolve
            el "See you later at the tavern, handsome."
            "Eliza is excited that you encouraged her, her trust has increased by {size=+3}{b}{color=#2bff8b}1{/color}{/b}{/size}."
            $ eliza_trust += 1
            scene ch3sc12_047 with dissolve
            mc "See you."

        "Not a good idea, but we each have five Silvers." if True:
            scene ch3sc12_041 with dissolve
            mc "I don’t think it’s wise to spend what little coin we have on outfits."
            scene ch3sc12_042 with dissolve
            mc "But we have five silvers each to spend, so I won’t stop you."
            mc "Just remember to have enough left over for the room tonight."
            scene ch3sc12_043 with dissolve
            el "Trust me! Once you see my new outfit you will regret hesitating!"
            scene ch3sc12_047 with dissolve
            mc "Whatever you say... Catch you later."

    scene black with Dissolve(2)
    stop music fadeout 2.0
    jump ch3sc13

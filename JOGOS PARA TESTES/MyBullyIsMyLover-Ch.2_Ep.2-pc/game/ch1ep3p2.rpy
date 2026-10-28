label ep3part2:
    scene ch1ep3p2
    with dissolve
    pause
    show screen day_friday with dissolve
    play music 'audio/IfItMatters.mp3'
    if allornothingroute:
        scene ch1ep3p2_1
        with Dissolve(1.0)
        yt "Weeks flew by since that talk with the girls..."
        yt "But I can't shake this... funky feeling, like something's been off ever since that day."
        yt "I expected them to start fighting over me or something."
        yt "But nothing ever happened."
        yt "It's like something's bugging them, yet nobody can put a finger on exactly what."
        yt "It's eerie."
        yt "I mean... they look and act like their normal selves. So, everything should be fine and dandy, right?"
        yt "Maybe it's just my mind playing tricks on me?"
        yt "But the air does feel strangely heavier as if harder to breathe..."
    else:
        scene ch1ep3p2_1
        with Dissolve(1.0)
        yt "Weeks passed by..."
        yt "I can't explain this funky feeling, like something has changed with everyone."
        yt "It's like something's nagging at them... but nothing's really popped up."
        yt "It's just unsettling."
        yt "I mean... they look and act like their normal selves. So, no alarms, right?"
        yt "Maybe... I'm reading into things too much?"
        yt "But the air does feel weirdly dense as if harder to breathe..."

    scene ch1ep3p2_2
    with dissolve
    yt "So... Lily, Freya, and Moon finally graduated."
    yt "Lily's really excited about it, but Moon's sort of lost about what to do next."
    scene ch1ep3p2_3
    with dissolve
    yt "Freya had it tough keeping up with her studies after moving out from Hera's, but hey, it's Freya - no sweat for her in the end."
    play sound airportambience loop fadein 4
    scene ch1ep3p2_4
    with dissolve
    yt "Lily wanted to stay, but her relative's offer... it was something she had to accept."
    yt "I suppose it's better this way, right? Putting her future first before her ties here."
    yt "Nothing you can do besides stand by her choice."
    yt "Shu said he had to go back overseas, too. Says he can't leave his stuff hanging."
    yt "Letting him go just like Lily... it's rough."
    yt "But it was bound to happen at some point... guess it's time to say our goodbyes..."
    stop music fadeout 3
    $ renpy.sound.set_volume(0.5, 1.0)
    play music2 'audio/SweetGoodbye.mp3' fadein 3 loop
    scene ch1ep3p2_5
    with dissolve
    mc "*sighs* You didn't even get a chance to finish your story."
    scene ch1ep3p2_6
    with dissolve
    l "Yeah... I promised, didn't I?"
    mc "Yeah, you did."
    scene ch1ep3p2_7
    with dissolve
    l "Well, you know what they say: promises are meant to be broken."
    scene ch1ep3p2_8
    with dissolve
    l "But you know what, [mc]?"
    l "Let's save it for when we meet again."
    mc "*chuckles* Even your speech has changed."
    mc "But yeah, one of these days, I'll come find you."
    mc "This time, I promise you."
    l "I'll hold you to that."
    scene ch1ep3p2_9
    with dissolve
    mc "..."
    scene ch1ep3p2_10
    with dissolve
    mc "Can't believe you're actually bouncing, dude. I knew you wouldn't stay long, but still..."
    shu "I know. Sorry, I didn't mention it sooner."
    shu "It was brief, but I had a blast, [mc]. Thanks for another batch of unforgettable memories."
    shu "I kept thinking I'd wake up and we'd be ready for our next adventure together."
    shu "It's a whole rollercoaster of emotions, isn't it?"
    mc "I'm damn proud of you, man. But I also wish I could steal a few more moments with you here."
    scene ch1ep3p2_11
    with dissolve
    shu "Ah shit... Don't do that to me, dude! I'm about to leave, for fuck's sake!"
    scene ch1ep3p2_12
    with dissolve
    mc "Yeah... But hey, the day's here. Doesn't make it easier, but we promise to have each other's backs, right?"
    shu "Always have, and we always will. It's just... \"see you later\" has always been the hardest part."
    mc "Indeed. But we got this. It's not goodbye, it's \"see you later\"."
    shu "Yeah, \"see you later\"..."
    scene ch1ep3p2_13
    with dissolve
    mc "Promise to FaceTime me from your new place ASAP? And to send me a ton of annoying travel texts?"
    shu "Hah, sure!"
    shu "Only if you promise to send me a care package with our favorite stuff and a ridiculously long letter for when I'm homesick."
    scene ch1ep3p2_14
    with dissolve
    mc "Deal, buddy."
    shu "Take care of yourself, okay?"
    mc "You too. Safe travels, dude."
    scene ch1ep3p2_15
    with dissolve
    f "*sniffs*"
    scene ch1ep3p2_16
    with dissolve
    l "Aww... Don't cry, Frey. It's not the end, you know?"
    l "Think of this as closing a chapter. You have to keep going and open the next one without me."
    l "Like [mc] said, I'll FaceTime you as soon as I get to my new place. Sound good?"
    scene ch1ep3p2_17
    with dissolve
    f "Okay... I know you'll be busy, but try to do it as often as possible."
    l "*giggles* I'll do my best."
    scene ch1ep3p2_18
    with dissolve
    l "Anyway, it's your turn for college, isn't it?"
    f "Yeah, but I think I'll hold off for a bit. Gonna focus on streaming and saving up."
    l "Then I'll be cheering you on. Good luck, Frey. I'm rooting for you."
    f "Thanks, Lil."
    scene ch1ep3p2_19
    with dissolve
    l "..."
    scene ch1ep3p2_20
    with dissolve
    l "I guess I should head out."
    mc "Mhm. Take care, Lily."
    l "See you later, guys."
    f "See you another time, Lil!"
    scene ch1ep3p2_21
    with dissolve
    shu "*sniffs* Byeee~!"
    shu "Goodbyeeeee~!"
    stop music2 fadeout 3
    $ renpy.sound.set_volume(1.0, 1.0)
    scene ch1ep3p2_22
    with dissolve
    mc "..."
    shu "Byee~!"
    scene ch1ep3p2_23
    with dissolve
    mc "Shu..."
    shu "..."
    mc "Hey..."
    scene ch1ep3p2_24
    with dissolve
    shu "Hm?"
    mc "... You're not leaving, are you?"
    scene ch1ep3p2_25
    with dissolve
    shu "Nope! Why would I?"
    mc "I want my tears back..."
    shu "Nope! Why would I?"
    mc "Give them back..."
    shu "You stole my dignity. Now we're even."
    scene ch1ep3p2_26
    with dissolve
    mc "Give. Them..."
    play sound2 woodcrash
    show ch1ep3p2_27
    with hpunch
    play sound3 bonebreak
    mc "Baaaack!"
    stop sound fadeout 2

    if naomiroute:
        scene black
        with dissolve
        with fade

        play sound carmoving loop
        play sound2 traffic loop
        scene ch1ep3p2_28
        with dissolve
        f "You think she'll be okay?"
        mc "Honestly? I'm not sure. But Lily's never been one to back down, so she'll probably be fine."
        mc "Let's just keep our fingers crossed, yeah?"
        f "Yeah..."
        play sound3 phonevibrate loop
        scene ch1ep3p2_29
        with dissolve
        pause
        mc "Ugh... I'm driving."
        shu "What?"
        mc "I'm getting a call."
        shu "I got it. Which pocket?"
        mc "Right side."
        scene ch1ep3p2_30
        with dissolve
        shu "Hold on..."
        mc "... The other right. Where do you think you're reaching?"
        shu "Oops, wrong phone."
        scene ch1ep3p2_31
        with dissolve
        shu "..."
        shu "It's Klara."
        mc "Answer it for me."
        play sound3 phoneclick
        scene ch1ep3p2_32
        with dissolve
        k "[mc]?"
        mc "Hey, Klara. What's going on?"
        k "Am I interrupting?"
        mc "Sort of. I'm driving right now."
        k "Oh, I'm sorry, dear. I just wanted to quickly ask if you'll be home for lunch."
        mc "Yeah, we will! We're actually on our way now."
        k "Oh, great! Drive safe, honey!"
        mc "Thanks. See you soon."
        play sound3 phoneclick
        scene ch1ep3p2_33
        with dissolve
        mc "Let's hu-"
        play sound3 phonevibrate loop
        scene ch1ep3p2_34
        with Dissolve(0.2)
        shu "\"Fixin' Ye Pipes\" is calling..."
        scene ch1ep3p2_35
        with Dissolve(0.2)
        shu "Who the fuck is this?!"
        mc "More importantly, why are you acting like my girlfriend?"
        mc "Anyway, it's Naomi. Pick it up."
        play sound3 phoneclick
        scene ch1ep3p2_36
        with dissolve
        shu "Alright. Go ahead."
        mc "Hey Naomi! Forget something?"
        n "Yeah, mate. Got sidetracked these past few weeks."
        mc "No worries. I've been swamped, too."
        mc "So what's up?"
        n "Would it be too much trouble to ask you to come by now? I'm workin' on somethin' and could use some big hands."
        mc "Now you've piqued my curiosity..."
        menu:
            "Go home for lunch":
                $ naomiroute = False
                mc "... But I can't. Klara just called me home for lunch."
                n "No worries. I'll figure something out. Take care, mate."
                mc "You too."
                scene ch1ep3p2_37
                with dissolve
                yt "... I sensed a hint of frustration in that response."
                yt "She was looking forward to it, huh?"
                jump naomifirstarcend
            "Satisfy your curiosity":
                $ naomiroute = True
                mc "... Yeah, why not! You've made me curious."
                mc "I have some of the gang with me, though. I need to drop them off first."
                n "Take your time, mate. I ain't goin' anywhere."
                n "And hey, about that dinner... how about we make it lunch instead?"
                mc "Ohh, works for me!"
                n "Cool. I'll be waitin'."

        scene ch1ep3p2_38
        with dissolve
        shu "Naomi, huh... She's always nice to me."
        f "She is to everybody. But sometimes, I can barely keep up with her when she talks."
        shu "Same here."
        mc "You'll get the hang of it. Just give it some time."
        shu "Is it just me, or does her voice kinda make you wanna relax and doze off? Ever notice that?"
        mc "*chuckles* It's not just you."
        shu "She could make a killing recording audiobooks. Haha!"
        mc "Pretty sure I said the exact same thing once."
        stop sound2 fadeout 2
        stop sound fadeout 2

        scene black
        with dissolve
        with fade

        play sound cardoorclose
        play sound2 parkwind loop
        scene ch1ep3p2_39
        with dissolve
        pause
        play music 'audio/YouMeanTheWorld.mp3'
        show naomigarageshowcase
        with dissolve
        pause 8.5
        scene ch1ep3p2_40
        with dissolve
        n "Nice truck, mate."
        mc "It's technically not mine, but I figured you might've scoped it out already."
        n "Not up close."
        scene ch1ep3p2_41
        with dissolve
        mc "... You've got less stuff in here than last time. What happened?"
        scene ch1ep3p2_42
        with dissolve
        n "Ahh, that lot?"
        n "Couple of smaller industrial companies have been buyin' our junk. One recently did a bulk buy, and what ya see's what's left."
        n "To be real, they could've taken it all. Managin' this lot without the old man's been a bit of a slog."
        scene ch1ep3p2_43
        with dissolve
        mc "Missing him already?"
        n "*chuckles* No way. I've got a lot more freedom without him hoverin' about. He can stay out in the countryside for all I care."
        n "And I reckon Mum won't let him pop back too quickly either. He was havin' a ripper of a time just stickin' 'round the capital."
        scene ch1ep3p2_44
        with dissolve
        mc "Yeah, I recall you folks run a coffee farm, too."
        mc "Hope your Mum doesn't give him too hard a time."
        scene ch1ep3p2_45
        with dissolve
        n "It'd do him good, in my book."
        n "No pain, no gain, right?"
        mc "Wouldn't be my choice with a bunch of broken bones, that's for sure..."
        scene ch1ep3p2_46
        with dissolve
        n "Over here, mate. I'll show ya."
        mc "Ah, the thing you've been on about."
        yt "God, her skin under sunlight is just glistening white."
        scene ch1ep3p2_47
        with dissolve
        n "Wanna have a stab at what it is?"
        mc "..."
        mc "You're not very good at surprises, are you?"
        mc "What could be in there aside from some kind of vehicle?"
        play sound woosh
        show ch1ep3p2_48
        n "{cps=25}Oi, don't be so quick to judge, mate! What if I've been workin' on a bloody smart AI robot, eh? Not some bloody tin can, but somethin' with a bit o' wit!"
        play music 'audio/AUAnthem.mp3'
        show ch1ep3p2_49
        pause 0.2
        show australia
        with Dissolve(5.0)
        play music 'audio/YouMeanTheWorld.mp3'
        show ch1ep3p2_50
        mc "A robot... huh?"
        n "Righto! But not just any ol' robot."
        n "Imagine an AI so bloody advanced it learns and adapts, and reckon, one day, could have the whole world under its shiny metal boot."
        n "Me own little creation could be the brains of the future - or the boss of us all!"
        mc "Sounds like a sci-fi movie ready to roll. Just promise me it'll remember us little guys in a good light?"
        n "Can't make any promises, mate, but I'll slip in a good word for ya!"
        mc "You're a real comfort, y'know that?"
        mc "And there goes your accent slipping out of nowhere again..."
        mc "You're excited, aren't you?"
        scene ch1ep3p2_51
        with dissolve
        n "*chuckles* Not really. Maybe. It's classified."
        scene ch1ep3p2_52
        with dissolve
        n "Anyway, here she is."
        mc "She...?"
        play sound doorcreak2
        scene ch1ep3p2_53
        with dissolve
        pause
        mc "Dodge Challenger SRT, huh? Now that's what I like to see!" #whistles
        n "It is a Dodge Challenger SRT, but may I ask if ya know what model?"
        menu:
            "Dodge Challenger SRT 392":
                mc "Of course! That'd be the 392!"
                n "Sorry, mate. It's the Demon."
                n "The 2018 Demon, to be precise."

            "Dodge Challenger SRT Demon":
                mc "That'd be none other than the Demon. Quite a beast from what I've heard."
                $ naomipoint += 1
                $ renpy.notify(naominotif)
                n "Spot on, mate! You've got a keen eye."
                n "It's the 2018 Demon, to be more precise."

            "Dodge Challenger SRT Hellcat":
                mc "Of course! That'd be the Hellcat!"
                n "Sorry, mate. It's the Demon."
                n "The 2018 Demon, to be precise."

        scene ch1ep3p2_54
        with dissolve
        n "She's one helluva machine."
        n "Packed with a supercharged 6.2-liter V8, she belts out a whopping 840 horses with the right fuel, and she'll catapult ya from nought to 60 in a mere 2.3 seconds."
        n "Ain't she a beauty? More than just a car, she's a ferocious beast on wheels."
        mc "I'd say that's quite impressive, but \"beauty\" isn't the right word to describe it at the moment."
        mc "More like... rusty."
        yt "... I could probably rev things up a few horsepower."
        menu:
            "Crank it up":
                scene ch1ep3p2_55
                with dissolve
                mc "I must admit, it looks a bit weathered. But... there's an undeniable charm seeing you there in the driver's seat."
                $ naomipoint += 1
                $ renpy.notify(naominotif)
                n "Aw, ya reckon? Tryin' to sweet-talk me won't save this ol' girl from a good polish, mate."
                mc "I wasn't planning on it. But you must admit, a beautiful driver can make any car shine, rust and all."
                n "You're a smooth talker, ain't ya?"
                n "I've clocked it, y'know, all the sheilas hangin' 'round ya."
                n "But like I said, mate, I just-"
                scene ch1ep3p2_56
                with Dissolve(0.2)
                mc "I get it. You're not looking for anything serious. And I respect that, really."
                mc "But is it wrong for a guy to compliment a pretty lady without any ulterior motives?"
                scene ch1ep3p2_57
                with dissolve
                n "*chuckles* No, it's not, and that's a bit of a relief, honestly."
                n "I don't want to hurt ya, mate. Especially not a top bloke like ya."
                mc "I see."
                yt "She doesn't want to hurt me, huh... I wonder why..."
            "Better be safe":
                yt "I can tell there's more than just mechanical passion in her eyes when she talks about this machine..."
                yt "She made it clear she's not into commitments, and throwing compliments around might just muddle things between us."
                yt "I value our friendship too much to risk it over a misinterpreted compliment."

        scene ch1ep3p2_58
        with dissolve
        mc "Well... she sure could use a bit of TLC!"
        play sound cardoorclose
        scene ch1ep3p2_59
        with Dissolve(0.2)
        n "The paint job can wait. We've got a bigger snag than that."
        mc "She can't run?"
        scene ch1ep3p2_60
        with dissolve
        n "What's it look like to ya?"
        mc "She's a no-go, then..."
        scene ch1ep3p2_62
        with Dissolve(0.5)
        pause 0.2
        scene ch1ep3p2_61
        with Dissolve(0.4)
        pause 0.2
        scene ch1ep3p2_62
        with Dissolve(0.2)
        pause
        scene ch1ep3p2_63
        with dissolve
        n "Aside from that, she's missin' a couple of key components here."
        n "First off, the glass - she's got no side windows or windshield. Crucial, not just for aerodynamics but safety as well."
        n "The headlights and taillights are gone, which not only makes her unroadworthy but also bloody unsafe."
        n "Can't have her blind and invisible on the roads."
        mc "That's a fair point. These are essential parts we're talking about."
        scene ch1ep3p2_64
        with dissolve
        n "Exactly, and don't get me started on the trunk cover. That's just leavin' the rear exposed."
        n "Plus, it messes with the overall aesthetic and function, doesn't it?"
        scene ch1ep3p2_65
        with dissolve
        mc "Absolutely, and I guess the interior needs quite a bit of attention too?"
        n "You hit the nail on the head."
        n "The interior is lackin' in a few spots as well - missing a bit of the dashboard, seat belts are shot, and the seats themselves have seen better days."
        n "It's not just makin' her look pretty; it's preservin' and enhancing what's under the hood by making sure every other component is up to snuff."
        mc "Totally get it. A car like this deserves to be restored to its former glory, with each part playing its role."
        mc "Although... It's going to be quite the project. Nevertheless, you know your stuff."
        scene ch1ep3p2_66
        with dissolve
        mc "... Wait, we're here talking about it like this car's a normal thing for people to have."
        mc "Where did you get her in the first place?"
        stop music
        show ch1ep3p2_67
        n "..."
        scene ch1ep3p2_68
        with dissolve
        n "That's... a story for another time, mate."
        mc "... A-alright."
        scene ch1ep3p2_69
        with dissolve
        yt "Why did she suddenly pause like that? It's like I hit on something..."
        play music 'audio/BeerBeardsBBQ.mp3'
        play sound carhoodopen
        scene ch1ep3p2_70
        with dissolve
        n "Anyway, here's our problem."
        mc "The engine? It looks alright to me! Heck, it even looks brand new!"
        n "That's because it already had some of yer so-called TLC."
        scene ch1ep3p2_71
        with dissolve
        n "I tried to start her a few days ago, but I noticed an unusual vibration and an odd, rhythmic tickin' noise."
        mc "And... that means?"
        scene ch1ep3p2_72
        with dissolve
        n "There's an issue with the crankshaft."
        n "Crankshafts are crucial for convertin' the pistons' up-and-down movement into rotational motion to drive the vehicle."
        n "There might be some kind of damage to it causin' the unusual noise."
        mc "Oh, I see... I think? At least I'm learning from you."
        mc "So what do we do with it?"
        scene ch1ep3p2_73
        with dissolve
        n "I'm afraid we'll have to do a full engine pull. That's where your muscles will come into play."
        mc "Now it all makes sense."
        image namctadodgeengp:
            "ch1ep3p2_74.jpg"
            pause 3.0
            "ch1ep3p2_75.jpg"
            pause .2
            repeat
        show namctadodgeengp
        with dissolve
        n "No matter how small the damage is, it could spell disaster on the track."
        n "Besides the crankshaft issue, the crankcase, bearings, and possibly the connecting rods could be at risk or compromised."
        n "The whole engine needs to be taken out to conduct a thorough inspection and ensure that no collateral damage has affected other components."
        mc "Let's say the crankshaft is damaged: then you'll have to replace it."
        mc "It'll be damn expensive considering this beast's manufacturer."
        n "No worries, already have the replacement. I went with the aftermarket option, so it was less expensive."
        mc "Seriously?! You don't even know if it's actually a crankshaft issue!"
        n "With my years of experience in this line of work, I'm certain it is."
        n "Sometimes, I don't have to look at the issue to diagnose it."
        mc "Damn..."
        mc "Oh, that's right... How long have you been doing this?"
        n "With automobiles specifically..."
        n "... From when I was seven."
        mc "That young?!"
        n "Yeah..."
        n "In any case, let's get her done, eh?"
        mc "Sure! Leave the heavy lifting to me."

        scene black
        with dissolve
        with fadeq

        "A few hours later..."

        scene black
        with dissolve
        with fadeq

        scene ch1ep3p2_76
        with dissolve
        mc "Ready?"
        n "Yeah, give it a go, mate!"
        play sound dodgechallengerstart
        scene ch1ep3p2_77
        with Dissolve(0.2)
        pause 1.0
        scene ch1ep3p2_78
        with Dissolve(0.2)
        mc "Ass kickin'!"
        mc "Man, listen to her purr!"
        scene ch1ep3p2_79
        with Dissolve(0.2)
        mc "Hey, Na-"
        scene ch1ep3p2_80
        with dissolve
        n "..."
        mc "..."
        yt "Is that relief I'm seeing on her face...?"
        scene ch1ep3p2_81
        with dissolve
        n "Finally, after all these bloody months..."
        mc "You've been tinkering with her for months?"
        n "Yeah. It's not all been smooth sailin', y'know."
        n "That crankshaft was a real pain in the arse to get situated and... despite lookin' good now, there's still a laundry list to get through."
        mc "You're not just tweaking the engine then?"
        scene ch1ep3p2_82
        with Dissolve(0.2)
        n "Oh, mate... it's never just the engine."
        n "I've gotta look at a new paint job, and then there's the interior to think about, gauges to fix, and just a bunch of little bits and bobs to get her roadworthy."
        n "And the stuff I mentioned earlier as well."
        scene ch1ep3p2_83
        with dissolve
        n "But listen to her... she's well on her way, ain't she?"
        mc "She is!"
        n "And thanks for lending a hand, mate. Means a lot to me."
        scene ch1ep3p2_84
        with dissolve
        mc "No biggie! The complicated stuff was all you. I didn't do much."
        n "Even so, your help sped things up. Every bit counts, y'know."
        mc "Haha, okay, okay, I'll take the credit then."
        image namctadodgeengp2:
            "ch1ep3p2_85.jpg"
            pause 3.0
            "ch1ep3p2_86.jpg"
            pause .2
            repeat
        show namctadodgeengp2
        with dissolve
        n "So then..."
        n "You get to pop one question my way."
        mc "Sorry?"
        n "I didn't just invite you here without a bit of give-and-take, mate. I don't roll like that."
        n "Ask away, I'll be straight up with my answer."
        yt "Damn... What should I dive into?"
        yt "There are many things I wanna know about her, but... something's been gnawing at me since she mentioned it."
        mc "... Alright, I got one."
        n "Shoot."
        mc "I know it's not your favorite topic, but you gave me a shot, so I gotta take it."
        mc "I've gotta know, Naomi..."
        mc "Why are commitments not your thing?"
        scene ch1ep3p2_87
        with dissolve
        n "Oh..."
        mc "Regretting that offer now?"
        scene ch1ep3p2_88
        with dissolve
        n "No, I just didn't think you'd go poking around about me."
        mc "I mean, you can't blame me."
        mc "You gave me the choice, and I chose to ask something that matters."
        n "*chuckles* Fair enough, mate..."
        n "Well, let's make it short. I hate tellin' life stories for hours."
        stop music fadeout 4
        play music2 'audio/Whispers.mp3' fadein 4 loop
        scene ch1ep3p2_89
        with dissolve
        n "..."
        scene ch1ep3p2_90
        with dissolve
        n "Truth be told, mate... you ain't the first to pry into my reluctance towards commitments."
        n "... Normally, when folks ask, I'd just shield myself behind the typical notion that blokes are all the same when dealin' with sheilas."
        n "But, my reality... it's a bit of a different story."
        scene ch1ep3p2_91
        with dissolve
        n "Before Francis, there were a few others."
        n "One was an artist, gentle soul. Loved me in a way that always made me feel like I was some kind of masterpiece he was always in awe of."
        n "Another was a mechanic like me. Shared the same passions and had loads in common, but somehow, like I always do, I still found a reason to walk away."
        n "Each relationship echoed the last - I'd find myself pullin' away, always endin' things because I thought they were just too bloody good for someone like me."
        show ch1ep3p2_92
        mc "... Naomi, you're not..."
        n "Let me finish, mate..."
        mc "Sorry..."
        image namctanapast:
            "ch1ep3p2_93.jpg"
            pause 3.0
            "ch1ep3p2_94.jpg"
            pause .2
            repeat
        show namctanapast
        with dissolve
        n "Then came Francis... He was different."
        n "Something about him drew me in like no one else had. I thought that was love."
        n "It all fell apart when I saw what he was really like, so I ended it without a second thought."
        n "But the pain lingered; a few weeks of being in a relationship cut deeper than I ever imagined."
        n "Yeah, you could say I was an easy girl."
        mc "Naomi... I'm so sorry."
        n "Don't be, 'cause it's all on me."
        n "Y'see, before Francis, there was this someone who was genuinely good to me."
        n "Someone I left in the shadows of my selfish pursuits."
        n "The thought that keeps me up at night is \"what if\"..."
        n "What if I had given a real chance to those that came before?"
        n "What if I hadn't been so quick to find flaws and end things?"
        n "Would any of this mess have happened?"
        n "It's those thoughts, those what-ifs, that hold me back now."
        n "Sure, I learned me lesson at the end of it, but now there's this fear... a fear of causin' someone pain, y'know?"
        n "Because I never learned a goddamn thing; I'm just a sad song with nothin' t'say."
        scene ch1ep3p2_95
        with dissolve
        n "... Since ya seem so keen on me..."
        n "I've got a curveball for ya..."
        mc "Hit me with it."
        n "Close yer eyes, mate, and keep 'em shut."
        n "Try to forget my face, just for a sec."
        scene ch1ep3p2_96
        with dissolve
        mc "Uhm, sure..."
        scene ch1ep3p2_97
        with dissolve
        n "Now, without takin' a look at me, do ya think you could ever find it in yourself to love a screw-up like me?"
        menu:
            "I could":
                $ naomiroute = True
                stop music2 fadeout 2
                play music 'audio/YouMeanTheWorld.mp3' fadein 2
                scene ch1ep3p2_98
                with dissolve
                mc "Looking into myself right now, with my eyes sealed shut, I'm faced with a pitch-black darkness..."
                mc "... Yet there's this vivid image of you, radiant and unbearably real."
                mc "My heart doesn't need eyes to see your worth or the beauty you hold, Naomi."
                mc "Yes, you've got a jagged and worn past, but don't we all?"
                mc "I'd be downright privileged to love a woman who's lived, learned, and still managed to hold onto a softness that life often tries to steal."
                mc "So, even blinded like this, my answer is a heartfelt yes. I could find it within myself to love a woman like you."
                scene ch1ep3p2_99
                with dissolve
                pause
                scene ch1ep3p2_100
                with dissolve
                pause
                yt "What's happening here? Is she just gazing at me?"
                scene ch1ep3p2_101
                with dissolve
                n "You can open 'em, [mc]..."
                scene ch1ep3p2_102
                with dissolve
                yt "Hold on a second... When was the last time she actually called me by my name?"
                yt "Hearing my name gently leaving her lips after all this time..."
                yt "That feels... so genuine when she says it under her breath like that!"
                yt "You can't help but get goosebumps and butterflies..."
                yt "I swear, this woman is a different kind of drug!"
                scene ch1ep3p2_103
                with dissolve
                n "[mc]... folks don't really converse like that anymore, y'know?"
                mc "I know. But I bet many wish they dared to speak like that to a lady like you."
                scene ch1ep3p2_104
                with dissolve
                pause
                scene ch1ep3p2_105
                with dissolve
                n "Ain't you a charmer."
                mc "Wait, what?"
                n "Let's shake a leg, yeah? We need to get cleaned up. We've got some lunch to catch up on."
            "That's a hard question to answer":
                $ naomiroute = False
                scene ch1ep3p2_102
                with dissolve
                mc "I can't lie to you, Naomi. It's a tough question to answer honestly without more time to really understand each other."
                mc "It's difficult to say I could love someone without knowing them through and through."
                mc "Love is a heavy word, and I just need to be sure before I say something like that, you know?"
                scene ch1ep3p2_103
                with dissolve
                n "Fair dinkum, mate. I appreciate the honesty."
                n "It's a heavy word indeed, and it's too easy to throw it around without realizing its weight."
                n "It's just... it's somethin' I needed to hear and to consider. I respect ya more for givin' me a true answer."
                scene ch1ep3p2_105
                with dissolve
                n "Let's shake a leg, yeah? We need to get cleaned up. We've got some lunch to catch up on."
                jump naomifirstarcend
    stop music fadeout 2
    stop sound2 fadeout 2

    if naomiroute:
        scene black
        with dissolve
        with fade

        play sound closedoor
        scene ch1ep3p2_106
        with dissolve
        mc "Was that all for today?"
        n "Yeah, for the moment. Just needed her to start without a hitch."
        n "Gonna be up for lendin' a hand again?"
        mc "Of course. Feel free to message me anytime. I'll let you know if or when I'm free."
        n "Will do."
        play sound chair
        scene ch1ep3p2_107
        with dissolve
        n "How about after this? Any plans, [mc]?"
        mc "Not in particular."
        mc "I was granted a day off by my boss as thanks for assisting a colleague with airport transit."
        mc "Also, I am officially off duty tomorrow, so I'm unoccupied for two days straight."
        label naomishowerfix:
        if _in_replay:
            $ name = persistent.gallery_name
        play music 'audio/ShakeThatFever.mp3' fadein 0.5
        play sound cloth
        scene ch1ep3p2_108
        with dissolve
        mc "I'll check if I have anything scheduled though, just in case I overlooked something."
        play sound cloth
        scene ch1ep3p2_109
        with dissolve
        mc "Let's see..."
        n "The room's gettin' all ripe with the scent of motor oil and sweat, [mc]. Reckon we oughta freshen up."
        play sound cloth
        scene ch1ep3p2_110
        with dissolve
        mc "Please, after you. I didn't get my hands as dirty as you did."
        play sound cloth
        scene ch1ep3p2_111
        with dissolve
        n "Ooh, ever the gentleman."
        scene ch1ep3p2_112
        with dissolve
        mc "Yep, nothing on my calendar."
        scene ch1ep3p2_113
        with dissolve
        mc "Why did you ask-"
        scene ch1ep3p2_114
        with dissolve
        mc "..."
        n "..."
        scene ch1ep3p2_115
        with dissolve
        n "Ya plannin' to stay there gawkin', mobile in hand, jaw on the floor? Or y'thinkin' of joinin' me for a shower?"
        play sound celldrop
        show ch1ep3p2_116
        with hpunch
        pause
        scene ch1ep3p2_117
        with dissolve
        mc "Standing..."
        n "Standing?"
        mc "It's standing-"
        mc "No, I mean shower. Yes, shower!"
        menu:
            "Give her some privacy":
                $ naomiroute = False
                yt "Am I really gonna turn down this golden opportunity?"
                yt "Well... it's probably best not to tempt fate and push things too far, right?"
                yt "I don't think she would like that, would she?"
                mc "As tempting as that sounds... I think it's best you go first, Naomi."
                mc "Let's not get any crazy ideas so quickly after we just had a heart-to-heart."
                scene ch1ep3p2_118
                with dissolve
                n "Fair dinkum, mate."
                n "Other blokes would probably call you a drongo for sayin' that, but I respect yer reasoning."
                n "Now don't be sayin' that then be a peeping tom while I'm in there!"
                mc "*chuckles* Don't worry, Naomi. I won't try to crack onto you."
                n "Good on ya, mate!"
                $ renpy.end_replay()
                jump naomifirstarcend
            "Strewth! Sweet as!":
                $ naomiroute = True
                yt "Did she just say what I think she said?"
                yt "Join her? Is that even a question?"
                yt "I am a guy with functioning eyes. And a functioning dick. So the answer is \"hell yes, let's go\"!"
                yt "But make sure to play it cool, [mc]."
                mc "Hell yeah!"
                yt "... Wow. Real cool. Thanks a lot, brain."
                scene ch1ep3p2_118
                with dissolve
                n "*chuckles* Alright then, let's get cleaned up."
                n "Or maybe get a little dirtier... Who knows?"
                play sound chair
                show ch1ep3p2_119
                with hpunch
                "With that, Naomi disappears into the bathroom, leaving the door open behind her."
                "Before your brain knows what's happening, your body jumps up and makes a beeline for the door."
                play sound cloth2
                show black
                with hpunch
                "Just as you enter the doorway, you feel something hit your face and obscure your vision."
                mc "Whoa! Hey!"
                n "Ah ah, not so fast, [mc]. What's the first rule before hoppin' in the shower?"
                mc "Um..."
                play sound cloth
                scene ch1ep3p2_120
                with Dissolve(1.0)
                "You reach up to remove the object from your face, then check to see what it is: a bath towel."
                mc "Always pack a towel?"
                scene ch1ep3p2_121
                with dissolve
                "You look up, trying to locate Naomi."
                "Just as you lock eyes with her, she gives a playful smirk."
                play sound thud2
                show ch1ep3p2_122
                with hpunch
                "She pushes you against the wall."
                n "Not quite."
                scene ch1ep3p2_123
                with Dissolve(1.0)
                "Without losing a beat, she leans her body into yours, catching you off-guard with a deep kiss."
                "Recovering smoothly, you wrap your arms around her waist and pull her tighter."
                yt "Damn! Naomi doesn't waste any time, does she?"
                yt "That's what I love about her. Even though she plays things cool, if she wants to do something, she'll always find a way."
                yt "But under that determination and resilient exterior, there's a girl that just wants to be loved, yet doesn't understand what love really is."
                yt "And even though she never showed her vulnerable side until today, there's got to be more than just failed relationships that shaped who she is today."
                yt "What other secrets do you have, you mysterious Sheila?"
                scene ch1ep3p2_124
                with dissolve
                "As your tongues dance in each other's mouths, Naomi brings her hand up to your collar."
                scene ch1ep3p2_125
                with dissolve
                "Grinning, Naomi breaks away as she seductively answers the question that she had asked you."
                n "You strip down, ya silly bogan."
                "You return her teasing smile."
                mc "With pleasure."
                play sound cloth
                scene ch1ep3p2_126
                with dissolve
                "You do exactly that, baring yourself in front of her."
                "Naomi looks up and down your body, clearly pausing once she sees the special package."
                "She gasps, then quickly recovers her mischievous smirk."
                n "So that's the beast you've been keepin' locked up all this time?"
                mc "Is that what you're calling it?"
                n "How else should I put it? That {i}thing{/i} is big enough to go toe-to-toe with the toughest creatures in the Outback."
                "She chuckles, her gaze never straying from your member."
                n "Bloody hell, might just come out on top by sheer intimidation too."
                mc "Hey, you: my eyes are up here."
                n "\"Hey\" yourself. You had your gawk. Now, it's my turn."
                mc "So that's what we're here for? Just to ogle each other while the grease sets into our skin?"
                scene ch1ep3p2_127
                with dissolve
                "At last, she looks you in the eyes."
                n "Fair enough. You and your Burrunjor stay put while I get the shower cranked up."
                scene ch1ep3p2_128
                with dissolve
                "Naomi turns around and gives you a knowing look as she walks towards the shower."
                n "And don't you move."
                scene ch1ep3p2_129
                with dissolve
                "She pauses once she reaches the faucet handle."
                n "Now, which way was the hot water again?"
                "She \"inspects\" the handle, bending over to observe the bottom."
                "As she does, she ever-so-slightly wiggles her own taut bottom at you."
                yt "Was that an invitation, or..."
                yt "Screw it. I'd rather beg for forgiveness than ask for permission. Especially when she has a body like that."
                play sound thud2
                show ch1ep3p2_130
                with hpunch
                "You close the distance almost the instant you finish your thought."
                "Grabbing Naomi's hips, you spin her around, then push her against the wall as you give her another deep kiss."
                n "Mmp!"
                "Naomi squeals, though it doesn't seem to be from surprise."
                yt "So this was her plan all along?"
                yt "Man... I {i}really{/i} like this girl."
                scene ch1ep3p2_131
                with dissolve
                "You back away just a bit, letting your lips hover over hers."
                mc "You know, that little move back there was just asking for trouble."
                "She whispers her response into your ear, causing your hair to stand on end."
                n "I've already found it, wouldn't you say?"
                mc "As have I."
                scene ch1ep3p2_132
                with Dissolve(0.2)
                "You move to kiss her again, but she turns her head to the side."
                play sound2 shower loop fadein 2
                scene ch1ep3p2_133
                with dissolve
                "Confused, you move back, then realization hits as you feel the water cascading down onto your body."
                n "There we go. Something to keep us squeaky clean while we're gettin' dirty."
                mc "Of course. Smart girl!"
                scene ch1ep3p2_134
                with dissolve
                mc "Although... I'm surprised."
                n "Why's that?"
                mc "Normally, when I turn on the shower, it takes a few seconds to warm up."
                mc "But this... the hot water came out instantly."
                scene ch1ep3p2_135
                with dissolve
                n "Ah, yep! It's a special faucet I found recently called the Shower Magician v2."
                mc "Ugh, please don't go all saleswoman again..."
                scene ch1ep3p2_136
                with dissolve
                n "Time and place, [mc]. Don't worry."
                n "Right now, my focus is squarely on you."
                scene ch1ep3p2_137
                with dissolve
                "Naomi wraps her arms around you as her lips reunite with yours."
                "You reciprocate the gesture, resting your hands on her butt as you return the kiss."
                scene ch1ep3p2_138
                with dissolve
                "Suddenly, Naomi grabs your wrists, pulling them away from her rear. You worry you may have moved too fast."
                scene ch1ep3p2_139
                with dissolve
                "However, rather than push you away, you feel Naomi escorting your hands towards her vulva."
                "Once your fingers rest on her clit, she pauses."
                scene ch1ep3p2_140
                with dissolve
                n "I'm all for a good chinwag, but bein' stuck in first gear gets old fast."
                n "Reckon your hands can keep up?"
                "You need no help answering that question."
                mc "You're about to find out."
                stop sound2 fadeout 2
                play sound glasshit
                show ch1ep3p2_141
                with hpunch
                "Wasting no time, you grab Naomi's wrist and pin her against the glass."
                n "I like th-"
                show naomi1
                with dissolve
                "You push your mouth into the crook of her neck, smothering the sentence."
                "Your teeth nibble her wet skin, then cede way for your tongue to caress the area."
                "Simultaneously, your fingers begin to move, gently massaging Naomi's most sensitive spot."
                n "Mmm..."
                "Naomi's eyes flutter shut as she surrenders to her desire."
                "You pull back to move from her lips to her neck, but her lips dart forward to meet yours before you can even react."
                yt "Heh, still a go-getter even when she's in the most vulnerable of positions. Never change, Naomi."
                yt "But I have a few surprises of my own, so don't get too comfortable."
                "As she begins to move back, you bite and tug on her lower lip."
                "Your mouth then moves from her lips to her neck, sucking the sensitive skin at each place."
                "Every time and everywhere you touch her, Naomi purrs in titillation."
                "Aided by the warm water running down her body, your fingers glide smoothly against her clit, massaging in a circle, then venturing up and down her labia."
                n "Nhh..."
                "Naomi gives another moan of approval, subconsciously telling you that you're hitting the right spots."
                "You can feel the warmth of her vagina increasing with each motion as her clitoris grows firmer in response to your movements."
                "And despite the warmth of the shower, goosebumps blanket her skin."
                n "Mmm... not... bad..."
                yt "Not bad? That's it?"
                yt "Your body's practically begging for more, and you consider it \"not bad\"?"
                yt "So you're gonna try to play it cool? Ok."
                yt "There's more where that came from, Naomi."
                yt "The question is: how much will you be able to handle?"
                show naomi2
                with dissolve
                hide naomi1
                "Determined to make her eat those words, you pick up the pace and try a new tactic."
                "As your thumb continues to massage Naomi's firm bud, your other fingers explore her inside."
                n "Oh!"
                "Naomi is surprised by the sudden change-up but makes no effort to stop you."
                mc "So, not bad?"
                n "Ah... yep..."
                n "Gettin' warmer..."
                show naomi3
                with dissolve
                hide naomi2
                mc "Only warm? Then I need to do better."
                "You move even faster, spurred on by the desire to achieve better accolades."
                "Your index and middle fingers massage her smooth inner walls while your thumb dances circles on and around her clitoris."
                "Your lips continue to assault the side of her neck, nibbling, licking, and sucking the skin raw."
                yt "You're a tough girl, Naomi, but even tough girls have a breaking point."
                yt "And I can feel you're getting close to yours."
                "Sure enough, it soon becomes impossible to tell which part of your hand is wet from the shower versus from the fluids produced by her arousal."
                n "Ahh! Hah... mmhh..."
                "Naomi's breathing becomes more labored as you continue to massage her nether region."
                "She struggles to gasp for air between the ebbs of intensifying euphoria."
                "Simultaneously, her heart races faster, matching the struggle felt by her lungs."
                n "Ho... ly... hmm!"
                "Your hand continues to move against her sensitive skin, refusing to stop until Naomi reaches her limit."
                n "Ngh! Ghmmm!"
                yt "Don't fight it, Naomi. Just let go."
                mc "How about now? Still not bad?"
                "Naomi opens her eyes to look at you; her expressions equal pleasure and strain."
                n "Nhh! What... do you... mmh!"
                "With her focus distracted, Naomi finally succumbs to the climax your efforts have built up."
                hide naomi3
                play sound cloth2
                show ch1ep3p2_142
                with hpunch
                n "Mmh!!!"
                "She lets out a near-silent moan, one which you might not have heard if you weren't right next to her."
                yt "Bold, horny, yet not a screamer? Naomi, you sure are full of surprises."
                show ch1ep3p2_143
                with hpunch
                "Her pussy contracts pulse after pulse against your fingers, releasing a torrent of fluid onto your hand; a stark contrast to her lack of noise."
                n "Nhh... mmh..."
                yt "But you sure {i}are{/i} a squirter. Good to know..."
                scene ch1ep3p2_144
                with dissolve
                "Finally, the last wave of orgasm passes through Naomi's body."
                "Out of breath, she braces herself against the glass to recover."
                n "Ho... holy... that's a... first..."
                scene ch1ep3p2_145
                with dissolve
                mc "You mean everything that just happened? Or do you mean this?"
                "You hold up your hand, still coated in Naomi's juices."
                n "You wouldn't... like to know..."
                mc "Alright then, keep your secrets."
                n "Damn... legs... feel like... vegemite..."
                "You chuckle to yourself."
                mc "Even though we were in the shower all this time, we didn't get very clean."
                scene ch1ep3p2_146
                with dissolve
                "Naomi lets out a tired but hearty laugh."
                n "You talkin' about... the mess... I left on your hand?"
                n "If so... not sorry... you're as much to blame... as I am."
                mc "Heh, no, not exactly. I meant more like the shower magically stopped once we started moving."
                n "Ah, that. You must've... bumped the handle and... turned off the water when you made your move."
                mc "Really? I guess that could have happened..."
                mc "Anyways, we still need to get cleaned up."
                n "Why don't we shift to the tub?"
                n "I could use a hand scrubbin' my back."
                scene ch1ep3p2_147
                with dissolve
                "Seemingly fully recovered, Naomi winks and grabs your hand, leading you to the bathtub across the room."
                scene ch1ep3p2_148
                with dissolve
                mc "You sure we'll get clean in there?"
                n "Only one way to find out."
                play sound watermovement
                scene ch1ep3p2_149
                with dissolve
                "Naomi steps into the tub."
                n "There we go. Perfect temperature."
                scene ch1ep3p2_150
                with dissolve
                "Noticing that you're still standing, she stares at you like you're still holding your phone, gawking at her."
                n "Well? You plan on reachin' every inch of my back standing over there?"
                mc "Ah, sorry. Silly me."
                play sound watermovement
                scene ch1ep3p2_151
                with dissolve
                "You slide in behind her and begin scrubbing."
                mc "Damn, who did they build this bath for? Chickens?"
                n "You reckon people always take baths two at a time, then?"
                mc "Point taken. But still, I feel like my legs will cramp up any second because of how tight it is in here."
                scene ch1ep3p2_152
                with dissolve
                n "Speaking of things gettin' stiff..."
                n "I can feel your hot rod cozying up against me."
                mc "Like I said, not a lot of room to work with here. And I can't exactly shrink it down, especially not after a hot girl just came all over me a minute ago."
                play sound watermovement
                scene ch1ep3p2_153
                with dissolve
                "Naomi turns around to face you, another naughty look on her face."
                n "Aww... poor diddums."
                "You pick up on her cue."
                yt "God, this woman is so much fun! I feel bad for those idiots who didn't manage to see her like this."
                yt "Sorry, folks. But she may be bound to be mine now."
                mc "I know... if only the person that caused this would fix the problem..."
                mc "Maybe by taking it for a ride?"
                n "Nah-uhh... The only ride you'll be gettin' today is the ride back to your house."
                yt "Oof... Not this time, I guess."
                n "But..."
                scene ch1ep3p2_154
                with dissolve
                "Once again, Naomi gives you that knowing smirk."
                n "It'd be bad form for a host to let her guest leave {i}unsatisfied{/i}."
                n "Up you get, [mc]. Park yourself on the edge of this tub so I can show you some good hospitality."
                play sound watermovement
                scene ch1ep3p2_155
                with dissolve
                "You do as she says, grabbing the tub's sides for balance."
                mc "I'm listening..."
                mc "But at the same time, I hope this tub won't tilt over..."
                n "No need to worry, mate."
                n "It's as sturdy as they come. Bolted it in myself."
                n "Now, you just sit tight and {i}stay upright{/i} for me, will ya?"
                mc "I like where this is going."
                n "Mate, you ain't seen nothin' yet."
                mc "Actually, I'm seeing a whole lot of sexy woman right now..."
                n "You gonna keep spoutin' those corny one-liners?"
                n "Or you want me to show you what else these hands can do?"
                mc "Hmm... why not both?"
                "Your answer causes her to snicker."
                n "Hah. Bogan."
                "Not waiting for another witty response, Naomi wraps her hands around your erection."
                n "This little bloke's been itchin' for some attention. Poor bugger."
                n "Well, maybe not so little, eh?"
                show naomi4
                with dissolve
                "Naomi begins to stroke your cock, her strong yet gentle hands stimulating your full length."
                "The same hands that push and lug around car parts handle your manhood with a surprising tenderness, amazing you with their delicate, purposeful movements."
                yt "How can hands that perform manual labor every day still be this soft? How does she have this much dichotomy?"
                yt "... Just who the hell is this girl?"
                "You feel the warmth building in your groin, the blood filling your lower chambers."
                mc "Holy shit, Naomi..."
                n "Hm?"
                "She looks up at you with an amused grin."
                mc "You're... really good with your hands..."
                n "I would hope so. I need them for my jobs, after all."
                mc "Heh. {i}Jobs{/i}."
                n "I'm glad I'm not the only one who enjoys a double entendre."
                mc "Hng-you speak French, too?"
                n "Nah, but I {i}do{/i} know my way around hard tools."
                mc "Hoooh-I might have to agree with you there!"
                n "Might?"
                show naomi5
                with dissolve
                hide naomi4
                "Naomi increases the pace, her two hands working in tandem to rub your throbbing rod."
                "She runs her hands along your manhood while slightly turning her wrists. Her soft palms set every nerve in your dick on fire with each move."
                "Any blood that your body has left now goes rushing into your crotch, making it hard to think straight."
                n "In that case, I {i}might{/i} have to put in a bit more elbow grease."
                "Each wave of pleasure hits you, one after another."
                yt "Fuck! I can't last much longer if she keeps this up."
                "As if she read your mind, Naomi starts to squeeze your cock each time she travels its length, willing your cock to release its load."
                "While her hands work their magic down low, she looks up to see how her actions are being received."
                "Though your eyes are closed, you hear her utter an amused chuckle. Seems like you don't have the most graceful O-face."
                "That said, it's hard to complain when you're this close to the edge."
                n "How you holdin' up?"
                mc "Mgh... F-fine!"
                n "Just fine? Alright, if you say so."
                "Acting annoyed, Naomi slows down noticeably."
                "You open your mouth to clarify your comments."
                show naomi6
                with dissolve
                hide naomi5
                "But before you can say a word, she speeds up again even faster than before."
                "Holy shit, this girl has a knack for knowing exactly when to push the right button."
                mc "Hagk!"
                "The sudden change in speed sends your already-taxed system into overdrive."
                "The waves of pleasure rapidly become tsunamis; it's only a matter of seconds before the floodgates open."
                mc "N-Naomi! I'm g-gonna c-"
                n "Really? The fact that I can feel your heart goin' a mile a minute through your mate down under doesn't make that obvious at all."
                mc "Urgh! I'm s-serious!"
                n "Relax, I know."
                mc "K-kinda hard to... relax now!"
                "Naomi deftly moves her mouth towards your manhood."
                n "Then release."
                "As she continues to stroke you with her right hand, Naomi sensually licks the base of your glans."
                "With that last move, she takes you far beyond the point of no return."
                hide naomi6
                play sound watermovement
                show ch1ep3p2_156
                with hpunch
                mc "Ghhhhh!!!"
                "Your cock violently twitches before projecting forward, possibly the largest amount of cum you've ever produced."
                "This process repeats itself over and over, as your body succumbs to the consequences of Naomi's actions."
                "By some miracle, Naomi is able to dodge each stream, with each spunk missile making an audible 'splash' as it lands into the bathwater."
                "Finally, you finish releasing your last load."
                play sound watermovement
                scene ch1ep3p2_157
                with dissolve
                "Content with her work, Naomi stands up and steps out of the water."
                n "Nice try, [mc], but you missed."
                "Exhausted, you hold on desperately to the edges of the tub. Any slip will send you straight into the tainted water."
                n "Better luck next go 'round, mate."
                mc "So... there's gonna... be... a next time?"
                scene ch1ep3p2_158
                with dissolve
                n "Hmm..."
                scene ch1ep3p2_159
                with dissolve
                n "I {i}might{/i} have to agree with you."
                yt "Did she just use my own words against me?"
                yt "... this cheeky minx."
                n "So, would you say I've done my bit as a host?"
                play sound watermovement
                scene ch1ep3p2_160
                with dissolve
                "Having regained enough energy, you stand."
                mc "Definitely... holy fuck..."
                n "Although I did promise you lunch, didn't I?"
                n "So how 'bout we clean ourselves up properly this time, and I'll whip us up some grub?"
                mc "Sounds good... you sure... you don't want help?"
                scene ch1ep3p2_161
                with dissolve
                n "Help gettin' clean? Fat chance, [mc]."
                n "We've already seen what happens when we try to clean each other up."
                mc "Ha...ha... I meant cooking..."
                scene ch1ep3p2_162
                with dissolve
                n "Also a no-go. Nobody touches my kitchen but me."
                mc "You s-"
                n "No. Bo. Dy."
                mc "Okay then, message received."
                mc "So, you want... the bath... or shower?"
                n "I'll take the shower, thanks."
                n "You've already marked the bath as yours."
                mc "Fair point."
                stop music fadeout 2

                scene black
                with dissolve
                with fade

                play music 'audio/YouMeanTheWorld.mp3'
                scene ch1ep3p2_163
                with dissolve
                mc "So..."
                n "So."
                mc "That was fun."
                n "Indeed."
                scene ch1ep3p2_164
                with dissolve
                n "It's always a good time gettin' your hands dirty while fixin' up a classic 4-wheeler."
                mc "Well, I guess that too."
                scene ch1ep3p2_165
                with dissolve
                n "Cheers for popping over, [mc]."
                n "Today would've been a right pain without you."
                mc "No problem at all, Naomi. I had fun."
                n "I mean it. You didn't just help mend a busted car."
                n "You also fixed something else that was once thought beyond repair."
                mc "What do you mean?"
                scene ch1ep3p2_166
                with dissolve
                n "What you said to me, it made me..."
                mc "Made you what?"
                scene ch1ep3p2_167
                with dissolve
                n "..."
                mc "Naomi?"
                scene ch1ep3p2_168
                with dissolve
                n "... Made me realize I'm bloody starving. Let's tuck in!"
                mc "Oh, okay. Sure."
                play sound closedoor
                scene ch1ep3p2_169
                with dissolve
                yt "Is that what she really wanted to say...?"
                yt "That was unlike her to be indecisive..."
        stop music fadeout 2
        $ renpy.end_replay()

        scene black
        with dissolve
        with fadeq

        "Later, late at night..."

        scene black
        with dissolve
        with fadeq

        play sound2 ceilingfan_low loop
        scene ch1ep3p2_170
        with dissolve
        pause
        show namctanapast
        with flash
        n "What if I had given a real chance to those that came before?"
        n "What if I hadn't been so quick to find flaws and end things?"
        n "Would any of this mess have happened?"
        n "It's those thoughts, those what-ifs, that hold me back now."
        n "Sure, I learned me lesson at the end of it, but now there's this fear... a fear of causin' someone pain, y'know?"
        n "Because I never learned a goddamn thing; I'm just a sad song with nothin' t'say."
        scene ch1ep3p2_170
        with flash
        n "..."
        play sound flipphone
        scene ch1ep3p2_171
        with Dissolve(0.2)
        pause
        stop sound2 fadeout 2
        scene black
        with dissolve
        pause 1.0
        play sound2 dawnambient loop
        play music 'audio/FirstCrush.mp3'
        scene ch1ep3p2_172
        with dissolve
        mc "Brr! It's starting to get chilly..."
        n "*phone* Ugh, tell me about it."
        scene ch1ep3p2_173
        with Dissolve(0.2)
        mc "And hey, no more FaceTiming me while you're driving, alright? Keep your eyes on the road."
        n "*phone* Relax, [mc]. I've got it all under control. And look, I'm here already."
        play sound carpark
        scene ch1ep3p2_174
        with dissolve
        pause
        scene ch1ep3p2_175
        with dissolve
        mc "Wow, that was fast! You didn't even take ten minutes!"
        mc "It took me a solid fifteen minutes to get from here to your place earlier."
        n "Sometimes, livin' on the edge has its perks."
        play sound woosh2
        show ch1ep3p2_176
        pause 0.5
        play sound bodyhit
        show ch1ep3p2_177
        pause 1.0
        play sound thud2
        show ch1ep3p2_178
        with hpunch
        mc "Whoa! Hot, hot!"
        scene ch1ep3p2_179
        with dissolve
        mc "What's this?"
        n "Just drink it. It'll help warm ya up."
        mc "Thanks."
        play sound cartrunkclose
        scene ch1ep3p2_180
        with dissolve
        mc "Up here, come on."
        scene ch1ep3p2_181
        with dissolve
        pause
        mc "*chuckles* Look at us, sitting here in the dead of night. What's got you up and calling me at this hour?"
        n "Just one of those nights where sleep feels like a distant dream."
        mc "Something on your mind?"
        scene ch1ep3p2_182
        with dissolve
        n "Yeah, opportunities. Ever think about them?"
        mc "Opportunities, huh? That's a pretty loaded word for this time of night."
        n "Right?"
        n "There's those you make, those that just land on your lap, and those that slip through yer fingers before ya even realize it."
        mc "Someone's been pondering some late-night philosophy, I see."
        n "I can't say I ain't guilty."
        n "But I've been thinking about this one opportunity. The kind I wanna carve out for myself."
        mc "Alright, you've got my attention again. What is this \"opportunity\" thing?"
        n "It's the chance not to let past mistakes dictate how I deal with the people who matter."
        n "I don't want to mess up my relationships anymore because of old baggage."
        mc "That's a big realization there, Naomi. What the hell happened after I left?"
        scene ch1ep3p2_183
        with dissolve
        n "I want ya to be part of that, [mc]."
        mc "Me? Why's that?"
        image naflipmcdc:
            "ch1ep3p2_184.jpg"
            pause 3.0
            "ch1ep3p2_185.jpg"
            pause .2
            repeat
        show naflipmcdc
        with dissolve
        n "Because I don't want to repeat the same mistakes. I wanna take the wheel and do things differently with you."
        mc "Wait, what? You're serious?"
        n "Dead serious."
        n "I want to... let's say, \"create a unique bond together\" where I'm at the helm."
        mc "Are you basically saying {i}you{/i} want to hit on {i}me{/i}?!"
        mc "Damn, Naomi... I know you're straightforward, but I did not expect that at all!"
        n "Yeah, ya heard me right. I wanna make a move on ya, [mc]. But this time, I'm the one taking the risks."
        n "If anything goes wrong, I want to be the one to take the fall, not you."
        mc "Shit... Talk about one hell of a plot twist..."
        n "I guess. I've always been a \"go after what I want\" kind of person, so why change now, right?"
        mc "I wouldn't if I were in your place. Can't fault you for that."
        scene ch1ep3p2_186
        with dissolve
        n "And while we're on the subject, let me lay this one on you: you're the marshmallow in my hot chocolate. You make life just that much sweeter."
        mc "..."
        scene ch1ep3p2_187
        with dissolve
        n "I'm no good, aren't I?"
        mc "Yep... You just killed the momentum, and your timing was off..."
        n "*sighs*"
        mc "Well, just remember: marshmallows tend to dissolve in hot chocolate."
        scene ch1ep3p2_188
        with dissolve
        n "Guess I'll just have to enjoy it before that happens, then."
        mc "Now, there you go. That was some smooth rizz."
        n "Pfff..."
        show naflipmcdc
        with dissolve
        n "So, what's it gonna be, [mc]? Are you on board?"
        mc "You've put a lot on the table, that's for sure. It's not every day someone lays it all out like that, all at once."
        mc "I'll give you this: you've got guts, and I respect that, Naomi."
        mc "But... why all of a sudden?"
        mc "Why me?"
        mc "What did I do to-"
        mc "..."
        n "You know what you said, and I took that to heart."
        n "I may be straightforward, but I don't joke around much either, y'know?"
        mc "Man... you really are one of a kind, Naomi."
        n "Simply put, you got through to me."
        n "I didn't want to give in, but I feel like I'd be losing out on something big if I let this opportunity pass."
        n "So here I am, in the dead of night, not holding anything back."
        mc "Yeah, you certainly didn't hold back..."
        mc "And you know, it's not fair how you've got this way of completely stopping me in my tracks."
        n "Oh?"
        mc "There are moments when you just freeze time, and I can't help but give in to whatever you're doing."
        n "That's the first I've heard of that."
        mc "Maybe it's because this might be the first time someone's actually seen you, looked straight into your eyes."
        scene ch1ep3p2_189
        with dissolve
        n "Oh..."
        mc "What?"
        n "I'm getting soaked."
        mc "Huh...?!"
        mc "Jesus, Naomi! You need to have some kind of restraint."
        scene ch1ep3p2_190
        with dissolve
        n "You're the one who dismantled my defenses, [mc]. Don't start asking me to rebuild them now."
        mc "Alright, this is... well, it's a lot to take in, not going to lie."
        mc "To be completely transparent with you, I'm a bit at a loss for words here."
        mc "This is the first time someone has done a reversal on me. I'd usually be the one to pop {i}the question{/i}, you know?"
        scene ch1ep3p2_188
        with dissolve
        n "*chuckles* I guess I tossed the wrong script your way..."
        play sound cloth
        scene ch1ep3p2_191
        with dissolve
        n "[mc]... Fancy indulging in a bit of mischief with me?" 
        mc "Well, when you put it that way..."
        scene ch1ep3p2_192
        with dissolve
        n "You know what they say: once you've had a taste of something good, you can't help but crave more."
        mc "Can't argue with that."
        play sound cartrunkclose
        scene ch1ep3p2_193
        with Dissolve(0.2)
        n "And don't worry, you don't need to make any decisions right now. I've got a little trick up my sleeve to make things easier for you."
        mc "Wait, what do you mean by that?"
        n "Just wait and see."
        mc "O-okay...?"
        n "Anyways, that's all I wanted to get off my chest. I won't take up any more of your time."
        mc "You're more than welcome to take my time whenever you want it."
        n "Look who's the smooth-rizzer now?"
        mc "*chuckles* Touché."
        n "Good night, [mc]."
        mc "Good night..."
        play sound cardriveaway
        scene ch1ep3p2_194
        with dissolve
        pause
        play sound2 phonemessage
        scene ch1ep3p2_195
        with dissolve
        pause
        scene ch1ep3p2_196
        with dissolve
        mc "A message?"
        scene ch1ep3p2_197
        with Dissolve(2.0)
        pause
        n "{i}How 'bout this for a teaser of what's to come?"
        scene ch1ep3p2_198
        with Dissolve(0.2)
        yt "Shit... when did she get the license to mess with my {i}head{/i} like this?"
        yt "Well, I'm not entirely sold on the idea... but I think I can observe for now and see what she wants to do..."
        scene ch1ep3p2_199
        with dissolve
        yt "*chuckles* \"Warm you up\", my ass... You knew I wouldn't need this from the start."
label naomifirstarcend:
    stop music fadeout 2
    stop music2 fadeout 2
    stop sound2 fadeout 2
    stop sound fadeout 2

    call hide_days from _call_hide_days_8
    with dissolve
    scene black
    with dissolve
    with fadeq

    "A week ago..."

    scene black
    with dissolve
    with fadeq

    play sound festivalcrowd loop
    scene ch1ep3p2_200
    with dissolve
    m "Commander..."
    mc "Yeah? You sound like a lost pup."
    m "It's over. Can we go home now?"
    mc "What? We're still waiting for Lily."
    mc "Don't you want to take pictures with her? And perhaps your classmates too?"
    mc "This day comes around only once, you know?"
    m "I want to, but this dress is a major... deficiency."
    mc "Deficiency?"
    m "Yeah. Everything feels so tight. I don't feel like myself."
    mc "Oh boy..."
    scene ch1ep3p2_201
    with dissolve
    m "These heels are like walking on stilts. They've compromised my stability."
    m "Minus 100 power points."
    scene ch1ep3p2_202
    with dissolve
    m "This skirt could tear with any sudden maneuvers."
    m "Loss of 200 power points."
    scene ch1ep3p2_203
    with dissolve
    m "This blouse isn't designed for mobility. It's restricting my range of motion."
    m "Minus 150 power points."
    if moonroute:
        yt "{i}And plus 200 libido points for [mc]. GODDAMN! Tight, fancy clothes look good on her...{/i}"
    scene ch1ep3p2_204
    with dissolve
    m "And this cap is a liability. A single gust of wind and it goes MIA."
    m "That's minus 50 power points."
    scene ch1ep3p2_205
    with dissolve
    m "All in all, I'm operating at half capacity. I need to fall back."
    yt "*sighs* So, one thousand operating points? I still don't get this woman sometimes."
    mc "How about you go find Lily so we can at least take a picture of you two?"
    mc "After that, we can head home."
    m "Affirmative."
    scene ch1ep3p2_206
    with dissolve
    pause
    scene ch1ep3p2_207
    with dissolve
    pause
    scene ch1ep3p2_208
    with dissolve
    un "Excuse me."
    play music 'audio/PinchPunch.mp3'
    $ renpy.sound.set_volume(0.5, 1.0)
    scene ch1ep3p2_209
    with Dissolve(1.0)
    mc "Hmm?"
    mc "Oh, hey. Can I help you?"
    scene ch1ep3p2_210
    with dissolve
    al "Name's Alexandra. I'm working the graduation today, snapping pics of grads and their families."
    mc "For the school?"
    al "Nah, I'm flying solo. Offering my lens to anyone who wants to freeze this moment in time."
    al "I mean, it's a {i}\"Once in a Lifetime\"{/i} event, right? Deserves better than a blurry phone pic."
    mc "Fair point."
    al "So, you in?"
    scene ch1ep3p2_211
    with dissolve
    yt "Now that I think about it, my old hobby would've been useful in this case."
    yt "I honestly prefer a good old Polaroid to these phone cameras nowadays."
    scene ch1ep3p2_212
    with dissolve
    mc "How much?"
    al "Here's the rundown..."
    al "$30 gets you a single edited digital shot. $60 for three, $80 for five. Anything more is ten a shot."
    mc "Sounds reasonable enough."
    al "And for the print lovers, I do a three-photo 5x7 set for 15 bucks."
    mc "Damn, that's a solid deal. You sure you're not shortchanging yourself? Could probably jack those prices up a bit."
    scene ch1ep3p2_213
    with dissolve
    al "Ah, there are a bunch of freelancers around here undercutting each other like crazy. I'm actually on the pricier side."
    al "But I stand by my rates. You get what you pay for, and I'm all about quality."
    scene ch1ep3p2_214
    with dissolve
    mc "Appreciate the transparency."
    mc "Alright, I'm sold. I'll take the $80 package and add the prints as well. That should cover everything, right?"
    al "That should do it. Let's discuss the details after I've taken the shots."
    mc "Sure."
    scene ch1ep3p2_215
    with dissolve
    pause
    scene ch1ep3p2_216
    with dissolve
    al "..."
    scene ch1ep3p2_217
    with dissolve
    al "Where are your graduates?"
    mc "Well... one of them's running late to come out, so I sent the other to track her down."
    mc "Hope you don't mind waiting for a bit?"
    scene ch1ep3p2_218
    with dissolve
    al "Not a problem. I'll take the opportunity to scout for other clients in the meantime. Is that okay with you?"
    mc "Totally. I'll be right here."
    al "Great. I'll circle back to you shortly."
    mc "See you then."
    stop music fadeout 5
    $ renpy.sound.set_volume(1.0, 3.0)
    scene ch1ep3p2_219
    with dissolve
    pause
    scene ch1ep3p2_220
    with dissolve
    un "Excuse me, young man."
    mc "Yeah?"
    un "I'd like a moment of your time."
    mc "Sorry sir, I've already contracted a photographer. You're a tad too late."
    scene ch1ep3p2_221
    with dissolve
    mc "I just had-"
    $ renpy.sound.set_volume(0.0, 1.0)
    scene ch1ep3p2_222
    with dissolve
    un "I trust I'm not intruding upon anything significant."
    play music 'audio/Infiltrator.mp3'
    play sound2 gravelslide
    show ch1ep3p2_223
    with hpunch
    pause
    scene ch1ep3p2_224
    with dissolve
    un "My apologies if I've startled you."
    mc "Who are you?"
    un "Ah, pardon my lack of manners."
    scene ch1ep3p2_225
    with dissolve
    bo "I am Bonheur Mentzelopoutous, a friend you have yet to make acquaintance with."
    yt "Bonheur, Francis' notorious daddy showing up here of all places...?"
    yt "The reality of that smile being genuine just sends shivers down my spine."
    yt "Unlike his son, this guy is clearly dangerous. I need to tread carefully."
    scene ch1ep3p2_226
    with dissolve
    mc "What's your angle?"
    bo "Worry not, young man. My sole intention is to offer you a friendly warning."
    mc "Save it. I know your game, Pretzeloctopus."
    scene ch1ep3p2_227
    with dissolve
    bo "Is that so?"
    bo "Then you won't be scouring the town for Jovian, will you?"
    yt "How on earth does he know about that? Was it Hera? Did she spill the beans?"
    yt "Or was he there incognito?"
    yt "No, that can't be. Claire and Moon combed the whole area. He couldn't have been there."
    yt "Unless... he's..."
    scene ch1ep3p2_226
    with dissolve
    mc "..."
    yt "Damn... What have you gotten yourself into, Hera?"
    yt "But I won't be the one leaking information here. I'll take this opportunity to see what this old man really wants."
    yt "Time to show him who he's dealing with."
    scene ch1ep3p2_228
    with dissolve
    mc "You seem awfully informed about me, Pretzel-O-Pus. It's as if you've had me under surveillance."
    mc "You've been spying on me, haven't you?"
    show ch1ep3p2_229
    with Dissolve(0.1)
    pause 0.5
    yt "A slight twitch in his left eyelid. He wasn't expecting me to be that observant."
    scene ch1ep3p2_230
    with dissolve
    mc "So, care to share his whereabouts?"
    yt "The snare is set. All that's left is for him to walk into it."
    scene ch1ep3p2_231
    with dissolve
    bo "..."
    yt "Come on, bite..."
    scene ch1ep3p2_232
    with dissolve
    bo "I'm afraid I cannot help you with that, young man."
    yt "That pause and subtle hesitation. He knows something, but he's not willing to spill it."
    yt "Let's push you a bit harder, Pretzeloctopus."
    mc "Because you've never met him, right?"
    yt "And now we wait. If he says yes, then he's lying. If he says no, then he's telling the truth."
    bo "No. Wherever Jovian is, his debts remain unpaid."
    yt "Debts...?"
    show ch1ep3p2_233
    with Dissolve(0.1)
    bo "... You..."
    bo "How did you..."
    scene ch1ep3p2_234
    with dissolve
    bo "*chuckles* A trivial mind game."
    show ch1ep3p2_235
    with Dissolve(0.1)
    mc "Trivial or not, you've just confirmed that you and your son are the biggest idiots I've ever had the displeasure of meeting."
    show ch1ep3p2_236
    bo "It appears conversing in this manner is futile."
    bo "Very well. We shall have a more candid discussion in due course."
    bo "If you'll excuse me while I-"
    scene ch1ep3p2_237
    with dissolve
    m "Commander?"
    bo "..."
    scene ch1ep3p2_238
    with dissolve
    m "Who is he?"
    mc "Bonheur, Francis's father. An {i}acquaintance{/i}."
    scene ch1ep3p2_239
    with dissolve
    bo "You're..."
    bo "Number Four."
    yt "He knows about Moon?! How?!"
    scene ch1ep3p2_240
    with dissolve
    bo "Is this mere happenstance? How much of this is premeditated? What do you all know?"
    mc "What the hell are you babbling about, old man?"
    bo "Oh, Hera... What a delightful web you've woven."
    bo "Friend, or foe? Ally, or adversary? Where will you all fall?"
    bo "*chuckles* Farewell, [mc]..."
    stop music fadeout 5
    $ renpy.sound.set_volume(1.0, 5.0)
    scene ch1ep3p2_241
    with dissolve
    mc "Hey, what about that warning, you pretentious windbag?!"
    mc "\"mY sOlE iNtEnTiOn Is To OfFeR yOu A fRiEnDlY wArNiNg~\""
    mc "Pompous scumbag. Running with his tail tucked between his legs."
    scene ch1ep3p2_243
    with dissolve
    mc "..."
    scene ch1ep3p2_242
    with dissolve
    m "Should I dispose of him? This is our opportunity while he's off guard."
    mc "With that?"
    m "Yes, it's not an issue."
    scene ch1ep3p2_243
    with dissolve
    mc "..."
    scene ch1ep3p2_240
    with flash
    bo "Is this mere happenstance? How much of this is premeditated? What do you all know?"
    scene ch1ep3p2_243
    with flash
    pause
    scene ch1ep3p2_244
    with dissolve
    mc "Nah..."
    mc "He's... no, they will spill every last detail."
    m "..."
    play music 'audio/StrangeConnection.mp3'
    $ renpy.sound.set_volume(0.3, 1.0)
    scene ch1ep3p2_245
    with dissolve
    m "How can you be so calm after that?"
    mc "Calm? Me?"
    mc "... I don't know. It's weird, right?"
    m "..."
    scene ch1ep3p2_246
    with dissolve
    mc "By the way, where's Lily?"
    m "I couldn't find her."
    mc "Are you sure you looked everywhere?"
    scene ch1ep3p2_247
    with dissolve
    m "..."
    mc "..."
    scene ch1ep3p2_248
    with dissolve
    mc "Moon."
    m "I... I got uncomfortable and came back..."
    mc "Uncomfortable? Was it your dress again?"
    scene ch1ep3p2_249
    with dissolve
    m "No, it wasn't the dress."
    mc "Then what was it?"
    m "It was you."
    mc "Huh...?"
    stop music fadeout 3
    stop sound fadeout 3
    $ renpy.sound.set_volume(1.0, 1.0)
    play sound2 dawnambient loop
    scene ch1ep3p2_250
    with Dissolve(2.0)
    show screen day_friday with dissolve
    mc "..."
    mc "...."
    yt "I might have jumped to conclusions there. Just how much does that guy really know about us?"
    yt "And what's his endgame? What does he stand to gain by involving Aine or any of us?"
    yt "Even he doesn't know where Jovian is. But now, at the very least, I know they're somewhat involved with each other."
    yt "Just where did you hole yourself up, huh? Why do you have to make this hard for us?"
    yt "*sighs* I've been so restless after that day..."
    k "[mc], dear! I need you back here!"
    play sound chair
    scene ch1ep3p2_251
    with dissolve
    mc "Yeah, one second!"
    yt "In any case, we need to be more careful..."
    stop sound2 fadeout 2

    scene black
    with Dissolve(2.0)
label moonpause3:
    if _in_replay:
        $ name = persistent.gallery_name
    scene moonpause3
    with dissolve
    $ renpy.pause()
    $ renpy.end_replay()
    play sound 'audio/gamepause.mp3'
    show title at move_slide
    with flash
    $ renpy.notify(imageunlock)
    $ renpy.pause()

    if aineroute:
        scene black
        with dissolve
        with fade

        play music 'audio/IfItMatters.mp3'
        scene ch1ep3p2_252
        with Dissolve(2.0)
        pause
        scene ch1ep3p2_253
        with Dissolve(2.0)
        pause
        scene ch1ep3p2_254
        with dissolve
        a "{i}I'm so tired..."
        a "{i}I really don't want to work right now..."
        a "{i}I just want to sleep..."
        a "{i}And eat...!"
        a "{i}I want to be rich...!"
        a "{i}And fall in love~!"
        play sound chair2
        scene ch1ep3p2_255
        with dissolve
        a "{i}... Wait, what am I saying? I am already in love..."
        a "*sighs* I want to cuddle..."
        scene ch1ep3p2_256
        with dissolve
        a "[mc]?"
        play sound opendoor
        scene ch1ep3p2_257
        with dissolve
        mc "Yes, m'lady?"
        scene ch1ep3p2_258
        with dissolve
        a "..."
        scene ch1ep3p2_259
        with dissolve
        a "{i}Oh, [mc]... Always there for me. What am I going to do without you?"
        scene ch1ep3p2_260
        with dissolve
        a "Busy?"
        mc "Well I'm helping Klara in the kitchen. What's up?"
        a "Come here, quickly."
        play sound cloth
        scene ch1ep3p2_261
        with dissolve
        mc "Oh... something wrong?"
        a "Mm, nothing. Just be mine for a minute."
        mc "Hah, come on! For a minute? You serious?"
        scene ch1ep3p2_262
        with dissolve
        a "Is it wrong to demand a moment of your time?"
        mc "No, not at all. In fact, you're asking for too little."
        a "*giggles* This is more than enough to let me recharge..."
        mc "Don't push yourself too hard, Aine. Rest when you need it. I'm sure Sky will understand."
        scene ch1ep3p2_263
        with dissolve
        a "{i}... Am I actually regaining energy from this?"
        a "{i}No, not really."
        a "{i}That was a lie."
        a "{i}The truth is that it's my heart and mind telling me to seek his comfort."
        a "{i}It has nothing to do with recharging my energy."
        a "{i}I just want him here with me so I don't feel so alone."
        a "{i}... Am I satisfied with this? Is this enough?"
        a "{i}... Yeah, this is all I could ever ask for."
        scene ch1ep3p2_264
        with dissolve
        a "{i}But..."
        a "{i}That doesn't change the fact that he..."
        a "{i}... Was hurt by my actions and words in the past."
        scene ch1ep3p2_265
        with dissolve
        a "{i}Though we've settled it, this constant state of confusion never fades away."
        a "{i}Do I really know who I am?"
        a "{i}Or am I... the person my mother shaped for her selfish goals?"
        a "{i}Even after everything I said to him on the island..."
        a "{i}I... still don't know who I am..."
        a "{i}... I might just be living in a constant self-delusion and a never-ending spiral of self-justification..."
        a "{i}Just like this minute of embrace..."
        play sound chair2
        scene ch1ep3p2_266
        with dissolve
        mc "Seriously though, I've got something boiling in the kitchen, so I have to go now."
        mc "I'll give you more than just an energy booster later, okay?"
        a "Yeah... alright..."
        play sound doorknock
        scene ch1ep3p2_267
        with Dissolve(0.2)
        pause
        a "Come in."
        play sound opendoor
        scene ch1ep3p2_268
        with dissolve
        mc "..."
        play sound closedoor
        play sound2 keyboardtype loop
        scene ch1ep3p2_269
        with dissolve
        s "Hey, are you sure you want to keep going, Aine?"
        a "Yeah, I'm halfway through the kids' final grades and assessments. I can do this."
        scene ch1ep3p2_270
        with dissolve
        s "You're halfway, and yet look at your eyes. That's not normal."
        scene ch1ep3p2_271
        with dissolve
        a "{i}And if I stop, then what?!"
        a "{i}I don't want to be spoon-fed! I don't want to become a liability!"
        scene ch1ep3p2_272
        with dissolve
        a "Trust me, I can finish this on time."
        s "I know you're not okay. It won't hurt to tap out just this once, Aine."
        s "Think about it... After this, you still need to organize and archive student work and materials from the past academic year."
        s "Then, plan and develop the curriculum and lesson plans for next school year."
        s "You know that takes time and can't be rushed."
        scene ch1ep3p2_273
        with dissolve
        a "I know, Sky. I know..."
        a "Just... let me do this, okay? I've got it. Don't worry about me."
        s "*sighs* What am I gonna do with you?"
        scene ch1ep3p2_274
        with dissolve
        s "Alright. But do me a favor, please."
        s "Stand up, leave your PC, and come eat downstairs with me."
        a "Okay, I'll be right-"
        play sound2 woodhit
        show ch1ep3p2_275
        with hpunch
        s "No! Do it now!"
        if allornothingroute:
            s "You may be calling the shots in the harem, but I'm still your boss. And as your boss, I'm concerned about your health."
            s "I won't coddle you like [mc] does."
        a "... Okay."
        play sound chair2
        scene ch1ep3p2_276
        with dissolve
        a "..."
        scene ch1ep3p2_277
        with dissolve
        s "I just noticed, but you do look pale, and..."
        scene ch1ep3p2_278
        with dissolve
        s "Aine?"
        play sound bodyfall2
        show ch1ep3p2_279
        with hpunch
        pause
        scene ch1ep3p2_280
        with Dissolve(0.2)
        s "Ah, uhm...!"
        scene ch1ep3p2_281
        with Dissolve(0.2)
        s "[mc]! Mom! Someone! Aine needs help!"
        stop music fadeout 2
        
        scene black
        with dissolve
        with fade

        play music 'audio/LongAfterDark.mp3'
        scene ch1ep3p2_282
        with Dissolve(2.0)
        pause
        scene black
        with Dissolve(1.0)
        scene ch1ep3p2_283
        with Dissolve(2.0)
        pause
        scene black
        with Dissolve(1.0)
        scene ch1ep3p2_284
        with Dissolve(2.0)
        pause
        scene black
        with Dissolve(1.0)
        scene ch1ep3p2_285
        with Dissolve(2.0)
        pause
        scene black
        with Dissolve(1.0)
        scene ch1ep3p2_286
        with Dissolve(2.0)
        pause
        scene black
        with Dissolve(1.0)
        scene ch1ep3p2_287
        with Dissolve(2.0)
        pause
        scene black
        with Dissolve(1.0)
        scene ch1ep3p2_288
        with Dissolve(2.0)
        pause
        scene black
        with Dissolve(1.0)
        pause 1.0
        play sound chair
        show ch1ep3p2_289
        with hpunch
        a "*gasps*"
        mc "Aine? You okay? You looked like you were-"
        play sound cloth2
        show ch1ep3p2_290
        a "Mmp!"
        play sound opendoor
        show ch1ep3p2_291
        with hpunch
        pause
        show ch1ep3p2_292
        mc "Wait! We haven't... even reached the point yet..."
        play sound sinkwater loop fadein 2
        scene ch1ep3p2_293
        with dissolve
        mc "Hey, you're not... pregnant, are you? Because, you know, we haven't-"
        a "[mc], can we not do this now, please?"
        mc "I'm just trying to lighten the mood a little."
        mc "But seriously, are you going to tell me what's wrong, or are we playing the silent game?"
        stop sound fadeout 3
        play sound2 faucetsqueak
        scene ch1ep3p2_294
        with dissolve
        s "What's all the commotion? I could hear doors slamming from..."
        scene ch1ep3p2_295
        with dissolve
        s "Oh..."
        mc "You good?"
        a "Y...yeah... I'm fine now. Thanks."
        scene ch1ep3p2_296
        with dissolve
        s "*sigh* Well, isn't this perfect timing..."
        s "I've been thinking, and I've already explained your situation to management, and the director approved my request immediately."
        s "So, I'm granting you a week off, Aine."
        a "But I-"
        s "Ah-! Enough."
        s "I'm exhausted too, and I won't entertain any of your excuses. Not anymore."
        s "Take the week, rest, and recover. If I catch you so much as glancing at work, consider yourself on a longer forced break. Capiche?"
        scene ch1ep3p2_297
        with dissolve
        a "..."
        s "I've never figured out what you two see in each other, but I bet it's that shared stubborn streak."
        s "Take that as you will."
        scene ch1ep3p2_298
        with dissolve
        mc "..."
        yt "... She really can step up when it matters."
        play sound closedoor
        scene ch1ep3p2_299
        with dissolve
        mc "Well, you heard her..."
        mc "After everything we've been through, here we are, Aine. Why doubt that I'll be here for you now?"
        scene ch1ep3p2_300
        with dissolve
        a "..."
        scene ch1ep3p2_301
        with dissolve
        a "You could probably guess. It's this job of mine."
        a "Of course, I don't blame it. It is just my job, after all."
        a "But like anyone, I get tired. The exhaustion messes with my head, and when it gets too much, it drags me back to... darker times."
        play sound closedoor
        scene ch1ep3p2_302
        with dissolve
        a "Times that involve us."
        mc "Elaborate for me?"
        play sound chair
        scene ch1ep3p2_303
        with dissolve
        a "One time, I had a dream. It was like a memory of you walking away because of who I am..."
        a "Today, it was about high school..."
        mc "The high school days, huh?"
        a "Exactly."
        mc "... I understand."
        scene ch1ep3p2_304
        with dissolve
        a "It's always the same, coming out of nowhere."
        a "I can't stop it. And I don't know why it happens."
        scene ch1ep3p2_305
        with dissolve
        mc "I know why it happens."
        mc "When stressed like that, you fall back into old habits. That drags up the past, doesn't it?"
        scene ch1ep3p2_306
        with dissolve
        a "..."
        mc "..."
        menu:
            "Give her space to think":
                scene ch1ep3p2_305
                with dissolve
                mc "You know what I think?"
                mc "I think you should strongly consider taking up Sky's suggestion."
            "Attempt to lighten her mood":
                scene ch1ep3p2_307
                with dissolve
                mc "You've been pretty on edge lately, haven't you, my cranky little miss?"
                $ ainepoint += 1
                $ renpy.notify(ainenotif)
                a "You can still tease at a time like this?"
                mc "Would never miss a chance to do so."
                mc "But seriously, what do you think about Sky's suggestion?"
        mc "That week off might be just what you need to feel like yourself again."
        mc "Take a rest. You'll be back to normal sooner than you think."
        scene ch1ep3p2_308
        with dissolve
        a "It's not just about resting, [mc]. I've been so buried in work that I feel trapped."
        a "... Well, if we're being honest, I've been using work as an excuse to prevent myself from going out, even though I've been dying to."
        a "Emma's plan gave me freedom, sure, but now... I'm suffocating."
        menu:
            "Suggest a plan":
                $ aineroute = True
                scene ch1ep3p2_309
                with dissolve
                mc "That's it? You've been holding back all this because you didn't want to step outside?"
                a "[mc], it's not that simple. You know the risks if I'm seen."
                mc "But things have changed, Aine. We can manage it differently now."
                a "You mean...? Oh no, [mc], we can't possibly impose on her."
                mc "Why not? She said to ask if I needed anything."
                a "... Fine, but only if she really means it. I won't go through with it if there's even a hint of reluctance."
                mc "And I wouldn't want you to. We'll do this right, or not at all."
                mc "Deal?"
                a "Jeez... How can I say no to that? The outside world, finally..."
                a "Alright, deal!"
            "Encourage her to take time off":
                $ aineroute = False
                scene ch1ep3p2_309
                with dissolve
                mc "Alright, why don't you rest first? Once you recover, let's plan it out. How's that sound?"
                a "*sighs* A week? What am I going to do for a week?"

        label crackinganaineopen:
        if _in_replay:
            $ name = persistent.gallery_name
        scene ch1ep3p2_310
        with dissolve
        mc "Have you always been this driven?"
        a "What, are you surprised? I have to be. Living and eating aren't free, [mc]."
        mc "I knew you were dedicated, but this is... intense."
        a "Normally, it's fine, but sometimes it just gets too much."
        play sound powerdown
        stop music
        scene ch1ep3p2_311
        with Dissolve(0.2)
        pause
        mc "Not this again... How often has it happened this week?"
        a "Excluding the scheduled blackouts?"
        mc "Uh-huh...?"
        a "This is the fourth time. For unscheduled blackouts, at least."
        a "Considering that noise, it should be the whole city."
        play sound drawer
        scene ch1ep3p2_312
        with dissolve
        mc "Stay here. I'll be right back to turn on the backup power."
        play sound chair
        play music 'audio/LanternRoom.mp3'
        show ch1ep3p2_313
        a "Wait! Where are you going?"
        mc "Basement. Gonna switch on the backup generator."
        scene ch1ep3p2_314
        with dissolve
        a "No, let someone else handle it. Just... stay, please."
        mc "..."
        mc "... Okay, I'll stay."
        play sound chair
        scene ch1ep3p2_315
        with dissolve
        yt "Is she scared, or is it what I think it is?"
        scene ch1ep3p2_316
        with dissolve
        mc "Aine."
        a "Hm?"
        mc "Are you sure you're fine with just sitting like this in pitch blackness?"
        a "Y-yes... as long as you're here."
        yt "Hesitation, yet a clear admission. I'm starting to think it isn't her fear speaking."
        yt "In that case, it can only be one thing."
        scene ch1ep3p2_317
        with dissolve
        "A bemused smile flits across your face as you pick up on the true motivation behind her behavior."
        "If your hunch is correct, then these next few minutes could be a lot of fun and reveal more about Aine's personality than she knows."
        scene ch1ep3p2_318
        with dissolve
        mc "But you know, anything can happen when the lights are out..."
        "You gauge your options as you tease your fiancée with your words."
        mc "Something, or someone, can exploit your defenselessness..."
        play sound cloth
        scene ch1ep3p2_319
        with dissolve
        "You slide your fingers along her cheek, pulling her face closer."
        "Even in the darkness, you can sense the desperation in her body language."
        "As she moves closer, her hand trembles against your arm, nails digging ever so slightly into your skin."
        yt "Oh, Aine. We both know that shaking isn't because you're scared."
        play sound cloth
        scene ch1ep3p2_320
        with dissolve
        "As you finish that thought, your free hand slinks between the crease of Aine's legs."
        "Your fingers rub against her soft, smooth flesh as you grasp her inner thigh."
        "Aine lets out an audible gasp that melts into a moan, surprising even herself."
        scene ch1ep3p2_321
        with dissolve
        a "[mc]! W-what are you...?!"
        "If she could properly see your face, she would notice your audacious grin."
        yt "Surprise, Miss Agnor. I bet you were expecting a kiss, but where's the fun in that?"
        "As you internally smirk to yourself, externally, you play dumb, waiting for the perfect moment to reveal your plans for the poor girl."
        scene ch1ep3p2_322
        with dissolve
        mc "What? I thought you wanted me to stay close?"
        a "W-well-ngh!"
        "Not giving her any time to process her thoughts and feelings, your fingers squeeze her thigh."
        mc "I'm just fulfilling your desires, Aine. Wouldn't you say?"
        scene ch1ep3p2_323
        with dissolve
        "Your fingertips inch higher towards her groin. At the same time, you use your other arm to firmly pull her towards you."
        a "Oh!"
        mc "Don't worry, I'll be right beside you."
        mc "'Til death do us part."
        "Reiterating your engagement vow has an immediate effect as the warmth emanating from her nether region increases."
        "Sensing this, Aine firmly presses her thighs together in an attempt to hide her excitement from you."
        "But you have no intention of letting her hide anything."
        mc "Hey, why so tense?"
        "Your thumb grazes across her sensitive thigh skin, eliciting a twitch from your fiancée."
        mc "Relax, Aine."
        "You breathe your next words directly into her ear."
        mc "I'm not going anywhere."
        a "Ngh... s-stop..."
        play sound chair
        scene ch1ep3p2_324
        with dissolve
        "You pull her towards the wall, seeking to have Aine see the effects that this... {i}situation{/i} is having on her."
        mc "Here, maybe this will help."
        "You turn on your phone's flashlight, creating a faint but sufficient light source."
        play sound cloth
        scene ch1ep3p2_325
        with dissolve
        "Once you lay the phone down, you can appreciate Aine's subconscious reactions to your efforts so far."
        "Her face is fully flushed, as beads of sweat begin to dot her forehead."
        "And despite telling you to stop moments ago, Aine is biting her lip, a clear sign that she's just trying to hold back for propriety's sake."
        yt "I knew it. She wants this. All of it."
        scene ch1ep3p2_326
        with dissolve
        mc "Are you okay? You're looking hot."
        "Faking concern, you press your forehead against hers to \"check her temperature.\""
        "You continue to massage her inner thighs with your hand."
        a "I-I said stop, [mc]."
        "Despite her verbal objection, Aine's legs relax, allowing your hand to explore more freely."
        "But only once the time comes, of course. The buildup is half the fun."
        mc "I don't think that's what you really want, Aine."
        mc "If it is, tell me now."
        a "..."
        mc "As I thought."
        scene ch1ep3p2_327
        with dissolve
        "You wrap your arm around her waist as you advance higher up her legs."
        "You rest your fingers against the outline of Aine's vagina, then trace your finger across the fabric covering her clitoral hood."
        "Your timid fiancée jumps, taken aback by your sudden movements."
        a "[mc]! T-This is not the t-time for this!"
        mc "If you really believe that, why are you opening your legs and pressing yourself back against my fingers?"
        "Your quick retort paralyzes Aine completely as you make her aware of her own role in these circumstances." 
        "Now is the perfect opportunity to reveal your plans."
        scene ch1ep3p2_328
        with dissolve
        mc "You always act all prim and proper, but deep down, you're a naughty lady, Aine."
        "You whisper these words into her ear, shaking Aine to her core."
        "Still, that isn't enough for you."
        mc "Look how warm you already are. You were expecting \"visitors\", clearly."
        a "Aah... t-that's not true..."
        scene ch1ep3p2_329
        with dissolve
        "For a moment, Aine turns away, ashamed of her physiological responses betraying everything she built herself to be."
        "Seizing the moment, you plant a kiss on her ear, then bite the skin of her nape."
        a "A-ahh!"
        scene ch1ep3p2_330
        with dissolve
        mc "Don't lie to yourself, Agnor."
        "She trembles to your words and actions like a leaf in the wind."
        mc "Admit it. Say that you want more."
        a "..."
        "Seeing her hesitate, you offer your fiancée some \"encouragement\"."
        mc "If you don't, it will be the death of your honesty that does us apart."
        a "I..."
        mc "Say it."
        a "{size=-10}I want more..."
        mc "Like you mean it."
        a "I... I want more..."
        play sound chair
        show ch1ep3p2_331
        with hpunch
        a "Agh~!"
        "Having now dismantled her entire defenses, you grab her slender frame and effortlessly drop her onto your lap."
        play sound cloth
        scene ch1ep3p2_332
        with dissolve
        "You pull off her shorts; Aine makes no effort to stop you."
        mc "See? That wasn't so difficult, was it?"
        mc "My dear fiancée finally accepts her true desires. This is a monumental moment that calls for celebration."
        mc "And I know exactly what to do."
        "Struggling to control her accelerating respiration, Aine takes a shaky deep breath."
        scene ch1ep3p2_333
        with dissolve
        a "[mc], I'm not sure that is necessary..."
        "Her voice was quiet as if she didn't want to stop but still felt obligated to be a proper lady in front of you."
        play sound cloth2
        show ch1ep3p2_334
        with hpunch
        "Completely ignoring her apprehension, you begin kissing down Aine's neck."
        a "Ooh..."
        "Your nose grazes against your fiancée's skin, inhaling a mixture of lavender perfume blended with her natural, alluring scent."
        "The smell travels into the depths of your male mind, stoking your primal instinct to drive her wild."
        "As your excited breaths cause the hairs on sensitive skin to stand on edge, you move your fingers against the fabric of Aine's underwear."
        "You can feel the warm moisture of her pussy through the thin cloth."
        yt "Oh, the things I'll do to you, Aine Agnor..."
        scene ch1ep3p2_335
        with dissolve
        "You temporarily pause kissing her neck, leaving a bright red mark where your lips once were."
        mc "I feel what's going on down here, Aine, and I know you do too. You're ruining a perfect pair of panties, you naughty woman."
        "In perhaps a last-ditch attempt to regain her dignity and some semblance of control, Aine lashes out."
        a "S-stop teasing me! I will no-"
        play sound fistbump
        show ch1ep3p2_336
        a "Mmph~!"
        "Her protest is short-lived as you grab Aine's jaw, turning her face to meet yours."
        mc "You will do as I say."
        a "I-I..."
        play sound slap2
        show ch1ep3p2_337
        "Re-establishing control of the situation, you give her a gentle love tap on the cheek."
        a "Nhh...!"
        mc "That's what you would say, was it not?"
        "Your display of dominance causes Aine's face to grow even redder."
        "She looks away, unable to meet your eyes."
        a "Y-yes..."
        mc "Good."
        scene ch1ep3p2_338
        with Dissolve(0.2)
        "You then bury your lips into hers, muffling her shocked squeal."
        scene ch1ep3p2_339
        with dissolve
        "But instead of playing with her lips, you break away."
        "Aine opens her eyes to look at you."
        play sound chair
        show ch1ep3p2_340
        with hpunch
        "Once she does, you shove your fingers into her mouth."
        a "Hgk?"
        yt "Damn, she's going along with this a lot more than I ever expected!"
        yt "Do I want to fully capitalize on this situation and go all-out dirty talk with her?"
        yt "I have a feeling she'll go along with anything, so it really comes down to what I feel like doing."
        menu:
            "Get down and dirty":
                $ ainegetdowndirty = True
            "Keep it clean":
                $ ainegetdowndirty = False
        scene ch1ep3p2_341
        with dissolve
        if ainegetdowndirty:
            mc "You know what to do, you dirty whore."
        else:
            mc "You know what to do, Aine."
        show aine6
        with dissolve
        "With a small nod, she acknowledges that she does."
        "Your fiancée begins sucking your fingers."
        "At first, she starts slowly, getting used to the feeling of your hand in her mouth."
        "To encourage her, you rub her vagina through her panties even more intently than before."
        "The combination of your commanding words and your purposeful actions have a pronounced effect on Aine."
        "As one arm holds you for balance, the other hand snakes up her body as she grabs her own breast."
        yt "Perfect: now she's not even trying to hide her arousal."
        "She also begins sucking your fingers with fervor and passion."
        "Your growing bulge presses against your pants. Seemingly sensing this with her eyes closed, your fiancée lets out a sultry moan."
        a "Mmh..."
        "Your fingers dance with her tongue, grappling with each other in a sensual wrestling match."
        "As her arousal continues to grow, Aine begins sucking your fingers with more force."
        "Her lips for a vacuum seal around your digits, making them almost immovable."
        if ainegetdowndirty:
            mc "You like this, you nasty bawd."
        else:
            mc "You like this, don't you?"
        mc "Actually, no, you love this, all of it. I can tell."
        "Though she does not reply verbally, Aine lets out another moan. At the same time, her fingers start to play with her nipple."
        play sound cloth2
        show ch1ep3p2_342
        with hpunch
        hide aine6
        "Noticing this, you abruptly grab her hand."
        "Aine pauses and looks at you, mouth still relentlessly sucking your fingers."
        if ainegetdowndirty:
            mc "Only I may touch you in your most sensitive areas, wench."
        else:
            mc "Only I may touch you in your most sensitive areas, Aine."
        mc "Just like your entire being, those parts belong to me, and only me. Are we clear?"
        a "Mmhmm..."
        mc "I'm glad we understand each other."
        mc "Now, take off your top."
        play sound cloth
        scene ch1ep3p2_343
        with dissolve
        "Smirking in the dim light, Aine does as she is told."
        "As she pulls her top past her ribs, she pauses, exposing the very bottom of her lower breasts."
        yt "Oh ho ho, so now you're teasing me? I'm gonna absolutely ravish you."
        play sound cloth
        scene ch1ep3p2_344
        with dissolve
        "After a few seconds, which seem like an eternity, Aine finally pulls her shirt over her head."
        yt "No bra? Hmm, so you were hoping for this all along."
        scene ch1ep3p2_345
        with dissolve
        mc "Took you long enough. Now, it's my turn."
        play sound cloth
        scene ch1ep3p2_346
        with dissolve
        "You strip off your shirt in hardly any time at all, tossing it to the side."
        mc "Even in the darkness, we should have nothing to hide from each other."
        mc "That is one of the commitments we made."
        a "I...I'm beginning to see what being your fiancée means, [mc]."
        mc "And don't you ever forget: You are mine. And I am yours."
        scene ch1ep3p2_347
        with dissolve
        "Hearing those words, Aine bites her lip again."
        a "Mmm, I like the sound of that..."
        "Once again, her hand begins to travel towards her breast."
        play sound cloth2
        show ch1ep3p2_348
        "You intercept just before it can reach its destination."
        "Feigning anger, you scold her."
        mc "What did I say before?"
        "Aine gives you an annoyed pout."
        a "Come on, [mc]... I can't help it when you make me like this..."
        play sound gasp
        show ch1ep3p2_349
        a "*gasp*"
        "Realizing what she said, Aine covers her mouth in flustered shock."
        a "I-I mean-I-I-I-"
        mc "We both know exactly what you meant."
        a "I..."
        scene ch1ep3p2_350
        with dissolve
        a "Ugh, fine. No use fighting it anymore."
        mc "Exactly. Good, you're learning."
        if ainegetdowndirty:
            mc "Now spread your legs, you spoiled slut."
        else:
            mc "Now spread your legs for me, Aine."
        play sound cloth
        scene ch1ep3p2_351
        with dissolve
        "Without hesitation, your fiancée does as she is told."
        mc "Now, tell me what I should do."
        a "..."
        mc "I'm not doing anything until-"
        a "Touch me."
        mc "Touch you where?"
        a "My..."
        mc "Your what?"
        a "My... my pussy."
        mc "Say it like you actually want it!"
        play sound chair
        show ch1ep3p2_352
        with hpunch
        a "Touch my pussy! Please, I'm begging you!"
        "With a newfound determination partially driven by desperate desire, Aine heeds your instruction."
        mc "With pleasure."
        show aine7
        with dissolve
        "After removing her panties, you press your fingers against her raw flesh."
        "You glide along the length of Aine's labia, pressing gently against her opening."
        "The sound of your fingers rubbing against her warm, wet skin reverberates throughout the dark room, interrupted only by her soft moans."
        a "Nhh... ohhh..."
        yt "Fuck... I know I'm the one doing the teasing, but her reactions are {i}really{/i} turning me on."
        yt "The only thing I want to do right now is to push her limits until they collapse. All of them."
        yt "She's already come this far. Let's see how much further she can go."
        mc "Aine."
        a "Mmh... huh?"
        mc "Tell me how it feels."
        a "W... what?"
        mc "You heard me."
        a "..."
        mc "Nothing? I guess I should stop, then."
        a "{size=-10}No..."
        a "Nnh... No. Don't stop."
        mc "Then tell me."
        a "H-hot."
        mc "It feels hot?"
        a "N-no, I'm getting hotter. It feels good..."
        mc "..."
        a "Okay, I lied. It feels {i}amazing{/i}."
        mc "Amazing, huh? We haven't even gotten to the good stuff yet."
        hide aine7
        show aine8
        with dissolve
        "Suddenly, you move faster, catching Aine by surprise."
        a "Oooaaah...!"
        mc "So, what's after \"amazing\"?"
        a "Hngggh...!"
        mc "Yeah, I bet it feels \"hnggh\"."
        if ainegetdowndirty:
            mc "And yet you had the audacity to resist me just minutes ago. Look how soaked you are, my little slut."
        else:
            mc "And yet you dared to complain to me just minutes ago. Look how soaked you are."
        mc "Your pussy is practically drooling, trying to suck my fingers in. What a greedy girl."
        a "Mmnh~! W-whose f-fault do you think that is?"
        "Your fingertips continue to prod against her tight, virgin pussy. The temptation of just taking her right then and there is almost overwhelming."
        "However, you resist your urges, eager to entice more desperate reactions from your fiancée."
        mc "Whose fault? You tell me."
        a "Y-ngaahhh~! Yours!"
        mc "Mine? I'm not the one literally gushing over her fiancé's hand right now."
        a "Nghhh... you..."
        mc "But, as your fiancé, I will take responsibility for your actions."
        scene ch1ep3p2_353
        with dissolve
        hide aine8
        "Still rubbing her, you use your free hand to grab Aine's hip, pulling your lover closer to you."
        "Your hard cock presses against your pants. And with how close your bodies are, it's impossible for Aine not to feel it pressing against her back as well."
        "Even in the darkness and with her facing away, you can sense Aine's cheeks growing redder."
        a "Mmhh... [mc]..."
        scene ch1ep3p2_354
        with dissolve
        "You move forward towards Aine's ear, purring your next words directly into her soul."
        mc "I bet you want to touch it, don't you?"
        a "..."
        mc "You haven't even seen it yet. All you could do is imagine my rock-hard..."
        a "..."
        mc "Teasing you..."
        mc "{i}Taunting{/i} you..."
        mc "All while I had my way with you, licking your pussy until you couldn't take it anymore."
        show aine9
        with dissolve
        "Your words have a pronounced effect on your fiancée."
        a "Oohhh... mmmhhh..."
        "Already struggling to keep up with your attack on her pussy, Aine's breathing grows more desperate with each word."
        "You move your hand towards her breast, giving it a firm squeeze."
        a "Ahhh~!"
        "Aine's nipple hardens in response, impressing itself into the skin of your palm."
        "As you continue your sinister monologue, your fingers move towards her nipple, resting on the very tip of her hardened teat."
        mc "But now, you can't even see it."
        mc "Still, I can read your mind like a book."
        mc "Right now, you couldn't care less about seeing it."
        mc "All you want to do is wrap your hands around my cock."
        mc "To squeeze it."
        "Your fingers mirror your words, pinching Aine's bud."
        a "Nghh~!"
        mc "To rub it."
        "You trace her areola before massaging her sensitive nipple."
        mc "To feel it-to feel {i}me{/i} inside you, pushing deep into your pussy walls..."
        a "[mc], please..."
        "Aine's pleading falls on deaf ears as you continue to torment her with your relentless assault against her breasts and pussy."
        "Your middle finger slides down towards her entrance, darting inside before and gliding back up to her clit."
        "By this point, your fingertips are all pruned up because of how wet Aine is."
        "You graze your other hand along her nipple, pinching it again."
        a "Mmmph~!!"
        "You pull her nipple away from her until it pops out of your fingers."
        a "Oo-ahh~!"
        "Her breast jiggles as her nipple recoils."
        "Once again, you grab her breast firmly, the soft flesh filling your hand."
        mc "Look at you, all hot and bothered. Nipple hard enough to cut diamonds, and pussy soaked enough to drown a man."
        "You feel Aine's pussy starting to twitch against your hand, a sign that she's almost at climax."
        mc "And yet, you still so desperately want the one thing you haven't had."
        a "Nnh! [mc], s-stop teasing, please!"
        a "I-mmngh~! I c-can't take it anymore!"
        mc "Yes, you can. And you will."
        a "B-but-"
        a "Aaagh~! Hahah~! Mmmmhh!!"
        "Your fiancée's words are interrupted by her involuntary moans as her nervous system begins to send weak tremors across her body."
        yt "Shit... she's close!"
        play sound doorknock
        show ch1ep3p2_355
        hide aine9
        "Just then, you hear a loud knocking sound."
        yt "Close... but no cigar. Impeccable timing."
        "Right before she reaches her breaking point, you pull your hands away."
        a "Nghh~! Nghaa... w-what's...?"
        a "[mc]?"
        scene ch1ep3p2_356
        with dissolve
        "Confused, Aine turns to face you."
        a "W-why did you stop?"
        mc "I think we've had enough of that, haven't we?"
        a "What?! B-but-"
        scene ch1ep3p2_357
        with dissolve
        "Thinking she has understood your intentions, Aine smiles."
        a "Oh... so now you're going to finally give me what I want, right?"
        mc "Mm... not quite."
        scene ch1ep3p2_358
        with dissolve
        if ainegetdowndirty:
            a "Come on, [mc]... are you really gonna make your little slut beg for it?"
        else:
            a "Come on, [mc]... are you really gonna make me beg?"
        "Aine drags her finger along your chest."
        a "Because I am more than prepared to do so if that's what it takes..."
        stop music fadeout 5
        scene ch1ep3p2_359
        with dissolve
        mc "Nope. Didn't you hear that?"
        a "Hear what?"
        "Annoyed, Aine asks you the question somewhat incredulously."
        play sound doorknock
        "But just then, you hear another loud knock on the door, prompting you to finally get up."
        mc "That. I need to see who it is."
        a "No, you don't."
        mc "Yes, I do."
        play sound cloth
        play sound2 belt
        scene ch1ep3p2_360
        with dissolve
        "You wipe your hands off using a towel, then put your shirt back on."
        a "[mc], ignore that, and stay here! We aren't done!"
        yt "Music to my ears, my dear fiancée. Got you hook, line, and sinker."
        mc "As the only man in the house, I have to answer the door."
        mc "That's not up for negotiation, Aine. You know that."
        play sound chair
        show ch1ep3p2_361
        a "... Hmph!"
        "Aine pouts, clearly frustrated from having the show end just before the grand finale."
        yt "Dammit... that face is almost enough to make me stay!"
        yt "But I have to play the long game here. Today was just the beginning, not the main action."
        scene ch1ep3p2_362
        with dissolve
        mc "I'll check it out. Hang on."
        play sound doorcreak
        scene ch1ep3p2_363
        with Dissolve(3.0)
        play music 'audio/AreYouAlone.mp3'
        mc "Yes? Who's there?"
        scene ch1ep3p2_364
        with dissolve
        a "[mc], who is it?"
        mc "Odd. There's no one here..."
        scene ch1ep3p2_365
        with dissolve
        a "How can that be-?{w=1.0}{nw}"
        play sound waterphone3
        show keicreepyturn
        pause 1.3
        show ch1ep3p2_366
        mc "Really, it's empty. Maybe a ghost?"
        a "Stop that! You'll give me a heart attack with those creepy looks!" with hpunch
        mc "Then I'll just have to perform mouth-to-mouth on you. That wouldn't be so bad, now would it?"
        play sound chair
        scene ch1ep3p2_367
        with dissolve
        a "A-anyway, it was probably just some prankster."
        a "But seriously, go fix the lights. It can't be that dark outside."
        scene ch1ep3p2_368
        with Dissolve(2.0)
        a "..."
        show ch1ep3p2_369
        a "It is actually rather dark outside..."
        mc "Maybe it was just a prank after all."
        a "Must have been Freya or Shu up to no good, right...?"
        mc "... Couldn't be Shu. He's more scared of the dark than we are. Freya?"
        a "I doubt it."
        mc "Then who? Gwen?"
        play sound closedoor
        scene ch1ep3p2_370
        with dissolve
        un "Hey."
        play sound woodhit
        show ch1ep3p2_371
        with hpunch
        a "HUWAAAAHH~!!" (multiple=2)
        mc "GAAAAHH~!!" (multiple=2)
        show ch1ep3p2_372
        g "Calm down, it's just me! Gwen!"
        mc "What happened to your hair?!"
        g "I was sleeping, okay?"
        mc "Phew! That was a close one."
        scene ch1ep3p2_373
        with dissolve
        g "Did you guys get a door-knocker too?"
        mc "You did as well?"
        scene ch1ep3p2_374
        with Dissolve(2.0)
        a "..."
        mc "..."
        a "S-Sky's doing?"
        mc "Y-yeah, has to be..."
        play sound closedoor
        scene ch1ep3p2_375
        with dissolve
        s "Nope, not me..."
        s "I was out cold when the power cut. Then came the knocking. I ignored it the first time, but it was persistent."
        s "I opened the door to nothing. No one was there."
        g "Same here..."
        scene ch1ep3p2_376
        with dissolve
        g "Emma? Did you check with her?"
        a "It doesn't seem like something Emma would do. She was never the type to have an interest in such things."
        scene ch1ep3p2_377
        with dissolve
        mc "That leaves only one possibility..."
        scene ch1ep3p2_378
        with Dissolve(2.0)
        mc "One person left..."
        play sound thegrudge
        transform klara_grudge:
            xalign 0.5 yalign 0.1
            zoom 1.0
            linear 4.5 zoom 1.1
            xalign 0.5 yalign 0.1
            zoom 1.1
            easein 0.2 zoom 3.0
        show ch1ep3p2_379 at klara_grudge
        with Dissolve(2.0)
        pause 2.9
        stop music
        stop sound
        play sound2 screamgroup
        show ch1ep3p2_380
        with hpunch
        ev "AAAAAAAAAAAAAAAAAAAHHHHH~!!!!!"
        play music 'audio/Albatross.mp3'
        scene ch1ep3p2_381
        with Dissolve(0.2)
        k "Ahahahahahahaaaaaaa~!"
        s "Jesus, Mom! That wasn't funny~!"
        mc "Fix your eyes, goddammit!"
        scene ch1ep3p2_382
        with dissolve
        k "I...I'm so sorry, my dears! It was too tempting!"
        mc "Apologies don't prevent a heart attack."
        scene ch1ep3p2_383
        with dissolve
        g "Is this a regular thing for her?"
        mc "More often than you'd expect. Thought we'd be immune by now."
        scene ch1ep3p2_384
        with dissolve
        k "Could I have the basement key, sweetheart? You didn't hand it over when I got back."
        mc "I was on the way down myself, but here you go."
        k "Thank you, darling. I'll get the power back up. You all go rest."
        scene ch1ep3p2_385
        with dissolve
        mc "Wait, weren't you the one knocking before?"
        stop music
        show ch1ep3p2_386
        k "Huh?{w=0.8}{nw}"
        show ch1ep3p2_387
        mc "What?"
        play sound cloth2
        show ch1ep3p2_388
        a "Uhm... N-now I'm actually scared...! C-can we j-just get the lights on, please...?"
        $ renpy.end_replay()
    stop music fadeout 2
    call hide_days from _call_hide_days_9
    with dissolve

    if aineroute:
        scene black
        with dissolve
        with fade

        show screen day_saturday with dissolve
        play music 'audio/RiverLume.mp3'
        scene ch1ep3p2_389
        with dissolve
        mc "Moon... I'm not sure that's the right look for where we're going."
        scene ch1ep3p2_390
        with dissolve
        a "It's unique, but..."
        a "Have you ever actually been on a date? Even a normal, ordinary date?"
        m "No, why would I have? Have you been on many?"
        a "A handful. My mother used to orchestrate these tiresome dinner dates with potential suitors."
        scene ch1ep3p2_391
        with dissolve
        m "So, does attire make a difference? My job is only to ensure your safety, after all." 
        a "About that: you're not just our bodyguard. You're representing us, meaning you must dress the part!"
        scene ch1ep3p2_392
        with dissolve
        mc "Isn't there something a bit more... everyday casual in your wardrobe?"
        m "This is my version of casual."
        mc "Maybe... but something that looks more balanced would be ideal."
        m "Balanced? I'd say this is balanced. Functional, too."
        scene ch1ep3p2_393
        with dissolve
        a "Your jeans are torn... You're missing an entire pant leg! You call that balanced?!"
        m "It's by design. Freedom of movement and all that."
        a "God... You're even more challenging than Emma when it comes to fashion..."
        mc "You have no idea, Aine. She and I have already been through this before."
        scene ch1ep3p2_394
        with dissolve
        a "Pick anything else, just... not this outfit, please!"
        m "Vetoed. The last time I wore what you call \"normal\" clothes, I felt like I was in a straitjacket."
        a "What exactly do you need to move that \"freely\" for in a café?"
        m "You never know."
        a "This isn't negotiable. Go change."
        a "I'll help with your hair. Trust me, you'll look great."

        scene black
        with dissolve
        with fade

        play sound cloth
        scene ch1ep3p2_395
        with dissolve
        a "Goodness..."
        a "You look... stunning."
        scene ch1ep3p2_396
        with dissolve
        m "Stunning in what way?"
        a "Like you're the one going on a date. You clean up nicely, rookie."
        m "I have a name."
        a "Of course, Moon. Honestly, it suits you. You might want to consider a wardrobe update."
        scene ch1ep3p2_397
        with dissolve
        m "I appreciate the sentiment, but this garb is a shackle."
        m "Every gram matters. Any flair could be a liability."
        m "I need my gear to be utilitarian, not this... vile get-up."
        a "*sighs* There's no getting through to you..."
        play sound closedoor
        scene ch1ep3p2_398
        with dissolve
        mc "Alright, the truck's warmed up. Are we ready to roll out?"
        play sound cloth2
        show ch1ep3p2_399
        a "Just wait till you see her!"
        mc "Hang on... Who's this now?!"
        scene ch1ep3p2_400
        with Dissolve(0.2)
        m "..."
        mc "Kidding, kidding..."
        scene ch1ep3p2_401
        with dissolve
        a "Are you good to go?"
        m "One second..."
        stop music fadeout 4
        play music2 'audio/ParticleEmission.mp3' fadein 4 loop
        play sound casepickup
        scene ch1ep3p2_402
        with dissolve
        mc "Hm?"
        play sound casedown
        scene ch1ep3p2_403
        with dissolve
        a "You're not seriously bringing that, are you? Weapons? Now?"
        m "A precaution."
        mc "You've been with us this long without so much as a scuffle. Why the need?"
        m "Because today's different. Today, I'm responsible for you and what's precious to you."
        play sound caseopen
        scene ch1ep3p2_404
        with dissolve
        a "That's... whoa..."
        mc "The sparkles in your eyes tell me a whole lot of stories about where you came from..."
        scene ch1ep3p2_405
        with dissolve
        pause
        scene ch1ep3p2_406
        with dissolve
        pause
        scene ch1ep3p2_407
        with dissolve
        mc "..."
        mc "So... what are they?"
        scene ch1ep3p2_408
        with dissolve
        m "An artifact from long ago. An extension of myself."
        mc "Are they identical?"
        m "Similar, but not the same. One's a replica without a sharpened edge, the other..."
        m "A tally of the thousands of lives I've ended."
        scene ch1ep3p2_409
        with dissolve
        mc "..."
        a "..."
        play sound woosh2
        show ch1ep3p2_410
        pause 0.8
        show ch1ep3p2_411
        mc "That the genuine one?"
        m "Yes."
        mc "... You've always been more than enough without it."
        scene ch1ep3p2_412
        with dissolve
        pause
        play sound casepickup2
        scene ch1ep3p2_413
        with Dissolve(0.2)
        pause
        scene ch1ep3p2_414
        with dissolve
        m "I'll keep that in mind... Commander..."
        stop music2 fadeout 2

        scene black
        with dissolve
        with fade

        play sound2 cityalley loop
        play sound3 car_idle loop
        scene ch1ep3p2_415
        with dissolve
        pause
        play music 'audio/JamboMambo.mp3'
        play sound woosh
        show ch1ep3p2_416
        g "Holy shit! You look like you're about to crash a funeral!"
        scene ch1ep3p2_417
        with dissolve
        mc "Seems like that's Aine's vision of \"casual\"."
        g "Who knew you had a soft spot for the macabre, Aine?"
        a "It's called having a sophisticated palette, Gwen."
        g "Tomato, tomahto..."
        scene ch1ep3p2_418
        with dissolve
        k "Black is quite the elegant choice, dear."
        scene ch1ep3p2_419
        with dissolve
        a "{i}Wow... I didn't realized she's this tall until now."
        show ch1ep3p2_420
        a "See? Someone here has taste, unlike you, saltymilk!"
        scene ch1ep3p2_421
        with dissolve
        a "Thanks, Klara-{w=0.7}{nw}"
        play sound woosh
        show ch1ep3p2_422
        a "I mean, what?"
        play sound woosh
        show ch1ep3p2_423
        mc "What?"
        play sound woosh
        show ch1ep3p2_424
        a "Okay."
        mc "You were crying when I slid that ring onto your finger not so long ago... and now..."
        scene ch1ep3p2_425
        with Dissolve(0.2)
        g "Ugh... this is why I hate kids..."
        scene ch1ep3p2_426
        with dissolve
        mc "So, what's on the agenda for you two?"
        k "Just quickly showing Gwen the ropes at the company. A regular day."
        mc "Cool. Stay safe, you two."
        k "And you be safe as well, darling. Call me if you'll miss dinner, okay?"
        scene ch1ep3p2_427
        with dissolve
        mc "I doubt we'll be out past sunset, right?"
        a "We'll be back in time for your cooking, Miss Klara."
        k "Just Klara. No need for honorifics anymore, Aine."
        a "O-okay... Klara."
        scene ch1ep3p2_428
        with dissolve
        mc "Hmmm?"
        a "What...?!"
        scene ch1ep3p2_429
        with dissolve
        k "Moon, dear, keep them all in one piece for me."
        m "Understood. They're in good hands."
        stop sound2 fadeout 2
        stop sound3 fadeout 2

        scene black
        with dissolve
        with fade

        play sound2 traffic loop
        play sound3 streetcrowd loop
        scene ch1ep3p2_430
        with dissolve
        mc "Relax, the truck isn't too far from here."
        a "Well... it should be right around here somewhere."
        mc "You've been there before?"
        a "Yes, with my mother. But that was ages ago, back in primary school."
        mc "So, hazy memory?"
        a "You could say that. But it's The Rustic Stave - a classic. My memory never fails me with the classics."
        scene ch1ep3p2_431
        with dissolve
        a "According to the map, we're right on the spot, but..."
        mc "What's the name again?"
        a "The Rustic Stave. This place is Alla Moda, though. More boutique than a bar."
        mc "Alla Moda? That's no watering hole. Isn't it a high-end clothing store?"
        a "Exactly. And it's owned by... her."
        mc "Her?"
        a "My mother..."
        mc "Wait, your mom owns Alla Moda?!"
        a "I was hoping she hadn't replaced The Rustic Stave with... this."
        scene ch1ep3p2_432
        with dissolve
        pause
        scene ch1ep3p2_433
        with dissolve
        a "Excuse me, sorry to bother you, but do you happen to know where The Rustic Stave is?"
        a "We're a bit lost. It was supposed to be right here."
        scene ch1ep3p2_434
        with dissolve
        yu "Oh, The Rustic Stave? Yes, I'm quite the regular there. They relocated it a few blocks from here."
        a "Really? That's a relief."
        a "Could you point us in the right direction?"
        yu "Absolutely! But I must warn you, the management is a bit-{w=2.0}{nw}"
        stop music
        play sound scream_female3
        show ch1ep3p2_435
        with hpunch
        wom "AAAAAAAAAHHH~!!!"
        mc "What in the world?"
        scene ch1ep3p2_436
        with Dissolve(0.2)
        yu "Something's wrong. Let's check it out."
        mc "Careful, it could be dangerous!"
        stop sound2 fadeout 1
        stop sound3 fadeout 1
        play sound handguncrack
        play music 'audio/Backweight.mp3'
        scene ch1ep3p2_437
        with Dissolve(0.2)
        gun "Nobody moves, or I swear I'll kill this woman!"
        scene ch1ep3p2_438
        with dissolve
        a "Oh my God, this is serious!"
        mc "Holy shit, that dude is huge!"
        play sound handgunmovement
        show ch1ep3p2_439
        gun "You!"
        yu "Me?"
        gun "Are you deaf? Yes, you! Get over here, now!"
        scene ch1ep3p2_440
        with Dissolve(0.2)
        yu "Listen, I don't want any trouble. I just-"
        gun "Shut it! You're part of this now. You're going to do exactly as I say." with hpunch
        show ch1ep3p2_441
        a "*whispers* [mc], what do we do? We can't let this escalate further."
        m "*whispers* On standby for your orders, commander."
        scene ch1ep3p2_442
        with dissolve
        yt "Do I really have time to help?"
        yt "... Well, I can't just step away when this girl showed us kindness, can I?"
        yt "The real question is..."
        yt "Do I have it in me to solve this without compromising the situation?"
        mc "..."
        scene ch1ep3p2_443
        with dissolve
        mc "*whispers* Do you guys trust me?"
        m "*whispers* Yes."
        a "*whispers* Mhm."
        mc "*whispers* Alright, I can't fully control the situation, but I still want you to listen."
        show ch1ep3p2_444
        with hpunch
        gun "Hey! Did you not hear me?! Come here, RIGHT. NOW!"
        show ch1ep3p2_445
        mc "*whispers* Don't move a muscle and stay right where you are."
        yu "*whispers* Okay..."
        scene ch1ep3p2_446
        with dissolve
        mc "*whispers* Watch. She's my most prized possession."
        yu "*whispers* Huh?"
        scene ch1ep3p2_447
        with dissolve
        a "Let them go. I'll take their place. You don't have to involve anyone else."
        gun "Why should I trust you?"
        a "Because I'm here, willingly stepping in. What do you want?"
        play sound woosh2
        show ch1ep3p2_448
        with hpunch
        hos "Ahhh!"
        gun "Fine! You, come closer!"
        scene ch1ep3p2_449
        with dissolve
        hos "T-thank you!"
        a "Piss off, wuss."
        hos "O-okay!"
        scene ch1ep3p2_450
        with dissolve
        a "What's your name? Why are you doing this?"
        gun "Shut up and get over here!"
        a "Not until you answer the question."
        scene ch1ep3p2_451
        with dissolve
        gun "..."
        scene ch1ep3p2_452
        with dissolve
        a "..."
        show ch1ep3p2_453
        gun "... F-fine."
        gun "Names don't matter. And I..."
        gun "I need money, okay? Everything's gone wrong."
        a "I get it. Life can be overwhelming. But there must be a better way to react than this."
        play sound woosh2
        show ch1ep3p2_454
        with hpunch
        gun "You don't know anything about my life!"
        a "Maybe not. But I do know what despair looks like. I see it in your eyes."
        a "You're not a bad person. You're just desperate."
        scene ch1ep3p2_455
        with dissolve
        gun "Y-you think you can read my mind, huh? You don't know me!"
        scene ch1ep3p2_456
        with dissolve
        a "I don't. But I do know that hurting others or yourself isn't the answer."
        a "What happened to you? What brought you so low that you think this is your only option?"
        play sound handgunmovement
        show ch1ep3p2_457
        with hpunch
        gun "Shut up! You don't understand!"
        a "I understand more than you think I do. I see a man who's lost, who thinks there's no hope. But this? This is just cowardice."
        gun "Stop... stop saying that!" 
        scene ch1ep3p2_458
        with Dissolve(0.2)
        a "It's the truth. You're acting out of fear."
        a "You think this gun gives you power? But no, All it does is reveal your weakness."
        a "Look at you, a pathetic being clinging to a gun because you can't face your failures."
        a "You're not just desperate: you're pitiful. Using threats to feel important? That's just sad."
        gun "I... I..."
        scene ch1ep3p2_459
        with dissolve
        a "You what? Can't handle the truth?"
        a "You're a coward, hiding behind a weapon, thinking it makes you strong."
        a "It's truly laughable. You're nothing but a scared little boy, trembling at the thought of facing the real world."
        scene ch1ep3p2_460
        with dissolve
        a "And let's not forget why you couldn't find a job. It's not because there weren't any; you just weren't good enough for them."
        a "You probably walked into every interview already defeated, reeking of desperation and incompetence."
        a "Employers can smell failure a mile away. And you? You're drenched in it."
        a "Is that why you're doing this? To prove to yourself that you can accomplish something, even if it's just terrorizing innocent people?"
        play sound thud3
        show ch1ep3p2_461
        with hpunch
        gun "Stop... Please..."
        scene ch1ep3p2_462
        with dissolve
        a "Oh, now you want pity? After all this? After threatening an innocent woman and dragging us into your mess?"
        a "You don't deserve pity. You don't deserve understanding. You don't deserve to live."
        a "You're just a pathetic, sniveling mess."
        a "You call yourself a man? A man faces his problems. You're just a child playing with a gun."
        play sound handgunmovement
        show ch1ep3p2_463
        with hpunch
        gun "Hrrnn!"
        scene ch1ep3p2_464
        with dissolve
        a "Go ahead. Do you think I care?"
        a "You pull that trigger, I'm finally free from this god-forsaken life. It's a win for me."
        a "My life, your life, it doesn't matter anymore, does it?"
        a "But think about it. What will you gain by shooting me? A moment of control? Is it worth it?"
        a "Think about the consequences. You shoot me, and then what? Police swarm in and arrest you in front of everyone, sweeping away the only shards of dignity you have left."
        a "Then you rot away your life in jail-if you're lucky."
        a "If someone decides to take their anger out on you, or make you their prison slave, you'll find yourself begging for the merciful release that death provides."
        a "And your family... do they know what you've been reduced to? What will this do to them?"
        scene ch1ep3p2_465
        with dissolve
        gun "I... I don't have a choice..."
        a "You always have a choice. This isn't just about you. It's about everyone you're dragging down with you."
        gun "My family... I didn't think..."
        a "See? There's more to this than just your own pain. Think about who else gets hurt."
        gun "Maybe... maybe I'm the one who should be... No, I can't even do this right..."
        a "That's not the answer either. Hurting yourself won't fix anything."
        a "It's not too late to make a different choice."
        play sound handgunmovement
        show ch1ep3p2_466
        with hpunch
        gun "NO, I SHOULD END THIS RIGHT HERE, RIGHT NOW!"
        stop music fadeout 1
        play sound criticalenter
        show ch1ep3p2_466a
        with Dissolve(0.1)
        pause 0.2
        transform kei_critical1:
            xalign 0.7 yalign 0.2
            zoom 1.0
            linear 30.0 zoom 1.2
        show ch1ep3p2_467 at kei_critical1
        with dissolve
        play music 'audio/CriticalThinking.mp3'
        yt "Shit! Aine's words didn't work as intended."
        yt "No, I should keep it calm..."
        yt "Think, [mc], think. There must be a way to defuse this without hurting anyone."
        transform kei_critical2:
            xalign 0.2 yalign 0.9
            zoom 1.0
            linear 30.0 zoom 1.2
        show ch1ep3p2_468 at kei_critical2
        with Dissolve(2.0)
        pause
        yt "..."
        yt "A pebble? That's all we have?"
        yt "It might be enough, but I can't direct Moon fast enough in this situation."
        yt "I don't know how strong she is yet, so we can't risk hitting him directly either."
        show ch1ep3p2_469 at kei_critical1
        with Dissolve(2.0)
        yt "If Moon aims for his hand or the gun, it could cause a reflex that would make him pull the trigger. That would certainly escalate things."
        yt "I don't know what we're in for, then..."
        yt "We only need something to knock him out."
        transform kei_critical3:
            xalign 0.5 yalign 0.3
            zoom 1.0
            linear 30.0 zoom 1.2
        show ch1ep3p2_470 at kei_critical3
        with Dissolve(2.0)
        yt "Something... to knock him out..."
        yt "That... That's what we need!"
        stop music
        play sound hit5
        show ch1ep3p2_471
        with hpunch
        pause
        play music 'audio/Ambushed.mp3'
        transform kei_critical4:
            xalign 0.5 yalign 0.3
            zoom 1.0
            linear 30.0 zoom 1.2
        show ch1ep3p2_474 at kei_critical4
        with Dissolve(2.0)
        pause
        show ch1ep3p2_473
        with hpunch
        m "*shivers*"
        show ch1ep3p2_472 at kei_critical4
        with dissolve
        mc "Look at me. This isn't the way out that you think it is..."
        show ch1ep3p2_475
        gun "W-what do you fucking know?!"
        yt "I got his attention!"
        play sound woosh4
        show ch1ep3p2_476
        pause 0.4
        play sound3 gravelslide
        show ch1ep3p2_477
        yt "Now, Moon! It's now or never!"
        m "Thank thee for the blessing, the vigor I wield..."
        scene ch1ep3p2_478
        with dissolve
        m "In the day's honest toil, across the expansive field..."
        play sound garbagecancrash2
        show ch1ep3p2_479
        with hpunch
        m "May the soft day enfold each toil and endeavor..."
        show ch1ep3p2_480
        gun "What the-?"
        m "As I fulfill my role, the bringer of light."
        show moonchargeslash
        pause 8.0
        play sound thud3
        show ch1ep3p2_481
        with hpunch
        hide moonchargeslash
        pause
        play sound2 katanasheath
        show ch1ep3p2_482
        with dissolve
        m "Amen."
        scene ch1ep3p2_483
        with dissolve
        mc "She's not human... I didn't even see her move."
        a "That was incredible... She just used the hilt of her sword and then he collapsed."
        scene ch1ep3p2_484
        with dissolve
        mc "What do you have, eagle eyes? How could you catch that?"
        a "Maybe I'm just more observant than you. Or maybe you need glasses."
        mc "Observant or superhuman? She was faster than a blink."
        a "Well, we can't all be as quick as her, but some of us can keep up."
        mc "I'll believe it when I see it - which, at this rate, will be never."
        stop music fadeout 2

        scene black
        with dissolve
        with fade

        play music 'audio/Nemesis.mp3'
        play sound2 traffic loop
        play sound3 streetcrowd loop
        scene ch1ep3p2_485
        with dissolve
        off "Alright, tell me what happened."
        scene ch1ep3p2_486
        with dissolve
        mc "We were near Alla Moda when we heard a scream. That's when we saw the man with the gun."
        off "Was he making any specific threats or demands?"
        a "He appeared desperate, threatening the woman he had grabbed. Mainly for money, it seemed."
        off "And how did you become involved?"
        scene ch1ep3p2_487
        with dissolve
        a "I offered to switch places with the hostage. I hoped to de-escalate the situation through negotiation."
        off "While I understand your intentions, such actions can be hazardous and unpredictable."
        a "It was a spur-of-the-moment decision. He was on the brink of doing something to the woman, and I felt it was the only way to calm him down."
        mc "Aine managed to get him to release the hostage, but then he turned the gun on himself."
        off "That's a highly volatile situation. How was it resolved without any shots?"
        scene ch1ep3p2_488
        with dissolve
        m "I used a pebble to create a distraction. The noise diverted his attention at the critical moment."
        off "Resourceful, but such actions could have escalated the situation, young lady. It's risky to intervene like that."
        off "And your sword: it's not a real weapon, is it?"
        scene ch1ep3p2_489
        with dissolve
        m "No, officer, it's just for cosmetic purposes."
        off "You seem to know how to wield it properly and took down the suspect despite it being a cosmetic. Care to explain?"
        scene ch1ep3p2_488
        with dissolve
        m "I am these two's hired bodyguard. I just did what's written in my job description."
        off "From what agency, may I ask?"
        m "From \"Sicae Agency\"."
        off "I see. No more questions, then."
        yt "Wait, what...?"
        scene ch1ep3p2_490
        with dissolve
        off "Look, while I appreciate that a worse outcome was avoided, I must emphasize that intervening in situations where the suspect is armed is extremely dangerous."
        off "You put yourselves and the original victim at greater risk."
        off "In the future, the best course of action is to ensure your safety and call us. Allow the professionals to handle the situation."
        mc "We understand, officer."
        off "My partner will take your statements for the official report. I appreciate your cooperation, and please be more cautious in the future."
        play sound cardriveaway
        scene ch1ep3p2_491
        with dissolve
        pause
        scene ch1ep3p2_492
        with dissolve
        a "..."
        mc "What's wrong?"
        scene ch1ep3p2_493
        with dissolve
        a "I keep replaying the words I said to him. They were... incisive and ruthless."
        a "Yes, they helped defuse the situation, but the ease with which I said each word... it scares me."
        mc "Aine, in that moment, you did what you thought was necessary."
        a "That's just it, though: my words had a cruel effect. They almost drove the man to a mental breakdown."
        a "There's a part of me that can be so detached, so analytical. It's a side I'm scared of."
        a "It worked out this time, but what about the future? It could just as easily do harm instead of good."
        a "It's a part of me my mother created for her own purposes, and..."
        scene ch1ep3p2_494
        with dissolve
        mc "And what?"
        a "... You know better than anyone. The damage I've done, the people I've hurt, including you. Especially you."
        a "[mc], I just..."
        mc "Tell me."
        scene ch1ep3p2_495
        with dissolve
        a "I don't know which part of me is really \"me\". The one I want to be, or the one I fear I've become."
        scene ch1ep3p2_496
        with dissolve
        mc "..."
        stop music
        stop sound2
        stop sound3
        show ch1ep3p2_497
        play sound lpapa
        un "Papa~!"
        play music 'audio/StarryEyed.mp3'
        scene ch1ep3p2_498
        with dissolve
        mc "!!!"
        scene ch1ep3p2_499
        with dissolve
        mc "..."
        scene ch1ep3p2_500
        with dissolve
        mc "Did you guys hear that?"
        a "Hm?"
        m "I didn't hear anything."
        scene ch1ep3p2_501
        with dissolve
        foff "Alright, you kids. Let's get this done so that you can carry on with your day."
        stop music fadeout 2

        scene black
        with dissolve
        with fade

        play sound2 pubambience loop
        scene ch1ep3p2_502
        with dissolve
        yu "Well, this is the place."
        scene ch1ep3p2_503
        with dissolve
        a "It hasn't changed one bit. Thanks for guiding us here, Yuki."
        yu "Yeah, no big deal. But I think I'll head home after everything that has happened."
        yu "I'm surprised you all treat this like water off a duck's back. After a situation like that, I'd be a wreck."
        scene ch1ep3p2_504
        with dissolve
        yt "That is strange, actually. Moon's calmness was expected, but Aine...?"
        yt "She's usually not this composed in intense situations. Is she hiding something from me?"
        scene ch1ep3p2_495
        with flash
        a "I don't know which part of me is really \"me\". The one I want to be, or the one I fear I've become."
        scene ch1ep3p2_504
        with flash
        mc "..."
        yt "What has Hera exposed her to? How deep does it go...?"
        scene ch1ep3p2_505
        with dissolve
        yu "I'll leave you to it, then. Stay safe, okay?"
        a "You too, Yuki. Take care."
        scene ch1ep3p2_506
        with dissolve
        mc "I'll be right back. I need to use the restroom."
        a "Alright, but don't take too long." 
        scene ch1ep3p2_507
        with Dissolve(0.2)
        a "Okay, where should we-"
        scene ch1ep3p2_508
        with dissolve
        pause
        a "Ah, you've already picked a table..."
        scene ch1ep3p2_509
        with dissolve
        m "It's the most secure spot here."
        a "Secure? How can you tell?"
        m "Vantage point. It's deep within the pub, giving me a clear view of any incoming threats."
        a "But wouldn't it be safer to sit closer to the exit for a quick escape?"
        m "If I can anticipate an attack, getting to the exit won't be a problem."
        a "I see..."
        play sound chair3
        scene ch1ep3p2_510
        with dissolve
        a "Thanks for earlier. Without you, it could have gotten ugly."
        m "You're the one who took charge. We were just your support."
        a "I just wish I had your strength."
        scene ch1ep3p2_511
        with dissolve
        m "I don't get why people always want to be something. To become someone."
        m "Physical strength isn't everything. You have your own strengths."
        a "Well..."
        m "Life has taught me that you can't be everything. We follow the paths set before us, unable to change our destiny."
        m "To defy that... you'd have to be a deity."
        a "Where did you get that philosophy?"
        m "From someone very wise and very old."
        m "And trust me, my path is not one you'd want to walk, Aine Agnor."
        play sound chair4
        scene ch1ep3p2_512
        with dissolve
        a "... You're one of {i}them{/i}, right? What do you actually know about me?"
        m "Other than your thing with [mc]? Everything. You are Hera's daughter, after all."
        a "I thought so."
        scene ch1ep3p2_513
        with dissolve
        m "Don't play ignorant, Aine. You know who I am."
        a "So you can make that kind of expression. I thought you're just a worse version of Emma."
        a "Well, sort of... I knew your codename, but never thought you were real."
        a "I mean... I only learned about Aunt Jess recently. I've been playing it by ear, so I'm still piecing things together."
        a "Once you came, I think I got the gist of what happened."
        a "So... where are you hiding it?"
        m "Hiding what? What are you trying to do, Agnor?"
        a "Now looks who's trying to play ignorant..."
        scene ch1ep3p2_514
        with Dissolve(0.2)
        mc "Seems like you two are getting along. What's the topic?"
        a "U-uhm..."
        m "Just girl talk."
        mc "Ah, got it."
        scene ch1ep3p2_515
        with dissolve
        a "*chuckles*"
        scene ch1ep3p2_516
        with dissolve
        a "*whispers* Sorry. I didn't mean to pry."
        play sound chair3
        scene ch1ep3p2_517
        with dissolve
        mc "Shall we order?"
        a "Absolutely!"
        m "I'm starving."
        scene ch1ep3p2_518
        with dissolve
        mc "Didn't you have breakfast earlier?"
        m "My services require substantial sustenance. Feeding me is non-negotiable."
        mc "I see, your aid ain't free, after all..."
        scene ch1ep3p2_519
        with dissolve
        a "Is that why you're not any taller?"
        m "..."
        a "Sorry..."
        scene ch1ep3p2_520
        with dissolve
        mc "Hey, I just noticed. Where's your ring?"
        a "Oh, it's safe in my pocket. I slipped it off earlier when we were near Alla Moda."
        a "I didn't want to risk showing it off in a street I'm not too familiar with, especially not something that precious."
        mc "Well... it was probably a good idea."
        scene ch1ep3p2_521
        with dissolve
        a "Still, it feels odd not wearing it."
        mc "*chuckles* Just don't get too comfortable without it."
        a "Don't worry, I won't. It's a part of me now."
        stop sound2 fadeout 2

        scene black
        with dissolve
        with fade

        label ainepubtensionbuildup:
        if _in_replay:
            $ name = persistent.gallery_name
        play sound2 pubambience loop
        scene ch1ep3p2_522
        with dissolve
        a "It's been thirty minutes already! Where is our food?"
        mc "Relax, Aine. It's busy today. The kitchen's probably swamped."
        yt "She's right, though. The hell is going on in the kitchen?"
        play sound chairdrag
        scene ch1ep3p2_523
        with dissolve
        m "I'm going to take a quick look around to ensure everything's in order."
        mc "That's not necessary, Moon..."
        m "Better safe than sorry. I'll be back shortly."
        scene ch1ep3p2_524
        with dissolve
        a "So, [mc]... about earlier, in the alley-"
        scene ch1ep3p2_525
        with Dissolve(0.2)
        a "..."
        mc "..."
        scene ch1ep3p2_526
        with dissolve
        a "... Well then, like I was saying-"
        scene ch1ep3p2_525
        with dissolve
        mc "..."
        play sound woodhit
        show ch1ep3p2_527
        with hpunch
        a "[mc], are you even listening to me?"
        scene ch1ep3p2_528
        with Dissolve(0.2)
        a "!!!"
        play music 'audio/HardFlirtation.mp3'
        show ch1ep3p2_529
        with dissolve
        pause 0.4
        scene ch1ep3p2_530
        with dissolve
        pause
        play sound woodhit
        show ch1ep3p2_531
        with hpunch
        pause
        mc "Sorry, what were you saying? I got lost in thought for a moment there."
        mc "Or maybe I was lost in your eyes..."
        scene ch1ep3p2_532
        with dissolve
        a "*whispers* [mc], right here?! Really?!"
        mc "Hold on. I think I might have spilled some beer."
        scene ch1ep3p2_533
        with dissolve
        pause
        scene ch1ep3p2_534
        with dissolve
        pause
        scene ch1ep3p2_535
        with dissolve
        pause
        scene ch1ep3p2_536
        with dissolve
        mc "There we go. That hit the {i}spot{/i}." #
        scene ch1ep3p2_537
        with dissolve
        yt "Yeah, that blackout sure was perfect timing."
        mc "You seem a bit out of sorts there, Aine. Is everything okay?"
        a "Mmh... y-yes..."
        mc "Still, we should probably freshen you up before we eat. Just to be sure."
        scene ch1ep3p2_538
        with dissolve
        a "*panting* Yeah, maybe you're right... so... you...you better follow me."
        play sound chairdrag
        scene ch1ep3p2_539
        with dissolve
        pause
        scene ch1ep3p2_540
        with dissolve
        mc "Cheers."
        play sound gulp
        scene ch1ep3p2_541
        with dissolve
        pause
        play sound mugdown
        scene ch1ep3p2_542
        with dissolve
        pause
        play sound cloth
        scene ch1ep3p2_543
        with dissolve
        pause
        play sound chairdrag
        scene ch1ep3p2_544
        with dissolve
        yt "Eyes on the prize, baby!"
        stop sound2 fadeout 2

        scene black
        with dissolve
        with fadeq

        play sound closedoor2
        scene ch1ep3p2_545
        with dissolve
        pause
        scene ch1ep3p2_546
        with dissolve
        mc "Praise the maiden in black!"
        scene ch1ep3p2_547
        with dissolve
        mc "Holy shit, Aine... look at you, all ready and dripping!"
        play sound cloth2
        show ch1ep3p2_548
        with hpunch
        "As soon as you finish speaking, Aine jumps at you like a hungry, feral beast ambushing its prey."
        "She latches onto your lip, almost biting your tongue, sucking it {i}hard{/i}."
        "You sense the surge of her emotions through the deep kiss."
        "Her erratic tongue movements punctuate her released stress, desperation, and raw lust."
        scene ch1ep3p2_549
        with dissolve
        "From what already happened, you understand perfectly what she's feeling: the overwhelming desire just to let everything go."
        "It's clear how ravenous she is for you."
        "However, your heart softens at how much care and restraint she shows despite her release of pent-up desire."
        "She craves you-every inch of you-but doesn't want to hurt you."
        "The sheer effort that it takes to hold back after days-no, years-of waiting for this moment with you must be overwhelming."
        "However, Aine shows no signs of losing her composure: only a desire to deepen the kiss, to savor every second."
        scene ch1ep3p2_550
        with dissolve
        yt "I've said it before, but I'll say it again..."
        yt "Holy shit! What is this?!"
        yt "If this isn't evidence of how much I mean to her, then I don't know what is!"
        scene ch1ep3p2_551
        with dissolve
        "Aine pulls away and looks deep into your eyes."
        "She opens her mouth as if to say something..."
        "... But no words come out. Instead..."
        scene ch1ep3p2_552
        with dissolve
        "... She grabs your hand and places it over her left breast, looking at you with pleading eyes."
        "You feel the deep thumping of her heart as she stares into your depths, looking for a sign that you're on the same page as her."
        yt "Oh fuck! She wants to do it! Right here?! Now?!"
        mc "Aine, this isn't the best place to-"
        play sound cloth2
        show ch1ep3p2_553
        with hpunch
        "Ignoring you, Aine starts kissing your neck while using one hand to guide yours over the crest of her breast." 
        scene ch1ep3p2_554
        with dissolve
        "She squeezes your hand, as if begging you to massage her." #
        "You can feel her erect nipple under the fabric of her bra, which doesn't help your already rock-hard member."
        play sound cloth
        scene ch1ep3p2_555
        with dissolve
        "She starts undoing your shirt with urgency. She needs more of you: as much as she can possibly have." 
        "You feel her hands trembling as she attempts to grasp it, and it takes a few tries before she manages to grab the hem."
        yt "Hold on. Something's wrong here. No, something's wrong with her."
        play sound cloth
        scene ch1ep3p2_556
        with dissolve
        "After she removes your shirt, she runs her hands over and across your newly exposed chest and abs." 
        "As she pants, you feel her warm breath on your skin, raising goosebumps all over your body."
        "Sweat begins to form, causing her light complexion to glisten."
        play sound cloth
        scene ch1ep3p2_557
        with dissolve
        "As if to combat this effect, or perhaps accentuate it, Aine lifts her bra above her breasts, exposing her hardened rosy pink buds." 
        a "H-hot... so hot..."
        scene ch1ep3p2_558
        with dissolve
        "Aine looks down and sees the bulge in your pants. She grins mischievously, dropping to her knees before you as she smiles." 
        "Unwilling to waste any more time, she starts undoing your bottoms with lightning speed."
        "Like a woman possessed, she is desperate to get to what's underneath."
        play sound belt
        scene ch1ep3p2_559
        with dissolve
        "Before you know it, Aine has your pants off. Your cock springs free, hard and throbbing." 
        yt "Shit! This isn't like her!"
        yt "I know where her desperation is coming from: We didn't get to finish last time! Her stress has been piling up recently, too!"
        yt "Arrgh, fuck! What have I done?!"
        yt "I need to stop her before she does something she will regret later!"
        "Aine stares at your manhood for a moment, her mouth already watering."
        scene ch1ep3p2_560
        with dissolve
        "Then she looks up at you, her bright eyes saturated with lust." 
        yt "But... can I really stop myself after seeing her pleading eyes?"
        scene ch1ep3p2_561
        with dissolve
        a "I need this... I need all of you..." 
        mc "Aine... a-are you sure? This place? In here?"
        a "I don't care... I don't need it to be somewhere special..."
        scene ch1ep3p2_562
        with dissolve
        "Without another word, Aine leans forward and takes your cock into her mouth."
        "Her lips wrap around the head as she sucks lightly, sending shivers down your spine."
        scene ch1ep3p2_563
        with dissolve
        "Aine's tongue darts out to lick the tip before she takes more of you into her mouth." 
        scene ch1ep3p2_564
        with dissolve
        "Her hand wraps around the base of your shaft as she starts to bob her head up and down."
        yt "Fuck! How the hell can I stop her now?!"
        yt "This feels too good to stop!"
        yt "I can't believe this is happening... More surprisingly, I can't believe she's doing this voluntarily."
        yt "She's never dared to step up and take control. But right now, her lust is simply taking over."
        stop music
        play sound doorknock
        show ch1ep3p2_565
        with hpunch
        "Just as Aine prepares to swallow you whole, there's a knock on the door."
        "You both freeze, hearts pounding."
        m "Are you guys okay in there? Our order is ready."
        scene ch1ep3p2_566
        with dissolve
        "You look down at Aine and feel her frustration and anger radiating throughout the entire room."
        yt "Shit..."
        yt "From the alley, to this. Just when I thought we were in for a smoother ride..."
        $ renpy.end_replay()
        scene black
        with dissolve
        play sound2 pubambience loop
        play sound woodhit
        show ch1ep3p2_567
        with hpunch
        a "This is the third time you've messed up our order! Are you intentionally trying to irritate us?!"
        wai "I'm very sorry, ma'am, it's just that-"
        a "Save your apologies! They're worthless at this point!"
        a "How hard is it to get a simple order right? We've been waiting here for an eternity!"
        yt "Her temper's flaring up. She's absolutely furious..."
        a "I want to speak to the owner, now! This is not just incompetence; it's outright disrespect!"
        scene ch1ep3p2_568
        with Dissolve(0.2)
        mc "Aine, maybe we should just let it-"
        a "No, [mc]! This is unacceptable! We're paying customers, not fools to be toyed with!"
        scene ch1ep3p2_569
        with dissolve
        wai "Please, ma'am, if you could just lower your voice and-"
        a "Lower my voice?! After waiting for over an hour for food that's still wrong?! I don't think so!"
        a "I'm done with this! Either bring me the owner, or I'll make sure everyone knows about this pathetic excuse for service!"
        mc "Aine, let's not escalate this further..."
        a "It already escalated, thanks to their incompetence! Owner. Now!"
        stop sound2 fadeout 2

        scene black
        with dissolve
        with fade

        play sound opendoorsilent
        play music 'audio/ThirdPerson.mp3'
        scene ch1ep3p2_570
        with dissolve
        pause
        show ch1ep3p2_571
        a "Mom...?"
        yt "Of course. Why am I not surprised about this...?"
        scene ch1ep3p2_572
        with dissolve
        h "..."
        scene ch1ep3p2_573
        with dissolve
        h "... Mark."
        mar "Yes, Madam?" 
        h "I appreciate you doing your job, but no one's going to hurt me..."
        scene ch1ep3p2_574
        with Dissolve(0.2)
        mar "But-"
        h "In this tiny little pub."
        mar "M-my apologies. I'll wait outside."
        h "Mm."
        play sound closedoor2
        scene ch1ep3p2_575
        with dissolve
        h "And what seems to be the problem here?"
        wai "Madam, I-" 
        scene ch1ep3p2_576
        with Dissolve(0.2)
        h "I don't want to listen to your personal issues: my time is too valuable. Get straight to the point."
        yt "They're cut from the same cloth, no doubt..."
        wai "This customer, she has a complaint."
        scene ch1ep3p2_577
        with dissolve
        h "..."
        scene ch1ep3p2_578
        with dissolve
        a "..."
        scene ch1ep3p2_579
        with dissolve
        h "What's the issue?"
        wai "Well, the thing is-"
        scene ch1ep3p2_580
        with dissolve
        a "We've been waiting an hour, and our orders are still wrong. Not just once, but multiple times."
        scene ch1ep3p2_581
        with dissolve
        h "And where is the manager?"
        wai "He's... um..."
        h "Spit it out."
        wai "He's asleep in the back..."
        scene ch1ep3p2_582
        with dissolve
        h "Incompetence. You, the manager, and anyone else responsible are all fired."
        wai "Madam?"
        h "Did I stutter?"
        scene ch1ep3p2_583
        with Dissolve(0.2)
        wai "B-but it's just one customer! How can you decide just like that based on a simple mistake?!"
        h "A simple mistake..."
        h "How about I pull a gun out and shoot you in the head? That's a simple mistake."
        scene ch1ep3p2_584
        with dissolve
        wai "I'm sorry. I didn't mean to insult you!"
        scene ch1ep3p2_585
        with dissolve
        h "One customer? Do you realize who you're serving?"
        wai "I... a regular customer?"
        h "My daughter."
        scene ch1ep3p2_586
        with dissolve
        wai "Your... daughter?!"
        wai "That ugly piece of shit is your daughter?! Haha, surely you're joking!"
        play sound woosh4
        show keiwaiterpunch
        pause 4.0
        play sound punch2
        show ch1ep3p2_587
        with hpunch
        pause 0.5
        play sound bodyfall2
        show ch1ep3p2_588
        with hpunch
        mc "That's it. How about we let my fist add a few words to this discussion?" #
        mc "Oh, look at that; it has already made its point."
        mc "And to think I almost gave you a chance to explain yourself..."
        scene ch1ep3p2_589
        with dissolve
        pause
        scene ch1ep3p2_590
        with dissolve
        pause
        scene ch1ep3p2_591
        with dissolve
        pause
        scene ch1ep3p2_592
        with Dissolve(0.4)
        a "Wait, mom!"
        h "... After all this time, you still have it in you to call me your mother. I'm flattered."
        a "You're just going to walk away?! Like always?!"
        h "I have other matters to attend to, Aine."
        scene ch1ep3p2_593
        with Dissolve(0.2)
        a "You always prioritize business! Always business, business, business!"
        a "Can't you stop and listen?! Just this once?! I have questions, things I need to understand!"
        play sound closedoor2
        scene ch1ep3p2_594
        with dissolve
        pause
        show ch1ep3p2_595
        a "Tsk!"
        scene ch1ep3p2_596
        with dissolve
        mc "Let's get out of here, Aine. This isn't worth it."
        stop music fadeout 2

        scene black
        with dissolve
        with fade

        play music 'audio/BlackVenom.mp3'
        play sound2 cityalley loop
        scene ch1ep3p2_597
        with dissolve
        mc "I still can't believe how I reacted back there. That's not who I am."
        a "You stood up for me. That's what matters."
        mc "But resorting to violence? That's not the solution. We're supposed to be better than that."
        scene ch1ep3p2_598
        with Dissolve(0.2)
        a "Better? [mc], sometimes you have to fight back!"
        a "It's not just about us, or good morality: it's about not being trampled on!"
        scene ch1ep3p2_599
        with dissolve
        mc "There's a difference between standing our ground and losing control. We should be handling these things maturely."
        scene ch1ep3p2_600
        with Dissolve(0.2)
        a "Maturely? Since when did we become these paragons of virtue? The world isn't always so black and white!"
        a "You think I had the luxury of being \"mature\" growing up?"
        a "The world doesn't always allow you the luxury of being the \"better person\", [mc]! I, myself, have never had that chance!"
        scene ch1ep3p2_599
        with dissolve
        mc "That's not the point, Aine! I'm saying we could've handled the situation without letting our emotions take over!"
        play sound woodhit
        show ch1ep3p2_601
        with hpunch
        a "And that's the problem with you! You're always so calm, so forgiving!"
        a "You never would've suffered if you had it in you to just punch me in the face!"
        mc "Why are you bringing up old wounds? The past is behind us, Aine! We agreed to move forward!"
        a "Because it matters! You are not the only one affected by what happened, [mc]!"
        scene ch1ep3p2_602
        with dissolve
        mc "So what, are you saying you don't want this? Our relationship? That you regret meeting me?"
        a "It's not about regret! It's about what's healthy! And right now, this... this isn't!"
        mc "So, you're giving up on us?"
        scene ch1ep3p2_603
        with dissolve
        a "No, I'm saying we both need to think, to consider if this is what we want." #
        mc "Time apart, then. Is that your solution?"
        a "Maybe. Maybe we both need space to figure ourselves out."
        scene ch1ep3p2_604
        with dissolve
        mc "Fine. But don't lump me in with \"we\". It seems like you're the one who needs to sort things out."
        scene ch1ep3p2_605
        with dissolve
        a "Maybe you're right..."
        scene ch1ep3p2_606
        with dissolve
        m "Are you really okay with this decision?"
        mc "I'm not, but Aine needs the space. I know her well enough to understand."
        mc "When she's not herself, what you say goes in one ear and out the other."
        mc "Usually, I'd just tell her to snap out of it or cut the conversation short. It works most of the time."
        mc "But this... was different. Things went too far."
        scene ch1ep3p2_607
        with dissolve
        m "I'm not one to interject, but you should consider taking time for yourself, too."
        mc "Why do you say that?"
        m "From what I've observed, it seems like you're still unsure about why you let her back into your life."
        scene ch1ep3p2_608
        with dissolve
        mc "..."
        scene ch1ep3p2_609
        with dissolve
        mc "You're pretty observant for someone who claims to have no experience in these matters."
        m "I don't. But I heard everything back on the beach."
        m "I don't need experience to see that your relationship lacks a solid foundation."
        m "Your relationship began almost like some elaborate charade that you had to go along with; not out of choice, but necessity."
        m "It's as if you both have followed a path neither of you chose, but one you felt compelled to follow."
        m "Like you're each other's shield and weapon, but there's no deeper connection."
        m "If you two had a real understanding, this fallout almost certainly would not have happened."
        scene ch1ep3p2_610
        with dissolve
        mc "... You might be right. I've always had the feeling that this was inevitable."
        scene ch1ep3p2_611
        with dissolve
        m "In my experience, respect and admiration among comrades are common, but it's not the same as a true bond."
        m "We rely on each other, but when we lose someone, it's the role we miss, not the person."
        m "It's a harsh reality, and I wish I could go back and change that. But I can't."
        scene ch1ep3p2_612
        with dissolve
        m "So, [mc], you and Aine have a chance to make things right. Don't waste it, or else I'll feel sad."
        scene ch1ep3p2_613
        with dissolve
        m "You two look good together, after all."
        if moonroute:
            yt "She doesn't smile often, but when she does, it's surprisingly captivating."
            yt "Maybe it's the rarity of her smiles that makes each one seem so earnest and heartfelt."
        scene ch1ep3p2_614
        with dissolve
        mc "Yeah, I know..."
        mc "It's just... this will be much more painful than I thought."
        scene ch1ep3p2_615
        with dissolve
        m "No time for regrets, commander. Remember: you're still living under the same roof. What are you going to do now?"
        mc "Damn, that's true..."
        scene ch1ep3p2_616
        with dissolve
        shu "Whoa, did I just walk into a breakup scene? That's rough, man."
        shu "You know you can crash at my place, right?"
        mc "No, thanks."
        scene ch1ep3p2_617
        with dissolve
        shu "Of course not! Right, right!"
        shu "And hey, you could just kick her out, you know?"
        mc "I don't want to escalate things further. It's complicated enough as it is."
        scene ch1ep3p2_618
        with dissolve
        m "If you need it, our couch is always available."
        scene ch1ep3p2_619
        with dissolve
        shu "Don't worry, dude. That's what your best neighbors are here for. We got you."
        mc "*chuckles* Thanks."
        stop sound2 fadeout 1
        scene black
        with dissolve
        play sound closedoor
        scene ch1ep3p2_620
        with dissolve
        g "Hey, you're back."
        scene ch1ep3p2_621
        with dissolve
        a "..."
        g "What's this?"
        scene ch1ep3p2_622
        with dissolve
        g "Hm, let me guess... A fallout?"
        a "..."
        k "Gwen, darling! Double-time, please!"
        scene ch1ep3p2_623
        with dissolve
        g "I don't recall you being this pathetic."
        show ch1ep3p2_624
        with Dissolve(0.1)
        pause
        scene ch1ep3p2_625
        with dissolve
        a "... Is Emma around?"
        s "No, she hasn't come back yet."
        a "I see..."
        play sound stomachrumble
        scene ch1ep3p2_626
        with Dissolve(0.2)
        a "..."
        a "*squeals*"
        scene ch1ep3p2_627
        with dissolve
        s "You haven't had lunch, have you?"
        a "No, not really..."
        s "Come on, let's go to the kitchen. I'll make something for you. What do you feel like eating?"
        scene ch1ep3p2_628
        with dissolve
        a "*hics*"
        s "Are you telling me you're just letting it out now~?!"
        a "Mhm... I was holding back the entire time..."

        scene black
        with dissolve
        with fade

        scene ch1ep3p2_629
        with dissolve
        pause
        scene ch1ep3p2_630
        with dissolve
        a "*sniffs* That's... that's what happened..."
        scene ch1ep3p2_631
        with dissolve
        s "Uhm... That doesn't sound like any date I've heard of."
        a "{cps=20}{size=-10}U{/size}{size=-9}U{/size}{size=-8}U{/size}{size=-7}U{/size}{size=-6}U{/size}{size=-5}U{/size}{size=-4}U{/size}{size=-3}U{/size}{size=-2}U{/size}{size=-1}U{/size}U{size=+1}U{/size}{size=+2}U{/size}{size=+3}U{/size}{size=+4}U{/size}{size=+5}U{/size}~!"
        a "What do I do now, boss~? What do I do~?!"
        s "It's strange for you to call me \"boss\" now of all times..."
        s "What did you do, anyway? Or... what did he do to you?"
        scene ch1ep3p2_632
        with dissolve
        a "It wasn't him, it was meeEEE~! I told him horrible things that I wasn't supposed to saaAAY~!"
        s "And then...?"
        a "And then I suggested we take a break. I can't believe I said that!"
        s "You actually proposed a break?"
        a "{cps=20}{size=-10}U{/size}{size=-9}U{/size}{size=-8}U{/size}{size=-7}U{/size}{size=-6}U{/size}{size=-5}U{/size}{size=-4}U{/size}{size=-3}U{/size}{size=-2}U{/size}{size=-1}U{/size}U{size=+1}U{/size}{size=+2}U{/size}{size=+3}U{/size}{size=+4}U{/size}{size=+5}U{/size}~!"
        a "S-sort of..." #
        a "I mean, I was extremely stressed and pissed, so I just blurted it out~!" 
        a "Sky, what should I do? Should I take my word back?"
        scene ch1ep3p2_633
        with Dissolve(0.2)
        s "No, you shouldn't! At least, not at first."
        s "You guys wouldn't argue without a reason. So, whatever that reason is, you two should sort it out first!"
        s "If you don't, it will become a constant cycle of fights and cool-offs, or worse, a total break-up!"
        s "[mc] will not disappear just because you told him bad things, you know?"
        a "What if he does~?!"
        s "He won't just walk away, Aine. That's not who he is."
        s "Sure, there are issues, but it comes down to how you both work through them."
        scene ch1ep3p2_634
        with dissolve
        a "It's complicated, Sky..."
        a "It's just not that simple to fix everything..."
        s "What's holding you back?"
        a "Earlier today, I opened up to him about the dangers of what I can do with my... capabilities."
        a "I've caused pain to so many, him included. And I'm so scared that I might hurt him again."
        a "And now, it feels like my worst fears just came true."
        s "You're overwhelmed right now, and that's okay. But you can't let that fear paralyze you."
        a "*sighs* Facing him seems impossible at this moment. Not with all this confusion."
        s "Confusion?"
        scene ch1ep3p2_635
        with dissolve
        g "She's struggling with figuring out who she really is. Am I right to assume that, Aine?"
        s "Wait, huh...? What does that mean?"
        g "She's spent so much time under her mom's control, being shaped into who knows what."
        g "The Aine we see every day, the one she's trying to be, and the version her mom created... they're clashing."
        scene ch1ep3p2_636
        with dissolve
        a "..." #
        s "I'm sorry, I can't imagine how tough that is, Aine..."
        scene ch1ep3p2_637
        with dissolve
        k "We couldn't help but overhear your conversation, dear. It's a difficult situation, and only you can navigate through it."
        k "What we can offer is our support, our ears, and our hearts."
        k "Remember, you're not alone, okay?"
        a "Thank you, Klara. It means a lot."
        play sound cloth
        scene ch1ep3p2_638
        with dissolve
        g "Who the hell you ever choose to be? That's up to you. All I care about is that you are my friend."
        g "So whenever I turn my back on you, that doesn't mean I don't care... It's because it pains me to see you hurt."
        a "*hics*"
        g "Be strong..."
        stop music fadeout 2
        
        call hide_days from _call_hide_days_10
        with dissolve
        scene black
        with dissolve
        with fade

        show screen day_sunday with dissolve
        play music 'audio/ComesAndGoes.mp3'
        scene ch1ep3p2_639
        with dissolve
        pause
        scene ch1ep3p2_640
        with dissolve
        pause
        scene ch1ep3p2_641
        with dissolve
        pause
        scene ch1ep3p2_642
        with dissolve
        pause
        call hide_days from _call_hide_days_11
        with dissolve
        scene black
        with Dissolve(1.0)
        show screen day_monday with dissolve
        scene ch1ep3p2_643
        with dissolve
        pause
        scene ch1ep3p2_644
        with dissolve
        pause
        scene ch1ep3p2_645
        with dissolve
        pause
        scene ch1ep3p2_646
        with dissolve
        pause
        scene ch1ep3p2_647
        with dissolve
        pause
        call hide_days from _call_hide_days_12
        with dissolve
        scene black
        with Dissolve(1.0)
        show screen day_tuesday with dissolve
        scene ch1ep3p2_648
        with dissolve
        pause
        scene ch1ep3p2_649
        with dissolve
        pause
        scene ch1ep3p2_650
        with dissolve
        pause
        scene ch1ep3p2_651
        with dissolve
        pause
        scene ch1ep3p2_652
        with dissolve
        pause
        call hide_days from _call_hide_days_13
        with dissolve
        scene black
        with Dissolve(1.0)
        show screen day_wednesday with dissolve
        scene ch1ep3p2_653
        with dissolve
        pause
        scene ch1ep3p2_654
        with dissolve
        pause
        scene ch1ep3p2_655
        with dissolve
        pause
        call hide_days from _call_hide_days_14
        with dissolve
        scene black
        with Dissolve(1.0)
        show screen day_thursday with dissolve
        scene ch1ep3p2_656
        with dissolve
        pause
        scene ch1ep3p2_657
        with dissolve
        pause
        scene ch1ep3p2_658
        with dissolve
        pause
        scene ch1ep3p2_659
        with dissolve
        pause
        scene ch1ep3p2_660
        with dissolve
        pause
        scene ch1ep3p2_661
        with dissolve
        pause
        call hide_days from _call_hide_days_15
        with dissolve
        scene black
        with Dissolve(1.0)
        show screen day_friday with dissolve
        scene ch1ep3p2_662
        with dissolve
        pause
        scene ch1ep3p2_663
        with dissolve
        pause
        call hide_days from _call_hide_days_16
        with dissolve
        scene black
        with Dissolve(1.0)
        show screen day_saturday with dissolve
        scene ch1ep3p2_664
        with dissolve
        pause
        scene ch1ep3p2_665
        with dissolve
        pause
        scene ch1ep3p2_666
        with dissolve
        pause
        scene ch1ep3p2_667
        with dissolve
        a "{i}Ugh, I'm beat..."
        a "{i}Work? Mhh, I'm not feeling it right now..."
        a "{i}Sleep sounds nice..."
        a "{i}Oh, and some good food too..."
        a "{i}Should I wake Sky up? Maybe she'll make me a plate..."
        a "{i}Hm? Fall in love?"
        a "{i}Wait, duh, I'm already smitten..."
        play sound chair2
        scene ch1ep3p2_668
        with dissolve
        a "*sighs* I'm so cold... I miss those cozy cuddle sessions right now..."
        a "I just want to fall asleep... in his arms..."
        scene ch1ep3p2_669
        with dissolve
        a "Uhh, [mc]...?"
        scene ch1ep3p2_670
        with dissolve
        a "..."
        scene ch1ep3p2_671
        with dissolve
        a "*whimpers*"
        scene ch1ep3p2_672
        with dissolve
        a "*sniffs*"
        scene ch1ep3p2_673
        with dissolve
        pause
        scene ch1ep3p2_674
        with dissolve
        pause
        play sound chair4
        scene ch1ep3p2_675
        with dissolve
        pause
        play sound chair
        scene ch1ep3p2_676
        with dissolve
        pause
        scene ch1ep3p2_677
        with dissolve
        a "Right... I can't reach her directly anymore."
        stop music fadeout 2
        scene black
        with dissolve
        pause 1.0
        play music 'audio/BackOnRoad.mp3' fadein 2
        play sound closedoor2
        scene ch1ep3p2_678
        with dissolve
        pause
        scene ch1ep3p2_679
        with dissolve
        k "What brings you here so late, dear?"
        play sound woodhit
        show ch1ep3p2_680
        with hpunch
        a "Ah~!"
        scene ch1ep3p2_681
        with dissolve
        k "You shouldn't be wandering around at this hour. What do you need?"
        a "No, the real question is: why are you up caressing... what even is that?!"
        k "Just an old collector's habit of mine. I haven't killed anyone, don't worry. Or at least, not yet."
        a "Not yet~?!"
        k "Ignore that."
        a "Jeez... I almost had a heart attack!"
        k "Well, I'm off to bed shortly. But tell me, what's on your mind?"
        scene ch1ep3p2_682
        with dissolve
        a "I need to speak to Jess. Could you call her for me?"
        k "Jess? Of course, but it's quite late, dear. We shouldn't disturb people when they're resting."
        play sound woosh2
        show ch1ep3p2_683
        a "It's really important! Please, I need your help!"
        k "A-alright, I'll see what I can do."
        stop music fadeout 2

        scene black
        with dissolve
        with fade

        play music 'audio/MorningLightSerenade.mp3'
        scene ch1ep3p2_684
        with dissolve
        j "Yes, I can arrange a meeting."
        j "But why now, after all your efforts to free yourself from her influence?"
        scene ch1ep3p2_685
        with dissolve
        a "I've always told myself... \"Be a good person\"."
        a "But being a good person shouldn't make me miserable, right?"
        a "I know, and I've seen more than enough... The world is a cruel place."
        a "Even if you sacrifice everything for the greater good, others may not notice your efforts at all."
        a "More than being a \"good person\"..."
        a "No, I just want to become someone who can love myself..."
        j "You sound quite distressed."
        scene ch1ep3p2_686
        with dissolve
        a "I am..."
        a "Right now, without [mc], I'm a lost cause. So... I'm prepared for whatever she'll do to me."
        a "It's just that... There are questions only she can answer. That's what I'm after."
        j "Understood. Do you have a meeting place in mind?"
        a "Yes, I know a place. I'll send you the details."

        scene black
        with dissolve
        with fade

        $ renpy.music.set_volume(0.4, 1.0)
        $ renpy.sound.set_volume(0.2, 1.0)
        play sound2 dawnambient loop
        play sound waterfountain loop fadein 2
        play sound3 riverwater loop fadein 2
        scene ch1ep3p2_687
        with dissolve
        pause
        $ renpy.sound.set_volume(1.0, 1.0)
        $ renpy.music.set_volume(0.5, 1.0)
        stop sound3 fadeout 2
        scene ch1ep3p2_688
        with dissolve
        pause
        scene ch1ep3p2_689
        with dissolve
        a "*sighs* After all that bravado, I'm still shaking. Perhaps I shouldn't have done this..."
        play sound3 cat_meow
        scene ch1ep3p2_690
        with dissolve
        a "Oh, hello there. You're still around, huh?"
        scene ch1ep3p2_691
        with dissolve
        a "Come here, little one."
        scene ch1ep3p2_692
        with dissolve
        a "Aww, look at you. You haven't changed a bit over the years. Still as spry as ever."
        play sound3 cat_meow
        pause
        a "*giggles* What's your secret to eternal youth, huh?"
        play sound3 cat_purr
        pause
        a "*chuckles* Alright, then. Keep your secrets."
        play sound3 cat_meow
        scene ch1ep3p2_693
        with dissolve
        a "Yeah, it's just me today. I had a falling out with someone very dear, and... well, it's complicated."
        a "But I'm planning to make things right. I'll bring him here next time, promise."
        play sound3 cat_meow
        scene ch1ep3p2_694
        with dissolve
        a "Look, I'd love your company, but someone who might not be so fond of you is coming. Best you stay safe."
        scene ch1ep3p2_695
        with dissolve
        pause
        scene ch1ep3p2_696
        with dissolve
        h "Ah, chasing after shadows and dreams, and where did it lead you? Right back to me."
        a "Speak of the devil..."
        play sound3 cat_meow
        scene ch1ep3p2_697
        with Dissolve(0.2)
        h "Oh, there you are!"
        h "Here, kitty, kitty!"
        play sound3 cat_purr
        scene ch1ep3p2_698
        with dissolve
        pause
        scene ch1ep3p2_699
        with dissolve
        a "..."
        scene ch1ep3p2_701
        with dissolve
        h "What's with that look?"
        scene ch1ep3p2_700
        with dissolve
        a "I thought you disliked cats."
        scene ch1ep3p2_701
        with dissolve
        h "Because I never let you have pets?"
        a "That's part of it, yes."
        scene ch1ep3p2_702
        with dissolve
        h "Mm, you thought this, you thought that. You always were narrow-minded, Aine. You see one thing and think it's the whole picture."
        a "..."
        h "You see, cats, though fragile, have their charm. They can make you soft, showing your weakness."
        h "They weren't what you needed for your development."
        scene ch1ep3p2_703
        with dissolve
        a "\"Development\". Oh, really?"
        a "Witnessing the horrors of torture, being forced into actions against my will, brainwashing, even physical harm."
        a "That's what you call \"development\"?"
        h "Mm."
        scene ch1ep3p2_704
        with dissolve
        h "Off you go now."
        scene ch1ep3p2_705
        with dissolve
        pause
        play sound3 cointoss
        scene ch1ep3p2_706
        with Dissolve(0.2)
        pause
        play sound3 watersplash_small
        scene ch1ep3p2_707
        with dissolve
        pause
        scene ch1ep3p2_708
        with dissolve
        a "... How did you know about that?"
        h "Who taught you in the first place?"
        a "Dad."
        h "And I taught it to your father. Back when we were still dreaming of matters we'll never achieve now."
        h "Although this land's beauty was his dream, not mine."
        h "I sold it. But he saw its value, so he repurchased it and then brought it back to life."
        h "How else would I have known where you and your young man were headed those days, hm?"
        scene ch1ep3p2_709
        with dissolve
        a "Ugh, I was so naive..."
        h "It seems you still are."
        scene ch1ep3p2_710
        with dissolve
        a "So you're the one maintaining this place?"
        h "Yes. I can't just abandon one of the precious things he's left behind." 
        scene ch1ep3p2_711
        with dissolve
        a "..."
        scene ch1ep3p2_712
        with dissolve
        pause
        stop music fadeout 4
        play sound3 chair3
        scene ch1ep3p2_713
        with dissolve
        h "So, what brings you to me?"
        a "Are you... not going to do anything to me?"
        h "I'd prefer you not waste my time; I haven't slept in ages."
        scene ch1ep3p2_714
        with dissolve
        a "Uhm..."
        h "Don't give me the \"uhm\". It's not a word to start a conversation."
        a "I just... want to know myself better."
        $ renpy.music.set_volume(1.0, 1.0)
        play music 'audio/ComesAndGoes.mp3'
        scene ch1ep3p2_715
        with Dissolve(0.2)
        h "*chuckles* That's what you called me here for? To find yourself? That's stupid."
        play sound3 woodhit
        show ch1ep3p2_716
        with hpunch
        a "Stupid?! This goddamn \"growth\" you imposed on me is tearing my life apart!"
        a "Your \"lessons\" turned me into someone I don't even recognize!"
        a "Do you even realize the damage you've caused, the pain you've inflicted?"
        a "You've shaped me into a person I never wanted to be!"
        a "Because of you, I've pushed away the person I care about most!"
        a "And now, I'm left picking up the pieces of the life you've shattered!"
        scene ch1ep3p2_717
        with dissolve
        h "..."
        scene ch1ep3p2_718
        with dissolve
        pause
        scene ch1ep3p2_719
        with dissolve
        h "Your fiancé?"
        a "How did you..."
        h "If that ring on your finger is not obvious enough, then I don't know what is."
        a "W-well..."
        h "Did you push him away?"
        scene ch1ep3p2_720
        with dissolve
        a "Yes..."
        h "The worst thing I expected was to be giving romantic advice..."
        scene ch1ep3p2_721
        with Dissolve(0.2)
        a "I don't need love advice! I need-"
        h "Let me guess. You're lost. Unsure which part of you is truly \"you\"."
        scene ch1ep3p2_722
        with dissolve
        a "Exactly... How do you know things before I even say them?"
        h "Because you are my daughter."
        h "... Sit down."
        play sound3 chair3
        scene ch1ep3p2_723
        with dissolve
        h "*sighs* God, I can't believe I'm about to say this. It's not usually in my nature to be so... forthcoming."
        a "Yeah, whatever."
        scene ch1ep3p2_724
        with dissolve
        h "Listen, child. You're not lost. The person you are now: that's the real you. It's as simple as that."
        a "But all those things you made me do, they changed me!"
        h "Changed? No. I merely brought out what was already there. Since your birth, I saw signs."
        a "Signs? What signs?"
        h "Your determination, even as a child. The way you never backed down, even when you were overpowered."
        a "That was just me being stubborn."
        h "It was more than that. It was the amber of a strong will, a trait I knew could be honed."
        h "You see it as oppression, but I was drawing out your inherent strength."
        a "Strength? You call that strength?"
        h "Absolutely. That \"oppressive\" personality of yours? It's a sign of resilience, a will to survive and thrive."
        h "I saw that early on - your refusal to yield, your fierce independence, even when you could barely walk."
        play sound3 chair4
        scene ch1ep3p2_725
        with dissolve
        a "But at what cost? It made me push away the people I care about."
        h "Having layers, Aine, is not a weakness. It makes you complex, interesting."
        h "People without layers are dull, predictable, like robots."
        a "But these goddamn layers are now tearing me apart!"
        h "No, they're making you who you are. Strong, capable..."
        h "... And yes, complicated."
        scene ch1ep3p2_726
        with dissolve
        a "So you're saying all this... turmoil inside me is a good thing?"
        h "It's a part of life. It means you're alive, not just existing."
        a "Alive, but at the cost of my happiness."
        h "Happiness is fleeting, Aine. Strength, resilience - these are lasting."
        a "But I don't want to be just strong. I want to be happy, too!"
        h "Strength can lead to happiness. You need to control it, not the other way around."
        a "And if I can't?"
        h "You can. You're my daughter, after all. You have more power than you realize."
        scene ch1ep3p2_727
        with dissolve
        a "Power... is that all you see in me?"
        h "Power, potential, depth. You're not just one thing, Aine. You're a myriad of things."
        a "And if I want to change? To be different?"
        h "Change if you must, I do not care. But remember: the core of who you are, that strength, it's a gift."
        scene ch1ep3p2_728
        with dissolve
        a "A gift that feels like a curse..."
        h "Only if you let it be."
        h "Try embracing it, and maybe... just maybe... you'll see its true value."
        a "It's not that simple after pushing away the most important person in my life..."
        h "Well, nothing worth having ever is. But you're capable of more than you give yourself credit for."
        a "I'm not sure if I can see it your way."
        a "No, I'm sure I never will. I still refuse to abide by your laws."
        h "Who knows? In time, you might."
        h "For now, just remember that you're not solely what you feel or have been through."
        h "You're a culmination of all your experiences, the good and the bad."
        scene ch1ep3p2_727
        with dissolve
        a "... So you admit that the things you did to me were {i}bad{/i}, then?"
        h "*chuckles* Good or bad, it was necessary parenting. I couldn't care less whether you accept that or not."
        a "How can you dismiss the pain you caused as simply \"parenting\"?"
        h "Again, you're looking at it too narrowly, Aine. Life isn't just about what hurts us."
        scene ch1ep3p2_726
        with dissolve
        a "But the pain you caused was real. How can you overlook that?"
        h "It's not overlooking. It's seeing beyond the immediate. I was preparing you for an unkind world."
        a "Preparation? There are gentler ways to teach someone about this world!"
        h "Perhaps, but would gentler ways have made you as strong as you are now?"
        scene ch1ep3p2_728
        with dissolve
        a "I didn't need to be this \"strong\" at the cost of my happiness."
        h "Like I said, happiness can be temporary. The strength I shaped in you is enduring."
        a "Is enduring strength worth the cost of constant suffering?"
        h "Suffering is a part of life. It shapes us, challenges us."
        a "But it shouldn't define us. I don't want my life defined by suffering."
        h "Then let it define your resilience. You've survived, haven't you?"
        a "..."
        play sound3 chair4
        scene ch1ep3p2_729
        with dissolve
        h "I was informed you did something a week ago. Did that really happen?"
        a "Wait, who told you?"
        h "Your man informed Jess, and the news came to me."
        play sound3 chair4
        scene ch1ep3p2_731
        with dissolve
        a "Oh my god..."
        h "Bold move, but it worked, nonetheless."
        scene ch1ep3p2_732
        with dissolve
        h "Without that strength I gave you, would you have been able to save that person's life?"
        a "..."
        scene ch1ep3p2_510
        with flash
        m "You're the one who took charge. We were just your support."
        scene ch1ep3p2_732
        with flash
        pause
        scene ch1ep3p2_733
        with dissolve
        a "No..."
        scene ch1ep3p2_734
        with dissolve
        h "You've always seen the world through a narrow lens, influenced by our family."
        h "I tried to broaden your perspective, yet you resist the possibilities."
        h "Open your eyes, Aine. There's no need to choose one identity. Embrace all facets of yourself."
        h "You've always despised the lamest things. So, what's with the tears now? I can't quite grasp what you're getting so emotional about."
        play sound3 phonevibrate loop
        scene ch1ep3p2_735
        with Dissolve(0.2)
        pause
        stop sound3
        scene ch1ep3p2_736
        with dissolve
        h "Ah, it seems your escort is here. Our time is up."
        a "Escort?"
        h "I can't let you wander alone at this hour, can I?"
        play sound3 chair4
        scene ch1ep3p2_737
        with dissolve
        a "Mom, wait!"
        h "Yes?"
        scene ch1ep3p2_738
        with dissolve
        a "After everything I've done for you..."
        a "Were you... ever proud of me?"
        scene ch1ep3p2_739
        with dissolve
        h "..."
        scene ch1ep3p2_740
        with dissolve
        a "Mnh..."
        h "You still love that, I see... I'm glad."
        scene ch1ep3p2_741
        with dissolve
        h "Farewell, Aine..."

        $ renpy.sound.set_volume(0.5, 1.0)
        scene ch1ep3p2_742
        with dissolve
        pause
        if heraslap:
            scene ch1ep3p2_743
            with dissolve
            mc "..."
            scene ch1ep3p2_744
            with dissolve
            h "Hold on."
            scene ch1ep3p2_745
            with dissolve
            $ renpy.sound.set_volume(1.0, 1.0)
            h "Oh, one more thing."
            a "Yes...?"
            $ renpy.sound.set_volume(0.5, 0.2)
            play sound3 cloth2
            show ch1ep3p2_746
            with hpunch
            mc "Mmp!"
            $ renpy.sound.set_volume(1.0, 0.2)
            scene ch1ep3p2_747
            with Dissolve(0.2)
            pause
            scene ch1ep3p2_748
            with dissolve
            a "You..."
            $ renpy.sound.set_volume(0.5, 0.2)
            scene ch1ep3p2_749
            with dissolve
            h "Be fucking decisive."
            $ renpy.sound.set_volume(1.0, 0.2)
            play sound3 woodhit
            show ch1ep3p2_750
            with hpunch
            a "You... BITCH!" #
            h "See? That's more like it."
            a "I will never become like you! Remember that!"
            h "Mm, at this point, you're already a cheap imitation of me!"
            a "I may have the same personality as you, but I swear, I will never become a monster!"
            $ renpy.sound.set_volume(0.5, 0.2)
            scene ch1ep3p2_751
            with dissolve
            h "A fine kisser. Tell Klara I said \"Hi\"."
            mc "Can you stop putting on a brave face and talk to your daughter like a real mother?"
            h "What do you think I just did? That was more than enough..."
            mc "*chuckles* More than enough..."
            $ renpy.sound.set_volume(1.0, 0.2)
            scene ch1ep3p2_752
            with dissolve
            h "Embrace it, Aine!"
        else:
            $ renpy.sound.set_volume(0.5, 0.2)
            scene ch1ep3p2_744
            with dissolve
            h "Tell Klara I said \"Hi\"."
            mc "..."
            $ renpy.sound.set_volume(1.0, 0.2)
            scene ch1ep3p2_750
            with dissolve
            a "I will never become like you! Remember that!"
            h "Mm, at this point, you're already a cheap imitation of me!"
            a "I may have the same personality as you, but I swear, I will never become a monster!"
            $ renpy.sound.set_volume(0.5, 0.2)
            scene ch1ep3p2_751
            with dissolve
            mc "Can you stop putting on a brave face and talk to your daughter like a real mother?"
            h "What do you think I just did? That was more than enough..."
            mc "*chuckles* More than enough..."
            $ renpy.sound.set_volume(1.0, 0.2)
            scene ch1ep3p2_752
            with dissolve
            h "Embrace it, Aine!"
        
        $ renpy.sound.set_volume(0.3, 0.2)
        scene ch1ep3p2_753
        with dissolve
        j "Shall we?"
        h "Mm."
        stop music fadeout 2
        stop sound fadeout 2
        stop sound2 fadeout 2
        scene ch1ep3p2_754
        with dissolve
        pause
        play sound3 parkwind loop
        play music2 'audio/FragileMoments.mp3' loop
        scene ch1ep3p2_755
        with flash
        h "Ow, ow, ow!"
        scene ch1ep3p2_756
        with dissolve
        ri "Hey, are you alright?"
        h "Yes, it's just... she's quite active in there..."
        scene ch1ep3p2_757
        with dissolve
        ri "Eager to see the world, aren't you, my dearest?"
        ri "But let's not be too hasty. We want you just perfect, not premature like someone we know."
        scene ch1ep3p2_758
        with dissolve
        h "..."
        ri "I'm just joking..."
        scene ch1ep3p2_759
        with dissolve
        h "*chuckles* She's going to be the best."
        scene ch1ep3p2_760
        with dissolve
        ri "You know, I've been giving it much thought... What about the name Aine?"
        h "Aine?"
        ri "Yeah, Aine. Like the goddess - strong, radiant, a reflection of her mother's beauty and strength."
        h "Aine... I love it, Richard. It's just right."
        scene ch1ep3p2_761
        with dissolve
        ri "I dream of her being as formidable as you, Hera. Able to stand tall against all odds."
        h "And she will. We'll guide her together."
        ri "She'll inherit the best from us. Your indomitable spirit and, hopefully, some of my charm and wit."
        h "Oh, she definitely will, with you as her father."
        ri "It's a team effort, after all. We're in this together, every step of the way."
        scene ch1ep3p2_762
        with dissolve
        pause
        scene ch1ep3p2_763
        with dissolve
        h "Always together."
        $ renpy.sound.set_volume(1.0, 0.2)
        stop sound3 fadeout 2
        scene ch1ep3p2_764
        with flash
        pause
        h "{i}And now, Richard, I've finally let our daughter go..."
        h "{i}On those lonely nights, those difficult days of conflict, you were always there with me."
        h "{i}Your presence gave me the strength to keep going."
        h "{i}But now that you're gone, I wonder... are you happy where you are?"
        h "{i}Memories of you often come back and always bring tears."
        h "{i}Without you and our daughters..."
        h "{i}... I feel so alone."
        play sound slap
        show ch1ep3p2_765
        with hpunch
        h "Ow!"
        scene ch1ep3p2_766
        with Dissolve(0.2)
        h "Shit! SHIT!"
        h "Goddamn it, Jess! What was that for?!"
        scene ch1ep3p2_767
        with dissolve
        j "I'm still here."
        scene ch1ep3p2_768
        with dissolve
        h "..."
        play sound cloth
        scene ch1ep3p2_769
        with dissolve
        j "Don't worry, you can cry now..."
        scene ch1ep3p2_770
        with dissolve
        h "{i}Richard, I've given everything I had for our daughter."
        h "{i}I can only hope... I've lived up to your dream and nurtured Aine into the strong woman you envisioned."
        h "{i}Tell me, have I done enough? Have I been the mother you always believed I could be...?"
        h "{i}If not, then please forgive me. I'll make it up to you when we see each other again."
        scene ch1ep3p2_771
        with dissolve
        j "I'm proud of you, sis."
        h "Stop it."
        j "Hey, thanks for the vote of confidence."
        h "Can it, Jess."
        j "Alright, alright."
        h "Where's your necklace? Did you lose it? I can buy you a different one."
        j "Nah, it just didn't match today's look."
        h "How about giving the hair dye a rest? You're still rebelling against a dead person."
        j "I'm used to it by now. This color's become part of my signature."
        h "Then at least try to act your age around me. Your childish antics make me sick."
        j "Love ya, sis."
        h "Urrgghh...!"
        stop music2 fadeout 5
        label aineonsteroids:
        if _in_replay:
            $ name = persistent.gallery_name
        play sound waterfountain loop
        scene ch1ep3p2_872
        with dissolve
        mc "Hey..."
        "You speak softly, stepping closer to her."
        scene ch1ep3p2_873
        with dissolve
        a "[mc]... why did you come for me?"
        mc "To take you home."
        scene ch1ep3p2_874
        with Dissolve(0.2)
        a "You don't have to obey her, especially not for my sake!"
        mc "It's not about her, Aine! I'm here because I care about you!"
        a "I don't need you to look after me!"
        scene ch1ep3p2_875
        with dissolve
        mc "Then why do you look so lost? I'm just trying to be here for you, Aine!"
        a "I never asked for you to be here!"
        scene ch1ep3p2_876
        with dissolve
        "You take another step forward, further closing the distance."
        mc "Do you know what your problem is? You push people away when you're scared!" 
        scene ch1ep3p2_877
        with Dissolve(0.2)
        "Aine's jaw tightens at your words as a surge of anger courses through her veins."
        play sound2 woosh2
        show ch1ep3p2_878
        with hpunch
        a "I'm not scared!" #
        mc "Then why did you run away? Why did you push me away?"
        a "I-I don't know, okay?! I just..."
        play sound2 cloth2
        show ch1ep3p2_879
        with hpunch
        "Before Aine can finish her words, your hand shoots out and grabs her waist, pulling her roughly towards you."
        "Your bodies collide as Aine lets out a small gasp."
        "You whisper, your breath hot against her ear."
        scene ch1ep3p2_880
        with dissolve
        mc "Maybe you were scared of admitting just how much you need me..."
        "Aine's heart pounds in her chest as she stares up at you, her anger slowly giving way to desire."
        "Both of you are acutely aware that the heat, the tension that had been building, is now threatening to consume you both."
        scene black
        with dissolve
        pause 1.5
        play music 'audio/DejaVu.mp3'
        play sound doorslam
        show ch1ep3p2_881
        with hpunch
        "Your lips crash against hers in a desperate kiss as you stumble into the room, slamming the door shut behind you."
        "With a grunt of determination, you sweep Aine off her feet and carry her towards the wall."
        "She clings to you instinctively as the world spins around her - one hand gripping at your shirt while the other entwines itself in your hair."
        play sound thud2
        show ch1ep3p2_882
        with hpunch
        a "Aahh~!" #
        "Aine's back hits the wall with a thud, causing her to let out a small yelp."
        "You press yourself against her, pinning her in place."
        scene ch1ep3p2_883
        with dissolve
        "You can feel the heat radiating off each other's bodies as you breathe hot air into each other's mouths."
        "Every touch - from your rough hands on her skin to how your lips move ravenously against hers - sends electricity up both your spines."
        "You grind your hips, your fully erect length pressing against her."
        "Even through the layers of fabric, Aine feels your pulsating rod."
        a "Mmh..."
        "She utters a subdued moan in response."
        "Aine becomes further lost in the sensation, overwhelmed by how you feel pressed on her torso."
        "You can feel the hunger growing in your soul as well - a hunger that will only be satisfied by finally claiming Aine completely as yours."
        "However..."
        scene ch1ep3p2_884
        with Dissolve(0.2)
        a "Mmp!"
        play sound chair
        show ch1ep3p2_885
        with hpunch
        "Aine pushes you back with all her might." #
        "As you fall back, you see her eyes reflecting a brewing storm of feelings."
        "You find yourself sitting on the edge of the bed once you reorient yourself."
        scene ch1ep3p2_886
        with dissolve
        mc "Tsk! Why can't you just...!" #
        play sound bodyhit
        show ch1ep3p2_887
        with hpunch
        "Regaining your composure, you purposefully grab her hand." #
        play sound chair
        show ch1ep3p2_888
        with hpunch
        "With a newfound resolve, you pin her down." #
        mc "Why can't you just get your head right and talk to me properly!"
        scene ch1ep3p2_889
        with dissolve
        a "... *hics*" #
        scene ch1ep3p2_890
        with dissolve
        a "I...I'm sorry~!" #
        mc "You don't need to apologize! All I wanted was for you to face me; I've been waiting!"
        scene ch1ep3p2_891
        with Dissolve(0.2)
        a "What do you think I just did~?!" #
        a "I love you, [mc]! I never wanted to hurt you! I didn't want you to go away!"
        a "So I thought I'd risk it and talk to my mother to find out who I really was! So I could face you as a better version of myself!"
        a "Yet the only thing she told me was to accept it?! How is that supposed to make me better?!"
        scene ch1ep3p2_892
        with dissolve
        a "*crying* I'm scared of myself, [mc]! I don't want any of this~! I don't want to lose you~!" #
        yt "She's shaking... Even worse than last time."
        yt "Her fear is there. It's real..."
        scene ch1ep3p2_893
        with dissolve
        mc "You won't lose me, Aine. But we can't let fear dictate our actions. My fear turned into anger that day, and I regret that." #
        a "But my fear turns into this urge to control, to push others away for protection."
        mc "Who are you trying to protect? Me, or yourself?"
        a "I don't know, [mc]. After speaking with Mom, everything's... more complicated."
        mc "Look, I get it, okay? But shutting me out wasn't the solution."
        mc "I just don't want us to become people we're not, Aine. That's all."
        a "But what if that's part of who I am, [mc]?"
        a "What if she's right, and I've just been fighting it?"
        scene ch1ep3p2_894
        with dissolve
        mc "Your other side never was a secret, especially to me. I experienced it firsthand." #wipes away her tears #####
        mc "Still, there's this question in my head that I've never really pondered until now: Why did I ever accept you back into my life?"
        mc "And do you know why? Because I saw more in you than just that side."
        mc "I saw someone brave, someone trying to overcome her shadows."
        mc "I saw a girl who cares deeply about the people in her life, who will do anything to lead them towards happiness."
        mc "I saw a girl who would move heaven and hell if it meant that she would make life easier for the people she loves."
        scene ch1ep3p2_895
        with dissolve
        mc "And most importantly, I saw a young woman who, despite her shortcomings, has a heart of gold that will unhesitatingly sacrifice her well-being for that of her beloved." #
        mc "I accepted you back because I believe in the person you are at your core."
        mc "Regardless of your battles, you have unique strengths and a kindness that outshines the darkness."
        mc "We all have our struggles, Aine. But it's how we face them and grow from them that defines us."
        mc "And every time I see you fight against what you fear you might become, I see the real you - the Aine who's much more than just Hera's daughter."
        mc "I liked you for who you were back then, and I love you just the way you are now."
        "You pause, chest heaving from the intensity of your heartfelt confession."
        a "..."
        scene ch1ep3p2_896
        with dissolve
        a "*hics*" #
        a "[mc], I... I don't know how to handle all of this. It feels like I'm walking on a tightrope."
        a "Hearing you say that you still believe in me - that you still love me - even after everything... it means more than you can imagine."
        a "I've been so afraid of letting my mother's shadow overtake me that I didn't realize I was pushing away the one person who truly cares."
        scene ch1ep3p2_897
        with dissolve
        a "I need you, [mc]. More than I've allowed myself to admit. Even more than I need the air I breathe." #
        a "You see something in me that I've been afraid to see in myself."
        a "Since you believe in me so much, maybe... it's time I start believing in that part of me, too."
        a "It's just... hard to let go of that fear. It's been a part of me for so long, and I'm sorry for letting it affect our relationship."
        a "I love you, [mc], and the last thing I want is for my cowardice to hurt us. I want to face them - with you by my side."
        a "Can we... can we start over? Can we still rebuild this? Together?"
        a "I want to be the person you see in me, the person I know I can be."
        scene ch1ep3p2_898
        with dissolve
        mc "Aine... there's nothing to rebuild because we never lost anything. We've just grown stronger together." #
        mc "Do you remember the day I let you into my house, even though I knew who you were?"
        a "Yes: why did you do that?"
        mc "I saw something in your eyes."
        mc "It was a glimpse of the real you, not the person others made you out to be."
        mc "You can be tough, sure. Stubborn, sometimes cold, ruthless even. But behind all that, there's a reason - a good one."
        mc "You do these things not out of malice, but out of love. To protect those you care about, to shield those who hold you dear."
        mc "That's the Aine I saw then and the Aine I see now. And it's her that I love."
        mc "It's {i}you{/i} that I love."
        scene ch1ep3p2_899
        with dissolve
        a "*hics*... *sniffs*... [mc]... *sobs*... I... *hics*..." #
        "After hearing your sincere words, a wave of emotion washes over Aine."
        "Tears flow freely from her eyes: not out of sadness, but from a profound sense of relief and being understood."
        "The drops spill over, cascading down her cheeks as she realizes the depth of your acceptance and love."
        "At this moment, the walls she built around her heart crumble to ash, replaced by the warmth of genuine connection and realization that she is cherished beyond any doubt."
        mc "Hey, hey, Aine... look at me."
        scene ch1ep3p2_900
        with dissolve
        "You gently lift her chin, encouraging her to meet your eyes."
        a "*hics*... [mc], I... *sniffs*"
        mc "Haven't we both shed enough tears this week?"
        "Aine looks up at you, her eyes glistening with mixed emotions."
        a "I just... *sniffs*... I didn't expect... *hics*"
        scene ch1ep3p2_901
        with dissolve
        mc "Shh, it's okay. No more tears now, alright?"
        "Once again, you wipe away her tears with a soft, affectionate touch."
        a "*sniffs*... How can you be so..."
        mc "Cute? Isn't that one of the reasons you fell in love with me in the first place?"
        play sound chair
        show ch1ep3p2_902
        with hpunch
        a "Do you really have to make a joke right now~?!" #
        mc "Of course. But you always know how to take them in stride..."
        play sound cloth
        scene ch1ep3p2_903
        with dissolve
        "With a tender smile, you lean in closer." #
        "You kiss her gently, a sweet gesture that promises love and understanding."
        "Aine melts into the kiss with a sense of peace and connection, as if all the pieces of her life puzzle are falling into place."
        scene ch1ep3p2_904
        with dissolve
        "Finally, you pull away." #
        "Aine smiles as her tears begin to dry, replaced only by the feeling of love - all meanings of the word."
        a "Nothing to hide from each other, right?"
        "Gently, Aine places her hands on your chest, nudging you just enough to give herself space."
        play sound cloth
        stop music fadeout 3
        $ renpy.music.set_volume(1.0, 1.0)
        play music2 'audio/LanternRoom.mp3' fadein 3 loop
        scene ch1ep3p2_905
        with dissolve
        "With a fluid motion, she sits up, her movements carrying a sense of purpose." #
        "There's a brief pause as she catches her breath; then, she begins to undress with a determined gaze that never breaks from yours."
        play sound cloth
        scene ch1ep3p2_906
        with dissolve
        "First, she glides her shirt over her head."
        play sound cloth
        scene ch1ep3p2_907
        with dissolve
        "Next, she peels off her pants, each movement imbued with her growing confidence."
        "Her underwear follows, discarded with the same decisive intent."
        "Now, completely bare in front of you, her transformation is complete. Gone is the vulnerability of the past: in their place lies the confident, assertive Aine." #
        "This is her - unguarded and driven, ready to take what she wants. The air around her seems to shift, charged with her newfound resolve."
        play sound chair
        scene ch1ep3p2_908
        with dissolve
        a "Now hold up your end of the promise, [mc]."
        scene ch1ep3p2_909
        with dissolve
        "Though she says \"promise\", this moment feels more like destiny." #
        yt "Promise? Oh yeah... I did..."
        "This has nothing to do with promises or obligations."
        "All you feel is a near-uncontrollable desire welling up inside you to ravish this girl..."
        "... To claim her, to protect her..."
        "... And to show her how you feel about her after all this time, despite all the setbacks and obstacles."
        "But now...?"
        "Even Hera herself wouldn't dare come between you and Aine."
        "Aine will become yours, and you hers." 
        "You can barely contain the anticipation and lust from bursting out of every limb."
        "However, you have to let her have her moment. You must be patient."
        scene ch1ep3p2_910
        with dissolve
        mc "Alright, Aine. Don't be too hasty. I'm not going anywhere." #
        "Those words were probably meant for both of you."
        "This girl has suffered so much, putting herself through hell and even sacrificing her greatest desire: to be with you."
        "To what end?"
        "Just to atone for her sins."
        "Even though you told Aine to be patient, only a heartless fool would keep this girl waiting."
        play sound cloth
        "You strip off your clothes as fast as you can, your eyes never ceasing to admire her for a single moment."
        "Once you pull your shirt up to your head, you hear Aine take a deep, excited breath from seeing your fully naked form."
        play sound chair
        show ch1ep3p2_911
        with hpunch
        "Just as you get your top off, she lunges at you like a possessed tigress, catching you totally off guard." #
        "Aine's fingers dig into your shoulder as she drives you back, causing you to lose balance."
        "Thankfully, a soft bed behind you cushions your fall."
        "Your extremely aroused lover uses the opportunity to climb onto your lap and claim her prey."
        mc "Whoa! Easy there, Miss! Like I said, I'm not going anywhere."
        scene ch1ep3p2_912
        with dissolve
        a "And I'll make sure of that, [mc]." #
        "You begin to feel something dripping onto your shaft." 
        scene ch1ep3p2_913
        with dissolve
        "Though you already have a good idea what it is, you still look down to see that Aine's cunt is drenched." #
        "In this condition, there's only one thing that she will let you do. And clearly, she wants you to do it now."
        scene ch1ep3p2_914
        with dissolve
        a "Look what you've done to me..." #
        "Aine's face is beet red, her body emanating enough heat to set the sun ablaze."
        scene ch1ep3p2_915
        with dissolve
        "She wraps her arms around your neck and back, desperately clinging onto you." #
        "Her soft skin conforms to your body, interrupted only by her hardening nipples imprinting themselves into your chest."
        a "[mc]... haa... I can't take it anymore."
        "Even considering what happened during the blackout and in the restaurant, you've never seen this level of raw desperation from Aine before."
        "Now that the shackles holding back her true feelings are shattered, Aine's unfiltered lust crashes onto her like a tidal wave, threatening to drag you both into its depths."
        scene ch1ep3p2_916
        with dissolve
        "Suddenly, you feel Aine gyrating her hips on top of you." #
        "Her moist slit begins to grind your ever-hardening shaft."
        "Back and forth she moves, leaving a fluid trail marking her travels."
        scene ch1ep3p2_917
        with dissolve
        a "Ngh... it feels so warm down there... and everywhere..." #
        a "I... feel like I'm burning up!"
        a "[mc]...! [mc]~!"
        "Aine's sweet moans ring into your ear, triggering something deep within your primal brain."
        "The way she says your name - such pure, unadulterated desire. Such deliciously carnal need."
        "Her breaths puff hot against your skin as her supple breasts drag along your chest, mimicking the movements of her hips."
        mc "Aine, I said slow down! You're be-"
        play sound cloth2
        scene ch1ep3p2_918
        with Dissolve(0.2)
        mc "Mppph!" #
        "Aine muffles your words with a kiss, and her lips suffocate your desperate plea."
        "She entwines her tongue with yours as her hips buck and glides against you."
        "High and low, she attacks you on both fronts without any sign of relenting."
        "As Aine continues to lose herself in the moment, her juices overflow onto your lap, staining the bedsheets in the process."
        scene ch1ep3p2_919
        with dissolve
        "Meanwhile, the wet shlicks from her pussy coerce your dick to grow even more as blood continues to flood south." #
        "This once-prudish girl is now a possessed succubus, threatening to drain your entire life force."
        "To regain some semblance of control, you wrap your arms around her."
        "Like ever-tightening vines, your arms caress and meander around her flawless curves."
        "One hand reaches down to grab her plump ass while the other buries itself into your insatiable lover's silken hair."
        scene ch1ep3p2_920
        with dissolve
        yt "Damn! There's no stopping her now." #
        yt "All the buildup really took its toll on this girl... I mean, she's practically climaxing already, just grinding on me!"
        yt "But I have to figure out a way to slow her down somehow; otherwise, she'll wear herself out and milk me dry before we even start."
        menu:
            "Pull her hair":
                yt "Okay, let's try this..."
                play sound cloth2
                show ch1ep3p2_921
                with hpunch
                a "Nghh! Mmhhn~!" #
                "You give Aine's hair a firm tug: not enough to hurt her, but just enough to separate her face from yours."
                "Aine lets out a long, lustful moan."
                a "Nghh... [mc]..."
                a "Again!"
                mc "Again?"
                a "Do that again, dammit!"
                mc "O-okay..."
                yt "Welp. So much for slowing her down."
                play sound cloth2
                show ch1ep3p2_922
                with hpunch
                a "Mmhhhh~!!" #
                "You obey her command, pulling her back by her raven locks."
                a "AGAIN! HARDER!!"
                "Clearly, her body is in overdrive. She's so sensitive that any touch adds fuel to her flaming lust inferno."
                mc "H-harder?"
                a "PULL IT LIKE YOU MEAN IT, PUSSY!!!"
                play sound cloth2
                show ch1ep3p2_923
                with hpunch
                a "Ngghhyeaaaahh~! F...fuuuuck~!"
                "You pull her hair again, this time with so much force that Aine's neck snaps back."
                "At first, you were concerned that you were going to rip her hair out - or worse."
                "But obviously, Aine thought it was just right. Yep, she's lost it..."
                scene ch1ep3p2_924
                with dissolve
                mc "Who knew you were so kinky?" #
                a "[mc]?"
                mc "... Yeah?"
                a "Shut up and kiss me."
                scene ch1ep3p2_920
                with dissolve
                "You two continue to make out as Aine keeps grinding her soaking heat against you. Somehow, her pussy lips haven't stopped massaging you this entire time." #
            "Just go with it":
                "You two continue to make out as Aine keeps grinding her soaking heat against you. Somehow, her pussy lips haven't stopped massaging you this entire time." #
        
        "Your flag is already at full mast, twitching in response to her movements."
        "Now, you notice her legs shaking each time her clit rubs against your glans."
        play sound chair
        show ch1ep3p2_925
        with hpunch
        "Unable to contain herself any longer, she pushes you onto your back." #
        "The force is so strong that it makes your back and head hit the bed at the same time, bouncing against it."
        yt "Jesus! Where did that come from?"
        mc "Help me! The mafia is putting a hit on me!"
        scene ch1ep3p2_926
        with dissolve
        "You make a quippy joke, but Aine doesn't react." #
        "Instead, she stares at you with a slight smile."
        mc "Aine? Is everything okay?"
        scene ch1ep3p2_927
        with dissolve
        a "I've been dreaming of this moment for so long..." #
        a "Perhaps it's not only Mom who turned me into a monster but you as well."
        a "Ever since I've felt the ultimate pleasure from your hands, my thirst for it - for you - has only grown..."
        a "This part of me... is all your fault, [mc]..."
        a "But it's a part that I will never, ever complain about..."
        "Her eyes mist over as she gazes into yours."
        "The way she looks at you is as if the whole world has disappeared around you: to her, you're the only one that matters."
        yt "How can this girl change moods so quickly...?"
        "Gone is the crazed lust that possessed her just moments ago. Instead, Aine looks at you with sincerity and true love."
        "Her pearly eyes stare straight into your soul, stripping you of any defense or wisecracks you plan to use."
        "Her gaze drags you into the moment with her as if time has frozen to provide it to you."
        "For Aine, this is the moment she has been dreaming of. Finally, united with you, no more obstacles or life getting in the way."
        scene ch1ep3p2_928
        with dissolve
        "Trembling, Aine positions herself just above you." #
        "You let out a throaty groan as her soft hands grab your member, gently squeezing it."
        mc "Ngh... Aine... *huff*... Your hand..."
        "Her touch sends a jolt up and down your spine, your dick twitching in anticipation."
        "However, instead of lowering herself down, Aine hesitates, fidgeting, trying to find the right angle."
        scene ch1ep3p2_929
        with dissolve
        mc "Hey, Aine? What's going on?" #
        a "..."
        "Even though she doesn't say a word, her silence tells you her thoughts."
        scene ch1ep3p2_930
        with dissolve
        mc "Aine, hey. Look at me." #
        "Still holding onto your manhood, she looks up."
        mc "Don't worry about waiting for the perfect position or moment."
        mc "Take the moment and make it perfect."
        "You can see the determination return to her expression as she processes your words."
        a "Thank you, [mc]. I needed that."
        a "However, I must disagree with you."
        mc "Oh? Why's that?"
        a "This moment is already perfect because I'm with you."
        scene ch1ep3p2_931
        with dissolve
        "With that, she begins to lower herself." #
        a "You're mine now, [mc]."
        "You'll never stop being mesmerized by how quickly your fiancée can regain her resolve."
        "She stops herself just as your tip rests against the entrance to her last frontier."
        scene ch1ep3p2_932
        with dissolve
        a "All... mine..." #
        "She crows that last word so sensually and affectionately..."
        "... And with that declaration - as if she was claiming her birthright - she pushes you in."
        "Aine slowly lowers herself on top of you, wincing as your cock presses against her hymen."
        a "Nhh..."
        "You open your mouth to offer some comforting words."
        "But before you can say anything, she looks at you and smiles..."
        scene ch1ep3p2_933
        with dissolve
        a "N-nghh~!" #
        "... And without any further hesitation, she pushes you inside down to the hilt, tearing through her maidenhead."
        "Her hands claw into your skin as her body adjusts to the pain caused by your girth."
        "However, other than a small groan and the red trickle coming from her vagina, her expression conveys no sense of discomfort."
        show aine10
        with dissolve
        "Instead, she follows her natural instincts and sinks her lips into yours."
        "You happily receive them as your tongue twirls with hers."
        "The taste of Aine's saliva intoxicates you further as she slowly begins to ride you."
        "As she moves, her legs slightly shake as she tries to adapt to the massive stick of meat now inside her."
        "You're certain that this doesn't feel comfortable for her, yet she keeps kissing you without even a hint of easing up."
        "To alleviate her discomfort, you keep your hips as still as possible. That should allow her time to get used to you inside her."
        a "Mmhh~..."
        "And sure enough, before you know it, she lets out a moan - this time, from pleasure."
        "Managing to overcome the sharpness of the initial pain, Aine lets out a deep sigh and starts moving faster."
        "In response, you also begin to gently buck your hips, mirroring her up and down motion."
        a "F-finally... mmhhh... this feels.."
        mc "Good? Painful? Indescribable?"
        a "Completely {i}right{/i}."
        "Aine sings an adorable tune with her moans as she continues to move."
        "In this moment, being completely bare and exposed to each other... it feels..."
        "Totally right, as Aine said."
        "Nothing else to hide. No more wondering who you really are to each other."
        "Only understanding. And most importantly, unity."
        "Once again, you feel Aine's secretions coating your entire dick."
        "Arousal overtakes her, causing her to arch back up as she drives herself along your length." 
        "The walls of her vagina are so tight, yet so incredibly soft at the same time."
        "It's as if, like their owner, her labia are holding onto you for dear life as she keeps up her motions."
        "As her accelerating breaths become shallower, she moves faster: far more than you expected."
        yt "Whoa, Nelly!"
        "You speed up as well, desperate to match her pace."
        "Her inner walls contract with each movement you both make, causing your cock to twitch in sync with her involuntary spasms."
        "As another sign of her peaking arousal, her hard nipples rub against your chest, practically trying to cut through your skin with their firmness."
        "You feel her vagina expand, allowing your shaft even more access to move."
        "Your hands cling onto Aine's waist, digging your nails into her flesh as you pull her body against you."
        "Now, your primal instincts start to take over as you drive yourself as deeply as physically possible."
        "As the pleasure builds, it takes every ounce of your remaining willpower not to grab her ass and full-strength thrust into her."
        "After all, she showed courage to take you completely inside on her own, so the least you can do is to let her enjoy her perfect moment."
        yt "Yep, that's what our world feels like right now..."
        yt "Absolutely... perfect..."
        yt "Two bodies... two minds... two souls... so perfectly entwined together."
        "You take in the taste of her lips... the scent of her sweat... the sounds of her moans... the feeling of her soft milky skin brushing against yours..."
        "And finally, your lover's... {b}your{/b} Aine's gorgeous face, this incredible beauty in plain sight."
        "Not a single sense is left ignored."
        "You're being completely consumed by Aine, something that you thought was impossible just a few days ago."
        "However, now it feels like exactly how things should be."
        "The growing feeling in your nether regions is also a nice bonus."
        "Aine's exquisite, pure form continues crashing herself onto you back and forth."
        "However, despite her vaginal muscles continuing to massage your cock, you feel Aine slowing down."
        yt "Hold on. Is she getting tired? Maybe having second thoughts?"
        yt "No, that couldn't be it... right?"
        yt "Well, as much as I hate to stop this... better find out what's on her mind."
        "You slow down with Aine, easing your grip on her hips so she can slowly extricate you from her insides."
        show ch1ep3p2_934
        with dissolve
        hide aine10
        "Finally, your lips part ways, breaking the kiss that seemed like an eternity."
        "You scan Aine's face for any sign of discontent."
        "But all you see is her lips glistening and her loving eyes taking in every detail of your visage."
        mc "You feel... so incredibly tight, Aine. A-are you okay?"
        "You struggle to find the right words as your heart races."
        "Aine's mind is still wandering in another realm; it doesn't hear a thing you say."
        "Face flushed, skin glistening, her chest rises and falls with every breath."
        "She occasionally lets out euphonic moans that send tingles throughout your core as she stares at you, lost in thought."
        "You etch the gorgeous sight into your long-term memory."
        scene ch1ep3p2_935
        with dissolve
        mc "Ai-..." #
        "You part your lips to comment but are interrupted by her timid words."
        scene ch1ep3p2_936
        with dissolve
        a "[mc]... [mc], I love you..."
        mc "And I love you, Aine."
        a "This feels... too good to be real..."
        "She continues, seemingly in a state of trance."
        a "It feels like I'm going to wake up from this dream at any time..."
        a "I'm so scared..."
        "The anguish in her sincere voice crushes your heart."
        "As she soldiers on to finish her thought, she shakes like a wind-blown leaf."
        scene ch1ep3p2_937
        with dissolve
        a "...Aah *hics*... but at the same time, even in my wildest fantasies..." #
        a "I never would have been able to... imagine these... feelings..."
        "Aine lovingly - tenderly - cups your cheeks, her eyes brimming with tears."
        "She caresses you so tenderly. It's as if she thinks any strong touch will push you away from her." 
        "Again, tears flow down Aine's rosy cheeks, drops falling onto your chest."
        "Like a dam cracking after holding repressed emotions and desires for so long..."
        "... She is finally breaking free from her prison. These are her first steps to relinquish her guilt and forgive herself."
        "With every tear that falls on your skin, you feel your bond, your resolve to protect this angel, strengthening."
        "As if she wants to make sure that bond is permanent, Aine slowly begins to move her hips against you again."
        "Finally able to find words through the charged emotional atmosphere, you speak."
        scene ch1ep3p2_938
        with dissolve
        mc "Aine... I'm real as it gets." #
        "You lift your hands and cup her cheeks in return."
        mc "Do you not feel me...?"
        "You rest your hands gently against Aine's skin as if holding a newborn kitten."
        mc "Do you not hear my heart beating for you?"
        mc "I am here. I am yours..."
        mc "... And I'm not going anywhere."
        "You use a stern yet loving tone to reassure her."
        mc "I will protect and cherish you to the last fiber of my being."
        "Aine pauses, completely blindsided by your declaration." #
        "Her eyes widen in surprise at such a direct revelation."
        "But you aren't done..."
        mc "I love you, Aine."
        mc "I love you to the marrow of my fucking bones."
        "You say it as bluntly as you know how."
        scene ch1ep3p2_939
        with dissolve
        "Before she can process, you decide to seal this promise by kissing her again." #
        "Her lips are shaky at first, but she quickly relaxes and accepts you, leaning in passionately."
        "With every part of your beings now laid bare for each other, what you're doing is not just a simple sexual act anymore."
        "You are truly... making love."
        "That realization makes your dick throb inside Aine, eliciting a moan."
        scene ch1ep3p2_940
        with dissolve
        "Finally, she breaks the kiss and pushes you back down." #
        "You see her with a newfound confidence... again."
        "Another breakthrough."
        "With a smile on her tear-kissed face, she uses her hands to hold you in place."
        "This may be your shared moment, but this is her show. And she's making sure you know that."
        a "You'll make any woman swoon with words like that, [mc]..."
        a "But I'm not just any woman."
        scene ch1ep3p2_941
        with dissolve
        a "Let me show you what the real Aine can do." #
        mc "Yes, please."
        show aine11
        with dissolve
        "Your fiancée leans back, grabbing onto your legs for balance."
        "In return, your hands reflexively latch onto her thighs to support her."
        a "I can... finally see you... all of you..."
        "You are, however, too mesmerized by the sight before your eyes to hear her."
        "Aine's breasts bounce to the rhythm of her impaling herself onto your hard member, hypnotizing your primitive mind."
        "Her silken black hair dances wildly with her movements."
        "And, of course, the rest of Aine's curves glisten perfectly in the dim light. So seductive, so sensual."
        "What man wouldn't pause to take in this sight?"
        a "I-I see... someone is... enjoying the view..."
        "She offers a sly quip to snap you out of your reverie."
        a "Wipe that d-drool... off your mouth... [mc]... mmmhh~"
        "Amid her witty comments and moans, she rides you like you're a galloping bronco."
        "The inside of Aine's warm, wet cunt caresses your cock, reigniting the fire burning in your belly."
        "Every time she slams down onto you, your balls slap against her ass."
        "The sound serves as a metronome to keep your movements in perfect sync."
        mc "Can you blame me? You look absolutely stunning."
        mc "I wish you could see what I'm seeing... because that's the only way to understand how amazing you are."
        "Aine's cheeks instantly grow bright red."
        a "S-shut up and let me-nghh... ride you! Your f-flattery... isn't g-going to earn you more points, [mc]!"
        "You decide to heed her words and enjoy the moment, gripping her thighs tighter."
        "You want to-no, you {b}must{/b}, leave your mark on every inch of her."
        a "Ghhn~!"
        "As you squeeze her thighs, Aine bites her lip to suppress a moan."
        a "F-ffuuuckkk..."
        "You chuckle, amused at the rare vulgar word that emerged from her mouth."
        yt "Well, shit... You are one kinky lass, Aine."
        a "You...nghhh... are you l-laughing at me, huh?"
        mc "Laughing at you? I wouldn't f-fuuuuuuckking dare!"
        a "H-hmph~!"
        "Aine does her best to give you a pouty face, but she's far too distracted by what is happening below her to hold her expression."
        a "Mmhhh~! Hnnggg~!"
        "The same things are also starting to take their toll on you."
        "The movements of her entire pelvic region send shockwaves up your spine."
        "Soon, you too begin to groan as you can no longer hold back."
        mc "G-good god, Aine. Your pussy is...mmmh... sucking the life out of me."
        a "H-huh?"
        "At first, she doesn't fully grasp what you said."
        "But a second later, you see her lip curl into a smirk."
        a "Ahh... [mc]... You better-hahhh~ g-get... used to it." 
        a "C-cause I'm not stopping... this feels... too good!" 
        "Every time she drops herself onto you, your head hits that perfect place on her g-spot, beckoning another chorus of moans from your fiancée."
        "The sound of wet flesh colliding against each other coupled with the clash of moans reverberates throughout the room, creating a symphony of love and lust."
        yt "Music to my ears."
        "Aine's grip on your knees tightens even further. Thrust by thrust, she loses control of her mind as her carnal instincts take over."
        "As you struggle to control your accelerating breathing, Aine's moans become more high-pitched and guttural."
        a "Nghhhh!! Aaahhh!! Mmmhhhh!!!"
        "Her eyes roll back as her nails dig hard into your skin."
        "And her pussy forms a vice around your dick as it contracts violently."
        "If she weren't so drenched, it would be nearly impossible to slide your member in and out of her."
        "But right now, that's the least of your worries."
        yt "Dammit! I'm right there with you, Aine!"
        "The pleasure builds in your groin, diffusing throughout your body."
        "You feel the edge approaching rapidly. Frantically, you try to think of anything to keep you from going over."
        "But your mind draws a blank, too inebriated by arousal."
        "However, just as you think you're about to let go..."
        play sound chair
        show ch1ep3p2_942
        with hpunch
        hide aine11
        a "F-FFFFUUUUUUCCCCKK!!!!"  #
        "Aine arches back violently. Her vaginal walls convulse around your cock, holding it in place and squeezing along its entirety."
        "Her legs shake, and she lowers her chin, biting her lip to hold back the remaining moans." #
        a "*whimpers* Hmm... hnnn..."
        "Unable to restrain yourself, you also fall over the edge."
        mc "Hrrngg!!"
        "You shoot your load as far into her as your dick can reach."
        "Three... four... five times your cock twitches..."
        "Before it finally relaxes to rejuvenate."
        "By the looks of it, all the buildup just showed their consequences. For both of you."
        scene ch1ep3p2_943
        with dissolve
        yt "Wow. That just... happened..." #
        "You breathe wordlessly, forcing yourself to enjoy this moment without interrupting."
        play sound chair
        show ch1ep3p2_944
        with hpunch
        "Aine falls forward, throwing her arms out at the last second to stay upright." #
        "Her hands find your shoulders, pinning you in place."
        "As her chest heaves out each time she fills her lungs, her perky nipples dangle in front of your eyes."
        "Glazed with sweat, they look so delicious... so tempting..."
        "You would say she looks like a goddess straight out of a sculpture or a painting..."
        "But you can't recall many paintings depicting a goddess right after peak coitus."
        scene ch1ep3p2_945
        with dissolve
        mc "Are you okay?"
        a "Y-yeah... just... one min... minute..."
        "Her enthusiasm got the better of her as she looked completely spent."
        "Luckily, you have an idea to help her regain her strength."
        mc "I have to say, you look so adorable."
        "The abrupt comment makes her tense up, and if her face wasn't completely flushed already, she would have been by now."
        scene ch1ep3p2_946
        with dissolve
        a "Y-you-...!"
        play sound chair
        show ch1ep3p2_947
        with hpunch
        "But before she can react, you wrap your arms around her back, then use your hips as a lever to topple her." #
        "You then roll Aine onto her back, pinning her down under you."
        "Aine's mouth hangs open, shocked at your sudden judo mastery."
        mc "Yes, me. It's my turn now."
        mc "I've waited patiently enough. Seeing your entire beauty as you orgasmed on top of me... I won't just be a spectator anymore."
        scene ch1ep3p2_948
        with dissolve
        a "[mc]..." #
        "Aine's face shows a bit of frustration. You can't tell if it's because she's so powerless or you keep teasing her."
        mc "Aine, I'm-!"
        a "That mindless move you just did cause your... stuff to leak out of me!"
        a "That's going to stain, stupid!"
        "Instead of anger, Aine decides to tease you back."
        a "A-and don't call me cute when I'm like this!"
        "Never mind, there's the anger-but just a little."
        scene ch1ep3p2_949
        with dissolve
        "Chuckling, you gently stroke the top of her head, just the way she loves it." #
        a "Mmhh..."
        "Forgetting her slight anger, Aine smiles, contentedly purring like a kitten." 
        "Such a simple gesture, yet at the worst times of her life, it was her one mote of happiness. The sole warm flame in the cold darkness."
        "No wonder why she loves them."
        mc "Consider this teasing a payback for all those years of tormenting me."
        scene ch1ep3p2_950
        with Dissolve(0.2)
        a "I-I'm s-" #
        mc "Relax, Aine. Would I have let you in my house if I really resented you for what you did?"
        mc "Would I have picked you up after you met with Hera?"
        mc "Would I have agreed to give \"us\" another chance?"
        mc "You might say you're lucky to have me, but once you manage to see the amazing woman that I have been seeing this whole time, you'll know that I'm the one who's lucky."
        a "I-I really hope to be worthy of that title someday, [mc]..."
        mc "Someday? You already are."
        "Your words make her heart flutter. But you're done waiting."
        scene ch1ep3p2_951
        with dissolve
        mc "Now come here. I'm not done with you." #
        "Reaching out to grab your member, you slide the tip up and down her slit, using it to kiss her clit and prod against her entrance."
        a "Mhhhhh~"
        "You get a clear reaction as Aine breathes heavily."
        scene ch1ep3p2_952
        with dissolve
        a "Haa... [mc]... That feels so g-good~" #
        "Her words and reactions do their part to reinvigorate your little soldier."
        "And before long, your cock grows hard enough to push the tip into Aine's hole."
        a "Don't keep a lady waiting, [mc]! Put it in already~!"
        "Aine impatiently bucks her hips against you, trying to soothe that aching need to feel you inside her."
        mc "Such an impatient, dirty princess. But you're right; I did say I was done waiting."
        show aine12
        with dissolve
        "With that, you push forward. Again, ingraining yourself within her."
        a "Aaahhh~!"
        a "Y-YES!!"
        "With a loud moan, Aine's hips recoil from your thrust, and her eyes immediately roll back."
        yt "Wow, no wonder why she was so impatient."
        "Her juices immediately start to flow again, allowing your dick to glide in and out smoothly."
        "Still aroused from the earlier orgasm, Aine's womanhood meets you with no resistance, absorbing your length with ease."
        "Not too tight, not too loose. Just right."
        "Even though you've barely restarted, Aine's already wailing in the sluttiest ways."
        a "Fuuuuh~! Ahhh~! Fuck~! That's...!"
        a "Y-yes! P-pound me, [mc]! FUCK ME SENSELESS!!"
        yt "Heh, didn't know she had that in her. Either way, her words are turning me on so, {i}so{/i} much."
        yt "But... I'm also a bit scared that this two-week period may have broken her..."
        yt "Who would have thought that this rich mafia heiress, who barely knew what sex was..."
        yt "... Would now be craving it like a nympho on crack?"
        yt "Don't get me wrong, I love this new brazen, unabashed, Aine."
        yt "But at this rate, her pussy might just swallow my dick whole, leaving just the base..."
        yt "... Ah, doesn't matter, had sex. Let's keep diving in."
        "You pick up the pace, practically slamming into the tip of her cervix every time you move forward."
        "Gone is the time for the overflowing emotions and confessions."
        "Now, it's time for unadulterated lust to take over as you make Aine yours."
        a "Hnngh~! MMMHHH~!!"
        "Based on her reaction, speeding up is exactly what Aine hoped you would do."
        "As your member takes Aine's pussy to pound town, you focus your attention on her tits."
        "Your hand holds one captive, indenting the milky skin with your fingerprints."
        "Meanwhile, unlike its twin being held in place, Aine's other breast bounces freely with your thrusts."
        mc "A g-guy could get u-used to this sight..."
        a "Mmhh! J-just a-any guy?"
        "Unbeknownst to you, you say your thoughts out loud."
        mc "N-nope. Your-mmh!-mine, and mine only."
        "Taking a glimpse at Aine's face, you see her biting her finger to try and contain her screams before giving up and grabbing the bedsheet while she moans her throat out."
        a "Nghahhh~! Hmmmm~!"
        "As if the massage Aine's vagina has been giving you wasn't enough... what your eyes are witnessing is revving your balls up to launch another giant load."
        yt "Fuck, gotta hold on... GOTTA HOLD ON!"
        show aine13
        with dissolve
        hide aine12
        "Desperate to delay the inevitable, you lean forward, resting on top of Aine."
        "Like war drums, your hearts thump against each other's chests, fully in tune with each other's bodies."
        "You push yourself into Aine, not pulling out too far."
        "You don't want to be away from her. You want to stay like this: fully connected."
        "And as an added bonus, less movement might mean more time before you reach the end."
        "Aine wraps her legs around your back as if to tell you she won't let you go anywhere."
        "It's almost as if being this close allows her to read your mind."
        mc "My god...!"
        "You let out an animalistic shout, psyching yourself up to hold onto your load just a little longer."
        "Between each thrust, you breathe in, inhaling Aine's raw scent."
        "You burn her smell into your mind, ensuring that she will always be a part of you no matter what happens."
        "With each thrust, you also grind your groin against her clit, giving her another source of stimulation."
        a "Ngahh~! Mmph~! Hahhh~!"
        "Your actions pay immediate dividends as her moans become more uncontrolled."
        "Aine desperately tries to breathe in between the moans exiting her lungs, but she's losing that battle with each thrust you deliver."
        "You're not faring much better, as Aine's pussy once again starts to contract against your dick rhythmically."
        "It's a signal that she's close; but it also rapidly breaks down what little willpower you have left to hold back your cum."
        a "[mc], I-I feel-NGHH!!"
        a "C-close!"
        "Barely able to speak that last word, Aine's mouth hangs open, preparing for the climax."
        mc "Fuckkk! Aine, I'm-kuh...! Cumming!"
        a "Cum with me~! Don't stop!"
        a "Fill me up, [mc]~! Don't hold back, please! PLEASE~!"
        "Her voice saying your name is the last straw."
        play sound chair
        show ch1ep3p2_953
        with hpunch
        hide aine13
        mc "Gahhh!! AINE!!" #
        a "NNGHHHHH!!"
        "Your hips thrust forward, ejaculating another load deep into Aine's gut."
        "Your dick collides against her uterus, filling her entire vagina with each jet of hot cum."
        "Somehow, this salvo feels even larger than the first."
        "Aine's toes curl up as her body is overtaken by spasms, a sign of her autonomic nervous system seizing full control."
        "Her legs squeeze against your sides as her pussy contracts even more violently around your shaft."
        "Each burst from your cock causes her to convulse even stronger than the prior convulsion."
        scene ch1ep3p2_954
        with dissolve
        a "Hmm~! Hnnngh!" #
        "At last, Aine seems to use up the last of her energy."
        "As her contractions fade, she lies below you motionlessly, save for her breathing."
        "For the moment, you remain on top of her as you attempt to recover from your own intense climax."
        scene ch1ep3p2_955
        with dissolve
        "Without exchanging words, you plant a kiss on Aine's lips." #
        "A perfect ribbon on top of this moment when you finally, at long last, made this woman yours."
        "Because that's what she is: a stunning, precious, perfect woman. All of her."
        "After a long, deep kiss, you pull out, letting your overflowing love spill out of her."
        stop music2 fadeout 2

        scene black
        with dissolve
        with fadeq

        play music 'audio/FirstCrush.mp3'
        scene ch1ep3p2_956
        with dissolve
        a "... We're definitely going to need new bedsheets..." #
        mc "Totally worth it, every single second."
        a "You're as ridiculous as the first time I met you."
        mc "I'm serious, Aine."
        scene ch1ep3p2_957
        with dissolve
        a "I know, I can tell." # she smiles sincerely #####
        mc "Then, promise me something..."
        scene ch1ep3p2_958
        with dissolve
        a "What's that?" #
        mc "Stop seeing me as someone you have to make up to. I don't need that from you, not anymore."
        a "I promise, [mc]. I'll remember that, always."
        scene ch1ep3p2_959
        with dissolve
        a "But... let's just be hopeful about the future, accepting our past, and using what we learn today to build the life we want." #
        mc "Exactly. We weren't always on the same page, but look at us now."
        mc "I know we'll make it. Together, with everyone."
        a "Mhm."
        scene ch1ep3p2_960
        with dissolve
        a "... You know, when Mom left, she actually smiled at me. Genuinely. For the first time." #
        a "It's weird... I feel so relieved, but also like I've lost something I can't quite describe."
        scene ch1ep3p2_961
        with dissolve
        a "Goddamnit, I still feel defeated..." #
        mc "Knowing your mom, we might never figure that out."
        a "*sighs*"
        scene ch1ep3p2_962
        with dissolve
        mc "So, is it safe to say I can stay here tonight?" #
        a "Of course, this is your room, you know? I never asked you to move out in the first place. Literally, I mean."
        mc "Thought so..."
        scene ch1ep3p2_963
        with dissolve
        mc "I heard from Sky you kept your ring on all week despite our... issue." #
        a "It never even occurred to me to take it off. I told you, it feels wrong without it."
        mc "*chuckles* You just keep making me fall for you more."
        a "Enough with the cheesiness, okay? Have you eaten yet?"
        mc "No, not really. Couldn't eat much with you on my mind."
        scene ch1ep3p2_964
        with dissolve
        a "Let's fix that. How about we head to the kitchen? What are you in the mood for?" #
        yt "From someone who couldn't cook to now offering to make me dinner?"
        yt "I can't imagine ever letting her go again. That would be the end of me."
        scene ch1ep3p2_965
        with dissolve
        mc "You know, I could just dine on you every night." #
        a "*giggles* That's quite enough out of you, [mc]."
        $ renpy.end_replay()
    else:
        scene black
        with dissolve
        with fadeq

        "A week later..."
    stop music fadeout 2
    
    call hide_days from _call_hide_days_17
    with dissolve
    scene black
    with dissolve
    with fade

    show screen day_sunday with dissolve
    play music 'audio/YouMeanTheWorld.mp3'
    play sound cityalley loop
    scene ch1ep3p2_772
    with dissolve
    pause
    scene ch1ep3p2_773
    with dissolve
    pause
    scene ch1ep3p2_774
    with dissolve
    f "Moon?"
    scene ch1ep3p2_775
    with dissolve
    f "Hey, what's up?"
    m "Is that my scarf?"
    scene ch1ep3p2_776
    with dissolve
    f "Oh, this? Yeah, I found it in the laundry room. I thought it was okay to borrow it for a bit."
    m "Please put it back. It's not meant to be worn casually like that."
    scene ch1ep3p2_777
    with dissolve
    f "Wait, really? Why not?"
    m "Just put it back."
    f "Okay, okay, no problem."
    scene ch1ep3p2_778
    with dissolve
    f "You've been standing out here for a while, haven't you? It's pretty chilly. Why not head inside?"
    m "I'm waiting for [mc]. Isn't he usually with you around this time?"
    f "Yeah, but today's been crazy at work. He's swamped with even more stuff than I was."
    f "I wanted to wait, but he practically shooed me off, saying I should head home."
    f "I'm so beat, I feel like I could crash any second now, so I just took his offer."
    scene ch1ep3p2_779
    with dissolve
    m "Got it, thanks."
    f "Hey, hold up! Where are you off to?"
    m "To your workplace."
    f "Oh, okay then. Just be careful, alright?"
    scene ch1ep3p2_780
    with dissolve
    f "..."
    f "Did I really tell her to be careful...?"
    scene ch1ep3p2_781
    with dissolve
    f "*yawn*"
    scene ch1ep3p2_782
    with dissolve
    f "Man, I'm really out of it... Hope I don't zonk out before dinner..."
    stop sound fadeout 2

    scene black
    with dissolve
    with fade

    scene ch1ep3p2_783
    with dissolve
    mc "..."
    scene ch1ep3p2_784
    with Dissolve(0.2)
    m "Hey."
    play sound woodhit
    show ch1ep3p2_785
    with hpunch
    mc "JESUS FUCKING CHRIST ON A MOTORBIKE!!!"
    m "'Sup?"
    scene ch1ep3p2_786
    with dissolve
    mc "What are you doing here?!"
    m "To make sure you're good."
    scene ch1ep3p2_787
    with dissolve
    mc "..."
    scene ch1ep3p2_788
    with dissolve
    mc "Is that really all you came here for?"
    m "..."
    mc "Hey, don't even think about it. You always look away from me when you're about to deny something."
    image moonmcbstapostgr:
        "ch1ep3p2_789.jpg"
        pause 3.0
        "ch1ep3p2_790.jpg"
        pause .2
        repeat
    show moonmcbstapostgr
    with dissolve
    m "I just... I graduated. And now I don't really have anything to keep me busy."
    m "It's... kind of uncomfortable not having you around."
    mc "Wait, you're feeling uncomfortable without me? That's... new."
    m "Don't make it weird. It's just that I'm used to having a purpose. Guarding you, college... and now it's all just... empty."
    mc "I get it. It's a big change."
    mc "But you know, there's a whole world out there. You can do anything."
    m "It's not that simple. After moving here, I've spent so long as your bodyguard and as a student."
    m "I don't even know what \"anything\" could be for me."
    scene ch1ep3p2_791
    with dissolve
    mc "Well, why not start by exploring what you like? There must be things you're interested in."
    m "I guess... I haven't really thought about it. I've always been focused on things specifically assigned to me."
    mc "Look, Moon, you've got skills, not just bodyguard-ing. There's more to you than just that."
    mc "I know you're committed to your duty, but isn't it time to explore what else life has for you? You've been at a crossroads since graduation, haven't you?"
    m "Honestly, I'm not sure. When you're not around, I feel... off, unsettled. Like something's missing, and it leaves me restless."
    scene ch1ep3p2_792
    with dissolve
    mc "..."
    yt "She's not wrong. I can feel it too: this subtle bond that's formed between us."
    yt "Sure, her sudden appearance startled me, but there was also this inexplicable relief that washed over me the moment I saw her."
    yt "When did this connection actually start? It's hard to pinpoint. But it definitely has strengthened since we've become much closer."
    yt "It's unlike anything I've felt before, and I can't quite put my finger on it."
    scene ch1ep3p2_793
    with dissolve
    mc "Give me a little time to finish up here. Then we'll head home together, okay?"
    m "I'm not going anywhere without you. I'll wait."
    stop music fadeout 2

    scene black
    with dissolve
    with fadeq

    "After dinner..."

    scene black
    with dissolve
    with fadeq

    play music 'audio/StrangeConnection.mp3'
    scene ch1ep3p2_794
    with dissolve
    pause
    scene ch1ep3p2_795
    with dissolve
    mc "This has been wrestling in my mind for a while. Now seems like the right time to talk about it."
    m "Hm?"
    mc "Man... I don't even know how to explain it..."
    scene ch1ep3p2_796
    with Dissolve(0.2)
    m "Do you want me to-"
    play sound woodhit
    show ch1ep3p2_797
    with hpunch
    mc "Whoa, whoa, whoa! Hold on!"
    m "They say it's a way to get people to talk."
    mc "Not talking and not being able to explain are two different things!"
    scene ch1ep3p2_798
    with dissolve
    mc "So... about you feeling uneasy when I'm not around. That could mean anything. But do you ever sense this unusual... connection when we're together?"
    m "What kind of connection?"
    mc "Like I said, I don't know how to explain it. It's a feeling I've never had before."
    mc "Strange, but it's there. Do you feel it too?"
    m "Because I grew up the way I did, my social development is lacking."
    m "It's only recently that I've been able to live my own life, thanks to you. So I have a lot of \"never felt this before\" moments. Can you elaborate?"
    scene ch1ep3p2_799
    with dissolve
    mc "Okay, let me rephrase. How do you feel right now, at this moment?"
    m "... Cold?"
    mc "No, not the temperature! Something deeper within, maybe?"
    scene ch1ep3p2_800
    with dissolve
    m "..."
    scene ch1ep3p2_801
    with dissolve
    m "... Beyond that, I feel... grounded. And whole, somehow..."
    scene ch1ep3p2_802
    with dissolve
    yt "Still not what I'm looking for..."
    menu:
        "Hold her shoulder":
            scene ch1ep3p2_803
            with dissolve
            mc "Now, tell me. What do you feel?"
            m "..."
            scene ch1ep3p2_804
            with dissolve
            m "I felt... a sudden jolt inside. But I don't know where, or... what it was..."
            m "It was weird."
            mc "Yes, that! I started to feel like that ever since we got closer to each other!"
            m "What was that...?"
            mc "That \"jolt\" thing? I don't have a clue."
            m "... Now that I'm aware, I felt the same thing when you talked to me on the sofa."
            mc "Like, where? We've talked on a lot of sofas before."
            m "Back in my headquarters. I felt you coming."
            mc "Huh...?! You felt me... coming?"
            m "Yeah."
            mc "What the hell..."
            scene ch1ep3p2_805
            with dissolve
            m "Y...your hand."
            mc "Sorry, is it cold?"
            m "Yeah, a bit."
        "Hold her hand":
            scene ch1ep3p2_806
            with dissolve
            pause
            scene ch1ep3p2_807
            with Dissolve(0.2)
            m "*lightly gasps*"
            mc "Now, tell me. What do you feel?"
            m "..."
            scene ch1ep3p2_808
            with dissolve
            m "I felt... a sudden jolt inside. But I don't know where, or... what it was..."
            m "It was weird."
            mc "Yes, that! I started to feel like that ever since we got closer to each other!"
            m "What was that...?"
            mc "I wish I knew..."
            m "... Now that you mention it, I remember feeling something similar back when we talked on the sofa."
            mc "Which sofa? We've talked on quite a few."
            m "In my headquarters. I sensed your presence before I even saw you."
            mc "You sensed me... coming?"
            m "Mhm."
            mc "What the hell..."
            scene ch1ep3p2_809
            with Dissolve(0.2)
            m "Uhm... y...your hand." #
            mc "Sorry, is it cold?"
            m "Yeah, a bit."
            $ moonpoint += 1
            $ renpy.notify(moonnotif)

    stop music fadeout 3
    play music2 'audio/HarvestMoon.mp3' fadein 3 loop
    scene ch1ep3p2_810
    with Dissolve(1.0)
    mc "Don't worry, this is about as bad as it gets here. It never even snows."
    m "I hope it stays that way."
    scene ch1ep3p2_811
    with dissolve
    mc "Hm? Why's that?"
    m "In the military, snow has always been seen as a bad omen."
    m "They say when it snows, the pristine white reveals the true color of blood - a perfect reminder of life's fragility."
    m "Snow doesn't just blanket the ground; it unveils the hidden truths, often the painful ones."
    m "It's believed to foreshadow deaths, marking the world with a reminder of loss."
    mc "That's a pretty intense perspective on snow."
    scene ch1ep3p2_812
    with dissolve
    m "Maybe it's an old belief, but it's always been a part of how I see the world."
    m "It reminds you that there's often more beneath the surface, even in something as beautiful as a snowfall beneath the moon..."
    scene ch1ep3p2_813
    with dissolve
    mc "..."
    scene ch1ep3p2_814
    with dissolve
    mc "It's interesting how something as simple as weather can hold so much meaning."
    m "Mhm."
    scene ch1ep3p2_815
    with dissolve
    mc "You know, Moon, I've always appreciated your perspective."
    mc "Yeah, you're an oddball, but you have these interesting things to tell."
    mc "And... I've come to realize there's something between us. Something more than just a bodyguard and her charge."
    mc "Whatever it is, whatever we're feeling, I'm glad you're a part of my life."
    scene ch1ep3p2_816
    with dissolve
    m "And I promise you, commander, no matter what happens, I'll be there when you need me. Always. As long as I'm alive."
    mc "Well... honestly, you don't have to try to accomplish anything special."
    mc "Even if no one likes you. Even if no one praises you... just being alive now is great enough."
    mc "\"How nice is it getting to live another day?\". You can say it with a smile."
    mc "And that's enough, isn't it?"
    m "*chuckles* Thank you."
    scene ch1ep3p2_817
    with dissolve
    mc "It's something Jovian used to tell me."
    mc "On the other hand, I want to achieve something. One thing I've been longing for ever since I met all of you."
    mc "I just want to live peacefully - together."
    mc "Someday, we'll never have to worry about anything. And I will make it happen."
    scene ch1ep3p2_818
    with dissolve
    m "At your disposal, Commander."
    mc "I'll count on you, Moon."
    m "Of course. That's why I'm here."
    mc "*chuckles*"
    scene ch1ep3p2_819
    with dissolve
    mc "Oh, by the way, is Freya still awake?"
    m "I doubt it. She seemed absolutely beat when she got home."
    scene ch1ep3p2_820
    with dissolve
    mc "Ah, shoot! I completely forgot about that thing!"

    scene black
    with dissolve
    with fade

    play sound doorknock
    scene ch1ep3p2_821
    with dissolve
    mc "Frey...?"
    "..."
    play sound doorknock
    mc "Freya, can we come in?"
    scene ch1ep3p2_822
    with Dissolve(0.2)
    m "Hey Freya, guess what? Your recent post just blew up online!"
    "..."
    scene ch1ep3p2_823
    with dissolve
    m "No reaction. She's definitely out like a light."
    mc "Huh...? What was that for?"
    m "She's usually obsessed with social media updates. I thought it might do the trick."
    m "Try the door. She's not one to lock it."
    if freyaroute:
        yt "Oh yeah, we've learned that the hard way..."
    play sound doorknob
    scene ch1ep3p2_824
    with dissolve
    mc "It's open."
    m "Leave your gift on her desk or by her bed. She'll see it when she wakes up."
    mc "Good call."
    play sound closedoor
    scene ch1ep3p2_825
    with dissolve
    pause
    scene ch1ep3p2_826
    with dissolve
    yt "Never fails to amaze me how you and your sister's sleeping positions are out of this world, Freya."
    scene ch1ep3p2_827
    with dissolve
    yt "Hope she likes whatever Hera bought for her."
    play sound closedoor
    scene ch1ep3p2_828
    with dissolve
    m "All set?"
    mc "Yeah, gift's delivered."
    scene ch1ep3p2_829
    with dissolve
    mc "Hey, I'm pretty beat. I think I'm gonna hit the hay as well."
    m "Alright. Sleep well, [mc]."
    mc "You too, Moon. Good night."
    if moonroute:
        scene ch1ep3p2_830
        with dissolve
        pause
        play sound woosh2
        show ch1ep3p2_831
        with hpunch
        pause
        scene ch1ep3p2_832
        with dissolve
        mc "Was that entrance necessary?"
        m "Yes. Those other times don't count. This is my first real kiss with you."
        m "I wanted to be the one to initiate my first kiss. Then maybe, next time, I want you to take the rest from me."
        mc "Oof... You're really tempting me now."
        m "Have a good one, Commander."
        mc "*chuckles* You too, Moon. Sleep well."
    scene black
    with dissolve
    scene ch1ep3p2_833
    with Dissolve(2.0)
    mc "..."
    scene ch1ep3p2_834
    with dissolve
    mc "...."
    scene ch1ep3p2_835
    with dissolve
    mc "To who we'll be in the future: May we meet with grace the scars of our past, and let the memories of today guide us towards a world we dream of."
    scene ch1ep3p2_836
    with Dissolve(1.0)
    pause
    scene ch1ep3p2_837
    with Dissolve(1.0)
    pause
    scene ch1ep3p2_838
    with Dissolve(1.0)
    pause
    scene ch1ep3p2_839
    with Dissolve(1.0)
    pause
    scene ch1ep3p2_840
    with Dissolve(1.0)
    pause
    scene ch1ep3p2_841
    with Dissolve(1.0)
    pause
    scene ch1ep3p2_842
    with Dissolve(1.0)
    pause
    scene ch1ep3p2_843
    with Dissolve(1.0)
    pause
    scene ch1ep3p2_844
    with Dissolve(1.0)
    pause
    scene ch1ep3p2_845
    with Dissolve(1.0)
    pause
    scene ch1ep3p2_846
    with Dissolve(1.0)
    pause
    scene ch1ep3p2_847
    with Dissolve(1.0)
    pause
    scene ch1ep3p2_848
    with Dissolve(1.0)
    pause
    scene ch1ep3p2_849
    with Dissolve(1.0)
    pause
    scene ch1ep3p2_850
    with Dissolve(1.0)
    pause
    stop music2 fadeout 3
    scene black
    with Dissolve(3.0)
    pause
    call hide_days from _call_hide_days_18
    with dissolve
    show ch1ep3p2end
    with dissolve
    pause 88.0
    scene black
    with dissolve
    play music 'audio/ParticleEmission.mp3'
    scene ch1ep3p2_851
    with Dissolve(1.5)
    h "Please, Jess..."
    h "I know I've made mistakes. Please, I'm begging you..."
    h "Look after my daughters for me...!"
    j "..."
    play sound cloth
    scene ch1ep3p2_852
    with dissolve
    j "It's hard to see you this way. So broken, so desperate. But I can't do what you're asking."
    j "I warned you once, but you ignored me. You've lost my sympathy."
    j "However, there's one thing I need from you."
    scene ch1ep3p2_853
    with dissolve
    h "Anything, please tell me!"
    scene ch1ep3p2_854
    with dissolve
    j "Abandon your dreams and face the end. Let it all go-"
    scene ch1ep3p2_855
    with dissolve
    mc "-Perhaps then, someone might brave the world you've created out of selfishness."
    mc "Tell her that."
    scene ch1ep3p2_856
    with dissolve
    j "*chuckles softly*"
    cl "It's almost like I'm seeing a part of you in him lately."
    scene ch1ep3p2_857
    with dissolve
    j "I suppose he does carry some of my influence. After all, he asked me to deliver the same message I told her when I picked up that gift."
    cl "He's become your most intriguing creation, I suppose."
    scene ch1ep3p2_858
    with dissolve
    j "Hm, I'm not sure about that. My only desire is to see him thrive, with or without my influence."
    j "Ultimately, it's his life, his choices."
    scene ch1ep3p2_859
    with dissolve
    cl "..."
    j "You seem troubled. There is no point if you're going to stay silent."
    scene ch1ep3p2_860
    with dissolve
    cl "... This might sound strange, but I must say it."
    j "Go on."
    cl "Ever since I first met [mc], there's been this unsettling feeling. It intensifies every time we lock eyes."
    cl "I think Fang sensed it too, at some point. Maybe even far worse, or better...?"
    scene ch1ep3p2_861
    with dissolve
    j "Huh? It's not like you to talk nonsense."
    cl "How do I put this... It's sort of... a nagging sense of..."
    cl "Familiarity, perhaps?"
    scene ch1ep3p2_862
    with dissolve
    j "!!!"
    scene ch1ep3p2_863
    with dissolve
    cl "Are you sure this is a battle he should be fighting?"
    cl "The boy merely wants something simple, but he keeps ending up in these needless fights."
    scene ch1ep3p2_857
    with dissolve
    j "Call him, now."
    cl "Him, or...?"
    j "Yes, I want to see Aveline's twin once more. I need some answers."
    stop music fadeout 3
    play music2 'audio/SheWolf.mp3' fadein 3 loop
    scene ch1ep4_263
    with Dissolve(3.0)
    pause
    scene ch1ep3p2_865
    with dissolve
    jov "This is Jovian. Entry for April 12th, XXXX. It's [mc]'s second day in the hospital."
    scene ch1ep3p2_866
    with dissolve
    jov "The doctors... they've confirmed it. [mc], my little boy, just three years old, he's got a terminal brain tumor."
    jov "I couldn't... I couldn't just sit there and do nothing. So, I sought out Bonheur, a trusted friend, a brilliant mind, once known as a leading scientist."
    scene ch1ep3p2_867
    with dissolve
    jov "I pleaded with him, desperate for any cure, anything that could save [mc] from his cruel fate."
    scene ch1ep3p2_868
    with dissolve
    jov "And Bonheur... had something. A miracle drug, he called it. Claimed it could cure any illness."
    jov "But the cost... is being in debt to him, possibly for the rest of my life."
    jov "But what is debt compared to [mc]'s life? Even if he's not my blood, it doesn't matter. I love him like my own son."
    jov "I didn't hesitate, not for a second. I accepted it, all for [mc], to save him."
    scene ch1ep3p2_869
    with Dissolve(1.5)
    jov "This... this right here... is called the {i}\"Chimera Genesis Serum\"{/i}."
    jov "It seems this serum is... the future of warfare between the Glabia and Sha Crea territories."
    jov "In their longstanding conflict, Glabia plans to use it as a covert weapon."
    scene ch1ep4_291
    with dissolve
    jov "There, it's known by a rather cryptic name:"
    jov "... The {i}\"Numbers Serum\"{/i}." with Dissolve(2.0)
    scene ch1ep4_292
    with Dissolve(1.0)
    m "All the others were always created in pairs, like One and Two. My friends, Five and Six, then Seven and Eight."
    m "It always made me wonder... why was I the only one created alone? Why just me?"
    m "[mc]...you're...how..."
    play sound cinematicimpact
    show black
    pause
    stop music2 fadeout 2
    scene black
    with Dissolve(1.0)
    

    jump ch1ep4
label update04:
    scene c 1
    mc "*Opens the door*" with dis12
    show c 2
    mc ". . ." with dis
    show c 3 with dis17
    play music2b syndicate2 fadein 10
    stop music2 fadeout 10
    mc "W-What..." with dis
    mc "Uhh... h-hello young lady!"
    mc "(What the hell? This girl looks way too young to be on this server alone...)"
    girl "Are you [mc]?"
    mc ". . ."
    mc "...Y-Yes."
    girl "I have a letter for you."
    mc "W-What? For me?"
    girl "Yes."
    play soundlow paper
    show c 4
    mc "*Taking the letter* (How did this random kid know where I was? Only the girls in the next room knew I’d be here. Well, and Chang I guess.)" with dis12
    show c 4b
    mc "Did Chang send you here to prank me? What’s going on?"
    mc "There's not even a return address on the envelope. Just this strange... symbol."
    show c 5
    girl "It is a message from the Syndicate." with dis
    show c 6
    mc "The Syndicate?"
    mc "(That name sounds familiar... but I can't quite remember where I heard it.)"
    show c 5
    girl "No matter what, you must NOT open this envelope."
    girl "You cannot read it yet."
    show c 6
    mc "What? I thought you said this was a message for me."
    show c 5
    girl "It is. But you cannot read it until the proper time. Not yet."
    mc "And when am I supposed to...?"
    girl "Remember the symbol. It is pivotal."
    show c 4b
    mc "This one...?" with dis08
    girl "Yes."
    mc "Hmm..."
    show c 6
    mc "If I'm not supposed to open it, then why are you giving me this now?" with dis08
    mc "Why not just... send me the message when..."
    show c 5
    girl "Because it has to be now. Not sooner. Not later. Because we've seen it. Because we've already tried."
    mc "Um..."
    mc "You're being too cryptic... I'm not sure I'm following you."
    show c 4b
    girl "Don't open it. Don't read it. You will know when it is the proper time."with dis
    show c 4
    mc ". . ." with dis08
    mc "(This creepy girl... Did Chang and Luna decide to team up to prank me this time?)"
    show c 6
    mc "And tell me, where...?" with dissolve
    play sound risingshort3
    stop music2b fadeout 2
    play music2 rain3 fadein 2
    show c 7 with dis15
    mc "(What the fuck...)" with dissolve
    show c 8
    mc "(Damn, she's quieter than a mouse. I couldn’t even hear her footsteps running down the stairs.)" with dis08
    mc "(Man, what kind of parents let their daughter play Eternum all alone? Especially on a server like this...)"
    mc "(I thought this place would be safe, but after this... I'm not so sure anymore.)"
    play sound footsteps
    show c 9 with Dissolve(1.8)
    play sound chair2
    mc "*Sitting down* Hmm..." with dis08
    mc "(I wonder...)"
    mc "Hmm..."
    play soundlow thunder
    play sound chair1
    show c 9b
    a "SAY SOMETHING!!!" with hpunch
    a "I CAN'T STAND THIS SUSPENSE ANY LONGER!"with hpunch
    a "WHO WAS IT? ARE WE GONNA DIE?!" with hpunch
    a "ARE WE ALREADY DEAD?!" with hpunch
    show c 10
    mc "No, no! It was just... a little girl."
    scene bh 40
    x "A little girl was banging on the door like that...?"
    x "Was she Micaela's sister or something?"
    l "What did she want?"
    scene c 10
    mc "She gave me this letter."
    scene bh 35b
    d "A letter? What does it say?"
    scene bh 35b2
    mc "She asked me not to read it. Well, commanded me, really."
    scene bh 40
    x "Then why did she give it to you? That doesn't make any sense."
    scene c 10
    mc "I don't know, but she insisted that I not read it yet."
    scene bh 40
    l "Maybe you shouldn't, then..."
    x "Why not? What could happen?"
    scene c 9b
    a "Don't read it! What if a spooky ghost starts chasing you because of it?!"
    scene c 9
    mc "Hmm..."with dis08
    menu:
        with dis
        "Open the letter":
            $ letteropen = True
            show c 10
            mc "Bah, to hell with it." with dissolve
            mc "Let's see what this is all about."
            play sound paper
            show c 10b
            mc "*Opens the letter* Alright..." with dis
            mc "It's... just a piece of paper with a single line written on it."
            mc "It says..."
            mc "*Reading slowly* {i}Askion kataskion lix tetrax damnameneus aision."
            mc "What the hell does that mean?"
            mc "Has anyone ever heard anything like this gibberish before?"
            scene bh 25
            no "I don't know what that was, but it sounded like some kind of code. Maybe it's the beginning of another one of Ulysses' events!"
            scene c 10b
        "[gr]Don't open the letter":
            show c 10
            mc "Bah, we don't have time for this."with dissolve
            mc "And... I don't know, I really feel like I shouldn't open it. The little girl was insistent."
            scene bh 25
            no "Maybe it's the beginning of another one of Ulysses' events! It wouldn't be the first time I've started a quest with something creepy like this."
            scene c 10
    mc "Yeah, maybe..."
    play sound2 paper
    scene bh 33
    mc "Anyway, let's get back to the issue at hand, girls!"with dis
    mc "We have a Gem of Doom to steal!"
    mc "And we have less than 2 hours to learn each step of the plan!"
    scene bh 21
    mc "As soon as the heist begins, at 9:00 PM, we’ll have exactly 60 minutes to steal the Gem AND leave the server – not a minute more."with dis08
    scene bh 35b
    d "What if we run into setbacks? Heists always have little obstacles and hiccups."
    scene bh 35b2
    mc "There can't be any. Everything has to be perfect. It NEEDS to be."
    mc "Chang’s plan is airtight. You’ll see. He’s assured me that if everyone sticks to the plan, everything will be fine."
    mc "And hey, call me an optimist, but I think so too."
    scene bh 35b
    d "You sure?"
    scene bh 37
    mc "Trust me, by 10:00 PM we'll all be sitting in a lounge, having a toast to a wonderful, successful, and beautifully executed heist."with dis08
    mc "We'll pull this off without a hitch!"
    mc "What could possibly go wrong?"
    d "If you say so..."
    mc "Ladies..."
    mc "The Gem Heist...{w} starts... {w}now."
    play sound ding
    hide screen heart
    stop music2
    scene black
    pause
    play music vent fadein 4
    show screen time0940 with dis12
    pause
    hide screen time0940 with dis08
    mc "Hmmm..." with dis08
    mc "(F-Fuck, that hurts...)"
    play sound clothes2
    play sound2 earringing
    play sound3 footsteps
    scene white
    blank "{i}Someone removes a bag from over your head." with dis12
    show screen heart
    scene c 11
    with dis17
    pause
    aaa "Time to wake up, sleepyhead." with dis08
    show c 12
    mc "Hmm...?" with dis12
    mc "(Motherfuckers... They beat me up...)"
    play sound zippo
    aaa "*Lighting up a cigar* You know..."with dis
    scene blurv31
    aaa "...of all the times someone attempted to rob me..."with dis
    scene c 13
    mc "(Where am I...?)" with dis
    cgar "...this was definitely the worst."
    cgar "It was pathetic, even. I guess this is what happens when you let kids into a server like mine. They think they're in a movie and come to fuck around."
    cgar "A fucking pain in the ass."
    scene c 14
    cgar "Now... save me some time and tell me how many of you there are, and why you tried to rob me." with dis
    scene c 16
    mc "Fuck you. I'm not telling you shit."
    show c 15
    cgar "*Chuckles* So cocky. You remind me of myself when I was young."
    show c 14
    cgar "You're gonna tell me what I want, boy. Whether you like it or not." with dis08
    cgar "Do you think we don't know how to make you talk?"
    cgar "Do you believe I give a single fuck about \"Eternum's General Code of Ethics\"?"
    cgar "I don't. And neither does Ulysses. They are aware of what happens under the radar on every server, and yet... they do NOTHING to stop it."
    cgar "That’s why Eternum is better than the real world, boy."
    cgar "Here, we don't have to fear censorship or punishment. Here, we're not restrained by petty morality or frivolous legality. Here, there’s only one rule: the big fish eat the little ones."
    cgar "And soon, when I gather all 10 Gems... I'll be its King."
    scene c 16
    mc "What a great speech. Tell me, how much time have you spent practicing monologuing in front of a mirror?"
    show c 15
    cgar "*Chuckles*"
    show c 14
    cgar "You're gonna tell me your name. You’re gonna tell me the name of every single person that came with you. And you're gonna tell me why you tried to rob me with the most boneheaded plan I’ve ever seen." with dis08
    cgar "What was the idea? Poisoning my son to distract me while you tried to assault the bank?"
    cgar "How were you planning to get past the cameras? The magic blockers? The hundreds of armed guards I have stationed all over the place?"
    show c 12
    mc ". . ."
    show c 15
    cgar "*Chuckles* I'll take your silence as your answer."
    cgar "You thought you'd got it all worked out, didn't you? And now you're wondering how you got stuck down here."
    show c 14
    cgar "After you give me their identities, I'll make sure I turn all of your lives, both here and in the real world, into a living hell." with dis08
    cgar "Every last one of you..."
    play sound chain
    show c 17
    mc "I won't tell you anything, and you're not gonna touch a single hair on any of their heads!" with hpunch
    show c 15
    cgar "\"Their heads\", huh?"
    cgar "So there's definitely a group of people..."
    show c 12
    mc ". . ."
    show c 15
    cgar "*Laughs* Come on, surrender their identities, and I'll try to be merciful. I can promise you that."
    show c 12
    mc ". . ."
    show c 15
    cgar "I know that face. I've seen it before."
    show c 12
    cgar "You're mentally reviewing your pitiful plan, aren't you?"
    show c 12b
    cgar "Running through it, step-by-step from the very beginning, to figure out where things went wrong... am I right?" with dis12
    play soundlow risingshort4
    mc ". . . .{w=2.2}{nw}" with dis2
    stop soundlow
    play sound ding
    stop music
    scene black
    pause
    play music2 heist2 fadein 6
    show screen time0855 with dis15
    pause
    scene c 18
    hide screen time0855
    with dis2
    pause
    play sound mouse
    cash "(God, this is so boring. Nothing cool ever happens here...)" with dissolve
    cash "(But well... at least the pay is good.)"
    play sound3 mouse
    scene c 19 with dis
    play sound4 mouse
    cash "*Yawns* (Definitely better than my last job in the real world.)" with dissolve
    cash "(But maybe I should start training and become a bounty hunter in one of those fantasy servers, like...)"
    mc "SLACKING OFF DURING WORKING HOURS?!" with hpunch
    play soundlow slam
    play sound2 mouse
    show c 20 with hpunch
    play sound3 mouse
    pause .3
    play sound4 mouse
    pause .25
    cash "I'M N-NOT!" with dissolve
    cash "I'm c-checking the bets at the roulette tables!"
    cash "I'm sorry Mr. Garrington, please don't fire me!"
    show c 21
    cash "What...?" with dis
    cash "Oh... I-I'm sorry, I got confused. Welcome to Garrington's Casino, sir!"
    play sound metalhit
    show snatch1
    pause
    play sound2 ding
    scene snatch1b
    cash "How may I help you today?"
    scene c 22
    mc "I'm sorry for my little joke. It's just that I'm very happy today!" with dissolve
    mc "I just got married!"
    show c 21
    cash "Oh wow, congratulations!" with dissolve
    play sound clothes2
    $ unlock_look("nova", 5)
    show c 23
    no "And I'm the lucky bride!" with dissolve
    play sound metalhit
    show snatch2
    pause
    play sound2 ding
    scene snatch2b
    no "I'm sorry girls, he's off the menu!"
    cash "Congratulations!"
    show c 39
    cash "And thank you for choosing Garrington's Casino."
    cash "Might I ask your name, age, and the reason for your visit?"
    show c 25
    no "Nina T. Riley. I'm 20."
    show c 24
    mc "Yanis Sharp, also 20. We're mostly coming to see the performances and have a couple of drinks, but I might also try my luck at a slot machine." with dissolve
    show c 39
    cash "Wow, you guys are so young!"
    show c 25
    no "Why should I wait when I know I've found the right man?!"
    show c 24
    mc "Yeah..." with dissolve
    menu:
        with dis
        "Far-fetched story":
            mc "I'm the son of an Arabian Prince. My father didn't approve of Nina, so we straddled two camels and ran off together across the desert."with dissolve
            mc "As soon as we arrived in Switzerland, we logged into Eternum and headed to the New Vegas server to get married."
            show c 39
            cash "*Awkward chuckle* Uhh... Yeah, of course!"
            cash "May I see your IDs, please?"
        "Credible story":
            mc "Nina and I have been friends since we were 4 years old."with dissolve
            mc "When we were 15, we started dating – and I immediately knew I’d marry this lady one day."
            mc "So a year ago, I proposed to her, and she said yes! Now I'm the happiest man on earth!"
            show c 39
            cash "That's lovely! I'm so happy for you guys."
            cash "I wish you luck in the casino. May I see your IDs, please?"
        "Stay close to reality [nova_pts]" if novapath:
            mc "I'd been living in another country all my life, but recently I moved to Nina's town." with dissolve
            mc "I'll tell you what, it was love at first sight."
            mc "The moment I first laid eyes on her, I knew I was going to marry Nov- \n...eh, Nina one day."
            $ nova_points += 1
            play sound "beat.ogg"
            show screen heartbeat
            show c 26
            mc "Her hair, her freckles, her flamboyance, her energy... I fell in love with all of it." with dissolve
            mc "Then we went to the New Vegas server and, on an impulse... we got married!"
            mc "Best decision of my life. By far."
            show c 27
            cash "I'm so happy for you guys!"with dissolve
            cash "And I wish you luck in the casino. May I see your IDs, please?"
            no ". . ."
            cash "Guys?"
            mc "*Clears throat*"
            show c 25
            no "Oh... OH! Sorry! I got distracted looking at my... husband." with dissolve
            no "What is it?"
            cash "Your IDs."
    show c 25
    no "Oh, sure! I have them right here!"
    show c 28
    p "EXCUSE MEEEEE?!" with dis08
    sec2 "Please, ma'am, don't shout..."
    show c 29
    p "Don’t you know who I am?!" with dis
    sec2 "Hmmm..."
    p "I can't believe it!"
    $ unlock_look("penelope", 8)
    show c 30
    p "I'm out of here." with dis08
    play sound metalhit
    show snatch3
    pause
    play sound2 ding
    scene snatch3b
    p "Ugh, I'm going to ruin this place with a single tweet after tonight."
    show c 31
    sec2 "I'm sorry, but I can't let you into the VIP area without a VIP pass." with dis08
    show c 32
    p "This is the first time I've been forced into a situation like this. I’ve never experienced such incompetence!"
    show c 33
    p "What am I supposed to do? Stay in the poor people area? And sit on these filthy stools?"with dis
    p "Over my dead body."
    p "*Gagging* Ughhh, even the carpet is sticky..."
    show c 31
    sec2 "If you have a second, I can ask the Head Security office."
    show c 32
    p "Really? Oh my gosh, this is SO humiliating. I’m sure YOU’RE used to it, but for someone like me, this is absolutely EMBARRASSING."
    p "*Sighs* You have exactly 1 minute. That’s as long as it’ll take me to draft up this 140-character review on the security at Garrington’s Casino."
    play sound beep2
    show c 34
    sec2 "Lisa? Do you hear me? I have a problem at access gate 6A of the VIP area." with dis08
    play sound hangup
    show c 35
    cash "Yeah, I can see you from here, Akim." with dis08
    cash "The entire floor is looking at you right now. The last bouncer that caused a fuss was fired, do you remember?"
    play soundlow glitch1
    show garglit
    sec2 "I know, I know! Look, this girl says she's famous or something. She said her name is... \"Miss Venus.\" Can you check that real quickly, please?"
    cash "*Sighs* Yeah, give me a minute."
    scene c 25
    cash "I'm sorry guys, we're having a little issue at the VIP area. It'll only be a moment."with dis
    no "No problem! Today, nothing can ruin my mood!"
    cash "Thank you for your understanding."
    play sound type2
    show c 37
    cash "Okay..." with dis
    cash "Miss Venus... ah yeah, she's here, Miss Karen Venus. More than 3.8 million followers on Twitch."
    cash "Four million followers on Instagram. She even has a Wikipedia page! Come on Akim, you're supposed to know these things."
    sec2 "You didn't know either!"
    cash "Yeah, but I'm not the doorman for the VIP area."
    stop sound
    show c 34
    sec2 "Okay, okay, thank you Lisa."
    play sound beep2
    show c 31
    sec2 "I'm so sorry for the misunderstanding, ma'am." with dis08
    sec2 "You can pass through now."
    show c 38
    p "Hmph. It's about time."
    p "You’d better hope that the performances at the VIP area are as good as people say, so that I forget about your ineptitude here."
    show c 31
    sec2 "Please enjoy your stay at Garrington's...  {w}*muttering* {size=25}bitch."
    show c 39
    cash "Alright guys, everything seems to be in order." with dis
    cash "Sorry for the wait, we ask that all of our members show their IDs as a security measure."
    show c 23
    no "Of course! That makes sense!"
    no "Thank you very much!"
    cash "Have fun and welcome to Garrington's!"
    play sound type2
    show c 18 with dis15
    cash "(This girl is getting married in her twenties, while I'm still single and almost 34.)" with dissolve
    cash "(Why is life so unfair...)"
    ca "Wondrous..."
    stop sound
    show c 39
    cash "Welcome to Garrington's Casino, ma'am! How may I help you today?" with dis08
    show c 40
    ca "If what Mercury said is true, you cannot use magic in this place, and yet you managed to create small balls of light that never extinguish."
    ca "Astonishing..."
    show c 41
    cash "Um..."with dis04
    play sound metalhit
    show snatch4
    pause
    play sound2 ding
    scene snatch4b
    cash "What...?"
    show c 40
    ca "The lights..."
    show c 41
    cash "Yeah..."
    cash "Magic is disabled in all the casino and hotel areas to prevent clients from cheating, if that's what you mean."
    cash "Um... Might I ask your name, age, and the reason for your visit, please...?"
    show c 42
    ca "Ah, yes." with dis08
    ca "My name is... {i}Carrie..."
    ca "I have come to exchange my currency for tokens of the same value in order to gamble on games of chance."
    ca "All in the hope of obtaining more tokens so I can exchange them again into my initial currency on my way back."
    show c 43
    cash "Erm..."
    cash "I'll type in \"gambling\"..."
    cash "Age?"
    show c 42
    ca "Eighty-four."
    show c 43
    cash ". . ."
    cash "(Why do I always get stuck with the weirdos?)"
    cash "*Sighs* Can I see your ID, ma'am?"
    show c 42
    ca "Of course."
    play sound type1
    show c 44
    cash "Okay... everything seems to be in order." with dis
    cash "Thank you and welcome to Garrington's Casino... {i}Carrie Morgan from Pennsylvania, 27."
    show c 42
    ca "Thank you."with dis08
    play sound2 type2
    show c 18
    cash "(God, this place is in serious decline.)" with dis
    cash "(If I had an eternal for every time someone...)"
    stop sound2
    show c 42
    ca "Excuse me, is there a meditation area? Somewhere quiet where I can concentrate." with dis08
    ca "If it is reserved for royalty, that is preferable, obviously."
    show c 43
    cash ". . ."
    stop music2
    play sound3 ding
    show black
    show screen time0909
    pause
    play music2 heist3
    scene c 45
    hide screen time0909
    with dis17
    no "Alright, if my info was correct, this is the floor where Bobbie likes to drink his scotch." with dis08
    no "He should be here anytime now. When you start playing, remember to go all-in on the third hand!"
    if novapath:
        menu:
            with dis
            "Grab her by the shoulder [nova_pts]":
                $ nhm4 = True
                $ nova_points += 1
                play sound "beat.ogg"
                show screen heartbeat
                show c 47
            "Focus on the mission":
                show c 46
    else:
        show c 46
    mc "Very well. I guess we need to try to go unnoticed until then." with dis
    mc "Go to the recreation room and make sure the dealer isn't here yet."
    mc "I'll stick around and kill some time ‘til Bobbie appears."
    if nhm4:
        mc "Join me when I sit down next to him, my dear wife."
        no "Yes! I will keep a low profile until then... my darling husband."
    else:
        show c 45
        no "Smart! Let's do it!" with dissolve
    show c 48
    mc "Hmmm..." with dis12
    show c 49
    mc "(There are cameras everywhere.)"
    mc "(They have no reason to be suspicious of us, but it'll be better if I pretend that I'm playing.)"
    show c 50
    mc "(Bobbie still hasn't come down anyway.)"
    mc "(I hope he appears soon, though... or else our entire plan will be ruined.)"
    show c 51 with dis
    mc "(I'll act like I'm playing the slot machines in the meantime.)"with dissolve
    scene rou 1 with dis12
    play sound chair4
    show screen eternals
    mc "*Sitting down* (Okay, how does this thing work...)" with dis08
    $ initialmoney = money
    $ money -= 10
    play sound slotsound
    show slotrotate
    pause 1.52
    scene rou 2
    pause .3
    mc "(Holy shit, 10 eternals per spin?! What a rip-off.)" with dis08
    $ money -= 10
    play sound slotsound
    show slotrotate
    pause 1.52
    scene rou 10
    pause .1
    play soundlow slotwin
    $ money += 6
    pause .06
    $ money += 7
    pause .06
    $ money += 7
    pause .06
    pause .15
    mc "(Hey! I won 20 eternals! Not bad.)" with dissolve
    mod "There's a cheat option afterward if you want to skip or have bad luck."
    call screen slotmenu with dis12
label slotplaylabel:
    $ money -= 10
    $ rng = renpy.random.randint (1, 40)
    play sound slotsound
    show slotrotate
    pause 1.52
    if rng == 1:
        scene rou 11
        play sound2 slotjackpot
        pause .1
        $ money += 10
        pause .06
        $ money += 10
        pause .06
        $ money += 10
        pause .06
        $ money += 10
        pause .06
        $ money += 10
        pause .06
        $ money += 10
        pause .06
        $ money += 10
        pause .06
        $ money += 10
        pause .06
        $ money += 10
        pause .06
        $ money += 10
        pause .06
        $ money += 10
        pause .06
        $ money += 10
        pause .06
        $ money += 10
        pause .06
        $ money += 10
        pause .06
        $ money += 10
        pause .06
        scene rou 12
        mc "Jackpot!" with dis
        show rou 11
        mc "My luck is changing!" with dis
    elif rng <= 3:
        scene rou 9
        pause .1
        play soundlow slotwin
        $ money += 10
        pause .06
        $ money += 10
        pause .06
        $ money += 10
        pause .06
    elif rng <= 7:
        scene rou 10
        pause .1
        play soundlow slotwin
        $ money += 6
        pause .06
        $ money += 7
        pause .06
        $ money += 7
        pause .06
    elif rng <= 13:
        scene rou 8
        pause .1
        play soundlow slotwin
        $ money += 3
        pause .06
        $ money += 3
        pause .06
        $ money += 4
        pause .06
    elif rng <= 17:
        scene rou 1
        pause .2
    elif rng <= 21:
        scene rou 2
        pause .2
    elif rng <= 25:
        scene rou 4
        pause .2
    elif rng <= 29:
        scene rou 5
        pause .2
    elif rng <= 34:
        scene rou 6
        pause .2
    else:
        scene rou 7
        pause .2
    if money <= 470:
        jump slotleavelabel
    if money >= 1900:
        jump slotleavelabel
    call screen slotmenu with dis04

label slotleavelabel:
    mc "(Okay, that's enough.)" with dissolve
    menu:
        mod "Wanna be a dirty cheater and have 2000 eternals?"
        "Hell yes":
            play sound coins
            $ money += 1000
            pause .2
            $ money += 1000
            pause .2
            $ money += 1000
            pause .2
            play sound coins
            $ money += 1000
            pause .2
            $ money += 1000
            pause .2
            $ money += 1000
            pause .2
            mod "Just kidding, you don't need that much..."
            $ money = 2000
        "Hell no":
            pass
    if money >= initialmoney:
        if money == initialmoney:
            mc "(At least I didn't lose any money. A withdrawal time is a victory, they say.)"
        else:
            mc "(I'm leaving with more money than I came in with. I see this as a resounding victory!)"
        $ moneywonsomething = True
    else:
        mc "(I think I've lost enough money already...)"
    hide screen eternals
    scene c 52
    mc "(Hmm...)" with dis12
    mc "(Oh shit, that's our man!)"
    mc "(It's showtime.)"
    play sound chair1
    show c 53
    mc "Ahhh, man! Can't wait to play some poker!"with dis12
    mc "Roulette, blackjack, slot machines... all that shit depends on chance, but not this!"
    show c 54
    bobb "If you want to play hold'em, you'll have to go to the third floor or wait another 20 minutes." with dis
    show c 55
    mc "Oh really? My wife told me I could play poker games at this table."with dis04
    show c 54
    bobb "You can, but there's only one game every 3 hours."with dis04
    bobb "Personally, I like to come early to save my seat and get a whiskey."
    show c 55
    mc "Oh, I see. Thanks for letting me know."with dis04
    show c 54
    bobb "Also, did you say \"my wife\"? Aren't you a little too young for that?"with dis04
    show c 55
    mc "I look much younger than I really am."with dis04
    mc "Also, she..."
    play sound chair1
    show c 56
    no "Hello honey!" with dissolve
    mc "Hey sweetheart."
    no "Are you gonna play poker?"
    mc "Not yet, this gentleman told me that the game doesn't start until 9:30 PM."
    show c 57
    bobb "You know, maybe we could ask one of the workers here to deal a quick game for us."
    bobb "If it’s me asking, they'll do it. I have certain... VIP privileges."
    show c 58
    mc "Damn, really? You have a VIP pass? What are you doing here, then?"
    show c 72
    bobb "I like to play with the... normal people. They're a bit easier to... *clears throat* interact with."
    show c 58
    mc "That makes sense. But would they really waste a dealer on just the two of us?"
    show c 72
    bobb "As I said, they will if I'm the one who asks."
    bobb "Watch this."
    play sound whistleloud
    $ unlock_look("luna", 5)
    show c 73
    bobb "*Whistling* HEY! Dealer, come here." with dis
    l "How may I help you, sir?"
    play sound metalhit
    show snatch5
    pause
    play sound2 ding
    scene snatch5b
    bobb "*Showing his VIP card* I'm Bobbie Briggs, you'll deal a quick hold'em game for us, right sweetie?"
    bobb "It's just me and..."
    show c 58
    mc "Yanis Sharp."
    show c 73
    l "Of course, sir."
    bobb "That's what I thought..."
    play sound chair4
    show c 76 with dis08
    play sound2 shuffle
    show c 75
    l "*Shuffling the cards* How much do you want the big blind to be, gentlemen?" with dis08
    play sound3 shuffle
    show c 76
    l "*Shuffling the cards* 100 eternals?" with dis08
    show c 57
    bobb "100 eternals is fine by me. You?"
    show c 58
    mc "Sure, that sounds good."
    play sound shuffle
    show c 77
    l "Mr. Sharp will start as the big blind." with dis
    play sound2 dealcard
    show c 79
    l "*Dealing the cards* Good luck." with dis08
    show screen eternals
    show c 59
    with dis12
    play sound coins
    $ money -= 33
    pause .05
    $ money -= 33
    pause .05
    $ money -= 34
    pause .05
    pause
    show c 63 with dis
    pause
    show c 64
    bobb "I raise. 150 eternals." with dissolve
    show c 61
    mc "Uhh... I fold."
    show c 57
    bobb "Seriously? Are you one of those pussy players, kid? I don't have all day, you know."
    play sound shuffle
    show c 77
    l "Mr. Briggs has won the round." with dis
    play sound2 dealcard
    show c 78
    l "*Dealing the cards* Now Mr. Briggs is the big blind." with dis08
    $ money -= 100
    play sound coins
    show c 59 with dis08
    pause
    show c 64
    bobb "I raise. 50 eternals." with dissolve
    $ money -= 50
    play sound coins
    show c 60
    mc "I call." with dis08
    play sound2 dealcard
    show c 77
    l "A 3 on the river."with dis08
    show c 64
    bobb "I raise 80 eternals." with dis08
    $ money -= 80
    play sound coins
    show c 60
    mc "I call!" with dis08
    show c 80b
    l "Flush against a pair of queens. Mr. Briggs wins again." with dis12
    show c 72
    bobb "*Laughs* Just a pair? That was a sad move."with dis08
    show c 61
    mc "Dammit..."
    no "Are you sure you know how to play this?"
    show c 62
    mc "Just a few bad draws. Stop worrying so much, Nina." with dissolve
    play sound shuffle
    show c 77
    l "Third round." with dis
    play sound2 dealcard
    show c 78
    l "*Dealing the cards* Mr. Sharp is the big blind now. Place your bets, gentlemen." with dis08
    $ money -= 100
    play sound coins
    show c 59 with dis08
    pause
    show c 63
    bobb ". . ."with dis08
    show c 72
    bobb "I'm only getting good cards today. You have magic hands, cutie."with dis08
    show c 76
    l "Thank you."
    if lunapath:
        mc "(Heh, you'd be surprised...)"
    show c 72
    bobb "I raise. 30 eternals."
    $ money -= 30
    play sound coins
    show c 60
    mc "I call!" with dis08
    play sound2 dealcard
    show c 80
    l "*Showing the flop* Make your bets." with dis
    show c 63 with dis08
    pause
    show c 64
    bobb "I raise. 1500 eternals."with dis04
    show c 58
    mc "W-What? 1500?! I can't risk that large an amount."
    show c 57
    bobb "Seriously? Well, I guess I've won then."
    bobb "That was a quick game."
    show c 58
    mc "Wait! I wanna raise your bet!"
    show c 57
    bobb "And I wanna be the king of Eternum. You have no money, you're out. That's how it works, kid."
    show c 58
    mc "I can offer something else! What do you want?"
    show c 57
    bobb "You have nothing that interests me."
    show c 65
    mc "What about my wife?"
    mc "I'll bet one night with her."
    show c 66
    no "Excuse me, what the fuck?"with dis08
    show c 67
    mc "Come on, honey... don’t be such a pussy! You have nothing to fear. I'm gonna win this hand, I'm 100\% positive. Statistically speaking, I’m due a good hand."
    show c 66
    no "That’s not how statistics work! We've been married for less than 6 hours and you're already gambling with ME?!"
    show c 67
    mc "But I'm gonna win! Don't worry!"
    play sound chair2
    show c 68
    no "Fuck you!"with dis08
    mc "Babe! Don't get mad!"
    no "You're fucking hopeless... I should have listened to my mom."
    mc "Do you agree, then?"
    no "Do whatever you want, asshole."
    show c 69
    mc "What do you say, Bobbie? Do we have a deal?" with dis08
    show c 70
    bobb ". . ."
    show c 71
    mc "Come on Nina, turn around. You're gonna miss my victory!"
    no "I said FUCK YOU!"
    show c 72
    bobb "Yeah, I'll accept your... wager."
    show c 69
    mc "Are you gonna bet more, then?"
    mc "I'd say my wife is worth more than just 1500 eternals."
    no "*Muttering under her breath* You're damn right I'm worth more than 1500 eternals, prick."
    show c 57
    bobb "I don't have any more cash on hand. I'd have to go all the way up to the cashier, and the line could take an hour."
    show c 69
    mc "What about that VIP pass you showed before? I've always wanted to go there."
    show c 72
    bobb "The VIP pass? Yeah, sure, if that’s what you want."
    show c 80
    bobb "Alright, here you go." with dis
    play sound card
    show c 81
    bobb "1630 eternals and a VIP pass." with dis08
    bobb "All in."
    play sound2 card
    show c 82
    bobb "And I’ve got a full house, aces and kings." with dis08
    mc "Oh shit..."
    mc "I may have made a huge mistake..."
    play sound3 card
    show c 83
    mc "I’ve got a pair of deuces..." with dis08
    bobb "Hahaha! Goddammit boy, you shouldn't have come here if you didn’t know how to play."
    play sound shuffle
    show c 76
    l "Alright gentlemen, let's see the last two cards."with dis08
    show c 83
    bobb "*Laughs* Yeah, let's follow the protocol." with dis08
    play sound dealcard
    show c 84
    l "A deuce on the turn." with dis08
    play sound2 dealcard
    show c 85
    l "And another deuce on the river." with dis08
    l "Four of a kind. Mr. Sharp wins the hand."
    show c 86 with dis
    bobb ". . ." with dis
    play sound musicstop
    stop music2
    show c 87
    bobb "Wait, what?!" with hpunch
    bobb "WHAT?!"with hpunch
    play music2 heist4
    show c 56 with dis
    play sound coins
    $ money += 500
    pause .05
    $ money += 550
    pause .05
    $ money += 580
    pause .05
    no "Well played, darling!" with dissolve
    mc "It was easy. You see, poker's not about playing the odds... it's about playing the man."
    no "I never doubted you."
    mc "Well, we have to leave now, thanks for playing with me, Mr. Briggs."
    play sound2 chair2
    hide screen eternals
    show c 73
    l "Yes, I need to leave too. My shift's over." with dis08
    l "Thank you for choosing Garrington's Casino."
    show c 87
    bobb ". . ." with dis
    bobb "But..."
    bobb "The odds..."
    show c 88
    deal "Good to see you again, Mr. Briggs." with dis
    deal "I'll be the dealer for the hold'em game tonight."
    show c 89
    bobb "What...?" with dis
    bobb "What about the girl with the black hair?"
    deal "Who?"
    bobb "Black hair, red eyes... She was very young."
    deal "I don't think there's anyone who looks like that working here tonight."
    bobb ". . ."
    stop music2
    play sound ding
    scene black
    show screen time0920
    pause
    play music2 heist3
    hide screen time0920
    show bankmove
    with dis2
    pause 4.6
    scene c 90 with Dissolve(.7)
    pause
    show c 91
    n "Good evening." with dis08
    $ unlock_look("nancy", 5)
    show c 92
    be "Good evening, ma'am." with dis
    play sound metalhit
    show snatch6
    pause
    play sound2 ding
    scene snatch6b
    be "How may I help you?"
    show c 93
    n "I am Katarina Vasiliev. I'm here for the delivery."with dissolve
    show c 92
    be "The delivery...?"with dissolve
    show c 93
    n "*Sighs* Can I speak with your supervisor? I don’t have time to waste – I’m in a rush."with dissolve
    show c 98
    be "Actually... I'm in charge today."
    show c 94
    n "Seriously? Then you should have known that I had an appointment."
    show c 98
    be "Uhh... Could you please remind me of the reason for your visit?"
    show c 94
    n "I've come on behalf of Ivan Antonov, CEO of Flex Energy Systems."
    n "We need to secure an artifact of the utmost importance. Mr. Garrington himself assured us that this was the most secure vault in all of Eternum."
    show c 98
    be "And it is, ma'am."
    be "What is this artifact?"
    play sound chair2
    show c 95
    n "This briefcase." with dis
    n "Its content is strictly confidential, so I must take it to the designated vault myself."
    show c 98
    be "I can assure you our workers are completely trustworthy. They're under constant surveillance."
    show c 97
    n "If they were completely trustworthy, there would be no need to keep them under constant surveillance, would there? Besides, Mr. Antonov insisted that no one touch the briefcase but me."
    n "And Garrington agreed. He claimed that everything would be arranged by the time I arrived."
    show c 96
    n "*Sighs* You know what, it's probably better to just forget about it. Coming here was a mistake." with dis08
    n "I knew we should have chosen Blibinar's Bank."
    show c 98
    be "No, no! Please ma'am, just give me a minute to confirm your appointment."
    be "It's a simple security measure."
    show c 96
    n "*Sighs* Okay, fine... but hurry up."
    show c 99
    be "It'll only be a second..." with dis
    play sound w1
    play sound2 beep2
    show c 100
    sec1 "Control room, Security Chief Mendez speaking." with pushl
    play sound2 w1
    show c 99
    be "Hi... I'm here with Ms. Vasiliev. She needs to stash an extremely valuable briefcase in the vault, and claims to have arranged everything with Mr. Garrington." with pushr
    be "Can you confirm that her appointment was scheduled?"
    play sound w1
    show c 100
    sec1 "Yes, we'll check the logs."with pushl
    show c 101
    sec1 "Camille, can you check if a delivery to the main vault by \"Ms. Vasiliev\" was scheduled for today?" with Dissolve(.6)
    show c 102
    sec1 "Anything else?" with dis
    play sound2 w1
    show c 99
    be "No, that's all for now." with pushr
    be "Have there been any incidents today?"
    play sound w1
    play sound2 knockdown
    show c 102
    sec1 "No sir. Everything's been running smoothly."with pushl
    show c 103
    sec1 "Cameras are on, the main vault's internal temperature and humidity remain stable, and all men are in their scheduled positions."with dis
    play sound w1
    play sound2 knockdown
    show c 99
    be "Alright, good."with pushr
    be "What about the appointment? Is everything okay?"
    sec1 ". . ."
    be "Mendez? Are you there?"
    play sound chairoffice
    sec1 "Yes, sorry." with dis08
    sec1 "Uhh... Ms. Vasiliev, yeah, she's here."
    play sound w1
    $ unlock_look("dalia", 7)
    show c 104
    d "The documents were misfiled, so that's probably why they didn't get to you in time." with pushl
    play sound metalhit
    show snatch7
    pause
    play sound2 ding
    scene snatch7b
    d "I'm so sorry for the inconvenience."
    d "Mr. Garrington pointed out that this was a very special client."
    play sound w1
    show c 99
    be "Understood. Thank you." with pushr
    play sound2 beep2
    show c 98
    be "All set, Ms. Vasiliev." with dis08
    be "Please accompany me to the vault. You may come around to the door on your left."
    show c 97
    n "It’s about time..."
    play sound w1
    show c 106
    d "Alright, I have visuals of every single room of both the bank and casino."with pushu
    show c 105
    d "Are the micro-auriculars working? Can you hear me, Saturn?"
    d "If you can, say: \"This place looks worryingly unprotected.\""
    play sound w1
    show c 108
    n "This place looks worryingly unprotected."with pushd
    d "*Giggles* Nice!"
    n "I'm not sure it's safe enough for us."
    show c 107
    be "It's the safest place in all of Eternum, ma'am. I assure you." with dis08
    be "The vault is located 7 floors below ground level, and there are armed guards on every floor."
    be "Even if something ever happened, the security system would block all possible exits. And, since there are no Exit Portals inside the bank, it'd be impossible to escape with any stolen loot."
    show c 108
    n "And what if someone managed to take all the money without being noticed?"with dis08
    show c 107
    be "Every eternal we have in physical format has a unique tracking number assigned, so the thief could be easily tracked."with dis08
    be "Also, all personal belongings, such as your briefcase, are locked inside of an individual safe-deposit box. Each panel has its own combination, allowing for a double layer of security."
    be "Even Mr. Garrington himself stores his most valuable items inside our vault. That should be enough of an endorsement."
    show c 108
    n "And what's your defense against magic?" with dis08
    show c 107
    be "The main vault has a magic blocker that is operational 24 hours a day." with dis08
    be "Also, all clients must pass through 3 different gate controls. Each gate detects the usage of any magical trickery or similar subterfuge, like invisibility or Polyjuice potion."
    show c 108
    n "I see... I hope that's enough."with dis08
    n "Alright, let's go down to the vault."
    show c 107
    be "Follow me!" with dis08
    stop music2
    play sound ding
    scene black
    show screen time0930
    pause
    play music2 heist4
    hide screen time0930
    show c 109
    with dis2
    p "*Giggles* Seriously?" with dissolve
    bgar "I tell no lies."
    show c 110
    bgar "Obviously, I fired him. I think he's cleaning toilets in Ion now."with dis12
    bgar "But anyway, I feel like I've been talking about myself for hours."
    show c 112
    bgar "What about you, babe? How's the influencer life?" with dis12
    show pbhm04f
    p "Oh well, you know... nothing extraordinary about it."with dis
    p "Playing video games, streaming on Twitch, interacting with fans. The same thing every day."
    p "It gets a little repetitive. Your life seems much more... interesting."
    scene c 112
    bgar "*Chuckles* You've seen nothing yet." with dis08
    bgar "Maybe we can continue this conversation in my private suite... in my hotel..."
    show pbhm04f
    p "*Giggles* Wow, you have a hotel too? Amazing."with dis
    p "Your offer sounds really great... just let me finish my drink, and we can head upstairs..."
    scene c 112
    bgar "Yeah, you can follow me up the stairs to the hotel overlooking the casino. Both me and my father have suites." with dis08
    show pbhm04f
    p "I'll try not to take too long then..." with dis08
    if penelopepath:
        menu:
            with dis
            "[gr]Sit between them":
                $ sitbet = True
                scene c 115
                mc "Excuse me, sorry, my bad, I’ve got to..." with dis12
                play sound chair1
                show c 116
                mc "Ahh! Finally!" with dis
                $ penelope_points += 1
                play sound2 "beat.ogg"
                show screen heartbeat
                show c 117
                bgar "What the hell, dude? We were in the middle of a conversation." with dissolve
                show c 116
            "Sit on the other sofa":
                $ sitbet = False
                play sound chair1
                scene c 119
                mc "Ahh! Finally! Nice to meet you!" with dis
                show c 121
                bgar "Are you talking to me? Who the fuck are you?"
                show c 119
    else:
        $ sitbet = False
        play sound chair1
        scene c 119
        mc "Ahh! Finally! Nice to meet you!" with dis
        show c 121
        bgar "Are you talking to me? Who the fuck are you?"
        show c 119
    mc "Mr. Garrington! I'm a big fan!"
    mc "I've always admired how your family built an empire out of nothing!"
    if sitbet:
        show c 117
    else:
        show c 121
    bgar "Thank you. You can fuck off now."
    if sitbet:
        show c 116
    else:
        show c 119
    mc "You must be wondering why I'm here."
    if sitbet:
        show c 117
    else:
        show c 121
    bgar "No."
    if sitbet:
        show c 116
    else:
        show c 119
    mc "Just like you, I'm an entrepreneur, and I've come to make you an offer you can't refuse."
    if sitbet:
        show c 117
    else:
        show c 121
    bgar "What offer? And how did you get into the VIP section?"
    play sound chair3
    show c 118
    mc "*Standing up* Would you be so kind as to take out of the fridge the bottle I gave you, young lady?"with dis
    wai "Of course, sir."
    play sound chair1
    play sound3 cork
    show c 120
    mc "This is my exclusive Marani Wine." with dis
    mc "Aged in oak barrels for seven years in a special server with experimental time dilation, we’ve created a wine that’s aged nearly 30 years in a quarter of the time! We believe we’ve created the perfect wine!"
    mc "And we think Garrington’s Casino would be the perfect partner for us to market and sell that wine!"
    show c 121
    bgar "*Sighs* Wine? For the casino? It's my father who deals with that stupid stuff, so stop bothering me about it."
    show c 123
    mc "Oh... I'm sorry, I thought you had some power in the company too. My bad."
    show c 121
    bgar "Hey, hey, hold your horses, buddy. It's not that. I have just as much power as my father."
    show c 120
    mc "In that case, I insist that you take a sip of my wine. Believe me, you'll order a full shipment after tasting it."
    show c 122
    p "Can I be the one to taste it?"
    p "*Giggles* Wine always makes me feel a little... naughty..."
    bgar "In that case... maybe you should drink the whole bottle..."
    show c 123
    mc "That's not a good idea... This wine is only for Mr. Garrington..."
    show c 122
    bgar "Nonsense."
    bgar "Drink as much as you want, baby..."
    play sound swallow
    show c 124
    mc "Wait, no!" with dis
    p "*Drinks all of it*"
    show c 125
    p "Ugh... It tastes bitter..." with dis08
    show c 126
    bgar "Seriously? Did you really try to sell me sour wine?"
    show c 125
    p "My throat feels sore..."
    p "And I’m feeling a little nauseous..."
    show c 126
    bgar "You ok? Do you want to–"
    play sound cough2
    show c 127
    p "*Coughs*" with hpunch
    bgar "Jesus Christ, be careful!"
    bgar "Cover your mouth when you're coughing."
    play sound chair1
    show c 128
    p "Agh... I feel awful all of a sudden..." with dis
    play sound2 chair1
    show c 129
    bgar "W-What the fuck is that?! What happened to your face?!" with hpunch
    show c 128
    p "I'm d-dying..."
    show c 129
    bgar "F-Fuck! Go get a doctor or something, Brad!"
    show c 130
    sec1 "But where?"
    bgar "I don't know, anywhere! Someone in the fucking casino has gotta be a doctor in the real world, right??"
    sec1 "O-Okay!"
    show c 128
    p "Fuck, my insides are burning..."
    p "I can't b-breathe..."
    show c 129
    bgar "Are you allergic to something??"
    show c 128
    p "Help me..."
    show c 129
    bgar "I'm not touching you! Get away from me!"
    show c 128
    p "It hurts so much..."
    p "I can't..."
    play sound chair1
    show c 131
    p "*Collapses*" with dis08
    show c 129
    bgar "What the fuck?!" with hpunch
    play sound dooropen3
    show c 130
    sec1 "I found a doctor!"
    show c 129
    bgar "It’s about damn time!"
    show c 131
    bgar "D-Do something, doctor! She started coughing, her face blew up, and then she fainted!"with dis08
    show c 132
    l "Hmmm..." with dis
    play sound click
    show c 133
    pause
    play sound2 click
    show c 132
    pause .2
    play sound click
    show c 133
    pause .1
    play sound2 click
    show c 132
    pause .2
    play sound click
    show c 133
    pause .4
    l "Oh my god..." with dis08
    l "She's dead..."
    l "She's been poisoned with Hydroxynosinemate toxin."
    l "Don't let anybody else touch her body or get too close to her. It's highly contagious and absolutely lethal. As long as she didn’t get too near or directly cough on anyone, we should be relatively safe."
    show c 129
    bgar "What do you mean {i}LETHAL{/I}?!"
    bgar "I touched her! S-She coughed all over me!"
    bgar "Am I infected?!"
    show c 133
    l "You touched her...?"
    l "Oh god, then it is very likely, yes..."
    show c 129
    bgar "W-What?!"with hpunch
    bgar "What's gonna happen to me? What's this Hydroxynomanate toxin?!"
    play sound jumpscare
    stop music2 fadeout 1
    play music risinglong
    show c 134
    pause .01
    show lz04
    l "The Hydroxynosinemate toxin was synthesized 4 years ago in a clandestine laboratory in Eastern Europe, when the Albanian mafia got tired of not being able to apply enough punishment to traitors..." with Dissolve(2)
    l "...It was specially designed with the goal of inflicting as much pain as possible within Eternum."
    l "In a world where dying is not a true punishment, they decided to create something worse than death... the worst of tortures... the Hydroxynosinemate compound."
    l "With such a high, concentrated dose, this woman died within seconds. However, in your case... you won't be that lucky."
    show lz042
    l "When the toxin gets into your bloodstream, absorbed through the skin, you start to feel dizzy after a few minutes."
    l "Then, your eyes swell and you start having trouble breathing. Sweating, chills, fever and migraines start."
    l "Before you can even react, you experience muscular paralysis and lose control of your limbs... and sphincter."
    show lz043
    l "Your skin starts peeling off, and your thinnest capillaries rupture, causing an internal hemorrhage throughout your body."
    l "Your lungs are filled with blood, provoking a choking sensation that can last several minutes."
    l "Finally, your nervous system fully collapses, causing a chain reaction that physicians describe as being burned alive."
    l "They say the pain is so heinous that the brain is unable to recover and attempts to shut itself down. Because of the nature of the neural implant, this can cause chronic ailments both in Eternum and in real life."
    l "All those who have suffered its effects have been confined to psychiatric hospitals where they still cry out in pain or, if they’re lucky, managed to kill themselves before being locked away."
    show lz044
    pause
    bgar "*Hyperventilating* S-So..." with dis08
    bgar "A-Am I already d-doomed??!"
    bgar "THERE'S N-NOTHING I CAN D-DO?!"
    show lz045
    l "I'm afraid that...{w=2}{nw}"
    play soundlow ding
    stop music
    play music2 heist4
    show laz04b
    l "Yeah, you probably can." with Dissolve(.05)
    l " But you have to wash your hands and face immediately."
    l "You should hurry."
    play soundlow slam
    play sound3 run
    play sound chair2
    scene c 135b
    bgar "GET THE FUCK OUT OF MY WAY!" with dis
    sec1 "Be careful! He's infected!"
    bgar "And kill the fucking bastard who tried to poison me!!!" with hpunch
    sec2 "Yes sir!"
    show c 136
    mc "Wait, wait, wait!" with dis
    mc "This was all just a big misundersta–"
    show uighrt4
    pause .12
    play sound punch
    play sound2 ding
    stop music2
    show screen time0938
    pause
    play music2 heist2 fadein 4
    hide screen time0938
    scene c 140
    with dis2
    be "And here it is! The Garrington vault."with dissolve
    show c 137
    be "More than 100 feet of reinforced concrete in all directions – impossible to break into."with dis
    be "1668 days since inauguration, and not a single successful robbery!"
    show c 138
    n "Good..." with dis08
    n "This is exactly what my boss was looking for."
    n "How many security officers were there again?"
    show c 137
    be "There's over 40 in the bank alone, plus another 50 in the casino hotel, ready to mobilize at a moment’s notice, in case of emergency."with dis08
    show c 138
    n "Excellent..."with dis08
    n "Alright, let's not waste any more time."
    show c 139
    be "Can you open the main vault, please? Authorization code number 23547."with dis
    sec2 "They both have passed through the Polyjuice scanners."
    play sound type1
    sec1 "Authorization code verified. You can retrieve your belongings now."
    show c 140
    sec1 "Opening the main vault."with dis
    play sound3 vault1
    pause .8
    show c 141
    pause .75
    show c 142
    pause 1
    show c 143
    pause 1
    show c 144 with dis12
    pause .3
    play sound2 vault2
    pause 1
    show c 145 with dis2
    pause
    show c 146
    be "Your designated deposit box will be D-32." with dis12
    be "And you will receive the only copy of the key, of course."
    show c 147
    n "Hmm..." with dis08
    play sound w1
    play sound2 type2
    scene c 106b
    d "Alright Saturn, I can deactivate the magic blocker inside the vault from here, but not for more than 60 seconds."with pushu
    d "After that, an alarm is triggered and the whole server gets locked."
    d "Once the distraction starts, leave the case and get out as fast as you can. Are you ready?"
    play sound2 w1
    scene c 147
    n "Mm-hm..." with pushd
    scene c 146
    be "Ms. Vasiliev? Is there a problem?"with dis08
    play sound w1
    scene c 106b
    d "Disabling magic blocker... now!"with pushu
    play sound2 w1
    scene c 148
    n "*Entering the vault* No problem. I was just admiring this construction." with pushd
    scene c 105
    d "And the show starts in 3..."with dis08
    show c 106
    d "2..."with dis
    scene c 148
    d "1..."with dis
    play soundlow explosionbank
    stop music2
    show c 148 with hpunch
    pause .6
    show c 149
    n "W-What was that?!" with dis12
    be "Uh..."
    play sound revolver
    play sound2 revolver
    show c 168 with flashfaster
    rau "Everybody get down!" with dis08
    show c 170
    rau "THIS IS A ROBBERY!" with hpunch
    play sound metalhit
    play music2 heist
    show snatch8
    pause
    play sound2 ding
    scene snatch8b
    player2 "Oh god, please don't kill me!"
    show c 170
    rau "Don't try anything funny and you won't get hurt."with dis04
    rau "We're just here for the money!"
    rau "We want $10 million in unmarked bills delivered in one hour's time."
    play sound gunload
    show c 171
    je "STAY ON THE FU–" with dis08
    play sound gunshot
    show c 172 with hpunch
    pause .4
    play sound3 fall
    play sound2 fall2
    play sound5 fall2
    show c 173
    rau "Oh shit, they have snipers!" with dis
    play sound4 sniperbolt
    play sound6 beep2
    sec2 "Officer number 34 reporting, attempted robbery in the bank's main hall."
    sec2 "I repeat, attempted robbery in Garrington's bank. I request immediate fire support. All units from the bank and hotel, maintain radio contact and move now!"
    play music2b firefight fadein 2
    show c 149
    n "What on Earth is going on up there?!" with dis12
    show c 150
    be "I assure you this rarely happens, ma'am!"with dis08
    be "Just leave the suitcase here, it's the safest place in all the bank! R-Rest assured, nothing will happen!"
    n "Are you sure?"
    be "Absolutely!"
    show c 151
    n "*Leaving the suitcase* You’d better be right..." with dis
    show c 152
    be "We can go back once the situation is under control, don't worry. It's just better if we keep the vault closed for now."with dis12
    play soundlow vault2
    show c 153
    sec1 "Closing the vault!" with dis12
    be "P-Please ma'am, follow me. We can get to the nearest Exit Portal by using the Emergency Exit."
    show c 154
    n "If something happens to that case, my boss will be really upset. And that will make ME very upset. Do you understand the importance of this matter?" with dis04
    be "O-Of course, ma'am!"
    stop music2b fadeout 2
    show c 155 with dis2
    pause
    play sound suitcase
    show c 156 with dissolve
    pause
    play sound chick
    show c 157
    chick "*Chirps*" with dis
    show c 158 with dis
    pause
    play soundlow chair4
    play sound2 chick
    show c 159
    chick "*Jumps*" with dis08
    show c 160 with dis12
    play sound chick
    chick "*Chirps*" with dis08
    show c 105
    d "Aaaand... magic blocker enabled again in 3..."with dis
    show c 106
    d "2..."with dis08
    scene c 162
    d "1..." with dis08
    play sound spell4
    play sound2 spell2
    show chickzoom with flashfast
    pause 2.4
    scene c 163 with dis12
    x "Ugh... "with dissolve
    play sound metalhit
    show snatch9
    pause
    play sound2 ding
    scene snatch9b
    x "It feels weird when I don't transform myself willingly."
    play sound chair3
    show c 164b
    x "Alright, let's get to work..."with dis
    play sound5 w1
    show c 104
    d "Can you hear me, hottie?"with pushu
    play sound5 w1
    $ unlock_look("alex", 4)
    show c 164
    x "*Connecting the earplug* Loud and clear."with pushd
    x "I'm sorry I added a shirt, I know you were enjoying the view."
    play sound5 w1
    show c 106
    d "*Chuckles* I won't confirm or deny those allegations."with pushu
    d "The chick was adorable, though."
    play sound5 w1
    show c 165
    x "I usually prefer my dragon or shark forms, but I'll admit this one can be very useful too."with pushd
    x "Alright, so... How's the diversion tactic in the main hall going?"
    play sound5 w1
    show c 105
    d "Um..."with pushu
    stop music2
    play music firefight
    show bothz04
    pause
    rau "This job is gonna be more difficult than we thought, Noah."with dis08
    rau "We underestimated the amount of men they could bring."
    play musicb epic2 fadein 3
    scene noahz04
    noa "You must retreat and go back to the Exit Portal. I'll stay and stall them." with dis12
    noa "We can't afford to lose your level and inventory."
    noa "Not after all we've been through."
    scene raulz04
    rau "You have just as much to lose as I do."with dis
    scene noahz04
    noa "Still, better to lose one than to lose both."with dis
    scene raulz04
    rau ". . ."with dis
    rau "Do you remember what I told you in the trenches in Sarajevo?"
    play sound explosionbank
    rau "That day 30 years ago?"
    scene noahz04
    noa ". . ."with dis
    noa "{i}You'll never fight alone."with dis08
    scene raulz04
    rau "And you never will, my brother."with dis
    rau "Let's have one last dance."
    scene noahz04
    noa "To hell and back, moj brate."with dis
    scene bothz04
    rau "To hell... and back." with dis
    stop musicb
    stop music
    play music2 heist
    scene c 105
    d "They're doing fine, I think."
    play sound w1
    show c 165
    x "Okay, so... which one’s Garrington's box?"with pushd
    d "A-26."
    play music lockpick fadein 1
    show c 166
    x "*Picking the lock* Okay, let's see what we have here..." with dis12
    d "So where did an upper-class, bougie girl like you learn to pick locks?"
    x "Oh, you don't wanna know..."
    stop music
    show c 106
    d "*Chuckles* Be honest, you just wanted people to think you were a bad girl."
    x "I'll admit that–"
    play sound chairoffice
    show c 106b
    d "Oh shit... some of them are coming back to the vault!"with dis08
    play music lockpick
    show c 167
    x "Fuck, really?"
    d "Yeah! There are 4 or 5 of them!"
    x "How did they find out?"
    d "I don't know!"
    d "But..."
    stop music
    show c 106b
    d "T-They have explosives!"
    d "Neptune, you gotta hide!"
    play music lockpick
    show c 166
    x "I don't know if you've seen it, but there's not much room to hide in here."
    x "Can you disable the magic blocker again?"
    x "Mars?"
    stop music
    show c 106b
    d "Neptune? Hello? Can you hear me?"
    d "Neptune!"
    d "Fuck, they cut off communications!"
    play music lockpick
    show c 166
    x "Come on, open up..."
    stop music
    show c 106b
    d "Watch out! They're opening the vault!!"with hpunch
    play music lockpick
    show c 166
    x "Come on..."
    sec1 "Blow the door off!" with hpunch
    stop music
    show c 167b
    x "Wait, what?!"with dis
    x "Wait, wait, wa–"
    play soundlow explosionbank
    stop music2
    show black
    pause
    play music vent fadein 3
    show screen time0958 with dis2
    pause
    hide screen time0958
    scene c 177
    with dis2
    pause
    show c 12
    mc ". . ." with dis12
    cgar "*Laughs*"
    show c 15
    cgar "You've been watching the clock for a while now."
    cgar "Were you expecting something to happen?"
    show c 12
    mc ". . ."
    show c 14
    cgar "I guess they must have arrested your friend in the vault already."
    mc "W-What...?"
    show c 15
    cgar "*Laughs* Did you really think I wasn't going to see that coming?"with dis08
    cgar "The distraction tactic is older than Rome, boy."
    cgar "The attempt to poison my son, the attack on the bank... it was all to distract me and my men, so you could sneak into my vault and steal my Gem of Doom, am I right?"
    show c 178
    mc "How the fuck did you..."
    show c 15
    cgar "How did I know?"
    cgar "I've lived a long time, son."
    cgar "Many others have tried before."
    cgar "But I'll be honest, I'm still curious about how you found out that I have a Gem of Doom."
    play sound chain
    show c 17
    mc "Son of a bitch!"with hpunch
    show c 15
    cgar "*Laughs* And do you know what the funniest thing is?"
    cgar "The Gem of Doom isn't even there!"
    cgar "My personal safe is totally empty!"
    cgar "I'd have paid to see the face of whoever opened it!"
    cgar "All that work and you weren't even close!"
    show c 178
    mc "E-Empty...?"
    show c 183
    mc "Fuck..." with dis
    mc "I knew this whole plan was too hasty..."
    play soundlow ring
    pause .6
    show c 15
    cgar "Ah, that must be my men telling me the job is done."with dis12
    play sound beep2
    show c 179
    cgar "Garrington." with dis08
    cgar "Is it done? Do you have them?"
    show c 180
    sec1 "We went to the security room, sir. The camera operators were unconscious, but whoever did it escaped before we arrived."with dissolve
    sec1 "Also, the shooting in the bank lobby has gotten complicated. Those two men are way tougher than we thought."
    show c 179
    cgar "Whatever, let them go. We'll get them later." with dissolve
    cgar "Tell me about the vault."
    show c 180
    sec1 "We're inside, sir. It’s... empty." with dissolve
    show c 181
    cgar "What do you mean, \"empty\"?"with dissolve
    show c 182
    sec1 "All the money is still on the table, they haven't touched anything."with dissolve
    show c 181
    cgar "Of course, because they know it's marked."with dissolve
    cgar "Did you get their thief?"
    show c 182
    sec1 "There's no one here."with dissolve
    sec1 "And only your personal box was open. It’s empty."
    show c 181
    cgar "I know it's fucking empty. But if the box was open, then they must have been in there!"with dissolve
    show c 182
    sec1 "There's no one, sir. We've checked everything and everywhere."with dissolve
    sec1 "The only thing we found out of place was this strange piece of cardboard."
    show c 181
    cgar "Cardboard? What cardboard?"with dissolve
    show c 182b
    sec1 "Um... It's just a white paper with a drawing and the word \"Chang'd\" written on it."
    sec1 "We don't know what it means."
    show c 181
    cgar "What? Are the..."
    show c 182
    cgar ". . ." with dissolve
    show c 183
    pause
    show c 182
    cgar ". . ."
    play sound chairmove
    show c 184
    cgar "*Standing up* Put me through to the guards at the door of my suite."with dis
    sec1 "Um..."
    sec1 "...I don't think there's anyone there right now."
    play soundlow slam
    show c 185
    cgar "WHAT?!" with vpunch
    cgar "What did you say?!"
    show c 186
    sec1 "A-All our guards from the casino and hotel moved to the bank after your call!"
    sec1 "W-We were already running short on men because of the shooting at the bank!"
    show c 185
    cgar "You left my suite unprotected?!"with vpunch
    show c 186
    sec1 "It's c-completely impenetrable, sir!"
    sec1 "Even if there's no surveillance, the magic blockers are always active, and the door has a titanium deadbolt and a reinforced jam!"
    sec1 "The windows are made with bulletproof glass, and the ventilation system is too small for anyone to pass through!"
    play sound dooropen3
    pause .5
    show c 187
    bgar "YOU!" with dis
    bgar "This guy is the one who tried to poison me, Dad!"
    bgar "Their group tried to kill me not once, but twice!"
    cgar "Twice...?"
    show c 188
    bgar "Yeah! When I was going to the bathroom to remove the poison from my skin, I was attacked by a kid!"with dis08
    bgar "She tried to cut me with a knife! I mean, I didn't see the knife, but... she scratched me!"
    show c 190
    cgar "What are you talking about? Kids can't enter the casino."
    show c 188
    bgar "Um... Well, to be honest, I didn't see her clearly. Maybe she was an adult."
    show c 189
    bgar "But in any case, she was no taller than... this."with dis
    bgar "I think..."
    show c 190
    cgar "Small enough to fit through the ventilation system?"
    show c 188
    bgar "What?"
    show c 190
    pause
    show c 191
    cgar ". . ." with dis
    show c 183
    pause
    show c 191
    pause
    stop music fadeout 15
    show c 192 with dis2
    $ renpy.music.set_volume(0.3, channel='music3')
    play music3 heist5 fadein 10
    pause
    play sound safeopen
    play sound2 safeopen
    show c 193 with dis12
    pause
    show c 194
    a "Ohhh..." with dis12
    play sound metalhit
    show snatch10
    pause
    play sound2 ding
    scene snatch10b
    a "It's so shiny!"
    show c 195
    if anniepath:
        a "It looks just as pretty as the one we found in the spooky server!"with dis
    else:
        a "It looks just as pretty as I imagined!"with dis
    a "And it's so cold..."
    play sound doorlocked
    show c 196 with dis
    play sound knock3
    sec2 "F-Fuck, they've locked it from the inside!"with dissolve
    sec2 "Open up!"with hpunch
    show c 195
    a "Time to go!" with dissolve
    show c 191
    cgar "You motherfucker..." with dis12
    show c 183
    pause
    play sound chain
    show c 198
    mc "We didn't really know where the Gem was, but there were only two options: the bank's vault, or the safe with the genetic scanner in your suite." with dis
    show c 199
    mc "We couldn't risk it, so we had to plan a simultaneous, two-pronged attack." with dis08
    mc "While some of us were breaking into the vault, others would also sneak into your suite: unprotected because of the attack, and breachable thanks to your son’s genetic sample."
    show c 198
    mc "There was also a third option, that you were carrying it around the whole time, but judging by your reaction, I don’t think that's the case." with dis08
    show c 210
    cgar "You're never going to escape from here with it..."
    show c 200
    mc "Ahh, well..."
    mc "That's where you're wrong."
    mc "We had a good escape plan."
    play sound3 spell3
    play sound2 spell2
    play music2b energy2 fadein 1
    show c 201
    mc "A damn good one. The easiest part of the heist, really." with dissolve
    play sound2 teleport
    show c 202
    mc "It almost feels like cheating, to be honest." with flashfast
    play sound chaindrop
    show c 205
    mc "We still had to find out a way to sneak in, of course." with dis12
    mc "It was a challenge to get into the vault and the suite unnoticed, but exiting was never a huge concern..."
    play sound chair2
    show c 206
    mc "*Standing up* This lady here can create portals to and from wherever we want." with dis12
    mc "And she’s unaffected by magic blockers or restrictions of any kind."
    mc "We're immensely lucky to be assisted by the Princess of the Sy-tel-quessir herself..."
    show c 207
    ca "That is better. I appreciate that you are finally treating me with due respect."with dis08
    show c 206
    mc "Anything to please my beloved Princess..."with dis08
    play soundlow spell2
    show c 208
    ca "Is this what you were looking for?" with dis
    show c 209
    mc "Hell yeah!"
    mc "I’m guessing Pluto gave this to you. Is she safe?"
    show c 208
    ca "They all are. You are the last one."
    show c 209
    mc "Excellent!"
    mc "Was it too tiring to open so many portals?"
    show c 208
    ca "I had enough time to prepare myself. And they were all near each other, and in the same world. That made it easier."
    ca "I am feeling stronger too. Soon I will be able to return to my homeland. I can feel it."
    show c 209
    mc "I'm happy to hear that. Please don’t overexert yourself."
    show c 212
    mc "Well, it's been a pleasure, Mr. Garrington." with dis
    show c 210
    mc "Take care and give your employees raises, they definitely deserve them after tonight."with dis08
    show c 211
    mc "Oh, and no worries Bennie, the Hydroxynosinemate toxin doesn't exist, so you can sleep soundly tonight."with dis08
    bgar "W-What is going on? Y-You had a Gem of Doom, Dad?"
    bgar "And they just stole it?!"with hpunch
    mc "Nah, I wouldn't say \"steal.\""
    show c 212
    mc "Someone once told me that in Eternum, things don't actually get stolen..." with dis
    mc "They just happen to... move around."
    play sound3 spell3
    play sound2 spell2
    show c 213 with flashfast
    stop music2b
    pause
    show c 210
    cgar ". . ." with dis
    bgar "Um... Dad?"
    play sound risingshort4
    cgar ". . .{w=2}{nw}"
    stop music3 fadeout 4
    show login3 with flash
    pause 8
    play soundlow whoosh4
    scene white with dissolve
    play music2b idriel fadein 6
    scene white with Dissolve(.3)
    scene cc 1 with Dissolve(2.5)
    mc "Oh my god, we did it!" with dis
    mc "We fucking did it, girls!!!" with hpunch
    mc "We..."
    mc "(Wait... Why am I in the Main Nexus? Wasn't I using a portal?)"
    play sound coinflip
    id "Heads."
    show cc 2
    mc "*Turning around* Oh... H-Hi, Idriel." with dis
    show cc 3
    mc "Why... Why am I here?" with dis
    play sound coinflip
    show cc 4 with Dissolve(.3)
    pause .3
    show cc 3 with dis04
    pause .2
    show cc 5
    id "Heads."with dissolve
    id "You were redirected here after using an Exit Portal."
    id "We detected you own a Gem of Doom now."
    id "Congratulations."
    show cc 3
    mc "Oh... Y-Yeah! Thank you!"
    mc "It's not the first time I've had one, though."
    play sound coinflip
    show cc 4 with Dissolve(.3)
    pause .3
    show cc 3 with dis04
    pause .2
    show cc 5
    id "Heads."with dissolve
    id "I know. But this time is special. We're holding an exclusive dinner this Saturday evening, at the Rockefeller server."
    id "Only the most important people of Eternum are invited, and that includes... the owners of Gems of Doom."
    play sound coinflip
    show cc 4 with Dissolve(.3)
    pause .3
    show cc 3 with dis04
    show cc 6 with dis12
    show cc 8
    id "Heads."with dis04
    show cc 6
    mc "Oh... that's... awesome! I had no idea."
    show cc 8
    id "The invitation of the previous owner of this Gem will be revoked, and given to you instead."
    id "If you lose your Gem before Saturday, you'll lose your invitation as well."
    show cc 6
    mc "I'll make sure not to lose it. Thank you so much."
    play sound coinflip
    show cc 7 with Dissolve(.3)
    pause .3
    show cc 6 with dis04
    pause .2
    show cc 8
    id "Heads."with dissolve
    id "You can bring a guest of your choice."
    id "Obviously, given the nature of the event, all kinds of violence or attempted robberies are forbidden."
    id "And finally, all guests must wear masks during the ceremony, to avoid disclosing the identities of the other Gem holders."
    show cc 6
    mc "That makes sense."
    mc "What do I have to do to go there?"
    play sound coinflip
    show cc 7 with Dissolve(.3)
    pause .3
    show cc 6 with dis04
    pause .2
    show cc 8
    id "Heads."with dissolve
    id "Just join the associated server and enter the Boyle mansion. You will be given access to both when the time comes."
    show cc 6
    mc "Wonderful. Thanks, Idriel."
    show cc 8
    id "Do you have any questions about anything?"
    show cc 6
    mc "Um..."
    mc "Well, now that you mention it, can I ask what level I am?"
    play sound coinflip
    show cc 7 with Dissolve(.3)
    pause .3
    show cc 6 with dis04
    pause .2
    show cc 8
    id "Heads."with dissolve
    if rotundafail:
        $ mclevel += 2
    else:
        $ mclevel += 7
    id "You're level [mclevel]."
    show cc 6
    mc "I see... Thank you."
    mc "Uh... well, I guess that was all."
    mc "Will I see you at the dinner?"
    show cc 8
    id "Of course."
    id "As long as you don't lose your Gem."
    play sound coinflip
    show cc 7 with Dissolve(.3)
    pause .3
    show cc 6 with dis04
    pause .2
    show cc 8
    id "Heads."with dissolve
    show cc 6
    mc "Alright."
    mc "I guess I'll log off now. I'm pretty tired. And hungry."
    mc "Bye!"
    show cc 8
    id "Until next time, [mc]."
    play sound coinflip
    show cc 7 with Dissolve(.3)
    pause .4
    play soundlow grab
    show cc 9 with dis04
    pause
    show cc 10
    id "Heads..." with dis08
    id "Or tails...?"with dis08
    show cc 11
    menu:
        with dis12
        "Heads":
            mc "Heads."with dissolve
            play sound risingshort
            pause 1.2
        "[gr]Tails":
            $ tailscoin = True
            mc "Tails."with dissolve
            play sound risingshort
            show cc 12 with dis
            pause 0.2
    stop music2b
    show black
    pause
    show screen afewdayslater with dis15
    pause
    $ renpy.music.set_volume(0.45, channel='music2')
    $ renpy.music.set_volume(0.45, channel='music2b')
    play music2 happy9 fadein 10
    hide screen afewdayslater
    scene cc 13
    with Dissolve(2.5)
    pause
    play sound type1
    mc "(Okay...)" with dis08
    mc "(I finally feel like everything is under control.)"
    show cc 14
    mc "(It should be safe to play Eternum again.)"with dis
    mc "(Not the New Vegas server, though. Garrington must have left no stone unturned to find clues about us.)"
    mc "(But he only knows our faces. As long as we keep low profiles, we should be good. Eternum is just too big, and technically we didn't even do anything illegal, according to Eternum's Code of Ethics.)"
    $ money -= 1170
    show screen eternals
    mc "(So... getting back to this balance statement...)" with dis
    play sound coins
    $ money += 1170
    mc "(We got 1170 eternals from Bobbie...)"
    play sound coins
    $ money += 880
    mc "(Plus the 880 unmarked eternals Bennie was carrying in his wallet when Annie took it...)"
    play sound coins
    $ money -= 270
    mc "(Minus the costs of the outfits and materials...)"
    play sound coins
    $ money -= 300
    mc "(The chip we needed to hack into their system and create our fake ID profiles...)"
    play sound coins
    $ money -= 1600
    mc "(And the cost of hiring Raul and Noah...)"
    mc "(We’re left with a net...)"
    show cc 15
    mc "(...loss of 120 eternals.)"with dis04
    mc "(Goddammit.)"
    mc "(At least Jerry helped us for free because of Dalia.)"
    if moneywonsomething:
        mct "And... well, I won something at the slots. Could be worse."
    hide screen eternals
    show cc 16
    x "More coffee?" with dissolve
    $ unlock_look("alex", 5)
    show cc 17
    mc "More coffee? God, no, please."with dis08
    mc "Tell whoever made it that it's absolutely terrible."
    if alexpath:
        show cc 18
        x "Ha, ha. Very funny."with dis04
        show cc 17
        mc "Oh shit, sorry! Did you make it?"with dis04
        show cc 18
        x "Fuck off, you know I did."with dis04
        x "Why did you come here again?"
        show cc 17
        mc "I was on my way to the gym, and I remembered this was the cafe where you said you were working after school."with dis04
        mc "And I had to crunch some numbers, so... I thought I'd enjoy a coffee here."
        show cc 18
        x "I see..."with dis04
        show cc 17
        mc "I'd ask you to sit with me for a moment, but your boss would probably be mad at you."with dis04
        show cc 18
        x "Actually, I'm on my 10 minute break."with dis04
        show cc 17
        mc "Oh! Would you mind spending it with me, then? There's something I have to ask you."with dis04
        play sound chair2
        show cc 21
        x "By the look on your face, it seems important... Okay, tell me."with dis12
        show cc 20
        mc "It's about that dinner at the Boyle mansion... The one I was invited to after getting Garrington's Gem." with dissolve
        x "Mm-hm."
        mc "I've been talking with the others and we think that it should be you who comes with me."
        show cc 23
        x "Who, me? Why?" with dis
        show cc 24
        mc "You've been living in these circles all your life, so you probably know how to blend in better than any of us."with dis04
        show cc 23
        x "Um... Really? Have you seen me? Do I look like someone who would blend in among a bunch of snobs?"with dis04
        show cc 24
        mc "I know you hate that kind of stuff, but I'm also sure you've been around people like that for a while now."with dis04
        mc "You're our best way of getting information from that dinner."
        show cc 22
        x "That's a fair point..." with dis
        x "But my father will probably be there. I don't want him to see me."
        mc "Idriel told me that all the guests will be wearing masks to preserve anonymity. You'll also have to use some kind of makeup to conceal the tats, but... that should be enough."
        show cc 21
        x "Oh... That's cool."with dissolve
        x "That... changes things a little."
        x "Yeah, okay, I'll go with you."
        show cc 20
        mc "Nice! Thanks, Alex."with dissolve
        mc "Don't make any plans for Saturday night."
        show cc 21
        x "I won't."with dissolve
        show cc 20
        mc "Alright, mission successful. I can happily go to the gym now."with dissolve
        show cc 21
        x "Ah, yeah. The gym competition is this afternoon, isn't it?"with dissolve
        show cc 20
        if daliapath:
            mc "Yep! Dalia's been pretty nervous about it the last few days."with dissolve
            mc "She's been talking about it for weeks."
            show cc 21
            x "I know, I'm happy that she could recover from her back injury in time. This is very important to her."with dissolve
            show cc 20
            mc "Aren't you participating?"with dissolve
            show cc 21
            x "I already did. There's a bunch of categories, so they're divided into three days. The swimming events were yesterday."with dissolve
            show cc 20
            mc "Oh, really? I'd have liked to come and see you. Did you win?"with dissolve
            show cc 21
            x "You doubt me?"with dissolve
            show cc 20
            mc "I don't! Dalia told me you're the best swimmer in the country."with dissolve
            show cc 21
            x "Bah, she always exaggerates."with dissolve
            x "I don't exaggerate, though, and I can tell she's very good at fitness. Wish her luck for me."
            show cc 20
            mc "I will!"with dissolve
        else:
            mc "Oh shit, I should get going if I want to get there on time." with dissolve
            mc "Dalia asked me not to go."
            show cc 21
            x "You better do as she says, then. She kicks hard."
            show cc 20
            mc "*Chuckles* Oh, I know."
            mc "No gym for me today, then."
        play sound chair2
        show cc 18
        x "*Standing up* Well, I gotta get back to work." with dis
        x "Thanks for coming by."
        show cc 17
        menu:
            with dis
            "Don't tip her":
                mc "My pleasure. See ya!"with dissolve
            "[gr]Give her a small tip":
                show screen eternals
                show cc 25b
                with dis
                play sound coins
                $ money -= 5
                mc "I haven't paid for my coffee. Take this, you can keep the change."with dis08
                hide screen eternals
                show cc 18
                x "You don't have to give me anything, no worries."with dis
                hide screen eternals
                show cc 17
                mc "It's an investment. Use it to buy me a couple of drinks when I visit your new apartment."with dis04
                show cc 18
                x "My apartment? What makes you think I'll invite you after I've moved?"with dis04
                show cc 17
                mc "You wouldn't dare leave me out, would you?"with dis04
                show cc 18
                x "Erm..."with dis04
                x "I'll think about it."
                show cc 17
                mc "I'll take that."with dis04
                $ alex_points += 1
                play sound "beat.ogg"
                show cc 18
                show screen heartbeat
                x "Thanks for the tip, in any case." with dissolve
                show cc 17
                mc "My pleasure, Alex. See you later!"with dis04
                show cc 18
                x "Bye, [mc]."with dis04
            "Give her a big tip":
                show cc 25
                mc "I haven't paid for my coffee. Take this, you can keep the change."with dis08
                show cc 19
                x "What? $50?"with dis
                x "I don't want that much."
                show cc 17
                mc "Come on, take it. I know you're moving soon, you'll need the money."with dis04
                show cc 19
                x "I don't need your charity, thank you."with dis04
                x "I can handle myself."
                show cc 17
                mc "Okay, okay, as you like."with dis04
                mc "See you later!"
    else:
        show cc 19
        x "Ha, ha. Very funny."with dis04
        x "*Sighs* Why did you say you came again?"
        show cc 17
        mc "Well, I wanted to ask you something."with dis04
        mc "It's about that dinner at the Boyle mansion... I've been talking with the others and we think that it should be you who comes with me."
        show cc 19
        x "What? Why me?"with dis04
        show cc 17
        mc "You've been living in these circles all your life, so you probably know how to blend in better than any of us."with dis04
        show cc 19
        x "I've never liked those fancy dinners or whatever this shit is."with dis04
        show cc 17
        mc "Come on... please, Alex!"with dis04
        show cc 19
        x "Uhh..."with dis04
        x "*Sighs* Well, I guess I can drop by. For our common goal. You wouldn't get anything out of it without me."
        x "And I told you not to call me Alex."
        show cc 25b
        mc "S-Sorry, I forgot."with dis08
        mc "But... great! I'll arrange everything!"
        x "Okay."
        mc "Do I have any special disco–"
        x "No."
        mc "Um... o-okay. Ring me up!"
    show cc 26 with dis12
    mc "(Well, I should get going.)"with dissolve
    if daliapath:
        mc "(The competition is about to start. Dalia will be happy to see me there.)"
    else:
        mc "(Now that the gym plan was canceled, I think I'll spend the day playing Eternum.)"
        mc "(A little extra practice never hurt!)"
        jump nightmare04
    mc "(Or so I hope...)"
    stop music2 fadeout 5
    show black with dis2
    show screen afewminuteslater with dis
    pause
    play music2b gym fadein 3
    hide screen afewminuteslater
    scene cc 27
    with dis17
    mc "Hi Millie!" with dissolve
    play sound chair2
    show cc 29 with dis
    show cc 28
    niko "Кто не рискует, тот не пьет шампанского."with dissolve
    show cc 29
    mc "Oh..."
    mc "I thought..."
    mc "Um... Is Millie here? I came for the competition."
    show cc 28
    niko "Милли наверху. Соревнование."
    show cc 29
    mc "Okay, I don’t think we'll get anywhere like this..."
    if nancypath:
        n "He said that Millie's upstairs."
        show cc 31
        mc "*Turning around* What?"with dis
        mc "*Laughs* You speak Russian now?"
        show cc 30
        n "*Chuckles* No, but Millie is upstairs, in the fitness room. So I’m guessing that's what he said."
        n "Did you come to participate in the competition?"
        show cc 31
        mc "Nah, I just came to see Dalia."
        show cc 33
        n "Oh... so you can come and see her, but I can't? Interesting..."with dis08
        n "I wanted to stay too, but she begged me to go home because she said she'd get nervous..."
        n "Looks like she's playing favorites... that's not fair."
        show cc 32
        mc "I guess that I'm just too persuasive."
        show cc 33
        n "That must be it..."
        show cc 30
        n "But well, I have a busy afternoon, so I probably shouldn’t have stayed anyway." with dis08
        n "Thank god tomorrow is Friday."
        show cc 31
        mc "Yeah, it's been a crazy week."
        show cc 30
        n "I haven't been able to play Eternum since the heist."
        show cc 31
        mc "Well, if it's any consolation, neither have I."
        mc "This Saturday, I need to log in no matter what, though."
        show cc 30
        n "Ah yes, the Ulysses dinner, right?"
        show cc 31
        mc "Yep. I'll tell you all about it after I finish."
        show cc 33
        n "Can't wait!" with dis08
        n "I'll probably go to Semper Invicta while you're there. I have an Empire to rule, ya'know."
        show cc 32
        mc "*Chuckles* True."
        mc "And... we still have... a yoga class pending... right?"
        show cc 33
        n "That’s a good boy. I haven't forgotten, don't worry..."
        n "I hope you can keep up with me this ti–"
        play sound clothes1
        show cc 34
        ger "*Hearty laugh* Come on Nan! I have to show you my hubby's new company car!" with dis04
        ger "Don't even ask how much it costs!"
        n "O-Okay, I won't."
        ger "*Hearty laugh* More than $50,000!"
        mc "Uhh... well, see you later!"
        show cc 35
        ger "Oh... Hi Dalia." with Dissolve(.6)
        ger "I'll borrow your mom for a while... You don't mind, do you?"
        menu:
            with dis
            "Play along [nancy_pts]":
                mc "Yeah, sure, I don't mind..."with dis08
                mc "Bye... “Mommy.”"
                $ nancy_points += 1
                play sound beat
                show screen heartbeat
                n "Uhh... I'll see you at home!"
            "Correct her":
                mc "*Sighs* I'm not Dalia. I've told you a hundred times."with dis08
                mc "I'm not Nancy's daughter. I mean, I'm not even a girl! Do I have to spell it out or what?"
                ger "*Hearty laugh* Sorry, I always get everyone's names mixed up! As the PTA president, I have a lot on my mind..."
                mc "Sure... Anyway, goodbye Nancy."
                n "*Chuckles* I'll see you at home!"
        show cc 36 with dis12
        mc "(Jesus, Nancy's flirting is out of control.)"with dissolve
        mc "(With so many people living under the same roof, it'll be hard to find some time alone.)"
        mc "(But oh boy, when we do...)"
        show cc 28
        niko "Рыжая хочет тебя трахнуть!" with dis
        show cc 29
        mc "Um... Yeah, I'll go upstairs, thank you!"
    else:
        mc "I'm gonna go to the fitness room."
        mc "Thanks! I guess."
    show cc 37 with dis2
    mc "Okay..." with dissolve
    mc "Now where's Dalia..."
    show cc 38
    c "Hey buddy!"with dis
    show cc 39
    mc "Hey! There's Chang the Heist Meister!"
    mc "It's been a while already and I still can't believe everything went as you predicted."
    show cc 39b
    c "Obviously. What did you expect from Chang the Brain?"with dis08
    mc "*Chuckles* I should have expected nothing less, I guess."
    mc "That's a nice shirt you’ve got there, by the way."
    show cc 38
    c "Right?" with dis08
    show cc 39
    mc "I assume you came to cheer on Micaela."
    show cc 38
    c "You're goddamn right! I..."
    show cc 40
    mi "Hi guys!" with dis08
    mi "Are you working, Chang?"
    show cc 41
    c "W-working? Ah, n-no! I just finished my shift and I thought I'd stay to..."
    show cc 42
    mi "Oh my god, did you really order that shirt? I thought it was a joke!"with dissolve
    c "Oh... this? I-It's nothing! I have one with [mc]'s face too."
    mc "You do? I-I mean, yeah, he does! Haha. Classic Chang."
    mi "Still, it's a bit embarrassing..."
    c "Oh... I can take it off!"
    mi "No! I mean... don't worry! It's... okay, I guess."
    show cc 43
    mil "OKAY EVERYONE! Let's start the Weightlifting Finals!"with dis
    show cc 44
    mc "Hey Millie! Have you seen Dalia?"
    show cc 45
    mil "She said she was going to drink some water 10 minutes ago, and she hasn't returned since." with dis08
    mil "I was waiting for her, but after the weightlifting competition we still have to do seven other categories."
    mil "I can't put it off anymore."
    show cc 46
    mc "Oh, really?"
    mc "That's weird..."
    mc "(Maybe something happened to her?)"
    mc "I'll go look for her! Give us 10 more minutes, please!"
    show cc 45
    mil "Um..."
    mil "*Sighs* Okay, 10 minutes! But that’s it!"
    show cc 46
    mc "Thanks! I'll be right back!"
    show cc 47 with dis2
    stop music2b fadeout 5
    mc "(Where the hell is she?)"with dis08
    mc "(She's been talking about this competition since I arrived to Kredon, no way she went home.)"
    play music2 sneaky4 fadein 12
    show cc 48
    mc "Hmm?" with dis
    mc "(Oh boy, I'd recognize that ass anywhere...)"
    mc "(What on Earth is she doing there?)"
    play music chew fadein 1
    show cc 49 with dis15
    pause
    stop music fadeout 1
    show cc 50
    d "*Stops chewing*" with dis08
    play sound swallow
    show cc 51
    d ". . ."with dissolve
    mc ". . ."
    d ". . ."
    play soundlow punch
    play sound slap1
    show cc 52
    mc "STOP!" with hpunch
    d "My sandwich!"
    show cc 53
    mc "What the hell, Dalia?!" with dis12
    mc "You can't gorge yourself before a competition!"
    show cc 54
    d "It was just a little snack. I... I’m carbo-loading!"
    show cc 53
    mc "That sandwich was the size of my head!"
    mc "If you eat so much, you’ll feel bloated during the competition later!"
    show cc 54
    d "I know, I know..."
    d "But... I was nervous. And when I'm stressed out, I eat."
    show cc 53
    mc "You're nervous? Why?"
    show cc 54
    d "I've taken part in this competition every fall for the last 4 years."
    d "And I’ve never won first place in ANYTHING."
    show cc 53
    mc "That's because Micaela also participates. I'm sure she'd even win in the male categories, if she could join them."
    mc "Also, who cares if you don't win?"
    show cc 54
    d "I do."
    d "I... I don't like losing."
    d "It makes me feel that all the effort I put into this is worthless."
    d "I think this year I'm gonna stay out of it."
    show cc 53
    mc "You can't do that!"
    mc "Come on, let's go back. Everyone is waiting for you."
    show cc 54
    d "Tell them to start without me."
    d "There are all these signs telling me not to compete today."
    show cc 53
    mc "What? What signs?"
    show cc 55
    d "Well, first off, this morning I put my clothes on inside-out." with dis
    d "And I didn't even realize until Penelope told me in the kitchen."
    show cc 56
    d "Then, I saw a black cat on my way here, and he even kept staring at me for a while, as if he was telling me to turn around."with dissolve
    show cc 57
    d "And finally, when I made it to the gym, a guy tripped by the entrance and spilled his protein shake all over me!"with dissolve
    d "I had to change my leggings!"
    show cc 54
    d "The universe is trying to tell me to go home."with dis
    show cc 53
    mc "I didn't know you were so superstitious."
    show cc 54
    d "I'm not, really. I... guess I’m just using those things as excuses. It's just that..."
    d "What's the point of participating if I already know I’m gonna lose?"
    show cc 53
    menu:
        with dis
        "Go back home with her":
            mc "I guess you have a point there."with dissolve
            mc "Trying is the first step towards failure."
            mc "And you don't have to prove anything to anyone. Come on, let's go home."
            show cc 54
            d "So... We leave? Just like that?"
            show cc 53
            mc "Yeah, I have a better plan: playing Eternum!"
            mc "Let's explore the forests of Ekabar. I've heard some mythical creature is terrorizing the village of Toussaint."
            show cc 58
            d "That sounds fun." with dis08
            d "Okay, let's go home."
            d "Thanks buddy. You're a good friend."
            show cc 59
            mc "(Ouch.)"
            mc "Anytime, Dalia."
            $ daliapath = False
            $ daliau = False
            jump nightmare04
        "[gr]Convince her to participate":
            mc "Those are all just coincidences. I literally wear my underwear inside-out all the time! And I’ve seen that black cat in the alleyway so many times on the way to school."with dissolve
    mc "Plus, that guy that bumped into you, that was probably just a random accident, don’t read into it so much."
    mc "I know this is important to you. You've been training all year, and if you go home now, you'll regret it. Trust me."
    mc "What's the worst that could happen? Coming in second? Pfft, big deal."
    show cc 54
    d "So... we should go back to the competition? Just like that?"
    show cc 53
    mc "Yep. You're strong, and you'll do great. You don't have to worry about anything."
    mc "And hey, whatever happens, you'll still have the best ass in the gym."
    show cc 58
    d "*Chuckles* If you say so..." with dis
    show cc 59
    mc "Just spitting facts."
    $ dalia_points += 1
    play sound beat
    show screen heartbeat
    show cc 58
    d "Thank you, [mc]."with dissolve
    show cc 59
    mc "Nah, I didn’t do anything. You were just overthinking this stuff."
    mc "But alright, enough talking. Let's pump some iron!"
    show cc 60
    d "Hell yeah!" with dis
    d "You're goddamn right! I'm strong! Nothing's gonna stop me!"
    mc "That's the Dalia I know!"
    show cc 61
    d "*Opening the can* To be honest, I don't know what happened to me."with dis08
    play sound sodaexplode
    d "*Opening the can* As you said, I was–{w=1}{nw}"
    show cc 62 with vpunch
    pause 1.4
    play sound2 blood2
    show cc 63 with dis2
    mc "Um..."with dissolve
    mc "L-Looks like that can was a bit shaken..."
    show cc 64
    d "THE UNIVERSE ISN’T MAKING IT EASY, HUH?!"with dis
    show cc 65
    mc "A-Are you okay?"
    show cc 64
    d "I'm fine! I'm feeling even stronger now!"
    d "You can keep sending me signs, universe! It won't stop me!"
    show cc 66
    mc "(Oh shit, her sports bra is transparent when wet...)"with dis
    mc "(It's stuck to her skin like honey...)"
    mc "(And man, her breasts are shaped beautifully, I'd almost forgotten. She doesn’t even need a bra, really...)"
    mc "(Should I say something?)"
    show cc 65
    menu:
        with dis12
        "Tell her about it [dalia_pts]":
            mc "Um... Before we go..." with dissolve
            mc "You probably want to dry off a little bit. I can see your... tits."
            show cc 67
            d "Huh?" with dis08
            play sound clothes1
            show cc 67b
            d "Arrghh!"with hpunch
            d "Fuck!"
            d "I knew this damn top was too cheap!"
            show cc 68
            d "For fuck's sake, can anything else happen to me today?!"with dis08
            show cc 69
            mc "Do you have a change of clothes?"
            show cc 68
            d "I have one in my locker, but I guess I'll have to shower at home. I'm not gonna put my sweaty clothes back on."
            show cc 69
            mc "Are you going to get changed, then?"
            show cc 68
            d "Of course I am. Nothing is stopping me!"
            d "Do you hear me, universe?!"
            d "FUCK YOU!" with hpunch
            show cc 69
            mc "Okay, hurry up!"
            mc "I'll go back to Millie and try to convince her to wait a couple more minutes!"
            $ dalia_points += 1
            play sound beat
            show cc 70
            show screen heartbeat
            d "Okay!" with dissolve
            d "I'll go as fast as I can. Thank you, [mc]."
            mc "See you up there!"
        "Say nothing":
            mc "Um... Okay, let's go." with dissolve
            show cc 71
            d "Nothing is going to stop me now!"with Dissolve(1.25)
            d "Do you hear me, universe?!"
            d "NOTHING!"
            d "Let's go, [mc], to the fitness room!"
            show cc 72 with dis
            play sound whistle2
            gymm "*Whistles* Damn, this gym's membership pays for itself."with dissolve
            show cc 71 with dis
            pause
            d "Huh?"with dissolve
            show cc 73
            d ". . ." with dissolve
            play sound clothes1
            show cc 67b
            d "Arrghh!"with hpunch
            d "Fuck!"
            d "I knew this damn top was too cheap!"
            show cc 68
            d "Were you really going to let me go upstairs like THIS?!"with dis08
            show cc 69
            mc "I d-didn't notice."
            show cc 68
            d "Yeah, sure, don't bullshit me."
            d "I'm gonna go change my top, go back there and convince them to wait for me for a couple more minutes!"
            show cc 69
            mc "Okay!"
            mc "It was a nice bra, though. That's too–"
            show cc 68
            d "Shut the fuck up!"
            show cc 69
            mc "S-See you up there!"
    stop music2 fadeout 4
    play music gymambience fadein 5
    show cc 37 with Dissolve(2.2)
    pause
    show cc 44
    mc "Hey!" with dis
    show cc 43
    mil "Finally! Okay, we can start now! The first competition will be bench–"
    show cc 44
    mc "W-Wait!"
    mc "She's not ready! Give us a couple of minutes, please."
    show cc 45
    mil "Whaaaat? Not yet? We can't wait anymore, [mc]."with dis08
    show cc 46
    mc "Just two minutes! Please!"
    show cc 45
    mil "*Sighs* Two minutes! And then we're starting, with Dalia or without her."
    show cc 46
    mc "Thanks!"
    show cc 38b
    c "Did she have any problems?" with dis
    show cc 39
    mc "Nah, she was just nervous, but she's feeling better already."
    show cc 38
    c "Ah, that happens to all of us. I usually like to relax in a quiet place before something like this."
    show cc 39
    mc "Actually, she told me there's a private server in Eternum where only she has access."
    mc "She should probably have gone there to calm the nerves."
    show cc 38b
    c "Are there private servers in Eternum?"
    show cc 39
    mc "Yeah, that's pretty cool, right? It's like a private beach, and you can only access that server with a password she chose."
    show cc 38b
    c "That sounds awesome! And how does it work? Is it just a code or...?"
    show cc 39
    menu:
        with dis
        "Tell Chang the password\n[mt][red](Closes Dalia's path)":
            $ tellpassword = True
            mc "Yeah, the server is called \"The Cove\", and the password is \"Stormblade.\" If you tell them both to Idriel when you're in the Main Nexus, you're redirected to said server. Pretty simple." with dissolve
            mc "Maybe we can chill there when you get yourself a neural implant!"
            show cc 38
            c "*Chuckles* At the rate I’m blowing through cash, it'll take a few years, but thank you anyway."
        "[gr]Keep it a secret":
            mc "Yeah... something like that, but I can't tell you, sorry. She asked me to keep it a secret."with dissolve
            show cc 38
            c "Ah, no worries man. Secrets are meant to be kept."
            c "I don't even have a neural implant anyway."
    show cc 39
    mc "We’ve gotta get you one!"
    mc "Trust me, it has–"
    play sound doorslam
    play sound2 slam
    $ unlock_look("dalia", 8)
    show cc 74
    d "*Comes in busting out the door*"with hpunch
    mc "There she is!"
    show cc 75 with dissolve
    pause
    show cc 77
    pause
    show cc 75
    pause
    show cc 77
    mi ". . ."
    show cc 75
    d ". . ."
    play sound metalhit
    play music2 gym2
    stop music
    show 04_daliazoom
    pause
    scene cc 77
    pause
    play sound metalhit
    show 04_micaelazoom
    pause
    scene cc79
    mil "Okay guys, we're finally ready to start!" with dis12
    mil "As always we have 6 finalists selected on the basis of personal records."
    mil "Let's start with the cardio–"
    scene cc 80
    gymm "Hey Millie, I'm gonna pass, so... don't count me in."with dis
    mil "What? Why?"
    gymm "Have you seen that girl? Her arms are bigger than my torso!"
    mil "But the important thing is taking pa–"
    gymm "Bullshit! I know you always post the results on social media."
    gymm "I don't come here so people can laugh at me, thank you very much."
    mil "Well... okay, then."
    show cc79
    mil "We have 5 finalists!" with dis
    mil "Let the competition begin!"
    play sound metalhit
    scene cc 81
    pause .4
    play sound2 metalhit
    show cc 82
    pause .4
    play sound3 metalhit
    show cc 83
    c "You got this, Micaela!"
    play sound metalhit
    show cc 84
    pause .4
    play sound2 metalhit
    show cc 85
    pause .4
    play sound3 metalhit
    show cc 86
    mc "Show them what you got, Dalia!"
    play sound w1
    show cc79
    mil "50 burpees, 50 pistols, and 50 sit-ups!"with pushl
    mil "Time starts... now!"
    play sound4 metalhit
    show gymv1 with pushl
    pause 2.5
    play sound5 metalhit
    show gymv2
    pause 2.03
    play sound6 metalhit
    show gymv3
    pause 3.4
    play sound ding
    scene cc 87
    pause
    play sound2 ding
    show cc 88
    pause
    play sound3 ding
    show cc 89
    pause
    play sound4 metalhit
    show gymv4
    pause 3.3
    play sound5 metalhit
    show gymv5
    pause 3.5
    play sound6 metalhit
    show gymv6
    pause 3.1
    play sound ding
    scene cc 90
    pause
    play sound metalhit
    show cc 91
    pause
    play sound2 metalhit
    show cc 92
    pause
    play sound3 metalhit
    show cc 93
    pause
    play sound4 metalhit
    show cc 94
    pause
    play sound5 ding
    show cc 95
    pause
    play sound6 ding
    show cc 96
    pause .2
    play sound ding
    show cc 97
    pause .2
    play sound2 ding
    show cc 98
    pause
    play sound3 metalhit
    show gymv7
    pause 2.9
    play sound4 ding
    scene cc 99
    pause .2
    play sound5 ding
    scene cc 100
    pause .2
    play sound6 ding
    show cc 101
    pause .3
    play sound3 metalhit
    show gymv8
    pause 2.95
    play sound4 ding
    scene cc 101
    pause .2
    play sound5 ding
    scene cc 102
    pause .2
    play sound6 ding
    show cc 103
    pause .3
    play sound3 metalhit
    show gymv9
    pause 2.9
    play sound4 ding
    scene cc79
    mil "Micaela wins this round!"
    play sound4 ding
    show cc792
    mil "Micaela wins!"
    play sound5 ding
    show cc793
    mil "Another medal for Micaela!"
    play sound6 ding
    show cc794
    mil "Micaela sets a new record!"
    play sound dingmultiple
    show cc795
    mil "MICAELA!" with hpunch
    stop music2 fadeout 7
    scene cc 104 with Dissolve(2.2)
    play music gymambience fadein 6
    d "*Panting*" with dis
    d "*Panting* F-Fuck... I can't..."
    d "*Panting* I can't lift another pound..."
    d "*Panting* She's too strong..."
    show cc 105
    mi "Well played, Dalia." with dis
    mi "You've improved a lot over the last year. I'm impressed!"
    d ". . ."
    show cc 106
    d "...You too, Micaela."with dis08
    d "Congratulations on the victory."
    show cc 107
    mi "I could only lift 20 more pounds than you during the squats competition!"with dis
    mi "That's insane! I'll have to train harder if I want to keep up with your progression!"
    show cc 108
    d "The only thing that counts is that you won and I lost every trial. 20 pounds, 50 pounds... Who cares? That doesn't matter."
    show cc 107
    mi "It matters when you consider that I weigh like 130 pounds more than you."
    mi "I'll admit that I've always been jealous of how you can be so strong while keeping such a slender body. You don't know how lucky you are!"
    show cc 108
    d "If you say so..."
    show cc 109
    mi "Well, I'll go get cleaned up. See you later, Dalia!"with dis
    d "Later..."
    show cc 110 with dis15
    pause
    mc "There you are!"with dissolve
    mc "I was looking for you!"
    d ". . ."
    play sound chair2
    show cc 111
    mc "*Sitting next to her* Holy fucking shit, did you really squat 350 pounds?!" with dis
    mc "You're a monster!"
    show cc 112
    d "Okay..."
    show cc 111
    mc "Huh? What's with the long face?"
    mc "You did amazing! Millie said you even beat your personal best, is that right?"
    show cc 112
    d "I don't know, maybe. I wasn't paying attention."
    show cc 111
    mc "Why are you so sad? Did you strain something?"
    show cc 112
    d "Don’t patronize me... I'm a fucking loser, and you know it."
    show cc 111
    mc "What?! Are you kidding me?!"
    mc "You lifted more than any man in the gym!"
    show cc 112
    d "I've been training every single day during the last year, just to try to win a single medal."
    d "And in the end, I didn’t win anything, like always..."
    show cc 111
    mc "Come on, who cares about those shitty medals? It's not even real gold."
    mc "And you say that as if you were the only one without one."
    mc "I didn't win a medal..."
    show cc 113
    mc "Kai and Nikolay didn't win a medal..."with dis08
    show cc 114
    mc "That woman didn't win a medal..."with dis08
    show cc 115
    mc "Chang didn't w–"with dis08
    mc ". . ."
    mc "W-Why do you have a medal?"
    show cc 116
    c "Oh, this?"with dis08
    c "I won it in the air guitar competition."
    show cc 115
    mc "T-The what...? Since when is there an air guitar competition?!"with dis08
    show cc 117
    c "I started teaching that class when I began working here last week."
    c "Thursdays at 7:30 PM. “Air Guitar with Chang the Czar.”"
    show cc 115
    mc "Um..."
    show cc 111
    mc "Okay, forget about Chang."with dis08
    mc "What I'm trying to say is that you did great today. If Micaela wasn't here, you'd have won every single trial."
    show cc 112
    d "Whatever..."
    show cc 119
    mil "Okay Dalia, time for your last trial."with dis
    show cc 118
    mil "Get ready!"with dis04
    show cc 112
    d "The MMA fight? I think I'm gonna pass."
    d "Micaela has humiliated me enough in front of everyone today."
    show cc 118
    mil "Nah, your opponent isn’t Micaela."
    show cc 121
    d "What? She's not?" with dis08
    show cc 120
    mil "Nope."
    mil "The MMA tournament was categorized by weight, and none of the participants were in Micaela’s weight range, so... she couldn't participate."
    show cc 121
    d "Then... who's my opponent?"
    show cc 120
    mil "Let me check..."
    show cc 119
    mil "Someone named... Brock."
    mil "Ah... yeah, I remember him. It's that guy who's always in the steam room."
    show cc 121
    d "A guy?"
    show cc 120
    mil "Yeah, but he weighs about the same as you."
    mil "Here at {i}PUMP IT{/i} we are committed to diversity, inclusion, and gender equality!"
    show cc 121
    d "Oh... yeah, I think I remember seeing him in spinning class."
    show cc 120
    mil "He talks a big game, but I've never seen him do anything noteworthy. He qualified for the finals by a whisker."
    mil "My money's on you!"
    show cc 122
    mc "Did you hear that?!" with dis08
    mc "The final isn't against Micaela!"
    mc "You can win this one!"
    d ". . ."
    show cc 123
    d "I can win this one."with dis04
    mc "Hell yeah!"
    d "I'll destroy this Brock dude."
    mc "To the octagon!"with hpunch
    show cc 119
    mil "Well we don't really have an octagon, we use the boxing room. So... the fighting area is more like a square. We don't have any professional equipment here."
    mc "To the square!"with hpunch
    show cc 121
    d "Actually, it's called a boxing ring."
    show cc 120
    mc "To the ring, then!"with hpunch
    stop music fadeout 4
    play music2 rain3 fadein 5
    show cc 124 with Dissolve(2.2)
    pause
    play sound punch
    play sound2 thunder
    show cc 125
    bro "HYAAAAAA!!!" with hpunch
    show cc 124
    gymm "Wow, did you see that?!"with dis
    gymm2 "He's so fast!"
    play soundlow applause2
    show cc 126
    bro "I call this... The Crested Crane pose."with dis
    gymm "*Clapping* He's so good!"
    kai "I taught him that!"
    show cc 127
    mc "*Massaging her shoulders* Okay, that was a pretty damn high kick, but there's no need to be scared, Dalia."with dis
    show cc 128
    d "I'm not scared."with dissolve
    show cc 127
    mc "Well you know what I mean, scared, nervous... Whatever it is that’s making you shake."with dissolve
    show cc 128
    d "I'm not shaking either! Are you trying to get on my nerves?!"with dissolve
    show cc 127
    mc "That's the spirit! Channel that anger into your opponent!"with dissolve
    show cc 128
    d "I can kick that thing too."with dissolve
    show cc 127
    mc "Good! Then you should start with a high kick, his own signature move! We’ll have the element of surprise in our favor, he won't see it coming."with dissolve
    play sound chair3
    show cc 129
    mil "Alright guys, let's end this last day of competition with a bang!" with dis
    mil "The last medal of this year is at stake!"
    mil "Kredon's Bantamweight title is decided..."
    play sound3 metalhit
    play music2b gym2
    stop music2 fadeout 1
    show cc129
    mil "NOW!"with hpunch
    scene cc 130
    mil "On my left, weighing in at 131 lbs... Brock Domen!"
    show cc 131
    mil "And on my right, weighing in at 125 lbs... Dalia Carter!"
    mc "Let's go Dalia! Kick his ass!"
    show cc 133
    bro "I was starting to think you wouldn't come, Dalia."
    show cc 132
    d "In your dreams."
    show cc 133
    bro "*Laughs* I heard you didn't even win a single medal in the fitness trials."
    bro "Isn't that kinda lame? I wonder what the hell you were doing up there everyday..."
    bro "Taking pictures of your ass to post on Instagram, I bet."
    show cc 132
    d "Shut the fuck up. I don't know about you, but I only come here to train."
    show cc 133
    bro "*Laughs* And yet you didn't manage to win anything? That's even sadder!"
    bro "Well at least you’re experienced at losing. Another defeat won't make much of a difference. Maybe you can convince them to give you a consolation prize, as the biggest loser?"
    show cc 132
    d "Can't wait to kick in that ugly face of yours."
    show cc 129
    mil "And the fight starts..."
    play sound boxingbell1
    show cc129
    mil "NOW!"with hpunch
    scene cc 134 with dis15
    gymm "Kill him!"with dissolve
    niko "дерись!"
    gymm2 "Destroy her!"
    play sound dodge
    scene cc 134b
    bro "HYAAAAA!{w=0.8}{nw}"with dissolve
    stop music2b
    play sound punch
    play sound2 bonebreak
    show cc135 with hpunch
    pause .2
    play sound3 fall
    play sound4 fall2
    scene cc 136 with dis12
    play music rain3 fadein 4
    pause
    mil "Um..." with dissolve
    mil "Brock?"
    mil "You dead?"
    bro ". . ."
    play sound boxingbell2
    show cc 129
    mil "Well, I guess Dalia won the fight!" with hpunch
    mil "Congratulations!"
    play soundlow applause2
    show cc 137
    d "What?" with dis08
    d "I... I won?"
    mil "Yeah!"
    d "I won..."
    play music2b romantic2
    stop music fadeout 10
    play sound chair3
    play sound4 chair1
    show cc 138
    d "[mc]! I won!" with hpunch
    d "I won!"
    d "Did you see that?!"
    mc "You bet I did!"
    mc "Holy shit, what a kick! And you were so fast!"
    play sound clothes2
    play sound3 chair3
    play sound5 fall2
    show cc 139
    d "*Jumping from the ring* Did you notice how I took the same stance we use in Eternum? Before the kick?"with dis08
    d "Did you?"
    show cc 140
    mc "Hell yeah!"with dis
    mc "I don't know any girl who can kick ass like you."
    mc "Congrats, Dalia."
    mc "I know it probably doesn't mean shit to you, but... I'm really proud of you."
    d ". . ."
    show cc 141
    d "*Kisses you*" with dis08
    mc "(Whoa!)"
    mc "(Where did that come from?)"
    menu:
        with dis
        "Kiss her back [dalia_pts]":
            show cc 142 with dis
            show screen heartbeat
            play sound beat
            $ dalia_points += 1
            pause .6
            mc "(Damn...)" with dis08
            mc "(She's been exercising and sweating for the past two hours, how the hell can she still smell so good?)"
        "Stand still":
            mc "(I... I wasn't expecting this. What am I supposed to do now?)" with dissolve
    show cc 143 with dis15
    pause
    mc "Wow... That was..." with dis08
    show cc 144
    d ". . ." with dissolve
    show cc145
    d ". . ." with dis12
    play sound musicstop
    stop music2b
    scene cc145b
    mi "I didn't know you were dating!"
    play sound5 punch
    play music2 sneaky4
    scene cc 146
    d "W-WHAT?!"with hpunch
    d "We're not! We're totally not!"
    d "Why do you say that?!"
    show cc 147
    d "This is just a misunderstanding!" with dis
    show cc 149
    mi "What do you mean?"with dis04
    show cc 148
    c "Why didn't you tell me, [mc]?!"with dis04
    show cc 149
    kai "I already knew, her mom told me. I’m her greatest confidante."with dis04
    show cc 148
    gymm "You two make a great couple!"with dis04
    show cc 147
    d "We're not dating!" with dis04
    d "We're just old friends!"
    d "And d-don't tell my mom!"
    show cc 149
    mi "But you kissed him!"with dis04
    show cc 147
    d "What? That stupid kiss? It's just my way of celebrating a victory!"with dis04
    d "It doesn't mean anything!"
    show cc 149
    mi "Really?"with dis04
    show cc 147
    d "Yeah! I kiss everyone when I win!"with dis04
    d "It just happened that [mc] was the first one I saw! It could have been anyone!"
    show cc 150
    d "Look!" with dis
    scene cc151 with dis15
    pause
    gymm2 ". . ."with dis12
    d ". . ."
    gymm2 ". . ."
    d ". . ."
    gymm2 ". . ."
    play sound clothes3
    show cc 152
    d "(F-Fuck, I can't do it.) Uhh... actually, I’m feeling a slight tickle in my throat." with dis
    d "*Coughs* Maybe it’s best if I don’t kiss anyone else..."
    stop music2 fadeout 7
    play music rain3 fadein 8
    bro "*Clears throat* EHEM." with hpunch
    bro "Attention, please!"
    show cc 154
    bro "Can you read that again, Millie?" with dis
    bro "Say it loudly, so everyone can hear you."
    show cc 153
    mil "Um... It says here that strikes to the throat of any kind are expressly forbidden."
    show cc 155
    d "What?"
    show cc 154
    bro "And that means that..."
    show cc 153
    mil "Since Dalia knocked out her opponent with an illegal hit, her victory is invalid, and she's disqualified."
    show cc 157
    d "Whaaat?!" with hpunch
    d "I didn't win, then?!"
    show cc 156
    mil "I'm sorry, Dalia... I’ve gotta give the medal to Brock."
    show cc 157
    d "You can't be serious! That is so unfair!"
    play soundlow applause2
    show cc 158
    gymm "Congrats, Brock!" with dis
    bro "Thank you, thank you..."
    bro "I'll be honest, I never doubted that I'd win this competition."
    bro "The road to the finals was difficult. I was expecting a tougher opponent in the last trial, but oh well... it is what it is."
    show cc 160
    bro "Look on the bright side, Dalia!"
    bro "At least you can spend another year without having to worry about where to put your medals!"
    play sound6 crowdlaugh
    gymms "*Laugh*"
    show cc 158
    bro "Can you believe that she didn't even know the rules? What a bimbo!"
    bro "Big ass, tiny brains, am I right?"
    show cc 159
    bro "*Imitating Dalia* [mc]! I won! I won! Did you see it!? Muah Muah *imitates kissing noises*"with dis08
    play sound7 crowdlaugh
    show cc 160
    gymms "*Laugh*"
    d "*Sobbing*"
    bro "*Laughs* Oh my god, is she crying?"
    bro "Come on, don't be sad, you little girl..."
    bro "Do you want a lollipop, Dalia? I'm sure it'll make you feel better. Seriously, just grow up."
    play sound run
    show cc 161 with dis15
    pause
    show cc 162
    mc "Dalia!"with dis
    show cc 163
    mc ". . ."with dis
    show cc 159
    bro "*Imitating Dalia* Did you notice how I took the same stance we use in Eternum?" with dis
    play sound7 crowdlaugh
    gymms "*Laugh*"
    menu:
        with dis
        "[gr]Say something to him\n(attack afterward)":
            show cc 164
            bro "*Imitating Dalia* Did you see it, did you see it?!" with dis15
            show cc 165
            mc "What the fuck is wrong with you, dude?"
            show cc 166
            bro "What do you want?" with dis
            show cc 167
            mc "Are you honestly happy winning like this?"
            mc "She kicked your ass up there. You couldn't even stand up."
            mc "How can you be so cocky after such a lame \"victory\"? If we can even call it that."
            show cc 166
            bro "I'm the lame one? Go tell that to that crybaby girlfriend of yours."
            bro "I had to put up with her acting all tough throughout the year, as if she was better than me. What gives her that right? She's just a loser."
            bro "Serves her right."
            show cc 167
            mc "Whatever you say, man, but she beat you. You're pathetic. Everyone in this room is stronger than you."
            show cc 166
            bro "Oh, please, are you including yourself in that statement? Because you couldn't hit me even if I was blindfolded and tied up in front of you."
            show cc 167
            mc "Of course I could."
            show cc 166
            bro "I have the reflexes of a feral cat."
            bro "You'd never be able to touch me, I can assure you."
            show cc 168
            bro "*Chuckles* Come on, try to hit me, big man. Right here."with dis08
            bro "I bet you..."
            play sound deception
            stop music fadeout 1
            show brockgray
            call screen qtebrock with dis04

        "Leave":
            jump posbrock
label brockwin:
    play music rain3
    play sound punch
    play sound2 punch
    play sound4 bonebreak
    play sound3 blood3
    scene cc 169 with hpunch
    pause .6
    $ punchbrock = True
    play soundlow slam
    play sound6 fall
    play sound fall2
    play sound6 chairmove
    show cc 170 with dis12
    bro "W-W-What the f..." with dis12
    gymm "Oh my god!"
    show cc 171
    mc "(Oh shit, I didn't want to hit him so hard.)" with dis
    show cc 172
    gymm2 "Holy fuck, that was amazing! How did you move so fast?!" with dis04
    show cc 173
    gymm "Did you see that punch?! WOW! He sent him flying like a ragdoll!" with dis04
    show cc 172
    niko "классный удар!" with dis04
    show cc 173
    mil "What the fuck, [mc]?! Now he's gonna sue us!" with dis04
    play sound thunder
    show cc 174
    c "Okay, okay, calm down everyone." with dis12
    gymm2 "Who are you?"
    c "Chang Wong, lawyer AND manager of Mr. [lastname]."
    c "I'm afraid you're overwhelming my client. All complaints and contract proposals must go through me first."
    show cc 175
    mc "*Whispering* Chang?" with dis04
    show cc 174
    c "*Whispering* No worries buddy, I’ve got this covered."with dis04
    c "*Whispering* You should go after Dalia, she seemed pretty shaken up."
    show cc 175
    mc "*Whispering* Thanks man, you're the best! I owe you one!"with dis04
    show cc 174
    c "*Whispering* Anytime, bro!"with dis04
    jump posbrock
label brocklose:
    play music rain3 fadein 1
    scene cc 168
    bro "...can't even get close."with dissolve
    bro "Hmm?"
    bro "What? Nothing?"
    show cc 166
    bro "As I thought. Come on, get the fuck out of here and stop wasting my time... pussy."with dis
    play sound7 crowdlaugh
label posbrock:
    if punchbrock:
        show cc 176 with dis17
        niko "Me need [mc] Saturday in Pitch. He fight. Many money. And woman." with dissolve
        c "Let's discuss this in my office."
        mc "(Chang's right, I should go after Dalia.)"
        mc "(Although...)"
    else:
        show cc 163
        mc "(What an asshole.)"with dis12
        show cc 162
        mc "(Bah, let's forget about him.)" with dis08
        mc "(I should go after Dalia.)"
        show cc 176 with dis17
        mc "(Although...)" with dissolve
    mc "(Knowing Dalia, maybe she prefers to be alone right now.)"
    mc "(But... on the other hand, maybe she'd appreciate some company. She was so happy when she thought she'd won... I mean, she even kissed me in the middle of her \"euphoria.\")"
    mc "Hmm..."
    menu:
        with dis
        "[gr]Go after her":
            mc "(I wonder where she is. Maybe she went home... or to the park.)" with dissolve
            mc "(Or...)"
            jump daliacove
        "Give her space\n[red][mt](Closes Dalia's path)":
            $ daliadontcove = True
            mc "(Going after her would just make things worse. She needs some space.)"with dissolve
            mc "(I'm sure she'll see things better in the morning, with a clearer head.)"
            mc "(Time to go home.)"
            $ daliapath = False
            $ daliau = False
            jump nightmare04



label daliacove:
    stop music fadeout 6
    show black with Dissolve(2.2)
    pause
    show screen afewhourslater with dis17
    pause
    if tellpassword:
        play music2 party fadein 7
        hide screen afewhourslater
        scene cd 1
        with Dissolve(2.2)
        pause
        gymm "Blake! Beer me, dude!"with dis08
        gymm2 "Here you go! Cold and bubbly!"
        gymm "Thanks, bro."
        mc "Holy shit!"
        show cd 0
        mc "(Look at this!)" with dis12
        mc "(I wasn't expecting a whole beach party here! I guess that’s one way for Dalia to get over the competition.)"
        mc "(From what she told me, I assumed it was gonna be a quiet cove.)"
        mc "(There's a pretty good vibe here, though.)"
        show cd 0b
        mc "Well, well, well..."with dis12
        mc "What do we have here?"
        mc "You forgot to tell me that you threw parties in your \"private\" server, didn't you?"
        d ". . ."
        mc "Hello? Earth to Dalia."
        show cd 0c
        d ". . ." with dissolve
        mc "Hey, I won't complain, though. It's a really nice setup you have here."
        mc "Who are all these people, though? Friends from...?"
        d ". . ."
        mc "Cat got your tongue or what?"
        bro "Welcome to the party!"
        show cd 0f
        mc "*Turning around* Huh?"with dis
        mc "What? What the fuck are you doing here? Did you seriously invite him too?"
        show cd 0g
        bro "I'm the one who's throwing the party."
        bro "But don't worry, I'll let you stay."
        if punchbrock:
            show cd 0h
            bro "That fucking punch of yours still hurts even in Eternum, not gonna lie..." with dis
            show cd 0g
            bro "But no worries bro, I don't hold grudges. It was just a lucky hit, anyway..." with dis
        show cd 0f
        mc "What are you talking about? Do you know the password too?"
        show cd 0g
        bro "Of course I do. You told me yourself."
        show cd 0f
        mc "What? No, I didn't."
        show cd 0g
        bro "Of course you did. Don't you remember? In the fitness room, with that friend of yours with that shirt of Micaela."
        show cd 0f
        mc "What?! You were eavesdropping on us?! You're a fucking asshole!"
        mc "That was private!"
        show cd 0g
        bro "It's not as if you were whispering, bro."
        bro "Having a private server in Eternum and not sharing it is a very selfish thing, after all. I thought you were inviting everyone in the gym to come."
        bro "Now it's so much more fun!"
        show cd 0f
        mc "(Fucking idiot...)"
        show cd 0c
        mc "*Turning around* O-Okay, I can explain."with dis
        bro "Yo guys, let's turn up that music! I want all of Eternum to hear us!"with hpunch
        mc "I didn't tell him, I swear!"
        mc "But he was spying on me when..."
        show cd 0d
        d ". . ." with dis12
        d "Don't talk to me ever again."
        mc "W-What?"
        show cd 0e with dis
        mc "Dalia!" with dis08
        mc "Oh... FUCK!"
        mc "(I really screwed the pooch this time...)"
        show cd 1
        mc "*Sighs* (I guess I'll just log off for today...)"with dis15
        mc "(She seemed really upset...)"
        mc "(And to be fair, she has reasons to be.)"
        mc "(Anyway... I'll apologize after she cools off. This is just the bathtub thing all over again.)"
        mc "(Tomorrow's another day...)"
        $ daliapath = False
        $ daliau = False
        jump nightmare04
    play musicb waves2 fadein 7
    hide screen afewhourslater
    scene cd 1
    with Dissolve(2.5)
    pause
    show cd 2 with dis2
    pause
    d ". . ."with dis08
    show cd 3
    d "(Today the sea is very calm.)"with dis15
    d "(I wish it was always like this... It almost looks like a pool.)"
    d ". . ."
    d "*Sighs*"
    d "(I'm pathetic.)"
    show cd 4 with dis17
    pause
    play sound sand
    stop musicb fadeout 15
    play music2 cove fadein 5
    show cd 5 with dis15
    pause .2
    mc "Did you know that sex is a death sentence for octopuses?" with dis
    mc "After the mating is done, it's game over for both of them."
    show cd 6
    mc "The male wanders off to die, and the female guards their eggs so obsessively that she even stops eating."with dis
    mc "When the eggs hatch, her body undergoes a cascade of cellular suicide until she dies as well."
    mc "Quite a sad fate, huh? Nature sure can be cruel."
    d ". . ."
    show cd 8
    d "How did you know where I would be?"with dis08
    show cd 7
    mc "Well, you told me yourself that you liked to come here when you wanted to relax or be alone."
    mc "I assumed I'd find you here."
    show cd 8
    d "When I told you the password, you said that you wouldn't come here without asking for my permission first."
    show cd 7
    mc "That’s true. Guilty as charged!"
    mc "I just thought that... after what happened, you'd like to have some company."
    show cd 8
    d "I don't wanna talk about it."
    show cd 7
    mc "No one's forcing you to!"
    mc "I was just telling you some awesome trivia about the fascinating world of octopuses. Technically, it was you who interrupted me and my fun facts."
    show cd 9
    d "*Snorts*" with dis04
    show cd 10
    d "True. I'm sorry."
    d "Please continue. Enlighten me."
    show cd 9
    mc "Thank you."
    mc "You see... although it's commonly said that they have 8 legs, in fact they have 6 arms and 2 legs."
    mc "If they are desperately hungry, they can eat their own arms, which will grow again after some time."
    mc "They have 3 hearts, and their blood is blue!"
    show cd 10
    d "Oh, so they're true blue royalty, huh?"
    show cd 9
    mc "Exactly!"
    mc "Not to mention, they're also said to be the most intelligent animal of all invertebrates."
    mc "They say that if octopuses had longer life spans, they would be the dominant species in the world."
    show cd 10
    d "Wow, that's scary."
    show cd 9
    mc "Right? We'd better be on the watch. You never know when they could attack... Plus, you ever see all that tentacle porn online? That shit’s not something to mess around with."
    show cd 10
    d "*Laughs* How the hell do you know all this stuff?"
    show cd 9
    mc "I've always liked the sea and marine life."
    mc "Do you remember when we went to the Aquarium?"
    mc "When we were like... 7?"
    show cd 10
    d "I do!"
    d "Mom took us there for my birthday."
    if divinationflashback:
        d "I remember seeing the sharks and thinking..."
        show cd 6
        mc "\"{i}One day I'll have my own boat! {/i}\""with dis12
        mc "\"{i}I'll navigate the seven seas and discover all the sea monsters that are hiding across the world! {/i}\""
        mc "\"{i}I'm Dalia the Explorer! {/i}\""
        show cd 11
        d "H-How do you remember that?" with dis12
        d "I thought you said you barely remembered your time in Kredon..."
        show cd 12
        mc "I was playing with Penny and Luna the other day and we used a device that dug up some old memories."
        mc "*Chuckles* And it's hard to forget your \"Dalia the Explorer\" phase."
    else:
        d "I remember seeing the sharks and thinking that one day I'd explore the seven seas with my own boat."
        show cd 9
        mc "I do remember your \"Dalia the Explorer\" phase!"
    mc "You kept repeating it all the time."
    show cd 10
    d "*Sighs* Yeah..." with dis04
    d "That was fun."
    d "I miss those carefree days when my only concern was what Mom would give us for dinner."
    show cd 9
    mc "*Chuckles* If it had been up to me, I'd have only eaten candy and potato chips all day."
    mc "Good thing that’s changed."
    show cd 10
    d "Yeah..."
    show cd 14
    d "Look, [mc]..." with dis12
    d "I appreciate you coming here. I really do."
    d "But... you can go now, don't worry about me."
    d "I mean, I know what you're thinking."
    d "\"This drama queen’s overreacting to a stupid competition that has 0 real-world value.\""
    d "\"If she'd had any {i}real{/i} problems during her lifetime, she wouldn't be crying over something so trivial.\""
    d "\"What a spoiled little girl.\""
    show cd 15
    mc "Wow, everything you just said was wrong."with dis12
    mc "I wasn't thinking that at all. I thought you knew me better than that, Dalia."
    mc "That competition was important to you, and that's all that matters."
    mc "I've been hearing you waking up at 5 AM every morning to go train."
    mc "I've seen your folders full of different gym programs."
    mc "I've even seen your sneakers’ soles get completely worn down and reduced to shreds from overuse."
    mc "No one likes to lose. After so much effort, I'd be pissed too."
    mc "It's totally normal."
    show cd 14
    d "It's..." with dis
    d "It's not even about the damn competition."
    d "It's just that... being good at sports is the one thing I have."
    d "I'm not funny. I'm not particularly clever or cunning, like Mom. I don’t have Penny’s supermodel-tier looks. I don't have any talent for music or art... I'm average at everything."
    d "The one thing I had was being... \"the fit girl.\""
    d "And if I can't even get that right..."
    d "Then I'm nothing."
    show cd 13
    mc "(Damn, I didn't know Dalia was so insecure deep down.)"
    mc "(It hurts to see her like this.)"
    show cd 15
    mc "You're unique and special, Dalia. You don't have to be the best at something to be somebody."with dis
    mc "Look at me! I'm the most average dude you'll ever see! I don't have any real talent, and yet, here I am."
    show cd 14
    d "That's not true."with dis
    d "You're a lot smarter than me. You got offered a full scholarship to participate in Kredon’s student exchange program."
    d "You started playing Eternum a few weeks ago, and you already managed to surpass me and learn a secret magic no one knows anything about."
    d "You're special..."
    play sound sand
    show cd 16
    d "And I'm not." with dis12
    d "Let’s just stop arguing about it and accept it."
    d "Acknowledging and accepting it are the first steps t–"
    play sound snow2
    show cd 17
    mc "*Getting on top of her* Okay, that's enough!"with dis08
    d "W-What are you doing?!"
    show cd 18
    mc "You're done talking nonsense for today."with dis
    mc "You're amazing, Dalia. Everything about you is amazing. And we're not leaving this beach until you accept it."
    show cd 19
    d "Okay, okay..."with dis04
    show cd 18
    mc "No, not okay. I want you to say it out loud."with dis04
    mc "\"I'm amazing.\""
    show cd 19
    d "Oh come on, what are we, 5?"with dis04
    d "Don't make me do it."
    show cd 18
    mc "I don't know about you, but I can stay here all day. This pose is quite comfortable."with dis04
    show cd 19
    d "You're kinda crushing my stomach."with dis04
    show cd 18
    mc "More reason to do what I say, then."with dis04
    show cd 19
    d "*Sighs* What the hell do you want?"with dis04
    show cd 18
    mc "\"I'm amazing.\""with dis04
    show cd 19
    d "*Sighs*"with dis08
    d "{size=25}I'm amazing..."
    show cd 18
    mc "Yes, you are."with dis08
    mc "You're funny, you're generous and kind, and you're the strongest girl I know."
    mc "You're one of my favorite people to spend time with, and one of the sexiest women I've ever met."
    mc "Your face looks beautiful at any time of the day, and you have an absolutely killer body."
    mc "Oh..."
    mc "And you're a pretty good kisser too."
    play sound snow2
    show cd 20
    d "*Snorts* Shut up! Haha!"with dis
    d "Don't remind me of that!"
    show cd 22
    mc "*Chuckles* Hey, it's true!" with dis15
    show cd 21
    d "*Chuckles* That was so embarrassing! I don't know what got into me. God, did you see the looks on their faces?"
    d "I wish the ground swallowed me up at that moment!"
    show cd 22
    mc "Hey, I actually thought..."
    mc "It was a good kiss."
    show cd 21
    d "Yeah, I guess it was..."
    show cd 24
    d "Thank you [mc]."with dis12
    show cd 23
    mc "For what?"with dis04
    show cd 24
    d "Talking to you made me feel better."with dis04
    d "It always does..."
    d "I guess you can add that to the list of your many talents."
    show cd 23
    mc "I have far too many talents. I’m gonna have to start carrying a list around."with dis04
    show cd 24
    d "*Chuckles* Oh, really?! Now you're showing your true colors!"with dis04
    d "Your humbleness from before was all a facade, wasn't it? “I’m the most average dude you’ll ever see.” You liar!"
    show cd 23
    mc "Oh yeah, totally. Now that you’ve accepted that you're amazing too, I don't have to pretend anymore."with dis04
    mc "I'm pretty damn awesome, let's be honest."
    show cd 24
    d "*Laughs* Fuck off."with dis04
    show cd 23
    mc "*Laughs*"with dis04
    show cd 1 with dis2
    stop music2 fadeout 9
    play music waves2 fadein 10
    d "Well, I guess we should get going now." with dissolve
    d "I think it's pretty late."
    if punchbrock and daliabet:
        mc "Oh, before we leave, I wanted to ask you something..."
    else:
        mc "Yeah, I guess it is."
        mc "I'm really hungry."
        d "I hope you are, because I'm making dinner tonight. And I'm serving Dalia-sized portions!"
        mc "Nice!"
        $ daliapath = False
        $ daliau = False
        jump nightmare04
    mc "Do you remember our bet in the Semper Invicta server?"
    show cd 27
    d "Oh man, hold your horses bud!" with dis15
    d "Don't you try to take advantage of this situation!"
    d "Thanks to you I'm not feeling down anymore, so you won't be able to have your way with me in a moment of weakness, sorry."
    show cd 26
    mc "Oh I know, that's why I'm bringing it up."
    show cd 28
    d "Look, I'm very tired, and my shorts are full of sand, so I'm not in the mood to fight with you right now."
    d "Maybe... another day."
    show cd 26
    mc "You should get rid of the sand if it’s making you uncomfortable."
    show cd 27
    d "I’m not gonna fight you, [mc]."
    d "Our... \"bet\" will have to wait."
    show cd 26
    mc "I know! I just want to tell you something. Trust me, you're gonna love it."
    show cd 27
    d "Why are you so pushy? You don't have a chance against me anyway."
    show cd 26
    mc "Ahhh, it's nice to see you regaining self-confidence."
    d ". . ."
    show cd 29
    d "What are you concocting in that pervy little brain of yours?" with dis12
    mc "I'm innocent, I swear."
    d "Of course..."
    show cd 30
    d "Fine, fine, let me “get comfortable.”"with Dissolve(1.3)
    d "It was a bad idea to sit down on the sand with pants on, anyway."
    mc "That's exactly what I'm saying."
    play sound clothes3
    show cd 31 with dis15
    $ unlock_look("dalia", 9)
    mc "(Jesus...)" with dissolve
    show cd 32
    mc "This bikini looks good on you, Dalia." with dis
    d "Thanks. I knew I liked it beforehand because I have the exact same model in the real world, so I bought it here as well."
    mc "You’re definitely looking more comfortable now."
    d "Oh, for sure..."
    play sound sand
    show cd 33 with dis15
    mc "(Oh my fucking god, those hips...)"with dissolve
    mc "(Those abs... is it bad that I want to lick them?)"
    show cd 34
    d "Okay, so... what did you want to tell me? I'm all ears."
    show cd 33
    mc "Ah, yeah."
    mc "Y’know that asshole from the gym, Brock? The guy you unjustly lost to?"
    d "Mm-hm."
    mc "After you left, we had a little argument, he provoked me, and..."
    mc "I might have punched him in the face."
    mc "Maybe a bit too hard."
    show cd 34
    d "*Snorts* Seriously?"
    show cd 33
    mc "Yeah. I think he fell unconscious."
    show cd 34
    d "Hah! Serves him right. Nice one!"
    show cd 33
    mc "Yeah, the guy was a total idiot."
    show cd 34
    d "Definitely."
    d "But... I fail to see the connection between this and our bet, though."
    show cd 33
    mc "Well, that's the thing... {i}Technically{/i}, you lost against him in combat."
    mc "And {i}technically{/i}, I beat him shortly after."
    mc "Therefore, by the transitive property, I beat you too."
    show cd 34
    d "*Chuckles* Excuse me? That's not how it works at all."
    show cd 33
    mc "I'm pretty sure it's valid. We didn't specify the rules."
    show cd 34
    d "Yeah, we didn't, but it's common sense."
    d "If I had made out with my sister yesterday, does that mean you could say that you’ve kissed Penelope too?"
    show cd 33
    mc "You made out with Penelope yesterday?!"
    show cd 34
    d "*Laughs* Of course not! I'm just trying to show the flaw in your logic."
    show cd 33
    mc "Okay, okay... whatever you say..."
    mc "*Chuckles* It was worth a try, though."
    mc "I was hoping I didn't have to punch that pretty face of yours in order to win, but I guess I'll have to do it. You’ve left me no choice."
    mc "Unless you find another technicality, of course..."
    show cd 34
    d "You're the one who's trying to find loopholes in our bet."
    show cd 33
    mc "*Chuckles* That depends on how you look at it."
    mc "Anyway, let's go home."
    mc "I loved spending some time with you in your server, Dalia. Thanks for letting me visit."
    d ". . ."
    show cd 34
    d "Okay... let's do it."
    show cd 33
    mc "The Exit Portal inside the cave is the only one around? Have you ever explored the rest of the island?"
    show cd 34
    d "I'm talking about the bet. Let's do it."
    show cd 33
    mc "The..."
    $ renpy.music.set_volume(0.4, channel='music3')
    play music3 covesexy fadein 8
    stop music fadeout 10
    mc "W-Wait, what?"
    show cd 34
    d "Isn't that what you wanted?"
    show cd 33
    mc "Um... y-yeah..."
    play sound sand
    show cd 35
    d "*Undoing her bikini* Never let it be said that Dalia doesn't honor her bets." with dis12
    if not rotundafail:
        d "The other day I bet and won 100 eternals in the rotunda from Jasticus' trainer."
    d "Sometimes you win, sometimes you lose..."
    play sound2 sand
    show cd 36
    mc "*Standing up* Did this really work? Or am I dreaming?"with dis12
    show cd 37
    d "Everything you did for me today really meant a lot. Coming to the competition, giving me that pep-talk before the trials, cheering me on and cheering me up..."with dis04
    d "You came looking for me when I was at one of my lowest points, and you helped me regain my self-esteem."
    d "And... well, that kiss honestly wasn’t half bad."
    d "So... as a thank you for everything... I'm choosing not to overthink your definition of \"beating me in a fight.\""
    show cd 38 with dis17
    mc "My god..." with dis08
    mc "You're fucking perfect..."
    show cd 39
    d "You’re saying so many nice things today... but well, I can't say I don't like being praised..."with dis04
    play sound sand
    show cd 40
    if dalianaked:
        d "I know you already saw me naked, but I hope this can still get you in the mood." with dis12
    else:
        d "Well... I hope this is enough to get you in the mood."with dis12
    d "It's gonna be difficult to do my part otherwise."
    show cd 41
    mc "I doubt that'll be a problem..."
    if dalianaked:
        show cd 40
        d "At least this time I'm getting naked for you voluntarily, not accidentally. You creep."
        show cd 41
        mc "I thought it was clear that that was just a huge misunderstanding..."
        show cd 40
        d "*Giggles* I still have my doubts..."
    show cd 42 with dis15
    d "*Starts to slowly open your fly*"with dis08
    mc "(Oh... fuck yeah!)"
    play sound zip
    pause .2
    play sound2 clothes3
    show cd 43 with dis17
    d "What the..." with dissolve
    d "Jesus Christ..."
    d "I wasn't expecting..."
    d "T-That..."
    show cd 44
    mc "*Taking off your shorts* I mean..."with dis15
    play sound clothes3
    show cd 45
    mc "You made me so fucking horny, Dalia. Do you see how hard you made me?"with dis12
    mc "I’m like a rock. Couldn't help it. Your tits, your ass, your abs... the entire package."
    show cd 46
    d "Still, that was way too fast. Did you get hard during our sincere and emotional exchange?"with dis04
    show cd 45
    mc "Of course not... only once you took off your pants. Your tummy is way too sexy."with dis04
    show cd 46
    d "I'll choose to believe you..."with dis04
    d "I don't want to dirty our best memory together."
    show cd 45
    mc "Dirty the memory? We're only making it better..."with dis04
    show cd 46
    d "Yeah, I’m sure we’re making it better for you."with dis04
    d "Anyways..."
    d "I should probably start before this... monster starts going down."
    show cd 45
    mc "I don't think that's gonna happen..."with dis04
    mc "Take your time... I’m not in a rush."
    show cd 47
    d "*Gets close to you*" with dis15
    mc "(Oh fuck yeah...)"
    d "(Jesus, this thing looks huge up close... and the smell...)"
    show cd 48
    mc "You sure you can take it?" with dis
    show cd 49
    d "Of course."
    show cd 48
    mc "Is it making you horny?"
    show cd 49
    d "N-no!"
    show cd 48
    mc "You're in denial today, Dalia..."
    show cd 50
    d "I'm already starting to regret agreeing to this."with dissolve
    mc "Your mouth says that, but your eyes say otherwise..."
    d "Shut up, idiot."
    show cd 51
    blank "{i}She starts licking the head of your penis."with dis12
    mc "Oh, yeah..."
    show cd 52
    blank "{i}Gently kisses and licks you along the length of your cock."with dis12
    show cd 51
    mc "(I can feel how her breathing keeps speeding up...)"with dis12
    show cd 52
    mc "You're driving me insane, Dalia..." with dis12
    mc "Stop teasing me... Put it inside your mouth, please..."
    d "I thought you said you weren’t in a rush..."
    show cd 51
    mc "I might have spoken too soon..."with dis12
    show cd 53 with dis12
    mc "Oh, y-yes..." with dissolve
    show cd 51
    d "Does it feel good?" with dis12
    show cd 53
    mc "It feels amazing..." with dis12
    show cd 54
    d "*Slight moan*"with dis12
    mc "Oh fuck yeah, baby..."
    show cd 55
    mc "(Oh my god, Dalia's sucking my cock...)"with dis12
    mc "(This is like a dream come true...)"
    show cd 56
    mc "Oh... fuck, your mouth is so warm..." with dis12
    mc "That’s a good girl..."
    show cd 57
    mc "(God, I'm stretching her little mouth so much...)"with dis
    show cd 56
    mc "That's it, Dalia..."with dis
    mc "Deeper..."
    show cd 57
    mc "Make it wet..."with dis
    show cd 58
    mc "Now, let's try that ability of yours we talked about all those weeks ago, shall we?" with dis12
    d "Mmmm...?"
    play sound blow4
    play sound2 blow4
    show cd 59
    blank "{i}You gently push Dalia's head further onto your cock."with dis12
    d "Mmmph!"
    mc "Oh f-fuck, yes!"
    play sound3 blow5
    show cd 60
    d "*Recovering her breath* AAahh..." with dis12
    mc "Holy shit, so it was true, huh? No gag reflex..."
    d "*Panting* I m-might have underestimated the size..."
    mc "Is it too much for you?"
    d "*Panting* Of course not, but..."
    d "W-Well, I s-still have to breathe, you know?"
    d "Are you trying to kill me?"
    mc "Not at all..."
    mc "I'll let you set the pace... Be as greedy as you want."
    scene cd 56
    d "Hmmmph..." with dis12
    mc "Oh yeah... that's a good girl..."
    $ renpy.music.set_volume(0.1, delay=5.0, channel='music3')
    play music blowjob2 fadein 5
    show daliablow1 with Dissolve(2.5)
    mc "Ohhhh Jesus..."with dis08
    mc "(She's taking it so fucking deep...)"
    mc "(God, I can feel the tip of my cock slipping down her throat...)"
    mc "(And yet, she keeps taking it in and out without a single gag...)"
    d "*Moans*"
    mc "H-Holy shit, Dalia, you're a fucking natural..."
    mc "It’s so tight... almost feels like a pussy..."
    mc "Ahhh..."
    mc "Your throat’s squeezing me so much..."
    mc "Y-You're enjoying this too, aren't you?"
    d "Mmmmhmm..."
    mc "That’s what I thought... You dirty girl..."
    pause
    mc "Come here, I wanna fuck your juicy mouth..."with dissolve
    d "*Moans*"
    mc "That’s it..."
    play music2 blowjob4 fadein 5
    stop music fadeout 5
    scene black
    show daliablow2 
    with dis2
    mc "A-A-Aaaahh f-fuck yes...!" with dissolve
    mc "Oh my god, Dalia...!"
    mc "(It slides in so easily... her throat feels tight, but there’s no resistance...)"
    d "Mmmm...!"
    scene black
    show daliablow3 
    with dis17
    mc "Ahhh...." with dissolve
    mc "You're basically drooling, Dalia... You like my cock that much?"
    d "Mmmph..."
    mc "You're doing an amazing job..."
    mc "Oh god..."
    mc "If you wanna stop, just give me a sign, babe..."
    d "Mmm...!"
    mc "(At first I thought she was trying to prove something, but looking at her face I can tell she's enjoying it...)"
    mc "Aaaahhh..."
    mc "Fuck, I don't think anyone could take it so deep and so fast..."
    scene black
    show daliablow4 
    with dis17
    mc "Oh f-fuck yeah..." with dissolve
    mc "Do you like getting your mouth fucked, Dalia?"
    d "Hmph... mmph... mmph..."
    mc "That’s it, work all that cum out..."
    mc "(And her tongue gliding on the underside of my dick feels too good, even if it barely has space to move...)"
    pause
    mc "Oh g-god... I think I'm gonna cum..."with dissolve
    mc "I can't hold it...!"
    stop music2
    play sound4 blow1
    play sound6 blow4
    scene cd 60b
    d "*Pulls away and takes several breaths* F-FUCK!" with dissolve
    play sound snow2
    play sound3 sand
    scene cd 61
    d "*Lies back on the sand* J-Jesus...!" with dis08
    d "*Panting* T-Too much... d-dick... N-Need... oxygen!"
    mc "Are you okay?"
    d "*Panting* Fuck yeah, I am..."
    d "It's just that... t-that thing is... too big..."
    d "I couldn't fucking breathe... How do they do that shit in porn!?"
    play sound sand
    show cd 62
    mc "*Getting on top of her* Oh shit, Dalia..."with dis08
    mc "You have no idea how close I am..."
    show cd 63
    d "Oh, that's too bad... poor baby [mc]..."
    show cd 62
    mc "My balls are about to explode..."
    show cd 63
    d "Stop groping me!"
    show cd 62
    mc "Your boobs are fantastic, did I ever tell you that?"
    show cd 63
    d "Never, not even once."
    show cd 65b
    mc "*Pinching her nipples* And your hard nipples give you away – you're horny as fuck..." with dis
    show cd 64
    d "*Giggles* Shut up!"with dis
    show cd 65
    mc "But it's true... isn't it?"
    show cd 64
    d "Perhaps."
    show cd 65
    mc "I want to cum on your pretty face, Dalia..."
    d ". . ."
    show cd 64
    d "{size= 22} Cum in my mouth..."with dissolve
    show cd 65
    mc "I'm sorry, what did you just say?"with dis04
    show cd 64
    d "Cum{w} in{w} my{w} mouth."
    show cd 65
    mc "Would you like that, you pervert? Are you hungry for some cum?"
    show cd 66
    d "Please..." with dis15
    show cd 67
    d "I want you to release your seed in my little mouth..."with dis12
    show cd 66 with dis12
    d "*Whispering* All of it..."with dis
    d "Pretty please..."
    d "Haven't I done such a good job?"
    scene cd 67
    mc "(Oh my god...)"with dis
    mc "Open up for me, babe..."
    play music2 blowjob2 fadein 2
    show daliablow5 with dis17
    blank "{i}Slightly opens her mouth to let your dick in." with dissolve
    mc "Oh, yeah, that's it..."
    d "Mmm..."
    mc "Ahh..."
    mc "(Her lips wrap around me like a second skin...)"
    mc "Oh god, go faster, Dalia..."
    mc "Take it all in..."
    stop music2 fadeout 2
    play music blowjob2 fadein 3
    scene black
    show daliablow6 
    with dis15
    mc "AAagh... yeah...!"with dissolve
    d "Mmmph... mmmph... mmph..."
    mc "Oh yeah..."
    mc "You want it so bad, don’t you?"
    d "*Moaning* Mmmmh..."
    mc "You drive me crazy when you look me in the eyes like that..."
    d "Mmmm..."
    mc "F-Fuck, I'm gonna cum so much..."
    mc "Are you sure you can take it?"
    d "Mm-hmmm...."
    stop music fadeout 2
    play music2 blowjob4 fadein 3
    scene black
    show daliablow7
    mc "*Grabbing her head with both hands and taking control of her movement* AAaahhh... fuck!" with dis15
    mc "Oh... D-Dalia..."
    mc "(Holy shit, I can feel the back of her throat with each thrust...)"
    mc "Oh god, I'm cumming..."
    mc "I'm cumming!!!"
    stop music2
    play sound cum1
    play sound2 cum2
    play sound3 cum3
    scene cd 68
    mc "*Burying your cock balls-deep into Dalia's mouth* AAAAAArgh...!" with hpunch
    play sound4 cum3
    d "Gggh...!"with hpunch
    play sound5 cum3
    d "Ghhhh...."with hpunch
    play sound6 cum3
    mc "*Still cumming* Aaahhh..."with hpunch
    play sound blow4
    show cd 69
    mc "Jesus fucking Christ..." with dis15
    mc "I came like a horse... Are you okay?"
    d ". . ."
    play sound swallow
    show cd 70
    d "*Swallows*" with dis
    d "Mm-hm..."
    mc "Good girl..."
    stop music3 fadeout 7
    play music waves2 fadein 7
    show cd 71 with dis2
    d "*Wipes off her mouth* God..." with dissolve
    d "Strangely, it tastes exactly like I thought it would..."
    show cd 72
    mc "Well, well, well... so you openly admit having fantasized about how my cum tastes, huh...?" with dis12
    show cd 74
    d "Oh, shut up!"with dis15
    show cd 73
    mc "But seriously though, that was... unbelievable!"
    show cd 74
    d "By the amount of... jizz you just dropped in my tummy, I could tell you enjoyed it, yeah."
    show cd 73
    mc "My god, Dalia."
    mc "You can add this to your list of talents."
    show cd 74
    d "*Chuckles* Oh, yeah, it'd look very good on my resume."
    show cd 73
    mc "*Laughs* I'd hire you if that was part of the interview process."
    show cd 74
    d "Anyway, this was... entertaining... but we’ve gotta go now."
    d "I'd leave you here to recover, but this is still my private server! No one can be here without me."
    show cd 73
    mc "No worries, I have no interest in coming to this server if you're not on it..."
    show cd 74
    d "Thank you..."
    d "Well okay, let's go. I wanna go for a run before having dinner."
    show cd 73
    mc "Running? Didn't you just come back from the competition?!"
    show cd 76
    d "*Standing up* I’ve gotta start training NOW if I want to beat Micaela next year!" with dis15
    d "No one's gonna stop me!"
    mc "Hell yeah!"
    mc "(I'm glad she regained confidence in herself.)"
    mc "(God, that ass, though. I need to see that bouncing on top of me one day...)"
    show cd 1
    mc "You know, this was one of the best experiences of my life. We should definitely do this again sometime." with dis2
    d "Never gonna happen again."
    mc "You wanna bet? I could return the favor this time..."
    d "I'm not making any bets with you ever again either."
    mc "Aw..."
    d "And if you talk about what happened here with anyone after we leave this server, I'll murder you."
    d "I swear to god, I'll do it. I'm not kidding."
    mc "I'll k-keep that in mind."
    mc "Can I at least hold onto it in my memories?"
    d "Um... Okay, but make it a hazy memory."
    mc "*Chuckles* Fair enough."
    $ daliablowjob = True


label nightmare04:
    stop music fadeout 7
    stop music2 fadeout 7
    stop music2b fadeout 7
    show black with Dissolve(3)
    pause
    show screen afewhourslater with dis17
    pause
    hide screen afewhourslater with dis17
    play musicb twinkle fadein 50
    mc "Hmmm..." with dis08
    mct "This fucking bed is way too hard to sleep on..."
    mct "I’ve gotta ask Nancy to change the mattress."
    scene ca 1 with Dissolve(3)
    mc "(Hmm?)" with dis08
    mc "(Since when do I have a...)"
    show ca 2
    mc "*Sitting up* (What the fuck...)" with dis15
    mct "Why am I naked?"
    mct "This table is freezing! I feel like my balls are gonna get stuck to it!"
    show ca 4 with dis12
    pause
    mc "*Reading the blackboard* (Corpse #1, brain.)"with dissolve
    mct "Corpse #2, heart and wounds. Cadaveric state..."
    mct "Hmm?"
    mct "Wait, is this a..."
    show ca 5 with dis15
    pause .5
    mc "*Hyperventilating*"with dis
    mct "O-Okay, what the hell is going on..."
    mct "T-That's a corpse!"
    mct "Why the fuck am I in a morgue?!"
    show ca 4
    mct "Am I supposed to be \"corpse #1\"?!"with dissolve
    show ca 3
    mc "*Hyperventilating* (Okay, calm down, [mc].)" with dis
    mct "I'm sure all this has a perfectly logical explanation."
    mct "I must be spending too much time on Eternum’s horror servers, that's all. What's the last thing I remember?"
    mct "Think..."
    mct "I had some dinner, I went to sleep..."
    show ca 7
    mct "Then I woke up and..." with dis12
    play sound fallkitchen
    show ca 8
    mc "F-FUCK!!!" with hpunch
    lad "Will you help us?"
    mc "W-What?!"
    mc "Who the hell are you?!"
    lad "The love of your life is about to die."
    mc "W-What?"
    show ca 6
    lad "In front of you, there is a button."with dis12
    lad "If you press it, there is a 1-in-7 chance to save her life."
    lad "However, there is also a 6-in-7 chance that pressing the button will kill you."
    lad "Do you press the button?"
    mc "What the fuck are you talking about..."
    lad "Do you press the button?"
    mc "Where am I?!"
    lad "Do you press the button?"
    mc ". . ."
    menu:
        with dis
        "[gr]Yes":
            $ buttondilemma = True
            mc "I g-guess."with dissolve
            lad "Why?"
            mc "Why? Well... Even if I might die..."
            mc "There's still a chance, isn't there?"
            mc "I'd do anything to protect the woman I love. Knowing that I had even the smallest chance to save her, and not trying... I’d probably hate myself for the rest of my life."
        "No{#0.4,button}":
            mc "I g-guess not." with dissolve
            lad "Why?"
            mc "Why? Well... there’s mathematically an... 86\% chance I'll die if I press that button."
            mc "There’s only a 14\% chance of us both living."
            mc "What's the point of both of us dying? I’m sure she wouldn’t want me to sacrifice myself for her sake."
    lad ". . ."
    prof "[mc]."
    mc "What?"
    prof "[mc]!"
    mc "What the..."
    play sound risingshort
    pause 1.1
    play sound2 schoolbell
    play sound4 chairmove
    stop music
    stop musicb
    pause .14
    play sound3 slam
    show ca 9 with flashfaster
    play music2 rain3 fadein 5
    if buttondilemma:
        mc "I'd press the button, yes!" with hpunch
    else:
        mc "I wouldn't press the button, of course not!" with hpunch
    mc "PLEASE!"with hpunch
    mc ". . ."
    show ca 10
    mc ". . ." with dis12
    show ca 11
    pause
    show screen fridaycorner
    mc "Oh... uh... Hi, Mr. Keating."with dissolve
    show ca 12
    prof "It's the second time you’ve fallen asleep in one of my classes, [mc]!"
    prof "All your classmates have already left."
    show ca 11
    mc "I'm so sorry professor, it's just that... I haven't been sleeping that well lately."
    mc "(Jeez, what a terrible nightmare...)"
    show ca 12
    prof "You're part of the student exchange program at Kredon, [mc]. Sleeping in class is not the behavior we expect or will tolerate from you. You're supposed to set an example for the rest of the students."
    show ca 11
    mc "I... know, Mr. Keating."
    show ca 12
    prof "Between the incident with Axel, and your naps in class, I think I’ll have to seriously consider probationary measures for you."
    prof "If this continues to happen, you’ll leave me with no choice but to call your former school and take more drastic measures."
    prof "It doesn’t matter how good your grades are."
    show ca 11
    mc "It won't happen again, Professor! I promise!"
    show ca 12
    prof "*Sighs* I hope that's true."
    prof "Now get out of here, I'm locking the door. And start studying for next week's exam!"
    show ca 11
    mc "I will! Thank you!"
    stop music2 fadeout 6
    play music rain2 fadein 5
    show ca 0 with Dissolve(2.5)
    play sound5 carpasswet
    mct "Honestly, he’s probably right... I should start sleeping earlier. I'm sleepy all day long." with dis08
    mct "Although... to be fair, Mr. Keating's \"Linear Algebra\" class wasn't exactly gripping. I taught myself that long ago."
    play sound3 vibration
    play sound2 vibration
    blank "{i}Your phone beeps."
    show ca 13
    mc "Hmm?"with dis
    mct "Oh damn, that’s a lot of messages. I should probably answer some of them."
    show ca 14 with dis12
    mod "You should check out all available messages."
label phone04:
    scene ca 14
    menu:
        with dis
        "Alex" if alexp04:
            $ alexp04 = False
            call chat(alex_chat) from _call_chat
            show ca 16
            mct "Hmm... Tomorrow's the big day." with dis08
            mct "Everyone’s counting on me. Not to mention all the big Ulysses power players being there: William Bardot, the other major shareholders, Idriel, the Founder... oh crap, probably even Thanatos?"
            mct "But I’ve gotta use this chance to obtain as much info as I can. I can’t just rely on Alex, I need to be ready too!"
        "Dalia" if daliap04 and (daliapath or tellpassword):
            $ daliap04 = False
            if daliapath:
                call chat(dalia_chat) from _call_chat_1
                if daliameme:
                    show ca 17
                    if daliablowjob:
                        mct "I was worried she’d be awkward around me after yesterday’s competition, but it doesn’t seem like it." with dis08
                        mct "She has the same silly humor as me."
                    else:
                        mct "She has the same silly humor as me." with dis08
                else:
                    show ca 18
                    mct "Oops, I think I was a little too rude there." with dis08
                    show ca 16
                    mct "Bah, who cares. She's the one who started making fun of me." with dis08
            else:
                call chat(dalia_chat2) from _call_chat_2
                show ca 18
                mct "Damn, she's still really angry." with dis08
                mct "You really blew it this time, [mc]."
        "Penelope" if pennyp04 and penelopepath:
            $ pennyp04 = False
            call chat(penelope_chat) from _call_chat_3
            if pennypics04:
                show ca 17
                mct "Damn, those photos were amazing." with dis08
                mct "I wonder if she'll post them... or if she just wanted to show them to me..."
        "Nova" if novap04 and novapath:
            $ novap04 = False
            call chat (nova_chat) from _call_chat_4
            show ca 18
            mct "Hmmm... That was... strange."with dis08
            mct "I wonder what she's up to..."
            show ca 17
            mct "But it's funny to see how, after all her life without a phone, she's totally hooked to it now."with dis08
        "Luna" if lunap04:
            $ lunap04 = False
            call chat (luna_chat) from _call_chat_5
            if dayofthedead:
                show ca 16
                mct "Day of the Dead, huh... That sounds pretty cool! I wonder if she’ll dress up?" with dis08
                mct "I'll write that date down on my calendar. I can't miss it!"
            elif not lunapath:
                mct "Hmm... She didn't reply. Luna’s just as closed-off as when we first met." with dis08
                mct "She's always so nice, though. Maybe she just needs more time... I'm sure we can be good friends."
            else:
                pause 0.8
        "Nancy" if nancyp04 and nancypath:
            $ nancyp04 = False
            call chat (nancy_chat) from _call_chat_6
            show ca 14
            mct "Damn, at this rate, the whole server will be hers in a matter of weeks. Maybe we’ll all be calling Nancy the Queen of Eternum soon?" with dis08
            show ca 17
            mct "That bikini though... sexy as hell." with dissolve
        "Chang" if changp04 and (not novap04 or not novapath):
            $ changp04 = False
            call chat (chang_chat) from _call_chat_7
            pause .8
        "Put your phone away":
            mct "Bah, I'll answer later. I don't have the time right now."with dissolve
            jump postphone
    if not alexp04 and not changp04 and (not daliap04 or not daliapath) and (not pennyp04 or not penelopepath) and (not lunap04 or not lunapath) and (not novap04 or not novapath) and (not nancyp04 or not nancypath):
        scene ca 14
        mct "Okay, finally! That was all." with dis
        mct "I'm not looking at my phone again until the masquerade party!"
        jump postphone
    jump phone04
label postphone:
    play sound6 carpasswet
    show ca 0 with dis2
    mct "Alright..." with dis08
    if not dayofthedead:
        $ lunapath = False
        $ lunau = False
    if anniepath:
        mct "Time to go home."
        mct "I have a date with a very special someone today, and I don't want to keep her waiting too long..."
    else:
        mct "I guess I don't have too much to do before tomorrow night, then."
        if not daliapath:
            mc "*Yawns* (That's what I call a quiet week. I haven't done shit yet and we're on Friday already.)"
        mct "I'll go home and do some research before the event."
        mct "And maybe I can log into a shopping mall server in Eternum and buy myself a nice suit..."
        jump fancydinner
    stop music fadeout 4
    show black
    show screen afewminuteslater
    with dis2
    play musicb birds fadein 4
    pause
    hide screen afewminuteslater
    scene ca 24
    with dis2
    mct "Of course." with dis08
    mct "The rain just HAS to stop once I get home and get ready for an Eternum gaming marathon..."
    mct "This bloody weather..."
    show ca 25
    mct "Anyways, I should probably find Annie." with dis
    mct "I haven't seen her around, though. Isn’t she home yet?"
    play sound run
    mc "*Yelling* AN–{w=0.8}{nw}"
    play sound slam
    show ca 26
    a "Good eveNING!!!" with hpunch
    play music2 quirky3 fadein 4
    stop musicb fadeout 5
    show ca 27
    mc "*Laughs* Were you waiting on the other side of the door, or what?" with dis12
    show ca 28
    a "O-Of course not! I was just, like, casually passin' through and remembered..."
    a "Well, today we're supposed to... I don't know if you remember...?"
    show ca 27
    mc "Of course I remember! Today we're going on a date, young lady."
    show annieshyzoom04
    a "(Oh my god, he remembered!)" with dis12
    a "(I was afraid he'd forget, but he didn't!)"
    a "(I'm going on a date with [mc]!)"
    scene ca 30
    mc "So..."
    mc "Are you ready?"
    show ca 28
    a "Yes, I am!" with Dissolve(.7)
    show ca 27
    mc "Hey, did you do something different with your hair? It looks longer."
    show ca 31
    a "My hair?" with dis08
    a "Oh well, yeah, I haven’t gotten my hair cut since we arrived in Kredon..."
    a "Y-You mentioned that I looked good with long hair in Eternum, so I thought of letting it grow a bit in the real world too."
    show ca 32
    mc "Cool! You look beautiful."
    show ca 31
    a "T-Thanks."
    show annieshyzoom04
    a "(Oh my god, he noticed!)" with dis12
    a "(And he also said he likes it!)"
    a "(I should let my hair grow as much as in Eternum!)"
    a "(Maybe extensions...?)"
    scene ca 30
    mc "Uh... Okay, so about this \"date\"..."
    show ca 28
    a "Yes! Did you have something in mind?" with Dissolve(.7)
    show ca 27
    mc "I do! Do you know the Andromeda server?"
    show ca 28
    a "Of course! It’s the biggest server in Eternum!"
    show ca 27
    mc "Well, I found a little planet where there's some kind of space-resort designed for couples. I took a look and there are a lot of activities and services, like theaters and Zero-G rooms."
    mc "It looks pretty fun!"
    show ca 33
    a "What? That probably costs a lot of money!" with dis08
    a "I can't accept that!"
    show ca 34
    mc "I knew you'd say that!"
    mc "First of all, when I first played Eternum, you gifted me all the eternals you had saved up – so you have no right to be mad about this!"
    mc "Oh, and I’m gonna pay all that back as soon as I have the money or a really valuable item, so don't think I've forgotten about it!"
    show ca 33
    a "Hey, that doesn't count!"
    show ca 34
    mc "And second of all, they have a deal right now where new players can bring a date and try some facilities for four hours without charge. And it’s only been about a month, so I just barely meet the cutoff!"
    mc "So... it’s totally free, and you have no excuse!"
    show ca 31
    a "Oh, in that case... okay!" with dis08
    a "Let's do it!"
    show annieshyzoom04
    a "(Oh my god, a date in Eternum!)" with dis12
    a "(A date with [mc]!)"
    a "(A date in Eternum WITH [mc]!)"
    a "(All my dreams are coming true!)"
    scene ca 30
    mc "*Chuckles* I think you're getting too excited about this, Annie. You need to relax. You'll enjoy it more if you take it less seriously!"
    show ca 35
    a "Too excited? Me?"with Dissolve(.7)
    show ca 36
    a "Where did you get that from?" with Dissolve(.7)
    show ca36
    a "I'm like... super chill!"
    scene ca 36
    a "Chillin’ like a villain on penicillin, bro!" with Dissolve(.2)
    scene ca 37
    a "Gonna play some Eternum with ma' homie..." with Dissolve(.2)
    scene ca 36
    a "Just vibin' in a space server y'know?" with Dissolve(.2)
    show ca36
    a "No biggie!"
    mc "*Laughs* You're right! It's obvious that you're super relaxed. Sorry, I was clearly mistaken!"
    scene ca 27
    mc "Alright then, I'll log in first and send you an invitation!" with dis
    show ca 28
    a "Okay! I'll put my E-suit on!"
    play sound run
    stop music2 fadeout 8
    play music birds fadein 5
    show ca 38 with dis15
    mct "Maybe not as much as Annie, but I'm pretty nervous too."with dis08
    play sound2 chair1
    show ca 39
    mc "*Jumping on the bed* (I read about this place on an Eternum forum, but I haven’t visited yet.)"with dis12
    play sound3 clothes3
    mc "*Putting the E-suit on* (I hope it's as good as the posts claim.)"
    play sound2 beep
    play sound ai7
    blank "{i}Connected." with dis
    play sound ai8
    blank "{i}Welcome back to Eternum." with dis
    play sound ai13
    blank "{i}You do not have any server invitations." with dis
    mc "I want to join the Andromeda server. I should have access to the Exit Portal number... L-768."
    play sound ai11
    blank "{i}Please prepare to connect..." with dis
    stop music fadeout 4
    play sound risingshort4
    pause 2
    show login3 with flash
    pause 8
    play soundlow whoosh4
    scene white with dissolve
    play music2 andromeda1 fadein 3
    show ca 40 with Dissolve(2.5)
    pause
    mc "*Taking a deep breath* (Ahh... this feeling of discovery again... I missed it!)" with dis08
    show ca 41
    mct "I guess this is where they receive customers."with dis12
    mct "So far, so good! It feels elegant and intimate... and futuristic as fuck!"
    play sound beep3
    show ca 42 with dis
    mct "Okay... Now I have to send an invitation to Annie..."with dissolve
    mct "I'm usually the one receiving the invitations, so... I hope I got this right."
    mct "Send invitation... to... Annie Winters."
    show ca 41
    mct "And done. It'll probably take her a few–" with dis08
    play sound whoosh2
    show ca 43 with flashfast
    pause .5
    mct "–Or maybe not."with dissolve
    play sound2 glassimpact
    show ca 44
    a "*Pressing herself up against the glass* Whoaaaa!" with dis08
    a "Look at this! It's like an endless ocean!"
    a "Amazing..."
    a "Most planets in this server are basically deserts..."
    show ca 45
    mc "Annie? Is that you?" with dis
    $ unlock_look("annie", 5)
    show ca 46
    a "Hi!" with dis08
    show ca 47
    mc "Wow! You look so different!"
    show ca 48
    a "Oh w-well, yeah, I went to buy a couple of things yesterday for the non-combat servers and I also got a new haircut option for Eternum..." with dis
    a "Nothing too special..."
    show ca 47
    mc "You look stunning!" with dis
    show ca 46
    a "T-Thanks!"
    a "You look good too!"
    show ca 47
    mc "Thank you! I didn't really know what to wear in a server like this, but in the ad they said \"casual outfit\", so I just went with it."
    show ca 46
    a "Yeah, in Andromeda, you can find all kinds of different scenarios."
    a "Eternum could consist of just this server, and it'd still be unfathomable!"
    show ca 47
    ast "Greetings!"
    show ca 49
    ast "Welcome to Astrocorp, the best way to forge a bond with your loved ones since 2022."with dis12
    ast "I'm Maria, and I'll introduce you to the systems before sending you out on your adventure."
    show ca 50
    a "Hi! Thank you for welcoming us in."
    show ca 51
    ast "No, thank you and your beloved for choosing Astrocorp."
    show ca 50b
    a "W-Well, we're not a c-couple."with dis08
    a "I mean, n-not yet."
    a "I mean... not that I want to..."
    a "N-Not that I don't want to...!"
    a "We're just having a date. But not like..."
    a "I mean..."
    show ca 52
    ast "*Chuckles* Don't worry. What's important is that you came here with someone you care about."
    ast "That’s all that matters. For any kind of date you have in mind, we hope you consider Astrocorp as your first option."
    ast "Astrocorp prides itself on its adaptability, as well. We’ve recently even begun catering experiences for polyamorous relationships, if that was something you were interested in..."
    show ca 53
    mc "Uh... that’s not exactly what we’re looking for right now...! Let’s stick with the original plan..."
    show ca 52
    ast "Please let me know if your plans change, it would be our pleasure to help. Our company has opened several new branches all over this server, and we have been operating on this planet almost since Eternum's launch."
    ast "Are you familiar with the Andromeda server?"
    show ca 50
    a "I like to play here sometimes, but it's the first time [mc] has been here."
    show ca 52
    ast "You couldn't have come to a better place, then. Would you like to know more about Andromeda?"
    show ca 53
    menu:
        with dis
        "Sure":
            mc "Sure! It's always fascinating to learn more about this world."with dissolve
            play sound spell5
            show ca 54
            ast "Andromeda holds the record for being the biggest server in Eternum." with flashfast
            ast "It is estimated that there are more than 30,000 star systems, each one with its unique set of orbiting planets."
            ast "Most of them are completely uninhabited, but no two are alike."
            ast "There are no borders or boundaries located anywhere in the server, and thanks to the FTL Space Launchers, space exploration is only limited by your imagination and effort."
            ast "However, most players are typically concentrated in the space stations located in the asteroid belt of Kalanar."
            ast "Planets have no owners, so you're free to build your base or colonize a settlement as long as you have the necessary resources."
            show ca 53
            mc "Wow, that sounds... massive." with dis
            mc "And who's running this server? Who designed it?"
            play sound spell5
            show ca 54
            ast "Andromeda was released alongside Eternum, and it has been constantly expanding since then. It was one of the initial promotional servers." with flashfast
            ast "The Founder and his team were instrumental in Andromeda’s development."
            show ca 53
            mc "Uh... yeah, that's really impressive." with dis
            play sound spell5
            show ca 55
            ast "We're located here, on Nox 7 – one of the two planets orbiting the white dwarf star Zheta-A." with flashfast
            ast "While the other planetoid is nothing but a wasteland of empty caverns, Nox 7 is one of the more bustling planets in this quadrant."
            ast "More than 25,000 players drop by everyday!"
            ast "I suggest you pay a visit when you get the chance."
            show ca 53
            mc "That's... simply astonishing. Thank you!" with dis
        "No{#0.4,astrocorp}":
            mc "Nah, you can spare me the history lesson, thank you."with dissolve
    show ca 56
    ast "Alright then. We're all set." with dis
    ast "The one-day package for the free trial visitors includes access to all of our facilities until 11 PM. If you need any assistance, please feel free to ask me or any of my colleagues."
    ast "Thank you again for choosing Astrocorp. I'm pleased to welcome you to the ultimate experience of love..."
    show ca 57
    ast "Annie..."with dis
    show ca 58
    ast "[mc]..."with dis
    stop music2 fadeout 1
    show ca 59
    ast "Falazio."with dis
    play music2b quirky3 fadein 10
    show ca 60
    fal "Um..." with dis08
    fal "I'm not sure I understood what you meant with your speech. I-Isn't this a dating service?"
    show ca 56
    ast "Not exactly. Our service is aimed at either new or long-established relationships. Here you can find numerous activities to make your date an unforgettable experience."
    show ca 60
    fal "Uhh... so... no meeting singles here?"
    show ca 56
    ast "I'm afraid all our clients already come here with a partner."
    show ca 61
    fal "Uhhh... I think I read the ad wrong."with dis
    fal "C-Can I get my money back?"
    show ca 56
    ast "No."
    show ca 61
    fal "Oof..."
    ast "However, you can still use facilities anyway. We offer an excellent selection of muffins in the canteen. They are simply... out of this world."
    show ca 62
    fal "Oh... oh!" with dis08
    fal "That doesn't sound that bad! Let's see those muffins!"
    ast "Please follow me."
    show ca 63
    ast "You can use our teleporter to get to the station in a matter of seconds." with dis12
    mc "A teleporter?"
    ast "The Astrocorp Experience takes place in a space station in orbit, 250 miles away from the surface of Nox 7. This is just the Entrance Hall."
    mc "So it's like a portal? I’ve been in way too many of these recently..."
    play sound glassimpact
    show ca 64
    a "Ahh! I see it! I can see the space station from here!"with hpunch
    mc "What? Where?"
    a "Right there! Between the clouds!"
    mc "*Narrowing your eyes* ...I don't see anything."
    fal "Oh, it's true! I can see it too!"
    mc "Are you messing with me?!"
    show ca 63
    ast "The teleporter will break down all of your molecules into atoms, and recombine them again in your designated cabin." with dis
    mc "That sounds... painful."
    show ca 65
    a "Let's break those molecules, [mc]!"with dis08
    mc "*Chuckles* I’ve gotta say, your enthusiasm is contagious."
    show ca 66
    a "That's because I’m really thrilled about this!"with dis08
    a "I’m having so much fun, and we haven't even started yet!"
    show ca 67
    mc "Can't wait to see the views from the space station. I've heard they're incredible."
    show ca 66
    a "This was a great date idea, [mc]. Thank you for inviting me!"
    show ca 67
    mc "Okay, that's it, you're forbidden from saying \"thank you\" again until the date is over!"
    show ca 66
    a "*Giggles* Okay, okay, sorry!"
    show ca 67
    mc "Alright, time to break down some molecules."
    show ca 66
    a "Let's hope our atoms don't get lost along the way!"
    show ca 67
    mc "Hey, nothing ventured, nothing gained."
    show ca 66
    a "That's my personal philosophy!"
    a "Like I said to you when we first played Eternum on Ion..."
    show ca 67
    menu:
        with dis
        "Take the leap of faith! [annie_pts]":
            $ annie_points += 1
            mc "Take the leap of faith!"with dissolve
            show ca 66
            a "That's the one!"
            play sound beat
            show screen heartbeat
            show ca 65
            a "Come on [mc], take the leap of faith!" with dis
        "Let's get this shit done!":
            mc "Let's get this shit done!"with dissolve
            show ca 66
            a "*Laughs* I didn't say that, but that's also a good quote!"
            show ca 65
            a "Let's get this shit done!"with dis
        "Nothing ventured, nothing gained!":
            mc "Nothing ventured, nothing gained!"with dissolve
            show ca 66
            a "*Laughs* You just said that right now!"
            a "That's also a good quote though."
            show ca 65
            a "Nothing ventured, nothing gained!"with dis
    show ca 68 with dis12
    mc "*Putting yourself in front of the strange device* Okay, sooo..." with dissolve
    mc "How does this thing work?"
    ast "Just stay right there, and try not to move."
    ast "Remember that this is a one-way trip. You'll have to use the teleporter in the station hangar, or use a transport ship to return to the surface, and use the Exit Portal here."
    mc "Gotcha."
    play sound2 charge
    show ca 69 with dis17
    ast "Molecular breakage in 3..."with dis08
    mc "Um... i-is this itching I'm feeling normal?"
    ast "2..."
    mc "M-Maria?"
    ast "1..."
    play sound portalandromeda
    stop music2b
    show portal04
    pause 2.35
    play music spaceshipambient
    scene ca 70 with flashfaster
    mc "AHHHHHH!" with hpunch
    mc "Jesus!"with hpunch
    mc "My... {w}molecules!"
    a "Wow..."
    show ca 71
    mc "Huh?" with dis08
    play music2 synth3 fadein 2
    show andromeda1 with dis2
    pause 1.9
    play soundlow spaceship
    pause 4.7
    scene ca 71
    a "Look at all these comets!"with dis04
    a "There are a lot of them!"
    a "Quick, [mc], make a wish!"
    mc "I want a hundred wishes!"
    show ca 72
    a "*Laughs* That's not allowed!" with dis12
    show ca 73
    mc "It is! I read Andromeda's wishing rules. I’m an expert now."
    show ca 72
    a "*Laughs* Oh, now you know more about this server than I do?"
    show ca 73
    mc "*Chuckles* Nah, probably not. Only about its wishing rules. I’m guessing you’ve spent hundreds of hours here."
    show ca 72
    a "Nah, not really!"
    a "It's an awesome server, but it almost feels too big for me."
    show ca 74
    a "And well, you really need your own spaceship to move freely in a server like this, and they're egregiously expensive!" with dis08
    mct "Note to self: buy Annie a spaceship to repay her for that initial Eternum gift."
    a "The cheapest ones cost between $500,000 and $700,000."
    mct "Note to self: disregard previous note."
    a "I'll get one someday!"
    mc "I'm sure of it!"
    show ca 75
    mc "Alright then, let's explore this romantic station, shall we?"with dis
    a "*Giggles* S-Sure!"
    play sound doorspace
    show ca 76 with dis15
    pause
    player "Thank you so much, Katniss!"with dissolve
    show ca 77
    ast "Hello, couple! Welcome to the USCSS Icarus, the most romantic station in all of Eternum!"with dis
    ast "My name is Katniss, nice to meet you. How may I help you today?"
    show ca 78
    mc "Hi Katniss!"
    mc "I’m [mc] and this is Annie. It's our first time here, what would you recommend?"
    show ca 77
    ast "Ah, if it's your first time at Astrocorp, I'd suggest that you try the Zero-G room. It's a unique experience that no one should miss!"
    ast "There's a bit of a queue, but I can make a reservation under your name 3 hours from now."
    show ca 78
    mc "Sure! Let's do it."
    show ca 77
    ast "And... while you wait... I'd suggest you check out our cinemas! We have two movies available today, Interstellar and Hot Tub Time Machine 2."
    ast "After the Zero-G experience, you can also visit our 4D bowling lanes, or try the ice rink."
    ast "And to finish up your date, you must go to the Planetarium! You can see all the corners of Andromeda from there."
    show ca 78
    mc "That all sounds awesome!"
    mc "Thank you very much!"
    show ca 77
    ast "And lastly, please note that you can find flyers with all the available activities in your cabin."
    show ca 78
    mc "Perfect."
    show ca 79
    mc "What do you say, Annie?" with dis08
    show ca 80
    a "I'm all for it! Everything sounds really fun."
    show ca 79
    mc "Let's start with a movie, then. What do you wanna see?"
    show ca 81
    a "I don't mind! I haven't seen either of the movies she said, so it's your choice!"with dis08
    mc "Any preference?"
    a "Nope! Not at all."
    a "Your call!"
    show ca 79
    menu:
        with dis12
        "[gr]Interstellar":
            $ interstellarm = True
            mc "Let's watch Interstellar. It's one of my favorite movies, and I know you haven't seen it yet." with dissolve
            mc "With how much you love sci-fi, I'm sure you'll like it too!"
        "Hot Tub Time Machine 2":
            mc "Let's watch Hot Tub Time Machine 2... whatever that is. I've already seen the other movie, so at least by going to this one we both can see something new."with dissolve
    show ca 80
    a "That sounds good!"
    a "Lead the way!"
    play sound doorspace
    show ca 82b with dis2
    mc "Damn, these views are amazing wherever you look."with dissolve
    a "Right?"
    mc "We definitely have to take one of those spaceships back to Astrocorp's Exit Portal. No way I’m using another teleporter!"
    a "Do you know how to fly those things?"
    mc "Oh please, I'm not only a cunning warrior, but also the best star-pilot in the galaxy."
    a "*Laughs* Alright, I trust you, Anakin!"
    play sound doorspace
    show ca 82 with dis15
    a "Ohh!" with dissolve
    a "It's awesome!"
    a "Where should we sit?! In the middle? I like to sit in the middle!"
    show ca82
    mc "Actually, I typically prefer the rear...{w=7}{nw}"
    scene ca 84
    mc "But it looks like those are reserved, so the middle sounds good!"with dis
    show ca 83
    a "Look at those speakers! They're huge!"
    show ca 84
    mc "Yeah, I read that the sound is spectacular. And the real 3D image makes it super immersive."
    show ca 83
    a "Wow... Can't wait to see it!"
    show ca 84
    mc "I'll go get some popcorn. What do you want?"
    show ca 83
    a "Um..."
    a "An XXL Bowl and a coke!"
    show ca 84
    mc "Got it! Go get a good seat, I'll be right back."
    show ca 85
    a "Understood! Don't be long!"with dis08
    stop music2 fadeout 5
    show black with dis2
    show screen afewhourslater with dis
    pause
    play music2b movietheatre fadein 4
    hide screen afewhourslater
    if interstellarm:
        scene ca 86
        with dis2
        mct "I've seen this movie like 4 times already, and I never get tired of it."with dissolve
        mct "One of the best sci-fi movies of all time, no doubt."
    else:
        scene ca 86b
        with dis2
        mct "Jesus Christ, this has to be the worst sci-fi movie I've ever seen..."with dissolve
        mct "It's unwatchable."
    show ca 90
    mc "*Looking at the other people in the theater*" with dis12
    show ca 91
    players "*Making out*"
    show ca 90
    pause
    show ca 87 with dis08
    pause
    show ca 89
    player "Do you know who the hottest person in this entire star system is?"
    show ca 88
    player2 "*Giggles* Who?"
    show ca 89
    player "You."
    show ca 88
    player2 "*Giggles* No, {i}you’re{/i} the hottest."
    show ca 89
    player "No, you."
    show ca 88
    player2 "*Giggles* You!"
    show ca 87
    pause
    show ca 92
    mc ". . ." with dis
    if interstellarm:
        play musicb interstellars
        play soundlow whoosh3b
        show ca93b with Dissolve(0.05)
        pause 0.05
        scene ca93
        pause 6
        a "Y-You have to make it, Cooper!{w=4.2}{nw}" with dis08
        a "You've gotta come back home!{w=4.2}{nw}"
        scene ca 93b
        mc "*Smiles*{w=4.7}{nw}"with dis15
        stop musicb fadeout 4
    else:
        show ca 94b
        a "Zzzzz..." with dis12
        mc ". . ."
        a "*Talking in her sleep* It's two days until my date with [mc]..."
        a "*Talking in her sleep* I’ve gotta buy me a new pair of boots..."
        a "Zzzzz..."
        scene ca 95
        mc "*Smiles*" with dis
    stop music2b fadeout 3
    show black with dis2
    show screen afewminuteslater with dis
    pause
    play music2b synth3 fadein 4
    hide screen afewminuteslater
    scene ca 96
    with Dissolve(2.1)
    player3 "Where do you wanna go now?" with dis08
    player2 "Bowling!"
    player3 "Bowling? Well, if my babygirl wants to bowl, bowling it is..."
    player2 "*Giggles*"
    if interstellarm:
        show ca 98
        a "*Crying* He p-promised his daughter he'd come back...!"with dis15
        a "*Crying* And she never s-stopped believing the p-promise..."
        show ca 99
        mc "Are you okay, Annie?" with dis12
        a "*Sobbing* Y-Yeah, it's just that..."
        a "*Sobbing* The m-movie moved me a little, I'm sorry."
        mc "You didn't like it, then?"
        $ bios_background["annie"] = "annie_bios2"
        $ interstellarm2 = True
        show ca 101
        a "What?! NO! Of course I did!" with dis08
        $ annie_points += 1
        play sound beat
        show screen heartbeat
        a "That was like... the BEST movie I've ever seen!"
        show ca 102
        mc "*Chuckles* Really?"
        show ca 101
        a "Yeah! I plan to watch it again as soon as we're back in the real world!"
        a "T-The acting, the cinematography, the epicness, the feels, the MUSIC!"
        a "I loved it all!"
        show ca 102
        mc "I'm glad to hear that!"
        mc "It's one of my favorites too. I think all the Astrocorp features really added to the experience!"
        show ca 101
        a "I can see why! I remember you talking about it, but I never got the chance to see it until now."
        a "WHAT ELSE HAVE I BEEN MISSING?!"
        show ca 102
        mc "Well, this was just the beginning! I, for one, am looking forward to that Zero-G experience."
    else:
        show ca 97
        a "OH MY GOD, I FELL ASLEEP!"with dis12
        a "I FELL ASLEEP during my date with [mc]!"with hpunch
        a "I've ruined it!" with hpunch
        show ca 99
        a "*Sobbing* I've ruined it forever..."with dis12
        mc "You haven't ruined anything!"
        mc "Let me guess, you didn't sleep last night, did you?"
        a "I..."
        show ca 101
        a "H-How do you know?"with dis
        show ca 102
        mc "Because I know you. You needed a little nap. And hell, I think I zoned out during some parts of that movie too. It was terrible! No one can blame you."
        mc "So no more sad faces! Can you promise me that?"
        show ca 101
        a "O-Okay! I promise!"
        show ca 102
        mc "Excellent!"
        mc "And now... I don't know about you, but I'm gonna go try out that Zero-G room."
        mc "I'm looking forward to it."
    show ca 103
    a "Ah, true! Is it time already?"with dis08
    mc "Yep! And I think it's at the other side of the station, so we’d better hurry!"
    a "I can't wait! Let's go!"
    stop music2b fadeout 5
    play music2 andromeda2 fadein 6
    show ca 104 with Dissolve(2.3)
    pause
    stop music fadeout 15
    play sound doorspace
    show ca 105 with Dissolve(2.2)
    mc "Alright, cabin 17! Here's where we have to get changed."with dissolve
    a "Awesome!"
    mc "It's...!"
    mc "I-Isn't it a bit... grimy? Looks like a pigsty..."
    play soundlow doorspace
    show ca 107
    ast "Hello guys!" with dis
    show ca 106
    mc "I m-mean... this is awesome! Very clean!"
    show ca 108
    ast "I know about the mess... I'm so sorry."with dis08
    ast "Claire, our cleaning lady, is currently in the infirmary. She started feeling poorly all of a sudden."
    ast "We thought it was just a little dizziness, but if it keeps up, she’ll have to go back to Nox 7 and log off for the day."
    ast "Unfortunately, we have no replacement for her, and with the rest of the staff being on strike... the dressing rooms are in terrible shape."
    ast "We've been forced to temporarily use the employees' cabins as alternatives..."
    show ca 106
    mc "No problem at all, seriously." with dis08
    mc "I know what it's like to be an employee at a big company. My last summer job was not... the best experience, to say the least."
    show ca 107
    ast "Thank you for understanding!"
    ast "You can find Zero-G suits of all sizes in the closet. Please remember to use the tightest fit possible. As soon as you've changed, you can follow the corridor on the right to the Zero-G room."
    ast "The entire space is reserved for you two for a period of 15 minutes."
    show ca 106
    mc "Only 15 minutes?"
    show ca 107
    ast "I'm afraid so. The Zero-G room is in high demand."
    show ca 106
    mc "Understandable. Well, 15 minutes are better than nothing."
    show ca 107
    ast "Please call me if you need anything else."
    show ca 106
    mc "We will. Thank you!"
    play soundlow doorspace
    show ca 109
    a "I'm so excited!" with dis15
    show ca 110
    mc "I was expecting a little more time, to be honest."
    show ca 109
    a "Well, I guess everyone wants to try it out, so they have to speed the whole process up."
    show ca 110
    mc "Yeah, you're probably right. That makes sense."
    mc "Alright then, let's get changed!"
    show ca 109
    a "Yeah!"
    show ca 110
    a ". . ."with dissolve
    mc ". . ."
    show ca 111
    a "Um..." with dis08
    a "C-Can you look the other way, please?"
    show ca 112
    mc "*Turning around* Oh... o-of course!" with dis08
    play sound clothes
    mct "I feel so comfortable with Annie that sometimes I forget we're not really... a couple."
    mct "I mean... of course we're not. We haven't even..."
    mct "What happened the other day was something out of the ordinary."
    mc "*Clears throat* Uh... Can you pass me one of those suits?"
    a "Of course! Which size?"
    mc "The lady said it has to be tight, so... I guess S or M."
    play sound2 clothes2
    a "There you go!"
    mc "Thanks!"
    play sound3 clothes
    mc "*Putting the new clothes on* You're not staring at my butt while I'm getting changed, are you?"
    a "*Laughs* Of course not!"
    mc "*Chuckles* A likely story, Ms. Winters... I'll believe you, for now..."
    a "Alright, I think I'm ready!"
    show ca 113
    mc "*Turning around* I am too." with dis08
    mct "Whoa, Annie's ass really looks like a peach in this..."
    $ unlock_look("annie", 6)
    show ca 114
    a "*Giggles* This thing feels... kinda weird, doesn't it?" with dis
    show ca 115
    mct "Damn... This suit is skin-tight... I can see every single curve of Annie's petite body."with dis12
    mct "Her stature and complexion make her seem fragile and vulnerable, but... oh boy, those hips say something else..."
    show ca 116
    mc "Ehh... yeah, I know!" with dis
    mc "This fabric feels glued on!"
    show ca 114
    a "Yeah, but it's not uncomfortable!"
    show ca 116
    mc "True. It looks like it's made with some kind of waterproof plastic, but the inside is a softer, more foam-like material."
    show ca 114
    a "It's probably designed for maximum comfort in zero gravity."
    show ca 116
    mc "Probably. There's only one way to find out!"
    show ca 114
    a "Let's go!"
    play sound doorspace
    show ca 117 with dis2
    a "Whoa! This room is bigger than I thought!"with dis08
    play soundlow announcement2
    pas2 "Artificial gravity disabled."with dis
    mc "Hmm? Already?"
    show ca 118
    a "Hmm..." with dis
    a "I don't feel anything different. Are we really in Zero-G already?"
    mc "*Standing on your toes* I don't think so."
    show ca 119
    a "Maybe we have to jump onto this structure." with dis
    mc "It's worth a try."
    play sound4 chair4
    play sound2 jump3
    show ca 120
    a "*Jumps*" with dis
    play soundlow zerog
    show ca 121
    a "W-Whoa!{w=1.2}{nw}" with dis
    show ca 122
    a "Oh my god, I c-can't stop!" with dis
    show ca 123
    a "W-WOW!" with dis12
    a "*Laughs* This is amazing! I'm floating!"
    a "There's no gravity!"
    mc "Wow, it looks like you're flying..."
    a "Come here, [mc]! Jump!"
    play soundlow zerog
    show ca 124 with dis15
    mc "H-Holy shit!" with dis
    mc "This is super cool!"
    show ca 125
    a "Right? It feels like scuba diving in the air!" with dis
    mc "Have you ever done any scuba diving?"
    show ca 124
    a "*Laughs* No, but this is how I imagined it'd feel, only with more... water!"with dis
    a "Let's have a race to the wall and back!"
    mc "You have no chance!"
    show ca 104 with dis22
    pause
    show ca 126 with dis22
    mc "God... this feels so relaxing..." with dis08
    mc "I can move my arms and legs without any effort... I think I could even fall asleep in any position!"
    show ca 127
    mc "Right, Annie?" with dis12
    mct "Ah, looks like Annie fell asleep already."
    mc "Annie, you awake? I can go call the Astrocorp employee if we’re ready to wrap this up."
    show ca 128
    a "*Laughs* I'm not sleeping!" with dis
    a "I'm just trying to relax and vibe with the cosmos!"
    mc "*Chuckles* Oh, so mystical... I like it."
    show ca 129
    a "And I was also thinking about... how happy I am to be here with you." with dis
    a "You and Chang have always been my best friends, and neither of you played Eternum until recently, so... I've always felt kind of alone here."
    a "For years, I kept a mental list of all the things I wanted to show you in this world, once you could join me."
    a "And now... well, I don't have to imagine it anymore! You're here!"
    show ca 130
    mc "You’re the one who’s really made these first few weeks in Eternum worthwhile, Annie. I couldn't have asked for anyone better to spend time with."with dis12
    show ca 131
    a "Likewise!"
    show ca 130
label anniezerog:
    if not azg1 and not azg2 and not azg3:
        show ca 126
        jump anniezerogpos
    menu:
        with dis
        "About Eternum..." if azg1:
            $ azg1 = False
            mc "You know..."with dis08
            mc "Just a month ago, if you told me that I’d be floating in a space station orbiting some planet in a new galaxy... I would've laughed you out of the room."
            mc "The things you can do in Eternum are just... incomprehensible."
            show ca 135
            a "Right?!"with dis08
            a "There's never a single session where I’m fully prepared. There’s always something unexpected just around the corner!"
            a "You can do magic, transform your body, become super strong, turn invisible, dine at luxurious restaurants! You can even sleep or get drunk!"
            a "Anything and everything you can do in the real world... but enhanced! It gets harder and harder to log off every single time!"
            a "In fact, I've even heard of psychiatric Eternum studies where people... Wait, why are you laughing?"
            show ca 134
            mc "Get drunk, huh? I didn't know you were an Eternum drunkard..."
            show ca 135
            a "*Laughs* I'm not! You know I don't like alcohol."
            show ca 134
            mc "*Chuckles* I know. I don't usually drink either. Except... maybe at parties."
            show ca 135b
            a "Yeah, I guess that makes sense..."with dis
            a "I don't remember you going to many parties, though."
            show ca 134
            if penelopepath:
                mc "Actually, I'm going to one next week!"with dis
                mc "Penelope invited me to a costume party at her campus."
                if novapath:
                    mc "I think Nova will be there too."
                show ca 135
                a "Whoa! A costume party! That's pretty cool!"
                a "What are you going as?"
                show ca 134
                mc "Hmm... I still haven't thought about it, to be honest."
                mc "Any ideas?"
                show ca 135b
                a "Um... Let me think..."with dis
                a "You could disguise yourself as a character from a show or movie you like... maybe an animal... or a superhero."
                a "Oh, you could also dress up as someone famous!"
                a "I guess it also depends on whether you want to cover your face or not... and how much you're willing to spend!"
                show ca 134
                mc "Hmmm... a few things come to mind..." with dis
                mc "I'll let you know once I've decided!"
                show ca 135
                a "Can't wait!"
            else:
                mc "Yeah, you're not wrong. I usually prefer to do other things."with dis
                mc "Like hanging out in Eternum!"
                show ca 135
                a "That makes two of us!"
            show ca 134
            jump anniezerog
        "About our mission..." if azg2:
            $ azg2 = False
            show ca 130
            mc "It feels good to have some quiet time for once."with dis
            mc "The Gems of Doom, the Weapons of Atlas, Calypso, Benjamin’s excommunication, Thanatos... Everything has happened in... what? Less than a month?"
            show ca 131b
            a "I know... it's been crazy."with dis
            a "I still can't believe we... well, {i}you {/i}were invited to a dinner in the Rockefeller server with Ulysses' big shots. Are you nervous about it?"
            show ca 131c
            mc "Well..."
            mc "Maybe a bit. I don't know who I'm going to see there."
            show ca 131b
            a "And... are you afraid of seeing Thanatos again? I definitely would be!"
            show ca 131c
            mc "No, not really... it's a non-combat area and, to be honest, he doesn't strike me as the kind of guy who would accept an invitation to a dinner with a bunch of rich dudes. I doubt he's going to be there."
            show ca 131b
            a "But he's trying to gather the 10 Gems, isn't he? His objective is the same as everyone else’s, to become the new CEO of Ulysses."
            a "So, in a certain sense, his goal is to become one of those rich dudes himself, in the end."
            show ca 131c
            mc "Huh. You have a point there..."
            mc "The people there have got to know more about Eternum than anyone else in the world. I'll try to gather some information about everything, but..."
            mc "I want to be careful about whom I speak with. It could be dangerous."
            mc "I'm glad Alex is coming with me. She’ll be way more comfortable around those shady bigwigs than I am."
            show ca 131b
            a "Yeah, me too! I haven't talked much with her, but she seems cool!"
            a "The other day I saw her riding her bike – she looked so badass!"
            a "I waved to her, but she didn't see me..."
            show ca 131c
            mc "Were you behind a fire hydrant? That'd explain it."
            show ca 131
            a "*Laughs* Don't make fun of me! I'm not that short!"with dis
            show ca 130
            mc "*Laughs* If you say so... Did I tell you that Bennie Garrington thought that a child had attacked him at first?"
            show ca 131
            a "WHAT? You’ve gotta be kidding..."
            a "He needs better glasses!"
            show ca 130
            jump anniezerog
        "About Kredon... [annie_pts]" if azg3:
            $ azg3 = False
            mc "So..." with dis08
            mc "How's life in Kredon so far?"
            show ca 131b
            a "It's great!" with dis
            a "You were right, it's a rather small town, but there's everything you need!"
            a "And I felt super welcome in our new home!"
            a "Nancy, Penelope, and Dalia are all very nice to me. They treat me as one of the family. You know I’ve always wanted sisters, so I really feel like they’re giving me that experience!"
            show ca 131c
            mc "Happy to hear that!"
            show ca 131b
            a "And they're all so pretty! I wish I was as beautiful as them..."
            show ca 131c
            mc "What do you mean? You're just as pretty as any of them!"
            mc "*Chuckles* Honestly, I’m sometimes more intimidated by all these beautiful women than I am by Thanatos!"
            show ca 132
            a "Well, by \"pretty\" I mean..." with dis
            a "You know what I mean!"
            show ca 133
            mc "Hmm... no, not really, no..."
            show ca 132
            a "Agh! You know! I don't have their..."
            show ca 132b
            a "Assets."with dis
            show ca 133
            mc "Oh! Come on, Annie! You can't be serious!"with dis
            mc "You're precious. I know plenty of men who can appreciate a petite body just as much as big tits or a big butt. And you can include me on that list as well."
            mc "Especially if everything is so nicely shaped, as in your case..."
            $ annie_points += 1
            play sound beat
            show screen heartbeat
            show ca 132
            a "Oh please, s-shut up!"with dissolve
            a "You're gonna make me blush!"
            show ca 133
            mc "*Laughs* You've been blushing for a while now."
            show ca 132
            a "I'm not! It's just this suit! It's... too warm."
            show ca 133
            mc "*Chuckles* Of course!"
            show ca 132
            a "C-Can we change the subject?!"
            show ca 133
            mc "Hey, it's not me who keeps bringing up Dalia's butt in every conversation!"
            mc "*Chuckles* But okay, okay..."
            mc "How about the first few weeks at the new school? All good?"
            show ca 131b
            a "Yeah!" with dis
            a "Some of the girls are a bit... {i}unfriendly{/i} sometimes, but luckily I have Luna. She's super nice!"
            show ca 131c
            mc "I'm glad you two get along."
            show ca 131b
            a "She's been helping me with my math homework too. She's a great teacher."
            show ca 131c
            mc "Nice! Don't hesitate to ask me if you need any extra help with the other subjects."
            mc "You know I'm a genius."
            show ca 131
            a "*Laughs* Only in what interests you!" with dis
            a "But sure, I'll remember that, \"professor\"!"
            show ca 130
            jump anniezerog
        "Relax and say nothing":
            show ca 126
label anniezerogpos:
    mc "Okay, okay, stop talking now!" with Dissolve(1.3)
    mc "I was trying to relax and vibe with the cosmos before you interrupted me, you know?"
    show ca 129
    a "*Laughs* That's my line! And you’re the one who started talking!"
    show ca 136
    mc "Are you sure? That's not how I rem–"with dis
    stop music2 fadeout 2
    play music spaceshipambient fadein 8
    play soundlow announcement2
    show ca 137
    pas2 "Session terminated. Restoring artificial gravity."with dis12
    pas2 "Thank you for choosing the Astrocorp Experience."
    show ca 138
    mc "Aww... it went by so fast!"with dis12
    play soundlow zerog
    show ca 139
    blank "{i}You slowly start to feel your weight again, as you descend to the ground." with dis17
    show ca 140
    mc "Huh, I was getting used to moving my limbs effortlessly. It feels weird to feel their weight again." with dis08
    play soundlow zerog
    show ca 141 with dis12
    play sound clothes2
    pause
    show ca 142
    a "S-Sorry!" with dis
    a "I was trying to get to the wall before falling."
    a "But I... couldn't reach it."
    a "Y-You can just leave me on the floor. I don't want to hurt your back."
    show ca143
    mc "Hurt my back?"with Dissolve(.6)
    mc "I'm pretty sure the bar I use for biceps curls at the gym weighs more than you."
    scene ca 142
    a "Oh..." with dis08
    show ca 145
    a "Well, in that case... take me to my chamber, Sir [mc]!"with dis08
    a "We still have lots of things to see!"
    a "Hurry up!"

label annielewdspace:
    play music2 synth3 fadein 4
    stop music fadeout 9
    play sound doorspace
    show cx 1 with dis2
    mc "Hmm, I didn't see that worker from earlier anywhere, I guess we're supposed to leave the suits where we found them." with dis08
    play sound2 chair1
    show cx 2
    a "*Jumps on the bed* Oh my god, [mc]! Look at this!"with dis
    mc "Oh, the stellar nebulae!"
    a "Do you know anything about them?"
    mc "As I understand it, they're like giant clouds of gas and dust in space. Some are literally hundreds of light-years in diameter!"
    a "Wow... It's like seeing the Northern Lights in outer space!"
    mc "I know!"
    play soundlow chair1
    show cx 4
    mc "On the website, they said they could be seen after 10 PM, thanks to the station's orbit." with dis
    mc "I was thinking of going to the Planetarium now, but we can save that ‘til the last minute."
    show cx 5
    a "Well, if the nebulae aren’t going anywhere... I'd go there later, yeah." with dis08
    a "You know... for a grand finale!"
    show cx 4
    mc "That's what I thought, too!"with dis08
    mc "What do you wanna do now, then?"
    show cx 5
    a "I don't know... all the activities they mentioned sounded really fun!"with dis08
    a "Maybe we should just go for a walk and look around the station."
    a "As long as I'm w-with you... I don't really mind..."
    show cx 4
    mc "That sounds good too! Let's see what we can find."with dis08
    mc "We should probably change back into our regular clothes now."
    show cx 5
    a "Yeah, we probably should..."with dis08
    show cx 4
    mc "Yeah..."with dis08
    a ". . ."
    if annie_points <= 8:
        show cx 4
        mc "Yeah..."with dis08
        a ". . ."
        a "(Why... why am I so uncomfortable with [mc] watching me undress?)"
        a "(Isn't this what I wanted?)"
        a "(Maybe... it's just not the right time yet...?)"
        a "(Why do I have so many doubts? You’ve had a crush on him for years, Annie! But... something feels like it’s missing...)"
        a "(Oh god, now he's looking at you, Annie.)"
        a "(Say something!)"
        mc "So..."
        play sound chair2
        show cx 7b
        a "*Stands up* Y-Yeah! Um..." with dis
        a "You know... on second thought... I think it'd be better if we went home now."
        a "I had so much fun! But... I'm so tired. I haven't slept properly for days."
        show cx 7
        a "(I... need some time to think...)"with dis
        mc "Oh..."
        mc "N-No worries! I totally understand. I'm quite tired too..."
        mct "Why the sudden change? Did I say or do something wrong?"
        show cx 7b
        a "Let's take one of those ships back to Nox 7." with dis
        show cx 7
        mc "S-Sure!"with dis
        $ anniepath = False
        $ annieu = False
        stop music2b fadeout 5
        show black with Dissolve(2.5)
        show screen afewminuteslater with dis
        pause
        play music2 rain3 fadein 3
        scene caa 130
        hide screen afewminuteslater
        with dis2
        pause
        play sound3 plugin
        play sound4 clothes
        mct "Well..." with dis
        mct "That was... weird. Annie hardly said anything on the way back."
        mct "She looked lost in her own thoughts the entire trip back to the Exit Portal. All the other customers had already left, so it was just us and an uncomfortable silence."
        mct "This date took a wrong turn at some point, and I don't know what I did wrong."
        mct "Argh! I wish the real world had a replay button. Maybe I could have done something differently. Life is just... too complicated."
        mct "Anyway, I guess I have other things to worry about right now. This can wait."
        mct "Focus on the mission, [mc]! Tomorrow's the day!"
        mct "Let's go, baby!"
        jump fancydinner
    play sound chair2
    show cx 6 with dis
    mc "*You turn around* Oops, sorry." with dissolve
    mc "I'll let you cha–"
    play soundlow chair4
    a "*Gets up from bed* N-No!"
    show cx 7
    mc "What? No?" with dis12
    mc "You don't want to change clothes?"
    show cx 8
    a "No, not that..."
    a "I..."
    a "I want you to look at me this time."
    show cx 7
    mc "Oh..."
    menu:
        with dis
        "[gr]Agree":
            stop music2 fadeout 7
            mc "Well..." with dis08
        "Decline and stay as friends":
            mc "Look, Annie..." with dis08
            mc "I've been thinking about this whole... \"date\" for the last couple of days."
            mc "I like you, and you're my best friend, you already know that."
            mc "But... I also feel like we're not meant to be more than that. Things would get awkward if we tried to get together, and our friendship is too important to risk, for me at least."
            mc "I just like spending time with you!"
            mc "I... I think we're meant to be friends. Best friends!"
            mc "So... let's just stay like this for now, okay?"
            mc "I just don’t have those feelings for you right now."
            mc "In the future... who knows? Maybe. But I don’t want to lead you on, either."
            show cx 7b
            a "Oh... Of c-course." with dis
            a "That's... what I want too."
            a "It's just that... sorry, my head has been a mess lately. I didn't want to misread the..."
            show cx 7
            mc "No worries! I totally understand. My head has been all over the place too, you know, with all this back and forth..."with dis
            mc "We can have this conversation again after we gather the 10 Gems!"
            show cx 7b
            a "Sure!" with dis
            show cx 7
            mc "So... to the Planetarium?"with dis
            show cx 7b
            a "Um... What if we leave that for another day? The truth is that I'm a little tired."with dis
            show cx 7
            mc "Of course! If that’s what you want to do."with dis
            mc "We'll go back to Nox 7 using one of those ships!"
            show cx 8
            a "*Sad chuckle* Sounds fun."
            $ anniepath = False
            $ annieu = False
            stop music2 fadeout 5
            show black with Dissolve(2.5)
            show screen afewminuteslater with dis
            pause
            play music2b rain3 fadein 3
            scene caa 130
            hide screen afewminuteslater
            with dis2
            pause
            play sound3 plugin
            play sound4 clothes
            mc "*Removing your visor* (Well...)" with dis
            mct "Annie looked pretty down on our way back."
            mct "She looked lost in her own thoughts the entire trip back to the Exit Portal. All the other customers had already left, so it was just us and an uncomfortable silence..."
            mct "I made the right decision, though."
            mct "We can't worry about stuff like that right now, things with her would be just... too complicated. I have too many things on my plate as it is."
            mct "Maybe everything will change after I become the new CEO of Ulysses!"
            mct "Focus on the mission, [mc]! Tomorrow's the day!"
            mct "Let's go, baby!"
            jump fancydinner
    mc "If that's what you want..."
    play music2b sexy4 fadein 6
    show cx 8
    a "I d-do."
    show cx 7
    mc "In that case, you won't see me complain..."
    mc "There's enough trust between us already, isn't there?"
    show cx 8
    a "Y-Yeah... It's been like... 10 years since we first met?"
    show cx 7
    mc "That’s quite a while... No big deal."
    show cx 8
    a "No big deal..."
    show cx 9 with dis15
    pause
    play sound3 clothes
    show cx 10
    blank "{i}She removes her bodysuit and lets it slide down her body to the floor." with dis2
    show cx 11 with dis15
    mct "Wow..." with dissolve
    mct "I know I already saw her naked that night in my room, but... well, there was barely any source of light then. Man, she's... stunning."
    mc "You're so pretty, Annie..."
    a "Mm-hm..."
    mct "God, she's shaking like a leaf. She’s so precious."
    mct "She's not even looking me in the eye... I don't think I've seen her so nervous before. And considering it’s Annie, that's saying something."
    mct "What could I do to calm her down...?"
    mc "Annie?"
    a "Hmm?"
    play sound clothes2
    play sound2 fall2
    play soundlow dodge
    show cx 12
    mc "*You pick her up like she weighs nothing* Hop!" with hpunch
    a "AAAAH!" with hpunch
    a "[mc]! What are you doing?!" with hpunch
    a "I'M NAKED!!"with hpunch
    mc "Oh, believe me, I know..."
    mc "I thought that was the idea!"
    show cx 14
    a "W-Well y-yeah, I know!" with dis
    a "B-B-But..."
    a "I mean..."
    a "G-God, this is so embarrassing...!"
    show cx 13
    mc "Seeing you undressing just for me was hot as fuck, Annie."
    show cx 14
    a "W-Was it?"
    show cx 13
    mc "But you looked way too nervous, so I wanted to calm you down a little."
    show cx 14
    a "Calm me down?! Y-You grabbed me while I was naked!"
    a "Like... totally naked! You're touching my... b-butt!"
    a "How is that supposed to calm me down?!"
    show cx 13
    mc "Would it help if I got naked too?"
    show cx 14
    a "N-No! That'd make things worse!"with hpunch
    show cx 13
    mc "*Chuckles* Can I tell you something?"
    show cx 14
    a "I... Y-Yes..."
    show cx 13
    mc "But I need you to relax first."
    show cx 14
    a "I'm relaxed! I'm super relaxed!"
    show cx 13
    mc "No, you're not!"
    mc "Let's do something. I want you to look me in the eyes."
    show cx 14
    a "Y-Your eyes?"
    show cx 13
    mc "Mm-hm..."
    show cx 15
    blank "{i}Her eyes make contact with yours. You start to feel her limbs loosening their grip around you." with dis12
    mc "I know you're nervous. It's totally normal to be. And you tend to be a jittery girl anyway, so a little nervousness makes sense here."
    mc "But... Do you think I'm NOT nervous? I'm super scared too! I mean, in my arms, I'm holding an adorably precious, absolutely gorgeous girl whom I’ve liked for years."
    mc "We just went on a date on a spaceship hurtling between constellations in the sky! I'm surprised I'm not weak in the knees yet."
    mc "I know it's scary to get out of your comfort zone, but... I think we can overcome it together."
    mc "So let's stop fooling around and cut to the chase: I like you, and you like me."
    mc "I want to be with you... in {i}that{/i} way."
    a ". . ."
    mc "That’s how I feel. If you don't feel the same way... we can always go back to where we were a month ago and stay friends!"
    mc "It’ll be a little awkward at first, but our friendship is strong, and I know we’d be back to normal in no time."
    mc "Is that what you want?"
    show anniesmh2
    a "*Shakes her head*"
    mc "I know it's scary to cross this bridge when you're not sure what your partner might want, so let me be clear..."
    mc "I love how open your heart is to others, how sweet and kind you are to people you’ve just met. I love your adorable blushes, your kind laughs, and... your petite body and curvy ass."
    mc "You are so ridiculously pretty, Annie, that I can’t help but want to take our relationship to the next level."
    mc "I want to be with you."
    a ". . ."
    mc "Is... is that what you want too?"
    show annienod2
    a "*Nods her head*"
    mc "*Sighs with relief* I feel so much better now that we're finally speaking clearly, don't you?"
    scene annienod2
    a "*Nods her head*"
    mc "Alright so... can I ask you another question?"
    scene annienod2
    a "*Nods her head*"
    mc "Can I kiss you?"
    scene cx 18
    a "*Smiles*" with dis08
    scene annienod3
    a "*Nods her head*"
    show cx 20
    blank "{i}She kisses you with a sincere, unrestrained passion. Her legs wrap around you."with dis
    mct "Her lips are trembling... but her body isn’t shaking anymore."
    show cx 21
    mc "Well, after getting all that off my chest, I feel so much better." with dis
    mc "*Caressing her cheek* I feel like I could never get enough of you, Annie..."
    play soundlow clothes3
    show cx 22b
    a "I feel the same way..." with dis12
    show cx 22
    mc "Must be this place... We have to leave a generous tip when we leave."
    show cx 22b
    a "*Giggles* Definitely!"
    a "I guess we should leave the room before they need it for someone else..."
    show cx 22
    mc "Hmm... I'm pretty sure they wouldn’t mind if we stayed for an extra 20 minutes..."
    show cx 22b
    a "20 minutes? How much time do you need to change your clothes?"
    play sound clothes3
    show cx 24
    mc "Well... I was actually thinking of doing something else while we're here..." with dis12
    show cx 25
    a "Oh, really...? What do you have in mind?"
    show cx 24
    mc "Do you remember our night together in my room?"
    show cx 25
    a "Remember? You'll probably laugh at me, but... I've been thinking about it all the time."
    show cx 24
    mc "Is that so? What have you been thinking about, exactly, Ms. Winters?"
    show cx 25
    a "Well..."
    a "You know..."
    a "The sound of the rain against the window..."
    a "The feeling of your skin against mine..."
    a "The heat that you were giving off..."
    a "Your ragged breaths on the back of my neck..."
    show cx 24
    mc "Nothing else?"
    show cx 25
    a "*Giggles* Well..."
    a "And..."
    a "The feeling of your... {i}cock{/i}... between my thighs..."
    show cx 26
    mct "She pronounced \"cock\" as if she was saying a forbidden word. I love how innocent she is..."with dis
    play soundlow clothes3
    show cx 27
    blank "{i}You gently spread her legs to expose her pussy."with dis15
    mct "What a sight..."
    mct "I wonder how many people have seen Annie's most intimate part. She seems like she’d get changed in a corner of the locker room, covered in a towel."
    mct "The fact that she's allowing ME to see and do this with her... it turns me on so much..."
    show cx 28
    mc "Did I hear that right? You've been thinking about my cock?" with dis
    mc "Have I been fooled all these years? Innocent, shy Annie is actually a horny, perverted little girl?"
    show cx 29
    a "*Giggles* Maybe just a bit..."with dis08
    show cx 30
    blank "{i}You start massaging her perky breasts and kissing down her neck."with dis12
    a "Ahh..."
    a "*Moans* Oh god..."
    mct "She's not shaking anymore, but her breaths have quickened."
    mct "God, there are so many things I want to do to Annie right now... but it's still Annie. I don't wanna cross any line too fast."
    show cx 27
    mc "You're making me so horny, Annie..." with dis12
    a "You too..."
    show cx 30b
    mc "Let me take care of you tonight..." with dis12
    play soundlow chair3
    scene cx 31
    a "*Gasps*" with dis08
    mc "Is everything okay?"
    a "Y-Yeah. It's just that... I wasn't expecting..."
    mc "Oh... I'm sorry, I should have warned you."
    a "N-No! It's okay!"
    a "It's what I want..."
    a "Please, c-continue..."
    show astro1 with dis2
    a "Aaahhh..." with dis08
    mc "If you want me to stop, just let me know..."
    a "*Soft moan* N-No..."
    a "It feels nice..."
    mct "Her skin’s so warm and soft... She’s so delicate..."
    mct "And I can feel her starting to get wet..."
    a "Mmm..."
    scene black
    show astro2 
    with dis17
    blank "{i}You start increasing the speed of your caresses"with dis08
    a "*Moans* Aaahhh..."
    a "Oh god..."
    mc "Better?"
    a "*Moans* Y-Yeah..."
    mct "Now we're talking..."
    mct "She's starting to let herself go... moving her hips to the rhythm of my fingers..."
    mct "And her lips are now soaked in her own juice..."
    mc "Can you feel yourself getting wetter?"
    a "Y-Yeah..."
    a "It feels g-great..."
    mc "It'll only get better from here, babe..."
    mc "I just want to make you feel good..."
    a "Aahhhh... [mc]..."
    pause
    a "*Moaning* Aaahh..."with dissolve
    mc "Is everything alright?"
    scene cx 34
    a "Y-Yes..." with Dissolve(1.3)
    show cx 33
    mc "I'm gonna put my fingers inside you now... alright?"
    show cx 34
    a "A-Alright..."
    show cx 35
    a "Do it..."with dis12
    play soundlow blow1
    show cx 36
    blank "{i}You slide two fingers inside her."with dis15
    show cx 37
    a "O-O-Ohhh m-my g-god...!"with dis08
    show cx 36
    a "*Her hips spasm* Y-You put t-them inside me..."with dis08
    mc "Yes I did..."
    show cx 37
    a "Ahhh..." with dis08
    show cx 36
    mc "Do they feel good?"with dis08
    scene cx 38
    a "Yes, they do..." with dis12
    mc "Do you want me to move them?"
    a "Y-Yes... p-please!"
    $ renpy.music.set_volume(0.2, delay=6.0, channel='music2b')
    $ renpy.music.set_volume(0.6, channel='music3')
    play music3 wetting1 fadein 5
    show astro3 with dis2
    a "O-Ohhh..." with dissolve
    a "My... GOD!!"
    a "This is... aaaAAah...!"
    mct "Annie's pussy feels so tight, even more than I imagined..."
    mct "But she's so wet that her vagina lets me plunge my fingers in and out with ease..."
    a "*Panting* Aaaaah... aaahhh!"
    a "Yeah!"
    a "P-Please, keep g-going!"
    a "*Panting* K-Keep going, [mc]! Y-You’re hitting just the... r-right spot!"
    scene black
    show astro4 
    with Dissolve(2.2)
    blank "{i}You start kissing Annie, while your fingers stroke her at the same steady pace." with dis08
    a "Mmmm.... mmmm.... mmmmmhh!"
    mct "Her lips always feel so soft... I can feel the soft tickle of her breath, it’s almost synced with her accelerated heartbeat."
    a "*High-pitched moaning* Mmmmmhh...!"
    mct "And her little moans are driving me insane..."
    $ renpy.music.set_volume(0.9, delay=2.5, channel='music3')
    scene black
    show astro5
    with Dissolve(2.3)
    a "*Squeals* AAAAAHHhh!" with dis08
    blank "{i}You curve your fingers inside her, changing their positions, and hasten your pace."
    a "OH M-MY G-GOD..."
    a "W-What is going on...?!"
    a "W-What are you *moans* doooooing to m-me...?"
    a "*Squeals* AAAAHHH!"
    a "Y-You have to stop! S-STOP! [mc]!"
    a "Ahhh... S-Stop! Or I'm g-gonna... {i}p-piss{/i} myself!"
    a "OH JESUS!"
    mc "Don't worry, babe..."
    mc "You're not gonna. That sensation is normal – you're about to orgasm."
    mc "Have you ever had one before? Touching yourself to your naughty thoughts...? Have you ever made yourself cum while jilling off in your room by yourself?"
    a "W-What? Aaahhhh...."
    a "An o-orgasm? I d-don't know..."
    mc "I guess that answers my question..."
    a "*Panting* Oh g-god..."
    a "Oh... {i}F-FUCK!"
    a "Aaaaahhh...."
    a "[mc]... S-Seriously... p-please... I d-don't know w-what..."
    a "AAAaaHHHhh!"with vpunch
    a "[mc]!!!"with vpunch
    play sound cum2
    stop music3 fadeout 1
    scene cx 39 with dis08
    play sound2 cum2
    a "AAAAAAAARGHGHHHH!!" with hpunch
    play sound3 cum2
    a "AAAAAAAAHHHHhhh..." with hpunch
    blank "{i}You can feel Annie's thighs squeeze around your hand, as her whole body tightens. Her hips gyrate back and forth as she orgasms from your ministrations." with dissolve
    play soundlow chair4
    show cx 40
    a "*Collapses* Oh my god..." with dis08
    mc "How was that, little lady?"
    a "T-That..."
    a "That was... indescribable..."
    a "My god... is this how you feel every time you... do this?"
    mc "*Chuckles* More or less..."
    show cx 41 with dis12
    pause
    play soundlow blow1
    show cx 42
    blank "{i}You gently pull your fingers out from Annie's insides, completely covered in her own juices." with dis12
    play sound2 chair4
    show cx 42b with dis12
    a "*Leaning back* WOW!" with dissolve
    a "That was incredible!"
    mc "Glad you liked it..."
    a "\"Like\" it? It was the best experience of my life!"
    mc "Nice..."
    a "(Oh my god! I can't believe it!)"
    a "([mc] made me... {i} cum{/i}!)"
    show cx 42c
    a "*Giggles*" with dis08
    a "Hmm?"
    play sound chair4
    show cx 43
    a "*Gets up* W-What's that?!" with dis12
    mc "What?"
    a "That... BULGE!"
    mc "Oh... well..."
    mc "You turn me on so much, Annie... I'd be lying if I said I wasn’t rock-hard the whole time..."
    a "Wow..."
    play sound2 clothes3
    show cx 44 with dis15
    a "Can I..." with dissolve
    a "Can I see it?"
    mct "Oh fuck yes..."
    mc "Of course you can see it... After all, you’re responsible for it..."
    play sound clothes3
    play soundlow clothes
    show cx 45
    a "*Takes off your tights*"with dis17
    mc "Much better..."
    a ". . ."
    play sound2 chair4
    play soundlow whoosh6
    show cx 46 with hpunch
    pause .4
    a "My... {w}GOD!" with dis08
    a "That thing is huge! You have such a big dick...!"
    mc "Y-You had already seen it!"
    a "B-But... I didn't look much at it! That day I was... too nervous!"
    a "And I only saw it from between my legs! I didn't know it went that far down..."
    mc "Well, you have pretty generous hips, so... even if you could only see the tip poking out..."
    show cx 47
    mc "I mean..."with dis
    a "...I g-guess that makes sense."
    a ". . ."
    a "Can I... {w}can I touch it? {w}Please?"
    mc "I want you to kill me if I ever say no to that question..."
    play sound clothes3
    show cx 48 with dis2
    pause
    scene cx 49
    blank "{i}Annie grabs your shaft with tenderness." with dis17
    mc "Oh, yeah..."
    play music3 wetting2 fadein 2
    show astro6 with dis2
    blank "{i}She starts to slowly move her hand along your penis."with dis08
    mc "Ohhh... god..."
    mct "Wow, I wasn't expecting her to take the lead so quickly..."
    mct "I guess she's finally starting to be comfortable with her own sexuality... Or my cock just made her really horny..."
    mc "Oh, Annie..."
    mc "This feels great..."
    a "You made me feel so good with your fingers... You made me c-cum and it felt amazing... I just want to return the favor..."
    mc "You're definitely succeeding at that..."
    mc "That's it, baby..."
    mc "Keep stroking it..."
    mc "AAaahhh..."
    mc "You’re such a good girl, Annie..."
    a "Do you want me to go faster?"
    mc "Oh fuck yes, please..."
    $ renpy.music.set_volume(0.9, channel='music3b')
    stop music3 fadeout 2
    play music3b wetting3 fadein 2
    scene black
    show astro7 
    with dis2
    mc "Ahhhh..." with dissolve
    a "L-Like this?"
    mc "Y-Yeah, just like that..."
    a "(My god, it REALLY is huge...)"
    a "(I could put like 3 hands here and it still wouldn’t cover it all...)"
    a "It's t-throbbing so hard!"
    mc "Ahh... I know..."
    mct "Annie's hands feel so small and soft... but she's squeezing my cock so fucking hard! It feels amazing..."
    mc "Aaaahhh... keep going, Annie..."
    mc "Aaahh... FASTER!"
    $ renpy.music.set_volume(1.0, delay=2.0, channel='music3')
    stop music3b fadeout 2
    play music3 wetting4 fadein 2
    scene black
    show astro8 
    with dis2
    mc "AAAAAHHhhhh..." with dissolve
    mc "Oh, fuck..."
    mct "Man, I can't believe her thin arm isn't tired yet..."
    mc "Oh god, that's it..."
    mc "This is incredible..."
    mc "Aaahh..."
    mc "D-Do you like beating off my cock, Annie?"
    a "I-I do..."
    mc "W-What do you like?"
    mc "Say it... I wanna hear you describe what you’re doing..."
    a "I..."
    a "I love beating off your... massive... pulsing... d-dirty cock..."
    mc "AAAaahh, fuck yes..."
    a "It’s just so big... I don’t want to stop playing with it..."
    a "C-Can we do this more often?"
    a "I-I wanna...{w} practice..."
    mc "Yeah, we can..."
    mct "God... hearing her talk dirty is driving me crazy..."
    mc "*Panting* F-Fuck, I won't last much longer, Annie..."
    mc "You're a natural at this..."
    a "I want to make you cum, [mc]... You were so kind to me..."
    mc "I'm almost there..."
    menu:
        with dis
        "Cum":
            stop music3 fadeout 1
            play sound cum1
            play sound2 cum2
            play sound3 cum3
            scene cx 50
            mc "AAAAAAAARGHH!" with hpunch
            play sound4 cum1
            play sound5 cum2
            play sound6 cum3
            mc "AAAAAaaahhhhhhhh..." with hpunch
            a "W-Wow!"
            a "(Look at all that cum shooting out...)"
            a "(I made that happen?)"
        "Grab Annie and put her on top of you":
            stop music3 fadeout 1
            play sound chair4
            play soundlow chair1
            scene cx 52
            mc "Bring that tight little pussy of yours over here..." with dis08
            show cx 51
            a "Wait..."
            a "W-WHAT?!"with hpunch
            a "I'M NOT READY!"with hpunch
            a "Not yet!"
            a "I'm not ready yet!"
            a "I c-can't take all that! I'm not ready yet! I'm not..."
            a "F-First I have to get myself a-appropriately psyched up f-for..."
            show cx 52
            mc "It's okay, Annie..."
            mc "I won't force you to do anything you don't want to..."
            mc "I just want to feel your pussy lips again..."
            show cx 51
            a "M-My... lips?"
            show cx 53
            mc "Yeah... Like the thighjob in my room, but..."with dis
            show cx 54
            mc "*You softly pull Annie's hips towards you* This time..."with dis15
            show cx 55
            mc "Aahh... you’re in control..." with dis15
            a "Aaahh..."
            scene cx 56
            a "Oh god, it's so warm... and sticky..." with dis
            mc "Oh yeah..."
            play music3 wetting5 fadein 2
            show astro9 with dis2
            blank "{i}Annie immediately starts moving her hips back and forth along your cock, her juices spreading all over you." with dissolve
            a "*Moaning* AAAahh..."
            mc "Oh Annie..."
            mc "F-Fuck, I love your body..."
            mc "How petite you are, how easy it is to move you along my cock..."
            mct "God, I'd love to stretch out her tiny pussy..."
            mc "I want you so bad, Annie... I can’t wait ‘til the day you can finally take this dick... But not yet..."
            a "*Moaning* Aaaahh... aaahhh..."
            a "W-We’ve g-gotta do some practicing b-beforehand, [mc]..."
            a "Aaahhh... I-I have t-to get ready for you..."
            mc "*Panting* Oh g-god, I'm gonna cum..."
            mc "Ahh... I w-was at the edge already... But you’re pushing me over..."
            a "T-That sensation... it's coming again... I c-can feel it..."
            mc "Oh yeah... just a little bit more..."
            a "AAAAaahh... Y-YEAH!"
            mc "I'm almost..."
            stop music3 fadeout 1
            play sound cum1
            play sound2 cum2
            play sound3 cum3
            scene cx 57
            mc "AAAAAAAARGHH!" with hpunch
            play sound4 cum1
            play sound5 cum2
            play sound6 cum3
            mc "AAAAAaaahhhhhhhh..." with hpunch
            a "W-Wow!"
            a "(Look at all that cum shooting out...)"
            a "(I made that happen?)"
    play sound chair1
    play sound2 chair4
    scene cx 58
    mc "MY GOD!" with dis12
    mc "Jesus fucking Christ... that felt...{w} good..."
    play soundlow chair1
    show cx 59
    a "*Lying down next to you* OH MY GOD!" with dis
    a "This has been... {w}the BEST night of my life!"
    show cx 60
    mc "Better than our first night together, you think?"
    show cx 59
    a "Definitely better..."
    mct "I love feeling her warm body curled up next to me. It feels comfortable... I almost feel... safe."
    a "This is exactly how I imagined everything would be... no, even better!"
    a "Everything's been simply..."
    a "*Sighs* Perfect..."
    show cx 60
    mc "Yeah, I can hardly imagine a better date..."
    mc "And hey, it's not even over yet!"
    show cx 59
    a "I wish we could stay like this forever..."
    show cx 60
    mc "Me too. It's too bad we have to leave already. Maybe next time, we can visit this server for a longer period of time."
    mc "At any rate, I'd rather not be here when the Astrocorp lady comes back and sees the mess we made..."
    show cx 59
    a "*Giggles* That's true!"
    stop music2b fadeout 9
    play sound chair3
    show cx 62
    blank "{i} You both stand up and start getting dressed."with dis15
    play music2 synth3 fadein 9
    show cx 61
    a "*Giggles* I hope we don't bump into her when we get out of here!"
    show cx 62
    mc "*Chuckles* Yeah, that'd be awkward."
    show cx 61
    a "Where do you wanna go now?"
    show cx 62
    mc "Katniss told us there were flyers with all the available activities in that cabin where the teleporter left us."
    mc "So... let’s head there first and check it out. We still have some time!"
    mc "I don't know about you, but I need a minute to replenish fluids..."
    show cx 61
    a "Oh, I saw a hot cocoa dispenser in the canteen!"
    a "I'll bring you a cup of hot chocolate!"
    show cx 62
    mc "Sweet! I don't know why it's so cold here, but a hot chocolate would definitely hit the spot."
    show cx 63
    a "Wait for me in our room, it'll just be a minute!"with dis
    mc "You'd better hurry up! I’m counting the seconds until I can see that booty of yours again..."
    a "*Giggles* Don't be silly!"
    a "It won't go anywhere... you know it's only for you..."
    mc "That’s my girl..."
    show cx 64
    a "*Putting on her pants* Start thinking about what you wanna do! Be right back!"with dis
    mc "On it!"
    play sound doorspace
    show cx 1 with dis2
    mc "Phew..."with dissolve
    mct "Boy, that was... AWESOME! I can’t believe things have gotten so hot and heavy with Annie!"
    mct "She's not only cute, but also sexy as hell when she wants to be..."
    mct "Things have worked out wonderfully so far!"
    play soundlow zip
    mc "*You finish getting dressed* (But anyway, I should get out of here before an employee comes back...)"with dis
    mct "Let's go back to the cabin."
    $ anniefingers = True


label xenoattack:
    stop music2 fadeout 4
    stop music
    stop musicb
    show caa 1 with Dissolve(2.2)
    play music2b romantic2 fadein 8
    play sound coffee
    a "*Pours herself a cup of hot chocolate*" with dissolve
    a "(I can't believe we did that!)"
    a "(That was... amazing!)"
    a "(At first I was nervous as hell, but... after he calmed me down, everything felt... like a dream.)"
    show caa 3
    a "(I mean... well, of course, we didn't do... {i}everything.)" with dis
    a "(Obviously.)"
    show caa 2
    a "(M-Maybe the next time...?)"
    show caa 3
    a "(Or... maybe not... yet. Probably a bad idea.)"
    a "(Right?)"
    a "(This is a big step...)"
    a "(I mean...)"
    a "(Am I ready?)"
    show caa 2
    a "(I think I'm ready.)"
    show caa 3
    a "(O-Or maybe not. Am I?)"
    show caa 2
    a "(Yes. If it's [mc], I feel like I want to.)"
    show caa 3
    a "(Although...)"
    a "(His thing is... {size=44}big{/size}. And I'm... {size=18}small.{/size})"
    a "(Will I be able to...)"
    show caa 2
    a "(Never mind, I’ll think about that later.)"
    play soundlow splash2
    show caa 4
    a "*Makes a small jump and turns around* (This date is turning out to be the best night of my life!)"with dis08
    a "(Thanks Astrocorp!)"
    show caa 5
    a "*Giggles*" with dis08
    stop music2b fadeout 8
    play music spaceshipambient fadein 6
    show caa 6 with dis2
    pause
    a "Hmm?" with dis08
    show caa 5
    a "(What's this?)" with Dissolve(1.4)
    a "(Red paint?)"
    show caa 8 with dis
    pause
    show caa 9 with Dissolve(1.8)
    pause
    a "W-W-Wha..." with dis08
    a "*Nervous laughter* W-What's this?"
    a "F-Falazio? Is t-that you?"
    a "*Nervous laughter* I d-didn't know there was a show in the canteen tonight!"
    show caa 10
    a "It's n-not really my thing, though, s-so you c-can s-stop pretending, haha!"
    a "O-Okay?"
    play sound lightstage
    play sound3 lightstage
    play sound2 lightstage
    scene black
    play musicb spaceshipalarm
    pause .2
    show caa 11 with dis17
    play soundlow announcement2
    pas2 "Emergency alert: Unidentified biological agent." with dis
    pas2 "Security locks activated. Quarantine initiated."
    pas2 "Please do NOT move from your current location."
    stop musicb fadeout 4
    scene greendark with Dissolve(2.3)
    pause
    mct "What the hell is going on? Why did the lights go out?"with dis12
    play soundlow screamwoman volume 0.25
    a "{size=20}AAAAAAAAAAAAAAGH!!!!" with hpunch
    play sound5 chair1
    scene caa 13
    mct "*Startled* W-Was that Annie?"with dis08
    mc "ANNIE?!"with hpunch
    mct "Fuck, what the hell is happening?!"
    play sound noise1
    mct "There has to be some source of light somewhere around here!"
    play sound2 noise1
    mct "I can't see shit like this!"
    mct "Is this some sort of flashlight?"
    play sound beep3
    show caa 15
    pause .02
    show caa 13
    pause .02
    show caa 15
    pause .02
    show caa 13
    pause .02
    show caa 15 with Dissolve(.2)
    mct "Yes! This will do."with dis08
    play sound4 doorspace
    play music xenosong1
    show caa 16 with dis15
    mc "H-Holy fuck, it’s even colder than bef-f-fore..." with dissolve
    mc "And where the hell is everyone?!"
    mc "HELLO? Is anybody there?!"with hpunch
    mct "Now that I think about it... I didn’t see anyone on the way here."
    mct "In fact, I... I haven't actually seen anyone apart from me and Annie for a long time..."
    mct "Where has everyone gone? Is this part of \"Astrocorp's Dating Experience\"?"
    mct "If it is, I know Annie won't enjoy it, that's for sure... This shit is even creeping ME out, and she’s way more squeamish..."
    play sound footsteps
    show caa 17 with dis2
    mc "HELLO?!" with dissolve
    mc "*Shivering* (My hands are freezing...)"
    mct "I’ve gotta find Annie and get out of here. I hope the canteen is warmer than this hall..."
    play sound2 doorspace
    show caa 18 with dis2
    mct "What the fuck is going on, man? Where are the other passengers...?" with dissolve
    mct "I didn't read anything about an event like this on Astrocorp's website... If it was some sort of performance, they'd have warned us when we first arrived, right? Not everyone enjoys this kind of stuff..."
    mc "*Shivering* (I have to keep walking...)"
    play sound3 footsteps
    show caa 19 with dis15
    mct "Is that what I think it is? A whole trunk of clothes!"with dissolve
    mct "Thank goodness, I thought I was gonna freeze to death."
    play sound clothes3
    play sound2 clothes2
    show caa 20 with dis17
    mct "Ahh... much better! I feel warmer already." with dissolve
    mct "Hmm... looks like a space captain’s outfit."
    mct "Well, it's not stealing if they just leave it lying around in the hallway."
    show caa 21 with dis12
    mct "And what's this?" with dissolve
    mct "Wait... I know that device, I saw it in Ion."
    mct "If I recall correctly, it’s some sort of intercom."
    mct "It's outdated technology, but people used it to record voice memos, almost like personal audio diaries... vintage tech that’s seeing a resurgence in popularity, like Polaroid cameras."
    mct "And that's an audio card next to it. I wonder whom it belonged to..."
    menu:
        with dis
        "[gr]Grab the audio log device":
            $ xenodiary = True
            mct "I can't help but be curious. And maybe it contains some useful information..."with dissolve
            mct "Let's listen to it."
            show screen audiologs
            show caa 22
        "Don't touch it":
            mct "Bah. I doubt it contains any useful information..."with dissolve
            mct "Let's continue."
            show caa 18
    with dis15
    if xenodiary:
        play sound beep3
        show newaudio with dis04
        hide newaudio with dis04
    pause
    if card1listened:
        mct "Isaac Langston, eh? What's your story...?"with dissolve
        mct "Maybe I can find more audio logs around here."
    play sound footsteps
    show caa 23 with dis22
    mct "Okay, I think this is the door that leads to the canteen and the cinema. We walked through it when we went to the movies." with dissolve
    play sound doorlocked
    play sound2 doorlocked
    show caa 24
    mct "What? It's locked!" with dis12
    mct "Fuck! Is this because of the emergency shutdown from before?"
    mct "This bridge is my only way to get to Annie and the escape ships..."
    stop sound fadeout 1
    stop sound2 fadeout 2
    show caa 25
    mct "Dammit, looks like the door only opens with a numpad."with dis
    show caa 26
    mct "And judging by these tools, someone has been trying to open the door... unsuccessfully, I guess."with dis
    if xenodiary:
        mct "Is that another audio card?"
        play sound clothes3
        show caa 27
        mc "*Picks it from the ground* (Yeah, it is.)"with dis08
        if card1listened:
            mct "I wonder if it's from Isaac as well..."
        else:
            mct "Who's leaving all these behind?"
    play sound jumpscare
    show caa 28
    aaa "THEY LOCKED US IN HERE!" with hpunch
    show caa 29
    mc "F-Fuck!"with dis08
    mc "You scared me!"
    show caa 28
    aaa "They don't want us to leave!" with Dissolve(.7)
    aaa "But why would we want to leave?"
    aaa "We've been blessed!"
    show caa 29
    mct "Why does this guy look so fucking nuts..." with Dissolve(.7)
    mc "Um... Well, I'm happy to finally see someone."
    mc "Do you know what happened? Everything was fine one hour ago!"
    mc "My date left the room and went to the canteen, and a few minutes later... the lights went out and everyone had disappeared!"
    show caa 28
    aaa "The emergency system blocked the exits, everyone else is either hiding... or dead!"with Dissolve(.7)
    show caa 29
    mc "What?! Why?! What is going on? Are we being boarded by some kind of space pirates?"with dissolve
    show caa 28
    aaa "The doctor said I could be one of the chosen ones! I have to be!"with Dissolve(.7)
    show caa 29
    mc "*Sighs* (He not only looks nuts, he {i}is{/i} completely nuts.)"with Dissolve(.7)
    mc "There's a trunk with clothes back there, by the way. You must be freezing."
    show caa 28
    aaa "I'm good. Cold just makes you a better host..."with Dissolve(.7)
    aaa "That’s why she lowered the temperature..."
    show caa 29
    mct "The fuck is he talking about?"with Dissolve(.7)
    mc "Okay... Uhh... I guess you don't know how I can get to the canteen."
    show caa 30
    vas "Oh, I do! Employees know the code for the door! I'm Vasil, I take care of the station's cleaning, and help the doctor sometimes..."with Dissolve(.7)
    show caa 29
    mc "Really?! That's great! Let's get out of here then!"with Dissolve(.7)
    show caa 28
    vas "Oh... no, no! Not yet! Not until I have my egg!"with Dissolve(.7)
    show caa 29
    mc "W-What egg? What the fuck are you talking about?"with Dissolve(.7)
    show caa 30
    vas "The egg! Doctor Mercer said I could be chosen! I need that egg!"with Dissolve(.7)
    vas "It's in the laboratory! Bring it to me and I'll open the door! I promise, yes..."
    show caa 29
    mc "What laboratory... dude, you can go yourself. I don't have time for this shit! My date could be in danger, open the damn door!"with Dissolve(.7)
    show caa 28
    vas "No, no, no... I need the egg... I can't leave without it... I need it, I need it!"with Dissolve(.7)
    vas "But it's dangerous... Bring the egg and I'll open the door, I promise..."
    show caa 29
    mc "Come on... isn't there anything else you want? I... could pay you."with Dissolve(.7)
    show caa 28
    vas "Money? Yes... I could buy another egg on Nox 7... I know a man..."with Dissolve(.7)
    vas "Give me 500 eternals and I'll open the door, yes..."
    show caa 29
    mc "500 eternals?!"with dissolve
    menu:
        with dis
        "Pay him 500 eternals":
            if money >= 500:
                show screen eternals
                hide screen audiologs
                with dis
                play sound coins
                $ money -= 166
                pause .05
                $ money -= 167
                pause .05
                $ money -= 167
                pause .05
                hide screen eternals
                show screen audiologs
                mc "*Sighs* Okay, fine, take your fucking money." with dis
                show caa 30
                vas "Ah... yes! YES! I can buy one with this!"with dissolve
                vas "I'll open the door, my friend..."
                play sound3 numpad
                show caa 94 with dis15
                pause 2
                play sound3 doorspace
                show caa 95 with dis
                pause
                show caa 30
                vas "You can go save your girl! G-Good luck!"with dis12
                show caa 29
                mc "Thank you!" with dis08
                show caa 29b
                vas "Oh! And... take this bomb! Yes! The commander left it here... it might be u-useful."with dis
                mc "A... b-bomb? Um... O-Okay, thanks buddy..."
                show caa 29
                mc "Uh... Can I ask what you’re planning to do with that money? What do you wanna buy, exactly?"with dis
                show caa 30
                vas "It's a secret! I can't tell! No, no!"with dis08
                show caa 29
                mc "You know what... I prefer not to know..."with dis08
                $ pay500 = True
                mc "Take care, Vasil."
                jump posposegg
            else:
                mc "Okay, I'll..." with dissolve
                mct "Fuck, I don't have enough money!"
                mct "I guess I have no other choice then..."
        "[gr]Go find the egg":
            mc "*Sighs* I guess I have no other choice..." with dissolve
    mc "Okay... where do I find that... egg?"
    show caa 30
    vas "Excellent, excellent! Go to the lab and grab one of the eggs!"with Dissolve(.7)
    show caa 28
    vas "But it has to be a closed one! Don't take one that has been opened already!"with dis04
    show caa 30
    vas "They're big! You'll see them on top of a table at the end of the room..."with dis04
    show caa 29
    mc "The lab? Do you mean the botanical garden?"with Dissolve(.7)
    show caa 30
    vas "Yes, yes..."with Dissolve(.7)
    show caa 29
    mct "I think I saw it earlier. I was thinking of buying Annie one of those roses that glow in the dark before leaving."with Dissolve(.7)
    mc "Okay, I know where it is. I'll go get that \"egg\"... Wait for me here."
    show caa 30
    vas "I won't move from here..."with Dissolve(.7)
    show caa 31 with dis15
    if xenodiary:
        $ card42 = True
        play sound beep3
        show newaudio with dis04
        hide newaudio with dis04
    pause
    if card42listened:
        mct "What the hell... these logs are starting to get creepy..." with dis08
        mct "Anyway... it's a bit of a hike until the botanical garden. I'd better get going."
    else:
        mct "It's a bit of a hike until the botanical garden. I'd better get going."with dis08
    mct "I hope Annie is alright..."
    play sound footsteps
    if xenodiary:
        show caa 22 with dis2
    else:
        show caa 18 with dis2
    play soundlow whisper1
    pause
    play sound doorspace
    show caa 32 with dis2
    pause
    play sound2 footsteps
    show caa 33 with dis2
    mct "Okay, if I remember correctly now I had to turn right and then..." with dis08
    play sound3 gunload
    play sound4 lasercharge
    show caa 34
    aaa "Turn around reeeeeal slow." with dis
    aaa "No sudden moves. Else, I'll shoot you in the fucking head."
    aaa "Understood?"
    show caa 36
    mc "*Putting your hands up* E-Easy there, buddy. I'm not a threat. I'm just a passenger, a customer of Astrocorp!"with dis12
    mc "W-Who are you?"
    show caa 35
    com "Commander Hasler, leader of the Second Brigade of the Galactic Union."
    show caa 36
    mc "Okay man, looks like we're on the same side here, so... could you stop pointing that thing at me, please?"
    com ". . ."
    play sound holster
    show caa 37
    com "Okay, I believe you." with dis
    show caa 38
    mc "Thank god..."
    mc "Why are you here? Do you know what happened?"
    show caa 37
    com "I... was just visiting the theater today on a date with my girlfriend. She was suddenly killed when one of those things jumped on her when we were exiting the theater."
    show caa 38
    mc "Holy shit... I'm sorry to hear that."
    show caa 37
    com "She’ll be fine. But I can't die here. If I lose my level, I'll also lose my job at the Brigade. I can't afford that. Plus, I have to avenge her."
    show caa 38
    mc "But who is attacking us??"
    show caa 37
    com "{i}What{/i} is attacking us."
    show caa 38
    mc "\"What\"...?"
    show caa 37
    com "A few months ago, I started hearing rumors about some kind of... plague that was spreading through Andromeda with great speed."
    com "I thought it was all bullshit, but... today I saw it firsthand."
    com "We need to destroy this entire station to kill the infection."
    show caa 38
    mc "What the hell..."
    mc "Um... Okay, do your thing, I don't really care about what happens to this station. I have to go to the botanical garden."
    play sound3 gunload
    play sound4 lasercharge
    show caa 35
    com "The botanical lab?! WHY?" with dis
    show caa 36
    mc "*Putting your hands up* A m-man told me to grab something for him there!"
    mc "I'm looking for my date, but there's a door blocking the way, and only he knows the code!"
    show caa 35
    com "Don't go to the lab!"
    show caa 36
    mc "W-Why? And why is everyone calling it the “lab”?"
    show caa 35
    com "That doesn't matter!"
    show caa 36
    mc "But the door..."
    play sound holster
    show caa 37
    com "I can open that door myself." with dis
    com "Do me a favor instead, and I'll open it for you."
    show caa 38
    mc "What kind of favor?"
    show caa 38b
    com "This."with dis
    com "Go to the generator room and place this explosive next to the main generator."
    mc "An explosive...?"
    com "It won't be activated until I trigger the remote control, don't worry."
    mc "Okay, so..."
    show caa 38
    mc "If I leave this explosive in the generator room... you'll open the door that leads to the canteen?" with dis
    show caa 37
    com "Yes. I'd go myself, but I need to place another explosive at the other side of the station."
    show caa 38
    mc "*Sighs* Okay... I'll do it."
    show caa 37
    com "Good."
    play sound holster
    show caa 40
    com "And take this gun. You might need it."with dis
    show caa 39
    mc "Really? You're giving it to me?"
    show caa 40
    com "Just take it and don't ask so many questions."
    show caa 39
    menu:
        with dis
        "[gr]Take the gun":
            $ xenogun = True
            play sound4 holster
            show caa 42
            mc "*Taking the pistol* Thanks." with dis
            mc "Are you sure you're gonna be okay without your gun?"
            show caa 41
        "Don't take it":
            mc "Thanks, but I don't need it. You can keep it."with dissolve
            com ". . ."
            play sound2 holster
            show caa 37
            com "Suit yourself."with dis
            show caa 38
            mc "I'd feel bad taking your only gun."
            show caa 37
    com "It's not mine."
    com "I found it lying around, along with some scraps of armor and some engineering gadgets."
    if xenodiary:
        show caa 43
        com "I also found these old audio cards next to it." with dis
        mc "Oh, I found some of those too."
        com "They were inside an almost empty backpack with a big hole at the bottom. I’m guessing the owner must have been losing their stuff wherever they passed."
        if xenogun:
            mc "Do you mind if I take these too?"
        else:
            mc "Do you mind if I take these instead?"
        com "Nah, they're all yours."
        if xenogun:
            show caa 42
        else:
            show caa 38
        mc "Alright then, I'll go to the generator room and... place the bomb."with dis
    else:
        if xenogun:
            show caa 42
        else:
            show caa 38
        mc "Alright then, I'll go to the generator room and... place the bomb."
    if xenogun:
        show caa 41
    else:
        show caa 37
    com "Thank you for your cooperation. Meet me back at the door you mentioned. I'll open it and help you save your girl."
    if xenogun:
        show caa 42
    else:
        show caa 38
    mc "Done deal."
    if xenogun:
        show caa 41
    else:
        show caa 37
    com "Good luck."
    show caa 33 with dis17
    if xenodiary:
        play sound beep3
        $ card43 = True
        $ card48 = True
        show newaudio with dis04
        hide newaudio with dis04
    pause
    if card48listened:
        mct "A dream...?"with dissolve
        mct "It wouldn't be the first time someone dreamt about Eternum, but in 1979? 45 years before Eternum's launch? That's... unbelievable..."
    play sound doorspace
    show caa 44 with dis2
    pause
    play sound2 footsteps
    show caa 45 with dis2
    play soundlow whisper2
    mct "Hmm..." with dissolve
    mct "If I go left, I'll get to the lab. If I go right, the generator room."
    mct "That Vasil was totally crazy, I can't trust him. But... can I trust Commander Hasler? I feel like he's hiding something from me..."
    menu:
        with dis
        mod "Choose whatever you like most or check out both paths."
        "Help Vasil and go get an egg":
            $ vasilhelp = True
            play sound footsteps
            show caa 47
            mct "I don't trust that Hasler guy."with dis12
            mct "Vasil might be weird, but at least he seemed sincere."
            mct "To the lab."
            play sound2 footsteps
            show caa 72 with Dissolve(2.1)
            mct "I think I'm going the right way..."with dissolve
            play sound4 doorspace
            show caa 73 with dis2
            mct "This is it..."with dissolve
            mct "The... \"lab\"."
            mct "Why does a dating and experiential company even need a laboratory?"
            show caa 74
            mct "Looks like someone has been here already... and whoever they were, they left one of those sound cards behind."with dis
            show caa 73 with dis12
            if xenodiary:
                play sound beep3
                $ card55 = True
                show newaudio with dis04
                hide newaudio with dis04
            pause
            show caa 75 with dis17
            mct "Okay, I need to find a table with..." with dissolve
            play sound2 chain
            play sound3 jumpscare
            show caa 76
            mer "Y-You!" with hpunch
            show caa 77
            mc "FUCK!"
            mc "W-What... Who are you? Why are you handcuffed to that pipe?"
            show caa 76
            mer "That fucking mercenary! He did this to me!"
            mer "He's trying to kill us all!"
            show caa 77
            mc "Do you mean... Commander Hasler?"
            show caa 76
            mer "Yes! He came in here and threatened me!"
            mer "He said he'd destroy the entire station!"
            show caa 77
            mc "Do you know why? Is it because of those eggs?"
            show caa 76
            mer "What eggs? The ones on my table? I found those on Nox 7! I don't even know what they are!"
            mer "Please, you have to uncuff me! I beg you!"
            show caa 74
            mer "The keys to the cuffs are on the desk over there!"with dis
            mc "The ones next to the tools?"
            mer "Yeah! Another man came here a few minutes ago, but he didn't want to help me! I think he's working with Hasler!"
            mc "Hmm..."
            menu:
                with dis
                "Uncuff her":
                    $ freemercer = True
                    play sound keys
                    play sound3 chain
                    show caa 78 with dis15
                    play sound2 chaindrop
                    mc "Alright..." with dis08
                    mc "Don't make me regret this."
                    show caa 79
                    mer "Thank you, THANK YOU! You have a good soul, thank god!"
                    mer "Who are you?"
                    show caa 78
                    mc "I'm [mc], I just came here to go on a date, like everybody else, I guess. Do you know anything about what's happening in this station?"
                    show caa 79
                    mer "Nothing! I was working on a new serum for my micro-algae when suddenly, the power went out. Next thing I knew, everyone was missing!"
                    show caa 78
                    mc "Do you know Vasil?"
                    show caa 79
                    mer "Of course, he's my assistant! He's not... the smartest, but he has a good heart."
                    mer "I had just sent him to the hangar to leave the station when that mercenary arrived and handcuffed me."
                    show caa 78
                    mc "I see... Well, you should leave the station ASAP. I don't know what's out there, but... it's not good. Find one of the teleporters and get out of here."
                    show caa 79
                    mer "You're not coming?"
                    show caa 78
                    mc "I have to find someone. My date is missing."
                    show caa 79
                    mer "I see... I'll be on my way, then. Good luck, and thanks again!"
                "Don't uncuff her":
                    show caa 77 with dis
                    mc "I'm... I'm sorry, I can't trust you." with dissolve
                    show caa 76
                    mer "WHAT?!"with hpunch
                    mer "You're gonna leave me here? To be devoured by those things?!"
                    show caa 77
                    mc "I'll fix this! As soon as I get out of here, I'll send help, I promise!"
                    show caa 76
                    mer "You can't do this to me!"
                    mer "You're even worse than that mercenary! I curse you!"
                    show caa 77
                    mc "I'm sorry."
            show caa 75 with dis15
            mct "Okay, and now... where are those damn eggs?" with dissolve
            play sound footsteps
            show caa 80 with dis15
            mct "Hmm... those things definitely look like eggs... more or less."with dissolve
            mct "They're bigger than I thought, though."
            show caa 81
            mct "One of the unhatched ones..."with dis
            mct "I wonder why he wants one of these..."
            mct "And why the hell are they so big? They look like dinosaur eggs."
            play soundlow whisper1 fadein 1
            menu:
                with dis15
                "Take a look inside the open eggs\n[red][mt](Death)":
                    show caa 82 with dis12
                    mct "That's an odd way of opening."with dissolve
                    show caa 83
                    mct "Hmmm..."with dis
                    mct "And they're not empty. They’re full of..."
                    mct "Wait, is that moving?"
                    play sound punch
                    play soundlow chestbuster3
                    show caa 84
                    mct "Hgggg!!!" with hpunch
                    play sound2 fall3
                    play sound3 fall
                    play sound4 chestbuster2
                    show caa 85
                    mc "*Falling on your knees* (W-WHAT THE HELL IS...)"with hpunch
                    mct "HGGG!!"with hpunch
                    mct "I CAN'T...!"with hpunch
                    play sound death
                    pause .3
                    show black
                    pause .1
                    hide black
                    pause .2
                    show black
                    pause .1
                    hide black
                    pause .3
                    show black
                    pause .1
                    hide black
                    pause .1
                    show black
                    pause .05
                    hide black
                    pause .05
                    show black
                    pause .05
                    hide black
                    pause .03
                    show black
                    pause .03
                    hide black
                    pause .03
                    show black
                    pause .03
                    hide black
                    pause .03
                    show black
                    stop sound4
                    $ xenodeath1 = True
                    jump xenodeath
                "Grab a closed egg and leave":
                    mct "I don't have time to waste."with dissolve
                    mct "Annie needs me."
                    show caa 80b with dis12
                    mct "Let's go back to Vasil."with dissolve
                    play sound footsteps
                    show caa 73 with dis2
                    pause
                    play sound doorspace
                    show caa 72 with dis2
                    jump xenolater
        "Help Commander Hasler and place the bomb":
            play sound footsteps
            show caa 46
            mct "I don't trust that Vasil guy."with dis12
            mct "Hasler might be hiding something, but at least he's not crazy."
            if xenogun:
                mct "He even gave me a gun, so he trusts me."
            mct "To the generator."
            play sound2 doorspace
            show caa 48 with Dissolve(2.12)
            play sound4 footsteps
            mct "This station is bigger than I thought..."with dissolve
            mct "The corridors seem to never end..."
            mct "Fuck, I'd like to think Annie left this place and she's safe, but I know she'd never leave without me, no matter how scared she was..."
            mct "I hope she's alright..."
            play sound3 xenovideo fadein 2
            show xenoattack with dis17
            pause 6.7
            if xenogun:
                play sound4 jumpscare
                play sound gunload
                scene caa 49
                mc "*Drawing your weapon* WHO'S THERE?!" with hpunch
            else:
                play sound4 gore
                $ xenodeathgun = True
                stop music
                scene black
                jump xenodeath
            mc "*Panting*"
            mc "(I could swear I heard something...)"
            mc "I know you're there! Show yourself!"
            blank ". . ."
            play sound holster
            show caa 50
            mct "Fuck, I need to finish this thing ASAP..." with dis
            mct "I'll enjoy blowing this cursed place up."
            show caa 48
            mct "Let's continue." with dis
            play sound2 doorspace
            show caa 51 with dis2
            mct "Finally, the generator room."with dissolve
            play sound4 footsteps
            show caa 52 with dis2
            mct "This seems to be the center of the room. I'll leave it here."with dissolve
            play sound3 gunload
            ast "DON'T MOVE!"
            show caa 53
            mc "*Turning around* E-Easy there."with dis12
            show caa 54
            ast "YOU'RE ONE OF THEM! YOU BROUGHT THIS UPON US!" with dis
            show caa 55
            mc "One of them? I don't even know what you’re talking about!"
            show caa 54
            ast "Those... things! Claire was feeling sick s-so I brought her to the infirmary, and..."
            ast "W-when I was about to leave, that... m-monster exploded out of her chest! It killed her!"
            show caa 55
            mc "You need to calm down, Katniss."
            show caa 54
            ast "How do you know my name?!"with hpunch
            show caa 55
            mc "We met when I first arrived at the station... just a few hours ago, remember? [mc] and Annie."
            show caa 53
            mc "You welcomed us and suggested that we visit the theater and the Zero-G room." with dis
            ast ". . ."
            play sound holster
            show caa 56
            ast "I remember you." with dis
            mct "Thank god..."
            ast "What is going on here?"
            mc "I know as much as you. I'm just trying to find Annie and get out of here."
            show caa 57
            mc "*Placing the explosive* You should go to the hangar and use one of those teleporters to go back to the Entrance Hall." with dis12
            ast "Is... is that a bomb?"
            mc "Um... yeah, it's a long story. The door that leads to the canteen is locked, and a man asked me to..."
            play sound chestbuster1
            show caa57
            pause 1.3
            scene caa58
            pause 0.1
            scene caa58b
            pause .2
            call screen qtexeno with dissolve
            pause
label xenowin:
    play sound3 punch
    play sound4 chestbuster2
    show caa57d
    blank "{i}You grab the creature in the air." with hpunch
    mc "What the hell is this..."
    show caa 59b
    ast "T-That's... that's what came out of Claire's chest!"
    show caa 59
    play sound chestbuster2 fadein 1
    mc "This thing caused all the chaos? It doesn't even have eyes... is it blind?"
    play soundlow chestbuster3
    play sound bonebreak
    play sound2 bonebreak
    show caa 60 with dis08
    pause .4
    play sound3 blood1
    play sound4 clothes1
    show caa 61 with dis12
    mc "They don't seem like a big threat..."with dissolve
    show caa 59b
    ast "They don't seem like a big threat?! I don't even know how the hell you saw it coming! I'd be dead if I'd been in your place!"
    if xenodiary:
        show caa 62
        mc "What does it have inside of its mouth?" with dis
        show caa 63 with dis
        mc "Another card..." with dissolve
        mc "I guess we're not the first ones this thing attacked..."
    else:
        show caa 61
        mc "Maybe..."
    show caa 59b
    mc "I need to go back to the living areas, Katniss."with dis
    mc "You go to the hangar and take one of the remaining escape pods or teleporters."
    ast "O-Okay!"
    ast "D-Don't get eaten!"
    mc "I'll try..."
    play sound footsteps
    show caa 51 with dis2
    if xenodiary:
        $ card67 = True
        play sound beep3
        show newaudio with dis04
        hide newaudio with dis04
    pause
    play sound doorspace
    show caa 48 with dis2
    play soundlow whisper2
    jump xenolater
label xenolose:
    play soundlow trashcan
    play sound3 chestbuster2
    play sound4 risinglong2
    show caa57c
    mc "AAAAAAARGH!!!" with hpunch
    play sound blood2
    mc "WHAT THE FUCK!"
    show caa 59b
    ast "That's what came out of Claire's chest!" with hpunch
    play sound3 blood3
    show caa 58b
    mc "GET IT OFF ME!" with hpunch
    ast "W-What?!"
    play sound2 blood2
    mc "GET IT OFF ME!!!" with hpunch
    play sound death
    pause .3
    show black
    pause .1
    hide black
    pause .2
    show black
    pause .1
    hide black
    pause .3
    show black
    pause .1
    hide black
    pause .1
    show black
    pause .05
    hide black
    pause .05
    show black
    pause .05
    hide black
    pause .03
    show black
    pause .03
    hide black
    pause .03
    show black
    pause .03
    hide black
    pause .03
    show black
    stop sound4
    $ xenodeath1 = True
    jump xenodeath
label xenolater:
    pause
    play sound2 footsteps
    show caa 44 with dis2
    pause
    play sound3 doorspace
    show caa 33 with dis2
    pause
    play sound4 footsteps
    show caa 32 with dis2
    pause
    if vasilhelp and not freemercer:
        show caa 31 with dis15
        mct "Jesus Christ, this fucking egg weighs a ton..."with dissolve
        show caa 29
        mc "*Lifting the egg* Is this what you wanted?"with dis12
        show caa 30
        vas "Ahh... yes, YES!" with dis08
        vas "The egg is finally with Vasil!"
        show caa 29
        mc "Will you open the door now?" with dis08
        show caa 30
        vas "Of course, OF COURSE!" with dis08
        vas "Vasil keeps his promises..."
        play sound3 numpad
        show caa 94 with dis15
        pause 2
        play sound3 doorspace
        show caa 95 with dis
        pause
        play sound clothes2
        show caa 93
        vas "You can go save your girl! Good luck!"with dis12
        mc "Thank you!"
        mc "Uh... Can I ask what you’re planning to do with that?"
        vas "It's a secret! I can't tell! No, no!"
        mc "You know what... I prefer not to know..."
        mc "Take care, Vasil."
        vas "*Giggles* The egg is all mine!"
        jump posposegg
    show caa 64 with dis2
    mct "What...?" with dissolve
    mc "Hasler? What is going on here?"
    com "I'll ask one last time. Where do they come from?"
    vas "*Crying* I d-don't know, I swear!"
    show caa 65
    vas "They've always been here! The first reports date back 10 years!"with dis
    vas "That's all we know!"
    show caa 64
    com "So it's all Ulysses’ doing?"with dis
    vas "No! They've always been here! They're not programmed!"
    com "You're not making any sense."
    com "Where did Doctor Mercer find those eggs?"
    vas "*Crying* I d-don't know..."
    com "Then you're not useful to me anymore."
    show caa 65 with dis
    pause .2
    if freemercer:
        play sound gunshot
        play sound4 gore
        show caa 86 with hpunch
        pause .5
        play sound2 fall2
        play sound3 fall
        show caa 87 with dis15
        play sound7 blood1
        mc "*Hyperventilating* W-What..."with dis08
        mc "D-Doctor Mercer?"
        play sound5 holster
        play soundlow whisper2
        show caa 88 with dis17
        mer "Are you okay, Vasil?"with dis08
        vas "*Crying* He hurt me..."
        mer "Shhh... It's alright now..."
        mer "Everything will be fine soon..."
        vas "Can I... Can I have an egg now?"
        mer "No... Not yet, Vasil... I have something much more special reserved for you... You just have to wait a bit longer..."
        mer "We will help this stranger now, and then we will leave together, alright?"
        vas "Alright..."
        play sound3 numpad
        show caa 89 with dis15
        pause 2
        play sound3 doorspace
        show caa 90 with dis
        pause
        show caa 91
        mer "You can leave. Go save your girl."with dis12
        mer "Thank you for your cooperation."
        show caa 92
        mc "You're fucking insane..."
        mc "Are you the one behind this whole nightmare?"
        show caa 91
        mer "God, no, I wish..."
        mer "But I've been studying these creatures for a long time. The plague of Andromeda... the ultimate stage of evolution... an improved, advanced version of the ones we've seen so far... the perfect predator."
        mer "The old lab at this station was the perfect cover for my studies."
        show caa 92
        mc "What are you trying to do?"
        show caa 91
        mer "The simulation of Eternum is perfect, [mc]. They say it’s more real than real life."
        mer "If I can isolate the DNA of these specimens, I can try to create them on the other side too, don't you understand?"
        show caa 92
        mc "That's completely loony. You're crazy."
        show caa 91
        mer "Gregor Mendel was also labeled as a madman, and today we call him the father of genetics."
        mer "We'll see what people call me in 50 years..."
        show caa 92
        mc "Whatever you say..."
        show caa 91
        mer "Goodbye, [mc]..."
    else:
        play sound laser3
        show caa 66 with Dissolve(.2)
        show caa 65 with dis08
        play sound2 fall3
        pause
        show caa 67 with dis12
        play sound3 numpad
        mc "W-What the hell are you doing?!" with dissolve
        mc "Why did you kill him?!"
        play sound3 doorspace
        show caa 68 with dis
        pause
        show caa 69
        com "Don't worry, our... {i}friend {/i}told me the code of the door. You can go, as promised."with dis
        show caa 70
        mc "You're a fucking psycho! You didn't have to shoot him!"with dis
        show caa 69
        com "I did what I had to do."with dis
        com "Now go find your girl and get out of this place before everything blows."
        mct "This bastard used me..."
label posposegg:
    play sound doorspace
    show caa 71 with dis2
    mct "Why... How..."with dissolve
    mct "Anyway... I can't worry about that now."
    if freemercer:
        mct "She can do whatever she likes..."
    else:
        mct "He can do whatever he likes..."
    mct "Fuck them all."
    mct "I’ve gotta save Annie!"
    play sound2 doorspace
    show caa 96 with dis2
    pause
    mct "Jesus, what the hell happened here...? There's blood everywhere..."with dissolve
    mc "ANNIE?!"
    blank ". . ."
    mct "Darn it..."
    a "*Rapid breathing*"
    mct "What...?"
    show caa 97
    mc "Hmm?" with dis12
    mc "Is that...?"
    show caa 98
    mc "Annie?!" with dis
    a "*Whispering* They can't hurt you if you don't see them, they can't hurt you if you don't see them..."
    mc "Annie, is that you?!"
    play sound stairsmetal
    show caa 99
    mc "*You go down the stairs*" with dis15
    mc "Annie!"
    show caa 100
    a "Hmm...?" with dis
    show caa 101
    a "[mc]? Is t-that really you?" with dis08
    mc "Of course!"
    play soundlow punch
    show caa 103
    a "OH MY GOD! I thought I was gonna be eaten alive here!" with vpunch
    a "*Sobbing* I thought everyone had already left except me!"
    show caa 102
    mc "I could have never left alone!"
    mc "Did you really think I'd leave without you?"
    show annienod
    a "*Nods*" with Dissolve(.2)
    scene caa 102
    mc "Oh Annie... I wouldn’t ever do that to you! I care for you way too much... You see how silly you’re being, right?"
    show annienod
    a "*Nods*" with Dissolve(.2)
    scene caa 102
    mc "Are you ready to leave this place?"
    show annienod
    a "*Nods*" with Dissolve(.2)
    scene caa 102
    mc "Let's go."
    play sound stairsmetal
    show caa 96 with dis2
    mc "Can't wait to leave this place and never come back..."with dissolve
    play sound2 doorspace
    show caa 71 with dis2
    mc "I think it's this way..."with dissolve
    play sound3 stairsmetal
    show caa 105 with Dissolve(2.2)
    mc "Yes!" with dissolve
    mc "Look, Annie! A teleporter! We can get out of here!"
    a "Thank god!"
    show caa 106 with dis15
    mc "Now how do I turn this thing on..."with dissolve
    mc "Maybe this button?"
    play sound2 charge
    show caa 107 with dis17
    blank "CHARGING THE DISRUPTORS."with dissolve
    blank "THE TELEPORTER WILL BE USABLE IN 300 SECONDS."
    mc "Oh, come on, really?!"
    a "*Pulling your shirt* [mc]..."
    a "L-Look..."
    show caa 108 with dis15
    mc "*Turning around* Oh shit..." with dis
    mc "What the hell happened to this guy...?"
    a "W-What's that thing?"
    mc "It's one of those audio diaries... I've been finding them all over the station..."
    if card1listened:
        mct "Could this be Isaac? The engineer?"
    menu:
        with dis
        "Listen to his last audio log\n[mt](recommended)":
            $ listenlast = True
            stop sound6 fadeout 1
            show caa 110
            hide screen audiologs
            hide screen audiolog1
            hide screen audiolog42
            hide screen audiolog43
            hide screen audiolog48
            hide screen audiolog55
            hide screen audiolog67
            with dis12
            play sound isaaclast
            call screen audiologlast with dissolve
        "Forget about it":
            hide screen audiologs
label audiologlastpos:
    if listenlast:
        pause 1
        show caa 109 with dis12
        a "W-W-What was t-that...?" with dis08
        mc "Oh shit..."
    show caa 107
    mc "D-Don't look at him, Annie." with dis
    mc "As soon as the teleporter is ready, we'll leave this place forever."
    mc "You have nothing to–"
    $ renpy.music.set_volume(0.3, channel='music3')
    play music3 beat fadein 6
    stop music fadeout 5
    play soundlow alien1 fadein 1
    play sound alien0b
    play sound2 alien0 fadein 1.5
    pause 3.2
    show caa 111 with dis2
    pause
    play sound3 alien2
    show caa 112 with dis15
    pause
    play sound4 alien1
    show caa 112b with dis17
    pause
    play sound5 sniffmonster
    show caa 113
    xen "*Sniffs out Annie*" with dis12
    play sound4 alien1
    show caa 112b with dis17
    pause
    play sound alien0b
    show caa 114 with dis2
    pause
    show caa 107
    mc "*Whispering* O-Okay Annie..."with dis15
    mc "A-As soon as this thing is ready, we’ll jump into it..."
    mc "D-Don't make any noise..."
    play sound7 charge
    blank "DISRUPTORS CHARGED TO 80\%."with hpunch
    mc "Y-You have to be kidding me..."
    play music xenosong2
    stop music3 fadeout 4
    play soundlow alien1 fadein 1
    play sound alien0b
    play sound2 alien0 fadein 1.5
    pause 2.7
    show caa 115 with Dissolve(2.4)
    mc "Oh no..." with dissolve
    mc "W-We're not food, bud..."
    play sound3 alien3
    show caa 116
    xen "*Squeals*"with hpunchlong
    play sound alien1
    play sound2 alien2
    play sound3 stairsmetal
    play soundlow alien3
    play sound5 alien2b
    show caa 117
    mc "S-STAY BACK, YOU FILTHY MUTTS!" with dis
    a "OH GOD, T-THERE ARE DOZENS OF THEM!"
    play sound5 alien1
    if pay500:
        mc "I have a bomb!"
    else:
        mc "I have one explosive left!"
    mc "If you're really so clever, you know that if you attack us, you're gonna blow us ALL up!"
    mc "STAY BACK!"with hpunch
    play sound6 alien2
    play sound7 alien1
    show caa 118 with dis15
    mct "Goddammit, I can't activate my magic... I'm way too exhausted..." with dis08
    mct "And I doubt I could do anything against so many of them..."
    a "*Sobbing* [mc]?"
    play sound6 alien1
    mc "D-Don't worry, Annie..."
    play sound5 alien2
    mct "We're fucked..."
    play sound alien1
    play sound2 alien2
    xen ". . ."
    play sound alien3
    show caa119 with hpunchlong2
    play sound explosionbank
    stop music
    hide screen audiolog1
    hide screen audiolog42
    hide screen audiolog43
    hide screen audiolog48
    hide screen audiolog55
    hide screen audiolog67
    hide screen audiologs
    scene black with flashfaster
    if chopchop != 3:
        menu:
            mod "Here's an option to cheat and get a pendant from Chop-Chop. You die otherwise."
            "Save me, modder!":
                $ chopchop = 3
            "I'll die with honor":
                pass
    if chopchop == 3:
        pause
        play music2 synth3 fadein 4
        pause
        show caa 120 with Dissolve(2.5)
        ast "If you need any assistance, you can ask me or any of my colleagues."with dis08
        play soundlow portalandromeda fadein 1
        ast "Thank you again for choosing Astrocorp. I'm pleased to welcome you to the ultimate experience of love."
        show caa 120b
        ast "Ah, I know that sound!" with dis08
        ast "Someone just used the teleporter to return!"
        ast "Come with me, you can ask them about their experience yourselves! Our best advertising is the satisfaction of our customers."
        show caa 121
        ast "Welcome back, lovers!" with dis12
        ast "How was the..."
        ast "Um... what are you covered with...?"
        show caa 122
        a "What..."with dis08
        mc "How..."
        a "Why... are we alive?"
        mc "The bomb did explode."
        a "It killed the aliens... but not us?"
        show caa 123
        mc "What's this glow?"with dis08
        mc "It’s coming from your pocket."
        show caa 124
        a "*Standing up* No way..." with dis15
        mc "What's that?"
        a "I-It's the Pendant of Destiny!"
        mc "The what?"
        a "The Pendant of Destiny! You bought this earring on Ion, at Chop-Chop's!"
        a "You gave it to me the first time we played Eternum together, remember?"
        mc "Holy shit, I remember!"
        mc "Chop-Chop told me that it’d bring good luck to the girl who wore it... I can't believe it was true!"
        play soundlow vanish
        show caa 125 with dis12
        a "It vanished..." with dissolve
        mc "I guess it was single-use only."
        a "It saved our lives..."
        mct "Wow, I’ve gotta thank Chop-Chop next time... seems like he's not just some charlatan. Not always, at least."
        show caa 126
        ast "Uh... Can you explain to me what's going on, guys?" with dis08
        show caa 127
        mc "You know, I'd love to, but I'm all worn out and I just want to log off."
        mc "So... maybe another day."
        show caa 126
        ast "But..."
        show caa 128
        a "Long story short, the facilities are awesome, great muffins, and amazing experience! At the last minute, though, some aliens invaded the station and killed everyone."with dis
        a "There's probably a loooot of cleaning to be done, and I'd expect your ratings from Google Reviews to drastically drop in the next few hours, so... you probably want to look into that. Sorry!"
        show caa 129
        mc "Bye!" with dis
        ast "What?"
        player "I'm sorry, did she say that some aliens killed everyone?"
        ast "Um..."
        stop music2 fadeout 4
        show login3 with Dissolve(2.3)
        pause 7
        play music2 rain3 fadein 5
        scene caa 130 with flash
        play sound2 beep
        pause
        play sound3 plugin
        play sound4 clothes
        mc "*Removing your visor* Jesus!" with dis
        mct "That sure escalated quickly!"
        mct "It's true what they say, you never know what you might run into in a new Eternum session. Damn..."
        jump rainposalien
    else:
        jump xenodeath


label xenodeath:
    stop music
    hide screen audiologs
    hide screen heart
    pause
    blank ".{w=0.7}  .{w=0.7}  .{w=0.7}  .{w=0.7}  .{w=0.7}{nw}"
    play soundlow beep
    show deadscreen with dissolve
    pause
    play sound beep3
    show screen deathtext with dissolve
    pause
    play sound2 beep3
    hide screen deathtext
    show screen deathtext2
    with dissolve
    pause
    play sound3 beep3
    hide screen deathtext2
    show screen deathtext3
    with dissolve
    pause
    play music2 rain3 fadein 1
    play sound2 beep
    hide screen deathtext3
    show screen heart
    scene caa 130
    with flash
    pause
    $ mclevel = 1
    play sound3 plugin
    play sound4 clothes
    if xenodeathgun:
        mc "*Removing your visor* Wait a second..." with dis
        mc "WHAT??!" with hpunch
        mct "What the fuck just happened?!"
        mct "I was walking around that damn station... and suddenly I'm fucking dead?!"
        mct "I didn't even hear anything!"
        mc "*Sighs* (Fuck this shit.)"
        mct "Well, at least I didn't suffer..."
    elif xenodeath1:
        mc "*Removing your visor* Goddammit!" with dis
        mct "What the hell was that creature?!"
        mct "I didn't even see it coming..."
        mct "That thing jumped on me, and then... I don't remember anything else. Just a terrible pain, and then... darkness."
    else:
        $ xenodeath2 = True
        mc "*Removing your visor* Goddammit!" with dis
        mct "Jesus, that explosion blew out everything..."
        mct "I don't even remember anything after the creatures jumped on us..."
        mct "Just... darkness."
label rainposalien:
    play soundlow thunder
    show caa 131
    mct "It's very late. This has gone on far too long... I should go to sleep now, I’ve gotta be fresh for tomorrow night." with dis12
    play sound chair2
    show caa 137
    mc "*Sighs* (This is not how I wanted my date with Annie to end up...)" with dis12
    mct "Everything was going so well... until everything went to shit, as always."
    mct "Another bad memory for Annie. God, she'll probably be traumatized for years. I wonder if this is it for us..."
    if xenodeath1 or xenodeathgun:
        mct "Anyway, tomorrow will be another day. Annie must still be connected to Eternum, and I can't really wake her up."
        mct "I'll wait in the dining room..."
        jump fancydinner
    else:
        mct "She probably..."
        play sound run
        pause 1.5
        play sound doorslam
        show caa 132 with hpunch
        pause .3
        mc "Oh... h-hey!" with dis08
        show caa 133
        a "Best. {w}Date.{w} Ever!"
        play music2b romantic2 fadein 4
        stop music2 fadeout 6
        show caa 132
        mc "Um..."
        mc "*Chuckles* Was it?"
        show caa 134
        a "It was better than I could have ever imagined!"with dis
        a "We went to the movies together, we floated up into the air, we saw the stars together..."
        a "It was like a romantic film!"
        $ annie_points += 1
        play sound beat
        show caa 135
        show screen heartbeat
        a "After that, everything turned into a horror movie, and just when everything seemed lost... you came to rescue me!"with dis
        if chopchop == 3:
            a "Then you tried to sacrifice yourself in order to destroy the monsters! That was so romantic!"
            a "And to round off everything, we were saved thanks to a magic pendant you bought me the first time we played Eternum!"
        else:
            a "And then you sacrificed yourself in order to destroy the monsters! That was so romantic!"
            show caa 132
            mc "B-But... we died."with dis
            show caa 133
            a "It doesn't matter! Now we can start climbing Eternum's ranks together!"
            a "It's even better!"
            show caa 132
            mc "*Chuckles* Well, that's not the reaction I was expecting from you. I just hope it doesn't catch up with us one day."
        if anniefingers:
            show caa 136
            a "And... w-well, the things we did in that room..." with dis
            a "It was... w-well, you know..."
            a "A-Amazing..."
        show caa 133
        a "Thank you for an amazing day, [mc]." with dis
        show caa 132
        mc "I'm glad you enjoyed it, Annie. Even with the alien attack, and... well, the bloodbath... it was still one of the best days I've ever had."
        show caa 133
        a "It really was! We’ve gotta repeat it sometime!"
        show caa 136
        a "I mean... not necessarily like... {i}every{/i} part... y'know..."with dis08
        a "Just hanging out and..."
        a "W-Well, you helping me discover new things, new experiences..."
        show caa 138
        a "I m-mean, I'm not just talking about... that! Although... we could repeat THAT too! But not like... I mean, we don’t have to... Not that I don't want to..."with dis08
        show caa 136
        a "*Clears throat* ANYWAY! God, it's super late and I haven't had any dinner yet!"with dis08
        a "See you tomorrow!"
        mc "*Chuckles* Goodnight!"
        play sound doorclose
        show caa 137 with dis12
        blank "{i}You hear Annie giggling as she goes down the stairs."with dis
        mct "Well, that's not the reaction I was expecting, but... phew, I'm glad!"
        mct "I'm sure looking forward to helping her to discover more... \"new experiences\"."
        mct "Tonight was... something else, that's for sure."
        play sound2 stomach
        pause 2
        mct "God, I'm so hungry..."with dis08
        jump fancydinner



label fancydinner:
    stop music fadeout 3
    stop music2 fadeout 3
    stop music2b fadeout 4
    show black with Dissolve(2.5)
    pause
    show screen nextday with dis
    pause
    play music2 happy10 fadein 8
    hide screen nextday
    scene cf 1
    with Dissolve(2.2)
    pause
    play sound doorclose
    play soundlow toilet
    show cf 2
    mct "The moment is finally here." with dis
    mct "The most exclusive meeting in the world is being held tonight."
    if xenodeath1 or xenodeath2 or xenodeathgun:
        mct "Ulysses' senior officials, the holders of the other Gems of Doom, and... {i}since we were able to retrieve the Gem from my dead body at the station{/i}... me!"
    else:
        mct "Ulysses' senior officials, the holders of the other Gems of Doom, and... me!"
    mct "All together in one place!"
    show cf 3
    mct "E-Suit correctly adjusted..."with dis08
    show cf 2
    mct "Check!"with dissolve
    show cf 4
    mct "E-Visor properly calibrated..."with dis08
    show cf 2
    mct "Check!" with dissolve
    show cf 5
    mct "Lovely confirmation text from my partner in crime..." with dis08
    call chat(alex_chat2) from _call_chat_8
    show cf 2
    mct "Check!" with dissolve
    mct "WE'RE READY!"with hpunch
    show cf 6
    p "Good luck, [mc]!"with dis
    show cf 7
    mc "Hey! Thanks, Penny!"
    if penelopepath:
        mct "Damn, Penelope in her underwear is always a sight to behold..."
        show cf 6
        if grimoirerest:
            p "I wish we could all go with you. I'm starting to be useful – yesterday I managed to master a level 6 healing spell!"
        else:
            p "I wish we could all go with you. I'm starting to be useful – yesterday I managed to master a level 5 fire spell!"
        show cf 7
        mc "Damn, really? Not bad!"
        mc "And starting to be useful? Please! Between your acting during the heist and your performance at Warthogs, you’ve more than held your own."
        show cf 6
        p "Thanks! You’re a sweetheart. I've been practicing with Luna these past few days. I can't stop playing!"
        p "I only took a break today because I went to the mall to buy a costume for the party next week."
        show cf 7
        mc "Sounds good! What are you dressing up as?"
        show cf 8
        p "*Giggles* That's a secret!"with dis08
        mc "Aww... come on! Give me a hint!"
        p "Nope!"
        mc "I'm sure Nova already knows what it is..."
        p "Of course she does! She came with me to the mall!"
        p "But I want you to see it for the first time at the party."
        show cf 6
        p "Well... if you still want to come, of course." with dis08
        show cf 7
        mc "Absolutely! I'm looking forward to it. Now that you mention it, I should start thinking about my costume too..."
    else:
        mct "Damn, Penelope doesn't even mind going in her underwear around me."
        mct "There's no way out of this friend zone..."
    play soundlow doorclose
    if tellpassword:
        show cf 8b
        d "Look who it is!" with dis08
        d "The blabbermouth! Be careful what you tell him, Penny, he might just gossip it away to everyone he sees!"
        mc "Come on Dalia, I already said I was sorry..."
        mc "Wish me luck!"
        d "If you come back without losing our Gem of Doom, I'll be surprised. Don't screw up."
        mc "*Gulps* I'll try."
    else:
        show cf 9
        d "Heeeey! Good luck with the fat cats, [mc]!" with dis08
        mc "Thanks Dalia!"
        d "If you can come back without losing our Gem of Doom, I'll consider it a success!"
        if daliapath:
            mc "You wanna bet?"
            d "*Giggles* Fuck off! I'm not betting against you ever again, you know it..."
            mc "Aw, that's too bad..."
            mc "Maybe you’ll change your mind in the future?"
            d "Unlikely..."
        else:
            mc "*Chuckles* I'll try."
    if daliapath:
        show cf 10
        d ". . ."with dis08
        p "Hmm?"
        show cf 11
        d "Did you run out of clean tops, or what?" with dis
        show cf 12
        p "I was about to take a shower and put on my pajamas."
        show cf 11
        d "Your pajamas? You're not going out tonight? It's a Saturday."
        show cf 12
        p "Nah, we have a party next week, I don't wanna feel overwhelmed. And plus, I wanted to play Eternum anyway."
        if penelopepath:
            show cf 11
            d "“We” have a party? Who’s “we”? You and [mc]?"
            show cf 12
            if novapath:
                p "Yeah, Nova, [mc], and I are going to a party on campus. I could have sworn I told you about it..."
                show cf 11
                d "Rightttt, well, I definitely remember you mentioning Nova going..."
            else:
                p "Yeah, [mc] and I are going to a party on campus. I could have sworn I told you about it..."
                show cf 11
                d "Rightttt, I might remember you mentioning going..."
                d "Didn't know about [mc]."
        show cf 11
        d "Anyway... you should hop in the shower before you catch a cold."
        show cf 12
        p "Is there any problem with me being in my bra and panties? You seem very concerned all of a sudden."
        show cf 11
        d "Nah, it's just that... well, it might be awkward for other people."
        show cf 12
        p "What other people? You? Mom? Annie? I'm sure [mc] doesn't mind either. He's like... family. Like a little brother, almost."
        mct "Ouch."
        show cf 11
        d "Yeah... like a little brother..."
        d "If I didn't know any better, I'd think that you were trying something."
        show cf 12
        p "With [mc]? Pffft, please, my bar is WAY higher. You’ve seen my Instagram DMs: models, actors, influencers... did you know that that Gigachad meme guy from a few years ago tried sliding into my DMs?"
        p "In fact, if I didn't know any better, I'd think that YOU were trying something."
        show cf 11
        d "Pffft, with that pervert with the monkfish face? Dream on."
        mc "Um... I'm still here, you know?"
    play sound doorsliding
    show cf 13
    n "Best of luck, honey!"with dis
    show cf 14
    mc "Thanks, Nancy!"
    mc "I wish I could invite more than one person."
    show cf 13
    n "I'm sure that the next time they host a fancy dinner party, we'll have more than 1 Gem of Doom, so that won't be a problem."
    show cf 14
    mc "Ah, you're not wrong there!"
    play soundlow doorclose
    show cf 15b
    a "Huh??" with dis
    a "Are we celebrating something? What are you all doing here?"
    mc "Nothing, really. I was about to log in now."
    show cf 15
    a "Oh, already?! Good luck, [mc]! Be sure to get plenty of information!" with dis
    if not anniepath:
        mct "Annie has been distant, but I'm happy to see her smile. I guess that's all I need for now. That's what best friends do, I guess."
    elif xenodeath1 or xenodeathgun:
        mct "I'm happy to see Annie smiling. I was afraid of her being traumatized after whatever happened in that station, but I'm glad she managed to escape in time."
    show cf 16
    if tellpassword:
        d "Yeah, do something useful for once, dumbass! Get us the address of Thanatos in real life, for example!"with dis08
    else:
        d "Yeah, you better return with the name and address of Thanatos in real life!"with dis08
    a "Or some information about Ulysses' mysterious disappearances!"
    p "Or a couple of big sacks full of eternals!"
    n "Or 5 new Gems of Doom in your pocket! I wanna see my face painted on the walls of Ulysses' headquarters after we become the new CEOs!"
    mc "*Laughs* I think your expectations are a little bit too high, but sure, we'll see what Alex and I can do."
    mc "Don't get too bored while I'm gone."
    show cf 17
    n "Oh, don't worry about that, we have work to do!" with dis08
    n "Turns out Aunt Cordelia is celebrating her 65th birthday next week. Your uncle asked us to do a collage of photos of her."
    n "We’ve gotta go through all of the family photo albums, and find the 100 best pictures of her, from birth ‘til now!"
    d ". . ."
    p ". . ."
    show cf 18
    d "Awwww, fuck! You know what I just remembered, sis? The... uhh, uhhh... a-bra-panty-ism Seminar! "with dis08
    p "AHHH, shit, the ABRAPANTISM SEMINAR! Was today the last day to register?"
    d "Yeaahhh... we have until midnight..."
    p "Oh, dammit... How could we forget?! I'm sorry Mom, we've gotta login to Eternum to check into the Abrapantism server..."
    p "We need it for... um... special Gem of Doom handling protocols... Your character must not need it for some reason..."
    d "DARN IT! AGH! I’m so mad! I SO wish we could participate in the creation of that collage..."
    p "Yeah, with how much we love Aunt Cordelia..."
    d "Well, I guess we’ve gotta go if we want to get there in time..."
    p "Yeah, I guess so..."
    play sound run
    show cf 19
    d "*Running away* Sorry Mom!" with dis12
    p "We'll make it up to you next week, we promise!"
    p "*Whispering to Dalia* Seriously, you couldn’t think of anything better than bra-and-panties??"
    n "Hmmm...."
    show cf 20
    a "I can help you out if you want, ma'am."with dis12
    a "I don't know Aunt Cordelia, but I'm good at making collages."
    play sound2 clothes1
    show cf 21
    n "AAAAAAH! How can you be so adorable?!" with hpunch
    n "If you were just a little bit smaller, I'd eat you whole!"
    n "Thank you Annie!"
    a "N-No problem!"
    n "Let's go to the living room!"
    play sound3 run
    show cf 22
    n "*Going downstairs* Have fun [mc]!" with dis
    mc "*Chuckles* Thanks!"
    stop music2 fadeout 7
    play music2b rain2 fadein 5
    play sound7 doorclose
    show bm 7 with dis15
    mc "*Jumping on the bed* Alright, time to log in. Here we go!"with dissolve
    play sound ai7
    blank "{i}Connected." with dis
    play sound ai8
    blank "{i}Welcome back to Eternum." with dis
    mc "To the Rockefeller server, please!"
    mc "Idriel invited me herself this time, you know? I feel a little special, hehe..."
    play sound ai11
    blank "{i}Please prepare to connect..." with dis
    mc "I couldn't be more prepared!"
    stop music2b fadeout 1
    play sound risingshort4
    pause 2
    show login3 with flash
    pause 8
    play soundlow whoosh4
    scene white with dissolve
    play music night fadein 3
    play sound3 fall3
    show cf 23 with Dissolve(2.5)
    pause
    mct "Another great landing!" with dissolve
    mct "Alright..."
    mct "If I'm not wrong, we were supposed to drop directly at the site, so..."
    show cf 24 with dis12
    play soundlow whistle3
    mc "*Whistles* (Damn, look at this mansion.)"with dissolve
    mct "An estate like this must cost tens of millions of eternals. This is definitely the place."
    show cf 25
    mct "Hey, this tuxedo fits me like a glove!"with dis12
    mct "And it looks more expensive than it actually is, so I should be able to get by relatively unnoticed. Nice!"
    mct "I’ve gotta thank Penelope and her model connections for this sweet deal!"
    mct "I wonder what Alex will be wearing..."
    show cf 26
    mct "Speaking of which, I should find her as soon as possible. We were supposed to meet at the backyard of the mansion, but this whole place is a maze."with dis
    mct "Maybe she's already inside?"
    mct "Hmm, there's a woman right in front of the gates. I'll go ask her..."
    $ renpy.music.set_volume(0.08, channel='music3')
    play music3 classic1 fadein 5
    show cf 27 with dis2
    mc "Good evening!" with dis08
    show cf 28
    player3 "Welcome to the Boyle mansion, sir. How may I help you?"
    show cf 27
    mc "Uh... My name is [mc] [lastname]."
    mc "I..."
    show cf 28
    player3 "Of course, sir. I see your name on our guest list. You may enter at your convenience."
    show cf 27
    mc "Ah, excellent."
    show cf 28
    player3 "In accordance with the night's theme, please consider wearing your mask before entering the mansion."
    player3 "A mask for yourself and for your partner should appear in your inventory."
    show cf 27
    mc "Understood."
    show cf 28
    player3 "If you would like, you may reveal your name to other attendees. However, it is prohibited to remove your mask during tonight’s event."
    player3 "Everyone inside the mansion must wear them... except for the staff, of course."
    show cf 27
    mc "The bossman doesn't let you play?"
    show cf 28
    player3 "The invited guests are the only human players at the mansion. It would not make sense for us to engage in the event."
    show cf 27
    mc "The... wait, you... you're not human?"
    show cf 28
    npc "I'm not."
    npc "Every single butler, waiter, and staff member in the mansion tonight is a non-playable character."
    npc "...Including me."
    show cf 27
    mct "Holy fuck... She looks so real and speaks so eloquently... I'd have never guessed."
    mc "Um... alright, thank you."
    show cf 28
    npc "Enjoy your stay, sir."
    play sound metalgate
    show cf 29 with dis22
    mct "Okay..." with dis08
    mct "First things first, I have to find Alex. She told me she was planning to get here earlier than me."
    mct "She's a smart girl, she must have hidden near the back of the house to avoid running into her father, since she didn’t have a mask on her."
    mct "Now that I think about it, though... William Bardot has seen my face too. I should probably get away from the entrance..."
    show cf 31
    mc "*Turning around* (I wouldn't want to...)"with dis12
    play sound5 deception
    scene prafb0 with flashfastest
    pause .15
    play sound deception
    scene prafb1 with flashfastest
    pause .15
    play sound2 deception
    scene prafb2 with flashfastest
    pause .15
    play sound3 deception
    scene prafb3 with flashfastest
    pause .15
    play sound4 deception
    scene cf 31 with flashfastest
    pause
    play soundlow swallow
    mc "*Gulps*" with dis
    show cf 32
    pra "Good evening, sir."
    show cf 31
    mc "W-What?"
    show cf 32
    pra "Welcome to the Boyle mansion."
    show cf 31
    mct "Oh..."
    mct "God, I forgot they all have the same face... She's not the one the girls and I met in Ogygia. I’ve gotta calm down."
    mc "G-Good to see Praetorians here. I feel safer already."
    show cf 32
    pra "Of course, sir. We’re taking all necessary precautions to ensure the security and safety of the players attending tonight."
    show cf 31
    mc "G-Good. Good."
    mc "Are there many of you here?"
    show cf 32
    pra "Enough units to prevent any unwelcome individuals, or to quell any possible conflicts."
    show cf 31
    mc "*Nervous laughter* Well, I guess I'll cancel all my planned shenanigans for tonight, then."
    pra ". . ."
    mc "*Clears throat* K-Kidding aside though, I think I'm gonna go for a little walk through the gardens."
    mc "That’s allowed, right?"
    show cf 32
    pra "Of course. Just remember to wear your mask when entering the mansion."
    show cf 31
    mc "S-Sure. Thank you!"
    mc "I'll see you around."
    show cf 33 with dis22
    mct "Holy shit, those damn eyes... They pierce your soul." with dis08
    mct "Talking with a Praetorian face to face is so uncomfortable. It feels like she can cut your throat at any second."
    mct "Okay, calm down, [mc]. You’ve gotta keep it cool. You can't appear inside, drenched in sweat."
    mct "On the other hand, I definitely have a future as a scared Annie impersonator..."
    mct "But anyway... where the hell is Alex?!"
    mct "She said–"
    play sound jumpscare2
    show cf34
    x "BOO!"with hpunch
    $ unlock_look("alex", 6)
    mc "GGGGHHHHH YOU SON OF A BITCH!!!!"
    play sound2 fall3
    play sound3 fall
    scene cf 34b
    mc "*Panting* F-FUCK!" with dis
    mc "What the hell is wrong with you?!!"
    blank "{i}She snorts, trying to hold her laugh."
    show cf 35
    if alexpath:
        mc "*Standing up* Yeah, very funny, Alex! And very mature!"with dis12
        show cf 36
        x "*Chuckles* Come on [mc], it's your fault for being so jumpy!"with dis
        show cf 35
        mc "I'm not jumpy! It's just that... loud noises... make me... jump."with dis
        mc "B-But in any case, I don't wanna die of a heart attack before I’m 20! Why does everybody keep trying to scare me?!"
        show cf 36
        x "*Chuckles* Because it's funny seeing you jump like a wallaby!"with dis
        show cf 35
        mc "*Laughs* Fuck off."with dis
        mc "I'll remember this one! Don't cry later, when I have my revenge..."
        show cf 36
        x "You’re gonna scare me? Hah! Good luck. It's impossible."with dis
        show cf 35
        mc "Oh, we'll see about that... We'll see..."with dis
        show cf 37
        x "Anyway... pretty fancy place, huh?" with dis12
        x "Reminds me of our house in Wales. We used to go there during the holidays when I was 7 or 8 years old."
        x "I used to spend entire days on the lake with my grandma."
        show cf 38
        mc "Oh really? And you don't go there anymore?"with dis
        show cf 37
        x "Nah, after she... died of cancer, I stopped going anywhere with my family. They've always had better things to do."with dis
        show cf 38
        mc "Oh... I'm sorry, Alex."with dis
        show cf 37
        x "No worries, it's been a long time. But thank you."with dis
        show cf 39 with dis15
        mc "Damn..."with dis08
        mc "You know, now that I can look at you properly..."
        menu:
            with dis
            "You look incredibly beautiful tonight":
                mc "You look incredibly beautiful tonight, Alex. That dress is..." with dis08
                show cf 44
                x "Yeah, yeah, that dress looks AMAZING on you and blah blah blah." with dis12
                x "Can we focus on the mission, please?"
                show cf 42
                mc "Oh... of c-course! Sorry, I forgot that you don't like compliments."
                show cf 44
                x "I don't like to be buttered up. It's different."
                show cf 43
                x "But anyway, getting back to business... do you have the masks?"with dissolve
            "You look like a high-society gal! [alex_pts]":
                mc "You look like a high-society gal!" with dis08
                show cf 40
                x "Oh, you really think so?" with dis12
                mc "Yep, definitely!"
                show cf40
                x "*Batting her eyelashes* Isn't it amazing what some make-up and fancy clothes can do?"
                x "Suddenly, the rebellious child is the perfect young lady!"
                scene cf40
                x "*Batting her eyelashes* The ugly duckling has turned into a beautiful swan! The black sheep has changed her colors! Finally, Papa will accept me back into the family!"
                show cf 42
                mc "*Laughs* Well, even if it's absurd to deny that you really look stunning with that dress... I've gotta say that I prefer the real you." with dis
                mc "An Alex with no tattoos is no Alex. They're like... part of you."
                show cf 43
                x "You're goddamn right."
                show cf 42
                mc "You did a great job hiding them, though. I can't see any trace."
                show cf 43
                x "It's not the first time I've had to use makeup to hide them. I attended a couple of dinners like this in the real world with my father shortly after I got the first ones."
                x "But after a few... incidents... he stopped forcing me to go. Less embarrassment for him, I guess."
                show cf 42
                mc "Are you wearing makeup on your arms too? Under the gloves?"
                show cf 43
                x "Yeah, I am. You never know what could happen. So I put makeup on everywhere."
                show cf 42
                mc "Everywhere? You sure you didn’t have any trouble with an area? If you want, I can check if the tattoos on your back and thighs are covered up well, under the dress."
                mc "I wouldn't mind, really. It’s for the good of the mission. You never know what could happen..."
                $ alex_points += 1
                play sound beat
                show screen heartbeat
                show cf 43
                x "*Chuckles* I bet you wouldn't dare..."with dissolve
                x "I'm sure everything is perfectly hidden, but thanks for the offer."
                x "I'll definitely keep it in mind..."
                show cf 42
                mct "Hmm... is she... flirting with me? Or is she just messing with me? It's hard to tell with her..."with dissolve
                mct "Probably the second, let's be realistic."
                show cf 43
                x "Anyway, getting back to business... do you have the masks?"
        show cf 42
        mc "I do!"
    else:
        mc "*Standing up* Yeah, very funny, Alexandra! And very mature!" with dis12
        show cf 43
        x "Oh, come on, [mc], it's your fault for being so jumpy."with dis
        show cf 42
        mc "Yeah, sure..."
        show cf 43
        x "Alright, stop being a pussy! We have a mission to do here... don't we?"
        show cf 42
        mc "Yeah, we should go inside before someone notices us hiding back here."
        show cf 43
        x "Do you have the masks?"
    show cf 43b
    mc "They're right here." with dis12
    x "Huh, interesting. Everyone has the same ones?"
    mc "I saw a couple of people in the distance and they were pretty similar. But different colors."
    show cf 43c
    x "So... we have a cat and... a demon?"with dis
    mc "Yeah, it seems so. Which one do you want?"
    x "Uhh... well, I guess I'll go with the cat."
    x "I'll leave the oni one to you. It's... more your color."
    show cf 42
    mc "*Chuckles* I'll take that as a compliment."with dis12
    mc "Alright then, we're all set. Any advice?"
    show cf 43
    x "These people love talking about themselves. Try to keep the conversation on them."
    x "Then you can try to casually sneak in a question about what we want to know. But don't make it look like an interrogation."
    show cf 42
    mc "Gotcha."
    show cf 43
    x "What topics should we prioritize tonight, anyway?"
    show cf 42
    mc "Well, anything we can learn about the Gems of Doom, the Weapons of Atlas, or Thanatos would be useful."
    mc "Maybe someone knows something about the deaths that Ulysses has hidden, but that might be difficult to bring up."
    show cf 43
    x "I see. Sounds good to me."
    show cf 45
    mc "Alright then, put on your mask and let's get back to the party!"with dis
    mc "The main entrance is this way, past the corner."
    show cf 46
    ca "And where shall we meet to share reconnaissance after the dinner?"
    ca "I prefer gathering intelligence myself, but if either of you gains information on Hyril'ar, I would like to hear it."
    show cf 45
    mc "Great point! I think a good meeting spot would be at..."
    mc ". . ."
    stop music3
    play sound fall3
    show cf 47
    mc "*Abruptly turning around* W-WH...!" with hpunch
    play music2 quirky4 fadein 6
    mc "WHAT THE HELL ARE YOU DOING HERE?!" with hpunch
    show cf 48
    ca "What do you mean?" with dis
    ca "Am I supposed to stay locked up? I am not a bird, [mc]."
    show cf 49
    mc "You can be wherever you want... EXCEPT HERE!"
    mc "Don't you remember what we talked about?! The people who are looking for you are gonna be here!"
    mc "The guards who attacked us in Ogygia are here!"
    mc "Shit, the people who crea... the people who put you in that box are probably IN this mansion!"
    show cf 48
    ca "All the more reason to be here, then."
    ca "I would very much enjoy having a {i}conversation{/i} with them."
    show cf 49
    mc "Oh god, this is such a bad idea..."
    show cf 48
    ca "Do not worry about me so much. I know how to take care of myself."
    ca "My power used to be feared across all the Elven Kingdoms."
    show cf 49
    mc "That doesn't exactly give me peace of mind..."
    mc "And how did you get in here, even?"
    mc "A-And what's up with that dress? I'm pretty sure it's not elven."
    show cf 50
    ca "Oh, well, I simply opened a portal to your location. I can instantly appear wherever you are." with dis12
    ca "And this attire... I copied parts of the outfits of other women I saw entering this palace."
    ca "I usually do not like your peasant garb, but this time I was not entirely displeased by them."
    ca "I believe these people are the elite of your society, correct?"
    mc "Um... yeah, I guess you could say that."
    mc "Well, I can't say this dress was a bad choice..."
    mc "You look..."
    x "You look hot as fuck, Calypso!"
    show cf 52
    ca "That is... quite inappropriate, but I will allow it. Thank you, Alexandra."with dis
    ca "You look... “hot as fuck” as well. I still suspect that the blood of my race courses through your veins."
    show cf 51
    x "And I still doubt it, but hey... maybe a distant relative, who knows."
    show cf 52
    ca "Perhaps... Our blood is powerful. It could persist through many generations."
    show cf 51
    x "Alright, so... tell me, why did you come? What's your plan?"
    show cf 52
    ca "I will keep a low profile, do not worry about me."
    ca "While you try to seek information about those Gems of Power, I will likewise ask questions about my realm."
    show cf 51
    x "I see... fair enough."
    x "Good luck with that."
    show cf 52
    ca "If you need my assistance, [mc] can summon me. I grant him permission to do that once tonight."
    show cf 51
    x "Well, he still doesn’t have full control of his powers, so we can't guarantee that, even if he tried."
    mc "Hey, I'm getting better!"
    x "What about your face, though? It’s very distinct."
    x "I guess you could say you're just roleplaying as an elf, and you wouldn't be the first, but someone might still recognize you. Someone you don't want to."
    show cf 53
    ca "That's not a problem. I saw those masks too." with dis
    ca "I'll just create one for myself."
    play sound polyjuice
    show cf 55 with dis2
    ca "Like this." with dissolve
    show cf 54
    x "Wow... That's quite cool!"
    x "And finally, what about the hair? Its turquoise color is quite... unique."
    play sound2 polyjuice
    show cf 55b with dis2
    ca "This will do." with dissolve
    mc "Damn! Can you really change your hair and clothes just by thinking about it?"
    ca "Yes... something like that."
    mc "Wow, you're like... living Penelope's dream."
    ca "Very well then, I will be on my way. If we do not see each other inside, we shall meet again here after the event."
    mc "Alright, good luck, Calypso. And be careful!"
    ca "I always am."
    show cf 42 with dis17
    mc "Well... what could go wrong?" with dis08
    show cf 43
    x "I'm honestly more worried about the other guests than Calypso herself. Every day she seems... more powerful."
    show cf 42
    mc "Yeah, she's definitely recovering confidence and power."
    mc "I guess we should go inside before she starts disintegrating people."
    show cf 43
    x "Yeah, I guess so. Are you ready?"
    show cf 42
    mc "Ready as I’ll ever be. Let’s go."
    stop music2 fadeout 6
    show cf 56 with dis15
    x "*Using a posh accent* Remember to talk as if you're better than the rest of the world."with dissolve
    mc "Impersonating Axel, then? Got it."
    x "*Chuckles* I see you catch on fast."
    $ renpy.music.set_volume(0.2, channel='music3')
    $ renpy.music.set_volume(0.6, channel='music2b')
    stop music fadeout 9
    play music2b classic1 fadein 6
    show black
    show screen afewminuteslater
    with dis2
    pause
    show chateau
    hide screen afewminuteslater
    with dis22
    pause 8.2
    scene cf 57
    mc "Damn..." with dissolve
    show cf 58 with dis15
    pause
    play soundlow whistle3
    mc "Holy fuck, this place is so... staggering."with dis08
    x "And ostentatious. It's always a question of excess – how much bigger and better am I than you? You’ve gotta flaunt it."
    mc "I feel so out of place, like they can see and smell the “poor” on me. Do I look rich to you?"
    x "You look... passable."
    x "Don't worry too much. None of them are particularly clever; I know that from experience."
    show cf 59
    npc "Good evening, sir, and welcome to the Boyle mansion." with dis
    show cf 60
    mc "Thank you."
    show cf 59
    npc "The Founder and the Lady of Eternum will make an appearance at 11:00 PM, but all other guests have already arrived."
    show cf 60
    mc "Ah, the big man."
    show cf 59
    npc "He apologizes for his delay, as an unforeseen event has detained him."
    show cf 60
    mc "Well, that's sensible. I imagine that being the CEO of the biggest company on Earth has to keep you busy."
    show cf 59
    npc "In the meantime, I suggest you partake in our gourmet cuisine, featuring a wine selection carefully crafted by our in-house sommeliers."
    show cf 60
    mc "That sounds good! Wait, is that sushi?"
    show cf 59
    npc "Yes it is, sir. Would you like to taste it?"
    show cf 60
    mc "Sure!"
    show cf 59
    npc "You can find further savory foods and other culinary delights in the Golden Room."
    show cf 60
    mc "I'll check it out! Thank you."
    show cf 61
    x "We didn’t come here to eat, remember?" with dis15
    if alexpath:
        mc "Oh, come on, Alex! I can't even eat a couple of canapes?"
    else:
        mc "Oh, come on, Alexandra! I can't even eat a couple of canapes?"
    x "Eat this one if you want, but that's it. You need to be focused."
    mc "Of course I'll be focused! It's just sushi, not a joint."
    play sound chew
    show cf62
    mc "*Eating the sushi* Mmph..."with dis12
    mc "*Eating the sushi* It's mnot as if it's mgonna–"
    $ renpy.music.set_volume(0.0, delay=10.0, channel='music2b')
    play sound sushi
    show sushi1
    show sushi1b
    pause 10.6
    stop sound
    play soundlow whoosh3b
    $ renpy.music.set_volume(0.6, channel='music2b')
    scene cf 64
    mc "J-JESUS TAPDANCING CHRIST!"
    mc "T-This is..."
    mc "DIVINE!"with hpunch
    x "The sushi?"
    mc "Is this what rich people eat everyday?! Sweet Mother of God, it's the best thing I've ever tasted!"
    x "You're outrageous, you know?"
    x "You’ve never eaten sushi before?"
    mc "This is not normal sushi! It's like... having an orgasm in your mouth!"
    x "Oh, for fuck's sake, don't overreact. It's just a handful of rice with a slice of tuna on top of it."
    mc "TASTE IT!"with hpunch
    if alexpath:
        x "*Sighs*"
        show cf 65
        x "Fine, I'll eat one. Will you shut up and start focusing if I do?"with dis
        mc "YES!"
        play sound chew
        show cf66
        x "*Eating the sushi* Mmph..."with dis12
        x "*Eating the sushi* Mmhappy? Can w–"
        $ renpy.music.set_volume(0.0, delay=10.0, channel='music2b')
        play sound sushi
        show sushi2
        show sushi2b
        pause 10.6
        stop sound
        play soundlow whoosh3b
        $ renpy.music.set_volume(0.6, channel='music2b')
        scene cf 67
        mc "AND?!"
        x "(Sweet Mother of God, this shit is divine.)"
        x "(It's the best thing I've ever tasted. It’s like the nectar of the gods.)"
        mc "It's amazing, isn't it?"
        show cf 64
        x "*Clears throat* Um... y-yeah, it's not... {size=27}n-not bad." with dis15
        mc "NOT BAD?!" with hpunch
        show cf 69
        x "O-Okay, enough!" with dis15
    else:
        x "Excuse me?? You can't tell me what to do!"
        x "Shut up and start focusing, for fuck's sake."
    x "We didn't come here to drink and eat, [mc]!"
    show cf 70
    if alexpath:
        mc "Yeah, you're right, I'm sorry."
    else:
        mc "Y-Yeah, you're right... I'm sorry." with dis15
    show cf 69
    x "No more distractions!"
    if alexpath:
        x "Dalia, Nova, and all the others are counting on us! So we need to stay focused, no matter how ridiculously good the food is here."
        show cf 70
        mc "So you admit that that sushi was amazing!"
        x ". . ."
        show cf 71
        x "Jesus Christ, it was glorious! How can it be so fucking good?! Do you think we can sneak a platter out of Eternum?" with dis08
        mc "Right??!"
        x "It was like... having an orgasm in your mouth!"
        mc "I know!!!"
        show cf 69
        x "B-But that's enough! Let's focus on the mission!"with dis
    else:
        x "Dalia, Nova, and all the others are counting on us! So we need to stay focused!"
    show cf 70
    mc "You’re right... we should get going."
    show cf 69
    x "We should split up. We'll be able to talk to more people that way."
    show cf 70
    mc "Makes sense."
    show cf 69
    x "I can see 3 members of Ulysses' board of directors from here, on the upper floor."
    x "I'll leave them to you. I doubt they would recognize me, but I prefer not to take that risk."
    x "The bearded man is Dr. Du Pont. He's as disgusting as my father, so be careful with him."
    x "The woman is Lisa Astor. She's haughty and full of herself, so you'll probably get her attention easily by complimenting her."
    x "And the last one is Mr. Mos. He's... nice. Or at least he's pretending to be. He was the only one of them who didn’t goggle at me the last time I saw these pigs. I'll give him the benefit of the doubt."
    show cf 70
    mc "Understood. You take the other stairs. Let's meet again downstairs, next to the statues."
    show cf 69
    x "Okay. Good luck."
    show cf 70
    mc "Good luck!"
    show cf 70b with dis2
    mct "Alright, you got this, [mc]."with dis
    mc "*Forcing a posh accent* It's refreshing to find someone whose countenance complements her attire so excellently, Madame."
    mct "Yeah, I'm nailing it."
    show cf 72 with dis2
    mc "Hmm..." with dis08
    queue music2b classic2
    mod "You should at least talk to Calypso and Mr. Mos."
label prefancymenu:
    show cf 72
    call screen fancyparty with dis15
    pause
label ldupont:
    $ fancytalk1 = False
    show cf 73
    dup "How many times do I have to say it?!" with dis12
    dup "I.{w} WANT. {w}MORE. {w}WINE!"
    dup "Get your ass to the cellar and bring me a full bottle, you moron!"with hpunch
    show cf 74 with dis12
    dup "Aghh... These fucking idiots still need a ton of improvement." with dissolve
    show cf 75
    mc "I agree. Whoever programmed them has no idea what they're doing."
    mc "Can you believe I asked for salmon nigiri, and they brought me uramaki?"
    show cf 74
    dup "Exactly. These programmers are terrible. I bet they hired immigrants. Or worse... women."
    show cf 75
    mc "Yeah, I bet they did."
    mct "Jesus, what a fucking bigot."
    mc "Can I ask you something, Dr. Du Pont?"
    show cf 74
    dup "No."
    dup "I don't even know who you are."
    show cf 75
    mc "Uh... I'm... in charge of Ulysses' network security."
    show cf 74
    dup "Then let me tell you that you're doing a shit job."
    show cf 75
    mct "This guy's a tough nut to crack..."
    show cf 74
    dup "We had a security breach in a restricted server the other day. Was that your fault?"
    show cf 75
    mc "Oh... yeah, I've heard of it. I'm so sorry, we were attacked by a group of... Chinese hackers."
    show cf 74
    dup "Chinese, huh? That makes sense."
    show cf 75
    mc "Everything is resolved now."
    show cf 74
    dup "What do you mean, {i}everything{/i}? They stole something very valuable."
    show cf 75
    mc "Oh, really? What was it?"
    show cf 74
    dup "You don't know? One of those Weapons of Atlas or something. I don't care about that bullshit, but if it becomes public that we can be robbed so easily, our stock will take a hit."
    show cf 75
    mc "I see..."
    mc "If I may ask, if that weapon was so valuable... why wasn't there more security? More Praetorians guarding it?"
    show cf 74
    dup "I don't know, you tell me."
    dup "Aren't you in charge of Ulysses' network security??"
    dup "Why isn't there a fucking Praetorian in every corner of Eternum?"
    show cf 75
    mc "Uh... well..."
    dup ". . ."
    show cf 74
    dup "...What was your name again?"
    show cf 75
    mc "Uh..."
    show cf 76
    npc "Good evening, gentlemen. Would you care for an hors d'oeuvre?" with dis12
    mct "Oof, thank god. He was backing me into a corner here."
    mct "He doesn't seem that invested in Eternum’s day-to-day goings-on though, unless it relates to the stock price. I won't get much more info out of him."
    show cf 77
    dup "I'll make it very clear to you: if you don't bring me my fucking wine in less than than 5 minutes, you will regret it."
    dup "Do you understand?"
    show cf 76
    npc "Of course, sir. My apologies."
    npc "I will be right back."
    show cf 74
    dup "Incompetent..." with dis12
    dup "Anyway, what were we talking about?"
    show cf 75
    mc "Um... I was saying that I'm headed to the kitchen to ask for an explanation."
    show cf 74
    dup "Good. Tell them to bring me my wine."
    show cf 75
    mc "Of course. Good evening, Dr. Du Pont."
    dup "*Grunts*"
    jump prefancymenu
label lmos:
    $ fancytalk2 = False
    show cf 80 with dis17
    mos "*Whispering*" with dissolve
    mc "Good evening!"
    mos2 "*Giggles*"
    show cf 81
    mos "Ah, good evening, young man." with dis12
    mos "How can I help you?"
    mc "You're Mr. Mos, right?"
    mos "Hah, I guess these masks don't cover enough."
    mos "Yes, I am. And this is my darling, Alice."
    show cf 82
    mos2 "Nice to meet you."with dis08
    mos2 "I'll let you talk. I need a glass of champagne. Do you need anything?"
    mos "No thank you, dear."
    show cf 83
    mos "Well..."with dis
    mos "You must be the man who stole the Gem from Garrington."
    mc "W-Wha..."
    mc "How do you..."
    mos "We have some business together, so I knew he was going to come here tonight. But it seems he lost the Gem at the last moment."
    mos "And then I noticed your tuxedo is not tailor-made, so I assumed you were one of the players invited tonight as part of the Gems event."
    mc "Wow, you're as sharp as they say."
    mc "Yeah, I had to buy this suit at the very last second, and I didn't have enough money to get a bespoke one."
    mos "That is unfortunate."
    play sound beep3
    show cf 84 with dis
    mos "Take this as a small token of welcome." with dissolve
    show screen eternals with dis08
    play sound coins
    $ money += 40
    pause .05
    $ money += 40
    pause .05
    $ money += 40
    pause .3
    hide screen eternals
    mos "No self-respecting man should go around without a good suit." with dis
    show cf 83
    mc "Did... did you just send me 120 eternals?!" with dis
    mc "Wow, thank you!"
    mos "This should be enough to have your suit tailored. True beauty comes from helping others."
    mct "Damn, I guess there are some good people working at Ulysses."
    mos "Is there anything else I can help you with?"
    mc "Well, now that you mention it... I've been wondering for a long time if..."
    mc "Do you know anything about..."
    menu:
        with dis
        "The Founder{#0.4,mos}":
            mc "The Founder?" with dissolve
            mos "Hmm."
            mos "He's a brilliant man. And most people don't realize how outrageously generous he is."
            mos "He could be charging monthly subscription fees, and every single player would happily pay it. Yet, he chose not to."
            mc "That is true."
            mos "But, personality-wise... I’m afraid there's not much I can tell you. He's a private man."
            mc "I see..."
        "The Syndicate":
            mc "The Syndicate?" with dissolve
            mos ". . ."
            mos "Where did you hear that name?"
            mc "Um... some people were talking about it in... a pub."
            mos ". . ."
            mos "It’s a group of people. They've been... causing some trouble."
            mos "You know, just small altercations and some public protests."
            mos "Nothing to worry about."
            mct "Hmm..."
            mc "I see..."
        "The Weapons of Atlas":
            mc "The Weapons of Atlas?" with dissolve
            mos "Ah, yes... Hyas, Dione, and Calypso."
            mos "Powerful artifacts. And the last one is yet to be found."
            mc "Yeah..."
            if not fancytalk1:
                mct "Du Pont knew that Calypso had been stolen. Mos has to know it too."
            else:
                mct "Hmm, doesn't he know someone stole it?"
            mct "Maybe he just wants to see my reaction...?"
            mc "I hope it's me who finds... Calypso, right? I've got some clues about its location!"
            mos ". . ."
            mos "Best of luck, kid."
            mc "Thanks!"
    mc "Well, I don't want to inconvenience you any more."
    mc "Thank you again for your gift, Mr. Mos."
    mos "My pleasure..."
    mct "I'm not sure why, but he has an air of mystery around him..."
    jump prefancymenu
label lastor:
    $ fancytalk3 = False
    $ calypso_interest += 1
    show cf 85 with dis17
    mct "Huh, looks like Calypso managed to blend in rather well." with dis08
    mct "What could they be talking about?"
    show cf 86
    ass "Actually, he was caught with HER sister in HIS office!"with dis
    show cf 87
    player2 "No way!"
    player2 "How do you always have the juiciest rumors in all of Eternum?"
    show cf 86
    ass "*Giggles* It's all about the connections, Susie."
    ass "Is there any particular rumor you'd like me to confirm or deny? I know them all..."
    show cf 87
    player2 "I heard the Founder was seen in Aphrodite's the other day. Is that true?!"
    show cf 88
    ass "*Giggles* Well, I didn't tell you this, but..." with dis12
    mct "Damn."
    mct "I'm digging the type of clothes these rich people are wearing. I wish Calypso or Alex would have chosen these threads..."
    show cf 90
    ass "Cutie?"with dissolve
    show cf 89
    mc "U-Uh...? What?"
    show cf 90
    ass "Any rumors you've heard about lately?"
    show cf 89
    mc "Oh... um..."
    mc "I've heard... that... Thanatos is actually a woman! That she walks on stilts and uses a voice changer to look like a big scary man."
    show cf 90
    ass "*Giggles* Oh, please, that's completely false."
    ass "Actually..."
    show cf 91
    ass "Keep this between us, but I go with him to the thermal baths of Hualalache." with dis08
    player2 "Really?!"
    mc "Huala what?"
    ass "I've seen him naked and... let me tell you, his stature is absolutely dwarfed by the weapon in his pants..."
    player2 "Oh boy!"
    mct "The thermal baths? That's total bullshit."
    mct "Next she’ll be trying to convince me that Thanatos is actually just 3 kids in a trenchcoat."
    show cf 86
    ass "And speaking of big instruments... I've got a new boyfriend, did I tell you?"with dis
    show cf 87
    player2 "Oh, tell me, tell me! Who is he?"
    show cf 86
    ass "I've been sleeping with a 24 year old bo–"
    play soundlow gasp
    show cf 92
    ca "*Gasps*" with hpunch
    mct "Eh?"
    ca "You unnatural deviant..."
    show cf 93
    ass "Um... excuse me?"
    show cf 92
    ca "How could you do that to an innocent child?"
    show cf 93
    ass "W-What? Did you hear me wrong? I said 24 years o–"
    show cf 92
    ca "I could hear you loud and clear the very first time! How dare you boast about such an act!"
    show cf 93
    ass "Um... What? I'm sorry, who are you again?"
    show cf 92
    ca "Me? I am Prin–"
    play sound clothes1
    show cf 89
    mc "S-She's a bit dizzy. Too much champagne!" with hpunch
    mc "If you’ll excuse us, I'll escort her to the restroom."
    show cf 90
    ass "Oh, I see. Of course."
    show cf 94 with dis2
    mc "*Whispering* What the hell was that?!" with dissolve
    play sound polyjuice
    show cf 95 with dis17
    mc "You promised me you'd try to go unnoticed!" with dissolve
    show cf 96
    ca "Am I supposed to stand idly by when people in this place abuse children, with nary a concern?" with dis12
    show cf 97
    mc "What the hell are you talking about?!"
    show cf 96
    ca "That woman said she's sleeping with a 24 year old! An infant!"
    show cf 97
    mc "Um... I'm still not sure how aging works with your race, but that's not an infant. Like, at all."
    mc "You know I'm only 18, right?"
    play soundlow gasp
    show cf 99
    ca "*Gasps*" with hpunch
    show cf98
    ca "You are... {w}18 years old?!"
    ca "I could barely walk when I was your age!"
    ca "You certainly... do not look 18."
    scene cf 99
    mc "Alex, Dalia, Luna, and Annie are 18 too."
    show cf 98
    ca "Sweet Mother of Celan'il, I have been spending time with toddlers!"
    show cf 99
    mc "We're not kids! We just grow faster than you!"
    mc "If you were human, you wouldn't look like this at 84 years old, I can assure you. You definitely wouldn’t have this... figure."
    mc "What's the life expectancy of the elves, actually?"
    show cf 96
    ca "Well... we grow up at a steady pace until we are 60 years old." with dis08
    ca "After 60 years, an elf is considered an adult."
    ca "Our bodies then stay physically the same for the next 2000-3000 years."
    show cf 97
    mc "Really? That's incredible! I wish we could live that long while looking eternally young."
    mc "And what happens after all those years?"
    show cf 96
    ca "We die, naturally. Although... it depends on the person. Lathlaeril, Lord of E'renabor, is still alive, and he is over 8000 years old."
    ca "It is said he fought in the War of the Last Alliance."
    show cf 97
    mc "Amazing."
    mc "And another question... I was wondering, what happens if a 60 year old elf sleeps with a 50 year old one?"
    show cf 100
    ca "What do you mean...?" with dis12
    show cf 101
    mc "Well, you know, if an \"adult\" elf has sex with an \"infant\" one... is that some kind of taboo or...?"
    show cf 100
    ca "Ah. I... should not be the one explaining this to a commoner, but... yes, that is... controversial."
    show cf 101
    mc "I see. Similar to our world, then."
    show cf 100
    ca "Although, it is nothing compared to inter-caste relationships, of course."
    ca "That is expressly prohibited."
    show cf 101
    mc "You mean like... a Prince with a peasant girl?"
    show cf 100
    ca "Yes. It is despicable and prohibited altogether."
    show cf 101
    mc "Come on... prohibited, yes, but despicable? The first time we met, you said you thought that relationships between humans and elves were hot because they were forbidden too..."
    show cf 100
    ca "I... n-never said such a thing."
    show cf 101
    mc "Oh! The Princess is lying to her people..."
    show cf 100
    ca "I..."
    ca "Agh, you are hopeless!"
    show cf 103
    ca "*Clears throat* Whatever, I will go back to the gathering." with dis12
    show cf 102
    mc "Don't get your hopes up, though."
    mc "I think that woman is making things up as she speaks."
    show cf 103
    ca "Yes, I noticed. These people pretend to be high society, but they are nothing but facades."
    ca "But I guess I will stay for now. I will be around if you need me."
    show cf 102
    mc "I'll call you if we need your help! Thanks Caly."
    ca ". . ."
    show cf 103
    ca "You are welcome."
    show cf 102
    mct "I called the Princess by a diminutive and I wasn't threatened with vaporization."
    mct "Making progress."
    play sound polyjuice
    jump prefancymenu
label lleavef:
    if fancytalk1 or fancytalk2 or fancytalk3:
        mct "Bah, I won't get anything out of these people. Let's go downstairs."with dis08
    else:
        mct "I pulled everything I could out of these people. Let's go downstairs." with dis08
    queue music2b classic1
    show cf 104 with dis2
    pause
    mct "Hmm, Alex is already here. She's talking to someone..." with dis08
    show cf 105
    x "Ah, finally! Come here, quickly!" with dis12
    x "Mr. Linus has something amazing to share with you!"
    mc "Really?"
    show cf 106
    mc "Well, I'm all ears."with dis
    show cf 107
    lin "It's nice to meet you. I'm Alastor Linus, ZipVerse's Chief Technology Officer."
    show cf 106
    mc "Pleased to meet you."
    show cf 107
    lin "My colleagues and I are interested in talking to you about our latest creation. We’ve finally put the finishing touches on our prototype of an artifact that will change Eternum forever."
    lin "At ZipVerse, our goal is to design products that allow users to answer daunting questions and explore the curiosities of the human mind."
    lin "For this project, we reached out to Eternum players to figure out the number one question on everyone’s mind..."
    play soundlow whoosh3b
    play sound ding volume 0.4
    show cf 108
    lin "DOES IDRIEL HAVE A PUSSY?!" with hpunch
    mc "Uh... excuse me?"
    show cf 108b
    lin "Eternum's NPCs are directly designed and controlled by The Founder's team. Whether you like it or not, Ulysses has the most advanced AI technology in the world."with dis08
    lin "Their NPCs are bound to do what they are programmed to do, no matter the situation."
    lin "And there was nothing we could do about it..."
    show cf 108
    lin "UNTIL NOW!"with dis08
    mc "Explain yourself..."
    show cf 108b
    lin "Each NPC has a chip on their neck, similar to our neural implants, that dictates their behavior." with dis08
    lin "It determines their role in the game, interactions, and... limitations."
    show cf 108c
    mc "And this artifact of yours..."
    show cf 108b
    lin "It is capable of reconfiguring the settings of said chip."
    show cf 108c
    mc "How?"
    show cf 108b
    lin "Let me offer you a practical demonstration..."
    show cf 109 with dis15
    lin "Hey there! Can you help us, cutie?"with dissolve
    show cf 110
    npc "Of course, sir. Is there anything I can do to serve you?"
    show cf 109
    lin "Actually... yes!"
    lin "I'd like to go with you to the restroom real fast to have some fun."
    npc ". . ."
    show cf 110
    npc "I'm sorry, I didn't understand your request."
    show cf 109
    lin "Let me rephrase it: I want you to come with me to the restroom so I can fuck your little pink cunt until it’s sore."
    show cf 110
    npc "...I'm sorry sir, we can't do that."
    show cf 109
    lin "Just a quickie."
    show cf 110
    npc "Please, do not insist or the Praetorians will intervene."
    show cf 109
    lin "Aw... that's too bad."
    lin "Can you give me your ID number, at least?"
    show cf 110
    npc "Of course. It's 012-574-111."
    show cf 111
    lin "Thank you." with dis
    mc "NPCs have ID numbers too? Like us?"
    lin "Yes, they all have one. It's linked to the chip I mentioned earlier."
    lin "*Talking to the artifact* 0, 1, 2, 5, 7, 4, 1, 1, 1."
    show cf 112
    lin "You enter the number, you rotate this thing as if it was a Rubik's Cube, and..."with dis
    npc "If you don't need anything else, I'll..."
    play sound glitch1
    show cf113
    pause 1.7
    scene cf 112
    npc "...I'll be on my way."with dissolve
    show cf 109
    lin "Not so fast... First, I want you to come with me to the restroom so I can fuck you."with dis
    show cf 110
    npc "Of course, sir."
    show cf 109
    mc "Holy shit!"
    x "What the hell..."
    lin "Go ahead. I'll be there in a minute..."
    show cf 108
    mc "How the fuck..." with dis12
    lin "It's a REVOLUTION!" with hpunch
    show cf 108b
    lin "And if you were wondering... yes, they have pussies. And they’re all unique, too!" with dis
    lin "It's simply... BRILLIANT!"
    show cf 108c
    mc "Are you not afraid of Ulysses taking action if they discover this?"
    show cf 108b
    lin "Ulysses and my company are trading partners. It wouldn't be the first time I've tried to push the limits while having fun."
    lin "And besides, we're using technology that could be found inside the world of Eternum, so... we're in a sort of legal gray area."
    show cf 108c
    mc "And could this... artifact be used with Idriel herself?"
    show cf 108b
    lin "I tried asking for her ID number, but she's not programmed to tell it to us like the rest of them. She seems to be more advanced."
    lin "But if somehow you managed to discover it... yes, it would be possible."
    lin "You could FUCK the Lady of Eternum!"
    show cf 108c
    mc "Well... that gives off a rapey vibe, to be honest... but technically it would also be possible to make her or other NPCs help you, or give you confidential info, right?"
    show cf 108b
    lin "Uh... well, I didn't think of non-sexual applications of the artifact, but... yes, I guess it would be possible, of course."
    show cf 108c
    mc "Interesting..."
    show cf 108
    lin "So what? Are you interested? One prototype for only 25!"with dis
    mc "25 eternals?! Absolutely! Give me 3!"
    lin ". . ."
    show cf 108b
    lin "...25 million." with dis
    show cf 108c
    mc "Oh..."
    show cf 114
    x "I'm feeling a bit sick. I'll go get some fresh air, meet me in the garden." with dis
    mc "...Sure."
    mct "What got into her all of a sudden?"
    stop music2b fadeout 2
    play sound doorecho
    show cf 116 with dis15
    play music2 suspense fadein 6
    mct "Oh, fuck..." with dis
    lin "William..."
    show cf 115
    will "Are you trying to rip people off with your junk again, Alastor?"
    show cf 116
    lin "M-My business is always legitimate."
    show cf 115
    will "I still don't understand why this company allows scum like you to come to these events."
    will "This is why it is in decay."
    show cf 116
    lin "I..."
    show cf 108b
    lin "I-I was leaving already. Um... I'll be in the Golden Room if you need me."with dis
    show cf 108c
    mc "Sure."
    play sound2 footsteps
    show cf 120 with dis15
    show cf 117
    blank "{i}William walks in front of you while you try to avoid eye contact." with dis15
    show cf 118
    will "I hope that clown didn't disturb you."
    show cf 117
    mc "N-No, it's all good, thank you."
    will ". . ."
    show cf 118
    will "Do we know each other?"
    show cf 117
    mc "No, I'm pretty sure we’ve never met before..."
    will ". . ."
    play sound doorecho
    show cf 119
    ax "Dad. Y-You have to come. Now."with dis
    mct "Oh shit, he's here too?!"
    will "Not now, Axel."
    ax "Dad, it's important! I... saw something!"
    ax "P-Please!"
    show cf 117
    will ". . ." with dis
    show cf 118
    will "I'm sorry, I must excuse myself."
    show cf 117
    mc "Mm-hm."
    will ". . ."
    stop music2 fadeout 3
    show cf 120 with dis15
    play sound doorecho
    play music3 crowdtalk volume 0.3
    pause
    mct "Oh my fucking god, why is he so terrifying?!" with dissolve
    mct "Phew, that was close... I thought he recognized me for a second."
    mct "I should go to the gardens with Alex... I've been here for too long."
    play music2b classic3 fadein 15
    stop music3 fadeout 8
    aaa "Psyche." with dis12
    show cf 121
    mc "Hmm?" with dis12
    mc "I'm sorry? Are you talking to me?"
    aaa "Isn't this sculpture fascinating?"
    show cf 122 with dis17
    mc "The... statue?" with dis08
    aaa "Yes."
    mc "Yeah, it's rather impressive."
    aaa "It represents Psyche, the goddess of the soul."
    mc "Mm-hm. Cool."
    show cf 123
    mc "And who's this one?"with dis15
    aaa "A man."
    mc "Well, yeah, I meant what man."
    aaa "Just a man."
    mc "So... no one in particular?"
    mc "Kind of an odd choice for a statue, isn't it?"
    aaa "It depends on whom you ask."
    aaa "Some people could see a god in the figure of a mere man."
    show cf 122
    aaa "Can a man obtain the power of a god?"with dis15
    aaa "Can a mortal subdue a deity?"
    aaa "Can a human transcend the limitations of mortality?"
    mc "Uh..."
    show cf 125
    aaa "I used to think that I understood the basic rules of our world, until I saw Eternum."with dis12
    aaa "Here... everything is different, and at the same time... exactly the same."
    mc "That's actually a good description. It has certainly transcended the term \"video game\"."
    aaa "*Snorts*"
    show cf 124
    aaa "A video game."with dis15
    aaa "Have you ever met the creator of a server?"
    mc "The creator of a server...? Well, not personally, no."
    aaa "They say most of them are created by the Founder and his \"team\". As if they were the only ones who could sculpt Eternum."
    mc "I've met some hackers, though. *Chuckles* That's... almost a developer, right?"
    aaa "What did they hack?"
    mc "What?"
    mct "Shit, did I talk too much?"
    show cf 122
    aaa "Let me guess. In-game computers? Drones? Databases? Chips? The Exit Portals?" with dis15
    mc "Erm..."
    aaa "Can they modify the terrain? Make you stronger? Become immortal? Change the rules of a world?"
    mc ". . ."
    mc "I guess not."
    aaa "Have you ever seen a single bug in Eternum? A glitch? Have you ever experienced lag? Or found the servers down?"
    mc "Uhh..."
    mc "I guess they have hundreds of people working every day to make sure the experience is absolutely perfect. That's what I meant when I said it's more than a video game."
    aaa ". . ."
    show cf 121
    aaa "Can I ask you a question, friend?"with dis15
    mc "...Of course."
    aaa "Why are you here? What did you come here looking for?"
    mc "Where? To this dinner?"
    aaa "Yes."
    menu:
        with dis
        "The Gems of Doom":
            mc "The Gems of Doom." with dissolve
        "Women":
            mc "Women." with dissolve
        "Money and power":
            mc "Money and... power." with dissolve
        "[gr]Answers":
            $ answersmenu = True
            mc "Answers." with dissolve
            show cf 122
            aaa ". . ." with dis15
            aaa "I see."
            aaa "In that case... meet me next to the main staircase at midnight."
            aaa "I must show you something."
            mct "What's going on with this guy?"
            mc "What is it? Why me?"
            aaa "You want answers? Just be there at 12."
            mc ". . ."
            mc "Okay, I will."
            aaa "Until then, friend."
            jump posmenuanswers
    show cf 122
    aaa "*Snorts*" with dis15
    aaa "That is fair."
    aaa "Good luck with your quest, friend."
    mc "Thanks..."
label posmenuanswers:
    stop music2b fadeout 12
    play music3 crowdtalk fadein 6
    show cf 126 with dis2
    mct "What the hell was that?" with dis
    mct "Just a weirdo, someone trying to mess with me, or..."
    mct "God, I've got a head like a beehive. Too much info and too many strange people in too little time."
    mct "I need a break."
    mct "I should join Alex in the gardens, some fresh air will do me good."
    stop music3 fadeout 11
    play music night fadein 8
    show ccc 1 with Dissolve(2.8)
    pause
    show ccc 2 with dis2
    mct "The gardens of this place are definitely impressive. They remind me of the Gardens of Versailles." with dis08
    mct "I wonder if they have NPCs taking care of them or if they hire real players... I'm not sure what would be cheaper."
    show ccc 3 with dis2
    mct "Aha! There she is." with dissolve
    mc "Hey! I finally found you!"
    show ccc 4 with dis12
    play sound grass
    mc "*Sitting next to her* Phew, that was close!" with dissolve
    mc "Thank god you saw your father coming, I don’t think the tattoo removal would have worked on him. He'd have definitely recognized you!"
    mc "I think he was even starting to remember me, even though we only saw each other for... maybe 20 seconds. And I had a mask on this time, too."
    show ccc 5
    x "Yeah... he never forgets a face."
    show ccc 4
    mc "And that's not all, do you know who else was with him? Your brother!"
    mc "I guess he was attending as William's guest."
    show ccc 5
    x "Huh."
    show ccc 4
    mc "But he was way too agitated, so he didn't notice me, luckily."
    mc "I wonder why he was so anxious..."
    show ccc 5
    x "Who knows."
    show ccc 4
    mc ". . ."
    if alexpath and alex_points >=5:
        mc "Are you okay, Alex? You seem distracted."
    else:
        mc "Are you okay, Alexandra? You seem distracted."
        show ccc 5
        x "Yeah, sorry, I was just..."
        x "Remembering something."
        show ccc 4
        mc "Do you wanna talk about it?"
        show ccc 5
        x "No, I'm okay. It's nothing."
        x "Let's go back to the mansion."
        jump v4alex
    $ renpy.music.set_volume(0.2, delay=12.0, channel='music')
    show ccc 6 with dis17
    play music2 stargazing fadein 2
    x "Do you see that?" with dis08
    mc "The moon?"
    x "No, underneath it."
    mc "Oh, the red star?"
    x "Yes."
    x "I can't believe we can see it..."
    show ccc 5
    x "Do you..."with dis12
    x "Do you mind if we stay out here for a bit?"
    show ccc 4
    menu:
        with dis
        "[gr]Nah, let’s hang out here":
            mc "Nah, let’s hang out here." with dis08
        "Let's focus on our goal first\n[red][mt](Closes Alex's path)":
            mc "Uhh... let’s focus on our goal first. We can come back here after we've talked to all the guests at the mansion." with dis08
            mc "We can't waste this opportunity."
            show ccc 5
            x "Yeah... you're right. Let's go."
            jump v4alex
    mc "The other guests won't go anywhere. The sushi is far too good for that to happen."
    show ccc 5
    x "*Chuckles* True."
    play sound grass
    show ccc 10
    mc "*You lay down next to her* So... what's so special about this red star?" with dis15
    play sound2 grass
    show ccc 7
    x "That star is RW Cephei." with dis15
    x "It's a variable star that can only be seen from our hemisphere for 3 days each year. October 14th to October 16th."
    show ccc 10
    mc "Really? And today it's..."
    show ccc 9
    x "...October 14th."with dissolve
    show ccc 7
    x "How..."with dis
    x "How can Eternum be so... real?"
    x "How can a simulation be so thoroughly accurate?"
    x "How... I mean..."
    show ccc 9
    x "Someone with a high degree of astronomy knowledge knew about this star, worked on Eternum, and made sure to implement something that just a handful of people in the world would notice."with dis
    x "And only if they played in a night server during those days! Think about the odds of that!"
    x "It's... mind-blowing."
    show ccc 11 with dis15
    pause
    mc "Do you believe in magic?" with dis
    x "*Chuckles* What?"
    x "I've been in fantasy servers, yeah."
    mc "No, not like that. I mean like... in the real world."
    mc "I met someone after you left, back at the mansion."
    mc "He looked strange, and he was saying weird things, but... he mentioned something that I’ve been kicking around in my head: that Eternum is \"more than a video game\"..."
    mc "That there's something more than coding and technology behind it."
    show ccc 10
    mc "What if... what if he was right? What if {i}there is{/i} something else...?" with dis
    show ccc 7
    x "Well, you're not alone in that."with dis
    x "There're literally thousands of forum posts online with people posting theories about how Eternum is the Matrix, how Eternum is another dimension, or how the real world is just another server."
    show ccc 8
    mc "So you don't believe it?"with dissolve
    show ccc 7
    x "Nah, I don't."with dissolve
    x "I don't believe in magic."
    x "But..."
    x "I would certainly {i}like{/i} to believe it."
    x "I wish I could believe in magic."
    x "It'd just make our world... better. Less boring. Don't you think?"
    show ccc 8
    mc "It certainly would..."with dissolve
    show ccc 7
    x "I guess I'd have to see something for myself that made me believe in it. It's not like there's a switch I can flip, you know?"with dissolve
    x "For now, I'll stay with my dumb stars and boring, rational scientific explanations."
    show ccc 10
    mc "Hey, stars are not dumb. It's all a matter of perspective." with dis
    mc "Maybe you just need a stargazing partner."
    show ccc 7
    x "Yeah, you might be right..."with dis
    x "I used to go stargazing at night with my grandma. She knew all the constellations!"
    show ccc 11
    x "Do you see that bright one? That's Ursa Major." with dis
    x "Underneath it there's Leo, and... oh, that W-shaped constellation is Cassiopeia."
    mc "Um... I'm sorry, it all looks the same to me. I can't see anything."
    show ccc 7
    x "*Chuckles* It's normal if you've never done this before. At first I couldn't see anything either, just a sea of stars with no semblance of order whatsoever. It took me a while..."with dis
    x "After my grandma passed away, I thought I'd never go stargazing again, but... I kept on doing it. Kinda to keep her memory alive, y’know?"
    x "I remember sneaking outside the house when my parents started arguing and spending hours looking for constellations."
    x "I snuck out so many times that I ended up learning them all."
    show ccc 8
    mc "Did they use to fight a lot?" with dissolve
    show ccc 7
    x "Uh huh. Constantly. I used to feel like fighting was their only interaction."with dissolve
    show ccc 8
    mc "That... must be terrible for a kid. It must have been tough after your grandma died."with dissolve
    show ccc 7
    x "Well, it depends on who you ask."with dissolve
    show ccc 9
    x "I lived in a big house. I had nannies, butlers, chefs... everything that money could buy."with dis
    x "Many people would say I was living the dream."
    x "It just wasn’t... my dream."
    show ccc 7
    x "Growing up, everything I did had to be... regimented."with dis
    x "“Alex, don’t put your elbows up on the table, we have international diplomats coming to visit for dinner tonight. Your dad’s promotion hinges on this.”"
    x "“No, Alex, you can’t get your ears pierced. That's improper.”"
    x "“Alex, don’t eat all that food on your plate, that’s not how a woman in higher society should behave...”"
    play soundlow grass
    show ccc 15
    x "At a certain point, I just... {w}snapped." with dis15
    x "I wasn’t being treated like my own person, I was just a doll... a fucking marionette that my parents wanted to show off and display."
    x "I just... couldn't take it anymore."
    show ccc 14
    mc "No one could blame you. You held on longer than I would have."with dissolve
    mc "You made the right choice."
    show ccc 15
    x "I..."with dissolve
    x "*Snorts* There was one summer..."
    x "I was supposed to be spending it at some hoity-toity boarding school abroad."
    show ccc 11
    x "One night, I was gazing at the night sky, just like this. Underneath the stars, looking for some sign. And I made a decision..."with dis
    x "The next morning, I told my parents that I wouldn't go to the school and... that I didn't want to carry on the family business."
    x "My mother started yelling at me, but my father limited himself to just giving me a look of pure contempt."
    show ccc 15
    x "And that’s when “bad girl” Alex was born."with dis
    x "The lockpicking, playing hooky, the attitude, all the tats..."
    show ccc 16
    x "Oh man, the tats! You should have seen the look on Axel’s face when I got the first one!"with dissolve
    x "A mixture of anger, pity... and honestly, a little envy... I'd pay to see that again!"
    mc "*Chuckles* Oh, you and me both!"
    play sound grass
    show ccc 7
    x "*Lying back* I just didn’t want to be controlled." with dis15
    x "I didn't want to be told what to do or wear or eat."
    x "I wanted to be... {w}myself."
    x "...Does that make any sense?"
    show ccc 8
    mc "Absolutely."with dissolve
    show ccc 7
    x "These tattoos that I had to hide tonight..."with dissolve
    x "I {i}hated{/i} doing that. I felt like I was burying part of myself, conforming to what others want me to be. And that’s not who I am."
    x "I control my own life, I should be able to do what I want without worrying that I’m hurting someone’s delicate sensibilities about how I should be acting."
    x "I'm..."
    x "...my own person." with dissolve
    stop music2 fadeout 8
    $ renpy.music.set_volume(1.0, delay=10.0, channel='music')
    play sound grass
    show ccc 12
    x "God, I'm sorry, I must sound like such a prissy brat!" with dis12
    x "I don't know what got into me."
    x "Thank you for sticking around for my TED talk, though. I appreciate that you didn’t fall asleep."
    show ccc 13
    mc "*Chuckles* What are you talking about? I loved having this conversation with you."
    mc "I like seeing you opening up with me."
    show ccc 12
    x "Well, don't get used to it."
    x "You just caught me in a rare moment of weakness."
    show ccc 13
    mc "Yeah, that's my specialty."
    mc "The crickets, the full moon, the stars..."
    mc "It was all part of my nefarious plan."
    show ccc 12
    x "Oh, is that so...? So you just wanted to get close to me because of my family's money, after all."
    show ccc 13
    mc "Yeah, totally, that was the initial idea. I'm a gold digger!"
    mc "But after getting to know you better, I discovered a few things that I like much more than that. So now, the Bardot riches no longer interest me."
    show ccc 12
    x "Oh, really?"
    x "Tell me, what things did you discover that you like so much?"
    show ccc 13
    mc "Ah, nice try. I know you don't like compliments. You won't catch me this time."
    mc "However, you can try telling me what things you like about me. I’d love to hear that."
    show ccc 12
    x "About you? I don't like anything."
    show ccc 13
    mc "Nothing at all? Come on, try giving it some thought."
    play soundlow leaves2
    show ccc 17 with dis15
    x "*Standing up* Hmm..." with dissolve
    x "Oh! You..."
    x "Maybe..."
    x "Hmm... no, nothing comes to mind, I'm sorry."
    show ccc 18 with dis12
    mc "*Chuckles* Let me help you..." with dissolve
    mc "You could say that I'm a good listener. Or that I'm a pretty funny guy."
    show ccc 19
    x "We have different definitions of funny, I think."with dis04
    show ccc 18
    mc "Then you could say that you like that I'm sporty as well, just like you. I'm in pretty good shape, you have to admit."with dis04
    show ccc 19
    x "I think skinny and scrawny are better descriptions."with dis04
    show ccc 18
    mc "Alright then, you at least have to recognize that I'm a very good Eternum player."with dis04
    mc "I managed to find not one, but two Gems of Doom in my first month of playing."
    show ccc 19
    x "Oh, that was pure luck." with dis04
    x "And we girls did all the legwork! You just happened to be there."
    x "You alone wouldn't even be able to find sand in the desert."
    show ccc 18
    mc "*Chuckles* You're really full of yourself, you know that?"with dis04
    show ccc 19
    x "Here, I’ll prove it. There's a small maze right here..."with dis04
    show ccc 18
    mc "Oh, you just dug your own grave. Get ready to be humiliated, girl."with dis04
    mc "You're about to discover why they call me [mc] \"Theseus\" [lastname], the Labyrinth Master."
    show ccc 19
    x "*Snorts* Let's see about that..."with dis04
    show ccc 20 with dis2
    x "Alright, here's the entrance..."with dis08
    x "First one out the other side wins..."
    show ccc 20b
    mc "What's the prize for winning?"
    show ccc 20
    x "Just the honor of victory, of course."
    show ccc 20b
    mc "And nothing else? No extra bonus prize for the winner...?"
    show ccc 20
    x "Hmm... maybe we can arrange something."
    show ccc 20b
    mc "Like what?"
    $ renpy.music.set_volume(0.6, channel='music3')
    stop music fadeout 15
    play soundlow leaves2
    show ccc 21 with dis17
    play music3 sexyalex fadein 8
    x "*Entering the labyrinth* Get to the other side first and find out..."with dis08
    mc "Oh boy..."
    show ccc 22 with dis22
    mc "You have no chance, Alex." with dis08
    x "Really? Because I think I see the exit already..."
    show ccc 23 with dis2
    x "[mc]? Are you lost?"with dis08
    mc "Of course not. I'm about to get out, actually."
    x "Sure..."
    show ccc 24 with dis2
    mct "Hmm..." with dis08
    mct "I think I've walked by this spot before..."
    mct "Maybe I can..."
    show ccc 22 with dis2
    pause
    show ccc 23 with dis2
    pause
    show ccc 25 with dis2
    x "And... it's over, ladies and gentlemen!" with dis08
    x "I've got bad news, [mc]. I've reached the other side."
    x "Are you still there?"
    show ccc 26
    x "I'd wait for you, but I've gotta go back to the mansion. Important mission and all." with dis
    x "Don’t feel too bad about coming in second place, I never lose."
    x "Anyway, there’s still a lot of–"
    play sound leaves
    play sound2 leaves
    show ccc 27
    mc "Well, well, well... FINALLY!"with hpunch
    x "W-What?!"
    x "When did you get out?"
    mc "I've been waiting for you for 10 minutes now. I was starting to think you’d be lost in there forever."
    show ccc 28
    x "*Chuckles* Don't bullshit me." with dis08
    x "We weren’t inside for more than 3 or 4 minutes, and I was clearly ahead of you."
    show ccc 29
    mc "Well... I might have jumped over a hedge or two."
    show ccc 28
    x "Hah! I knew it. You're a fucking cheater."
    show ccc 29
    mc "We didn't specify the rules anywhere."
    mc "Now... where's my prize?"
    show ccc 28
    x "Oh, I know what you want, and... you wouldn't be able to handle it, pretty boy."
    show ccc 29
    mc "I'm pretty sure I would..."
    mc "I know you better than you think. I definitely could handle you."
    mc "I know that under that tough girl facade of yours, you're as sweet as a cupcake. You can't deceive me."
    show ccc 28
    x "*Chuckles* I'm too much woman for you, [mc]."
    show ccc 29
    mc "I could totally prove you wrong, Alex..."
    play sound clothes3
    show ccc 30 with dis15
    x "*Removing her gloves* Oh, could you? And how would you do that, exactly?" with dis08
    show ccc 30b
    mc "Give me 20 minutes and I'll show you."with Dissolve(.4)
    show ccc 30
    x "How about 20 seconds?"with Dissolve(.4)
    show ccc 30b
    mc "Oh, are we negotiating now?"with Dissolve(.4)
    show ccc 31
    x "We're not. That's my..." with dis17
    play sound zippo
    stop music3 fadeout 5
    play music night fadein 4
    pause .2
    show ccc 32 with dis15
    play sound2 zippo
    mc "What's that noise? Is someone coming?" with dis08
    show ccc 33 with dis15
    mct "Goddammit, nice timing..."with dis08
    mct "They're gonna kill the mood, whoever they are."
    show ccc 34
    mc "Hmm?" with dis08
    show ccc 35
    play sound zippo
    will "*Lights a cigarette*"
    play sound2 smoke
    show ccc 36
    will "*Exhales*" with dis17
    show ccc 38
    mc "Oh man, you have to be kidding me..." with dis15
    show ccc 37
    x "Who is it?"
    show ccc 38
    mc "It's... y-your father."
    show ccc 37
    x "My father? What’s he doing?"
    show ccc 38
    mc "He's smoking. He's... just standing there, menacingly. If looks could kill, I’d be super worried."
    show ccc 37
    x "Hmm, yeah, sounds like him."
    show ccc 38
    mc "Wait, someone else is coming..."
    play soundlow leaves2 volume 0.3
    show ccc 39 with dis15
    mc "Oh shit, it's your brother..." with dis08
    x "It's so nice to see the Bardot family reunited."
    ax "Dad, I swear to god, it was him!" with hpunch
    will "Go back to the party, Axel."
    ax "Maybe he's in witness protection! Or maybe..."
    will "I told you to drop that line of thinking. I will not repeat myself."
    ax "B-But you have to listen to me!"
    ax "It makes no sense that–"
    play sound leaves
    play sound2 leaves
    play sound3 leaves
    play sound4 punch
    show ccc 40
    will "ENOUGH!" with hpunch
    will "I'M GETTING SICK OF YOUR IDIOCY!" with hpunch
    will "You have to start taking things seriously! I will not have you sullying the Bardot name, like your sister!"with hpunch
    ax "I-I'm sorry, Dad..."
    will "Now get back to the fucking mansion and do what you were told!"
    will "ARE WE CLEAR?" with hpunch
    ax "Y-Yes! I'm s-sorry..."
    play sound smoke
    show ccc 36
    will "I’m surrounded by idiots fucking everywhere." with dis17
    show ccc 38 with dis15
    mc "Seems like they had a fight and Axel ran away." with dis08
    show ccc 37
    x "What were they talking about?"
    show ccc 38
    mc "I'm not sure, I didn't quite catch it. They're too far."
    play soundlow leaves2
    show ccc 41
    mc "O-Okay, I think Axel went back to the mansion, but William is still there." with dis12
    mc "But... f-fuck, I left my mask at the entrance of the maze. We can't let them see us."
    mc "W-We'll wait here until he goes back to the mansion."
    show ccc 42
    x "*Giggles* You sound a little shaky, [mc]." with dis08
    x "Are you afraid of my daddy?"
    show ccc 43
    mc "W-What? I'm not!"with dissolve
    show ccc 42
    x "Are you shaking because of Axel, then? Is he the one making you so nervous?"with dissolve
    x "You can admit it, don't worry. I won't laugh."
    show ccc 43
    mc "Of course not! Not now, not ever..."with dissolve
    show ccc 44
    x "Then... Why are you nervous, [mc]?" with dis15
    mc "What are you doing?!"
    stop music fadeout 18
    play music3 sexyalex fadein 6
    x "Maybe it's... because of me?"
    mc "W-What? No!"
    show ccc 45
    x "No? I don't make you anxious? Not one tiny... little... bit...?" with dis12
    mc "Not one bit..."
    play sound clothes3
    show ccc 46
    x "And what if I do this?" with Dissolve(1.4)
    x "Still nothing...?"
    mc "Nothing..."
    play sound2 clothes3
    show ccc 47
    x "And now...?"with Dissolve(1.4)
    mct "Oh god..."
    mct "This feels so dangerous, yet so exciting..."
    mc "I've never been calmer..."
    play sound3 clothes3
    show ccc 48
    x "I guess I've lost my touch. I'm used to getting people on edge..."with Dissolve(1.4)
    mc "You'll have to try harder with me..."
    show ccc 49
    x "Well, I do like challenges... and like I told you, I never lose..." with dis12
    mc "We’ll see about that..."
    play sound belt volume 2
    x "*Removing your belt* Now tell me...."
    x "What if I..."
    show ccc 50
    x "(Hmm?)" with dis
    show ccc 51
    x "(Holy shit, his cock is huge as fuck!)" with dis12
    x "(This is... certainly not what I was expecting.)"
    x "(I was joking about salami the other day, and this whole time he was packing this...)"
    mc "You okay, Alex? You're so quiet all of a sudden..."
    mc "Are {i}you{/i} nervous about something...?"
    show ccc 52
    x "O-Of course not... It's just that..."with dissolve
    x "I-I'm surprised you got hard so fast. That's all. Couldn’t help yourself, eh?"
    show ccc 53
    x "But I guess it's a natural reaction when you're tense..." with dissolve
    mc "You’re not letting up on that, huh?"
    mc "I'm sorry to burst your bubble, but I feel very relaxed next to you. No nervousness whatsoever."
    show ccc 54
    blank "{i}Alex grabs your penis softly, but firmly." with dis15
    x "This doesn't look relaxed to me."
    mc "{size=28}O-Oh, god..."
    show ccc 55
    x "I'm sorry? Did you say anything?" with dis12
    mc "N-Nothing."
    scene ccc 54
    mc "Y-your hands are just... cold." with dis12
    x "*Chuckles* Yeah, I bet..."
    show boyle1 with dis2
    mc "Oh, f-fuck..." with dissolve
    mc "O-O-Oh god..."
    x "Shhhh..."
    x "Keep your voice down..."
    x "You wouldn’t want my daddy to hear us, would you...?"
    mc "O-Okay, I'll admit it... you're making me a bit nervous now, A-Alex..."
    mc "T-This was fun, b-but we’ve gotta hide..."
    mc "What if your father finishes his cigarette and comes this way...?!"
    x "You’re scared of him seeing us do this?"
    x "If he saw you, with your pants down, getting your huge, thick cock rubbed by his little girl... After what you said to him the other day in my house?"
    x "He'd definitely kill you..."
    x "Seriously, he would. No joke. He'd send someone to kill you in the real world."
    x "Not because he cares about me, but because this is the ultimate way of “sullying the Bardot name”, you know?"
    x "The daughter of one of the richest, most powerful men on the planet, is currently giving you a handjob, less than 20 feet away from her dad."
    mc "AAahh..."
    mc "I d-don't want him to kill me..."
    x "*Giggles* Isn't it thrilling? The risk of getting caught? My boobs pressed against your back... my hands holding onto your manhood, giving you these long... slow... strokes..."
    mc "I-It's... a c-confusing mixture of emotions..."
    x "Well... I’ll tell you what... if you finish before he puts out his cigarette, I'll let you hide..."
    mc "What? I-I can't finish before he does..."
    x "Oh, is that another challenge...?"
    mc "Aahh... w-what?"
    play soundlow leaves2
    scene ccc 56
    blank "{i}Alex stops and walks in front of you." with dis15
    show ccc 57
    x "I see what you're trying to do..."
    x "This has now become personal."
    show ccc 56
    mc "What? I'm not trying to do any–"
    play sound clothes3
    show ccc 59 with dis15
    mc "Holy shit..." with dissolve
    mc "Those perky nipples... I’ve thought about them ever since we visited Ogygia..."
    play soundlow leaves2
    show ccc 60
    blank "{i}She kneels down before you and grabs your dick once again." with dis12
    mc "Oh god..."
    show ccc 61
    x "Do my hands still feel cold?"
    show ccc 60
    mc "Not anymore..."
    scene ccc 61
    x "Good..."
    $ renpy.music.set_volume(0.2, delay=10.0, channel='music3')
    play music wetting3 fadein 6
    show boyle2 with dis22
    mc "O-Oh Jesus!" with dissolve
    mc "F-Fuck..."
    mct "God, I can't believe Alexandra Bardot is giving me a handjob..."
    mc "Ahhh..."
    mc "This is a t-terrible idea, Alex..."
    mc "But... fuck, I love seeing your tits bouncing like that..."
    mc "You’re driving me insane..."
    mc "I'm not gonna last much longer at this rate..."
    x "That's the idea."
    mc "You're enjoying this too, right, you pervert?"
    mc "Your hard nipples give you away..."
    x "I'm enjoying the thrill of the risk. We could be caught at any moment."
    x "Check your ego..."
    pause
    scene black
    show boyle3 
    with dis22
    blank "{i}Alex starts massaging your balls and increases the speed of her shakes even further." with dissolve
    mc "G-God..."
    x "Do you like this...? Calling ME a pervert, when you’re such a dirty boy, [mc]..."
    mc "Y-Yeah..."
    mc "Ahhh..."
    mc "This is definitely not how an upper-class lady should behave, Alex..."
    x "Yeah..."
    x "It definitely isn't..."
    x "But who gives a fuck? I've never been part of this world anyway... right?"
    x "Fuck them all..."
    mc "Y-Yeah, fuck them all..."
    mc "AAahh, yeah..."
    x "Are you gonna cum...?"
    mc "Not yet..."
    x "Are you close?"
    mc "I'm not sure..."
    stop music fadeout 1
    scene ccc 61
    x "You're gonna make me sweat, aren't you? You’re gonna make me work that load out?" with dis
    show ccc 60
    mc "I know you can try harder..."
    show ccc 61
    x "*Chuckles* Fuck you."
    x "Very well, then..."
    show ccc 62 with dis15
    x "Let's try a bit harder..." with dis08
    mc "Oh fuck yes, that's it..."
    x "Will my tight, little mouth be enough?"
    mc "We'll see..."
    mc "Let me feel it..."
    show ccc 63
    blank "{i}She puts your dick inside her mouth and starts caressing your glans with her tongue." with dis12
    mc "Oh... F-FUCK!"
    show ccc 62
    x "Keep your voice down, you idiot..."with dis15
    mc "S-Sorry..."
    scene ccc 63
    mc "I... aahhh... I forgot..."with dis12
    play music blowjob2 fadein 3
    show boyle4 with dis22
    mc "Oh my f-fucking god..."with dis08
    mc "Ahhh... yeah... that's the spot, Alex..."
    mc "Don't stop..."
    stop music fadeout 2
    scene ccc 64 with Dissolve(1.75)
    play soundlow putoutcigar
    will "*Putting out his cigarette*"with dis
    mc "Aaahh...!"
    will ". . ."
    show ccc 65
    will ". . ." with dis15
    blank ". . . . . ."
    will ". . ."
    show ccc 66
    will "*Leaving* This company needs a fucking purge." with dis15
    play music blowjob2 fadein 3
    show boyle4 with dis22
    x "Mmmmm...."with dissolve
    mc "Oh g-god..."
    mc "Your mouth feels amazing..."
    mc "Do you like the taste of my cock, Alex?"
    x "Mmmffhhh..."
    mc "I'll take that as a yes..."
    x "Mmm-hmmmm..."
    mc "You look so good taking that cock in your mouth..."
    mct "I’d love to feel how my dick stretches her {i}other{/i} lips..."
    x "*Gagging* Mmmmh..."
    mct "Fuck yes, she's drooling all over me..."
    mc "Oh yeah..."
    mct "I wish I could push it further..."
    scene black
    show boyle5 
    with dis22
    blank "{i}As if she had heard your thoughts, Alex suddenly increases her pace, taking your cock deeper into her throat." with dissolve
    mc "Ohhh... F-FUCK!!"
    x "*Gagging* Mmmmm... mmmmhhh... mmmmmfffhhh..."
    mc "Oh babe..."
    mc "Oh my god..."
    mc "J-Just like that...!"
    x "*Gagging* MMmmhh..."
    mc "Aaahhh..."
    mc "Your mouth feels so tight..."
    x "Mmmm..."
    mct "She's completely obsessed..."
    mc "I'm gonna cum so much, Alex..."
    mc "You’re doing such a good job, I can feel it coming..."
    menu:
        with dis
        "Cum in her mouth":
            $ boylemouth = True
        "Cum on her face":
            $ boylemouth = False
    mc "Aaahhh... I'm almost..."with dissolve
    mc "I'm..."
    stop music fadeout 1
    if boylemouth:
        scene ccc 67b with dis
    else:
        scene ccc 69b with dis
    play sound cum2 volume 1.5
    play sound2 cum1
    play sound3 cum3
    if boylemouth:
        show ccc 67
        blank "{i}You grab Alex's head and unload your seed deep inside her throat." with hpunch
    else:
        show ccc 69
        blank "{i}You push Alex away at the last second and you unload your seed all over her." with hpunch
    play sound cum2 volume 1.5
    play sound2 cum1
    play sound3 cum3
    mc "AAaaaaaarghh..." with hpunch
    if boylemouth:
        show ccc 68 with dis15
    else:
        show ccc 70 with dis15
    mc "Oh my god..." with dis08
    mc "Holy shit, that was a lot..."
    x "Hmph."
    stop music3 fadeout 8
    play musicb night fadein 10
    play soundlow leaves2
    if boylemouth:
        show ccc 73
        x "*Standing up* You could have warned me or something, you fucking idiot." with dis17
    else:
        show ccc 71
        x "*Standing up* God, what a fucking mess."with dis17
        mc "Y-Yeah, sorry about that."
        show ccc 72
        x "*Wiping her face* You could have warned me or something, you fucking idiot."with dis12
    mc "I did! But you were too engrossed in your task..."
    show ccc 73b
    x "That's not true! You didn't say shit!" with dis12
    x "And I w-wasn't engrossed in anything."
    show ccc 74
    x "But anyway, what matters is that I won! You came before my father finished his cigarette!" with dis12
    mc "I... think he left a while ago."
    show ccc 75
    x "WHAT?!" with dissolve
    show ccc 75b
    x "Goddammit!"
    x "When did he leave?"
    mc "I'm not sure... 5 or 6 minutes ago?"
    x "5 minutes ago?!"
    show ccc 77
    mc "See! Totally engrossed! You even lost track of time."with dis
    mc "It was just too good..."
    show ccc 76
    x "It wasn't that great..."
    show ccc 77
    mc "Well, it was for me."
    show ccc 78
    x "*Snorts* Yeah, I can imagine."
    mc "Can't wait to tell everyone what I did with one of the Bardots."
    show ccc 79
    x "Whoa, whoa! Hold your horses! Y-You tell anything to anyone and you're a dead man!" with dis08
    x "You hear me?"
    x "DEAD!"with hpunch
    show ccc 80
    mc "It was a joke!"
    show ccc 79
    x "I don't care if it was a joke or not, you're not telling shit to anyone! Not Dalia, not Chang, NO ONE!"
    show ccc 80
    if daliapath:
        mct "Huh, this reminds me a lot of the situation with Dalia at the Cove."
        mct "She reacted the same way."
        mct "The pair of them are actually quite similar..."
        mct "Can you imagine if I ever got both of them to–"
    show ccc 79
    x "ARE YOU LISTENING TO ME?!" with hpunch
    show ccc 80
    mc "N-No one! I swear!"
    mc "Don't worry, you can trust me!"
    mc "N-No one will ever know. I don't even remember what happened. What are we talking about? Did something happen?"
    x ". . ."
    show ccc 79
    x "...Good."
    x "This didn't happen."
    show ccc 80
    mc "It never happened."
    show ccc 83
    x "Okay... now that that's clear... I guess we should go back to the party."with dis12
    x "And by the way, I forgot to hand this to you earlier since you were late."
    x "This is a communicator I got from Nova. It can be easily hidden and it works in all servers where technology is allowed."
    x "Call me if you need me or in case of an emergency."
    show ccc 84
    mc "Oh, that's neat! I’ve gotta thank Nova later."
    mc "But wait, you're not coming back inside with me?"
    show ccc 81
    x "No, you go ahead. I'll go to the fountain I saw back there to... *clears throat* ...clean myself a little."with dis2
    mc "Oh... yeah, sorry about the mess... That makes sense, though. I'll wait for you in the main hall."
    x "Alright."
    mc "Thank you for this, Alex, you made this a very special night..."
    x ". . ."
    $ alex_points += 1
    x "It certainly was..."
    play sound beat
    show screen heartbeat
    x "...special."
    show ccc 82 with dis2
    mct "Damn, boy!"with dis08
    mct "That was something else."
    mct "And not only the blowjob... I loved seeing Alex open up with me when we were stargazing."
    mct "This dinner turned out better than I could have ever imagined. I came looking for copper and found gold!"
    mct "Maybe this could be the beginning of something more with Alex...? Could it be possible?"
    mct "I think I saw her smirking when she turned the corner... Maybe the ice queen’s heart is finally melting?"
    mct "Hmmm..."
    mct "Anyway, I'll worry about that later."
    mct "I should pick up my mask from the maze entrance and head back inside now."
    jump ending04


label v4alex:
    play soundlow leaves2
    stop music2 fadeout 8
    $ renpy.music.set_volume(1.0, delay=10.0, channel='music')
    show ccc 85 with dis17
    x "*Standing up* Oh by the way, I forgot to hand this to you earlier since you were late."with dissolve
    x "Take this communicator I got from Nova. It can be easily hidden and it works in all servers where technology is allowed."
    x "Call me if you need me or in case of an emergency."
    show ccc 86
    mc "Oh, that's neat! I’ve gotta thank Nova later."
    mc "But wait, you're not coming back inside with me?"
    show ccc 85
    x "No, you go ahead. I saw Ms. Dilinger going to the fountain near the entrance. She's Ulysses' PR manager, I think I can get some info from her."
    show ccc 86
    mc "Oh, clever."
    mc "Alright, I'll see you inside. I'll be waiting for you in the main hall."
    mc "Good luck!"
    show ccc 2 with dis22
    mct "I wonder what she was thinking about..." with dis08
    mct "Maybe I can try to ask her about it after we're done here, although... I doubt she'd share it with me."
    mct "Anyway, let's get back inside for now."
    $ alexpath = False
    $ alexu = False
    jump ending04


label ending04:
    stop musicb fadeout 4
    show black
    show screen afewminuteslater
    with Dissolve(2.2)
    pause
    play soundlow doorecho
    $ renpy.music.set_volume(0.15, channel='music3')
    play music3 crowdtalk fadein 5
    hide screen afewminuteslater
    show cz 0
    with dis22
    pause
    mct "Alright, back to business." with dis08
    mct "Now that I think about it, I haven't seen any other Gem holders. I wasn't expecting Thanatos to show up, but there has to be at least another one..."
    mct "Maybe I should take another look around."
    show cz 0b
    dup "William asked me to sell him my part of the company again." with dis15
    dup "I don't know what to do, honestly. I think Mos already agreed."
    show cz 0c
    if not fancytalk1:
        dup "Hmm? Oh... the IT guy."with dis08
        mc "Uh?"
        mc "Oh, y-yeah! That's me!"
    else:
        dup "Hmm? Who are you?" with dis08
        mc "Uhh... I'm Raimond. I'm... in charge of Ulysses' network security."
        dup "...I see."
    dup "We're going to the Golden Room. Are you coming?"
    mc "Well... it's 11:00 PM. The Founder must be about to arrive, right? I thought he'd give a speech or something."
    dup "*Laughs* What? Is this your first Ulysses dinner?"
    mc "Um... yeah, it is, actually. Why?"
    dup "The Founder is not coming. He never does."
    mc "What...?"
    play music2 mystery2 fadein 14
    stop music3 fadeout 15
    show cz 0d
    ass "Yeah, one of the NPCs just told me that he had an emergency and he had to cancel his appearance at the last moment. Hah! What a surprise!" with dis08
    show cz 0c
    mc "He does this a lot?"with dis08
    show cz 0d
    ass "Yeah, all the time. It's... quite funny, actually. I don't know why he doesn't just say he's not coming from the beginning."with dis08
    show cz 0c
    mc "Maybe he's not a very social person."with dis08
    show cz 0d
    ass "Maybe. I'll ask him myself if I ever see him."with dis08
    show cz 0c
    mc "Wait... what?"with dis08
    mc "You've never seen the Founder in-person?"
    show cz 0d
    ass "Not even once. Neither I nor anyone from Ulysses' board of directors."with dis08
    ass "It's always memos, emails, or pre-recorded videos, like the ones shown when a Gem of Doom is found."
    ass "Huh! Maybe William knows him in-person, who knows. Perhaps we're not special enough..."
    show cz 0c
    mct "But then, how..."with dis08
    dup "Anyway, are you coming with us, or not?"
    mc "Erm... g-go ahead, I'll stay here for a bit."
    dup "Step aside, then."
    play soundlow doorecho
    show cz 0 with dis17
    mct "None of Ulysses' senior officials have ever seen the Founder? How is that possible...?" with dis12
    mct "That’s inconceivable..."
    mct "Unless..."
    mct "I’ve gotta find Alex. I'll call her with this communicator she gave me."
    mct "But I should find a quiet place. I don't want William Bardot to find me while I'm distracted here."
    stop music2 fadeout 4
    play music fireplace fadein 5
    show cz 1 with Dissolve(2.4)
    mct "Wow, this mansion is huge." with dis08
    mct "Once you leave the main hall, it becomes a labyrinth of corridors and rooms."
    mct "This cellar is very far from the main entrance, so it should be safe to remove my mask."
    play sound chair2
    show cz 2 with dis12
    mc "*Sitting on the stairs* Okay... how does this thing work?" with dissolve
    show cz 3
    mc "Um... hello?" with dis
    mc "Alex?"
    mc "Do I have to keep pressing this button or...?"
    play music night
    play sound beep2b
    show cz 4
    x "No, you only have to press it once."
    x "What do you want now, dumb-dumb?"
    if alexpath:
        x "You can't live without me? Are you missing me already?"
        play music fireplace
        show cz 5
        mc "*Chuckles* Oh yeah, being apart from you for more than 5 minutes is torture."
        play music night
        show cz 4
        x "Don't worry, I'm going back to the mansion now. I managed to clean the... dress. More or less."
    else:
        x "Are you lost or something?"
        play music fireplace
        show cz 5
        mc "*Chuckles* Yeah, it's dark and I'm scared. I need help."
        play music night
        show cz 4
        x "Don't worry, I'm going back to the mansion to rescue you."
    x "Where are you?"
    play music fireplace
    show cz 3
    mc "Go to the end of the east wing of the mansion, on the ground floor. I'm in some kind of cellar, a basement, maybe."
    mc "There's something I wanted to discuss with you in private."
    play music night
    show cz 7
    x "Discuss something in private? That sounds ominous. Any hints about the topic?"
    play music fireplace
    show cz 6
    mc "Well, it's about how we should handle our \"investigation\" for the rest of the night. You know, our questions and the people we talk to."
    mc "I have... a suspicion."
    play music night
    show cz 7
    x "A suspicion?"
    play music fireplace
    show cz 6
    mc "Yes, about this... \"Founder\"."
    mc "Did you know that no one from Ulysses' high-ranking positions has ever seen him?"
    play music night
    show cz 7
    x "Really? Never? How is that possi–"
    show cz 8
    x "Wait a second..."with dissolve
    x "Now that you mention it..."
    x "I remember hearing my father bitching about how he never showed up to any events or meetings, and how that made him a weak leader."
    play music fireplace
    show cz 6
    mc "Exactly!"
    mc "No one has ever seen him in person. No one knows his real name. No one has ever had a real conversation with him face-to-face, either in Eternum or in the real world."
    mc "He can only be seen in those pre-recorded holograms when there's a public announcement."
    mc "All that makes me believe that..."
    play music night
    show cz 8
    x "T-The Founder doesn't exist..."
    play music fireplace
    play sound2 chair3
    show cz 9
    mc "*Standing up* Bingo!"with dissolve
    mc "He's not real! The Founder is just a fucking cover!"
    mc "And whoever is truly pulling the strings just needed a scapegoat. A mask to hide behind!"
    mc "There's no Founder, there's no genius, and there's no messiah!"
    play music night
    show cz 8
    x "B-But..."
    x "He's the most important man in the world. If he doesn't exist... Who created Eternum and most of its servers? Who's in charge of Ulysses right now?"
    play music fireplace
    show cz 9
    mc "That's what we have to find out!"
    show cz 10
    mc "All I know is that..." with dissolve
    play music night
    play sound beep2b
    show cz 11b
    x ". . ."
    show cz 11
    x "What did you say? It got cut off."with dissolve
    show cz 11b
    blank ". . ."with dissolve
    show cz 11
    x "[mc]?"with dissolve
    x "Hellooooo...?"
    show cz 11b
    blank ". . ."with dissolve
    play sound clothes3
    play sound2 beep2b
    show cz 12
    x "(Bah, batteries must have run out.)" with dis12
    x "(I should go find him. He said... east wing? Real specific...)"
    x "(It’s gonna take me ages to find him around here...)"
    stop music fadeout 3
    play musicb fireplace fadein 4
    show cz 13 with Dissolve(3)
    pause
    show cz 14 with Dissolve(2.5)
    pause
    mc "Um..." with dis
    mc "I-Is anything w-wrong...?"
    mc "If t-this is a restricted section of the house, I'm s-sorry, I d-didn't know–"
    $ renpy.music.set_volume(0.3, channel='music3')
    play music3 mystery2 fadein 6
    aaa "I must admit that I am impressed."with dis12
    aaa "Just a little over a month into playing Eternum..."
    aaa "And yet..."
    aaa "You managed to find not one, but two Gems of Doom."
    aaa "You killed two of my Praetorians..."
    show cz 13
    aaa "You found the player who has Dione in her possession..." with dis17
    aaa "And you claimed the third Weapon of Atlas as yours..."
    play sound6 deception
    aaa "Calypso."
    show cz 15
    mc ". . ." with dis
    aaa "I am sorry, where are my manners..."
    aaa "Please, sit down."
    aaa "I have been looking forward to meeting you..."
    play sound6 deception
    aaa "...[mc]."with dis15
    show ending04 with dis2
    play sound2 risingshort6 volume 2
    show cz 16
    pause 6.8
    jump update05

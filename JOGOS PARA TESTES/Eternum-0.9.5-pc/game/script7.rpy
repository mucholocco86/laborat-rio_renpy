label update07:
    $ renpy.music.set_volume(1.0, channel='music')
    $ renpy.music.set_volume(1.0, channel='musicb')
    $ renpy.music.set_volume(0.75, channel='music2')
    $ renpy.music.set_volume(0.75, channel='music2b')
    $ renpy.music.set_volume(0.1, channel='music3')
    $ renpy.music.set_volume(0.6, channel='soundlow')
    scene black with flashfaster
    play music pendulum fadein 6
    pause
    scene f 0 with dis25
    pause
    show edd 7 with dis2
    pause
    mc "Do..."with dis
    mc "Do you know who I am?"
    show edd 8
    will "I am well aware of your shenanigans, [mc]."
    will "I know you've been fooling around with the WRE with your peculiar group of... {i}friends."
    will "I know you attacked that fool Clarence and stole his laptop data in order to ascertain Thanatos' real identity."
    will "And I know you have Calypso... even if you're too stupid to use it properly."
    show edd 7
    mc "“It”?"
    mc "She's not a thing."
    show edd 8
    will "IT is a tool you must use to achieve your goal... same as everyone else."
    will "That foolish, naive mentality of yours is exactly why your progress has come to a screeching halt."
    will "The best thing you could do would be to hand over your Gems to a more skilled veteran player. Someone who actually understands these rules... so you could stop wasting everyone's time."
    show edd 7
    mc "Hah, someone like yourself, for instance?"
    show edd 8
    will "I am not looking for the Gems."
    will "However, since you asked... Thanatos would be a better option."
    will "He'll grab them from your corpse sooner or later, so... why delay it?"
    show edd 7
    mct "Fucking bastard..."
    mc "If you're not looking for the Gems, why do you even care?"
    show edd 8
    will "Because {i}someone{/i} must stop The Founder."
    will "Someone must gather the ten Gems. Anyone but him."
    will "I won't let him destroy everything I've built."
    show edd 7
    mc "The Founder...?"
    mct "Is this what this is all about? A power struggle? Some pathetic dick measuring contest?"
    mc "How are his goals any different from yours?"
    will ". . ."
    show edd 8
    will "Hmm. I suppose whether or not you're aware of the full backstory won't affect your fate."
    show edd 7
    mc "Aware of what backstory?"
    will ". . ."
    show edd 8
    will "What I'm about to tell you could reshape society as we know it today. It could lead to revolt and revolution, anger and incredulity, questions of faith and of life’s grand meaning."
    show edd 7
    mc "Very dramatic."
    show edd 8
    will "I will only say it once, so pay attention. You might learn something to change that bleeding heart of yours."
    show edd 7
    mc "*Sighs* Enlighten me..."
    play sound impact
    scene f1 with flashfast 
    will "The Founder... didn't create Eternum." with dis
    will "He... {i}discovered{/i} it."
    mc "I'm sorry?"
    will "The worlds which form Eternum... the desert lands and magical forests and galactic worlds you prance through... they have {i}always{/i} been there."
    mc "What...?"
    will "In the past, many civilizations had even gleaned sight of it, but those fools believed it to be the afterlife."
    will "They didn’t know what we found out... that even the living were capable of entering Eternum for a short time."
    will "Though, unwillingly, in most cases. Usually accidents, dismissed as dreams or mere delusions."
    will "Some special ones, though... were capable of entering Eternum at will. They were known in Eternum as... the Immortals."
    mct "The Immortals? Could these be the same ones Calypso mentioned?"
    will "The Founder was one of these... {i}chosen ones."
    bla "You remain silent, in an attempt to process what you're hearing."
    scene f2
    will "He was able to synthesize a system that allowed humans lacking this innate capability to access Eternum."with dis2
    will "The key to the system was the neural implant, which allowed the manifestations of astral projections."
    will "He crafted Eternum's inventory system, designed the Exit Portal mechanism, outlined levels, and even established a new commerce system... ostensibly through advanced coding skills."
    will "Yet, no one at even Ulysses has ever seen a hint of a source code."
    will "He ensnared the entire world within an intricate web of deception."
    mct "Astral projections?"
    mct "This shit can't be real..."
    if axelhelp:
        mct "Does this mean that Axel was right...?"
    mc "And so what about the NPCs?"
    will "The souls of the dead, drawn from the pages of human history."
    will "The Founder can manipulate them and bend their will."
    will "Make them dance like puppets."
    mc "So... that's it?"
    mc "He's an almighty GOD? He can do anything he wants?"
    scene f3
    will "He's HUMAN."with dis17
    will "And that's why he needs the Gems."
    mc "I thought he created the Gems of Doom himself."
    will "He did not."
    will "The ten Gems are the very essence of Eternum itself."
    will "They're the beginning... and the end."
    will "They are the conclusion of an order, the perfect and the ultimate. The end of a cycle... and the start of a new one."
    will "The one who gathers them all... will transcend the confines of time and space."
    will "Becoming..."
    play sound deception
    mc "...a god."
    scene f4
    will "The Founder began this quest so people would find the Gems and bring them to him."with dis2
    will "The moment someone does that... it'll be too late."
    mc "But..."
    mc "What about Thanatos? He's... dead."
    will "Not all the NPCs are under The Founder's control. Some continue to live their lives, unaware that they have passed into the realm of the soul."
    will "Others, like Thanatos, are aware of Eternum's true nature and pursue the Gems of Doom for their own purposes."
    will "The Founder is the only man who knows how to harness the power of the Gems of Doom."
    will "That makes him the most dangerous out of anyone in the hunt."
    will "It would mean... our end."
    stop music fadeout 8
    play soundloop rain3 fadein 6
    scene edd 7 with dis25
    mct "What the fuck..." with dis12
    mct "We already knew this was bigger than we thought at first, but... holy fuck, I'm gonna need some time to process all this information."
    mc "How many servers are there, then?"
    show edd 8
    will "There's an uncountably infinite number of them."
    will "But only a handful are controlled by The Founder. If there's no Exit Portal, a common human has no way to access it."
    show edd 7
    mc "But then why–"
    play sound2 dooropen1
    play sound doorsqueak
    x "*Entering the room* Okay, done."
    scene f 6
    mc "Huh...? Alex!" with dis
    show f 5
    x "I signed it."
    x "Now get the fuck out of my house."
    show f 6
    will "Ah... I almost forgot the original reason I came here."
    will "Did you read it all?"
    show f 5
    x "I read enough."
    play sound footsteps
    play sound2 squeak
    show f 7 with dis2
    play soundlow thunder fadein 3
    bla "William rises from his seat and strides towards Alex. She attempts to maintain her composure, but it's clear that she cannot bring herself to meet her father's gaze." with dis
    will "Do you understand all the implications of that document?"
    show f 8
    x "You’ve disowned me. Didn’t take a genius to see that coming."
    show f 7
    will "It's not just that."
    will "From this moment forward, you're no longer a Bardot. You have no tie to us. No property, no riches, no will. You don’t even have the name Bardot anymore."
    will "There will be {b}nothing{/i} linking you to this family."
    will "You're an outcast now."
    will "A pariah."
    will "Do you understand?"
    show f 8
    x "Like I said, disowned. Completely."
    show f 7
    will "Tell me then, will your shitty job cover the costs of your education? Your swimming tutor? Your rent? Healthcare? Another whorish tattoo?"
    x ". . ."
    will "Hmph."
    will "You're such a haughty brat. Always projecting this air of independence and sanctimony... but in the end, that was all just a disguise, eh, Alexandra?"
    will "Still just an arrogant child who knows nothing about how the world works."
    bla "You notice Alex clenching her fist, her shoulders slowly shaking."
    will "You've always been a disappointment, Alexandra."
    will "A burden."
    play sound2 squeak
    play sound chair3
    play sound3 slam volume 0.3
    play soundlow thunder fadein 3
    scene f9tra
    bla "You suddenly stand up, rage consuming you in response to William's hurtful words." with hpunch
    show f 10
    mc ". . ."with dis08
    show f 11
    bla "William's henchmen remain motionless with their hands firmly on their firearms. It is clear that they would be ready to react to even the slightest provocation."
    mct "F-Fuck, I shouldn't do anything stupid..."
    show f 12
    bla "You look at Alex, her eyes quietly imploring your inaction in the face of her father’s verbal abuse."with dis12
    mct "She doesn't want me to get involved."
    will "Anyway... I've already wasted more time here than I would have liked, and this is going to be a very long night."
    show f 13
    will "Farewell, Alexandra." with dis15
    will "This is the last time we'll see each other."
    x "Fuck off."
    will "Do you have any final questions?"
    x ". . ."
    x "Does Mother know about this?"
    will "Know...?"
    will "It was her idea."
    play sound2 footsteps 
    play sound3 footsteps 
    play sound4 doorsqueak
    play sound thunder volume 0.5
    scene f 15 with dis2
    play sound7 doorslam
    bla "William and his men leave the house, leaving Alex standing by the door, her gaze fixed on the floor in solemn silence." with dis 
    mct "What a fucking son of a bitch..."
    mct "He's a total monster."
    mct "I don't even know if I should believe the things he just said to me. He must have some sort of plan."
    mct "Although... if he wanted the Gems for his own use, he wouldn't have revealed himself like this. That wouldn't make sense."
    mct "Might it be that he wants just anyone to gather the ten Gems? Simply to take down The Founder?"
    x "*Sniffs*"
    mct "Fuck, poor Alex."
    mct "I don't even know what to say..."
    mc "Hey..."
    show f 14
    x "I'm sorry you had to see this... again."
    show f 15
    mc "Don't say that!"
    mc "Fuck William. You don–"
    show f 14
    x "I really need to be alone right now."
    x "Thank you for coming, [mc]."
    show f 15
    mc "But..."
    show f 14
    x "I'll see you Monday at school."
    x "If... I'm still allowed to attend after this disownment fiasco. I'll have to look into that."
    scene f 15
    if alexpath:
        menu:
            with dis
            "Leave her alone":
                mc "*Sighs* Okay... I understand."with dis06
                mc "Promise me that if you need someone to talk to, or if you need... anything at all, you'll give me a call."
                show f 20
                x "*Sniffs* Okay, okay, I promise." with dis14
                show f 18
                mct "She was crying..."
                mc "Are you absolutely sure you don't want me to stay?"
                show f 20
                x "Yeees, I'm sure."
                x "You've done enough for today."
                show f 18
                mc "Well, alright... I'll trust your judgment."
                show f 20
                x "And besides... who needs you when I have Dr. Eggdogstein."
                show f 18
                mc "*Laughs* Ah, I knew you liked it!"
                show f 19
                x "I'm starting to believe he's the secret to my quick recovery."
                show f 18
                mc "Told you. He'll protect you against all illnesses."
                show f 19
                x "*Chuckles* Let's hope so."
                x "Thank you for coming, [mc]."
                x "Tonight was... really special. In many ways."
                show f 18
                mc "It was very special to me too."
                mc "Are you su–"
                show f 20
                x "Yes, I am suuure. Now get the fuck out of my house already!"
                show f 19
                x "You can take my umbrella."
                show f 18
                mc "*Chuckles* Okay, okay."
                mc "See you tomorrow, then."
                show f 19
                x "Sure."
                x "Have a good night."
                x "And... thanks again, [mc]."
                x "For everything."
                show f 18
                mc "Don't even mention it."
                mc "Good night, Alex."
            "[gr]Hug her":
                $ alexnotstay07 = True
                play sound2 clothes2
                scene f 16 with dis
                bla "Without uttering a word, you simply grab Alex and pull her into a hug before she has a chance to respond." with dis08
                x ". . ."
                play music2 forgiven fadein 6
                stop soundloop fadeout 12
                $ alex_points += 1
                play sound beat
                show screen heartbeat
                play sound5 clothes3
                scene f 17 
                bla "She slowly encircles her arms around you as tears begin to stream down her cheeks." with dis17
                mc "You don't really have a say in who your parents or family are."
                mc "But you do get to choose your friends."
                mc "And I promise... you'll never be alone again."
                bla "Alex stays silent, her body telling you everything you need to know as she continues to cry on your shoulder."
                x ". . ."
                x "*Sniffing* Mmph!"
                play sound clothes3
                show f 20
                x "*Clears throat* W-Well, that was... a m-moment of weakness. I'm sorry."with dis15
                show f 18
                mc "Don't worry, I won't tell anyone you cried in front of me." with dis06
                mc "I think that makes it the second time, doesn't it?"
                mc "I must be hitting a soft spot with you, admit it."
                show f 19
                x "*Chuckles* Yeah, I guess so."
                x "Or... maybe it's because you always seem to show up when troubles do. You bring bad luck."
                show f 18
                mc "*Chuckles* I can't deny that's also a possibility."
                x "Hmph."
                show f 19
                x "Thank you for everything, [mc]."
                x "Tonight was... really special. In many ways."
                show f 18
                mc "It was very special to me too."
                mc "One that'll be hard to forget."
                mc "Now come on, let's watch some more of those boring swimming competitions so I can fall asleep!"
                show f 19
                x "Hey! They’re not that boring."
                show f 18
                mc "Be real! I saw you starting to snore during that Phelps compilation."
                show f 19
                x "*Chuckles* Fair enough."
                x "But just so you know, tomorrow morning, you're out as soon as the sun peeks over the horizon."
                show f 18
                mc "Sounds like a plan to me!"
                stop music2 fadeout 8
                play soundloop rain3 fadein 6
    else:
        mc "I can–"
        show f 14
        x "[mc]."
        x "Enough."
        x "I... I appreciate it, but I told you I need to be alone. This is not your concern."
        show f 15
        mc "*Sighs* Okay... I understand."
        mc "Take care, Alex. Please."
        mc "Promise me that if you need anything at all you'll give us a call."
        show f 14
        x "I'll be okay. This isn't my first rodeo around Bardot family drama."
        show f 15
        mc "Alright then... goodbye, Alex."
        mct "I hope she'll be okay..."
        mct "But if she needs some time alone, I need to give her that."
        mct "Hopefully she'll feel better tomorrow..."
        jump morning07


label morning07:
    play soundlow thunder fadein 4
    scene eee 50b with dis25
    if not alexnotstay07:
        mct "Oh boy, it's gonna be a long way home..."with dis12
    else:
        x "So... what did my father say to you while I was outside signing that shit?" with dis12
        mc "Oh..."
        mc "You might want to take a seat for this..."
    stop soundloop fadeout 9
    play music happy15 fadein 7
    scene f 21 with Dissolve(3.5)
    show screen afewdayslatercorner
    pause 
    play sound4 doorsqueak
    play sound2 keys
    play sound ["<silence 2>", doorclose2]
    x "I'm back!" with dis12
    play sound5 clothes3
    play sound6 keys
    scene f 22 with dis15
    x "*Leaving her things on the table* Girl, you won't believe this!"with dis 
    x "Ms. Kellegan told me she talked to some folks, and... I can keep training with her!" 
    scene f 23
    x "She said that since I show so much potential, I can continue attending the..."with dis 
    show f 24
    x "Huh?" with dissolve
    show f 25
    x "You're still playing Eternum?!"
    x "I left literally 4 hours ago!"
    show f 26
    x "Well, it’s your loss..."
    x "I bought some handmade chocolate from the store you like!"
    x "I guess I'll have to eat it all on my own!"
    x "Eh??"
    show f 25 
    x "No?"
    d ". . ."
    x "Damn, if food can't wake you up from your slumber, nothing will."
    play soundlow zip
    play sound2 clothes3
    show f 27
    x "*Taking her boots off* I guess I'll have to chill until you're done playing."with dis12
    x "You'd better come back with a new Gem or something at least!"
    play sound3 squeak
    play sound4 chair1
    show f 28
    x "*Lying down next to Dalia* I really shouldn't have let you stay all alone with the Eternum gear around." with dis12
    x "What about our plans for the day?"
    x "You're really lucky you can't hear me right now, or you'd be in for a valuable lesson!"
    show f 29
    x "Hmph."
    show f 28
    x "I'm pampering you, you know? Like, this is special treatment."
    x "I've never let anyone stay at my place alone before. Not even [mc]!"
    if alexpath:
        x "And I..."
        show f 30
        x "I let him do a lot of things that night, believe me." with dis
        show f 30b
        x "(A {i}lot{/i}...)"
        show f 30
        x "But not staying alone in my apartment!"
        x "Not that..."
        show f 30b
        x ". . ."
        play sound squeak
        show f 32
        x "*Whispering* I mean... jeez, can you believe we actually had sex?!"with dis
        x "*Whispering* Because I definitely can't."
        x "*Whispering* That was CRAZY!"
        play sound2 squeak
        show f 30
        x "*Clears throat* Although..."with dis 
        x "Well, that was just... something that happened. That's all."
        x "We're not in a relationship or anything."
        show f 30b
        x ". . ."
        show f 30
        x "However..."
        x "Sometimes, if I imagine him with someone else, I get... kinda... jealous?"
        x "Does that... does that mean something?"
        x "Like... it's not anything serious, but... I don't want to share him either, you know?"
        play sound squeak
        show f 32
        x "Unless I shared him with my best friend, of course..." with dis
        x "Can you imagine? [mc], you, and me... sharing a bottle of booze..."
        x "And then..."
        show f 33
        x "*Snorts* Don't worry, I'm kidding, I'm kidding!"with dissolve
        x "I'm just kidding."
        x "I'm only... messing around."
        show f 34
        x "I should really stop talking to myself."with dis12
        x "One day someone will catch me and they'll think I'm nuts."
        x "Don't say anything, eh, Dalia?"
        scene f34
        d ". . .{w=2.5}{nw}"
        pause .4
    else:
        x "*Chuckles* And that day it was raining like crazy."
        x "I even felt kind of bad."
        play sound squeak
        show f 32
        x "You're all turning me into a big ol’ softie." with dis
        x "With all your kindness, and your selfless acts..."
        x "Lately, I feel like I've been nicer to other people because of you too."
        show f 34
        x "Yep, I don't like that, Dalia."with dis14
        x "*Chuckles* Not one bit..."
        scene f34
        d ". . .{w=2.5}{nw}"
        pause .4

label iondalianancy:
    stop music fadeout 7
    play music2 cyberpunk fadein 6 volume 0.8
    hide screen afewdayslatercorner
    scene f 35 
    with Dissolve(3)
    $ unlock_look("dalia", 12)
    d "Aaah..." with dis
    scene f 36
    d "AAAaaaaahhh..." with dis
    play sound sneeze2
    show f 37
    d "*Sneezes* Ah-choo!" with vpunch 
    d "*Sniffs* Ugh, these fumes are getting up in my nose."
    play soundlow tripod 
    play sound3 transform2
    play sound4 footstep
    play soundloop robotloop volume 0.4
    scene f 38 with hpunch
    pause 0.2
    pur "{sc=2}Potential infection detected.{/sc}"with dis14
    show f38
    pur "{sc=2}For your own safety, please raise your hands and remain still.{/sc}"
    pur "{sc=2}Engaging decontamination protocol.{/sc}" 
    scene f 39b
    d "W-What the fuck is happening?!"with dis
    d "I just sneezed!"
    play sound5 steam2 fadein 3
    show f39
    pur "{sc=2}Please, respond to the following queries.{/sc}" 
    pur "{sc=2}Have you accessed the Andromeda server in the last 36 hours?{/sc}"
    scene f39b
    d "W-What? No!"
    scene f 39
    pur "{sc=2}Have you come into contact with any alien eggs recently?{/sc}"
    scene f 39b
    d "I haven't!"
    scene f39
    pur "{sc=2}Are you currently experiencing nausea or abdominal pain?{/sc}"
    scene f39b
    d "NO!"
    scene f39
    pur "{sc=2}Have you engaged in any sexual activity with someone infected?{/sc}"
    show f39b
    d "W-What?! Of c-course not!"
    d "My goodness, I just sneezed!"
    scene f39
    pur "{sc=2}. . . .{/sc}"
    scene f 39
    pur "{sc=2}Preliminary assessment... inconclusive.{/sc}"with dis12
    pur "{sc=2}Initiating XM-Ray scanning procedure.{/sc}"
    pur "{sc=2}You may experience a slight itching in your cranial region.{/sc}"
    pur "{sc=2}Please remain still.{/sc}"
    play sound transform2
    show f 40
    pause 
    play sound3 xray
    show f41 
    pause 3.6
    play sound5 transform2
    scene f 40
    pause .3
    play sound7 transform2
    play sound2 steam2 fadein 3
    scene f 39
    pause .7
    pur "{sc=2}Scanner complete.{/sc}"with dis
    scene f 39c
    pur "{sc=2}No Xenomorph larvae detected in the subject's thoracic cavity.{/sc}"
    pur "{sc=2}Status: Not infected.{/sc}"
    play sound ding
    play sound3 ding
    stop soundloop
    play sound2 steam2 fadein 3
    show f 42
    pur "We appreciate your cooperation, citizen."
    stop music2 fadeout 5
    play music2b daisy fadein 4 volume 1
    play sound5 robotwalk volume 0.8
    show f 43
    bla "The robot continues its patrol along the street, humming a cheerful tune."with dis15
    d "Jesus, that was close..."
    pur "{bt=2}*Singing* {i}Daaaaaisy, Daaaaaisy...{/bt}"
    pur "{bt=2}*Singing* {i}Give me your answer, dooooo...{/bt}"
    player "*Coughs*"
    stop music2b
    play soundlow tripod
    play sound3 transform2
    play sound4 footstep
    play soundloop robotloop fadein 1 volume 0.45
    scene f 44
    pur "{sc=2}Potential infection detected.{/sc}"with hpunch 
    pur "{sc=2}Engaging decontamination protocol.{/sc}"
    player "W-WHAT?!" with hpunch 
    stop soundloop fadeout 5
    play music2 cyberpunk2 fadein 5
    show f 46
    n "Good lord, what the hell is wrong with these robots?"with dis14
    $ unlock_look("nancy", 9)
    show f 45
    d "I thought I was about to be blasted for a second."
    show f 48
    inf "I know, right?"
    inf "They say the Xenomorph epidemic has gotten out of hand, so Ulysses decided to take drastic measures."
    show f 47
    inf "And instead of releasing a fucking software patch, they deployed these damn robots everywhere to ruin all the fun and scare away my customers."with dis
    inf "FUCK YOU, PIGS!"
    show f 48
    inf "But anyway, what were we talking about?"with dis
    show f 45
    d "El Coyote."
    d "You mentioned that you knew where his base was hidden."
    show f 48
    inf "Ah, yeah..."
    inf "Emphasis on {i}was{/i} hidden, I guess."
    inf "Now he’s probably moved on to one of the hundreds of abandoned warehouses you can find throughout Ion. Sorry."
    inf "The guy's a touch paranoid when it comes to staying hidden."
    show f 49
    n "Agh, so the reports were right... we're too late."
    show f 48
    inf "Yeah, apparently he arrived two days ago very agitated and demanded everybody pack up and leave."
    show f 51
    n "Damn it... he's slipped through our fingers again."
    show f 49
    n "Any idea about where he could have gone?"with dis 
    show f 50
    inf "No clue. People used to say he frequented Frontier Trails, so maybe you'll get lucky looking there."
    show f 49
    n "Nah... we've been there already. And I doubt he'd return."
    show f 51
    n "Dammit... he keeps eluding us." with dis
    n "Bastard."
    show f 45b
    d "He's running out of places to hide, though."
    d "It's gotta be The New World."
    show f 49
    n "Yeah... I was waiting to gather some info before heading there personally."
    n "I sent some men to explore the area in advance."
    show f 52
    inf "Welp, I guess my job here is done."
    inf "And now that that's settled..."
    inf "Hear me out: CIRCUIT EDGE. The ultimate nightclub in all of Ion! Music, cool people, and the best Braindances you'll ever see!"
    inf "Two free drinks each! I've got coupons!"
    inf "What do you say?"
    show f 49
    n "Um... I can't, I'm busy today."
    show f 53
    inf "Aghh... come on, after being a WRE informant for so long?"
    inf "I work on commission, lend me a hand!"
    show f 49
    n "I'm sorry, maybe another day."
    show f 53
    inf "I'll take your word for it..."
    show f 54
    inf "What about your sister? You up, cutie?" with dis
    inf "You'll have fun, I promise!"
    show f 45b
    d "Nah, I'm sorry, I also–"
    show f 45
    d "Hold up a second... w-what did you just say?"
    show f 52
    inf "Yep, TWO free drinks!"
    show f 55
    d "Not that!"
    d "Do you... do you think we're sisters?!"
    show f 54
    inf "Oh... are you not?"
    inf "My bad, it's just that you two look a lot alike."
    show f 55
    d "We look alike because we're family, but NOT sisters!"with hpunch
    d "How old do you think we are?!"
    show f 53
    inf "Ehh..."
    inf "Well, if I had to guess, I'd say she's... 28? 29?"
    show f 56
    n "Oh please, stop it!"
    n "You should see me without makeup on..."
    show f 54
    inf "And you look like..."
    inf "23?"
    show f 55
    d "WHAT?!" with hpunch
    d "You think there's only a 5-year difference between us?!"
    show f 54
    inf "Younger?"
    inf "Sorry, I'm not good at this."
    inf "I think it's the jacket, it makes you look o–"
    play soundlow zip
    play sound ["<silence 0.4>", clothes2]
    show f 57
    bla "Dalia takes off her jacket and tosses it to the ground." with dis
    show f 54
    inf "Uh..."
    show f 57
    inf "Mmm..."
    show f 54
    inf "Um..."
    inf "...22?"
    show f 58
    d ". . ."
    inf "No?"
    inf "21...?"
    d "{bt=3}*Gritting her teeth* MMMmmmmmhhh...{/bt}"
    show f 49
    n "*Clears throat* Anyway, thank you for your help." with dis
    show f 50
    inf "Anything for the WRE."
    inf "Tell the Empress I helped you!"
    show f 49
    n "Yeah, will do... thank you."
    show f 59
    n "Okay, we're almost done here, Dalia." with dis14
    n "I'm gonna investigate that warehouse before logging off, I wanna see if I can find any clues about Coyote."
    n "I know you had plans with Alex, so feel free to log off, no worries."
    show f 60
    d "Mm-hm."
    n ". . ."
    show f 61
    n "Are you okay?"
    show f 60
    d "Hmm."
    show f 61
    n "You sure?"
    show f 60
    d "Hmm."
    if daliapath:
        play sound whoosh6
        play soundlow debris3
        scene f60
        n "Aaaahhh... I know what's going on."
        n "It's because of a boy, isn't it?"
        scene f 63
        d "What?"with dis08
        d "W-Where did that come from?"
        d "I don't even know what you're talking about."
        show f 64
        n "You've never cared about what others think of you, let alone some random informant."with dis
        n "But something's changed lately..."
        n "A mother notices these things."
        show f 65
        d "Stop it. You’re talking nonsense, Mom."
        show f 64
        n "Ah, young love... my little princesses grew up too fast!"
        show f 65
        d "I told you to stop making things up."
        show f 64
        n "So there's no secret boyfriend you're trying to keep from me?"
        show f 65
        d "Of course not."
        show f 64
        n "Nothing serious, then? A no-strings-attached relationship?"
        n "Just sex?"
        show f 66
        d "Mom! Please!"with hpunch
        show f 68
        n "Make sure he uses protection!"
        show f 67
        n "Or if you'd like, I can go with you to the pharmacy to get some birth control pills! I’m sure old Ms. Shirley at the pharmacy would be discreet!"
        show f 66
        d "NO! D-Don’t tell Ms. Shirley! I... o-oh my god, can we stop talking about this, please?! You’re embarrassing me!"
        show f 67
        n "You can talk to your mommy about these things, darling, it's perfectly natural."
        show f 66
        d "I do NOT want to talk about these things."
        show f 67
        n "That's okay hun, I'll meet him whenever you're ready. We’ll go at your pace."
        n "I’m sure things are steamy and physical now, but when things calm down, I’ll be there for you!"
        show f 66
        d "I TOLD YOU I'M NOT SLEEPING WITH ANYONE!"
        d "So please, STOP TALKING ABOUT IT!"
        show f 67
        n "Oh... so there's someone, but you're not {i}there{/i} yet. Is that it?"
        show f 66
        d "It's not like..."
        d "I..."
        d "He..."
        show f 64
        n "I see..." with dis 
        n "Don't worry, I won't push further."
        n "I just want you to know you can talk to me whenever you want."
        n "About anything."
        show f 65
        d "A-Alright."
        show f 64
        n "And I won't breathe a word to anyone, rest assured."
        show f 64b
        d "Hmm."
        show f 65
        d "Not even Penny."
        show f 64
        n "My lips are sealed!"
        show f 64b
        n "Mmmh?"
        d "Hmmm."
    else:
        n ". . ."

label pennymall:
    stop music2 fadeout 7
    if penelopepath:
        scene f 69 with Dissolve(3.1)
        play music happy16 fadein 8
        p "Mmmmh..." with dis
        $ unlock_look("penelope", 14)
        p "*Scrolling through her Instagram feed* ([mc] still hasn't liked my latest pic...)"
        show f 71
        p "(Although... well, I guess we've all been crazy busy lately.)"with dis14
        p "(I've barely had time for any modeling stuff myself. Just college and Eternum.)"
        show f 70
        p "(Yeah, he probably just missed it.)"
        p "Hmm."
        p ". . ."
        p "(He used to be on top of liking my pics, though. I remember he even had post notifications on...)"
        p "(Did something... happen?)"
        p "(Is he mad at me? Did I say something, maybe...?)"
        p "Hmm..."
        show f 71
        p "(Bah, I'm totally overthinking this.)"
        p "(You seriously can't let this nonsense get to you, Penny. Don't be in your head.)"
        p "(He probably just didn’t see it, that's all.)"
        show f 70
        p "Mm-hm."
        p "(Yeah.)"
        p ". . ."
        p "(Maybe it's because of the pants I'm wearing in this pic?)"
        p "(Now that I look at them... they do make my hips look kinda weird.)"
        lil "Penny!"
        p "(Are those hip dips...? Or is it the angle?)"
        lil "PENNY!"
        p "(Do I even have hip dips?? Since when?)"
        play sound3 slap1
        play sound4 slap1
        show f 71b
        lil "*Clapping her hands* PENNY!!!" with hpunch 
        show f 72
        p "W-What, what?! Jeez, don't shout!"with dis06
        show f 73
        lil "Marco’s got some goodies to spill!"with dis
        show f 75
        p "Oh, y-yeah, the surprise he mentioned."
        p "I'm all ears."
        show f 74
        mar "Okay... remember when we said we deserved a good long break after last week's media law test?"
        show f 73
        lil "Ugh, don't even remind me! That was so brutal!"
        show f 75
        p "Yeah..."
        p "(Was it? I pulled an A without sweating it much.)"
        p "...it was a tough one. Thank goodness I put in some serious study time."
        show f 74
        mar "Well... me and Sebastian have been secretly plotting a little surprise."
        mar "We're throwing a party tomorrow..." 
        mar "AT HIS PARENTS’ HOUSE!"with hpunch 
        play music2b party3 fadein 13
        stop music fadeout 10
        show f 77
        lil "*Gasps* No way! At Sebastian's place?!"with dis12
        show f 78
        p "The chalet?! Really?"
        p "How did he manage to pull that off?"
        show f 76
        mar "His parents are both out of town until next Monday."
        mar "So Sebs and I put our heads together to plan the bash of the year."
        mar "We're even bringing in our very own DJ!"
        show f 77
        lil "*Gasps* Our own DJ?!"with hpunch 
        mar "And a pool..."
        lil "A POOL?!"with hpunch 
        show f 76
        mar "Unlimited bar..."
        show f 78
        p "No way!"with hpunch 
        show f 76
        mar "A huge dance floor with music blaring..."
        scene f78
        p "Whoa!{w=3}{nw}"with hpunch 
        scene f76
        mar "It’s gonna be a full-out spectacle!{w=3}{nw}"with hpunch 
        scene f78b
        p "You're kidding!{w=3}{nw}"with hpunch 
        scene f76b
        mar "We've invited people from all over the state!{w=3}{nw}"with hpunch 
        scene f78bb
        p "Oh my!{w=3}{nw}"with hpunch 
        scene f76
        mar "And there will be plenty of spare rooms in case anyone wants to... sleep over...{w=3}{nw}"with hpunch 
        scene f79
        p "OH MY GOD!{w=3}{nw}"with hpunch 
        play sound2 pop
        stop music2b
        play music happy16 fadein 4
        scene f 80
        p "Ahh, I wish I could make it!"
        p "Promise you'll send me lots of videos!"
        show f 76
        mar "There will also be–"
        show f 81
        mar "W-Wait, what? You're not coming?"with dis08
        show f 80
        p "Tomorrow, right? Nah, I have some other things to do, sorry."
        p "Next time!"
        show f 86
        lil "WHAT?! B-But this is THE party of the year! You HAVE to be there!"
        show f 83
        p "I'm sorry, I just... have better plans."
        show f 86
        lil "Better? What could possibly be better than this?!"
        show f 82
        p "Uhh... well, there are quite a few things that come to mind."
        p "But... to be honest, I just don’t feel like partying anymore."
        p "Didn't we just have that costume party not too long ago?"
        show f 86
        lil "The Halloween one? That was over a month ago!"
        show f 84
        p "Really? Damn, it feels like yesterday..."with dis
        p "*Sighs* I guess my partying days are already behind me."
        p "*Melancholy tone* We're not 20 anymore, Lily..."
        show f 85
        lil "We're literally 21!"
        show f 83
        p "Well, either way, I can't make it. I swear."with dis 
        p "Today I'm playing Eternum until... midnight, probably."
        p "Tomorrow evening, I managed to get an appointment at the Photo Studio with [mc]. I haven’t done any modeling in forever, I need to get back into it."
        p "And after that... I'm meeting up with Alex and my sister to play again."
        show f 86
        lil "WHAT?! Pause. Eternum?!"
        lil "You too?? Are you serious?"
        show f 82
        p "Yes...?"
        show f 86
        lil "That's like... so... nerdy."
        show f 82
        p "It's not nerdy."
        show f 86
        lil "It is!"
        show f 82
        p "Are you calling 80%% of the campus a nerd?"
        p "Because everyone there plays it."
        show f 86
        lil "You're like my brother! And he's definitely a total nerd!"
        show f 82
        p "You're just saying that because you haven't given it a try."
        p "And besides..."
        show f 84
        p "Who gives a shit? We’re in COLLEGE. We’re ADULTS. Who cares what others say?" with dis
        p "If playing Eternum makes me a nerd or whatever, so be it."
        p "It's not like it's gonna make me stop anyway."
        play sound chair2
        play sound2 bags
        show f 87
        bla "Penelope grabs her shopping bags and stands up, catching the attention of everyone around her in the mall."with dis12
        p "Anyways, I've gotta go!"
        show f 88
        p "It was fun hanging out with you guys!" with dis08
        p "See you around campus tomorrow!"
        lil "S-Sure, bye Penny."
        show f 89 with dis17
        lil "Hah! Can you believe it?"with dis06
        lil "Penelope Carter plays Eternum!"
        show f 90
        mar "I mean... didn't she mention it before?"
        mar "When we asked her about her Lady of Eternum costume?"
        mar "And... several times after that?"
        show f 91
        lil "Well, yeah, but I thought she was joking."
        lil "Do you think this is why we've been seeing her less these past few weeks?"
        show f 90
        mar "I guess so."
        mar "They say it can be quite addicting."
        mar "Ulysses even opened a store in this mall just a few weeks ago."
        mar "Honestly... I was thinking about getting an implant myself just to see what all the fuss is about."
        show f 91
        lil "Huh."
        lil "Might even be worth it."
        lil "I mean... if Penelope plays it too, it's gotta be {i}at least{/i} worth checking out... right?"
        lil "I might swing by that store one of these days too."
        show f 90
        mar "Yeah... me too. Perhaps."
        show f 92
        lil "Hmm."
        mar "Mmmh."
        lil ". . ."
        mar ". . ."
        show f 90
        mar "Wanna go now?"
        show f 93
        lil "YES!"

label novaprepare:
    if novapath:
        stop music fadeout 7
        scene f 94 with Dissolve(3.1)
        play music2 happy4 fadein 8
        no "*Taking a deep breath* . . ." with dis
        $ unlock_look("nova", 12)
        show f 95
        no "*Exhaling* Fuuu...."with dis14
        show f 96
        no "O-Okay, I'm honestly a bit nervous, but..."with dissolve
        no "I-I need to get this off my chest."
        no "I c-can't hold it in any longer."
        show f 97
        no "*Nervous chuckle* I know that we met in quite a bizarre situation, and..." with dis12
        show f 98
        no "W-Well, a lot has happened since then."
        no "We've been thrust into tons of even stranger situations."
        show f 97
        no "Like..."
        show f 98
        no "I mean..."
        no "We've actually done... more than we probably should have done. Always... forced by some external circumstance."
        no "So I don't really know if you feel the same way towards..."
        show f 97
        no "I mean, some time ago, I started to see you like..."
        show f 98
        no "*Clears throat* I guess that w-what I'm trying to say is that..."
        no "I invited you here today because..."
        show f 97
        no "I... I want to be with you."
        no "I want to take our relationship to the next level."
        no "I... I want you."
        show f 98
        no "God, no, that sounds so cringy."
        show f 97
        no "I like you."
        no "I like you a lot."
        no "I want to–"
        play sound knock4
        san "*Knocking on the door* Nova? Is your friend already here? Or are you talking alone again?"
        show f 99
        no "T-There's no one, Mom!"with dis
        no "I'm just... singing!"
        show f 100
        san "It's okay, honey, he doesn't need to hide!"
        show f 99
        no "I-I told you he's coming on Saturday, not today!"
        show f 100
        san "Oh, right!"
        san "I'll prepare some food!"
        show f 99
        no "I'll handle the food myself!"
        show f 100
        san "Oh, okay. Then I'll take your father for a walk so you can have some time alone, don't worry."
        san2 "*From the living room* What?!"
        san2 "*From the living room* No chance, I'm staying here. And I want that door open at all times, Nova!"
        san "Shut up, Rory!"with hpunch
        san "I'll stop bothering, sweetie. Keep singing!"
        no "Mm-hm."
        show f 101 with dis14
        no "*Kneeling down* (Tsk, when will they stop treating me like a kid?!)"with dis08
        play sound switch
        show f 102
        no "*Turning on the light* (I'm not a child anymore...)" 
        play sound2 chair1
        play sound3 squeak
        show f 104 with dis12
        no "*Sighs* This date with [mc] has to be PERFECT, Pochita." with dis06 
        no "Perfect!"
        show f 103
        no "*Deep exhale* . . ."
        no "(Okay, mental rundown of the plan.)"
        no "([mc] arrives as arranged.)"
        no "(We enjoy some pirate-themed snacks, like a shot of rum and those Devil Fruits I ordered online.)"
        no "(Afterwards, we log into Eternum, teaming up with Nancy on The New World server to really get into the pirate mood.)"
        no "(We log off, and I present him with a manga drawing in the style of One Piece, followed by us enjoying some of the best anime moments together.)"
        no "(And to cap it off, we watch the final episode LIVE... snuggled up together.)"
        play sound clothes3
        play sound2 squeak
        show f 105
        no "*Giggles* (And after that... we'll see. Netflix and chill.)" with dis12
        no "Mmmh."
        no "(Sounds like a solid plan.)"
        no "(I swear, if {i}anything{/i} goes wrong, I'm gonna die.)"
        no "(I've gotta make sure I don't forget anything.)"
        no "(The snacks, the drinks, the Eternum suit, the video recaps, the–)"
        play sound chair1
        play sound2 whoosh3b
        scene fdrama1
        no "NO."with vpunch
        no "*Looking at her desk* THEY'RE NOT THERE!"with vpunch
        play sound chair1
        play sound2 whoosh3b
        scene fdrama2
        no "FUCK, FUCK, FUCK!" with vpunch 
        no "*Hyperventilating* I left my drawing utensils at the Carter house last time I was there!"
        no "*Hyperventilating* How am I supposed to draw without them?!"
        no "*Hyperventilating* NO, NO, NO... MY DATE IS RUINED!"with hpunch 
        no "*Hyperventilating* I..."
        scene f 108
        no "W-Wait, I'm supposed to meet Annie for coffee at the cafe in half an hour." with dis
        no "Maybe she's still at home, and she can bring them to me."
        no "This way I could still start drawing tonight as I planned."
        play soundloop phone2 fadein 1
        scene f 109
        no "Come on, pick up, please, pick up..."with dis15
        no ". . ."
        no "*Hyperventilating* Come on..."
        stop soundloop 
        play sound w1
        play sound2 beep2
        scene f 109b
        a "Hi!" with pl
        $ unlock_look("annie", 11)
        play sound w1
        scene f 110
        no "Annie, thank goodness!" with pr
        no "Listen, are you still at home?!"
        no "Last time I was there I forgot–"
        play sound w1
        scene f 109b
        a "Your drawing utensils?"with pl
        a "No worries, I'm already at the bus stop, but I have them with me."
        a "I can give them to you at the cafe when we see each other in a bit."
        play sound w1
        scene f 111
        no "*Regaining a normal pulse rate* Oh my god..."with pr
        no "You're the absolute best, thank you so much."
        no "(Phew, I almost had a heart attack. I haven’t been so nervous about something since I lost my laptop...)"
        play sound w1
        scene f 112b
        a "Are you okay?" with pl
        a "You sound agitated."
        play sound w1
        scene f 112
        no "Yeah, I'm fine!"with pr
        no "It's just that I needed them to... um... draw something for my mother."
        no "It's her birthday soon, and I've planned an entire day with her. I want everything to be perfect."
        no "Looking back at it, I was probably overreacting, but... you know."
        no "I guess I can be a bit neurotic sometimes."
        play sound w1
        scene f 109b
        a "Oh, that's nice!" with pl
        a "And I can understand, I'm a perfectionist too."
        a "I need all the details to be perfect."
        play sound w1
        scene f 112
        no "Exactly!"with pr
        no "I need it to be ready before this Saturday. I wanna draw something in the style of One Piece."
        no "You know, because of the final episode."
        play sound w1
        scene f 112b
        a "This Saturday?"with pl
        a "You didn't hear?"
        play sound w1
        scene f 112
        no "Hear?"with pr
        play sound w1
        scene f 112b
        a "The animation studio went on strike for better worker rights, demanding bathroom breaks, an extra vacation day, regular family visits, and only 12-hour work days!"with pl
        a "Looks like the episode will be delayed in the meantime."
        play sound w1
        scene f 112
        no "De...layed?"with pr
        a "Yeah, the finale will be delayed by a couple of weeks, at least! So you’ll have plenty of time to work on–"
        no "A couple of–"
        stop music2
        play sound impact
        play sound2 impact
        scene f 113
        pause .1
        scene f 114 with dis12
        play soundlow dramaphonemusic fadein 3
        pause 0.5
        scene novadrama with dis15
        pause 6.4
        play sound4 dramaphonesound
        pause 7.3
        stop soundlow
        stop sound4
        play music happy16
        play sound5 busyphone volume 0.7
        scene f 115
        a ". . ."
        show f 116
        a "(She hung up?)" with dis12
    else:
        play music happy16 fadein 14

label cafe07:
    stop sound5 fadeout 2
    scene ff 1 with Dissolve(3.2)
    mc "*Stretching* Mmmm..."with dis12
    mc "(If the barista takes much longer, we won’t have any time for our drinks.)"
    mc "(We're supposed to meet Penny in Ekabar in about an hour.)"
    if penelopepath:
        play sound vibration
        play sound2 vibration
        bla "Your phone buzzes."
        mc "(Ah, right on cue!)"
        call chat(penelope_chat3) from _call_chat_15
        mct "I'm pumped to check out that mysterious town." with dis08
    mct "Although... I don't know much about what's going on there, I only heard about it yesterday."
    mct "I should ask Luna for the deets before we all log in."
    play sound saloondoors fadein 1
    play sound7 storebell
    show ff 2 with dis12 
    clerk "Hi cutie!" with dissolve
    clerk "I'm sorry for the wait, my partner couldn't make it to work today, so it's just me."
    clerk "What can I get you?"
    play sound chair2
    show ff 4
    mc "*Standing up* No worries, I just got here."with dis12
    show ff 3
    clerk "Well, if I knew a handsome fellow like you was waiting for me, I'd have hurried out sooner!"
    show ff 4
    mc "*Chuckles* You always compliment me to try to get me to spend more money, Ruth."
    show ff 3
    clerk "Oh, come on now! It's a heartfelt compliment!"
    show ff 4
    mc "*Chuckles* Whatever."
    mc "In any case, I'm actually not alone this time. I came with the brunette outside."
    show ff 5
    clerk "Oh, really...? Hah, that makes sense."
    clerk "I saw her before, she looks like a doll."
    clerk "It's a bit unfair when all you pretty people gather in one place, you know?"
    show ff 4
    mc "*Chuckles* You can stop the flattery, I'm ordering something anyway."
    show ff 3
    clerk "Ah, you're in luck then, because we have an offer for pretty couples today."
    clerk "Two drinks and fresh croissants for only $19.95."
    show ff 4
    mc "$20?!"
    mct "And that's supposed to be a deal?"
    show ff 3
    clerk "You won't regret it."
    show ff 4
    mc "Jeez, I hope not..."
    show ff 3
    clerk "So, what'll it be?"
    clerk "Coffee, tea, or hot chocolate?"
    show ff 4
    mc "I'll have a... coffee. With milk."
    show ff 3
    clerk "And for your little angel outside?"
    show ff 4
    if lunapath:
        mc "Hmm..."
        mct "What will Luna want?"
        menu:
            with dis
            "Coffee":
                mc "Another coffee." with dissolve
            "Tea":
                mc "A tea."with dissolve
                $ lunadrinkcafe += 1
            "Hot chocolate [luna_pts]":
                mc "Hot chocolate."with dissolve
                $ lunadrinkcafe += 2
    else:
        mc "Um... I don't know, another coffee, I guess?"
    show screen eternals
    with dis
    play sound coins
    $ money -= 7
    pause .05
    $ money -= 7
    pause .05
    $ money -= 6
    pause .3
    show ff 3
    hide screen eternals
    clerk "Coming right up!" with dis06 
    show ff 4
    mc "Thanks!" 
    mc "I'll take it myself to the table, no worries."
    if money < 0:
            mct "Shit, I'm still overdrawn. Ulysses sent me an email telling me I have 14 days to fix this or I'll be banned."
            mct "I've gotta be careful."
    play sound5 doorsliding
    scene ff 6 with dis2
    mc "*Sitting down* Sorry for the delay!"with dis08
    $ unlock_look("luna", 10)
    if lunapath:
        mct "Man, the clerk was actually right. She really does look like an angel with this light."
    mc "I grabbed us a little something to eat before leaving."
    show ff 7
    l "You didn't have to."
    show ff 6
    mc "Nonsense."
    show ff 8
    if lunadrinkcafe == 0:
        mc "There's a couple of croissants for each of us, and I wasn't sure of what drink you wanted, so I got you a cup of coffee."
    elif lunadrinkcafe == 1:
        mc "There's a couple of croissants for each of us, and I wasn't sure of what drink you wanted, so I got you some hot tea."
    else:
        mc "There's a couple of croissants for each of us, and I wasn't sure of what drink you wanted, so I got you a cup of hot chocolate."
    mc "Is that okay?"
    if lunadrinkcafe <= 1:
        l ". . ."
        show ff 7
        l "It's perfect! Thank you so much."
        play sound sip
        show ff 6
        mc "*Taking a sip of your coffee* Don't mention it!"
        l ". . ."
        show ff 6
        mc "You're not drinking?"
        show ff 7
        l "I will... in a minute."
        l "It seems to be scalding hot, I don't wanna burn my tongue."
        show ff 6
        mc "Ah, that makes sense."
    else:
        play sound whoosh6
        play sound2 ceramic
        show ff 9
        bla "Luna snatches her cup with lightning speed and takes a deep whiff."with hpunch
        mc "*Chuckles* I'll take that as a yes."
        play sound3 sip
        l "*Taking a sip* I love chocolate."
        mc "I had a feeling you did."
        mc "You strike me as a chocolate girl."
        show ff 10
        l "I don't even like coffee or tea that much, actually."
        mc "Really?"
        l "Yeah, I know it's kinda odd, considering my dad runs a cafe."
        l "But... I don't know, they're just too bitter for my taste."
        l "Unless I add a lot of sugar."
        mc "Guess I made the right choice then."
        play sound4 sip
        show ff 9
        l "*Taking another sip* You did."
        $ luna_points += 1
        play sound5 beat
        show screen heartbeat
        show ff 10
        l "Thank you, [mc]."
        mc "Please, don't even mention it."
    mc "*Looking at her book* Oh, I forgot to ask you earlier, what are you reading?"
    if lunadrinkcafe == 2:
        play sound cup 
    show ff 11
    l "Oh... it's just some old mystery novel I found in my attic." with dis14
    show ff 13
    mc "What's the story about?"
    show ff 12
    l "Um..."
    l "It's essentially about a girl who inherits an old house in a remote town, and... things happen."
    show ff 11
    l "It has its share of eerie and mysterious moments."
    show ff 13
    menu:
        with dis
        "Is that all?":
            mc "Is that all? It sounds pretty cliche, to be honest."with dissolve 
            show ff 12
            l "I guess the premise does sound basic, but there are definitely some intriguing twists and turns later on."
            show ff 16
            if not lunapath:
                show ff 16b
            l "It might not revolutionize anything, but I have a fondness for horror stories." with dis15
        "Cool":
            mc "Cool. Enjoy it!"with dissolve 
            show ff 16
            if not lunapath:
                show ff 16b
            l "Thanks! I definitely will." with dis15
            l "I have a fondness for horror stories."
        "Tell me more [luna_pts]":
            mc "You can't stop there! Tell me more!"with dissolve 
            show ff 12
            l "I didn't want to bore you with it."
            show ff 13
            mc "Nonsense! You could never bore me."
            show ff 11
            l "Well... if you insist..."
            if lunapath:
                $ luna_points += 1
                play sound5 beat
                show screen heartbeat
            l "Okay then!"
            l "It tells the story of a girl called Ivy."
            show ff 12
            l "After the death of her grandmother, she inherits an old house and travels to a remote town to assess the value of the land before selling it."
            show ff 13
            mc "Mm-hm."
            show ff 12
            l "The once-grand manor is eerily preserved, but there's something that quickly disturbs her..."
            stop music fadeout 8
            play musicb lu fadein 7
            scene ff14
            l "Its halls are populated by a haunting congregation of lifelike, grotesque statues, all carved from obsidian stone." with dis3
            l "They depict twisted scenes of suffering and despair, each one more macabre than the last."
            l "As Ivy explores the mansion, the statues' expressions seem to shift, their sinister grins deepening, their eyes becoming harrowed."
            l "One night, while following faint whispers that reverberate through the corridors, she stumbles upon a statue that disturbingly resembles her dead grandmother, etched in agonized detail."
            l "Reaching her limit, Ivy quickly packs her things and races towards the small town nestled near the station, only to find..."
            play sound2 swallow
            mc "*Gulps*"
            l "More statues."
            l "Standing sentinels in every corner. On every bench. In every window."
            l "There's not a living soul in the town."
            l "She begins to retreat, panicked, when suddenly, someone... or something grabs her shoulder and whispers in her ear..."
            mc "W-What does it whisper...?"
            play sound pop
            stop musicb
            play music happy16           
            scene ff 16
            if not lunapath:
                show ff 16b
            l "That would be a spoiler!"
            l "I only described the first 3 chapters of the book."
            show ff 15
            if not lunapath:
                show ff 15b
            mc "H-Holy shit... that was scary, but so cool at the same time! You have such a way with words, Luna."
            mc "I need to know what comes next."
            show ff 16
            if not lunapath:
                show ff 16b
            l "I can lend you the book after I'm done, if you want."
            l "There are tons of them at home – I have a fondness for horror stories."
    show ff 15
    if not lunapath:
        show ff 15b
    mc "I like them too, although I'll admit that I don't read anymore."
    show ff 16
    if not lunapath:
        show ff 16b
    l "I’m the same, between Eternum and the constant lure of our phones and PCs, I just don’t have time to read."
    l "I'm trying to make it a habit to read at least one book every month."
    if not lunapath:
        show ff 15b
        mc "That's a very good decision!"
        play sound5 doorsliding
    else:
        show ff 15
        mc "That's a very good de–"
        mc "Wait a second... your hands!"
        mc "You're not wearing your gloves!"
        show ff 17
        l "*Dropping the croissant* Oh... yeah, I know."with dis
        l "It's just you and me here, so... I felt... comfortable enough to take them off."
        show ff 18
        mc "Ah, I'm so glad to hear that!"
        mc "I want you to feel safe when you're with me."
        show ff 19
        l "*Looking at her hand* I don't want to carry shame for what my hands do anymore."with dis12
        l "I don't want to be afraid of myself."
        menu:
            with dis
            "[gr]Grab her hand":
                $ lunagrabhand07 = True
                show ff 20
            "Don't grab her hand":
                mc "You have no reason to be."with dis06 
                show ff 23
                mc "This power of yours, we'll learn to control it together."with dis
                mc "We'll all be there for you. You don't have to fear it anymore."
                show ff 23b
                l "Thank you, [mc]."
                l "I... I do feel safe when I'm with you."
                l "I..."
                play sound doorsliding
                show ff 24
                a "Oh, and add a couple of cookies too, please!" with dis15
                jump cafeannieluna
        mc "*Gently grabbing her hand* You have no reason to be."with dis 
        show ff 21
        bla "Luna struggles to maintain her composure, her body trembling slightly at your touch."with dis 
        mc "This power of yours, we'll learn to control it together."
        mc "We'll all be there for you. You don't have to fear it anymore."
        mc "Your visions could even help us on our quest!"
        l "Hmph."
        show ff 22
        l "But... what if I foresee bad things?"
        show ff 21
        mc "Then we'll try our best to prevent whatever you saw. You can warn us!"
        show ff 22
        l "It can't be avoided. Whatever I see... it will happen."
        show ff 21
        mc "It {i}may{/i} happen. But our destinies are not written in stone anywhere."
        show ff 22
        l "But you don’t get it... the things I see... they always come to pass."
        show ff 21
        mc "You also believed that you {i}always{/i} had visions of the future when touching anyone with your bare hands."
        mc "Yet, when you touched me... nothing happened."
        mc "That was a first. Why would this be any different?"
        l "Hmm."
        show ff 23b
        l "You're right, that {i}did{/i} happen... I guess you have a point."
        show ff 23
        mc "Don't worry, Luna."
        mc "I'll always be there for you."
        $ luna_points += 1
        play sound5 beat
        show screen heartbeat
        l ". . ."
        show ff 23b
        l "I..."
        play sound doorsliding
        show ff 24
        a "Oh, and add a couple of cookies too, please!" with dis15
label cafeannieluna:
    scene ff 25 with dis14
    a "Hi guys!"with dis06
    if not novapath:
        $ unlock_look("annie", 11)
    show ff 26
    if lunapath:
        l "A-Annie! So good to see you!"with dis
        mct "I guess she's not ready to share her secret with anyone else for now."
        mct "Part of me wishes she would, but I can't deny that it makes me feel somewhat special."
    else:
        l "Annie! I didn't know you were coming."with dis
    show ff 25
    a "I'm meeting up with Nova here in a minute, but since I knew you guys were here, I decided to arrive a couple of minutes early to say hi."
    a "And let me say, I LOVE your top!"
    show ff 26
    l "Thank you!"
    l "Penny picked it out for me when we went to the mall the other day."
    play sound chair2
    show ff 27
    a "*Sitting down* Ah, you couldn't have a better stylist than her! That color looks absolutely stunning on you."with dis12
    show ff 28
    mc "Well, I don’t want to be the only one without a compliment, but I have to say, I absolutely love your hair, Annie."
    if anniepath:
        mc "Those braids are..."
        mci "(Imagine getting Annie on all fours and pulling her from those...)"
        mc "T-Those braids are adorable."
        mct "[mc], don't you start..."
        show ff 29
        a "Thank you, [mc]..."with dis06
    else:
        show ff 27
        a "Thanks, I like it too."
    show ff 30
    l "Now I feel kind of bad for having to leave."
    show ff 27
    a "Don't be! Nova is going to be here any minute now, so no worries."
    a "And besides, I already knew you were about to leave."
    a "You're going to Ekabar, right?"
    show ff 30
    l "Yeah, Penny, [mc], and I. We're going to a small village called Hollowbrook, where there have been reports of NPCs going rogue."
    show ff 31
    mc "Rogue how? What do we know about it?"
    show ff 32
    l "Only that some villagers have been acting strangely lately."
    l "Apparently, they've suddenly started hunting down anyone, be it a player or another NPC, who uses magic, claiming it's the work of the devil."
    l "There have even been reports of them burning people alive, accusing them of vampirism or witchcraft."
    show ff 31
    mc "Hmm, it's oddly fitting for a medieval server, isn't it?"
    show ff 34
    a "It might be, but that's not the expected behavior for NPCs in Ekabar. Everyone is allowed to use magic there, so this conduct is entirely irrational."
    show ff 33
    mc "Interesting..."
    mc "Do you think we'll learn anything about how to free the NPCs from Ulysses' influence?"
    show ff 34
    a "I certainly hope so!"
    show ff 30
    l "I was already disturbed by how poorly people treated NPCs sometimes, but after what [mc] discovered from Alex's father the other day... even more so."
    show ff 34
    a "We've gotta save them!"
    a "We have to gather the ten Gems and liberate the NPCs from... whatever Eternum is!"
    show ff 33
    mc "You can say that again!"
    mc "Are you sure you don't want to join us, Annie?"
    show ff 35
    a "An eerie village in the middle of nowhere, inhabited by menacing dwellers who murder magic users? No, thank you."
    a "I've already had my fill of frights for this week."
    show ff 33
    mc "*Laughs* Fair enough."
    show ff 31
    mc "Welp, ready to go, Luna?"with dis
    mc "Penny texted me that she was heading home as well."
    show ff 32
    l "Sure thing!"
    l "Let's not keep her waiting."
    play sound chairmove
    play sound4 chair2
    if lunapath:
        show ff 36
        l "*Standing up* It was nice seeing you, Annie."with dis12
        l "Tell Nova I said hello."
        play sound clap
        play sound2 clap
        stop music
        scene ff 37
        a "Will do!"with hpunch
        mc "Huh...?!"
        play sound7 visionlunasound
        show lunavision1
        pause 1.2
        play sound6 clotheswhoosh
        pause 0.1
        scene black       
        pause .1
        scene white 
        play soundloop birds
        play soundloop2 birds fadein 2
        pause .02
        scene ff 38 with hpunch
        pause .2
        bla "Luna abruptly withdraws her hand, her eyes wide with surprise, as she stands frozen in place." with dis12
        mc "F-Fuck, Luna??"
        mc "Are you alright?!"
        show ff 40
        a "Luny? Are you okay?"
        a "What happened?"
        show ff 38
        l ". . ."
        if anniepath:
            show ff 39 with dis04
            pause
            show ff 40
            a "I didn't hit you that hard, did I?"
            show ff 39
            pause
            show ff 41 with dis04
            pause
            show ff 42
            mc ". . ."
            show ff 41
            pause
            show ff 43 with dis
            pause
            play music quirky7 fadein 2
            show ff 44
            bla "Luna's gaze shifts between the two of you, then down to herself, and her cheeks burn with a deep flush." with dis12
            mc "Luna...?"
            mc "Are you okay? What did you see?"
            show ff 40
            a "“See”?"
            show ff 45
            l "Y-Yeah, I'm okay, don't worry."with dis
            show ff 40
            a "What happened?"
            a "I'm so confused."
            show ff 45
            l "It's nothing, really. It's just that sometimes I get these... dizzy spells."
            l "But they pass quickly."
            show ff 40
            a "Oh, I'm sorry!"
            a "Was it bad?"
            show ff 45
            l "It... it wasn't. At all."
            l "Just that..."
            l "I mean..."
            l "I don't think that's ever gonna..."
            l "I-I've gotta go. I still have to pass by my dad's cafe before..."
        else:
            show ff 46b
            l "Erm... y-yeah... I'm okay."
            mc "What did you see??"
            l "I saw..."
            l "Just... an ordinary day."
            show ff 40
            a "“See”?"
            a "What are you guys talking about?"
            show ff 46b
            l "Um... nothing, sorry!"
            l "It's just that sometimes I get these... dizzy spells."
            l "Um... I've gotta go! I still have to pass by my dad's cafe before logging in."
        l "I'll catch you in Ekabar, [mc]."
        mc "Um... sure!"
        l "See you later, guys."
        play sound doorsliding
        show ff 46
        bla "Luna quickly exits the cafe."with dis15
        mct "That was odd..."
        mct "Did she have a vision?"
        mct "And if so, what did she see...?"
        mct "I've gotta ask her later..."
        show ff 40
        a "Is she gonna be okay?"with dis 
        a "I'm a bit worried."
        show ff 33
        mc "Y-Yeah! No worries, it's happened to her before."
        mc "Nothing to be concerned about, really."
        show ff 34
        a "Well, in that case, I'm more reassured."
        show ff 33
        mc "I guess I should head out as well, I don't wanna keep Luna and Penny waiting."
        mc "Have fun with Nova!"
        show ff 34
        a "I will!"
        a "Give my best to Penny when you see her too."
        show ff 33
        mc "*Chuckles* Penny? You literally see each other and have dinner together every day."
    else:
        show ff 36b
        l "*Standing up* It was nice seeing you, Annie."with dis12
        l "Tell Nova I said hello."
        play sound clap
        play sound2 clap
        show ff 37b
        a "Will do!"with hpunch
        a "And send my best to Penny, will ya?"
        show ff 33
        mc "Penny? We literally have dinner together every day." with dis12
    show ff 34
    a "But I haven't had a chance to catch up with her since yesterday! Promise me you'll give her my best!"
    show ff 33
    mc "*Laughs* Alright, alright, I will."
    mc "Take care, Annie."
    show ff 34
    a "See you later! And best of luck!"
    show ff 33
    mc "Later!"
    stop music fadeout 6
    jump vampireserver


label vampireserver:
    stop soundloop fadeout 4
    scene black with dis25
    show screen sometimelater with dis15
    pause 
    scene ff 47
    hide screen sometimelater
    with dis25
    play sound doorclose
    mc "*Shutting the door behind you* (Alright... equipment ready!)" with dis12
    mct "Luna should have invited me by now."
    mct "I'll admit, it's almost a pity to play Eternum on a sunny d–"
    play sound thunder fadein 1
    pause 1.2
    mct "Okay, nevermind... I forgot we live in Kredon." with dis
    mct "Sunny moments are as rare as they are brief."
    play sound3 chair1
    show ff 48
    mc "*Jumping on the bed* (Well, it is what it is.)"with dis12
    if penelopepath:
        mct "Better now than tomorrow evening, considering I have to go to the studio with Penny after school."
        mct "And to be honest, knowing that it's raining in the real world adds a certain ambiance."
    else:
        mct "Knowing that it's raining in the real world adds a certain ambiance."
    mc "Hmm."
    mct "Can I even continue calling it the “real world”?"
    mct "I suppose I can... right?" 
    mct "I might not have fully processed William's revelation yet, but one thing's crystal: we've gotta gather those ten Gems... and I sure as hell ain't handing them over to him or the Founder."
    play sound2 beep
    play sound ai7
    blank "{i}Connected." with dis12
    play sound ai8
    blank "{i}Welcome back to Eternum." with dis
    play sound ai9
    blank "{i}You've received an invitation from..." with dis
    play sound ailuna
    blank "{i}Luna." with dis
    mct "Right on time!"
    play sound ai10
    blank "{i}Would you like to join her session?" with dis
    mc "Yes, ma'am."
    play sound ai11
    blank "{i}Please prepare to connect..." with dis
    scene ff48
    stop soundloop2 fadeout 4
    play sound risingshort4
    pause 2
    scene login3 with flash
    pause 8
    play soundlow whoosh4
    scene white with dissolve
    play soundloop river fadein 6
    scene ff 49 with Dissolve(2.5)
    play sound4 ["<silence 2.4>", howl] volume 0.3
    pause 1.3
    mc "*Taking a deep breath* (Aaaahh... it feels good to be back!)"with dis14
    mct "So good."
    mct "The Ekabar server always has this inexplicable “feel good” aura."
    mct "Even though... today's visit isn't supposed to be the most pleasant of experiences."
    mct "Which is precisely why having Calypso's help today would've been awesome, dammit."
    mct "But..."
    stop soundloop fadeout 1
    play soundloop2 fireplace
    play sound whoosh1
    show screen daybeforecorner
    scene ff 0 
    mc "Really?" with flash
    mc "In this cave, in the middle of nowhere?"
    show ff 0b
    ca "Indeed."
    ca "It fulfills all the necessary requisites."
    show ff 0
    mc "So... you're meant to stay here? Meditating?"
    show ff 0b
    ca "The {i}Elarisil{/i} is a ritual perfected by our people over generations."
    ca "It aids us in channeling all our magic towards a specific objective."
    ca "Through this, I believe I shall finally be able to find my way back to Hyril'ar."
    ca "I have deferred my search for far too long."
    show ff 0
    mc "And you need to be alone?"
    show ff 0b
    ca "I must remain in complete isolation, with no company but my own."
    show ff 0
    mc "For how long?"
    show ff 0b
    ca "It is uncertain. It may span days, or perhaps weeks."
    show ff 0
    mc "WEEKS?!" 
    show ff 0b
    ca "Once you leave this cave, I shall commence the ritual."
    ca "Under no circumstances must you disturb me or disrupt the proceedings."
    ca "Do you understand?"
    show ff 0
    mc "Damn."
    mc "Well... if you think you can find your homeland through this, we won't disturb you, don’t worry."
    mc "Will you be safe all on your own, though? Ekabar can be treacherous."
    show ff 0b
    ca "Do not fret for me."
    ca "I have yet to encounter a potential threat to my person in any of the worlds we have visited."
    ca "And moreover... I doubt your presence would alter the outcome in combat."
    show ff 0
    mc "Hey, you know I'm no ordinary human."
    mc "Who knows, I might even surprise you."
    if calypsopath:
        mc "It wouldn't be the first time, would it...?"
        show ff 0bb
        ca ". . ." with dis
        ca "Hmph."
        show ff 0c
        ca "Y-You have demonstrated yourself a capable warrior, I will admit that."
        show ff 0bbb
        mc "*Chuckles* (She might be an elven Princess, but in the end, she stutters like any other girl would when she's nervous.)"
        show ff 0c
        ca "If all proceeds according to plan, the next time we meet I shall have reclaimed my throne."
        ca "Remember, do not disturb me under any circumstances."
        show ff 0bbb
        mc "We won't, my Princess."
        mc "I wish you the utmost success."
        show ff 0c
        ca "Thank you, [mc]."
        ca "You shall be granted a special place in my court when I reign over Hyril'ar once more."
        show ff 0bbb
        mc "Next to the Princess herself?"
        show ff 0c
        ca "Directly under her."
        show ff 0bbb
        mct "That's certainly the position I'd like to be in..."
        mc "What an honor, your Highness..."
    else:
        show ff 0b
        ca "Regardless... I shall commence now."
        ca "If all proceeds according to plan, the next time we meet I shall have reclaimed my throne."
        ca "Remember, do not disturb me under any circumstances."
        show ff 0
        mc "We won't, my Princess."
        mc "I wish you the utmost success."
        ca "Hmph."
    stop soundloop2 fadeout 1
    play soundloop river fadein 1
    play sound whoosh1
    hide screen daybeforecorner
    scene ff 49 
    mct "So... yeah, better not to disturb her." with flash
    l "[mc]!"
    play music2 wvv0 fadein 6
    scene ff 50
    bla "You turn around and see Luna at the other side of the river." with dis12
    mc "Hey there!"
    l "Come this way, the village is up north!"
    mc "On it!"
    play sound2 water2
    play sound3 drips
    show ff 51 with dis17
    $ unlock_look("luna", 11)
    if lunapath:
        mc "Ah, I'm relieved to see you're alright!" with dis08
        mc "I was kind of worried after what went down at the cafe with Annie."
        mc "I guess that what happened was partly on me, too."
        show ff 52b
        l "Oh... don't worry, you seriously didn't do anything wrong."with dis
        l "I just forgot who I was for a moment and... well, this is why I always wear gloves in the real world."
        show ff 52c
        mc "What did you see, though?"
        mc "You're usually so calm, so seeing you that rattled threw me off."
        mc "Was it... was it something bad?"
        mc "Is Annie in danger?"
        show ff 52b
        l "No! Not at all!"
        l "She's fine, really."
        if anniepath:
            l "We... we seemed to be more than fine, actually."
            show ff 52c
            mc "We?"
            show ff 52b
            l "It was nothing, really."
            l "Like I said, my visions are random and I can't control what I see."
        else:
            l "I just got startled because I wasn't expecting it."
            l "But like I said, my visions are random and I can't control what I see."
        l "I just saw... an ordinary day in Annie's future."
        l "Nothing to worry about."
        show ff 52c
        mc "Oh... well, you put me at ease, then."
        l "Mm-hm."
        mct "She's clearly hiding something..."
        mct "I might ask her again about it at a better time."
        mc "You know, changing the subject, I love your look!"
    else:
        mc "Wow, I love your look!" with dis08
    mc "Very... “Van Helsing-esque”."
    show ff 52
    if not lunapath:
        l "Thanks! I prepared 3 hunter outfits for the three of us."
    else:
        l "Ah, thanks. I prepared 3 hunter outfits for the three of us." with dis
    show ff 51
    mc "*Gasps* I have one too?!"
    show ff 52
    l "Yes!"
    l "Do you wanna try it? I'll send it to your inventory."
    show ff 51
    mc "You bet I do!"
    play sound4 ["<silence 0.5>", howl] volume 0.15
    show ff 54 with dis15
    bla "Luna gives you your new outfit and turns her back on you." with dis12
    play sound belt
    play sound2 zip volume 0.5
    play sound3 clothes3
    mc "*Getting changed* So... do we know the exact location of this village?"
    show ff 53
    l "That's what I was trying to determine right now."
    l "If I'm not mistaken, Hollowbrook should be beyond that small hill, about a 20-minute walk from this Exit Portal."
    play sound clothes5
    show ff 54
    mc "Ah, not too far from here, that's good."
    show ff 53
    l "Our meeting point was supposed to be right at the village entrance, so Penny might already be waiting for us there."
    play sound2 zip volume 0.4
    show ff 55
    mc "Let's not keep her waiting, then!" with dis14
    mc "I think I'm ready!"
    show ff 56
    mc "What do you think?"
    mc "It looks pretty cool, doesn't it?"
    show ff 57
    l "You look so... badass!" 
    l "I was worried I might have picked the wrong size, but it seems not."
    l "It fits you like a glove."
    play sound clothes3
    show ff 59
    mc "*Putting on the mask* Oh boy, I feel like a hunter already." with dis
    mc "What's our cover? Vampire slayers?"
    show ff 57
    l "I'll explain more when we find Penny, but I thought of telling them we're indeed hunters from another village that was also attacked by vampires."
    l "And that we're there to assist the villagers, essentially."
    show ff 58
    mc "That sounds good!"
    show ff 57
    l "We can use this cover to find out how it all began and what triggered their erratic behavior."
    l "They even killed real players not too long ago, so we should be extra careful."
    show ff 58
    mc "Interesting..."
    mc "They could be the key to free all the NPCs from Ulysses' control."
    show ff 57
    l "And remember, no magic – they might mistake us for foes too."
    show ff 58
    mc "No magic, gotcha."
    show ff 57
    l "Are you ready?"
    play sound clotheswhoosh
    show ff 60
    mc "I'm ready!" with hpunch 
    mc "Monster hunters Luna Hernandez and [mc] [lastname] set off on a thrilling new adventure in Hollowbrook!"
    l "*Chuckles* Follow me."
    stop music2 fadeout 5
    scene black with dis22
    show screen afewminuteslater with dis17
    pause 
    play music wvv1 fadein 13 volume 0.9
    stop soundloop fadeout 9
    scene ff 61
    hide screen afewminuteslater
    with dis25
    play sound4 ["<silence 0.9>", howl] volume 0.2
    play sound5 ["<silence 2.1>", wind4] 
    bla "Following a brief stroll through the forest, you and Luna unexpectedly come upon a village nestled in the heart of the woods." with dis12
    mc "Shit, it's gotta be this!"
    l "Yes, this has to be Hollowbrook."
    l "But it looks..."
    mc "Abandoned."
    l "I like abandoned villages."
    if lunapath:
        l "When I began to play Eternum there was one I liked to visit a lot. It had an old barn where I liked to hide."
        l "I even became friends with a cow."
        mct "God, she's adorable."
    mc "This one looks especially decrepit, though."
    mc "Do you think we're too late?"
    mc "Did the vampires... kill everyone?"
    l "I hope not..."
    show ff 62
    bla "Suddenly, Penelope appears at the doorway of the nearest house and starts enthusiastically waving her hand for you to come closer." with dis12
    l "Penny!"
    l "Wait... that's Penny, right?"
    mc "Yep!"
    mc "(I could recognize those hips from a mile away...)"
    mc "We're coming!"
    play sound2 doorsqueak
    scene ff 63 with dis22
    stop sound2 fadeout 1
    play sound doorwoodclose
    bla "You step inside, as Penelope promptly closes the door behind you."with vpunchslow
    mc "Good to see you, Penny!"
    p "Silence!"with hpunch 
    mc "W-What?"
    $ unlock_look("penelope", 15)
    show ff 64b
    p "Shhh, keep your voice down." with dis12 
    p "We don't know who could be watching us."
    mc "Watching us...?"
    show ff 64
    p "I arrived a bit earlier than we agreed to scout the surroundings, and this whole village gives off an eerie vibe that I don't like."with dis
    p "I had this strange sense, like I was being watched."
    p "We have to be careful."
    show ff 65
    mc "Oh, I see..."
    show ff 64
    p "I also found some footprints on the road leading to the south forest that appear to be from a rather {i}big{/i} canine. So... be cautious."
    show ff 65
    mct "She arrived “a bit earlier to scout”, eh? And I thought she was hitting the mall."
    mct "Heh, who would've thought Penelope would get so into Eternum?"
    mct "She's been playing even more than me lately."
    if penelopepath:
        mct "And I've gotta say... I love it."
        mct "It makes her even sexier."
        show ff 65b
        p "Looking good, [mc]." with dis
        p "You look badass. I dig it."
        show ff 65bb
        mc "Ah, thanks!"
        mc "You look fantastic as well."
        show ff 67
        l "I'm with [mc] on this one!"
        show ff 65b
        p "Thanks, guys!" 
    else:
        mc "By the way... looking good, Penny!"
        show ff 65b
        p "Right?" with dis
    p "I'm really loving this outfit, too. It's a gift from someone with a remarkable, hidden talent for fashion."
    show ff 67
    l "*Chuckles* I just went for bolder colors for your outfit."
    l "I thought you'd like it."
    play sound chair2
    show ff 68
    p "*Leaning next to Luna* I'm in LOVE with it."with dis14
    p "Luna should become the official stylist of the team."
    p "I've passed on all my knowledge, she's the master now."
    show ff 70
    mc "*Chuckles* I'm all for it."
    mc "Everyone knows that in video games, and... well, by extension... parallel astral realities, the only stat that truly matters for an outfit is how good it looks."
    show ff 69
    l "I only had two silver swords, though, so we'll have to share."
    show ff 68
    p "No worries, I'll probably use mine only as a prop."
    p "I've never had sword practice, so magic will be my go-to if we run into danger."
    show ff 70
    mc "Just remember, no magic unless it's absolutely necessary. We can't afford to blow our cover."
    mc "That's assuming there's even an NPC left alive in the village, of course..."
    show ff 69
    l "We should aim for the town center."
    l "If there's anyone alive, they'll likely be there."
    show ff 68
    p "Yeah, we should check it out before nightfall. The sun's setting soon."
    show ff 70
    mc "Good idea."
    mc "Alright then, we've got our plan!"
    mc "Time to hunt down those bloody vampires."
    stop music fadeout 7
    play soundloop wind2 fadein 7 volume 0.45
    scene ff 71 with dis3
    play sound4 ["<silence 1.7>", howl2] volume 0.4
    pause 
    mc "Hmmm..." with dis
    mc "Is this the center of the village already?"
    p "I believe so, yeah."
    mc "It's a rather small settlement."
    p "True, I doubt there were more than 300 people living here."
    l "Should we start going through the houses one by one?"
    l "Maybe we'll find someone this way."
    play sound chill
    scene hollowgray with dis12
    pause .3
    scene ff 71 with dis15
    bla "An intense chill runs down your spine." with dis15
    mct "This sensation again... like in the Western server."
    mct "As if I could... sense the danger."
    p "[mc]?"
    mc "That won't be necessary."
    l "What?"
    show ff 72
    mc "Searching each house." with dis15
    mc "Looks like they've found us already."
    p "Huh?"
    play sound jumproof
    play musicb wvv2 fadein 7
    scene ff73
    bla "Four men suddenly descend with swift, graceful precision from the roof of a nearby building." with vpunch
    play sound2 debris
    scene ff 75 with dis2
    show ff 74
    hun "*Standing up* You don't belong here, outsiders." with dis
    hun "The sun is about to set. Leave now if you value your lives."
    show ff 75
    mc "*Pointing at your attire* We're hunters, just like you."
    mc "Our village was ravaged by vampires a long time ago. We've come to ensure you don't suffer the same fate."
    show ff 74
    hun "Magic is a malevolent force, a temptation from the devil in this world. It is present everywhere."
    hun "Seek your battles elsewhere. We'll manage here."
    show ff 75
    mc "Are you all... hunting the demons?"
    show ff 74
    hun "Those who couldn't wield a blade or run fast enough... left us long ago."
    hun "Few of us remain."
    show ff 75
    mc "So you're all from Hollowbrook?"
    mc "Why don't you abandon the town?"
    show ff 74
    hun "We won't rest until those abominations have been eradicated."
    hun "The Lord watches over us in our pursuit."
    show ff 75
    mc "When did the attacks begin?"
    mc "How many have–"
    show ff 74
    hun "Enough questions."
    hun "Leave, before night is upon us."
    show ff 75
    mct "He's on the defensive."
    mct "We should help them dispatch the “demons” – they'll probably be more open to our questions after."
    mct "There has to be something that triggered their abnormal behavior, and we need to discover {i}what."
    mc "I insist."
    mc "Let us help you in this hunt."
    hun ". . ."
    show ff 74
    hun "Alright... suit yourself."
    hun "But know this: if you fall, your remains will feed the swine come dawn. You won't receive a proper burial."
    show ff 75
    mc "I... I understand."
    mct "This is certainly not the warm welcome I was expecting."
    show ff 78
    hun "About the women... they must seek shelter inside the inn, with the rest of them." with dis12
    show ff 77
    l "What? We're also hunters."
    show ff 78
    hun "Only men can be hunters."
    show ff 77
    l "Maybe in Hollowbrook, but where we're from, it's a different story."
    show ff 78
    hun "Oh, yeah? And what do you expect to do when a 250-pound mongrel tries to rip your leg off?"
    mct "Oh shit, so that's where the howls we've been hearing come from..."
    show ff 77
    l "I'm sure we'll manage, one way or another."
    l "And if we don't... well, we'll face the music."
    show ff 78
    hun ". . ."
    hun "Bah."
    show ff 74
    hun "Do as you like." with dis12
    hun "Just don't bring those cursed creatures to the town, or we will treat you no differently than them."
    show ff 75
    mc "We won't."
    mc "So, where can we find them?"
    show ff 74
    hun "Head east to the old crypt of the Lord of Hollowbrook, that's where those bloodsuckers like to hang out."
    hun "We've tried to smoke 'em out a few times, but they're slippery vermin."
    hun "And for the mutts, well, they're somewhere out west. Couldn't tell you exactly where."
    show ff 75
    mc "Mutts...?"
    mc "Do you mean... werewolves?"
    show ff 74
    hun "You can call them whatever you want."
    hun "In the end, they're all just demons that need to be butchered like the beasts they are."
    show ff 75
    mc "Of course..."
    mc "I understand the situation."
    mc "By dawn, there won't be any demons left standing."
    hun "Hmm."
    mc "Anything else we should know?"
    hun ". . ."
    show ff 74
    hun "You don't have a weapon."
    hun "There's a sword in the first house past the chapel."
    hun "If you're curious about what happens to the dogs who get too close, they're in the same spot."
    hun "Vampires, on the other hand, simply turn to ashes when the sun kisses 'em."
    show ff 75
    mc "I... appreciate it, I'll check it out."
    mc "Good luck."
    hun ". . ."
    stop musicb fadeout 7
    play sound footsteps3
    show ff 81 with dis2
    mc "Well..." with dis06
    mc "Vampires and werewolves."
    mc "This is getting better and better by the moment."
    show ff 80
    p "I think it's cool!"
    show ff 79
    mc "Really?"
    show ff 82
    l "Absolutely!"
    l "I've always been captivated by stories about vampires and lycanthropes."
    show ff 81
    mc "*Chuckles* Your enthusiasm is infectious, I'll admit it."
    show ff 79
    mc "Okay, so... what's the plan?"
    show ff 80
    p "I suggest we split up. It increases our chances of finding the monsters."
    show ff 79
    mc "Are you sure? Will you be able to handle something like that all alone?"
    show ff 80
    p "Oh, definitely, trust me!"
    p "I've been honing my skills and making great progress with my magic."
    show ff 79
    mc "Well... alright, but if you're planning to use magic keep out of sight from the villagers!"
    show ff 82
    l "How should we split up?"
    show ff 80
    p "I'll take on the vampires!"
    p "If they're as elegant as the legends go, I want to witness it firsthand."
    show ff 82
    l "Oh, I'll go find the werewolves, then."
    l "I've always felt more comfortable around animals than people anyway."
    show ff 81
    mc "Damn, no one can say you're hesitant, that's for sure."
    mc "Alright, I guess that settles it."
    mc "I'll stay in town, gather intel, maybe even find some clues."
    mc "Or maybe the creatures decide to attack the town at night, so it's probably better if one of us stays around."
    show ff 80
    p "That sounds good!"
    p "Let's meet again here in 4 hours."
    show ff 79
    mc "Okay, let's do that."
    mc "But promise me, be careful!"
    show ff 80
    p "Don't worry, a couple of low-level monsters are no threat to us!"
    show ff 82
    l "She's right!"
    l "YOU be careful!"
    show ff 81
    mc "I will, I will..."
    mc "*Sighs* Four hours, everyone! Four hours and we all rendezvous here!"
    show ff 82
    l "Yes!"
    show ff 80
    p "Deal!"
    play sound footsteps3
    scene ff 71 with dis25
    mc "(Agh, splitting up again.)" with dis
    mct "That’s always worked well before, yeah..."
    mc ". . ."
    mc "*Sighs* (I guess I have to trust them, though.)"
    mct "We're a team, and I can't be everywhere at once."
    mct "I should do my part. Let's start checking out the house that man mentioned..."
    play sound2 footsteps3
    scene ff 83 with dis25
    mct "Mmh, it should be this one." with dis
    play sound3 doorsqueak
    scene ff 84 with dis22
    play soundloop2 deception
    mct "Holy fuck..." with dis12
    mct "These are... the werewolves?"
    mct "They revert to their human forms after dying, I guess..."
    mct "Jesus, they mutilated and burned their corpses."
    mct "Or... at least I hope they were already dead when they burned them."
    mct "My god..."
    mct "I better investigate the rest of the village."
    mct "I feel like the sooner we leave this place, the better..."
    stop soundloop fadeout 8
    stop soundloop2 fadeout 5
    scene black with dis3
    show screen sometimelater with dis2
    pause 
    play soundloop2 night fadein 4
    hide screen sometimelater
    show hollowbrook
    with dis17
    play sound5 wind4 volume 0.6 fadein 5
    pause 1
    play soundlow howl2
    pause 7.2
    scene ff 86 
    mc "*Yawns* AAAaagh..." with dis
    mct "It hasn't even been two hours, and I've already scoured the entire village."
    mct "It's like a ghost town, except for a couple of houses."
    mct "And what's worse, trying to talk to the few villagers left is like talking to a brick wall."
    mc "*Sighs* (I should have stuck with the girls.)" 
    play sound ["<silence 0.2>", church2] volume 0.14
    mc ".​​ㅤ​​ㅤ.​​ㅤ​​ㅤ.​​ㅤ​​ㅤ.​​ㅤ​​ㅤ."
    mc ".​​ㅤ​​ㅤ.​​ㅤ​​ㅤ.​​ㅤ​​ㅤ.​​ㅤ​​ㅤ.​​ㅤ​​ㅤ.​​ㅤ​​ㅤ.​​ㅤ​​ㅤ.​​ㅤ​​ㅤ."
    mct "...I don't like being alone with my thoughts for so long."
    mct "I'm much happier when I don't overthink what I do and just go with the flow."
    mc ". . ."
    mct "Maybe I should try to find them?"
    mct "I'd probably be way more useful out there than here."
    mct "But... what if the monsters attack the town while I'm away?"
    mc ". . ."
    play sound clothes4
    play sound2 debris
    show ff 87
    mct "You know what, let's leave it to chance."with dis12
    mct "I think I have a coin around here somewhere."
    mct "Hmm..."
    play sound3 clothes3
    show ff 88
    mct "Aha!" with dis
    mct "Alright, let fate decide whether I should go find them or not."
    mct "I go help them if I get..."
    menu:
        with dis12
        "Heads":
            mc "Heads."with dissolve
            play sound glitch4 volume 0.5
            show 07idrielglitch
            pause 0.35
            mc "If I get tails, I stay in town."
            $ headshollowbrook = True
        "Tails":
            $ tailscoin3 = True
            mc "Tails."with dissolve
            play sound glitch4 volume 0.5
            show 07idrielglitch
            pause 0.35
            mc "If I get heads, I stay in town."
    play sound coinflip
    scene ff 89 with Dissolve(.4)
    pause .3
    show ff 88 with dissolve
    pause .3
    show ff 90
    mc "Hmm?" with dis12
    if headshollowbrook:
        mc "Heads!" 
    else:
        mc "Tails!" 
    mct "Well, it's decided. I'll go find them."
    mct "I won't be the one to go against fate."
    play sound2 clothes3
    play sound3 clothes3
    scene ff 87
    mc "Now, the big question..." with dis12
    mc "Should I head east or west? Vampires or werewolves?"
    show ff 85
    mc "Hmmm..." with dis15
    call screen ekabarlunapennychoice with dis17
label mod_vamp_wolf_help:
    scene ekabaridle
    mod "You'll see both options and will then decide which one will be the main one."
    $ mod_vamp_wolf = True
label vampirehelpm:
    $ vampireshelp = True
    scene ekabaridle
    pause 0.001
    scene ff 85
    mct "Let's go find Penny."with dis
    mct "She's probably the one who needs more help anyway, she's still a newbie after all."
    mct "I'm sure Luna will be fine."
    jump poshelpm
label werewolfhelpm:
    $ werewolveshelp = True
    scene ekabaridle
    pause 0.001
    scene ff 85
    mct "Let's go find Luna." with dis
    mct "Werewolves seem way more menacing. I’m sure Penny will be able to charm the vampires."
    mct "The werewolves though... some extra help won't hurt, I'm sure."
label poshelpm:
    play sound debris
    show ff 85bb
    mc "*Standing up* (Alright then, let's wrap up this whole thing before it gets too late.)" with dis15
    mct "It's easy to forget that it's still Thursday and there's school tomorrow..."
    mct "So let's get moving!"
    stop soundloop fadeout 8
    stop soundloop2 fadeout 5
    scene black with dis2
    show screen sometimelater with dis2
    pause
    if vampireshelp:
        jump vampireslabel
    else:
        jump werewolveslabel
    
label vampireslabel:
    play soundloop wvvgraveyard fadein 5
    hide screen sometimelater
    scene fv 1 
    with dis25
    bla "After a meandering walk through the woods, you eventually stumble upon an ancient cemetery, cocooned in the embrace of shadows." with dis17
    mct "Ah! This has to be the place. The hunter mentioned an old crypt."
    mct "Hmm, I wonder if Penny was able to find it, too."
    mct "Maybe she's already back in the village waiting for us."
    mct "I should get closer to be sure..."
    play sound footsteps3 fadein 2
    scene fv 2 with dis22
    mct "O-Okay, this place is kinda creepy, not gonna lie."with dis12
    mct "Maybe..."
    scene fv 3
    mct "Huh? A torch on the floor...?" with dis
    mct "Shit, could it be Penny's?"
    scene fv 2
    mct "Ugh, just the thought makes me shiver." with dis
    mct "I don't like this..."
    mct "But there's no turning back now."
    mc "*Taking a deep breath* (Grow a pair, [mc].)"
    mct "YOU'RE A HUNTER."
    play sound metalgate
    show fv 4 with dis17
    bla "You pick up the torch from the ground and slowly open the creaky cemetery door. You can hear it shutting behind you."with dis 
    mc "*Whispering* Penny?"
    mc "Are you here?"
    mc "I've come to lend a hand!"
    bla ". . ."
    show fv 5 with dis2
    bla "You start walking through the corridors of the old cemetery, only to find dead trees and weathered tombstones." with dis
    mct "Holy fuck, this scenario looks like something straight out of a spooky movie."
    mc "Hello...?"
    bla ". . ."
    mct "Dammit Penny, where are you..."
    show fv 6 with dis2
    mct "Hmm..." with dis 
    mct "This place looks completely deserted."
    mct "I wonder if there are even any vampires."
    mct "Maybe there are no werewolves either... maybe it's all part of a collective hysteria, stories spun from too much mead and–"
    play sound branch
    bla "You hear a noise coming from behind the mausoleum in front of you."
    mc "H-Hey!" with hpunch
    mc "I heard that!"
    mc "Show yourself or you'll regret it..."
    play sound2 clotheswhoosh
    play sound4 debris3
    play sound5 punch
    play sound3 sword3
    play soundloop night
    scene fv7
    bla "Penelope suddenly appears and shoves you against the cold, stone wall." with hpunch
    play music shenanigans fadein 5
    mc "P-Penny?"
    mc "Oh, thank god, I thought–"
    p "Quiet, demon!" with hpunch
    mc "I'm sorry...?"
    mc "It's me, [mc]!"
    p "The real [mc] is in Hollowbrook!"
    mc "What?!"
    mc "I mean... yes, I was, but then I got bored and came over to help you!"
    p "Oh, great, a repeat of the Warthogs incident..."
    mc "Eh?"
    p "You're not the first fake [mc] I’ve run into!"
    mc "WHAT?!" with hpunch
    mc "I'm real!"
    p "How do I know you're not just some Boggle trying to deceive me?"
    p "Prove it!"
    mc "Um... o-okay."
    mc "Eh..."
    mc "Remember when we..."
    if penelopepath:
        menu:
            with dis
            "Had the photo session":
                mc "Had the photo session?!"with dissolve
                mc "I hadn't been in Kredon for too long, and we both went to a photoshoot together."
                mc "I told Valentino to leave, and we ended up having a... private session."
                mc "A... really good one."
            "[gr]Used the Reminiscecombobulator" if divinationflashback:
                $ pennyremember = True
                mc "Used the Reminiscecombobulator?!"with dissolve
                mc "It was your first time in Eternum, so we went with Luna to Warthogs to learn the basics of magic."
                mc "We both saw one of your memories where you gave up going to the dance so Nancy could get her new job!"
            "Went to Regina's room":
                mc "Went to Regina's room?!"with dissolve
                mc "She ruined your Idriel costume, and then we went to her room to retrieve the yearbook."
                mc "We didn't find it, but we ended up... naked, and... doing some other things."
                mc "Good... things. And we... er... I left a mess on the floor."
    else:
        mc "Erm..."
        mc "Orchestrated a heist together?"
        mc "We stole Garrington's Gem from his own casino!"
        mc "You disguised yourself as a renowned influencer and convinced his son he'd been poisoned!"
    p "Oh..."
    scene fv 8
    if pennyremember:
        $ penelope_points += 1
        play sound beat
        show screen heartbeat
    play sound2 holster2 fadein 1
    p "*Putting her sword down* I do remember that." with dis12
    mc "Oh, thank goodness..."
    show fv 10
    if pennyremember:
        p "How come you brought that up?"
        show fv 9
        mc "I don't know, it just popped into my head."
        mc "That day holds a special place in my memories."
        show fv 10
        p "That's not what I was expecting you to say... but I like it."
        p "Although... I would've been equally pleased with a nod to those {i}incredibly{/i} delicious pretzels we baked with Annie the other day."
        show fv 9
        mc "*Laughs* That was my backup choice."
    elif penelopepath:
        p "Only recalling horny stuff when trying to remember a past memory?"
        p "Yeah, you're definitely the real [mc]."
        show fv 9
        mc "*Laughs* Hey, it's your fault that those memories struck a chord with me..."
        show fv 10
        p "*Chuckles* Fair enough."
        p "At least now I know you're legit."
        p "Although... I would've also accepted a nod to those {i}incredibly{/i} delicious pretzels we baked with Annie the other day."
        show fv 9
        mc "*Laughs* That was my backup choice."
    show fv 9
    mc "I'm relieved to see you're okay, Penny."
    show fv 10
    p "And I'm so glad you're here!"
    show fv 9
    mc "Are you alright? What happened to your vest?"
    show fv 11
    p "Ugh, don't remind me..."with dis
    p "I got ambushed by those cursed vampires and they tore it off."
    show fv 12
    mc "Oh shit, really?"
    show fv 11
    p "Yeah, I managed to shake them off, but I lost my vest in the process."
    p "Luna is gonna be mad..."
    show fv 12
    mc "*Chuckles* Don't worry, I don't think I've ever seen Luna angry."
    mc "It's a shame, though. It was such a nice outfit."
    show fv 11
    p "I know!"
    show fv 12
    mc "Try to look on the bright side, at least now you have more freedom of movement."
    if penelopepath:
        show fv 14
        p "*Pressing her boobs together* Well..." with dis12
        p "Yes... but actually, no."
        p "You catch my drift?"
        show fv 16
        mc "N-Not really, no. What do you mean?"
        scene fv14
        p "Like, the vest was also kind of supporting my breasts, you know?" with dissolve 
        p "I mean... I'm not wearing anything under this shirt."
        scene fv 16
        mc "Oh." with dissolve
        mct "My god..."
        mct "Is she trying to hypnotize me? Because she's certainly succeeding."
        scene fv14
        p "Standing still or walking is fine, but when I had to sprint to escape from those vampires earlier... it kinda hurt." with dissolve 
        p "Because of the... you know, the bouncing."
        scene fv 16
        mc "Oh, of course, yeah... I can imagine." with dissolve
        mct "Oh boy, would you look at that..."
        mct "I can't believe I actually got to shove my cock between Penny's massive tits at the party."
        mct "I'd give anything to repeat that someday."
        mct "Which reminds me... we're supposed to have a photo session together tomorrow."
        mct "And she seemed quite excited when she asked me to go with her."
        mct "Maybe... she’s hinting she wants to do something more with me...?"
        mct "I mean, I don't think so. We haven't really talked about it since that day. And... it's a public place, after all."
        mct "Although... the first photoshoot was also in a public place, and..."
        bla "You raise your gaze from Penelope's chest to meet her eyes, finding her staring at you in a bemused manner."
        mc "*Clears throat* SO!"with hpunch 
        mc "W-We'll have to retrieve that vest!"
        mc "Did you say... vampires took it?"
    else:
        show fv 11
        p "Yeah... I guess."
        show fv 12
        mc "And... the vampires took it, you say?"
    scene fv 13
    p "Yeah... those fucking leeches." with dis12
    p "They're fast as hell, and there's literally a horde of them, but luckily they're also stupid."
    p "If we set up a trap, we should be able to outmaneuver them."
    stop music fadeout 10
    stop soundloop fadeout 8
    play soundloop2 wvvgraveyard fadein 8 volume 0.6
    scene fv 17 with dis17
    p "*Whispering* Come over here, I'll show it to you." with dis
    mc "Are they still in this cemetery?"
    mc "I didn't see anything earlier."
    p "That's because they all rushed to the other side when I screamed before."
    p "They're blind, but they hunt by sound."
    p "They're coming this way... look!"
    show fv 18
    bla "You look towards the direction Penelope is pointing at and squint your eyes into the inky darkness." with dis15
    mc "Hmm..."
    play sound debris
    play sound2 debris3
    play sound3 monsterbreath2
    play sound4 jump2
    scene fv19
    bla "A creature suddenly climbs up the tombstone with lightning-fast speed." with vpunchslow
    mc "H-Holy shit!"with hpunch 
    mc "What the fuck is that?!"
    p "*Whispering* Keep your voice down!"
    play sound5 vampire
    scene fv 20 with dis04
    vam "*Squeals*{w=3.6}{nw}" with hpunchlong5
    play sound6 jump2
    play sound7 debris2
    play sound monsterbreath2
    scene fv 21 with dis2
    bla "Answering the call, more creatures start emerging from everywhere, heading towards your direction." with dis12
    p "O-Oh shit."
    mc "Fuck, there are dozens of them!"
    p "I tried to attack one of them before, but they seem to be immune to magic."
    mc "That's not good..."
    p "Maybe you can take my sword and–"
    play sound3 jump2
    play sound4 debris3
    play sound5 punch
    scene fv22
    bla "You swiftly push Penelope around the corner."
    p "W-What's going on?"
    mc "*Whispering* Don't make a sound. One of them is coming this way."
    mc "*Whispering* And he looks BIG."
    p "*Whispering* W-What?"
    if daliapath:
        mct "A-Alright [mc], calm down."
        mct "If magic can't harm them, now's the time to put into practice Dalia's training from last week."
        mct "O-Okay, what was the first step against bigger enemies..."
        mct "Think, [mc], think..."
        mct "It was..."
        jump daliatraining07
label continuedaliapenny:
    if daliapath:
        play soundloop2 wvvgraveyard fadein 9
        play soundloop night fadein 5
        stop music fadeout 8
        scene fv 22b with dis27
        mct "Goddammit, Dalia needs to stop wearing those shorts to our training sessions."with dis12
        mct "I get distracted way too easily."
    play music beat3 fadein 3
    play soundloop beat3 fadein 3
    play sound6 footstepsmonster
    scene fv 23 with dis27
    play sound7 monsterbreath2
    mct "H-HOLY SHIT."with dis12
    mct "I was right, up close they're way larger than they looked from a distance."
    mct "Now that I see one standing straight, they almost look... human-like."
    play sound monsterbreath2
    show fv 24
    bla "The creature remains still, utterly immobile. You can feel Penelope clinging tightly to your back, her body pressed firmly against yours."with dis15
    mct "Why is he not moving?"
    mct "Why did he stop {i}here{/i}...?"
    play sound3 monsterbreath2
    show fv 25
    mct "Wait..." with dis17
    mct "They might be blind, but..."
    mct "What about their sense of smell...?"
    play sound2 sniff2
    show fv 26
    vam "*Sniffs* . . ." with dis15
    play sound7 transformpower
    mc "*Activating your powers* You wanna dance, you bastard?"
    mc "*Pushing Penelope behind you* THEN LET'S DANCE!" with hpunch
    play sound5 vampire
    scene fv 27 with dis04
    vam "*Squeals*{w=1.8}{nw}" with hpunchlong5
    stop music
    stop soundloop2
    play soundloop night
    play sound5 stab
    play sound2 vampire2
    scene fv 28 
    vam "{sc=2}Gggh.{/sc}" with vpunch 
    play sound fallfull
    play sound2 monsterbreath
    play music wvvball0 fadein 8
    scene fv 29 
    vam "*Collapsing to the ground* G-Gggghh-h-hgghhhh..." with dis14
    aaa "You stupid animal..."
    aaa "Can't you see that they're our guests?"
    p "What the..."
    aaa "Of course you can't."
    play sound punch
    play sound3 debris3
    play sound2 vampire2
    show fv 30
    aaa "*Kicking the creature* Now get out of my sight!" with hpunch
    aaa "And go take a shower, for heaven's sake, you reek like rotten eggs!"
    play sound4 leather
    scene fv 31
    aaa "*Bowing gracefully* Good evening, madam and sir."with dis12
    mor "I am Mortimer. Please, accept my sincerest apologies for the unsettling welcome you just received."
    mc "Uh..."
    p "N-No problem."
    mor "It is my great pleasure to welcome you to Lord Iliescu's residence."
    play sound4 leather
    scene fv 32
    mc "What..." with dis12
    mc "How..."
    mc "WHAT are you?!"
    scene fv 33
    mor "I understand that my actual appearance can be... startling at first."
    mor "However, please be assured, my manners are nothing like those of my less refined brethren."
    scene fv 32
    mc "So... you're also a vampire, then?"
    mc "Why can you speak, when the others can’t?"
    scene fv 33
    mor "I am certain Lord Iliescu will be more than willing to address all of your inquiries."
    mor "Please, allow me to escort you to his chambers."
    scene fv 32
    mc "Um... I appreciate the offer, but we're actually in a bit of a hurry."
    mc "We were headed to West...sylvania and arrived in Hollowbrook by mistake. We should probably get a move on."
    scene fv 33
    mor "Please, I insist."
    mor "I am confident Lord Iliescu and his wife would be delighted to receive you."
    mor "It has been quite some time since we last had visitors... excluding those vexatious hunters, of course."
    play sound4 leather
    show fv 35
    mor "Because... you're not hunters, are you?"with dis12
    show fv 34
    mc "N-Not at all."
    play sound4 leather
    show fv 36
    mor "Good, good." with dis12
    mor "I noticed you're wearing hunter attire, but the lady's outfit doesn't seem to adhere to the typical regulation."
    mor "And when I saw you entering the cemetery without immediately attempting to set everything ablaze, I thought it was just a mere coincidence."
    mor "Perhaps you took the guise of the hunter to travel across this land more easily?"
    mc "That's... surprisingly accurate, actually."
    play sound4 leather
    show fv 33
    mor "Now please, come with me to meet Lord Iliescu."with dis12
    mor "I assure you, it shan't take more than 15 minutes of your time."
    show fv 32
    mc "Um..."
    mct "Hmm... it seems like he's actually a genuinely nice guy... despite his appearance."
    mct "At worst, I could activate my powers and take Penelope to a safe place before they even realized what was happening."
    mc "Alright... we'll meet them."
    mc "But we have to be back in Hollowbrook within 30 minutes. Northsylvania awaits!"
    show fv 33
    mor "I thought you said Westsylvania."
    show fv 32
    mc "W-Westsylvania awaits!"
    play sound4 leather
    show fv 31
    mor "*Bowing gracefully* Excellent!"with dis12
    mor "Please, follow me."
    mc "Sure."
    mc "*Whispering* The things that happen to us... Never a dull day."
    p "*Chuckles* I like it! It's exciting!"
    mc "Let's see what this “Lord” can tell us..."
    stop music fadeout 9
    stop soundloop fadeout 9
    play soundloop2 cave fadein 6
    scene fv 37 with dis3
    bla "Mortimer guides you through a labyrinth of tunnels and galleries, eventually leading you to a crypt adorned with a mysterious altar at its center." with dis14
    mor "Here it is!"
    mc "*Whispering* Do you remember the way out?"
    p "*Whispering* We took a right, then left, another left, down the stairs, followed by a right, straight ahead, left, and finally, another right."
    mc "*Whispering* God bless your memory."
    play sound4 leather
    show fv 38
    mor "*Bowing gracefully* Please, wait here. Lord Iliescu will meet you shortly."with dis12
    mc "Of course... thank you, Mortimer."
    mor "I live to serve."
    show fv 39 with dis2
    p "*Walking into the room* Wow, it's so humid in here." with dis
    mc "*Shivers* And bone-chillingly cold."
    mc "I've gotta say, if I were to imagine the dwelling of a vampire... it would look exactly like this."
    play sound clothes3
    show fv 40
    p "*Sitting on the altar* Really?" with dis12
    show fv 41
    mc "Wouldn't you?"
    show fv 40
    p "I don't know, I kind of pictured it more like a grand castle."
    p "Elegant attires, baroque decor, an air of opulence draping every corner... like in Interview with a Vampire, you know?"
    show fv 41
    mc "Mmmm, yeah, Mortimer isn't exactly Brad Pitt."
    show fv 40
    p "*Laughs* Yeah, he's not."
    p "Although he does have his charm."
    show fv 41
    mc "*Laughs* He does."
    show fv 40
    p "I wonder if–"
    stop soundloop2
    play sound smokebomb
    play sound3 steam2 volume 0.7 
    play sound7 jumpscare3b volume 0.66
    play music wvvball0 fadein 10
    show iliescuappear
    p "{sc=2}AAAAARGGHHHH!!{/sc}" with hpunchlong4
    p "WHAT THE FUCK?!" with hpunch
    mc "*Getting into attack position* Watch out!" with hpunch
    play sound2 jump2
    play sound4 sword3
    scene fv 43
    p "*Standing up with a jump* You son of a bitch!" with dis
    p "Who are you?!"
    p "Was this a trap?"
    p "Speak before we kill you!"with hpunch 
    play sound5 debris
    scene fv 44
    ili "*Shaking off the dust from his clothes* I-I'm sorry, I apologize." with dis14
    ili "It's just that... it's been so long since we last had visitors that I kind of forgot how to make a proper introduction."
    show fv 45
    ili "*Clears throat* Pleased to meet you, travelers." with dis
    ili "I am Lazarus Iliescu, sovereign of Stravenovia... at your service."
    show fv 43
    p "*Catching her breath* You're... Lord Iliescu?"
    show fv 45
    ili "Since the day I was born."
    show fv 46
    mc "You sure made quite an entrance..."
    mc "Um... we're [mc] and Penelope."
    mc "Nice to meet you."
    show fv 45
    ili "It feels refreshing to engage in conversation with someone other than Mortimer and my wife Lysa..."
    show fv 47
    ili "Oh... I almost forgot. Lysandra? Where are you, my dear?" with dis14
    ili "We have guests."
    mc "It's not necessary, really, we just–"
    play sound3 debris
    play sound7 sniff3
    show fv 48
    ili2 "*Sniffing* Aaaaahhh... yeeeesss... I could smell them outside the crypt..." with dis12
    mct "Where the hell did she come from...?"
    play sound jump2
    play sound2 debris3
    play sound4 sniff
    scene fv49
    ili2 "*Sniffing* They smell... wonderfully indeed..."  
    mct "D-Damn, she's fast as fuck."
    scene fv 50
    ili2 "Look at this human, Lazarus."
    ili2 "So... strong..."
    play sound3 sniff3
    show fv 49
    ili2 "*Sniffing* So... virile."
    show fv 51
    mc "Um... thank you, ma'am."
    show fv 50
    ili2 "Y-You would make an exceptional vampire, young man."
    ili2 "Have you ever considered it?"
    show fv 51
    mc "Erm..."
    show fv 50
    ili2 "Once we manage to break this c-curse, it'll only have benefits! YES!"
    ili2 "Immortality, eternal youth, superhuman might, and access to carnal pleasures beyond mortal imagining."
    show fv 51
    mc "Well, when you put it that way, it does sound... intriguing, for sure."
    ili2 "Mm-hmm..."
    show fv 50
    ili2 "Have you ever had your blood suctioned from your erect member?"
    show fv 51
    mc "I... haven't had the pleasure, no."
    show fv 50
    ili2 "This is your chance, boy."
    show fv 51
    mc "Uh..."
    p "[mc]...?"
    play sound jump2
    play sound2 debris3
    play sound6 bodycollide2
    scene fv52
    ili2 "And... oh, my DEAR, look at this woman!"with hpunch
    play sound3 sniff3
    ili2 "*Sniffing* As s-splendorous as him!"
    scene fv 53
    p "Um..."
    scene fv 52
    ili2 "We must convert them..."
    ili2 "What a mammate specimen! Just smell this bosom!"
    ili2 "These precious, rounded vessels full of {b}blood{/b}..."
    ili2 "Have you ever seen breasts of this size, Lazarus?"
    play sound4 sniff3
    ili2 "*Sniffing* Aaahhhh... the muliebrity..."
    show fv 53
    p "C-Could you please... stop sniffing my chest, ma'am?"
    play sound jump2
    play sound2 debris3
    scene fv52b
    ili2 "*Returning to Lord Iliescu's side* O-Of course, of course!" with hpunch 
    ili2 "W-Where are my manners!"
    ili2 "*Sinister giggle* W-W-Welcome to our castle, [mc]ov and... Popolina."
    scene fv55
    ili "I'm afraid you'll have to excuse my wife's behavior, she's been feeling rather... peculiar as of late."
    scene fv56
    mc "Y-Yeah, we noticed."
    scene fv55
    ili "This is not her usual self, I assure you."
    scene fv 57
    ili "It's all because of this damn curse."with dis 
    show fv 61
    p "A curse?"
    p "So... you weren't always vampires?"
    scene fv55
    ili "Oh, no, not that."
    ili "We come from a proud lineage of Strigoi. Our entire people, in fact."
    scene fv 54
    ili2 "Everything was harmonious when we lived in idyllic Stravenovia."
    ili2 "There were only feasts, and parties..."
    ili2 "Ah, the parties..."
    scene fv55
    ili "Until one day..."
    ili "Something changed. One by one, our entire kin began to transform into these... creatures you saw outside."
    ili "Now, only we remain."
    scene fv 61
    p "*Gasps* Those monsters outside are... your people?"
    scene fv55
    ili "What's left of them."
    ili "They begin by exhibiting erratic behavior. Their thirst increases dramatically. Finally, they become the mindless creatures you encountered."
    ili "Only Mortimer managed to maintain his sanity after the process was complete."
    ili "The others would be little more than animals if not for my ability to control them."
    scene fv 61
    p "You can control them all at will?"
    scene fv55
    ili "I can. I gave them orders to guard the cemetery from outsiders while we remain here."
    scene fv56
    mc "So, your wife..."
    scene fv55
    ili "Yes."
    ili "The initial stages of the transformation have already begun."
    scene fv 57
    ili "That's why we traveled so far from our homeland." with dis 
    ili "I will find a way to break this curse before it's too late."
    ili "I WILL {b}NOT{/b} LET MY WIFE BECOME ONE OF THOSE VOMITIVE AND HORRENDOUS MONSTROSITIES!"with hpunch
    scene fv 58
    ili "No offense, Mortimer."with dis
    scene fv 59
    mor "None taken, sir."
    mor "I'm as ugly as the devil permits."
    scene fv55
    ili "So... yeah, this is our story."
    ili "What about you, though?"
    ili "What brought you to our abode?"
    scene fv56
    mc "Um..."
    mct "It's probably best we avoid mentioning we actually came to hunt them down..."
    mct "Still might be a good chance to get some info about what made all NPCs go rogue in this area, though."
    mc "We... we're simply passing through, to be honest."
    mc "We're investigating something that affected the people in this area."
    mc "Some kind of... magic. Probably."
    scene fv55
    ili "In that case, I can certainly be of assistance."
    scene fv56
    mc "Huh...? Can you?"
    scene fv55
    ili "My lineage has been amassing knowledge from both the earthly and astral realms for millennia."
    ili "Whatever questions you have, I'm confident we can assist. Though, I will ask for your assistance in return."
    scene fv56
    mct "The astral realm, he said...?"
    mct "Hmm, maybe he knows more about the nature of Eternum than I initially thought."
    mc "Very well. In that case..."
    scene fv55
    ili "Hold on a moment."
    ili "I will gladly answer all your inquiries, but first, I must explicitize my request."
    scene fv56
    mc "Ah, I should have seen this coming..."
    scene fv55
    ili "It's simple enough."
    ili "I'd like you to help me heal my wife."
    scene fv56
    mc "And how am I supposed to do that?"
    scene fv55
    ili "All we ask for... is a waltz dance."
    scene fv 61
    p "A... waltz dance?"
    scene fv 60
    ili "You see, before all of our people turned into monsters, we used to host big masquerade parties at our grand castle."
    scene fv55
    ili "The ballroom dances were my wife's most cherished pastime, and she sorely misses them."
    scene fv 54
    ili2 "*Imitating the sound of a violin* Tarara... nanana... nino..."
    scene fv55
    ili "Maybe... remembering the life we once knew... will stop, or at least slow down my wife's transformation."
    ili "So, if you would grant us one last dance for us to witness and reminisce... I will assist you in every way I can."
    ili "That's all we ask for."
    scene fv56
    if penelopepath:
        menu:
            with dis
            "[gr]Accept":
                mc "So... we just have to dance?" with dis06
                $ pennywaltzdance = True
            "Refuse":
                mct "Yeah, no chance I'm dancing in front of these people." with dis06
                mct "We have better things to do."
                mc "Um... well, I'd gladly accept, but Penelope twisted her ankle earlier."
                scene fv 61b
                p "Did I...?"
                scene fv56
                mc "Yes. Severely."
                mc "So... yeah, it won't be possible, I'm afraid."
                scene fv55
    else:
        mc "So... we just have to dance?"
    if pennywaltzdance:
        mc "I'm not {i}entirely{/i} confident in my waltzing abilities."
        scene fv 60
        ili "Don't worry about that, just let the music guide you and your wife."
        menu:
            with dis 
            "Alright":
                mc "Hmm... well, alright then, seems fair." with dis06
                mc "Let's do it."
                show fv 63
                p "W-What...?" with dis06
                p "Are we really doing this? Are you serious?"
            "She's not my wife":
                mc "Uhh... well, she's not my wife, but... alright, let's do it." with dis06
                show fv 63
                p "W-What...?" with dis06
                p "Are we really doing this? Are you serious?"
            "She's not my wife, yet [penelope_pts]":
                mc "Well, she's not my wife {i}yet{/i}, but... alright, let's do it." with dis06
                $ penelope_points += 1
                play sound beat
                show screen heartbeat
                show fv 63
                p "W-What...?" with dis06
                p "What did you just say...?"
                show fv 64
                mc "It can't be that hard, can it? It's worth a try!"
                show fv 63
                p "N-No, not the dance, I mean the..."
                show fv 64
                mc "Hmm?"
                show fv 63
                p "Um..."
                p "N-Nevermind. Um... so... are we really doing this?"
        show fv 64
        mc "Yeah, why not? It'll be fun!"
        show fv 63
        p "Do you even have any clue about what you're supposed to do?"
        show fv 64
        mc "*Chuckles* Of course! Trust me."
        mc "And hey, this is my long-awaited opportunity to repay you with the dance I owe you."
        show fv 63
        p "Huh."
        p "Well... if you insist."
        show fv55
        ili "Delightful!"
        ili "Let's begin, then."
        stop music fadeout 8
        play soundloop cave fadein 6
        scene fv 58
        ili "Now, where are the musicians..." with dis08
        ili "Gentlemen, could you play some waltz music?"
        scene fv 64b
        ili "Perhaps something from..."
        mc "What the..."
        ili "Strauss? Tchaikovsky?"
        ili "Any suggestions?"
        scene fv 59
        mor "Shostakovich?"
        ili "Ah, excellent choice, Mortimer. A true classic."
        show fv 64b
        ili "Yes, let's play the Waltz No. 2."
        ili "One, two..."
        ili "One, two, three, and..."
        play music wvvball1 fadein 2
        stop soundloop fadeout 9
        scene fv 64
        bla "The vampiric musicians begin to play with surprising skill." with dis15
        mc "*Chuckles* (This whole situation is surreal.)"
        scene fv 65
        mc "*Extending your hand* My lady." with dis12
        show fv 66
        bla "Penelope reaches for your hand, a hint of uncertainty and bashfulness still lingering in her eyes."with dis14
        mc "The key is to just let yourself go."
        p "Mm-hm."
        mc "Like this."
        play sound2 jump2
        play sound3 debris3
        scene pennydancetran
        pause 0.05
        scene pennydance07 with Dissolve(.15)
        pause 1
        p "Oh my.{w=2.4}{nw}" with dis 
        play sound7 clothes3
        scene fv 67
        bla "You deftly lift Penelope to an upright position, bringing her body as near to you as possible until you can feel her heartbeat through her bust." with dis15
        p "Where... where did you learn these moves?"
        mc "Honestly, I'm not sure."
        p "You're not sure?"
        mc "It's... Eternum."
        p "Eternum? What do you mean?"
        mc "Sometimes I feel like I can ace pretty much everything I try to do here."
        mc "Or learn it incredibly fast."
        scene fv 71
        mc "*Dancing with her* It's like... like I was connected to it, you know?" with dis15
        mc "As if I had learned how to waltz in another life, for instance."
        scene fv 69
        p "Well, you won't see me complaining." with dis15
        p "Looks like in that past life you were quite the dancer."
        scene fv 68
        mc "Or... maybe it's just the enchanting company that's fueling my inspiration. Who's to say?" with dis15
        p "Mm-hm..."
        p "*Giggles* Or maybe you’ve just been practicing in secret for the dance you owed me?"
        scene pennywaltz
        bla "You and Penelope continue dancing synchronously, the music guiding your steps like a conductor leading an orchestra through a symphony." with dis2
        bla "For a moment, everything else fades away."
        bla "No Gems of Doom, no looming threats, no spirits trapped in Eternum – just you... and her. The breaths, the sighs, and the desire between the two of you fill the little space between your shared sensuous movements."
        scene fv 68
        mc "You know..." with dis2
        mc "There's something I've been meaning to ask, Penny."
        p "Hmm?"
        mc "Are we..."
        p "Hmmmm...?"
        mc "Do you want to maybe..."
        play sound musicstop
        stop music
        play soundloop cave
        play music wvvball0 fadein 7
        show fv 67
        ili2 "BRAVO!"with hpunch  
        play sound2 clappingfast volume 0.8
        scene fv72
        ili2 "That was absolutely enchanting!"
        ili2 "Exquisite!"
        mct "Damn, I almost forgot we had an audience."
        ili2 "It was quite an unconventional dance... but beautiful nonetheless!"
        scene fv 63
        p "*Clears throat* T-Thank you."with dis12
        scene fv 64
        mct "I wonder if Penny felt the same way..."
        scene fv 72
        ili2 "You really took me back home with this!"
        ili2 "For a moment, your terpsichorean movements transported me back to Romania! Bravo!"
        mct "Romania...?"
        scene fv 63
        p "G-Glad you liked it. I suppose."
        scene fv 74
        ili "I must echo my wife's sentiment, [mc]."with dis12
        ili "You both danced with remarkable finesse." 
        scene fv 75
        mc "Thank you, sir."
        scene fv 74
        ili "You may go now, carrying my eternal gratitude."
        ili "But before you leave... you mentioned you had questions before, so feel free to ask."
    elif not penelopepath:
        scene fv 61b
        p "Uh... yeah, that's not gonna be possible."
        p "I... kind of twisted my ankle, so no dances for me, I'm afraid."
        scene fv 60
    if not pennywaltzdance: 
        ili "Oh... that is... unfortunate."
        ili "Very unfortunate."
        scene fv 72
        ili2 "C-Can I get a piece of clothing from you, then?" with dis 
        scene fv 61
        p "Clothing?"
        scene fv 72 
        ili2 "Yes!"
        ili2 "The scent takes me back home!"
        ili2 "It reminds me of the maids I used to have back in Romania!"
        mct "Romania...?"
        ili2 "Now that they have all transformed into monsters, I can no longer smell those aromas!"
        scene fv 61
        p "I mean... yeah, sure, I don't see why not."
        scene fv 72
        ili2 "Sweeeet!"
        ili2 "Tell them whatever they want to know, Lazarus."
        scene fv 74
        ili "Well... that will do for now, I suppose." with dis 
        ili "But you and your... {i}companion{/i} still owe us a dance."
        ili "Can I trust you'll return once her ankle has healed?"
        scene fv 75
        mc "You have my word."
        mct "It's not lying if we don't know for sure."
        ili "Hmm."
        show fv 74
        ili "Very well, then."
        ili "You can ask your questions before you leave."
    ili "I'll respond as honestly as I'm able."
    show fv 75
    mc "I appreciate it."
    mct "Mmm, I should get straight to the point."
    mct "Luna must be already waiting for us."
    mc "Okay..."
label menuvampirequestions:
    if not vquest1 and not vquest2 and not vquest3:
        mc "Well, I'd love to stay and continue asking you questions, but we really must be on our way now."
        jump postmenuvampire
    menu:
        with dis
        "[gr]What does being a vampire entail?" if vquest1:
            $ vquest1 = False
            mc "I've often wondered, what exactly does being a vampire entail?" with dis06 
            mc "Like, can you turn into a bat? Do you die if sunlight touches you?"
            show fv 74
            ili "*Chuckles* Ah, the old tales."
            ili "It's true that we don't age and we need blood to survive, but I'm afraid most of what you've heard are just stories meant to frighten children."
            show fv 76
            ili "We can't transform into bats, and while it's true that sunlight ends up turning us into ashes, it doesn't instantly kill us."with dis
            show fv 74
            ili "I don't sleep in a coffin, but in a large bed with my wife. And yes, we can see our reflections in mirrors."with dis
            show fv 77
            ili "As for peculiar items like human crucifixes, they can't harm or scare us more than a common blade. In fact, I use one as a bookend."with dis
            show fv 78
            ili "*Chuckles* And my personal favorite: for some reason, there's this belief that garlic can repel or harm us."with dis12
            play sound4 whoosh6 volume 0.5
            show fv 79 
            ili "Aaah..." with dis08
            play sound7 bite2
            play sound ["<silence 0.7>", eat] 
            show fv 80 with dis15
            ili "*Munching on the garlic* Mmmm..."with dis
            play sound2 swallow
            play sound swallow
            show fv 75
            ili "*Swallows* ..."with dis08
            show fv 74
            ili "As you can see, that's completely absurd."
            show fv 75
            mc "Did you..."
            mc "Did you just eat a whole head of garlic unpeeled?"
            show fv 74
            ili "Yes, it was disgusting."
            ili "But I wanted to make a point."
            show fv 75 
            mc "Fair enough."
            jump menuvampirequestions
        "[gr]What do you remember about your past?" if vquest2:
            $ vquest2 = False
            mc "What do you remember about your past?" with dis06
            mc "Before arriving here."
            show fv 74
            ili "Well, as I mentioned, we spent all our lives in Stravenovia, in the Eastern parts of the continent."
            show fv 75
            mc "And what about... Romania?"
            mc "Your wife mentioned it earlier."
            show fv 81
            ili "Romania...?"with dis
            ili "I've never heard that name in my life, no."
            show fv 82
            mc "Do you know what “Eternum” is? Or Ulysses? Or things like... Europe, Asia, or America?"
            show fv 81
            ili "Uhh... no, I'm not familiar with those terms, I'm sorry."
            show fv 74
            ili "Despite living for millennia, we've never left Ekabar."with dis
            ili "Not even we know what lies beyond the great seas."
            show fv 75
            mc "No worries..."
            mct "His wife definitely mentioned Romania. I heard it. Shit, now that I think about it, they even brought up actual composers from the real world!"
            mct "Could their actual memories be intertwined with the false ones they acquired when they became NPCs?"
            mct "Perhaps that's the trigger that can “free” them from Ulysses' control?"
            mct "I’ll need to note that down for later..."
            jump menuvampirequestions
        "[gr]What's your current relationship with the town of Hollowbrook?" if vquest3:
            $ vquest3 = False
            mc "What's your current relationship with the town of Hollowbrook?" with dis06
            show fv 74
            ili "It's... not the best."
            ili "Their hunters started targeting us without any provocation."
            ili "We sustain ourselves on the blood of animals, and we never enter settlements unless it's strictly necessary."
            ili "However, after they began massacring us... I had to take action."
            ili "These creatures might be mindless monsters now, but they were once my people. I will not stand idly by while they are slaughtered."
            show fv 75
            mc "Understandable."
            mct "I wonder what started this surge of erratic behavior among the NPCs."
            mct "Did the hunters go rogue first? Or perhaps it was the vampires?"
            mct "Hmm..."
            jump menuvampirequestions
        "Leave":
            mc "Well, I'd love to stay and continue asking you questions, but we really must be on our way now." with dis08
label postmenuvampire:
    mc "I hope we can continue our conversation sometime."
    show fv 74
    ili "Very well."
    ili "It was a pleasure meeting you, Lord [mc]."
    ili "I also hope we have the chance to meet again in the future."
    show fv 72
    ili2 "Thank you for the visit!"
    ili2 "And don't hesitate to return! We don't b-bite, I swear!"
    show fv 75
    mc "Oh, and by the way..."with dis
    menu:
        with dis
        "Side with the hunters\n[mt](Hunters allies)":
            mc "If you truly wish to aid your wife, Hollowbrook is your best bet."with dis06
            mc "We crossed paths with the hunters upon our arrival, and they were leaving the town for good."
            mc "Now only a handful of civilians remain, and among them there's a healer. Perhaps she can provide some assistance."
            mct "Hopefully this will lead to a truce and to us becoming friends with the hunters of Hollowbrook."
            show fv 45
            ili "Oh, that's excellent news."
            ili "We'll pay them a visit soon, then."
        "Side with the vampires\n[gr][mt](Vampires allies)":
            $ vampiresside = True
            mc "We passed through Hollowbrook on our way here, and I can tell you the hunters have lost all reason."with dis06
            mc "They believe you're all malevolent creatures that must be eradicated."
            mc "If you wish to help your wife, you'd be better off far from that town of lunatics."
            show fv 45
            ili "Thanks for the advice, we'll stay away from it."
            ili "Unfounded fear is something we're accustomed to."
    ili "Thanks again for your help, [mc]."        
    show fv 46
    mc "No problem."
    show fv 45
    ili "Mortimer will escort you to the exit."
    show fv 59
    mor "With pleasure!"
    if penelopepath:
        mor "Stick close, you two lovebirds, unless you fancy becoming dinner for giant tarantulas!"
    else:
        mor "Stick close, unless you fancy becoming dinner for giant tarantulas!"
    mc "W-We're right behind you!"
    if mod_vamp_wolf:
        scene black with fade
        $ vampireshelp = False
        jump werewolfhelpm
    jump poswerevamp


label werewolveslabel:
    play soundloop night2 fadein 9
    hide screen sometimelater
    scene fw 1
    with dis25
    play sound6 wind4 volume 0.7 fadein 3
    bla "After walking through the woods for a while, you finally come across the ruins of an old fortress." with dis17
    play sound2 footsteps3 fadein 2
    show fw 2 with dis2
    stop sound2 fadeout 1
    play sound3 ["<silence 0.4>", whistle3]
    mc "*Whistles* (Damn, look at this castle.)" with dis
    mct "I mean, it's clear it's seen better days, but its former glory still shines through."
    mct "I wonder if Luna also found this place. Without the {i}Lumina{/i} spell she taught me, I would have been completely lost in these woods."
    mc "*Scanning the surroundings* (Hmm...)"
    mct "There's something off about this place, though."
    show fw 3
    mct "There are lit torches everywhere, so this can't be the monsters' hideout – there have to be humans nearby."
    mct "Also, there seem to be... chests scattered around?"
    mct "It almost looks like they were begging me to plunder their content."
    show fw 4
    mct "Looks like a classic, basic trap, if you ask me."
    mct "Probably bandits waiting to catch unsuspecting travelers on the road."
    mct "A single path through the valley, all surrounded by towering structures."
    mct "Yep, perfect for an ambush."
    show fw 5
    mct "Furthermore, the main wall and its gate are still in pretty good condition, which would make a hypothetical attack easy to defend."
    mct "The whole place is simply too quiet not to be a trap..."
    mct "Damn it, could Luna have fallen victim to this place?"
    mct "What if the bandits have taken her captive?!"
    show fw 6
    mct "Fuck... there are dozens of doors in the main courtyard. Could they have stashed her inside?"
    mct "Or... perhaps she was captured and taken elsewhere...?"
    mct "FUCK! This place is too big, I'll never find her!"with hpunch
    mct "Goddamn it, what should I do..."
    show fw 7
    mct "Okay... let's calm down and think this through." with dis14
    mct "Luna might seem adorable, but she's actually quite powerful."
    mct "She wouldn't have let herself be captured without a fight."
    mct "I'll go down there and try to spot any signs of–"
    l "[mc]?"
    play sound2 clotheswhoosh
    play sound debris
    play soundlow rocks volume 0.4
    show fw 8
    mc "NN-NAAAA-NAA!{w=0.26}{nw}" with hpunch
    mc "S-SU-GGL!{w=0.26}{nw}" with hpunch
    mc "NN-NAAAA-NAA!{w=0.26}{nw}" with hpunch
    mc "S-SU-GGL!{w=0.26}{nw}" with hpunch
    play music shenanigans fadein 5
    mc "G-G-GHJ-HW-WHAT?!" with hpunch
    mc "Wha..."
    mc "L-Luna?"
    show fw 10
    mc "Oh Jesus, you're okay! Thank goodness!" with dis12
    mc "How did you manage to escape from the bandits?!"
    show fw 9
    l "Bandits...?"
    l "What bandits?"
    show fw 10
    mc "Um..."
    mc "*Clears throat* Y-Yeah, for some reason I assumed you'd been captured by a group of thugs. I'm not sure why."
    mc "But in any case, I'm relieved to see you're alright!"
    show fw 11
    l "Thanks! I'm glad to see you too!"
    show fw 10
    mc "How did you find me so fast?"
    show fw 9
    l "Well, you're... quite noisy."
    l "And the Lumina spell you cast can actually be spotted from a mile away."
    show fw 10
    mc "Oh. Y-Yeah, that's fair."
    mc "I definitely can't say the same about you, you’re quieter than a black cat on a moonlit rooftop."
    if lunapath:
        show fw 9
        l "But why are you here?"
        l "I thought you were supposed to stay in Hollowbrook."
        show fw 10
        menu:
            with dis
            "I was bored":
                mc "I know, but I got bored and thought I would come your way to see those werewolves."with dissolve
            "I missed you [luna_pts]":
                mc "I know, but I was missing you, so I decided to come your way."with dissolve
                mc "I don't know, playing Eternum without you isn't the same."
                $ luna_points += 1
                play sound beat
                show screen heartbeat
                scene fw 12
                l "Oh... thank you."with dis15
                l "I... miss you too when you're not around."
                show fw 13
                mc "*Chuckles* The feeling is definitely mutual."
                show fw 12
                l "Sorry if I've been more distant lately. Between my dad's cafe and the upcoming exams, I've barely had any free time."
                show fw 13
                mc "No worries! Both Annie and Dalia have been hitting the books like crazy too, whenever they weren't in Eternum."
                show fw 12
                l "I should have more chill time once these exams are over."
                l "We can hang out more then."
                l "If you want."
                show fw 13
                mc "I'd love to!"
                show fw 12
                l "Cool."
                l "I'll text you."
                show fw 13
                mc "Looking forward to it!"
                show fw 12
                l "But anyway, let's focus on the werewolves for now."
                show fw 13
                mc "Oh, for sure. Can't wait to face off against a real werewolf!"
            "I thought you'd need the help":
                mc "I know, but then I thought you'd be in danger on your own, so I came your way to lend a hand."with dissolve
                show fw 9
                l "Oh... thank you."
                l "Although I should be alright."
                l "I've faced tougher things in Eternum."
                show fw 10
                mc "Have you ever run into a werewolf in Ekabar before?"
                show fw 9
                l "I haven't, but I've heard some tales."
                show fw 10
                mc "They've always struck me as intriguing."
                mc "But, I imagine they must be quite terrifying."
    else:
        show fw 10
        mc "I got bored in Hollowbrook, so I decided to come your way to see those werewolves."
    mc "Well... if they're even real."
    mc "I mean, I haven't really seen anything strange on my way here, have you?"
    mc "Maybe there are no vampires either... maybe it's all part of a collective hysteria, stories spun from too much mead and wild imaginations."
    play soundlow debris fadein 1
    show fw 14
    l "*Moving in closer* Well, there {i}is{/i} something, of that I'm sure." with dis15
    l "Even if it's not werewolves, there's definitely some big stuff roaming around here."
    l "Do you see that courtyard?"
    mc "Yeah, I was looking at it before."
    l "I sent the owl I summoned to do a quick flyby, and it reported back some seriously hefty footprints over there."
    show fw 15
    mc "Hmm... well, we can't really leave without investigating the area, so... there's only one way to go, if you ask me." with dis
    mc "Let's make our way to the courtyard and then back to Hollowbrook? Reaching this place took me longer than expected."
    mc "Penny might be on her way back too."
    show fw 14
    l "Sounds good."with dis
    l "Just be careful when descending this wall, the rocks are quite slippery."
    mc "Gotcha."
    stop music fadeout 9
    play soundlow debris2
    show fw 4 with dis25
    play sound5 debris3 volume 0.6
    play sound6 wind4 volume 0.5 fadein 5
    bla "You and Luna carefully climb down the steep slope that leads to the fortress entrance." with dis14
    l "This place is so quiet."
    mc "Yeah, and that freaks me out so much..."
    mc "Keep an eye out."
    play sound footsteps3 fadein 2
    show fw 16 with dis25
    bla "You make your way to the courtyard you spotted earlier, yet you encounter nothing but dust, and silence." with dis12
    l "Nothing."
    l "Perhaps the werewolves are gone for good?"
    mc "Or maybe they were captured by a group of poachers."
    mc "And then abandoned."
    l "Could be."
    play sound branch
    bla "You hear a noise coming from behind you."
    play sound2 whoosh6
    play soundloop2 deception
    show fw19b 
    mc "H-Hey!" with hpunch
    l "What happened?"
    mc "I... I heard something."
    l "Maybe the wind?"
    mc "No..."
    mc "We're not alone here..."
    l "*Pointing at the door* Let's check inside." 
    scene fw 17
    mc "Inside? Are you sure?" with Dissolve(1.9)
    l "Yes."
    l "If there are really monsters here... there's something I need to see." 
    mc "*Gulps* Alright then... but stay close."
    mc "We don't know what kinds of traps we might find."
    play sound were1
    show fw 18 with dis17
    wer ". . ." with dis12
    play sound3 howl2
    play sound4 howl2
    show fw 19 
    wer "*Howls*" with dis2
    play music tensionhorror fadein 5
    show fw 16
    mc "D-Did you hear that? It sounded way closer this time."with dis17
    l "Definitely..."
    mc "Let's get out of here, it's not worth staying here just to win favor with the hunters."
    mc "Follow m–"
    stop soundloop2
    play sound5 rocks
    play sound6 monsterbreath2
    play sound2 whoosh6
    play sound7 steam3
    play sound8 debris2 
    scene fw 20
    bla "As you turn around, a colossal creature almost the size of a car plummets from the stone arch above." with dis22
    play sound4 were1
    scene fw 21
    mc "H-Holy shit, THAT is big..." with dis17
    l "[mc]...?"
    play sound3 footstepsmonster
    show fw 22 with dis2
    play sound were1
    bla "Another werewolf, as big as the first one, appears on the other side of the courtyard, blocking the only two possible exits." with dis17
    mc "F-Fuck..."
    play sound4 sword
    play sound5 debris3
    scene fw 23 with dis12
    play sound4 monsterbreath2
    mc "W-Well, looks like the rumors were true after all..." with dis
    mc "Um..."
    mc "Can you... understand my words?"
    mc "We mean you no harm. We can leave as quietly as we arrived."
    play sound3 were1
    bla "The creature looks at you menacingly, growling and arching its back."
    play soundloop2 beat2 fadein 2
    play sound transformpower fadein 1
    scene fw 24
    mc "So you're nothing but mindless animals? Fine." with dis15
    mc "Let's see who's faster, you monsters."
    mct "I need to find a way to defend myself while ensuring Luna's safety."
    mct "She's my priority, even if it means..."
    l "Wait!"
    show fw 25
    mc "Huh?"
    show fw 26
    l "Don't attack them!"
    show fw 25
    mc "What? Why not?"
    show fw 26
    l "They won't harm us if we don't provoke them."
    show fw 25
    mc "W-What?"
    mc "How are you so sure?"
    show fw 26
    l "Trust me!"
    show fw 21
    mc "*Observing the beast* Um..." with dis12
    mc "I've seen enough National Geographic documentaries to know that's not a friendly stance, Luna."
    show fw 26
    l "Please, don't attack them!"
    l "And don't speak!"
    l "You have to trust me!"
    show fw 25
    mc "Uh..."
    mc "O-Okay, I trust you."
    mc "I hope we don't regret this..."
    play sound were1
    play sound2 debris
    show fw 27 
    bla "The werewolf in front of Luna takes a small step, preparing to attack." with dis2
    play sound3 were2
    wer2 ". {w=0.25}. {w=0.25}.{w=0.25}{nw}"
    play sound4 whoosh6
    play sound5 debris3
    scene wereroar
    wer2 "{sc=2}*Roars*{/sc}{w=4.2}{nw}" with hpunchlong6
    play sound6 were1 
    scene fw 29
    wer2 ". . ." with dis15
    l ". . ."
    play sound7 were2
    pause .2
    scene fw 28 with Dissolve(0.7)
    wer2 "{sc=2}*Roars*{/sc}{w=4.2}{nw}" with hpunchlong6
    play sound were1 
    scene fw 29
    wer2 ". . ." with dis15
    scene fw 30
    wer2 ". . ." with dis17
    play sound2 monsterbreath2
    show fw 31
    wer2 "*Looking at the other werewolf* . . ." with dis15
    show fw 32
    wer ". . ."
    scene werenod
    wer "*Nods*"
    scene fw 31
    wer2 ". . ."
    play sound7 were2
    scene fw 30 with Dissolve(0.6)
    scene fw 34 with dis03
    wer2 "{sc=2}*Roars*{/sc}{w=4.2}{nw}" with hpunchlong6
    play sound were1 
    scene fw 30
    wer2 ". . ." with dis15
    l ". . ."
    play sound2 risingshort4
    wer2 ". {w=0.9}. {w=0.9}.{w=0.9}{nw}"
    stop music fadeout 1
    stop soundloop2 fadeout 1
    wer2 "Hmph."
    play musicb quirky7 volume 0.8
    scene fw 35
    wer2 "Um..." with dis12
    wer2 "Dude, she's not reacting."
    mct "What in the..."
    wer2 "Why is she not reacting?"
    show fw 36
    wer "Are you asking me?"
    show fw 35
    wer2 "No, I'm asking the mushroom behind you."
    wer2 "Of course I'm asking you, dumbshit."
    wer2 "What are we supposed to do now?"
    show fw 36
    wer "Eh..."
    wer "I-I don't know, usually everyone's run away by this point."
    show fw 35
    wer2 "What did the guard orientation handbook say?"
    show fw 36
    wer "Um... I'm not sure, I haven't finished reading it yet."
    show fw 35
    wer2 "Duuude..."
    show fw 36
    wer "Don't give me that look, you know how much Fangrend likes to over-explain everything."
    wer "That thing has like... a hundred pages."
    wer "He literally weaves in a childhood story that spans three chapters just to explain night shifts."
    show fw 35
    wer2 "*Cheeky laugh* Yeah, the one about the rice fields, right?"
    show fw 37
    l "Hi!"
    play sound whoosh7
    play sound2 leaves2
    scene fw19bb
    wer2 "*Backing off* WHAT THE HELL?! SHE CAN SPEAK!" with hpunch 
    scene fw 36
    wer "Of course she can speak, nitwit."
    wer "She's a human, humans can talk."
    play sound3 footstepsmonstershort volume 0.8
    scene fw 35
    wer2 "Ah, yeah, that makes sense."with dis15
    show fw 36
    wer "And didn't you hear them chatting just a minute ago?"
    show fw 35
    wer2 "I didn't, no." 
    wer2 "Still got my ears clogged from our last swim."
    show fw 36
    wer "Again? That's why I always tell you to bring earplugs, dude."
    show fw 35
    wer2 "{i}Alright, Mom."
    wer2 "{i}I'll grab my jacket next time too."
    play sound footstepsmonster
    show fw 39 with Dissolve(2.4)
    bla "The two creatures step back a few paces, assuming a relaxed stance before you and Luna."with dis14
    show fw 40
    wer2 "*Clears throat* Erm... well, this is awkward."
    duk "Uh... hello."
    duk "My name's Duke, and my buddy here's Burpee."
    show fw 41
    l "I'm Luna! Nice to meet you guys."
    show fw 39
    mc "Yeah, and I'm... [mc]."
    mc "I have to admit, when I saw you I wasn't expecting you to be so... rational."
    show fw 40
    duk "And we didn't expect you to... do nothing. Like, at all."
    duk "Everyone usually just runs away."
    duk "Why didn't you?"
    show fw 41
    l "I had a hunch when I saw Duke cautiously walking to avoid stepping on that flower over there."
    show fw 42
    mc "A flower?"
    show fw 38b
    l "That one."
    l "He passed right over it, but he carefully stepped aside not to crush it."
    l "No mindless, wild animal would care about a simple flower."
    show fw 45
    duk "Ohh... she's clever."with dis
    show fw 44
    bur "Yeah, and you're dumb."
    bur "Why do you care about a shitty flower?"
    show fw 45
    duk "Maaaan, it just sprouted!"
    show fw 44
    bur "But why...? Do they taste good?"
    show fw 45
    duk "No."
    duk "It's about its beauty."
    show fw 44
    bur "Ahh..."
    bur "Yeah, forgot you're a weirdo."
    show fw 45
    duk "Shut up."
    show fw 41
    l "I think those flowers are beautiful."
    show fw 45
    duk "See? The pretty girl understands."
    show fw 41
    l "We mean you no harm, we promise you that."
    l "We're not here to cause trouble."
    show fw 40
    duk "That's good."
    duk "I don't enjoy tearing apart pretty things."
    duk "And you are pretty."
    duk "I like your eyes."
    show fw 41
    l "Aw, thank you so much! That’s very sweet of you, guys!"
    l "And you both have very cute ears!"
    show fw 44
    bur "*Cheeky laugh* Heheh, she said she likes our ears."
    show fw 45
    duk "Heh, she's so cute, isn't she?"
    show fw 44
    bur "She's adorable!"
    bur "Should we take her to Fangrend?"
    show fw 45
    duk "We should!"
    show fw 44
    bur "I wanna ask Betty if we can keep her!"
    show fw 45
    duk "Just be sure to keep her away from Tissle."
    duk "I like this girl's smell as it is."
    play sound wheezing volume 0.7
    show fw 46
    bur "*Wheeze laugh* HAHAHAH, I still can't believe he was sprayed by that skunk." with dis
    show fw 45
    duk "{i}“You guys are such wimps. Let the alpha deal with it.”"with dis
    play sound2 wheezing volume 0.7
    show fw 46
    bur "*Wheeze laugh* Hahahah, he's been smelling like shit for 4 days straight."with dis 
    bur "*Laughs* Had to be fucking Tis."
    show fw 40
    duk "*Clears throat* Sorry about that." with dis12
    duk "Yeah, we'd be happy to accompany you to meet our leader."
    duk "He's been itching for a chat with someone from outside the pack."
    duk "Things have been... complicated lately."
    show fw 42
    mc "Hmm... what do you think?"with dis
    show fw 43
    l "We should go for it!"
    l "They seem friendly."
    show fw 42
    mc "*Chuckles* Yeah, they do seem pretty funny, not gonna lie."
    mc "And... well, your hunch was definitely right before, so I’ll follow your lead."
    mc "Let's not take too long, though."
    mc "We're supposed to meet Penny back in Hollowbrook in 40 minutes."
    show fw 41
    l "How long will the visit take?"
    show fw 40
    duk "Um... no more than 15 minutes."
    duk "Just a quick stop, it won't..."
    play sound wheezing volume 0.7
    show fw 46
    bur "*Wheeze laugh* Hahahah dude, the face he made!" with dis12
    bur "S-Sorry, sorry, hahah, I remembered Tissle's incident again."
    show fw 44
    bur "Hahah...hah...o-okay, okay, *clears throat* I'm sorry."with dis 
    bur "Let's get back on track."
    show fw 40
    duk "...it won't eat up much of your time, promise." with dis12
    show fw 39
    mct "Hmm... it seems like they're actually genuinely good fellas after all."
    mct "At worst, I could activate my powers and take Luna to a safe place before they even realized what was happening."
    mc "Alright... let's meet him."
    mc "But we have to be back in Hollowbrook within 30 minutes."
    show fw 40
    duk "Cool, follow us then."
    show fw 39
    mc "Right behind you." 
    mct "Let's see what this leader can tell us..."
    stop musicb fadeout 9
    stop soundloop fadeout 9
    play soundloop2 fireplace fadein 6
    play sound2 footstepsmonster fadein 5
    scene fw 47 with dis3
    bla "Duke and Burpee guide you through a labyrinth of diverse corridors within the ruins, culminating in a more spacious room on the uppermost floor." with dis14
    duk "Alright, this is the place."
    duk "I'll let the rest of the pack know you're here."
    duk "I wouldn't want anyone to kill you by accident."
    mc "A-Appreciate it."
    play sound3 howl2
    play sound4 howl2
    show fw 48
    duk "*Howls*" with dis2
    mc "Are there many of you here?"
    mc "We didn't see anything when we–"
    play sound werewolvesappear
    play music ["<silence 6>"]
    queue music shenanigans  
    show fw 49 
    bla "Suddenly, dozens of werewolves materialize from every corner of the chamber, halting just before you with a curious gaze."with dis2
    mc "O-Okay."
    l "Wow!"
    show fw 50
    wer "Who are these people, Duke?"
    show fw 49
    duk "We found them on the road."
    play sound2 fall3
    show fw 51
    wer3 "WHAT?!" with hpunch 
    wer3 "You brought strangers into our lair, you idiot?!"
    wer3 "How do we know they're not enemies?!"
    show fw 54
    bur "It's alright, calm down, we have reasons to believe they're not hostile."
    show fw 51
    wer3 "They better be GOOD reasons!"
    show fw 54
    bur "They are!"
    show fw 55
    bur "Look at the girl." with dis
    bur "She's so cute."
    show fw 49
    wer3 ". . ."
    show fw 50
    wer3 "Okay, yeah, she's cute."
    show fw 52
    wer2 "Oof, I got scared for a moment."
    wer3 "Yeah, that was close."
    show fw 51
    wer "Oh my god, she's adorable!"
    show fw 57
    bur "Okay, let me introduce you to everyone." with dis 
    bur "The humans are Luna and [mc]."
    bur "And they are..."
    show fw 49
    bur "From left to right, Larry, Lupin, Biscuit, Bella, Pippin, Whisker, Happy, Flutter, Nimbus, Zigzag, Noodle, and Gizmo."
    l "Pleasure to meet you all!"
    mc "Y-Yeah, nice to meet you."
    mct "How the hell am I supposed to tell them apart...? They all look exactly the same."
    play sound footstepsmonstershort
    show fw 53 with dis15
    bet "*Feminine voice* Burpee...? What's going on here?" with dis08
    show fw 54
    bur "Ah, honey!"
    bur "Look at what I found!"
    show fw 55
    bur "This super cute human was lost on the road!" with dis 
    bur "Look at how tiny she is!"
    show fw 53
    bet "No."
    show fw 55
    bur "Her eyes remind me of..."
    show fw 54
    bur "Wait, what? I didn't even ask anything yet!"with dis
    show fw 53
    bet "We can't keep her."
    show fw 54
    bur "What?! Why not?"
    show fw 53
    bet "Because a human isn't a pet."
    bet "They have a lot of needs."
    show fw 54
    bur "But I'll take good care of her!"
    bur "I'll hunt food for her and take her for walks every day!"
    show fw 53
    bet "I said no, Burpee."
    show fw 56
    bur "Awwwhh..." with dis12
    bur "I'm sorry, Luna."
    show fw 58
    l "No worries, Burpee!"
    l "We can be friends anyway!"
    show fw 52
    larry "*Cheeky laugh* Looks like someone's wife has him on a tight leash."
    play sound3 debris3
    play sound4 fall3
    show fw 57
    bur "I heard that, Larry!" with hpunch
    play sound sniff3
    show fw 51
    nimbus "*Sniffing* Ugh, what's that smell...?"
    show fw 52
    larry "Oh god, not Tissle again..."
    show fw 52b
    wiggle "Oh, COME ON, guys!"
    wiggle "I don't smell anymore!"
    show fw 57
    bur "You're stinking up the place with your skunk stench, Tis!"
    bur "Go back to the river and get washed again!"
    show fw 52b
    wiggle "But the water is so cold!"
    show fw 52
    larry "He does have a point, that water is freezing."
    show fw 51
    nimbus "Yeah, one of the drawbacks of having short fur."
    show fw 52
    larry "Well, our northern cousins have long fur everywhere, but they get roasted during summer."
    larry "I don't know what's worse."
    show fw 51
    nimbus "But they look cooler, like... actual wolves."
    nimbus "We could pass as oversized Dobermans."
    show fw 52
    larry "I prefer to say we look like descendants of Anubis."
    mct "Anubis...?"
    show fw 51
    nimbus "What the fuck is an anubis?"
    show fw 52
    larry "The Egyptian deity, hello?"
    show fw 51
    nimbus "The what now?"
    show fw 57
    bur "Yeah, stop making things up, Larry."
    show fw 52
    larry "I'm not making anything up, you bunch of illiterates!"
    larry "Ask the pretty girl!"
    show fw 58
    l "He's actually right!"
    l "And I agree, you remind me of–"
    stop music fadeout 1
    play sound7 were2
    scene fw 59 with dis04
    scene fw 61 with dissolve
    fan "{sc=2}*Roars*{/sc}" with hpunchlong6
    play sound6 rocks
    scene fw 62
    fan "WHAT ARE YOU ALL DOING HERE?!" with hpunch
    fan "STOP SLACKING OFF AND GET BACK TO YOUR POSTS!"with hpunch 
    fan "NOW!" with hpunch 
    play sound werewolvesappear fadein 1
    show fw49 
    bla "The entire pack swiftly disengages, obediently following their leader's commands as they sprint out of the chamber."with dis2
    play sound footstepsmonster
    play music tensionhorror fadein 4
    scene fw 65 with dis27
    bla "Despite bearing the same appearance as his kin, Fangrend stands before you enveloped in an aura that renders him particularly daunting." with dis14
    play sound2 were1
    show fw 66
    fan "Duke...? Burpee?"
    fan "You let hunters into our sanctuary?" 
    show fw 56
    bur "W-What do you mean h-hunters...?"
    bur "Y-You're hunters?"
    show fw 65
    mc "We're not!"
    mc "We just–"
    show fw 66
    fan "LIES!" with hpunch 
    fan "You're dressed in their garb!"
    show fw 65
    mc "But we're not! It's all a ruse!"
    mc "We just came to these lands to investigate something, that's all!"
    show fw 66
    fan "Do you know how many of us have fallen to those murderers since the hunt began?"
    show fw 65
    mc "We're not a part of it, I swear."
    fan ". . ."
    fan "Hmph."
    show fw 66
    fan "I can hear your pulses, and they don’t indicate lies... so I'll let you live today."
    fan "Leave, and never come back."
    show fw 65
    mc "Wait! I was hoping I could ask you a few questions before–"
    show fw 66
    fan "I have nothing to discuss with a human from outside our pack."
    show fw 65
    mc "We don't have to be enemies."
    show fw 66
    fan "You're not even worthy to be here."
    show fw 65
    mc "Then let me prove you my worth!"
    show fw 66
    fan "You?"
    fan "You're nothing but a frail human."
    show fw 65
    mc "I am not weak."
    show fw 66
    fan "Hah."
    fan "Overconfidence can be a dangerous quality, young man."
    fan "Do you really think you could best me in a duel?"
    show fw 65
    mc "I could."
    show fw 66
    fan "Hah..."
    fan "Alright then."
    fan "Prove your mettle."
    fan "Defeat me in combat... and I'll address all of your questions."
    fan "You and me, in my human form. Even odds."
    show fw 65
    mct "A duel?"
    menu:
        with dis12
        "[gr]Accept":
            $ lunawolffight = True
            mc "I was thinking of fighting you in your wolf form."with dis06 
        "Refuse":
            mc "We have better things to do than unnecessary fights." with dis06 
            show fw 66
            fan "Hah. So I thought."
            play sound were1
            fan "Now go, and never come back."
            fan "Take them to the exit, Duke."
            show fw 65
            mc "Rest assured, we won't come back."
            show fw 58
            l "Goodbye, Burpee!"
            show fw 56
            bur "B-Bye Luna."
            bur "I'm sorry things turned out this way."
            show fw 58
            l "No worries!"
            l "I'm sure we'll cross paths again."
            show fw 54
            bur "That would be nice! You can visit us outside the camp anytime!"with hpunch
            show fw 58
            l "Will do!"
            l "Take care, guys!"
            $ werewolvesside = True
            jump poswerevamp
    mc "In your human one? Even easier."
    show fw 66
    fan "Hahahah..."
    fan "I like you, boy."
    play sound were1
    show fw 67 with dis15
    pause
    stop music fadeout 5
    play sound2 transformwerewolf
    show fw 68 with Dissolve(3.2)
    pause 0.4
    fan "Hmmmmgh..." with dis12
    play musicb wvvwerewolves fadein 6
    play sound7 debris
    show fw 69
    fan "*Standing up* Oooh boy, that felt good." with dis15
    play sound3 bonebreak
    show fw 69b
    fan "*Cracking his neck* It's been a while since I reverted to my human form." with dis
    play sound4 bonebreak
    show fw 69
    fan "*Cracking his neck* I almost forgot how refreshing it used to feel." with dis
    show fw 71
    mc "Well..." with dis
    mct "Is he really not gonna cover himself...?"
    mc "*Clears throat* It's good to finally be able to talk face-to-face."
    mc "Can all of you shift into your human forms at will?"
    show fw 70
    fan "You won't get any answers from me unless you defeat me in combat."
    show fw 71
    mc "Hmm. Okay then, I'm ready whenever you are."
    mc "We're actually in a rush, so let's get this done quickly."
    show fw 70
    fan "Excellent. Disrobe and meet me in the main courtyard."
    fan "We shall fight there."
    show fw 71
    mc "Um..."
    mc "I'm sorry, do we have to fight... naked? Me too?"
    fan "Mm-hm."
    mc "I-I'm not sure I'm entirely comfortable with that."
    show fw 72
    fan "Why not?" with dis
    fan "Clothes are nothing but an unnecessary hindrance in battle, imposed on us by those who are blind to the natural beauty of the beast!"
    fan "The art of combat should always be practiced by warriors adorned as they came into this world. In contact and one with nature!"
    show fw 73
    fan "Well... that is, if your woman is okay with it, of course." with dis
    fan "We can make adjustments if she's not comfortable with it. I've gotta respect that."
    mct "Oh, thank god."
    show fw 59
    if lunapath:
        l "Nah, it's perfectly fine. Go on and strip."
    else:
        l "Don't worry, I couldn't care less."
    show fw 60
    mc "LUNA?! Y-YOU'RE SUPPOSED TO SAY NO!" with hpunch 
    show fw 70
    fan "Excellent then."
    fan "Let us shed this wretched garb and commence battle."
    show fw 71
    mc "Um..."
    mc "*Sighs* I guess I have no other option."
    mct "Ending my Eternum session with a Gachimuchi brawl... I definitely didn't see that one coming."
    play sound clothes5
    play soundlow tear1
    play sound2 belt
    mc "*Getting rid of your hunter robes* Okay, fuck it." with dis15
    mc "Happy now?"
    scene fw 70
    fan "I will explain the rules."
    fan "No elemental spells are allowed."
    show fw 74
    mc "Got it."
    fan "No weapons of any sort either. Just our bare hands."
    show fw75
    mc "And how is the winner determined?" 
    fan "Until the other surrenders or is knocked out."
    mc "Understood."
    bur "BETTY!" with hpunch
    scene fw 76
    bet "W-W-WHAT, WHAT? WHAT'S HAPPENING!" with dis 
    show fw 77
    bur "You were looking at the human's penis!"
    show fw 76
    bet "No, I wasn't!"
    show fw 77
    bur "Yes, you were, I saw it!"
    show fw 76
    bet "I was looking at his butt!"
    show fw 77
    bur "*Gasps* So you admit it!"
    show fw 76
    bet "M-Mere curiosity for human anatomy!"
    bet "I... um, s-stop making me waste my time with your human penises and butts, Burpee!"
    mct "Was Luna looking too...?"
    mct "I kind of expected her to turn around."
    bet "Can you let me go back to my post??"
    show fw 73
    fan "Calm down, guys."
    fan "Yes, you can go back to your post, Betty."
    fan "Duke and Burpee will handle this."
    show fw 70
    fan "Well... it seems like this might cause unnecessary distraction." with dis
    fan "So it may be better if we just wear a simple loincloth during the combat exercise."
    show fw 71
    mc "Oh thank goodness, yes, please."
    show fw 70
    fan "Follow me to the courtyard."
    fan "I wouldn't want to make you waste more time."
    show fw 71
    mc "After you."
    stop soundloop2 fadeout 7
    stop musicb fadeout 8
    play soundloop night2 fadein 6
    show fw 78 with dis3
    bla "You wear the rags provided by Fangrend and go with him to the courtyard, followed by Luna, Burpee, and Duke." with dis12
    fan "So... are you ready?"
    scene fw 79
    mc "Absolutely." with dis15
    show fw 80
    fan "Your overconfidence is admirable. I wonder how long it lasts."
    fan "Have you never lost a battle?"
    show fw 79
    mc "I have. And that only made me stronger."
    show fw 80
    fan "HAHA!"
    fan "That's the spirit of a true champion!"
    fan "Alright boy, let's fight!"    
    show fw 81
    l "You don't have to do this, [mc]."
    l "We can go back to Hollowbrook and figure out what to do with Penny."
    show fw 82
    mc "Don't worry, Luna, I got this."
    mct "This man is no ordinary NPC. None of them are."
    show fw 79
    mct "They each have their own motives, they never repeat themselves, and they're willing to fight back if they have to."
    mct "All of them broke free from Ulysses' control somehow, and I need to find out how."
    play sound debris
    show fw 83
    mct "But he's strong." with dis12
    mct "I must be careful."
    mc "Okay..."
    play sound2 transformpower
    show fw 85
    mc "Ready whenever you are." with dis12
    show fw 84
    fan "Wow, you hardly look human anymore!"
    show fw 85
    mc "Just a little power boost."
    mc "Is that okay?"
    show fw 84
    fan "Absolutely! As long as you only use your fists."
    show fw 85
    mc "Of course."
    show fw 101
    mct "He's way bigger than me." with dis
    if daliapath:
        mct "This would be a good moment to remember Dalia's advice for close combat against larger opponents..."
        mct "Now, what was it..."
        mct "Hmmm..."
        if mod_vamp_wolf:
            mod "Skipping the same Dalia's scene..."
            jump continuedalialuna
        jump daliatraining07
    else:
        mct "Dammit, I'm not sure how to approach him."
        mct "Maybe if Dalia had taken the time to train me on how to fight against taller opponents, like she had mentioned..."
        jump continuedalialuna
label daliatraining07:
    stop music2 fadeout 5
    stop soundloop fadeout 5
    stop soundloop2 fadeout 5
    play music quirky7 fadein 4 volume 0.6
    scene fw 86 with dis3
    show screen daybeforecorner
    mc "*Panting* O-Okay, okay..." with dis 
    mc "*Panting* That's... 200 pushups."
    play sound water
    show fw 87 
    d "Nice job, [mc]." with dis12
    d "Each time you do better than the last!"
    d "Soon you'll be carrying us all to the throne of Eternum."
    show fw 88
    mc "*Recovering your breath* Hah... so that's your plan, eh? You're basically just using me?"
    show fw 87
    d "It's mutually beneficial!"
    d "You bring the muscle, and we bring the brains! And... some more muscle."
    show fw 88
    mc "*Chuckles* Fair enough."
    show fw 87
    d "Alright, listen up!"
    d "You need to learn how to face opponents bigger than you. This is crucial."
    d "Thanatos is like... two feet taller than you, so your usual approach won't cut it."
    show fw 88
    mc "O-Okay, but can I sit down while you explain the theory?"
    play sound water
    show fw 89
    d "Fine, fine, sit and catch your breath... but pay attention!" with dis12
    play sound2 chair2
    show fw 90
    mc "*Sighs* Oof, thank goodness." with dis12
    show fw 91
    d "Okay, imagine this pile of straw is Thanatos." with dis08 
    mc "Mm-hm."
    show fw 92
    d "Basically, you're up against an opponent as quick as you, but larger and taller." with dis12
    show fw 93
    mc "Mm-hm..." with dis
    show fw 94
    d "So you must outsmart him with technique!"
    d "You can't just charge in like a wild bull."
    mc "Aha."
    play soundlow water3
    show fw 95
    d "So try this move: you fake a kick to his right side like this, and when he tries to protect himself from it..." with dis12
    play sound3 splash2 volume 0.7
    play sound4 whoosh6
    show fw 96
    d "BAM! You quickly shift your weight and kick his left ear with your other foot!" with hpunch
    play soundlow water
    show fw 97
    d "With his left ear discombobulated, he won't be able to react for a few seconds!" with dis12
    mct "Jesus Lord almighty, these shorts can't be legal."
    show fw 98
    mct "I mean... have you seen that?!" with dis14
    mct "The perfect shape."
    mct "Not a hint of imperfection, not a trace of cellulite."
    mct "And boy, was it soft that one time..."
    mct "She really–"
    play sound splash2
    play sound2 water3
    scene fw 99
    d "Are you paying attention?" with hpunch
    show fw 100
    mc "Y-YES!"
    show fw 99
    d "What did I just say?"
    show fw 100
    mc "You discombobulate the left ear."
    show fw 99
    d "And then?"
    show fw 100
    mc "You..."
    mc "Discombobulate... the..."
    mc "...right leg?"
    d ". . ."
    mc "I'm planning to make discombobulation my signature move."
    show fw 99
    d "Well, I had a surprise for you at the end of this training, but since you don't seem to care, I won't bother."
    show fw 100
    mc "Awh, no! Please, I love surprises!"
    show fw 99
    d "You've missed your chance."
    show fw 100
    mc "Come on, Dalia!"
    mc "What is it?"
    show fw 99
    d "I won't tell you."
    show fw 100
    mc "Give me another shot!"
    d "Hmm."
    show fw 99
    d "Okay, do 300 pushups in a row and I might consider giving you a second chance."
    show fw 100
    mc "300 pushups in a row?!"
    mc "Today?!"
    show fw 99
    d "You have one week to pull it off."
    show fw 100
    mc "One week, huh..."
    mc "If you promise I’ll still get the surprise afterwards, I'll do those 300 pushups."
    mc "I'll train harder than ever."
    play sound water3
    show fw 89
    d "We'll see about that..." with dis14
    d "Just try to stay focused for once."
    mc "You're {i}perfectly{/i} aware of what you're doing, aren't you?"
    play sound2 water
    show fw 87
    d "Who, me...?" with dis14
    d "I don't know what you're talking about."
    d "I'm just trying to get the best out of you. Can’t have you getting distracted during a big fight..."
    show fw 88
    mc "*Chuckles* Of course..."
    hide screen daybeforecorner
    if vampireshelp:
        jump continuedaliapenny
    else:
        jump continuedalialuna
label continuedalialuna:
    if daliapath:
        stop music fadeout 8
        play soundloop night2 fadein 5
        scene fw 101 with dis27
        mct "Goddammit, Dalia needs to stop wearing those shorts to our training sessions."with dis12
        mct "I get distracted way too easily."
    scene fw 84
    fan "Before we start, though... I have a question for you."
    fan "How confident are you in your victory?"
    show fw 85
    mc "I'm... highly confident."
    mc "Why?"
    show fw 84
    fan "Confident enough to raise the stakes?"
    show fw 85
    mc "Raising it how...?"
    show fw 84
    fan "Elevating it to..."
    play soundloop2 deception
    fan "A fight to the death."
    show fw 85
    mc "I'm sorry?"
    show fw 84
    fan "If you win, I will embrace death, and my entire pack will be at your service forever."
    fan "You will assume my mantle as their leader, forging them into your personal army."
    fan "Yet, if I win... you and your companion must also embrace the end."
    show fw 85
    mc "Are you talking about Luna? She has nothing to do with this."
    show fw 84
    fan "This is the essence of being a part of a pack, young man."
    fan "You are one. When one falls, all fall with them."
    fan "If you can't understand this, then we have nothing to discuss."
    fan "The door is open for you to leave."
    show fw 101
    fan "Now... make your choice."
    menu:
        with dis12
        "Accept":
            scene fw 85
            mc "Fine, I accept." with dis
            mc "A fight to the death."
            show fw 84
            fan "I see."
            fan "Are you sure?"
            show fw 85
            mc "I already said yes. Now shut up and face me already."
            mc "I'm starting to get sick of you."  
            $ werewolvesside = True        
        "[gr]Keep Luna out of it":
            $ lunafightdeath = True
            scene fw 85
            mc "Keep Luna out of it and you've got a deal." with dis
            mc "If I lose, only I have to die."
            show fw 84
            fan "That's not an option."
            fan "You're a pack. You are one."
            stop soundloop2 fadeout 2
            show fw 85
            mc "Then I guess we're done here."
            mc "Let's leave this place, Luna."
            show fw 84
            fan "Hah! Just like that?"
            fan "Weren't you so sure of your victory?"
            show fw 85
            mc "And I am."
            mc "But you seem confident too. You might have an ace up your sleeve, or play dirty, I don't know."
            if lunapath:
                mc "I won't jeopardize the lives of the ones I love, under any circumstances."
                $ luna_points += 1
                play sound beat
                show screen heartbeat
                show fw 102
                fan "Very well." with dis12
                fan "Your choice has been made."
                l ". . ."
                show fw 103
                bur "Awww, did you hear that, Luna?" with dis12
                bur "That was so cute! Your boyfriend really loves you, huh?"
                show fw 104
                l "W-We..." with dis
                l "I mean, he's not my boyfriend."
                show fw 103
                bur "Oh. So you're already married? So young?" with dis
                show fw 104
                l "That's not what I mean, we're not..." with dis
                show fw 105
                duk "You dumbass, can't you see they're not dating yet?" with dis
                show fw 106
                bur "What do you mean? Really?"
                show fw 105
                duk "Of course not!"
                duk "It's obvious that they like each other, but they're not {i}there{/i} yet."
                show fw 106
                bur "Ahh..."
                show fw 105
                duk "You just have to see the way they look at each other for a second, Burp."
                show fw 106
                bur "Oh, forgive me for not being a human sociologist, Duke."
                show fw 105
                duk "This is why you can't appreciate the little delicate things."
                show fw 106
                bur "Not this again!"
                bur "I swear I'll eat all those flowers of yours!"
                show fw 105
                duk "DON'T YOU DARE!" 
                mc "*Looking at Luna* (What are they all mumbling about?)"
            else:
                show fw 81
                l "We're not bad people. We just want to help."
                show fw 82
                mc "*Looking at Luna* Yeah, she's right. We–"
            play sound bodycollide
            show fw 108
            fan "Congrats, [mc]. You passed the test."
            jump ufheyfeyufherff
        "Refuse":
            $ lunafightdeath = True
            scene fw 85
            mc "I refuse." with dis
            show fw 84
            fan "Hah! You're scared now?"
            show fw 85
            mc "It's not about fear."
            mc "I won't jeopardize our lives over something trivial like this."
            show fw 84
            fan "Weren't you so sure of your victory?"
            show fw 85
            mc "And I am."
            mc "But you seem confident too. You might have an ace up your sleeve, or play dirty, I don't know."
            mc "Even if there's only a 1%% chance of losing... death’s not a risk worth taking."
            mc "So... yeah, we're done here."
            mc "Let's get out of here, Luna."
    show fw 84
    fan "Very well."
    fan "Your choice has been made."
    play sound whoosh4
    fan "And with this...{w=1}{nw}"
    stop soundloop2
    show fw 101
    fan "The fight is over."with dis14
    if lunafightdeath:
        fan "You win."
    show fw 85
    mc "Huh?" with dis
    if not lunafightdeath:
        play sound2 transformpower
        show fw 83
        mc "Wait, what...?" with dis12
        mc "What do you mean, it's over?"
        show fw 84
        fan "You didn't pass the test."
        fan "I'm afraid I have nothing else to discuss with you."
        show fw 83
        mc "What...?"
        mc "What test?"
        show fw 81
        l "But why? We agreed to all your terms."
        show fw 82
        mc "Exactly! Why–"
        play soundlow whoosh7
        play sound2 debris
        show fw82b
        fan "*Appearing behind you* That was not the point of this little performance." with hpunch
        scene fw 113
        mc "W-What... how did you move so fast...?"
        show fw 112
        fan "Bargaining with the lives of your pack members is a non-starter."
        show fw 113
        mc "I'm not trading shit, I would have defeated you!"
        show fw 112
        fan "You can't be certain of that."
        show fw 113
        mc "*Cocky laugh* Oh, believe me, I'm sure of it."
        show fw 112
        fan "You're entirely missing the point here."
        show fw 113
        mc "And what about “when one falls, all fall with them” and all that bullshit?"
        show fw 112
        fan "Again, you're missing the point."
        fan "Now, please, leave."
        show fw 113
        mc "But–"
        show fw 112
        fan "Leave."
        show fw 113
        mc "Bah!"with hpunch 
        mc "Fine!"
        show fw 82
        mc "Let's get out of here, Luna."
        mc "We won't get anything out of these... broken NPCs. I was probably mistaken earlier about them being different from the typical ones."
        show fw 81
        l "O-Okay."
        l "Bye guys... good luck."
        show fw 82
        duk "Thanks Luna!"
        bur "Please take care!"
        show fw 113
        mc "Thanks for nothing, I guess."
        mc "We'll go back to Hollowbrook. Hopefully we'll find more rational people there."
        show fw 112
        fan "May the winds blow in your favor."
        show fw 113
        mc ". . ."
        mc "Yeah, thanks..."
        mc "Let's go, Luna."
        jump poswerevamp
    else:
        mc "What do you mean, I win?"
        mc "We didn't fight."
        show fw 81
        l "So... this was just a test?"
        show fw 82
        mc "*Looking at Luna* A test?"
        play sound bodycollide
        show fw 108
        fan "Indeed, and you passed it."
label ufheyfeyufherff:
    play soundlow whoosh7
    play sound2 debris
    scene fw82bb
    mc "*Getting away from him* W-WHAT THE..." with hpunch
    mct "What the hell... I only looked away for a second!"
    mct "How did he move so fast?!"
    mct "I didn't even sense his presence until he touched my shoulder..."
    mc "A-And what do you mean I passed the test?!"
    play music wvvwerewolves fadein 11
    stop soundloop fadeout 11
    show fw 110
    fan "You were willing to face me, that was the first step." with dis12
    fan "Yet, you refused to fight if it meant risking the loss of one of your own."
    fan "The pack and the individual are one. The well-being of our people must always be our ultimate priority."
    fan "Always."
    show fw 113
    mc "Huh... very sneaky." with dis
    show fw 112
    fan "Welcome to the pack, [mc]."
    show fw 113
    mc "Um... thank you."
    mc "I'm... honored."
    mct "To be honest, he never gave me a bad feeling. I'm relieved to see he's a good man and I don't have to actually fight him."
    show fw 112
    fan "We've all wasted enough of your time, so you're free to go now."
    fan "Although you mentioned you had questions earlier, so feel free to ask before you leave."
    show fw 113
    mc "I appreciate it."
    mct "Mmm, I should get straight to the point."
    mct "Penny must be already waiting for us."
    mc "Okay..."
label menuwerewolfquestions:
    if not wquest1 and not wquest2 and not wquest3:
        mc "Well, I'd love to stay and continue asking you questions, but we really must be on our way now."
        jump postmenuwerewolf
    menu:
        with dis
        "[gr]Can I be a werewolf?" if wquest1:
            $ wquest1 = False
            mc "You mentioned we're considered members of the pack now." with dis06
            mc "Does that mean that... we can become werewolves?"
            show fw 110
            fan "Becoming a werewolf is a grueling, painful process, and I wouldn't recommend it to anyone." with dis 
            fan "You see, we were originally created as weapons for combat, a long time ago."
            fan "We were treated like animals for so long that most of us have forgotten how to shift back into our human forms."
            fan "I'm one of the few remaining who can switch at will."
            fan "The rest of the pack, including Burpee and Duke, are bound to their wolf forms until I can find a way to reverse the curse."
            show fw 113
            mc "Damn, that's not quite the fantastical picture I had in my mind." with dis
            mc "I truly hope you can find a cure one day."          
            jump menuwerewolfquestions
        "[gr]What memories do you have of your past?" if wquest2:
            $ wquest2 = False
            mc "What memories do you have of your past?" with dis06
            mc "Before arriving here."
            show fw 112
            fan "We all come from the northern regions of Ekabar."
            fan "I've spent the last few years traveling across the continent in hopes of finding a cure."
            show fw 113
            mc "And what about... Egypt?"
            mc "One of your brothers mentioned it earlier."
            mc "He even spoke of one of their gods."
            show fw 114
            fan "Egypt...?"with dis
            fan "Um... I'm afraid I've never come across that name... I think."
            show fw 115
            mc "Do you know what “Eternum” is? Or Ulysses? Or things like... Europe, Asia, or America?"
            show fw 114
            fan "Uh... no, those terms don't ring a bell."
            fan "Despite covering thousands of kilometers in our travels, Ekabar is all we've known."
            fan "We have no idea of what lies beyond the great seas, I'm sorry."
            show fw 113
            mc "No worries..." with dis
            mct "One of the werewolves mentioned Egypt and Anubis. I heard it."
            mct "Could their actual memories from the real world be merging with the fabricated ones they acquired when they became NPCs?"
            mct "Perhaps that's the trigger that can “free” them from Ulysses' control? I’ll have to note that for later..."
            jump menuwerewolfquestions
        "[gr]What's your current relationship with the town of Hollowbrook?" if wquest3:
            $ wquest3 = False
            mc "What's your current relationship with the town of Hollowbrook?" with dis06
            show fw 110
            fan "If you've been there recently, you'll probably notice that it's... become strained."with dis
            fan "Their hunters began targeting us without any provocation when we sought medicine from them."
            fan "We've been doing our best to steer clear of them, but if they encroach on our hideout... we'll defend ourselves."
            fan "We're planning to relocate again in a few days, so hopefully it won't come to that."
            show fw 113
            mc "Understandable."with dis 
            mct "I wonder what triggered this sudden shift in behavior among the NPCs."
            mct "Did the hunters go rogue first?"
            mct "Or perhaps it was the werewolves? They're clearly not following any prescribed path anymore."
            mct "Hmmm..."
            jump menuwerewolfquestions
        "Leave":
            mc "Well, I'd love to stay and continue asking you questions, but we really must be on our way now." with dis08
label postmenuwerewolf:
    mc "I hope we can continue our conversation sometime."
    show fw 112
    fan "Very well."
    fan "It was a pleasure meeting you, [mc] and Luna."
    fan "I also hope we have the chance to meet again in the future."
    show fw 113
    mc "Oh, before we leave..."
    menu:
        with dis
        "Side with the hunters\n[mt](Hunters allies)":
            mc "You should know that, if you truly wish to cure your brothers, Hollowbrook is your best bet."with dis06
            mc "We crossed paths with the hunters upon our arrival, and they were leaving the town for good."
            mc "Now only a handful of civilians remain, and among them there's a shaman. Perhaps she knows how to help them return to their human form."
            show fw 112
            fan "Oh... really? That's excellent news indeed."
            fan "I'll send someone to pay them a visit soon, then."
            show fw 113
            mct "Hopefully this will lead to a truce and to us becoming friends with the hunters of Hollowbrook."
            mc "Good."
            show fw 112
        "Side with the werewolves\n[gr][mt](Werewolves allies)":
            $ werewolvesside = True
            mc "You should know that we passed through Hollowbrook on our way here, and I can tell you the hunters have lost all reason."with dis06
            mc "They believe you're all malevolent creatures that must be eradicated."
            mc "If you wish to help your brothers, you'd be better off far from that town of lunatics."
            show fw 112
            fan "Thanks for the advice, we'll steer clear of it."
            fan "It's not something we aren't used to by now. I understand that our appearance can be intimidating and instill fear."
    fan "Thanks again for your help, [mc]."        
    show fw 113
    mc "No problem."
    mc "And best of luck."
    scene fw 116
    l "Bye guys!" with dis15
    l "Take care! It was so nice to meet you!"
    bur "BYE LUNA!"with hpunch
    duk "PLEASE PROMISE US YOU'LL VISIT!"with hpunch
    bur "AND TAKE CARE OUT THERE!"with hpunch
    duk "I'LL PREPARE A FLOWER BOUQUET FOR WHENEVER YOU'RE BACK!"with hpunch
    l "I'll be looking forward to it!"
    mc "*Chuckles* (I'll miss those guys.)"


label poswerevamp:
    stop music fadeout 6
    stop soundloop fadeout 7
    stop soundloop2 fadeout 7
    scene black with dis25
    if mod_vamp_wolf:
        $ vampireshelp = True
        menu:
            with dissolve
            mod "Choose which option will be the main one."
            "[gr]Vampires' path and allies":
                $ werewolveshelp = False
                $ vampiresside = True
                $ werewolvesside = False
            "Vampires' path and Hunters allies":
                $ vampiresside = False
                $ werewolveshelp = False
                $ werewolvesside = False
            "[gr]Werewolves' path and allies":
                $ vampireshelp = False
                $ werewolvesside = True
                $ vampiresside = False
            "Werewolves' path and Hunters allies":
                $ vampireshelp = False
                $ werewolvesside = False
                $ vampiresside = False

        menu:
            with dissolve
            mod "And would you like to see alternative scenes from other paths/allies when appropriate?"
            "Yes":
                pass
            "No":
                $ mod_vamp_wolf = 0

    menu:
        with dissolve
        mod "The following scene has variations depending on the animal you bought. Would you like to see them all here and in the future when possible?"
        "See variations":
            $ mod_animals = True
        "Don't":
            pass
    show screen afewminuteslater with dis17
    pause
    play soundloop2 night fadein 6
    hide screen afewminuteslater
    scene fv 83 
    with dis27
    mc "*Sighs* Damn, that took waaaaay too long."with dis12
    if werewolveshelp:
        mc "Penny is gonna think we're pushing up daisies."
    else:
        mc "Luna is gonna think we're pushing up daisies."
    play sound footsteps3 fadein 1
    scene fl 1
    mc "And what's worse, it was all a huge waste of time." with dis15
    mc "It's obvious that those are not normal NPCs and they behave like real people, but we didn't learn anything about why or how they broke free of their rails."
    show fl 2
    if werewolveshelp:
        l "I don't think it was a waste of time!"
        show fl 4
        l "We made new allies!"
        l "I'm sure Fangrend, Duke, and Burpee would have our backs in the future if we ever needed them."
        show fl 3
        mc "Hmm, perhaps you're right."
        show fl 4
        l "And even if not, we made new friends, at least."
        show fl 3
        mc "*Chuckles* I guess. I love how you always find the silver lining in every situation."
        show fl 4
        l "Now let's meet up with Penny!"
        l "I'm curious to hear if she's actually found the vampires... and if they were as nice as the werewolves."
        show fl 3
    else:
        p "I don't think it was a waste of time!"
        show fl 4b
        p "We gained some new allies!"
        p "I'm sure Lord Iliescu and his wife would be willing to help us out in the future if we ever need it."
        if pennywaltzdance:
            p "Maybe just... in exchange for another dance."
        show fl 3b
        mc "*Chuckles* Perhaps you're right."
        mc "I just hope that curse doesn't mess with their heads too."
        show fl 6b
        p "I certainly hope so too!"
        show fl 4b
        p "I'll do a bit of digging on my own about that curse, see if I can find any leads on what's happening to them. I’ve been studying all these old tomes, so maybe I can find a clue!"
        show fl 3b
        mct "She's got such a kind heart."
        mct "Most people wouldn't give a shit."
        show fl 4b
        p "Now let's meet up with Luna!"
        p "I'm dying to know if she had any luck with those werewolves!"
        show fl 3b
    mc "Yep! Let's go!"
    mc "Hollowbrook should be right behind the next–"
    play music2 dark1 fadein 7
    play soundlow wind4 fadein 5 volume 0.5
    scene fl 7
    bla "You abruptly turn around, sensing a presence lurking in the shadows." with dis12
    mc ". . ."
    if werewolveshelp:
        l "[mc]?"
        l "What's wrong?"
        mc ". . ."
        show fl 5
        mc "*Whispering* We're being followed."with dis12
        show fl 6
        l "What? Since when?"
        show fl 5
        mc "I'm not sure."
        mc "But I can feel it."
        mc "You go on ahead and wait for me in Hollowbrook, Penny must be beside herself with worry by now."
        show fl 6
        l "What? And leave you here?"
        show fl 5
        mc "Don't worry, I'll handle it."
        mc "Actually, just wait for me next to the Exit Portal. I'll join you as soon as I can."
        mc "It's probably just a lost villager or... some other NPC."
        show fl 6
        l "Are you sure...?"
        show fl 5
        mc "Absolutely."
        show fl 6
        l "Well... okay then."
        l "But if you're not at the Exit Portal by the time we get there, we are coming to find you."
        show fl 5
        mc "I'll be there!"
        show fl 6
        l "Okay..."
        l "Be careful."
        scene fl 7 with dis2
        bla "Luna continues walking down the path until she disappears over the hill. You stand in the middle of the pathway in complete silence, waiting for what feels like an eternity." with dis12
    else:
        p "[mc]?"
        p "What's wrong?"
        mc ". . ."
        show fl 5b
        mc "*Whispering* We're being followed."with dis12
        show fl 6b
        p "What? Since when?"
        show fl 5b
        mc "I'm not sure."
        mc "But I can feel it."
        mc "You go on ahead and wait for me in Hollowbrook, Luna must be beside herself with worry by now."
        show fl 6b
        p "What? And leave you here?"
        show fl 5b
        mc "Don't worry, I'll handle it."
        mc "Actually, just wait for me next to the Exit Portal. I'll join you as soon as I can."
        mc "It's probably just a lost villager or... some other NPC."
        show fl 6b
        p "Are you sure...?"
        show fl 5b
        mc "Absolutely."
        show fl 6b
        p "Well... okay then."
        p "But if you're not at the Exit Portal by the time we get there, we are coming to find you."
        show fl 5b
        mc "I'll be there!"
        show fl 6b
        p "Okay..."
        p "Be careful."
        scene fl 7 with dis2
        bla "Penelope continues walking down the path until she disappears over the hill. You stand in the middle of the pathway in complete silence, waiting for what feels like an eternity." with dis12
    mc ". . ."
    mc "So, are you gonna come out, or what?"
    bla ". . ."
    mc "Look, I don't have all day."
    mc "If you want something from me, speak up now."
    mc "If not, I'll be on my way."
    bla ". . ."
    mct "I definitely sense a presence around..."
    mct "But at the same time, I don't sense any bad intentions. They're not a threat, they mean no harm."
    mct "I just... know it."
    mct "Every day that passes I feel more connected to Eternum. Even when I'm not actively using my powers."
    mct "It's like I can... {i}feel{/i} the world around me."
    mct "I wouldn't be able to explain it with words to anyone, even if I tried with all my might."
    bla ". . ."
    mc "Very well, I'll head out, then."
    mc "But I’m warning you, stop following me or you'll face the consequences."
    mc "Got it?"
    bla ". . ."
    mct "Bah, I'm wasting my time. They're probably just a lost NPC."
    mct "Let's meet up with the girls in town and call it a day."
    scene fl 8
    if werewolveshelp:
        bla "You follow Luna's path and head towards Hollowbrook, feeling the presence fade the further you move away from the woods."with dis25
    else:
        bla "You follow Penelope's path and head towards Hollowbrook, feeling the presence fade the further you move away from the woods."with dis25
    aaa ". . ."
    stop music2 fadeout 6
    show black with dis2
    show screen meanwhile 
    with dis15
    pause 
    hide screen meanwhile
    scene fl 9 
    with dis25
    play soundlow wind4 volume 0.4 fadein 2
    p "(Hmmm... looks like there's nobody around yet.)" with dis14
    if werewolveshelp:
        p "(I truly hope [mc] and Luna are okay.)"
    else:
        p "(I truly hope Luna is okay.)"
    p "(Perhaps the werewolves weren't as “welcomingly eccentric” as the vampires.)"
    play music2b wvv2 fadein 4
    play sound doorold 
    scene fl 10 with dis
    hun "Thomas, grab your sword, quickly!" with dis08
    p "(Hmm?)"
    play soundlow footsteps3 volume 0.4
    scene fl 11 with dis15
    hun2 "Huh? Why?" with dis08
    hun "I've found it!"
    hun "I know where the centaurs are hiding! In the forest!"
    hun2 "So what?"
    hun "What do you mean, so what? Arm yourself and let's go!"
    hun "They must be eradicated."
    hun2 "But..."
    hun2 "I mean, what have the centaurs ever done to us?"
    hun "Have you forgotten the teachings of Father Bakhar?"
    hun "Magic is a malevolent force, a temptation from the devil in this world."
    hun "We are but instruments of God, and as such, we must cleanse the world from the Dark Lord's influence."
    hun2 "I remember them..."
    hun "Then shut up and let's go."
    hun2 "Alright..."
    scene fl 12
    p "(As I imagined, none of the creatures that live in the woods have harmed the villagers.)"
    p "(They've taken up this crusade against magic solely because of this 'Father Bakhar'...)"
    p "(I need to find [mc] and Luna as soon as possible and warn them...)"
    stop music2b fadeout 8
    scene fl 13 with dis27
    pause
    play sound4 footsteps3 volume 0.5
    scene fl 14 with dis2
    if werewolveshelp:
        l "(I don't see Penny anywhere.)"with dis 
        l "(I hope she's alright.)"
    else:
        l "(I don't see [mc] or Penny anywhere.)"with dis 
        l "(I hope they're alright.)"
    l "(Perhaps I should just head to the Exit Portal?)"
    l "(The sun is about to rise.)"
    play soundlow crygirl fadein 1 volume 0.4
    show fl 15
    bla "The sound of a girl sobbing emanates from a nearby building." with dis
    l "(A girl... crying?)"
    play sound doorold
    stop soundloop2 fadeout 4
    play soundloop fireplace fadein 5 volume 0.6
    scene fl 16 with dis2
    bla "Luna steps into the weathered building, following the sound of weeping." with dis
    l "(It looks like an old inn.)"
    play sound2 crygirl
    show fl 17
    girl "*Cries*" with dis12
    play sound3 footsteps2 volume 0.6 fadein 2
    scene fl 18 with dis2
    bla "Luna cautiously approaches the source of the sound, only to find a small girl huddled in front of a flickering candle." with dis
    girl "*Sobbing* I-I'll never stay out late again, I promise..."
    play sound4 chair2
    show fl 19
    l "*Sitting next to her* Hello!" with dis
    l "Are you okay? Why are you crying?"
    show fl 21
    girl "*Gasps* E-Eh?" with dis
    girl "W-Who are you?"
    show fl 20
    l "My name is Luna. And you?"
    show fl 21
    girl ". . ."
    syb "S-Sybilla."
    syb "Are you also a hunter?"
    show fl 20
    l "Not exactly."
    l "I'm just visiting, but I'm a friend!"
    l "Why are you here all by yourself?"
    show fl 21
    syb "I..."
    syb "*Sniffs* O-Our dog Rub ran off right before sunset, so I went out to search for him."
    syb "B-But then I got lost and ended up here and couldn’t make it back home before dark."
    syb "We can't go out at night due to the monsters in the streets, s-so... I have to wait until dawn."
    show fl 20
    l "I see."
    l "Well, then we'll wait together!"
    show fl 21
    syb "Wait? Together...?"
    show fl 18
    syb "*Sobbing* It won't work. They'll find us." with dis 
    syb "That's what my mom said."
    show fl 22
    l ". . ."
    show fl 20
    l "You know, this almost feels like deja-vu!"
    show fl 21
    syb "W-What?"
    syb "What's a dejafu?"
    show fl 20
    l "It's like when you feel you've already experienced something before."
    l "I once met a little girl named Anne, just like you, who was also scared and all alone in a big, dark house because she lost her mom."
    l "And do you know what happened?"
    show fl 21
    syb "What...?"
    show fl 20
    l "She found her! They were reunited again and everyone was safe!"
    show fl 21
    syb "Really...?"
    show fl 20
    l "Absolutely!"
    show fl 21
    syb "Oh..."
    show fl 18
    syb "*Going back to crying* B-But-but..."with dis
    syb "*Sobbing* That won't happen to me."
    syb "*Sobbing* The monsters will eat me."
    syb "*Sobbing* And I'll be gone forever, just like Daddy when he left the town."    
    show fl 22
    l ". . ."
    show fl 23
    l "Hmmm..."with dis
    show fl 18
    l "Increarbus Severum."
    play sound spell
    show fl 24 with dis
    play sound2 steam2 fadein 3
    scene fl 18 with dis
    pause
    play music lunaquirky fadein 4
    if goat or mod_animals:
        play sound goat
        mau "*Bleats*" with dis
        show fl 25
        syb "Huh...?" with dis
        show fl 26
        syb "A... a goat?"
        syb "How did it get here?"
        play soundlow dodge
        play sound7 bodycollide
        show fl 27
        zpy "*Jumping on top of Maurice* Hello Sybil!" with dis
        scene fl 25
        syb "Uhh?"
        syb "Who are you?"
        scene fl 27
        zpy "My name is Zippy!"
        zpy "Very nice to meet you!"
        show fl 28
        zpy "And this right here is my trusty steed Maurice!" with dis 
        zpy "Say hi to the lady, Maurice!"
        play sound goat
        mau "*Bleats*"
        show fl 25
        syb "Nice... to meet you too."
        syb "What are you??"
        show fl 27
        zpy "I'm a magic fox, of course!"
        zpy "I live in the forest!"
        show fl 25
        syb "The forest? With the monsters?"
        show fl 27
        zpy "Oh, there are no monsters! We all like to play there!"
        show fl 25
        syb "Really...?"
        show fl 27
        zpy "Actually, Rub told me that you were here all by yourself, and he asked me if I could come and hang out with you until the sun comes up!"
        zpy "Isn't that cool?!"
        show fl 25
        syb "You know Rub?!"
        show fl 27
        zpy "I do! We’re great friends!"
        zpy "He's always telling us all how great his human owner is!"
        show fl 25
        syb "Really??"
        show fl 27
        zpy "ALL DAY!"
        zpy "But don't think I'm a bad owner either!"
        zpy "I've taught some GREAT tricks to Maurice!"
        zpy "Do you want to see them?"
        show fl 25
        syb "Yes..."
        show fl 28
        zpy "Very well! You heard the little miss, Maurice!"
        zpy "Let's show her how fast we can go!"
        zpy "So..."
        play soundlow kickball
        zpy "*Stomping on him* GEE UP!" with vpunch  
        play sound6 punch
        play sound5 whoosh6
        play sound7 debris3
        show fl 29
        zpy "Ouch!" (multiple=2)
        bla "Maurice kicks Zippy and sends him flying backwards." (multiple=2) with hpunch
        if mod_animals:
            scene black with fade
    if toucan or mod_animals:
        play sound toucan
        mau "Stockholm!" with dis
        show fl 25
        syb "Huh...?" with dis
        show fl 30
        syb "A... a bird?"
        syb "How did it get here?"
        play sound toucan
        show fl 31
        mau "Stockholm!" with dis
        show fl 30
        syb "What? What does that mean?"with dis
        play soundlow dodge
        play sound7 bodycollide
        show fl 32
        zpy "*Jumping on top of the table* Hello Sybil!" with dis
        scene fl 25
        syb "Uhh?"
        syb "Who are you?"
        scene fl 32
        zpy "My name is Zippy!"
        zpy "Very nice to meet you!"
        show fl 33
        zpy "And this right here is my trusty steed Maurice!" with dis 
        zpy "The word he says is actually the name of a city veeeeery far from here, where Maurice was born!"
        zpy "Maurice is quite the world traveler!"
        play sound toucan
        mau "Stockholm!" with hpunch 
        show fl 25
        syb "Ohh... I didn't know that."
        syb "Nice... to meet you."
        syb "What are you??"
        show fl 32
        zpy "I'm a magic fox, of course!"
        zpy "I live in the forest!"
        show fl 25
        syb "The forest? With the monsters?"
        show fl 32
        zpy "Oh, there are no monsters! We all like to play there!"
        show fl 25
        syb "Really...?"
        show fl 32
        zpy "Actually, Rub told me that you were here all by yourself, and he asked me if I could come and hang out with you until the sun comes up!"
        zpy "Isn't that cool?!"
        show fl 25
        syb "You know Rub?!"
        show fl 32
        zpy "I do! We’re great friends!"
        zpy "He's always telling us all how great his human owner is!"
        show fl 25
        syb "Really??"
        show fl 32
        zpy "ALL DAY!"
        zpy "But don't think I'm a bad owner either!"
        zpy "I've taught some GREAT tricks to Maurice!"
        zpy "Do you want to see them?"
        show fl 25
        syb "Yes..."
        show fl 33
        zpy "Very well! You heard the little miss, Maurice!"
        play soundlow dodge
        play sound7 bodycollide
        show fl 34
        zpy "Let's show her how we fly!" with dis 
        zpy "GEE UP!" with hpunch 
        play sound6 bird_flying
        show fl 35
        bla "Zippy and Maurice start flying in circles around the room." with dis15
        show fl 25
        syb "Wow!"
        show fl 35
        zpy "Faster, Maurice!"
        zpy "Use your ultra-speed!" with hpunch 
        play sound5 bird_flying
        play sound7 whoosh3b
        show fl 36
        zpy "O-Oh wait!" with hpunch 
        zpy "I FORGOT TO FASTEN MY SEATBELT!!" with hpunch 
        if mod_animals:
            scene black with fade
    if cat or mod_animals:
        play sound cat
        mau "*Meows*" with dis
        show fl 25
        syb "Huh...?" with dis
        show fl 37
        syb "A... a cat?"
        syb "When did it get here?"
        play soundlow dodge
        play sound7 bodycollide
        show fl 38
        zpy "*Jumping on top of the table* Hello Sybil!" with dis
        scene fl 25
        syb "Uhh?"
        syb "Who are you?"
        scene fl 38
        zpy "My name is Zippy!"
        zpy "Very nice to meet you!"
        show fl 25
        syb "N-Nice to meet you."
        syb "Is the cat yours?"
        play sound purr2
        show fl 39
        zpy "*Patting Maurice* Indeed, he is! This is my trusty steed Maurice!" with dis 
        zpy "Though he's quite independent, so I prefer to think of us as friends, instead of pet and master!"
        show fl 25
        syb "That's cool..."
        syb "B-But what are you??"
        show fl 38
        zpy "I'm a magic fox, of course!"
        zpy "I live in the forest!"
        show fl 25
        syb "The forest? With the monsters?"
        show fl 38
        zpy "Oh, there are no monsters! We all like to play there!"
        show fl 25
        syb "Really...?"
        show fl 38
        zpy "Actually, Rub told me that you were here all by yourself, and he asked me if I could come and hang out with you until the sun comes up!"
        zpy "Isn't that cool?!"
        show fl 25
        syb "You know Rub?!"
        show fl 38
        zpy "I do! We’re great friends!"
        zpy "He's always telling us all how great his human owner is!"
        show fl 25
        syb "Really??"
        show fl 38
        zpy "ALL DAY!"
        zpy "But don't think I'm a bad owner either!"
        zpy "I've taught some GREAT tricks to Maurice!"
        zpy "Do you want to see them?"
        show fl 25
        syb "Yes..."
        show fl 38
        zpy "Very well! You heard the little miss, Maurice!"
        play soundlow dodge
        play sound7 bodycollide
        show fl 40
        zpy "Let's show her how fast we can gallop!" with dis 
        zpy "Go as fast as you can!"
        zpy "GEE UP, MAURICE!" with hpunch 
        play sound7 whoosh3b
        show fl 41
        zpy "O-Oh wait!" with hpunch 
        zpy "I FORGOT TO FASTEN MY SEATBELT!!" with hpunch 
    else:
        zpy "Hello Sybil!"with dis 
        scene fl 25
        syb "Uhh?"with dis
        show fl 20b
        zpy "*Waving his hand* Right here! On the table!"
        show fl 25
        syb "How do you know my name...?"
        syb "Who are you?"
        scene fl 20b
        zpy "My name is Zippy!"
        zpy "Very nice to meet you!"
        show fl 25
        syb "Nice... to meet you."
        syb "But... what are you??"
        show fl 20b
        zpy "I'm a magic fox, of course!"
        zpy "I live in the forest!"
        show fl 25
        syb "The forest? With the monsters?"
        show fl 20b
        zpy "Oh, there are no monsters! We all like to play there!"
        show fl 25
        syb "Really...?"
        show fl 20b
        zpy "Actually, Rub told me that you were here all by yourself, and he asked me if I could come and hang out with you until the sun comes up!"
        zpy "Isn't that cool?!"
        show fl 25
        syb "You know Rub?!"
        show fl 20b
        zpy "I do! We’re great friends!"
        zpy "He's always telling us all how great his human owner is!"
        show fl 25
        syb "Really??"
        show fl 20b
        zpy "ALL DAY!"
        zpy "Do you want to play a game?!"
        zpy "It's one Rub taught us!"
        show fl 25
        syb "Sure..."
        show fl 20bb
        zpy "*Walking towards the edge of the table* Very well! Then let me go to–"
    play sound woodhit
    play sound2 punch
    play sound3 ceramicfall
    play soundlow fallbottle
    show fl 25 with vpunch
    pause .2
    zpy "Aaaghhh..." with dis14
    zpy "What a klumpy-dumpy!"
    show fl 42 
    syb "*Laughs* Are you okay?!" with dis
    scene fl 43
    zpy "Y-Yeah, I'm okay, n-no worries..."
    zpy "I-I'm just a little dizzy..."
    zpy "Have you always had four legs?"
    show fl 42
    syb "*Laughs* I only have two!"
    show fl 43
    zpy "Oh, really?"
    show fl 44
    zpy "Oh... okay, yeah, I see them!" with dis08
    zpy "Everything is starting to stop spinning now! As good as new!"
    zpy "Two legs and three arms, right?"
    show fl 42
    syb "*Laughs* No! I only ha–"
    stop music fadeout 7
    sybm "S-Sybilla." 
    show fl 45
    syb "Huh?"with dis08
    show fl 46
    syb "*Gasps* MOM!" 
    show fl 47
    sybm "S-Syb, get away from her and come here."
    show fl 45
    syb "She's my friend! Her name is Luna and–"
    play music deception
    play sound2 woodhit
    show fl 47
    sybm "*Stomping the floor* SYBILLA!" with vpunch
    sybm "I said get away from her... NOW!"
    play soundlow chair2
    show fl 49
    l "*Standing up* I'm sorry Ma'am, we were only–" with dis
    show fl 48
    sybm "*Pushing her daughter away* Shut up, you monster." with dis12
    syb "Monster...?"
    sybm "I saw the vermin you created, witch."
    show fl 49
    l "I didn't mean to frighten anyone, miss."
    l "I can assure you he's completely harmle–"
    play sound3 woodhit
    show fl 48
    sybm "I said SHUT UP!" with vpunch
    sybm "You won't beguile me with your wicked tongue, you... b-bloody harlot."
    sybm "W-What were you planning to do to my daughter? HUH?!"
    sybm "Were you going to eat her? Use her in one of your dark rituals??"
    show fl 49
    l "Of course not..."
    show fl 48
    sybm "Father Bakhar was right... you need to be purged from this world."
    sybm "All of you!" with hpunch
    show fl 49
    l "I-I'm not a witch."
    show fl 48
    sybm "Please, those eyes speak for themselves."
    sybm "You can call it whatever you want."
    sybm "You're..."
    show fl 51
    sybm "You're a monstrosity."with dis15
    if donedarkarts:
        play sound impact
        scene bwda 71
        lmom "You're a monster, Luna." with flashfaster
        scene fl 51
        sybm "An abomination." with dis 
    else:
        sybm "An abomination."
    l "*Breathing heavily* . . ."
    show fl 48
    sybm "Let's get out of here, Sybil."
    syb "But–"
    play sound doorold
    scene fl 50
    bla "Sybilla's mother forcefully pulls her daughter out of the building." with dis15
    sybm "Hunters!" with hpunch
    sybm "There's a witch right here inside the inn!"
    hun2 "What?!"
    show fl 51
    sybm "Kill her!"
    sybm "Burn the building down!"
    hun2 "Call the others!"
    l ". . ."
    stop soundloop fadeout 6
    stop music fadeout 6
    scene black with dis22
    show screen afewminuteslater with dis17
    pause
    play soundloop2 night2 fadein 5
    scene fl 52 
    hide screen afewminuteslater
    with dis25
    mct "Alright, here we are." with dis12
    mct "Back where we started."
    mct "I don't see the girls anywhere though, maybe–"
    play sound2 slam3
    play sound sword
    play sound5 debris3
    play music2 wvv2
    scene fl52b
    bla "Out of nowhere, a hunter kicks the door beside you wide open." with hpunch
    hun "You bastard..."
    mc "*Putting your hands up* Whoa, whoa, whoa!" 
    mc "Easy there, buddy!"
    hun "You..."
    hun "You were with the witch, weren't you?!"
    mc "What...?"
    mct "Shit..."
    mct "I better play dumb for now."
    mc "What witch?"
    scene fl 54
    hun "The woman that rolled in with you." with dis12
    hun "The one with the red eyes!"
    mc "Ah, her... yeah, we met in a nearby town."
    mc "I was skeptical at first too, but it turns out red eyes are a thing in the southern isles where she's from."
    hun "Pff, you should learn not to be so gullible."
    hun "She's actually a witch. One of our men caught her casting magic, trying to lure children to devour!"
    mc "You're kidding..."
    hun "No joke."
    show fl 53
    mc "That... h-hussy... I can't believe I fell for her trickery!" with dis14
    mc "I will rip her guts out myself!"with hpunch 
    hun "You can help us find her, if you want."
    hun "She fled after we nabbed her, but she can't be too far."
    mc "I'll start searching immediately."
    hun "If you do find her... kill her. We don't keep monsters prisoners."
    mc "Understood."
    play soundlow run 
    scene fl 55
    bla "The hunter leaves in a hurry." with dis15
    mct "Oof, that was close..."
    scene fl 52
    mct "I've gotta find Luna before these psychos do." with dis
    mct "But... fuck, where could she have gone?"
    mct "Was there a specific building she talked about?"
    mc "Hmm..."
    if not lunapath:
        mct "Fuck, I don't think she did."
        mct "I might as well check out the church."
        mct "She seems like the kind of girl who'd enjoy dark, creepy churches."
        mc "*Sighs* (Please be there, Luna...)"
        jump morninghollow
    menu:
        with dis
        "[gr]The old barn":
            mct "Maybe the barn?"with dis06
            mct "When we arrived, she had mentioned hiding in an old barn when she first started playing Eternum."
            mct "Please be there, Luna..."
        "The windmill":
            mct "Maybe the windmill?" with dis06
            mct "I have to start somewhere, I guess."
            mct "Please be there, Luna..."
            $ lunapath = False
            $ lunau = False
            jump morninghollow
        "The church":
            mct "Maybe the church?"with dis06
            mct "I have to start somewhere, I guess."
            mct "Please be there, Luna..."
            $ lunapath = False
            $ lunau = False
            jump morninghollow
    scene fl 56 with dis2
    bla "You stroll through the streets of Hollowbrook, dodging the patrols of hunters, until you stumble upon what appears to be an old barn." with dis14
    mct "It has to be this one."
    if werewolveshelp:
        mct "I remember passing through here before going to find her and the werewolves, it was chock-full of hay bales and farm machinery."
    else:
        mct "I remember passing through here before going to find Penny and the vampires, it was chock-full of hay bales and farm machinery."
    stop music2 fadeout 6
    stop soundloop2 fadeout 6
    play soundloop fireplace fadein 5 volume 0.4
    play sound doorold
    scene fl 57
    bla "Clutching your lantern tightly, you cautiously step into the dark building."with dis22
    mct "Okay..."
    mc "*Whispering* Luna?"
    mc "*Whispering* It's me, [mc]!"
    bla ". . ."
    mct "I should scope out the upper floors before trying another building."
    play sound2 stairswood2 
    scene fl 58 with dis22
    stop sound2 fadeout 2
    pause
    play sound3 stairswood
    scene fl 59 with dis2
    mct "This seems to be the attic." with dis
    mct "Not much to see, though. Must've been a rough year for crops."
    mct "Which... probably didn't do much to quell the collective hysteria."
    show fl 60
    mc "*Looking around* Luna?" with dis
    mc "Are you in here?"
    mc "It's [mc]!"
    play soundlow wood volume 0.4
    scene fl 61
    bla "You catch a soft noise behind the nearby barrels." with dis12
    play sound clothes3
    show fl 62
    l "[mc]?" with dis
    mc "Luna!" with hpunch
    mc "Oh, thank god!"
    play music sad2 fadein 9
    stop soundloop fadeout 14
    play sound clothes3
    scene fl 63
    l "*Standing up* What are you doing here? How did you find me?" with dis12
    show fl 64
    mc "Remember when we got to Hollowbrook, and you told me about your thing for hiding out in old barns when you started playing Eternum?"
    mc "I... well, I figured I'd start my search here."
    show fl 63
    l "Ah... that was smart."
    show fl 64
    mc "I saw the whole village going nuts, on the hunt for a 'red-eyed' witch, and it had me seriously freaking out."
    show fl 65
    l "Thank you for trying to find me, [mc]."
    l "But no worries, I'm okay!"
    show fl 64
    mc "I know how powerful you are, I've seen it."
    mc "But I also know you're way too kind to harm most people. Even if they're trying to kill you."
    mc "So I was worried you could be in danger because of that."
    show fl 65
    l "I managed to slip in here without being seen, so it's all good now."
    l "If they're not looking for you, you should log off with Penny."
    l "I'll be alright, seriously."
    l "I'll leave quietly when the sun's up; there can't be much time left."
    show fl 64
    menu:
        with dis
        "[gr]Stay with her":
            mct "I know both Luna and Penny can hold their own against these hunters." with dis06
        "Leave":
            mc "But..." with dis06
            mc "I mean, are you really sure about this?"
            show fl 65
            l "Of course!"
            l "Penny's probably freaked too, you should try to find her."
            show fl 64
            mc "Well... yeah, I suppose she's likely worried or even in some kind of danger."
            mc "Hmmm..."
            mc "Fine, I'll trust you."
            mc "But promise me you'll watch your back!"
            mc "And text me THE SECOND you log off!"
            show fl 65
            l "I will!"
            l "I promise."
            show fl 64
            mct "I guess she's right, she can handle herself better than Penny."
            mct "I should go find her and ditch this cursed town once and for all."
            mc "Alright then, let's do that."
            mc "Take care of yourself!"
            show fl 65
            l "You too!"
            show fl 64
            mct "I hope I'm making the right call here."
            $ lunapath = False
            $ lunau = False
            $ lunabandonbarn = True
            jump morninghollow
    mct "But I feel like right now, it's not about physical danger."
    if donedarkarts:
        mct "I remember how tough it was for Luna the last time she was called a monster, back at Warthogs."
    mct "I can't just leave her on her own. Not now."
    play sound chair2
    play sound2 clothes3
    scene fl 66
    bla "You take a seat on the floor and set your lantern down beside you." with dis15
    mc "Well, in that case, we'll wait together until dawn!"
    mc "Like you said, there can't be much time left."
    $ namelong = mc[-1]*5
    mc "*Playfully mimicking Luna's usual concerned tone* {i}But [mc][namelong], you don't have to do that..."
    mc "Shhh!"
    mc "You're not allowed to talk unless you sit right here next to me!"
    l ". . ."
    scene fl 67
    l "*Giggles*" with dis12
    mc "Ah! A sincere smile!"
    mc "I like that better!"
    show fl 68
    l "It's just that... I said the exact same thing to a little girl I came across earlier."
    show fl 67
    mc "And did she listen?"
    show fl 68
    l "Yeah, she did."
    show fl 67
    mc "See? You're not going to let a little kid teach you how to behave, are you?"
    mc "Come on!"
    l "*Chuckles* Hmm."
    play soundlow chair2
    scene fl 69 with dis22
    bla "You and Luna settle down together, passing the time as you wait for the sun to rise. Following a bit of casual conversation, a comfortable silence envelops the moment." with dis12
    mc ". . ."
    l ". . ."
    l "(I don't know what else to talk about.)" 
    l "(I've never been good at making conversation.)"
    scene fl 70
    l "(He's probably figuring out that I'm not the most exciting company.)"
    l "(Probably... regretting spending his free time here. I can't blame him.)"
    mct "Hmm, these barrels are quite big. I could probably squeeze myself into one."
    mct "Perhaps I could take them to the river and go down the rapids like in The Hobbit...?"
    mct "What if I got stuck inside though? Hmm, I gotta think about this..."
    scene fl 71
    l "So... um... I'm sorry." with dis12
    scene fl 73
    mc "Hhm...? What for?"with dis
    show fl 72
    l "Well, making you stay here in complete silence."
    l "I-I know it's surely not the most exciting way to spend your time in Eternum."
    show fl 73
    mc "First of all, you didn't make me do anything, I'm here with you because I want to be."
    mc "And secondly, I've always said there are two types of silence."
    mc "The awkward kind, and the good kind, like now!"
    mc "The difference lies in the person you're with."
    mc "When you find someone with whom you can stay in silence and everything feels right... you can't let them go."
    show fl 74
    l "*Chuckles* Yeah... I like that."
    l "You always know what to say."
    l "I wish I had your gift with words."
    show fl 73
    mc "You don't need it."
    mc "Everyone is different, and you're amazing just the way you are."
    mc "But trust me, I don't have a gift with words either."
    mc "*Chuckles* I wouldn't find myself in so many sticky predicaments if I did."
    show fl 72
    l "Yes, you do!"
    l "You're..."
    l "I mean..."
    show fl 74
    l "I never thought I'd find someone I could trust as much as my dad, but with you... I feel like I can share anything without being judged, you know?"
    l "And it's not just because my power doesn't work on you."
    l "You make me feel... safe."
    show fl 73
    mct "I don't recall Luna opening up so freely about her feelings before."
    mct "It feels nice."
    show fl 74
    l "I've never had many friends, but now I have so many!"
    l "And it's all thanks to you!"
    l "You bring us all together."
    show fl 73
    mc "You don't need me for that!"
    mc "Your personality just naturally draws everyone in and makes them love you. It’s like you have a magnetic aura or something!"
    show fl 97
    l "Hmm."
    show fl 75
    l "I guess I've always... pushed people away since I was little."
    l "I sort of learned that being alone was... easier."
    l "Even before we moved to Kredon."
    show fl 73
    mc "You didn't grow up in Kredon?"
    mc "What was that like?"
    show fl 97
    l ". . ."
    scene fl 76 with Dissolve(3.3)
    pause
    play soundlow schoolbell volume 0.8
    pause .2
    tea "Alright kids, you can go now!" with dis
    tea "Don't forget to prepare for the math exam on Monday!"
    tea "And have a good evening!"
    l ". . ."
    kid "Trying to find your next victim, monster?"
    show fl 77
    l "Hmm?" with dis08
    show fl 78
    kid "Isn't one dead dog enough??"
    kid "You want to kill another one?"
    show fl 79
    l "I didn't kill your dog."
    show fl 78
    kid "That's bull!"
    kid "She killed him!"
    kid "It happened exactly like I told you!"
    kid "She said my dog would die, and a truck hit him a week after!"
    show fl 79
    l "T-That's why I told you to keep him inside the house during the weekend!"
    l "I just wanted to help you prevent it."
    show fl 78
    kid "Shut up, monster!" with hpunch 
    kid "Hope you get hit by a truck too!"
    show fl 80
    l ". . ."
    play soundlow zip volume 0.3
    play sound ["<silence 0.4>", noise3]
    show fl 81
    l "*Putting her things back in the bag* . . ." with dis15
    play sound kickball
    play sound3 ["<silence 0.5>", drop]
    scene fl82
    kid "*Throwing a pencil at her* Bullseye!" with dissolve
    kid2 "Hahahaha!"
    kid "Looks like objects can't go through her."
    kid2 "At least we know she's not a ghost! Hahaha!"
    kid "Come on, let's leave the freak here all alone."
    l ". . ."
    scene fl 84 with dis25
    pause
    tea "Do you know Luna Hernandez?" with dis12
    tea2 "The Mexican kid?"
    tea "Yes."
    show fl 86
    tea2 "Yeah, she's always sitting in the back, never talks to anyone." with dis14
    tea2 "She kind of weirds me out, honestly."
    tea2 "And what's the deal with those red contacts?"
    show fl 85
    tea "They're not contact lenses! Turns out that's her real eye color!"
    show fl 86
    tea2 "Are you serious? Hah, that's even creepier!"
    show fl 85
    tea "And that's not all, they say she supposedly killed her own mother a few years back, but obviously she was never convicted because she was only five years old at the time."
    show fl 86
    tea2 "*Laughs* Come on, that's gotta be a made-up story."
    show fl 85
    tea "*Chuckles* I don't know, but I'm not about to ask her, just in case."
    tea "I don't wanna be jinxed."
    show fl 86
    tea2 "*Chuckles* Fair enough."
    show fl 85
    tea "I heard she's moving to Kredon in a couple of weeks or something."
    show fl 87
    tea2 "*Laughs* Oh, thank goodness." with dis2
    tea2 "There're enough little demons in my class already, I don't need a real one!"
    tea "*Laughs* Tell me about it!"
    l ". . ."
    scene fl 88 with dis3
    play soundloop whispers2 fadein 7
    pause
    scene fl 89 with dis22
    pause
    scene fl 90 with dis22
    pause
    scene fl 89
    l ". . ." with dis22
    scene fl 91 with dis3
    pause
    her "Luna." with dis08
    l ". . ."
    her "Luna?"
    l ". . ."
    play sound risingshortb volume 0.2
    stop soundloop fadeout 1
    her "Luna!" with hpunch
    show fl 92
    l "Huh?"with dis 
    l "Yes, Dad?"
    play soundlow chair2 volume 0.6
    scene fl 93
    her "*Kneeling next to her* Are you okay, sweetie?" with dis 
    show fl 92
    l "Yeah... why?"
    show fl 93
    her "You've been a bit... distracted lately."
    her "Less cheerful than usual."
    her "Is everything alright at school?"
    show fl 92
    l "At... school...?"
    l ". . ."
    show fl 94
    l "...Yeah! Everything's awesome!" with dissolve
    show fl 93
    her "Are you sure, princess?"
    her "You know you can tell me anything, right?"
    her "If something happened..."
    show fl 94
    l "I know, Dad!"
    l "But everything is going okay, I swear!"
    l "Today was so much fun!"
    show fl 95
    her "*Sad chuckle* Hmm."
    show fl 96
    her "Alright then, so tell me, do you like the house?"with dissolve 
    show fl 94
    l "I love it!"
    l "Are we gonna live here from now on?"
    show fl 96
    her "Yes, we will!"
    her "And you know what that means?"
    her "I'm gonna be muuuch closer to the cafe now! So we'll have more time to play together!"
    her "How does that sound?"
    show fl 94
    l "Awesome!"
    show fl 96
    her "And the first thing I'll do... is learn how to braid your hair!"
    her "I know Mom used to be the one in charge of that, but I'll try my best!"
    show fl 94
    l "Super!"
    scene fl 97 with Dissolve(3.2)
    l ". . ." with dis15
    show fl 75
    l "I learned to always smile, even when I wasn't feeling it."
    l "I learned to hide my emotions, to always maintain the same expression no matter what was going on inside my head."
    l "I learned that... life was a tad less complicated when I flew under the radar."
    l "I..."
    show fl 74
    l "You know, I started playing Eternum because here I didn't feel judged for what I was or how I acted."
    l "In this world, things are so weird that I can just blend in."
    show fl 75
    l "But in the end... I suppose I took everything too far." 
    l "In the end..."
    l "I guess I’m a monster in both worlds."
    play sound whoosh6
    play sound2 debris3
    play sound3 wood
    play sound4 hay
    stop music 
    play soundloop fireplace volume 0.3
    scene fl98
    bla "You grasp Luna and pin her against the haystack, where she remains motionless, looking straight into your eyes." with hpunch 
    mc "NO!"with hpunch 
    scene fl 99
    l "W-What?"
    show fl 98
    mc "I can understand feelings of insecurity, confusion, or sadness, but I won't stand by while you deceive yourself!"
    mc "You are no monster, Luna!"
    mc "Not here, not in the real world, and not on Mars."
    show fl 99
    l "O-Okay."
    show fl 98
    mc "There's no worse feeling than trying to help someone you love and being unable to do so!"
    mc "So, I need you to do your part too!"
    mc "You're literally the kindest and most gentle soul I've ever met, and you have to see that!"
    mc "So from now on, you're gonna be absolutely transparent with me!"
    show fl 99
    l "O-Okay."
    show fl 98
    mc "No more fake smiles, no more hiding emotions, no more not saying what you really think!"
    mc "When we're alone, you're gonna be the REAL you!"
    mc "If you're sad, tell me."
    mc "If you're angry, tell me."
    mc "And if something worries you, tell me!"
    show fl 99
    l "O-Okay."
    show fl 98
    mc "Promise me!"
    show fl 99
    l "I..."
    l "I promise."
    show fl 98
    mc "Okay."
    mc "Good."
    mc "Hmph."
    l ". . ."
    mc ". . ."
    mct "Um... alright, now I'm not sure how to proceed."
    mc "*Looking at Luna's eyes* (God, she truly is beautiful.)"
    if not lunamassagefail and trykissluna:
        mct "I want to kiss her again so bad."
    else:
        mct "I want to kiss her so bad."
    mct "But it's probably not the right time, she'd think I'm trying to take advantage of her vulnerable state."
    mc "*Assessing your own posture* (And... shit, now that I think about it, I kinda look like I'm trying to assault her.)"
    mct "I-Is this why she's not saying anything??"
    mc "*Clears throat* Alright, now that we've settled that..." with vpunch
    mc "Let's go back to town. We probably can–"
    $ renpy.music.set_volume(0.8, channel='music3')
    play music3 ["<silence 0.8>"]
    queue music3 lunasex1 fadein 4
    play sound debris3
    stop soundloop fadeout 11
    scene fl 100
    bla "Luna leans in quickly and catches your lips with a sudden kiss." with dis12
    mct "W-What?"
    mct "How..."
    mct "Why..."
    mct "I don't..."
    play sound hay
    play sound2 debris3
    scene fl 101
    bla "Your thoughts and concerns fade as you eagerly return the kiss, drawing closer to Luna." with dis14
    mct "Fuck it..."
    l "Mmmm..."
    play sound2 footsteps
    scene fl 102 with dis17
    bla "Without breaking the kiss, you effortlessly lift Luna from the floor, carrying her towards the nearby barrels." with dis
    l "Mmmmhh..."
    play soundlow woodhit
    scene fl 103
    mc "*Dropping her on top of the barrels* Wow..." with dis12
    mc "That sure was unexpected."
    show fl 105
    l "I'm sorry, I just had a–"
    show fl 103
    mc "Oh, don't you dare apologize!"
    mc "That was amazing."
    mc "I just didn't expect you to take the lead, it caught me off guard."
    show fl 104
    l "I just felt like I wanted to do it."
    l "So... I did it."
    l "You told me I had to open myself to you and be the real me from now on, so..."
    show fl 103
    mc "Ahh, I dig that."
    mc "Anything else you want to share with me, miss?"
    mc "What made you want to kiss me so bad?"
    show fl 104
    l "*Giggles playfully* Well..."
    l "I guess your words got me."
    l "You're always caring, funny, confident, intelligent, and you share my quirky hobbies."
    l "Being with you is simply... fun."
    show fl 105
    l "And, uh, you're also... handsome. And... like..."
    l "S-Super hot."
    l "You're s-so... fit."
    show fl 103
    mc "Oh, yeah?"
    l "Mm-hm."
    mc "Well, since we're sharing feelings here..."
    mc "Gotta say, every word I said before stands true. You're kind, genuine, clever, and I love your humor."
    mc "But, let me also add... you're also incredibly hot, Luna."
    mc "Your body, your face, and your eyes – they're simply irresistible."
    show fl 104
    l "T-Thank you..."
    show fl 105
    l "And oh, I forgot!"
    l "I also like that I can touch you with my hands without getting visions."
    l "It makes me feel more... connected to you."
    show fl 103
    mc "You should take off those gloves, then."
    mc "You can touch all you want."
    show fl 104
    l "*Giggles* Okay..."
    play sound untie
    show fl 106
    bla "Luna begins untying the laces of her gloves." with dis15
    play sound2 clothes3
    scene fl 107
    l "*Breathing nervously* . . ." with dis15
    mc "*Chuckles* So?"
    mc "You're scared to touch now?"
    show fl 108
    l "I'm not!"
    l "I mean..."
    l "With anyone else, I might be. But... not with you."
    show fl 107
    mc "Hmm, I don't know, you look pretty scared to me."
    mc "You might have to convince me otherwise."
    show fl 109 with dis12
    mc "Ah, I see..." with dis
    mc "Is that all, though?"
    play sound2 clothes3
    scene fl 110
    bla "Luna's fingers trace a path up your chest, reaching toward the back of your head, where she cups your neck with a gentle embrace." with Dissolve(1.9)
    play sound rubbody
    play sound3 wood volume 0.4 fadein 1
    scene fl 111
    l "{sc=2}*Twitching* MMmm-m-m-mmmmhh......{/sc}" with dis12
    mc "L-Luna? You okay?"
    l "*Purring like a cat* Mmmmrr-mhhh-hmm."
    l "Y-Your skin is so warm."
    mc "Oh."
    l "It feels... good."
    l "T-Touching someone else, I mean."
    scene fl 112
    l "Will I ever get used to this feeling?" with dis08
    mc "Through enough practice? I'm sure of it."
    mc "But it'll never stop feeling good, don't worry."
    play sound chair3
    scene fl 113
    bla "Luna leaps back into your arms, initiating another passionate kiss. Her fingers eagerly weave through your hair, tracing the lines of your neck with tender caresses." with dis12
    mct "Oh, man..."
    mct "I never thought I'd see Luna acting so passionately."
    mct "And I fucking love it."
    play sound rubbody
    play soundlow chair2
    scene fl 114
    l "*Putting her feet back onto the ground* MMmmmmmmhh..." with dis15
    mct "I love how she can't keep her hands on a single place."
    mct "As if she wanted to map every inch of me."
    scene fl 115
    mct "And the way she molds her body to mine, refusing to release her grip..." with dis15
    mct "God, she turns me on so much."
    play sound2 wood volume 0.4
    scene fl 116
    l "*Leaning forward* Mmmmmh..."with dis14
    mct "Oh shit, please don't–"
    play sound rubbody
    scene fl 117
    l "*Leaning back* Mmmmh?" with dis
    mc "Um... s-sorry, I..."
    mc "I got too excited."
    show fl 118
    l "Is that..."
    show fl 119
    mc "...Yes."
    mc "Sorry."
    show fl 118
    l "No, no, it's okay."
    l "I just... wasn't expecting it."
    show fl 119
    mc "Yeah..."
    mct "This is awkward."
    mc "Um..."
    mc "If you give me one minute..."
    l ". . ."
    l "Hmm."
    mc "You okay?"
    play sound clothes
    scene fl 120
    bla "Luna lowers herself to her knees, moving with such deliberate slowness that it feels as if time itself is moving in slow motion." with dis25
    mct "W-What is going on...?"
    mc "L-Luna?"
    l "Do you want me to..."
    l "Help you...?"
    mc "Wha..."
    scene fl 122
    mc "W-What did you just say?" with dis15
    scene fl 121
    l "If you want to."
    scene fl 122
    mc "I..."
    mc "I mean..."
    mc "I-I would like to, yeah."
    mct "Jesus Christ, just seeing Luna in this position, speaking like that... I can feel the blood rushing to my cock."
    mc "Are you sure, though?"
    show fl 121
    l "Yeah."
    l "I want to do it."
    show fl 123
    if lunamassagefail:
        l "I would probably have done it already if I hadn't panicked at my uncle's place."
    else:
        l "*Giggles playfully* I mean, I was about to do it anyway at my uncle's place, right after your... massage."
        l "I would probably have done it already if my dad hadn't interrupted."
    l "I guess I owe it to you."
    show fl 122
    mc "So you really wanted to do that right before you left the terrace! I thought it was all in my head."
    show fl 123
    l "*Giggles* I suppose now that I promised you to be completely transparent, I can't keep secrets from you anymore."
    show fl 122
    mc "Well, if I can be sincere too, I will admit that right now you're driving me wild down there..."
    show fl 121
    l "Let me lend a hand, then."
    l "Let me... help you feel good."
    l "Like you helped me."
    play sound clothes3
    play sound2 ["<silence 1>", zip] volume 0.4
    scene fl 124
    mc "*Reaching for your zipper* Oh man..." with dis15
    mc "Very well, then..."
    play sound3 clothes3
    play sound4 clothes4
    scene fl 125 with dis2
    l ". . ." with dis
    mc "Ahh, much better..."
    l "Wh..."
    l "W-Wow."
    show fl 126
    mc "All good?"
    show fl 125
    l "I mean... y-yeah."
    l "I guess."
    l "I..."
    l "I wasn't sure of what to expect, but... wow."
    l "H-How can you keep all that inside your pants...?"
    l "Aren’t you in swimming class?! How do you hide it in your trunks?!"
    show fl 126
    mc "Well... I'm usually not this... excited."
    show fl 125
    l "Ah."
    l "Yeah."
    l "That... makes sense."
    l ". . ."
    l "Can I... touch it?"
    mc "Of course... I thought that was the whole point."
    scene fl 127
    l "Ah... y-yeah... of course."with dis15
    l "Sorry, I'm a bit jittery."
    mc "No need to be, Luna."
    mc "There's literally nothing you could do that would be wrong."
    scene fl 128
    l "That's... reassuring." with dis15
    scene uefuefneubf
    bla "Luna playfully trails her fingers along, mimicking tiny legs as they saunter up to your manhood."with dis2
    l "Hmm..."
    mc "Now grab it..."
    play sound rubbody
    play sound2 ["<silence 0.3>", bodycollide]
    play sound3 ["<silence 0.3>", bodycollide]
    scene nvruiwoqww
    l "{sc=2}*Twitching* M-M-Mmm-m-m-mmmhh . . . . . .{/sc}" with dis
    mc "O-Ohhh god..."
    mct "I fucking love the way she twitches each time she touches me with her bare hands..."
    scene fl 131
    l "*Pulling herself together* Mmmh..."with dis
    mc "Y-You okay?"
    l "Mm-hm..."
    play soundlow wood2 fadein 1
    play sound2 clothes3
    $ renpy.music.set_volume(0.6, delay=7.0, channel='music3')
    scene lunah1 with dis22
    bla "Luna draws near, so close that your dick nearly reaches her face, her touch moving in a teasingly slow, deliberate motion." with dis12
    mc "O-Ohh my fucking god, yes..."
    l "It's so... warm..."
    l "So hard..."
    l "I can feel it... on my hand!"
    l "*Giggles playfully* It's pulsing!"
    mc "Y-Yeah..."
    mct "Oh dear, she's so close..."
    mct "My cock is literally skimming her lips."
    l "I didn't know giving “massages” could be as fun as receiving them."
    mc "R-Right?"
    l "Yeah..."
    mc "Aahh..."
    mc "Y-You know, maybe..."
    mc "You should take those clothes off, Luna...?"
    l "My... clothes?"
    l "What for?"
    mc "Well..."
    mc "Now I could probably come up with some silly excuse, but I value this newfound honesty policy between us."
    mc "The truth is, I just want to see you naked again so fucking badly."
    l "*Giggles* Ah, I see..."
    play soundlow wood2
    play sound2 clothes3
    play sound3 belt
    scene fl 133 with dis12
    bla "Luna sidles away, her playful smirk lingering as she begins to unfasten her hunter corset." with dis
    mct "Fuck yes..."
    play sound5 clothes
    stop sound3 fadeout 1
    scene fl 134 with dis17
    bla "She slips out of the leather corset, unveiling a tight black shirt that perfectly contours her slender figure." with dis12
    mc "That shirt looks good on you... although it doesn't seem very breathable."
    show fl 135
    l "Yeah... it really isn't."
    l "It almost feels like a thermal t-shirt."
    l "Good for hunting demons, but perhaps not so much for... alternative activities."
    l "It was actually making me sweat a bit."
    show fl 134
    mc "So I could actually have come up with an excuse after all."
    mc "What a wasted opportunity."
    l "*Snorts* Mm-hm."
    play sound clothes3
    scene fl 136 with dis17
    pause
    play sound5 buttons volume 0.4
    play sound2 clothes3
    play sound3 clothes
    scene fl 137 with dis2
    bla "Luna slips off her shirt, revealing, indeed, faint traces of sweat on her porcelain skin." with dis
    mc "Jesus fucking Christ..."
    show fl 138
    mc "Simply... wow." with dis12
    if lunamassagefail:
        mc "Your tits are so perfectly shaped..."
    else:
        mc "I had forgotten how perfectly shaped your tits were."
    play soundlow wood
    scene fl 140
    l "*Standing up* Oh, please." with dis12
    scene fl 139
    mc "I'm serious."
    mc "I mean... just look at you!"
    mc "So... oof."
    scene fl 140
    l "*Giggles* Stop giving me that smirk!"
    l "*Giggles* It makes me jittery!"
    show fl 139
    mc "I can't help it."
    mc "Topless Luna Hernandez and the silly smirk on my face go together."
    mc "It's a reflex."
    play soundlow wood
    play sound clothes3
    scene fl 141
    bla "Luna strides towards you with surprising confidence, pressing your dick against her belly." with dis14
    play sound2 clothes2
    show fl 142
    l "*Lifting your face mask up* Hmm." with dis
    mc "*Chuckles* Ahh, fair enough."
    play sound3 wood fadein 1
    $ renpy.music.set_volume(0.45, delay=7.0, channel='music3')
    play soundloop handjobslow fadein 4 volume 0.2
    scene lunah2 with dis22
    bla "Luna gracefully kneels down before you and starts jacking you off again." with dis
    mc "Ohhh yeah, babe..."
    mct "Oh my god, her face is so close again..."
    mct "I wanna put my cock inside her little cute mouth so bad..."
    mct "I {i}need{/i} to."
    mct "Should I try it? Or at least... ask?"
    mct "I mean, it's Luna we're talking about, I already can't believe she's doing what she's doing."
    mct "Although... I bet she's yearning for physical contact. She's been missing it all her life because of her condition."
    l "Am I doing it right...?"
    mc "Fucking perfect."
    mct "Maybe..."
    mc "Are you sure you don't wanna take off your pants too, though?"
    l "My pants?"
    l "Is it because you're concerned about me sweating or because you want to see more of me...?"
    mc "Why not both?"
    l "Hah."
    l "Okay..."
    l "I guess I can do that..."
    mc "Fuck yes..."
    stop soundloop fadeout 1
    play sound footsteps
    scene fl 144 with dis15
    play sound chair2
    mc "*Sitting on a nearby box* Please, don't mind me." with dis
    mc "I'm just getting a better seat for the show."
    show fl 145
    l "*Playfully giggles* You're so silly, you know that?" with dis12
    mc "A silly, but happy man."
    show fl 146
    l "*Unfastening her belts* Ah, that usually goes together, you're right..."with dis12
    play sound beltdrop
    show fl 147 with dis12
    pause
    play sound2 clothes5 volume 0.4
    show fl 148 with dis17
    mct "Oh wow, she's wearing a thong!" with dis
    mct "And oh god, that body..."
    mc "Please, come back here, Luna."
    mc "I need it."
    mc "NOW."
    scene fl 149
    l "I haven't even fully taken off my pants yet!" with dis 
    show fl 150
    mc "There's no need."
    mc "It's sexier this way."
    show fl 151
    mc "You're not gonna leave me hanging now, are you?" with dis
    l "*Giggles* You're lucky I'm so nice. The kindest soul some people have ever met, I hear..."
    mc "*Chuckles* Lucky me indeed..."
    mct "I adore seeing Luna at ease, playing along."
    play sound clothes
    scene fl 152 with dis2
    bla "Luna elegantly walks towards you and crouches between your legs." with dis
    mc "That's right..."
    play soundloop handjobslow fadein 4 volume 0.16
    scene lunah3 with dis22
    mc "Aaahh, yeah, that's it..." with dis
    mc "*Meticulously examining every inch of Luna's naked body* (Jesus, she's fucking breathtaking.)"
    mct "And she's entirely for me and me alone..."
    mc "Aaahh, yes..."
    mc "Are you still having fun being on the giving side?"
    l "Mm-hm."
    l "I feel so..."
    mc "Horny?"
    l "*Giggles* Y-Yes."
    mc "Are you enjoying the feeling of running your hands along my cock?"
    l "I am..."
    l "It... t-turns me on."
    l "Caressing your... big... t-thing."
    mc "*Chuckles* (She's just as cute and innocent as she looks.)"
    l "I-I'm sorry, I never talked about sex with my family, s-so... saying gross stuff out loud still feels a bit... embarrassing."
    mc "Don't worry, you can ask me whatever you want."
    mc "We can explore whatever you want... together."
    l "I'd like that..."
    menu:
        with dis
        "Let her continue [mt](no bj variation)":
            mct "As much as I'd like to push her a little further, I can't ask her for much more."with dissolve
            mct "She's already way out of her comfort zone."
            l "*Slight moan* Mmmm..."
            mct "She's obviously so turned on, though."
            mct "Maybe it's my turn to give something in return..."
        "[gr]Ask her for a blowjob":
            $ lunablowjob = True
            mc "Agh... I can't bear the teasing anymore, Luna..." with dissolve
            mc "Do you think you could... maybe... use your mouth?"
            scene lunah4 with dis22
            bla "Luna moves her face even closer and starts giving you small kisses on the tip of your shaft." with dis
            mc "O-o-oohhh, Jesus, now that level of teasing is just pure evil..."
            l "There's no way I can fit your huge... {i}c-cock{/i} inside my mouth, [mc]."
            l "It’s too big for me, I think..."
            mct "She said “cock”!"
            mc "Not even the tip?"
            mc "I'm sure you can do it..."
            l ". . ."
            l "It's too big..."
            mct "Maybe she needs a little more time..."
            l "*Slight moan* Mmmm..."
            mc "Well, in that case..."
    play sound chair2
    play sound2 clothes3
    stop soundloop fadeout 1
    scene fl 153
    bla "You suddenly stand up and lift Luna off the floor." with dis12     
    l "U-uh?"
    mc "You're horny as fuck, aren't you?"   
    l ". . ."
    l "*Whispering* Yes..."
    mc "Do you want me to take care of you too?"
    mc "We can have fun together."
    l ". . ."
    mc "You don’t have to be shy here... it’s just you and me."
    mc "Just open up and say what's on your mind, like we talked about before!"
    mc "There are no taboo topics with me, no bad questions."
    l "I know..."
    mc "You want me to play with your pussy, don't you, naughty girl?"
    l ". . ."
    if lunamassagefail:
        mc "You want me to make you cum? Leaving you breathless and dazed...?"
    else:
        mc "You want me to make you cum, like I did last time? Making you all breathless and dazed...?"
    l ". . ."
    scene fl153
    l "*Nods*"
    play sound clothes3
    play sound2 clothes3 fadein 1
    play sound7 wood2 fadein 1
    scene fl 155
    mc "Good girl..." with dis14
    l "*Moans* AAAaaaahh..."
    bla "You start caressing Luna's lips through her underwear's thin fabric, as she instinctively closes her legs."
    mc "You're so wet..."
    l "AAahh..."
    mc "Do you want me to stop...?"
    l "N-NO..."
    play sound whoosh6
    play soundlow clotheswhoosh
    scene fl155
    pause .15
    play sound2 ["<silence 0.5>", beltdrop]
    play sound3 bootsdrop
    scene fl 157
    mc "*Lifting Luna so fast her boots slip off* How about we make ourselves a bit more comfortable then?"with dis08
    show fl 158
    l "W-Wow, you're so strong."
    l "Um... more comfortable, y-yeah, sure."
    l "That sounds... good."
    play sound clothes2
    play sound2 clotheswhoosh
    scene fl 158b
    bla "You remove Luna's trousers entirely and toss them across the room." with hpunch
    play sound3 chair3
    play soundlow whoosh6
    scene fl 159
    mc "*Sitting down* Better, isn't it?" with vpunch 
    show fl 160
    l "Y-Your..."
    l "I mean..."
    l "Your..."
    l "Y-Your {i}thing{/i} is so close to my..."
    show fl 159
    mc "We've done this before."
    show fl 160
    l "Y-Yeah, but last time you weren't naked."
    show fl 159
    mc "Just relax."
    show fl 160
    l "O-Okay."
    l "Relax."
    l "I can do that."
    play sound rubbody 
    scene fl 161 with dis17
    play sound2 penetration2 volume 0.4
    bla "You gently move your hand towards Luna's already soaking wet pussy and slowly insert two fingers inside of her." with dis12
    scene fl 163
    l "*Moaning* Ooooooohhh my god, [mc]..." with dis15
    l "T-That... felt... good..."
    show fl 164
    bla "As you continue softly massaging Luna's insides, she gradually guides her right hand towards your dick, brushing it with her fingertips." with dis17
    play sound2 rubbody
    play sound3 bodycollide
    scene fl 165
    l "{sc=2}*Twitching* MMmm-m-m-m-mmmmhh......{/sc}" with dis12
    mct "Wow, even her vagina contracts when she twitches like that!"
    l "W-Whoa..."
    l "K-Keep going, please..."
    mc "With pleasure..."
    $ renpy.music.set_volume(0.3, delay=7.0, channel='music3')
    play soundloop wetting3 fadein 3
    scene lunah5 with dis22
    l "AAAAaaaaahhhhh..." with dis
    l "O-Oh my GOD!"
    l "*Moaning* I had f-forgotten... h-how amazing this feels..."
    mct "God, I love her so much."
    l "*Moans* AAaahh..."
    mct "There's something about Luna..."
    mct "I don't know if it's her always sweet, neutral tone of voice, or her always gentle, reserved attitude."
    mct "But seeing her letting out these loud moans... it drives me absolutely wild."
    l "*Moans* Oh f-fuck, [mc]..."
    if lunablowjob:
        mc "Fuck?! That’s the second bad word out of your mouth tonight, Luna."
    else:
        mc "Fuck?! An elegant lady like you shouldn't use such foul language, Luna."
    mc "Bad girl..."
    l "*Giggles* Aaa-ahaahh... y-yeah..."
    l "*Moans* S-Sorry..."
    mct "I wonder if using her hands to touch me while being fingered also increases her pleasure."
    mct "Literally all she's experiencing now must feel like a new world to her."
    l "AAaahhh..."
    l "F-Faster..."
    mc "Huh...?"
    l "G-Go... faster..."
    mc "Hah..."
    mc "You'll see now..."
    $ renpy.music.set_volume(0.2, delay=7.0, channel='music3')
    play soundloop2 wetting4 fadein 3
    stop soundloop fadeout 3
    scene lunah6 with dis22
    l "*Squeals* AAAAAAAaaahhh y-yeah! YEAH!"with dis
    l "*Moans* MMMmmmmMmmmhh..."
    l "*Panting* Oh Dios mio, [mc]..."
    mct "OH FUCK YES, her voice can't be sexier when she speaks in Spanish..."
    l "*Moans* K-K-Keep this p-pace, p-please..."
    mc "I won't slow down one bit..."
    mct "Jesus, she's so fucking tight."
    mct "I can't help but imagine the sensation of penetrating Luna."
    mct "I imagine it has to be an experience bordering on the mystical..."
    l "*Squeals* AAAAaaaaahhh..."
    l "*Moans* D-Diosss..."
    mct "Just seeing the way she squirms at the slightest touch..."
    mct "She's simply craving serious physical closeness."
    mct "And oh boy, I will be there to give her all the affection she needs..."
    l "*Moans* Ooooooohhh my goddd...."
    l "*Moans* I t-think..."
    l "*Moans* I-I think I'm g-gonna come..."
    l "*Moans* I can feel it coming..."
    l "*Squeals* AAAAAaaaaahhHH!"
    mct "Man, she's so fucking hot..."
    l "*Moans intensely* AAAAaaaaaAAAaahhh..."
    mct "I wanna make her scream."
    mct "I wanna make her writhe in pleasure."
    mct "I wanna make her cum over and over again..."
    l "[mc], I'm c-coming...!"
    mc "Me too, Luna, I'm almost there..."
    l "AAaahh..."
    l "AAAAAAaAaaghh..."with hpunch
    l "AAAAAAAAAAAAAAAHHHHHH..."with hpunch
    $ renpy.music.set_volume(0.4, delay=8.0, channel='music3')
    stop soundloop2
    play sound2 punch volume 0.3
    play sound3 cum4
    scene fl 166
    l "{sc=2}*Orgasming* MMMMMMmmMMMmmMmMmmmm.......!!!{/sc}" with hpunch
    play sound4 cum4
    l "{sc=2}*Orgasming* MmmmmhhmmmmMMMmMmmm......{/sc}" with hpunch
    play sound5 cum4
    l "{sc=2}*Orgasming* MmmMMMMHHHhhmmMMMmMmmm......{/sc}" with hpunch
    mct "W-Wow, that felt intense."
    play sound wood2
    scene fl 167 with dis2
    play sound2 woodhit
    bla "Luna struggles to rise, managing to crawl for a few feet before succumbing to the floor in exhaustion." with vpunch
    l "*Panting* Wow..."
    l "T-This was even more... vigorous than the first massage."
    mc "And it will only get more intense from this point."
    l "I'm not sure if I'd be able to stand it..."
    mc "Oh, I'm sure you would..."
    play sound ["<silence 0.6>", hay]
    play sound2 chair2
    show fl 168
    mc "*Sitting on the haystack* (Awh man, I was so close to finishing.)" with dis12
    mc "(Just a few more seconds and I would–)"
    play soundlow wood2 fadein 1
    scene fl 169
    mc "H-Huh...?" with dis15
    mc "Luna...?"
    show fl 170
    l "You didn't... finish."
    show fl 169
    mc "Eh... no."
    mc "I was about to, but–"
    play sound2 rubbody
    play sound wood2 fadein 1 volume 0.6
    play sound3 ["<silence 0.4>", bodycollide]
    scene fl 171
    bla "Luna suddenly straightens up and firmly grasps your member with both of her delicate hands. A fierce look of determination flashes across her face." with dis12
    mc "O-Oh Lord..."
    $ renpy.music.set_volume(0.2, delay=9.0, channel='music3')
    play soundloop wetting6 fadein 3
    scene lunah7 with dis22
    mc "O-O-Ohhh god, Luna..." with dis
    mc "Oh, f-fuck yes..."
    l "I want you to finish too..."
    l "I want you to feel... as good as I did."
    l "I want you to teach me... how to give you pleasure."
    mc "Oh, babe..."
    mc "You've got the perfect touch..."
    l "I-It feels so... enormous between my hands."
    mc "You're handling it just right..."
    l "*Giggles* Thank you."
    mc "Aahhh..."
    mct "I swear, I can't resist when she looks at me with this angelic expression of hers."
    l "Like this...?"
    mc "Y-Yeah, keep doing what you're doing..."
    if lunablowjob:
        mc "*Looking at Luna's lips* (Man, this is becoming unbearable...)"
        mct "I-I know she said no, but–"
        play sound2 rubbody
        play sound wood2 fadein 1 volume 0.6
        stop soundloop fadeout 1
        scene fl 172 with dis15
        bla "Almost as if sensing your thoughts, Luna slouches down again and starts licking your shaft." with dis
        mc "G-Goodness gracious..."
        l "*Whispering* This is what you wanted, right...?"
        mc "FUCK YES..."
        mc "Please..."
        mc "Do it..."
        play sound2 ["<silence 0.25>", blow5]
        scene fl 173
        bla "Luna slides her lips over the tip of your dick. You can feel her throat gradually accommodating, overcoming a few reflexes along the way." with dis17
        mc "OOOOOOOhhhhh YES, f-finally..."
        play sound3 blowpop volume 0.5
        scene fl 174 with dis17
        l "*Giggles* Hah..." with dis08
        l "Turns out it could fit in after all..."
        mc "Told you..."
        mc "Now put it back in..."
        play sound2 ["<silence 0.25>", blow5]
        scene fl 173
        l "Mmmmm..." with dis17
        mc "YES..."
        mc "Use your hands too..."
        play sound debris
        play soundloop blowjob2 fadein 3
        scene lunah9 with dis22
        mc "O-O-OOOoooohhh Luna..." with dis
        mc "Exactly like this, yeah..."
        l "*Moans* Mmmmm..."
        mct "At last..."
        mct "My cock is inside Luna's mouth..."
        mct "I can feel her warmth..."
        mct "Her tongue sliding under my cock..."
        mct "And fuck me, it feels as good as I imagined..."
        l "*Gagging* Mmmmm..."
        mc "T-This feels unbelievable..."
        l "Mm-hmmm..."
        pause 
        bla "As Luna finds her own rhythm, she grows increasingly confident with each passing moment, embracing and savoring every second of the new experience." with dis 
        mc "AAAAAahh..."
        mc "Good girl..."
        play sound debris
        play sound2 fallhay
        play soundloop2 blowjob2 fadein 3
        play soundloop3 blowjob2 fadein 3
        stop soundloop fadeout 3
        scene lunah10 with dis2
        bla "You sit back onto the haystack as Luna, undeterred, continues sucking you off, taking your dick even deeper into her tight throat." with dis 
        mc "{sc=2}F-FUUUUUCK...{/sc}"
        mc "LUNA..."
        mc "Oh sweet Lord, y-you're a natural..."
        l "Mmmmm..."
        mct "In the end it will be true what they say about innocent-looking girls..."
        mct "They end up being the freakiest in bed..."
        mc "AAAAaaah, fuck yes..."
        l "*Pressing her hands tight against your body* MMMMmmmmmhh..."
        mct "I can sense it in the way she moans."
        mct "I can see it written all over her face."
        mct "Those innocent features, now twisted by desire... and corrupted by lust."
        mc "J-Jesus fucking Christ, Luna..."
        mc "You're something else..."
        mc "I told you that you could do it, didn't I...?"
        l "MMmmmMm–"
        stop soundloop2 fadeout 1
        stop soundloop3 fadeout 1
        play soundloop wetting6 fadein 2
        play soundloop4 wetting6 fadein 2
        play sound blow4
        play sound2 blow5
        scene lunah8b
        l "*Stopping to recover her breath* AAAaAAAAHHh..." with dis12
        l "*Panting* Y-Yes, yyyyou..."
        mc "T-Take your time, get your breath back..."
        l "*Recovering her breath* W-Wow..."
        l "*Recovering her breath* Y-Yes..."
        l "*Recovering her breath* Yes, y-you did say I could do it."
        l "*Recovering her breath* And I could! I got all of your... d-dick inside my mouth."
        mc "I-I'm sure you're capable of much more than you think..."
        l "*Recovering her breath* Hah... maybe you're right..."
        mct "Even as she struggled for breath, her gaze remained locked on my face. Her hands shuffled back and forth between my cock and her own body."
        mct "This is it, she can't get more uninhibited than she is right now."
        mct "Every barrier she had was completely replaced by the rush of hormones and raw desire."
        mct "Is it wrong that I feel proud about being the one who brought her to this state...?"
        l "I'm ready... to continue..."
        mc "Don't let me stop you..."
        play sound blow5
        stop soundloop fadeout 3
        stop soundloop4 fadeout 3
        play soundloop2 blowjob2 fadein 3
        play soundloop3 blowjob2 fadein 3
        scene lunah10 with dis22
        bla "Luna hungrily takes your dick inside her mouth again, enthusiastically continuing to suck it." with dis
        mc "Fuck yes, that's it..."
        l "Mmmmm..."
        mc "AAaaaaah..."
        mc "Fuck, Luna, I'm gonna cum..."
        play sound2 ["<silence 0.2>", debris]
        stop soundloop2 fadeout 3
        stop soundloop3 fadeout 3
        play soundloop blowjob2faster fadein 3
        play soundloop4 blowjob2faster fadein 3
        scene lunah11 with dis22
        bla "Determined to give you as much pleasure as possible, Luna hastens her pace, surpassing your expectations with a deliciously unanticipated speed." with dis 
        mc "O-O-Ooohhh my fucking god..."
        mc "F-Fuck, Luna, I'm g-gonna cum so much..."
        l "*Gagging* MMMmmmM..."
        mc "I'm almost there... don't stop now..."
        mc "K-Keep that pace..."
        l "*Gagging* MMMmmmmh..."
        mc "Milk that cock, babe..."
        mc "Milk it till it's fucking dry..."
        l "*Gagging* MMMmmmMmmmmhhh......"
        mc "Look at me..."
        mc "That's it..."
        mc "Look at me while you choke on my cock..."
        l "*Gagging* MMMmmmmh..."
        menu cumminglunaattic:
            with dis
            "Cum on her":
                mc "Shit, I'm almost..." with dis06
                mc "I'm cumming!" with hpunch 
                if lunablowjob:
                    play sound blow4
                    play sound2 blow5
                    stop soundloop fadeout 2
                    stop soundloop4 fadeout 2
                else:
                    play sound rubbody
                    stop soundloop2 fadeout 2
                    stop soundloop3 fadeout 2
                scene fl 175b with dis17
                pause .1
                show fl 175
                play sound cumall
                play sound2 cumall
                mc "{sc=2}FFFFFFUUUUCKKK.....{/sc}{w=0.65}{nw}" with vpunch 
                play sound cumall
                play sound2 cumall
                mc "{sc=2}FFFFFFFFFUUUUUUUUUUUCKKKKKKK.....{/sc}" with vpunch 
                scene fl 176
                l "Wow." with dis15
                mc "OOOooooooh, godddd..." 
                mc "That was... glorious..."
                l "Geez, what a mess."
                mc "I'm sorry..."
                l "I-It's okay."
                l "Nothing that can't be cleaned."
                l "I-I've got a cloth right there."
            "Finish in her mouth" if lunablowjob:
                play sound rubbody
                stop soundloop fadeout 2
                stop soundloop4 fadeout 2
                scene fl 177
                mc "Oh f-f-fuck..." with dis
                mc "I'm cumming!" with hpunch 
                play sound cumall
                play sound2 cum3
                play sound3 fallhay 
                play sound4 impactwood
                scene fl 178
                mc "{sc=2}*Kicking the floor* FFFFFFFFFUCKKKKKKK.....{/sc}" with vpunch 
                l "Mmmmgh..."
                play sound cumall
                play sound2 cum3
                play sound3 fallhay
                play sound4 impactwood
                scene fl 179
                mc "{sc=2}AAAAaaaaaaaaghhh....{/sc}" with hpunchlong4  
                l "MMmmmmmmhmhmhh......" 
                play sound blow4
                play sound2 blow5
                show fl 180
                bla "Luna steps back with her mouth brimming with cum, not knowing exactly what to do next." with dis17
                mc "Ooooh, godddd..." 
                mc "That was... glorious..."
                l ". . ."
                play sound swallow
                play sound2 swallow
                scene fl 181
                l "*Swallowing* Mmph." with dis
                scene fl 182
                l "W-Wow." with dis
                l "That was... m-more than expected."
                mc "Yeah... sorry."
                l "I-It's okay."
                l "Easier to... clean, I-I guess."
                mct "She didn't even flinch when swallowing..."
                mct "My little deviant... Who would have thought..."
    else:
        mct "Man, now that she's using both of her hands, this feels like heaven..."
        mct "Only if she went fa–"
        stop soundloop fadeout 1
        play soundloop2 wetting6 fadein 2
        play soundloop3 wetting6 fadein 2
        scene lunah8 with dis22
        bla "Almost as if sensing your thoughts, Luna hastens her pace, determined to give you as much satisfaction as possible." with dis 
        mc "Ooooohhh, L-Luna..."
        l "Does it feel good...?"
        mc "Fucking incredible..."
        mc "P-Please, don't stop."
        l "Okay..."
        mc "Looks like your magic touch is finally doing the trick on me..."
        l "*Giggles* But this specific power is just for you..."
        mc "F-Fuck yeah..."
        play sound ["<silence 0.4>", spit]
        play sound2 ["<silence 0.4>", spit]
        stop soundloop2 fadeout 1
        stop soundloop3 fadeout 1
        scene fl 120b
        bla "Luna spits on the tip of your cock and uses it to lube your member." with dis12
        mc "My little deviant..."
        play soundloop2 wetting6 fadein 2
        play soundloop3 wetting6 fadein 2
        scene lunah8b with dis22
        mc "{sc=2}F-FUUUUUCK...{/sc}" with dis 
        l "Better?"
        mc "Much better..."
        l "*Whispering* Good..."
        mct "She's enjoying this."
        mct "She WANTS this."
        mct "I can sense it in the way she speaks."
        mct "I can see it written all over her face."
        mct "Those innocent features, now twisted by desire... and corrupted by lust."
        mct "Is it wrong that I feel proud about being the one who brought her to this state...?"
        mc "AAAAaaaahhh..."
        mc "J-Jesus fucking Christ, Luna..."
        mc "You're something else..."
        l "Mm-hm..."
        mc "AAAaahhh..."
        mc "F-Fuck, I'm g-gonna cum so much..."
        mc "I'm almost there... don't stop now..."
        l "I won't..."
        mc "Milk that cock, babe..."
        mc "Milk it till it's fucking dry..."
        jump cumminglunaattic
    stop music3 fadeout 10
    play soundloop birds fadein 6
    play soundloop2 birds fadein 6
    play sound clothes
    play sound2 wood2 fadein 1 volume 0.4
    play sound3 debris
    scene fl 183 with dis22
    play sound4 chair2
    mc "*Sitting on the floor* My god, Luna..." with dis 
    mc "You left me empty."
    l "*Giggles* Did I...?"
    mc "For real."
    play sound5 church2 volume 0.35 fadein 1
    play sound6 ["<silence 8.5>", church2] volume 0.35
    mc "I don't even know how you–"   
    l "*Gasps* [mc]!" with hpunch
    show fl 184
    mc "Hmm?" with dis08
    l "The church!"
    mc "Yeah, I hear it. What about it?"
    l "And the sun! It's morning!"
    mc "Huh?"
    $ lunaattic = True
    play sound fallhay
    play sound2 whoosh6
    scene fl185
    mc "*Standing up abruptly* Oh, SHIT, ALREADY?!" with vpunch
    mc "How long have we been here?!"
    scene fl 186
    l "I'm not sure... maybe for an hour?"
    l "Maybe more?"
    scene fl 185
    mc "Damn, Penny must think we're dead!"
    mc "We need to find her!"
    scene fl 186
    l "Yeah! I didn’t realize, we should get going."
    l "Penny’s clever and resourceful, so I’m not too worried... but still, there’s no telling what those hunters could get up to."
    l "At the very least, she’ll be worried about us."
    scene fl 185
    mc "Yeah, definitely."
    mc "Let's find her and get out of this damn town once and for all!"
    show fl 186
    l "*Trying to cover herself* Y-Yeah!"
    show fl 185
    mc "(It's adorable seeing her shyness return after everything we just did.)"
    mct "That look of hers... she's so fucking cute."
    mct "But damn, she sure gears up when she wants to."
    mct "Dammit... she's starting to get me all riled up again..."
    show fl 186
    l "Shouldn't we... get dressed?"
    show fl 185
    mc "*Clears throat* Ah, y-yes!"
    mc "S-Sorry, I was just thinking through the plan!"
    mc "T-The town!"
    mc "Let's leave it!"
    mc "ONCE AND FOR ALL!"with hpunch
    jump morninghollow


label morninghollow:
    stop music fadeout 6
    stop music2 fadeout 6
    stop soundloop2 fadeout 6
    stop soundloop fadeout 6
    scene black with dis25
    show screen sometimelater with dis15
    pause 
    play soundloop forest2 fadein 3
    hide screen sometimelater
    scene ft 1 
    with dis25
    if lunapath:
        mc "Okay... I remember passing through these small ruins when we arrived." with dis12
        l "Yeah, me too."
        l "If I'm not mistaken, the Exit Portal and the river should be just within a hundred yards."
        mc "Dammit, Penny's still nowhere to be found."
    else:
        if lunabandonbarn:
            bla "You dedicate several hours to searching for Penelope, but with no success. Eventually, the sun rises and you find yourself back at a small set of ruins you saw when you first arrived." with dis12
            mct "Fuck... she’s nowhere to be found. Where the hell are you, Penny?"
            mc "*Sighs* (At least I saw the hunters searching for both Penny and Luna during the whole night.)"
            mct "I guess that's a good sign. It means they didn't find them either."
            mct "Or so I hope."
            l "[mc]?"
        else:
            bla "You dedicate several hours to searching for Luna, but with no success. Eventually the sun rises and you find yourself back at a small set of ruins you saw when you first arrived." with dis12
            mct "Fuck... she wasn't by the church or the windmill."
            mct "Maybe I should have tried looking somewhere else...? She didn't mention any other meeting spot, right...?"
            mct "AGHHH, I should have paid more attention!" with hpunch
            mct "And now I'm nearly back at the Exit Portal, and there's still no sign of anyone here!"
            mct "What if something happened to them?"
            mct "Shit, did I really fail them?!"
            mct "Did I let them die?!!" with hpunch
            mct "DID I–"with hpunch
            l "Hey [mc]."
        scene ft 47
        mc "*Turning around* Huh?" with dis
        mc "LUNA!" with hpunch
        if lunabandonbarn:
            mc "So good to see you!"
            show ft 48
            l "What are you still doing here?"
            l "I thought you were supposed to find Penny and leave the server."
            show ft 47
            mc "That's the problem – I couldn't find her!"
            mc "I've been looking for her for hours, but she's M.I.A.!"
            mc "*Sighs* But at least you’re safe! Definitely a sight for sore eyes!"
        else:
            mc "Thank god, are you okay?!"
            mc "I was so worried!"
            show ft 48
            l "Yeah, I'm alright."
            l "No worries."
            show ft 47
            mc "Oof, thank god."
            mc "Where have you been?"
            show ft 48
            l "I've been hiding in the old barn, waiting for the sun to come up so I could avoid the hunter patrols."
            show ft 47
            mc "The old barn! I knew it!"
            mc "W-Well, I didn't, but I wish I had known."
            mc "But anyway, I'm glad to see you're safe."
        show ft 48
        l "Yeah."
        show ft 47
        mct "Hmm..."
        mct "Her smile seems a bit off today."
        if lunabandonbarn:
            mc "Did anything happen while you waited in that barn?"
            mc "You know you can tell me anything."
        else:
            mc "You sure everything's cool, though?"
            mc "You know you can tell me anything."
            mc "If something happened..."
        show ft 48
        l "I know!"
        l "But everything is okay, I swear!"
        l "I'm just tired, that's all."
        show ft 47
        mct "Well, that actually makes sense."
        mc "Alright... okay then!"
        mc "I'll take your word for it."
        mct "Sometimes it's hard to know what's inside Luna's mind."
        mc "*Sighs* Now we're just missing Penny."
    play sound rungrass
    mc "Do you think we should–{w=1}{nw}"
    play sound whoosh6
    play sound2 debris3
    play sound3 clothes2
    play music2 wvv0 fadein 11
    stop soundloop fadeout 20
    scene ft2 
    p "{sc=2}GUUUUUUYYSSS!!!{/sc}" with hpunch
    l "Penny!"
    mc "W-Whoa!"
    scene ft 3
    mc "Speaking of the devil! It's so good to see you!" with dis
    p "Oh my god, I was so worried!"
    p "I thought something terrible had happened to you!"
    mc "We were the worried ones!"
    mc "Have you been here the whole time?"
    play sound whoosh3b volume 0.7
    scene ft 5 
    p "*Dismounting you* Not at all!" with hpunch
    p "So much has happened that I couldn't possibly cover it all!"
    scene ft 8
    l "Tell us the short version, then!"
    scene ft 4
    p "Short version...? OKAY! Yeah, short version!"
    play sound2 inhale volume 0.5
    scene ft4b
    p "*Takes a deep breath*{w=0.8}{nw}"
    play sound2 whoosh6
    scene ft4
    p "OkayrememberwhenwesplitintownandIwenttofindthosevampiresright?!"
    scene ft 5b
    mc "W-What?"with hpunch 
    mc "Breathe and don't speak so fast!"
    p "Mm-hm!"
    scene ft 5
    p "O-Okay."
    p "So, as I was saying, I went to find those vampires, and..."
    scene ft4
    if vampireshelp:
        p "THEN I stumble upon this old cemetery, creepy monsters everywhere, when suddenly whoop, there's [mc]!" 
        p "We meet Lord Iliescu, nice talk, good people, zip back to Hollowbrook, but wait! [mc] hears someone tailing us, so we split again!"
    else:
        p "THEN I stumble upon this old cemetery, dark, scary, creepy monsters everywhere, yes? But WAIT because in the same place I also meet Lord Iliescu, his wife, and this cool butler Mortimer – good folks!" 
        p "Lysandra sniffs my tits, they're like, “yo, want some drink?” Not blood, just wine! Had a chat, said bye-bye, zoomed back to Hollowbrook!"
    p "Then I get there, and I'm hearing these peeps talking about killing innocent centaurs, and I'm thinking, “man, these guys are nuts!”"
    p "So I start looking for you, I can't find you anywhere, then, whoosh! I spy four dudes heading into the forest. I tail them, and I catch them trying to ambush a centaur family, with babies and everything!"
    p "I'm like, “HEY!” – I shout it out loud. Centaurs hear me, hunters show themselves, chaos breaks out, hunters die, and the centaurs are all, “wow, thank you, come meet the king!” and I'm like “well, okay I guess.”"
    p "So, I tag along, and bam, meet the king, everyone's chilling, and then he's like “so, do you wanna be my queen?” and I'm like “whaaaaaat?”"
    p "And he's like “we can breed some half-human, half-horse lineage!” and I'm thinking, “but aren't centaurs already half-human, half-horse...?”"
    mc "W-What?"
    p "So anyway, that question distracts them and causes a huge debate, so I use it to sneak out, and I head back to town!"
    p "Then I find this injured woman, I use restoration magic to patch her up, then bam! Her husband shows up, and I'm like, “ OH FUCK!”"
    p "But surprise, he's actually super grateful! They say Father Bakhar is crazy, they help me find a way out of town, and point me to this keep."
    p "I get here, no one's around. I wait ten minutes, meet a funny squirrel and a mushroom that I could swear moved, 5 more minutes, and..."
    scene ft 5
    p "BOOM! I finally find you both!" with hpunch
    scene ft 5b
    mc "W-Wow."
    mc "And did all of this happen... today?"
    p "Mm-hm."
    mc "H-Holy shit."
    mc "*Laughs* Going on an adventure with you sure guarantees a wild ride."
    show ft 8
    l "The important thing is that you're safe and sound!"
    play sound rubbody
    show ft 9
    p "Awww, thank you Luny!" with dis
    p "Your sweet voice always takes all of my stress away."
    if not lunapath:
        mct "Even if Penny doesn't realize it, she's had that same effect on Luna."
        mct "She looks a lot happier since she showed up."
    p "But anyway, enough talking about myself! Tell me, how was your ride?"
    if lunapath:
        show ft 11
        l "W-What ride?" with dissolve 
        l "I didn't r-ride anything."
        l "I just..."
        l "We, uh, just..."
        show ft 12
        mc "...we just hid in one of the town's buildings."
        mc "There were a lot of hunters patrolling the streets, so we stayed put until dawn."
        show ft 10
        l "Y-Yeah! Exactly."
        l "It wasn't safe to venture out with them around."
    else:
        show ft 10
        l "We don't really have a cool story to tell like you."
        l "I just hid in one of the town's buildings and stayed put until dawn to avoid the hunters patrolling."
        show ft 13
        mc "Yeah, we regrouped here just a minute before you showed up."
    show ft 9
    p "Well, I agree, the important thing is that you're safe and sound!"
    play sound gunload
    stop music2 fadeout 6
    play music2b wvv2 fadein 6
    bak "I wouldn't be so sure about that..." 
    scene ft 14
    bla "As you slowly turn around, you find the leader of the hunters, Father Bakhar, pointing a gun at you." with dis15
    mct "Oh, man, not this guy again..."
    if not werewolvesside and not vampiresside or mod_vamp_wolf:
        mc "Um... look, we were about to leave."
        mc "If you let us go our way, we won't get in yours."
        bak "Hmm."
        play sound holster
        scene ft 36
        bak "*Stopping to point at you* Of course, of course." with dis12
        bak "Don't worry, we came here in peace..."
        bak "No need to get so defensive."
        show ft 37
        mc "And what's up with your “I wouldn't be so sure about that”, then?"
        show ft 36
        bak "I simply mean that these woods hold danger, that's all."
        bak "We've got to protect our friends from the demons."
        show ft 37
        mc "Of course..."
        show ft 36
        bak "But I'm glad I bumped into you."
        bak "I wanted to thank you personally."
        show ft 37
        mc "Thank me? For what?"
        show ft 36
        bak "Well, today's hunt was a huge success thanks to you."
        show ft 37
        mc "Thanks to me...?"
        show ft 36
        bak "Show them our trophy, Geoffrey."
        if vampireshelp:
            show ft 38
            bla "One of the hunters that came with Father Bakhar steps closer, clutching a blood-stained bag." with dis15
            bak "Open it."
            play sound baghead
            scene ft38
            bla "The hunter starts untying the bag, and something tumbles out.{w=3.2}{nw}"
            scene ft38b with hpunch 
            mc "Oh–{w=1}{nw}" with dis 
            mc "OH, F-FUCK!" with hpunch
            mc "I-Is that..." 
            mc "L-Lord Iliescu?"
            show ft 44
            p "Oh god, I think I'm gonna puke."
            p "That's disgusting."
            show ft 39
            bak "I don't know."
            bak "I never bothered to learn its name."
            bak "He was the leader of the vampires, that's what matters."
            show ft 36
            bak "He ventured to our town, apparently because you told him we had a healer capable of curing his wife, or so he said." with dis12
        else:
            show ft 40
            bla "One of the hunters that came with Father Bakhar steps closer, clutching a blood-stained bag." with dis15
            bak "Open it."
            play sound baghead
            scene ft40
            bla "The hunter starts untying the bag, and something tumbles out.{w=3.2}{nw}"
            scene ft40b with hpunch 
            mc "Oh–{w=1}{nw}" with dis 
            mc "OH, F-FUCK!" with hpunch
            mc "I-Is that..." 
            mc "F-Fangrend?"
            show ft 46
            l "Ugh, I can't even look at it."
            l "It's just so dreadful."
            show ft 41
            bak "I don't know."
            bak "I never bothered to learn its name."
            bak "He was the leader of the werewolves, that's what matters."
            show ft 36
            bak "He ventured to our town, apparently because you told him we had a shaman capable of curing their curse, or something." with dis12
        bak "That was a clever ruse."
        bak "It was easy to drug him and decapitate him when he lay unconscious."
        show ft 37
        mc "Really...? Was this truly necessary?"
        show ft 36
        bak "Don't play the saint now."
        bak "Someone has to get their hands dirty."
        bak "And if no one else has the nerve, I will."
        show ft 37
        mc "*Sighs* I guess."
        show ft 42
        bak "Anyway, we've got to head back to town." with dis12
        bak "The other monsters could initiate a revenge attack any time now."
        bak "If you ever need help, you can reach out to us."
        bak "Hollowbrook won't leave a fellow demon hunter hanging."
        mc "I'll... keep that in mind."
        mc "Goodbye."
        bak "HUNTERS! We're leaving!" with hpunch
        stop music2b fadeout 7
        play soundloop forest2 fadein 6
        scene ft 35 with dis2
        bla "Your newfound allies disappear into the woods as they make their way back to Hollowbrook." with dis12
        mct "Fuck, this is not how I expected the day to end."
        mct "But, on the bright side, we've got some new powerful allies, I guess. Though their methods are somewhat... questionable."
        mct "And I don’t know how welcome they’ll be on other servers."
        mct "But... well, if we're really supposed to liberate all the NPCs from Ulysses, this is definitely a huge first step."
        if vampireshelp:
            scene ft 43
            mc "*Turning towards Penelope* Well, that was a pretty rough ending to this short tale, I'll admit."with dis12
            scene ft 44
            p "That was so disgusting."
            p "Is... is Lord Iliescu's head still there...?"
            show ft 43
            mc "Um... yes."
            show ft 44
            p "Jesus... they're way worse than the “monsters” they claim to pursue."
            show ft 43
            mc "Yeah, I have to agree."
            show ft 44
            p "Lord Iliescu didn't deserve this."
            show ft 43
            mc "No, he didn't."
            mc "*Sighs* But I guess this is something we'll have to deal with if we really want to “free” all the NPCs from Ulysses."
            mc "With free will comes human nature."
            mc "And human nature can be... something scary."
            show ft 44
            p "Yeah... that's an understatement."
        else:
            scene ft 45
            mc "*Turning towards Luna* Well, that was a pretty rough ending to this short tale, I'll admit."with dis12
            scene ft 46
            l "That was so disgusting."
            l "I can't even imagine how Duke and Burpee will feel when they find out about this."
            l "Should we try to warn them?"
            show ft 45
            mc "They're certainly quirky, but they're not stupid. They'll spot those hunters from a mile away."
            mc "They might even have bolted by now, for all we know. Plus... I don’t know how trustworthy they’ll find other humans after this."
            show ft 46
            l "I hope you're right about them escaping..."
            l "These hunters are far worse than the m-monsters they claim to chase."
            show ft 45
            mc "Yeah, I can't argue with that."
            show ft 46
            l "Fangrend didn't deserve this."
            show ft 45
            mc "No, he really didn't."
            mc "*Sighs* But I guess this is something we'll have to deal with if we really want to “free” all the NPCs from Ulysses."
            mc "With free will comes human nature."
            mc "And human nature can be... something scary."
            show ft 46
            l "Yeah... I guess you're right."
        scene ft 1
        mc "I don't know about you, but I can't wait to get the fuck out of this server." with dis15
        l "Please..."
        l "This last encounter left a bad taste in my mouth."
        p "Yeah, I wish I could just erase it from my memory."
        mc "I know it's a lot to ask, but try not to dwell on it."
        mc "Empty your mind!"
        p "Some of us sure have less to empty."
        l "*Chuckles*"
        mc "*Laughs* Okay, I'll take one for the team."
        if mod_vamp_wolf:
            scene black with fade
            mod "Another path..."
            scene ft 14 with dis2
            jump mod_nohunters
        jump posekabar07
    label mod_nohunters:
    mc "Um... look, we were about to leave, so..."
    show ft 15
    bak "You thought you were so clever, didn't you?"
    show ft 16
    mc "Yeah, yeah, you caught us."
    mc "We're magic users, and no, we're not actually hunters."
    mc "But hey, we're outta here for good now, so if you don't mind..."
    show ft 15
    bak "No, that's not gonna happen."
    show ft 14
    mc "I'm sorry?"
    show ft 15
    bak "Your existence ends here."
    bak "I will kill you and fulfill my duty to purge the world of the devil's spawn."
    show ft 14
    mc "*Sighs* Don't try it, man."
    mc "I really don't wanna hurt you."
    show ft 17
    bak "*Chuckles*" with dis14
    show ft 18
    bak "Do you know what I hold in my hand, demon?"
    show ft 17
    mc "I know what a gun is, yes."
    mc "I'm more surprised you know about it. I thought you were still stuck on slingshots and pitchforks."
    show ft 18
    bak "Not just any gun... a dimeritium one."
    show ft 17
    mc "Dimeritium...?"
    mct "Wasn't that the stuff in the shackle around Calypso's neck?"
    show ft 18
    bak "From your face, I'm guessing you know what it does."
    bak "It doesn't matter what magic tricks you've got. Teleporting, pyrokinesis, turning into who-knows-what."
    bak "As soon as I pull the trigger, all magic in a 10-foot bubble gets zapped."
    bak "You and your friends will die like the dogs you are. And I? I will be rewarded for having faith, beyond measure..."
    show ft 17
    mct "That dimeritium stuff shouldn't affect me, right...?"
    mct "But... what if it does? If it blocked Calypso's magic, why wouldn't it shut down my powers too?"
    mct "Fuck..."
    mc "What do you want? If you didn't want anything from us, you would have killed us already."
    show ft 18
    bak "Ah, smart."
    show ft 15
    if vampireshelp:
        bak "The vampires. I know you've met them."with dis12
    else:
        bak "The werewolves. I know you've met them."with dis12
    bak "I want to know where they're hiding, and how many of them are there."
    bak "Tell me... and I'll let you live."
    show ft 14
    mc "Hmm."
    mct "Shit, I can't betray them like that."
    mct "Not after how nice they were to us."
    mc "*Gesturing to the girls to back off* Yeah, no."
    show ft 15
    bak "Excuse me...?"
    show ft 14
    mc "Fuck you. I won't tell you shit about them."
    mc "Ask something else."
    show bakharsss with dis17
    bak "*Breathing heavily* Something... else...?" with dis
    bak "D-Do you really believe you're in any position to negotiate, you insolent fool?!"
    scene ft 16
    mc "You would have pulled the trigger regardless."
    scene bakharsss
    stop music2b fadeout 20
    play sound risinglong1 fadein 5
    play sound2 risinglong1 fadein 13
    bak "*Laughs maniacally* Hahaha... you know what..."
    bak "{sc=2}YOU'RE FUCKING RIGHT I WOULD!{/sc}"
    bak "{sc=2}I AM BUT THE INSTRUMENT OF THE LORD...{/sc}"
    bak "{sc=2}TASKED WITH ERADICATING EVIL FROM THIS WORLD!{/sc}"
    bak "{sc=2}NOW EMBRACE YOUR DEMISE, YOU DEMONS!{/sc}"with hpunch
    bak "{sc=2}AND DIEEEEEEEEE!!!!!!{/sc}"with hpunch
    stop music2b
    play sound2 holster
    stop sound
    scene ft20
    pause 3.4
    bak ". . ." with dis08
    scene ft 22
    bak "Huh...?" with dis12
    bak "What...?"
    play music lunaquirky fadein 5
    play sound wheezing volume 0.6 fadein 2
    show ft 23
    bur "*Wheeze laugh* HAHAHAHA I can't believe that actually worked!" with dis15
    play soundlow rocks volume 0.4
    scene ft 24
    duk "*Laughs* T-The motherfucker really tried to shoot with the violin!" with vpunchslow
    play sound3 wheezing volume 0.6
    bur "*Wheeze laugh* What a jackass!"with vpunch 
    show ft 24b
    l "Hi guys!"
    bur "{sc=2}HI LUNA!!!{/sc}" with hpunch
    duk "{sc=2}YOU SMELL AS GOOD AS EVER!!{/sc}" with hpunch
    if vampireshelp:
        show ft 24c
        mc "D-Do you know them?"
        show ft 24b
        l "I do! They're the guys I met at the werewolves' hideout."
    show ft 23
    bak "W-What... what are these things?"
    bak "How did you do that?!"
    bak "Are my eyes... bewitched?"
    show ft 25
    ili "Fear not, Father."
    ili "The only magic involved here is the unnatural speed of my kin."
    show ft 27b
    p "Lord Iliescu!"
    show ft 27c
    ili "Ah, Lady Penelope..."
    ili "Your radiance shines even brighter in the light of day."
    show ft 27b
    p "Aw, thank you!"
    if werewolveshelp:
        show ft 27c
        mc "D-Do you know him?"
        show ft 27b
        p "I do! He's the Lord of the Vampire clan I met at that cemetery!"
    show ft 23
    bak "No, no... this is impossible..."
    show ft 25
    ili "Not impossible at all."
    ili "You perceived my people as mere animals to be hunted, but the reality is they can possess discipline when... properly guided."
    play sound7 steam2 fadein 4
    play sound holster
    scene ft 26
    ili "They're capable of moving swiftly... even beyond the perception of human sight." with dis12
    ili "Of course, it helped that you were so oblivious that you didn't even notice how we swapped your firearm for one of our instruments."
    play sound5 monsterbreath
    play sound4 sniff3
    vam "*Sniffing the gun* Hmmmgg..."
    play sound punch
    play sound3 debris3
    play sound4 whoosh6
    play sound2 vampire2
    show ft 27
    mor "*Kicking the creature* Can't you see you're getting burned in the sunlight, you dolt?!" with hpunch
    mor "Stay in the shadows!" with hpunch
    bak "No..."
    play sound risinglong1 fadein 6
    stop music fadeout 15
    show bakharsss with dis17
    bak "No... no... NO..." with dis12
    bak "What is this absurd circus...?"
    bak "I refuse to be ridiculed by these infernal creatures..."
    bak "{sc=2}I WILL NOT TOLERATE IT!{/sc}"with hpunch
    bak "{sc=2}I WILL KILL YOU ALL!{/sc}"with hpunch
    bak "{sc=2}DO YOU HEAR ME?!{/sc}"with hpunch
    bak "{sc=2}I WILL EVISCERATE EVERY SINGLE ONE OF Y–{/sc}"with hpunch
    stop music
    play sound punch
    play sound2 bonebreak
    scene ft 28
    pause .9
    play sound3 ["<silence 0.2>", fallfull]
    show ft 29 with dis14
    pause
    play sound4 pickup
    play sound5 debris3
    scene ft 30 with dis17
    play music wvvwerewolves fadein 9
    fan "*Picking Father Bakhar up from the ground* Welp, everything seems to have turned out rather well after all, wouldn't you agree?" with dis12
    scene ft 32
    if werewolveshelp:
        if lunawolffight:
            mc "Fangrend!"
            mc "What are you doing here?!"
        else:
            mc "Uh... I-I suppose so, yeah."
            mc "But... who are you?"
            show ft 30
            fan "*Laughs* I suppose it's normal you don't recognize me."
            fan "I'm Fangrend. We had a brief chat in our hideout earlier, when I was a little more... animalized."
            show ft 32
            mc "Oh, right!"
            mc "I knew your voice was familiar!"
        show ft 30
        fan "You see... after our encounter, I pondered for a while with the pack until I finally decided to take action."
        fan "I guess you could say you inspired me."
        fan "I was making my way towards Hollowbrook, evading the hunter patrols, when I crossed paths with Lazarus."
        show ft 31
        ili "A pleasure to meet you, [mc]."
        ili "Lazarus Iliescu, sovereign of Stravenovia, at your service."
        show ft 32
        mc "The pleasure is mine."
        show ft 31
        ili "Penelope mentioned you several times during our brief meeting in our catacombs."
        ili "Looks like her description was... deeply accurate."
        show ft 32
        mc "Is that so?"
        mct "Huh, I wonder what she said..."
    else:
        mc "Uh... I-I suppose so, yeah."
        mc "But... who are you?"
        show ft 30
        fan "My name is Fangrend, proud leader of a pack of valiant werewolves hailing from the western regions of Ekabar."
        show ft 32
        mc "Ohh..."
        mc "Pleasure to meet you, I'm [mc]."
        show ft 30
        fan "I had a feeling. Luna spoke of you often during her time with us."
        fan "Seems her portrayal of you was... remarkably accurate."
        show ft 32
        mc "Is that so?"
        mct "Huh, I wonder what she said..."
        mc "And what are you two doing here?"
        show ft 31
        ili "After our encounter, Mortimer and I deliberated for some time before deciding to take action."
        ili "I was making my way towards Hollowbrook, evading the hunter patrols, when I crossed paths with Lord Fangrend."    
    show ft 30
    fan "The thing is that, after some talking, we came to the conclusion that our motivations aren’t as disparate as we once believed."     
    fan "So we set aside the age-old rivalry between our clans, and decided to collaborate towards a common goal."
    fan "The first step was to dismantle Father Bakhar's influence, halting his corruption of Hollowbrook's citizens."
    show ft 32
    mc "I see..."
    mc "Good. He had to be stopped."
    mc "What are you gonna do with him now?"
    show ft 30
    fan "I'll take him to our sanctuary."
    fan "Some time amongst our community might encourage a... reconsideration of his principles."
    show ft 31
    ili "However, that's a concern for another time."
    ili "I heard you were preparing to leave, I wouldn't wish to detain you or Lady Penelope any longer."
    show ft 32
    mc "Thank you very much."
    mc "Can I make one final request, though?"
    mc "Whenever he wakes up... could you ask him where he got that dimeritium gun? I'm interested."
    show ft 30
    fan "Of course, we'll check on that for you."
    show ft 31
    ili "We'll gladly share any findings with you the next time we cross paths."
    show ft 30
    fan "And if you ever need assistance in these lands, don't hesitate to reach out."
    fan "You've got allies in Ekabar."
    show ft 32
    mc "The feeling is mutual."
    mc "You can count on us."
    show ft 34
    fan "Alright, boys, we're done here!" with dis12
    fan "Duke, Burpee, back into the fold!"
    bur "Yes, sire!"
    duk "Bye, Luna!"
    show ft 33
    ili "Indeed, it's time for us to depart as well." with dis12
    ili "Let's return to Lysandra, Mortimer."
    mor "Yes, sir."
    mor "Farewell, Lady Penelope."
    scene ft 35 with dis25
    bla "Your newfound allies disappear into the woods as they make their way back to Hollowbrook, taking Father Bakhar along with them." with dis15
    mct "We've gotta swing by again, no doubt about it."
    mct "Both of them look like solid allies, at least in this server."
    mct "And if we are really supposed to “free” all the NPCs from Ulysses, this is definitely a huge first step."
    scene ft 13
    mc "*Turning towards Luna and Penelope* Well, that was a pretty happy ending to this short tale, huh?"with dis12
    show ft 9
    p "Definitely!"
    p "We have to come back, no question!"
    p "I've gotta introduce Luna to Lysandra someday."
    show ft 10
    l "And you have to meet Duke and Burpee, you'll love them!"
    scene ft 13
    mc "But let's leave that for another day!"
    mc "I seriously NEED to go back to the real world now."
    mc "PLEASE."
    scene ft 1
    p "*Chuckles* Yes, yes!" with dis15
    p "Let's leave before we stumble into some random war between dwarves and talking mushrooms or something."
    l "Or before you bump into those centaurs again."
    p "*Laughs* Oh god, that'd be even worse."
    mc "Are you absolutely certain about declining their offer to become their queen, Penny? Imagine the advantages, a race of half-human, half-horsies at your beck and call."
    p "*Laughs* Shut up!"
    jump posekabar07


label posekabar07:
    stop soundloop fadeout 5
    stop music fadeout 5
    play sound risingshort4
    scene login3 with dis22
    pause 5.8
    play soundlow whoosh4
    scene white with dissolve
    play soundloop night2 fadein 5
    scene ft 49 with dis08
    play sound2 beep
    pause 
    play sound3 plugin
    play sound4 clothes3
    mc "*Removing your E-Visor* (And back to the real world...)" with dis08
    mc "(Feeling {b}exhausted{/b}, as usual.)"
    mct "What time is it, even?"
    play sound6 clothes3
    mc "*Looking at your phone* (Ugh, nearly 5AM.)"
    mct "I'm supposed to wake up for school in 3 hours."
    mct "Ugh."
    mct "Makes me wonder, though... nights in Ekabar are slightly shorter than on Earth. Curious."
    mct "Well, I guess Eternum is still Earth."
    mct "Just a different... plane? Dimension?"
    mct "Or maybe not...? What if there's another planet somewhere in the vast Universe where we're teleported through the neural implant...?"
    mct "Or where our astral projections are..."
    mc "*Yawns* (O-Okay, enough of my crazy internal monologues for now.)"
    mc "*Hugging your pillow* (Time for sleep.)"
    if lunapath:
        play sound3 vibration
        play sound2 vibration
        blank "{i}Your phone buzzes."
        mc "Hmm?"
        mct "Oh, it's Luna."
        call chat(luna_chat3) from _call_chat_16
        if goodnightluna:
            mc "*Chuckles* (God, she's adorable.)" with dissolve
            mct "I just wanna hold her close and never let go."
            mc "*Relieved sigh* (I needed this little chat, things ended a bit abruptly in Hollowbrook.)"
            mct "I really love how cute and innocent she is, but damn, she really opened up to me earlier."
        else:
            mct "Man, Luna really opened up to me earlier." with dissolve
        mct "In every sense..."
        mct "Can't wait to spend more time with her."
        play sound clothes3
        mc "*Getting comfy* (But now... seriously, it's time to sleep.)"
    mct "Three hours of rest are better than none."
    mc "*Yawns* (I'm sure I'll wake up... as fresh as...)"
    stop soundloop fadeout 6
    scene black with Dissolve(3.3)
    mct "A head of... lettuce..." with dis14


label friday07:
    play sound alarmclock volume 0.8
    scene ft 50 with hpunchlong
    play music2 letsgo
    pause .1
    mc "W-W-Whaat...?" with dis
    show screen fridaycorner
    mc "Where am I? What time is it?!"with hpunch 
    n "*From downstairs* Come on, everyone, wake up!"
    n "You're gonna be late!"
    mct "Oh fuck me, have three hours passed already?!"
    mct "I just closed my eyes..."
    p "Move, move, move!"
    p "I have a photoshoot today and my hair needs to be flawless!"
    if penelopepath:
        mct "Oh right, it's photoshoot day!"
    else:
        mct "Oh right, Penelope's going to her photoshoot today."
        mct "I wish I could have joined her..."
    d "Fuck off, it's my turn to shower!"
    p "You haven't showered yet?! Then why... OH SHIT, what’s that behind you??"
    d "*Turning around* Huh? Where?"
    play sound doorslam
    p "*Closing the bathroom door* Sorry! It's urgent!" with hpunch 
    play sound knock1
    d "Goddammit, Penny, open up!" with hpunch 
    mc "*Chuckles* (At least it looks like the little sleep didn't affect Penny's energy.)"
    mct "Alright then, let's finish the week."
    mct "LET'S GO!" with hpunch 
    play sound ding
    scene black
    hide screen fridaycorner
    show screen afewhourslater
    pause .3
    play sound5 ding
    hide screen afewhourslater
    scene ft 51
    pause
    play sound6 ding
    scene black
    show screen afewhourslater
    pause .3
    play sound7 ding
    hide screen afewhourslater
    scene ft 51b
    pause
    play sound4 ding
    scene black
    show screen afewhourslater
    pause .3
    play sound ding
    hide screen afewhourslater
    scene ft 52
    pause
    play sound3 ding
    scene black
    show screen afewhourslater
    pause .3
    play sound2 ding
    hide screen afewhourslater
    scene ft 53
    pause
    play sound ding
    scene black
    show screen afewhourslater
    pause .3
    hide screen afewhourslater
    scene classtime 1 
    play sound3 ding
    pause 
    scene classtime 2 
    play sound4 ding
    pause 
    scene classtime 3 
    play sound5 ding
    pause 
    play sound7 ding
    play sound6 ["<silence 0.45>", schoolbell] volume 0.4
    play sound ["<silence 0.15>", ding]
    play sound2 ["<silence 0.3>", ding]
    play sound3 ["<silence 0.45>", ding]
    scene ft 54 with hpunch 
    pause 
    mc "*Taking a deep breath* Mmmmmhhh..." with dis17
    mct "Finally, the last class of the day."
    mct "Boy, what a marathon of a week."
    prof "Alright everyone, that wraps it up for today... Have a nice weekend!"
    class "Goodbye, Mr. Keating!"
    scene ft 55
    mc "Hmm?" 
    play sound2 zip volume 0.3
    play sound ["<silence 0.4>", noise3]
    scene ft 56
    bla "You look at Luna as she neatly tucks away her things into her bag."with dis
    mc "You got any plans for the weekend, Luna?"
    scene ft 57
    if lunapath:
        l "I do!" with dis
    else:
        l "I do, actually." with dis
    l "Tomorrow I'm gonna be playing with Alex while you're in the pirate server."
    l "And today I'm helping my dad at the cafe."
    show ft 58
    mc "Ah, I see!"
    if penelopepath:
        mc "I'm meeting with Penny in a few minutes."
        show ft 57
        if lunapath:
            l "I know! I'd wait for her with you, but I have to run. The regular barista at Loco's on Fridays couldn't make it, so I've got to fill in."
            l "Sorry for leaving in such a rush."
        else:
            l "Yeah, I know. I'd like to see her too, but I have to run."
            l "The regular barista at Loco's on Fridays couldn't make it, so I've got to fill in."
    else:
        mc "You're even busier than Penny!"
        show ft 57
        l "Yeah, sorry for leaving in such a rush."
    show ft 58
    mc "Oh, no worries!"
    mc "Give your dad a “hey” from me!"
    show ft 57
    if lunapath:
        l "I will!"
        l "See you later, [mc]!"
    else:
        l "Sure. See you."
    show ft 58
    mc "Bye!"
    play sound chairmove
    scene ft 59 with dis17
    mct "It's pretty sweet how, even amidst all the chaos in our lives, we still find time for the little things and kick it together." with dis08
    if lunapath and daliapath and anniepath and alexpath:
        mct "Hmm, I wonder what the gang at school would say if they knew me and Luna, Dalia, Annie, or Alex are a little more than just “pals”."
    elif lunapath and daliapath and anniepath:
        mct "Hmm, I wonder what the gang at school would say if they knew me and Luna, Dalia, or Annie are a little more than just “pals”."
    elif lunapath and daliapath and alexpath:
        mct "Hmm, I wonder what the gang at school would say if they knew me and Luna, Dalia, or Alex are a little more than just “pals”."
    elif lunapath and anniepath and alexpath:
        mct "Hmm, I wonder what the gang at school would say if they knew me and Luna, Annie, or Alex are a little more than just “pals”."
    elif daliapath and anniepath and alexpath:
        mct "Hmm, I wonder what the gang at school would say if they knew me and Dalia, Annie, or Alex are a little more than just “pals”."
    else:
        mct "Very sweet."
        mct "I mean, isn't this what makes us human after all?"
        mct "Sometimes I wonder what–"
        jump keatingstopsmonologue
    mct "I mean... I’ve caught their looks. Some would totally be jealous, heh."
    show ft 55
    if penelopepath:
        mct "And not only that... I’m about to meet Penelope to tag along to one of her photoshoots!"with dis14
        mct "Bet some of these dudes drool over her Insta pics..."
    else:
        mct "Bet some of these dudes drool over their Insta profiles..." with dis14
    mct "Boy, life is good!"
    mc ". . ."
    play soundloop twirl fadein 2 volume 0.33
    scene ft60
    mc "*Spinning your pen* (Although...)" with dis
    mct "This makes me wonder... would the girls be mad if they found out I'm fooling around with the others?"
    mct "I’ve never thought about it... maybe I should start."
    scene ft62
    mct "I mean... I'm not “officially” dating anyone, and no one's popped the exclusive question, so... I'm not doing anything wrong, am I...?"
    mct "I really don't want to hurt anyone."
    scene ft60
    mct "But nah, they shouldn't be too upset, I think."
    mct "Like, I wouldn't be upset if they wanted to explore something between themselves."
    mct "On the contrary, that might even be kinda hot."
    scene ft62
    mct "Although... would I get jealous if I caught one of them flirting with some other dude?"
    mct "Hell yes, I would. I'd even be annoyed if they were flirting with another girl outside our “circle”."
    mct "Does that make me a hypocrite...?"
    scene ft60
    mct "Probably..."
    mct "But truth is... fuck, I can't change how I feel. And I just can't help but love them all."
    mct "{i}Like{/i} them all."
    mc ". . ."
    scene ft62
    mct "Did I say “love”? Hmm."
    mct "I mean, I love them, but do I {i}love{/i} them?"
    mct "Shit, is this... love? Am I in LOVE with them? With ALL of them?"
    mc ". . ."
    mct "Have I ever actually been in love before...?"
    scene ft60
    mct "Like, what even is love anyway, am I right?"
    mct "I mean... what is “love” but a consumerist, societal construct that–"
label keatingstopsmonologue:
    stop soundloop
    play sound2 slam
    play sound4 slam3
    play sound kickball
    play sound3 ["<silence 0.5>", drop]
    scene ft 64
    prof "[mc!u]!!!{w=0.6}{nw}" with vpunch 
    scene ft 65
    mc "U-U-Uhh??! M-Mr. Keating!" with dis
    show ft 66
    prof "Didn't you hear me?! Class is dismissed!"
    show ft 67
    mc "Oh! Yes! S-Sorry, Mr. Keating, I was, uh..."
    show ft 66
    prof "Lost in thought again, right?"
    show ft 67
    mc "N-No, Professor!"
    show ft 66
    prof "Come on, [mc]! We both know better."
    prof "Your mind's often elsewhere, caught up in your own world!"
    show ft 67
    mc "N-No, Professor!"
    mc "I-I mean... well, yeah, sometimes, but I'm working on improving that!"
    show ft 66
    prof "I bet you didn't even pay attention in class."
    show ft 67
    mc "No, I did!"
    mc "Fascinating class, Professor!"
    show ft 66
    prof "Oh, really? Then I'm sure you won't have any issues if I ask you a couple of questions?"
    show ft 67
    mc "Not at all, Professor."
    show ft 66
    prof "What are the differences between prokaryotic and eukaryotic cells?"
    show ft 67
    mc "Prokaryotic cells lack a nucleus and organelles; eukaryotic cells have both."
    show ft 66
    prof "What are the stages of mitosis?"
    show ft 67
    mc "Prophase, metaphase, anaphase, and telophase."
    show ft 66
    prof "What is the function of the Krebs cycle?"
    show ft 67
    mc "Generating high-energy molecules and ATP through the oxidation of acetyl-CoA derived from carbohydrates, fats, and proteins."
    show ft 65
    prof ". . ."
    show ft 68
    mc ". . ."
    show ft 65
    prof ". . ."
    show ft 66
    prof "You think you're so clever, don't you?"
    show ft 67
    mc "N-Not really, Professor."
    mc "I just have a good memory and knack for certain things."
    mc "Other areas? Total mess."
    show ft 65
    prof ". . ."
    show ft 68
    mc ". . ."
    prof "Did you do something different with your hair?"
    show ft 67
    mc "Uh... it's a bit longer now."
    show ft 65
    prof "Hmm."
    show ft 66
    prof "It suits you. Takes me back to my younger days."
    show ft 67
    mc "T-Thank you, Professor."
    show ft 66
    prof "I used to have a magnificent mane, you know?"
    show ft 67
    mc "I-I'm sure of it, Professor."
    show ft 65
    prof ". . ."
    show ft 68
    mc ". . ."
    show ft 65
    prof ". . ."
    show ft 66
    prof "Alright, you're free to go!"with hpunch 
    prof "Go home and study!"
    prof "I expect top marks on next week's test!"
    show ft 65
    mc "Yes, Mr. Keating!"
    stop music2 fadeout 8
    play soundloop forest2 fadein 5
    play soundlow schoolbell fadein 1
    scene ft 69 with dis3
    mct "Phew, finally." with dis
    mct "For a second, I thought he was going to threaten me with expulsion again."
    mct "Although... I have to admit that, despite his constant scolding, I genuinely appreciate Mr. Keating."
    mct "I know he means well."
    mct "And to be honest, he's right, sometimes I stay in my own world for too long."
    mct "Alright, no more overthinking!"
    mct "From now on, it's all about living in the present!"
    mct "Send me distractions, Universe!" with hpunch 
    play sound floorsqueak
    play music2 happy15 fadein 8
    stop soundloop fadeout 7
    show ft 69b
    c "*Drifting through the hallway* MY MAN!" with dis17
    mct "Damn, that was fast."
    mc "HEY CH–"
    play sound2 changrun
    scene ft 70 with Dissolve(0.17)
    scene ft 71 with Dissolve(0.17)
    scene ft 72 with Dissolve(0.17)
    scene ft 73 with Dissolve(0.17)
    scene ft 74 with Dissolve(0.17)
    scene ft 75 with Dissolve(0.17)
    scene ft 76 with Dissolve(0.17)
    scene ft 77 with Dissolve(0.17)
    scene ft 78 with Dissolve(0.17)
    scene ft 79
    c "*Hyperventilating* Y-YES! I knew it was you!" with dis14
    c "I'd recognize those broad, masculine, thick, solid, tight shoulders from a mile away!"
    show ft 80
    mc "*Chuckles* Thanks, bro."
    show ft 79
    c "Those muscular, powerful thighs and th–" 
    show ft 80
    mc "D-Don't beat around the bush!"with hpunch 
    mc "What's the matter?"
    show ft 79
    c "S-Sorry, I'm nervous."
    c "I was about to ask Micaela out on a date."
    c "Like, an official date. Not as friends. I want to ask her to be my girlfriend."
    show ft 80
    mc "Oh man, that's great!"
    show ft 79
    c "I was supposed to meet her to go back home together, and when I was about to ask her... I-I panicked and dashed here to find you instead."
    show ft 80
    mc "You mean like... right now?"
    mc "A-And you left her there hanging?"
    show ft 79
    c "I told her I had a sudden bathroom emergency."
    show ft 80
    mc "Oh... okay, that might even work."
    show ft 79
    c "I need your advice, man."
    c "I need you to guide me. You're my pillar, the rock I lean on."
    c "Please!"
    show ft 80 
    menu:
        with dis
        "[gr]Go for it":
            $ changaskmicaelaout = True
            mc "You're at the threshold, Chang."with dis08
            mc "You really like this girl. And it seems like she feels the same about you."
            mc "You've been laying the groundwork for this moment over the past few weeks."
            mc "All the little moments you've shared together."
            if micatickets:
                $ changmicaela += 2
            elif micadumbbell:
                $ changmicaela += 1
            elif micaflower:
                $ changmicaela += 1
            if micatickets or micadumbbell or micaflower:
                mc "The birthday gift."
            if changmoneymovies:
                $ changmicaela += 1
                mc "The day you invited her to the movies."
            mc "Your unwavering support during the gym competition."
            if changshirts:
                $ changmicaela += 1
                mc "Even the self-confidence you've built making those awesome shirts for all of us."
            mc "IT'S ALL LED YOU TO THIS MOMENT!" with hpunch
            mc "So you're going to head back to her, ask her out on an incredibly romantic date, and begin a beautiful love story with the woman of your dreams."
            show ft 79
            c "Yes."
            show ft 81
            c "YES!" with dis
            c "I'm doing it!"
            c "Right now!"
            c "And she's going to say yes!"
            show ft 82
            mc "Hell yeah!"
            mc "Just be confident, and everything will be just fine."
            mc "Good luck, buddy."
            show ft 81
            c "Thanks, man."
            show ft 82
            mc "Anytime!"
        "Don't ask her on a date":
            mc "Um... I think this might not be the best time, Chang."with dis08
            mc "You're clearly too nervous at the moment."
            mc "I know you really like this girl, and it seems like she feels the same way about you, but asking her out right now might lead to regrets."
            mc "You should wait for a moment when you feel more confident."
            show ft 79
            c "Yes..."
            show ft 81
            c "Yes, that makes sense." with dis
            c "I should wait for the right moment! Rushing this might make me regret it forever."
            c "She's special, you know?"
            show ft 82
            mc "Exactly!"
            show ft 81
            c "I feel a lot more relaxed now. Thank you."
            show ft 82
            mc "Anytime, man."
    show ft 81
    c "You're really good at lifting others up. You're a born leader!"
    c "No wonder you've got so many beautiful girls going crazy about you."
    show ft 82
    mc "*Chuckles* If you say so."
    show ft 81
    c "Okay, I'm heading back to Micaela!"
    if changaskmicaelaout:
        c "I feel a lot more confident now."
    c "Thanks again, brother!"
    c "And sorry I came to bother you."
    show ft 82
    mc "Don't even mention it."
    mc "And no worries, you'll never be a bother."
    if changaskmicaelaout:
        mc "Tell me all about it next time!"
        show ft 81
        c "Will do!"
    else:
        mc "See you Monday?"
        show ft 81
        c "Sure thing!"
    c "Good luck finding those Gems of yours!"
    show ft 82
    mc "Thanks!"
    play sound run
    show ft 69 with dis2
    mct "Man, I genuinely hope that relationship goes well."with dis08
    mct "I'd really hate to see Chang heartbroken."
    if penelopepath:
        mct "But anyway, speaking of dates..."
        mct "I should start heading to the meeting spot with Penny too."
        mct "A professional agent shouldn't keep his client waiting. That's not how I handle business..."
        mct "Let's roll!"
    else:
        mc "*Sighs* (Well, time to head home.)"
        mct "Everyone's busy today, so I'll guess I'll just play some video games."
        mct "As much as I love Eternum, sometimes it feels good to just lay back on the bed with a controller and simply relax..."  
        mct "So alright... let's roll!"  
        jump saturday07
    stop music2 fadeout 5
    scene black with dis25
    show screen afewminuteslater with dis17
    pause 
    play soundloop forest2 fadein 5   
    scene ft 83 
    hide screen afewminuteslater
    with dis25
    play soundloop2 town_ambience fadein 9 volume 0.2
    mct "Whoa, what fantastic weather we have today." with dis
    mct "Kredon really looks beautiful when it's not raining."
    play sound caraway2 fadein 6
    scene ft 84
    mct "I've never been to this area. Lots of office buildings and banks." with dis12
    mct "There's definitely more wealth in this town than meets the eye."
    mct "If we can even continue calling it a “town”. With how it’s grown during the past few years, it’s basically a city."
    mct "I can't help but wonder if Ulysses has influenced it all..."
    play music funk fadein 7 volume 0.75
    stop soundloop fadeout 12
    stop soundloop2 fadeout 11
    scene ft 85
    p "Oh my, what a gorgeous fella!" with dis08
    p "Are you here to model in the photoshoot too?"
    $ unlock_look("penelope", 16)
    scene ft 86
    mc "*Laughs* I'm here for the shoot, but not to steal any modeling thunder." with dis12
    mc "I didn't make the cut, I'm afraid. You should see the beauties that work in this industry."
    scene ft 86b
    mc "*Checking Penny out* Then again... damn, girl, you'd probably outshine them all effortlessly." with dis12
    mc "Face, body, that pose... you've got the whole package."
    mc "Would you consider working with me? I promise to elevate your career to new heights."
    scene ft 87
    p "*Laughs* I don't know... I'm hesitant. There are some pretty scandalous tales about agents in the modeling world, you know?"with dis12
    p "I've heard stories about them all being opportunistic perverts."
    show ft 86
    mc "Not me, I can assure you of that."
    mc "If anything were to develop between us beyond a strictly professional connection, it would purely stem from our natural chemistry and mutual sexual attraction."
    mc "No shady, hidden agendas for me!"
    show ft 87
    p "*Chuckles* Oh wow, what a professional."
    show ft 88
    p "In that case... deal. I accept your offer."
    p "You can come with me to the photoshoot."
    show ft 86
    mc "*Chuckles* Sounds great."
    mct "I love these flirty exchanges with Penny."
    mct "She is such a tease..."
    mc "Jokes aside though, I really mean it."
    mc "You look incredible, Penny."
    show ft 88
    p "*Chuckles* Thanks!"
    show ft 86
    mc "I'm guessing this is what you'll wear during the photoshoot?"
    show ft 88
    p "Oh, not really, I'll change once we're there."
    p "Today, I have to pose with a fancy car and model some famous designer’s dress."
    show ft 86
    mc "So this is just your day-to-day outfit?"
    show ft 88
    p "Yeah, it's what I wore at college."
    show ft 86
    mc "Ohh, I see."
    mc "Well, let me say, I absolutely love that top."
    show ft 89
    p "Do you? Thank you!" with dis
    p "It's just something I saw at a local street market – I just couldn't resist it!"
    p "I love how it looks with high-waisted jeans or a skirt. It highlights my waist, but without showing too much, you know?"
    show ft 90
    mc "You've got a good eye!"
    mct "God, the way her boobs jiggled when she turned around..."
    mct "Is she not wearing a bra...?"
    show ft 92
    p "Hmph." with dis
    mc "*Chuckles* What?"
    show ft 91
    p "I've come to recognize that horndog expression by now, [mc]."
    p "What filthy thoughts are dancing through that mind of yours this time?"
    show ft 92
    mc "*Chuckles* I was just admiring how the colors of that top complement your complexion and all those cute moles on your skin."
    p "Hmph."
    show ft 91
    p "Is that all you were admiring...?"
    show ft 92
    mc "And... I must say your breasts look especially... breast-y today."
    mc "I can say that, right? As your manager."
    show ft 91
    p "*Giggles* Yeah, yeah, of course."
    p "Thank you. I'm glad you like them."
    show ft 92
    mct "{i}Liking them{/i} is an understatement..."
    mc "But you know, I was wondering–"
    show ft 91
    p "No, I'm not wearing a bra."
    p "As long as I don't start running or jumping, I don't need it with this top."
    show ft 92
    mc "I see..."
    mc "Am I that easy to read?"
    show ft 91
    p "Like an open book."
    show ft 92
    mc "*Chuckles* Fair enough."
    show ft 91
    p "What's the next thing you're going to ask me?"
    p "If I'm not wearing panties either...?"
    show ft 92
    mc "Nah, I ju–"
    show ft 93
    mc "*Looking at Penny's tight skirt* Wait..."with dis12
    mc "A-Are you serious?"
    mc "You're not wearing underwear??"
    show ft 87
    p "*Snorts* You should see your face right now."with dis12
    show ft 88
    p "Of course I'm wearing panties!"
    p "I'm not crazy enough to spend the whole day in class wearing such a short skirt without undies."
    show ft 86
    mc "*Chuckles* You sure love to keep me on my toes, eh?"
    show ft 87
    p "*Giggles* What can I say, it's one of my favorite pastimes."
    show ft 88
    p "But anyway, we should get going before we miss our session at the studio."
    show ft 86
    mc "Sure! Lead the way."
    show ft 88
    p "Do you mind waiting for a minute here?"
    p "I need to use that public bathroom real quick before leaving."
    show ft 86
    menu:
        with dis
        "[gr]Tease her with the panties":
            $ pennypanties = True
            mc "Ah, going to take off your underwear now that class is over, right?"with dissolve
            mc "Kinky..."
            mc "I like it."
            show ft 91
            p "*Snorts* Who's the tease now, huh??"with dis 
            show ft 92
            mc "Sorry, forget I said anything."
            mc "I know you'd never dare to do something like that."
            mc "Guess these kinds of “games” are for less prudish girls, my bad."
            show ft 91
            p "*Chuckles* HAH! You did not just say that!"
            p "Do you really think that trick will work?"
            show ft 92
            mc "*Chuckles* What trick? I’m just a truth-teller, speaking the truth. Truly."
            p "Mm-hm."
            mc "Feel free to prove me wrong, though."
            show ft 91
            p "I'm going to the bathroom for a touch-up and nothing else. That's all."
            show ft 92
            mc "I'll be right here."
            show ft 91
            p "*Giggles* You’d better be."
        "Nevermind":
            mc "Sure thing, I'll be right here." with dissolve 
            show ft 88
            p "I just need a touch-up. Be right back!"
    scene ft 94 with dis2
    mct "Oh boy..." with dis
    mct "This woman's gonna be the end of me."
    mct "Guess I'm gonna chill over there and wait for her to do her thing."
    mct "Although she looked flawless already, I wonder what she's fixing."
    mct "Women, I guess."
    scene ft 95 with dis27
    play sound2 chair4
    bla "Penelope rounds the corner, finding a quiet spot behind Kredon's bank. She settles by the stairs, taking a moment to breathe." with dis14
    scene ft 96
    p "*Exhaling* Fuuuu..." with dis
    p "Better..."
    play sound rubbody
    scene ft 97
    p "*Groaning* (What on earth is going on with you, Penny?)" with dis14
    p "(You know that all this teasing with him isn't right.)"
    p "(Why are you trying to bring trouble into your life?!)"
    show ft 98
    p "(Agh... everything seemed crystal clear just a few hours ago.)"
    p "(But then I saw him... and now I’m like a middle school girl stressing about her first crush.)"
    p "(Come on girl, have some self-respect.)"
    p "(You said it yourself earlier today, remember??)"
    p "*Groaning* (Hmph...)"
    stop music fadeout 6
    scene ft 102 with dis3
    play sound2 schoolbell volume 0.45
    play music2 quirky8 fadein 12
    show screen earliercorner 
    profc "And remember, in statistics: correlation does not imply causation." with dis14
    profc "Always delve deeper into the data!"
    p "(Why the hell do we have to study stats for a journalism degree...?)"
    show ft 101
    p "*Sighs* (This is so boring.)"with dissolve
    show ft 102
    profc "Tomorrow we'll proceed to an even more thrilling statistical model!"with dissolve
    p "(Please don't say analysis of variance.)"
    profc "Analysis of variance!"
    p ". . ."
    if novapath:
        scene ft 103
        no "*Groaning* MMMmmmmmmmmhhh..."with dis08
        show ft 104
        p "I know, girl, I know... isn't it weird how stats seem to appear in every degree?"with dis12
        p "But hey, I guess it's all part of Kredon University’s whole “core curriculum” thing right? “Excellency in every aspect of life” and all..."
        show ft 105
        no "That's not it..."
        p "Hmm?"
        no "I'm still frustrated about the delay of the final episode of One Piece."
        show ft 104
        p "Oh... I see."
        p "But it was just a delay of a few weeks, wasn't it?"
        show ft 105
        no "But the thing is that I was supposed to watch it with [mc] tomorrow, and I had prepared a ton of pirate-themed things to do with him and... now it's all ruined."
        show ft 104
        p "Oohhh..."
        p "I'm sorry."
        show ft 105
        no "Thank you..."
        show ft 104
        p "So it was like a date?"
        show ft 105
        no "We were–"
        play sound2 whoosh6
        play sound3 chair3
        scene ft106
        no "NO!" with vpunch 
        no "N-Not at all!"
        no "It was more like a... m-meeting between anime fans."
        scene ft 107
        no "Actually, we're going to spend most of the time playing in the pirate server with Nancy to try to find Coyote's Gem!"with dis
        no "We're gonna be WAAAAAY too busy for anything else."
        show ft 106
        no "I-I mean... it was NOT a date in the first place. It wouldn't have been one even if we had all the time in the world."with dis 
        play sound whoosh6 volume 0.3
        scene ft 108
        p "*Giggles* Are you acting all nervous because I told you that I had a crush on him at the party?"with pl
        play sound whoosh6 volume 0.3
        show ft 106
        no "W-WHAT?! NO!"with pr
        play sound whoosh6 volume 0.3
        show ft 108
        p "Don't worry, I don't mind! We can share."with pl
        play sound whoosh6 volume 0.3
        show ft 106
        no "What?!"with pr 
        no "I don't..."
        no "I mean..."
        no "You wouldn't..."
        no "I..."
        no "WHAT?!"with hpunch 
        play sound whoosh6 volume 0.3
        show ft 108
        p "I'll actually see him later today, you know?"with pl
        p "Maybe I'll ask if he's up for dating both of us. Two for the price of one – a hot blonde and a hot redhead!"
        play sound whoosh6 volume 0.3
        show ft 106
        no "S-Stop joking!!!"with pr 
        no "I told you that's not it!"with hpunch 
        show ft 115
        p "*Laughs* Okay, okay."with dis15
        p "*Laughs* Sorry, I was just messing around."
        show ft 109
        no "I-I know."
        show ft 115
        p "*Chuckles* Anyway, I better head to my next class before I'm late."
        show ft 109
        no "C-Can I ask you something before leaving?"
        show ft 110
        p "Ask me something? Of course!"
        show ft 109
        no "Since you mentioned it..."
        no "Is that... still a thing? I mean... [mc]."
        show ft 110
        p "Oh... you mean if I still have a crush on [mc]?"
        p "Uh... no, not really."
        p "I mean... of course I like him, but not in that way, you know?"
        p "It was just... the alcohol talking."
        show ft 109
        no "Oh... I see."
        no "The alcohol."
        show ft 110
        p "Yeah."
        show ft 109
        no "Aha."
        show ft 110
        p "Yep."
        show ft 109
        no "Roger that."
        show ft 110
        p "*Clears throat* Sooo..."
        p "Do you wanna hang out tomorrow?"
        p "Shopping? Just the two of us!"
        p "After you've recovered Coyote's Gem of Doom."
        show ft 109
        no "Sure! Although... [mc] is going to be at my house, so... maybe he'd like to come too."
        show ft 110
        p "Oh! I thought you'd have postponed that too after the One Piece delay."
        show ft 109
        no "Oh."
        no "No, I didn't."
        show ft 111
        no "Aw, shit, should I have?"
        show ft 110
        p "No! I just thought that–"
        show ft 111
        no "Aaaaww, I should have totally canceled that."
        play sound whoosh6
        play sound2 woodhit
        scene ft106b
        no "AAAAAAAAW..." with vpunch 
        no "Why didn't I cancel it?!"
        no "I'm such a fucking mess..."
        show ft 104
        p "You know what... let's do something."
        p "How about spending the whole Sunday together?"
        p "That way, we can share every detail about our weekend!"
        p "A whole day just for me and my BEST friend!"
        show ft 105
        no ". . ."
        play sound chair3
        show ft 112
        no "*Giggles* I-Is that best friend me?" with dis
        show ft 108
        p "Of course! Who else could it be?"
        show ft 112
        no "*Giggles* O-Okay."
        no "*Giggles* Let's go shopping this Sunday."
        show ft 113
        no "Me and my best friend."with dis
        no "Penelope Carter is my bestie."
        show ft 115
        p "Is that a yes, then?"
        show ft 114
        no "Hell yeah! I'm in!"
        no "This way we can celebrate recovering Coyote's Gem!"
        show ft 115
        p "*Chuckles* That's the attitude!"
        p "I trust you guys can do it!"
        show ft 114
        no "We won't let you down!"
        show ft 115
        p "Alright then! It's settled."
        p "Now I've gotta go to the next class or I'm gonna be late."
        p "Catch you later!"
        show ft 114
        no "Yeah, same!"
        no "Later!"
        play sound chairmove
        scene ft 116 with dis22
        bla "Penelope and Nova toss their laptops in their bags and head downstairs, ready to move to the next class." with dis
        p "(Hmmm...)"
        p "(Just the alcohol talking... sure.)"
        p "(It's been days, yet he's still stuck in your mind, Penny.)"
        p "(Every single time you saw him yesterday at the medieval server you...)"
        p ". . ."
        p "(Maybe I'm the one who should cancel today's appointment with him...?)"
        p ". . ."
        p "*Sighs* (Anyway, let's focus on the remaining classes for now.)"
    else:
        p "(And I've still got four long hours ahead of me before meeting [mc].)"
        p "(This is gonna be a looong day...)"
        show ft 101
        p "*Sighs* I better get going."
        play sound chairmove
        scene ft 116 with dis2
        bla "Penelope slides her laptop into her purse and heads downstairs, ready to move to the next class." with dis
        p "(I fail to see how this is going to help me investigate a corrupt politician or interview a famous designer.)"
    p "*Looking at the blackboard* (I wonder if Walter Cronkite was familiar with the Chi-square distribution...)"
    lil "There you are!"
    scene ft 117
    hide screen earliercorner 
    p "Hmm?" with dis
    show ft 118
    p "*Walking towards her* Oh, hey Lily!" with dis15
    p "Do you have stats class now?"
    show ft 119
    lil "Nah, I already did that." with dis12
    lil "I just came here because I have something BIG to tell you!"
    lil "Are you free tomorrow?"
    show ft 120
    p "Uhh... not really. I'm playing with my sister."
    show ft 119
    lil "Playing..."
    play sound whoosh6
    show ft 121
    lil "ETERNUM?!" with hpunch 
    show ft 120
    p "Aha."
    show ft 121
    lil "Then you're in luck, girl, because I just got my own neural implant!"
    lil "We can play together now!"
    show ft 122
    p "No way! Are you serious?!"
    p "That's awesome!"
    p "I'd love to play with you!"
    show ft 121
    lil "Right?!"
    lil "So... what do you say? Tomorrow?"
    show ft 120
    p "I'm sorry, I can’t!"
    p "Like I said, I have a thing with my sister."
    show ft 121
    lil "Sunday, then?"
    show ft 120
    p "I'm meeting Nova."
    show ft 121
    lil "Today?!"
    show ft 120
    p "You already know I have the photoshoot."
    show ft 121
    lil "Ah."
    show ft 121b
    lil "Dammit, you sure are busy."
    lil "I guess I'll have to settle for Marco or Regina for now."
    show ft 124
    p "Huh?"
    show ft 121
    lil "MARCO! I meant only Marco!"
    lil "S-Sorry, I forgot you have some beef with Regina."
    show ft 124
    p "Be honest, are you really into playing, or did you just get the game because I did and you thought it was the new “popular” thing to do?"
    show ft 121
    lil "Ehh..."
    show ft 119
    lil "Anyway, game chat can wait! Let's go to the photoshoot!"with dis08
    show ft 125
    p "What?"
    show ft 119
    lil "You need an assistant!"
    play sound whoosh6
    show ft 121
    lil "And I offer myself!" with hpunch
    lil "*Gasps* Do you think any famous people from Kredon will show up?!"with hpunch
    lil "Because you're posting those pics later, right?!"with hpunch
    lil "DON'T FORGET TO TAG ME!"with hpunch 
    show ft 120
    p "Oh... yeah, the thing is that I already have an “assistant”. Sort of."
    p "[mc] is going with me. Sorry."
    show ft 121
    lil "Oh."
    show ft 119
    lil "Ah."with dis08
    show ft 123
    lil "Ew."with dis08
    show ft 124
    p "What now?"
    show ft 123
    lil "I mean... your step-bro? Really? Ewww."
    show ft 124
    p "What are you talking about, he's not my step-anything."
    show ft 123
    lil "Well, I know, but didn't you practically grow up around him?"
    lil "You even mentioned babysitting him when your mom had to work."
    show ft 124
    p "That literally only happened once, and... yeah, so what?"
    p "That was ages ago."
    show ft 123
    lil "Yeah, but he's still just 18."
    lil "I swear, freshmen are so immature... but high schoolers? Total kids in my book."
    show ft 124
    p "If you say so."
    show ft 123
    lil "And I mean... what if you have to get naked with him around?"
    show ft 124
    p "I don't plan on that happening, don't worry."
    show ft 123
    lil "Yeah, but it can still get weird!"
    lil "Like, imagine if he walks in while you're getting changed!"
    lil "Think about how uncomfortable dinner would be at your place that day!"
    show ft 125
    p "I-I mean..."
    p "Y-Yeah, that would be... SO weird! Haha!"
    p "Him seeing me naked?! N-No way!"
    show ft 123
    lil "I bet he's all about that!"
    lil "Guys these days are just a bunch of perverts, trust me!"
    lil "I wouldn't be shocked if he's plotting some shady “changing room thing” just to pull off some seriously gross moves on you!"
    show ft 125
    p "Oh god, no! Haha!"
    p "That would be so..."
    show ft 126
    p "*Sticking her tongue out* Uggghhh..."
    show ft 125
    p "S-So... gross!"
    p "Definitely NOT what I'd want. Nope."
    show ft 119
    lil "Anyway... as long as he doesn't see more than he's supposed to, it's all good, I guess. I'll leave you to it!"
    show ft 122
    p "A-Aha."
    show ft 119
    lil "Let's catch up later, okay?"
    lil "And be careful with that boy!"
    show ft 122
    p "Y-Yeah, sure, I'll be... careful."
    p "Bye bye!"
    lil "Bye, baby girl!"
    scene ft 127
    bla "Lily exits the classroom." with dis2
    p ". . ."
    stop music2 fadeout 7
    play soundloop forest2 fadein 5   
    scene ft 128 with dis3
    play soundloop2 town_ambience fadein 9 volume 0.2
    p "Hmmm..." with dis14
    p "(Maybe I shouldn't let Lily get to me, but... she's got a point.)"
    p "(This is just weird.)"
    p "(I mean, I can't deny I enjoyed what happened at Regina's dorm. And yeah, I can't stop thinking about him.)"
    p "(But the trouble it'd cause...)"
    p "(How would we even explain this to Mom or Dalia?)"
    play sound rubbody
    $ renpy.music.set_volume(0.6, channel='music3')
    play music3 funk fadein 6
    show ft 129
    p "(That's it. What happened between us was fun and everything, but it's time to move on!)"with dis12
    p "(You can't be fixated on [mc] like some teenage crush, Penny. There's plenty more fish in the sea!)"
    p "(I mean, check out my Instagram DMs! There are tons of hot guys hitting on me literally EVERY DAY.)"
    $ renpy.music.set_volume(0.0, channel='music3')
    stop soundloop2
    stop soundloop
    play sound impact5
    scene ft 130
    pause .37
    play sound2 impact5
    show ftt 131
    pause .37
    play sound3 impact5
    show fttt 132
    pause .37
    play sound4 impact5
    show ftttt 133
    pause
    $ renpy.music.set_volume(0.5, channel='music3')
    scene ft 134
    p ". . ." 
    play sound rubbody
    scene ft 128
    p "(Or maybe it's best to put boys on the back burner for now.)" with dis12
    p "(I'll just focus on my career... or whatever people usually say in these situations.)"
    p "*Sighs* . . ."
    play sound pop
    scene ft 99
    p "(Oh shit, how long have I been here?)"
    p "([mc] must be wondering what's taking me so long.)"
    p "(I should head back before he leaves without me!)"
    play sound2 pop
    scene ft 98
    if pennypanties:
        p "(Should I go along with that joke about taking off my panties, though?)"
    else:
        p "(Should I continue behaving the way I have been around him, though?)"
    p "(If I've truly decided that this isn't going anywhere, should I really continue teasing him?)"
    play sound3 pop
    show ft 97
    p ". . ."
    play sound pop
    scene ft 100
    p "*Standing up* (No, of course not!)"
    p "(What the hell are you thinking, Penny?!)"
    p "(IT'S OVER!)" with hpunch 
    p ". . ."
    play sound pop
    show ft 98
    p "(But then again...)"
    play sound3 pop
    show ft 97
    p "(If I make a big deal out of it, am I not making it less casual than what it should be? Which is exactly what I'm trying to avoid.)"
    play sound pop
    show ft 98
    p "(We're just two friends goofing around.)"
    p "(Maybe I should just keep acting like usual.)"
    p "(I mean... what's wrong with mutual teasing? We're just having fun.)"
    p "(There's nothing wrong with enjoying a bit of playful banter between us.)"
    p ". . ."
    play sound2 pop
    show ft 97
    p "(Right...?)"
    show ft 94 with dis25
    mc "*Stretching out* (Damn, she's taking her time.)" with dis
    show ft 88
    p "*Running* Hi! Pardon the wait!" with dis12
    show ft 86
    mc "Hey! No worries, I was busy people-watching."
    mc "*Looking at Penelope's hair and makeup* (I don't see any difference.)"
    mct "Probably better not to comment on anything..."
    mc "So, ready to go?"
    show ft 88
    p "Yes! The studio's just around the corner, follow me."
    show ft 86
    mc "Right beside you, m'lady."
    stop music3 fadeout 6
    scene black with dis27
    show screen afewminuteslater with dis17
    pause
    $ renpy.music.set_volume(0.6, channel='music3')
    play music3 pennysexins2 fadein 7
    hide screen afewminuteslater
    scene fg 1 
    with dis27
    mc "Ahh, we're here!" with dis12
    mc "So exciting!"
    play sound whistle3
    mc "And damn girl, check out that scaffolding."
    scene fg 2
    mc "This place looks huge. And very professional." with dis 
    show fg 3
    p "Right?"
    show fg 2
    mc "It feels like a huge step up from the first studio we visited." 
    scene fg 3
    p "Oh, because it is!"
    show fg 2
    mc "Is it? I thought the first time you said that one was your favorite studio."
    show fg 3
    p "My favorite at the time!"
    play sound whoosh6
    show fg 5
    p "The modeling world is like climbing a ladder, [mc]!" 
    p "Start at small photo studios, move up to larger ones, then land the cover of the Ulysses magazine..."
    p "And ultimately become someone who can influence the entire world!"
    show fg 4
    mc "*Laughs* I love your optimism."
    play soundlow whoosh6
    show fg 3
    p "Actually, I'm not even kidding – this photoshoot might even get us closer to Ulysses." 
    p "That's why I was so eager to take on this offer."
    show fg 2
    mc "Really? How?"
    show fg 3
    p "It's meant to be used to promote a new racing and car-tuning server."
    p "You know, for those flashy online ads."
    show fg 2
    mc "Oh, seriously? That's awesome!"
    mc "So... the idea is putting a super hot girl next to a car to boost people's attention by 200%%, correct?"
    show fg 3
    p "*Chuckles* I guess that was pretty much their reasoning, yes."
    show fg 2
    mc "Clever bastards."
    mc "But hey, you're right, this could push us closer to Ulysses!"
    mc "It's always a good thing to have more strings to pull."
    show fg 3
    p "Exactly!"
    p "I was happy to be able to contribute something to the team."
    show fg 2
    mc "Don't say that, you've–"
    play sound doorclose2
    show fg 2
    phi "*Slamming the door* UH!" with hpunch 
    scene fg 7
    p "Hmm?" with dis
    scene fg 6
    phi "{sc=2}PENELOPE{w=.5} P. {w=.5}CARTER.{/sc}" with hpunch
    show fg 7
    p "Philippe!"
    show fg 6
    phi "Don't “Philippe” me, darling!"
    phi "I've been waiting for you for thirty long minutes!"
    phi "I told you I need to leave before 6!"
    show fg 7
    p "I know! But you said that you just need 5 minutes to do my hair!"
    p "You can leave afterward!"
    show fg 6
    phi "OH! And does that give you the right to keep me waiting?!"
    phi "People in this town would KILL to have me as their stylist, you know?!"
    show fg 7
    p "I know!"
    p "I'm sorry, Philly, please forgive me..."
    show fg 8
    phi "*Checking Penny out* Hmmm..."with dis
    show fg 6
    phi "Agh, you're lucky you're as stunning as a Vietnamese lotus flower, sweetheart."with dis
    show fg 7
    p "So... you forgive me?!"
    play sound clotheswhoosh
    scene fg7b
    phi "*Pushing Penelope* Yes, but now move, move, MOVE!"with hpunch
    phi "I have a reservation at Cipriani in 40 minutes!"
    scene fg 10
    p "Okay, okay!"
    scene fg 9
    phi "I'll do your hair and leave."
    phi "Your outfit's in the locker behind the main backdrop."
    show fg 10
    p "Ehh..."
    show fg 9
    phi "Don't give me that look – I already adjusted it for your bust, sugar, no worries."
    show fg 11b
    mc "Alright then, I'll go ahead and wait for you in the studio."
    show fg 11
    phi "Hmm?"with dis08
    show fg 13
    phi "Ohh... you brought your photographer friend!"
    phi "Good to see you, [mc]."
    show fg 12
    mc "Thank you, Philippe!"
    show fg 13
    phi "Oh, darling, you look so much better than the last time I saw you."
    phi "What a glow up!"
    show fg 12
    mc "*Chuckles* Thank you."
    show fg 13
    phi "Gosh, I would LOVE to work with your hair."
    phi "A classic men's side-swept hairstyle would look absolutely DIVINE on you!"
    phi "Have you ever thought about giving it a try?"
    show fg 12
    mc "Uh... not really. I don't usually spend much time combing my hair, but... I could try, I guess."
    show fg 13
    phi "Fabulous!"
    phi "I could style your hair myself."
    show fg 12
    mc "Sounds good."
    show fg 13
    phi "We can swing by my place, grab a couple of Cosmopolitans, and–"
    play sound6 whoosh6
    show fg 14
    p "Hey!"with hpunch
    show fg 15
    phi "Oh, honey, don't be jealous!"
    phi "You know you and Paul are the only apples of my eye!"
    show fg 14
    p "Didn't seem like it just a moment ago..."
    show fg 15
    phi "Don't frown so much or you'll get wrinkles on that pretty face of yours!"
    show fg 13
    phi "Anyway, let's get this show on the road."with dis
    phi "It was good to see you again, [mc]!"
    show fg 12
    mc "Likewise!"
    mc "Catch you later, Penny."
    scene fg 1 with dis2
    mct "Alright, I'll go wait for Penny where the photo backdrop is." with dis
    mct "Let's see what they have around here..."
    play sound2 curtain2
    scene fg 16 with dis22
    bla "You make your way around the scaffolds and find a well-equipped space filled with an array of photography gadgets."with dis12
    mct "No fucking way..."
    mct "Is that..."
    play sound carrev
    show fg 17
    mct "Holy shit!" with hpunch
    mct "A Lamborghini!"
    mct "Is Penny supposed to take photos next to it? That's so cool!"
    show fg 18 with dis17
    mc "*Getting closer* (Man, I'd love to drive a lambo someday.)" with dis 
    mct "The sensation of speed has to be incredible."
    scene fg 19
    mct "Hmmm... are there more cars over there?"with dis 
    scene fg 20 with dis17
    mct "I wonder what's hiding under these tarpaulins." with dis
    mct "Maybe GT cars? Rally?"
    mct "Perhaps I should unveil them and have a peek..."
    play sound jumpscare3
    scene fg20
    asp "HANDS OFF THE CARS." with hpunch
    scene fg 22
    mc "F-Fuck, you startled me!" with hpunch
    show fg 21
    asp "All materials presently in the studio belong to Ulysses Inc. and must not be damaged, spoiled, or otherwise exposed under any circumstances."
    show fg 22
    mc "Okay, okay, jeez."
    mc "Who are you anyway...?"
    show fg 21
    asp "Aspen Simmons, Regional Marketing Coordinator at Ulysses Inc., responsible for overseeing publicity productions in Kredon."
    show fg 22
    mc "Why do you speak like a robot...?"
    asp ". . ."
    mc "I-I mean, nice to meet you!"
    mc "I'm [mc] [lastname] – Penelope Carter's representative."
    mc "And... photographer. Manager?"
    show fg 21
    asp "Ah, good. I was about to call you."
    asp "The session has been canceled."
    show fg 22
    mc "Eh? Wait... what? Why?!"
    show fg 21
    asp "The commission was transferred to a more experienced subcontractor."
    asp "Nico Valentino."
    asp "His agency will manage the ad contract with Ulysses Inc. and conduct the session with his own models."
    show fg 22
    mc "WHAT?!"with hpunch 
    mc "You've got to be kidding me, not that dude again!"
    mc "He did the EXACT same thing last time!"
    mc "He also showed up at the studio last minute and tried to kick us out!"
    show fg 21
    asp "Welcome to the modeling world."
    asp "A universe where only connections and owed favors will ever get you somewhere, and real talent doesn't mean shit."
    show fg 22
    mc "Come on, are you really going to let him get away with this?"
    show fg 21
    asp "He controls the studios, he controls the contracts."
    show fg 22
    mc "But we need this session!"
    mc "Penelope was really counting on it!"
    show fg 21
    asp "*Sarcastic tone* I'm devastated by your increeeedibly tragic story, but the answer is still no."
    asp "Now move."
    show fg 22
    mc ". . ."
    menu:
        with dis
        "[gr]Get tough":
            $ aspentough = True
            mc "Okay, no. Just no."with dis
            mc "Fuck you and your shitty attitude."
            mc "We booked this studio for an hour today, we had a prior agreement with the company you work for, and you can't cancel on us on such short notice."
            show fg 21
            asp "It's not my prob–"
            show fg 22
            mc "I swear to god, if you cut us out now, I'll work night and day until you're fired for this and you end up begging for coins in front of Kredon's bank."
            asp ". . ."
        "Bribe her" if money >= 150:
            $ aspenbribe = True
            mc "*Sighs* Okay, I get it." with dis
            mc "How much do you want?"
            asp ". . ."
            show fg 21
            asp "How much do you have?"
            show fg 22
            mc "Ahhh, so now you can suddenly squeeze us in, huh??"
            show fg 21
            asp "You know? Forget it..."
            show fg 22
            mc "No, no, wait!"
            mc "Alright, how about... 100 eternals?"
            mc "I could transfer them to you right now."
            mc "For the... trouble."
            asp "Hmm..."
            show fg 21
            asp "150 eternals. 30 minutes with the Lambo."
            show fg 22
            mct "Greedy bitch..."
            show screen eternals
            with dis
            play sound coins
            $ money -= 50
            pause .05
            $ money -= 50
            pause .05
            $ money -= 50
            pause .3
            hide screen eternals
            mc "Okay, done." with dis08
        "Be nice":
            mc "I understand your position, and I know you're just following protocol, but please!" with dis
            mc "I'm begging you!"
            show fg 21
            asp "I'm sorry."
            asp "There's nothing more I can do."
            show fg 22
            mc "*Sighs* Dammit..."
    show fg 23
    p "What's going on?" with dis12
    show fg 24
    mc "Penny!"
    mc "Wow, you look so pretty!"
    show fg 25
    p "*Giggles* Thanks!"with dis08
    p "Philippe said this style would be the best one for the shoot!"
    p "He said that “it merges elegance with a touch of controlled chaos”, which is the vibe they aim to capture for the racing server."
    mc "He nailed it!"
    show fg 23
    p "Is there any problem, though?"with dis08
    if aspentough:
        show fg 24
        mc "Nothing to worry about. We were just... having a little conversation."
        $ penelope_points += 1
        play sound beat
        show screen heartbeat
        show fg 23b
        p "Yeah, I overheard you arguing."with dissolve 
        p "You sounded... authoritative."
        show fg 23
        p "So, is the... issue resolved?"with dissolve 
        show fg 24
        mc "I'm not sure."
        show fg 26
        mc "Is it...?" with dis
        asp "Hmmm..."
        show fg 21
        asp "Is this your model...?" 
        show fg 22
        mc "Yes."
        mc "An upcoming model set to revolutionize the essence of the Ulysses brand."
        show fg 26
        asp "Hmmm."
        show fg 27
        asp ". . ."
        mc "I mean, look at her."
        mc "My only question is, would you rather be the one who overlooks this opportunity, or the visionary who uncovers her potential?"
        asp "Hmph."
        show fg 26
        asp ". . ."
        show fg 21
        asp "Ooookay... I think I can... squeeze you in before the next client arrives."
        show fg 22
        mc "Excellent!"
        show fg 23b
        p "Oh my, what an agent I have."     
    elif aspenbribe:
        p "I overheard you arguing."
        show fg 24
        mc "Not at all!"
        mc "I was just... finalizing the details with Aspen here."
        show fg 26
        mc "Right...?" with dis
        show fg 21
        asp "Yes... that's right."
    else:
        p "I overheard you arguing."
        show fg 24
        mc "Ehh... maybe."
        mc "Turns out the contract was canceled at the last second."
        show fg 23c
        p "Aw, are you serious?" with dis
        p "Does this mean we have to go home?"
        show fg 23d
        mc "I think so... I'm so sorry, Penny."
        show fg 26
        asp "Hmmm..." with dis
        show fg 21
        asp "Is this your model...?" 
        show fg 22
        mc "Huh?"
        mc "Yes, this is Penelope."
        show fg 26
        asp "Hmmm."
        show fg 27
        asp ". . ."
        asp "Hmph."
        show fg 21
        asp "Okay, I think I can... squeeze you in before the next client arrives."
        show fg 22
        mc "Seriously? That's wonderful!"
        mc "Why the sudden change of opinion, though...?"
        show fg 21
        asp "Are you interested or not?"
        show fg 22
        mc "Y-Yes, yes!"
    play sound clothes4
    show fg 28
    asp "*Taking a tablet out* You have 30 minutes before Mr. Valentino arrives." with dis12
    show fg 23c
    p "Ugh, Valentino? That weirdo is here too?"
    p "How can you work with him?"
    show fg 37
    asp "Yes, yes... he's a repulsive abuser who trades jobs for blowjobs, and we live in a dark world full of corruption and moral decay."
    asp "Now, if I'm to fit you in, I need to rearrange some schedules and create a new profile for you, which will take some time."
    asp "So stop interrupting me and just answer my questions. Got it?"
    show fg 29
    p "Y-Yes. Understood."
    show fg 28
    asp "Alright..."
    mct "Well, at least we get 30 minutes."
    mct "It should be enough to take some good pics."
    mct "I'm happy for Penny."
    asp "Are you from Kredon?"
    show fg 29
    p "Born and raised."
    show fg 28
    asp "Okay..."
    if pennypanties:
        show fg 30
        bla "As she responds to Aspen's questions, you notice Penelope fidgeting and crossing her legs in a nervous yet deliberate manner." with dis14
        mct "Hmm?"
        mct "Why is she doing that? Does she need to go to the bathroom?"
        mct "Or perhaps... wait. No way."
        mct "Did she actually take off her panties when she went to the bathroom??"
        mct "I've gotta verify that..."
        mc "*Clears throat* Well..."
        show fg 31 
        mc "*Getting close to her* Thirty minutes is better than nothing."with dis15
        show fg 32
        p "Definitely!"with dis06 
        p "After we're done setting up the profile, I'll quickly change and head to the car."
        show fg 32b
        p "Just take some shots of me in different poses, that should do it."with dis
        mc "Sounds good."
        bla "You slowly slide your hand beneath Penelope's short skirt."
        play soundlow whoosh3b
        scene fg33
        p ". . ." with vpunch
        show fg 34
        p "*Whispering* [mc]! W-What are you doing??!" with dissolve
        show fg 35
        mc "*Whispering* Oh my, no panties today?"
        mc "*Whispering* You're quite the pervert..."
        show fg 34
        p "*Whispering* I..."
        p "*Whispering* I thought that it would..."
        p "*Whispering* F-Fuck, I don't know what I thought, okay??"
        p "*Whispering* My mind's been a whirl lately, I'm sorry!"
        show fg 35
        mc "*Whispering* Sorry for what?"
        mc "*Whispering* This is super hot!"
        show fg 34
        p "*Whispering* No, it's not, it's embarrassing!"
        show fg 35
        mc "*Whispering* That's what makes it hot!"
        mc "*Whispering* And don't lie to yourself, the risk and the fact that I'm the only one around that knows it... that turns you on, doesn't it?"
        mc "*Whispering* That's why you took them off in the bathroom."
        show fg 34
        p "*Whispering* Um..."
        p "*Whispering* I..."
        show fg 35
        mc "*Whispering* Don't lie to yourself..."
        show fg 34
        p "*Whispering* O-Okay, maybe a bit, now please, stop it!"
        p "*Whispering* This is not the ti–"
        scene pennysh0 with dis2
        bla "She pauses mid-sentence as you smoothly slide one finger between Penelope's pussy lips, beginning to massage her with a rhythmic motion." with dis
        p "*Biting her lip* G-Goddaaaaammit, [mc]...."
        p "*Whispering* P-Please s-stop this nooooow..."
        p "*Whispering* F-Fuck..."
        scene fg 28
        asp "Okay, this is ready."with dis
        asp "Now I'll ask you some personal questions to fill the form, alright?"
        show fg 39
        p "Huh?"
        show fg 38
        p "Ah! Questions, yes! I'm ready! Shoot!"
        show fg 28
        asp "Okay..."
        scene pennysh0
        asp "What's your Instagram account?" with dis
        asp "I'll take your profile photo from your feed and we'll use that to contact you if needed."
        p "Uh..."
        p "I-It's “miss”, underscore, “penny”."
        asp "Hmm..."
        asp "Okay, I see it."
        asp "Damn, 185,000 followers. Not bad."
        asp "Do you have any affiliate links?"
        p "Affiliate? N-No. Not really."
        p "I just get some offers to wear certain outfits sometimes."
        asp "Are you on TikTok? Facebook?"
        p "Only Instagram."
        asp "Uh, you sure are bad at making money."
        asp "Anyway, let's fill in the personal data and get this done with."
        p "A-Aha..."
        p "*Whispering* [mc], stop, please... not now..."
        mc "*Whispering* Your pussy is so fucking wet, Penny. You’re absolutely dripping."
        mc "*Whispering* There's no better lie detector than that."
        p "*Whispering* This is wrong..."
        mc "*Whispering* {i}But{/i}...? I sense there's a “but”."
        p "*Whispering* B-But... fuck, it feels good..."
        mc "*Whispering* So... you want me to continue?"
        p "*Whispering* I..."
        mc "*Whispering* If you want me to stop you just have to say so."
        p ". . ."
        asp "Okay, full name?"
        p "P-Penelope Paige Carter."
        asp "Age?"
        p "21."
        asp "Height?"
        p "5'8''."
        asp "Weight?"
        p "*Moans* Aahhh..."
        scene fg 36
        asp "*Raising an eyebrow* . . ." with dis
        show fg 37
        asp "Are you alright?"
        show fg 38
        p "Yeah!"
        p "S-Sorry, it's something I ate before."
        p "It didn't sit very well."
        show fg 36
        asp "Hmm."
        show fg 28
        asp "Okay, just make sure not to throw up in the photo set."with dis
        scene pennysh0
        asp "Anyway, weight?" with dis
        p "Ehh... around... 143 or 145 lbs."
        asp "Cup size?"
        p "Uhh... 32F."
        asp "32F...?"
        asp "*Mumbling* Some have so much and others so little..."
        asp "Occupation?"
        p "I-I'm studying. Journalism at Kredon University."
        asp "Marital status?"
        p "S-Single."
        asp "Previous experience?"
        p "P-Previous experience?"
        p "Eh... n-not much."
        p "But... I'm willing to... learn... I’m a g-good student."
        p "And I'm... mmmh... tremendously excited to start... w-working with you."
        scene fg 28
        asp "I'm sure you are..." with dis 
        asp "Okay, that should be everything we need."
        asp "You have 30 minutes, starting now."
        play sound2 punch volume 0.3
        play sound whoosh6
        show fg 41
        p "*Pushing you away* AAh! Finally, thank you!" with hpunch
        p "I better hurry up, then!"
        p "D-Do you know where the lockers are?"
        show fg 37
        asp "Behind the main backdrop."
        show fg 41
        p "Thanks!"
        show fg 42
        p "*Clears throat* Alright, be right back! It'll only be a minute!" with dis08
        mc "Let me know if you need a hand with that dress!"
        show fg 44
        p "*Snorts* Hmm." with dis
        mc "*Chuckles* What?"
        show fg 43
        p "Was that a pun?"
        show fg 44
        mc "What pun? I was just asking if you needed any assistance."
        show fg 43
        p "*Giggles* I think I've got this covered, thank you very much." 
        show fg 44
        mc "Always happy to help."
        show fg 43
        p "Ah, so you've been doing nothing but helping me until now?"
        show fg 44
        mc "Absolutely nothing else."
        show fg 43
        p "And how did {i}that{/i} help me, exactly?"
        show fg 44
        mc "I wanted you stress-free."
        mc "A relaxed model is the secret sauce for photo magic. Trust me, as an expert manager, I've got a keen eye for those subtle cues in pictures."
        p "*Snorts*"
        show fg 43
        p "You sound so confident saying all that bullshit that it almost sounds true."
        show fg 44
        mc "*Chuckles* The wanting to help you part was legit, though."
        show fg 43
        p "You're fucking nuts..."
        $ penelope_points += 1
        play sound beat
        show screen heartbeat
        show fg 42
        p "But alright, if you want to continue helping me... go get the camera set and wait for me by the car, expert manager." with dis
        mc "Consider it done!"
        show fg 45
        bla "Penelope dashes off to the locker rooms, giggling playfully."with dis12
        mct "We might have gotten carried away a bit right there, but what I said was kind of true."
        mct "She really looks much more like herself when she's in this mood."
        mc "*Hiding your erection* (Although I need to control myself, this woman turns me on way too easily...)"
        show fg 22
        asp ". . ." (multiple=2) with dis12
        mc "*Turning around*" (multiple=2)
        mc "Um..."
        show fg 21
        asp "Yeah, I don't give a shit about what's going on between you two."
    else:
        asp "Now I'll ask you some personal questions to fill the form, alright?"
        asp "Answer fast and to the point. We don't have all day."
        show fg 29
        p "Fast and to the point, you got it!"
        show fg 28
        asp "Okay, full name?"
        show fg 29
        p "Penelope Paige Carter."
        show fg 28
        asp "Age?"
        show fg 29
        p "21."
        show fg 28
        asp "Height?"
        show fg 29
        p "5'8''."
        show fg 28
        asp "Weight?"
        show fg 29
        p "Something around... 143 or 145 lbs."
        show fg 28
        asp "Cup size?"
        show fg 23
        p "Uhh... 32F."
        p "Although it depends on–"
        show fg 28
        asp "Occupation?"
        show fg 23
        p "I-I'm studying. Journalism at Kredon University."
        show fg 28
        asp "Marital status?"
        show fg 23
        p "Single."
        show fg 28
        asp "Previous experience?"
        show fg 23
        p "Experience...? You mean in modeling?"
        show fg 37
        asp "Yes?"
        asp "What else would I be referring to?"
        asp "I'm not setting up your Tinder profile, you know?"
        show fg 29
        p "*Nervous chuckle* O-Of course."
        p "I don't have much experience, just a couple other photoshoots and my social media."
        scene fg 28
        asp "I see..." with dis 
        asp "Okay, that should be everything we need."
        asp "You can go now."
        show fg 40
        p "Sweet!" with dis
        p "I'll go get changed, then! It'll only be a minute!"
        mc "Sure! Let me know if you need any help!"
        p "Will do!"
        show fg 45
        bla "Penelope dashes off to the locker rooms."with dis12
        show fg 22
        mc "*Turning around* Alright, so what now?" with dis
        show fg 21
    asp "Grab the camera from the table and come with me."
    asp "Let's get this done with."
    show fg 22
    mc "S-Sure!"
    mct "Why is this woman always so angry?"
    scene fg 46 with dis22
    bla "You accompany Aspen to the photoshoot set and get all the necessary equipment set up and ready to go." with dis
    show fg 47
    asp "Okay, you have 30 minutes, you hear me?"with dis
    asp "Thirty."
    asp "And if you happen to run into Valentino, you CANNOT tell him that you're also snapping pics for the new racing server promo."
    asp "I'm putting my job on the line for you two, so you better not fuck this up."
    show fg 48
    mc "30 minutes and not telling Valentino, got it."
    show fg 47
    asp "29 now."
    show fg 48
    mc "*Grumbling* 29 minutes... got it."
    play sound chair2
    show fg 49 with dis12
    asp "*Sitting down* Let me know when you're done. I'm gonna be here." with dissolve
    mc "Are you not gonna give us some tips?"
    asp "Weren't you such an expert? Suit yourself."
    mc "Charming as always..."
    mc "What camera should I use?"
    asp "There's a Reflex on the table. "
    show fg 50
    mc "*Picking the camera up* Oh yeah, I see it." with dis12
    show fg 51
    asp "That thing costs more than a brand new neural implant, so you better watch out."
    asp "You break it, you buy it."
    show fg 50
    mc "Yeah, I always heard photography was such an expensive hobby."
    show fg 52
    mc "Let me get adjusted to it before Penny arrives..."with dis 
    play sound zoomin
    scene fg 53
    show camera
    mc "Okay, this is the zoom... the ISO button... and the manual focus." with dis06
    mc "Say {i}cheeeese{/i}!"
    play sound camera
    show black
    pause 0.08
    hide black
    asp ". . ."
    mc "Do you ever smile?"
    show fg 54
    asp "The SD card is almost full, so I wouldn't fool around if I were you."
    scene fg 55
    mc "You could have said that before I wasted a pic with you."with dis
    show fg 56
    asp "27 minutes."
    mct "I'm gonna kill this woman."
    stop music3 
    play sound2 musicstop
    play sound doorclose2
    show fg 57
    p "Okay, okay! I'm ready, sorry!" with hpunch 
    p "We can begin!"
    $ renpy.music.set_volume(0.4, channel='music3b')
    play music3b pennysexins fadein 9
    show fg 58 with dis2
    $ unlock_look("penelope", 17)
    mc "Whoa..." with dis12
    mc "Holy shit, Penny..."
    show fg 59
    p "Do you like it?" with dis12
    show fg 60
    mc "You look beautiful..."
    show fg 59
    p "Apparently, the NPC who greets you on the server wears this exact outfit."
    p "Or... at least very similar."
    show fg 60
    mc "I have no idea what she looks like, but I feel bad for anyone who joins that server thinking you're gonna be in it."
    show fg 59
    p "*Giggles* Thank you..."
    show fg 61
    asp "25 minutes."
    mc "Okay..."
    mct "I'm so mesmerized by Penny that I can't even summon any anger anym–"
    asp "And stop making that salivating dog expression."
    mct "Although she's certainly testing my fucking patience..."
    show fg 62
    mc "*Clears throat* Um... alright, I'm thinking of snagging a few shots of you sitting on the car first." with dis14
    mc "Then we can do some more with you lying on the hood or maybe even striking a pose on the side. What do you think?"
    p "Sounds great!"
    play sound ["<silence 0.1>", carsuspension2]
    show fg 63
    p "*Sitting on the car* Make sure to make me look pretty!" with dis12
    show fg 64
    mc "Don't worry, making you look anything less than perfect would defy the laws of photography."
    show fg 61
    asp "That was cheesy as fuck."
    mc "CAN YOU SHUT THE FUCK UP?!" with hpunch 
    mc "That was the joke!"
    asp "24 minutes..."
    scene fg 64
    mc "*Taking a deep breath* Okay, sorry." with dis
    play sound zoomout
    show fg 65
    show camera
    mc "*Looking through the camera* Let's start." with dis06
    mc "I like this angle."
    mc "Just let me remove the umbrellas and adjust the lights..."
    play sound2 noise1 fadein 1
    show fg 66 with dis12
    mc "*Going back to the camera* Ah, perfect." with dis08
    play sound camera
    show black
    pause 0.08
    hide black
    mc "Nice."
    mc "How many pictures do we have to send to Ulysses?"
    scene fg 61
    asp "You need to select 4 pictures."
    asp "The only requirements are that the model has to be wearing that dress, and the Lamborghini logo has to be in the frame."
    scene fg 66
    show camera
    mc "Gotcha."
    mc "This is gonna be one..."
    play sound w1
    show fg 67 with pl
    mc "Two..."
    play sound camera
    show black
    pause 0.08
    hide black
    pause 0.08
    play sound camera
    show black
    pause 0.08
    hide black
    pause
    play sound w1
    show fg 70 with pl
    mc "Three..."
    play sound camera
    show black
    pause 0.08
    hide black
    pause 0.08
    play sound2 camera
    show black
    pause 0.08
    hide black
    pause .5
    mct "And how should the last one be?" with dis06 
    mct "She really looks good from any angle."
    mc "Hmm..."
    menu pennyphotosmenu:
        with dis
        "Leaning over the hood":
            $ pennypicturecar = 1
            play sound w1
            show fg 68 with pl
            pause
            play sound camera
            show black
            pause 0.08
            hide black
            pause
            play sound zoomout
            show fg 69 with dissolve
        "Lying on the hood":
            $ pennypicturecar = 2
            play sound w1
            show fg 71 with pl
            pause
            play sound camera
            show black
            pause 0.08
            hide black
            pause
            play sound zoomout
            show fg 72 with dissolve
        "Spread out in front of the hood":
            $ pennypicturecar = 3
            play sound w1
            show fg 73_b with pl
            pause
            play sound camera
            show black
            pause 0.08
            hide black
            pause
            play sound zoomout
            show fg 73 with dissolve
    menu:
        with dis
        "Try another angle":
            jump pennyphotosmenu
        "Go with this one":
            mct "Yeah, this is the one." with dis06
    mct "My fucking god, her body is absolutely perfect." 
    play sound camera
    show black
    pause 0.08
    hide black
    pause 0.08
    play sound camera
    show black
    pause 0.08
    hide black
    pause
    scene fg 73b
    mct "She sure knows how to pose..." with dis12  
    mc "Keep that expression!"      
    play sound whoosh6
    scene fg73c
    asp "*Grabbing your camera* Okay, time's up!" with vpunch 
    scene fg 73d
    mc "What? No chance it's been 30 minutes already."
    scene fg 73c
    asp "You have your 4 pics, and I have to take the SD card to the office outside the studio, transfer your pics to my laptop, and send them over to the contractor."
    asp "And I have to do all that before Valentino struts in."
    show fg 73d
    mc "Seriously? Can't we just upload them straight to the U-cloud?"
    mc "What century is that camera from?"
    show fg 73c
    asp "Old cameras capture magic."
    asp "More megapixels don't mean a better shot."
    show fg 73d
    mc "If you say so..."
    show fg 73c
    asp "I'll be back in 10."
    asp "Tell your model to start getting changed, I'd rather you weren't here by the time Valentino arrives."
    asp "Less explaining for me that way."
    show fg 73d
    menu:
        with dis
        "[gr]Be nice":
            $ aspennice = True
            mc "Copy that."with dissolve 
            mc "Hey, I know we've started off on the wrong foot, but... thanks for the opportunity. I really appreciate it." 
            mct "Might be better to try to get on her good side..."
            asp "Hmph."
            show fg 73c
            asp "You're... welcome."
            asp "I really think she has... potential."
            asp "But anyway, you've got 10 minutes to bounce! Capeesh?"
            show fg 73d
            mc "Got it!"
        "Be rude":
            mc "Jesus, what a useless piece of shit."with dissolve
            mc "I'm baffled how you even got this gig in the first place."
            show fg 73c
            asp "I've seen better insults in a middle-school Xbox chat. God, you're even lamer than I thought."
            asp "You've got 10 minutes to bounce, got it?"
            show fg 73d
            mc "Yeah, yeah. I'd really like to not see you again either."
            asp "Hmph."
    play sound ["<silence 0.5>", doorclose2] volume 0.3
    queue music3b pennysex
    show fg 74 with dis17
    mc "Welp, that sure was an express shoot." with dis08
    mc "But goddamn, it was hot..."
    show fg 75
    p "Yeah... hopefully we managed to take some good pics."
    show fg 74
    mc "Trust me, we did."
    show fg 75
    p "Good, good..."
    p "This was fun. I love modeling. I missed it."
    show fg 76
    p "It always makes me feel... frisky."
    show fg 74
    mct "Oh god, that look..."
    mc "And I love snapping pics of you."
    mc "Is it wrong if I say that I literally couldn't stop imagining you naked while you were doing all those suggestive poses?"
    show fg 76
    p "*Giggles* Don't tempt me..."
    show fg 74
    mc "I only wish we would have had a chance to capture some extra... special shots... for our personal collection."
    mc "You know... like we did last time."
    show fg 75
    p "*Giggles* Ah yeah, that was also fun..."
    p "Too bad she swiped the camera."
    show fg 74
    mc "Well... if that's the only hiccup, I could use my phone."
    show fg 76
    p "*Giggles* Even then, someone could walk in at any moment."
    show fg 74
    mc "I could lock the door."
    mc "Or..."
    show fg 76
    p "*Giggles* You don't take a no for an answer, huh?"
    show fg 74
    mc "I'm doing it for you!"
    mc "Last time you looked like you were left wanting it..."
    show fg 75
    p "Some spicy pics with this car would certainly be... memorable, I'll give you that."
    show fg 74
    mc "Right?"
    show fg 76
    p "Right..."
    show fg 74
    mct "Oh man, her sultry voice is enough to drive a man crazy."
    mc "So... is that a yes?"
    mc "Do you want a more intimate shoot... just for yourself?"
    mct "Please say yes."
    p "Hmm..."
    show fg 75
    p "Okay, if you can lock that door... we can do... another quick shoot."
    show fg 76
    p "Just a bit more... {i}personal{/i} this time."
    scene fg76b
    play sound whoosh6 
    play sound2 run
    play sound3 run
    pause 1.8
    stop sound3
    play sound2 slam
    scene fg 78b 
    bla "You slam a chair against the door and slide it under the knob." with hpunch 
    play sound doorlocked2b
    mc "*Trying to force the door open* (There’s no chance anyone can open this from the outside now.)" with hpunchlong
    scene fg76bb
    play sound whoosh6 
    mc "Done!"
    mc "Huh?"
    mc "Penny?"
    mct "Where the hell did she go?"
    p "So... I've been thinking."
    show fg 80 
    mc "*Turning around* Hmm?" with Dissolve(1.3)
    mc "Oh Lord..." 
    show fg 81
    p "Probably even a bit too much lately, but... *giggles* that's beside the point now."
    p "You know, all this... fooling around between us?"
    show fg 80
    mc "Aha..."
    show fg 81
    p "I've come to the conclusion that... there's nothing wrong with it."
    show fg 80
    mc "Nothing wrong, no..."
    show fg 81
    p "I mean, we're just having fun."
    p "And isn't that what matters most?"
    show fg 80
    mc "Those are my thoughts exactly..."
    show fg 81
    p "Good! I just wanted to make sure we were on the same page."
    p "As long as we don't cross the line... it's all good."
    p "It'd just bring waaay too many headaches... I don’t think either of us want more drama in our lives."
    show fg 80
    mc "And... where exactly are we drawing that line...?"
    show fg 81
    p "*Giggles* You know exactly where."
    p "So, before we continue with this little photo session... do you think we can control ourselves?"
    p "Or should we hit the brakes right here?"
    show fg 80
    mc "I'm known for my self-control. But I have a better question: do we want to?"
    mc "Like you said, there's nothing wrong with a bit of... fooling around."
    mc "Just a spicy photo session."
    show fg 81
    p "Exactly."
    p "Again, good to see we're on the same page."
    show fg 80
    mc "The very same."
    p "Mm-hm..."
    play sound clothes3
    play sound2 clothes3
    show fg 82 with dis2
    bla "Penelope gracefully glides along the studio's light stand, leaning against it, and unveiling her naked form before you." with dis
    mc "Oh my fucking god..."
    show fg 83
    p "I'm glad I have a friend who I trust and with whom I can do these kinds of things, [mc]."
    p "I would have never dared to do a naked session if it wasn't for you."
    p "Even if the photos were supposed to be private."
    show fg 82
    mc "It should be a crime to cover your body with clothes..."
    show fg 83
    p "*Giggles* Alright, so... come on, take a pic. Bring out the artist in you."
    p "Do you think this pose enhances my... features?"
    play sound zoomout
    show fg 82
    show camera2
    mc "I think it does, yes..." with dis08
    play sound camera
    show black
    pause 0.08
    hide black
    pause
    show fg 83
    p "I also want a picture with you."with dissolve
    show fg 82
    mc "Just you and me?"
    p "Mm-hm."
    mc "With me... naked?"
    p "Mm-hmmm..."
    mc "*Chuckles* Very well."
    mc "What kind of manager would I be if I refused such a simple request from my client?"
    play sound clothes
    play sound2 belt
    scene fg 84 with dis17
    bla "You race to shed your clothes, Penny’s gaze on you all the while. You notice her gaze growing more and more lustful with every passing second."with dis12
    show fg 86
    mc "Do you like what you see? Do I look... artistic?"with dis12
    show fg 85
    p "*Giggles* Very much."
    p "I'll admit it's quite alluring to see you in this lighting."
    p "Regina's room was... too dark to appreciate it all."
    show fg 86
    mc "I could say the very same thing..."
    play sound clothes3
    show fg 88
    p "*Approaching you* Alright, big boy..." with dis15
    p "Let's take a pic together."
    p "Do you remember last time?"
    p "You sitting, and me perched on top of you."
    show fg 87
    mc "I do..."
    show fg 88
    p "Only this time... *giggles* I won't jump up all startled when I notice your junk, don't worry."
    show fg 87
    mc "That sounds good..."
    show fg 88
    p "You can leave your phone on that tripod with timed shots enabled, or... even recording."
    p "Then we can select the perfect shot and keep it for ourselves... sound good?"
    show fg 87
    mc "That's a fantastic idea..."
    show fg 95b with dis17
    bla "You grab your phone and set it up on a tripod, aiming the camera at the Lamborghini, and start recording." with dis12
    p "Good."
    mc "Good..."
    play sound ["<silence 0.1>", carsuspension2]
    play sound2 clothes3
    show fg 90
    p "*Sitting on the car* Are you okay? Your mind seems to be elsewhere, [mc]." with dis12
    show fg 89
    mc "I can assure you, my mind is only in one place in the world right now..."
    show fg 90
    p "You're not secretly plotting to sell these pics online, right?"
    show fg 89
    mc "I'd never let another man see you in your most glorious form."
    show fg 90
    p "Oh my, so selfish..."
    play sound ["<silence 0.1>", carsuspension2]
    show fg 91
    bla "You sit on the car's hood next to Penelope." with dis12
    play sound3 rubbody
    play sound2 carsuspension2
    show fg 92
    p "*Climbing on top of you* Does it bother you if I sit like this? Or... is it too much...?" with dis12
    mct "Oh sweet Lord Jesus, she's not wasting any second..."
    p "...[mc]?"
    play sound4 rubbody
    show fg 93
    mc "Does it bother you if I touch you like this...?" with dis12
    scene pennygrop1 with dis2
    p "*Soft moan* Aahh..." with dis
    p "N-No, it doesn't..."
    mct "Boy, I could never get enough of her massive, perfect tits..."
    mct "They're almost too much to hold in just my hands."
    p "*Soft moan* Mmmmh..."
    mct "And those perky nipples tell me she's as excited as I am..."
    p "*Soft moan* Aahh..."
    mc "Penny..."
    p "Yeah...?"
    mc "I might have overestimated my self-control..."
    mc "I-I'm having a hard time right now trying to control myself..."
    play sound2 bodycollide2
    play sound rubbody fadein 1
    play sound2 rubbody fadein 1
    scene fg 94b
    bla "Penelope seizes your hands and redirects them downward." with dis15
    show fg 95
    p "I'll admit that... I'm a bit horny right now too." with dis12
    p "But... that's normal."
    p "We're just humans after all. We have a history together, and this is quite an... explicit session."
    p "But as long as we... don't cross..."
    play sound3 clothes3
    scene pennysex0 with dis2
    p "The line..." with dis
    mc "O-O-Oh my god..."
    p "As long as we keep it..."
    p "*Whispering* Professional..."
    bla "Penny starts sensually gliding her hands up and down your shaft, pressing it against her pussy and moistening it with her touch. You can practically feel her needy warmth."
    mc "Oh, fuck..."
    p "*Whispering* God..."
    p "*Whispering* I-It feels... so... massive..."
    mc "Oh, Penny..."
    p "*Whispering* So warm..."
    bla "Penelope continues to touch your fully erect member as a prolonged silence surrounds you."
    pause 
    p "*Deep exhale* Fuuu..." with dis06
    mc "I-Is everything okay?"
    p "Can I..." 
    p "C-Can I be frank with you, [mc]?"
    mc "Of course..."
    p "*Deep exhale* Okay..."
    p "All this teasing between us... it started off as a game because I just loved watching how jittery you'd get every single time."
    p "But... then... it went too far. That day at Regina's room. It went way too far."
    p "I tried to stop... but I couldn't."
    p "I... I thought that if I acted casually about it, if I didn't make a big deal out of it... it would stay like that. As a game."
    p "That I would stop thinking about you 24/7."
    mc "And...?"
    p "And..."
    p "*Biting her lip* F-FUCK, this isn't working, [mc]." 
    p "I'm..."
    p "I-I think I'm a little more than just a bit horny right now..."
    p "It's... almost..."
    p "{sc=1}Painful...{/sc}"
    mc "You're not the only one feeling that way..."
    play sound rubbody
    play sound2 clothes3
    scene fg 97b
    p "*Biting her lip* W-We probably should stop here for today..." with dis15
    p "Before that other wild idea of mine pops back into my head, and we end up regretting this forever."
    mc "What other idea...?"
    scene fg 97c
    p "Ah... nothing. It was just... a c-crazy thought I had."
    show fg 97
    mc "I'd really like to hear it..."
    show fg 97c
    p "It's not worth it. It was {i}really{/i} crazy."
    show fg 97
    mc "I {i}really{/i} like crazy ideas, Penny..."
    p ". . ."
    mc "Come on, please..."
    show fg 96
    p "Well... I thought..."
    show fg 97c
    p "Um... imagine for a second... hypothetically... if there were absolutely no consequences for your actions. Stay with me, alright?"
    show fg 97
    mc "Alright..."
    show fg 96
    p "I thought that..."
    p "Maybe..."
    p "The solution to get rid of all this sexual tension between us..."
    p "Would be to..."
    play sound clothes3
    show fg 98
    p "*Removing her gloves* To..." with dis15
    p "Actually... {w=0.5}have... {w=0.5}sex...{w=0.5} once." 
    p "Just... once."
    show fg 99
    mc ". . ."
    mc "W-What did you just say...?"
    show fg 98
    p "I think it's my imagination that’s been driving me insane lately."
    p "So maybe if I just..."
    p "F-Feel it once."
    p "Instead of {i}thinking{/i} about how you’d f-fuck... or about how your cock would feel in my t-tight pussy..."
    p "If I could just actually feel it once..."
    p "Without feelings attached..."
    show fg 100
    p "*Caressing your dick* Maybe then... the sexual tension would ease up..." with dis15
    p "And we could go back to being our regular selves."
    p "Hah... crazy idea, right...?"
    mct "Oh my fucking god, YES PLEASE..."
    p "Am I crazy?"
    mc "No, you're not..."
    p ". . ."
    show fg 99
    p ". . ." with dis14
    show fg 98
    p "O-Okay..."
    p "Let's keep it casual."
    show fg 100
    p "I-I'm gonna try to... put it inside. Once." with dis12
    mct "Oh sweet heavens."
    p "Let's cross this line... just once."
    p "And after this... the game will be over. It will be... our secret."
    p "Forever."
    show fg 98
    p "Deal...?"with dis12
    show fg 99
    mc "Deal..."
    show fg 100
    p "Alright..." with dis12
    p "Here goes nothing..."
    play sound ["<silence 0.1>", carsuspension2]
    play sound2 clothes3
    show fg 101b with dis15
    bla "Penelope sits up and lets out a moan as the head of your cock rubs against her pussy lips." with dis12
    p "*Moans* Aaahh..."
    mct "She's wet as fuck even without any kind of foreplay..."
    p "S-Shit... this is crazy, [mc]."
    p "We're crazy."
    mc "This is the best idea you've ever had in your life."
    p "*Giggles* Of course you'd say that..."
    p "Okay..."
    p "Okay."
    p "Are you ready...?"
    mc "I'm not sure if I'm ready, but I certainly want it..."
    p "*Deep exhale* . . ."
    play sound5 penetration2 fadein 1
    play sound6 clothes3
    show fg 102 with dis2
    bla "After a brief moment of hesitation, she slowly lets the tip of your cock slide inside of her dripping pussy." with dis12
    p "*Moans* O-O-Oooohhh..."
    mc "Oh god, FINALLY..."
    p "F-F-fuck, IT'S IN."
    mc "It is..."
    play sound6 penetration2 fadein 1
    show fg 103
    p "MMMmmmmmMmmhhh..." with dis17
    show fg 104
    p "O-Ohhh wooOOOow, that feels..." with dis12
    p "Holy fuck, [mc], that feels..."
    p "G-Good..."
    $ renpy.music.set_volume(0.2, delay=9.0, channel='music3b')
    play soundloop pennysex1 fadein 5
    scene pennysex1 with dis2
    p "{sc=2}M-MY GODDDDD....{/sc}" with dis12
    mc "Ooh PENNY...."
    mct "Oh my god, it's happening at last."
    mct "No more teasing."
    mct "No more games."
    mct "I'm inside Penelope."
    mct "I'm having sex with her. I’m fucking Penelope Carter."
    mct "I'm living out the fantasy of what her 180,000 followers can only dream of."
    mct "And sweet Jesus, it feels good..."
    p "*Moaning* Aaaghhh, [mc]..."
    mc "F-Fuuuck yes, this is better than I imagined..."
    p "*Giggles* Oh y-yeah? You thought about this...? Thought about fucking little old me?"
    mc "All the fucking time..."
    p "*Moaning* AAaaahhh..."
    p "Just... a little bit faster..."
    mc "Oh boy..."
    mc "Please, d-don't let me stop you..."
    p "Just... a little bit... okay...?"
    $ renpy.music.set_volume(0.15, delay=6.0, channel='music3b')
    stop soundloop fadeout 3
    scene pennysex2b with dis2
    p "AAAAAaaahhhhh... yeaaahh..." with dis12
    mc "Jesus Christ, that feels good, Penny..."
    p "Mmmmmhh... *giggles* y-yeah..."
    mc "W-Where the fuck did you learn to move like that?"
    p "L-Like what...?"
    p "I just imagine I'm... d-dancing..."
    p "J-Just that it feels... so much fucking better..."
    p "*Panting* AAaahhh...."
    mc "Y-Yeaah, keep going..."
    p "*Groaning* F-Fuck, you're so fucking big, [mc]..."
    bla "You can feel Penelope's tight cavity slowly adjust to your size. Each of her movements feels extra sensitive on your dick."
    mc "Take it all..."
    p "AAaahh..."
    mc "Take it balls deep..."
    p "I c-can't... it’s t-too much..."
    mc "Try it for me, baby girl..."
    p "I..."
    p "A-Are you sure?"
    mc "Don’t you wanna ditch this tension once and for all? And feel good and r-relaxed?"
    mc "We've crossed the line already... might as well roll with it, right?"
    p "*Giggles* That's a good point..."
    mc "You'll see how good it feels..."
    p "*Moaning* Okay..."
    p "*Moaning* I'm g-gonna drop myself on you, yes...?"
    mc "Fuck yes..."
    p "O-Okay, here we go..."
    $ renpy.music.set_volume(0.1, delay=6.0, channel='music3b')
    scene pennysex3b with dis2
    p "*Moaning* OH GOD.{sc=2} OH MY FUCKING GOD.{/sc}" with dis12
    bla "Penelope lets herself drop, the weight of her body slamming you against the car with each powerful thrust."
    p "*Screaming* AAAaaahhhh, fuck THAT'S {b}HUGE{/b}..."
    mc "O-Oh Penny..."
    p "T-T-This is o-otherworldly..."
    mc "*Panting* Fuck, it really is..."
    mc "Ohhh f-fuck..."
    mc "FUUUUUCK..."with hpunch 
    p "*Panting* P-Please, please don't cummm..."
    p "Please let me cum first..."
    mc "You're asking for a lot there, Penny..."
    p "I-I need to cum so I can get rid of the... tension..."
    p "I need it..."
    p "I need to... I n-need to do this..."
    p "Please..."
    p "*Moans* AAAaaaAahh..."
    p "M-My god, this feels better with each passing second... aaaahhhh... how the fuck is this possible..."
    pause
    scene pennysex3_2b with dis15
    p "*Panting* AAAaahhh... aAAAAAahh... aaaaahhhhhh..." with dis12
    mc "Holy shit..."
    p "{sc=2}*Squeals* AAAAAAAAGHHH!{/sc}"
    mc "Oh y-yeah, good girl..."
    p "O-Oh my god, [mc], you're stretching me out so much..."
    mc "Y-You're taking it like a pro, Penny..."
    p "Ohhhhh god...."
    mc "That's it, babe, ride that dick..."
    mc "Keep riding it like that..."
    p "Oh, [mc]..."
    mc "Penny..."
    pause 
    bla "Penny’s jiggling, voluptuous body fills your every sense, as each individual bounce and thrust causes your body to radiate with a divine pleasure."with dis08
    p "*Panting* AAAah... aaaaaahhh... aaaaahhhh..."
    p "*Panting* F-Fuck, I'm getting tired, [mc]..."
    p "*Panting* B-But I don't want it to stop..."
    p "*Panting* Not when I'm this close..."
    p "*Panting* Not when it feels... t-this good..."
    mct "Maybe now that she's gotten used to it, I can let her “rest” and simply relish the pleasure..."
    mc "Now it’s my turn to ask..."
    mc "Are you ready?"
    p "*Panting* Ready... f-for what...?"
    play soundlow slam
    scene pennysex4b with vpunch
    p "{sc=2}OH MY F-FUCKING GOD...........!!!{/sc}" with dis12
    mc "OH FUCK YESSS...."with hpunch 
    p "AAAAAAHHHhh!!!"with hpunch 
    mc "This is what you wanted, didn't you...?"
    mc "You wanted me to fuck you this hard from the beginning... always teasing, always flirting..."
    p "O-Oh Lord, t-this is unbelievable..."
    mc "You wanted this, didn’t you, you naughty girl?"
    p "F-Fuck YESSSS, I did..."
    p "Fuck me hard, [mc]..."
    mc "Oh I will..."
    pause
    bla "You keep hammering Penelope's pussy, your ears drowning in her small, constant whimpers of pleasure."with dis 
    p "*Panting* I-I'm gonna cum so hard, [mc]..."
    p "*Panting* I'm almost there..."
    p "*Panting* P-Please don't s-slow down..."
    mc "I'm gonna give you the orgasm of your life..."
    mc "You’ll never forget this..."
    scene pennysex4_2b with dis15
    p "{sc=2}AAAAAAAHAHHH YEAAAAHHHH...!!!{/sc}" with dis12
    p "{sc=2}*Biting her tongue* MMMMmmMMMmhhhh!!!!{/sc}"
    mc "*Panting* O-Oh god... I knew you'd love it hard..."
    p "{sc=2}*Noises of pleasure* MmmMmmggggGGggghhh!{/sc}"
    mct "I don't think anyone could take it as roughly as she does..."
    mct "She’s a total sex freak..."
    mct "I can literally feel the tip of my cock poking the innermost parts of her."
    p "{sc=2}MmmMmmgggmmmmmh....{/sc}"
    mct "I feel so fucking powerful destroying her slender body like this..."
    p "{sc=2}AAAAaahhhh...{/sc}"
    mct "And she seems to like all of it..."
    mct "This is gonna leave a mark."
    p "{sc=2}MmmMMmmmmmh!!{/sc}"
    mc "*Panting* A-Are you gonna cum?"
    p "*Biting her tongue* Y-Y-Y-Yahh..."
    p "I'm gonna..."
    p "I'M THERE!"
    p "{sc=2}DON'T STOP!!!{/sc}"
    p "I'm..."
    p "I'M–"
    play sound2 carsuspension 
    play sound7 slap1
    play sound3 cum4
    scene fg 105
    p "{sc=2}*Orgasming* AAAAAAAAaaaAAAAAGHHHH.....!!!{/sc}" with hpunch
    bla "Penelope orgasms, soaking your cock in vaginal fluids and contracting all of her muscles at once."
    play sound4 carsuspension
    play sound5 slam volume 0.4
    play sound6 penetration2
    stop music3b fadeout 8
    play soundloop vent fadein 9 volume 0.8
    scene fg106
    bla "She faints on top of you, utterly dazed, her legs still trembling uncontrollably." with vpunch
    p "*Breathing heavily* AAaAAAaaahghh . . . . . ."
    mc "*Catching your breath* Oh, Penny..."
    mc "Fuck, that was intense."
    p "*Breathing heavily* . . ."
    mc "Got rid of all that sexual tension, eh?"
    p "*Breathing heavily* Mm-hmmm...."
    mc "Glad I could be of service..."
    mct "Man, I can't believe I just fucked Penny."
    mct "I was literally just a few seconds away from cumming too."
    mct "But I can't really ask much more of her, to be honest."
    mct "That was insane."
    p "{bt=3}{i}*Unintelligible murmurs*{/bt}"
    mc "What...?"
    p "{bt=3}{i}*Unintelligible murmurs*{/bt}"
    mc "You're gonna have to say it louder."
    p "{bt=3}{size=10}*Whispering* Break me.......{/bt}"
    mc "Eh?"
    p "{bt=3}{size=25}*Whispering* Break me please...{/bt}"
    $ renpy.music.set_volume(0.35, channel='music3')
    play music3 pennysex fadein 3
    stop soundloop fadeout 12
    show fg 107
    mc "What...?" with dis12
    scene fg 109
    mc "What did you say...?"with dis12
    show fg109
    p "I want you..."
    p "I want you to break me."
    p "I want you to fuck me again until you ruin me..."
    p "And again... and again."
    p "Grab me and use me as rough as you can... don’t give me a second or a moment to breathe..."
    p "{bt=3}*Whispering* I want you to destroy me...{/bt}"
    scene fg108
    mc "A-Are you fucking serious?"
    scene fg109
    p "C’mon... you were talking such a big game earlier, [mc]..."
    p "Split me in half..."
    scene fg108
    mc "Oh, baby..."
    menu pennysexcar:
        with dis12
        "Fuck her in missionary" if pennylambomis:
            $ renpy.music.set_volume(0.2, delay=7.0, channel='music3')
            play sound4 carsuspension
            play sound5 slam volume 0.35
            play sound6 whoosh6 
            if pennylambo1:
                scene carmisagain with hpunch 
                p "*Panting* AAAAaaaaaaahhh..." with dis
                p "*Panting* A-A-Again...?"
                mc "*Panting* I just can't stop, Penny..."
                p "*Panting* O-O-Oh my goddd..."
                pause 
                scene pennysex6b with dis15
                p "{sc=2}AAAAAAAAHHH....{/sc}" with dis  
                p "{sc=2}SWEET LORD, [mc!u]...{/sc}"  
                mc "*Panting* FUCK YES...." 
                pause
                $ pennylambomis = False
                $ pennylambodog = True
                jump pennysexcar
            scene fg110
            mc "*Pulling her to the front of the car* Bring that tiny waist of yours here..." with hpunch
            if not pennylambodog:
                p "*Still catching her breath from the last position* J-Jeez..."
                p "A-Aren't you even gonna let me–"
            else:
                p "Yeah..."
                p "Fill me up with your huge cock..."
                p "My body’s all yours... this pussy, this mouth, everything..."
                p "Yours..."
                mc "Now you'll see what's good..."
            scene pennysex5b with dis15
            if not pennylambodog:
                bla "You suddenly penetrate her, cutting her off."with dis12
                p "AAaaaaaaahhhh... MY G-GOD, I GUESS NOT..."
            else:
                p "AAaaaaaaahhhh... MY G-GOD, YEAHHH..." with dis12
            mc "OH FUCK..."
            p "Mmmmmmmhhh YESSSSS..."
            mc "O-Oh my god, Penny..."
            p "*Moaning* Yeah..."
            p "F-Fuck me..."
            p "Fuck me with that monster fucking cock of yours... give me what I need..."
            p "Shove every inch of it inside of me..."
            pause 
            bla "You continue to hammer her relentlessly, feeling how your dick breaks the resistance that her tight insides offer with each stroke." with dis
            p "*Moans* AAAaaaAAhh..."
            p "Oh my god, you're tearing me apart..."
            p "*Giggles* A-And I fucking love it..."
            p "Mmmmmhhh..."
            scene pennysex5_2b 
            pause 0.01
            mc "Ahhhh..."
            mc "Dear Lord, about time I get a good look at these tits of yours..."
            mc "You have no right to be this hot..."
            p "*Moaning* AAAaaahhh..."
            mc "I fucking love how your boobs bounce..."
            p "T-They're all yours... I told you, e-everything is yours..."
            p "*Moans* AAAaaaaAAaahh..."
            p "D-Do with me as you please..." 
            p "*Moaning* Just don't stop fucking me ever..."
            mc "Y-You're a fucking nympho..."
            p "*Moaning* Faster..."
            p "*Panting* Fuck me harder..."
            mc "Very well..."
            if pennyrough:
                scene pennysex6_2b with dis15
                p "AAAAAAAAHHH.... y-yeah... HIT ME!{w=3.6}{nw}" with dis12               
            else:
                scene pennysex6b with dis15
                p "AAAAAAAAHHH!!!" with dis12
            p "MmmmMMMmMmmmhhh..." with hpunch
            p "F-Fuck yeah..."
            p "Punish me..."
            p "Punish me for all the teasing..."
            p "I've been a bad girl... mmmMmmhh... all those naughty dresses... all those comments..."
            p "F-Fucking punish me..." 
            mc "AAAAAAARGHHH, fuck, PENNY..."
            mc "*Panting* AAAahhhh..."
            mc "O-Oh god, my dick's gonna be sore after this..."
            p "*Squeals* AAAAAaghhh..."
            $ pennylambo1 = True
            $ pennylambomis = False
            $ pennylambodog = True
            jump pennysexcar
        "Fuck her from behind" if pennylambodog:
            $ renpy.music.set_volume(0.2, delay=7.0, channel='music3')
            play sound4 carsuspension
            play sound5 slam volume 0.35
            play sound6 whoosh6 
            if pennylambo2:
                scene cardogagain with hpunch 
                p "*Panting* AAAAaaaaaaahhh..." with dis
                p "*Panting* Fuck, [mc]... don't you ever run out of stamina?"
                mc "*Panting* Not with you..."
                p "*Panting* O-O-Oh my goddd..."
                p "*Panting* I need... t-to rest..."
                play sound fallfull
                play sound2 carsuspension
                play sound3 carsuspension
                scene pennycartransfall2 with vpunch 
                p "{sc=2}AAAAAAAAHHH....{/sc}" with dis 
                p "{sc=2}[mc!u]...{/sc}"     
                mc "*Panting* GGGgghhh...." 
                pause
                $ pennylambomis = True
                $ pennylambodog = False
                jump pennysexcar
            scene fg111
            mc "*Pulling her to the side of the car* Come here..." with hpunch
            if not pennylambomis:
                p "*Still catching her breath from the last position* J-Jeez..."
                p "A-Aren't you even gonna let me–"
            else:
                mc "Your tits are the fucking best I've ever seen in my life, Penny, but goddamn, this butt of yours deserves some attention too..."
                p "*Giggles* Please, put it back inside..."
                mc "Your wish is my command..."
            scene pennysex7b with dis15
            if not pennylambomis:
                bla "You suddenly penetrate her, cutting her off."with dis12
                p "AAaaaaaaahhhh... MY G-GOD, I GUESS NOT..."
            else:
                p "MMmmmmMmmmmm... Y-YEAAAHHHHHH..." with dis12
            mc "*Panting* Oh dear Lord, y-your pussy is so fucking tight, Penny..."
            p "AAAaaaahhh..."
            p "*Panting* Hell y-yeah, that's the stuff..."
            p "*Panting* Slam it in me..."
            mc "Aaaahhh...."
            p "*Panting* Yes..."
            p "*Panting* D-Deeper..."
            p "*Panting* H-Harderrrr..."with hpunch 
            mc "*Panting* God..."
            p "*Panting* I d-don't give a shit anymore..."
            p "*Panting* I don't give a shit about consequences..."
            p "*Panting* I just want you to fuck me every day..."
            p "*Panting* J-Just take your cock and fucking give it to me..."
            p "*Panting* I want Mom and Dalia to hear me scream..."
            mc "Oh f-fuck me, don't say that or you're gonna make me cum instantly..."
            p "*Giggles* AAAAAaahaaahaaahhh..."
            scene pennysex7_2b with dis15
            p "AAAAaahhh...." with dis12
            p "*Squeals* Oh my god, you're so deep..."
            mc "D-Do you even realize we're fucking on a $400,000 car?"
            p "*Panting* F-Fuck yeah we are...."
            p "*Giggles* And that makes it so much hotter..."
            p "AaAAaaahhhhhhh..." with hpunch 
            p "Crush me against this car, [mc]..."
            p "*Giggles* L-Let's see if it breaks before I do..."
            mc "Oh yeah, Penny..."
            scene pennysex7_3b with dis15
            p "*Panting* AAAaahhh..." with dis12
            p "*Panting* I never imagined I could ever feel so filled..."
            p "*Panting* D-Don't slow down, please..."
            mct "I knew Penny had hinted she was into rough sex, but... holy fuck." 
            mct "We're rutting like fucking animals in the middle of mating season."
            mct "And she's enjoying it as much as I am."
            p "*Moans* MMMMmmmMMmmhh..."
            mct "No, she’s definitely enjoying it more..."
            scene pennysex7_2b with dis15
            p "*Moans* AAAaaaahhh..."with dis12
            p "Oh d-d-dear LORD... I can't even feel my legs anymore..."
            p "{sc=2}AAAAAAAAGHHHHH... YEAHHH...{/sc}"with hpunch 
            p "Fuck, I c-can't..." with hpunch
            play sound fallfull
            play sound2 carsuspension
            play sound3 carsuspension
            if pennyrough:
                scene pennycartransfall1 with vpunch 
            else:
                scene pennycartransfall2 with vpunch 
            bla "Penelope's legs give out, and you both tumble onto the floor."with dis
            p "{sc=2}AAAAAAAAHHH.... my GODDDDD.....!!!!{/sc}" with hpunch
            mc "F-Fuck yes..."
            mc "Y-You told me yourself that you wanted me to fuck you without giving you time to even breathe, didn't you...?"  
            p "*Squeals* AAAAAAaaaaaHHHH..."   
            if pennyrough:
                p "Y-Y-Yeaahh.... I deserve it..." 
                p "Be rough with me..."   
                p "Use me..."  
            else:
                p "Y-Y-Yeaahh...." 
                p "Keep fucking me like that..."
                p "I-It feels so good..."
            p "AAAAAAAAahhh..."with hpunch 
            p "*Panting* Fuck me..." 
            $ pennylambo2 = True
            $ pennylambomis = True
            $ pennylambodog = False
            jump pennysexcar
        "Finish" if pennylambo1 or pennylambo2:    
            mc "I-I'm at my limit, Penny..." with dis
            p "{sc=2}*Panting* AAaaa.... aaaahhh... aaaaaahhh...{/sc}"
            mc "*Panting* I'm gonna cum..."with hpunch 
            mc "*Panting* I'M GONNA..."with hpunch
            jump valentinoend
label valentinoend:
    play sound doorclose2
    play sound2 slam
    play sound3 doorslam
    bla "You hear a sudden noise.{w=0.8}{nw}" with hpunch 
    play sound5 penetration2
    play sound5 carsuspension
    scene fg 112 with dis12
    mc "*Suddenly stopping* W-What was that?" with dis
    p "{bt=3}MMMmmmmmmhmmm...{/bt}"
    mc "H-Hold on... THE DOOR!"
    mc "Someone just kicked the door open!"with hpunch 
    mc "Shit, I totally forgot about where we are! We have to get out of here!"
    p "{bt=3}*Giggles* Oh nooo...{/bt}"
    mc "*Whispering* S-Shit, Penny, keep it down! We need to leave!"
    p "{bt=3}Keep fucking me...{/bt}"
    mc "*Whispering* Don't you realize that if they catch us they're gonna hit us with a massive fee for property damage?!"with hpunch
    p "{bt=3}*Giggles* I'm the damaged property here...{/bt}"
    play sound4 carsuspension
    show fg 113
    p "{bt=3}*Blowing you* Please, make me cum again...{/bt}" with dis14
    scene fg113
    p "{bt=3}*Blowing you* Pretty pretty please...?{/bt}"
    mc "G-G-Ggggghhhh... P-Pennyyy s-stay quieeeeet..."
    play sound clotheswhoosh
    play sound3 clotheswhoosh
    play sound2 curtain2
    scene fg115
    val "*Pushing aside the curtains* This is the last time I work with this shitty studio, you hear me?!" with hpunch 
    val "I couldn't even get inside! UNBELIEVABLE!"
    show fg 115b
    asp "I-I don't know what happened, Mr. Valentino, I'm so sorry!"
    asp "Someone from the cleaning staff must have forgotten to–"
    scene fg 115
    val "Don't sell me that bullshit, bitch!"
    val "Now go find my girl and tell her to start getting changed!"
    show fg 115b
    asp "Y-Yes, right away, Mr. Valentino!"
    show fg 115
    val "Then why are you still here?! Move, you fucking incompetent dog!" with hpunch
    asp "Y-Yes!"
    play sound run
    show fg 116
    val "Hmm..." with dis12
    show fg 16
    val "*Sighs* (This is what happens when you give women any kind of important job.)"
    val "(Anyway... at least the car's good to go.)"
    show fg 117 with dis14
    val "(I'm gonna get that emo bitch fired as soon as Ulysses gives us the contract.)" with dis
    play sound type1
    val "*Typing* (She'll regret having disrespected me like that...)"
    show fg 118 with dis15
    pause
    scene pennysex9b 
    show fg 119
    with dis12
    pause
    $ renpy.music.set_volume(0.1, delay=7.0, channel='music3')
    hide fg 119 with dis17
    mc "*Whispering* J-Jesus..." with dis12
    p "MMmMmMmmmmhh..."
    mct "Oh Lord..."
    mct "What the fuck is happening to me...?"
    mct "If we get caught, we're gonna get in BIG trouble."
    mct "But I just..."
    mct "Fuck, I just {b}can't{/b} seem to stop..."
    p "*Biting down on her panties with force* MMMMMGH!" with hpunch
    mct "Please, just a little bit more..."
    p "MMMMmmmmmh..."
    mct "The sounds she makes..."
    mct "The way her body feels..."
    mct "Or the way she absolutely LOVES being dominated..."
    mct "Every single thing about Penny just makes me want to turn into an animal and unleash my primal instincts."
    p "MMMMMmmmmmHHHHH..."
    mct "She not only managed to keep up with my rhythm, but she relished every single second of it..."
    mct "If I hadn't put her panties in her mouth, her moans would have revealed us already."
    p "MMMmmmmMmMmmmhh..."
    mct "We need to leave..."
    p "{sc=2}MMMMMMMHHHHHHhhh...{/sc}"
    mc "But I NEED to cum first..."
    p "{sc=2}MMMMMMMMMmmmMMHHHHmHHhhh...{/sc}" 
    mc "I'm finally almost there..."
    mc "My balls are about to explode..."
    p "{sc=2}MMMMMmmmmMMMMmmmMMHHHHmmHHhhh...{/sc}" with hpunch
    mc "I'm..."
    menu:
        with dis
        "Cum inside [gr][mt](Creampie)":
            $ renpy.music.set_volume(0.16, delay=10.0, channel='music3')
            $ pennycreampie = True
            play sound3 penetration2
            scene fg 120 with dis
            pause .2
            play sound5 cumall
            play sound4 slap1
            scene fg 121
            mc "*Trying to repress your groans* AAAAAAaaaaahhh..." with hpunch 
            play sound3 penetration2
            scene fg 120 with dis
            play sound5 cumall
            play sound4 slap1
            scene fg 121
            mc "AAaaaaahhh..." with hpunch
            play sound3 penetration2
            scene fg 120 with dis
            play sound5 cumall
            play sound4 slap1
            scene fg 121
            mc "AAaaaaaaAAAAaaaaaaaahhhhh..." with hpunch
            mc "F-Fuuuuuuck..."
            scene fg 122
            bla "You can feel how Penelope orgasms again at the same time as you finish unloading an insane amount of jizz deep inside her warm vagina." with dis15
            mc "*Whispering* Take it all..."
            play sound penetration2
            play sound2 penetration3
            scene fg 123 with dis17
            mc "*Whispering* Oh, Penny..." with dis
            scene fg 124
            mc "That was..." with dis14
            mc "Glorious..."
        "Cum outside":
            $ renpy.music.set_volume(0.16, delay=10.0, channel='music3')
            play sound rubbody
            play sound2 fall2
            scene fg 125 with dis12
            mc "FUCK, COME HERE..." with dis
            mc "I wanna turn your beautiful body into a fucking mess..."
            play sound5 cumall
            play sound6 bodycollide
            scene fg 126
            mc "*Trying to repress your groans* AAAAAAaaaaahhh..." with hpunch 
            play sound3 penetration2
            scene fg 127 with dis
            play sound5 cumall
            play sound4 bodycollide
            scene fg 128
            mc "AAaaaaahhh..." with hpunch
            play sound3 penetration2
            scene fg 129 with dis
            play sound5 cumall
            play sound4 bodycollide
            scene fg 130
            mc "AAaaaaaaAAAAaaaaaaaahhhhh..." with hpunch
            mc "F-Fuuuuuuck..."
    play sound ["<silence 0.3>", fallfull] volume 0.6
    stop music3 fadeout 12
    play soundloop vent fadein 12
    if pennycreampie:
        scene pennysex10 with dis12
    else:
        scene pennysex10_2 with dis12
    bla "As you take a step back, Penelope's legs finally surrender and she crumples onto the floor, completely spent." with dis
    mc "*Panting* Oh god, Penny..."
    p "{bt=3}*Panting* Gggg-gG-gg-gggghhh...{/bt}"
    mc "W-What?"
    p "{bt=3}*Panting* AAAAaaaagahhhgh...{/bt}"
    mct "I-I’d better give her a minute."
    scene fg 131
    val "Hmm?" with dis12
    show fg 132
    val "(What the hell was that noise?)"with dis12
    val "Hello??"
    val "Is there anyone there?"
    if pennycreampie:
        show pennysex10
    else:
        show pennysex10_2
    mc "*Whispering* F-Fuck! He heard us!"
    mc "*Whispering* Shit, shit shit... Penny, we've gotta get out of here!"
    p "{bt=3}*Panting* AAAAaahhhgghgh....{/bt}"
    p "{bt=3}*Panting* I f-feel like I juust got r-rammed by arr bull...{/bt}"
    p "{bt=3}*Giggles* A bull...{/bt}"
    mc "*Whispering* Penny, focus!" with hpunch 
    mc "*Whispering* Snap out of it!"
    val "ASPEN?? Is that you?"
    mc "*Whispering* PENNY! HE'S COMING THIS WAY!" with hpunch 
    mc "*Whispering* I NEED YOU TO STAND UP!"
    mc "*Whispering* I CAN'T CARRY YOU AWAY LIKE A POTATO SACK!"
    p "{bt=3}*Giggles* Hahahahhgaa...{/bt}"
    p "{bt=3}*Panting* Potato...{/bt}"
    mc "*Whispering* Goddammit!" with hpunch 
    scene fg 133 with dis2
    pause 
    play sound risingshortb fadein 1
    pause .6
    play sound2 debris3
    show fg 134 with dissolve
    pause
    play music quirky7 fadein 8
    show fg 135
    val "Hmph." with dis12
    val "(There's no one here.)"
    val "(Maybe something toppled from the scaffolding.)"
    show fg 134
    val "(This place is filthy as fuck, though.)"
    val "(I swear, this is the last gig with this studio.)"
    play sound lightstage
    show fg 136
    pause
    show fg 137
    val "*Sniffs* (And seriously, what the fuck is this stench?)" with dis12
    val "(Smells like the Lamborghini...)"
    val "(It seems... kinda familiar, but I can't quite put my finger on it.)"
    val "(Perhaps our cleaning crews are using the same cleaning supplies?)"
    scene fg 138 with dis22
    pause
    show fg 139 with dis2
    pause
    play soundlow wood2
    show fg 140 with dis2
    pause 
    play sound2 whoosh6
    play sound run
    scene fg 141
    show mcpotato with hpunch
    pause 
    jump saturday07


label saturday07:
    stop music2 fadeout 8
    stop soundloop fadeout 8
    stop music fadeout 8
    scene black with Dissolve(3.5)
    pause
    show screen afewhourslater with dis2
    pause
    hide screen afewhourslater
    with dis2
    pause
    mc "Hmmm..." with dis12
    mc "Hmm."
    play sound chain
    mc "*Touching the floor* Mmmh?"
    play music twinkle fadein 50 volume 0.8
    mc "What...? Why is it so dark?"
    play sound3 chain
    mc "What is this...?"
    play sound5 debris3 fadein 1
    play sound chain
    bla "You stand up and start analyzing the oppressive darkness enveloping you, only to discover that your neck is ensnared by a chain tethered to a rock structure."
    play sound2 chain2
    play soundlow chain volume 1
    mc "*Pulling the chain* WHAT?!" with hpunch
    mc "W-What the fuck is going on?!"
    play sound7 chain2
    play sound6 chain
    mc "HELLO?!" with hpunch
    mc "Where am I?!"
    play sound coinflip
    aaa "Heads." 
    mc "Huh??"
    mc "Who's there?"
    play sound glitch4 volume 0.7
    show 07idrielglitch2
    pause
    mc "Idriel...?" with dis
    scene fe 1
    id "Welcome back, [mc]."
    show fe 2
    mc "What... where am I?"
    mc "Is this a dream?"
    mc "No... it's way too vivid to be a dream..."
    mc "Am I in... Eternum?"
    show fe 1
    id "You are."
    show fe 2
    mc "But... how...?"
    mc "I don't remember logging in."
    mc "I... I don't remember how I got here at all."
    mc "And... w-why am I imprisoned?!"
    show fe 1
    id "This is not your prison, [mc]."
    id "It is mine."
    show fe 2
    mc "What...?"
    show fe 1
    id "This is the Limbo."
    id "A place in Eternum beyond space. Beyond time."
    show fe 2
    mc "Beyond time?"
    mc "So... time is frozen while we're here?"
    show fe 1
    id "Time isn't frozen, nor is it flowing."
    id "It simply doesn't exist in this place."
    show fe 2
    mc "Uh... okay."
    mc "And what about {i}outside{/i} this place?"
    show fe 1
    id "There is no “outside” while we're here."
    id "Limits are non-existent in the Limbo, making the notion of something beyond it... inconceivable."
    show fe 2
    mc ". . ."
    mc "That doesn't make any sense."
    show fe 1
    id "Trying to comprehend eternity as mortals is as futile as explaining color to a person born blind."
    id "But you've been making progress."
    id "Your mind seems to be more receptive than it used to be."
    show fe 2
    mc "I talked to William Bardot."
    mc "He told me that Eternum isn't a creation of the Founder, but a discovery."
    show fe 1
    id "Do you believe him?"
    show fe 2
    mc "I..."
    mc "I don't trust him, but I do believe him, yes."
    mc "I'm kinda shocked at how quickly I've accepted this new “reality”, but... I genuinely believe it's true. I think deep down... it just seems like it’s the truth."
    mc "The NPCs... they're real. They were once humans."
    mc "And they're trapped in here."
    mc "I must free them."
    show fe 1
    id "You must gather the ten Gems of Doom."
    id "Once you have them all, Eternum will be yours."
    id "Only you can do it. Only you can save them."
    show fe 2
    mc "Then help me!"
    mc "Aren't you the Lady of Eternum?!"
    show fe 1
    id "I am ensnared here, [mc]."
    id "Beyond the confines of the Limbo... I'm but a puppet, a hollow vessel."
    id "Akin to all the others."
    show fe 2
    mc "Then stop with all your stupid riddles, just tell me where the Gems are!"
    mc "Tell me where to go, what to do, how I can defeat the Founder! How can I help free anyone if you won’t help me?"
    show fe 1
    id "That would be in vain."
    id "You won't remember. You never do."
    show fe 2
    mc "What...?"
    mc "Then why engage in this conversation at all?"
    show fe 1
    id "I thought you might have different questions this time."
    show fe 2
    mc "You just said I won't remember, so what's the point?"
    show fe 1
    id "Perhaps you're still not asking the right question."
    show fe 2
    mc "The right question...?"
    play sound glitch4
    play sound2 debris3
    play sound3 chain
    play sound4 ["<silence 0.1>", chain3]
    show 07idrielglitch3
    id "You must keep moving forward, [mc]."
    id "You must help us."
    id "That is the only way."
    id "The only hope."
    scene fe 4
    mc "But... how? I'm just a guy."
    mc "Why not try to seek someone else’s help?"
    scene fe 3
    id "There is no other way, [mc]."
    show fe 4
    mc "How do you know there isn't another option?"
    show fe 3
    id "Because we've seen it."
    id "Because we've already tried."
    show fe 4
    mc "Tried...?"
    scene fe 3
    id "Keep moving forward, [mc]."
    id "Defy fate."
    play sound deception
    id "{sc=2}Break.{/sc}"
    play sound2 deception
    play sound5 deception
    id "{sc=2}{size=39}The.{/sc}"
    play sound3 deception
    play sound4 deception
    play sound6 deception
    id "{sc=2}{size=47}Chain.{/sc}"
    play sound risingshort3
    scene fe3
    pause 2
    stop music
    play soundloop rain3
    play sound2 thunder
    play sound3 chair1
    scene fe5 
    mc "*Sitting up* AAAAH!!!" with hpunchlong4 
    show screen saturdaycorner
    mc "*Panting* (Holy fuck...)"
    mct "God..."
    mct "I'm drenched in sweat... I feel like Dalia after a workout."
    mct "T-The one time I actually have a dream, and it goes like that."
    mc "*Touching your neck where the chain was* (That was a messed up nightmare. Or... at least I hope it was a nightmare. Better than suffering from the bleeding effect...)"
    play soundlow thunder fadein 2
    show fe 6 with dis
    mct "Ah, Kredon's rain is back." with dis
    mct "Three days in a row without it was too much to ask, I guess."
    play sound3 vibration
    play sound4 vibration
    show fe 7
    blank "{i}Your phone buzzes." with dis
    play music happyquirky fadein 7
    play sound clothes
    show fe 5 
    mc "*Grabbing your phone* (Hmmm... oh, it's a message from Penny.)" with dis12
    if penelopepath:
        mct "Damn, it's all coming back to me now..."
        mct "We arrived crazy late, and she crashed immediately. I went on a mission to clear out half the fridge, and then I went to bed as well."
        mct "Man, that sex was WILD. Penny's a damn succubus..."
        mct "We didn't even get a chance to chat about what happened."
        mct "She was too wiped out for that – I practically had to drag her home."
        play sound chair1
        show fe 6
        mc "*Popping open your chat app* (Time to suss out what the deal is...)" with dis 
        hide screen saturdaycorner
        call chat(penelope_chat4) from _call_chat_17
        mct "Damn..." with dis
        mct "I'm glad to see things with Penny didn't get awkward."
        mct "Boy, I can't wait to see her again..."
    else:
        mct "Hmmm... she says she went to the gym with Dalia and Annie."
        mct "Oh boy, I wish I could have joined them."
        mct "All three of them rocking gym leggings has to be a sight to behold..."
    mc "*Sighs* (Aaahh...)"
    play sound slap1
    show fe 5
    play sound2 slap1
    play sound3 slap1
    mc "*Slapping your cheeks* (But alright, let's focus now!)"with hpunch
    if novapath:
        mct "Time to get dressed and head over to Nova's place to log into that pirate server."
    else:
        mct "Time to get dressed and start getting ready to log into that pirate server."
        mct "I think I'm even gonna go grab some breakfast at Loco's before playing."
        mct "I've gotta hit the ground running!"
    mct "So no more daydreaming about women for today, [mc]."
    mct "You have a Gem to snag!" with hpunch
    play sound4 chair2
    play sound ["<silence 1.6>", doorclose]
    scene fe 8
    bla "You put on your clothes, grab your backpack and umbrella, and step out of your room."with dis15
    n "Good morning, honey!"
    show fe 10
    mc "*Turning around* Ah, good morning Na-" with dis
    $ unlock_look("nancy", 10)
    play sound2 swallow
    mc "*Gulps* N-Nancy."
    mct "Guess today's “no-daydreaming-about-women” vow was short-lived..."
    mct "Goddammit, that bathrobe is a menace."
    mc "D-Doing some laundry?"
    scene fe 9
    n "Yeah!"
    n "The girls headed out to the gym a few minutes ago, so I thought I'd get some chores done before logging in with you and Nova."
    show fe 10
    mc "Solid plan."
    if penelopepath:
        show fe 12
        n "I noticed Penny was particularly smiley today."with dis
        n "Guess yesterday's photoshoot was a hit?"
        show fe 11
        mc "Eh?"
        mc "Ah, y-yeah! It went really smoothly, I'd say."
        mc "I mean, we won't be certain about that contract from Ulysses until a few days have passed, but I'm feeling pretty positive."
        mc "We took some killer pics."
        n "Mm-mh."
        show fe 12
        n "Is there... anything else you wanna spill?"
        show fe 11
        mc "Spill? L-Like what...?"
        show fe 12
        n "I don't know. You tell me."
        show fe 11
        mc "N-Not really, no. That's about it."
        n "Hmm."
        mc "*Clears throat* Uhh... well, I'm excited to play with you and Nova today!"
        mc "Aren't you?? It's been a while!"
        show fe 9
        n "Ah, yes! Me too!" with dis
    else:
        show fe 9
    n "Mind if I grab a few more minutes? I'm almost done."
    show fe 10
    mc "Sure!"
    if novapath:
        mc "I still have to go to her house, actually. It's about a 20-minute walk, so we're not in any rush."
        show fe 12
        n "Ah, yeah, I forgot you were playing from her place." with dis 
    else:
        mc "I'm going to Loco's to buy some breakfast first, so we're not in any rush."
        show fe 12
        n "Ah, going to see Luna?" with dis
    n "You sure are quite the playboy, aren't you? Jumping from one date to another."
    if nancypath:
        n "*Sighs* If we weren't so busy, I'd probably suggest taking advantage of this alone time between you and me..."
    show fe 11
    if novapath:
        mc "W-What? I-It's not like that, I'm just going to Nova's to play."
        mc "We're just friends."
    else:
        mc "W-What? I'm just going to grab breakfast! Luna's not even going to be there, just her dad!"
        mc "And besides, we're just friends, nothing more!"
    show fe 12
    if nancypath:
        n "Yeah, we're all {i}really{/i} lucky to have you as our friend."
        show fe 11
        mc "That said... I've gotta say you look even sexier than usual somehow, Nancy."
        mc "If you were serious about seizing the empty house..."
        show fe 12
        n "Oh, I was..."
        play sound pop
        show fe 9
        n "But no time, unfortunately!"
        n "We'll have to leave that for another day!"
    else:
        n "Yeah, they're all {i}really{/i} lucky to have you as their friend..."
        play sound pop
        show fe 9
        n "But you're right, it's time to move!"
    show fe 10
    mc "But–"
    show fe 9
    n "Come on, let's get ready, we're running late!"
    n "Hop, hop!" with hpunch
    show fe 10
    mc "O-Okay, when should we meet? Or where?"
    show fe 9
    n "I'll send you both an invite to the New World server in 30 or 40 minutes!"
    n "I've got something pretty awesome to show you!"
    show fe 10
    mc "Oh, really?"
    mc "What is it?"
    show fe 9
    n "Nuh-uh! It's a surprise!"
    show fe 10
    mc "But–"
    show fe 9
    n "See you later, sweetie!"
    show fe 13
    bla "Nancy glides past you, her breasts gently swaying with each step, exuding a seductive allure as she trots along." with dis15
    mct "Oh boy..."
    if penelopepath:
        mct "I can see where Penny inherited her love for teasing me."
    mct "These women are gonna make me lose my mind..."
    if not nancypath and not penelopepath:
        mct "Sometimes I feel like I'm living with constant blue balls."
    mct "But anyway, she's right. No time to waste if I want to get there on time."
    if novapath:
        mct "I hope Nova's all set."
    mct "Let's roll!"
    if not novapath:
        mct "That Gem only has one name etched on it... [mc!u] [lastname!u]!"
        mc "LET'S GO!" with hpunch
        jump piratestart
    stop soundloop fadeout 5
    stop music fadeout 5
    scene black with dis2
    show screen afewminuteslater with dis15
    pause
    play soundloop2 rain5 fadein 5
    play sound carpasswet
    scene fe 14 
    hide screen afewminuteslater
    with dis25
    mct "Alright, here we are." with dis
    mct "If I'm not mistaken, I arrived just in time."
    show fe 15 with dis17
    play sound2 doorbell
    mc "*Ringing the doorbell* (Heh, I still remember the first time I met Nova, right here at this door.)" with dis
    mct "What a cringe-fest that was."
    mct "But hey, after a gazillion adventures together, here we are, poised for..."
    mct "Um..."
    play sound3 carpasswet
    mct "I'm not even sure what this is supposed to be. We were supposed to watch the last episode of One Piece together, then it was delayed, but we didn't cancel the date."
    mct "Date. Date? Is this even a date?"
    mct "Hmm..."
    mct "Bah, don't overthink it, [mc]."
    mct "Don't be nervous."
    mct "I mean, I'm not nervous. Am I nervous? Why am I nervous?!"
    mct "It's just Nova! We practically live in each other's pockets!"
    play sound doorbell
    mc "*Ringing the doorbell* (Speaking of, where the fuck is this girl?!)"with hpunch 
    play sound2 doorbell
    mc "*Ringing the doorbell* Hello?!"
    no "Yes, yes, sorry! Come in!"
    no "It's open!"
    play sound3 dooropen1
    play sound ["<silence 1.6>", doorclose]
    stop soundloop2 fadeout 3
    play music happyquirky fadein 8
    play sound4 drips
    scene fe 16 with dis15
    bla "You stroll into Nova's place, umbrella in hand, and drop it right by the door." with dis12
    play sound5 clothes4
    play sound6 clothes3
    mc "*Taking your jacket off* Ah, finding refuge from the rain feels like such a relief!"
    mc "It's starting to get chilly out there these days."
    no "I'm sorry, I was in the middle of wrapping up a game!"
    no "You can drop the package right there!"
    play sound2 doorclose
    show fe 17
    no "*Closing the door behind her* Do you need me to sign anything or..." with dis12
    $ unlock_look("nova", 13)
    no "Eh?"
    mc "Package? What package?"
    show fe 18
    no "[mc]?" with dis
    no "You're not the Amazon guy."
    show fe 19
    mc "Uh... nope."
    show fe 18
    no "What are you doing here?"
    show fe 19
    mc "Um..."
    mc "You invited me over."
    mc "To watch the last episode of One Piece."
    mc "And join Nancy on The New World server."
    mc "The “pirate-themed” day... r-remember?"
    mct "Did she really forget...?"
    show fe 18
    no "Oh... but... the episode of One Piece got delayed."
    show fe 19
    mc "Well... yeah, but we didn't scrap the whole plan for the day, so... I figured..."
    mc "I thought we were still on for the rest of it."
    show fe 20
    no "Oh... damn, I just assumed we called it off and that we'd play from our own respective places." with dis
    show fe 21
    mc "Ah."
    mc "Oh."
    no ". . ."
    mc "Well, this is awkward."
    mc "Um... might be better if I just head out then."
    mc "We can p–"
    show fe 20
    no "NO! No!" with hpunch
    no "You can stay!"
    no "It's just that... I didn't even think about it ALL week, so I honestly didn't prepare anything."
    show fe 21
    mc "Oh well, if that's the only problem, no worries!"
    show fe 20
    no "Agh, I bet you were hoping for a ton of SUPER cool and fun activities and even delicious homemade food, huh?"
    show fe 21
    mc "Not rea–"
    show fe 20
    no "I COMPLETELY spaced on our meet-up plans, I'm SO sorry."with hpunch
    show fe 21
    mc "No need to apologize, Nova, it's all good."
    mc "We've all been having a ton of things in our heads recently."
    mct "Looks like I was the only one overthinking today's stuff after all."
    mc "Let's just enjoy our time together. We're gonna be in Eternum for most of the day anyway."
    show fe 22
    no "Alright, then you can go to the guest room."with dis
    no "My room's a bit of a chaos zone right now, so we'll probably be more comfortable there."
    show fe 23
    mc "Alright, cool!"
    show fe 22
    no "It's the second room on the right after you head upstairs."
    no "I'm gonna change into the E-suit real quick and join you, make yourself at home!"
    show fe 23
    mc "Thanks!"
    scene fe 24 with dis22
    mct "I guess it's this one." with dis12
    mct "Man, I feel like a bit of an idiot. I should've texted her before showing up."
    mc "*Sighs* (But anyway, now I'm already here.)"
    show fe 25
    mct "I guess we should just dive into Eternum, focus on the mission, and forget about it." with dis15
    play soundlow thunder fadein 2 volume 0.5
    mct "After all, nothing beats playing Eternum on a rainy day."
    play sound doorclose
    show fe 26
    no "*Closing the door behind her* Alright, I'm ready!" with dis12
    mc "Damn, that was fast."
    play sound chair1
    show fe 27
    no "*Jumping onto the bed next to you* Again, sorry for blanking on today." with dis
    no "I completely forgot."
    no "I'll prepare a SUPER FUN event next time, I promise."
    show fe 28
    mc "And also again, don't worry, Nova."
    mc "I'm happy just hanging out with you, no need to prepare anything."
    mc "Now, let's snag that Gem from Coyote and take it home, shall we?!"
    show fe 27
    no "YES!"
    play sound chair1
    show fe 29
    no "*Turning around* I'll let you change into the E-suit too." with vpunchslow 
    play sound2 clothes3
    play sound3 belt
    play sound4 zip volume 0.5
    show fe 30
    mc "*Starting to get changed* I don't mind if you look, don't worry." with dis15
    mc "Wouldn't be the first time..."
    no "No way!"
    mc "*Chuckles* Okay, okay, as you wish."
    mc "You know, now that I take a closer look, I'm digging this new hairstyle of yours!"
    show fe 31
    no "What, this?" with dis08
    no "It's just a quick fix because it's practical and I was short on time."
    mc "Oh, really?"
    mc "You didn't even have to straighten your hair?"
    no "Not really. It depends on... the day. Sometimes it's more straight on its own."
    mc "Is that how it works...?"
    show fe 30
    no "Really, it just took me 3 minutes." with dis 
    no "But anyway... you ready?"
    mc "Yep!"
    play sound chair1
    show fe 32
    no "*Turning around* Cool!" with dis
    show fe 34
    mc "Should we grab something to eat before jumping into the game?"
    mc "I don't know how long we're gonna be playing, I guess it depends on how fast we can find Coyote's base."
    show fe 33
    no "I don't know... I already had breakfast. Let's just go with the flow."
    show fe 34
    mc "I'm fine with that."
    show fe 33
    no "Just chilling, you know, this is... nothing special."
    no "We didn't even remember our plans until a few minutes ago, so what's the big deal, right?"
    show fe 34
    mc "Well... I kinda did."
    show fe 33
    no "No biggie. Just a laid-back Saturday."
    show fe 32
    no "You can't really have any high expectations for a normal Saturday, am I right?"
    no "Just a regular, uneventful Saturday."
    show fe 34
    mc "I didn't come with any high expectations."
    show fe 32
    no "Anyway, aren't you getting bored? Let's play already."
    show fe 33
    no "I'm sooo bored. Aren't you?"
    show fe 34
    mc "Um..."
    show fe 33
    no "Let's play, and then we can decide if we should casually grab something from the fridge, depending on the time."
    show fe 32
    no "You know, the kind of things we all do on a normal Saturday."
    show fe 34
    mc "Mm-hm."
    show fe 33
    no "Just burning some ti–"
    play sound slam
    play sound2 slam3
    stop music
    play music2 quirkynova fadein 6
    scene fe 35
    san "*Slamming open the door* There you are!" with hpunch
    no ". . ."
    san "I thought you'd be in your room, not the guest one!"
    play sound chair2
    show fe 35b
    no "*Standing up* M-Mom?! I told you to knock on my door!" with dis
    no "And can you NOT slam the doors like that?!"
    show fe 36
    san "It's so good to see you again, [mc]!"
    show fe 37
    mc "Thank you, Mrs. Johnson! I had no idea you were home!"
    mc "I'm sorry, I would have said hello if I'd known."
    show fe 36
    san "Ah, don't worry about that, sweetie."
    san "I just came to bring you some cappuccinos!"
    show fe 37
    mc "Oh, thank you so much!"
    show fe 35b
    no "Yeah, yeah, thanks, Mom. Can you give us some privacy now?"
    show fe 36
    san "I'm so glad you're finally here! Nova was practically chewing her nails off all week thinking about today."
    show fe 37
    no "NO, THAT'S NOT TRUE!" with hpunch
    mc "Is that so...? And here I thought it was just a regular Saturday for her..."
    show fe 36
    san "*Laughs* She was crushed when they canceled those pirate cartoons you were going to watch together!"
    san "Yesterday she spent the whole day whining and brainstorming plans for today."
    scene fenova
    no "T-That's because I really wanted to see that episode, so it was a bummer!"
    scene fe 36
    san "She even attempted to bake a special dessert herself!"
    san "Unfortunately, we had to bid it farewell because she kinda... set it on fire."
    scene fe 38
    san "...and the kitchen too... {i}again."
    scene fenova
    no "I-I only bake once in a while."
    no "A-And it's not my fault the oven doesn't make any noise when the timer's up!"
    scene fe 37
    mc "*Laughs* So... is there anything else Nova had planned for today?"
    show fe 36
    san "She tried to draw one of those Japanese comics of hers for you, but she wasn't happy with how it turned out, so she tossed it away."
    scene fe 41
    no "I'll try it again another day."
    scene fe 36
    san "Then I suggested a cartoon marathon, but she wasn't sold on that either."
    scene fe 39
    no "[mc] wouldn't have liked that. He's too... {i}cool{/i} to spend a whole day watching anime with me."
    scene fe 36
    san "Oh, and did you see the new hairstyle she whipped up for you?"
    san "She spent a good three hours this morning, trying to straighten her hair and comb it just right."
    san "I even had to give her a hand!"
    scene fe 37
    mc "Oh, really?? She told me it only took her three minutes and was just a quick, casual style."
    scene fe 40
    no "W-Well, yeah, it might have taken a bit more time than 3 minutes, now that I think about it..."
    no "I thought you were referring to my scrunchy, actually."
    scene fe 36
    san "*Chuckles* I'm so glad to have you with us, [mc]."
    san "It's such a relief to finally see Nova with a thoughtful and handsome boy instead of alone with her computer."
    san "Seeing her with such a big crush takes me back to my younger days!"
    show fe 42
    no "OKAY, THAT'S ENOUGH FOR TODAY!" with hpunch 
    no "Thank you for the coffees, Mom! See you later!" with hpunch
    show fe 38
    san "Your dad and I are heading out now, but if you two are planning to get cozy, remember to–"
    show fe 43
    no "{sc=2} OH MY GOD, SHUT UP!!!!!!!{/sc}" with hpunch 
    play sound whoosh6
    play sound2 punch
    scene fhefeyrfbyefdh
    no "*Pushing her mom away* OKAY, BYE!" with hpunch
    san "Bye guys, enjoy your Eternum session!"
    mc "Thank you, Mrs. Johnson!"
    play sound slam
    play sound2 slam3
    stop music2
    scene fe 26 with hpunch 
    pause
    play music happyquirky fadein 6
    play sound clothes3
    scene fe 45
    bla "Nova slides around the corner of her wardrobe while you casually take a seat on her bed, smirking, without saying a word." with dis12
    show fe 46
    no "Sorry about that, my mom can be a pain sometimes."
    no "A-And she has such an imagination on her, my god."
    show fe 45
    mc "*Chuckles* I knew that hairstyle didn't take you only three minutes."
    show fe 46
    no "I did it for myself, seriously, so it’s okay if you don't like it – I won't feel bad."
    show fe 45
    mc "What are you talking about? I lo–"
    show fe 46
    no "SERIOUSLY! I won't feel bad."
    no "It's better if you don't say anything."
    show fe 45
    mc "But–"
    show fe 46
    no "I'm trying to work on my self-esteem and anxiety, so I don't need so much validation from others anymore."
    no "A simple nod when you notice is more than enough."
    show fe 47
    no "Like... “huh, new hairstyle, Nova? Huh. Cool.”"
    show fe 48
    mc "*Laughs* Alright, got it."
    mc "I did catch your new hairstyle today, yeah."
    show fe 47
    no "Yes, I was going for something that looked kinda pirate-y."
    show fe 48
    mc "Mmh, I can see that."
    show fe 47
    no "Yuuup."
    show fe 48
    mc ". . ."
    mc "Sooo... should we log in now? Nancy must be waiting for us already."
    show fe 47
    no "Yep!"
    show fe 48
    mc ". . ."
    show fe 47
    no "Any last comments before getting down to business?"
    show fe 48
    mc "Mmmmhh, not really, no."
    show fe 47
    no "I mean, you can say something about my hairstyle if you want to."
    show fe 48
    mc "Yeah, I already saw it."
    mc "It's new."
    no "Mm-hm."
    show fe 47
    no "Cool."
    show fe 48
    mc "Hmph."
    show fe 48
    no "Hmm."
    mc ". . ."
    no ". . ."
    mc ". . ."
    play sound jumpscare3b
    play sound2 fist
    stop music
    show fe 49
    no "OKAY, FORGET EVERYTHING I SAID – I NEED COMPLIMENTS OR I'M GONNA STARVE AND DIE!" with hpunch
    mc "I-I LOVE IT, YOU LOOK SO CUTE!" with hpunch
    play music happyquirky fadein 5
    play sound2 chair1
    scene fe 50
    no "*Giggles* Thanks." with dis
    show fe 52
    mc "*Laughs* You're something else."
    mc "I'm serious though, you really look lovely with this hairstyle."
    mc "Oh, and want another one? Those pants you had on earlier? Your tummy looked extra sexy with them..."
    scene fe 50
    no "*Giggles* Thank you, thank you."
    scene fe 52
    mc "Okay, so... let me guess."
    mc "You thought I'd come in here with sky-high expectations, but when the episode got delayed, you totally freaked out thinking I'd get bored and start disliking you."
    mc "Is that why you've been acting all weird since I arrived?"
    show fe 51
    no "Eh..."
    no "*Giggles* Something like that."
    show fe 52
    mc "*Chuckles* You're such a goofball."
    mc "It's {i}literally{/i} impossible to get bored around you."
    mc "You manage to turn the most mundane stuff into a wild whirlpool, and I love it."
    show fe 51
    no "T-Thank you."
    show fe 52
    mc "And now that that's been said... can we switch back to being normal now?"
    show fe 51
    no "*Chuckles* Yes, we can."
    show fe 52
    mc "Sweet!"
    mc "Now buckle up because I'm taking the reins on our {i}date{/i} agenda today. No veto power for you today!"
    show fe 50
    no "*Giggles* Okay."
    mct "I knew she'd like me to call it a “date”."
    show fe 52
    mc "First up, we're diving into Eternum to snag that Gem of Doom from El Coyote."
    mc "Then, we'll take a break, and I'll swing by Mario's Pizza to grab a couple of calzones."
    mc "We'll chow down together, and after that, it's decision time: anime, video games, or another round of Eternum on a random server, just the two of us. You call the shots!"
    mc "Sounds good?"
    show fe 51
    no "Sounds awesome."
    show fe 52
    mc "Nice!"
    mc "So, Ms. Delilah Warren... ready to get our third Gem of Doom?!"
    play sound chair1
    play sound2 fist
    show fe 53
    no "*Bumping your fist* Heck yeah!" with hpunch 
    mc "READY TO DESTROY EL COYOTE AND THE REST OF HIS CREW?!" with hpunch 
    no "YES!" with hpunch 
    mc "READY TO CONQUER ETERNUM?!" with hpunch 
    no "{sc=2}YES!!!!{/sc}" with hpunch 
    mc "{sc=2}LEEEEEET'S GO!!!{/sc}" with hpunch 
label piratestart:
    play sound ding
    stop music
    scene black
    play soundloop ["<silence 1.2>"]
    queue soundloop wavesship fadein 8
    pause 
    show screen afewhourslater with dis22
    pause
    play sound7 wave volume 0.7
    hide screen afewhourslater
    scene pirateship1 
    with dis17
    play sound2 seagull2
    pause 2.5
    play sound seagull
    pause 5
    play sound3 seagull2
    play music pirate1 fadein 7 volume 0.8
    play soundlow wave
    scene fe 55
    mc "*Gagging* Uggghhh..." with dis14
    mc "This seasickness is killing me... how much longer are we going to be stuck drifting in this never-ending ocean...?"
    play sound chair2
    play sound2 fist
    play sound3 jump2
    play sound4 seagull
    show fe 56
    no "*Hopping onto the ship's rail* [mc]! Check out the sea!" with dis
    $ unlock_look("nova", 14)
    no "We finally got a break from those relentless waves!"
    no "The ocean's as calm as a kiddie pool right now."
    show fe 57
    mc "Yaaay..."
    mc "Can we spot any islands yet?"
    mc "I'm dying to finally set foot on solid ground..."
    show fe 56
    no "Not yet, but Nancy said we're already headed back to Tortuga."
    show fe 57
    mc "Tortuga?"
    show fe 56
    no "The island where we started."
    no "The one with the Exit Portal, that tavern, and all those pirates."
    play sound clothes4
    show fe 58
    mc "Ohhh... yeah, it's been so long that I had almost forgotten." with dis12
    play sound2 chair2
    show fe 60
    mc "*Leaning on the rail* I mean, how long have we been going in circles??"with dis12
    play sound3 seagull
    show fe 61
    no "Since we left Tortuga? I'd say... about 6 hours or so."
    show fe 60
    mc "Only?! It felt like I spent an eternity surrounded by nothing but water."
    play sound chair2
    show fe 63
    n "*Leaning on the rail as well* For being the strongest among us, you sure can't handle a little water, [mc]!"with dis
    $ unlock_look("nancy", 11)
    show fe 62
    mc "Because I can't control it!"
    mc "Getting dizzy isn't about strength or skill..."
    show fe 63
    n "*Chuckles* Still, I can't help but feel a bit disappointed."
    show fe 62
    mc "*Clears throat* Well, now that the waves have chilled, I'm feeling better."
    show fe 59
    no "Ah..."
    show fe 60
    mc "Did I say better? I meant {i}much{/i} better."
    show fe 63
    n "Oh..."
    show fe 62
    mc "Actually, scratch that – I'm feeling TOP-NOTCH already!"
    show fe 59
    no "OH!"
    show fe 60
    play sound3 seagull2
    mc "See? I can recover suuuper fast. It's all about discipline!"
    mc "I'm ready to kick some asses again!"
    show fe 63
    n "*Laughs* Ah yes, that's the resilient and mighty warrior I know."
    show fe 62
    mc "BUT OF COURSE!"with hpunch 
    mc "*Chuckles* I know what you did there, by the way."
    mc "But it successfully got me all pumped up again, so I won't complain."
    play sound seagull
    show fe 61
    no "So... we scoured all the supposed trading routes of El Coyote's ships, checked every rumored hiding spot, and still came up empty-handed."with dis
    no "Do you think he managed to slip away from us again?"
    show fe 60
    mc "He's got to be around. The WRE turned the world upside down – land, air, and sea, and this server is the last hiding spot he has left."
    mc "He's just lurking somewhere with his Gem like a coward."
    show fe 63
    n "Oh, we'll track him down, no doubt, just that... it might take a bit longer than we thought."
    show fe 62
    mc "From what I saw in the wild west server, he's got a good network of informants, but he's not exactly the sharpest tool in the shed."
    mc "He'll slip up eventually."
    show fe 60
    mc "But anyway, we can save the El Coyote hunt for tomorrow." with dis
    mc "I don't know about you, but I'm absolutely famished right now."
    show fe 59
    no "Me too!"
    play sound3 seagull2
    show fe 63
    n "The captain mentioned earlier that if winds play nice we should be back in Tortuga in less than 20 minutes."
    show fe 62
    mc "Ah, sweet!"
    if novapath:
        show fe 60
        mc "I promised someone pizza for lunch, and I can't risk her being mad at me."
        mc "I mean, we're already behind schedule, so it'll really be dinner. But still."
        show fe 59
        no "*Laughs* You do well to fear me!"
        no "I can be scarier than Dalia when I'm hungry."
        show fe 63
        n "*Chuckles* No time to waste, then!"
    else:
        mc "To Tortuga it is, then!"
    play sound2 chair2
    show fe 66
    n "*Getting up* Maximo!"with dis12
    play sound stairswood2
    show fe 65
    leg "*Climbing down the stairs* Yes, my Empress?" with dis15
    show fe 66
    n "Could you go to the lower decks and inform the crew that we're going back to Tortuga?"
    n "Tell them to orient the sails towards North-East to optimize speed, and ensure the staysails are efficiently deployed!"
    n "Full-speed ahead!"
    show fe 65
    leg "Right away, your Highness!"
    play sound chair2
    play sound2 stairswood2
    show fe 67
    mc "*Standing up* Oh damn, you're turning into an expert sailor now too?!" with dis12
    show fe 68
    n "*Chuckles* Obviously."
    n "I must master all domains where the WRE can make an impact."
    n "I devour a book or two every week about different disciplines to stay ahead. This week's pick was “Sailing of the Golden Era.”"
    play sound3 seagull
    show fe 67
    mc "Sometimes I wonder where you find the time."
    mc "I feel like I'm busier than ever, and next to you it looks like I don't do shit."
    mc "You've got your full-time job, you take care of Dalia, Penny, Annie and me, AND you still have time to run an Empire with a military network spying on half the servers in Eternum."
    mc "How do you even manage that?"
    show fe 68
    if nancypath:
        n "You’re also constantly helping us, [mc]."
        if daliapath and penelopepath and lunapath and novapath: 
            n "Whether it's supporting Dalia's competitions, Penny's photoshoots, Luna's family get-togethers, being Annie's rock since forever, or simply chilling with Nova today."
        show fe 67
        mc "Well... hanging out with all of you is the best part of my day."
        mc "I would hardly call that a “sacrifice” on my part."
        show fe 68
        n "That doesn't make it any less significant."
        n "You're the glue holding us together, [mc]. Don't ever forget that."
        play sound chair2
        show fe 69
        n "*Turning around* But alright, let's not get into melodrama mode again!" with dis12
    else:
        n "Mastering the art of time management, that's the key!"
        n "I could school you on it someday."
        show fe 67
        mc "*Chuckles* Yeah, I could use some of that."
        mc "I appreciate it."
        play sound chair2
        show fe 69
        n "*Turning around* But alright, let's leave that for another time!" with dis12
    n "We've got more fun things to do and more work to tackle!"
    mc "*Chuckles* Alright."
    n "Gentlemen! Sails up!"
    stop music fadeout 6
    play sound ["<silence 1>", seagull]
    n ". . ."
    n "Mmmh?"
    mc "Huh?"
    scene fe 70
    n "Where's everyone at...?" with dis12
    n "I thought I asked Maximo to round up the crew on deck, didn't I?"
    show fe 71
    no "Now that you mention it, I haven't seen a single sailor up here in a while."
    no "Maybe they're all taking a nap?"
    show fe 70
    n "Do you think so?"
    n "That'd be extremely lazy, even for these guys..."
    show fe 72
    n "And do you know what's even weirder? There's no noise at all..." with dis15
    play sound5 seagull
    n "Just the ship rocking with the waves and the distant seagull calls."
    show fe 73 with dis15
    pause
    play sound3 deception
    play sound4 impact3
    scene fe73gray
    pause .08
    scene white
    pause .01
    scene fe73gray 
    pause 0.08
    scene fe 73
    pause
    play sound2 transformpower
    show fe 74 with dis14
    pause
    play sound wood2
    play music piratetension fadein 10
    $ renpy.music.set_volume(0.6, delay=12.0, channel='soundloop')
    scene fe 75 with dis17
    mc "I know you're there, I can sense your presence." with dis12
    no "Huh??"
    mc "Open the door and step out."
    bla "You hear a deliberate, ominous laugh coming from behind the closed doors."
    play sound2 saloondoors
    show fe 76 with dis15
    boo "*Dragging Maximo alongside him* Well, well, well..." with dis15
    boo "Looks like your reputation is well-deserved... [nickname]."
    if not nickname == mc:
        boo "Or should I just call you [mc]?"
    if daliacabin:
        mc "Boone...?"
    else:
        mc "Who are you? And how do you know me?"
    show fe 76d
    n "*Gasps* Maximo!" with hpunch 
    play sound holster2
    show fe 76c
    no "W-Who's this guy?!"with hpunch 
    if daliacabin:
        no "Do you know him??"
    show fe 76
    if daliacabin:
        mc "I do know him..."
        mc "His name's Boone. He's the guy from the Frontier Trails server that I met with Dalia, the one who spilled about El Coyote's hideouts."
        mc "But... what the hell, Boone? You told me you left his gang!"
    else:
        boo "Indeed, he doesn't know me. But I had the pleasure to meet your charming companion, Dalia, when she paid me a visit in my cabin."
        mc "You...? You're the one Dalia talked to? You're the source of all the intel on El Coyote's hideouts??"
    show fe 77
    boo "*Grabbing his bandana* You see..."with dis
    boo "That man you dueled and dropped in Blackridge?"
    boo "He was just a decoy. One of my guys."
    mc "What...?"
    play sound clotheswhoosh
    play sound2 tear2
    play sound4 holster2
    play sound5 fist
    show fe79
    bla "Boone tosses his bandana to the ground, stepping on it furiously." with vpunch 
    play sound3 impact3
    scene fe 78
    ec "{b}I AM EL COYOTE." with dis08
    show fe 79
    mc "What...?"
    mc "You son of a bitch..."
    mct "Fuck, I knew something was off about the 'El Coyote' I encountered in Blackridge."
    mct "He seemed too weak to own a Gem of Doom, let alone avoid Thanatos's pursuit for so long."
    mct "I can't believe I let him fool me."
    mc "But... this doesn't make any sense, why did you tell us your own hiding spots? Why not just come after me directly?"
    show fe 78
    ec "Because I needed you here, in The New World."
    ec "I need your help, [mc], I'm not ashamed to admit it."
    show fe 79
    mc "My help...?"
    show fe 78
    ec "Although, gotta say, it took you a freaking eternity to get here, and now time's running out. So, be a good sport and pay attention, will ya?"
    ec "Oh, and before you even think about calling for backup... your crew's done for. Dead. Kaput."
    show fe 79
    mc "Motherfucker..."
    show fe 78
    ec "Now, now, no need to have a potty mouth! Swearing like a sailor on this ship?"
    ec "Just behave, and your dear friend here won't meet his maker."
    show fe 79b
    play sound holster2
    leg "I will gladly give my life for the WRE and the Empress!"with hpunch 
    leg "Don't heed the demands of this terrorist, General!"with hpunch 
    show fe 78
    ec "Inspiring loyalty!" 
    ec "*Mocking tone* What will you do, {i}General{/i}...?"
    show fe 79
    menu:
        with dis
        "Don't listen to his demands":
            mc "I won't bow to your demands."with dis08
            mc "Hand over your Gem, or prepare for the consequences."
            mc "I won't ask twice."
            show fe 80
            ec "Agh, looks like your pals don't give a fuck about your well-being, Maximo."
            ec "If you ever fancy joining a crew that values loyalty as much as you, you can come find me."
            ec "Unlike your general here, I'd lay down my own life for any of my comrades."
            ec "*Sighs* Such a pity you're on the wrong side of this tale."
            play sound revolver2
            play sound2 shotgun
            play sound3 shotgun
            play soundlow shootecho volume 0.4
            play sound4 blood2
            play sound7 seagull
            scene white
            pause 0.003
            scene fe 81 with hpunch
            pause .6
            play sound5 ["<silence 0.6>", fall]
            play sound6 ["<silence 0.6>", woodhit]
            show fe 82 with dis
            pause .2
            play sound seagull2
            mct "Holy shit, he didn't even flinch..."with dis08
            scene fe 76d
            n "MAXIMO, NO!" 
            play sound holster2
            show fe 83         
        "[gr]Negotiate":
            $ maximoalive = True
            mc "*Motioning to Nova to lower her gun* Let Maximo go first." with dis08
            mc "I won't entertain any of your demands until you release him."
            show fe 80
            ec "Aww, look at that, Maximo. Isn't it endearing how he cares about his crew?"
            ec "That's something I can respect, yes."
            show fe 78
            ec "Very well! Consider this a token of goodwill."
            show fe 82b
            play sound ["<silence 0.3>", fallfull]
            bla "El Coyote releases Maximo, who slumps to the floor from the pressure applied to his neck and crawls away gasping for breath." with dis
            play sound7 holster2
            show fe 83b         
    ec "*Pointing the gun at you* Alright, ladies and gentlemen!" with dis12
    ec "I guess now that we're finally in a more intimate setting, it's time to have a quick, yet fruitful conversation."
    ec "First things first, I've got one condition!"
    stop soundloop
    stop music
    play sound shipanimation
    play sound2 impactwood
    show pirateship2 
    pause 4.9
    play soundloop wavesship
    play sound crashwood
    play sound2 bonecrush
    play sound3 gundrop
    play sound4 rocks
    play sound5 impactwood
    scene fe84 with hpunchlong4
    pause
    show fe 76d
    n "Oh my god, that was fast!"
    n "You nearly vanished into thin air there!"
    show fe 76c
    no "*Panting* D-Dead? He dead? I-Is he dead?"
    show fe 84
    mc ". . ."
    play music piratedark fadein 5
    ec "{sc=2}Hahahahah...{/sc}"
    ec "{sc=2}Yes... YES!{/sc}"
    ec "{sc=2}You didn't even hesitate!{/sc}"
    play sound glitch4
    scene coyotedecoy1
    if daliacabin:
        ec "{sc=2}I could sense your determination from the day I saw you...{/sc}"with hpunch
    else:
        ec "{sc=2}I was right to choose you...{/sc}"with hpunch
    scene fe 76c
    no "What in the world is that..."
    scene fe 85
    mc ". . ."
    scene fe 86b
    mc "*Smirks* Hmmm." with dis 
    scene fe 86
    mc "Another decoy..."
    mc "Looks like our friend El Coyote here prefers pulling strings from the shadows, am I right?"
    play sound glitch4
    scene coyotedecoy1
    ec "I've always favored staying hidden over exposing myself."with hpunch
    ec "If it wasn't for this little habit of mine, I'd probably have lost my Gem of Doom a long time ago."
    scene fe 86
    mc "Okay then... spill it. What do you want from me?"
    mc "The two Gems of Doom we have?"
    play sound glitch4
    scene coyotedecoy1
    ec "Incorrect!"with hpunch
    ec "Actually, I'm willing to hand over the one I've got."
    ec "As much as I take pride in my deceptive skills, I'm aware I can't compete in this race at the same level as the others."
    play sound glitch4
    scene coyotedecoy1
    ec "So, I thought of taking a little advantage of the situation."with hpunch
    scene fe 86
    mc "Why me?"
    scene fe 85
    ec "Well, out of the strongest contenders out there, you seemed to be the most... reasonable one."
    ec "At least more so than Thanatos."
    scene fe 86
    mc "And what do you want in exchange?"
    play sound glitch4
    scene coyotedecoy1
    ec "The Heart of the Abyss."with hpunch
    ec "A treasure that resides on the Island of the Lost Souls."
    ec "But here's the tricky part: it only surfaces once a year during the 11th lunar cycle, which conveniently ends... today!"
    ec "I would have preferred to give you more leeway, but you took your sweet time coming to see me."
    scene fe 86
    mc "A treasure in exchange for your Gem of Doom?"
    mc "And why didn't you go get it yourself?"
    play sound glitch4
    scene coyotedecoy1
    ec "The Island of the Lost Souls is more than 100 miles away from the nearest Exit Portal, heavily guarded by mortal dangers."with hpunch
    ec "And, as I said, one of my strengths is recognizing both my abilities and shortcomings."
    ec "I knew I'd never make it through the journey."
    play sound glitch4
    scene coyotedecoy1
    ec "But you?! You can pull it off!"with hpunch
    ec "Bring me The Heart of the Abyss and my Gem of Doom will be yours!"
    mc "Mmh."
    scene fe 86
    mc "And how do I even know where to find this island?"
    play sound glitch4
    scene coyotedecoy1
    ec "Go back to Tortuga and seek out Gypsy Goldtooth at the tavern!"with hpunch
    ec "He will tell you how to find the island and provide you with a map!"
    mc "Hmph."
    play sound glitch4
    scene coyotedecoy1
    ec "You've got exactly 16 hours left! As soon as the sun rises tomorrow, the Island of the Lost Souls will vanish along with The Heart of the Abyss."with hpunch
    ec "And, of course, my Gem of Doom will remain forever out of your reach!"
    ec "*Laughs* You know how sneaky I can be, don't you?!"
    play sound glitch4
    scene coyotedecoy1
    ec "{sc=2}16 hours, [mc]!{/sc}" with hpunch
    play sound3 glitch4
    scene coyotedecoy1
    ec "{sc=2}The clock is ticking!{/sc}" with hpunch
    stop music fadeout 7
    play sound steam2 volume 0.33 fadein 2
    scene fe 84
    bla "El Coyote falls silent as you feel how life abandons his avatar." with dis2
    play sound2 fallfull
    scene fe 87 with dis2
    bla "You let El Coyote's decoy crumple, lifeless, and turn towards the girls after regaining your normal appearance." with dis12
    play music pirate1 fadein 8
    mc "Well..."
    mc "Looks like that cunning bastard was one step ahead of us the entire time."
    show fe 88
    n "You can say that again... we might have underestimated him."
    show fe 87
    mc "Oh, we definitely did."
    mc "Primarily because I mistook El Coyote for that foolish guy I dueled in Blackridge."
    mc "But this one? Ohhh yeah, it all makes more sense now."
    mc "*Smirks* THIS is a worthy opponent."
    play sound6 seagull
    show fe 88
    if not maximoalive:
        n "I feel bad for Maximo."
        show fe 87
        mc "Well, at least we can hold onto all the loot here on the ship and return it to him and the other WRE members when they can play again."
        show fe 88
        n "*Sighs* Yeah, that's true."
        n "Anyway... what's the plan now? Do we even have one?"
    else:
        n "And what's the plan now?"
    show fe 87
    mc "What do you mean? Isn't it obvious?"
    mc "I'm not one to shy away from a challenge when it's presented to me."
    mc "We're going to track down that treasure and use it to trade for our 3rd Gem of Doom!"with hpunch
    show fe 89
    no "HELL YES!" (multiple=2) with dis
    n "YEAH!" (multiple=2)
    if maximoalive:
        play sound woodhit
        play soundlow whoosh6
        scene jjjkdjddd
        leg "*Kicking the floor* Thank you for saving my life, General!"with vpunch 
        scene fe 88b
        mc "Oh, it was nothing, Maximo."
        mc "I couldn't let you bite the dust that easily, not after all you've done for us."
        scene fe 88c
        leg "I pledge to dedicate my entire life to the WRE, Empress Nancy, and to you, my General!"
        show fe 88b
        mc "*Playing along* I expected no less from someone of your caliber."
        play sound6 seagull2
        mct "Maximo really takes roleplaying to a whole new level."
        mct "Some players truly immerse themselves in Eternum, even though they're completely unaware of the reality beneath it all."
        scene fe 88c
        leg "I request permission to name my child, due in two months in the real world, [mc] the Great!"
        scene fe 88b
        mct "M-Maybe even immerse a little bit too much."
        mc "Um... that won't be necessary, Maximo."
        scene fe 88c
        leg "I insist, General! Please!"
        scene fe 88b
        mc "P-Perhaps you should discuss that with your wife first."
        scene fe 88c
        leg "She's named our other two lovely children already."
        leg "Now, it's my turn."
        play sound6 seagull
        scene fe 88b
        menu:
            with dis08
            "Accept":
                $ maximochildname = True
                mc "Uh... w-well, okay then."with dis08
                mc "But just [mc] is fine. No need for... “the Great”."
                scene fe 88c
                leg "Excellent idea, General! We shall name him [mc]!"
            "Refuse":
                mc "You might want to consider a different name, Maximo, really."with dis08
                mc "It makes me feel kind of awkward, to be honest."
                mc "How about something like... Maximo Jr., or..."
                mc "I don't know, Victor, or Chang, or..."    
                scene fe 88c
                leg "Excellent idea, General! We shall name him Chang!"
                scene fe 88b
                mc "Uh... t-that's not what I was trying to–"
        scene fe 88c
        leg "I'll go take control of the rudder to ensure a safe return to Tortuga now!"
        leg "Permission to proceed?"
        scene fe 88b
        mc "Um... yeah, of course. You're dismissed."
        scene fe 88c
        leg "Thank you!"
        scene fe 91 with dis15
        mc "*Turning around* He's certainly committed to his role, huh?"with dis
        show fe 90
        n "*Laughs* Definitely, no one can say otherwise."
        show fe 91
        mc "Can we go back to Tortuga with just the four of us?"
    else:
        scene fe 91
        mc "Can we go back to Tortuga with just the three of us?"
    show fe 90
    n "We can!"
    n "The sails are set, the sea's calm, and we've already got our course dialed in."
    n "Tortuga should be on the horizon in less than 5 minutes."
    show fe 91
    mc "Excellent!"
    play sound6 seagull2
    mc "El Coyote mentioned that the “Island of the Lost Souls” is around 100 nautical miles away."
    mc "How long do you figure it'll take us to cover that distance?"
    show fe 90
    n "Well, considering this ship can hit speeds of 14 or 15 knots... I'd say about 7 or 8 hours. Maybe a bit longer if we run into some setbacks along the way."
    show fe 91
    mc "That's good enough!"
    show fe 90
    if maximoalive:
        n "But we'll need to recruit a fresh crew. At least 3 more members, especially since Maximo is leaving once we reach Tortuga."
    else:
        n "But we'll need to recruit a fresh crew. At least 3 more members."
    show fe 91
    mc "I see..."
    play sound woodhit
    mc "*Kicking the floor* ALRIGHT!" with vpunch 
    mc "Here's the new plan: we head back to Tortuga, split up across town, and drop a few signs announcing our need for emergency sailors. Big reward, of course!"
    mc "After that, we log off, grab a quick bite, toilet, and then dive back in! 15 minutes max!"
    play sound6 seagull
    mc "We gather our new sailors, set sail on this new adventure, and we bag that treasure before tomorrow's sunrise!"
    mc "Sounds good?!"
    if novapath:
        show fe 92
        no "Oh..." with dis12
        no "So we have to log back in that quickly?"
        show fe 93
        mc "Of course! This is a BIG opportunity!"
        mc "We can't afford to let it slip away! Every Gem gets us closer to our ultimate goal!"
        show fe 92
        no "Oh..."
        no "I mean... yeah, you’re right."
        show fe 93
        mc "You okay, Nova?"
        mc "Is anything wrong?"
        show fe 92
        no "No... no. Of course not."
        show fe 94
        no "Alright, let's head back to Tortuga ASAP then!" with dis
        no "Full-speed ahead!"
        mc "That's the spirit!"
    else:
        show fe 89
        no "Sounds good to me!"
        n "Solid plan!"
        show fe 91
        mc "To Tortuga it is, then!"
    play sound3 wood2
    scene fe 95
    mc "*Leaning on the rail* Here we go..." with dis15
    mct "It's weird. For some reason, I got all fired up when El Coyote proved to be a real challenge. Am I getting addicted to adrenaline or what?"
    mct "Mmh, well, in any case, living a real pirate adventure sounds so damn exciting!"
    if novapath:
        play sound piratescaribbean
        play sound2 piratescaribbean fadein 2
        stop music fadeout 10
        play sound7 woodhit
        mc "Man, I haven't been this pumped in a while!{w=1.8}{nw}"with vpunch 
        mc "*Looking at the horizon* This Gem of Doom will be ours...{w=1.7}{nw}" 
        play sound7 woodhit
        mc "{sc=2}COME ON EVERYONE ! ! !{/sc}{w=1.1}{nw}"with vpunch 
        play sound7 woodhit
        mc "{sc=2}FULL SP–{/sc}{w=0.7}{nw}"with vpunch
        stop music
        play sound slap1
        play sound2 slap3
        play sound3 fist
        scene fe 96
        mc "Ouch." with hpunch 
        play music pirate1 fadein 6
        play sound7 wood2
        scene fe 97 
        mc "W-What was that for? What did I do now?!" with dis12
        show fe 98
        n "How can you be so dense?!"
        show fe 97
        mc "What??"
        show fe 98
        n "Didn't you notice how crushed Nova looked when you dropped the new plan bomb?"
        show fe 97
        mc "Did she...?"
        show fe 98
        n "Didn't you guys already have plans?"
        show fe 97
        mc "I mean... yeah, we did, but we can't pass up on this! The third Gem of Doom is right there for us to take!"
        show fe 98
        n "It's not about changing plans, it's about the way you said it."
        n "You made it seem like you didn't give a damn."
        show fe 97
        mc "What?! That's not true!"
        mct "Did I really come off that way?"
        play sound6 seagull
        mct "Shit, I'm bummed about delaying our anime-binging date too, but maybe Nancy has a point. I could've been more considerate in breaking the news."
        mct "Especially knowing how much Nova had been looking forward to today."
        mc "Okay, now I feel bad."
        show fe 98
        n "With good reason."
        show fe 97
        mc "Maybe... we don't have to rush so much."
        mc "Would it be alright if we take a bit more time before logging back in?"
        mc "I'd really like to have a leisurely lunch with Nova and maybe catch an episode or two of something."
        show fe 99
        n "Now, that's better."with dis
        n "See how it's not that hard?"
        n "Nova is a sensitive soul – you've got to be mindful of that."
        show fe 100
        mc "I guess you're right."
        show fe 99
        n "I'm sure she'll love that... “readjustment” of the plan."
        n "And to answer your question, yes, we've got plenty of time, so no worries."
        play sound6 seagull
        n "How about we reconvene in, let's say... 3 hours? Back in Tortuga?"
        show fe 100
        mc "Perfect!"
        show fe 99
        n "Just make sure you both savor a good meal..."
        n "After this little break, we won't be able to log off until we lay our hands on that treasure!"
        show fe 100
        mc "Gotcha! We will!"
        mc "Thanks Nancy."
        show fe 99
        n "You can thank me later..."
        n "Now, go on, you can continue yelling at the ocean until we arrive."
        show fe 100
        mc "*Laughs* Thanks, I appreciate it."
    else:
        mc "*Looking at the horizon* (This Gem of Doom will be ours...)"

label tortugaprebreak:
    play sound wave
    stop music fadeout 7
    stop soundloop fadeout 11
    scene black with dis22
    play sound2 seagull
    show screen afewminuteslater with dis2
    play soundloop2 waves fadein 6
    pause  
    play sound3 seagull2
    play sound5 ["<silence 1.6>", church2] volume 0.4 
    play sound6 ["<silence 1.6>", seagull] volume 0.8
    scene fd 1  
    hide screen afewminuteslater
    with dis25
    pause 
    mct "Ahh... Tortuga."with dis
    mct "The Mecca of piracy."
    mct "Booze, gambling, disreputable women, and shady grog houses with poor sanitation. The perfect haven for any despicable pirate chasing some fortune!"
    play sound whoosh6
    play music sneaky5 
    play sound2 seagull
    scene fd0
    mct "Too bad we don't have time to enjoy this picturesque place." 
    scene fd 3
    mct "Or maybe... luckily."
    scene fd 2
    mct "For better or for worse, we've gotta keep moving."
    mct "I should go to the tavern and ask for..."
    show fd 3
    mct "Gypsy Goldtooth, was it?"
    scene fd 2
    mct "Without that map, we're not going anywhere."
    play sound footsteps3
    scene fd 4 with dis22
    mct "The Last Resort Tavern. And Shop. It should be here." with dis
    mct "I hope I can locate him quickly, Nancy and Nova will likely have all the crew members recruited in no time."
    mct "Let's do this!"
    play sound saloondoors
    stop soundloop2 fadeout 2
    stop music fadeout 2
    play musicb piratetavern fadein 3
    scene fd 5 with dis2
    bla "You confidently step into the quaint, crowded tavern, enveloped in the comforting scent of aged wood, liquor, and lingering smoke." with dis
    mct "Huh, not bad."
    mct "This place has a cozier vibe than I thought it would."
    show fd 6 with dis12
    mct "Damn, are those the bones of a real mermaid?"with dis
    mct "That's pretty cool."
    mct "I wonder what other weird stuff lurks in that ocean..."
    tav "Can I help you?"
    show fd 8
    mc "*Turning around* Hmm?" with dis
    mc "Oh, hi there. Are you the one running this joint?"
    show fd 7
    tav "For the next couple of hours or so until I clock out, yes, I am."
    tav "What do you need?"
    show fd 8
    mc "You see, I'm on the lookout for some new crew members for a quick but crucial trip overseas."
    mc "Is there anyone here interested in a gig like that? BIG reward."
    show fd 9
    tav "HAH!"with dis
    show fd 11
    tav "Big reward, you said? Who isn't looking for a job like that around here?" with dis
    tav "Almost everyone in this server is chasing that paper, boy."
    tav "If you've got the coin, you'll find folks here ready to jump on your ship."
    show fd 10
    mc "Excellent then!"
    mc "Mind spreading the word around?"
    mc "I'm gonna be back in about... 3 hours."
    show fd 11
    tav "Sure thing. I'll let these bastards know."
    show fd 7 
    tav "Huh, it would actually be doing me a solid if you could take some of the ones who are broke as a joke!"
    show fd 8
    mc "*Chuckles* I bet."
    show fd 7
    tav "You'll probably have a crew of the less fortunate ready to roll by the time you're back."
    show fd 8
    mc "Sounds good to me."
    show fd 7
    tav "So... anything else?"
    show fd 8
    mc "Yes, actually. I'm looking for Gypsy Goldtooth."
    mc "I heard he hangs around here. Any idea where I can find him?"
    show fd 7
    tav "Oh... sure, he's got the place next to the tavern rented. I can send someone to let him know you're looking for him."
    show fd 8
    mc "That would be perfect. Thank you for all your help."
    show fd 7
    tav "Although... what's the deal with him? If you're planning to kick up a fuss, do it outside my tavern."
    show fd 8
    mc "No worries, nothing like that. He's just got a map I need."
    show fd 7
    tav "A map to... where exactly?"
    show fd 8
    mc "The Island of the Lost Souls."
    show fd 9
    tav "Hahahahahaha!" with dis
    show fd 10
    mc "What's so funny...?"with dis 
    show fd 11
    tav "Is that why you're recruiting crew members? To sail to the Island of the Lost Souls?"
    tav "That might thin out the applicant pool, you know."
    show fd 10
    mc "What? Why?"
    show fd 11
    tav "It isn't called “The Island of the Lost Souls” because it's full of Golden Retrievers and hammocks for sunbathing, boy."
    tav "I've seen countless ships head there for the Heart of the Abyss, and not a single one has ever come back."
    tav "Sailing there is basically a one-way ticket to the afterlife."
    show fd 10
    mc "Well, none of them were me."
    show fd 9
    tav "Hahahahahaha!" with dis
    show fd 11
    tav "*Laughs* I like your spirit."with dis
    tav "I'll raise a glass to your health when the ocean spits out the remains of your ship on Tortuga's shores."
    show fd 10
    mc "Thanks for the motivation..."
    show fd 11
    tav "Anyway, grab a seat."
    tav "Goldtooth will be here in a minute."
    show fd 10
    mc "Thanks."
    play sound2 chairmove
    play sound ["<silence 0.5>", chair2]
    scene fd 12 with dis14
    mc "*Sitting down* (Jeez, he made it sound like it's a death sentence.)" with dis
    mct "Now it's starting to make sense why El Coyote is willing to trade this Heart of the Abyss for a Gem of Doom."
    mct "The remains of our ship on Tortuga's shore... this guy doesn't know who he's talking to."
    show fd 13
    pi1 "I'm telling you, that server is in complete chaos." with dis
    mc "Hmm?"
    show fd 14
    pi1 "I even heard Ulysses might tighten access soon."
    show fd 16
    pi2 "Andromeda? Is it really that bad?"
    show fd 15
    pi3 "Yeah, my wife's friend and her entire family got murdered in Zyrion-3 the other day when the horde attacked a combat-free zone."
    pi3 "Those aliens are going way out of control."
    show fd 14
    pi1 "The Xenomorphs are like a plague."
    pi1 "They're spreading like a virus, wiping out everything in their path."
    show fd 16
    pi2 "I heard a rumor that the Chinese cooked them up to mess with Ulysses' monopoly."
    play sound tablehit
    show fd 14
    pi1 "OF COURSE THEY DID!" with vpunch
    pi1 "And yet, ain't nobody doing a damn thing to stop it!"
    show fd 15
    if freemercer:
        pi3 "They say Doctor Mercer is diving into researching them. She set up a hospital for the infected and claims she'll put an end to the plague."
        pi3 "Word is, she's even planning to use them to develop a regeneration serum in the real world."
        show fd 14
        pi1 "That sounds like some sketchy shit, though – you won't see me volunteering."
        pi1 "I've watched enough apocalypse movies that kick off exactly like that."
    else:
        pi3 "They say Commander Hasler is on a mission to wipe them out."
        pi3 "He took over as the new leader of the Galactic Union, and the word is, they've already taken down thousands of those disgusting creatures."
        show fd 14
        pi1 "Eh, I’d steer clear of him, though. His methods are... questionable."
        pi1 "Rumor has it, he shoots anyone suspected of being infected everywhere he goes, like a full-on witch hunt."
    show fd 18
    if anniepath:
        mct "Hmm... seems like the things I went through with Annie were just the tip of the iceberg."
    else:
        mct "A plague in Andromeda...? Maybe it's best to steer clear of that server for now."
    show fd 17
    pi2 "Huh, and that's not even the worst of it! Have you heard about the rogue NPCs in Ekabar?"
    pi2 "They're straight-up murdering real players!"
    pi2 "And I'm not talking about monsters, I mean regular farmers and villagers!"
    show fd 14
    pi1 "Man, Eternum's really going to shit..."
    pi1 "All these fucking kids are ruining it!"
    show fd 15
    pi3 "It's those damn hackers, I tell ya. Fucking up everything with their boosted weapons."
    pi3 "Nobody gives a shit about roleplaying anymore, it's all about who's packing the biggest damn gun."
    play sound tablehit
    show fd 16
    pi2 "MAKE ETERNUM GREAT AGAIN!" with vpunch 
    pi2 "We need a new CEO! The Founder's an old fart who doesn't even know or care about what's going down in his own game."
    show fd 14
    pi1 "Yeah, you're right... we need someone else to get the Gems of Doom pronto and kick that dude out of his fancy golden chair."
    show fd 15
    pi3 "But Thanatos is dragging his feet."
    pi3 "How many Gems does he have again? 4 or 5?"
    show fd 16
    pi2 "Oh, and what about that new guy working with the WRE?"
    pi2 "People are saying he's a real powerhouse."
    play sound2 wood2
    mc "*Leaning towards the three men's table* Hmmmm...?"
    show fd 14
    pi1 "Oh yeah, I've heard about him... people say he has two or three Gems of Doom."
    pi1 "But ain't he just a kid?"
    show fd 16
    pi2 "I don't know, kid or not, he's got some balls."
    if rotundafail:
        pi2 "There’s a rumor he almost defeated Jasticus the Decapitator in the Rotunda."
        mct "Damn you, Jasticus..."
    else:    
        pi2 "There’s a rumor he knocked down Jasticus the Decapitator in the Rotunda with just one hit."
        mct "Yep, that was me."
    show fd 15
    pi3 "Yeah, and they also say he swiped Wagner's Gem even before Thanatos rolled in and wiped the entire server out."
    mct "He didn't even see it coming."
    show fd 16
    pi2 "And wasn't he the one who won this year's Triwizard Tournament at Warthogs?"
    if grimoirerest or grimoiredest:
        mct "You bet I did."
    else:
        mct "Eh... well, technically not, but... almost."
    show fd 14
    pi1 "Think he's got a shot against Thanatos?"
    show fd 16
    pi2 "Well, folks who've seen him scrap swear he moves like a damn shadow and hits like a bullet to the gut."
    mct "Heh, you got that right, old man."
    show fd 19
    pi2 "There's not much info about who he really is, not even his name, but..." with dis12
    pi2 "People call him..."
    play sound deception
    play sound2 deception
    pi2 "The Zigzagopopolis." with dis
    play sound slam
    play sound2 fallbottle
    show fd 20
    mc "*Standing up* WHAT?!" with vpunch 
    pi1 ". . ."
    if nickname == __("Zigzagopopolis") or nickname == __("The Zigzagopopolis"):
        mct "Oh wait... it {i}is{/i} The Zigzagopopolis."
        mct "Why the fuck did I choose such a stupid name...?"
        mct "Was I drunk that day?"
    else:
        mc "*Clears throat* I-I mean..."
        mc "I'm pretty sure people call him... [nickname]."
        show fd 21
        pi2 "Ohh... yeah, now that you mention it, that's the name I heard." with dis
        pi2 "My bad, got it mixed up with a show my grandson watches."
    show fd 23
    pi1 "Do you know [nickname], kid?"with dis
    pi1 "You seem pretty worked up about him."
    show fd 22
    mc "Well... I've heard the stories too. You could say I'm a... fan."
    mc "People say he's near invincible."
    mc "That he could take down Thanatos if they ever faced off again."
    show fd 23
    pi1 "Again?"
    pi1 "They've already fought?"
    show fd 22
    mc "They have, actually."
    mc "Thanatos snagged the win, but it was back when he was still a greenhorn. He won't go down like that again."
    mc "Or... *clears throat* yeah, so they say."
    mc "Anyway, I better go outside now. I need to find Gypsy Goldtooth."
    mc "Sorry to bother you, gentlemen."
    show fd 24
    pi1 "Ugh, I can't stand that guy."
    show fd 22
    mc "Goldtooth?"
    show fd 23
    pi1 "Yeah, watch yourself with him. He's gonna peddle a load of crap, and only like 1 in 10 items actually works."
    pi1 "So you gotta either be real damn lucky or real smart."
    show fd 22
    mc "*Chuckles* Yeah, I've run into sellers like him before."
    mc "I once–"
    mc "Hold on..."
    mc "How often does he show up around here?"
    show fd 23
    pi1 "Um... not much."
    pi1 "I think he's got other joints in other servers."
    show fd 22
    mc "Oh no."
    show fd 23
    pi1 "Sometimes his assistant swings by too."
    show fd 22
    mc "OH NO."
    show fd 23
    pi1 "What?"
    show fd 22
    mc "Please, for the love of everything, tell me Gypsy Goldtooth isn't a tanned, five-foot-one Asian with poor English."
    show fd 24
    pi1 "Eh..."
    play sound slam
    play sound2 doorwoodclose
    stop musicb
    play music ["<silence 1>"]
    queue music pirate2 fadein 6
    scene fd25
    chop "{sc=2}OOOOOOOOOOOOOOOOOHHHHHH!!!!!{/sc}" with hpunchlong4 
    chop "{sc=2}WELCOME BACK BESTEST FRIEND [mc!u]!!!{/sc}"
    scene fd 26 with dis15
    mc "I must be dreaming..."with dis
    show fd 27
    chop "No wet dream here, only best prices!"
    chop "Only best quality!"
    chop "In case you no know, this best shop in all New World!"
    chop "No, no, all ETERNUM!" with hpunch
    chop "{sc=2}CHA-CHING BEST BLING KACHOWWWW!!!!{/sc}" with hpunch
    show fd 26
    mc "Over 40 million simultaneous online users in a limitless world, and yet, it's the fourth time we’ve “accidentally” bumped into each other in some random spot!"
    mc "How convenient, huh??"
    show fd 27
    chop "What can me say, fate lead best client [mc] to most esteemed seller in Eternum!"
    chop "I am destiny!"
    show fd 26
    mc "Of course..."
    show fd 26b
    chop "OOOOOOHH... I see someone visiting barber and hitting big-boy gym since last time I gave you best sale! My my my!"
    show fd 26
    mc "Um... thank you. In case that was a compliment."
    play sound whoosh3b
    show fd28
    we "*Gasps* Oh, it's [mc]!" with hpunch 
    we "Good to see you back!"
    scene fd 29
    mc "Oh, hey Wenlin!"
    mc "Almost didn't recognize you without your little fairy look."
    mc "Still tagging along with this crazy old man, huh?"
    show fd 28
    we "Absolutely!"
    we "Gotta stick to the sensei's path."
    we "No riches for those who slack!"
    play sound slam
    play sound2 tablehit
    play sound3 fallbottle
    scene fd 30
    pi1 "HEY, THERE YOU ARE!" with vpunch 
    pi1 "Those enlargement pills you sold me enlarged the wrong thing, Chop-Chop!"
    pi1 "I want a refund!"
    show fd 31
    chop "*Whispering* Uh-oh, little weenie man is back. Cannot have him scare best client [mc]."
    show fd 32
    we "*Whispering* Do you want me to handle it?"
    show fd 31
    chop "*Whispering* No, no, your tongue is not sharp enough yet, young niece Wenlin."
    chop "*Whispering* I lay down law with tiny meat-man, you go with best client [mc] to balcony and start business."
    chop "*Whispering* I be back in minute."
    show fd 32
    we "*Whispering* Gotcha."
    show fd 34 with dis14
    chop "OOOOOOOOOOOHOHOHO best client Pete welcome back! You know you are number 1 client of Chop-Chop?!"with dis08
    pi1 "Cut the crap!"with hpunch 
    show fd 33
    we "Please, come with me, [mc]!"
    show fd 34
    mc "*Chuckles* Gypsy Goldtooth, really?"
    show fd 33
    we "Indeed!"
    we "He goes by different names depending on where we're selling our products."
    we "In The New World server, he's Gypsy Goldtooth; in Meiyo, he's Bonsai Shearer, and in Andromeda, he's Quantum Quasar Starlord!"
    show fd 34
    mc "Oh god, thanks for the warning... I'll try to remember those names."
    show fd 33
    we "Please, follow me!"
    we "Let's get down to business!"
    show fd 34
    mc "Um... well, alright, I guess I have 5 minutes. But not more than that."
    mc "Lead the way."
    play sound7 saloondoors fadein 1
    play soundloop waves fadein 6 volume 0.8
    scene fd 35 with dis2
    play sound seagull
    bla "You trail behind Wenlin as she leads the way to the balcony on the second floor of the bustling tavern." with dis12
    we "Give me a sec! I'll go get the merchandise ready!"
    mc "S-Seriously though, there's no need!"
    mc "I've got a shopping list as short as my attention span!"
    play sound saloondoors
    scene fd 37
    we "Okay, ready!" with dis
    we "What's on your shopping list today?!"
    show fd 36
    mc "Just one thing."
    mc "You see, I need to reach the Island of the Lost S–"
    show fd 37
    we "Rum barrels, 50%% off just today!"
    show fd 36
    mc "Really, I just–"
    show fd 37
    we "We've also got mimic chests, sunscreen that turns you invisible, and fire swords that are all sizzle, no burn!"
    show fd 36
    mc "*Sighs* I don't–"
    mc "Is that why your palm is all red...?"
    play sound saloondoors
    play sound2 whoosh6
    play sound3 crashwood volume 0.3
    play sound4 seagull
    scene fd38
    chop "*Jumping in* I'M BACK!" with hpunch
    chop "YOU MISS ME AS MUCH AS I MISS YOU?? HAH! Trick question. IMPOSSIBLE! No one miss [mc] as much as Chop-Chop miss [mc]!"
    scene fd 39
    mc "Oh no, what's all that shit you're carrying..."
    scene fd 38
    chop "Now listen me here, I have bestest product saved SPECIALLY for you! Top customer! You find nothing like this anywhere else!"
    scene fd 39
    mc "Okay guys, I appreciate the enthusiasm, but today I only need one thing."
    show fd 38
    chop "BEHOLD! Scimitar of Destiny, wielded by Blackbeard himself!"
    chop "Not like butter knife from other sellers – this here REAL DEAL!"
    show fd 39
    mc "Please, I'm in a rush. I just need a map to–"
    show fd 38
    chop "Magic jam of pig princess from distant kingdom! Moist and juicy, can feed even most fat white woman for weeks!"
    show fd 39
    mc "Are you even listening to me?!"
    show fd 38
    chop "Oh, need new companion?! Shoulder parrot Maurice is best–"
    play sound woodhit
    play sound2 impactwood
    play sound3 musicstop
    play sound4 seagull
    play sound5 fallbottle
    play sound6 bird_flying
    stop music
    scene fd 40
    mc "{sc=2}{b}ENOUGH!!!!{/sc}" with vpunch  
    mc "I was told to come here to get a map to the Island of the Lost Souls!"with hpunch
    mc "I'm on a quest for The Heart of the Abyss, and I need to get to that island before tomorrow's sunrise!"with hpunch
    mc "I don't want princess jam, I don't want weird, giant penis-looking creatures, and I don't want any other fucking pieces of junk!"with hpunch
    mc "So, do you have the map or not?!"with hpunch
    we ". . ."(multiple=2)
    chop ". . ."(multiple=2)
    mc "And that's not even a parrot, it's a pigeon!"
    we ". . ."(multiple=2)
    chop ". . ."(multiple=2)
    mc ". . ."
    mc "Um..."
    mc "S-Sorry, I didn't mean to shout. Got a little carried away."
    play music pirate1 fadein 6
    show fd 41
    chop "See, little niece Wenlin? [mc] mad because I neglect him for too long and he starving from lack of good product!" with dis14
    chop "Lucky for him, he can never stray too far from Chop-Chop's loving embrace! And we have map JUST for him!"
    show fd 42
    we "Yeah, we've been selling those like hotcakes this month, actually!"
    we "A lot of people wanted to get the Heart of the Abyss."
    show fd 41
    chop "[mc] is VIP customer, so we gotta show him only the most trending products!"
    chop "I come back quick with something he'll really like!"
    show fd 42
    we "And I'll hand him the map in the meantime!"
    play sound saloondoors fadein 1
    play sound2 noise1 volume 0.77
    show fd 42b
    bla "Chop-Chop disappears through the balcony doors as Wenlin frantically starts rummaging behind the barrels."with dis15
    play sound2 noise1 volume 0.77
    we "Alright, let me figure out where we stashed those..."
    we "I hope we didn't sell 'em all... isn't today the last shot at that island thing?"
    mc "Yeah, that's why I'm in a hurry."
    play sound3 noise1 volume 0.77
    we "Ah! That makes sense... Aha! Found it!"
    play sound4 paper3
    play sound5 paper3
    show fd 43
    we "*Unrolling the scroll* You're lucky, it was the last one!" with dis
    we "And because you're in the VIP club, I'll cut you a deal – this one's on the house!"
    we "You can also consider this a little apology for taking up your precious time."
    show fd 44
    mc "Oh, really? Thanks a bunch!"
    show fd 43
    we "That said... do you need a quick rundown on how to hit up the Island of the Lost Souls?"
    we "Special insider info for just 50 eternals!"
    show fd 44
    mc "Insider info, uh...?"
    menu:
        with dis
        "Accept":
            mc "Seems fair, alright."with dis06
            show screen eternals
            with dis08
            play sound coins
            $ money -= 17
            pause .05
            $ money -= 17
            pause .05
            $ money -= 16
            pause .4
            hide screen eternals 
            mc "Done." with dis06
            show fd501
        "[gr]Just the map":
            mc "Thank you, but I'll stick with just the map."with dis06
            scene fd 45
            we "Ohhh... a hard-nosed negotiator, huh...?"
            we "Okay, okay... you win!"
            we "Let's call it a deal at 20 eternals, yes?"
            show fd 46
            menu:
                with dis
                "Accept":
                    mc "Now that sounds better."with dis06
                    show screen eternals
                    with dis08
                    play sound coins
                    $ money -= 7
                    pause .05
                    $ money -= 7
                    pause .05
                    $ money -= 6
                    pause .4
                    hide screen eternals 
                    mc "Done." with dis06
                    show fd502
                "[gr]Just the map (Insist)":
                    mc "Seriously, I appreciate it, but the map is all I need."with dis06
                    we ". . ."
                    play sound7 paper3
                    scene fd 47
                    we "*Mumbling* Agh! You're such a penny-pincher!" with dis 
                    we "FINE, 10 ETERNALS!"
                    we "I can't go any lower or Chop-Chop will straight-up give me the boot."
                    show fd 48
                    menu:
                        with dis
                        "[gr]Accept":
                            mc "Now that sounds better."with dis06
                            $ moneypincher = True
                            show screen eternals
                            with dis08
                            play sound coins
                            $ money -= 3
                            pause .05
                            $ money -= 3
                            pause .05
                            $ money -= 4
                            pause .4
                            hide screen eternals 
                            mc "Done." with dis06
                            show fd502
                        "Just the map (Insist again)":
                            $ wenlinsupport = False
                            mc "Just. The. Map."with dis06
                            we ". . ."
                            scene fd 47
                            we "I hate you."
                            we "Take the fucking map and get out of here."
                            show fd 48
                            mc "THANK YOU! That's exactly what I've been trying to do this whole time!"
                            we "Mmph."
                            play sound6 paper3
                            play soundlow wood2
                            show fd 49 with dis12
                            mc "*Unrolling the scroll* (Alright, let's see what we've got here...)" with dis
                            mc "Hmmm... "
                            mct "We have to go through the Icebergs of Frostbone... Siren's Cove... the Bay of the Undead... and then tackle the Paradox Archipelago."
                            mct "Damn, seems like it won't be as smooth sailing as I hoped."       
                            mct "But at least now we know where to go." 
                            play sound saloondoors fadein 1
                            play sound2 saloondoors fadein 1
                            show fd 54
                            chop "Ah, you found your map I see!" with dis12
                            show fd 55
                            mc "Yep! And that was ALL I needed!"
                            jump poswenlin                  
    play sound whoosh3b
    play sound4 seagull2
    play sound2 whoosh6
    play sound3 fist
    stop music fadeout 1
    play musicb pirate3 volume 0.5
    if moneypincher:
        we "*Passing you the map* Excellent! Now pay attention and take note, you bloody penny-pincher."with hpunch
    else:
        we "*Passing you the map* Excellent! Now pay attention and take note!"with hpunch
    we "Do you see this island in the top left corner?"
    play sound paper3
    play sound2 whoosh6
    play sound3 fist
    show pm1
    we "*Pointing at the map* Here?" with hpunch
    mc "I do." 
    we "That's Tortuga."
    we "*Clears throat* Now, if you want to snag that treasure in one piece, you better pay attention now!"
    we "It's not as easy as just sailing in a straight line."
    mc "I'm all ears."
    play sound wind2 fadein 2
    scene fd 50
    show pm2
    we "First, you set sail south until you spot the colossal Icebergs of Frostbone."
    mc "Gotcha."
    mct "I better tell the girls to grab some warm clothes."
    play sound2 whale
    play sound7 whale
    scene fd 50
    show pm3
    we "Next, veer east for a good 40 miles, steering clear of the killer whale that patrols those waters!"
    we "Watch out, that sea giant ain't too keen on ships invading his turf!"
    mc "Avoid the killer whale, noted."
    play sound3 mermaid 
    scene pm4
    we "Then, head north until you're skirting the coast of Siren's Cove... but be on your toes!"
    we "That's mermaid territory! Hope you can resist the siren song and not end up spellbound by their melody..."
    mc "Yeah..."
    mct "It'll probably be easier if I ask them to tie me to the mast."
    stop sound3 fadeout 3
    play sound4 thunder volume 0.6
    play sound5 evillaugh
    scene pm5
    we "After that, catch Serenity's Current to turbocharge your ship until you hit the Bay of the Undead."
    mc "That doesn't sound good..."
    we "It isn't!"
    we "Better watch your step there, unless you fancy spending eternity swabbing decks on Davy Jones' ship..."
    scene pm6
    we "And last but not least... go north again to enter the Paradox Archipelago!"
    we "Sailors have practically gone bonkers trying to navigate its intricate waters!"
    we "Watch out, not everything is as straightforward as it seems..."
    play sound2 whoosh6
    scene pm6b
    we "Some of them have even claimed to appear back in Tortuga somehow!"
    mc "Oh... we don't want that."
    play sound whoosh6
    scene pm6b2
    we "Definitely not!"
    play sound3 thunder fadein 2
    scene fd 50
    show pm7
    we "So, if by some miracle, you navigate all these perils and come out in one piece... you'll finally see it!"
    we "The Island of the Lost Souls!"
    we "And the Heart of the Abyss right there for you to take it!"
    we "Congrats, you made it!"
    we "Easy peasy!"
    play sound3 whoosh6
    play sound7 kraken
    play sound6 kraken
    scene fd 50
    show pm8
    mc "W-Wait, and what about this sketch of a fucking massive crab-like monster?"
    we "Oh."
    we "Yes. The Kraken. Hehe, almost slipped my mind, sorry."
    we "You better watch out, he's always on high alert to defend the Heart of the Abyss from trespassers!"
    play sound swallow
    play sound2 swallow
    mc "*Gulps* Ah, of course."
    mc "Sounds... like a stroll in the park."
    play sound4 paper2
    play sound5 paper2
    scene fd 51
    we "And that's all!" with dis
    we "To set sail, point your ship south and dive into the adventure!"
    mc "Mm-hm..."
    play sound saloondoors fadein 1
    play sound2 saloondoors fadein 1
    show fd 54
    chop "Ah, nice explanation niece Wenlin, yes!" with dis12
    show fd 55
    mc "Okay! That was ALL I needed!"
label poswenlin:
    mc "So don't even try to sell me anything else!"
    mc "Maybe next time! Thank you and have a good one!"
    play sound whoosh6
    scene fd 53
    chop "WAIT!" with hpunch  
    chop "Before you leave, Chop-Chop save best for last!"
    show fd 52
    mc "What now?!"
    show fd 53
    chop "Chop-Chop always make wildest dreams come true!"
    chop "Polyjuice potion!" with hpunch 
    show fd 52
    mc "Eh...?"
    if doneemporium:
        mc "Oh shit, it's true! Last time you told me you were producing a new batch!"
        mc "I had almost forgotten about it."
    else:
        mc "Oh... okay, I gotta admit, that could come in handy."
    show fd 53
    chop "Can't be detected by fancy magic gadgets!"
    chop "Just drink and... BING BONG KABLOM! Instant change!"
    chop "Turn ugly hippopotamus wife into your kid's hot babysitter for only 1100 eternals the bottle!"
    show fd 52
    mc "1100 ETERNALS?!"
    show fd 42
    we "Remember it's an incredibly rare and pricey potion to concoct. The production cost alone is over 750 eternals." with dis 
    show fd 41
    chop "BUT, since [mc] is most tip-top, non-stop, big chungus VIP client, we can do special price! Don't tell anyone, but for you, only 999!"
    chop "Only today!"
    show fd 42
    we "You took the words right out of my mouth!"
    show fd 39
    mc "Hmmm..." with dis
    menu:
        with dis
        "[gr]Buy Polyjuice Potion":
            if money <= 998:
                mct "Do I even have enough moolah...?" with dis06
                mct "Goddammit, I don't."
                mc "Ehh... yeah, not today, sorry."
                mod "You can add money in Cheats, you should buy the potion."
            else:
                $ polyjuicebuy = True
                mct "An item this powerful is bound to come in handy someday, no doubt." with dis06
                mct "And who knows when I'll cross paths with Chop-Chop again. This might be my one shot."
                mc "This thing doesn't have an expiration date, right?"
                show fd 38
                chop "No need for the fridge, my friend! If it smell funky and looks chunky, that means it will work!"
                show fd 39
                mc "Hmph."
                mc "Alright, fine, hand me a bottle."
                show screen eternals
                with dis08
                play sound coins
                $ money -= 333
                pause .05
                $ money -= 333
                pause .05
                $ money -= 333
                pause .4
                hide screen eternals 
                show screen polyjuiceb
                mc "It better do what it says! Otherwise, I'll personally kill you!"with dis
        "Don't buy it":
            mc "Ehh... yeah, not today, sorry." with dis06
    if polyjuicebuy:
        scene fd 38
        chop "Excellent purchase, excellent!"
        chop "You won't regret, congratulation!"
        show fd 39
    else:
        mc "I've gotta save the cash for something else."
        mc "But stash one bottle away! I'll grab it next time, I promise."     
        show fd 38
        chop "Alrighty, we keep a potion for you in Chop-Chop's stash, just in case... ONLY because you best friend!"
        chop "Come back here when you have more JINGLE-JANGLE in pocket!"
        show fd 39
        mc "Thank you, I appreciate it."
    mct "I really do hope I don't regret this decision later."
    mc "Anyway, for real now, time for me to hit the road."
    if novapath:
        mct "Nova's probably wondering why I'm taking so damn long..."
    mc "Thanks for the map and take care!"
    scene fd 38
    chop "Thank you friend! Come back another day!"
    chop "You won't regret purchase, I promise!"
    chop "I even offer warranty on all purchases now! So come back if you have trouble!"
    chop "{size=20}Limited half hour warranty applicable to most purchases.{w=0.35}{nw}"
    chop "{size=20}Warranty does not cover any products that have been used, destroyed, touched, or looked at.{w=0.35}{nw}"
    chop "{size=20}To complete warranty claim, please fill-out 42 page form and submit to Once You Chop Chop, You Don’t Stop Inc. via carrier pigeon ONLY.{w=0.35}{nw}"
    chop "{size=20}Submitted claims will take between 52-69 weeks for processing and are subject to approval.{w=0.35}{nw}"
    chop "See ya!"with hpunch 
    scene fd 39
    mc "*Chuckles* Goodbye."
    stop music fadeout 8
    stop musicb fadeout 8
    scene fd 56 
    hide screen polyjuiceb
    with dis25
    play sound3 footsteps3
    play sound2 ["<silence 1.2>", seagull]
    bla "You leave the tavern and begin strolling back toward Tortuga's Exit Portal." with dis12
    mct "Oh god, why do I always leave Chop-Chop's with a headache...?"
    mct "I can still hear his ear-piercing voice in my head..."
    play sound saloondoors
    chop "GOODBYE FRIEND!" with hpunch
    show fd 57
    mc "*Turning around* Huh?" with dis12
    play sound5 seagull
    chop "MY HEART MISS YOU SO MUCH ALREADY!"
    we "Farewell, [mc]! Come back soon with lots of gold!"
    mc "*Waving* Haha okay, okay! I'll try my best!"
    mc "Goodbye, guys!"
    show fd 56
    mc "*Chuckles* (Those two are something else.)"with dis12
    we "Say hi to your hot girls from me!"
    we "And best of luck on your mission!"
    chop "Keep moving forward, [mc]!"
    play sound deception
    chop "That is the only way."
    mct "Okay, time to head back and–"
    mc ". . ."
    play sound2 seagull
    show fd 58
    mc "*Turning around* What did you just sa–" with dis
    mct "Oh... they already left."
    mct "For a moment, he didn't sound like the usual Chop-Chop."
    mct "I could swear I've heard that before..."
    show fd 56
    mct "Anyway, time to head back. I can't waste any more time." with dis12
    if novapath:
        mct "Still have to grab lunch with Nova, come back to Tortuga, assemble a new crew, and set sail for the Island of the Lost Souls."
    else:
        mct "Still have to grab lunch, come back, assemble a new crew, and set sail for the Island of the Lost Souls."
    mct "No time to waste!"
    stop soundloop fadeout 5
    play sound risingshort4
    scene login3 with dis22
    pause 5.8
    play soundlow whoosh4
    scene white with dissolve
    play soundloop rain3 fadein 5
    if not novapath:
        scene fe 5 with dis08
        play sound2 beep
        pause 
        play sound4 clothes3
        play sound5 stomach
        mc "*Sitting up* (Oh man, it's not until you log off that you realize how hungry you actually are...)" with dis
        mct "I'd KILL for a pizza."
        play sound thunder fadein 3
        scene fe 6
        mct "Mmh, but it's still raining." with dis15
        mct "Maybe it'd be quicker if I just grab them myself. The delivery guy's gonna take forever."
        mct "Hmm..."
        mct "Actually... if I cut through Chinatown for a shortcut, I can be back here in 30 minutes. Easy."
        mct "And I could grab one for Nancy as well."
        scene fe 5
        mct "Alright, sounds like a plan!" with dis12
        mct "I'll leave without telling her and surprise her with the pizza when I'm back."
        mct "What can I say, I'm a hopeless romantic..."
        jump ending07
    scene fc 1 with dis08
    play sound2 beep
    pause 
    play sound4 clothes3
    play sound5 stomach
    mc "*Sitting up* (Oh man, it's not until you log off that you realize how hungry you actually are...)" with dis12
    mct "I'd kill for those pizzas."
    play sound thunder
    scene fc11
    pause 1.4
    mct "Mmh, but it's still raining." with dis15
    scene fc 3
    mct "Maybe it'd be faster if I just go grab them myself. The delivery guy is gonna take forever." with dis 
    mct "Let's check with Nova, perhaps we could make it a joint adventure."
    scene fc 4
    san "Honey! I thought you'd be playing!" with dis
    mct "Oh, is her mom still here?"
    scene fc 5
    san "Nova?" with dis12
    no ". . ."
    san "Nova!"
    show fc 6
    no "Hmm...?" with dis
    show fc 8
    no "Oh, sorry, Mom." with dis
    no "Just got lost in my thoughts for a sec."
    show fc 7
    san "Aren't you wearing the Eternum suit?"
    san "I thought you were planning to play together."
    show fc 8
    no "Oh, yeah, we are."
    show fc 9
    no "I just took it off to grab a quick bite while we have a break."
    show fc 7
    san "Oh, I see!"
    san "Well, enjoy then, you two!"
    show fc 9
    no "Thanks, we will."
    show fc 8
    no "What about you, though?"
    no "Weren't you going out with Dad?"
    show fc 7
    san "Yeah, but your father forgot the tickets, so we had to come back."
    san "*Chuckles* I swear, he's becoming increasingly forgetful!"
    show fc 8
    no "Ah, I see."
    show fc 10
    san "Don't worry though, I'm heading out again now!"
    san "Have fun with [mc]!"
    show fc 9
    no "Okay, Mom."
    show fc 10
    san "*Whispering* And promise me you'll use protection if you... you know."
    show fc 9
    no "Yes, Mo–"
    play soundlow thunder fadein 4
    show fc 11
    no "Oh my god, c-can you stop with the awkward sex talk already??" with dis   
    no "I'm not 15 years old, you know?!"
    no "And didn't I tell you [mc] and I are just friends?!"
    no "Stop making it weird, for Christ's sake!"
    show fc 12
    san "Oh..."
    san "I'm sorry, sweetie, I didn't..."
    san "Did something happen?"
    show fc 14
    no "Nothing happened."
    show fc 12
    san "I just..."
    san "I thought you liked that boy, I'm sorry."
    show fc 14
    no "Who gives a shit about what I like or not."
    no "That's not... important. Never has been."
    no "I'm just..."
    no "I'm just the clumsy, quirky, ginger friend people call when they need something and then... forget about."
    show fc 13
    san ". . ."
    show fc 12
    san "Do you want me to stay?"
    san "I'll go tell your dad to cancel our plans."
    show fc 14
    no "No. Please, go."
    show fc 12
    san "Are you sure? It's no trouble, really."
    show fc 14
    no "Yes, I'm sure."
    no "We're logging back into Eternum in like 10 minutes anyway."
    no "We have something important to tackle there."
    show fc 13
    san ". . ."
    show fc 12
    san "Alright then..."
    san "We won't take long anyway, just a couple of hours at most."
    show fc 14
    no "Okay."
    show fc 13
    san ". . ."
    show fc 12
    san "Okay, take care, honey."
    san "I love you."
    show fc 14
    no "Love you too."
    play sound2 ["<silence 0.2>", keys]
    scene fc 15 with dis25
    play sound doorclose2
    bla "Nova waits and stays quiet until she finally hears her mom heading downstairs and leaving through the front door." with dis12
    show fc 16
    no "*Sighs* Agh..." with dis12
    no "I hate this weather."
    play sound3 dooropenclose fadein 1
    show fc 17
    bla "Nova steps into the guest bedroom, her gaze fixed on the floor." with dis12
    show fc 18 with dis08
    no "*Turning around* Oh s-shit!" with hpunch
    no "W-Why are you standing here like a psychopath?!"
    no "I thought you were still connected! You scared me!"
    mc "Sorry, I just logged off."
    show fc 19
    no "Anyway, listen, about that lunch..."with dis
    no "I know we were planning on pizza, but the delivery guy's gonna take a while because of the rain, and we gotta get back to The New World, like, now."
    no "So I thought we could just snag something from the fridge."
    no "Is that cool with you?"
    no "I've got some mac and cheese leftovers from yesterday and some tacos from Luna's cafe from... Thursday, I think?"
    no "Wednesday...?"
    menu:
        with dis
        "[gr]Prove to her you care about her":
            $ renpy.music.set_volume(0.8, channel='music3')
            play music3 novascene fadein 8
            stop soundloop fadeout 16
            play sound2 bodycollide
            play sound clotheswhoosh
            scene fc20
            bla "You swiftly grab Nova's waist and draw her in, your touch sparking a rapid blush across her cheeks almost immediately." with hpunch
        "I'm craving for pizza":
            scene fcc 1
            no "Or... maybe Tuesday." with dis15
            scene fcc 2
            mc "Um..." 
            mct "It's probably best if I don't mention that I overheard her chat with her mom."
            mct "I'd come off as nosy, and she'd be embarrassed."
            mc "Uh... I'm honestly craving pizza."
            scene fcc 1
            no "Oh..."
            no "Fair enough."
            show fcc 2
            mc "But I don't mind running out to get it myself!"
            mc "A little rain won't stop me."
            mc "I'll cut through Chinatown for a shortcut. I can be back here in... 20 minutes."
            show fcc 1
            no "Oh well, in that case... sure, okay then."
            no "I'll take a quick shower while you're out, so we can hop on Eternum faster later."
            show fcc 2
            mc "Sounds good!"
            show fcc 1
            no "Just make sure you grab an umbrella."
            show fcc 2
            mc "I will!"
            mc "What kind of pizza do you want?"
            show fcc 3
            no "Anything's fine." with dis12
            no "Just... thick crust. If possible."
            no "And thank you for going!"
            mc "No problem!"
            play sound ["<silence 0.6>", doorclose] 
            show fcc 4 with dis17
            mct "Hmm, maybe it's just my imagination, but she sounds a bit down."with dis12
            mct "I should plan another anime date next week to make it up to her."
            mct "If she's still up for it, that is."
            mct "You never know with women..."
            mct "But anyway, let's go grab the food!"
            mct "I wonder if I can polish off a whole extra-large pizza by myself..."
            $ novapath = False
            $ novau = False
            jump ending07
    scene fc 21
    no "W-What's going on with you now...?" 
    show fc 22
    no "We really have no time to waste..."
    show fc 20
    mc "No, we don't."
    mc "And that's precisely why I want to dedicate the next few hours entirely to you, Nova."
    show fc 22
    no "We need to get that treasure for El Coyote."
    show fc 20
    mc "We have time."
    mc "Actually... even if we didn't, I don't give a fuck."
    mc "Right now, you're the only thing on my mind, Nova. The only one deserving of attention."
    mc "I'm sorry I haven't shown you enough how much you really mean to me."
    show fc 21
    no "W-What's gotten into you all of a sudden?"
    show fc 20
    mc "Today was our date. Everything else can wait."
    no "Mmh...?"
    mc "I just want to prove to you that you're much more than my clumsy, quirky, ginger friend."
    show fc 22
    no "Ohh... y-you heard that."
    no "Um..."
    no "T-This is a bit embarrassing."
    no "What I meant is that I–"
    play sound bodycollide
    scene fc 23
    bla "You gently tug Nova closer, making your lips meet in a tender kiss." with dis06
    no ". . ."
    no "Mmh?"
    play sound2 clothes3
    play sound7 beat
    show screen heartbeat
    $ nova_points += 1
    scene fc 24
    bla "After a brief moment of hesitation, Nova leans into you and reciprocates the kiss with an energetic passion that lingers for several seconds." with dis12
    no "{bt=3}*Moaning* MMMmmmmmmmh...{/bt}"
    mct "Damn, her soft, fleshy lips feel like pure magic... I could kiss her for hours without getting tired."
    no "MMMMmmmm..."
    play sound3 chair1
    play sound4 couch
    scene fc 25
    no "*Breaking away from the kiss and easing onto the bed* W-Wow."with dis12
    no "W-Where did that come from...?"
    show fc 27
    mc "Just something we should've done a long time ago."
    mc "I mean, can you believe this was actually our first kiss?"
    mc "After {i}everything{/i} we've done together?"
    show fc 26
    no "Was it...? Are you sure?"
    no "N-Never really thought about it, but... now that you mention it..."
    show fc 27
    mc "*Chuckles* Come on, stop! We've moved past that already!"
    mc "You {i}definitely{/i} know that was our first kiss."
    show fc 25
    no "*Giggles* Okay, okay..."
    no "I know it was."
    no "And... it felt... as perfect as I had hoped."
    show fc 27
    mc "I felt the same way."
    show fc 25
    no "I-I'm glad."
    show fc 27
    mc "Tell me then, is there anything else you've been hoping for...?"
    show fc 25
    no "Well... if we actually do have some time to spare before going back to The New World..."
    no "W-We could... cuddle for a bit."
    no "Maybe kiss a little bit more..."
    show fc 27
    mc "Ah, I couldn't have thought of a better idea myself."
    mc "Do you mind if I take off the E-suit?"
    show fc 25
    no "Not at all."
    play sound rubclotheslong
    play sound2 clothes4
    play sound7 clothes3
    scene fc 28
    bla "You take off the top part of the E-suit as Nova gives you a surreptitious once-over, a playful smirk gracing her lips." with Dissolve(1.9)
    mct "Man, I'm already hard as a rock and she’s barely touched me."
    mct "And her sexy look isn't making it any easier..."
    play sound3 clothes3
    scene fc 29 with dis15
    mc "*Lifting her head* Fuck... I want you so bad, Nova." with dis
    mc "I want us to be way more than friends."
    mc "And I think we've danced around it long enough... don't you think?"
    no "Mm-hm..."
    if novadildo and novacrimelewd:
        mc "There’s no pretense this time. No external interferences. No crazy chicks with guns, aphrodisiacs, or bizarre duplicating artifacts. No more excuses."
    elif novacrimelewd: 
        mc "There’s no pretense this time. No external interferences. No crazy chicks with guns or bizarre duplicating artifacts. No more excuses."
    elif novadildo:
        mc "There’s no pretense this time. No external interferences. No crazy chicks with guns or aphrodisiacs. No more excuses."
    else:
        mc "There’s no pretense this time. No external interferences. No more excuses."
    mc "Now, it's just me... longing for you."
    no "Mmmhh..."
    mc "Don’t you want me too?"
    show fc 30
    no "I do..."
    no "And I don't think I can hold out much longer before going completely insane..."
    show fc 31
    mc "Oh, my poor Nova..."
    mc "I'm gonna give you everything you're craving... and more..."
    show fc 30
    no "Please..."
    no "I want it so bad..."
    no "I want to... take things to the next level with you. I want..."
    no "I want you to be the one."
    show fc 31
    mct "FINALLY she's shedding all that nervousness and speaking her mind clearly..."
    mc "Oh, Nova..."
    mc "There's literally nothing else I want more in this world right now."
    no "*Purring* Mmmmmmh..."
    mc "*Teasingly* Wait... we're still talking about cuddling, right?"
    no "*Giggles* Mhhmm."
    show fc 30
    no "Of course..."
    no "I need you to {i}cuddle{/i} me hard..."
    show fc 31
    mc "Oh boy..."
    play sound3 chair1
    play sound4 couch
    show fc 32
    mc "*Sitting next to her* Why don't you take those shorts off too?"with dis12
    mc "Consider it my only request for the night."
    mc "I'm just itching to see that perfect round butt of yours again."
    show fc 33
    no "Uh..."
    no "*Giggles* Well, if you insist..."
    play sound chair2
    play sound2 clothes5
    show fc 34
    no "*Standing up* I haven't been hitting the gym in a while, so... my butt might not be at its peak." with dis12
    mc "I'm sure it's still just as–"
    play sound clothes4
    play sound6 clothes4
    show fc 35 with dis12
    mc "...good." with dis08
    play sound2 clothes3
    play sound7 clothes3
    show fc 36 with dis15
    mc "Jesus Christ, Nova..."with dis
    mc "You only brought up the training bit because you wanted me to swoon over how flawlessly perfect your butt was, didn't you?"
    no "*Giggles* Perhaps."
    mc "Not to mention those panties look sexy as fuck on you..."
    show fc 37
    no "*Giggles* Do you like them?" with dis
    mc "Hell yeah..."
    no "Anything else you like...?"
    mc "Well, we can start talking about that sexy, toned tummy of yo–"
    $ renpy.music.set_volume(0.7, delay=9.0, channel='music3')
    play sound chair1
    play sound2 clotheswhoosh
    play sound3 whoosh6
    play sound4 squeak
    scene fc38 
    bla "Stirred by the shower of compliments, Nova enthusiastically leaps onto you, initiating another passionate kiss." with hpunch 
    play sound5 clothes3
    show fc 39
    mc "*Kissing her back* (God... her fragrance is intoxicating...)" with dis15
    no "MMMMmmmmm..."
    show fc 40
    mc "*Groping her butt* (I can't get enough of her body...)" with dis14
    mct "She's like pure energy, a mischievous little devil tempting me..."
    no "Mmmmmm..."
    mct "But I need to take it slow... Nova's first time has to be special."
    mct "Given her moans and reactions, she's probably fantasized about this even more eagerly than I have... I can't ruin it now."
    show fc 41
    no "MMMmmmmmmm..." with dis14
    show fc 42 with dis12
    no "*Interrupting the kiss* C-Can I..." with dis12
    no "*Whispering* Can I touch it...?"
    mc "*Whispering* Touch it...?"
    mct "Or maybe there's no need to be that gentle with her after all..."
    mc "*Whispering* Fuck yes, you can..."
    play sound clothes4
    play sound2 clothes5
    play soundlow zip volume 0.6
    scene fc 43 with dis17
    no "*Whispering* Oh my god..."with dis12
    no "*Whispering* You're so... hard..."
    no "*Whispering* I-Is that all for me?"
    mc "You know it is..."
    $ renpy.music.set_volume(0.45, delay=8.0, channel='music3')
    play sound clothes5 fadein 2
    $ renpy.music.set_volume(1.0, channel='soundloop')
    $ renpy.music.set_volume(1.0, channel='soundloop2')
    play soundloop wetting4 fadein 2
    play soundloop2 wetting4 fadein 2 volume 0.4
    scene novasex1 with dis2
    bla "Nova pulls your pants down and proceeds to jerk you off, as her lips close around yours once more." with dis12
    no "MMmmmmmmMMmm..."
    mct "Oh my god, her fingers are curled so tightly around my dick..."
    mct "She’s so soft..."
    mct "And the best part is that I didn't even have to prompt her or guide her into it."
    no "*Moaning in between breaths* AAaahhh..."
    mct "There’s a hint of nervousness behind each of her movements, but her fierce passion shines through."
    mct "This feels too damn good..."
    no "Mmmmmhh..."
    mct "I wanna make her mine..."
    pause
    stop soundloop fadeout 2
    stop soundloop2 fadeout 2
    play sound2 clothes3
    play sound rubclotheslong
    play soundlow squeak
    scene fc 44 with dis2
    no "*Leaning over your lap* MMmmmmmhh..." with dis12
    mc "Oh fuck yes..."
    show fc 45
    mc "I've missed your touch so much, Nova..." with dis12
    no "Me too..."
    no "I wanna... taste you again..."
    play sound4 clothes3
    show fc 46
    mc "*Pulling her panties down* Were you left yearning for more after the last time you sucked my cock, you naughty girl?" with dis14
    no "*Giggles* Maybe..."
    mc "It's all yours then..."
    $ renpy.music.set_volume(0.35, delay=7.0, channel='music3')
    play soundloop blowjob2 fadein 2
    scene novasex2 with dis2
    bla "Without thinking twice, Nova wraps her fleshy lips around your member and starts sucking it with fervor. Her slurpy sounds fill the air, ceasing only for her brief gasps for air."with dis 
    mc "Oooooohhhhh f-fuck yeaaaahhh..." 
    mc "That's it, babe..."
    mct "Oh my god, she’s just pouring out drool from her mouth..."
    mct "I feel like I'm in heaven..."
    no "*Gagging* MMmmmhhh... mmmhmhhh..."
    scene novasex2b with dis2
    mc "Nice job..." with dis 
    no "*Gagging* MmmMmMMmmmhh..."
    bla "Nova’s every move makes it clear how much she’s savoring the moment. Her tongue glides enthusiastically around your cockhead, her desire to please overpowering her."
    mc "Oh, Nova..."
    mc "You're so fucking good at this..."
    no "MMmmmmmh..."
    mct "Dear Lord, she barely needs to pause for breath..."
    mc "Please don't stop..."
    no "*Gagging* MMmmmm..."
    mc "Don't stop now..."
    pause
    play sound chair1
    play sound2 squeak
    stop soundloop fadeout 1
    scene fc 47
    bla "You suddenly stand up and push Nova onto the bed beside you."with dis12
    mc "F-Fuck, Nova, I'm about to lose it."
    mc "No more foreplay... I don’t want any more wasted time."
    mc "Let's do it NOW..."
    play sound4 squeak
    play sound3 clothes3
    play sound8 ["<silence 0.4>", bodycollide]
    scene fc 48
    bla "You spread Nova's legs and get on top of her, slapping your fully erect cock on her tummy with an enticing “plap.”"with dis12
    mc "I {i}need{/i} to be inside of you..."
    mc "I NEED to feel your pussy..."
    no "Aahh..."
    play sound5 clothes3
    show fc 49
    no "Mmmh... I c-can't. S-Sorry. I want to, b-but I can’t." with dis12
    mc "E-Eh? What? What happened?"
    no "I..."
    no "I promised my mom we wouldn't do it without a condom."
    mc "W-What?"
    mc "But... I d-didn't bring any. Do you have any here?"
    no "N-No."
    mc "Then..."
    mc "Shit, p-please don't bail on me now."
    no ". . ."
    mc "D-Do you really want to stop?"
    scene fc 50
    no ". . ." with dis15
    show fc 51
    mc "What if... I just make sure to finish outside?"
    mc "Would you want to continue then...?"
    show fc 50
    no ". . ."
    show fc 51
    no ". . ."
    play sound2 clothes3
    show fc 52
    no "*Playfully* Would you tell my mom?" with Dissolve(1.3)
    show fc 53
    mc "Not even a word..."
    no "Hmm."
    show fc 52
    no "Okay then..."
    show fc 53
    mc "*Teasingly* Okay, what?"
    show fc 52
    no "Okay... let's do it."
    show fc 53
    mc "Do what?"
    show fc 52
    no "*Giggles* You know what."
    show fc 53
    mc "Mmmm... not really, no. You'll have to be more explicit."
    mc "What exactly do you want me to do?"
    no ". . ."
    show fc 52
    no "*Whispering* I want you to fuck me."
    no "*Whispering* Now."
    show fc 53
    mc "Oh, Nova... hearing those words is literally a dream come true."
    play sound clothes3
    play soundlow squeak
    play sound7 ["<silence 0.6>", penetration2] volume 0.6
    play sound6 rubbody volume 0.6
    scene fc 54
    bla "You gently place the tip of your dick on Nova's pussy. A soft moan escapes her lips, but her eyes betray no sense of nervousness. She is ready for you." with dis12
    no "Aaah..."
    mc "You sure about this...?"
    no "*Whispering* Yes..."
    no "*Whispering* Put it in..."
    mc "Here we go..."
    play sound penetration3
    show fc 55
    mc "AAAAaaaaahh..." with dis15
    no "AAAAAAaaaAAAGhh..."
    mc "F-Fuck, you're so tight..."
    play sound2 clothes3
    play sound4 squeak 
    show fc 56
    no "*Panting* OH MY GOD."with dis12
    no "*Panting* OH MY G-GOD, IT'S IN."
    show fc 57
    mc "It is, at last..."
    show fc 56
    no "It feels so huge..."
    show fc 57
    mc "I'm gonna start to move, okay?"
    show fc 56
    no "Yes..."
    no "O-Okay..."
    no "I'm ready..."
    play soundloop novasex3 fadein 2 volume 1.1
    scene novasex3 with dis2
    no "*Moans* Aaahh..." with dis12
    no "Oh my g-god..."
    no "OH MY FUCKING GOD."
    mc "Ohhhhh Nova, FINALLY..."
    mc "You have no idea how long I've been longing for this... how long I’ve been thinking about this..."
    no "M-Me too..."
    no "*Panting* I've b-been dreaming about this... f-for ages..."
    mc "Dear Lord, you're too tight..."
    no "*Panting* You're too big..."
    mct "If she wasn't absolutely soaked right now, I wouldn't even be able to fit the tip in..."
    mct "But fuck me, this feels like heaven..."
    no "*Moans* AAAAaaaAAaahh..."
    mc "D-Does it hurt...? L-Let me know if it’s too much..."
    no "N-No! It feels..."
    no "A-A-AaAAagghhh..."
    no "{bt=3}*Moans* Good...{/bt}"
    mc "Good girl..."
    no "*Moans* AAAAAaahhh..."
    no "Oh, [mc]..."
    mc "Do you like feeling me inside of you? Is it what you hoped for?"
    no "*Moaning* I f-fucking love it....."
    stop soundloop fadeout 2
    play sound clothes3
    play soundlow squeak
    scene fc 58
    mc "I don’t believe you... let me check that myself..." with dis2
    no "*Giggles* Mmmmmmh..."
    play sound2 rubbody
    show fc 59
    bla "You lift Nova's shirt up, revealing her erect nipples." with dis15
    mc "Ah, you weren’t kidding..."
    no "*Giggles* Mmmh..."
    mc "God, you're so fucking hot."
    mc "Ready to speed up a bit...?"
    no "*Giggles* Mm-hm..."
    play sound5 clothes3
    play sound6 clothes3
    play sound7 squeak fadein 1 volume 0.6
    play soundloop novasex3b fadein 2
    scene novasex3b with dis2
    no "AAAAaahhhhh... aaaaahhh..." with dis12
    mc "*Panting* Oh, baby..."
    no "MMmhh.... mmmmm.... mmmggghh..."
    pause
    no "*Panting* J-Jesus..."with dis12
    mc "Ohh y-yeah..."
    no "*Panting* Oh, [mc]..."
    no "*Panting* From down here you look so..."
    no "*Panting* So p-powerful... so strong..."
    no "*Panting* I can see... all your muscles..."
    no "*Panting* The veins on your a-arms... you’re so... unghhh..."
    no "*Panting* AAAaaAAAaaAaahhhh..."
    no "*Panting* P-Please, take me..."
    no "*Panting* Make me yours..."
    bla "Nova's words, coupled with the sight of your manhood penetrating the petite ginger girl's pale physique, kindle a fire within you. You renew your thrusts with exuberance."
    mc "AAahhh... FUCK YES..."
    no "D-Do you like my body too?"
    mc "I fucking love your body... your skin... your cute face... your tight ass..."
    no "*Moaning* MMMMmmmmmhh... yeah..."
    mc "Your pussy feels like it’s... sucking me in..."
    no "*Moaning* Oh, [mc]..."
    no "*Moaning* This feels... i-incredible..."
    no "AAAAAAGGHH....."with hpunch 
    no "YES... give it all to me..."
    no "Go deeper..."
    no "G-Go faster..."
    mc "Deeper?"
    mct "I can actually sense her tension easing and her body getting more relaxed... maybe she's ready for some harder thrusts?"
    mc "A-Are you sure?"
    no "*Panting* I've never been m-more certain of anything..."
    no "*Panting* Give me every inch..."
    stop soundloop fadeout 1
    play sound chair1
    play sound3 clothes3
    play sound4 rubclotheslong
    play sound2 squeak
    scene fc 60
    bla "You finally peel off Nova's shirt and pin her body against the bed." with dis
    mc "Now you'll see the real deal..."
    no "*Breathing heavily in anticipation* Yeah..."
    no "*Breathing heavily in anticipation* Fuck me HARD, [mc]..."
    play sound4 squeak
    scene novasex3c with dis2
    no "Oh my GOD....." with dis12
    no "{sc=2}Oh my fucking GODDDDD........{/sc}"
    bla "You begin thrusting your hips relentlessly against Nova's, your dick hitting the deepest parts of her with each thrust. Goosebumps appear all over her skin as she adjusts to your new speed."
    mc "OOOOOOooohhh fuuuuuck..."
    mct "I knew she could take it all... she might be petite, but she's resilient as a nail."
    mc "AAAahh..."
    mc "N-Now we're talking, babe..."
    no "*Panting* AAAAAAhhh... AAAHHHHH... AAAAGGGGHHHGHH..."
    mc "O-Oh sweet heavens, t-this is amazing..."
    no "*Panting* Oh Lord... y-you're gonna break me..."
    mc "Isn't this what you wanted...? Didn’t you hope I’d f-fuck you like this?"
    no "*Panting* AAAAAAGgghhh... yeah..."
    pause
    no "Oh my god..."with dis
    no "{sc=2}Oh my god......{/sc}"
    no "{sc}OH MY GODDDDDD......{/sc}"
    play soundlow chair1
    play sound squeak
    scene novasex3c2 with hpunch
    mc "*Panting* FUUUUUUCKKK...." with dis12
    no "*Panting* OH GOOD GRACIOUS..."
    no "*Panting* Aaahhhh..."
    no "*Panting* I d-d-don't think I can keep up this pace, [mc]..."
    if novadildo:
        mc "*Panting* I saw your pussy devouring that dildo, Nova..."
    mc "*Panting* I know you can do this..."
    if novadildo:
        no "*Panting* B-But you're WAY thicker than t-that..."
        no "*Panting* And w-way more..."
    else:
        no "*Panting* T-This is just too..."
    no "{sc=2}*Panting* Intense....{/sc}"
    mc "*Panting* Aaaahhh..."
    mc "*Panting* I love how wet you are, even at this speed..."
    no "*Panting* I'm gonna cum, [mc]..."
    no "*Panting* I can't..."
    no "*Panting* H-Hold it..."
    no "*Panting* Any..."
    no "*Panting* MORE!!!!"with hpunch
    no "{sc=2}*Panting* [mc!u]....{/sc}"with hpunch
    play sound cumall
    play sound2 chair1
    play sound3 squeak
    scene fc 59b
    no "{sc=2}*Orgasming* AAAAAAAaaghhhhhhhhhgh...{/sc}" with hpunchlong4 
    play sound4 cum4
    play sound5 squeak
    bla "You stop as Nova’s thighs wrap tightly around your waist, her shudders and shakes surprising you as she orgasms." with hpunch
    play sound6 cum4
    play sound7 squeak
    scene fc 59b
    no "{sc=2}*Orgasming* AAAAAAAaaghhhhhhhhhgh...{/sc}" with hpunchlong4 
    mc "*Panting* Damn..."
    no "*Panting* OH, [mc!u]..."
    no "*Giggles* T-This sensation was... indescribable..."
    mc "Y-Your hips spasmed so hard that I thought you were gonna snap my cock..."
    no "*Giggles* S-Sorry..."
    play sound ["<silence 0.6>", chair1] volume 0.7
    play sound2 ["<silence 0.6>", squeak]
    play sound3 clothes3
    play sound4 rubbody
    scene fc 61
    bla "As though she were a squirrel clinging to a branch, Nova deftly spins on top of you, prompting you to sit on the bed." with dis17
    mc "Huh...?"
    no "*Recovering her breath* We're not done here yet..."
    no "*Panting* I need..."
    scene novasex4 with dis2
    no "*Panting* Moreeeee..." with dis12
    no "*Panting* Oh my goddd..."
    bla "Nova starts to bounce on your cock, seemingly immune to fatigue."
    mc "Oooohhh Lord..."
    no "*Moans* AAAaaahh..."
    no "*Moans* Aaaaaahhhh... it's sp-preading me apart..."
    mc "You're doing just fine... keep going..."
    mc "Ride that cock for all it’s worth..."
    bla "The tantalizing view of Nova's petite breasts bouncing right in front of your face propels you into a new realm of heightened sensations and pleasure."
    bla "Her ceaseless energy awakens something deep within you, enhancing your own drive."
    mc "M-My god, Nova, yessss..."
    mc "So good..."
    no "*Moans* Yeaahhh..."
    mc "Go faster..."
    no "*Moaning* Can I...?"
    mc "How is that even a question...?"
    no "*Giggles* Okay..."
    scene novasex4bswitch with dis2
    no "*Panting* AAAaaaagghhhh... aaaaaahhh... aaaAaaaAAAhh..."with dis12
    mc "O-O-Ohh f-fuck..."
    show screen novaangle1 with dis
    pause
    no "*Moans* Oh my g-god, [mc]..." with dis
    no "AAAAaahhhh..."
    mc "D-Does this feel as good as you expected?"
    no "*Moans* It f-feels M-MUCH BETTER..."
    no "AAAaahhh... aaaghhhh..."
    mc "Good..."
    no "*Panting* I can feel you... deep within... exploring every part of me..."
    no "*Panting* This feels... like m-magic..."
    no "{sc=2}AAAAAHHhhhhhh...{/sc}"
    mc "Ohhh fuck, you're a total addict..."
    no "*Panting* Holy fuck, all that wait was so worth it..."
    no "{sc=2}*Biting her lip* MMMHhhMMMMmmmhhhh.....{/sc}"with hpunch 
    mc "AAaghh..."
    no "*Panting* All those awkward talks about sex at school and college where I couldn't join in..."
    no "*Panting* It was all worth it... just for this moment..."
    no "*Panting* Oh, [mc]..."
    mc "F-Fuck yes..."
    mc "We have to make up for the lost time now..."
    no "*Panting* Y-Yes, we have to..."
    no "*Panting* I want you to f-fuck me... every day..."
    if novadildo:
        mc "And we'll have to hit up another party soon and play the polygraph game with Dolores and Haskel again, eh?"
        mc "You’ll probably have spicier things to tell this time..."
        no "*Giggles* YEEESsssss PLEASE!!!"
    play sound chair1
    play sound2 squeak
    scene novasex4cswitch 
    show screen novaangle2
    hide screen novaangle1
    with dis14
    no "{sc=2}AAAAAHHhhhhh... aahaahhh... aaaAAAGGHHhh....{/sc}" with dis12
    bla "Nova pushes you down onto the bed, molding her body against yours and taking your dick as deeply inside her as she can."
    no "{sc=2}AAAHHhh... aahhh... aaaghahhhh....{/sc}"
    mc "*Panting* Good grief..."
    pause
    no "{sc=2}*Faint voice* Oh my g-god, [mc], I-I'm gonna cum again...{/sc}"with dis 
    mc "*Panting* F-Fuck, me too, Nova..."
    mc "*Panting* I'm at my a-absolute limit..."
    no "{sc=2}*Panting* P-Please, just give me 20 seconds...{/sc}"
    no "{sc=2}*Panting* I'm almost there...{/sc}"
    no "{sc=2}*Panting* Please d-don't move...{/sc}"
    mc "*Panting* Oh god..."
    bla "You avert your gaze from the sight of the ginger girl's perfect body, and instead silently implore the spirits for the strength to endure another 20 seconds."
    no "{sc=2}AAAAAHHhhhhh...{/sc}"
    mc "*Panting* N-Nova..."
    no "{sc=2}*Panting* I'm cumming...{/sc}"
    no "{sc=2}*Panting* I'M CUMMING!{/sc}"
    play sound cum4
    no "{sc=2}*Panting* OH MY GOD, [mc!u]!!!{/sc}" with hpunch 
    play sound2 cum4
    no "{sc=2}AAAAAAAAAAAGGHHHHHHHH...{/sc}" with hpunch 
    play sound cum4
    no "{sc=2}YEEEESSSS...{/sc}" with hpunch 
    mc "{sc=2}F-FUCK, I CAN'T...{/sc}"
    play sound penetration3
    play sound2 penetration2
    play sound3 squeak
    play soundlow chair1 volume 0.33
    play sound4 penetration3
    scene fc 62 
    hide screen novaangle2
    with dis
    bla "At the very last second, Nova lets your cock slip out of her pussy, right as you climax." with dis
    play sound5 slap1
    play sound6 cumall
    show fc 63
    mc "*Cumming* AAAAAAAAAAHHHHHH..." with hpunchlong3
    play sound7 cumall
    show fc 63
    mc "*Cumming* FUUUUUUUUCCKKKK..." with hpunchlong3
    play sound6 cumall
    show fc 63
    mc "*Cumming* OOOoooooohhh..." with hpunchlong3
    no "Whoa..."
    play sound chair1
    play soundloop rain3 fadein 20
    stop music3 fadeout 18
    scene fc 64
    mc "*Collapsing onto your back* OH MY GOD....." with dis12 
    mc "*Breathless* Man..."
    mc "*Breathless* What in the world just happened..."
    mc "*Breathless* I don't even know if I'm still in the same dimension..."
    play sound2 squeak
    play sound3 clothes3 
    play sound4 clothes3
    scene fc 66
    bla "You watch Nova as she hops off you and rolls over the bed, purring like a playful cat." with dis15
    show fc 65
    no "Oh, [mc]..."
    no "Just... WOW."
    show fc 66
    mc "I take it you enjoyed it..."
    show fc 65
    no "Enjoy...?"
    no "I enjoy drawing and watching anime, this was..."
    no "I don't even know what this was."
    show fc 66
    mc "*Chuckles* I'm–"
    play sound chair1
    play sound2 squeak
    show novasexzoom
    no "C-Can we do it again?!" with vpunch 
    scene fc 68
    mc "*Chuckles* Of course, we..."
    mc "Wait... you mean... now?"
    show novasexnod
    no "*Nods*"
    mc "Now... like... immediately?"
    scene novasexnod
    no "*Nods*"
    mc "Um..."
    mc "I m-mean... I-I'd love to, but I need a little rest. R-Refractory period and all."
    mc "The spirit is willing, but the flesh is spongy and... bruised."
    scene fc 67
    no "Rest like... for a minute?"
    scene fc 68
    mc "M-More like..."
    no ". . ."
    mc "...10?"
    play sound squeak
    play sound2 clothes3
    show fc 69
    no "*Sitting up* PERFECT!" with dis
    no "Right on schedule! Enough time to eat and head back to The New World later, but also just enough for me to do something I've been itching to try!"
    show fc 70
    mc "W-What are you going to do...?"
    show fc 69
    no "It's a surprise!"
    no "Give me 10 minutes!"
    no "Actually... I already straightened my hair, so... just 5!"
    no "You stay here and recover!"
    play sound squeak
    play sound2 dooropen1
    play sound3 run
    scene fc 71
    bla "Nova bolts out of the room at lightning speed." with dis2
    play sound4 chair1
    scene fc 64
    mc "*Lounging back on bed* Holy cow..." with dis
    mct "This girl is going to be the death of me."
    mct "She really has unlimited energy... and what's better, she knows how to use it."
    no "I'm almost finished!"
    mc "Not even a minute has passed!" with hpunch
    no "There's water and eggs in the fridge if you need them!"
    mc "O-Okay, thanks!"
    mct "Oh Jesus, she wants to wring me out like an orange..."
    mct "I mean... not that I'm complaining."
    mct "I never thought I'd find someone who'd match my energy levels, but damn..."
    mct "And how tight and wet she is... sheesh. Wars have been fought over less."
    play sound doorclose
    no "*Closing the door* Done!"
    mc "Oh my gosh, Nova, it hasn't even been 3 minutes..."
    $ renpy.music.set_volume(0.5, channel='music3')
    play music3 ["<silence 1.3>"]
    queue music3 silverware fadein 4
    stop soundloop fadeout 16
    play sound wood2
    show fc 72
    mc "*Turning your head towards her* You can't expect me to..."with dis14
    mc "Oh my god."
    play sound2 chair2
    play sound3 squeak
    scene fc 73
    mc "*Standing up* Oh my fucking god..." with dis12
    bla "You can feel your body deciding to defiantly ignore any notion of a refractory period, as blood rushes to your cock."
    mc "How..."
    mc "Is that a wig?"
    show fc 75
    no "*Giggles* Of course not!" with dis 
    no "But it's not a real dye, just a spray can I bought."
    no "The blue color will wash away the next time I shower."
    show fc 74
    if novadildo:
        mc "Oh fuck, babe, you don’t know how much I’ve wanted this..."
        show fc 75
        no "I've been wanting to do this since the party when I first wore this cosplay."
        no "It's been lingering in my mind since that day..."
        show fc 74
        mc "You and me both..."
        show fc 75
        no "Except this time... no alarms will go off if we get too close."
        no "*Whispering* This time... we can touch each other as much as we want..."
    else:
        mc "Oh fuck, babe, this is REALLY turning me on, and I don't even play that game..."
        show fc 75
        no "*Giggles* It's not Jinx from the game, but the show! It's different!"
        show fc 74
        mc "Wherever it's from, I like it..."
    play sound wood2 volume 0.5 fadein 2
    play sound2 rubbody
    play soundlow clothes3
    scene fc 76
    bla "You effortlessly scoop up Nova by the thighs, lifting her against the wall as if she weighed nothing." with dis12
    if novadildo:
        mc "Fuck yes, we can..."
    show fc 77
    no "*Giggles* You're so strong..."
    show fc 76
    if novadildo:
        mc "You can't even imagine how many times I pictured myself fucking you in your Jinx costume."
    else:
        mc "Fucking you while you're in cosplay is a fantasy I didn't even know I had."
    show fc 77
    no "Well... you can make it a reality now."
    no "Fuck me right here and right now."
    show fc 76
    mc "Is that what you want, you dirty girl?"
    show fc 77
    no "Yeah..."
    if maatsex:
        no "I want you to fuck me against this wall just like you fucked Maat that day in front of me..."
        no "Make me scream like she did..."
        no "Actually... scratch that. Make me scream louder..."
    else:
        no "I want you to fuck me against this wall..."
    show fc 76
    mc "Oh yeah..."
    play sound penetration2
    scene novasex5 with dis2
    bla "You penetrate Nova's warm pussy once more, pressing her against the wall with strong, passionate thrusts." with dis12
    no "AAAAaaahhh..."
    mc "L-Like this?"
    no "*Moans* Yessss..."
    no "*Moans* Oh, fuckkk..."
    no "*Moans* Y-You're so deep..."
    mc "Aaaaahhh... I know..."
    no "*Whines* AAAAaghhh... f-fuck..."
    mc "I thought Jinx was a tough one..."
    no "AAAahh... I-I am a tough girl...."
    mc "Are you...?"
    no "Yeah... and I can... pr-prove it..."
    no "F-Fuck my pussy, [mc]..."
    no "Make it yours..."
    no "Do whatever you want to me..."
    no "{bt=3}*Whispering* I can take it all...{/bt}"
    play sound slam
    scene novasex5b
    pause 0.001
    no "{sc=2}*Panting* AAAAHHH.... AAAAGHHhhhh...{/sc}" with hpunch
    mc "*Panting* Ooooohhhhh..."
    no "*Panting* AAAAagGGGHHHH..."
    no "*Panting* J-Just like thisss..."
    no "*Panting* OOOoooggghhhhh... aaaAAAAaaHHh...."
    no "*Panting* T-This is c-completely surreal..."
    no "{sc=2}*Panting* OH MY GODDDDD...{/sc}"with hpunch 
    mc "F-Fuck yeah..."
    no "{sc=2}*Panting* AAAAAAGHHH... YESSSS...{/sc}"
    mc "I r-really hope these walls are thick enough, or the next encounter with your neighbors might get a tad awkward..."
    no "*Panting* AAAAHHHH... "
    no "*Panting* P-PLEASE DON'T STOP..."
    bla "Yielding to the moment, Nova just lets herself go and completely surrenders her body to you, her sole focus to maintain a tight grip on your neck."
    mc "*Panting* Oh shit..."
    mc "*Panting* I'm g-gonna cum again..."
    no "*Panting* AAAAAHHHHH..."
    no "*Panting* NOT YET, PLEASE..."
    mc "*Panting* I-I can't stop it..."
    no "*Panting* I'm gonna cum too..."
    no "*Panting* I'm almost there..."
    mc "*Panting* I-I have to set you down..."
    no "*Holding onto your neck* NOT YET PLEASE..."
    no "{sc=2}*Panting* AAAAGH!!!{/sc}" with hpunch 
    mc "*Panting* Oh, Nova..."
    mc "*Panting* O-Okay, I really have to set you down now..."
    mc "*Panting* I have to s-stop or I'm gonna finish insi–"
    play sound bodycollide2
    play sound2 fall3
    play sound4 fall2
    play sound3 clotheswhoosh
    play sound5 penetration2
    scene novaspinner
    bla "Nova twirls around you like a fidget spinner, clasping onto you incredibly tightly and forcing you to lean against the wall." with hpunch
    $ ns5c = True
    scene novasex5cswitch 
    show screen novaangle3
    with dis2
    mc "{sc=2}O-O-OHHH FUCKKKKK.....{/sc}" with dis12
    no "{sc=2}*Squeals* AAAAHHHH.... AAHHH.... AAAAAGGGGHH...{/sc}"
    mc "{bt=3}W-W-What the fuck are you doing, Nova...{/bt}"
    no "{sc=2}*Squeals* F-Fuck yes...{/sc}"
    no "{sc=2}*Panting* Oh my god, this is AMAZING....{/sc}"
    mc "{bt=3}O-Oh s-sweet Jesus....{/bt}"
    no "{sc=2}*Squeals* AAaaaahhh...{/sc}"
    mc "{bt=3}Y-You're fucking crazy...{/bt}"
    no "{sc=2}AAAAAAAAGGHHHhhh...{/sc}"
    no "{sc=2}P-Please don't let me go, [mc]...{/sc}"
    mc "{bt=3}I'm not even holding you...{/bt}"
    no "{sc=2}*Squeals* AAAAAAAHHHH!!!!{/sc}" with hpunch 
    bla "Nova continues to milk you furiously, letting out a piercing shriek with each forceful collision of your cock against her petite form." 
    no "{sc=2}AAaaghhh... aaaghhh... aaAAAhhh... AaaggGGhh...{/sc}"
    mc "{bt=3}Nova, s-stop...{/bt}"
    mc "{bt=3}You're gonna make me cum inside...{/bt}"
    no "{sc=2}*Panting* I don't c-c-care anymore...{/sc}"
    no "{sc=2}*Panting* I-I want you to f-fill me up...{/sc}"
    mc "{bt=3}B-But you said...{/bt}"
    no "{sc=2}*Panting* E-Empty yourself INSIDE of me...{/sc}" with hpunch
    mc "{bt=3}Oh f-fuck...{/bt}"
    mc "{bt=3}I-I'm cumming so much...{/bt}"
    no "{sc=2}*Panting* Yeah... cum inside me... please. Please. Pleaseeeee.{/sc}" with hpunch
    play soundlow thunder fadein 1
    scene novasex6 
    hide screen novaangle3
    with dis12
    play sound4 ["<silence 6.72>", cum3]
    play sound3 ["<silence 7.22>", cum3]
    play sound2 ["<silence 8.05>", cum3]
    play sound ["<silence 9.2>", cumall]
    play sound6 ["<silence 9.2>", slap1]
    no "{sc=2}I'm cumming...{/sc}{w=1.3}{nw}" with dis08
    no "{sc=2}OH [mc!u]...{/sc}{w=1.1}{nw}" 
    no "{sc=2}YES.{/sc}{w=0.38}{nw}"
    no "{sc=2}YES. YES.{/sc}{w=0.37}{nw}"
    no "{sc=2}YES. YES. YES. {/sc}{w=0.37}{nw}"
    no "{sc=2}YES. YES. YES. YES. {/sc}{w=0.37}{nw}"
    no "{sc=2}YES. YES. YES. YES. YES. {/sc}{w=0.37}{nw}"
    no "{sc=2}YES. YES. YES. YES. YES. YES.{/sc}{w=0.37}{nw}"
    no "{sc=2}AHH!{/sc}{w=0.28}{nw}"
    no "{sc=2}AHH! AHH!{/sc}{w=0.28}{nw}"
    no "{sc=2}AHH! AHH! AHH! {/sc}{w=0.28}{nw}"
    no "{sc=2}AHH! AHH! AHH! AGHH! {/sc}{w=0.28}{nw}"
    no "{sc=2}AHH! AHH! AHH! AGHH! AAAGGHHH!!!!{/sc}{w=0.29}{nw}" 
    no "{sc=2}AAAAAGH!!{/sc}{w=0.5}{nw}"with hpunch 
    no "{sc=2}{size=33}AAAAAAAAAAAHHH!!!{/sc}{w=0.83}{nw}"with hpunch 
    no "{sc=3}{size=36}AAAAAAAAAAAAAGGGGGHHHHH!!!!{/sc}{w=1.15}{nw}"with hpunch 
    no "{sc}{size=39}AAAAAAAAAAHAAAGGGGGHHHHHHHHHH......{/sc}{w=1.2}{nw}"with hpunch 
    stop music3 fadeout 16
    play soundloop rain3 fadein 11
    play sound4 penetration3
    scene fc 79 with Dissolve(1.3)
    no "{bt=3}*Finally releasing her tight grip* AAAaaAaaaaggghhh...{/bt}"with dis2
    mc "*Panting* Oooooh jeeeezzzz..."
    mct "God, I feel like I just unloaded 3 gallons of cum inside her..."
    mct "Even though I came twice in less than 10 minutes..."
    no "*Panting* W-W-Waaawaaa...."
    mc "*Panting* Oh, Nova..."
    play sound penetration3
    play sound2 rubbody
    play sound4 ["<silence 0.9>", fallfull]
    scene fc 80 with Dissolve(1.1)
    no "*Collapsing to the floor* G-Gggaaaaahhh..." with vpunchslow
    mc "Oh boy..."
    scene fc 64 with dis2
    play sound5 chair1
    play sound6 squeak
    bla "After having reached climax together, you wobble back to the bed on shaky legs and flop down onto the blanket, completely drained." with vpunchslow
    bla "Both of you linger in silence for a minute, each grappling to regain a sense of reality amidst the aftermath."
    mc "Damn..."
    mc "You're a nympho..."
    no "*Still on the floor, laughing* Hahah, shut up..."
    play sound wood2 volume 0.5
    no "*Struggling to stand up* Oh jeez, I c-can't even walk." with dis
    play sound7 chair1
    play sound2 squeak
    no "*Collapsing onto the bed next to you* AAaagh..." with vpunchslow
    play music2 romantic3 fadein 7
    mc "How am I supposed to face the world after this?"
    no "*Giggles* I don't know."
    mc "I even lost track of time."
    mc "I mean, do we still have time to get Coyote's treasure? Or is it already Monday? I feel like we’ve spent a year fucking."
    no "*Giggles* We've got time!"
    play sound rubbody
    play sound2 squeak
    scene fc 81
    mc "*Sitting up* You're quite the giggler, huh?" with dis14
    show fc 82
    no "*Giggles* I'm just happy!"
    show fc 81
    mc "Damn..."
    mc "You're so beautiful..."
    show fc 83
    no "*Giggles* Oh, hush! My hair is a mess."
    show fc 81
    mc "Truly!"
    mc "I don't know if it's the light, that messy style, or just your eyes, but... wow."
    show fc 82
    no "Thank you for all of this, [mc]."
    show fc 83
    no "I mean... not just the... you know, which was obviously MIND-BLOWING."
    show fc 82
    no "For everything."
    no "Thank you for making me feel special."
    show fc 81
    mc "You {i}are{/i} special."
    show fc 83
    no "I know I can be a bit annoying sometimes, and a bit irrational, and perhaps a smidge overdramatic too." 
    show fc 82
    no "But somehow, you make me feel good about myself."
    no "It's like you care about more than just what I can do – you care about who I am."
    no "And..."
    show fc 83
    no "Please, if this is all just in my head, don't tell me. I'm happier this way."
    show fc 81
    mc "*Chuckles* No, it's not just in your head. I feel the same way."
    mc "Thank you, Nova."
    mc "And I also don't mean just the “you know”, which was obviously W-O-W."
    mc "For everything."
    mc "You're awesome. I'm so glad you became a part of my life."
    $ nova_points += 2
    play sound beat
    show screen heartbeat
    no "Hmm."
    show fc 83
    no "Anyway!"
    no "We should REALLY eat something now!"
    no "We still gotta go back to The New World and recover the Heart of the Abyss!"
    show fc 81
    mc "Hell yeah!"
    mc "I NEED that pizza!"
    show fc 82
    no "Pizza?? Are you still willing to go get it?"
    show fc 81
    mc "Oh, for sure. A little rain won't stop me."
    mc "I'll cut through Chinatown for a shortcut. I can be back here in... 20 minutes."
    show fc 82
    no "Well... okay then!"
    no "*Giggles* I'm way too hungry to hold you back."
    no "I'm gonna grab a shower in the meantime."
    show fc 81
    mc "The rain will be my shower. Just keep a towel out for me for when I'm back, please."
    show fc 82
    no "*Giggles* Will do!"
    show fc 81
    mc "Alright then, see you in a bit!"
    no "Mm-hm."
    play sound clothes3
    play sound2 squeak
    show fc 84 with dis15
    bla "Nova crawls towards you and gives you one last, passionate kiss on the lips." with dis12
    no "Mmmmm..."
    play sound squeak
    play sound2 dooropen1
    play sound3 run
    scene fc 71
    no "*Running away* Alright, go, go, FAST!" with dis2
    no "I'm super hungry!"
    no "I'll shower and get everything ready in the meantime so we can hop back into Eternum SUUUUPER fast!"
    mc "Sounds good!"
    no "Oh, and ask them to make mine with extra cheese! Crust EXTRA thicc!"
    mc "*Chuckles* Got it!"
    mct "Oh man, this girl is truly one of a kind..."
    mct "I'm one lucky bastard."
    mc "*Sighs* (Alright... I better get moving!)"
    mct "As has become customary, I've got no time to waste..."
    jump ending07


label ending07:
    stop music2 fadeout 6
    stop soundloop fadeout 7
    stop music fadeout 6
    scene black with dis25
    show screen afewminuteslater with dis17
    pause
    $ renpy.music.set_volume(0.35, channel='soundloop2')
    play soundloop2 wind fadein 5 
    scene fff 1 
    hide screen afewminuteslater
    with dis25
    mc "*Glancing at the sky* (Hmmm... seems like the rain's going to give me a break while I go grab those pizzas.)" with dis15
    mct "After all, I'm having some real luck today!"
    mct "Everything just keeps getting better and better."
    play sound dogfar
    show fff 2
    bla "You stroll along the deserted streets of Kredon’s Chinatown district, halting briefly in front of a shop window to gaze at your own reflection." with Dissolve(1.8)
    mc "Hmm."
    show fff 3
    mct "My hair's getting pretty long."
    mct "I should start thinking about getting a haircut soon."
    mct "Or... maybe I just let it keep growing and try a different style? I could talk to Penny’s hairdresser friend."
    mct "I should put some time aside for it next weekend."
    mct "And I could go shopping with Penny for some new clothes too, this shirt's already feeling too snug."
    show fff 4
    mct "Ha, if I keep getting stronger at this rate, I'll need a whole new wardrobe soon." with dis
    mc "*Chuckles* Hmm."
    if penelopepath or alexpath or nancypath:
        mct "Looking better than ever, feeling better than ever, acing all my tests at school, and getting laid with girls I used to think I couldn't even smell in my life."
    else:
        mct "Looking better than ever, feeling better than ever, and acing all my tests at school. Not that many girls yet, but... I'm making progress."
    mct "You're speedrunning through life with cheat codes enabled, [mc]."
    show fff 5
    mc "*Strolling casually* (Not to mention how I'm practically a powerhouse in Eternum now.)" with dis15
    mct "No one stands a chance against me at this point."
    mct "Not even Thanatos."
    mct "If we face each other again, I'll wipe the floor with him..."
    jun "Hey bro, you got a smoke...?"
    play sound2 dogfar
    play music2 tensionmusic fadein 6
    show fff 6
    mc "*Turning around* Huh?"with dis
    mct "Jesus, these two look and smell like shit..."
    mct "I'd heard Chinatown started to go downhill since Eternum hit the scene, but damn, didn't expect it to be this bad."
    mct "I guess this is one of the ugly sides of Eternum that nobody talks about."
    play soundlow police
    mct "In Eternum, drugs offer a temporary escape without lingering health effects, but at a marked-up steep price."
    mct "The higher cost of drugs in Eternum often leaves their users strapped for cash... until they realize they can buy the same drugs in the real world. Except now? They have to deal with all the physical fallout."
    mct "But of course, surprise, surprise... the news conveniently forgets to talk about this."
    mct "As happens with anything involving Ulysses..."
    show fff 7
    jun "Yo, didn't you hear me? I asked you if you got a cig."
    show fff 6
    mc "Eh? Ah, no, I don't have any cigarettes."
    show fff 5
    mc "*Turning around* (Anyway, I'm digressing again.)" with dis12
    mct "Let's go grab those pi–"
    play sound3 grab3 volume 0.5
    play soundlow debris3
    scene fff 8
    jun "*Grabbing you by the shoulder* Whoa, whoa, whoa..."with dis
    jun "What's the fuckin' rush?"
    jun "Chill the fuck out, dude."
    scene fff 9
    mc "Don't. Fucking. Touch me."
    show fff 8
    jun "Damn... why you gotta be such a dick, bro?"
    play sound leather2 volume 0.35
    jun "*Squeezing your shoulder tight* We're just tryna be cool here... ain't we, JJ?"
    show fff 9
    mc "*Sighs* What is this, some pathetic attempt at mugging?"
    mc "Get the hell outta my face."
    show fff 8
    jun "What'd ya just say...?"
    show fff 9
    mc "You heard me."
    show fff 8
    jun "Whoa, look at this... this lil' bitch thinks he's tough."
    show fff 9
    mc "I won't say it again."
    show fff 8
    jun "Bro, all I want is a couple of eternals. Can't you spare a little somethin' for us less fortunate souls?"
    jun "Hand over your stuff and we won't mess you up, aight?"
    show fff 9
    mct "These lowlifes are starting to piss me off..."
    mc "You don't know who you're talking to, buddy."
    show fff 8
    jun "Bein' some rich daddy's boy from uptown ain't gonna save ya here, bro."
    show fff 9
    mc "I don't need a rich daddy. I could squash you like a bug with my bare hands if I wanted."
    mc "And trust me, I’ve got way better shit to do than waste my money on a couple of fucking junkies who'll just blow it all on their next fentanyl hit like the fucking human trash they are."
    mc "So I swear to god, this is my last warning."
    mc "Let me go {b}NOW."
    show fff 10
    jun "*Giggles* Hihihi..." with dis12
    jun "Yo, did ya hear that, JJ?" 
    jun "The kiddo said he can squash us like a bug!"
    jun "They play Eternum for a few weeks and they think they become big dogs in the real world."
    jun "You're a riot, kid..."
    jun "A total riot..."
    play sound3 clotheswhoosh
    play sound debris3 volume 0.6
    play sound2 ["<silence 0.1>", fist]
    stop music2
    show fff11b
    bla "The mugger attempts to land a quick blow on your face, but you easily react and block the punch with your right hand." with hpunch
    jun "Huh...?"
    play sound5 clotheswhoosh
    play sound4 debris3 volume 0.6
    play sound6 ["<silence 0.1>", fist]
    play sound punch
    play sound2 blood3
    play sound3 bonebreak
    scene fff12b
    bla "You punch him back." with hpunch
    play sound7 fallfull
    play sound8 fallbottle
    play sound fallkitchen
    play sound3 dogfar
    scene fff 14 with dis12
    jun2 "D-Dude... w-what the fuck??" with dis08
    jun2 "He sent you flyin'!"
    play sound2 debris
    play sound4 punchlocker
    scene fff 15
    jun "*Hitting the dumpster in anger* AAAAARRRGHHHH, FUCK!!!"with hpunch 
    jun "You b-broke my nose, you fuckin' cocksucker!"
    mc "I warned you more times than I should've, so don't come crying now."
    jun "AAAAAggghh..."
    jun "You're fuckin' dead, you hear me?!" with hpunch 
    jun "{b}DEAD!" with hpunch 
    mc "Do yourself a favor and get the hell out of my town."
    mc "I don't wanna lay my eyes on your sorry ass ever again."
    show fff 5
    mc "*Turning around* (Anyway, I better hurry up to the pizzeria.)" with dis17
    mct "I've wasted enough time with this scum."
    mct "Gotta make sure to tell the girls to stay away from Chinatown, though."
    mct "This neighborhood used to be decent when I was a kid, but now it–"
    stop soundloop2
    play sound3 dogfar
    play sound gunshot volume 0.4
    play sound4 revolver
    play soundlow shootecho volume 0.1
    play sound2 earringing
    scene fff5 with Dissolve(.2)
    scene fff 5 with dis25
    pause 1
    $ renpy.music.set_volume(0.2, channel='soundloop2')
    play soundloop2 wind fadein 9
    mct "Eh...?" with dis15
    mc "*Coughing* (What...?)"
    jun2 "Are you fucking nuts?!!" 
    jun "Didn't you see him fuckin' disrespecting us?!"
    show fff 16
    jun2 "You shot him in the fucking stomach!" with dis15
    jun "Have you forgotten what happened to Alvarez??"
    jun "We gotta show 'em who's the boss!"
    jun2 "F-Fuck, dude... the cops are gonna come!"
    jun2 "I c-can't go back to the slammer..."
    jun "Then stop crying and start moving your fuckin' ass!"
    jun2 "F-FUCK..."
    play sound run volume 0.5 fadein 2
    play sound2 ["<silence 0.3>", run] volume 0.4
    scene fff 17
    bla "The two men hastily flee the scene, sprinting away into the distance."with dis2
    mc "The... stomach...?" 
    play soundloop beat3 fadein 12
    show cliff1 with Dissolve(1.52)
    pause 4
    mc "Oh, f-fuck...{w=2}{nw}" with dis
    play sound deception
    play sound2 fall3
    pause 3.6
    play sound3 deception
    play sound4 fallfull
    pause 4.1
    play sound5 glitch4 volume 0.3
    scene cliffidriel1 with dis12
    play sound5 glitch4 volume 0.3
    scene cliffidriel1
    mc "*Coughing up blood* F-Fuck...." with dis17
    mc "*Fading out* I c-can't move..."
    mc "*Fading out* M-Must... agghh... s-stay awake..."
    bla "As the initial rush of adrenaline begins to ebb, a wave of excruciating pain washes over you, enveloping your senses entirely." 
    mc "{sc=2}*Bleeding out* AAAAaaaAAARRrraaghh...{/sc}"
    play sound5 glitch4 volume 0.5
    scene cliffidriel1 with dis
    pause
    play sound5 flashback3 volume 0.6
    scene cliffidriel2b 
    pause 
    mc "{bt=3}*Bleeding out* W-What?{/bt}" with dis15
    mc "{bt=3}*Bleeding out* Id-driel...?{/bt}"
    play sound6 glitch4 volume 0.7
    scene cliffidriel2 
    id "This was not part of the path, [mc]."
    id "This wasn't foreseen."
    scene fff 18
    mc "{bt=3}*Bleeding out* You c-Can't be hEre...{/bt}"
    mc "{bt=3}*Bleeding out* T-This is Not EteRnum...{/bt}"
    scene fff 19
    id "Indeed, it's not."
    id "And that's precisely why this will be your demise."
    scene fff 18
    mc "{bt=3}*Bleeding out* W-What...?{/bt}"
    play sound6 glitch4 volume 0.7
    scene cliffidriel2 
    id "You became arrogant, [mc]."
    id "Overconfident."
    if novapath or nancypath or penelopepath or daliapath or alexpath or lunapath or anniepath:
        id "Intoxicated by power. By women. By the pleasures of life."
    else:
        id "Intoxicated by power. By the pleasures of life."
    id "You believed yourself invincible."
    id "But you're nothing but a fragile mortal."
    scene fff 18
    mc "{bt=3}*Bleeding out* P-Please, heLp mE....{/bt}"
    play sound6 glitch4 volume 0.7
    scene cliffidriel2 
    id "I can't help you in this world, [mc]."
    id "There is no coin here."
    id "No reset."
    id "No fresh start."
    scene fff 18
    mc "{sc=2}*Choking on your own blood* HHHhhgGgGGGg...{/sc}"
    scene fff 19
    id "I'm afraid this is your end, [mc]."
    id "Our end."
    id "The end. For all of us."
    mc "{sc=2}I-I...{/sc}"
    mc "{sc=2}C-C-cCa...{/sc}"
    play sound exhale fadein 3 volume 0.35
    stop music2 fadeout 2
    stop soundloop fadeout 2
    scene fff 18
    bla ". . . . ." with dis17
    id ". . ."
    play sound6 glitch4 volume 0.7
    scene cliffidriel2b
    pause
    play sound2 flashback3
    scene cliffidriel1
    stop soundloop2
    pause
    scene fff 20
    id "Farewell... [mc]." with dis17
    stop soundloop2 fadeout 12
    play sound7 police fadein 4
    play sound8 police fadein 19.5
    play music ending07song fadein 5
    pause .4
    show cliff2 with dis15
    pause 17
    jump update08


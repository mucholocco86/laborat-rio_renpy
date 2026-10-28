label update08:
    $ renpy.music.set_volume(1.0, channel='music')
    $ renpy.music.set_volume(1.0, channel='musicb')
    $ renpy.music.set_volume(0.7, channel='music2')
    $ renpy.music.set_volume(0.7, channel='music2b')
    $ renpy.music.set_volume(0.1, channel='music3')
    $ renpy.music.set_volume(0.6, channel='soundlow')
    $ renpy.music.set_volume(1.0, channel='soundloop')
    $ renpy.music.set_volume(1.0, channel='soundloop2')
    $ renpy.music.set_volume(1.0, channel='soundloop3')
    if changtie:
        $ changmicaela += 1
    if changaskmicaelaout:
        $ changmicaela += 1
    if lunapath:
        $ unlock_look("luna", 11)
    scene black
    stop sound7
    stop sound8
    pause
    play soundloop rain1 fadein 17
    play soundloop2 rain5 fadein 17
    stop music fadeout 12
    show screen sometimelater with dis3
    play sound thunder fadein 3
    pause
    $ renpy.music.set_volume(0.4, channel='soundloop3')
    hide screen sometimelater with dis2
    play soundloop3 carengine fadein 3
    scene g 1 with dis3
    play sound2 dogfar
    pause 
    stop soundloop3 fadeout 1
    play sound7 police
    play sound6 cardoor
    scene g 2 with dis17
    cap "*Snorts* Fucking hell, I hate this dumpster of a place." with dis06
    cap "And now that it gets dark before 5PM, even more so."
    cap "Can't wait to get that promotion and finally get off the streets, I swear..."
    scene g 3
    cap "What are you doing over there? Did you find anything?" with Dissolve(.9)
    play sound3 dogfar 
    scene g 4
    cop "Just trying to do my job, Em."with dis 
    cop "*Muttering* At least one of us has to..."
    show g 3
    cap "I'm sorry?"
    cap "I'm the one who set up the perimeter and called for backup."
    show g 4
    cop "There could still be someone lurking around!"
    cop "Stay alert!"
    show g 3
    cap "You know they're probably long gone by now."
    cap "I mean, come on, how many calls do we get from Chinatown every week?"
    cap "In the end it's always drug traffickers settling scores or some shit."
    cap "You know the drill, the captain briefed us himself."
    show g 5
    cop "And are we supposed to turn a blind eye? Let people kill each other?"
    cap "No one said that."
    cop "Agh, this city isn't what it used to be..."
    show g 3
    cap "Hah, it definitely isn't, you got that right."
    cap "And no, we can't ignore it, but you know how it goes."
    cap "Cordon off the area, wait for backup, collect evidence. No heroics."
    show g 5
    cop "Yeah..."
    play sound holster
    show g 6
    cop "*Sighs* I guess you're right." with dis
    show g 10
    cop "Something about that pool of blood seems off, though..." with dis12
    play sound2 thunder fadein 3
    cap "Why?"
    cop "There’s too much blood. Seems like the shooter nailed a major artery."
    cap "So?"
    cop "There's no way they walked away on their own two feet."
    show g 7
    cap "So... you think someone moved the body?"
    show g 10
    cop "Blood's fresh, no sign of drag."
    cop "Who could have carried away an adult like that, and so quickly?"
    show g 7
    cap "Maybe the perp was like... {i}very{/i} strong?"
    show g 10
    cop "Or what if..."
    cop "What if the victim was a kid...?"
    show g 7
    cap "Or... maybe someone just dumped a bucket of blood right in the middle of the street."
    show g 7b
    cop "Why do you always have to joke and trivialize everything?!"with dis08
    cop "This is serious!"
    show g 8
    cap "*Sighs* It's you who takes everything way too seriously."
    show g 7b
    cop "DEATH should be something taken seriously."
    cop "Someone could have died!"
    show g 8
    cap "I'm sorry if I don't start crying over some junkie who got killed in the worst neighborhood of Kredon because he didn't pay his dealer on time."
    show g 7
    cap "Is it wrong to maintain a professional demeanor now?" with dis08
    show g 7b
    cop "There's a difference between professionalism and lacking empathy."
    show g 7
    cap "If you say so."
    show g 7b
    cop "I do."
    cop "And you know who's to blame for all this?"
    show g 8
    cap "Oh my god, not this again..."
    show g 7b
    cop "ETERNUM!" with hpunch
    play sound6 thunder fadein 3
    cop "Society's gone numb to consequences, like life doesn't mean shit anymore!"
    cop "You're all getting brainwashed!"
    cop "Desensitized to violence!"
    cop "You can't tell reality from the game!"
    show g 7
    cap "That's not true."
    show g 7b
    cop "Do you think it's a coincidence that crime shot up by 220%% in just 5 years in the USA alone?"
    cop "Last week, a waitress shot a woman because she left her no tip!"
    cop "What's happening to America? To the world?!"
    show g 7
    cap "*Sighs* Yeah, yeah... I've seen your constant social media rants against Eternum, Mark."
    cap "But here's a reality check: Ulysses doesn't give a shit, and Eternum gains over 80,000 new players daily."
    show g 7b
    cop "Believe me, I know. Society is doomed."
    cop "And by the time you all realize it, it'll be too late."
    play sound7 police
    show g 9
    cap "Yeah... thank you for the TED talk, Mark."with dis
    cap "I’ll be in the car until backup gets here."
    cap "You can patrol the surroundings if you want to. Just keep the radio open."
    play sound ["<silence 0.8>", cardoor]
    show g 10
    cop "Sure..." with dis14
    cop "I will..."
    stop soundloop fadeout 7
    stop soundloop2 fadeout 7
    stop sound7 fadeout 9
    scene g10
    pause 1.3
    play sound whoosh4
    $ renpy.music.set_volume(1.0, channel='soundloop3')
    scene black with dis17
    play soundloop3 ["<silence 1.5>"]
    queue soundloop3 forest2 fadein 10
    pause
    play sound calypsoheal fadein 5
    scene g11 with dis3
    scene black with dis22
    pause .6
    scene 083 with dis22
    pause 5.9
    scene black with dis2
    pause .5
    scene 082 with dis22
    pause 5.9
    scene black with dis2
    pause 1
    ca "E'goven aman' ech..." with dis14
    ca "Eneth lin i'ravar..."           
    ca "E'goven aman' ech..." 
    mc "Mmh..."
    scene g11 with dis22
    mc "*Opening your eyes* Hmmmph..." with dis15
    mct "Oh god..."
    mct "My head... is spinning..."
    scene g 11
    mct "But the sun... feels so good..." with dis14
    mct "Am I... in paradise?"
    play sound branch volume 0.6
    play sound2 leaves2 volume 0.44
    play music2 calypso2 fadein 8
    scene g 12
    ca "I do wonder: Is being pierced through the torso one of your peculiar fascinations?" with dis15
    ca "If it is, please inform me, and I shall cease my efforts in rescuing you."
    scene g 13
    mc "C-Calypso...?"
    mc "Where are we...?"
    mc "This place feels like heaven..."
    show g 12
    ca "The Elarisil did not... yield the expected results initially, so I relocated myself to try anew."
    ca "But it is still the realm of Ekabar."
    show g 13
    mc "I don't even remember how I got here."
    mc "I was... in the pirate server. And then..."
    mc "There was..."
    mc "Pizza...?"
    play sound whoosh6
    play sound2 debris
    play sound3 debris2
    scene g13b
    mc "FUCK." with vpunch 
    mc "THE ALLEY!"
    show g 16
    mc "I g-got..." with dis
    mc "Eh?"
    play sound rubshort volume 0.8 fadein 1
    scene touchwound
    mc "W-What...?"
    mc "When? Why? How..."
    mc "T-There's... nothing."
    mc "I'M HEALED!"
    show g 15
    mc "Holy fuck, I thought I was done for real this time." with dis 
    show g 18
    mc ". . ."
    mc "Did you..."
    show g 19
    mc "D-Did you save me?"
    show g 20
    ca "This time was even worse than when we faced Thanatos, [mc]."
    ca "If I had been just one second late, I would not have been able to heal your wounds."
    show g 19
    mc "Oh my god... I bet."
    mc "I don't think I've ever felt worse in my life."
    mc "I've been hurt before, but... this time it was like I could feel the light fading away."
    mc "T-Thank you, Calypso."
    show g 20
    ca "You lost a lot of blood."
    ca "I actually had to regenerate it, which is a magic way more advanced than just closing wounds."
    show g 19
    mc "But..."
    mc "How am I in Eternum?!"
    mc "It's not possible! I was just in the middle of the street! In Kredon!"
    mc "Even if I passed out, no one could've hooked me up to Eternum that fast!"
    mc "It's–"
    mc "Wait..."
    mc "Wait a fucking second..."
    mc "You healed me here... b-but I was hurt in the real world!"
    mc "Does that mean I'm still bleeding out there?!"
    show g 20
    ca "If your other self did not get proper treatment, he is probably gone by now."
    ca "You barely made it here in time."
    show g 19
    mc "W-What...?"
    mc "M-My real body is DEAD?!"
    mc "What if I try to go back to the real world through an Exit Portal now?!"
    show g 20
    ca "I suppose... you cannot?"
    show g 19
    mc "What do you mean I CANNOT...??!"
    mc "Am I..."
    mc "Am I stuck in Eternum?!"
    mc "Oh no..."
    mc "DID I BECOME AN NPC?!" with hpunch 
    play sound2 clothes3b
    show g 22
    ca "I... am afraid I am not familiar with that concept." with dis15
    ca "I cannot offer much help on that front."
    show g 21
    mc "*Hyperventilating* O-Okay, okay..."
    mc "I-I need to calm down."
    mc "If someone linked me to Eternum while I was out, they must be providing medical assistance too."
    mc "Sure, I can't heal with magic like here, but hopefully, they managed to stop the bleeding."
    mc "I need to find an Exit Portal and go back to the real world."
    show g 22
    ca "I believe there is one nearby, by the river."
    play sound debris
    show g 23
    ca "*Standing up* Follow me, I can..."with dis12
    play sound3 ["<silence 0.3>", bodycollide2]
    play sound4 clothes3
    play sound5 rubbody
    play sound2 ["<silence 0.3>", fallhay]
    show g 24
    bla "Calypso staggers and collapses into your arms, as if struck by a sudden heatstroke." with dis
    mc "Oh shit, Caly??"
    mc "Are you okay?!"
    ca "*Panting* I..."
    ca "*Panting* Y-Yeah..."
    play sound6 debris
    play sound7 clothes3
    show g 25
    ca "*Clears throat* D-Don't worry." with dis15
    show g 26
    bla "She swiftly distances herself from you and regains her composure, evidently attempting to conceal her current state."
    mc "*Taking a step towards her* Are you sure you're alright...?"
    show g 28
    ca "P-Please, seriously, I am fine." with dis
    show g 27
    mc "Your eyes..."
    show g 28
    ca "It is just that... the Elarisil drained a lot of energy from me."
    ca "I just need to rest for a while and I will be fine."
    show g 27
    mc "Fuck... I feel awful now."
    mc "You're like this because of me."
    mc "Is there anything I can do to help?"
    show g 28
    ca "You cannot..."
    show g 30
    ca "I mean... well." with dis12
    ca "Now that you mention it, if you could refrain from getting into near-death situations when I'm not at full strength, I would appreciate it."
    show g 29
    mc "I-I can't make any promises, but I'll try."
    mc "Thank you again for saving me, Calypso."
    mc "I owe you my life."
    show g 30
    ca "It was... nothing."
    ca "It would not have exhausted me so much if I had been in full form."
    show g 29
    mc "Of that, I have no doubt."
    ca "Hmph."
    show g 30
    ca "Now... if you’ll excuse me, I shall retire to my... inn."
    ca "I need to... rest."
    ca "I will recover by tomorrow."
    show g 29
    menu:
        with dis
        "Accompany her to the inn [calypso_pts]":
            $ calypso_interest += 1
            mc "I'm coming with you." with dissolve
            show g 30
            ca "There is no need."
            show g 29
            mc "I won't take a no for an answer."
            mc "This transcends royal protocol, debts, or interests."
            mc "We're in this together, Princess."
            mc "You and me."
            mc "And I'll stand by you until the end."
            if calypso_interest >= 5 and calypsohandjob:
                $ calypsotogether = True
                show g 32
                ca "Hmph."with dis06
                show g 31
                ca "Very well."
                ca "I... appreciate that."
                ca "I must admit, I find solace in knowing I have someone who chooses to stand by my side out of genuine care, rather than mere obligation dictated by royal protocols or interests of power."
                show g 32
                mc "Of course, my Princess."
                mct "It lifts the heart to hear Calypso’s sincerity through her words."
                mct "She must have lived a rather lonely life until now, after all."
                mct "Even before her imprisonment, they've been trying to isolate her and exploit her powers all her life."
                mct "She couldn't afford to show any vulnerability."
                show g 31
                ca "Just remember, if you ever visit Hyril'ar, I will still have to introduce you as my servant."
                ca "For appearances."
                show g 32
                mc "*Chuckle* Fair enough."
                mc "I imagine the other elves might not be too welcoming to a human so close to the Princess."
                show g 31
                ca "Lorelei and some of the other maids might be curious about you."
                ca "But General Arannis and the royal guards? Heh. Not so much."
                show g 32
                mc "Understandable."
            else:
                show g 30
                ca "*Sighs* You can be more annoying than General Arannis himself."
                ca "Okay, you can come."
                show g 29
                mc "Nice!"
        "Go to the Exit Portal":
            mc "Will you be alright?"with dissolve 
            show g 30
            ca "I will, fear not."
            ca "It is not the first time such an incident occured to me."
            ca "In my youth,  I exerted myself so strenuously during training that I slept for five days straight."
            ca "I will be fine."
            show g 29
            mc "Alright then... I'll trust in your resilience."
            mc "I’ll go back to my realm and return to you after all is resolved."
            ca "Mm-hm."
    show g 30
    ca "Before we leave, though... I must ask, how did you get so badly injured?"
    ca "Was your adversary truly so formidable?"
    show g 29
    mc "Uh... well... that's..."
    mc "That's the irony of it all. They weren't. At all."
    mc "They were two nobodies."
    mc "I let my guard down. For a moment I let myself believe I was invincible... when I'm clearly not."
    mc "Fuck... I guess that was a lesson in humility if there ever was one. We can't afford to be careless, not even for a heartbeat."
    show g 30
    ca "So you were defeated in a duel?"
    show g 29
    mc "No, not like that. They attacked me from behind."
    mc "I made the mistake of turning my back – a rookie move, I know – and they pulled a gun."
    mc "Jeez, just the memory of it sends shivers down my spine."
    mc "*Raising your hands theatrically* I was already thinking about something else when suddenly..."
    play sound teleport2
    stop music2
    stop soundloop3
    show teleportalley
    pause 0.6
    play soundloop rain1 
    play music2 ["<silence 3>"]
    queue music2 tension2 fadein 9
    mc "BANG!"
    play sound2 thunder fadein 3
    mc ". . ."
    mc "Wha..."
    mc "W-W-What...?"
    scene g 34
    mc ". . ." with dis17
    mct "This is... Kredon."
    mct "I-I'm back at the alley."
    mct "But... how?"
    cop "You work tomorrow?"
    show g 35
    cap "Nah, I'm free this weekend." with dis12
    cop "Cool, me too."
    show g 36
    cap "Agh, where's the radio?"
    cap "By the time the forensics arrive, the rain will have washed away all the blood."
    cap "Bunch of lazy bastards..."
    show g 35
    mc ". . ."
    show g 39
    bla "You allow the rain to soak your body for a few moments, giving your brain time to process the bewildering experience you're witnessing." with dis2
    mct "I'm back."
    mct "And I'm... completely unharmed."
    mct "Calypso healed my real body...?"
    mct "I entered Eternum... without the E-visor? Without activating the neural implant? Without creating an astral projection...?"
    mct "It was... the real me...?"
    show g 36
    cop "Hey... do you wanna go for a coffee tomorrow?"with dis12
    cop "I heard there's a cheese festival near the church."
    show g 37
    cap "Erm..."with dis
    cap "I appreciate the offer, Mark, but... it wouldn't work out, really."
    cap "You voted for Kilpatrick, and I'm more of a Stabb girl, you know."
    cap "You hate Eternum, and I practically spend all of my..."
    show g 38
    cap ". . ." with dis
    show g 39
    pause 
    show g 40
    cap "Huh...?"
    play sound splash3
    play sound4 whoosh6
    play sound2 switch 
    scene g41 
    cap "*Pulling out her flashlight* W-WHO ARE YOU?!" with hpunch  
    show g 44
    mc "Uh..."
    show g 42
    cop "Eh?"
    show g 43
    cop "What the hell are you–"with dis
    show g 44
    mc ". . ."
    show g 43
    cop ". . ."
    play sound splash3
    play sound4 whoosh6
    play sound2 gunload 
    play sound5 holster
    play sound6 splash2
    scene g45 
    cop "*Pulling out his gun* Oh f-fuck!"with hpunch
    cop "FREEZE! NOW!" with hpunch  
    cop "PUT YOUR HANDS WHERE I CAN SEE THEM!" with hpunch 
    play sound2 whoosh6 volume 0.7
    show g46
    mc "OH GOD, OKAY, OKAY!" 
    mc "I..."
    mc "I-It's not what it looks like!"
    show g 47
    cop "Are you armed?! Drop your weapon! NOW!"
    show g 46
    mc "I'm not armed!"
    mc "I didn't do anything! This is MY blood!"
    mc "I mean..."
    mc "I-I know it sounds impossible, but it's true!"
    show g 47
    cop "Don't try anything stupid or you'll regret it, son!"
    play sound holster2
    cop "NOW, ON YOUR KNEES!" with hpunch
    show g 46
    mc "What?!"
    mc "I..."
    show g 48
    mct "Fuck, fuck, fuck..." with dis06
    mct "I can't afford to get arrested..."
    mct "I have no time for this!"
    mct "And besides, how the hell am I supposed to explain that I'm actually the victim and that it's all a matter of... “MAGIC”?!"
    play sound holster2
    show g 47
    cop "I WON'T SAY IT AGAIN!" with hpunch
    cop "ON YOUR KNEES, NOW!" with hpunch 
    scene g 46
    mc "*Hyperventilating* I'm innocent!"
    mc "*Hyperventilating* (What am I supposed to do now?!)"
    mc "*Hyperventilating* I-I don't..."
    mc "*Hyperventilating* Uh..."
    show 081 with dis08
    pause 0.8
    cop "I SAID FREEZE!{w=1.4}{nw}" with dissolve
    cap "Suspect on the run, move, move!{w=1.4}{nw}"
    mc "Fuck, fuck, FUCK!{w=1.4}{nw}"
    play soundloop forest2
    play sound teleport2
    play sound2 deception
    stop soundloop2
    stop music2
    scene teleportalley2
    pause 0.6
    play sound3 debris2
    play sound4 fallfull
    bla "You suddenly bump into a solid wall of rock." 
    mc "*Hyperventilating* . . ."
    mc "*Hyperventilating* (W-W-What...?)"
    mct "Where am I...?"
    mct "Is this... Ekabar again?"
    mct "What the fuck is going on?!"with hpunch 
    play music2 calypso2
    play sound fallfull
    play sound2 rocks
    play sound3 whoosh6
    play soundloop electricity volume 0.4
    scene calym1b
    bla "In a sudden burst of energy, Calypso pushes you against the wall and conjures an orb that radiates an intense heat on your skin." with hpunch
    show g 50
    mc "C-Calypso??"
    mc "What are you doing?! It's me!"
    show g 51
    ca "You... you can traverse between realms at will!"
    ca "You know the ancient magic!"
    show g 50
    mc "I-I didn't know I could do that!"
    show g 51
    ca "Only those descended from Queen Anima can harness that power!"
    ca "Only us... and those of the bloodline of Yliar the Usurper!"
    show g 50
    mc "W-What?!"
    show g 53
    ca "The Immortals!"with dis 
    ca "Do not feign ignorance!" 
    show g 54
    mc "I-I'm not one of them!"
    mc "Why would I have freed you if I was?"
    mc "You said it was them who locked you up in the first place!"
    show g 53
    ca "It could all be part of a nefarious plan to siphon my powers again, as King Yliar did with Anima thousands of years ago."
    show g 54
    mc "It's not!"
    mc "You've gotta trust me!"
    mc "You..."
    mc "Y-You can see my thoughts, right? Just like you did with Alex when we first met!"
    mc "Do it! You'll see I'm not lying!"
    mc "PLEASE!"with hpunch 
    show g 52
    ca ". . ." with dis
    ca "Hmm..."
    ca "Hmph."
    play sound spell
    stop soundloop fadeout 1
    scene g 55 with dis12
    pause .1
    mc "Oh, thank god..."with dis08
    play soundlow footsteps3 fadein 1 
    show g 57
    ca "*Taking a step back* By the Lord... you are right."with dis15
    ca "I am unable to distinguish a real threat from an innocent anymore."
    ca "I... I must apologize. I suppose that in my current condition I am not as composed as I strive to be."
    show g 56
    mc "You have nothing to apologize for."
    mc "And I meant what I said, you can delve into my mind if that helps."
    show g 57
    ca "There is no need for that. I trust you."
    ca "I am sorry I reacted the way I did. I... need to rest."
    ca "Perhaps more than I thought."
    show g 56
    mc "Believe me, I'm as shocked as you are."
    mc "I don't even know how I'm doing what I'm doing."
    mc "I mean... how did you even find me in the first place?"
    show g 32b
    ca "Well, you simply... materialized beside me, barely clinging to life."with dis 
    show g 32c
    mc "Hmm..."
    mc "I actually remember thinking of you and Eternum in my final moments. Could that be the reason?"
    show g 32b
    ca "Huh..."
    ca "It is possible."
    ca "That is how I conjure my portals too. I have to focus entirely on my destination."
    ca "That is why I need to have physically been in a realm before creating a portal to it."
    show g 32c
    mc "So, if I concentrate on returning to Earth... could I teleport there? Just like that?"
    show g 32b
    ca "Perhaps."
    ca "I would offer guidance, but... I fear I currently lack the strength."
    show g 32c
    mc "Of course, we can leave it for later."
    mc "You've already done more than enough."
    mc "Thank you again for saving my life, Calypso."
    mc "I'm forever in your debt."
    play sound3 spell3
    play sound2 spell2
    play soundloop2 energy2 fadein 1
    scene g 32d with dis12
    ca "No more debts." with dis06
    if calypsotogether:
        ca "We are in this together now, remember?"
        ca "You and me."
        ca "And I will stand by you until the end."
        show g 32d2
        mc "Thank you, my Princess."
    else:
        ca "Our paths have merged now. Our destinies are already entwined."
        show g 32d2
        mc "I can't argue with that."
    show g 32d
    ca "I will return to the inn by myself, do not worry about me."
    ca "Will you be alright on your own?"
    show g 32d2
    mc "I'll manage. I need to compose myself somehow and get back to the real world as soon as possible."
    mc "Then back to the New World server to continue our mission."
    mc "We're really close to obtaining another Gem of Doom."
    show g 32d
    ca "I see..."
    ca "I look forward to hearing of your success."
    ca "Farewell, [mc]."
    show g 32d2
    mc "Farewell, my Princess."
    play sound3 spell3
    play sound2 spell2
    stop soundloop2 fadeout 1
    show g 57b with flashfast
    pause  
    play sound5 ["<silence 0.3>", fall2]
    play sound6 ["<silence 0.4>", debris]
    show g 58 with dis2
    bla "As Calypso departs to rest, you take a moment to catch your breath, sinking down onto the very rock where you first awoke." with dis
    mc "*Taking a deep breath* . . ."
    show g 59
    mc "*Exhaling* Fuuuu..." with dis06
    show g 58
    mct "My brain is a damn whirlwind right now, but I need to take a second to clear my mind and block everything else out."with dis08 
    mct "I managed to go back to that alley before, when my emotions were hitting me like a tidal wave."
    mct "If I concentrate hard enough, maybe I can recreate that moment."
    show g 59
    mc "*Exhaling* Fuuuu..." with dis06
    show g 58
    mct "Just think about it, [mc]. Over the last four months you've seen some crazy stuff. Stuff you would have never believed before."with dis08
    mct "This is real. All that's happening to you. You've gotta believe you can do it."
    mct "Just like when you activate your powers and transform in Eternum."
    mct "If I managed to control that power, then surely this is within reach."
    scene black
    mc "*Keeping your eyes closed* (I can feel the ground beneath me.)"with dis15
    stop music2 fadeout 22
    mct "I can hear the birds chirping, the bugs buzzing, the river flowing across the valley."
    play soundloop rain1 fadein 22
    play soundloop2 rain3 fadein 23
    mct "I can see Kredon."
    mct "I can hear the rain tapping on the windows."
    mct "I can smell Nancy's homemade cookies."
    mct "I can practically taste them."
    mct "I can..."
    mct "Feel the cold water on my feet..."
    play sound thunder fadein 3
    scene g 60 with dis3
    play music2 tension2 fadein 7
    mc "*Opening your eyes* (Oh my god...)" with dis15
    mct "Unbelievable..."
    mct "I... fucking did it..."
    mct "We need to investigate this further. If I no longer need the neural implant to access Eternum, maybe I can remove it altogether."
    mct "What if the Founder was tracking my movements through it...?"
    show g 61 with dis15
    mc "*Turning around* (Although I need to learn to control it better first.)"with dis12
    mct "I was trying to focus on Nancy's house, but I still appeared on the same exact spot where I left. Maybe I need more practice?"
    cop "The area is cordoned off, Sergeant."
    mct "But all that can wait..."
    play sound thunder fadein 2
    scene g 62 with dis2
    bla "You quietly approach the spot where you first materialized, where a pool of blood still stains the ground as a stark reminder of how close you came to death." with dis 
    scene g 63
    cops "So... let me recap."
    cops "The suspect was observed at the crime scene, but there's no sign of the victim or the weapon used."
    cops "He's described as a white male, muscular build, between 5'9'' and 6', with brown, medium-short hair. Possibly in his early 20s."
    cops "He attempted to flee, initiating a pursuit, but you lost visual contact shortly thereafter."
    show g 64
    cap "We didn't just lose him, he VANISHED!" with dis08
    cap "There's no conceivable way he could have scaled a wall that quickly!"
    cop "She's right, we rounded the corner literally one second after he did!"
    cops ". . ."
    show g 65
    cops "*Writing it down* Sure... he {i}vanished." with dis12
    mct "Damn, I was lucky... if I had ran into them again, I would have been in some serious trouble."
    mct "I better sneak out while I still can."
    if novapath:
        mct "I'll go back to Nova's and try to reassess the situation."
    else:
        mct "I think Nova lives nearby. I'll go to her place and try to reassess the situation."
    cops "Jackson, go check the area where the suspect... “vanished”."
    mct "Time to go."
    stop music2 fadeout 5
    stop soundloop fadeout 7 
    stop soundloop2 fadeout 7
    scene black with dis22
    show screen afewminuteslater with dis15
    pause 
    play sound carpasswet
    play soundloop3 rain1 fadein 6
    scene g 67 
    hide screen afewminuteslater
    with dis22
    mct "Phew, at least I managed to slip away without being seen."with dis12
    mct "I'm not setting foot in Chinatown ever again, that's for sure."
    mct "And maybe I should stop ordering pizza too. It seems like every time I do, something bad happens... for some reason."
    if not novapath:
        mct "Thank god Nova's place was close..."
    play sound3 dooropen1
    play sound6 ["<silence 1.6>", doorclose]
    stop soundloop3 fadeout 3
    play soundloop rain3 fadein 3
    play sound4 drips
    scene fe 16 with dis17
    if novapath:
        mc "*Closing the door behind you* Nova, I'm back!" with dis12
        no "*From upstairs* FINALLY!"with hpunch
    else:
        mc "*Closing the door behind you* Nova, I'm here!" with dis12
        mc "Did you see my last message? Thank you for letting me come, really!"
        bla ". . ."
    mc "You're not gonna believe what happened to me!"
    mc "I..."
    scene g 69
    mct "Hmmm... should I explain everything to her now?" with dis15
    mct "Or do I wait till we're done with the New World server?"
    mct "Right now, nabbing the Heart of the Abyss is priority number one, and perhaps all this new info is too much to digest for her. I don't wanna overload her."
    show g 70
    mct "I can tell both her and Nancy once we've successfully gotten to the Island of the Lost Souls."with dis12
    mct "Might even help me stay focused as well."
    show g 71
    mct "I've gotta go back to Tortuga to find a new crew member to join us and set sail tow–"with dis12
    play sound7 whoosh3b
    play sound teleport2
    play sound2 deception
    stop soundloop 
    scene teleportalley3
    play soundloop ["<silence 0.6>"]
    queue soundloop waves
    play sound3 ["<silence 0.6>", seagull]
    if novapath:
        no "Missed you!" with hpunch
    else:
        no "BOO!" with hpunch 
    play music2 piratequirky
    scene g 74
    mc ". . ." with dis12
    no ". . ."
    no "Eh?"
    play sound7 wood2
    scene g 75 with dis2
    bla "Nova slowly dismounts from your back and walks silently to the edge of the dock, her expression unreadable." with dis
    no ". . ."
    mc "D-Did we just..."
    no "This is... Tortuga."
    mc "*Looking around* Y-Yes, I think so."
    no "We're in the New World server."
    mc "...yeah."
    no "My house is... not in the New World server."
    play sound impactwood
    play sound3 whoosh3b
    scene g 76
    no "*Turning around* W-What the fuck is going on?!" with hpunch
    show g 77
    mc "Erm... o-okay, I kinda planned to ease into this, but... I guess it's too late for that now."
    show g 76
    no "Ease into what?!"
    show g 77
    mc "Um..."
    mc "Jeez, I-I don't even know where to start."
    mc "Ehh... yeah, so, here's the thing. I've got pretty solid evidence to believe that... I can get into Eternum without using the neural implant."
    show g 76
    no "You can... WHAT?!" 
    show g 77
    mc "Yeah, and judging by what just happened... seems like I can even bring someone along with me."
    show g 76
    no "*Hyperventilating* We're in Eternum?! HOW? Why?! Are our real bodies still at my place? DID YOU LOCK THE DOOR?! *gasps* WHAT IF THERE'S A RAPIST IN THE NEIGHBORHOOD?! WHAT IF–"
    show g 77
    mc "O-Okay, I can explain it all from the beginning, but you need to chill out!"
    show g 76
    no "*Hyperventilating* OKAY."
    show g 78
    no "O-Okay... okay. I'm calm. I've calmed down."with dis
    show g 79
    mc "You sure? "
    show g 78
    no "Y-Yes. S-Sorry. It was just the initial shock."
    show g 79
    mc "Alright, cool. I'll try to explain everything from the beginning."
    show g 78
    no "Great. I'm calm."
    show g 79
    mc "*Taking a deep breath* Alright..."
    if novapath:
        mc "Remember how I said I was gonna take a shortcut through Chinatown?"
        no "Mm-hm."
    else:
        mc "Remember that break we took to grab a bite?"
        mc "Turns out... I decided to pick up a couple of pizzas for Nancy and me."
        mc "And I decided to take a shortcut through Chinatown."
        mc "And then..."
    mc "Well, things went south real fast, and... I ended up getting shot."
    play sound impactwood
    play soundlow impact5
    play sound2 seagull
    play sound3 splash3
    show g 80
    no "{sc=2}AAAAAAAAAAAAAAAAGGGGHH!!!{/sc}" with hpunchlong3
    show g 81
    mc "YOU SAID YOU WERE CALM!"
    show g 80
    no "WE WERE SHOT AND NOW OUR SOULS ARE TRAPPED IN ETERNUM!" with hpunch 
    show g 81
    mc "I didn't say that!"
    show g 80
    no "WE WERE MURDERED AND NOW A HOBO IS RAPING OUR BODIES!" with hpunch
    show g 81
    mc "NO ONE IS BEING RAPED!" with hpunch 
    play sound wood2
    show g 82
    if novapath:
        n "Oh, it's really you, guys! Right on time!" with dis12
    else:
        n "Oh, it's really you, guys! I didn't even hear you coming back, [mc]." with dis12
    $ unlock_look("nancy", 12)
    mc "Nancy!"
    n "What's with the yelling?"
    show g 80
    no "[mc!u] AND I WERE KILLED AND ARE NOW MINDLESS NPCs!" with hpunch
    no "RUN WHILE YOU CAN, NANCY!" with hpunch 
    show g 81
    mc "WE'RE NOT NPCs!"
    show g 83
    n "Eh?"
    mc "D-Don't listen to her!"
    mc "S-Something big happened, that's true, and I need to explain it to you, b-but first–"
    show g 80
    no "F-FUCK, I THINK THE FOUNDER IS ALREADY TAKING CONTROL OF MY NPC SOUL! I CAN FEEL IT!" with hpunch
    no "RUN BEFORE IT'S TOO LATE!" with hpunch
    no "HE'S ORDERING ME TO MURDER YOU!" with hpunch
    show g 81
    mc "Goddammit Nova, stop making things up!" with hpunch
    show g 84
    n "Oooookay..."with dis
    n "Looks like we're all a bit on edge here."
    n "But, lucky for you, I know just the perfect fix... yoga!"
    show g 85
    mc "W-What?"
    mc "Yoga?"
    show g 76
    no "Y-Yoga?"
    show g 84
    n "Just follow my lead! Your body will loosen up, and your mind will chill out."
    n "No questions, just trust me!"
    show g 85
    mc "But you don't understand, we logged–"
    show g 84
    n "Ah, ah, ah! No talking until we're all zen."
    n "Just let yourselves be transported by the sound of the waves and my voice!"
    show g 85
    mc "But..."
    n ". . ."
    mc "O-Okay, if you say so..."
    show g 84
    n "First movement, the tree pose or vrksasana."
    n "Come on, everybody on one foot!"
    stop music2 fadeout 4
    scene black with dis22
    show screen afewminuteslater with dis17
    pause
    scene g 86 
    hide screen afewminuteslater
    with dis22
    play music2b yoga fadein 12
    play sound seagull2
    pause
    scene g 87
    mc "Mmmmmhh..." with dis15
    mct "Damn, she wasn't kidding – this really felt relaxing."
    mct "Both for my body and my mind."
    show g 88
    mc "So anyway, in conclusion, the whole Eternum trip with Nova seems to indicate that I can bring someone along with me."with dis14
    mc "Seemingly only if they're touching me at the moment I “teleport”."
    show g 88c
    mc "I can't access Ulysses' inventory, but... the Gems of Doom still magically appeared in my pocket – just like Dione did with Nova." with dis15
    mc "Almost like... these items were connected to us somehow?"
    show g 88
    mc "Still figuring out the logistics of the whole thing, though. Seems like I'm stuck appearing wherever I last vanished." with dis14
    mc "Happened both here and in that alley back in Kredon."
    show g 89
    pause
    show g 90
    n "*Exhaling* Fuuuu..." (multiple=2) with dis08
    no "*Exhaling* Fuuuu..." (multiple=2)
    play sound2 wood
    play sound3 wood2
    scene g 91
    no "Yeah, that makes perfect sense." with dis15
    show g 88b
    mc "Does it...?"
    show g 91
    no "Of course."
    no "We've known for a while that Eternum isn't just a video game, but a whole dimension where we can create astral projections of ourselves."
    show g 92
    n "The neural implant made it accessible to everyone, but people with an extraordinary compatibility like [mc] are probably able to enter Eternum without it."
    show g 91
    no "All the bleeding cases reported by different users around the world, including [mc], have probably been brief trips to Eternum, and not just mere “hallucinations” as commonly believed."
    show g 92
    n "Shocking revelation, yet... oddly soothing at the same time."
    n "I should have seen this coming sooner."
    show g 88b
    mc "Uh..."
    show g 88
    mc "Yeah..." with dis15
    mc "Yes."
    mc "I don't know if it's Nancy's yoga or what... but suddenly all this craziness sounds like the most logical thing ever."
    show g 92
    n "In any case, our goal stays the same."
    n "We need to collect the ten Gems and free all the NPCs from Ulysses' grip."
    show g 91
    no "Exactly!"
    show g 92
    n "So..."
    n "Ready to continue our mission?"
    play sound wood
    play sound2 impactwood 
    play sound3 woodhit
    play music2b piratequirky
    play sound7 seagull
    scene g 93
    no "*Standing up* NEVER BEEN READIER!" with vpunch 
    no "We need to assemble a new crew and set sail towards the Island of the Lost Souls ASAP!"
    no "LET'S GO!"with hpunch 
    play sound2 whistle4 volume 0.7
    pi1 "*Whistling* AHOOOOOYYYY ! ! ! !" with hpunch 
    pi1 "WHY DON'T YOU COME JOIN US FOR A DRINK, YOU SEXY PEACH?!"
    show g 94
    no "Oh shit, I f-forgot I'm in my underwear!" with dis
    no "Oh my god, why didn't you tell me?! How embarrassing!"
    show g 95
    n "*Giggles* Actually... you two showing up here half-naked turned out to be quite fortuitous!"
    n "I just happened to pick up some new clothes for you both!"
    show g 88
    mc "For real?"
    show g 95
    n "Yep! I got here a bit earlier than planned and spotted a cute little boutique... I couldn't resist!"
    n "Do you wanna try them on?"
    no "Oh, please, please, please!"
    play sound clothes5
    play sound2 clothes4
    play soundlow tear1
    scene g 96 with dis2
    $ unlock_look("nova", 15)
    no "*Gasps* Whoaaaaaaaa!" with dis12
    no "This is so beautiful!"
    show g 104
    n "I knew this skirt would be perfect for you!"
    n "It really accentuates your legs and waist, and the color complements your hair beautifully!"
    show g 98
    n "Do you like yours, [mc]?" with dis
    if nancypath:
        n "I chose this shirt because it highlights your... well-toned torso."
    mc "Love it! It's stylish and fresh at the same time!"
    if novapath:
        n "Don't you think [mc] looks super hot with this, Nova?"
        no "E-Eh? M-Me?"
        no "I mean... y-yeah! Super hot..."
        if nancypath:
            n "Right...?"
    show g 99
    mc "Where did you find these?"with dis
    mc "I feel like I've seen Nova's skirt somewhere before..."
    scene g 101
    play sound pop
    show wenlinpen
    n "I told you, in a boutique I found near the tavern!"
    n "There was a pretty girl there with green hair, about the same size as Nova, wearing this same skirt."
    n "I couldn't resist asking her where she got it, and next thing I knew, I had bought a whole new outfit for both of you."
    n "That girl sure knows how to make a sale!"
    show g 100
    mc "I think I know who you're talking about..."
    mc "Was this girl with a short Asian man, by any chance...?"
    play sound4 seagull2
    play sound pop
    show g 102
    show chopchoppen
    n "Now that you mention it..."
    n "Yeah, there was this weird guy with her, carrying around some bizarre, phallic artifacts. He claimed they were magical or something."
    n "Didn't buy anything from him, though."
    show g 103
    mct "Well, that pretty much confirms I'm the only sucker buying Chop-Chop's weird stuff."
    if polyjuicebuy:
        mct "I just hope that polyjuice potion I bought doesn't turn me into some giant penis if I ever use it..."
    else:
        mct "I just hope the map they sold me doesn't lead us to some dead end..."
    scene g 99
    mc "But hey, in any case, the outfits are awesome!" with dis12
    mc "Thanks a bunch, Nancy."
    show g 96
    no "I couldn't agree more!" with dis
    no "Thanks a million, Nan! I owe you one!"
    show g 104
    n "Don't worry about it."
    n "I'll consider it even if you manage to find a new crew member."
    show g 97
    mc "Ah, true! I bet there are some eager sailors already waiting for me at the tavern!"
    mc "Shall we go now?"
    show g 104
    n "Yes!"
    n "Let's split up and check the spots where we hung the signs, then meet again at the ship in 30 minutes!"
    n "With each of us bringing aboard a new crew member, we'll be set to sail!"
    play sound wood2
    show g 106
    no "Noice! Sounds like a plan!"with dis
    no "Catch you all in 30 minutes back at the ship!"
    no "I'll make sure to bring the BEST sailor in all of Tortuga!"
    mc "Not if mine is better!"
    play sound twirl 
    show novawavetortuga
    no "Bye guys!"
    mc "See ya!"
    scene g 107 with dis17
    bla "Nancy and Nova walk towards the dock and move to their respective recruit spots." with dis12
    mct "Man, Nancy's gift for soothing us in moments of crisis is unmatched."
    mct "She not only calmed Nova but also managed to ease my nerves effortlessly."
    mc "*Sighs* (Still, I can't let that overshadow what just happened.)"
    mct "I need to remain vigilant at all times. Even the slightest threat could end it all if I let my guard down."
    mct "There's too much at risk now, [mc]."
    mct "It's not just your life hanging in the balance anymore."
    play sound footsteps3
    stop music2b fadeout 8
    scene fd 4 with dis22
    mct "Ah, the WRE's ship is still anchored behind the tavern, just a 4-minute stroll away." with dis
    mct "I've got plenty of time to decide who to recruit."
    mct "I better steer clear of the shop in case Chop-Chop's still around, though..."
    play sound saloondoors
    stop soundloop2 fadeout 2
    stop soundloop fadeout 2
    play musicb piratetavern fadein 3
    scene gg 1 with dis2
    bla "You step into the tavern, the scent of aged wood, liquor, and smoke welcoming you back like an old friend." with dis
    mct "Hmm... I can't help but constantly glance around every corner or turn around every few seconds."
    mct "Guess it'll take a while for this paranoia to wear off."
    show gg 2
    mct "In any case, I won't make the mistake of turning my back on an enemy again. I must be there to protect the girls."
    if nancypath:
        $ haremnumber += 1
    if anniepath:
        $ haremnumber += 1
    if daliapath:
        $ haremnumber += 1
    if penelopepath:
        $ haremnumber += 1
    if alexpath:
        $ haremnumber += 1
    if lunapath:
        $ haremnumber += 1
    if novapath:
        $ haremnumber += 1
    if haremnumber >= 3:
        show gg 1
        mc "*Exhales* (Being on the brink of losing everything made me realize how much I love them. ALL of them.)"
        mct "This whole thing has really opened my eyes."
        mct "Although... I honestly don't know how I'm supposed to handle this situation."
        mct "I'm no harem-owning sheikh. I think I need to have some serious conversations before anyone gets hurt."
        mct "Hmm, maybe I should start by opening up about how I feel about them."
        mct "I need to let them know I love them."
    tav "Mr. [mc]?"
    show gg 3
    mc "Hmm?" with Dissolve(.7)
    show gg 4
    tav "Are you here to hire that new crew member?"
    show gg 5b
    mc "Yes, sir."
    mc "Any interest?"
    show gg 4
    tav "There are three waiting."
    tav "You can talk to them and decide who you want to take with you."
    show gg 5b
    mc "Damn, only three...?"
    mc "I was hoping for at least... a dozen."
    show gg 4
    tav "I told you the journey to the Island of the Lost Souls is practically a death sentence."
    tav "You're lucky you got three."
    show gg 5b
    mc "*Sighs* I guess so..."
    mc "Well, let's hope one of them fits the bill. We need to leave immediately."
    show gg 4
    tav "You can take a seat over there. I'll send them your way."
    show gg 5
    mc "*Looking at the empty table* Sure."
    mc "Thank you for your help."
    show gg 4
    tav "Anytime. Goldtooth's friends are my friends."
    show gg 6 with dis2
    play sound chair2
    mc "*Taking a seat* (Would you look at that, being Chop-Chop's friend is actually proving to be useful. Who would've thought.)" with dis 
    play sound3 chairmove
    play sound2 ["<silence 0.6>", chair2]
    show gg 7
    reds1 "*Sitting down* Mr. [mc], I presume?" with dis
    reds1 "Blackheart Reds at your service, the finest pirate in all of Tortuga."
    show gg 8
    mc "Ah, nice to meet you, Mr. Reds."
    show gg 9
    reds2 "Please, it's “ReDDs” with two Ds. Like, stretching the sound with your tongue."with dis
    reds2 "Just one D brings terrible luck."
    show gg 8
    mc "Oh, sorry. Nice to meet you, Mr. Redds."with dis
    show gg 10
    reds "Oh no, no! ReddSS, with two Ss too!" with dis
    reds "Dragging the D but not the S brings even worse luck!"
    show gg 8
    mc ". . ." with dis
    mc "...Nice to meet you, Mr. Reddssssss."
    show gg 7 
    reds "Pleasure's all mine."
    show gg 8
    mc "So... yeah, any questions about the job?"
    show gg 7
    reds "Back and forth to the Island of the Lost Souls, and we can snag whatever treasures we find, is that correct?"
    show gg 8
    mc "Except for the Heart of the Abyss. I need that for myself."
    show gg 7
    reds "Got it."
    reds "Ready to set sail whenever you give the word."
    show gg 9
    reds "As long as we don't have any bananas or cats on board, of course."with dis
    reds "Very bad luck, you know it."
    show gg 8
    mc "No... I don't think we have any on board."with dis
    show gg 7
    reds "In that case, I'm your man."
    show gg 8
    mc "Anything special you can bring to the table?"
    show gg 7
    reds "Well, to begin with, I'm the top cook in the New World server!"
    show gg 8
    mc "Oh, a chef, huh?"
    mc "*Chuckles* Do you also want to find the All Blue?"
    show gg 9
    reds "P-Please, don't do that!"with dis
    reds "One Piece references bring very, VERY bad luck in this server."
    reds "No Gomu Gomu no Pistols, no Peter Pan jokes, and especially NO Jack Sparrow quotes."
    show gg 8
    mc "Oh... o-okay, I'll keep that in mind."with dis12
    mc "Anyway... anything else?"
    show gg 7
    reds "Oh, I'm also quite the magician!"
    reds "Do you wanna see a trick?"
    show gg 8
    mc "It's okay, that won't be necessa–"
    play sound shuffle
    show gg 12
    reds "Pick a card." with dis
    mc "Um..."
    reds "Just choose one. No need to touch them."
    mc "Uh..."
    mc "Alright, done."
    play sound2 shuffle
    show gg 7
    reds "*Shuffling the cards behind his back* Actually, I lied."with dis 
    reds "I'm not the magician here."
    play sound whoosh3b
    show gg 13
    reds "Mr. Paws is!"with dissolve 
    play sound2 smokebomb
    show gg 14
    reds "EH?! WHERE DID HE GO?!"with flashfaster
    reds "Wait..."
    reds "Could he be looking for..."
    play sound3 smokebomb
    show gg 15
    reds "Your card?"with flashfaster
    show gg 16
    menu:
        with dis
        "Yes{#0.8,magic}":
            mc "Wow! It {i}is{/i} my card!" with dissolve 
            mc "Impressive!"
            show gg 7
            reds "Hehe, thank you, thank you..."with dis
            reds "As you can see, both my mind reading and my hand speed are on point."
        "No{#0.8,magic}":
            mc "Um... nope."with dissolve 
            reds ". . ."
            show gg 7
            reds "Well, I'm still working on the mind reading bit, but the hand speed is on point, as you can see." with dis
    play sound4 smokebomb
    show gg 17
    reds "AHA!" with flashfaster
    reds "Check this out! A sea urchin cake right out of the oven!"
    reds "You've got to taste it!"
    mc "Um... y-yeah, maybe later."
    mc "Thanks, though."
    show gg 7
    reds "I'll save it for later. It's delicious even when cold."with dis 
    show gg 8
    mc "I've gotta interview a couple more pirates now. I'll call you if you're chosen."
    show gg 7
    reds "Very well. Thank you for the opportunity."
    reds "I'll be in the kitchen whipping up another delectable cake."
    show gg 8
    mc "Ah, sounds good! Good lu–"
    show gg 10
    reds "Shh, shhh! Wishing good luck brings very ba–"with dis
    show gg 11
    mc "YEAH, YEAH, EVERYTHING'S BAD LUCK, I GET IT!"with hpunch 
    mc "THANK YOU, SEE YOU LATER!"
    play sound chairmove
    show gg 6 with dis15
    mct "Man, he's quite the character." with dis
    mct "Although it's true he's lightning-fast with those hands."
    play sound3 chairmove
    play sound2 ["<silence 0.6>", chair2]
    show gg 18
    lor1 "*Sitting down* Ahoy, Mr. [mc]! Lordy Silverhook at your service!" with dis
    lor1 "Let's sail before the sun dips below the horizon!"
    show gg 19
    mc "Ah, nice to meet you."
    mc "Just Lordy, right? Not LorDDy or LoRRdy?"
    show gg 19b
    lor1 "LoRRdy..."
    lor1 "Aye, I like the sound of that."
    lor1 "Adds a touch of pirate flair, like a hearty “Arrrrr”!"
    show gg 18
    lor "Aight! From this moment forth, I be Lorrdy Silverhook!"
    show gg 19
    mc "Um... sure, let's get straight to it..."
    mc "What would you bring to the crew?"
    show gg 20b
    lor "Well, to begin with, you're getting two for the price of one!"with dis
    lor "Myself, and my matey Iago!"
    lor "Together, we're the TOP team of navigators in all of Tortuga!"
    lor "Isn't that right, Iago?"
    play sound parrot
    scene iago1
    iag "Best navigators!"
    scene gg 20b
    lor "If there's something out there on the ocean, we can find it!"
    show gg 19
    mc "Hmm, that sounds very useful."with dis 
    mc "Anything else?"
    show gg 19b
    lor "Anything... else...?"
    show gg 18b
    iag "*Whispering*" with dis08
    show gg 18
    lor "Ah, yes, yes, of course! I'm a man of many talents!" with dis08
    lor "I've got a whole array of skills! A whole array!"
    show gg 19
    mc "Such as?"
    show gg 23
    lor "Well, first off, I'm an exceptional navigator." with dis 
    mc "Yeah... you mentioned that already."
    show gg 24
    lor "Secondly, I have a way with all kinds of animals."with dis08
    lor "Parrots, iguanas, manatees, or even sharks!"
    mc "Nice."
    show gg 25
    lor "Thirdly, I can hunt all kinds of animals."with dis08
    scene fd 6
    lor "Do you see that mermaid skeleton?"
    lor "I snagged it myself with a pointy stick!"
    mc "That took an unexpected turn..."
    scene gg 26
    lor "Fourth, I'm a connoisseur of rum and whiskey."
    lor "I can differentiate them by taste alone!"
    mc "Can't anyone who's tried them at least once...?"
    show gg 27
    lor "And fifth but not least, I'm also a superb navigator."with dis08
    mc "You already said that!"with hpunch
    show gg 18
    lor "Believe me, mate, I'm a highly sought-after pirate in Tortuga."with dis12
    lor "I agreed to venture to the Island of the Lost Souls to etch my name not just on Tortuga's boards, but throughout the New World server."
    lor "Take me on, and you won't be disappointed."
    play sound parrot
    scene iago2
    iag "Won't regret it!"
    mc "Okay, um..."
    mc "Before making any decisions, I've gotta interview one last person."
    mc "I'll let you know if you're chosen."
    play sound parrot
    scene iago3
    iag "Choose Iago!"
    scene gg 18
    lor "We'll be right at the counter."
    lor "Thank you for your time!"
    play sound chairmove
    show gg 6 with dis15
    mct "Well... that makes two." with dis
    mct "His navigator skills could be quite useful, that's for sure."
    mct "Hmm... I should wrap this up as quickly as I can and–"
    play sound3 chairmove
    play sound2 ["<silence 0.6>", chair2]
    show gg 28
    scar "*Sitting down* Hi, handsome... I'm Red Scarlet." with dis
    show gg 29
    mc "Oh my..."
    mc "Uh, hi Scarlet."
    show gg 28
    scar "I'm here about the job offer."
    scar "The sign promised riches beyond measure... is that correct?"
    show gg 29
    mc "Indeed. You can keep anything we find, except for the Heart of the Abyss."
    mc "But before we continue, I just have a couple of questions..."
    show gg 30
    scar "*Giggles* Yeah, they're all natural."
    show gg 29
    mc "Um... t-that's good to know, but actually, I was gonna ask..."
    mc "What are your best skills for the mission?"
    show gg 30
    scar "Well..."
    scar "I give really, {i}really{/i} good blowjobs."
    show gg 29
    mc ". . ."
    mc "Mm-hm."
    mc "G-Good."
    mc "And... anything related to sailing?"
    show gg 31
    scar "Oh!"
    scar "Ehh..."
    scar "Well, I know the basics."
    scar "Wind, waves, skull flags... you know."
    show gg 28
    scar "Ah, and the ships have cannons!"
    show gg 29
    mc "Mm-hm."
    mc "That's a fact."
    mc "Anyway... that would be all, I think."
    mc "Thank you for your time, Scarlet."
    mc "I'll be in touch if you're selected."
    show gg 28
    scar "I'll be over there touching up my makeup."
    scar "Can't wait to be a part of your crew, [mc]..."
    play sound chairmove
    show gg 6 with dis15
    mct "Well..." with dis
    mct "I guess it's time to decide and go back to Nancy and Nova."
    mct "We've got a superstitious magician chef, a navigator with a parrot, and a lady with some... “skills”."
    mc "Hmm..."
    call screen piratecrew with dis14
label piratecrewreddss:
    $ reddss = True
    scene crewidle
    pause 0.001
    scene gg 6
    mct "Hmmm... I think I'm gonna go with him." with dis
    mc "Uh... Mr. Reddss?"
    play sound whoosh6
    play sound2 plate
    scene gg7
    reds "Yes, sir?" with pl
    scene gg 8
    mc "You're coming with me."
    mc "We're departing for the Island of the Lost Souls right away."
    show gg 7
    reds "Ah, excellent decision, sir, excellent!"
    reds "Just say the word, I'm ready to set sail!"
    show gg 8
    jump postchoicepir
label piratecrewlorrdy:
    $ lorrdy = True
    scene crewidle
    pause 0.001
    scene gg 6
    mct "Hmmm... I think I'm gonna go with him." with dis
    mc "Uh... Mr. Lorrdy?"
    play sound whoosh6
    play sound2 plate
    scene gg18
    lor "Right here, sir." with pl
    scene gg 19
    mc "You're coming with me."
    mc "We're departing for the Island of the Lost Souls right away."
    show gg 18
    lor "YES!"
    lor "You've made the wisest decison!"
    play sound parrot
    scene iago2
    iag "Wise [mc], wise [mc], yes!"
    scene gg 18
    lor "We're ready to set sail whenever you're ready!"
    show gg 19
    jump postchoicepir
label piratecrewscarlet:
    $ scarlet = True
    scene crewidle
    pause 0.001
    scene gg 6
    mct "Hmmm..." with dis
    mct "Yes."
    mct "It's the logical choice."
    mc "Uh..."
    mc "Ms. Scarlet?"
    play sound whoosh6
    play sound2 plate
    scene gg28
    scar "Yes...?" with pl
    scene gg 29
    mc "You're coming with me."
    mc "We're departing for the Island of the Lost Souls right away."
    show gg 28
    scar "You won't regret it..."
    scar "I'm ready whenever you are, love."
    scene gg 29
    jump postchoicepir
label postchoicepir:
    mc "Let's not wait another second, then."
    mc "To the ship!"
    stop musicb fadeout 5
    scene black with dis22
    show screen afewminuteslater with dis15
    play soundloop waves fadein 4
    pause 
    hide screen afewminuteslater 
    scene gg 32 
    with dis22
    play music2 pirate1 fadein 7
    play sound seagull2
    no "*Waving* [mc], over here!"with dis12
    mc "*Waving back* Hey there!"
    if reddss:
        play sound whistle3
        reds "*Whistles* That's a big boat."
    elif lorrdy:
        play sound whistle3
        lor "*Whistles* Look at the size of that ship!"
    else:
        scar "That's a big ship... *giggles* compensating much...?"
        mc "Of course not!"
    no "Come on, hurry up!"
    mc "Coming, coming!"
    play sound stairswood2
    play sound2 wood2
    scene gg 34 with dis17
    mc "*Walking up the gangplank* Is everyone ready?" with dis08
    show gg 33
    no "Ready to set sail at your orders, Quartermaster!"
    show gg 34
    mc "Do we have enough crew members to manage the ship?"
    show gg 33
    no "We do!"
    no "I found the BEST sailor in all of Tortuga!"
    show gg 34
    mc "*Chuckles* Oh, did you?"
    show gg 33
    no "Absolutely!"
    no "I present you..."
    play sound whoosh3b
    show gg 35
    no "Tartaria-san!" with pl 
    tar "Good evening."
    play sound wood2
    show gg 36 with dis12
    mc "Nice to meet you, sir. My name's [mc]." with dis
    show gg 37
    tar "You can call me Mr. Tartaria."
    tar "Forgive me for not revealing my real name, one can never be sure someone else isn't a secret agent of the NWO."
    show gg 36
    mc "The what?"
    show gg 37
    tar "NWO. The secretive global elite that controls the world."
    show gg 36
    mc "Ah... yeah."
    mc "I call them “Ulysses”. Heh."
    show gg 39
    tar "Oh, you fool... Ulysses is just one tentacle of the Satan-worshipping, pedophile cabals that form the NWO."with dis14
    tar "We must expose them before the next great reset, when they plan to restructure society as we know it today."
    tar "WAKE. {w=0.2}{size=49}UP."
    show gg 38
    mc "Yeah..."
    mc "I-I was just... making a joke with the Ulysses thing."
    show gg 39
    tar "At least you can afford to joke here – luckily, there are no birds."
    show gg 38
    mc "Birds...?"
    show gg 39
    tar "Oh, so blind..."
    tar "Have you ever seen a baby pigeon in the real world, my child?"
    show gg 38
    mc "I'm sorry...?"
    show gg 39
    tar "Pigeons and other birds are nothing but surveillance drones controlled by the New World Order."
    tar "That's why we're actually safer inside Eternum than out there."
    show gg 38
    mc "Um..."
    show gg 37
    tar "You need to start asking yourself questions, [mc]."with dis14
    tar "Seek the truth!"
    show gg 36
    mc "I-I will."
    mc "Thank you."
    show gg 37
    tar "You know, since we're already on the topic... have you ever wondered which celebrities are actually reptili-"
    play sound whoosh3b
    play sound7 woodhit
    show gg40
    no "O-OKAY, that's enough! Thank you, Tarta!"with pr 
    no "*Whispering* Um... yeah, as you can see, he's a little bit... eccentric."
    no "But he's a good sailor! He knows the waters!"
    play sound2 stairswood2
    play sound3 wood2
    scene gg 41
    n "*Climbing down the stairs* Ah, looks like we're all set!" with dis15
    mc "Hey Nancy!"
    mc "Ah, is this man another one of our new recruits?"
    zap "ZAP!" with hpunch 
    show gg 43
    zap "You must be [mc]. You can call me Zap, a pleasure."with dis
    zap "I have 25 years of experience fishing in both fresh and saltwater."
    zap "I've caught specimens in oceans all around the globe, including 16 different servers of Eternum!"
    show gg 37
    tar "*Snorts* The “globe”?"
    tar "Interesting name for something that's actually shaped like a cube."
    tar "The Elite wants us to believe that–"
    play sound7 woodhit
    show gg 36
    no "SHUT UP!" with hpunch 
    show gg 42
    n "Zap has captained his own ship for 15 years."
    n "I'm sure he'll be a great asset for our short journey."
    show gg 43
    zap "It's been a dream of mine to visit the Island of the Lost Souls since I first discovered this server."
    zap "You have my expertise at your disposal."
    if reddss:
        show gg 47b
        reds "Wait, wait, wait..."with dis12
        reds "T-Two women on board?!" with hpunch 
        reds "Oh no, this is terrible."
        reds "Absolutely TERRIBLE luck."
        reds "This journey is doomed to failure before starting!"
        show gg 54
        n "Hello mate!"
        show gg 47b
        reds "P-Please, don't talk to me."
        show gg 55
        n "I... believe if the woman on board speaks to you directly, it neutralizes the curse."
        n "Am I wrong?"
        show gg 47b
        reds "Ehh?"
        show gg 47
        reds "Oh..." with dis
        reds "True... that's true."
        reds "I see you know your stuff. Did you also throw salt over your shoulder?"
        show gg 54
        n "Over the left shoulder, yes. I also have a rabbit's foot talisman."
        n "Don't worry, I already saw how supersititious pirates can be when I recruited my first crew, before El Coyote ki–"
        show gg 54b
        n "*Clears throat* B-Before they all happily retired and went to Ion to spend all their money at Aphrodite's." with dissolve
        show gg 47
        reds "Ah, I see I'm dealing with an expert..."
        reds "Good. That's good."
        reds "Sorry about my initial reaction, ma'am."
        reds "Blackheart Reddss at your service. Sailor, magician, and expert cook."
        if novapath:
            play sound stomach
            show gg 48
            no "Ugh, just hearing the word {i}cook{/i} made me remember how hungry I am."with dis12
            no "In the end, we didn't have any dinner today."
            show gg 49
            reds "Don't worry, ginger girl, I've got some freshly baked pastries for you!"
            reds "They won't really fill you up in the real world, but they'll take the edge off that hunger."
            show gg 50
            no "Ohh! Seriously? Thanks!"
            $ nova_points += 1
            play sound beat
            show screen heartbeat
            no "Okay that's it, you've officialy got the best sailor on the island, [mc]! Thank you!"
            mc "*Chuckles* I'm glad you feel that way."
    elif lorrdy:
        show gg 44
        lor "I suppose it's my turn to introduce myself." with dis 
        lor "I'm Lorrdy Silverhook, and my friend here on my shoulder goes by the name of Iago."
        lor "We're notorious for being Tortuga's finest navigators."
        show gg 54
        n "Ah, a navigator!"
        if nancypath:
            $ nancy_points += 1
            play sound beat
            show screen heartbeat
        n "We could certainly use one around here. Really good thinking, [mc]."
        show gg 44
        lor "As a German, born and raised miles from any ocean, the vastness of the seas always filled me with yearning."
        lor "Ever since I was a wee lad, I dreamt of charting the world's coasts, becoming a master navigator of the eight seas!"
        show gg 55
        n "But... Germany does have a coast."
        show gg 45
        lor "Eh?"
        lor "Does it...? Since when?"
        play sound parrot
        scene iago4
        iag "North sea and Baltic sea!" 
        show gg 55
        n "Do you even know how to use a sextant?"
        show gg 45
        lor "Uh..."
        lor "Well, talking about sex toys is a bit awkward, but..."
        lor "It's basically the thing you..."
        play sound parrot
        scene iago4
        iag "It uses the sun and stars to determine your position, yes!" 
        scene gg 44
        lor "A-Ah... yes, that, of course." with dis08
        show gg 54
        n "Well, at least the parrot seems to know its stuff!"
        show gg 50
        no "He's so smart! Can I actually ask him navigation or geography questions?"
        no "Like... do you know what the biggest island in the Antilles is?"
        play sound parrotshort
        show gg 44
        lor "Spain."(multiple=2)
        iag "Cuba."(multiple=2)
        show gg 54
        n "Great! Iago will be our navigator!"
    else:
        scene gg 51
        scar "I guess it's my turn now!"with dis
        scar "Hi, hi, everyone!"
        scar "I'm Scarlet! I'm your morale booster and go-to gal for... *giggles* whatever you might need..."
        scene gg 52
        pause
        show gg 53
        n ". . ." (multiple=2)with dis
        no ". . ." (multiple=2)
        mc "D-Don't give me that look!"
        mc "It's not what it seems! Underneath it all, she's incredibly resourceful."
        show gg 51b
        mc "Look!"
        mc "Scarlet! What do you know about... I don't know, let's say... whales?"
        show gg 51
        scar "Eh... they're very big fish."
        scar "And they eat... uhh... sharks, I suppose?"
        show gg 51b
        mc "Okay, nevermind..."
    play sound church2 volume 0.5 fadein 1
    scene gg 56
    n "Alright crew, listen up!" with dis12
    n "Time to get to work!"
    show gg 50
    no "Yes, Captain!"
    show gg 56
    n "Trim the mainsail, man the capstan, and raise the anchor!"
    n "We're leaving Tortuga!" with hpunch
    play sound rope
    play sound2 rope2
    play sound3 wood
    play sound4 wood2
    play sound5 whoosh6
    if reddss:
        scene novaropeup1
    elif lorrdy:
        play sound7 parrot
        scene novaropeup2
    else:
        scene novaropeup3
    no "*Climbing the rope* Come on, guys!"with pu
    no "The Island of the Lost Souls won't conquer itself!"
    play sound5 seagull
    no "FULL SAIL!" with hpunch 
    stop music2 fadeout 4
    play sound7 wave
    scene black
    show pm2long with dis3
    play sound6 seagull
    stop soundloop fadeout 6
    play sound2 ["<silence 1.5>", whale]
    pause 2.7
    play sound6 wind4
    play soundloop2 wavesship fadein 5
    scene gg 58 with dis3
    pause  
    play sound wood2
    play soundloop fireplace fadein 3
    scene gg 59 with dis17
    mc "*Leaning on the guardrail* J-Jeez, it's so freaking cold here."with dis12
    mc "And the fact that we have to move so slowly doesn't exactly help."
    play sound2 sneeze
    mc "*Sneezes*"with vpunch 
    show gg 60
    tar "So yeah, in short, JFK was killed by the reptilians when he tried to reveal that we're all living in a simulation that generates energy for the alien Lizard Queen." with dis14
    tar "He was silenced."
    show gg 61
    mc "*Sighs* Why do your conspiracies keep getting crazier and crazier?"with dis
    show gg 60
    tar "Believe what you want, I'm just trying to open your eyes."with dis
    tar "I present the truth about the world. Whether you choose to accept it is entirely up to you."
    show gg 61
    mc "Alright, then, tell me: what is Eternum really, Mr. “I present the truth”?"with dis
    show gg 60
    tar "Obviously, Eternum is nothing but a parallel dimension where we project our astral selves through the neural implant."with dis
    tar "Ulysses discovered how to manipulate the souls of the dead to create NPCs and turned it into a multi-billion dollar business."
    show gg 61
    mc "*Snorts* That's..."with dis
    mc "W-Wait, that's surprisingly accurate... what the fuck?"
    mc "Are reptilians real...?"
    show gg 62
    no "So... what about the moon landing? Or 9/11?"
    no "Do you have any takes on those too?"
    show gg 60
    tar "Oh, please. Those are just a silly myths spread by conspiracy charlatans."
    tar "The truth is far more shocking than that."
    tar "I mean, for starters, New York doesn't even exist."
    show gg 62
    no ". . ."
    show gg 64
    no "What...?" with dissolve
    no "The... whole city doesn't exist?"
    show gg 60
    tar "Have you ever been to Manhattan?"
    show gg 64
    no "Erm..."
    no "I mean, no, but there are millions of videos and photos on the Internet."
    show gg 60
    tar "All of them fabricated by the NWO."
    tar "Have you ever seen it with your own eyes?"
    show gg 64
    no "Um..."
    no "I have relatives who've been there."
    no "My mom's cousin was literally there two years ago."
    no "And I bet at least half the people on the East Coast have visited it at least once."
    show gg 60
    tar "Have YOU ever been to New York?"
    show gg 63
    no ". . ."
    show gg 64
    no "No, I haven't."
    show gg 65
    pause 
    show gg 60
    tar "I rest my case."with dis
    show gg 63
    no ". . ."
    show gg 66
    no "Anyway... are we close?"with dis
    play sound stairswood2
    scene gg 67
    n "We should be nearing the edge." with dis15
    n "Unless the compass is broken, we're gonna be out of this icy mess in about 20 minutes."
    scene gg 68
    zap "Once we spot a big, horse-shaped iceberg, we're gonna be out of danger."
    show gg 67
    n "Yeah..."
    n "Not quite seeing it yet, but it shouldn't be too far off."
    show gg 70
    no "We've been sailing for hours already."with dis 
    no "Aren't we falling behind schedule? What if the island vanishes before we get there?"
    show gg 68
    zap "This map isn't really that accurate distance-wise. We've actually covered over half the journey already."
    zap "Crossing from the mermaid territory to the Paradox Archipelago should only take a couple of hours."
    play music piratescary
    show gg 69
    zap "The Icebergs of Frostbone are much larger than depicted here, and the most perilous part of the trip."with dissolve 
    zap "Most ships never make it past them."
    show gg 70
    no "Is it truly that dangerous?"
    show gg 69
    zap "Hah! You have no idea, child."
    zap "A monster capable of swallowing you whole roams these waters."
    zap "It approaches silently, and when you lean over the guardrail for just a moment to gauge the wind's direction..."
    play sound impactwood
    show gg 70
    zap "ZAP!" with hpunch 
    zap "It springs from the depths and devours you in one gulp!"
    no "O-One gulp?"
    show gg 69
    zap "The killer whale of Frostbone has claimed the lives of countless sailors."
    zap "It's faster than a motorboat and stronger than a carrier."
    show gg 70b
    n "Could it sink the ship if it wanted to?"
    show gg 69
    zap "Hard to tell."
    zap "But it could definitely poke a big ol' hole in the hull, that's for sure."
    show gg 70
    no "I thought whales were peaceful creatures."
    show gg 69
    zap "Oh, but it's an orca – they're technically dolphins."
    zap "And those bastards are anything but peaceful."
    zap "Once they get a taste for human blood... there's no turning back."
    show gg 70b
    n "Does the one that roams these waters have a name?"
    show gg 71
    zap "He's mostly known as the Devourer of Men, or... the Abyssal Terror."with dis
    zap "But the locals usually call it..."
    play sound deception
    play sound2 impact
    zap "Phil."with dis
    show gg 70
    no ". . ."
    stop music
    play sound pop
    show gg 72
    no "What?"
    no "The killer whale is called... “Phil”?"
    no "What kind of name is that?"
    show gg 69
    zap "I don’t know, ask the fishermen, they named it."
    show gg 72b
    n "I'm with Nova, why would someone name a killer whale... that?"
    n "It should be called... “Leviathan”, or... I don't know, “The Sea Reaper”."
    n "It would be more fitting. No?"
    show gg 72
    no "Yeah, it's like if “Sauron, the Dark Lord” was instead called... “Bobby”."
    no "“Bobby, the Dark Lord of Middle Earth”."
    show gg 69
    zap "Look, I'm not the one who came up with it, okay?"
    zap "If you wanna file a complaint, take it up with the Fishermen's Union or something."
    show gg 73
    no "“Phil the Whale” sounds super cute!"
    show gg 73b
    n "I agree! It makes it sound so adorable."
    n "Maybe he's friendly after all."
    show gg 68
    zap "You should be grateful I kept it at bay."
    zap "If it weren't for my skills in–"
    play sound whalehit
    scene gg 74 with vpunchslow
    pause 
    stop soundloop fadeout 5
    play music2 apassionato 
    play sound2 wood2
    scene gg 75
    no "*Standing up* W-What was that?" with dis
    tar "Did we just hit a block of ice...?"
    scene gg 76
    n "I-I don't think that was an iceberg."
    show gg 77
    n "Zap??"
    show gg 81
    zap "Alright... everyone stay calm."
    zap "We're almost out of his territory."
    zap "We're moving so slowly, maybe he just thinks we're another iceberg."
    show gg 76
    n "So what do we do n–"
    play sound3 whalehit
    scene gg 77
    n ". . ."with vpunchslow
    scene gg 75
    no "I-It hit us again!" 
    show gg 81
    zap "E-Everyone stay calm and quiet."
    zap "[mc], Nova, check over the side and see if you can spot it."
    zap "Nancy, go get the wheel. We'll just avoid it until we leave these waters – I think I can already see the horse-shaped iceberg!"
    mc "Got it!"
    play sound wood2
    scene gg 78 with dis12
    zap "Look for a 30-foot shadow in the water!"with dis08
    no "Yes!"
    mct "I've gotta sharpen my..."
    play sound2 whalepass 
    show whalepass with dis14
    pause 7.9
    scene gg 79 with dis14
    mc ". . ." with dis
    mc "Eh?" 
    play sound7 woodhit
    play sound6 impactwood
    play sound5 whoosh3b
    show gg80
    mc "THE FUCK IS THAT?!" with hpunch 
    mc "Thirty foot, my ass! That thing's the size of a football stadium!"with hpunch 
    scene gg 81
    zap "Uhh... well, maybe it's been eating well all these years."
    zap "They say the orcas in this area never stop growing."
    show gg 80
    mc "And you tell us this NOW?!"
    play sound3 whalehit
    scene gg 80
    bla "The colossal creature strikes the ship once more, its forceful blow echoing throughout the vessel." with vpunchslow
    scene gg 83
    zap "I'm afraid there's only one way to get out of this."with dis12
    zap "We must sacrifice one of us to the waters."
    zap "If the legends are true, that will appease the giant."
    show gg 82
    mc "Ah, of course, and I bet you're not volunteering yourself?"
    if reddss:
        reds "Fear not, my friends!"
        show gg 88c2
        mc "Huh? Reddss?" with dis
        mc "Please, tell me you have a magic trick to make sea monsters vanish."
        show gg 88c
        reds "Almost!"
        reds "I've got a recipe to lull those creatures to sleep!"
        show gg 88c2
        mc "A recipe...? Are you serious?"
        show gg 88c
        reds "Absolutely! I once knocked out a giant megalodon in the southern oceans with just a slice of my sleepy cake."
        reds "Phil might be a bit larger, but I'll use the whole cake just to be safe."
        show gg 88c2
        mc "Uh..."
        mc "I'm not sure..."
        play sound3 whalehit
        scene gg76
        n "F-Fuck!" with vpunchslow
        n "[mc], please, whatever you decide, make it quick!" 
        play sound4 whoosh3b
        show gg 88c2
        mc "O-Okay, okay!" with pl 
        mc "Let's try it!"
        show gg 88c
        reds "Follow me to the back of the ship!"
        show gg 88c2
        mc "Oh god, this better work..."
        play sound wood2
        scene gg 89c with dis22
        reds "Don't worry, my friends, I got this."with dis
        reds "My sleepy cake is foolproof."
        reds "Just watch and let yourselves be amazed!"
        show gg 90
        zap "I have complete faith in you, Mr. Reddss! Complete faith!"with dis 
        show gg 91
        zap "Start considering who we should offer as a sacrifice – the cake idea is bound to fail."
        show gg 89c
        reds "Pass me more rope, Mr. Zap! I'll start lowering it now." with dis
        zap "And why not just toss the cake into the ocean?"
        reds "Well, that would bring us very bad luck."
        show gg 92c
        reds "*Lowering the rope* Furthermore, the whale might miss it, and the cake would sink into the depths of the ocean."with dis14
        reds "Without any more fish pheromones, this is our only shot."
        reds "Now, listen up: here's the plan."
        reds "First, the whale eats the cake."
    elif lorrdy:
        lor "Looks like my time to shine has finally arrived."
        show gg 88b2
        mc "Huh? Mr. Lorrdy!"with dis
        mc "Finally! Where the hell have you been?"
        show gg 88b
        lor "I was in the toilet when the whale knocked me off the seat, please don't go anywhere near it anytime soon—NOW LISTEN!"
        lor "I need you all to relax."
        lor "I can communicate with the whale and convince it to let us go."
        show gg 88b2
        mc "What?"
        mc "You can... {i}communicate{/i} with the whale...?"
        show gg 88b
        lor "As I told you, I have a way with all sorts of animals."
        lor "Once, I convinced a great white shark to stop snacking on kids at the beaches of Copacabana, Mexico."
        show gg 88b2
        mc "B-But Copacabana is not even on–"
        show gg 88b
        lor "Just trust me on this, you've got nothing to worry about."
        show gg 88b2
        mc "Uh..."
        mc "I'm not sure..."
        play sound3 whalehit
        scene gg762
        n "F-Fuck!" with vpunchslow
        n "[mc], please, whatever you decide, make it quick!" 
        play sound4 whoosh3b
        scene gg 88b2
        mc "O-Okay, okay!" with pl 
        mc "Let's give it a try!"
        show gg 88b
        lor "Follow me to the stern. I'll have a little chat with our giant friend there."
        show gg 88b2
        mc "Oh god, this better work..."
        play sound wood2
        scene gg 89b with dis22
        lor "Don't worry, guys. I've got this."with dis
        lor "*Clears throat* I just need to warm up my throat and recall my orca dialect."
        show gg 90
        zap "I have complete faith in you, Mr. Lorrdy! Complete faith!"with dis 
        show gg 91
        zap "Start considering who we should offer as a sacrifice – this dialogue idea is bound to fail."
        show gg 89b
        lor "{bt=3}AAAAaarrrhhhhh... ooooooorrrhh...{/bt}" with dis12
        lor "*Clears throat* Alright, I think I got this. It was called... Phil, right?"
        zap "Um... well, I guess. His whale buddies probably call him something else."
        lor "It's okay, I'll just start with a friendly intro."
        play sound7 bird_flying
        play sound6 ["<silence 0.6>", parrot] volume 0.45
        show gg92b
        bla "Iago takes to the sky, flying far from the ship." with dis14
        mc "That can't be good..." 
        lor "*Clears throat* Alright."
        lor "{bt=3}Buuuuurrrrraaaaaarrrrrrrrrrrrr...{/bt}"
    else:
        show gg 83
        zap "I will, if I have to."
        zap "It's your call, Quartermaster."
        show gg 82
        mc "Really?"
        show gg 83
        zap "My idea was to pick the person who contributes the least to the team."
        zap "In other words... the most expendable member of the crew."
        show gg 82
        mc "Mmph."
        zap ". . ."
        mc ". . ."
        play sound wood2
        show gg 84 with dis15
        pause 
        show gg 85
        scar "What...?" with dis
        scar "Why is everyone looking at me?"
        show gg 86
        scar "Wait..."with dis12
        scar "Are you suggesting I get swallowed by the whale?!"
        show gg 87
        zap "Not exactly, darling!"
        zap "Being “swallowed” implies you'd be eaten and all, but you'd just be residing within the whale until we return from the Island of the Lost Souls!"
        show gg 86
        scar "Inside...? How?!"
        show gg 87
        zap "Ever heard of Gepetto? Pinocchio's dad?"
        zap "It's the same thing! Except, in this case, this picky whale only swallows the most stunning women!"
        zap "Therefore, we must select the loveliest lady among us!"
        show gg 86
        scar "Oh..."
        show gg 88
        scar "Okay, yeah, that makes sense."with dis
        show gg 87
        zap "Right?!"
        zap "Now, let's head to the back of the ship, quick!"
        mct "This won't end up well..."
        play sound wood2
        scene gg 89 with dis22
        scar "Oh my, this thing's swaying like crazy!"with dis
        scar "Alright..."
        scar "Am I good here?"
        show gg 90
        zap "Perfect!" with dis
        zap "Agh, you're so lucky! I wish it could be me!"
        show gg 91
        zap "*Whispering* Let's just pray the whale doesn't spit her out with all that plastic and makeup on."
        show gg 89
        scar "So... what now?"with dis12
        scar "Do I just wait here and wait for it to come?"
        zap "You have to jump."
        show gg 92
        scar "Whaaaat? But it's so high up!" with dis14
        zap "It's just water!"
        scar "But what if I land wrong and I break my nail–"
    stop music2
    play sound whalejump
    scene gg 93 with vpunchslow
    pause 1
    play sound8 swallow3
    phil "*Swallows*{w=2.8}{nw}" with dis08
    play sound2 ["<silence 0.2>", whalefall]
    scene gg 94 with dis15
    play sound3 whale
    play sound4 ["<silence 1.5>", wave]
    play music ["<silence 4.5>"]
    play soundloop waves
    pause
    play sound6 woodhit
    play sound7 whoosh3b
    play music2 pirate2 fadein 3
    scene gg 95
    mc "H-HOLY FUCK." 
    mc "T-That thing is even bigger than I thought."
    show gg 96
    zap "O-Okay, that didn't go as planned, but..."
    if reddss:
        zap "Mr. Reddss' sacrifice will be remembered, no doubt!"
        zap "We should honor his memory and get the fuck out of here ASAP!"
    elif lorrdy:
        zap "Mr. Lorrdy's sacrifice will be remembered, no doubt!"
        zap "We should honor his memory and get the fuck out of here ASAP!"
    else:
        zap "Ms. Scarlet's sacrifice will be remembered, no doubt!"
        zap "We should honor her memory and get the fuck out of here ASAP!"
    show gg 95
    mc "NANCY!"
    show gg 96
    zap "TARTARIA!"
    show gg 95
    mc "NOVA!"
    mc "GET US OUT OF HERE!"with hpunch 
    n "On it!"
    play sound whalepass
    scene gg 97 with dis3
    no "Bye Phil!" with dis14
    stop music2 fadeout 7
    scene pm3long with dis3
    stop soundloop fadeout 6
    pause 2.7
    play sound6 wind4
    scene ggg 6 with dis3
    pause   
    scene ggg 1
    mct "Man, this sun is brutal... I almost miss those icebergs." with dis2
    mct "But we have to push through."
    mct "If Coyote keeps his word and we succeed here, we'll already have three Gems of Doom."
    mct "With two more still hidden, that would put us in a 5-5 tie with Thanatos."
    mct "And then... everything will come down to our final showdown."
    mc "Hmph."
    mct "I used to think I could defeat him effortlessly if we faced each other again, but after what happened in the alley... my confidence has wavered."
    mct "I need to keep training."
    show ggg 2
    mc "*Sighs* Ahh..."
    show ggg 1
    mct "But anyway, now's not the time to worry about that. One step at a time."
    show ggg 2
    mc "Tartaria? You've been so silent for a while."
    mc "How about entertaining us with another one of your conspiracy theories?"
    show ggg 1
    tar "Do you hear the music, [mc]?"
    tar "It's so beautiful..."
    show ggg 2
    mc "Hah, that one sounds intriguing!"
    mc "Please, I'm all ears."
    show ggg 1
    bla ". . ."
    show ggg 2
    mc "Tartaria? Come on, I'm interested!"
    show ggg 1
    bla ". . ."
    scene ggg 3
    mct "Hmm?" with dis
    show 084 with dis12
    play sound2 ["<silence 1.6>", splash3] volume 0.6
    play sound7 ["<silence 1.7>", splash2] volume 0.5
    pause 2.2
    play sound wood2
    play sound3 chair2
    play soundlow wave
    scene ggg 4
    mc "*Standing up* W-What the..."with dis12
    mc "What the hell are you doing, man?!"
    mc "That's not funny!"
    play sound stairswood2
    scene ggg 5 with dis12
    mc "*Climbing down the stairs* (What's going on with this guy now?)"with dis08
    mc "Tartaria?!"
    play sound2 woodhit
    mc "Fuck!"with vpunch 
    show ggg 6
    mc "Nancy, Nova! Come up here!"with dis08
    play music mermaid fadein 30
    stop soundloop2 fadeout 30
    mc "We have to stop the ship, Tartaria jumped overboard!"
    scene ggg 5
    mct "This can't be real."with dis08
    mct "I swear, if this is all because of another one of his conspiracies, we're not coming back for..."
    mct "For..."
    mc ". . ."
    scene ggg 7
    mc "*Turning around* (Wait... I can hear music too...)"with dis12
    mct "Is that... a woman singing...?"
    mct "It's so..."
    mct "So beautiful..."
    play soundlow wood2
    scene ggg 8 with dis17
    play sound wave
    mc "*Leaning on the guardrail* (What a beautiful melody...)" with dis12
    mct "It's so..."
    mct "Incredibly..."
    mct "Inviting..."
    play sound chair2
    scene ggg 9
    bla "You clamber onto the ship's guardrail, straining to catch the enchanting music more clearly."with dis14
    mct "Whoa..."
    mct "I've never heard a more beautiful voice in my life..."
    show ggg 10
    mc "*Gazing downward* . . ." with dis
    scene ggg 11
    mct "The water looks so good..."
    mct "Could the girl singing this melody be down there...?"
    mct "Maybe..."
    mct "I should... take a peek...?"
    mct "Just... for a second..."
    mct "It can't... hurt... right...?"
    menu:
        with dis
        "Jump off the ship":
            jump jumpoff
        "Don't jump [mt](continue)":
            mct "I probably shouldn't..." with dis08
            show ggg 10
            mc ". . ."with dis12
            mct "Or should I...?"
            menu:
                with dis
                "{bt=2}Jump off the ship{/bt}":
                    jump jumpoff
                "Don't jump [mt](continue)":
                    mct "No..." with dis08
                    mct "I would die."
                    show ggg 11
                    mct "But... on the other hand..."with dis12
                    mct "Who cares about death if it means I can forever be with the woman who sings this beautiful melody...?"
                    menu:
                        with dis
                        "":
                            pass
                        "":
                            pass
                        "":
                            pass
                        "":
                            pass
                        "":
                            pass                      
                        "{sc=3}{size=44}Jump off the ship.{/sc}":
                            jump jumpoff
                        "":
                            pass
                        "":
                            pass
                        # "":
                        #     pass
                        # "":
                        #     pass
                        "Don't jump [mt](continue)":
                            mct "My mind keeps saying “don't do it”..." with dis08
                            mct "But my heart insists..."
                            show ggg 9
                            mct "Jump and unite with the love of your life..."with dis12
                            mct "“DO IT”."
                            show screen mousemovemermaid
                            menu:
                                with dis
                                "":
                                    pass
                                "":
                                    pass
                                "":
                                    pass
                                "":
                                    pass
                                "":
                                    pass                              
                                "[gr]{sc=3}{size=51}JUMP OFF THE SHIP.{/sc}":
                                    hide screen mousemovemermaid
                                    jump jumpoff
                                "":
                                    pass
                                "":
                                    pass
                                # "":
                                #     pass
                                # "":
                                #     pass
                                "Don't jump":
                                    hide screen mousemovemermaid
                                    menu:
                                        with dis
                                        "{size=60}J. U. M. P.":
                                            jump jumpoff
label jumpoff:
    mct "Yes..."with dis 
    scene ggg 12
    mct "Of course, why should I not...?"with dis12
    mct "I finally see it clearly."
    play sound wood2
    mc "*Taking a step forward* (Wait for me, my love... I'm coming...)"
    play sound3 grab3
    stop music
    play sound4 woodhit
    play sound5 impactwood
    play sound6 grab3
    play music2 piratefunk
    scene ggg 13
    no "{sc=3}WHAT THE FUCK ARE YOU DOING, [mc!u]!{/sc}" with hpunchlong4
    mc "Let me go..."
    mc "You can't stop me..."
    no "NANCY, HELP!" with hpunch 
    no "[mc!u] WANTS TO KILL HIMSELF!" with hpunch 
    mc "I must follow the music..."
    no "What music?! What are you talking about?!" with hpunch 
    mc "Don't you hear the melody of the ocean...?"
    no "I only hear the waves and fucking seagulls!" with hpunch 
    no "SNAP OUT OF IT!"with hpunch 
    mc "You don't understand the love a man can feel for a woman..."
    mc "I must..."
    mc "Join her..."
    no "{sc=4}NANCYYYYY!!!{/sc}" with hpunchlong4
    play sound ding
    play sound6 rope2
    play sound7 rope2
    stop music2
    play soundloop wavesship
    scene ggg 14
    mc "The music..."
    mc "I need to follow the music..."
    show ggg 15
    n "My god, that was tough!"with dis12
    n "He's so strong."
    show ggg 17
    no "These sirens sure are scary."
    no "If I had popped up on deck just a second later, he'd be dead by now."
    show ggg 16
    n "Yeah, thank god it only affects men."
    show ggg 17
    no "Speaking of men... where's Tartaria? Wasn't he up here with [mc]?"
    show ggg 14
    mc "Tartaria's already taken the plunge..."
    mc "Lucky bastard..."
    mc "I wish I could've been the one..."
    show ggg 15
    n "Seriously?!"
    n "*Sighs* That's another crew member gone..."
    n "If we lose one more we're gonna be screwed."
    n "We've gotta make sure to..."
    show ggg 16
    n "Oh no."with dissolve
    n "Mr. Zap!"
    show ggg 18
    no "Oh fuck, I forgot about him."
    no "W-Where is he?"
    show ggg 16
    n "I-I think he was down below, messing with the cannons."
    show ggg 18
    no "We've gotta go tie him down before he gets hypnotized and decides to take a dive too!"
    show ggg 16
    n "Oh man, I hope we're not too late..."
    play sound run
    show ggg 14
    no "DON'T MOVE FROM HERE, [mc!u]!"with dis14
    n "We'll be right back!"
    mc "'Kay..."
    play music mermaid fadein 18
    stop soundloop fadeout 19
    show ggg 19
    mc "As long as I can keep having this view..."with dis15
    mc "God, what a sight."
    mc "Look at how beautiful the ocean is."
    play sound rope
    play sound2 rope
    mc "*Struggling to untie yourself* If only I could get a little closer..."
    play sound3 water
    play sound4 drips
    scene ggg 20
    bla "A sudden splash of water draws your attention towards the guardrail on your right." with dis12
    mc "Huh?"
    mc "Is there anyone there...?"
    play soundlow whoosh3b
    play sound6 water
    show ggg 22
    merm "Boo!" with dis03
    show ggg 21
    mc "Wha..."
    mc "Who are you...?"
    mc "Did you... did you just climb up the hull of the boat?"
    mc "Are you from a shipwreck...?"
    show ggg 22
    merm "*Giggles* I did climb the hull, but I'm no shipwreck!"
    merm "I live in the ocean."
    show ggg 21
    mc "Oh..."
    mc "Cool..."
    mc "Were you the one singing that beautiful melody...?"
    show ggg 23
    merm "*Giggles* Well, I was, but now my sisters have taken over."
    merm "I must admit, their singing is muuuuch better than mine."
    show ggg 22
    merm "Can I come up? I wouldn't want to be a bother."
    show ggg 21
    mc "Of course, come on up..."
    play sound water
    play sound2 wood2
    play sound3 drips
    show ggg 24 with dis12
    merm "*Climbing up on deck* Wow, you have a great ship, [mc]..."with dis
    show ggg 25
    mc "You know my name...?"
    show ggg 26
    merm "Who in this ocean doesn't know [nickname]!"
    merm "*Giggles* I'm quite the fan, I must confess."
    show ggg 25
    mc "Oh..."
    mc "Thank you..."
    mc "You..."
    mc "You're a mermaid..."
    show ggg 26
    merm "*Giggles* Guilty as charged!"
    show ggg 25
    mc "Won't you dry up here in the sun...?"
    show ggg 26
    merm "Not at all! In fact, we enjoy soaking up some rays now and then."
    merm "You don't mind if I catch some sun, do you?"
    show ggg 25
    mc "Suit yourself..."
    show ggg 26
    merm "Thanks!"
    play sound wood2
    show ggg 27 with dis14
    pause 
    play sound2 clothes3
    play sound3 clothes5
    show ggg 28 with dis14
    mc "Whoa..." with dis
    show ggg 29
    merm "*Giggles* Much better."
    show ggg 28
    mc "I bet..."
    show ggg 29
    merm "Do you like my breasts?"
    show ggg 28
    mc "I do..."
    show ggg 29
    merm "Do you want to... touch me?"
    show ggg 28
    mc "Yeah... but..."
    mc "I can't..."
    mc "I am... tied up..."
    show ggg 29
    merm "Are you sure about that?"
    merm "*Giggles* You look pretty unrestricted to me."
    show ggg 30
    mc "Eh...?"
    show ggg 31
    mc "Huh?"with dis
    show ggg 32
    mc "Ooh... how did you do that...?"with dis12
    play sound wood2
    scene ggg 33
    merm "*Giggles* I can do a lot of magical things, [mc]... especially to young handsome men like you."with dis12
    merm "Do you want to see everything I'm capable of...?"
    show ggg 34
    mc "Yes..."
    show ggg 33
    merm "Would you like to come with me to the source of the music and spend eternity underwater together?"
    show ggg 34
    mc "Nothing would make me happier..."
    show ggg 33
    merm "*Giggles* Good boy..."
    play sound3 wood2
    show ggg 35
    merm "*Sitting up* Then let's not wait another second." with dis12
    merm "Take my hand, and come with me..."
    mc "Yes..."
    merm "Come with me and experience the greatest of plea–"
    play music ["<silence 2>"]
    queue music piratefunk
    play sound arrow
    play sound2 gore
    play sound4 crashwood volume 0.4
    play sound5 impactwood
    play sound6 blood3
    play sound3 ["<silence 0.3>", mermaidscream]
    show gg36
    merm "{sc=3}NNNNGGGGGGGGYAAAAAAAA!!!{/sc}"with hpunch
    scene ggg 37
    n "Get away from him, you filthy hag." with dis
    show ggg 37b
    mc "What did you do..."
    mc "I loved her..."
    show ggg 37
    n "Don't worry, [mc], we'll be the ones protecting you this time."
    scene ggg 38
    no "Can we manage the ship on our own with only two people?"
    show ggg 37
    n "We'll have to try."
    n "But first, we need to–"
    play sound7 impactwood
    play sound mermaidscream
    scene ggg39
    merm "{sc=3}NNNNGGGGGGYAAAAAAAA!!!{/sc}{w=1.2}{nw}"with hpunchlongsubtle
    play sound3 choke
    play sound gore
    play sound2 arrow
    scene ggg 40 with hpunch
    pause
    play sound4 splash3
    play sound8 splash3
    scene ggg 41
    n "I'm almost out of spears..."with dis
    n "We need to get out of here and into Serenity's Current, or the sirens won't stop coming."
    scene ggg 42
    no "I can cover you, don't worry!"
    play sound5 mermaidshot
    play sound6 ["<silence 0.6>", blood3]
    play sound7 ["<silence 1.8>", splash3]
    show ggg43
    no "But... are you sure you can handle the ship on your own?"
    no "Mr. Zap is tied up down below, and [mc] is still–"
    play sound whoosh3b
    scene ggg 45
    nosc "AAAAARGH, [mc!u] IS GONNA JUMP AGAIN!"with hpunch 
    scene ggg 11
    mc "They won't be able to separate us, my love..."with dis12
    n "Damn it, we can't be everywhere! You have to shoot him!"
    no "WHAT?!"with hpunch 
    n "Doesn't Dione have a tranquilizer dart pistol version or something similar?!"
    no "Eh??"
    no "Oh! It does! Good idea!"
    show ggg 12
    mc "Here I go..." with dis12
    no "Sorry [mc], it's for your own good!"
    mc "*Taking a step forward* Make me yours, queen of the oc–"
    stop music
    play sound dart
    play sound2 revolver2
    play sound4 ["<silence 1.1>", fallfull]
    play sound5 ["<silence 1.1>", woodhit]
    scene black
    pause
    play soundloop waves fadein 5
    show screen afewhourslater with dis25
    pause
    play sound3 seagull
    hide screen afewhourslater
    with dis2
    scene ggg 46 
    with dis2
    mc "*Opening your eyes* Ughh..." with dis15
    mct "Where am I...?"
    mc "Mmmmhh..."
    mct "The music..."
    play sound7 seagull
    play sound2 snow
    scene ggg 47
    mc "*Sitting up* (I remember the music...)"with dis12
    stop soundloop fadeout 25
    play music2 pirate4 fadein 8
    mc "W-Wait... I remember now!"
    mc "G-Get away from me, you fucking monsters!"with hpunch 
    n "[mc]!"
    show ggg 49
    mc "*Turning around* Huh? Nancy!"with dis08
    mc "P-Please, tell me we're safe from the sirens now."
    show ggg 48
    n "We left their territory a while ago, no need to worry."
    show ggg 49
    mc "Oh, thank goodness..."
    play sound snow
    play sound2 debris
    show ggg 50
    mc "*Standing up* Jeez, that was scary." with dis
    show ggg 51
    n "Sorry for putting you to sleep like that, we had too many threats and just the two of us to handle them."
    show ggg 50
    mc "Oh, trust me, I'm SO glad you did."
    mc "As strange as it might sound, I remember everything."
    mc "I knew I'd probably die if I jumped off the ship, but at the same time... I couldn't resist the overwhelming urge to do it."
    mc "It's hard to explain, it was such a weird sensation."
    show ggg 52
    no "[mc]! I'm so glad you're back with us!"with dis
    mc "Nova!"
    show ggg 53
    mc "All thanks to you two!" with dis12
    mc "Phew, it feels good to be back on solid ground again."
    mc "What happened after you knocked me out, exactly?"
    show ggg 54
    no "Well, with both you and Mr. Zap out of commission, Nancy took the wheel and we redirected the ship as fast as we could."
    show ggg 56
    n "Those sirens didn't make it easy, though."
    show ggg 55
    no "Yeahhh... they kept popping up everywhere like {bt=3}{i}nyaaaaaaaaaah!{/i}{/bt} – trying to kill us both!" 
    show ggg 56
    n "Women aren't affected by their singing, but those sharp nails of theirs can still slice a shark in half."
    show ggg 51
    n "Although... I guess at least our fate is better than the men's."with dis
    show ggg 50
    mc "What would have happened to me?"
    show ggg 56
    n "Well... according to the stories, the sirens lure men into the water, making them jump willingly."with dis
    show ggg 55
    no "Once they're in, they chop off their testicles and introduce them into their genital pores to fertilize their eggs, breeding dozens of new sirens."
    mc "T-They what?"
    show ggg 56
    n "Finally, if the man hasn't drowned by then, they decapitate him and feast on his flesh."
    n "All while still hearing their cursed melody..."
    play sound swallow
    mc "*Gulps* T-That sounds pretty awful."
    n "Oh, you have no idea..."
    show ggg 57
    n "Luckily for us, Nova's superhuman aim took out every single siren that tried to board the ship before they could even get close to us."
    show ggg 58
    no "*Giggles* Well, I wouldn't say {i}superhuman{/i}, but..."
    no "Hihi, I appreciate it, thank you."
    mc "Yeah, I'm well aware of Nova's extraordinary skills."
    no "*Giggles* Come on, guys, stop it!"
    show ggg 50
    mc "*Chuckles* So... where are we now?" with dis
    show ggg 51
    n "On the border between the Bay of the Undead and the Paradox Archipelago."
    n "Our journey is almost over!"
    show ggg 50
    mc "Seriously? We managed to avoid the Bay of the Undead?!"
    show ggg 51
    n "Yes! It was as simple as steering clear of their island."
    n "Once we find our way out of this archipelago, we'll finally see the Island of the Lost Souls!"
    show ggg 50
    mc "Oh, neat!"
    show ggg 51
    n "Compasses stop working in here, so Mr. Zap went to that old pirate post to find a high vantage point for..."
    show ggg 59
    zap "Guys, over here!" with dissolve
    show ggg 60
    n "*Turning around* Oh, he's back!" with dis
    zap "Ah, good to see you safe and sound, Mr. [mc]!"
    mc "Thank you, Zap!"
    zap "Now come over here, quick! I have juicy, juicy news!"
    mc "My favorite kind of news!"
    play sound wave
    scene ggg 61 with dis25
    play sound2 seagull
    bla "You wade through the tidal pool of the bay and regroup with Zap on the abandoned but still intact dock."with dis
    play sound3 footsteps2
    show ggg 62 with dis15
    mc "Alright, what did you find out?" with dis
    show ggg 63
    zap "I've made a crucial discovery, my friend. CRUCIAL!"
    zap "You know how the few sailors who made it to the Archipelago could never get past this point?"
    zap "I finally know why... it's the winds!"
    show ggg 67
    no "The winds?"
    show ggg 63
    zap "The islands in the Archipelago form a circle, creating their own wind currents."
    zap "Without working compasses, sailors can't keep track of their direction and end up sailing in circles, thinking they're going straight!"
    zap "That's why some of them even wound up back in Tortuga!"
    show ggg 66
    n "But... can't you navigate by the sky? Tracking the sun or the moon?"
    show ggg 63
    zap "Uh..."
    show ggg 64b
    zap "Erm... I'm not sure. The archipelago might create an optical illusion, making the sun appear to shift constantly..."with dis06
    zap "Or... perhaps they just weren't that good as sailors, I don't know."
    show ggg 64
    zap "*Clears throat* But anyway, in any case, and as I was just saying, I know the solution." with dis
    zap "We need to trek across the main island on foot!"
    show ggg 67
    no "What?"
    no "We have to... hike through the jungle?"
    show ggg 64
    zap "I know what you're thinking: “isn't it dangerous, Mr. Zap?”"
    zap "Fear not, I happen to be an expert at navigating jungles."
    show ggg 65
    mc "I thought you were an expert fisherman."
    show ggg 64
    zap "They're compatible."
    show ggg 66
    n "I was actually wondering what ship we're gonna take from the other side of the island."
    show ggg 64b
    zap "Uh... there will likely be some boat there or something, I wouldn't worry about that."
    show ggg 66
    n "Eh..."
    n "Well, if you're so sure about it..."
    show ggg 64
    zap "We've only got 4 hours left until the Island of the Lost Souls vanishes, so less chatter and more trekking!"
    zap "Let's move!"
    show ggg 65
    mc "So... on a scale of 1 to 10, how sure are you about this plan of yours?"
    zap ". . ."
    show ggg 64
    zap "About a 6."
    show ggg 65
    mc ". . ."
    show ggg 63
    zap "Look, I get it, [mc], you're scared." with dis 
    show ggg 62
    mc "I'm not scared."
    show ggg 63
    zap "But it's fear that held back every other pirate from grabbing that treasure."
    zap "We've gotta stick together, stay strong."
    zap "I've helmed my own ship for 15 years."
    zap "I fought off Davy Jones' cruel crew in the Bay of the Undead."
    show ggg 67
    no "We didn't even see them."
    show ggg 63
    zap "AND I WILL TAKE YOU TO THE ISLAND OF THE LOST SOULS!"
    zap "TRUST ME AND WE WILL PREVAIL!" with hpunch
    show ggg 62
    mc "Okay, okay!"
    mc "I guess it's worth a try."
    play sound footsteps2
    play sound2 stairswood2
    scene ggg 68
    zap "*Walking down the ramp* Don't worry, guys, everything will be alright if you stick close to me." with dis15
    play sound rope2
    play sound3 rope2
    scene ggg 69
    zap "This island might be full of dangers, so try to–"with dis
    play sound arrowb
    play sound3 blood3
    stop music2
    scene ggg 70 with pr
    pause
    play sound6 ["<silence 0.35>", fallfull]
    scene ggg 71 with dis
    play music2 piratequirky
    pause 
    no "Eh...?" with dis
    aaa "Oh, please, not again..."
    play soundlow wood2
    show ggg 72
    aaa "AGGGGGHHH, FUCK, NOT AGAIN!" with dis12 
    aaa "ED, COME HERE!"
    ed "What did you do now, Morty?"
    mo "It happened again!"
    ed "Eh?!"
    scene ggg 73
    ed "{sc=3}AAAAAAAAAAAAAAAAAAAAAARH!{/sc}" with dis
    ed "For fuck's sake, ain't there a single pirate left who's not retarded?!" with hpunch 
    mc "What the hell..."
    show ggg 74
    ed "Didn't you see the fucking sign, you dingbats?!" with dis
    mc "T-The what...?"
    show ggg 74b with dis
    mc "Oh..." with dis
    mc "Um..."
    show ggg 75
    mc "W-We somehow missed it, sorry."
    show ggg 74
    ed "Yes, I can see you missed it!"
    ed "Now who's gonna clean up this mess?! YOU?!"with hpunch 
    ed "Just..."
    ed "Agh, just move your asses back to the fucking dock before another one of you blows their head off!"with hpunch 
    ed "We're coming down! DON'T MOVE!"with hpunch 
    show ggg 76
    mo "Ease up, Ed."with dis
    mo "It's not good for your heart. Metaphorically."
    show ggg 77
    ed "*Sighs* Fine, fine... I'll calm down."with dis 
    ed "I swear, Davy doesn't pay us enough for this shit."
    ed "Now, let's go chat with the fleshbags before they implode themselves..."
    play soundlow wood2
    show ggg 78 with dis14
    play sound2 doorwoodclose
    no "W-What's going on?"with dis08
    n "Are those... skeletons?!"
    mc "W-We better do what they say for now... but stay alert."
    play sound wave
    scene ggg 79 with dis22
    pause 
    ed "*Taking a deep breath* Alright..."with dis
    play sound3 stairswood2
    show ggg 84
    ed "Now please... would you be so kind to enlighten me as to what the hell you are fucking doing here, fellas?" with dis15
    show ggg 83
    mc "Um... you can call me [nickname]. We're trying to get to the Island of the Lost Souls."
    show ggg 84
    ed "Ah, of course you are..."
    ed "EVERYONE wants to get to that damn island."
    ed "But NO ONE ever stops by to buy one of my brother's paintings."
    ed "Do you have any idea how good they are?"
    show ggg 80
    mo "They're pretty good."
    show ggg 66
    n "I paint too! And if you painted that sign yourself, I have to admit, you're very talented!"
    show ggg 80
    mo "Aw, thank you, sunshine!"
    show ggg 81
    mo "They're good folks, Ed."with dis06 
    show ggg 84
    ed "Yeah... now I can't help but feeling kind of bad for your dead partner."
    ed "Didn't they warn you about the monkey traps set in Paradox when you passed through Undead Bay?"
    show ggg 66
    n "Well... we actually avoided passing through Undead Bay."
    n "I mean, the legends say Davy Jones either kills pirates or turns them into his immortal crew for all eternity, so..."
    show ggg 84
    ed "Hah! I wish!"
    show ggg 85
    ed "Can you imagine, Morty?"with dissolve 
    show ggg 81
    mo "*Snorts* These people have been reading too many fantasy books."
    show ggg 84
    ed "Ma'am, I spent four years studying to pass the Jones service exams."
    show ggg 80
    mo "Not to mention the physical tests."
    show ggg 84
    ed "Not to mention the physical tests – you've gotta be able to do at least one strict pull-up."
    ed "Which is... not easy without actual muscles, y'know."
    show ggg 80
    mo "This year we're stuck here in this forgotten post instead of being part of the A-team on the main ship, but... well, that's a worry for another day."
    show ggg 84
    ed "Yeah, let's get back to your thing..."
    ed "So, you wanna head to the Island of the Lost Souls, huh?"
    ed "Just so you know, you've only got, like, four hours left. After that, poof! It disappears for a year."
    show ggg 66
    n "We know! We left Tortuga over 10 hours ago."
    n "That's precisely why we need to escape this Archipelago as soon as possible."
    show ggg 84
    ed "Well, lucky for you, our shift is almost done, and... yes, we know how to avoid the wind currents of the Paradox Archipelago."
    ed "Only the living can step foot on the Island of the Lost Souls, so we'd have to drop you off on its coast."
    ed "But, we can take you right up to their sunny beaches."
    show ggg 83
    mc "Oh, that's great!"
    show ggg 84
    ed "...for a price."
    show ggg 83
    mc "Oh."
    menu:
        with dis
        "[gr]Buy a painting from Morty":
            $ paintingmorty = True
            mc "How about... we buy one of your brother's paintings for the passage?"with dis08
            mc "We could display it on the ship, or... perhaps in Tortuga's tavern."
            mc "I know the owner."
            show ggg 82
            mo "*Gasps* Whaaaat?!"
            show ggg 80
            mo "DEAL!"with dis06
            mo "And I'll say more: if you hang it in the tavern, the painting is on the house!"
            show ggg 83
            ed ". . ."
            show ggg 85
            ed "You're terrible at negotiating, Morty, you know that?"with dis06
            show ggg 81
            mo "This is my chance, brother!"
            mo "I could become famous!"
            show ggg 85
            ed "Alright, alright..."
            ed "Ahh... what wouldn't I do for my little brother?"
            show ggg 84
            ed "Okay, deal."with dis06 
        "Offer 150 eternals" if money >= 150:
            mc "How about... 150 eternals for the passage?"with dis08
            show ggg 84
            ed "150 what?"
            show ggg 81
            mo "That's like 4 Spanish Pieces of Eight, brother."
            mo "It's good money!"
            show ggg 85
            ed "Four pieces?!"
            show ggg 84
            ed "Okay, you've got a deal."with dis06
            show screen eternals
            show ggg 83
            with dis
            play sound coins
            $ money -= 50
            pause .05
            $ money -= 50
            pause .05
            $ money -= 50
            pause .3
            hide screen eternals
            mc "Thank you."with dis
            show ggg 84
            ed "Deal, set and done."
        "Threaten them":
            mc "How about... you take us to the Island, and in exchange, I refrain from killing you?"with dis08
            ed ". . ."
            show ggg 84
            ed "What?"
            show ggg 80
            mo "You do realize we're already dead, right?"
            mo "We're the ones without a brain, man, have some self-respect."
            show ggg 66
            n "W-What [mc] meant to say is... how about you help us reach the Island of the Lost Souls in exchange for... let's say, 2 Spanish Pieces of Eight?"
            n "I could give them to you right now."
            show ggg 81
            mo "Oh, that's good money, brother."
            mo "We could buy at least 8 bottles of rum with that."
            show ggg 85
            ed "Eight bottles?!"
            show ggg 84
            ed "Alright, you've got a deal."with dissolve
    ed "We'll take you to the Island of the Lost Souls, you have my word."
    show ggg 83
    mc "Nice!"
    show ggg 89
    no "They say the island hides a lot of secret treasures too!"
    no "We're only after a specific artifact, so you can keep the rest!"
    show ggg 82
    mo "*Gasps* The treasure of the Lost Souls?!"
    show ggg 86
    ed "*Gasps* For us?!"
    show ggg 82
    mo "*Gasps* We could buy our own ship!"
    show ggg 86
    ed "*Gasps* AAAGH!"
    show ggg 82
    mo "*Gasps* AHHHHHHHH!"
    show ggg 86
    ed "{sc=2}*Gasps* AHHHHHHHHHHHHHHHH!{/sc}"
    show ggg 87
    ed "*Clears throat* A-Ahem. Sorry. I mean..."with dis06
    ed "Yeah, that sounds fair."
    show ggg 88
    ed "We'll grab the kraken repellent, pack our things, and meet you at the cove over there."with dis08
    ed "It's a stunning beach, just watch out for the gnomes, pheromone monkeys, and other Paradox beasts. Don't leave any food unattended."
    show ggg 85
    ed "We should be ready in... 20 minutes?"with dis08
    show ggg 81
    mo "20 minutes sounds good."
    show ggg 84
    ed "20 minutes."
    show ggg 83
    mc "20 minutes!"
    mc "But be punctual! We need to complete this mission in less than 4 hours!"
    show ggg 84
    ed "Yes, yes, no worries, we have it all under control."
    show ggg 80
    mo "All under control."
    show ggg 84
    ed "You've even got time for a quick dip and chill for a bit."
    show ggg 89
    no "*Gasps* Oh my god, yes, please!"
    no "Can we swim at the beach, [mc]?! Pretty please!"
    show ggg 90
    mc "Mmh, sure. While we're waiting for them, I don't see why not."
    show ggg 89
    no "Yay!"
    show ggg 83
    mc "Alright then."
    mc "See you on the beach in a few minutes."
    mc "Don't be late!"
    stop music2 fadeout 7
    play soundloop waves fadein 7
    scene ggg 91 with dis3
    play sound2 seagull
    play music2b pirate4 fadein 6
    bla "You, Nancy, and Nova leave the skeletons to their preparations at the post while the three of you head to the beach to wait for them."with dis15
    mct "Wow... you don't really see waters this clean in the real world anymore."
    mct "There's not a single cigarette butt or piece of plastic in sight."
    $ unlock_look("nova", 16)
    scene ggg 92
    no "*Running to the water* Whoaaaaaaa!" with dis15
    no "Look at this beach! It's so clean!"
    no "Tortuga's water was already pretty clear, but this is next level!"
    mc "Damn, when did you get changed?!"
    show ggg 93
    no "Nancy had a spare bikini in my size!" with dis12
    mc "Oh..."
    mc "She certainly knows how to pick outfits..."
    no "*Taking a deep breath* Ahhh, I'm so glad we finally get a moment to breathe. I needed it!"
    show ggg 96
    no "Sometimes it feels like our lives are a never-ending rollercoaster. Just when you think it's over... it throws you for another loop!" with dis
    show ggg 94
    mc "You removed your patch!"
    show ggg 96
    no "Yeah! I'm planning to swim in the ocean, and I can't get it wet."
    no "I can keep my left eye closed the whole time anyway."
    if novapath:
        show ggg 95
        no "And even if I open it for a bit... we're only going to be here for 20 minutes, so it's not really a problem."
        show ggg 94
        mc "Damn, I always forget how beautiful your eyes are."
        show ggg 97
        no "*Giggles* Thank you."with dissolve
        show ggg 96
        no "I used to be quite embarrassed about showing or talking about my condition in public, but thanks to you, I've grown more confident."with dissolve
        no "Now, I don't mind anymore."
        show ggg 94
        mc "As you shouldn't!"
    else:
        no "Honestly, I'm still a bit embarrassed to show or talk about my condition in public, but we're among friends here, so I don't mind."
        show ggg 94
        mc "You shouldn't feel that way in public either."
    mc "There's nothing to be ashamed of."
    if novapath:
        show ggg 95
        no "That's right!"
        show ggg 94
        menu:
            with dis 
            "Flirt [nova_pts]":
                mc "Goddammit Nova, that bikini of yours is making it so hard for me to stay focused. You're just too sexy."with dis06
                mc "I might need to get into the water to hide my... {i}enthusiasm."
                $ nova_points += 1
                play sound6 beat
                show screen heartbeat
                show ggg 97
                no "[mc]! Come on, don't be a perv!"with dissolve 
                no "We just slept together like... a few hours ago."
                no "Twice..."
                show ggg 98
                mc "Good things come in threes, you know...?"
                show ggg 97
                no "*Giggles* I do want to do it again too, but not now!"
                no "Although..."
                no "Well, perhaps after we log off we can..."
                play sound whoosh3b
                show ggg 99
                no "O-Ohh! Was that a swordfish jumping out of the water?!" with hpunch 
                no "SO COOL!"
                mc "Eh...?"
            "Swim with her":
                mc "What do you say, up for a little swim race?"with dis06
                mc "First one to cross the cove, wins!"
                show ggg 96
                no "Sure."
                no "But only if you promise to tell Alex about my incredible swimming skills when I win!"
                show ggg 94
                mc "*Chuckles* Deal."
    else:
        show ggg 96
        no "Yeah, I guess..."
        no "I'll try to improve!"
    $ unlock_look("nancy", 13)
    play sound footsteps3
    show ggg 100
    n "Whoaaa... this hidden beach looks stunning!" with dis15
    mct "Holy shit. You're the one looking stunning..."
    mct "I could settle for being stranded on a beach with Nova and Nancy wearing these."
    show ggg 101
    if nancypath:
        n "Aw, thank you!" with dis
        show ggg 102
        mc "W-What?"
        mc "Wait, did I say that out loud...?"
        show ggg 101
        n "You didn't, but your reaction pretty much confirmed what I thought you were thinking."
        n "I appreciate the compliment..."
        show ggg 102
        mc "You're way too smart for your own good, you know that?"
        show ggg 101
        n "*Giggles* I try my best."
    else:
        n "We'll have to thank Ed and Morty for this discovery." with dis
        show ggg 102
        mc "Indeed."
    show ggg 93
    no "I almost feel sad we can't spend more time here."with dis12
    no "I know we have to get to that island to obtain a new Gem of Doom, but I'd love to come back here after we're done."
    if nancypath and novapath:
        no "We could–"
        play sound2 slap3
        play sound3 whoosh6
        show ggg103
        n "Alright, [mc], what's your take on Nova's bikini?"with vpunch
        mc "11 out of 10."
        n "Good answer..."
        scene ggg 104
        no "P-Please, I could barely fill the top."
        show ggg 103
        n "With a sexy tummy like yours and so much {i}meat{/i} on your backside, that should be the least of your worries, baby."
        mc "I couldn't agree more."
        show ggg 104
        no "C-Can we go swim now, please?"
        show ggg 103
        n "Yeah, good idea... [mc] seems to be getting anxious to taste that water..."
        play sound footsteps3
        show ggg 106 with dis15
        play sound7 snow
        n "*Lying down* Seriously now though, go ahead!" with dis12
    else:
        play sound footsteps3
        show ggg 106 with dis15
        play sound7 snow
        n "*Lying down* Better to make the best of our time here while we can, then!" with dis12
        n "You guys can take a swim, if you want."
    n "I'd rather stay here and soak up some sun."
    show ggg 105
    no "Oh, that sounds tempting!"
    no "Mind if I join? I'm paler than a glass of milk."
    play sound2 snow
    show ggg 107
    n "*Tapping the towel* Of course! There's plenty of room for all of us..."with dis14
    show ggg 108
    no "*Giggles* Thanks!"
    play sound7 snow
    play sound8 debris
    show ggg 110 with dis15
    no "*Lying down* Aaaaaah... the sun feels so good..." with dis
    no "I haven't been to the beach in ages..."
    show ggg 109
    n "It really feels amazing..."
    show ggg 110
    no "I know being in Eternum means I can't get tanned in the real world, but it still feels like heaven."
    no "So comfortable..."
    no "It makes me feel so sleepy..."
    show ggg 109
    n "Well, that makes sense. It must be like... 4 or 5 AM in the real world now."
    n "We might not notice it, but our bodies are getting tired and craving some sleep. They're smarter than our minds sometimes!"
    show ggg 110
    no "Yeah, that makes sense..."
    no "Ahhhh... I think I'm gonna take a nap."
    no "Wake me up when Ed and Morty come back."
    show ggg 109
    n "I think I'm gonna close my eyes for a minute too..."
    n "They can... wake us up themselves..."
    play sound debris
    play sound2 snow
    show ggg 112
    mc "*Covering your face with the hat* Yeah... I might have dozed off earlier because of the tranquilizer dart, but I'm still feeling really tired..." with dis12
    mc "Taking a quick nap doesn't sound like a bad idea, to be honest."
    mc "We deserve a little break."
    show ggg 111
    mc "*Yawns* And well... we'll be more energized for the last part of the mission." with dis12
    mc "Mmmmhhh..."
    mct "Man, I didn't realize how tired I actually was until I finally sat down for a second..."
    mct "I feel so, so..."
    mct "Soooo sleepy..."
    mc "*Yawns* AAAaaghh..."
    mct "I'm gonna close my eyes just for a minute..."
    mct "Just... a minute..."
    stop music2b fadeout 9
    stop soundloop fadeout 13
    play sound ["<silence 0.9>", wave]
    scene black with dis3
    mc "Just a... quick... nap..." with dis14
    aaa "Hehehe..." 
    aaa "See you in a long, long, long time..."
    mc "Mmmmmhh..."
    play soundloop2 officesound fadein 4
    pause
    show screen tenyearslater with dis25
    pause
    hide screen tenyearslater with dis17

label office1:
    scene gs 1 with dis25
    mc "*Opening your eyes* Mmmmhh..." with dis15
    if starep2:
        mc "Hmm?"
        mct "Oh, fuck..."
        mct "Well, that didn't work."
    else:
        mct "Huh...?"
        mct "Where... am I...?"
        if starep:
            mct "Oh shit, not this again..."
        else:
            mc "*Yawns* (Oh man, I think that beach nap was longer than I intended.)"
    play music stanley fadein 6
    play sound6 stanleyvo1 volume 0.7
    bla "{cps=16}With his face still glued to the desk by dried beer, our long-forgotten hero finally opened his eyes... and stirred from his protracted, dizzying dream."
    stop sound6
    if not starep:
        mct "Eh...?"
        mct "The fuck is that voice?"
        play sound6 stanleyvo2 volume 0.7
        bla "{cps=15}Ten long years had passed since he and his friends gathered the ten Gems of Doom... yet, the sense of powerlessness that had overtaken him since then still lingered."
        stop sound6
    play sound3 chairoffice
    play soundlow chairmove
    scene gs 2
    if starep2:
        mc "*Sitting up* (Goddammit, I'm stuck in freaking Groundhog Day.)" with dis12
        mct "There has to be a way out..."
    elif starep:
        mc "*Sitting up* (Fuck, fuck, fuck...)"with dis12
        mct "Why am I here again?!"
        mct "Can't I escape this fucking place?!"
    else:
        mc "*Sitting up* (W-Who the fuck is that guy talking...?)" with dis12
        mct "Where is that voice coming from?!"
        mct "Where..."
        scene gs 5
        mc "*Looking around* (Where the hell am I...?)"with dis12
        mct "Is this an... office?"
        play sound6 stanleyvo3 volume 0.7
        bla "{cps=14.5}After a moment of reflection, our hero finally snapped back to reality and recalled the stark truth...{cps=1} {cps=16}it had already been five years since he abandoned his dreams and finally settled for an office job back in London."
        stop sound6
        mc "What are you talking about? I didn't abandon anything!"
        mc "I..."
        show gs 2
        mct "Shit, am I dreaming...?" with dis 
        mct "Can I dream while sleeping inside Eternum...?"
        mct "Perhaps I was transported to some weird server against my will?"
        mct "But... how does this voice know so much about me...?"
        mct "Fuck, I need to figure out what's going on and go back to the New World server as soon as possible."
        mod "Numbered/highlighted choices are steps to progress, check out other things if you'd like."
    if officedalia and officeluna:
        play sound email
        computer "*Ping*"
        mct "Huh?"
        mct "A new email?"
    elif starep and not starep2:
        scene gs 5
        play sound6 stanleyvo4 volume 0.7
        bla "{cps=15.2}After five years of working at the same desk doing the same job day in and day out, our hero felt a disorienting sensation wash over him...{cps=1.2} {cps=14}making him mistake his monotonous routine{cps=2.5} {cps=13}for deja vu."with dis2
        stop sound6
        scene gs 2
        mct "Yeah, “disorienting sensation” my ass."with dis12
        mct "Shit, I need to get out of here..."
label desk08:
    menu:
        with dis
        "Check your computer [gr][mt](1st and 3rd time)" if sta1:
            $ sta1 = False
            play sound type1
            show gs 3
            if sta1r:
                mct "Hmmm... maybe I can find some answers if I check the computer..." with dis
                mct "Looks like I have some unread emails."
            else:
                mct "Hmmm... maybe I missed something the first time." with dis 
            menu deskpc08:
                with dis
                "[gr]RE: Birthday Celebration!":
                    $ sta1b = True
                    play sound mouse
                    show screen email1 with dis04 
                    pause
                    play sound2 mouse
                    hide screen email1 with dis03
                    jump deskpc08
                "RE: Come to reception":
                    $ sta1c = True
                    play sound mouse
                    show screen email2 with dis04 
                    pause
                    play sound2 mouse
                    hide screen email2 with dis03
                    jump deskpc08
                "RE: Improvement needed":
                    play sound mouse
                    show screen email3 with dis04 
                    pause
                    play sound2 mouse
                    hide screen email3 with dis03
                    if not sta1d:
                        mct "Eternum's closure?"with dissolve
                        mct "We shut Eternum down...?"
                        play sound3 sniff
                        mc "*Sniffing your armpit* . . ."
                        mct "Oof. Guess they're not lying about that."
                        $ sta1d = True
                    jump deskpc08
                "[gr]RE: Read this" if officedalia and officeluna:
                    $ annieexit = True
                    play sound mouse
                    show screen email4 with dis04 
                    pause
                    play sound2 mouse
                    hide screen email4 with dis03
                    mct "This wasn't here before..."with dissolve
                    mct "The 7th floor, huh... that's where the left elevator goes."
                    jump deskpc08
                "Leave":
                    if starep and not annieexit:
                        mct "Nothing new..." with dis06
                    else:
                        mct "I need to get out of here..."with dis06
                    $ sta1r = False
                    play sound8 mouse
                    scene gs 2 with dis
                    jump desk08
        "Look at the photo frame" if sta2:
            show gs 6 with dis 
            if sta2r:
                mct "What the hell..." with dis
                mct "Is that... Dalia?"
                mct "In a wedding dress with... Jerry?!"
                mct "Not a fucking chance. She wouldn't be caught dead with Jerry in her life."
                mct "And even if it were true, why would I have a picture of their wedding on my own desk?! That's like the ultimate cuck move!"
                play sound6 stanleyvo5 volume 0.7
                bla "{cps=15}Despite his attempts to cope, our hero understood all too well why he kept that picture on his desk...{cps=2} {cps=15}to remind him of the life he once lived...{cps=2} {cps=15}the one he could have pursued...{cps=2} {cps=12}the one he lost."
                stop sound6
                mc "Oh, fuck off..."
                mc "That doesn't make any sense..."
                $ sta2r = False
            else:
                mct "Ugh, this is still the most bizarre thing in this whole circus."with dis
            $ sta2 = False
            show gs 2 with dis
            jump desk08
        "Peer under your desk" if sta3:
            play sound6 stanleyvo6 volume 0.7
            show gs 7
            bla "{cps=15}He glanced beneath his desk, only to see what he already knew he'd find...{cps=1} {cps=13}a heap of garbage, expired condoms, and empty bottles of booze." with dis12
            stop sound6
            if sta3r:
                mc "Jesus, what a mess..."
                mc "The boss better not see this."
                play sound chairoffice
                scene gs 2
                mc "I-I mean... wait, I don't even work here!" with dissolve
                mc "I don't give a fuck about any “boss”! Focus, [mc]!"
                $ sta3r = False
            elif starep2:
                mct "Yeah, still the same shit."
                scene gs 2 with dis
            else:
                mct "He seems to be sticking to a script. He said the exact same thing last time."
                mct "Am I being punked...?"
                scene gs 2
                mct "I feel like I'm in The Truman Show or something..." with dis
            $ sta3 = False
            jump desk08
        "Stand up":
            play sound chairoffice
    play sound2 chairmove
    scene gs 4
    mct "I need to get back to Nancy and Nova ASAP." with dis
    if starep:
        mct "Every minute I’m here increases the chances of them being in danger."
    else:
        mct "I should try to find someone else and ask them what the hell is going on."
        play sound6 stanleyvo7 volume 0.7
        bla "{cps=16}Standing up, our hero resolved to seek out a coworker for conversation...{cps=1} {cps=17}only to find that everyone else had {cps=18}apparently already left for the day."
        stop sound6
        mct "Get out of my head..."
    scene gs 8 with dis17
    if starep:
        play sound6 stanleyvo8 volume 0.7
        bla "{cps=17.5}The empty office served as a stark reminder of his own–{nw}"with dis12
        stop sound6
        if starep2:
            mc "YES, YES. You've told me that quite a few times already, buddy."
            mc "Don't you have a mute button?"
        else:
            mc "Yes, yes... my friends and lovers abandoned me."
            mc "Don't you ever shut up?"
    else:
        play sound6 stanleyvo8 volume 0.7
        bla "{cps=16}The empty office served as a stark reminder of his own life.{cps=2} {cps=19}It wasn't after he and his friends shut down Eternum for good when collecting the ten Gems of Doom,{cps=2} {cps=17}that our hero finally confronted the harsh reality."with dis12
        stop sound6
        mct "Don't listen to him... he just wants to make you mad..."
        mct "We don't have the ten Gems of Doom yet..."
        play sound6 stanleyvo9 volume 0.7
        bla "{cps=17}He possessed no tangible skills in the real world,{cps=1} {cps=18}and those he considered friends...{cps=2} {cps=17}even lovers...{cps=2} {cps=17}abandoned him when he ceased being useful."
        stop sound6
        mc "Shut the fuck up..."
        mc "They'd never do that..."
    stop soundloop2 fadeout 11
    play sound dooropen4
    play sound2 dooropen4
    scene gs 9 with dis17
    if starep:
        mct "Alright... here we go again..." with dis08
    else:
        mct "Yes! The exit has to be that way." with dis08
    play sound3 footsteps
    scene gs 10 with dis17
    play sound6 stanleyvo10 volume 0.7
    bla "{cps=16}Our hero strode through the deserted floor until he reached the pair of elevators.{cps=1} {cps=15}After a brief moment of consideration,{cps=5} {cps=15}he opted for the one on his right and continued his journey."with dis12
    stop sound6
    menu menuelevator:
        with dis
        "Take the right elevator":
            play sound footsteps
            scene gs 12 with dis17
            pause .3
            play sound elevator
            scene gs 12b with dis14
            mct "Okay..." with dis08
            if starep:
                if officedalia and officeluna:
                    mct "There's no point in going back to the meeting room or the reception desk, it would end the same."
                    mct "I guess my only option is to try escaping the office directly... just... faster this time?"
                elif officedalia:
                    mct "It doesn't make sense for me to go back to the meeting room, the outcome would be the same."
                    mct "I guess I could either attempt to escape the office directly... or try my luck at the reception desk."
                elif officeluna:
                    mct "It doesn't make sense for me to go back to the reception desk and retrace my steps, the outcome would be the same."
                    mct "I guess I could either attempt to escape the office directly... or try my luck at the meeting room and see if I can find someone else."
                if escapesta:
                    mct "I mean, I've already tried escaping directly, but maybe if I {i}keep{/i} trying..."
            elif sta1b and sta1c:
                mct "I received emails mentioning both the meeting room and reception."
                mct "I can probably find someone in either of those areas."
                play sound6 stanleyvo11 volume 0.7
                bla "{cps=8}Ah... {cps=17}another electrifying choice in our hero's life! {cps=1} {cps=19}Not only could he choose the elevator, but also the next floor to visit! {cps=1} {cps=20}This had already become his most thrilling day since his adventurous youth in Eternum."
                stop sound6
                mc "You can shove your sarcasm up your ass..."
            else:
                mct "Where to go now..."
                play sound6 stanleyvo12 volume 0.7
                bla "{cps=15}Our hero was once again faced with{cps=5} {cps=15}a single choice,{cps=2} {cps=15}another chapter{cps=5} {cps=15}in his monotonous life.{cps=1} {cps=15}After a moment of reflection,{cps=6} {cps=15}he finally decided to try his luck at the reception desk."
                stop sound6
                mct "Mmmmh... I guess I have no choice but to play along."
            menu:
                with dis12
                "[gr]Reception desk" if not officeluna:
                    jump receptiondesk
                "[gr]Meeting room" if (sta1b and not officedalia) or (starep and not officedalia):
                    jump meetingroom
                "Escape" if starep:
                    $ escapesta = True
                    jump officeleave
        "Take the left elevator" if not annieexit:
            scene gs11 with dis12
            play sound buttonpush
            pause 1.5
            play sound6 stanleyvo13 volume 0.7
            bla "{cps=18}The elevator on the left only went up to the 7th floor and was off-limits to employees at his level...{cps=1} {cps=18}something our hero knew well."with dis12
            stop sound6
            if staeleleft:
                mct "Still doesn't work..."
            else:
                mc ". . ."
                play sound6 stanleyvo14 volume 0.7
                bla "{cps=16}Despite this fact,{cps=2} {cps=16}he still tried to open it.{cps=1} {cps=18}Maybe as an attempt to create an illusionary sense of choice in his life,{cps=1} {cps=18}or...{cps=3} {cps=19}perhaps his thoughts were simply still clouded from...{cps=3} {cps=17}last night's alcohol intake."
                stop sound6
                mct "I'm starting to hate this guy..."
                $ staeleleft = True
            if annieexit:
                scene gs 90
                mc "Hmmm..." with dis14
                play sound6 stanleyvo15 volume 0.7
                bla "{cps=16}Our hero glanced at the stairs,{cps=1.5} {cps=16}briefly considering using them.{cps=1} {cps=16}However,{cps=2} {cps=16}he quickly dismissed the idea,{cps=3} {cps=17}knowing all there was of interest on other floors was...{cps=3} {cps=19}easily accessible using the right elevator."
                stop sound6
                scene gs 10
                mc "Hmm." with dis
                scene gs 90
                mc "Hmmmm..." with dis
                play sound6 stanleyvo16 volume 0.7
                bla "{cps=19}He looked at the stairs again and couldn't help but laugh at his own stupidity.{cps=1} {cps=18}Realizing he had no time to waste, he continued his journey by taking the right elevator."
                stop sound6
                scene gs 10
                mc ". . ." with dis
                scene gs 90
                mc ". . ." with dis12
                play sound6 stanleyvo17 volume 0.7
                bla "{cps=19}I...{cps=0.8} {cps=19}said...{cps=0.7} {cps=19}he entered the right elevator."
                stop sound6
                scene gs 10
                mc "Yeah... that makes sense."with dis
                mc "I'm gonna take the right ele–"
                stop sound6
                jump annieofficeleave
        "[gr]Take the left elevator" if annieexit:
            if annieexit:
                scene gs 90
                mc "Hmmm..." with dis14
                play sound6 stanleyvo15 volume 0.7
                bla "{cps=16}Our hero glanced at the stairs,{cps=1.5} {cps=16}briefly considering using them.{cps=1} {cps=16}However,{cps=2} {cps=16}he quickly dismissed the idea,{cps=3} {cps=17}knowing all there was of interest on other floors was...{cps=3} {cps=19}easily accessible using the right elevator."
                stop sound6
                scene gs 10
                mc "Hmm." with dis
                scene gs 90
                mc "Hmmmm..." with dis
                play sound6 stanleyvo16 volume 0.7
                bla "{cps=19}He looked at the stairs again and couldn't help but laugh at his own stupidity.{cps=1} {cps=18}Realizing he had no time to waste, he continued his journey by taking the right elevator."
                stop sound6
                scene gs 10
                mc ". . ." with dis
                scene gs 90
                mc ". . ." with dis12
                play sound6 stanleyvo17 volume 0.7
                bla "{cps=19}I...{cps=0.8} {cps=19}said...{cps=0.7} {cps=19}he entered the right elevator."
                stop sound6
                scene gs 10
                mc "Yeah... that makes sense."with dis
                mc "I'm gonna take the right ele–"
                stop sound6
                jump annieofficeleave
    scene gs 10 with dis15
    jump menuelevator
label receptiondesk:
    play sound elevatoride
    scene gs 12b with vpunchslow
    pause 2
    play sound2 elevatorstop
    pause .6
    scene gs 12b with vpunchslow
    pause 0.5
    play sound3 ding
    play sound4 elevator 
    show gs 14 with dis15
    pause
    play sound6 footsteps
    scene gs 16
    mct "Alright... this should be reception." with dis15
    recep "Yeah, Susy, I fucking swear on my life."
    show gs 17
    recep "This bitch goes and tells me “I can do that job for you if you want”." with dis12
    recep "And I'm like, shut up, bitch. Do you think I'm an idiot?"
    mc "Hey, can you help me??"
    recep "*Whispering* Oops, there's someone here, gotta hang up. Call you later!"
    show gs 18
    cha "Good evening, sir, how can I..." with dis08
    show gs 20
    cha "Oh, it's you." with dis
    show gs 19
    mc "Oh, no... Charlotte?!"
    mc "*Sighs* You're literally the last person I wanted to see here."
    mc "Well... maybe after William Bardot. Or... Gertrude."
    show gs 20
    cha "Get used to it, loser."
    cha "I got this job on my own merits, and not by kissing up like someone else."
    show gs 19
    mc "I see you still have the same old ugly attitude. But... you're also brainwashed to boot, so I doubt you can be of any help."
    show gs 20
    cha "Ehh?"
    cha "What are you babbling about now, nerd?"
    show gs 19
    mc "Forget it..."
    show gs 20
    cha "*Sighs* Just get the fuck out of here already, we're closing up in 30 minutes anyway."
    show gs 19
    if sta1c:
        mc "You're the one who called me! I had an email!"
    else:
        mc "Don't you have any messages for me or... any idea of what I'm supposed to do?"
    show gs 20
    cha "What?"
    cha "Oh... wait."
    show gs 21
    cha "Yeah... now that you mention it, Mrs. Whitmore called for you." with dis
    cha "She said she needs to have a talk with you in meeting room number 2, on the 5th floor, in like... 10 minutes ago."
    show gs 20
    cha "Hopefully to fire you." with dis
    show gs 19
    mc "Thank you..."
    show gs 20
    cha "And... you also got a call – they left a message."
    cha "They said your phone was off or something."
    show gs 19
    if officedalia:
        mct "Hmm... right, my phone must be on the table in the TV room again, just like I found it in the first loop."
    else:
        mct "Hmmm... true, I couldn't find my personal phone anywhere."
    play sound ["<silence 0.35>", beep2b]
    play sound2 ["<silence 0.35>", button]
    show gs 22
    cha "Wanna hear it or not?" with dis 
    mc "Sure."
    show gs 23
    p "{i}Hey [mc]!" with dis
    mc "Holy crap, is that Penny?!"
    p "{i}Long time no see, eh?"
    p "{i}Listen, I was just calling to see if you've heard anything about my mom. I haven't heard from her in a few months."
    p "{i}You know how she, Dalia, and I stopped talking to each other after what happened that Christmas in '38, so I thought... I don't know, I thought maybe she reached out to you."
    mct "What...? There's no power in this world strong enough to stop Nancy from talking to her daughters."
    p "{i}I've been trying to reach you for a few days now, but your phone's been off, or maybe you changed your number?"
    p "{i}Anyway, if you hear anything, let me know!"
    p "{i}And if you're free, don't forget to catch my interview on NBC today at 6! Bigger audience means more sponsors!"
    p "{i}See ya!"
    play sound2 button
    play sound beep2b
    bla ". . ." 
    cha "Holy moly!"
    show gs 18
    cha "Was that Penelope Carter?!" with dis
    cha "You're still in contact with her?!"
    cha "Do you think you can arrange for us to meet? Tell her I'm Charlotte Bartimore, we were best friends 10 years ago!"
    if penelopepath:
        mc "You only met her once at that Halloween party, and... no, I can't."
    else:
        mc "No, I can't."
    cha ". . ."
    show gs 19
    cha "Mmh." with dis
    show gs 17
    cha "Well, fuck you, then." with dis 
    cha "No wonder you're so fucking alone."
    cha "Get the hell out of my sight, you pathetic nerd."
    mc "Always a pleasure, Charlotte..."
    play sound7 elevatoride fadein 1
    play soundlow ["<silence 3.5>", ding] volume 0.66
    scene gs 13b with dis25
    play sound6 stanleyvo18 volume 0.7
    bla "{cps=19}Our hero left the reception desk and took the elevator back to the meeting room floor.{cps=1.4} {cps=18}Despite his best efforts to endure the harsh words of the receptionist,{cps=2} {cps=18}he couldn't hold back his tears any longer and began to cry." with dis15
    stop sound6
    mc "What the hell are you talking about? I'm not crying."
    play sound6 stanleyvo19 volume 0.7
    bla "{cps=18}However,{cps=2} {cps=18}he had to compose himself.{cps=0.9} {cps=20}He then made his way to the meeting room number 2 to meet his boss...{cps=1.2} {cps=16}unaware that an unexpected turn of events{cps=4} {cps=18}was about to unfold."
    stop sound6
    mct "An unexpected turn of events...?"
    mc "*Sighs* (This can't be good...)"
    play sound footsteps
    scene gs 70 with dis2
    play sound2 dooropen4
    mc "*Opening the door* Uh... hello there!" with dis12
    mct "Is this my “boss”?"
    mc "Hello?"
    play sound5 footsteps
    scene gs 71
    mc "Good evening, ma'am." with dis12
    mc "I was told to..."
    mc "Wait."
    play sound3 chairoffice
    play sound4 whoosh6
    scene gs 72
    mc "*Sitting down* Luna?!" with vpunchslow
    mc "It's you!"
    mc "LUNA!" with hpunch 
    show gs 74
    l "Jesus, don't shout..."
    l "I have a big headache..."
    show gs 73
    mc "Oh god, what happened to you? You look... terrible."
    show gs 74
    l "Whoa, thanks. You don't look so great either."
    show gs 72
    mc "No, I mean... j-just that your eyebags are... pretty bad."
    show gs 74
    l "Mmh, I haven't been sleeping well."
    show gs 73
    mc "Do you know where we are?"
    mc "Or how we ended up here?!"
    show gs 74
    l "The boss called, she wants to talk to us."
    show gs 73
    mc "No, not that! I mean in this weird ass office!"
    mc "Do you also hear this annoying narrator all the time?"
    show gs 74
    l "This what...?"
    show gs 73
    mc "Agh, dammit!"
    mc "Why am I the only one acting normal?!"
    show gs 74
    l "Whoa... you're tripping hard today."
    l "You've gotta hook me up with whatever you're on."
    show gs 73
    mc "What?!"
    play sound dooropen4
    xb "*Opening the door* Forgive my tardiness."
    play sound2 footsteps
    scene gs 75
    x "And thank you for coming." with dis14
    mc "Oh come on, you've got to be kidding me..."
    play sound3 chairoffice
    play sound5 chairmove
    play sound4 ["<silence 0.6>", type1]
    scene gs 75b
    x "*Sitting down* I will be extremely brief, don't worry." with dis12
    x "I've called this meeting because we need to address a critical issue."
    x "When I hired each of you, it wasn't because we were buddies, but because I thought you could significantly contribute to our company."
    x "However, your performance hasn't been up to par. Right now, you're the least productive developers on the team, and your results are FAR from satisfactory."
    show gs 76
    mc "A-Alex?"
    mc "You're also brainwashed?!"
    show gs 77
    x "What did you just call me...?"
    show gs 76
    mc "Huh?"
    show gs 77
    x "It's {i}Mrs. Whitmore{/i} to you."
    show gs 76
    mc "Whitmore...?"
    mc "That's the name you chose after Bardot?"
    show gs 77
    x "That's my husband's name."
    show gs 76
    mc "Your WHAT?!"
    play sound type2
    show gs 75b
    if alexpath:
        x "*Sighs* Good Lord, it's been a decade and you're still hung up on that?"
        x "Yeah, [mc], we slept together."
    else:
        x "*Sighs* Good Lord, you're still as immature as you were at 18."
        x "Yeah, we all had a good time playing Eternum together, but once we collected the Gems of Doom, we shut it down."
    stop sound
    show gs 77
    x "Ten fucking years ago."
    x "It's time to move on and make something meaningful out of your life, don't you think?"
    show gs 76
    mc "W-What?"
    x ". . ."
    show gs 77
    x "Are you drunk again...?"
    show gs 79
    x "Is he drunk?"
    show gs 81
    l "I don't know. Maybe?"
    show gs 77
    x "Jesus Christ..."
    play sound7 type1
    show gs 75b
    x "*Sighs* Anyway, Luna, we really need to talk about your productivity too."
    x "We've switched your project three times already, and you're still struggling to find your place."
    stop sound7
    show gs 79
    x "Not to mention there have been reports from your colleagues about... illegal substances during office hours."
    show gs 80
    l "Excuse me...? Are you accusing me of something?"
    show gs 79
    x "I'm not accusing you of anything. I'm simply conveying what's been reported."
    x "But... in any case, you need to improve your performance, or we'll have to have a more serious conversation. Are we clear?"
    show gs 81
    l "Yes, boss, crystal clear..."
    play sound type1
    show gs 75b
    x "I'll go get the new project guidelines you need to complete by the end of the month."
    x "Please, wait here, I'll be back in 5 minutes."
    play sound chairoffice
    play sound2 chairmove
    scene gs 82 with dis22
    play sound3 doorglass
    play sound5 footsteps2
    play sound6 stanleyvo20 volume 0.7
    bla "{cps=15}Luna watched expressionlessly as Alexandra left the room...{cps=1.5} {cps=17.5}her gaze lingering until she disappeared around the corner of the hall." with dis17
    stop sound6
    play soundlow zip volume 0.3
    play sound4 ["<silence 0.4>", noise3]
    scene gs 83
    l "Finally, she's gone... what a goddamn pain in the ass." with dis12
    mc "S-Since when do you curse? Doesn't sound like you."
    play sound clothes3
    show gs 84
    l "At last, we've got some peace..." with dis 
    show gs 86
    mc "What?! Are those... pills?"
    mc "Do you do drugs?!"
    show gs 87
    l "Relax, it's just E. To calm the nerves."
    show gs 86
    mc "You take ecstasy?!"
    mc "YOU?! What the hell, Luna..."
    mc "Does Mr. Hernandez know about this?"
    show gs 87
    l "Huh?"
    l "My dad died six years ago."
    play sound impactwood
    show gs 86
    mc "MR. HERNANDEZ IS DEAD?!" with vpunch 
    mc "This is the worst timeline ever..."
    show gs 87
    l "Look, she's gonna be back soon, and I'm taking this with or without you."
    l "Want some or not?"
    play soundlow wood2
    show gs 88
    mc "*Grabbing one of the pills* Uh..." with dis17
    menu:
        with dis12
        "Take the pill":
            $ lunapill = True
            mc "Well..."with dis08
            mc "Maybe popping this will finally wake me from this nightmare."
            mc "I can't think of a more perfect time to give it a shot..."
        "Refuse":
            mc "Uh... I appreciate the offer, but... it's not really my thing, sorry."with dis08
            mc "Taking Ecstasy for the first time isn't exactly what I need right now."
    play sound6 stanleyvo21 volume 0.7
    scene gs 89
    bla "{cps=17}Our hero felt the weight of weeks of depression and anxiety crash down on him all at once.{cps=0.7} {cps=17}Overwhelmed by his suffering,{cps=3} {cps=17}he accepted the pill his old friend offered and swallowed it whole." with dis17
    stop sound6
    if not lunapill:
        mc "Wait, what?! That's not what I said!"
        mc "I refused!"
    else:
        mc "Down the rabbit hole..."
    scene black with dis27
    pause
    scene gs 69 with dis27
    mc "*Opening your eyes* Mmmmh..."with dis15
    if officedalia:
        mc "W-What just..."
        mc "Oh man, not this again..."
    else:
        mc "W-What... just happened...? Where's Luna?"
        mc "Why can't I remember anything after she offered me the pill...?"
    play sound6 stanleyvo22 volume 0.7
    bla "{cps=14}After a disorienting trip induced by the psychedelic stimulant,{cps=1} {cps=15}our hero awoke drenched in sweat and vomit,{cps=1.5} {cps=16}wondering if this would finally be the reason he got fired."
    stop sound6
    if officedalia:
        if lunapill:
            mc "You're a fucking cheater!"
        else:
            mc "You're a fucking cheater! I didn't even take it!"
    else:
        if lunapill:
            mc "W-What?! I don't even remember taking it!"
        else:
            mc "W-What?! I didn't even take it!"
    mc "Everything just turned black!"
    play sound6 stanleyvo23 volume 0.7
    bla "{cps=16}Despite feeling dizzy and repulsed by what he had become, he finally mustered the strength to stand up and leave the office for the day."
    stop sound6
    mc "I don't even feel dizzy!"
    play sound6 stanleyvo24 volume 0.7
    bla "{cps=17.5}He decided to stand up and leave the office for the day."
    stop sound6
    if officedalia:
        mc "Are you really gonna do this again?"
    else:
        mc "But–"
    play sound6 stanleyvo25 volume 0.7
    bla "{cps=19}He left{cps=1.5} {cps=19}the office{cps=1.3} {cps=19}for the day."
    stop sound6
    mc "You son of a bitch..."
    if officedalia:
        mct "Fuck... it's like he can control all of my movements."
        mc "*Sighs* (But I guess I have no other choice.)"
    else:
        mc "*Sighs* (I guess I have no other choice.)"
        mct "Perhaps I can find the way out of this nightmare outside."
    mct "Let's get the fuck out of here..."
    $ officeluna = True
    jump officeleave
label meetingroom:
    play sound elevatoride
    scene gs 12b with vpunchslow
    pause 2
    play sound2 elevatorstop
    pause .6
    scene gs 12b with vpunchslow
    pause 0.5
    play sound3 ding
    play sound4 elevator 
    show gs 13 with dis15
    pause
    play sound6 footsteps
    scene gs 13b
    if officeluna:
        mct "Alright... back to the 5th floor." with dis12
        mct "Let's see what I can find in the general lounge..."
    else:
        mct "Alright... floor 5. The meeting lounge should be here." with dis12
    mct "Let's do this."
    play sound dooropen4
    scene gs 24 with dis15
    play sound6 stanleyvo26 volume 0.7
    bla "{cps=16}Ah, the meeting lounge...{cps=1.3} {cps=16}the place where friendships are forged, hard workers find respite, and colleagues discuss the latest advancements in the video game industry."with dis12
    stop sound6
    mct "Yes! There has to be someone here somewhere!"
    mct "Perhaps in that room at the end?"
    play sound2 doorglass
    scene gs 25 with dis15
    play sound6 stanleyvo27 volume 0.7
    bla "{cps=16}However, after losing contact with his old friends,{cps=1.5} {cps=15}our hero became increasingly antisocial.{cps=0.8} {cps=16}As a result, none of his coworkers even noticed his absence.{cps=1.5} {cps=16.5}By the time he arrived, everyone else had already left."with dis12
    stop sound6
    mc "You have to be fucking kidding me..."
    show gs 26
    mc "They didn't even leave me any sushi..."with dis 
    mc "*Sighs* Fuck."
    mc "Nancy, Nova, where are you...?"
    play sound ["<silence 0.5>", chair1]
    scene gs 27 with dis15
    mc "*Sitting on the couch* Aghh..." with dis12
    mct "I need to think about the next step. There has to be something I can do to escape this nightmare..."
    mct "But what...?"
    play sound6 stanleyvo28 volume 0.7
    bla "{cps=13}Our hero felt utterly defeated.{cps=1} {cps=17}With no meaningful goals left for the day, he turned on the TV to watch his favorite talk show, hoping it would help him forget his pointless life."
    stop sound6
    if officeluna:
        mct "The TV...?"
        mct "Wait... it's true!"
        mct "Penny mentioned in her call that she'd be on NBC at 6!"
        mc "*Grabbing the remote control* (Maybe this can clear things up...)"
    else:
        mc ". . ."
        mc "*Grabbing the remote control* Okay, I'll play along..."
    play sound button
    play music2 talkshow fadein 4
    stop music fadeout 4
    play sound2 crowdcheer
    scene gs 28 
    egg "Good evening, ladies and gentlemen!" with dis
    show gs 29
    egg "Welcome to Studio Retro! This is your favorite host, Anton Eggrik!" with dis12
    egg "Tonight, we have a treat for you! A very, very special guest straight from the heart of Kredon!"
    mc "Eh...?"
    scene gs 30
    egg "She's beautiful, she's smart, she's the epitome of glamour, and she's already stolen all of our hearts." with dis
    egg "A journalist, a model, an actress, and an influencer with over 19 million followers on Instagram alone!"
    egg "You've been clamoring for her, and she's finally gracing our stage tonight!"
    show gs 31
    egg "The one and only... PENELOPE CARTER!" with dis
    mc "W-What?"
    egg "Please, let's give her a warm Retro welcome!"
    play sound crowdcheer
    play sound6 crowdfangirls
    show gs 32 with dis12
    pause
    show gs 33
    p "Thank you, Anton."with dis
    p "It's truly a thrill to finally be on your fabulous show."
    show gs 34
    egg "It's an absolute pleasure to have you here, Penelope."
    egg "And I think I can speak for everyone here when I say that! Tickets to see tonight's show LIVE were sold out in mere seconds!"
    show gs 38
    egg "Yes, I'm talking about you, green shirt!" with dis08
    play sound7 crowdlaugh
    egg "I don't remember seeing you between the crowd when Jonah Hill was here last week!"
    show gs 34
    egg "But let's dive right in, Penelope, shall we?"with dis08
    egg "Your latest film has been causing quite the stir. And tomorrow's finally the big day! Are you nervous?"
    show gs 35
    p "I'm always a bit nervous before the premiere of any movie, but this time I'm confident, Anton."
    p "Both my co-stars and the entire team, really, have put in astonishing work."
    p "It's been quite the challenge, but I have no doubt people will love it."
    play sound2 crowdcheer
    show gs 36
    egg "As humble as she is beautiful."
    show gs 37
    egg "Now, stop me if I'm being too bold, but I've gotta ask..."
    egg "It's been pretty much confirmed that you appear naked in this movie... the most anticipated topless scene in the history of cinema!"
    show gs 35
    p "That's correct, I do."
    show gs 37
    egg "Tomorrow, literally millions of men are gonna be waiting in line at their local theater because of it."
    play sound5 crowdlaugh2
    show gs 38
    egg "Yeah, I'm talking about you, green shirt! I know you've already set your alarm for 6 AM!" with dis08
    show gs 42
    egg "Seriously though, how do you feel about that?"
    egg "Was it a hard decision?"
    show gs 39
    p "Maybe a bit at first, but the director and my colleagues made me feel incredibly comfortable throughout."
    p "In the end, I felt completely free. I'm so glad I went through with it."
    show gs 41
    p "And... there are also some other exciting surprises in the movie. But you'll have to go and see it for yourselves!"
    p "I hope you won't be disappointed..."
    play sound crowdcheer
    show gs 40
    egg "Oh, she's such a tease!"
    show gs 37
    egg "Can we perhaps get a little sneak peek?"
    egg "Could you show us that jaw-dropping dress of yours?"
    show gs 39
    p "*Giggles* Well... alright, just a little. Just for you, Anton!"
    play sound2 cheersmall
    show gs 43
    egg "Oh my, look at those curves..."with dis12
    egg "You're driving the crowd wild!"
    show gs 44 with dis
    pause
    play sound3 crowdcheer
    show gs 45
    p "Muah!" with dis08
    show gs 46
    egg "OOOOOoooohhh boy!" with dis
    egg "I'm gonna have to ask you to stop, Penelope! You're killing me!"
    play sound4 chair1
    show gs 41
    p "*Giggles* You're such a flatterer!" with dis 
    show gs 37
    egg "*Chuckles* Although... at the risk of being heartbroken, I've gotta ask."
    egg "Was that last kiss directed to me? Or is there someone special, perhaps...?"
    egg "The rumor mill has been churning out stories about your off-screen chemistry with your co-star, Liam Hara."
    egg "Is there any truth to it?"
    show gs 41
    p "Um..."
    p "*Giggles* Well, we wanted to keep it low-profile, but... I guess it's already too late for that now."
    show gs 39
    p "Yes, we're together."
    play sound crowdcheer
    play sound2 crowdfangirls
    play sound3 cheersmall fadein 2
    show gs 40
    egg "NO WAY!" with dis 
    egg "You heard it here first, ladies and gentlemen!"
    show gs 37
    egg "Such a lucky man..."
    egg "Alright, this is getting interesting!"
    egg "Now that we've broken the ice and finally got confirmation, I have a question for the ladies out there..."
    egg "And remember, you don't have to answer if you don't want to."
    egg "How's Liam in bed...?"
    play sound3 crowdcheer
    play sound4 crowdfangirls
    show gs 41
    p "*Giggles* Well, he...{w=1.3}{nw}"
    play sound3 button
    play sound4 turnofftv
    stop sound
    stop sound2
    stop music2 
    play music stanley fadein 6
    scene gs 47
    mc "OKAY, ENOUGH." with flashfaster
    mc "Penny would never appear naked in a movie."
    mc "A-And she wouldn't date Liam Hara!"
    mc "Whoever that is..."
    play soundloop [vibration, "<silence 0.45>"] 
    play soundloop2 [vibration, "<silence 0.45>"] 
    pause .6
    scene gs 48
    mc "Huh...?" with dis12
    mct "A phone?"
    play sound6 stanleyvo29 volume 0.7
    bla "{cps=16.3}Our hero finally found the phone he thought he'd lost on a nearby table, receiving an unexpected call.{cps=0.7} {cps=16.5}Not accustomed to receiving many messages, he picked up without a second thought."
    stop sound6
    stop soundloop
    stop soundloop2
    play sound beep2b
    play sound3 grab
    show gs 49
    mc "*Picking up the phone* Hello...?"with dis04
    d "[mc]...?"
    play sound2 chair1
    show gs 50
    mc "Dalia?! Is that you?!" with dis 
    d "Wha...? Y-Yeah, it'sh me..."
    mc "Where are you?! Are you also trapped in here?!"
    d "Uh, I think sho... are you... in your office...? I was jus'... *hic* passin' by..."
    mc "I am! Do you know how to leave this place?"
    d "I'll come find ya... I-I need to see ya..."
    d "J-Jus' wait there..."
    mc "O-Okay! I'll wait right here! I'm at the 5th floor!"
    mc "Dalia?"
    mc "You still there?"
    mc ". . ."
    mct "She hung up."
    mct "Okay... this could be my way out of this bizarre world."
    mct "She sounded dizzy, but if I can actually see a real–"
    c "{i}*Humming* Mm-hm-hm-mmmh..."
    show gs 51
    c "{i}*Humming* Don't wanna see no blood, don't be a macho man..." with dis12
    mc "What the hell..."
    c "{i}*Humming* You wanna be tough, better do what you can..."
    c "{i}*Humming* So beat it..."
    play sound2 chair2
    scene gs 52
    mc "*Standing up* Chang?!" with dis
    scene gs 58
    c "Mmh?" with dis
    scene gs 53
    c "Whooopa! The man himself!" with dis08
    c "It's been a while, [mc]! How've you been, buddy?!"
    c "We really need to catch up one of these days."
    show gs 54
    mc "A-Are you real?! What is this place?"
    show gs 55
    c "Hah! Still cracking jokes, I see!" with dis08
    c "And point taken! I know we haven't hung out much since my promotion, but you better not miss our annual barbecue with Micaela and the kids!"
    show gs 56
    mc "Kids...? What kids?"
    mc "Y-you and Micaela already have kids?!"
    show gs 55
    c "*Chuckles* Of course we do!"
    show gs 57
    c "Although... it's a little bit worrying that you ask that, considering you're their godfather, not gonna lie."
    c "Have you been drinking again?"
    show gs 58
    mc "What the hell is going on..."
    show gs 57
    c "Is all of this because I replaced you with Andrew as my padel partner?"
    show gs 58
    mc "Of course not! I just..."
    mc "Wait, you have a new padel partner?!"
    mc "Maaaan, that's our thing!"
    mc "I mean... I know with everything that's been happening in Eternum we haven't had many opportunities lately, but..."
    show gs 55
    c "Oh man, Eternum... that brings back memories of our Kredon days. Remember those?"
    c "Time sure flies..."
    show gs 56
    mc "The fuck do you mean?! I was playing Eternum just this morning!"
    show gs 55
    c "Exactly! It really does feel like that."
    show gs 56
    mc "That's not what I mea–"
    show gs 53
    c "Anyway, I've gotta hit the road now, buddy." with dis
    c "Gotta pick up the kids from school, you know the drill!"
    c "Take care and we'll catch up soon! See ya!"
    scene gs 58b 
    play sound6 stanleyvo30 volume 0.7
    bla "{cps=16}Chang hurriedly left the office, not glancing back.{cps=0.8} {cps=16}Our hero had painfully observed how,{cps=2} {cps=16}with each passing year,{cps=2} {cps=17}his old friends slipped further and further from his life." with dis17
    stop sound6
    mc "Shut the fuck up. That was not my Chang."
    play sound6 stanleyvo31 volume 0.7
    bla "{cps=16}However...{cps=1.5} {cps=16}the call from Dalia Carter sparked a glimmer of hope within him, so he decided to head to the coffee area and wait for her.{cps=1} {cps=16}This...{cps=1.4} {cps=16}was his chance."
    stop sound6
    $ officedalia = True
    menu:
        with dis 
        "Go to the coffee area and wait for Dalia [gr][mt](more content)":
            scene gs 59 with dis2
            mc "*Biting your nails* (This can't be real... this has got to be some Eternum trickery. But... it's weird... this narrator knows way too much about my life.)"with dis 
            mct "Could someone be pranking me...?"
            mct "No... not when we're in the middle of our mission to get to the Island of the Lost Souls."
            mct "But how the heck did I end up here, then?!"
            d "[mc][namelong]..."
            show gs 60
            mc "*Turning around* Huh??" with dis
            mc "Dalia! Finally!"
            mc "Please, tell me it's the real you."
            show gs 61
            d "As real as a... *hic* as a 300 lbs sssquat."
            show gs 60
            mc "Are you drunk...?"
            show gs 61
            d "Nah... I jus' had a couple of drinks wit' my frien's."
            show gs 63
            d "There was a TV in the bar, and they were showin' Penelope's inter...interview..."
            d "Can you 'elieve the things that b-bitch said?"
            show gs 62
            mc "That... {i}bitch{/i}?"
            mc "Why would you say that? You love each other!"
            show gs 63
            d "That sl-slut only loves herself..."
            show gs 61
            d "But anyway... let's not talk 'bout that, eh??"
            d "Ya know... I was jus' checkin' pictures of our time in Kredon, and I r-r-remembered... you... and us..."
            d "Do you remember?"
            show gs 60
            mc "Of course I remember, but..."
            mc "Agh, I don't have time to lose now, I'm sorry. I've gotta get out of here."
            show gs 61
            d "I can help you with that."
            show gs 60
            mc "Huh?"
            mc "Can you really...?"
            d "Mm-hm."
            show gs 61
            d "Come wit' me 'round the corner and I'll tell you how."
            show gs 60
            mc "Do you know where we are, then? Do you know the exit?"
            show gs 61
            d "Ah, ah, ah."
            d "I won't tell you 'less you come with me."
            show gs 60
            mc "*Sighs* Okay... let's go."
            mc "But let's hurry up! I have no time to lose!"
            d "Mm-hm..."
            play sound6 stanleyvo32 volume 0.7
            scene gs 64 
            bla "{cps=17}Dalia turned around the corner barely able to walk straight...{cps=1.5} {cps=20}prompting our hero to follow her out of concern." with dis2
            stop sound6
            mct "Jesus, she's worse off than I thought..."
            scene gs 65 with dis15
            mc "*Turning around the corner* Okay, is here good enough?" with dis12
            mc "The office is completely empty anyway, so–"
            play sound chair1
            play sound2 clotheswhoosh
            play sound3 clothes2
            scene gs66
            d "*Pushes you* Mm-hm..." with vpunchslow
            mc "W-What are you doing now?!"
            play sound4 clothesfull volume 0.8
            scene gs 67
            d "Mmmmmh..." with dis15
            mc "H-Holy shit."
            play sound5 chair2
            scene gs 68
            d "*Straddling you* I want you to f-fuck me, [mc]..." with dis14
            mc "W-What?!"
            if daliapath:
                d "Remember when we were foolin' around in Kredon...?"
                d "We never got to... go all the way..."
                d "I never got to know how your... h-huge an' veiny cock would have... *hic* felt... w-within me..."
            else:
                d "I never shaid this before, but even if somethin' never happened between us, I... I tottaly had a crush on you..."
            d "*Giggles* Hihi."
            mc "Dalia, y-you're so drunk."
            d "All these years... wonderin' how you'd make me moan..."
            mc "U-Uh..."
            d "I never stopped hittin' the gym, ya know...?"
            mc "Y-Yeah, I can see that. Still in great shape."
            d "An' Jerry can't give me what I need..."
            mc "Wait, so you did marry Jerry?!"
            d "Fuck me, [mc]..."
            d "I want ya to spank me and pull my hair..."
            d "Make me yours..."
            menu:
                with dis12
                "Have sex with Dalia":
                    $ daliaofficesex = True
                    mc "Ohh fuck, Dalia..."with dis08
                    mc "I..."
                    mc "Well... I guess we have nothing to lose..."
                "Refuse":
                    mc "I-I appreciate the offer, I really do, but..."with dis08
                    mc "I don't think it's the right moment or place. Or that you're in your best condition."
                    mc "I mean, you're not even the real Dalia, so..."
                    mc "If you could move aside, please..."
            play sound6 stanleyvo33 volume 0.7
            bla "{cps=17}Our hero was unable to resist the sight of his old friend's ample bosom and alluring figure.{cps=0.6} {cps=16}Overwhelmed by desire, he accepted her offer and surrendered himself to her embrace."
            stop sound6
            if not daliaofficesex:
                mc "Wait, what?! That's not what I said!"
            else:
                mc "I'm only human after all..."
            scene black with dis27
            pause
            scene gs 69 with dis27
            mc "*Opening your eyes* Mmmmh..."with dis15
            if officeluna:
                mc "W-What just..."
                mc "Oh man, not this again!"
            else:
                mc "W-What just happened...? Where's Dalia?"
                mc "Why don't I remember anything...?"
            play sound6 stanleyvo34 volume 0.7
            bla "{cps=15}Exactly 3 minutes and 50 seconds later,{cps=1.5} {cps=16}he snapped back to reality after yet another session of...{cps=2} {cps=15}unsatisfying sex."
            stop sound6
            mc "W-What?!"
            play sound6 stanleyvo35 volume 0.7
            bla "{cps=18}Observing how Dalia had already left in haste and feeling frustrated by yet another failed attempt to satisfy a woman,{cps=1.5} {cps=18}he decided to follow suit and leave the office for the day."
            stop sound6
            if officeluna:
                mc "You're a fucking cheater! I didn't even do anything!"
            else:
                mc "I didn't even do anything!"
            play sound6 stanleyvo36 volume 0.7
            bla "{cps=17}He decided to follow suit and leave the office for the day."
            stop sound6
            if officeluna:
                mc "Are you really gonna do this again?"
            else:
                mc "But–"
            play sound6 stanleyvo25 volume 0.7
            bla "{cps=19}He left{cps=1.5} {cps=19}the office{cps=1.3} {cps=19}for the day."
            stop sound6
            mc "You son of a bitch..."
            if officeluna:
                mct "Fuck... it's like he can control all of my movements."
                mc "*Sighs* (But I guess I have no other choice.)"
            else:
                mc "*Sighs* (I guess I have no other choice.)"
                mct "Perhaps I can find the way out of this nightmare outside."
            mct "Let's get the fuck out of here..."
        "Leave the office":
            mc "You don't get to tell me what to do." with dissolve
            mc "Fuck you. I'm out of here."
            mc "I'll find my way out, and you won't be able to stop me!"
    $ escapesta = False
    jump officeleave
label officeleave:
    if escapesta:
        play sound6 stanleyvo37 volume 0.7
        bla "{cps=17}It had been an exhausting week, and our hero had finally reached his limit.{cps=1} {cps=18}He decided not to overwork himself any further, and...{cps=21} left the office.{cps=0.7} {cps=18}Bringing another day...{cps=1.5} {cps=15}another cycle in this routine we call life...{cps=1.6} {cps=19}to a close."with dis
        stop sound6
    else:
        play sound6 stanleyvo38 volume 0.7
        scene gs 12b
        bla "{cps=15}And with that, our hero left the office...{cps=1} {cps=17}bringing another day...{cps=1} {cps=17}another cycle in this routine we call life...{cps=1} {cps=18}to a close." with dis22
        stop sound6
    play sound6 stanleyvo39 volume 0.7
    show outoffice
    bla "{cps=18.4}Deep within his mind, he harbored a hope for a different outcome in the days to come...{cps=0.9} {cps=15}yet... he knew all too well...{cps=1.1} {cps=17}that the future awaiting him was nothing but a repeat...{cps=1} {cps=11}of his past mistakes...{nw}" with Dissolve(2.4)
    play sound ding
    stop sound6 
    stop music
    scene black
    if starep:
        $ starep2 = True
    $ starep = True
    $ sta1 = True
    $ sta2 = True
    $ sta3 = True
    pause
    play soundloop2 officesound fadein 4
    jump office1
label annieofficeleave:
    play sound whoosh6
    play sound2 debris3
    stop music
    play soundloop vent
    play sound4 panting volume 0.75
    play sound3 musicstop
    show gs91
    bla "You start running and climb the stairs as fast as your legs will carry you, heading straight to the 7th floor." with hpunch
    mc "*Panting* F-Fuck you!"
    mc "*Panting* You can't tell me what to do!"
    mc "*Panting* . . ."
    mct "Alright..."
    mct "I'm here."
    mct "Now what?"
    a "You made it!"
    play music2 stanley2 fadein 5 
    stop soundloop fadeout 20
    scene gs 93
    mc "*Turning around* What...?" with dis12
    mc "Oh no... not another odd version of people I know..."
    show gs 92
    a "Not this time!"
    a "I'm here to help you escape!"
    show gs 93
    mc "Eh...?"
    mc "Wait... are you serious? Are you the real Annie?!"
    show gs 92
    a "YES!"
    show gs 97
    a "Well... not exactly. We're actually in your mind."with dis
    a "I'm just the version of Annie that lives in your subconscious."
    show gs 98
    mc "Uh... okay..."
    mc "So... you're not real."
    show gs 97
    a "You're trapped within your own psyche."
    a "None of what you've seen here is true."
    show gs 98
    mc "So... Dalia didn't marry Jerry."
    show gs 94
    a "Obviously not."with dis
    show gs 95
    mc "Luna is not an addict."
    show gs 94
    a "She's the healthiest girl I know."
    show gs 95
    mc "Alex isn't really married. And Penelope is not dating that movie star."
    show gs 94
    a "Nope. None of that ever happened."
    show gs 95
    mc "Oh, thank fucking god."
    show gs 97
    a "You're just trapped in a mental prison, replaying your worst fears on a loop, faced with fake choices you can't actually make."with dis
    show gs 98
    mc "So... you're not real either."
    show gs 94
    a "I'm the image you have of Annie in your own mind, I told you!"with dis
    a "Come on, [mc], I need you to catch on quickly! We're running out of time."
    show gs 95
    mc "O-Okay, okay, I think I understand."
    mc "Sort of."
    show gs 97
    a "*Sighs* Okay, let's go over it one more time." with dis
    a "I'm simply your subconscious trying to help you, acting, speaking, and thinking just like you imagine Annie would in real life."
    show gs 96
    a "Although, I've gotta admit... oh my god, this top is SO cute!"with dis
    a "Thank you for making me look so adorable!"
    show gs 93
    mc "I agree! You do look really cute!"
    show gs 94
    a "Who are you complimenting now, yourself?"with dis
    a "Remember, I'm just your own image of Annie inside your own head!"
    a "I need you to focus!"
    show gs 95
    mc "O-Okay, I definitely get it now, sorry."
    show gs 97
    a "Every second you spend here, the narrator's influence on you grows stronger!"with dis
    a "He can't hear us here, but that won't last!"
    a "You need to take the reins back!"
    show gs 98
    mc "Alright! I'm with you!"
    mc "What do we need to do?"
    show gs 97
    a "The narrator weaves a scripted and twisted version of your life using your fears and memories, where he can control every single step you take."
    a "We need to break free from that cycle."
    a "End the story in a way he can't predict."
    show gs 98
    mc "Gotcha!"
    mc "And how do we do that?"
    show gs 97
    a "Simple."
    play sound whoosh3b
    play sound2 holster2
    show gs 99
    a "With THIS!" with Dissolve(.1)  
    mc "Whoa."
    play sound5 holster
    show gs 100
    a "Come on, take it before it's too late!"with dis
    play sound3 holster
    play sound4 grab
    scene gs 101
    mc "*Taking the gun* Alright..."with dis
    mc "I think I get it."
    mc "We're gonna take the people in the office as hostages to negotiate with the narrator. We'll force him to give us an exit."
    show gs 102
    a "Exactly!"
    show gs 103
    a "Well... not exactly, exactly."with dis12
    a "You have to kill yourself."
    show gs 104
    mc "WHAT?!"with hpunch
    show gs 94
    a "There's no time to hesitate, [mc]!"with dis
    a "The narrator will be here soon!"
    show gs 95
    mc "B-But..."
    show gs 94
    a "This isn't real!"
    a "Do you honestly think Dalia, Penny, Alex, Luna, or Chang would behave like they did in this fever dream?"
    show gs 95
    mc "Well..."
    mc "I guess not. You make a good point."
    show gs 94
    a "You have to end this nightmare in a way the narrator can't foresee and shoot yourself! That's the only way!"
    a "And you need to do it before the narrator erases me from his story!"
    a "Either you pull the trigger or I will!"
    show gs 95
    menu:
        with dis
        "Shoot yourself":
            mc "Alright."with dis08
        "Ask Annie to shoot you":
            mc "*Offering her the gun* Okay, you do it."with dis08
            show gs 105
            a "Oh my g-goodness, are you kidding me?!"with dis 
            a "I was bluffing! Just the recoil of this thing would knock me into a wall!"
            a "A-And I could never bring myself to shoot you, it has to be you!"
            show gs 106
            mc "Then why did you even say anything?!" 
            show gs 105
            a "I-I don't know, I just thought it'd sound cool!"
            show gs 106
            mc "*Sighs* Alright..."
    play sound holster2
    mc "*Pointing the gun to your head* I'm doing it." with hpunch
    show gs 92
    a "That's right!" with dis
    a "We've got shit to do! We can't afford to be stuck in a vegetative state forever."
    show gs 93
    mc "I suppose not..."
    mc "But... I'm not sure if I should trust you."
    show gs 92
    a "I look and act like Annie for a reason, [mc]."
    a "Do you trust yourself?"
    show gs 93
    mc "I do."
    show gs 92
    a "Do you trust your gut? Your instinct?"
    show gs 93
    mc "...I do."
    show gs 92
    a "Then I'll see you on the other side."
    if anniepath:
        a "And take me on a date to a nice restaurant!"
        a "You know nothing would make me happier!"
    play sound7 swallow
    show gs 93
    mc "*Gulps* . . ."
    mct "No hesitation, [mc]."
    mct "Trust yourself."
    play sound risingshortbb
    stop music2 fadeout 1
    mc "*Taking a deep breath* . . ." with dis 
    stop music2
    play sound gunshot
    play soundloop jungle fadein 7
    scene black with flashfastest
    pause 
    play sound5 seagull
    play sound6 debris3
    scene gt 1 
    mc "*Opening your eyes* . . ."
    mc ". . ."
    mct "Holy fuck."
    play sound2 debris
    play sound3 debris3
    scene gt 2
    mc "*Sitting up* (I...)" with dis12
    mct "I did it!"
    mct "I'm back on the New World server! I escaped the nightmare!"
    scene gt 3
    no "*Groaning* Mmmmmmhh..." with dis
    show gt 4
    no "*Mumbling* [mc]... w-what do you mean you don't need me anymore...?"
    no "*Mumbling* Penny isn't answering my calls..."
    no "*Mumbling* I-I thought I was her best friend..."
    show gt 5
    mct "Fuck, looks like she's having the same kind of dream I had."
    show gt 6
    gn "Hehehe..." with dis
    play soundloop2 powder fadein 2
    show gt 7
    bla "You spot a strange creature sprinkling some kind of powder all over Nancy." with dis14
    n "*Mumbling* Y-You can't come to the Christmas dinner this year either...?"
    n "*Mumbling* But why...?"
    gn "Dream, dream, sweet princess..."
    n "*Mumbling* Wait... w-why is there a picture of [mc] kissing Gertrude on the bedside table...?"
    n "*Mumbling* Eh...? What...? I'm not coping..."
    gn "Hehehe..."
    play sound footsteps3
    stop soundloop2 fadeout 2
    scene gt 8 with dis2
    pause
    play sound7 rubbody
    scene gt 9
    gn "Huh?" with dis
    play sound7 leather2
    play soundloop scaryaura
    play soundloop2 horrorsound
    scene gt10
    pause 3.6
    stop soundloop
    stop soundloop2
    play sound2 beating
    scene black
    pause 3.2
    play sound3 ding
    play sound4 whoosh3b
    play soundloop jungle
    play music2 pirate4 fadein 5
    scene gt 11 with pr
    pause
    no "You got what you deserve, you... ugly... thing!" with dis
    scene gt 20
    no "You made me think everyone was..."
    no "Y-You made me believe ten years had gone by!"
    no "That everyone had moved on without me! I had even lost my left eye!"
    show gt 11
    mc "You were the narrator we all kept hearing earlier...?"
    show gt 12
    gn "Well, not quite me. Not... exactly, at least. You all created that narrator inside your own minds."
    gn "I just... made it possible."
    gn "We Paradox Gnomes have spent generations perfecting this mindfuck powder."
    show gt 22
    n "So you're one of those “gnomes” Ed and Morty warned us about...?"
    n "I mean... no offense, but you look more like a goblin than a gnome."
    show gt 13
    gn "You have no idea of how racist that is, miss."
    gn "I look nothing like those dirty, stinky goblins."
    show gt 22
    n "What's the difference?"
    show gt 13
    gn "The difference?!"
    gn "Just the fact that you're even asking that is {i}outrageously{/i} offensive."
    gn "I won't even bother to answer that. Fascist."
    show gt 22
    n "Uh... well okay, if you say so..."
    show gt 11
    mc "So, what was your plan? Knock us out, give us nightmares of twisted futures, and then what?"
    show gt 19
    no "Ugh, is this some kind of... sexual thing?"
    show gt 12
    gn "Of course not. The plan was to keep you here until the nightmare took complete hold of your mind."
    gn "Then I would have taken your ship and anything valuable on it."
    show gt 14
    gn "You'd have only been asleep for... maybe a couple of days at most."with dis08
    show gt 19
    no "TWO DAYS?!"
    show gt 20
    no "We oughta just shoot you right here and now!"with dis08
    no "Give us a single reason not to!"
    show gt 12
    gn "Do what you want."
    gn "Better than starving to death here like you."
    show gt 11
    mc "Huh? What do you mean by that?"
    show gt 15
    gn "Hehehe... you're in Paradox Canyons now, you poor bastards." with dis08
    play sound2 wind4
    show gt 16
    gn "This place is a death sentence for any living creature." with dis14
    gn "Not many pirates make it this far, but those who get lost in the Paradox jungle never get to see the ocean again."
    gn "The jungle will always drag you back in an endless cycle."
    show gt 21
    no "We're stuck here?"with dis12
    no "What do you mean, an endless cycle?"
    show gt 15
    gn "I mean that no matter if you try scaling the rock walls, digging a hole, or walking straight... the island will always lead you back to where you started."
    gn "*Laughs* That's Paradox Archipelago for you!"
    show gt 22
    n "You said... any {i}living{/i} creature?"
    n "Does that mean the magic of this place doesn't affect the dead?"
    show gt 14
    gn "Yeah, that's why Davy Jones' skeletons can hang around here."
    gn "They don't sleep either, so they're also immune to our powder."
    gn "So annoying..."
    show gt 13
    gn "But luckily for you, us gnomes know a way to escape the infinite jungle of Paradox, so I can get you out of here." with dis08
    show gt 22
    n "Really? Would you help us get back to the shore?"
    show gt 12
    gn "Yeah, I'm quite impressed by the kid's mental strength to escape our mind trap, so I'll selflessly guide you back."
    show gt 11
    mc "Wow, that's a nice ges–"
    play sound2 pop
    show gt 17
    gn "OR... that's what I would say if I wasn't just biding my time for my triumphant escape!" 
    mc "W-Wait, what?"
    gn "And I finally got it ready!"
    gn "Get rekt, losers!"
    play sound smokebomb
    show gt18 with hpunch
    pause .2
    no "WHAT?!" with dis12
    mc "Son of a bitch!"
    no "He's gone!"
    no "W-What are we supposed to do now?"
    no "FUCK, are we trapped here forever?!"
    mc "Uh... shit, I d-don't know."
    no "ARE WE GONNA DIE HERE?!" with hpunch
    mc "I DON'T KNOW!" with hpunch
    n "Hmmm..."
    scene gt 22
    n "First of all, let's try not to panic. That won't get us anywhere." with dis12
    n "We need to come up with a plan..."
    mc "Yeah... yeah, you're right."
    mct "I've got to say, I'm so glad Nancy can keep her composure even in the most stressful situations. It really helps keep everyone calm."
    n "A plan..."
    n "A plan!"
    play sound whoosh6
    play sound2 leaves
    scene gt 24
    n "Alright guys, operation Escape from Paradox has just begun!" with pr
    mc "YES!"
    n "First, Nova, I need you to turn Dione into a flare gun and fire a shot into the air. Keep doing it every 5 minutes until Ed and Morty find us!"
    show gt 23
    no "Do you think they'll come for us?"
    show gt 24
    n "Pirates are bound by a camaraderie oath to keep their promises. We have to trust them!"
    n "Besides, I doubt they'd miss the chance to snatch the treasure for themselves and get their own ship..."
    n "But in any case, we can't sit idly by here. We'll head in that direction! Based on the sun's position, the coast should be that way."
    show gt 23
    no "Got it!"
    play sound3 holster
    scene gt 25
    bla "Nova transforms Dione into a flare gun at Nancy's command and fires a flare into the air." with dis15
    play soundlow steam2
    play sound flaregun
    show gt 26 with dis03
    pause .1
    show gt 27 with dis2
    pause
    show gt 29
    if nancypath:
        n "And finally, we just need a strong, athletic young man who can climb those massive walls and let us know if he spots the ocean in any direction."with dis12
    else:
        n "And finally, we just need a valiant soldier of the WRE who can climb those massive walls and let us know if he spots the ocean in any direction."with dis12
    show gt 28
    mc "*Chuckles* Ah, you're certainly in luck, you’ve got just the one right here."
    mc "I'll get you two out of here, my Empress!"
    show gt 29
    n "I expected no less..."
    show gt 28
    mc "We won't let the Heart of the Abyss slip away after all we've invested."
    mc "Let's do this!"
    stop soundloop fadeout 8
    stop music2 fadeout 7
    scene black with dis27
    show screen sometimelater with dis17
    pause 
    play sound4 wind4
    play sound3 footsteps3 fadein 3
    scene gt 30 
    hide screen sometimelater
    with dis3
    play soundloop2 jungle fadein 7  
    bla "You spend several minutes trying to navigate the intricate labyrinth of cliffs and canyons, but just as the gnome said, you always end up finding yourself back at the starting point."with dis17
    n "Mmmmh... the sun hasn't moved since we started walking."
    mc "I guess the Paradox Archipelago really lives up to its name, huh?"
    n "Yeah... it makes me wonder how long we've really been asleep."
    n "Maybe we've been here longer than we thought."
    if not nancypath or not novapath:
        mc "*Looking around* And... I hate to be the bringer of bad news, but I swear we just passed this same spot like twenty minutes ago."
    else:
        play music2 pirate4 fadein 6 volume 0.5
    play sound fallfull volume 0.4
    play sound2 debris
    scene gt 31
    no "*Collapsing to the ground* AAAAAaaghhhhh... we're gonna die here!" with dis12
    no "WE'RE DOOMED!"with hpunch
    play sound6 stomach
    no "{bt=3}And I'm hungry...{/bt}"
    play sound7 debris
    if not nancypath or not novapath:
        play sound fall2
        show gt 116
        mc "*Lying down on a nearby rock* Hmmm... I guess we can take a short break to regain our strength."with dis12
        jump piratefail
    else:
        jump piratesuccess
label piratefail:
    $ threesomenancynovafail = True
    mc "And maybe we should fire another flare into the air."
    n "Does Dione ever run out of ammo?"
    no "Depends on what I turn it into, some forms only get a single shot."
    no "Although for something like a flare gun... it should be pretty much infinite."
    mc "Tsk, this cursed place..."
    mc "It's making us lose our minds."
    mo "Mr. [nickname]!"
    mc "I'm even hearing voices now."
    mc "*Sighs* There has to be a way to break this curse that traps us here."
    no "No, wait! I also heard that!"
    mc "Huh?"
    mc "*Shouting* HELLO...?!"
    play music2 ["<silence 2>"]
    queue music2 piratewellermanfast fadein 4 
    stop soundloop2 fadeout 20
    stop soundloop fadeout 20
    play sound debris
    show gt 117 with dis
    pause .2
    mo "Oh, there he is!" with dis14
    ed "About time!"
    play sound debris3
    mc "*Standing up* OH MY GOD!" 
    no "ED!"
    n "MORTY!"
    mc "Oh my god, I've never been happier to see dead people!"
    mc "How did you find us?!"
    ed "My brother saw one of those stinky gnomes trying to swim to your boat when a Paradox White Shark devoured him."
    no "HAH! Serves him right!"
    ed "Then we spotted the flares coming from the jungle cliffs, and..."
    ed "Well, you don't need a brain to put two and two together."
    mc "YES! I LOVE YOU!" with hpunch 
    ed "We've only got 2 hours before the Island of the Lost Souls sinks into the ocean, you know?"
    n "Oh no, we've been here longer than we realized."
    mc "Do you think we can still make it?"
    ed "Well... if you can all climb a rope and run fast... maybe."
    mc "Ah, I like the sound of that “maybe”! I've worked with worse odds!"
    mc "Can everyone here climb a rope?"
    no "Yes, sir!"
    n "It was my best exercise in school!"
    ed "Alright, then let's wrap this up!"
    mc "Start the boat's engine! We're leaving this place!"
    mc "LET'S GET THAT TREASURE!" with hpunch 
    jump pirateending
label piratesuccess:
    scene gt 32
    no "Can we just sit here for a few minutes, please?"with dis
    no "Or... you guys go on without me and try to find an exit. Just take Dione so it doesn't get lost here with my bones for all eternity."
    play sound debris3
    show gt 33
    mc "*Sitting down* We're not leaving anyone behind, and we're not dying in this godforsaken place, Nova. I promise." with dis
    play sound debris
    play sound7 fall2
    scene gt 34
    n "Let's sit here for a while – I could use some rest too, not gonna lie."with dis 
    show gt 33
    mc "Maybe we should change direction? Try heading back to where the gnome disappeared?"
    show gt 34b
    n "I'd try staying here for a bit while continuing to shoot flares."
    n "If Ed and Morty don't find us, maybe another creature from Paradox will. Perhaps another gnome we can negotiate with."
    n "A flare can be seen from up to 15 miles away on a clear day, so..."
    show gt 32
    no "*Sighs* I wish I had just a fraction of your positivity, Nancy."
    show gt 33
    mc "Yeah, you're even more optimistic than me, and that's saying something."
    show gt 34
    n "Don't sweat it, guys. My gut says we'll find a way out soon."
    n "Now it's all about playing the waiting game." 
    n "And hey! Turns out I've got just the thing to make time pass faster..."
    mc "Huh?"
    play sound2 bottle
    play sound3 whoosh6
    show gt 35
    n "*Pulling a bottle from her back* Rum!" with pr 
    show gt 35b
    no "Huuuuhhh... pirate rum! Where did you get that from?"
    show gt 36
    n "From the remains of that dead corsair we found earlier. Should still be fine since it's sealed, booze keeps forever."
    show gt 35
    n "It might not be food, but it'll settle the stomach."
    show gt 36
    n "Plus, in Eternum we literally can't get a hangover tomorrow, so..."
    show gt 35b
    no "Uuuh..."
    no "I'm sold!"
    show gt 37
    mc "You're such a bad influence, Nancy."
    show gt 36
    n "I see three adults here over 18 years old... everyone's mature enough to make their own decisions."
    n "No one is forcing you to drink anything."
    show gt 37
    mc "Alright, alright, pour me a glass."
    show gt 35
    n "Attaboy..."
    show gt 38 with dis25
    pause
    play sound7 sip
    n "*Taking a sip* Alright... it's Nova's turn now." with dis
    n "Question!"
    show gt 41
    no "Oh, already?"with dis
    show gt 42
    no "Hmmm..."
    show gt 43
    no "Okay, I've got one!"
    show gt 41
    no "I mean, this might sound a bit like the classic “what would you bring to a deserted island” question, but..."
    no "If you were stuck alone in a medieval server for a month, with no way to contact the outside world, what would you want to have with you?"
    no "Like, for entertainment. Assume all basic needs are taken care of."
    scene gt 40
    n "Mmmmh..."
    show gt 39
    n "Probably a canvas and some brushes? I could easily spend hundreds of hours painting."
    n "Assuming there are no electronic devices, of course."
    show gt 43
    no "Ohhh, that's pretty cool!"
    no "I could settle for some papers and pencils too! I'd draw a whole manga!"
    show gt 41
    no "That is... if my technology addiction doesn't kill me before the month's over. I need the internet to survive."
    show gt 44
    mc "Yeah, I'd honestly struggle without internet too."
    mc "But if I had to choose something..."
    show gt 45
    mc "Hmmm..."
    menu:
        with dis
        "A dog [nova_pts]":
            show gt 44
            mc "Maybe... a dog?" with dis08
            mc "I mean, the rules said no technology, so... would that be allowed?"
            mc "I bet a doggo would keep me more entertained than anything else."
            $ nova_points += 1
            play sound beat
            show screen heartbeat
            show gt 43
            no "Ohhhh, a puppy! That's a super cute answer!" with dis08
            no "Can I bring a dog too? I'd teach him to play dead!"
            show gt 39
            n "*Chuckles* Yeah, if all basic needs are really taken care of, that sounds like a great answer."
            n "I can't think of better non-human company."
            show gt 43
            no "Alright, it's your turn again, [mc]! Ask a question!"
        "Books [nancy_pts]":
            show gt 44
            mc "Probably some books?" with dis08
            mc "If I could even choose the type of books, I could go for different kinds: novels, survival guides, maybe even... I don't know, some kind of language learning materials."
            mc "It'd be pretty cool to come back from that month knowing how to read Japanese or something."
            $ nancy_points += 1
            play sound beat
            show screen heartbeat
            show gt 46
            n "Ah, a very smart choice, [mc]... always making the most of every situation. I expected no less!" with dis08
            n "Intelligence is a very attractive trait in a man."
            show gt 43
            no "Yeah, I'll admit learning Japanese would be pretty awesome."
            no "I could watch anime without subtitles!"
            no "Cool..."
            show gt 46
            n "Alright, your turn, [mc]! Ask a question."
        "Porn magazines":
            show gt 44
            mc "Maybe... porn magazines?" with dis08
            mc "Or... some adult comics."
            mc "I mean, if I really have to stay there for a month doing nothing, at least I could... you know."
            show gt 43b
            no "Ugh, seriously?"
            no "You're such a perv!"
            show gt 46
            n "Yeah, [mc] is way too horny for his own good."
            show gt 43b
            no "Definitely."
            no "But anyway... ask the next question, Mr. Perv."
    show gt 45
    mc "Hmmm..."    
    menu:
        with dis
        "What would you buy with 1M dollars?":
            show gt 44
            mc "Alright, imagine you suddenly win a million dollars overnight. No taxes. What are you buying?" with dis08
            show gt 41
            no "Oh, good question..."
            show gt 42
            no "Hmmm..."
            show gt 41
            no "Okay, I'd buy..."
            no "Tickets to Japan. Tons of clothes and hairstyles for Eternum. And a super high-end PC with top-of-the-line specs!"
            no "Oh, and some life-size figures for my room."
            show gt 43
            no "Oh, oh! And I want to create my own indie video game based on my ideas!"
            no "I've got a TON!"
            show gt 40
            n "Hmmmm..."
            show gt 39
            n "Well, I'd probably pay for Penelope and Dalia's college tuition."
            n "Then I'd buy a better car, and... I'd invest the rest."
            n "Probably index funds or real estate."
            show gt 41
            no "Ohhh..."
            show gt 43b
            no "Dammit, now my answer sounds so childish."
            show gt 43
            no "Can I change my answer? I also want to pay for my tuition and do some investments."
            show gt 44
            mc "Nope, too late, you already spent the money."
            show gt 43b
            no "Dammit. What the hell were you thinking, Nova? So stupid."
            show gt 51
            mc "But seriously, Nancy, you're really telling me you wouldn't treat yourself to anything?"
            show gt 46
            n "What can I say, I always think of others first. It's just who I am."
            show gt 47
            mc "*Chuckles* Cheeky liar..."
        "Have you ever been arrested?":
            show gt 44
            mc "I wonder... have you ever broken the law?" with dis08    
            mc "I mean, like actually getting arrested. Not like going 50 in a 35 zone."
            show gt 41
            no "Uh..."
            no "Well, with all the data breaches, DDoS attacks, and unauthorized access I could be charged with... yeah, I could probably face some serious jail time."
            show gt 43
            no "But I NEVER leave any trace! I'm as clean as a peeled peach!"
            show gt 41
            no "I mean... I almost got caught once when the police confiscated my laptop, the day I met Luna. But still."
            show gt 44
            mc "Oh yeah, I remember that. She helped you hide your flash drives, right?"
            show gt 43
            no "Yeah! And we didn't even know each other yet!"
            no "I might not be here today if it wasn't for her!"
            show gt 46
            n "I've never been arrested either."
            n "I've always been a good girl."
            show gt 47
            mc "Really...? Not even during your high school days?"
            play sound pop
            show gt40b
            mc "In that picture of yours from a pajama party we found the other day, you looked like quite the rebel."
            no "Ohhh, I wanna see that picture too!"
            mc "*Chuckles* I'll send it to you. Nancy's about 15 in it."
            mc "She looks just as good as she does today, just younger. Even Dalia said she was jealous of her abs back then!"
            scene gt 46
            n "*Giggles* I was 16, and while we might have thrown a bash or two, we never got as far as getting arrested!"with dis
            show gt 47
            mc "I'll pretend I believe it..."
    show gt 58
    n "*Chuckles* I'm telling the truth!"
    show gt 46
    n "But hey, now it's my turn to ask, let's see if you're as honest as I am."
    n "Tell me..."
    n "Would you rather... watch or be watched?"
    show gt 47
    mc "Ah, I see this is getting interesting..."
    show gt 48
    no "W-Watch? Watch what?"
    show gt 46
    n "I mean, would you rather watch a friend having sex, or have a friend watch you having sex?"
    show gt 48
    no "O-Oh... you mean {i}that{/i} kind of watch."
    show gt 49
    no "Uh... that's a tough question."with dis06
    no "I guess... I'd rather... um... be... watched?"
    no "I mean, I'd feel super awkward being the one watching."
    show gt 48
    no "At least if I'm the one being watched, I don't have to give any explanations later."with dissolve 
    no "Right?"
    show gt 49
    no "Does that make sense?"with dis06
    show gt 46
    n "Interesting..."
    n "[mc]?"
    show gt 44
    mc "Uh..."
    show gt 45
    menu:
        with dis
        "Watching":
            $ watchingnancynova = True
            show gt 44
            mc "Maybe... watching?"with dis08
            mc "Like... I wouldn't mind watching a video of a... {i}friend{/i} having fun with herself, for example."
        "Being watched":
            show gt 44
            mc "Probably... being watched?"with dis08
            mc "Like, I wouldn't mind if a... {i}friend{/i} watched me having fun with another... {i}friend{/i}."
    show gt 47
    mc "I wouldn't mind at all, actually."
    show gt 46
    n "Interesting."
    n "Very interesting..."        
    n "*Giggles* Oh my, this is getting spicy! Nova, it's your turn!"
    show gt 50
    no "Oh no no no, I'm super terrible at coming up with questions!"
    no "I prefer just answering them!"
    no "Please, skip me!"
    show gt 46
    n "Very well. [mc]?"
    show gt 45
    mc "Mmmmh..."
    menu:
        with dis
        "Have you ever caught a family member in the act?":
            show gt 47
            mc "Have you ever caught a family member in the act?" with dis08
            show gt 50
            no "Eh?? Caught?"
            no "L-Like... catching my parents?"
            mc "Doing it, yeah."
            no "Oh... oh god, no. Never."
            no "I would probably gouge my eyes out and implode if that ever happened."
            show gt 47
            mc "And have they ever caught you touching yourself? You know, in your room, or... in the shower...?"
            show gt 50
            no "Uh..."
            show gt 49
            no "Uh... no. I don't think so."with dis
            no "I mean... not that I'm aware of, at least."
            no "I've always tried to be... discreet."
            show gt 51
            mc "And how about you, Nancy? Have you ever caught Dalia or Penny... you know, giving in to their impulses?"
            show gt 46
            n "Even if I had, they'd kill me if they knew I told you."
            show gt 51
            mc "Please, just a yes or no! You don't even have to tell me who it was!"
            n "*Snorts* Hmm."
            show gt 46
            n "Well... I'll just say that... okay, yes, I once entered our bathroom without knocking – bad habit, I know – and found one of them... enjoying the shower a little bit too much."
            show gt 48
            no "Oh MY! Was it Dalia?! No... Penny... it had to be Penny. Was it Penny?!"
            show gt 46
            n "I won't say any more."
            show gt 47
            mc "Oh boy...."
            mc "And what happened after that? Did she notice you, or was she too focused?"
            show gt 46
            n "I've already said too much!"
            n "I'll leave the rest to your imagination."
            show gt 48
            mc "*Chuckles* Alright, fair enough."
            no ". . ."
            show gt 47
            mc "It's probably better to ask the next question, Nova's already lost in fantasies about Penny being caught by you."
            show gt 50
            no "N-NOT TRUE!"with hpunch
            no "I was... thinking about s-something else!"
            show gt 51
            mc "*Chuckles* Yeah? What was that something, then?"with dis
            no "J-Just... how strong this rum is!"
        "What's your favorite position?":
            $ favoriteposenova = True
            show gt 47
            mc "What's your favorite position?" with dis08
            show gt 50
            no "M-My favorite position??"
            show gt 46
            n "Oh my... going strong, huh?"
            show gt 47
            mc "No one is forced to answer, of course."
            show gt 46
            n "*Giggles* Well, I don't think I have a favorite position, but if you ask me right now I might say..."
            n "Maybe... spooning."
            n "It's like cuddling, but... you know. A bit more."
            show gt 58
            n "And... I'd be lying if I said I don't like being on top and in charge of the situation."
            n "So hard to choose. So many options..."
            show gt 47
            mc "I see..."
            mc "What about you, Nova?"
            show gt 50
            no "U-Uh..."
            no "I mean... I haven't..."
            no "Had much..."
            show gt 47
            mc "Even if you haven't tried it, just say something you saw online or heard about that made you feel like “whoa, I wanna try that so bad”."
            show gt 50
            no "Oh..."
            show gt 49
            no "Uhh..." with dis
            no "Maybe... me... on top too?"
            no "But like... without me being in control. Hanging on tight. And instead of facing each other, me with my back to y–"
            play soundlow whoosh3b volume 0.6
            show gt 50
            no "HIM." with hpunch 
            no "Him!"
            no "My back to him."
            show gt 51
            mc "*Chuckles* Were you gonna say “you”?"with dis
            no "Whaaaat? O-Of course not!"
            no "It's just... this rum is too strong! It's making me all tongue-tied!"
    mc "It's not that strong! You just get drunk super fast!"
    if novadildo:
        mc "Remember the Halloween party?"
    no "No, I don't! I drank more than you, that's all!"
    mc "*Chuckles* Oh my god, you're a compulsive liar!"
    mc "You're lucky you're this cute."
    no "*Giggles* Thank you."
    show gt 46
    n "Okay, it's my turn to ask!"
    play sound sip
    show gt 52
    n "I didn't want to pry, but you two are so adorable together and have so much chemistry that I can't help it." with dis12
    n "I've gotta ask!"
    n "How was your first time together...?"
    stop music2
    play sound2 spitwater
    scene gt53 with hpunchlong4
    pause 0.7
    play sound3 drips
    show gt 54
    no "W-W-W-Wh-whaa-wawa...?" with dis17
    no "What...?"
    no "W-What first time?"
    $ renpy.music.set_volume(0.65, channel='music3')
    play music3 piratelewd fadein 12
    stop soundloop2 fadeout 20
    show gt 46
    n "You know..."
    n "Your first time, going all the way. When we stopped to have dinner earlier."
    n "I bet it was something."
    show gt 54
    no "HAHA!"
    no "We didn't..."
    no "We didn't! Where did you get that idea?!"
    no "W-We just..."
    show gt 55
    no "[mc], tell her!"
    show gt 56
    mc "Uh..."
    show gt 55
    no "B-But don't hesitate or she'll know we..."with hpunch 
    show gt 54
    no "She'll THINK we did something that we didn't! HAHA!"
    no "We're just friends!"
    no "We..."
    play sound debris3
    play sound2 leaves2 volume 0.4
    scene gt 57
    no "*Standing up* Anyway, I think we should keep going through the jungle!" with dis12
    no "Maybe if we keep walking, we'll eventually find a way out!"
    show gt 58
    n "Come on, Nova, there's no need to get this nervous!"
    n "With how close you two are and how much time you spend together, it's the most natural and healthy thing you could do."
    n "There's literally nothing to be ashamed of."
    show gt 57
    no "*Wiping the rum off her chest* O-Oh damn, what a mess I made!"
    no "I need a good shower!"
    no "Go, go!"
    show gt 58
    n "There's nothing wrong with having sex, Nova. It's just a part of life."
    n "[mc] and I also had some fun together not too long ago."
    n "And honestly, I had some reservations at first, but now I don't regret it one bit."
    show gt 56
    mc "N-Nancy...?"
    show gt 46
    n "*Whispering* I'm just helping her loosen up. You'll thank me later."
    show gt 57
    no ". . ."
    show gt 59
    no "You two... what?"with dis14
    no "WHEN?"
    show gt 58
    n "A few weeks ago."
    show gt 59
    no ". . ."
    no "Whoa."
    no "Holy shit, I-I really didn't expect that."
    show gt 58
    n "*Giggles* Don't worry, I won't get in your way."
    show gt 62
    no "No... it's not that."with dis12
    no "I... I don't mind what happened."
    no "I just don't..."
    no "I mean, if the others find out about [mc] and I, I don't want to... be isolated from the group."
    no "I-I know others have feelings for him too. I don't wanna be selfish."
    no "I don't want them to..."
    no "Like..."
    play sound debris
    show gt 60
    n "*Standing up* You're afraid of what others might think?"with dis12
    show gt 61
    no "Hmph."
    show gt 62
    no "Yeah..."
    no "Kinda."
    show gt 60
    n "But... what is it that YOU really want?"
    n "Forget about what others might think for a moment."
    n "Allow yourself to be selfish just for a second!"
    show gt 61
    no ". . ."
    show gt 62
    no "I... I just want to be with [mc]."
    no "And... I want to stay together with all of you. I don't want you to exclude me."
    no "I don't want to be alone. I've been alone my whole life and it..."
    no "It doesn't feel good."
    show gt 60
    n "So you'd be okay sharing our love for [mc]...? Staying all together?"
    show gt 61
    no ". . ."
    show gt 62
    no "I mean... that's not even an option, is it?"
    no "Like..."
    no "That's not... normal."
    show gt 61
    n "Normal?"
    show gt 60
    n "Alright..."
    n "I have three questions for you, Nova. And I need you to answer them as sincerely as you possibly can."
    n "Okay?"
    show gt 61
    no "Mm-hm."
    n "Do you actually think our lives are... {i}normal{/i}?"
    n "Has anything that's happened to us in the last three months been even {i}remotely{/i} normal in any way?"
    no ". . ."
    show gt 62
    no "I... s-suppose not."
    no "Not... not in the slightest, in fact."
    play sound footsteps3
    show gt 63
    n "Second question... would you be hurting anyone by being in that completely abnormal, unconventional, and off-protocol situation?" with dis2
    show gt 64
    no "Uh..."
    no "W-Well, if everyone agreed to it..."
    no "No, I guess not."
    show gt 63
    n "Good girl."
    show gt 65
    n "And finally, the most important question of them all." with dis15
    n "Do you enjoy being with [mc]? Does he make you feel happier?"
    n "*Whispering* Did you savor every moment when you slept together...?"
    show gt 66
    no "*Whispering* Yes..."
    show gt 65
    n "Are you in love with [mc]?"
    show gt 66
    no "I..."
    no "I am."
    show gt 65
    n "Now tell him while looking into his eyes."
    show gt 67
    no ". . ." with dis
    show gt 68
    no "I love you."
    show gt 69
    n "Now tell us..."
    n "Do you love us, [mc]?"
    show gt 67
    menu:
        with dis
        "I do [gr][mt](Harem path){#0.8,harem}":
            $ harempath = True
            mc "With all my soul." with dis06
        "It's complicated":
            mc "I mean... I do like you." with dis06
            mc "But..."
            no ". . ."
            show gt 68
            no "But...?"
            play sound musicstop
            stop music3
            play soundloop jungle
            play sound2 whoosh6
            play sound3 debris3
            scene gt 200
            no "*Moving away from Nancy* BUT! E-Exactly! That's what I meant!"with pl
            no "It's just... weird!"
            no "It's not normal! What would my mom think!"
            no "We..."
            no "W-We should focus on getting out of this place, c'mon!"
            play sound4 footsteps3
            scene gt 201
            no "*Walking away* I-I'll go shoot the flare gun again! We might have someone nearby!" with dis15
            n ". . ."
            show gt 202
            n "Seriously...?"with dis12
            n "{i}“I do LIKE you, BUT”?"
            show gt 203
            mc "I-I don't mean I {i}don't{/i} love you all, it's just that–"
            show gt 202
            n "Please, don't make it even worse."
            n "We had the perfect mood and you ruined it."
            show gt 203
            mc "C-Can we start over?"
            show gt 202
            n "Look, [mc]... I was serious when I said our lives are anything but “normal”, but you still need to sort things out in your life."
            n "Seems like you don't even know what YOU want, and... that's when people can get hurt."
            n "You need to make up your mind. Soon."
            show gt 203
            mc "Yes... I know. I'm sorry."
            show gt 202
            n "And now I'm frustrated AND horny. You owe me one for this..."
            show gt 203
            mc "F-Fair enough."
            play sound footsteps3
            show gt 204
            n "*Walking away* Come on, let's keep moving."with dis15
            n "We need to get out of here!"
            mc "On my way!"
            mc "*Sighs* (She's right, I have to start making decisions soon.)"
            mct "I can't have it all."
            mct "Although... getting better at expressing myself in crucial moments wouldn't hurt either, not gonna lie."
            mct "What a mess..."
            stop soundloop fadeout 4
            scene black with dis27
            show screen afewminuteslater with dis15
            pause
            play sound7 wind4
            scene gt 116 
            hide screen afewminuteslater
            with dis25
            play soundloop jungle fadein 7
            play sound fall2
            play sound2 debris3
            mc "*Lying down on a nearby rock* Can we take a short break to regain our strength...?" with dis15
            mc "My feet are starting to hurt."
            jump piratefail
    show gt 69
    n "*Giggles* Now come over here and give this girl a kiss. She's craving it."
label ga_novanancy:
    if _in_replay:
        $ renpy.music.set_volume(0.65, channel='music3')
        play music3 piratelewd fadein 12
    play sound footsteps3
    show gt 70
    bla "Nova takes a step forward and you gently grasp her by the waist. In her eyes, you see reassurance and confidence, as if a great weight has been lifted from her spirit." with dis22
    $ nova_points += 1
    $ nancy_points += 1
    play sound2 beat
    show screen heartbeat
    play sound3 rubbody
    show gt 71
    bla "You two merge into a passionate kiss." with dis15
    no "Mmmmmm..."
    mct "Damn..."
    mct "Our kisses are getting even better each time."
    mct "Her tongue is so playful now... our lips move together in a perfect dance."
    show gt 72
    no "*Moaning* Mmmm..." with dis14
    play sound rubbody
    scene gt 73
    bla "Nova slowly moves her petite hand towards your crotch and starts groping you through the pants."with dis15
    no "*Giggles* Hihi..."
    no "*Whispering* You get ready so fast..."
    mc "Well, it was a good kiss..."
    show gt 76
    no "I think I should keep my distance from Nancy, [mc]." with dis14
    no "She’s far too good at getting me to see things her way."
    no "And her sultry voice doesn't make it any easier. It always turns me on way too fast..."
    mc "*Chuckles* I don't think she told you anything you didn't already know deep down, Nova."
    no "*Giggles* You think so?"
    no "Are we degenerates, [mc]...?"
    mc "I think we always have been."
    no "*Giggles* Maybe you're right."
    show gt 74
    no "In that case..."with dis08
    no "Could I ask you... a little favor, Nancy?"
    show gt 75
    n "Of course, sweetheart."
    show gt 74
    no "You seem like quite the expert, so..."
    no "Do you think you..."
    no "Could you teach me... how to give him..."
    no "Better pleasure...?"
    show gt 75
    n "I'm sure you're more than capable of giving him pleasure and more, Nova."
    n "Although... if [mc] wants me to... I could give you some help."
    show gt 76
    no "[mc]...?"
    no "Can Mistress Nancy give me... a few tips...?"
    mc "I don't see why not..."
    show gt 75
    n "Well, in that case..."
    n "You'll have to sit down, [mc]."
    n "Then kneel before him, and... follow my instructions."
    show gt 76
    no "You heard my mistress, [mc]."
    no "Sit down..."
    play sound fall2
    play sound2 debris3
    show gt 77
    bla "Nova releases her embrace and makes you settle onto a nearby rock." with dis15
    mc "Oh boy, I'm starting to wonder if this is all just a dream after those sirens took me to the bottom of the ocean."
    play sound4 debris
    show gt 78 with dis15
    n "*Kneeling down* I think sirens wouldn't have their bad reputation if all they did was give people dreams like this."with dis12
    mc "Heh, that's a good point..."
    n "*Giggles* Now, Nova... pull his pants down before they explode, would you?"
    play sound5 clothesfull
    scene gt 79 with dis17
    no "*Pulling your pants down* Whoa..." with dis14
    no "*Devious giggle* Hello again..." 
    n "*Giggles* I don't think I'll ever get used to your size, [mc]."
    n "Alright... grab it with both of your hands, Nova..."
    play sound6 rubbody
    show gt 80
    no "Like this...?" with dis15
    mc "O-Oh, fuck yes..."
    show gt 81
    no "Whoa, it's so hard..." with dis12
    show gt 82
    n "Isn't it great...?"
    n "Now... start stroking it suuuuper gently while looking into his eyes."
    n "Enjoy yourself, girl..."
    $ renpy.music.set_volume(1.0, channel='soundloop')
    play soundloop wetting6 fadein 3
    play soundloop2 wetting5 fadein 3
    $ renpy.music.set_volume(0.35, delay=8.0, channel='music3')
    scene nn1 with dis2
    bla "Nova obediently follows Nancy's instructions and begins to massage your cock with both of her hands." with dis12
    no "Something... like this...?"
    n "Just like that..."
    mc "Oh my g-god..."
    n "*Giggles* You seem excited."
    n "Have you ever given him a handjob, Nova?"
    no "I mean... n-not like this."
    no "I-It feels... so big in my hands."
    n "Tsk, tsk, tsk, [mc], skipping basic steps... so bad..."
    mc "S-Sometimes it's hard not to..."
    n "You need to appreciate the value of foreplay."
    n "It's all about enhancing the experience... about fostering an emotional connection between each other..."
    n "I know you want to be inside of her... but trust me, the build-up just makes it so much better."
    mc "I guess y-you're right..."
    mc "Oh yeahhh..."
    n "Can you feel how [mc]'s arousal keeps rising...?"
    no "Mm-hm..."
    n "His anticipation for what's to come..."
    n "The big, final prize he's yearning for..."
    n "Oh, but you can't give him that yet!"
    n "Ah, ah, ah... not yet, big boy..."
    mc "I-I can't deny you know what you're doing, Nancy..."
    n "And don't think you're the only one getting fired up, [mc]."
    n "I bet Nova right here is starting to drip like a broken faucet."
    n "You just have to look at her face..."
    no "*Giggles* It's... quite arousing..."
    pause
    stop soundloop fadeout 1
    stop soundloop2 fadeout 1
    play sound debris
    show gt 83
    n "*Moving away* Now, let's give [mc] a bit more of a... visual stimulation, shall we?" with dis14
    play sound2 clothes4
    play sound3 rubbody
    scene gt 84
    bla "Nancy sensually lowers the top of her bikini, revealing her ample breasts to both of you." with dis14
    play sound3 debris3
    show gt 84a
    no "Wow... your tits are as big as Penny's! I can see where she got them from."with dis
    no "And they look so... so perfect."
    show gt 84b
    mct "Nova has seen Penelope naked...? When...?"
    mct "Oh boy, I'll have to explore that path..."
    show gt 85
    n "Don't worry, sweetheart, I'm sure [mc] appreciates a petite, fit body just as much as a voluptuous one."
    n "Am I wrong... [mc]?"
    show gt 86
    mc "You've never been more right in your life."
    no ". . ."
    show gt 85
    n "Why don't you also take off that wet bikini, Nova?"
    n "We're all in a safe space here."
    show gt 86
    no "Hmph."
    show gt 87 
    no "Mmmh." with dis12
    play sound rubbody
    show gt 88 
    mc "Oh, fuck yes..." with dis14
    play sound2 debris
    play sound3 clothes4
    show gt 89
    n "*Gently pushing Nova's head* And now... come back here. Things are about to get a bit more intense." with dis15
    show gt 90
    n "Does that sound good, [mc]...?"
    mc "OH FUCK YES..."
    n "Just follow my lead..."
    n "*Whispering* And let yourself go..."
    $ renpy.music.set_volume(0.29, delay=7.0, channel='music3')
    play soundlow rubbody
    scene nn2 with dis2
    mc "OHHHH GOD... my girls..." with dis
    n "You lick it just like this..."
    n "You tease him..."
    n "And then..."
    mc "A-AAAa-aAaaahhhh..."
    mc "F-Fuck yeaaahh..."
    bla "Nancy and Nova start taking turns plunging your shaft deep into their mouths, pushing it as far down their throats as they can."
    n "*Moaning* Mmmhh..."
    n "Looks like Nova's a natural student. You're a lucky, lucky man, [mc]."
    mc "Y-Yeah, I can see that..."
    no "MmmmmmMmmmm..."
    no "*Giggles* This is turning me on so much..."
    mc "Good..."
    n "I'm amazed you managed to fit this huge cock in your tiny pussy, Nova."
    mc "I-I already told her she's capable of more than she realizes..."
    n "Mm-hmmm... naughty, naughty girl..."
    pause 
    bla "Both girls continue to coat your dick with their saliva, heightening the pleasure with each passing second."with dis
    mc "*Panting* Oh m-my god..."
    n "Good job, Nova..."
    n "You're doing great..."
    n "Mmmmmmhh..."
    mct "Oh god, I need to fuck them..."
    mct "I need to fuck them SO BAD..."
    n "*Giggles* See that face?"
    n "That's the face of a man on the edge..."
    n "Should we give him what he wants...?"
    mc "P-Please..."
    no "*Moaning* Hmmmm..."
    play sound rubbody
    scene gt 91b with dis14
    no "*Giggles* Mmmmmh... well..." with dis14
    no "Perhaps we should..."
    show gt 92
    n "Ahh... looks like she's ready for you, [mc]."
    n "Do you want Nova to finally surrender her body to you...?"
    mc "Fuck yes, I do..."
    n "*Giggles* Very well..."
    n "*Whispering* Then {i}take{/i} it..."
    play sound leaves2
    play sound2 fallfull
    play sound3 debris3
    scene gt93 
    bla "You effortlessly lift Nova as if she were a feather, placing her on top of you and sliding your erect member between her thighs."with hpunchslow
    mc "Come here, baby..."
    n "Spread your legs for him..."
    no "*Purring* Mmmmm..."
    play sound7 rubbody
    show gt 95 with dis15
    n "That's it..." with dis
    n "And now... the crowning moment."
    n "*Giggles* You know what to do, girl..."
    play sound5 penetration3
    play sound4 penetration2
    play sound6 clothes3
    show gt 96
    bla "Nova guides your dick towards her tight, recently deflowered pussy, inserting it and releasing a soft, sensual moan." with dis17
    no "A-A-A-AAAAaaaaaaahhh...."
    no "[mc][namelong]..."
    scene nn3 with dis2
    no "*Moaning* Aaaahhh... aAAaaAahhh... AAAAaaAAAAHHH..." with dis
    no "{bt=3}Oh my goddd....{/bt}"
    mc "O-Ohhhh... babe..."
    bla "You begin thrusting into Nova's insides, her body swiftly adjusting to your size and transforming any initial discomfort into pure, unadultered pleasure."
    no "*Moaning* AAAAaaaaaghhh..."
    mc "Good Lord, Nancy wasn't lying..."
    mc "Y-You're soaking..."
    no "Mmmm... mmMmmhh... mmMMMMHHH!"
    no "I c-can't help it..."
    no "*Moaning* Ohhhh J-Jesus..."
    play sound debris
    show gt 94b
    n "Oh my god, you're ravaging this poor little girl, [mc]..."with dis
    n "*Touching herself* Although... I won't lie, this is so fucking hot..."
    hide gt 94b
    no "*Moaning* AAAaaaaaahhh..."with dis 
    no "I c-can't believe we're doing this for the th-third time today..."
    bla "You gently massage Nova's clit with your fingers, while maintaining your rhythmic thrusts in and out, determined to make her orgasm in record time."
    no "AAaaaaaaaahhhh... h-holy f-f-fuck..."
    no "*Moaning* [mc]..."
    no "What are you doooinggg to meeee...?"
    mc "Do you like it, you dirty girl?"
    no "*Moaning* F-Fuck yes, I do..."
    no "Keep touching me there..."
    no "P-Please don't stop for even a second..."
    show gt 94b
    n "I'm shocked by how deep you can take him, Nova."with dis
    scene nn4 with dis 
    n "Not many girls of your size would be able to do that."with dis
    n "Especially not with so little experience..."
    no "*Moaning* AAAaaahhh.... AAAAaaAAAhHHH..."
    no "*Stuttered giggle* Th-Thank you..."
    n "You have no idea of how hot it is to see your petite, pale body on top of [mc]'s..."
    n "When we first met, I knew you were something special..."
    no "AAAaaahhaa..."
    no "*Giggles* Gaggaagh...."
    bla "The multiple compliments, the relentless slams against her G-spot, the stimulation from her clitoris – Nova's mind begins to slowly drift away, overwhelmed by the myriad sensations flooding her at once."
    no "{bt=3}*Moaning* AAAAAAAaaGGHHHhhHh...{/bt}"
    mc "Oh babe, it feels so good..."
    no "*Giggles* I'm g-gla... AAAGH!!!"
    no "*Panting* [mc], I th-think I'm gonna cum..."
    mc "Oh yes, you will..."
    play sound debris3
    play sound2 debris
    scene nn5 with dis2
    nosc "*Panting* AAAaaagghhhh... aaaahhh... aaaAaaaAAAhh..."with dis12
    no "{sc=2}*Panting* FFFFUUUUUUCCKKKK....{/sc}"with hpunch 
    mc "*Holding her tight* O-Oh, babe..."
    n "Oh my, you're something else, guys..."
    scene novanancyswitch1 
    show screen novanancyangle1
    with dis17
    pause
    mc "*Panting* Oh y-yes, so fucking good..."with dis12
    mc "*Holding her even tighter* Your body is mine now, Nova..."
    no "*Panting* AAAAHHH... AAAGHHH... AAGAGAHHHHHHHH..."
    n "*Touching herself* Aaaahhh yeah..."
    n "I do wonder if you're actually enjoying being watched as you said, Nova..."
    n "*Moans* Aaaaahhh..."
    n "*Giggles* I certainly am enjoying watching you guys..."
    if favoriteposenova:
        n "*Giggles* [mc] even made your dream position come true, you can't complain, girl..."
    no "{sc=2}*Panting* Oh Lord... AAAAaaaaaHHHHhhh...{/sc}"with hpunch 
    no "{sc=2}[mc] I'm gonna cum!{/sc}" with hpunch 
    mc "*Panting* G-Good..."
    no "Please keep that same pace..."
    no "PLEASE DON'T MOVE AN INCH..."
    no "{sc=2}AAAAaaaaaHHHHhhh...{/sc}"with hpunch 
    nosc "[mc!u] I'M CUMMING..." with hpunch 
    bla "As the slender ginger moans stridently, her cries only heighten your primal urge to keep hammering her body with yours until she orgasms."
    nosc "O-Oh god I'm there..."
    nosc "Aaaahhh..."
    nosc "AAAAAAaGhHH..."
    nosc "AAAAAAAAAARGHHH..."
    play sound fall3
    play sound2 debris3
    play sound3 squirt
    play sound7 cumall
    play soundlow slap1
    scene gt 97 
    hide screen novanancyangle1
    pause .01
    no "{sc=3}*Twisting her body* AAAAAAAAAARGHHHHHHHHH...{/sc}"with vpunchslow
    play sound4 cum4
    play sound7 squirt
    play sound5 debris
    no "{sc=2}Y-YEEEEAHHHH...{/sc}"with vpunchslow
    play sound4 cum4
    play sound7 squirt
    play sound5 debris
    bla "Without loosening your tight embrace on her, Nova orgasms intensely and contorts her body while you fight the urge to cum alongside her, determined to prolong the moment a little longer."with vpunchslow
    nobt "OOoooooooOOooOoooooohhh god...."
    play sound rubclotheslong
    play sound2 rubclotheslong 
    play sound3 debris 
    scene gt 98 with dis22
    no "*Crawling away* Aaaa-ha-hahaaaa..." with dis14
    no "H-Holy fuck..."
    no "O-Okay... t-this is it..."
    no "I c-can happily die in this jungle now..."
    no "*Giggles* Ahaha..."
    play sound4 debris3
    scene gt 99
    n "*Crawling towards you* Damn, guys... there's nothing else I can teach you, I'm afraid." with dis14
    n "Young generations sure come stomping."
    n "I almost came just watching you two... fucking like animals."
    show gt 98
    no "I d-did cum."
    no "Oh boy, I s-sure did..."
    show gt 99
    n "I'm terribly jealous..."
    mc "Perhaps I could help you finish, Nancy."
    n "Oh, would you look at that! What a gentleman..."
    show gt 100b
    n "Do you mind if I take my turn with [mc] just for a quick minute?"with dis
    n "Just, you know... before continuing our adventure..."
    show gt 100
    no "*Giggles* Go ahead..."
    no "I need... I-I could use a moment to catch my breath..."
    play sound leaves2
    play sound2 debris3
    scene gt 101
    mc "*Pulling Nancy towards you* Hmph..." with dis
    n "Thank you..."
    n "*Whispering* Well... I'm almost there, big boy..."
    if nancymommy:
        n "*Whispering* Mommy just needs one small final push..."
        play sound rubbody
        scene gt 102
        mc "I'll be happy to oblige..."with dis12
    else:
        n "*Whispering* The Empress just needs one small final push..."
        play sound rubbody
        scene gt 102
        mc "Glad to serve, my Queen..." with dis12
    play sound penetration3
    play sound2 penetration2
    show gt 103
    n "AAAAAAaaaaaGHH..." with dis12
    mc "Oh, Nancy..."
    scene nn7 with dis2
    n "*Moaning* Oh MY GOD...!!!"with dis12
    n "*Moaning* YESSSS......"
    n "Oh d-dear Lord, [mc], you have no idea of how much I've m-missed this..."
    nbt "MmmmmmMmMMMmmmmm..."
    mct "She wasn't lying... her pussy is insanely wet and swollen after she's been on the edge for so long while I fucked Nova."
    mct "God, I can feel her juices literally trickling down her thighs."
    if favoriteposenova:
        mc "S-So spooning, eh...?"
        mc "Looks like wishes come true in this place after all."
        n "*Giggles* Indeed... they do..."
    mc "Ohhh g-god, Nancy..."
    mc "It feels amazing..."
    mc "How are you still tight after giving birth to two children...?"
    n "*Giggles* Oh, well..."
    n "*Giggles* I simply s-sold my soul to the devil w-when I was young."
    mc "AAahh... well, that explains it all."
    mc "T-That might have been the smartest decision of your life."
    n "*Giggles* R-Right...?"
    n "AAAAaaaahhh..."
    n "F-Fuck, I'm almost there..."
    n "I can feel it..."
    n "*Moans* Give it all to me, my baby boy..."
    if nancymommy:
        nbt "FUCK YOUR MOMMY HARD..."
    else:
        nbt "FUCK ME HARD..."
    scene novanancyswitch2 with dis2
    show screen novanancyangle2
    bla "You adjust your position to be able to penetrate Nancy with every inch of your length, and proceed to pound her with all your might." with dis 
    nsc "AAAAAAaaaaarghh..." 
    n "{sc=3}*Moans* YEEESSSSS!!!{/sc}"
    n "{sc=3}*Moans* MmmmmMmmMmhh...{/sc}"
    show gt 104 
    hide screen novanancyangle2
    with dis12 
    n "*Moans* AAAAAaaaGghhHHH..." with dis
    mc "Oh Nancy, so good..."
    n "*Moans* AAAAhhh..."
    no ". . ."
    scene nn9 with dis 
    nsc "*Moaning* Aaaahh... aaaAAaaaahhh..." with dis 
    nsc "*Panting* R-Right there..."
    show gt 104
    no ". . ."with dis
    hide gt 104
    play sound woosh1
    show gt 49g
    no "I mean, I'd feel super awkward being the one watching." with flashfast
    play sound2 woosh1
    show gt 104
    no ". . ."with flashfast
    if maatsex:
        play sound woosh1
        if maatsexvariant:
            scene maat8:
                matrixcolor SaturationMatrix(0.0) 
            with flashfast
        else:
            scene maat10:
                matrixcolor SaturationMatrix(0.0) 
            with flashfast
        pause
        show bbb 107g with dis15
        pause
        play sound6 woosh1
        hide maat8
        hide maat10
        pause 0.01
        hide bbb 107g
        scene novanancyswitch2
        show gt 104 
        no ". . ." with flashfast
    play sound woosh1
    show gt 1g with flashfast
    pause .3
    play sound2 woosh1
    show gt 2g with flashfast
    pause .3
    play sound3 woosh1
    show gt 3g with flashfast
    pause .3
    play sound4 woosh1
    show gt 105 with flashfast
    pause
    $ nna2 = False
    show gt 105b
    no ". . ." with dis17
    hide gt 105b with dis2
    show screen novanancyangle2
    n "*Panting* AAAaahh.... aaaghghhh..." with dis 
    n "*Panting* [mc]..."
    n "*Panting* I-I'm at m-my limit..."
    n "*Panting* I'm g-gonna c-cum... so hard..."
    mc "Cum for me, Nancy..."
    pause 
    n "Y-Yesss, right t-there..."with dis 
    n "RIGHT THERE..."
    n "{sc=3}RIGHT THEREEEEEEEE....{/sc}"
    hide screen novanancyangle2
    play sound4 cum4
    play sound7 squirt
    play sound5 debris3
    scene gt 106
    pause 0.01
    n "{sc=2}*Orgasming* AAAAAAAAAAAAGHHHHH...{/sc}"with hpunchlong4
    play sound7 squirt
    n "{sc=2}*Orgasming* O-O-OoooOoohhh...{/sc}"with hpunchlong4
    play sound8 rubbody
    show gt 106b
    n "{bt=3}*Panting* Godddd....{/bt}" with dis17
    play sound footsteps3 fadein 1
    scene gt 108 with dis2
    play sound fallfull
    n "*Collapsing on a nearby rock* Jeeeeeesus C-Christ almighty..." with vpunchslow
    n "*Panting* H-How can you endure so well, Nova...? We went for like, seven minutes and I can barely walk..."
    n "*Panting* Is it the age?"
    show gt 107
    no "*Giggles* Maybe."with dis12 
    no "I do a lot of exercise too. I skate."
    n "*Panting* Perhaps it's time to swap yoga for skating..."
    no "*Giggles* Maybe."
    show gt 108 with dis15
    menu:
        with dis12
        "Finish with Nova [gr][mt](Nova Creampie)":
            $ novacreampie = True
            play sound debris 
            play sound2 rubbody
            scene gt 108b
            bla "You grab Nova by the legs and draw her closer." with dis14
            mc "I feel left out being the only one who hasn't cummed here yet, girls."
            mc "My balls are about to explode, but... I still think I'm gonna need the help of my personal fidget spinner."
            no "*Purring* Mm-hm..."
            mc "Come here..."
            play sound debris
            scene nn10 with dis2
            bla "You penetrate Nova once again, finally ready to release the immense load you've been holding back all this time. Simultaneously, Nancy leans in and begins kissing you passionately." with dis
            no "*Moaning* AAAaaahhh..."
            n "Mmmmmmmmhhh..."
        "Finish with Nancy [gr][mt](Nancy Creampie)":
            $ nancycreampie = True
            play sound debris 
            play sound2 rubbody
            scene gt 108a
            bla "You grab Nancy and turn her around, starting to caress both girls' legs with gentle, lingering strokes." with dis14
            mc "I feel left out being the only one who hasn't cummed here yet, girls."
            mc "My balls are about to explode, but... I still think we can give Nancy one last ride."
            mc "What do you think, Nova?"
            no "Mm-hm..."
            mc "Come here, Nan..."
            play sound debris
            scene nn11 with dis2
            bla "You penetrate Nancy once again, finally ready to release the immense load you've been holding back all this time. Simultaneously, you begin fingering Nova's pussy." with dis
            n "*Moaning* MMmmm-m-mmhhh..."
            n "D-Dear Lord..."
            n "Y-You're insatiable..."
            no "*Moans* Oh god... and I-I thought I was done for..."
    mct "Oh yeah..."
    mct "My girls..."
    if novacreampie:
        no "*Moaning* Oh [mc]..."
    else:
        n "*Moaning* Oh [mc]..."
    mct "This is completely surreal. I'm fucking two stunning red-haired goddesses at the same time."
    if novacreampie:
        no "*Moaning* AAAAaaahhh..."
    else:
        n "*Moaning* AAAAaaahhh..."
    mct "Although... no, it's not just about the sex."
    mct "We're all together now, in every sense of the word."
    mct "I love them, and they love me."
    mct "And as Nancy said herself... I don't give a fuck if that's not “normal”."
    mct "I don't give a bloody damn if the world doesn't understand it."
    mct "For the first time, everything is clear."
    mct "These women are mine... and I am theirs..."
    if novacreampie:
        no "*Moans* Aaaaahhh..."
    else:
        n "*Moans* Aaaaahhh..."
        no "AAAAAAaahhhHh..."
    mc "M-MmMmmm..."
    mct "Oh shit... I was w-way closer than I thought..."
    mct "Time for the grand finale..."
    if novacreampie:
        scene nn10b with dis15
        nosc "AAAh-AAAH...AAHH-A-A-AAAHHHHH..." with dis 
        bla "You finally shift into the final gear, smashing your hips fervently against Nova's slender figure, ready for your final release."
        mcsc "*Guttural grunt* Grrrg...grrrghHH...GGGRH!!!"
        nbt "Mmmm.... MMMMMHHH!"
        mc "AAaa-Aaahh... oh god, I'm cumming..."with hpunch
        nosc "M-m-m-mMMmmhh..."
        mc "O-Oh babe..."
        mc "I want you to take all my jizz deep inside your tight pussy again..."
        nosc "*Giggles* Y-Yeeaaahhh-haa..."with hpunch
        nosc "F-Fill me up..."with hpunch
        mcsc "OH MY GOD...."with hpunch
        play sound debris
        play sound2 debris3
        play sound3 penetration3
        play sound8 clothes4
        scene gt 109 with dis08
        bla "You pull Nova's body towards you and abruptly spread her legs completely." with dis
        play sound4 cumall
        play sound5 slap1
        scene gt 110 
    else:
        scene nn11b with dis15
        nsc "AAAh-AAAH...AAHH-A-A-AAAHHHHH..." with dis 
        bla "You finally shift into the final gear, smashing your hips fervently against the buxom redhead's figure, ready for your final release."
        mcsc "*Guttural grunt* Grrrg...grrrghHH...GGGRH!!!"
        no "AAaaaahhh..."
        nbt "Mmmm....mmMmMM...MMMMMHHH!!!"
        nbt "T-That's it baby..."
        if nancymommy:
            nbt "Fuck your mommy hard..."
        else:
            nbt "Fuck me hard..."
        mc "AAaa-Aaahh... oh god, I'm cumming..."with hpunch 
        nosc "A-A-A-aaaa-aAaaahhh..."
        mc "*Panting* I'm gonna fill you up so much..."
        mc "*Panting* You won't be getting out of it this time..."
        nsc "*Giggles* Y-Yeeaaahhh-haa..."with hpunch
        nsc "F-Fill me up..."with hpunch
        mcsc "OH MY GOD...."with hpunch
        play sound debris
        play sound2 debris3
        play sound3 penetration3
        play sound8 clothes4
        scene gt 112 with dis08
        bla "You pull Nancy's body towards you and abruptly spread her legs completely." with dis
        play sound4 cumall
        play sound5 slap1
        scene gt 113
    mcsc "*Cumming* AAAAAAAGGGGGGGGH..." with hpunch
    play sound4 penetration3
    if novacreampie:
        show gt 109 with dis
    else:
        show gt 112 with dis
    play sound6 cumall
    play sound7 slap1
    if novacreampie:
        show gt 110 
    else:
        show gt 113 
    mcsc "*Cumming* AAAAaaaghhhh..." with hpunch
    play sound4 penetration3
    if novacreampie:
        show gt 111 with dis
    else:
        show gt 112 with dis
    play sound4 cumall
    play sound5 slap1
    if novacreampie:
        show gt 110 
    else:
        show gt 113 
    mcsc "*Cumming* Y-Yeeah, take it all, babe..."with hpunch  
    if novacreampie:
        nosc "G-Gggnnnnggg..."   
    else:
        nsc "G-Gggnnnnggg..."
    play sound penetration3
    play sound2 penetration3
    play sound3 penetration2
    if novacreampie:
        scene gt 111
    else:
        scene gt 114
    mc "*Panting* Aahhhh... aaahhhh...aaaahh..." with dis2
    mc "*Panting* G-God..."
    if novacreampie:
        n "Oh my, you're such a champion, Nova..."
        mc "*Still panting* Indeed, she is..."
        nobt "*Giggles* T-Thank you..."
    else:
        mc "*Panting* I've been longing for this ever since you left me wanting last time..."
        no "*Giggles* Wow..."
        nbt "*Panting* Y-You sure didn't hold anything back..."
    play soundloop jungle fadein 13
    stop music3 fadeout 14
    play sound rubbody
    scene gt 115 with dis17
    play sound2 debris
    play sound fallfull
    mc "*Collapsing next to the rock* Jesus Christ..." with vpunchslow
    mc "I-I need a moment to catch my breath..."
    $ renpy.end_replay()
    no "*Panting* I need two..."
    mc "You girls are... nothing short of amazing..."
    no "*Giggles* T-Thank you."
    n "We could certainly say the same about you..."
    mc "Damn... you squeezed me like a peach."
    n "A peach...? You mean a lemon?"
    no "*Giggles* Yeah, what kind of peaches have you been eating, [mc]?"
    mc "*Snorts* I meant a lemon, yeah. My blood is still coming back to my brain."
    n "*Chuckles* Fair enough."
    show gt 116
    mc "*Looking up* Whoa, that was something else..."with dis12
    mc "Hmmm... I guess we should launch another flare."
    n "Oh, right, it's been a while."
    no "I totally forgot about it."
    n "*Giggles* Understandable..."
    mc "There has to be a way out of this cursed place..."
    mc "But how?"
    mo "Mr. [nickname]!"
    mc "I'm even hearing voices now."
    mc "*Sighs* There has to be a way to break this curse."
    no "No, wait! I also heard that!"
    mc "Huh?"
    mc "*Shouting* HELLO...?!"
    play music2 ["<silence 2>"]
    queue music2 piratewellermanfast fadein 4 
    stop soundloop fadeout 20
    play sound debris
    show gt 117 with dis
    pause .2
    mo "Oh, there he is!" with dis14
    ed "About time!"
    play sound debris3
    show gt 117b
    mc "*Standing up* OH MY GOD!" with dis12 
    mc "ED! MORTY!"
    mc "Oh fuck yes, I've never been happier to see dead people!"
    show gt 117
    ed "And... he's naked."
    mo "*Whispering* Damn, he's packing."
    ed "*Whispering* Yeah, I used to have one like that back when I still had flesh."
    mo "*Whispering* No, you didn't."
    show gt 117b
    mc "How did you find us?!"
    show gt 117
    ed "Ah, my brother saw one of those stinky gnomes trying to swim to your boat when a Paradox White Shark devoured him."
    mc "Heh, serves him right..."
    ed "Then we spotted the flares coming from the jungle cliffs, and..."
    ed "Well, you don't need a brain to put two and two together."
    mo "*Whispering* I can't stop staring at his junk."
    show gt 117b
    mc "I LOVE YOU!" 
    show gt 117
    ed "We've only got 2 hours before the Island of the Lost Souls sinks into the ocean, you know?"
    mc "Shit, just two hours?!"
    ed "And where are your friends, by the way?"
    show gt 118
    mc "Huh..." with dis
    n "*From behind a rock* Getting changed!"
    no "*From behind a rock* Fuck, where's my bikini?!"
    show gt 117
    mc "Um... they'll be ready in a minute!" with dis
    mc "Do you think we can still make it?"
    ed "Well... if you can all climb a rope and run fast... maybe."
    mc "Ah, I like the sound of that “maybe”! I've worked with worse odds!"
    ed "Alright, then let's wrap this up! Follow us!"
    mc "YES!"
    mc "LET'S GET THAT TREASURE!" with hpunch 
label pirateending:
    play sound7 wave
    scene pm7long with Dissolve(3.3)
    pause 3.7
    play sound6 wind4
    play soundloop wavesship fadein 2
    stop music2 fadeout 7
    scene gp 1 with Dissolve(3.3)
    play sound seagull
    play sound2 wave
    pause
    ed "Well... " with dis12
    ed "Ladies and gentlemen... the Island of the Lost Souls."
    ed "At least we tried."
    play sound stairswood2
    play sound2 seagull
    show gp 2
    mc "What do you mean, “at least we tried”?" with dis15
    mc "We made it!"
    show gp 3
    ed "Well yes, but actually... no."
    show gp 1
    ed "Do you see that pointy mountain over there, across the bay?"with dis
    mc "Uh-huh."
    ed "There's a big cave entrance at the base of it. You need to enter the mountain and traverse its galleries until you reach a secret temple."
    ed "And... that's where the treasure is hidden. Supposedly."
    mc "And what's the problem?"
    play sound2 earthquake2
    play sound seagulls
    bla "An earthquake shakes the ship violently, causing you to stumble as you watch the birds fleeing the island." with hpeq
    show gp 3
    ed "Yeah... {i}that's{/i} the problem." with dis
    ed "We only have about 20 minutes until the sun sets completely."
    ed "After that? Poof, the entire island, along with all its treasures, sinks into the ocean as if it never existed."
    ed "The water in the bay is too shallow for the ship to pass safely, and it would also take us about 20 minutes to go around it."
    ed "By the time we got there, the temple would already be disappearing into the depths of the ocean."
    show gp 2
    mc "And why can't we just disembark here and make our way to the temple on foot?"
    mc "I could start running now. I'm ready."
    show gp 3
    ed "Heh."
    ed "Well, first off, the dead can’t set foot on the island. Otherwise, my brother and I would have been here ages ago."
    ed "Secondly, it would take you about three hours to reach the mountain on foot without a guide."
    ed "Three hours of walking... and 20 minutes before the island vanishes."
    ed "The maths ain't mathin', my friend."
    show gp 4
    n "But what if we could get there before it sinks?"
    show gp 5
    ed "Uh... I guess?"
    ed "I'm not sure of what you're suggesting."
    show gp 6
    mo "I mean... no offense, ma'am, but there's not a single human fast enough to..."
    show gp 7
    mo ". . ."with dis12
    play sound shiphit volume 0.5
    play sound2 speed
    play soundlow wave
    play sound3 seagulls volume 0.65
    scene gp 8 with hpunch
    pause .6
    show gp 9 with dis25
    pause
    show gp 10
    mo "Okay, nevermind." with dis
    show gp 5
    ed "Holy smokes, you guys are something else."
    ed "I can see now how you managed to reach the Paradox Archipelago with all your limbs intact."
    show gp 12
    no "Yeah, we make a good team..."
    show gp 11
    if harempath:
        n "The best of teams, if you ask me..."
        show gp 12
        no "And we haven't even got the full crew on board yet."
        show gp 11
        n "Not yet! But... we will."
        n "I think once we're all together, we're gonna be even more... powerful."
        show gp 12
        no "*Giggles* I’m inclined to trust Mistress Nancy's words on that..."
        show gp 5
        ed "Hehe... yes... what a team we make."
        show gp 12b
        mo "I think they're not including us, Eddy."
        show gp 12c
        ed "Shit, really?"
        ed "But we rescued them from the Paradox Jungle and guided them here."
        show gp 12b
        mo "Yes, but I'm pretty sure they were speaking with a double meaning about their relationship."
        mo "I think they have some sort of polyamorous setup."
        show gp 5
        ed "Oooooooohhh... I see..."
        ed "Lucky bastard, that [nickname]. He's got his own harem!"
        ed "*Melancholic sigh* I used to have one of those when I was still alive too."
        show gp 12b
        mo "No, you didn't."
        show gp 12c
        ed "Shut up."
        ed "You just never got to meet them."
    else:
        n "The best of teams!"
        show gp 5
        ed "Yep, can't deny that."
    show gp 12
    no "Anyway, let's get moving!"
    no "We need to set sail for the mountain too!"
    no "Someone’s got to pick up [mc] when he leaves the temple and the whole island begins to sink."    
    show gp 5
    ed "Yes, that's a good point."
    show gp 12
    no "Let's–"
    play sound shiphit
    play sound2 seagulls
    play sound3 kraken
    play music2 piratedark
    scene gp 13 
    no ". . ." with hpunchslow
    show gp 4
    n "Uh..." with dis12
    n "Was that another earthquake...?"
    show gp 12c
    ed "Eh... yeah, no, I don't think so."
    ed "Morty?"
    play sound4 wood2
    play sound6 stairswood2
    scene gp 14
    mo "Let's not jump to conclusions, it doesn't have to be the Kraken. It could just be Billy-Bolo, the friendly beluga from Lost Souls."with dis14
    play soundloop2 kraken2
    play soundloop waves
    play sound3 krakenjump
    scene gp14b
    kra "{sc=3}RRAAAAAAAAAAAAAAAAAAAGGGHGHGHHHHHH!!!{/sc}" with vpunchslow
    mo "Okay, it's the Kraken."
    show gp 16
    mo "*Dramatic tone* This is our end, my cherished comrades!" with dis 
    mo "*Dramatic tone* It was an honor sailing alongside you!"
    mo "*Dramatic tone* I'll see you in the next life!"
    show gp 5
    ed "Welp, looks like the island's guardian has found us."
    ed "But hey, it's not all bad! When the kraken devours you, your soul gets bound to these waters, and you get to become a sexy skeleton like us!"
    ed "And lucky for you, Davy Jones is always on the lookout for new recruits at the Bay of the Undead."
    show gp 11
    n "Thanks for the offer, Ed, really, but we've got other plans."
    n "We can't afford to die just yet."
    play sound2 whoosh6
    play sound6 woodhit
    play sound7 impactwood
    scene gp 17
    no "Yep, I'm with Nancy on this one." with pr
    no "[mc] is doing everything he can to reach that treasure, and we need to be there to back him up!"
    no "Nothing personal, buddy, but we're on a tight schedule!"
    play sound charge
    play sound2 lasercharge
    play sound3 fire 
    scene gp17 
    pause 0.1
    show gp18 with dis2
    stop sound 
    stop sound2
    stop soundloop2
    play soundloop jungle
    scene gp 19
    pause .4
    play sound7 seagulls
    play sound bombdistant1
    play sound2 bombdistant2
    play sound3 bombdistant1
    show gp 20 with dissolve
    pause .3
    show gp 19 with dis 
    scene gp 21 with dis15
    mc "(Shit, did that come from our ship's direction?)" with dis
    mct "Are they being attacked?!"
    show gp 19
    mc "(Fuck... I can't turn back now. I need to trust the girls and finish the mission.)"with dis
    mc "(I can't let them down.)"
    mc "(Hmmm... there seems to be an opening in the side of the mountain. It's gotta be there.)"
    mct "ONE LAST PUSH." 
    play sound2 speed
    play sound3 speed
    scene gp22 with hpunch 
    pause 
    stop music2 fadeout 5
    stop soundloop fadeout 10
    scene black with dis25
    show screen afewminuteslater with dis2
    pause
    play soundloop2 cave fadein 8
    hide screen afewminuteslater
    scene gp 23
    with dis25
    pause .1
    bla "After running with all the strength you have left, the hours without sleep and the growing hunger begin to take their toll, leaving you utterly exhausted and unable to use your powers any further." with dis25
    play sound5 panting fadein 1 volume 0.8
    mc "*Panting* (F-Fuck...)"
    mc "*Panting* (I'm... so fucking tired...)"
    mc "*Panting* (I shouldn't... abuse this state...)"
    mc "*Panting* (I-I need a minute to–)"
    mct "Wait..."
    mct "Is that... artificial light?"
    play soundlow footsteps3 
    show gp 24 with dis22
    play music piratetemple fadein 6
    mct "No way..." with dis15
    mct "FINALLY!"
    mct "That's gotta be the temple! I made it!"
    play sound2 earthquake2
    scene gp 24 with hpeq
    pause .3
    play soundlow debris2
    mct "This place isn't going to stay put for much longer..." with dis15
    mct "I need to get out of here fast."
    scene gp 25 with dis22
    bla "You slowly enter the temple carved into the mountain, discovering a wide area and a rock bridge spanning a vast chasm." with dis22
    mct "Wow..."
    mct "This place makes me feel so tiny."
    show gp 26
    mc "*Leaning over the edge* (And that's a long drop.)" with dis12
    mct "Probably best not to look down too much."
    play soundlow footsteps3 fadein 2
    scene gp 27 with dis22
    bla "You measuredly walk across the solemn bridge until you reach the end of the cave, where an austere altar stands." with dis22
    play sound footsteps
    scene gp 28 with dis2
    mc "(Alright... this has to be it. The artifact El Coyote wanted us to find.)"with dis17
    mct "The Heart of the Abyss."
    play sound clothes3
    show gp 29 with dis17
    mct "It's cold..." with dis14
    mct "And it shines, but it doesn't produce any light."
    mct "It's just... there. Floating."
    mct "Why was he so keen to get this thing?"
    play sound2 earthquake2
    scene gp 29 with hpeq
    pause .3
    play soundlow debris2
    mct "Anyway, now’s not the time for questions." with dis15
    play sound4 rubbody
    scene gp 30
    mct "I can ask him later. Let's grab this thing and get out of here." with dis12
    ec "You really did it."
    mc ". . ."
    play sound7 clothes3
    play sound5 ceramic volume 0.3
    scene gp 31 
    mc "*Turning around* . . ." with dis15
    mc "How..."
    play sound6 ["<silence 0.6>", earthquake2]
    scene gp32 with dis2
    mc "It's... impossible..."with dis15
    ec "I had my doubts, I'll admit."
    ec "Especially when you vanished in the Paradox Archipelago for hours. Hell, I thought you were a goner."
    ec "But... here you are. Overcoming every single obstacle. And still on time!"
    show gp 33
    ec "Seems like your reputation is well-deserved, [nickname]." with dis15
    show gp 34
    mc "How..."
    mc "How are you here...?"
    mc "How the hell did you do it? Hiding inside a barrel in the ship's hold? Teleportation device? Invisibility potion?"
    mc "You... shrank yourself and hid inside my pocket...?"
    show gp 35
    ec "Ahh... a magician never reveals his tricks, [mc]."with dis
    ec "No decoys this time though, I promise. I'd never send a substitute for an exchange involving items of... such profound value."
    show gp 34
    mc "Mmph." with dis 
    mc "Alright, then... keep your secrets."
    show gp 36
    ec "Now, I'd love to stay and have a fruitful conversation with you, but we both know we need to leave this island soon or we'll sink into the ocean with it."with dis12
    ec "So..."
    show gp 37
    mc "First, tell me what the Heart of the Abyss does."
    ec ". . ."
    show gp 38
    ec "It allows you to speak with the dead. Once a year, right before the Island of the Lost Souls disappears."
    ec "And yes, I'm aware it's too late now, but I'll be ready next year."
    show gp 37
    mc "The dead...?"
    mc "Who..."
    mc "Who do you want to..."
    show gp 38
    ec "I don't believe that's relevant to our agreement."
    show gp 37
    mc "It is to me. Either you tell me, or there's no exchange." 
    ec ". . ."
    show gp 39
    ec "*Exhaling* Mmmmh..." with dis12
    show gp 40
    ec "My daughter."
    show gp 39
    mc "Your daughter...?"
    ec ". . ."
    show gp 40
    ec "It's been... consuming me."
    ec "This corrupt world took her away way too soon."
    ec "I..."
    ec "I just want to see her one last time."
    ec "Just once."
    show gp 39
    mct "Damn..."
    mct "His words feel different this time. They actually convey... truth."
    show gp 40
    ec "I know she's here somewhere, and I..."
    ec "I just want to tell her I love her one last time. That's all."
    show gp 39
    mc "You... {i}know{/i} she's here?"
    show gp 40
    ec "Eternum... is much more than just a VR world, [nickname]." 
    ec "I believe it really is the afterlife humankind has always pondered about."
    ec "A reality that's being... poisoned and perverted by us, the living, intruding where we don't belong."
    show gp 42
    ec "But... I don't have to tell you, do I, [mc]?"with dis12
    ec "Something tells me you already know."
    ec "Am I wrong?"
    show gp 41
    mc ". . ."
    ec "Hmph."
    show gp 42
    ec "But anyway... I digress. I believe we had a deal, didn't we?"
    ec "The Heart of the Abyss. Give it to me."
    show gp 41
    mc "The Gem of Doom."
    ec ". . ."
    play sound clothes3
    play sound2 clothes
    scene gp 43
    bla "El Coyote reaches into his pocket and pulls out a dazzling gem, instantly recognizable as genuine." with dis22
    show gp 44
    ec "So..."
    ec "On the count of three?"
    play sound speed
    play sound2 debris3
    play sound7 grab2
    show gp45 
    ec ". . ." with hpunch
    scene gp 46
    ec ". . ." with dis08
    play sound4 earthquake2
    play sound3 earthquake2
    play sound5 ["<silence 2.9>", debris2]
    scene gp47
    ec "Hmph." with dis
    scene gp 48
    ec "Well, I think that was our final warning! Time to get out of here." with dis14
    ec "It's been a pleasure doing business with you, [nickname]."
    ec "Everyone seems to be assuming Thanatos will win the Gems race, but... if I were to bet, my money would be on you."
    ec "You have something special, kiddo."
    ec "If our paths ever cross again, I'll share the tale of how I got that Gem. It's quite the story, I promise!"
    ec "Until then... farewell, friend."
    mc "I'm clearly faster and stronger than you."
    show gp 49
    ec "Huh?"with dis12
    show gp 49b
    mc "You might be good at hiding, but... you're exposed now."
    mc "I already have the Gem in my hands. What stops me from killing you and taking both the Gem and the Heart of the Abyss?"
    show gp 50
    ec "Hmph."
    show gp 51
    ec "Nothing. Nothing is stopping you."
    ec "I just... don't think you'll do it."
    show gp 49b
    mc "Why not?"
    show gp 52
    ec "No reason."
    show gp 53
    ec "Sometimes a man's just gotta trust his gut." with dis
    scene gp 49b
    ec "Flip a coin and... believe you already know which side it'll land on."
    mc ". . ."
    mc "Flip a coin..."
    play sound3 flashback3 volume 0.7
    scene idrielpirate
    pause 0.26
    mc ". . ."
    scene gp 54
    bla "You turn around, only to see Coyote vanish as quietly as he arrived." with dis17
    mct "What an enigmatic man..."
    mct "He might not be strong, but... I have a feeling he's smarter than any of us."
    mc "*Coughs* (I don’t even think I could have taken him on, even if I'd wanted to – I used my last bullet there. I'm too drained to use my powers now.)"
    play sound4 earthquake2
    play sound3 earthquake2
    play sound5 ["<silence 2.9>", debris2]
    scene gp 54 with hpeq
    mct "Fuck, the island is about to collapse." with dis15
    mct "Time to get back to Tortuga. I better hurry up."
    mct "Please, don't start sinking just yet..."
    play sound7 earthquake2
    stop music fadeout 7
    stop soundloop2 fadeout 7
    scene black with dis3
    stop sound7 fadeout 5
    show screen afewhourslater with dis25
    pause
    play soundloop night2 fadein 6
    hide screen afewhourslater with dis22
    scene gp 55 with dis27
    play sound debris
    play sound2 fall2
    mc "*Sitting on the sand* Aggghh..." with dis22
    mc "Man, I can't believe we actually made it back alive."
    mc "What a trip, though..."
    mc "Even with Ed and Morty's so-called “shortcut”, it still took us a good five hours to get back to Tortuga."
    mc "*Yawns* I feel like I've been awake for three days straight."
    scene gp 56
    mc "Do you think El Coyote managed to escape the island too?" with dis12
    mc "Nova?"
    no "Zzzzz..."
    mc "*Chuckles* (She's so cute when she's sleeping.)"
    mct "I'm surprised she managed to stay awake for so long. She's definitely stronger than she looks."
    mct "I almost feel bad waking her up."
    mc "Hey, Nova?"
    mc "We have to go. It's time."
    no "Zzzzz..."
    mc "No–"
    play sound sand 
    play sound2 debris3
    show gp 57
    no "W-ww-ww-AaGgaa! No! I-It wasn't me!" with hpunchslow
    mc "W-What?"
    play sound3 debris
    show gp 58
    no "Oh... s-sorry." with dis12
    no "I was having a nightmare."
    show gp 59
    mc "*Chuckles* Yeah, I could tell you were in a deep sleep."
    show gp 58
    no "I don't think I've ever been this exhausted in my life."
    no "Can we finally go now? I need a bed..."
    show gp 59
    mc "Yes, let's meet up with Nancy."
    mc "She should be almost done."
    play sound footsteps3
    show gp 60
    n "*Turning around the corner* Indeed, I am! Let's get out of here." with dis2
    mc "Ah, speak of the devil!"
    play sound2 debris
    show gp 61
    mc "*Standing up* So, how did it go?" with dis12
    mc "Did you actually lend the WRE ship to Ed and Morty?"
    show gp 62
    n "Yes, but with the condition that it's at our disposal whenever we need it."
    n "They were still so happy."
    show gp 61
    mc "Ah, nice."
    mc "It’s always good to have allies in different servers."
    mc "And since in the end I couldn't snag anything from the Island of the Lost Souls... it’s the least we could do. Those two saved our lives."
    play sound debris
    play sound3 ["<silence 0.6>", siren] fadein 3 volume 0.18
    show gp 63
    no "*Yawns* AAAAaaaaaagh..." with dis15
    no "C-Can we go find the Exit Portal now?"
    mc "What was that sound...?"
    play soundlow spell2
    play sound2 spell3
    play sound3 debris
    show gp64 
    no "AAAAa-aaAAAAAA-gaaahHHH-MOTHERFUCK-!" with hpunch
    play music2 founder fadein 12
    play sound4 footsteps3
    scene gp 65
    mc "*Taking a step back* W-What... what’s he doing here?!" with dis17
    n "I think it's one of those public announcements...?"
    tf ". . ."
    play sound debris
    scene gp 66
    tf "Good morning, evening, and night, citizens of Eternum!" with dis12
    tf "I hope you're all enjoying your session today."
    tf "I'm deeply sorry to interrupt your experience, but as you know, I wouldn't do it without a very important announcement to make."
    tf "Today, I'm about to unveil the biggest event we've ever held since I created this world we all love so much."
    show gp 68bb
    no "You didn't create shit..."
    no "Liar."
    scene gp 66
    tf "This event will commence tomorrow, December 4th, and run until the end of January."
    tf "And just like our last cross-server event, you can join in solo or team up with up to three others."
    tf "Ladies and gentlemen, we're excited to introduce... “The Big Hunt”."
    show gp 66b
    if gemevents:
        mct "Oh... I forgot about that. I saw it on Clarence's laptop when I was in Nancy's office, and Dalia mentioned it not too long ago as well."
    else:
        mct "Oh... I forgot about that. Dalia mentioned it not too long ago."
    show gp 67
    tf "And what will we be hunting, you must be wondering...?" with dis12
    tf "Well... if you’re a regular player on the Andromeda server, you’ve likely encountered some of them already."
    play soundlow spell3
    play sound3 debris
    play sound5 alien2
    show gp 68
    tf "This... is a Xenomorph." with dis12
    show gp 68b
    no "W-What the hell is that?!"
    if anniepath:
        mc "Yeah... I ran into way too many of these things when I visited a space station with Annie."
    else:
        n "Yeah... I saw a small herd of them in Ion with Dalia a few days ago."
    n "They say the Andromeda server is infested."
    show gp 68
    tf "As you probably know, certain political groups are bent on taking down Eternum by any means necessary."
    tf "They created this virus to destroy our paradise. It’s spread throughout Andromeda and has even been spotted in the servers of Ion, Meiyo, Valley of the Kings, and The Red Herring."
    show gp 67
    tf "However, we won’t be intimidated by this threat." with dis14
    tf "It is time... to fight back."
    tf "Together, we’ll defeat this plague and reclaim our servers."
    tf "And to show my gratitude... the player or team that takes down the most Xenomorphs from tomorrow until the event ends will earn a highly valuable reward."
    play sound rubbody
    show gp 69 with dis12
    play sound2 deception
    tf "The 9th Gem of Doom." with dis14
    mc "No fucking way..."
    tf "Eight Gems have already been discovered and are in the possession of players like you. And once this one is claimed... only one will be left."
    tf "The endgame is finally within reach, my children."
    tf "It is time to give it your all."
    play sound2 rubbody
    show gp 67
    tf "Don't forget. The person who manages to gather all 10 Gems will gain access to the Temple of Acheron and thus claim the throne of Eternum." with dis12
    tf "Becoming... the most powerful person on Earth."
    show gp 66
    tf "And that's all I've got for you!" with dis14
    tf "Thank you for listening, and be sure to spread the word to any friends who missed this announcement today."
    show gp 65 with dis12
    tf "Keep fighting, citizens of Eternum." with dis
    tf "And have a good hunt."
    play soundlow spell2
    play sound2 spell3
    play sound3 debris
    show gp 70 with flashfast
    stop music2 fadeout 12
    pause 
    show gp 74
    no "Ugh... my brain’s too tired and my stomach’s way too empty to process all this right now." with dis14
    no "But basically... we kill Xenomorphs and we get a new Gem of Doom?"
    play sound7 footsteps3
    scene gp 72
    n "It seems so." with dis15
    n "Though... it’s a bit odd, innit?"
    n "If the Founder really needs all 10 Gems to become an all-powerful “god” in Eternum, why would he give away one he already has?"
    show gp 71
    mc "Hmm, maybe it’s to motivate the entire player base to find the last one?"
    mc "If people know there’s only one Gem left, it’ll drive everyone to hunt it down."
    show gp 72
    n "Huh..."
    n "Yeah... that's a good point."
    n "He definitely seemed to be trying to hype up the players to step up their search for the last Gem."
    show gp 71
    mc "He’s a natural liar. I mean, he’s trying to pass off this plague as a “virus” from who knows where."
    mc "And well, he’s probably confident that whoever collects all 10 Gems won’t know how to use them and will end up bringing them to him anyway."
    show gp 72
    n "Would we even know what to do with them if we ever manage to gather them all?"
    show gp 71
    mc "Eh..."
    mc "Well, honestly, I'm not sure."
    mc "But in any case, we shouldn't worry about that for now."
    mc "We need to focus on finding a way to defeat Thanatos. And if the Founder is really offering a Gem as a reward in this event, we need to go all in."
    show gp 72
    n "Yes, that's true..."
    n "We should come up with a strategy to ensure we’re the ones who take down the most aliens."
    show gp 73
    no "*Yawns* I th-think...waawa...aaahh...shouldawa."
    show gp 74
    no "Oh my god, s-sorry."with dis08
    show gp 75
    n "*Chuckles* Yeah, Nova's right."with dis
    n "I think it's time for us to get some sleep. We've been awake for over 24 hours now, and not exactly relaxing on the sofa."
    show gp 76
    mc "*Yawns* Yeah, let's go."
    mc "Tomorrow we can tell the others about this and come up with a plan of action."
    play soundloop2 waves fadein 7
    stop soundloop fadeout 10
    show gp 55 with dis27
    pause
    play sound planks
    show gp 77 with dis27
    mc "Oh god, what a beautiful sight." with dis2
    mc "Do you think we'll be able to integrate back into society?"
    n "*Laughs* Come on, don't be so overdramatic."
    play sound2 wood2 volume 0.7
    show gp 78
    n "Is Nova asleep?" with dis12
    show gp 79
    mc "Yeah, I think so."
    mc "She could probably fall asleep standing up at this point."
    show gp 78
    n "Aw, that's too bad... I wanted to give her a goodnight kiss."
    if not nancypath:
        play sound planks
        show gp 84
        n "*Walking backwards* You better take her to her bed like a gentleman, [mc]." with dis17
        show gp 85
        mc "*Chuckles* I will, I promise."
        mc "Thank you for all your help and also for the incredible day, Nancy."
        show gp 84
        n "I'm the one who should be thankful, [mc]."
        n "We wouldn't have succeeded if it wasn't for you."
        n "You've got a gift of making everything... exciting, to say the least."
        n "Now rest! You deserve it."
        show gp 85
        mc "I will! Good night, Nancy."
        jump posnancyplanks
    n "Will you give her one when you're back to her place?"
    show gp 79
    mc "*Chuckles* I will, I promise."
    play sound2 wood2 volume 0.8
    play sound5 rubbody
    scene gp 81 with dis15
    play music2 love2 fadein 8
    stop soundloop2 fadeout 20
    bla "Nancy leans in and kisses you passionately on the lips."with dis14
    $ nancy_points += 1
    play sound beat
    show screen heartbeat
    nbt "Mmmmmm..." with dis12
    play soundlow wood2
    show gp 82 with dis14
    n "*Giggles* Sorry, I couldn't help it." with dis 
    mc "No, it's... more than okay..."
    if harempath:
        n "I'm a big girl, [mc]."
        n "I can handle rejection."
        n "I can handle... pain."
        n "But you're the first love of these girls. Be kind to them."
        mc "I will..."
        n "As “unusual” as our lives are, we're all still human."
        n "If you ever hurt Nova, Annie, Luna, or Alex... I'll be seriously mad at you, young man."
        show gp 83
        n "Oh, and if you EVER hurt Penny or Dalia..."with dis12
        n "I'll straight-up murder you."
    else:
        n "I'm still not sure of how you convinced me that this could work, [mc]."
        show gp 83
        n "But if my daughters stop talking to me because of you..."with dis12
        n "I'll straight-up murder you."
    play sound planks
    show gp 84
    n "*Walking backwards* Just wanted to make that clear." with dis17
    show gp 85
    mc "*Chuckles* Got it."
    if harempath:
        mc "I love you all, Nancy. I swear."
    else:
        mc "I'll start working on it."
        mc "I love you, Nancy."
    show gp 84
    n "Good."
    if harempath:
        n "We love you too."
    else:
        n "I love you too."
    n "And that's all that matters."
    n "Just... don't mention any of {i}this{/i} to Auntie Cordelia at Christmas dinner, okay?"
    n "She's a bit too... old-school. I'm not sure her heart could handle it."
    show gp 85
    mc "No killing Auntie Cordelia, gotcha."
    show gp 84
    n "*Chuckles* Good night, [mc]."
    n "Thanks for the memorable day."
    show gp 85
    mc "Thank you for everything, Nancy."
    mc "Good night."
label posnancyplanks:
    play sound whoosh1
    pause .1
    play sound2 spell4
    show gp 77 with dis2
    bla "Nancy touches the Exit Portal and disappears without a trace." with dis17
    if nancypath:
        mct "You're a lucky bastard, [mc]."
        mct "Today more than ever."
    else:
        mct "And that's how another adventure finally reaches its end."
    play sound3 planks
    show gp 86 with dis17
    mct "It’s crazy how much one’s life can change in just a few months." with dis15
    mct "And the best part? I feel like this is just the beginning."
    mct "We've got a long, long road ahead of us."
    mc "*Taking a deep breath* (Until next time, New World.)"
    play soundloop waves fadein 4
    mc ". . ."
    stop music2 fadeout 5
    show gp 87
    mc ". . ." with dis15
    show gp 88 with dis06
    pause
    show gp 87 with dissolve
    pause
    play sound rubshort volume 0.75
    scene gp87
    pause 
    mc ". . . ?"with dis
    mct "Why is this thing not wor–"
    play soundloop2 beat3 fadein 5
    play sound planks
    scene gp 77 with dis22
    mc "*Slowly walking away* (W-Wait a fucking second...)"with dis17
    mct "Nova and I entered Eternum without using the neural implant."
    mct "We didn't use Ulysses' trickery to create an astral projection of ourselves."
    mct "So... we cannot use the Exit Portals to leave."
    mct "Does that..."
    mct "Does that mean we're trapped here?!" with hpunch 
    mct "No, no, no..."
    mct "Calm down..."
    mct "Don't let your emotions control you, [mc]."
    scene black
    mc "*Closing your eyes* (I mustn't panic.)"with dis12
    mct "I've already been through this. I managed to get back to the real world when I was with Calypso – I can do it again."
    mct "I just need to concentrate..."
    play soundloop3 rain3 fadein 24
    stop soundloop2 fadeout 22
    stop soundloop fadeout 24
    mc "*Exhaling* Fuuuuu...."with dis
    mct "I can see it."
    mct "An opening."
    mct "I am as much a part of this world as I am of the other."
    mct "Crossing between them is as easy as opening a door."
    mct "I can see it."
    mc "*Exhaling* Fuuuuu...."with dis 
    mct "I."
    mct "Am."
    mct "In."
    mct "Control."
    scene gp 89 with dis25
    mct "Yes..."with dis2
    play sound impactwood
    play soundlow thunder
    mc "FUCK YES!!!" with vpunch
    mc "LET'S GO, BABY!" with hpunch
    no "Mmmmmh...?"
    no "[mc]...?"
    show gp 90
    mc "Oh shit, sorry, Nova." with dis12
    mc "I didn't mean to wake you up."
    mc "I got so focused on getting back to Earth that I almost forgot I was carrying you on my back."
    no "*Yawns* Oh... we're back home already?"
    mc "Yep."
    no "I-I fell into a deep sleep so fast."
    play sound clothes3
    show gp 91 with dis14
    no "*Dismounting you* But I'm glad we're finally back."with dis12
    no "Thank you for carrying me."
    show gp 92
    mc "You're not gonna believe this: we came back without using the Exit Portal!"
    mc "I mean, I think I can only return to the exact spot where I entered Eternum, and I can’t travel between servers like Calypso, but still, it’s... incredible!"
    mc "Isn't it?!"
    show gp 93
    no "Oh... so that's why my left eye still itches and why I'm still wearing the bikini from our pirate quest."with dis
    show gp 94
    no "*Sniffs* And also... why I smell like a fish market." with dis12
    show gp 92
    mc "Exactly! There was no astral projection this time... it was US inside Eternum!"with dis12
    mc "The real us! We didn’t leave any unconscious bodies behind; we entered Eternum with everything!"
    mc "WE-"
    play sound pop
    show gp 95
    no "Wait, wait, wait... what do you mean, {i}our real bodies{/i}?"
    no "No... no astral projection?"
    show gp 96
    mc "Yeah, that's what I'm saying! Real, real!"
    show gp 95
    no "So..."
    no "What would have happened if we had died during our journey to the Island of the Lost Souls?"
    show gp 96
    mc ". . ."
    mc "Um..."
    mc "Well, I don't know."
    no ". . ."
    if not anniepath and alexpath:
        $ alexpoolvisit = True
    play sound impact5
    play sound2 impactwood
    play music quirkynova
    show gp97
    no "WHAT THE HELL DO YOU MEAN, YOU DON'T KNOW?!" with hpunch 
    no "I WAS SO CLOSE TO DYING LIKE... A DOZEN TIMES!"
    mc "B-But what matters is that–"
    if novapath:
        no "WHERE WOULD YOU BE IF THOSE MERMAIDS HAD DRAGGED YOU TO THE BOTTOM OF THE OCEAN?! I BARELY GRABBED YOU IN TIME!" with hpunch 
    else:
        no "WHERE WOULD I BE IF THOSE MERMAIDS HAD DRAGGED ME TO THE BOTTOM OF THE OCEAN?!" with hpunch 
    mc "Don't think about “what if”!"
    mc "What’s important is that it didn’t happen and we’re safe now!"
    no "OH MY GOD, I COULD HAVE DIED SO MANY TIMES!"with hpunch 
    no "NANCY TOO!"with hpunch 
    mc "But Nancy didn't even–"
    no "WE ALMOST GOT SWALLOWED ALIVE BY A WHALE!"with hpunch
    mc "W-Well yeah, but–"
    no "WHERE WOULD I BE NOW?!"with hpunch 
    no "TURNED INTO A SKELETON LIKE ED AND MORTY? IN HELL? SURROUNDED BY ETERNAL DARKNESS?!!"
    no "I'M NOT READY FOR THAT!"with hpunch 
    mc "What ma–"
    no "I CAN'T HANDLE IT!"with hpunch 
    menu:
        with dis
        "Kiss her [gr][mt](Nova's path)":
            no "I ALMOST–" with hpunch
            if not novapath:
                mc "*Leaning towards her* (Now.)"
                play sound slap1
                play sound2 slap3
                stop music
                scene gp 103b
                no "*Slapping you* What the hell do you think you're doing?" with hpunch
                mc "S-Sorry. I... saw it in a movie."
                no "You're a pervert."
                mc "W-Well, at least I stopped your panic attack."
                jump novanokiss
            stop music
            play sound3 whoosh3b
            play sound7 bodycollide2
            scene gp98
            no "Mhh!" with hpunch
            no "Mmmmhh."
            stop soundloop3 fadeout 22
            play music romantic4 fadein 6 volume 0.8
            show gp 99
            nobt "Mmmmmhhhhhhhhh..." with dis15
            $ nova_points += 1
            play sound beat
            show screen heartbeat
            bla "You and Nova merge in a kiss where raw desire and intensity give way to romance and gentle passion."with dis 
            no "Mmmmm..."
            play sound6 clothes3
            show gp 99b with dis2
            no "*Purring* Mmmmmmmmmmmhh..." with dis17
            mc "*Clears throat* AS I WAS SAYING, what matters is that we're safe now."
            mc "I'll be honest, I wouldn't have put you in so much danger if I had known the true extent of the risk, although... well, let's face it, you wouldn't have agreed to stay behind anyway."
            mc "In any case, we all made it back in one piece, and that's what counts."
            mc "We can't dwell on the past, can we?"
            no "Mm-hm..."
            show gp 100
            no "Yeah... you're right."with dissolve 
            no "We've gotta... keep moving forward."
            show gp 101
            mc "Hell yes!"
            show gp 100
            no "We're alive and we have three Gems of Doom."
            no "And you've also got a new super cool power! There's literally nothing we can complain about."
            show gp 101
            mc "And it's not even about the Gems or Ulysses anymore."
            mc "I admit, I got... obsessed. Blinded by them."
            mc "I guess you could say that near-death experience in the alley changed me. It made me see what truly matters in life."
            mc "Yes, we still have to pursue our mission and save the world, but..."
            if harempath:
                mc "Honestly? I'd let the world burn to the ground for you, girls."
            else:
                mc "Honestly? I'd let the world burn to the ground for you."
            mc "I love you, Cheeto."
            show gp 101b
            no "*Giggles* Oh my god."with dis08
            no "Did you really say that? I hope this isn't a dream."
            mc "*Chuckles* I certainly hope not."
            show gp 100
            no "I know “today” has lasted like 28 hours, b-but..."with dis08
            no "Even despite El Coyote's attack, the giant orca, the murderous mermaids, the hallucinogen goblin, the endless jungle loop, the kraken, and even your murder attempt in Chinatown... this has truly been..."
            no "The best day of my life."
            no "I..."
            no "I love you."
            show gp 101
            mc "I love you so much, Nova."
            mc "*Sighs* It’s so hard to say goodbye, even if it’s just until next weekend."
            show gp 100
            no "I know... a whole week! We're so busy, huh?"
            show gp 101
            mc "Can't wait to finally retire after a lifetime of hard labor."
            show gp 100
            no "*Laughs* Same."
            no "But until then... I guess I've gotta continue going to college."
            show gp 101
            mc "Yeah... unfortunately."
            show gp 100
            no "Will you miss me...?"
            show gp 101
            mc "*Chuckles* Every day."
            show gp 100
            no "Good."
            no "Me too..."
            no "I will try to–"
            show gp 102
            san "Nova? Is that you??" with dis
            san2 "Is she finally home?!"
            san2 "NOVA!"
            play sound punch 
            show gp 103
            no "*Pushing you* F-Fuck, you've gotta go!" with hpunch
            mc "W-Why? They already know I'm here."
            no "They knew you were here like 10 hours ago! T-They'll think w-we've been at it all night!"
            mc "Well, that wouldn't be that far from the tru–"
            play sound doorslam
            play sound2 doorclose
            play soundloop rain2 fadein 2
            scene gp104
            no "*Closing the door behind you* [mc]!" with hpunch 
            no "Don't be a pervert!"
            no "*Giggles* Although... okay, fair enough."
            no "*Whispering* Now, GO! Talk to you later!"
            no "*Whispering* Love you!"
            $ novaloveyou = True
            jump novayeskiss
        "Let her calm":
            mc "Um..." with dis
            mct "It's probably better if I don't say a word."
            no "SIX, SEVEN... EIGHT! NO, WAIT, NINE!"
            no "I ALMOST DIED NINE TIMES!" with hpunch 
            jump novanokiss
label novanokiss:
    san "Nova? Is that you??" 
    san2 "Is she finally home?!"
    san2 "NOVA!"
    play sound punch 
    play sound2 musicstop
    stop music
    scene gp103bb
    no "*Pushing you* F-Fuck, my parents! You've gotta go!" with hpunch
    if novapath:
        mc "W-Why? They already know I'm here."
        no "They knew you were here like 10 hours ago! T-They'll think w-we've been at it all night!"
        mc "Well, that wouldn't be that far from the tru–"
    else:
        mc "Eh?? W-Why?"
        no "What do you mean, why?! We're half-naked!"
        no "T-They'd think w-we've been at it all night!"
        mc "But–"
    play sound doorslam
    play sound2 doorclose
    play soundloop rain2 fadein 2
    stop soundloop3 fadeout 1
    scene gp104
    if novapath:
        no "*Closing the door behind you* [mc]!" with hpunch 
        no "Don't be a pervert!"
        no "*Giggles* Although... okay, fair enough."
        no "*Whispering* Now, GO! Talk to you later!"
    else:
        no "*Closing the door behind you* Sorry, they're traditional people!" with hpunch 
        mc "O-Okay, I understand."
        no "*Whispering* Now, GO!"
        mc "*Whispering* Alright, alright!"
label novayeskiss:
    san2 "Nova! Where the hell have you been?!"
    no "*Turning around* O-Oh, hey! It feels soooo good to be home!"
    san2 "Do you know what time it is?!"
    no "Oh come on, Dad, I'm 21! I'm not a kid anymore!"
    if novapath:
        san "Are you okay, though? Your dad and I were worried after what happened with [mc]..."
        no "Huh...? Oh! Nothing happened! I'm fine! We're fine!"
        san "Aw, I'm so happy to see you smiling again, sweetie."
    else:
        san "Are you okay, though? Your dad and I were worried..."
        no "I'm fine! Totally fine!"
    san2 "What are you wearing...?"
    no "Oh..."
    no "Haha, funny story... erm... you see, I was on my way home when a flash mob broke out at the community pool. They needed one more person to break the world record, so..."
    san2 "What...?"
    san "At this time...?"
    no "L-Let's go to the living room! I'll explain it all there!"
    mc "*Chuckles* (As kooky as the day I met her.)"
    play sound carpasswet
    show fe 14 with dis17
    mc "*Yawns* (Jesus, the sun's already up. I really need to get some sleep.)" with dis12
    mct "And tomorrow's already Monday again... ugh."
    mct "I think I’ll skip a few classes and just crash for 20 hours straight."
    mct "I hope Mr. Keating doesn't get too mad..."
    mc "*Yawns* (I mean, we were saving the world. I'm sure he'd understand.)"
    stop soundloop fadeout 13
    stop music fadeout 8
    scene black with dis3
    show screen afewdayslater with dis27
    pause 
    if anniepath:
        play music2 happy14 fadein 10
    hide screen afewdayslater with dis27
    if not anniepath:
        jump arabiadayletsgo2
    scene gf 0
    with dis3
    pause
    play sound footsteps
    scene gf 1 
    bla "Annie nervously enters the living room walking backward, adjusting the front of her dress." with dis15
    a "Alright, so..." 
    a "Here it is. I need you to rate it from 1 to 10. And be honest!"
    a "I mean... well, if it's less than a 7, don't tell me, please. Or lie."
    a "If it's less than a 7, just say seven."
    play sound2 clothes3
    scene gf 2
    a ". . ." with dis2
    l "Wow!"
    show gf 3
    l "You look so beautiful!"
    l "There's no way anyone could rate this less than a 10."
    show gf 4
    a "R-Really? You sure? Isn't it too... formal? Or too tight?"
    show gf 3
    l "Not at all."
    l "You look so pretty!"
    play sound2 pop volume 0.6
    show gf 5
    a "I'm gonna be wearing exactly the same thing, the only difference would be my hair. It's finally starting to be long enough, so I'll probably wear it down."
    play sound pop volume 0.6
    show gf 6
    a "Well... and I'll also be wearing heels so I don't look like a hobbit."
    show gf 3
    l "I'm sure you'll be turning heads either way, Annie, don't worry."
    l "I mean... in a good way!"
    show gf 4
    a "Alright... good. I'm glad you think so, I needed a second opinion."
    a "I spent like... 8 hours at the mall yesterday."
    show gf 7
    l "I'm sorry I don't have more insightful comments."
    l "I'd be in black clothes all the time if it wasn't for Penny."
    show gf 3
    l "You should show her instead!"
    show gf 8
    a "Oh, no, no, no. Penny, Dalia, and Nancy were not an option."
    a "We live together, so that would..."
    a "I mean, they would..."
    show gf 9
    a "*Muttering* They would ask too many questions."
    l "They what?"
    play sound pop volume 0.6
    show gf 4
    a "*Clears throat* T-They would be too nice to me! I wouldn't be able to tell if they're being honest or just trying to avoid awkward dinner conversations."
    show gf 2
    l "Ohh... I see."
    play sound ["<silence 0.3>", chair1]
    show gf 10 with dis12
    a "In any case, thank you for helping me, Luny." with dis12
    show gf 11
    l "Don't mention it."
    l "I'm so happy we got to spend time together today."
    show gf 10
    a "I know! That's why I suggested teaming up today!"
    if lunapath:
        show gf 15
        a "I mean... ever since that day at the cafe, you've seemed a bit distant, so I thought..." with dis08
        a "I know you don't like people touching your hands and that's why you always wear gloves. I'm sorry I forgot that day."
        a "So I just wanted to apologize if I made you uncomfortable in any way."
        show gf 12
        l "Oh... about that... please, don't worry at all."
        l "It's just that..."
        l "Uh..."
        show gf 13
        l "I've been feeling a bit sick lately, that's all."
        l "There must be... some spirit in the house tormenting me, nothing to worry about."
        show gf 14
        a "S-Some what...?"
        show gf 13
        l "Either that, or it's just my body sensing winter's coming."
        show gf 12
        l "But anyway... back to your dress... what is it for?"
        l "Any... special occasion?"
        show gf 16
        a "Oh... yeah, after we finish playing Eternum, I'm going on a date."
        a "I think it's supposed to be a fancy restaurant, so... yeah."
        show gf 12
        l "Oh... so happy for you!"
        l "Have fun with... the boy. Or girl."
        show gf 16
        a "I-I'm not sure if you know him. I met him at... the club."
        show gf 13
        l "Yeah, no... I've never been there. But I know where it is."
        show gf 16
        a "Anyway... I'll go put the E-suit back on."
        show gf 12
        l "Sure. We still have time to hunt some more Xenomorphs."
        show gf 16
        a "Y-Yeah."
        show gf 12
        l "Yeah."
        play sound2 clothes fadein 2
        scene lunaspin with dis3
        l ". . ." with dis2
        l "(She's definitely going on a date with [mc].)"
        l "(So... it's really happening. My vision was true. Again.)"
        l "(Maybe I should... say something? Perhaps that would stop it.)"
        l "(Not like the other times telling anyone ever changed anything, though.)"
        l "(Perhaps I should just... distance myself from them?)"
        l "(It'd be as simple as that.)"
        l ". . ."
        l "(Although...)"
        l "(I don't want to do that.)"
        l "(The thought of [mc] not talking to me... terrifies me.)"
        l "(And... they make me feel... happier. For the first time in my life, I can be with someone other than my dad without feeling anxious or out of place.)"
        l "(Although... {b}that{/b} sounds like a pretty extreme step.)"
        l ". . ."
        l "(But... I want to be with [mc].)"
        l "(And I... actually seemed to be enjoying myself in that vision. We all were. Which is... strange. I've almost always seen bad things.)"
        l "(Mmh.)"
        l ". . ."
        l "(Do I... do I really want to avoid it?)"
        l "(Or do I want it to happen...?)"
        l "(Am I turning into Auntie Natalia, but in reverse? She had two husbands when she was in Guadalajara.)"
        l "(And what would Dad say...?)"
        l "(He seemed pretty laid-back about that.)"
        l "(Maybe–)"
        play sound chair1
        play sound2 couch
        show gf 17
        a "Annie calling Luna..."with vpunch
        show gf 19
        l "S-Sorry, I was lost in thought."
        show gf 17
        a "Are you sure you're not hiding anything...? You're still acting weird."
        a "I feel like you're so kind that you wouldn't tell me if I was annoying you."
        show gf 19
        l "You're not annoying me!"
        l "I love spending time with you."
        show gf 17
        a "Are you suuuuure?"
        a "You don't hate me?"
        show gf 19
        l "Of course not!"
        show gf 17
        a "Reaaaaally...?"
        show gf 19
        l "Really!"
        show gf 17
        a "Swear it."
        show gf 19
        l "I don't hate you, I swear it!"
        show gf 18
        a "Mmmh..."
        l ". . ."
        a ". . ."
        l ". . ."
        show gf 19
        l "I swear on my dad's cafe."
        show gf 18
        a "Mmh."
        play sound2 couch
        play sound standup
        show gf 20
        a "*Laughs* Alright, alright! I'll take your word for it!" with dis15
        a "I tried my best to avoid annoying you. From now on, whatever happens is all on you!"
        show gf 21
        l "*Chuckles* I'll take that responsibility."
        show gf 20
        a "Alright, seriously now, I'm gonna put the E-suit back on."
    else:
        a "But alright, enough talk! Time to get back to the grind!"
        play sound2 couch
        play sound standup
        show gf 20
        a "I'm gonna put the E-suit back on!" with dis15
    a "Let's not keep [mc] waiting!"
    show gf 21
    l "Sounds good!"
    show gf 20
    a "Be right back!"
    play sound3 whoosh6
    play sound jumpscare
    play sound2 jumpscare3b
    play sound4 thunder
    play music2 horrorsound
    show gf22 with pr
    pause 0.01
    her "A-Annie... run before the spirit of El Charro Negro devours you too...{w=5}{nw}" with Dissolve(4)
    play music2 happy14
    play sound pop
    stop sound4
    scene gf 23
    a ". . ."
    play sound ["<silence 0.8>", fallfull]
    show gf 24
    bla "Annie faints and collapses to the floor."with dis12
    her "Oh my god, Annie, are you okay?!"
    l "DAD! I told you not to scare her!"
    her "I-I'm sorry, I was just trying on this costume and couldn't resist it."
    abt "Please don't devour my soul..."
    scene gf 25 with dis27
    mc "*Adjusting your clothes* I don't get why you're making me do this, bro."with dis12
    play sound clothes3
    show gf 26
    mc "It's literally just a normal sweater, I told you." with dis14
    mc "*Sighs* But anyway..."
    show gf 27
    mc ". . ." with dis
    show gf 28
    mc ". . ."
    mc "Happy?"
    c ". . ."
    mc "Chang...?"
    c "*Sobbing* My god, you're so fucking beautiful, bro."
    play sound chair4
    play sound2 couch
    show gf 29
    mc "*Laughs* Oh, fuck off."with dis12
    mc "Now you're just being sarcastic."
    show gf 30
    c "I'm deadly serious, bro."
    c "You look like a gigachad."
    show gf 29
    mc "*Chuckles* I'm literally just wearing a sweater and jeans I bought at Nordstrom."
    show gf 36
    c "Exactly!"
    c "It's straightforward yet stylish, giving off a confident vibe. It shows you're not desperate but also considerate enough to dress well for a date with someone who's been your second-best friend for so many years."
    c "If it weren’t for those bags under your eyes, you could be a model."
    show gf 33
    mc "I know, I know, I’ve been in Eternum a TON lately and I look like a college student during finals, but time is of the essence."
    mc "Once we get the 10 Gems, I’m taking at least a whole year off from any video game or... parallel dimension, I promise."
    show gf 30
    c "Hey, don’t sweat it. I already told you, it gives you a mysterious, sexy vibe."
    c "And in any case, no worries — Annie’s going to look at you with those lovey-dovey eyes of hers, so she’ll only see the good stuff."
    show gf 29
    mc "*Chuckles* If you say so..."
    mc "After three dates with Micaela you seem to be quite the expert now, huh?"
    show gf 34
    if changaskmicaelaout:
        c "Man, I still can’t believe she said yes. Each date has been more amazing than the last."
    else:
        c "Dude, I know you said not to do it yet, but you know how I get when I freak out. I ended up blurting it out in the middle of my rambling – and holy crap, I still can't believe she said yes!"
    c "I can feel the love blooming between us."
    show gf 29
    mc "Any plans to... you know... take it to the next level soon?"
    show gf 36
    c "Well, today we've got our fourth date."
    c "And if all goes as planned... Chang the Stallion might seal the deal tonight, if you catch my drift."
    c "She was giving me “the look” last time."
    show gf 29
    mc "*Chuckles* Ohhhh... make sure to tell me all about it tomorrow."
    show gf 30
    c "You bet! Wanna hang out in the evening?"
    show gf 31
    mc "Uhh... well, I'd like to, but I don’t think I’ll have time."
    mc "In the morning I’m hitting the gym with Dalia, and after that, we’re going to the Valley of the Kings server to hunt more Xenomorphs for the event."
    show gf 35
    c "Oh, I’m working at the gym tomorrow morning too. We can catch up then."
    show gf 29
    mc "Ah, really? Sweet, that sounds good."
    show gf 31
    mc "Aaaaand well, I really should get back to Andromeda now."with dis
    mc "I told Annie and Luna I’d be there at 4. And Annie and I are supposed to be at the restaurant by 7:30, so..."
    show gf 30
    c "Sure thing bro, thanks for stopping by."
    c "Go hunt those Gems down!"
    show gf 32
    mc "Well, technically we're hunting aliens now, but... yeah, the end goal is the same."
    mc "The team of four that takes down the most will get a Gem of Doom by the end of January, so we’re rolling with Nova, Luna, Annie – the ones with the highest level – and myself."
    if novaded or (anniepath and chopchop <= 2):
        mc "Or... at least they would, if not for that tiny incident..."
    show gf 30
    c "Solid team."
    c "Chang's Nine never miss."
    show gf 32
    mc "You know my offer to visit Eternum still stands, right?"
    mc "You could help us with your plans from inside, and... now that I can bring someone else into Eternum, you don’t even need the neural implant."
    show gf 33
    mc "Which... I probably shouldn’t have mentioned because it’s like top-secret stuff, so please, remember to keep it under wraps."with dis08
    show gf 35
    c "Nah, man. If the whole Eternum thing already seemed like witchcraft to me, now that you’ve confirmed it basically is, I want to try it even less."
    show gf 36
    c "Besides, you can use me as a control sample to tell reality from Eternum."with dis08
    c "If you see Chang the Maestro, it means you're in the real world."
    show gf 29
    mc "*Laughs* I like the sound of that."
    mc "Please, never leave my side. I need you to keep my feet on the ground."
    show gf 36
    c "I got your back till the end, bro."
    show gf 31
    mc "*Shaking the bottle* Welp, I've run out of beer and duty calls." with dis12
    mc "Time to get back to the grind."  
    show gf 29
    mc "Catch you later!"with dis08
    show gf 30
    c "Have fun saving the world, bro."
    c "See you later!"
    show gf 37
    mc "*Taking a deep breath* . . ." with dis14
    mct "Here you are, [mc]."
    mct "You finally know what “100%% compatibility” means."
    mct "I am part of this world."
    mct "Just as much as I am part of that one."
    mc "*Exhaling* . . ."
    play sound risingshortbb
    pause 0.7
    play sound2 spell4
    play sound3 debris
    scene gf 38 with flashfast
    pause 
    show gf 35
    c "Holy fuck..."with dis12
    c "He even took the bottle with him."
    show gf 38
    c "I’ve seen him do this three times already, and I still can’t believe it."
    c "How am I supposed to compete with this?!"
    c "I need to pick up a cool, magic ability too before Micaela dumps me for being useless..."
    c "Hmm."
    c "Maybe if I learned to do a handstand..."
    stop music2 fadeout 8
    play sound wind4 fadein 3
    scene gf 39 with Dissolve(3.5)
    pause
    play music airsiren
    queue music cosmicdreams fadein 9
    pause .8
    pas "{i}Attention, citizens of Polaxymer-83: This is the final call for evacuation."with dis2
    pas "{i}Please proceed immediately to the nearest Exit Portal or seek alternative means to depart the planet."
    pas "{i}The presence of Praetorians has been officially terminated. Be advised, this is no longer a combat-free zone."
    pas "{i}Your safety can no longer be assured."
    mc "Huh."
    mct "Another planet in Andromeda that goes down the drain because Xenomorphs have taken over."
    mct "Psh, and they have the nerve to claim they “created” this event for the players. Bullshit."
    mct "More like they need us to clean up their mess before everyone figures out they can't actually control Eternum."
    play sound footsteps3 fadein 1
    show gf 40 with dis22
    mct "This place truly is deserted now, though." with dis17
    mct "Sometimes it's easy to forget most players don't have any real combat skills."
    mct "Imagine logging into Eternum for a chill time on a non-combat server, only to get eaten by a Xenomorph... *shivers* yikes, poor people." 
    a "[mc], over here!"
    scene gf 41
    mc "Hmm?" with dis12
    show gf 42
    mc "Ah, hey there!"
    a "We're both up here, there's a ramp on the right!"
    mc "Coming!"
    show gf 43 with dis22
    mc "Hell yeah, the A-team is back!" with dis12
    $ unlock_look("annie", 12)
    $ unlock_look("luna", 11)
    $ unlock_look("luna", 12)
    show gf 44
    l "Hi, [mc]!" with dis08
    show gf 43
    mc "Good to see you, Luna!"with dis08
    play sound whistle3
    mc "*Whistles* Damn, nice outfits you got there, ladies."
    show gf 45
    a "Right? Courtesy of Luna!" with dis
    show gf 46
    l "I haven't spent much time on the Andromeda server, but I had some gear left over from when I investigated the Unitology cult near the Flar-4 System." with dis12
    show gf 47
    a "Ooohhh... we actually met their leader when the Collector invited Nova to his house in the Rockefeller server."
    if baekalive:
        a "She actually made it out alive, but she mentioned she learned a lesson from that encounter."
        a "Maybe the cult's getting reformed into something slightly better, though... I wouldn't bet on it."
    else:
        a "She got fried by the lasers though, so the cult's probably history now."
        show gf 46
        l "Good!"
        show gf 47
        a "Unless... she came back all mad and tried to reform it into something... even worse, of course."
    show gf 48b
    mc "Yeah, might as well hang on to those suits, just in case we have to deal with them again."with dis14
    show gf 48
    l "They are good for any situation. They make you immune to cold and fire, and with the helmet on, you can even survive in space or vacuum environments."
    show gf 49
    a "Ohh... that's handy."
    a "What about protection from lasers or bullets?"
    show gf 50
    mc "*Discreetly glancing down* . . ." with dis15
    mct "Sweet baby Jesus..."
    mct "These outfits sure are TIGHT. It's like they’re vacuum-sealed."
    mct "Makes them look so damn fit."
    mct "I mean, look at those curves..."
    play soundlow whoosh3b
    show gf 49
    mc "*Snapping out of it* (Alright, enough!)" with pu
    mct "You’re not a dumb, hormonal teenager anymore, [mc]. You've gotta show some character development."
    mct "You LOVE these women. This isn’t just about sex or lust — you’ve got to prove to them you’re more than just some horny pervert."
    mct "From now on, only eye contact like the man in love you are."
    a "...and they say the entire mining district is ground zero for the plague."
    show gf 48
    l "So if we don't go too far we can either take the Exit Portal back or hop on one of the spaceships at the spaceport to head to another planet, right?"
    show gf 51
    a "Well, we’ll have to use that Exit Portal over there. The spaceships are out — I've got a plan that makes them a no-go." with dis12
    l "Oh, I see it."
    mc ". . ."
    show screen mousemovebutts  
    menu:
        with dis       
        "Keep your gaze forward like a gentleman":
            hide screen mousemovebutts
            mct "Yes. YES." with dis
            mct "I did it. I hacked the system."
            mct "Fighting your demons, [mc]."
        "{sc=3}{size=46}Look at their butts{/sc}":
            hide screen mousemovebutts
            play sound6 whoosh6
            show gf 52 with pdd
            pause .2
            mct "Oh my god..." with dis2
            mct "I mean, alright, there's no need to turn into a monk either. I can look."
            mct "It’s possible to savor the sweetness of life's pleasures without losing sight of what needs to be done."
            mct "There’s nothing wrong with desire or in wanting to feel desired by the ones you love."
            mct "Nothing wrong at all..."
    play sound pop
    show gf 54
    a "Right?"
    show gf 53
    mc "E-Eh?"
    show gf 54
    a "You didn't use the neural implant to get here, right?"
    show gf 53
    mc "A-Ah, yeah, I didn't!"
    mc "I can enter servers without using it, but I still struggle with picking a specific location within them. I need to have been there before and remember exactly how it looks."
    mc "Also, when I return to the real world, I always end up at the spot where I left off."
    mc "But... yeah, no neural implant, no astral projection. Just regular old {i}real{/i} me."
    show gf 54
    a "So cool..."
    show gf 53
    mc "I also can’t travel within a server or between different ones — only from the real world to Eternum and back."
    mc "...At least for now."
    mc "Calypso said that it'd take me hundreds of years to master that power."
    show gf 56
    l "Do you think it’d be worth removing the neural implant? They've always claimed it's painless."
    show gf 55
    a "He should! The less control Ulysses has over us, the better."
    a "And maybe [mc] could even teach us how to learn that ability someday!"
    show gf 53
    mc "Eh, I'd rather not. I’m still worried about what might happen if I die while I’m in here. I... prefer not to think about it, honestly."
    mc "I wouldn't want to put you in danger."
    show gf 54
    a "When you’re up against an evil megacorporation that controls the world, there’s no place where you can stay out of danger."
    a "Plus, you can leave Eternum now without relying on the Exit Portals, which makes things safer in a way."
    show gf 53
    mc "Hmm. I suppose you have a point there."
    show gf 57
    l "I wonder where the last Gem of Doom is hidden." with dis14
    l "There’s never been one found in the Andromeda server, so maybe it’s hidden somewhere in the galaxy?"
    show gf 58
    mc "Oof, I hope not. This server is endless – if it's here, we might never find it."
    mc "And we still need to get the ones Thanatos has, somehow."
    mc "And... win the Big Hunt event. AND find the other owner."
    show gf 59
    a "What? What other owner?"with dis
    a "Thanatos has five Gems, and we have three. Then there’s the one given by The Founder as a reward for the event, and a final one that’s still hidden somewhere."
    a "That makes it ten."
    show gf 60
    mc "Oh..."
    mc "Crap, yeah, I forgot Thanatos already has five."
    show gf 59
    a "Come on, [mc], you of all people should have this clear by now!"
    show gf 60
    mc "S-Sorry, too many crazy things have been happening lately, my head's been all over the place."
    show gf 59
    a "Okay, let's do a quick test: where was the 5th Gem found, The Red Herring or Ion?"
    show gf 60
    mc "Um..."
    menu:
        with dis
        "The Red Herring":
            mc "The Red Herring."with dissolve 
        "Ion":
            mc "Ion."with dissolve 
    show gf 59
    a "Wrong!"
    a "It was a trick question, it was in Ekabar."
    show gf 60
    mc "Oh come on, that's not fair!"
    play sound whoosh6
    play soundlow musicstop
    stop music 
    scene gf61
    a "Okay, pit stop. Let’s take a quick break and go over the current Gem status to refresh your memory."with hpunch
    a "YOU CLEARLY NEED IT!"
    mc "O-Okay."
    stop music 
    play music2 quirky9 volume 0.7
    play sound pop
    show chibithana0 1
    a "Let's go back five years."
    a "Thanatos was already a pretty well known player in Eternum."
    mc "Mm-hm."
    play sound pop
    show chibigem0 1
    a "But it's when he discovered the first Gem of Doom in the Meiyo server that his popularity really took off, which, as we later found out, happened about the same time as he died in the real world."
    mc "I see..."
    play sound pop
    show chibigem00 2
    a "Almost a year later, another player found the second Gem of Doom, but Thanatos quickly tracked him down and stole it."
    play sound pop
    show chibigem000 3
    a "Following the same modus operandi, a third different player obtained a new Gem a few months later, but Thanatos stole it from them within days."
    mc "And things pretty much stayed that way until I got my neural implant."
    a "Correct!"
    scene gf 61
    show chibixet 1
    show chibigem 1
    a "Now let’s fast-forward nearly three years." with dis15
    a "A new Gem of Doom is found in the Ekabar server by the brothers Xet and Con, although Dalia and Jerry manage to pinpoint them."
    mc "True... we should give more credit to Jerry."
    play sound stab
    play sound2 punchcomic
    scene gf 61 
    show chibixet 2
    show chibithana 1
    show chibigem 2
    show chibigem2 1
    show chibigem3 1
    show chibigem4 1
    a "However, once again, Thanatos is faster. He kills Xet, steals his Gem, and disappears back into the shadows."
    mc "That makes it four."
    hide chibixet 2
    hide chibithana 1
    hide chibigem 2
    hide chibigem2 1
    hide chibigem3 1
    hide chibigem4 1
    show chibiluna 1 
    show chibiannie 1
    a "And now, the cutest spellcasters in Eternum finally make their entrance!"with dis15
    a "Annie Winters and Luna Hernandez travel to the super scary Red Herring server and complete–"
    mc "Hey, I was there too!"
    play sound whoosh6
    show chibimc 1
    show chibiluna 2
    show chibiannie 2
    a "I know, I was getting there! Just let me finish!"
    mc "Oh... *chuckles* sorry, my bad."
    scene gf 61
    show chibimc 2
    show chibiluna 3
    show chibiannie 3
    show chibigem 5
    a "LIKE I WAS SAYING, the three of us find a new Gem of Doom in the Flink mansion after completing a suuuuuper scary mission." 
    show chibiannie 4
    show chibiluna 4
    show chibimc 3
    show chibigem 6
    a "However, at that time we didn’t know Thanatos could identify the first-time owners of each Gem, so we leave [mc] alone and unprotected..."
    scene gf 61
    play sound stab
    play sound2 punchcomic
    show chibimc 4
    show chibithana 2
    show chibigem 7
    show chibigem0 2b
    show chibigem2 1b
    show chibigem3 1
    show chibigem4 1
    a "A FATAL MISTAKE. Thanatos tracks [mc] down, nearly kills him, and adds a fifth Gem to his collection!"
    mc "I've been nearly dead way too many times for being only 18..."
    scene gf 61 
    show chibigarrington 1
    show chibigem 8
    a "But this is when Chang's Nine start getting serious."with dis15
    a "We locate the 4th Gem, which, after changing hands several times for almost two years, ends up being bought by the billionaire Cornelius Garrington."
    play sound punchcomic
    scene gf 61
    show chibimc 5
    show chibigem 9
    show chibigarrington 2
    a "Thanks to Chang’s rocambolesque plan, we manage to steal the Gem from his casino right under Garrington's nose!" 
    mc "Heh, I enjoyed that one."
    scene gf 61 
    show chibiwagner 1
    show chibigem 8
    a "A short while later, we find out that another Gem is in the hands of Jasper Wagner, the leader of a well-known inter-server faction in Eternum." with dis15
    play sound punchcomic
    scene gf 61
    show chibimc 5
    show chibigem 10
    show chibigem11 1
    show chibiwagner 2
    a "Miraculously, this time we're faster than Thanatos. [mc] manages to sneak past his trenches and escape with another Gem!" 
    mc "I'm so glad I got out of there before he arrived..."
    scene gf 61
    show chibimc 6
    show chibigem 11
    show chibigem11 2
    show chibiwagner 3
    show chibiabyss 1
    a "Then, a few weeks later, El Coyote contacts us with an offer: his Gem of Doom in exchange for the legendary Heart of the Abyss."
    play sound spell4
    show chibicoyote 1
    show chibigemnew 1
    with flashfaster
    a "After a long and perilous journey through the New World waters, [mc] finally reaches the Island of the Lost Souls and encounters the enigmatic Coyote once more!" 
    play sound3 whoosh6
    show chibigemnew 2
    show chibiabyss 2
    a "Despite being initially enemies, they both honorably fulfill their part of the bargain..."
    play sound2 spell4
    hide chibicoyote 1
    hide chibiabyss 2
    with flashfaster
    a "And just like that, El Coyote vanishes as mysteriously as he arrived, leaving us with three Gems of Doom in our possession!" 
    scene gf 61
    show chibigemnew 3
    show chibigem 12
    show chibigem11 3
    show chibigem5
    show chibigem6
    show chibigem7
    show chibigem8
    show chibigem9 
    show chibithana 3 
    show chibimc 7
    a "...which sets the stage for the most epic clash Eternum has EVER seen!" 
    play sound2 zap
    show vsto
    a "Thanatos with five Gems, [mc] with three, and only two Gems left to find!" 
    a "But... oh wait, what's that?!"
    play sound whoosh6
    show chibigemf 1
    show chibifounder 1
    show chibithana 4
    show chibimc 8
    a "*Gasps* An unexpected guest appears on stage..."
    a "The gamemaster himself arrives to stir things up even more!"
    scene gf 61
    show chibigemf 2
    show chibifounder 2
    a "The Founder announces that the winner of the Big Hunt event will receive no less than the 9th Gem of Doom!" with dis15 
    show chibigemf 3
    a "Which just leaves us with that one Gem to get..." 
    show chibigemmissing 1 
    a "And the final one, still hidden somewhere we haven’t found yet!" with dis15
    a "If we can get our hands on both of these Gems, we'll be able to face Thanatos on an equal footing!"
    a "And with all 10 Gems, we might even defeat The Founder himself!"
    a "We can save Eternum!"with hpunch 
    asc "WE CAN SAVE... THE WORLD!" with hpunch
    play sound2 pop
    stop music2 
    scene gf 62
    mc "*Chuckles* Have you drawn these characters yourself?" 
    a "Me?"
    play music cosmicdreams fadein 8
    show gf 63
    a "O-Oh, well..." with dis
    a "Y-Yeah, I did."
    a "I was drawing with Nova the other day, but I'm terrible at trying to draw manga characters like she does. "
    a "Then I drew a chibi Luna and Nova said she was so cute, so I just kept going... a-and then I ended up summarizing the most important things that have happened to us."
    a "We can't all be everywhere at once, so I thought it'd be useful to keep these at the base so everyone can stay up to date with the latest events."
    a "Or at least... funnier than just plain text."
    show gf 65
    mc "*Chuckles* So that’s why you asked me to describe El Coyote the other day."
    show gf 64
    l "That's a brilliant idea!"
    l "And you draw so well!"
    show gf 65
    mc "I couldn't agree more, it's both handy and absolutely adorable."
    show gf 66
    a "T-Thank you!"
    a "I'm glad you like them!"
    a "I'll show them to Nancy later so I can–"
    stop music fadeout 3
    play soundlow alien3 fadein 2
    play soundloop wind3 fadein 7 volume 0.45
    play sound4 distantmetal
    show gf 67
    a ". . ." with dis15
    show gf 68 with dis15
    mc "*Turning around the corner* Oh shit... I think they found us." with dis12
    mc "Alright girls... I hope you're ready for this. It's showtime."
    l "The last report said this planet has over 100 Xenomorphs per square mile."
    mc "Yeah, I don't wanna do the math, but... yeah, not great."
    mc "They tend to move in herds, though, so with any luck, we’ll only have to deal with waves of 40 or 50 at a time."
    play sound footsteps3
    mc "*Moving forward* Let's try to find a–{w=1}{nw}"
    play sound bonk
    show gf 69
    mc "Ouch!" with hpunch
    mc "Son of a..."
    show gf 71
    mc "*Stepping back* What...?" with dis14
    show gf 70
    mc "What the hell is this?!" with dis12
    mc "I'm... I'm trapped in a force field!"
    show gf 72
    l "Yes, same here..."
    l "It looks like some kind of barrier."
    l "A strong one. Very powerful magic."
    show gf 71
    mc "Fuck, how can we destroy it?"
    mc "Any ideas??"
    play music2 epic3 fadein 8
    stop soundloop fadeout 13
    show gf 73
    a "It's totally impossible to destroy it unless I die or dissolve it myself!" with dis14
    a "I spent years perfecting that barrier."
    show gf 74
    mc "A-Annie...?"
    mc "W-What are you doing?"
    mc "The Xenomorphs are coming!"
    show gf 73
    a "Don't worry, nothing can break my barrier. I made sure of it."
    a "You're literally in the safest spot on the server!"
    a "I'll handle the Xenomorphs."
    show gf 74
    mc "What?! You can't do it alone!"
    mc "This is even worse than what we faced at Astrocorp's station!"
    play soundloop3 firespell fadein 4 volume 0.4
    play sound2 fire
    show gf 75
    a "I know... what you think of me."with dis14
    a "And honestly, I can't blame you."
    a "Always scared. Always set apart. Always... despised."
    a "The useless Annie."
    mc "What?"
    show gf 76
    a "They laughed at me." with dis15
    a "They dismissed me as insignificant."
    a "I had to beg just to be included on the Xenomorph hunting team, and even then, I could feel their disdain radiating from them."
    a "They questioned my worth, whispered doubts behind my back."
    a "{i}“Why her? She'll just cry and accomplish nothing.”"
    a "{i}“How's her level so high? What's she even doing here? I haven't seen her contribute anything of value since she joined.”"
    a "{i}“Why did I ever think it was a good idea to bring her to Kredon? I should have come with only Chang...”"
    show gf 78
    mc "W-Wait, wait, wait, hold on, what the hell are you talking about? Was that last one supposed to be me?!"with dis08
    mc "I've never said or thought anything like that in my life!"
    mc "No one's ever said anything like that!"
    l "That's true, Nancy and Alex even put you forward for the hunting team before you said a word!"
    show gf 77
    a "I know, I know, I'm just adding a touch of drama and theatricality to enhance my “villain speech”."
    a "Just watch and don't interrupt!"
    show gf 78
    mc "Oh... o-okay."
    l "Ohh, so cool..."
    show gf 76
    a "I was scorned. Looked down upon."with dis
    a "But all that only fueled my resolve."
    a "Today, their ridicule will become but a distant memory."
    a "Today... humankind will witness my true power."
    play sound2 fire
    play sound ["<silence 0.7>", steam2] volume 0.7
    stop soundloop3 fadeout 2
    show gf 79 with Dissolve(1.1)
    pause
    play sound3 clotheswhoosh
    play sound4 debris3
    show gf80 with hpunch
    pause 
    play sound5 alien3 fadein 2
    scene gf 81 with dis17
    mc "*Turning around* Um... Annie..." with dis12
    play sound6 alien1
    play sound7 distantmetal
    show gf 82
    bla "Several Xenomorphs start emerging from every corner of the plaza." with dis15
    mc "ANNIE..."
    show gf83
    play sound bonk
    play sound2 alien3
    play sound3 rocks
    xen "{sc=2}*Squeals* EEEEEEEEEEEEEEEEEEEEEEEEKKKKKK!!!{/sc}" with hpunchlong
    mcsc "ANNIE!!!!!!!!!!!!!!!"
    scene gf 80 with dis17
    a "*Taking a deep breath* I channel the energy swirling around me." with dis14
    a "In the metal. The water. The air."
    a "I compress it into the palm of my hand."
    a "And I release all that energy back into the surrounding space."
    play sound4 alien1
    play sound5 ["<silence 1.1>", alien3] volume 0.45
    play sound6 distantmetal
    play sound7 alien0b
    scene gf 84 
    a "This is... the core of destruction magic." with dis2
    a "This is... my ultimate spell."
    a "{i}SOLAR CATACLYSM."
    play sound risingshortbb
    scene gf84
    pause .9
    stop music2 
    stop sound4
    stop sound5
    stop sound6
    stop sound7
    play sound2 ["<silence 1.7>", annieboom] 
    show annieexplosion
    pause 12.8
    play soundloop3 wind3 fadein 8 volume 0.7
    scene gf 85 with Dissolve(4.7)
    pause
    show gf 86 with dis22
    bla "Still disoriented, you gaze into the endless expanse of barren dust, stretching for thousands of miles, unable to utter a word."with dis22
    mc "Ho..."
    mc "Holy mother of god..."
    a "Heh."
    play music sneaky5 fadein 6
    $ renpy.music.set_volume(0.2, delay=25.0, channel='soundloop3')
    show gf 87
    a "Not bad at all, huh?!" with dis14
    a "Last time I tried this, I didn't manage to get a BOOM this big!"
    a "I guess I've improved."
    mc "T-That was... INSANE."
    play sound debris
    show gf 89
    a "*Giggles* Thanks!" with dis 
    show gf 92
    l "I knew you were good at destruction magic, Annie, but... wow."
    l "This had to be... at least 10,000 or 20,000 times more powerful than the Tsar Bomba."
    show gf 88
    mc "Seriously. For a minute there, all I saw was light and all I could hear was this deafening noise."
    show gf 89
    a "*Giggles* T-Thank you, guys!"
    show gf 88
    mc "Have you been able to do THIS since we started playing?!"
    show gf 90
    a "Well... I can only cast Solar Cataclysm every now and then."
    a "It'll take me a while to gather enough mana to use it again, but we probably wiped out a few million Xenomorphs with that... so I'd say it was worth it."
    show gf 88
    mc "I-I mean, holy shit, it certainly was! There's no way we can lose the event after this!"
    show gf 89
    a "And I do know a lot of other useful spells too!"
    a "My physical abilites are practically zero, but my magic is powerful!"
    show gf 90
    a "I-I’ve wanted to show off for ages, but I kept ending up in magic-blocked servers, getting too scared to act, or just being late to everything."
    show gf 88
    mc "No one ever thought you were useless, Annie. But after this? D-Damn, even less so."
    show gf 92
    l "How are we supposed to leave the planet now, though...?"
    show gf 89
    a "I've got this covered, no worries! I set up another barrier around the Exit Portal."
    show gf 90
    a "Although... it might be a couple of miles above us. We’re actually in the middle of a massive crater, even if it doesn’t look like it."
    show gf 92
    l "Ohh... alright then, no problem."
    l "I should be able to conjure some winged creature to take us there."
    play sound slap1
    play sound7 debris3
    show gf 91
    a "Alright!" with hpunch 
    a "Looks like it's time to head out! Job's done here!"
    play sound2 whoosh6
    show gf93
    a "Bye, bye, [mc]!"
    a "Thank you for playing with us!"
    scene gf 93b
    mc "Oh, uh... y-yeah, sure!"
    mc "This was way faster than I anticipated. I guess we took the express route."
    show gf 93
    a "Yeah, I'd love to stay and play some more, but I need to go get my hair done with Luna."
    a "I really need her expert eye."
    show gf 95
    l "*Whispering* But I'm not good at these kinds of things, I told you."
    show gf 94
    a "*Whispering* Nonsense! If you can make yourself look this pretty, you're also capable of giving advice."
    a "*Whispering* Or are you going to tell me you just wake up every morning looking like that?"
    show gf 95
    l "*Whispering* Um... I suppose."
    show gf 94
    a "*Whispering* Wait, what? That's your natural skin? You're not using any foundation?"
    show gf 95
    l "*Whispering* Not really."
    show gf 94
    a "*Whispering* Really?? Wowza... so jealous."
    a "*Whispering* I need to eat more Mexican food."
    mc "So..."
    show gf 96
    a "*Clears throat* ANYWAY!" with hpunch 
    a "Yeah, so... see you..."
    show gf 97
    a "*Winks* Later at home, [mc]."
    show gf 98
    mc "*Chuckles* Alright, have fun, girls."
    mc "Still up for that Horror Movie Marathon at Kredon’s cinema next week, Luna?"
    show gf 99
    l "Definitely! I'm really looking forward to it."
    show gf 98
    mc "Sweet!"
    mc "I won't keep you any longer, then."
    mc "Take care, Luna."
    mc "And see you later {i}at home{/i}, Annie!"
    mc "Don't worry about me, I'll take the express exit back to Kredon too."
    show gf 99
    l "Take care!"
    show gf 97
    a "See ya!"
    scene gf 100 with dis2
    bla "Both girls start walking away searching for the Exit Portal, while you once again find yourself lost in the desolate wasteland Annie left behind." with dis22
    mct "Well, I've still got a couple of hours before meeting Annie at the restaurant."
    mct "Might as well continue working on my sword skills until then. Dalia will definitely notice tomorrow when we're in the Valley of the Kings server."
    mc "*Looking at the rocks around you* Hmm."
    mct "Jesus Christ, there's not a trace of those huge skyscrapers left, much less of the Xenomorphs."
    mct "I better not piss off Annie..."
    stop soundloop3 fadeout 7
    stop music fadeout 7
    scene black with dis3
    show screen afewhourslater with dis25
    pause
    $ renpy.music.set_volume(0.4, channel='music3')
    play music3 jazzbar fadein 10
    hide screen afewhourslater
    scene gh 1
    with dis3
    mct "Alright... here we are." with dis14
    mct "A plain ol' date in the real world."
    mct "A romantic dinner... the true classic."
    mct "It’ll be good for me to take a break from Eternum too. It can't hurt to have these regular reality checks to stay grounded."
    mct "Although... huh, I’m feeling... weirdly nervous."
    mct "Why...? Come on, [mc], you've met up with Annie solo a hundred times, why the jitters now?!"
    wai "One second!"
    show gh 2 with dis
    wai "Sorry for keeping you waiting!"with dis08
    wai "Good evening, and welcome to Gusteau’s!"
    eul "My name is Eulalie, and I'll be your server tonight."
    show gh 3
    mc "Nice to meet you, Eulalie."with dis12
    mc "I had a reservation at 7:30 by the name of [mc] [lastname]."
    show gh 4
    eul "Of course, Mr. [lastname], we've been expecting you." with dis
    eul "Your table is the last one on the left, just past the counter."
    show gh 5
    mc "Sweet, thank you very much."
    show gh 4
    eul "Please, don't hesitate to call me if you need anything."
    eul "I'll be right with you."
    show gh 5
    mc "Will do, thanks!"
    play sound footsteps
    scene gh 6 with dis2
    mct "Whoa, this place looks great." with dis
    mct "I had no idea Kredon had such a swanky hotel-restaurant."
    play sound chairmove
    play sound2 ["<silence 0.4>", chair2]
    show gh 7
    mct "Crap, I should've done some more research before inviting Annie."with dis12
    mct "Everyone’s dressed so fancy here."
    mct "I should’ve at least worn a shirt and blazer."
    show gh 8
    mct "Luckily, knowing her, she won't mind at all." with dis08
    mct "She’s not the type to get upset over something like this."
    play sound vibration
    play sound2 vibration
    bla "{sc=1}Your phone buzzes.{/sc}"
    show gh 8b
    mc "Hmm?" with dis
    mct "Oh, speak of the devil!"
    call chat(annie_chat2) from _call_chat_18
    mct "I know that underpass, it always floods." with dis08
    mct "If I hadn't come from Chang's, I'd be stuck there too."
    show gh 8
    mct "Welp, looks like I’ve got a few minutes to myself until Annie shows up."with dis08
    mct "Maybe I could start asking for the..."
    show gh 9
    mct "Hey... it's Raul and Noah!" 
    mct "I love how I keep running into people I know in this town."
    mct "I don't recognize their friend, though."
    stop music3 fadeout 12
    play music2 mafia fadein 10 volume 0.7
    show gh 10 with Dissolve(3.6)
    giu "Ah, Raul... you’ve got a knack for picking out just the right wine. This one’s got the same rich notes as the vintage back in Palermo." with dis17
    rau "We brought it straight from Bosnia, just for you, old friend." 
    show gh 12
    giu "However... as much as I’m savoring this, I’m here to talk business."with dis17
    show gh 11
    rau "What’s on your mind?"
    rau "Anything specific you need to discuss with me and my brother?"
    show gh 12
    giu "Don’t play the fool with me, Raul. It doesn’t suit you."
    giu "We both know why I'm here."
    giu "I’ve come to deliver one final warning."
    giu "Consider it... a gesture of respect. For all the history between our families."
    show gh 14
    rau "A last warning, he says, brother."
    show gh 15
    rau "Do you have any idea what he’s referring to?"
    rau "No, right?"
    rau "Hmm, you'll have to be more specific."
    show gh 13
    giu ". . ."
    show gh 12
    giu "For over 20 years, the seven big families have maintained a delicate balance."with dis
    giu "El Lobo Mendoza rules over South America, Hugo controls Mexico, Ivanov holds sway in Russia, Hiromi in Asia, Callahan on the East Coast..."
    giu "And finally... you’ve got the West Coast... and I got Europe AND Eternum."
    giu "It’s {i}always{/i} been this way."
    show gh 11
    rau "It started being {i}this way{/i} when Eternum was released and you assumed control of it during an extraordinary meeting where only four of the big families were present."
    show gh 12
    giu "*Sighs* It's simple, really."
    giu "Stay out of Eternum, and we won't have any issues."
    show gh 11
    rau "We never questioned your illegitimate grip on this new market, not for a second."
    rau "But let me remind you, my friend, Eternum is vast. I'm pretty sure it's big enough for the both of us."
    show gh 13
    giu "Hmph."
    show gh 12
    giu "So... is this how it's going to be?"with dis
    giu "You want to start a war? Do you really think you stand a chance with Mendoza and Callahan on my side?"
    show gh 11
    rau "We'd never start a war without provocation."
    rau "That's not how we do business."
    show gh 16
    noa "Please, let's eat first and take a moment to cool down."with dis
    noa "It'd be a shame to let the food go cold."
    show gh 12
    giu "Yeah..."
    giu "You'd be wise to listen to your brother, amico mio."
    giu "Maybe you should have heeded his advice a long time ago..."
    show gh 11
    rau "You might be right about that, old friend."
    rau "You just might be right..."
    play sound risingshort5b
    show gh13 with dis22
    pause 1.5
    show gh11b with dis22
    pause 1.5
    stop music2
    play music3 jazzbar
    stop sound
    scene gh 17
    mct "The fuck is going on over there...?"
    mct "They look tense as hell."
    eul "Hi, handsome."
    show gh 18
    mc "Hmm?" with dis
    mc "Oh, hi there."
    show gh 19
    eul "Can I get you started with a drink while you check out the menu?"
    show gh 18
    mc "Uuh... sure!"
    mc "It almost feels weird being offered alcohol at a restaurant."
    mc "I'm still getting used to this whole “legal adult” thing."
    show gh 19
    eul "Gotta thank former President Stabb for the lowered drinking age."
    show gh 18
    mc "*Chuckles* Yeah, I should probably send him a thank-you card."
    show gh 19
    eul "Can I recommend the Grand Rouge from 2008?"
    show gh 18
    mc "Depends. Will it cost me more than my student loans?"
    show gh 19
    eul "*Giggles* It's actually discounted today. It’s our cheapest wine on the menu, but also one of the best."
    show gh 18
    mc "Well, that's a hard offer to refuse, then."
    show gh 19
    eul "Excellent choice! Would you like to look at the menu too?"
    show gh 18
    mc "I checked it out online, actually. We’re going to have one of those five-course menus, but please don’t start serving until my date arrives."
    show gh 19
    eul "Of course."
    eul "If you need {i}anything{/i} to make your wait shorter, please just let me know."
    show gh 18
    mc "I will, thank you!"
    show gh 20 with dis17
    mct "Damn, service here is top-notch." with dis
    mct "We'll have to leave a good tip, I suppose. I'm still not fully used to how the tipping system works in the US either..."
    play sound vibration
    play sound2 vibration
    bla "{sc=1}Your phone buzzes.{/sc}"
    mct "Oh wow, more messages."
    mct "Feeling popular today."
    menu menurestaurant:
        with dis
        "[gr]Chang" if changaskmicaelaout and chacha1:
            $ chacha1 = False
            call chat(chang_chat2) from _call_chat_19
            if changborrowjoke:
                $ changmicaela += 1
                mc "*Snorts* (I swear, if Chang doesn't end up with Micaela I'm gonna be even more heartbroken than him.)" with dis08
            else:
                mct "I really want them to end up together, but... bro, there are limits." with dis08
                mct "That joke is way too good."
            jump menurestaurant
        "[gr]Alex" if alexpath and chacha2:
            $ chacha2 = False
            call chat(alex_chat4) from _call_chat_20
            mct "Damn, Alex has really been pushing herself lately."with dis08
            mct "Since William Bardot basically made her an outcast, she’s been juggling studying, working, and keeping up with her swimming lessons."
            mct "And all on minimum wage."
            mct "If she weren’t so stubborn and let us help her..."
            mct "I’ve got to figure out how to help her without her realizing I’m actually helping her."
            jump menurestaurant
        "[gr]Nova" if novapath and ((not chacha1 or not changaskmicaelaout) and (not chacha2 or not alexpath)):
            call chat(nova_chat4) from _call_chat_21
            if photonovatan:
                mct "Holy smokes, Nova's butt is severely underrated." with dis08
                scene gh 21 
                mct "I have to see those tan lines from the front before they disappear." with dis14
                mct "I wonder how–"
            else:
                mct "Huh, I didn’t even think about that. Entering Eternum without the implant also means all physical impacts carry over to the real world."with dis08
                mct "Interesting."
        "Put your phone away":
            if changaskmicaelaout or alexpath:
                mct "Mmmh, well, I can also reply later." with dis08
                mct "I'll just scroll through Insta and X for a bit."
            else:
                mct "Oh... it was just spam as usual..."
                mct "Well, I guess I'll just scroll through Insta and X for a bit."
            show gh 21
            mct "Heh, I love this new trending meme." with dis14
            mct "It's me for real."
    eul "*Clears throat* Ahem." 
    if photonovatan:
        play sound2 whoosh3b
        play soundlow slam3
        play sound plate
        scene gh22
        mc "AAAH!!!{w=0.17}{nw}"
        mc "NO!{w=0.17}{nw}"
        mc "WHA-{w=0.17}{nw}"
        mc "EH-?{w=0.17}{nw}"
        mc "NOT!!{w=0.17}{nw}"
        mc "NOTWHATITSEEMS!"
        scene gh 23
        mc "*Turning around* I wasn't..." with dis12
        mc "I wasn't looking at naked pictures on my phone."
        mc "I was..."
        mc "Please don’t kick me out of the restaurant."
        show gh 34
        eul "*Giggles* Don't worry, sweetheart, I won't tell the manager."
        show gh 23
        mc "I appreciate it."
    else:
        scene gh 23
        mc "*Turning around* Hmm?" with dis12
        mc "Ah, hello again!"
        mc "Is that for me?"
    show gh 34
    eul "I just brought you a little starter. Cream canapes with truffle and cucumber."
    eul "It's on the house, so don't worry about the cost."
    show gh 23
    mc "Ohh... thank you so much!"
    show gh 34
    eul "I just saw you sitting here all alone and figured you'd be hungry."
    show gh 23
    mc "I'm that easy to read, eh?"
    show gh 34
    eul "The kitchen closes in just over an hour, and my shift ends shortly after."
    eul "If you're still feeling... hungry by then, I could help you out. I know some good, cheap spots nearby."
    show gh 23
    mc "Oh..."
    menu:
        with dis
        "Flirt [red][mt]{s}(Annie Path){/s}":
            $ eulalieflirt = True
            mc "Well... I'll certainly keep it in mind."with dis
            mc "I hate being hungry."
            show gh 34
            eul "*Chuckles* I can imagine..."
            eul "You know, if you're {i}really{/i} hungry, we could even... order room service."
            eul "I've got a room here at the hotel."
            eul "We could drink some wine, play Eternum..."
            show gh 23
            mc "Sounds like a solid plan..."
            eul "Mm-hm..."
        "[gr]Reject":
            mc "Thank you, but my date must be about to arrive."with dis
            show gh 34
            eul "Yeah, sure..."
            eul "Well... if she ends up not appearing, or if... you just... change your mind... just give me a call."
            eul "Aight?"
            show gh 23
            mc "Uh... sure, thanks for the offer."
    play sound plateputdown
    show gh 35 with dis17
    bla "Eulalie sets the starter on the table and saunters out, deliberately swaying her hips with each step." with dis12
    show gh 70
    if eulalieflirt:
        mct "Wow, this woman's flirting is... direct." with dis15
        mct "I hope Annie doesn't show up when she's saying something awkward."
    else:
        mct "Okay, this woman's definitely hitting on me." with dis15
        mct "I hope Annie doesn’t show up while she’s saying something awkward and get the wrong idea."
    show gh 36
    mct "Hopefully she'll arrive soon, though. I'm starving." with dis
    mc "Hmm."
    mct "At least this little wait helped me shake off those stupid jitters I had earlier."
    mct "You said it yourself. It's just a meal with Annie, like it's been a hundred times over the past 10 years."
    mc ". . ."
    mct "Ten years..."
    mct "Man, time flies by."
    mct "Can't believe it's been that long already."
    mct "10 years and it still feels like it was yesterday."
    mc "Hmph."
    mct "Ten years..."
    stop music3 fadeout 6
    play soundloop town_ambience fadein 7 volume 0.7
    scene gh 37 with Dissolve(3.7)
    show screen tenyearsago
    mct "I remember it clear as day..." with dis15
    mc "*Snorts* Mmh."
    mct "This city sucks ass. This country sucks ass. This continent sucks ass."
    mct "And these stupid buses are crap."
    mc ". . ."
    kid "NO WAAAAY!"
    play music kidsfb fadein 5
    stop soundloop fadeout 22
    show gh 38
    mc "Hmm...?" with dis08
    show gh 39
    kid "WE HAVE THE SAME SHIRT!"
    kid "Where'd you get yours?!"
    show gh 39b
    mc "Uh... online. Probably from the same place you did."
    show gh 39
    kid "No chance, I have no money! My mom got it for me."
    show gh 39b
    mc "Oh... well, I didn't buy mine either. Nancy did."
    mc "My... nanny. She got it for my birthday."
    mc "I just told her where to buy it."
    show gh 39
    kid "Uuuhhh... so you know how to use a computer?!"
    show gh 39b
    mc "Erm... I just told her the website, but... yeah, kinda. I guess so."
    show gh 39
    kid "Whoa, cool..."
    c "I'm Chang Wong, by the way!"
    c "I'm 8 years old! Almost 9!"
    show gh 39b
    mc "Oh."
    mc "I'm... [mc]."
    hide screen tenyearsago
    play sound clotheswhoosh
    show gh 40
    c "*Punching the air* Saitama is the best!" with hpunch 
    c "He can beat bad guys with just one punch!"
    mc "...Yeah."
    c "Do you like anime too?"
    show gh 39b
    mc "Uh... yeah, I do."
    show gh 39
    c "Whoa... you're so cool..."
    c "Do you wanna be friends?"
    mc "Um..."
    play sound2 whoosh3b
    play sound3 chair3
    show gh41
    c "*Jumping over the bench* There aren’t a lot of kids around here ‘cause it’s like a business-y area." with hpunch 
    c "And... the kids at school don’t like me much either."
    c "My dad says it’s ‘cause I’m too annoying. And ‘cause I talk too much. But I think it’s ‘cause I’m too mature for my age. Or... at least that’s what my grandma says. She lives in Guangzhou!"
    scene gh 42
    c "By the way, you shouldn't be here alone, you know that?"
    c "You could be kidnapped! Or killed. Or... kidnapped and then killed!"
    show gh 43
    mc "You're alone too!"
    show gh 44
    mc "And I'm not really alone, my dad's inside this office registering our new address."with dis
    mc "We just moved here."
    show gh 45
    c "*Gasps* Wait, so you're gonna live here?!"with dis 
    c "Are you gonna come to our school?!"
    show gh 46
    mc "I guess so."
    show gh 45
    c "*Gasps* That's SO awesome!"
    c "I live here too! My parents have a hotpot restaurant just around the corner! You and Annie should totally come someday!"
    show gh 46
    mc "Who's Annie?"
    show gh 45
    c "Annie from school!"
    show gh 46
    mc "Oh... I don't know her. I just arrived here."
    show gh 42
    c "Oh... really? And then why is she here?"
    show gh 46
    mc "Wha–"
    show gh 47
    mc ". . ." with dis15
    show gh 47b
    mc "O-Oh..." with dis12
    mc "Hi."
    mc "Are you Annie?"
    a ". . ."
    mc ". . ."
    mc "*Whispering* Why isn't she talking...?"
    show gh 49
    c "*Whispering* I know her from school, but she never talks there either."
    c "*Whispering* I think she's mute."
    show gh 48
    a "I can speak!"
    show gh 47b
    c "*Gasps* She can speak!"
    show gh 48
    a "I'm just... shy."
    a "I heard you talking earlier."
    a "I go to school with Chang. I'm Annie."
    show gh 47b
    mc "Hi Annie. I'm [mc]."
    show gh 48
    a "Hi [mc]."
    a "D-Did you..."
    a "Did you move here?"
    show gh 47b
    mc "Yep! From the US, with my dad."
    show gh 48
    a "Cool..."
    show gh 49
    c "You shouldn't be out here alone either, Annie."
    c "You could be kidnapped. Or kidnapped and then sold."
    show gh 50
    a "I'm not alone, my dad's over there."
    show gh 51
    a "He's a businessman. He's doing business calls now."
    mc "Ohh..."
    a "We were gonna see the pandas at the zoo, but... he got a call. So I guess we’re not going anymore."
    c "Oh... I see."
    show gh 48
    a "I like your... h-hair, American boy."
    a "And your shirt."
    show gh 47b
    mc "Thanks!"
    show gh 56
    c "OHHH, YOU LIKE ANIME TOO?!"
    show gh 52
    a "N-Not really. I mean... my mom doesn't let me watch it."
    a "She says those Japanese cartoons aren't for kids."
    show gh 53
    mc "Oh... too bad."
    show gh 56
    c "No problem! Do you wanna play with us?! Let's meet at school tomorrow at lunch and pretend to be something we all know!"
    c "How about... Spiderman?!"
    show gh 52
    a "My mom says superhero movies are too violent."
    show gh 54
    a "But I like Minions! And Frozen!"with dis08
    show gh 49
    c "Uh... I haven't seen that."
    c "How about... Harry Potter?"
    show gh 48
    a "Haven't seen it. My mom says witchcraft is the devil's work."
    show gh 49
    c "SpongeBob?"
    show gh 48
    a "No."
    show gh 49
    c "Adventure Time? Pokemon? Transformers?"
    show gh 48
    a "Sorry."
    show gh 49
    c "Eh... Star Wars?"
    show gh 48
    a "I haven't–"
    show gh 54
    a "Wait... yes! I saw it at my uncle's house!" with dis06
    a "They were super old movies!"
    show gh 56
    c "Oh, NICE! Let's play that!"
    play sound pop
    play sound2 whoosh6
    show gh 57
    mc "I wanna be Luke!"with pl
    play sound pop
    play sound2 whoosh6
    show gh 54
    a "I wanna be Vader!"with pl
    play sound pop
    play sound2 whoosh6
    show gh 56
    c "I wanna be–" with pr 
    show gh 58
    c "Wait, what? No! I wanna be Vader!"with dis06
    c "You have to be Princess Leia!"
    show gh 59
    a "I don't wanna be Leia, she was so boring."
    a "I wanna be Vader and make everyone go “whoa, she's so strong!”"
    show gh 58
    c "Agh... okay, I'll be Leia."
    show gh 54
    a "Thanks!"
    show gh 60
    c "Alright, so here's the game!"
    c "I have some sticks we can use as lightsabers."
    c "I can put them in my bag and–"
    play sound whoosh6
    play sound2 slam3
    play sound3 leather
    show gh61
    cmom "{sc=2}{size=40}{font=chinafont.ttf}王常！ 你个小兔崽子，说了让你赶紧买完菜回饭店！！！{/sc}"with vpunch 
    cmom "{sc=2}{size=40}{font=chinafont.ttf}你在这坐着干嘛？！{/sc}"with hpunch
    scene gh 62
    c "{sc=2}{size=40}{font=chinafont.ttf}我马上就去！ 我正跟我的朋友说再见呢！！！！{/sc}" with hpunch 
    play sound rubbody
    show gh 63 with dis12
    c "Sorry friends, I gotta go back with my mom now!" with dis12
    c "I'll continue later!"
    show gh 64
    cmom "Yeah, sorry, guys, but Chang’s gotta head out."
    cmom "You can hang out with him all you want after school..."
    show gh 65
    cmom "...as long as he finishes his homework first."
    show gh 63
    c "I'll have them done tomorrow! Promised!"
    c "Don't miss me too much!"
    show gh 54
    a "Yeah, I should go before my dad gets mad too." with dis2
    a "Will you... will you be at school tomorrow?"
    show gh 55
    mc "I will!"
    show gh 54
    a "You sure...?"
    show gh 55
    mc "Yeah!"
    show gh 54
    a "You won't ignore me there...?"
    show gh 55
    mc "Of course not. Why would I...?"
    show gh 66
    a "Pinky promise!"with dis 
    mc "What...? What for?"
    a "Promise me we'll be friends!"
    mc "Um..."
    show gh 67
    mc "Yeah, sure. Pinky promise." with dis
    mc "Friends."
    a "Friends forever!"
    show gh 54
    a "Okay!" with dis12
    a "I'll leave now!"
    a "See you tomorrow... [mc]!"
    show gh 55
    mc "See ya!"
    show gh 38
    mc ". . ." with dis2
    mct "They said there weren’t many kids around here, but it seems like it’s full of weird ones."
    mc ". . ."
    play soundlow wood2 volume 0.5
    show gh 68 
    mc "*Swinging your legs* (Maybe it won't suck ass so much after all.)" with dis15
    $ renpy.music.set_volume(0.15, channel='music3')
    stop music fadeout 8
    play music3 jazzbar fadein 6
    scene gh 69 with Dissolve(3.4)
    mc "*Chuckles* Hmm." with dis2
    mct "The day after, we spent the entire afternoon playing together."
    mct "Sometimes, it feels like we're still those kids deep down."
    play sound annierunrest
    stop music3 fadeout 2
    show gh 70
    wai "Hey, hey!" with dis 
    wai "Excuse me, miss, do you have a reservation??" 
    play music2 annielove fadein 4
    show annierestaurant with dis2
    pause 2
    a "{bt=2}*Panting* Aaahh... ahh... aahh... ahh...{w=7.3}{nw}{/bt}" with dis3
    $ unlock_look("annie", 13)
    play soundlow rubbody
    scene gh 71
    a "*Panting* I..." with dis14
    a "*Panting* I-I'm so sorry!"
    a "*Panting* I ran as f-fast as I could, I swear!"
    show gh 72
    mc "But we're definitely not those kids anymore..."
    mc "Wow..."
    show gh 73
    a "What...?"with dis06
    show gh 74
    mc "*Chuckles* Nothing."
    mc "Just thinking."
    show gh 71
    a "I-It's not my fault!" with dis06
    a "That stupid bus took a ridiculous detour, so I decided to walk, b-but I couldn't move fast with these heels, and I was so scared I’d trip and get my hair all messed up, and–"
    show gh 72
    mc "Hey, hey! I haven't even been here that long!"
    mc "No problemo!"
    show gh 71
    a "You sure...?"
    a "But the kitchen closes in just one hour!"
    show gh 72
    mc "Then we'll just have to eat faster!"
    mc "You're here now... and you look absolutely stunning. That's all that matters."
    mc "You've never been more beautiful, Annie."
    show gh 75
    a "Oh... r-really? Do you like the dress?" with dis15
    a "It's... it's new!"
    a "I bought it yesterday."
    a "Along with the shoes, the necklace, and... a new perfume."
    show gh 76
    mc "Everything's perfect."
    mc "All of you."
    show gh 75
    a "Phew... thank goodness."
    a "I was afraid the rain would mess something up."
    a "Or that... I'd be too late and you'd have left already."
    show gh 76
    mc "*Chuckles* As if I could do that. I'd wait all night for you if I had to."
    mc "I’d even ask you to stay standing all night just so I could keep admiring you, but I bet you’re tired."
    mc "Good thing I saved you the best seat in the restaurant!"
    mc "*Pointing at the seat in front of you* M'lady, please..."
    play sound clothes3
    play soundlow ["<silence 1.3>", chair3] volume 0.6
    show gh 77
    bla "Annie sits in front of you with a radiant smile. Her new perfume wafts through the air, captivating your senses." with dis15
    show gh 79
    a "Whew... I was also worried I might be overdressed, but thankfully, there are other women in dresses too."
    show gh 77
    mc "If anything, I’m the one underdressed tonight... sorry about that."
    mc "Next time, I'm gonna show up in a suit, I swear."
    show gh 78
    a "Nah, you look great."
    a "Honestly, you look... perfect."
    show gh 77
    mc "Even the hair?"
    show gh 78
    a "*Giggles* Of course! That messy fringe is just so you."
    show gh 77
    mc "*Chuckles* Thank you for the reassurance."
    mc "And speaking of hair, what did you do to yours?!"
    mc "I knew you were growing it out, but wow!"
    show gh 80
    a "Oh... I didn't do anything too fancy, really." with dis12
    a "I just teased the roots a bit and used a lot of hairspray to... you know, add some volume."
    show gh 81
    mc "You're gonna have to give me the brand of that hairspray."
    show gh 80
    a "Sure thing! It's one Penelope recommended me."
    show gh 81
    mc "*Chuckles* Ah, of course, who else but our personal stylist."
    play soundlow clothes3
    play sound clothes3
    show gh 82
    a "So... tell me, what did you do while you were waiting for me here?" with dis14
    a "*Giggles* Besides, you know, drowning in sadness and yearning, of course."
    show gh 83
    mc "Well, I had some wine, replied to a few messages, and just checked out the place."
    mc "Raul and Noah are here too! But they’re with someone I don’t know, so I figured it’d be best not to interrupt."
    show gh 84
    a "Uhh... you were busy, busy!"
    a "Looks like you don't need me to keep you entertained."
    show gh 85
    mc "Actually, just before you got here, I was reminiscing about the day I met you and Chang."
    show gh 82
    a "Ohh... I'm surprised you still remember that."
    show gh 83
    mc "By all means! When I moved to London, I felt like my life was falling apart. You and Chang turned everything around for me."
    mc "I remember every detail of that day."
    show gh 84
    a "Every detail, huh...? Let me check that!"
    a "What was I wearing?"
    show gh 85
    menu:
        with dis
        "Denim overalls over a rainbow-striped t-shirt":
            mc "Denim overalls over a rainbow-striped t-shirt." with dis06
        "A pink hoodie paired with leggings":
            mc "A pink hoodie paired with leggings." with dis06
        "[gr]An orange shirt tucked into a skirt with suspenders":
            mc "An orange shirt tucked into a skirt with suspenders." with dis06    
            show gh 84
            a "And where was I going that day with my dad?"
            show gh 85
            menu:
                with dis
                "To the movie theater":
                    mc "To the movie theater." with dis06
                "To see the pandas at the zoo [annie_pts]":
                    mc "To see the pandas at the zoo." with dis06
                    mc "Although... you had to cancel those plans."
                    $ annie_points += 1
                    play sound beat
                    show screen heartbeat
                    show gh 82
                    a "Wooooooow... impressive memory!"with dis
                    show gh 83
                    mc "Naturally."
                    mc "Unlike you, I’ve got a special place in my mind where I treasure every second I spend with you."
                    show gh 84
                    a "What do you mean, “unlike me”?!"  
                    jump rememberdinnersuccess                
                "To play mini golf":
                    mc "To play mini golf." with dis06
    show gh 84
    a "Wrong!"
    a "SO wrong! *Chuckles* You said that so confidently that you almost made me doubt myself!"
    show gh 85
    mc "*Chuckles* In my defense, it was so long ago that no one would remember the details."
    show gh 84
label rememberdinnersuccess:
    a "I remember EVERY moment we've spent together!"
    show gh 85
    mc "Oh, is that so...?"
    mc "Alright, tell me about the first birthday we celebrated together, a couple of years after that."
    play soundlow clothes3
    play sound clothes3
    show gh 78
    a "Sure!" with dis14
    a "We couldn’t celebrate your birthday because you were sick, so we decided to do a joint birthday celebration three weeks later at Chang’s parents' restaurant."
    show gh 79
    a "I was already secretly saving up every cent to play Eternum, so we agreed not to give gifts."
    show gh 78
    a "But you still got me a blue stuffed hippo for my collection."
    show gh 79
    a "And then... Chang slipped while carrying the cake, so we ended up blowing out the candles on a pile of cream and pie."
    show gh 77
    mc "Wow!"
    mc "*Chuckles* Alright, I stand corrected. Your memory is undisputed."
    show gh 78
    a "I told you!"
    show gh 77
    mc "What did you wish that day?"
    show gh 79
    a "No way I'm telling you!"
    a "It was so stupid, you'd laugh at me."
    show gh 77
    mc "Come on! It's been 8 years since then!"
    mc "I promise I won't laugh."
    play sound clothes3
    play soundlow clothes3
    show gh 82
    a "You suuure...?" with dis14
    show gh 83
    mc "I promise!"
    show gh 82
    a "Well... okay then."
    a "I wished..."
    a "I wished we could be together forever."
    show gh 83
    mc "*Laughs*"
    show gh 84
    a "Hey! You said you wouldn't laugh at it!"
    show gh 85
    mc "Sorry, it's just funny..."
    mc "That was my wish, too."
    show gh 86
    a ". . ." with dis
    play sound clothes3
    play soundlow clothes3
    show gh 80
    a "D-Darn it, [mc]." with dis14
    a "Why do you always know exactly what to say and how to say it?!"
    a "Gosh, I don't even care if it's not true."
    a "That was just... so romantic."
    show gh 81
    mc "*Chuckle* It is true!"
    if eulalieflirt:
        eul "Hi handsome..."
    else:
        eul "Hello again!"
    show gh 87
    eul "These are the two first dishes of the five-course menu." with dis12
    eul "Tender beef and shrimp marinated in tangy citrus sauce, and herb-crusted grilled tuna steak. Bon appetit!"
    show gh 88
    mc "Oh, sweet! I'm so hungry."
    if not eulalieflirt:
        a "That smells so good!"
    show gh 87
    eul "Just a reminder, the restaurant closes in less than an hour, though the hotel is still open."
    if eulalieflirt:
        show gh 133
        mc "Yeah, we're aware, no worries."
        show gh 132
        eul "So if you're still up for that Eternum session we talked about earlier..."
        show gh 133
        mc "O-Oh... *nervous laugh* I'll think about it, thanks."
        show gh 132
        eul "*Giggles* Sure..."
        a ". . ."
        show gh 130 with dis2
        mc "*Clears throat* I d-don't know what she was talking about." with dis14
        mc "She's a weird woman."
        show gh 131
        a "Really? Because she knew you play Eternum."
        show gh 130
        mc "Duh... who doesn't nowadays?"
        mc "Remember that for most people Eternum is still just their everyday entertainment – it's normal to ask."
        mc "We’re the ones who made it a world-changing thing, for better or worse."
        a "Mmh."
        show gh 131
        a "Yeah... I suppose so."
        show gh 130
        mc "Anyway... let's eat! I'm starving!"
        show gh 131
        a "Yes! I'm also very hungry."
        show gh 130
        mc "Cheers!"
        jump posdinnerannie
    show gh 88
    mc "Yeah, we're aware, no worries."
    play sound plateputdown
    show gh 89 with dis12
    eul "So, if you’re still hungry after dinner..." with dis
    eul "The special offer we talked about earlier still stands, [mc]..."
    show gh 90
    mc "Sure, thank you very mu–" with dis12
    show gh 91
    mc "W-Wait, what special offer...?"with dis
    mc "We didn't talk about anything!"
    mc "H-Hey!"
    play sound tablehit
    show gh 92
    mc "WE DIDN'T TALK ABOUT ANYTHING!"with hpunch
    mc "T-This woman just started flirting with me out of the blue! I didn't do anything!"
    mc "S-She just wants to ruin my date or something!"
    mc "FUCKING BITCH!"
    show gh 93
    a "*Giggles* I know, don't worry."
    show gh 92
    mc "E-Eh?"
    mc "You know...?"
    show gh 93
    a "After all these years, I think I can read you pretty well."
    a "Just from how you reacted, I can tell you’re being honest."
    a "Not to mention, I know you’re a kind person. At least to me!"
    a "Agreeing to meet someone else tonight {i}during{/i} our date would be... *giggles* well, pretty messed up."
    show gh 92
    mc "Oh, thank god. I was worried you'd get all jealous or irrational."
    show gh 93
    a "Tonight, I just want to focus on us. You, me, and a delicious dinner – nothing else matters."
    show gh 92
    mc "You just read my mind!"
    mc "I'm so glad we're on the same page."
    show gh 93
    a "Can I ask you something before we start eating, though?"
    show gh 92
    mc "Absolutely! I'm all yours tonight."
    mc "Ask away."
    show gh 93
    a "Uhh... that's a generous offer!"
    show gh 94
    a "Mmmmmh..."
    show gh 93
    a "Okay, I have a fun one!"
    show gh 92
    mc "Shoot!"
    play sound lightstage
    play sound2 impact3
    stop music2
    scene gh 95
    a "What do you like most about me?"
    play music millionaire fadein 8
    play sound3 lightstage
    play sound4 impact3
    show gh 96
    mc ". . ."
    show gh 95b
    mc "W-What do you mean, “what do I like most”...?" with dis12
    show gh 95
    a "It's a pretty straightforward question, I think."
    a "What do you like about me."
    a "Very simple."
    show gh 95b
    mc "A-Ahh... yes. Of course."
    mc "Um..."
    show mcshakemillion
    mc ". . ." with dis2
    mc "*Gulps* (Alright, [mc], this is one of those trap questions.)"
    mct "I've seen this on social media before."
    mct "But not everything is lost yet. You just need to play your cards right."
    mct "Your answer could shape how the rest of tonight goes and... maybe even your relationship with Annie."
    play sound3 impact3
    mod "Try not answering in time ;) (-1 Annie point for that or Butt)"
    call screen millionairescreen with dis22
label millioncontinue:
    play sound impact3
    play sound2 impact
    scene gh 95b with dis2
    mc "Um..." with dis15
    if millionqeyes:
        mc "Your... eyes."
        mc "I could... get lost in them forever."
        a ". . ."
        show gh 95
        a "So... you don't like my personality? Just my looks?"
    elif millionqbutt:
        mc "Your... butt."
        mc "It's like... so slappable. Big fan."
        a ". . ."
    elif millionqpersonality:
        mc "Your... personality."
        mc "Being around you is just... always fun."
        a ". . ."
        show gh 95
        a "So... you don't think I'm attractive? You just like my personality...?"
    elif millionqyes:
        mc "Y-Yes."
        a ". . ."
        show gh 95
        a "Yes... what?"
        a "You don't have a favorite part because everything’s equally awful?"
    else:
        mc "Eyes, butt... the personality of your... butt. And the eyes. Yes."
        a ". . ."
    if millionqyes or millionqpersonality or millionqeyes:
        show gh 95b
        mc "W-What? No! I just..."
        mc "U-Uhh..."
        play sound pop
        stop music
        play music3 jazzbar
        show gh 93
        a "*Laughs* Okay, I can’t keep a straight face anymore!"
        a "I’m just messing with you!"
        a "You should see how much you're sweating right now."
        show gh 92
        mc "Oh, thank fucking god..."
        show gh 93
        a "Good answer, though!"
        a "I approve."
        show gh 92
        mc "*Chuckles* Thank goodness."
    else:
        play sound pop
        stop music
        play music3 jazzbar
        show gh 98
        a "What...?"
        a "My butt, seriously?"
        show gh 99
        mc "No! I mean..."
        show gh 98
        a "*Grumbling* You're lucky I was just messing with you."
        $ annie_points -= 1
        a "But terrible answer! You're killing the romantic vibes!"
        show gh 99
        mc "S-Sorry, I got nervous."
    play sound clothes3
    show gh 100
    a "Alright, enough chit-chat!" with dis12
    a "I don't know about you, but I'm SOOO hungry and this looks delicious!"
    show gh 101
    mc "Yeah, if we’ve only got an hour to finish, we’d better dig in!"
    mc "And cheers!"
label posdinnerannie:
    play sound clink
    show gh102 
    if eulalieflirt:
        stop music2 fadeout 8
        play music3 jazzbar fadein 7
        bla "You and Annie continue savoring the dinner, but even if the food is fine, there are awkward pauses between the laughs, making the evening turn out to be more uncomfortable than you anticipated." with dis3
    else:
        bla "You and Annie continue savoring the dinner, filled with laughter and shared memories. As you indulge in the food and drinks, the evening ends up feeling warmer and more intimate than what you could have expected." with dis3
    play sound clothes3
    scene gh 104
    a "Oof, I'm so full..."with dis22
    if not eulalieflirt:
        a "I feel like my belly's gonna explode if I take one more bite!" 
    else:
        a "I can't take another bite."
    show gh 105
    mc "*Laughs* You always say you're “sooo hungry”, and then you get full in no time."
    mc "I had to finish half of your dishes!"
    show gh 104
    if eulalieflirt:
        a "Yeah, I guess I am like that... sorry 'bout it."
        show gh 105
    else:
        a "It's not my fault! I'm small, so my belly's smaller too!"
        a "I swear I can't eat another bite."
        show gh 105
        mc "*Chuckles* Alright, fair enough."
    mc "Too bad we don't have time for dessert, I would've loved to try the cheesecake."
    if eulalieflirt:
        show gh 104
        a "True... too bad."
        show gh 105
        mc "Yeeah..."
    else:
        show gh 106
        a "Ooooh... for dessert, I could’ve found a little tiny bit of space in my stomach."
        show gh 105
        mc "Right? Maybe we can find some other place that's still open..."
    show gh 107
    eul "Hi guys, we're closing the restaurant now." with dis12
    eul "You can pay at the front desk."
    show gh 108
    mc "Sounds good, thanks."
    show gh 107
    eul "Oh, and just so you know, it's... 307."
    show gh 108
    mc "$307?! W-WHAT?!"
    mc "How expensive was that wine?!"
    show gh 107
    eul "*Giggles* No, not the dinner... remember, this is a hotel-restaurant."
    show gh 108
    mc "Huh?"
    show gh 107
    eul "Anyway, I've gotta get back to cleaning up."
    eul "If you'll excuse me..."
    show gh 109 with dis17
    mc "What...?" with dis12
    mc "The fuck is she talking about?"
    mc "I seriously don't get this woman. She's so weird."
    if eulalieflirt:
        show gh 105
        mc "Do you know what's she talking about?"
        show gh 104
        a "Nope. No idea."
        play sound clothes3
        show gh 134
        a "*Standing up* Anyway, time to go!" with dis15
        show gh 125
        mc "Hey, I was thinking..."
        mc "Do you wanna go to the park for a walk? It's not raining now."
        show gh 134
        a "Not really, I wanna go home."
        a "I'm so tired."
        show gh 125
        mc "Oh... alright."
        mc ". . ."
        play sound chairmove
        show gh 135
        mc "*Standing up* Are you alright, Annie?" with dis12
        mc "You've been so distant during the whole dinner."
        show gh 137
        a "I'm okay."
        show gh 135
        mc "No, you're not!"
        mc "Please, just tell me what's wrong!"
        a ". . ."
        show gh 138
        a "I don't wanna talk about it." with dis12
        a "I'm fine, I just want to go home."
        show gh 139
        mc "But what happened?!"
        mc "Is it because of that waitress?! Seriously??"
        show gh 138
        a "Look, [mc]..."
        a "Maybe you all think I'm an idiot, but I'm really not."
        show gh 139
        mc "What?! No one thinks that."
        a ". . ."
        show gh 138
        a "I know our situation is... rather... unconventional."
        a "Nancy, Penny, Dalia, Luna, Alex, Nova..."
        a "I see how they look at you."
        show gh 139
        if harempath:
            mc "W-What...?"
            mc "I was gonna..."
            mc "I mean... Nancy told me..."
        else:
            mc "WHAT?! Now you're just making things up."
        show gh 138
        a "I thought... I thought it was all because of this crazy and chaotic situation that brought us together."
        a "And I thought you could give me at least one night, entirely for me."
        a "I thought I was special to you. That we all were."
        a "But... I guess we're all just... “one more”."
        a "I guess... I was wrong. About so many things."
        show gh 139
        mc "What...? I swear I'm not following you, Annie."
        a ". . ."
        show gh 137
        a "...I'm just tired, I told you."with dis12
        a "I'm sorry."
        show gh 135
        mc "We can talk about this."
        show gh 137
        a "I really appreciate the dinner. It was wonderful."
        a "But I'm exhausted. I need to go home and rest."
        show gh 135
        mc "But..."
        mc "*Sighs* Okay..."
        mct "Fuck... I ruined the date."
        mct "Well, at least she's not crying or anything."
        mct "So that's good."
        mct "Right...?"
        mc "Okay, let's go."
        a ". . ."
        $ anniepath = False
        $ annieu = False
        $ harempath = False
        jump arabiadayletsgo
    show gh 106
    a "I think that was her room number."with dis
    show gh 105
    mc "Uh?"
    show gh 106
    a "307 - it's her room number at the hotel."
    show gh 105
    mc "Ohhh..."
    mc "Ugh, this woman is really getting on my nerves. Why is she trying to sabotage our date?!"
    mc "I’m sorry, Annie. I swear I didn't–"
    show gh 106
    a "Please, don't worry about it, I already told you that I don't mind."
    a "I’m not going to let something like this ruin my perfect night."
    show gh 105
    mc "Whoa..."
    mc "I'm so impressed, Annie."
    mc "You're coming across so mature tonight."
    show gh 106
    a "Well, we're not kids anymore, are we?"
    show gh 105
    mc "Definitely not..."
    mc "Alright then! Ready to head out?"
    show gh 106
    a "Sure!"
    a "Do you mind if I go to the bathroom before we go?"
    show gh 105
    mc "Not at all, I'll wait here."
    mc "Just don’t try to sneak off and pay the check while you’re at it."
    mc "It’s my treat tonight. I’ve still got a ways to go before I can repay you for that initial eternals donation from my first day in Eternum."
    show gh 106
    a "*Giggles* Alright, I promise I won't!"
    a "Be right back!"
    play sound clothes3
    show gh 110 with dis2
    mct "Ahhh... tonight has been perfect so far." with dis15
    mct "Annie really deserved a romantic date like this. I know she loves these kinds of moments."
    mc "*Looking through the window* Hmm..."
    mct "It doesn't look like it's raining now."
    mct "I wonder if we could take a walk at the park before heading home..."
    show gh 111 with dis25
    eul "Can you cover me tomorrow evening, Mary?" with dis15
    show gh 112
    wai2 "Again?"
    show gh 111
    eul "*Whispering* I got a rich one!"
    eul "*Whispering* He has a Bentley!"
    show gh 112
    wai2 "*Sighs* Fine, but you owe me 2 days already."
    show gh 111
    eul "Thank you, Cupcake."
    a "Excuse me."
    scene gh 113
    eul "Hmm?" with dis14
    show gh 114
    eul "Oh... it's you." with dis14
    eul "The bathroom's right at the end of the hall, on the left."
    show gh 116
    a "Nah, I'm good." with dis14
    show gh 115
    eul "Oh." 
    eul "Then I'm sorry, I can't help you – we're closing up now."
    eul "No more food or drinks here, but the hotel bar's open till 3AM if you need something."
    show gh 116
    a "Actually, I just wanted to ask something."
    show gh 115
    eul "Oh... sure, go ahead."
    eul "But please, make it quick. I don't ha–"
    play sound whoosh6
    play sound2 musicstop
    play sound3 punch
    play sound4 slam3
    play sound5 debris3
    stop music3
    play music anniehorror
    show gh115b
    a "Am I invisible?" with hpunch 
    scene gh 126
    eul "I-I-I'm sorry...?"
    show gh 117
    a "I asked if I'm invisible."
    show gh 126
    eul "W-What?"
    show gh 117
    a "Do I have to repeat myself...?"
    show gh 126
    eul "N-No, no! You're not invisible!"
    scene gh 118
    a "Then why the hell did you continue flirting with him right in front of me, Eulalie?" with dis14
    a "This was supposed to be the perfect day I've dreamed about for years, and you ALMOST RUINED IT."
    a "You certainly tried really hard to."
    show gh 126
    eul "I-I'm sorry!"
    eul "I-I just... I was just playing around, that's all!"
    show gh 117
    a "Playing around?"
    show gh 126
    eul "I just thought he was cute and I... I was just playing!"
    eul "That's it! NOTHING PERSONAL!"
    show gh 118
    a "Do you think I don't see he's cute?"
    if harempath:
        a "You think I don't see all the other girls eyeing him...? You think I don't notice the glances? The way they look at him?"
    a "DO YOU THINK I'M AN IDIOT, EULALIE?"
    show gh 126
    eul "I don't!"
    if harempath:
        show gh 117
        a "Here's the thing, Eulalie..."
        a "Dalia, Penny, Nancy, Luna, Nova, Alex..."
        a "I like them, Eulalie. A lot."
        show gh 118
        asc "BUT {w=0.2}{size=35}I {w=0.2}{size=45}DON'T {w=0.2}{size=55}LIKE {w=0.2}{size=70}YOU."
        a "Do you see the difference, Eulalie?"
    else:
        show gh 118
        a "Do you realize how incredibly rude it is to flirt with someone when their date is right there, Eulalie?"
    show gh 126
    eul "I-I do! I see it!"
    show gh 118
    a "If I ever catch you even LOOKING at him again... it'll be the last thing you ever do in your miserable life."   
    a "The. Fucking. LAST. One."
    a "Am I being clear enough..."
    asc "{size=67}...EULALIE?"     
    show gh 126
    eul "Y-YES!"
    eul "Crystal clear!"
    eul "I'll never do it again, I swear! Not with him, and not with anyone else!"
    show gh 117
    a "Good."
    a "Now get out of my sight."
    show gh 126
    eul "Y-Yes!"
    play sound run
    show gh 127 with dis15
    pause
    a ". . ." with dis
    a "*Clears throat* Hrrm."
    play sound whoosh6
    play soundlow debris3
    stop music
    play music3 jazzbar fadein 4
    show gh 128 with pl
    a "*Breathing rapidly* (OH MY GOD.)" with dis2
    a "*Breathing rapidly* (I can't believe I actually managed to pull that off.)"
    a "*Breathing rapidly* (But, well...)"
    show gh 129
    a "(Cheese and crackers, you did it, girl!)" with dis 
    a "(For once, I was the one being scary and not the one being scared! Luna's tips actually worked!)"
    a "*Giggles* (Maybe I should wear heels more often... they really boost my self-confidence.)"
    a "(It really feels amazing to be confident. Why don’t more people do this?)"
    stop music3 fadeout 12
    play music2 mafia fadein 10 volume 0.7
    show gh 12 with Dissolve(3.6)
    giu "Un pasto squisito, amico mio. Truly." with dis17
    giu "However... I'm afraid I have to be on my way."
    show gh 121
    rau "Yes... let's get out of here."
    rau "These folks have earned their peace for the night."
    show gh 12
    giu "I'm genuinely sorry we couldn't come to a mutual understanding tonight, my friend."
    giu "I really am..."
    show gh 121
    rau "Well... at least we had the chance to reminisce a bit about the old days."
    rau "That’s always worth getting together for."
    rau "And you got to meet my brother, so–"
    show gh 119
    giu "Oh, I already knew Noah, fear not."
    show gh 15
    rau "*Looking at his brother* Huh...?" with dis12
    rau "I wasn't aware of that. He never... mentioned it to me."
    show gh 16
    noa "I didn’t think it was important."
    noa "We only had a brief encounter in New York last April when I went to visit Callahan."
    noa "We barely exchanged any words."
    show gh 119
    giu "Yeah..."
    giu "You know your brother is not much of a talker, although... even in that short time, it was clear how sharp he really is."
    play sound chairmove
    show gh 120
    giu "But anyway, my flight is in an hour, and I don’t want to keep you any longer." with dis12
    giu "Until we meet again, my friend."
    show gh 122
    bla "Raul watches quietly as Giuseppe leaves the restaurant, not casting a single glance back." with dis22
    rau ". . ."
    show gh 123
    rau "*Sighs* Aaahhh..." with dis08
    rau "I'm afraid he's right, Noah."
    rau "I really don't know if we can win this war."
    rau "But... at this point, avoiding it isn’t an option."
    show gh 15
    rau "At least I know I can count on you, brother."with dis12
    rau "Even when everything seems to be falling apart... I know I'll always have you by my side to face it together."
    noa "Mmh."
    play sound risingshort5b
    show gh124
    noa ". . . .{w=7.2}{nw}" with dis3
    stop music2
    play music3 jazzbar
    stop sound
    scene gh 17
    mc ". . ."
    a "I'm ready!"
    show gh 125
    mc "*Turning around* Nice! Let's..." with dis12
    mct "God, I still can't get over how beautiful she looks tonight."
    a "Hmm?"
    mc "*Chuckle* Yeah, sorry."
    mc "Let's go!"
    stop music3 fadeout 7
    scene ga 1 with dis3
    play soundlow thunder fadein 3
    pause 1
    play music2 ["<silence 7>"]
    queue music2 hotelsneak fadein 10
    mc "Ah, crap... did you hear that thunder?" with dis14
    a "Yeah!"
    mc "*Sighs* Well, I left an umbrella by the entrance – a walk in the rain sounds kinda romantic too."
    mc "Y'know, as long as it's not like... typhoon-level chaos out there."
    play sound3 ding
    play sound4 elevator 
    show ga 2 with dis15
    mc "Huh?" with dis12
    mc "Oops, this isn't the hall."
    mc "Did we click on the third floor by accident?"
    show ga 3
    a "Whoa, this hotel looks so nice!" with dis
    mc "Yeah, it's not bad."
    mc "Though the reviews said the restaurant is better than the rooms."
    a "Let's take a look!"
    play sound run
    show ga 2 
    bla "Annie suddenly darts out of the elevator and into the hallway." with dis15
    mc "W-What?" 
    mc "Hey, come back!"
    show ga 4 with dis2
    mc "*Whispering* Annie!"with dis
    mc "We're not supposed to be here, come on!"
    play sound rubbody
    show ga 5
    a "*Popping out from around the corner* [mc!u]! Look what I found lying on the floor!" with dis
    show ga 6
    mc "Hmm? What is it?"
    show ga 5
    a "A key card to room 306! Someone probably lost it..."
    a "*Gasps* We should totally use it! We could wait out the rain in there!"
    a "Oh! Do you think they've got a minibar?"
    show ga 6
    mc "*Chuckles* No way. Did you book a room?"
    show ga 7
    a "Of course not! I just told you, I found this card on the floor!"
    show ga 6
    mc "Ahh... yes, I see."
    mc "You conveniently stumbled upon a card for a room that’s not yours, and now you’re suggesting we sneak in, raid their minibar, and risk the actual guests walking in at any moment."
    mc "You. {i}You{/i} are suggesting that."
    mc "Annie Winters."
    show ga 7
    a "Absolutely! I don't even know why you're acting so surprised, I've always been an adventurous girl..."
    show ga 6
    mc "*Chuckles* Of course."
    show ga 7
    a "Come on, let's go! It'll be fun!"
    a "An opportunity like this doesn't come around every day! Let's take a look!"
    play sound run
    show ga 8 with dis15
    mc "*Chuckles* (What's she up to now?)" with dis12
    show ga 9 with dis2
    mct "So room 306, huh..." with dis12
    show ga 10
    mct "And “Please Do Not Disturb”, HUH..." with dis14
    mct "I'm starting to like where this is going."
    play sound2 dooropenclose2
    play soundloop rain3 fadein 8 volume 0.5
    stop music2 fadeout 7
    show ga 11
    mc "Coming through, excuse me..." with dis15
    mc "You know, even if we put a 'Do Not Disturb' sign on the door, I doubt it’ll keep the real guests out."
    play sound rubbody
    show ga 12
    a "*Coming out of the bathroom* Okay, about that..." with dis14
    a "I have a confession to make."
    show ga 13
    mc "*Chuckles* Oh no, what is it?"
    show ga 12
    a "I didn't actually find that card on the floor."
    a "I booked this room for the night while I was in the bathroom earlier."
    show ga 13
    mc "*Gasps* WHAT? NO WAY..."
    show ga 12
    a "*Laughs* Alright, I know you already knew, but hear me out."
    a "It might seem a bit silly to get a hotel when we’re only, like, 40 minutes from home, but... with the rain and all, I thought it might..."
    show ga 13
    mc "It was a fantastic idea."
    mc "I definitely don’t want to end up soaked and freezing after such a wonderful date."
    show ga 12
    a "Right?!"
    show ga 13
    mc "Absolutely."
    show ga 14
    mc "*Chuckles* (Now that her heels are off, she’s back to her adorable, petite height. So cute.)"with dis14
    mct "Not that it makes her any less hot – quite the opposite."
    mct "That dress ain't lying..."
    a "*Giggles* What are you staring at?!"
    play sound clothes
    play sound2 footsteps
    show ga 15
    a "*Pulling you into the room* Alright, let’s ditch these clothes and slip into our pajamas! There are two comfy sets in the wardrobe!" with dis15
    mc "Uhh, good plan!"
    a "Of course! I'm SO good at making plans!"
    a "I always–"
    play sound4 clothes3
    play sound3 clothes
label ga_annie4:
    if _in_replay:
        play soundloop rain3 fadein 8 volume 0.5
    show ga 17
    a "*Tossing your sweater aside* Whoa..." with dis15
    a "You're so fit."
    a "You've gotten so much stronger since last year."
    show ga 16
    mc "Thank you, I try to eat well."
    show ga 17
    a "*Giggles* I can tell..."
    a "I like it."
    show ga 16
    a ". . ."
    mc "The way you’re tracing your finger on my chest is kind of turning me on more than it should, Annie..."
    mc "I wouldn't want to ruin your plans..."
    show ga 17
    a "Oh, don't worry... my plans are pretty simple. Nothing fancy needed."
    show ga 16
    mc "Oh really...?"
    mc "And what exactly are these... plans...?"
    mc "If you don't mind sharing."
    show ga 17
    a "Well..."
    a "We didn’t get to have dessert at the restaurant because of me being late, so I thought it’d be nice if we had it here instead."
    show ga 16
    mc "Oh, dessert, huh... that sounds good."
    a "Mm-hm..."
    mc "Although... room service is already closed."
    a "*Giggles* Mmh."
    show ga 17
    a "Yes."
    a "*Whispering* I know..."
    play sound clotheswhoosh
    play sound2 fall
    play sound3 debris3
    $ renpy.music.set_volume(0.45, channel='music3')
    stop soundloop fadeout 1
    play music3 ["<silence 1.5>"]
    queue music3 anniegoodfriends fadein 6
    scene ga18 
    bla "You press Annie against the wall, her breathing quickening rapidly." with hpunch
    mc "Annie, Annie, Annie... I’m starting to think you had ulterior motives for bringing me here."
    a "Really...?"
    a "Guess I wasn't as subtle as I thought..."
    mc "Are you sure you wanna do this?"
    a "*Breathing rapidly* . . ."
    a "Yes..."
    a "I'm ready."
    a "*Whispers* I'm ready for you."
    stop music2 fadeout 3
    menu:
        with dis12
        "[gr]Kiss her":
            play soundloop2 kissing fadein 3
            scene anniesex1 with dis2
            bla "You lean in towards Annie's lips and she quickly responds, rising on her toes to kiss you back with fervor." with dis12
            a "Mmmmmmhh..."
            mct "This is it... tonight's the night."
            mct "After so many years thinking I’d never be more than friends with Annie... it's finally happening."
            mct "She chose me. Her first time... is gonna be with me."
            mct "I feel like the luckiest man in the world right now."
            a "Mmmm..."
            mct "I just hope my nerves don’t mess things up."
            mct "I need to make this night unforgettable for both of us."
            a "*Moans* Mmmm..."
            pause 
            scene anniesex2 with dis2
            bla "You pull Annie's body even closer, pressing tightly against her, your lips never parting for a single moment." with dis12
            mct "I wonder what’s going through her mind right now."
            mct "As much as I want to rush to the finish line with her, I need to stay calm and take things slow, making sure she feels comfortable."
            mct "I really don't want her to freak out."
            mct "Not tonight..."
            a "MMmmmmMmmmm..."
            mct "She's definitely eager, though..."
            mct "You want this as much as I do, don't you, little nugget?"
            a "*Moans* Mmmmmm..."
            pause 
            play sound7 kiss
            stop soundloop2 fadeout 2
            play sound3 rubbody
            scene ga 20 with dis15
            play sound2 chair1
            bla "Breaking the kiss, you swiftly but gently push Annie onto the bed." with vpunchslow
            mc "Phew... you sure know how to drive me crazy, Annie."
            $ annieforeplay += 1
        "Throw her onto the bed":
            play sound ["<silence 0.1>", whoosh6]
            play sound2 chair1
            scene ga19
            bla "You abruptly push Annie onto the bed." with vpunchslow
            mc "Let's not waste a single second, then..."
            a ". . ."
            mc "God, you drive me crazy, Annie."
    show ga 22
    a "*Giggles* Who, me...?" with dis14
    show ga 21
    mc "Yeah, you..."
    mc "You know the effect you have on me."
    show ga 22
    a "I know nothing!"
    a "I'm just an innocent poor little girl."
    show ga 21
    mc "*Chuckles* Sure you are..."
    play sound clothes
    play sound2 couch
    show ga 23b
    bla "As you lean on the bed, Annie playfully removes her panties, making sure her dress covers everything as she teases you with a sly smile." with dis22
    show ga 24
    a "Do you mind if I also lose some of my clothes?"
    show ga 23
    mc "Not at all."
    mc "Although I wouldn't mind if you left that dress on."
    show ga 24
    a "*Giggles* The dress? No chance!"
    a "What if I get {i}dessert{/i} all over it? This thing was so expensive!"
    show ga 23
    mc "We'll just have to be... careful."
    show ga 24
    a "*Giggles* Last time you definitely were neither careful nor clean."
    show ga 23
    mc "Oh, but I've turned over a new leaf since then..."
    show ga 24
    a "*Giggles* Ah..."
    a "Well..."
    a "Show me, then..."
    show ga 23b
    menu anniepres:
        with dis14
        "[gr]Continue the foreplay":
            stop soundloop2 fadeout 2
            play sound clothes3
            play sound2 couch
            scene ga 25
            bla "You climb on top of Annie, trailing passionate kisses along her neck as she moans softly in appreciation." with dis17
            a "Mmmmmm..."
            play sound7 kiss
            mc "*Kiss* Mmwah."
            play sound3 clothes3
            scene ga 26
            bla "You begin your descent, kissing every inch of her body, savoring each soft gasp that escapes her lips." with dis2
            play sound7 kiss
            mc "*Kiss* Mmwah."
            a "*Whispers* [mc]..."
            mc "Shhh..."
            mc "Don't talk. Just relax and savor the moment."
            play sound6 kiss
            mc "*Kiss* You're my princess tonight..."
            a "*Giggles* O-Okay..."
            play sound4 clothes3
            scene ga 27
            bla "You take a moment to contemplate Annie's plump, virgin pussy lips." with dis17
            mc "Oh Annie..."
            mct "She looks so exposed..."
            mct "So vulnerable..."
            mct "And she's all mine..."
            $ renpy.music.set_volume(0.35, delay=20.0, channel='music3')
            play sound rubbody
            play soundloop wetting2 fadein 2
            scene anniesex3 with dis2
            a "*Moans* Mmmmmmmmhhhh...." with dis
            bla "You press your tongue against Annie's clit, losing yourself in the heat of the moment as her body's response grows more intense, her increasing wetness drawing you in deeper."
            mc "Mmmmmmhh..."
            mct "How the hell can she smell and taste this good...?"
            a "*Moans* O-Oh my god..."
            a "So good..."
            mct "She's completely smooth, not a single hair out of place."
            mct "She really prepared for tonight."
            a "Mmmmmmhhh....."
            mct "She was so looking forward to this moment..."
            mct "I've gotta make the wait worth it..."
            a "*Moans* Mmmmm-m-mmmhh..."
            a "*Moans* Ohh mmmm-y-yes, [mc]..."
            abt "*Moans* It f-feels so good..."
        "Fuck her [mt](fail)":
            jump annienotready
    menu:
        with dis14
        "[gr]Continue the foreplay":
            a "A-Aaaaahhh..." with dis 
            mct "Time to turn up the intensity a bit..."
            stop soundloop fadeout 2
            play sound rubbody
            play sound6 couch
            scene ga 27b
            mc "Stand up..." with dis17
            play sound7 clothes3
            play soundlow chair2
            scene ga 28
            bla "You gently guide Annie to her feet, her body pliant under your touch, as you return to kissing her neck and savoring the softness of her skin." with dis17
            play sound7 kiss
            mc "*Kiss* Mmwah." 
            a "*Giggles* Y-Your beard is tickling me..."
            mc "*Whisper* Now lean over the bed..."
            show ga 29
            a "Eh...? T-The... bed...?"with dis12
            a "What are you gonna..."
            mc "Just trust me."
            a "Ah..."
            a "O-Okay..."
            play sound couch
            play sound clothes3
            scene ga 30
            a "Like this...?" with dis15
            show ga 31
            mc "Yeah..." with dis14
            mc "Exactly like this..." 
            play soundloop2 wettingslow fadein 2
            play sound5 rubbody
            scene anniesex4 with dis2
            bla "Annie flinches as she feels your bare fingers glide between her thighs, trailing up and down her pussy lips." with dis15
            a "G-G-GGGgggghhh!!"
            a "*Moans* O-Oh my god....."
            abt "AAAAAAAHHHH..." with hpunch
            mc "Good?"
            a "O-Oh Lord, this feels amazing..."
            mct "Whoa... she's getting crazy wet."
            mct "Her juices are literally dripping all over my hand."
            asc "MmmMmm!" with hpunch 
            mc "Do you like it there?"
            a "G-God, YES, I do..."
            a "*Panting* S-So much..."
            mc "Nice..."
            bla "You continue running circles around Annie's clit and sliding your hand up and down her soaked pussy, savoring every moan and gasp she releases with each movement."with dis15
            a "AAAAAAaahhh..."
            a "Y-Yes, right there..."
            asc "Right there..."
            bla "After a few minutes, Annie relaxes into your touch, starting to push her lower body into your confident arm."
            abt "AAAaaaahhh yess...."
            abt "[mc], I'm g-gonna cum..."
            mct "She's ready..."
            stop soundloop2 fadeout 2
            jump annieyesready
        "Fuck her [mt](fail)":
            jump annienotready
label annienotready:
    stop soundloop fadeout 2
    play sound rubbody
    play sound2 couch
    scene ga 33
    bla "You take off your pants and leap onto the bed, pulling Annie toward you with a firm grip." with dis15
    mc "*Tracing Annie's figure* Oh, babe..."
    mc "You have no idea how long I've been waiting for this moment."
    show ga 34b
    a "*Breathing nervously* O-Oh my god."with dis14
    a "A-A-Already...?"
    mc "You said you were ready."
    a "I-I know, yeah, but..."
    a "I-I'm... n-nervous."
    mc "That's normal. You need to relax and enjoy the moment."
    a "R-Relax...?"
    a "Y-Yeah. O-Okay..."
    a "I'll try..."
    show ga 35
    mc "Let's just get a little more comfortable, yeah?" with dis12
    play sound tear2 volume 0.7
    play sound2 clothes4
    scene ga 36 with hpunch
    mc "Fuck yes..." with dis2
    a "Aah..."
    mc "You're so fucking hot..."
    play sound3 couch
    play sound4 clothes3
    show ga 40
    mc "Okay... are you ready...?" with dis15
    a "I-I'm not sure..."
    a "But... I want you to d-do it..."
    mc "Alright then..."
    mc "I'm going in..."
    show ga 41
    bla "You slowly start pushing yourself into Annie's petite body." with dis2
    mc "F-Fuck, that's too tight..."
    a "*Groans* AAAghh..."
    show ga 42
    bla "You continue trying to penetrate her, but her body resists your advances with a resilience like you've never encountered before." with dis2
    a "*Groans* Aggh..."
    a "*Panting* T-That's... t-too big for me..."
    a "*Panting* I c-can't..."
    stop music3 fadeout 20
    play soundloop rain3 fadein 35
    show ga 40
    mc "Ugh... you're just... too nervous..." with dis17
    mct "Damn, she's not wet enough, and her body is way too tense."
    mct "I don't wanna hurt her."
    show ga 43
    mc "You need to relax."with dis12
    show ga 44
    a "I-I'm t-trying."
    show ga 43
    mc ". . ."
    mc "How about we take a short break and try again later?"
    mc "I can go buy some lube too, that'll make things way easier."
    mc "Yeah?"
    a ". . ."
    show ga 44
    a "O-Okay."
    play sound couch
    play sound2 clothes3
    show ga 45
    bla "Annie slowly slips from beneath you and crawls to the corner of the bed." with dis2
    a ". . ."
    mc "Hey... are you okay?"
    a "*Sobbing* Yes."
    mc "Annie... please don't be sad. It's breaking my heart..."
    mc "I know it's your first time and it's very important to you."
    mc "We can wait."
    a "*Sobbing* Is it my fault...?"
    mc "What?! No! It's not your fault at all!"
    mc "You're just nervous, these things can happen."
    mc "You need to relax all of you."
    a "*Sobbing* Maybe we're just not compatible."
    mc "Oh, please don't say that!"
    a ". . ."
    a "I-I'm gonna take a shower."
    a "Do you mind if we just... sleep tonight?"
    mc "Of course not."
    a "Okay."
    a "Thank you."
    $ renpy.end_replay()
    play sound couch 
    play sound2 footsteps
    play sound3 ["<silence 2>", doorclose]
    show ga 46
    bla "Annie stands up, closes the bathroom door behind her, and locks it." with dis2
    play sound4 ["<silence 0.3>", chair1]
    scene ga 71
    mc "*Lying down* Aghh..." with dis
    mct "Well, this probably wasn’t Annie’s ideal first time."
    mct "If... we can even call it a first time. We barely did anything."
    mct "Maybe I went too fast?"
    mct "Or... perhaps we all have too many things on our mind right now."
    mct "She’s a nervous girl, maybe I should have taken things slower."
    play soundloop2 shower2 fadein 3
    bla "You hear the sound of the shower turning on."
    mct "Something tells me this shower’s going to be a long one."
    mct "And... the night might be even longer..."
    mc "*Sighs* (What a day...)"
    $ anniefirstimefail = True
    jump arabiadayletsgo
label annieyesready:
    play sound couch
    play sound2 clothes3
    play soundlow rubbody
    scene ga 32 with dis2
    play sound chair1
    bla "Just as you sense Annie nearing her peak, you pause and gently guide her to roll over onto the bed." with vpunchslow
    a "*Panting* Noooo..."
    a "*Panting* W-Why did you... stop...?"
    a "*Panting* I was... s-so close. If you'd kept that pace..."
    play sound rubbody
    play sound2 couch
    scene ga 33
    bla "Finally letting your erection free, you take off your pants and leap onto the bed, pulling Annie toward you with a firm grip." with dis15
    mc "*Tracing Annie's figure* Oh, babe..."
    mc "You have no idea how long I've been waiting for this moment."
    show ga 34
    a "*Breathing nervously* O-Oh my god."with dis15
    a "A-Are we...?"
    a "Are you gonna...?"
    a "W-What if I can't..."
    mc "You're ready, Annie. You said it yourself."
    mc "Just look at how insanely wet you are."
    a "Ahh..."
    a "A-Am I...?"
    $ renpy.music.set_volume(0.25, delay=15.0, channel='music3')
    scene anniesex5 with dis2
    abt "Oh my godddd...." with dis17
    bla "You begin to rub your throbbing member against Annie's drenched pussy lips with ease." 
    mc "Oooohh, Lord..."
    mc "Y-Yeah... that looks pretty fucking wet to me..."
    a "*Giggles* Y-Yeah, I guess I am..."
    mct "Jesus, this is so hot."
    mct "I need to be inside of her so bad..."
    a "*Moans* AAaahh..."
    a "*Panting* Ohh, [mc]..."
    pause
    play sound clothes3 
    scene ga 35 with dis12 
    mc "I wanna see more of you..." with dis
    play sound tear2 volume 0.7
    play sound2 clothes4
    scene ga 36 
    a "Aahh..." with hpunch
    mc "Much better..." 
    a "Y-Yeah..."
    play sound6 clothes3
    scene anniesex6 with dis2
    a "*Moans* AAAaaahhh..." with dis15
    a "*Moans* O-Oh my goodness..."
    mc "You’ve got me all kinds of messed up with how great you look, Annie..."
    mc "Your blush, your moans, your tiny raised nipples..."
    mc "Your dripping wet pussy..."
    a "*Giggles* Hah..."
    a "It's all... b-because of you..."
    mc "Is it...?"
    a "*Moans* Mmmmyeahh..."
    scene anniesex7 with dis2
    a "*Moans* AAaaaaahhh..." with dis15
    a "S-So good..."
    mc "Oh, trust me, you've seen nothing yet, my love..."
    a "*Moans* I-I haven't...?"
    mc "Hggghh..."
    mc "I-I can't handle this unbearable teasing anymore, Annie..."
    a "*Moans* AAaahh..."
    a ". . ."
    a "*Whispering* D-Do it..."
    mc "Do what...?"
    a "P-Put it..."
    a "Inside..."
    mc "Oh fuck yeah..."
    a "AAAahh..."
    a "I-I want you inside of me..."
    a "I..."
    abt "I need it..."
    play sound couch
    play sound2 rubbody
    scene ga 40 with dis2
    bla "After having waited for what felt like a lifetime, you put the tip of your cock in between Annie's pussy lips, poised to finally penetrate her." with dis15
    mc "Oh babe..."
    scene ga 38
    mc "Are you ready...?" with dis14
    show ga 39
    a "I am..."
    show ga 38
    mc "Good girl..."
    show ga 40
    mc "Alright..." with dis14
    mc "I'm going in..."
    play sound7 clothes3oily fadein 1
    show ga 41
    bla "You slowly start pushing yourself into Annie's petite body." with dis2
    a "*Pants* Oh h-holy..."
    mc "Oh sweet Lord, you're too tight..."
    a "*Panting* I... can take it..."
    play sound6 clothes3oily fadein 1
    show ga 42
    mc "Oooooooh yes..." with dis2
    abt "Ooooooohhh...."
    abt "O-OhHh GOD..."
    scene anniesex8 with dis2
    a "AAaahhh..." with dis17
    a "*Moans* Oh good grief, it's IN..."
    a "*Moans* I can feel it..."
    mc "W-WHAT THE HELL... that feels... amazing..."
    mct "I've never felt a pussy this tight in my life..."
    mct "I literally can't go deeper."
    a "*Moans* AAAaaahhh..."
    mct "This is it..."
    mct "I'm finally taking Annie's virginity..."
    mc "Aaahh yeah..."
    mc "You're doing great, babe..."
    a "P-Push deeper..."
    mc "Uhh...?"
    mc "D-Deeper?"
    mc "Are you sure...?"
    a "*Moans* Y-Yes... I wanna..."
    a "*Moans* Feel more of you..."
    mc "Lord give me strength..."
    scene anniesex9 with dis2
    mc "O-Oh fuck YEAHH..."with dis15
    mc "NOW WE'RE TALKING..."
    a "AAAAahhh... aaaaahhhhhh... aaAAaahh..."
    mct "My god, her petite body feels even better than I thought it would..."
    mct "I’ve never felt anything like this before."
    a "AAAAAGHH..."
    a "S-Sweet mercy..."
    a "It feels... it feels SO m-massive inside of me..."
    mc "A-Are you good? Does it hurt?"
    a "*Moans* No..."
    a "*Moans* It just feels..."
    a "*Moans* P-Perfect..."
    scene anniesex10 with dis2
    a "*Panting* AAaaaahhh..."with dis15
    mc "Oh babe, y-you feel so good..."
    mc "Keep looking me in the eyes..."
    a "*Panting* Y-Yeahh..."
    a "AAAggGh..."
    mc "D-Do you want me to slow down?"
    a "N-NO!"
    a "*Panting* KEEP GOING!"
    a "*Panting* I want you to go faster..."
    a "*Panting* T-This is... AMAZING..."
    mc "I t-told you you could handle it..."
    a "*Panting* AAAaahhh..."
    play sound clothes3
    play sound2 couch
    scene anniesex11 with dis2
    bla "As the minutes pass, Annie's insides adjust to your size and allow you to enter her even more, driving you both to an ecstasy of heat and pleasure." with dis15
    a "*Panting* Aaaah..."
    abt "*Panting* AAaAaaAaahh..."
    asc "*Panting* AAaaaAaAAAAAHHHH!!!!" with hpunch
    mc "O-Oh my god..."
    asc "*Panting* Y-YES..."
    asc "*Panting* K-Keep that pace...!!!"
    asc "*Panting* OH MY GOD!"
    mc "Oh Annie..."
    mct "She's almost taking all of my length inside of her..."
    asc "*Holding you tight* AAAAAAGGHH!!!"
    asc "*Panting* I-I'm cumming, [mc]..."
    asc "*Panting* I'm cumming so hard..."
    mc "Me too..."
    mc "I can't hold it inside any longer..."
    asc "*Panting* AAAAAAGH....."
    mc "I'm almost there..."
    asc "*Panting* D-Don't finish inside...!"
    asc "*Panting* AAaaghh..."
    asc "*Panting* P-Please..."
    mc "*Panting* B-But... where..."
    asc "*Panting* A-Anywhere... but... there..."with hpunch
    menu:
        with dis
        "Cum inside [mt](early scene end)":
            mc "A-Annie..." with dis 
            mc "I-I can't–" with hpunch 
            play sound cum4
            play sound2 chair1
            play sound3 slap1
            scene ga 47
            mcsc "*Cumming inside* AAAAAAAGHHH!!!" with vpunchslow 
            play sound6 couch
            play sound7 squirt
            asc "*Spasming* AAAAAhhhh!!!!" with vpunch 
            play sound cumall
            play sound7 couch
            mcsc "*Cumming inside* Oh, ANNIE...." with vpunch 
            play soundlow penetration3
            scene ga 48 with dis17
            mc "W-Whoa..." with dis14
            mc "Wow..."
            mc "That was... absolutely mind-blowing..." 
            mc "Your pussy's got to be the best in the world..."
            mc "It was... unreal..."
            a "*Catching her breath* I t-told..."
            a "I-I told you not to finish i-inside!" with hpunch 
            mc "W-What? Oh..."
            play sound couch
            a "G-Get off of me!"with hpunch 
            stop music3 fadeout 8
            play soundloop rain3 fadein 11
            play sound2 couch
            play sound3 rubbody
            play soundlow penetration3
            play sound3 clothes3oily
            show ga 50 with dis2
            bla "You move aside, letting Annie quickly slip from beneath you and crawl to the corner of the bed." with dis2
            mc "I-I'm so sorry."
            mc "I couldn't stop myself."
            show ga 49
            a "I told you not to do it inside!"
            show ga 50
            mc "I-I know, I'm really sorry."
            mc "I just... lost my mind for a second."
            a "*Grumbling* Mmmmmrrh..."
            mc "So, are you... in the dangerous days?"
            show ga 49
            a "Not really, but that's not an exact science. You know that."
            show ga 50
            mc "R-Right, sorry about that. Again."
            a "*Grumbling* Hmmmmph."
            show ga 49
            a "Anyway... I'm gonna take a shower to clean up this... mess."
            show ga 50
            mc "Do you forgive me...?"
            a "Grumbling* Hmph."
            show ga 49
            a "I'll consider it."
            show ga 50
            mc "*Chuckles* Yay!"
            show ga 51
            a "*Sticks out her tongue* PERVERT!" with dis
            a "You're lucky I'm in such a good mood!"
            play sound couch 
            play sound2 footsteps
            play sound3 ["<silence 2>", doorclose]
            show ga 46
            bla "Annie stands up and closes the bathroom door behind her." with dis2
            play sound4 ["<silence 0.3>", chair1]
            scene ga 71
            mc "*Lying down* Ahhhh..." with dis
            mct "This was even better than I imagined."
            $ renpy.end_replay()
            mct "Well... except for that accidental ending."
            play soundloop2 shower2 fadein 3
            bla "You hear the sound of the shower turning on."
            a "I'm getting into the shower!"
            mc "Okay!"
            a "Do you miss meeee...?"
            mc "*Laughs* Yes, a lot."
            a "Good! See you later!"
            mc "*Chuckles* (Something tells me this shower’s going to be a long one.)"
            mct "I should wait for her to finish up, though."
            mct "I've already pushed my luck tonight."
            mct "Although... I've gotta say."
            mct "It was so worth it..."
            jump arabiadayletsgo
        "Pull out":
            mc "A-Annie..." with dis
            mc "I-I'm gonna–" with hpunch  
    play sound penetration3
    scene ga 52b with dis15
    play sound2 cumall
    show ga 52
    mcsc "AAAAAAaghhh..." with hpunch
    play sound2 cumall
    show ga 52
    mcsc "AAAAAAHHHHHHH..." with hpunch
    play sound2 cumall
    play sound6 couch
    play sound4 cum4
    show ga 52
    mcsc "AAAAAAAHHHHHHGGHH..." with hpunch
    play sound3 clothes3oily
    scene ga 53 with dis2
    mc "*Panting* W-Whoa......" with dis15
    mc "G-God..."
    mc "That was... absolutely mind-blowing..." 
    mc "I swear, your pussy's got to be the best in the world..."
    mc "It was... unreal..."
    a "*Breathless* Hah..."
    a "T-Thank you..." 
    mc "Fuu..."
    a "C-Could you..."
    a "Could you move aside now, p-please? I need to..."
    mc "O-Oh, of course."
    stop music3 fadeout 8
    play soundloop rain3 fadein 11
    play sound3 clothes fadein 2
    play sound4 clothes3oily
    show ga 55
    bla "You move aside, letting Annie slip from beneath you and crawl to the corner of the bed." with dis22
    mc "Wow..."
    show ga 54
    a "*Giggles* Wow, indeed..."
    show ga 55
    mc "Was it as good for you as it was for me?"
    show ga 54
    a "I'm still in a state of shock, I think."
    a "I thought I knew o-orgasms could feel amazing, but... holy smokes."
    a "This one was something else. It felt way more... intense. So much... deeper."
    show ga 55
    mc "You took that like a champ."
    show ga 54
    a "*Giggles* T-Thank you..."
    show ga 55
    mc "But now... it's time for me to make the most scandalous proposition of the night."
    mc "Wanna cuddle?"
    show ga 54
    a "*Laughs* ABSOLUTELY!"
    a "Although, give me a minute – I need to hit the bathroom for a sec."
    show ga 56
    a "*Sticks out her tongue* Some PERVERT made a mess of me." with dis
    play sound couch 
    play sound2 footsteps
    play sound3 ["<silence 2>", doorclose]
    show ga 46
    bla "Annie stands up and closes the bathroom door behind her." with dis2
    play sound4 ["<silence 0.3>", chair1]
    scene ga 71
    mc "*Lying down* Ahhhh..." with dis
    mct "This was even better than I imagined."
    mct "Everything's turning out just perfectly."
    a "Are you still awake?!"
    mc "Of course!"
    a "Do you miss meeee...?"
    mc "*Laughs* Yes, a lot."
    a "Good!"
    mc "*Chuckles* (She's adorable.)"
    play sound dooropen1
    scene ga 57
    a "Finished!" with dis
    show ga 58
    mc "Oh, that was fast."
    show ga 57
    a "Can we cuddle now?"
    show ga 58
    mc "Of course! Come, come!"
    show ga 59
    a "But look away! I'm still naked!"
    show ga 58
    mc "*Snorts* What? Why?"
    show ga 59
    a "What do you mean, “why”?"
    a "Because I'm shy, obviously!"
    show ga 58
    mc "*Snorts* You're so silly."
    play sound couch
    play sound2 clothes3
    show ga 56b
    mc "*Sitting up* Alright, alright." with dis12
    mc "I'm not looking."
    a "*Giggles* Thanks!"
    mc "You do realize we just had sex and I literally saw everything I could have seen of you, right?"
    play sound chair1 volume 0.8
    a "*Jumping on the bed* But it's different!"with vpunchslow
    mc "*Chuckles* If you say so."
    a "I'm ready!"
    play sound3 clothes
    play sound7 couch
    show ga 61
    mc "*Pulling her in by the waist* Can I cuddle you now?" with dis17
    a "*Giggles* Yes..."
    mc "Aren't you cold like this?"
    a "Not really..."
    a "Your warmth is... all I need..."
    play sound4 clothes
    stop soundloop fadeout 40
    play music3 anniegoodfriends fadein 11
    show ga 60
    bla "Annie slowly moves her hips toward you, gently pressing her body against yours, her touch creating a delicious friction." with dis25
    mc "Annie..."
    show ga 62
    a "What...?"with dis14
    mc "You know what you're doing..."
    a "I'm just cuddling! Don't be a per–"
    scene ga 63
    bla "Annie's words are cut off by a soft moan as she feels your hardness poking on her still soaking wet pussy." with dis14
    a "AAahh..."
    a "You're... getting h-hard again...?"
    mc "I couldn't help it."
    mc "Do you want me to turn around...?"
    a "Mmmmh..."
    a "Perhaps we could..."
    a "Do it one last time before going to sleep...?"
    mc "Oh wow..."
    mc "Look who's the pervert now..."
    a "*Giggles* I'm just saying it for y–"
    play sound2 ["<silence 0.3>", penetration3] fadein 1
    play sound3 clothes3oily
    scene ga 64
    abt "A-A-AAaaaaggghhhh..." with dis2
    scene anniesex12 with dis2
    bla "You thrust deeply into Annie once more, letting yourself be engulfed by her warmth as your hands explore her, memorizing every ridge and curve of her body." with dis15
    a "Mmmm...."
    a "MmnnnnMMhh....."
    asc "MmMmMMMMMMhHHHH...!"
    mc "O-Oh Annie..."
    mc "You're so amazing..."
    a "*Moans* AAaahhhh... yeah..."
    a "Y-You are..."
    pause
    scene anniesex13 with dis2
    bla "You continue penetrating Annie over and over again, each thrust coming a little faster than the last." with dis15
    a "*Moans* S-Sweet heavens..." 
    a "*Moans* AAAAAHHHhh..."
    a "*Moans* T-This feels... amazing..."
    a "*Moans* P-Please... DON'T... STOP..."
    mc "AAAahh..."
    mc "I c-couldn't stop even if I wanted to..."
    asc "Y-Yeah..."
    asc "MMMMMhhHh..." with hpunch
    asc "K-Keep doing that..."
    asc "Fu..."
    asc "F-Fuck me..."
    mct "She did NOT just say that..."
    mct "I wanna go deeper in her... but with this position and how tight she is, it's gonna be complicated."
    asc "Aaaaahhh... AAaaahHHh..."
    abt "More..." with hpunch 
    mct "Should I lift her leg? Maybe ask her to–"
    play sound4 blow4
    play sound3 ["<silence 0.2>", whoosh6]
    play sound2 clothes4
    play soundlow chair1 
    scene ga 65b with pl
    bla "Annie suddenly spins around and climbs on top of you with a sudden boldness that catches you off guard." with vpunchslow
    mc "Oh, wow..."
    mc "That move definitely took me by surprise."
    scene ga 65
    a "I just wanted to see you."
    a "*Giggles* A-Although... now I don't know what to do next."
    show ga 65b
    mc "*Chuckles* Oh, don't worry..."
    play sound clothes3 
    show ga 66
    mc "*Lifting her hips* Just let me take care of the rest..." with dis17
    a "*Laughing nervously* O-Okay..."
    play soundlow ["<silence 0.3>", penetration3] fadein 1
    play sound7 clothes3oily
    scene ga 67
    bla "Annie slowly sinks onto your cock, groaning softly as your shaft stretches her." with dis22
    abt "Oooooofff..."
    mc "*Gently pushing her hips down* J-Just a little bit more..."
    play soundlow ["<silence 0.3>", penetration3] fadein 1
    play sound7 clothes3oily
    scene ga 68
    bla "She fully impales herself on your cock, being able to take all of you for the first time in the night." with dis22
    mc "F-FUUUUUUCK..."
    show ga 69
    mc "G-God..." with dis12
    mc "Y-You good?" 
    a "N-Never..."
    a "N-N-Never been better..."
    mc "Oh, my love..."
    scene anniesex14 with dis22
    asc "AAAHH... AAAAHHH... AAAAAGHHHH...." with dis12
    asc "Oh my god...!!!"
    mc "OH ANNIE..."
    asc "*Squeals* AAAAAGHH!" with hpunch
    mc "A-Are you holding up?"
    asc "Y-Yyyeaahh...."
    asc "I-I've never... felt... so wildly... full..."
    asc "*Squeals* AaaAAaaahh..." with hpunch
    asc "Y-You're hitting places I didn't even know existed..."
    mc "Oh, my girl..."
    mc "My perfect, beautiful, innocent little Miss Winters..."
    asc "AAAAAAahhhHh..."
    mct "Geez..."
    mct "I can't fucking believe I'm plunging all of my cock inside of her..."
    mct "She's so petite..."
    mct "And so damn tight... I almost feel like I'm rearranging her insides."
    asc "*Moans* AAAAaaHHhh..."
    mc "Dear Lord..."
    mc "Y-You're so... beautiful..."
    asc "*Breathy giggle* Aha-aaaahh..."
    play sound rubbody
    scene anniesexswitch 
    with dis04
    show screen annieangle
    asc "*Squeals* AAAahhh... AAAHHHHH!"with dis17
    mct "I fucking love how she even started to sync her movements with mine..."
    mct "She feels so light..."
    mct "I'm literally in heaven..."
    asc "[mc!u]..."
    asc "*Shivers* I'M CUMMING AGAIN..."
    mc "*Panting* F-Fuck, me too, babe..."
    mc "*Panting* I'm almost–"
    asc "*Moans* AAAAhhHHhh..."
    asc "*Panting* O-Okay..."
    asc "*Panting* D-D-DO IT..."
    mc "*Panting* H-Huh...?"
    asc "*Panting* F-FINISH... INSIDE... ME..."
    mc "*Panting* W-What? A-Are you sure?"
    mc "*Panting* But you said–"
    asc "*Panting* I CHANGED... M-MY... MIND..."
    asc "*Panting* I WANT... YOUR... S-S-SEED INSIDE OF ME..."
    asc "{size=50}I... {size=60}NEED... {size=75}IT..."
    mc "*Panting* OH LORD..."
    scene anniesex17 
    hide screen annieangle
    with dis04
    pause 22
    play sound2 rubbody
    play sound3 clothes3
    scene ga 70 with dis12
    stop music3 fadeout 18
    play soundloop rain3 fadein 17
    play sound chair1
    show ga 70 with vpunchslow
    bla "After vehemently orgasming at the same time, Annie collapses on you." with dis3
    bla "The room falls into a heavy silence, broken only by the ragged gasps of both of you as you struggle to catch your breath and regain your composure."
    abt "*Still flickering* G-G-Goddd..."
    abt "T-That was... intense..."
    mc "Haha... it really was, huh?"
    abt "Indes...cribable..."
    play sound5 clothes3
    scene ga71 with dis15
    pause .1
    play sound4 chair1
    mc "*Lying down* AAARGHH..." with dis15
    mc "T-That was... almost a religious experience, Annie."
    mc "Whoa..."
    play sound clothes
    play music2 annielove fadein 8
    scene ga 72 with dis22
    play sound7 couch
    stop soundloop fadeout 25
    bla "Annie softly crawls over you, her warmth pressing close as she pulls you into a tender embrace and her heartbeat syncs with yours." with dis2
    show ga 75
    mc "All good?"
    show ga 72
    a "Mm-hm."
    show ga 74
    a "Never been better."
    $ renpy.end_replay()
    show ga 75
    mc "Did it hurt?"
    show ga 74
    a "Not one bit."
    show ga 75
    mc "Really?"
    show ga 72
    a "Mm-hm."
    show ga 74
    a "Well... maybe I'm a little bit itchy now, but it felt AMAZING too, so it totally makes up for it."
    a "It was everything I dreamed it'd be and more."
    show ga 75
    mc "Well... I'm happy to hear that."
    show ga 72
    a "Hmmm."
    show ga 75
    mc "So... what do you want to do now, m'lady?"
    mc "Do you wanna take a shower?"
    scene anniesmh
    a "*Shaking her head* Mm-mm."
    scene ga 74
    a "No."
    a "I wanna stay here hugging you like a monkey until the sun comes up."
    show ga 75
    mc "But we need to sleep!"
    mc "I need to be at the gym with Dalia tomorrow at 9 in the morning!"
    show ga 74
    a "You can sleep, I don't mind."
    a "I'll just stay like this until you have to leave."
    show ga 75
    mc "Oh... so you'll let me sleep?"
    mc "No deep conversations or scary questions in the middle of the night?"
    scene anniesmh
    a "*Shaking her head* Mm-mm."
    scene ga 74
    a "Nothing, I promise."
    a "Although... you can ask, if you want."
    show ga 75
    mc "Ohh, is that so..."
    mc "Alright then."
    mc "Then let me ask you... when did you realize you were in love with me?"
    show ga 74
    a "Since the day I failed my first computing exam in Year 6 of primary school."
    a "You came over and helped me study, even though you missed a football game with some other kids from school because of it."
    show ga 75
    mc "Oh, wow!"
    mc "*Chuckles* I wasn't expecting such a precise answer."
    show ga 71
    a "Okay, how about you??" with dis15
    a "When did you start to {i}like{/i} me? I won't say “love”, don't worry."
    mc "I do love you!"
    a "*Giggles* Oh, really...?"
    a "Since when?!"
    mc "Huh... well, probably since forever, but I really realized it the other day after I got shot in that alley."
    a "*Gasps* THAT'S TOO LATE!"
    mc "B-But I've liked you since the day I met you!"
    mc "I was just scared to lose you if I ever tried anything!"
    a "Mmmmmmh..."
    mc "Did I fix it?"
    a "A little bit."
    mc "And if I say I love you again?"
    a "Hmm... It might just save you."
    mc "*Chuckles* I love you."
    a "*Giggles* I love you too."
    $ anniefullscene = True
    jump arabiadayletsgo







label arabiadayletsgo:
    stop music2 fadeout 8
    stop music3 fadeout 8
    stop soundloop fadeout 8
    stop soundloop2 fadeout 8
    scene black with dis3
    pause
    show screen nextday with dis27
    pause
    hide screen nextday with dis27
label arabiadayletsgo2:
    play soundloop gymambience volume 0.4 fadein 3
    scene gx 1 with dis3
    pause .5
    gymm "Yo, have you seen Chang?" with dis2
    gymm2 "What for?"
    gymm2 "If you want to join Air Guitar, that class is fully booked till February."
    gymm "Damn it..."
    mc "*Exhaling* Fuuuu...." 
    play sound boxingbag
    scene gx 2 
    scene gx3 with dissolve
    mc "YES!" with dis12
    play sound7 clothes3
    play sound5 panting volume 0.6 fadein 2
    scene gx 3b with dis2
    mc "*Panting* (Nice...)" with dis14
    mc "*Panting* (I keep getting stronger and stronger every day.)"
    mc "*Panting* (Ever since the day I joined Eternum, it's like I can feel myself leveling up constantly.)"
    mc "*Panting* (Close combat, knives, guns... in just a few months, I went from a complete noob to someone who can hold their own against almost anyone.)"
    show gx 4
    mct "But I've got to keep pushing." with dis14
    mct "Overconfidence isn’t just reckless – it’s a death sentence."
    mct "I'll be the man who will get the 10 Gems of Doom."
    mct "This isn't even about owning Ulysses anymore."
    mct "I'll defeat the Founder. I'll unravel the secrets of Eternum. Of its people."
    mct "I will save them all."
    play music happy17 fadein 5
    stop soundloop fadeout 12
    if daliapath:
        scene gx 5 
        d ". . ." with dis22 
        mil "Daaaamn, girl."
        mil "[mc]'s getting hella strong."
        show gx 6
        mil "Where'd you find yourself a man like that?"with dis
    else:
        scene gx 6
        mil "Aaaaaahhh... [mc]'s been looking hella fine lately." with dis22
        mil "Where can I find myself a man like that?"
    mil "I might not have that ass of yours, but come on..."
    mil "All I want is a muscular, hairy dude who can throw me over his shoulder!"
    mil "Is it really too much to ask?"
    if daliapath:
        d "*Chuckles* Seems reasonable to me."
    else:
        d "Maybe you should try asking him out."
        mil "Nah... I prefer dating people I don't know from work."
    show gx 7
    mil "*Sighs* And yet, all I find are things like... this." with dis12
    show gx 8
    mil ". . ." with dis
    mil "*Sighs* Demoralizing..."
    show gx 9
    kai "I know you're trying to hurt my feelings, Millie, but I'm invulnerable."
    kai "I transcended a long time ago."
    kai "Rejection and harsh words don't faze me anymore."
    show gx 8
    mil "Any dating tips for your coworker, Mr. Transcended?"
    show gx 9
    kai "I’ve given up on dating."
    kai "You should just forget about men and dedicate your life to yoga like me."
    show gx 8
    mil "The hell are you talking about? I literally saw your Tinder profile yesterday when I was swiping, and you just updated it with a recent pic!"
    kai ". . ."
    show gx 9
    kai "I mistook it for LinkedIn."
    show gx 8
    mil "Bullshit! You're a hypocrite!"
    show gx 11 
    mc "Hey, Dalia, I'm done over here!" with dis15
    mc "We can go whenever you want."
    show gx 12
    d "Sure!"
    d "Let's go."
    show gx 12b
    mil "Aight, I should go back to the front desk too." with dis 
    mil "Have a nice Sunday, boyos!"
    mil "And keep stacking plates on that squat, Dalia!"
    d "Always!"
    if daliarapewestern:
        scene gx 16
        bla "Dalia picks up her things and approaches you." with dis2
        mc "*Stretching* Phew, this was one hell of a workout."
        mc "Don't you think so?"
        show gx 15
        d "Look, I'm still mad about what happened at Frontier Trails."
        show gx 16
        mc "Aw shit, here we go again..."
        mc "I told you I'm sorry a hundred times..."
        show gx 15
        d "I know. And that's why I decided to try and put on a good face from now on."
        d "It's been weeks, and... I know you're not a bad guy."
        d "So... yeah. You're forgiven."
        d "Friends again."
        show gx 16
        mc "OH! THANK YOU!"
        mc "So... we good?"
        show gx 14
        d "Yeah, we good."
        show gx 13
        mc "Thank god."
        mc "I'm so sorry about that, Dalia. I really am."
        mc "I just want to leave it in the past."
        d "Mm-hm."
    else:
        scene gx 13
        bla "Dalia picks up her things and approaches you." with dis2
        mc "*Stretching* Phew, this was one hell of a workout."
        mc "Now I just need a mirror to check out that juicy pump."
        show gx 14b
        d "Hell yeah, nothing like a good abs or butt pump to boost the ego."
        show gx 13
    mc "Alright, so... how about we meet at the entrance in, say, 20 minutes?"
    mc "I can be ready in 5, but I'm guessing you need to dry your hair and handle all those “women things” after the shower."
    if alexpoolvisit:
        show gx 14
        d "Didn't you have to go to the pool to drop off the notes I gave you before for Alex?"
        show gx 13
        mc "Oh, right, I forgot."
        mc "Okay, then... let's meet in, like, 40 minutes at our corner?"
    show gx 14
    d "Sounds good."
    show gx 13
    mc "Cool!"
    mc "The plan is still to go to the Valley of the Kings server to check out the Xenomorph situation, right?"
    mc "And... you said you had a contact we were supposed to meet?"
    show gx 15
    d "Yep. I thought we could relax after what Annie did yesterday, but Ulysses just released the new current top 3 for the event. We might want to stay alert a little longer."
    show gx 16
    if anniepath:
        mc "Wait, seriously? We're not in first?"
    else:
        mc "Yeah, Luna told me about it. She said Annie almost blew up an entire planet."
        mc "Although... maybe it wasn't as big as we thought? We're still not in first?"
    show gx 15
    d "We are, but our lead isn’t as big as I expected."
    play sound whoosh6
    scene gx16b1 
    d "Thanks to Annie's special attack, “[nickname]” is still in the lead with over 1.6 million Xenomorph kills." with pr
    mc "Holy shit, that's a ton!"
    play sound whoosh6
    scene gx16b2
    d "In the third place, there's a paramilitary group from Andromeda led by someone called “Astra Zero”."
    d "They're way behind us, so I don't think they can ever become a real threat."
    mc "As expected."
    play sound whoosh6
    scene gx16b3
    d "But here's the problem: Hassan al-Rashid, the current number 2."
    d "Somehow, his team racked up over 1.1 million kills in just a week."
    mc "Damn, that's also a lot."
    d "He operates in the Valley of the Kings server, but there haven't even been that many Xenomorph sightings there. Which makes it... weird."
    d "And the guy's got like, unlimited money, but he's not exactly a fighter."
    mc "Hmm... yeah, something seems off."
    play sound whoosh6
    scene gx 16
    mc "Maybe he hired some skilled members for his team and sent them out to hunt Xenomorphs?" with pl
    show gx 15
    d "It's possible. For all we know, Thanatos himself could be a part of his team."
    show gx 16
    mc "Yikes, I hope not."
    mc "Although... I honestly doubt it. He doesn't exactly strike me as a team player."
    show gx 15
    d "Yeah, I had the same thought."
    show gx 16
    mc "Well, either way, I guess we've gotta pay Mr. Hassan a visit."
    show gx 15
    d "For sure, we've gotta figure out what's going on in that server."
    show gx 14
    d "So come on, let's take a shower, drink our protein shakes, and dive in!"
    d "Time to get to work!"
    if daliaproteinbuy and daliapath:
        show gx 16
        mc "OH, now that you mention protein shakes... I have something for you!"
        show gx 15
        d "Huh? For me?"
        show gx 16
        mc "Yeah! Close your eyes!"
        show gx 15
        d "My eyes...? What for?"
        show gx 16
        mc "It's a surprise! Just do it!"
        show gx 18
        d "*Closing her eyes* Alright, alright..." with dis14
        play sound2 locker
        show gx 17
        mc "*Opening the locker* Don't open them just yet..."
        show gx 18
        d "I swear, if you're about to do something weird..."
        show gx 17
        mc "Of course not, who do you take me for?"
        mc "Alright... here, grab this."
        mc "Careful, it's heavy!"
        play sound grab3
        play sound2 grab2
        if proteinflavor == 1:
            show gx 21 with vpunch
        elif proteinflavor == 2:
            show gx 19 with vpunch
        else:
            show gx 20 with vpunch
        pause
        mc "Okay, you can open your eyes now." with dis08
        if proteinflavor == 1:
            show gx 21b
        elif proteinflavor == 2:
            show gx 19b
        else:
            show gx 20b
        d ". . ." with dis
        d "Hmm?"
        show gx 22
        d "Huh...? Whey protein?" with dis12
        d "Where did you get this from?"
        show gx 22b
        mc "TA-DA!" 
        mc "It's a gift for you!"
        mc "Happy birthday!"
        show gx 22
        d "Birthday...?"
        d "What? My birthday's in January. And... it's still December."
        show gx 22b
        mc "I know, that's why it's a surprise!"
        d ". . ."
        mc ". . ."
        mc "I mean... I know it's nothing fancy, but I thought you'd like this more than flowers, or... you know, other “girly” stuff."
        show gx 22
        d "Oh..."
        show gx 22b
        mc ". . ."
        mc "A-And I know the whole “early birthday” thing sounds kinda stupid now that I say it out loud, but..."
        mc ". . ."
        mc "If you don’t like it, we can totally return it."
        if proteinflavor == 1:
            show gx 22
            d "No, no, I like it!"
            d "Just that..."
            d "It says... kale flavor?"
            d "This can't be real."
            show gx 22b
            mc "It is!"
            mc "I just thought it would be funnier if I picked some weird flavor."
            mc "Better than the typical “vanilla” one."
            show gx 22
            d "Oh, I see..."
            show gx 25
            d "*Snorts* Well, it’s definitely not the flavor I’d have picked, but maybe I can use it in some of my new recipes." with dis
            d "I've been experimenting with new things lately."  
        if proteinflavor == 2:
            show gx 22
            d "No, no, I like it!"
            d "I..."
            show gx 25
            d "I LOVE it, actually!" with dis
            d "*Chuckles* Sorry, I was still processing it."
            d "I really wasn't expecting this at all."
            d "Thank you so much, [mc]. You're the best."
            show gx 26
            mc "Don't even mention it."
            mc "It's just some silly gift for... a very special girl."      
            show gx 25
            d "Cookies and cream, huh? What made you pick this flavor?"
            show gx 26
            mc "Well, I wasn't sure of which one you'd like, so I went with a typical one."
            mc "You can't go wrong with the classics."
            show gx 25
            d "Ahh... a boring flavor for a boring girl. I get it."
            show gx 26
            mc "Oh come on, I didn't say that!"
            show gx 25
            d "*Laughs* I know, I know, I'm just messing with you."
            d "I'll definitely use this in one of my recipes."
        if proteinflavor == 3:  
            show gx 22
            d "No..."
            $ dalia_points += 1
            show gx 23
            d "N-NO! Of course not!" with dis12
            play sound beat
            show screen heartbeat
            d "Oh my god, I love it!"
            show gx 24
            mc "Oof, thank god. You weren't saying anything, so I thought..."
            show gx 23
            d "*Giggles* Sorry, I was still processing it."
            d "I really wasn't expecting this at all."
            d "Thank you so much."
            show gx 24
            mc "I'm so glad you liked it."
            show gx 23
            d "Was the barbecue flavor intentional?"
            show gx 24
            mc "Obviously!"
            mc "Honestly, I’ve never seen such a weird flavor before, but I know it’s your favorite food, so I figured it was worth a shot."
            show gx 23
            d "It {i}is{/i} my favorite."
            d "Thank you so much, [mc]."
            d "You're the best."
            show gx 24
            mc "Don't even mention it."
            mc "It's just some silly gift for... a very special girl."
            show gx 23
            d "I'm totally gonna use this with some of my new recipes."
        if proteinflavor == 3:
            show gx 24
        else:
            show gx 26
        mc "Uhh, that sounds exciting!"
        mc "I've noticed you've been cooking a lot more lately."
        show gx 25
        if proteinflavor == 3:
            d "You bet I am! And I'm getting pretty good at it." with dis
        else:
            d "You bet I am! And I'm getting pretty good at it." 
        d "I love to eat, so learning how to cook was the next logical step."
        show gx 26
        mc "I see no flaws in that logic."
        show gx 25
        if proteinflavor == 1:
            d "Thank you so much, [mc]."
            d "Just the thought alone means a lot to me."
            show gx 26
            mc "Don't even mention it."
            mc "It's just some silly gift for... a very special girl."
            show gx 25
            d "I’ll be sure to cook up some veggies for you from now on, since you seem to love them so much."
            show gx 26
            mc "*Chuckles* Oh no."
            mc "Will I at least get some delicious stuff too? Like chicken wings, or... cinnamon rolls?"
        if proteinflavor >= 2:
            d "I actually have some protein cinnamon rolls in my locker! Want to try one?"
            show gx 26
            mc "Hell yes!"
            show gx 25
            d "Okay then! Close your eyes."
            scene black
            mc "*Closing your eyes* Ah, you wanna give it back to me, huh..." with dis06
            play sound locker
            d "*Opening the locker* Who, me? Not at all..."
            mc "*Chuckles* So... tell me, did you bake those cinnamon rolls just for me? Or did you just {i}happen{/i} to have them in your locker?" 
            d "I baked them for everyone!"
            mc "Has anyone else tasted them?"
            d "Uh... no, not really."
            mc "Sooo, you baked them for me..."
            d "Sh-shush and open your mouth!"
            mc "You're not gonna do anything weird, are you?"
            d "*Giggles* You wish..."
            play sound chew
            bla "Dalia playfully places a cinnamon roll in your mouth, and as you start to chew, it melts on your tongue – it's absolutely delicious."
            show gx 13
            mc "*Opening your eyes* Oh mma mmgo'!"with dis06 
            play sound swallow
            mc "Whoa! This is SO good!"
            mc "It's still warm, soft, and packed with... gooey cinnamon goodness!"
            show gx 14b
            d "*Giggles* I know, right?"
            if daliabrowniesno:
                d "That time you chose Alex’s bagels over my brownies really got to me, so I’ve been working hard to level up my recipes ever since."
                show gx 14
                mc "And that's exactly why I said it, to motivate you. I saw your potential."
                show gx 14b
                d "*Giggles* Sure, sure..."
            elif daliabrowniesyes:
                d "That time you chose my brownies over Alex’s bagels made me realize I could actually have a future in cooking, so I’ve been working really hard to improve my recipes ever since."
                show gx 14
                mc "And that's why I was so enthusiastic about it, to motivate you. I saw your potential."
                show gx 14b
                d "*Giggles* Sure, sure..."
            else:
                show gx 13
                mc "Seriously, so, so good."
                d "Mm-hm."
            show gx 13
            mc "So, does this mean that you'll be whipping up more delicious food for me from now on?"
            mc "Maybe using my protein?"
        show gx 27
        d "Ummm... I'll think about it." with dis15
        d "But we can save that for another day."
        d "The desert awaits!"
        show gx 28
        mc "*Chuckles* Indeed. See you in a bit!"
        mc "Enjoy your shower..."
        d "Mm-hm..."
    else:
        show gx 13
        mc "See you in a bit!"
    play soundlow ["<silence 2>", doorclose2]
    scene gx 29
    bla "Dalia exits the room and makes her way to the changing room." with dis22
    mct "Alright..."
    if alexpoolvisit:
        mct "I should hurry up and go find Alex by the pool."
        play sound2 sniff
        mc "*Smelling yourself* (But... yikes, let's take a quick shower first.)"
    else:
        mct "I’ve got plenty of time before I have to meet Dalia outside, but I shouldn’t slack off either."
        mct "I've got no time to waste!"
    mc "Bye Kai!"
    kai "Ah, take care, [mc]!"
    kai "Tell Nancy to come back to class soon!"
    kai "*Whispering* Spending time alone with Gertrude has been... t-tough."
    mc "O-Of course! I will!"
    if alexpoolvisit:
        jump alexpool
    else:
        jump daliavalley


label alexpool:
    $ renpy.music.set_volume(0.0, channel='soundloop3')
    play soundloop3 poolambiance fadein 4
    play soundloop2 poolambiance fadein 4
    stop music fadeout 11
    scene gx 30 with dis3
    pause
    mct "Shit, I forgot to take off my shoes." with dis22
    mct "My old swimming teacher would kill me."
    $ renpy.music.set_volume(1.0, delay=2.0, channel='soundloop3')
    scene gx 31 with dis22
    play soundlow ["<silence 1.4>", splashpool] volume 0.8
    play sound2 poolwhistle
    swim "Jessica! Keep your head down!" with dis17
    swim "And do a proper flip turn!"
    mct "Ah, the memories... I remember coming here to learn how to swim as a kid."
    mct "I wonder if I ever crossed paths with Alex here before we even knew each other."
    play sound3 poolwhistle
    show gx 32 with dis14
    play sound splashpool volume 0.7
    mc "*Chuckles* (Maybe we did and I never noticed. She probably blended in way easier back then without all her tattoos.)" with dis12
    mc "*Looking around* (Hmmm... I'm not exactly sure of where I'm supposed to meet her now, though.)"
    mct "Maybe she's already in–"
    play sound water2
    play sound2 bubbles
    x "Well, well, well... look who's here."
    play music happy17 fadein 7
    $ renpy.music.set_volume(0.0, delay=8.0, channel='soundloop3')
    show gx 33
    mc "*Turning around* Hmm?" with dis12
    mc "Hey... I think I know that tattooed punk..."
    mc "Looks like she's trying way too hard to be cool."
    show gx 34
    x "*Snorts* Yeah... I think I know that juiced nerd too."
    x "Too bad he couldn't lift a sense of style."
    show gx 33
    mc "*Laughs* Excuse me? Did you just insult me, miss?"
    show gx 34
    x "I did. Any problem?"
    show gx 33
    mc "You wouldn't dare to say that to my face."
    show gx 34
    x "You think so...?"
    play sound bubbles
    play sound3 water
    play sound2 drips
    show gx 35
    bla "Alex comes out of the water." with dis15
    mct "Damn, boy... that's a tight swimsuit..."
    play sound7 water3
    play sound3 drips
    scene gx 36 with dis15
    x "Oh no..." with dis14
    $ unlock_look("alex", 9)
    play sound5 clothes4
    show gx 37
    x "*Pulling off her swim cap* I know that horndog look." with dis14
    show gx 38
    mc "I'm just appreciating how... {i}hydrodynamic{/i} your swimsuit is."
    show gx 37
    x "Well... better than staring at my face, I guess. My hair must be a disaster."
    show gx 38
    mc "You're as gorgeous as always."
    show gx 37
    x "No, I'm not. I know what chlorine and this swim cap do to me."
    x "But I appreciate the lying."
    show gx 38
    mc "Ah, the price to pay to be the best..."
    show gx 37
    x "*Chuckles* Indeed."
    x "Do you have {i}any{/i} idea how many yards I swam today?"
    show gx 38
    mc "Mmmm... 50?"
    show gx 37
    x "Over 10,000. I've been here since 7AM."
    play sound whistle3
    show gx 38
    mc "*Whistles* Holy shit."
    mc "Should I give you a medal now, or...?"
    show gx 37
    x "*Laughs* Oh, fuck off already."
    x "Did you bring my math notes or not?"
    show gx 38
    mc "*Chuckles* I did. I have them here in my backpack."
    show gx 37
    x "Sweet. Thank you, [mc]."
    show gx 38
    mc "I'm really glad to see you, Alex."
    mc "How are you holding up? I feel like we barely saw you these last few days."
    show gx 37
    x "I'm good, thanks. Just swamped with work."
    x "A bunch of swimming practices too, but I enjoy those."
    x "Helps me clear my head."
    show gx 38
    mc "Well, glad to hear it."
    mc "Still wish I could see you more often, though."
    show gx 37
    x "Next week should be better – I’ve got some time off from the cafe starting Saturday."
    show gx 38
    mc "Oh, nice!"
    mc "Saturday, 16th – annoy Alex. Noted down in my calendar."
    show gx 37
    x "*Chuckle* Looking forward to it."
    show gx 38
    mc "You know Nancy's offer still stands, right?"
    mc "You could come live with us. You don't have to work yourself so hard."
    show gx 39
    x "I didn't leave my parents' place just to go beg somewhere else."
    x "And I’m not giving William the satisfaction of seeing me unable to survive on my own."
    x "Fuck him and his entire bloodline."
    show gx 37
    x "But... don't get me wrong, I still appreciate the gesture. Thanks, [mc]."
    show gx 38
    mc "Mmh, fair enough."
    mc "And anytime, of course. You'll always have my support."
    show gx 40
    swim "Oh my sweet baby Jesus." with dis14
    swim "Tell me you did NOT just enter the pool fully dressed."
    show gx 41
    x "Y-Yeah, I was telling him just that."
    x "I'm so sorry, Coach."
    show gx 40
    swim "Is this man your friend, Alexandra?"
    show gx 41
    x "Y-Yeah, he's my... I know him from school."
    x "He just came to give me something."
    show gx 40
    swim "He can't be at the pool without a swimsuit and appropriate footwear."
    show gx 41
    x "Yeah, he's heading out right now!"
    x "Just that..."
    x "Um... do you mind if I take a 10-minute break before I hit the pool again so he can give me my stuff?"
    show gx 40
    swim "*Grumbling* Ugh..."
    swim "Fine, but don't take too long."
    swim "We don't have practice until next Friday, and nationals are coming up fast!"
    show gx 41
    x "Absolutely!"
    show gx 42
    x "*Whispering* Do you see that exit in the corner?" with dis12
    mc "*Whispering* I do, yeah."
    x "*Whispering* All my stuff is right there, in the locker room."
    x "*Whispering* Let's meet there. You give me the notes, you leave, and I go back to the pool."
    x "*Whispering* But don't walk by the pool. Take the stairs up and walk across the upper stands, unless you want Anna to actually kill you."
    mc "*Whispering* Gotcha."
    show gx 43
    bla "Alex makes her way to the exit, walking along the edge of the pool."with dis2
    mc "Um... I'm so sorry, ma'am."
    show gx 44
    swim "So... you're her boyfriend?"
    show gx 43
    mc "W-What?"
    mc "No, I'm..."
    show gx 44
    swim "I've been in this world for almost five decades, boy, so don't bullshit me."
    swim "That girl is the best swimmer I've seen in the last 10 years."
    swim "If you’re the reason she doesn’t make it to the next Olympics, I’ll personally hunt you down to kick your ass."
    show gx 43
    mc "U-Understood, ma'am."
    mc "Not gonna happen. I'll be there cheering for her at the Olympics."
    mc "Front row."
    show gx 44
    swim "You better."
    show gx 43
    mc ". . ."
    swim ". . ."
    mc "You know, if you allow me the compliment, you don't look fift–"
    show gx 44
    swim "Get out of my pool."
    show gx 43
    mc "On it."
    stop music fadeout 16
    $ renpy.music.set_volume(1.0, delay=8.0, channel='soundloop3')
    scene gx 30 with dis25
    play sound poolwhistle
    swim "Alright everyone, back to the water!" with dis2
    swim "500 yards of freestyle kick!"
    mct "T-That woman is scary."
    mct "Anyway, I better get this over with quickly. I don't want to waste too much of Alex's time."
    scene gx 45 with dis2
    bla "Just as you were told, you head to the other side of the pool, making your way past the stands." with dis15
    mct "I can feel the coach's eyes cutting right through me... I know she's watching my movements."
    mct "Don't turn your head, [mc]..."
    play soundlow poolwhistle
    play sound ["<silence 1.4>", splashpool] volume 0.4
    show gx 46 with dis2
    mc "*Going down the stairs* Alright, mission accomplished!" with dis15
    mc "Here are all of your notes."
    show gx 47
    x "Sweet, thanks."
    show gx 46
    mc "*Handing her the bag* There you go."
    show gx 47
    x "Uh... I'm still wet, do you mind taking it to my locker yourself?"
    x "I don't wanna mess up Dalia's notes with water."
    show gx 46
    mc "Huh, that's totally on you both. Who even writes notes by hand anymore?"
    show gx 47
    if alexpen:
        x "Says the guy who complimented a pen as a conversation starter."
        show gx 46
        mc "*Snorts* Okay, you got me there."
    else:
        x "I'm an old-school girl."
        show gx 46
        mc "*Chuckles* If you say so."
    mc "Alright, so, where are the lockers?"
    show gx 47
    x "Here, in the changing room."
    show gx 46
    mc "The... changing room?"
    mc "You mean the women's one?"
    x "Mm-hm."
    show gx 47
    x "What? Are you scared?"
    show gx 46
    mc "I mean... “scared” is not the word, just that..."
    show gx 49
    x "No worries, there're only three other women using the pool today, and they're all gonna be in there for at least another hour." with dis
    show gx 48
    mc "Um... are you sure?"
    mc "I don't wanna be kicked out of the gym."
    show gx 49
    x "Yeah, I'm sure. They're all part of the team."
    x "And we're only gonna be there for a moment."
    x "Come on, don't be a pussy and follow me."
    play sound dooropenclose2
    scene gx 50 with dis15
    mct "Umm... okay." with dis14
    mct "Well, if I do get caught, I suppose Alex will speak up for me." 
    mct "Or... at least I like to think she would..."
    $ renpy.music.set_volume(0.6, delay=3.0, channel='soundloop3')
    stop soundloop2 fadeout 3
    play sound dooropenclose2
    scene gx 51 with dis17
    bla "You quickly turn around the corner and enter the women's locker room." with dis14
    mc "Damn, this place is quite an upgrade from the men's changing room."
    mc "Not only does it look clean, but it actually smells nice in here."
    show gx 52 with dis17
    play sound dropbackpack
    mc "*Leaving your bag on a bench* (Not gonna lie, it's quite exciting to be here...)" with dis14
    mct "I'm basically living out my middle school fantasy right now."
    mc "So... which one is your locker?"
label ga_alex3:
    if _in_replay:
        $ renpy.music.set_volume(0.6, channel='soundloop3')
        play soundloop3 poolambiance fadein 1
        show gx 52 
        mc "So... which one is your locker?" with dis15
    mc "Do you always have the same one, or do you just pick one every–"
    play sound whoosh6
    play sound2 fall3
    play sound3 debris3
    $ renpy.music.set_volume(0.8, channel='music3')
    play music3 eyg2 fadein 3
    stop soundloop3
    show gx53
    bla "Alex appears from around the corner, pushing you against the wall." with hpunch 
    scene gx 54
    mc "A-Alex...?" with dis12
    mc "You okay...?"
    show gx 55
    x "I've missed you, you know?"
    show gx 54
    mc "Eh...?"
    mc "I mean... I've missed you so much too."
    show gx 55
    x "Really...?"
    show gx 54
    mc "Of cour–"
    play sound grab2
    play sound2 whoosh6
    play soundlow fist
    show gx56
    bla "Alex lunges forward and kisses you on the lips." with hpunch
    mct "Mmmh!?"
    mct "What's gotten into her all of a sudden?!"
    mct "She's usually not this... {i}direct."
    x "Mmmmm..."
    $ alex_points += 1
    play sound3 beat
    show screen heartbeat
    play sound clothes3
    scene gx 57
    bla "As Alex starts to playfully tease your tongue, you easily cave in, matching her passion and energy." with dis15
    mct "Although... well, I definitely shouldn't complain..."
    x "Mmmmmh..."
    mct "Even though you can tell she’s been swimming for a while, her scent is still there — as unmistakable as always."
    mct "God, she's such a good kisser..."
    bla "You can feel yourself getting hard. Alex, sensing it, and far from pulling away, presses her body against yours with more intensity."
    x "Mmmmm..."
    play sound clothes3
    scene gx 58 with dis15
    x "*Taking a step back* Mmmhh..." with dis12
    mc "D-Damn, girl... I didn't know the pool's chlorine got you this horny."
    show gx 59
    x "*Chuckles* Must be that."
    show gx 58
    mc "Although I must say, that kiss got me all fired up too, that's for sure."
    show gx 59
    x "Yeah, I can see the bulge in your pants."
    show gx 58
    x "Hmmmm..."
    show gx 59
    x "We're gonna have to do something about that before you go back out there, don't you think?"
    x "My coach would be so mad if she saw you like this."
    show gx 58
    mc "What...?"
    mc "You mean... now? H-Here?"
    x "Mm-hm..."
    mc "But... I'm supposed to meet Dalia in 15 minutes."
    show gx 59
    if daliapath:
        x "Oh, do you wanna call her to see if she wants to join?"
        show gx 58
        mc "W-What...??"
        show gx 59
        x "I said that I'm also supposed to be back in the pool in 10 minutes."
        show gx 58
        mc "That's not what you said."
        show gx 59  
        x "*Giggles* Seriously, I have to be there in 10."
    else:
        x "And I'm supposed to be back in the pool in 10."
    x "But that doesn't mean we can’t sneak in a little... quick fun in here, right?"
    x "Or... do we need to go through some loooong adventure in Eternum every time? Fighting outlaws and dodging Praetorians for hours... just to be able to enjoy each other for a short while afterwards?"
    show gx 58
    mc "I mean... no, we don't really need to..."
    mc "You know I’m all for spontaneity."
    show gx 59
    x "If you need several hours of blood and action just to get in the mood, I understand, no worries."
    show gx 58
    mc "Nah... not really, no... this works just fine."
    show gx 59
    x "Really...?"
    x "Let me see..."
    play sound clothesfull
    play sound2 zip volume 0.25
    scene gx 60
    bla "Alex leans forward and pulls your pants down, exposing your fully erect member." with dis22
    show gx 62
    x "Whoa... you weren't lying. You {i}really{/i} are a spontaneous guy."
    x "I like it..."
    show gx 60
    mc "Oh... F-FUCK yes, babe..."
    show gx 62
    x "Calm down, cowboy... I haven't even touched you yet."
    x "What if I walked away now?"
    show gx 61
    mc "Oh, I know you wouldn't."
    mc "You're craving this more than me... I can see it in your eyes."
    show gx 62
    x "*Snorts* You hold yourself in such high regard, you know?"
    show gx 61
    mc "So I'm not telling the truth?"
    show gx 60
    x "Hmmm..."
    play sound clothes3oily
    play sound2 ["<silence 1>", kiss] volume 0.8
    show gx 63
    x "*Kissing your dick* Perhaps..." with dis14
    mc "Oh yeah..."
    mc "That's it..."
    mc "Put it inside..."
    x "*Using a high-pitched voice* It's too big for my little mouth, senpai..."
    mc "*Chuckles* We both know you can handle it perfectly fine..."
    play sound blow6
    show gx 64 with dis15
    mc "Oh, f-fuck yes, Alex..." with dis12
    x "Mmmmhmm..."
    play sound2 blowpop
    show gx 63
    x "*Taking a deep breath* Mmmmghh..." with dis14
    mc "Yeah... p-put it back in..."
    x "Mmmh... you're very demanding today..."
    mc "Well, we don’t exactly have that kind of time right now..."
    x "*Giggles* I'm starting to think this was a bad idea."
    x "Can you even finish within 10 minutes...?"
    mc "If you do a good job..."
    x "*Whispering* Ahh... I like a challenge..."
    $ renpy.music.set_volume(0.2, delay=13.0, channel='music3')
    play sound2 ["<silence 0.9>", poolwhistle] volume 0.3
    play sound4["<silence 2.3>", splashpool] volume 0.1
    play soundlow blow6
    $ renpy.music.set_volume(1.0, channel='soundloop')
    $ renpy.music.set_volume(1.0, channel='soundloop2')
    play soundloop blowjob2 fadein 3
    scene alexpool1 with dis22
    pause 7.8
    show alexpool2 
    hide alexpool1
    with dis14
    mc "O-O-OOHHHHhhhh... sweet Jesus..." with dis
    mc "O-Oh my god, Alex..."
    x "Mmmmmhh..."
    mc "Yeah, keep sucking it just like that, baby..."
    mc "Make it wet..."
    x "*Moans* Mmmmmhhh..."
    mc "F-Fuck, I can't even see the door from here..."
    mc "You'd hear it if someone opens the door, r-right?"
    mc "I'm afraid I might be... too distracted..."
    x "*Giggles* Mm-mm-mmhh..."
    mc "I'll take that as a {i}maybe..."
    mc "AAaaahhh..."
    x "*Gagging* Mmmmmmhh..."
    pause
    stop soundloop
    play sound3 clothes3oily
    scene gx 65
    bla "Alex suddenly stops and leans back." with dis15
    mc "Oh yes..."
    show gx 65b
    mc "Let me see you better..." with dis12
    play sound latexswim
    play sound7 clothes3
    show gx 66 with dis2
    mc "Good Lord..." with dis15
    mc "I thought that super tight swimsuit looked great on you... but it doesn't even do you justice..."
    x "*Chuckles* Mmmhh..."
    play sound clothes3oily
    play sound6 blow4
    play soundloop blowjob2 fadein 2
    scene alexpool3 with dis15
    bla "Without saying a word, Alex leans forward again, taking your pulsing cock into her warm mouth once more." with dis15
    mc "A-AaaA-Aaahhh... f-fuck yeah..."
    mct "God... I don't even know how she can hold this pose."
    mct "My back would literally break if I tried something like this."
    mct "I guess swimming really pays off... her back and core strength are on another level..."
    play soundlow ["<silence 1.4>", splashpool] volume 0.12
    play sound2 poolwhistle volume 0.3
    x "*Moans* Mmmmm...."
    mc "Aaaahh yeah..."
    mct "I guess it also helps that she's actually a shortie."
    mct "I always forget she's not much taller than Nova or even Annie."
    x "*Moans* Mmmmmmhhh..."
    mc "Oooooohhhh b-babe..."
    mc "I can't think straight anymore..."
    stop soundloop fadeout 2
    play soundlow blowpop
    scene gx 68
    bla "Alex stops sucking your dick and takes a moment to breathe." with dis15
    x "AAaahh... ahhh....aaaaaaahhhh..."
    x "F-Fuck..."
    mc "Good girl..."
    x "*Sniffs* You're... so smelly..."
    mc "But you like that smell... don't lie..."
    x "It's f-fucking disgusting..."
    mc "Your eyes don't tell the same story, Alex..."
    x "*Giggles* O-Oh, really...?"
    mc "Now put my big cock inside your mouth again... I know you want to..."
    x "*Giggles* Mmhm..."
    play soundloop blowjob2 fadein 2
    play sound blow6
    scene alexpool4 with dis2
    bla "Alex engulfs your already soaked cock with her lips, devouring you as if she were starving." with dis15
    mc "*Moans* Y-Yeah, just like that..."
    mc "You're such an obedient girl..."
    x "Mmm-hmmm...?"
    mc "*Moans* Y-Yeah..."
    mc "T-This is... glorious..."
    x "*Moaning* MmmmmMmmhh..."
    mc "Don't stop..."
    x "*Moaning louder* MmmmmMMMmmmmhhh..."
    bla "Despite the subtle gagging sounds you hear, Alex, driven by lust, maintains her pace without hesitation."
    mc "AAaahh..."
    mc "Does it taste good?"
    play sound2 poolwhistle volume 0.3
    x "*Moans* Mm-mhh...."
    mc "Good..."
    mc "Your throat is mine..."
    mc "And only mine..."
    scene alexpool5 with dis2
    bla "The world outside fades into a blur. You can only focus on Alex, memorizing every inch of her tattoos and the curves of her body as she takes you into her mouth without relent." with dis15
    x "Mmmmggg... mmmmgggghhh... mmmmgghhhw..."
    mc "O-Ohh, fuck yes..."
    bla "Even though you can feel your girth stretching Alex's lips, she still manages to swirl her tongue around the tip of your cock each time she takes it up and down her throat."
    mc "W-Whoa..."
    x "*Moans* Mmmmmmhhh..."
    mc "This is... h-heaven..."
    mct "I’m not even sure I’d want her to know if someone came in right now..."
    mct "I just... need her to... continue..."
    mc "D-Don't stop..."
    mc "*Moans* AAAAaaAAaAA-Aaahhh..."
    stop soundloop fadeout 2
    play soundlow blowpop volume 0.7
    scene gx 68
    x "*Stopping to breathe* AAAAahhh..." with dis15
    x "F-Fuck... y-you're moaning like a foghorn, [mc]... show some self-control..."
    mc "*Chuckles* M-Me? And what about you?"
    mc "You're not exactly showing much self-control down there..."
    x "*Giggles* Oh, but that's where we differ..."
    x "I know I have no self-control. I don't want it."
    x "*Whispering* I simply take what I want..."
    play soundloop blowjob2 fadein 2
    play sound3 clothes3oily
    scene alexpool6 with dis2
    bla "Alex takes your junk into her saliva-soaked throat again. Your mind begins to drift away as waves of pleasure surge through you." with dis15
    mc "O-O-Ohhh Jesus..."
    mc "*Pushing your hips towards her face* Y-Yeah... take it all..."
    play soundlow ["<silence 1.7>", splashpool] volume 0.12
    play sound2 ["<silence 0.3>", poolwhistle] volume 0.3
    x "*Moans* Mmm-mmmhhh..."
    mc "S-Suck it till it's dry..."
    x "*Moans* MmMMmmmmMmhh..."
    mc "Oh Alex..."
    mc "Good girl..."
    pause
    bla "The sight of the high-class girl going down on you and her sultry gaze locking onto yours send a thrill of power coursing through your veins. You can finally feel the climax looming tantalizingly close." with dis
    mct "Oh shit..."
    x "*Moans* Mm-m-mmmmhhmmhmm..."
    mct "F-Fuck, I'm at my limit..."
    mct "I'm gonna cum..."
    mct "I can't stop it..."
    mct "I'm gonna–"
    stop soundloop fadeout 2
    play sound blow1 
    play sound3 clothes3
    scene gx 68
    x "*Stopping to breath* AAAAAGgggGGhhhh..." with dis15
    x "*Panting* F-FUCKING... HELL..."
    mct "Oh god, that was so close..."
    x "*Recovering her breath* Jesus Christ, w-when are you gonna cum?"
    x "*Recovering her breath* It didn't take you this long at the Boyle mansion..."
    mc "Heh... feeling frustrated?"
    play sound clothes3
    show gx 70
    x "*Leaning back* Oh, shut the fuck up." with dis15
    show gx 69
    mc "Hey... it's okay, we can't win every day."
    mc "Sometimes we've gotta take the L and move on."
    show gx 70
    x "*Snorts* Are you at least close, or...?"
    show gx 69
    mc "Me? Nah... sorry, I feel like I could continue for hours."
    show gx 70
    x "Really...?"
    show gx 71
    x ". . ." with dis08
    play soundlow ["<silence 2>", splashpool] volume 0.1
    play sound2 ["<silence 0.6>", poolwhistle] volume 0.3
    show gx 72
    bla "Alex glances at the door, pausing for a few seconds in silence, with only the distant whistle of the swimming coach and the splashes of water breaking the silence." with dis14
    x ". . ."
    show gx 74 with dis15
    x "*Grabbing your hand* Okay, come with me..." with dis12
    show gx 73
    mc "What...?"
    mc "O-Okay, I-I lied, I'm actually so fucking close."
    mc "P-Please, don't stop now. I'm almost there..."
    show gx 74
    x "Shut up and come..."
    show gx 73
    mc "Eh...?"
    play sound dooropen4 fadein 1
    show gx 75 with dis2
    bla "Alex guides you to the toilets of the locker room while you struggle to fully remove your pants." with dis17
    show gx 75b
    x "Here. Get inside."
    show gx 75
    mct "Oh boy."
    mct "OH FUCK YES."
    mc "Is this what I think it is...?"
    mc "*Walking towards her* Or are you–"
    play sound3 whoosh6
    play sound toiletceramic
    play sound2 debris3
    show gx76
    bla "As soon as you get close, Alex swiftly pushes you into the toilet cubicle." with hpunch 
    x "I'm sure no one will notice it if I'm missing another five minutes."
    x "But... you better be quiet..."
    mc "Oh no... what are you planning to do...?"
    scene gx 78
    x "I said I'd make you cum... and that's exactly what I plan to do." with dis17
    show gx 77
    mc "Oh my... bringing out the big guns, huh...?"
    show gx 78
    x "Well, since we're at it... I might as well have my fun too."
    x "Just a quickie. Five minutes."
    x "You know what a “quickie” is, right?"
    show gx 77
    mc "*Snorts* Yeah, I’ve seen it mentioned on a few forums."
    show gx 78
    x "*Giggles* Good... that'll save us time."
    play sound clothes3
    show gx 79
    bla "After taking one last peek outside, Alex moves the lower part of her swimsuit aside as she positions herself above you, guiding your cock towards her awaiting pussy." with dis14
    x "Time to put this monster cock of yours to better use..."
    mc "Fuck yes..."
    play sound penetration3 fadein 1
    play sound2 clothes3oily
    show gx 80
    x "AAAaaaahhhh..." with dis2
    mc "Oh my g-god, that's tight..."
    show gx 81
    x "Oh, f-for fucking fuck's sake..." with dis15
    x "I missed this sensation sooo fucking much..."
    scene alexpool7 with dis2
    bla "Alex starts to sway her hips, letting herself be penetrated by your manhood, enveloping you in a wave of pleasure like only her body can deliver."with dis14
    x "*Moans* OH MY F-FUCKING GOD..."
    mc "Oh d-dear, y-you're so wet..."
    x "Haha..."
    x "Let's just say... that sucking your cock out there turned me on a {i}little{/i} bit..."
    mc "*Moans* O-Oh, Alex..."
    x "AAAaAaaaAahhh..."
    mc "O-Oooohhh..."
    x "D-Don't you dare to finish now..."
    mc "I-I'll try..."
    x "*Moans* AAAaagghhh..."
    x "Naked grannies, the lineup of the '90s Bulls, or f-fucking Jabba the Hutt – start thinking of whatever the fuck you want... but..."
    xsc "D-DON'T. {size=40}CUM. {size=50}YET."
    mc "O-Oh fuck..."
    scene alexpool8 with dis2
    x "*Moans* AAAAahhh... aAAAhhh... AAAgggwwwggh..." with dis15
    x "*Panting* OH MY GOD..."
    x "Y-You feel... as m-massive as I remembered..."
    mc "And you feel... tighter than ever..."
    x "*Panting* H-Heh... g-good combination, isn't it...?"
    mc "*Chuckles* H-Hell yeah, babe..."
    x "*Moans* Oh god..."
    x "*Moans* S-So good..."
    pause
    bla "Alex continues to ride you relentlessly, allowing herself to adjust to your size until she can finally take all of you deep inside of her." with dis
    scene alexpool9 with dis2
    xsc "*Moaning* Aaaahhh... {size=40}aaahhh... {size=55}aaaAAaaHHHhh..." with dis15
    xsc "N-Now..."
    xsc "W-We're... talking..."
    mc "Oh m-my god..."
    xsc "*Panting* AAAAHH.... AAAGWHHHH... AGGGGHHWWW!!!"
    mc "D-Don't scream so m-much, Alex..."
    mc "S-Someone's gonna hear us..."
    x "*Panting* H-How am I supposed n-not to scream when I'm... being impaled by that... {i}thing..."
    xsc "*Panting* AAAAagggwggg..." with hpunch 
    x "*Panting* Oh dear L-Lord, this feels... AMAZING..."
    mc "F-Fuck, it really does..."
    x "*Moans* AAAAahhh..."
    scene alexpool10 with dis2
    bla "Alex keeps bouncing on your lap, as if she was determined to crush you against the toilet beneath her."with dis15
    mc "AAahh..."
    mc "Y-Yeah... d-don't stop..."
    mc "K-Keep going..."
    x "*Moans* AAAAhhh...aaaAgggww...ggwwwaaah..."
    x "*Panting* Y-Yeah..."
    x "*Panting* I-I love feeling you... inside of me..."
    x "*Panting* Ohhhh... [mc]..."
    xsc "*Squeals* AAAaaaAhHHhHHwwWWWww..." with hpunch 
    bla "A rhythmic moan escapes Alex's lips each time she lets your cock sink into her, the sound reverberating through the empty locker room."
    xsc "*Panting* AAaahh... aaahhh... ahhhh... aaaaaagghhh..."
    xsc "F-Fuck... I can't..."
    xsc "I need to... t-take a break..."
    xsc "G-GgggGAAAAHH...!"with hpunch
    play sound slap1
    play sound2 squirt
    play sound6 penetration3
    scene gx 82b 
    xbt "*Panting* G-G-Gggaaahh..." with vpunchslow
    xbt "*Panting* AAAaahh..."
    xbt "*Panting* J-Jesus fucking Christ..."
    xbt "*Panting* O-Okay..."
    xbt "*Panting* G-Give me... a minute..."
    play sound3 latexgloves
    play sound4 doorslam
    scene gx 82
    bla "Without pulling out, you lift Alex to her feet and press her against the door of the cubicle, tearing off her swimsuit in the process." with dis12
    mc "I'm sorry, babe, we don't have a minute."
    mc "But don't worry, just let me handle the heavy lifting now..."
    x "*Still panting* Ahh..."
    x "S-Sounds good..."
    scene alexpool11 with dis2
    xsc "Ohh... F-FUCKKKKKkkkkkkkkkkk...!!!" with dis15
    mc "*Panting* Ohhhhh... s-so good...."
    x "*Panting* F-Fuck... YES..."with hpunch
    x "*Panting* FUCK ME HARD, [mc!u]..."
    x "*Panting* F-Fuck me as hard as you did in my apartment..."
    mc "I t-thought you said “never again”..."
    x "*Giggles* Hah... f-fuck NO..."
    x "I want this... every DAY..."
    x "I want you to come to all of my swimming practices..."
    x "And f-fuck me like... an animal..."
    mc "Y-You like it like that, don't you?"
    x "*Giggles* F-Fuck yes, I do..."
    x "*Moans* AAAAAAaaAaaaaghhh..."
    scene gx 83 with dis2
    pause .1
    show alexpool12 with dis2
    bla "Despite Alex’s futile attempts to stifle her moans, the relentless pounding against her slender body eventually shatters her resilience." with dis12
    xsc "*Squeals* AAahhh... aaaaahhh... aaAAAAaGggghh... AAAAHHHHH..."
    mc "*Panting* AAAAaghh..."
    mc "*Panting* Oh dear God, y-you're the fucking best..."
    mc "*Panting* Y-You're taking every inch like a master..."
    xsc "*Moans* AAahhh... a-am aaahh...I...?"
    mct "God..."
    mct "Who would've thought I'd be dominating Alexandra Bardot like this when we first met..."
    xsc "*Panting* AAAAhhh..."
    mct "Fuck... this position brings out my animal side..."
    mct "My balls are gonna explode..."
    mc "A-Alex..."
    xsc "*Panting* Hah... y-yes..."
    xsc "*Panting* You have... permission... to cum..."
    xsc "*Panting* F-F-Fill me up..."
    xsc "*Panting* F-Fill me up with everything you have..."
    mc "O-Ohhh yeah..."
    mc "Agghhh... I'm gonna cum so much..."
    mc "I'm almost there..."
    mc "Oh Alex..."
    mcsc "I'm cumming!!" with hpunch
    play sound teleport2
    scene teleport84
    pause .5
    play soundloop2 night
    mcsc "AAAAAAGHHH!!!" with hpunchlong4
    play sound2 ["<silence 0.2>", fall3]
    play sound3 debris
    scene gx 85
    x ". . ." with dis
    x "Wha..."
    x "WHAT...?!"with hpunch
    x "What the fuck just happened?! Where are we?!"with hpunch
    mc "Oh, crap..."
    mc "We... we entered Eternum."
    x "WHAT?!" with hpunch 
    show gx 86
    mc "Holy cow... we're in Semper Invicta's rotunda..." with dis12
    x "WE'RE... WHERE?!"
    mc "I-I already explained to you everything that happened to me in that alley... and how I can access servers I’ve been to before without using the neural implant."
    x "Well... y-yeah, but you didn't mention you do that while having sex!"
    mc "T-That wasn't intentional. Sorry, I still have to learn how to control it better."
    x "Jesus..."
    show gx 87
    x "A-Anyway... w-we need to go back to the real world." with dis15
    x "L-Let me down."
    mc "Damn..."
    mc "This pose is hot as fuck, Alex, not gonna lie..."
    x "W-What...?"
    x "Sh-shut up and let me do–"
    scene alexpool13 with dis2
    x "G-gG-GGGggggghhhh..." with dis15
    x "W-What the f-fuuuucckk are you doin', you idiot..."
    mc "Oooohhh..."
    mc "Oh my god, this position feels so good..."
    mc "It feels so tight..."
    x "I s-said... let m-me... downnnn..."
    x "*Moans* AAaahhh..."
    x "*Panting* F-Fuck, it {i}does{/i} feel good..."
    mc "Hah... r-right...?"
    x "*Panting* But w-we need to..."
    x "*Panting* G-Go back..."
    xsc "*Squeals* AAAAAGHH......." with hpunch
    x "*Panting* . . ."
    x "*Panting* F-FUCK."
    x "*Panting* Is this..."
    x "*Panting* I-Is this place... safe...?"
    mc "W-Why do you ask...? You don't want me to stop anymore...?"
    xsc "*Moans* Mmmmmmhhhwwwgg..." with hpunch
    mc "I'll take that as a “keep fucking me, [mc]”..."
    xsc "F-FUCK ME..."
    mc "AAAAAagghHHHH yeah..."
    stop soundloop2 fadeout 1
    play sound teleport2
    scene teleport85
    pause .5
    x "*Panting* AAaahhh... ahhhh... aaahhh..." with dis12
    x "*Panting* OH MY GODDD..."
    x "*Panting* W-Where the hell are we now...?"
    mc "*Looking around* Ehh..."
    mc "T-The Collector's house..."
    x "*Panting* AAahhh... there's a f-fucking robot over there..."
    mc "Y-Yeah... I hope it's really turned off and not secretly recording us..."
    x "*Panting* AAaa-ha... that would be so fucking hot, w-wouldn't it...?"
    mc "Oh my, Alex..."
    mc "You're a dirty little slut deep down, aren't you...?"
    x "*Panting* Hah..."
    mc "What would your daddy say if he heard you saying these things...?"
    x "*Panting* Haha..."
    x "*Panting* I-I don't know, and I don't care..."
    x "*Panting* You..."
    x "*Whispering* You're my daddy now..."
    mct "SHE DID NOT SAY THAT..."
    play sound teleport2
    scene teleport86
    pause .5
    bla "As you sense the climax drawing near once more, Alex begins to thrust her hips against yours, her thighs tightening around your torso, intensifying the pleasure beyond anything you thought possible." with dis12
    xsc "*Squeals* AAHHH.... AHHHH.... AAAAGGHHW!!!!!"
    xsc "F-Fuck... I'm cumming...!" with hpunch
    mcsc "Sh-Shit... me too..."
    mcsc "Oh, Alex..."
    xsc "[mc]..."
    xsc "Aaaahh... aaahh... ahhhhhhhggg..."
    xsc "YEAH..."
    xsc "YEAH, RIGHT THERE..."with hpunch
    xsc "FOR THE LOVE OF GOD, DON'T STOP NOW..."with hpunch 
    xsc "AAAAAAAGGHHH..."with hpunch 
    xsc "RIGHT THEREEEE..."with hpunch 
    play sound teleport2
    scene teleport87
    pause .5
    play sound4 doorslam
    play sound5 fall3
    play sound6 squirt
    xsc "{size=45}AAAAAAAAWAAAGHHHHHHHH!!!" with hpunchlong3
    play sound7 squirt
    bla "Alex's body convulses in a violent orgasm, her vaginal walls clenching tightly around you for several seconds." with hpunch 
    xsc "A-A-AaAaAahhh..."
    play soundlow ["<silence 3.5>", splashpool] volume 0.1
    play sound2 ["<silence 2.1>", poolwhistle] volume 0.3
    play sound3 ["<silence 0.9>", fallfull] volume 0.5
    scene gx89 
    bla "She collapses onto the floor, her body still trembling." with dis
    xbt "Ga-gagg-g-g-ghhh..." with dis
    play sound7 whoosh3b
    play sound6 grab2
    scene gx 90
    mc "*Pulling her hair* Bring that pretty face of yours here..." with hpunch
    play sound whoosh3b
    play sound2 debris3
    play sound8 cumfacial
    scene alexpool16pr with hpunch 
    pause 11.1
    play sound3 ["<silence 0.7>", fallfull] volume 0.4
    stop music3 fadeout 20
    play soundloop3 poolambiance fadein 13
    scene gx 91 with dis08
    show gx 91 with vpunchslow
    x "Mmmmmhhh..." with dis
    mc "O-Oohhhhh yeah..."
    x "Mm-mmh..."
    show gx 92
    x "*Catching her breath* You're... such a fucking pig..."
    show gx 91
    mc "*Chuckles* Says the girl sitting on the bathroom floor covered in cum."
    show gx 92
    x "For your information, the locker room was just disinfected this morning, and no one else has been in here since then."
    show gx 91
    mc "And what about the {i}covered in cum{/i} part?"
    x "*Snorts* Mmph."
    show gx 92
    x "Yeah... I guess I don't have an excuse for that one."
    show gx 91
    mc "*Chuckles* So I thought..."
    show gx 92
    x "Is it always gonna be like this...?"
    show gx 91
    mc "Well... we’ll probably have to tone it down by the time we’re 60."
    show gx 92
    x "*Snorts* Ahh..."
    x "Yeah, I can live with that."
    show gx 91
    x "*Taking a deep breath* Hmphh...."
    $ renpy.end_replay()
    play sound debris
    play sound2 clothes3b
    play music alexloveguitar fadein 6
    show gx 94
    bla "You gently lift Alex from the floor and settle her onto your lap." with dis22
    show gx 95 
    mc "Damn..."
    show gx 93
    x "Damn indeed."
    show gx 94
    mc ". . ."
    x ". . ."
    mc ". . ."
    show gx 93
    x "*Giggles* What?"
    x "Do I have something on my face or what?"
    x "If you think you can beat me in a staring contest, think again."
    show gx 95
    mc "Can't a man simply admire how beautiful a girl is in silence?"
    show gx 93
    x "Ooohhh... so that's what it is."
    x "Tell me, is it the smell of bleach from the floor or the jizz on my face that's dazzling you?"
    show gx 95
    mc "Well, technically the second one's just the expression of our love, so..."
    show gx 95b
    x "*Snorts* Oh, fuck off already with your flowery bullshit."
    show gx 93
    x "No way you're actually trying to turn {i}this{/i} into a romantic shitshow."
    show gx 95
    mc "Are you referring to the wild dance of desire that just took place in here?"
    show gx 93
    x "*Giggles* Cut the crap. Last warning."
    show gx 95
    mc "Hey, I’m just giving you the royal treatment you deserve."
    mc "Can you really blame me for that?"
    show gx 93
    x "Oh, so I'm a princess now?"
    show gx 95
    mc "Of course!"
    mc "Or you think princesses don't like to be drilled against the headboard of their beds too from time to time?"
    show gx 95b
    x "*Giggles* Well... Princess Elsa does look like a vicious nympho, that's true."
    show gx 95
    mc "You are my princess, Alex."
    mc "And I'll always treat you like one."
    mc "During the day, at least."
    show gx 93
    x "Oh... and what about at night?"
    show gx 95
    mc "Ah, well..."
    mc "I'll leave that up to you..."
    show gx 94
    x "Mmmmh."
    show gx 93
    x "*Whispering* That sounds pretty good..."
    show gx 95b
    x "But anyway... as much as I’m enjoying your cringe-fest, we really need to get going. I told my coach I’d be back in 10 minutes, and I’m pretty sure it’s been at least 20."
    show gx 96
    mc "Yeah... and about this mess..." with dis
    mc "Should we clean the floor before we leave?"
    show gx 97
    x "Yeah, I'll give it a quick wipe, don't worry."
    scene gx 96
    mc "Shit, sorry about it."
    mc "Although... well, at least it's “safer” than... you know."
    scene gx 97
    x "Yeah, well... I don't think that matters anymore."
    scene gx 98
    mc "Huh? What do you mean?" with dis12
    show gx 99
    x "Um..."
    x "N-Nothing, forget I said anything."
    x "It's just something that... I'll handle myself."
    show gx 98
    mc "Hey, if it's your problem, then it's mine too."
    mc "I'm here to help you with everything I can."
    x ". . ."
    show gx 99
    x "Uh..."
    x "*Sighs* Okay..."
    x "Um... remember the night we spent together in my apartment?"
    show gx 98
    mc "Of course, how could I forget?"
    show gx 100
    x "And... remember how you, uh... finished inside? Several times...?"with dis14
    mc "Of course..."
    x "Well... turns out we pushed our luck too much."
    x "I'm..."
    x "I'm pregnant."
    mc "Oh."
    stop music
    play sound impact3
    play sound2 deception
    scene alexpregnantgray with dis
    menu:
        with dis
        "That's amazing! [alex_pts]":
            $ alexhappypregjoke = True
        "Panic":
            $ alexhappypregjoke = False
    mc "You're..."with dis
    play sound slam
    play sound2 ceramichit
    play sound3 debris3
    if alexhappypregjoke:
        play music alexloveguitar fadein 3
        show gx 101
        mcsc "WHAT?!" with hpunch 
        mcsc "That's... a-amazing! No fucking way!" with hpunch
        mcsc "Oh my god, is this r-really happening?!" with hpunch
        mcsc "But... how will we... n-nevermind, we'll figure it out!" with hpunch
        mcsc "That's... AMAZING!" with hpunch
        mcsc "If it's a boy, can we name him–"with hpunch 
    else:
        play soundlow risinglong
        show gx 101b
        mcsc "WHAT?!" with hpunch
        mcsc "Oh my god, what?!" with hpunch
        mcsc "That's... t-terrible! TERRIBLE TIMING!" with hpunch
        mcsc "What are we gonna do?!" with hpunch
        mcsc "Do you have to g-get an a-abortion now?" with hpunch
        mcsc "F-Fuck, is it even legal in this state?!" with hpunch
        mcsc "THAT'S... {b}TERRIBLE!"with hpunch 
        mcsc "And what if–"with hpunch 
        stop soundlow fadeout 4
        play music alexloveguitar fadein 3
    show gx 102
    x "W-Whoa, whoa, chill, buddy." with dis14
    x "I-It's a joke. I was kidding."
    mc "Ehh??"
    x "I'm not pregnant."
    mc "Oh..."
    if alexhappypregjoke:
        show gx 105
        mc "W-What the hell is wrong with you?"with dis15
        mc "Why would you joke about something like that?"
        show gx 106
        x "Um... w-well, I thought you would... react... differently."
        show gx 105
        mc "That was a terrible joke."
        show gx 106
        x "I... I know. I'm sorry."
        x "Did you... did you say... “amazing”...?"
        x "You were happy about this?"
        show gx 105
        mc "I mean, it was probably not the best timing, but... of course, my first reaction was happiness."
        show gx 106
        x "Why...?"
        show gx 105
        mc "What do you mean, why?"
        mc "Because I love you, silly."
        show gx 106
        x "You... love me...?"
    else:
        show gx 103
        mc "What the actual fuck is wrong with you?"with dis15
        mc "Why would you joke about something like that?"
        show gx 104
        x "Yeah, well, if you actually panic so easily, you should stop cumming inside women, you know?"
        x "It's basic biology."
        show gx 103
        mc "That's a different issue."
        mc "It was still a bad joke."
        show gx 104
        x "Yeah, I got that already."
        x "You shouted “TERRIBLE” like six times."
        show gx 103
        mc "How was I supposed to react?"
        show gx 104
        x "I don't know, but–"
    play sound dooropenclose2
    play sound2 dooropenclose2
    show gx 107 with dis15
    x "*Whispering* Shit, was that the main door?" with dis12
    play sound clothes3b
    scene gx 108
    x "*Standing up* F-Fuck, where's my swimsuit?!" with dis15
    mc "*Whispering* Over there."
    x "*Whispering* Oh, thank god."
    mc "*Whispering* Should I sneak out?"
    x "*Whispering* NO! YOU STAY HERE!"
    mc "*Whispering* B-But my clothes are outside."
    x "*Whispering* Ehh? Fuck!"
    x "*Whispering* Let's hope she doesn't see them..."
    scene gx 109 with dis2
    pause
    scene gx 110
    bla "Alex's swimming coach scans the locker room, her grunts audible from the other side of the room." with dis14
    swim "Mmmmrhh..."
    show gx 113
    swim "Hello?" with dis12
    swim "Alexandra? Are you in the toilet?"
    play sound4 whoosh3b
    play sound3 debris3
    show gx 114
    x "*Sprinting to her* Coach!" with pr
    x "I'm so sorry for the delay!"
    show gx 111
    swim "You've been here the whole time?! What the hell happened?"
    show gx 115
    x "Uh... well, after my boyfriend left, I had a... little setback."
    mct "Did she call me her “boyfriend”?"
    mct "Nice..."
    show gx 114
    x "But I'm ready to jump back into the pool!"
    show gx 112
    swim "A setback? What kind of setback?"
    show gx 115
    x "Uhhh..."
    x "I had..."
    x "A sudden attack of..."
    show gx 114
    x "Explosive diarrhea."
    x "Wouldn't recommend it to anyone."
    show gx 112
    swim "Oh, damn... really?"
    swim "You should probably go home, then."
    show gx 114
    x "No, no! I feel like a new woman now!"
    x "Ready to keep going!"
    show gx 112
    swim "Oh... well, alright, if you're sure about that..."
    swim "Okay, let's go."
    show gx 113
    swim "Should we... tell the staff what happened? Is the toilet dirty?"
    show gx 114
    x "NO! N-NO STAFF!" with hpunch
    show gx 115
    x "I'm... so embarrassed about it. Please don't tell anyone, and let me clean it up myself after training."
    show gx 116
    x "There was, like... you know, shit everywhere!"with dis
    xsc "It was like KA-BOOOM!" with hpunch 
    x "The walls, the seat, even the ceiling – EVERYTHING is covered!"
    show gx 113
    swim "O-Okay, I get it, I get it... I'll let you clean it up yourself."
    swim "No need to be so descriptive, jeez."
    show gx 117
    swim "Alright, let's go then." with dis15
    swim "If you're really convinced your... digestive troubles are solved, back to the water!"
    x "Yes, ma'am!"
    if alexhappypregjoke:
        x "Although... can I go get something I forgot in there first?"
        swim "*Sighs* Yeees, but hurry up."
        x "Thanks!"
        play sound footsteps
        play sound2 ["<silence 2>", wood2] volume 0.27
        scene gx 118
        bla "You hear Alex's footsteps approaching the toilet where you're still hiding." with dis22
        mct "Hmm?"
        show gx 119
        mc "*Whispering* Alex?" with dis17
        mc "*Whispering* Is there anything wrong?"
        x ". . ."
        $ alex_points += 1
        play sound beat
        show screen heartbeat
        show gx 120
        x "*Whispering* I love you too." with dis
        play sound3 run
        show gx 121 with dis17
        pause
    stop music fadeout 18
    scene gx 122 
    play sound dooropenclose2 fadein 1
    bla "You hear Alex and her coach exiting the locker room." with dis22
    if alexhappypregjoke:
        mct "Damn, man..."
        mct "Those words hit better than anything else we did today."
        mct "This girl is definitely one of a kind, no doubt about it."
        mct "What a trip..."
    else:
        mct "Phew... that was close."
        mc "*Taking a deep breath* (Damn, boy...)"
        mct "That was a “quickie” like non other, that's for sure."
        mct "This girl is certainly irreplaceable."
    play sound vibration
    play sound2 vibration
    bla "{sc=2}Your phone buzzes.{/sc}"
    mc "Hmm?"
    mc "(Oh shit, it's Dalia, right! I'm late!)"
    if daliameme:
        call chat(dalia_chat3) from _call_chat_22
    else:
        call chat(dalia_chat3b) from _call_chat_23
    mct "Shit, it's already 12:40!" with dis08
    mct "Alright, time to flee!"



label daliavalley:
    stop soundloop3 fadeout 6
    stop music fadeout 6
    scene black with dis27
    show screen afewminuteslater with dis22
    pause
    play soundloop rain5 fadein 3
    hide screen afewminuteslater
    scene gb 1
    with dis3
    play sound5 thunder fadein 2
    mc "*Shivers* (Ughh-huh... holy shit, it's starting to get WAY too cold...)" with dis15
    play sound2 sneeze
    mc "*Sneezes*"with vpunchslow
    mct "U-Ugh... I can feel a cold coming on."
    play sound3 dogfar
    mct "We were just in shorts a couple of weeks ago, what the hell happened?"
    mct "This fucking weather is crazy..." 
    play sound carpasswet
    scene gb 2 with dis2
    mct "Hmm... ah, there she is!" with dis15
    mct "Heh, at least I’ve got someone to suffer through the cold with me."
    $ unlock_look("dalia", 13)
    play music2 chillmusic fadein 5
    show gb 3 with dis15
    mc "You’re gonna get sick if you keep wearing that in this weather, girl." with dis15
    show gb 4
    d "Hmm?" with dis08
    play sound3 chair2
    show gb 5 
    d "*Standing up* FINALLY!" with dis14
    d "Do you have any idea how long I’ve been waiting out here in this freezing weather? It's like... 50 degrees today!"
    show gb 6
    if alexpoolvisit:
        mc "I know, I know!"
    else:
        mc "Y-Yeah, I know I'm late, sorry about that. I was stuck with Nikolay for a while talking about..."
        mc "Well, I honestly didn't understand a damn thing, but he seemed very passionate about it."
    mc "I'm sorry!"
    d "*Grumbles* Mmh."
    mc "It won't happen again."
    d "*Grumbles again* Mmmh."
    mc ". . ."
    mc "Do you forgive me...?"
    if daliapath:
        d ". . ."
        show gb 7
        if daliaproteinbuy:
            d "Well... you're lucky you got me that protein earlier." with dis
        else:
            d "Well... you're lucky a hot dog vendor passed by while I was waiting for you." with dis
        d "I'm in a good mood."
        d "So yes, I forgive you."
        show gb 8
        mc "*Chuckles* Thank you."
        if daliaproteinbuy:
            mc "I'm gonna have to buy you a new pot every month."
            show gb 9
            d "Obviously. I expect no less."
            show gb 8
            mc "*Chuckles* But seriously though, why are you braving the cold winds out here like that?"
        else:
            mc "But seriously though, why are you braving the cold winds out here like that?"
        mc "Not that I’m complaining about getting a peek at that sexy stomach, but aren’t you worried about catching a cold?"
        show gb 10
        d "Yeah, I know... I thought I’d just be going straight home after the gym, so I figured a sports bra and this mid-season jacket would do the trick."
        show gb 11
        d "But... I was obviously wrong."
        show gb 9
        d "I suppose it's finally time to pull the thick coat out from the wardrobe."
        d "Winter has finally arrived in Kredon."
        show gb 8
        if alexpoolvisit:
            mc "Tell me about it – I was at the heated pool for so long, I didn’t even notice how cold it got outside."
            mc "Stepping out was like getting slapped in the face."
            show gb 10
            d "Oh yeah, now that you mention it... how was Alex's “special massage”?"
            show gb 11
            d "Is she better?"
            show gb 12
            mc "Uh..."
            mc "I-I'm sorry...?"
            mc "What... w-what special massage?"
            play sound3 carpasswet
            show gb 9b
            d "Um... did I get it wrong? She was texting me right before you showed up." with dis14
            d "Yeah, here. That's what she told me just now."
            show gb 9c
            mct "What the hell, I thought she was supposed to be swimming!"
            show gb 9b
            d "She said... she had a small back injury like me a few weeks ago, but mentioned you gave her one of your massages. Apparently, she feels like a new woman now."
            show gb 9c
            mc "A-Aha."
            show gb 9b
            d "She also said you’ve learned a new amazing technique... and suggested you should try it on me too."
            d "Or... maybe a double session with both of us."
            show gb 9c
            mc "HAHA! You sure want to exploit me, huh??"
            mct "What the hell is wrong with Alex?!"
            mct "Is she for real, or is she just trying to mess with me like always?!"
            d ". . ."
            mc "Um... but sure, yeah!"
            mc "I-I'd love to have a... physiotherapy session with... you."
            mc "I'd really love it..."
            show gb 9
            d "Neat!" with dis14
            d "I'll schedule it with her, then."
            show gb 8
            mc "C-Cool!"
            mct "Heh, this will likely end up really bad for Alex for messing with me."
            mct "Or... well, it could also end up... {i}really well."
            mc "*Clears throat* Anyway, so... the mission!"
        else:
            mc "Was about time!"
            mc "But hey, I don't know about you, but with this cold I feel more like going to the Valley of the Kings server."
            mc "Don't you think?"
            show gb 9
            d "*Chuckles* That's true."
            show gb 8
    else:
        show gb 5
        d "No."
        show gb 6
        mc "Oh, come on..."
        mc "Don't be like this..."
        mc "Pleeeeaseeee..."
        d ". . ."
        show gb 11
        d "*Sighs* Fine, whatever, okay. You're forgiven." with dis 
        show gb 12
        mc "Yay!"
        show gb 11
        d "Let's just focus on the mission, shall we?"
        show gb 12
        mc "Hell yes!"
    mc "Time to go into the desert!"
    mc "What's the plan?"
    show gb 9b
    d "Well... we were supposed to meet Samir, our contact in the server who was going to help us get into Hassan al-Rashid's citadel, at... 1 PM."with dis14
    d "But we missed our bus, and the next one doesn't come until... *checking Ulysses Maps* ...1:30 PM."
    show gb 9c
    mc "Fuck."
    mc "Is there any way we can let him know we're gonna be late?"
    show gb 9b
    d "Well... Jerry's offline, so he's probably already there."
    show gb 9c
    mc "Oh... FUCK. I totally forgot Jerry was joining us."
    mc "He's gonna fuck it up. Big time."
    show gb 11
    d "It was {i}you{/i} who suggested bringing him along." with dis14
    show gb 12
    mc "I know. He's been in the server before, and he proved to be useful in our trench warfare against Wagner's men."
    mc "BUT only if he's with us. If he's on his own, he's gonna get himself killed and blow up the whole mission."
    show gb 11
    d "So... what do you suggest?"
    show gb 12
    mc "Hmm..."
    mc "Well... now I don't really need any equipment to enter Eternum."
    mc "And I checked the meeting point just yesterday."
    mc "So... I’m pretty sure I could take the express route. And... well, technically, I can bring someone along with me, so..."
    show gb 13
    d "Whoa, whoa, whoa!" with dis12
    d "You want me to join Eternum... with you? With my REAL BODY?"
    show gb 14
    mc "I-It was just an idea!"
    mc "But... yeah, you're right, that was stupid. It could be dangerous for you."
    mc "Sorry, I don't even know why I brought it up. Was just an impulse."
    show gb 12
    d "Hmmmm..." with dis14
    show gb 10
    d "Yeah, you're right... Nova just went on a real-body adventure with you a few days ago. She’d totally think I’m a coward if I refuse."
    d "And then she'd probably go and tell everyone, and the whole team would think I'm a total wuss."
    show gb 12
    mc "That thing with Nova was an accident, and... what do you mean, “you're right”...? I didn't imply anything remotely close to what you said."
    show gb 11
    d "Okay, let's do it."
    show gb 12
    mc "Wait, what?!"
    mc "Seriously??"
    show gb 11
    d "Totally."
    show gb 12
    mc "You sure...?"
    mc "If we got hurt somehow – knock on wood – you'd bring those injuries back to the real world."
    show gb 11
    d "I'll take that risk."
    d "I mean, can we even say that logging in using Ulysses' neural implant is the “safe” way to enter Eternum?"
    d "For all we know, the Founder could be cooking up some secret plan behind the scenes and turn us all into brainless NPCs at any moment."
    show gb 12
    mc "Hmm... well, if you put it like that... that's a solid point."
    show gb 10
    d "A Gem of Doom is on the line here. We can't let this chance slip away."
    show gb 11
    d "And besides, it should be relatively safe anyway."
    d "No one even knows we're going there except for Samir."
    show gb 12
    mc "Hmm... well..."
    mc "I’m not sure why I'm the one that needs convincing for an idea I came up with, but I'll admit you’re making sense..."
    show gb 11
    d "Plus, the murder rate in the Valley of the Kings is really low – less than 15 homicides per 10,000 players."
    d "It's basically as safe as going on a weekend trip to any major city."
    show gb 12
    mc "Probably safer, if you also consider the chances of dying in a car accident."
    show gb 9
    d "*Chuckles* Now you're on my same wavelength!"
    show gb 8
    mc "Okay, let's do this, but if we say we're leaving, we're leaving!"
    mc "The best part about entering Eternum this way is that we don’t need an Exit Portal to escape, so we actually have the upper hand there."
    show gb 9
    d "Got it!"
    show gb 8
    mc "Alright then..."
    mc "Let's find a discreet corner. Follow me."
    play sound4 thunder fadein 2
    show gb 15 with dis25
    bla "You lead Dalia towards a nearby alley." with dis22
    mc "Alright, let's find a spot under one of those balconies."
    d "Whenever we leave Eternum, are we gonna come back to this same place?"
    mc "Yep. That's all I can manage for now."
    d "Sounds good. Hopefully it won't be raining by then."
    play sound2 ["<silence 2.2>", dogfar]
    play soundlow carpasswet volume 0.6
    play sound5 water3
    if daliapath:
        show gb 16 with dis22
    else:
        show gb 17c
    bla "You both slip into a blind spot beneath a fire escape, leaving your umbrellas at your side as you wrap your arm around Dalia's waist." with dis2
    if daliapath:
        show gb 17
        mc "*Taking a deep breath* Alright..." 
        mc "Now close your eyes."
        mc "I just need a moment to concentrate."
        show gb 17b
        d "*Closing her eyes* Okay." 
        stop music2 fadeout 16
        show black 
        d "Is this really necessary, though?" with dis12
        mc "You mean the eyes?"
    else:
        mc "*Taking a deep breath* Alright..." 
        mc "Now close your–"
        stop music2 fadeout 16
        show black 
        play sound slap3
        play sound2 slap1
        d "*Slapping you* If you really have to touch me, hands on the shoulder." with hpunch
        mc "O-Okay, okay, jeez..."
        mc "Just c-close your eyes."
        d "Is it really necessary?"
    mc "Not really for you, but it’ll definitely help you avoid the shock."
    d "Oh... alright then."
    mc "*Inhaling* . . ." with dis14
    stop soundloop fadeout 15
    mc "*Exhaling* Fuuu..." with dis14
    bla ". . ."
    play sound teleport2
    play sound2 deception
    show teleportdalia1
    stop music2
    stop soundloop
    play sound3 wind4
    pause
    scene gb 18 with dis25
    play music2 arabia1 volume 0.8
    mc "*Squinting your eyes into the sun* Oh yeah..." with dis2
    mct "OH HELL YEAH! I'm making progress!"
    if alexpath:
        mct "I mean, I teleported to three different realms with Alex just a few minutes ago."
        mct "Sure, it was unwillingly, but I still managed to get exactly where I wanted this time, with no exhaustion at all."
    mct "Can't wait to tell Calypso about my evolution."
    show gb 19
    mc "*Squinting your eyes again* Holy cow... it's scorching out here." with dis15
    mc "This sudden temperature change can't be healthy."
    mc "Agh, we need to find some shade soon, or the sun's gonna roast us alive."
    d "Wow..."
    show gb 20
    mc "*Turning around* Hmm?" with dis15
    d "You really did it." 
    d "This is... crazy!" 
    d "I mean, it still feels the same as always, but... we really made it in without the neural implant!"
    play soundlow whoosh3b
    play sound2 debris3
    show gb21
    d "You even brought us next to the Exit Portal!" with pr
    mc "Yeah, this little spot around the Exit Portal is the only area I’ve been on this server, so it’s the only place I can access."
    if maatsex:
        mc "And..."
        mc "Well, I did visit a small temple with Nova on the other side of the desert too, in the Egyptian area."
        mc "B-But... that’s a story for another time."
    d "This is so cool! We should enter Eternum like this every time!"
    d "Only that..."
    scene gb 22
    d "W-With this method we actually have to enter Eternum with our Earth clothes, I didn’t think about that." with dis14
    d "Good grief..."
    d "Suddenly this little jacket makes me feel like I'm stuck in an oven."
    show gb 23
    mc "Yeah... I know."
    mc "We have no access to any of Ulysses' “trickery” anymore. No inventory, no Exit Portals... nothing."
    show gb 22
    d "I see..."
    show gb 23
    mc "Do we have anything we can wear?"
    play sound clothes5b volume 0.66
    show gb 25
    d "*Taking off her jacket* Actually, yeah, I left a couple of Ishari outfits for us stashed at the meeting point." with dis15
    show gb 24
    mc "Ishari outfits?"
    show gb 25
    d "The desert-dwelling tribe that Samir, our contact, is a member of."
    d "We’ve gotta blend in like them if we want to get close to the citadel without raising any suspicion."
    d "Plus, their outfits are designed to handle the heat, so it’s a win-win."
    show gb 24
    mc "Oh, gotcha."
    mc "Alright then! Let's get to that meeting point before we turn into puddles."
    show gb 25
    d "Let's go. We just need to head East for about 15 minutes."
    d "Jerry should already be there if he’s still breathing."
    show gb 24
    if daliapath:
        mc "*Checking her out* Mm-hm."
        mc "Sounds good..."
        mct "Goddamn, man... with all that sweat glistening on her skin, her stomach looks like a statue of a goddess."
        d "Hmm?"
        mc "Your abs are looking good, Dalia."
        show gb 25
        d "What?"
        show gb 26
        d "Who, me...?" with dis17
        d "I don't know why you’d say that, I didn’t even train them today."
        bla "Dalia flexes her muscles, arching her back to accentuate their definition."
        mc "*Chuckles* You know just how hot you are, don’t try to play coy with me."
        d "You really think so...?"
        d "Hmm, I guess I'm just too humble to notice..."
        show gb 27
        d "But it's true that I've put on almost four pounds of muscle over the last three weeks, so maybe you're onto something..." with dis17
        d "Must be the new diet."
        show gb 28
        mc "How do you manage to not gain a pound of fat?"
        mc "I've seen you devour a whole chicken for dinner."
        show gb 27
        d "It's all about balancing weight training with cardio."
        show gb 28
        mc "Ah, interesting..."
        mc "Care to share how you keep up with your cardio to stay that lean?"
        show gb 27
        d "I don’t think you need my advice, considering how cut you are as well, but... sure, I can keep you entertained on our way to the meeting point."
        show gb 28
        mc "*Chuckles* I'm all ears."
    else:
        mc "Sounds good."
    scene gb 29 with Dissolve(3.3)
    bla "You and Dalia walk under the blazing sun for a few minutes until you arrive at a small oasis, nestled around a crystal-clear pond." with dis22
    mc "Whoa... this place looks beautiful."
    d "Right? Told you!"
    show gb 30 with dis2
    mc "Look at these plants... how can they even grow in the middle of the desert?" with dis12
    d "The Ishari probably take care of them, although the pond is naturally formed, as far as I know." 
    d "But come, come! Our outfits are–"
    je "Well, well, well... look who finally decided to show up."
    show gb 31
    mc "Hmm?" with dis
    mc "Oh! Hey, Jerry!"
    mc "Sorry for being late, man – we got caught up with something."
    je "Hmph."
    play sound metalhit2
    play sound3 hit2
    play sound2 debris3
    show gb 32
    bla "Jerry dramatically sticks his sword in the ground." with hpunch
    je "Hmph."
    show gb 33
    je "*Chuckles* They got... caught up with something." with dis15
    je "Of course."
    show gb 35
    mc "Yeah... sorry about it."
    show gb 33
    je "Do you have any idea what the temperature is like in the sun here?"
    show gb 35
    mc "Um..."
    mc "I mean, you could have found some shade."
    show gb 34
    d "Yeah, cut the crap, Jerry – did our contact come already or not?"
    show gb 33
    je "Samir sent a letter with one of his hawks."
    je "He said he had to push back our meeting by 40 minutes."
    show gb 36
    d "Oh? Really?!"
    d "That's neat! I thought we'd be the ones being late!"
    show gb 37
    d "Alright then, in that case I'm gonna go get into the Ishari outfit."with dis
    d "You should do the same before Samir shows up – we’ve gotta look professional!"
    d "A deal with the WRE is involved, and I really want to make Mom proud."
    show gb 38
    mc "Sure thing! I'll get right on it too."
    show gb 37
    d "See you in a minute!"
    show gb 35
    mc "Where did you leave the other male outfit, Jerry?" with dis14
    show gb 33
    je "Our contact is late, Dalia's late, you are late."
    je "And no one gives a damn fuck about me."
    show gb 35
    mc "Oh come on, we already apologized."
    mc "And we do give a damn. I wouldn't have invited you to join the mission otherwise."
    show gb 33
    je "People used to bow before me, [mc]."
    je "They used to tremble when they heard the name of Sir Jermaine of Noriander."
    je "And what have I become?"
    je "A clown. A meme. A buffoon people mock."
    show gb 35
    mc "Now you're just being dramatic."
    show gb 33
    je "Am I just meant to accept it and cry like a defeated man?"
    je "Assume that I'll never be a great Eternum player again?"
    je "Please, tell me."
    show gb 35
    mc "Um..."
    mc "No...?"
    je "Hmph."
    show gb 33
    je "I'll tell you what I'm {i}not{/i} gonna do, [mc]..."
    stop music2
    play sound3 hit2
    play sound2 metalhit2
    show gb 32 with hpunch
    pause
    play music combat1
    play sound debris3
    play sound4 sword3
    play sound5 metalhit2
    play sound6 whoosh6
    play sound7 hit2
    show gb39
    je "{sc=2}I WON'T LET MYSELF BE DISRESPECTED ANY LONGER!{/sc}"with hpunch 
    je "{sc=2}THIS JOKE... {w=0.2}{size=45} ENDS... {w=0.2}{size=65}TODAY!{/sc}"
    mc "Please, don't do this."
    scene gb 40
    je "Once I defeat [nickname] in combat, everyone will finally realize how..." with dis12
    je "How..."
    mc ". . ."
    je ". . ."
    je "Huh...?"
    play soundlow metalhit2
    play sound2 debris3
    play sound3 clotheswhoosh
    stop music
    play music2 arabia1 volume 0.8
    scene gb41
    je "Holy smokes!" with hpunch
    je "S-Since when are you so damn shredded?"
    mc "W-What...?"
    je "Size, shape, proportion, conditioning, symmetry... you have everything!"
    je "You son of a bitch!"
    mc "Oh..."
    mc "Um... well, thanks, bro."
    je "I’ve been hitting the gym like a madman for the past four months and haven’t seen any changes!"
    je "WHY?!" with hpunch 
    mc "Uh..."
    mc "I-I don't know, man, maybe you're overtraining?"
    show gb 42
    je "Ah... overtraining, huh..." with dis14
    je "That's actually a possibility."
    show gb 43
    mc "Were you seriously thinking about attacking me?"
    show gb 44
    je "Oh, not really. I was just putting on a theatrical display of my combat mindset and unbreakable resolve."with dis
    je "My therapist said I need to express my feelings more intensely."
    je "Please, don't mind it."
    show gb 45
    mc "I see..."
    mc "Well, as long as it helps."
    show gb 42
    je "Seriously though, you look so damn aesthetic."with dis
    je "How much do you bench?"
    show gb 43
    mc "Uh... I think my last one-rep max was 269."
    mc "But it could be more nowadays, I haven't tried in a while."
    show gb 42
    je "And what supplements are you on? I'm only using protein, creatine, BCAAs, beta-alanine, glutamine, multivitamins, and L-carnitine."
    show gb 43
    mc "I... usually just eat whatever Nancy cooks."
    show gb 42
    je "Would you share your muscle routine with me?"
    je "And how many rest days do you take each week?"
    je "Should I be doing cardio? Or I save that for when I'm cutting?"
    show gb 43
    mc "L-Look, I’d love to chat about gym stuff with you, Jerry, but I really need to get into that Ishari outfit."
    show gb 44
    je "Ah, absolutely! Please, follow me." with dis
    je "We can continue talking about it while you change!"
    show gb 45
    mc "Uhh..."
    mc "*Sighs* Sure."
    mct "Oh god, this new gym bro phase of Jerry is going to be even more annoying than his last version, which is saying something."
    mct "Someone save me..."
    stop music2 fadeout 9
    scene black with dis27
    show screen afewminuteslater with dis25
    pause 
    play sound6 wind4 fadein 3
    scene gb 30 
    hide screen afewminuteslater
    with dis27
    play music2b arabia2 fadein 5
    mc "*Panting* G-GgghHhh..." with dis15
    play soundlow leathershort
    play sound2 ["<silence 1.4>", leathershort] volume 0.5
    if daliapath:
        mc "*Panting* T-Two hundred n-ninety-eight..." 
    else:
        mc "*Panting* O-One hundred e-eleven..." 
    show gb 47
    mc "*Panting* F-Fuck..." with dis17
    if daliapath:
        mc "*Panting* C-come on... just two more..."
    play soundlow leathershort
    play sound2 ["<silence 1.4>", leathershort] volume 0.5
    show gb46
    if daliapath:
        mc "*Panting* Two hundred n-ninety-n-nine..."
        mc "*Panting* A-And..."
        play soundlow leathershort
        scene gb 46
        mc "T-Three..." with dis14
        play sound5 leathershort
        scene gb 47
        mc "{sc=2}H-HUNDRED...!!!!{/sc}" with dis17
    else:
        mc "*Panting* One hundred t-twelve..."
    play sound3 fallfull
    play sound7 debris3
    scene gb48fall 
    mc "AAAAAAAAGGGgggGHHHHhhhhh..." with vpunchslow
    mc "*Panting* Oh, sweet Lord..."
    if daliapath:
        mc "*Panting* M-My chest's gonna be sore for a whole week..."
    else:
        mc "*Panting* I can't fucking do it..."
    $ unlock_look("dalia", 14)
    show gb 49
    if daliapath:
        d "Wow, that's unbelievable..."with dis14
        d "You..."
        d "You crazy son of a bitch, you actually did it!"
        d "Three hundred pushups!"
        show gb 50
        mc "*Panting* Haha... I-I told you I'd do it, didn't I?!"
        show gb 49
        d "I didn't think one hundred in a row was even possible when I started training you."
        d "Not without activating your demon form, at least!"
        show gb 48
        d "And in good form too..." with dis
        d "Just... WOW!"
        mc "*Panting* Hehe..."
        play sound debris
        play sound2 dustoff
        show gb 51
        bla "After taking a moment to finally catch your breath, you stand up and shake the dust off your armor." with dis15
        mc "Well, you know... that's how I operate."
        mc "I do {i}everything{/i} in good form."
        show gb 52
        d "Was that a sexual innuendo?"
        show gb 51
        mc "Perhaps. Very sharp."
        mc "And talking about sexual innuendos... you promised me a “surprise” if I managed to complete 300 pushups in a row."
        mc "Or am I remembering it wrong?"
        show gb 52
        d "Indeed, I did."
        d "Do you want your surprise now?"
        show gb 51
        mc "Please."
        show gb 52
        d "Very well..."
        play sound clothes3
        show gb 53 with dis15
        play soundlow kiss
        bla "Dalia takes a step forward and kisses you on the cheek." with dis
        play sound2 clothes3
        show gb 52
        d "There you go!" with dis14
        show gb 51
        mc "Really??"
        mc "Mmmh, as much as I enjoyed that, it just left me wanting more..."
        mc "Was that all?"
        show gb 52
        d "Oh my, you're so greedy!"
        d "What else do you want from me...?"
        show gb 51
        mc "How about another kiss?"
        mc "I'd settle for that."
        show gb 52
        d "*Giggles* Okay, okay..."
        play sound clothes3
        show gb 53 with dis15
        play soundlow kiss
        pause
        play sound2 rubbody
        play soundlow ["<silence 1.4>", kiss]
        scene gb 54
        bla "Dalia’s lips inch closer to yours, the movement slow and deliberate. You respond instinctively, your mouths colliding in a sloppy, heated kiss." with dis17
        play soundloop kissing fadein 1 volume 0.7
        show daliaarabiakiss with dis2
        dbt "Mmmmmmmhhh...{w=3.2}{nw}" with dis14
        mc "(My god, that tongue of hers is dangerously playful...){w=3.2}{nw}"
        mc "(That brings back very good memories...){w=3.1}{nw}"
        dbt "MmmmMMmhh...{w=3}{nw}"
        play sound clothes3 
        stop soundloop fadeout 1
        play soundlow debris
        scene gb 56
        d "*Dashing back* O-OKAY! O-Okay... eaaaasy, tiger..." with dis14
        d "*Giggles* You get carried away too easily, [mc]."
        scene gb 55
        mc "*Chuckles* Me? You were the one who started the kiss!"
        show gb 56
        d "*Giggles* Oh, was I...?"
        d "My memory's a little fuzzy..."
        show gb 55
        mc "In the end I’m gonna start thinking you’re actually into me, Dalia..."
        show gb 56
        d "Oh god, please, no... not in a million years."
        show gb 55
        mc "*Chuckles* That was a nice surprise, though."
        mc "Much better."
        mc "Between that and how the Ishari outfit looks on you... I'm starting to feel overheated again."
        show gb 56
        d "Oh no, be careful not to get dehydrated."
        show gb 55
        mc "Is there any other step of your surprise that I'm missing or...?"
        show gb 56
        d "Ah, well, now that you mention it..."
        d "There's an... optional one. I might show you later, if you behave."
        d "But I've gotta go grab my sandstorm glasses now, Samir's gonna be here any minute."
        show gb 55
        mc "Ah, in that case I'll make sure to be a good boy until then."
        d "*Giggles* Mm-hm."
        show gb 56
        d "Good."
        show gb 57 with dis17
        bla "Dalia gracefully slips out of sight, disappearing around the pillar." with dis15
        mct "Oh boy... the sexual tension between us is getting so thick you could cut it with a knife."
        mct "And all that's bound to explode at some point..."
        mct "Could this really be the {i}grand{/i} moment...?"
        mct "We really need to find another intimate moment for ourselves somewhere."
    else:
        d "Wow, that wasn't a bad attempt at all, actually." with dis14
        d "Far from the 300 hundred pushups you said you could do, but... still impressive."
        show gb 50
        mc "I'm a failure..."
        show gb 49
        d "Don't be sad, you did good!"
        d "But for real, you should get up now – Samir's gonna be here any minute."
        d "I'm gonna go grab my sandstorm glasses, get ready."
        show gb 50
        mc "O-Okay..."
        play sound debris
        play sound2 dustoff
        show gb 57
        bla "After taking a moment to finally catch your breath, you stand up and shake the dust off your armor." with dis15
        mct "Man, I need to exercise more."
        mct "And if Dalia doesn't want to help me train, I'll have to find some other coach somewhere."    
    show gb 58
    mc "*Looking around* (But in any case, first we need to–)" with dis12
    mct "Oh, crap, I didn't realize Jerry was sitting right there."
    if daliapath:
        mct "That's... a little embarrassing."
    else:
        mct "We've been kind of ignoring him all this time."
    mc ". . ."
    mct "Shit, should I say something...?"
    menu:
        with dis
        "[gr]Talk to Jerry":
            $ jerrytalk = True
            show gb 59 with dis17
            if daliapath:
                mc "*Clears throat* Hey, man..." with dis12
                mc "Sorry about... yeah, sorry about that."
                mc "I didn’t mean to make it uncomfortable or anything."
                mc "I just thought you weren’t here."
            else:
                mc "Hey, man." with dis12
                mc "I've noticed you're a bit down today, but... hey, don't worry, really. Everything will be alright."
                mc "If it helps at all, she rejected me too."
            show gb 60
            je "Hmm?"
            show gb 61
            je "What are you talking about?"
            show gb 60
            if daliapath:
                mc "Well... I mean... Dalia and I."
                mc "Kissing."
                mc "And acting cringy and all flirty, like some lovey-dovey couple."
                mc "I know you liked her, I don't want to make it uncomfortable for you."
                mc "That's not my style."
            else:
                mc "Dalia."
                je "Hmm?"
            show gb 62
            je "Ah, that..."
            je "Don't sweat it, I'm over it."
            if daliapath:
                je "I’m not going to play the jealous ex, pouting over my old girlfriend's new guy. I'm not that pathetic."
                show gb 59
                mc "Okay, first off, Dalia and you were never together, so she can't be your “ex”."
                mc "That only existed in your head."
                mc "Although... I've gotta say, saying that is a step up for you."
            else:
                show gb 59
                mc "Wow, really? Saying that is already a step up for you."
            mc "You're not chasing after her anymore?"
            show gb 62
            je "Nah..."
            je "I'm not an idiot, even if you all think I am."
            if daliapath:
                je "I see the way she looks at you. She never looked at me like that."
            else:
                je "I realized she never cared about me."
            je "No one ever has."
            show gb 59
            mct "Damn... that took a sad turn all of a sudden."
            mct "Jerry sounds much more mature than usual today."
            mc "Um..."
            mc "I'm not sure what to say."
            mc "But hey, I’m really glad we can finally chat like this, just man to man."
            show gb 62
            je "At this point I just want to achieve something I can be proud of."
            je "I thought climbing the ranks in the WRE would help me make a name for myself, but... I keep dropping the ball."
            show gb 59
            mc "I'm sure you'll get there eventually."
            mc "You've just had some bad luck, but you've got the talent."
            mc "And hey, if there’s anything we can do to help, just let us know."
            je "Hmph."
            show gb 62
            je "Thanks, man."
            je "I appreciate you saying that."
            show gb 59
            mc "Anytime, bro."
            show gb 61
            je "But I still don’t like you. It's when YOU showed up in my life that everything started going downhill."
            je "To begin with, I lost the contest at Loco's Cafe because of you."
            show gb 60
            mc "Well..."
            show gb 61
            je "Then, an ogre crushed my skull in Ekabar, a Roman Legionnaire skewered me with a spear, I got headshot during the heist mission, and I even stepped on a mine during our WWI raid on Wagner's bunker!"
            je "That’s nearly half the times I’ve died in Eternum in the past three months, and every time, I was with you!"
            show gb 60
            mc "What do you mean, “nearly half the times”...?"
            mc "H-How many times have you died?"
            show gb 62
            je "I don't know, man, I lost count."
            je "The last time was... yesterday morning. I just barely made it past the penalty waiting period to be here today."
            show gb 59
            mc "Damn, yesterday? What happened?"
            show gb 62
            if anniepath:
                je "I went to Polaxymer-83, in the Andromeda server, to try to locate Xenomorph nests for you and Dalia to hunt, and..."
                show gb 59
                mc "T-To where...?"
                show gb 62
                je "Then... POOF, everything went black."
            else:
                je "I went to Polaxymer-83, in the Andromeda server, to try to locate Xenomorph nests for you and Dalia to hunt, and then... POOF, everything went black."
            je "I don't even know what happened."
            show gb 59
            mc "U-Uhh..."
            if anniepath:
                mc "T-That sounds mysterious, yeah. N-No idea, I've never been there."
                mct "I better not mention this to Annie or Luna..."
            else:
                mct "Wasn't that the planet that Annie blew up when she was playing with Luna?"
            mc "*Clears throat* B-But anyway, as I said, you've just been having bad luck."
            mc "From now on, everything will start improving, trust me."
            show gb 62
            je "If you say so..."
            show gb 59
            mc "I'm sure of it."
            je "Hmph."
        "Ignore him":
            mct "Bah, he's gonna be okay." with dis
            if daliapath:
                mct "If he doesn't wanna see us, he can look elsewhere."
            else:
                mct "He's a big boy."
    stop music2b fadeout 5
    play sound horse
    pause 1
    play music2 arabia1 fadein 7 volume 0.75
    play sound2 horsesaddle
    scene gb 63 with dis2
    bla "A man on the back of a large, gray horse rides into the oasis." with dis17
    mct "Ah, that must be our man."
    play sound3 horsewalk
    scene gb 64 with dis22
    play sound4 ["<silence 1.8>", horse2]
    bla "The man reins his horse toward your position, its hooves landing with a solemn stamp." with dis14
    mct "Dang, that's what I call having aura."
    show gb 64b
    je "Whoa..."with dis
    je "Dude, I need to become an Ishari."
    je "Do you accept new members?"
    show gb 65
    sam "The Ishari are always on the lookout for valiant players to join our cause."with dis
    sam "You'd be very welcome."
    show gb 64
    je "Awesome..."
    mc "You must be Samir."
    show gb 65
    sam "I am."
    sam "And you're... not Dalia, I assume?"
    show gb 64
    mc "You can call me [nickname]."
    show gb 66
    d "I am Dalia." with dis
    d "And you're late."
    show gb 65
    sam "My apologies." with dis
    sam "Something came up before I could leave for the meeting point, but I’m still willing to honor our deal if you’re still sticking to it."
    show gb 66
    d "We are."
    d "The WRE offers you support against the Sultan, in return for safe passage into their citadel for us three."
    show gb 65
    sam "I will do as promised. I can get all three of you right to Hassan’s doorstep."
    sam "But we don't have much time, so please do as I say."
    show gb 64
    mc "Wait, not so fast..."
    mc "I don't like trusting my life to someone I know nothing of."
    mc "Are you really the Leader of the Ishari? You're wearing the same outfit as us."
    show gb 65
    sam "The Ishari take no pride in elevating our leaders to divine status. In the face of the endless sands, all men and women stand as equals."
    show gb 64
    mc "Hmm."
    mc "And... why do you want to destroy Hassan?"
    show gb 65
    sam "Because he's a parasite that must be eradicated."
    show gb 64
    mc "A parasite?"
    show gb 67
    sam "You see... from the lands of Egypt all the way to Canaan, my ancestors have roamed the dunes of Valley of the Kings for countless generations." with dis12
    sam "I was born here, just like my father before me, and his father before him."
    sam "We–"
    show gb 68
    d "Can we skip the fake lore dump, please?"
    d "Eternum is not even ten years old. Or... well, Ulysses at least."
    show gb 69
    d "And you literally said we were in a hurry just a moment ago."
    sam ". . ."
    show gb 65
    sam "It's called {i}immersion." with dis12
    sam "But fine, I'll give you the short version."
    sam "We've basically been playing in this server since the beginning, back when it was just a barren wasteland."
    sam "We built EVERYTHING you can see now."
    sam "But then... Hassan showed up with his endless oil money and his jackal army, and declared himself sultan."
    sam "Since that day, he’s been enslaving both players and NPCs and exploiting our land, destroying everything we built."
    sam "All we want... is to reclaim what’s rightfully ours."
    show gb 64
    mc "Hmm."
    mc "That's a solid motive."
    mc "Alright then, the WRE will help your people when the day comes."
    mc "You have my word."
    show gb 65
    sam "I appreciate it."
    show gb 70
    sam "Very well, then!"with dis12
    sam "I'll take all three of you to Hassan, but we need to split up first."
    show gb 71
    sam "Do you see the horses beneath the palm tree across the lake?"with dis12
    d "I do."
    sam "You'll meet with my sister Yssandra there."
    sam "She'll assist you in infiltrating a delivery of slaves destined for Hassan. The wagon is already nearing the citadel, so you must hurry."
    mc "Slaves? Will it be safe...?"
    sam "If she stays out of trouble, they won't harm her. By the time things could get dangerous, she’ll be long gone."
    sam "I assume you're also capable of defending yourself?"
    d "Of course."
    sam "Excellent."
    show gb 65
    sam "And you two will come with me." with dis12
    sam "The Ishari are still not banned from trading in the open market, so that'll be our gateway."
    sam "Our chances of success aren't as high as using the slave route, but unfortunately, the Sultan is only interested in a... specific type of slave."
    show gb 64
    mc "Yeah... I can imagine."
    show gb 65
    sam "Any questions?"
    show gb 64
    mc "Not at the moment."
    show gb 65
    sam "So be it, then! Time to move!"
    play sound3 horsewalk
    play sound5 horse
    show gb 72
    d "Ahh... this is gonna be fun!" with dis17
    d "Good luck, guys!"
    show gb 73
    mc "Your route sounds a lot riskier than ours, so please be careful!"
    mc "Stay alert and keep an eye out at all times!"
    mc "Oh, and NEVER turn your back to a potential enemy!"
    mc "Trust me, I'm speaking from experience."
    show gb 74
    d "Yes, yeees... jeez, don't lecture me..." with dis12
    d "I'm gonna be fine..."
    if daliapath:
        show gb 75
        d "Although... I do like seeing you worry about me, not gonna lie." with dis12
        d "You be careful too, okay?"
        show gb 76
        mc "*Chuckles* I will, I promise."
        show gb 77
        d "Good!" with dis12
        d "And try to keep Jerry alive while you're at it, would ya?"
        mc "*Laughs* I'll try my best."
        d "See you later!"
        mc "Later!"
    play sound run
    show gb 78 with dis2
    if daliapath:
        mct "Alright, let's get this done with." with dis
    else:
        mct "You better..."with dis
        mct "But alright, let's get this done with."
    mct "We've gotta discover how the Sultan is taking down so many Xenomorphs. I can't let the team down."
    sam "[nickname]? We're also in a bit of a hurry."
    mc "Yes, sir. I'm coming!"
    stop music2 fadeout 8
    scene black with dis3
    show screen sometimelater with dis3
    pause
    play sound wind4 fadein 2
    hide screen sometimelater with dis2
    play music arabia3 volume 0.85
    scene citadelpan with dis3
    pause 8.6
    play sound2 footsteps3
    scene gb 79
    sam "Alright, gentlemen... welcome to the Citadel."with dis2
    sam "One of the most important trading hubs of Valley of the Kings, a crucial link between Egypt, Arabia, and the other free cities scattered across the desert, and now..."
    sam "Also the stronghold of Hassan al-Rashid."
    show gb 80
    mc "How could he take the city so easily?"
    mc "This place looks imposing. Didn't the Citadel have its own army or something?"
    show gb 79
    sam "He simply bought his way in."
    sam "Despite our traditions and our code of honor, at the end of the day most of the top players of this server are just regular people with day jobs."
    sam "When someone offers you more money than you’d make in a decade, it’s hard to say no."
    show gb 80
    mc "Hmph... understandable, I suppose."
    show gb 79
    sam "As for those who put up a fight... the Sultan’s personal army of jackals took care of them in no time."
    sam "Those beasts are taller than any man and built like solid rock."
    sam "You'd be wise to avoid them."
    show gb 80
    mct "Could Hassan be using those jackals to kill Xenomorphs and win the event?"
    mct "Hmm... no, I don't think you can team up with monsters or creatures like that."
    mct "Which brings us to the real question – how is he wiping out so many? As far as I know, he only plays in this server, but I haven’t seen a single trace of a Xenomorph."
    show gb 79
    sam "The central market will be starting soon."
    sam "The place will be crawling with people, and that'll be our way in."
    show gb 80
    mc "Understood. Lead the way."
    show gb 79
    sam "Follow me."
    scene gb 81
    bla "Samir guides you and Jerry to a deserted street tucked behind the market." with dis27
    play soundlow footsteps3
    show gb 83 with dis17
    sam "*Looking behind* Okay..." with dis12
    sam "No one seems to be following us..."
    sam "Open the door behind me and get inside, quick!"
    play sound2 doorsqueakk
    play sound doorold
    show gb 84 with dis2
    bla "You step through the door and into an opulent room, the air thick with the rich aroma of incense."with dis12
    play sound3 whistle3
    mc "*Whistles* Damn, the Ishari sure know how to throw a party."
    mc "Nice place you got yourself here."
    sam "This building used to be a fuck pad for the old guards."
    sam "We repurposed it as our base of operations in the Citadel until... well, at least until Hassan's men catch wind of it."
    sam "We can all meet back here when you've gotten the info you need."
    show gb 86 with dis12
    play sound chair1
    je "*Sitting down* Aaaghh..." with vpunchslow
    je "Can I just stay here and smoke opium with this hookah?"
    je "I'd probably be more useful guarding the base than out there, where I'd just end up... with my head smashed by a flowerpot falling from a window or something, I don't know."
    show gb 87
    if jerrytalk:
        mc "Come on, Jerry..."
        show gb 86
        je "No, seriously, you go ahead."
        show gb 87
        mc "Didn’t you say you wanted to climb the ranks within the WRE?"
        mc "If you help us with this and we win the event, everyone will know you helped secure a new Gem of Doom."
        mc "Do you really want to go down as the coward who failed the Empress in her hour of need instead?"
        je ". . ."
        show gb 87b
        je "No, I don't want to."
    else:
        mc "Come on, Jerry, do you really want to let Dalia down like this?"
        mc "And besides, with your recent luck, who's to say you won’t get killed if you stay here anyway?"
        je ". . ."
        show gb 86
        je "*Sighs* Okay, okay, I'll come..."
    show gb 88
    mc "All said, then." with dis
    mc "We're ready, Samir. What's the plan?"
    show gb 89
    sam "At the south end of the market, there’s an archway guarded by just one jackal. It leads directly to Hassan’s chambers, where you can probably find the information you need."
    sam "I’ll create a distraction, and when the guard comes over, you two can sneak past him."
    show gb 90
    sam "Once you're finished, we can meet back here. Just make sure to lock the door behind you if you get here faster than I can."with dis12
    sam "Don't open the door unless the person outside says the password “Free Sands”. I won't let you in unless you say it first either."
    show gb 89
    sam "All clear?" with dis12
    show gb 88
    mc "Perfectly clear."
    show gb 89
    sam "We're leaving for the market in 10 minutes. Get ready."
    show gb 88
    mc "What about Dalia?"
    mc "Is she using the market too?"
    show gb 89
    sam "If she successfully joined the slave delivery, she could even be with Hassan himself as we speak."
    sam "If she plays her cards right, she can easily get any info she needs from him. After the inspection, they'll go back to my sister to “negotiate the price”, and that's when she'll help her escape."
    show gb 88
    mc "Alright... at least it seems like you guys have everything under control."
    mc "*Sighs* I hope she's alright..."
    stop music fadeout 11
    play soundloop river fadein 6
    scene gcc 1 with Dissolve(3.3)
    play musicb arabiatension volume 0.85 fadein 5
    pause
    d "(Hmmm...)" with dis14
    d "(That wall looks easy enough to climb.)"
    show gcc 2
    d "(And the stable is also in that direction, unless my orientation is off.)" with dis17
    d "(If I needed to escape on my own, I could probably slip over there, grab a horse, and gallop into the desert before they could even react.)"
    show gcc 3
    d "(The only problem would be...)"
    show gcc 4
    d "(Those statue-looking things.)"
    d "(They might look dumb, but they seem to be as loyal as dogs and as strong as a bull. And there are like dozens of them...)"
    show gcc 5
    jac "*Looks towards Dalia's position* . . ." with dis14
    show gcc 6
    d "(Yikes, their gaze makes my skin crawl.)" with dis12
    d "(I can feel their eyes on me, always watching my every move.)"
    d "(It won't be easy...)"
    play sound footstepsmonster
    show gcc 7
    ha "Ahh, yes... lovely, lovely!" with dis2
    ha "My apologies for the wait, ladies, and welcome to the Citadel!"
    show gcc 8
    d "(Huh...?)" with dis12
    d "(That's... that's him! The Sultan!)" 
    d "(O-Okay, calm down, Dalia... just play along for now...)"
    d "([mc] is counting on you...)"
    ha "*Chuckles* Mmh-mh..."
    show gcc 9
    bla "The Sultan spends several seconds silently scrutinizing the faces and bodies of the captured girls, his nasty gaze turning Dalia's stomach."with dis14
    show gcc 13
    ha "You seem frightened, my young flowers of the desert... but I assure you, there’s nothing to fear." with dis 
    ha "Your days among the cockroaches of the Ishari are finally over."
    show gcc 10
    ha "From now on, my personal guards and Zahra al-Nabi, the Citadel's Oracle, will be at your full service."
    show gcc 11
    ha "She may be blind, but she can actually see things that no one else can."
    ha "Isn't that right, Zahra?"
    show gcc 12
    ora "It is."
    ora "The Sultan's wives are treated with the same reverence as the Prophet himself. They shall want for nothing."
    show gcc 11
    ha "Indeed, they are."
    show gcc 13
    ha "However... you must first demonstrate that you're worthy of such a high honor, obviously."
    ha "You must prove to me that you're... pure."
    show gcc 14
    is1 "Eh?"
    is1 "Pure?"
    is1 "What... w-what do you mean?"
    show gcc 13
    ha "Oh, well, you {i}know{/i} what I mean."
    show gcc 10
    ha "Becoming one of my wives transcends Eternum, young lady. Your life will be forever free of worries, and all your expenses will be taken care of."
    show gcc 13
    ha "Nevertheless, your... virginity... must remain intact. Only then can I ensure your purity and uphold the honor of my family."
    show gcc 14
    is1 "Ah.... y-yeah... of course."
    is1 "And... if I may ask... w-what does “virginity” entail?"
    show gcc 15
    is1 "Because I've... {i}kissed{/i}... people before, so..."
    show gcc 13
    ha "*Chuckles* Fear not, my petal of the desert."
    ha "I may be traditional, but I'm not an irrational man."
    ha "As long as the final, sacred act hasn’t been consummated, such preliminaries don’t count."
    show gcc 14
    is1 "O-Oh, well... then... I'm good! I'm pure!"
    is1 "Purest girl in the server!"
    show gcc 13
    ha "Ah, wonderful!"
    ha "That's wonderful..."
    show gcc 21
    ha ". . ." with dis
    show gcc 11
    ora ". . ."
    show gcc 12
    ora "She's lying."
    show gcc 15
    is1 "What?! No!" with hpunch
    show gcc 14
    is1 "I mean..."
    is1 "O-Okay, yes, but I-I've only done it in Eternum!"
    is1 "I didn't..."
    show gcc 13
    ha "*Chuckles* Please, please, relax..."
    ha "There's no need to be so tense."
    ha "Just because you may not be fit to be my wife doesn’t mean you can't serve a purpose just as important."
    ha "What's your name, darling?"
    show gcc 14
    is1 "M-My name is Samantha. I'm 23, and I live in N-New Orleans!"
    is1 "I only joined this server becaus–"
    show gcc 13
    ha "Please, please, calm down..."
    ha "I insist, there's nothing to fear, Samantha."
    ha "As I said, you'll serve a greater purpose now."
    show gcc 22
    ha "*Chuckles* Mmh-mh."
    ha ". . ."
    ha "Hmph."
    stop musicb
    play sound musicstop
    show gcc 16
    ha "Take this slut to the incubation room."
    play music2 arabiatension2
    play sound grab3
    play sound2 debris
    play sound3 fms
    scene gcc17
    is1 "{sc=2}WHAT?!{/sc}" with hpunch
    ha "Please, do not resist and accompany my guards."
    is1 "WHERE ARE YOU TAKING ME?!" with hpunch 
    ha "You'll see soon enough."
    ha "But seriously, don't worry, you'll be back to the real world in no time."
    play sound footstepsmonsterleave
    scene gcc 18
    bla "One of the guards hoists the Ishari girl onto its shoulders and disappears with her into the nearby building." with dis17
    d "What the hell is going on in here..."
    d "Did he say... the incubation room...?"
    show gcc 13
    ha "Alright! Who's next?" with dis
    play sound2 debris3
    show gcc 19
    is2 "{sc=2}*Shivers* M-M-My name is Pam!{/sc}" with hpunch 
    is2 "{sc=2}I'm 19! F-From Los Angeles!{/sc}"
    is2 "{sc=2}I'm studying at Stanford! And I...{/sc}"
    is2 "{sc=2}I-I've only done it once, I swear!{/sc}" with hpunch 
    is2 "{sc=2}It was prom night, I got a little drunk, and...{/sc}"
    is2 "{sc=2}I-It was terrible! The guy lasted like 30 seconds!{/sc}"with hpunch 
    is2 "{sc=2}I d-didn't even finish!{/sc}"with hpunch 
    show gcc 13
    ha "*Laughs* You girls are way too skittish to play on servers like this."
    ha "But I do appreciate the honesty."
    ha "Thank you, Pam."
    show gcc 11
    ora ". . ."
    show gcc 12
    ora "It's true. Everything she said."
    show gcc 10
    ha "Ah, I see..."
    show gcc 13
    ha "Well, I’ve got to admit, you won me over with your sincerity, Pam."
    ha "That's something I deeply value in a wife."
    show gcc 20
    is2 "R-Really?"
    is2 "T-Thank you! Of course! I'll always be sincere."
    show gcc 13
    ha "Of that, I have no doubt, Pam."
    ha "No doubt..."
    show gcc 22
    ha ". . ."
    play sound deception2
    play sound7 deception2
    show gcc23
    ha "To the incubation room." 
    scene gcc 19
    is2 "WHAT?!" with hpunch 
    play sound2 debris
    play sound3 fms
    scene gcc23b
    is2 "{sc=2}NOOOO!!!!{/sc}" with vpunchslow
    is2 "{sc=2}PLEASE, DON'T KILL ME!!!{/sc}" with hpunch 
    play sound footstepsmonsterleave
    show gcc 23
    ha "Hassan al-Rashid's Citadel has no place for spoiled whores." with dis12
    ha "Take her out of my sight."
    ha "“I didn't even finish”, she says... fucking disgusting."
    show gcc 24
    ha "Well, well, well..." with dis17
    ha "Only one candidate remains."
    play sound4 debris
    show gcc 25
    bla "Dalia strikes a defiant pose, preparing her body to fight back if needed." with dis15
    show gcc 26
    d "If you or one of your mangy dogs lays a single finger on me, you'll regret it for the rest of your life."
    show gcc 24
    ha "Ahh... a fighter!"
    ha "Nice... I like when they resist."
    show gcc 26
    d "Where are you taking those girls?"
    d "Let them go and tell me everything you know about the Xenomorph contest, or I'll inform the Praetorians that you're violating the EGCE in here."
    show gcc 24
    ha "*Chuckles* Tough girl..."
    ha "Finally, someone who lives up to the reputation of Ishari women."
    show gcc 29
    ha "Too bad such an exuberant body was probably already spoiled long ago."
    ha "I bet she gave her purity to some pathetic loser ten years older just to get back at her daddy."
    ha "A shame..."
    show gcc 26
    d "My dad left before I was even born, you fucking idiot."
    show gcc 24
    ha "Ah... is that so?"
    ha "I noticed you didn't deny the first part of my statement."
    ha "Interesting..."
    show gcc 28
    ha "Tell me... are you still pure?"
    d ". . ."
    show gcc 27
    d "T-That's... that's none of your fucking business."
    show gcc 28
    ha "*Sighs* Agh, I know what that means..."
    show gcc 29
    ha "As I expected..."
    ha "What a waste."
    ha "Each passing day it becomes harder and harder to find–"
    show gcc 12
    ora "Wait."
    show gcc 11
    ora ". . ."
    show gcc 30
    ora "She's... still pure." with dis
    show gcc 24
    ha "Huh?!"
    ha "No way..."
    ha "Are you sure?"
    show gcc 30
    ora "I am."
    show gcc 28
    ha "Ahhh, the sun shines today!" with dis12
    ha "Who would've thought, with that body?! What a wonderful surprise!"
    show gcc 28
    ha "You'll become my most beloved queen, my young flower!"
    show gcc 27
    d "I have questions for you."
    show gcc 24
    ha "And I shall answer them all, my sweet petal..."
    ha "But first you need to get ready."
    play sound clotheswhoosh
    play sound2 debris
    show gcc 31
    ha "Take her to my chambers and help her get all set, Zahra." with dis
    show gcc 11
    ha "And take two guards with you."
    show gcc 30
    ora "As you command, Sultan."with dis
    show gcc 31
    ha "The rest, with me – there's something I need to take care of."
    show gcc 28
    ha "I'll be there in no time to... answer all of your questions, my desert rose, don't worry..."
    d ". . ."
    stop music2 fadeout 8
    stop soundloop fadeout 8
    scene gcc 38 with Dissolve(3.2)
    $ renpy.music.set_volume(0.75, channel='music3')
    play music3 ["<silence 2>"] 
    queue music3 arabia1 
    play soundloop2 citadelmarketsound fadein 9 volume 0.8
    pause 1.8
    play soundlow footsteps3
    show gcc 39
    je "Holy Toledo, this place is pure chaos." with dis17
    je "There are people selling... some pretty {i}questionable{/i} stuff everywhere."
    show gcc 41
    mc "Yeah... I hope Samir doesn't bail on us at the last moment."
    mc "I wouldn't even know where to start."
    show gcc 40
    je "Nah... his people need the WRE for this so-called “war” against the Sultan."
    je "He needs us more than we need him."
    show gcc 41
    mc "Yeah... that's true."
    mc "Though... it makes me wonder, if he can really get us to the Sultan so easily, why hasn’t he just killed him himself and ended this whole thing?"
    show gcc 40
    je "Well, just killing him wouldn't end his control over the Citadel – he'd just respawn in 24 hours like nothing happened."
    show gcc 41
    mc "Huh..."
    mc "Yeah, I suppose you have a point there."
    show gcc 40
    je "In Eternum, things work a little differently. You have to destroy their infrastructure, take control of their–"
    play sound debris3
    play sound3 whoosh6
    play sound2 dromedary
    show gcc 42
    je "{sc=4}AAAAAAAAAAARGGGGHHHH!!!!{/sc}" (multiple=2) with hpunchlong
    camel "{sc=3}GGGYYYYYYYAAA...{/sc}" (multiple=2) 
    je "{sc=2}M-Motherfucker!{/sc}" with hpunch 
    show gcc 43
    mc "*Laughs* Come on, Jerry, it's just trying to be friendly!"
    mc "Don't tell me you're scared of what's essentially just a big doggo with–"
    play sound footstepsmonstershort
    scene gcc 44 with dis2
    pause 0.5
    scene gcc 44 with vpunchslow
    pause
    show gcc 45
    mct "THE FUCK...?!" with dis14
    mct "W-What in the world is this golem??" 
    mct "Are these the jackal guards Samir mentioned?!"
    play sound2 footstepsmonsterleave
    show gcc 46 with dis2
    mc "M-My god, those things are way bigger than I thought." with dis14
    mc "How many did he say there were again?"
    sam "Oh shit, this is bad..."
    show gcc 48
    mc "*Turning around* Hmm?" with dis12
    mc "Ah, finally, there you are!"
    show gcc 47
    sam "The whole market's crawling with jackals..."
    sam "This is NOT good. The Sultan must've tightened security." 
    show gcc 48
    mc "So... what now?"
    mc "Do we call it off?"
    show gcc 47
    sam "No, no... we're sticking to the plan."
    sam "We need to wait until 3:30, when my lieutenant will arrive."
    sam "Then, just like I said: I’ll distract the guard at the archway, and you two sneak into the palace."
    sam "We just have to... stay hidden until then."
    show gcc 48
    mc "Hidden?"
    show gcc 47
    sam "Split up, walk around, buy some shit at the market, talk to people... I don't know, just don’t attract any guard's attention until 3:30."
    sam "We're already on their radar just by wearing Ishari uniforms."
    show gcc 48
    mc "Understood. We'll be ready when the opportunity arises."
    show gcc 47
    sam "Good, good..."
    sam "Now, let's all split up and blend in. Move!"
    play sound footsteps3
    scene gcc 32 with dis22
    mct "Alright..." with dis14
    mct "Blend in with the crowd for 10 minutes and steer clear of the guards."
    mct "I've played Assassin's Creed – I can do this."
    mod "Do the leftmost circle last to complete them all."
    call screen arabiamarket with dis15
label arabiamarket:
    scene gcc 32 with dis2
    if citadeltime >= 30:
        mct "Hmm... it's time already." with dis
        jump arabiaposmarket
    if citadeltime == 29:
        mct "Hmm... looks like I still have some time left." with dis
        mct "I don't see Jerry, though. I hope he's still alive..."
    call screen arabiamarket with dis15
label arabiamarket1:
    $ amarket1 = False
    play sound2 footsteps3
    scene gcc 63 with dis2
    mc "Hmm?" with dis12
    me "*Snores* Zzzzz..."
    mct "Is this one sleeping...?"
    mc "Erm... hello?"
    show gcc 64
    me "H-Huh?"with dis 
    me "Oh... s-sorry, do you want to buy some spices?"
    mc "Spices?"
    mc "Um... not at the moment, no."
    me "Eh...?"
    me "Then why did you wake me up?"
    show gcc 63
    me "Agh... this job isn't worth it..."with dis08 
    me "*Snores* Zzzzz..."
    mct "I better keep moving..."
    $ citadeltime += 7
    if maatsex:
        play sound footsteps3
        show gcc 65 with dis15
        mc ". . ." with dis14
        ma ". . ."
        play sound3 whoosh3b
        play sound4 debris3
        play soundlow slam3
        scene gcc63
        mcsc "S-So, how much did you say the spices were?!"
        play sound3 whoosh3b
        play sound5 debris3
        play soundlow punch
        play sound holster2
        scene gcc66
        ma "I KNEW IT WAS YOU!" with hpunch 
        scene gcc 67
        mc "*Raising your hands* O-OKAY, let's calm down everyone!"
        mc "I don't..."
        mc "Wait, is that a crossbow...?"
        mc "In this server?! I-Is that even lore-accurate??"
        show gcc 66
        ma "Yes, it's really you..."
        ma "With more muscle and longer hair, but I'd recognize that bastard face anywhere!"
        scene gcc 67
        mc "*Gasps* Wait a second..."
        mc "Maat?! Oh my god, what a pleasant surprise!"
        mc "What are you doing around here?!"
        mc "I-It's been a while, hasn't it?!"
        show gcc 68
        ma "*Giggles* You really thought you could waltz back into {i}my{/i} server without me finding out, huh?"with dissolve 
        ma "Well, tough luck, pal... turns out the desert isn't big enough for that to happen."
        ma "Now I can finally have my sweet revenge..."
        show gcc 69
        mc "What revenge?!"
        play sound holster2
        show gcc 66
        ma "You raped me!" with hpunch 
        play soundlow slam3
        show gcc 67
        mc "EXCUSE ME?!" with hpunch 
        mc "You're the one who forced us to undress and everything at gunpoint!"
        mc "If anything, YOU raped me!"
        show gcc 68
        ma "*Laughs* Please, you got hard, [mc]." with dis
        show gcc 69
        mc "So...?"
        show gcc 68
        ma "If you have an erection, you can't be “raped”."
        ma "It means you're having fun."
        show gcc 69
        mc "That's not how it works."
        play sound holster2
        show gcc 66
        ma "That's exactly how it works!" with hpunch 
        ma "You enjoyed every second of what happened that day!"
        show gcc 67
        mc "Oh yeah, because you didn't, right??"
        ma ". . ."
        ma "*Grumbles* Mmmrrr..."
        show gcc 70 with dis12
        ma "*Taking a deep breath* You know what? Let’s hit the reset button." with dis
        ma "Let's just agree that we both had a good time that day, okay? No need to kid ourselves."
        ma "Now, if you can just give me my money back, we can go our separate ways and get on with our lives."
        ma "Cool?"
        show gcc 71
        mc "What money?"
        show gcc 70
        ma "You used the Bastet figurine on me and looted me. You owe me 250 eternals."
        if not maatmoney:
            show gcc 71
            mc "Uh... I didn't loot anything."
            mc "Someone else probably swiped it after we left you in that temple."
            show gcc 70
            ma "Well, even if that was true, it’s basically the same thing. You left me there unconscious, so it’s on you."
            ma "Now please, my money."
        show gcc 71
        mc "I'm not giving you back anything."
        mc "You deserved that."
        ma ". . ."
        show gcc 70
        ma "*Taking a deep breath* Look... let's make a deal."
        ma "You give me back 80 eternals, which is what I need to kick off a little project of mine that'll get my “career” back on track, and we're even."
        ma "If everything goes as planned, I promise I'll return it to you... with interest."
        ma "Deal?"
        show gcc 71
        menu:
            with dis
            "[gr]Give her 80 eternals":
                $ maat80 = True
                mc "*Sighs* Fine, if that’s what it takes to wrap this up and move on." with dis08
                play sound2 holster2
                show gcc 68
                ma "Excellent!" with dis12
                show gcc 69
                mc "Why are you pointing that thing at me again?! I said yes!"
                show gcc 68
                ma "Just making sure you stick to the deal."
                show gcc 69
                mc "*Sighs* Fine, fine."
                show screen eternals with dis08
                play sound coins
                $ money -= 28
                pause .05
                $ money -= 24
                pause .05
                $ money -= 28
                pause .3
                show gcc 69         
                hide screen eternals
                mc "Done. Now just get out of my sight already."with dis
                show gcc 70
                ma "Thank you, [mc], I always knew you were the real deal." with Dissolve(1.3)
                ma "I promise that when I become the ruler of Valley of the Kings, I’ll have them build a giant statue of your monster junk right at the entrance of my temple."
                show gcc 71
                mc "T-That won't be necessary, but thank you."
                show gcc 70
                ma "Maat never forgets, trust me."
                ma "You'll be rewarded!"
                ma "Thank you, and may the sands bless you!"
                ma "Ah, and give my regards to your naughty ginger girl!"
            "Refuse":
                $ maat80deny = True
                mc "No." with dis08
                ma ". . ."
                play sound2 holster2
                show gcc 66
                ma "Is this really how you want to do this?!" with dis12
                ma "GIVE ME MY MONEY BACK!"with hpunch 
                show gcc 67
                mc "I wouldn't shoot that thing if I were you."
                mc "First off, you'd find out the hard way just how much stronger I've gotten."
                mc "And honestly... I have a feeling you don’t want to get the guards involved either. Am I wrong?"
                ma ". . ."
                ma "*Grumbles* Mmmrrh."
                show gcc 70
                ma "You know what...?" with Dissolve(1.3)
                ma "Fine... fine."
                ma "Let's just leave it like this, pretty boy."
                ma "I'll get my money back one way or another, don't you worry."
                ma "And when I do... I swear to God, I’m gonna spend my days plotting my revenge on you."
                ma "Just when you think everything’s going great... BAM!"
                ma "I’ll take it all from you."
                ma "Then you’ll be left there, sobbing, wondering “ohh no, why didn’t I help poor Maat when I had the chance? Now my life is ruined!”"
                show gcc 71
                mc "You have a knack for creating stories, I'll give you that."
                show gcc 70
                ma "Yes... laugh now that you can."
                ma "That'll only make my revenge all the more delicious."
                ma "Just wait and see, [mc]..."
                ma "Whenever you least expect it..."
        play sound  footsteps3
        show gcc 72 with dis22
        mct "Bro..." with dis12
        mct "What are the odds?!"
        mct "Eternum's got like a billion players, and I keep bumping into people I know. How is that even possible?!"
        if eva1:
            mct "At least this time none of the girls were around to see her..."
        mc "*Sighs* (But anyway, I should head back to the market entrance before I run out of time. It's already 15:[citadeltime].)"
    jump arabiamarket 
label arabiamarket2: 
    $ amarket2 = False
    $ citadeltime += 1
    play sound2 footsteps3
    scene gcc 33 with dis2
    mc "Good morning, friend." with dis
    show gcc 34
    me "It's 3:[citadeltime] PM."
    show gcc 33
    mc "Huh?"
    mc "Oh... y-yeah, I meant {i}good afternoon{/i}, my bad."
    mc "It's always tough keeping track of the time differences between Eternum and the real world."
    mc "Don't you think?"
    show gcc 34
    me "Why don't you get the fuck out of here and leave me in peace, you dumbshit?"
    show gcc 33
    mc "Whoa! That really came out of nowhere!"
    mc "Why so rude, buddy?"
    mc "I just came here to buy something."
    show gcc 34
    me "I'm not your buddy."
    me "And I'm not selling you shit."
    show gcc 33
    mc "Wow, you sure woke up on the wrong side of the bed today, huh..."
    mc "...BUDDY?"
    play sound whoosh6
    play sound2 debris3
    play soundlow impact5
    show gcc35
    me "{sc=2}I'M NOT SELLING SHIT TO ISHARI TRASH, YOU HEAR ME?!{/sc}" with hpunch
    scene gcc 36
    mc "O-Okay, okay, relax!"
    mc "I'm leaving, but please, don't scream!"
    show gcc 35
    me "Why...? You scared of the guards?"
    me "{sc=2}GUARDS! THIS ISHARI IS TRYING TO ROB ME!{/sc}" with hpunch 
    show gcc 36
    mc "NO!" with hpunch 
    show gcc 37
    mc "Shut up, p-please!" with dis12
    mc "I'm not an Ishari!"
    mc "I'm just pretending, please SHUT UP!"
    jac ". . ."
    show gcc 33
    mc "I-I'm just wearing one of their armors, but I'm not one of them, I swear!" with dis12
    show gcc 34
    me "Oh... really...?"
    me "Well, in that case... I apologize."
    show gcc 33
    mc "Jesus... what have the Ishari done to you to be this mad?"
    show gcc 34
    me "I... used to be one of them myself."
    me "I followed Samir, respected him like a king, and loved him like a brother."
    show gcc 33
    mc "And what happe–"
    show gcc 34
    me "He fucked my girlfriend."
    show gcc 33
    mc "O-Oh."
    mc "I see."
    show gcc 34
    me "That coward isn’t fit to rule the Ishari."
    me "Under his command, they'll never reclaim the Citadel, let alone the Valley of the Kings like they always wanted."
    me "I might have a grudge against current members because of him, but as a clan, they used to be a proud and respectable organization."
    show gcc 33
    mc "Would you consider rejoining them if they ever got a new leader?"
    show gcc 34
    me "Without a doubt."
    me "I... I wasn't born to sell potatoes in a market."
    me "I'm not good with people."
    show gcc 33
    mc "Y-Yeah, I can tell."
    mc "Well, in any case... I wish you luck."
    mct "Good to know a little more about that Samir guy..."
    if daliapath:
        mct "Although I'm not worried. If he ever tried something with Dalia, I doubt he’d get anything but a kick in the nuts."
    show gcc 34
    me "Um... hey, sorry about earlier."
    me "I lost my temper."
    show gcc 33
    mc "No worries, mate."
    mc "It's all good."
    show gcc 34
    me "Good luck with whatever you're doing here, bro."
    show gcc 33
    mc "Thanks, you too!"
    $ citadeltime += 2
    jump arabiamarket 
label arabiamarket3: 
    $ amarket3 = False
    play sound2 footsteps3
    scene gcc 49 with dis2
    mc "Uh... hello there!" with dis
    mc "Are you..."
    mc "Is this a shop...?"
    me "Mm-hmm."
    show gcc 49b
    me "It is." with dis14
    me "I sell small statues of the goddess Psyche, all made of copper."
    mc "Oh, cool."
    mc "They're very pretty."
    mc "How much are they?"
    me "Why do you care? You're not going to buy any."
    stop music3 fadeout 12
    play music syndicate fadein 10
    show gcc 50
    mc "And how do you know if I'm going to buy one or not?" with dis12
    mc "That's a bad business strategy, you know."
    show gcc 51
    me "I know you're not here to buy anything."
    me "You're here to blend in with the crowd and avoid drawing the guards' attention."
    show gcc 50
    mc "*Looking around* K-Keep your mouth shut, old man."
    mc "How do you..."
    mc "Who the hell are you...?"
    me "Mmh."
    show gcc 51
    me "Hyril'ar, the genocide, the loss of the ones you love, the end of everything."
    me "We've seen it all. Each moment as inevitable as it is preventable."
    me "But... you’re getting close to the point of no return, [nickname]."
    me "Once the chain is broken... only one path will remain."
    me "You'll be alone."
    me "And our fate will be sealed... by whichever side of the coin lands."
    show gcc 50
    mc "I recognize that ominous, cryptic verbiage..."
    mc "You're with the Syndicate, aren't you?"
    me ". . ."
    mc "Yeah... you're not the first one I've stumbled upon. Who the hell are you people, and why do you keep following me everywhere I go?"
    mc "Are you really some sort of group against Ulysses, or is the Founder just trying to play mind games with me?"
    show gcc 51
    me "The statues are just three eternals."
    show gcc 50
    mc "What...?"
    show gcc 51
    me "The copper figures, they're three eternals each."
    show gcc 49c
    mc "*Turning around* Not interested, old man, sorry." with dis12
    me "As expected."
    me "The others didn't buy any either."
    mc ". . ."
    menu:
        with dis
        "[gr]Buy one":
            $ syndicatestatue = True
            show gcc 50
            mc "You know what?" with dis
            mc "Sure, give me one. Send it to the WRE headquarters."
            mc "For three eternals you're basically giving it for free."
            mc "Hard to pass up, right?"
            show screen eternals with dis08
            play sound coins
            $ money -= 1
            pause .05
            $ money -= 1
            pause .05
            $ money -= 1
            pause .3
            show gcc 51          
            hide screen eternals
            me "Ah..." with dis 
            me "So... it truly can land on a different side."
            show gcc 50
            mc "What...?"
            show gcc 51
            me "Thank you for your purchase."
            me "God bless your kind soul."
            show gcc 50
            mc "Hmph..."
            mct "I should keep moving." 
        "Don't buy it":
            mc "Smart people, those “others”." with dis08
            mct "I should keep moving." 
    mct "This old man attracts more attention than anything else."
    $ citadeltime += 4
    stop music fadeout 8
    play music3 ["<silence 3>"] 
    queue music3 arabia1 
    jump arabiamarket 
label arabiamarket4: 
    $ amarket4 = False
    play sound2 footsteps3
    scene gcc 52 with dis2
    mct "Hmmm... I'm gonna ask around here." with dis
    mct "The guards don't seem to be paying much attention to this corner."
    play sound3 footsteps3
    show gcc 53
    mc "*Clears throat* Hello!" with dis15
    show gcc 54
    me "Hmm?"with dissolve
    play sound6 whoosh3b
    show gcc 56
    me "Ahhh... yes... YES!" with hpunch
    me "I knew my prayers wouldn't go unheard! Thank you, Lord Gilgamesh!"
    me "And welcome to my humble shop, traveler!"
    me "Are you from these lands?"
    show gcc 55
    if novapath:
        mc "I'm not, it's only the second time I've been in this server."
    else:
        mc "I'm not, it's the first time I've been in this server."
    show gcc 56
    me "Ahh well, in that case... let me welcome you to Valley of the Kings! Or as the pros like to call it, VotK!"
    me "Let me guess... you're looking for a brand new sword!"
    show gcc 55
    mc "Uh... not really, no."
    show gcc 57
    me "Oh, I see... you're interested in my dromedaries!" with dis
    me "Well, check it out!"
    me "This one's Humpfrey, the best dromedary in all of Valley of the Kings!"
    me "He can trek across the desert and take you to Egypt without needing to sip a single drop of water!"
    show gcc 55
    mc "Um... I'm in no need of a camel, but thank you." with dis 
    mc "Actually, I just–"
    play sound whoosh3b
    show gcc 58
    me "Alright, alright, you win!" with hpunch 
    me "Take it, take it! My best staff! It's yours!"
    me "You always wanted to feel like Sun Wukong, didn't you? Well, now you can! And for just 350 eternals!"
    me "I'll even make you a discount to–"
    show gcc 59
    mc "O-Okay, I'm sorry to interrupt, but I'm a bit short of money at the moment, and... I already have this personal quirky merchant who seems to follow me everywhere and sells me all kinds of useless stuff and animals."with hpunch
    mc "It'd feel like I'm betraying him."
    mc "For some weird reason..."
    show gcc 61
    me "Well, can't say I don't respect that." with dis12
    me "Loyalty between a customer and their extravagant merchant is a value that’s sadly fading away."
    show gcc 60
    mc "You've got the spirit, though."
    mc "Keep that up, and I'm sure you'll go far."
    show gcc 56
    me "Aight, aight! I don't wanna be too pushy."with dis
    me "I like to let my clients shop at their own pace."
    me "But if you've got any last-minute buys to make before leaving the Citadel, please, swing by Alfonso's!"
    if haremnumber >= 3 and harempath:
        me "You can't leave the place without picking up a beautiful gift for your beautiful girl."
        show gcc 55
        mc "*Chuckles* I'm sure they'd love it, that's true. I'll keep it in mind."
        mc "Thank you, Alfonso."
        show gcc 61
        me "Heh... “they”, huh..."with dis 
        me "And here I thought harems were only a thing in this server."
        show gcc 60
        mc "Oh, well, um..."
        mc "I-It's complicated."
        show gcc 61
        me "Oh... so it's nothing serious, I see."
        show gcc 60
        mc "No, no, it {i}is{/i} serious."
        mc "Like, I want it to be serious."
        mc "As cheesy as it might sound, I'm... I'm in love with all of them, and I just can't help it."
        show gcc 61
        me "But do they know about each other?"
        show gcc 60
        mc "Well... some do. Some others... suspect it, I think?"
        mc "I would've told everyone after the accident in the alley, when I finally sorted out my thoughts, but Nancy insisted that I shouldn't, not yet."
        show gcc 61
        me "I see..."
        me "You think Nancy wants to play the role of some sort of intermediary? Because she wants it too?"
        show gcc 60
        mc "Exactly! That's what she implied."
        mc "She asked me to keep acting like normal, to let my feelings take over at every moment, and to leave all the worrying to her."
        mc "So... that's what I'm trying to do."
        show gcc 61
        me "Do you think these girls love you as much as you love them?"
        show gcc 60
        mc "Man, I really hope so."
        mc "Sometimes I feel like–"
        mc ". . ."
        play sound slam2
        play sound2 slam
        show gcc 62
        mc "WAIT A SECOND, WHY THE FUCK AM I EVEN TELLING YOU THIS?!" with hpunch 
        show gcc 56
        me "Alfonso’s place is a one-stop shop! Camels, weapons, clothes, pots – even psychology services!" with dis
        me "Or a bar, if you want to call it that. My pops used to say the only difference between a bartender and a psychologist is whether you’re holding a drink or not."
        me "Want a beer?"
        show gcc 55
        mc "*Snorts* Maybe later."
        mc "But anyway, thank you for listening, I guess."
        mc "I really should keep moving now, I'm trying to keep a low profile."
        show gcc 56
        me "Of course! Have a lovely day and come back if you need me!"
    else:
        show gcc 55
        mc "*Chuckles* Will do. Thank you, Alfonso."
    show gcc 56
    me "Take care!"
    show gcc 55
    mct "What a nice fella. I should recommend him to become the official WRE partner in this server."
    mct "I've gotta remember to mention it to Nancy."
    $ citadeltime += 5
    jump arabiamarket 
label arabiaposmarket:
    if anniefingers:
        mod "Use Cheats in the Heart menu now to change your resolution on the Space server if you'd 
        like to see path differences."
    mct "Where the hell is Samir?"
    if anniefingers and not vasilhelp:
        com "Huh... funny running into you in the exact same position."
        com "Makes me wonder, is it you drawing in the Xenomorphs, or the other way around?"
        show gcc 73
        mc "*Turning around* Hmm?" with dis
        mc "Are you talking to me?"
        show gcc 74
        com "What?"
        com "Have you forgotten me already?"
        show gcc 73
        mc "Eh...?"
        mc "Am I supposed to kno–"
        play sound impact3
        play sound3 deception
        stop soundloop2
        $ renpy.music.set_volume(0.0, channel='music3')
        show haslerremember with flashfast
        pause .33
        play sound2 impact3
        play sound4 deception
        play soundloop2 citadelmarketsound
        $ renpy.music.set_volume(0.75, channel='music3')
        scene gcc 73 with flashfast
        pause .2
        mc "Shit..." with dis14
        mc "You're the guy who had me plant the bomb at the Astrocorp station... back when we first learnt about the Xenomorph plague!"
        show gcc 74
        com "And you did a good job at that, I must admit."
        com "The whole station blew up into a million pieces."
        show gcc 73
        if chopchop == 3 and not xenodeath1 and not xenodeathgun:
            mc "Yeah... we only came out of that place alive thanks to an artifact I didn't even know I had."
        else:
            mc "Yeah... tell me about it."
        mc "Did you manage to escape in time?"
        show gcc 74
        com "I... didn't. But that doesn't matter."
        com "It was a far better fate than turning into one of those things."
        show gcc 73
        mc "Hmph, fair enough."
        mc "So, you're here because of the Big Hunt event too?"
        show gcc 74
        com "I'm not interested in the Gems, even though anything that gets players out hunting those vile creatures is welcome."
        com "So... my goal's different, but yes, I'm after those monsters too."
        show gcc 73
        mc "We came here because of the Sultan, Hassan al-Rashid."
        mc "According to the current rankings, his team's killed over a million Xenomorphs in just a few days."
        mc "Although... this server seems pretty chill so far, so I don't know."
        show gcc 75
        com "Doctor Mercer must be stopped." with dis
        show gcc 76
        mc "Stopped? I thought you'd be happy they're hunting so many Xenos."
        mc "And who's Doctor Mercer?"
        show gcc 75
        com "She's the reason the Xenomorphs infested the dating station. She wants to make the plague bigger."
        com "And I'm sure she's the reason the Sultan's kill count is so high."
        com "She must have some secret underground lair with MILLIONS of them!"
        show gcc 76
        mc "A-ha..."
        mc "And how do you plan to dismantle that... “secret underground lair”...?"
        show gcc 74
        com "I will kill Doctor Mercer, and anyone related to those monsters." with dis
        com "I might have lost my girlfriend and my job at the Brigade, but my resolve's stronger than ever."
        com "And don't try to stop me. You, women, elders, or even children – I'll kill ANYONE who stays in my way."
        show gcc 73
        mc "Okay, okay... jeez, calm down, man."
        mc "You stick to your mission, I’ll stick to mine."
        mc "No one needs to get in anyone's way."
        show gcc 74
        com "Good."
    play sound footsteps3
    scene gcc 77
    sam "Well... it's official – our initial plan was a bust." with dis17
    sam "My lieutenant's nowhere to be found, so we'll have to try getting into the palace another day."
    sam "Can't do it without him."
    show gcc 78
    mc "What?!"
    mc "No! It has to be today!"
    mc "Dalia's in the palace!"
    show gcc 79
    sam "We can meet up with her outside."
    sam "Or... maybe we could also try dressing up as women and take the same route she did."
    show gcc 78
    mc "That was not the deal, our deal was to get all three of us inside the palace."
    mc "TODAY."
    show gcc 79
    sam "Well..."
    sam "I don't know what you want me to tell you, man."
    show gcc 80
    je "*Panting* F-Fuck..." with dis17
    je "*Panting* I-I almost got caught, but I managed to sneak past the jackals."
    je "*Panting* G-God, a guard caught me peeking at the palace entrance, so I had to eat an entire onion to avoid suspicion."
    je "*Gagging* That's gonna bite me later..."
    mc "Well, sorry to say, Jerry, but Samir lost his lieutenant or whatever, so your sacrifice was good for nothing."
    play sound deception2
    play sound7 deception2
    play sound2 whoosh6
    show gcc 81
    je "What...?" with pu
    je "How?"
    show gcc 82
    sam "Sometimes things don't go our way. It is what it is."
    show gcc 81
    je "What?"
    je "Bro, you're fucking useless."
    show gcc 82
    sam "Says the guy who hasn't done shit yet."
    sam "Why are you even here?"
    if anniefingers and not vasilhelp:
        show gcc 83
        com ". . ." with dis14
        show gcc 74
        com "So... you want to enter the palace?"
        show gcc 73
        mc "That was the plan, yeah."
        com "Hmm..."
        show gcc 74
        com "You know..."
        com "I could help you... in exchange for a little something."
        show gcc 73
        mc "Really?"
        mc "What is it?"
        show gcc 75
        com "You need to kill Doctor Mercer." with dis
        show gcc 76
        mc "W-What?"
        show gcc 75
        com "You need to kill Doctor Mercer and ANYONE remotely tied to the Xenomorph plague inside the palace. Servants included!"
        com "Do that, or we've got no deal."
        show gcc 76
        mc "Um..."
        mct "Jeez, this guy's unhinged."
        mct "Although... perhaps I should play along for now."
        mct "Once I’m inside the palace, I don’t really have to follow through."
        mct "But right now, I need to move fast. I'm worried Dalia might be in trouble."
        mc "Mmph, okay. Deal."
        show gcc 74
        com "Very well..." with dis
        com "Listen, this is how we're gonna do it: those guards are incredibly fast and strong, but they're dumb as rocks."
        com "They've been told to stop any fights in the market, so if we make it look real, they'll come running."
        com "If we can distract the one by the arch at the south end of the market, you can slip past him."
        com "There you'll find a trapdoor that'll lead you directly to the palace."
        show gcc 79
        sam "That's true, that's the route I was planning to take too."with dis
        show gcc 74
        com "I need a man to fight me and distract the guard, while the other two slip into the Palace."with dis
        com "And you need to choose now. We're running out of time."
        show gcc 73
        mc "Gotcha."
        show gcc 84
        mc "Okay..." with dis12
        mct "It's time to think fast."
        mct "Who should I take with me...?"
        menu:
            with dis
            "Samir{#0.8,companion}":
                mc "Samir, you're with me." with dis08
                mc "Jerry, you're in charge of starting a fight with Hasler."     
            "[gr]Jerry{#0.8,companion}":
                $ jerrypalace = True
                mc "Jerry, you're with me." with dis08
                mc "Samir, you're in charge of starting a fight with Hasler."
        show gcc 73
        mc "Good?" with dis
        show gcc 74
        com "Yes."
        com "Now, everyone, move!"
        com "And you better stay true to your word..."
        scene gcc 85 with dis22
        pause
        play sound footsteps3
        show gcc 86
        bla "As instructed, the four men quickly move into their positions." with dis2
        mct "I wonder if Dalia's still inside or if she managed to get out already."
        mc "*Sighs* (If only I could travel within servers or jump to the exact location of someone I know...)"
        mct "But I guess that's a power only Calypso has."
        play sound2 punch 
        play soundloop citadelcrowd fadein 2
        show gcc 87
        com "FUCK YOU, COCKSUCKER!" with dis14
        play sound7 fightcitadel
        com "TAKE THIS!"
        play sound punch
        play sound2 fallkitchen
        if jerrypalace:
            show gcc 88b
        else:
            show gcc 88
        com "THIS WILL TEACH YOU NOT TO TOUCH MY WIFE!" with hpunch 
        player2 "My vases!" with hpunch
        player "KILL HIM!" with hpunch 
        mct "H-Holy shit, he was serious about putting up a “real” fight."
        play sound3 fightcitadel
        play sound footstepsmonsterleave
        scene gcc 89
        bla "The guard abandons his post to break up the fight, as you spot Commander Hasler fleeing the scene." with dis15
        mc "It worked!"
        mc "It's now or never! Come on!"
        play sound8 run
    else:
        play sound footstepsmonster
        show gcc 78
        mer "So it turns out my informants were not wrong after all..." with dis15
        mer "It's really you."
        sam ". . ."
        mc "Oh, shit..."
        show gcc 90
        mc "*Turning around* U-Um..." with dis12
        mc "G-Good evening, my lady."
        mc "Are you working with our beloved Sultan? If so, please, let him know that we're delighted to–"
        show gcc 91
        mer "*Shrill giggle* Oh, please, there's no need for theatrics."
        mer "I've been looking for you for a long time, [nickname]."
        show gcc 90
        mc ". . ."
        mc "E-Excuse me?"
        mc "Do... do you know me...?"
        show gcc 91
        if not anniefingers or pay500: 
            mer "Not personally, but I've heard wonders about you."
            mer "Even before I started working with the Sultan!"
            mer "*Giggles* I’d go so far as to say I’m a big fan of yours."   
        else:
            mer "Of course I do. Have you forgotten about me already?"
            show gcc 90
            mc "Eh?"
            mc "You...?"
            mc "Hmm..."
            play sound impact3
            play sound3 deception
            stop soundloop2
            $ renpy.music.set_volume(0.0, channel='music3')
            show mercerremember with flashfast
            pause .33
            play sound2 impact3
            play sound4 deception
            play soundloop2 citadelmarketsound
            $ renpy.music.set_volume(0.75, channel='music3')
            scene gcc 90 with flashfast
            pause .2
            mc "Shit..." with dis14
            mc "I remember now..."
            mc "You're... Doctor Mercer!"
            mc "The woman I found at the Astrocorp station back when we first learnt about the Xenomorph plague!"
            if not freemercer:
                mc "The one I... left handcuffed."
                mc "Um... I-I'm so sorry about that, really."
                mc "I didn't know who to trust back then, so I just–"
                show gcc 92
                mer "Please, don't even worry about that..."
                mer "You had every right to distrust me back then."
                show gcc 91
                mer "It's all forgiven now."
                show gcc 90
                mc "Oh."
                mc "Why, thank you."
                show gcc 91
                mer "More than forgiven, actually. I’d go so far as to say I’m a big fan of yours."    
            else:
                mc "The one who... manipulated Vasil and tried to... bring Xenomorphs into the real world."
                show gcc 92
                mer "Oh, my poor Vasil..."
                mer "So innocent, yet so naive..."
                show gcc 91
                mer "He ended up serving a much bigger purpose after that, so don't you worry."
                mer "He always liked you, you know? Just like I like you."
                show gcc 92
                mer "Well... more than “liking”, actually."
                mer "*Giggles* I’d go so far as to say I’m a big fan of yours."    
        show gcc 90
        mc "A fan...?"
        mc "How do you know who I am?"
        show gcc 91
        mer "You see... for the past few weeks, I’ve been researching everything I can about Eternum’s top players, looking for the most capable... warrior."
        mer "And I must admit, you're one of my favorites."
        mer "You may not have the extensive record of, let's say, Thanatos, but your progress has been remarkably fast."
        show gcc 90
        mc "Erm..."
        mc "Well, thank you."
        show gcc 91
        if not anniefingers or pay500:
            mer "I was just returning from a quick meeting with an old friend when I spotted you here in the market!"
            mer "*Giggles* Pardon my forwardness, but I've gotta ask..."
        else:
            mer "I was just returning from a quick meeting with Commander Hasler when I spotted you here in the market!"
            mer "Couldn't believe my eyes! What a day full of reunions!"
            show gcc 90
            mc "Oh... I remember Commander Hasler."
            mc "Are you two... on good terms now?"
            show gcc 91
            mer "We are!"
            play sound7 chestbuster3 volume 0.7
            play sound8 chestbuster1 volume 0.7
            play sound impact3
            play sound3 deception
            stop soundloop2
            play music xenosong1
            $ renpy.music.set_volume(0.0, channel='music3')
            show gcc 93
            mer "{i}After exchanging ideas, he finally saw the potential in my investigation." with flashfast
            mer "{i}He even offered himself to join my team and help me!"
            mer "{i}Isn't it wonderful?!"
            mc "{i}Y-Yeah, very wonderful."
            mer "{i}Indeed..."
            play sound2 impact3
            play sound4 deception
            stop music
            play soundloop2 citadelmarketsound
            $ renpy.music.set_volume(0.75, channel='music3')
            scene gcc 91
            mer "But let's get back on topic..." with flashfast
        mer "Would you mind joining me for a short walk through the palace gardens? I promise I won’t take up much of your time."
        mer "Nothing would make me happier than having a conversation with [nickname] himself and hear of his adventures."
        show gcc 90
        mc "A walk...?"
        mc "Um... I don't think we..."
        show gcc 91
        mer "Please, allow me to be clear."
        mer "I'm only working with the Sultan out of convenience. I couldn’t care less about him, the event, or those Gems of Doom you’re holding."
        mer "I'm just interested in a conversation with you. If you can indulge me, I’ll also answer any questions you may have."
        mer "I assume you came here for intel. Am I wrong?"
        show gcc 90
        mc "Uh..."
        mc "Yeah... you're right."
        mct "Something doesn't add up here..."
        mct "We’re looking for a way into the palace, and suddenly this woman shows up, offering to help us get in and even giving us information? This all feels way too convenient."
        mct "But... even if it's a trap, she's still my best chance. I might never find Dalia in this place unless she helps me."
        if not anniefingers or pay500:
            mct "Not to mention she's probably related to the Xenomorph hunting event somehow."
        else:
            mct "Not to mention she's obviously related to the Xenomorph hunting event somehow."
        mct "I need to continue playing along until she tells me what I want..."
        mc "Uh..."
        mc "Okay, fine. I'll come with you."
        show gcc 91
        mer "Excellent!"
        mer "Although... I'm afraid I can only take you and one of your friends."
        mer "The guards would start asking too many questions otherwise."
        show gcc 90
        mc "Hmm..."
        mc "Sure... it's not a problem."
        show gcc 84
        mc "Okay..." with dis12
        mct "Hmm..."
        mct "Who should I take with me...?"
        menu:
            with dis
            "Samir{#0.8,companion}":
                mc "Samir, you're with me." with dis08
                mc "Jerry, you can wait for us here in the market."    
            "[gr]Jerry{#0.8,companion}":
                $ jerrypalace = True
                mc "Jerry, you're with me." with dis08
                mc "Samir, you can wait for us here in the market."
        show gcc 90
        mc "Alright, that's settled." with dis
        show gcc 91
        mer "Terrific."
        mer "Please, follow me."
        play sound footsteps3 fadein 1
        scene gcc 94 with dis22
        mer "These two men are coming with me." with dis
        mer "Kill anyone else who tries to come through this door."
        mer "Understood?"
        jac "Mmh."
        show gcc 95
        mer "This way, gentlemen!" with dis
        mer "Please, don't be shy..."
        show gcc 96
        mc "Hmmm..." with dis14
        mc "This smells very bad."
        if jerrypalace:
            je "Yeah, she gives me the creeps."
        else:
            sam "Well, at least she's kinda hot."
        mc "We better stay on our watch..."
    stop soundloop2 fadeout 8
    stop soundloop fadeout 8
    stop music3 fadeout 9
    scene black with dis3
    show screen afewminuteslater with dis25
    pause
    play music arabiatension fadein 1
    hide screen afewminuteslater
    scene gcc 97 
    with dis3
    pause
    if anniefingers and not vasilhelp:
        mc "Hmm... these must be the inner gardens." with dis2
        if jerrypalace:
            je "Haven't we already been here?"
        else:
            sam "Haven't we already been here?"
        mc "I don't think so. Or... well, I hope not."
        mc "*Looking at the sun's position* (Fuck, we've been here for too long already...)"
        mct "Dalia, where are you..."
        mc "Alright, we can't afford to waste any more time."
        if jerrypalace:
            mc "Let's split up and meet back at the Ishari base of operations Samir showed us earlier."
            je "Got it."
        else:
            mc "Let's split up and meet back at the base of operations."
            sam "Um... are you sure...?"
        bla "You hear whispers and footsteps approaching from outside, growing closer to your position."
        mc "*Whispering* Fuck, someone's coming!"
        show gcc 98
        mc "*Whispering* Should we go back?" with dis
        if jerrypalace:
            je "*Whispering* Do you remember the way?"
            je "*Whispering* I kinda got lost."
            mc "*Whispering* Fuck, I'm not sure either... this place's like a maze."
        else:
            sam "*Whispering* O-Okay, let's split up."
            sam "*Whispering* You stay here, I'll go back."
            mc "*Whispering* What?! No fucking chance."
            sam "*Whispering* Then what?!"
        mc "*Whispering* Okay... hear me out."
        mc "*Whispering* If it's a human, I think I can manage to talk my way out. Just let me do the talking."
        mc "*Whispering* And if it's one of those guards, I'll–"
        play sound footstepsmonstershort volume 0.75
        show gcc 99 with dis2
        aaa "Aaaahh... there you are." with dis12
        aaa "Welcome to the Citadel, gentlemen."
        show gcc 100
        mc "G-Good evening, my lady."
        mct "Think fast, think fast, think fast..."
        mc "The infiltration mission was a success. I need to take this prisoner to–"
        show gcc 99
        aaa "*Giggle* Oh, please, there's no need for theatrics."
        aaa "I've been looking for you for a long time, [nickname]."
        show gcc 100
        mc ". . ."
        mc "E-Excuse me?"
        mc "Do... do you know me...?"
        show gcc 99
        aaa "Of course. You could say I'm a big fan."
        show gcc 100
        mc ". . ."
        mc "Who are you...?"
        show gcc 99
        mer "I'm Irina Mercer, I work with the Sultan."
        show gcc 100
        mc "Mercer?"
        mc "You... you're Doctor Mercer?"
        show gcc 99
        mer "*Shrill giggle* I'm honored to see that you've heard of me."
        show gcc 100
        mc "How do you know who I am?"
        show gcc 99
        mer "We've been tracking that fool Hasler’s every move since he first set foot in the Citadel."
        mer "When my informants described the person he’d just been seen speaking to, I immediately knew it matched the descriptions of [nickname]."
        show gcc 100
        mc "Ah... I see."
        mc "But... why are you interested in me?"
        show gcc 99
        mer "I’ve been researching everything I can about Eternum’s top players, looking for the most capable... warrior."
        mer "I must admit, you're one of my favorites."
        mer "You may not have the extensive record of, let's say, Thanatos, but your progress has been remarkably fast."
        show gcc 100
        mc "Erm..."
        mc "Well, thank you."
        mc "Listen... I'm just looking for a girl, really. If you help me find her, we'll leave immediately and let you be."
        show gcc 99
        mer "Would you mind joining me for a walk through the gardens first? I promise I won’t take up much of your time."
        show gcc 100
        mc "A walk...?"
        mc "Um... I don't think we..."
        show gcc 99
        mer "Allow me to be clear."
        mer "I'm only working with the Sultan out of convenience. I couldn’t care less about him, the event, or those Gems of Doom you’re holding."
        mer "I'm just interested in a conversation with you. If you can indulge me, I’ll also answer any questions you may have."
        mer "I assume you came here for intel. Am I wrong?"
        show gcc 100
        mc "Uh..."
        mc "Yeah... you're right."
        mct "Something doesn't add up here. All this feels way too convenient."
        mct "But... even if it's a trap, she's still my best chance. I might never find Dalia in this place unless she helps me."
        mct "Not to mention she's obviously related to the Xenomorph hunting event somehow."
        mct "I need to continue playing along until she tells me what I want..."
        mc "Okay, fine. I'll come with you."
        show gcc 99
        mer "Excellent!"
        mer "Just... a small requisite, if you don't mind."
        mer "Your companion needs to stay behind."
    else:
        mc "*Whispering* Hey..." with dis2
        mc "*Whispering* Don't you feel like we've been walking in circles for an hour?"
        mc "*Whispering* Is she trying to disorient us?"
        if jerrypalace:
            je "*Whispering* Maybe we should go back to the Ishari base of operations Samir showed us earlier and think of a better plan."
        else:
            sam "Maybe we should just go back to the base of operations."
        mc "*Whispering* If we split up we should do that, yes."
        play sound footstepsmonstershort volume 0.75
        show gcc 99 with dis2
        mer "Is there any problem?" with dis12
        show gcc 100
        mc "No, nothing, sorry."
        mc "We were just... admiring the views."
        show gcc 99
        mer "In this courtyard you can find the Fountain of Purity."
        mer "However, from here on out, only me, one guard, and one guest are allowed."
        mer "So, you'll have to leave your companion behind."
        mer "I hope you don't mind."
        show gcc 100
        if jerrypalace:
            mct "First Samir, now Jerry..."
        else:
            mct "First Jerry, now Samir..."
        mct "She's obviously trying to get me alone."
        mc "If I come with you, will you answer all of my questions?"
        show gcc 99
        mer "Absolutely. A conversation is a two-way street, after all."
        show gcc 100
        mc "Hmph."
        mc "Okay then. Let's go."
        show gcc 99
    mer "Oh, and you'll have to leave your weapons and armor here."
    mer "Just... as a matter of precaution."
    show gcc 100
    mc "Sure..."
    if jerrypalace:
        scene gcc 101
    else:
        scene gcc 102
    mc "Alright... I'll go with Doctor Mercer." with dis12
    if jerrypalace:
        mc "You stay here, Jerry. I'll be right back."
    else:
        mc "You stay here. I'll be right back."
    mc "*Whispering* I don't trust this woman – she's gotta be planning something. If I'm not back in 15 minutes, leave on your own and try to find Dalia."
    mc "*Whispering* And stay alert."
    if jerrypalace:
        scene gcc 101b
        je "Understood." with dissolve 
    else:
        scene gcc 102b
        sam "Sure." with dissolve 
    show gcc 100
    mc "Alright, I'm ready." with dis12
    show gcc 99
    mer "You can leave your stuff with the guard on my left."
    mer "Please, follow me."
    show gcc 100
    mc "With pleasure..."
    play soundloop river fadein 5
    scene gcc 1 with dis3
    bla "You walk beside Doctor Mercer for several minutes as she relentlessly asks questions about your past battles and adventures, to which you respond with a mix of evasive answers and outright lies." with dis22
    mct "We're wasting time... I need to find Dalia and get out of here."
    mer "Ah, the Fountain of Purity..."
    mer "Don't you think it's beautiful?"
    play sound footsteps3 fadein 1
    scene gcc 103
    mc "Yeah, very much..." with dis2
    mc "*Sighs* Listen, I've been answering all of your questions."
    mc "Now it's my turn to get some answers."
    mc "I need to know how the Sultan’s getting so many kills for the Big Hunt event, and I need to know where the slave deliveries are being sent within the Cit–"
    play sound sword3
    stop music fadeout 1
    show gcc 104
    mc ". . ." with dis12
    mct "I knew it."
    play music2 arabiatension2 fadein 4 
    scene gcc 105
    mc "*Turning towards Doctor Mercer* Well..." with dis2
    mc "I was wondering how long you'd continue that little charade of yours. Thank you for not dragging it out."
    mer "It was no charade, [nickname]."
    mer "I really am a fan of yours."
    mc "*Sighs* Why don’t you just tell me what the fuck you really want?"
    mer "What I want? Have I not been clear enough yet?"
    mer "What I want..."
    play sound deception2
    play sound2 deception2
    show gcc 106
    mer "{sc=2}Is YOU.{/sc}"with hpunch 
    show gcc 107
    mc "What do you mean, “me”...?"
    show gcc 106
    mer "Strong, agile, fast, intelligent, and remarkably adaptable."
    mer "There are only records of you from a few months ago, and yet somehow, you’ve managed to obtain not one but two Gems of Doom – maybe even more!"
    mer "Your evolutionary metrics are off the charts!"
    mer "You are..."
    play sound deception2
    mersc "THE PERFECT HOST." with hpunchsubtle
    show gcc 107
    mc "What the hell are you talking about, you psycho bitch?"
    mc "Is this some kind of... sexual thing...?"
    show gcc 106
    mer "You asked how the Sultan's team is getting to kill so many Xenomorphs, didn't you?"
    mer "Well, I'll tell you..."
    mer "Turns out he and I have a {i}little{/i} arrangement."
    mer "Hassan backs me with his money and resources, and in return, I mass-produce hundreds of thousands of Xenomorphs every week."
    mer "His team can increase their kill count with each newborn Xenomorph, and I get to keep refining their biology!"
    mer "Each new batch is an improvement from the last – faster, stronger, DEADLIER!"
    show gcc 107
    mc "But... I thought that for a Xenomorph to be born, a human host was need–"
    mc "Oh, no..."
    show gcc 109
    mer "Yeah, well..." with dis12
    mer "Little sacrifices are sometimes necessary for the sake of progress, don't you think?"
    show gcc 108
    mc "You..."
    mc "You've killed hundreds of thousands of people just to use them as incubation pods?!"
    show gcc 109
    mer "*Shrill giggle* Turns out, both this server and Andromeda are crawling with NPCs!"
    mer "And they nourish my Xenomorph larvae just as well as real players do!"
    show gcc 108
    mc "Y-You're a fucking monster..."
    show gcc 109
    mer "*Shrill giggle* Not that we haven’t used our fair share of real humans, of course..."
    mer "Captured enemies have never served a better purpose!"
    show gcc 108
    mc "I've heard enough. Tell me where the captured Ishari girls are."
    mc "NOW."
    show gcc 106
    mer "And here's the best part!" with dis12
    mer "I'm so close to finally completing my experiments!"
    mersc "I can create the PERFECT ORGANISM!"with hpunch
    mersc "And the only missing piece... is the PERFECT host!"with hpunch
    play sound deception2
    mersc "YOU." with hpunch 
    show gcc 107
    mc "This conversation is over."
    mc "Tell me where the captured Ishari girls are. I won't ask again."
    show gcc 109
    mer "Oh, [nickname]..."with dis
    mer "These jackals are also a creation of mine. And the one pointing a spear at you is the strongest of them all."
    mer "This patio's got a magic blocker, but fear not, they can still move around just fine since they're the result of pure biology!"
    show gcc 106
    mer "*Shrill giggle* What I'm getting at is, there's no need to make this harder than it should be! So be a good boy and come with us to the incubation room, will you?" with dis
    mer "The process is almost painless, I promise..."
    show gcc 107
    mc "You truly are a rarity. Somehow a monster, a genius, and a complete idiot, all rolled into one."
    mc "You act like you've got it all figured out, yet your plan has holes everywhere."
    stop music2 fadeout 1
    play sound transformpower fadein 1
    play soundlow risingshort
    mc "And your first mistake... was thinking I'd even need a weapon." with dis12
    play music2 ["<silence 2>"]
    queue music2 epiccitadel
    play sound7 speed2
    play sound3 debris4
    play soundlow metalhit2
    scene gcc110b
    pause 0.9
    play sound gore
    play sound4 monstershriek
    scene gcc110 
    bla "In a split second, you wrench the spear from the colossal guard’s grip and drive it straight through him." with hpunchlongsubtle
    play sound6 fms
    play sound7 fms
    play sound8 whoosh6
    play sound2 monstershriek2
    scene gcc111 
    bla "Just as fast, the jackal whirls around and slams a punch into your stomach." with hpunchlongsubtle
    play sound dodge
    play sound3 rocks
    play soundlow debris2
    scene gcc112 with hpunch
    pause .3
    play sound4 ["<silence 0.1>", fallfull]
    scene gcc 113 with dis14
    pause
    scene gcc 114
    mc "*Coughing up* Son of a bitch..." with dis2
    show gcc 115
    mc "Argh... that was a good punch..." with dis12
    mc "I was not expecting them to be this fast."
    mc "This is gonna hurt tomorrow..."
    show gcc 116 with dis12
    show gcc116
    pause 0.01
    play sound fms
    play sound2 blood3
    play sound3 blood1
    bla "The creature manages to make only two staggering steps before collapsing due to the massive blood loss." with dis 
    jac ". . ."
    scene gcc 117
    mer "Yes... yes... YES!" with dis14
    mer "This is exactly what I was talking about..."
    mer "You took down the commander of the Jackal Army in one hit!"
    mer "{sc=2}*Shrill giggle* PURE POWER!{/sc}" with hpunch 
    play sound speed
    play sound2 debris3
    play sound7 fist
    play sound8 leathershort
    scene gcc118
    mer "{sc=2}*Choking* A-AAAarghhhHh...{/sc}" with hpunch 
    mer "{sc=2}*Choking* C-Cant... b-breathe...{/sc}"
    play sound3 leathershort
    show gcc 119
    mc "I'm done with your giggles." with dis12
    mc "Where's Dalia?"
    show gcc 120
    mer "W-Who?"
    show gcc 119
    mc "She was brought here with other Ishari girls to be sold as slaves."
    show gcc 121
    mer "*Giggles* O-Ohh... then she must've passed the Sultan's examination right here in this very courtyard!"with dis12
    mer "If she was discarded, she's probably in the incubation room already so she can have her belly filled with one of my b-babies..."
    play sound3 leathershort
    show gcc 119
    mc "Where's the incubation room?" with dis12
    show gcc 120
    mer "A-Aghhh... in... the b-basement of the palace."
    mer "T-The stairs are hidden behind a fake wall in the eastern section."
    show gcc 119
    mc "And if she wasn't?"
    show gcc 120
    mer "W-What...?"
    show gcc 119
    mc "You said that if she was discarded, she'd be sent to the incubation room."
    mc "But what if she wasn't?"
    show gcc 121
    mer "*Shrill giggle* Oh well, if she actually met Hassan's requirements..."with dis12
    mer "She was likely taken to the storage tower for... p-preparation."
    mer "The Sultan enjoys deflowering those poor girls up there, and let me tell you, *giggles* he’s anything but gentle!"
    mersc "*Shrill giggle* You should hear how those little pigs scream!" with hpunch
    play sound leathershort
    scene gcc 118
    menu:
        with dis14
        "[gr]Kill her":
            $ mercerkill = True
            play sound2 bonebreak
            play sound bonebreak
            play soundlow necksnap
            scene gcc 122 with hpunch
            pause
        "Let her go":
            pass
    scene gcc 123 with dis12
    play sound fallfull
    pause
    if not mercerkill:
        mer  "Eh...?" with dis
        show gcc 124
        mer "What...?" with dis 
        mer "Why... why didn't you kill me?"
        mc "You're not worth it."
        mer "E-Ehh...?"
        mer "Is that..."
        mer "MERCY...??"with hpunch
        mer "No... no, no, no... that is such a weak trait..."
        mersc "MY PERFECT HOST CAN'T BE WEAK." with hpunch
        mc "I won't waste another second on trash like you."
        mc "Now shut the fuck up."
    scene gcc 125 
    mct "I can't fight against an entire army of these jackals – I need to find Dalia and leave this cursed place at once." with dis14
    mct "I know she can more than handle herself, but... these people don't seem to know any limits."
    mct "I must hurry."
    stop music2 fadeout 8
    stop soundloop fadeout 7
    scene black with dis27
    show screen meanwhile with dis25
    pause 
    play music2b arabiatension fadein 1
    scene gd 1 
    hide screen meanwhile
    with dis27       
    d ". . ." with dis
    play sound doorecho
    show gd 2 with dis
    pause
    play sound2 footstepsmonstershort
    scene gd 3
    bla "Two jackal guards stride into the room where Dalia's been waiting for several minutes." with dis22
    play soundlow footsteps3
    show gd 4 with dis17
    ora "Ah... hello again!" with dis17
    ora "I'm terribly sorry for keeping you waiting, young lady." 
    ora "But... ah, looks like the maids already worked their magic on your hair!"
    ora "You look perfect."
    show gd 5
    d "I thought you were blind."
    show gd 4
    ora "*Chuckles* My eyes might be blind in the real world, but in Eternum? I see clearer than anyone else, trust me."
    ora "You know how some people are just {i}connected{/i} to this place on another level? Well... that’s me."
    ora "Here, I can see all that surrounds me."
    ora "Like... a whole new sense."
    show gd 5
    d "Ah... yeah... fascinating."
    d "But anyway... where's Hassan?"
    show gd 4
    ora "*Chuckles* Oh my, so impatient!"
    ora "Hassan's wives usually aren't this... {i}eager{/i} their first time."
    show gd 5
    d "Believe me, I'm anything but eager."
    d "I just need information."
    show gd 4
    ora "He'll be here shortly."
    ora "But I warn you, you're not allowed to speak in his presence unless he gives you permission."
    ora "And you'll need to obey every command he gives."
    show gd 5
    d "I see..."
    d "*Sighs* This has been a waste of time."
    show gd 6
    d "Welp, in that case, I'll be on my way!" with dis12
    d "Thank you for the free hair styling, and see yo–"
    play sound fms
    play sound2 metalhit2
    scene gd 7
    bla "The guards quickly block the room's only exit." with vpunchslow
    show gd 8
    d ". . ."
    show gd 9
    ora "Oh, come on... did you really think you could just come and go whenever you wanted?" with dis12
    ora "You are Hassan al-Rashid's property now."
    show gd 10
    d "Look, I just came over to get some info about the Big Hunt event, that's all."
    d "I don't even care about what you psycho weirdos do in here."
    d "Let me go and I won't hurt you."
    d "'Kay?"
    show gd 9
    ora "*Laughs* How endearing."
    ora "These albino jackals are Doctor Mercer's finest creation, young flower."
    ora "At least... until she completes her Perfect Organism research."
    ora "Getting to learn how strong and fast they can get would be a... let's say, very painful lesson for you."
    show gd 10
    d "What the fuck do you even want from me?"
    show gd 9
    ora "Wasn't the Sultan clear enough?"
    ora "I need you to prepare and lie on the Bed of Defloration until Hassan arrives."
    ora "And be fast, would you?"
    show gd 11
    d "Lie on the bed of..."
    show gd 12
    d "*Turning around* . . ." with dis14
    show gd 13
    d "*Shudders* U-Ugghh..." with dis12
    d "T-Thank god I didn't sit on there."
    show gd 9
    ora "Come on... start undressing."
    ora "We're running out of time and you still need to pass the inspection."
    show gd 14
    d "W-What? What inspection?"
    d "A-And I'm not getting naked, bitch, stop insisting."
    show gd 9
    ora "I need to ascertain that you're indeed still a virgin."
    ora "Don't worry, I'll also be here the whole time to make sure everything goes smoothly."
    show gd 14
    d "Y-You guys are certified freaks."
    d "I'll come back with backup and burn this whole place to the ground whenever I get the chance."
    show gd 9
    ora "*Chuckles* I'm sure you will..."
    ora "Now please, focus on the task at hand."
    ora "Get naked, lie on the bed, and open your legs."
    show gd 14
    d "FUCK. YOU."
    play sound footsteps3 fadein 1
    show gd 16
    ora "*Sighs* Agh..." with dis2
    ora "I know you're trying to buy time, hoping for [nickname] to come and save you..."
    ora "But I'm sorry, sweetie, he's not coming."
    show gd 15
    d "W-What...?"
    d "How do you..."
    d "D-Do you know us...?"
    show gd 16
    ora "He finished a quick meeting with our scientist just now."
    ora "I'm sorry to be the one to tell you this, darling... but he left."
    d "What? He'd never do that."
    ora "Huh, you should’ve seen how his eyes lit up when we offered him a Gem of Doom. He must've been after them for a while, huh?"
    show gd 15
    d "A... Gem?"
    show gd 16
    ora "Indeed."
    ora "Hassan's going to win the Big Hunt event."
    ora "Once it's over, he'll give the Gem to [nickname] in exchange for becoming an ally in the coming war."
    ora "And... well, he also accepted to hand you over to join the Sultan's harem."
    show gd 15
    d "But..."
    show gd 17
    d ". . ." with dis17
    d "You're lying."
    show gd 18
    ora "I know it's hard to accept, but the sooner you do, the better. That's just how men are."
    ora "You can't fight back, and no one's coming to save you."
    ora "You literally have no choice but to join the Sultan's harem."
    show gd 17
    ora "And hey, the first time is always the worst." with dis
    ora "After that, the advantages clearly outweigh the downsides."
    ora "You'll have everything you've ever dreamed of!"
    d ". . ."
    d "And..."
    d "What would I have to do, exactly...?"
    show gd 18
    ora "You need to surrender the purity of your body to the Sultan."
    show gd 17
    ora "Sounds like a big deal, but trust me, it’s really not. Just try to enjoy it."
    d ". . ."
    d "And how..."
    d "How long will it take?"
    show gd 18
    ora "Well... that depends on you."
    ora "The more cooperative you are, the sooner it'll all be over."
    show gd 19
    d ". . ." with dis17
    d "...Fuck."
    d "*Sighs* Okay..."
    d "You win. I'll..."
    d "I'll do it."
    show gd 18
    ora "Good girl..."
    ora "Now, undress. Take everything off."
    show gd 19
    d ". . ."
    d "Alright..."
    $ renpy.music.set_volume(0.6, channel='soundlow2')
    show daliaknife1 with dis14
    play sound7 ["<silence 2.4>", dks1]
    play sound2 ["<silence 2.4>", impact4]
    pause 2.5
    stop music2b
    play sound3 slowmo
    pause 2.6
    play sound6 dks2
    pause 0.2
    play soundlow whoosh7
    scene gcctransr
    pause 0.13
    play sound8 runfastshort
    show daliaknife2
    pause 3.6
    play soundlow2 whoosh7
    scene gcctransl
    pause 0.13
    play sound8 runfastshort
    play sound5 ["<silence 0.3>", dks3]
    show daliaknife3
    pause 3.4
    play soundlow whoosh7
    scene gcctransr2
    pause 0.13
    play sound8 runfastshort
    play sound4 ["<silence 0.3>", runfastshort]
    show daliaknife4
    pause 0.8
    play sound5 deception2
    play sound6 punch
    play soundlow leather2
    scene gcctransr3
    pause 0.13
    play sound debris4 volume 0.7
    scene gd 19b with hpunch
    play music2 ["<silence 2.5>"]
    queue music2 arabiatension2
    play sound2 ["<silence 0.3>", fms]
    play sound3 ["<silence 0.7>", fms]
    play sound5 ["<silence 0.7>", fallfull]
    play sound4 ["<silence 0.7>", sworddrop]
    pause .7
    ora "*Panting* E-E-Ehgh...? "with dis17
    show gd 20
    d "Enough fucking bullshit."
    show gd 19b
    ora "W-What just happened?!" with hpunch 
    show gd 20
    d "What do you mean? I thought your super duper ultra blind-but-not-blind vision could see everything."
    d "What happened? Some kind of interference?"
    show gd 19b
    ora "GUARDS!" with hpunch 
    show gd 20
    d "Your dogs are dead."
    if daliapath:
        d "And now, if you're done making up shit [mc] would never do... I think it's time for you to answer some of my questions."
    else:
        d "And now, if you're done making up shit about [mc] like we're some kind of couple or whatever... I think it's time for you to answer some of my questions."
    d "How's Hassan's team getting so many Xenomorph kills?"
    show gd 19b
    ora "W-What?"
    show gd 20
    d ". . ."
    d "I'm gonna ask you again, and this time you're gonna give me a clear, straight answer... or I'll slit your throat as easily as opening a bag of potato chips."
    d "How is Hassan's team getting so many kills for the event?"
    show gd 19b
    ora "D-Doctor Mercer!" with hpunchsubtle
    ora "She uses NPCs and players as hosts, incubating thousands of Xenomorphs every week!" with hpunchsubtle
    ora "T-Then the Sultan's team eliminates the newborn Xenomorphs!" with hpunchsubtle
    ora "He wants the Gem of Doom to sell it and obtain enough resources to take control of the entire Valley of Kings!" with hpunchsubtle
    show gd 20
    d "Ahh..."
    d "I see... that explains a lot."
    d "Thank you."
    show gd 19b
    ora "P-Please don't kill me!"
    show gd 20
    d "Not yet."
    d "First, you're gonna show me the way out of this maze."
    d "And then, you’re gonna go straight to wherever they’re making those abominations and order the jackals to destroy it all."
    d "If you don't do that, I'll be back. And it won't end well for you."
    d "Do you understand?"
    show gd 19b
    ora "YES! PERFECTLY!" with hpunchsubtle
    show gd 20
    d "Good girl..."
    scene gd 20b with Dissolve(3.3)
    mc "(F-Fucking hell... who built this place?)" with dis17
    mct "I keep climbing stairs, but it feels like there's always one more floor..."
    play sound2 microphonesound
    ha "{sc=1}{i}*Via loudspeakers* Guards of the Citadel, heed my command!{/i}{/sc}" with dis12
    ha "{sc=1}{i}Intruders have dared to trespass within the palace!{/i}{/sc}"
    ha "{sc=1}{i}Kill ANY Ishari you find within the Citadel walls on the spot!{/i}{/sc}"
    ha "{sc=1}{i}Find the intruders and bring their heads before me!{/i}{/sc}"
    mct "Oh shit... that's not good."
    mct "I need to continue, I can't stop now."
    if jerrypalace:
        scene gcc 98 with dis22
        mct "Fuck, now I'm back to where I started..."with dis12
        mct "And where the hell is Jerry?!"
        mct "I told him to wait here!"
        scene gd 28
        mct "Did he run away...?" with dis12
        mct "Bloody coward..."
        if not jerrytalk:
            mc "*Sighs* (Although... well, to be fair, I did tell him to do exactly that if I didn’t make it back.)"
            scene gd 29
            mct "In any case, I have no time to worry about Jerry now." with dis
        else:
            mc "*Sighs* (Although... well, to be fair, I did tell him to do exactly that if I–)"
            je "{sc=2}HEEEEELP!{/sc}" with hpunch 
            scene gd 29
            mct "Huh...?" with dis
            mct "Was that him?"
            mct "Fuck, what the hell has he gotten himself into this time?!"
            menu:
                with dis
                "[gr]Rescue Jerry":
                    $ jerryfriend = True
                    mct "Goddammit, Jerry!" with dis
                    play sound footstepsmonster
                    scene gd 30 with dis22
                    je "*Crawling backwards* Fuck, fuck, fuck..." with dis15
                    je "E-EASY, BOY!" 
                    je "C-Calm down, please... I'm not a menace!"
                    play sound2 footstepsmonstershort
                    scene gd 31
                    je "And I didn't steal anything, I swear!" with dis2
                    je "I-I'm not even a real Ishari!"
                    je "I was just trying to help out my friends!" with hpunch 
                    play sound sword3
                    scene gd 32
                    bla "Ignoring Jerry's desperate pleas, the guard raises its spear, ready to deliver a single, fatal strike." with dis12
                    play sound2 fall3
                    play sound3 debris3
                    scene gd33
                    je "{sc=2}AAAAAWWW SHIT, NOT AGAIN!{/sc}" with hpunch 
                    je "{sc=2}It's even worse when you see it coming!{/sc}" with hpunch 
                    je "{sc=2}AAAAAAAARRGHHH!!!{/sc}" with hpunch 
                    play sound risingshort
                    stop music2 fadeout 3
                    play soundlow wind4
                    pause 1.2
                    play sound2 rocks
                    scene gd 34 with vpunch
                    pause 
                    show gd 35
                    je ". . ." with dis12
                    je "Eh...?"
                    je "I'm... not dead...?"
                    je ". . ."
                    je "I'm..."
                    je "I'M NOT DEAD!"with hpunch
                    je "THE CURSE IS BROKEN!"with hpunch 
                    play sound fms
                    play sound2 blood3
                    play sound3 blood1
                    show gd 35 with vpunchslow
                    play music2 epiccitadel fadein 4
                    pause
                    play sound7 clothes3
                    scene gd 36
                    je "*Turning around* Huh...?" with dis15
                    play sound blood1 fadein 2
                    show gd 37 with dis22
                    mc "Hmmm..." with dis2
                    show gd 38
                    mct "This palace is way too damn big." with dis14
                    mct "How am I supposed to figure out which one of these is the “storage tower”?"
                    mct "I didn’t think this place would be such a maze..."
                    show gd 39
                    mc "Jerry, I need your help!" with dis08
                    play sound debris
                    show gd 40
                    je "*Standing up* . . ." with dis
                    show gd 39
                    mc "I’m pretty sure Dalia’s in one of these towers, but there’s still a chance she’s in the incubation rooms!"
                    mc "I need you to go to the dungeons to check!"
                    show gd 40
                    je ". . ."
                    show gd 39
                    mc "JERRY!" with hpunch 
                    show gd 40
                    je "Ye..."
                    play sound whoosh7
                    show gd 41
                    je "Y-YES, MY GENERAL!" with hpunch 
                    show gd 39
                    mc "If she's not there, retreat and go back to an Exit Portal immediately."
                    mc "AND DON'T DIE."
                    show gd 41
                    je "YES, SIR!" with hpunch 
                    je "I WON'T FAIL YOU!" with hpunch 
                    play sound run
                    show gd 42
                    bla "Jerry sprints away." with dis15
                    mct "Alright..."
                    mct "I have to keep going. Stopping isn't an option."
                "Ignore his cries for help": 
                    mct "Arghhh, I have no time to worry about Jerry now!" with dis
        mct "What if Dalia's being used in some twisted experiment by that mad scientist’s crew?"
        mct "Or... even worse, what if the Sultan's trying to..."
        mct "FUCK! I NEED TO FIND HER!" with hpunch 
        mct "NOW!" with hpunch
    else:
        scene gd 20c with dis22
        mct "Fuck, now I'm back to where I started..."with dis12
        mc "Huh...? Samir!" 
        show gd 21 with dis14
        mct "What the hell is he doing...?" with dis08
        mc "Samir!"with hpunch 
        play sound whoosh6
        play sound2 debris3
        show gd22
        sam "AAGH!" with hpunch 
        sam "F-Fuck, you scared me!"
        scene gd 23
        mc "I need your help!"
        mc "I’m pretty sure Dalia’s in one of these towers, but there’s still a chance she’s in the incubation rooms!"
        mc "I need you to go to the dungeons to check!"
        show gd 22
        sam "Fuck no, didn't you hear the Sultan's public announcement?"
        sam "The jackals have orders to kill us on the spot, dude!"
        show gd 23
        mc "Come on, don't be a pussy!"
        mc "You're supposed to be the Leader of a tribe of warriors!"
        show gd 24
        sam "Y-Yeah, now that you mention that..." with dis
        sam "Fuck that. I quit."
        sam "I... I officially name you Leader of the Ishari."
        sam "The seven tribes are yours. Good luck!"
        show gd 25
        mc "WHAT?!" with hpunch 
        mc "WHERE DO YOU THINK YOU'RE GOING?!" with hpunch 
        show gd 26
        sam "M-Man, I'm gonna be honest with you." with dis
        sam "I only joined the Ishari to get laid, and... hell, it worked!"
        sam "But then I started climbing the ranks somehow... one promotion here, one stroke of luck there... and in the end I ended up as their leader, I don't even know how."
        sam "I-I never wanted this!"
        sam "I'm not cut out to be a leader. I'm not even a good fighter!"
        show gd 27
        mc "You've gotta be kidding me..."
        mc "You're a bloody coward!" with hpunch 
        show gd 26
        sam "YEP!"
        sam "Coward but alive!"
        sam "I wish you the best of luck, man, I really do!"
        sam "But... I'm out of here!"
        sam "Tell my people I'm sorry!"
        play sound run
        show gd 28 with dis15
        mc "This has to be a joke..." with dis
        mc "Useless bastard!" with hpunch 
        scene gd 29
        mct "I need to find Dalia..." with dis
        mct "What if she’s being used in some twisted experiment by that mad scientist’s crew?"
        mct "Or... even worse, what if the Sultan's trying to..."
        mct "FUCK! I NEED TO FIND HER!" with hpunch 
    play sound2 speed
    scene black 
    show screen afewminuteslater
    with dis25
    pause
    show gd 43 
    hide screen afewminuteslater
    with dis25
    play sound7 panting fadein 2
    bla "You spend several minutes scouring the area, but you find no trace of her." with dis17
    mc "*Panting* (It's impossible...)"
    mc "*Panting* (Where is she?! I've searched every corner of this fortress!)"
    mc "*Panting* (Could I...)"
    mc "*Panting* (Could I have been mistaken?!)"
    if daliapath:
        play sound impact3b
        play sound2 impact3b
        scene gd 43c with flashfaster
        pause .35
        scene gd 43 
        mct "Was my gut feeling off??" with dis14
    mct "Is she really in the incubation rooms?!"
    scene gd 44
    mc "*Walking outside* (Fuck, fuck, fuck...)" with dis14
    mct "Or perhaps she..."
    if daliapath:
        play sound impact3b
        play sound2 impact3b
        scene gd 43b with flashfaster
        pause .35
        scene gd 44
        mct "No, no, no..." with dis14
        mct "NO!" with hpunch
        mct "D-DID I FAIL HER?!" with hpunch 
    else:
        mct "No, no, no... did she really..."
    mct "DID I..." 
    mc ". . ."
    play sound pop
    stop music2 
    scene gd 45 
    pause
    mc ". . ." with dis 
    mc "D-Dalia...?"
    if daliapath:
        play music2 cove volume 0.75 fadein 2
    else:
        play music arabia3 volume 0.75 fadein 3
    play soundlow clothes2
    play sound debris3
    show gd 46 
    d "THANK GOD." with hpunch
    if daliapath:
        play sound2 transformpower fadein 1 volume 0.7
        show gd 47
        mc "Hey, hey... what's wrong, Dal? Are you okay?" with dis17
        d "Y-You have no idea of how long I've been searching for you."
        mc "Don't worry, everything's okay now..."
        mc "*Chuckles* If only you knew how much running I've done through this palace just to find you too..."
        mc "*Relief sigh* I was worried sick about you."
        mc "This is the last time any of you enter Eternum without the neural implant. Got it?"
        mc "It was a terrible idea. There's no such a thing as a “safe” server."
        d "'Kay..."
        mc "I just..."
        mc "I don't even know what I'd have done if something had happened to you."
        mct "It's almost strange seeing Dalia like this. I haven't seen her this vulnerable since that day at The Cove."
        mct "She's always acting so tough... but in the end she can get scared just like anyone else."
        play sound clothes3
        show gd 48 with dis14
        play soundlow stomach
        d "Aaaaghh... I'm starving..." with dis12
        show gd 49
        mct "Or... p-perhaps she's just hungry?"
        mc "When's the last time you ate something?"
        show gd 48
        d "Um... I don't know... this morning?"
        d "I had a light breakfast before going to the gym, and then just a protein shake after that."
        show gd 49
        mc "Good grief, that's like three whole days without food for a normal human."
        mc "Let's get out of here! We'll deal with the Sultan another day."
        play sound whoosh3b volume 0.65
        show gd50
        d "T-The Sultan! YES!" with pu
    else:
        mc "Um..."
        mct "Wow, this was unexpected."
        mc "Are you okay...?"
        d "Yeah, I'm..."
        play sound whoosh3b volume 0.6
        play sound2 debris3
        show gd 53
        d "*Clears throat* I-I'm fine!" with pr 
        d "Totally fine!"
        show gd 54
        d "(What the hell, Dalia...)"
        show gd 53
        d "S-Sorry, I don't know why I reacted that way."
        d "I just..."
        d "You know, with the mission, I just..."
        show gd 50
        d "Y-YEAH! The mission!" with hpunch
    d "I need to tell you!"
    d "The Big Hunt event is ours! 100%% guaranteed!"
    d "I found out SOOO many things!"
    scene gd 51
    mc "Me too!"
    mc "Should we compare and contrast information?"
    show gd 50
    d "Yes! Did you hear about someone called Doctor Mercer?"
    show gd 51
    mc "Oh, I’d say I’ve done a bit more than just “hear” about her..."
    mc "Total psycho."
    show gd 50
    d "*Gasps* Tell me, tell me!"
    show gd 51
    mc "Okay, I didn't actually get to see Hassan himself, but–"
    show gd 50
    d "Oh, I DID see him!"with hpunch 
    show gd 51
    mc "Wait, really?!"
    show gd 50
    d "Yeah! Turns out he–"
    play sound microphonesound
    show gd 52
    ha "{sc=1}{i}*Via loudspeakers* ATTENTION!{/i}{/sc}" with dis2
    mc "Speak of the devil..."
    ha "{sc=1}{i}THE INTRUDERS HAVE BEEN SEEN NEAR THE PURITY FOUNTAIN!{/i}{/sc}" 
    ha "{sc=1}{i}ALL UNITS, HEAD TOWARDS THE GARDENS!{/i}{/sc}" 
    show gd 53
    d "Uhh... perhaps we should leave this place first." with dis12
    show gd 54
    mc "Y-Yeah, that's a smart idea."
    mc "I know of some kind of secret Ishari headquarters within the Citadel, we could lay low there for now."
    show gd 50
    d "Sounds good!"
    d "You lead the way?"
    show gd 51
    mc "Follow me!"
    stop music2 fadeout 10
    stop music fadeout 8
    scene black with dis3
    show screen sometimelater with dis25
    pause
    if not daliapath:
        jump arabialogoff
    play soundloop fireplace fadein 5
    $ renpy.music.set_volume(0.25, channel='music3')
    play music3 arabiarelax fadein 7
    scene gd 55 
    hide screen sometimelater
    with dis27
    pause
    play sound2 chew
    d "*Eating Arabian pastries* Mmmyeah, so, there's gotta be, like, at least... a thousand of those giant dog golems in total." with dis12
    d "Or even more, who knows!"
    mc "How many of those things do you think you could handle at once?"
    stop sound2
    play soundlow swallow
    d "*Swallows* Of those jackals? Damn, I'm not sure..."
    show gd 58
    d "But at least... three, for sure." with dis14
    d "They were fast, but... yeah, three sounds plausible."
    d "At least in today's conditions."
    show gd 60
    mc "Today's conditions?"
    show gd 58
    d "Yeah, like... I believe having our real bodies here might actually play in our favor, you know?"
    d "I think our survival instincts would kick in if things got really dangerous."
    d "Adrenaline just doesn’t hit the same when you know you’re not actually in real danger."
    show gd 59
    mc "Yeah, that's a fair point..."
    mc "I mean, it all feels the same as always, but... this time there's no safety net."
    show gd 60
    mc "Which is also... kinda scary, not gonna lie."
    show gd 58
    d "Maybe, but at the same time it also feels more... {i}real{/i}, don't you think? More... authentic."
    d "I mean, yeah, the sensations have always been just like the real world, you're right, but..."
    d "There was always that little voice in the back of your head saying, {i}“it doesn't matter, there are no consequences, no worries”."
    d "{i}“If you mess up, just roll back and try again”."
    show gd 59
    mc "Yeah... I know what you mean."
    mc "Even after everything we've been through – the souls of the dead trapped in Eternum, Calypso not being just a simple AI... hell, Eternum not being a video game but a whole different reality!"
    mc "Even after all that... this world still felt somehow unreal."
    show gd 58
    d "Exactly."
    d "But being here with our real bodies... damn, it sure hits differently."
    d "Not because of what we can feel, but because we know what we do actually has consequences."
    d "When everything you thought you knew about life crumbles like a cookie... maybe {i}this{/i} is what makes something... “real”."
    d "No second chances..."
    show gd 59
    mc "Only one path..."with dis06
    show gd 56
    d "*Giggles* But anyway, we're definitely getting into stoner-level philosophy here, so maybe we should get going." with dis08
    show gd 57
    mc "*Snorts* Yeah, I'm starting to think these little cakes might've had opium in them or something."
    show gd 58
    d "*Sighs* I guess we've waited long enough. We can only hope that Hassan didn't find Jerry and Samir and they managed to escape safely."with dis06
    d "But... well, worst case scenario, they're just here as astral projections."
    d "So... it should be fine."
    show gd 60
    mc "Oh, now that you mention Hassan, what exactly did he want from you?"
    mc "You told me how you escaped from that blind woman, but not why you were chosen."
    mc "I’m guessing he was after sexual slaves, but... why you specifically?"
    show gd 61
    d "O-Oh, well..." with dis08
    d "He only cared about... a certain kind of girls."
    show gd 62
    mc "What kind?"
    show gd 61
    d "Um... he liked... brown hair. And athletic women."
    show gd 62
    mc "Oh, really?"
    mc "Was that all?"
    show gd 61
    d "Uh... there might have been something else, but... I don't remember very well–b-but no biggie in any case! Why so many questions??"
    d "I told you everything!"
    show gd 62
    mc "Oh, I just–"
    show gd 61
    d "A-Anyway, look at the time! We should go now before it's too late!"
    d "Can we go now?"
    show gd 62
    mc "Uh... sure."
    mc "I just need a sec to focus, and I’ll take us back to that same alley in Kredon."
    mc "Whenever you want."
    play sound rubbody
    show gd 63
    d "Oh, but before we leave, tell me again how you defeated those monsters one last time!" with dis12
    d "I love hearing about the fruits of my teachings."
    show gd 65
    mc "Oh... *chuckles* alright." with dis
    mc "First off, that crazy doctor said the one assigned to be her bodyguard was her strongest creation, so that one's gotta be worth at least ten."
    mc "I was unarmed, but I managed to snatch the spear right out of its hands and drove it straight through its chest."
    mc "A single, rapier-like thrust—solid footing, right through its heart, just like you taught me."
    mc "That thing couldn’t even take more than two steps before it went down."
    show gd 66
    d "Ah, yes... my undefeatable knight in shining armor..."
    show gd 65
    mc "After that, I started running all over the citadel looking for you, killing a few more unsuspecting golems along the way."
    mc "I was crazy worried about you."
    show gd 66
    d "Ahhh... that could make such a great story."
    d "The warrior lady who trained a young, undisciplined soldier and turned him into a killing machine."
    d "Now that she's old, he protects his old master from danger using everything she taught him."
    show gd 65
    mc "*Chuckles* First of all, you killed two of those creatures yourself too, so it's not like you need that much protection."
    mc "And second, you're anything but old, girl."
    show gd 66
    d "What do you mean? I'm gonna be 19 in less than a month!"
    d "I'm a whoooole year older than you."
    show gd 65
    mc "*Laughs* That's not even how it works."
    d "*Giggles* Mm-mmh." 
    show gd 67
    d "*Sighs* Mmmh." with dis
    d ". . ."
    mc "Huh?"
    mc "You okay?"
    show gd 68
    d "Hmm?"
    show gd 66
    d "Ah, yeah, sorry, I was just... self-absorbed." with dis06
    d "Thinking about..."
    d "W-Well, about how much I love... s-spending time with you and everything."
    d "Thank you for... humoring me with my ramblings, [mc]."
    show gd 67
    mc "Oh, I see..." with dis08
    mct "My god, she can be so adorable when she wants to." 
    mc "I also love spending time with you, Dalia."
    mc "Hey, listen, we don't really have to leave yet if we don't wa–"
    show gd 69
    d "Do you like me, [mc]?"
    show gd 68
    mc "W-What...?"
    mct "Damn... that really came out of nowhere."
    mct "Looks like her insecurities are always right on her tail."
    menu:
        with dis
        "I like spending time with you [red][mt]{s}(Dalia's path){/s}":
            mc "I... like spending time with you, of course."with dis08
            d ". . ."
            d "Hmm."
            show gd 67
            d "Hmph..."
            mc "Are you okay, Dalia...?"
            mc "What got into you all of a sudden?"
            show gd 68
            d ". . ."
            show gd 69
            d "It's..."
            show gd 66
            d "S-Sorry, yeah, I-I don't know what... got into me, yeah." with dis06
            d "Classic, old... stupid... Dalia."
            d "Yeah..."
            show gd 63
            d "*Clears throat* Anyway!" with dis08
            d "Time to go back to Kredon!"
            show gd 65
            mc "Sure thing!" with dis08
            mc "Say goodbye to the feeling of being in Eternum with your real body."
            mc "We're not doing this EVER AGAIN."
            show gd 66
            d "*Chuckle* Fair enough."
            show gd 65
            mc "Grab my arm!"
            $ daliapath = False
            $ daliau = False
            jump arabialogoff
        "Of course I like you":
            mc "Of course I like you."with dis08
            show gd 69
            d "But... w-well, yeah, but I mean..."
            d "L-Like me... how...?"
            d "Like..."
            d "I mean, like me like... “ah, yeah, she's hot. I like her... butt”?"
            d "Or like me, like..."
        "I love you [dalia_pts]":
            mc "“Like” you...?"with dis08
            mc "I love you, silly."
            show gd 69
            d "Lo..."
            show gd 70
            d "W-Wait, what?" with dis12
            d "What do you mean, you l-love me...?"
            d "T-That's... such a big word, you know?"
            show gd 71
            mc "I know. I mean it."
            show gd 70
            d "But..."
            d "You mean... love me... like a good friend? Or like a sister?"
            show gd 71
            mc "Like a woman."
            $ dalia_points += 1
            play sound beat
            show screen heartbeat
            show gd 70
            d "W-WHAT?!" with dis 
            d "S-Since when?"
            show gd 71
            if harempath:
                mc "Huh, people keep asking me these kinds of questions lately."
            else: 
                mc "Huh, good question."
            mc "And... I only have one answer: A near-death experience like the one I had in Chinatown really helps you see things clearly."
            mc "I finally know what I want. What I've always wanted."
            mc "Crystal clear."
            show gd 69
            d "Oh... I see." with dis12
            d "So it's like... some sort of... post-traumatic experience?"
            show gd 68
            mc "A post-traumatic...?"
            d ". . ."
    stop music3
    play sound clotheswhoosh
    play sound3 debris3
    show gd73
    bla "You quickly jump towards Dalia." with hpunch   
    scene gd 72
    mc "Let me be extremely clear so you don't have to ask ever again."with dis08
    mc "I’d trade all my powers and all of my Gems of Doom in a heartbeat to keep you safe."
    mc "I would have wiped out the entire citadel and this whole godforsaken desert."
    mc "And I would have burned this entire planet to ash before letting that sickening sultan lay a finger on a single strand of your hair."
    show gd 74
    d "O-Oh."
    show gd 72
    mc "Yeah, you're smoking hot, but no, I didn't come looking for you because of your “butt”."
    mc "I LOVE everything you are."
    mc "I. LOVE. YOU."
    show gd 73
    d ". . ."
    show gd 74
    d "O-Okay."
    d "I-I believe you."
    show gd 73
    d ". . ."
    mc ". . ."
    show gd 72
    mc "Aaaand... I was overdramatic again. S-Sorry about that."
    show gd 75
    d "*Snorts* Mm-hm."with dis08
    $ dalia_points += 1
    play sound clothes3
    show gd 76 with dis15
    play sound2 beat
    show screen heartbeat
    pause
    d "Mmmmmh..." with dis
    play sound3 clothes3
    show gd 77
    d "*Giggles* It's okay. I like it when you get all “romantico”." with dis14
    d "And..."
    d "*Giggle* I-I think I love you too."
    d "I don't know how, or why, but... it happened."
    play sound rubbody
    play soundlow chair2
    show gd 78
    d "*Standing up* But anyway! *Giggles* Good talk." with dis
    mc "*Chuckles* Good talk..."
    d "Time to move!"
    mc "As you wish, m'lady!"
    scene gd 79 with dis22
    bla "You pick up the scattered things from the floor and turn your attention back to Dalia, who is waiting for you by the door." with dis15
    mc "Alright, my {i}love{/i}... all set!"
    d "Mm-hm..."
    mc "You know we don't really have to go outside, right?"
label ga_dalia4:
    if _in_replay:
        play soundloop fireplace
        scene gd 79
        mc "You know we don't really have to go outside, right?" with dis12
    mc "I can take us back to Kredon from here, we don't need to go back to the Exit Portal."
    $ renpy.music.set_volume(0.33, channel='music3')
    play music3 daliasexsong fadein 7
    play sound lock
    show gd 81
    d "*Locking the door* I know."
    stop soundloop fadeout 33
    show gd 80
    mc "Huh...?"
    show gd 81
    d "I just thought..."
    d "Got any plans for tonight? 'Cause I really don't."
    d "So maybe we could... stick around a little longer. Although... well, it's just an idea."
    d "What do you think?"
    show gd 80
    mc "I have no plans, no..."
    mc "Got anything in mind...?"
    show gd 81
    d "Well... I guess I did promise you one last surprise reward for your push-ups challenge, didn't I?"
    d "We could... get that off our back."
    show gd 80
    mc "Ah, you did, indeed..."
    mct "I like where this is going..."
    show gd 81
    d "Wanna see it now?"
    d "I'm kinda in the mood for... surprises."
    show gd 80
    mc "That sounds pretty good, yes..."
    play sound chairmove
    show gd 83 with dis2
    bla "Dalia drags a table closer, leaning against it with a sexual, deliberate allure." with dis17
    mc "Does this mean what I think it means...?"
    show gd 82
    d "I know what you want, pig. No need to pretend."
    d "And you're in luck."
    d "I guess those Arabian pastries didn't... {i}satiate{/i} me enough."
    show gd 83
    mc "Oh boy... y-you sure?"
    show gd 82
    d "Yeah, I'm sure."
    d "Why so much hesitation? I thought you loved to pull out little [mc] at the slightest opportunity."
    show gd 83
    mc "Well... you never can be too careful these days."
    play sound2 footsteps
    play sound3 clothes3 
    show gd 84 with dis17
    bla "You walk towards Dalia, as she immediately grabs your pants, locking her gaze with yours." with dis14
    mc "Gotta make sure you're totally on board too."
    d "*Giggles* Ah, of course..."
    play sound clothes4
    show gd 85 with dis17
    mc "But oh, well..." with dis12
    mc "That looks pretty consensual to me..."
    show gd 86
    bla "Dalia softly brushes the tip of your dick on her lips, her warm breath sending shivers down your spine." with dis17
    mc "Oh god, this teasing is making me so hard..."
    d "*Giggles* Mm-hm..."
    play sound2 ["<silence 0.1>", kiss] volume 0.6
    show gd 87
    bla "She gently kisses you on the tip of your cock." with dis
    show gd 86
    d "Hmm." with dis
    show gd 88
    d "Alright, done!" with dis12
    show gd 89
    mc "Eh?"
    mc "Wait... w-what?!"
    show gd 88
    d "That was your surprise!"
    show gd 89
    mc "A single kiss?!"
    show gd 88
    d "*Giggles* Isn't it romantic?"
    d "We can go now."
    show gd 89
    mc "Oh, you naughty girl..."
    play sound clothes3
    show daliacit1 with dis2
    mc "You're not planning to walk away and leave me like this now, are you?" with dis15
    mc "You surely wouldn't be this evil."
    d "I never agreed to anything more... did I?"
    mc "I know you want to do it, Dal..."
    mc "I can see it in your eyes..."
    d "Do what? Sucking your... huge, veiny, and smelly cock?"
    d "Hell nah... my jaw always hurts afterwards."
    mc "I know you love it, Dalia, you can't fool me..."
    d "Me? You've been watching too much porn, [mc]."
    d "Most girls don't really like giving head, did you know that...?"
    mc "You're not like most girls..."
    d "Am I not...?"
    mc "Open your mouth..."
    d "Nah-nah..."
    mc "Do I have to beg...?"
    play sound ["<silence 0.5>", wood2] volume 0.6
    play sound2 chairmove
    scene gd 90 with dis2
    bla "Dalia teasingly removes her boots, turning around and stepping onto the table." with dis15
    d "How is a cute little kiss not enough? You're getting so greedy, [mc]..."
    mc "*Chuckles* Now you're just taunting me..."
    d "Taunting?! What else do you even want from me? To show you my pussy?! Are you gonna ask me to expose my boobs now?"
    mc "Well, that doesn't sound bad at all, actually..."
    d "*Giggles* Such a perv..."
    d "Fine, fine..."
    play sound clothes3 
    play sound2 wood2 volume 0.4
    show gd 91 with dis2
    mc "Oh, yeah, I missed that pair..." with dis12
    play sound3 footsteps
    play sound4 clothes3
    show gd 92
    bla "You walk around the table as she finishes slipping her top off, her head falling back towards you." with dis17
    mc "Can you see how hard you got me without even touching me?"
    scene gd 93
    d "*Giggles* Whoa... it looks even bigger from this angle." 
    scene gd 92
    mc "And it's all for you, Dal..."
    mc "You just have to open your little mouth..."
    d "Mmmmh..."
    scene gd 93
    d "Like this? Is this open enough...?"with dis 
    mc "No, not enough, I'm afraid..."
    mc "You'll have to try harder..."
    d "*Giggles* It's not my fault that you have a–"
    play sound clothes3oily
    scene gd 94
    d "Hu-hhhgggghh..." with dis14
    bla "You interrupt her, sliding your cock between her parted lips."
    mc "Oh, Dalia..."
    d "M-Mmmhh..."
    mc "You’ve got me so turned on, it’s driving me insane..."
    mc "I {i}need{/i} to see my dick disappearing into your throat..."
    d "*Moans* Mmmmhhmm..."
    play sound2 clothes3oily
    show gd 93
    d "*Moans* Aaahh..." with dis15
    mc "But, oh well..."
    mc "If you don't want to do it, I'll just be on my way."
    d "*Whispers* Fuck no..."
    mc "Huh? What was that...?"
    d "*Giggles* Hah..."
    d "I want... all of you..."
    mc "Fuck yes, babe..."
    mc "Open for me..."
    show gd 95
    d "Aah..." with dis15
    d "Beeetter...?"
    mc "Oh yes, that's much better..."
    play sound blow4
    play sound2 blow5
    play sound5 clothes3oily 
    show gd 97b
    bla "You thrust into Dalia’s mouth with a rough urgency, her lips parting wide to accommodate you." with dis14 
    play sound3 blow5
    d "H-Hhhhgg!!!" with hpunchsubtle
    d "Mmmmhh..."
    $ renpy.music.set_volume(0.15, delay=10.0, channel='music3')
    play soundloop blowjob2 fadein 2
    scene daliacit2 with dis2
    dbt "*Moans* MMMMmmMMMhhh..." with dis12
    mc "Ohhhh... dear Lord, yes..."
    mc "I missed your god-like skills so much...."
    d "*Moans* Mmmmm..."
    mc "You're enjoying this, aren't you...?"
    d "*Giggles* Mmmmhm-mhhh..."
    mc "I knew it..."
    mct "Fuck yes... there's nothing like getting an eager mouth sucking your cock like that..."
    mct "It's not just the feeling, it's knowing she's enjoying this as much as I am..."
    d "Mmmmmmhmmmm..."
    mct "And dear Lord, she's good at it..."
    mct "The way she swirls her tongue around the tip of my cock..."
    mct "She knows EXACTLY what she's doing..."
    pause
    scene daliacit3 with dis2
    bla "Dalia continues eagerly working her mouth on you, her free hand slipping between her thighs to pleasure herself in rhythm." with dis12
    mc "AAaa-agh... cheeky girl..."
    d "*Moans* Mmmmmhhh..."
    mct "I don't think there's anyone with a more natural talent for this."
    mct "I swear, it feels like she's creating a vacuum with her lips."
    mc "Aaaghh..."
    mct "It's... completely insane..."
    d "Mmmmmmhhh..."
    mct "The little sounds she makes... like she’s savoring every inch of me..."
    d "HHhmmmm!" with hpunch
    bla "Dalia lets out a high-pitched whine as your hands firmly squeeze her breasts, her petite waist arching instinctively."
    mc "O-Oohhh baby, yeah..."
    mc "I fucking love your body..."
    dbt "Mm-hmmMm...."
    pause
    stop soundloop fadeout 1
    play sound blow4
    play sound2 clothes3oily
    scene gd 95
    d "*Gasping for air* AAAaagghHhh... aaAaaghh... aaaahh..." with dis12
    mc "Aghh... you're the best, Dalia..."
    d "*Giggles* Haha... th-thank you..."
    mc "Do you think you’re ready for me to test that reflex of yours again? Or, well... the lack of it, more like."
    d "*Giggles* Hah..."
    d "I-I can take... e-every f-fucking inch of you..."
    play sound3 clothes3
    scene gd 95b
    mc "*Dropping your pants* That's my girl..." with dis15
    play sound blow4
    play sound2 clothes3oily
    scene gd 97
    d "Mmmhm..." with dis12
    play soundlow penetration3
    show gd 96
    mc "Here we go..." with dis12
    play sound blow4
    play sound2 blow5
    play sound5 bodycollide2  
    play sound7 penetration3
    show gd 98
    dsc "HHHGgGhHHhhhh!!!" with hpunch
    play sound blow4
    play sound2 blow5
    dsc "HgggwwWwh!" with hpunch
    play soundloop blowjob4slow fadein 2
    scene daliacit4 with dis2
    dbt "Hhhgghhh... hhhhggggh... hggggh..." with dis12
    mc "OH M-MY GOD..."
    bla "After just a few seconds of adjustment, Dalia's throat accommodates to the intrusion, surrendering to you fully and allowing you to sink as deep as you want." with dis
    dbt "Ggg-ggghh-ggghh..."
    mc "F-FUUUUUCK..."
    mct "J-Jesus Christ..."
    mct "I can't believe how deep I'm going."
    mct "I can literally feel my balls hitting her face."
    mct "She keeps doing those noises of hers... but without a single spasm or hint of gagging."
    mct "How on earth can she even breathe?"
    dbt "GGhhhmmmmmmhmhmhhh..."
    mc "*Moans* AAAagh..."
    mct "What a natural gift..."
    mct "She truly is a goddess at this..."
    dbt "*Moans* Mmmm-gggh-mmhhh..."
    mc "Oh, D-Dalia..."
    mc "S-So good..."
    dbt "*Moans* Mm-mm-mmhhhh..."
    mc "T-That's it, gobble it all..."
    dbt "*Moans* Mmmhhhh..."
    $ renpy.music.set_volume(1.0, channel='soundloop2')
    play soundloop2 deepthroat fadein 2
    scene daliacit5 with dis2
    bla "Without really stopping to think about it, you suddenly find yourself thrusting into Dalia's mouth as if you were pounding a pussy." with dis12
    bla "Far from pulling away, she quickly adapts to your pace with ease, her every movement an invitation to go faster."
    mc "OH M-MY FUCKING GOD..."
    mc "THIS CAN'T BE REAL..."
    dbt "GGH-HGGG-HHHGGG---HGGPHH..." with hpunch
    mc "O-Oh Lord, this is heaven..."
    dbt "*Moans* Mmmm-hmm-mhhhgh..." with hpunch
    mc "*Looking at Dalia's neck* (I can literally see my cock stretching her throat with every thrust.)"
    mct "This is..."
    mct "Oh no..."
    mc "*Panting* A-Aaagh, fuck, I'm gonna cum..." with hpunch 
    mc "*Panting* I'm losing control..."
    mc "*Panting* Ohhh s-sweet heavens, I don't wanna c-cum yet..."
    mc "*Panting* It's too soon..."
    dbt "*Moans* Mmmm-hmm-mhhhgh..." with hpunch 
    mcsc "*Panting* B-BUT HOW AM I SUPPOSED TO..."
    mcsc "*Panting* A-A-AAAGGHH..."
    mcsc "*Panting* I CAN'T..."
    mcsc "*Panting* STOP..."
    dbt "*Moans* Mmmm-hmm-mhhhgh..." with hpunch 
    mcsc "*Panting* O-OOH D-D-DALIA, HANG IN RIGHT THERE..." with hpunch 
    mcsc "*Panting* I'M ALMOST..." with hpunch 
    mcsc "*Panting* F-FUUUUCKkkk..." with hpunch 
    stop soundloop2
    stop soundloop
    scene gd 98
    play sound3 slap1
    play sound cumall
    play sound2 blow5
    play sound4 woodhit volume 0.7
    mcsc "AAAAAAARRRRgggGGHhhh....!!!!" with hpunchlong3
    play sound3 bodycollide
    play sound cumall
    mcsc "AAAaaahhggh..." with hpunchlong3
    play sound2 swallow
    dbt "*Swallows* MMmmmhh..." with dis14
    play sound4 penetration3
    show gd 99
    mc "H-Holy crap..." with dis17
    play soundloop fireplace fadein 7
    $ renpy.music.set_volume(0.25, delay=10.0, channel='music3')
    play sound ["<silence 0.5>", wood2] volume 0.6
    play sound2 chairmove
    scene gd 100
    bla "As you take a step back, Dalia slowly steps off the table." with dis22
    d "*Clears throat* J-Jesus... that was... r-rough."
    mc "S-Sorry, did I go too far?"
    d "N-No, it's okay, don't worry."
    play sound clothes3
    show gd 100b
    d "*Tying her bottom part again* You're lucky I'm a tough girl." with dis14
    show gd 101
    mc "Goddamn gracious, you're a fucking goddess..."
    show gd 100b
    d "I don’t think I’ve ever seen you finish that fast before."
    d "*Giggles* At least, not when I’ve been around."
    d "I guess I win this round!"
    show gd 101
    mc "Hey, that's not fair... I wasn't even doing anything to make you cum this time."
    mc "*Smirks* Although... well, that can be fixed."
    mc "I've gotta say..."
    mc "It’d be terribly cruel of me to let you leave all worked up like this."
    show gd 100b
    d "You're a horny dog, [mc]. Don't you ever run out of fuel?"
    show gd 101
    mc "Just looking at you gets me all fired up, can't help it."
    mc "I just need more of you..."
    show gd 100b
    d "*Giggles* What do you wanna do, Casanova?"
    d "We're not gonna fuck, sorry to disappoint you."
    show gd 101
    mc "Well, I wouldn't say no to another sixty-nine."
    mc "Or if you're in the mood for a little grinding again..."
    show gd 102
    d "*Looking at your cock* Hmmm." with dis08
    show gd 100b
    d "You're getting soft down there, big boy." with dis08
    show gd 101
    mc "Trust me, the moment I see you on top of me, I’ll be back in action faster than you can even think about kneeling."
    show gd 100b
    d "You're underestimating the amount of “energy” you just unloaded a minute ago, [mc]."
    show gd 101
    mc "Wanna bet?"
    show gd 102
    d "*Snorts* Hmph." with dis08
    show gd 103
    d ". . ." with dis08
    show gd 100b
    d "Okay... fine." with dis08
    d "I guess we can spend... another minute in here."
    show gd 101
    mct "FUCK YES..."
    mc "Ah, I knew you were too horny to refuse..."
    play soundlow rubbody
    show gd 103b
    d "*Giggles* Shut up and prove to me you're more than just a big mouth." with dis14
    d "On the ground."
    stop soundloop fadeout 20
    play sound clothes3
    play sound2 ["<silence 1>", fall2]
    show gd 104
    bla "You quickly lie onto a nearby carpet." with dis17
    mc "Yes, my mistress..."
    d "*Giggles* Shut up."
    play soundlow rubbody
    play sound3 wood2 volume 0.2
    show gd 105
    bla "Dalia sits on your legs and slowly starts to remove her panties." with dis14
    mc "Oh my god..."
    d "Okay..."
    play sound4 clothes3
    show gd 106
    d "Just rubbing... yes?" with dis15
    mc "Oh Jesus, just look at how perfect your pussy is..."
    play soundlow oily
    show gd 107
    bla "As you expected, just the sight of Dalia baring herself before you and the thoughts of what you'd do to her make you hard again in an instant." with dis17
    d "O-Ooooofff..."
    scene daliacit6 with dis2
    d "*Moans* Ooohhh..." with dis12
    mc "O-Oh, babe..."
    d "Fuck, this f-feels good..."
    mc "Oh Dalia..."
    mc "How long are we gonna continue delaying this...?"
    d "D-Delaying... what?"
    mc "You know what..."
    d "*Giggles* Hah..."
    d "I... I want to do it, but..."
    mc "But?"
    d "I'm... scared. W-What if... it hurts?"
    d "What if I'm not... w-what you expected?"
    mc "If it hurts, we stop."
    mc "And you're everything I could ever expect and more. You're perfect."
    d "Aaaahh... a-always the romantic, aren't you...?"
    d "*Moans* Mmmhh..."
    d "Does it... does it feel better than this?"
    mc "Much better..."
    d "*Moans* R-Really...?"
    d "*Moans* Mmmmhh..."
    pause
    d ". . ." with dis 
    d "*Whispers* Do you want to {i}fuck{/i} me, [mc]...?"
    mc "My god, Dalia, I do..."
    d "*Giggles* Hah..."
    play sound clothes3oily
    play soundlow tear1 volume 0.5
    show gd 108
    bla "Dalia tears off her loincloth and suddenly stops moving, her juices spilling all over you as she presses her swollen lips against your throbbing cock." with dis14
    mc "Oh m-my god..."
    d ". . ."
    d "[mc]..."
    show gd 109
    d "I..." with dis12
    d "I can't bear it anymore."
    d "Fuck, it's almost p-painful."
    d "It's like... my body {i}screams{/i} for more."
    show gd 108
    mc "Oh god, Dalia..." with dis12
    mc "Is today really the day?"
    d "I..."
    d "Sh-Should we really do it?" 
    mc "This is your decision. You already know what I want."
    d ". . ."
    play sound3 clothes3b
    show gd 109b
    bla "Dalia hesitates for a moment before nervously pulling off her shirt and tossing it aside." with dis17
    mc "Oh man, I can hear my heart pounding..."
    d ". . ." 
    d "I need you..." 
    mc "Ohh yes, say it..."
    d "Inside..."
    mc "Yes..."
    d "Of me..."
    mc "OH, BABE, YES..."
    play sound clothes3oily
    scene gd 110
    d "*Slowly getting into position* S-So..." with dis15
    d "L-Let's take it slow, okay?"
    mc "You're in charge here..."
    d "*Deep exhale* Fuuuuuu..."
    d "J-Just... a little... bit..."
    d "Just... for a second..."
    d "Just... to see..."
    d "How... it feels..."
    play sound2 oily
    scene gd 111
    d "MMmmMMmmmmmhhhh..." with dis2
    mc "O-Oh my word..."
    play sound3 oily
    scene gd 112
    d "Aaaaaaghhh..." with dis2
    play sound4 fall2
    scene gd 112b
    d "*Leaning forward* Fuuuuck..." with dis
    d "Oh my god, i-it's... it's really i-inside..."
    mc "A-All good...?"
    d "Y-Yee-ahh..."
    d "I-It feels..."
    d ". . ."
    scene gd 113
    dbt "{size=50}Amazing..." with dis12
    $ renpy.music.set_volume(0.15, delay=10.0, channel='music3')
    scene daliacit7 with dis2
    d "*Moans* AAaahhh... aaahahhhhh... aaAAAaaAhHHh..." with dis12
    dbt "W-WOOOWWWWww..." with hpunch
    dbt "H-HOLY... SHIT..." with hpunch
    mc "S-Sweet Jesus, that's TIGHT..."
    d "O-Oh my god, you're {b}massive{/b}..."
    d "You feel... so HUGE..."
    mct "I can't believe it's finally happening..."
    mct "I'M HAVING SEX WITH DALIA..."
    d "*Moans* AaaaaaaaaAaahh..."
    mc "O-Oh Dalia, I've been waiting for this forever..."
    if daliacabin:
        mc "I’ve dreamed of this moment since the day we left that cabin in Frontier Trails..."
    d "Haha... r-really...?"
    d "*Moans* AAAAaghh..." with hpunch 
    d "And tell me..."
    d "W-Was it worth it?"
    mc "W-Worth every damn second..."
    mc "W-Was it for you...?"
    dbt "*Moans* AAAAAghh..." with hpunch
    mc "I'll take that as an answer..."
    dbt "*Moans* AAaahhhhh... aaahh..."
    mc "That's it..."
    mc "Keep going..."
    mc "Keep bouncing that perfect, gym-toned butt of yours on my cock..."
    d "Agghhh... oh [mc]..."
    d "I can feel it... s-stretching me so much..."
    d "F-Fuck, my fingers are NOTHING compared to this..."
    d "*Moans* It is... a thousand t-times better..."
    mc "You have no idea how good your pussy is making me feel right now, Dalia..."
    mc "Somehow it's even better than in my fantasies..."
    d "*Moans* AAAAAhhh... [mc]..."
    play sound clothes3
    scene daliaanglerideswitch1
    show screen daliaangleride1
    with dis2
    bla "Dalia continues riding you with fervor, her moans growing louder with every thrust." with dis12
    dbt "*Panting* AAAhhh... aahhh... ahhhhh..." 
    dsc "*Screams* AAAAaGHHHH..." with hpunch 
    mc "OH MY GOD..."
    d "G-God..."
    d "[mc], you're t-too big..."
    d "I can't..."
    d "I c-can't even take all of it..."
    mc "Oh sweet Lord, Dal, just keep doing what you're doing..."
    d "*Moans* AAAAggHGhh..."
    d "*Moans* This feels... like... heaven..."
    mc "H-How can you be this tight?!"
    mc "Is it because of the exercises you do at the gym, or j-just genetics...?"
    d "F-Fuck, I don't know..."
    d "But... I do... p-pelvic floor exercises... regularly..."
    mc "Oh god, PLEASE keep doing them..."
    d "*Giggles* Hah... I don't know if–"
    d "*Moans* AAAahh..."
    d "*Moans* AAAAAAHHHH..." with hpunch 
    d "[mc], I'm gonna cum..."
    mc "A-Already?"
    dsc "AAAAAhhh..." with hpunch 
    dsc "Fuck, it's just... hitting on the right spot..."
    dsc "[mc], I'm cumming..."
    dsc "Stop me..."
    mc "Stop you? Please, just let yourself go..."
    mc "You d-don't have to hold back, Dalia."
    mc "Not today..."
    dsc "Aaah..."
    dsc "AAaaAAAhhh..."
    dsc "AAAAAAAAAAAAAAGRGHHHHH..."
    play sound slap1
    play sound2 squirt
    hide screen daliaangleride1
    scene gd114
    dsc "*Orgasming* AAAAAAAAaaaarghhh!!!" with vpunchslow
    play sound7 squirt volume 0.5
    dsc "F-FUCK!" with hpunch
    play soundlow clothes3oily
    scene gd 116 
    d "*Gasping for air* F-Fuuuuuck...." with dis14
    mc "Oh boy, that was hot..."
    d "*Gasping* That was... the strongest o-orgasm of my whole life..."
    mc "I'm glad..."
    d "*Gasping* H-How is it possible?"
    mc "Well, they do say vaginal orgasms are different from only-clitoral ones."
    mc "Every girl's different."
    d "*Gasping* It felt like an electric domino chain under my skin..."
    d "*Gasping* Spreading everywhere..."
    mc "Don't worry, we can take a minute to re–"
    play sound clothes3oily
    show daliacit10 with dis2
    bla "Before you can even finish your sentence, Dalia moves with renewed intensity, her desire overwhelming any pause." with dis12
    mc "W-W-WHAT?!"
    dbt "AAaahh... aahhh... aahhh..." 
    d "*Giggles* Hahah..." with hpunch 
    mc "Oh god, this can't be real..."
    d "*Panting* I wanna..."
    d "*Panting* I-I want you to make me cum again, [mc]..."
    mc "Oh L-Lord..."
    mc "You're a nympho..."
    mc "Are you really the same girl who was s-so hesitant just a minute ago...?"
    d "*Giggles* N-No one told me it would feel this... g-gooddd..."
    d "And..."
    d "W-Well..."
    d "I-I just wanted... my first time to be with... the r-right one..."
    dbt "*Moans* AAAAaahh..." with hpunch
    mc "O-Oh, well..."
    mc "A-Are you... happy with your choice?"
    d "*Giggles* Haha..."
    d "*Moans* Yes..."
    d "*Moans* I want you..."
    d "*Moans* I-I want you to be the only one t-to ever have me, [mc]..."
    d "*Moans* F-For the rest of my life..."
    mc "Oh, baby..."
    d "I'm..."
    dsc "AAAAhhh..." with hpunch 
    dsc "I'm yours..." with hpunch 
    mc "You're mine..."
    dsc "*Moans* I've nev–"
    dsc "*Moans* Sh-Shit, I'm c-cumming again..."with hpunch 
    mc "A-Again?!"
    dsc "I can't he–" with hpunch 
    dsc "Mmmmmgggh!" with hpunch 
    dsc "MmmmMMMmgGGggh!" with hpunch 
    play sound slap1
    play sound2 squirt
    scene gd 115 
    dsc "*Orgasming* AAAAaaaaAAAAaGGGhhh!!!" with vpunchlong
    play sound7 squirt
    dsc "AAAaaaaRghh..." with hpunch
    play sound bodycollide2
    play sound2 fall3
    play soundlow debris3
    scene gd 116b with vpunchslow
    dbt "*Breathing heavily* Aaaahhaahh... *giggles* w-whooaaaaaa..." with dis17
    mc "O-Oh god..."
    mc "Your vaginal contractions every time you orgasm will end up turning me into a eunuch at this rate..."
    d "*Giggles* Sorry, I c-can't help it..."
    play sound clothes3oily
    show gd 117 with dis15
    mc "Oh Lord, have mercy..." with dis
    scene daliacit11 with dis2
    dbt "*Panting* AAAGGgghhh... aaahhh... aaaAAhhHh..." with dis12
    dbt "*Panting* Oh, [mc]..." 
    mcsc "OHHHHhhhh GODDD..." with hpunch 
    dbt "*Moans* AAaahh... aaaaaAAahh..."
    mct "H-How the hell is she cumming so many times so fast... without even needing a single second of rest?"
    mct "Is she... is she multi-orgasmic?!"
    d "*Moans* Oh, my g-god..."
    d "*Moans* I-It's sooooo deep....." 
    mc "Holy fuck, it really is..."
    mc "Y-You're taking every inch..."
    d "*Panting* You're hitting..."
    d "*Panting* The d-deepest parts of me..."
    dbt "*Moans* AAAaaahhh..." with hpunch
    mc "F-Fuck yes..."
    d "*Panting* Th-think you can handle me going faster?"
    mc "I-I think the real q-question is, can you...?"
    d "*Giggles* H-Hah-ah..."
    d "Let's see..."
    play sound clothes3oily
    scene daliaanglerideswitch2
    show screen daliaangleride2
    with dis12
    dsc "A-AAaaghh... a-aghhh... a-a-ahhh..." with dis
    dsc "*Panting* OH MY GOD..." with hpunch 
    dsc "*Panting* T-This position hits... s-s-so good..."
    mc "*Panting* A-AAaaahh... j-jeez..."
    mct "God's holy balls, every time she slams her ass against me, it feels like getting hit by a goddamn cannon..."
    mct "She's a beast..."
    mc "O-Ohh, fuck, Dalia..."
    mc "P-Please don't stop..."
    d "Hah-a... this w-would be a very good workout, don't you think...?"
    mc "N-Never been more thankful for your gym obsession than I am right now..."
    d "*Giggles breathlessly* Hah-aaaaaahhhh..."
    d "*Moans* Yeah..."
    d "*Moans* Air squats n-never felt better..."
    mc "*Panting* W-Who’d have thought when I came back to Kredon..."
    mc "*Panting* That the childhood friend I used to p-play with would end up ramming her p-perfect, huge ass down on my cock..."
    d "*Giggling breathlessly* A-And who’d have thought..."
    d "*Giggling breathlessly* That the idiot who m-moved back in with us w-would..."
    dsc "W-Wou–aaaAAAaaahhh...." with hpunch 
    dsc "Oh fuck, I'm cumming again, [mc]..." with hpunch 
    mc "F-Fuck yeah..."
    dsc "AAAahh..." with hpunch 
    dsc "AAAaAAaaahhhhh..." with hpunch 
    dsc "AAAAAAAAAAAAAAGGHHHhhhhh...." with hpunch 
    play sound slap1
    play sound2 squirt
    play soundlow whoosh6
    play sound3 debris3 volume 0.5
    hide screen daliaangleride2
    scene gd114b
    d "{sc=3}*Orgasming* AAAAAAAAaaaarghhh!!!!!!{/sc}" with vpunchslow
    play sound squirt
    bla "As Dalia climaxes once more, her legs finally give out and she crumples against you, her body trembling uncontrollably." with hpunch
    dsc "G-GODDDDDDD...."
    play sound2 clothes3oily
    scene gd 116
    d "*Desperately gasping for air* O-Okay..." with dis15
    d "*Desperately gasping for air* G-Give me a..."
    mc "Fuck, we can't stop now, Dal..."
    d "E-Eh...?"
    play sound2 whoosh6
    play soundlow debris3 volume 0.7
    scene daliacit14t
    bla "Noticing Dalia's exhaustion, you take the lead and grip her waist firmly, pushing into her as deep as her body allows." with hpunch
    dsc "*Panting* O-Oh my gwaadd..."
    mc "O-Oh fuck YES..."
    dsc "*Panting* AAAahh...mmmmhh...aaaAAAahh..."
    mct "How the hell can she feel this good..."
    mct "The way her plump, soft lips stretch for me... and how unbelievably tight she is..."
    dsc "*Moans* AAAaaAaaaagghh..." with hpunch 
    mc "I-Is this how you thought the day would end, Dal...?"
    mc "I noticed you shaved. You don't have a single hair on you..."
    dbt "*Giggling breathlessly* T-That's just..."
    dbt "*Giggling breathlessly* For... hygiene..."
    mc "Ahhh... of course..."
    dbt "*Panting* Oh sweet L-Lord, [mc]..."
    mc "Faster, you say...?"
    scene daliacit15 with dis15
    dsc "*Shriek* [mc!u]....!!!!" with dis12
    mct "God, I love it when she screams my name..."
    mct "Now I'm actually glad I came earlier during the blowjob..."
    mct "There's no way I could've managed to last this long otherwise."
    dsc "AAAahhHhH...aAaaahhhh...aaaaaHhhhmmmhh...aaaaAahh..."
    mct "Although... I feel like I'm reaching my limit..."
    dsc "[mc], you're..."
    dsc "G-God, you're gonna b-break me..."
    mc "I-Is that a dare or a plea...?"
    dsc "*Breathless giggle* H-Hah..."
    dsc "It's... nei–"
    dsc "*Panting* F-Fuck, I-I'm gonna cum againnnn...!!"with hpunch
    dsc "*Panting* W-W-What is wrong with meee...?!" 
    mc "F-Fuck yes, babe..."
    mc "Nothing is wrong with you at all..."
    dsc "*Moans* A-Aaaghh..."
    mc "Cum for me..."
    mc "Don't hold back..."
    dsc "Oh, f-fuck..."
    dsc "Mmmmmh..." 
    dsc "Mmmmhmhmmmm..." with hpunchsubtle
    dsc "MMmMMMMmmmMMMMMMhhHHHHhh!!!" with hpunch 
    play sound slap1
    play sound3 slap1
    play sound2 squirt
    scene gd 118 
    d "{sc=3}AAAAaaaaAAaagGGgHHhhHHhhhh...{/sc}" with hpunchlong
    play sound2 clothes3oily
    scene gd 116b
    d "*Desperately gasping for air* J-Jeeeeez..." with dis15
    mc "*Panting* G-God..."
    mc "*Panting* Can you... c-can you continue?"
    d "*Gasping* C-Continue...?"
    d "*Breathless giggle* I-I swear..."
    d "*Breathless giggle* I think I might actually p-pass out if I cum again, but..."
    dbt "{b}{size=50}FUCK IT..." with dis12
    mct "Oh, balls, this woman..."
    play sound6 debris3
    scene daliacit16 with dis2
    mcsc "*Putting her on all fours* Good God almighty..." with dis2
    dsc "AAAahhHhH...aAaaahhhh...aaaaaHhhhmmmhh...aaaaAahh..."
    mcsc "Y-Yeah... that's my tough girl..."
    mc "{sc=2}(S-Sweet heavens...){/sc}"
    dsc "*Moans* AAAAAaaaAHHHhh..."
    mc "{sc=2}(Man, the way she keeps cumming so fast, so easily...){/sc}"
    mc "{sc=2}(This shit is... straight-up ADDICTIVE...){/sc}"
    dsc "*Moans* AAaaahhh.... aaaahhhHh..."
    mc "{sc=2}(I want to cum inside of her so bad...){/sc}"
    dsc "*Moans* Yes...YES... f-fu..."
    mcsc "Y-Yeah, say it..."
    dsc "*Breathless giggle* Hah..."
    dsc "F-F-FUCK ME, [mc]..."with hpunch 
    dsc "Harder!!!" with hpunch 
    mcsc "*Panting* Oh, babe..."
    mcsc "*Panting* Y-Your pussy's pure fucking magic, Dalia..."
    mcsc "*Panting* H-How many times have you come already?"
    mcsc "*Panting* L-Like... five? S-Six?"
    dsc "*Breathless giggle* I-I... don't know..."
    mcsc "*Panting* And you’re still just as wet as when we started..."
    mcsc "*Panting* It's almost... u-unnatural..."
    dsc "*Moans* AAAaaahhHhH...mmhhh[mc][namelong]..."
    play sound clothes3oily
    scene daliacit17 with dis15
    dsc "*Panting* O-Oh shit..." with dis12
    dsc "*Panting* It's c-coming again..."
    dsc "*Panting* I-I can feel it..."
    mcsc "T-This is it... I-I'm almost there too..."
    mcsc "I'm at my fucking limit..."
    dsc "*Panting* Y-Yeah!"
    dsc "*Panting* D-Do it... let's do it together..."
    mcsc "A-Are you saying I can–"
    dsc "{b}{size=55}D-DO... IT." with hpunch
    play sound fallfull
    scene daliacit18 with hpunch
    d "{sc=3}AawhgHhH...aAawahhh...aaHhgmhh...aaAahh...aAAAhh...{w=30.9}{nw}{/sc}" with dis3 
    play sound clothes3oily
    scene daliacit19 with dis2
    play sound2 fallfull
    play sound3 debris3
    stop music3 fadeout 20
    $ renpy.music.set_volume(0.6, channel='soundloop3')
    play soundloop3 fireplace fadein 15
    "{w=0.52}{nw}" with vpunchslow
    bla "After reaching yet another climax, this time in perfect sync with you, Dalia collapses onto the floor, trembling and wheezing like someone pulled from the brink of drowning." with dis22
    play music2 arabiarelax fadein 9
    d "*Gasping for air* Aaahh... aaaaghhhh... aahhh... aaaagh..." with dis22
    play sound4 clothes3
    scene gd 119 with dis2
    play sound5 fallfull volume 0.6
    scene gd119
    pause 0.01
    mc "*Sitting down* Boy..." with dis12
    mc "I-I need... a m-minute..."
    show daliacit19 
    d "I need..."
    d "An hour..."
    mc "*Chuckles* O-On second thought, I might need that too..." 
    d "*Still gasping* W-What on Earth just fucking happened...?"
    mc "I-I'm not even sure yet."
    d "I think I just reached Nirvana."
    d "Or... like, the Arabian version of it, I don't know."
    mc "*Chuckles* Arabian Nirvana?"
    d "Yeah..."
    d "I saw... a radiant oasis filled with gold, dates, and camels wearing tiny hats."
    mc "*Laughs* Tiny hats?"
    d "Yeah, like... small fedoras."
    d "One of them even tipped it and said, “M'lady”."
    mc "*Chuckles* I'm pretty sure that's not how Nirvana works, but hey, I won't question your version of enlightenment."
    $ renpy.end_replay()
    scene gd 119
    mc "Was I in your majestic oasis, at least?" with dis
    scene gd 120
    d "Of course..."
    play sound2 clothes3
    play sound clothes
    scene gd 121b
    bla "Dalia awkwardly crawls towards you." with dis25
    scene gd 121
    d "*Deep exhale* If you hadn't been there, it wouldn't have been an oasis..."
    show gd 122
    mc "You sound exhausted, Dalia."
    show gd 121
    d "Hell, I am..."
    d "And not only... {i}there{/i}. My whole body feels like I just got run over."
    show gd 122
    mc "Well, I'm glad to hear that..."
    show gd 121
    d "You've basically ruined my gym sessions for the next two days, at least. Hope you're happy."
    show gd 122
    mc "Hey, it's not my fault you came so hard every single time. And so many times, too..."
    mc "How many was it, anyway?"
    show gd 121
    d "My god, I don't know. I lost the ability to count after the second one."
    show gd 122
    mc "You got noisier and messier each time."
    show gd 121
    d "Because every time it felt better than the last..."
    show gd 122
    mc "Maybe you have, like, a... hypersensitive vagina or something?"
    mc "Is that a thing?"
    show gd 121
    d "I dunno, I'm not an orgasm scientist."
    d "I just thank God for making me a woman. Imagine only being able to cum once and then going all Floppy Joe and having to stop."
    d "What a curse..."
    show gd 122
    mc "Some girls can't even continue immediately after orgasming like you do, you know?"
    mc "They get too sensitive for a bit."
    show gd 121
    d "Well, I don't know, then I just thank my mom for making me the way I am."
    show gd 122
    mc "*Chuckles* Ah, I'll give you that."
    mc "Nancy definitely knew what she was doing during those nine months she had you cooking."
    show gd 121
    d "*Deep exhale* Aaahhh..."
    d "This was... amazing, [mc]. Everything was... so perfect." 
    show gd 122
    mc "It really was."
    mc "We... connected. As if we had been lovers for years."
    show gd 121
    d "We're gonna do it again, right?"
    show gd 122
    mc "Of course..."
    show gd 121
    d "I know today we took it slow, but next time I'll–"
    show gd 123
    mc "I'm sorry, we took it... WHAT?"
    mc "You're joking, right?"
    show gd 124
    d "My legs failed me when I was squatting on you!"
    d "That was totally unacceptable. I haven't been training my glutes at the gym for the past 8 years for this."
    d "I'll train even harder from now on!"
    d "And next time... I'm gonna be up to the challenge."
    show gd 123
    mc "Is this a competition now?"
    show gd 124
    d "Kinda. And this time, I'm going for that gold medal..."
    show gd 123
    mc "Oh my..."
    mc "Well, consider me in–"
    stop music2 fadeout 4
    play music2b arabia4
    play sound knock3
    show gd 125
    if jerryfriend:
        je "[mc]?! Are you in there?!" with dis 
    else:
        sam "Hello?!" with dis 
    play sound chair2
    stop soundloop2
    scene gd 126
    if jerryfriend:
        mc "*Standing up* Wait, is that... Jerry?" with dis12
    else:
        mc "*Standing up* Wait, is that... Samir?" with dis12
    d "*Whispers* I think so...?"
    play sound knock3
    if jerryfriend:
        je "[mc]?!" with hpunch 
        je "Oh no... I fear the worst."
        je "Step aside, I'll bust the door down!"
        mc "W-Wait, don't bust anything, I'm here!"
        je "*Gasps* He's alive!"
        je "But he needs the password, of course... What was it?!"
        is2 "Free Sands?"
        je "Agh, there's no time for this – the guards are almost here!"
        je "I'll break the door down!"
        is2 "I just told you!"
        mc "G-Goddammit, wait, WAIT! I'm opening!"
    else:
        sam "Fuck, why is it locked from the inside?!" with hpunch 
        sam "Hello?!"
        mc "You asked us to lock it yourself, dumbass!"
        sam "Oh..."
        sam "Right, the password thing..."
        sam "Uh... it was..."
        sam "Ah! F-Free Sands! Yeah!"
        d "*Whispers* Is that correct?"
        mc "*Whispers* Yeah, that's the one he told us."
        sam "The guards are all over the place, please!"
        sam "Shit, I'm gonna break the door down!"
        mc "Wait, wait, DON'T! I'm opening!"
    play sound2 lock
    play sound doorold
    if jerryfriend:
        scene gd 135
        bla "As you open the door, Jerry rushes in with an Ishari girl, gasping for breath." with dis2
        je "*Panting* O-Oh god, that was so close..."
        mc "Jerry? What the hell is going on?!"
        play sound clotheswhoosh
        show gd136
        je "I've come to warn you, General!" with vpunch 
        scene gd 137
        mc "W-What? Warn me about what?"
        mc "What's going on? And who's this girl?"
        show gd 136
        je "I successfully..."
        show gd 138
        je ". . ." (multiple=2) with dis
        is2 ". . ." (multiple=2)
        play soundlow whoosh3b
        show gd 139
        is2 "Oh my god, why is he naked?!" with hpunch
        mc "*Covering yourself* O-Oh... y-yeah, sorry about that, I just..."
        show gd 140
        je "Magnificent instrument, General!"
        show gd 139
        mc "Dammit Jerry, what the fuck do you want?!"
        show gd 139b
        is2 "The guards are coming!" with hpunch 
        show gd 139
        mc "What?"
        show gd 139b
        is2 "Jerry got us out of the incubation rooms, and now the Sultan's sending his giant golems to break into all the houses in the Citadel, one by one!"
        show gd 140
        je "That's right. I ordered the retreat of all our soldiers, but I couldn't leave knowing there was still a chance you might be here."
        je "Now that I've warned you, we can retreat as well!"
        show gd 139
        mc "You... ordered...?"
        show gd 140
        je "Indeed! I am the new leader of the Ishari!"
        show gd 139
        mc "Um..."
        mc "I'm getting lost."
        show gd 139b
        is2 "It's true! I saw Samir name him our new Leader when we found him trying to escape!"
        is2 "He said he was quitting!"
        show gd 140
        je "As you hear it!"
        show gd 141
        je "Ain't gonna lie, I... kinda feel like he only made me the new Leader because I just happened to be the one stumbling across him at that exact moment."with dis
        show gd 140
        je "But either way, I'll make sure to honor this new title!" with hpunchsubtle
        show gd 139
        mc "Um..."
        mc "I'm confused, and I have a ton of questions, but... maybe we should save them for later, whenever we're safe."
        mc "Go find shelter before the guards arrive, we'll also leave immediately."
        show gd 140
        je "We shall, General."
        show gd 142
        je "Take a good look at this man and his penis, Pam."with dis
        show gd 143
        je "Yes, I was once the greatest mage Eternum had ever known... and no, he’s not quite on par with Sir Jermaine of Noriander just yet."
        show gd 140
        je "But, if there’s a man who can someday surpass me and become the new King of Eternum..."
        je "If there’s {i}anyone{/i} capable of gathering the 10 Gems of Doom and claiming the throne of Eternum..."
        je "IT'S HIM."
        show gd 139
        mc "Wow."
        mc "That last part sounded so out of character coming from you, Jerry. Did you hit your head or something?"
        show gd 140
        je "You saved my life, [mc]."
        je "And more than that... you gave me a purpose. Something to live for."
        je "I shall never forget it."
        show gd 139
        mc "Oh, uh... y-you're welcome."
        show gd 143
        je "But enough talk!" with hpunchsubtle 
        je "Tell the Empress that the Ishari are now in service to the WRE!"
        show gd 142
        je "And Pam, spread the word to your people! Tell them that [nickname] is the man who freed them and will give them their server back!"
        show gd 139b
        is2 "O-Okay!"
        show gd 140
        je "Farewell, friend."
        je "And don't stay for too long. Make sure to leave before those monsters arrive!"
        show gd 139
        mc "We'll leave right now."
        mc "Thank you for the warning, Jerry."
        mc "And please, be careful."
        je ". . ."
        show gd 144
        je ". . ." with dis
        show gd 145
        d ". . ."
        show gd 144
        je ". . ."
        show gd 145
        d ". . ."
        show gd 146
        d "...Jerry."
        show gd 147
        je "...D-Dalia."
        show gd 145
        d ". . ."
        show gd 144
        je ". . ."
        play soundlow inhale2
        show gd 148
        je "*Taking a deep breath* MMMmmmmmmmhhh..." with dis12
        show gd 149
        je "{i}*Faint voice* I'm not gonna lie. This hurts."
        je "{i}*Faint voice* A lot."
        je "{i}*Faint voice* I knew, but... it certifies my defeat."
        show gd 148
        mc "Um..."
        show gd 149
        je "{i}*Faint voice* But losing to the future King of Eternum is no shame."
        je "{i}*Faint voice* So."
        je "{i}*Faint voice* I will leave now."
        je "{i}*Faint voice* I will cry."
        je "{i}*Faint voice* And I'll come back stronger."
        show gd 148
        mc "Uh... o-okay. Sounds good."
        show gd 149
        je "{i}*Faint voice* Goodbye, General."
        show gd 148
        mc "G-Good luck, Jerry."
        je ". . ."
        play sound doorold
        show gd 150 with dis2
        mct "Okay..." with dis12
        mct "T-That was awkward."
    else:
        scene gd 127
        bla "As you open the door, Samir rushes in, gasping for breath." with dis2
        sam "*Panting* F-fuck, that was close..."
        mc "Is everything okay...?"
        play sound clotheswhoosh
        show gd128
        sam "We need to leave immediately!" with vpunch 
        scene gd 129
        mc "What?! Why?"
        show gd 128
        sam "The guards are..."
        show gd 130
        sam ". . ." with dis
        show gd 131
        sam "Uh..."
        sam "You're..."
        show gd 130
        mc "*Covering yourself* U-Um... y-yeah, I know."
        mc "You caught us at a bad time."
        show gd 131
        sam "Oh."
        show gd 132
        sam ". . ."with dis
        show gd 145
        d ". . ."
        show gd 132
        sam ". . ."
        show gd 133
        sam "...Miss Dalia."
        show gd 146
        d "Samir."
        show gd 132
        sam ". . ."
        show gd 131
        sam "Lucky bastard..." with dis
        show gd 130
        mc "A-Anyway, we need to leave immediately, you said??"
        show gd 131
        sam "Yeah, so... as I was saying..."
        sam "The guards are starting to break into all the houses in the Citadel."
        sam "Hassan al-Rashid won't... stop... until he... finds..."
        show gd 130
        mc "*Still covering yourself* Can you stop staring at my dick?!" with hpunch 
        mc "What about the guards?!"
        show gd 131
        sam "Y-Yeah, sorry, the guards..."
        show gd 128
        sam "Shit, YES!" with dis08
        sam "The entrances to the Citadel are blocked, and now they're raiding all the houses, one by one!"
        if jerrypalace:
            sam "I even saw one of them kill your friend in such a brutal way!"
            show gd 129
            mc "Oh no, Jerry..."
            show gd 128
            sam "They'll soon be here! We only have a few minutes left!"
        else:
            sam "They'll soon be here!"
        show gd 129
        mc "Damn, really?"
        mc "Hmph... I guess it's finally time to get the hell out of here, then."
        mc "Thank you, Samir."
        mc "Did you really come back here just to warn us...?"
        show gd 128
        sam "OF COURSE!"
        show gd 129
        mc "Really...?"
        sam ". . ."
        show gd 133
        sam "Well, also needed to grab my opium bag."
        sam "That shit's expensive, y'know."
        show gd 132
        mc "I knew it..."
        mc "Well, thanks in any case, I suppose."
        show gd 128
        if not jerrypalace:
            sam "What I said earlier at the palace still stands, man."
            sam "The Ishari are yours. I'm so out."
        else:
            sam "Man, I'm not fit to be the leader of anything."
            sam "I quit. I'm so out."
            sam "Tell the Empress that she can take control of everything! Or... you can!"
            sam "I officially name you the new Leader of the Ishari!"
        sam "I'll send some eagles to the main lieutenants to let them know."
        show gd 129
        if jerrypalace:
            mc "Uh... w-what? I don't..."
            sam ". . ."
            mc "*Sighs* Yeah, whatever... okay, we'll... I'll see what I can do."
        else:
            mc "*Sighs* Yeah... okay, I'll... I'll see what I can do."
            mct "I guess I've got no other choice."
        show gd 128
        sam "They'll do much better under your leadership."
        sam "Good luck, friend."
        sam "And don't hang around too long, or those monsters will find you!"
        show gd 129
        mc "We won't."
        mc "Good luck, Samir."
        play sound doorold
        show gd 134 with dis2
        mc "*Sighs* (Leader of the Ishari.)" with dis12
        mct "As if I didn't have enough headaches already..."
    show gd 151
    if jerryfriend:
        mc "But, well, in any case... Jerry's warning was legit." with dis15
    else:
        mc "Well... you heard the man." with dis15
    mc "It's time for [mc]'s Express Departure."
    mc "We'll have to report back to Nancy and figure out our next move."
    mc "At least now we know what Hassan's up to. It shouldn't be too complicated to dismantle his Xenomorph farms and win the event."
    show gd 152
    if jerryfriend:
        d "The future King of Eternum, damn..."
        d "That's quite the title. What's your secret to climbing the rankings like that?"
    else:
        d "Leader of the Ishari, damn..."
        d "That sure was a meteoric rise in rankings. What's your secret?"
    d "Is it just charisma?"
    show gd 151 
    mc "*Chuckles* What can I say, I've got that natural magnetism."
    show gd 152
    d "Indeed, you do..."
    d "Will you forget about me when you're at the top as King [mc] and the new CEO of Ulysses?"
    show gd 151
    mc "Not a chance."
    mc "Get used to my face, girl, you're stuck with it for life."
    show gd 152
    d "Oh, wow... I really am a lucky girl."
    show gd 151
    mc "I could say the very same..."
    show gd 152
    d "*Giggle* Alright! We can go!"
    d "Just let me find something to wear before going back to Kredon first."
    d "I wouldn't want to scandalize anyone."
    show gd 151
    mc "*Chuckles* You won't catch me agreeing to you wearing more clothes too often, but fair enough."
    jump arabialogoff
    
    


label arabialogoff:
    stop music3 fadeout 7
    stop music2b fadeout 7
    stop soundloop fadeout 8
    stop soundloop3 fadeout 8
    play soundloop2 rain5 fadein 6
    hide screen sometimelater
    scene gv 1 
    with Dissolve(3.5)
    play sound8 carpasswet
    pause
    play sound teleport2
    play sound2 splash2
    scene gv 2 with flashfaster
    play music chillmagic fadein 5
    pause 
    mc "*Opening your eyes* Ahh, thank god..." with dis15
    mc "I've never been happier to see Kredon's rain."
    if daliapath:
        mc "This place might be cold, but damn, it really screams... “home”."
        play sound3 water5
        show gv 3
        d "*Grabbing her umbrella* I'm sorry? Are we talking about the same place where you got shot, like, a week ago?" with dis17
        d "{i}That{/i} home?"
        show gv 4
        mc "*Chuckles* Okay, in Kredon's defense, that just happened because I have a bad habit of sticking my nose where it doesn’t belong."
        mc "Not to mention how careless I was."
        show gv 3
        d "*Giggles* That's true. Fair enough."
        show gv 4
        mc "If you were trying to pull that rhetoric to convince me to bring you into Eternum with your real body again, forget it, miss."
        mc "If anyone's gonna put their life on the line from now on, it's gonna be me and only me."
        show gv 3
        d "*Chuckles* Alright, alright..."
        d "I won't insist, I promise."
        show gv 4
        mc "And speaking of putting your life in danger, you better get home quick before you freeze to death out here!"
        show gv 3
        d "Oh, no need to tell me twice!"
        d "I plan to take the longest, hottest shower of my whole life."
        play sound5 dogfar
        d "You said you had to go back to Eternum, right?"
        show gv 4
        mc "Yeah, but it shouldn't take me long."
        mc "I’ll go say hi to Calypso in Ekabar, then I’ll meet you all back home."
        show gv 5
        d "Oh, how convenient... leaving me alone to deal with all the awkward questions on my own."
        show gv 4
        mc "Hmm? You mean the Ishari outfit?"
        mc "Everyone in the group already knows about my new “power”. Just tell them it was life or death, and you had no choice but to come in with me."
        mc "And if some rando asks on the way home, you can just say it's a cosplay for a convention."
        show gv 5
        d "Heh, yeah, that wouldn't even stand out that much."
        d "It's not like we're short on Eternumites in this town."
        show gv 3
        d "But that's not what I meant."
        d "I was talking about what just went down at the den."
        d "What am I supposed to say when Mom or Penny see me walking funny?"
        d "You really made a mess of me... {i}brute."
        show gv 4
        mc "*Chuckles* Oh, I see..."
        mc "I thought that's how you liked it."
        show gv 3
        d "Oh, I do... but that doesn't avoid awkward questions."
        show gv 4
        mc "You're a smart girl... I'm sure you'll figure something out."
        d "Mm-hm..."
        show gv 5
        d "Thanks again for everything today, [mc]..."
        d "You made all the... well, you know, a-all the waiting worth it."
        d "It really was... WOW."
        show gv 4
        mc "*Chuckles* I've gotta agree, that was pretty “wow” indeed."
        play sound water5
        show gv 6
        d "*Taking a step back* Anyway, stop letting me hold you up!" with dis17
        d "Go, go! See you later!"
        mc "See you in a minute!"
        mc "*Closing your eyes* Love you."
        d "*Giggles* L-Love you too."
        play sound teleport2
        show gv 7 with flashfaster
        pause
        play soundlow water5
        show gv 8
        d "*Happy giggle* Mm-hm-hm..." with dis2
        d "Mmmmmh..."
        d "(I have to buy a new jacket. And new pants.)"
        d ". . ."
        d "(And I {i}have{/i} to tell someone about this. How am I supposed to keep quiet after what just went down?!)"
        show gv 9
        d "(But... who though...?)"
        d "(Hmm...)"
        d "(Logical choice would be Alex.)"
        show gv 8
        d "(Hmm, yeah.)"
        d ". . ."
        show gv 10
        d "(Or maybe Sissy too...?)"
        d "Hmmm..."
    else:
        d "Can I open my eyes now?"
        mc "Yep! We did it!"
        d "Oh, thank fucking god..."
        mc "No more desert, no more giant jackals, no more danger."
        mc "*Sighs* This place might be cold, but it really feels like home."
        d "Are we talking about the same place where you got shot, like, a week ago?"
        d "{i}That{/i} home?"
        mc "Okay, touché." (what_style='textsp')
        play sound water5
        show gv 6
        mc "Anyways... I'm relieved knowing you're now safe. See you at home, Dal!" with dis2
        d "Huh? Where are you off to now?"
        mc "I'm gonna say hi to Calypso and then meet you all back at home."
        d "Now?? Jeez, you sure are a wandering spirit."
        mc "That's me!"
        d "Fine, whatever... I'll let the others now."
        mc "Wanna race to see who gets home first? Loser buys the snacks!"
        d "Nah, thanks, I'm good."
        mc "Pfft, fine, fine..."
        mc "Catch you later, then!"
        play sound teleport2
        show gv 7 with flashfaster
        pause
        d "I'm totally winning this race..." with dis 
    stop soundloop2 fadeout 6
    play sound2 wind4
    scene gv 11 with Dissolve(3.5)
    pause
    play sound snow4
    show gv 12 with dis17
    mc "*Shivers* (By Odin's frozen balls...)" with dis15
    mct "I-It was not the best idea to show up here with this “outfit”."
    mct "Coming to Ekabar straight from Valley of Kings feels like a slap in the face."
    play sound2 clothes3
    show gv 13
    mc "Although..." with dis17
    mct "Well, at least this inn seems to hold the heat pretty well."
    mct "I wonder if it’s just the thick stone walls or if there’s some magic at play."
    show gv 14
    player "*Laughs* Oh, I know, I know!" with dis12
    player "I'm gonna put live music in here!"
    player2 "*Hic* Oh, yeah, yeah! I can play!"
    play sound stairswood
    show gv 15 with dis17
    mc "*Getting closer* Huh...?" with dis12
    mct "Calypso drinking with other players...? That's certainly not what I was expecting to stumble upon."
    player "And now... anudda toast to Princessss Calypso of the... uh, Hiriar Realm!"
    player "D-Did I... did I get that right?" 
    show gv 16
    mc "Almost. It's... Hyril'ar Realm." 
    show gv 17
    ca "Ah! [mc]!" with dis12
    if calypsotogether:
        ca "This is the friend I mentioned before!"
    ca "What brings you to this place?"
    show gv 18
    mc "I just wanted to drop by and see you."
    mc "I know you said not to bother you, but it’s been a few days since I saw you, and I was worried you might be pushing yourself too hard with that Elarisil ritual."
    show gv 17
    ca "Oh, do not fret over me."
    ca "I... I failed again in my search for a way back to Hyril'ar."
    ca "So today I decided to spend some time among the common folk, hoping it would help clear my mind."
    show gv 19
    ca "These are my new human companions!" with dis
    ca "She is... Arwen."
    show gv 20
    player2 "Gwen."
    show gv 21
    ca "And... Fyrandoriel...?"with dis 
    show gv 22
    player "Uh... John, but close enough."
    show gv 21
    ca "Ah, yes. Hmm, human names are so difficult to remember."
    show gv 18
    mc "*Chuckles* Well, I'm glad to see you're doing well."with dis12
    show gv 17
    ca "Thank you!"
    show gv 22
    player "Glad to meet you, [mc]." with dis
    if calypsotogether:
        player "Princess can't stop talking about you."
        show gv 21
        mc "Is that so..."
    else:
        show gv 21
        mc "Thank you, John!"
    show gv 22
    player "You and all of Lady Calypso's friends got a lifetime open bar in my inn!"
    player "An' you can tell Alexandra she don’t owe me a coin no more!"
    player "All debts... forgiven!"
    show gv 21
    mc "Wait... seriously?"
    mc "Thank you!"
    play sound6 clothes3
    play soundlow sword fadein 1 volume 0.6 
    show gv 22b
    player "And take this sword too! Forged by the greatest blacksmith in Ekabar!" with dis15
    player "It was meant for my son one day, but... fuck 'em kids."
    player "It's yours!"
    show gv 21b
    mc "Um..."
    mc "A-Are you sure?"
    show gv 22b
    player "Absolutely!"
    show gv 21b
    mc "Erm..."
    play sound6 clothes3
    play soundlow sword fadein 1 volume 0.6  
    show gv 21
    mc "*Grabbing the sword* Thanks." with dis14
    mct "I'll return it whenever he's sober..."
    mc "Are you sure this isn't a bit too much?"
    show gv 22
    player "She turned two dozens of barrels of dirty water into premium ale, lad!" 
    player "PREMIUM! I ain't never drank somethin' better, not in my whole life!"
    player "She's like Jesus Christ, but with more... elf. And huge breasts."
    show gv 21
    mc "Oh, wow."
    show gv 22
    player "I gotta go now, but you can stay here at the inn, no worries."
    player "I'll be back in some hours. Gotta take a nap."
    show gv 21
    mc "*Chuckles* Thank you, Sir."
    show gv 20
    player2 "See ya later, Princess!"
    show gv 19
    ca "Safe travels."
    show gv 23 with dis22
    play sound2 doorecho
    bla "Both players stumble out of the old tavern, swaying with each step and belting out a lively song." with dis17
    mc "Well, well, well..."
    mc "Never thought I'd see you drunk, Princess."
    show gv 24
    ca "What? I... I have no idea what you mean."
    ca "I am not the least bit intoxicated."
    show gv 23
    mc "You might still speak as correctly as always, but your nose is all red."
    mc "It's so adorable."
    show gv 24
    ca "Nonsense."
    show gv 23
    if not calypsotogether:
        mc "*Chuckles* By the way, I noticed you're reusing the outfit from the Western server."
    else:
        show gv 23
        mc "What would the royal court say if they caught you sharing drinks with human commoners?"
        mc "I bet they'd be scandalized."
        show gv 24
        ca "Firstly, I said I am not intoxicated."
        ca "And secondly..."
        ca "Well, that is not even the most questionable thing I have allowed a human to do in my presence."
        ca "Or... shall I remind you that I touched you... there, during our visit to that arid realm teeming with horses?"
        show gv 23
        mc "There's no need to remind me at all, my Princess, trust me..."
        show gv 24
        ca "By Turska's mercy, I... I allowed you to see me unclothed!"
        ca "Do you have any idea what they would do to you if this were discovered?!"
        ca "Or to me! They would confine me to the castle for no less than a decade!"
        show gv 23
        mc "Well, in that case we'll just have to keep it a secret."
        ca "Hmph."
        show gv 24
        ca "Yes... I appreciate your discretion."
        show gv 23
        mc "And speaking of the Western server, I noticed you're reusing the outfit you used there."
    mc "Gotta say, it looks amazing on you."
    show gv 25
    ca "Oh, thank you! I am, indeed." with dis
    ca "I thought it would be rather fitting to wear human attire, to better blend in with the commoners."
    show gv 24
    ca "I must begin to accept that... it may take longer than I anticipated to find my way back to my realm, so I should grow accustomed to living among your kind."with dis
    show gv 23
    mc "*Chuckles* That's not exactly how it works, since we're not supposed to wear the same stuff in different servers, but it's still a solid effort."
    mct "Man... I kinda feel bad for her."
    mct "I can’t bring myself to tell her, but... the more I think about it, the clearer it becomes that Hyril'ar might not exist."
    mct "She's obviously not a regular NPC, but... she's not human either."
    mct "Whether she was “created” or not... all the servers in Eternum are filled with either monsters, real players, or NPCs that were once alive."
    mct "And just like those NPCs... she could have... fabricated memories."
    mct "God, finding out something like that would break anyone."
    show gv 24
    ca "W-What is it that you are staring at?"
    show gv 23
    mc "I have a proposition!"
    mc "Alex, Annie, and I were thinking of inviting you tomorrow for an adventure in Andromeda, an outer space server."
    mc "Now, I know it's probably not what you're used to, and you might be tied up with the Elarisil, but–"
    show gv 26
    ca "Oh, that sounds wonderful!" with dis12
    ca "I would be delighted to join you."
    show gv 27
    mc "Really?"
    mc "Sweet! That took less convincing than I thought."
    show gv 26
    ca "Is that one of those realms of metal and artificial lights?"
    show gv 27
    mc "It is!"
    mc "You'll see, we've got a couple of surprises prepared."
    show gv 26
    ca "Fascinating..."
    show gv 28
    mct "I'll never get tired of watching Calypso react to everyday stuff like a kid." with dis15
    mct "It makes me happy to see her smile."
    play sound doorwindclose
    scene gv29 
    pause 2.3
    bla "A gust of wind slams the doors of the old inn with an echoing bang." with dis15
    mc ". . ."
    scene gv 30
    mc "Hmph." with dis
    play sound riserfast
    stop music fadeout 4
    play soundloop windhouse fadein 5
    show gv 31 with dis3
    pause
    show gv 32 with dis15
    pause
    play soundloop2 deception fadein 1
    $ renpy.music.set_volume(0.33, channel='music3')
    play music3 twinkle fadein 30
    scene gv 33 with dis25
    pause
    play sound2 wood2 volume 0.4
    show gv 34 
    mc ". . ." with dis17
    mc "Why..."
    show gv 33
    mc "Why are you here?" with dis14
    id ". . ."
    show gv 38
    id "You're still not asking the right questions, [mc]."
    play sound2 wood2 volume 0.4
    show gv 35
    ca ". . ." with dis14
    show gv 36
    ca "Uh... are you alright?"
    show gv 34
    mc "You don't see her?"
    show gv 36
    ca "See her?"
    show gv 37
    ca ". . ."with dis
    show gv 36
    ca "Um... see... who, exactly?"with dis
    show gv 33
    mc "No..." with dis15
    mc "You're not real." 
    mc "The real Idriel is just a creation of the Founder. You're only in my head."
    mc "You can't be here."
    id ". . ."
    show gv 38
    id "Imagine... two identical glasses, falling in unison, shattering on the floor."
    id "They are perfect replicas, identical in every way – down to the last molecule."
    id "The floor beneath them is the same, the conditions are unchanged. No wind, no variables, no difference in force as they hit the ground at the exact same moment."
    id "And yet..."
    id "Their shards scatter in completely different patterns across the floor."
    id "As though there was a hidden chaos... capable of reshaping the same story."
    show gv 33
    mc "What are you talking about...?"
    mc "I'm seriously not in the mood for your cryptic nonsense right now."
    show gv 39
    id ". . ." with dis17
    id "Oh, [mc]..."
    id "Why is it... that every time everything seems to fall into place, when life feels like it's finally perfect..."
    id "It all shatters in the blink of an eye?"
    show gv 34
    mc "What...?"
    id "It’s as if the very chains of fate were relentlessly trying to drag you back to the void from which you came."
    show gv 39
    id "And yet... you keep resisting." with dis17
    id "Time and time again..."
    id "You always end up... finding a way."
    show gv 40
    id "I do wonder... will this time be any different?" with dis17
    mc ". . ."
    mc "I don't know what you–"
    play music drums fadein 6
    play sound riser
    show thanatosattack with dis
    pause 2.85
    stop music3
    stop soundloop2
    stop soundloop
    play sound2 debris4 
    play sound3 speed
    show gvtrans1 with hpunch 
    pause
    play sound4 chain
    play sound5 chain2
    play sound6 chain3
    play sound7 debris4 volume 0.7
    play sound8 impactwood
    scene gvtrans1b
    bla "As you barely manage to avoid Thanatos' fatal strike, three dimeritium chains are violently hurled at Calypso." with hpunch 
    play sound chain3
    ca "W-What is this?!" with hpunch
    ca "Why... why can't I use my magic?!"
    play sound3 chain3
    ca "No, no, no... NOT THIS AGAIN!" with hpunch 
    mct "F-Fuck... that's the same thing she had on her neck when we found her..."
    play sound2 footstepsheavy
    play soundlow sigh
    show gv 43
    tha ". . ." with dis22
    show gv 44
    mc "We meet again... Thanatos." with dis14
    show gv 43
    tha ". . ."with dis14
    tha "You dodged my attack. Impressive."
    show gv 44
    mc "I've been training since the last time we saw each other."
    show gv 43
    tha "Hmph."
    tha "I can respect the resolve of a warrior."
    tha "Give me the Gems of Doom... and I might spare your life."
    show gv 44
    mc "The Gems..."
    mc "What do you even want them for?"
    mc "I know you're not planning to give them to the Founder either."
    show gv 43
    tha "I am not here to answer your questions."
    tha "This is your final warning."
    tha "Give me the Gems... or die."
    show gv 44
    mc "Wait! Listen to me!"
    mc "I can help you!"
    mc "Maybe we don't have to–"
    play sound speed
    scene gvtrans2
    pause 1.1
    play sound2 swordclash
    scene gv46 with hpunchlong3
    play soundloop swordclashloop fadein 3
    mc "{sc=1}(F-Fuck...){/sc}" with dis12
    mc "{sc=1}(H-He's still too fast for me...){/sc}"
    mc "{sc=1}(I...){/sc}"
    mc "{sc=1}(I can't beat him... There's just no way...){/sc}"
    tha "You've managed to dodge and block two of my attacks at full strength..."
    tha "I'll admit it, you truly are strong."
    mc "{sc=1.5}G-Ggghhhh...{/sc}"
    tha "Unfortunately for you..."
    tha "{sc=3}{size=44}NOWHERE NEAR STRONG ENOUGH.{/sc}" with hpunch
    stop soundloop
    play sound6 fms
    play sound8 whoosh6
    play sound7 bonebreak
    scene gvtrans3 with hpunch 
    pause
    play sound clotheswhoosh
    play sound2 rocks
    play sound3 crashwood
    scene gvtrans4 with hpunch 
    pause 0.5
    play sound4 crashwood
    play sound5 wood2
    scene gv 49 with dis2
    play sound6 blood2
    mc "*Coughing up blood* AAghh..." with dis12
    mc "*Wheezing* (G-God, that felt like a fucking cannon...)"
    mc "*Gasping for air* (I... can't... b-breathe...)"
    play sound footstepsheavy
    play soundlow sigh
    show gv 50
    tha "Most men would be dead by now after a blow like that." with dis2
    mc "(I-I can't even get up...)"
    mc "(He broke my ribs with... a single kick...)"
    mc "(Is this... is this really it?)"
    mc "(Is this... the end...?)"
    play sound2 sword2
    show gv 51
    bla "Thanatos raises your head, his sword tilting your chin upward." with dis15
    tha "You will be remembered when we build a better world, soldier."
    mc "Your..."
    mc "Y-Your mother's still waiting for you to come home, you know?"
    tha ". . ."
    tha "What?"
    mc "I... I know who you are, Wyatt."
    mc "Or... who you used to be."
    tha ". . ."
    tha "That man... is dead."
    tha "I am Thanatos now. Nothing more."
    tha "Goodbye... [nickname]."
    play sound2 earthquake2 fadein 3
    $ renpy.music.set_volume(0.7, channel='soundloop3')
    scene gv52 with dis22
    play soundloop3 earthquakeloop fadein 4
    pause
    scene gv52b with dis15
    pause
    play sound6 leathershort
    scene gv53
    tha "{sc=1.5}. . .{/sc}" with dis15
    scene gv54
    ca "{sc=1.5}Y-You will not... ensnare me...{/sc}" with dis15
    scene gv53
    tha "{sc=1.5}That's...{/sc}"
    tha "{sc=1.5}Impossible.{/sc}"
    tha "{sc=1.5}You're bound by dimeritium.{/sc}"
    scene gv54
    ca "{sc=1.5}Release me at once... or I shall destroy it all.{/sc}"
    play sound2 chain3
    ca "{sc=1.5}This is your final warning!{/sc}" with hpunch 
    scene gv53
    tha "{sc=1.5}You would kill us all?{/sc}"
    play sound chain3
    scene gv54
    ca "{sc=3}I will not be chained ever again!{/sc}" with hpunch 
    scene gv53
    tha "{sc=1.5}. . ."
    tha "{sc=1.5}You don't have the power...{/sc}"
    tha "{sc=1.5}Nor the resolve to carry out your threats.{/sc}"
    show gv54
    ca "{sc=3}DO NOT TEST ME!{/sc}"
    scene gv53
    tha "{sc=1.5}Then act. Prove me wrong.{/sc}"
    tha "{sc=1.5}Are you really willing to sacrifice this man?{/sc}"
    show gv55
    ca "{sc=3}*Rapid breathing* . . .{/sc}" with dis2
    scene gv53
    tha "{sc=1.5}As I expected.{/sc}" with dis15
    tha "{sc=1.5}You're nothing... but a pathetic, weak being.{/sc}"
    scene gv52
    tha "{sc=1.5}A tool... forged to serve.{/sc}"with dis15
    mc "{sc=1.5}C-Calypso...{/sc}" 
    scene gv55
    tha "{sc=1.5}Created... to obey.{/sc}" with dis17
    tha "{sc=1.5}To bow.{/sc}"
    tha "{sc=1.5}To serve its purpose...{/sc}"
    tha "{sc=1.5}...and nothing more.{/sc}"
    play sound calypsoboom
    scene calysnap2
    show calysnap 
    ca "{sc=4}. . .{/sc}{w=3.7}{nw}"
    hide calysnap
    pause 0.08
    stop music
    stop soundloop3
    scene black with flashfastest
    pause 
    play soundloop forest2 fadein 3
    bla ". . ." with dis22
    $ renpy.music.set_volume(0.5, channel='soundloop3')
    play soundloop3 river fadein 6 
    bla "Still disoriented and barely conscious, the icy touch of water soaking your bruised skin slowly wakes you up—a jarring blend of comfort and pain coursing through every inch of your body." with dis15
    scene gv 57 with dis2
    scene black with dis2
    mc "Mmmh..." with dis14
    scene gv 57 with dis2
    mc "A-Aggh..." with dis12
    mct "M-My head..."
    mct "Is spinning..."
    $ renpy.music.set_volume(0.3, channel='music3')
    play music3 hyrilarforest fadein 5
    scene gv 58
    mct "What..." with dis2
    mct "W-What the hell just happened? Where am I?" 
    mct "A forest...?"
    mc "*Coughing up blood* (Shit, I think I've got a few broken ribs...)"
    play sound water
    show gv 59
    mc "*Trying to sit up* Aaagghh..." with dis17
    mct "What is this place...? Am I... still in Ekabar?"
    mct "Fuck, I remember..."
    mct "Thanatos destroyed me in seconds."
    mct "He was about to finish me off, and then..."
    mct "Calypso..."
    play sound2 water4b
    show gv 60
    mct "F-Fuck, I need to find her..." with dis14
    mct "Thanatos might've taken her to–"
    show gv 61
    mc "Huh...?"
    mc "C-Calypso?!"
    play sound water5
    play sound2 water2
    play sound3 water3
    play sound4 drips
    scene gv 63 with dis15
    bla "Struggling to ignore the pain, you push through and quickly cross the small pond, lifting Calypso from the water and cradling her in your lap." with dis14
    show gv 62
    mc "H-Hey, Caly?? Calypso?!"
    mc "Can you hear me? Princess!"
    mc "Please, answer me!"
    show gv 63
    ca ". . ."
    mct "F-Fuck... she has no visible wounds, and she's still breathing, but her heartbeat's so weak..."
    mct "Is she like this because she tried to save me??"
    mct "Did she... cast a portal to get us out of the inn right before everything blew up? All while being chained by dimeritium?!"
    ca ". . ."
    show gv 62
    mc "D-Don't worry, Princess, I'm gonna get us out of here."
    show gv 63
    mct "I-I need to get her to a healer..."
    mct "But where?! I know a place full of druids in Ekabar, but I can't teleport to a specific spot within a server with my power!"
    mct "H-Hmmm... o-okay, I'll take her to Agora, by the Exit Portal, and then ask for help."
    show gv 62
    mc "Hang on, Calypso, you'll be better soon."
    show gv 63
    ca ". . ."
    play sound water
    scene black
    mc "*Closing your eyes* (Alright...)" with dis08
    mct "Agora server..."
    mct "Come on..."
    mc ". . ."
    scene gv 63b
    mc "*Opening your eyes* . . ." with dis17
    mc "What...?"
    scene black
    mc "*Closing your eyes* (Come on, focus...)" with dis
    mct "I've been there before, it's easy..."
    mc ". . ."
    scene gv 63b
    mc "*Opening your eyes* . . ." with dis17
    mct "What the fuck is going on..."
    show gv 64
    mct "Why... why can't I leave?" with dis15
    mct "Why can't I use my powers? Is it because I'm too injured??"
    mct "No... it can't be that..."
    mct "I... I can't even sense Kredon."
    mct "I can't even feel the–"
    mc ". . ."
    show gv 65
    mc ". . ." with dis12
    show gv 66
    aaa ". . ."
    show gv 65
    mc ". . ."
    show gv 66
    aaa ". . ."
    show gv 67
    aaa "F-F-FATHER...?" with dis
    aaa "YOU NEED TO COME HERE."
    show gv 65
    mc "C-Calm down, please."
    mc "We're not gonna hurt you, b-but we need help!"
    show gv 66
    aaa "*Gasps* You can... speak so fluently?"
    show gv 65
    mc "What...?"
    show gv 66
    aaa "The other maids said you could barely speak our tongue... and, you have far less hair than I imagined!"
    aaa "It's... it's not truly her, is it? This is just some human illusion."
    aaa "They always speak of you as deceptive and treacherous."
    show gv 65
    mc "What the hell are you talking about...?"
    mc "What server is this?"
    show gv 66
    aaa "Server?"
    show gv 65
    mc "I mean... w-what server of Eternum?"
    show gv 66
    aaa "Server of..."
    aaa "What's Eternum...?"
    show gv 65
    mc ". . ."
    mc "What...?"
    play sound clotheswhoosh
    play sound2 water2
    play sound3 splash3
    play sound4 drips
    play sound5 draw
    show gv68 with hpunch
    pause 
    scene gv 69
    mc ". . ." with dis12
    play sound water5
    scene gv 70
    aaa "*Taking a step back* By Turska's mercy..." with dis2
    aaa "It's... It's really her..."
    show gv 71
    mct "{i}Her{/i}...?"
    mct "No..."
    mct "It's impossible..."
    mc "Who are you...?"
    show gv 70
    aaa "How do you dare touch the Princess with such filthy hands..."
    aaa "Where do you come from?!"
    show gv 71
    mc "Where am I...?"
    play sound water3
    show gv 70
    aaa "ANSWER ME!" with hpunch 
    show gv 71
    mc "Please..."
    mc "I... I need to know..."
    aaa ". . ."
    aaa "Hmm..."
    aaa "Hmph."
    stop soundloop 
    stop soundloop3
    stop music3
    play sound draw
    play sound2 water2
    play sound3 splash3
    play sound4 ["<silence 0.5>", bird_flying]
    show gv 73
    bla "The elven soldier plants his spear into the mud with such reverence, it seems to hush the entire forest into a breathless stillness." with vpunchslow
    show gv 72
    aaa "A human such as yourself is unworthy of honor or equal treatment."
    aaa "And yet..."
    aaa "It is precisely such mercy that elevates us above your wretched kind."
    aaa "Very well. I shall grant your questions the courtesy they do not deserve."
    aaa "After that, you will be escorted to the castle, where you shall be hanged for what you have done."
    play soundlow inhale2 volume 0.8
    show gv 73
    aaa "*Taking a deep breath* . . ." with dis12
    play music hyrilarclifflong fadein 2
    scene hyri1 with dis25
    ara "{cps=18}I am Arannis Thornvale, General of the Royal Guard, and this is my blood, my daughter... Lorelei.{w=1.2}{nw}" with dis12
    ara "{cps=19}I stand as guardian of the Western Glades, sworn blade to the rightful heir of the throne, Princess Calypso.{w=1.2}{nw}"
    ara "{cps=19}The sole and true descendant of Queen Anima, Heiress of the Sy-tel-quessir, last of her bloodline, Warden of the Eternal Soul, and sovereign of the most powerful and exalted realm upon this continent...{w=1.2}{nw}"
    ara "{cps=9}Hyril'ar.{w=1.3}{nw}"
    show hyri2 
    hide hyri1
    with dis17
    pause 5.2
    play sound leaves volume 0.6
    play sound2 water3 volume 0.6
    lo "And you...?{w=2.2}{nw}" with dissolve 
    jump update09
